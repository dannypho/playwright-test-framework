from pages.base_page import BasePage
from playwright.sync_api import Page

class LoginPage(BasePage):
    # Locators (using CSS selectors)
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "button[type='submit']"
    SUCCESS_MESSAGE = ".flash.success"
    ERROR_MESSAGE = ".flash.error"
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    def navigate_to_login(self):
        """Navigate to login page"""
        self.navigate("/login")
    
    def enter_username(self, username: str):
        """Enter username"""
        self.fill(self.USERNAME_INPUT, username)
    
    def enter_password(self, password: str):
        """Enter password"""
        self.fill(self.PASSWORD_INPUT, password)
    
    def click_login(self):
        """Click login button"""
        self.click(self.LOGIN_BUTTON)
    
    def get_success_message(self) -> str:
        """Get success message text"""
        self.wait_for_selector(self.SUCCESS_MESSAGE)
        return self.get_text(self.SUCCESS_MESSAGE)
    
    def get_error_message(self) -> str:
        """Get error message text"""
        self.wait_for_selector(self.ERROR_MESSAGE)
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_success_message_visible(self) -> bool:
        """Check if success message is visible"""
        return self.is_visible(self.SUCCESS_MESSAGE)
    
    def is_error_message_visible(self) -> bool:
        """Check if error message is visible"""
        return self.is_visible(self.ERROR_MESSAGE)
    
    def login(self, username: str, password: str):
        """Complete login flow"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()