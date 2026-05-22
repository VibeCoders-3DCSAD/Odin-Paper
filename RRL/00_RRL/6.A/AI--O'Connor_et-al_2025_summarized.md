# A Review of Electricity Price Forecasting Models in the Day-Ahead, Intra-Day, and Balancing Markets

## Metadata

```yaml
---
paper_id: "10.3390/en18123097"
designation: algorithm-specific
title: "A Review of Electricity Price Forecasting Models in the Day-Ahead, Intra-Day, and Balancing Markets"
authors: "O'Connor, C.; Bahloul, M.; Prestwich, S.; Visentin, A."
year: 2025
venue: "Energies"
odin_topics: ["6.A", "6.B", "12.B"]
shorthand_tags: ["/forecasting-methods-survey", "/forecast-algo-candidates", "/forecast-algo-comparison", "/forecast-algo-sparsity", "/forecast-algo-tradeoffs", "/forecast-eval-metrics", "/forecast-cold-start", "/eval-ml-design", "/eval-limitations"]
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

Hybrid and ensemble models dominate day-ahead forecasting; recurrent neural networks lead intra-day; simple regularized models like LEAR outperform complex DL in volatile balancing markets due to overfitting.

## Problem and Motivation

Electricity price forecasting is critical but increasingly difficult due to renewable energy volatility and market structure differences across day-ahead, intra-day, and balancing markets. Most existing reviews focus only on the day-ahead market, ignoring the unique challenges of real-time markets. This review fills the gap by systematically comparing forecasting model performance across all three short-term markets.

## Approach

- Reviewed 176+ studies on electricity price forecasting from 2002 to 2025.
- Categorized models into statistical (AR, ARIMA, GARCH, LASSO, LEAR), ML (RF, XGB, KNN, SVR), DL (LSTM, GRU, CNN, TFT), and hybrid architectures.
- Analyzed performance separately for day-ahead, intra-day, and balancing markets.
- Evaluated models based on accuracy, volatility handling, overfitting tendency, and data requirements.
- Identified persistent issues in evaluation metrics (MAPE problematic near-zero prices).

## Findings

- Hybrid and ensemble models (XGB, LSTM-CNN) consistently outperform standalone models in day-ahead markets.
- LSTM and GRU dominate intra-day forecasting due to effective capture of short-term dependencies.
- **LEAR (LASSO-elastic net AR) outperforms complex DL models in balancing markets**, where volatility and data sparsity cause overfitting.
- Simple naive models remain competitive baselines in real-time markets due to strong autocorrelations.
- MAPE is unsuitable for balancing markets because prices approach zero, inflating errors.

## Key Figures and Tables

- Figure 1: Market temporal granularity → balancing operates at seconds/minutes, DAM at hours.
- Table 1: Pre-2020 EPF models → DAM dominates; statistical models prevalent before 2017.
- Table 2: Post-2020 EPF models → real-time markets (IDM, BM) gain attention; hybrid models rise.
- Figure 2: DAM/IDM/BM trading timelines → submission windows shrink from 12h to 1–15 minutes.

## Key Equations

$$y_t = \phi_0 + \sum_{i=1}^p \phi_i y_{t-i} + \epsilon_t$$
*Linear combination of past values (autoregressive model).*

$$\hat{\beta} = \arg\min_\beta \left( \sum_{t=1}^T (y_t - x_t^\top \beta)^2 + \lambda \sum_{j=1}^p |\beta_j| \right)$$
*L1 penalty shrinks coefficients to zero for feature selection (LASSO).*

$$h_t = (1 - z_t) \odot h_{t-1} + z_t \odot \tilde{h}_t$$
*Gated balance between old state and candidate activation (GRU update).*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| EPF | Electricity price forecasting — predicting future electricity market prices. |
| DAM | Day-ahead market — trades scheduled one day before delivery, relatively stable. |
| IDM | Intra-day market — continuous trading hours before delivery, higher volatility. |
| BM | Balancing market — real-time supply-demand matching, most volatile. |
| AR / ARIMA | Autoregressive models — predict using past values and error terms. |
| GARCH | Generalized autoregressive conditional heteroscedasticity — models changing volatility over time. |
| LASSO | Least absolute shrinkage and selection operator — linear regression with L1 penalty for feature selection. |
| LEAR | Lasso-estimated autoregressive model — AR with elastic net regularization. [Think: sparse + robust] |
| RF | Random forest — ensemble of decision trees averaging predictions. |
| XGB | Extreme gradient boosting — sequential tree ensemble correcting previous errors. |
| LSTM | Long short-term memory — recurrent network with gates to remember long sequences. |
| GRU | Gated recurrent unit — simpler LSTM variant with fewer gates. |
| MAPE | Mean absolute percentage error — percentage error metric that fails near zero values. |

## Critical Citations

- [Weron, 2014] — Seminal electricity price forecasting review establishing statistical baselines.
- [Lago et al., 2021] — State-of-the-art benchmark for day-ahead forecasting with open dataset.
- [Uniejewski et al., 2016] — Introduced LEAR model that dominates balancing market forecasting.

## Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper's comparative review of forecasting algorithms directly informs Odin's spending forecasting module selection. The finding that LEAR outperforms complex DL models in volatile, data-sparse environments (balancing market) justifies using regularized linear models for cold-start or sparse user spending data. The paper's analysis of evaluation metrics (MAPE's failure near zero) guides Odin's choice of MAE or sMAPE for spending forecast evaluation. The observation that simpler models avoid overfitting in high-volatility contexts supports Odin's algorithm selection for users with short transaction histories.

**Directly justifies:**

- "Regularized AR models (LEAR) outperform LSTM and GRU in volatile, data-sparse markets by avoiding overfitting."
- "MAPE is unreliable when values approach zero; MAE or sMAPE are preferred for sparse or near-zero spending periods."
- "Hybrid CNN-LSTM architectures capture both local patterns and sequential dependencies, improving forecast accuracy."
- "XGB and LGBM balance accuracy and computational cost, making them suitable for mobile deployment with moderate data volumes."

**Limits of relevance:**

- Domain is electricity prices, not personal spending; volatility patterns and seasonality differ.
- No user behavior or cultural spending factors considered.
- No mobile-specific constraints (latency, battery, offline operation) analyzed.
- Cold-start problem (new users with no history) is not explicitly addressed.

## Limitations

- Focuses only on point forecasting, not probabilistic forecasts that provide uncertainty bounds. [unacknowledged]
- No standard benchmark for intra-day or balancing markets — results are not directly comparable across studies.
- MAPE is widely used despite known flaws; the review critiques it but does not propose a unified alternative.
- Discussion of data sparsity in balancing markets is relevant but no specific cold-start solution is offered. [unacknowledged]
- Computational cost comparisons between models are qualitative; no runtime benchmarks are provided.

## Remember This

- 🔑 **LEAR beats LSTM** in volatile, sparse data — overfitting is the enemy for short transaction histories.
- 📌 MAPE fails when values near zero — use MAE or sMAPE for spending forecasts with zero-spending months.
- 💡 Hybrid CNN-LSTM captures local + sequential patterns — best for day-ahead (longer forecast horizon).
- ⚠️ No cold-start evaluation — Odin's new users need special handling beyond standard forecasting models.
- 🧠 XGB balances accuracy and speed — a strong candidate for mobile deployment with moderate data.
