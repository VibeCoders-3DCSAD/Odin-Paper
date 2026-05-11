# Expense tracker management system using machine learning

## Metadata

```yaml
---
paper_id: "10.14744/sigma.2025.00119"
designation: algorithm-specific
title: "Expense tracker management system using machine learning"
authors: "Thakur, R. S.; Jadhav, A."
year: 2025
venue: "Sigma Journal of Engineering and Natural Sciences"
odin_topics: ["A.2", "D.1", "G.1"]
shorthand_tags: ["/pfms-limitations", "/pfms-gap", "/forecasting-methods", "/cat-approaches"]
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[ ]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
---
```

## TL;DR

A voting ensemble regressor achieves **78.11% R-squared** and the lowest relative absolute error (0.1765) for expense prediction, outperforming individual models like XGBoost.

## Problem and Motivation

Existing expense trackers rely on manual input and lack predictive analytics, making expense tracking time-consuming and error-prone. Poor tracking limits financial awareness and budgeting effectiveness. No prior work applied ensemble machine learning to expense prediction within a full-featured web application.

## Approach

- Dataset: “Daily Household Transactions” (Kaggle) with date, mode, category, subcategory, note, amount, income/expense.
- Preprocessing: MinMax scaling, log1p transformation of amount, TF-IDF vectorization (min_df=3) for text fields.
- Train-test split: 70% training, 30% testing.
- Individual models: XGBoost, Random Forest, SVM, MLP, KNN, Decision Tree, Extra Tree, CatBoost.
- Ensemble methods: Bagging, Boosting, Stacking, Voting, Blending.
- Evaluation metrics: R-squared, Mean Absolute Error (MAE), Mean Square Error (MSE), Relative Absolute Error (RAE).
- Web application built with Django (backend), PostgreSQL (database), HTML/CSS/JS + Chart.js (frontend).

## Findings

1. XGBoost achieved the highest R-squared among individual models: **77.89%**.
2. Voting ensemble regressor outperformed all models with R-squared = **78.11%** and RAE = 0.1765.
3. Voting ensemble also achieved the lowest MAE (0.6121) and MSE (0.9648) among ensembles.

- The web application provides expense categorization, income/expense entry, monthly budget forecasting, and interactive dashboards.

## Key Figures and Tables

- Table 2: Performance of machine learning models → Voting ensemble has highest R² (78.11%) and lowest RAE (0.1765).
- Figure 1: Distribution of log(1+amount) after transformation → Shows normalization of skewed expense values.

## Key Equations

$$R^2 = 1 - \frac{SS_{res}}{SS_{tot}}$$
*Proportion of variance explained by the model (higher is better).*

$$MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|$$
*Average absolute prediction error in original units.*

$$RAE = \frac{\sum_{i=1}^{n}|y_i - \hat{y}_i|}{\sum_{i=1}^{n}|y_i - \bar{y}|}$$
*Normalized error relative to predicting the mean (lower is better).*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| XGBoost | Extreme Gradient Boosting — a fast, efficient boosting algorithm that builds trees sequentially to correct prior errors. |
| Voting ensemble | Combines predictions from multiple models by averaging (regression) to improve accuracy and reduce variance. |
| R-squared (R²) | Percentage of variance in actual expenses explained by the model; 78.11% means the model captures most spending patterns. |
| RAE | Relative Absolute Error — prediction error relative to simply guessing the average expense. |
| TF-IDF | Transforms text (e.g., categories) into numerical importance scores for machine learning. |

## Critical Citations

- [Kaggle, 2024] — Daily Household Transactions dataset used for all experiments; without it no model training possible.
- [Odegua, 2019] — Empirical study of ensemble techniques (bagging, boosting, stacking) justifying the choice of voting ensemble.
- [Doan & Kalita, 2015] — Framework for selecting ML algorithms using regression models, informing model comparison methodology.

## Relevance to Odin

**Topics:**

A.2 — Existing Personal Finance and Budget Management Systems

D.1 — Predictive Modeling in Personal Finance Systems

G.1 — Expense Categorization in Filipino Personal Finance Contexts

**Contribution to Odin:**

This paper directly informs Odin's spending forecasting module by demonstrating that ensemble methods (specifically voting regressor) achieve higher prediction accuracy (78.11% R²) than individual models like XGBoost on household transaction data. The systematic comparison of eight ML models against five ensemble techniques provides a benchmark for algorithm selection when Odin's forecasting module is implemented. Additionally, the paper's expense categorization approach (predefined + custom categories) and web-based dashboard design offer practical implementation patterns for Odin's expense categorization and user interface modules.

**Directly justifies:**

- "A voting ensemble regressor achieves 78.11% R-squared for expense prediction, outperforming XGBoost (77.89%) and other individual models on a household transaction dataset."
- "Ensemble methods (bagging, boosting, stacking, voting, blending) consistently improve predictive accuracy over single models for personal expense forecasting."
- "Expense categorization into predefined categories (food, transportation, entertainment, utilities) with custom category support is a viable design pattern for personal finance systems."
- "Log transformation of expense amounts (log1p) and TF-IDF vectorization of textual category data are effective preprocessing steps for machine learning-based expense tracking."

**Limits of relevance:**

- Dataset is from Indian households (Indian Rupee); spending patterns and category relevance may differ from Filipino young professionals.
- The web application is not mobile-first; Odin requires mobile-first design, and interface assumptions may not transfer directly.
- No LSTM or time-series specific models were tested; forecasting uses regression on aggregated features, not sequential spending data.
- Prediction task is total expense amount, not per-category spending as in Odin's forecasting module.

## Limitations

- No evaluation of the web application using standardized usability frameworks (e.g., SUS, ISO 25010). [unacknowledged]
- Dataset is synthetic/virtual transactions, not real user spending data, which may limit generalizability to real-world behavior.
- The paper does not address cold-start prediction for new users with no spending history.
- No comparison with deep learning models (LSTM, GRU) that are standard for time-series forecasting in personal finance.
- The application requires manual expense entry; Odin also uses manual input, but the paper does not study user fatigue or retention.

## Remember This

- 🔑 **78.11% R²** — voting ensemble beats XGBoost by 0.22 percentage points on expense prediction.
- 📌 Ensemble methods (voting, stacking, boosting) consistently improve accuracy over single models.
- ⚠️ No LSTM or time-series models — this paper uses regression on static features, not sequential spending.
- 💡 Expense categorization with predefined + custom categories is implemented and usable.
- ✅ Log1p + TF-IDF preprocessing are effective for skewed expense and text category data.
