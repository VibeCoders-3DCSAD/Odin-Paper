# Performance analysis of neural network architectures for time series forecasting: A comparative study of RNN, LSTM, GRU, and hybrid models

## Metadata

```yaml
---
paper_id: "f3d8c2a1-6b7e-4d9f-8c5a-2e7b1d4f9a3c"
designation: algorithm-specific
title: "Performance analysis of neural network architectures for time series forecasting: A comparative study of RNN, LSTM, GRU, and hybrid models"
authors: "Yunita, A.; Pratama, M. I.; Almuzakki, M. Z.; Ramadhan, H.; Akhir, E. A. P.; Mansur, A. B. F.; Basori, A. H."
year: 2025
venue: "MethodsX"
odin_topics: ["6.A", "6.B", "12.B"]
shorthand_tags: ["/forecasting-methods-survey", "/forecast-algo-candidates", "/forecast-algo-comparison", "/forecast-algo-tradeoffs", "/forecast-eval-metrics", "/eval-ml-design", "/eval-limitations"]
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

No statistically significant difference among nine RNN architectures (p=.127), but LSTM-based hybrids consistently outperform standalone models across three real-world datasets.

## Problem and Motivation

Random weight initialization causes variability in neural network performance, making single-run evaluations unreliable for time series forecasting. Existing hybrid model proposals (e.g., RNN-LSTM, LSTM-GRU) are often trained only once, leaving their stability and comparative advantages unquantified. No prior benchmark had systematically compared nine architectures using Monte Carlo simulation to account for initialization randomness.

## Approach

- **Datasets**: Sunspot activity (3,625 monthly records, 1749–2018), Indonesian COVID-19 daily cases (634 days), dissolved oxygen readings from an oil/gas plant (1,033 daily records).
- **Architectures**: 9 models — vanilla RNN, LSTM, GRU, plus six hybrids (RNN-LSTM, RNN-GRU, LSTM-RNN, GRU-RNN, LSTM-GRU, GRU-LSTM) — all with two hidden layers and comparable parameter counts.
- **Evaluation protocol**: Monte Carlo simulation with 100 independent runs per model, each trained for 100 epochs; 95% confidence intervals with 2.5% trimming.
- **Metrics**: MAE, MAPE, RMSE (error) plus computation time; Friedman test for statistical comparison across architectures.

## Findings

1. **Friedman test showed no statistically significant difference** among nine architectures (χ² = 12.593, df = 8, p = .127).
2. **LSTM-GRU achieved the lowest mean rank (2.23)** across all datasets; vanilla RNN had the highest mean rank (8.57).
3. **LSTM-RNN performed best on sunspot (MAE=16.96, RMSE=23.39)** and oxygen datasets (MAE=2.97, MAPE=7.42%, RMSE=4.04).
4. **Standalone LSTM was best for COVID-19 forecasting** (MAE=0.90, MAPE=9.04%, RMSE=1.16), beating hybrids on percentage error.
5. **Vanilla RNN had fastest training (<20s per iteration) but highest errors** — e.g., sunspot MAPE=50.94% vs. LSTM-RNN’s 37.28%.

- Hybrid models generally had slightly longer training times but more stable predictions (narrower boxplot spreads).

## Key Figures and Tables

- Table 3: Performance metrics (MAE, RMSE, MAPE) for all nine models across three datasets → LSTM-GRU and LSTM-RNN consistently rank top 2.
- Figure 4: Sunspot error boxplots → LSTM-GRU has lowest median MAE (16.88) and narrowest spread; RNN shows largest errors and outliers.
- Figure 6: COVID-19 error boxplots → LSTM achieves smallest MAPE spread (∼9%) and best median; RNN shows wide variance.
- Figure 8: Oxygen error boxplots → LSTM-RNN has lowest median MAPE (7.42%) and tightest distribution; RNN’s spread is largest.

## Key Equations

$$MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|$$
*Average absolute prediction error in original units.*

$$MAPE = \frac{100}{n}\sum_{i=1}^{n}\left|\frac{y_i - \hat{y}_i}{y_i}\right|$$
*Percentage error — scale‑free, good for comparing datasets of different magnitudes.*

$$RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}$$
*Root mean squared error — penalizes large errors more heavily.*

$$z_t = \sigma(W_{xz}x_t + W_{hz}h_{t-1} + b_z)$$
*GRU update gate: decides how much past information to keep.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| RNN | Recurrent Neural Network — processes sequences by passing a hidden state forward; suffers from short‑term memory. |
| LSTM | Long Short‑Term Memory — RNN variant with a “cell state” and three gates (input, forget, output) that retains information over long sequences. |
| GRU | Gated Recurrent Unit — RNN variant with two gates (update, reset); simpler and faster than LSTM. |
| Monte Carlo simulation | Running the same model 100 times with different random initializations to measure performance stability. |
| Friedman test | Non‑parametric statistical test that compares multiple models across multiple datasets by ranking their performance. |

## Critical Citations

- [Hochreiter & Schmidhuber, 1997] — Introduced LSTM, the foundation for all LSTM‑based hybrids benchmarked here.
- [Chung et al., 2014] — Empirical comparison of GRU vs. LSTM; this paper extends that work with hybrid architectures.
- [Demšar, 2006] — Establishes the Friedman test as the standard for comparing multiple classifiers over multiple datasets.

## Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly informs Odin’s spending forecasting module by benchmarking nine RNN-family algorithms under controlled, repeatable conditions. The finding that LSTM-based hybrids (especially LSTM-RNN and LSTM-GRU) perform best across diverse temporal patterns justifies their selection for forecasting user spending, where transaction sequences have irregular intervals and varying volatility. The Monte Carlo evaluation protocol — 100 runs to account for random initialization — provides a methodological template for Odin’s own algorithm validation, ensuring that reported performance is not due to lucky weight initializations.

**Directly justifies:**

- “LSTM-RNN hybrid achieves the lowest MAE (2.97) and MAPE (7.42%) on a real‑world sensor time series, outperforming standalone LSTM and GRU.”
- “No statistically significant difference among nine RNN architectures (p=.127) suggests that practical considerations — computational cost and stability — should guide model selection, not just point estimates.”
- “Monte Carlo simulation with 100 iterations reveals that LSTM‑based hybrids have narrower error spreads than standalone RNN, indicating more consistent forecasts under random initialization.”
- “Vanilla RNN’s MAPE on sunspot data (50.94%) is 13 percentage points worse than LSTM‑RNN (37.28%) — a gap that would materially degrade spending forecasts for volatile categories.”

**Limits of relevance:**

- Datasets are non‑financial (sunspots, disease cases, oxygen levels); spending transaction sequences may have different autocorrelation structures.
- All models were evaluated on univariate time series; Odin’s forecasting may benefit from multivariate inputs (e.g., day of week, income timing).
- Training used 100 epochs per run; Odin’s on‑device or cloud training budget may be more constrained.
- No explicit evaluation of cold‑start performance (fewer than 30 transactions), which is critical for new Odin users.

## Limitations

- Only three datasets used — small sample size may have masked true performance differences (paper acknowledges this).
- Friedman test non‑significance could be due to low statistical power, not genuine equivalence. [unacknowledged]
- No hyperparameter tuning — all models used fixed architectures (2 hidden layers, 64 units per layer) — may favor certain models.
- Paper removed outliers by trimming 2.5% from Monte Carlo results; this may discard legitimate extreme forecast errors that matter in budgeting.
- No comparison with traditional statistical baselines (ARIMA, exponential smoothing) — only neural architectures are benchmarked.

## Remember This

- 🔑 **No statistical difference among 9 architectures** — but LSTM‑GRU had lowest mean rank (2.23) across all datasets.
- 📌 **LSTM‑RNN excelled on two of three datasets** — best MAE for sunspot (16.96) and oxygen (2.97).
- 💡 **Vanilla RNN is fastest but least reliable** — MAPE on sunspot was **50.94%** vs. 37.28% for LSTM‑RNN.
- 🔍 **Monte Carlo with 100 runs** — essential to avoid mistaking lucky initialization for good architecture.
