# Analysing community-level spending behaviour contributing to high carbon emissions using stochastic block models

## Metadata

```yaml
---
paper_id: "10.1038/s41598-025-14364-7"
designation: algorithm-specific
title: "Analysing community-level spending behaviour contributing to high carbon emissions using stochastic block models"
authors: "Simeonov, O.; Restocchi, V.; Goddard, B. D."
year: 2025
venue: "Scientific Reports"
odin_topics: ["4.A", "4.B", "5.A", "5.C", "11.B"]
shorthand_tags: ["/pfms-intelligent-features", "/pfms-limitations", "/pfms-transferable", "/profiling-role", "/classification-vs-clustering", "/classifier-candidates", "/value-driven-retention"]
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

Stochastic block modeling on bipartite spending networks identifies consumer groups with homogeneous carbon emission profiles, enabling scalable targeted interventions.

## Problem and Motivation

Policymakers need to identify consumer groups with similar spending and carbon emissions patterns to design effective group-level interventions, but existing clustering methods rely on demographics or single-category analysis. Financial transaction datasets offer rich behavioural data, yet no prior work applied stochastic block models to capture multi-category spending interactions for sustainability targeting. Without unbiased, network‑based segmentation, scalable carbon‑reduction strategies remain impractical.

## Approach

- Dataset: 1,362 UK customers (2021–2023) from a sustainable banking FinTech; filtered to 272 customers with ≥30 transactions across ≥10 MCCs.
- Bipartite network: customers on one side, merchant category codes (MCCs) on the other; edges weighted by transaction count or spending amount normalised by category average.
- Community detection: degree-corrected nonparametric hierarchical stochastic block model (SBM) applied to the bipartite network via graph‑tool.
- Carbon estimation: Trendl et al. multipliers (LCFS + UKMRIO) mapped from COICOP to MCCs.
- Validation: synthetic dataset (1M transactions, 3K customers) replicated real distributions; Kolmogorov‑Smirnov test confirmed fidelity.

## Findings

1. Unweighted SBM produced clusters where customer transaction counts per MCC were tightly clustered around the mean, with near‑zero standard deviation.
2. **Weighted SBM (spending normalised by category average) produced clusters where percentage spending per category fell within one median absolute deviation (MAD) of the population median for 71/80 clusters (≥30 customers).**
3. Under half‑MAD threshold, 43/80 clusters still aligned; unweighted SBM had <50% within one MAD.
4. Specific emission drivers emerged per cluster: grocery (cluster 22), taxi (clusters 17‑18), service stations (clusters 3,11,12), public transport (cluster 20).

- Hierarchical SBM revealed nested community structures, allowing analysis at multiple granularity levels.

## Key Figures and Tables

- Figure 3: Bipartite network with coloured communities and blue overlay → hierarchical structure: lower‑level sub‑communities aggregate into broader spending groups.
- Figure 4: Emissions heatmap across clusters → taxi, service stations, and public transport dominate different clusters’ carbon footprints.
- Figure 5: Weighted SBM spending percentages heatmap → cluster spending equals population spending within one MAD for all top‑10 categories.
- Figure 7: Taxi emissions per cluster → cluster 17 has high transaction count (target frequency), cluster 18 has high spend per transaction (target amount).

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| SBM | Stochastic block model: probabilistic method that groups nodes by connection patterns. |
| MCC | Merchant category code: four‑digit code assigned to each transaction by card networks. |
| MAD | Median absolute deviation: median of absolute deviations from the median; robust measure of spread. |
| Bipartite network | Graph with two node types; edges only connect nodes of different types. |
| COICOP | Classification of Individual Consumption According to Purpose: UN expenditure classification. |
| LCFS | Living Costs and Food Survey: UK household expenditure survey. |
| UKMRIO | UK Multi‑Region Input‑Output: model of inter‑industry flows and environmental impacts. |

## Critical Citations

- [Trendl et al., 2023] — Provides the open‑source carbon multipliers that map MCCs to emissions; foundational to the study’s carbon estimation.
- [Peixoto, 2014] — Introduced hierarchical nonparametric SBM with high resolution limits; directly implemented in this study.
- [Holland et al., 1983] — Original SBM formulation; the probabilistic basis for all later extensions.
- [Wells et al., 2025] — Concurrent work using k‑means on financial data to segment UK households by carbon footprint; cited as contrast to SBM approach.

## Relevance to Odin

**Topics:**

4.A — Landscape of Existing Personal Finance Systems

4.B — Limitations and Gaps in Existing Systems

5.A — Financial Behavioral Profiles in Personal Finance

5.C — Financial Behavioral Profile Classification Algorithm

11.B — Retention Mechanisms and Engagement Design

**Contribution to Odin:**

This paper demonstrates that stochastic block modeling identifies consumer spending communities without requiring demographic or socio‑economic features, directly informing Odin’s financial behavioral profiling module. The finding that weighted SBM preserves average spending across communities while isolating category‑level emission drivers justifies using SBM over k‑means for Odin’s user classification, particularly when the goal is to test behavioural interventions across groups with identical spending patterns but different external characteristics. The paper’s emphasis on scalable, group‑level targeting (rather than individual nudges) supports Odin’s retention strategy: value‑driven engagement via community‑specific budget recommendations rather than gamification.

**Directly justifies:**

- “Stochastic block models detect consumer spending communities without demographic features, achieving near‑zero variance in category‑level transaction counts within clusters.”
- “Weighted SBM produces clusters where percentage spending per category falls within one median absolute deviation of the population median, enabling ceteris paribus analysis of external factors.”
- “Hierarchical SBM allows analysis at multiple granularity levels: lower levels capture fine‑grained habits, higher levels capture broad spending archetypes.”
- “Community detection on bipartite spending networks identifies which merchant categories drive emissions for each consumer group, enabling targeted behavioural interventions.”

**Limits of relevance:**

- Study population is UK‑based with higher environmental consciousness; Filipino young professionals may exhibit different spending patterns and carbon intensities.
- Carbon multipliers are UK‑specific (LCFS/UKMRIO); not directly transferable to Philippines without local input‑output data.
- Dataset excludes direct debits (utilities, rent) and cash transactions; Odin’s manual input model would capture these, but the SBM approach was not tested on such categories.
- SBM computational cost increases with dataset size; Odin’s mobile‑first constraints may require lighter community detection methods for real‑time profiling.

## Limitations

- Static network assumption: SBM does not account for temporal changes in spending behaviour; consumer profiles may drift over time. [unacknowledged]
- Computational expense: SBM inference is slower than k‑means, especially for million‑scale datasets; may limit real‑time profiling on mobile.
- Sample bias: customers are sustainability‑oriented and predominantly young; generalisability to average Filipino consumers is unknown.
- Missing high‑emission categories: utility payments (direct debit) and rent are underrepresented, potentially underestimating true emission footprints.
- No direct comparison to other clustering algorithms (k‑means, hierarchical) on the same dataset; the claimed advantages over distance‑based methods are referenced from literature, not empirically demonstrated.

## Remember This

- 🔑 **SBM clusters without demographics** — spending‑pattern communities emerge from network structure alone, not age or income.
- 📌 Weighted SBM holds spending constant — all clusters spend identically per category, enabling fair cross‑group comparisons.
- 💡 Emission drivers vary by cluster — one group’s top emitter is grocery, another’s is taxi; targeting must be community‑specific.
- ⚠️ No temporal dynamics — static SBM ignores behaviour drift; Odin may need periodic reclustering.
- 🔍 Synthetic validation passes — method scales to 3,000 customers, 1M transactions; clustering still works.
