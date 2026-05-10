# Research Progress and Trends of Deep Learning in Stock Price Prediction: A Systematic Review from LSTM to Transformer

## Metadata

```yaml
---
paper_id: "10.1051/itmconf/20268402004"
designation: algorithm-specific
title: "Research Progress and Trends of Deep Learning in Stock Price Prediction: A Systematic Review from LSTM to Transformer"
authors: "Gong, H."
year: 2026
venue: "ITM Web of Conferences"
odin_topics: ["D.1", "D.2"]
shorthand_tags: ["/forecasting-methods", "/spending-time-series", "/lstm-architecture", "/lstm-vs-alternatives", "/lstm-justification"]
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

LSTM dominates short-term prediction with high Sharpe ratios (up to 2.34), Transformer improves long-range accuracy (20–25% error reduction), and LSTM‑Transformer hybrids cut errors by over 50% while boosting interpretability.

## Problem and Motivation

Traditional linear models (ARIMA, GARCH) and early machine learning methods fail to capture the non‑linear, non‑stationary dynamics of financial time series. Deep learning models like LSTM and Transformer offer superior temporal dependency modeling, yet no systematic review traces their evolution from recurrent architectures to hybrid and multimodal systems. This gap leaves researchers without a consolidated technical roadmap for selecting and justifying forecasting algorithms.

## Approach

- Systematic literature review covering RNN variants (LSTM, GRU), CNN‑LSTM hybrids, Transformer and its variants, and hybrid LSTM‑Transformer models.
- Comparative analysis based on evaluation metrics: RMSE, MAE, MAPE, directional accuracy (DA), R², and Sharpe ratio.
- Datasets include daily and high‑frequency data from S&P 500, NIFTY 50, Moroccan exchange, and Chinese markets.
- Empirical studies compared against baselines: ARIMA, logistic regression, DNN, standalone LSTM/Transformer.
- Discussion of challenges: data noise, overfitting (N ≪ P problem), interpretability, computational cost, and deployment latency.

## Findings

1. LSTM achieved a daily return rate of **0.46%** on S&P 500 constituents (1992–2015), outperforming DNN (0.32%) and logistic regression (0.26%).
2. LSTM generated a Sharpe ratio of **2.34** — all other control methods scored far below 1.0.
3. Transformer reduced MAE by ~20.73%, MSE by ~34.84%, and MAPE by ~25.63% compared to LSTM on new energy vehicle stock prediction.
4. LSTM‑Transformer hybrid model reduced MAE and RMSE by **>50%** relative to either parent model, with R² rising from 0.84 (LSTM) and 0.78 (Transformer) to 0.96.
- GRU matches LSTM accuracy but with better computational efficiency; however, advantage varies by time period.
- Hybrid models (CNN‑LSTM, LSTM‑Transformer) complement local pattern extraction and global dependency modeling, but introduce overfitting risks and complex hyperparameters.

## Key Figures and Tables

None.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LSTM | Long Short-Term Memory — a recurrent network with gates that decide what to remember and forget [think: memory cell with a delete/save/read mechanism]. |
| GRU | Gated Recurrent Unit — simplified LSTM with fewer gates, trains faster. |
| Transformer | Neural network using self‑attention instead of recursion — sees all time steps at once. |
| Self‑attention | Mechanism that computes relationships between every pair of positions in a sequence. |
| RMSE | Root Mean Square Error — penalizes large errors heavily. |
| MAE | Mean Absolute Error — average prediction error, unit‑same as the data. |
| MAPE | Mean Absolute Percentage Error — error as a percentage, scale‑free. |
| Sharpe ratio | Risk‑adjusted return measure — higher means better return per unit of risk. |

## Critical Citations

- [Fischer & Krauss, 2018] — Foundational LSTM benchmark on S&P 500 with Sharpe ratio 2.34, establishing LSTM as the recurrent baseline.
- [Wang et al., 2022] — Transformer achieves ~20–25% error reduction over LSTM on stock indices.
- [Zhao et al., 2025] — LSTM‑Transformer hybrid cuts errors >50% and raises R² to 0.96, defining hybrid superiority.
- [Rahmadeyan, 2024] — Direct LSTM vs. GRU efficiency‑accuracy tradeoff; GRU trains faster but accuracy varies.
- [Saberironaghi et al., 2025] — Comprehensive survey of evaluation metrics for deep learning in stock prediction.

## Relevance to Odin

**Topics:**

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

**Contribution to Odin:**

This systematic review directly supports Odin’s forecasting module design by providing empirical benchmarks for LSTM against alternatives (GRU, Transformer, hybrid models). The finding that LSTM generates high‑Sharpe trading signals (2.34) and outperforms memoryless models confirms its suitability for sequential spending data. The review also quantifies the trade‑off: GRU is computationally lighter but not consistently more accurate, and Transformer excels on long sequences but suffers on small samples — directly informing Odin’s algorithm choice under cold‑start constraints. Although the domain is stock prices, spending time series share non‑linearity, volatility, and sequential dependence, making the comparative performance data transferable.

**Directly justifies:**

- “LSTM achieved a Sharpe ratio of 2.34 on daily financial returns, significantly outperforming non‑memory models (logistic regression: 0.26), supporting LSTM’s selection for spending forecasting where sequential memory is critical.”
- “GRU offers comparable accuracy to LSTM with higher computational efficiency, but the advantage is period‑dependent — a lightweight alternative for mobile deployment without guaranteed parity.”
- “Transformer reduced MAE by ~20.73% over LSTM on long sequences but suffers from overfitting when sample size is small — a caution for cold‑start user forecasting in Odin.”
- “LSTM‑Transformer hybrid models reduced RMSE by >50% compared to either parent model, but introduce complex hyperparameters and overfitting risks, indicating that hybrid architectures require careful regularization.”

**Limits of relevance:**

- Stock price prediction (financial asset returns) is not identical to personal spending forecasting — spending has different volatility patterns and is influenced by income cycles, not market sentiment.
- The reviewed studies use daily and high‑frequency trading data, whereas Odin operates on manual transaction logs at lower frequency (e.g., weekly or daily aggregates).
- No evaluation of per‑category forecasting — the review focuses on univariate or index‑level prediction, while Odin requires multi‑output per‑category forecasts.
- LSTM’s high Sharpe ratio comes from directional trading signals; Odin does not trade, but the temporal memory advantage remains valid for predicting expenditure.

## Limitations

- Review excludes direct comparison of model performance on personal finance datasets — all evidence is from equity markets. [unacknowledged]
- No discussion of how LSTM/Transformer performance degrades with sparse, irregular transaction data (common in manual input systems).
- The reported hybrid model gains (>50% error reduction) come from a single study on Chinese stocks; generalizability to other domains is unverified.
- Does not address real‑time or incremental learning for streaming transaction data, though it mentions adaptive learning as a future direction.
- Computational cost analysis is qualitative (e.g., Transformer’s O(n²) attention) — no concrete mobile‑device latency benchmarks.

## Remember This

- 🔑 **Sharpe ratio 2.34** — LSTM crushes memoryless models for sequential prediction.
- 📌 Transformer cuts MAE by **~21%** on long sequences but overfits small samples.
- 🧠 LSTM‑Transformer hybrids cut errors **>50%** but add hyperparameter complexity.
- ⚠️ Stock data ≠ spending data — transfer the method, not the magnitude.