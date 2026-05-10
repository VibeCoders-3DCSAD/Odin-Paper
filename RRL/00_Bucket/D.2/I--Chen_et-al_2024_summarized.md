# A Survey of Time Series Data Forecasting Methods Based on Deep Learning

## Metadata

```yaml
---
paper_id: "10.56557/jobari/2024/v30i69014"
designation: international
title: "A Survey of Time Series Data Forecasting Methods Based on Deep Learning"
authors: "Chen, J.; Chen, T.; Wang, Y.; Wang, L."
year: 2024
venue: "Journal of Basic and Applied Research International"
odin_topics: ["D.1", "D.2"]
shorthand_tags: ["/forecasting-methods", "/spending-time-series", "/temporal-dependency", "/lstm-architecture", "/lstm-vs-alternatives", "/lstm-spending-applied", "/lstm-justification"]
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

Deep learning models (RNN, LSTM, GRU, Transformer) outperform traditional methods on time series forecasting, with no single model dominating across all datasets.

## Problem and Motivation

Traditional machine learning and statistical models struggle with massive time series data due to manual feature engineering and structural assumptions. Deep learning can automatically extract temporal patterns with minimal preprocessing. A comprehensive comparison of deep learning forecasting methods was missing across diverse public datasets.

## Approach

- **Data sources**: ETT (transformer oil temperature), ECL (electricity consumption), Traffic (road occupancy), Weather (21 meteorological indicators), ILI (influenza), TE (chemical process).
- **Models compared**: RNN, LSTM, GRU, Transformer, and LSTM-RNN hybrid.
- **Experimental setup**: Input sequence length = 24, prediction length = 1; Adam optimizer; PyTorch implementation.
- **Evaluation metrics**: MSE (mean squared error) and MAE (mean absolute error).
- **Datasets excluded** from final comparison: ILI and TE due to insufficient periodicity, seasonality, or data volume.

## Findings

1. Transformer achieved **lowest MSE (3.418) and MAE (1.399)** on ETTm2 dataset.
2. LSTM achieved minimum MAE on Electricity (1.848) and Traffic (0.020).
3. GRU achieved minimum MSE on Electricity (19.524) and Traffic (0.00110).
4. RNN achieved best performance on Weather (MSE=0.007, MAE=0.060).
- LSTM-RNN hybrid generally outperformed standard RNN and showed better results than ordinary LSTM on ETTm2 and Weather.
- No single model dominates across all datasets; performance depends on data characteristics.

## Key Figures and Tables

- Figure 10: Prediction curves on ETTm2 → Transformer fits closest to actual (blue) vs. predicted (red).
- Figure 11: Prediction curves on Electricity → LSTM and GRU track actual values more closely than RNN.
- Table 1: Univariate prediction performance comparison → numeric MSE/MAE for all five models across four datasets.

## Key Equations

$$MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$
*Average squared prediction error; penalizes large errors more heavily.*

$$MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|$$
*Average absolute error; robust to outliers.*

$$h_t = f(Wx_t + U h_{t-1} + b)$$
*RNN hidden state depends on current input and previous state.*

$$f_t = \sigma(W_f [h_{t-1}, x_t] + b_f)$$
*LSTM forget gate decides what to discard from cell state (0=discard, 1=keep).*

$$\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$
*Self-attention computes weighted sum of values based on query-key similarity.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| TSF | Time Series Forecasting — predicting future values from historical data. |
| RNN | Recurrent Neural Network — processes sequences by maintaining a hidden state; suffers from vanishing gradients. |
| LSTM | Long Short-Term Memory [think: three gates (forget, input, output) control what to remember] — RNN variant that solves vanishing gradient. |
| GRU | Gated Recurrent Unit [think: simpler LSTM with two gates (update, reset)] — computationally efficient alternative to LSTM. |
| Transformer | Deep learning architecture using self-attention instead of recurrence; excels at long-range dependencies. |
| MSE | Mean Squared Error — average of squared differences between predicted and actual values. |
| MAE | Mean Absolute Error — average of absolute differences between predicted and actual values. |
| ETT | Electricity Transformer Temperature — minute-level oil temperature data from Chinese power grid. |

## Critical Citations

- [Hochreiter & Schmidhuber, 1997] — Original LSTM paper that introduced gating mechanisms to solve vanishing gradient. [Citation inferred from text: Gers et al. 2000 builds on this]
- [Vaswani et al., 2017] — Introduced Transformer architecture with self-attention, foundational for modern time series forecasting.
- [Gers et al., 2000] — Extended LSTM with forget gate, enabling continual learning without memory overflow.
- [Abdel-Nasser & Mahmoud, 2019] — Applied LSTM-RNN to photovoltaic power forecasting, demonstrating deep learning's utility in energy domains.

## Relevance to Odin

**Topics:**

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

**Contribution to Odin:**

This survey provides direct benchmark evidence for Odin's spending forecasting module by comparing LSTM against RNN, GRU, and Transformer across multiple public time series datasets. The finding that no single model dominates all datasets justifies Odin's empirical model selection approach rather than assuming LSTM is universally optimal. The explicit performance metrics (MSE, MAE) on energy and traffic data offer a baseline expectation for forecasting accuracy in similar univariate settings, which can inform Odin's performance targets despite the domain difference from personal spending.

**Directly justifies:**

- "LSTM achieved the lowest MAE on Electricity (1.848) and Traffic (0.020) datasets compared to RNN, GRU, and Transformer, demonstrating competitive univariate forecasting performance."
- "Transformer achieved the lowest MSE (3.418) and MAE (1.399) on ETTm2, but its performance degraded on Weather (MSE=0.827), showing that model superiority is dataset-dependent."
- "GRU achieved the minimum MSE on Electricity (19.524) and Traffic (0.00110), offering a computationally cheaper alternative to LSTM with comparable or better error metrics."
- "The LSTM-RNN hybrid generally outperformed standard RNN and showed better results than ordinary LSTM on ETTm2 and Weather, suggesting hybrid architectures may improve forecasting stability."
- "No single deep learning model dominates across all time series forecasting tasks; algorithm selection must be guided by data characteristics and empirical validation."

**Limits of relevance:**

- Domains tested are energy, traffic, and weather — not personal finance or spending behavior.
- All datasets are high-frequency sensor measurements (minutes to hours), unlike daily/weekly spending transactions.
- No evaluation on sparse, irregular, or human-initiated transaction sequences typical of personal budgeting.
- Models were evaluated only on univariate forecasting (single variable), whereas Odin forecasts per-category spending which may be multivariate.

## Limitations

- Survey does not propose novel methods; findings are aggregations of existing literature and limited experiments.
- Experimental comparison used only univariate forecasting with fixed input length (24) and prediction length (1), which may not generalize to longer horizons. [unacknowledged]
- No statistical significance testing (e.g., p-values) reported for model comparisons.
- Datasets are all from sensor/industrial domains; no financial or consumer spending data included. [unacknowledged]
- Transformer performance on Weather (MSE=0.827) was dramatically worse than RNN (0.007), but paper does not explain why.

## Remember This

- 🔑 Transformer best on ETTm2 (MSE **3.418**) — but fails badly on Weather (MSE 0.827 vs RNN's 0.007).
- 📌 LSTM wins on Electricity (MAE 1.848) and Traffic (MAE 0.020) — strong for univariate sequences.
- 💡 GRU matches or beats LSTM on two of four datasets — cheaper model may suffice.
- ⚠️ No single deep learning model dominates all time series — Odin must validate empirically.
- 🔍 Survey excludes personal finance data — benchmark numbers are directional, not directly transferable.