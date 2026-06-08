# A Comparative Analysis of Budget Forecasting Methods: A Systematic Literature Review Covering the 1983–2024 Period

## Metadata

```yaml
---
paper_id: "10.1111/pbaf.70008"
designation: algorithm-specific
title: "A Comparative Analysis of Budget Forecasting Methods: A Systematic Literature Review Covering the 1983–2024 Period"
authors: "Kara, B.; Şengüler, H."
year: 2025
venue: "Public Budgeting & Finance"
odin_topics: ["D.1", "D.2", "J.1"]
shorthand_tags: ["/forecasting-methods", "/spending-time-series", "/lstm-vs-alternatives", "/eval-frameworks"]
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

No single forecasting method is universally best; context dictates choice, with **43%** of studies on the US.

## Problem and Motivation

The literature lacks a systematic evaluation of which budget forecasting methods perform best under specific conditions, as findings are fragmented across datasets, countries, and time periods. Accurate forecasts are critical for fiscal policy, resource allocation, and public trust, yet method performance varies substantially with economic environment and data quality. Prior work provided no holistic framework comparing method families (statistical, ML, deep learning) across contexts.

## Approach

- Systematic review of 69 peer-reviewed studies (1983–2024) that compare at least two forecasting methods against actual outcomes.
- Descriptive statistical analysis of method frequency, geographic distribution, metric preferences, and dataset characteristics.
- Trend analysis to identify temporal shifts in method popularity.
- Network analysis (Gephi) of method–method, method–year, and method–metric co-occurrence.
- Dataset analysis covering training period length (1 to 50+ years), observation count (1 to 1000+), and data frequency (annual, quarterly, monthly).

## Findings

1. **43%** of studies focus on the United States; developing economies are severely underrepresented.
2. MAPE (38 studies), RMSE (36), and MAE (22) dominate evaluation metrics; directional errors are almost entirely neglected.
3. LSTM’s average forecasting horizon is only **3.3 years** (short-term), while AR and MA models reach 14+ years (long-term).
4. Studies comparing 3–6 methods receive the highest average citations (26), versus 7 citations for single-method studies.
5. Four evolutionary phases: statistical methods (1980s), diversification (1990s–2000s), machine learning (2010s), deep learning (2020s).

- Methodological diversity has increased but created “inflation,” complicating practitioner choice.
- Simple models (OFC, RW, regression) remain essential benchmarks; no complex model consistently outperforms them.

## Key Figures and Tables

- Figure 1: Evolution of forecasting methods over time → Four-phase trajectory from ARIMA to LSTM and hybrid PCA-W-KSVR.
- Figure 2: Co-occurrence of methods in comparative studies → ARIMA and OFC serve as universal benchmarks against ML methods.
- Graph 3: Average forecasting horizons by method → LSTM (3.3y), ANN (5.3y), AR (14.3y) — linear models dominate long-term.
- Table 3: Country-level distribution → US (30 studies), China (6), Turkey (4), 17 countries studied once.
- Table 4: Number of studies using each metric → MAPE (38), RMSE (36), MAE (22) — three metrics account for vast majority.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| MAPE | Mean Absolute Percentage Error — average percentage difference between forecast and actual. |
| RMSE | Root Mean Squared Error — penalizes large errors more heavily than MAE. |
| MAE | Mean Absolute Error — average absolute difference. |
| LSTM [think: memory cell that learns what to forget] | Long Short-Term Memory — a deep learning model for sequential data. |
| ARIMA | Autoregressive Integrated Moving Average — classic time series model. |
| ANN | Artificial Neural Network — ML model inspired by biological neurons. |
| SVM | Support Vector Machine — ML model that finds optimal decision boundaries. |
| ML | Machine learning — algorithms that learn from data without explicit programming. |
| DL | Deep learning — multi-layer neural networks. |
| OFC | Official forecast — government agency baseline prediction. |
| RW | Random walk — naive forecast that next period equals current period. |

## Critical Citations

- [McDonald et al., 2024] — Sets field agenda ranking “Data and Methods” as top priority, framing this review’s importance.
- [Downs & Rocke, 1983] — One of the earliest comparative studies using multivariate ARMA for municipal budgets.
- [Ghysels & Ozkan, 2015] — Introduces MIDAS for real-time federal budget forecasting, cited as key mixed-frequency approach.

## Relevance to Odin

**Topics:**

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

J.1 — System Evaluation

**Contribution to Odin:**

This systematic review directly supports Odin’s forecasting module by demonstrating that LSTM is suited for short-term (3.3-year horizon), context-sensitive forecasting—exactly Odin’s use case for monthly spending prediction. The review’s finding that no single method is universally best justifies Odin’s design decision to benchmark LSTM against simpler alternatives (ARIMA, regression) rather than assume superiority. The dominance of MAPE, RMSE, and MAE as evaluation metrics (38, 36, 22 studies respectively) provides empirical grounding for Odin’s choice of these same metrics to assess forecasting accuracy. Although the paper examines public sector budgets, the methodological comparisons (LSTM vs. ARIMA vs. XGBoost) and the finding that ML/DL methods excel on short, nonlinear sequences apply directly to personal spending time series.

**Directly justifies:**

- “LSTM’s average forecasting horizon of 3.3 years indicates suitability for short-term spending forecasts, while linear models (AR, MA) are better for long-term projections.”
- “MAPE is the most frequently used accuracy metric in forecasting comparisons (38 of 69 studies), establishing it as the standard for evaluating prediction error in financial time series.”
- “Studies comparing 3–6 methods receive the highest citation impact (average 26 citations), suggesting that focused, multi-model benchmarking yields the most credible evidence.”
- “43% of forecasting research concentrates on the United States, revealing a geographic bias that limits generalizability; Odin’s Philippine context requires local validation.”
- “Deep learning methods (LSTM, ANN) are consistently applied to short-term forecasts, while traditional statistical methods dominate long horizons—a division of labor directly applicable to Odin’s monthly spending predictions.”

**Limits of relevance:**

- Public budget forecasting focuses on macroeconomic aggregates (tax revenue, deficits), not individual-level spending categories or behavioral patterns.
- Geographic concentration on US data (43%) means findings may not replicate in the Philippine young professional context with different income volatility and spending norms.
- LSTM’s data requirements (hundreds of observations) may challenge Odin’s cold-start phase when users have little history.
- The review does not address mobile-specific constraints (compute, battery, offline operation) that affect algorithm selection for Odin.

## Limitations

- Severe geographic bias — 43% of studies from the US, 17 countries represented only once — limits generalizability to emerging economies like the Philippines. [unacknowledged]
- Metric hegemony (MAPE, RMSE, MAE) ignores directional errors — the cost of over-forecasting vs. under-forecasting — which is critical for budgeting decisions.
- Data constraints: 8 studies use only 1–25 observations, raising reliability concerns for data-hungry methods like LSTM.
- No analysis of personal finance or behavioral factors (e.g., user adherence, spending guilt) that influence forecast utility.
- Long-term forecast performance beyond 5 years is rarely evaluated for ML/DL methods due to parameter instability risk.

## Remember This

- 🔑 **No universal best method** — context (horizon, data quality) determines choice, not model complexity.
- 📌 **43% of studies focus on the US** — Philippine validation is essential, not optional.
- 💡 LSTM’s sweet spot is **3.3 years** — perfect for monthly spending forecasts, useless for long-term planning.
- 🔍 MAPE appears in **38 of 69 studies** — the gold standard metric for forecasting error in finance.
- ⚠️ Share of developing-economy studies is **<10%** — a major gap this review itself acknowledges.
