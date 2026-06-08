```yaml
paper_id: "10.1145/3707693"
designation: "algorithm-specific"
title: "Modelling Concept Drift in Dynamic Data Streams for Recommender Systems"
authors: "Caroprese, L.; Pisani, F. S.; Veloso, B. M.; Konig, M.; Manco, G.; Hoos, H.; Gama, J."
year: 2025
venue: "ACM Transactions on Recommender Systems"
odin_topics:
  - "6.A"
  - "8.A"
  - "12.B"
shorthand_tags: []
tldr: "Generates synthetic data streams with concept drift by modeling user preferences as dynamic tripartite graphs and learning latent embeddings via matrix factorization."
problem_and_motivation: "Recommender systems research lacks large public datasets that capture evolving user preferences over time. Existing synthetic data generators ignore concept drift, making it hard to evaluate algorithm robustness in streaming scenarios."
approach:
  - "Uses Bayesian Personalized Ranking (BPR) matrix factorization to learn user and item embeddings from implicit feedback."
  - "Models concept drift as changes in the tripartite graph connecting users, features, and items, triggered by performance degradation."
  - "Detects drift via HDDM_W on loss values; when drift occurs, extends latent dimension and retrains with a penalty on deviation from previous model."
  - "Evaluates on MIND (news), Amazon Video Games, and Yoochoose datasets, using HR@5 and HR@10 metrics."
  - "Compares against VAE baseline and conducts ablation studies on regime identification."
findings:
  - "num: The proposed method generates synthetic item frequency distributions that closely match real data when number of users exceeds items."
  - "Drift detection identified 6 regimes in Amazon Video Games and 1 in Yoochoose, with performance drops followed by recovery."
  - "Inverted Amazon dataset (users < items) showed poor synthetic fidelity, confirming need for sufficient preferences per item."
  - "BPR outperformed VAE in adaptive scenarios with many new items, while VAE performed better on stable news datasets."
  - "A single model trained only on first regime performed poorly on subsequent regimes, validating the need for drift adaptation."
key_figures_tables:
  - "Figure 3: Loss on MIND test batches with warning and drift indicators → Loss stable with fluctuations due to rapid news cycles."
  - "Figure 5: Real vs synthetic frequency distributions for MIND → Distributions are closely matched (Kolmogorov-Smirnov positive)."
  - "Figure 8: Real vs synthetic for Amazon Video Games → Poor match due to insufficient item preferences."
  - "Figure 13: Real vs synthetic for inverted Amazon → Good match after swapping user/item roles."
  - "Figure 15: BPR vs VAE HR@5 on MIND → VAE stable at higher median, BPR fluctuates."
key_equations:
  - equation: "\\hat{r}_{u,i} = \\sigma(\\mathbf{p}_u^T (\\mathbf{q}_i - \\mathbf{q}_j))"
    explanation: "Logistic function for pairwise preference comparison."
  - equation: "\\mathcal{L}_{bpr}(M|V) = \\sum_u \\sum_{i \\succ_u j} \\log \\sigma(\\mathbf{p}_u^T(\\mathbf{q}_i-\\mathbf{q}_j))"
    explanation: "BPR loss optimizing embedding closeness for preferred items."
  - equation: "\\mathcal{L}_d(M'; M, R^{(t)}) = \\mathcal{L}_c(M'; R^{(t)}) + \\delta \\sum_u \\sum_k |p'_{u,k} - p_{u,k}| + ..."
    explanation: "Drift loss penalizes changes to previous embeddings."
definitions:
  - term: "BPR"
    definition: "Bayesian Personalized Ranking, a matrix factorization method for implicit feedback."
  - term: "Concept drift"
    definition: "Change in data distribution over time in a data stream."
  - term: "HDDM_W"
    definition: "Hoeffding Drift Detection Method with exponentially weighted moving average."
  - term: "MF"
    definition: "Matrix factorization."
  - term: "HR@k"
    definition: "Hit Rate at cutoff k, proportion of users for whom the correct item appears in top-k recommendations."
critical_citations:
  - "[Rendle et al., 2009] — Introduces BPR model for implicit feedback."
  - "[Gama et al., 2014] — Survey on concept drift adaptation."
  - "[Koren, 2009] — Temporal dynamics in collaborative filtering."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      justification: "Paper's BPR model predicts user preferences from implicit feedback, applicable to spending forecasting."
    - code: "8.A"
      name: "Anomaly Detection in Personal Finance Systems"
      justification: "Concept drift detection method identifies distribution shifts, analogous to anomaly detection in spending streams."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      justification: "Paper uses HR metrics and compares BPR vs VAE, providing evaluation methodology for PFMS algorithms."
  contribution: "This paper provides a drift-adaptive matrix factorization method that can be used to model evolving user spending preferences in Odin. The synthetic data generator enables controlled testing of Odin's spending forecasting and anomaly detection modules under different drift scenarios. The drift detection algorithm (HDDM_W on loss) can be adapted to monitor performance degradation in Odin's behavioral profiling and trigger model retraining. The comparison of BPR and VAE under concept drift informs algorithm selection for Odin's recommendation engine."
  directly_justifies:
    - "Adaptive matrix factorization models outperform static models when user preferences drift over time."
    - "Drift detection based on loss function monitoring can reliably identify distribution shifts in streaming interaction data."
    - "Synthetic data generation with controlled drifts is necessary for evaluating algorithm robustness in personal finance systems."
  limits:
    - "Experiments conducted on news, games, and e-commerce data, not personal finance or spending data."
    - "Assumes binary implicit feedback (like/dislike), but spending data may include amounts and categories."
    - "Requires sufficient number of preferences per item; may fail for cold-start items."
    - "Drift detection thresholds may need tuning for different domains."
  mapping_rationale: "This paper does not directly address personal finance but provides foundational methods for predictive modeling and anomaly detection in streaming data. Topics 6.A and 6.B (predictive/spending forecasting) are relevant because the BPR model predicts user preferences from implicit feedback, analogous to predicting spending likelihood. Topic 8.A (anomaly detection) is relevant because concept drift detection identifies distribution shifts, similar to detecting unusual spending patterns. Topic 12.B (evaluation) is included for its rigorous comparison of algorithms under drift. Topics 5.A (behavioral profiling), 3.A (categorization), and 7.A (budgeting) were rejected as the paper does not discuss financial behaviors, categories, or budgets. Topic 10.A (privacy) is not mentioned. The paper's international venue and algorithm focus justify 'algorithm-specific' designation."
limitations:
  - "Synthetic data generation quality depends on sufficient item preferences; poor performance when users < items."
  - "Drift detection using HDDM_W assumes bounded signals; not validated on financial data. [unacknowledged]"
  - "Experiments only on three non-financial datasets; generalization to PFMS untested."
  - "Assumes preference changes are captured by embedding modifications; may not model all real-world drift types."
remember_this:
  - "BPR matrix factorization with drift detection generates realistic synthetic preference streams."
  - "Hit rate drops to 0.6 after drift but recovers within a few batches."
  - "Adaptive models outperform static when user preferences change over time."
  - "Synthetic data fidelity requires more users than items to capture distribution."
```