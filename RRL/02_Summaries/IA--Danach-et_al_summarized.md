```yaml
paper_id: 10.29020/nybg.ejpam.v18i4.6707
designation: international
title: "Toward Transparent Optimization: A Systematic Review of Explainable AI in Decision-Making Systems"
authors: "Danach, K.; Aly, W. H. F.; Tarhini, A.; Laouadi, S."
year: 2025
venue: "European Journal of Pure and Applied Mathematics"
odin_topics:
  - 6.A
  - 6.B
  - 7.B
  - 7.C
  - 8.A
  - 8.B
  - 10.A
  - 10.B
  - 12.A
  - 12.B
shorthand_tags:
  - "/predictive-modeling"
  - "/spending-forecast"
  - "/budget-recommendation"
  - "/budget-algorithm"
  - "/anomaly-detection"
  - "/anomaly-algorithm"
  - "/data-privacy"
  - "/user-trust"
  - "/eval-framework"
  - "/eval-algorithm"
tldr: "A systematic review synthesizes the integration of explainable AI (XAI) with optimization methods across healthcare, finance, logistics, and energy, proposing a taxonomy and highlighting trade-offs between performance and interpretability."
problem_and_motivation: "Optimization-driven AI systems often operate as black boxes, undermining trust, regulatory compliance, and human-AI collaboration in high-stakes decisions. Despite advances in XAI, systematic integration with optimization frameworks remains fragmented and lacks unified taxonomies. This gap hinders the development of transparent, accountable intelligent systems."
approach:
  - "Conducted a systematic literature search across Scopus, Web of Science, IEEE Xplore, and ACM Digital Library for 2010-2024, retrieving 642 records and including 112 peer-reviewed studies after screening."
  - "Proposed a structured taxonomy categorizing XAI-optimization integration by explainability level, optimization complexity, and domain specificity."
  - "Analyzed integration strategies including post-hoc explanations (SHAP, LIME), interpretable models (decision trees, MILP), certificate-based verification, and data-driven frameworks like EXALT."
  - "Examined applications in healthcare (resource allocation), finance (portfolio optimization), logistics (supply chain), and energy systems."
  - "Identified key challenges: performance-interpretability trade-offs, lack of standardized benchmarks, and scalability issues."
findings:
  - "num: EXALT framework reduces explanation generation time by 72% compared to post-hoc methods while maintaining 98% solution optimality."
  - "num: Explainable optimization approaches achieve error reduction rates of 41-68% compared to black-box optimization in healthcare logistics and derivatives pricing."
  - "Explainability constraints can enhance solution quality by acting as regularizers that embed domain knowledge."
  - "The trade-off between optimality and interpretability can be favorable, with explainable path constraints increasing solution cost by only a small margin."
  - "Standardized evaluation metrics for explainability are lacking, hampering systematic comparison of methods."
key_figures_tables:
  - "Figure 1: Taxonomy of XAI techniques, evaluation criteria, and challenges → XAI includes post-hoc, intrinsic, and example-based methods."
  - "Figure 2: Overview of exact, approximate, and hybrid optimization methods → Optimization lacks transparency, motivating XAI integration."
  - "Figure 3: Annual publication trend 2010-2024 → Sharp growth after 2020, indicating rising interest."
  - "Figure 4: Top keywords: ExplainableAI, optimization, transparency, healthcare, finance → Dominant themes and sectors."
  - "Table 1: Comparative evaluation of XAI-optimization approaches → Trade-offs among scalability, fidelity, computational cost."
  - "Table 3: Domain mapping with advantages and limitations → Each sector has unique challenges."
key_equations:
  - equation: "$\\min_x f(x) + \\lambda \\sum_{j=1}^k w_j \\|x - x_j^*\\|^2$"
    explanation: "Contextual similarity-weighted regularization for explanation-by-precedent."
  - equation: "$x_{t+1}^* = \\arg\\min_x [f(x) + \\gamma \\|x - x_t^*\\|^2]$"
    explanation: "Temporal smoothing ensures explanation continuity across decision points."
definitions:
  - term: "XAI"
    definition: "Explainable Artificial Intelligence, a suite of techniques to make AI outputs understandable to humans."
  - term: "SHAP"
    definition: "SHapley Additive exPlanations, a post-hoc feature attribution method."
  - term: "LIME"
    definition: "Local Interpretable Model-agnostic Explanations, a local surrogate explainer."
  - term: "MILP"
    definition: "Mixed-Integer Linear Programming, an exact optimization method."
  - term: "RL"
    definition: "Reinforcement Learning, a learning-based optimization paradigm."
  - term: "AutoXAI"
    definition: "Automated selection and tuning of XAI methods for optimization workflows."
  - term: "L2O"
    definition: "Learning to Optimize, an approach encoding knowledge through optimization."
  - term: "EXALT"
    definition: "Explainable Algorithmic Tools for optimization problems using similarity-preserving embeddings."
critical_citations:
  - "[Barredo Arrieta et al., 2020] — Comprehensive XAI taxonomy."
  - "[Molnar, 2020] — Interpretable machine learning book."
  - "[Goerigk et al., 2024] — Feature-based interpretable surrogates."
  - "[Heaton & Wu Fung, 2023] — Explainable AI via learning to optimize."
  - "[NIST, 2021] — Four principles of explainable AI."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      justification: "Reviews predictive optimization with explainability for financial forecasting."
    - code: "6.B"
      name: "Spending Forecasting Algorithm"
      justification: "Covers learning-to-optimize and time-series forecasting with XAI."
    - code: "7.B"
      name: "Budget Recommendation in Personal Finance Systems"
      justification: "Discusses multi-objective optimization for resource allocation with explainable constraints."
    - code: "7.C"
      name: "Budget Recommendation Algorithm"
      justification: "Analyzes MILP, metaheuristics, and AutoXAI for interpretable recommendations."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      justification: "XAI methods like SHAP can explain anomaly scores in transaction data."
    - code: "8.B"
      name: "Anomaly Detection Algorithm"
      justification: "Certificate-based verification and rule-based models for interpretable anomaly detection."
    - code: "10.A"
      name: "Data Privacy and Security in Personal Finance Systems"
      justification: "Discusses transparency and auditability as prerequisites for user trust and compliance."
    - code: "10.B"
      name: "User Trust in Personal Finance Systems"
      justification: "XAI is framed as essential for building stakeholder trust and accountability."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      justification: "Highlights lack of standardized explainability metrics and evaluation benchmarks."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      justification: "Compares XAI-optimization approaches on scalability, fidelity, and computational cost."
  contribution: "This review provides a taxonomy of XAI-optimization integration that can guide Odin's choice of interpretable algorithms for spending forecasting and anomaly detection. The analysis of post-hoc methods (SHAP, LIME) and intrinsically interpretable models (MILP, decision trees) informs the design of transparent budget recommendation modules. The discussion of certificate-based verification and AutoXAI frameworks supports building user trust and regulatory compliance in Odin's personal finance management system. The quantitative findings on explanation efficiency (72% reduction in time) and error reduction (41-68%) justify prioritizing explainable optimization over black-box methods."
  directly_justifies:
    - "XAI methods can explain optimization-driven decisions without sacrificing near-optimal performance."
    - "Explainability constraints can be embedded as multi-objective optimization objectives."
    - "Certificate-based verification provides formal guarantees for solution properties like feasibility and stability."
    - "Standardized evaluation benchmarks for explainability are currently absent."
    - "EXALT framework reduces explanation generation time by 72% while maintaining 98% optimality."
  limits:
    - "The review is a systematic literature synthesis, not an empirical validation of specific algorithms for PFMS."
    - "The paper focuses on general XAI-optimization integration, not on Filipino young professionals or culturally specific financial practices."
    - "Scalability of explainable optimization to large-scale personal finance data is not empirically tested."
  mapping_rationale: "The paper addresses transparency and trust in optimization-based decision systems, directly relevant to Odin's need for explainable spending forecasting (6.A, 6.B), budget recommendation (7.B, 7.C), and anomaly detection (8.A, 8.B). The emphasis on user trust and data privacy through XAI aligns with topics 10.A and 10.B. The systematic review's evaluation of algorithmic modules and frameworks justifies topics 12.A and 12.B. Topics related to Filipino demographics (1.A-C), cultural practices (2.A-C), or mobile design (9.A-B) were rejected as the paper is domain-agnostic. The inclusion of finance sector examples makes it relevant despite lack of localization."
limitations:
  - "Scalability to large-scale industrial problems remains a significant challenge [unacknowledged]."
  - "Standardization of explainability metrics and evaluation frameworks is lacking [acknowledged]."
  - "Integration with existing enterprise systems and workflows has received limited research attention [unacknowledged]."
  - "Most approaches assume idealized environments; real-world conflicting stakeholder needs are not addressed [unacknowledged]."
remember_this:
  - "Explainable optimization reduces explanation time by 72% while preserving 98% optimality."
  - "XAI methods can turn black-box optimizers into transparent, auditable systems."
  - "The performance-interpretability trade-off is often favorable in practice."
  - "Certificate-based verification provides formal guarantees for optimization decisions."
  - "Standardized explainability benchmarks are urgently needed for comparison."
```