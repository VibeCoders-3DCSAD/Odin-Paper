# Using Item Personality-Based Profiling in Music Recommender Systems

## Metadata

```yaml
---
paper_id: "10.1145/3779657.3779698"
designation: algorithm-specific
title: "Using Item Personality-Based Profiling in Music Recommender Systems"
authors: "de Goma, J.; Anonuevo, J. N.; Pangan, G. N.; Deang, J. J.; Villaluz, A."
year: 2025
venue: "2025 The 7th World Symposium on Software Engineering (WSSE 2025)"
odin_topics: ["5.B", "5.C", "12.A", "12.B"]
shorthand_tags: ["/profiling-cold-start", "/classifier-eval-metrics", "/eval-frameworks-survey", "/eval-ml-design"]
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

A hybrid recommender using personality-based item profiles and LightFM outperforms pure collaborative filtering, achieving 0.57 precision and 0.62 recall in cold-start scenarios.

## Problem and Motivation

Music recommender systems struggle with user variability and the cold-start problem, where new users have no interaction history. These problems reduce recommendation accuracy and user satisfaction, limiting the utility of personalized music services. Prior work had not systematically integrated personality profiles with hybrid models to address both issues simultaneously.

## Approach

- Dataset: 208 student respondents provided Big Five personality scores, genre preferences (max 5 of 10), and like/dislike ratings for 100 songs.
- Method: LightFM hybrid model combining collaborative filtering with user features (personality scores + genres) and item features (sonic features from Spotify API + computed item personality profiles).
- Item personality profile: 15-feature vector where each Big Five dimension is split into low/average/high, with proportions calculated from users who liked the item.
- Baseline: Pure collaborative filtering model using only interaction matrix (like/dislike).
- Evaluation: Offline (80/20 train/test split, 30 epochs, 0.02 learning rate) and online (20 new users rating top-10 recommendations from both models). Metrics: precision@10, recall@10, AUC, F1.

## Findings

1. Hybrid model with WARP loss achieved **0.46 precision, 0.64 recall, and 0.54 F1** on validation set — no severe overfitting unlike pure CF.
2. In online evaluation, the hybrid model (Model A) scored higher than pure CF (Model B): precision 0.57 vs 0.41, recall 0.62 vs 0.46, F1 0.58 vs 0.40.
- Users rated hybrid model higher on recommendation quality (3.7 vs 3.4) and user satisfaction (4.15 vs 3.55), but pure CF was perceived as more diverse (3.95 vs 3.75).
- Chi-square test showed statistically significant preference for hybrid model’s recommendation quality (p < 0.05).

## Key Figures and Tables

- Figure 1: Proposed model workflow → data collection → pre-processing → LightFM training → offline/online evaluation.
- Table 1: Training metrics (CF: recall 0.86, AUC 1.00) → CF overfits drastically on training data.
- Table 2: Validation metrics (Hybrid WARP: precision 0.46, recall 0.64, F1 0.54) → hybrid generalizes better.
- Table 5: Online evaluation precision/recall → hybrid beats CF by 0.16 precision, 0.16 recall.

## Key Equations

$$Proportion = \frac{\text{Number of users who liked item and have same BF degree}}{\text{Total number of users who liked the item}}$$
*Fraction of users with a specific Big Five level who liked this item.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| BFI | Big Five Inventory — personality test measuring five traits (openness, conscientiousness, extraversion, agreeableness, neuroticism). |
| IPP | Item Personality Profile — vector of 15 features (low/avg/high for each Big Five dimension) describing an item’s appeal across personality types. |
| UPP | User Personality Profile — normalized T-scores (mean 50, SD 10) converted to low (<45), average (45–55), or high (>55) categories. |
| LightFM | Python library for hybrid recommender systems combining user/item features with matrix factorization. |
| CF | Collaborative Filtering — recommendation based on user-item interaction patterns only, no content features. |
| BPR | Bayesian Personalized Ranking — loss function optimizing AUC by ranking positive items above negatives. |
| WARP | Weighted Approximate-Rank Pairwise — loss function optimizing top-k recommendation ranking. |
| Cold-start problem | Difficulty recommending to new users with no interaction history. |

## Critical Citations

- [Kleć et al., 2023] — Demonstrated that personality facets reduce recommendation error; basis for using Big Five in music RS.
- [Alharthi, 2015] — Introduced proportion-based item personality profiles; directly adapted for this paper’s IPP method.
- [Lu & Tintarev, 2018] — Showed personality-based re-ranking improves diversity and user satisfaction; used for online evaluation design.

## Relevance to Odin

**Topics:**

5.B — Profile Dynamics and the Cold-Start Problem

5.C — Financial Behavioral Profile Classification Algorithm

12.A — Evaluation Frameworks for Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly informs Odin’s approach to cold-start profiling by demonstrating that hybrid models (combining user features with interaction data) outperform pure collaborative filtering when user history is sparse. The LightFM architecture with WARP loss provides a concrete algorithmic template for Odin’s financial behavioral profile classification module, where new users have no spending history. The evaluation framework — combining offline metrics (precision/recall/AUC/F1) with online user-centric assessment (ResQue) — maps directly to Odin’s planned evaluation strategy under ISO 25010 and SUS.

**Directly justifies:**

- “Hybrid recommender systems incorporating user feature embeddings (personality, preferences) achieve 16 percentage points higher precision than pure collaborative filtering in cold-start scenarios (0.57 vs 0.41).”
- “WARP loss function outperforms BPR for top-k recommendation on sparse, imbalanced interaction data — applicable to Odin’s budget recommendation cold-start problem.”
- “Item personality profiles constructed from user-item affinity proportions enable content-based cold-start recommendations without requiring extensive interaction history.”
- “Offline metrics (precision@k, recall@k, AUC, F1) combined with user-reported quality and satisfaction produce a complete evaluation picture — aligns with Odin’s ISO 25010 + SUS design.”

**Limits of relevance:**

- Domain is music recommendation, not financial budgeting — the user-item interaction structure differs (likes vs. spending amounts).
- Personality traits (Big Five) are not equivalent to financial behavioral profiles — Odin profiles based on income stability and spending patterns, not psychological traits.
- Dataset size (208 users, 100 items) is small; scaling to Odin’s expected user base may require validation.
- No explicit temporal dynamics; Odin’s spending forecasting requires sequential data, which this paper does not address.

## Limitations

- Small sample (208 students) from a single university — not representative of Filipino young professionals broadly.
- Only 100 songs in the dataset; limited item diversity may inflate precision and recall artificially. [unacknowledged]
- Personality data was self-reported via survey; no validation against ground-truth listening behavior.
- No comparison against non-hybrid content-based methods; only pure CF baseline.
- Online evaluation used only 20 new users — too small for robust statistical inference beyond chi-square.

## Remember This

- 🔑 Hybrid model (LightFM + personality IPP) achieved **0.57 precision, 0.62 recall** — cold-start gains over pure CF.
- 💡 WARP loss beat BPR on sparse data — choose top-k optimization for cold-start recommendation.
- 📌 Users rated hybrid higher on quality (3.7 vs 3.4) and satisfaction (4.15 vs 3.55) — but pure CF felt more diverse.
- ⚠️ Music domain, not finance — transfer requires adapting features from personality to spending patterns.
