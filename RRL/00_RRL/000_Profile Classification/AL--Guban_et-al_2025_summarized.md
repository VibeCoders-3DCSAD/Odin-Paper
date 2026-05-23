# WEKA-BASED DECISION-TREE MODEL FOR USER SUBSCRIPTION PLAN PREDICTION

## Metadata

```yaml
---
paper_id: "b7c8a9e6-3f4d-5a1e-9b2c-8d7e6f5a4b3c"
designation: algorithm-specific
title: "WEKA-BASED DECISION-TREE MODEL FOR USER SUBSCRIPTION PLAN PREDICTION"
authors: "Guban, J. C. R.; Menderico, C. D. R.; Montalban, D. M. G."
year: 2025
venue: "Unknown"
odin_topics: ["5.C", "12.B"]
shorthand_tags: ["/classifier-candidates", "/classifier-eval-metrics", "/eval-ml-design"]
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

A J48 decision tree predicts streaming subscription plans with **72% accuracy**, identifying country, age, and device type as the most influential predictors.

## Problem and Motivation

Streaming platforms lack an understanding of how demographic and behavioral attributes (age, country, device) jointly influence subscription tier choice, limiting targeted marketing. Predicting plan selection matters because personalized offers can improve retention and revenue. No prior work had built an interpretable decision-tree model specifically for subscription plan prediction using these attributes.

## Approach

- Dataset: 2,500 anonymized user records with five predictors (country, age, gender, device type, subscription start month) and target (Basic, Standard, Premium).
- Algorithm: J48 decision tree (WEKA’s C4.5 implementation), trained on 80% of data and tested on 20% (500 instances).
- Preprocessing: Removed duplicates and missing values; encoded categorical fields as nominal; kept age as continuous.
- Evaluation metrics: Accuracy, Kappa statistic, mean absolute error, root mean squared error, precision, recall, F‑measure, ROC area, and confusion matrix.
- No hyperparameter tuning or cross‑validation beyond the single 80/20 split reported.

## Findings

1. Overall classification accuracy: **72%** on the 500‑instance test set.
2. Country was the most influential predictor, followed by age and device type (gender and start month had weaker effects).
3. Standard plan achieved highest precision (0.793) and ROC area (0.871); Basic and Premium had ROC areas >0.81.
- United Kingdom users all defaulted to Standard plan (195 training instances), indicating extreme market homogeneity.
- Young smartphone users who subscribed later in the year preferred Premium; older Smart TV users leaned toward Basic or Standard.

## Key Figures and Tables

- Table 1: Split testing summary → Accuracy 72%, Kappa 0.5797, mean absolute error 0.2216.
- Table 2: User profile combinations per country → Example: US smartphone users aged ≤31, start month ≤5 → Basic.
- Table 3: Per‑class performance metrics → Standard plan has precision 0.793 and F‑measure 0.765.
- Table 4: Confusion matrix → Correct predictions: 123 Basic, 118 Premium, 119 Standard out of 500.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| J48 | WEKA’s implementation of the C4.5 decision‑tree algorithm. |
| WEKA | Waikato Environment for Knowledge Analysis, a data mining toolkit. |
| ROC area | Receiver Operating Characteristic area; measures how well the model separates classes (0.5 = random, 1.0 = perfect). |
| Kappa statistic | Agreement between predicted and actual classes after accounting for chance agreement. |
| Precision | Proportion of true positives among all instances predicted as positive. |
| Recall (True Positive Rate) | Proportion of true positives among all actual positive instances. |
| F‑measure | Harmonic mean of precision and recall (balanced performance metric). |
| Confusion matrix | Table showing correct and incorrect classifications per class. |

## Critical Citations

- [Chaurasia & Pal, 2019] — Data mining for Netflix subscription prediction, establishing the problem domain.
- [Akar, 2023] — Decision trees balance accuracy and interpretability, justifying algorithm choice.
- [Hsiao, 2023] — 70% accuracy benchmark for commercial predictive models, contextualizing the 72% result.
- [Powers, 2011] — Accuracy alone can mislead; precision/recall/ROC are essential for uneven class distributions.

## Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper demonstrates a complete supervised classification pipeline (J48 decision tree) for predicting user plan choices from demographic and behavioral attributes. The methodology directly informs Odin’s financial behavioral profile classification module, showing how an interpretable tree-based model can produce actionable rules (e.g., “age ≤31 and device=smartphone → Premium”). Although the domain is streaming subscriptions, the classification approach and evaluation framework (accuracy, precision, recall, F-measure, ROC area, confusion matrix) are transferable to predicting user spending behavior or budget preference profiles in Odin. The paper also reinforces that country/geography can be a strong predictor—relevant when Odin expands beyond Metro Manila.

**Directly justifies:**

- “J48 decision trees achieve 72% accuracy on multi‑class user classification with 2,500 records and five attributes using an 80/20 train‑test split.”
- “Country, age, and device type are the most influential predictors in user tier choice, demonstrating that geography and demographics drive subscription decisions.”
- “Standard plan classification reached precision 0.793 and ROC area 0.871, showing strong discriminative power for balanced classes.”
- “Per‑class precision, recall, and F‑measure provide more nuanced evaluation than accuracy alone, especially when class distributions differ.”

**Limits of relevance:**

- Domain is streaming subscription plans, not personal spending or budgeting behavior.
- Dataset lacks financial variables (income, expenses, savings) essential for Odin’s core tasks.
- The paper is a student course project, not peer‑reviewed; methodology lacks rigorous validation (e.g., cross‑validation, hyperparameter tuning).
- Findings are based on a streaming platform dataset, not Philippine financial data.

## Limitations

- The original data source is not specified, and real‑world validity is unconfirmed [unacknowledged].
- No comparison to other algorithms (Random Forest, SVM, logistic regression) to justify J48 selection.
- Single 80/20 split without cross‑validation increases risk of overfitting; tree depth and leaf count not reported.
- External validity limited to streaming platforms; not tested on financial transaction data.
- No analysis of class imbalance or handling of rare subscription tiers (all three tiers appear roughly balanced in the confusion matrix).

## Remember This

- 🔑 **72% accuracy** — J48 predicts subscription plans from 5 user attributes on 2,500 records.
- 📌 Country > age > device — geography drives tier choice most, then demographics.
- ✅ Standard plan easiest to classify (precision 0.793, ROC 0.871), Basic and Premium slightly harder.
- ⚠️ Domain mismatch — streaming subscriptions ≠ personal budgets, but the classification method transfers to Odin’s profiling module.
