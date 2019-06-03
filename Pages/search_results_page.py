from selenium.webdriver.common.by import By
from EnvironmentSetUp.environment import EnvironmentSetUp
from Locators.search_results_page_locators import SearchResultsPageLocators


class SearchResultsPage(EnvironmentSetUp):

    def assert_search_term(self):
        return self.get_element(By.XPATH, SearchResultsPageLocators.locators["_page_heading"]).text
