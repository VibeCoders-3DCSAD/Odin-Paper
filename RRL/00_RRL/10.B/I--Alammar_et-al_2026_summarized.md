# Explainable AI (XAI) for transparent resource allocation in public safety communications networks

## Metadata

```yaml
---
paper_id: "10.1038/s41598-026-43440-9"
designation: algorithm-specific
title: "Explainable AI (XAI) for transparent resource allocation in public safety communications networks"
authors: "Alammar, M.; Al Ayidh, A.; Abbas, M.; Parayangat, M."
year: 2026
venue: "Scientific Reports"
odin_topics: ["8.A", "8.B", "10.B", "12.A", "12.B"]
shorthand_tags: ["/anomaly-ml-families", "/explainability-trust", "/eval-frameworks-survey", "/eval-ml-design"]
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

SLIRA, a hybrid SHAP–LIME framework with Bayesian uncertainty, achieves near-optimal resource allocation while reducing fairness gaps by 40% and improving temporal stability by 31% in public safety networks.

## Problem and Motivation

Black-box AI resource allocation models in public safety networks lack transparency, eroding stakeholder trust and making it impossible to justify decisions in life-critical emergencies. Without explainability, unfair distributions and undetected biases can go unnoticed, compromising equity and accountability. Prior work offered either global (SHAP) or local (LIME) explanations in isolation, without unifying them into a regulatory allocation mechanism.

## Approach

- Dataset: Synthetic PSN simulation with 20–50 users (police, fire, medical, command) and 5 resources; time‑varying bursty demand and priority levels.
- Method: SLIRA – explanation‑regularized allocation integrating SHAP (global fairness) and LIME (local fidelity) with a hybrid update rule.
- Key innovation: SHAP‑informed LIME proximity kernel; fused attribution Φ = γΦ_SHAP + (1‑γ)Φ_LIME; Bayesian uncertainty over decisions and explanations.
- Baselines: direct convex solver (MOSEK), black‑box AI, post‑hoc SHAP/LIME, and ablations.
- Metrics: normalized utility, fairness gap (inter‑group allocation difference), temporal stability, explanation fidelity, runtime.

## Findings

1. SLIRA achieved **0.981 ± 0.008 normalized utility** – within 2% of the optimal solver (1.000) but with 40.2% lower fairness gap.
2. Fairness gap dropped from 0.087 (solver) to **0.052 ± 0.008** – a 40% relative improvement.
3. Temporal stability gained 31.5% over the solver baseline, reaching very high consistency (0.967 in long‑run monitoring).

- SLIRA uniquely provides regulatory‑grade explainability: explanations actively govern allocation updates, not just post‑hoc diagnostics.
- Bayesian uncertainty estimates allow confidence‑aware decisions – a capability absent in solvers and black‑box models.

## Key Figures and Tables

- Table 2: Benchmark of 8 methods → SLIRA (full) achieves best fairness (0.052 gap) and stability (Very High) with near‑optimal utility.
- Figure 9: Explanation consistency over time → stabilizes at 0.967, confirming long‑term interpretability.
- Figure 13: Group fairness constraint → mean feature contribution difference of only 0.022 between protected groups.
- Figure 17: Precision, sparsity, efficiency → SLIRA matches SHAP’s precision but runs faster than SHAP and LIME.

## Key Equations

$$Φ_{SLIRA}(t) = γ Φ_{SHAP}(t) + (1-γ) Φ_{LIME}(t)$$
*Fused explanation balances global fairness (SHAP) and local fidelity (LIME).*

$$A(t) = A(t-1) + α Φ_{SLIRA}(t) - λ ∇L_{fair}(A(t-1))$$
*Allocation updated by explanation gradients minus fairness penalty.*

$$L_{SLIRA} = L_{LIME} + λ_1 Ω(g) + λ_2 ||φ_{SHAP} - φ_{SLIRA}||^2$$
*Hybrid loss enforces sparsity and SHAP consistency in local explanations.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| SHAP | Shapley Additive Explanations – global feature importance from cooperative game theory. |
| LIME | Local Interpretable Model‑agnostic Explanations – local surrogate model per prediction. |
| XAI | Explainable Artificial Intelligence – AI whose decisions humans can understand. |
| PSN | Public Safety Network – emergency communication system for first responders. |
| Fairness gap | Absolute difference in average allocation between protected user groups. |
| Temporal stability | Consistency of explanations across consecutive time steps. |

## Critical Citations

- [Raja et al., 2022] – Established foundational PSN communication demands and routing challenges.
- [Alsamhi et al., 2021] – Reviewed green IoT and UAV integration in B5G networks, motivating adaptive allocation.
- [Wang & Ran, 2023] – Compared network governance models, informing fairness and accountability in AI‑driven public systems.

## Relevance to Odin

**Topics:**

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

10.B — User Trust in Personal Finance Systems

12.A — Evaluation Frameworks for Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper provides a template for making Odin’s anomaly detection and budget recommendation modules explainable to users. By integrating SHAP (global explanation of spending patterns) and LIME (local explanation for a single flagged transaction), Odin could justify why a particular expense is anomalous or why a budget limit was suggested – directly addressing user trust. The SLIRA framework’s fairness‑constrained, uncertainty‑aware design also informs how Odin’s evaluation module can measure explanation fidelity and stability, going beyond raw algorithm accuracy. Although the domain is emergency networks, the XAI methodology is fully transferable to personal finance, where users need to understand and trust AI‑driven alerts and recommendations.

**Directly justifies:**

- “A hybrid SHAP–LIME explanation mechanism can reduce the fairness gap in resource allocation by 40% while maintaining near‑optimal utility (within 2% of an optimal solver).”
- “Bayesian uncertainty quantification over explanations enables confidence‑aware decisions, essential when users must decide whether to act on an AI‑generated anomaly alert.”
- “Explanation consistency tracked over time (final value 0.967) ensures that interpretability does not degrade as user behavior patterns evolve.”
- “Regulatory‑grade explainability – where explanations actively govern allocation updates – produces higher temporal stability (+31.5%) than post‑hoc explanation methods.”

**Limits of relevance:**

- The study uses synthetic PSN traffic data, not real personal financial transactions; spending pattern complexity may differ.
- User trust was not measured directly with human subjects; the paper reports only algorithmic explainability metrics.
- Fairness constraints are applied to protected groups (e.g., police vs. medical); Odin’s fairness concerns involve income levels or spending categories, not demographic groups.
- The evaluation assumes a centralized controller with full state observability; Odin’s mobile‑first, manual‑input setting has sparser and noisier data.

## Limitations

- Synthetic dataset with controlled burst patterns; generalizability to real‑world emergency (or financial) data is unvalidated.
- User trust and human interpretability were not measured via user studies – only algorithmic consistency and fidelity. [unacknowledged]
- Fairness constraints assume known protected groups; Odin does not collect such attributes, so adaptation would require different fairness definitions.
- Runtime analysis (10.6 ms per step) was performed on a workstation; mobile device constraints are not considered.
- No comparison against other XAI methods (e.g., DeepLIFT, Integrated Gradients) to establish relative advantage.

## Remember This

- 🔑 **40% lower fairness gap** – SHAP–LIME fusion actively regulates allocation equity.
- 📌 **31% higher temporal stability** – explanations stay consistent as conditions change.
- 💡 **0.967 explanation consistency** – interpretability persists across 24+ time steps.
- ⚠️ Domain mismatch – PSN emergency traffic ≠ personal spending; adapt methods, not numbers.
