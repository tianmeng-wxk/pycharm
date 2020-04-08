from appium.webdriver import webdriver
from page import subPage
from time import sleep

def setUp(self):
    cas = {}
    cas["deviceName"] = "127.0.0.1:7555",
    cas["platformName"] = "Android",
    cas["platformVersion"] = "6",
    cas["appPackage"] = "com.tencent.mobileqq",
    cas["appActivity"] = ".activity.SplashActivity",
    cas["unicodeKeyboard"] = True,
    cas["resetKeyboard"] = True
    self.driver = webdriver.WebDriver("http://localhost:4723/wd/hub", cas)
    sleep(2)

runner = subPage()
setUp()

runner.dl(3394788013, "www111")


