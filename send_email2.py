import smtplib
from email.mime.text import MIMEText
#from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.header import Header

message = MIMEMultipart()
#邮件内容
text = """
请输入你想说的邮件内容
"""
message.attach(MIMEText(_text=text, _subtype='plain', _charset="utf-8"))
#需要发送的附件的路径
with open(r"F:\脚本\pycharm\report.html", 'rb') as f:
    content = f.read()
att1 = MIMEText(content, "base64", "utf-8")
att1["Content-Type"] = 'application/octet-stream'
att1['Content-Disposition'] = 'attachment; filename = "report.html"'
message.attach(att1)

#邮件主题
message["Subject"] = Header("主题", "utf-8").encode()
message["From"] = Header("tianmeng", "utf-8")
message["To"] = Header('tianmeng_wxk', "utf-8")

try:
    smtp = smtplib.SMTP()
    #smtp = smtplib.SMTP_SSL('smtp.163.com', 465)
    smtp.connect(host="smtp.qq.com", port=587)
    smtp.login(user="3394788013@qq.com", password="lizceyidpekpdbhd")
    sender = "3394788013@qq.com"
    receiver = ['tianmeng_wxk@163.com']
    smtp.sendmail(sender, receiver, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print(e)
