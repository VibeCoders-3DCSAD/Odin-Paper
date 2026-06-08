```yaml
paper_id: 10.1016/j.actpsy.2025.105334
designation: local
title: Financial literacy and sustainable planning assessment among Filipino millennials
authors: Dimaunahan, D. S. F.; Santiago, A. F. B.; Eusebio, M. C. C.; Loteriña, S. M. M.; Ong, A. K. S.; Chavez, J. X. S.
year: 2025
venue: Acta Psychologica
odin_topics:
  - 1.C
  - 13.A
shorthand_tags:
  - /filipino-demographic
  - /financial-behavior
  - /goal-setting
  - /savings-goal-management
tldr: Financial literacy among Filipino millennials is low and does not directly affect financial planning, but monthly income, occupation, and monthly expenses significantly influence planning via goal setting theory constructs.
problem_and_motivation: Filipino millennials exhibit low financial literacy and poor financial decision-making, yet no recent studies have assessed their financial literacy and planning. Understanding these factors is crucial for improving financial inclusion and sustainable planning in the Philippines.
approach:
  - Data were collected from 400 Filipino millennials in Makati City via online and in-person surveys.
  - Financial literacy was measured using Lusardi and Mitchell's "Big Three" questions on interest compounding, inflation, and risk diversification.
  - Financial planning was operationalized through goal setting theory constructs: goal commitment, specificity, acceptance, and difficulty.
  - Structural equation modeling (PLS-SEM) was used to test four hypotheses on direct effects of financial literacy and demographics on planning.
  - Respondents had low literacy scores (means of 0.545, 0.388, and 0.338 for the three concepts).
findings:
  - "num: Mean correct scores were 0.545 for interest compounding, 0.388 for inflation, and 0.338 for risk diversification."
  - "num: Financial literacy had no significant direct effect on financial planning (β=0.077, p=0.153)."
  - "num: Monthly expenses (β=0.205, p=0.001) and monthly income (β=0.180, p=0.003) showed significant effects on financial planning."
  - "num: Goal acceptance (β=0.924) and goal commitment (β=0.809) were the strongest predictors of financial planning among goal setting constructs."
  - "Occupation also had a significant but smaller effect (β=0.164, p=0.004)."
key_figures_tables:
  - "Figure 2: Initial SEM showing low factor loading for financial literacy → negligible impact on planning."
  - "Table 2: Statistical analysis of indicators → mean correct answers for financial literacy concepts are below 0.55."
  - "Figure 3: Final SEM after removing low-loading items → monthly expenses, income, and occupation significantly affect financial planning."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "The Big Three"
    definition: "Three financial literacy questions covering interest compounding, inflation, and risk diversification (Lusardi & Mitchell, 2011)."
  - term: "Goal Setting Theory (GST)"
    definition: "Theory by Locke and Latham (1990) stating that specific, challenging goals enhance performance through commitment, specificity, acceptance, and difficulty."
  - term: "SEM"
    definition: "Structural equation modeling, a multivariate statistical analysis technique."
  - term: "PLS-SEM"
    definition: "Partial least squares structural equation modeling, used for prediction and theory development."
critical_citations:
  - "[Lusardi & Mitchell, 2011] — Standardized 'Big Three' financial literacy measure."
  - "[Locke & Latham, 1990] — Foundational goal setting theory framework."
  - "[S&P Financial Literacy Survey, 2014] — Only 25% of Filipino adults are financially literate."
relevance:
  topics:
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      justification: "Directly assesses financial literacy and planning behavior of Filipino millennials."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      justification: "Uses goal setting theory (commitment, specificity, acceptance, difficulty) to model financial planning, directly applicable to savings goal features."
  contribution: "This paper quantifies the low baseline financial literacy of Filipino millennials, informing Odin's behavioral profiling module (topic 1.C). It demonstrates that demographic factors (income, expenses, occupation) dominate planning behavior, guiding budget recommendation algorithms to prioritize these inputs. The validated goal setting constructs provide a framework for designing savings goal management features (topic 13.A) that leverage goal acceptance and commitment to drive user engagement."
  directly_justifies:
    - "Financial literacy does not directly affect financial planning among Filipino millennials."
    - "Monthly income and expenses are significant determinants of financial planning behavior."
    - "Goal acceptance and goal commitment are strong predictors of financial planning in this demographic."
  limits:
    - "Sample limited to Makati City, not representative of all Filipino millennials."
    - "Only one financial literacy measurement (The Big Three) was used."
    - "Quantitative only; mixed methods could deepen insights."
    - "Cross-sectional design; causal claims require longitudinal data."
  mapping_rationale: "The paper directly studies financial behavior of Filipino young professionals (topic 1.C) through literacy and planning measures. Goal setting theory applied to financial planning maps to savings goal management (13.A). No algorithm is proposed, so topics 5.C (classification algorithm) and 7.C (budget recommendation algorithm) are rejected. No spending forecasting (6.A/B), anomaly detection (8.A/B), or expense categorization (3.A/B) are present. Demographic factors are analyzed but not as a cold-start profile (5.B)."
limitations:
  - "Only Makati City residents were surveyed, limiting generalizability."
  - "Only millennials were included; older generations may differ."
  - "Only 'The Big Three' questions measured financial literacy; other dimensions omitted."
  - "Mixed-method approach recommended but not used."
  - "Cross-sectional design prevents causal inference."
remember_this:
  - "Only 0.545 mean correct on interest compounding, 0.388 on inflation, 0.338 on risk diversification."
  - "Financial literacy had no significant effect on financial planning (p=0.153)."
  - "Monthly expenses and income were stronger predictors than financial literacy."
  - "Goal acceptance (β=0.924) and commitment (β=0.809) drive financial planning."
```