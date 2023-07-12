import smtplib, ssl
import os

port = 465
smtp_server = "smtp.gmail.com"
#USERNAME = os.environ.get('USER_EMAIL')
#PASSWORD = os.environ.get('USER_PASSWORD')
USERNAME = os.environ.get('USER_EMAIL1')
PASSWORD = os.environ.get('USER_PASSWORD1')
message = """\
Subject: GitHub Email Report

This is your daily email report.
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(USERNAME,PASSWORD)
    server.sendmail(USERNAME,USERNAME,message)
