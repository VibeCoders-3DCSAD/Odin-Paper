# An Overview of Forecasting Methods for Monthly Electricity Consumption

## Metadata

```yaml
---
paper_id: "10.17559/TV-20220430111309"
designation: algorithm-specific
title: "An Overview of Forecasting Methods for Monthly Electricity Consumption"
authors: "Krstev, S.; Forcan, J.; Krneta, D."
year: 2023
venue: "Tehnički vjesnik (Technical Gazette)"
odin_topics: ["6.A", "6.B", "12.B"]
shorthand_tags: ["/forecasting-methods-survey", "/forecast-algo-candidates", "/forecast-algo-comparison", "/forecast-eval-metrics"]
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

Neural network autoregression (NNAR) achieved the lowest forecasting error (MAPE = 2.67%) for monthly electricity consumption, outperforming classical time series and other machine learning methods.

## Problem and Motivation

Mid-term load forecasting (MTLF) receives less research attention than short-term forecasting, yet accurate MTLF is critical for power plant production planning and grid maintenance. No prior study had compared twelve different forecasting methods—including classical time series (ARIMA, ETS, structural models) and modern ML approaches (KNN, random forest, XGBM, SVM, neural networks)—on the same monthly consumption dataset from a real distribution system operator.

## Approach

- Data: Monthly electricity consumption (kWh) from Bosnia and Herzegovina DSO, Jan 2000–Mar 2020 (228 training months, 15 test months).
- Outlier detection via Loess seasonal-trend decomposition; missing values imputed with linear interpolation.
- Feature engineering: 24 lagged variables; feature selection via linear model (lm) and principal component analysis (PCA).
- Classical methods: Seasonal naïve, ARIMA(1,0,1)(1,1,1), ETS(A,N,A), and structural time series (BSM) with Kalman filter.
- ML methods: Linear regression, Elastic net, KNN, random forest, XGBM, linear SVM, radial SVM.
- Neural network: NNAR(p,P,k)m with p=3, P=1, k=6 (seasonal autoregression).
- Evaluation metric: Mean absolute percentage error (MAPE) on test period (Jan 2019–Mar 2020).

## Findings

1. NNAR(3,1,6) achieved the **lowest MAPE of 2.67%** — the best among all twelve methods.
2. Classical time series performed better than most ML methods: ETS(A,N,A) at 3.28%, ARIMA at 3.36%, BSM at 3.87%, seasonal naïve at 4.16%.
3. Best ML result came from PCA+KNN with MAPE 4.38%; worst was PCA+XGBM at 7.35%.

- For small sample sizes (228 monthly observations), statistical methods (ETS, ARIMA) outperformed most ML methods except NNAR — consistent with prior findings that ML requires larger data.
- Absolute relative errors varied by month; NNAR gave <1% error for five months (Mar, Aug, Sep, Dec 2019, Jan 2020).

## Key Figures and Tables

- Figure 4: Forecasts from SNAIVE, ARIMA, ETS, BSM → ETS visually tracks actual consumption most closely.
- Figure 8: MAPE comparison bar chart → NNAR lowest, then ETS, ARIMA, BSM, then ML methods.
- Table 2: MAPE for ML methods with lm vs. PCA → PCA improves all except XGBM; best PCA+KNN (4.38%).
- Table 3: Absolute relative error per month for ETS, PCA+KNN, NNAR → NNAR has smallest error in 11 of 15 months.

## Key Equations

$$y'_{T+h|T} = y_{T+h-m(k+1)}$$
*Seasonal naïve forecast: repeat value from same season in previous cycle.*

$$\text{MAPE} = \frac{100}{n} \sum_{t=1}^{n} \left| \frac{y_t - \hat{y}_t}{y_t} \right|$$
*Mean absolute percentage error — used to compare all forecasting methods.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| MTLF | Mid-term load forecast: prediction horizon from two weeks to two years. |
| MAPE | Mean absolute percentage error — lower is better for forecast accuracy. |
| NNAR | Neural network autoregression — combines lagged inputs with a hidden layer for time series. |
| ETS | Exponential smoothing state-space model (Error, Trend, Seasonal) — averages past values with exponentially decaying weights. |
| BSM | Basic structural model — decomposes time series into trend, seasonal, and noise components, estimated via Kalman filter. |

## Critical Citations

- [Hyndman & Athanasopoulos, 2014] — Foundational textbook defining ETS, ARIMA, and forecast evaluation used in this paper's methodology.
- [Makridakis et al., 2018] — Prior study showing statistical methods can outperform ML on univariate time series; this paper replicates that finding for monthly electricity data.
- [Cerqueira et al., 2019] — Established that sample size drives method choice (small data favors statistics); this paper's results support that conclusion.

## Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper provides a direct benchmark for Odin’s spending forecasting module by comparing twelve forecasting methods on monthly time series data. The finding that NNAR (neural network autoregression) achieves the lowest MAPE (2.67%) justifies considering neural network architectures for per-category spending prediction, even on modest-sized historical datasets (228 months). The observation that classical methods (ETS, ARIMA) outperform most ML methods when sample size is limited directly informs Odin’s cold-start strategy: for new users with few transactions, a simpler statistical forecaster may be more accurate than a complex ML model until sufficient spending history accumulates.

**Directly justifies:**

- "Neural network autoregression (NNAR) achieved 2.67% MAPE on monthly consumption forecasting, outperforming ARIMA (3.36%) and ETS (3.28%) on a 228-month univariate time series."
- "For small to medium-sized time series (under ~250 observations), classical statistical methods (ETS, ARIMA) produce lower forecast error than most machine learning models, with the exception of neural networks."
- "PCA-based feature selection improved MAPE for 6 of 7 ML methods compared to linear-model feature selection, reducing error by up to 2 percentage points."
- "Seasonal naïve forecasting — repeating the same month’s value from the prior year — achieved 4.16% MAPE, serving as a simple baseline for evaluating more complex forecasting algorithms."

**Limits of relevance:**

- Domain is electricity consumption, not personal spending; temporal patterns and volatility differ.
- Dataset is aggregated monthly consumption, whereas Odin operates on per-transaction daily or weekly spending.
- No evaluation of cold-start performance (forecasting with <12 months of history), which is critical for new Odin users.
- The study assumes stationary seasonality (annual cycle); Filipino spending may have multiple cycles (monthly paydays, 13th-month pay, holidays).

## Limitations

- Only univariate forecasting (past consumption alone); Odin’s spending could benefit from exogenous variables (income, priorities) not considered here.
- No explicit cold-start evaluation — all models trained on ≥19 years of data; performance with limited history is unknown. [unacknowledged]
- Dataset is from Bosnia and Herzegovina; seasonal and trend patterns may not generalize to Metro Manila’s tropical climate and financial calendar.
- MAPE can be misleading when actual values are near zero (common in spending categories); the paper does not discuss this limitation.
- Neural network architecture (NNAR) is relatively simple (single hidden layer); deeper architectures like LSTM were cited but not implemented for MTLF.

## Remember This

- 🔑 **NNAR achieved 2.67% MAPE** — best among 12 forecasting methods on monthly time series data.  
- 📌 Small data favors statistics: ETS (3.28%) beat most ML models except NNAR — crucial for Odin’s cold-start users.  
- 💡 PCA feature selection improved ML forecast accuracy vs. raw lag features — applicable to Odin’s transaction lag engineering.  
- ⚠️ Domain is electricity, not spending — seasonality and volatility differ; validate before adopting for personal finance.
