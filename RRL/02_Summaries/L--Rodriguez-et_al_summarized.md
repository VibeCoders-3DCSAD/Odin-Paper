```yaml
paper_id: 10.20944/preprints202409.1696.v1
designation: local
title: The Mediation of Financial Behavior to Financial Literacy and Spending Habits of Gen Z: An Exploratory Factor Analysis
authors: Rodriguez, J. M. P.; Labong, M. D. C. G.; Palallos, L. Q.
year: 2024
venue: Preprints.org
odin_topics:
  - 1.C
  - 5.A
  - 7.A
  - 13.A
shorthand_tags:
  - /fin-behavior-young-pros
  - /behavioral-profiles
  - /budgeting-strategies
  - /savings-management
tldr: Financial behavior mediates the relationship between financial literacy and spending habits among Gen Z, with significant direct and indirect effects.
problem_and_motivation: Understanding how financial literacy translates into actual spending behavior remains poorly understood, especially for Gen Z. Existing research shows financial literacy is associated with spending, but the mediating role of financial behavior has been underexplored. This study addresses the gap by examining mediation effects.
approach:
  - Data from 317 Gen Z respondents aged 18-25 in Quezon City using stratified random sampling.
  - Structured questionnaire measuring financial literacy, financial behavior, and spending habits based on validated scales.
  - Pearson correlation, regression analysis, mediation analysis, and Structural Equation Modeling (SEM).
  - Confirmatory Factor Analysis (CFA) to assess model fit and construct validity.
  - Path analysis to examine direct and indirect effects.
findings:
  - "num: Pearson correlation r=0.821 (p<0.001) between financial literacy and spending habits."
  - "num: Direct effect of financial literacy on spending is 0.642 (p<0.001)."
  - "num: Indirect mediation effect through financial behavior is 0.180 (p<0.001)."
  - "num: Total effect of financial literacy on spending is 0.821."
  - "num: Financial literacy explains 51.9% of variance in financial behavior (R²=0.519)."
  - "num: Path coefficient from financial literacy to financial behavior is 0.721."
  - Financial behavior mediates the relationship, confirming its essential role.
key_figures_tables:
  - "Figure 1: Conceptual framework showing direct and indirect paths → financial behavior mediates."
  - "Table 1: Correlation analysis r=0.821 → strong positive relationship."
  - "Table 3: Indirect effect 0.180 → significant mediation."
  - "Figure 2: Path plot analysis → visual confirmation of mediation."
  - "Table 13: SEM coefficients → financial literacy to spending 1.167, behavior to spending 0.797."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Gen Z"
    definition: "Individuals aged 18-25 years old in this study."
  - term: "Financial literacy"
    definition: "Knowledge and understanding of financial concepts and decision-making."
  - term: "Financial behavior"
    definition: "Actions and practices related to managing personal finances, e.g., budgeting and saving."
  - term: "Spending habits"
    definition: "Patterns and tendencies in consumption and expenditure."
  - term: "SEM"
    definition: "Structural Equation Modeling, a multivariate statistical analysis technique."
  - term: "CFA"
    definition: "Confirmatory Factor Analysis, used to test measurement model validity."
critical_citations:
  - "[Shan et al., 2023] — Financial literacy enables goal setting and future planning."
  - "[Rodriguez et al., 2024] — Higher literacy linked to more spending behavior."
  - "[Anjani & Darto, 2023] — Literacy interacts with income and self-control on behavior."
relevance:
  topics:
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      justification: "Paper quantifies financial behavior as a mediator for Gen Z spending habits."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      justification: "Explores how behavioral profiles (literacy-driven) affect spending outcomes."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      justification: "Financial behavior includes budgeting and saving, directly relevant to recommendation systems."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      justification: "Findings show literacy improves saving behavior, informing savings module design."
  contribution: "The mediation analysis directly informs Odin's behavioral profiling module (5.A) by quantifying how financial behavior translates literacy into spending. The path coefficients (0.642 direct, 0.180 indirect) provide benchmarks for Odin's spending forecasting (6.A) and budget recommendation (7.A) systems. The finding that financial literacy explains 51.9% of behavioral variance guides Odin's cold-start profile initialization (5.B). The validated measurement model (CFA) offers a template for evaluating Odin's categorization and anomaly detection modules."
  directly_justifies:
    - "Financial literacy has a direct positive effect on spending behavior (coefficient 0.642)."
    - "Financial behavior mediates the relationship between financial literacy and spending (indirect effect 0.180)."
    - "Increased financial literacy leads to improved financial behavior (standardized coefficient 0.721)."
    - "Higher financial literacy correlates with more spending (Pearson r=0.821)."
  limits:
    - "Sample limited to four barangays in Quezon City, not nationally representative."
    - "Cross-sectional design cannot establish causality over time."
    - "AVE values below 0.5 for spending (0.415) and literacy (0.404) indicate modest convergent validity. [unacknowledged]"
    - "Preprint not peer-reviewed; findings may change after review."
  mapping_rationale: "The paper was screened against Odin's functional domains. Behavioral profiling & classification (domain 5) applies directly because it models financial behavior as a mediator. Spending forecasting (domain 6) is partially relevant but no predictive model is built; however, the correlation and path coefficients can inform forecasting priors. Budget recommendation (domain 7) is supported by the emphasis on budgeting and saving as key behaviors. Expense categorization (domain 3) and anomaly detection (domain 8) are not addressed. Mobile-first design (domain 9) and data privacy (domain 10) are absent. Selected codes: 1.C (financial behavior of young Filipinos), 5.A (behavioral profiles), 7.A (budgeting strategies), 13.A (savings goal management). Rejected codes like 3.A (categorization) and 8.A (anomaly detection) because no mention of transaction classification or outlier identification. Borderline case: 2.C (user-declared preferences) was rejected as the study uses observed behavior not declared preferences."
limitations:
  - "Sample restricted to Gen Z in Quezon City, limiting generalizability to other regions or age groups."
  - "Self-reported questionnaire data may introduce social desirability or recall bias."
  - "Reliability for financial literacy construct (Cronbach's α=0.6568) is below the commonly accepted 0.70 threshold. [unacknowledged]"
  - "No longitudinal follow-up to assess stability of mediation effects over time."
remember_this:
  - "Financial behavior mediates 18% of literacy's effect on spending."
  - "Financial literacy explains 51.9% of variance in financial behavior."
  - "Higher financial literacy correlates with more spending (r=0.821)."
  - "Targeted financial education should emphasize behavioral skills over knowledge alone."
```