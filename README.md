


# 🤖 Hdnx Handbook Bot

A lightweight, streamlit-based internal documentation assistant.  
Ask natural language questions about company processes — it will search across the internal handbook and return relevant, structured answers with Process IDs.

## 🔍 Features

- **RAG (Retrieval-Augmented Generation) Pipeline**
  - Combines **BM25 keyword retriever** and **OpenAI embedding-based retriever** (via FAISS)
  - Question rewriting to improve query understanding
  - Fusion retrieval for higher recall and precision
- **Natural language Q&A**
  - Accepts free-form English questions
  - Rewrites question into a better form for searching
  - Finds relevant documents and extracts Process IDs
- **Simple Web Interface**
  - Built with [Streamlit](https://streamlit.io)
  - Deployed to Streamlit Cloud
  - Can be embedded in Notion or internal tools

---

## 🛠️ Tech Stack

| Component            | Technology          |
|---------------------|---------------------|
| UI                  | Streamlit           |
| RAG Framework       | LangChain           |
| Vector Store        | FAISS               |
| Keyword Retriever   | BM25 (with spaCy tokenizer) |
| Embeddings          | OpenAI (`text-embedding-3-small`) |
| LLM                 | OpenAI GPT-3.5 / GPT-4o |
| Question Rewriting  | Prompt + GPT-4o     |
| Deployment          | Streamlit Cloud     |

---

## 📁 Project Structure

```
hdnx-handbook-bot/
│
├── app.py                  # Streamlit frontend
├── main.py                 # Main logic: RAG chain, query rewrite, tokenizer, etc.
├── data/
│   └── handbook_chunks.txt # Pre-chunked internal documentation
├── faiss_index/            # FAISS vector index
├── .streamlit/
│   └── secrets.toml        # Stores OpenAI API key in the streamlit cloud
├── requirements.txt        # For Streamlit Cloud compatibility and environment setup
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. 🔐 Create `.streamlit/secrets.toml`

```toml
OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxx"
```

This file is automatically recognized by Streamlit Cloud and should **not** be committed to Git.

---

### 2. 🧪 Local Development

1. Clone the repo
2. Create virtual environment (if using `uv` or `poetry`, follow your preferred setup)
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```
4. Start Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## 🚀 Deployment (Streamlit Cloud)

1. Push to a **public GitHub repo**
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and deploy a new app from the repo
3. In **Secrets**, add your `OPENAI_API_KEY`

---

## 📌 Notes

- The app uses a **hybrid retriever** (BM25 + FAISS) to cover both keyword and semantic matches.
- BM25 tokenizer is customized using `spaCy` to improve match quality.
- Relevant `Process IDs` are extracted from `####` headers in the source documents.
- Question rewriting uses GPT-4o to optimize search accuracy in the vector DB.
- The current version uses a static handbook dump — update `handbook_chunks.txt` if the handbook changes.

---

## 🧪 Example Usage

> **Q:** What is the procedure after a mapping mission?  
> **A:** Process IDs: 309, 289  
> The mapper must fill out a post-mission interview checklist, upload data, confirm all zones, and submit logs. A signed PDF is stored in the archive.

---

## 📬 Contact

Built with ❤️ by [Linda]  
Reach out on Slack/Github if anything breaks or you want to contribute.