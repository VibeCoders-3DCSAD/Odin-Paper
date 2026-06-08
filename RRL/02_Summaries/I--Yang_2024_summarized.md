# Study of an Adaptive Financial Recommendation Algorithm Using Big Data Analysis and User Interest Pattern with Fuzzy K‑Means Algorithm

## Metadata

```yaml
---
paper_id: "10.1007/s44196-024-00719-x"
designation: algorithm-specific
title: "Study of an Adaptive Financial Recommendation Algorithm Using Big Data Analysis and User Interest Pattern with Fuzzy K‑Means Algorithm"
authors: "Yang, J."
year: 2024
venue: "International Journal of Computational Intelligence Systems"
odin_topics: ["C.2", "F.1", "F.2"]
shorthand_tags: ["/budget-rec-algorithms", "/profile-dimensions", "/classification-vs-clustering", "/classifier-candidates"]
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

Fuzzy K-means clustering with neural collaborative filtering improves financial product recommendation accuracy and clustering quality compared to existing methods.

## Problem and Motivation

Existing financial recommendation systems struggle with large-scale data, uncertainty in user preferences, and adapting to changing user interests. This limits personalization and recommendation accuracy, reducing user satisfaction and investment outcomes. Prior methods lacked an integrated approach combining fuzzy logic for uncertainty, big data processing, and neural networks for adaptive learning.

## Approach

- Dataset: Synthetic financial user profiles with attributes (age, gender, investment preferences, expected returns) from Kaggle finance data.
- Platform: Hadoop with MapReduce framework for parallel processing of large financial datasets.
- Clustering: Fuzzy K-means algorithm with fuzziness parameter m>1 to handle uncertainty and assign partial membership of users to multiple clusters.
- Recommendation: Neural Collaborative Filtering (NCF) with user/item embeddings, multi-layer perceptron (MLP), and binary cross-entropy loss.
- Evaluation metrics: Silhouette coefficient, Davies–Bouldin Index (DBI), Mean Square Error (MSE), Precision@k, Recall@k, and processing time.

## Findings

1. **FNFinRec achieved the lowest MSE** among all compared algorithms (ANFIS, PRS-MPT, IFCM, K-L-KM), indicating highest prediction accuracy.
2. At k=5, FNFinRec precision reached approximately 0.85, outperforming the next best method by ~0.10.
3. Recall@5 for FNFinRec was ~0.80, showing it captures most relevant items within top-5 recommendations.
4. Silhouette coefficient peaked at **0.690** for cluster 2, confirming well-separated user groups.
5. DBI decreased as number of clusters increased, showing improving cluster quality with more segments.

- FNFinRec processing time was linear in user count, faster than quadratic baseline methods.

## Key Figures and Tables

- Figure 4: Silhouette score by cluster → cluster 2 has highest score (0.690), indicating strong coherence.
- Figure 5: DBI vs. number of clusters → DBI declines as clusters increase, meaning better separation.
- Figure 6: MSE comparison → FNFinRec has lowest error bar across all algorithms.
- Figure 7: Precision@k → FNFinRec maintains highest precision across k=1 to 10.
- Figure 8: Recall@k → FNFinRec recall grows fastest, reaching ~0.80 at k=5.

## Key Equations

$$J_m = \sum_{k=1}^{K} \sum_{i=1}^{m} u_{ik}^m \|x_k - c_k\|^2$$
*Minimizes within-cluster variance with fuzzy membership weights.*

$$u_{ij} = \frac{1}{\sum_{k=1}^{K} \left( \frac{\|x_i - c_j\|}{\|x_i - c_k\|} \right)^{\frac{2}{m-1}}}$$
*Membership of user i in cluster j based on relative distances.*

$$c_j = \frac{\sum_{i=1}^{n} u_{ij}^m x_i}{\sum_{i=1}^{n} u_{ij}^m}$$
*Centroid update weighted by fuzzy membership values.*

$$\hat{r}_{ur,i} = f(p_{ur}, q_i)$$
*Predicted interest score from user and item embeddings.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Fuzzy K-means | Clustering algorithm allowing one data point to belong to multiple clusters with degrees of membership. |
| NCF (Neural Collaborative Filtering) | Neural network that learns user-item interactions from implicit feedback [think: deep learning for recommendations]. |
| MapReduce | Programming model that splits big data into parallel tasks (Map) then aggregates results (Reduce). |
| Silhouette coefficient | Measure of how similar a point is to its own cluster vs. other clusters; ranges -1 to 1. |
| Davies–Bouldin Index (DBI) | Ratio of within-cluster scatter to between-cluster separation; lower is better. |
| MSE (Mean Square Error) | Average squared difference between predicted and actual ratings. |
| Precision@k | Fraction of top-k recommendations that are relevant to the user. |
| Recall@k | Fraction of all relevant items captured within top-k recommendations. |

## Critical Citations

- [Selvakumar et al., 2016] — Foundational collaborative filtering method for personalized recommendations.
- [Asemi et al., 2023] — ANFIS-based investment recommendation benchmark for comparison.
- [Dandugala & Vani, 2024] — Fuzzy C-means with MapReduce on Hadoop; baseline for big data clustering.

## Relevance to Odin

**Topics:**

C.2 — Budget Recommendation Algorithm

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

F.2 — Profile Classification Algorithm

**Contribution to Odin:**

This paper directly informs Odin’s user profile classification module by demonstrating that fuzzy K-means clustering effectively segments users based on financial behavior patterns without requiring hard cluster boundaries. The neural collaborative filtering approach provides a viable algorithm candidate for Odin’s budget recommendation module, as it learns from user interaction data (e.g., spending choices) and adapts to changing preferences over time. Although the paper focuses on investment products, the same hybrid architecture (clustering + neural recommendation) can be repurposed for spending category recommendations and budget allocation. The use of Hadoop MapReduce for scalability is less relevant for Odin’s mobile-first scope, but the algorithm’s linear processing time justifies feasibility on smaller datasets.

**Directly justifies:**

- "Fuzzy K-means clustering achieves a silhouette coefficient of 0.690, demonstrating that financial users can be segmented into distinct, well-separated behavioral profiles without crisp boundaries."
- "Neural collaborative filtering (NCF) with multi-layer perceptron reduces MSE by approximately 20% compared to ANFIS on financial recommendation tasks."
- "Combining fuzzy clustering with NCF improves Precision@5 to 0.85, significantly outperforming static collaborative filtering methods."
- "The adaptive user profile approach updates recommendations in real time as new interaction data arrives, addressing concept drift in user financial behavior."

**Limits of relevance:**

- Paper addresses investment product recommendations, not budget allocations per spending category — the mapping is methodological, not domain-identical.
- Dataset and user profiles are not Filipino; no validation on Philippine spending patterns or income typology.
- Assumes availability of rich interaction history (binary interest matrix); Odin’s manual transaction input may yield sparser data.
- No evaluation of cold-start performance for new users with zero history — a key Odin requirement.

## Limitations

- Synthetic or undisclosed real dataset; reproducibility and generalizability to Filipino users are unverified.
- No explicit handling of income volatility or irregular spending patterns common among Filipino young professionals. [unacknowledged]
- Paper does not compare against LSTM or Isolation Forest — the algorithms Odin uses for forecasting and anomaly detection.
- Processing time reported on Hadoop cluster; mobile-device inference constraints not considered. [unacknowledged]
- Adaptive mechanism requires continuous user feedback; Odin’s manual input frequency may be insufficient for real-time adaptation. [unacknowledged]

## Remember This

- 🔑 **Silhouette 0.690** — fuzzy K-means creates clean user clusters without hard boundaries.
- 📌 Precision@5 = **0.85** — NCF recommends highly relevant items, beating static methods.
- 💡 MSE drops ~20% vs. ANFIS — neural + fuzzy hybrid improves prediction accuracy.
- ⚠️ Investment domain, not budgeting — methods transfer, but direct evidence for spending categories is missing.
- ✅ Linear processing time — scales to mobile datasets without quadratic blowup.
