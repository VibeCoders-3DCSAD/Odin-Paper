```yaml
paper_id: 10.21203/rs.3.rs-7730348/v1
designation: international
title: Mental Accounting Through Two-stage Budgeting Under Bounded Rationality
authors: Pretnar, N.; Olivola, C. Y.; Montgomery, A.
year: 2025
venue: Research Article (preprint)
odin_topics:
  - 5.A
  - 5.C
  - 6.A
  - 6.B
  - 7.A
  - 13.A
  - 13.B
shorthand_tags:
  - /behavioral-profiles
  - /classification-algorithm
  - /predictive-modeling
  - /spending-forecasting
  - /budgeting-strategies
  - /savings-management
  - /debt-management
tldr: A model of two-stage budgeting with cognitive constraints shows consumers exhibit heterogeneous bounded rationality, updating only half of budgets weekly, with mental accounting affecting spending and savings.
problem_and_motivation: Classical two-stage budgeting assumes perfect fungibility and ex-post budget adherence. Behavioral evidence suggests consumers use mental accounting and sticky budgets, but field evidence is lacking. This paper quantifies how cognitive constraints and budget rigidities explain observed expenditure patterns.
approach:
  - Builds a dynamic model with planner/doer structure, mental accounting state variable, and sparse budget updates.
  - Uses weekly agent-level expenditure data from 2,509 low-income prepaid debit card users spanning September 2013 to January 2016.
  - Estimates structural parameters via Bayesian MCMC with latent change-point inference, sampling over four million parameters.
  - Compares models with different numeracy thresholds (relative percentage or absolute dollar margins).
  - Classifies consumers into four ex-ante (budget) and four ex-post (spending) behavioral types based on responsiveness to prior over/under-spending.
  - Simulates counterfactual of forcing full budget attention (k=J every period) to assess welfare and bankruptcy risk.
findings:
  - "num: Consumers update only 2.48 budgets per week on average (out of 4 categories) in baseline, 2.11 with $1 numeracy threshold."
  - "num: 68% of consumers do not benefit from forced weekly full budget updates; 3.3% go bankrupt under forced attention in $1-threshold model."
  - Ex-ante most consumers (79%) are budget prioritizers (mental accounting), but ex-post a plurality (43-47%) are spendthrifts who increase spending regardless of prior over/under-spending.
  - Heterogeneous rationality: most consumers are neither fully rational (always update all budgets) nor fully bounded (never update).
  - Bankrupt consumers have stickier budgets (1.25 updates/week vs. sample average 2.11-2.48) and exhibit planning fallacy syndrome.
  - A $1 numeracy threshold reduces budget updates by 14.9% compared to baseline.
key_figures_tables:
  - "Figure 2: Time series of actual vs. predicted weekly expenditure for median income consumer → both baseline and $1-threshold models fit well."
  - "Figure 3: Posterior density of average weekly budget updates per consumer → updates drop significantly with higher numeracy thresholds."
  - "Table 3: Marginal distributions of ex-ante and ex-post types → 79% ex-ante are budget prioritizers, but only 11% ex-post are same type."
  - "Table 4: Joint distributions of types → 38% are ex-ante budget prioritizers and ex-post spendthrifts."
key_equations:
  - equation: "\\omega_{ijt} = \\theta_{ijt} \\ell_{it} + \\gamma_i a_{ijt}"
    explanation: "Budget as function of income share and mental account balance."
  - equation: "x_{ijt} = \\omega_{ijt} + \\zeta_{ijt}"
    explanation: "Actual expenditure equals budget plus idiosyncratic shock."
  - equation: "a_{ij,t+1} = -\\zeta_{ijt}"
    explanation: "Mental account updates as negative of previous shock."
definitions:
  - term: Mental accounting
    definition: "Book-keeping mechanism where past over/under-spending affects future budgets, limiting fungibility."
  - term: Bounded rationality
    definition: "Cognitive constraints that prevent consumers from updating all budgets every period."
  - term: Narrow choice bracketing
    definition: "Updating only a subset of spending categories each period due to attention limits."
  - term: Numeracy constraint
    definition: "Budget change is implemented only if candidate budget differs sufficiently from current budget."
  - term: Personal mental accounting equilibrium
    definition: "Consistent decision outcome under sparse-max budgeting and mental account dynamics."
  - term: Budget prioritizer
    definition: "Consumer who reduces spending after over-spending and increases after under-spending."
  - term: Spendthrift
    definition: "Consumer who increases spending after both over- and under-spending."
critical_citations:
  - "[Thaler, 1985] — Foundational mental accounting with over/under-spending tracking."
  - "[Gabaix, 2014] — Sparse maximization framework for bounded rationality."
  - "[Deaton and Muellbauer, 1980] — Classical two-stage budgeting with perfect fungibility."
  - "[Shefrin and Thaler, 1981] — Planner/doer model of self-control."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      justification: "Classifies consumers into four ex-ante and ex-post behavioral types based on budget responsiveness."
    - code: 5.C
      name: Financial Behavioral Profile Classification Algorithm
      justification: "Uses latent change-point inference to recover individual budgeting decisions from expenditure data alone."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      justification: "Predicts weekly expenditure with a dynamic structural model incorporating cognitive constraints."
    - code: 6.B
      name: Spending Forecasting Algorithm
      justification: "Forecasts spending using mental accounting state variables and sparse budget updates."
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      justification: "Models budgeting strategies with cognitive constraints, numeracy thresholds, and mental accounting anchoring."
    - code: 13.A
      name: Savings Goal Management in PFMS
      justification: "Analyzes savings outcomes and welfare under counterfactual attention policies, showing forced attention harms many."
    - code: 13.B
      name: Debt Management in PFMS
      justification: "Examines bankruptcy risk from over-spending cycles due to budget stickiness and planning fallacy."
  contribution: "This paper provides a structural model that Odin could use to infer latent user budgets from spending data alone. The classification of users into ex-ante (budget) and ex-post (spending) types (budget prioritizers vs. spendthrifts) directly informs Odin's behavioral profiling module (5.A, 5.C). The finding that forced full budget attention reduces welfare for 68% of users suggests Odin should use adaptive, personalized nudge timing rather than constant reminders. The counterfactual analysis on bankruptcy risk (3.3% under $1 threshold) informs Odin's debt management and savings goal features (13.A, 13.B)."
  directly_justifies:
    - "Consumers update only a subset of budgets each period due to cognitive constraints."
    - "Forcing full budget attention reduces welfare for 68% of consumers."
    - "Bankrupt consumers exhibit stickier budgets and planning fallacy syndrome."
    - "Ex-ante budget prioritizers often become ex-post spendthrifts."
    - "A $1 numeracy threshold reduces budget updates by 14.9%."
  limits:
    - "Data limited to low-income prepaid debit card users, not generalizable to all populations."
    - "Model assumes strong separability and Stone-Geary utility, which may restrict flexibility."
    - "Prices are imputed from CPI, not observed at transaction level."
    - "Latent budgeting inference is model-dependent and not directly validated with observed budgets."
    - "Household size and composition unknown, affecting interpretation of per-capita spending."
  mapping_rationale: "Selected topics focus on behavioral profiling (5.A, 5.C) due to consumer type classification, predictive modeling (6.A, 6.B) for expenditure forecasting, budgeting strategies (7.A) for the two-stage budgeting model, and savings/debt management (13.A, 13.B) for welfare and bankruptcy analysis. Rejected topics: 1.A (not Filipino YPs), 2.A/B (no cultural or seasonal patterns), 3.A/B (expense categorization not central), 4.A/B (landscape not discussed), 8.A/B (no anomaly detection), 9.A/B (mobile design absent), 10.A/B (privacy not addressed), 11.A/B (engagement/retention not directly studied), 12.A/B (evaluation frameworks not primary). Borderline case 5.C: the paper infers latent budgets via changepoint detection, which is a classification algorithm for behavioral states, so included."
limitations:
  - "Data limited to low-income prepaid debit card users, not generalizable. [unacknowledged]"
  - "Model assumes strong separability and Stone-Geary utility, potentially unrealistic. [unacknowledged]"
  - "Latent budgeting inference is model-dependent and lacks direct validation. [acknowledged]"
  - "Prices imputed from CPI, not observed at transaction level. [acknowledged]"
  - "Household size unknown, affecting interpretation of individual vs. household spending. [unacknowledged]"
remember_this:
  - "2.11 average weekly budget updates under $1 numeracy threshold."
  - "68% of users worse off with full budget attention."
  - "Bankrupt consumers have only 1.25 updates per week."
  - "Most consumers are neither fully rational nor fully behavioral."
```