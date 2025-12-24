# 📚 Scientific Paper RAG Database & Dashboard

This project aims to **ingest scientific articles (from arXiv)**, extract structured content from PDFs, store it in a **relational + vector database**, and provide an **interactive Streamlit dashboard** to explore papers, authors, domains, categories, and chunks.  
The architecture is designed to be **RAG-ready (Retrieval-Augmented Generation)**.

---

## 🚀 Features

### 📄 Data Ingestion
- Fetch papers metadata from **arXiv** (title, abstract, authors, categories, publication date).
- Download PDFs and parse them using **Docling**.
- Extract:
  - Text blocks
  - Equations
  - Captions
  - Structured sections
  - ...

### ✂️ Chunking & Embeddings
- Split documents into semantic chunks.
- Generate vector embeddings using **Sentence Transformers**.
- Store embeddings using **pgvector** (SQLite during development).

### 🗄️ Database Design
Relational schema with SQLAlchemy:
- **Paper**
- **Author**
- **Domain**
- **Category**
- **Chunk** (with vector embeddings)

Supports:
- Many-to-many relations (papers ↔ authors, papers ↔ categories)
- Cascade deletion
- Efficient indexing for search & filtering

### 📊 Streamlit Dashboard
- Global metrics (papers, authors, domains, categories)
- Filter papers by:
  - Domain
  - Category
  - Publication date range
- Detailed paper view:
  - Authors, domains, categories
  - Abstract
  - Number of chunks
- Dedicated chunk view per paper
- Page-to-page navigation with session state

## 🧱 Tech Stack

- **Python 3.11.9**
- **SQLAlchemy**
- **SQLite** (development) / **PostgreSQL + pgvector** (production)
- **Sentence Transformers**
- **Docling**
- **Streamlit**
- **arXiv API**

## 🔎 RAG-READY (In Progress)

This project is designed as a foundation for a **Retrieval-Augmented Generation (RAG)** system.

Current capabilities:
- Scientific papers ingestion (arXiv)
- PDF parsing and structured extraction (text, equations, sections)
- Chunking strategy aligned with embedding constraints
- Vector embeddings stored in a PostgreSQL database using `pgvector`
- Rich metadata schema (papers, authors, domains, categories)
- Interactive Streamlit dashboard for exploration and inspection

Planned next steps:
- Semantic search over chunks using vector similarity
- Hybrid retrieval (metadata filtering + vector search)
- RAG pipeline integration with an LLM
- Question answering over scientific papers
- Chunk-level provenance and citation tracking

Status: **under active development**
