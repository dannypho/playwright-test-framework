import pytest
from pages.login_page import LoginPage
from utils.csv_reader import CSVReader

class TestLogin:
    """Test suite for login functionality"""
    
    def test_successful_login_with_expect(self, page, config):
        """Test using Playwright's expect assertions"""
        login_page = LoginPage(page)
        
        login_page.navigate_to_login()
        login_page.login(config['valid_username'], config['valid_password'])
        
        # Playwright-style assertions (cleaner!)
        login_page.expect_visible(login_page.SUCCESS_MESSAGE)
        login_page.expect_text(login_page.SUCCESS_MESSAGE, "You logged into a secure area")
    
    def test_invalid_username(self, page, config):
        """
        Test login fails with invalid username.
        Verifies error message appears.
        """
        login_page = LoginPage(page)
        
        login_page.navigate_to_login()
        login_page.login("invaliduser", config['valid_password'])
        
        assert login_page.is_error_message_visible(), \
            "Error message not visible"
        assert "Your username is invalid" in login_page.get_error_message(), \
            "Error message text incorrect"
    
    def test_invalid_password(self, page, config):
        """
        Test login fails with invalid password.
        Verifies error message appears.
        """
        login_page = LoginPage(page)
        
        login_page.navigate_to_login()
        login_page.login(config['valid_username'], "wrongpassword")
        
        assert login_page.is_error_message_visible()
        assert "Your password is invalid" in login_page.get_error_message()
    
    def test_empty_credentials(self, page):
        """
        Test login fails with empty credentials.
        Verifies error message appears.
        """
        login_page = LoginPage(page)
        
        login_page.navigate_to_login()
        login_page.login("", "")
        
        assert login_page.is_error_message_visible()
    
    def test_login_with_network_check(self, page, config):
        """Test login and verify API calls"""
        
        # Listen for network requests
        requests = []
        page.on("request", lambda request: requests.append(request.url))
        
        login_page = LoginPage(page)
        login_page.navigate_to_login()
        login_page.login(config['valid_username'], config['valid_password'])
        
        # Verify certain API was called
        assert any("/authenticate" in url for url in requests)
    
    def test_multiple_sessions(self, browser, config):
        """Test with multiple browser contexts (users)"""
        
        # Create two separate contexts (like incognito windows)
        context1 = browser.new_context()
        context2 = browser.new_context()
        
        page1 = context1.new_page()
        page2 = context2.new_page()
        
        # User 1 logs in
        login1 = LoginPage(page1)
        login1.navigate_to_login()
        login1.login(config['valid_username'], config['valid_password'])
        
        # User 2 logs in
        login2 = LoginPage(page2)
        login2.navigate_to_login()
        login2.login(config['valid_username'], config['valid_password'])
    
        # Both should be logged in independently
        assert login1.is_success_message_visible()
        assert login2.is_success_message_visible()
    
        context1.close()
        context2.close()

class TestLoginDataDriven:
    """Data-driven login tests"""
    
    @pytest.mark.parametrize(
        "username,password,expected",
        CSVReader.get_login_data()
    )
    def test_login_with_csv_data(self, page, username, password, expected):
        """
        Data-driven test for login functionality.
        Tests multiple scenarios from CSV file.
        """
        login_page = LoginPage(page)
        
        login_page.navigate_to_login()
        login_page.login(username, password)
        
        if expected == "success":
            assert login_page.is_success_message_visible(), \
                f"Expected success for {username}/{password}"
        else:
            assert login_page.is_error_message_visible(), \
                f"Expected error for {username}/{password}"