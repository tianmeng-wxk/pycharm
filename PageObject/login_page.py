from BasePage.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginPage(BasePage):
    url = "http://219.135.151.105:8002/Modules/jpmis/login.html?ReturnUrl=%2f"
    uname_id = (By.ID, "uid")
    upwd_xp = (By.XPATH, "//*[@id='pwd']")
    loginbt_xp = (By.XPATH, '//*[@id="form1"]/div[4]/a')
    def input_username(self,username):
        self.loc(self.uname_id).send_keys(username)
    def input_userpwd(self,userpwd):
        self.loc(self.upwd_xp).send_keys(userpwd)
    def login_bt(self):
        self.loc(self.loginbt_xp).click()
    def check(self, username, userpwd):
        self.visit(self.url)
        self.input_username(username)
        self.input_userpwd(userpwd)
        self.login_bt()
if __name__ == '__main__':
    username = "hzsyg02"
    userpwd = "hzsyg022019"
    driver = webdriver.Chrome()
    lp = LoginPage(driver)
    lp.check(username, userpwd)







