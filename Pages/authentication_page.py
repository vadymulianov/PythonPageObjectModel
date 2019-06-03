from selenium.webdriver.common.by import By
from EnvironmentSetUp.environment import EnvironmentSetUp
from Locators.authentication_page import AuthenticationPageLocators


class AuthenticationPage(EnvironmentSetUp):

    def click_on_create_an_account_button(self):
        self.driver(By.ID, AuthenticationPageLocators.locators["_create_an_account_button"]).click()
