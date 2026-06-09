```yaml
paper_id: 10.34001/jmer.2025.12.06.4-80
designation: international
title: Behavioral Shifts in Digital Finance: How E-Payment Influences Consumer Spending and Financial Literacy
authors: Yuttama, F. R.
year: 2025
venue: Journal of Management and Entrepreneurship Research
odin_topics:
  - 1.C
  - 7.A
shorthand_tags:
  - /financial-behavior
  - /budgeting-strategies
tldr: E-payment usage increases consumer spending but also improves cash management, with financial literacy moderating both effects: higher literacy reduces impulsive spending and enhances use of digital tracking tools.
problem_and_motivation: Prior studies on e-payment's behavioral effects are inconclusive, with some finding increased impulsive spending and others improved financial tracking. The role of financial literacy as a boundary condition shaping these dual outcomes remains underexplored, particularly in emerging markets like Indonesia. This gap limits the ability to design effective digital finance policies and consumer education programs.
approach:
  - Surveyed 400 active e-payment users in Central Java, Indonesia, using a structured Likert-scale questionnaire.
  - Measured e-payment usage, consumer spending behavior, cash management, and financial literacy with validated multi-item scales.
  - Analyzed relationships using PLS-SEM with bootstrapping (5,000 resamples) to test direct and moderation effects.
  - Assessed measurement model via factor loadings, Cronbach's alpha (>0.87), and AVE (>0.65), confirming convergent and discriminant validity.
  - Tested hypotheses for H1 (e-payment→spending), H2 (e-payment→cash management), H3 (literacy weakens spending effect), H4 (literacy strengthens cash management effect).
findings:
  - "num: E-payment usage positively affects consumer spending (β=0.731, p<0.000)."
  - "num: E-payment usage positively affects cash management (β=0.493, p<0.000)."
  - "num: Financial literacy weakens the positive effect of e-payment on spending (β=-0.082, p<0.000)."
  - "num: Financial literacy strengthens the positive effect of e-payment on cash management (β=-0.065, p<0.005)."
  - "num: The model explains 87.7% of variance in consumer behavior and 83.1% in cash management (R²)."
key_figures_tables:
  - "Figure 1: E-payment transaction value growth in Central Java (2023-2024) → QRIS transactions grew 385% year-on-year."
  - "Figure 2: PLS-SEM structural model results → Path coefficients show significant direct and moderation effects."
  - "Table 4: Reliability and validity metrics → All constructs meet thresholds (Cronbach's α >0.87, AVE >0.65)."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: PLS-SEM
    definition: Partial Least Squares Structural Equation Modeling, a variance-based SEM method.
  - term: AVE
    definition: Average Variance Extracted, a measure of convergent validity.
  - term: HTMT
    definition: Heterotrait-Monotrait ratio, a criterion for discriminant validity.
  - term: QRIS
    definition: Quick Response Code Indonesian Standard, a national QR code payment system.
  - term: MSME
    definition: Micro, Small, and Medium Enterprises.
critical_citations:
  - "[Lusardi & Mitchell, 2014] — Financial literacy theory foundation."
  - "[Thaler & Sunstein, 2008] — Pain of paying concept."
  - "[Hampson et al., 2021] — E-payment increases impulsive spending."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      justification: Examines how e-payment usage influences consumer spending and cash management behaviors, moderated by financial literacy in an emerging market.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      justification: Shows that e-payment enhances cash management through tracking and budgeting features, with financial literacy strengthening this effect.
  contribution: This paper justifies Odin's use of financial literacy as a moderating factor in spending forecasting and budget recommendation modules. It supports the inclusion of in-app nudges (spend alerts, category caps) to curb impulsive spending, particularly for low-literacy users. The dual-effect finding (e-payment increases both spending and cash management) informs Odin's anomaly detection by distinguishing between beneficial and harmful spending patterns. The moderation effect validates personalizing budget recommendations based on user financial literacy levels.
  directly_justifies:
    - E-payment usage increases consumer spending propensity by reducing psychological friction at checkout.
    - E-payment usage improves cash management through automated transaction tracking and budgeting features.
    - Higher financial literacy weakens the positive relationship between e-payment and impulsive spending.
    - Higher financial literacy strengthens the positive relationship between e-payment and cash management.
  limits:
    - Geographical focus on Central Java, Indonesia, limiting generalizability to other regions.
    - Reliance on self-reported survey data may introduce social desirability bias.
    - Cross-sectional design cannot establish causality or capture behavioral dynamics over time.
  mapping_rationale: The paper was screened against Odin's functional domains. Behavioral profiling (5.A-C) was rejected because the paper does not classify users into distinct profiles but uses financial literacy as a continuous moderator. Spending forecasting (6.A-B) was rejected as no predictive modeling is performed. Budget recommendation (7.A-C) was partially selected: 7.A (budgeting strategies) applies because the paper empirically demonstrates that e-payment's tracking features support budgeting, and financial literacy enhances this. 7.B and 7.C were rejected as no recommendation algorithm is proposed. Expense categorization (3.A-B) and anomaly detection (8.A-B) were not relevant. Savings & debt (13.A-B) was rejected as savings are mentioned only peripherally. The selected codes 1.C (financial behavior) and 7.A (budgeting strategies) capture the paper's core contribution on how digital payment affects spending and cash management with financial literacy as a boundary condition.
limitations:
  - Geographical focus on Central Java, Indonesia, limiting generalizability.
  - Self-reported data may introduce social desirability bias.
  - Cross-sectional design cannot establish causality.
  - Excludes other moderators such as income and digital literacy [unacknowledged].
remember_this:
  - E-payment increases spending (β=0.731) but also improves cash management (β=0.493).
  - Financial literacy weakens e-payment's spending effect (β=-0.082).
  - Financially literate users leverage digital tracking for better budgeting.
  - The model explains 87.7% of spending behavior variance.
```