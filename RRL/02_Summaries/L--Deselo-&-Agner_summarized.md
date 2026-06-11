```yaml
paper_id: 10.5539/ijef.v15n6p27
designation: international
title: Financial Inclusion and the Role of Financial Literacy in the Philippines
authors: Desello, J. M. U.; Agner, M. G. R.
year: 2023
venue: International Journal of Economics and Finance
odin_topics:
  - 1.C
  - 5.A
shorthand_tags:
  - /financial-behavior
  - /behavioral-profile
tldr: Financial literacy positively predicts financial account ownership and use of financial services among Filipinos, with age, gender, income, and household decision-making role as key drivers.
problem_and_motivation: Financial inclusion is a national development agenda in the Philippines, but local studies linking financial literacy to inclusion using nationally representative data are scarce. Understanding the drivers of account ownership and service usage is necessary to bridge the inclusion gap and raise financial literacy levels.
approach:
  - Data from Bangko Sentral ng Pilipinas 2019 Financial Inclusion Survey (n=1,200).
  - Financial literacy measured with three-item quiz (inflation, simple interest, compound interest).
  - Dependent variables: ownership of formal accounts (bank, e-money, cooperative, microfinance) and use of financial services (credit, investment, insurance).
  - Linear probability and probit models estimated with robust standard errors.
  - Controls include age, gender, employment, education, income, residence, remittance receipt, awareness of BSP programs, and household financial decision-maker role.
findings:
  - "num: A one-standard-deviation increase in financial literacy raises likelihood of account ownership by 3.7-4.2 percentage points."
  - "num: A one-point increase in financial literacy score increases likelihood of availing a financial service by 4.9-6.0 percentage points."
  - "num: Financial literacy increases bank account ownership by 2.1 percentage points and investment ownership by 3.7-4.2 percentage points."
  - Awareness of BSP financial education programs and being the main household financial decision-maker are strong positive drivers of inclusion.
  - Being female positively correlates with account ownership and use of formal credit and insurance, but negatively with investment.
  - Higher education (college or vocational) and income above 40,000 PHP significantly increase likelihood of owning a bank account and using financial services.
key_figures_tables:
  - "Table 1: OLS and probit results for owning at least one account → Literacy increases ownership by 3.7-4.2 pp."
  - "Table 3: Financial literacy effect on any financial service → Increases by 4.9-6.0 pp."
  - "Table 4: Literacy only significant for accounts and investments → 3.7-4.2 pp for investments."
key_equations:
  - equation: "FA_i = β_0 + β_1 FL_i + β_2 X_i + u_i"
    explanation: "Financial account ownership as function of literacy and controls."
  - equation: "FS_i = β_0 + β_1 FL_i + β_2 X_i + u_i"
    explanation: "Financial service usage as function of literacy and controls."
definitions:
  - term: BSP
    definition: "Bangko Sentral ng Pilipinas, the Philippine central bank."
  - term: FIS
    definition: "Financial Inclusion Survey conducted by BSP."
  - term: Financial literacy
    definition: "Combination of awareness, knowledge, skill, attitude, and behavior for sound financial decisions."
  - term: Financial inclusion
    definition: "Effective access to a wide range of financial services for all, especially vulnerable sectors."
  - term: GPFI
    definition: "Global Partnership for Financial Inclusion."
  - term: OECD/INFE
    definition: "OECD International Network on Financial Education."
critical_citations:
  - "[Morgan & Trinh, 2017] — Financial literacy drives inclusion in Cambodia and Vietnam."
  - "[Grohmann, Klühs, & Menkhoff, 2018] — Cross-country evidence of literacy improving inclusion."
  - "[Lusardi & Mitchell, 2011] — Financial literacy and retirement planning."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      justification: "Paper identifies demographic and literacy drivers of account ownership and service use among Filipinos."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      justification: "Provides empirical determinants (age, gender, income, literacy) that can inform behavioral profile classification."
  contribution: "This paper justifies using financial literacy scores as a feature in Odin's behavioral profiling module to predict user financial capability. The identified demographic drivers (age, gender, income, employment) inform Odin's spending forecasting and budget recommendation algorithms by providing population-level priors. The finding that household decision-maker role affects financial inclusion supports Odin's design for joint household financial management features. The positive effect of financial literacy on investment uptake directly supports Odin's savings and debt management module design."
  directly_justifies:
    - "Financial literacy increases the probability of owning a bank account by 2.1 percentage points per standard deviation."
    - "Being the main household financial decision-maker raises likelihood of using financial services by 24-34 percentage points."
    - "Awareness of financial education programs positively correlates with account ownership and investment uptake."
    - "A one-point increase in financial literacy improves financial service uptake by 4.9-6.0 percentage points."
  limits:
    - "Only three financial literacy questions may not capture full construct (acknowledged in paper)."
    - "Cross-sectional design prevents causal inference [unacknowledged]."
    - "Sample of 1,200 may not fully represent all Filipino subgroups [unacknowledged]."
  mapping_rationale: "The paper primarily addresses financial behavior of Filipinos (1.C) through empirical analysis of account ownership and service use. It also supports behavioral profiling (5.A) by identifying key determinants such as literacy, age, gender, income, and household decision-making role. Rejected codes include spending forecasting (6.A) as no predictive modeling; budget recommendation (7.A) as no budgeting strategies; anomaly detection (8.A) as no outlier analysis; mobile design (9.A) as no UX; privacy (10.A) as no discussion; retention (11.A) as no engagement metrics; evaluation (12.A) as no system evaluation; savings/debt (13.A) as no goal management. Borderline case 2.B (seasonal spending) not covered."
limitations:
  - "Uses only three financial literacy questions, which may not capture full construct (acknowledged)."
  - "Cross-sectional design prevents causal inference [unacknowledged]."
  - "Sample of 1,200 may not fully represent all Filipino subgroups [unacknowledged]."
  - "No discussion of potential self-report or social desirability bias [unacknowledged]."
remember_this:
  - "Financial literacy raises account ownership by 3.7-4.2 percentage points."
  - "Being main financial decision-maker increases service use by 24-34 percentage points."
  - "Awareness of BSP programs strongly predicts bank account ownership."
  - "Women are more likely to own accounts and use formal credit and insurance."
  - "Income above 40,000 PHP dramatically boosts financial inclusion."
```