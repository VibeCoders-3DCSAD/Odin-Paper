# Assessing the Financial Literacy of Senior High School and College Students: A Comprehensive Analysis

## Metadata

```yaml
---
paper_id: "b3c7d9f1-2a4e-6c8a-9d2f-1e3b5c7d9f1a"
designation: local
title: "Assessing the Financial Literacy of Senior High School and College Students: A Comprehensive Analysis"
authors: "Dela Rama, K. A.; Baylon, F.; Balwet, L. F.; Pullos, K. E.; Durias, R. C.; Cabusca, J. F.; Eguia, A. L.; Cabilin, L. M.; Duran, R.; Mante, J.; Prepecio, D.; Gilongos, C. J.; Rosel, M."
year: 2024
venue: "The Threshold"
odin_topics: ["1.C"]
shorthand_tags: ["/budgeting-prevalence", "/budget-failure-points"]
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

Filipino senior high and college students have basic financial knowledge (mean ~2.1/4) but large gaps in compound interest understanding and consistent budgeting, with no gender differences.

## Problem and Motivation

Financial literacy among young Filipinos is understudied, especially at the transition from school to independent financial management. Poor financial decisions lead to high debt and low savings, undermining long-term economic stability. Prior research focused on adults, leaving a gap in understanding students’ formative financial skills and behaviors.

## Approach

- Sample: 345 students (SHS and college) at Colegio de San Francisco Javier, stratified random sampling by year and program.
- Instrument: 4-point Likert scale survey adapted from OECD/INFE, measuring financial knowledge and behavior (savings, budgeting, borrowing).
- Reliability: Pilot study (n=30) gave Cronbach’s alpha = 0.85.
- Analysis: Descriptive statistics, Welch’s t-test (for group comparisons), Pearson correlation, all computed in Python.
- Baseline: No experimental control; compared SHS vs. college and male vs. female.

## Findings

1. Financial knowledge weighted mean: SHS = 2.10, College = 2.11 (basic understanding, scale 1–4).
2. Financial behavior weighted mean: SHS = 1.92, College = 1.85 (moderate proficiency).
3. **Less than 30% of students could correctly explain compound interest** or calculate APY.

- Students report inconsistent budgeting practices and difficulty sticking to budgets when unexpected expenses arise.
- No significant gender differences in any financial literacy dimension (Welch’s t-test, p > 0.05).

## Key Figures and Tables

None.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Financial literacy | Ability to understand and use financial skills like budgeting, saving, and investing. |
| Compound interest | Interest earned on both the original money and previously earned interest. |
| APY | Annual Percentage Yield — the real rate of return accounting for compounding. |
| Likert scale | A rating scale (e.g., strongly agree to strongly disagree) used to measure attitudes. |
| Cronbach’s alpha | A statistic that measures how consistently survey questions measure the same thing. |
| Welch’s t-test | A statistical test that compares two group means without assuming equal variances. |

## Critical Citations

- [Lusardi & Mitchell, 2014] — Foundational evidence that financial literacy predicts economic well-being.
- [OECD, 2016] — Establishes framework for measuring youth financial literacy in schools.
- [Briones, 2021] — Documents low financial literacy levels and economic inequality in the Philippines.

## Relevance to Odin

**Topics:**

1.C — Financial Behavior of Filipino Young Professionals

**Contribution to Odin:**

This paper provides empirical baseline data on financial behavior gaps among young Filipinos, directly informing Odin’s UX and feature design. The finding that students struggle with compound interest and consistent budgeting explains why Odin must include simple, just-in-time explanations for financial concepts and flexible budget adjustment tools. The absence of gender differences supports gender-neutral design choices. Although the sample consists of students, their reported behavioral patterns (e.g., difficulty handling unexpected expenses) are directly transferable to Odin’s target demographic of young professionals.

**Directly justifies:**

- “Filipino SHS and college students have basic financial knowledge (mean 2.1/4) but large gaps in compound interest understanding, with less than 30% able to explain it.”
- “Students report inconsistent budgeting practices and difficulty staying within budgets when unexpected expenses occur, indicating a need for flexible budget adjustment features.”
- “No significant gender differences in financial literacy were found among Filipino students, suggesting gender-neutral design is appropriate for personal finance tools.”
- “Most students learn finance from family rather than formal education, implying that Odin’s explanations should complement existing informal financial socialization.”

**Limits of relevance:**

- Sample is students (not employed young professionals) from a single institution in Mindanao, not Metro Manila.
- Study measures self‑reported literacy and behavior, not actual transaction data or PFMS usage.
- No evaluation of digital financial tools or mobile app contexts.

## Limitations

- Single‑institution sample in Mindanao limits generalizability to Metro Manila young professionals.
- Cross‑sectional design cannot establish causation between education and financial behavior. [unacknowledged]
- Self‑reported Likert responses may overstate actual financial skills (social desirability bias). [unacknowledged]
- No measure of income or employment status, so findings may not reflect spending patterns of working adults.
- Study does not assess how literacy translates to real‑world financial decisions under pressure.

## Remember This

- 📌 Knowledge mean = 2.1/4, behavior mean = 1.9/4 — basic understanding but weak execution.
- ⚠️ Less than 30% explain compound interest — a core concept missing from most students.
- 💡 Budgets fail when unexpected expenses appear — Odin needs flexible, not rigid, rules.
- ✅ No gender differences — one less variable to segment in design.
