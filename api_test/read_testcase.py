import requests,json
import unittest
from api_test.key_work import Httpclien
# from read_yaml import read_yaml
# data = read_yaml()
class Test_api(unittest.TestCase):
    # url = data["login"]["url"]
    #session = requests.session()
    token = ''




    def setUp(self) -> None:
        self.clien = Httpclien()

#获取token的请求
    def test_auth(self):
        # response = self.session.post(self.url+"auth")
        # jsonres = json.loads(response.text)
        # print(jsonres)
        # self.session.headers["token"] = jsonres["token"]#之后的每个用例不必在headers同步token
        # self.assertEqual(jsonres["status"], 200, msg="获取token失败")
        res = self.clien.send_request("post", name="auth")
        Test_api.token = res["token"]

        print("response：",res)
#登录
    def test_login(self):
        #print("token为:{}".format(Test_api.token))
        data = {"username": "Will", "password": 123456}
        headers = {
            "token": Test_api.token
        }
        # response = self.session.post(self.url+"login", data=data)
        # res = response.json()
    #   print(res)
    #   self.assertEqual(res["msg"], "恭喜您，登录成功", msg="登录失败")
        res = self.clien.send_request("post", name="login", data=data,  headers=headers)
        self.assertEqual(res["msg"], "恭喜您，登录成功", msg="登录失败")
        print("response：",res)



#登出
    def test_logout(self):
        headers = {
            "token": Test_api.token
        }
        # print(self.session.headers["token"])
        # response = self.session.post(self.url+"logout")
        # res = response.json()
        # print(res)
        # res = self.assertEqual(res["msg"], "用户已退出登录", msg="登出失败")
        res = self.clien.send_request("post", name="logout",headers=headers)
        self.assertEqual(res["msg"], "用户已退出登录", msg="登出失败")
        print("response：", res)




