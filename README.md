# 🧠 MEDIGPT – AI Healthcare Chatbot for Teenagers

An AI-powered healthcare chatbot designed specifically for teenagers that provides safe, context-aware, and easy-to-understand health guidance using Retrieval-Augmented Generation (RAG).

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Gradio](https://img.shields.io/badge/Gradio-UI-orange)
![FAISS](https://img.shields.io/badge/FAISS-VectorDB-green)
![RAG](https://img.shields.io/badge/RAG-AI-purple)
![Groq](https://img.shields.io/badge/Groq-LLM-red)

---

## 📌 Overview

MEDIGPT is a final-year research project that combines semantic search, vector databases, and Large Language Models to deliver reliable healthcare awareness for teenagers.

Unlike traditional chatbots, MEDIGPT retrieves relevant information from verified healthcare documents before generating responses, reducing hallucinations and improving factual accuracy.

---

## ✨ Features

- 💬 Natural conversational healthcare chatbot
- 🔍 Semantic search using Sentence Transformers
- 📚 Retrieval-Augmented Generation (RAG)
- ⚡ Fast inference using Groq API
- 🧠 FAISS vector database
- 🩺 Teenager-focused healthcare awareness
- 🛡️ Safety-aware response generation

---

## 🏗️ System Architecture

User Query → Embedding → FAISS Retrieval → Context Building → LLaMA 3.1 → Response

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend |
| Gradio | User Interface |
| FAISS | Vector Database |
| Sentence Transformers | Embeddings |
| Groq API | LLM Inference |
| NumPy | Vector Operations |
| Pickle | Metadata Storage |

---

## 📂 Project Structure

```text
MEDIGPT/
├── app.py
├── backend.py
├── requirements.txt
├── data/
│   ├── chunks/
│   ├── vector_store/
│   └── raw_pdfs/
├── assets/
├── docs/
└── README.md
```

## 🚀 Installation

```bash
git clone https://github.com/hOPeOP07/MediGPT-AI-Healthcare-Chatbot-for-Teenagers.git

cd MediGPT-AI-Healthcare-Chatbot-for-Teenagers

pip install -r requirements.txt

python app.py
```

The chatbot will run locally on:

```text
http://127.0.0.1:7860
```

---

## 📊 Research Contribution

**Research Paper:** AI Healthcare Chatbot for Teenagers

Presented at the **6th International Conference on Recent Trends in Engineering, Technology and Management (ICRETM 2026).**

The research focuses on reducing hallucination in healthcare conversational AI using Retrieval-Augmented Generation.

---

## 🎯 Future Scope

- Voice-based interaction
- Multilingual support
- Mobile application
- Doctor consultation integration
- Personalized wellness recommendations

---

## 👨‍💻 Author

**Shikhar Chaturvedi**

B.Tech Computer Science Engineering

AI • NLP • Healthcare Technology
