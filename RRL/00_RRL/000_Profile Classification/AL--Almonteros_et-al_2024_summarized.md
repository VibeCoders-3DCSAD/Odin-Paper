# Forecasting Students’ Success To Graduate Using Predictive Analytics

## Metadata

```yaml
---
paper_id: "10.12785/ijcds/150151"
designation: algorithm-specific
title: "Forecasting Students’ Success To Graduate Using Predictive Analytics"
authors: "Almonteros, J. R.; Matias, J. B.; Pitao, J. V. S."
year: 2024
venue: "International Journal of Computing and Digital Systems"
odin_topics: []
shorthand_tags: []
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

Genetic Algorithm feature selection with Logistic Regression achieved 79% accuracy and 71% AUC, outperforming LASSO and Ridge for predicting on-time college graduation.

## Problem and Motivation

Predicting whether a student will graduate on time is difficult because admission test scores alone are weak predictors. Early identification of at-risk students allows universities to provide targeted interventions and improve graduation rates. Prior work did not compare feature selection methods (LASSO, Ridge, Genetic Algorithm) combined with multiple classifiers on Philippine K-12 graduate data.

## Approach

- Dataset: 2,207 new entrant records from Caraga State University (2018–2022) with 24 features (demographics, prior academics, admission exam scores).
- Missing data handled via KNN imputation (numerical) and mode imputation (categorical). Binary encoding applied to nominal features, expanding to 64 predictors.
- Three feature selection methods applied separately: LASSO (L1), Ridge (L2), and Genetic Algorithm (GA) with 150 iterations.
- Seven classifiers tested: Decision Tree, Random Forest, Ensemble (bagging with J48), KNN, Logistic Regression, SVM, Naïve Bayes.
- Evaluation metrics: accuracy, error rate, precision, recall, AUC. Train/test split 70/30.
- Best model (Logistic Regression + GA) deployed as a Django web app with bulk and single-prediction interfaces.

## Findings

1. No Feature Selection (NFS) achieved **78% accuracy** (Random Forest) and 67% AUC.
2. LASSO (L1) selected only 5 features and performed worst (58% accuracy, 50% AUC with Decision Tree).
3. Ridge (L2) selected 15 features, achieving 77% accuracy (SVM) and 66% AUC.
4. Genetic Algorithm (GA) selected 33 features on average across classifiers and improved all metrics.
5. **Logistic Regression with GA achieved 79% accuracy and 71% AUC** — the highest in the study, a 21% AUC gain over NFS with the same classifier.
- Admission exam score was the most frequently selected feature (6/9 times), followed by mother income, English score, math score, and sex.
- Abstract score and father income were selected least often.

## Key Figures and Tables

- Table V: Evaluation metric scores for all classifiers across NFS, L1, L2, GA → GA+Logistic Regression highest at 79% accuracy, 71% AUC.
- Table VI: Feature selection matrix for L1, L2, and seven GA classifiers → admission exam selected in 6 of 9 runs; abstract score in only 2.
- Figure 2: Bar chart of feature selection frequency → admission exam, sex, mother income, English, math as top predictors.
- Figure 3: Bulk prediction interface → upload CSV, get per-student intervention flag.
- Figure 6 & 7: Pop-up prediction results → “Can Graduate on Time” (green) vs “Needs Intervention” (red).

## Key Equations

None. The paper uses standard classification metrics (accuracy, recall, precision) without introducing novel equations.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| AUC | Area Under the ROC curve — measures how well a model separates positive from negative classes; 0.5 = random, 1.0 = perfect. |
| Binary encoding | Converting categorical values (e.g., red/green/blue) into binary columns to avoid false rank ordering. |
| Genetic Algorithm (GA) | An optimization method that evolves a population of feature subsets through selection, crossover, and mutation to find the best set. |
| KNN imputation | Fills missing numerical values using the average of the k most similar data points (nearest neighbors). |
| LASSO (L1) | A regression method that forces some feature coefficients to exactly zero, performing feature selection. |
| Ridge (L2) | A regression method that shrinks all coefficients toward zero but keeps all features. |
| Mode imputation | Fills missing categorical values with the most frequent category in that column. |

## Critical Citations

- [Kumar & Garg, 2018] — Defines the seven-phase predictive analytics process (requirement collection to monitoring) used as the study's methodological framework.
- [Lumboy, 2019] — Establishes that SHS track misalignment affects college performance, justifying inclusion of SHS track as a predictor.
- [Chingos, 2018] — Shows high school GPA and admission test scores together predict college readiness better than either alone.
- [Alyahyan & Düştegör, 2020] — Literature review confirming prior academic achievement (44% of studies) and demographics (25%) as top predictors of student success.

## Relevance to Odin

**Topics:**

None — contextual only.

**Contribution to Odin:**

This paper does not address personal finance systems, Filipino financial behavior, or any of Odin's functional domains (spending forecasting, budget recommendation, anomaly detection, etc.). Its educational context and student success prediction task are not applicable to budget management or spending behavior. Therefore, it offers no direct justification for Odin's design decisions.

**Directly justifies:**

None.

**Limits of relevance:**

- Domain mismatch: student graduation prediction vs. personal spending and budgeting.
- Target variable (on-time graduation) has no parallel in Odin's classification or forecasting tasks.
- Dataset characteristics (academic records, admission scores) share no features with financial transaction histories.
- Evaluation metrics (accuracy, AUC) are general, but the specific results do not transfer to financial behavior modeling.

## Limitations

- No external validation on other universities or cohorts — results may not generalize beyond Caraga State University.
- High missingness in SHS track (1702 missing) and GPA (593 missing) — imputation may introduce bias [unacknowledged].
- Binary classification only (graduate on time vs. not) — does not predict degree of delay or academic performance.
- Feature set excludes psychosocial factors (motivation, peer influence, internet access) that prior work shows affect student success [unacknowledged].
- Web app requires preprocessed CSV inputs; real-time prediction for individual students uses manual form entry, limiting practical deployment scale.

## Remember This

- 📌 GA + Logistic Regression hit **79% accuracy** — best among 7 classifiers and 3 feature selectors.
- 🔍 Admission exam score was selected 6/9 times — strongest single predictor in this dataset.
- ⚠️ LASSO (L1) collapsed to 5 features and dropped to 58% accuracy — aggressive selection hurts performance here.
- 🧠 English and math scores outperformed abstract score — subject-specific skills matter more than general ability.
- 💡 Domain is education, not finance — no direct application to Odin's budgeting or spending modules.
