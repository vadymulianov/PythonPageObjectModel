import unittest
import HtmlTestRunner
from WebDriver.webdriver import WebDriver


class EnvironmentSetUp(unittest.TestCase, WebDriver):

    @classmethod
    def setUpClass(cls):
        cls.driver.get("http://automationpractice.com/index.php")
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
