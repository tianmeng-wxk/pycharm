import requests, unittest, json, jsonpath
class TestCase(unittest.TestCase):
    vardict = {}
    #登录
    def test_1_login(self):
        url = 'http://39.98.138.157:5000/api/login'
        data = {"username":"admin","password":"123456"}
        headers = {"content-type":"application/json"}
        res = requests.post(url=url,headers=headers,data=json.dumps(data))
        resjson = res.json()
        print("登录返回：",resjson)
        TestCase.vardict["login"] = resjson
        token = jsonpath.jsonpath(TestCase.vardict["login"],"$.token")[0]
        msg = jsonpath.jsonpath(TestCase.vardict["login"],"$.msg")[0]
        print("获取到的token:", token)
        self.assertEqual("success", msg, msg="登录断言失败")

    #用户信息
    def test_2_userinfo(self):
        url = 'http://39.98.138.157:5000/api/getuserinfo'
        token = jsonpath.jsonpath(TestCase.vardict["login"],'$.token')[0]
        headers = {"token": token}
        res = requests.get(url=url,headers=headers)
        resjson = res.json()
        TestCase.vardict["userinfo"] = resjson
        print("用户信息返回：", resjson)
        openid = jsonpath.jsonpath(TestCase.vardict["userinfo"], '$.data[0].openid')[0]
        userid = jsonpath.jsonpath(TestCase.vardict["userinfo"], '$.data[0].userid')[0]
        self.assertEqual(openid,'UEHUXUXU78272SDSassDD', msg="openid获取失败")
        self.assertEqual(userid, 17890, msg="userid获取失败")

    #产品信息
    def test_3productinfo(self):
        url = "http://39.98.138.157:5000/api/getproductinfo?productid=8888"
        res = requests.get(url)
        resjson = res.json()
        print("产品信息返回",resjson)
        TestCase.vardict["productinfo"] = resjson
        httpcode = jsonpath.jsonpath(TestCase.vardict["productinfo"], '$.httpstatus')[0]
        productid = jsonpath.jsonpath(TestCase.vardict["productinfo"], '$.data[0].productid')[0]
        self.assertEqual(8888, productid)
        self.assertEqual(200, httpcode)

    #添加购物车
    def test_4addcart(self):
        url = "http://39.98.138.157:5000/api/addcart"
        token = jsonpath.jsonpath(TestCase.vardict["login"], '$.token')[0]
        userid = jsonpath.jsonpath(TestCase.vardict["userinfo"], "$.data[0].userid")[0]
        openid = jsonpath.jsonpath(TestCase.vardict["userinfo"], "$.data[0].openid")[0]
        productid = jsonpath.jsonpath(TestCase.vardict["productinfo"],"$.data[0].productid")[0]

        header = {"token": token, "content-type": "application/json"}
        data = {"userid": userid, "openid": openid, "productid": productid}
        res = requests.post(url, headers=header, data=json.dumps(data))
        resjson = res.json()
        TestCase.vardict["addcart"] = resjson
        print("添加购物车返回：", resjson)
        cartid = jsonpath.jsonpath(TestCase.vardict["addcart"],"$.data[0].cartid")[0]
        httpstatus = jsonpath.jsonpath(TestCase.vardict["addcart"], "$.httpstatus")[0]
        self.assertEqual(200, httpstatus)
        self.assertEqual(45233, cartid)

    #创建订单
    def test_5createorder(self):
        url = "http://39.98.138.157:5000/api/createorder"
        token = jsonpath.jsonpath(TestCase.vardict["login"], '$.token')[0]
        cartid = jsonpath.jsonpath(TestCase.vardict["addcart"],"$.data[0].cartid")[0]
        openid = jsonpath.jsonpath(TestCase.vardict["userinfo"],"$.data[0].openid")[0]
        productid = jsonpath.jsonpath(TestCase.vardict["productinfo"],"$.data[0].productid")[0]
        userid = jsonpath.jsonpath(TestCase.vardict["userinfo"], "$.data[0].userid")[0]

        header = {"token": token, "content-type": "application/json"}
        data = {"cartid": cartid, "openid": openid, "productid": productid, "userid": userid}
        data = json.dumps(data)
        res = requests.post(url, headers=header, data=data)
        resjson = res.json()
        TestCase.vardict["createorder"] = resjson
        print("创建订单返回：", resjson)
        httpstatus = jsonpath.jsonpath(TestCase.vardict["createorder"], "$.httpstatus")[0]
        self.assertEqual(200, httpstatus)

if __name__ == '__main__':
    unittest.main()