# Personal Financial Information Presentation and Consumer Spending

## Metadata

```yaml
---
paper_id: "a0b1c2d3-e4f5-4a6b-8c9d-0e1f2a3b4c5d"
designation: international
title: "Personal Financial Information Presentation and Consumer Spending"
authors: "Levi, Y."
year: 2025
venue: "Unknown"
odin_topics: ["5.A", "7.B", "8.A", "11.A", "12.A"]
shorthand_tags: ["/profiling-role", "/budget-rec-evidence", "/alert-design", "/eval-pfms-applied", "/pfms-intelligent-features"]
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

Presenting net worth as a monthly cash flow with a consumption frame and a salient spending comparison reduced discretionary spending by **15%** in a large field experiment.

## Problem and Motivation

Consumers can access online financial tools, but the way financial information is presented may systematically influence their spending decisions. Understanding how framing and salience affect behavior could inform low-cost policies to promote saving. Prior research on annuity framing showed valuation effects but never tested actual spending responses in a live setting.

## Approach

- Field experiment with 3,138 active users of an account aggregation app over 25 months.
- Personalized index converts net worth to a lifetime monthly cash flow using real annuity prices.
- Treatments varied index name (Financial Sustainability Index [fear appeal] vs Life Annuity Index [neutral]) and presence of a context plot comparing the index to historical spending.
- Main outcome: monthly discretionary spending (entertainment, restaurants, clothing, travel) from transaction-level data.
- Secondary outcomes: login frequency, cash withdrawals, large infrequent transactions, non-discretionary spending (gas, groceries, utilities).
- Random assignment to seven groups; analysis uses individual and month fixed effects.

## Findings

1. FSI-Plot group (consumption frame + context plot) reduced discretionary spending by **15%** relative to control (p<0.05).
2. Cash withdrawals decreased by 25% in the same groups, representing additional spending reduction.
3. **The spending reduction started immediately, persisted through the 8‑month experiment, and took another 8 months to converge back to control levels.**
4. No significant change in non‑discretionary categories (gas, groceries, utilities) or in groups receiving only the frame or only the plot.

- Reduction was strongest in “tempting” categories: restaurants (-14%), clothing (-20%), entertainment (-14%), travel (-24%).
- Large infrequent transactions also decreased, consistent with reminder effects on exceptional expenses.

## Key Figures and Tables

- Figure 1: Dashboard page for FSI-Plot treatment → shows the index and context plot placement.
- Figure 3: Monthly logins by treatment group → all treated groups increased logins; no difference across treatments.
- Figure 4: Monthly discretionary spending over time → FSI‑Plot groups diverge immediately and stay lower.
- Table 5: Main regression results → 15% discretionary spending drop (FSI‑Plot and FSI‑Plot‑inf).
- Table 7: Category‑specific effects → largest reductions in clothing, travel, and cash withdrawals.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| FSI | Financial Sustainability Index — consumption‑framed name intended to evoke fear of unsustainable spending. |
| LAI | Life Annuity Index — neutral‑framed name describing the index as a market annuity quote. |
| Context plot | A time‑series graph directly comparing the user’s index level to their historical monthly spending. |
| Discretionary spending | Spending on non‑essential categories (entertainment, restaurants, clothing, travel) that can be adjusted quickly. |
| Account aggregation app | An app that links multiple financial accounts (checking, savings, loans) to give a unified view of net worth. |

## Critical Citations

- [Benartzi, Previtero, & Thaler, 2011] — Foundational annuity framing experiments that motivated the consumption‑frame design.
- [Goldstein, Hershfield, & Benartzi, 2016] — “Illusion of wealth” effect: lump‑sum net worth feels larger than equivalent monthly income.
- [Karlan, McConnell, Mullainathan, & Zinman, 2016] — Salient reminders increase saving; directly parallels the context plot mechanism.

## Relevance to Odin

**Topics:**

5.A — Financial Behavioral Profiles in Personal Finance

7.B — Budget Recommendation in Personal Finance Systems

8.A — Anomaly Detection in Personal Finance Systems

11.A — Engagement Dynamics in Personal Finance Applications

12.A — Evaluation Frameworks for Personal Finance Systems

**Contribution to Odin:**

This paper demonstrates that a simple information design change (framing net worth as monthly cash flow with a salient spending comparison) produces large, persistent reductions in discretionary spending. For Odin, this directly justifies designing budget recommendation and alert interfaces that frame financial sustainability in monthly terms and explicitly contrast current spending with a sustainable benchmark. The finding that users increased login frequency when presented with the index supports Odin’s engagement strategy: novel, personally relevant financial information drives attention without gamification. The field experiment methodology provides a template for evaluating Odin’s own modules against a control group.

**Directly justifies:**

- “A consumption frame combined with a salient spending comparison reduces discretionary spending by 15% in a live field experiment.”
- “Presenting net worth as a monthly cash flow rather than a lump sum encourages users to cut spending on ‘tempting’ categories (entertainment, restaurants, clothing).”
- “Salient reminders of financial sustainability decrease large infrequent transactions by making exceptional expenses more visible.”
- “Users increase login frequency when a personalized financial index is added to their dashboard, indicating that novel information content drives engagement.”

**Limits of relevance:**

- Study population is wealthy U.S. users (mean net worth $1.1M), not Filipino young professionals with different income volatility and cultural obligations.
- The app used account aggregation (bank APIs); Odin relies on manual transaction entry, which may affect how users perceive spending comparisons.
- The experiment’s 8‑month follow‑up is shorter than Odin’s intended retention horizon; long‑term persistence beyond one year is unknown.
- No cold‑start analysis: all users had at least five months of transaction history before the experiment.

## Limitations

- Sample is high‑net‑worth U.S. users; results may not generalize to lower‑income or Philippine populations. [unacknowledged]
- No analysis of whether the spending reduction was offset by increased spending in unobserved accounts (e.g., cash accounts not linked to the app).
- The experiment was conducted in 2014 (pre‑registration era); the paper acknowledges it was not pre‑registered.
- Treatment effects on overall spending were only significant at the 10% level (6% reduction, p<0.10), suggesting weaker evidence for total spending changes.
- The mechanism (fear appeal vs. anchoring vs. new information) is not isolated; multiple channels could be at work.

## Remember This

- 🔑 **15% discretionary spending cut** — consumption frame + context plot works; neither alone does.
- 📌 Spending stayed lower for 8 months after the experiment — habits changed, not just a one‑time nudge.
- 💡 Cash withdrawals dropped 25% — users cut cash first (higher subjective value).
- ⚠️ Wealthy US sample (mean net worth $1.1M) — may not apply to Filipino young professionals.
