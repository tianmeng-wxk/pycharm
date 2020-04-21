import os
import sys

from xlrd读取文件.read_eg import ReadExcel

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.path.append('E:\\pycharm')
print(sys.path)
import unittest
from selenium import webdriver
from time import sleep
from ddt import ddt, data, file_data, unpack
from testingshop.PageObject.login_page import LoginPage
from testingshop.PageObject.search_page import SearchPage
'''放到github要去掉项目文件名testingshop'''
#sys.path.append('E:/pycharm/testingshop')
#from testingshop.BasePage.base_page import BasePage

# test_data = [{"url": "http://www.testingedu.com.cn:8000/Home/user/login.html", "username": "13800138006", "password": "123456", "vercode": "1111"},
#              {"url": "http://www.testingedu.com.cn:8000/Home/user/login.html", "username": "13800138006", "password": "123456", "vercode": "1234"}
#              ]
# test_data = [["http://www.testingedu.com.cn:8000/Home/user/login.html", "13800138006", "123456", "1111"],
#              ["http://www.testingedu.com.cn:8000/Home/user/login.html", "13800138006", "123456", "1234"]
#              ]

excel_path = "C:/Users/Administrator/Desktop/testingdata.xlsx"
sheet_name = "Sheet1"
excel_data = ReadExcel(excel_path, sheet_name)
test_data = excel_data.dict_data()
@ddt
class TestCase(unittest.TestCase,LoginPage,SearchPage):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.lp = LoginPage(self.driver)
        self.sp = SearchPage(self.driver)
    def tearDown(self) -> None:
        self.driver.quit()

    '''如何通过读取文件参数化'''
    @data(*test_data)
    #@unpack
    #@file_data('data.yaml')
    def test_1_login(self, test_data):
            url = test_data['url']
            username = test_data['username']
            password = test_data['password']
            #vercode = test_data['vercode']
            self.lp.login(url, username, password)
            sleep(5)
            #self.lp.check(url, username, password, vercode)
            self.assertEqual("http://www.testingedu.com.cn:8000/index.php/Home/user/login.html", url, msg="地址验证失败")

    # @data(["http://www.testingedu.com.cn:8000/Home/user/login.html", "13800138006", "123456", "1111", "http://www.testingedu.com.cn:8000/Home/User/index.html", "华为"])
    # @unpack
    # def test_2_search(self, url, username, password, vercode, url2, searchtext):
    #     self.lp.login(url, username, password, vercode)
    #     self.sp.check(url2, searchtext)

    # @file_data('data.yaml')
    # def test_2_search(self, **kwargs):
    #     if 'login' in kwargs:
    #         url = kwargs['login'].get('url')
    #         username = kwargs['login'].get('username')
    #         password = kwargs['login'].get('password')
    #         vercode = kwargs['login'].get('vercode')
    #         searchtext = kwargs['login'].get('searchtext')
    #         self.lp.login(url, username, password, vercode)
    #         sleep(2)
    #         self.sp.check(searchtext)
        # self.input_search(*searchtext)
        # self.click_searchbt()

if __name__ == '__main__':
    unittest.main()





