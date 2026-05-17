# Review of Methods and Models for Forecasting Electricity Consumption

## Metadata

```yaml
---
paper_id: "10.3390/en18154032"
designation: international
title: "Review of Methods and Models for Forecasting Electricity Consumption"
authors: "Misiurek, K.; Olkuski, T.; Zy´sk, J."
year: 2025
venue: "Energies"
odin_topics: ["6.A", "6.B", "12.B"]
shorthand_tags: ["/forecasting-methods-survey", "/forecast-algo-candidates", "/forecast-eval-metrics"]
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

No single method works for all electricity data; deep learning excels on volatile individual loads, ARIMA on stable aggregate series, and hybrid models offer the best balance.

## Problem and Motivation

Electricity forecasting lacks a universal method, forcing practitioners to choose among dozens of statistical and AI models without clear guidance. Inaccurate forecasts cost grid operators an estimated USD 10 million annually per 1% increase in error. No prior review systematically mapped method performance to both forecast horizon (very short to long term) and data type (national aggregate to individual smart meter).

## Approach

- Review of studies from 2024 and earlier, with focus on last 5 years plus classical works.
- Four forecast horizons: very short-term (minutes–hours), short-term (days–weeks), medium-term (months–years), long-term (years–decades).
- Methods covered: statistical (ARIMA, SARIMA, exponential smoothing, linear regression); machine learning (ANN, LSTM, GRU, CNN-LSTM, Transformer); hybrid (ARIMA-ANN, SARIMA-ANN); evolutionary (genetic algorithms, grey models).
- Evaluation metrics: MAPE, RMSE, MAE, sMAPE, correlation coefficient, inference time.
- Mapping of methods to data types: national aggregate → ARIMA/SARIMA; sector-level → hybrid/LSTM; smart meter → LSTM/CNN-LSTM/Transformer; industrial → ARIMA/grey models.

## Findings

1. **LSTM networks achieved 10–15% RMSE improvement** over traditional ML models on high-volatility household load forecasting.
2. Hybrid CNN-LSTM reduced MSE to 0.3738 on residential data, outperforming standalone LSTM by capturing both spatial and temporal features.
3. Transformer-based models with sparse attention reached **up to 5× faster inference** than RNNs while maintaining comparable accuracy (RMSE ≈ 0.06 on AEP dataset).
4. ARIMA models achieved MAPE as low as 3.14% on stable aggregate consumption with clear seasonality, outperforming regression (8.1%) and ANN (5.6%) in that context.
5. Hybrid SARIMA-ANN models reduced RMSE from 0.0823 to 0.0792 compared to SARIMA alone, demonstrating benefit when linear and nonlinear structures are inseparable.

- No universal model exists; optimal choice depends on data volatility, seasonality, forecast horizon, and computational constraints.

## Key Figures and Tables

- Figure 2: Forecast horizons (VSTLF to LTLF) and operational domains → horizon dictates method selection; minutes vs. decades need完全不同 approaches.
- Table 1: Very short-term methods comparison → LSTM and IT-1 FIS both work, but LSTM handles nonlinearity better.
- Table 5: Mapping forecasting methods to data types → national aggregates need ARIMA; smart meters need deep learning; industrial data need grey or ARIMA.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| ARIMA | AutoRegressive Integrated Moving Average — statistical model for non-stationary time series. |
| LSTM | Long Short-Term Memory [think: memory cell that learns what to forget] — recurrent neural network that retains long-range dependencies. |
| MAPE | Mean Absolute Percentage Error — forecast error as percentage of actual values. |
| RMSE | Root Mean Square Error — penalizes large errors more heavily than MAE. |
| STLF | Short-Term Load Forecasting — predictions from one day to several weeks ahead. |
| LTLF | Long-Term Load Forecasting — predictions from years to decades ahead. |
| VSTLF | Very Short-Term Load Forecasting — predictions in minutes to hours ahead. |
| CNN | Convolutional Neural Network — extracts spatial/local patterns from time-series windows. |

## Critical Citations

- [Box & Jenkins, 1970] — Foundational ARIMA methodology still used as baseline in most forecasting papers.
- [Kong et al., 2017] — Demonstrated LSTM superiority for residential load forecasting; cited as benchmark for deep learning in volatile time series.
- [Kim & Cho, 2019] — Introduced CNN-LSTM hybrid for energy forecasting, proving spatial+temporal feature extraction improves accuracy.

## Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This review directly informs Odin's spending forecasting module by providing a structured, evidence-based comparison of candidate algorithms (LSTM, GRU, Transformer, ARIMA) across different data characteristics — volatility, seasonality, and sparsity. The finding that LSTM outperforms traditional models on high-volatility individual-level data (10–15% RMSE improvement) justifies selecting recurrent neural networks for forecasting per-category spending from user transaction histories, which are inherently irregular and volatile. The mapping of methods to data types (Table 5) offers a decision framework: if Odin users have stable, seasonal spending patterns, ARIMA may suffice; if patterns are erratic, deep learning is justified. Additionally, the review's coverage of evaluation metrics (MAPE, RMSE, MAE) and hybrid architectures supports Odin's algorithm evaluation and potential ensemble designs.

**Directly justifies:**

- "LSTM achieves 10–15% lower RMSE than traditional machine learning models on high-volatility individual-level time series data (Kong et al., 2017)."
- "Hybrid CNN-LSTM models reduce MSE to 0.3738 on residential energy data by capturing both local and global temporal patterns (Kim & Cho, 2019)."
- "Transformer-based models with sparse attention achieve up to 5× faster inference than RNNs while maintaining comparable forecasting accuracy (Chan & Yeo, 2024)."
- "No universal forecasting method exists; algorithm selection must align with data volatility, seasonality, forecast horizon, and computational constraints."
- "Standard evaluation metrics for forecast accuracy include MAPE, RMSE, and MAE, which are directly applicable to Odin's spending forecasting module."

**Limits of relevance:**

- Domain is electricity consumption, not personal spending; electricity has daily/seasonal cycles and weather dependency, while spending patterns are driven by income, obligations, and lifestyle — though both are time series with autocorrelation.
- Data source differences: electricity studies use smart meters (automated, high-frequency); Odin uses manual user input (sparse, potentially lower frequency and accuracy).
- No evaluation of cold-start forecasting (new users with no history) — a critical gap for Odin that this review does not address.
- Computational constraints of mobile devices are not discussed; deep learning inference speed and battery impact remain unexamined.

## Limitations

- Review paper synthesizes existing studies rather than presenting original experiments; conclusions depend on the quality and context of cited works.
- Focus on electricity consumption only; generalizability to financial spending time series is assumed but not tested. [unacknowledged]
- Does not address forecasting under manual data entry constraints (e.g., irregular logging, missing entries, user fatigue) — core to Odin's manual-input design. [unacknowledged]
- Minimal discussion of computational feasibility on mobile hardware or in-browser inference, which is essential for Odin's mobile-first architecture. [unacknowledged]
- The hybrid and deep learning methods reported often require large training datasets; applicability to Odin's smaller per-user transaction histories is uncertain.

## Remember This

- 🔑 **LSTM beats traditional models by 10–15% RMSE** on volatile individual-level data — key for Odin's spending forecast.
- 📌 No universal model — match algorithm to data volatility, seasonality, and horizon.
- 💡 Hybrid CNN-LSTM reduces MSE to 0.37 — captures both local and global patterns.
- ⚠️ Cold-start forecasting for new users is **not addressed** — a critical Odin gap.
