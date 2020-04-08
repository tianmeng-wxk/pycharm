from BasePage.base_page import BasePage
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class SearchPage(BasePage):
#定位元素
    input_id = (By.ID, "kw")
    click_id = (By.ID, "su")
#给每个控件一个方法
    def input_text(self, input_text):
        self.loc(self.input_id).send_keys(input_text)
    def click_element(self):
        self.loc(self.click_id).click()
#测试函数（整个流程）
    def check(self, url, input_text):
        self.visit(url)
        self.input_text(input_text)
        self.click_element()


if __name__ == '__main__':
    url = "http://www.baidu.com"
    input_text = "test"
    driver = webdriver.Chrome()
    sp = SearchPage(driver)
    sp.check(url, input_text)
    #sp.visit(url)
    # sp.input_text("test")
    # sp.click_element()


