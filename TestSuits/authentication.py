import unittest
import HtmlTestRunner
from HtmlTestRunner import HTMLTestRunner
from Tests.Accounts.test_create_an_account import TestAuthenticationPage


# Get all tests from TestHomePageSearch class
create_an_account = unittest.TestLoader().loadTestsFromTestCase(TestAuthenticationPage)

# Create a Test suite combining Simple Add Tests and Simple Sub Tests
search = unittest.TestSuite([create_an_account])

# Run the suite without Reporting
# unittest.TextTestRunner(verbosity=2).run(math_tests)

# Run the suite with Reporting
# runner = HTMLTestRunner(output='example_suite')
# runner.run(math_tests)

# Run the suite with Advanced Reporting
reports = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="MyReport", add_timestamp=True).run(create_an_account)