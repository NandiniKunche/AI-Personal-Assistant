# 🤖 AI Personal Assistant

An intelligent AI Personal Assistant built using **Streamlit**, **Groq LLM**, and **FAISS Vector Database**. It provides conversational AI with long-term memory, voice input, and persistent memory across sessions.

---

## 🚀 Features

- 💬 Chat-based interface
- 🧠 Long-term memory using FAISS
- 🔍 Semantic memory search
- ♻️ Intelligent memory replacement
- 🎤 Voice input support
- 📅 Current date & time awareness
- 💾 Persistent memory across application restarts
- ⚡ Powered by Groq Llama 3.3

---

## 🛠️ Tech Stack

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
AI-Personal-Assistant/
│
├── chatbot/
│   ├── llm.py
│   ├── memory.py
│   ├── memory_filter.py
│   ├── memory_decision.py
│   ├── speech.py
│   └── __init__.py
│
├── memory/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## ⚙️ Installation

```bash
git clone <repository-url>

cd AI-Personal-Assistant

python -m venv myenv

myenv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
```

---

## 🔑 Environment Variable

Create a `.env` file.

```
GROQ_API_KEY=your_api_key_here
```

---

## 📸 Features Demonstrated

- AI Chat
- Voice Input
- Long-Term Memory
- Persistent Memory
- Semantic Search
- Date & Time Responses

---

## 📄 License

This project is for educational purposes.