```yaml
paper_id: 10.1371/journal.pone.0294466
designation: international
title: Impact of financial literacy, mental budgeting and self control on financial wellbeing: Mediating impact of investment decision making
authors: Bai, R.
year: 2023
venue: PLOS ONE
odin_topics:
  - 3.A
  - 5.A
shorthand_tags:
  - /expense-categorization
  - /behavioral-profiles
tldr: Financial literacy, mental budgeting, and self-control positively affect subjective financial wellbeing, with investment decision making partially mediating these relationships.
problem_and_motivation: Financial stress harms mental health and productivity. Understanding cognitive factors like financial literacy, mental budgeting, and self-control that influence subjective financial wellbeing is needed. The mediating role of investment decision making in these relationships has not been fully examined.
approach:
  - Data were collected from 449 Chinese university students via convenience sampling using physical and electronic channels.
  - The study employed Partial Least Squares Structural Equation Modeling (PLS-SEM) for path analysis and mediation testing.
  - Financial literacy was measured with 7 items, mental budgeting with 4 items, and self-control with 5 items from the Brief Self-Control Scale.
  - Investment decision making behavior was measured with 9 items, and financial wellbeing with 7 items covering financial anxiety and security.
  - Hypotheses were tested for direct effects and mediation following Baron and Kenny's approach.
findings:
  - num: Financial literacy has a direct positive effect on financial wellbeing (beta = 0.299, p < 0.001).
  - num: Mental budgeting has a direct positive effect on financial wellbeing (beta = 0.102, p < 0.001).
  - num: Self-control has a direct positive effect on financial wellbeing (beta = 0.182, p < 0.001).
  - num: Investment decision making partially mediates the effect of financial literacy on financial wellbeing (indirect effect = 0.017, p = 0.034).
  - num: Investment decision making partially mediates the effect of mental budgeting on financial wellbeing (indirect effect = 0.016, p = 0.035).
  - num: Investment decision making partially mediates the effect of self-control on financial wellbeing (indirect effect = 0.019, p = 0.036).
key_figures_tables:
  - Figure 1: Conceptual model of financial literacy, mental budgeting, self-control, investment decision making, and financial wellbeing → All hypothesized paths were supported.
  - Table 3: Path coefficients for direct effects → All direct effects significant except DMB->FWB at p=0.059.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: PLS-SEM
    definition: Partial Least Squares Structural Equation Modeling, a variance-based SEM method.
  - term: Financial wellbeing
    definition: Subjective evaluation of one's present and future financial situation.
  - term: Mental budgeting
    definition: Cognitive process of mentally classifying and monitoring income and expenses.
  - term: Self-control
    definition: Ability to manage impulses and behaviors to achieve long-term goals.
  - term: Financial literacy
    definition: Knowledge of financial concepts and ability to make informed financial decisions.
  - term: Investment decision making
    definition: Process of choosing financial investments influenced by knowledge, attitude, and behavior.
critical_citations:
  - "[Thaler, 1999] — Introduced mental accounting theory underpinning mental budgeting."
  - "[Tangney et al., 2004] — Provided the Brief Self-Control Scale used in this study."
  - "[Baron & Kenny, 1986] — Established the mediation testing framework applied here."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      justification: Mental budgeting involves mentally categorizing expenses into budgets.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      justification: Self-control and mental budgeting are behavioral traits linked to financial wellbeing.
  contribution: This paper justifies Odin's use of mental budgeting as a cognitive expense categorization mechanism for user profiling. It supports incorporating self-control measures into behavioral profile classification to predict financial wellbeing. The mediation via investment decision making suggests that Odin's recommendation modules should consider investment behavior as an intermediate outcome.
  directly_justifies:
    - Individuals with higher self-control achieve better financial outcomes.
    - Mental budgeting practice improves subjective financial wellbeing.
    - Financial literacy positively influences investment decisions.
    - Investment decision making partially transmits the effects of cognitive factors to financial wellbeing.
  limits:
    - Student sample limits generalizability to young professionals.
    - Cross-sectional design prevents causal inference.
    - Self-reported measures may introduce response bias.
  mapping_rationale: The paper focuses on cognitive-behavioral factors (financial literacy, mental budgeting, self-control) and their impact on subjective financial wellbeing. It does not address Filipino young professionals specifically, nor algorithmic implementation. Topic 3.A is selected because mental budgeting directly involves mental categorization of expenses, relevant to Odin's expense categorization module. Topic 5.A is selected because self-control and mental budgeting are behavioral profile attributes that can inform user classification. Topics related to forecasting, anomaly detection, system design, or mobile UX were rejected as the paper does not discuss them. The paper is international and non-algorithm-specific.
limitations:
  - Student sample limits generalizability to broader populations.
  - Cross-sectional design cannot establish causality.
  - Self-reported measures may be subject to social desirability bias.
remember_this:
  - Financial literacy has direct beta 0.299 on financial wellbeing.
  - Mental budgeting directly improves financial wellbeing.
  - Self-control influences financial wellbeing via investment decisions.
  - Investment decision making partially mediates all three relationships.
```