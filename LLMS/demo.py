from langchain_groq import ChatGroq
# for openai we will run the command 
# from lanchain_openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# 2. Model initialize kiya (Ab Groq() ki jagah ChatGroq() use hoga)
model = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="openai/gpt-oss-120b"  # Groq ka fast model
)

# 3. LangChain ke tareeqe se AI ko call kiya (invoke kiya)
response = model.invoke("what is captial of pakistan ")

print(response.content)
