# Explainable AI (XAI) for transparent resource allocation in public safety communications networks

## Metadata

```yaml
---
paper_id: "10.1038/s41598-026-43440-9"
designation: algorithm-specific
title: "Explainable AI (XAI) for transparent resource allocation in public safety communications networks"
authors: "Alammar, M.; Ayidh, A. A.; Abbas, M.; Parayangat, M."
year: 2026
venue: "Scientific Reports"
odin_topics: ["10.B", "12.B"]
shorthand_tags: ["/explainability-trust", "/eval-ml-design"]
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

Integrating SHAP and LIME explanations directly into resource allocation updates improves fairness by 40% and temporal stability by 31% while preserving near-optimal utility.

## Problem and Motivation

Public safety networks (PSNs) require transparent resource allocation under dynamic emergency conditions, but traditional AI models operate as black boxes, eroding trust. Without explainability, stakeholders cannot validate whether allocations are fair or justify why certain users receive prioritized resources. Prior XAI approaches treated explanations as post-hoc diagnostics rather than as active components of the allocation decision process.

## Approach

- **Hybrid explanation-regulated framework (SLIRA)** – Allocations updated using a weighted combination of global SHAP values and local LIME attributions, with tunable parameter γ balancing fairness and local fidelity.
- **SHAP-informed LIME kernel** – Local perturbation weights scaled by global SHAP feature importance, ensuring local explanations remain consistent with system-level fairness.
- **Bayesian uncertainty modeling** – Variational inference over both allocation decisions and explanation coefficients, providing probabilistic confidence estimates for risk-aware decisions.
- **Allocation update rule** – A(t) = A(t-1) + αΦ_SLIRA(t) - λ∇L_fair(A(t-1)), where Φ_SLIRA fuses SHAP and LIME attributions, followed by constraint projection.
- **Evaluation** – Simulated PSN with 20–50 users, 5 resources, time-varying demand, bursty traffic, and protected groups for fairness testing. Benchmarked against solver-based optimization, black-box AI, and post-hoc SHAP/LIME.

## Findings

1. SLIRA achieves **0.981 normalized utility** (95% CI: 0.973–0.989), within 1.9% of the optimal solver baseline (1.000), while black-box AI achieves 0.987.
2. **Fairness gap reduced by 40.2%** (to 0.052 ± 0.008) compared to solver baseline (0.087 ± 0.012) and 44% better than black-box AI (0.094 ± 0.019).
3. **Temporal stability increased by 31.5%** over solver baseline, with explanation consistency reaching 0.967 after convergence.
4. Per-step runtime of SLIRA (10.6 ms) is 3.5× faster than warm-started solver re-optimization (36.7 ms) and only 2× slower than non-explainable black-box AI (4.8 ms).
5. Bayesian uncertainty estimates show that higher posterior variance correlates with volatile network states, enabling confidence-aware allocation adjustments.

- SLIRA’s explanation fidelity is rated “Very High” (regulatory grade) compared to “Low/Medium” for black-box or post-hoc methods.
- SHAP-informed LIME kernel weights decay smoothly with Euclidean distance, ensuring local explanations respect global importance patterns.

## Key Figures and Tables

- Figure 5: User utility distribution → Shows variation across users, highlighting need for adaptive fairness mechanisms.
- Figure 9: Explanation consistency over time → Stabilizes at 0.967, confirming temporal reliability of SLIRA explanations.
- Table 2: Comparative benchmarking → SLIRA (Full) achieves fairness gap 0.052 vs. solver 0.087, with runtime 10.6 ms vs. solver 48.3 ms.
- Figure 12: SHAP-LIME hybrid gradient vs. γ parameter → Linear relationship allows tunable balance between global fairness and local fidelity.
- Figure 13: Group fairness constraint analysis → Mean feature contribution difference of 0.022 between protected groups, indicating minimal bias.

## Key Equations

$$A_{ij}(t+1)=A_{ij}(t)+\alpha \left[\gamma \phi^{SHAP}_{ij}(t)+(1-\gamma)\phi^{LIME}_{ij}(t)\right] - \lambda \frac{\partial \mathcal{L}_{fair}}{\partial A_{ij}}$$
*Hybrid update rule balancing global and local explanations.*

$$\phi^{SLIRA}_{ij} = \gamma \phi^{SHAP}_{ij} + (1-\gamma) \phi^{LIME}_{ij}$$
*Fused explanation coefficient combining SHAP and LIME.*

$$\pi_{x_i}(z)=\exp\left(-\frac{D(x_i,z)^2}{\sigma^2}\right) \cdot \left(\sum_{j=1}^m \phi^{SHAP}_j \cdot |z_j - x_{ij}|\right)$$
*SHAP-informed proximity kernel for LIME perturbations.*

$$P(\phi^{SLIRA}_{ij}|\text{Data}) = \int \left[ \gamma P(\phi^{SHAP}_{ij}|\theta) + (1-\gamma) P(\phi^{LIME}_{ij}|\theta) \right] P(\theta|\text{Data}) d\theta$$
*Bayesian fusion of SHAP and LIME uncertainties.*

## Definitions

| Term / Acronym | Plain‑English Definition |
| -------------- | ------------------------ |
| PSN | Public Safety Network – emergency responder communication system. |
| XAI | Explainable AI – machine learning that provides human-understandable justifications. |
| SHAP | Shapley Additive Explanations – game‑theory method for global feature importance. |
| LIME | Local Interpretable Model‑agnostic Explanations – surrogate model for per‑instance explanations. |
| SLIRA | SHAP‑LIME Integrated Resource Allocation – the proposed framework. |
| Φ_SLIRA | Fused explanation coefficient combining SHAP and LIME. |
| γ | Tunable parameter balancing global (SHAP) vs. local (LIME) explanation weight. |

## Critical Citations

- [Ribeiro et al., 2016] – Introduced LIME; foundational to local surrogate explanations used in SLIRA.
- [Lundberg & Lee, 2017] – Developed SHAP; provides the global additive feature attribution method SLIRA integrates.
- [Long et al., 2024] – Particle swarm optimization for scheduling; cited as prior heuristic-based allocation lacking explainability.
- [Feng et al., 2025] – Q‑learning for resource allocation; example of black-box RL without transparency.

## Relevance to Odin

**Topics:**

10.B — User Trust in Personal Finance Systems (This paper demonstrates that integrating SHAP and LIME explanations directly into allocation decisions improves fairness and transparency, directly supporting the claim that explainable AI fosters user trust in financial systems.)

12.B — Evaluation of Algorithmic Modules (The paper provides a rigorous comparative benchmarking framework for explainable AI, including metrics like explanation fidelity, temporal stability, fairness gap, and runtime, which can inform how Odin evaluates its own classification, forecasting, and recommendation modules.)

**Contribution to Odin:**

Odin’s behavioral profiling, spending forecasting, budget recommendation, and anomaly detection modules will all rely on AI models. This paper provides empirical evidence that embedding explainability (via SHAP and LIME) directly into the decision update rule—rather than adding post-hoc explanations—reduces fairness disparities by 40% and improves temporal stability by 31% with minimal utility loss (<2%). For Odin, this justifies a design where explanation signals actively regulate budget adjustments or anomaly alerts, not just serve as audit logs. The Bayesian uncertainty component also supports confidence-aware recommendations, particularly during cold-start or volatile spending periods.

**Directly justifies:**

- “Integrating SHAP and LIME attributions directly into the update rule for allocation decisions reduces fairness disparities by 40% compared to post-hoc explainability or black-box models.” (Table 2, SLIRA fairness gap 0.052 vs. AI+SHAP 0.093)
- “Explanation-regulated decision updates maintain near-optimal utility (within 2% of solver optimum) while providing regulatory-grade transparency and uncertainty quantification.” (Table 3, utility change -1.9%, explainability gain “High (Regulatory)”)
- “Bayesian uncertainty modeling over explanations enables confidence-aware adjustments, with posterior variance correlating with volatile system states.” (Section “Uncertainty-Aware Explainability via Bayesian Inference” and Figure 7)
- “Temporal consistency of explanations can be tracked and maintained above 0.96, ensuring that feature attributions do not fluctuate erratically without justified state changes.” (Figure 9, consistency 0.967)

**Limits of relevance:**

- Domain is public safety communication networks, not personal finance; direct transfer requires re-contextualizing fairness constraints (e.g., protected groups in finance are not emergency response roles).
- The evaluation uses synthetic traffic data with bursty emergency surges; financial spending patterns have different temporal dynamics (e.g., monthly cycles, seasonal shopping).
- The framework assumes real-time allocation decisions every few milliseconds; Odin operates at transaction-level (daily or per-transaction) with lower latency requirements.
- SHAP and LIME computational overhead (10.6 ms per step) may be acceptable for Odin’s batch processing but cited as a trade-off.

**Mapping Rationale:**

- **Functional domains screened:** Financial behavioral profiling (no), spending forecasting (no direct forecasting method, but uncertainty modeling could apply), budget recommendation (allocation with fairness constraints is structurally similar to budget allocation), anomaly detection (explanation of deviations), mobile-first design (no), data privacy (no explicit), user trust (yes – explainability directly addresses trust), retention (no), system evaluation (yes – comparative benchmarking and stability metrics), savings/debt (no).
- **Selected topics:** 10.B because the paper’s core claim is that transparent, explainable decisions foster stakeholder trust, directly supporting Odin’s need to build user trust in AI-driven recommendations. 12.B because the paper introduces a rigorous evaluation protocol (utility, fairness gap, temporal stability, runtime, explanation fidelity) that Odin can adopt for its own module evaluation.
- **Considered but rejected:** 5.C (classification) – the paper does not address behavioral profiles or cold-start classification. 6.B (forecasting) – no forecasting algorithm is proposed; only resource allocation. 7.C (budget recommendation) – while allocation is analogous, the constraints (bandwidth capacity vs. income) and objectives differ. 8.B (anomaly detection) – the paper uses fairness detection, not spending anomaly detection. Rejected due to lack of direct method transfer without significant reinterpretation.
- **Borderline handling:** The paper’s methods (SHAP/LIME fusion, Bayesian uncertainty) are model-agnostic and could apply to any ML system, including Odin’s modules. However, to avoid overclaiming, I selected only the two topics where the evidence is most direct: user trust (explicitly studied) and evaluation methodology (explicitly benchmarked).

## Limitations

- **Synthetic dataset** – No real-world PSN traffic data; findings depend on simulated bursty demand and priority structures.
- **Fixed Monte Carlo sampling sizes** (K=100 SHAP coalitions, P=500 LIME perturbations) – May not generalize to larger feature spaces or higher-dimensional problems.
- **[unacknowledged] No comparison with other XAI methods** (e.g., Anchors, DeepLIFT) – SLIRA’s superiority is shown only against SHAP/LIME individually, not the broader XAI landscape.
- **Scalability tested only up to 50 users** – The linear complexity O(UR) may hide constant factors that dominate at much larger scales.
- **Fairness definition limited to demographic parity** – Does not address equality of opportunity or individual fairness, which may be critical in personal finance.

## Remember This

- 🔑 **Fairness gap reduced by 40%** (from 0.087 to 0.052) when explanations regulate allocation updates directly.
- ⚠️ **Utility loss under 2%** – SLIRA stays within 0.981 vs. solver optimum 1.000, proving explainability need not sacrifice performance.
- 💡 **SHAP+LIME fusion via tunable γ** lets you balance global fairness awareness (γ high) vs. local decision fidelity (γ low) in real time.
- 🧠 **Bayesian uncertainty** provides confidence intervals for every explanation – essential for risk-aware decisions during volatile periods.
- ✅ **Temporal stability >0.96** – Explanations don’t fluctuate erratically, enabling auditability and user trust over long operation.