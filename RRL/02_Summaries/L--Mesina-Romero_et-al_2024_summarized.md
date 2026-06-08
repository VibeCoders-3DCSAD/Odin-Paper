# From Surge to Stability: Digital Payments Driving a Steady Transition: 2024 Status of Digital Payments in the Philippines

## Metadata

```yaml
---
paper_id: "d2e4c6a8-1b3f-4e5d-9a7b-2c8f5d3e1a9b"
designation: local
title: "From Surge to Stability: Digital Payments Driving a Steady Transition: 2024 Status of Digital Payments in the Philippines"
authors: "Mesina-Romero, B.; Masangkay, M. C.; Franco, M.; Yambao, M. A. V.; Delgado, K.; Bueno, P. N.; Lingat, P. J.; Natividad, G. M.; Lapus, A. R.; Manuel, R. M.; Yñigo, K. T."
year: 2024
venue: "Bangko Sentral ng Pilipinas"
odin_topics: ["A.1", "G.1", "H.1"]
shorthand_tags: ["/expenditure-patterns", "/fil-pfms-categories", "/security-standards", "/user-trust"]
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

Digital payments reached **57.4%** of retail transaction volume in the Philippines by 2024, driven by merchant payments (66.4% share) and person-to-person transfers (20.6% share).

## Problem and Motivation

The BSP lacks a systematic, data-driven way to measure the country's progress toward a digital payments ecosystem. Without reliable measurement, policymakers cannot identify barriers or prioritize interventions to accelerate adoption. Prior measurement models (e.g., BTCA 2019) provided a foundation but needed enhancement for sustained tracking.

## Approach

- Dataset: Monthly retail payment transactions across government (G2X), business (B2X), and person (P2X) categories, disaggregated into 24 use-cases.
- Method: Estimation exercise using quantitative data from multiple sources (DBM, BTr, PSA, BSP, financial institutions) plus critical assumptions to fill gaps.
- Analysis: Compute share of digital vs. non-digital by volume and value for each use-case, then aggregate to national totals.
- Key use-cases: Merchant payments (P2B), P2P transfers, B2B supplier payments, government disbursements, tax collections.
- Enhancement from BTCA model: Refined use-case grid and incorporation of new payment channels (QR Ph, InstaPay, PESONet).

## Findings

1. **57.4%** of total monthly retail payment volume was digital in 2024, up from 52.8% in 2023, exceeding the Philippine Development Plan target of 52–54%.
2. **59.0%** of total retail payment value was digital, representing USD 136.0 billion monthly.
3. Merchant payments (P2B) dominate at **66.4%** of digital volume (2.2B transactions), growing 29.1% year-on-year.
4. P2P transfers grew 34.7% to 680.5M transactions, now 20.6% of digital volume.

- Government disbursements (G2X) are 97.2% digital, but government collections (P2G) are only 24.6% digital — a key opportunity.
- InstaPay volume rose 67.8% year-on-year; PESONet added a third daily settlement cycle in July 2024.

## Key Figures and Tables

- Figure: Share of digital payments by volume (2013–2024) → from 1% (2013) to 57.4% (2024), steepest rise after 2020.
- Figure: Share of digital payments per use-case (volume) → G2X at 97.2%, P2X at 72.2%, B2X at 19.8%.
- Table: Payment grid with percentage shares → P2B (person-to-business) accounts for 57.3% of total volume, B2B 26.1%, P2P 13.1%.
- Figure: Share of digital payments by value → 59.0% overall, with P2X at 80.4% by value.
- Table: Monthly volume by use-case (millions) → Total 5,756.5M, digital 3,307.0M.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| P2X | Person-to-anything: payments made by individuals to government, businesses, or other persons. |
| B2X | Business-to-anything: payments made by businesses. |
| G2X | Government-to-anything: payments made by the government. |
| P2B | Person-to-business payments (e.g., merchant purchases, utilities). |
| P2P | Person-to-person transfers (e.g., remittances, lending). |
| QR Ph | National QR code standard for interoperable payments in the Philippines. [think: scan once, pay from any wallet] |
| InstaPay | Real-time, low-value electronic fund transfer system (account-to-account). |
| PESONet | Batch settlement system for higher-value or non-urgent transactions. |
| EFT | Electronic fund transfer — moving money digitally between accounts. |

## Critical Citations

None.

## Relevance to Odin

**Topics:**

A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

G.1 — Expense Categorization in Filipino Personal Finance Contexts

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

**Contribution to Odin:**

This BSP report provides authoritative, national-scale data on how Filipinos actually make payments — knowledge that grounds Odin’s expense categorization and user behavior assumptions. The finding that merchant payments (P2B) dominate digital volume (66.4%) confirms that retail spending is the core use case, directly informing which expense categories (e.g., groceries, dining, transport) should be prioritized in Odin’s FIES/CFS-based taxonomy. Additionally, the report’s documentation of BSP consumer redress and merchant acquisition regulations (Circulars 1195 and 1198) offers citable evidence of the regulatory emphasis on trust and security — justifying Odin’s privacy-by-design approach even without banking integration.

**Directly justifies:**

- “Merchant payments account for 66.4% of digital payment volume in the Philippines (2024), indicating that retail spending is the primary transaction type for Filipino consumers, which directly maps to Odin’s expense categorization module.”
- “Only 24.6% of government collections (P2G) were digital in 2024, showing that a large share of taxes and fees are still paid via cash — a relevant constraint for young professionals who may have irregular cash-based government payments.”
- “InstaPay transaction volume grew 67.8% year-on-year, demonstrating rapid adoption of real-time account-to-account transfers among Filipinos, supporting the design assumption that users are comfortable with digital financial interfaces.”
- “BSP Circular No. 1195 requires timely notifications and fund return for failed EFTs, establishing consumer protection norms that Odin can cite when designing transparent manual transaction logging and error handling.”

**Limits of relevance:**

- Report focuses on payment infrastructure and aggregate volumes, not individual spending behavior or budgeting practices.
- No demographic breakdown by age (young professionals) or income type — cannot be used to claim specific patterns for Odin’s target user segment.
- Data covers all retail payments, not just those made by individuals; business and government transactions inflate some categories (e.g., B2B supplier payments).
- Manual transaction input (Odin’s scope) is not measured or discussed; the report assumes digital payment initiation, not manual logging.

## Limitations

- No disaggregation by age, income, or occupation — generalizes across all Filipinos. [unacknowledged]
- Relies on estimation and assumptions for several use-cases where direct data is unavailable (e.g., P2P lending).
- Does not address user behavior after digital payment adoption (e.g., budgeting, overspending, financial literacy).
- Excludes informal payment methods (e.g., cash under the table) that may still dominate certain spending categories for young professionals. [unacknowledged]
- Measurement model is designed for policy, not for behavioral finance research; causal claims cannot be drawn.

## Remember This

- 🔑 **57.4% of retail payment volume is digital** — up from 1% in 2013, showing rapid Filipino adoption.
- 📌 Merchant payments (P2B) are **66.4% of digital volume** — retail spending drives the ecosystem.
- 💡 Only **24.6% of P2G** (person-to-government) is digital — cash still dominates taxes and fees.
- 🔍 InstaPay volume grew **67.8% YoY** — real-time transfers are the new normal for Filipinos.
- ⚠️ No breakdown by age — cannot assume young professionals behave like the national average.
