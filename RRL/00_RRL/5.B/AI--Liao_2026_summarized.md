# A Dynamic Intrusion Detection System Integrating Concept Drift Detection and Incremental Learning

## Metadata

```yaml
---
paper_id: "550e8400-e29b-41d4-a716-446655440000"
designation: algorithm-specific
title: "A Dynamic Intrusion Detection System Integrating Concept Drift Detection and Incremental Learning"
authors: "Liao, Z."
year: 2026
venue: "Journal of Computer, Signal, and System Research"
odin_topics: ["5.B", "5.C", "6.A", "8.A", "8.B"]
shorthand_tags: ["/concept-drift", "/progressive-reclassification", "/classifier-tradeoffs", "/anomaly-algo-candidates"]
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

Concept drift detection and incremental learning must be tightly integrated to maintain intrusion detection performance when network traffic distributions change over time.

## Problem and Motivation

Traditional intrusion detection systems assume static data distributions, but network traffic patterns drift continuously as attacks evolve and user behavior shifts. This concept drift causes static models to degrade over time, forcing costly periodic retraining that lags behind emerging threats. No prior framework had theoretically unified drift detection with incremental learning in a closed-loop adaptive system for security applications.

## Approach

- Formalizes intrusion detection in dynamic environments as a continuous adaptation problem, abandoning static closed-world assumptions.
- Proposes three-layer collaborative monitoring: macro-level (aggregate traffic statistics), micro-level (behavioral clusters), and correlation/sequence level (temporal dependencies).
- Drift detection methods include statistical process control (control charts), hypothesis testing (two-window tests), and ensemble difference metrics.
- Incremental learning addresses the stability-plasticity dilemma via regularization-based, dynamic architecture-based, and replay-based paradigms.
- Introduces an adaptive coordination mechanism with context parsing, strategy mapping, and execution control components.
- Emphasizes resource-aware optimization (Pareto trade-offs) and explainability for human-in-the-loop intervention.

## Findings

- Concept drift detection must distinguish adversarial drift (attacker evasion) from benign drift (legitimate environment evolution) to select appropriate update strategies.
- Micro-level monitoring (per-cluster drift detection) overcomes class imbalance by turning a global imbalanced problem into locally balanced subproblems.
- The stability-plasticity dilemma is the core theoretical challenge: too much stability causes rigidity; too much plasticity induces catastrophic forgetting.
- A closed-loop perception-decision-execution-evaluation cycle enables autonomous model adaptation without full retraining.
- **Explainability and resource awareness are necessary for practical deployment** — the coordinator must output rationales and respect computational constraints.

## Key Figures and Tables

None.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Concept drift | Change in the underlying statistical distribution of data over time. |
| Incremental learning | Model updates continuously from new data without retraining from scratch. |
| Stability-plasticity dilemma | Trade-off between retaining old knowledge (stability) and adapting to new patterns (plasticity). |
| Adversarial drift | Deliberate, targeted changes by attackers to evade detection. |
| Catastrophic forgetting | Loss of previously learned knowledge when a model adapts to new data. |

## Critical Citations

- [Ouyang et al., 2011] — Foundational classification of concept drift types in data streams.
- [Liu & Zhao, 2023] — Hierarchical concept drift detection using online ensemble methods.

## Relevance to Odin

**Topics:**

5.B — Profile Dynamics and the Cold-Start Problem

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

**Contribution to Odin:**

This paper's framework for integrating concept drift detection with incremental learning directly supports Odin's need to adapt to changing user financial behavior over time — such as income shifts, new spending patterns, or evolving financial obligations. The stability-plasticity dilemma formalizes the design trade-off Odin faces between retaining learned user profiles and updating them as behavior drifts. Although the paper addresses network intrusion detection, its theoretical model of drift detection (identifying when a user's financial behavior changes) and adaptive incremental learning (updating the profile classifier or anomaly detector without full retraining) is transferable to Odin's behavioral profiling and anomaly detection modules.

**Directly justifies:**

- "Concept drift detection identifies when a user's spending behavior shifts significantly, enabling model updates without waiting for scheduled retraining."
- "Micro-level drift monitoring — tracking changes within behavioral clusters rather than global statistics — detects subtle shifts in minority patterns (e.g., anomalous spending) that global metrics would miss."
- "The stability-plasticity dilemma forces a design choice: Odin's profile classifier must balance retaining long-term user traits (stability) with adapting to new patterns (plasticity)."
- "A closed-loop perception-decision-execution-evaluation cycle allows Odin to autonomously trigger model updates when drift is detected, then verify improvement."
- "Resource-aware adaptation (Pareto trade-offs between detection performance, response speed, and computational cost) is essential for Odin's mobile-first, offline-capable deployment."

**Limits of relevance:**

- Paper is theoretical — no empirical validation or quantitative performance metrics are provided.
- Domain is network security, not personal finance; the specific types of concept drift (e.g., adversarial evasion) may not map directly to benign financial behavior drift.
- No discussion of cold-start conditions (new users with no transaction history) — a core Odin problem.
- Assumes continuous data streaming; Odin's manual input produces sparse, irregular transaction data.

## Limitations

- Entirely theoretical; lacks any experimental validation or real-world dataset evaluation. [unacknowledged]
- No quantitative comparison of drift detection methods (e.g., control charts vs. hypothesis testing) in the proposed framework.
- Assumes sufficient data volume for micro-level clustering; may fail in sparse transaction environments like Odin's manual input.
- Does not address how drift detection thresholds should be set or tuned for different domains. [unacknowledged]
- Discussion of incremental learning assumes labeled data for updates; Odin's anomaly detection is largely unsupervised.

## Remember This

- 🔑 **Concept drift + incremental learning** — closed-loop adaptation beats static retraining.
- 📌 Micro-level monitoring catches rare pattern shifts that global stats hide — crucial for sparse anomalies.
- ⚠️ Stability-plasticity trade-off: too much adaptation forgets; too little ignores new behavior.
- 💡 Resource-aware decisions (Pareto trade-offs) matter for mobile deployment — Odin must balance accuracy and compute.
