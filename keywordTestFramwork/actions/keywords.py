from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def open():
    global driver
    driver = webdriver.Chrome()

def navigate(url):
    driver.get(url)

def find_element(loc_type, loc_ex):
    return driver.find_element(loc_type, loc_ex)
    # return WebDriverWait(driver, 20, 0.5).until(lambda x:x.find_element(loc_type, loc_ex))

def input(loc_type, loc_ex, value):
    # 为了提高脚本的稳定性, 每次定位元素前,都应该加一个显示等待
    find_element(loc_type, loc_ex).send_keys(value)

def click(loc_type, loc_ex):
    find_element(loc_type, loc_ex).click()

def verify(value):
    assert value in driver.page_source
