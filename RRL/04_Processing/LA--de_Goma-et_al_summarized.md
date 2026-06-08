```yaml
paper_id: 10.1145/3779657.3779698
designation: algorithm-specific
title: Using Item Personality-Based Profiling in Music Recommender Systems
authors: de Goma, J.; Anonuevo, J. N.; Pangan, G. N.; Deang, J. J.; Villaluz, A.
year: 2025
venue: 2025 The 7th World Symposium on Software Engineering (WSSE2025)
odin_topics:
  - 5.A
  - 5.C
  - 12.B
shorthand_tags:
  - /behavioral-profiles
  - /classification-algorithm
  - /eval-algorithm
tldr: Incorporating Big Five personality profiles into a hybrid LightFM recommender improves music recommendation accuracy over pure collaborative filtering, especially for cold-start users.
problem_and_motivation: Music recommender systems struggle with user variability and the cold-start problem. Traditional collaborative filtering fails to capture diverse user preferences. Personality-based profiling offers a potential solution but has accuracy issues.
approach:
  - Data collected from 208 Mapua students via survey (10-item BFI, 100 song ratings, top 5 genres) plus Million Song Dataset playcounts.
  - LightFM hybrid model with user features (BFI T-scores, genre preferences) and item features (sonic features: acousticness, danceability, energy, etc., and item personality profiles as proportions).
  - Item personality profile computed as proportion of users who liked the item with a given Big Five degree.
  - Compared pure collaborative filtering (CF) against hybrid variants using BPR and WARP loss functions.
  - Offline evaluation used precision, recall, AUC, F1 on 80/20 train-test split.
  - Online evaluation with 20 new users measuring recommendation quality, diversity, satisfaction, and precision/recall.
findings:
  - num: Hybrid WARP model achieved training precision 0.23, recall 0.75, AUC 0.82; validation precision 0.46, recall 0.64, AUC 0.57.
  - Pure CF overfitted (training AUC 1.00, validation AUC 0.56) and performed worse on unseen data.
  - Online evaluation: hybrid Model A had mean user satisfaction 4.15 vs pure CF 3.55 (p<0.05).
  - Hybrid model achieved precision 0.57, recall 0.62, F1 0.58 on user feedback, outperforming pure CF (0.41/0.46/0.40).
  - Hybrid WARP generalized better than BPR on sparse data (personality info for <20% of users).
key_figures_tables:
  - Table 1: Training metrics comparison → Hybrid WARP has best recall and AUC among hybrids.
  - Table 2: Validation metrics → CF overfits, hybrid generalizes better.
  - Table 5: Precision/recall/F1 on user feedback → Model A outperforms Model B.
key_equations:
  - equation: \text{Proportion} = \frac{\text{totalNumber of Users who liked the Item and has the same BF degree}}{\text{totalNumber of Users who Liked the Item}}
    explanation: Computes item personality profile for each Big Five degree.
definitions:
  - term: BFI
    definition: Big Five Inventory, a personality assessment tool measuring five core traits.
  - term: IPP
    definition: Item Personality Profile, a vector representing an item's personality associations.
  - term: CF
    definition: Collaborative Filtering, a recommendation method based on user-item interactions.
  - term: LightFM
    definition: A hybrid recommender system library combining collaborative and content-based filtering.
  - term: WARP
    definition: Weighted Approximate-Rank Pairwise loss, optimizes top-k recommendation ranking.
  - term: BPR
    definition: Bayesian Personalized Ranking, optimizes AUC score for pairwise preferences.
  - term: AUC
    definition: Area Under the ROC Curve, measures ranking quality.
critical_citations:
  - "[Kleć et al., 2023] — Personality facets affect music recommendation error rates."
  - "[Alharthi, 2015] — Introduced proportion-based item personality profile method."
  - "[Lu & Tintarev, 2018] — Diversity adjustment strategy using personality for music recommendation."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      justification: Demonstrates using Big Five traits to predict user preferences, applicable to spending profiles.
    - code: 5.C
      name: Financial Behavioral Profile Classification Algorithm
      justification: Hybrid LightFM with personality features offers a classification approach for cold-start users.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: Comprehensive offline/online metrics (precision, recall, AUC, user feedback) directly inform PFMS algorithm evaluation.
  contribution: "This paper's hybrid personality-profiling approach can inform Odin's behavioral profiling module (5.A) by demonstrating how Big Five traits predict user preferences in a sparse-data setting. The item personality profile method (IPP) offers a transferable technique for cold-start scenarios in spending categorization (3.A) by leveraging aggregate user behaviors. The evaluation framework using precision, recall, and user feedback directly applies to Odin's system evaluation (12.B) for algorithmic modules. The comparison of loss functions (BPR vs WARP) provides guidance on optimizing for top-k recommendation quality in personal finance."
  directly_justifies:
    - "Incorporating personality profiles improves recommendation accuracy over pure collaborative filtering."
    - "Hybrid models using WARP loss generalize better to unseen data than BPR or pure CF."
    - "User satisfaction is higher for personality-enhanced recommendations (mean 4.15 vs 3.55)."
    - "Cold-start problems can be mitigated using item personality profiles computed from aggregate user data."
  limits:
    - "Small song dataset (100 songs) limits recommendation variation and diversity perception."
    - "Personality data available for less than 20% of users, causing sparsity [acknowledged]."
    - "Online evaluation sample size of 20 new users is small [unacknowledged]."
    - "Generalizability beyond student population in the Philippines is not discussed [unacknowledged]."
  mapping_rationale: "The paper focuses on personality-based recommendation algorithms, which map to behavioral profiling (5.A) and classification algorithms (5.C) in Odin’s domains. Although the application is music rather than finance, the hybrid LightFM approach and IPP method are algorithmically transferable to spending behavior prediction. The extensive offline and online evaluation (precision, recall, AUC, user feedback) directly supports system evaluation (12.B). Domains such as spending forecasting (6.A) and budget recommendation (7.A) were rejected because the paper does not address financial data or temporal spending patterns. The cold-start mitigation technique also touches on profile dynamics (5.B) but was not selected due to insufficient focus on profile evolution over time."
limitations:
  - "Small song dataset (100 songs) limits recommendation variation. [unacknowledged]"
  - "Personality data available for less than 20% of users, causing sparsity. [acknowledged]"
  - "Online evaluation sample size of 20 new users is small. [unacknowledged]"
  - "Results may not generalize beyond Filipino student population. [unacknowledged]"
remember_this:
  - Hybrid WARP model achieved 0.46 precision and 0.64 recall on validation.
  - Personality profiling reduces cold-start problems in recommender systems.
  - User satisfaction improved by 0.6 points with personality integration.
  - Pure CF overfits and fails on unseen data.
```