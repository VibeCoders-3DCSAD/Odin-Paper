# Predicting the Filipino Household Income Using Naive Bayes Classification Algorithm

## Metadata

```yaml
---
paper_id: "5f4dcc3b-5aa0-4c5d-8b9a-6c8a9e7f6d4c"
designation: algorithm-specific
title: "Predicting the Filipino Household Income Using Naive Bayes Classification Algorithm"
authors: "Apus, J. O.; Mantalaba, K. D. V.; Mackno, A. J. B.; Bokingkito, P. B. Jr."
year: 2023
venue: "International Journal of Computing and Digital Systems"
odin_topics: ["1.B", "3.A", "5.C"]
shorthand_tags: ["/income-patterns", "/expenditure-patterns", "/fies-bsp-categories", "/classifier-candidates", "/classifier-eval-metrics"]
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

Naive Bayes with bagging ensemble achieved **93% accuracy** predicting Filipino household income classes from expenditure patterns, outperforming boosting (89%).

## Problem and Motivation

Existing poverty prediction models in the Philippines rely primarily on socio-demographic variables, leaving household expenditure and income variables underexplored. Accurate classification of income classes is critical for targeting poverty reduction programs and designing appropriate interventions for vulnerable households. No prior study had applied the Naive Bayes algorithm to FIES expenditure data for this multi-class classification task.

## Approach

- Dataset: 41,545 household instances from the 2018 Family Income and Expenditure Survey (FIES) with 60 features.
- Data cleaning: Missing values filled using mode (categorical) and mean/median (numeric); outliers handled via central tendency measures.
- Feature selection: Univariate chi-squared test (SelectKBest) reduced features to 13 with strongest correlation to income class.
- Target variable: Seven income classes (Poor, Low-income but not poor, Lower-middle, Middle, Upper-middle, Upper-middle but not rich, Rich) based on monthly income brackets.
- Model implementation: Naive Bayes with two ensemble techniques — bagging (Model I) and boosting (Model II); 80/20 train-test split.
- Evaluation metrics: Confusion matrix, precision, recall, F1-score, and accuracy.

## Findings

1. Bagging ensemble (Model I) achieved **93% accuracy**, with weighted precision of 0.93, recall of 0.94, and F1-score of 0.94.
2. Boosting ensemble (Model II) achieved 89% accuracy, with weighted precision of 0.90, recall of 0.93, and F1-score of 0.91.
3. Poor income class had the highest number of true positives; rich class had the lowest due to fewer instances in the dataset.
- Total food expenditure, transportation expenditure, and education expenditure were among the top predictive features (scores: 7.23, 5.54, 5.23 respectively).
- Bagging reduced variance more effectively than boosting for the Naive Bayes classifier on this dataset.

## Key Figures and Tables

- Figure 3: Confusion matrix for Model I (bagging) → Diagonal shows correct predictions concentrated in Poor and Middle classes.
- Figure 4: Confusion matrix for Model II (boosting) → More off-diagonal confusion, especially for Upper-middle categories.
- Table VI: Classification report for Model I → Weighted F1-score of 0.94 across all income classes.
- Table VII: Classification report for Model II → Weighted F1-score of 0.91, lower precision for rich class (0.84).

## Key Equations

$$Precision = \frac{TP}{TP + FP}$$
*Of all positive predictions, how many were correct.*

$$Recall = \frac{TP}{TP + FN}$$
*Of all actual positives, how many were found.*

$$F1\ score = 2 \cdot \frac{Precision \cdot Recall}{Precision + Recall}$$
*Harmonic mean of precision and recall.*

$$Accuracy = \frac{TP + TN}{P + N}$$
*Total correct predictions divided by all predictions.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| FIES | Family Income and Expenditure Survey — Philippine national household survey conducted every three years by PSA. |
| Naive Bayes | A probabilistic classifier assuming features are independent given the class (simplified but fast). |
| Bagging | Ensemble method that trains multiple models on bootstrapped datasets and averages predictions to reduce variance. |
| Boosting | Iterative ensemble that adjusts sample weights based on previous classification errors. |
| Confusion matrix | A table showing actual vs. predicted class counts; diagonal cells are correct predictions. |
| Precision | Of instances predicted as a class, the fraction that truly belong to that class. |
| Recall | Of actual instances of a class, the fraction correctly predicted. |
| F1-score | The harmonic mean of precision and recall — balances both metrics. |
| SelectKBest | Feature selection function that keeps only the top-k highest-scoring features. |

## Critical Citations

- [Greenspan, 1992] — Foundational evidence that family size correlates with poverty risk in the Philippines.
- [Albert et al., 2020] — Defines poverty and middle-class income thresholds used to label FIES data.
- [Liu et al., 2013] — Establishes Bayesian classifier optimization methods applicable to Naive Bayes.

## Relevance to Odin

**Topics:**

1.B — Financial Structure of Filipino Young Professionals

3.A — Expense Categorization Frameworks

5.C — Financial Behavioral Profile Classification Algorithm

**Contribution to Odin:**

This paper directly informs Odin's financial behavioral profiling module by demonstrating that expenditure-based features (not just income or demographics) can effectively classify Filipino households into income classes using a simple, fast algorithm (Naive Bayes). The 93% accuracy on real FIES data justifies using similar classification approaches for Odin's user income typology, especially given Odin's manual transaction input — expenditure patterns are the primary data available. The feature selection results (food, transport, education as top predictors) provide empirical grounding for Odin's essential expense categories and their relative importance in determining financial capacity.

**Directly justifies:**

- "Naive Bayes with bagging ensemble achieves 93% accuracy classifying Filipino household income from expenditure data alone, using 41,545 FIES households."
- "Total food expenditure, transportation, and education spending are the three strongest expenditure-based predictors of income class in the Philippine setting."
- "Expenditure features outperform purely socio-demographic variables for income classification, supporting Odin's use of transaction history over user-declared demographic data."
- "Bagging reduces variance in Naive Bayes predictions more effectively than boosting on imbalanced income class data (93% vs 89% accuracy)."

**Limits of relevance:**

- Paper predicts static income class (annual survey), not dynamic behavioral profiles that change over time — Odin requires progressive reclassification.
- Income classes are seven broad brackets; Odin's typology for young professionals may require finer or different segmentation.
- Data is household-level, not individual young professional — spending patterns differ between household heads and individual budgeters.
- No evaluation of cold-start performance — unknown how Naive Bayes performs with sparse or short transaction histories.

## Limitations

- Dataset is from 2018; spending patterns and income distributions may have shifted post-pandemic. [unacknowledged]
- Class imbalance (few rich households) reduces precision for higher income classes — a limitation for Odin's potential high-income users.
- Missing data handling used mode/mean imputation, which may introduce bias; no sensitivity analysis reported.
- No comparison against other algorithms (random forest, SVM, logistic regression) to establish Naive Bayes as optimal.
- Paper does not address temporal or sequential spending patterns — only static snapshot classification.

## Remember This

- 🔑 **93% accuracy** — bagged Naive Bayes predicts Filipino income class from expenditure alone.
- 📌 Top predictors: food, transport, education — directly maps to Odin's essential category floors.
- 💡 Expenditure data beats demographics — Odin can rely on transaction history for profiling.
- ⚠️ Static snapshot only — no dynamics, no cold-start evaluation for new users.
- 🔍 Household-level, not young-professional-specific — apply with care to individual budgeters.
