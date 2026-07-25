from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Gemini 1.5 Pro Model Initialize kiya
model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0.7 # Creativity control karne ke liye
)

response = model.invoke("hello gemini what is json?")
print(response.content)
