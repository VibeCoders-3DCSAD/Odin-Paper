# A Constrained, Data-Driven Budgeting Framework Integrating Macro Demand Forecasting and Marketing Response Modeling

## Metadata

```yaml
---
paper_id: "10.51903/jtie.v4i3.466"
designation: algorithm-specific
title: "A Constrained, Data-Driven Budgeting Framework Integrating Macro Demand Forecasting and Marketing Response Modeling"
authors: "Lu, Y.; Zhou, H.; Zhang, Y."
year: 2025
venue: "Journal of Technology Informatics and Engineering (JTIE)"
odin_topics: ["C.1", "C.2", "D.1", "J.1"]
shorthand_tags: ["/forecasting-methods", "/budget-rec-formulation", "/budget-algo-tradeoffs", "/eval-pfms-applied", "/budget-algo-justification"]
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

Multivariate VAR improves total demand forecast accuracy to **2.85% MAPE**; optimal marketing spend sits below ratio caps due to diminishing returns and revenue uncertainty.

## Problem and Motivation

Budgeting combines heterogeneous signals (macro demand, channel effectiveness, accounting constraints) but lacks an auditable, end‑to‑end pipeline. Without integrating demand uncertainty and diminishing returns, budgets risk violating ratio constraints or leaving value on the table. Prior work did not combine macro forecasting, saturating response curves, and chance‑constrained optimization into a single reproducible workflow.

## Approach

- Data: FRED PCE components (durable, nondurable, services; 2010Q1‑2025Q3), Advertising dataset (TV/radio/newspaper spend, sales), Apple FY2025 Form 10‑K for constraint calibration.
- Forecasting models: seasonal naïve, SARIMAX(1,1,1)×(0,1,1,4), gradient boosting (lags 1‑4), VAR on log‑differences (lag by AIC ≤4).
- Rolling one‑step‑ahead backtest (2018Q1‑2025Q3; expanding window from 2010Q1).
- Marketing response: OLS, ridge, lasso, gradient boosting, and Hill saturation model (diminishing returns). 5‑fold CV evaluation.
- Constraint calibration: gross margin 46.9%, SG&A 6.63% of revenue, marketing cap set to 1.5% of revenue, operating cash‑flow ratio 26.8% (Apple 10‑K).
- Optimization: grid search over allocation shares (5% increments) and budget utilization (20‑100% of cap); 500 Monte Carlo scenarios bootstrapped from VAR forecast errors.
- Objective: operating profit = (gross margin – non‑marketing opex) * (revenue + Δrevenue) – spend, with risk‑aversion parameter λ.

## Findings

1. **Multivariate VAR achieved the lowest total demand MAPE (2.85%)**, marginally ahead of seasonal naïve (2.86%) and SARIMAX (2.92%); gradient boosting underperformed (6.06%).
2. Hill saturation model (CV RMSE = 1.449, R² = 0.922) identified strong diminishing returns: newspaper spend had near‑zero marginal effect.
3. Risk‑neutral (λ=0) optimal spend = 0.97% of revenue (below 1.5% cap), allocating 25% TV / 75% radio / 0% newspaper. Incremental revenue‑to‑spend ratio ≈5.6×.
4. Optimal channel shares remained stable across ±5% macro scenarios; absolute spend scaled with revenue.
5. Higher risk aversion (λ=2.0) reduced spend to 0.90% of revenue, trading mean profit for lower volatility.
- Spending at the deterministic cap (1.5%) under high marketing effectiveness (5% lift) reduced SG&A satisfaction rate to 59.8% due to revenue uncertainty.

## Key Figures and Tables

- Figure 2: Total demand proxy actual vs VAR 1‑step forecasts → Errors widen during 2020 shock but recover.
- Figure 5: Hill‑model marginal response curves → Radio highest marginal ROI at low spend, newspaper negligible.
- Table 7: Category‑level RMSE/MAPE → Durable goods most volatile (MAPE 3.08‑5.87%); nondurable smoothest (1.65‑2.29%).
- Table 9: Baseline optimal budget (λ=0) → total spend $1,016M, inc_rev $5,735M, mean profit $35,961M, SG&A satisfaction 1.0.
- Table 12: Sensitivity to marketing cap κ → Cap at 1.0% reduces SG&A satisfaction to 0.948; caps ≥1.5% not binding.

## Key Equations

$$\Pi(b) = (g - o)(R + \Delta R(b)) - \sum b_i$$
*Operating profit = net margin times revenue uplift minus marketing spend.*

$$\sum b_i \leq \kappa R$$
*SG&A constraint: total marketing spend ≤ fixed share of revenue (κ = 1.5%).*

$$\mathbb{P}(B \leq \kappa R) \geq 1 - \delta$$
*Chance constraint: probability of staying under cap must exceed threshold 1‑δ.*

## Definitions

| Term / Acronym | Plain‑English Definition |
| -------------- | ------------------------ |
| FP&A | Financial Planning & Analysis – corporate budgeting and forecasting function. |
| PCE | Personal Consumption Expenditures – US macro demand measure (FRED). |
| VAR | Vector Autoregression – multivariate time‑series model capturing cross‑category dynamics. |
| SARIMAX | Seasonal ARIMA with exogenous regressors – classical statistical forecasting. |
| GBR | Gradient Boosting Regressor – tree‑based ensemble for supervised learning. |
| Hill function | Saturation curve \( h(s) = s^\gamma / (\alpha^\gamma + s^\gamma) \) – models diminishing returns. |
| SG&A | Selling, General & Administrative expenses – includes marketing. |
| MAPE | Mean Absolute Percentage Error – scale‑free forecast accuracy metric. |
| Monte Carlo | Simulation drawing many random outcomes from forecast error distribution. |

## Critical Citations

- [Box et al., 2015] – Foundational time‑series analysis framework for ARIMA/SARIMA models.
- [Friedman, 2001] – Formalized gradient boosting, used as flexible forecasting benchmark.
- [Hanssens et al., 2001] – Market response modeling and saturation curves (Hill function).
- [Markowitz, 1952] – Mean‑variance optimization template for balancing profit and risk.

## Relevance to Odin

**Topics:**

C.1 — Budgeting Strategies and Budget Recommendation

C.2 — Budget Recommendation Algorithm

D.1 — Predictive Modeling in Personal Finance Systems

J.1 — System Evaluation

**Contribution to Odin:**

This paper directly supports Odin’s budget recommendation module by demonstrating a constraint‑based optimization framework that respects hard spending limits (e.g., income‑based caps) while handling diminishing‑returns benefits. The use of Hill saturation functions provides a method to model saturating utility per spending category – directly analogous to how Odin might model that excess budget in a category yields lower marginal value. The paper’s Monte Carlo evaluation of constraint satisfaction under demand uncertainty offers a template for Odin to report confidence levels (e.g., “95% chance you will stay under budget”) rather than deterministic recommendations. Although the domain is enterprise FP&A, the algorithmic structure (forecast → response → constrained optimization) maps cleanly to Odin’s spending forecasting and budget recommendation modules.

**Directly justifies:**

- “Multivariate VAR achieves 2.85% MAPE for aggregate demand forecasting on quarterly PCE data, outperforming seasonal naïve (2.86%) and SARIMAX (2.92%).”
- “Hill saturation models with diminishing returns produce marginal ROI curves that identify saturating spend levels – radio saturates after moderate spend, newspaper provides near‑zero marginal value.”
- “Optimal marketing spend under uncertainty is strictly below the nominal ratio cap (0.97% vs 1.5%) to maintain constraint satisfaction; spending at the cap risks violation in ~40% of scenarios.”
- “A budget planner can trade off expected profit and volatility via a risk‑aversion parameter λ, with higher λ reducing spend (e.g., from 0.97% to 0.90% of revenue).”

**Limits of relevance:**

- Enterprise focus (firm‑level budgeting, marketing mix) not personal finance; the objective (operating profit) differs from Odin’s user‑level adherence.
- Data sources are US‑centric (PCE, Advertising dataset) and not grounded in Filipino spending behavior.
- Marketing response uses a cross‑sectional toy dataset without temporal dynamics (adstock effects), limiting direct transfer to Odin’s user‑level spending patterns.
- No cold‑start evaluation – all models assume historical data, while Odin must handle new users with no transaction history.

## Limitations

- Data sources not internally consistent: macro PCE from FRED, marketing from small cross‑sectional dataset, constraints from Apple. [unacknowledged]
- No adstock (carryover) effects in marketing response; real effects persist over time.
- Forecasting sample limited to 63 quarterly observations, restricting complex model training.
- Validation only on public data, not a real firm’s internal FP&A process; no comparison to human expert budgets. [unacknowledged]
- Assumes constant market share (ρ) linking macro demand to firm revenue; not validated for structural breaks.

## Remember This

- 🔑 **VAR total demand MAPE = 2.85%** – beats seasonal naïve (2.86%) and SARIMAX (2.92%).
- 📌 Optimal spend = **0.97% of revenue**, below 1.5% cap – diminishing returns bind before the cap.
- ⚠️ Spending at the deterministic cap risks **40% constraint violation** under revenue uncertainty.
- 💡 Hill response curves: radio highest marginal ROI, newspaper near zero – same channel prioritization principle applies to spending categories.
- ✅ Risk aversion (λ=2.0) cuts spend to 0.90% of revenue – trade mean profit for lower volatility.