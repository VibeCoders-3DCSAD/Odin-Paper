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
odin_topics: ["A.1", "F.1", "G.1"]
shorthand_tags: ["/expenditure-patterns", "/income-typology", "/fil-behavioral-patterns", "/fil-pfms-categories", "/fies-bsp-mapping"]
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

Food spending is income‑inelastic (elasticity = 0.58) — as Filipino household income rises 1%, food expenditure rises only 0.58%, confirming Engel’s Law.

## Problem and Motivation

Understanding how household income and food expenditure interact is essential for food security and poverty policy, but prior Philippines studies lacked integrated spatial, compositional, and nonlinear modeling. This gap matters because food accounts for the largest share of Filipino household spending (57.2% in 2021), yet the drivers and geographic patterns remain underexplored. Previous work used older FIES rounds or narrower methods, leaving a need for a multi‑method update with 2023 data.

## Approach

- Data: 163,268 Filipino households from the 2023 Family Income and Expenditure Survey (FIES), nationally representative.
- **Income & expenditure patterns:** Descriptive statistics, Gini index, Lorenz curves.
- **Income source clustering:** Principal Component Analysis (PCA) on 10 income‑generating activities, with scree plots and biplots.
- **Spatial clustering:** Provincial‑level mapping using GADM shapefiles (Level 1 administrative units).
- **Rural‑urban comparison:** Mann‑Whitney U test (non‑parametric) for food expenditure and per capita income.
- **Food insecurity prediction:** Generalized Additive Model (GAM) with smooth terms for household size, per capita income, crop, livestock, fishing, forestry income, plus urban/rural indicator.
- **Income‑food relationship:** Log‑log Engel curve (linear regression on log‑transformed variables) to estimate income elasticity.
- **Out‑of‑home food spending:** Beta regression with logit link, using log income, urbanicity, and household size as predictors.

## Findings

1. Mean annual household income = ₱332,147 (SD ₱406,065); median = ₱241,080. Food expenditure Gini = 0.277, lower than income Gini (0.394) — food spending is more evenly distributed.
2. **Income elasticity of food = 0.58** (p < .001, R² = 0.589) — food is a necessity; a 1% income increase raises food spending only 0.58%.
3. Rural households spend more on food (median ₱102,467 vs. urban ₱80,700) and have higher per capita income (median ₱6,000 vs. ₱5,000), both p < .001.

- PCA identified five income‑source components: retail/transport, informal/miscellaneous, crop farming (positive) vs. fishing (negative), forestry vs. remittances/manufacturing, and remittances/forestry.
- Provinces with highest food expenditure: Leyte and Bohol (>₱120,000); lowest: Cagayan, Isabela, Southern Leyte (₱80,000–90,000).
- GAM model (accuracy 90.02%, AUC 0.86) shows per capita income has the strongest nonlinear effect on reducing food insecurity; household size increases risk; urban residence lowers risk (β = −0.51).

## Key Figures and Tables

- Figure 1: Lorenz curve for food expenditure → moderate inequality, Gini = 0.277.
- Figure 2: Histogram of food expenditure per member → strong right skew; most households spend low amounts.
- Figure 5: Philippines spatial map of mean food expenditure → Leyte and Bohol are high‑spending clusters.
- Figure 6: Ternary plot (bread, meat, fish shares) → households concentrate spending on bread and meat, not fish.
- Figure 10: Engel curve (log‑log scatter with regression line) → positive but inelastic slope (0.58).

## Key Equations

$$log(FOOD_i) = \beta_0 + \beta_1 \cdot log(TINC_i) + \varepsilon_i$$
*Log‑log Engel curve: slope = income elasticity of food demand.*

$$g(E(Y)) = \beta_0 + f_1(x_1) + \dots + f_m(x_m)$$
*GAM link function (logit for binary food insecurity) with smooth nonlinear terms.*

$$logit(\mu_i) = ln\left(\frac{\mu_i}{1-\mu_i}\right) = \beta_0 + \beta_1 \cdot log(INCOME_i) + \beta_2 \cdot URB_i + \beta_3 \cdot FSIZE_i$$
*Beta regression for proportion of food spending outside the home, with logit link.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| FIES | Family Income and Expenditure Survey — Philippine national household survey on income and spending. |
| PCA | Principal Component Analysis — reduces many correlated variables into a few independent components. |
| GAM | Generalized Additive Model — regression that allows nonlinear, smooth relationships for predictors. |
| Engel’s Law | As income rises, the proportion spent on food falls, even if absolute food spending increases. |
| Income elasticity | % change in spending for a 1% change in income (<1 = necessity, >1 = luxury). |
| Gini coefficient | Measure of inequality from 0 (perfect equality) to 1 (perfect inequality). |
| RPCINC | Real per capita income — inflation‑adjusted income per household member. |

