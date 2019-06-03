import unittest
import HtmlTestRunner
from HtmlTestRunner import HTMLTestRunner
from Tests.Search.test_home_page_search import TestHomePageSearch
from Tests.Accounts.test_create_an_account import TestAuthenticationPage


# Get all tests from TestHomePageSearch class
home_page_search = unittest.TestLoader().loadTestsFromTestCase(TestHomePageSearch)
create_an_account = unittest.TestLoader().loadTestsFromTestCase(TestAuthenticationPage)


# Create a Test suite combining Simple Add Tests and Simple Sub Tests
all_tests = unittest.TestSuite([home_page_search, create_an_account])

# Run the suite without Reporting
# unittest.TextTestRunner(verbosity=2).run(math_tests)

# Run the suite with Reporting
# runner = HTMLTestRunner(output='example_suite')
# runner.run(math_tests)

# Run the suite with Advanced Reporting
reports = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="MyReport", add_timestamp=True).run(all_tests)