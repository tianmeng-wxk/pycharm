from selenium import webdriver
from time  import sleep
import time
import xlrd
from ddt import ddt, data, unpack
import unittest
option = webdriver.ChromeOptions()
#option.add_argument("headless")
import re
#import requests
#from requests
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome(options=option)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://219.135.151.105:8002")
expect_url = "http://219.135.151.105:8002/Modules/jpmis/login.html?ReturnUrl=%2f"
actual_url = driver.current_url
print(driver.current_url)
if expect_url in actual_url:
    print("yes")
else:
    print("no")
expect_title = "广东省驾驶培训监管服务平台"
actual_title = driver.title
print(driver.title)
if expect_title in actual_title:
    print("yes")
else:
    print("no")

dl = driver.find_element_by_id("uid")
dl.send_keys("hzsyg02")

dl2 = driver.find_element_by_id("pwd")
dl2.send_keys("hzsyg022019")

dl3 = driver.find_element_by_class_name("btnGro")
dl3.click()
driver.implicitly_wait(5)
dl4 = driver.find_element_by_link_text("学员培训过程管理")
dl4.click()
time.sleep(2)
dl5 = driver.find_element_by_link_text("电子教学日志管理")
dl5.click()
time.sleep(2)
#driver.switch_to.default_content()
#跳转页面需添加
#driver.switch_to_window(driver.window_handles[1])
#driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
driver.switch_to.frame(1)
dl7 = driver.find_element_by_class_name("more").click()
sleep(2)
dl8 = driver.find_element_by_id("8_input").click()
sleep(2)
dl9 = driver.find_element_by_id("8_input_2").click()
sleep(1)
        # dl9 = driver.find_element_by_css_selector("#25_container>ul>li#46_input_2").click()
#或者使用下面的绝对定位方式
#driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[@class='content']/div[2]/div[2]/div[2]/iframe"))
#跳出frame
'''driver.switch_to.default_content()'''
#element = driver.find_element_by_css_selector("frame")
#driver.switch_to.frame(element)
#element = driver.find_element_by_css_selector("iframe")    #第一步：定位iframe元素
#driver.switch_to.frame(element)
#driver.switch_to_window(driver.window_handles[1])
#frame = driver.find_elements_by_tag_name("iframe")[0]
#driver.switch_to.frame(frame)
#driver.switch_to.default_content()
#dl6 = driver.find_element_by_partial_link_text("更多").click()





#print(i)

#while a>2:
'''def printinfo(arg1, *vartuple):
        "打印任何传入的参数"
        print("输出: ")
        print(arg1)
        for var in vartuple:
            print(var)
        return


    # 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)'''
class ReadExcel:
    def __init__(self, excel_path, sheet_name):
        self.workbook = xlrd.open_workbook(excel_path)
        self.worksheet = self.workbook.sheet_by_name(sheet_name)
        self.rownum = self.worksheet.nrows
        self.colnum = self.worksheet.ncols




    def dict_data(self):
        if self.rownum <= 1:
             print("表格行数小于等于1，不能进行自动化")
        else:
             list = []
             self.headers = self.worksheet.row_values(0)
             #self.headers = self.worksheet.row_values(0)
             #j = 1#从1开始
             for i in range(1, self.rownum):
                 s = {}
                 values = self.worksheet.row_values(i)

                 for x in range(self.colnum):
                    s[self.headers[x]] = values[x]
                 list.append(s)
                 #j += 1
             return list
excel_path = "C:/Users/Administrator/Desktop/idcard.xlsx"
sheet_name = "Sheet1"
d = ReadExcel(excel_path, sheet_name)
d.dict_data()













@ddt
class TestCase(unittest.TestCase):
    # def setUpClass(cls) -> None:
    #     pass
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @data(*d.dict_data())
    @unpack
    def test_1(self, idcard):

        dl6 = driver.find_element_by_xpath("//*[@id='cert_num']").send_keys(idcard)

        dl10 = driver.find_element_by_id("searchBtn").click()
        sleep(5)

        try:

            dl11 = driver.find_element_by_css_selector("td[aria-describedby='gridTable_validMin']").text


        except:

            print(idcard+"   "+"查不到数据")
        else:
            print(idcard+"   "+dl11)
        finally:
            dl12 = driver.find_element_by_xpath("//*[@id='cert_num']").clear()
            sleep(2)








#with open("music.txt","r",encoding="utf-8") as f:
    #r = f.read()
    #print(r)
# file_name = "C:/Users/Administrator/Desktop/music.txt"
# with open(file_name, "w") as f:
#     f.write(file_name)
#     #f.write("I love you\n")

#sleep(2)
#dl12 = driver.find_element_by_css_selector("form>table>tbody>tr:nth(3)>td:last>input").send_keys("S157283407010570")
#dl7 = driver.find_element_by_xpath("//div[@class='more']").click()
#dl7 = driver.find_element_by_link_text("更多").click()
#driver.implicitly_wait(5)

# 先定位到iframe
#driver.switch_to.frame(0)
#driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
#driver.switch_to_default_content()
#a = w.find_element_by_class_name('frameBox qf12')
# 再将定位对象传给switch_to_frame()方法
#w.switch_to_frame(a)
#w.switch_to.parent_content()
'''如果完成操作后，可以通过switch_to.parent_content()
方法跳出当前iframe，或者还可以通过'''
#w.switch_to.default_content()
'''方法跳回最外层的页面。'''
# driver.switch_to.parent_frame()#返回上一层
# driver.switch_to.default_content()#返回默认界面


#dl6 = driver.find_element_by_link_text("更多").click()

#driver.switchTo().frame(driver.findElement(By.xpath(("//iframe[contains(@src,'/gdgs/single_tree/list/eova_menu')]"))))


