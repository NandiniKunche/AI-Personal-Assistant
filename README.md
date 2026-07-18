# 🤖 AI Personal Assistant

An AI-powered Personal Assistant built using **Python, Streamlit, Groq Llama 3.3, FAISS, and Sentence Transformers**. The assistant supports long-term memory, semantic search, voice input, and intelligent memory management.

---

## ✨ Features

- 💬 Interactive Chat Interface
- 🧠 Long-Term Memory using FAISS
- 🔍 Semantic Memory Retrieval
- ♻️ Intelligent Memory Replacement
- 🎤 Voice Input Support
- 📅 Current Date & Time Awareness
- 💾 Persistent Memory Across Sessions
- ⚡ Powered by Groq Llama 3.3

---

## 🛠 Tech Stack

- Python
- Streamlit
- Groq API
- FAISS
- Sentence Transformers
- SpeechRecognition
- NumPy

---

## 📂 Project Structure

```
AI-Personal-Assistant
│
├── chatbot
│   ├── llm.py
│   ├── memory.py
│   ├── memory_filter.py
│   ├── memory_decision.py
│   ├── speech.py
│   └── utils.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Installation

```bash
git clone https://github.com/NandiniKunche/AI-Personal-Assistant.git

cd AI-Personal-Assistant

python -m venv myenv

myenv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
```

---

## 🔑 Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

## 📌 Key Features

- Conversational AI Assistant
- Long-Term Memory using Vector Embeddings
- Semantic Memory Search
- Voice-to-Text Input
- Intelligent Memory Updating
- Persistent Memory Storage

---

## 📄 License

This project is created for educational and learning purposes.
