```yaml
paper_id: 10.20944/preprints202508.0349.v1
designation: local
title: Analysis of the Food and Income Expenditure Survey 2023 Among Filipino Households
authors: Ama, Nathan Andrie
year: 2025
venue: Preprints.org
odin_topics:
  - 3.A
  - 6.A
  - 6.B
  - 7.A
  - 7.B
shorthand_tags:
  - /expense-categorization-frameworks
  - /predictive-modeling
  - /spending-forecasting
  - /budgeting-strategies
  - /budget-recommendation
tldr: Analysis of 163,268 Filipino households shows food expenditure is income inelastic (elasticity 0.58), rural households spend more on food than urban, and bread and meat dominate food spending.
problem_and_motivation: Food constitutes the largest household expenditure in the Philippines, yet understanding how income, geography, and household characteristics drive food spending patterns is limited. Existing studies lack integrated spatial and predictive analysis of food insecurity. This gap hinders targeted food security and poverty policies.
approach:
  - Data from 2023 Family Income and Expenditure Survey (FIES) of 163,268 Filipino households.
  - Principal Component Analysis (PCA) identified dominant income sources: retail, transport, farming, and remittances.
  - Spatial mapping at province level revealed clustering of food expenditure across regions.
  - Mann-Whitney U test compared rural vs urban food expenditure and per capita income.
  - Generalized Additive Model (GAM) predicted food insecurity using smooth terms for income, household size, and income sources.
  - Log-log Engel curve estimated income elasticity of food expenditure.
  - Beta regression modeled proportion of food spending outside home against income, urbanicity, and household size.
findings:
  - "num: Income elasticity of food expenditure is 0.58, indicating food is a necessity good."
  - "num: Rural households spend a median of ₱102,467 on food vs urban ₱80,700 (p<.001)."
  - "num: GAM explained 27.2% deviance in food insecurity, with per capita income as strongest predictor (edf=6.71, χ²=16,981.31, p<.001)."
  - Bread accounts for 29.5% of food spending, followed by meat (14.8%) and fish (14.2%).
  - Spatial clustering shows Leyte and Bohol have highest food expenditure (₱120,000+).
  - "num: Higher-income households allocate larger proportion to food outside home (β=0.72, p<.001)."
key_figures_tables:
  - "Figure 1: Lorenz curve for food expenditure → Gini 0.277, more equal than income."
  - "Figure 2: Histogram of food expenditure per member → Right-skewed, most households spend low."
  - "Figure 3: Scree plot of PCA variances → Five components explain 55.33% of variance."
  - "Figure 5: Spatial map of mean food expenditure → Leyte and Bohol highest spending clusters."
  - "Figure 6: Ternary plot for bread, meat, fish → Households prefer bread and meat over fish."
  - "Figure 7: Pie chart of food categories → Bread largest share at 29.5%."
  - "Figure 8: GAM partial effects → Income shows sharp decline in food insecurity at low levels."
  - "Figure 10: Engel curve log-log plot → Positive inelastic relationship."
key_equations:
  - equation: \log(FOOD_i) = \beta_0 + \beta_1 \log(TINC_i) + \epsilon_i
    explanation: Income elasticity of food expenditure.
  - equation: g(E(Y)) = \beta_0 + f_1(x_1) + \ldots + f_m(x_m)
    explanation: Additive smooth predictors for food insecurity.
  - equation: \text{logit}(\mu_i) = \beta_0 + \beta_1 \log(INCOME_i) + \beta_2 URB_i + \beta_3 FSIZE_i
    explanation: Models proportion of food spent outside home.
definitions:
  - term: FIES
    definition: Family Income and Expenditure Survey conducted by Philippine Statistics Authority.
  - term: PSA
    definition: Philippine Statistics Authority.
  - term: GAM
    definition: Generalized Additive Model for nonlinear regression.
  - term: PCA
    definition: Principal Component Analysis for dimensionality reduction.
  - term: RPCINC
    definition: Real per capita income.
critical_citations:
  - "[Valera et al., 2022] — QUAIDS model for Philippine food demand."
  - "[Briones, 2022] — Impact of price shocks on nutrient intake."
  - "[Bairagi et al., 2022] — Rural-urban food basket composition differences."
  - "[Smithson & Verkuilen, 2006] — Beta regression transformation."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      justification: Paper categorizes food into bread, meat, fish, vegetables, fruit with proportional shares.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      justification: Uses GAM to predict food insecurity from household characteristics.
    - code: 6.B
      name: Spending Forecasting Algorithm
      justification: Estimates income elasticity (0.58) for forecasting food expenditure changes.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      justification: Confirms Engel's law: food is a necessity, informing budget allocation.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      justification: Provides empirical basis for recommending food budget shares based on income.
  contribution: This paper informs Odin's spending forecasting module by providing income elasticity of food expenditure (0.58) from Philippine household data. The GAM approach for predicting food insecurity can be adapted for Odin's anomaly detection or risk profiling. The expense categorization framework (bread, meat, fish, vegetables, fruit) offers a starting point for Odin's expense categorization module. The rural-urban spending differences can guide personalized budget recommendations based on user location.
  directly_justifies:
    - Food expenditure has income elasticity 0.58, meaning a 1% income increase leads to 0.58% more food spending.
    - Rural households spend more on food (median ₱102,467) than urban (₱80,700) in the Philippines.
    - Bread accounts for 29.5% of Filipino household food expenditure, the largest single category.
    - Higher-income households allocate a larger proportion of food spending to eating outside the home.
  limits:
    - The paper studies general households, not specifically young professionals, limiting direct applicability.
    - Cross-sectional data prevents causal inference for spending behavior changes over time.
    - Lacks granular nutritional or dietary quality measures needed for comprehensive financial health assessment.
    - No evaluation of algorithmic modules or user interaction data.
  mapping_rationale: The paper was screened against Odin's functional domains. It directly contributes to expense categorization (3.A) through its breakdown of food categories and spending shares. Predictive modeling (6.A) and spending forecasting (6.B) are supported by the GAM for food insecurity and Engel curve elasticity estimation. Budgeting strategies (7.A) and recommendation (7.B) are informed by Engel's law and income elasticity findings. Topics related to behavioral profiling (5.A-C) were rejected because the paper does not classify financial behaviors or profiles. Anomaly detection (8.A-B) and retention (11.A-B) were not addressed. The paper's focus on food expenditure as a necessity provides domain knowledge for budget allocation algorithms in Odin.
limitations:
  - Cross-sectional design limits causal interpretation.
  - Lacks dietary diversity and nutritional status measures [unacknowledged] in relation to PFMS.
  - Spatial analysis only at province level, obscuring intra-provincial disparities.
  - Self-reported income/expenditure may introduce recall bias.
  - No validation of predictive model on separate test set [unacknowledged].
remember_this:
  - Food spending elasticity is 0.58, confirming Engel's law for Filipino households.
  - Rural households spend more on food than urban households despite lower expectations.
  - Bread and meat dominate Filipino food budgets, accounting for over 44% of food spending.
  - Household size and per capita income are the strongest nonlinear predictors of food insecurity.
```