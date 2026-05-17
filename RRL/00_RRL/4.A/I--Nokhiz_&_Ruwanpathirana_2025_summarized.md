# Consumer Autonomy or Illusion? Rethinking Consumer Agency in the Age of Algorithms

## Metadata

```yaml
---
paper_id: "10.23919/JSC.2025.0015"
designation: international
title: "Consumer Autonomy or Illusion? Rethinking Consumer Agency in the Age of Algorithms"
authors: "Nokhiz, P.; Ruwanpathirana, A. K."
year: 2025
venue: "Journal of Social Computing"
odin_topics: ["1.C", "4.B", "5.A", "7.A"]
shorthand_tags: ["/budget-failure-points", "/pfms-limitations", "/profile-dimensions", "/strategy-mechanics", "/budgeting-evidence"]
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

Even rational utility‑maximizing consumers face early financial ruin when agency is constrained by obligatory payments, algorithmic manipulation, or unstable work schedules.

## Problem and Motivation

Digital ecosystems impose systemic barriers (mandatory subscriptions, hidden fees) and manipulative tactics (personalized recommendations, BNPL) that undermine consumers’ ability to make value‑aligned spending decisions. This erosion of agency leads to impulsive purchases, poor financial planning, and increased risk of bankruptcy. Prior work had not formally linked limited agency to measurable financial instability across structural, behavioral, and temporal dimensions.

## Approach

- Formal framework: discounted utility model with concave utility (CRRA family) and asset non‑negativity constraint.
- Three agency‑constraint scenarios analyzed analytically: (1) fixed obligatory consumption, (2) minimum subsistence + algorithm‑driven impulsive consumption, (3) unpredictable income from unstable work schedules (lookahead vs. no lookahead).
- Ruin defined as assets falling to zero or below within finite time.
- Solution modeling: value deliberation (prioritizing needs, budgeting leftover for discretionary spending) and policy interventions (schedule notice requirements).

## Findings

1. Under fixed obligatory consumption, concave utility forces ruin regardless of initial wealth — no consumption path avoids finite‑horizon bankruptcy.
2. With impulsive consumption and minimum subsistence, ruin probability decreases **exponentially with time** — e.g., probability of avoiding ruin at time \(T\) is \(\le e^{-cT}\) for constant \(c>0\).
3. A worker with \(k\)‑step lookahead (advance schedule knowledge) achieves utility at least \(\Omega(k)\) higher than a worker with no lookahead, even when both behave optimally.

- Mandatory “value deliberation” (allocating funds first to essentials, then to discretionary spending) allows infinite‑horizon utility maximization without ruin.
- Regulatory advance‑notice policies (e.g., Schedules that Work Act) directly improve financial utility by enabling better planning.

## Key Figures and Tables

- Figure 1: Conceptual flowchart of three scenarios (obligatory consumption, algorithmic persuasion, work scheduling) and their path to limited agency → lower financial welfare and early ruin.

## Key Equations

$$ \max_{R_t, y_t} \mathbb{E}\left[ \sum_{t=0}^{\infty} \beta^t u(c_t) \right] \quad \text{s.t. } a_{t+1} = R_t(a_t - c_t) + y_t,\; 0 < c_t \le a_t $$
*Discounted utility maximization with asset evolution and no borrowing.*

$$ \Pr(a_T \le 0) \ge 1 - e^{-cT} \quad \text{where } c = \frac{(B-Y)^2}{8(d+e)^2} $$
*Under impulsive consumption, ruin probability approaches 1 exponentially fast as time horizon \(T\) grows.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Discounted utility | Total future utility where each period’s utility is multiplied by a discount factor \(\beta < 1\) (people value immediate rewards more). |
| Ruin | State where assets become zero or negative, preventing further consumption. |
| Obligatory consumption | Mandatory spending driven by legal, social, or infrastructure constraints (e.g., subscriptions, taxes, fees). |
| Algorithmic persuasion | Digital tactics (personalized recs, scarcity alerts, BNPL) that push impulsive purchases. |
| Lookahead | How many future time steps of income/schedule the agent knows with certainty. |
| Value capture | Adopting externally imposed consumption values without critical reflection. |
| Minimum subsistence | Lower bound on consumption needed for basic living (food, shelter). |

## Critical Citations

- [Pariser, 2011] — Introduced filter bubbles, foundational for algorithmic manipulation of choice.
- [Nguyen, 2024] — Developed “value capture” framework used to explain how consumers adopt external values.
- [Schneider & Harknett, 2019] — Empirical work on work‑schedule instability and financial harm, grounding the temporal agency scenario.
- [Frederick et al., 2002] — Standard reference on time discounting, used to set the model’s discount factor assumptions.

## Relevance to Odin

**Topics:**

1.C — Financial Behavior of Filipino Young Professionals

4.B — Limitations and Gaps in Existing Systems

5.A — Financial Behavioral Profiles in Personal Finance

7.A — Budgeting Strategies as Domain Knowledge

**Contribution to Odin:**

This paper formally demonstrates that constrained agency (obligatory payments, manipulative nudges, income unpredictability) leads to measurable financial ruin — a finding that justifies Odin’s need to model user‑specific constraints rather than assume rational, unconstrained behavior. The three‑dimensional typology (structural, behavioral, temporal) directly informs Odin’s financial behavioral profiling module, providing a classification framework based on the sources of agency limitation. The proposed solution of “value deliberation” (prioritizing essential expenses before discretionary spending) offers a budgeting strategy that Odin can implement as a recommendation heuristic, supported by the paper’s proof that such deliberation avoids ruin under concave utility.

**Directly justifies:**

- “Even utility‑maximizing consumers go to ruin under fixed obligatory consumption (subscriptions, hidden fees) — personal finance systems must explicitly model mandatory expenses as non‑negotiable constraints.”
- “Algorithm‑driven impulsive consumption causes ruin probability to approach 1 exponentially with time; therefore, anomaly detection for overspending is not optional but essential for financial stability.”
- “Work schedule unpredictability reduces financial utility by at least \(\Omega(k)\) — a Philippine PFMS must account for income volatility when recommending budgets.”
- “Value deliberation (allocating essentials first, then discretionary) allows infinite‑horizon consumption without ruin, justifying budgeting strategies that enforce this priority order.”
- “Three distinct agency constraint types (structural, behavioral, temporal) form a usable taxonomy for constructing financial behavioral profiles.”

**Limits of relevance:**

- Paper is theoretical (proofs, no empirical user study); results are asymptotic and probabilistic, not calibrated to Philippine income or expense data.
- The model assumes no debt or borrowing; real‑world consumers use credit, which may delay ruin but add interest burdens.
- “Work schedule instability” examples are U.S.‑centric (retail, food service); applicability to Filipino gig economy needs validation.
- No evaluation of value deliberation in live systems — the solution is proven mathematically, not user‑tested.

## Limitations

- Model excludes debt, credit cards, and BNPL as access to negative assets — a major real‑world mechanism that can mask or delay ruin. [unacknowledged]
- Assumes rational, utility‑maximizing agents; behavioral biases (present bias, loss aversion) are not modeled, likely underestimating ruin risk.
- No empirical validation — all results are analytical; real income distributions and consumption patterns may deviate from assumptions.
- Societal uniformity assumed; does not address differential targeting by algorithms based on race, income, or education.
- Work schedule analysis abstracts away labor law enforcement gaps in the Philippine context. [unacknowledged]

## Remember This

- 🔑 **Ruin probability decays exponentially** — once average consumption exceeds average income, bankruptcy is nearly certain in finite time.
- 📌 **Three agency killers**: obligatory payments, manipulative algorithms, and unpredictable schedules — each mapped to a distinct formal result.
- 💡 **Value deliberation works** — allocating essentials first, then discretionary, mathematically avoids ruin under concave utility.
- ⚠️ **No debt in the model** — real consumers use credit, which the paper does not address; findings may underestimate actual risk.
- 🧠 **Lookahead matters** — knowing your work schedule \(k\) weeks ahead yields \(\Omega(k)\) higher utility; regulation like two‑week notice rules is directly justified.
