# Hybrid Greedy-Dynamic Programming Approach for Multi-Criteria Weighted Activity Selection

## Metadata

```yaml
---
paper_id: "5f4d3c2b-1a0e-4d6c-8f9a-7b6e5d4c3b2a"
designation: algorithm-specific
title: "Hybrid Greedy-Dynamic Programming Approach for Multi-Criteria Weighted Activity Selection"
authors: "Espina, J. C.; Anino, G. M.; Antonio, D. J.; Landicho, J."
year: 2025
venue: "Unknown"
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

Hybrid greedy-dynamic programming achieves **42-48% assignment rates** and fairness >0.94 Jain's index across scheduling problems, with sub-100ms runtime.

## Problem and Motivation

Existing multi-person weighted activity selection methods either sacrifice overall value for fairness or maximize value while ignoring equitable distribution. Real-world scheduling (healthcare, conferences, project management) requires both high-value task allocation and fair workload sharing among participants. No prior integrated approach simultaneously optimizes both criteria in a scalable, computationally efficient way.

## Approach

- Three-phase algorithm: initial greedy allocation (value-to-finish-time ranking + least-loaded participant), dynamic programming refinement (weighted interval scheduling per participant per time slot), fairness optimization (iterative reassignment from over-allocated to under-allocated participants).
- Evaluated on synthetic datasets (50–500 activities, 5–15 participants), benchmark instances (ScheduleNet job shop), and real-world case studies (hospital scheduling, conference management, software project allocation).
- Performance metrics: total weighted value, normalized deviation fairness metric, Jain’s fairness index, assignment rate, runtime, makespan.
- Baseline comparisons: pure greedy, pure dynamic programming, ScheduleNet (reinforcement learning).
- Implementation in C++ with sub-100ms target; adaptive fairness tolerance parameter based on weight distribution statistics.

## Findings

1. Assignment rates reached **42-48%** across all synthetic datasets after Phase 2, compared to 6-14% after pure greedy and 8-9% for pure DP on large-scale problems.
2. Final Jain’s fairness index exceeded **0.94** across synthetic datasets, reaching 0.981 for the most balanced case.
3. HGDP outperformed ScheduleNet on makespan by **10x to 23x** (e.g., 100 vs. 5,879) with runtime under 312ms even for 100x20 instances.
4. Real-world value improvements: +101% in healthcare resource allocation, +65% in conference scheduling, +32% in project management.
5. Fairness recovery after Phase 2 was complete in all cases, with final fairness scores of 0.64–0.88 and Jain’s index 0.89–0.986.

## Key Figures and Tables

- Table 1: Phase-by-phase metrics → Assignment rates jump from 6-14% (greedy) to 42-48% (DP), fairness dips then recovers above 0.94 Jain.
- Table 2: Pure vs. HGDP → At 500 activities, HGDP achieves 48% assignment vs. 8% for pure DP; total weight 47,905 vs. 4,301.
- Table 3: ScheduleNet benchmark → HGDP makespan ~100 vs. SN’s 1,047–5,879; improvement 11x–59x.
- Table 4: Real-world case studies → Hospital-RW value improves 101% (5,779 → 11,622) with final fairness 0.64.
- Fig. 2: Fairness and Jain’s index comparison → HGDP converges to >0.94 Jain across all synthetic datasets.

## Key Equations

$$\max \sum_{i=1}^{n} w_i \cdot y_i$$
*Maximize total weight of selected activities, where y_i is 1 if activity i is assigned.*

$$F(\phi) = 1 - \frac{\sum_{j=1}^{m} (v_j - v_{avg})^2}{m \cdot v_{avg}^2}$$
*Normalized deviation metric; ranges 0 (worst) to 1 (perfect fairness).*

$$OPT(i) = \max(w_i + OPT(p(i)),\; OPT(i-1))$$
*Dynamic programming recurrence for weighted interval scheduling; p(i) is latest non-overlapping activity before i.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| ASP | Activity Selection Problem – choose maximum number of non-overlapping activities. |
| WASP | Weighted Activity Selection Problem – maximize total value instead of count. |
| Jain’s fairness index | Standard resource-allocation equity metric; 1 = perfectly equal, 1/m = worst. |
| Makespan | Total duration from earliest start to latest finish of scheduled activities. |
| Fairness tolerance ε | Maximum allowed deviation from equal value distribution across participants. |
| HGDP | Hybrid Greedy-Dynamic Programming – the proposed three-phase algorithm. |

## Critical Citations

- [Cormen et al., 2009] — Classic greedy algorithm for ASP; foundation for Phase 1’s value-to-finish-time ranking.
- [Sviridenko et al., 2014] — Provides (1-1/e)-approximation guarantee for submodular optimization with bounded curvature, used for theoretical bound.
- [Liu et al., 2023] — Deep multi-agent RL for job shop scheduling; benchmark for comparison and motivation for hybrid approach.
- [Park et al., 2021] — ScheduleNet; direct benchmark for makespan comparison (10-23x improvement claimed).

## Relevance to Odin

**Topics:**
None — contextual only.

**Contribution to Odin:**
This paper does not address any of Odin’s functional domains (financial behavioral profiling, spending forecasting, budget recommendation, anomalous spending detection, expense categorization, mobile-first design, data privacy, user retention, or system evaluation). Its focus on activity scheduling, resource allocation, and fairness among participants has no direct application to personal budget management. The algorithm’s core constraints (non-overlapping time intervals, resource capacities) do not map to any Odin module.

**Directly justifies:**
None.

**Limits of relevance:**
None identified.

## Limitations

- Scalability of fairness optimization: runtime increased to 68ms for 500 activities, potentially prohibitive for thousands of activities.
- Extreme sensitivity to problem structure: assignment rate dropped to 1.75% on job shop datasets with exclusive resources and precedence constraints. [unacknowledged]
- Consistent 42-48% assignment rate ceiling – may be insufficient for applications requiring >70% utilization.
- Temporal inconsistency: fairness intentionally drops during Phase 2 (e.g., 0.53 → 0.40 in Hospital-RW) before recovery; early termination yields poor fairness.
- Assumes static participant set and indivisible activities; no validation for dynamic environments (e.g., participants joining/leaving).

## Remember This

- 🔑 **42-48% assignment rate** – HGDP’s consistent coverage ceiling across scales and distributions.
- 📌 Fairness recovery: Phase 3 raises Jain’s index from ~0.78 to >0.94 in all synthetic cases.
- ⚠️ Problem structure matters: flexible resource sharing yields 36% assignment; rigid job shops yield <2%.
- 💡 Runtime <100ms for 500 activities – suitable for near-real-time scheduling.
- 🔍 101% value improvement in healthcare – domain-specific gains vary widely (101% vs. 32% in project management).
