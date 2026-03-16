import smtplib, ssl
import os

def send_mail(message, receiver):
    host = 'smtp.gmail.com'
    port = 465

    username = 'shandevacc@gmail.com'
    password = os.getenv('PASSWORD')

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
