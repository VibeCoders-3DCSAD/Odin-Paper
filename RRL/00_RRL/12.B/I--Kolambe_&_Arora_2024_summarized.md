# Forecasting the Future: A Comprehensive Review of Time Series Prediction Techniques

## Metadata

```yaml
---
paper_id: "9c3e5f1a-4d2b-8a7c-6e9d-1f2b3c4d5e6f"
designation: international
title: "Forecasting the Future: A Comprehensive Review of Time Series Prediction Techniques"
authors: "Kolambe, M.; Arora, S."
year: 2024
venue: "J. Electrical Systems"
odin_topics: ["6.A", "6.B", "12.B"]
shorthand_tags: ["/forecasting-methods-survey", "/forecast-algo-candidates", "/forecast-algo-tradeoffs", "/forecast-eval-metrics", "/eval-ml-design"]
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

Classical, machine learning, deep learning, and hybrid time series forecasting methods are categorized and compared, with a focus on challenges like non-stationarity and evaluation metrics (MAE, RMSE).

## Problem and Motivation

Traditional forecasting methods struggle to capture complex patterns and dynamics in real-world time series data, limiting prediction accuracy. Accurate forecasting is critical for finance, economics, energy, weather, and healthcare applications. Prior work lacked a comprehensive, up-to-date review that synthesizes modern deep learning approaches (LSTM, GRU, Transformers) alongside classical methods to guide method selection.

## Approach

- Survey of time series forecasting literature spanning classical statistical methods (ARIMA, exponential smoothing, STL) to modern deep learning (LSTM, GRU, Transformers).
- Categorization into four families: classical, machine learning (random forest, SVM, XGBoost), deep learning (RNN, LSTM, GRU, Transformer), and hybrid approaches.
- Analysis of data-related challenges (noise, outliers, missing values, non-stationarity), model-related challenges (overfitting, hyperparameter tuning, interpretability), and temporal challenges (seasonality, irregular intervals, evolving patterns).
- Review of evaluation metrics: MAE, MSE, RMSE, MAPE, forecast bias, and coverage probability.
- Discussion of future directions: explainable AI (SHAP, LIME), probabilistic forecasting (Gaussian processes, Bayesian methods), handling big data (Apache Spark), and advanced feature engineering.

## Findings

- **Deep learning methods (LSTM, GRU) excel at capturing long-term dependencies but lack interpretability**, while classical methods (ARIMA, exponential smoothing) are simple and interpretable but struggle with non-linear patterns.
- Hybrid approaches that combine classical methods with machine learning or deep learning (e.g., ARIMA-NN, ensemble stacking) often outperform individual models by leveraging complementary strengths.
- Key forecasting challenges include non-stationarity (solved via differencing or decomposition), missing values (imputation), and seasonality (STL, SARIMA).
- Evaluation metrics: MAE measures average absolute error; RMSE penalizes larger errors more heavily; MAPE expresses error as percentage for scale-independent comparison.
- Future directions emphasize explainable AI to build trust, probabilistic forecasting to capture uncertainty, and scalable algorithms for big time series data.

## Key Figures and Tables

- Table 1: Methods applied by application domain → LSTM, ARIMA, and exponential smoothing are widely used across finance, supply chain, energy, and healthcare.
- Table 2: Forecasting methods and their characteristics → LSTM handles long-term dependencies; GRU is simpler with comparable performance; Transformers enable parallel processing via attention.

## Key Equations

$$MAE = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y_i}|$$
*Average absolute difference between predicted and actual values.*

$$MSE = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y_i})^2$$
*Squares errors, penalizing larger deviations more heavily.*

$$RMSE = \sqrt{\frac{1}{n} \sum_{i=1}^n (y_i - \hat{y_i})^2}$$
*Square root of MSE, expressed in original data units.*

$$MAPE = \frac{1}{n} \sum_{i=1}^n \left|\frac{y_i - \hat{y_i}}{y_i}\right| \times 100$$
*Percentage-based error, scale-independent for relative comparison.*

$$Bias = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y_i})$$
*Systematic overestimation (negative) or underestimation (positive).*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| ARIMA | Autoregressive Integrated Moving Average — classical model combining auto-regression, differencing, and moving averages. |
| LSTM | Long Short-Term Memory — RNN variant with memory cells that learn what to forget [think: selective memory that keeps important patterns]. |
| RNN | Recurrent Neural Network — neural network with loops for sequential data, but suffers vanishing gradients. |
| GRU | Gated Recurrent Unit — simplified LSTM with fewer gates, computationally efficient. |
| SARIMA | Seasonal ARIMA — extends ARIMA to handle repeating seasonal patterns. |
| STL | Seasonal-Trend decomposition using LOESS — breaks time series into seasonal, trend, and remainder components. |
| MAE | Mean Absolute Error — average absolute forecast error, robust to outliers. |
| RMSE | Root Mean Squared Error — standard deviation of residuals, sensitive to large errors. |
| MAPE | Mean Absolute Percentage Error — percentage error, useful for comparing across scales. |
| XGBoost | Extreme Gradient Boosting — ensemble method with sequential weak learners, high accuracy. |
| SHAP | SHapley Additive exPlanations — method to measure feature importance for model interpretability. |
| LIME | Local Interpretable Model-agnostic Explanations — explains individual predictions locally. |

## Critical Citations

- [Yan & Ouyang, 2018] — Foundational application of deep learning to financial time series prediction.
- [Siami-Namini et al., 2019] — Benchmarks LSTM and BiLSTM for time series forecasting performance.
- [Lundberg & Lee, 2017] — Introduces SHAP values for interpreting black-box model predictions.

## Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This review directly supports Odin's spending forecasting module by surveying candidate algorithms (LSTM, GRU, ARIMA, hybrid models) and their trade-offs in capturing temporal dependencies. The categorization of forecasting challenges — particularly non-stationarity, missing values, and seasonality — informs design decisions for handling Filipino young professionals' irregular income and spending patterns. The evaluation metrics section provides justification for using MAE or RMSE to measure forecasting accuracy in Odin's module-level testing, and the future directions on explainable AI align with Odin's need for user trust through transparency.

**Directly justifies:**

- "LSTM networks address the vanishing gradient problem and capture long-range temporal dependencies in sequential data, making them suitable for spending forecasting over multi-month horizons."
- "Hybrid methods that combine ARIMA with neural networks often outperform individual models by leveraging both linear and non-linear pattern extraction."
- "Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) are standard accuracy metrics for time series forecasting, with RMSE penalizing larger errors more heavily."
- "Non-stationarity in time series — where statistical properties change over time — can be addressed via differencing or decomposition into trend, seasonal, and residual components."
- "Probabilistic forecasting using Gaussian processes or Bayesian methods provides uncertainty estimates alongside point predictions, which is critical for user-facing budget alerts."

**Limits of relevance:**

- The review is domain-agnostic; no findings are specific to personal finance or Filipino spending behavior.
- No empirical comparisons or performance numbers are provided — only qualitative method characteristics.
- Cold-start forecasting (new users with no transaction history) is not discussed.
- The review assumes regularly sampled data; Odin's manual input may produce irregular intervals not fully addressed.

## Limitations

- No empirical evaluation or benchmark results — the review synthesizes existing literature without novel quantitative comparisons.
- Limited discussion of mobile-specific constraints (e.g., on-device computation, battery, storage) for deploying forecasting models. [unacknowledged]
- Ignores the cold-start problem common in personal finance apps where users have no historical data.
- Does not address domain adaptation or transfer learning across different user populations (e.g., Western vs. Filipino).
- Future directions mention explainable AI but do not provide concrete implementation guidance for time series.

## Remember This

- 🔑 **LSTM and GRU capture long-term dependencies** — RNNs suffer vanishing gradients; LSTMs solve it with memory cells.
- 📌 **Hybrid models (ARIMA + NN) beat single methods** — combine linear and non-linear pattern extraction.
- 💡 **RMSE penalizes large errors more than MAE** — choose based on whether big mistakes are costly.
- ⚠️ **Non-stationarity breaks most models** — fix with differencing or decomposition before forecasting.
- 🧠 **No empirical numbers in this review** — use it for method surveys and trade-offs, not performance benchmarks.
