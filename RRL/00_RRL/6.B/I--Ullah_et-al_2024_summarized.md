# Short-Term Load Forecasting: A Comprehensive Review and Simulation Study With CNN-LSTM Hybrids Approach

## Metadata

```yaml
---
paper_id: "10.1109/ACCESS.2024.3440631"
designation: algorithm-specific
title: "Short-Term Load Forecasting: A Comprehensive Review and Simulation Study With CNN-LSTM Hybrids Approach"
authors: "Ullah, K.; Ahsan, M.; Hasanat, S. M.; Haris, M.; Yousaf, H.; Raza, S. F.; Tandon, R.; Abid, S.; Ullah, Z."
year: 2024
venue: "IEEE Access"
odin_topics: ["6.A", "6.B"]
shorthand_tags: ["/forecasting-methods-survey", "/temporal-dependency", "/forecast-algo-candidates", "/forecast-algo-comparison", "/forecast-algo-tradeoffs", "/forecast-eval-metrics"]
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

Hybrid CNN-LSTM model achieves superior short-term load forecasting accuracy (RMSE 538.71, MAPE 2.72% single-step) by combining CNN feature extraction with LSTM temporal sequencing.

## Problem and Motivation

Accurate short-term load forecasting (STLF) is critical for power grid stability and economic reserve management, yet existing models struggle with nonlinearities, non-stationarity, and high-dimensional inputs. The problem matters because forecasting errors directly increase operating costs and risk grid instability. Prior work lacked a comprehensive, comparative evaluation of statistical, intelligent, and hybrid methods alongside a validated CNN-LSTM hybrid on real grid data.

## Approach

- Dataset: Pakistan NTDC national grid, hourly data Jan 2019–May 2023; AEP dataset for external validation.
- Preprocessing: outlier detection via IQR (Q1-1.5×IQR, Q3+1.5×IQR), holiday/weekend binary encoding, 17 input features (hour, month, weekday, load lags, etc.).
- Model: Three 1D CNN blocks (48→32→16 filters, kernel size 3, ReLU) for feature extraction, followed by three LSTM layers (20 units each) for temporal dependencies, then concatenation and dense output layer.
- Training: 70/30 train-validation split; Adam optimizer; MAE loss; dropout 0.25 for regularization.
- Evaluation: RMSE, MAE, MAPE for single-step and 24-hour-ahead forecasting.

## Findings

1. Single-step forecast on NTDC: **RMSE 538.71, MAE 371.97, MAPE 2.72** — substantially better than reference [79] (RMSE 1038.04, MAPE 5.35).
2. 24-hour forecast on NTDC: RMSE 951.94, MAE 656.35, MAPE 4.72 — outperforming both [79] and [55].
3. On AEP dataset: single-step RMSE 126.35, MAE 94.27, MAPE 0.64; 24-hour RMSE 702.97, MAPE 3.39.

- LSTM layers capture long-term temporal dependencies that statistical models (ARIMA, SARIMA) miss due to stationarity assumptions.
- CNNs effectively extract local patterns (trends, periodicities) from high-dimensional time series inputs.

## Key Figures and Tables

- Figure 18: Actual vs. predicted load over Dec 2020–Apr 2021 → Predicted load (red) closely mirrors actual (black) across all fluctuations.
- Figure 19: Comparison with reference model → Proposed model’s predictions (red) track actual load far better than reference method (blue).
- Table 8: Single-step performance comparison → Proposed model RMSE 538.71 vs. reference [79] 1038.04 on NTDC.
- Table 9: 24-hour performance comparison → Proposed model MAPE 4.72 vs. [55] 6.16.
- Figure 15: Feature correlation heatmap → Hour of day and load lag have strongest correlation with current load.

## Key Equations

$$Y(t) = c + \phi_1 Y(t-1) + \phi_2 Y(t-2) + \dots + \phi_p Y(t-p) + \varepsilon(t)$$
*AR(p) model: current value depends linearly on past p values plus error.*

$$(1 - B)^d Y(t) = c + \phi_1 (1-B)^d Y(t-1) + \dots + \phi_p (1-B)^d Y(t-p) + \varepsilon(t) - \psi_1 \varepsilon(t-1) - \dots - \psi_q \varepsilon(t-q)$$
*ARIMA(p,d,q): integrates differencing to make non-stationary series stationary.*

$$\text{Gini Impurity} = 1 - \sum (\pi_i)^2$$
*Decision tree split criterion: lower values mean purer class separation.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| STLF | Short-term load forecasting — predicting electricity demand hours to days ahead. |
| CNN | Convolutional neural network — extracts local patterns (like edges in images, trends in time series). |
| LSTM | Long short-term memory [think: memory cell that learns what to forget and remember over long sequences] — captures long-range dependencies in sequential data. |
| ARIMA | Autoregressive integrated moving average — statistical model for non-stationary time series after differencing. |
| SARIMA | Seasonal ARIMA — extends ARIMA with seasonal components (daily/weekly cycles). |
| MAPE | Mean absolute percentage error — average forecast error as percentage of actual values. |
| RMSE | Root mean square error — penalizes large errors more heavily than MAE. |
| MAE | Mean absolute error — average absolute difference between predicted and actual. |
| IQR | Interquartile range (Q3-Q1) — used to detect outliers as points beyond 1.5×IQR from quartiles. |
| ReLU | Rectified linear unit — activation function that outputs zero for negative inputs, identity for positives. |

## Critical Citations

- [Rafi et al., 2021] — Baseline integrated CNN-LSTM model for STLF; this paper directly compares and outperforms it.
- [Alhussein et al., 2020] — Reference hybrid CNN-LSTM for household load; used as performance benchmark.
- [Tarmanini et al., 2023] — Comparative study of ARIMA vs. ANN for STLF; informs statistical baseline selection.

## Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

**Contribution to Odin:**

This paper directly informs Odin’s spending forecasting module by providing a rigorous, comparative evaluation of time series forecasting methods — from statistical (ARIMA, SARIMA) to intelligent (SVM, RF, MLP) to hybrid (CNN-LSTM). Although the domain is electrical load, the methodological findings transfer directly to predicting sequential spending data: CNN layers extract local spending patterns (e.g., weekly cycles), and LSTM layers capture long-term behavioral drift. The demonstrated superiority of CNN-LSTM over pure LSTM or statistical models on irregular, high-dimensional sequential data justifies Odin’s selection of a hybrid architecture for per-category spending prediction. The paper’s evaluation metrics (RMSE, MAE, MAPE) and preprocessing techniques (outlier detection via IQR, cyclical feature encoding) are directly adoptable for Odin’s algorithm performance measurement and data pipeline.

**Directly justifies:**

- "Hybrid CNN-LSTM reduces single-step forecasting MAPE to 2.72% compared to 5.35% for LSTM-only models — sequential feature extraction combined with temporal memory outperforms either alone."
- "ARIMA and SARIMA models assume stationarity and linearity, making them unsuitable for spending data with non-stationary behavioral shifts and nonlinear category interactions."
- "Outlier detection using IQR (Q1-1.5×IQR, Q3+1.5×IQR) effectively identifies anomalous load values; same method applies to spending anomaly detection in cold-start profiles."
- "Hour, day-of-week, and holiday encodings as categorical features significantly improve forecast accuracy — analogous temporal features (payday cycles, weekend spending) are essential for Odin’s forecasting inputs."

**Limits of relevance:**

- Domain mismatch: electrical load forecasting vs. personal spending forecasting — spending patterns have different volatility drivers (income, obligations, discretionary choice).
- Data scale and frequency: NTDC hourly grid data is high-frequency and macro-level; Odin uses sparse, user-entered transaction data (often daily or weekly).
- No evaluation on cold-start profiles or sparse user activity — the model assumes dense historical sequences.
- Filipino cultural spending patterns (family obligations, 13th month, etc.) are not considered; the algorithm’s feature set would need adaptation.
- Paper assumes no missing data (after outlier replacement); Odin’s manual entry inherently creates irregular gaps.

## Limitations

- Study exclusively uses power grid data; no validation on financial transaction sequences. [unacknowledged]
- Outlier handling replaces anomalies with mean values — this would mask genuine anomalous spending that Odin must detect. [unacknowledged]
- Model complexity (three CNN blocks, three LSTM layers) may be overkill for mobile deployment with limited compute and battery.
- No probabilistic forecasting (quantiles, confidence intervals) — Odin may need uncertainty estimates for budget alerts. (Acknowledged as future work in conclusion.)
- Authors treat all national holidays uniformly — personal finance calendars are more nuanced (e.g., holiday spending spikes vs. utility load dips).

## Remember This

- 🔑 **CNN-LSTM cut MAPE by half** — 2.72% vs 5.35% for LSTM-only on single-step forecasting.
- 📌 IQR outlier detection (1.5×IQR rule) works — same formula applies to spending anomaly flags.
- 💡 Temporal features (hour, weekday, holiday) boost accuracy — Odin must encode payday cycles and local holidays.
- ⚠️ Power grid ≠ personal spending — transfer the method, not the domain assumptions.
- 🔍 No cold-start evaluation — unknown how hybrid model performs for users with <1 month of transaction history.
