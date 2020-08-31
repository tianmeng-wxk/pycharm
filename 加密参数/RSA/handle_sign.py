import rsa
import base64

# 需要安装rsa模块, pip install rsa

import rsa
import base64
def to_encrypt(msg):
    """
    非对称加密
    :param msg: 待加密字符串或者字节
    :param pub_key: 公钥
    :return: 密文
    """
    server_pub = """
        -----BEGIN PUBLIC KEY-----
        MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDQENQujkLfZfc5Tu9Z1LprzedE
        O3F7gs+7bzrgPsMl29LX8UoPYvIG8C604CprBQ4FkfnJpnhWu2lvUB0WZyLq6sBr
        tuPorOc42+gLnFfyhJAwdZB6SqWfDg7bW+jNe5Ki1DtU7z8uF6Gx+blEMGo8Dg+S
        kKlZFc8Br7SHtbL2tQIDAQAB
        -----END PUBLIC KEY-----
        """
    msg = msg.encode('utf-8')
    pub_key = server_pub.encode("utf-8")
    public_key_obj = rsa.PublicKey.load_pkcs1_openssl_pem(pub_key)  # 创建 PublicKey 对象
    cryto_msg = rsa.encrypt(msg, public_key_obj)  # 生成加密文本
    cipher_base64 = base64.b64encode(cryto_msg)  # 将加密文本转化为 base64 编码

    return cipher_base64.decode()  # 将字节类型的 base64 编码转化为字符串类型


if __name__ == '__main__':
    data = "musen"
    cryto_info = to_encrypt(data)
    print(cryto_info)
