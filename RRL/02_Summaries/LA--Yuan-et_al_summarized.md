```yaml
paper_id: 10.1109/ACCESS.2023.3338705
designation: international
title: User Cold Start Problem in Recommendation Systems: A Systematic Review
authors: Yuan, H.; Hernandez, A.A.
year: 2023
venue: IEEE Access
odin_topics:
  - 4.B
  - 5.A
  - 5.B
  - 5.C
  - 6.A
  - 10.A
  - 10.B
  - 11.A
  - 12.A
  - 12.B
shorthand_tags:
  - /limitations-gaps
  - /behavioral-profiles
  - /cold-start-dynamics
  - /profile-classification
  - /predictive-modeling
  - /data-privacy
  - /user-trust
  - /engagement-dynamics
  - /evaluation-frameworks
  - /algorithm-evaluation
tldr: A systematic review of 45 papers (2016-2023) categorizes user cold start solutions into data-driven and method-driven approaches, analyzing evaluation metrics and future directions.
problem_and_motivation: Existing systematic reviews on user cold start are scarce, outdated, or fail to distinguish between user and item cold start problems. Solutions for these two problems differ, yet prior work often conflates them. A focused, up-to-date review is needed to guide researchers.
approach:
  - Followed systematic literature review guidelines (Kitchenham 2007) with seven steps: research questions, search strings, database selection (IEEE, ACM, Web of Science), inclusion/exclusion criteria, paper search, pre-selection, full reading, and classification.
  - Search strings combined terms like "recommendation system", "user cold start", and "cold start".
  - 1480 papers initially retrieved; after title/abstract screening and inclusion/exclusion criteria, 45 papers from 2016-2023 were selected for deep analysis.
  - Categorized approaches into data-driven (using cross-domain, social network, demographic data) and method-driven (meta-learning, deep learning, matrix factorization, collaborative filtering improvements, content-based improvements).
  - Analyzed evaluation metrics used (rating prediction, classification accuracy, ranking metrics) and future research directions.
findings:
  - num: 45 papers were selected from 1480 initial search results, with the highest number (11) published in 2020.
  - Data-driven strategies commonly use cross-domain and social network data to provide additional user information for cold-start users.
  - Method-driven strategies increasingly apply meta-learning, deep learning (DNN, GNN, GAN), and attention mechanisms to learn from limited user interactions.
  - num: Most literature (over 70% of analyzed papers) uses ranking metrics such as NDCG@K and Hit@K for evaluation, rather than rating prediction metrics.
  - Future directions identified include multi-task learning, attention mechanisms, harmonized user satisfaction indicators, and privacy-preserving methods.
key_figures_tables:
  - "Figure 1: Systematic literature review flow diagram → Seven-step process from questions to classification."
  - "Figure 2: Paper selection process → 1480 initial papers reduced to 45 final selected."
  - "Figure 3: Papers per year (2016-2023) → Peak of 11 papers in 2020, increasing trend."
  - "Figure 7: Classification of user cold start recommendation strategies → Two main branches: data-driven and method-driven."
  - "Figure 8: Timeline of methods for new user problem → Deep learning and meta-learning dominate recent years."
  - "Figure 9: Deep learning algorithm overlay visualization → GNN and attention mechanisms are newest."
  - "Figure 10: Evaluation metrics overlay diagram → NDCG is most frequently used recently."
key_equations:
  - equation: Y_t = W Y_s
    explanation: Similarity-based model for cold-start using source domain Y_s and target domain Y_t.
definitions:
  - term: User cold start
    definition: Problem where a new user lacks historical data, making accurate recommendations difficult.
  - term: Item cold start
    definition: Problem where a new item lacks ratings, hindering its recommendation to users.
  - term: Meta-learning
    definition: Learning to learn; enables rapid adaptation to new tasks with few examples.
  - term: Cross-domain recommendation
    definition: Using user preferences from source domains to improve recommendations in a target domain.
  - term: NDCG@K
    definition: Normalized Discounted Cumulative Gain at rank K, a ranking metric for recommendation quality.
critical_citations:
  - "[Panda and Ray, 2022] — Categorized cold-start mitigation but did not separate user vs item."
  - "[Son, 2016] — Early user cold start review but outdated (pre-2014)."
  - "[Camacho and Alves-Souza, 2018] — Focused only on social network data for cold start."
  - "[Abdullah et al., 2021] — Reviewed only data-driven strategies, missing method-driven approaches."
relevance:
  topics:
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      justification: Paper explicitly identifies gaps in prior cold-start reviews.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      justification: User profiling is central to cold-start recommendation.
    - code: 5.B
      name: Profile Dynamics and the Cold‑Start Problem
      justification: Directly addresses the cold-start problem for new user profiles.
    - code: 5.C
      name: Financial Behavioral Profile Classification Algorithm
      justification: Reviews classification algorithms (meta-learning, deep learning) for new users.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      justification: Cold-start solutions involve predicting user preferences from limited data.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      justification: Paper lists privacy protection as a future research direction.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      justification: Privacy concerns affect user trust; paper discusses reluctance to share data.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      justification: Cold start affects user experience and engagement; paper mentions user satisfaction.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      justification: Paper analyzes evaluation metrics (NDCG, RMSE, AUC) for cold-start systems.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: Categorizes and compares performance of different cold-start algorithms.
  contribution: "Odin's behavioral profiling module can leverage cross-domain and social network data fusion strategies from this review to address cold-start for new Filipino young professionals. The review's categorization of meta-learning algorithms provides a blueprint for Odin's spending forecasting module to quickly adapt to new users with few interaction records. The analysis of evaluation metrics (NDCG, RMSE, AUC) informs Odin's system evaluation framework for cold-start scenarios. Privacy-preserving methods highlighted in future directions guide Odin's data privacy module to balance personalization and user trust."
  directly_justifies:
    - "User cold start can be mitigated using auxiliary data from social networks or cross-domain sources."
    - "Meta-learning enables rapid adaptation to new users with limited interaction data."
    - "Ranking metrics like NDCG@K are preferred for evaluating cold-start recommendation performance."
    - "Deep learning methods (GNN, attention) capture non-linear user-item relationships for cold-start users."
  limits:
    - "Review includes no experimental validation or comparative analysis of the surveyed methods."
    - "Papers selected only from IEEE, ACM, and Web of Science; other databases may contain relevant work."
    - "Focus is on general recommendation systems, not specifically on personal finance or Filipino demographics."
  mapping_rationale: "This systematic review directly addresses the user cold-start problem, which maps to Odin's behavioral profiling domain (5.A, 5.B, 5.C) and predictive modeling (6.A). The paper identifies gaps in existing systems (4.B) and reviews evaluation frameworks (12.A, 12.B). Privacy and trust (10.A, 10.B) are noted as future challenges, and engagement (11.A) is mentioned via user experience. Topics unrelated to personal finance (e.g., expense categorization, mobile design, savings/debt) were rejected because the paper does not cover those domains."
limitations:
  - "No experimental validation of the surveyed methods. [unacknowledged]"
  - "Only 45 papers analyzed; may not capture all recent advances."
  - "Does not address domain-specific challenges of personal finance systems. [unacknowledged]"
remember_this:
  - "45 papers from 2016-2023 were analyzed for user cold start."
  - "Data-driven and method-driven are the two main solution categories."
  - "Meta-learning and deep learning are increasingly applied to cold start."
  - "Ranking metrics like NDCG dominate evaluation of cold-start systems."
  - "Privacy protection remains an open challenge for cold-start recommendations."
```