# Effects of Filipino Consumers’ Financial Attitudes, Subjective Norms, and Perceived Behavioral Control on Intentions to Formal Banking: Towards Financial Inclusion

## Metadata

```yaml
---
paper_id: "3c0f7e2a-1b4d-5e9f-0a1b-2c3d4e5f6a7b"
designation: local
title: "Effects of Filipino Consumers’ Financial Attitudes, Subjective Norms, and Perceived Behavioral Control on Intentions to Formal Banking: Towards Financial Inclusion"
authors: "Co, M.; Centeno, D.D.G."
year: 2023
venue: "Philippine Management Review"
odin_topics: ["A.1", "F.1"]
shorthand_tags: ["/income-type-behavior-diff", "/fil-behavioral-patterns"]
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

Subjective norms (having a banked household member) and perceived behavioral control significantly predict unbanked Filipinos’ intention to save surplus money in formal banks, but attitudes do not.

## Problem and Motivation

Financial exclusion in the Philippines is often attributed to cost and lack of funds, but psychological factors on the demand side remain underexplored. Understanding attitudes, social influences, and perceived behavioral control can inform financial inclusion strategies. No prior local study had quantitatively linked these theory of planned behavior (TPB) factors to banking intentions using a nationwide survey.

## Approach

- Data: 2014 BSP Consumer Finance Survey (CFS) of 15,503 Filipino households nationwide.
- Dependent variable: Intention to put surplus money in a bank deposit account.
- Independent variables: Attitudes (liking to save in bank), subjective norm (another household member has bank account), perceived behavioral control (two items: "don't earn enough to save regularly" and "don't save enough for the future" reversed).
- Demographics: Education, gender, age (millennial/Gen X/baby boomer), income (low/middle/high), employment, pension membership, household size.
- Method: Logistic regression with marginal effects.

## Findings

1. Subjective norm (banked household member) increased banking intention probability by **10.16%** (p < 0.001) — strongest effect.
2. Perceived control ("earn enough to save regularly") increased intention by 1.42% (p = 0.024).
3. Perceived control ("don't save enough for the future") reversed: agreeing with "don't save enough" increased intention (negative coefficient on reversed scale).

- Attitude toward banking was not significant.
- College graduates had 7.95% higher probability of intention than non-graduates (p < 0.001).
- Males were 2.02% more likely than females (p = 0.030).
- Baby boomers were 2.8% less likely than millennials (p = 0.036).
- Middle-income: +3.18% vs low-income (p = 0.002); high-income: -10.14% vs low-income (p = 0.004).
- Unemployed respondents had higher intention (+1.97%) than employed (p = 0.029).
- Pension members: +8.06% (p < 0.001).

## Key Figures and Tables

- Table 3: Logistic regression results → subjective norm (β=0.4397) and college education (β=0.3344) are strongest positive drivers.
- Table 4: Marginal effects (dy/dx) → subjective norm adds 10.17% probability, college adds 7.95%.

## Key Equations

$$Logit(P(Banki=1)) = \alpha + \beta_1 X_1 + \beta_2 X_2 + ... + \beta_k X_k$$
*Logistic model predicting probability of banking intention from attitudes, norms, control, and demographics.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| TPB | Theory of Planned Behavior — psychological model where attitudes, social norms, and perceived control predict intentions. |
| Perceived behavioral control | One's belief about how easy or hard it is to perform a behavior (e.g., saving money). |
| Subjective norm | Perceived social pressure to perform or not perform a behavior. |
| CFS | Consumer Finance Survey — BSP's nationwide household finance survey. |
| BSP | Bangko Sentral ng Pilipinas (Philippine central bank). |

## Critical Citations

- [Ajzen, 1991] — Foundational TPB paper establishing attitude, subjective norm, and perceived control as predictors of intention.
- [BSP, 2014] — Source of the CFS dataset used in the study.

## Relevance to Odin

**Topics:**

A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

**Contribution to Odin:**

This paper directly informs Odin's user profiling module (F.1) by identifying specific psychological and demographic factors that predict financial behavior intentions among Filipinos. The finding that subjective norm (household member with a bank account) has the largest marginal effect (10.16%) suggests that Odin's profiling should consider social influence and household financial context, not just individual attributes. Additionally, the significant effects of income typology (middle-income individuals more likely to intend banking, high-income less likely) and age (millennials more likely than baby boomers) provide empirical grounding for Odin's demographic-based behavioral segmentation. Although the paper targets banking inclusion rather than budget management, the behavioral mechanisms — perceived control over saving, social norms, and education — are directly transferable to understanding why Filipino young professionals might adopt or reject a personal budget management system.

**Directly justifies:**

- "Having a banked household member increases an unbanked Filipino's intention to save surplus money in a formal bank by 10.16 percentage points (p<0.001), demonstrating the strong effect of social proximity on financial behavior intentions."
- "College-educated Filipinos are 7.95% more likely to intend formal banking than non-graduates, indicating educational attainment as a key segmentation variable for financial behavior change."
- "Middle-income Filipinos show 3.18% higher banking intention than low-income, but high-income individuals show 10.14% lower intention, suggesting that income's effect on financial intentions is non-linear."
- "Millennials (aged 14–32 in 2014) have significantly higher banking intentions than baby boomers (2.8% higher probability), supporting age-based targeting for financial products."
- "Perceived behavioral control — specifically believing one earns enough to save — increases banking intention by 1.42%, highlighting self-efficacy as a modifiable psychological lever."

**Limits of relevance:**

- The study measures intention to save in banks, not intention to use a budget management app; transfer requires analogy but the psychological constructs are similar.
- Data from 2014 may not reflect current digital finance behaviors post-pandemic (e.g., GCash, Maya adoption).
- Sample includes all Filipino adults, not specifically young professionals aged 20–40; however, millennials (14–32 in 2014) overlap with Odin's target age range.
- Attitude toward banking was not significant, which contradicts some TPB findings; caution needed when extrapolating to attitudes toward budgeting apps.
- No explicit measure of spending or budgeting behavior; only surplus saving intention.

## Limitations

- Cross-sectional data cannot establish causality between psychological factors and intentions.
- Attitudes measured by a single Likert item ("I like to save using a banking institution") may lack reliability; the non-significant finding may be due to measurement error. [unacknowledged]
- Data from 2014 predates widespread digital wallet adoption in the Philippines; financial behavior may have shifted.
- No validation of TPB constructs using established multi-item scales; relies on proxy items from CFS.
- Low pseudo R² (0.0094) indicates the model explains very little variance in banking intention — many unmeasured factors.

## Remember This

- 🔑 Subjective norm (banked household member) boosts banking intention by **10.16%** — strongest predictor.
- 📌 Only 12.4% of Filipinos had a bank account in 2014; 41.2% intended to save surplus in banks.
- 💡 College grads are 7.95% more likely to intend banking — education matters for financial behavior.
- ⚠️ Attitudes toward banking were NOT significant — liking banks doesn't predict intention.
- 🧠 Perceived control over earning enough to save increases intention by 1.42% per scale point.
