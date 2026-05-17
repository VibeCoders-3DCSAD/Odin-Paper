# Modelling Concept Drift in Dynamic Data Streams for Recommender Systems

## Metadata

```yaml
---
paper_id: "10.1145/3707693"
designation: algorithm-specific
title: "Modelling Concept Drift in Dynamic Data Streams for Recommender Systems"
authors: "Caroprese, L.; Pisani, F. S.; Veloso, B. M.; Konig, M.; Manco, G.; Hoos, H.; Gama, J."
year: 2025
venue: "ACM Transactions on Recommender Systems"
odin_topics: ["5.B", "5.C", "6.A", "8.A", "12.B"]
shorthand_tags: ["/concept-drift", "/profiling-cold-start", "/temporal-dependency", "/eval-ml-design"]
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

A stream-based data generator using user/item embeddings and concept drift detection produces realistic synthetic preference data for evaluating recommender systems.

## Problem and Motivation

Public datasets for recommender systems lack temporal dynamics, ignoring how user preferences evolve over time. This limits the development and evaluation of algorithms that must adapt to changing tastes. Existing synthetic data generators do not model concept drift, leaving a gap between offline benchmarks and real-world streaming scenarios.

## Approach

- **Preference model**: Bayesian Personalized Ranking (BPR) maps users and items to a K‑dimensional latent space; preferences arise from geometric closeness.
- **Graph representation**: Tripartite graph of users, items, and feature nodes; concept drift corresponds to rewiring or dimension changes.
- **Drift detection**: HDDMW (Hoeffding’s bounds with EWMA) monitors loss on test shards; warns or signals drift when error increases.
- **Adaptation on drift**: Extend latent dimensions (ΔK), retrain with penalty on deviation from previous embeddings (loss Ld).
- **No‑drift update**: Generate synthetic samples from current model (nS = current shard size) and combine with real data for continual learning.
- **Synthetic generation**: Sample items per user proportionally to predicted scores; user/item frequencies follow Zipf distributions.

## Findings

1. On the MIND dataset, **HR@5 averaged ~0.6–0.8** across batches; drift detection flagged changes aligned with news topic shifts.
2. On the Amazon Video Games dataset (original orientation, many items), synthetic frequency distributions diverged from real data due to insufficient item preferences.
3. **Inverting users and items** (fewer items than users) produced close frequency matches; HR@5 reached ~0.8 after adaptation.
4. On Yoochoose, a single major drift reduced HR@5 from ~0.7 to ~0.5, with recovery within batches.

- BPR outperformed a variational autoencoder on the inverted Amazon dataset (**HR@5 ~0.8 vs ~0.6**) when new items appeared over time; VAE was better on stable MIND data.
- A model trained only on the first regime performed poorly on later regimes, confirming drift necessity.

## Key Figures and Tables

- Figure 3: Loss over batches (MIND) → stable with warnings; drifts marked in red correspond to news topic changes.
- Figure 4: HR@5/10 over batches (MIND) → dips after drift warnings, recovers within batches.
- Figure 8: Frequency distributions (Amazon original) → synthetic (red) diverges from real (blue); poor fit.
- Figure 13: Frequency distributions (inverted Amazon) → synthetic closely matches real; good fit.
- Figure 15-17: BPR vs VAE HR@5 → BPR adapts better to new items; VAE stable on homogeneous data.

## Key Equations

$$L_{bpr}(M|V) = \sum_u \sum_{i \prec_u j} \log \sigma\big(p_u^T (q_i - q_j)\big)$$
*BPR loss: maximizes likelihood that preferred item i ranks above non‑preferred j.*

$$L_d(M'; M, R^{(t)}) = L_c(M'; R^{(t)}) + \delta\sum_{u,k}|p'_{u,k} - p_{u,k}| + \dots$$
*Drift‑adaptation loss penalizes deviation from previous embeddings while allowing new dimensions.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| BPR | Bayesian Personalized Ranking — learns item order from implicit feedback. |
| MF | Matrix Factorization — factorizes user‑item matrix into latent embeddings. |
| Concept drift | Change in data distribution over time (e.g., user taste shifts). |
| HDDMW | Hoeffding Drift Detection Method with moving weighted average — uses EWMA to detect drift. |
| EWMA | Exponentially Weighted Moving Average — gives more weight to recent observations. |
| HR@k | Hit Rate at k — proportion of test items ranked in top‑k recommendations. |
| Regime | A period where the underlying data distribution is stable. |
| Cold‑start | Problem of recommending to new users or items with no history (mentioned as future work). |

## Critical Citations

- [Rendle et al., 2009] — BPR loss function and embedding framework this work builds on.
- [Gama et al., 2004] — Foundational drift detection method (DDM) adapted into HDDMW.
- [Bifet & Gavalda, 2007] — Adaptive Windowing (ADWIN) for change detection; alternative to HDDMW.
- [Koren, 2009] — Temporal dynamics in collaborative filtering, modeling gradual drifts.
- [Veloso et al., 2021] — Previous work on hyper‑parameter optimization for latent spaces in streaming RS.

## Relevance to Odin

**Topics:**

5.B — Profile Dynamics and the Cold-Start Problem

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

8.A — Anomaly Detection in Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly informs Odin's need to detect and adapt to changes in user financial behavior (concept drift). The drift detection framework (monitoring loss on incoming transaction shards, triggering retraining when error rises) justifies a similar mechanism in Odin's profiling and forecasting modules: as a user's spending patterns shift (e.g., new job, holiday season), the system must update its behavioral profile and budget recommendations. The embedding‑based BPR model, while designed for recommendations, provides a template for representing users in a latent financial space. The paper's evaluation of continual learning (generating synthetic samples to retain past knowledge) supports Odin's design of a lightweight online update strategy without storing full history. The comparative analysis of BPR vs VAE under item‑arrival drift (inverted Amazon) shows that adaptive models outperform static ones when new categories appear — directly relevant to Odin's handling of new expense types or merchants.

**Directly justifies:**

- “Concept drift in user preferences can be detected online by monitoring a loss function on test shards using HDDMW, triggering model retraining when error exceeds Hoeffding bounds.”
- “When a drift is detected, extending the latent dimension (ΔK) and penalizing deviation from prior embeddings (Ld loss) balances adaptation with stability.”
- “A model trained only on historical data (first regime) degrades sharply on later regimes; continual learning with synthetic sample replay maintains performance.”
- “On streams with many new items appearing over time, an adaptive BPR model achieves HR@5 ~0.8, outperforming a fixed‑catalog VAE (HR@5 ~0.6).”
- “Cold‑start handling (new users/items) is identified as a future direction, but the proposed graph‑based drift modeling provides a foundation for addressing it.”

**Limits of relevance:**

- Domain is e‑commerce/news recommendation, not personal finance; spending behavior drift may have different temporal characteristics.
- Uses implicit binary feedback (click/read), whereas Odin has transaction amounts and categories.
- No evaluation on financial data or Philippine user populations.
- Cold‑start solution is not implemented; only mentioned as future work.
- Assumes ability to sample negative items uniformly at random, which may not hold for sparse financial transactions.

## Limitations

- The approach assumes geometric closeness in latent space as the preference model; other preference structures (e.g., Markovian) are not handled. [unacknowledged]
- Synthetic generation fidelity depends heavily on sufficient item preferences; fails when items outnumber users (Amazon original orientation).
- Drift detection using loss on test shards requires a held‑out set; not evaluated in pure online settings where labels arrive late.
- The method extends latent dimensions on drift but does not prune obsolete dimensions, potentially increasing memory over time. [unacknowledged]
- No user study or qualitative validation that generated drifts match real preference evolution in financial contexts.

## Remember This

- 🔑 **BPR adapts to new items** — HR@5 ~0.8 on inverted Amazon vs VAE’s ~0.6 when catalog grows.  
- 📌 **Drift kills static models** — A model frozen after first regime fails on later data; continual learning required.  
- 💡 **Extend dimensions on drift** — Penalty on embedding change (Ld) balances new patterns vs old knowledge.  
- ⚠️ **Cold‑start not solved** — New users/items remain future work; Odin must handle this separately.  
- 🔍 **Fidelity requires enough item samples** — Synthetic data matches real only when items have many preferences.
