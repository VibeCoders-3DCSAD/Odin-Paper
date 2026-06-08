# Next.js-Powered AI Platform for Smart Expense Tracking, Budgeting and Insights

## Metadata

```yaml
---
paper_id: "2c3e4f5a-6b7c-8d9e-0f1a-2b3c4d5e6f7a"
designation: algorithm-specific
title: "Next.js-Powered AI Platform for Smart Expense Tracking, Budgeting and Insights"
authors: "Badiger, R.; Robin, R.; Moraas, T.; Naik, V. G.; Karthikeyan, A. N."
year: 2026
venue: "Unknown"
odin_topics: ["A.2", "C.1", "C.2", "D.1", "E.1", "G.1", "H.1", "I.1", "J.1"]
shorthand_tags: ["/pfms-typology", "/pfms-features", "/pfms-budget-rec", "/pfms-limitations", "/budget-rec-algorithms", "/min-user-input", "/budget-rec-formulation", "/forecasting-methods", "/spending-time-series", "/per-category-forecast", "/anomaly-approaches", "/alert-design", "/cat-approaches", "/security-standards", "/privacy-by-design", "/entry-friction", "/value-driven-retention", "/eval-pfms-applied"]
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[X]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
---
```

## TL;DR

Spend AI combines XGBoost categorization (91.3% F1) and Gemini LLM insights in a Next.js platform, cutting manual expense logging by 78%.

## Problem and Motivation

Existing personal finance apps lack automated, real-time categorization and personalized insights, forcing manual entry that users abandon. This leads to poor financial discipline and missed savings opportunities. Prior work did not combine ML-based categorization with LLM-generated natural-language insights in a single production-ready system for multi-channel digital payments.

## Approach

- Data sources: manual entry, CSV import from bank statements, and OCR receipt scanning.
- Preprocessing: merchant name normalization, temporal feature extraction (day of week, month), target encoding for merchants, min-max scaling of amounts.
- Categorization: XGBoost classifier trained on labeled personal finance transactions with synthetic data augmentation; 18 spending categories.
- LLM insights: Gemini API with retrieval-augmented generation (RAG) – injects user spending summaries, budget utilization, and anomaly scores into prompts.
- Forecasting: Prophet time-series model per category, producing point forecasts and 90% credible intervals for next month’s expenditure.
- Architecture: Next.js 14 App Router (server actions), Prisma ORM, Supabase PostgreSQL with row-level security, Clerk authentication.

## Findings

1. XGBoost achieves a **weighted F1-score of 0.913** across 18 categories on a held-out test set of 4,200 transactions.
2. Manual expense-logging effort reduced by approximately 78% compared to conventional approaches in pilot trials.
3. Server response time for dashboard loads averages 420ms; AI insight generation adds 800–1,400ms (streamed progressively).

- 84% of pilot users rated Gemini-generated insights as “useful” or “very useful” for financial decisions.
- High-frequency categories (Food & Dining, Transport, Utilities) have F1-scores above 0.95; “Miscellaneous” lower at 0.81.

## Key Figures and Tables

- Figure 1: End-to-end user workflow → authentication → transaction entry → ML categorization → dashboard → AI insights → forecasting → alerts.
- Figure 2: Five-layer architecture (Presentation, Business Logic, AI, Data, Authentication) → modular separation enables independent scaling.
- Figure 3: Technology stack overview → Next.js, Prisma, Supabase, Clerk, Gemini, XGBoost, Prophet.
- Figure 4: AI insight generation pipeline (RAG pattern) → user data → structured prompt → Gemini API → structured JSON insights.
- Figure 5: XGBoost transaction categorization F1-scores per category → highest for Food & Dining (0.96), lowest for Miscellaneous (0.81).

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LLM | Large language model (here, Google Gemini) that generates human-like text from prompts. |
| RAG | Retrieval-augmented generation – injects user-specific data into the prompt to reduce hallucination. |
| XGBoost | Gradient-boosted tree ensemble used for transaction text classification. |
| Prophet | Decomposable time-series forecasting model handling trend, seasonality, and holidays. |
| RLS | Row-level security – database-enforced per-user data isolation in Supabase. |
| ORM | Object-relational mapper (Prisma) that translates database rows to typed objects. |
| UPI | Unified Payments Interface – India’s real-time payment system. |

