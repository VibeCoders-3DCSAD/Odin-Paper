# A SYSTEMATIC REVIEW OF DEMAND FORECASTING MODELS FOR RETAIL E-COMMERCE ENHANCING ACCURACY IN INVENTORY AND DELIVERY PLANNING

## Metadata

```yaml
---
paper_id: "10.63125/mbbfw637"
designation: algorithm-specific
title: "A SYSTEMATIC REVIEW OF DEMAND FORECASTING MODELS FOR RETAIL E-COMMERCE ENHANCING ACCURACY IN INVENTORY AND DELIVERY PLANNING"
authors: "Chowdhury, A. R.; Paul, R.; Rozony, F. Z."
year: 2025
venue: "International Journal of Scientific Interdisciplinary Research"
odin_topics: ["6.A", "6.B", "12.B"]
shorthand_tags: ["/forecasting-methods-survey", "/temporal-dependency", "/per-category-forecast", "/forecast-algo-candidates", "/forecast-algo-comparison", "/forecast-algo-tradeoffs", "/forecast-eval-metrics", "/eval-ml-design"]
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

Deep learning (LSTM, transformers) and hybrid ARIMA-ML models consistently outperform traditional statistical methods, improving forecast accuracy by up to 20% in volatile e-commerce demand scenarios.

## Problem and Motivation

Demand forecasting for retail e-commerce lacks a comprehensive synthesis comparing traditional statistical, machine learning, deep learning, and hybrid models across inventory and delivery planning contexts. Accurate forecasting is critical because e‑commerce operates under high volatility, rapid SKU turnover, and real‑time logistics pressure. Prior literature focused narrowly on specific methods without offering a holistic, comparative view of model performance and applicability.

## Approach

- Systematic review following PRISMA guidelines of 72 peer‑reviewed studies (2010–2024) from Scopus, Web of Science, IEEE Xplore, and ScienceDirect.
- Categorized models into four groups: traditional statistical (ARIMA, SARIMA, Holt‑Winters), machine learning (random forests, gradient boosting, SVR, k‑NN), deep learning (LSTM, GRU, CNN, transformers), and hybrid (ARIMA+ML/DL).
- Evaluated performance using MAE, RMSE, MAPE, and sMAPE; also assessed integration of external data (weather, economic indicators, social media sentiment).
- Quality assessment included data sources, model clarity, reproducibility, and alignment with e‑commerce operational issues.

## Findings

1. Machine learning models (31 studies, 4,800 citations) **improve RMSE and MAPE by up to 20% over statistical methods** in short‑term, high‑frequency forecasting.
2. Deep learning models (22 studies, 3,900 citations) excel at capturing nonlinear patterns, long‑term dependencies, and multivariate inputs, especially for SKU‑level demand.
3. Hybrid ARIMA‑ML/DL models (18 studies, 2,500 citations) balance interpretability and accuracy, performing well during promotional spikes and structural breaks.
4. External data integration (27 studies, 5,000 citations) — weather, sentiment, clickstream — significantly enhances forecast performance in volatile, promotion‑sensitive categories.

- Traditional models (ARIMA, Holt‑Winters) remain relevant for stable, seasonal demand and as benchmarks, but fail under nonlinearity and external shocks.

## Key Figures and Tables

- Table 1: Summary of findings → ML/deep learning models have highest citation counts and accuracy gains (up to 20%).
- Figure 2: Classical time series methods → ARIMA/SARIMA work for stable patterns but not for volatility.
- Figure 5: Machine learning models → ensembles (random forests, XGBoost) handle nonlinear demand well.
- Figure 6: Deep learning networks → LSTM and GRU capture temporal dependencies in retail data.
- Figure 7: Hybrid and ensemble approaches → ARIMA‑LSTM reduces forecast error in flash sales.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| ARIMA | AutoRegressive Integrated Moving Average — a linear time‑series model for non‑stationary data. |
| SARIMA | Seasonal ARIMA — extends ARIMA with seasonal components. |
| LSTM | Long Short‑Term Memory [think: memory cell that learns what to forget] — recurrent network for long‑range dependencies. |
| GRU | Gated Recurrent Unit — simplified LSTM with faster training. |
| CNN | Convolutional Neural Network — extracts local patterns from time‑series or spatial data. |
| ML | Machine learning — algorithms that learn from data without explicit programming. |
| DL | Deep learning — multi‑layer neural networks for complex patterns. |
| RMSE | Root Mean Squared Error — penalizes large errors heavily. |
| MAPE | Mean Absolute Percentage Error — scale‑independent percentage error. |
| MAE | Mean Absolute Error — average absolute forecast error. |
| SKU | Stock Keeping Unit — unique identifier for each product. |
| PRISMA | Preferred Reporting Items for Systematic Reviews and Meta‑Analyses — structured review guideline. |

## Critical Citations

- [Lara‑Benítez et al., 2020] — Foundational definition of e‑commerce demand forecasting and its data‑intensive nature.
- [Bandara et al., 2019] — Demonstrated LSTM for e‑commerce sales forecasting, a key deep learning baseline.
- [Mosavi et al., 2020] — Comprehensive review of deep reinforcement learning in economics, supporting methodological breadth.
- [Frei et al., 2022] — Showed LSTM outperforms shallow ML (SVR, random forests) in daily retail sales.

## Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This systematic review directly informs Odin's spending forecasting module by providing a comparative analysis of candidate algorithms (LSTM, GRU, ARIMA, hybrid models) and their performance trade-offs. The finding that LSTM and GRU capture temporal dependencies in irregular, high‑frequency transaction sequences justifies selecting recurrent neural networks over simpler methods for forecasting per‑category spending. The review's benchmarking of evaluation metrics (MAE, RMSE, MAPE) supports Odin's module evaluation framework under ISO 25010, and the discussion of hybrid models offers a path to balance accuracy with interpretability when explaining budget recommendations.

**Directly justifies:**

- "LSTM and GRU networks capture long‑range temporal dependencies and nonlinear demand patterns, outperforming traditional statistical models by up to 20% in RMSE/MAPE on volatile retail data."
- "Machine learning models (random forests, gradient boosting) provide 15–20% accuracy improvement over ARIMA for short‑term forecasting with multivariate inputs such as promotions and web traffic."
- "Hybrid ARIMA‑ML/DL models balance interpretability and accuracy, making them suitable for production systems where explainability is required alongside predictive power."
- "Integration of external variables (weather, sentiment, economic indicators) significantly enhances forecast accuracy in volatile environments, a principle applicable to personal finance with income volatility and cultural spending cycles."

**Limits of relevance:**

- Domain is retail e‑commerce inventory and delivery planning, not personal spending behavior — spending patterns may have different volatility drivers.
- No evaluation of cold‑start forecasting (new users with no transaction history), which is critical for Odin's initial user experience.
- External data sources (e.g., social media sentiment, weather) may not be available or relevant for personal finance.
- All reviewed studies use international datasets; Filipino‑specific income volatility and cultural obligations (e.g., remittances, family support) are not addressed.

## Limitations

- Traditional models underperform under nonlinear, promotional, or external shock conditions — acknowledged in the review.
- Hybrid models are underutilized in operational systems due to design complexity and maintenance overhead — acknowledged.
- No discussion of mobile‑specific constraints (computational limits, offline operation) for deploying deep learning models — [unacknowledged].
- Generalizability to personal finance domain is untested; spending behavior may have different stationarity and seasonality properties — [unacknowledged].
- All studies come from international contexts (US, China, Europe); no Philippine‑specific validation of forecasting models — [unacknowledged].

## Remember This

- 🔑 ML models beat ARIMA by up to 20% RMSE/MAPE — proven across 31 studies.
- 🧠 LSTM captures long‑term spending patterns; GRU is faster but slightly less accurate.
- 📌 Hybrid ARIMA‑ML gives accuracy + interpretability — ideal when users need explanations.
- ⚠️ No cold‑start data — unknown how these models perform for new Odin users with zero history.
- 💡 External data (weather, sentiment) boosts accuracy but may not exist for personal finance.
