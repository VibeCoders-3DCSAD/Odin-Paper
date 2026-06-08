```yaml
paper_id: 10.47738/ijaim.v4i4.92
designation: algorithm-specific
title: User Profiling Based on Financial Transaction Patterns: A Clustering Approach for User Segmentation
authors: Pratama, S. F.; Putri, N. A.
year: 2024
venue: International Journal for Applied Information Management
odin_topics:
  - 5.A
  - 5.C
shorthand_tags:
  - /behavioral-profiles
  - /clustering
tldr: K-means clustering on transaction amounts, times, and types identifies three user segments with distinct spending behaviors, achieving a moderate Silhouette Score of 0.33.
problem_and_motivation: Traditional user segmentation methods rely on predefined categories or historical data, missing nuanced behavioral patterns. The increasing complexity and diversity of transaction data require advanced techniques to capture hidden patterns. Without such techniques, financial institutions cannot fully personalize services or target marketing effectively.
approach:
  - Data source: Simulated financial transaction dataset from Kaggle, generated with Python Faker, containing transaction ID, amount, type, customer ID, and timestamp.
  - Preprocessing: Imputed missing numerical values using mean/median, categorical with mode; removed rows with excessive missingness.
  - Feature extraction: Derived hour, day of week, and month from transaction_time; scaled amount via Min-Max; encoded transaction_type using one-hot or label encoding.
  - Method: K-means clustering with Euclidean distance, initialized via K-Means++, optimized to minimize within-cluster sum of squares (WCSS).
  - Number of clusters selected using Silhouette Score evaluated for different K values, with K=3 maximizing average score.
  - Evaluation: Silhouette Score (0.33) and visual inspections via PCA and t-SNE projections.
findings:
  - num: Silhouette Score of 0.33 indicates moderate cluster separation with some overlap.
  - Three clusters identified: Cluster 0 (mean amount 1876.92, purchases, early week, ~11:15 AM), Cluster 1 (mean amount 4147.06, transfers, mid-week, ~1:35 PM), Cluster 2 (mean amount 1970.00, purchases, late week, ~11:20 AM).
  - num: Cluster 2 has the highest transaction count (just over 20), followed by Cluster 1 (~17), then Cluster 0 (under 15).
  - Transaction day of week distinguishes purchase behavior: Mondays (Cluster 0), Wednesdays (Cluster 1), Fridays (Cluster 2).
  - PCA and t-SNE visualizations show clear but not perfect separation among the three clusters.
key_figures_tables:
  - Figure 2: 3D clustering of users with hour vs amount vs cluster ID → Clusters separate by amount and time.
  - Figure 3: Bar chart of cluster distribution → Cluster 2 has most transactions, Cluster 0 the fewest.
  - Figure 4: PCA projection of clusters → Moderate separation along principal components.
  - Figure 5: t-SNE projection of clusters → Clusters show internal cohesion but some boundary overlap.
  - Table 1: Cluster characteristics (mean amount, std, hour, day_of_week) → Quantitative summary of three segments.
  - Table 2: Statistical summary including transaction type → Cluster 1 exclusively transfers; others purchases.
key_equations:
  - equation: d(x_i, C_j) = sqrt( sum_{k=1}^{n} (x_{i,k} - c_{j,k})^2 )
    explanation: Euclidean distance between data point and centroid.
  - equation: WCSS = sum_{i=1}^{K} sum_{x_i in C_k} (x_i, c_k)^2
    explanation: Within-cluster sum of squares minimized by K-means.
definitions:
  - term: K-means
    definition: Unsupervised clustering algorithm partitioning data into K clusters by minimizing intra-cluster distances.
  - term: Silhouette Score
    definition: Metric from -1 to +1 measuring how similar a point is to its own cluster vs others.
  - term: PCA
    definition: Principal Component Analysis, a linear dimensionality reduction technique.
  - term: t-SNE
    definition: t-Distributed Stochastic Neighbor Embedding for nonlinear dimensionality reduction.
  - term: WCSS
    definition: Within-Cluster Sum of Squares, the objective function of K-means.
critical_citations:
  - "[Zhao et al., 2021] — extended regularized K-means for customer segmentation."
  - "[Zhang et al., 2020] — DBSCAN for fraud detection using transaction patterns."
  - "[Komati, 2025] — ML architectures for real-time financial decision systems."
  - "[Martinovska et al., 2021] — clustering algorithms for business user profiling."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      justification: "Paper segments users based on transaction amount, time, and type into behavioral clusters."
    - code: 5.C
      name: Financial Behavioral Profile Classification Algorithm
      justification: "K-means clustering is the algorithm used to classify users into three distinct profiles."
  contribution: "Clustering on transaction features provides a direct method for constructing financial behavioral profiles in Odin. The identified segments (purchase-dominant early/late week and transfer-dominant mid-week) can inform cold-start personalization when little user history exists. The moderate Silhouette Score of 0.33 establishes a baseline for evaluating Odin's own clustering modules and highlights the need for refinement before deployment."
  directly_justifies:
    - "Transaction amount, time, and type are sufficient features to distinguish user spending segments."
    - "K-means clustering achieves a Silhouette Score of 0.33, indicating moderate but improvable cluster separation."
    - "Users with transfer behaviors tend to have higher transaction amounts and occur mid-week."
    - "Purchase transactions cluster into early-week and late-week subgroups with similar average amounts."
  limits:
    - "Dataset limited to a single month, missing seasonal or long-term behavioral changes."
    - "Simulated data (Faker) may not fully capture real-world financial transaction noise or fraud patterns."
    - "Silhouette Score of 0.33 suggests significant overlap between clusters, limiting practical segmentation accuracy."
    - "No comparison with alternative clustering algorithms (e.g., DBSCAN, hierarchical) to justify K-means choice."
  mapping_rationale: "The paper directly addresses behavioral profiling (Domain: Behavioral profiling & classification) by clustering users based on transaction patterns, selecting 5.A (Financial Behavioral Profiles) and 5.C (Classification Algorithm). Topics under spending forecasting (6.A,6.B) were rejected because the paper does not predict future spending; it only segments observed behavior. Anomaly detection (8.A,8.B) is mentioned only in background, not the core contribution. Expense categorization (3.A,3.B) is partially relevant via transaction types, but the paper's primary contribution is user segmentation, not category design. No coverage of privacy, retention, evaluation frameworks, or savings/debt management, so those topics were omitted."
limitations:
  - "The dataset is simulated and limited to one month, which may not generalize to real-world multi-year transaction histories. [unacknowledged]"
  - "Moderate Silhouette Score (0.33) indicates clusters are not well-separated, but the paper acknowledges this as a limitation."
  - "No validation with external criteria (e.g., user survey or downstream task performance) to confirm cluster utility."
  - "Only K-means was tested; other algorithms might yield better separation, but the paper acknowledges this as future work."
remember_this:
  - "K-means clustering achieved a Silhouette Score of 0.33."
  - "Cluster 1 had highest mean transaction amount at 4147.06."
  - "Transaction day of week distinguishes purchase from transfer behavior."
  - "Single-month dataset limits generalization to seasonal spending."
  - "Simulated data may not reflect real-world financial noise."
```