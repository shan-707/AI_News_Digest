import requests
import streamlit as st
import sendmail
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()


api_key = "50ad419e81d84a69851d617bb30abdd7"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
NEWS_API_KEY = os.getenv("API_KEY")
url = ("https://newsapi.org/v2/top-headlines?"
       "country=us&"
       "category=business&"
       "language=en&"
       "pageSize=8&"
       "sortBy=publishedAt&"
       "apiKey="+NEWS_API_KEY)

# Make a request
request = requests.get(url)

# Create a Dictionary
content = request.json()
articles = content["articles"]


# AI SUMMARIZING THE NEWS
model = init_chat_model(model="gemini-3-flash-preview",
                        model_provider="google-genai",
                        api_key=GEMINI_API_KEY
                        )
news_text = "\n".join([a["title"] for a in articles if a["title"]])

prompt = f"""
You are a news summarizer.
Write a short paragraph analyzing the following headlines:

{news_text}
"""
response = model.invoke(prompt)
response_str = response.content[0]["text"]
body = "Subject: News Summary\n\n" + response_str + "\n\n"

st.title("News API App")
st.info("Get news sent to your email that you enter below.")
with st.form(key='sendmail_form'):
    user = st.text_input("Enter your email :", key="receiver")
    submit = st.form_submit_button("Send", key="send")
    if submit:
        body = body.encode('utf-8')
        sendmail.send_mail(message=body, receiver=user)

        st.success("Email sent successfully")