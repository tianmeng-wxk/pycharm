
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5

"""
使用说明：请先安装模块  Crypto

安装命令：pip3  install Crypto

该库python2 名为Crypto，模块内部导入全部是基于Crypto，
python3中模块名虽然改为crypto，内部导入依然使用的是Crypto,
因此，安装好了之后，需要找到该模块，手动修改包名为Crypto，才可以正常使用

"""


def encryption(msg):
    """
    公钥加密
    :param msg: 要加密内容
    :type msg:str
    :return:  加密之后的密文
    """
    # 获取公钥内容
    key = '-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDQENQujkLfZfc5Tu9Z1LprzedE\nO3F7gs+7bzrgPsMl29LX8UoPYvIG8C604CprBQ4FkfnJpnhWu2lvUB0WZyLq6sBr\ntuPorOc42+gLnFfyhJAwdZB6SqWfDg7bW+jNe5Ki1DtU7z8uF6Gx+blEMGo8Dg+S\nkKlZFc8Br7SHtbL2tQIDAQAB\n-----END PUBLIC KEY-----\n'
    publickey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(publickey)

    # 分段加密
    cipher_text = []
    for i in range(0, len(msg), 80):
        cont = msg[i:i + 80]
        cipher_text.append(cipher.encrypt(cont.encode()))

    # base64进行编码
    cipher_text = b''.join(cipher_text)

    cipher_result = base64.b64encode(cipher_text)
    return cipher_result.decode()


def decrypt(msg):
    """
    私钥进行解密
    :param msg: 密文
    :type msg:str
    :return: 解密之后的内容

    """
    # base64解码
    msg = base64.b64decode(msg)
    # 获取私钥
    privatekey = open('rsa_private_key.pem').read()
    rsakey = RSA.importKey(privatekey)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    # 分段进行解密
    text = []
    for i in range(0, len(msg), 128):
        cont = msg[i:i + 128]
        text.append(cipher.decrypt(cont, '解密失败'))

    text = b''.join(text)
    return text.decode()


if __name__ == '__main__':
    # 案例：
    # 待价密内容
    msg = '{"retcode":0,"result":{"result":0,"agency_course_category":[{"type":0,"id":"15380424295395507","title":"免费课"},{"type":0,"id":"15380424295395508","title":"试听课"},{"type":0,"id":"15380406286796005","title":"自动化测试"},{"type":0,"id":"14924071315271203","title":"软件测试就业"},{"type":0,"id":"15380406286796004","title":"管理/ISTQB证"},{"type":0,"id":"15380406286796003","title":"测试高薪速成"},{"type":1,"id":"15380406286796006","title":"高级测试开发"},{"type":0,"id":"14924071315271202","title":"性能测试"}]}}'

    # 加密操作
    en_msg = encryption(msg=msg)
    print('加密密文：', en_msg)

    # # 解密操作
    data = decrypt(en_msg)
    print('解密后明文：', data)
