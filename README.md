# 🤖 AI Engineer Learning Journey

A public log of my path to becoming an **AI Engineer** — tracking what I learn, build, and ship along the way.

> Started: June 2026 · Updated continuously

---

## 🎯 Goal

Build the practical skills to design, build, and deploy production AI systems — LLM apps, RAG pipelines, agents, evals, and the MLOps around them.

## 🗺️ Roadmap

Progress legend: ⬜ Not started · 🟨 In progress · ✅ Done

### 1. Foundations
- 🟨 Python for AI (typing, async, packaging) — working through [20 build-it-yourself projects](projects/learning-python/)
- ⬜ Math refresher (linear algebra, probability, gradients)
- ⬜ Classic ML concepts (train/test, overfitting, metrics)

### 2. Deep Learning
- ⬜ Neural network fundamentals
- ⬜ PyTorch basics
- ⬜ Transformers & attention

### 3. Large Language Models
- 🟨 Prompt engineering
- 🟨 Tokenization & context windows
- 🟨 Fine-tuning vs. prompting vs. RAG
- 🟨 Working with LLM APIs (Fireworks, Claude / OpenAI)

### 4. Building AI Applications
- 🟨 Retrieval-Augmented Generation (RAG)
- 🟨 Vector databases & embeddings
- 🟨 Agents & tool use
- 🟨 Structured output & function calling

### 5. Evaluation & Reliability
- ⬜ LLM evals & test harnesses
- ⬜ Guardrails & safety
- ⬜ Observability / tracing

### 6. Productionizing
- ⬜ Serving & latency/cost optimization
- ⬜ Caching strategies
- 🟨 Deployment (Docker, cloud)
- ⬜ MLOps / LLMOps basics

---

## 📝 Notes

Concept notes live in [`topics/`](topics/) — short "explain it in my own words" write-ups, following the [roadmap.sh AI Engineer](https://roadmap.sh/ai-engineer) path. Current clusters:

- **Core LLM concepts** — tokens, context, how LLMs work, inference, training, embeddings
- **Sampling parameters** — temperature, top-k, top-p, repetition penalties
- **Prompt engineering** — zero-/few-shot, chain-of-thought, ReAct, system prompting, input format, function calling, prompt caching, streaming, prompt vs. context engineering
- **RAG** — chunking, embeddings, vector stores, retrieval, generation
- **Vector databases** — purpose & functionality, Chroma / Pinecone / Weaviate / FAISS / Qdrant / …, indexing, similarity search
- **Agents** — agent SDKs (Claude, OpenAI, Google), manual implementation

## 📚 Log

A running journal lives in [`log/`](log/). Each entry: what I studied, what I built, and what clicked.

| Date | Topic | Notes |
|------|-------|-------|
| 2026-07 | Python fundamentals | Started [20 build-it-yourself projects](projects/learning-python/) — shipped #1 (number guessing) and #2 (unit converter); learned EAFP input handling and dict dispatch |
| 2026-07 | Prompt engineering notes | Added a full cluster of concept notes — zero-/few-shot, CoT, ReAct, system prompting, function calling, prompt caching, streaming, prompt vs. context engineering |
| 2026-06 | LangChain RAG chatbot | Built a full agentic-RAG web app (FastAPI + React + Fireworks) — see [`projects/learning-langchain/`](projects/learning-langchain/) |
| _–_ | Kickoff | Repo created |

## 🛠️ Projects

Hands-on builds live in [`projects/`](projects/). The best way to learn is to ship.

| Project | Status | Description |
|---------|--------|-------------|
| [learning-langchain](projects/learning-langchain/) | 🟨 | RAG chatbot web app (FastAPI · React · LangChain · Fireworks · Chroma) — agentic RAG with streaming, tool use, security hardening, and Docker. Being built into a public "chat with me" portfolio bot. |
| [learning-python](projects/learning-python/) | 🟨 | 20 build-it-yourself Python projects, easy → hard (2/20 done). Fundamentals → data & persistence → real-world tooling → systems, async & packaging. |
| [Backlog](projects/todo/) | ⬜ | Candidate gigs & builds — multi-tenant WhatsApp AI agent, clinical report extraction. |

## 📖 Resources

Curated courses, papers, and references in [`resources/`](resources/).

---

## License

Notes and original content are released under [CC BY 4.0](LICENSE). Code samples under MIT.
