# A Predictive Framework for Annual Financial Planning using Deep Learning Models

## Metadata

```yaml
---
paper_id: "3d4e5f6a-7b8c-5d9e-8f0a-1b2c3d4e5f6a"
designation: algorithm-specific
title: "A Predictive Framework for Annual Financial Planning using Deep Learning Models"
authors: "Singh, U.; Anand, U.; Singh, V."
year: 2025
venue: "Journal of Scientific Innovation and Advanced Research (JSIAR)"
odin_topics: ["D.1", "D.2"]
shorthand_tags: ["/forecasting-methods", "/spending-time-series", "/temporal-dependency", "/lstm-vs-alternatives", "/lstm-spending-applied", "/lstm-justification"]
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[ ]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
---
```

## TL;DR

LSTM achieved **7.02% MAPE**, outperforming GRU (7.48%) and RNN (9.85%) on annual expense forecasting.

## Problem and Motivation

Traditional forecasting methods (ARIMA, linear regression, exponential smoothing) fail to capture non-linear and dynamic patterns in financial data, limiting prediction accuracy. Accurate annual expense forecasting is critical for fiscal discipline, resource allocation, and risk mitigation. Prior work focused on short-term predictions; no comprehensive deep learning comparison existed for long-term annual forecasting in financial planning contexts.

## Approach

- **Data**: Government expenditure portals and enterprise datasets, augmented with synthetic data (Gaussian/exponential distributions).
- **Preprocessing**: Missing values imputed (forward-fill, mean substitution); min-max normalization; sliding window with 12-month lookback.
- **Models**: RNN (baseline), LSTM, and GRU — implemented in TensorFlow/Keras.
- **Hyperparameters**: Grid search + Bayesian optimization for learning rate, batch size, hidden layers, dropout.
- **Training split**: 70% train, 15% validation, 15% test (temporal split to preserve chronology).
- **Evaluation metrics**: MAE, RMSE, and MAPE.

## Findings

1. LSTM achieved the lowest error across all metrics: **MAE 1872.56**, RMSE 2614.32, and **MAPE 7.02%**.
2. GRU performed second: MAE 1950.45, RMSE 2701.25, MAPE 7.48%.
3. RNN performed worst: MAE 2450.13, RMSE 3120.88, MAPE 9.85%.
- LSTM and GRU mitigated vanishing gradient problems; RNN suffered instability.
- Deep learning models captured seasonal variations and long-term dependencies that traditional methods miss.

## Key Figures and Tables

- Table II: Model performance comparison (MAE, RMSE, MAPE) → LSTM best across all three metrics.
- Figure 4: Actual vs. predicted expenses (LSTM) → LSTM forecasts closely follow true spending trend.
- Figure 5: Training and validation loss curves → Smooth convergence, no overfitting.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LSTM | Long Short-Term Memory [think: memory cell with forget/input/output gates that learns what to keep and discard]. |
| GRU | Gated Recurrent Unit [think: simplified LSTM with update and reset gates, fewer parameters]. |
| RNN | Recurrent Neural Network [think: simple loop that suffers vanishing gradient on long sequences]. |
| ARIMA | Autoregressive Integrated Moving Average [think: classical statistical model for trend+seasonality]. |
| MAE | Mean Absolute Error — average absolute difference between predicted and actual values. |
| RMSE | Root Mean Squared Error — penalizes larger errors more than MAE. |
| MAPE | Mean Absolute Percentage Error — error as percentage of actual values. |

## Critical Citations

- [Hochreiter & Schmidhuber, 1997] — Introduced LSTM architecture that solves the vanishing gradient problem.
- [Cho et al., 2014] — Proposed GRU as a computationally efficient alternative to LSTM.
- [Siami-Namini et al., 2019] — Prior benchmark showing LSTM outperforms ARIMA on financial time series.

## Relevance to Odin

**Topics:**

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

**Contribution to Odin:**

This paper directly informs Odin's spending forecasting module by providing empirical evidence that LSTM outperforms GRU and RNN on financial expense time series. The reported 7.02% MAPE on annual data supports Odin's design decision to select LSTM over alternative recurrent architectures. Although the study uses organizational budgeting data rather than personal finance, the methodological comparison (LSTM vs GRU vs RNN) and the handling of temporal dependencies with a 12-month lookback window map directly to Odin's sequential spending prediction problem.

**Directly justifies:**

- "LSTM achieved 7.02% MAPE on annual expense forecasting, significantly outperforming GRU (7.48%) and RNN (9.85%)."
- "LSTM captures long-term dependencies and seasonal patterns in financial time series that traditional methods (ARIMA, linear regression) cannot model effectively."
- "GRU offers comparable accuracy to LSTM with lower computational cost, making it a viable alternative for mobile deployment where resources are constrained."
- "Traditional statistical forecasting methods degrade in the presence of irregular spending patterns and volatility, whereas deep learning models maintain robustness."

**Limits of relevance:**

- Study uses organizational/enterprise financial data, not individual consumer spending; spending patterns differ in scale and volatility.
- Population is Indian, not Filipino; cultural spending behaviors and income typology may differ.
- Focus on annual forecasting; Odin requires monthly or weekly per-category forecasts, which may have different temporal dynamics.
- Data assumptions include high-quality, complete datasets; Odin relies on manual user input, which is sparser and noisier.
- No evaluation of cold-start performance (new users with no spending history).

## Limitations

- Framework depends on high-quality, clean datasets; incomplete or noisy financial data may degrade performance [unacknowledged].
- Performance may vary with different forecasting horizons (monthly, quarterly) — not evaluated [unacknowledged].
- Models are sensitive to overfitting on small datasets; careful tuning required.
- Synthetic data augmentation may not reflect real-world noise patterns in Philippine personal finance contexts.
- No comparison with Transformer-based architectures (e.g., Informer, Temporal Fusion Transformer) that now represent state-of-the-art in time series forecasting [unacknowledged].

## Remember This

- 🔑 LSTM achieved **7.02% MAPE** — beats GRU (7.48%) and RNN (9.85%) on annual expense forecasting.
- 📌 LSTM captures long-term dependencies; GRU is lighter but slightly less accurate.
- ⚠️ Study uses organizational data — not individual consumer spending. Validate before citing for personal finance.
- 💡 12-month lookback window mirrors Odin's sequential design for spending forecasting.
- 🧠 Traditional models (ARIMA, linear regression) degrade on irregular spending — deep learning is more robust.