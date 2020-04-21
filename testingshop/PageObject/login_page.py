from Chaojiying_Python.chaojiying import Chaojiying_Client
from testingshop.BasePage.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from PIL import Image
import pytesseract
import requests

class LoginPage(BasePage):

    uname = (By.XPATH, '//*[@id="username"]')
    upwd = (By.XPATH, '//*[@id="password"]')
    vcode = (By.XPATH, '//*[@id="verify_code"]')
    vcodeimg = (By.XPATH, '//*[@id="verify_code_img"]')
    loginbt = (By.XPATH, '//*[@id="loginform"]/div/div[6]/a')

    def input_username(self, username):
        self.loc(self.uname).send_keys(username)

    def input_password(self, password):
        self.loc(self.upwd).send_keys(password)

    def input_vercode(self, vercode):
        self.loc(self.vcode).send_keys(vercode)

    def click_loginbt(self):
        self.loc(self.loginbt).click()

    def login(self, url, username, password):
        self.maximize_window()
        self.open_url(url)
        sleep(3)
        self.input_username(username)
        self.input_password(password)
        self.driver.save_screenshot("E:\\pycharm\\testingshop\\vercode_img\\page.png")
        vcode = self.driver.find_element_by_xpath("//*[@id='verify_code_img']")
        loc = vcode.location
        size = vcode.size
        left = loc['x']
        top = loc['y']
        right = (loc['x'] + size['width'])
        button = (loc['y'] + size['height'])
        page_pic = Image.open("E:\\pycharm\\testingshop\\vercode_img\\page.png")
        v_code_pic = page_pic.crop((left, top, right, button))
        v_code_pic.save("E:\\pycharm\\testingshop\\vercode_img\\vercode.png")
        chaojiying = Chaojiying_Client('qq121292679', 'a546245426', '904603')#用户中心>>软件ID 生成一个替换 96001
        im = open('E:\\pycharm\\testingshop\\vercode_img\\vercode.png', 'rb').read()#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
        res = chaojiying.PostPic(im, 1902)
        print(res)
        vercode = res['pic_str']
        print(vercode)
        # # 验证码地址
        # url = "http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=verify&r=0.1467503305118174"
        # response = requests.get(url).content
        # # 将图片写入文件
        # with open('C:\\Users\\Administrator\\Desktop\\rryz.png', 'wb') as f:
        #     f.write(response)
        # # 读取文件内容
        # with open('C:\\Users\\Administrator\\Desktop\\rryz.png', 'rb') as f:
        #     pic1 = f.read()
        # # 调用第三方打码平台接口识别验证码
        # from chaojiying import Chaojiying
        # yz = Chaojiying(username='qq121292679', password='a546245426', soft_id='904603')
        # res = yz.post_pic(pic1, 1902)
        # print(res)
        # vercode = res['pic_str']
        self.input_vercode(vercode)
        self.click_loginbt()
if __name__ == '__main__':
    url = "http://www.testingedu.com.cn:8000/Home/user/login.html"
    username = "13800138006"
    password = "123456"
    # vercode = "1111"
    driver = webdriver.Chrome()
    lp = LoginPage(driver)
    lp.login(url, username, password)








