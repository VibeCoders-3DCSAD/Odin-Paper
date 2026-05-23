# When machine learning meets econometrics: Can it build a better measure to predict multidimensional poverty and examine unmeasurable economic conditions?

## Metadata

```yaml
---
paper_id: "10.1016/j.sctalk.2024.100387"
designation: algorithm-specific
title: "When machine learning meets econometrics: Can it build a better measure to predict multidimensional poverty and examine unmeasurable economic conditions?"
authors: "Onsay, E. A.; Rabajante, J. F."
year: 2024
venue: "Science Talks"
odin_topics: ["5.C", "6.A"]
shorthand_tags: ["/classifier-candidates", "/classifier-eval-metrics", "/forecast-algo-candidates", "/forecast-algo-comparison"]
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

Random forest achieved **0.9208 R²** and 95.94% accuracy for poverty prediction, outperforming XGBoost and LightGBM on Philippine indigenous community census data.

## Problem and Motivation

Poverty measurement using traditional surveys is costly, labor-intensive, and time-consuming, making policy targeting difficult. Indigenous communities face complex, multidimensional poverty that generic national methods fail to capture. No prior work combined machine learning with econometric causality testing to produce disaggregated, replicable poverty predictions for Philippine indigenous populations.

## Approach

- Data: Full census of all households in Goa, Camarines Sur, Philippines, including indigenous people (1,660 IP households, 8,022 persons).
- Method: Econometric causality tests (logit/probit) first identified 15 multidimensional predictors (health, housing, water, education, income, peace/order).
- Algorithms compared: Random Forest, XGBoost, LightGBM, SVM, AdaBoost, Decision Tree, Bagging, Gaussian NB, Perceptron, linear regression.
- Evaluation metrics: R², RMSE, MSE, accuracy, classification pipeline performance.
- Outcome variable: Binary poverty status (monthly income below PhP10,481 for a family of five) plus continuous poverty index.

## Findings

1. Random forest regressor achieved the **highest R² of 0.9208** — linear regression scored only 0.4221.
2. Random forest classifier attained 95.94% accuracy in pipeline mode, with 90.69% at random split.
3. Lowest RMSE: random forest at 0.3298 vs. LightGBM 0.3642 and XGBoost 0.4001.
- Household size and informal settlement status are the strongest poverty predictors.
- 82% of indigenous people live in poverty; 71% are food-insecure.

## Key Figures and Tables

- Figure 4: RMSE comparison → random forest lowest at 0.3298.
- Figure 6: R² comparison → random forest highest at 0.92075.
- Figure 7: Accuracy comparison → random forest classifier 95.94% (pipeline) vs. Bagging 84.37%.
- Figure 12: MSE for IP modeling → random forest lowest at 0.5497.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Random Forest | An ensemble ML method that averages many decision trees to reduce overfitting. |
| XGBoost | Extreme Gradient Boosting — an optimized tree-boosting algorithm. |
| LightGBM | Light Gradient Boosting Machine — a fast, leaf-wise tree-boosting algorithm. |
| Econometrics | Statistical methods to test causal relationships and estimate economic models. |
| Multidimensional poverty | Poverty measured across multiple deprivations (health, education, income, etc.) not just income. |
| RMSE | Root mean square error — typical error magnitude of a regression model. |
| MSE | Mean square error — average squared difference between predicted and actual values. |

## Critical Citations

- [Onsay & Rabajante, 2024] — Source of the census dataset and ML models used in this paper.
- [Sohnesen & Stender, 2017] — Prior empirical assessment of random forest for poverty prediction, used as benchmark.
- [Muñetón-Santa & Manrique-Ruiz, 2023] — Open-data approach to predicting multidimensional poverty with ML.
- [Browne et al., 2021] — Multivariate random forest for poverty and malnutrition prevalence.

## Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

**Contribution to Odin:**

This paper directly informs Odin's classification module (user financial profiling) by demonstrating that random forest outperforms boosting algorithms (XGBoost, LightGBM) on Philippine household data, achieving 0.92 R² and 95%+ accuracy. Although the target is poverty classification rather than spending behavior, the methodological framework — using econometric causality tests to select predictors before applying ML — maps directly to Odin's need to identify which user features (income stability, household size, spending patterns) causally drive financial behavior profiles. The paper's use of a full census (no sampling error) and local Philippine data provides strong justification for algorithm selection in Odin's cold-start profiling scenario.

**Directly justifies:**

- "Random forest achieves 0.9208 R² for binary poverty classification on Philippine census data, outperforming XGBoost (0.4722 MSE) and LightGBM (0.1242 MSE)."
- "Econometric causality testing (logit/probit) should precede ML feature selection to ensure predictors are causally linked to the target outcome, not merely correlated."
- "Household size and informal settlement status are the strongest predictors of poverty status in Philippine indigenous communities, suggesting these variables should be included in financial behavior profiles."
- "Random forest's ability to handle non‑linear relationships and estimate feature importance makes it suitable for classification tasks with multidimensional socioeconomic indicators."

**Limits of relevance:**

- Paper predicts poverty (binary low-income status), not spending behavior or budgeting adherence — the target outcome differs from Odin's forecasting and anomaly detection domains.
- Dataset is rural indigenous communities in Bicol, not Metro Manila young professionals; income patterns and spending structures may not generalize.
- No time-series or sequential data — the paper uses cross-sectional census data, whereas Odin requires longitudinal transaction sequences.
- Poverty classification uses a fixed monthly income threshold (PhP10,481 for a family of five), which does not account for individual‑level expense categorization or discretionary spending.

## Limitations

- No temporal validation — models are evaluated on cross-sectional data only; performance over time is untested. [unacknowledged]
- Paper claims “no known limits” due to full census, but generalizability outside Goa, Camarines Sur is not established.
- Model interpretability for end users is not addressed — only feature importance is reported.
- Binary poverty threshold (PhP10,481) is not adjusted for household size variation beyond the stated “family of five” assumption.
- The paper does not compare against deep learning methods (e.g., neural networks), which may be relevant for Odin's sequential forecasting.

## Remember This

- 🔑 **R² = 0.9208** — random forest beats XGBoost, LightGBM on Philippine poverty data.
- 💡 Econometric causality first → then ML: identify predictors that are causally linked, not just correlated.
- 📌 Household size and informal settlement are the top poverty predictors — both are candidate features for Odin’s user profile.
- ⚠️ Cross‑sectional poverty classification — not time‑series spending forecasting; generalization to spending behavior is untested.
