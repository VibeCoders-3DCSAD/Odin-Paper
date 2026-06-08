```yaml
paper_id: 10.1145/3698062.3698088
designation: algorithm-specific
title: Exploring Machine Learning for Credit Card Fraud Detection from a Philippine Perspective
authors: Blancaflor, E.; Asuncion, K. D.; Reyes, H. J.; Verzosa, M.
year: 2024
venue: 2024 The 6th World Symposium on Software Engineering (WSSE)
odin_topics:
  - 8.A
  - 8.B
  - 12.B
shorthand_tags:
  - /anomaly-detection
  - /ml-classification
  - /model-evaluation
tldr: Evaluates machine learning models (SVM, ANN, k-NN, Naive Bayes, logistic regression) for credit card fraud detection in the Philippines, finding ANN achieves up to 98.44% accuracy.
problem_and_motivation: Credit card fraud in the Philippines increased 21% since COVID-19, with traditional fraud prevention systems inadequate due to large data volumes, imbalanced distributions, concept drift, and real-time detection needs. There is a need to customize machine learning algorithms to the Philippine economic, technological, and social context to improve fraud detection effectiveness.
approach:
  - Data source: credit card transaction data from the Philippines (dataset size not specified).
  - Methods evaluated: logistic regression, k-Nearest Neighbors, Naive Bayes, Support Vector Machines, and Artificial Neural Networks with GA and SMOTE enhancements.
  - Evaluation metrics: accuracy, sensitivity, specificity, precision, Matthews Correlation Coefficient, and balanced classification rate.
  - Baseline comparisons among all models; ANN-SMOTE outperformed others.
findings:
  - "num: ANN-SMOTE achieved the best performance with up to 98.44% accuracy."
  - "num: k-NN achieved 97.69% accuracy and Naive Bayes 97.92% accuracy."
  - "num: Logistic regression had the lowest accuracy at 54.86%."
  - A trade-off exists between model accuracy and explainability; logistic regression is better for regulatory compliance.
  - Imbalanced data handling via SMOTE and hybrid sampling improves detection performance.
key_figures_tables:
  - "Figure 1: Compares ANN and LR with GA/SMOTE enhancements → ANN-SMOTE has highest precision, recall, and F1."
  - "Table 1: Lists model accuracies (54.86% to 98.44%) and improvement strategies → hybrid sampling and meta-learning are recommended."
key_equations:
  - equation: "MCC = (TP * TN - FP * FN) / sqrt((TP+FP)(TP+FN)(TN+FP)(TN+FN))"
    explanation: "Balanced measure for binary classification on imbalanced data."
  - equation: "f(x) = sgn(x \\cdot w) + b"
    explanation: "SVM decision function maximizing class separation margin."
definitions:
  - term: MCC
    definition: "Matthews Correlation Coefficient, a balanced metric for binary classification."
  - term: BCR
    definition: "Balanced Classification Rate, average of sensitivity and specificity."
  - term: Logistic Regression
    definition: "Statistical model for binary classification predicting event probability."
  - term: k-NN
    definition: "K-Nearest Neighbors, non-parametric classifier based on proximity."
  - term: Naive Bayes
    definition: "Probabilistic classifier assuming feature independence."
  - term: SVM
    definition: "Support Vector Machine, kernel-based classifier maximizing margin."
  - term: ANN
    definition: "Artificial Neural Network, deep learning model for pattern recognition."
  - term: SMOTE
    definition: "Synthetic Minority Over-sampling Technique for imbalanced data."
  - term: GA
    definition: "Genetic Algorithm, meta-heuristic for optimization."
  - term: FPS
    definition: "Fraud Prevention System, real-time security controls."
  - term: FDS
    definition: "Fraud Detection System, post-transaction anomaly detection."
critical_citations:
  - "[Awoyemi et al., 2017] — Comparative analysis of ML for credit card fraud."
  - "[Abdallah et al., 2016] — Survey of fraud detection system challenges."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      justification: "Credit card fraud detection is a canonical anomaly detection task in financial transaction data."
    - code: 8.B
      name: Anomaly Detection Algorithm
      justification: "Paper compares SVM, ANN, k-NN, Naive Bayes, and logistic regression for fraud identification."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: "Uses accuracy, precision, recall, MCC, and balanced accuracy to benchmark models on imbalanced data."
  contribution: "For Odin's anomaly detection module (8.B), this paper validates that ANN-SMOTE can effectively identify fraudulent transactions with 98.44% accuracy, supporting algorithm selection. The evaluation framework (12.B) metrics like MCC and balanced accuracy provide robust ways to assess detection performance on imbalanced data, directly informing Odin's testing strategy. The paper's emphasis on real-time detection and adaptive learning guides the design of a real-time anomaly detection subsystem that continuously updates from new transaction patterns."
  directly_justifies:
    - "ANN-SMOTE achieves 98.44% accuracy for fraud detection in the Philippine context."
    - "Logistic regression offers interpretability at the cost of lower accuracy (54.86%)."
    - "Imbalanced data handling via SMOTE improves detection performance."
    - "Real-time detection requires models that adapt to concept drift."
  limits:
    - "Dataset size and exact origin not specified, limiting reproducibility."
    - "Paper is a literature survey with synthetic examples rather than original experimentation."
    - "Philippine-specific data may not generalize to other countries."
  mapping_rationale: "The paper directly addresses anomaly detection (8.A) by framing credit card fraud as an anomaly in transaction streams. It compares multiple algorithms (8.B) including SVM, ANN, and k-NN, which are relevant to Odin's detection module. The evaluation methodology (12.B) using accuracy, MCC, and balanced accuracy on imbalanced data matches Odin's need for robust algorithmic assessment. Topics like behavioral profiling (5.A), spending forecasting (6.A), or budget recommendation (7.A) were rejected because the paper does not discuss user financial behavior or budgeting. Data privacy (10.A) and retention (11.A) are mentioned only peripherally."
limitations:
  - "No explicit dataset size or transaction volume provided. [unacknowledged]"
  - "All reported accuracies are from cited secondary sources, not original experiments. [unacknowledged]"
  - "Real-time detection challenges mentioned but no latency or throughput benchmarks given."
remember_this:
  - "ANN-SMOTE achieves 98.44% accuracy for fraud detection."
  - "Imbalanced data handling is critical for anomaly detection."
  - "Explainability trade-off matters for regulatory compliance."
  - "Real-time detection requires adaptive learning against concept drift."
```