from PIL import Image
import requests
from Chaojiying_Python.chaojiying import Chaojiying_Client
#方法一
def ivercode(driver):
    driver.save_screenshot("E:\\pycharm\\testingshop\\vercode_img\\page.png")
    vcode = driver.find_element_by_xpath("//*[@id='verify_code_img']")
    loc = vcode.location
    size = vcode.size
    left = loc['x']
    top = loc['y']
    right = (loc['x'] + size['width'])
    button = (loc['y'] + size['height'])
    page_pic = Image.open("E:\\pycharm\\testingshop\\vercode_img\\page.png")
    v_code_pic = page_pic.crop((left, top, right, button))
    v_code_pic.save("E:\\pycharm\\testingshop\\vercode_img\\vercode.png")
    chaojiying = Chaojiying_Client('qq121292679', 'a546245426', '904603')  # 用户中心>>软件ID 生成一个替换 96001
    im = open('E:\\pycharm\\testingshop\\vercode_img\\vercode.png', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    res = chaojiying.PostPic(im, 1902)
    vercode = res['pic_str']
    return vercode
#方法二
def ivercode2(driver):
    ele = driver.find_element_by_xpath("//*[@id='verify_code_img']")
    ele.screenshot("E:\\pycharm\\testingshop\\vercode_img\\verify.png")
    headers = {
        'Connection': 'Keep-Alive',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
    }
    data = {
        'user': 'wuqingfqng',
        'pass2': '6e8ebd2e301f3d5331e1e230ff3f3ca5',#密碼：wuqing&fqng
        "softid": "904357",
        "codetype": "1902"
    }
    userfile = open("E:\\pycharm\\testingshop\\vercode_img\\verify.png","rb").read()
    userfile = {"userfile": ("E:\\pycharm\\testingshop\\vercode_img\\verify.png", userfile)}
    res = requests.post("http://upload.chaojiying.net/Upload/Processing.php",data=data,files=userfile,headers=headers)
    res = res.json()
    vercode = res["pic_str"]
    return vercode






