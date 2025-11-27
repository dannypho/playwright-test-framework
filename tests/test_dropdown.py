from pages.dropdown_page import DropdownPage

class TestDropdown:
    def test_select_option_1(self, page):
        """Test selecting option 1"""
        dropdown_page = DropdownPage(page)
        
        dropdown_page.navigate_to_dropdown()
        dropdown_page.select_option("1")
        
        assert dropdown_page.get_selected_option() == "1"
    
    def test_select_option_2(self, page):
        """Test selecting option 2"""
        dropdown_page = DropdownPage(page)
        
        dropdown_page.navigate_to_dropdown()
        dropdown_page.select_option("2")
        
        assert dropdown_page.get_selected_option() == "2"