import rsa
import base64

def to_encrypt(msg):
    server_pub = """
    -----BEGIN PUBLIC KEY-----
    MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDQENQujkLfzfc5Tu9Z1LprzedE
    O3F7gs+7bzrgPsMl29LX8UoPYvIG8C604CprBQ4FkfnJpnhWu2lvUB0WZyLq6sBr
    tuPorOc42+gLnFfyhJAwdZB6SqWfDg7bW+jNe5Ki1DtU7z8uF6Gx+blEMGo8Dg+S
    kKlZFc8Br7SHtbL2tQIDAQAB
    -----END PUBLIC KEY-----
    """
    msg = msg.encode("utf-8")
    pub_key = server_pub.encode("utf-8")
    pubilc_key_obj = rsa.PublicKey.load_pkcs1_openssl_pem(pub_key)
    cryto_msg = rsa.encrypt(msg, pubilc_key_obj)
    cipher_base64 = base64.b64encode(cryto_msg)
    return cipher_base64.decode()

if __name__ == '__main__':
    data = "musen"
    cryto_info = to_encrypt(data)
    print(cryto_info)