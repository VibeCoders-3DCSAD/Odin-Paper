# An Enhancement of Particle Swarm Optimization Algorithm Applied in Sowing and Harvesting Periods Recommendation System

## Metadata
```yaml
---
paper_id: "10.2139/ssrn.6467398"
designation: algorithm-specific
title: "An Enhancement of Particle Swarm Optimization Algorithm Applied in Sowing and Harvesting Periods Recommendation System"
authors: "Reyes, F.; Layson, D."
year: 2026
venue: "Pamantasan ng Lungsod ng Maynila (Bachelor's Thesis)"
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

An enhanced Particle Swarm Optimization with angular diversity, Page-Hinkley drift detection, and lexicase archiving achieved 93.33% success rate on agricultural scheduling, reducing climate risk by 11.32%.

## Problem and Motivation

Standard Particle Swarm Optimization (PSO) suffers from premature convergence, static control parameters, and single‑objective incompatibility, making it unreliable for volatile agricultural planning. This matters because static planting calendars cannot adapt to climate shifts, threatening food security in Nueva Ecija. Prior PSO variants lacked integrated mechanisms for spatial diversity maintenance, dynamic change detection, and true multi‑objective Pareto front approximation.

## Approach

- Dataset: 30‑year historical climate data (PAGASA, Open‑Meteo), soil properties (BSWM), rice phenology (NSIC Rc222), and typhoon records for Nueva Ecija.
- Baseline: Standard PSO with inertia weight 0.729, cognitive/social coefficients 1.494.
- Enhancement 1: Angular Poisson Disk Sampling – reorients worst 20% of particles into sparse directional bins while preserving speed.
- Enhancement 2: Page‑Hinkley Adaptive Trigger – monitors global fitness drift; upon detection, re‑initializes 50% of particles (quantum re‑initialization).
- Enhancement 3: Lexicase Micro‑Archiving with crowding distance – stores non‑dominated solutions; selects leaders by shuffling objective priorities.
- Validation: 30 independent runs on unimodal (Sphere), multimodal (Rastrigin), shifted Rastrigin, Rosenbrock, and multi‑objective benchmarks (ZDT1/ZDT2).

## Findings

1. Enhanced PSO reduced mean Rosenbrock error from **3,034.21 to 31.07** – a 99.0% improvement.
2. Page‑Hinkley detection latency was **13.7 iterations** vs. baseline’s 250‑iteration timeout (94.5% faster).
3. Post‑shift mean error dropped from 78,146.98 to 8,638.31 – **88.95% error reduction**.
4. Hypervolume increased from 22.345 to 24.492 – **9.6% broader objective space coverage**.
5. Spacing error fell from 0.0753 to 0.0134 – **82.2% more uniform Pareto front**.
- Yield improved 8.06% over static calendar (5.36 vs 4.96 t/ha); climate risk reduced from 12.73% to 1.41%.
- Integrated system achieved **93.33% success rate** (error <10k) vs. 0% for baseline.

## Key Figures and Tables

- Figure 4.1‑A: Hypervolume and spacing recovery after environmental shift → integrated system re‑converges; baseline flatlines.
- Figure 4.1‑C: Pareto frontier (Yield Loss vs. Risk) → baseline collapses to clusters; enhanced spreads uniformly.
- Table 4.1‑A: Descriptive statistics → enhanced: mean HV 24.492 (SD 0.0976), spacing 0.0134 (SD 0.0024).
- Table 4.2.2‑A: Dynamic adaptability → reaction latency 13.7, recovery rate 273.67, post‑shift error 8,638.31.
- Table 4.2.4‑A: Multi‑objective metrics → enhanced F5 spacing 0.0049 vs. baseline 0.8000.

## Key Equations

$$V_i^{t+1} = w V_i^t + c_1 r_1 (pbest_i - X_i^t) + c_2 r_2 (gbest - X_i^t)$$
*Standard PSO velocity update: inertia + cognitive + social terms.*

$$f_1(x) = \sum_{d=1}^{D} x_d^2$$
*Sphere function – unimodal test for convergence stability.*

$$f_2(x) = 10D + \sum_{d=1}^{D} (x_d^2 - 10\cos(2\pi x_d))$$
*Rastrigin function – multimodal test for escaping local optima.*

$$f_{dyn}(x,t) = f_{Rastrigin}(x + s(t))$$
*Shifted Rastrigin – dynamic benchmark with landscape change at iteration 250.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| PSO | Particle Swarm Optimization – swarm of candidate solutions updating positions via personal and global bests. |
| Premature convergence | Swarm collapses to a suboptimal local optimum before exploring the whole search space. |
| Angular Poisson Disk Sampling | Diversity mechanism that reorients stagnant particles toward less crowded headings without changing speed. |
| Page‑Hinkley test | Sequential change‑detection method that triggers a reset when cumulative fitness deviation exceeds a threshold. |
| Lexicase selection | Leader selection that randomly shuffles objective priorities, preserving diverse trade‑offs. |
| Hypervolume (HV) | Volume of objective space dominated by the Pareto front – higher is better. |
| Spacing (SP) | Uniformity metric of Pareto front distribution – lower is better. |

## Critical Citations

- [Kennedy & Eberhart, 1995] – Introduced canonical PSO; foundation for all swarm comparisons.
- [Clerc & Kennedy, 2002] – Constriction factor (χ=0.729) used in baseline to balance exploration/exploitation.
- [Jordehi, 2015] – ELPSO successive mutation; inspects leader‑enhancement strategies.
- [Zitzler et al., 2000] – Hypervolume and spacing metrics for multi‑objective evaluation.

## Relevance to Odin

**Topics:**

None — contextual only.

**Contribution to Odin:**

This paper presents generic algorithmic enhancements for swarm intelligence that could inform Odin’s design if optimization modules (e.g., hyperparameter tuning, multi‑objective budget allocation) are implemented. The Angular Poisson Disk Sampling mechanism demonstrates how to maintain diversity and prevent premature convergence in multimodal spaces. The Page‑Hinkley trigger provides a lightweight, model‑agnostic change‑detection method applicable to concept drift in user spending behavior. The Lexicase micro‑archiving with crowding distance offers a principled way to handle multiple conflicting objectives (e.g., savings vs. discretionary spending) without collapsing to a single scalar. However, the paper applies these techniques to agricultural biophysical models, not personal finance data, so direct transfer requires re‑implementation and validation on financial transaction sequences.

**Directly justifies:**

- "Angular Poisson Disk Sampling reorients the worst‑performing 20% of particles into sparser directional bins, preserving speed while preventing premature swarm collapse."
- "The Page‑Hinkley Adaptive Trigger detects environmental shifts with 13.7‑iteration latency, achieving 88.95% post‑shift error reduction."
- "Lexicase selection with crowding distance produces a uniformly distributed Pareto front, reducing spacing error by 82.2% on non‑convex benchmarks."

**Limits of relevance:**

- Domain is rice agriculture (Nueva Ecija), not personal finance; no transaction or spending data.
- Algorithm validated on biophysical simulations (yield, water deficit, typhoon risk), not on financial objectives (e.g., savings rate, debt reduction).
- The paper is a preprint bachelor’s thesis, not peer‑reviewed; methodological rigor and reproducibility are not independently verified.
- No comparison to other metaheuristics (e.g., GA, DE) or to financial‑domain PSO variants.

## Limitations

- Excludes economic variables (price, labor, ROI) – only biophysical optimization.
- Data resolution bounded by PAGASA/Open‑Meteo; micro‑climate variations not captured.
- Validated only for lowland rice in Nueva Ecija; parameters not transferable without re‑calibration.
- Assumes perfect irrigation infrastructure and bureaucratic compliance – no delays or failures modeled.
- Does not model biotic stresses (pests, diseases). [unacknowledged]
- Preprint not peer‑reviewed; statistical claims require independent replication.

## Remember This

- 🔑 **93.33% success rate** – integrated PSO vs. 0% baseline on shifted Rastrigin.
- 📌 **13.7‑iteration drift detection** – Page‑Hinkley catches environmental shifts 94.5% faster.
- 💡 **11.32% absolute risk reduction** – from 12.73% to 1.41% climate vulnerability.
- ⚠️ **Agriculture only** – no financial data; transfer to Odin requires re‑validation.
- 🧠 **Lexicase archiving** – randomly shuffling objective priorities maintains Pareto diversity (spacing 0.0049 vs 0.8000).
