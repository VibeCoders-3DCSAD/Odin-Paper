```yaml
paper_id: c5a2e4b7-9d8f-4c3a-8e1b-6f4d2a9c7e3b
designation: local
title: Effects of Filipino Consumers’ Financial Attitudes, Subjective Norms, and Perceived Behavioral Control on Intentions to Formal Banking: Towards Financial Inclusion
authors: Co, M.; Centeno, D.D.G.
year: 2023
venue: Philippine Management Review
odin_topics:
  - 1.C
  - 5.A
  - 13.A
shorthand_tags:
  - /financial-behavior
  - /savings-intention
  - /tpb
tldr: Filipino consumers' intentions to save surplus money in formal banks are significantly predicted by subjective norms and perceived behavioral control, but not by attitudes.
problem_and_motivation: Financial exclusion in the Philippines is often attributed to cost and lack of funds, yet attitudinal and psychological factors remain underexplored. Understanding how attitudes, social influences, and perceived control affect banking intentions can improve financial inclusion strategies. This study addresses the gap by applying the Theory of Planned Behavior to a national consumer finance survey.
approach:
  - Data from the Bangko Sentral ng Pilipinas Consumer Financial Survey 2014 with 15,503 randomly sampled households.
  - Dependent variable is intention to put surplus money in a bank deposit account (binary).
  - Independent variables include attitude toward banking, subjective norm (household member with bank account), and perceived behavioral control (two items on earning and saving enough).
  - Logistic regression used to estimate effects, with average marginal effects computed via delta method.
  - Demographic controls include education, gender, age, income, employment, pension membership, and household size.
findings:
  - "num: Having a banked household member increases intention probability by 10.16% (p<0.001)."
  - "num: Perceived ability to earn enough to save regularly increases intention probability by 1.42% per unit (p=0.024)."
  - "num: College graduates have 7.95% higher probability of intention than non-college graduates (p<0.001)."
  - "num: Males have 2.02% higher probability of intention than females (p=0.030)."
  - "num: Middle-income individuals have 3.18% higher probability than low-income (p=0.002)."
  - "num: Baby boomers have 2.80% lower probability of intention than millennials (p=0.036)."
  - Attitude toward banking was not a significant predictor of intention.
  - Unemployed respondents showed higher intention than employed ones, contrary to expectation.
key_figures_tables:
  - "Figure 1: Conceptual framework of Theory of Planned Behavior for banking intentions → Attitudes, subjective norms, PBC lead to intention."
  - "Table 3: Logistic regression results → Subjective norms and perceived behavioral control significant, attitudes not."
  - "Table 4: Marginal effects of independent variables → Subjective norm has largest positive effect at 10.16%."
key_equations:
  - equation: "logit(P(Bank=1)) = \\beta_0 + \\beta_1 X_1 + \\beta_2 X_2 + ... + \\beta_k X_k"
    explanation: "Logistic regression for binary intention outcome."
definitions:
  - term: "Theory of Planned Behavior (TPB)"
    definition: "Behavioral intention predicted by attitude, subjective norm, and perceived behavioral control."
  - term: "Perceived Behavioral Control (PBC)"
    definition: "Individual's perception of ease or difficulty in performing a behavior."
  - term: "Subjective Norms"
    definition: "Perceived social pressure to perform or not perform a behavior."
critical_citations:
  - "[Ajzen, 1991] — Foundational TPB framework."
  - "[BSP, 2014] — Source of survey data."
  - "[Rutherford & DeVaney, 2009] — TPB applied to credit card use."
relevance:
  topics:
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      justification: "Studies financial intentions and behaviors of Filipinos including working-age adults."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      justification: "Uses TPB factors (attitudes, norms, control) to profile banking intentions."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      justification: "Directly examines intentions to save surplus money in formal bank accounts."
  contribution: "Odin can leverage the finding that subjective norms (household members with bank accounts) strongly influence banking intentions to design social features like family savings goals. The non‑significant effect of attitudes suggests Odin should prioritize perceived behavioral control and social proof over attitudinal messaging. Demographic insights (education, income, age, gender) inform targeted savings recommendations and budget assignment for different user segments. The TPB framework provides a validated model for predicting user savings intentions within Odin's behavioral profiling module."
  directly_justifies:
    - "Subjective norms from household members increase intention to save in banks by 10.16%."
    - "Perceived behavioral control over earning enough money positively predicts banking intention."
    - "College graduates have higher banking intentions than non‑graduates."
    - "Males have higher banking intentions than females."
    - "Middle‑income individuals are more likely to intend formal savings than low‑income."
  limits:
    - "Data from 2014 may not reflect current digital banking and fintech adoption. [unacknowledged]"
    - "Attitudes measured via single Likert item may lack reliability compared to multi‑item scales."
    - "The study measures intention, not actual savings behavior, which may overstate real action."
  mapping_rationale: "The paper was screened against Odin's functional domains. Behavioral profiling (5.A) applies because TPB factors (attitudes, norms, control) are direct inputs for user financial profiles. Savings & debt management (13.A) applies because the outcome is intention to save surplus money in banks. Financial behavior of Filipinos (1.C) applies as the sample includes working‑age adults relevant to young professionals. Domains like expense categorization (3.A), spending forecasting (6.A), and budget recommendation (7.A) were rejected as no categorization or forecasting is performed. The paper does not address mobile design, privacy, or retention."
limitations:
  - "Cross‑sectional design limits causal inference."
  - "Data from 2014 may be outdated for current financial behavior."
  - "Self‑reported intentions may not translate to actual behavior."
  - "Low pseudo R² (0.0094) indicates model explains little variance."
remember_this:
  - "Subjective norms from household members increase banking intention by 10.16%."
  - "Perceived ability to earn enough money predicts savings intention."
  - "Attitudes alone do not significantly predict banking intentions."
  - "College graduates and males show higher banking intentions."
```