# LLM Cognition Suite

A multi-application AI platform designed to improve human reasoning, decision-making, and clarity of thought.

This repository powers four independent user-facing applications — **Influence Clarity**, **Decision Intelligence**, **Plain-Language Explanation**, and **Mental Model Builder** — all built on a shared LLM-driven backend architecture.

The goal of this project is not to wrap a chatbot around prompts, but to design structured AI systems that:

- Reduce cognitive load  
- Improve reasoning quality  
- Surface hidden assumptions  
- Make complex information understandable  
- Encourage clearer thinking  

Each application operates as a standalone product with its own frontend, domain, and UX, while leveraging a shared backend that provides:

- Structured LLM orchestration  
- Schema-based outputs (Pydantic)  
- Multi-pass reasoning pipelines  
- Prompt versioning  
- Logging and evaluation harness  
- Cost and latency tracking  
- Safety guardrails and uncertainty scoring  

---

## Applications Included

### 1. Influence Clarity (Clarity Lens)

Analyzes articles, speeches, and long-form text to detect framing bias, emotional persuasion techniques, and missing perspectives.

---

### 2. Decision Intelligence (Decision Tree)

Transforms complex life or career decisions into structured decision variables, scenario simulations, and assumption tracking.

---

### 3. Plain-Language Explanation (Explain This)

Converts legal, medical, or technical documents into clear explanations with risk flags and ambiguity detection.

---

### 4. Mental Model Builder (Model Map)

Generates structured concept graphs for complex topics, highlighting relationships, misconceptions, and “what-if” scenario analysis.

---

## Architecture Overview

This project uses a monorepo structure:

- Shared **FastAPI** backend  
- Separate **Next.js** frontends for each app  
- Shared SDK for typed API communication  
- **PostgreSQL** for persistence  
- Structured LLM pipelines for reasoning tasks  

The system emphasizes reliability, structured outputs, and evaluation over novelty.

---

## Why This Project Exists

AI systems should amplify human reasoning, not replace it.

This repository explores how large language models can be orchestrated into practical cognitive tools that support clearer thinking in everyday life.
