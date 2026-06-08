```yaml
paper_id: 10.3390/ijfs13040222
designation: local
title: Exploring the Interplay of Life Attitude and Cognitive Ability in Shaping the Intention to Stock Market Participation Among Young Professionals in the Philippines
authors: Mutuc, E. B.
year: 2025
venue: International Journal of Financial Studies
odin_topics:
  - 1.A
  - 1.C
  - 5.A
shorthand_tags:
  - /filipino-yp
  - /financial-behavior
  - /behavioral-profile
tldr: Life attitude profile positively influences stock market participation intention among Filipino young professionals, with cognitive ability (financial literacy) mediating this relationship.
problem_and_motivation: The stock market participation puzzle has been examined through economic, demographic, and cognitive lenses, but the role of broader psychological orientations such as life attitude remains underexplored. Young professionals in emerging economies like the Philippines face unique financial contexts yet lack empirical study. Understanding how life purpose and meaning interact with cognitive ability to shape investment intentions is critical for designing behavioral interventions.
approach:
  - A quantitative cross-sectional survey of 195 randomly selected young professionals (aged 20-39, white-collar) in Bulacan, Philippines.
  - Life Attitude Profile-Revised (LAP-R) measured seven existential dimensions on a 7-point scale.
  - Cognitive ability proxied by financial literacy using van Rooij et al. (2011) 16-item inventory.
  - PLS-SEM with SmartPLS 4.0 used to estimate direct, indirect, and mediating effects.
  - Bootstrapping with 5000 resamples assessed significance; control variables (sex, age, education, employment) and multi-group analyses performed.
findings:
  - "num: Life attitude profile has a positive direct effect on stock market participation intention (β=0.154, p=0.025)."
  - "num: Cognitive ability mediates the relationship between life attitude and participation intention (indirect β=0.051, p=0.032)."
  - "num: Death acceptance (β=0.312, p<0.001) and goal seeking (β=0.396, p=0.009) positively predict intention."
  - Life purpose negatively predicts stock market intention (β=-0.243, p=0.036).
  - "num: The model explains 47.1% to 58.2% of variance in participation intention (R²=0.471-0.582)."
  - "num: Cognitive ability directly and strongly predicts intention (β=0.329, p<0.001)."
key_figures_tables:
  - "Figure 1: Conceptual framework showing LAP → SMP direct path and LAP → C → SMP mediation → Life attitude and cognition jointly shape investment intention."
  - "Table 2: Internal consistency and convergent validity (α>0.70, AVE>0.50) → Measurement model is reliable and valid."
  - "Table 5: Hypothesis testing results including direct and indirect effects → Mediation by cognitive ability is significant."
  - "Figure 4: Higher-order structural model with path coefficients (LAP→SMP β=0.154, C→SMP β=0.329) → Cognition exerts stronger direct influence than life attitude."
key_equations:
  - equation: "SMP_i = β_0 + β_1(LAP_i) + ε_i"
    explanation: "Life attitude directly predicts stock market intention."
  - equation: "C_i = β_0 + β_1(LAP_i) + ε_i"
    explanation: "Life attitude predicts cognitive ability."
  - equation: "SMP_i = β_0 + β_1(LAP_i) + β_2(CA_i) + ε_i"
    explanation: "Both LAP and cognitive ability jointly predict SMP."
definitions:
  - term: LAP
    definition: "Life Attitude Profile, a multidimensional measure of existential meaning, purpose, and control."
  - term: SMP
    definition: "Intention to Stock Market Participation, the dependent variable measuring willingness to invest in equities."
  - term: PLS-SEM
    definition: "Partial Least Squares Structural Equation Modeling, a variance-based technique for testing mediation and prediction."
  - term: LAP-R
    definition: "Life Attitude Profile-Revised, instrument assessing seven dimensions including life purpose, goal seeking, and death acceptance."
critical_citations:
  - "[van Rooij et al., 2011] — Financial literacy predicts stock market participation."
  - "[Haliassos & Bertaut, 1995] — Foundational stock market participation puzzle."
  - "[Reker et al., 1987] — Developed Life Attitude Profile framework."
  - "[Lusardi & Mitchell, 2014] — Economic importance of financial literacy."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      justification: "Study focuses exclusively on Filipino young professionals aged 20-39 in Bulacan."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      justification: "Examines stock market participation intention as a specific financial behavior."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      justification: "Life attitude dimensions (purpose, goal seeking, death acceptance) constitute a behavioral profile that predicts investment intention."
  contribution: "This paper justifies Odin's behavioral profiling module (5.A) by demonstrating that life attitude dimensions (purpose, goal seeking, death acceptance) predict financial behavior. It supports the inclusion of cognitive ability measures (financial literacy) as a mediator in spending forecasting (6.A) or budget recommendation (7.A) by showing that knowledge enhances intention. The findings inform Odin's design for Filipino young professionals (1.A, 1.C) by highlighting purpose-driven and goal-seeking orientations as key behavioral drivers that can be targeted for personalized nudges."
  directly_justifies:
    - "Life attitude profile directly influences stock market participation intention among young professionals."
    - "Cognitive ability mediates the effect of life attitude on investment intention."
    - "Death acceptance and goal seeking are positively associated with intention to participate in stock markets."
    - "Life purpose can negatively predict investment intention when values are conservative."
  limits:
    - "Cross-sectional design restricts causal inference."
    - "Sample from Bulacan province limits generalizability to other Philippine regions or national contexts."
    - "No marker variable for common method variance; Harman's test and VIF used instead."
    - "LAP-R used in original English without local cultural adaptation or pilot testing."
    - "Sample size of 195 is below the targeted 384, potentially affecting power [unacknowledged]."
  mapping_rationale: "The paper was screened against Odin's functional domains. Behavioral profiling (5.A) applies because life attitude is a psychological profile that predicts financial behavior. Filipino young professionals (1.A) is directly targeted as the sample. Financial behavior (1.C) is the outcome (stock market intention). Domains such as spending forecasting, budget recommendation, anomaly detection, and mobile design received no support because the paper does not model time-series spending, generate budget rules, detect outliers, or address UX. Cognitive ability as a mediator informs predictive modeling (6.A) but is not a direct algorithm, so 6.A was omitted. Savings & debt management (13.A) is tangentially related to investment but not explicitly about goal setting within a PFMS, so it was rejected. Borderline case: death acceptance as a predictor is novel but fits within behavioral profiling."
limitations:
  - "Self-reported data may introduce response and social desirability bias."
  - "Cross-sectional design prevents causal conclusions. [unacknowledged]"
  - "Sample from Bulacan limits generalizability to other regions."
  - "No marker variable for common method variance; alternative tests used but are less robust. [unacknowledged]"
  - "LAP-R not culturally adapted or piloted for the Philippine population."
  - "Sample size (195) below initial target (384), potentially reducing statistical power. [unacknowledged]"
remember_this:
  - "Life attitude directly affects stock market intention (β=0.154)."
  - "Cognitive ability mediates 39% of life attitude's effect on investment."
  - "Death acceptance and goal seeking are strong positive predictors of intention."
  - "Life purpose can reduce investment intention due to conservative values."
  - "Financial literacy enhances translation of life attitudes into action."
```