from BasePage.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



class LoginPage(BasePage):

    uname = (By.XPATH, '//*[@id="username"]')
    upwd = (By.XPATH, '//*[@id="password"]')
    vcode = (By.XPATH, '//*[@id="verify_code"]')
    loginbt = (By.XPATH, '//*[@id="loginform"]/div/div[6]/a')

    def input_username(self, username):
        self.loc(self.uname).send_keys(username)

    def input_password(self, password):
        self.loc(self.upwd).send_keys(password)

    def input_vercode(self, vercode):
        self.loc(self.vcode).send_keys(vercode)

    def click_loginbt(self):
        self.loc(self.loginbt).click()

    def login(self, url, username, password, vercode):
        self.maximize_window()
        self.open_url(url)
        sleep(3)
        # self.title()
        # print(self.driver.title)
        self.input_username(username)
        self.input_password(password)
        self.input_vercode(vercode)
        self.click_loginbt()


# if __name__ == '__main__':
#     url = "http://www.testingedu.com.cn:8000/Home/user/login.html"
#     username = "13800138006"
#     password = "123456"
#     vercode = "1111"
#     driver = webdriver.Chrome()
#     lp = LoginPage(driver)
#     lp.check(url, username, password, vercode)








