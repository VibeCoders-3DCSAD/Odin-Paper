# Analysis of the Food and Income Expenditure Survey 2023 Among Filipino Households

## Metadata

```yaml
---
paper_id: "10.20944/preprints202508.0349.v1"
designation: local
title: "Analysis of the Food and Income Expenditure Survey 2023 Among Filipino Households"
authors: "Ama, N. A."
year: 2025
venue: "Preprints.org"
odin_topics: ["1.A", "1.B", "2.A", "3.A", "5.A"]
shorthand_tags: ["/yp-profile", "/income-patterns", "/expenditure-patterns", "/informal-fin-mechanisms", "/fies-bsp-categories", "/fil-profile-construction"]
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
```

## TL;DR

Among 163,268 Filipino households, food is a necessity (income elasticity 0.58), with rural households spending more on food than urban but remaining more food-insecure.

## Problem and Motivation

Understanding how household income and food expenditure interact is fundamental to shaping food security and poverty policies, yet detailed 2023 data on Filipino households remains underanalyzed. Food accounts for the largest share of household consumption (57.2% in 2021), but prior studies used older survey rounds or lacked advanced spatial and nonlinear methods. This study fills the gap by applying PCA, spatial mapping, GAM, and Engel curve analysis to the 2023 Family Income and Expenditure Survey (FIES).

## Approach

- Dataset: 163,268 households from the 2023 Philippine Family Income and Expenditure Survey (FIES), nationally representative.
- Methods: Descriptive statistics, Gini index and Lorenz curves for inequality, Principal Component Analysis (PCA) on 10 income sources.
- Spatial analysis: Provincial-level mapping of mean food expenditure using GADM shapefiles.
- Urban-rural comparison: Non-parametric Mann–Whitney U test (Wilcoxon rank-sum) for food spending and per capita income.
- Food insecurity prediction: Generalized Additive Model (GAM) with logit link, smooth terms for household size, per capita income, and livelihood incomes.
- Engel curve: Log-log linear regression estimating income elasticity of food.
- Food away from home: Beta regression with logit link, predictors: log income, urbanicity, household size.

## Findings

1. **Food income elasticity = 0.58 (necessity good, Engel’s Law)** — a 1% income increase raises food spending by only 0.58%.
2. Rural households spend more on food (median ₱102,467) than urban (median ₱80,700) and have higher per capita income (₱6,000 vs ₱5,000), both differences highly significant (p<.001).
3. GAM predicted food insecurity with 90.0% accuracy (95% CI [0.8987,0.9016]) and AUC 0.86; per capita income (edf=6.71, χ²=16,981) and household size (edf=6.23) are strongest nonlinear predictors.
- PCA identified five income source clusters: retail/transport (12.4% variance), informal services (12.1%), agriculture (10.8%), fishing (10.1%), and remittances/forestry (10.0%).
- Bread (29.5%) and meat (14.8%) dominate food spending; fruit (4.5%) is smallest.
- Wealthier and smaller households spend proportionally more on food outside home; rural households also show higher outside-home share (β=-0.50 for urban vs rural).

## Key Figures and Tables

- Figure 5: Spatial map of mean food expenditure → Leyte and Bohol highest (>₱120k); Northern Luzon lowest (₱80k–90k).
- Figure 6: Ternary plot (bread, meat, fish) → households cluster near bread–meat edge, indicating preference over fish.
- Figure 10: Engel curve (log-log) → positive slope of 0.58, showing inelastic relationship.
- Table 5: GAM results → s(RPCINC) most significant (edf=6.71, χ²=16,981.31, p<.001).
- Table 10: Beta regression → log-income positive (β=0.72), urban negative (β=-0.50), both p<.001.

## Key Equations

$$\log(\text{FOOD}_i) = \beta_0 + \beta_1 \log(\text{TINC}_i) + \varepsilon_i$$
*Income elasticity of food: percentage change in food spending per 1% income change.*

$$g(E(Y)) = \beta_0 + f_1(\text{FSIZE}) + f_2(\text{RPCINC}) + \dots$$
*GAM link function (logit) sums smooth nonlinear effects of each predictor.*

