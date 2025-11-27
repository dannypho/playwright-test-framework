from pages.checkbox_page import CheckboxPage

class TestCheckboxes:
    def test_check_checkbox(self, page):
        """Test checking a checkbox"""
        checkbox_page = CheckboxPage(page)
        
        checkbox_page.navigate_to_checkboxes()
        checkbox_page.check_checkbox_1()
        
        assert checkbox_page.is_checked(checkbox_page.CHECKBOX_1)
    
    def test_uncheck_checkbox(self, page):
        """Test unchecking a checkbox"""
        checkbox_page = CheckboxPage(page)
        
        checkbox_page.navigate_to_checkboxes()
        checkbox_page.uncheck_checkbox_1()
        
        assert not checkbox_page.is_checked(checkbox_page.CHECKBOX_1)