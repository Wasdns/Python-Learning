#!/usr/bin/env python

from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

# QQ mail smtp server
host_server = 'smtp.qq.com'

# sender QQ
sender_qq = '952693358'

# pwd
pwd = '***'

# sender qqmail
sender_qq_mail = '952693358@qq.com'

# receiver QQ
receiver = '952693358@qq.com'

# content
mail_content = 'Hi, you are being attacked!'

# title
mail_title = 'Hello'

# SSL login
smtp = SMTP_SSL(host_server)
smtp.set_debuglevel(1) # debug
smtp.ehlo(host_server)
smtp.login(sender_qq, pwd)

msg = MIMEText(mail_content, "plain", 'utf-8')
msg['Subject'] = Header(mail_title, 'utf-8')
msg['From'] = sender_qq_mail
msg['To'] = receiver

for i in range(10):
	smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
smtp.quit()
