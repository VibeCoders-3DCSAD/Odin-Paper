```yaml
paper_id: d9b7a8c6-5f4e-3d2c-1b0a-9e8f7d6c5b4a
designation: international
title: Consumers semi-intertemporally make intertemporal decisions: insights from the payday effects
authors: Ma, C.; Gu, Y.; Chong, J. K.
year: 0
venue: Unknown
odin_topics:
  - 1.C
  - 2.B
  - 5.A
  - 7.A
  - 13.A
shorthand_tags:
  - /financial-behavior
  - /payday-cycle
  - /behavioral-profile
  - /mental-budgeting
  - /savings-goal
tldr: Analysis of storable product purchase data reveals that consumers self-impose monthly mental budgets, renewing them on paydays, leading to larger expenditures on first post-payday trips and decreasing expenditures over subsequent trips.
problem_and_motivation: Consumers are neither fully rational nor completely myopic, yet existing models do not explain how they make intertemporal purchase decisions for storable products without liquidity constraints. The gap is understanding the intrinsic commitment devices like mental budgeting that consumers use to manage spending across pay cycles. This paper provides empirical evidence for monthly mental budgets and the role of payday salience.
approach:
  - Analyzed individual-level transaction data from a retail chain selling storable products (cosmetics, personal care) from 2011-2015 in a Southeast Asian country.
  - Used regression discontinuity design around paydays (26th of each month) with customer-day and customer-trip level regressions.
  - Compared cash users vs credit card users to isolate liquidity constraints vs behavioral effects.
  - Controlled for prices, customer fixed effects, store fixed effects, seasonality, and holidays.
  - Examined expenditures, basket size, new product purchases, product upgrading, and purchase mistakes.
findings:
  - "num: Expenditures on paydays are 3.3% higher conditional on store visit."
  - "num: For credit card users, first trip after payday (non-payday) has 0.726 higher expenditure than later trips."
  - "num: Payday effect increases variety seeking by 0.1 varieties for credit card users."
  - "num: Probability of purchasing a new variety increases by 0.63% on paydays."
  - "num: Purchase mistakes (new variety never repurchased) increase by 1.08% on paydays."
  - Mental budget renewing explains 75% of payday effect for cash users, 55% for credit card users; salience explains the rest.
  - Expenditures decrease over trips within paycheck cycle, supporting monthly mental budgeting.
key_figures_tables:
  - "Figure 1: Unconditional daily expenditure spikes on payday → Payday increases spending."
  - "Figure 2: Conditional expenditure spikes on payday → Effect due to spending more, not more trips."
  - "Figure 3: Variety seeking, new-product trying, upgrading, consumption rate spike on paydays → Real effects beyond stockpiling."
  - "Figure 4: Purchase mistakes spike on paydays → Projection bias on paydays."
  - "Figure 5: First-trip expenditure drops sharply from payday to day after, then flat → Salience effect, not just mental budget renewing."
  - "Table 4: Expenditure decreases over trips within cycle → Monthly mental budget depletion."
key_equations:
  - equation: "\\max_{e} U(e) + g(h - e)"
    explanation: "Utility maximization with mental budget constraint."
  - equation: "\\frac{1-\\delta^{\\bar{t}}}{1-\\delta} \\frac{1}{\\bar{t}} u'\\left(\\frac{e}{\\bar{t}}\\right) - g'(h-e) = 0"
    explanation: "First order condition: marginal utility equals pain from spending."
  - equation: "u(b, \\text{non-payday} | \\text{payday}) = (1-\\alpha)u(b, \\text{non-payday}) + \\alpha u(b, \\text{payday})"
    explanation: "Projection bias during payday overestimates future utility."
definitions:
  - term: Mental budget
    definition: Self-imposed monthly spending limit based on target saving rate.
  - term: Salience
    definition: Phenomenon where payday draws attention, reducing perceived pain of spending.
  - term: Projection bias
    definition: Tendency to project current tastes (e.g., payday mood) onto future.
  - term: Payday effect
    definition: Increased spending on payday and first trip after payday.
  - term: Storable product
    definition: Goods that can be stored and consumed over multiple periods.
critical_citations:
  - "[Amador et al., 2006] — Optimal commitment imposes minimum savings."
  - "[Thaler, 1985] — Mental accounting and transaction utility."
  - "[Loewenstein et al., 2003] — Projection bias formalization."
  - "[Stephens, 2006] — Payday effect on consumption."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      justification: Demonstrates financial behavior patterns including mental budgeting and payday spending.
    - code: 2.B
      name: Seasonal and Cyclical Spending Patterns
      justification: Documents cyclical spending around monthly paydays.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      justification: Defines behavioral profile of self-imposed monthly mental budget users.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      justification: Provides empirical basis for rule-of-thumb budgeting strategies as commitment devices.
    - code: 13.A
      name: Savings Goal Management in PFMS
      justification: Shows consumers target saving rates within monthly budgets.
  contribution: "Odin's behavioral profiling module (5.A) can incorporate monthly mental budgeting as a distinct financial behavior pattern identified by this paper. The spending forecasting module (6.A) should account for payday cycles and first-trip-after-payday spikes, as well as decreasing expenditure over trips within a cycle. The budget recommendation module (7.A) can leverage the finding that users may respond well to monthly mental budgets with target saving rates, and that salience of paydays can be designed to encourage saving. The savings goal management module (13.A) can use the observed rule-of-thumb saving behavior to structure goal-based budgets."
  directly_justifies:
    - "Consumers self-impose monthly mental budgets even without liquidity constraints."
    - "Payday salience causes overspending beyond mental budget renewal."
    - "First trip after payday (non-payday) has larger expenditure than later trips."
    - "Expenditures on storable products decrease over trips within a paycheck cycle."
    - "Credit card users are more susceptible to payday salience than cash users."
    - "Projection bias is triggered by payday salience, not by mental budget renewing."
  limits:
    - "Study focused on upper-middle-class consumers in one Southeast Asian country; may not generalize to lower-income populations."
    - "Data limited to one retail chain with high brand loyalty; results may differ for non-loyal customers."
    - "[unacknowledged] The model assumes consumers know number of future trips; not validated."
    - "[unacknowledged] Causal identification relies on RD design, but unobserved confounding on paydays possible."
  mapping_rationale: "The paper primarily addresses financial behavior (1.C) through the lens of cyclical payday spending patterns (2.B). It defines a specific behavioral profile (5.A) of consumers who use monthly mental budgets as a self-control device. The budgeting strategy described (7.A) provides domain knowledge for rule-of-thumb budget recommendations. The target saving rate behavior informs savings goal management (13.A). Topics related to classification algorithms (5.C), forecasting (6.A), anomaly detection (8.A), expense categorization (3.A), mobile design (9.A), privacy (10.A), retention (11.A), evaluation (12.A), and debt management (13.B) were rejected as the paper does not provide citable claims for those Odin modules. Borderline case 2.C (user-declared preferences) was rejected because the paper infers behavior from transactions, not declared preferences."
limitations:
  - "Data only covers one retail chain in one country; external validity limited."
  - "RD design assumes no other events coinciding with paydays; may be confounded by end-of-month effects."
  - "Cannot fully rule out stockpiling as alternative explanation for some findings [unacknowledged]."
  - "Model of mental budgeting assumes consumers know future trip counts, which is unrealistic."
remember_this:
  - "Monthly mental budgets renew on paydays, not just on payday itself."
  - "Expenditures decrease over trips within a paycheck cycle."
  - "Payday salience causes overspending beyond mental budget renewal."
  - "Credit card users are more sensitive to payday salience than cash users."
  - "Projection bias on paydays leads to purchase mistakes."
```