from selenium import webdriver
from time import sleep
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
#option.add_argument('headless')

driver = webdriver.Chrome(options=option)
driver.get("http://www.baidu.com")
print(driver.title)
