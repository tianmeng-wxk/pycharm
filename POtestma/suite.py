import unittest
import os
from POtestma.TestCase.test_case import TestCase
from HTMLTestRunner import HTMLTestRunner
suite = unittest.TestSuite()
#list = [TestCase("test_2"), TestCase("test_3")]
#path = "./"
#discover = unittest.defaultTestLoader.discover(start_dir=path, pattern="test_*.py")

# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCase))
#
# runner = unittest.TextTestRunner()
# runner.run(suite)


#集成测试报告
report_name = "测试名称"
report_title = "测试标题"
report_desc = "测试描述"
report_path = "./report/"
report_file = report_path+"report.html"
if not os.path.exists(report_path):
    os.mkdir(report_path)
else:
    pass


with open(report_file, "wb") as report:
    list = [TestCase("test_2"), TestCase("test_3")]
    suite.addTests(list)
    #suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCase))
    runner = HTMLTestRunner(stream=report, title=report_title, description=report_desc)
    runner.run(suite)