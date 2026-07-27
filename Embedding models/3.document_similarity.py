from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv
load_dotenv()
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embeddings=GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=os.getenv("GEMINI_API_KEY")
)
documents = [
    "Python is an amazing programming language for AI.",
    "Machine learning is a subset of artificial intelligence.",
    "Natural language processing is a field of AI that focuses on the interaction between computers and humans through natural language.",
    "Deep learning is a subset of machine learning that uses neural networks to model complex patterns in data.",
    "Computer vision is a field of AI that enables computers to interpret and understand visual information from the world.",
    "Reinforcement learning is a type of machine learning where an agent learns to make decisions by interacting with an environment and receiving feedback in the form of rewards or penalties.",
    "Generative AI refers to a class of artificial intelligence techniques that can generate new content"
]

query = "tell me about generative AI"
#  convert document and query into embeddings

doc_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

# now we will calculate the cosine similarity between the query embedding and each document embedding
# first we will send query embedding in a 2d list then doc embedding which is already in a list so we will send it as it is

cosine_similarities = cosine_similarity([query_embedding], doc_embeddings)[0]
index,score=sorted(list(enumerate(cosine_similarities)), key=lambda x: x[1])[-1]
print(query)
print(documents[index])
print("similarity score is ",score)


