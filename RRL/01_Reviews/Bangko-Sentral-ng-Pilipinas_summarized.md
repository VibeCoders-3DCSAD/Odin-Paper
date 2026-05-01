---
name: paper-summary
paper_id: "f7d9e3a2-5b1c-4e8a-9d2f-6b4e8c7a3d1f"
source_document: "converted.md"
designation: local
title: "2021 Consumer Finance Survey (CFS)"
authors: "Bangko Sentral ng Pilipinas"
year: 2021
venue: "Bangko Sentral ng Pilipinas"
odin_topics: [1, 9, 11]
shorthand_tags: ["/income-typology", "/expenditure-patterns", "/income-type-behavior-diff", "/fil-behavioral-patterns", "/profile-dimensions", "/fies-bsp-mapping", "/cultural-expense-types", "/fil-pfms-categories", "/sss-pagibig"]
summary_date: 2026-04-28
version: "1.0"
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

# 2021 Consumer Finance Survey (CFS)

## TL;DR
National survey of 18,000 Filipino households shows average annual income ₱189,842, food takes 55.4% of spending, 35.3% own a deposit account, and only 29.3% carry any debt.

## Problem and Motivation
No comprehensive national data existed on household wealth, indebtedness, and financial asset ownership in the Philippines. Existing surveys (FIES, APIS) did not cover detailed balance sheets. Policymakers and researchers needed evidence‑based metrics on income, spending, assets, and liabilities to design financial inclusion and social protection policies.

## Approach
- Nationwide two‑stage cluster sample of 18,000 households (2013 Master Sample, updated 2015 Census).
- Face‑to‑face computer‑assisted personal interviewing (CAPI), 2022 data collection covering calendar year 2021.
- Unit of analysis: primary economic unit (PEU) – financially interdependent household members.
- 90.1% response rate, estimates weighted and disaggregated by urbanization (NCR, urban AONCR, rural AONCR) and island group (Balance Luzon, Visayas, Mindanao).
- Captured demographics, employment, income, expenditure, non‑financial assets (housing, vehicles, appliances), financial assets (deposits, e‑money, insurance), and liabilities (loans, credit cards, past‑due bills).

## Findings
1. Average annual household income: **₱189,842** (median ₱144,000). Wage employment is primary source (91.5% of PEUs), government *ayuda* (pandemic aid) reached 55.6%.
2. Average annual expenditure: ₱230,904 (median ₱201,000). Food at home accounts for **55.4%** of total spending, followed by housing & utilities (10.6%) and transportation (7.2%).
3. Homeownership rate: 69.9% (NCR 43.9%, AONCR 73.9%). 96.6% own at least one appliance; mobile phone ownership 92.8%.
4. Financial asset ownership rose sharply to 50.4% (from 22.6% in 2018), driven by deposit accounts (35.3%) and e‑money wallets (24.3%).
5. Only 29.3% of PEUs have any outstanding debt. Business loans (6.1%) and “other loans” (8.2%) dominate; credit card ownership is 1.1%, with average limit ₱60,000.
6. Average net worth is ₱435,346 (median ₱120,200). Principal residence makes up 50.3% of total assets; financial assets only 7.4%.

## Key Figures and Tables
- Table III.A‑1: Average annual income by area → NCR ₱229,562, Mindanao ₱164,109.
- Figure I.B‑1: Age‑sex pyramid → broad base (half of members under 28), 49 dependents per 100 working‑age.
- Table V.A‑1: Tenure status → homeownership 69.9%, renting 11.3% (up from 10.2% in 2018).

## Key Equations
None. (Survey report with descriptive statistics and regression‑based hedonic pricing models, but no central equation presented as a core contribution.)

## Definitions

| Term / Acronym | Plain‑English Definition |
|----------------|--------------------------|
| PEU | Primary Economic Unit – financially interdependent household members excluding self‑sufficient boarders. |
| EDM | Economically Dominant Member – the member who contributes most to household finances. |
| AONCR | Areas Outside the National Capital Region – all provinces and cities except Metro Manila. |
| Gini coefficient | Measure of income inequality (0 = perfect equality, 1 = perfect inequality). |
| PCOICOP | Philippine Classification of Individual Consumption According to Purpose – standard for expenditure categories. |
| BDA | Basic Deposit Account – low‑balance, low‑fee account (opening ≤₱100, no maintaining balance). |

## Critical Citations
- [PSA, 2022d] – 2021 Family Income and Expenditure Survey, used for comparison of income distributions.
- [BSP, 2022] – Financial Inclusion Dashboard, referenced for growth in basic deposit accounts and cash agents.
- [World Bank Group, 2022] – Global Findex, cited for pandemic‑driven surge in digital payments.

## Relevance to Odin

**Topics:**
1. Spending and Budgeting Behavior of Filipino Young Professionals  
9. User Behavioral Profiling in Filipino Personal Finance Contexts  
11. Expense Categorization in Filipino Personal Finance Contexts

**Contribution to Odin:**
This survey provides the most authoritative national baseline of Filipino household income, expenditure, and asset‑holding patterns. It directly informs the design of Odin’s spending forecasting, anomaly detection, and user profiling modules by grounding them in real, locally representative consumption data. The detailed expenditure breakdowns (food at home vs. outside, housing, transportation, education, health, sin products) validate category taxonomies and highlight culturally significant items like *ayuda*, remittances, and *sari‑sari* store spending.

**Directly justifies:**
- Filipino households allocate **55.4% of total expenditure to food at home**, making food the dominant spending category that forecasting models must prioritize.
- Only **35.3% of households own a deposit account**, but e‑money ownership surged to 24.3% during the pandemic, indicating a transition to digital wallets as a primary transactional account.
- The majority of employed workers are in **services/sales (23.2%) and elementary occupations (15.5%)** with irregular income, supporting the need for anomaly detection that handles variable earnings.
- Past‑due household bills affect **16.4% of PEUs** (mostly electricity and water), establishing a realistic baseline for detecting over‑spending anomalies.

**Limits of relevance:**
- The sample is national and not segmented specifically by “young professionals” (age 22–35), though age‑group breakdowns are available (e.g., young adults 25–44).
- The survey describes *observed* behavior in 2021 (pandemic year) – not a predictive model or algorithm.
- Financial attitudes and risk preferences are self‑reported and may not translate directly to in‑app behavioral triggers.

## Limitations
- Recall bias for income and expenditure over the entire 2021 calendar year; respondents encouraged to use receipts but likely under‑reported.
- Non‑sampling errors from intentional under‑reporting of assets and over‑reporting of socially desirable behaviors (e.g., savings).
- Wealth estimates exclude some non‑market assets (e.g., informal lending networks, barter) that are common in rural areas.
- Cross‑sectional design – no panel data to track how households changed over time.

## Remember This
- 🔑 **₱189,842 average annual income** – baseline for calibrating Odin’s synthetic household data.
- 💡 **Only 29.3% carry debt** – debt is not the norm; anomaly detection should not expect frequent loan transactions.
- 📌 **Food is 55.4% of spending** – any spending forecast must treat groceries as the primary category.