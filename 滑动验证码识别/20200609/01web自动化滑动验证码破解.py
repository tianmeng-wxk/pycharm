"""
============================
Author:柠檬班-木森
Time:2020/6/9   14:45
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
from selenium import webdriver
from slideVerfication import SlideVerificationCode

"""
环境安装：
1、安装python
2、安装selenium ，cmd中输入：pip install selenium
3、下载chromedriver,并且配置环境变量

"""

# 第一步：打开浏览器
driver = webdriver.Chrome()
driver.implicitly_wait(15)

# 第二步：访问qq空间登录页面
driver.get(url="https://qzone.qq.com/")

# 第三步：点击账号密码登录
# 3.1 切换iframe
driver.switch_to.frame('login_frame')
driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()

# 第四步：输入账号密码
# 4.1定位账号输入框，输入账号
driver.find_element_by_xpath('//*[@id="u"]').send_keys('362715381')
# 4.2 定位密码输入框，输入密码
driver.find_element_by_xpath('//*[@id="p"]').send_keys('1234r2we')

# 第五步：点击登录
driver.find_element_by_xpath('//*[@id="login_button"]').click()

# 第六步：滑动验证码
# 6.1创建一个滑动验证的对象
sli = SlideVerificationCode()
# 6.2 计算滑动的距离

# 切换到验证码所在的iframe
driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="tcaptcha_iframe"]'))
# 定位滑块图片
slider_ele = driver.find_element_by_xpath('//*[@id="slideBlock"]')
# 定位验证码背景图
background_ele = driver.find_element_by_xpath('//*[@id="slideBg"]')

distance = sli.get_element_slide_distance(slider_ele, background_ele)
# print("滑动的距离为：", distance)
# 根据页面图片缩放比调整滑动距离
distance = distance * 280 / 680 - 31
# 6.3模拟滑动鼠标
btn = driver.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
sli.slide_verification(driver,btn,distance)


driver.close()



