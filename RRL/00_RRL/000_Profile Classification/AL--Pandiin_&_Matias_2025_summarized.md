# Predictive Modeling for Loan Eligibility Assessment: A Comparative Study of Logistic Regression, Random Forest, and Support Vector Machine with Detailed Oversampling

## Metadata

```yaml
---
paper_id: "a3f4c5e6-7d8b-4c9a-8b2f-1e3d5c7b9a4b"
designation: algorithm-specific
title: "Predictive Modeling for Loan Eligibility Assessment: A Comparative Study of Logistic Regression, Random Forest, and Support Vector Machine with Detailed Oversampling"
authors: "Pandiin, J. D.; Matias, J. B."
year: 2025
venue: "AEIS"
odin_topics: ["5.C", "6.A", "12.B"]
shorthand_tags: ["/classifier-candidates", "/classifier-features", "/classifier-tradeoffs", "/classifier-eval-metrics", "/eval-ml-design", "/eval-limitations"]
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

Random Forest achieves **85% accuracy** and 0.94 AUC for loan eligibility prediction, outperforming Logistic Regression and SVM after Genetic Algorithm feature selection.

## Problem and Motivation

Many banks and lending companies still rely on manual approval processes or basic models, increasing financial risk from misclassified loan applicants. Loan defaults directly impact bank profits, yet existing studies lack systematic comparison of ensemble methods with advanced feature selection and class imbalance handling. No prior work had integrated Genetic Algorithm for feature selection with oversampling and a multi-classifier benchmark on a balanced loan dataset.

## Approach

- Dataset: Kaggle loan dataset (class imbalanced; oversampled minority class to create balanced set).
- Preprocessing: EDA, missing value handling, outlier treatment, resample oversampling for class balance.
- Feature selection methods: Correlation-based, RFE, SelectKBest, Lasso, plus Genetic Algorithm (GA) for optimization.
- Classifiers: Logistic Regression, Random Forest, Support Vector Machine (SVM).
- Evaluation: Accuracy, precision, recall, F1, AUC, 5-fold cross-validation.
- Deployment: Web application for real-time loan eligibility prediction.

## Findings

1. Random Forest achieved the highest balanced performance: **accuracy 85%**, precision 86%, recall 84%, F1 85%, AUC 0.94.
2. Cross-validation mean accuracy for Random Forest was 92% (range 0.87–0.94), confirming robustness.
3. Lasso feature selection boosted Random Forest to 88.48% accuracy; same method dropped SVM to 52.73%.
4. SVM had very high recall (99%) but low precision (63%), minimizing false negatives at cost of many false positives.
- Logistic Regression showed consistent but lower accuracy (67%) and poor ability to capture non-linear patterns.
- Feature importance: Credit History (26.8%), Applicant Income (19.7%), Loan Amount (19.2%); Gender and Education had minimal impact (<2.5%).

## Key Figures and Tables

- Figure 2: Distribution of loan status from imbalance to balance → oversampling equalized class counts for unbiased training.
- Table 1: Accuracy by feature selection method → Lasso + Random Forest gave 88.48% accuracy, highest among all combinations.
- Table 3: Comparative classifier matrix (accuracy, precision, recall, F1, AUC) → Random Forest leads all metrics except recall (SVM wins recall).
- Figure 6: ROC curves of three classifiers → Random Forest has AUC 0.94, Logistic Regression 0.73, SVM 0.69.
- Figure 7: Confusion matrices → Random Forest: low false positives (11) and false negatives (13); SVM: 47 false positives.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| GA | Genetic Algorithm — an optimization method that evolves feature subsets toward better predictive performance. |
| RFE | Recursive Feature Elimination — iteratively removes weakest features to find the best subset. |
| SVM | Support Vector Machine — a classifier that finds a hyperplane to separate classes; sensitive to feature scaling. |
| AUC | Area Under the ROC Curve — measures how well the model distinguishes between positive and negative classes (0.5 = random, 1.0 = perfect). |
| EDA | Exploratory Data Analysis — initial data inspection to find patterns, missing values, or outliers. |
| Oversampling | Increasing minority class instances by copying existing samples to balance class distribution. |

## Critical Citations

- [Chawla et al., 2002] — Foundational SMOTE oversampling technique; this study uses simpler resample method for balance.
- [Mehrabi et al., 2021] — Fairness and bias in ML; cited to justify balanced classifier evaluation for equitable loan decisions.
- [Karthiban et al., 2019] — Review of ML classification for bank loans; provides baseline for comparing this study's advanced methods.

## Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly informs Odin's choice of classifier for financial behavioral profiling by benchmarking Random Forest against Logistic Regression and SVM on a balanced financial dataset. The demonstration that Random Forest balances precision and recall (86% and 84%) while achieving high AUC (0.94) supports its selection over SVM (high recall but low precision, risking false profile assignments) for Odin's profiling module, where misclassification could erode user trust. Although the domain is loan eligibility rather than spending behavior, the methodological framework — feature selection via GA, oversampling for class balance, and multi-metric evaluation (accuracy, precision, recall, F1, AUC, cross-validation) — applies directly to Odin's algorithm evaluation under ISO 25010:2023.

**Directly justifies:**

- "Random Forest achieved 85% accuracy and 0.94 AUC on a balanced financial classification task, outperforming Logistic Regression (67%) and SVM (71%)."
- "Lasso-based feature selection combined with Random Forest raised accuracy to 88.48%, demonstrating that aggressive feature reduction benefits ensemble methods more than linear models or SVMs."
- "Credit history (26.8%), applicant income (19.7%), and loan amount (19.2%) dominated predictive importance, while demographic attributes (gender, education) contributed under 2.5% — a pattern that may generalize to financial behavior profiling."
- "5-fold cross-validation mean accuracy for Random Forest was 92%, confirming robust generalization beyond a single train-test split."

**Limits of relevance:**

- Loan eligibility prediction (binary approval/denial) differs from spending forecasting or multi-class behavioral profiling, so classifier performance may not translate directly.
- Dataset is from Kaggle (not Philippine-specific), and no Filipino demographic or cultural spending data was used.
- Oversampling via resample (not SMOTE) may cause overfitting; temporal patterns in transaction sequences are absent.
- No mobile-first or privacy constraints were considered; paper assumes batch processing on structured loan applications.

## Limitations

- The dataset is from Kaggle, not real-world bank data, limiting external validity to actual financial institutions. [unacknowledged]
- Oversampling with replacement may introduce overfitting; no comparison with SMOTE or other advanced balancing techniques.
- Hyperparameter tuning for classifiers is not described in depth; GA focused on feature selection, not model parameters. [unacknowledged]
- No evaluation of model explainability or fairness metrics beyond accuracy/precision/recall, despite citing fairness in ML.
- The study does not address temporal dynamics or sequential data, making it less applicable to recurring spending pattern detection.

## Remember This

- 🔑 **Random Forest: 85% accuracy, 0.94 AUC** — best balance of precision (86%) and recall (84%).
- 📌 **Credit history drives 26.8% of prediction** — income and loan amount add ~19% each; demographics barely matter (<2.5%).
- 💡 **Lasso + RF = 88.48% accuracy** — aggressive feature reduction helps ensembles, hurts SVM (dropped to 52.7%).
- ⚠️ **SVM recalls 99% but precision 63%** — great for avoiding false rejections, terrible for false approvals (financial risk).
