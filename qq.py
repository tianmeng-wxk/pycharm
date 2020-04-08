# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
caps = {}
caps["deviceName"] = "127.0.0.1:7555"
caps["platformName"] = "Android"
caps["platformVersion"] = "6.0.1"
caps["appPackage"] = "com.tencent.mobileqq"
caps["appActivity"] = ".activity.SplashActivity"
caps["unicodeKeyboard"] = True
caps["resetKeyboard"] = True
sleep(8)
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
sleep(8)
TouchAction(driver).tap(x=571, y=613).perform()
sleep(2)
TouchAction(driver).tap(x=546, y=607).perform()
sleep(40)
TouchAction(driver).tap(x=178, y=1011).perform()
sleep(2)
TouchAction(driver)
dl = driver.find_element_by_class_name("android.widget.EditText").send_keys("3394788013")
dl1 = driver.find_element_by_id("password").send_keys("www111")
dl2 = driver.find_element_by_id("login").click()
sleep(2)
