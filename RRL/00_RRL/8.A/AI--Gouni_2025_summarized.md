# Evolution of Machine Learning: A Foundation for Intelligent Systems

## Metadata

```yaml
---
paper_id: "10.32996/jcsts.2025.7.5.74"
designation: algorithm-specific
title: "Evolution of Machine Learning: A Foundation for Intelligent Systems"
authors: "Gouni, M. R."
year: 2025
venue: "Journal of Computer Science and Technology Studies"
odin_topics: ["5.C", "6.A", "8.A", "8.B"]
shorthand_tags: ["/classifier-candidates", "/classifier-tradeoffs", "/forecasting-methods-survey", "/temporal-dependency", "/anomaly-taxonomy", "/anomaly-behavioral-evidence", "/anomaly-ml-families", "/anomaly-algo-candidates", "/anomaly-unsupervised-baseline"]
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

Machine learning evolved from supervised classifiers to deep learning and unsupervised anomaly detection, enabling real-time fraud detection with lower false positives.

## Problem and Motivation

Traditional rule-based fraud systems are reactive, require constant manual updates, and cannot detect novel fraud patterns. Credit card fraud is one of the fastest-growing financial crimes, causing substantial losses as criminals adapt faster than static rules. No prior survey traced the full evolution from logistic regression to hybrid deep learning architectures specifically for transaction fraud detection.

## Approach

- Survey of supervised learning: logistic regression, decision trees, random forests, gradient boosting, deep neural networks.
- Survey of unsupervised learning: clustering (k-means, DBSCAN, spectral), autoencoders, and drift-adaptive methods.
- Survey of deep learning: RNNs, LSTMs, GRUs for sequential patterns; CNNs for spatial pattern extraction across transaction dimensions.
- Survey of future directions: hybrid ensembles, federated learning, explainable AI, adversarial training, continuous learning.
- Evaluation perspective: detection accuracy vs. false positive trade-offs, real-time constraints, regulatory compliance.

## Findings

- Supervised ensemble methods (random forests, gradient boosting) outperform single classifiers, especially on imbalanced fraud data.
- Autoencoders detect anomalies via reconstruction error without labeled data, capturing non-linear relationships linear methods miss.
- LSTMs address the vanishing gradient problem, maintaining contextual awareness across long transaction histories for card-not-present fraud.
- CNNs automatically extract hierarchical features from raw transaction data, reducing manual feature engineering.
- Hybrid multi-tier detection pipelines (high-sensitivity flagging + high-specificity intervention) balance accuracy and operational efficiency.
- Concept drift in transaction patterns requires adaptive models; static unsupervised methods increase false positives over time.
- Real-time deep learning deployment requires GPUs/TPUs, distributed computing, and online learning mechanisms.

## Key Figures and Tables

- Figure 1: Evolution of Supervised Learning Models in Fraud Detection → progression from logistic regression to deep neural networks improves pattern recognition.
- Figure 2: Unsupervised Learning for Novel Fraud Pattern Detection → clustering and autoencoders isolate outliers without labeled examples.
- Figure 3: Deep Learning Applications in Transaction Monitoring → RNNs and CNNs process sequential and multi-dimensional transaction patterns.
- Figure 4: Future Directions and Challenges in ML-Based Fraud Detection → hybrid, federated, and explainable AI are emerging best practices.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Supervised learning | Training models on labeled historical data to predict outcomes for new inputs. |
| Unsupervised learning | Finding patterns in unlabeled data, such as grouping or anomaly detection. |
| Deep learning | Neural networks with multiple hidden layers that automatically learn hierarchical features. |
| RNN | Recurrent Neural Network [think: memory of previous inputs in a sequence]. |
| LSTM | Long Short-Term Memory [think: selective forgetting and remembering over long sequences]. |
| GRU | Gated Recurrent Unit [think: simpler LSTM with fewer gates]. |
| CNN | Convolutional Neural Network [think: sliding filters to detect local patterns]. |
| Autoencoder | Neural network that compresses input then reconstructs it; large reconstruction error signals anomalies. |
| Concept drift | Gradual change in data patterns over time, requiring model adaptation. |
| Federated learning | Training across decentralized data sources without sharing raw data. |

## Critical Citations

- [Dal Pozzolo et al., 2017] — Realistic fraud modeling and novel learning strategy benchmark.
- [Zareapoor & Shamsolmoali, 2015] — Bagging ensemble classifiers for imbalanced fraud data.
- [Chan et al., 2002] — Distributed data mining for credit card fraud across multiple databases.
- [Kovach et al., 2011] — Local and global behavioral profiling for online banking fraud detection.

## Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

**Contribution to Odin:**

This survey directly informs Odin’s algorithm selection across three modules. For anomaly detection, the paper establishes autoencoders and clustering as viable unsupervised methods that do not require labeled fraud data — a critical property for Odin’s cold-start spending anomaly detection. For spending forecasting, the discussion of LSTMs and GRUs for sequential transaction data justifies their consideration as candidates for predicting per-category spending over time. For behavioral profile classification, the comparison of ensemble methods (random forests, gradient boosting) against single classifiers provides a basis for selecting a robust classifier given Odin’s imbalanced user activity data. Although the domain is credit card fraud, the methodological foundations transfer directly to personal finance anomaly detection and sequential prediction.

**Directly justifies:**

- “Autoencoders detect anomalies via reconstruction error without labeled data, making them applicable to cold-start user profiles where fraudulent (anomalous) spending has no prior examples.”
- “LSTM networks capture long-term dependencies in transaction sequences, outperforming standard RNNs by addressing the vanishing gradient problem — relevant to spending forecasting over months of user history.”
- “Random forests aggregate predictions across multiple decision trees, improving robustness against novel patterns compared to single decision trees, with reasonable real-time computational requirements.”
- “Concept drift in transaction patterns necessitates adaptive models; static anomaly detectors increase false positives over time as legitimate user behavior evolves.”
- “Hybrid detection pipelines with multiple sensitivity layers (high-sensitivity flagging + high-specificity intervention) balance detection accuracy and operational efficiency.”

**Limits of relevance:**

- Domain is credit card fraud, not personal budget anomaly detection; spending anomalies (overspending) differ from fraud (unauthorized use).
- No empirical benchmarks on personal finance datasets; all reported performance comparisons are from fraud detection literature.
- Filipino young professional spending patterns and cultural obligations are not addressed.
- Real-time processing assumptions (GPUs/TPUs, sub-millisecond latency) may exceed Odin’s mobile-first deployment constraints.
- Paper does not evaluate algorithm performance under manual transaction entry (vs. automated bank feeds).

## Limitations

- The paper is a survey, not an original empirical study; no new experiments or quantitative results are presented.
- Performance claims (e.g., “ensemble methods outperform single classifiers”) are cited from other works without meta-analysis or replication. [unacknowledged]
- Geographic and demographic context is absent; findings assume Western financial infrastructure and consumer behavior.
- No discussion of mobile-specific constraints (battery, compute, offline operation) for deploying deep learning models. [unacknowledged]
- The survey focuses on fraud detection, so applicability to personal finance budget recommendation and forecasting is inferred, not tested.

## Remember This

- 🔑 Autoencoders spot anomalies without labeled data — ideal for cold-start spending alerts.
- 📌 LSTMs remember long transaction sequences — candidate for Odin’s spending forecast module.
- 💡 Ensembles (random forests, gradient boosting) beat single classifiers on imbalanced data.
- ⚠️ Concept drift raises false positives over time if models don’t adapt — Odin must handle behavior changes.
- 🔍 Domain is credit card fraud — methods transfer, but spending anomalies ≠ fraud.
