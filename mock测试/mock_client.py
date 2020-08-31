#利用request发送post请求给服务端
import requests

# body={
#     'd1':'hi',
#     'd2':'falsk123123123123'
# }
#
# resp=requests.post('http://127.0.0.1:9090/post',data=body)
# print(resp.text)

data={
    'out_trade_no':'20150320010101001',
    'auth_code':'2876344382566439',
    'buyer_id':'2088202954065786',
    'seller_id':'2088102146225135',
    'subject':'Iphone6',
    'total_amount':'88.88',
}

resp=requests.post('http://127.0.0.1:9090/trade/purchase',json=data)
print(resp.json())