$$\text{logit}(\mu_i) = \ln\left(\frac{\mu_i}{1-\mu_i}\right) = \beta_0 + \beta_1 \log(\text{INCOME}_i) + \beta_2 \text{URB}_i + \beta_3 \text{FSIZE}_i$$
*Beta regression logit link models proportion of food spent outside home.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| FIES | Family Income and Expenditure Survey (Philippine Statistics Authority) — national household survey. |
| PCA | Principal Component Analysis — reduces many income sources into few clusters. |
| GAM | Generalized Additive Model — captures nonlinear relationships without assuming a fixed curve shape. |
| Engel’s Law | As income rises, the proportion spent on food falls, even if absolute spending rises. |
| Income elasticity | % change in demand for a good when income rises 1%. <1 = necessity. |
| Food insecurity (operational) | Household food expenditure ratio below 0.30 (30% of total spending). |
| RPCINC | Real per capita income (income per person, inflation-adjusted). |
| Gini coefficient | 0 = perfect equality, 1 = perfect inequality. Food Gini=0.277, income Gini=0.394. |

## Critical Citations

- [Cirera & Masset, 2010] — Foundational statement of Engel’s Law and income elasticity classification.
- [Valera et al., 2022] — Previous QUAIDS demand estimation using FIES, establishing baseline for food group elasticities.
- [Bairagi et al., 2022] — Documented structural shifts in rural vs urban food baskets in the Philippines.

## Relevance to Odin

**Topics:**

1.A — Filipino Young Professionals as a Demographic

1.B — Financial Structure of Filipino Young Professionals

2.A — Culturally Specific Financial Practices

3.A — Expense Categorization Frameworks

5.A — Financial Behavioral Profiles in Personal Finance

**Contribution to Odin:**

This paper provides empirically grounded baseline data on Filipino household income and spending patterns, directly informing Odin’s expense categorization and budget recommendation modules. The finding that food is a necessity (elasticity 0.58) justifies setting food as a protected category with a mandatory spending floor in Odin’s budget constraint formulation. The PCA-derived income source clusters (retail, transport, farming, remittances) offer a data-driven typology for financial behavioral profile classification, relevant to Odin’s profiling module. Urban-rural differences and the strong predictive power of per capita income and household size on food insecurity highlight variables that Odin’s forecasting and anomaly detection must account for when targeting Filipino young professionals across different geographies.

**Directly justifies:**

- “Among Filipino households, food income elasticity is 0.58, confirming Engel’s Law — a 1% income increase raises food spending by only 0.58%.”
- “Rural households spend more on food (median ₱102,467) than urban households (₱80,700) but remain more vulnerable to food insecurity, indicating that location modifies spending behavior independently of income.”
- “Bread (29.5%) and meat (14.8%) account for the largest shares of household food expenditure, while fruit (4.5%) is smallest — a spending hierarchy that can guide default category weights.”
- “PCA on 163,268 households identified five distinct income source clusters: retail/transport, informal services, agriculture, fishing, and remittances/forestry — providing a basis for Filipino-specific financial behavior profiles.”
- “Per capita income is the strongest nonlinear predictor of food insecurity (edf=6.71, χ²=16,981, p<.001), supporting income-based thresholds in budget recommendation.”

**Limits of relevance:**

- Paper analyzes all Filipino households, not specifically young professionals aged 20–40; spending patterns may differ for this subset (e.g., different food away-from-home behavior).
- Cross-sectional 2023 data cannot capture seasonal or year-to-year behavioral drift, limiting direct use for forecasting module validation.
- Food categories are aggregated (bread, meat, fish, fruit, vegetables) — less granular than Odin’s expense categorization needs.
- Relies on survey-reported spending, not actual transaction logs; recall bias may affect comparability to Odin’s manual input data.
- Food insecurity defined by expenditure ratio <0.30, not a behavioral or psychological measure; Odin’s anomaly detection focuses on deviations from user’s own pattern, not absolute poverty thresholds.

## Limitations

- Cross-sectional design prevents causal inference; associations cannot distinguish income changes from cohort effects.
- No validation of the 0.30 food expenditure ratio threshold against actual hunger or food sufficiency measures. [unacknowledged]
- GAM model shows low specificity (24.9%), meaning it frequently misclassifies food-insecure households as food-secure — a limitation for any diagnostic use.
- Spatial analysis aggregated at province level; intra-provincial urban-rural gradients and barangay-level disparities are lost.
- Self-reported income and expenditure data may contain recall bias, especially for informal or non-monetized activities.

## Remember This

- 🔑 **Food income elasticity = 0.58** — necessity good; budget must protect food as a fixed-priority category.
- 📌 Rural households spend **₱102k vs ₱80k** on food — location reverses the intuitive urban-spends-more pattern.
- 💡 Bread (29.5%) and meat (14.8%) dominate — set default food subcategory weights accordingly.
- ⚠️ GAM predicts food insecurity with 90% accuracy but only 25% specificity — don't use for individual risk flags.
- 🧠 PCA yields 5 income clusters (retail, transport, farming, fishing, remittances) — profile dimensions for Filipino users.
