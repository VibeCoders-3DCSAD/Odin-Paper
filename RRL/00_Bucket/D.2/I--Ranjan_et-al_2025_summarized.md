# Online Payment Fraud Detection Using Decision Tree and LSTM Neural Network

## Metadata

```yaml
---
paper_id: "10.59256/ijsreat.20250505011"
designation: algorithm-specific
title: "Online Payment Fraud Detection Using Decision Tree and LSTM Neural Network"
authors: "Ranjan, A.; Jangir, A. K.; Abrol, K.; Saurav, S."
year: 2025
venue: "International Journal of Scientific Research in Engineering & Technology"
odin_topics: ["D.1", "D.2", "E.2"]
shorthand_tags: ["/lstm-architecture", "/lstm-vs-alternatives", "/lstm-spending-applied", "/anomaly-ml-families", "/anomaly-algo-justification"]
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

Hybrid fraud detection combining Decision Trees (fast, interpretable rules) and LSTM (temporal sequence modeling) outperforms standalone methods by capturing both static fraud triggers and evolving behavioral patterns.

## Problem and Motivation

Rule-based fraud detection systems cannot learn from evolving attack patterns, leading to high false positives and missed novel fraud. As online payment volume grows, organizations need adaptive, explainable systems that operate in real time. Prior work lacked hybrid architectures that jointly leverage interpretable tree models and deep sequential networks.

## Approach

- **Datasets:** IEEE-CIS Fraud Detection Dataset (e-commerce) and Kaggle Credit Card Fraud Detection dataset (highly imbalanced European transactions).
- **Preprocessing:** SMOTE for class balancing, class weighting, temporal feature extraction (1-hour / 24-hour rolling aggregates), and sequential encoding for LSTM.
- **Decision Tree models:** CART with Gini impurity; Random Forest ensemble to reduce overfitting; sub-millisecond inference suitable for real-time screening.
- **LSTM architecture:** Bidirectional LSTM (64–128 memory units), dropout 0.3–0.5, attention mechanism; input sequences of last 10–20 transactions per user.
- **Hybrid fusion:** Two-stage pipeline — Decision Tree flags high-risk transactions, LSTM performs deep temporal analysis; weighted voting (40:60 favoring LSTM) or feature stacking.

## Findings

- Decision Trees provide interpretable, low-latency fraud screening (sub-millisecond per transaction) — suitable as a first-layer filter.
- LSTMs capture long-term behavioral changes and multi-stage fraudulent activities missed by static classifiers.
- Bidirectional LSTM with attention improves interpretability by assigning importance to specific transaction steps.
- Hybrid architectures (Decision Tree + LSTM) outperform standalone models by combining rule-based clarity with sequential intelligence.
- SMOTE and class weighting are essential to address extreme class imbalance in fraud detection tasks.

## Key Figures and Tables

None.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LSTM | Long Short-Term Memory — a recurrent neural network that remembers patterns over long sequences [think: memory cell with forget/input/output gates]. |
| Decision Tree | A flowchart-like model that splits data on feature values to make classification rules. |
| SMOTE | Synthetic Minority Over-sampling Technique — creates synthetic examples of the minority class to balance datasets. |
| CART | Classification and Regression Tree — algorithm that builds binary decision trees using Gini impurity or entropy. |
| Attention mechanism | A layer that assigns different weights to different time steps, highlighting which transactions mattered most. |
| Bidirectional LSTM | Two LSTMs processing a sequence forward and backward, capturing past and future context. |

## Critical Citations

- [Hochreiter & Schmidhuber, 1997] — Introduced LSTM architecture; foundational for all sequence-based fraud detection.
- [Breiman, 2001] — Random Forests paper; ensemble method cited to justify reduced overfitting in tree models.
- [Chawla et al., 2002] — SMOTE paper; essential for handling imbalanced fraud datasets.
- [Jurgovsky et al., 2018] — First major application of LSTM to credit card fraud as sequence classification.
- [Bhattacharyya et al., 2011] — Benchmark comparing Decision Trees, SVMs, and Neural Networks; establishes trade-offs between interpretability and accuracy.

## Relevance to Odin

**Topics:**

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

E.2 — Anomaly Detection Algorithm

**Contribution to Odin:**

This paper directly justifies Odin’s selection of LSTM for sequential transaction modeling by demonstrating that LSTMs capture temporal dependencies (e.g., spending patterns over 10–20 transactions) that static classifiers miss. Although the domain is fraud detection, the same methodological claim — LSTM outperforms rule-based models on sequential financial data — transfers directly to Odin’s spending forecasting module. The hybrid two-stage architecture (fast rule-based filter followed by deep sequential analysis) offers a design pattern for Odin’s anomaly detection module, where a lightweight overage rule could flag potential budget violations before an Isolation Forest or LSTM performs deeper behavioral analysis. The paper’s emphasis on class imbalance handling (SMOTE, class weighting) is also relevant to Odin’s anomaly detection, where fraudulent-like overspending events are rare relative to normal transactions.

**Directly justifies:**

- “Bidirectional LSTM with 64–128 memory units and dropout (0.3–0.5) effectively models sequential transaction patterns over windows of 10–20 time steps, capturing long-term behavioral drift.”
- “Decision Trees execute in sub-millisecond per transaction, making them suitable as a first-stage filter before computationally heavier deep learning models.”
- “Hybrid architectures combining interpretable rule-based models with sequential deep networks achieve higher detection performance than either model alone on imbalanced financial transaction data.”
- “SMOTE and class weighting are required to prevent models from ignoring rare but high-cost events (fraud or budget overages) when the positive class constitutes less than 1% of samples.”
- “Attention mechanisms improve interpretability of LSTM predictions by highlighting which transaction steps most influenced the output.”

**Limits of relevance:**

- The paper focuses on fraud detection, not spending forecasting or budget adherence; the performance claims (e.g., sub-millisecond inference) are specific to fraud classification, not per-category spending prediction.
- No quantitative performance metrics (precision, recall, F1, AUC) are reported for the hybrid LSTM–Decision Tree model — only qualitative claims about relative superiority.
- The datasets are credit card and e-commerce transactions (European and IEEE-CIS), not Filipino household spending; income typology and cultural spending categories are absent.
- The paper does not evaluate cold-start performance (new users with no transaction history), a critical constraint for Odin’s initial user journey.

## Limitations

- No empirical results (accuracy, precision, recall, F1, or AUC) are presented for the proposed hybrid model — the paper is a system design proposal, not an evaluated implementation.
- The literature review is extensive but not systematic; key cited works (e.g., Jurgovsky et al., 2018) are not critically compared or meta-analyzed. [unacknowledged]
- Real-time deployment constraints beyond latency (e.g., memory footprint, model update frequency, regulatory explainability requirements) are not addressed.
- The hybrid fusion strategy (weighted voting 40:60) is arbitrary; no sensitivity analysis or cross-validation results justify the ratio.
- The paper does not discuss how to handle variable-length transaction sequences or missing data in the LSTM input layer.

## Remember This

- 🔑 **LSTM captures sequential patterns** — 10–20 transaction windows detect behavioral drift missed by static rules.  
- 📌 **Two-stage hybrid design** — Decision Tree flags suspicious transactions (sub-ms), LSTM deep-dives on flagged cases.  
- 💡 SMOTE + class weighting are mandatory — fraud/overspending is <1% of data; unweighted models ignore rare events.  
- ⚠️ No performance numbers — this is a proposal, not an evaluated system. Cite methods, not claimed accuracy.