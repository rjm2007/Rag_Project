# 🧠 RAG-Powered PDF Query System using LangChain, HuggingFace, and Astra DB

This project allows you to query PDFs using a **RAG (Retrieval-Augmented Generation)** pipeline powered by:
- 📚 HuggingFace Embeddings (`allenai-specter`)
- 🔎 SemanticChunker for intelligent text splitting
- 🌐 AstraDB Vector Store
- 🤖 Groq LLM (`qwen-qwq-32b`)
- 🧠 LangChain for orchestration

---

## 📦 Features

- Extract **text**, **tables**, and **images** (OCR) from PDFs
- Split documents semantically using embeddings
- Store & retrieve chunks from AstraDB
- Generate answers using a Groq-hosted LLM

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/rag-pdf-query.git
cd rag-pdf-query
2. Install requirements
bash
Copy
Edit
pip install -r requirements.txt
3. Configure .env
Create a .env file with the following:

env
Copy
Edit
HUGGING_FACE_TOKEN=your_huggingface_token
GROQ_API_KEY=your_groq_api_key
ASTRA_DB_API_ENDPOINT=https://your-endpoint.apps.astra.datastax.com
ASTRA_DB_APPLICATION_TOKEN=your_astra_token
🔐 Never commit .env to GitHub!

🧪 Run the App
Update main.py with your PDF path:

python
Copy
Edit
pdf_path = "your-pdf-file.pdf"
Then run:

bash
Copy
Edit
python main.py
🛠️ Project Structure
bash
Copy
Edit
.
├── Astra_db.py              # Astra DB setup
├── loader.py                # PDF extractor (text, tables, OCR)
├── Semantic_splitter.py     # Embedding-based chunking
├── prompt_llm.py            # LLM + RAG chain setup
├── main.py                  # Pipeline execution
├── .env                     # API keys (ignored by git)
└── README.md
🤖 Example Query
Once running, the program will answer:

csharp
Copy
Edit
What is TableFormer?