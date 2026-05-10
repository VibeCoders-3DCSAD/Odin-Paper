# Dynamic Model for Budget Allocation in via Multi-Criteria Optimization

## Metadata

```yaml
---
paper_id: "10.47738/jads.v6i4.935"
designation: algorithm-specific
title: "Dynamic Model for Budget Allocation in via Multi-Criteria Optimization"
authors: "Gulbakyt, S.; Almaz, A.; Saule, S.; Suhrab, Y."
year: 2025
venue: "Journal of Applied Data Sciences"
odin_topics: ["C.2"]
shorthand_tags: ["/budget-rec-formulation", "/budget-alloc-algos", "/budget-algo-tradeoffs"]
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

Multi-criteria optimization with SQP and GA allocates a regional budget across seven sectors, achieving near-identical objective values (0.0007% difference) and a Gini coefficient of 0.223.

## Problem and Motivation

Kazakhstan’s regional budget allocation is opaque and inefficient, lacking public participation and data-driven tools. Poor allocation worsens socioeconomic disparities and erodes trust in local government. Prior work did not integrate citizen satisfaction, strategic priorities, basic needs, and urbanization into a single optimization framework.

## Approach

- Dataset: Four districts in Almaty region (Raimbeksky, Karasaysky, Talgarsky, Kegensky) with total budget 42,656,543 thousand tenge across seven activity areas (education, healthcare, transport, infrastructure, digitalization, culture, ecology).
- Method: Quadratic programming with Sequential Quadratic Programming (SQP) in MATLAB’s fmincon, and Genetic Algorithm (GA) in Python’s DEAP library.
- Criteria weights: citizen satisfaction (0.2), strategic priorities (0.2), basic needs (0.3), urbanization level (0.3). Weights set by expert judgment.
- Constraints: Equality (sum of allocations equals total budget), inequality (sectoral shares limited), and variable bounds (min/max per district-activity).
- Inputs: Synthetic citizen votes derived from population demographics, strategic priority multipliers (1.0–2.1), urbanization coefficients (20–65%), and demographic data from Kazakhstan’s statistics bureau.

## Findings

1. SQP achieved objective function value **18,519,864.85** thousand tenge; GA reached 18,520,000.00 thousand tenge — a difference of 135.15 thousand tenge (0.0007% of total budget).
2. Healthcare received 22.05% of the budget, transport 21.11%, education 7.03% (smallest), and infrastructure 11.26%.
3. Fairness metrics: standard deviation of sectoral shares = 5.69%, coefficient of variation = 0.398, **Gini coefficient = 0.223**.

- SQP converged in under 100 iterations; GA required 500 generations but avoided local optima.
- Both methods funded all seven activity areas, unlike linear programming (which omitted some) or level balancing (which ignored strategic priorities).

## Key Figures and Tables

- Figure 2: Budget allocation result by district and activity → healthcare and transport dominate; education smallest across all districts.
- Figure 5: Convergence of objective function during SQP optimization → rapid improvement from 16.5M to 18.52M tenge in first iteration.
- Figure 6: Budget distribution obtained using GA → similar to SQP, with slightly higher education in Raimbeksky.
- Table 4: Numerical results (thousands tenge) per district and category → precise allocations (e.g., Karasaysky healthcare = 3,082,251.69).
- Table 6: Comparative characteristics of SQP and GA methods → SQP: deterministic, fast, high accuracy; GA: stochastic, slow, robust to local minima.

## Key Equations

$$ \min \left( \frac{1}{2} x^T Q x + c^T x \right), \quad \text{s.t. } A_{eq}x = b_{eq},\ A_{ineq}x \leq b_{ineq} $$
*Quadratic programming formulation with linear equality and inequality constraints.*

$$ \text{Objective} = \max \left( \alpha \sum \frac{V_{i,j}}{\max(V)} B_{i,j} + \beta \sum \frac{W_{i,j}}{\max(W)} B_{i,j} + \gamma \sum \mathbf{1}(B_{i,j} \geq B_{\min i,j}) + \delta \sum \frac{U_i}{\max(U)} B_{i,j} \right) $$
*Weighted sum of citizen votes, strategic priorities, basic needs satisfaction, and urbanization.*

$$ B_{\min,i} = k_{\text{pop}} \times \text{Population}_i + k_{\text{urban}} \times \text{Urbanization}_i + k_{\text{income}} \times \text{Income}_i, \quad B_{\max,i} = \alpha \times B_{\min,i} $$
*Minimum budget from population, urbanization, income; maximum as a multiplier of minimum.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| SQP | Sequential Quadratic Programming — an algorithm that solves nonlinear optimization by approximating the problem as a quadratic subproblem at each step. |
| GA | Genetic Algorithm — an evolutionary search method that mimics natural selection to find optimal solutions. |
| AA | Area of Activity — one of seven spending categories (education, healthcare, transport, infrastructure, digitalization, culture, ecology). |
| CU | Urbanization coefficient — ratio of urban to total population in a district [hint: higher CU means more demand for complex services]. |
| fmincon | MATLAB function for constrained nonlinear optimization, used here with the SQP method. |
| DEAP | Distributed Evolutionary Algorithms in Python — library used to implement the GA. |

## Critical Citations

- [Gulbakyt & Abdualiyev, 2024] — Prior linear programming and level-balancing models that this paper extends with multi-criteria optimization.
- [Bartocci et al., 2023] — Systematic review of participatory budgeting, justifying the inclusion of citizen satisfaction as a criterion.
- [Blank & Deb, 2020] — Introduces Pymoo, a modern Python library for multi-objective optimization cited for future constraint handling improvements.
- [Mazelis et al., 2021] — Dynamic model for regional human capital investment, similar constraint-based approach used as methodological reference.

## Relevance to Odin

**Topics:**

C.2 — Budget Recommendation Algorithm

**Contribution to Odin:**

This paper directly informs Odin’s budget recommendation module by demonstrating how multi-criteria optimization (SQP and GA) can allocate a constrained budget across competing categories. The comparison of deterministic (SQP) versus stochastic (GA) methods provides a design trade-off for Odin: SQP offers fast, precise solutions suitable for near-real-time recalculation, while GA provides robustness against local optima at higher computational cost. Although the domain is regional government, the mathematical formulation — weighted criteria subject to min/max bounds and equality constraints — maps directly to personal budget allocation where users have income limits, fixed expenses, and variable priorities.

**Directly justifies:**

- “SQP achieves rapid convergence (under 100 iterations) for constrained quadratic programming problems, making it suitable for real-time budget recalculations in mobile personal finance apps.”
- “GA reaches near-identical solutions to SQP (0.0007% difference) but requires 500 generations, trading speed for global search robustness — useful when user preferences are uncertain or non-convex.”
- “Multi-criteria optimization with weighted citizen satisfaction, strategic priorities, basic needs, and urbanization produces a Gini coefficient of 0.223, indicating equitable resource distribution across sectors — a fairness metric applicable to evaluating budget recommendation algorithms.”
- “Constraint-based allocation with min/max bounds ensures all categories receive at least a minimum threshold (basic needs) and no category dominates excessively, directly analogous to protecting essential spending categories (e.g., food, rent) in personal budgets.”

**Limits of relevance:**

- Domain is regional public sector budgeting (Kazakhstan), not personal finance; behavior of users vs. citizens differs.
- Synthetic citizen voting data — no real preference elicitation; Odin would need actual user input.
- Weights (0.2,0.2,0.3,0.3) are expert-defined without sensitivity analysis; Odin would require user-adaptable or learned weights.
- No validation with real-world budget outcomes; the model remains conceptual pending pilot testing.

## Limitations

- No real-world pilot deployment; conclusions about practical feasibility are preliminary — acknowledged by authors.
- Citizen voting data is synthetic (derived from demographics, not actual votes), limiting external validity — acknowledged.
- Non-zero constraint violation (≈865,100 tenge, 0.47% of budget) remained at final SQP iteration — acknowledged.
- Weight coefficients lack formal sensitivity analysis; alternative weight sets might produce different allocations — [unacknowledged].
- Comparison to baseline models (level balancing, linear programming) is qualitative only; no quantitative error metrics (RMSE, MAE) due to lack of disaggregated real budget data — acknowledged.

## Remember This

- 🔑 SQP and GA differ by just **0.0007%** — both reliably solve multi-criteria budget allocation.
- 📌 Gini coefficient **0.223** — model achieves equitable distribution across 7 sectors with no category zeroed out.
- ⚠️ Synthetic citizen votes (not real data) — limit for personal finance generalization.
- 💡 Healthcare (22%) and transport (21%) get largest shares due to strategic weights — shows how criteria drive outcomes.
- 🧠 SQP converges in <100 iterations; GA needs 500 generations — speed vs. robustness trade-off for Odin’s budget rec module.
