# A Recommendation System for Participatory Budgeting

## Metadata

```yaml
---
paper_id: "123e4567-e89b-12d3-a456-426614174000"
designation: algorithm-specific
title: "A Recommendation System for Participatory Budgeting"
authors: "Leibiker, G.; Talmon, N."
year: 2023
venue: "Proceedings of the 22nd International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2023)"
odin_topics: ["5.C", "7.C", "12.B"]
shorthand_tags: ["/classifier-candidates", "/classifier-eval-metrics", "/budget-rec-formulation", "/budget-rec-algo-candidates", "/budget-rec-algo-tradeoffs", "/budget-rec-eval-metrics", "/eval-ml-design"]
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

Predicting missing voter preferences in participatory budgeting using binary classification (XGBoost) achieves higher budget allocation accuracy than sampling, enabling all voters to participate with fewer inputs.

## Problem and Motivation

Participatory budgeting voters face information overload when evaluating many projects, leading to incomplete ballots. This reduces participation and undermines democratic budget decisions. Existing approaches either collect full ballots (high cognitive burden) or sample voters (excluding many voices).

## Approach

- Dataset: 10 real-world PB instances from Warsaw (2020–2023), 2,614–10,424 voters, 67–111 projects, approval rate ≈10%.
- Simulated partial ballots by hiding preferences; defined sample degree (0.1–0.9) and LV degree (0.1–1) for training voters.
- Prediction methods: Matrix Factorization (MF), Factorization Machines (FM), and binary classification (XGBoost with imbalance weighting).
- Sampling modules: random (expose random projects), offline (expose popular/consensus/controversial projects), online (adaptive controversial).
- Evaluation metrics: precision, recall, F1 for ballot completion; Symmetric Distance (SD) and Fractional Allocation (FA) score for winning bundle vs. ground truth.

## Findings

- Classification (XGBoost) outperformed MF and FM across all sampling setups.
- Online and offline-popularity sampling achieved higher FA scores than random sampling.
- At 10% sample degree, classification-online matched the FA score of sampling at 30% sample degree, requiring less voter input.
- FA and SD improved monotonically with sample degree and LV degree (sanity test confirmed).
- Classification-online and classification-offline-popularity performed best overall, especially at low sample degrees (0.1–0.3).

## Key Figures and Tables

- Table 1: Dataset characteristics (voters, projects, budget, % approved) → 10 PB instances from Warsaw districts.
- Figures 7–12: FA score heatmaps across sample degree and LV degree → classification-online and offline-popularity achieve highest FA.
- Figures 13–18: SD heatmaps → same trend; higher sample degree reduces SD.
- Figure 5 & 6: Sanity check heatmaps → FA increases and SD decreases with more data, as assumed.

## Key Equations

$$FA = \frac{\sum_{p \in pb \cap rb} cost(p)}{B}$$
*Fraction of budget correctly allocated to predicted winning projects.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| PB | Participatory Budgeting – community decides public spending. |
| RS | Recommendation System – predicts user preferences for items. |
| CF | Collaborative Filtering – recommends based on similar users’ opinions. |
| MF | Matrix Factorization – factorizes user-item matrix into latent factors. |
| FM | Factorization Machines – hybrid CF that learns feature interactions. |
| XGBoost | eXtreme Gradient Boosting – ensemble of decision trees with gradient boosting [think: high-performance tree model]. |
| FA score | Fractional Allocation – sum cost of correctly predicted winning projects divided by budget. |
| SD | Symmetric Distance – number of projects that differ between real and predicted winning bundles. |

## Critical Citations

- [Aziz and Shah, 2021] – Foundational survey of PB models and approaches.
- [Rendle, 2010] – Introduced Factorization Machines for sparse prediction tasks.
- [Chen and Guestrin, 2016] – XGBoost algorithm, the basis for the best-performing predictor.
- [Talmon and Faliszewski, 2019] – Defined greedy approval voting rule used in this paper.

## Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

7.C — Budget Recommendation Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper demonstrates that binary classification (XGBoost) outperforms collaborative filtering methods (MF, FM) for predicting missing user preferences from partial inputs, directly informing Odin's cold-start profile classification module. The evaluation framework—using FA score to measure budget allocation correctness rather than just ballot accuracy—provides a template for Odin's module-level evaluation beyond simple classification metrics. Although the domain is public budgeting, the technique of adaptively sampling the most controversial items (online controversial) to maximize prediction accuracy with minimal user input is directly transferable to Odin's preference elicitation for budget recommendation.

**Directly justifies:**

- "XGBoost with weighted loss functions handles imbalanced approval data (≈10% approval rate) and improves prediction of minority class compared to MF and FM."
- "Online adaptive sampling (revealing most controversial projects first) yields higher prediction accuracy than random sampling when collecting partial user preferences from sparse data."
- "Fractional Allocation (FA) score—sum of correctly predicted winning project costs divided by total budget—captures financial impact of prediction errors better than per-item accuracy metrics."
- "Greedy approval (funding highest-approved projects until budget exhausted) serves as a baseline budget allocation rule that balances popularity and cost constraints."

**Limits of relevance:**

- Domain is public participatory budgeting (collective spending), not personal budget management (individual spending).
- Data from Warsaw, Poland; not representative of Filipino young professionals' financial behavior or cultural spending patterns.
- No temporal dynamics or sequential transaction history; predictions are static per ballot, not time-series forecasting.
- Evaluation assumes full ground truth ballots exist; Odin's cold-start has no prior user data.

## Limitations

- Only tested on approval-based combinatorial PB; other PB variants (e.g., cumulative voting) not evaluated.
- Data from a single country (Poland); generalizability to other cultural contexts unknown. [unacknowledged]
- No comparison to deep learning methods (e.g., neural collaborative filtering).
- Interactive correction loop (voter refining predictions) proposed but not implemented or tested.
- Real-time deployment constraints (latency, mobile compute) not considered. [unacknowledged]

## Remember This

- 🔑 XGBoost beats MF and FM for predicting missing preferences in sparse approval data.
- 📌 At 10% sample degree, classification-online matches sampling at 30% – less input, same budget accuracy.
- 💡 FA score measures budget-wise correctness, not just ballot accuracy – relevant for Odin's module evaluation.
- ⚠️ Domain is public budgeting – apply the ML methods, not the PB context, to personal finance.
- ✅ Online adaptive sampling (most controversial first) maximizes prediction gain per user question.
