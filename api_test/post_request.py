import requests
import json
session = requests.session()

#可以使用Session
response = session.post("http://www.testingedu.com.cn:8081/inter/HTTP/auth")
'''如果上面使用requests就要在后面写上headers = session.headers'''
print(response.text)#现在为json类型，要转为字典类型
jsonres = json.loads(response.text)
print(jsonres)
session.headers["token"] = jsonres["token"]
'''前面让浏览器实时获取token的值，后面就不需要每一个加上token'''

response = session.post("http://www.testingedu.com.cn:8081/inter/HTTP/login", data={"username": "Will", "password": "123456"})#使用session请求就不用每个请求加上头headers=session.headers
result = response.json()
print(result)
