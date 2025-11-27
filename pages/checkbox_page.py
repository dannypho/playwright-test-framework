from pages.base_page import BasePage
from playwright.sync_api import Page

class CheckboxPage(BasePage):
    CHECKBOX_1 = "input[type='checkbox']:nth-of-type(1)"
    CHECKBOX_2 = "input[type='checkbox']:nth-of-type(2)"
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    def navigate_to_checkboxes(self):
        self.navigate("/checkboxes")
    
    def check_checkbox_1(self):
        if not self.is_checked(self.CHECKBOX_1):
            self.click(self.CHECKBOX_1)
    
    def uncheck_checkbox_1(self):
        if self.is_checked(self.CHECKBOX_1):
            self.click(self.CHECKBOX_1)
    
    def is_checked(self, selector: str) -> bool:
        return self.page.is_checked(selector)