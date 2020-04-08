from selenium import webdriver
from time import sleep
class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def loc(self, loc):
        return self.driver.find_element(*loc)

    def quit_browser(self):
        self.driver.quit()

    def visit(self, url):
        self.driver.get(url)
    def get_title(self):
        return self.driver.title






