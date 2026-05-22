# Credit Card Fraud Detection Through Deep Learning and Real-Time Data Streams: A Comparison and New Directions

## Metadata

```yaml
---
paper_id: "10.47852/bonviewFSI52026108"
designation: algorithm-specific
title: "Credit Card Fraud Detection Through Deep Learning and Real-Time Data Streams: A Comparison and New Directions"
authors: "Polytarchos, E."
year: 2025
venue: "FinTech and Sustainable Innovation"
odin_topics: ["5.C", "6.B", "8.A", "8.B", "12.B"]
shorthand_tags: ["/classification-vs-clustering", "/classifier-candidates", "/classifier-tradeoffs", "/classifier-eval-metrics", "/forecast-algo-candidates", "/forecast-algo-comparison", "/forecast-algo-tradeoffs", "/forecast-eval-metrics", "/anomaly-algo-candidates", "/anomaly-unsupervised-baseline", "/anomaly-algo-tradeoffs", "/anomaly-eval-metrics", "/eval-ml-design", "/eval-limitations"]
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

Real-time clustering (BEReTiC) offers lower false positives (0.003%) than deep learning (0.007%) but lower classification accuracy (66% vs 92% for total funds range).

## Problem and Motivation

No prior empirical comparison exists between real-time unsupervised stream-based fraud detection and batch-trained deep learning models on imbalanced, high-volume financial data. Without such comparisons, financial institutions cannot make informed decisions about deploying timely and effective fraud prevention mechanisms. Existing literature lacks a side‑by‑side evaluation of accuracy, false positives, and adaptability to novel fraud patterns.

## Approach

- Dataset: 17.5M individual transactions (IND) and 1.2M summaries (SUM) from one year of credit/debit card activity; labeled, complete, structured.
- Synthetic fraud injection: Generated 1,000 transactions mimicking behavioral inconsistency (e.g., a transaction matching a different customer’s average profile).
- Deep learning pipeline: LSTM and MLP models trained to predict 9 customer demographic labels; ensemble computes Scale of Suspicious Transaction (SST) – percentage of misclassifying classifiers.
- Real‑time system (BEReTiC): Patented clustering algorithm (CluNN) with Gower similarity; processes raw streams without preprocessing; detects anomalies via deviation from dynamic customer “fingerprints.”
- Evaluation metrics: Per‑label classification accuracy, number of detected fraudulent transactions, false positives, misclassification rate.

## Findings

1. LSTM achieved **92% accuracy** predicting “total funds range” – the highest among all labels; MLP reached only 78% for the same label.
2. Deep learning detected 788/1000 injected fraudulent transactions with 1,340 false positives (0.007% misclassification rate).
3. Real‑time clustering detected 619/1000 injected frauds with 574 false positives – a **0.003% misclassification rate** (lower than deep learning).

- Real‑time accuracy per label was substantially lower (e.g., 66% for total funds range) due to cold‑start: the system lacks historical data early in the stream.
- Real‑time clustering adapts to new fraud patterns without retraining; deep learning requires periodic retraining to handle concept drift.

## Key Figures and Tables

- Table 1: Classification accuracy by label → LSTM dominates (92% vs MLP’s 78% for total funds range; real‑time trails at 66%).
- Table 2: Fraud detection performance → Real‑time: 619 detected, 574 false positives; deep learning: 788 detected, 1,340 false positives.
- Table 3: Methodology trade‑offs → Deep learning: high accuracy but high latency & preprocessing; real‑time: lower accuracy but low latency & adaptability.
- Figure 1: BEReTiC modules (Data receptor, SCoDe2, Clustering, Classification, Reporting) → shows real‑time processing pipeline.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LSTM | Long Short-Term Memory network – a recurrent neural net that remembers patterns over time [think: memory cell with forget gate]. |
| MLP | Multilayer Perceptron – a basic feedforward neural network. |
| BEReTiC | Best Effort Real-Time Clustering and Classification adapter – patented system for real‑time anomaly detection without preprocessing. |
| SST | Scale of Suspicious Transaction – percentage of ensemble classifiers that mispredict a transaction’s labels. |
| SLT | Scale of Legitimate Transaction – complement of SST (1 – SST). |
| CSST | Confidence of SST – product of accuracies of classifiers that mispredicted. |
| Gower similarity | A metric that combines categorical and numerical data to compare instances. |
| Concept drift | Change in underlying data patterns over time (e.g., new fraud tactics). |
| Cold‑start | Situation where a model has insufficient historical data to make accurate predictions early on. |

## Critical Citations

- [Polytarchos et al., 2024] — Patent describing the BEReTiC real‑time clustering system; core method for stream‑based detection.
- [Fiore et al., 2019] — Foundational use of GANs to improve classification on imbalanced fraud datasets.
- [Manoharan et al., 2024] — Prior work on machine learning for real‑time fraud detection in high‑throughput transactions.
- [Mehri et al., 2024] — BankGAN: generative model for synthetic financial transactions; relevant for imbalance handling.

## Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

6.B — Spending Forecasting Algorithm

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly informs Odin’s anomaly detection module by benchmarking batch‑trained deep learning (LSTM/MLP) against a real‑time unsupervised clustering algorithm (BEReTiC), highlighting the accuracy‑vs‑latency trade‑off essential for mobile‑first personal finance. The finding that real‑time clustering achieves lower false positives (0.003%) without data preprocessing supports Odin’s design for manual entry and cold‑start users where labeled fraud data is unavailable. Although the domain is credit card fraud, the comparative methodology and algorithm candidates (LSTM for time‑series, unsupervised clustering for anomalies) transfer directly to spending anomaly detection and behavioral profile classification in Odin.

**Directly justifies:**

- “LSTM achieved 92% accuracy predicting customer total funds range on a 17.5M transaction dataset, demonstrating its strength in time‑series demographic classification.”
- “Real‑time unsupervised clustering (BEReTiC) detected fraud with a 0.003% misclassification rate and 574 false positives, compared to deep learning’s 0.007% rate and 1,340 false positives.”
- “Real‑time clustering adapts to new fraud patterns without retraining, while deep learning requires periodic retraining to handle concept drift.”
- “Cold‑start significantly reduces real‑time clustering accuracy (66% vs 92% for deep learning), a critical design consideration for new Odin users with no transaction history.”

**Limits of relevance:**

- Study uses credit card fraud data from Greece; Filipino young professionals’ spending anomalies may differ (e.g., family obligations, informal transfers).
- Domain is fraud detection, not personal budget anomaly detection (overspending vs budget thresholds), though the unsupervised method is transferable.
- Datasets are bank‑provided and labeled; Odin uses manual input without ground‑truth fraud labels.
- Real‑time clustering’s lower accuracy may be unacceptable for core classification tasks in Odin unless hybridized.

## Limitations

- No cross‑validation on a held‑out test set from a different time period; generalization to future fraud patterns unassessed. [unacknowledged]
- Synthetic fraud injection may not replicate real fraudsters’ adaptive tactics, overestimating detection rates.
- Real‑time clustering’s accuracy never reaches deep learning’s level even after full data ingestion – a permanent trade‑off.
- Dataset not publicly available (NDA), preventing replication or adaptation to Philippine spending data.
- No evaluation of computational resource usage on mobile devices; Odin’s mobile‑first constraint is not addressed.

## Remember This

- 🔑 LSTM hit **92% accuracy** on total funds range – strong for time‑series classification.
- 💡 Real‑time clustering cut false positives to **0.003%** vs 0.007% – better for alert fatigue.
- 📌 Cold‑start cost: real‑time accuracy lagged at 66% vs 92% – new users need hybrid seeding.
- ⚠️ No preprocessing required for BEReTiC – matches Odin’s manual input, no data cleansing.
- 🔍 Hybrid models (LSTM + clustering) proposed as future direction – best of both worlds.
