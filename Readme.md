# RAG Application with Groq, LangChain, LangSmith, and ChromaDB

This project is a **Retrieval-Augmented Generation (RAG)** application that allows users to query their own documents using a large language model powered by **Groq**.  
It combines document ingestion, vector search, and conversational generation, with observability via **LangSmith** and persistence via **ChromaDB**.

The application supports **per-user isolation** using a `user_id`, enabling multi-user usage without cross-contamination of data.

---

## Architecture Overview

At a high level, the system works as follows:

1. **Document Ingestion**
   - User uploads documents.
   - Documents are chunked and embedded using LangChain.
   - Embeddings are stored in ChromaDB under a user-specific namespace.

2. **Retrieval**
   - A query is embedded.
   - Relevant chunks are retrieved from ChromaDB for the given `user_id`.

3. **Generation**
   - Retrieved context is injected into a prompt.
   - Groq-hosted LLM generates the final response.

4. **Observability**
   - All chains, prompts, and LLM calls are traced using LangSmith.

---

## Tech Stack

- **Groq** – Fast LLM inference
- **LangChain** – Orchestration framework
- **LangSmith** – Tracing, debugging, and evaluation
- **ChromaDB** – Vector database for document retrieval
- **Streamlit** – Web UI
- **Python 3.9+**

---

## Features

- Retrieval-Augmented Generation (RAG)
- Multi-user support via `user_id`
- Persistent vector storage with ChromaDB
- File upload and ingestion
- Query-based document search
- LangSmith tracing for debugging and evaluation
- Fast inference using Groq

---

## Project Structure

```text
.
├── app.py                # Streamlit application
├── rag/
│   ├── app.py            # RAG App class (ingest, retrieve, generate)
│   ├── retriever.py      # ChromaDB retriever logic
│   ├── llm.py            # Groq LLM configuration
│   └── prompts.py        # Prompt templates
├── uploads/              # Temporary uploaded files
├── chroma/               # ChromaDB persistence directory
├── requirements.txt
└── README.md
```

## Environment Variables
```bash
GROQ_API_KEY
LLM_BASE_URI
MODEL_NAME
EMBEDDING_MODEL_API_KEY
EMBEDDING_MODEL
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT
LANGSMITH_API_KEY
LANGSMITH_PROJECT
```

## Installation
```bash
git clone https://github.com/sanjeet145/rag-application.git
cd rag-application
python -m venv venv
venv/bin/activate 
pip install -r requirements.txt
```

## Running the application
```bash
streamlit run app.py
```