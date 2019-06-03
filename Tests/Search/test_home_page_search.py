from Pages.home_page import HomePage
from Pages.search_results_page import SearchResultsPage


class TestHomePageSearch(HomePage):

    def test_search_item_valid(self):

        search_term = "Dress"
        # Ideally to compare with DB
        search_results_counter = "7 results have been found."

        home_page = HomePage()
        home_page.enter_search_term(search_term)
        home_page.click_on_search_button()

        search_results_page = SearchResultsPage()

        if self.assertEqual(search_results_page.assert_search_term(), search_results_counter):
            pass
        else:
            self.driver.save_screenshot('ScreenShots/search_results_page.png')