## Critical Citations

- [Regmi & Meade, 2013] — Establishes demand‑side drivers of food security and Engel’s Law framework.
- [Valera et al., 2022] — Previous Philippine food demand estimation using QUAIDS on 2018 FIES; baseline for method comparison.
- [Bairagi et al., 2022] — Structural shifts in rural‑urban food baskets in the Philippines; directly comparable to this study’s urban‑rural findings.
- [Briones, 2022] — Food and nutrient response to price shocks; supports the policy relevance of income‑food relationships.

## Relevance to Odin

**Topics:**

A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

G.1 — Expense Categorization in Filipino Personal Finance Contexts

**Contribution to Odin:**

This paper provides empirical, nationally representative data on how Filipino households actually spend on food across categories (bread 29.5%, meat 14.8%, fish 14.2%), directly grounding Odin’s expense categorization module in local FIES behavior rather than Western assumptions. The PCA‑derived income source typology (retail/transport, farming, fishing, remittances, informal services) offers a data‑driven foundation for Odin’s user profile classification — enabling the system to distinguish users by dominant income type, which affects spending volatility and budget recommendation needs. The Engel curve elasticity (0.58) quantifies how spending on food (a necessity) scales with income, which can calibrate Odin’s spending forecasting module: lower‑income users will allocate a larger share of any income increase to food, while higher‑income users shift proportionally more to non‑food categories. The finding that rural households spend more on food and have higher per capita income than urban households challenges simple income‑based assumptions and suggests Odin must incorporate geography and cost‑of‑living adjustments.

**Directly justifies:**

- “Filipino households allocate 29.5% of total food expenditure to bread, 14.8% to meat, 14.2% to fish, 7.2% to vegetables, and 4.5% to fruit (2023 FIES, n=163,268).”
- “Income elasticity of food demand among Filipino households is 0.58 — a 1% income rise increases food spending only 0.58%, confirming food as a necessity (Engel’s Law).”
- “Principal Component Analysis of 10 income sources reveals five distinct livelihood clusters: retail/transport, informal/miscellaneous, crop farming (positive vs. fishing negative), forestry vs. remittances, and remittances/forestry — these can inform user profiling.”
- “Rural households have higher median per capita income (₱6,000) and higher food spending (₱102,467) than urban households (₱5,000 and ₱80,700), indicating geography‑dependent spending patterns that a budget system must account for.”
- “Generalized Additive Model (AUC 0.86) shows household size, per capita income, and urban/rural status have strong nonlinear effects on food insecurity — similar nonlinearities likely affect budget adherence.”

**Limits of relevance:**

- The study covers all Filipino households, not specifically young professionals (20–40) — spending patterns may differ for this subset.
- Data are from 2023, but Odin targets current and future users; spending shares may shift with inflation or post‑pandemic recovery.
- Food expenditure categories are broad (e.g., “meat” and “bread”) — Odin needs more granular categorization (e.g., restaurant vs. grocery, specific subtypes).
- The paper does not analyze discretionary vs. non‑discretionary spending thresholds, which are central to budgeting.

## Limitations

- Cross‑sectional design prevents causal inference on how income changes affect food spending over time (acknowledged).
- Reliance on self‑reported income and expenditure may introduce recall or underreporting bias, especially for informal sources (acknowledged).
- No nutritional or dietary diversity measures — cannot assess quality of food spent, only quantity (acknowledged).
- Spatial analysis only at provincial level, masking intra‑provincial rural‑urban gradients [unacknowledged].
- The GAM model for food insecurity had low specificity (24.93%), meaning it poorly identifies insecure households — weak for predictive use [unacknowledged].

## Remember This

- 🔑 **Income elasticity of food = 0.58** — necessity good, not luxury; 1% income rise → 0.58% more food spending.
- 📌 **Top food categories:** bread 29.5%, meat 14.8%, fish 14.2% — use these as default weights in Odin’s expense categorization.
- 💡 **Five income clusters** from PCA: retail/transport, informal, farming (vs. fishing), forestry/remittances, remittances/forestry — feed into user profiling.
- ⚠️ **Rural households spend more on food (₱102k vs. ₱80k urban)** — geography matters, don’t assume urban = higher spending.
- ✅ **Gini for food = 0.277** (vs. income 0.394) — food spending is more equal across households; a stable baseline for budget recommendations.
