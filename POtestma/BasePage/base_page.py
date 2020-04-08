import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
'''腾讯课堂搜索PO模式'''
class BasePage(object):

    def __init__(self, driver):

        self.driver = driver

    def open_url(self, url):

        self.driver.get(url)

    def quit_browser(self):

        self.driver.quit()

    def loc(self, loc):
        return self.driver.find_element(*loc)

    def max_windows(self):
        self.driver.maximize_window()













