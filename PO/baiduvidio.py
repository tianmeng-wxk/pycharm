from selenium import webdriver
from time import sleep
#使用缓存
from selenium.webdriver.chrome.options import Options
option = Options()
option.add_argument(r"--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data")
driver = webdriver.Chrome(chrome_options=option)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.m.baidu.com")
sleep(3)
step1 = driver.find_element_by_xpath("//*[@id='new-bdvSearchInput']").clear()
step2 = driver.find_element_by_xpath("//*[@id='new-bdvSearchInput']").send_keys("beautiful")
step3 = driver.find_element_by_xpath("//*[@id='new-bdvSearchBtn']").click()
sleep(2)
# 跳转到新的页面，定位元素时，一定要加上这两行：
windows = driver.window_handles
driver.switch_to.window(windows[-1])
# driver.window_handles是获取当前的所有窗口
# driver.switch_to.window(windows[-1])是切换到最新打开的窗口
# 扩展：
# driver.switch_to.window(windows[0])是切换原来的窗口
# driver.current_window_handle是获取当前窗口
# 加上这两行再去定位元素就可以定位到了
sleep(2)
step4 = driver.find_element_by_xpath('//*[@id="loginbtn"]').click()
sleep(3)
# 弹出框不是alert类型：
# 1、弹出框是div层，跟平常一样定位，不用管弹出框
# # 点击退出按钮
# FindElement(self.brower, "classname", "btn-exit").click()
# # time.sleep(3)
# # 点击确认按钮（直接定位元素不用管页面的弹出样式，driver.window_handles打印出来的窗口在同一个页面）
# FindElement(self.brower, "classname", "pro-btn.btn-2.btn-confirm").click()
#
# 2、弹出框是iframe
# driver.switch_to.frame("frame1")
# 之后进行定位元素
#
# 3、弹出内容是嵌入的窗口解决思路：
# # 打印所有的handle
# all_handles = driver.window_handles
# print(all_handles)
# # 切换到新的handle上
# driver.switch_to.window(all_handles[1])
#driver.switch_to.frame(0)
driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[20]/iframe"))
sleep(5)
step5 = driver.find_element_by_xpath('//*[@placeholder="手机/用户名"]').send_keys("18344562525")
step6 = driver.find_element_by_xpath('//*[@id="login-xd-nickname"]/p[3]/input').send_keys("Wxk11111")
step7 = driver.find_element_by_xpath('//*[@id="login-xd-nickname"]/p[6]/button').click()
step8 = driver.switch_to.default_content()


