import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.header import Header


msg = MIMEText(_text="python邮件发送测试...", _subtype='plain', _charset="utf-8")
msg["Subject"] = Header("python email send test","utf-8")
msg["From"] = Header("tianmeng","utf-8")
msg["To"] = Header('tianmeng_wxk',"utf-8")
smtp = smtplib.SMTP()
mail_host = "smtp.qq.com"
try:

    smtp.connect(host=mail_host, port="587")
    smtp.login(user="3394788013@qq.com",password="lizceyidpekpdbhd")
    sender = "3394788013@qq.com"
    to = "tianmeng_wxk@163.com"
    smtp.sendmail(sender, to, msg.as_string())
    print("发送成功")
except smtplib.SMTPException as e:
    print(e)
