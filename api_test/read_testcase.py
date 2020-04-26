import requests,json
import unittest

from read_yaml import read_yaml

data = read_yaml()
class Test_api(unittest.TestCase):
    url = data["login"]["url"]
    session = requests.session()
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    def test_auth(self):

        response = self.session.post(self.url+"auth")
        jsonres = json.loads(response.text)
        print(jsonres)
        self.session.headers["token"] = jsonres["token"]#之后的每个用例不必在headers同步token
        self.assertEqual(jsonres["status"], 200, msg="获取token失败")

    def test_login(self):
        print(self.session.headers["token"])
        data = {"username": "Will", "password": "123456"}
        response = self.session.post(self.url+"login", data=data)
        res = response.json()
        print(res)
        self.assertEqual(res["msg"], "恭喜您，登录成功", msg="登录失败")

    def test_logout(self):
        print(self.session.headers["token"])
        response = self.session.post(self.url+"logout")
        res = response.json()
        print(res)
        self.assertEqual(res["msg"], "用户已退出登录", msg="登出失败")



