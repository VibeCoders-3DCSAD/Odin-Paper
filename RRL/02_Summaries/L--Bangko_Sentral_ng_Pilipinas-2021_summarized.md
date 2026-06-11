```yaml
paper_id: f47ac10b-58cc-4372-a567-0e02b2c3d479
designation: local
title: "Consumer Finance Survey 2021"
authors: "Bangko Sentral ng Pilipinas"
year: 2021
venue: "Unknown"
odin_topics:
  - 1.A
  - 1.B
  - 1.C
  - 2.A
  - 2.C
  - 3.A
  - 4.A
  - 4.B
  - 5.A
  - 10.B
  - 13.A
  - 13.B
shorthand_tags: []
tldr: The 2021 Consumer Finance Survey by the Bangko Sentral ng Pilipinas provides comprehensive data on income, expenditure, assets, liabilities, and demographics of Filipino households, revealing trends in financial inclusion, digital adoption, and debt during the COVID-19 pandemic.
problem_and_motivation: There were significant data gaps on household wealth and indebtedness in the Philippines, as existing surveys like FIES and APIS had limited coverage of assets and liabilities. Collecting detailed financial condition data was necessary to inform evidence-based socio-economic policies and monetary decisions. The survey aimed to provide a comprehensive picture of household balance sheets, income sources, spending patterns, and demographic characteristics.
approach:
  - "Sample of 18,000 households drawn from PSA's 2013 Master Sample (two-stage cluster sampling) covering all regions including BARMM."
  - "Face-to-face interviews using structured CAPI questionnaire, translated into six major languages, conducted from March to December 2022."
  - "Reference period for income and expenditure was calendar year 2021; assets and liabilities as of interview date."
  - "Unit of analysis is the primary economic unit (PEU), consisting of financially interdependent members."
  - "Response rate 90.1%; weighted estimates with coefficients of variation ≤20% considered precise."
  - "Comparisons made with 2018 CFS round to show trends."
findings:
  - "num: 91.5% of households had wage income in 2021, up from 73.7% in 2018."
  - "num: Only 29.3% of households carried any debt, down from 40.4% in 2018."
  - "num: 35.3% owned deposit accounts, significantly up from 9.7% in 2018."
  - "num: 24.3% owned electronic money accounts, up from 0.3% in 2018."
  - "num: Average household net worth was ₱435,346, with median ₱120,200."
  - "Food at home accounted for 55.4% of total expenditure, the largest share."
  - "Homeownership rate was 69.9%, with 11.3% renting."
  - "Mobile phones were the most owned appliance (92.8% of households)."
  - "Government assistance (ayuda) was a key income source for 55.6% of households during the pandemic."
key_figures_tables:
  - "Figure I.B-1: Age-sex distribution → Broad base, half of members under 28 years old."
  - "Figure III.B-1: Distribution of income sources → Wage employment primary, government ayuda notable."
  - "Figure IV.B-2: Average expenditure shares → Food at home largest (55.4%), housing/utilities 10.6%."
  - "Figure V.A-1: Tenure status → 69.9% homeowners, 11.3% renters."
  - "Figure VI-1: Financial asset ownership → 50.4% own at least one financial asset."
  - "Figure VII-1: Debt distribution → 16.4% with past due bills, 15.2% with loans."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "PEU"
    definition: "Primary economic unit, financially interdependent household members including economically dominant member and dependents."
  - term: "EDM"
    definition: "Economically dominant member, contributes most to household finances."
  - term: "CFS"
    definition: "Consumer Finance Survey, BSP's household financial condition survey."
  - term: "AONCR"
    definition: "Areas Outside the National Capital Region."
critical_citations:
  - "[BSP, 2021] — Core survey report."
  - "[PSA, 2021] — Family Income and Expenditure Survey for comparison."
relevance:
  topics:
    - code: "1.A"
      name: "Filipino Young Professionals as a Demographic"
      justification: "Provides age, education, employment, and income breakdowns for young adult cohort."
    - code: "1.B"
      name: "Financial Structure of Filipino Young Professionals"
      justification: "Detailed income, expenditure, asset, and liability data for all household types, applicable to young professionals."
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      justification: "Covers saving habits, risk preferences, debt usage, and digital financial service adoption."
    - code: "2.A"
      name: "Culturally Specific Financial Practices"
      justification: "Documents paluwagan (rotating savings), sangla-ATM, and informal lending prevalence."
    - code: "2.C"
      name: "User-Declared Financial Preferences"
      justification: "Includes survey on risk tolerance, time preference, and attitudes toward credit."
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      justification: "Uses PCOICOP classification for expenditure items, providing baseline for categorization."
    - code: "4.A"
      name: "Landscape of Existing Personal Finance Systems"
      justification: "Comprehensive mapping of bank, e-money, insurance, and loan product ownership rates."
    - code: "4.B"
      name: "Limitations and Gaps in Existing Systems"
      justification: "Identifies barriers to financial inclusion: lack of money, distance to banks, high fees, lack of documents."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      justification: "Segments households by saving behavior, risk aversion, and emergency fund adequacy."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      justification: "Reasons for not having accounts include dislike of banks and trust issues."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      justification: "Measures emergency fund holdings and adequacy relative to expenses."
    - code: "13.B"
      name: "Debt Management in PFMS"
      justification: "Analyzes outstanding loans by type, provider, interest rate, and repayment behavior."
  contribution: "This survey provides baseline empirical data on Filipino household finances, essential for Odin's expense categorization module to calibrate category shares and typical spending levels. It informs behavioral profiling by documenting saving propensities, risk preferences, and digital adoption rates across income groups. The detailed loan and asset data support anomaly detection by establishing normal ranges for debt-to-income and asset ownership. Findings on government transfers and informal lending reveal culturally specific practices that Odin's budget recommendation and savings management modules should incorporate."
  directly_justifies:
    - "Filipino households spend 55.4% of their budget on food at home."
    - "Only 35.3% of households have a formal deposit account."
    - "E-money account ownership reached 24.3% during the pandemic."
    - "29.3% of households carry any debt, down from 40.4% pre-pandemic."
    - "Average household net worth is ₱435,346, with wide inequality."
  limits:
    - "Self-reported data may have intentional under-reporting or over-reporting."
    - "Recall bias for income and expenditure covering the previous year."
    - "High coefficients of variation (CV>20%) for some estimates (marked in yellow), requiring caution."
    - "Non-sampling errors due to respondent reluctance or lack of documentation."
    - "Cross-sectional design cannot infer causality."
  mapping_rationale: "This report is a broad household survey, not an algorithmic paper. Selected topics focus on demographic, financial behavior, and system landscape domains that directly support Odin's need for empirical baselines. Rejected topics include any involving prediction, classification algorithms, or mobile UX design because the report contains no such models. Borderline cases like cultural practices (2.A) and user preferences (2.C) were included due to explicit sections on paluwagan, sangla-ATM, risk preferences, and credit attitudes. Topics on savings and debt management (13.A, 13.B) were included because the report measures emergency fund adequacy and loan characteristics, even though it does not propose management strategies."
limitations:
  - "Estimates with coefficients of variation above 20 percent should be interpreted with caution."
  - "Recall bias may affect income and expenditure values reported for the previous year."
  - "Non-sampling errors from intentional under-reporting of assets and liabilities. [unacknowledged]"
  - "The survey does not capture informal financial flows fully. [unacknowledged]"
  - "Cross-sectional nature prevents tracking of household dynamics over time."
remember_this:
  - "Wage income source increased to 91.5% of households during the pandemic."
  - "Debt prevalence dropped to 29.3% as households reduced borrowing."
  - "Digital financial assets grew rapidly: e-money accounts up to 24.3%."
  - "Food at home accounts for 55.4% of total household expenditure."
  - "Only 2.0% of households had emergency funds covering at least three months of expenses."
```