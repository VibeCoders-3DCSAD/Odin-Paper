# A Decade of Applied Quantitative Analytics for Philippine Policy: Forecasting, Statistical Forensics, and Predictive Modeling Across Education, Energy, Agriculture, Health, and Finance

## Metadata

```yaml
---
paper_id: "10.20944/preprints202603.1811.v1"
designation: local
title: "A Decade of Applied Quantitative Analytics for Philippine Policy: Forecasting, Statistical Forensics, and Predictive Modeling Across Education, Energy, Agriculture, Health, and Finance"
authors: "Velasco, A."
year: 2026
venue: "Preprints.org"
odin_topics: ["6.A", "6.B", "8.A", "8.B", "12.B"]
shorthand_tags: ["/forecasting-methods-survey", "/forecast-algo-candidates", "/forecast-algo-comparison", "/forecast-eval-metrics", "/temporal-dependency", "/anomaly-unsupervised-baseline", "/anomaly-algo-candidates", "/eval-ml-design"]
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

A review of Philippine policy analytics across five sectors shows a progression from classical time series toward machine learning, Benford-based anomaly detection, and explainable AI, with uneven validation rigor.

## Problem and Motivation

Philippine policy research lacks a synthesized overview of applied quantitative analytics moving from descriptive diagnostics to predictive and forensic methods. Government planning requires reliable forecasting and data-quality assessment under nonstationary social, epidemiological, and economic conditions. Prior work had not systematically compared methodological evolution across education, energy, agriculture, health, and finance using official Philippine datasets.

## Approach

- Structured narrative review of 17 Philippine studies (2019–2025) coded by domain, dataset, modeling approach, validation strategy, and policy contribution.
- Sectors covered: education (dropout profiling), energy (electricity/coal demand forecasting), agriculture (rice/corn production and Benford audit), health (dengue, measles, diabetes, underreporting), finance (PSE index with LSTM).
- Methods compared: ARIMA, SARIMA, Holt–Winters, random forests, echo-state networks, NNAR, LSTM, Benford analysis, PCA, SHAP for interpretability.
- Validation strategies: holdout sets, residual diagnostics, error metrics (RMSE, MAE, MAPE), but uneven across studies; some use only in-sample diagnostics.
- External comparison literature benchmarks the corpus against international developments in dropout research, electricity forecasting, crop analytics, and epidemiological surveillance.

## Findings

1. **Random forests outperformed other ML models for quarterly rice and corn production forecasting** in the Philippines.
2. NNAR achieved the best performance for measles incidence forecasting among SARIMA, Holt–Winters, ESN, and NNAR.
3. Holt–Winters gave lower RMSE and MAPE than SARIMA for quarterly rice and corn.
- Benford-based anomaly detection identified unusual first-digit patterns in dengue and crop statistics, providing a low-cost data-quality screen.
- LSTM with Takens embedding improved Philippine Stock Exchange Index prediction over linear models.
- Validation rigor is uneven: some studies use explicit holdout, others rely on residual diagnostics only.

## Key Figures and Tables

None.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| ARIMA | AutoRegressive Integrated Moving Average — a classical time-series forecasting model. |
| SARIMA | Seasonal ARIMA — ARIMA extended to handle repeating patterns like monthly cycles. |
| LSTM | Long Short-Term Memory [think: memory cell that learns what to forget and keep over long sequences] — a recurrent neural network for sequential data. |
| NNAR | Neural Network AutoRegressive — a feedforward neural network applied to lagged time-series values. |
| ESN | Echo State Network — a recurrent network with a fixed, random reservoir for efficient training. |
| RMSE | Root Mean Square Error — measures average forecast error, penalizing large errors heavily. |
| MAE | Mean Absolute Error — average absolute forecast error, less sensitive to outliers. |
| MAPE | Mean Absolute Percentage Error — error as a percentage of actual values. |
| SHAP | SHapley Additive exPlanations — game-theory method to explain individual predictions from ML models. |
| Benford's Law | A statistical principle that smaller leading digits (1,2,3) appear more often in many real-world datasets. |
| PSE index | Philippine Stock Exchange Index — the main benchmark index of the Philippine stock market. |
| ML | Machine Learning — algorithms that learn patterns from data without explicit programming. |

## Critical Citations

- [Deyle & Sugihara, 2011] — Foundational theory of nonlinear state-space reconstruction used in the LSTM finance study.
- [van Klompenburg et al., 2020] — Systematic review of ML for crop yield prediction, used as external benchmark for agriculture studies.
- [Rumberger & Lim, 2008] — Seminal 25‑year review of dropout research framing the education section's descriptive approach.
- [Idrovo et al., 2011] — Benford-based public health surveillance method applied to dengue and crop statistics in the reviewed corpus.

## Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This review directly informs Odin’s forecasting module by surveying candidate algorithms (ARIMA, LSTM, random forests) and documenting their comparative performance on Philippine time-series data — justifying algorithm selection for spending prediction. The Benford-based anomaly detection work provides a precedent for unsupervised, cold-start anomaly screening that Odin could adapt to detect irregular manual transaction entries or data-quality issues. The paper’s critique of validation practices (holdout vs. residual diagnostics) and its call for rolling-origin evaluation and uncertainty quantification establish a benchmark for how Odin’s algorithmic modules should be rigorously tested before deployment.

**Directly justifies:**

- "LSTM with state-space reconstruction captures nonlinear temporal dependencies in Philippine financial time series, outperforming linear models on the PSE index."
- "Random forests achieved superior forecast accuracy for quarterly production data compared to ARIMA and SARIMA, supporting their use in spending forecasting."
- "Benford-based anomaly detection provides a low-cost unsupervised screening method for identifying unusual patterns in administrative data without labeled training examples."
- "Validation using holdout sets and error metrics (RMSE, MAE, MAPE) is standard, but rolling-origin evaluation and uncertainty quantification are recommended for operational policy analytics."

**Limits of relevance:**

- The paper is a review of policy analytics, not an original empirical study on personal finance systems; specific performance claims come from the cited primary studies, not the review itself.
- The finance domain is stock market prediction, not individual spending forecasting; transferability to personal transaction sequences is assumed but not tested.
- Benford analysis is used for data-quality auditing (e.g., crop statistics, disease counts), not for detecting anomalous spending deviations from a user’s budget.
- The reviewed studies use official aggregate datasets; Odin’s manual transaction input at the individual user level presents different sparsity and cold-start challenges not addressed.

## Limitations

- The corpus mixes journal articles, preprints, and SSRN papers with heterogeneous data frequencies, sample sizes, and validation designs — direct cross-sector comparisons are not appropriate.
- Some study characteristics were reconstructed from metadata when full texts were not equally accessible.
- No original empirical results are presented; the review synthesizes existing work, limiting the novelty of citable claims. [unacknowledged]
- The paper does not address mobile-first constraints, manual data entry, or personal finance user behavior — all central to Odin’s context. [unacknowledged]
- External validation across regions or periods is absent in most reviewed studies, a gap the paper itself acknowledges.

## Remember This

- 🔑 Random forests beat ARIMA/SARIMA for Philippine crop forecasting — a candidate for Odin’s spending prediction module.
- 📌 Benford analysis flags data anomalies without labeled training — applicable to Odin’s cold-start anomaly detection.
- 💡 LSTM + chaos embedding improves Philippine stock index prediction over linear models — supports deep learning for financial sequences.
- ⚠️ Validation rigor is uneven; rolling-origin evaluation and uncertainty intervals are missing — Odin must adopt stricter practices.
