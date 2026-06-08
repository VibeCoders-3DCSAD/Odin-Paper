```yaml
paper_id: 10.1051/bioconf/20249305010
designation: local
title: Decoding the eco-financial mindset: financial literacy, attitudes, and efficacy measures and the spending behavior of Filipino millennials
authors: Lim, C. T.; Cordova, W.
year: 2024
venue: BIO Web of Conferences
odin_topics:
  - 1.A
  - 1.C
  - 5.A
shorthand_tags:
  - /filipino-young-professionals
  - /financial-behavior
  - /behavioral-profiles
tldr: Survey of 431 Filipino millennials finds strong positive correlations among financial literacy, attitude, and efficacy, and a negative correlation between spending behavior and financial attitude.
problem_and_motivation: Existing literature often examines financial literacy, attitude, and efficacy in isolation or paired combinations, leaving a gap in comprehensive understanding. Filipino millennials face economic uncertainties and lack financial acumen, making them financially vulnerable. A holistic exploration of these variables together is needed to inform targeted interventions.
approach:
  - Online survey of 431 millennials in Laguna, Philippines using Google Forms.
  - Measured financial literacy (7 items), attitude (8 items), efficacy (10 items), and spending behavior (9 categories) via Likert scales.
  - Used Structural Equation Modeling (SEM) and Confirmatory Factor Analysis (CFA) in Jamovi.
  - Evaluated model fit with RMSEA, CFI, TLI, SRMR, AIC, BIC.
  - Reported Cronbach’s alpha (0.656–0.917) and VIF to check multicollinearity.
findings:
  - "num: Strong positive correlations: financial efficacy ↔ literacy (β=0.614, p<.001), attitude ↔ literacy (β=0.578, p<.001), attitude ↔ efficacy (β=0.888, p<.001)."
  - "num: Negative relationship between spending behavior and financial attitude (β=-0.176, p=0.034)."
  - "num: 42% of respondents spend 41% or more of their income (S1)."
  - "num: 93.7% spend 10% or less of income on beer and wine (S9, SD=0.521)."
  - Financial literacy and efficacy showed no statistically significant direct effect on spending.
  - CFA fit indices indicated adequate model fit for all latent variables (RMSEA 0.092–0.163).
  - Most respondents had moderate financial literacy (mean=3.42) and positive attitudes (mean=3.69).
key_figures_tables:
  - "Table 1: Categorical socio-demographics of 431 respondents → Majority male (62.9%), aged 26-27 (45.5%), monthly income P20k-27k (50.8%)."
  - "Table 3: Spending construct frequency → Highest variability in total spent income, lowest in beer/wine."
  - "Table 4: CFA baseline comparison indices → Acceptable to moderate fit (RMSEA 0.092-0.163, CFI 0.810-0.955)."
  - "Figure 1: SEM path diagram with standard coefficients → Visualizes strong positive paths among literacy, attitude, efficacy."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: SEM
    definition: Structural Equation Modeling, a multivariate technique for testing complex variable relationships.
  - term: CFA
    definition: Confirmatory Factor Analysis, validates latent variable measurement models.
  - term: TPB
    definition: Theory of Planned Behavior, links attitudes, norms, and control to behavioral intentions.
  - term: RMSEA
    definition: Root Mean Square Error of Approximation, a model fit index (lower is better).
  - term: CFI
    definition: Comparative Fit Index, measures model improvement over null (≥0.90 acceptable).
  - term: TLI
    definition: Tucker-Lewis Index, a non-normed fit index.
  - term: SRMR
    definition: Standardized Root Mean Square Residual, absolute fit index (<0.08 good).
critical_citations:
  - "[Ajzen, 1991] — Foundation for Theory of Planned Behavior used."
  - "[Yanto et al., 2021] — Social media’s role in financial literacy among millennials."
  - "[Dewi et al., 2020] — Links financial literacy, attitude, and behavior."
  - "[Sotiropoulos & d'Astous, 2013] — Supports financial attitude preventing overspending."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      justification: Studies millennials (ages 26–42) in Laguna, many employed in finance-related jobs.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      justification: Directly measures spending behavior and its correlates (literacy, attitude, efficacy).
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      justification: Identifies interdependencies among literacy, attitude, and efficacy, shaping spending patterns.
  contribution: "This paper provides empirical evidence on how financial literacy, attitude, and efficacy interrelate and affect spending behavior among Filipino millennials, directly informing Odin’s behavioral profiling module (5.A). The negative relationship between financial attitude and spending supports the design of budget recommendation algorithms that prioritize attitudinal interventions (7.B). The detailed breakdown of spending categories (e.g., groceries, dining, credit payments) offers a foundation for expense categorization frameworks (3.A) and spending forecasting features (6.A)."
  directly_justifies:
    - "Financial attitude has a significant negative relationship with spending behavior among Filipino millennials (β=-0.176, p=0.034)."
    - "Financial literacy and financial attitude are strongly positively correlated (β=0.578, p<0.001), suggesting they reinforce each other."
    - "Most Filipino millennials (42%) spend 41% or more of their income, indicating high spending propensity."
  limits:
    - "Self-reported data may introduce recall and social desirability bias."
    - "Cross-sectional design limits causal inference and temporal tracking."
    - "Sample from only Laguna, Philippines, not generalizable to all Filipino millennials [unacknowledged]."
    - "Overrepresentation of respondents in finance-related jobs may inflate financial literacy scores."
  mapping_rationale: "The paper squarely targets Filipino millennials (1.A) and their spending behavior (1.C), making it highly relevant to Odin’s demographic and behavioral domains. The identification of interdependencies among literacy, attitude, and efficacy directly supports financial behavioral profiling (5.A). Topics related to algorithms (e.g., 6.B, 7.C, 8.B) are rejected because the paper uses SEM/CFA, not predictive or anomaly detection models. Expense categorization (3.A) is borderline; the paper reports spending by category but does not propose a classification framework, so it was excluded. Similarly, no mobile design, privacy, retention, or savings/debt management content appears, so those codes are omitted."
limitations:
  - "Reliance on self-reported Likert scales may introduce bias."
  - "Cross-sectional design prevents observation of behavioral changes over time."
  - "Sample predominantly from Laguna, limiting geographic generalizability [unacknowledged]."
  - "High proportion of finance-related job respondents may skew financial knowledge measures."
  - "Cronbach’s alpha for spending construct (0.656) is below conventional thresholds [unacknowledged]."
remember_this:
  - "Financial attitude negatively predicts spending behavior (β=-0.176)."
  - "42% of Filipino millennials spend over 41% of their income."
  - "Financial literacy and attitude are strongly correlated (β=0.578)."
  - "93.7% allocate 10% or less of income to alcohol."
```