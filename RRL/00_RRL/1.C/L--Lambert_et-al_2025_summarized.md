# RELATIONSHIP BETWEEN FAMILY RESOURCES, FINANCIAL STRESS, WITH FINANCIAL MANAGEMENT AMONG FILIPINO MILLENNIALS

## Metadata

```yaml
---
paper_id: "15c5c9d0-7b3a-5b3c-9e2a-1f4b6d8e9a0c"
designation: international
title: "RELATIONSHIP BETWEEN FAMILY RESOURCES, FINANCIAL STRESS, WITH FINANCIAL MANAGEMENT AMONG FILIPINO MILLENNIALS"
authors: "Lambert, M.; Jusoh, Z.; Zainudin, N."
year: 2025
venue: "Journal Pengguna Malaysia"
odin_topics: ["1.A", "1.C", "2.A", "5.A"]
shorthand_tags: ["/fin-problem-prevalence", "/budgeting-prevalence", "/family-obligations", "/profiling-role", "/fil-profile-construction", "/profile-dimensions"]
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

Financial stress strongly harms financial management among Filipino millennials (β = -0.724), while millennial traits like tech-savviness and adaptability improve it (β = 0.480).

## Problem and Motivation

Financial well-being among Filipinos is low despite economic growth, with 52% struggling and 30% suffering financially, yet millennial-specific factors remain underexplored. Understanding how family resources and financial stress interact to shape financial management is critical for designing effective interventions. No prior study has simultaneously examined financial stress and millennial characteristics as direct predictors of financial management in the Philippine context.

## Approach

- Multistage random sampling of 400 Filipino millennials (aged 20-40) from Eastern Visayas (Tacloban, Ormoc, Baybay).
- Self-administered online questionnaire using validated scales: Pew Millennial Survey (29 items), Frufonga’s financial stress checklist (14 items), and Rajnah’s financial management instrument (26 items).
- Structural Equation Modelling (SEM) used to test direct relationships between independent variables (financial stress, millennial characteristics) and dependent variable (financial management).
- Model fit and path coefficients assessed with bootstrapping (95% CI, p < .001 threshold).
- Demographics: 51.5% male, majority college graduates (25.3%), 41.5% aged 26-35, 60.8% earn Php 10,001-30,000/month.

## Findings

1. Financial stress has a **strong negative effect** on financial management (β = -0.724, p < .001) — one-unit increase in stress reduces management by 0.726 units.
2. Millennial characteristics have a **positive effect** on financial management (β = 0.480, p < .001) — traits like adaptability, digital literacy, and collaboration improve practices.
3. Respondents reported high millennial trait scores (mean 4.80/5 for optimism, 4.81/5 for tech-savvy) but low financial stress (mean 2.23/5), indicating resilience despite challenges.
- Only 25% of adult Filipinos understand basic financial concepts (World Bank), highlighting a literacy gap.
- Financial stress undermines cash management, credit management, and retirement planning; millennials under low stress demonstrate proactive budgeting and emergency funds.

## Key Figures and Tables

- Table 5: Structural model for millennial characteristics → β = 0.480, T = 13.806, p < .001 — positive, robust.
- Table 6: Structural model for financial stress → β = -0.724, T = -27.581, p < .001 — negative, very strong.
- Table 2: Millennial characteristics sub-scores (optimistic 4.80, family-oriented 4.48, tech-savvy 4.81) → all high (4+ out of 5).
- Table 3: Financial stress overall mean = 2.23/5 → relatively low stress in this sample.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| SEM | Structural Equation Modelling — a statistical method to test causal relationships between observed and latent variables. |
| β (beta) | Standardized regression coefficient — shows the strength and direction of an effect (range -1 to +1). |
| Millennial characteristics | Traits measured: optimism, achievement focus, family orientation, tech-savviness (from Pew Research). |
| Financial management | Practices including budgeting, saving, bill payment, credit use, and emergency fund planning. |

## Critical Citations

- [Dollahite, 1991] — ABCD-XYZ Resource Management Model integrates stress and resource theories; provides the conceptual framework.
- [Delafrooz & Paim, 2011] — Established negative relationship between financial stress and financial wellness; directly supports the stress→management path.
- [Pew Research Centre, 2021] — Documents millennial financial concerns (debt, housing, job stability); used to justify trait measurement.

## Relevance to Odin

**Topics:**

1.A — Filipino Young Professionals as a Demographic

1.C — Financial Behavior of Filipino Young Professionals

2.A — Culturally Specific Financial Practices

5.A — Financial Behavioral Profiles in Personal Finance

**Contribution to Odin:**

This paper directly validates that financial stress is a powerful negative predictor of financial management among Filipino millennials, and that generational traits (digital literacy, adaptability) are positive predictors. For Odin, this justifies building a stress-aware behavioral profile that can detect when users are under financial pressure and adjust recommendations or alerts accordingly. The finding that millennial traits like tech-savviness enhance management supports Odin’s mobile-first, digital-native interface design as a leverage point. Additionally, the paper’s documentation of low financial literacy (25%) in the Philippines reinforces Odin’s need for transparent, educational budget recommendations rather than opaque ML outputs.

**Directly justifies:**

- “Financial stress reduces financial management practices by 0.724 standard deviations among Filipino millennials (β = -0.724, p < .001), warranting stress-detection features in personal finance systems.”
- “Millennial characteristics such as digital literacy and adaptability improve financial management (β = 0.480), supporting a mobile-first, tech-optimized interface for this demographic.”
- “Only 25% of adult Filipinos understand basic financial concepts, underscoring the need for interpretable, educational budget recommendations rather than purely algorithmic outputs.”
- “Filipino millennials report high family orientation (mean 4.48/5), which may create financial obligations that increase stress — Odin’s category structure must include family remittance and support expenses.”

**Limits of relevance:**

- Sample limited to Eastern Visayas (provincial cities); Metro Manila young professionals may have different income and stress profiles.
- Cross-sectional design; causal direction not established (stress could result from poor management as well as cause it).
- Financial management was self-reported, not observed behavior; Odin uses actual transaction data.
- Millennial characteristics measured as fixed traits; Odin profiles must be dynamic as behavior changes.

## Limitations

- Sample not representative of all Filipino millennials (only three cities in Eastern Visayas); generalizability to Metro Manila is untested. [unacknowledged]
- Cross-sectional design prevents causal inference; the negative relationship could be bidirectional.
- Self-report bias in financial management and stress measures; social desirability may inflate reported good practices.
- No objective financial data (e.g., bank records) to validate self-reported management behaviors.
- The study did not control for income level in the SEM model, though income likely moderates the stress–management relationship. [unacknowledged]

## Remember This

- 🔑 **β = -0.724** — financial stress is the dominant negative force on management; stronger than positive traits.
- 📌 Millennial traits add +0.480 — digital literacy and adaptability are assets Odin should amplify.
- 💡 Only 25% of Filipinos are financially literate — Odin’s UI must teach, not just predict.
- ⚠️ Sample is rural/provincial — Metro Manila dynamics (higher rent, different obligations) may differ.
