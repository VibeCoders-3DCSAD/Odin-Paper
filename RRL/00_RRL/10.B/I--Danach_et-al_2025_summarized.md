# Toward Transparent Optimization: A Systematic Review of Explainable AI in Decision-Making Systems

## Metadata

```yaml
---
paper_id: "10.29020/nybg.ejpam.v18i4.6707"
designation: international
title: "Toward Transparent Optimization: A Systematic Review of Explainable AI in Decision-Making Systems"
authors: "Danach, K.; Aly, W. H. F.; Tarhini, A.; Laouadi, S."
year: 2025
venue: "European Journal of Pure and Applied Mathematics"
odin_topics: ["10.A", "10.B", "12.A"]
shorthand_tags: ["/explainability-trust", "/eval-frameworks-survey"]
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

Explainable AI can be embedded into optimization pipelines by design, not as an afterthought, balancing solution quality with interpretability across healthcare, finance, and logistics.

## Problem and Motivation

Complex optimization systems (metaheuristics, reinforcement learning, mathematical programming) function as black boxes, producing optimal decisions without justification. This opacity undermines trust, blocks regulatory compliance, and limits adoption in high-stakes applications. Prior work focused on explainable machine learning in isolation, not on integrating interpretability into optimization itself.

## Approach

- Systematic literature review covering 2010–December 2024 from Scopus, Web of Science, IEEE Xplore, and ACM Digital Library.
- 642 initial records screened to 112 studies for in-depth synthesis.
- Taxonomy of XAI methods: post-hoc (SHAP, LIME), intrinsically interpretable (decision trees, linear models), and example-based (counterfactuals).
- Classification of optimization paradigms: exact (branch-and-bound, branch-and-cut), approximate (metaheuristics, hyperheuristics), and learning-enhanced (reinforcement learning, surrogate-based).
- Integration strategies: constraint-based knowledge injection, certificate-based verification (feasibility, optimality gap, stability), and data-driven frameworks (EXALT).
- Evaluation criteria: fidelity, comprehensibility, robustness, fairness, and computational cost.

## Findings

- Publication volume at the intersection of XAI and optimization has grown sharply after 2020, peaking in 2024.
- **Explainability constraints can be embedded without losing polynomial solvability in structured problems (e.g., explainable shortest path).**
- Data-driven frameworks (EXALT) reduce explanation generation time by 72% while maintaining 98% solution optimality.
- Certificate-based verification enables formal guarantees for feasibility, optimality bounds, and solution stability.
- Feature-based interpretable surrogates often outperform black-box approaches in both robustness and interpretability.
- AutoXAI frameworks automate selection and tuning of explanation methods based on fidelity, stability, comprehensibility, and efficiency.

## Key Figures and Tables

- Figure 1: Taxonomy of XAI methods → post-hoc, intrinsic, and example-based techniques with evaluation criteria.
- Figure 3: Annual publication trend (2010–2024) → sharp growth after 2020, peaking in 2024.
- Table 1: Comparative evaluation of XAI–optimization approaches → certificate-based frameworks offer highest fidelity but very high cost.
- Table 3: Domain mapping (healthcare, finance, logistics, energy, policy) → each domain’s techniques, advantages, and research opportunities.
- Figure 7: Key limitations (scalability, standardization, enterprise integration) → three primary barriers to deployment.

## Key Equations

$$ \min_{x} f(x) + \lambda \sum_{j=1}^{k} w_j \|x - x^*_j\|^2 $$
*EXALT framework: adds regularization to pull solution toward historical precedents weighted by similarity.*

$$ x^*_{t+1} = \arg\min_{x} \left[ f_t(x) + \gamma \|x - x^*_t\|^2 \right] $$
*Temporal smoothing ensures explanation continuity across decision points, avoiding “explanation jitter.”*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| XAI | Explainable Artificial Intelligence — techniques that make AI outputs understandable to humans. |
| SHAP | SHapley Additive exPlanations — post-hoc method attributing predictions to input features. |
| LIME | Local Interpretable Model-agnostic Explanations — creates simple local surrogate models. |
| MILP | Mixed-Integer Linear Programming — optimization with continuous and integer variables. |
| RL | Reinforcement Learning — agents learn optimal actions through trial and error. |
| AutoXAI | Automated selection and tuning of explanation methods. |
| EXALT | Example-based framework that regularizes optimization toward historical solution patterns. |
| Fidelity | How accurately an explanation reflects the original model’s behavior. |

## Critical Citations

- [Arrieta et al., 2020] — Comprehensive survey establishing XAI concepts and taxonomies.
- [Heaton & Fung, 2023] — Formulates “learning to optimize” (L2O) with certificate-based verification.
- [Goerigk et al., 2024] — Introduces feature-based interpretable surrogates for optimization.
- [NIST, 2021] — Four principles of explainable AI (used as reference for transparency criteria).
- [Bertsimas et al., 2020] — Optimization approach to interpretable clustering.

## Relevance to Odin

**Topics:**

10.A — Data Privacy and Security in Personal Finance Systems

10.B — User Trust in Personal Finance Systems

12.A — Evaluation Frameworks for Personal Finance Systems

**Contribution to Odin:**

This systematic review directly supports Odin’s requirement for transparent, trustworthy AI modules by demonstrating that explainability can be embedded into optimization pipelines without catastrophic performance loss. It informs Odin’s design philosophy for modules like budget recommendation and anomaly detection: interpretability should be a first-class constraint, not a post-hoc wrapper. The review’s coverage of evaluation criteria (fidelity, comprehensibility, stability) provides a blueprint for how Odin’s team should assess its own algorithm explanations before user testing.

**Directly justifies:**

- “Certificate-based verification (feasibility, optimality gap, stability) provides formal guarantees that an optimization solution respects constraints — directly applicable to Odin’s budget recommendation module to prove that allocations stay within income.”
- “EXALT framework reduces explanation generation time by 72% while maintaining 98% solution optimality, showing that real-time explainability is feasible for mobile budget recommendations.”
- “Feature-based interpretable surrogates can outperform black-box optimization in robustness and interpretability, contradicting the assumption that accuracy must be traded for transparency.”
- “AutoXAI frameworks automate selection of explanation methods based on fidelity, stability, and comprehensibility — relevant to Odin’s need to adapt explanations to different user profiles.”

**Limits of relevance:**

- Systematic review, not primary research — citations must reference original studies, not the review itself, for specific algorithm claims.
- None of the reviewed applications focus on personal budget management; most are healthcare, finance (enterprise), or logistics.
- The Philippine regulatory context (RA 10173) is not discussed; GDPR is the reference.
- No evaluation of explainability methods on manual-entry transaction data (Odin’s data environment).

## Limitations

- Review relies on existing literature up to December 2024; emerging methods after that date are not covered.
- No quantitative meta-analysis; claims about performance (e.g., 72% reduction) come from individual primary studies, not aggregated statistics. [unacknowledged]
- Scalability of explainable optimization to large industrial problems remains unproven; most examples are small- to medium-scale.
- Standardized benchmarks for explainability metrics do not exist, making cross-study comparison difficult.
- Integration with legacy enterprise systems and real-time constraints is understudied.

## Remember This

- 🔍 XAI can be embedded **by design** into optimization — not just as post-hoc SHAP/LIME.
- 📌 EXALT framework cuts explanation time by **72%** while keeping 98% optimality.
- 🔑 Certificate-based verification (feasibility, optimality, stability) offers formal guarantees for budget constraint adherence.
- ⚠️ No standardized benchmarks for explainability — evaluate Odin’s explanations with user studies, not just metrics.
- 💡 Feature-based interpretable surrogates can be **more robust** than black-box models, challenging the accuracy-transparency trade-off.
