# The Mediation of Financial Behavior to Financial Literacy and Spending Habits of Gen Z: An Exploratory Factor Analysis

## Metadata

```yaml
---
paper_id: "10.20944/preprints202409.1696.v1"
designation: local
title: "The Mediation of Financial Behavior to Financial Literacy and Spending Habits of Gen Z: An Exploratory Factor Analysis"
authors: "Rodriguez, J. M. P.; Labong, M. D. C. G.; Palallos, L. Q."
year: 2024
venue: "Preprints.org"
odin_topics: ["1.A", "1.C", "5.A"]
shorthand_tags: ["/literacy-behavior-gap", "/budgeting-prevalence", "/profiling-role"]
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

Financial behavior mediates the link between financial literacy and spending habits in Gen Z, with literacy directly influencing spending (coefficient 1.167) and indirectly through behavior (coefficient 0.797).

## Problem and Motivation

The relationship between financial literacy and actual spending remains poorly understood, particularly whether financial behavior acts as a mediator. This gap matters because Gen Z faces rising costs and digital financial access, yet few studies examine how literacy translates into spending through behavior. Before this work, no study had explicitly tested the mediating role of financial behavior between literacy and spending habits for this demographic.

## Approach

- Sample: 317 Gen Z respondents aged 18–25 from four barangays in Quezon City, Philippines, via stratified random sampling.
- Instruments: Structured questionnaire measuring financial literacy, financial behavior, and spending habits using validated Likert-scale items.
- Analysis sequence: Pearson correlation, regression, mediation analysis, and Structural Equation Modeling (SEM).
- Factor analysis: Exploratory Factor Analysis (EFA) followed by Confirmatory Factor Analysis (CFA) to validate construct measurement.
- Mediation test: Indirect effects computed with bootstrapped confidence intervals (95% CI).

## Findings

1. Financial literacy and spending habits have a **strong positive correlation (r = 0.821, p < .001)**.
2. Direct effect of financial literacy on spending is **1.167** (unstandardized coefficient from SEM).
3. Financial behavior exerts a mediation effect of **0.797** on the literacy→spending relationship (behavior→spending path).
4. Financial literacy explains 51.9% of variance in financial behavior (R² = 0.519, F = 340.48, p < .001).
5. Construct reliability: financial behavior (Cronbach’s α = 0.75), spending (α = 0.68), literacy (α = 0.66).

- The indirect effect through behavior was significant (estimate 0.180, 95% CI [0.114, 0.245]).

## Key Figures and Tables

- Table 1: Pearson correlation (r = 0.821) → strong positive relationship between literacy and spending.
- Table 5: Path coefficients → FL→Spending (0.642), FL→Behavior (0.721), Behavior→Spending (0.249).
- Figure 2: Path plot analysis → visual confirmation of significant direct and mediated paths.
- Table 13: SEM results → FL→Spending (1.1666), FL→Behavior (0.7639), Behavior→Spending (0.7971).
- Figure 4: Structural Equation Model diagram → full model with standardized coefficients.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Financial literacy | Knowledge and understanding of financial concepts needed to make informed decisions. |
| Financial behavior | Actions and practices such as budgeting, saving, and spending management. |
| Spending habits | Recurring patterns of expenditure, including impulse vs. planned purchases. |
| Gen Z | Generation born approximately 1997–2012; in this study, ages 18–25. |
| EFA | Exploratory Factor Analysis [finds underlying structure without pre-specifying factors]. |
| CFA | Confirmatory Factor Analysis [tests whether measured items represent intended latent constructs]. |
| SEM | Structural Equation Modeling [combines factor analysis and path analysis to test causal models]. |
| AVE | Average Variance Extracted [measure of convergent validity; values near 0.5 indicate acceptable validity]. |

## Critical Citations

- [Shan et al., 2023] — Establishes that financial literacy helps Gen Z set goals and avoid poor spending habits.
- [Rodriguez et al., 2024] — Prior finding that higher financial literacy correlates with more spending behavior.
- [Anjani & Darto, 2023] — Shows literacy combines with self-control to influence financial management behavior.

## Relevance to Odin

**Topics:**

1.A — Filipino Young Professionals as a Demographic

1.C — Financial Behavior of Filipino Young Professionals

5.A — Financial Behavioral Profiles in Personal Finance

**Contribution to Odin:**

This paper directly supports Odin’s behavioral profiling module by demonstrating that financial behavior is not merely an outcome of literacy but a necessary mediator that transforms knowledge into spending action. For Odin, which targets Filipino young professionals, the finding that literacy alone explains only 52% of behavior variance means the system must actively measure and shape behavior through features like transaction logging and budget adherence tracking. The mediation evidence justifies why Odin should prioritize behavioral interventions (e.g., alerts, reminders) over pure financial education content. Even though the sample is Gen Z (18–25) rather than the full 20–40 range, the mechanism likely extends upward, and the methodological use of SEM provides a template for validating Odin’s own latent constructs.

**Directly justifies:**

- "Financial behavior mediates the relationship between financial literacy and spending habits, with a significant indirect effect (estimate = 0.180, 95% CI [0.114, 0.245])."
- "Financial literacy explains 51.9% of the variance in financial behavior, indicating that nearly half of behavioral variation is driven by other factors such as self-control and social influences."
- "The path from financial behavior to spending (coefficient = 0.797 in SEM) is comparable in magnitude to the direct literacy→spending path (1.167), making behavior a necessary target for intervention."
- "Reliability of financial behavior as a latent construct (Cronbach’s α = 0.75) supports its operationalization in a Philippine young adult sample."

**Limits of relevance:**

- Sample restricted to 18–25 year olds in Quezon City; may not fully represent young professionals aged 26–40 or other regions of the Philippines.
- No longitudinal data; causal direction claimed (literacy → behavior → spending) relies on cross-sectional SEM assumptions.
- Preprint not peer-reviewed; findings should be triangulated with published studies.
- Relies on self-reported spending, which may suffer from recall and social desirability bias.

## Limitations

- Cross-sectional design prevents establishing true causality despite SEM assumptions. [unacknowledged]
- Sample limited to four barangays in Quezon City, limiting generalizability to other Philippine urban or rural areas.
- Low convergent validity for spending (AVE = 0.415) and literacy (AVE = 0.404) — constructs may not be fully captured by indicators.
- No control for income level or personality traits, which the literature suggests also influence financial behavior.
- The study does not address digital financial behavior (e.g., e-wallet spending), which is highly relevant to Odin’s mobile-first context. [unacknowledged]

## Remember This

- 🔑 **r = 0.821** — financial literacy and spending are strongly correlated; knowledge doesn't suppress spending.
- 📌 Indirect effect = **0.180** — financial behavior is a significant but partial mediator (p < .001).
- 💡 Literacy explains **51.9%** of behavior variance — almost half the story is missing (self-control, social factors).
- ⚠️ AVE for literacy (0.404) below 0.5 — measure may need refinement for Philippine young adults.
- 🧠 Behavior→spending path = **0.797** — changing spending requires changing behavior, not just teaching facts.
