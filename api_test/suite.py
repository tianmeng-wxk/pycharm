from HTMLTestRunner import HTMLTestRunner
import unittest

from api_test.read_testcase import Test_api
# path = "E:\\pycharm\\api_test"
# discover = unittest.defaultTestLoader.discover(start_dir=path, pattern="read_*.py")#在path目录下运行以read开头的文件,运行discover
suite = unittest.TestSuite()
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_api))
dir = "E:\\pycharm\\api_test\\report\\report.html"
with open(dir,'wb')as file:
    runner = HTMLTestRunner(stream=file, title="特斯汀接口測試報告", description="特斯汀接口測試")
    runner.run(suite)