## Critical Citations

- [Hean et al., 2025] — Shows Gemini is competitive for personal finance advisory tasks, justifying its use.
- [Kotios et al., 2022] — Hybrid deep learning + XAI for transaction classification; benchmark for the XGBoost approach.
- [Verma et al., 2024] — Next.js + PostgreSQL finance tracker lacking AI; baseline for adding ML/LLM layers.
- [Pancholi et al., 2026] — Multi-agent AI for personal finance; demonstrates feasibility of composable AI components.

## Relevance to Odin

**Topics:**

A.2 — Existing Personal Finance and Budget Management Systems

C.1 — Budgeting Strategies and Budget Recommendation

C.2 — Budget Recommendation Algorithm

D.1 — Predictive Modeling in Personal Finance Systems

E.1 — Anomaly Detection in Personal Finance Systems

G.1 — Expense Categorization in Filipino Personal Finance Contexts

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

I.1 — User Retention and Engagement in Personal Finance Systems

J.1 — System Evaluation

**Contribution to Odin:**

This paper provides a production-ready blueprint for Odin’s expense categorization module, showing that XGBoost achieves 91.3% F1 on 18 categories – directly applicable to Odin’s FIES‑based classification task. The Gemini + RAG insight pipeline informs Odin’s budgeting and anomaly alerting modules, demonstrating how LLMs can generate natural-language spending advice grounded in user data. The 78% reduction in manual effort supports Odin’s retention strategy (value‑driven engagement over gamification). While Odin uses LSTM for forecasting, the Prophet-based approach here offers a simpler cold‑start alternative that may be cited as a baseline comparison.

**Directly justifies:**

- “XGBoost achieves 91.3% weighted F1-score for transaction categorization across 18 spending categories on a 4,200‑transaction test set.”
- “Manual expense-logging effort is reduced by approximately 78% using ML-based automated categorization compared to conventional apps.”
- “Gemini LLM with retrieval-augmented generation produces structured financial insights that 84% of users find useful for spending decisions.”
- “Row-level security in Supabase PostgreSQL enforces per-user financial data isolation at the database level, meeting privacy requirements for personal finance apps.”
- “Prophet time-series forecasting provides per-category expenditure predictions with 90% credible intervals, requiring only three months of history for reliable forecasts.”

**Limits of relevance:**

- Study population is Indian (UPI‑centric); Filipino spending patterns and payment channels (e.g., GCash, Maya) may differ.
- Odin uses LSTM for forecasting; this paper uses Prophet – can be cited as an alternative but not a direct justification for LSTM.
- Platform relies on manual entry or CSV import; Odin also uses manual input, but the paper does not evaluate entry friction reduction for first-time users.
- Cold-start categorization accuracy for users with fewer than 50 transactions is not reported; Odin faces the same challenge.
- No evaluation of long-term retention or behavioral drift beyond pilot user feedback.

## Limitations

- Cold-start problem: categorization accuracy lower for new users with <50 transactions, common to personalized ML systems [acknowledged].
- LLM hallucination risk: Gemini may occasionally generate imprecise guidance despite RAG prompting [acknowledged].
- Manual data entry dependency: without banking API integration, incomplete records reduce forecast quality [acknowledged].
- Forecasting requires at least 3 months of history; shorter histories produce wide, less actionable intervals [acknowledged].
- No comparison with LSTM or GRU on the same dataset; Prophet’s relative performance for irregular spending sequences is unaddressed [unacknowledged].

## Remember This

- 🔑 **91.3% F1** – XGBoost categorizes 18 spending types, beating rule‑based systems.
- 📌 **78% less manual logging** – ML automation alone justifies AI investment for user retention.
- 💡 Gemini + RAG produces insights 84% of users find useful – natural language works for financial advice.
- ⚠️ Cold‑start hurts accuracy (<50 transactions) – Odin must design fallback rules for new users.
- ✅ Prophet forecasts per category with 90% intervals – needs 3 months data, simpler than LSTM.
