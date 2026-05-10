# Detection of Fraudulent Transaction Issues in the Payment Card Industry using Machine Learning: A Comprehensive Survey

## Metadata

```yaml
---
paper_id: "12345678-1234-1234-1234-123456789abc"
designation: international
title: "Detection of Fraudulent Transaction Issues in the Payment Card Industry using Machine Learning: A Comprehensive Survey"
authors: "Kalideen, M. R."
year: 2025
venue: "Journal of Information and Communication Technology (JICT)"
odin_topics: ["E.1", "E.2", "H.1", "J.1"]
shorthand_tags: ["/anomaly-taxonomy", "/anomaly-approaches", "/anomaly-tradeoffs", "/anomaly-ml-families", "/anomaly-algo-tradeoffs", "/data-sensitivity", "/user-trust", "/privacy-by-design", "/eval-frameworks", "/eval-pfms-applied"]
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

A comprehensive survey of machine learning techniques for payment card fraud detection, comparing supervised, unsupervised, deep learning, and ensemble methods while highlighting imbalanced data, interpretability, scalability, and privacy challenges.

## Problem and Motivation

Traditional rule-based fraud detection systems are static and fail to adapt to evolving fraud patterns, causing high false positives and missed detections. The rapid growth of digital payments demands more accurate, scalable, and real-time detection to prevent financial losses and maintain consumer trust. Prior surveys lacked integrated coverage of emerging trends such as explainable AI, privacy-preserving machine learning, and blockchain for fraud detection.

## Approach

- Systematic literature review of 49 studies published between 2010 and 2024.
- Searched IEEE Xplore, Scopus, and PubMed using keywords: credit card fraud detection, machine learning, payment card fraud, anomaly detection.
- Classified techniques into supervised, unsupervised, semi-supervised/hybrid, deep learning, and ensemble methods.
- Analyzed evaluation metrics: precision, recall, F1-score, AUC-ROC, average precision, Matthews Correlation Coefficient.
- Identified challenges: imbalanced datasets (fraud <1% of transactions), model interpretability, scalability for real-time detection, adversarial attacks.
- Covered emerging trends: explainable AI (XAI), privacy-preserving ML (federated learning, differential privacy, homomorphic encryption), blockchain integration.

## Findings

- Fraudulent transactions typically account for less than 1% of all payment card transactions, creating severe class imbalance.
- Deep learning models (DNN, RNN, autoencoders, GANs) achieve state-of-the-art accuracy but operate as “black boxes” with limited interpretability.
- Ensemble methods (bagging, boosting, random forests) improve generalization and resilience to noise compared to single models.
- Supervised learning requires large labeled datasets, which are costly and time-consuming to obtain.
- Unsupervised learning can detect novel fraud patterns without labels but is harder to evaluate.
- **Fraudulent transactions represent less than 1% of all transactions** — the core imbalance challenge.
- Explainable AI (XAI) techniques are critical for regulatory compliance and user trust in financial institutions.
- Federated learning enables collaborative model training without sharing raw customer data, addressing privacy concerns.

## Key Figures and Tables

- Table I: Traditional vs ML fraud detection → ML offers adaptability, scalability, real-time detection; traditional is static.
- Table III: Deep learning techniques (DNN, RNN, autoencoders, GANs) → GANs generate synthetic fraud data to augment imbalanced datasets.
- Table V: Comparison of ML techniques → No single algorithm dominates; trade-offs between accuracy, interpretability, and scalability.
- Table VI: Evaluation metrics comparison → Choose metrics based on business priorities (precision vs recall).

## Key Equations

$$Precision = \frac{TP}{TP+FP}$$
*Proportion of flagged frauds that are actually fraudulent.*

$$Recall = \frac{TP}{TP+FN}$$
*Proportion of actual frauds correctly detected.*

$$F1 = 2 \cdot \frac{Precision \cdot Recall}{Precision + Recall}$$
*Harmonic mean balancing precision and recall.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| ML | Machine learning — algorithms that learn patterns from data. |
| DNN | Deep neural network — multi-layered neural net capturing complex non-linear relationships. |
| RNN | Recurrent neural network — processes sequential data (e.g., transaction time series). |
| GAN | Generative adversarial network — two networks (generator/discriminator) trained adversarially to create synthetic data. |
| XAI | Explainable AI — methods that make model predictions understandable to humans. |
| PPML | Privacy-preserving machine learning — techniques (federated learning, differential privacy) that protect sensitive data during model training. |
| AUC-ROC | Area under the receiver operating characteristic curve — measures trade-off between true positive and false positive rates. |
| TP/FP/FN | True positive / false positive / false negative — confusion matrix outcomes for binary classification. |

## Critical Citations

- [Rawat & Tiwari, 2023] — Comprehensive review of ML techniques for credit card fraud detection.
- [Lucas & Jurgovsky, 2020] — Foundational survey on ML benchmarking for fraud detection.
- [Rudin, 2019] — Argues for interpretable models over black boxes in high-stakes finance.

## Relevance to Odin

**Topics:**

E.1 — Anomaly Detection in Personal Finance Systems

E.2 — Anomaly Detection Algorithm

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

J.1 — System Evaluation

**Contribution to Odin:**

This survey directly informs Odin's anomaly detection module by cataloging algorithms suitable for imbalanced financial transaction data, where fraud (or overspending) is rare. The discussion of precision-recall trade-offs guides Odin's alert design: prioritizing recall to catch overspending vs. precision to avoid annoying users with false alarms. Privacy-preserving ML techniques like federated learning justify Odin's manual-input-only approach as a deliberate privacy advantage rather than a limitation. Finally, the emphasis on XAI supports Odin's need for explainable anomaly alerts to build trust among Filipino young professionals.

**Directly justifies:**

- "Fraudulent transactions constitute less than 1% of all payment card transactions, creating a severe class imbalance that requires specialized handling (oversampling, cost-sensitive learning, or ensemble methods)."
- "Ensemble methods like Random Forest outperform single classifiers on imbalanced fraud datasets by reducing overfitting and improving generalization."
- "Explainable AI is necessary for regulatory compliance and user trust in financial fraud detection systems; black-box models are problematic in high-stakes environments."
- "Federated learning enables collaborative model training without sharing raw transaction data, preserving customer privacy while still improving model accuracy."

**Limits of relevance:**

- Paper focuses on payment card fraud (criminal activity), not personal spending anomalies (budget overages) — the behavioral context differs.
- No Philippines-specific data or cultural spending patterns are analyzed.
- Most cited studies use bank-integrated transaction streams; Odin relies on manual user input, which may have different data sparsity and latency characteristics.
- The survey does not address mobile-first implementation constraints (e.g., on-device inference, battery, network latency).

## Limitations

- The paper is a survey, not an original empirical study; all performance claims are secondary and lack unified benchmark validation.
- Excludes literature before 2010, potentially missing foundational anomaly detection methods. [unacknowledged]
- Does not address cultural or demographic variation in spending behavior — fraud patterns differ across regions. [unacknowledged]
- No discussion of cold-start scenarios where no historical transaction data exists, a key issue for new Odin users. [unacknowledged]
- Scalability suggestions (e.g., Apache Spark, Kafka) assume enterprise infrastructure, not mobile app constraints.

## Remember This

- 🔑 **Fraud is <1% of transactions** — class imbalance is the central ML challenge for anomaly detection.
- 📌 Ensemble methods (Random Forest) beat single models on imbalanced data — consider for Odin's anomaly detection.
- 💡 XAI is not optional — trust and compliance demand explainable alerts, not black boxes.
- 🔍 Federated learning trains models without sharing raw data — a privacy win that aligns with Odin's manual input design.
- ⚠️ No Philippines-specific data — adapt carefully to local spending patterns before citing fraud detection findings directly.
