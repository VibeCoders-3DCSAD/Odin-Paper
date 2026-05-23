# Use of Boosting Algorithms in Household-Level Poverty Measurement: A Machine Learning Approach to Predict and Classify Household Wealth Quintiles in the Philippines

## Metadata

```yaml
---
paper_id: "6ba7b810-9dad-11d1-80b4-00c04fd430c8" # UUID v5 generated from title
designation: algorithm-specific
title: "Use of Boosting Algorithms in Household-Level Poverty Measurement: A Machine Learning Approach to Predict and Classify Household Wealth Quintiles in the Philippines"
authors: "Salvador, E. L. V."
year: 2024
venue: "Preprint"
odin_topics: ["5.C", "12.B"]
shorthand_tags: ["/classification-vs-clustering", "/classifier-candidates", "/classifier-eval-metrics", "/eval-ml-design", "/eval-limitations"]
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

CatBoost achieved **90.93% accuracy** across five wealth quintiles on 20,679 Philippine households, outperforming XGBoost (89.41%), GBM (89.05%), LightGBM (88.52%), and AdaBoost (80.39%).

## Problem and Motivation

Conventional poverty measurements oversimplify multidimensional welfare by relying on pre‑selected features like income, ignoring non‑monetary indicators such as health and education. Accurate poverty classification is critical for targeting policy interventions, but econometric models miss complex data interactions. No prior study compared multiple boosting algorithms on a large‑scale Philippine household dataset with hundreds of features.

## Approach

- Dataset: 2022 Philippine Demographic and Health Survey (DHS), 30,372 households → after cleaning: 20,679 households, 396 features.
- Target: 5‑class wealth quintile (Poorest, Poorer, Middle, Richer, Richest).
- Models: AdaBoost, CatBoost, GBM, LightGBM, XGBoost — hyperparameter tuning via grid search + manual trial.
- Class imbalance handled with SMOTE (Synthetic Minority Over‑sampling Technique) on training data.
- Feature selection: SelectFromModel() across all models, retaining 36 features with minimal multicollinearity (Pearson < 0.8).
- Evaluation metrics: accuracy, precision, recall, F1, AUC‑ROC, plus training/testing time and model size.

## Findings

1. CatBoost achieved **90.93% accuracy** — highest among all models, followed by XGBoost (89.41%), GBM (89.05%), LightGBM (88.52%), and AdaBoost (80.39%).
2. Precision, recall, and F1‑scores followed the same ranking: CatBoost ≈ 90.9%, XGBoost ≈ 89.4%, GBM ≈ 89.0%, LightGBM ≈ 88.5%, AdaBoost ≈ 80–83%.
3. AUC‑ROC for CatBoost/GBM/LightGBM/XGBoost exceeded 0.98 across all quintiles; AdaBoost scored as low as 0.73 for the “Poorer” class.
- Top predictive features (from Table 1): source of drinking water, toilet type, television, refrigerator, bicycle, motorcycle, car, floor/wall/roof materials, and 4Ps beneficiary status.
- Computational trade‑offs: AdaBoost trained fastest (4.48s) but tested slowest (0.23s); CatBoost trained slowest (69.29s) with largest model (30.5 MB) but fastest testing (0.01s); LightGBM and XGBoost balanced speed and size well.

## Key Figures and Tables

- Figure 1 (missing values distribution): Threshold 3,050 removed features with excessive missing data → final 396 features.
- Table 1: 36 selected features (drinking water, toilet, appliances, housing materials, 4Ps, etc.) → top asset‑based poverty indicators.
- Table 3: Performance metrics (accuracy, precision, recall, F1) for all five models → CatBoost leads in all.
- Table 4: AUC‑ROC per wealth class → CatBoost/GBM/LightGBM/XGBoost near 1.0; AdaBoost lags.
- Table 5: Computational efficacy (training/testing time, model size) → LightGBM and XGBoost offer best practical balance.

## Key Equations

$$Accuracy = \frac{TP + TN}{TP + TN + FP + FN}$$
*Correct predictions divided by all predictions.*

$$Precision = \frac{TP}{TP + FP}$$
*Of predicted positives, how many were actually positive.*

$$Recall = \frac{TP}{TP + FN}$$
*Of actual positives, how many were correctly identified.*

$$F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}$$
*Harmonic mean of precision and recall.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| AdaBoost | Adaptive Boosting — iteratively reweights misclassified samples to improve a weak learner. |
| CatBoost | Categorical Boosting — handles categorical features natively; uses symmetric trees for speed. |
| GBM | Gradient Boosting Machine — builds trees sequentially, each correcting previous errors via gradients. |
| LightGBM | Light Gradient Boosting Machine — uses leaf‑wise tree growth for faster training on large data. |
| XGBoost | Extreme Gradient Boosting — regularized gradient boosting with tree pruning and parallelization. |
| SMOTE | Synthetic Minority Over‑sampling Technique — creates synthetic samples for minority classes to fix imbalance. |
| AUC‑ROC | Area Under the Receiver Operating Characteristic curve — probability that a model ranks a random positive higher than a random negative (1.0 = perfect). |
| DHS | Demographic and Health Survey — national household survey with health and wealth indicators. |
| 4Ps | Pantawid Pamilyang Pilipino Program — Philippine conditional cash transfer program. |

## Critical Citations

- [Bentéjac et al., 2021] — Comparative analysis of gradient boosting algorithms, establishing the expanded family of boosting methods and their speed/accuracy trade‑offs.
- [Li et al., 2017] — Feature selection survey, justifying SelectFromModel() for high‑dimensional poverty data.
- [Tingzon et al., 2019] — Prior Philippine poverty mapping using machine learning with geospatial data (R²=0.63), establishing baseline for comparison.

## Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly informs Odin’s classification module by benchmarking five boosting algorithms on a multi‑class prediction task using Philippine household data. Although the target (wealth quintile) differs from Odin’s financial behavioral profiles, the methodology — feature selection, handling class imbalance with SMOTE, and comparing accuracy/precision/recall/F1/AUC — is directly transferable to Odin’s user classification problem. The finding that CatBoost delivers top accuracy while LightGBM and XGBoost offer better computational efficiency provides a concrete trade‑off for Odin’s algorithm selection: accuracy‑critical modules may prefer CatBoost, while mobile‑constrained real‑time classification may favor LightGBM or XGBoost.

**Directly justifies:**

- “CatBoost achieved 90.93% accuracy on a 5‑class Philippine household classification task, outperforming XGBoost (89.41%), GBM (89.05%), and LightGBM (88.52%) — establishing CatBoost as a strong candidate for Odin’s financial profile classifier.”
- “LightGBM and XGBoost balance high accuracy (≥88.5%) with small model sizes (2.5–3.1 MB) and sub‑3‑second training times, making them suitable for mobile‑first deployment where computational resources are constrained.”
- “SMOTE (synthetic oversampling) effectively addresses class imbalance in household survey data and is directly applicable to Odin’s cold‑start problem where majority spending patterns may overwhelm minority behavioral profiles.”
- “AUC‑ROC scores near 1.0 for top boosting algorithms indicate excellent class separability — a desirable property for Odin’s profile classification to avoid ambiguous user assignments.”

**Limits of relevance:**

- The task is poverty/wealth classification using asset indicators (appliances, housing materials), not financial transaction‑based behavioral profiling — the feature space differs substantially from Odin’s spending data.
- The paper does not address temporal dynamics or profile updating over time, which is critical for Odin’s progressive reclassification.
- Dataset size (20,679 households) is larger than Odin’s expected early user base; cold‑start performance with sparse data is not evaluated.
- Evaluation metrics focus on static classification accuracy, not on interpretability or user trust, which are priorities for Odin’s classification module.

## Limitations

- The paper uses DHS asset‑based wealth index as ground truth, not actual income or spending data — limits direct transfer to financial behavior classification. [unacknowledged]
- No evaluation of model performance under cold‑start conditions (very few transactions per user), which is Odin’s core challenge.
- Feature selection retained 36 asset variables, but Odin’s classification would rely on transaction history, not household durable goods — feature engineering approach is not portable.
- Computational efficiency metrics are from a server environment; mobile inference times are not reported.
- The paper does not address concept drift (changing spending behavior over time), which Odin’s profiling module must handle.

## Remember This

- 🔑 **CatBoost: 90.93% accuracy** — top performer for multi‑class classification on Philippine household data.
- ⚠️ LightGBM & XGBoost: 88.5% accuracy with <3.1 MB models — best for mobile‑constrained deployment.
- 📌 SMOTE fixes class imbalance — essential for Odin’s cold‑start where minority profiles need synthetic samples.
- 💡 Feature selection (SelectFromModel) reduced 396 → 36 features — Odin can apply same to transaction attributes.
- 🧠 AUC‑ROC >0.98 for top models — excellent class separation, minimizes ambiguous profile assignments.
