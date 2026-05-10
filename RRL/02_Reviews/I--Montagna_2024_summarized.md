# Integration of Explainability in Recommender Systems to Enhance Enterprise Value Strategies

## Metadata

```yaml
---
paper_id: "a6b7c8d9-e0f1-4a2b-8c3d-4e5f6a7b8c9d"
designation: international
title: "Integration of Explainability in Recommender Systems to Enhance Enterprise Value Strategies"
authors: "Montagna, A."
year: 2024
venue: "University of Padova (PhD Thesis)"
odin_topics: ["C.2", "J.1"]
shorthand_tags: ["/budget-rec-algorithms", "/budget-algo-justification", "/eval-frameworks", "/user-trust"]
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[x]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
---
```

## TL;DR

Balancing business value and explainability in recommender systems improves user trust and adoption without catastrophic accuracy loss, demonstrated by the XVMF model.

## Problem and Motivation

Recommender systems optimize business value (profit, CTR) but operate as black boxes, reducing user trust and adoption. This opacity prevents enterprises from confidently adopting AI-driven recommendations, especially in high-stakes domains like finance. No prior model systematically balanced value generation with quantitative explainability metrics.

## Approach

- Systematic literature review of Value-Aware Recommender Systems (VARS) following PRISMA guidelines, analyzing 109 papers.
- Taxonomy of VARS algorithms: post-processing (value ranking, value policy), in-processing (value objective), and value reinforcement (RL).
- Proposed XVMF (Explainable Value-aware Matrix Factorization) – extends matrix factorization with two regularization terms: explainability power (Eui) and item business value (vi).
- Experiments on Yelp (124,999 interactions) and Amazon Tools & Home Improvement (134,323 interactions) datasets.
- Evaluation metrics: NDCG (accuracy), NDCV (value-aware ranking), E-NDCG (explainability quality).

## Findings

1. On Yelp, XVMF achieved **0.2493% NDCG** vs MF 0.1281% and EMF 0.1003% – a 94% relative improvement.
2. XVMF-v (value-optimized) on Amazon reached 0.1154% NDCV vs MF 0.0792% – a 46% gain.
3. XVMF-e (explainability-optimized) on Amazon achieved 0.1723% E-NDCG; MF scored 0.0836% and EMF 0.0000%.

- Performance degrades sharply when regularization terms (λ for explainability, δ for value) exceed 0.01 on Yelp and 0.05/0.005 on Amazon.
- Most surveyed graph-based explainable recommenders (83%) rely on qualitative case studies, lacking quantitative explanation evaluation.

## Key Figures and Tables

- Figure 3.1: Yelp single-parameter variation → optimal λ=0.001 for E-NDCG; δ=0.001 for NDCV.
- Figure 3.2: Yelp heatmaps → best trade-off region at λ≤0.01 and δ≤0.01.
- Figure 3.3: Amazon single-parameter → best E-NDCG at λ=0.01; NDCV peaks at δ=0.001.
- Table 3.5: Yelp metrics → XVMF outperforms MF and EMF across all three metrics.
- Table 3.6: Amazon metrics → XVMF-v achieves highest NDCV (0.1154%); XVMF-e highest E-NDCG (0.1723%).

## Key Equations

$$L = \sum_{(u,i)\in S} (r_{u,i} - p_u \cdot q_i^T)^2 + \frac{\beta}{2}(\|p_u\|^2 + \|q_i\|^2) + \|p_u - q_i\|^2(\lambda W_{u,i} + \delta v_i)$$
*XVMF loss: balances accuracy, explainability (λW), and business value (δv).*

$$E\text{–NDCG} = \frac{E\text{–DCG}_u}{E\text{–IDCG}}$$
*Explainable NDCG: ranks explainability power of recommended items, not just relevance.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| VARS | Value-Aware Recommender System – optimizes business metrics (profit, CTR) alongside user relevance. |
| XVMF | Explainable Value-aware Matrix Factorization – proposed model balancing accuracy, explainability, and value. |
| NDCV | Normalized Discounted Cumulative Value – ranking metric that weights items by their business value. |
| E-NDCG | Explainable NDCG – measures how well the top-N list can be explained to users. |
| Explainability Power | A score (Eui) measuring how many similar users rated an item highly, used to justify recommendations. |

