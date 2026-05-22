# Time-Series Forecasting Using Deep Learning and Data Mining Models

## Metadata

```yaml
---
paper_id: "5e4f2d8c-6a3b-4e9c-9f2a-1b3c5d7e9f1a"
designation: algorithm-specific
title: "Time-Series Forecasting Using Deep Learning and Data Mining Models"
authors: "Scrivano, A."
year: 2025
venue: "Unknown"
odin_topics: ["5.C", "6.A", "6.B", "8.B", "12.B"]
shorthand_tags: ["/forecasting-methods-survey", "/forecast-algo-candidates", "/forecast-algo-comparison", "/forecast-algo-tradeoffs", "/forecast-eval-metrics", "/anomaly-algo-candidates", "/anomaly-eval-metrics", "/anomaly-algo-tradeoffs", "/eval-ml-design"]
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

Transformer models reduced MAE by **12–17%** over LSTM and TCN on retail datasets, while Gradient Boosting Machines achieved the lowest MAPE (8.0%) on financial data.

## Problem and Motivation

Traditional time-series models like ARIMA fail to capture non-linear dynamics and long-range dependencies in real-world sequential data. Accurate forecasting is critical for finance, energy, healthcare, and other domains where prediction errors drive costly decisions. No prior comparative benchmark systematically evaluated both deep learning architectures and data mining methods across multiple real-world datasets with consistent metrics.

## Approach

- Dataset: Financial markets, energy consumption trends, and retail transaction records; chronological partitioning into train/validation/test.
- Models: RNN, LSTM, TCN, Transformer (deep learning); Random Forest, Gradient Boosting Machine (data mining).
- Hyperparameter tuning: Grid search for each model across all datasets.
- Evaluation metrics: MAE, RMSE, MAPE for point forecasts; quantile loss for probabilistic forecasts.
- Implementation: TensorFlow and scikit-learn frameworks.

## Findings

1. **Transformer models achieved 12–17% lower MAE than LSTM and TCN on retail datasets** (Table 1: LSTM MAE 34500, Transformer MAE 27500).
2. Gradient Boosting Machine outperformed Random Forest across all three domains, achieving MAPE as low as 8.0% on finance data (Table 3: GBM MAPE 8.0% vs Random Forest 8.7%).
3. TCN attained 20% higher accuracy in early-stage anomaly detection from industrial sensor data compared to traditional methods.

- LSTM reduced mean absolute error by 15% over conventional methods in web traffic prediction when encoding day-of-week patterns.
- Transformer and Gradient Boosting showed strongest probabilistic forecasting performance (quantile loss coverage).

## Key Figures and Tables

- Figure 2: Temporal forecast error dynamics on retail data → Transformers show most stable reduction in prediction variance.
- Table 1: Retail dataset comparison (LSTM, TCN, Transformer) → Transformer lowest MAE (27500) and MSE (180).
- Table 2: Deep learning across energy, finance, retail → Transformer lowest MAPE in each domain (10.5%, 8.2%, 13.0%).
- Table 3: Random Forest vs Gradient Boosting → GBM consistently lower MAE, RMSE, and MAPE across all datasets.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LSTM | Long Short-Term Memory [think: memory cell with gates that decide what to remember and forget] |
| TCN | Temporal Convolutional Network — uses dilated convolutions to capture patterns at multiple time scales |
| Transformer | Attention-based architecture that weighs all time steps simultaneously; no recurrence |
| GBM | Gradient Boosting Machine — ensemble of weak decision trees trained sequentially to correct prior errors |
| MAE | Mean Absolute Error — average absolute difference between predicted and actual values |
| RMSE | Root Mean Squared Error — penalizes large errors more than MAE |
| MAPE | Mean Absolute Percentage Error — error normalized as percentage of actual value |
| Quantile loss | Loss function that evaluates forecast uncertainty by measuring accuracy at specified percentiles |

## Critical Citations

- [Hochreiter & Schmidhuber, 1997] — Introduced LSTM, foundational for recurrent sequence modeling.
- [Vaswani, 2017] — Proposed Transformer architecture with self-attention, enabling long-range dependency capture.
- [Friedman, 2001] — Developed Gradient Boosting Machines, core ensemble method for structured data.
- [Breiman, 2001] — Random Forests, baseline ensemble for comparison.

## Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

8.B — Anomaly Detection Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly informs Odin's algorithm selection for spending forecasting and anomaly detection by providing comparative benchmarks on real-world time-series data. The finding that Transformers reduce MAE by 12–17% over LSTM on retail sequences supports evaluating attention-based models for transaction forecasting in Odin's forecasting module. Gradient Boosting Machines' superior performance on structured financial data (8.0% MAPE) justifies their use for behavioral profiling classification, particularly given Odin's need for interpretability. The paper's evaluation framework (MAE, RMSE, MAPE, quantile loss) aligns with Odin's multi-metric assessment requirements for algorithmic modules under ISO 25010.

**Directly justifies:**

- "Transformer models achieved 12–17% lower MAE than LSTM and TCN on retail time-series forecasting tasks (Table 1: LSTM MAE 34500, Transformer MAE 27500)."
- "Gradient Boosting Machines outperformed Random Forest across energy, finance, and retail datasets, achieving MAPE as low as 8.0% on finance data (Table 3)."
- "Temporal Convolutional Networks attained 20% higher accuracy in early-stage anomaly detection from sensor data compared to traditional methods, supporting TCN as a candidate for Odin's anomaly detection module."
- "LSTM networks reduced mean absolute error by 15% over conventional methods when encoding temporal metadata such as day-of-week patterns, applicable to Odin's calendar-aware spending forecasts."

**Limits of relevance:**

- Datasets are not specific to personal finance or individual spending transactions; results are from energy, retail, and financial market data.
- Anomaly detection examples are industrial sensor data (machinery vibration), not financial anomalies like budget overages.
- No evaluation on cold-start conditions (new users with no transaction history), a critical gap for Odin's profiling module.
- Computational demands of Transformers may exceed mobile constraints; the paper does not address mobile deployment.

## Limitations

- Models require large, high-quality datasets; many real-world domains (including personal finance for new users) lack such data.
- Transformer computational demands limit deployment in resource-constrained environments (mobile devices). [unacknowledged]
- Generalizability across domains is not guaranteed; the paper notes that hybrid models need careful calibration to avoid overfitting.
- Probabilistic forecasting evaluation remains nascent; the paper highlights uncertainty quantification as a persistent gap.
- No comparison of model performance on irregularly sampled or sparse time-series, which characterizes manual transaction entry. [unacknowledged]

## Remember This

- 🔑 **12–17% lower MAE** — Transformers beat LSTMs on retail forecasting; consider for Odin's spending prediction.
- 📌 GBM achieves **8.0% MAPE** on finance data — strong candidate for behavioral profile classification.
- ⚠️ TCN gives **20% higher anomaly detection accuracy** — relevant for Odin's alert module, but tested on industrial sensors.
- 💡 No cold-start or mobile-constrained evaluation — limits direct transfer to Odin's deployment context.
