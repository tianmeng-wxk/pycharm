import time
from time import sleep

class Page:
    def __init__(self, driver):
        self.driver = driver
    def find_element(self,locid,loccl):
        #loc页面元素变量名
        try:
            return self.driver.find_element_by_id(locid), self.driver.find_element_by_class(loccl)
        except Exception as e:
            print('没找到元素%s' %(self, locid, loccl))
class subPage(Page):
    dl_locid=("com.tencent.mobileqq:id/btn_login")
    username_loccl=("android.widget.EditText")
    passwd_locid=("com.tencent.mobileqq:id/password")
    dlbutton_locid=("com.tencent.mobileqq:id/login")
    def dl(self,uValue,pValue):
        self.driver.find_element_by_id(self.dl_locid).clike()
        sleep(1)
        self.driver.find_element_by_class(self.username_loccl).send_keys(uValue)
        self.driver.find_element_by_id(self.passwd_locid).send_keys(pValue)
        self.driver.find_element_by_id(self.dlbutton_locid).clike()










