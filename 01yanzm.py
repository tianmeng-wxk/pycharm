import requests
from PIL import Image
import pytesseract


"""下载验证码图片"""
# 验证码地址
# https://www.renrendai.com/passport/index/captcha?time=1551682134111
# url = "https://www.renrendai.com/passport/index/captcha?time=1551682134111"
url = "http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=verify&r=0.8834463023296559"
response = requests.get(url).content


#将图片写入文件
with open('C:\\Users\\Administrator\\Desktop\\rryz.png', 'wb') as f:
    f.write(response)

# '''识别验证码'''
# #第一步：通过内置模块PIL打开文件
# # with open('rryz.png','wb') as f:
# pic = Image.open('C:\\Users\\Administrator\\Desktop\\rryz.png')
# #第二步：识别图片中的内容
# str1 = pytesseract.image_to_string(pic, lang="chi_sim")# 复杂的验证码，直接识别不了（要进行降噪，，，，处理）
# print("验证码识别", str1)


#读取文件内容
with open('C:\\Users\\Administrator\\Desktop\\rryz.png', 'rb') as f:
    pic1 = f.read()
#调用第三方打码平台接口识别验证码
from chaojiying import Chaojiying
yz = Chaojiying(username='qq121292679', password='a546245426', soft_id='904603')
res = yz.post_pic(pic1, 1902)
print(res['pic_str'])