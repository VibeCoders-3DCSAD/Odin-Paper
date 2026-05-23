# Exploring Machine Learning for Credit Card Fraud Detection from a Philippine Perspective

## Metadata

```yaml
---
paper_id: "10.1145/3698062.3698088"
designation: local
title: "Exploring Machine Learning for Credit Card Fraud Detection from a Philippine Perspective"
authors: "Blancaflor, E.; Asuncion, K. D.; Reyes, H. J.; Verzosa, M."
year: 2024
venue: "Proceedings of the 2024 6th World Symposium on Software Engineering (WSSE 2024)"
odin_topics: ["8.A", "8.B"]
shorthand_tags: ["/anomaly-ml-families", "/anomaly-algo-candidates", "/anomaly-algo-tradeoffs", "/anomaly-eval-metrics"]
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

Credit card fraud in the Philippines rose 21% post-pandemic, and ML models—especially k‑NN (97.69%) and Naïve Bayes (97.92%)—outperform logistic regression (54.86%) on local transaction data.

## Problem and Motivation

Credit card fraud in the Philippines surged 21% since COVID‑19, yet traditional fraud prevention systems cannot secure digital payment networks effectively. Rising financial losses (P540 million in online fraud in 2021 alone) demand stronger detection, but existing fraud detection systems struggle with imbalanced data, concept drift, and real‑time requirements. No prior work had systematically compared ML algorithms specifically tailored to the Philippine economic, technological, and social context.

## Approach

- Dataset: Credit card transaction data from the Philippines (size not specified).  
- Algorithms evaluated: Logistic regression (LR), k‑nearest neighbors (k‑NN), Naïve Bayes, support vector machines (SVM), artificial neural networks (ANN).  
- Evaluation metrics: Accuracy, sensitivity, specificity, precision, Matthews correlation coefficient (MCC), balanced classification rate (BCR).  
- Implementation: Python; models applied to both raw and preprocessed data.  
- Enhancement techniques: SMOTE and genetic algorithms tested with ANN and LR to handle class imbalance.

## Findings

1. k‑NN achieved **97.69% accuracy** on Philippine credit card transaction data.  
2. Naïve Bayes reached **97.92% accuracy**, slightly outperforming k‑NN.  
3. Logistic regression performed poorly at **54.86% accuracy**.  
4. SVM accuracy varies up to 80%; ANN up to 98.44% depending on configuration.  
- ANN‑SMOTE outperformed all other model‑enhancement combinations (accuracy, precision, recall, F1).  
- Imbalanced data and concept drift remain key obstacles; hybrid sampling and meta‑learning are proposed as future improvements.

## Key Figures and Tables

- Figure 1: Comparative performance of ANN, LR, GA‑enhanced, and SMOTE‑enhanced models → ANN‑SMOTE is best across all metrics.  
- Table 1: Accuracy of LR (54.86%), k‑NN (97.69%), Naïve Bayes (97.92%), SVM (≤80%), ANN (≤98.44%) → k‑NN and Naïve Bayes excel on local data.

## Key Equations

$$f(x) = sgn(x \cdot w) + b$$
*SVM decision function: sign of dot product plus bias determines class.*

$$MCC = \frac{TP \times TN - FP \times FN}{\sqrt{(TP+FP)(TP+FN)(TN+FP)(TN+FN)}}$$
*Balanced metric for binary classification with imbalanced classes.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| ML | Machine learning — algorithms that learn patterns from data without explicit rules. |
| SVM | Support vector machine — finds a boundary that best separates two classes (think: widest street between groups). |
| ANN | Artificial neural network — layered connections that mimic how neurons learn patterns. |
| FPS | Fraud prevention system — stops fraud before it happens (e.g., multifactor authentication). |
| FDS | Fraud detection system — identifies fraud after a transaction occurs (e.g., anomaly detection). |
| MCC | Matthews correlation coefficient — a balanced accuracy measure for highly skewed datasets. |
| BCR | Balanced classification rate — average of true positive and true negative rates. |
| k‑NN | k‑nearest neighbors — classifies a point by looking at its k closest neighbors. |
| SMOTE | Synthetic minority oversampling technique — creates synthetic examples of rare fraud cases to balance data. |

## Critical Citations

- [Agcaoili, 2022] — Documents 21% rise in Philippine credit card fraud post‑pandemic, grounding the paper’s problem statement.  
- [Abdallah et al., 2016] — Surveys fraud detection systems and lists LR, decision trees, ANN, SVM as standard tools.  
- [Awoyemi et al., 2017] — Provides the comparative ML accuracy benchmarks (LR 54.86%, k‑NN 97.69%, Naïve Bayes 97.92%) that Table 1 cites.  

## Relevance to Odin

**Topics:**

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

**Contribution to Odin:**

This paper directly informs Odin’s anomalous spending detection module by benchmarking ML classifiers on imbalanced, real‑world transaction data from the Philippines. The finding that k‑NN and Naïve Bayes achieve >97% accuracy on highly skewed fraud data supports algorithm selection for detecting rare spending anomalies in Odin’s manual transaction logs. Although the domain is credit card fraud, the methodological lessons—handling class imbalance, evaluating with MCC/BCR, and the trade‑off between ANN accuracy and LR interpretability—apply directly to Odin’s need to flag unusual spending patterns without false‑alert fatigue.

**Directly justifies:**

- “k‑NN achieved 97.69% accuracy and Naïve Bayes 97.92% accuracy on Philippine credit card transaction data, outperforming logistic regression (54.86%) for imbalanced binary classification.”  
- “ANN with SMOTE enhancement outperformed all other model combinations on accuracy, precision, recall, and F1, making it a strong candidate for anomaly detection when interpretability is not the primary constraint.”  
- “Imbalanced data and concept drift are key challenges in transaction anomaly detection; hybrid sampling and meta‑learning are necessary to maintain real‑time performance.”  
- “MCC and BCR are more reliable than raw accuracy for evaluating detectors on highly skewed datasets where fraud (anomaly) cases are rare.”

**Limits of relevance:**

- The paper targets credit card fraud, not personal spending anomalies (e.g., overspending in a category). Fraud patterns may differ from legitimate but unusual spending.  
- No evaluation of cold‑start performance (new users with no transaction history), which is critical for Odin.  
- Dataset is not publicly described (size, features, class imbalance ratio), limiting replicability.  
- Algorithms compared are supervised; Odin’s anomaly detection may require unsupervised methods due to lack of labeled anomalies.

## Limitations

- Dataset size and exact class imbalance ratio are not reported, making it difficult to judge generalizability.  
- No comparison of supervised vs. unsupervised anomaly detection methods (e.g., Isolation Forest), which are more relevant when labeled fraud is unavailable. [unacknowledged]  
- The paper does not evaluate computational cost or latency for real‑time detection on mobile devices. [unacknowledged]  
- Concept drift is mentioned but not empirically tested; no longitudinal evaluation over changing fraud patterns.  
- Accuracy figures for SVM and ANN are reported as “varies up to” without specific dataset conditions, reducing precision.

## Remember This

- 🔑 **k‑NN (97.7%) and Naïve Bayes (97.9%)** — top accuracy for imbalanced fraud data in the Philippines.  
- 📌 MCC and BCR > raw accuracy — always use balanced metrics when anomalies are rare.  
- ⚠️ ANN‑SMOTE best overall — but explainability suffers; Odin’s alert system may need interpretable models.  
- 💡 Imbalanced data + concept drift are the real enemies — hybrid sampling and meta‑learning are the fixes.
