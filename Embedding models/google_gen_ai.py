import os
from dotenv import load_dotenv
# 1. Google ka official Embeddings connector import kiya
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

# 2. Embeddings model initialize kiya
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    #  write models/gemini instead of text-embedding-004
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# 3. Kisi bhi text ko numbers (Vector) mein badla
text_data = "Python is an amazing programming language for AI."
vector = embeddings.embed_query(text_data)

# Screen par numbers ki lambi list (Array) print ho jayegi!
print("Text converted into Numbers (Vector):")
print(vector[:10]) # Sirf pehle 10 numbers dekhne ke liye
print(f"\nTotal Dimensions (Length of numbers list): {len(vector)}")
