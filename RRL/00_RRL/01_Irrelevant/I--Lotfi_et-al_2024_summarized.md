# Budget allocation problem for projects with considering risks, robustness, resiliency, and sustainability requirements

## Metadata

```yaml
---
paper_id: "10.1016/j.rineng.2024.102828"
designation: international
title: "Budget allocation problem for projects with considering risks, robustness, resiliency, and sustainability requirements"
authors: "Lotfi, R.; Vaseei, M.; Ali, S. S.; Davoodi, S. M. R.; Bazregar, M.; Sadeghi, S."
year: 2024
venue: "Results in Engineering"
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

A hybrid robust stochastic optimization model integrating risk, robustness, resiliency, and sustainability reduces project progress by 13.5% but ensures budget stability under uncertainty.

## Problem and Motivation

Large national projects face critical budget allocation risks that can delay completion and affect public welfare. Existing budget allocation methods ignore the combined effects of uncertainty, disruptions, and sustainability requirements. No prior model simultaneously addressed robustness, resiliency, risk-aversion, and sustainability in project budget allocation.

## Approach

- **Data**: Case study of 8 national projects in Iran under 3 scenarios (optimistic, probable, pessimistic) with stochastic parameters (budget, claims, progress).
- **Model**: Mixed-integer linear programming (MILP) formulation called S3RBAP with robust stochastic optimization.
- **Risk criteria**: Weighted VaR (WVaR) combining VaR, CVaR, and EVaR plus a min‑function to ensure robustness of the objective.
- **Constraints**: Budget limits with a resiliency coefficient (δ), sustainability via minimum occupation level (ocu), and linear progress assumption.
- **Evaluation**: Sensitivity analysis on conservatism coefficient (β), resiliency coefficient (δ), problem scale, and nonlinear S‑curve progress functions.

## Findings

1. Incorporating 3R (robustness, resiliency, risk) and sustainability reduced the progress function by **13.5%** compared to ignoring them (86.4% vs 98.1%).
2. Increasing conservatism (β) from 0% to 20% decreased progress by 1.0 percentage point (86.9% → 85.9%).
3. Lowering resiliency (δ) from 80% to 60% dropped progress by 1.5% and reduced occupation (498 → 438 persons).
4. Scaling up to 100 projects × 9 scenarios increased computation time smoothly (0.225 → 0.302 sec) but progress fell to 77.6%.

- Exponential progress functions produced risk‑averse behavior (82.9% progress), while sine functions produced risk‑seeking behavior (92.4% progress).

## Key Figures and Tables

- Figure 5: Budget assignment across 8 projects → uneven distribution favoring projects with higher weight factors.
- Table 4: Comparison with/without 3R + sustainability → 13.5% progress reduction, 20.3% occupation reduction.
- Figure 7: Progress vs conservatism coefficient → near‑linear decline from 86.9% to 85.9% over 0–20% β.
- Table 8: S‑curve function comparison → sine yields highest progress (92.4%), exponential lowest (82.9%).
- Figure 11: Progress for large‑scale problems → declines from 86.4% (8 projects) to 77.6% (100 projects).

## Key Equations

$$Z = (1 - \beta)\Gamma\Gamma + \beta \frac{\Gamma'' + \text{WVaR}(\varepsilon)}{2}$$
*Objective function balances expected progress, minimum progress, and weighted risk.*

$$\text{WVaR}(\varepsilon) = \Gamma\Gamma + \omega_1 \left( z_{1-\alpha} \right) \sigma + \omega_2 \frac{\phi(z_{1-\alpha})}{\alpha} \sigma + \omega_3 \sqrt{-2\ln(\alpha)} \sigma$$
*Combined risk measure using VaR, CVaR, and EVaR under normality.*

$$\sigma = \sum_s p_s |\Gamma\Gamma - \Gamma'_s|$$
*Mean absolute deviation of progress across scenarios.*

$$\text{prBap}_{is} = \left( \frac{x_{is}}{\text{bacrcc}_{is}} \right)^n (1 - \text{pr}_{is}) + \text{pr}_{is}$$
*Linear (n=1) progress function from allocated budget.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| BAP | Budget Allocation Problem – distributing a fixed budget across projects. |
| 3R | Robustness, Resiliency, Risk – three pillars for handling uncertainty. |
| S3RBAP | Sustainable, Robust, Resilient, Risk‑averse Budget Allocation for Projects – the proposed model. |
| WVaR | Weighted Value at Risk – composite risk measure (VaR + CVaR + EVaR). |
| MILP | Mixed‑Integer Linear Programming – optimization with both continuous and integer variables. |
| MINLP | Mixed‑Integer Non‑Linear Programming – harder problem with nonlinear terms. |
| Conservatism coefficient (β) | Weight on risk terms vs expected value in the objective. |
| Resiliency coefficient (δ) | Factor that relaxes total budget to absorb disruptions. |

## Critical Citations

- [Lotfi et al., 2023] – Prior 3RBAP model for healthcare projects; this paper extends it with sustainability.
- [Jemmali, 2021] – Lower bounds and heuristics for equity‑based budget assignment.
- [Yu et al., 2023] – Budget allocation policy for tabu search in stochastic simulation optimization.

## Relevance to Odin

**Topics:**

None — contextual only.

**Contribution to Odin:**

This paper does not address personal finance systems, spending behavior, or any of Odin’s functional domains (profiling, forecasting, budget recommendation, anomaly detection, mobile UX, privacy, retention, evaluation). The methods focus on large‑scale national project portfolio management under uncertainty, not individual budget management. No algorithm, dataset, or finding transfers to a personal budget management system for Filipino young professionals.

**Directly justifies:**

None.

**Limits of relevance:**

- Domain mismatch: project portfolio budgeting vs personal consumer budgeting.
- No behavioral or categorical spending data – only physical project progress metrics.
- Objective is maximizing project progress, not adherence to spending limits or user welfare.
- All constraints (budget at completion, remaining claims, occupation) are irrelevant to personal finance.

## Limitations

- Model assumes linear progress per budget unit, which is unrealistic for most projects (acknowledged, then replaced with S‑curves).
- Case study uses only Iranian national projects – no external validation.
- Nonlinear S‑curve variants become MINLP and require heuristics; solution optimality not guaranteed. [unacknowledged]
- No comparison with alternative optimization methods (e.g., genetic algorithms, particle swarm).
- Assumes decision‑maker can set project weight factors subjectively, introducing potential bias.

## Remember This

- 📌 **13.5% progress reduction** when adding 3R + sustainability – robustness costs performance.
- 🔍 Sine S‑curve gives 92.4% progress (risk‑seeking); exponential gives 82.9% (risk‑averse).
- ⚠️ No relevance to personal finance – this is project portfolio budgeting, not individual spending.
- 💡 Increasing conservatism (β) from 0% to 20% cuts progress by only 1%, a small trade‑off.
