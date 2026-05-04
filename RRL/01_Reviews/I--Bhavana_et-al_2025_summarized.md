# AI-Based Wealth Advisory System using Machine Learning and Predictive Analytics for Personalized Budget Planning

```yaml
---
name: paper-summary
paper_id: "10.15662/IJARCST.2025.0805004"
source_document: "Bhavana_et-al_converted.md"
designation: algorithm-specific
title: "AI-Based Wealth Advisory System using Machine Learning and Predictive Analytics for Personalized Budget Planning"
authors: "Bhavana, B. R.; Pavan, D.; Guru Darshan, T. H."
year: 2025
venue: "International Journal of Advanced Research in Computer Science and Technology"
odin_topics: [2, 4, 5, 6, 7, 8, 12, 14, 15]
shorthand_tags: ["/pfms-limitations", "/pfms-gap", "/budget-rec-algorithms", "/forecasting-methods", "/lstm-spending-applied", "/anomaly-approaches", "/alert-design", "/isolation-forest", "/security-standards", "/privacy-by-design", "/budget-alloc-algos", "/eval-pfms-applied", "/sus"]
summary_date: 2026-05-04
version: "1.0"
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

Integrates LSTM, Isolation Forest, and contextual bandits to deliver personalized budget planning with **95% anomaly detection accuracy** and a 22% savings improvement.

## Problem and Motivation

Existing personal finance apps (Mint, YNAB) are reactive, rule-based, and lack predictive adaptation. No consumer‑centric AI system combines forecasting, anomaly detection, transparency, and natural‑language advice. This gap leads to poor financial literacy and missed savings opportunities.

## Approach

- **Data**: Transaction logs (bank APIs), household expenditure surveys, macroeconomic indicators, and the European Credit Card Fraud Dataset.
- **Preprocessing**: Cleaning, normalization, NLP-based expense categorization, anonymization, and KNN imputation.
- **Models**: XGBoost/BERT for classification; ARIMA, Prophet, LSTM, Transformers for forecasting; Isolation Forest, Autoencoders, GANs for anomaly detection; Contextual Bandits and RL for recommendations.
- **Explainability**: SHAP and LIME with rule‑based summaries translated via Natural Language Generation (NLG).
- **Privacy**: AES‑256, TLS 1.3, differential privacy, federated learning, role‑based access.
- **Evaluation**: Accuracy, F1, MAE, RMSE, AUC, adoption rate, and System Usability Scale (SUS) on 100 pilot users.

## Findings

1. Anomaly detection accuracy = **95%** (AUC not reported but 95% stated).
2. Expense classification F1‑score = **91%** using XGBoost + BERT.
3. Forecasting error = **$43 MAE per user per month**.
4. Recommendation adoption rate = **41%**.
5. **22% improvement** in user savings after using the system.
6. **78%** of participants reported enhanced financial literacy.

## Key Figures and Tables

- **Table 1 (Literature Review)**: Summaries of 15 prior works (fraud, forecasting, XAI, fairness) → diverse ML methods applicable to personal finance.
- **Figure 1 & 2**: Architectural diagrams without captions → not informative for summary.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| XAI (Explainable AI) | Methods (SHAP, LIME) that reveal why a model made a prediction. |
| NLG (Natural Language Generation) | Translates numeric anomalies into plain English explanations (e.g., “38% higher grocery spending”). |
| LSTM (Long Short‑Term Memory) | A neural network that remembers patterns over long sequences — *like a memory cell with a forget gate*. |
| Isolation Forest | An algorithm that isolates anomalies by randomly splitting data — *outliers need fewer splits*. |
| SHAP (SHapley Additive exPlanations) | Assigns each feature a value for a prediction, based on cooperative game theory. |
| LIME (Local Interpretable Model‑agnostic Explanations) | Explains a single prediction by building a simple surrogate model around it. |
| Federated Learning | Training models on user devices without sending raw data to a central server. |
| Differential Privacy | Adds statistical noise to query results so individual records cannot be reconstructed. |
| Contextual Bandit | A recommendation algorithm that learns to choose actions based on context (e.g., user spending profile) and immediate feedback. |

## Critical Citations

- [Lundberg & Lee, 2017] — SHAP framework for consistent feature attribution, used to explain financial predictions.
- [Ribeiro et al., 2016] — LIME enables model‑agnostic interpretability, critical for regulatory acceptance.
- [Goodfellow et al., 2016] — Foundational deep learning principles that justify LSTM and GAN architectures in finance.

## Relevance to Odin

**Topics:**

2 – Existing Personal Finance and Budget Management Systems  

4 – Budgeting Strategies and Budget Recommendation in Personal Finance Systems  

5 – Predictive Modeling in Personal Finance Systems

6 – LSTM as the Spending Forecasting Algorithm  

7 – Anomaly Detection in Personal Finance Systems  

8 – Anomaly Detection Algorithm  

12 – Data Privacy, Security, and User Trust in Personal Finance Systems  

14 – Budget Recommendation Algorithm  

15 – System Evaluation  

**Contribution to Odin:**

This paper provides algorithmic justifications for three core Odin modules: forecasting (LSTM outperforms ARIMA for non‑linear spending patterns), anomaly detection (Isolation Forest works well on imbalanced transaction data), and budget recommendation (contextual bandits adaptively personalize suggestions). It also demonstrates a practical evaluation framework mixing ML metrics (MAE, AUC) with usability (SUS) and adoption rate – directly applicable to Odin’s validation plan.

**Directly justifies:**

- “LSTM captures long‑range temporal dependencies in sequential spending data, reducing forecast error to $43 MAE per month.”
- “Isolation Forest detects spending anomalies with 95% accuracy without requiring labeled training data.”
- “Contextual bandit recommendation engines increase user engagement and savings (22% improvement).”
- “Explainable AI (SHAP/LIME) built into financial advisory systems is necessary for user trust and regulatory compliance.”

**Limits of relevance:**

- The paper originates from India, not the Philippines; spending behavior and cultural categories may differ.
- Pilot study used only 100 users – SUS and adoption rates are preliminary.
- Privacy techniques (differential privacy, federated learning) may be too heavy for mobile‑first deployment without optimization.

## Limitations

- No long‑term retention study; user engagement measured only during the pilot.
- Datasets are not publicly available, limiting reproducibility.
- Bias and fairness are discussed but not empirically evaluated across demographic groups.
- Mobile‑specific constraints (battery, latency) are not addressed.

## Remember This

- 🔑 **95% anomaly detection accuracy** – Isolation Forest + Autoencoders on transaction data.
- ⚠️ **$43/month forecast error** – baseline for Odin’s per‑category LSTM target.
- 💡 **22% savings lift** – personalized recommendations drive measurable financial outcomes.
