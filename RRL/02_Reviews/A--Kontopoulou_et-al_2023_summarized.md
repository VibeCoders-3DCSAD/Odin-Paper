# A Review of ARIMA vs. Machine Learning Approaches for Time Series Forecasting in Data Driven Networks

## Metadata

```yaml
---
paper_id: "10.3390/fi15080255"
designation: algorithm-specific
title: "A Review of ARIMA vs. Machine Learning Approaches for Time Series Forecasting in Data Driven Networks"
authors: "Kontopoulou, V. I.; Panagopoulos, A. D.; Kakkos, I.; Matsopoulos, G. K."
year: 2023
venue: "Future Internet"
odin_topics: ["D.1", "D.2"]
shorthand_tags: ["/forecasting-methods", "/lstm-vs-alternatives", "/lstm-justification", "/forecast-cold-start"]
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

Machine learning models generally outperform ARIMA in time series forecasting, but ARIMA remains competitive for small, linear datasets; hybrid models consistently beat both.

## Problem and Motivation

The literature lacks a systematic, cross-domain comparison of ARIMA against machine learning methods for time series forecasting. This gap matters because practitioners are shifting toward AI without clear evidence of superiority. No prior review consolidated comparisons across finance, health, weather, utilities, and network traffic domains with explicit performance metrics.

## Approach

- Reviewed over 60 comparative studies published mostly after 2018 across five application domains.
- Compared ARIMA/SARIMA against SVM, tree-based (XGBoost, LightGBM, Random Forest), deep learning (LSTM, GRU, CNN), and hybrid models.
- Evaluated models using standard error metrics: MSE, RMSE, MAE, MAPE, R², and NSE.
- Identified conditions where ARIMA outperforms ML: small dataset size, limited value range, linear data relationships, and strong seasonality.
- Hybrid models follow two workflows: ARIMA models linear component then ML models residuals, or ML post-processes ARIMA residuals.

## Findings

1. In COVID-19 case forecasting, deep learning models (LSTM, GRU) achieved RMSE values **up to 40 times smaller** than ARIMA across multiple countries (ArunKumar et al., 2022).
2. ARIMA outperformed SVM and wavelet neural networks in drought forecasting, achieving R² > 0.9 vs. ~0.83 for ML models (Zhang et al., 2020).
3. Hybrid ARIMA-NARNN improved RMSE by **35.3%** over standalone ARIMA in COVID-19 forecasting (Prajapati et al., 2021).
4. SVM beat ARIMA in gold price prediction with RMSE = 0.028 vs. 36.18, and MAPE = 2.5% vs. 2897% (Makala et al., 2021).

- ML models showed superior performance in 80% of reviewed applications, with exceptions tied to dataset characteristics.

## Key Figures and Tables

- Table 2: ARIMA vs. SVM comparison studies → SVM wins except when data is linear or geographically specific.
- Table 4: ARIMA vs. deep learning studies → LSTM generally superior except for small/short-term datasets.
- Table 6: ARIMA vs. AI tradeoffs → ARIMA is explainable and low-complexity; AI requires large data and high compute.
- Figure 6: Hybrid ARIMA-ML workflow → ARIMA captures linear patterns, ML residuals model non-linearity.

## Key Equations

$$MSE = \frac{1}{N}\sum_{t=1}^{N}(y_t - \hat{y}_t)^2$$
*Mean squared error — penalizes large errors quadratically.*

$$MAPE = \frac{1}{N}\sum_{t=1}^{N}\left|\frac{y_t - \hat{y}_t}{y_t}\right|$$
*Mean absolute percentage error — scale-independent relative error.*

$$MAE = \frac{1}{N}\sum_{t=1}^{N}|y_t - \hat{y}_t|$$
*Mean absolute error — intuitive average error in original units.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| ARIMA | AutoRegressive Integrated Moving Average — classical statistical model for non-stationary time series. |
| LSTM | Long Short-Term Memory [think: memory cell with forget/input/output gates] — recurrent neural network that learns long-term dependencies. |
| SVM | Support Vector Machine — supervised model that finds optimal separating hyperplane; regression variant used for forecasting. |
| Hybrid model | Combines ARIMA (linear patterns) with ML (non-linear residuals) — outperforms either alone. |
| RMSE | Root Mean Square Error — square root of MSE, interpretable in original units. |
| MAPE | Mean Absolute Percentage Error — forecast error as percentage of actual values. |
| Seasonal ARIMA (SARIMA) | ARIMA extended with seasonal components (P,D,Q) to handle periodic patterns. |

## Critical Citations

- [Box et al., 2015] — Foundational textbook defining ARIMA methodology and parameter selection.
- [Hochreiter & Schmidhuber, 1997] — Original LSTM paper; all LSTM forecasting comparisons trace here.
- [Zhang, 2003] — Pioneering hybrid ARIMA-ANN model that became template for hybrid forecasting.

## Relevance to Odin

**Topics:**

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

**Contribution to Odin:**

This review directly supports Odin's choice of LSTM over ARIMA for the spending forecasting module by systematically aggregating evidence that deep learning models outperform ARIMA on non-linear, real-world time series across multiple domains. The finding that ARIMA can be superior only for small, linear datasets (e.g., cold-start conditions) informs Odin's fallback strategy: use ARIMA for users with minimal transaction history, then transition to LSTM as data accumulates. The review's conclusion that hybrid ARIMA-ML models consistently beat standalone approaches suggests a potential future enhancement for Odin's forecasting module.

**Directly justifies:**

- "Deep learning models (LSTM, GRU) achieve up to 40× lower RMSE than ARIMA on non-linear time series with sufficient training data (ArunKumar et al., 2022, as reviewed by Kontopoulou et al., 2023)."
- "ARIMA outperforms machine learning models only when datasets are small, exhibit limited value ranges, or follow linear relationships — conditions that do not hold for mature user spending histories."
- "Hybrid ARIMA-ML models, where ARIMA captures linear components and ML models residuals, consistently improve forecasting accuracy over standalone ARIMA by margins of 20–35% across multiple domains."
- "The No Free Lunch theorem (Wolpert & Macready, 1997) implies no single forecasting method dominates all time series; algorithm selection must match data characteristics."

**Limits of relevance:**

- The review aggregates findings from diverse domains (finance, weather, health, networks) — no study specifically targets personal spending time series of young professionals.
- Most compared studies use high-frequency data (daily/hourly); Odin operates on monthly manual entries, which may reduce LSTM's advantage.
- The superior ML performance assumes large training datasets; Odin's cold-start users may see better results from ARIMA initially.
- No comparison includes Filipino-specific spending patterns or income volatility.

## Limitations

- This is a review paper, not primary research; it reports others' findings without controlling for experimental differences. [unacknowledged]
- The review may suffer from publication bias — studies showing ML superiority are more likely published.
- Thresholds for "small dataset" where ARIMA beats ML are not quantified (e.g., number of time steps).
- Many primary studies use proprietary datasets, limiting reproducibility and generalizability to spending data.
- The review does not address computational constraints on mobile devices, which is critical for Odin's deployment.

## Remember This

- 🔑 **ML beats ARIMA in 80% of studies** — LSTM leads on non-linear, large-dataset forecasts.  
- 📌 ARIMA **40× worse RMSE** than LSTM on COVID-19 curves (non-linear time series).  
- 💡 Hybrid ARIMA-ML improves RMSE by **35%** — best of both worlds for complex patterns.  
- ⚠️ ARIMA wins on **small, linear datasets** — use as cold-start fallback before LSTM.
