import smtplib, ssl
import os
import streamlit as st

def send_mail(message, receiver):
    host = 'smtp.gmail.com'
    port = 465

    username = st.secrets["EMAIL_USER"]
    password = st.secrets["EMAIL_PASS"]

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
