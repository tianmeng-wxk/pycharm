import unittest
import requests
import json
import jsonpath


class MyTestCase(unittest.TestCase):
    tokenout = ""
    openid=""
    userid=""
    productid=""
    cartid=""
    vardict={}
    def test_1login(self):
        url = "http://39.98.138.157:5000/api/login"
        data = {"username": "admin", "password": "123456"}
        header = {"content-type": "application/json"}
        res = requests.post(url, headers=header, data=json.dumps(data))
        resjson = res.json()
        MyTestCase.vardict["login"]=resjson
        # 利用jsonpath库去取值token
        # token=jsonpath.jsonpath(resjson,"$.token")[0]
        MyTestCase.tokenout = jsonpath.jsonpath(resjson, "$.token")[0]
        # rint(token)
        msg = jsonpath.jsonpath(resjson, "$.msg")[0]
        self.assertEqual("success", msg)

    def test_2userinfo(self):
        url = "http://39.98.138.157:5000/api/getuserinfo"
        print(MyTestCase.tokenout)
        #header = {"token": MyTestCase.tokenout}
        #使用dict的变量取值
        headervalue=jsonpath.jsonpath(MyTestCase.vardict["login"],"$.token")[0]
        header = {"token": headervalue}
        res=requests.get(url,headers=header)
        resjson=res.json()
        print(resjson)
        MyTestCase.openid=jsonpath.jsonpath(resjson,"$.data[0].openid")[0]
        MyTestCase.userid = jsonpath.jsonpath(resjson, "$.data[0].userid")[0]
        print(MyTestCase.openid)
        httpcode=jsonpath.jsonpath(resjson, "$.httpstatus")[0]
        self.assertEqual(200, httpcode)

    def test_3productinfo(self):
        url="http://39.98.138.157:5000/api/getproductinfo?productid=8888"
        res = requests.get(url)
        resjson=res.json()
        httpcode = jsonpath.jsonpath(resjson, "$.httpstatus")[0]
        MyTestCase.productid=jsonpath.jsonpath(resjson, "$.data[0].productid")[0]
        self.assertEqual(200, httpcode)

    def test_4addcart(self):
        url="http://39.98.138.157:5000/api/addcart"
        header={"token":MyTestCase.tokenout,"content-type":"application/json"}
        data={"userid":MyTestCase.userid,"openid":MyTestCase.openid,"productid":MyTestCase.productid}
        data=json.dumps(data)
        res=requests.post(url,headers=header,data=data)
        resjson=res.json()
        print(resjson)
        MyTestCase.cartid=jsonpath.jsonpath(resjson, "$.data[0].cartid")[0]
        httpcode = jsonpath.jsonpath(resjson, "$.httpstatus")[0]
        self.assertEqual(200, httpcode)

    def test_5createorder(self):
        url="http://39.98.138.157:5000/api/createorder"
        header = {"token": MyTestCase.tokenout, "content-type": "application/json"}
        data={"cartid":MyTestCase.cartid,"openid":MyTestCase.openid,"productid":MyTestCase.productid,"userid":MyTestCase.userid}
        data=json.dumps(data)
        res=requests.post(url,headers=header,data=data)
        resjson=res.json()
        print(resjson)
        httpcode = jsonpath.jsonpath(resjson, "$.httpstatus")[0]
        self.assertEqual(200, httpcode)

if __name__ == '__main__':
    unittest.main()
