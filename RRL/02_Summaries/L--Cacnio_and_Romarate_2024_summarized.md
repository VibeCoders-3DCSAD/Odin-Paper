# How does financial literacy affect financial behavior over the life cycle? Evidence from Filipino households

## Metadata

```yaml
---
paper_id: "f5a3c2e1-d4b3-4c2a-9a1b-2c3d4e5f6a7b"
designation: local
title: "How does financial literacy affect financial behavior over the life cycle? Evidence from Filipino households"
authors: "Cacnio, F.; Romarate, M."
year: 2024
venue: "Bangko Sentral ng Pilipinas Discussion Paper Series"
odin_topics: ["A.1", "F.1"]
shorthand_tags: ["/expenditure-patterns", "/budget-failure-points", "/fil-behavioral-patterns", "/profile-dimensions"]
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

Higher financial literacy among young Filipino adults (18-39) does not guarantee spending within income, but improves loan payment timeliness, retirement planning, and insurance uptake across age groups.

## Problem and Motivation

How financial literacy affects short-term versus long-term financial behaviors across different life stages remains underexplored in developing countries like the Philippines. Understanding age-specific effects is critical for designing effective financial education programs and interventions. Prior studies relied predominantly on developed-country data and did not isolate age as a moderating factor in the literacy-behavior relationship.

## Approach

- Data: 2018 BSP Consumer Finance Survey of 7,084 Filipino households with annual income ≥₱10K and expenditure ≥₱1K.
- Financial Literacy Index (FLI) composed of two equally weighted components: Financial Attitude (money/spending outlook, risk attitude, time discounting) and Financial Aptitude (loan, deposit, and surplus scores).
- FLI ranges 0 to 1; mean FLI = 0.386, indicating low overall financial literacy.
- OLS regression to identify FLI determinants: age group, gender, income, education, presence of children, receipt of remittances.
- Logit regression (odds ratios) to assess impact of financial attitude and aptitude on five binary financial behaviors: spending ≤ income, paying loans on time, loan-to-income ratio ≤1, having pension/retirement plan, having insurance.
- Age groups: Young adult (18-39), Middle-aged (40-59), Senior (60+); young adult as reference category.

## Findings

1. Young adults have the highest FLI (mean 0.392) versus middle-aged (0.387) and seniors (0.370).
2. Higher financial attitude increases likelihood of paying loans on time (odds ratio 4.01, p<0.05).
3. **Financial aptitude strongly predicts having a pension/retirement plan (odds ratio 85.48, p<0.01)** and insurance (odds ratio 46.81, p<0.01).
4. Higher financial literacy (both attitude and aptitude) is associated with lower likelihood of spending ≤ income (odds ratios 0.435 and 0.051, p<0.01).

- Middle-aged and seniors are less likely to spend within income than young adults.
- Only 2% of Filipino adults answered all six basic financial literacy questions correctly (background from BSP survey).

## Key Figures and Tables

- Table 2: FLI summary → mean FLI 0.386, financial aptitude (0.099) much lower than attitude (0.673).
- Table 3: FLI by age group → young adults highest, seniors lowest; attitude drives the difference.
- Table 5: OLS determinants → education, income, children, remittances positively affect FLI; female slightly negative.
- Table 6: Logit odds ratios → financial aptitude strongest predictor of pension and insurance ownership.
- Table 7: Savings by age → seniors have highest average savings (₱36,722) despite smallest sample size.

## Key Equations

$$FLI_i = \frac{1}{2} \sum_{j} x_{ij} \gamma_{j1} + \frac{1}{2} \sum_{j} x_{ij} \gamma_{j2} \in [0,1]$$
*FLI equals equal-weighted sum of financial attitude and aptitude sub-component scores.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| FLI | Financial Literacy Index, a composite score from attitude and aptitude. |
| Financial Attitude | Component measuring money/spending outlook, risk tolerance, and time preference (present vs future). |
| Financial Aptitude | Component measuring actual financial activities: loans, deposits, and surplus allocation. |
| CFS | Consumer Finance Survey, a triennial BSP household survey. |
| OLS | Ordinary Least Squares, a linear regression method. |

## Critical Citations

- [Lusardi & Mitchell, 2014] — Foundational review linking financial literacy to economic outcomes; establishes measurement approach.
- [Huston, 2010] — Conceptual framework for financial literacy as knowledge plus application; adapted for index construction.
- [Agarwal et al., 2009] — Demonstrated age-related patterns in financial decision quality; supports life-cycle analysis.

## Relevance to Odin

**Topics:**

A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

**Contribution to Odin:**

This paper directly informs Odin's user profiling module by providing empirical evidence that Filipino young adults (18-39) exhibit higher financial literacy than older cohorts but are paradoxically less likely to spend within their income. The finding that financial aptitude (actual use of loans, deposits, surplus) strongly predicts retirement planning and insurance uptake suggests that Odin's profile classification should include observed transaction behaviors, not just survey-based attitudes. Additionally, the segmentation into three validated age groups (young, middle, senior) provides a demographic baseline for Odin's behavioral profile dimensions, supporting the design of adaptive budget recommendations that account for life-stage differences.

**Directly justifies:**

- "Filipino young adults (18-39) have the highest financial literacy index score (0.392) among age groups, but higher literacy correlates with lower likelihood of spending within income (OR 0.435, p<0.01)."
- "Financial aptitude — measured by loan, deposit, and surplus activities — is a stronger predictor of long-term financial behaviors (pension: OR 85.48; insurance: OR 46.81) than financial attitude."
- "Only 2% of Filipino adults answered all six basic financial literacy questions correctly, indicating very low objective knowledge despite some positive attitudes."
- "Middle-aged and senior Filipinos are significantly less likely to spend less than or equal to their income compared to young adults, suggesting life stage affects budget adherence independent of literacy."

**Limits of relevance:**

- Data from 2018; spending patterns may have shifted post-pandemic.
- Financial literacy index lacks a pure knowledge component (CFS had no knowledge questions), so findings reflect attitude and aptitude only.
- Sample excludes very low-income households (below ₱10K annual income), limiting generalizability to the poorest segments.
- Causal direction assumed (literacy → behavior); reverse causality or mutual reinforcement not tested.

## Limitations

- Financial literacy measurement omits objective knowledge questions due to survey limitations — acknowledged by authors.
- Small sample for loan payment analysis (1,743) and loan-to-income ratio (1,738) reduces statistical power. [unacknowledged]
- Potential endogeneity between literacy and behavior not fully addressed; only control variables used.
- Savings data likely underreported; only 686 respondents had deposit account details.
- No validation of FLI against external criteria or test-retest reliability.

## Remember This

- 🔑 Young adults (18-39) have highest financial literacy (0.392), yet spend more than income.
- 💡 Financial aptitude (actual banking/loan use) predicts pension uptake 85x better than baseline.
- 📌 Only 2% of Filipino adults pass all basic financial literacy questions — very low baseline.
- ⚠️ Middle-aged and seniors are less likely to budget within income than young adults.
- ✅ Education and remittances increase financial literacy; being female slightly decreases it.
