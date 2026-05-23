# Measuring the unmeasurable multidimensional poverty for economic development: Datasets, algorithms, and models from the poorest region of Luzon, Philippines

## Metadata

```yaml
---
paper_id: "10.1016/j.dib.2024.110150"
designation: algorithm-specific
title: "Measuring the unmeasurable multidimensional poverty for economic development: Datasets, algorithms, and models from the poorest region of Luzon, Philippines"
authors: "Onsay, E. A.; Rabajante, J. F."
year: 2024
venue: "Data in Brief"
odin_topics: ["1.B", "5.C", "6.A", "8.A"]
shorthand_tags: ["/income-patterns", "/classifier-candidates", "/forecasting-methods-survey", "/anomaly-taxonomy"]
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

Logistic regression applied to 14,021 households in rural Philippines predicts multidimensional poverty with 73.29% accuracy using health, housing, water, education, and disaster indicators.

## Problem and Motivation

Poverty is multidimensional and notoriously difficult to measure, yet most poverty studies rely on generic macro-level data with large sampling errors. Rural localities need granular, locality-specific poverty measurements to design targeted interventions, but such data from the poorest district of Luzon has been entirely absent.

## Approach

- Dataset: 14,021 households (63,749 members) from 34 barangays in Goa, Camarines Sur — complete enumeration, no sampling error.
- Method: Logistic regression predicting poverty outcomes at income and food thresholds.
- Variables: 19 multidimensional indicators (health, housing, water/sanitation, education, employment, crime, calamities, disaster preparedness) plus 13 interaction terms.
- Tools: R, STATA, Python, SPSS, MS Excel for cleaning, transformation, and modeling.
- Poverty metrics: Headcount ratio, poverty gap index (depth), severity index (intensity), Watts index (distributional).

## Findings

1. Municipality-wide poverty incidence is **63.70%** (headcount ratio) — ranges from 21.38% to 98.45% across barangays.
2. Logistic regression achieved **73.29% correctly classified** predictions for poverty status.
3. **77.48% sensitivity** (correctly identified poor households) and 66.31% specificity.
- Household size, informal settler status, and lack of water/sanitation access are strong positive predictors of poverty (p < 0.001).
- Disaster preparedness reduces poverty probability; typhoon and drought exposure increase it.

## Key Figures and Tables

- Table 5: Poverty analytics by barangay → headcount ranges 21%–98%; severity index highest in Abucayan (0.0723).
- Figure 3: Rural poverty analytics visualization → poverty incidence varies dramatically across sectors within same municipality.
- Figure 4: Classification margins → probability of poverty decreases as water access and housing quality improve.
- Table 8: Classification matrix → 73.29% correct classification; 79.25% positive predictive value.
- Table 10: Logistic regression coefficients by sector → significant predictors vary across the four sectors (Isarog, Poblacion, Ranggas, Salog).

## Key Equations

$$POVC\_IT = \beta_0 + \beta_1 C\_Mortality + \beta_2 M\_Mortality + \beta_3 C\_Malnutrition + ... + \beta_n i + \mu$$
*Logistic regression predicting poverty at income threshold from 19 multidimensional indicators.*

$$P0 = \frac{1}{N} \sum_{i=1}^{N} I(y_i < z)$$
*Headcount ratio — proportion of population below poverty line z.*

$$P1 = \frac{1}{N} \sum_{i=1}^{N} \frac{G_i}{z}$$
*Poverty gap index — average distance below poverty line as percentage of the line.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| CBMS | Community-Based Monitoring System — local government household census data collection mandated by RA 11315 |
| Headcount ratio | Proportion of population living below poverty line (incidence measure) |
| Poverty gap index | Average shortfall from poverty line as % of line (depth measure) |
| Severity index | Squared poverty gap — weights poorest households more heavily (intensity measure) |
| Watts index | Distribution-sensitive poverty measure using log of income ratios |
| Multidimensional poverty | Poverty measured across health, education, housing, water, employment, and security — not just income |
| Ceteris paribus | All other variables held constant [think: other things being equal] |

## Critical Citations

- [Haughton & Khandker, 2009] — Foundational handbook defining poverty measurement formulas (headcount, gap, severity, Watts).
- [Foster, Greer & Thorbecke, 1984] — Origin of the decomposable poverty measures (FGT indices) used in this analysis.
- [Reyes et al., 2011] — Philippine chronic and transient poverty methodology adapted for the logistic regression framework.

## Relevance to Odin

**Topics:**

1.B — Financial Structure of Filipino Young Professionals

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

8.A — Anomaly Detection in Personal Finance Systems

**Contribution to Odin:**

This paper provides a validated methodological template for Odin's classification module, demonstrating that logistic regression on complete enumeration household data achieves 73% accuracy in predicting binary financial outcomes (poor/non-poor). The interaction-term approach (e.g., informal settlers × household members) is directly applicable to Odin's profile classification, where income stability interacts with dependency ratios. Although the outcome variable is poverty status rather than spending behavior, the same logistic regression framework can classify users into financial behavioral profiles using Odin's transaction and declaration data.

**Directly justifies:**

- "Complete enumeration household data eliminates sampling error entirely, a property relevant to Odin's user-level classification where each user is their own population."
- "Logistic regression on 19 multidimensional indicators achieved 73.29% classification accuracy for poverty status, providing a baseline benchmark for Odin's behavioral profile classifier."
- "Interaction terms (e.g., household size × informal settlement) significantly improved model fit — analogous to Odin using income stability × dependency ratio interactions in profile classification."
- "The poverty gap index measures depth, not just incidence — Odin's anomaly detection can similarly measure deviation magnitude, not just binary overage."
- "Predictive power varied substantially across four sectors within the same municipality — Odin must expect and handle geographic and cultural heterogeneity in spending patterns."

**Limits of relevance:**

- Paper predicts poverty (income < threshold), not per-category spending or budget adherence — the dependent variable differs from Odin's forecasting targets.
- Rural agricultural population (Goa, Camarines Sur) differs demographically from Metro Manila young professionals.
- Data is complete enumeration census (no sampling), but Odin operates on individual user data with cold-start sparsity.
- Logistic regression is simpler than LSTM or sequential models Odin may use for spending forecasting; relevance is primarily to classification, not time-series prediction.

## Limitations

- Time restriction: data covers 2018–2020 only; no update cycle specified for longitudinal analysis.
- Geography-specific: rural Bicol region findings may not generalize to urban Metro Manila context. [unacknowledged]
- No validation of model performance on holdout data or alternative time periods — classification accuracy reported on training data only. [unacknowledged]
- Binary poverty outcome (poor/non-poor) collapses continuous variation in financial health.
- Authors state "no known limitations due to complete enumeration," but sampling error is not the only validity threat — omitted variable bias remains.

## Remember This

- 🔑 **73.29% classification accuracy** — logistic regression on household indicators predicts binary financial status.
- 📌 Household size + informal settlement interaction strongly predicts poverty (p < 0.001 across sectors).
- ⚠️ Poverty incidence varies from 21% to 98% across barangays in same municipality — local context dominates.
- 💡 Complete enumeration (14k households) eliminated sampling error — design principle for user-level systems.
- 🔍 Poverty gap index measures **depth**, not just incidence — analogous to anomaly severity, not just detection.
