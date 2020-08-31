import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.header import Header
smtp = smtplib.SMTP()
host = "smtp.qq.com"
port = 587
try:
    smtp.connect(host,port)
    user = "3394788013@qq.com"
    pwd = "lizceyidpekpdbhd"
    smtp.login(user,pwd)
    with open(r"F:\脚本\pycharm\report.html",'rb') as f:
        content = f.read()
    subject = "主题"
    send_user = "3394788013@qq.com"
    to_user = "tianmeng_wxk@163.com"
    msg_enclosure = MIMEMultipart()
    enclosure = MIMEApplication(content)
    enclosure.add_header('content-disposition', 'attachment', filename='report.html')
    msg = MIMEText("主题", _subtype='plain', _charset="utf-8")
    msg_enclosure.attach(msg)
    msg_enclosure.attach(enclosure)
    msg_enclosure["Subject"] = Header(subject)
    msg_enclosure["From"] = send_user
    msg_enclosure["To"] = to_user
    smtp.send_message(msg,send_user,to_user)
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print(e)
#smtp.send_message(msg_enclosure.as_string(),send_user,to_user)
