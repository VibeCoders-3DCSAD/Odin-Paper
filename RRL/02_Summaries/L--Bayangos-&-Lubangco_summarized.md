```yaml
paper_id: d4f8c2a1-5e6b-4c7d-9a8b-1f2e3d4c5b6a
designation: local
title: Do Remittances Boost Household Spending: New Evidence from Migrants’ Household Survey
authors: Bayangos, V. B.; Lubangco, C. K.
year: 2024
venue: Bangko Sentral ng Pilipinas Discussion Paper
odin_topics:
  - 1.C
  - 3.A
  - 5.A
  - 6.A
  - 13.A
  - 13.B
shorthand_tags:
  - /financial-behavior
  - /expense-categorization
  - /behavioral-profiles
  - /spending-forecasting
  - /savings-goals
  - /debt-management
tldr: Remittances increase household spending in the Philippines, but financial constraints limit welfare gains for poorer households, while macroeconomic factors like exchange rates and transfer costs drive remittance flows.
problem_and_motivation: Understanding how remittances affect household consumption and the factors driving remittance flows is critical for maximizing development impact in remittance-dependent economies like the Philippines. Prior research leaves gaps in the nuanced relationship between remittances, consumption patterns, and macroeconomic determinants. This study provides new evidence using household surveys and financial sector data.
approach:
  - Analyzed Survey on Overseas Filipinos (SOF) 2007-2022 (nationally representative, 1.96M OFWs in 2022) and Family Income and Expenditure Survey (FIES) 2018/2021.
  - Used logistic regressions (odds ratios) to assess determinants of saving vs investing behavior of migrant households.
  - Applied propensity score matching (PSM) to estimate average treatment effects of remittances on consumption shares for poor vs non-poor households.
  - Estimated panel generalized method of moments (GMM) for regional remittance inflows using 17 regions, 2007-2022.
  - Incorporated annual survey (2015-2023) of remittance transfer costs from 44 universal/commercial banks and 15 non-bank entities.
  - Controlled for region, year, household head age, gender composition, education, and family size.
  - Compared OFW vs immigrant households and high vs low education migrants.
  - Tested spillover effects using remittance density at province level.
findings:
  - "num: OFW households allocated 9.9% of cash remittances to savings on average (2008-2022), while 75% allocated nothing to investments."
  - "num: 57.2% of cash remittances were sent through banks in 2022; telegraphic transfer fees average 6-7% of remittance value."
  - "num: A 1% increase in telegraphic transfer fees reduces cash remittances by approximately 12.5%."
  - Poor remittance-receiving households show smaller shifts in expenditure shares (e.g., food reduction -1.28% vs -1.48% for non-poor).
  - Remittances increase education, health, and housing spending only for non-poor households; poor households see no change in education or durables.
  - Higher regional unemployment rates increase remittance receipts, supporting the altruistic motive.
  - OFW households save significantly more (10.35%) than immigrant households (7.40%).
  - Migrants with higher education have higher saving rates (10.58% vs 7.31%).
  - Exchange rate depreciation increases cash remittance receipts.
  - Financial development (bank deposit liabilities) positively correlates with cash remittances.
key_figures_tables:
  - "Figure 4: Saving and investing rates of OFW households (2008-2022) → Saving peaked at 13.1% in 2009, investing at 10.6% in 2021."
  - "Table 3: Consumption behavior of remittance-receiving poor vs non-poor households → Non-poor increase education share by 0.40%, poor show no significant change."
  - "Table 5: Determinants of cash and personal remittances (panel GMM) → Transfer fees have large negative effect (-12.46 coefficient), exchange rate positive."
  - "Figure 5: Pooled distribution of OFW households' allocation → 50% save nothing, 75% invest nothing, >50% consume ≥90% of remittances."
key_equations:
  - equation: "Y_{ij} = \\beta_0 + \\beta_1 \\ln cons_j + \\mathbf{X}^T_i \\gamma + \\theta R_{dj} + \\varepsilon_{ij}"
    explanation: "Working-Leser model for budget share of good i."
  - equation: "Remit_{it} = \\beta_1 + \\beta_2 Remit_{i,t-1} + \\beta_3 GRDPpc_{it} + \\beta_4 OFW_{it} + \\beta_5 wage_{it} + \\beta_6 \\pi_{it} + \\beta_7 unemployment_{it} + \\beta_8 forex_t + \\beta_9 cost_t + \\varepsilon_{it}"
    explanation: "Panel GMM for remittance determinants."
definitions:
  - term: OFW
    definition: Overseas Filipino Worker – Filipino working abroad with or without contract.
  - term: SOF
    definition: Survey on Overseas Filipinos – annual PSA survey of migrant households.
  - term: FIES
    definition: Family Income and Expenditure Survey – triennial household survey.
  - term: GRDP
    definition: Gross Regional Domestic Product.
  - term: PSM
    definition: Propensity Score Matching – method to estimate treatment effects.
  - term: GMM
    definition: Generalized Method of Moments – dynamic panel estimation.
  - term: BSP
    definition: Bangko Sentral ng Pilipinas (central bank of the Philippines).
critical_citations:
  - "[Docquier & Rapoport, 2006] — theoretical framework for remittance motives."
  - "[Randazzo & Piracha, 2019] — PSM methodology for remittance expenditure effects."
  - "[Tuaño-Amador et al., 2022] — remittance resilience during COVID-19 in Philippines."
  - "[Mishra et al., 2022] — comparative remittance expenditure analysis."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      justification: "Paper analyzes spending, saving, and investing behavior of Filipino OFW households."
    - code: 3.A
      name: Expense Categorization Frameworks
      justification: "Provides detailed expenditure shares for food, education, health, housing, durables, clothing."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      justification: "Identifies distinct saving/investing behaviors by migrant status, education, and poverty level."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      justification: "Quantifies macroeconomic drivers (exchange rates, unemployment, transfer costs) of remittance inflows."
    - code: 13.A
      name: Savings Goal Management in PFMS
      justification: "Reports saving rates and constraints, showing 50% of OFW households save nothing."
    - code: 13.B
      name: Debt Management in PFMS
      justification: "Finds 17% of households used remittances for debt payments (Q4 2023 data)."
  contribution: "This paper directly informs Odin's expense categorization module by demonstrating how remittances shift spending shares across food, education, health, and housing, with clear differences by poverty status. It supports behavioral profiling by identifying how household poverty status, migrant status (OFW vs immigrant), and educational attainment affect saving versus immediate consumption decisions. The findings on remittance determinants (exchange rates, transfer costs, unemployment, financial development) provide empirical inputs for Odin's spending forecasting module. The analysis of binding financial constraints highlights design considerations for savings goal management and debt management features for lower-income users. The quantifiable impact of transfer fees (6-7% of remittance value) also informs UX decisions around transaction cost transparency."
  directly_justifies:
    - "Poor remittance-receiving households do not increase education or durable goods spending due to binding financial constraints."
    - "OFW households save more than immigrant households, with a saving rate of 10.35% vs 7.40%."
    - "A 1% increase in telegraphic transfer fees reduces cash remittances by about 12.5%."
    - "Higher regional unemployment rates increase remittance receipts, supporting altruistic motives."
    - "50% of OFW households allocate no cash remittances to savings, and 75% allocate nothing to investments."
  limits:
    - "Cross-sectional household surveys cannot fully resolve endogeneity between remittances and consumption."
    - "SOF lacks itemized consumption categories for the direct remittance allocation question, requiring FIES linkage."
    - "Small sample size for immigrant households (n=522) limits statistical power for some comparisons."
    - "Sea-based OFW remittance determinants were inconclusive due to data limitations."
  mapping_rationale: "The paper was screened against Odin's functional domains. Behavioral profiling (5.A) applies because it compares saving/investing rates by migrant status and education. Expense categorization (3.A) applies due to detailed expenditure share analysis (food, education, health, housing, durables). Spending forecasting (6.A) applies from the panel GMM identifying macroeconomic drivers. Savings and debt management (13.A, 13.B) apply from explicit saving/investment allocation data and debt payment usage. Topics related to algorithm-specific modules (anomaly detection, budget recommendation) were rejected because the paper uses econometrics (logit, PSM, GMM) not ML models. Mobile-first design and user retention were irrelevant. Topic 1.C (financial behavior of Filipino young professionals) was selected even though the sample is all OFW households, as many are young professionals; the behavioral patterns are generalizable."
limitations:
  - "Endogeneity between remittances and consumption may bias OLS results, though PSM partially addresses this. [unacknowledged]"
  - "The SOF question on remittance allocation only started in 2008 and lacks itemized non-food categories."
  - "Small sample of immigrant households (n=522) limits generalizability of comparisons."
  - "No analysis of migration costs or debt-financed migration, which could affect remittance behavior. [unacknowledged]"
  - "Regional panel GMM may mask household-level heterogeneity in remittance motives."
remember_this:
  - "OFW households save 9.9% of cash remittances on average, but 50% save nothing."
  - "Transfer fees of 6-7% significantly reduce remittance flows."
  - "Remittances increase non-food spending only for non-poor households."
  - "Financial constraints limit welfare gains for poor remittance recipients."
  - "Higher unemployment in the Philippines increases remittance receipts altruistically."
```