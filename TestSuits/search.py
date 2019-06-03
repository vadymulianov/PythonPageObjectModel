import unittest
import HtmlTestRunner
from HtmlTestRunner import HTMLTestRunner
from Tests.Search.test_home_page_search import TestHomePageSearch


# Get all tests from TestHomePageSearch class
home_page_search = unittest.TestLoader().loadTestsFromTestCase(TestHomePageSearch)

# Create a Test suite combining Simple Add Tests and Simple Sub Tests
search = unittest.TestSuite([home_page_search])

# Run the suite without Reporting
# unittest.TextTestRunner(verbosity=2).run(math_tests)

# Run the suite with Reporting
# runner = HTMLTestRunner(output='example_suite')
# runner.run(math_tests)

# Run the suite with Advanced Reporting
reports = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="MyReport", add_timestamp=True).run(search)