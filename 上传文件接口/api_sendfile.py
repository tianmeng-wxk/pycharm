import requests

def send_file():
    url = "http://httpbin.org/post"
    data = ""
    #这种写法一个key可以传多个文件
    files = [
        ('images', ('images.jpg', open('./img/timg.jpg', 'rb'), 'image/png')),
        ('images', ('images2.jpg', open('./img/ti.jpg', 'rb'), 'image/png'))
    ]

    res = requests.post(url=url,files=files)
    print(res.text)

send_file()