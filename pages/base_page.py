from playwright.sync_api import Page, expect
from utils.config_reader import ConfigReader

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = ConfigReader.get_base_url()
        self.timeout = ConfigReader.get_timeout()
    
    def navigate(self, path=""):
        """Navigate to a URL"""
        url = f"{self.base_url}{path}"
        self.page.goto(url)
    
    def click(self, selector: str):
        """Click an element"""
        self.page.click(selector)
    
    def fill(self, selector: str, text: str):
        """Fill a text input"""
        self.page.fill(selector, text)
    
    def get_text(self, selector: str) -> str:
        """Get text from an element"""
        return self.page.text_content(selector)
    
    def is_visible(self, selector: str) -> bool:
        """Check if element is visible"""
        return self.page.is_visible(selector)
    
    def wait_for_selector(self, selector: str):
        """Wait for selector to appear"""
        self.page.wait_for_selector(selector)
    
    def screenshot(self, name: str):
        """Take a screenshot"""
        self.page.screenshot(path=f"screenshots/{name}.png")
    
    def get_title(self) -> str:
        """Get page title"""
        return self.page.title()
    
    def expect_visible(self, selector: str):
        """Assert element is visible (Playwright way)"""
        expect(self.page.locator(selector)).to_be_visible()
    
    def expect_text(self, selector: str, text: str):
        """Assert element contains text"""
        expect(self.page.locator(selector)).to_contain_text(text)
    
    def expect_url(self, url: str):
        """Assert current URL"""
        expect(self.page).to_have_url(url)