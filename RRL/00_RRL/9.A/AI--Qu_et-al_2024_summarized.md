# Budgeted Embedding Table For Recommender Systems

## Metadata

```yaml
---
paper_id: "10.1145/3616855.3635778"
designation: algorithm-specific
title: "Budgeted Embedding Table For Recommender Systems"
authors: "Qu, Y.; Chen, T.; Nguyen, Q. V. H.; Yin, H."
year: 2024
venue: "Proceedings of the 17th ACM International Conference on Web Search and Data Mining (WSDM '24)"
odin_topics: ["9.A"]
shorthand_tags: ["/mobile-technical-constraints"]
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

BET guarantees strict memory budget compliance while improving recommendation accuracy by adaptively sizing each user and item embedding via set-based fitness prediction.

## Problem and Motivation

Existing lightweight embedding methods either fail to strictly meet memory budgets or require inefficient instance-by-instance search. This limits deployment of recommender systems on resource-constrained local devices (e.g., mobile, IoT). No prior approach could both enforce a hard memory cap and efficiently search table-level embedding size assignments.

## Approach

- Pre-train a backbone recommender (NCF, NGCF, or LightGCN) with full-size embeddings (max dimension 128).
- Sample table-level actions: assign embedding sizes to all users and items by drawing from random probability distributions (power law, truncated normal, etc.) with a budget-aware sampler that caps total parameters.
- Represent each action as a set of users/items per embedding size; embed actions using DeepSets for permutation-invariant representation.
- Fitness prediction network (MLP-based) estimates action quality without full retraining, reducing evaluations from O(mT) to O(T).
- Three action selection strategies: greedy by predicted fitness, random for diversity, or nearest neighbor to the current best action.
- After T=50 iterations, selectively retrain top 5 actions from scratch to identify the optimal embedding table.

## Findings

1. On Gowalla with LightGCN at 90% sparsity, BET achieves **0.1620 Recall@20 and 0.1376 NDCG@20**, outperforming CIESS (0.1589/0.1353) and all other baselines.
2. BET strictly meets target sparsity (80%, 90%, 95%) whereas ESAPN and OptEmbed deviate (67–83%).
3. Paired t-tests show BET significantly beats best baseline in most settings (p < 0.05).

- DeepSets-based fitness predictor improves performance over a simple predictor and over random selection alone (Table 2).
- Increasing candidate actions m to 100 yields best results; performance stabilizes after 40 iterations.

## Key Figures and Tables

- Table 1: Full comparison on Gowalla and Yelp across three backbones → BET dominates at all sparsity levels; best results highlighted.
- Table 2: Selection method ablation → DeepSets fitness predictor outperforms random and simple predictor on both datasets.
- Figure 4: Sensitivity to m (20–100) → performance rises with m, saturating at 100.
- Figure 5: Sensitivity to T (iterations) → performance plateaus after ~40 iterations.

## Key Equations

$$d_i = \lfloor \tilde{p}_i \cdot w \cdot d_{max} \cdot (|U|+|V|) \rfloor$$
*Embedding size for user i = budget fraction times max dimension.*

$$\boldsymbol{h}_a = \frac{1}{d_{max}} \sum_{d=1}^{d_{max}} \boldsymbol{s}_d$$
*Action embedding = mean of set embeddings for each possible size.*

$$r_a = \frac{\text{eval}(\mathbf{E} \odot \mathbf{M}_a | \mathcal{D}_{val})}{\text{eval}(\mathbf{E} | \mathcal{D}_{val})}$$
*Fitness score = validation performance ratio relative to full embedding table.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| RS | Recommender systems – predict user preference for items. |
| BET | Budgeted Embedding Table – the proposed method. |
| Embedding table | Matrix storing vector representations of all users and items. |
| Sparsity ratio | Proportion of embedding parameters retained (e.g., 90% sparsity = 10% of original). |
| Table-level action | One assignment of embedding sizes to every user and item in the system. |
| DeepSets | Neural architecture that learns permutation-invariant set representations. |
| BPR | Bayesian Personalized Ranking – loss function for implicit feedback. |
| NCF / NGCF / LightGCN | Popular neural recommender models used as backbones. |

## Critical Citations

- [Chen et al., 2021] – Elastic embeddings for on-device recommenders; foundational to adaptive sizing.
- [Qu et al., 2023] – Continuous input embedding size search (CIESS); direct baseline for BET.
- [Liu et al., 2021] – Learnable embedding sizes via pruning thresholds; representative of sparsification methods.
- [Zaheer et al., 2017] – DeepSets; core architecture for BET's fitness predictor.

## Relevance to Odin

**Topics:**

9.A — Mobile-First Design Principles and Rationale

**Contribution to Odin:**

This paper provides a method to compress embedding tables under strict memory budgets while preserving model accuracy, directly supporting Odin’s mobile-first design where on-device storage and compute are constrained. Although BET targets recommender systems, its budget-aware action sampling and set-based fitness prediction are general techniques applicable to any embedding-based ML module Odin might employ (e.g., user behavioral profiling or category embedding). The paper demonstrates that hard memory caps can be enforced without manual coefficient tuning, which is critical for deploying Odin on diverse mobile hardware in Metro Manila.

**Directly justifies:**

- "BET achieves strict memory budget compliance without manually tuned trade-off coefficients, overcoming a key limitation of sparsification and RL-based embedding compression methods."
- "The set-based fitness predictor reduces evaluation cost from O(mT) to O(T), enabling efficient architecture search under mobile constraints."
- "On Yelp2018 with LightGCN at 90% sparsity, BET achieves 0.0816 NDCG@20 versus 0.0762 for the best baseline CIESS, demonstrating that adaptive per-entity embedding sizes improve accuracy under identical memory budgets."
- "BET guarantees that total embedding parameters never exceed a pre-specified cap by using a bounded sampler that directly allocates parameters from probabilistic distributions."

**Limits of relevance:**

- Paper focuses on recommender systems (user–item interaction prediction), not personal finance management or budgeting.
- Datasets are user–item click/interaction logs, not financial transaction records with seasonal or cultural patterns.
- No evaluation on cold-start scenarios or very sparse user histories, which are common in new PFMS users.
- Mobile constraints are assumed but not tested on actual mobile hardware or battery-limited environments.

## Limitations

- Hyperparameter sensitivity: number of sampled actions m and iterations T require tuning (optimal m=100, T=50).
- Fitness predictor may overfit if action diversity is low; the random selection strategy mitigates this but adds variance.
- Evaluation only on two datasets (Gowalla, Yelp2018); generalizability to other domains (e.g., finance) not tested. [unacknowledged]
- Does not address streaming or continually evolving user/item sets; future work noted but not implemented.
- Selective retraining still requires training top 5 actions from scratch, which adds final computational cost.

## Remember This

- 🔑 **BET achieves 0.1620 Recall@20 at 90% sparsity** on Gowalla — beats all baselines.
- 📌 Guarantees memory budget without manual coefficient tuning — essential for mobile deployment.
- 🧠 Set-based fitness predictor cuts evaluation cost by ~10× vs. full retraining per action.
- ⚠️ Designed for recommenders — transfer to Odin's profiling/forecasting modules needs validation.
