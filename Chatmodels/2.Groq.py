from langchain_groq import ChatGroq
# for openai we will run the command 
# from lanchain_openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# 2. Model initialize kiya (Ab Groq() ki jagah ChatGroq() use hoga)
model = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="openai/gpt-oss-120b" , temperature=0.1 # Groq ka fast model
)

# 3. LangChain ke tareeqe se AI ko call kiya (invoke kiya)
response = model.invoke("what is capital of pakistan ")

print(response)

# just like previous one .. but in previous one we can use groq instead og chatgroq
# reponse.content will give the content of the response but if we want to get the whole response then we can use print(response)