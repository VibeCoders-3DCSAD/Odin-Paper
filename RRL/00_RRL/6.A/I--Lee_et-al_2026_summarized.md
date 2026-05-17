# Comparing deep learning and classical regression approaches for predicting healthcare expenditure and spending: a systematic review

## Metadata

```yaml
---
paper_id: "10.1080/13696998.2026.2630598"
designation: algorithm-specific
title: "Comparing deep learning and classical regression approaches for predicting healthcare expenditure and spending: a systematic review"
authors: "Lee, J. T.; Yeh, M. H.-S.; Li, V. C.-S.; Chen, H.-H.; Liu, Y.-H.; Chen, Y.-C.; Wu, D. B.-C."
year: 2026
venue: "Journal of Medical Economics"
odin_topics: ["6.A", "6.B", "12.A", "12.B"]
shorthand_tags: ["/forecasting-methods-survey", "/temporal-dependency", "/forecast-algo-candidates", "/forecast-algo-comparison", "/forecast-algo-tradeoffs", "/forecast-eval-metrics", "/eval-frameworks-survey", "/eval-ml-design", "/eval-limitations"]
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

Deep learning models (LSTM, CNN-LSTM) reduce healthcare cost prediction error by 10–20% over classical regression in longitudinal settings, but tree-based methods remain competitive for cross-sectional tabular data.

## Problem and Motivation

It remains unclear when deep learning architectures add predictive value over classical regression and tree-based models for healthcare expenditure forecasting. Accurate cost predictions are essential for insurance underwriting, budget planning, and value-based payment models. No prior systematic review had directly compared neural network performance against traditional methods across varying data contexts and study designs.

## Approach

- Systematic review (PROSPERO CRD420251129440) of Web of Science, PubMed, Embase, Scopus through August 2025.
- Eight eligible studies using real-world individual-level data (claims, EHR, registries) from US, Europe, and Asia; sample sizes 50,000 to 1.4 million.
- Deep learning architectures: feedforward DNN, LSTM, stacked LSTM, CNN-LSTM hybrid, RNN, V-GAN.
- Comparators: linear regression, GLM, ridge, LASSO, random forest, gradient boosting, ARIMA.
- Evaluation metrics: RMSE, MAE, R², AUROC, precision@k, cost-capture; internal validation only (no external validation).
- Proposed Complexity–Performance Hypothesis: model capacity should match data complexity for optimal accuracy.

## Findings

1. Sequential deep models (LSTM, CNN-LSTM) achieved **10–20% lower RMSE/MAE** than classical regression in longitudinal cost forecasting tasks.
2. R² improvements of 0.01 to 0.15 for deep models over baselines; AUROC up to 0.78 for high-risk classification.
3. Stacked LSTM reduced RMSE by ~19% over ARIMA for medication spending time series.

- Shallow feedforward neural networks underperformed random forest on cross-sectional tabular data (adj-R² 0.316 vs 0.475).
- Prior costs and utilization were consistently the strongest predictors across all studies.
- Tree-based methods (random forest, GBM) remained highly competitive for cross-sectional, low-dimensional cost prediction.

## Key Figures and Tables

- Figure 2: Model performance by data complexity → deep learning dominates longitudinal/multimodal regime; regression plateaus early.
- Table 2: Comparative performance of deep learning vs classical models → LSTM reduces RMSE by ~19% over ARIMA.
- Table 3: Neural network architectures applied → feedforward, recurrent, hybrid/generative.
- Table 4: Five challenges for deep learning in healthcare cost prediction (interpretability, benchmarking, short horizons, data diversity, underuse of SDOH).

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LSTM | Long Short-Term Memory [think: memory cell that learns what to forget and remember over time] |
| CNN | Convolutional Neural Network (extracts local patterns from sequential data) |
| RNN | Recurrent Neural Network (processes sequences with internal memory) |
| DNN | Deep Neural Network (feedforward network with multiple hidden layers) |
| GLM | Generalized Linear Model (regression family for non-normal outcomes) |
| RMSE | Root Mean Square Error (typical prediction error in original units) |
| MAE | Mean Absolute Error (average absolute prediction error) |
| R² | Coefficient of determination (variance explained by the model) |
| AUROC | Area Under Receiver Operating Characteristic curve (discrimination ability for binary classification) |
| EHR | Electronic Health Record (digital patient data from clinical care) |
| EMR | Electronic Medical Record (clinical data from a single provider) |

## Critical Citations

- [Drewe-Boss et al., 2022] — First large-scale comparison showing DNN outperforms ridge regression for population health cost prediction.
- [Lewis et al., 2021] — LSTM and CNN achieve AUROC of 0.78 for predicting preventable acute care use in heart failure patients.
- [Yang et al., 2018] — RNN increases test R² from 0.14 to 0.30 for Medicaid high-cost patient expenditure prediction.
- [Vimont et al., 2022] — Shallow MLP underperforms random forest on cross-sectional claims data (adj-R² 0.316 vs 0.475).

## Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

12.A — Evaluation Frameworks for Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This systematic review directly informs Odin's spending forecasting module by benchmarking sequential deep learning architectures (LSTM, CNN-LSTM) against classical regression and tree-based methods on longitudinal expenditure data. The finding that LSTM reduces prediction error by 10–20% over regression on temporal sequences justifies selecting LSTM or hybrid models for Odin's per-category spending forecasting, especially given Odin's manual transaction input which generates sequential user history. The review's proposed Complexity–Performance Hypothesis provides a guiding principle for Odin's algorithm selection: match model capacity to data complexity — simple cold-start users may benefit from tree-based models, while established users with rich transaction histories justify LSTM. Finally, the evaluation metrics reported (RMSE, MAE, R²) establish a benchmark for Odin's module-level performance assessment.

**Directly justifies:**

- "Sequential deep learning models (LSTM, CNN-LSTM) reduce prediction error by 10–20% over classical regression on longitudinal cost data with temporal dependencies."
- "Tree-based methods (random forest, gradient boosting) outperform shallow feedforward neural networks on cross-sectional tabular data, suggesting they are better baselines for cold-start user profiles with limited history."
- "Prior costs and utilization are consistently the strongest predictors across all studies — Odin's forecasting module should heavily weight historical transaction sequences rather than demographic features alone."
- "The Complexity–Performance Hypothesis states that predictive accuracy is maximized when model capacity is matched to data complexity: simple data → simple models; rich temporal data → deep sequential models."

**Limits of relevance:**

- The prediction target is healthcare expenditure, not general personal spending; spending patterns differ in volatility and seasonality.
- All studies use institutional or claims data with automatic capture, not manual transaction entry as in Odin.
- No study includes Filipino populations or addresses cultural spending obligations (e.g., family remittances, 13th-month pay cycles).
- Prediction horizons are typically one year; Odin's forecasting may operate on monthly or weekly intervals.
- External validation across datasets is absent, limiting generalizability claims.

## Limitations

- Only eight studies were included, with substantial heterogeneity in design, data sources, and outcome definitions — no meta-analysis possible.
- No full external validation across independent datasets was performed in any included study. [unacknowledged]
- Prediction horizons were limited to one year in most studies, ignoring longer-term expenditure dynamics.
- Calibration, fairness, and decision-curve analyses were rarely reported.
- Social determinants of health and behavioral predictors were almost entirely omitted from model inputs. [unacknowledged]

## Remember This

- 🔑 **LSTM/CNN-LSTM cut forecast error by 10–20%** over regression in longitudinal spending data — key for Odin's forecasting module.
- 📌 Tree-based models beat shallow neural nets on cross-sectional tabular data — better cold-start baseline.
- 💡 Complexity–Performance Hypothesis: match model capacity to data complexity — don't overfit simple users with deep nets.
- ⚠️ No Filipino data and no manual entry validation — findings require cautious transfer to Odin's context.
