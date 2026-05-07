# Effects of Filipino Consumers' Financial Attitudes, Subjective Norms, and Perceived Behavioral Control on Intentions to Formal Banking: Towards Financial Inclusion

> NOTE: Flagged for obsolescence; data derived from 2014 survey.

```yaml
---
name: paper-summary
paper_id: "f47ac10b-58cc-4372-a567-0e02b2c3d479"
source_document: "Co_Centeno.md"
designation: local
title: "Effects of Filipino Consumers' Financial Attitudes, Subjective Norms, and Perceived Behavioral Control on Intentions to Formal Banking: Towards Financial Inclusion"
authors: "Co, M.; Centeno, D."
year: 2023
venue: "Philippine Management Review"
odin_topics: [1, 9]
shorthand_tags: ["/income-typology", "/budget-failure-points", "/profiling-role", "/western-taxonomy-gap", "/fil-behavioral-patterns", "/fil-profile-construction", "/profile-dimensions"]
summary_date: 2026-05-04
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
```

## TL;DR

Subjective norms and perceived behavioral control, but not attitudes, significantly predict unbanked Filipinos' intention to save surplus money in banks.

## Problem and Motivation

Financial exclusion in the Philippines is usually explained by cost or lack of funds, ignoring psychological drivers. No prior local study measured how attitudes, social pressure, and perceived control affect formal banking intentions. Understanding these demand‑side factors is critical for effective financial inclusion policy.

## Approach

- **Data**: BSP Consumer Finance Survey 2014, 15,503 nationally representative households.
- **Dependent variable**: Intention to deposit surplus money in a bank (binary).
- **Independent variables**: Attitude toward banks (Likert), subjective norm (household member with bank account), two perceived‑control items (“don’t earn enough”, “not saving enough”), plus demographics.
- **Method**: Logistic regression with average marginal effects (AME).

## Findings

1. **Subjective norm** (co‑household bank account) increases intention by **10.16%** in marginal probability (p < 0.001).
2. **Perceived control 1** (“I earn enough to save regularly”) raises intention (AME +1.42%, p = 0.024).
3. **Perceived control 2** (“I don’t save enough for the future”) *lowers* intention (AME -2.54%, p < 0.001).
4. **Attitude toward banks is not significant** (p = 0.369).
5. Higher education (high school or college), male gender, middle income (vs. low), being unemployed, and having a pension all significantly increase banking intention.
6. Baby boomers have lower intention than millennials (p = 0.036). High income also lowers intention vs. low income (p = 0.009).

## Key Figures and Tables

- **Table 3**: Logistic regression coefficients → subjective norm (β=0.44) and both control items significant; attitude not significant.
- **Table 4**: Average marginal effects → family member with bank account gives the largest positive effect (+10.16%).
- **Figure 1**: Conceptual framework (Theory of Planned Behavior) → no data, but illustrates attitude, subjective norm, and PBC → intention → behavior.

## Key Equations

$$
Logit[P(Bank=1)] = a + \beta_1X_1 + \beta_2X_2 + \ldots + \beta_kX_k
$$
*Logistic regression models the log‑odds of intending to use a bank for surplus money.*

## Definitions

| Term / Acronym | Plain‑English Definition |
| -------------- | ------------------------ |
| TPB | Theory of Planned Behavior – behavior is predicted by intention, which is shaped by attitudes, subjective norms, and perceived behavioral control. |
| Perceived Behavioral Control (PBC) | One’s belief about how easy or hard it is to perform a behavior (e.g., saving regularly). |
| AME | Average Marginal Effect – percentage‑point change in probability when an independent variable increases by one unit. |
| BSP | Bangko Sentral ng Pilipinas – Philippine central bank. |

## Critical Citations

- [Ajzen, 1991] – Foundational TPB paper; the entire model is built on it.  
- [BSP, 2014] – Source of the Consumer Finance Survey data.  
- [Rutherford & DeVaney, 2009] – Earlier TPB application to credit card behavior, cited as a Western benchmark.

## Relevance to Odin

**Topics:**  

1 – Spending and Budgeting Behavior of Filipino Young Professionals

9 – User Behavioral Profiling in Filipino Personal Finance Contexts  

**Contribution to Odin:**  

This paper provides the first large‑scale empirical profiling of Filipino financial behavior using psychological constructs (attitudes, social norms, perceived control). It shows that **social influence from family** and **perceived ability to save** dominate over positive attitudes in driving banking intentions. These patterns directly inform Odin’s user behavioral profiling module and highlight that Filipino users may respond more to social‑norm cues and “control‑enabling” features than to mere positive messaging.

**Directly justifies:**  

- “Perceived behavioral control (e.g., ‘I don’t earn enough to save regularly’) is a stronger predictor of saving intentions than general attitudes toward banking among Filipinos.”  
- “Having a household member with a bank account increases an unbanked individual’s intention to save by 10 percentage points, demonstrating the critical role of family social norms.”  
- “Demographic profiling (income, education, gender, age, employment, pension membership) significantly differentiates banking intention, supporting segmented behavioral models.”

**Limits of relevance:**  

- Data from 2014 – pre‑digital finance boom and pre‑pandemic; may not fully reflect current mobile‑first behaviors.  
- Focuses on formal bank deposit intention, not spending or budgeting behavior per se.  
- Does not test any algorithm (logistic regression is explanatory, not a predictive system deployed in Odin).

## Limitations

- Cross‑sectional design – cannot establish causality, only association.  
- Self‑reported intentions, not actual banking behavior.  
- Older data (2014) – financial inclusion and digital payments have evolved significantly.  
- Low pseudo‑R² (0.0094) suggests many unmeasured factors influence banking intention.

## Remember This

- 🔑 **Family bank account = +10% intention** – strongest effect by far.  
- ⚠️ **Attitude didn’t matter** (p = 0.369) – don’t assume liking banks leads to action.  
- 💡 **“Earn enough” helps, “save enough” hurts** – framing matters for control beliefs.
