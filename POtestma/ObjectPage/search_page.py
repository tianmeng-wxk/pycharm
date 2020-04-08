from POtestma.BasePage.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    search = (By.ID, 'js_keyword')
    searchbt = (By.ID, 'js_search')

    def input_search(self, searchtext):
        self.loc(self.search).send_keys(searchtext)
    def search_bt(self):
        self.loc(self.searchbt).click()

