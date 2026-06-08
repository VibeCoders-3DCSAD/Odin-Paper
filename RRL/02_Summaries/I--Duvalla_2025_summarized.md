# Human-AI Collaboration in Customer Behavior Research: Personalizing Financial Services

## Metadata

```yaml
---
paper_id: "10.32996/jcsts.2025.7.4.12"
designation: international
title: "Human-AI Collaboration in Customer Behavior Research: Personalizing Financial Services"
authors: "Duvalla, V. R."
year: 2025
venue: "Journal of Computer Science and Technology Studies"
odin_topics: ["D.1", "F.1", "F.2", "H.1", "I.1"]
shorthand_tags: ["/forecasting-methods", "/temporal-dependency", "/profiling-role", "/profile-dimensions", "/classification-vs-clustering", "/classifier-candidates", "/data-sensitivity", "/privacy-by-design", "/retention-mechanisms", "/value-driven-retention"]
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

Human-AI collaboration in financial services improves customer segmentation granularity (up to 15 distinct behavioral segments) and retention via predictive churn analysis, blending AI pattern recognition with human contextual intelligence.

## Problem and Motivation

Purely algorithmic personalization lacks cultural and socioeconomic nuance, while human-only analysis cannot process massive transaction datasets at scale. Financial institutions struggle to implement effective personalization due to data integration, talent, and regulatory hurdles. Prior work lacked a structured framework for human-AI collaboration that bridges computational power with human interpretive insight.

## Approach

- Data infrastructure: integrated platforms unify customer data across touchpoints, improving CX metrics by 40% via entity resolution and graph databases.
- Segmentation: unsupervised clustering identifies up to 15 behavioral segments (vs. 4–5 conventional); RNNs achieve higher predictive accuracy than conventional ML.
- Temporal pattern mining: identifies sequences preceding life decisions (mortgage, retirement) with higher predictive power than non-temporal approaches.
- Human-in-the-loop (HITL): knowledge collaboration frameworks improve prediction accuracy by 35% over fully automated systems.
- Ethical oversight: multi-layered fairness audits and counterfactual analysis detect disparate impacts across demographic dimensions.
- Operationalization: containerized microservices with feature stores enable real-time deployment; omnichannel orchestration yields 59% higher CSAT vs. siloed channels.
- Experimentation: multi-armed bandit and causal inference achieve higher conversion rates than static personalization.

## Findings

1. Integrated data platforms improve customer experience metrics by **40%** compared to non-integrated approaches [3].
2. Human-in-the-loop frameworks improve model prediction accuracy by **35%** over fully automated systems [7].
3. Omnichannel orchestration achieves **59%** higher customer satisfaction versus siloed channel approaches [10].
4. JP Morgan Chase's human-AI collaborative platform delivered **94%** higher engagement with financial wellness recommendations [10].

- Multi-dimensional behavioral segmentation identifies up to 15 distinct customer segments, enabling significantly more targeted personalization.

## Key Figures and Tables

- Figure 1: Data infrastructure layers (integrated platforms, real-time, governance) → Unifying data sources drives CX gains.
- Figure 2: Advanced segmentation methods (clustering, temporal patterns, neural networks) → RNNs outperform conventional ML on behavioral prediction.
- Figure 3: Operationalization stack (execution, omnichannel, experimentation, case study) → Chase's platform achieved 94% engagement lift.
- Figure 4: Ethical AI roadmap (XAI, privacy-preserving, governance) → Federated learning preserves accuracy while protecting data.
- Table 1: Comparison of HITL collaboration models → Confidence-based escalation optimizes resource use but requires sophisticated scoring.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| HITL | Human-in-the-loop: humans review or guide AI decisions, especially for complex cases. |
| RNN | Recurrent neural network: a neural net with loops that remembers past inputs (think: memory of transaction sequences). |
| CX | Customer experience: the overall perception a customer has with a financial service. |
| CSAT | Customer satisfaction score: a metric measuring how happy users are with a service. |
| XAI | Explainable AI: techniques that make model decisions interpretable to humans. |
| LIME | Local Interpretable Model-agnostic Explanations: explains individual predictions by approximating the model locally. |
| SHAP | SHapley Additive exPlanations: game-theory-based method to attribute prediction outcomes to input features. |
| Federated learning | A privacy-preserving technique where models train on local devices, sharing only gradient updates, not raw data. |
| Multi-armed bandit | An algorithm that balances exploration (testing new options) and exploitation (using the best known option) in real time. |

## Critical Citations

- [BluEnt Tech, 2024] — Provides the 40% CX improvement figure used to justify integrated data platform benefits.
- [Arif, M., 2024] — Reports the 35% accuracy gain from HITL frameworks, directly supporting Odin's human-review design.
- [Bentre, S. et al., 2024] — Source of the 59% CSAT and 94% engagement numbers used in retention and omnichannel arguments.
- [Ailyn, D., 2024] — Discusses RNN advantages over conventional ML, informing Odin's forecasting module algorithm selection rationale.

## Relevance to Odin

**Topics:**

D.1 — Predictive Modeling in Personal Finance Systems

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

F.2 — Profile Classification Algorithm

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

I.1 — User Retention and Engagement in Personal Finance Systems

**Contribution to Odin:**

This paper directly informs Odin's user profile classification module by demonstrating that multi-dimensional behavioral segmentation using clustering and RNNs captures up to 15 distinct patterns, far exceeding demographic-only approaches. The human-in-the-loop framework with confidence-based escalation justifies Odin's planned design for anomaly detection and budget recommendation reviews, where uncertain predictions flag human oversight. Privacy-preserving techniques like federated learning support Odin's privacy-by-design commitment given manual transaction input and Philippine data privacy law (RA 10173). The reported retention lift from predictive churn analysis (not gamification) aligns with Odin's value-driven engagement strategy.

**Directly justifies:**

- "Integrated data platforms improve customer experience metrics by 40%, supporting Odin's need to unify manually entered transactions across categories for consistent profiling."
- "RNN implementations achieve higher predictive accuracy for future financial behaviors than conventional ML, applicable to Odin's spending forecasting module (though Odin uses LSTM specifically)."
- "Human-in-the-loop collaboration improves model prediction accuracy by 35%, justifying Odin's inclusion of human review for anomaly alerts or budget recommendations."
- "Federated learning enables personalization without centralized sensitive data, aligning with Odin's local-only storage and privacy-by-design for Filipino users."
- "Predictive churn analysis using customer behavior sequences enables proactive retention — a direct alternative to gamification for Odin's engagement strategy."

**Limits of relevance:**

- The paper focuses on general financial services (banking, wealth management), not specifically personal budget management systems like Odin.
- All quantitative findings are derived from enterprise banking environments with automated data feeds; Odin relies on manual transaction input, which may affect behavioral pattern detection.
- Population and geography are not specified but implicitly Western; Filipino cultural spending norms and income volatility are not addressed.
- The paper is a conceptual review synthesizing secondary sources, not an original empirical study with controlled experiments in a PFMS context.

## Limitations

- No original empirical validation; all cited numbers come from blog posts and non-peer-reviewed industry sources, reducing evidentiary weight.
- Lacks specific algorithm benchmarks (e.g., LSTM vs. GRU) or hyperparameter details needed for direct implementation in Odin's modules.
- Does not address cold-start scenarios for new customers with no transaction history — a core challenge for Odin's profiling and forecasting. [unacknowledged]
- Geographical bias toward US/Western financial systems; no discussion of low-data environments or manual data entry contexts common in Filipino personal finance. [unacknowledged]
- The paper acknowledges implementation challenges (data integration, talent, regulation) but does not quantify their impact on real-world deployment timelines or costs.

## Remember This

- 🔑 Integrated data platforms boost CX by **40%** — unifying transaction views matters for Odin's categorization module.
- 📌 Human-in-the-loop improves prediction accuracy by **35%** — AI needs human context for anomaly and budget alerts.
- 💡 Omnichannel orchestration yields **59%** higher satisfaction — consistent experience principles apply even to Odin's single mobile channel.
- 🧠 Chase saw **94%** higher engagement with collaborative personalization — human-AI partnership works without gamification.
- 🔍 Federated learning preserves accuracy while keeping data local — directly supports Odin's privacy-by-design approach under Philippine law.
