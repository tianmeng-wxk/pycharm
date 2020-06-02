import requests
from read_yaml import read_yaml
data = read_yaml()
class Httpclien():

    def __init__(self):
        self.url = data["login"]["url"]
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded'}


    def get(self,data):
        try:
            r = requests.get(url=self.url,params=data,headers=self.headers)
            return r.json()
        except BaseException as e:
            raise ("接口发生未知错误", e)

    def post(self,data,files):
        try:
            r = requests.post(url=self.url,data=data,headers=self.headers,files=files)
            return r.json()
        except BaseException as e:
            raise ("接口发生未知错误", e)

    def detelet(self,data):
        try:
            r = requests.post(url=self.url, data=data, headers=self.headers)
            return r.json()
        except BaseException as e:
            print("接口发生未知错误", e)

    def send_request(self, methon, name=None, data=None, files=None,headers=None):
        if headers:
            for key,value in headers.items():
                self.headers[key]=value
            print("添加后的headers为：",self.headers)
        # if data:
        #     if isinstance(data,dict):
        #         import json
        #         data = json.dumps(data)#字典才转换成json字符串
        #     #return data
        # print("data是：",data)

        self.url = self.url+name
        methon = methon.upper()
        res = ''
        if methon == "GET":
            res = self.get(data)
        elif methon == "POST":
            res = self.post(data,files)
        elif methon == "DETELET":
            res = self.detelet(data)
        return res





