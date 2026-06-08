# Financial freedom of Filipinos in personal finance management

## Metadata

```yaml
---
paper_id: "5f4dcc3b-5aa0-4b5a-8b0e-3e3e2a3b4c5d"
designation: local
title: "Financial freedom of Filipinos in personal finance management"
authors: "Flores, C."
year: 2025
venue: "Unknown"
odin_topics: ["A.1", "F.1"]
shorthand_tags: ["/budget-failure-points", "/fil-behavioral-patterns"]
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

Cash, debt, risk, and wealth management practices among Filipino corporate employees do not significantly predict financial freedom, despite moderate self-assessed competence.

## Problem and Motivation

Many Filipinos lack awareness of financial instruments and exhibit cultural tendencies like the "come-what-may" attitude, leading to poor emergency fund preparedness and reliance on debt. This financial illiteracy undermines long-term wealth accumulation and increases financial stress, especially for working parents and young professionals. Prior studies had not quantitatively evaluated how cash, debt, risk, and wealth management jointly contribute to financial freedom in the Philippine corporate context.

## Approach

- Data: 150 respondents from 10 Philippine Stock Exchange-indexed corporations (SM, Ayala, BDO, etc.) in Metro Manila.
- Survey measured demographics, work profile, and four personal finance dimensions: cash, debt, risk, and wealth management.
- Weighted mean calculated for each dimension on a Likert scale (1-5, higher = better practice).
- Linear regression analysis tested the contribution of the four dimensions to self-reported financial freedom.
- Respondents included top management (33%), middle management (27%), and rank-and-file (40%).

## Findings

1. Majority demographics: 57% male, 63% married, 43% aged 31-40, 57% have 1-2 children.
2. Work profile: 40% rank-and-file, 50% have 11-18 years working, 40% earn ₱30,000+ monthly.
3. Weighted means: cash management 3.73, debt management 3.7, risk management 3.7, wealth management 3.7 — all indicating agreement with positive practices.

- **Linear regression found that cash, debt, risk, and wealth management do not significantly contribute to financial freedom (p > 0.05 for all variables).**
- Risk management had the highest weighted mean (3.65) but still not significant.

## Key Figures and Tables

- Table 1: Demographic profile (sex, civil status, age, children) → majority male, married, 31-40, 1-2 children.
- Table 2: Work profile (position, years working, income) → 40% rank-and-file, 50% work 11-18 years, 40% earn ₱30k+.
- Table 3: Weighted means for CDRW variables → cash 3.73, debt 3.7, risk 3.7, wealth 3.7.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| CDRW | Cash, debt, risk, and wealth management — the four pillars of personal finance in this study. |
| PSE | Philippine Stock Exchange, where the sampled corporations are listed. |
| PDIC | Philippine Deposit Insurance Corporation — insures bank deposits up to ₱500,000. |
| NFIS | Negative Finding Information System — credit bureau database for delinquent borrowers. |
| Alkansya | Traditional Filipino bamboo or clay piggy bank for cash savings. |
| Utang | Filipino term for debt or loan. |

## Critical Citations

- [Lusardi, 2004] — Foundational research on savings behavior and financial education effectiveness.

## Relevance to Odin

**Topics:**

A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

**Contribution to Odin:**

This paper provides direct empirical evidence on the personal finance practices, attitudes, and gaps among Filipino corporate employees — a population that overlaps with Odin's target young professionals. It informs Odin's user profiling module by documenting cultural behaviors (traditional alkansya usage, utang cycles, fear of bank savings, "come-what-may" attitude) that can be operationalized as profile dimensions. The finding that standard CDRW practices do not predict financial freedom suggests Odin should look beyond basic finance metrics and incorporate behavioral economics or social factors into its budget recommendation and anomaly detection logic. Although the study uses regression instead of ML, its descriptive statistics on emergency fund unpreparedness and high debt reliance justify Odin's emphasis on automated savings nudges and debt-prioritization features.

**Directly justifies:**

- "57% of Filipino corporate respondents keep their savings in traditional alkansya or at home due to perceived bank insecurity, leading to low emergency fund preparedness."
- "Majority of respondents agree that paying off high-interest debt first and paying more than the minimum balance are effective debt management strategies."
- "Filipino employees exhibit a 'come-what-may' attitude toward financial planning, which hinders budgeting and investment practices."
- "Life insurance uptake in the Philippines is low because Filipinos perceive it as an unnecessary expense, intangible, or a lack of funds — not as a risk management tool."
- "Linear regression showed that cash, debt, risk, and wealth management combined do not significantly predict financial freedom (p > 0.05), indicating other unmeasured factors (e.g., financial literacy, social pressures) are more influential."

**Limits of relevance:**

- Sample is limited to large corporations in Metro Manila; findings may not generalize to self-employed, informal sector, or provincial Filipino young professionals.
- Study uses self-reported survey data with potential social desirability bias; actual behavior may differ.
- No digital or mobile finance context; Odin's mobile-first design is not addressed.
- Regression found no significance, suggesting the CDRW framework may be incomplete — use cautiously as justification for excluding these variables.

## Limitations

- Sample size of 150 from only 10 corporations limits statistical power and generalizability. [unacknowledged]
- Relies on self-reported Likert-scale agreement, not observed financial behavior. [unacknowledged]
- The study explicitly acknowledges that regression results were non-significant, suggesting unmeasured confounders (the paper recommends further exploration).
- No control for income volatility or irregular employment, which is common among young professionals in the Philippines. [unacknowledged]
- The paper does not provide regression coefficients or p-values, only states non-significance, limiting citable detail.

## Remember This

- 🔑 CDRW variables do **not** significantly predict financial freedom (p > 0.05) — basic metrics aren't enough.
- 📌 57% of respondents save in alkansya or at home — traditional habits persist despite bank access.
- 💡 "Come-what-may" attitude and utang cycles are key Filipino behavioral patterns for Odin's profiling.
- ⚠️ Study sampled only large-corp employees in Metro Manila — not generalizable to all young professionals.
