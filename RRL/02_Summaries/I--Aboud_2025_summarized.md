# Goal Programming Model in Financial Planning of the International Development Bank

## Metadata

```yaml
---
paper_id: "10.21070/acopen.10.2025.12858"
designation: algorithm-specific
title: "Goal Programming Model in Financial Planning of the International Development Bank"
authors: "Aboud, M. S. F."
year: 2025
venue: "Academia Open"
odin_topics: ["C.1", "C.2"]
shorthand_tags: ["/budget-rec-formulation", "/budget-alloc-algos", "/budget-algo-tradeoffs"]
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

Goal programming balances seven conflicting financial objectives (revenue, expenses, profit, assets, loans, equity, management ratio) with near-zero deviations for an Iraqi development bank.

## Problem and Motivation

Financial institutions struggle to balance multiple conflicting objectives like profit maximization, cost control, and liquidity under resource constraints. Traditional single-objective models cannot accommodate competing priorities, limiting planning efficiency. No prior study applied a hybrid weighted-preemptive goal programming model to a bank in an emerging market (Iraq) with a nine-year dataset.

## Approach

- Case study: International Development Bank for Investment and Finance (IDB), a private Iraqi bank.
- Data: Annual financial statements from 2016–2024 (9 years) scaled to billion IQD.
- Decision variables: X1 to X9 representing financial statement quantities for each year.
- Seven goal constraints: revenue (≥0.290878B), expenses (≤0.238279B), net profit (≥0.342094B), fixed assets (≥1.069823B), loans (≤0.684292B), common stock (≥0.337092B), financial management ratio (≥1.608461B).
- Method: Combined weighted and preemptive goal programming with priorities (revenue highest, management ratio lowest).
- Solver: WINQSB (linear goal programming).

## Findings

1. Optimal solution achieved all seven goals with only minor deviations (Z = 2.1553, not zero due to priority weighting).
2. Revenue shortfall (d1⁻) = 0.1884B — slightly below target.
3. Net profit shortfall (d3⁻) = 0.3006B — below allowable target.
4. Fixed assets exceeded target by **0.7833B** (d4⁺ positive deviation).
5. Loan reduction goal achieved fully (d5⁻ = d5⁺ = 0).

- Equity goal (common stock) fell short by 0.2956B (d6⁻ = 0.2956) — the only unmet target.
- Management ratio exceeded target by 1.1655B (d7⁺ positive).

## Key Figures and Tables

- Table 1: Raw financial data (2016–2024) in Iraqi dinars — shows annual revenues, expenses, net profit, fixed assets, loans, and common stock.
- Table 2: Scaled values in billion IQD — used as coefficients in the goal programming constraints.
- Figure (implicit): Objective function deviation results — shows d1⁻=0.1884, d3⁻=0.3006, d4⁺=0.7833, d6⁻=0.2956, d7⁺=1.1655.

## Key Equations

$$Min Z = \sum_{i=1}^{m} (w_i^- d_i^- + w_i^+ d_i^+)$$
*Minimize weighted sum of under-achievement and over-achievement across all goals.*

$$\sum_{j=1}^{n} a_{ij} X_j + d_i^- - d_i^+ = b_i$$
*Goal constraint: actual value plus negative deviation minus positive deviation equals target.*

$$Min Z = \sum_{i=1}^{p} M_i R (dev^- + dev^+)$$
*Preemptive method: higher-priority goals satisfied before lower-priority ones.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Goal Programming (GP) | A multi-objective optimization method that minimizes deviations from multiple targets rather than optimizing a single metric. |
| Negative Deviation (d⁻) | Amount by which actual value falls below the target. |
| Positive Deviation (d⁺) | Amount by which actual value exceeds the target. |
| Weighted Method | Assigns numeric importance weights to each deviation, then minimizes their weighted sum. |
| Preemptive Method | Ranks goals by priority; solves higher-priority goals completely before lower ones (lexicographic order). |
| WINQSB | Software solver for linear programming and goal programming models. |

## Critical Citations

- [Alam, 2022] — Foundational multi-objective financial planning model using goal programming for SABIC, establishing the methodological template.
- [AlArjani & Alam, 2021] — Lexicographic goal programming for bank performance management, directly informing the preemptive priority structure.
- [Nyor et al., 2022] — GP application to a Nigerian industrial goods firm, demonstrating emerging-market feasibility.
- [Lakshmi et al., 2021] — GP for financial planning in an Indian distribution company, validating LINGO-based solutions.

## Relevance to Odin

**Topics:**

C.1 — Budgeting Strategies and Budget Recommendation

C.2 — Budget Recommendation Algorithm

**Contribution to Odin:**

This paper directly informs Odin's budget recommendation module by demonstrating that goal programming (a multi-objective optimization method) can balance competing financial targets (revenue, expenses, profit, assets) under resource constraints. While the case study is an Iraqi bank, the algorithmic approach — weighted and preemptive goal programming — maps directly to Odin's problem of allocating a limited budget across spending categories while respecting priority constraints (e.g., savings first, then essentials, then discretionary). The paper provides a quantitative justification for using deviation-minimization over single-objective maximization when user goals conflict (e.g., "maximize savings" vs. "minimize expense tracking burden").

**Directly justifies:**

- "Goal programming achieves near-optimal financial plans under conflicting objectives by minimizing weighted deviations from multiple targets, as demonstrated on a nine-year bank dataset solved with WINQSB."
- "Preemptive goal programming — ranking goals by priority and satisfying higher-priority targets before lower ones — provides a mathematically sound mechanism for budget recommendation when users have non-negotiable savings or expense caps."
- "The weighted method allows differential importance assignment to under-achievement (d⁻) vs. over-achievement (d⁺), enabling Odin to penalize overspending more severely than undersaving."
- "Goal programming handles both upper-bound constraints (e.g., expenses ≤ target) and lower-bound constraints (e.g., revenue ≥ target) simultaneously, matching Odin's budget constraints (spending limits per category) and savings floors."

**Limits of relevance:**

- Domain mismatch: bank-level financial planning (institutional) vs. personal budget management (individual) — principles transfer, but scale and behavioral factors differ.
- Geography: Iraqi financial context; Filipino young professionals' spending patterns and income volatility not addressed.
- Method assumes static target values over time; Odin requires adaptive targets based on user spending history.
- No user interaction or behavioral feedback loop — the model is deterministic and not personalized beyond priority rankings.

## Limitations

- The paper does not compare goal programming against alternative multi-objective methods (e.g., Pareto optimization, evolutionary algorithms) — no benchmark for relative performance. [unacknowledged]
- Model assumes linear relationships between decision variables and goals; non-linear interactions (e.g., expense reduction indirectly increasing profit) are ignored. [unacknowledged]
- Data covers only one bank over nine years; generalizability to other financial institutions or personal finance contexts is untested.
- The paper acknowledges that the equity goal (common stock) was not fully achieved but does not explain why or how to adjust weights to satisfy it.
- WINQSB solver details (algorithm, convergence criteria) are not provided, limiting reproducibility.

## Remember This

- 🔑 **Seven conflicting goals balanced** — revenue, expenses, profit, assets, loans, equity, management ratio — with near-zero deviations on five of seven.
- 📌 Fixed assets exceeded target by **0.7833B IQD** — largest positive deviation, showing where the model over-delivered.
- ⚠️ Equity goal shortfall (d6⁻ = 0.2956) remained unresolved — priority weighting can leave lower-priority targets partially unmet.
- 💡 Hybrid weighted-preemptive GP offers a template for Odin's budget rec algorithm when users rank spending priorities.
- ✅ Goal programming minimizes deviation sums, not maximize profit — a fit for budgeting where "close enough" beats single-objective extremes.