## Critical Citations

- [De Biasio et al., 2023] — First systematic review and taxonomy of VARS; foundational for Odin's algorithm selection.
- [Abdollahi & Nasraoui, 2016] — Introduced Explainable Matrix Factorization (EMF) and MEP/MER metrics; basis for XVMF.
- [Coba et al., 2019] — Proposed E-NDCG metric and NEMF model; corrects position bias in explainability evaluation.
- [Tintarev & Masthoff, 2015] — Definitive guidelines for designing and evaluating explainable recommender systems.

## Relevance to Odin

**Topics:**

C.2 — Budget Recommendation Algorithm

J.1 — System Evaluation

**Contribution to Odin:**

This thesis directly informs Odin's budget recommendation module by demonstrating that value-aware optimization (analogous to maximizing user budget adherence or savings) can be quantitatively balanced with explainability, a critical requirement for user trust in personal finance apps. The XVMF model provides a tunable framework where Odin could prioritize either recommendation value (e.g., surplus allocation efficiency) or explanation quality (e.g., "why this budget limit") via hyperparameters. Furthermore, the systematic VARS taxonomy helps Odin designers evaluate candidate algorithms (RL, constraint optimization, post-processing) for budget recommendation based on their value optimization approach. The critique of graph-based explainable systems highlights the need for Odin to adopt quantitative evaluation metrics rather than qualitative examples when justifying explainability features.

**Directly justifies:**

- "Value-aware recommender systems that maximize profit or CTR can be extended with explainability regularization without complete loss of recommendation accuracy (XVMF achieves 0.2493% NDCG vs MF 0.1281% on Yelp)."
- "The trade-off between business value and explainability is controlled by hyperparameters (λ, δ); optimal balance occurs at low values (λ=0.001, δ=0.001 for Yelp), beyond which both metrics degrade sharply."
- "83% of graph-based explainable recommender systems lack quantitative evaluation of explanation quality, relying on qualitative case studies — a gap Odin's evaluation framework should avoid."
- "Explainable Matrix Factorization (EMF) with neighborhood-based explainability power (Eui) improves explanation coverage but requires careful tuning to avoid accuracy loss."

**Limits of relevance:**

- Thesis uses product recommendation datasets (Yelp, Amazon) with item profit as business value; Odin's budget recommendation involves different value constructs (user adherence, savings rate).
- Experiments are offline and do not measure actual user trust or adoption in a financial context.
- The XVMF model assumes item-level business value is known and static; Odin's budget categories may have dynamic or user-defined value weights.
- No Filipino demographic or spending behavior data used; cultural factors affecting explanation preferences are unaddressed.

## Limitations

- The thesis does not validate XVMF on personal finance data; results may not generalize to budget recommendation tasks.
- Explainability metric E-NDCG relies on user-neighborhood similarity, which may not capture all explanation styles (e.g., feature-based, counterfactual). [unacknowledged]
- Systematic review excludes non-English and unpublished industrial VARS implementations, potentially missing practical approaches.
- XVMF's value term vi assumes uniform item value across users; real budgets have user-specific opportunity costs.
- No user study measuring actual trust or adoption improvement from explainability features.

## Remember This

- 🔑 **XVMF boosted NDCV by 46% over MF** on Amazon – value + explainability can coexist.
- 📌 Optimal trade-off at λ,δ ≤ 0.01 – beyond that, both metrics collapse.
- ⚠️ 83% of graph-based explainable RSs skip quantitative evaluation – don't follow that pattern.
- 💡 Explainability power (Eui) uses neighbor ratings to justify recommendations – works without natural language.
- 🧠 XVMF's loss function adds two regularization terms to MF – one for explainability (λW), one for value (δv).
