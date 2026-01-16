# Crypto_Research_Capstone
A capstone project created from the basic idea of Crypto Research
---

## 1. Project Overview

**Crypto Researcher** is an end-to-end AI-driven system designed to ingest real-time cryptocurrency and financial news, store it in a vector database, and provide **semantic, sentiment-aware, and summarized insights** through a modern interactive UI.

The system mimics a **real-world financial research workflow**, combining:

- Real-time data ingestion  
- Vector similarity search  
- Local LLM reasoning  
- Analyst-grade summaries  
- Responsive frontend UX  

**Domain:** AI in Finance  
**Primary Focus:** Real-time crypto market intelligence & research automation

---

## 2. Problem Statement

Crypto markets are:

- Highly volatile  
- News-driven  
- Sentiment-sensitive  

Existing solutions suffer from:

- Keyword-based search  
- Delayed aggregation  
- Generic summaries  
- Lack of explainability  

### ❌ Challenges Addressed

- Noise in crypto news  
- Poor relevance ranking  
- No sentiment context  
- Slow or opaque summarization  
- Vendor lock-in with cloud LLMs  

---

## 3. Project Objectives

### Core Objectives

1. Real-time news ingestion using a free-tier News API  
2. Semantic search over news articles using embeddings  
3. Vector database storage (mandatory requirement)  
4. Local LLM-based summarization  
5. Sentiment-aware analysis (bullish / bearish / neutral)  
6. Interactive UI with analyst-friendly presentation  

### Secondary Objectives

- Streaming (live token) summaries  
- Delta summaries (“what changed since last update?”)  
- Clean modular architecture  
- Production-grade testing with pytest  

---

## 4. Technology Stack

| Layer | Technology | Reason |
|-----|------------|--------|
| Backend API | FastAPI | High-performance, async-ready |
| Frontend | Streamlit | Rapid, interactive dashboards |
| Vector DB | **Qdrant** | Production-grade, metadata filtering |
| LLM Runtime | Ollama | Local & private AI |
| Embeddings | Ollama model | Semantic retrieval |
| Data Source | NewsAPI | Free tier access |
| Testing | Pytest | Reliable backend tests |
| Containerization | Docker | Reproducibility |

---

## 5. High-Level Architecture



---

## 6. Project Timeline & Milestones

> **Total Duration:** ~2 Days  
> **Methodology:** Incremental feature-driven development

---

### 🟩 STEP 1 — Project Setup & Infrastructure

**Objectives**

- Establish project structure  
- Choose vector database  
- Set up FastAPI + Qdrant  

**Key Decisions**

- Selected **Qdrant over Chroma** for  
  - Persistence  
  - Metadata filtering  
  - Production readiness  

**Outcome**

- Stable backend foundation  
- Independent vector database  

---

### 🟩 STEP 2 — News Ingestion Pipeline

**Implemented**

- News API integration  
- Normalization  
- Embedding generation  
- Sentiment classification  
- Qdrant upsert  

**Enhancement**

- Background ingestion using FastAPI tasks  

**Outcome**

- Non-blocking real-time ingestion  

---

### 🟩 STEP 3 — Semantic Search

**Implemented**

- Query embedding  
- Similarity search  
- Score ranking  

**Outcome**

- Meaning-based retrieval instead of keywords  

---

### 🟩 STEP 4 — AI Summarization

**Implemented**

- Sentiment-aware summaries  
- Prompt constraints  
- Cleanup pipeline  

**Outcome**

- Actionable market insights  

---

### 🟩 STEP 5 — Streaming Output

**Implemented**

- Ollama streaming  
- FastAPI StreamingResponse  
- Live Streamlit rendering  

**Outcome**

- Real-time AI responses  

---

### 🟩 STEP 6 — Frontend UI

**Implemented**

- Cyberpunk theme  
- Summary cards  
- Sentiment badges  
- Ranked sources  

**Outcome**

- Professional analyst dashboard  

---

### 🟩 STEP 7 — Testing

**Implemented**

- Pytest suite  
- API tests  
- Service unit tests  
- Mocking external calls  

**Outcome**

- CI-ready deterministic tests  

---

## 7. Key Functionalities

- Real-time ingestion  
- Vector semantic search  
- Sentiment-aware summaries  
- Streaming AI output  
- Modern UI  
- Local AI stack  

---

## 8. Why This Project Stands Out

- Production vector DB  
- Local LLM privacy  
- Async ingestion design  
- Clean separation of concerns  
- Finance-first usefulness  

---

## 9. Future Enhancements

- Delta comparisons  
- Asset clustering  
- Alerts on sentiment shifts  
- Scheduled ingestion  
- Auth system  

---

## 10. How to Run

```bash
# Start Qdrant
docker run -d -p 6333:6333 qdrant/qdrant

# Backend
uvicorn app.main:app --reload

# Frontend
streamlit run streamlit/ui.py
