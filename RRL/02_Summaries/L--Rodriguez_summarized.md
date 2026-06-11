```yaml
paper_id: 10.20944/preprints202409.1696.v1
designation: local
title: The Mediation of Financial Behavior to Financial Literacy and Spending Habits of Gen Z: An Exploratory Factor Analysis
authors: Rodriguez, J. M. P.; Labong, M. D. C. G.; Palallos, L. Q.
year: 2024
venue: Preprints.org
odin_topics:
  - 1.A
  - 1.C
  - 5.A
shorthand_tags:
  - /filipino-demographic
  - /financial-behavior
  - /behavioral-profiles
tldr: Financial literacy directly increases spending habits, and financial behavior partially mediates this relationship among Gen Z in the Philippines.
problem_and_motivation: Understanding how financial literacy translates into actual spending is poorly understood for Gen Z. Prior research shows that financial knowledge alone does not guarantee responsible spending. The mediating role of financial behavior remains underexplored in this demographic.
approach:
  - Data from 317 Gen Z respondents (aged 18-25) across four barangays in Quezon City, Philippines.
  - Structured questionnaire measured financial literacy, financial behavior, and spending habits using validated scales.
  - Applied Pearson correlation, regression, mediation analysis (bootstrapped CIs), and Structural Equation Modeling.
  - Tested direct effects, indirect effects via financial behavior, and total effects with path analysis.
findings:
  - "num: Pearson's r = 0.821 between financial literacy and spending habits (p < .001)."
  - "num: Direct effect of financial literacy on spending is 0.642 (p < .001)."
  - "num: Indirect mediation effect through financial behavior is 0.180 (p < .001, 95% CI 0.114 to 0.245)."
  - Financial literacy explains 51.9% of variance in financial behavior (R²=0.519).
  - SEM path coefficient from financial behavior to spending is 0.797, exceeding the direct literacy-to-spending path of 0.642 in the full model.
  - Indicator loadings for all constructs exceed 0.5, confirming measurement model adequacy.
key_figures_tables:
  - "Figure 1: Conceptual framework with direct and mediated paths → Financial behavior is a partial mediator."
  - "Figure 2: Path plot analysis → Confirms significant mediation at p < .001."
  - "Figure 4: Structural equation model coefficients → Literacy→Spending=1.167, Behavior→Spending=0.797."
  - "Table 1: Correlation between literacy and spending → r=0.821, p<.001."
  - "Table 6: Regression summary for behavior → R²=0.519, literacy explains 52% variance."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "Gen Z"
    definition: "Individuals born approximately 1997-2012, aged 18-25 in this study."
  - term: "Financial literacy"
    definition: "Knowledge and understanding of financial concepts enabling effective money management."
  - term: "Financial behavior"
    definition: "Actions and habits related to managing personal finances, including budgeting and saving."
  - term: "Spending habits"
    definition: "Patterns of expenditure on goods and services."
  - term: "SEM"
    definition: "Structural Equation Modeling, a multivariate statistical technique for testing causal relationships."
  - term: "CFA"
    definition: "Confirmatory Factor Analysis, used to assess measurement model fit."
  - term: "AVE"
    definition: "Average Variance Extracted, a measure of convergent validity."
critical_citations:
  - "[Shan et al., 2023] — Links financial literacy to goal setting and planning."
  - "[Rodriguez et al., 2024] — High literacy associates with more spending, not less."
  - "[Anjani & Darto, 2023] — Literacy interacts with income and self-control to shape behavior."
  - "[Azmi & Ramakrishnan, 2018] — Financial knowledge correlates with desirable financial behavior."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      justification: "Study samples Gen Z from Quezon City, Philippines, representing local young adults."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      justification: "Directly measures and models financial behavior as a mediator between literacy and spending."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      justification: "Exploratory factor analysis reveals how financial behavior shapes spending, informing profile design."
  contribution: "Odin's behavioral profiling module can use the finding that financial behavior mediates literacy's effect on spending to design a two-stage prediction model. The spending forecasting module can incorporate both financial literacy scores and observed financial behavior as separate inputs. The budget recommendation system should prioritize behavior change interventions because behavior has a 0.797 direct coefficient on spending. User retention may benefit from financial literacy education that explicitly links knowledge to behavioral practice."
  directly_justifies:
    - "Financial literacy alone does not directly determine spending; financial behavior is a necessary mediator."
    - "Improving financial behavior can translate literacy gains into responsible spending habits."
    - "Financial literacy accounts for 51.9% of variance in financial behavior among young Filipinos."
    - "The path coefficient from financial behavior to spending (0.797) exceeds the direct literacy effect (0.642) in the full model."
  limits:
    - "Cross-sectional design cannot establish causality."
    - "Sample limited to four barangays in Quezon City, not nationally representative."
    - "All measures self-reported, risking social desirability bias."
    - "AVE values below 0.5 suggest convergent validity concerns for spending and literacy constructs."
  mapping_rationale: "This paper studies financial literacy, behavior, and spending habits of Gen Z in the Philippines. I flagged the domain 'Behavioral profiling & classification' because the paper uses exploratory factor analysis to identify relationships between financial constructs, which can inform user profiling. Topic 1.A (Filipino Young Professionals) is selected because the sample is from Quezon City and the demographic overlaps with Odin's target users. Topic 1.C (Financial Behavior) is directly studied. Topic 5.A (Financial Behavioral Profiles) is selected because the mediation model and factor loadings provide empirical support for how financial behavior operates as a distinct profile dimension. I rejected topics related to algorithms (6.A, 7.C, 8.B) because no predictive models are implemented. Topics on mobile design (9.A, 9.B) and data privacy (10.A, 10.B) are absent. Topic 13.A (savings) is mentioned in passing but not central. Borderline case: Topic 2.C (User-Declared Preferences) was rejected because the study measures behavior via validated scales, not user-declared preferences for system features."
limitations:
  - "Sample size of 317 from only 4 barangays limits generalizability."
  - "Cross-sectional design cannot confirm mediation temporally [unacknowledged]."
  - "AVE below 0.5 for spending and literacy indicates weak convergent validity [unacknowledged]."
  - "No control for income or personality traits despite literature suggesting their importance."
remember_this:
  - "Financial behavior mediates 22% of literacy's effect on spending."
  - "Literacy explains 52% of variance in financial behavior among Gen Z."
  - "SEM path from behavior to spending is 0.797, larger than direct literacy path 0.642."
  - "Higher financial literacy correlates with more spending, not less."
```