import unittest
from selenium import webdriver
from time import sleep
from ddt import ddt, data, unpack



from POtestma.read_excel import dict_data

from POtestma.ObjectPage.search_page import SearchPage

# test_data = [["https://ke.qq.com", "测码学院"], ["https://ke.qq.com", "柠檬班"]]
file_path = "C:/Users/Administrator/Desktop/testma.xlsx"
sheet_name = "Sheet1"
@ddt
class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.sp = SearchPage(cls.driver)
        url = "https://ke.qq.com"
        cls.sp.open_url(url)
        sleep(3)
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()#这种模式无法直接调用基类的方法，只能直接写



    @data(*dict_data(file_path, sheet_name))
    @unpack
    def test_1_search(self, searchtext):
        self.sp.input_search(searchtext)
        self.sp.search_bt()
        sleep(2)
        self.sp.driver.find_element_by_xpath('//*[@id="js_keyword"]').clear()
        sleep(2)
        text=self.driver.find_element_by_xpath("//*[@class = 'bold']")
        self.assertEqual("学院", text.text, msg="搜索失败")
    @unittest.skip("这一条不执行")
    def test_2(self):
        print("test_2")
    @unittest.skipUnless(2>1,"这是unless的理由")#条件为false才跳过，不执行
    def test_3(self):
        print("test_3")
    @unittest.skipIf(2>1,"这是if的理由")#条件为True才跳过，不执行
    def test_4(self):
        print("test_4")
if __name__ == '__main__':
    unittest.main()

