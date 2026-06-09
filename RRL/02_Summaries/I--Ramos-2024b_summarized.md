```yaml
paper_id: fc5e6d7c-8b9a-4a1e-9f2d-3c4b5a6d7e8f
designation: international
title: Essays on the Causes and Consequences of Employment Uncertainty
authors: Ramos, Vincent Jerald R.
year: 2024
venue: Hertie School
odin_topics:
  - 1.C
  - 5.A
  - 13.A
shorthand_tags:
  - /financial-behavior
  - /behavioral-profiling
  - /savings-management
tldr: Employment uncertainty, operationalized through informal work, fixed-term contracts, recession entry, social class, and caregiving, has persistent negative effects on fertility behavior and intentions across the Philippines and Germany.
problem_and_motivation: Employment uncertainty is a global phenomenon with profound demographic consequences, yet its multiple dimensions and causal effects on fertility are understudied. Prior research lacks integration of various uncertainty types and robust causal identification. This dissertation examines how different forms of employment uncertainty affect fertility decisions across contexts.
approach:
  - Chapter 2 uses difference-in-differences on Philippine Labor Force Surveys (2016-2020) to estimate extreme lockdown effects on informal employment.
  - Chapter 3 uses optimal full matching and Cox PH models on German SOEP to analyze fixed-term and recession entry effects on first birth hazards within 10 years.
  - Chapter 4 uses piecewise constant event history and cure fraction models on SOEP to assess social class and second birth rates.
  - Chapter 5 uses a factorial survey experiment (vignettes) on SOEP-IS to test future caregiving and employment uncertainty effects on ascribed fertility intentions.
findings:
  - "num: Extreme lockdowns increased informal employment probability by 1.7 percentage points for women but not for men."
  - "num: Female fixed-term labor market entrants had a 19% lower first birth hazard within 10 years."
  - "num: Male recession entrants had a 23% lower first birth hazard within 10 years."
  - "Upper service class members have strongly elevated second birth rates compared to semi-/unskilled workers."
  - "num: No future caregiving responsibilities increased ascribed fertility intentions by 2.8 points on a 0-10 scale."
key_figures_tables:
  - "Figure 2.3: Informal employment trends by lockdown status and gender → sharp increase for women in lockdown regions."
  - "Table 3.1: Cox PH results for fixed-term entry → females have 0.813 hazard ratio (19% lower)."
  - "Table 4.3: Second birth hazard ratios by social class → upper service class as reference, lower classes have 0.58-0.79 hazard ratios."
  - "Figure 5.1: Effect of caregiving and employment uncertainty → no responsibilities increases intentions by 2.8 and 1.9 units."
key_equations:
  - equation: "F_{c,t} = α + γ U_{c,t-1} + δ D_{c,t-1} + ω M_{c,t-1} + θ Z_{c,t} + ϵ_t"
    explanation: "Fertility rate as function of lagged unemployment and controls."
  - equation: "h(t|X) = h_0(t) × exp(βx)"
    explanation: "Proportional hazard model for second birth transitions."
definitions:
  - term: Employment uncertainty
    definition: "Umbrella term covering positional, durational, statutory, recessionary, class-based, subjective, and caregiving dimensions of job insecurity."
  - term: Informal employment
    definition: "Non-professional own-account workers and contributing family workers outside agriculture and government."
  - term: Fixed-term contract
    definition: "Time-bound employment without guarantee of renewal or permanent conversion."
  - term: Recession entry
    definition: "Labor market entry during an officially classified recession year (1993, 2002, 2003, 2009 in Germany)."
  - term: Social class (EGP schema)
    definition: "Occupation-based categories reflecting employment relations and economic vulnerability."
  - term: Ascribed fertility intentions
    definition: "Respondent's rating of a hypothetical couple's likelihood of having a child, not their own intention."
critical_citations:
  - "[Blossfeld et al., 2006] — Typology of economic, temporal, and employment uncertainty."
  - "[Vignoli et al., 2020] — Narrative framework emphasizing future-oriented uncertainty."
  - "[Alderotti et al., 2021] — Meta-analysis of employment instability and fertility in Europe."
  - "[Goldstein et al., 2013] — Fertility reactions to the Great Recession in Europe."
relevance:
  topics:
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      justification: "Chapter 2 analyzes how extreme lockdowns gendered informal employment in the Philippines, a key financial behavior context."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      justification: "The dissertation profiles individuals by multiple employment uncertainty dimensions (fixed-term, recession entry, class, caregiving) and their fertility responses."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      justification: "The survivalist motive mechanism in Chapter 2 shows lack of savings forces informal work, supporting need for emergency savings features."
  contribution: "The dissertation's findings justify a behavioral profiling module that incorporates employment uncertainty dimensions to predict financial stress and life course decisions. The analysis of informal employment in the Philippines informs Odin's expense categorization for gig economy and precarious workers. The survivalist motive evidence supports a savings goal management feature that prioritizes emergency funds for users with unstable income. The gendered effects highlight the need for gender-sensitive financial planning tools."
  directly_justifies:
    - "Extreme lockdowns increase informal employment probability for women by 1.7 percentage points."
    - "Female fixed-term labor market entrants have 19% lower first birth hazard within a decade."
    - "Male recession entrants have 23% lower first birth hazard within a decade."
    - "Couples with no future caregiving responsibilities have 2.8 point higher fertility intentions on a 0-10 scale."
    - "Upper service class individuals have 42% higher second birth rates than semi-/unskilled workers."
  limits:
    - "The dissertation does not evaluate PFMS systems or user behavior within such apps."
    - "Findings are context-specific to the Philippines and Germany and may not generalize to other populations."
  mapping_rationale: "The dissertation primarily contributes to understanding employment uncertainty and fertility, which indirectly informs financial behavior (1.C) as employment uncertainty affects spending, saving, and risk-taking patterns. Behavioral profiling (5.A) is supported by the systematic classification of uncertainty types (positional, durational, statutory, recessionary, class-based, subjective, caregiving) and their differential effects on life outcomes. Savings goal management (13.A) is relevant due to the survivalist motive mechanism in Chapter 2, where lack of precautionary savings forces informal work as a coping strategy. Codes related to expense categorization (3.A, 3.B), spending forecasting (6), budget recommendation (7), anomaly detection (8), mobile design (9), data privacy (10), user retention (11), and system evaluation (12) were rejected as the paper does not address these PFMS-specific functions. Borderline cases like class-based uncertainty (which could map to 5.A) were included under behavioral profiling."
limitations:
  - "LFS data undercounts informal employment, potentially underestimating lockdown effects."
  - "Analysis in Chapter 3 limited to first 10 years post-entry due to sample attrition."
  - "Vignette experiment measures ascribed intentions, not actual fertility behavior. [unacknowledged]"
  - "Findings may not generalize beyond Germany and Philippines due to contextual specificities."
  - "The dissertation does not empirically mediate the pathways from employment uncertainty to fertility (e.g., income vs. subjective worries). [unacknowledged]"
remember_this:
  - "Extreme lockdowns increased women's informal employment by 1.7 percentage points."
  - "Fixed-term entry reduces first birth hazard for women by 19% over 10 years."
  - "Male recession entrants have 23% lower first birth hazard within a decade."
  - "No future caregiving responsibilities raises fertility intentions by 2.8 points."
  - "Upper service class members have 42% higher second birth rates than lower classes."
```