# An Introduction to Machine Learning Methods for Fraud Detection

## Metadata

```yaml
---
paper_id: "10.3390/app152111787"
designation: algorithm-specific
title: "An Introduction to Machine Learning Methods for Fraud Detection"
authors: "Compagnino, A. A.; Maruccia, Y.; Cavuoti, S.; Riccio, G.; Tutone, A.; Crupi, R.; Pagliaro, A."
year: 2025
venue: "Applied Sciences"
odin_topics: ["D.2", "E.1", "E.2", "H.1", "J.1"]
shorthand_tags: ["/lstm-architecture", "/lstm-justification", "/anomaly-taxonomy", "/isolation-forest", "/anomaly-algo-tradeoffs", "/data-sensitivity", "/privacy-by-design", "/eval-frameworks"]
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

Machine learning fraud detection models face severe class imbalance and concept drift; even well-tuned Random Forest misses over 60% of frauds in real banking data.

## Problem and Motivation

Traditional rule-based fraud detection fails against increasingly sophisticated and evolving fraud schemes, causing billions in annual global losses. Financial institutions need adaptive, data-driven approaches that can identify subtle anomalous patterns in massive transaction streams. Prior literature lacked a systematic review that bridges theoretical ML taxonomies with operational realities demonstrated on proprietary banking data.

## Approach

- Systematic literature review of 120+ peer-reviewed articles (2014–2023) from Scopus, IEEE Xplore, ACM, and Web of Science.
- Taxonomic classification of fraud types: external (credit card, loan, insurance) and internal (financial statement, money laundering, tax, asset misappropriation).
- Survey of supervised methods (Random Forest, XGBoost, SVM, logistic regression) and unsupervised methods (Isolation Forest, autoencoders, k-means, LOF).
- Deep learning coverage: LSTM, CNN, RNN, GANs for sequential pattern detection and synthetic data generation.
- Two case studies on proprietary Intesa Sanpaolo banking data (90k–48k transactions) applying Random Forest, XGBoost, and Extra Trees with class_weight tuning.

## Findings

1. Random Forest achieved the highest AUPRC (0.619–0.697) across both case studies, but fraud recall at default threshold remained only **0.34–0.36** — meaning **two-thirds of frauds were missed**.
2. Setting `class_weight="balanced"` or `"balanced_subsample"` in Random Forest produced no meaningful improvement in fraud recall versus the default configuration.
3. Recall@0.5% (top 0.5% of ranked transactions) was 0.14–0.20, indicating that even with capacity-aware screening, 80% of frauds escape detection when review is limited to ~25 alerts.

- Supervised learning dominates the literature (57% of techniques), but low recall in real-world data suggests isolation alone is insufficient.
- Gradient boosting (XGBoost) and Extra Trees perform comparably but still fail to exceed 0.36 recall for the minority class.

## Key Figures and Tables

- Table 2: AUPRC benchmark on ULB 2013 dataset → XGBoost (0.867) and Random Forest (0.871) lead; kNN lags at 0.585.
- Table 4: Case study 1 test results (N=5000, prevalence 2.37%) → Random Forest AUPRC=0.619, recall=0.34, precision=0.93.
- Table 5: Case study 2 test results (N=23,310, prevalence 3.39%) → AUPRC=0.697, recall=0.36, no improvement from class_weight.
- Figure 1: Precision‑recall curve for Random Forest (Case study 1) → average precision 0.619, steep drop at high recall.
- Figure 2: Precision‑recall curve for Random Forest (Case study 2) → AUPRC 0.697, confirms ranking strength fails at decision threshold.

## Key Equations

$$Accuracy = \frac{TP + TN}{TP + TN + FP + FN}$$
*Correct predictions over total predictions — misleading under class imbalance.*

$$Precision = \frac{TP}{TP + FP}$$
*Of transactions flagged as fraud, how many were actually fraud (minimizes false alarms).*

$$Recall = \frac{TP}{TP + FN}$$
*Of all actual frauds, how many were caught (minimizes financial loss).*

$$F1 = \frac{2 \times Precision \times Recall}{Precision + Recall}$$
*Harmonic mean balancing false positives and false negatives.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LSTM | Long Short-Term Memory — a recurrent neural network with gates that remembers patterns over long transaction sequences [think: memory cell that learns what to forget]. |
| Isolation Forest | Unsupervised algorithm that isolates anomalies by random feature splits — no labeled training data needed. |
| Autoencoder | Neural network that compresses then reconstructs data; high reconstruction error signals anomaly. |
| Concept drift | Gradual change in fraud patterns over time, making models trained on old data obsolete. |
| Class imbalance | Fraud transactions are extremely rare (<1–3%), so models learn to predict “legitimate” by default. |
| AUPRC | Area under precision‑recall curve — better than ROC for imbalanced data because it ignores true negatives. |
| XAI | Explainable AI — methods like SHAP and LIME that reveal why a model flagged a transaction. |
| SHAP | Shapley additive explanations — game‑theory method attributing prediction to each feature’s contribution. |
| GAN | Generative adversarial network — two competing neural networks that generate synthetic fraud samples for training. |

## Critical Citations

- [Dal Pozzolo et al., 2022] — Documented concept drift as a persistent operational challenge in credit card fraud detection.
- [Sahin et al., 2013] — Established cost‑sensitive decision tree framework for balancing false positive vs. false negative costs.
- [Fiore et al., 2019] — Demonstrated GAN‑based synthetic fraud generation to mitigate class imbalance.
- [Salam et al., 2024] — Proposed federated learning for privacy‑preserving cross‑institutional fraud model training.

## Relevance to Odin

**Topics:**

D.2 — LSTM as the Spending Forecasting Algorithm

E.1 — Anomaly Detection in Personal Finance Systems

E.2 — Anomaly Detection Algorithm

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

J.1 — System Evaluation

**Contribution to Odin:**

This review directly informs Odin’s anomaly detection module by benchmarking Isolation Forest as an unsupervised outlier detector that requires no labeled fraud data — critical for Odin’s cold‑start user profiles where no historical “fraud” (i.e., budget overage or unusual spending) labels exist. The paper’s demonstration that even well‑tuned Random Forest achieves only 0.34 recall on real banking data provides a sobering baseline: Odin cannot rely on supervised classifiers alone for behavioral anomaly detection and should prioritize ranking‑based (Recall@K) or cost‑sensitive evaluation over accuracy. The discussion of LSTM for sequential transaction analysis justifies Odin’s forecasting module architecture, while the coverage of concept drift and class imbalance highlights challenges Odin will face as user spending patterns evolve over time and legitimate overspending is rare.

**Directly justifies:**

- “Isolation Forest isolates anomalies without labeled training data by randomly partitioning feature space, making it applicable to cold‑start anomaly detection in personal finance systems.”
- “Supervised classifiers like Random Forest achieve high accuracy (98%) but miss two‑thirds of actual frauds (recall ≤0.36) on imbalanced banking data — accuracy is a misleading metric for rare event detection.”
- “LSTM networks model long‑range temporal dependencies in transaction sequences, outperforming feedforward networks for detecting sequential fraud patterns.”
- “Recall@0.5% — the proportion of frauds caught when reviewing only the top 0.5% of highest‑scoring transactions — provides an operationally relevant evaluation metric when manual review capacity is limited.”
- “Class_weight adjustments do not resolve extreme class imbalance; data‑level techniques (SMOTE) or hybrid unsupervised‑supervised architectures are required.”

**Limits of relevance:**

- The paper focuses on financial fraud (theft, money laundering), not personal budget anomalies (overspending, category deviation) — Odin’s anomaly detection targets behavioral rule violations, not criminal fraud.
- Case study datasets are from European banking transfers; spending patterns and fraud typologies differ from Filipino young professional budgets.
- Models evaluated on transaction‑level fraud flags; Odin requires user‑level behavioral profiling over time, a different unit of analysis.
- No evaluation of explainability methods (SHAP/LIME) on the case study data, though the paper recommends them for regulatory compliance.

## Limitations

- Case studies used proprietary banking data with limited feature disclosure (PCA‑transformed in public dataset) — reproducibility is restricted. [unacknowledged]
- No longitudinal evaluation of concept drift; models were trained and tested on static periods, not adaptive retraining. [unacknowledged]
- Deep learning methods (LSTM, GANs) are reviewed but not empirically tested in the case studies — claims about their superiority remain theoretical.
- The review does not address behavioral profiling or user typology, which are central to Odin’s anomaly detection and profile classification modules.
- Ethical bias and fairness in fraud detection are mentioned as future directions but not integrated into the experimental design.

## Remember This

- 🔑 **Best model missed 66% of frauds** — recall ≤0.36 on real banking data despite 98% accuracy.
- 📌 Isolation Forest works without labels — ideal for Odin’s cold‑start anomaly detection.
- 💡 Use AUPRC, not accuracy — accuracy hides the fraud detection failure rate.
- ⚠️ Class_weight doesn’t fix imbalance — need SMOTE or hybrid models instead.
- 🔍 Recall@0.5% catches only 14–20% of frauds — manual review alone is insufficient.
