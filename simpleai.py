from langchain.chat_models import init_chat_model

model = init_chat_model(model="gemini-3-flash-preview",
                        model_provider="google-genai",
                        api_key=GOOGLE_API_KEY
                        )

response = model.invoke("What's up?")
response_str = response.content
print(response_str)