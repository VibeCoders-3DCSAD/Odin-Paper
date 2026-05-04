# Do Remittances Boost Household Spending: New Evidence from Migrants' Household Survey

```yaml
---
name: paper-summary
paper_id: "10.1016/j.latcb.2025.100196"
source_document: "Bayangos_Lubangco.md"
designation: local
title: "Do Remittances Boost Household Spending: New Evidence from Migrants' Household Survey"
authors: "Bayangos, V. B.; Lubangco, C. K."
year: 2024
venue: "BSP Discussion Paper"
odin_topics: []
shorthand_tags: []
summary_date: 2026-05-04
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
```

## TL;DR

Remittances increase non‑food spending, but binding financial constraints limit welfare gains for poorer Filipino households.

## Problem and Motivation

Existing literature confirms a positive link between remittances and consumption but lacks a nuanced understanding of how remittances reshape spending across income groups and what macroeconomic factors drive remittance flows. The Philippines, a top remittance recipient, needs evidence to optimize the developmental impact of these flows, especially given declining remittance growth and persistent household reliance on them.

## Approach

- **Data sources**: Survey on Overseas Filipinos (SOF, 2007–2022) and Family Income and Expenditure Survey (FIES, 2018 & 2021) — both nationally representative.
- **Household spending analysis**: Logistic regressions (odds ratios) for saving/investing behavior; propensity score matching (PSM) with Working‑Leser model to estimate average treatment effects on consumption shares.
- **Remittance driver analysis**: Two‑step system panel GMM on regional panel (17 regions, 2007–2022), including GRDP per capita, OFW count, wages, unemployment, exchange rate, and telegraphic transfer fees.
- **Financial cost survey**: Annual survey (2015–2023) of 44 banks and 15 non‑banks for remittance transfer costs.

## Findings

1. Average saving rate from remittances is **9.9%** (2008–2022); investing rate is 7–8%. Over 75% of OFW households allocate **no** remittances to investments.
2. Remittance‑receiving households shift from food to non‑food spending, but shifts are **smaller for poor households**: e.g., education share increases 0.4% (non‑poor) vs. 0.02% (poor, not significant).
3. Higher unemployment and peso depreciation **increase** remittance receipts (altruistic motive), while higher regional wages and transfer fees **reduce** receipts.
4. A **1‑percentage‑point** rise in telegraphic transfer fees (as % of average remittance) reduces cash remittances by **12–15%** (significant at p<0.01).
5. Financial development (bank deposit liabilities) positively affects remittances, but only for cash remittances, not personal remittances.

## Key Figures and Tables

- **Figure 4**: Saving vs. investing rates over time → Savings peaked at 13.1% in 2009; investing briefly surpassed savings in 2021 (10.6%).
- **Table 3**: PSM average treatment effects → Non‑poor remittance households increase education share by +0.4% and health share by +0.5%.
- **Table 5**: Panel GMM results → Transfer fees coefficients: −12.46 to −15.16 (p<0.05), exchange rate coefficients: +0.018 to +0.022 (p<0.05).

## Key Equations

$$Y_{ij} = \beta_0 + \beta_1\ln \text{cons}_j + X^T\gamma + \theta_iR_{dj} + \epsilon_{ij}$$
*Budget share model: remittance receipt as a dummy, controlling for total expenditure and household covariates.*

$$\text{Remit}_{it} = \beta_1 + \beta_2\text{Remit}_{it-1} + \beta_3\text{GRDPpc}_{it} + \beta_4\text{OFW}_{it} + \beta_5\text{wage}_{it} + \beta_6\pi_{it} + \beta_7\text{unemployment}_{it} + \beta_8\text{forex}_t + \beta_9\text{cost}_t + \epsilon_{it}$$
*Dynamic panel model for remittance determinants, estimated with system GMM.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| OFW | Overseas Filipino Worker — a Filipino working abroad. |
| SOF | Survey on Overseas Filipinos — annual PSA survey of migrant households. |
| FIES | Family Income and Expenditure Survey — triennial PSA survey on household income/spending. |
| GRDP | Gross Regional Domestic Product — regional economic output. |
| GMM | Generalized Method of Moments — econometric technique for dynamic panel data. |
| PSM | Propensity Score Matching — matches treated and control units to estimate causal effects. |
| Telegraphic transfer fee | Fee for sending remittances via bank wire transfer (includes intermediary charges). |
| PhilPaSSplus | Philippine Peso Real‑Time Gross Settlement system (low‑risk large‑value transfers). |

## Critical Citations

- [Docquier & Rapoport, 2006] — Theoretical framework linking return migration propensity to saving/investment remittances.
- [Randazzo & Piracha, 2019] — PSM approach for remittance consumption effects (methodological template).
- [Tuaño‑Amador et al., 2022] — Resilience of Philippine remittances during COVID‑19 and policy responses.

## Relevance to Odin

**Topics:**

None — contextual only.

**Contribution to Odin:**

This paper does not address personal finance systems, budgeting algorithms, user profiling, or mobile‑first design. It is a macroeconomic and household‑level study of remittance effects on consumption. It offers no direct justification for Odin’s algorithmic choices (LSTM, isolation forest, classification, recommendation) or user‑facing features. The spending behavior findings (e.g., binding financial constraints, altruistic vs. investment motives) are not specific to young Filipino professionals or PFMS design.

**Directly justifies:**

- None applicable to Odin’s system design or RRL arguments.

**Limits of relevance:**

- Domain is international migration and development economics, not personal finance software.
- Unit of analysis is households (often older, rural) — not young professionals.
- No machine learning, anomaly detection, or predictive modeling components.

## Limitations

- Self‑reported survey data (SOF and FIES) subject to recall and social desirability bias.
- PSM addresses selection on observables but cannot eliminate unobserved confounding.
- Panel GMM relies on lagged instruments; weak instrument issues possible despite Sargan/Hansen tests.
- Telegraphic transfer fee data limited to banks; informal remittance channels (e.g., door‑to‑door) not included in cost analysis.

## Remember This

- 🔑 **9.9% average saving rate** from remittances; 75% of households invest nothing.
- 💡 Poor households do **not** increase education spending from remittances — financial constraints bind.
- 📌 Transfer fees cut remittances by **12–15%** — cost reduction is high‑leverage policy.
