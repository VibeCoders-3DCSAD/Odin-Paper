```yaml
paper_id: 10.1145/3616855.3635778
designation: algorithm-specific
title: Budgeted Embedding Table For Recommender Systems
authors: Qu, Y.; Chen, T.; Nguyen, Q. V. H.; Yin, H.
year: 2024
venue: Proceedings of the 17th ACM International Conference on Web Search and Data Mining (WSDM '24)
odin_topics:
  - 4.A
  - 4.B
  - 7.B
  - 7.C
  - 12.B
shorthand_tags:
  - /landscape
  - /gaps
  - /budget-recommendation
  - /budget-algorithm
  - /evaluation
tldr: Proposes Budgeted Embedding Table (BET) for efficient embedding size search in recommender systems under strict memory budgets using table-level actions and a fitness predictor.
problem_and_motivation: Existing lightweight embedding methods rely on manually tuned trade-off coefficients that fail to strictly meet memory budgets and perform inefficient instance-by-instance search. The implicit memory complexity term cannot guarantee parameter usage caps, and RL-based approaches require costly per-instance optimization. A method is needed that directly enforces memory budgets while scaling to large user/item sets.
approach:
  - Uses two real-world datasets, Gowalla and Yelp2018, with up to 1.56M interactions.
  - Defines a bounded sampler that draws embedding sizes for all users and items from probabilistic distributions, ensuring total parameter usage is capped.
  - Employs a DeepSets-based fitness predictor that evaluates table-level actions without full model retraining.
  - Alternates three action selection strategies: greedy by predicted fitness, random, and nearest neighbor to the best known action.
  - Compares against six baselines including CIESS, OptEmbed, PEP, and uniform/random allocation under sparsity ratios of 80%, 90%, and 95%.
findings:
  - "num: BET achieves the highest Recall@20 (0.1753) and NDCG@20 (0.1483) on Gowalla with LightGCN at 80% sparsity."
  - "num: At 95% sparsity on Gowalla with LightGCN, BET obtains 0.0627 Recall@5 and 0.1037 NDCG@5, outperforming CIESS by 22% and 21% respectively."
  - "num: On Yelp2018 with LightGCN at 80% sparsity, BET reaches 0.0873 Recall@20, exceeding the best baseline by 4%."
  - BET guarantees strict memory budget satisfaction, unlike ESAPN and OptEmbed which often exceed target sparsity.
  - The DeepSets-based fitness predictor reduces the number of required full model evaluations from O(S*T) to O(T).
key_figures_tables:
  - "Table 1: Performance comparison on Gowalla and Yelp2018 under 80%, 90%, 95% sparsity → BET outperforms all baselines in most settings."
  - "Figure 1: Overview of BET workflow → Action sampler generates table-level actions, fitness predictor selects best, then recommender finetuned."
  - "Figure 2: Set-based action formulation → Each embedding size corresponds to a set of users/items, enabling inductive learning."
  - "Figure 3: DeepSets-based fitness predictor → Encodes user/item frequencies and set memberships to predict action fitness."
key_equations:
  - equation: "\\min_{\\Theta, \\Phi} L_{BPR} \\quad \\text{s.t.} \\quad 1 - \\frac{\\|M\\|_{1,1}}{(|U|+|V|) \\times d_{max}} \\leq \\rho"
    explanation: "Objective to minimize BPR loss under sparsity constraint ρ."
  - equation: "d_i = \\lfloor \\tilde{p}_i \\cdot w \\cdot d_{max} \\cdot (|U|+|V|) \\rfloor"
    explanation: "Embedding size for user i from normalized probability and budget split."
  - equation: "\\mathbf{h}_{\\mathcal{A}} = \\frac{1}{d_{max}} \\sum_{d=1}^{d_{max}} \\mathbf{h}_{S_d}"
    explanation: "Action embedding by averaging set embeddings from DeepSets."
  - equation: "\\hat{f}_{\\mathcal{A}} = \\mathcal{D}(\\mathbf{h}_{\\mathcal{A}})"
    explanation: "Decoder predicts fitness score from action embedding."
definitions:
  - term: BET
    definition: Budgeted Embedding Table, the proposed method for embedding size search under memory constraints.
  - term: table-level action
    definition: A single decision specifying embedding sizes for all users and items simultaneously.
  - term: fitness predictor
    definition: A neural network that estimates the recommendation quality of a table-level action without full training.
  - term: sparsity ratio
    definition: Fraction of parameters pruned from the full embedding table, target ρ ∈ {0.8,0.9,0.95}.
  - term: DeepSets
    definition: A permutation-invariant neural architecture for set representation learning.
critical_citations:
  - "[Qu et al., 2023] — Proposed CIESS, an RL-based continuous embedding size search."
  - "[Lyu et al., 2022] — Proposed OptEmbed, learns pruning thresholds for embedding features."
  - "[Joglekar et al., 2020] — Neural input search with heuristic trade-off coefficients."
  - "[Liu et al., 2021] — PEP prunes embeddings based on learnable thresholds."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      justification: "Reviews lightweight embedding methods for recommender systems, analogous to PFMS modules."
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      justification: "Identifies two major drawbacks: heuristic budget tuning and per-instance inefficiency."
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      justification: "The memory budget allocation problem mirrors financial budget recommendation under resource constraints."
    - code: 7.C
      name: Budget Recommendation Algorithm
      justification: "BET provides a novel algorithm for allocating budgeted resources (embedding sizes) across entities."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: "Rigorous empirical comparison with six baselines using Recall and NDCG metrics."
  contribution: "BET offers a directly applicable algorithm for any PFMS module that must allocate a limited resource (e.g., memory, compute, or financial budget) across heterogeneous users or categories. The bounded sampler guarantees strict budget satisfaction, eliminating manual tuning of trade-off coefficients – a key requirement for robust PFMS deployment. The DeepSets-based fitness predictor reduces evaluation cost, enabling faster iteration over candidate allocation strategies. These ideas can inform Odin's budget recommendation engine (7.B, 7.C) and system evaluation framework (12.B)."
  directly_justifies:
    - "A table-level action that sets embedding sizes for all users simultaneously can strictly enforce a memory budget."
    - "DeepSets-based fitness prediction reduces the number of full model evaluations from O(number of candidates × iterations) to O(iterations)."
    - "Ranking users and items by frequency and allocating larger embeddings to frequent entities improves recommendation quality under sparsity."
    - "Alternating greedy, random, and nearest-neighbor action selection prevents overfitting and improves search efficiency."
  limits:
    - "Experiments only on two public datasets (Gowalla, Yelp2018) without Philippine-specific financial data."
    - "Assumes static user/item sets; not evaluated on streaming or cold-start scenarios."
    - "Requires pre-training a full-size embedding table before search, which may be costly for very large systems."
  mapping_rationale: "This paper addresses algorithmic challenges in resource-constrained recommendation, which maps to Odin's 'Budget recommendation' (7.B, 7.C) and 'System evaluation' (12.B) domains because the core problem is allocating a limited budget (memory) across many entities to maximize utility (recommendation accuracy). The paper also surveys existing methods and their limitations, covering 'Landscape' (4.A) and 'Gaps' (4.B). No direct mapping to behavioral profiling, spending forecasting, anomaly detection, or mobile UX. The borderline case of 7.B is justified by the analogy between memory budget and financial budget allocation; the algorithm's principles (strict constraint, fitness prediction) are transferable."
limitations:
  - "Does not address cold-start users or items; frequency-based ranking fails for new entities. [unacknowledged]"
  - "May not generalize to streaming recommendation where user/item sets grow over time (mentioned as future work)."
  - "Requires a pre-trained full embedding table, which itself may be infeasible for extremely large-scale systems. [unacknowledged]"
  - "Evaluation metrics (Recall, NDCG) are information retrieval standards but not validated for financial well-being outcomes. [unacknowledged]"
remember_this:
  - "BET guarantees strict memory budget adherence without manual coefficient tuning."
  - "DeepSets fitness predictor cuts evaluation cost from O(S*T) to O(T) full trainings."
  - "At 95% sparsity, BET achieves 0.0627 Recall@5 on Gowalla with LightGCN."
  - "Alternating three selection strategies prevents overfitting in action search."
  - "Frequent users and items receive larger embeddings, improving quality under budget."
```