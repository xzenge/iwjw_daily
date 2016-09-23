# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os

class MyEmail:
    def __init__(self):
        self.user = None
        self.passwd = None
        self.to_list = []
        self.cc_list = []
        self.tag = None
        self.doc = None

    #发送邮件
    def send(self):
        try:
            with smtplib.SMTP_SSL("smtp.exmail.qq.com", port=465) as server:
                server.login(self.user, self.passwd)
                server.sendmail(self.user, self.to_list, self.get_attach())
                print("send email successful")
        except Exception as e:
            print("send email failed {0}".format(e))

    #构造邮件
    def get_attach(self):
        msg = MIMEMultipart()
        now = datetime.now().strftime('%Y%m%d')
        if self.tag is not None:
            # 主题,最上面的一行
            tag = '工作日报{0}-史翔'.format(now)
            msg["Subject"] = tag
        if self.user is not None:
            # 显示在发件人
            msg["From"] = self.user
        if self.to_list:
            # 收件人列表
            msg["To"] = ";".join(self.to_list)
        if self.cc_list:
            # 抄送列表
            msg["Cc"] = ";".join(self.cc_list)
        if self.doc:
            path = self.doc +  '\\' + now + '.txt'
            if not os.path.exists(path):
                raise Exception
            with open(path,'r',encoding='utf-8') as f:
                content = f.read()
                msg.attach(MIMEText(content, 'plain', 'utf-8'))

        return msg.as_string()


if __name__ == "__main__":
    my = MyEmail()

    my.user = "shixiang.sh@superjia.com"
    my.passwd = "Sx56242522"
    my.to_list = ["376574680@qq.com", ]
    my.cc_list = ["376574680@qq.com", ]
    my.doc = u"d:\daily"
    my.tag = True
    my.send()