# Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking

```yaml
---
name: paper-summary
paper_id: "a3f5e2d1-4b7c-4e9f-8a2d-6c3e8b5f1d7a"
source_document: "001_Alenazi_BCSHCI23.md"
designation: international
title: "Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking"
authors: "Alenazi, M.; Sas, C."
year: 2023
venue: "BCS HCI 2023"
odin_topics: ["A.2", "C.1", "G.1"]
shorthand_tags: ["/pfms-typology", "/pfms-features", "/pfms-limitations", "/pfms-gap", "/strategy-mechanics", "/strategy-distillation", "/cat-approaches"]
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

Only 26 of 45 top budgeting apps support multiple budgets via money envelopes; most prioritize transaction tracking over true budgeting.

## Problem and Motivation

Budgeting apps are growing rapidly, but limited HCI research evaluates their actual budgeting functionality. Existing work focuses on exploratory studies of financial practices, not systematic feature analysis. A theoretical gap exists: mental accounting theory (money envelopes) is rarely applied to app design.

## Approach

- Searched Google Play and Apple Store (UK) with keywords “budget, budgeting, finance” → 1335 apps.
- Filtered to 45 top-rated free apps (rating ≥4.0, ≥1000 reviews, no bank account requirement).
- Used mental accounting theory (Thaler, 1999) as analytic lens.
- Expert evaluation of each app by two authors (Android and iOS) over several months.
- Identified functionalities: accounts, transactions (income/expense/transfer), budgets (single vs multiple), categories.

## Findings

1. All 45 apps support tracking transactions, but **only 26 (58%)** support multiple budgets (money envelopes).
2. 19 apps use a single budget for all expenses — no category-level monitoring.
3. Only two apps (Goodbudget, SimpleBudget) explicitly mention envelope systems in their descriptions.
4. Terminology for accounts is inconsistent: 41 apps use banking terms (virtual bank/card accounts), few use everyday terms like “wallet” or “budget.”
5. Transfer transactions are supported by 35 apps, but 33 allow transfers even when source account has insufficient funds.

## Key Figures and Tables

- Figure 1: PRISMA diagram → 1335 initial apps filtered down to 45 for analysis.
- Table 1: Functionalities for funds and expenses → 44 apps support income creation; all 45 support expense creation.
- Table 2: Accounts and budgets → Only 26 apps allow multiple budgets with per-category envelopes.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Mental accounting | Behavioral economics theory: people mentally partition money into labeled categories (envelopes) for specific purposes. |
| Money envelope | A physical or digital container for funds allocated to a specific expense category (e.g., groceries, rent). |
| Transaction account | A container (virtual bank, cash, wallet) that holds income, expense, or transfer transactions. |
| Single budget | One global spending limit covering all expense categories together. |
| Multiple budget | Separate spending limits for each expense category — aligns with envelope budgeting. |

## Critical Citations

- [Thaler, 1999] — Foundational mental accounting theory paper; defines money envelopes and budgeting as cognitive operations.
- [Kaye et al., 2014] — HCI study on personal finance tracking; shows people use analogue tools like diaries and spreadsheets.
- [Snow and Vyas, 2015a] — Identifies use of coin jars and envelopes in household budgeting practices.

## Relevance to Odin

**Topics:**

A.2 (Existing Personal Finance and Budget Management Systems), C.1 (Budgeting Strategies and Budget Recommendation), G.1 (Expense Categorization in Filipino Personal Finance Contexts)

**Contribution to Odin:**

This paper provides a systematic functionality review of 45 budgeting apps, revealing a critical gap: most apps emphasize tracking past expenses rather than supporting proactive envelope-based budgeting. It justifies Odin’s design decision to implement multiple budgets with per-category envelopes (not just a single spending limit). The paper also highlights inconsistent terminology for accounts and transactions — a lesson for Odin’s user-facing vocabulary.

**Directly justifies:**

- “Most existing budgeting apps prioritize transaction tracking over proactive budgeting using money envelopes.”
- “Only 58% of top-rated apps support multiple budgets (per-category spending limits), indicating a market gap that Odin can address.”
- “Mental accounting theory (Thaler, 1999) provides a principled foundation for envelope-based budgeting features.”
- “Inconsistent terminology for accounts (banking vs. everyday terms) creates user confusion — Odin should adopt clear, everyday language.”

**Limits of relevance:**

- Study conducted on UK app stores (Google Play and Apple Store) — not specific to Filipino users or cultural spending patterns.
- Evaluation is functionality review, not user study with Filipino young professionals.
- No algorithmic or predictive modeling components — relevance is to feature design, not ML-specific modules.

## Limitations

- Only free apps analyzed (premium features may offer more budgeting support).
- Excluded apps requiring bank account linkage — misses category of full-automation tools.
- No user testing; findings based on expert walkthrough only.
- One-time snapshot — does not assess longitudinal usability or retention.

## Remember This

- 🔑 **Only 26/45 apps** support envelope budgeting — most just track spending.
- 💡 Money envelopes (mental accounting) are the gold standard for proactive budgeting.
- 📌 33 of 35 apps allow transfers even with **insufficient funds** — a dangerous design flaw.
