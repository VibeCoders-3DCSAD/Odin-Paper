# Optimizing Fleet Composition for Electric Vehicle Integration: A Case Study in the Philippines

## Metadata

```yaml
---
paper_id: "10.3390/engproc2026128029"
designation: algorithm-specific
title: "Optimizing Fleet Composition for Electric Vehicle Integration: A Case Study in the Philippines"
authors: "Ramos, L. G. O.; Rapada, L. A. M.; Umlas, D. L.; Kurata, Y. B."
year: 2026
venue: "Engineering Proceedings (MDPI)"
odin_topics: []
shorthand_tags: []
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

A hybrid AHP–linear programming model determined the optimal fleet mix for Philippine government EV transition: 54 BEVs, 50 HEVs, 1 PHEV, and 30 ICEs under PhP 273.3M procurement cap.

## Problem and Motivation

Government fleets in the Philippines must electrify by 2030, but rigid procurement processes and limited budgets prevent effective planning. Aligning sustainability goals with fiscal reality matters for public sector decarbonization. Prior approaches failed to integrate qualitative strategic criteria (emissions, range, technology maturity) into quantitative resource optimization.

## Approach

- Data: Baseline of 135 ICE vehicles (2025); 2030 target of ≥70% AFVs (≥95 units) from BEV, HEV, PHEV.
- Method 1: Analytic Hierarchy Process (AHP) with pairwise comparisons from experts to weight three criteria: emission (0.6434), range (0.2828), technology maturity (0.0738).
- Method 2: Integer Linear Programming (LP) using AHP-derived utility scores (BEV=0.5507, HEV=0.2933, PHEV=0.1572) as objective coefficients.
- Constraints: fleet size (135), AFV minimum (95), BEV bounds (9–54), annual fuel budget (PhP 8.2M), procurement budget (PhP 273.3M), repair/maintenance cap (PhP 6M), diversity cap (≤70% of AFVs per type).
- Solver: Branch and bound for integer solutions.

## Findings

1. Optimal fleet mix: 54 BEVs, 50 HEVs, 1 PHEV, 30 ICEs → **77.78% AFV penetration** (above 70% target).
2. BEV count hit upper bound (54 units) due to charging station capacity (2 BEVs per charger, charging every 3 days).
3. Objective value achieved: 44.5050.
- AHP preference order: BEV (0.5507) > HEV (0.2933) > PHEV (0.1572), driven by emission reduction priority.
- Removing BEV upper bound theoretically allows 70 BEVs and raises objective value by 6.5%.

## Key Figures and Tables

- Figure 1: AHP hierarchy (Goal → Criteria → Alternatives) → shows three criteria feeding three AFV types.
- Table 1: Input values by fuel type (capital, annual fuel cost, annual R&M cost) → BEV has highest capital ($48,776) but zero fuel cost.

## Key Equations

$$Z = 0.2922 X_{HEV} + 0.5507 X_{BEV} + 0.1572 X_{PHEV}$$
*Objective function: maximize weighted sum of AHP-derived utilities.*

$$X_{HEV} + X_{BEV} + X_{PHEV} \geq 95$$
*Mandatory AFV floor: at least 70% of 135 vehicles must be electric or hybrid.*

$$X_{BEV} \leq 54$$
*Charging infrastructure limits BEV fleet to 54 units under daily rotation.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| AHP | Analytic Hierarchy Process — a method that uses pairwise comparisons to weight decision criteria. |
| LP | Linear Programming — an optimization method that maximizes or minimizes an objective under linear constraints. |
| BEV | Battery Electric Vehicle — runs only on electricity, no internal combustion engine. |
| HEV | Hybrid Electric Vehicle — combines internal combustion engine with electric motor; cannot plug in. |
| PHEV | Plug-in Hybrid Electric Vehicle — hybrid that can recharge from an external power source. |
| ICE | Internal Combustion Engine — traditional gasoline or diesel vehicle. |
| AFV | Alternative Fuel Vehicle — any vehicle not running solely on gasoline/diesel (BEV, HEV, PHEV). |

## Critical Citations

- [Saaty, 2008] — Introduced AHP; this paper uses the principal eigenvector method and consistency ratio (CR=0.0564).
- [Bai et al., 2016] — Prior hybrid AHP–LP framework for sustainable fleet appraisal; directly informs this study’s methodology.
- [Cinar & Eren, 2019] — Integer LP applied to fleet assignment; supports branch-and-bound solver choice.

## Relevance to Odin

**Topics:**

None — contextual only.

**Contribution to Odin:**

This paper does not address personal finance, budgeting, spending behavior, or any of Odin's functional domains (financial profiling, forecasting, anomaly detection, expense categorization, mobile design, privacy, retention, or system evaluation). The methods (AHP and linear programming) are general-purpose optimization techniques, but the paper applies them exclusively to government vehicle fleet procurement. No claim, finding, or dataset in this paper supports any design decision or RRL argument for a personal budget management system.

**Directly justifies:**

None.

**Limits of relevance:**

- Domain mismatch: vehicle fleet optimization vs. personal finance management — no transferable claims.
- No user behavior data, transaction histories, or spending patterns — all inputs are vehicle technical specifications and budget caps.
- Population irrelevant: expert judgments from government fleet managers, not Filipino young professionals.
- Methodological analogy (LP for budget allocation) is too generic to cite; foundational LP texts would be more appropriate.

## Limitations

- No disaggregation by vehicle class (sedan, MPV, pickup) — limits logistics-specific planning. [unacknowledged]
- Static cost, maintenance, and infrastructure assumptions — does not account for price or technology changes over time.
- AHP weights reflect a fixed expert panel; different stakeholders would produce different outcomes.
- BEV charging constraint assumes every vehicle charges every 3 days — may not reflect real-world usage variance.
- Framework not validated against real operational data or pilot implementations.

## Remember This

- 🔑 **77.78% AFV penetration** — optimal mix: 54 BEV, 50 HEV, 1 PHEV, 30 ICE.
- ⚠️ BEV capped at 54 units by charger capacity — removing cap allows 70 BEVs (+6.5% objective).
- 📌 Emission criterion dominated AHP (weight 0.6434) — policy priorities override cost in this model.
- 🔍 Hybrid AHP–LP links qualitative expert judgments to integer-constrained resource allocation.
