#from testingshop.PageObject.search_page import SearchPage
import unittest
from selenium import webdriver
from time import sleep
from ddt import ddt, data, file_data, unpack

from testingshop.BasePage.base_page import BasePage
from testingshop.PageObject.login_page import LoginPage
from testingshop.PageObject.search_page import SearchPage
# test_data = [{"url": "http://www.testingedu.com.cn:8000/Home/user/login.html", "username": "13800138006", "password": "123456", "vercode": "1111"},
#              {"url": "http://www.testingedu.com.cn:8000/Home/user/login.html", "username": "13800138006", "password": "123456", "vercode": "1234"}
#              ]
# test_data = [["http://www.testingedu.com.cn:8000/Home/user/login.html", "13800138006", "123456", "1111"],
#              ["http://www.testingedu.com.cn:8000/Home/user/login.html", "13800138006", "123456", "1234"]
#              ]

# excel_path = "C:/Users/Administrator/Desktop/testingdata.xlsx"
# sheet_name = "Sheet1"
# excel_data = ReadExcel(excel_path, sheet_name)
# test_data = excel_data.dict_data()
@ddt
class TestCase(unittest.TestCase,LoginPage,SearchPage):

    def setUp(self) -> None:
        driver = webdriver.Chrome()
        self.lp = LoginPage(driver)
        self.sp = SearchPage(driver)
    def tearDown(self) -> None:
        pass


    '''如何通过读取文件参数化'''
    #@data(*test_data)
    #@unpack
    @file_data('data.yaml')
    def test_1_login(self, **kwargs):
        if 'login' in kwargs:
            url = kwargs['login'].get('url')
            username = kwargs['login'].get('username')
            password = kwargs['login'].get('password')
            vercode = kwargs['login'].get('vercode')
            self.lp.login(url, username, password, vercode)
            #self.lp.check(url, username, password, vercode)
            self.assertEqual("http://www.testingedu.com.cn:8000/index.php/Home/user/login.html", url, msg="地址验证失败")
        else:
            pass

    # @data(["http://www.testingedu.com.cn:8000/Home/user/login.html", "13800138006", "123456", "1111", "http://www.testingedu.com.cn:8000/Home/User/index.html", "华为"])
    # @unpack
    # def test_2_search(self, url, username, password, vercode, url2, searchtext):
    #     self.lp.check(url, username, password, vercode)
    #     self.sp.check(url2, searchtext)
    #
    @file_data('data.yaml')
    def test_2_search(self, **kwargs):
        if 'login' in kwargs:
            url = kwargs['login'].get('url')
            username = kwargs['login'].get('username')
            password = kwargs['login'].get('password')
            vercode = kwargs['login'].get('vercode')
            searchtext = kwargs['login'].get('searchtext')
            self.lp.login(url, username, password, vercode)
            sleep(2)
            self.sp.check(searchtext)
            print("hello")
        # self.input_search(*searchtext)
        # self.click_searchbt()


if __name__ == '__main__':
    unittest.main()





