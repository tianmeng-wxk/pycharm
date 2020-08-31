import base64

data = {"code":1101,"data":"nifhajdk","msg":"登录成功"}

# base64编码 byte类型
data = data["msg"] # 转换为二进制
res = '55m75b2V5oiQ5Yqf'

def base64_encode(msg):
    res = base64.b64encode(msg.encode())#.encode()转换为二进制,因为base64编码为byte类型
    print("base64编码之后的内容：", res.decode())#。decode()二进制转为字符串类型

def base64_decode(msg):

    res = base64.b64decode(msg.encode())
    print("base64解码之后的内容：",res.decode())

if __name__ == '__main__':
    base64_encode(data)
    base64_decode(res)