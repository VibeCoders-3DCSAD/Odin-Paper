---
name: paper-summary
paper_id: "10.20944/preprints202508.0349.v1"
source_document: "Ama_converted.md"
designation: local
title: "Analysis of the Food and Income Expenditure Survey 2023 Among Filipino Households"
authors: "Ama, N. A."
year: 2025
venue: "Preprints.org"
odin_topics: [1]
shorthand_tags: [/expenditure-patterns, /income-typology]
summary_date: 2026-04-28
version: "1.0"
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[X]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
---

# Analysis of the Food and Income Expenditure Survey 2023 Among Filipino Households

## TL;DR
Food is a necessity: a 1% income rise increases food spending by only 0.58%, with rural households spending more on food than urban ones.

## Problem and Motivation
Policymakers need empirical evidence on how Filipino household income, geography, and livelihood affect food spending patterns. Existing studies lack advanced statistical methods and spatial analysis at the provincial level. This paper fills that gap using the nationally representative 2023 FIES dataset.

## Approach
- Data: 163,268 Filipino households from the 2023 Family Income and Expenditure Survey (PSA).
- Methods: PCA, spatial mapping, GAM, Engel curves, beta regression, and Mann-Whitney U tests.
- Outcome variables: food expenditure, food insecurity (binary), share of food spent outside home.
- Predictors: income deciles, livelihood type, household size, urban/rural residence.

## Findings
1. Mean food expenditure is **P101,708** per household; Gini for food (0.277) is lower than for income (0.394).
2. Rural households spend **P21,767 more** on food than urban households (Mdn P102,467 vs. P80,700, p<.001).
3. Income elasticity of food is **0.58** — food is a necessity good (Engel's Law confirmed).
4. Bread (29.5%), meat (14.8%), and fish (14.2%) dominate food spending; fruits and vegetables are under-budgeted.
5. Per capita income is the strongest nonlinear predictor of food insecurity (edf=6.71, χ²=16,981, p<.001).
- Higher-income and smaller households spend proportionally more on food outside the home.

## Key Figures and Tables
- Table 1: Descriptive statistics → Mean income P332,147, mean food P101,708.
- Figure 5: Spatial map → Leyte and Bohol highest food expenditure (P120,000+); Northern Luzon lowest.
- Figure 10: Engel curve (log-log) → Slope 0.58, showing inelastic food demand.

## Key Equations
$$log(FOOD_i) = 4.177 + 0.580 \cdot log(TINC_i)$$
*Income elasticity of 0.58: food spending grows slower than income.*

$$logit(\mu_i) = -10.61 + 0.717 \cdot log(INCOME) - 0.498 \cdot URB - 0.026 \cdot FSIZE$$
*Higher income increases share of food outside home; urban and larger households reduce it.*

## Definitions
| Term / Acronym | Plain-English Definition |
|----------------|--------------------------|
| FIES | Family Income and Expenditure Survey — Philippine national household survey. |
| RPCINC | Real per capita income — income per person adjusted for inflation. |
| Engel's Law | As income rises, the proportion spent on food falls, even if total food spending rises. |
| GAM | Generalized Additive Model — captures nonlinear relationships without assuming linearity. |

## Critical Citations
- [Valera et al., 2022] — QUAIDS model applied to FIES; staple foods show inelastic demand.
- [Briones, 2022] — Cash transfers buffer poor households against food price shocks.
- [Bairagi et al., 2022] — Urban vs. rural food basket composition differences in the Philippines.

## Relevance to Odin

**Topics:**
1. Spending and Budgeting Behavior of Filipino Young Professionals

**Contribution to Odin:**
This paper provides authoritative Philippine household expenditure data showing that food is treated as a necessity good with inelastic demand (ε=0.58). It establishes that household size, income level, and rural/urban status are strong predictors of spending patterns and food insecurity. These findings directly support Odin's assumption that young Filipino professionals exhibit income-inelastic food spending behavior and that demographic factors must inform personalized budgeting.

**Directly justifies:**
- Filipino households exhibit **income-inelastic food demand** (elasticity 0.58), validating Engel's Law in the local context.
- Household size is a significant nonlinear predictor of food insecurity — larger households allocate proportionally less to discretionary categories.
- Rural households spend more absolute on food but less proportionally on higher-value categories — geographic context shapes consumption.
- Per capita income is the strongest predictor of food-related financial vulnerability (χ²=16,981, p<.001).

**Limits of relevance:**
- Focuses on general population, not specifically young professionals (ages 22–35).
- No data on digital financial tools or app-based spending tracking.
- Cross-sectional design provides association, not causal inference for behavior change.

## Limitations
- Cross-sectional data prevents causal claims about income changes over time.
- No dietary diversity or nutritional adequacy measures (only expenditure).
- Spatial analysis limited to province level; intra-provincial variations lost.
- Self-reported income/expenditure may have recall bias, especially for informal sector households.

## Remember This
- 🔑 **ε = 0.58** — Food is a necessity: income up 1%, food spending up only 0.58%.
- 📌 **Rural households spend P22K more** on food annually than urban counterparts.
- 💡 **Bread + meat + fish = 58.5%** of food budget; fruits and vegetables are underfunded.