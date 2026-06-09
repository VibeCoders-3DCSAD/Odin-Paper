```yaml
paper_id: 10.51903/jtie.v4i3.466
designation: international
title: A Constrained, Data-Driven Budgeting Framework Integrating Macro Demand Forecasting and Marketing Response Modeling
authors: Lu, Y.; Zhou, H.; Zhang, Y.
year: 2025
venue: Journal of Technology Informatics and Engineering
odin_topics:
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 7.C
  - 12.B
shorthand_tags:
  - /spending-forecast
  - /forecasting-algo
  - /budget-strategies
  - /budget-recommendation
  - /budget-algo
  - /eval-algo
tldr: Integrates macro demand forecasting, marketing response with diminishing returns, and accounting constraints into a budget optimization framework under uncertainty.
problem_and_motivation: Budgeting must combine macroeconomic signals, channel-level marketing effectiveness, and hard accounting constraints. Existing approaches treat these components separately and ignore uncertainty, leading to suboptimal or constraint-violating allocations.
approach:
  - Uses quarterly PCE components (durable, nondurable, services) from FRED as macro demand proxy.
  - Compares seasonal naïve, SARIMAX, gradient boosting, and VAR in rolling backtest (2018Q1-2025Q3).
  - Estimates marketing response from Advertising dataset (TV, radio, newspaper) using OLS, ridge, lasso, GBR, and Hill saturation model.
  - Calibrates financial constraints (gross margin, SG&A ratio, cash flow) from Apple Inc. FY2025 Form 10-K.
  - Solves constrained portfolio optimization with Monte Carlo evaluation over budget allocations.
findings:
  - num: Multivariate VAR improves aggregate demand accuracy with ≈2.85% MAPE.
  - num: Newspaper spend has near-zero marginal ROI; radio saturates quickly, TV saturates slowly.
  - Optimal marketing spend lies below the SG&A ratio cap due to diminishing returns.
  - num: Spending at the deterministic cap yields ≈40% violation probability under demand uncertainty.
  - num: Risk-aversion parameter λ=2 reduces budget utilization from 0.97% to 0.60% of revenue.
  - Hill model provides interpretable saturation curves while gradient boosting gives best predictive fit (CV_RMSE=0.661).
  - Channel shares (25% TV, 75% radio) remain stable across ±5% macro scenarios.
  - Tighter marketing cap (1.0% of revenue) reduces SG&A satisfaction rate to 94.8%.
  - Higher assumed marketing effectiveness (5% revenue lift) pushes spend to cap but drops satisfaction to 59.8%.
  - Operating profit objective uses gross margin minus non-marketing expenses (≈33.5% of incremental revenue).
key_figures_tables:
  - Table 7: Demand forecasting accuracy by category → VAR lowest RMSE for durables and services.
  - Table 8: Total demand proxy accuracy → VAR achieves 2.85% MAPE, improving over seasonal naïve.
  - Figure 2: Total demand actual vs VAR forecasts → errors widen around 2020 but recover.
  - Figure 4: Hill-model response curves → diminishing returns for TV and radio, flat for newspaper.
  - Figure 5: Marginal response curves → radio highest initial ROI, TV moderate, newspaper near zero.
  - Table 9: Baseline optimal budget (λ=0) → $1,016M spend, 25% TV, 75% radio, $5,735M incremental revenue.
  - Table 11: Risk-aversion sensitivity → λ≥1 reduces spend to $938M, slightly lower profit and std.
key_equations:
  - equation: "\\Pi(b) = (g - o)(R + \\Delta R(b)) - \\sum b_i"
    explanation: Operating profit after incremental revenue and marketing spend.
  - equation: "\\sum b_i \\leq \\kappa R"
    explanation: SG&A constraint limits marketing spend to fixed revenue share.
  - equation: "\\mathbb{P}(B \\leq \\kappa R) \\geq 1 - \\delta"
    explanation: Chance constraint for ratio-based cap under uncertain revenue.
  - equation: "Sales(s) = \\beta_0 + \\sum_i \\beta_i h(s_i; \\alpha_i, \\gamma_i)"
    explanation: Hill saturation model for diminishing marketing returns.
  - equation: "\\hat{R}_{t+1} = \\rho \\frac{\\hat{P}_{t+1}}{4}"
    explanation: Maps macro demand forecast to quarterly firm revenue.
definitions:
  - term: FP&A
    definition: Financial Planning and Analysis, budgeting and forecasting function.
  - term: PCE
    definition: Personal Consumption Expenditures, a measure of consumer spending.
  - term: VAR
    definition: Vector Autoregression, multivariate time series model.
  - term: SG&A
    definition: Selling, General and Administrative expenses.
  - term: Hill function
    definition: Saturation curve modeling diminishing returns in marketing response.
  - term: SARIMAX
    definition: Seasonal ARIMA with exogenous regressors.
  - term: SAAR
    definition: Seasonally Adjusted Annual Rate, quarterly data scaled to annual.
  - term: CFO
    definition: Cash Flow from Operations.
  - term: MAPE
    definition: Mean Absolute Percentage Error, scale-free accuracy metric.
  - term: Chance constraint
    definition: Constraint that must hold with a minimum probability.
critical_citations:
  - "[Box et al., 2015] — Foundational time series forecasting methods."
  - "[Hanssens et al., 2001] — Market response models with saturation."
  - "[Markowitz, 1952] — Mean-variance optimization for portfolio allocation."
  - "[Bertsimas & Sim, 2004] — Robust optimization framework for uncertainty."
  - "[James et al., 2021] — Source of Advertising dataset and linear models."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      justification: Compares multiple forecasting models for demand, applicable to spending prediction.
    - code: 6.B
      name: Spending Forecasting Algorithm
      justification: Rolling backtest of VAR and gradient boosting for macro demand forecasting.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      justification: Introduces chance constraints and buffers for ratio-based budget caps.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      justification: End-to-end constrained optimization for marketing spend allocation.
    - code: 7.C
      name: Budget Recommendation Algorithm
      justification: Grid search with Monte Carlo evaluation under demand uncertainty.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: Compares multiple forecasting and response models with RMSE, MAPE, R².
  contribution: This paper provides a framework for budget recommendation under uncertainty that combines demand forecasting, response modeling, and accounting constraints. For Odin's budget recommendation module (7.B), it demonstrates how to treat spending caps as feasibility boundaries rather than targets, using chance constraints to buffer against revenue volatility. The rolling backtest methodology (12.B) offers a template for evaluating forecasting algorithms on spending data. The use of saturation functions (Hill model) for diminishing returns directly informs how Odin might model non-linear effects of budget changes on financial outcomes.
  directly_justifies:
    - "Optimal budgets may be below ratio caps due to diminishing returns."
    - "Spending at a deterministic cap yields 40% violation probability under demand uncertainty."
    - "Multivariate forecasting improves aggregate demand accuracy over univariate baselines."
    - "Risk-averse optimization reduces budget utilization to create constraint buffers."
    - "Channel shares remain stable across macro scenarios, simplifying execution."
  limits:
    - "Data sources are not internally consistent (macro PCE vs small cross-sectional marketing dataset)."
    - "Marketing response assumed contemporaneous; no adstock or carryover effects modeled."
    - "Constraint calibration uses Apple Inc. data, which may not generalize to other firms."
    - "Normalization mapping response units to dollars is stylized, not empirically estimated."
  mapping_rationale: This paper was screened against Odin's functional domains. Budget recommendation (domain 7) is the primary match because the paper proposes a constrained optimization framework for allocating spend under accounting constraints. Spending forecasting (domain 6) applies due to the demand forecasting module comparing multiple time series models. System evaluation (domain 12) applies from the rolling backtest and cross-validation comparisons. Behavioral profiling (5), anomaly detection (8), categorization (3), mobile design (9), privacy (10), retention (11), and savings/debt (13) are not addressed. Selected codes 6.A, 6.B, 7.A, 7.B, 7.C, 12.B capture the full methodological contribution.
limitations:
  - "Macro PCE and Advertising datasets are not internally consistent; response-to-dollar normalization is arbitrary. [acknowledged]"
  - "No adstock or carryover effects in marketing response, limiting dynamic budgeting. [acknowledged]"
  - "Constraint calibration uses a single firm (Apple); results may not transfer to other sectors. [acknowledged]"
  - "Grid search scales poorly with more than three channels. [unacknowledged]"
  - "Assumes constant market share parameter ρ, which may drift over time. [unacknowledged]"
remember_this:
  - "Optimal budgets often sit below ratio caps due to diminishing returns."
  - "VAR forecasting achieved 2.85% MAPE for aggregate demand proxy."
  - "Newspaper spend showed near-zero marginal ROI in the Advertising dataset."
  - "Spending at the deterministic cap violates constraints 40% of the time under uncertainty."
  - "Risk aversion reduces budget utilization to create safety buffers against revenue shortfalls."
```