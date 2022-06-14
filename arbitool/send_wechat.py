# coding:utf -8

import smtplib  # smtp服务器
from email.mime.text import MIMEText  # 邮件文本


class SendWechat:
    def __init__(self, subject: str, sender: str, content: str, recver: str, password: str):
        self.subject = subject  # 邮件标题
        self.sender = sender  # 发送邮箱，建议用163邮箱，并打开stmp功能
        self.content = content  # 邮件内容
        self.recver = recver  # 接受邮箱，使用qq邮箱，并在微信中打开qq邮箱提醒功能
        self.password = password  # 163邮箱的stmp密码，不是邮箱登录密码

    def send_wechat(self):
        message = MIMEText(self.content, "plain", "utf-8")
        # content 发送内容和"plain"文本格式，使用utf-8 编码格式
        message['Subject'] = self.subject
        message['To'] = self.recver
        message['From'] = self.sender
        smtp = smtplib.SMTP_SSL("smtp.163.com", 465)  # 实例化smtp服务器
        smtp.login(self.sender, self.password)  # 登录
        smtp.sendmail(self.sender, [self.recver], message.as_string())
        # as_string 对 message 的消息进行了封装
        smtp.close()
