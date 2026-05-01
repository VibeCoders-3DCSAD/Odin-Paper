---
name: paper-summary
paper_id: "f8c3e5a2-7b1d-4e9c-8a3f-2d6e9b1c4a7d"
source_document: "Cacnio_Romarate_converted.md"
designation: local
title: "How does financial literacy affect financial behavior over the life cycle? Evidence from Filipino households"
authors: "Cacnio, F. Q.; Romarate, M. E. G."
year: 2024
venue: "Unknown"
odin_topics: [1, 9]
shorthand_tags: ["/expenditure-patterns", "/budget-time-horizons", "/fil-behavioral-patterns", "/profile-dimensions"]
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

# How does financial literacy affect financial behavior over the life cycle? Evidence from Filipino households

## TL;DR
Higher financial literacy among young Filipinos correlates with greater spending but also more retirement and insurance plans.

## Problem and Motivation
Prior studies on financial literacy and behavior focus on developed nations, leaving a gap in developing countries like the Philippines where literacy levels are lower. Researchers lacked evidence on how financial literacy interacts with age to shape short-term (spending, loans) and long-term (retirement, insurance) financial decisions. This paper addresses that gap using nationally representative Filipino household data.

## Approach
- Data: 2018 BSP Consumer Finance Survey, final sample of 7,084 Filipino households.
- Constructed Financial Literacy Index (FLI) from financial attitude (risk, time discounting) and financial aptitude (loan/deposit/surplus engagement) components.
- Used OLS to identify determinants of financial literacy (age, gender, income, education, children, remittances).
- Used logistic regression to assess effects on budgeting (spending ≤ income), loan payment timeliness, loan-to-income ratio, retirement plans, and insurance.
- Compared young adults (18-39), middle-aged (40-59), and seniors (60+).

## Findings
1. Young adults have highest FLI (0.392) vs middle-aged (0.387) and seniors (0.370).
2. Higher financial aptitude increases likelihood of having retirement plans by **85.5 times** (odds ratio 85.478, p<0.01).
3. Higher financial attitude increases likelihood of paying loans on time by 4.0 times (odds ratio 4.011, p<0.05).
4. Higher financial literacy (both components) reduces likelihood of spending within income (attitude OR=0.435, aptitude OR=0.051).
5. Middle-aged and seniors are less likely to spend within income than young adults (OR=0.610 and 0.667, p<0.01).

## Key Figures and Tables
- Table 1: Descriptive statistics → 45% of respondents are middle-aged, 64% female, 81% have children.
- Table 2: FLI scores → Financial aptitude (0.099) is much lower than attitude (0.673), pulling overall FLI down.
- Table 6: Logistic regression → Financial aptitude strongly predicts retirement (OR=85.5) and insurance (OR=46.8); attitude predicts on-time loan payment.

## Key Equations
$$FLI_{i} = \frac{1}{2}\sum_{j}^{n}x_{ij}\gamma_{j1} + \frac{1}{2}\sum_{j}^{n}x_{ij}\gamma_{j2}\in [0,1]$$
*Financial Literacy Index: equal weight (0.5) to attitude and aptitude, each composed of three sub-components.*

## Definitions
| Term / Acronym | Plain-English Definition |
|----------------|--------------------------|
| FLI | Financial Literacy Index — a score from 0 (low) to 1 (high). |
| Financial attitude | Component measuring risk tolerance, time discounting, and spending-planning mindset. |
| Financial aptitude | Component measuring actual use of loans, deposit accounts, and surplus money activities. |
| Odds ratio (OR) | Multiplicative change in likelihood; OR >1 means higher probability. |

## Critical Citations
- [Lusardi & Mitchell, 2014] — Foundational link between financial literacy and retirement planning.
- [Huston, 2010] — Defines financial literacy as knowledge plus application (attitude and behavior).
- [Agarwal et al., 2009] — Age-related financial decision quality in debt markets.

## Relevance to Odin

**Topics:**
1 (Spending and Budgeting Behavior of Filipino Young Professionals), 9 (User Behavioral Profiling in Filipino Personal Finance Contexts)

**Contribution to Odin:**
This paper justifies modeling both financial attitude (risk, time discounting) and financial aptitude (engagement with loans, deposits, surplus) as distinct user dimensions in Odin's profile. It shows that young Filipinos (the target users of Odin) have the highest financial literacy but also spend beyond their income, suggesting a need for budgeting nudges rather than purely educational interventions. The finding that higher financial aptitude strongly predicts retirement and insurance uptake validates Odin's goal of promoting long-term financial behavior through improved financial skills.

**Directly justifies:**
- Young Filipino professionals (18-39) exhibit higher financial literacy than older cohorts but are more likely to overspend (spending > income).
- Financial aptitude (loan/deposit/surplus engagement) is a stronger predictor of long-term financial behavior (retirement, insurance) than financial attitude.
- Age-based financial behavior patterns (e.g., middle-aged take larger loans) require adaptive profiling in personal finance systems.
- Financial attitude influences loan repayment timeliness, supporting inclusion of attitude metrics in user behavioral models.

**Limits of relevance:**
- Data from 2018 may not fully reflect post-pandemic financial behaviors or digital finance adoption.
- Sample excludes households below PHP 10,000 annual income, limiting generalizability to extreme poverty contexts.
- Financial knowledge was not directly measured due to survey limitations; only attitude and aptitude are captured.
- Does not address mobile-first design, algorithmic forecasting, or anomaly detection — only behavioral patterns.

## Limitations
- Financial knowledge (numeracy, inflation, interest) not measured — only attitude and aptitude.
- Survey data is self-reported, subject to recall and social-desirability bias.
- Cross-sectional design cannot establish causality (reverse causality possible: behavior → literacy).
- Low response rates for loan and savings amount details reduce statistical power for some analyses.

## Remember This
- 🔑 Young adults (18-39) have highest financial literacy but are **less likely** to spend within their income.
- 📌 Higher financial aptitude → **85x** more likely to have retirement plans (strongest effect in the paper).
- ⚠️ Financial attitude affects loan repayment timeliness (4x higher odds); aptitude affects long-term planning like retirement and insurance.