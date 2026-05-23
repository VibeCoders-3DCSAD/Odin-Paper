# Predict, Optimize, Deliver: Demand Forecasting and Resource Optimization for a Market Research Firm

## Metadata

```yaml
---
paper_id: "10.1145/3785171.3785187"
designation: algorithm-specific
title: "Predict, Optimize, Deliver: Demand Forecasting and Resource Optimization for a Market Research Firm"
authors: "Mariano, M. T. G.; Monreal, R. N."
year: 2025
venue: "The 9th International Conference on Business and Information Management (ICBIM 2025), Bangkok, Thailand"
odin_topics: ["6.A", "6.B", "12.B"]
shorthand_tags: ["/forecasting-methods-survey", "/forecast-algo-candidates", "/forecast-algo-comparison", "/forecast-eval-metrics", "/eval-ml-design", "/eval-limitations"]
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

Prophet outperformed ARIMA, Holt-Winters, and LSTM in demand forecasting for a market research firm, balancing accuracy, interpretability, and speed for short-term workforce planning.

## Problem and Motivation

Professional service firms face unpredictable service demand, and manual workforce planning fails to adapt to volatility, causing inefficiencies and revenue loss. Effective resource allocation is critical because human labor drives both cost and value in these firms. No prior study systematically compared forecasting methods with interpretability and speed trade-offs specifically for professional service environments.

## Approach

- Dataset: 7 years (Jan 2018–Dec 2024) of billable hours from a Manila-based market research firm’s time-tracking system, aggregated daily.
- Models compared: ARIMA, Holt-Winters Exponential Smoothing, Prophet, and LSTM.
- Evaluation: Multiple train-test splits (60:40, 70:30, 80:20) plus a 30-day holdout; metrics: MAE, RMSE, MAPE.
- Weighted error score: 0.35×MAE + 0.35×RMSE + 0.30×MAPE; interpretability and training speed each weighted 0.25 in final selection.
- Optimization: Pyomo-based MILP (CPLEX solver) allocates workforce subject to work-hour caps (8h regular, +2h overtime), leave schedules, and dedicated/shared staffing rules.
- Visualization: Power BI dashboard with Sankey diagrams, bar charts, and KPI cards.

## Findings

1. Prophet achieved the lowest weighted error for Client 1 (**13.038**) and Client 2 (27.786) on the 30-day holdout, outperforming ARIMA (21.164 and 24.664) and LSTM (16.703 and 27.833).
2. Prophet’s overall weighted score (10.456) ranked #1, followed by ARIMA (11.582), LSTM (11.634), and Holt-Winters (13.062).
3. Larger training sizes consistently improved ARIMA and Holt-Winters MAE/RMSE but MAPE remained volatile for volatile clients.
- LSTM showed stable absolute accuracy across splits but higher complexity and data requirements reduced practical viability.
- Optimization achieved near-zero demand gaps under baseline, over‑forecast, and under‑forecast scenarios, respecting all capacity constraints.

## Key Figures and Tables

- Figure 1: ARIMA performance across splits → larger training size improves MAE/RMSE; MAPE volatile for Client 2.
- Figure 2: Holt-Winters performance → lowest errors at higher training size but high MAPE sensitivity.
- Figure 3: Prophet performance → variability across splits indicates sensitivity to changepoint prior scale.
- Figure 4: LSTM performance → stable across splits, slight advantage for Client 1.
- Table 3: Weighted error metrics → Prophet lowest for both clients.
- Table 4: Overall model selection → Prophet best (10.456), Holt-Winters worst (13.062).

## Key Equations

$$\min \sum_{i,t} C_{regular}(x_{iC1t} + x_{iC2t}) + C_{overtime}(o_{i,t}) + C_{penalty}(E_{1t} + E_{2t})$$
*Minimize regular labor, overtime, and penalty costs for unmet demand.*

$$\sum_{i} x_{iC1t} = HC_{1t} + E_{1t-1}$$
*Demand satisfaction: supplied hours plus backlog must meet forecasted demand.*

$$\sum_{i} x_{iC1t} + x_{iC2t} \leq (8 + o_{i,t}) \times (1 - y_{i,t})$$
*Work-hour limit: regular plus overtime, zero if employee on leave.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| ARIMA | Autoregressive Integrated Moving Average – a classical time series model assuming stationarity. |
| LSTM | Long Short-Term Memory – a deep learning model with memory cells for long‑term dependencies. |
| Prophet | Facebook’s open‑source forecasting model that decomposes trend, seasonality, and holiday effects. |
| MAE | Mean Absolute Error – average absolute forecast error. |
| RMSE | Root Mean Square Error – penalizes large errors more heavily. |
| MAPE | Mean Absolute Percentage Error – relative error as a percentage. |
| MILP | Mixed-Integer Linear Programming – optimization with both continuous and integer decisions. |
| CPLEX | A high‑performance solver for large‑scale optimization problems. |

## Critical Citations

- [Ugboko & Ehugbo, 2021] – Establishes resource utilization’s effect on competitive advantage in service firms.
- [Sharma & Singh, 2022] – RLS model for forecasting resource fulfillment in IT/consulting; baseline for demand volatility.
- [Terrada et al., 2022] – LSTM outperforms ARIMA in supply chain demand forecasting; supports LSTM’s potential.
- [Kumar et al., 2024] – Comparative assessment of Holt-Winters vs. ARIMA for inventory optimization.

## Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly informs Odin’s spending forecasting module by benchmarking four time‑series models (ARIMA, Holt-Winters, Prophet, LSTM) on real operational demand data using MAE, RMSE, and MAPE – metrics Odin will use to evaluate its own forecasting algorithms. The finding that Prophet balances accuracy, interpretability, and training speed (weighted score 10.456 vs. LSTM’s 11.634) justifies considering Prophet alongside LSTM for Odin’s short‑term per‑category spending forecasts, especially given Odin’s mobile‑first constraints where model simplicity and speed matter. Although the domain is workforce demand rather than personal spending, the methodological comparison of sequential forecasting algorithms and the weighted multi‑metric evaluation framework are directly transferable to Odin’s algorithm selection process.

**Directly justifies:**

- “Prophet achieved the lowest weighted error (13.038) on a 30‑day holdout, combining MAE, RMSE, and MAPE with interpretability and speed weights.”
- “LSTM showed stable performance across training splits but higher complexity and slower training reduced its practical viability for resource‑constrained environments.”
- “Larger training datasets improve ARIMA and Holt‑Winters accuracy, but MAPE remains volatile for irregular demand patterns – a limitation relevant to variable‑income users.”
- “A weighted evaluation score that includes interpretability (0.25) and training speed (0.25) alongside error metrics provides a more operational model selection criterion than accuracy alone.”

**Limits of relevance:**

- Domain is B2B workforce demand forecasting, not personal spending; patterns of seasonality and volatility may differ.
- Dataset is daily aggregated hours; Odin’s spending data is transaction‑level with potentially different temporal granularity.
- The paper does not address cold‑start forecasting (no historical data) – a critical challenge for new Odin users.
- No evaluation of per‑category forecasting; Odin requires separate models for each spending category.

## Limitations

- Data is from a single market research firm; generalizability to other service or personal finance contexts is unknown. [unacknowledged]
- Forecast evaluation excludes cold‑start scenarios; models assume sufficient historical data (multiple years). [unacknowledged]
- MAPE can exaggerate errors when actual values are small; the paper acknowledges this but still includes MAPE in weighted score.
- External economic indicators (e.g., inflation, remittance flows) were not incorporated, though they may affect demand.
- Optimization costs ($5/h regular, $10/h overtime) are hypothetical; real costs may alter allocation outcomes.

## Remember This

- 🔑 **Prophet weighted error 13.038** – beat ARIMA (21.164) and LSTM (16.703) on 30‑day holdout.
- 📌 Interpretability and speed each weighted 0.25 – practical deployment matters beyond raw accuracy.
- 💡 Larger training datasets improve ARIMA/Holt‑Winters but not Prophet – Prophet is more parameter‑sensitive.
- ⚠️ No cold‑start evaluation – Odin’s new users lack history, so findings apply only after data accumulates.
