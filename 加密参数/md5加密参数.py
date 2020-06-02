# str = "admin"
# strcmd5 = hashlib.md5(str.encode("utf-8"))
# strcmd5 = strcmd5.hexdigest()
# print(strcmd5)

import requests
import hashlib
import json
ip = '47.93.148.45'
sign = hashlib.md5(b'admin').hexdigest()
print(sign)
#这是个对房源下单的接口，可以理解为对某个商品下单
url = 'http://{}/api_create_order/?sign={}'.format(ip,sign)
#sign 使用来验证发起接口请求这一方的身份的。
data = {
  "luId":1, #房源ID，也可以是商品ID
  "guestNum":2, #房客数量，多少人入住
  "checkInDate":"2020-01-03", #入住日期
  "checkOutDate":"2020-01-04" #离开日期
}
json.dumps(data)
print("url",url)
re = requests.post(url,json=data)
print(re.text)