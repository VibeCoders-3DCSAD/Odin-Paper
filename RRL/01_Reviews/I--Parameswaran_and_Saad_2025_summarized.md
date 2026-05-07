# DEVELOPMENT AND EVALUATION OF MY MONEY MANAGER: AN INTELLIGENT MOBILE APP FOR PERSONALIZED FINANCIAL INSIGHT

```yaml
---
name: paper-summary
paper_id: "10.32890/jdsd2025.3.2.9"
source_document: "unknown.md"
designation: international
title: "DEVELOPMENT AND EVALUATION OF MY MONEY MANAGER: AN INTELLIGENT MOBILE APP FOR PERSONALIZED FINANCIAL INSIGHT"
authors: "Parameswaran, S.; Saad, S. Z."
year: 2025
venue: "Journal of Digital System Development"
odin_topics: ["A.2", "B.1", "C.1", "E.1", "G.1", "H.1", "J.1"]
shorthand_tags: ["/pfms-features", "/pfms-limitations", "/pfms-gap", "/mobile-first-def", "/mobile-ux-entry", "/strategy-mechanics", "/budget-rec-existing", "/anomaly-approaches", "/cat-approaches", "/user-trust", "/data-sensitivity", "/sus", "/eval-pfms-applied", "/eval-limitations"]
summary_date: 2026-05-07
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

Intelligent app with 90‑day analysis achieves **82.8%** user approval for expense tracking and 74.3% for better financial habits.

## Problem and Motivation

Existing mobile finance apps lack intelligence, offering generic advice instead of personalized guidance. This leads to overspending, debt, and financial stress for users. No prior solution provided dynamic, evolving insights based on individual 90‑day spending patterns.

## Approach

- Iterative, incremental agile methodology with 6 phases (research to maintenance).
- Android app following MVC pattern and Material Design principles.
- Automated expense categorization distinguishing fixed vs. variable costs.
- 90‑day spending pattern analysis with anomaly detection and personalized savings recommendations.
- Core metrics: monthly income, expenses, savings, income/expense ratio, budget status.
- Usability evaluation with 35 participants using 6‑point Likert scale.

## Findings

1. **82.8%** of users (45.7% strongly agree, 37.1% agree) found income/expense tracking efficient and reliable.
2. 74.3% reported the app encouraged better financial management (budget planning and savings recommendations).
3. 71.4% agreed financial insights helped guide decision‑making (37.1% strongly agree, 34.3% agree).
4. 77.1% rated navigation, adding entries, and budget setting as “Strongly Agree” easy; editing had 60% strongly agree.
5. Only 37.1% strongly agreed that viewing financial insights was easy; **14.3%** found it somewhat difficult.
6. Data security perception was weakest: only 11.4% strongly agreed data was safe; 31.4% somewhat disagreed.

## Key Figures and Tables

- Figure 7 (App Experience): Mixed confidence in task completion – 42.9% only somewhat agreed they could finish without help.
- Figure 8 (Perceived Ease of Use) / Table 1: 77.1% strongly agreed adding entries easy; insights had 37.1% strongly agree (lowest).
- Figure 9 (Perceived Usefulness) / Table 2: Income/expense tracking most valued (82.8% positive), insights least (71.4% positive).
- Figure 10 (Perceived Acceptance): Security trust concerning – 31.4% somewhat disagreed data was secure.

## Key Equations

$$\text{Monthly Savings} = \text{Monthly Income} - \text{Monthly Expenses}$$
*Savings derived from income minus all expenses for the selected month.*

$$\text{Category Percentage} = \frac{\text{Category Expense}}{\text{Monthly Expenses}} \times 100$$
*Percentage of total spending allocated to each expense category.*

## Definitions

| Term / Acronym | Plain‑English Definition |
| -------------- | ------------------------ |
| MVC | Model‑View‑Controller – separates data, UI, and logic for maintainability. |
| UTAUT2 | Unified Theory of Acceptance and Use of Technology 2 – model for adoption factors. |
| YNAB | “You Need A Budget” – rules‑based budgeting app with steep learning curve. |
| PocketGuard | App that auto‑categorizes recurring expenses and distinguishes fixed/variable costs. |
| 90‑day analysis | Spending pattern review over three months to detect anomalies and optimize savings. |

## Critical Citations

- [Mijić & Cebić, 2023] – UTAUT2 model identifies performance expectancy and effort expectancy as key adoption drivers.
- [Forbes Advisor, 2024] – Highlights PocketGuard and YNAB as market leaders with limitations (steep learning curve, reliance on precise categorization).
- [Torno et al., 2021] – Taxonomy of mobile finance apps by core functionalities (budgeting, tracking, investment).

## Relevance to Odin

**Topics:**

A.2 (Existing Systems), B.1 (Mobile‑First Design), C.1 (Budgeting Strategies), E.1 (Anomaly Detection), G.1 (Expense Categorization), H.1 (Data Privacy & Trust), J.1 (System Evaluation)

**Contribution to Odin:**

The paper validates that automated expense categorization and 90‑day anomaly detection are highly valued by users (82.8% for tracking). It also reveals critical trust gaps in data security (only 11.4% strong trust) – a finding that directly informs Odin’s H.1 arguments about user confidence. The evaluation methodology (6‑point Likert, N=35) provides a template for J.1 system assessment, though it lacks SUS standardization.

**Directly justifies:**

- “Automated expense categorization reduces user entry friction and improves reliability (82.8% user approval).”
- “Anomaly detection via spending pattern analysis can identify behavioral irregularities without requiring labeled training data.”
- “User trust in data security is a major adoption barrier; 31.4% of users expressed distrust even in a prototype.”
- “Personalized 90‑day insights drive better financial habits, with 74.3% of users reporting improved management.”

**Limits of relevance:**

- Study conducted in Malaysia; not specific to Filipino young professionals or local cultural obligations (A.1, F.1).
- No machine learning or algorithmic detail – anomaly detection is rule‑based; does not support D.2 (LSTM) or E.2 (Isolation Forest).
- Evaluation uses custom Likert questions, not ISO 25010 or SUS, limiting comparability with standard J.1 frameworks.

## Limitations

- Small sample size (N=35) limits generalizability.
- No longitudinal data on long‑term habit change or retention.
- Self‑reported survey responses may suffer from social desirability bias.
- Security and privacy features were not technically implemented; only user perceptions were measured.

## Remember This

- 🔑 **82.8%** found expense tracking efficient – core functionality is solid.
- ⚠️ Only **11.4%** strongly trusted data security – a major red flag to address.
- 💡 90‑day analysis personalizes savings advice; 74.3% said it improved financial habits.
