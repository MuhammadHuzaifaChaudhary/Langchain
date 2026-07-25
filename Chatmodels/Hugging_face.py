import os
from dotenv import load_dotenv
# LangChain ka official Hugging Face connector
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

# 1. Pehle Endpoint tayyar kiya (Bina paid endpoint ke aap unka free hub model address bhi de sakte hain)
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta", # Ek mashhoor open-source model
    text="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
    # it is optional to write huggingfaceapi_token if you have already set it in your environment variables

)

# 2. Use ChatModel mein badal diya taake standard chat format chal sake
chat_model = ChatHuggingFace(llm=llm)

# 3. Standard invoke method chalaya
response = chat_model.invoke("Hello Hugging Face! What are embeddings?")
print(response.content)
