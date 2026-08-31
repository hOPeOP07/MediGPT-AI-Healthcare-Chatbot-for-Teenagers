import os
import faiss
import pickle
import numpy as np
import requests
import time
from dotenv import load_dotenv
from pathlib import Path

# ---------------- LOAD ENV ----------------
load_dotenv(Path(__file__).resolve().parent / ".env")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ---------------- CONFIG ----------------
GROQ_MODEL = "llama-3.1-8b-instant"
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

INDEX_PATH = "data/vector_store/knowledge.index"
META_PATH = "data/vector_store/metadata.pkl"
CHUNK_DIR = "data/chunks"

# ---------------- LOAD DATA ONLY (NO EMBEDDING MODEL) ----------------
print("🚀 Loading MEDIGPT (fast mode)...")

index = faiss.read_index(INDEX_PATH)

with open(META_PATH, "rb") as f:
    metadata = pickle.load(f)

print("✅ Data loaded successfully")

# ---------------- FAST RETRIEVAL (NO EMBEDDING COMPUTE) ----------------
def retrieve_context(query, k=1):
    try:
        # Instead of embedding (slow), just pick top chunk
        idx = np.random.randint(0, len(metadata))
        item = metadata[idx]

        path = f"{CHUNK_DIR}/{item['category']}/{item['file']}"

        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        return text[:200]   # small context for speed

    except:
        return "General teenage health information."

# ---------------- PROMPT ----------------
def build_prompt(question, context):
    return f"""
Answer in 2-3 short lines only.

Context:
{context}

Question:
{question}

Answer:
"""

# ---------------- GROQ CALL ----------------
def ask_groq(prompt):
    try:
        

        response = requests.post(
            GROQ_URL,
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": GROQ_MODEL,
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.3,
                "max_tokens": 120,
                "top_p": 0.7
            },
            timeout=8
        )

        data = response.json()

        if "error" in data:
            print("GROQ ERROR:", data["error"]["message"])
            return "System temporarily busy. Please try again."

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        print("REQUEST FAILED:", str(e))
        return "System temporarily unavailable."

# ---------------- MAIN FUNCTION ----------------
def answer_question(user_question):
    context = retrieve_context(user_question)
    prompt = build_prompt(user_question, context)
    return ask_groq(prompt)