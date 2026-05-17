# A Review of ARIMA vs. Machine Learning Approaches for Time Series Forecasting in Data Driven Networks

## Metadata

```yaml
---
paper_id: "10.3390/fi15080255"
designation: international
title: "A Review of ARIMA vs. Machine Learning Approaches for Time Series Forecasting in Data Driven Networks"
authors: "Kontopoulou, V.; Panagopoulos, A.; Kakkos, I.; Matsopoulos, G."
year: 2023
venue: "Future Internet"
odin_topics: ["6.A", "6.B", "8.A", "12.B"]
shorthand_tags: ["/forecasting-methods-survey", "/forecast-algo-comparison", "/forecast-eval-metrics", "/anomaly-ml-families", "/anomaly-algo-candidates", "/eval-ml-design", "/eval-limitations"]
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

Machine learning models generally outperform ARIMA for time series forecasting, but ARIMA remains competitive on small, linear datasets; hybrid ARIMA-ML models consistently beat both.

## Problem and Motivation

No comprehensive review systematically compares ARIMA against modern machine learning (ML) and deep learning (DL) models across multiple application domains. Many studies claim ML superiority without a proper ARIMA baseline, leading to unreliable algorithm selection. Prior work lacked a structured evaluation of when and why ARIMA might still be preferable.

## Approach

- Systematic review of published studies that directly compare ARIMA (or SARIMA) with ML/DL models on the same datasets.
- Covers five domains: finance (stock, bitcoin), health (COVID-19), weather (drought, wind), utilities (load, water, oil), and networks (web, cellular).
- ML/DL models reviewed: SVM, decision trees (XGBoost, LightGBM), RNN, LSTM, GRU, CNN, and hybrids (ARIMA+NN, ARIMA+SVM, etc.).
- Evaluation metrics: MSE, RMSE, MAPE, MAE, R², NSE, and others; most comparisons use RMSE or MAPE as primary.

## Findings

- **LSTM and GRU achieve RMSE values up to 40 times smaller than ARIMA for COVID‑19 case prediction in non‑linear data regimes** (ArunKumar et al., 2022).
- Hybrid ARIMA‑NARNN improved RMSE by 35.3% over ARIMA alone for COVID‑19 forecasting (Prajapati et al., 2021).
- ARIMA outperforms ML on small datasets (≤ few hundred points) and when the time series is approximately linear (e.g., linear load patterns, low‑volatility stock prices).
- Tree‑based models (XGBoost) require fewer data and features than deep learning for comparable accuracy, and dominated recent forecasting competitions (M4, M5).
- In 15+ comparison studies, ARIMA was superior only in specific conditions: strong seasonality (wind speed), very small value ranges, or when data granularity is coarse.

## Key Figures and Tables

- Table 2: ARIMA vs. SVM comparison studies → SVM wins for non‑linear data (gold price, COVID‑19), ARIMA wins for drought forecasting.
- Table 4: ARIMA vs. deep learning → LSTM/GRU dominate except for small bitcoin datasets and offshore wind speed.
- Table 5: ARIMA vs. hybrid models → hybrids always beat standalone ARIMA.
- Table 6: Advantages/disadvantages of ARIMA vs. AI → ARIMA: explainable, low compute, small data; AI: needs large data, black‑box, better non‑linear fit.
- Figure 6: Hybrid model flowchart (ARIMA then ML on residuals) → standard two‑step decomposition approach.

## Key Equations

$$MSE = \frac{1}{N}\sum_{t=1}^{N}(y_t - \hat{y}_t)^2$$
*Mean squared error — penalizes large errors quadratically.*

$$MAPE = \frac{1}{N}\sum_{t=1}^{N}\left|\frac{y_t - \hat{y}_t}{y_t}\right|$$
*Mean absolute percentage error — scale‑independent but undefined for zero values.*

$$\nabla^d x_t = c + \sum_{i=1}^{p}\phi_i\nabla^d x_{t-i} + \sum_{i=0}^{q}\theta_i \epsilon_{t-i}$$
*General ARIMA(p,d,q) model — differencing (d) removes non‑stationarity.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| ARIMA | AutoRegressive Integrated Moving Average — linear time series model that uses past values and errors. |
| LSTM | Long Short-Term Memory — recurrent neural network with gates that learn what to remember/forget. |
| GRU | Gated Recurrent Unit — simplified LSTM with two gates instead of three. |
| SVM | Support Vector Machine — finds a hyperplane to separate or regress data; SVR is regression version. |
| XGBoost | Extreme Gradient Boosting — tree‑based ensemble that builds weak learners sequentially. |
| Hybrid model | Combines ARIMA (linear part) + ML (non‑linear residuals) for improved accuracy. |
| Stationarity | Statistical properties (mean, variance) constant over time — required for basic ARIMA. |

## Critical Citations

- [Box & Jenkins, 2015] — Foundational ARIMA theory and model identification.
- [Zhang, 2003] — Pioneered hybrid ARIMA‑ANN two‑step residual modeling.
- [Hochreiter & Schmidhuber, 1997] — Introduced LSTM, now dominant for sequence forecasting.
- [Makridakis et al., 2018] — Highlighted that many ML papers lack proper ARIMA baselines.

## Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

8.A — Anomaly Detection in Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This review directly informs Odin's spending forecasting module by providing a clear decision framework: LSTM and hybrid ARIMA-ML are best for non-linear, irregular spending patterns, while ARIMA alone suffices for cold-start users with very short history. The finding that tree‑based models (XGBoost) achieve competitive accuracy with fewer data and less feature engineering than deep learning justifies considering LightGBM or XGBoost as lighter alternatives for mobile deployment. The review also establishes standard evaluation metrics (RMSE, MAPE) and cautions that dataset size and linearity determine algorithm superiority—critical for Odin's early adoption phase.

**Directly justifies:**

- "LSTM and GRU achieve RMSE values up to 40 times lower than ARIMA for non‑linear time series, but ARIMA works better on small (≤500 points) or linear datasets."
- "Hybrid ARIMA-ML models consistently outperform individual models; ARIMA‑NARNN improved RMSE by 35.3% over ARIMA alone in COVID‑19 forecasting."
- "Tree‑based models like XGBoost require fewer training data and features than deep learning while delivering similar or better forecasting accuracy."
- "ARIMA fails on highly non‑linear or chaotic series (e.g., COVID‑19 deaths, Bitcoin volatility) but remains robust for short‑term, stable, or seasonal univariate series."

**Limits of relevance:**

- Review aggregates studies from finance, health, weather — personal spending data has different periodicity (daily/weekly) and lower volatility.
- Most benchmark datasets are large (years of hourly data); Odin's manual input yields sparse, short histories, favoring simpler models.
- Philippine cultural spending patterns (e.g., remittances, 13th month) not represented in any reviewed study.
- Deep learning models in review require non‑trivial compute; mobile deployment constraints not discussed.
- No direct comparison of cold‑start performance except inference that ARIMA handles small data better.

## Limitations

- The review itself does not perform original experiments; conclusions depend on quality and bias of included studies. [unacknowledged]
- Most compared studies optimize ARIMA manually but use default ML hyperparameters, potentially disadvantaging ARIMA.
- Publication bias likely: studies where ML fails may be underrepresented.
- No discussion of real‑time or streaming forecast updates, which matter for Odin's progressive reclassification.
- Computational cost and memory footprint of each model are not quantitatively compared — essential for mobile‑first design.

## Remember This

- 🔑 **40× lower RMSE** for LSTM/GRU vs ARIMA on non‑linear data — big win for complex spending patterns.
- 📌 ARIMA wins on small datasets (<500 points) — relevant for Odin's cold‑start users.
- 🧠 Hybrid ARIMA‑ML improves RMSE by **35%** — best of both linear and non‑linear worlds.
- ⚠️ Tree models (XGBoost) need less data than deep learning — lighter option for mobile forecasting.
- ✅ Use RMSE or MAPE to compare algorithms; review provides benchmarks for each domain.
