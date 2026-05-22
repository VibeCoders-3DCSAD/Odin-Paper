# User Profiling Based on Financial Transaction Patterns: A Clustering Approach for User Segmentation

## Metadata

```yaml
---
paper_id: "10.47738/ijaim.v4i4.92"
designation: algorithm-specific
title: "User Profiling Based on Financial Transaction Patterns: A Clustering Approach for User Segmentation"
authors: "Pratama, S. F.; Putri, N. A."
year: 2024
venue: "International Journal for Applied Information Management"
odin_topics: ["3.A", "5.A", "5.C", "8.A"]
shorthand_tags: ["/cat-approaches", "/profiling-role", "/profile-dimensions", "/classification-vs-clustering", "/classifier-candidates", "/classifier-tradeoffs", "/classifier-eval-metrics"]
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

K-means clustering on transaction amount, time, and type identifies three user segments with distinct spending behaviors, achieving a moderate Silhouette Score of 0.33.

## Problem and Motivation

Traditional user segmentation methods rely on static categories and miss nuanced transaction patterns, leading to incomplete customer insights. Better profiling enables personalized financial services, fraud detection, and targeted marketing in increasingly complex digital finance ecosystems. Prior work lacked granular segmentation using multiple transaction features (amount, time, type) simultaneously to reveal distinct behavioral groups.

## Approach

- Dataset: Simulated financial transactions from Kaggle (Python Faker library) covering one month.
- Preprocessing: Imputed missing values, scaled numerical features, one-hot encoded categorical variables, extracted hour and day of week from timestamps.
- Algorithm: K-means clustering with Euclidean distance, minimizing within-cluster sum of squares (WCSS).
- Features: Transaction amount, hour of day, day of week, transaction type (purchase, transfer, withdrawal).
- Evaluation: Silhouette Score to determine optimal cluster count and separation quality.
- Visualization: PCA and t-SNE projections for 2D cluster separation.

## Findings

1. Three distinct clusters identified: Cluster 0 (purchases, ~11 AM Monday, mean amount 1877), Cluster 1 (transfers, ~1:35 PM Wednesday, mean amount 4147), Cluster 2 (purchases, ~11 AM Friday, mean amount 1970).
2. **Silhouette Score of 0.33** indicates moderate cluster separation with some overlap.
3. Cluster distribution: Cluster 2 highest transaction count (>20), Cluster 0 lowest (<15).

- PCA and t-SNE visualizations show clear separation between clusters in reduced dimensions.
- One-month dataset limits detection of seasonal or long-term behavioral trends.

## Key Figures and Tables

- Figure 2: 3D clustering plot (hour, amount, cluster) → three clusters separate by amount and hour.
- Figure 3: Cluster distribution bar chart → Cluster 2 has highest transaction volume.
- Table 1: Cluster characteristics (mean amount, hour, day of week) → Cluster 1 has highest amount and mid-week timing.
- Figure 4: PCA projection → clusters separate along first two principal components.
- Figure 5: t-SNE projection → confirms cluster separation in non-linear embedding.

## Key Equations

$$ d(x_i, C_j) = \sqrt{\sum_{k=1}^{n} (x_{i,k} - c_{j,k})^2 } $$
*Euclidean distance between data point and centroid, used for cluster assignment.*

$$ WCSS = \sum_{i=1}^{K} \sum_{x_i \in C_k} (x_i, c_k)^2 $$
*Within-cluster sum of squares — K-means minimizes this objective.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| K-means | Clustering algorithm that groups data into K clusters by minimizing distances to centroids. |
| Silhouette Score | Metric from -1 to +1 measuring how well each point fits its cluster (higher = better separation). |
| WCSS | Sum of squared distances between points and their cluster center — lower means tighter clusters. |
| PCA | Principal Component Analysis — reduces data dimensions while preserving variance. |
| t-SNE | t-Distributed Stochastic Neighbor Embedding — non-linear dimensionality reduction for visualization. |
| DBSCAN | Density-based clustering algorithm that finds arbitrarily shaped clusters (mentioned as alternative). |
| Centroid | Center point of a cluster, calculated as mean of all points in that cluster. |

## Critical Citations

- [Chen, 2024] — K-means application in marketing segmentation, supporting algorithm selection.
- [Zhao et al., 2021] — Extended regularized K-means for transaction-based customer segmentation.
- [Zhang et al., 2020] — DBSCAN for fraud detection in low-frequency transactions, referenced as alternative method.

## Relevance to Odin

**Topics:**

3.A — Expense Categorization Frameworks

5.A — Financial Behavioral Profiles in Personal Finance

5.C — Financial Behavioral Profile Classification Algorithm

8.A — Anomaly Detection in Personal Finance Systems

**Contribution to Odin:**

This paper directly informs Odin's financial behavioral profiling module by demonstrating that K-means clustering on transaction amount, time, and type can segment users into interpretable behavioral groups. The use of transaction type (purchase vs. transfer) as a feature aligns with Odin's expense categorization design. Although the dataset is simulated and not Filipino, the methodology provides a baseline for user segmentation that Odin can adapt using real transaction histories from manual inputs. The moderate Silhouette Score (0.33) also justifies considering alternative clustering algorithms (e.g., DBSCAN) for better separation.

**Directly justifies:**

- "K-means clustering on transaction amount, hour of day, day of week, and transaction type produces three distinct user segments with different spending behaviors."
- "A Silhouette Score of 0.33 indicates moderate cluster separation, suggesting density-based methods like DBSCAN may improve segmentation quality."
- "Transaction amount, time of day, and day of week are effective features for profiling financial users without requiring labeled training data."
- "Purchase-focused clusters (Clusters 0 and 2) differ by day of week (Monday vs. Friday), revealing weekly spending cycles."

**Limits of relevance:**

- Dataset is simulated, not real user transactions — real-world noise and irregularity may affect cluster quality.
- Single month of data — cannot capture seasonal spending patterns or behavioral drift over time.
- Geography not specified — findings may not generalize to Filipino young professionals' spending habits.
- Silhouette Score of 0.33 is moderate — clusters overlap, limiting practical deployment without refinement.
- No evaluation of how clusters evolve when new transaction data arrives (cold-start or concept drift).

## Limitations

- Dataset limited to one month of simulated transactions — cannot capture seasonal or long-term behavioral patterns.
- Silhouette Score of 0.33 indicates only moderate cluster separation — overlapping clusters may cause misclassification. [unacknowledged]
- No validation with domain experts to confirm whether identified clusters are financially meaningful or actionable.
- K-means assumes spherical clusters of equal size — may not fit real transaction distributions with outliers.
- Dataset size and composition not fully disclosed (only transaction counts shown in figures), limiting reproducibility.

## Remember This

- 🔑 **0.33 Silhouette Score** — clusters are distinguishable but overlap; try DBSCAN for better separation.
- 📌 Three segments: purchase-early-week (Mon AM), transfer-midweek (Wed PM), purchase-late-week (Fri AM).
- 💡 Amount, hour, and day of week are key features — time features reveal weekly cycles.
- ⚠️ One-month simulated data — real-world validation needed for Filipino users.
