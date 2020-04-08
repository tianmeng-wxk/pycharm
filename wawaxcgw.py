# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.touch_actions import TouchActions
from time import sleep
caps = {}
caps["deviceName"] = "C7Y6R19B08010683"
caps["platformName"] = "Android"
caps["platformVersion"] = "9"
caps["appPackage"] = "com.g3237355640.rkh"
caps["appActivity"] = "com.uzmap.pkg.EntranceActivity"
caps["unicodeKeyboard"] = True
caps["resetKeyboard"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
sleep(5)
#driver.find_element_by_class_name("android.view.View").click()
TouchAction(driver).tap(x=530, y=2020).perform()
driver.quit()