# Do Remittances Boost Household Spending: New Evidence from Migrants’ Household Survey

## Metadata

```yaml
---
paper_id: "d8f4c5a2-6b3a-5c1e-9f7d-2e8b4a6c0d1e"
designation: local
title: "Do Remittances Boost Household Spending: New Evidence from Migrants’ Household Survey"
authors: "Bayangos, V. B.; Lubangco, C. K."
year: 2024
venue: "Unknown"
odin_topics: ["A.1", "F.1", "G.1"]
shorthand_tags: ["/expenditure-patterns", "/income-type-behavior-diff", "/budgeting-prevalence", "/fil-behavioral-patterns", "/fies-bsp-mapping"]
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

Remittances boost household spending in the Philippines, but poor households face binding financial constraints that limit welfare gains, and high transfer costs reduce remittance inflows.

## Problem and Motivation

The nuanced relationship between remittances, household consumption patterns, and macroeconomic drivers remains poorly understood despite extensive research. Remittances reached USD40 billion in the Philippines in 2023, serving as a critical source of foreign exchange and household support. Prior studies did not combine household-level spending allocation analysis with regional panel data on remittance determinants.

## Approach

- Data: Survey on Overseas Filipinos (SOF) 2007-2022 (1.96M OFWs in 2022), Family Income and Expenditure Survey (FIES) 2018/2021, and BSP survey of 44 banks + 15 non-banks on transfer costs (2015-2023).
- Logistic regression (odds ratios) to assess determinants of saving vs investing behavior among migrant households.
- Propensity score matching (PSM) to estimate average treatment effect of remittance receipt on household expenditure shares.
- Working-Leser model for budget share analysis across food, education, health, clothing, housing, and durable goods.
- Two-step system panel GMM with 17 Philippine regions (2007-2022) to identify macroeconomic drivers of remittance flows.

## Findings

1. Average saving rate from cash remittances (2008-2022) is 9.9%; investing rate is 7–8%. **50% of OFW households allocate nothing to savings; 75% allocate nothing to investments.**
2. Non-poor remittance-receiving households increase education spending share by 0.40 percentage points (pp) and health by 0.50 pp, while poor households see only 0.02 pp (ns) and 0.11 pp respectively — financial constraints are binding for the poor.
3. A 1% increase in telegraphic transfer fees reduces cash remittances by approximately 12–13% (p < 0.01), with fees representing 6–7% of average remittance value.
4. Regional unemployment rate is positively associated with remittances (altruistic motive), while higher regional wages reduce remittances (coefficient -0.525, p < 0.10).

- OFW households save more (10.35% vs 7.40%) than households with immigrant members, consistent with return-migration motives.

## Key Figures and Tables

- Figure 4: Saving vs investing rates (2008-2022) → saving peaked at 13.1% in 2009, investing rose to 10.6% during COVID.
- Figure 5: Distribution of allocation rates → 50% save nothing, 75% invest nothing, 90%+ consume immediately.
- Table 3: Average treatment effects for poor vs non-poor households → non-poor show significant education/health gains; poor show none.
- Table 5: Panel GMM determinants → transfer fees (negative, -12.7 to -19.0 coefficient) and unemployment (positive) drive remittances.

## Key Equations

$$Y_{ij} = \beta_0 + \beta_1 \ln cons_j + \boldsymbol{X}^T\gamma + \theta_i Rd_j + \varepsilon_{ij}$$
*Budget share equals intercept plus log expenditure, controls, and remittance dummy.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| OFW | Overseas Filipino Worker — Filipino working abroad. |
| Remittance | Money sent by migrants to their home country household. |
| SOF | Survey on Overseas Filipinos — annual PSA household survey of OFW families. |
| FIES | Family Income and Expenditure Survey — triennial national survey of household spending. |
| PSM | Propensity Score Matching — statistical technique to estimate treatment effects by matching similar households. |
| GMM | Generalized Method of Moments — panel estimation method that handles endogeneity using lagged variables. |
| GRDP | Gross Regional Domestic Product — regional economic output measure. |
| Binding financial constraint | Situation where a household cannot reallocate spending beyond essentials because income is too low. |

## Critical Citations

- [Rosenzweig & Stark, 1989] — Foundational consumption-smoothing motive for remittances.
- [Docquier & Rapoport, 2006] — Theoretical framework linking remittance motives (altruism, exchange, investment) to migrant return intentions.
- [Tuaño-Amador et al., 2022] — Philippine-specific evidence on remittance resilience during COVID-19, used as baseline.

## Relevance to Odin

**Topics:**

A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

G.1 — Expense Categorization in Filipino Personal Finance Contexts

**Contribution to Odin:**

This paper directly informs Odin's user profiling (F.1) by demonstrating that income status (poor vs non-poor) fundamentally changes how additional funds are allocated — poor households cannot shift from food to education/health even when receiving remittances. This finding justifies a design priority for Odin's budget recommendation module: the algorithm must account for binding financial constraints and not assume fungibility for users with low discretionary income. The paper also provides empirical budget shares for FIES-aligned spending categories (food, education, health, housing, durable goods, clothing), which validates Odin's choice of FIES/BSP as the categorization grounding (G.1). Finally, the observed heterogeneity in saving/investing behavior by migrant status and education level supports Odin's need for behavior-driven profile classification rather than static demographic rules.

**Directly justifies:**

- "Poor Filipino households exhibit binding financial constraints: remittance receipts do not increase education or health spending shares, while non-poor households show significant increases of 0.40–0.50 percentage points."
- "50% of OFW households allocate nothing to savings, and 75% allocate nothing to investments — immediate consumption dominates, with over 90% of cash remittances spent directly."
- "Higher regional unemployment rates increase remittance inflows (altruistic motive), while higher regional wages reduce them — indicating that household financial vulnerability drives remittance dependence."
- "OFWs save more than immigrants (10.35% vs 7.40%), supporting the exchange motive: migrants intending to return remit more for future liquidity."

**Limits of relevance:**

- Study focuses on remittance-receiving OFW households, not the general population of Filipino young professionals (age 20–40 non-migrant workers).
- No ML or algorithmic methods — findings are behavioral/economic, not directly applicable to algorithm selection for forecasting or anomaly detection.
- Spending data is cross-sectional (FIES 2018/2021), not time-series, limiting claims about dynamic budgeting behavior.
- Remittance context differs from earned income — Odin users rely on salary/wages, not external transfers, which may change spending elasticity.

## Limitations

- Generalizability limited to remittance-receiving households; findings may not apply to non-migrant Filipino young professionals. [unacknowledged]
- Endogeneity concerns in consumption regressions remain despite PSM; no strong instrumental variable for remittance receipt is available.
- SOF lacks itemized consumption categories beyond broad allocation (saving/investing/consumption), forcing reliance on FIES for granular spending.
- Panel GMM uses regional aggregates, masking within-region heterogeneity in remittance motives and spending responses.
- Transfer cost data limited to bank telegraphic transfers; informal channels (e.g., door-to-door) not covered, potentially underestimating true costs.

## Remember This

- 🔑 **50% save nothing, 75% invest nothing** — immediate consumption dominates OFW household behavior.
- 💡 Poor households cannot shift remittances to education or health — financial constraints are binding, not a preference issue.
- 📌 Transfer fees cut remittances by ~12-13% — high costs directly reduce funds available for household spending.
- 🧠 OFWs save more than immigrants — return intention changes remittance allocation, a key profiling dimension for Odin.
