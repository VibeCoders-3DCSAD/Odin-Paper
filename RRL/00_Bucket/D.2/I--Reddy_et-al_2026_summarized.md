```markdown
# Welth — AI-Powered Financial Insights Platform

## Metadata

```yaml
---
paper_id: "c0a8e5d4-3b2a-4f1e-9d7c-8e6b5a4f3c2d"
designation: algorithm-specific
title: "Welth — AI-Powered Financial Insights Platform"
authors: "Reddy, S. T.; Soniya, C.; Thanushree, G.; Darshan, B. G.; Gupta, S."
year: 0000
venue: "Unknown"
odin_topics: ["D.1", "D.2", "G.1", "J.1"]
shorthand_tags: ["/forecasting-methods", "/lstm-spending-applied", "/cat-approaches", "/eval-pfms-applied"]
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[ ]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
---
```

## TL;DR

Welth integrates LSTM forecasting, LLAMA conversational AI, and Gemini receipt scanning in a unified web app, achieving 420ms dashboard load and sub‑2s AI response times.

## Problem and Motivation

Most Indian working-class and student users lack access to personalized, affordable financial advisory services despite widespread digital banking. Low financial literacy and the absence of a unified platform for budgeting, investment, EMI tracking, and tax planning compound the issue. No intelligent, context-aware chatbot existed that leverages a user’s own transactional data to deliver actionable advice.

## Approach

- Full‑stack serverless architecture using Next.js 15 with React Server Components and client interactivity.
- Authentication via Clerk (JWT) and data storage in PostgreSQL (Supabase) with Prisma ORM.
- Conversational AI advisor “CA Arjun” powered by Groq’s LPU: Llama 3.1 8B for intent parsing, 70B for investment recommendations.
- Multimodal receipt scanner using Google Gemini 1.5 Flash to extract amount, merchant, date, and category into JSON.
- Dedicated LSTM prediction microservice (FastAPI + TensorFlow/Keras) for cash flow forecasting, proxied through Next.js API.
- Live portfolio tracker fetching real‑time stock prices (Yahoo Finance) and mutual fund NAVs (MFAPI.in).
- EMI calculator with client‑side reducing‑balance formula and server‑side amortization schedule generation.
- Dashboard analytics with 6‑month trends, category breakdowns, and daily views using Recharts.

## Findings

1. Dashboard initial load (SSR with Suspense): **~420ms** to first meaningful content.
2. CA Report generation (parallel DB fetch + Groq 8B): ~1.8s average.
3. Investment recommendation (Groq 70B): ~3.2s average.
4. Receipt scan (Gemini 1.5 Flash): ~2.1s average.
5. EMI schedule creation (60 installments): ~180ms database round‑trip.
- All core features passed functional testing, including graceful fallback when LSTM microservice is offline.
- Arcjet null‑guard pattern allows rate limiting to bypass safely when API key is missing.
- Receipt scanner successfully detects blurry or non‑receipt images and returns user‑friendly error messages without crashing.

## Key Figures and Tables

None.

## Key Equations

$$EMI = P \times r \times (1+r)^n / ((1+r)^n - 1)$$
*Monthly EMI for reducing‑balance loan with principal P, monthly rate r, and n months.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LSTM | Long Short‑Term Memory – a recurrent neural network that learns order dependence in sequence data. |
| LLM | Large Language Model – AI trained on vast text to understand and generate human‑like responses. |
| OCR | Optical Character Recognition – technology to extract text from images. |
| EMI | Equated Monthly Installment – fixed payment made by a borrower to a lender each month. |
| NAV | Net Asset Value – per‑share value of a mutual fund. |
| JWT | JSON Web Token – compact token for secure authentication between parties. |

## Critical Citations

- [Chen et al., 2023] — Foundational work on LLM‑based financial advisory (FinGPT) that validates using user context via RAG.
- [Zhang et al., 2021] — LSTM time‑series forecasting for personal finance, providing basis for Welth’s prediction module.
- [Meta AI, 2024] — Llama 3.1 model architecture and capabilities, used for CA Arjun’s reasoning.

## Relevance to Odin

**Topics:**

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

G.1 — Expense Categorization in Filipino Personal Finance Contexts

J.1 — System Evaluation

**Contribution to Odin:**

This paper directly supports Odin’s forecasting module by providing a validated LSTM microservice architecture for cash flow prediction, demonstrating that such models can be integrated into a consumer web application with acceptable latency. The receipt scanner using Gemini 1.5 Flash offers an implementation pattern for Odin’s expense categorization module, showing how multimodal AI can extract structured transaction data from images. The reported performance metrics (e.g., 420ms dashboard load, 2.1s receipt scan) give Odin realistic benchmarks for system evaluation using ISO 25010 or SUS.

**Directly justifies:**

- “LSTM prediction service running on FastAPI with TensorFlow/Keras provides forecasting for cash flow trajectories in a personal finance web app.”
- “Google Gemini 1.5 Flash extracts total amount, merchant, date, and category from receipt images with an average response time of 2.1 seconds.”
- “Dashboard initial load using Next.js Server Components and Suspense streaming achieves ~420ms to first meaningful content, suitable for mobile web.”
- “Groq’s LPU infrastructure enables Llama 3.1 8B to operate with sub‑200ms latency for intent parsing in a conversational finance advisor.”

**Limits of relevance:**

- The platform is designed for the Indian market (SEBI guidelines, INR currency); spending behavior and regulatory context differ from the Philippines.
- Welth integrates live stock and mutual fund APIs; Odin is scoped to manual transaction input only, so portfolio tracking features are not directly applicable.
- No user‑facing accuracy metrics are reported for the LSTM forecasting model – only architectural integration and fallback behavior.
- The receipt scanner accuracy claim (92%) is cited from external research, not measured within this paper.

## Limitations

- No quantitative evaluation of LSTM forecasting accuracy – only architectural description and graceful fallback. [unacknowledged]
- System requires at least 3 months of user transaction data for the AI to provide meaningful “CA Advisor” insights.
- Heavy reliance on third‑party APIs (Yahoo Finance, MFAPI.in, Google Gemini, Groq); downtime or API changes directly impact core features.
- Geographical and regulatory focus on India limits generalizability to Filipino personal finance contexts.
- Performance metrics reported under ideal conditions (serverless, high‑speed internet); real‑world performance on mobile networks may differ.

## Remember This

- 🔑 Dashboard loads in **420ms** – SSR with Suspense boundaries streams data progressively.
- 📌 Receipt scanner returns structured JSON in 2.1s – uses Gemini 1.5 Flash with in‑memory processing, no disk storage.
- 💡 LSTM microservice falls back gracefully when offline – dashboard shows placeholder instead of crashing.
- ⚠️ No LSTM accuracy reported – only integration and latency; do not cite for predictive performance.
```