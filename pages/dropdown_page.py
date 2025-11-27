from pages.base_page import BasePage
from playwright.sync_api import Page

class DropdownPage(BasePage):
    DROPDOWN = "#dropdown"
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    def navigate_to_dropdown(self):
        self.navigate("/dropdown")
    
    def select_option(self, value: str):
        """Select dropdown option by value"""
        self.page.select_option(self.DROPDOWN, value)
    
    def get_selected_option(self) -> str:
        """Get currently selected option"""
        return self.page.input_value(self.DROPDOWN)