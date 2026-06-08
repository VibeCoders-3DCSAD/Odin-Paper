# Development and Evaluation of My Money Manager: An Intelligent Mobile App for Personalized Financial Insight

## Metadata

```yaml
---
paper_id: "10.32890/jdsd2025.3.2.9"
designation: algorithm-specific
title: "Development and Evaluation of My Money Manager: An Intelligent Mobile App for Personalized Financial Insight"
authors: "Parameswaran, S.; Saad, S. Z."
year: 2025
venue: "Journal of Digital System Development"
odin_topics: ["A.2", "B.1", "C.1", "E.1", "G.1", "J.1"]
shorthand_tags: ["/pfms-limitations", "/mobile-first-def", "/strategy-mechanics", "/anomaly-approaches", "/western-cat-limitations", "/sus"]
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

A personal finance Android app with fixed-variable expense differentiation and 90-day spending pattern analysis achieved **82.8% user validation** for income-expense tracking and 74.3% for improved financial habits.

## Problem and Motivation

Existing personal finance apps treat financial management as one-size-fits-all, offering generic advice that ignores individual spending patterns and fails to distinguish between fixed essential costs and variable discretionary expenses. Most apps lack the intelligence to detect abnormal spending behaviors or provide dynamic, personalized recommendations that adapt to changing circumstances. Prior work had not demonstrated an integrated mobile solution combining automated expense categorization, anomaly detection, and evolving financial guidance in a single user-validated system.

## Approach

- Dataset: 35 participants evaluated the app via six-point Likert-scale questionnaires covering App Experience, Perceived Ease of Use, Perceived Usefulness, and Perceived Acceptance.
- Development: Iterative and incremental agile methodology with Scrum principles, following Model-View-Controller architecture for Android.
- Core algorithm: Fixed vs. variable expense differentiation via rule-based categorization; 90-day lookback window for spending pattern analysis.
- Key calculations: Monthly income/expense summation (Equations 1–2), monthly savings = income - expenses (Equation 3), income/expense ratio (Equation 4), budget status = monthly budget - monthly expenses (Equation 5), category percentage = (category expense ÷ monthly expenses) × 100 (Equation 7).
- Evaluation metrics: Structured questionnaires measuring navigation ease, data entry efficiency, budget setting, insight comprehension, and perceived security.

## Findings

1. **82.8%** of users (45.7% strongly agreed, 37.1% agreed) confirmed income and expense tracking was efficient and reliable — the strongest validation across all features.
2. **74.3%** of users reported the app encouraged more effective financial management (28.6% strongly agreed, 45.7% agreed).
3. **71.4%** agreed financial insights helped guide financial decision-making (37.1% strongly agreed, 34.3% agreed).
4. **77.1%** rated adding income/expense entries as "Strongly Agree" for ease of use — identical for navigation and budget-setting.

- **Data security emerged as the weakest area:** only 11.4% strongly agreed their data was safe; 31.4% somewhat disagreed, the most concerning finding.

## Key Figures and Tables

- Figure 7: App experience ratings → visual appeal strong (45.7% strongly agree), but 42.9% only somewhat agreed they could complete tasks without help.
- Figure 8: Perceived ease of use → core functions (navigation, data entry, budget) at 77.1% strongly agree; insight comprehension dropped to 37.1% strongly agree.
- Figure 9: Perceived usefulness → income/expense tracking highest (45.7% strongly agree), insights lower (37.1% strongly agree).
- Figure 10: Perceived acceptance → overall satisfaction 40% strongly agree; data security only 11.4% strongly agree.
- Table 2: Perceived usefulness responses → time savings: 37.1% strongly agree, 37.1% agree; habit improvement: 28.6% strongly agree.

## Key Equations

$$Monthly\ Income = \Sigma(\text{all income entries for selected month})$$
*Sum of all income transactions within the filtered month.*

$$Monthly\ Savings = Monthly\ Income - Monthly\ Expenses$$
*Positive savings indicate surplus; negative signals deficit spending.*

$$Income/Expense\ Ratio = Monthly\ Income \div Monthly\ Expenses$$
*Ratio below 1.0 indicates spending exceeds income.*

$$Category\ Percentage = (Category\ Expense \div Monthly\ Expenses) \times 100$$
*Shows which spending categories dominate the user's budget.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Fixed expenses | Essential recurring costs (rent, loan payments) that do not vary month to month. |
| Variable expenses | Discretionary spending (entertainment, dining out) that users can control. |
| UTAUT2 | Unified Theory of Acceptance and Use of Technology 2 — an adoption model measuring performance expectancy, effort expectancy, and social influence. |
| MVC | Model-View-Controller — software architecture separating data logic (Model), user interface (View), and input handling (Controller). |
| Scrum | An agile framework organizing development into fixed-length sprints with iterative feedback loops. |
| 90-day analysis | The app's lookback window for detecting spending patterns and providing recommendations. |

## Critical Citations

- [Shaikh et al., 2022] — Identified the failure to distinguish fixed from variable costs as a critical gap in existing PFMS apps.
- [Mijić & Ćebić, 2023] — Provided UTAUT2 framework for understanding adoption factors including performance expectancy.
- [Carlin et al., 2022] — Demonstrated that mobile apps reducing barriers to financial data access improve user behavior and reduce overdraft fees.
- [Torno et al., 2021] — Developed PFMS taxonomy that informed feature classification.
- [Nielsen, 2012] — Usability testing principles used in the evaluation methodology.

## Relevance to Odin

**Topics:**

A.2 — Existing Personal Finance and Budget Management Systems

B.1 — Mobile-First Design in Personal Finance Systems

C.1 — Budgeting Strategies and Budget Recommendation

E.1 — Anomaly Detection in Personal Finance Systems

G.1 — Expense Categorization in Filipino Personal Finance Contexts

J.1 — System Evaluation

**Contribution to Odin:**

This paper provides direct empirical validation that users value fixed-vs-variable expense differentiation and anomaly detection — both features Odin's expense categorization and anomaly detection modules require. The finding that 31.4% of users somewhat disagreed about data security serves as a critical warning for Odin's privacy-by-design requirements, especially given the sensitivity of Filipino financial data. The usability evaluation framework (six-point Likert across four dimensions) offers a tested template for Odin's ISO 25010 and SUS evaluation protocol, while the 35-participant sample size provides a benchmark for Odin's target evaluation scale.

**Directly justifies:**

- "Users reported 82.8% validation for income-expense tracking features, indicating that reliable manual transaction logging is the most valued capability in personal finance apps."
- "Only 11.4% of users strongly agreed their financial data was secure in a standard Android PFMS app, demonstrating that data security is the weakest trust dimension requiring explicit design attention."
- "Fixed vs. variable expense differentiation addresses a critical gap identified in existing PFMS literature (Shaikh et al., 2022) and was implemented successfully in a working mobile application."
- "Financial insight comprehension received only 37.1% 'Strongly Agree' for ease of use, indicating that data visualization quality directly impacts perceived usefulness of analytical features."
- "A 35-participant usability evaluation with six-point Likert scales provides sufficient signal to identify both strengths (tracking) and weaknesses (security, insight clarity) in PFMS design."

**Limits of relevance:**

- Study population is Malaysian, not Filipino; cultural spending norms and financial inclusion contexts differ, though both are Southeast Asian emerging economies.
- The app uses rule-based categorization, not ML classification — Odin's approach is more sophisticated but the user validation patterns remain instructive.
- No algorithm performance metrics (accuracy, precision, recall) are reported — only user perception data, which cannot justify model selection.
- The 35-participant sample is small for generalizable claims about usability across demographic segments.
- Data security concerns reflect user perception, not objective security auditing results.

## Limitations

- Small sample size (n=35) limits statistical power and generalizability to broader populations. [unacknowledged]
- No longitudinal follow-up — measurement captures first impressions only, not sustained behavior change or retention.
- The paper acknowledges low insight comprehension (14.3% found it somewhat challenging) but does not propose specific visualization improvements.
- No comparison to existing apps (YNAB, PocketGuard) — claims of "addressing gaps" lack competitive benchmarking evidence.
- Data security findings (only 11.4% strongly agree) are presented as user perception without technical root-cause analysis or proposed mitigations beyond "clearer messaging."

## Remember This

- 🔑 **82.8% validated tracking** — manual expense entry is the most trusted, most valued PFMS feature.
- ⚠️ **Only 11.4% strongly trust data security** — Odin must prioritize privacy-by-design or lose user confidence.
- 📌 **Insight comprehension lagged at 37.1% strongly agree** — charts and recommendations need clearer design, not just better data.
- ✅ **74.3% reported better habits** — even simple fixed/variable differentiation drives behavioral change.
- 🧠 **35-user SUS-style evaluation works** — Odin can use this scale and sample size for early validation.
