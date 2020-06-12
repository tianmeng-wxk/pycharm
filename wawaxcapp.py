# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.touch_actions import TouchActions
caps = {}
caps["deviceName"] = "A5RNW18320011338"
caps["platformName"] = "Android"
caps["platformVersion"] = "9"
caps["appPackage"] = "com.wawaxcStudent.Android"
caps["appActivity"] = "com.uzmap.pkg.EntranceActivity"
caps["unicodeKeyboard"] = True
caps["resetKeyboard"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

TouchAction(driver).tap(x=272, y=1127).perform()
driver.quit()
driver.swipe()