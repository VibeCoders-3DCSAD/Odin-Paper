```yaml
paper_id: c7b3a1d9-6e5f-4c2a-8b9d-1f3e5a7c9d2b
designation: local
title: Predictive Modeling for Loan Eligibility Assessment: A Comparative Study of Logistic Regression, Random Forest, and Support Vector Machine with Detailed Oversampling
authors: Pandiin, J. D.; Matias, J. B.
year: 2025
venue: AEIS
odin_topics:
  - 12.A
  - 12.B
shorthand_tags:
  - /evaluation-frameworks
  - /algorithm-evaluation
tldr: Compares Logistic Regression, Random Forest, and SVM for loan eligibility prediction using oversampling and genetic algorithm feature selection, finding Random Forest most balanced with 85% accuracy.
problem_and_motivation: Manual loan approval processes are inefficient and prone to error. Existing machine learning approaches lack robust feature selection and class imbalance handling. A comparative evaluation of optimized classifiers is needed for fair and accurate loan decisions.
approach:
  - Data from Kaggle loan dataset with binary target variable Loan_Status.
  - Oversampling applied to minority class to address imbalance.
  - Feature selection using Correlation, RFE, SelectKBest, Lasso, and Genetic Algorithm optimization.
  - Classifiers: Logistic Regression, Random Forest, SVM with default kernels.
  - Evaluation using accuracy, precision, recall, F1-score, AUC, and 5-fold cross-validation.
findings:
  - Random Forest achieved highest accuracy (85%), precision (86%), recall (84%), F1-score (85%) with Lasso feature selection.
  - num: Random Forest cross-validation mean accuracy 92%.
  - num: Credit History most important feature (26.8%), followed by Applicant Income (19.7%) and Loan Amount (19.2%).
  - SVM achieved 99% recall but low precision (63%), indicating many false positives.
  - Logistic Regression underperformed with 67% accuracy and struggled with non-linear relationships.
key_figures_tables:
  - Figure 2: Distribution of loan status before and after oversampling → Oversampling balanced classes.
  - Table 1: Accuracy results for feature selection methods → Random Forest with Lasso achieved 88.5% accuracy.
  - Figure 5: Performance matrix of three classifiers → Random Forest shows best balance.
  - Figure 6: ROC curves → Random Forest AUC 0.94, highest discriminative ability.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: GA
    definition: Genetic Algorithm, used for optimizing feature subsets.
  - term: SVM
    definition: Support Vector Machine, a classifier for high-dimensional spaces.
  - term: RFE
    definition: Recursive Feature Elimination, iteratively removes least important features.
  - term: AUC
    definition: Area Under the ROC Curve, measures discriminative ability.
  - term: Oversampling
    definition: Resampling minority class to balance dataset.
critical_citations:
  - "[Chawla et al., 2002] — SMOTE oversampling foundation."
  - "[Mehrabi et al., 2021] — fairness in ML cited for ethical decisions."
relevance:
  topics:
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      justification: Provides comparative evaluation metrics and cross-validation for ML classifiers.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: Benchmarks Random Forest, SVM, Logistic Regression for loan prediction task.
  contribution: Odin can adopt the comparative evaluation methodology for its spending forecasting and anomaly detection modules. The use of genetic algorithm for feature selection improves model interpretability, which is valuable for user trust. The finding that Random Forest balances precision and recall informs algorithm selection for risk-sensitive PFMS features. The oversampling technique addresses class imbalance, applicable to rare event detection in user financial data.
  directly_justifies:
    - Random Forest achieves 85% accuracy and balanced precision-recall, suitable for fair loan decision support.
    - Genetic algorithm feature selection identifies most relevant features, reducing model complexity.
    - Credit history and income are top predictors, suggesting PFMS should prioritize these for risk assessment.
  limits:
    - Dataset from Kaggle may not represent Filipino young professionals specifically.
    - Oversampling may introduce synthetic bias not acknowledged.
    - No fairness-aware evaluation across demographic groups [unacknowledged].
  mapping_rationale: The paper focuses on comparative ML evaluation for loan eligibility, which maps to Odin's system evaluation domains (12.A, 12.B). It provides metrics and cross-validation methods relevant for assessing algorithmic modules like spending forecasting or anomaly detection. Topics related to behavioral profiling (5.A-C) were rejected because the paper does not profile user financial behavior but rather predicts binary approval. Budget recommendation (7.A-C) and spending forecasting (6.A-B) are not addressed. Debt management (13.B) is tangential as loan approval is not debt management strategy. Overall, the methodological contributions to model evaluation justify inclusion of 12.A and 12.B.
limitations:
  - Only one dataset from Kaggle, limiting generalizability.
  - No comparison with deep learning methods.
  - Feature selection via GA may overfit to training data [unacknowledged].
remember_this:
  - Random Forest with Lasso feature selection achieved 88.5% accuracy.
  - Credit history is the most important predictor at 26.8%.
  - SVM has near-perfect recall but high false positives.
  - Cross-validation confirmed Random Forest robustness with 92% mean accuracy.
```