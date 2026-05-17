# A Comparative Review of Electricity Load Forecasting Methods Across Temporal Horizons

## Metadata

```yaml
---
paper_id: "f47ac10b-58cc-4372-a567-0e02b2c3d479"
designation: international
title: "A Comparative Review of Electricity Load Forecasting Methods Across Temporal Horizons"
authors: "Saeedian, Z."
year: 2025
venue: "Politecnico di Milano (Master's Thesis)"
odin_topics: ["6.A", "6.B", "8.A", "12.B"]
shorthand_tags: ["/forecasting-methods-survey", "/temporal-dependency", "/forecast-algo-candidates", "/forecast-algo-comparison", "/forecast-eval-metrics", "/anomaly-ml-families", "/anomaly-algo-candidates", "/eval-ml-design"]
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

LSTM and hybrid models outperform statistical methods like SARIMA for nonlinear time series forecasting, with LSTM achieving MAPE as low as 2.42% in short-term electricity demand.

## Problem and Motivation

Electricity load forecasting is essential for grid stability and operational planning, but traditional statistical models fail to capture nonlinear patterns and long-term dependencies. The increasing complexity from renewable integration, climate change, and consumer behavior demands more accurate, adaptable forecasting methods. Prior work lacked a systematic comparison of methods across short-, medium-, and long-term horizons with explicit guidance on trade-offs between accuracy, interpretability, and data requirements.

## Approach

- Reviewed methods across three horizons: short-term (minutes to 1 week), medium-term (1 week to 1 month), long-term (beyond 1 month).
- Categorized into statistical (ARIMA, SARIMA, regression), machine learning (SVR, tree-based, k-NN, ANN), deep learning (LSTM, Transformer), and hybrid models.
- Compared performance using MAE, RMSE, MAPE, and R² on real-world electricity datasets.
- Identified key influencing factors: weather, building attributes, socioeconomic indicators, technology adoption, and human behavior.
- Proposed a scalability framework linking method complexity to data availability (household to national level).

## Findings

1. LSTM achieved **2.42% MAPE** for short-term forecasting, outperforming SARIMA (which did not report comparable MAPE) and ARIMA (MAPE >5%).
2. Hybrid models (e.g., CNN-LSTM, ETS+LSTM) reduced MAPE by up to 25% over standalone models.
3. Transformer-based models (LDTformer, Autoformer) achieved MAE as low as 0.173 and SMAPE of 0.0186 for 4-week forecasts.

- SARIMA works well for stable seasonal patterns but fails on nonlinear, high-frequency, or volatile data.
- k-NN is interpretable but computationally expensive for large datasets; tree-based ensembles (XGBoost, LightGBM) balance accuracy and efficiency.
- No single model is universally optimal; selection depends on horizon, data volume, and need for interpretability.

## Key Figures and Tables

- Figure 2.1: Time horizon classification → maps methods to short (SARIMA, SVR), medium (RF, XGBoost), long (LSTM, Transformer).
- Table 2.1: Common error metrics (MAE, RMSE, MAPE, R²) → all directly applicable to Odin's forecasting evaluation.
- Figure 3.4: LSTM cell structure → gating mechanism enables long-term dependency learning.
- Table 3.9: Hybrid model benefits → CNN-LSTM improves short-term feature extraction and temporal modeling.
- Figure 6.2: Scalability by spatial data availability → guides model choice from household to national scale.

## Key Equations

$$MAE = \frac{1}{n}\sum_{t=1}^{n}|y_i - \hat{y_i}|$$
*Mean absolute error — average magnitude of forecast errors.*

$$MAPE = \frac{1}{n}\sum_{t=1}^{n}\left|\frac{y_i - \hat{y_i}}{y_i}\right| \times 100$$
*Mean absolute percentage error — scale-independent accuracy measure.*

$$f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$$
*LSTM forget gate — decides what past information to discard.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| STLF | Short-term load forecasting (minutes to 1 week). |
| MTLF | Medium-term load forecasting (1 week to 1 month). |
| LTLF | Long-term load forecasting (beyond 1 month). |
| SARIMA | Seasonal ARIMA — statistical model capturing trends and repeating patterns. |
| LSTM | Long Short-Term Memory [think: memory cell with gates that learns what to remember]. |
| MAPE | Mean Absolute Percentage Error — forecast error as a percentage. |
| Hybrid model | Combines two or more methods (e.g., statistical + deep learning). |

## Critical Citations

- [Bilgili & Pinar, 2023] — Direct comparison showing LSTM (2.42% MAPE) vastly outperforms SARIMA for electricity forecasting.
- [Deng et al., 2022] — Bagging-XGBoost hybrid improves short-term forecast stability under extreme weather.
- [Wang et al., 2021] — City-scale daily forecasting using data-driven models; establishes baseline for multi-step horizons.
- [Bendaoud et al., 2022] — XGBoost achieves 1.88% MAPE, best among ML models for short-term load.
- [Muzaffar & Afshari, 2019] — LSTM outperforms ARMA and SARIMA across 24h to 30-day horizons.

## Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

8.A — Anomaly Detection in Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly supports Odin's spending forecasting module by providing a comprehensive comparison of time series forecasting algorithms (SARIMA, LSTM, XGBoost, Transformer) and their trade-offs in accuracy, interpretability, and data requirements. The finding that LSTM outperforms statistical models on nonlinear, irregular sequences justifies Odin's use of sequential deep learning for per-category spending prediction, even though the domain is electricity rather than personal finance. The review of error metrics (MAE, MAPE, RMSE) establishes standard evaluation practices that Odin can adopt for module-level validation. Additionally, the discussion of anomaly detection methods (e.g., extreme weather identification) maps directly to Odin's anomalous spending detection — both require identifying deviations from learned patterns.

**Directly justifies:**

- "LSTM achieves 2.42% MAPE on short-term forecasting tasks, significantly outperforming SARIMA and ARIMA on nonlinear time series data."
- "Hybrid models combining statistical decomposition (ETS, ARIMA) with LSTM reduce forecasting error by up to 25% compared to standalone models."
- "XGBoost achieves the lowest MAPE (1.88%) among machine learning models for short-term forecasting, balancing accuracy and computational efficiency."
- "Quantile regression enables probabilistic forecasting, capturing uncertainty in demand — applicable to spending forecasts with confidence intervals."
- "For anomaly detection, Bagging-XGBoost robustly identifies extreme deviations (weather events); similar unsupervised or ensemble methods can flag spending outliers without labeled data."

**Limits of relevance:**

- Domain is electricity load, not personal spending — transaction patterns differ in scale, frequency, and drivers (e.g., income vs. temperature).
- Paper assumes abundant historical data (smart meters, weather stations); Odin's cold-start scenario (new users with no history) is not addressed.
- Many hybrid models require significant computational resources and tuning, which may exceed Odin's mobile-first constraints.
- Geographic and cultural context is Western/global; Filipino-specific spending seasonality (e.g., 13th month pay, remittances) is not discussed.

## Limitations

- Review is qualitative comparative analysis, not a controlled benchmark — performance claims aggregated from multiple studies with different datasets and preprocessing.
- No evaluation of forecasting methods under cold-start conditions (new users, no history) — a critical gap for Odin. [unacknowledged]
- Focuses on electricity load; assumes stationarity and seasonality that may not perfectly align with irregular human spending behavior.
- Deep learning and hybrid models require large datasets and high computational power — practical deployment constraints not quantified.
- Probabilistic forecasting methods (quantile regression, prediction intervals) are mentioned but not deeply evaluated for real-time use.

## Remember This

- 🔑 **LSTM beats SARIMA on nonlinear sequences** — 2.42% MAPE vs. statistical models' 5%+.
- 📌 **XGBoost is the best ML model** — 1.88% MAPE, balancing accuracy and speed for structured data.
- 💡 **Hybrids (ETS+LSTM) cut error by 25%** — combining trend decomposition with deep learning.
- ⚠️ **No cold-start evaluation** — unknown how any method performs with zero user history.
- 🔍 **Use MAE/MAPE for module evaluation** — standard metrics from load forecasting apply directly.
