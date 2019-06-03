from selenium import webdriver
from selenium.webdriver.common.by import By


class WebDriver:

    driver = webdriver.Chrome()

    def get_element(self, locator_type, locator_value):

        if locator_type == By.ID:
            return self.driver.find_element_by_id(locator_value)
        elif locator_type == By.NAME:
            return self.driver.find_element_by_name(locator_value)
        elif locator_type == By.TAG_NAME:
            return self.driver.find_element_by_tag_name(locator_value)
        elif locator_type == By.XPATH:
            return self.driver.find_element_by_xpath(locator_value)
        elif locator_type == By.LINK_TEXT:
            return self.driver.find_element_by_link_text(locator_value)
        elif locator_type == By.TAG_NAME:
            return self.driver.find_element_by_tag_name(locator_value)
        else:
            return "Locator type " + locator_type + " is invalid or doesn't exist"
