'''HtmlTestRunner框架测试报告模板'''
from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
#from test_case.test_cases import TestCase
from testingshop.test_case.test_cases import TestCase


example_tests = TestLoader().loadTestsFromTestCase(TestCase)

suite = TestSuite([example_tests])

runner = HTMLTestRunner(output='example_suite')

runner.run(suite)