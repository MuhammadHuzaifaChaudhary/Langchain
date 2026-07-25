# 🚀 LangChain Multi-Provider Intelligence Hub

A professional, production-grade implementation of the **LangChain** ecosystem. This repository demonstrates how to build modular, hardware-agnostic AI applications by seamlessly hot-swapping between world-class inference providers for both Chat Completions and Vector Embeddings.

---

## ✨ Features

* **🧩 Multi-Provider Integration:** Switch seamlessly between **Google Gemini**, **Groq Engine**, **NVIDIA NIM**, and **Hugging Face** endpoints.
* **🛡️ Secure Token Matrix:** Production-safe configuration using isolated `.env` files coupled with rigorous strict parameter validations.
* **🧬 Semantic Vectors Engine:** Text data conversion into numerical embeddings arrays leveraging Google’s enterprise-grade `text-embedding-004` model.
* **🔥 Dynamic Error Fail-safes:** Engineered with strict `try-except` blocks ensuring the pipeline executes effortlessly even if specific provider keys are throttled or empty.

---

## 🏗️ Architecture Blueprint

```text
my-ai-hub/
│
├── .env                # Hardware secret tokens (Securely ignored by Git)
├── .gitignore          # Production security parameters (.env & virtual loops locked)
├── requirements.txt    # Standard universal production dependencies
├── app.py              # Multi-Provider Chat Completions Core Engine
└── embeddings.py       # Semantic Text-to-Vector Embedding System
```

---

## 📊 Core Dependencies (`requirements.txt`)

Our universal platform pipeline runs efficiently on standard production packages:
```text
langchain-core
langchain-groq
langchain-google-genai
langchain-nvidia-ai-endpoints
langchain-huggingface
python-dotenv
```

---

## 🛠️ Step-by-Step Execution Guide

### 1. Repository Setup
Clone this workspace and jump into the dynamic production environment:
```bash
git clone https://github.com
cd langchain_models
```

### 2. Dependency Tracking
Install all core and model connectors instantly using `uv` or standard package management tools:
```bash
uv pip install -r requirements.txt
```

### 3. Environment Allocation
Create a `.env` locker file in the core project folder and insert your generated API keys:
```text
GROQ_API_KEY=gsk_your_groq_key_here
GOOGLE_API_KEY=AIzaSy_your_gemini_key_here
NVIDIA_API_KEY=nvapi-your_nvidia_key_here
HUGGINGFACEHUB_API_TOKEN=hf_your_inference_token_here
```

### 4. Running the Pipelines

* **For Chat Completions:** Execute the modular multi-provider model call script:
  ```bash
  python app.py
  ```
* **For Text-to-Vector Embeddings:** Execute the high-speed semantic calculations script:
  ```bash
  python embeddings.py
  ```

---

## 📈 Roadmap (Future Scope)
- [ ] Integration of persistent local Vector Stores (ChromaDB / FAISS) for custom PDF parsing.
- [ ] Memory-buffered multi-turn conversation conversational layout.
- [ ] Frontend user configuration panel engineered with Streamlit.

---
*Maintained as an advanced framework implementation to demonstrate runtime stability, dynamic model selection, and standardized prompt-inference pipelines.*
