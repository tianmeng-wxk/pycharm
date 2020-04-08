import unittest
from selenium import webdriver
from time import sleep
from ddt import ddt, data, unpack

from PageObject.search_page import SearchPage

@ddt
class TestCase(unittest.TestCase):
    #前置条件
    #@classmethod
    #def setUpClass(cls) -> None:  cls.driver = webdriver.Chrome()
    def setUp(self) -> None:
        driver = webdriver.Chrome()#executable_path=可以自定义路径
        self.sp = SearchPage(driver)
    #后置条件

    def tearDown(self) -> None:
        self.sp.quit_browser()

    @data(["http://www.baidu.com", "test"], ["http://www.baidu.com", "case"])
    @unpack
    def test_1(self, url, input_text):
        self.sp.check(url, input_text)
        sleep(2)
        self.assertEqual(self.sp.get_title(), "百度一下，你就知道", msg="对不起")

if __name__ == '__main__':
    unittest.main()







