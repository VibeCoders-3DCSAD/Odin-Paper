# ARTIFICIAL INTELLIGENCE-DRIVEN PERSONAL FINANCE SOLUTION

## Metadata

```yaml
---
paper_id: "00000000-0000-5000-8000-000000000001"
designation: algorithm-specific
title: "ARTIFICIAL INTELLIGENCE-DRIVEN PERSONAL FINANCE SOLUTION"
authors: "Bashshar, S. A.; Imran, M.; Kumar, P. S.; Goud, E. S.; Venunath, M.; Prasad, M. L. M."
year: 2025
venue: "International Journal of Engineering Science and Advanced Technology (IJESAT)"
odin_topics: ["A.2", "D.1", "G.1"]
shorthand_tags: ["/forecasting-methods", "/spending-time-series", "/cat-approaches"]
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

NLP‑based transaction categorization reaches 86.2% accuracy; ARIMA forecasts 30‑day expenses with MAE 253.47.

## Problem and Motivation

Manual financial tracking lacks real‑time insights and predictive capabilities, leading to poor budgeting and overspending. Improving financial awareness is critical for responsible spending and savings. Prior systems offered automation without forward‑looking forecasts or domain‑specific NLP.

## Approach

- Dataset: 1,000+ labeled transaction descriptions (80/20 train/test split) + six months of historical spending data.
- Preprocessing: tokenization, stop‑word removal, lemmatization using NLTK.
- Categorization: Random Forest classifier with TF‑IDF features maps descriptions to categories (Food, Travel, Utilities, Entertainment).
- Forecasting: ARIMA model with parameters selected by AIC; differencing applied to achieve stationarity.
- Implementation: Python, Django, SQLite, responsive web interface.
- Evaluation: classification accuracy/precision/recall/F1; forecasting MAE/RMSE; Likert‑scale user feedback (10 participants).

## Findings

1. Categorization accuracy = **86.2%**, precision = 0.88, recall = 0.85, F1 = 0.86.
2. Forecasting MAE = 253.47, RMSE = 318.91 on six‑month historical data.
3. User feedback on a Likert scale was mostly positive, with participants noting clear visualizations and ease of use.

- Overlaps between similar categories (e.g., Dining vs. Groceries) remain a challenge, suggesting need for more domain‑specific training data.

## Key Figures and Tables

- Figure 2: List of Goals → shows user‑configurable financial targets.
- Figure 3: Forecasts of expenses for next 30 days → predicted trend follows historical pattern with modest error.
- Figure 5: Earnings Overview → visualizes income vs. expenses by category.

## Key Equations

$$Y_t = \phi_1 Y_{t-1} + \phi_2 Y_{t-2} + \dots + \phi_p Y_{t-p} + \epsilon_t$$
*Auto‑regressive term: current value depends on past values plus noise.*

$$Y'_t = \nabla^d Y_t = (1 - B)^d Y_t$$
*Integrated term: differencing d times to make the series stationary.*

$$Y_t = \epsilon_t + \theta_1 \epsilon_{t-1} + \theta_2 \epsilon_{t-2} + \dots + \theta_q \epsilon_{t-q}$$
*Moving‑average term: current value depends on past forecast errors.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| NLP | Natural Language Processing — techniques to interpret human language. |
| ARIMA | AutoRegressive Integrated Moving Average — a time‑series forecasting model. |
| MAE | Mean Absolute Error — average absolute forecast error. |
| RMSE | Root Mean Square Error — standard deviation of forecast errors (penalizes large errors more). |
| TF‑IDF | Term Frequency‑Inverse Document Frequency — numerical representation of text importance. |
| NLTK | Natural Language Toolkit — Python library for NLP. |
| AIC | Akaike Information Criterion — metric to select the best forecasting model parameters. |

## Critical Citations

- [Budiherwanto, 2025] — Commercial IPAs (Siri, Google Assistant, Alexa) perform well on general tasks but fail on domain‑specific financial forecasting.
- [Arrieta et al., 2019] — Framed explainable AI as a requirement for responsible financial assistants.
- [Khashei & Bijari, 2010] — Hybridization of ARIMA with neural networks improves forecasting accuracy.
- [Manning & Schütze, 1999] — Foundational text on statistical NLP that guides transaction description processing.

## Relevance to Odin

**Topics:**

A.2 — Existing Personal Finance and Budget Management Systems

D.1 — Predictive Modeling in Personal Finance Systems

G.1 — Expense Categorization in Filipino Personal Finance Contexts

**Contribution to Odin:**

This paper directly informs Odin’s expense categorization module by demonstrating that a Random Forest classifier with TF‑IDF achieves 86.2% accuracy on raw transaction descriptions, providing a baseline for FIES‑grounded category mapping. The ARIMA forecasting results (MAE 253.47 on six‑month data) serve as a statistical benchmark against which Odin’s LSTM‑based forecasting module can be compared, especially for cold‑start or low‑data scenarios. Although the system is web‑based, its modular architecture and use of lightweight SQLite align with Odin’s manual‑input, mobile‑first design constraints.

**Directly justifies:**

- “Random Forest with TF‑IDF achieves 86.2% categorization accuracy on financial transaction descriptions using a 1,000+ labeled dataset.”
- “ARIMA forecasts 30‑day expenses with MAE 253.47 and RMSE 318.91 on six months of historical spending data.”
- “Overlaps between semantically similar categories (e.g., Dining vs. Groceries) remain a challenge, requiring more domain‑specific training data.”
- “User feedback indicates that clear visualizations and forward forecasts improve perceived financial control and engagement.”

**Limits of relevance:**

- Study population is not Filipino; spending patterns and category relevance may differ.
- No mobile‑specific evaluation (web interface only); Odin’s mobile constraints may alter categorization and forecasting performance.
- Dataset size (1,000+ transactions) is small; Odin’s classification module will need more data or transfer learning.
- ARIMA assumes stationarity and may not capture irregular spending spikes common among young professionals.

## Limitations

- Small user feedback sample (n=10) limits generalizability of usability claims. [unacknowledged]
- Inconsistent method description: methodology describes keyword matching, but results report Random Forest with TF‑IDF.
- No comparison to deep learning models (e.g., LSTM, GRU) that are standard in modern forecasting.
- Forecasting horizon limited to 30 days; longer horizons not evaluated.
- No external validation on a held‑out or third‑party dataset.

## Remember This

- 🔑 **86.2% categorization accuracy** — Random Forest + TF‑IDF on transaction descriptions.
- 📌 **ARIMA MAE = 253.47** — statistical baseline for Odin’s LSTM forecasting module.
- 💡 Overlaps between similar categories (Dining vs. Groceries) remain a weak spot.
- ⚠️ User feedback from only 10 participants — not statistically robust.
