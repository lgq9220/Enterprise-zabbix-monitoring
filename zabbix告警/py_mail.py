#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication
 
sender = 'XXXXXX'
receivers = ['XXXXXX','XXXXXX']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
#创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("运维监控组", 'utf-8')
message['To'] = Header("运维监控组", 'utf-8')
subject = '一周周报,详情请查看报表'
message['Subject'] = Header(subject, 'utf-8')
 
#邮件正文内容
message.attach(MIMEText(subject, 'plain', 'utf-8'))
 
try:
    smtpObj = smtplib.SMTP('smtp.139.com')
    smtpObj.login('XXXXXXXX','XXXXXXXXX')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException as e:
    print e," Error: 无法发送邮件"
