# Deep learning-based time series forecasting

## Metadata

```yaml
---
paper_id: "10.1007/s10462-024-10989-8"
designation: international
title: "Deep learning-based time series forecasting"
authors: "Song, X.; Deng, L.; Wang, H.; Zhang, Y.; He, Y.; Cao, W."
year: 2025
venue: "Artificial Intelligence Review"
odin_topics: ["D.1", "D.2"]
shorthand_tags: ["/forecasting-methods", "/spending-time-series", "/temporal-dependency", "/lstm-architecture", "/lstm-vs-alternatives", "/lstm-spending-applied"]
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

Complex deep learning time series forecasting models often underperform simpler linear models due to overfitting and inability to effectively use sequential order information.

## Problem and Motivation

Deep learning time series forecasting models have exploded since 2014, but no systematic review has experimentally compared their ability to capture time-step dependencies, variable correlations, and sequential order. Accurate forecasting is critical for energy, traffic, weather, and finance applications, yet model complexity often introduces overfitting and noise sensitivity. Prior surveys lacked controlled experiments across multiple architectures and datasets to reveal why complex models fail relative to simpler alternatives.

## Approach

- Reviews 10 years (2014–2024) of deep learning forecasting models, categorized by: time-step dependency mining (RNN, LSTM, GRU, Transformer, TCN), variable correlation mining (TFT, Aliformer, Crossformer), and long-term optimization (sparse attention, patch slicing).
- Evaluates models on 5 multivariate datasets (ETTh1, Electricity, Exchange, Traffic, ILI) and univariate versions, using input length 96 (36 for ILI) and output lengths 48, 96, 336 (12,24,48 for ILI).
- Metrics: MAE, MSE, MAPE, R². Implements simple time split and sliding window validation (window = 1/10 dataset length for Exchange).
- Runs two diagnostic experiments: (1) input shuffling to test sequential order sensitivity, (2) varying lookback window (48→192) to detect overfitting and noise interference.
- Compares 15+ models including ARIMA, CNN-1D, LSTM, GRU, LSTnet, Transformer, LogTrans, Reformer, Informer, Autoformer, Fedformer, ETSformer, DLinear, PatchTST, Crossformer, NS-Transformer.

## Findings

1. **DLinear beats most Transformer-based models** on ETTh1, Exchange, and Electricity datasets despite using only linear layers (e.g., on ETTh1 at O=336, DLinear MAE 0.4301 vs Fedformer 0.4445).
2. Shuffling the input sequence drops **PatchTST's MAE by 50.32%** on ETTh1 – the largest decline among all models – proving its strong reliance on temporal order.
3. Complex models (Autoformer, TDformer) show **minimal change or even improvement** after shuffling (TDformer MSE improves 33.87% on Exchange), indicating they fail to use sequential information.
4. Extending lookback from 48 to 192 worsens accuracy for Autoformer, ETSformer, and TDformer, but **PatchTST improves** (ETTh1 MAE 0.4454→0.4357).
5. On an artificial dataset with explicit trend and season terms, Fedformer achieves best trend MAE (0.0612) and season MAE (0.0823), outperforming time-domain methods.

## Key Figures and Tables

- Table 5: Multivariate forecasting results → DLinear and PatchTST dominate on ETTh1, Exchange, and Traffic.
- Table 7: Shuffling experiment → PatchTST shows largest accuracy drop; TDformer often improves after shuffling.
- Table 8: Lookback window sensitivity → Complex models peak at shortest window; PatchTST improves with longer window.
- Table 9: Trend and season prediction on artificial data → Fedformer best for both terms; N-BEATS worst.
- Figure 18: Trend term prediction plots → Fedformer tracks true trend closely; ETSformer oscillates erratically.

## Key Equations

$$ \text{Attention}(Q,K,V) = \text{Softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V $$
*Attention computes query-key similarity to weight values for capturing time-step dependencies.*

$$ f_t = \sigma(W_{xf}x_t + W_{hf}h_{t-1} + b_f) $$
*LSTM forget gate decides which past information to discard, mitigating vanishing gradient.*

$$ \hat{x} = \gamma\left(\frac{x - \mu}{\sqrt{\sigma^2 + \epsilon}}\right) + \beta $$
*RevIN normalizes input with learnable affine parameters to reduce non-stationarity.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LSTM | Long Short-Term Memory [think: cell state with three gates to remember or forget]. |
| GRU | Gated Recurrent Unit – simplified LSTM with two gates. |
| TCN | Temporal Convolutional Network – CNN with dilated causal convolutions to expand receptive field. |
| MAE | Mean Absolute Error – average absolute prediction error. |
| MSE | Mean Squared Error – penalizes large errors more heavily. |
| Patch | Short fixed-length segment of a time series treated as one token. |
| Lookback window | Number of past time steps used as input to forecast future values. |
| Trend term | Long-term directional movement in a time series. |
| Seasonal term | Regular, repeating pattern with fixed period (e.g., daily, weekly). |
| RevIN | Reversible Instance Normalization – standardizes then restores non-stationary statistics. |

## Critical Citations

- [Vaswani et al., 2017] — Transformer attention mechanism, foundation for most modern forecasting models.
- [Shi et al., 2015] — LSTM applied to sequence forecasting, source of gating equations.
- [Wu et al., 2021] — Autoformer, introduces auto-correlation for seasonal pattern extraction.

## Relevance to Odin

**Topics:**

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

**Contribution to Odin:**

This systematic review directly supports Odin’s spending forecasting module by comparing LSTM against GRU, Transformers, and simple linear models across multiple time series domains. The finding that DLinear (a single linear layer) often beats complex models warns Odin’s team not to default to LSTM without testing simpler baselines. The shuffling experiment provides a diagnostic method to verify that Odin’s chosen model actually uses temporal order – a critical requirement for spending prediction. The observation that complex models overfit on longer lookback windows informs Odin’s design: with sparse manual transaction data, a simpler model may generalize better than an LSTM.

**Directly justifies:**

- "LSTM's gating mechanism mitigates vanishing gradient and captures long-term temporal correlations in sequential data, but simpler linear models can outperform LSTM on certain datasets, requiring empirical validation."
- "Shuffling the input time series and measuring prediction accuracy drop is a valid method to test whether a model truly leverages sequential order – a property essential for spending forecasting."
- "Extending the lookback window from 48 to 192 time steps degrades accuracy for Transformer-based models (Autoformer, ETSformer) due to overfitting and noise, suggesting that for small mobile datasets, shorter windows may be optimal."
- "Patch-based attention (PatchTST) reduces computational complexity while improving long-term accuracy, offering a potential alternative to LSTM for mobile deployment where resources are constrained."

**Limits of relevance:**

- Experiments use energy, traffic, exchange, and illness data – not personal spending transactions from Filipino young professionals.
- All datasets are dense, regularly sampled time series; Odin’s manual input produces sparse, irregular data, which may change model rankings.
- Computational complexity comparisons do not simulate mobile hardware constraints (battery, CPU).
- The review does not evaluate cold-start performance, which is critical for new Odin users with no spending history.

## Limitations

- Acknowledges that complex models (Autoformer, Fedformer, ETSformer) overfit and are noise-sensitive, explaining their poor performance relative to DLinear.
- Acknowledges that most Transformer-based models cannot handle flexible input/output lengths without retraining.
- [Unacknowledged] Does not test any model on personal finance or spending data, limiting direct applicability to Odin.
- [Unacknowledged] All experiments use fixed lookback windows; no evaluation of streaming or incremental learning scenarios.
- [Unacknowledged] No analysis of model robustness to missing values or irregular sampling intervals, which are typical in manual transaction logging.

## Remember This

- 🔑 Shuffling input drops PatchTST's MAE by **50%** on ETTh1 – temporal order is vital for forecasting.
- 📌 Autoformer and TDformer show **<2% MAE change** after shuffling – they ignore sequential structure.
- 💡 DLinear beats Transformers on 3 of 5 datasets – simpler can be better, test baselines before LSTM.
- ⚠️ Longer lookback windows hurt Autoformer but help PatchTST – overfitting is real; validate window size empirically.
- 🧠 Fedformer excels at extracting trend (MAE 0.0612) and season (MAE 0.0823) via frequency-domain attention.
