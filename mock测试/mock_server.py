#什么是mock?
# 测试桩，模拟被测对象的返回，用于测试
#通常意义的mock指的就是mock server, 模拟服务端返回的接口数据，用于前端开发，第三方接口联调

#为什么要用Mock?
#1.前后端开发进度不一致，前端开发速度快于后端，需要一个假的接口用于模拟后端返回
#2.项目需要用到第三方接口，如果第三方接口未开发好，或者第三发接口没有测试环境，为了报证进度，所以需要模拟接口用于调试

#如何mock？
#1.利用抓包工具比如fiddler
#2.可以利用web框架模拟，Django  Flask  ---python web开发框架

# Flask的特点就是，结构简单，容易入门

#1.安装Flask,  pip install flask


#利用flask编写一个最简单的接口
import random
import time

from flask import Flask,request,json
#实例化一个web服务对象
app=Flask(__name__)


#创建一个方法来处理请求
#定义一个路由--访问服务的根目录就可以得到结果
@app.route('/')
def hello():
    return '<h1>hello flask</h1>'

#构造一个接受post请求的响应
@app.route('/post',methods=['POST'])
def test_post():
    #处理接口发送过来的两个参数，将两个参数合并成一个字符串返回
    d1=request.form['d1']
    d2=request.form['d2']
    return d1+d2
#处理极简交易接口
@app.route('/trade/purchase',methods=['POST'])
def purchase():
    #拿到客户端返回的数据
    res=json.loads(request.get_data())
    out_trade_no=res['out_trade_no']
    auth_code=res['auth_code']
    data={
        'code': '40004',
        'msg': 'Business Failed',
        'sub_code': 'ACQ.TRADE_HAS_SUCCESS',
        'sub_msg': '交易已被支付',
        'trade_no': '2013112011001004330000121536',
        'out_trade_no': '6823789339978248'
    }
    #把out_trade_no改成客户端发送过来的数据
    data['out_trade_no']=out_trade_no
    data['trade_no']=time.strftime('%Y%m%d%H%M%S')+str(random.random()).replace('0.','')
    #验证授权码
    if auth_code !='28763443825664394':
        return {'coode':'50000','msg':'请求码验证失败'}

    return data

if __name__ == '__main__':
    #运行服务，并确定服务运行的IP和端口
    app.run('127.0.0.1','9090')

