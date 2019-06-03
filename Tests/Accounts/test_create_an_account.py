from Pages.home_page import HomePage
from Pages.authentication_page import AuthenticationPage


class TestAuthenticationPage(HomePage):

    def test_assert_page_heading(self):

        home_page = HomePage()
        home_page.click_on_sign_in_link()

        authentication_page = AuthenticationPage()
        authentication_page.click_on_create_an_account_button()

        assert "Invalid email address." in self.driver.page_source()