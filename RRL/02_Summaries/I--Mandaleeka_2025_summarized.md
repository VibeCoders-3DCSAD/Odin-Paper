# Explainable and Context-Aware Financial Nudges via Event-Driven Microservices

## Metadata

```yaml
---
paper_id: "10.63282/3050-922X.ICRCEDA25-143"
designation: algorithm-specific
title: "Explainable and Context-Aware Financial Nudges via Event-Driven Microservices"
authors: "Mandaleeka, A. P."
year: 2025
venue: "International Journal of Emerging Research in Engineering and Technology"
odin_topics: ["A.2", "C.1", "C.2", "E.1", "I.1", "H.1"]
shorthand_tags: ["/pfms-gap", "/budget-rec-algorithms", "/anomaly-approaches", "/alert-design", "/user-trust", "/value-driven-retention"]
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

A modular, event-driven microservices framework with SHAP-based explanations delivers context-aware financial nudges that users understand and trust.

## Problem and Motivation

Existing financial alerts are generic, lack transparency, and ignore user context (time, location, habits), causing users to ignore or distrust them. This matters because opaque AI-driven advice undermines financial decision‑making and long‑term wellness. No prior system integrated real‑time context, explainable AI (XAI), and microservices into a single transparent nudging architecture.

## Approach

- Data Ingestor reads bank transactions via API and publishes structured events to Kafka.
- Context Processor enriches events with user behavior, budget goals, geolocation, and temporal patterns.
- Nudge Decision Engine uses rule‑based logic or an ML classifier to determine whether to send an alert.
- XAI module applies SHAP (SHapley Additive exPlanations) to compute feature contributions for each decision.
- Notification Service converts SHAP outputs into human‑readable explanations (e.g., “grocery spending is 25% above average”).
- Security enforced via OAuth 2.0, TLS encryption, role‑based access control (RBAC), and privacy‑by‑design data minimization.

## Findings

- **SHAP provides local interpretability with formal guarantees of fairness and consistency**, making it suitable for regulated financial environments.
- Contextual triggers (time, location, prior habits) increase user engagement more than static alerts.
- Explainability boosts users’ perceived relevance and trust in automated financial advice.
- The microservices architecture enables modularity, fault isolation, and horizontal scalability for real‑time nudging.
- No quantitative performance metrics (e.g., adherence rates, retention gains) are reported; evaluation is limited to synthetic data.

## Key Figures and Tables

- Figure 1: Personalized Financial Alerts Nudge System → high‑level flow from user to alert.
- Figure 2: System Overview with Kafka topics and microservices → each service interacts via asynchronous event streams.
- Figure 3: Example data ingestion pipeline → transaction spike → context → decision → SHAP → notification.
- Table 1: Example SHAP attribution output → grocery spend (+0.35) and budget threshold (+0.28) drive nudge decisions.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| XAI | Explainable AI – techniques that make model outputs understandable to humans. |
| SHAP | SHapley Additive exPlanations – a method that assigns each input feature a value showing how much it contributed to a prediction [think: cooperative game theory for ML]. |
| Kafka | A distributed event streaming platform for building real‑data pipelines. |
| Nudge | A timely, context‑aware alert designed to influence user behavior (e.g., spending warning). |
| Microservices | Small, independently deployable services that communicate via APIs or messaging. |
| Event‑driven architecture | System where components react to events (e.g., a new transaction) instead of polling. |
| Context‑aware | Using user‑specific data (time, location, past behavior) to tailor alerts. |

## Critical Citations

- [Lundberg & Lee, 2017] — Introduces SHAP, the core explainability method used for feature attribution in nudges.
- [Kreps et al., 2011] — Defines Kafka’s messaging semantics, which underpin the event‑driven pipeline.
- [Ben‑David et al., 2021] — User study showing explanations increase trust and compliance with financial advice.
- [Kim & Woo, 2021] — Demonstrates XAI in regulated financial rating models, supporting SHAP’s applicability.

## Relevance to Odin

**Topics:**

A.2 — Existing Personal Finance and Budget Management Systems

C.1 — Budgeting Strategies and Budget Recommendation

C.2 — Budget Recommendation Algorithm

E.1 — Anomaly Detection in Personal Finance Systems

I.1 — User Retention and Engagement in Personal Finance Systems

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

**Contribution to Odin:**

This paper directly informs Odin’s design by showing how explainability (via SHAP) can be embedded into a real‑time financial nudging pipeline, addressing user trust – a critical gap for manual‑input apps. The event‑driven microservices architecture provides a blueprint for Odin’s modular deployment, where each intelligent module (forecasting, anomaly detection, budget recommendation) could expose explainability hooks. Although the paper evaluates on synthetic data, its claim that SHAP‑based explanations increase perceived relevance and trust justifies Odin’s inclusion of an XAI layer, especially for the anomaly detection and budget recommendation modules.

**Directly justifies:**

- “SHAP provides local interpretability with formal guarantees of fairness and consistency, making it suitable for financial systems where trust and transparency are critical.”
- “Contextual triggers (e.g., time, location, prior habits) increase user engagement compared to static, generic alerts.”
- “Explainability (e.g., SHAP outputs converted to natural language) boosts users’ perceived relevance and trust in automated financial advice.”
- “A microservices architecture using Kafka for event streaming enables modular, scalable, and fault‑tolerant financial nudging without blocking user interactions.”

**Limits of relevance:**

- Paper reports no quantitative adherence, retention, or accuracy metrics – only qualitative claims and synthetic evaluation.
- The proposed system assumes open banking APIs (e.g., Plaid) for transaction ingestion; Odin relies on manual input, which changes the data availability and latency profile.
- Findings are not specific to Filipino users; cultural spending patterns and financial literacy levels may alter nudge effectiveness.
- SHAP’s computational cost in real‑time may be prohibitive for mobile‑first deployment without optimizations (caching, asynchronous generation).

## Limitations

- No empirical user study or A/B test; the framework’s effectiveness on real users is unvalidated.
- SHAP computation can be expensive; the proposed optimizations (caching, asynchronous generation) are not benchmarked. [unacknowledged]
- Synthetic and anonymized datasets may not capture real‑world behavioral complexity or noise.
- The architecture assumes always‑on connectivity and low‑latency event processing, which may not hold across all Philippine mobile networks. [unacknowledged]
- No comparison to alternative XAI methods (e.g., LIME, counterfactuals) or simpler rule‑based explanations.

## Remember This

- 🔑 SHAP explains *why* a nudge appears – users trust advice they understand.
- 📌 Context (time, location, habits) + explainability = higher engagement than static alerts.
- ⚠️ No real‑world user metrics – effectiveness remains unproven beyond synthetic data.
- 🧠 Kafka decouples services – Odin could adopt this for modular, scalable processing.
- ✅ Privacy‑by‑design (OAuth, RBAC, data minimization) is built into the architecture.
