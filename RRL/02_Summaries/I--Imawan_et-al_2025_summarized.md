# Enhancing Financial Literacy in Young Adults: An Android-Based Personal Finance Management Tool

## Metadata

```yaml
---
paper_id: "10.58536/j-hytel.166"
designation: international
title: "Enhancing Financial Literacy in Young Adults: An Android-Based Personal Finance Management Tool"
authors: "Imawan, R.; Putra, W. P.; Alqahtani, R.; Milakis, E. D.; Dumchykov, M."
year: 2025
venue: "Journal of Hypermedia & Technology-Enhanced Learning"
odin_topics: ["A.2", "B.1", "C.1", "G.1", "I.1", "J.1"]
shorthand_tags: ["/pfms-typology", "/pfms-features", "/mobile-first-def", "/mobile-ux-entry", "/strategy-mechanics", "/budget-rec-existing", "/cat-approaches", "/retention-mechanisms", "/value-driven-retention", "/eval-frameworks", "/eval-pfms-applied"]
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

An Android-based personal finance app achieved an **"Excellent" 4.6/5** usability score from 50 young adults, with income/expense tracking and goal setting driving consistent engagement.

## Problem and Motivation

Young adults face rising financial instability due to limited experience and guidance, yet most existing financial tools are not designed for their mobile-first, interactive preferences. Without targeted interventions, poor financial habits formed early can lead to long-term debt cycles. Prior work established financial literacy's importance but did not evaluate how a customized mobile app directly changes financial behaviors among Indonesian young adults.

## Approach

- Waterfall development model (requirements → design → implementation → testing → deployment) with black-box testing of all modules.
- Features: secure login, income/expense tracking with categorization, financial goal setting with progress bars, budget projection with alerts, and notification reminders.
- Dataset: 50 university students aged 19–34 in Indonesia, using Android devices (Samsung, Xiaomi, Oppo, Android 10+) over two weeks.
- Evaluation: 5‑point Likert survey covering usability, user satisfaction, functionality, engagement, design satisfaction, and improvement feedback.
- Analysis: Average aspect scores (Equation 1) aggregated to overall application score (Equation 2), categorized from "Very Poor" (1.00–1.80) to "Excellent" (4.21–5.00).

## Findings

1. Overall application score was **4.6/5 (Excellent)** — 4.6 out of 5, with 72–78% of users rating each indicator as 5.
2. Highest-rated indicators: ENG2 (likelihood to continue using, 4.74/5) and DES1 (visual design, 4.70/5).
3. Lowest-rated (still high): FUN2 (features function as described, 4.54/5) and USA2 (navigation ease, 4.54/5).

- Users praised intuitive design, accurate tracking, and motivational reminders; suggested more customization (budget categories) and deeper trend analysis.
- Notification reminders and visual goal progress bars were cited as key drivers of consistent engagement.

## Key Figures and Tables

- Figure 7: Home page and income/expense tracking displays → clean dashboard with clear navigation to all core features.
- Figure 8: Financial goal and budget projection screens → progress bars and adjustable targets motivate goal‑oriented saving.
- Table 13: Evaluation scores by aspect → 72–78% of users gave the highest rating (5) across all indicators.
- Figure 10: Average scores per indicator → engagement (ENG2 = 4.74) and design (DES1 = 4.70) lead; functionality (FUN2 = 4.54) slightly lower.

## Key Equations

$$Aspect\ Score = \frac{\sum(Indicator\ Scores)}{Number\ of\ Indicators}$$

*Aspect score averages all indicator scores for one evaluation dimension.*

$$Overall\ Application\ Score = \frac{\sum(Aspect\ Scores)}{Number\ of\ Aspects}$$

*Final score averages all aspect scores across usability, satisfaction, functionality, engagement, design, and feedback.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Waterfall model | Linear software development process: requirements → design → implementation → testing → deployment. |
| Black‑box testing | Testing software functionality without inspecting internal code, only inputs and outputs. |
| Likert scale | 1–5 rating scale measuring agreement or satisfaction (1 = very poor, 5 = excellent). |

## Critical Citations

- [Petersen et al., 2009] — Justifies the Waterfall model as suitable for large‑scale, phase‑gated development.
- [Zhang et al., 2021] — Behavior change theory used to explain why reminders and progress indicators sustain engagement.

## Relevance to Odin

**Topics:**

A.2 — Existing Personal Finance and Budget Management Systems

B.1 — Mobile-First Design in Personal Finance Systems

C.1 — Budgeting Strategies and Budget Recommendation

G.1 — Expense Categorization in Filipino Personal Finance Contexts

I.1 — User Retention and Engagement in Personal Finance Systems

J.1 — System Evaluation

**Contribution to Odin:**

This paper validates the feature set Odin intends to implement (income/expense tracking, budgeting, goal setting, notifications) by demonstrating high user satisfaction (4.6/5) and self‑reported behavior change in a young adult population. The finding that visual goal progress bars and reminders are the strongest engagement drivers directly informs Odin's retention design — prioritizing value‑driven feedback over gamification. Although the study uses a basic Likert scale rather than ISO 25010 or SUS, its evaluation approach provides a benchmark for Odin's own usability testing with 50 users. The application's reliance on manual transaction entry (no bank integration) matches Odin's scope, making the engagement patterns directly transferable.

**Directly justifies:**

- "An Android‑based PFM app with income/expense tracking, budget projection, and goal setting achieved an overall usability score of **4.6/5 (Excellent)** from 50 young adults after two weeks of use."
- "Seventy‑eight percent of users rated their intention to continue using the app as 5/5, indicating that core tracking features alone can drive retention without gamification."
- "Visual progress bars for financial goals and automated reminders were cited as the most effective features for maintaining consistent tracking behavior."
- "Users request deeper spending trend analysis and customizable budget categories — gaps that Odin's predictive modules (forecasting, anomaly detection) are designed to fill."

**Limits of relevance:**

- Study population is Indonesian, not Filipino; cultural spending norms and income volatility may differ, though both are Southeast Asian emerging economies.
- Evaluation period was only two weeks; long‑term habit formation and retention beyond initial enthusiasm are not measured.
- No AI/ML features are present; the paper cannot justify algorithm selection for Odin's forecasting, anomaly detection, or profile classification modules.
- Usability evaluation used an ad‑hoc Likert scale, not the ISO 25010 or SUS frameworks Odin requires for formal evaluation.

## Limitations

- Short two‑week evaluation window cannot assess long‑term financial habit change or sustained retention.
- Sample size of 50, though adequate for initial usability, may not generalize to all Filipino young professionals.
- No control group or objective financial behavior measurement (e.g., actual savings growth) — only self‑reported satisfaction and engagement.
- The app lacks any predictive or adaptive features; its value is purely transactional tracking. [unacknowledged]
- Waterfall methodology, while structured, is less iterative than agile approaches — may not reflect modern mobile app development practices. [unacknowledged]

## Remember This

- 🔑 **4.6/5 Excellent** — young adults rate this manual‑entry PFM app highly across usability, engagement, and design.
- 📌 Goal progress bars + reminders → strongest drivers of consistent use, no gamification needed.
- 💡 78% intend to continue using — core tracking features alone can retain users if designed intuitively.
- ⚠️ No AI, no long‑term data, no Filipino validation — use for feature inspiration, not algorithm justification.
