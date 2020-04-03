class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def quit_browser(self):
        self.driver.quit()

    def open_url(self, url):
        self.driver.get(url)

    def loc(self, loc):
        return self.driver.find_element(*loc)

    def maximize_window(self):
        self.driver.maximize_window()

    # def title(self):
    #     self.driver.title




