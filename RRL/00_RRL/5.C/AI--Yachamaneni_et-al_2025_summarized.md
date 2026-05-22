# Credit Card Customer Profiling Using Self-Supervised Representation Learning on Multi-Source Financial Data

## Metadata

```yaml
---
paper_id: "10.63282/3050-9262.IJAIDSML-V6I1P118"
designation: algorithm-specific
title: "Credit Card Customer Profiling Using Self-Supervised Representation Learning on Multi-Source Financial Data"
authors: "Yachamaneni, T.; Kotadiya, U.; Arora, A. S."
year: 2025
venue: "International Journal of Artificial Intelligence, Data Science, and Machine Learning"
odin_topics: ["5.A", "5.C"]
shorthand_tags: ["/profiling-role", "/classification-vs-clustering", "/classifier-candidates", "/classifier-eval-metrics"]
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

Self-supervised learning on multi-source financial data produces richer customer profiles than K-Means or XGBoost, improving credit risk AUC to 0.91 and churn F1 to 0.81.

## Problem and Motivation

Traditional customer profiling relies on labeled data and hand-crafted features, which are costly, privacy-sensitive, and fail to capture complex temporal patterns. Financial institutions generate massive unlabeled multi-source data (transactions, demographics, credit reports, web activity) that remains underutilized. No prior approach systematically applies self-supervised learning to integrate all four modalities for unsupervised customer representation learning.

## Approach

- Data: 100,000 customers with transaction logs, demographics, credit bureau reports, and web activity logs.
- Preprocessing: Missing data handling, normalization, categorical embeddings, sinusoidal temporal encoding.
- SSL pretext tasks: contrastive learning (augmented view matching), masked attribute prediction, temporal order prediction.
- Model: Transformer encoder with multi-head attention, followed by MLP head and clustering layer (K-Means).
- Training: Self-supervised on unlabeled data, then fine-tuned for downstream tasks (credit risk, churn prediction).
- Baselines: K-Means clustering and XGBoost supervised classifier.
- Evaluation metrics: Silhouette score (clustering), AUC (credit risk), F1-score (churn prediction).

## Findings

1. SSL achieved Silhouette score 0.56 vs K-Means 0.35 and XGBoost 0.41.
2. SSL reached credit risk AUC **0.91** vs XGBoost 0.84 and K-Means 0.71.
3. SSL churn prediction F1-score 0.81 vs XGBoost 0.69 and K-Means 0.58.

- Ablation: Removing temporal encoding dropped AUC by 4.2%; removing web activity dropped 3.8%; removing pretext tasks dropped 2.7%.

## Key Figures and Tables

- Table 1: Quantitative Results → SSL outperforms baselines on all metrics (Silhouette 0.56, AUC 0.91, F1 0.81).
- Figure 9: Bar graph of results → SSL highest across three metrics.
- Table 2: Ablation study → Temporal encoding most critical (4.2% AUC drop).

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| SSL | Self-Supervised Learning — training on unlabeled data by solving auxiliary tasks like predicting missing values. |
| Contrastive learning | A technique that pulls similar data points together and pushes dissimilar ones apart in embedding space. |
| Pretext task | A self-supervised training task (e.g., predicting masked attributes) that forces the model to learn useful representations. |
| AUC | Area Under the ROC curve — probability that a model ranks a random positive instance higher than a random negative one. |
| Silhouette score | A measure of how similar a point is to its own cluster compared to other clusters; higher = better separated clusters. |

## Critical Citations

- [Chen et al., 2020] — SimCLR framework for contrastive learning, basis for SSL pretext tasks.
- [Devlin et al., 2019] — BERT masked language modeling, inspiration for masked attribute prediction.
- [Chen & Guestrin, 2016] — XGBoost used as a supervised baseline.
- [MacQueen, 1967] — K-Means clustering baseline.

## Relevance to Odin

**Topics:**

5.A — Financial Behavioral Profiles in Personal Finance

5.C — Financial Behavioral Profile Classification Algorithm

**Contribution to Odin:**

This paper demonstrates that self-supervised learning on multi-source financial data (transactions, demographics, credit, web activity) produces superior customer profiles compared to traditional clustering or supervised methods. For Odin's financial behavioral profiling module, SSL offers a label-efficient way to learn user representations from transaction history alone (since Odin has no web activity or credit data, but the principle of using sequential transaction data with temporal encoding applies). The finding that temporal encoding provides the largest performance gain (4.2% AUC drop when removed) directly justifies Odin's use of sequential modeling for spending forecasting and profile classification.

**Directly justifies:**

- "Self-supervised learning on unlabeled transaction sequences improves clustering coherence by 60% over K-Means (Silhouette 0.56 vs 0.35) without requiring labeled data."
- "Temporal encoding of transaction timestamps yields the single largest contribution to predictive accuracy, with removal causing a 4.2% drop in credit risk AUC."
- "Contrastive learning and masked attribute prediction enable robust customer representations that generalize to downstream tasks such as risk assessment and churn prediction."
- "Multi-modal integration (transaction, demographic, credit, web) outperforms any single modality, but transaction and temporal signals dominate."

**Limits of relevance:**

- Study uses credit card data from a private bank, not personal budgeting data; spending patterns differ (credit vs debit/cash).
- No Filipino demographic data; cultural and income patterns may not generalize.
- Web activity and credit bureau reports are unavailable in Odin's manual-input, no-banking-integration scope.
- Odin does not perform churn prediction or credit risk assessment, but the representation learning method transfers to spending forecasting and profile classification.

## Limitations

- Dataset not publicly available; reproducibility unknown. [unacknowledged]
- No evaluation of cold-start performance — model assumes sufficient historical data per customer. [unacknowledged]
- SSL pretext tasks require careful design; effectiveness may vary with data volume (Odin's per-user data is sparse early on).
- Paper does not address model interpretability, which is critical for financial user trust.

## Remember This

- 🔑 **AUC 0.91** for credit risk — SSL beats XGBoost by 7 points.
- 📌 Temporal encoding drives 4.2% gain — time order matters most.
- 💡 Unlabeled transaction data alone can learn rich profiles via contrastive learning.
- ⚠️ No cold-start test — Odin's new users may need different handling.
