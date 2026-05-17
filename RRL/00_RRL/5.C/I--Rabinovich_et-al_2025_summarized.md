# Mapping Financial Mindsets: A Two-Stage Unsupervised Framework for Behavioral Profiling Using High-Dimensional Psychometric Data

## Metadata

```yaml
---
paper_id: "d9b3c2a1-4e5f-6a7b-8c9d-0e1f2a3b4c5d"
designation: algorithm-specific
title: "Mapping Financial Mindsets: A Two-Stage Unsupervised Framework for Behavioral Profiling Using High-Dimensional Psychometric Data"
authors: "Rabinovich, I.; Rabinovich, R.; Ashburn, N.; DeGeare, M."
year: 2025
venue: "Unknown"
odin_topics: ["5.A", "5.B", "5.C"]
shorthand_tags: ["/profiling-role", "/profile-dimensions", "/profiling-cold-start", "/classification-vs-clustering", "/classifier-candidates", "/classifier-eval-metrics"]
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

Two-stage unsupervised learning (UMAP + spectral clustering) identifies psychologically interpretable financial behavior profiles from psychometric data, validated across proprietary (N=337) and nationally representative U.S. (N=5,897) datasets.

## Problem and Motivation

Existing financial segmentation relies on spending patterns or demographics, overlooking the psychological traits (motivation, self-control, emotional resources) that drive financial behavior. Without psychometric profiles, personalized financial tools cannot address why users struggle to follow through. Prior work lacked a replicable, scalable framework to integrate multidimensional psychometric data into coherent behavioral profiles.

## Approach

- Dataset 1: Proprietary 122-item psychometric assessment (N=337, eight domains: Character Strengths, Attitudes & Capabilities, Psychological Capital, Motivation, Financial Behavior, Positive Functioning, Construal Level, Literacy).
- Dataset 2: U.S. CFPB National Financial Well-Being Survey (N=5,897, five domains: Capability, Budgeting & Saving, Planning, Social Support, Literacy).
- Stage 1: Domain scoring via UMAP embedding + anchor-based projection (linear or geodesic) to produce unidimensional, sample-independent scores.
- Stage 2: Second-stage UMAP on domain scores, then spectral clustering to identify latent behavioral profiles.
- Internal validation: silhouette score, Calinski–Harabasz index, adjusted Rand index (ARI) across 100 random seeds.
- External validation: associations with life satisfaction, psychological well-being, perceived financial health, and material hardship.

## Findings

1. Silhouette scores: **0.569** (proprietary) and 0.500 (CFPB) — clear cluster separation in embedded space.
2. Cluster stability: mean ARI = 0.916 (proprietary) and 0.814 (CFPB) across random seeds; subsample ARI = 0.970–0.994.
3. Demographics explain little cluster variance: McFadden pseudo-R² = 0.091 (proprietary) and 0.061 (CFPB).

- Cluster membership explains 44% (CFPB) and 61% (proprietary) of variance in perceived financial health — far exceeding demographics (R²=0.25 and 0.16).
- Supervised ensemble classifier assigns new individuals to existing clusters with **79.2% accuracy** (5-fold CV), enabling cold-start profiling.
- Seven interpretable clusters emerged per dataset, ordered along a global functioning gradient with distinct psychological configurations.

## Key Figures and Tables

- Figure 1: UMAP projections of both datasets colored by spectral cluster assignments → clusters show clear separation with nonlinear geometry.
- Figure 3: Heatmaps of mean domain scores per cluster → each cluster has a distinct psychological profile (e.g., "low capability, low resources" vs. "highly resourced and effective").
- Figure 5: Variance explained (R²) bar charts → clusters add 14–45 percentage points beyond demographics for financial health and life satisfaction.
- Table 5a/5b: Descriptive cluster profiles → labels like "cognitively engaged, moderately supported" and "highly organized, cautious executor" summarize each segment.

## Key Equations

$$s_i = \frac{(p_i - v^e_{\min}) \cdot (v^e_{\max} - v^e_{\min})}{\|v^e_{\max} - v^e_{\min}\|^2}$$
*Linear anchor projection: participant’s position along domain axis from minimum to maximum anchor.*

$$CPSI_{i,j} = \frac{1}{1 + d(i,j)}$$
*Cluster-Pair Similarity Index: inverse Euclidean distance between cluster centroids (0 to 1).*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| UMAP | Uniform Manifold Approximation and Projection — a nonlinear dimensionality reduction method that preserves local and global data structure. |
| Spectral clustering | A graph-based clustering method that captures non-convex cluster shapes using eigenvectors of a similarity matrix. |
| Anchor-based projection | Scoring method that maps responses onto a fixed axis defined by theoretical minimum and maximum profiles, independent of sample distribution. |
| CFPB | U.S. Consumer Financial Protection Bureau — conducted the nationally representative financial well-being survey. |
| ARI | Adjusted Rand Index — measures similarity between two clustering solutions, corrected for chance (1 = perfect agreement). |
| PCA | Principal Component Analysis — linear dimensionality reduction. |

## Critical Citations

- [Kahneman & Tversky, 1979] — Foundational behavioral finance theory of cognitive biases in decision-making under risk.
- [McInnes et al., 2018] — Introduced UMAP, the nonlinear embedding method central to the framework's two-stage approach.
- [Ng et al., 2002] — Spectral clustering algorithm used in Stage 2 to identify latent behavioral profiles.
- [Prochaska & DiClemente, 1983] — Transtheoretical Model of Change, grounding the Financial Behavior domain in stages-of-change theory.

## Relevance to Odin

**Topics:**

5.A — Financial Behavioral Profiles in Personal Finance

5.B — Profile Dynamics and the Cold-Start Problem

5.C — Financial Behavioral Profile Classification Algorithm

**Contribution to Odin:**

This paper directly informs Odin's financial behavioral profiling module by providing a validated unsupervised framework (UMAP + spectral clustering) that identifies psychologically meaningful profiles from psychometric survey data — exactly the type of input Odin will collect from users (e.g., attitudes, motivations, self-reported behaviors). The two-stage design, which separates within-domain scoring from cross-domain clustering, is directly applicable to Odin's need to combine multiple behavioral indicators (financial literacy, spending attitudes, self-regulation) into a coherent user profile without manual category definitions. Most critically, the paper demonstrates that a supervised classifier can assign new users to existing clusters with 79% accuracy — a solution to Odin's cold-start profiling problem, where new users have no transaction history and must be classified using an initial questionnaire.

**Directly justifies:**

- "Two-stage unsupervised learning (UMAP + spectral clustering) identifies psychologically coherent financial behavior profiles with silhouette scores of 0.50–0.57, demonstrating internal validity without ground-truth labels."
- "A supervised ensemble classifier achieves 79.2% accuracy assigning new individuals to existing clusters, enabling cold-start behavioral profiling for users with no transaction history."
- "Demographic variables (age, education, income) explain only 6–9% of variance in cluster membership, confirming that psychometric profiles capture behavioral variation not reducible to socioeconomic status."
- "Cluster membership accounts for 44% of variance in perceived financial health in a nationally representative sample, exceeding the 25% explained by demographics alone."

**Limits of relevance:**

- All data are from U.S. populations; Filipino financial behaviors, cultural obligations (e.g., family remittances, utang na loob), and psychometric scale validity may differ substantially.
- Cross-sectional design; no evidence on whether profiles change over time or respond to interventions — Odin's profiling dynamics (topic 5.B) will require longitudinal adaptation.
- Proprietary sample is modest (N=337) and skewed younger; cluster stability in smaller or more homogeneous populations (e.g., Metro Manila young professionals) is untested.
- Framework requires a sufficiently rich psychometric instrument (≥5 domains, ≥5 items per domain) — may need adaptation for shorter onboarding surveys.

## Limitations

- Cross-sectional data cannot assess how profiles evolve with life events or financial habits — a key unknown for Odin's dynamic profiling. [unacknowledged]
- Self-report measures may introduce social desirability and recall bias, affecting the geometry of learned representations.
- Proprietary dataset is modest (N=337) and drawn from a convenience sample (advisors, students, voluntary users) — not representative of any population.
- Hyperparameter sensitivity (UMAP n_neighbors, spectral clustering gamma) requires manual tuning; no fully automated selection procedure provided.
- No validation on non-U.S. or non-English populations; applicability to Filipino cultural and economic context is untested.

## Remember This

- 🔑 **Silhouette 0.57 (proprietary) / 0.50 (CFPB)** — two-stage UMAP+spectral clustering yields cleanly separated financial mindset profiles.
- 📌 **79% assignment accuracy** — new users can be profiled without transaction history, solving Odin's cold-start problem.
- 💡 **Clusters explain 44% of financial health variance** — psychometric profiles far outperform demographics (25%) in predicting outcomes.
- ⚠️ U.S. data only — Filipino validation required before direct adoption in Odin's profiling module.
