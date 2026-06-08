# Consumer Finance Survey Report 2021

## Metadata

```yaml
---
paper_id: "c3f5a9e2-d1b8-5a4f-7e9c-2d3b5a1f6e8c"
designation: local
title: "Consumer Finance Survey Report 2021"
authors: "Bangko Sentral ng Pilipinas"
year: 2021
venue: "Bangko Sentral ng Pilipinas"
odin_topics: ["A.1", "D.1", "F.1", "G.1"]
shorthand_tags: ["/expenditure-patterns", "/income-typology", "/spending-time-series", "/fil-behavioral-patterns", "/fies-bsp-mapping", "/fil-pfms-categories"]
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[ ]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
---
```

## TL;DR

Filipino households earned ₱190k average annual income in 2021, spent 55% of it on food at home, held ₱435k median net worth, and only 29% carried debt.

## Problem and Motivation

The Philippines lacked comprehensive data on household wealth, indebtedness, and financial assets beyond basic income/expenditure surveys. This data gap hindered evidence-based monetary and financial policy formulation. Prior surveys (FIES, APIS) did not capture detailed assets, liabilities, or digital financial service usage.

## Approach

- Two-stage cluster sampling from 2013 Master Sample Frame (based on 2010 CPH, updated with 2015 census), covering all 17 regions including BARMM.
- Sample size: 18,000 households; overall response rate 90.1%.
- Unit of analysis: Primary Economic Unit (PEU) — economically dominant member, spouse/partner, and financially interdependent members.
- Data collection: Face-to-face CAPI interviews from 31 March to 11 December 2022, using structured questionnaire translated into six major languages.
- Data items: demographics, employment, income (wage, business, other), expenditure (food/non-food, 2020 PCOICOP), non-financial assets (real property, vehicles, appliances, valuables), financial assets (deposits, e-money, insurance/pension, investments), liabilities (loans, credit cards, past due bills), and financial attitudes.

## Findings

1. Average annual household income: ₱189,842 (median ₱144,000); wages accounted for 84.3% of total income, government *ayuda* reached 55.6% of households.
2. **55.4% of total household expenditure went to food at home** — the largest single spending category, up from 49.9% in 2018.
3. Housing and utilities (10.6%) and transportation (7.2%) were the next largest non-food essentials; non-essential items (miscellaneous, alcohol, recreation) totaled 8.6%.
4. 69.9% of households owned/co-owned their residence; 35.3% owned a deposit account (up from 9.7% in 2018), and 24.3% owned an e-money account (up from 0.3%).

- 92.8% of households owned a mobile phone, surpassing television (81.1%) as the most common appliance.
- Only 29.3% of households had any outstanding debt; 16.4% had past due bills (mostly electricity), 15.2% had outstanding loans, and 0.7% had credit card debt.

## Key Figures and Tables

- Figure I.B-1: Age-sex distribution → broad base, half of members under 28 years, sex ratio 0.98.
- Figure III.B-1: Income sources → 91.5% received wage income, 55.6% other sources (mostly government aid).
- Figure IV.B-2: Expenditure shares → food at home 55.4%, housing+utilities 10.6%, transportation 7.2%.
- Table V.A-1: Tenure status → 69.9% homeowners, 11.3% renters, higher homeownership in Visayas/Mindanao.
- Table VI.A-1: Deposit account ownership → 35.3% overall, 42% in NCR, 27.8% in Mindanao.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| PEU | Primary Economic Unit — financially interdependent members within a household. |
| EDM | Economically Dominant Member — the person who contributes most to household finances. |
| CFS | Consumer Finance Survey — BSP's household wealth survey, patterned after US SCF. |
| FIES | Family Income and Expenditure Survey — PSA's triennial income/expenditure survey. |
| PCOICOP | Philippine Classification of Individual Consumption According to Purpose — standard for expenditure categories. |
| GIDA | Geographically Isolated and Disadvantaged Areas — remote barangays with limited services. |

## Critical Citations

- [PSA, 2021a] — 2020 Annual Poverty Indicators Survey, baseline for household convenience ownership trends.
- [BSP, 2022] — Financial Inclusion Dashboard, corroborates growth in deposit and e-money accounts.
- [SSS, 2023] — Membership data for insurance/pension plan validation.
- [IATF-EID, 2021] — Omnibus guidelines defining essential vs. non-essential expenditures during pandemic.

## Relevance to Odin

**Topics:**

A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

D.1 — Predictive Modeling in Personal Finance Systems

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

G.1 — Expense Categorization in Filipino Personal Finance Contexts

**Contribution to Odin:**

This survey provides the authoritative empirical baseline for Filipino household spending patterns, income sources, and asset ownership, directly grounding Odin’s expense categorization module (G.1) in the PCOICOP framework used by the Philippine government. The detailed per-category expenditure shares (e.g., 55.4% food at home, 10.6% housing+utilities) supply realistic priors and validation targets for Odin’s spending forecasting (D.1) and budget recommendation algorithms. The income typology (wage, entrepreneurial, government transfers) and demographic profiles (age, education, health insurance) inform user profiling (F.1) and cold-start behavior assumptions. The finding that 92.8% own mobile phones but only 35.3% have bank accounts strongly justifies Odin’s mobile-first, manual-input, no-banking-integration design.

**Directly justifies:**

- "Filipino households allocated 55.4% of total expenditure to food at home in 2021, making it the single largest budget category and a mandatory anchor for any budget recommendation system targeting this population."
- "Only 29.3% of households carried any debt, with past due bills (16.4%) more common than formal loans (15.2%) — anomaly detection in Odin should prioritize budget overage alerts over debt-based indicators."
- "Mobile phone ownership reached 92.8% while deposit account ownership was only 35.3% — Odin’s mobile-first, manual transaction input design matches actual Filipino financial behavior."
- "Average annual PEU income was ₱189,842 (median ₱144,000), with 40.4% of respondents aged 25-44 — this income range defines the target young professional segment for Odin."
- "The survey’s expenditure categories follow the 2020 PCOICOP, which aligns with FIES and BSP Consumer Finance Survey — Odin can directly adopt these category definitions for local regulatory alignment."

**Limits of relevance:**

- Survey covers all Filipino households, not specifically young professionals; young-adult subset extraction is possible but not pre-aggregated.
- Data collected during COVID-19 pandemic (2021) may overstate emergency government transfers and understate normal discretionary spending.
- No algorithmic or predictive modeling is presented; the relevance is purely descriptive and foundational for category design and baseline statistics.
- Geographic granularity is at regional/urban-rural level, not at the individual user level needed for personalization calibration.

## Limitations

- Self-reported data subject to recall bias and intentional under-/over-reporting of income and asset values. [unacknowledged]
- Estimates with CV >20% (yellow highlights) should be used with caution; some regional breakdowns have low precision.
- Reference period for income/expenditure is calendar year 2021, while asset/liability data are as of interview date (2022), creating temporal mismatch.
- No longitudinal component — cannot track changes in individual household behavior over time. [unacknowledged]
- The survey excludes financially independent boarders and helpers, potentially under-representing certain urban household structures.

## Remember This

- 🔑 **55.4% of spending on food at home** — the baseline for budget allocation, unchanged from previous rounds.
- 📌 **92.8% own mobile phones, 35.3% own bank accounts** — mobile-first, manual input is the only viable design.
- 💡 **29.3% carry debt, mostly past due bills** — anomaly detection should flag utility overages, not credit card debt.
- ⚠️ **Pandemic-year data (2021)** — government ayuda reached 55.6% of households; normal-year patterns may differ.
