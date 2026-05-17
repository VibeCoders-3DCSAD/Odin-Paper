# Recommendation system for financial decision-making using Artificial intelligence

## Metadata

```yaml
---
paper_id: "10.15276/aait.07.2024.24"
designation: algorithm-specific
title: "Recommendation system for financial decision-making using Artificial intelligence"
authors: "Shuryhin, K.; Zinovatna, S."
year: 2024
venue: "Applied Aspects of Information Technology"
odin_topics: ["4.A", "4.B", "6.A", "6.B", "7.B", "7.C", "8.A", "8.B", "10.A", "10.B"]
shorthand_tags: ["/pfms-intelligent-features", "/pfms-limitations", "/forecasting-methods-survey", "/forecast-algo-candidates", "/forecast-algo-comparison", "/anomaly-taxonomy", "/anomaly-algo-candidates", "/budget-rec-approaches", "/budget-rec-formulation", "/data-sensitivity", "/user-trust-behavior"]
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

Combining Isolation Forest for anomaly detection, ARIMA+LSTM for forecasting, and an LLM for personalized advice produces an ethical financial recommendation system that supports rational spending without manipulation.

## Problem and Motivation

Cognitive biases and aggressive AI-enhanced marketing lead consumers to irrational spending, yet existing financial tools lack intelligent, personalized support that respects user autonomy. Without such systems, individuals remain vulnerable to manipulative financial nudges. Prior work did not integrate anomaly detection, hybrid forecasting, and LLM-generated advice into a single ethically-grounded financial recommendation architecture.

## Approach

- **Data**: User transaction history, spending anomalies, forecasted expenses, plus financial goals and risk tolerance.
- **Anomaly detection**: Isolation Forest isolates atypical transactions by measuring path length in random binary trees.
- **Short‑term forecasting**: ARIMA (p,d,q) models seasonality and autoregressive dependencies.
- **Long‑term forecasting**: LSTM captures long‑term dependencies using memory cells and gating mechanisms.
- **Hybrid forecast**: Weighted average of ARIMA and LSTM outputs (α for ARIMA, 1‑α for LSTM).
- **Recommendation generation**: LLM (LLaMa 3.1) receives anomaly flags and forecasts, then produces contextual, personalized financial advice.
- **Ethical design**: System preserves user autonomy, avoids judgement, and provides transparent, option‑based recommendations.
- **Implementation**: Modular microservices (Spring, Python, React.js) with OAuth 2.0 and AWS infrastructure.

## Findings

- Isolation Forest successfully identifies anomalous expenses by isolating shortest-path data points in an unsupervised manner.
- **Combining ARIMA and LSTM via weighted average balances short‑term (seasonal) and long‑term (dependency) patterns, improving forecast stability.**
- LLM integration enables natural‑language, goal‑aligned financial advice that adapts to any income level.
- Ethical safeguards (no manipulation, user‑choice preservation, transparency) are embedded as core design requirements, not afterthoughts.
- OAuth 2.0 and OWASP Top 10 compliance protect user data and support privacy.

## Key Figures and Tables

- Figure 1: Request diagram for LLM recommendation → context flows from anomaly+forecast to personalized advice.
- Figure 2: Example LLM response → natural‑language suggestion based on detected overspending and forecast.
- Figure 3: AI component interaction diagram → Isolation Forest → ARIMA/LSTM → LLM pipeline.
- Figure 4: ERD for recommendation system → links users, transactions, budgets, goals, categories.
- Figure 5: Main page screenshot → clean dashboard with spending overview.
- Figure 6: Anomaly detection UI → flagged transaction with AI explanation.

## Key Equations

$$E(h(x)) = c(n) + \frac{2\log(n-1) - \frac{2(n-1)}{n}}{n}$$
*Expected path length in Isolation Forest: shorter paths indicate anomalies.*

$$s(x,n) = 2^{-\frac{E(h(x))}{c(n)}}$$
*Anomaly score: ≈1 for anomalies, ≈0.5 for normal points.*

$$y_t = c + \phi_1 y_{t-1} + \dots + \phi_p y_{t-p} + \theta_1 \epsilon_{t-1} + \dots + \theta_q \epsilon_{t-q} + \epsilon_t$$
*ARIMA(p,d,q) models value as linear combination of past values and past errors.*

$$C_t = f_t * C_{t-1} + i_t * \tilde{C_t}$$
*LSTM cell state update: forget old, add new candidate controlled by input gate.*

$$\hat{y_t} = \alpha \cdot \hat{y_t}^{ARIMA} + (1-\alpha) \cdot \hat{y_t}^{LSTM}$$
*Final forecast is weighted average of ARIMA and LSTM predictions.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Isolation Forest | Anomaly detection algorithm that isolates rare points by random splits; anomalies have shorter tree paths. |
| ARIMA | AutoRegressive Integrated Moving Average — time series model using past values and errors. |
| LSTM | Long Short-Term Memory [think: memory cell with forget/input/output gates that learns what to remember]. |
| LLM | Large Language Model — neural network that generates human‑like text from context. |
| Cognitive bias | Systematic deviation from rational judgment (e.g., loss aversion, framing effects). |
| Weighted average | Forecast combination method: each model's output multiplied by a coefficient (α) summing to 1. |
| OAuth 2.0 | Industry standard for token‑based access delegation without sharing passwords. |
| OWASP Top 10 | List of most critical web application security risks. |

## Critical Citations

- [Lu et al., 2020] — Foundational overview of intelligent information systems, framing RS as core technology.
- [Zibriczky, 2016] — First literature review on RS meeting finance, establishing spending‑opportunity recommendations.
- [Milano et al., 2020] — Ethical challenge taxonomy for RS (accuracy, user autonomy, harmful content).
- [Zhang et al., 2020] — AI in RS, emphasizing opacity and privacy as trust barriers.

## Relevance to Odin

**Topics:**

4.A — Landscape of Existing Personal Finance Systems

4.B — Limitations and Gaps in Existing Systems

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

7.B — Budget Recommendation in Personal Finance Systems

7.C — Budget Recommendation Algorithm

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

10.A — Data Privacy and Security in Personal Finance Systems

10.B — User Trust in Personal Finance Systems

**Contribution to Odin:**

This paper provides a complete, integrated AI architecture for personal finance management, directly mapping to Odin’s forecasting, anomaly detection, and recommendation modules. The hybrid ARIMA+LSTM approach justifies Odin’s spending forecasting algorithm selection, while Isolation Forest offers a well‑documented unsupervised anomaly detection method suitable for cold‑start user profiles. The explicit ethical design — preserving user autonomy, avoiding manipulation, and ensuring transparency — directly supports Odin’s privacy‑by‑design and trust requirements, especially the requirement to avoid gamification and instead provide value‑driven advice.

**Directly justifies:**

- “Isolation Forest detects financial anomalies without labeled training data, using path‑length scoring where s(x,n)≈1 indicates atypical spending.”
- “Combining ARIMA (short‑term seasonality) with LSTM (long‑term dependencies) via weighted average improves forecast stability over either model alone.”
- “LLM‑generated financial advice can be personalized to any income level by conditioning on transaction history, anomaly flags, and forecasted expenses.”
- “Ethical recommendation systems must balance influence with user autonomy, offering multiple options rather than imposing single decisions.”
- “OAuth 2.0 and OWASP Top 10 compliance are baseline requirements for user data protection in financial AI systems.”

**Limits of relevance:**

- Study is conceptual/architectural; no quantitative performance metrics (e.g., MAE, precision@k) are reported for the integrated system.
- User population is not Filipino; income volatility and cultural spending norms (e.g., family obligations) are not addressed.
- The system assumes banking API integration (mentioned in Section 4), whereas Odin is manual‑entry only — may affect data availability for forecasting.
- LLM deployment costs and on‑device feasibility are not evaluated; Odin’s mobile‑first constraints may limit use of cloud‑hosted LLMs.

## Limitations

- No empirical evaluation — the paper presents architecture and models but no accuracy, retention, or usability metrics. [unacknowledged]
- Forecasting combination weight α is not optimized or benchmarked; arbitrary weighting may underperform adaptive methods.
- Isolation Forest anomaly detection thresholds are not specified; real‑world tuning requirements are omitted.
- LLM recommendation quality is not validated against human expert advice or user acceptance studies.
- Ethical claims (non‑manipulation, autonomy) are design intentions, not validated user outcomes. [unacknowledged]

## Remember This

- 🔑 **Isolation Forest scores** — s≈1 flags anomalies; s≈0.5 means normal. No labels needed.
- 📌 **ARIMA+LSTM weighted average** balances short‑term seasonality and long‑term memory for spending forecasts.
- 💡 LLM generates income‑agnostic advice from anomaly + forecast context — works for any budget level.
- ⚠️ **No performance numbers** — paper describes architecture, not accuracy or retention gains. Use as design justification, not evidence of efficacy.
- 🔍 OAuth 2.0 + OWASP Top 10 = baseline security for financial AI — directly usable in Odin’s privacy section.
