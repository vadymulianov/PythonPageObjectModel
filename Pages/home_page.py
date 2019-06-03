from selenium.webdriver.common.by import By
from EnvironmentSetUp.environment import EnvironmentSetUp
from Pages.search_results_page import SearchResultsPage
from Pages.authentication_page import AuthenticationPage
from Locators.home_page_locators import HomePageLocators


class HomePage(EnvironmentSetUp):

    def enter_search_term(self, term):
        self.get_element(By.ID, HomePageLocators.locators["_search_text_field"]).send_keys(term)

    def click_on_sign_in_link(self):
        self.get_element(By.LINK_TEXT, HomePageLocators.locators["_sign_in_link"]).click()
        return AuthenticationPage()

    def click_on_search_button(self):
        self.get_element(By.NAME, HomePageLocators.locators["_search_button"]).click()
        return SearchResultsPage()
