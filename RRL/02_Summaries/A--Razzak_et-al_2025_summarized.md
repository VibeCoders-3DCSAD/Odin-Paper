# A SYSTEMATIC REVIEW OF DEMAND FORECASTING MODELS FOR RETAIL E-COMMERCE ENHANCING ACCURACY IN INVENTORY AND DELIVERY PLANNING

## Metadata

```yaml
---
paper_id: "10.63125/mbbfw637"
designation: international
title: "A SYSTEMATIC REVIEW OF DEMAND FORECASTING MODELS FOR RETAIL E-COMMERCE ENHANCING ACCURACY IN INVENTORY AND DELIVERY PLANNING"
authors: "Chowdhury, A. R.; Paul, R.; Rozony, F. Z."
year: 2025
venue: "International Journal of Scientific Interdisciplinary Research"
odin_topics: ["D.1", "D.2"]
shorthand_tags: ["/forecasting-methods", "/spending-time-series", "/lstm-vs-alternatives", "/lstm-spending-applied", "/lstm-justification"]
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

A systematic review of 72 studies finds that deep learning models (LSTM, transformers) outperform traditional statistical methods in volatile e-commerce demand forecasting, with hybrid and context-aware models offering balanced accuracy and interpretability.

## Problem and Motivation

E-commerce demand forecasting faces volatility, high SKU diversity, and real-time requirements that traditional statistical models cannot handle effectively. Accurate forecasts are critical for inventory planning and delivery scheduling, directly affecting operational costs and customer satisfaction. Prior literature lacked a comprehensive synthesis comparing classical, machine learning, deep learning, and hybrid forecasting models specifically for retail e-commerce contexts.

## Approach

- PRISMA-guided systematic review of 284 initial papers, narrowed to 72 peer-reviewed studies published between 2010 and 2024.
- Four model categories evaluated: traditional statistical (ARIMA, SARIMA, Holt-Winters), machine learning (random forests, gradient boosting, SVR, k-NN), deep learning (LSTM, GRU, CNN, transformers), and hybrid/ensemble methods.
- Performance metrics used across studies: MAE, RMSE, MAPE, sMAPE, and CRPS for probabilistic forecasts.
- Analysis of external data integration: weather, social media sentiment, economic indicators, clickstream, and promotional calendars.
- Focus on applications in inventory replenishment, stockout/overstock reduction, and delivery route optimization.

## Findings

1. Deep learning models (LSTM, transformers) consistently achieved superior accuracy for volatile, high-frequency e-commerce demand, **reducing MAPE by up to 20% over statistical methods**.
2. Machine learning models (random forests, gradient boosting) outperformed traditional models by 15–20% in RMSE and MAPE when promotional and exogenous variables were included.
3. Hybrid ARIMA-ML/DL models outperformed standalone models across 70% of SKUs in multi-retailer datasets.

- External data integration (sentiment, weather, economic indicators) significantly improved forecast accuracy during flash sales and promotions.
- Traditional models remain relevant for stable, seasonal demand with short horizons and low computational cost.

## Key Figures and Tables

- Table 1: Summary of findings across model categories → deep learning and ML have highest citation impact (4800 and 3900 citations respectively).
- Figure 5: Machine learning models for nonlinear demand → ensemble and tree-based methods excel at capturing promotion and seasonality interactions.
- Figure 6: Deep learning networks (LSTM, GRU, CNN) → capture long-term dependencies and nonlinear patterns in high-frequency data.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LSTM | Long Short-Term Memory — a deep learning network that remembers patterns over long sequences [think: memory cell with forget/update gates] |
| GRU | Gated Recurrent Unit — a simpler LSTM variant with fewer gates, faster training |
| CNN | Convolutional Neural Network — detects local patterns in data, adapted for time-series |
| ARIMA | AutoRegressive Integrated Moving Average — classic time-series model for non-stationary data |
| SARIMA | Seasonal ARIMA — ARIMA extended with seasonal components |
| ML | Machine learning — algorithms that learn from data without explicit programming |
| DL | Deep learning — multi-layer neural networks for complex pattern recognition |
| MAE | Mean Absolute Error — average magnitude of forecast errors |
| RMSE | Root Mean Squared Error — penalizes large errors more heavily |
| MAPE | Mean Absolute Percentage Error — scale-independent percentage error |
| SKU | Stock Keeping Unit — unique identifier for each product in inventory |

## Critical Citations

- [Lara-Benítez et al., 2020] — Defined e-commerce demand forecasting as data-intensive and volatile, motivating need for advanced models.
- [Mosavi et al., 2020] — Showed the shift from classical to ML/DL methods in retail demand prediction.
- [Bandara et al., 2019] — Demonstrated LSTM for e-commerce sales forecasting, foundational for deep learning adoption.

## Relevance to Odin

**Topics:**

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

**Contribution to Odin:**

This systematic review provides a comprehensive benchmark of LSTM against alternative forecasting models (ARIMA, GRU, random forests, transformers) in volatile, high-frequency transaction environments — directly analogous to Odin's per-category spending forecasting. The finding that LSTM reduces MAPE by up to 20% over statistical methods in promotion-sensitive retail data justifies Odin's selection of LSTM over simpler baselines for the spending forecasting module. The review also highlights that hybrid models (ARIMA+LSTM) offer improved robustness during demand shifts, which could inform Odin's cold-start forecasting strategy or adaptive model retraining. While the domain is retail e-commerce, the time-series characteristics (seasonality, irregular spikes, external influences) mirror personal spending patterns, making the evidence transferable.

**Directly justifies:**

- "LSTM outperforms ARIMA and exponential smoothing by up to 20% in MAPE for volatile, high-frequency demand data (Chowdhury et al., 2025)."
- "Deep learning models (LSTM, GRU, transformers) capture long-term dependencies and nonlinear patterns that statistical models miss, making them suitable for per-category spending forecasting."
- "Hybrid ARIMA-LSTM models achieve lower forecasting errors than standalone models in datasets with structural breaks (e.g., promotions or sudden demand shifts)."
- "External data integration (e.g., sentiment, economic indicators) enhances forecast accuracy beyond historical sales alone, suggesting potential for incorporating calendar events or behavioral signals into spending forecasts."

**Limits of relevance:**

- The review focuses on retail e-commerce (product demand), not personal spending, which may have different volatility drivers (income shocks vs. promotions).
- All studies are from non-Philippine contexts; Filipino spending behavior patterns may differ in seasonality and cultural obligations.
- The review does not address cold-start scenarios with no historical user data.
- Implementation in mobile resource-constrained environments (on-device inference, battery, memory) is not discussed.

## Limitations

- The review synthesizes studies narratively without a meta-analysis with pooled effect sizes; comparisons are qualitative. [unacknowledged]
- Most studies use proprietary or non-public e-commerce datasets, limiting reproducibility for personal finance applications.
- Deep learning models' computational requirements and inference latency are acknowledged as barriers for smaller enterprises.
- The review does not specifically evaluate forecasting for personal finance or budgeting contexts — only retail product demand.
- No discussion of model interpretability requirements for end-user financial applications where users need explanations.

## Remember This

- 🔑 **LSTM beats ARIMA by up to 20% MAPE** — key evidence for Odin's forecasting module selection.
- 📌 Hybrid models (ARIMA+LSTM) handle demand shifts better than pure deep learning.
- ⚠️ Retail e-commerce data (SKU demand) vs personal spending: similar time-series challenges but different drivers.
- ✅ Systematic review of 72 studies confirms deep learning dominance in volatile, high-frequency data.
