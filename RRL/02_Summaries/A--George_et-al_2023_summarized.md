# Machine Learning for Fraud Detection in Digital Banking: A Systematic Literature Review

## Metadata

```yaml
---
paper_id: "10.63125/913ksy63"
designation: international
title: "Machine Learning for Fraud Detection in Digital Banking: A Systematic Literature Review"
authors: "George, M. Z. H.; Alam, M. K.; Hasan, M. T."
year: 2023
venue: "ASRC Procedia: Global Perspectives in Science and Scholarship"
odin_topics: ["D.2", "E.1", "E.2", "J.1"]
shorthand_tags: ["/lstm-architecture", "/lstm-justification", "/anomaly-approaches", "/anomaly-tradeoffs", "/anomaly-ml-families", "/eval-frameworks"]
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

Supervised learning dominates fraud detection, but deep learning (especially LSTM) and hybrid models are rapidly rising, with precision-recall metrics and interpretability frameworks essential for real-world banking deployment.

## Problem and Motivation

The literature on machine learning for fraud detection in digital banking is fragmented across algorithms, evaluation metrics, and regulatory contexts, making it difficult for researchers and practitioners to identify best practices. Without systematic synthesis, institutions may adopt suboptimal methods that fail to address evolving fraud patterns or comply with regional regulations. Prior reviews lacked cross-methodological and cross-regional comparisons, particularly for deep learning, hybrid models, and explainability frameworks.

## Approach

- PRISMA-guided systematic review with four phases: identification, screening, eligibility, and inclusion.
- Databases: Scopus, Web of Science, IEEE Xplore, ACM Digital Library, ScienceDirect, SSRN, Emerald Insight.
- Search terms: “machine learning AND fraud detection,” “digital banking AND anomaly detection,” “credit card fraud AND deep learning.”
- Initial yield: 2,346 records; after screening and eligibility, 118 studies retained.
- Studies categorized: 36 supervised learning, 27 unsupervised/anomaly detection, 19 hybrid, 21 deep learning, 15 evaluation/interpretability.
- Cross-regional analysis: Europe (PSD2/GDPR), North America (fintech-led, model risk governance), emerging economies (mobile-first, infrastructure-dependent).

## Findings

1. Supervised learning remains dominant: 36 studies with **over 9,200 citations**; decision trees, logistic regression, and SVMs are most widely adopted.
2. Deep learning is rising rapidly: 21 studies (primarily RNNs, LSTMs, CNNs, autoencoders) accumulated over 7,300 citations, despite being more recent.
3. Hybrid models (supervised + unsupervised + deep) outperform single-paradigm approaches, with 19 studies garnering **over 5,600 citations**.
4. Evaluation metrics are critical: precision, recall, F1-score, and PR-AUC are preferred over accuracy and ROC-AUC for imbalanced fraud data.

- Unsupervised anomaly detection is essential for capturing novel fraud patterns where labeled data is scarce.
- Interpretability frameworks (SHAP, LIME) are increasingly required for regulatory compliance and analyst trust.

## Key Figures and Tables

- Figure 4: Fraud Detection Machine Learning Framework → supervised, unsupervised, and hybrid paradigms with data flows.
- Figure 5: Deep Learning Fraud Detection Framework → RNN/LSTM, CNN, autoencoders for sequential transaction monitoring.
- Figure 6: Data Imbalance and Real-Time Processing Challenges → SMOTE, cost-sensitive learning, and latency constraints.
- Table (implicit): Study counts by paradigm → supervised (36), deep learning (21), hybrid (19), unsupervised (27), evaluation (15).

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LSTM | Long Short-Term Memory; a recurrent neural network that remembers patterns over long sequences [think: memory cell with forget gate]. |
| RNN | Recurrent Neural Network; processes sequential data by looping back previous outputs. |
| CNN | Convolutional Neural Network; detects local patterns (e.g., spending spikes) using sliding filters. |
| PR-AUC | Precision-Recall Area Under the Curve; measures performance on imbalanced data by focusing on the minority class. |
| ROC-AUC | Receiver Operating Characteristic Area Under the Curve; can overstate performance when fraud is rare. |
| SMOTE | Synthetic Minority Oversampling Technique; creates synthetic fraud examples to balance datasets. |
| SHAP | SHapley Additive exPlanations; assigns each feature a value for a prediction, making black-box models interpretable. |
| LIME | Local Interpretable Model-agnostic Explanations; explains individual predictions by approximating the model locally. |
| PSD2 | Revised Payment Services Directive (EU); mandates strong customer authentication and open banking. |

## Critical Citations

- [Ngai et al., 2011] — Early comprehensive review establishing supervised learning as the fraud detection benchmark.
- [Carcillo et al., 2021] — Demonstrated that hybrid unsupervised-supervised systems reduce false positives while improving recall.
- [Lundberg & Lee, 2017] — Introduced SHAP, now the standard for interpretability in regulated fraud detection.
- [Krawczyk, 2016] — Critiqued ROC-AUC for imbalanced data and advocated PR-AUC as the superior metric.

## Relevance to Odin

**Topics:**

D.2 — LSTM as the Spending Forecasting Algorithm

E.1 — Anomaly Detection in Personal Finance Systems

E.2 — Anomaly Detection Algorithm

J.1 — System Evaluation

**Contribution to Odin:**

This systematic review directly supports Odin’s anomaly detection module by consolidating evidence that hybrid models (e.g., unsupervised anomaly detection followed by supervised classification) reduce false positives while improving recall — a critical trade-off for a personal budget manager where false alerts erode user trust. The review’s finding that LSTM and RNN architectures excel at modeling sequential transaction data justifies Odin’s selection of LSTM for spending forecasting, even though the paper’s domain is fraud detection rather than forecasting. Finally, the emphasis on PR-AUC over ROC-AUC for imbalanced data provides a concrete evaluation guideline for Odin’s anomaly detection algorithm, where fraudulent (or anomalous) spending is rare relative to normal transactions.

**Directly justifies:**

- “LSTM and RNN architectures capture sequential dependencies in transaction streams, outperforming traditional models on temporal patterns (21 reviewed studies, 7,300+ citations).”
- “Hybrid models combining unsupervised anomaly detection with supervised classification reduce false positive rates while improving recall compared to single-paradigm approaches (Carcillo et al., 2021).”
- “PR-AUC is the preferred evaluation metric for imbalanced financial datasets, as ROC-AUC overstates performance when fraud prevalence is below 1% (Krawczyk, 2016).”
- “Interpretability frameworks such as SHAP and LIME are essential for deploying black-box models in regulated environments, providing auditable explanations for each alert.”
- “Unsupervised anomaly detection (clustering, density-based methods, autoencoders) is essential for identifying novel fraud patterns without labeled data — directly applicable to cold-start anomaly detection in personal finance systems.”

**Limits of relevance:**

- The paper focuses on financial fraud (theft, account takeover), not spending anomalies (budget overages, behavioral deviations). The severity and user reaction differ.
- All reviewed studies use banking transaction data (credit cards, wire transfers), not personal budget entries with category labels. Spending patterns may have different temporal signatures.
- Odin relies on manual transaction input, while fraud detection systems typically integrate directly with bank APIs. Data volume and latency constraints differ.
- The review does not evaluate algorithm performance on Filipino spending behavior or income typology.

## Limitations

- No empirical benchmarking of specific algorithms; the review synthesizes existing studies without new experiments, so claimed performance gains are second-hand.
- The review acknowledges heterogeneity in datasets and evaluation metrics across studies, which limits direct comparability of reported results.
- Deep learning studies are mostly recent; long-term deployment challenges (concept drift, adversarial adaptation) are underreported. [unacknowledged]
- Cross-regional analysis is descriptive; no quantitative comparison of model performance under PSD2 vs. non-PSD2 regimes.
- The review does not address cold-start scenarios (new users with no transaction history), a key gap for Odin’s anomaly detection module. [unacknowledged]

## Remember This

- 🔑 **LSTM captures sequential patterns** — 21 deep learning studies (7,300+ citations) confirm RNN/LSTM superiority on transaction streams.
- 📌 PR-AUC beats ROC-AUC for rare events — use precision-recall curves, not accuracy, to evaluate anomaly detection.
- 💡 Hybrid models lower false positives — combining unsupervised (anomaly detection) with supervised (classification) cuts alert noise.
- ⚠️ Fraud ≠ spending anomaly — methods apply but user impact differs (theft vs. overspending).
