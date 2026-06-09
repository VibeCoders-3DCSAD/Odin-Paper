```yaml
paper_id: 10.3390/app15211787
designation: international
title: An Introduction to Machine Learning Methods for Fraud Detection
authors: Compagnino, A. A.; Maruccia, Y.; Cavuoti, S.; Riccio, G.; Tutone, A.; Crupi, R.; Pagliaro, A.
year: 2025
venue: Applied Sciences
odin_topics:
  - 8.A
  - 8.B
  - 12.A
  - 12.B
  - 10.A
  - 10.B
shorthand_tags:
  - /anomaly-detection
  - /anomaly-detection-algorithm
  - /evaluation-frameworks
  - /algorithm-evaluation
  - /data-privacy
  - /user-trust
tldr: Reviews machine learning for financial fraud detection, covering supervised, unsupervised, and deep learning approaches, datasets, performance metrics, and case studies highlighting class imbalance and recall challenges.
problem_and_motivation: Financial fraud causes severe economic and social damage, with 56% of companies experiencing fraud. Traditional detection methods are increasingly inadequate against evolving fraudulent activities. A systematic analysis of ML techniques bridging academic research and operational reality is missing.
approach:
  - Systematic literature search across Scopus, IEEE Xplore, ACM Digital Library, and Web of Science for articles published 2014-2023.
  - Classification of fraud types into external (credit card, loan, insurance) and internal (financial statement, money laundering, tax, asset misappropriation).
  - Review of supervised methods (Random Forest, XGBoost, SVM, etc.), unsupervised methods (Isolation Forest, Autoencoders, K-Means), and deep learning (LSTM, CNN, RNN, GAN).
  - Analysis of datasets (ULB credit card, CSMAR, PaySim, etc.) and evaluation metrics (precision, recall, F1, AUPRC, silhouette coefficient).
  - Two case studies on proprietary banking data applying Random Forest and XGBoost with class_weight tuning and temporal validation.
findings:
  - "num: Random Forest achieved AUPRC of 0.619 on banking test set (prevalence 2.37%) but fraud recall was only 0.34."
  - "num: XGBoost on ULB2013 dataset achieved AUPRC of 0.867, outperforming Logistic Regression (0.724) and KNN (0.585)."
  - "num: Class_weight='balanced' and 'balanced_subsample' did not improve recall (stuck at 0.36) compared to default on bank transfer dataset."
  - "num: Recall@0.5% for Random Forest was 0.202, capturing about 24 of 119 frauds when screening top 0.5% of transactions."
  - Supervised learning accounts for 57% of techniques in reviewed literature, Random Forest appears in 34 studies.
key_figures_tables:
  - "Table 1: Comparative analysis of ML algorithms (RF, LR, XGBoost, Isolation Forest, Autoencoders, LSTM) → trade-offs between complexity, interpretability, and imbalance handling."
  - "Table 4: Case study 1 results on banking data (N=5000, prevalence 2.37%) → Random Forest best AUPRC 0.6188, fraud recall only 0.34."
  - "Figure 1: Precision-recall curve for Random Forest → AUPRC 0.619, illustrating difficulty of achieving high recall at high precision."
  - "Table 5: Case study 2 results with class_weight settings → none improved recall beyond 0.36 despite AUPRC ~0.70."
key_equations:
  - equation: "Precision = TP / (TP + FP)"
    explanation: "Proportion of flagged transactions that are truly fraudulent."
  - equation: "Recall = TP / (TP + FN)"
    explanation: "Proportion of actual frauds correctly detected."
  - equation: "F1 = 2 * (Precision * Recall) / (Precision + Recall)"
    explanation: "Harmonic mean balancing precision and recall."
  - equation: "AUPRC = ∫_0^1 Precision(Recall) d(Recall)"
    explanation: "Area under precision-recall curve for imbalanced data."
definitions:
  - term: AUPRC
    definition: Area under the precision-recall curve, preferred over ROC for imbalanced classification.
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network for sequential data.
  - term: XAI
    definition: Explainable artificial intelligence, methods like SHAP and LIME for model transparency.
  - term: SMOTE
    definition: Synthetic Minority Over-sampling Technique for balancing imbalanced datasets.
  - term: Concept drift
    definition: Change in data distribution over time, degrading model performance.
critical_citations:
  - "[Dal Pozzolo et al., 2022] — Practitioner perspective on credit card fraud detection challenges."
  - "[Saito & Rehmsmeier, 2015] — Precision-recall plot more informative than ROC for imbalanced data."
  - "[López-Rojas, 2017] — Synthetic datasets (PaySim, BankSim) for fraud detection research."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      justification: "Reviews anomaly detection methods (Isolation Forest, Autoencoders, LOF) for financial fraud."
    - code: 8.B
      name: Anomaly Detection Algorithm
      justification: "Compares supervised, unsupervised, and deep learning algorithms with benchmark AUPRC results."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      justification: "Provides comprehensive metrics (precision, recall, F1, AUPRC, silhouette coefficient) and validation protocols."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: "Case studies demonstrate temporal validation, cost-sensitive thresholding, and top-K screening."
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      justification: "Discusses privacy-preserving federated learning and synthetic data generation for fraud detection."
    - code: 10.B
      name: User Trust in Personal Finance Systems
      justification: "Highlights need for explainable AI (SHAP, LIME) and fairness/bias mitigation to maintain user trust."
  contribution: "This paper justifies selection of anomaly detection algorithms (8.B) by benchmarking Random Forest, XGBoost, and deep learning models on real banking data. It provides an evaluation framework (12.A) for imbalanced classification using AUPRC and Recall@K metrics. The case studies demonstrate that standard supervised models fail to achieve adequate recall, motivating hybrid architectures (anomaly detection + classification) for Odin's spending anomaly module. Privacy-preserving techniques like federated learning (10.A) are identified as enablers for collaborative model training without exposing user data."
  directly_justifies:
    - "Fraudulent transactions typically constitute less than 1% of all transactions, making class imbalance a fundamental challenge."
    - "Accuracy is misleading for imbalanced data; AUPRC is the preferred metric for comparing anomaly detectors."
    - "Even with class_weight adjustments, Random Forest recall on fraud class was only 0.34 in a real banking dataset."
    - "Explainable AI (SHAP, LIME) is required for regulatory compliance and user trust in automated financial decisions."
  limits:
    - "Review focuses on financial fraud detection broadly, not specifically on personal finance management for young professionals."
    - "Case studies use proprietary banking data, limiting reproducibility of exact numerical results."
    - "Deep learning methods (LSTM, GANs) are discussed but not empirically evaluated in the case studies."
  mapping_rationale: "The paper strongly aligns with Anomaly Detection (8.A, 8.B) as its core subject is identifying fraudulent transactions, a canonical anomaly detection task. Evaluation frameworks (12.A, 12.B) are directly addressed through detailed metrics and validation protocols. Data privacy (10.A) appears in discussions of federated learning and synthetic data. User trust (10.B) is justified by sections on explainable AI and algorithmic bias. Topics related to Filipino demographics, spending forecasting, budgeting, expense categorization, mobile design, retention, and savings/debt were rejected because the paper contains no citeable claims about those domains."
limitations:
  - "The review does not propose a novel algorithm or system, only synthesizes existing literature."
  - "Case studies use tree-based ensembles only; deep learning and hybrid methods were not empirically tested. [unacknowledged]"
  - "The low recall achieved (0.34-0.36) suggests standard supervised models are insufficient, but the paper does not implement or evaluate the recommended hybrid solutions."
  - "All experiments use proprietary data, making exact replication impossible for independent researchers."
remember_this:
  - "Random Forest achieved AUPRC 0.619 but fraud recall only 0.34 on real banking data."
  - "Class_weight adjustments did not improve recall beyond 0.36 in imbalanced fraud detection."
  - "AUPRC is preferred over ROC for evaluating models on imbalanced datasets."
  - "Explainable AI (SHAP, LIME) is required for regulatory compliance in automated finance."
```