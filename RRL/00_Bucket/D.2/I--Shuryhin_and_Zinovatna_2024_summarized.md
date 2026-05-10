# Recommendation system for financial decision-making using Artificial intelligence

## Metadata

```yaml
---
paper_id: "10.15276/aait.07.2024.24"
designation: algorithm-specific
title: "Recommendation system for financial decision-making using Artificial intelligence"
authors: "Shuryhin, K. A.; Zinovatna, S. L."
year: 2024
venue: "Applied Aspects of Information Technology"
odin_topics: ["D.1", "D.2", "E.2", "H.1"]
shorthand_tags: ["/forecasting-methods", "/spending-time-series", "/lstm-spending-applied", "/isolation-forest", "/isolation-forest-applied", "/user-trust", "/privacy-by-design"]
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

Combining Isolation Forest for anomaly detection, ARIMA+LSTM for forecasting, and an LLM generates personalized financial advice without manipulation.

## Problem and Motivation

Cognitive biases like loss aversion lead to irrational spending, and AI-enhanced marketing can manipulate consumer behavior. Existing financial management tools lack intelligent, transparent support for rational decision-making across income levels. Prior work did not integrate anomaly detection, hybrid forecasting, and ethical LLM-based advice generation in a single system.

## Approach

- Dataset: User transaction history, spending anomalies, budget forecasts, financial goals, risk tolerance.
- Anomaly detection: Isolation Forest isolates atypical expenses by measuring path lengths in random binary trees.
- Short-term forecasting: ARIMA (p,d,q) models dependencies and removes non-stationarity for near-term predictions.
- Long-term forecasting: LSTM captures long-term dependencies using memory cells and forget gates.
- Forecast combination: Weighted average of ARIMA and LSTM outputs (α coefficient for model influence).
- Recommendation generation: LLM (e.g., LLaMa 3.1) ingests processed data, forms context, and produces personalized advice with explanations.
- Ethical design: System prioritizes user autonomy, transparency, privacy (OAuth 2.0, OWASP), and non‑judgmental support.

## Findings

- Isolation Forest effectively isolates anomalous transactions by identifying short path lengths in binary trees.
- Combining ARIMA and LSTM produces more accurate and stable expense forecasts than either model alone.
- LLM integration enables personalized financial recommendations tailored to individual risk levels, goals, and spending patterns.
- System supports users across all income levels by adapting advice to their specific financial capacity.
- Ethical safeguards (no manipulation, full user control) promote responsible financial behavior without imposing decisions.

## Key Figures and Tables

- Figure 1: Request diagram to LLM for personalized recommendation → shows data flow from user context to advice generation.
- Figure 2: Example LLM response based on provided context → demonstrates actionable, plain‑language financial advice.
- Figure 3: Interaction diagram of AI components within the system → maps anomaly detection, forecasting, and LLM integration.
- Figure 4: ERD for the recommendation system → illustrates entities: users, transactions, budgets, goals, categories.
- Figure 6: Use of AI models for anomaly detection → Isolation Forest flagging atypical expenses in the UI.

## Key Equations

$$s(x, n) = 2^{-\frac{E(h(x))}{c(n)}}$$
*Anomaly score; scores near 1 indicate anomalies, near 0.5 normal behavior.*

$$y_t = c + \phi_1 y_{t-1} + \dots + \phi_p y_{t-p} + \theta_1 \epsilon_{t-1} + \dots + \theta_q \epsilon_{t-q} + \epsilon_t$$
*ARIMA forecasts linear dependencies and past error terms.*

$$f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$$
*LSTM forget gate decides what to discard from the memory cell.*

$$\hat{y}_t = \alpha \cdot \hat{y}_t^{ARIMA} + (1 - \alpha) \cdot \hat{y}_t^{LSTM}$$
*Final forecast is weighted average of ARIMA (short‑term) and LSTM (long‑term).*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Isolation Forest | Anomaly detection algorithm that isolates outliers by random partitioning. |
| ARIMA | AutoRegressive Integrated Moving Average — linear time‑series forecasting model. |
| LSTM | Long Short-Term Memory — recurrent neural network that learns long‑term dependencies [think: memory cell with forget/input/output gates]. |
| LLM | Large Language Model — deep learning model (e.g., LLaMa) that generates human‑like text from context. |
| Anomaly score | Value between 0 and 1 indicating how unusual a transaction is; >0.5 suggests anomaly. |

## Critical Citations

- [Lu et al., 2020] — Foundational reference on intelligent information systems and recommendation system theory.
- [Verma & Sharma, 2020] — Establishes AI-based recommendation system capabilities across domains including finance.
- [Chua et al., 2023] — Defines the attitude‑perception‑intention model for user acceptance of AI investment advice.
- [Milano et al., 2020] — Analyzes ethical challenges of recommendation systems, including autonomy and manipulation.
- [Zibriczky, 2016] — Literature review on recommender systems in finance, highlighting context dependency and user goals.

## Relevance to Odin

**Topics:**

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

E.2 — Anomaly Detection Algorithm

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

**Contribution to Odin:**

This paper directly informs Odin’s anomaly detection module by demonstrating Isolation Forest for identifying atypical spending events without labeled training data — a key requirement for cold‑start users. It also supports Odin’s spending forecasting module through a hybrid ARIMA+LSTM approach, showing that combining short‑term and long‑term models improves forecast stability. The ethical framework emphasizing user autonomy and transparency provides a justification for Odin’s design choices around non‑manipulative alerts and privacy‑by‑default logging.

**Directly justifies:**

- "Isolation Forest detects financial anomalies without requiring labeled historical data by isolating outliers through random binary tree partitions, making it suitable for cold‑start user profiles."
- "Combining ARIMA (short‑term) and LSTM (long‑term) forecasts via weighted average yields more stable spending predictions than either model alone."
- "LLM‑generated financial advice can be personalized to user risk tolerance, financial goals, and spending patterns while preserving user autonomy through optional follow‑through."
- "Ethically designed recommendation systems must balance influence with user control, providing structured advice without judgment or manipulation."

**Limits of relevance:**

- Study population and dataset are not Filipino; cultural spending norms and income volatility patterns in Metro Manila may differ.
- System architecture assumes banking integration (OAuth 2.0, API access to transaction data), while Odin relies on manual input only.
- No quantitative evaluation metrics (e.g., MAE, precision, recall) are reported — the paper describes architecture but not empirical performance.
- Forecasting combination uses simple weighted average; Odin may require per‑category or multi‑output LSTM configurations not explored here.

## Limitations

- No empirical results or performance metrics — paper presents system design without validation on real user data. [unacknowledged]
- Cold‑start performance for new users (no transaction history) is not addressed — Isolation Forest and LSTM both require data to function. [unacknowledged]
- LLM generation described conceptually; no evaluation of recommendation quality, user acceptance, or bias mitigation.
- Weighted average coefficient α for forecast combination is not tuned or justified against alternative fusion methods.
- System depends on cloud infrastructure (AWS SageMaker, SQS, Glue), which may not align with Odin’s mobile‑first, offline‑capable scope.

## Remember This

- 🔑 **Isolation Forest finds anomalies by short isolation paths** — no training labels needed, ideal for cold‑start anomaly detection.
- 📌 **ARIMA + LSTM weighted average** — short‑term + long‑term forecasts outperform either model alone.
- 💡 **LLM generates non‑manipulative advice** — preserves user autonomy while explaining options.
- ⚠️ **No quantitative results reported** — this is a system architecture paper, not an empirical validation.