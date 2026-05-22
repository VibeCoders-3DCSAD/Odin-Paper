# Machine Learning Methods in Customer Segmentation and Recommendation Systems

## Metadata

```yaml
---
paper_id: "10.1051/shsconf/202521802012"
designation: algorithm-specific
title: "Machine Learning Methods in Customer Segmentation and Recommendation Systems"
authors: "Guo, Y."
year: 2025
venue: "SHS Web of Conferences, ICDDE 2025"
odin_topics: ["4.A", "5.C", "6.A", "6.B", "7.B", "8.B", "10.A", "12.B"]
shorthand_tags: ["/pfms-intelligent-features", "/classification-vs-clustering", "/classifier-candidates", "/classifier-eval-metrics", "/forecast-algo-candidates", "/forecast-algo-comparison", "/budget-rec-approaches", "/anomaly-algo-candidates", "/data-sensitivity", "/eval-ml-design"]
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

K-means, DBSCAN, and collaborative filtering improve segmentation and recommendation accuracy by 12–18% in e-commerce, banking, and healthcare, but data quality and privacy remain challenges.

## Problem and Motivation

Traditional demographic and geographic customer segmentation fails to handle the size and complexity of modern datasets. Businesses need scalable, automated solutions to classify customers and deliver personalized recommendations that drive sales. Prior methods lacked the ability to process high-volume data and adapt to changing consumer preferences.

## Approach

- Paper is a comparative review of machine learning methods for customer segmentation and recommendation systems.
- Segmentation algorithms surveyed: K-means clustering (requires pre‑specified cluster count, assumes spherical clusters), DBSCAN (density‑based, handles noise and irregular shapes), PCA (dimensionality reduction as pre‑processing).
- Recommendation methods: collaborative filtering (user‑ or item‑based, suffers cold start and scalability), content‑based filtering (relies on item metadata quality), hybrid models (combine both, e.g., matrix factorization + deep learning).
- Case studies: Amazon (collaborative filtering + DBSCAN for fraud detection), banking (PCA for anomaly detection in transactions), healthcare (K‑means and DBSCAN for patient grouping).
- Evaluation metrics: accuracy improvements reported as percentage gains over baseline methods.

## Findings

1. **Amazon achieved a 12% improvement in recommendation accuracy** by applying DBSCAN over K‑means for handling noisy transaction data.
2. PCA‑based preprocessing improved anomaly detection accuracy by **15%** in banking transactional data.
3. DBSCAN improved patient classification accuracy by **18%** in noisy healthcare datasets (chronic disease management).

- Collaborative filtering faces cold start (new users/items) and scalability issues with large datasets.
- Content‑based filtering depends heavily on metadata quality; poor labels degrade performance.
- Hybrid models combine user behavior and item attributes to overcome individual method limitations.

## Key Figures and Tables

None.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| K‑means | Clustering algorithm that groups data into a pre‑specified number of spherical clusters. |
| DBSCAN | Density‑based clustering that identifies dense regions as clusters and marks low‑density points as noise. |
| PCA | Principal Component Analysis – reduces data dimensions while preserving variance, used as pre‑processing. |
| Collaborative filtering | Recommendation method based on past user interactions (e.g., “users who bought this also bought…”). |
| Content‑based filtering | Recommendation method that uses item attributes (genre, actor) rather than user interaction history. |
| Cold start problem | System cannot recommend for new users or items due to lack of historical interaction data. |

## Critical Citations

- [Owolabi et al., 2024] — Comparative ML analysis for customer churn in U.S. banking.
- [Amin & Chatterjee, 2023] — Benchmark of ML models for customer segmentation.
- [Johnson et al., 2021] — ML for customer segmentation in digital banking.
- [Chen et al., 2022] — ML for fraud detection in banking, citing PCA gains.

## Relevance to Odin

**Topics:**

4.A — Landscape of Existing Personal Finance Systems

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

7.B — Budget Recommendation in Personal Finance Systems

8.B — Anomaly Detection Algorithm

10.A — Data Privacy and Security in Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This survey directly informs Odin’s algorithm selection for customer segmentation (financial profiling) and recommendation (budget suggestions). The comparison of K‑means, DBSCAN, and PCA justifies using density‑based clustering (DBSCAN) for outlier detection in transaction data and dimensionality reduction for high‑dimensional spending patterns. The discussion of collaborative filtering’s cold start problem supports Odin’s reliance on content‑based and hybrid approaches when user history is sparse. Reported accuracy gains (12–18%) provide benchmarks for evaluating Odin’s modules.

**Directly justifies:**

- “DBSCAN improves recommendation accuracy by 12% over K‑means when handling noisy data, as demonstrated in Amazon’s e‑commerce platform.”
- “PCA reduces noise and improves anomaly detection accuracy by 15% in banking transactional data, applicable to spending anomaly detection.”
- “Collaborative filtering suffers from cold start and scalability issues; hybrid models overcome these by combining user behavior and item attributes.”
- “The Equifax 2017 data breach exposed 147 million records, underscoring the need for advanced encryption and privacy‑by‑design in financial systems.”

**Limits of relevance:**

- Paper is a literature review, not an original experimental study; claims rely on cited sources.
- Demographics and datasets are not Filipino; spending patterns may differ.
- Domains include e‑commerce and healthcare, not exclusively personal finance; algorithm transferability requires validation.
- No evaluation of cold‑start performance for recommendation algorithms in personal finance contexts.

## Limitations

- Review format lacks original experimental rigor; no unified benchmark across compared methods. [unacknowledged]
- Accuracy improvements (12%, 15%, 18%) come from different studies with different datasets and tasks, limiting direct comparability.
- Privacy discussion is superficial (only Equifax example); no technical details on encryption or anonymization. [unacknowledged]
- Does not address how segmentation and recommendation handle concept drift or user behavior changes over time. [unacknowledged]
- No discussion of computational costs or scalability constraints on mobile devices, relevant to Odin’s mobile‑first design.

## Remember This

- 🔑 **DBSCAN beats K‑means by 12%** on noisy transaction data – use density‑based clustering for outlier detection.
- 💡 **PCA boosts anomaly detection by 15%** – dimensionality reduction helps spot suspicious spending.
- 📌 **Cold start limits collaborative filtering** – content‑based or hybrid models work better for new users.
- ⚠️ **Data quality and privacy are critical** – the Equifax breach (147M records) shows the stakes.
