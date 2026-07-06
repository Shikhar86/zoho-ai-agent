# Zoho AI Email Assistant

An AI-powered email assistant built using **FastAPI**, **LangGraph**, **Ollama**, **FAISS**, and **Tavily Search**.

The assistant analyzes incoming emails, determines what information is required, retrieves relevant company knowledge and previous conversation history, performs internet searches when necessary, and generates a professional email reply.

---

# Project Architecture

```
                   Incoming Email
                          │
                          ▼
                    FastAPI API
                          │
                          ▼
                    LangGraph Graph
                          │
                          ▼
                     Analyzer Agent
                          │
                          ▼
                     Planner Agent
                          │
      ┌───────────────┬───────────────┬───────────────┐
      ▼               ▼               ▼
 Memory Agent   Company Agent   Search Agent
      │               │               │
      ▼               ▼               ▼
 Memory RAG     Company RAG      Tavily Search
      └───────────────┴───────────────┘
                      │
                      ▼
                 Writer Agent
                      │
                      ▼
                Reviewer Agent
                      │
                      ▼
                 Final Email Reply
```

---

# Entry Point

The application starts from:

```
api.py
```

Run the backend:

```bash
uvicorn api:app --reload
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

# API Endpoint

### POST `/generate_reply`

Example Request

```json
{
    "email_subject": "Refund",
    "email_body": "Can I get my money back?",
    "thread_context": ""
}
```

Example Response

```json
{
    "analysis": {...},
    "plan": {...},
    "final_reply": "..."
}
```

---

# Execution Flow

1. FastAPI receives the email.
2. A shared **state** object is created.
3. LangGraph executes the workflow.
4. Each agent updates the shared state.
5. The final reply is returned to the API.

```
FastAPI
    │
graph.invoke(state)
    │
Analyzer
    │
Planner
    │
Memory
    │
Company
    │
Search
    │
Writer
    │
Reviewer
    │
Return Response
```

---

# Project Structure

```
zoho-ai-agent/

│
├── app/
│   ├── agents/
│   ├── graphs/
│   ├── services/
│   ├── repositories/
│   ├── vectorstore/
│   ├── memory/
│   ├── knowledge/
│   ├── memory_data/
│   ├── prompts/
│   └── models/
│
├── api.py
├── main.py
├── oauth_server.py
├── requirements.txt
└── .env
```

---

# Folder Responsibilities

## agents/

Contains all AI agents.

- analyzer.py
- planner.py
- memory.py
- company.py
- search.py
- writer.py
- reviewer.py

Each agent performs one specific task.

---

## graphs/

Contains the LangGraph workflow.

Current execution order:

```
Analyzer
↓

Planner
↓

Memory

↓

Company

↓

Search

↓

Writer

↓

Reviewer
```

---

## services/

Contains business logic.

Services decide **how** information should be retrieved.

Example:

```
Company Agent

↓

Company Service
```

---

## repositories/

Repositories hide the data source.

Instead of agents directly accessing FAISS or APIs, they call repositories.

```
Agent

↓

Service

↓

Repository

↓

Retriever

↓

Data Source
```

This makes replacing the backend storage very easy.

---

## vectorstore/

Contains the Company Knowledge RAG.

Files:

- build_index.py
- retriever.py
- company_index/

Uses:

- FAISS
- Ollama Embeddings

---

## memory/

Contains Memory RAG.

Files:

- build_index.py
- retriever.py
- memory_index/

Uses:

- FAISS
- Ollama Embeddings

---

## knowledge/

Contains company knowledge documents.

Current example files:

- refund.txt
- pricing.txt
- support.txt
- meeting.txt

Future:

Replace with company PDFs, documentation, or knowledge base.

---

## memory_data/

Contains previous conversation examples.

Current:

- meeting.txt
- quotation.txt

Future:

Replace with actual Zoho email threads.

---

# Agents

## Analyzer

Reads the email and extracts:

- Intent
- Urgency
- Tone
- Summary
- Questions
- Requires Memory
- Requires Search
- Requires Human

---

## Planner

Uses the analyzer output to determine which agents should execute.

Example:

```python
{
    "memory": True,
    "company_context": True,
    "internet_search": False,
    "generate_reply": True,
    "review_reply": True
}
```

---

## Memory Agent

Retrieves previous conversation context.

Flow:

```
Memory Agent

↓

Memory Service

↓

Memory Repository

↓

Memory Retriever

↓

Memory FAISS
```

---

## Company Agent

Retrieves company knowledge.

Flow:

```
Company Agent

↓

Company Service

↓

Company Repository

↓

Company Retriever

↓

Company FAISS
```

---

## Search Agent

Runs only when the planner decides internet search is required.

Uses:

- Tavily Search API

---

## Writer

Receives:

- Original Email
- Company Context
- Memory Context
- Internet Context

Generates a professional draft reply.

---

## Reviewer

Improves:

- Grammar
- Professionalism
- Clarity

Returns the final email.

---

# Shared State

LangGraph shares one state object between every agent.

Example:

```python
state = {

    "email_subject": "...",

    "email_body": "...",

    "analysis": {},

    "plan": {},

    "memory_context": "",

    "company_context": "",

    "internet_context": "",

    "draft_reply": "",

    "final_reply": ""

}
```

Every agent only updates its own section.

---

# Technologies Used

- Python
- FastAPI
- LangGraph
- LangChain
- Ollama
- Llama 3
- Nomic Embeddings
- FAISS
- Tavily Search

---

# Setup

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

Windows

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Pull Ollama Models

```bash
ollama pull llama3

ollama pull nomic-embed-text
```

---

## Configure Environment

Create a `.env` file containing:

- TAVILY_API_KEY
- ZOHO_CLIENT_ID
- ZOHO_CLIENT_SECRET
- ZOHO_REFRESH_TOKEN
- ZOHO_ACCESS_TOKEN

---

## Run

```bash
uvicorn api:app --reload
```

Swagger:

```
http://127.0.0.1:8000/docs
```

---

# Current Features

- Email Analysis
- AI Planner
- Company Knowledge RAG
- Memory RAG
- Internet Search
- AI Email Generation
- AI Review
- FastAPI Backend

---

# Future Improvements

- Replace sample memory data with real Zoho email threads.
- Replace company text files with enterprise knowledge base.
- Integrate with Zoho Mail Extension.
- Deploy backend.
- Add Auto Draft / Auto Send functionality.

---

# Notes

The project follows a layered architecture:

```
FastAPI

↓

LangGraph

↓

Agents

↓

Services

↓

Repositories

↓

Retrievers

↓

Vector Database / APIs
```

This separation allows the data source (FAISS, Zoho Mail, PostgreSQL, etc.) to be replaced without changing the agent logic.