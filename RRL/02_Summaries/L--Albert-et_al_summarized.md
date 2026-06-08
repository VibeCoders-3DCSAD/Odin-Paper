```yaml
paper_id: 10.62986/dp2025.35
designation: local
title: Gender Equality, Disability, and Social Inclusion in the Philippines: Progress, Challenges, and Opportunities in SDG 5 and SDG 10
authors: Albert, J. R. G.; Dacuycuy, C. B.; Quisumbing, A. R.; Basillote, L. B.; Cabalfin, D. L. D.; Vargas, A. R. P.; Luzon, P. E. D.; Mahmoud, M. A.
year: 2025
venue: PIDS Discussion Paper Series, No. 2025-35, Philippine Institute for Development Studies
odin_topics:
  - 1.A
  - 1.C
shorthand_tags:
  - /filipino-young-professionals
  - /financial-behavior
tldr: Philippines has progressive GEDSI laws but implementation gaps persist; intersectional analysis reveals compound marginalization for women, persons with disabilities, and indigenous peoples across income, education, and employment.
problem_and_motivation: Despite robust legal frameworks like the Magna Carta of Women and the Indigenous Peoples Rights Act, significant inequalities persist for marginalized groups. The COVID-19 pandemic exacerbated existing disparities, pushing millions into poverty. This study examines progress on SDG 5 and SDG 10 to identify intersectional barriers and inform inclusive policy reforms.
approach:
  - Mixed-methods design combining quantitative analysis of national surveys (FIES, LFS, NDHS, NDPS) and qualitative stakeholder interviews (KIIs, FGDs).
  - Shapley decomposition of merged FIES-LFS data (2018, 2021, 2023) to quantify contributions of gender, education, location, and income to inequality.
  - Intersectional analysis examining how gender, disability, ethnicity, and geography interact to shape development outcomes.
  - Descriptive analytics of SDG Watch data and World Bank Indigenous Peoples Household Survey (2023).
  - Time-use analysis from International Social Survey Programme (2012, 2022) and COVID-19 online survey.
findings:
  - num: Female disability prevalence 15% vs male 9% (2016 NDPS).
  - num: Child marriage before age 18 dropped from 16.5% (2017) to 9.4% (2022).
  - num: Gini coefficient decreased from 0.453 (2015) to 0.406 (2023).
  - Women with no formal education have 55% severe disability prevalence vs 6% for college graduates.
  - Indigenous women's engagement in unpaid family work is more than three times higher than non-Indigenous counterparts.
  - num: Urban location explains 25-36% of inequality in working hours (Shapley decomposition).
  - num: Only 34% of women who experienced violence sought help (2022 NDHS).
  - Unpaid care work gap persists: women spend 9-10 hours more per week on housework and care than men.
key_figures_tables:
  - Figure 1: Poverty incidence by basic sector (2018-2023) → Poverty remains highest among IPs (32.4%) and fisherfolk (27.4%).
  - Figure 10: Gini coefficient in ASEAN member states → Philippines remains among most unequal despite recent declines.
  - Table 15: Inequality decomposition using per capita income → Education explains 27-30% of between-group inequality.
  - Table 35: Disability prevalence by sex and employment → Women in unpaid family farm work have 25% severe disability.
key_equations:
  - equation: T_{total hours worked} = \alpha + \beta (male) + \gamma (education) + \delta (age^2) + \zeta (married) + \eta (married mother with child 0-2) + \theta (hh salaries) + \iota (wholesale/retail income) + \kappa (entrepreneurial income) + \lambda (urban) + \mu (NCR) + \nu (poor) + \epsilon
    explanation: Linear model for determinants of weekly working hours.
definitions:
  - term: GEDSI
    definition: Gender Equality, Disability and Social Inclusion – condition of equal rights and opportunities regardless of identity.
  - term: Intersectionality
    definition: Analytical framework examining how multiple identities interact to create unique disadvantage patterns.
  - term: Shapley decomposition
    definition: Method to attribute explained variance in inequality to different factors (e.g., gender, location).
  - term: NDPS
    definition: National Disability Prevalence Survey (2016) using environmental-contextual disability measurement.
critical_citations:
  - "[Crenshaw, 1989] — introduced intersectionality concept."
  - "[Goldberg et al., 2025] — Global Gender Distortions Index methodology."
  - "[World Bank, 2023] — documentation of persistent gender asset gaps."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      justification: Provides extensive income, employment, education, and disability data for Filipino population including young adults.
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      justification: Documents time allocation to market vs unpaid care work, labor force participation patterns, and income inequality affecting financial capacity.
  contribution: This paper informs Odin's demographic profiling module (1.A) by quantifying income inequality, labor force participation gaps, and disability prevalence among Filipinos. It highlights that women and persons with disabilities face compounded economic disadvantages, which Odin's behavioral profiling (5.A) should account for. The finding that unpaid care work consumes 9-10 more hours weekly for women directly impacts spending forecasting (6.A) and budget recommendation (7.A) by reducing available work hours and disposable income. Finally, the documentation of "statistical invisibility" for indigenous groups underscores the need for inclusive data collection in Odin's expense categorization (3.A) and anomaly detection (8.A) to avoid systemic bias.
  directly_justifies:
    - "Women in the Philippines spend 9-10 hours more per week on unpaid care work than men."
    - "Severe disability prevalence is 55% for women with no formal education compared to 6% for college graduates."
    - "Indigenous women's unpaid family work participation is three times higher than non-Indigenous women."
    - "Only 34% of women who experience intimate partner violence seek formal help."
  limits:
    - "Disability data from 2016 NDPS predates pandemic and may not reflect current prevalence."
    - "Qualitative sample may not capture full range of intersectional experiences due to thematic saturation limits."
    - "Official statistics systematically under-represent indigenous peoples and persons with disabilities [unacknowledged]."
  mapping_rationale: This paper was screened against all Odin functional domains. No direct relevance was found for spending forecasting, budget recommendation, anomaly detection, expense categorization, mobile-first design, data privacy, user retention, system evaluation, or savings/debt management. However, the paper provides foundational demographic and behavioral context for Filipino young professionals (domain: behavioral profiling). Specifically, it offers quantitative estimates of income distribution, labor force participation, gender gaps, and disability prevalence (topic 1.A), and detailed analysis of time allocation between market and unpaid care work that shapes financial behavior (topic 1.C). Topics related to financial product design (e.g., 7.A, 8.A) were rejected because the paper does not discuss algorithms or personal finance systems. The selected codes reflect the paper's value as contextual research for understanding Odin's target user population and their economic constraints.
limitations:
  - "Official statistics under-represent marginalized populations due to geographic isolation and mistrust of data collection. [unacknowledged]"
  - "Small sample sizes for intersectional categories (e.g., women with disabilities from IP communities) limit robust statistical analysis."
  - "No formal IRB approval obtained, though ethical principles were followed. [unacknowledged]"
  - "Shapley decomposition explains only 6-8% of variation in working hours, indicating omitted variables."
remember_this:
  - "15% of women have disabilities versus 9% of men."
  - "Child marriage before 18 fell to 9.4% in 2022."
  - "Women spend 9-10 more hours weekly on unpaid care work."
  - "Gini coefficient improved from 0.453 to 0.406 since 2015."
  - "Indigenous women face triple disadvantage in labor, education, and land rights."
```