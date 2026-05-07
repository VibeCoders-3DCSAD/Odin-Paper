# Expense tracker management system using machine learning

```yaml
---
name: paper-summary
paper_id: "c3f5a6d8-9e1b-4c7a-8d2f-6e9b4a7c1d5e"
source_document: "1754475364-en.md"
designation: algorithm-specific
title: "Expense tracker management system using machine learning"
authors: "Thakur, R. S.; Jadhav, A."
year: 2025
venue: "Sigma Journal of Engineering and Natural Sciences"
odin_topics: ["A.2", "D.1"]
shorthand_tags: ["/pfms-limitations", "/forecasting-methods"]
summary_date: 2026-05-07
version: "1.0"
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

A voting ensemble regressor achieves the highest expense prediction accuracy (R² = 78.11%), outperforming individual models like XGBoost.

## Problem and Motivation

Existing expense trackers rely on manual data entry and lack automated prediction, making them time‑consuming and error‑prone. Users need a system that forecasts future expenses from past spending patterns. No prior work applied ensemble learning to household transaction data for expense prediction.

## Approach

- Dataset: Daily Household Transactions (India) with date, mode, category, subcategory, note, amount, income/expense.
- Preprocessing: MinMax scaling, log1p amount transformation, TF‑IDF vectorizer (min_df=3) on text fields.
- Models: XGBoost, Random Forest, SVM, MLP, KNN, Decision Tree, Extra Tree, CatBoost.
- Ensembles: Bagging, Boosting, Stacking, Voting, Blending.
- Evaluation: 70/30 train/test split; metrics R², MAE, MSE, RAE.

## Findings

1. XGBoost achieves the highest R² among individual models: **77.89%**.
2. Voting ensemble regressor outperforms all models: R² = **78.11%**, RAE = **0.1765**.
3. Relative absolute error (RAE) is the deciding factor when R² values are similar.
4. Manual entry and limited analytics are the main limitations of prior systems (Table 1).

## Key Figures and Tables

- Table 1: State‑of‑the‑art existing works → common limitations: manual input, no automation, platform restrictions.
- Table 2: Performance comparison → Voting ensemble has highest R² (78.11) and lowest RAE (0.1765).
- Figure 1: log(1+amount) distribution → shows transformation that normalizes skewed transaction amounts.

## Key Equations

$$R^2 = 1 - \frac{SS_{res}}{SS_{tot}}$$
*Proportion of variance in expenses explained by the model; higher is better (max 1).*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| XGBoost | Extreme Gradient Boosting – an efficient tree‑based ensemble that corrects prior errors sequentially. |
| CatBoost | Categorical Boosting – handles categorical features natively with ordered boosting to reduce overfitting. |
| TF‑IDF | Term Frequency – Inverse Document Frequency; converts text to numeric features by weighting rare terms higher. |
| RAE | Relative Absolute Error – total absolute error divided by error of a simple mean predictor; lower is better. |

## Critical Citations

None.

## Relevance to Odin

**Topics:**

A.2 – Existing Personal Finance and Budget Management Systems  

D.1 – Predictive Modeling in Personal Finance Systems

**Contribution to Odin:**

This paper provides empirical evidence that ensemble machine learning (specifically voting regression) outperforms individual models for expense prediction using household transaction data. It identifies key limitations of existing PFMS (manual entry, no automation) that Odin must avoid. The evaluation metrics (R², MAE, RAE) offer a benchmark framework for comparing Odin’s forecasting module against prior work.

**Directly justifies:**

- Ensemble methods (voting regressor) improve expense forecasting accuracy over single models like XGBoost or SVM.
- Manual data entry is a primary failure point in existing PFMS – automated prediction reduces user friction.
- Relative absolute error (RAE) is a decisive metric when R² values are close, guiding algorithm selection for Odin’s forecasting.
- Predictive analytics based on past transactions can generate monthly budget forecasts without explicit user goal input.

**Limits of relevance:**

- Dataset is Indian (not Filipino) – spending categories and cultural norms differ.
- No temporal sequence modeling (LSTM, RNN) – the paper uses regression on engineered features, not time series.
- The system still requires manual expense entry (no automated bank sync or receipt scanning).

## Limitations

- Dataset lacks temporal ordering across users – no explicit time‑series validation.
- Evaluation done on a static split; no cross‑validation or real‑world deployment testing.
- Manual entry remains a bottleneck despite prediction automation.
- Web application is Django‑based, not mobile‑first – mobile constraints not addressed.

## Remember This

- 🔑 **78.11% R²** – voting ensemble gives the best expense prediction accuracy.
- 💡 XGBoost alone reaches 77.89% – close but ensemble edges it out via lower RAE (0.1765).
- 📌 Still requires **manual expense entry** – prediction doesn’t automate data capture.
