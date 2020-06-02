import requests,json
import unittest
from HTMLTestRunner import HTMLTestRunner
import yaml
import os,logging


logger = logging.getLogger('test')
logger.setLevel(logging.DEBUG)  # 输出所有大于DEBUG级别的log
# 设置日志输出格式
fmt = logging.Formatter('[%(filename)-6s]: [%(levelname)-6s] [%(asctime)s]: %(message)s')
stream_hdl = logging.StreamHandler()
stream_hdl.setFormatter(fmt)
stream_hdl.setLevel(logging.DEBUG)
logger.addHandler(stream_hdl)

# logger.info('这是info')
# logger.debug('这是debug')
# logger.error('这是error')

current_path=os.path.abspath(os.path.dirname(__file__))
config_path=current_path+'\config\data.yaml'
def read_yaml():
    with open(config_path,'r',encoding='utf-8') as f:
        cfg=yaml.load(f.read())
        #print(type(cfg),cfg)
        return cfg
# import  pymysql
# def connect_mysql(sql):
#     # db_connect=pymysql.connect(host='',port='3306',user='',password='')
#     # cursor=db_connect.cursor()
#     # cursor.execute(sql)
#     # res=cursor.fetchall()
#     res=''
#     return  res
#from inter_request import TestHttpClien
data=read_yaml()
class TestHttpClien():
    '''封装发送所有http请求的类'''
    def __init__(self):
        self.url=data['api_url']['on_line']
        self.headers = {
            'Content-Type': 'application/json'
        }
    def get(self,data):
        try:
            r = requests.get(url=self.url, params=data, headers=self.headers)
            return r.json()  # 返回接口的返回值
        except BaseException as e:
            raise ("接口发生未知错误", e)

    def post(self,data,files):
        try:
            r=requests.post(url=self.url,data=data,headers=self.headers,files=files)
            return r.json()  #返回接口的返回值
        except BaseException as e:
            raise ("接口发生未知错误",e)


    def detelet(self,data):
        try:
            r = requests.delete(url=self.url, data=data, headers=self.headers)
            return r.json()  # 返回接口的返回值
        except BaseException as e:
            raise ("接口发生未知错误", e)

    def send_request(self,methon,name=None,data=None,files=None,headers=None):
        '''  headers = {
            'token':API_TestCase.TOKEN,
            "cookie":"111"
        }'''
        if headers:
            for key,value in headers.items():
                self.headers[key]=value
        if data:
            if isinstance(data,dict):
                import json
                data=json.dumps(data) #字典才转换成字符串
        self.url=self.url+name  #拼接每次请求的url
        methon=methon.upper()
        res=''
        if methon=='POST':
            res=self.post(data,files)
        elif methon=='GET':
            res=self.get(data)
        elif methon=='DELETE':
            res=self.detelet(data)
        logger.info("接口地址：{0}，接口的入参是{1},入参类型{2}，接口的响应值{3}".
                    format(self.url,data,type(data),res))

        return res





class API_TestCase(unittest.TestCase):
    '''类变量 ：self.变量名称   类名称.变量名称
    ：实例变量'''
    # TEST_URL=data['api_url']['on_line']
    # TOKEN='aaa'
    @classmethod
    def setUpClass(self) -> None:
        '''所有用例执行之前，数据库前置操作'''
        #self.sql=connect_mysql('select')
        self.client=TestHttpClien()


    def test01_login(self):

        payload = {"username": "admin", "password": "123456"}
        headers = {
            'Content-Type': 'application/json'
        }
    #     # payload = json.dumps(payload)
    #     # response = requests.request("POST", self.TEST_URL+'login', headers=headers, data=payload)
    #     # res=response.json()
    #     # API_TestCase.TOKEN=res["token"]
    #     # logger.info("第一个用例，接口地址：{0}，接口的入参是{1},入参类型{2}，接口的状态码{3}接口的响应值{4}".
    #     #             format(self.TEST_URL+'login',payload,type(payload),response.status_code,res))
    #     #
        res=self.client.send_request("post",name='login',data=payload,) #发送请求
    #     self.assertEqual(res['msg'],'登录成功')
    def test02_userlist(self):
        payload={}
        headers = {
            'token':'1',
        }
        # response = requests.request("GET", self.TEST_URL+'user/list', headers=headers )
    #     # logger.info("第一个用例，接口地址：{0}，接口的入参是{1},入参类型{2}，接口的状态码{3}接口的响应值{4}".
    #     #             format(self.TEST_URL + 'user/list', payload, type(payload), response.status_code, response.json()))
        res=self.client.send_request("get",name='user/list',data=payload,headers=headers)
    #     self.assertEqual(len(res['data']),2)
    #

    def test_interface(self):
        '''所有的接口用例 ，100多少组数据， 只用写一个函数的情况下，依次运行所有100接口，
        而且生成相应的100测试报告 '''
if __name__=="__main__":
    #unittest.main()
    testcase=unittest.TestSuite()  #创建一个测试套件
    testcase.addTests(unittest.TestLoader().loadTestsFromTestCase(API_TestCase))  #套件增加用例
    dir=r'D:\测码\VIP\2020.03.05-接口自动化实战\request_testcase\report\test.html'
    file = open(dir, 'wb')
    runner = HTMLTestRunner(stream=file, title='接口自动化测试报告', description='描述信息')
    runner.run(testcase)
