# A Review of Machine Learning and Deep Learning Approaches for Fraud Detection Across Financial and Supply Chain Domains

## Metadata

```yaml
---
paper_id: "10.21203/rs.3.rs-7893661/v1"
designation: international
title: "A Review of Machine Learning and Deep Learning Approaches for Fraud Detection Across Financial and Supply Chain Domains"
authors: "Martínez, O.; Sánchez, P.; Alcaraz, E."
year: 2025
venue: "Research Square"
odin_topics: ["D.1", "D.2", "E.1", "E.2", "F.2", "J.1"]
shorthand_tags: ["/forecasting-methods", "/lstm-architecture", "/anomaly-approaches", "/isolation-forest", "/anomaly-algo-justification", "/classifier-candidates", "/eval-frameworks"]
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

Ensemble methods (XGBoost, LightGBM, Random Forest) consistently outperform deep learning on tabular fraud data, while two-phase semi-supervised frameworks (Isolation Forest + self-training SVM) achieve strong performance with only 1.2% labeled data.

## Problem and Motivation

Rule-based fraud detection systems fail against dynamic, sophisticated fraud schemes. Machine learning offers adaptive solutions but existing research is fragmented across domains and lacks systematic comparison. No prior review bridged financial and supply chain fraud detection while comprehensively comparing traditional ML, deep learning, ensemble, and semi-supervised methods.

## Approach

- Systematic review following PRISMA guidelines, analyzing 97 high-quality studies published 2015–2025.
- Categorizes algorithms into five families: traditional ML (SVM, Random Forest, Logistic Regression), deep learning (CNN, LSTM, autoencoders), ensemble (XGBoost, LightGBM, stacking), semi‑supervised/unsupervised (Isolation Forest, self‑training), and emerging (federated learning, GNNs).
- Evaluates methods on benchmark datasets: European Credit Card (284k transactions, 0.17% fraud), IEEE-CIS (590k transactions, 3.5% fraud), and DataCo Smart Supply Chain.
- Uses metrics: accuracy, precision, recall, F1‑score, AUC‑ROC, AUC‑PR, plus computational cost and interpretability analysis.

## Findings

1. **Ensemble stacking achieved AUC-PR of 0.891, a 2% improvement over single models, on IEEE-CIS dataset.**
2. XGBoost and LightGBM deliver AUC‑ROC of 0.90‑0.93 on IEEE‑CIS, outperforming deep neural networks on tabular fraud data.
3. Isolation Forest pre‑filtering reduces data volume by 76% while capturing 94% of fraud, enabling semi‑supervised learning with only 1.2% labels (F1 = 0.817, FPR < 3%).
4. LSTM networks achieve 89‑92% AUC‑ROC on sequential fraud detection (e.g., transaction sequences), but require more data and longer training than gradient boosting.

- Borderline‑SMOTE outperforms standard SMOTE and ADASYN for handling extreme class imbalance (fraud rates < 1%).

## Key Figures and Tables

- Table 3: Comparative analysis of ensemble methods (Random Forest, XGBoost, LightGBM, CatBoost, stacking) → stacking gives highest accuracy but lower interpretability.
- Table 7: Performance summary on major benchmarks → ensemble methods reach 0.92‑0.93 AUC‑ROC on IEEE‑CIS; deep learning lags slightly.
- Figure (Isolation Forest path length illustration): anomalies isolate faster → shorter path length → higher anomaly score.

## Key Equations

$$s(x,n) = 2^{-\frac{E[h(x)]}{c(n)}}$$
*Isolation Forest anomaly score; lower expected path length indicates anomaly.*

$$Precision = \frac{TP}{TP+FP},\quad Recall = \frac{TP}{TP+FN},\quad F1 = 2\cdot\frac{Precision\cdot Recall}{Precision+Recall}$$
*Key imbalanced‑classification metrics; accuracy alone is misleading for fraud detection.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| AUC‑ROC | Area under the Receiver Operating Characteristic curve — probability that a random fraud scores higher than a random legitimate transaction. |
| AUC‑PR | Area under the Precision‑Recall curve — more informative than AUC‑ROC for extreme class imbalance. |
| LSTM | Long Short‑Term Memory [think: memory cell with forget/input/output gates for sequence learning] — captures temporal dependencies in transaction sequences. |
| Isolation Forest | Tree‑based anomaly detector that isolates anomalies in fewer random splits — no labels required, linear time complexity. |
| SMOTE | Synthetic Minority Oversampling Technique — creates synthetic fraud examples by interpolating between existing frauds. |
| Concept drift | Change in fraud patterns over time; models degrade 10‑30% within 6‑12 months without retraining. |

## Critical Citations

- [Chawla et al., 2002] — Introduced SMOTE, the most widely used oversampling technique for imbalanced fraud data.
- [Chen & Guestrin, 2016] — XGBoost algorithm, the dominant fraud detection method in production and competitions.
- [Liu et al., 2008] — Isolation Forest, enabling unsupervised pre‑filtering for semi‑supervised fraud detection.
- [Dal Pozzolo et al., 2014] — Practitioner insights on credit card fraud detection, including threshold calibration and undersampling.

## Relevance to Odin

**Topics:**

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

E.1 — Anomaly Detection in Personal Finance Systems

E.2 — Anomaly Detection Algorithm

F.2 — Profile Classification Algorithm

J.1 — System Evaluation

**Contribution to Odin:**

This review directly informs Odin’s algorithm selection across multiple modules. For the anomaly detection module, it provides a direct comparison of Isolation Forest (unsupervised, fast) against supervised alternatives, and shows that a two‑phase unsupervised‑plus‑semi‑supervised framework achieves strong performance with minimal labeled data — critical for Odin’s cold‑start user problem. For spending forecasting, the review benchmarks LSTM against GRU and XGBoost on sequential transaction data, reporting LSTM’s 89‑92% AUC‑ROC but also its higher computational cost, justifying a trade‑off analysis. For user profile classification, the review evaluates Random Forest, XGBoost, and SVM classifiers on high‑dimensional imbalanced data, providing evidence for classifier choice. Finally, the review’s emphasis on evaluating with AUC‑PR (not just accuracy) and using temporal train‑test splits sets a standard for Odin’s system evaluation under ISO 25010.

**Directly justifies:**

- "Ensemble methods (XGBoost, LightGBM, Random Forest) consistently achieve AUC‑ROC of 0.90‑0.93 on imbalanced fraud datasets, outperforming deep neural networks on tabular data."
- "Isolation Forest pre‑filtering reduces data volume by 76% while capturing 94% of anomalies, enabling effective semi‑supervised learning with only 1.2% labeled data — directly applicable to Odin’s cold‑start anomaly detection."
- "LSTM networks achieve 89‑92% AUC‑ROC for sequential transaction fraud detection, but require 3‑5x longer training than XGBoost and GPU acceleration for real‑time inference."
- "Borderline‑SMOTE improves fraud recall by 12‑15% over standard SMOTE on the IEEE‑CIS dataset, making it the preferred oversampling method for extreme class imbalance."

**Limits of relevance:**

- Review focuses on fraud detection (malicious transactions), not spending anomalies (budget overages or unusual but legitimate spending) — Odin’s anomaly detection is behavioral, not criminal.
- Benchmark datasets (European credit card, IEEE‑CIS) are from Western institutions; spending patterns and fraud typologies may differ in the Philippine young professional context.
- LSTM performance reported (89‑92% AUC‑ROC) is on transaction sequences of 10‑50 items; Odin’s forecasting module uses per‑category spending time series, which may have different temporal dependencies.
- Privacy‑preserving techniques (federated learning, differential privacy) are discussed but their accuracy‑privacy trade‑off (5‑15% loss) may be unacceptable for Odin’s resource‑constrained mobile setting.

## Limitations

- Predominantly focused on financial fraud (credit card, insurance) and supply chain; direct applicability to personal budget management (non‑fraudulent overspending) is limited. [unacknowledged]
- Most benchmark datasets are dated (European dataset from 2013) or synthetically transformed (PCA), reducing generalizability to contemporary Filipino spending data.
- Deep learning comparisons are based on static tabular datasets; no evaluation of on‑device LSTM for mobile resource constraints (battery, CPU) — critical for Odin.
- Label delay (fraud conﬁrmation lag) is identified as a problem but no concrete solution is provided; Odin faces similar delay in obtaining user‑confirmed anomaly labels.
- The review acknowledges publication bias (positive results overrepresented) but does not quantify its effect on reported performance metrics.

## Remember This

- 🔑 **Ensemble stacking tops at AUC‑PR 0.891** — 2% gain over single XGBoost on IEEE‑CIS.  
- 📌 **Isolation Forest cuts data by 76%** — captures 94% of fraud for semi‑supervised learning with minimal labels.  
- 💡 **LSTM gets 89‑92% AUC‑ROC** — but requires 3‑5x training time and GPU; questionable for mobile‑first Odin.  
- ⚠️ **Borderline‑SMOTE beats SMOTE** — improves recall by 12‑15% on extreme imbalance (fraud < 1%).
