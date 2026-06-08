# Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking

## Metadata

```yaml
---
paper_id: "10.14236/ewic/BCSHCI2023.1"
designation: international
title: "Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking"
authors: "Alenazi, M.; Sas, C."
year: 2023
venue: "BCS HCI 2023"
odin_topics: ["A.2", "C.1", "G.1"]
shorthand_tags: ["/pfms-typology", "/pfms-features", "/pfms-limitations", "/pfms-gap", "/strategy-mechanics", "/strategy-distillation", "/cat-approaches"]
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

Only 26 of 45 top-rated budgeting apps (58%) support envelope-based multiple budgets; one third offer only expense tracking with no budgeting functionality.

## Problem and Motivation

Existing HCI research on personal finance has focused on exploratory studies of financial practices, leaving a gap in systematic evaluations of budgeting app functionalities. Without proper budgeting support, users struggle to control spending and abandon digital tools shortly after adoption. Prior work has not evaluated whether popular apps actually implement envelope-based budgeting informed by mental accounting theory.

## Approach

- Dataset: 1,335 apps from Google Play Store and Apple Store filtered to 45 top-rated free apps (rating ≥4.0, ≥1,000 reviews, no bank account requirement).
- Method: Functionality review using mental accounting theory (Thaler, 1999) as the analytical lens.
- Evaluation: Expert evaluation of all 45 apps on Galaxy S21+; second author validated 5 apps on iPhone 12.
- Key functionalities analyzed: account types (available funds, wealth, expenses), transaction types (income, expense, transfer), budget types (single vs multiple envelopes), and categorization.
- Data extraction: Iterative identification of functionalities from app descriptions followed by hands-on testing.

## Findings

1. **Only 26 of 45 apps (58%)** support multiple budgets (money envelopes) as advocated by mental accounting theory.
2. 8 apps provide only expense tracking with no budget monitoring; 7 apps use a single budget for all expenses.
3. Only 2 apps (Goodbudget, SimpleBudget) explicitly mention money envelope systems in their descriptions; none reference mental accounting theory.
4. Account terminology is inconsistent: 41 apps have transaction accounts, but only 11 support saving accounts, and 4 apps store transactions directly on home screen without any account container.
5. Transfer transactions (moving money between accounts) are supported by 35 apps, but 33 allow transfers even with insufficient funds — a risk for budget integrity.

- Most apps prioritize tracking over budgeting, with limited distinction between income (money-in) and expense (money-out) accounts.
- 40 apps provide predefined expense categories (e.g., grocery, transport); 42 allow user-defined categories.

## Key Figures and Tables

- Figure 1: PRISMA diagram of app selection → 1,335 apps narrowed to 45 eligible for analysis.
- Table 2: Functionality comparison across 45 apps → 26 apps support multiple budgets (col 11); 19 support only single budget or none.
- Figure (implied from text): Single vs multiple budget distribution → 58% envelope-based, 16% single budget, 18% tracking-only, 8% unclassified or premium.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Mental accounting | Behavioral economics theory where people mentally partition money into separate “accounts” for different purposes. |
| Money envelopes | Physical or digital representation of a mental account — money set aside for a specific expense category (e.g., groceries). |
| Single budget | One overall spending limit for all expenses, without category-specific allocations. |
| Multiple budgets | Separate spending limits per expense category (money envelopes), aligned with mental accounting. |
| Transfer transaction | Movement of money from one account to another (e.g., from income account to grocery envelope). |
| Transaction account | A container (virtual wallet) that holds income, expense, or transfer records. |

## Critical Citations

- [Thaler, 1999] — Foundational mental accounting theory; provides the analytical framework for evaluating budgeting apps.
- [Snow and Vyas, 2015a] — Prior HCI study showing users abandon budgeting apps due to manual entry burden and lack of spending control.

## Relevance to Odin

**Topics:**

A.2 — Existing Personal Finance and Budget Management Systems

C.1 — Budgeting Strategies and Budget Recommendation

G.1 — Expense Categorization in Filipino Personal Finance Contexts

**Contribution to Odin:**

This paper directly justifies Odin’s design decision to prioritize envelope-based multiple budgets over simple tracking or single-budget approaches. The finding that only 58% of top-rated apps support money envelopes reveals a market gap that Odin can fill by implementing theoretically grounded budgeting. The paper’s analysis of inconsistent account terminology (income vs expense) informs Odin’s need for clear distinction between available funds and spending categories. Additionally, the documented lack of transfer transaction support (or allowing transfers from empty accounts) warns Odin’s design team to implement balance-checked transfers to preserve budget integrity.

**Directly justifies:**

- “Only 26 of 45 top-rated budgeting apps (58%) implement envelope-based multiple budgets; one third provide no budgeting functionality beyond expense tracking.”
- “Most budgeting apps fail to distinguish between income accounts (money-in) and expense accounts (money-out), leading to cognitive confusion and overspending risk.”
- “Four of the reviewed apps store transactions directly on the home screen without linking to any account container, preventing proper budget tracking.”
- “Thirty-five apps support transfer transactions, but 33 allow transfers even when the source account has insufficient funds — a design flaw Odin must avoid.”

**Limits of relevance:**

- Study population and app stores are UK-based; Filipino app usage patterns and financial behaviors may differ.
- The review excluded apps requiring bank account integration; Odin is manual-only, so this exclusion does not affect applicability.
- No user study was conducted; findings are based solely on expert functionality review, not actual usage data or retention metrics.

## Limitations

- Only top-rated apps (≥4.0 stars, ≥1,000 reviews) were analyzed; lower-rated or niche apps may offer different budgeting features. [unacknowledged]
- No user evaluation — the review cannot determine whether the identified functionalities are actually used or effective in changing financial behavior.
- Findings are based on UK app stores; cultural differences in budgeting practices (e.g., ubiquity of cash envelopes in the Philippines) are not considered. [unacknowledged]
- The review does not assess data privacy, security, or compliance with local financial regulations.
- Manual entry assumption: all apps require manual transaction input (since bank integration was excluded), which aligns with Odin’s scope but may not reflect apps that rely on automatic import.

## Remember This

- 🔑 **58% (26/45)** of top budgeting apps support envelope-based budgets — the rest offer only tracking or single budgets.
- 📌 One third of apps provide **no budgeting functionality** at all — just expense tracking.
- 💡 Inconsistent account terminology (income vs expense) confuses users and undermines budget control.
- ⚠️ 33 of 35 apps allow **transfers from empty accounts** — a design risk Odin must block.
- 🧠 Mental accounting theory (Thaler, 1999) is the gold standard for envelope budgeting, but only 2 apps mention it.
