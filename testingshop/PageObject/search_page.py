from testingshop.BasePage.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from testingshop.PageObject.login_page import LoginPage
from time import sleep




class SearchPage(BasePage):
    search = (By.XPATH, '//*[@id="q"]')
    searchbt = (By.XPATH, '//*[@id="sourch_form"]/a')

    def input_search(self, searchtext):
        self.loc(self.search).send_keys(searchtext)

    def click_searchbt(self):
        self.loc(self.searchbt).click()

    def check(self,searchtext):
        #self.open_url(url2)
        self.input_search(searchtext)
        self.click_searchbt()
if __name__ == '__main__':
    #同一个driver完整执行登录后搜索流程
    searchtext = "华为"
    url = 'http://www.testingedu.com.cn:8000/index.php/Home/user/login.html'
    username = 13800138006
    password = 123456
    vercode = 1111
    driver = webdriver.Chrome()
    lp = LoginPage(driver)
    lp.login(url, username, password, vercode)

    sp = SearchPage(driver)
    sleep(2)
    sp.check(searchtext)






