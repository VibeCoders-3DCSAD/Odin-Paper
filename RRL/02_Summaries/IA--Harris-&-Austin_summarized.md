```yaml
paper_id: b7c9a6d2-5e3f-4a1b-8c7d-9e2f3a4b5c6d
designation: international
title: Comparative Study of Supervised and Unsupervised Machine Learning Approaches in Banking Applications
authors: Harris, F.; Austin, V.
year: 0
venue: Unknown
odin_topics:
  - 8.A
  - 8.B
shorthand_tags:
  - /anomaly-detection-framework
  - /anomaly-detection-algorithm
tldr: Supervised learning achieves high accuracy for credit scoring and fraud detection using labeled data, while unsupervised learning excels at anomaly detection and customer segmentation without labels.
problem_and_motivation: Banking institutions need to leverage machine learning on vast datasets but face choices between supervised and unsupervised approaches. Each approach has distinct strengths and limitations for tasks like fraud detection and customer segmentation. A systematic comparison is missing to guide practitioners on optimal selection based on data availability and objectives.
approach:
  - Conducts a literature-based comparative analysis of supervised and unsupervised machine learning in banking.
  - Examines supervised algorithms: regression, decision trees, SVMs, and neural networks for labeled data tasks.
  - Examines unsupervised algorithms: clustering (k-means, hierarchical) and dimensionality reduction (PCA) for unlabeled data.
  - Evaluates applications: credit scoring, fraud detection, customer segmentation, anomaly detection, and market basket analysis.
  - Discusses hybrid models combining both approaches for enhanced performance.
findings:
  - Supervised learning provides higher predictive accuracy when labeled data is sufficient.
  - Unsupervised learning enables discovery of hidden patterns without labeling costs.
  - Hybrid models that use unsupervised for feature extraction then supervised for prediction improve overall performance.
  - Credit scoring and fraud detection are best served by supervised learning.
  - Anomaly detection and customer segmentation are best served by unsupervised learning.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: ML
    definition: Machine learning, a subset of AI enabling systems to learn from data.
  - term: AI
    definition: Artificial intelligence, the broader field of simulating human intelligence in machines.
  - term: PCA
    definition: Principal Component Analysis, a dimensionality reduction technique.
  - term: SVM
    definition: Support Vector Machine, a supervised classification algorithm.
critical_citations:
  - "[Arora & Kaur, 2019] — comparison for fraud detection."
  - "[Carcillo et al., 2019] — hybrid model for fraud detection."
  - "[Lessmann et al., 2015] — benchmarking credit scoring algorithms."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      justification: Paper discusses unsupervised learning for anomaly detection in banking transactions.
    - code: 8.B
      name: Anomaly Detection Algorithm
      justification: Paper compares clustering and isolation forest techniques for anomaly detection.
  contribution: "Odin's anomaly detection module can implement unsupervised clustering (k-means, hierarchical) to identify unusual spending patterns without labeled fraud data. Supervised learning can complement this by training on historical flagged anomalies for higher precision. The paper's comparison of evaluation metrics (silhouette score for unsupervised, F1 for supervised) directly informs Odin's module testing strategy."
  directly_justifies:
    - Unsupervised learning effectively detects anomalies in transaction data without requiring labeled examples.
    - Supervised learning achieves high accuracy for fraud detection when labeled historical data is available.
    - Hybrid models that combine unsupervised feature extraction with supervised classification improve detection performance.
  limits:
    - The paper does not address real-time anomaly detection constraints in mobile PFMS.
    - The findings are based on general banking data, not specifically on Filipino young professionals' spending patterns.
  mapping_rationale: "The paper primarily addresses anomaly detection and fraud detection in banking. Odin's functional domain for anomaly detection (8.A and 8.B) directly aligns with the paper's discussion of unsupervised learning for identifying unusual transactions and supervised learning for fraud classification. Topics related to spending forecasting, budget recommendation, and expense categorization are not covered. Borderline topics like evaluation frameworks (12.A) were rejected because the paper's comparative metrics are generic and not tailored to personal finance systems."
limitations:
  - The paper is a conceptual comparison without empirical validation on real banking datasets. [unacknowledged]
  - It does not address class imbalance issues in fraud detection datasets, though referenced works do. [unacknowledged]
  - The interpretability trade-offs between supervised and unsupervised models are discussed but not quantified.
remember_this:
  - Supervised learning needs labeled data but gives high accuracy.
  - Unsupervised learning finds hidden patterns without labels.
  - Hybrid models combine strengths of both approaches.
  - Choose method based on data availability and task goal.
```