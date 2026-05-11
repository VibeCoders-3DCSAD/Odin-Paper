# AI-Based Wealth Advisory System using Machine Learning and Predictive Analytics for Personalized Budget Planning

## Metadata

```yaml
---
paper_id: "10.15662/IJARCST.2025.0805004"
designation: algorithm-specific
title: "AI-Based Wealth Advisory System using Machine Learning and Predictive Analytics for Personalized Budget Planning"
authors: "Bhavana, B. R.; Pavan, D.; Darshan, T. H. Guru"
year: 2025
venue: "International Journal of Advanced Research in Computer Science & Technology (IJARCST)"
odin_topics: ["A.2", "C.2", "D.1", "D.2", "E.1", "E.2", "G.1", "H.1", "J.1"]
shorthand_tags: ["/pfms-gap", "/budget-rec-algorithms", "/forecasting-methods", "/lstm-architecture", "/anomaly-approaches", "/isolation-forest", "/cat-approaches", "/data-sensitivity", "/eval-frameworks", "/sus"]
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

An AI wealth advisor using forecasting, anomaly detection, and explainable AI achieved **95% anomaly detection accuracy** and 22% savings improvement in a 100-user pilot.

## Problem and Motivation

Most personal finance apps are reactive expense trackers, not proactive wealth managers. Poor financial literacy leads to debt and poor retirement planning, especially in emerging economies. No prior system integrated predictive analytics, anomaly detection, and explainable AI in a single consumer-centric advisory tool.

## Approach

- Dataset: Transaction logs (bank APIs), household expenditure surveys (US, India), macroeconomic indicators (World Bank, IMF), and a credit card fraud dataset for anomaly detection.
- Preprocessing: Cleaning, normalization, NLP-based categorization, anonymization, and KNN imputation.
- Feature engineering: Financial ratios, behavioral patterns (spending spikes, seasonality), temporal features (day-of-week).
- Classification: XGBoost and Random Forests for structured data; BERT for unstructured transaction descriptions.
- Forecasting: ARIMA, Prophet, LSTM networks, and Transformers; ensemble combination to reduce error.
- Anomaly detection: Isolation Forest, Autoencoders, and GAN-based detectors.
- Recommendation engine: Contextual bandits and reinforcement learning for adaptive suggestions.
- Explainability: SHAP and LIME for feature importance; rule-based summaries for non-technical users.
- Privacy: AES-256 encryption, TLS 1.3, differential privacy, and federated learning.
- Evaluation metrics: Accuracy, F1, MAE, RMSE, AUC, adoption rate, and SUS.
- Pilot test: 100 users; 6-month study measuring classification, forecasting, anomaly detection, and adoption.

## Findings

1. Anomaly detection reached **95% accuracy** using Isolation Forest and Autoencoders on transaction data.
2. Pilot participants achieved a **22% improvement in savings** after using the system.
3. Financial literacy increased for **78% of participants** (self-reported).
4. Expense classification F1-score = 91% using XGBoost and BERT.
5. Forecasting error = MAE of $43/month per user (ensemble of ARIMA, Prophet, LSTM).
6. Recommendation adoption rate = 41% (users followed suggested budget adjustments).

- Explainable AI (SHAP/LIME) improved user trust and transparency, especially for anomaly explanations.
- XAI explanations helped users understand spending spikes (e.g., “38% higher grocery spend due to festival”).

## Key Figures and Tables

- Table II (Literature Review Summary): 15 studies on fraud detection, forecasting, XAI, and fairness → Covers Autoencoders, Isolation Forest, LSTM, SHAP, and SUS as evaluation frameworks.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| XAI | Explainable AI — methods that make model decisions understandable to humans. |
| NLG | Natural Language Generation — converting data into readable sentences. |
| LSTM | Long Short-Term Memory [think: memory cell that learns what to forget] — a deep learning model for sequences. |
| ARIMA | AutoRegressive Integrated Moving Average — a statistical model for time-series forecasting. |
| GBDT | Gradient Boosted Decision Trees — an ensemble method combining weak decision trees. |
| SHAP | SHapley Additive exPlanations — a game-theory method to explain feature importance. |
| LIME | Local Interpretable Model-agnostic Explanations — explains individual predictions by approximating a simple model locally. |
| BERT | Bidirectional Encoder Representations from Transformers — a deep NLP model for text classification. |
| GAN | Generative Adversarial Network — two neural networks competing to generate realistic data. |
| SUS | System Usability Scale — a 10-item questionnaire measuring perceived usability. |
| PII | Personally Identifiable Information — data that can identify a specific person (e.g., name, account number). |
| GDPR | General Data Protection Regulation — EU privacy law requiring consent and anonymization. |
| KNN | K-Nearest Neighbors — imputation method that fills missing values using similar records. |

## Critical Citations

- [Mohammed et al., 2021] — Autoencoders + Isolation Forest achieved 96% fraud detection, baseline for anomaly module.
- [Zhang et al., 2022] — ARIMA+GBDT hybrid reduced forecasting error by 18%, justifying ensemble approach.
- [Lundberg & Lee, 2017] — SHAP framework for explainability, directly used in this system.
- [Davis et al., 1989] — Technology Acceptance Model (TAM) linking perceived usefulness to adoption.
- [Makridakis et al., 2018] — LSTM/RNN outperformed econometric models, supporting LSTM selection.

## Relevance to Odin

**Topics:**

A.2 — Existing Personal Finance and Budget Management Systems

C.2 — Budget Recommendation Algorithm

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

E.1 — Anomaly Detection in Personal Finance Systems

E.2 — Anomaly Detection Algorithm

G.1 — Expense Categorization in Filipino Personal Finance Contexts

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

J.1 — System Evaluation

**Contribution to Odin:**

This paper validates the multi-module architecture Odin intends to implement — forecasting, anomaly detection, classification, and recommendation — all in a single AI-driven personal finance system. The reported 95% anomaly detection accuracy using Isolation Forest and Autoencoders directly supports Odin's algorithm selection for the anomaly detection module. The 22% savings improvement and 41% recommendation adoption rate provide benchmarks for Odin's budget recommendation and user engagement design. Although the pilot population is not Filipino, the system's use of XAI (SHAP/LIME) and privacy safeguards (differential privacy, federated learning) align with Odin's requirements for user trust and data protection.

**Directly justifies:**

- "Isolation Forest combined with Autoencoders detected anomalous transactions with 95% accuracy on real-world financial data."
- "An ensemble of ARIMA, Prophet, and LSTM achieved a per-user monthly forecasting error of $43 MAE — a benchmark for Odin's spending forecasting module."
- "Expense classification using XGBoost and BERT reached 91% F1-score, supporting the use of transformer-based NLP for transaction categorization."
- "Contextual bandit and reinforcement learning recommendation engines achieved a 41% adoption rate for personalized budget suggestions."
- "Explainable AI (SHAP and LIME) improved user trust by translating anomaly scores into plain-English reasons (e.g., '38% higher grocery spend due to festival')."

**Limits of relevance:**

- Pilot conducted in India; spending patterns, income volatility, and financial infrastructure differ from the Philippines.
- Sample size of 100 users is small; statistical significance and generalizability are limited.
- System assumes banking API integration (PSD2/Open Banking); Odin uses only manual input, which may affect data richness and forecasting accuracy.
- No mobile-specific usability evaluation reported (SUS mentioned but no score provided).

## Limitations

- Small pilot (n=100) limits statistical power and generalizability to broader populations.
- Reliance on bank API data (real-time transaction feeds) — not applicable to Odin's manual-entry design. [unacknowledged]
- No cold-start evaluation: performance for users with no transaction history is not reported.
- Geography mismatch: Indian spending behavior may not transfer to Filipino young professionals.
- Privacy safeguards (differential privacy, federated learning) described but not empirically evaluated for impact on model accuracy.

## Remember This

- 🔑 **95% anomaly detection accuracy** — Isolation Forest + Autoencoders work on real transaction data.
- 📌 22% savings improvement and 41% recommendation adoption — benchmarks for Odin's modules.
- 💡 LSTM in ensemble achieved $43 MAE — supports sequential models for spending forecasting.
- ⚠️ Pilot used bank APIs (not manual input) — Odin's cold-start and manual-entry gaps are unaddressed.
