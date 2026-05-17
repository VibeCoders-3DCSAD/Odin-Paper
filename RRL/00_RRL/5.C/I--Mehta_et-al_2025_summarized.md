# Clustering and Similarity Learning in Financial Markets: A Tutorial for the Practitioners

## Metadata

```yaml
---
paper_id: "d4c2b1a0-5e6f-4a7b-8c9d-0e1f2a3b4c5d"
designation: algorithm-specific
title: "Clustering and Similarity Learning in Financial Markets: A Tutorial for the Practitioners"
authors: "Mehta, D.; Thompson, J. R. J.; Lee, H.; Lee, Y."
year: 2025
venue: "Unknown"
odin_topics: ["5.A", "5.C", "8.A", "12.A"]
shorthand_tags: ["/profiling-role", "/classification-vs-clustering", "/classifier-candidates", "/anomaly-taxonomy", "/eval-frameworks-survey"]
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

Clustering and similarity learning have evolved from static industry codes to adaptive, data‑driven frameworks integrating tabular, time‑series, text, and graph data for peer discovery across financial asset classes.

## Problem and Motivation

Traditional peer‑grouping methods (industry codes, style boxes, return correlations) are coarse and rigid, failing to capture adaptive risk and thematic exposures. Financial practitioners need similarity systems that align with actual trading, valuation, and compliance needs. Prior work lacked integrated multimodal pipelines and operational evaluation metrics such as substitution fidelity and neighborhood stability.

## Approach

- Data sources: Tabular fundamentals, time‑series returns, textual disclosures (filings, prospectuses), graph structures (ownership, supply chain), and images.
- Clustering methods: Partitioning (k‑means, k‑medoids), hierarchical, density‑based (DBSCAN), model‑based (Gaussian mixtures), time‑series (DTW, correlation), text (TF‑IDF, transformer embeddings), graph (community detection, node2vec, GNNs).
- Similarity learning: Metric learning (Mahalanobis, kernel), Random Forest proximities, Siamese networks, triplet loss, contrastive learning, multimodal fusion, open‑set recognition.
- Evaluation: Academic metrics (Silhouette, ARI, NMI, stability) vs. practitioner metrics (substitution fidelity, category reproducibility, segment utility, interpretability).

## Findings

- Adaptive, data‑driven similarity systems outperform static taxonomies (GICS, SIC) by capturing actual risk, liquidity, and thematic exposures.
- Evaluation must shift from abstract indices to operational validity: substitution fidelity for bonds, category reproducibility for funds, and segment utility for investors.
- Multimodal fusion (tabular + time‑series + text + graphs) is essential for robust peer discovery, especially in sparse or illiquid markets.
- Supervised similarity (Random Forest proximities, metric learning) aligns distance functions with task‑specific labels (e.g., fund categories, client segments).
- Open‑set similarity flags outliers (e.g., novel fund styles, market anomalies) beyond learned clusters.
- Investor clustering on transaction data reveals misalignments between elicited risk profiles and actual behavior, improving KYC and personalization.

## Key Figures and Tables

- Exhibit 2: Common distance metrics by data type → Euclidean for numeric, Gower for mixed, DTW for time series.
- Exhibit 3: Clustering methods across modalities → k‑means for tabular, community detection for graphs.
- Exhibit 5: Evaluation metrics academic vs. practitioner → substitution fidelity for bonds, segment utility for investors.
- Exhibit 7: Fund clustering applications → return‑based style analysis, holding‑based overlap detection.
- Exhibit 10: Investor clustering → K‑means on demographics, DTW on transaction sequences.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| GICS | Global Industry Classification Standard – a static sector taxonomy. |
| SIC | Standard Industrial Classification – coarse industry code system. |
| DTW | Dynamic Time Warping – aligns time series that are shifted or stretched in time. |
| GNN | Graph Neural Network – learns embeddings from relational data (e.g., issuer–bond links). |
| KYC | Know Your Client – regulatory requirement to understand investor risk and suitability. |
| ARI | Adjusted Rand Index – measures agreement between two clusterings (external validation). |
| NMI | Normalized Mutual Information – information‑theoretic cluster agreement metric. |

## Critical Citations

- [Breiman, 2001] — Random Forest proximities enable supervised similarity learning from mixed‑type financial data.
- [Kulis, 2013] — Foundational survey of metric learning techniques adapted for bond substitution and fund classification.
- [Jeyapaulraj et al., 2022] — Validates Random Forest proximities for corporate bond peer discovery under desk constraints.
- [Desai & Mehta, 2021] — Demonstrates that clustering outcomes depend heavily on feature and metric choice, not just label quality.

## Relevance to Odin

**Topics:**

5.A — Financial Behavioral Profiles in Personal Finance

5.C — Financial Behavioral Profile Classification Algorithm

8.A — Anomaly Detection in Personal Finance Systems

12.A — Evaluation Frameworks for Personal Finance Systems

**Contribution to Odin:**

This paper directly informs Odin’s behavioral profiling and classification module by surveying clustering methods (k‑means, hierarchical, kernel metric learning) that can group users by transaction patterns, risk tolerance, and financial behavior. The discussion of supervised similarity (Random Forest proximities, contrastive learning) provides algorithmic justifications for cold‑start profiling and progressive reclassification as user data accumulates. Although the paper targets institutional investment, its emphasis on operational evaluation metrics (stability, segment utility) and open‑set outlier detection directly supports Odin’s anomaly detection and ISO 25010 evaluation requirements.

**Directly justifies:**

- “Clustering investors on transaction data reveals misalignments between self‑assessed risk profiles and actual trading behavior, supporting dynamic reclassification.”
- “Random Forest proximities produce interpretable, task‑specific similarity without requiring labeled ground truth, applicable to cold‑start user profiling.”
- “Open‑set similarity frameworks flag observations that fall outside all learned clusters — directly applicable to detecting anomalous spending patterns or new behavioral profiles.”
- “Evaluation of clustering must prioritize substitution fidelity and segment utility over abstract indices — a principle transferable to Odin’s module‑level performance metrics.”

**Limits of relevance:**

- Domain is institutional investment management, not personal budget management; transaction data volumes and risk objectives differ.
- Methods assume access to rich time‑series and textual data (e.g., prospectuses, filings) that Odin may not collect.
- No validation on Filipino young professionals or manual entry financial data.
- Some advanced methods (graph neural networks, multimodal transformers) exceed Odin’s computational scope for a mobile‑first system.

## Limitations

- Hyperparameter sensitivity: clustering outcomes vary with distance metric and preprocessing — acknowledged but not fully mitigated.
- Interpretability: deep similarity models (Siamese, GNNs) operate as black boxes, complicating fiduciary compliance.
- No universal ground truth for similarity — results depend on task and regime, making cross‑study comparison difficult. [unacknowledged]
- Most case studies use U.S. or European data; applicability to Philippine financial behavior and spending patterns is untested.
- Computational cost of multimodal fusion may exceed mobile‑first deployment constraints. [unacknowledged]

## Remember This

- 🔑 Clustering shifts from static labels to **adaptive, data‑driven similarity** — essential for dynamic user profiling.
- 📌 **Multimodal fusion** (tabular + time‑series + text) beats single‑source methods for peer discovery.
- 💡 Open‑set similarity flags outliers — directly applicable to Odin’s anomalous spending detection.
- ⚠️ No universal similarity metric — choice must match task (e.g., DTW for time‑series, Gower for mixed tabular).
- ✅ Evaluate by **operational utility** (substitution fidelity, segment stability), not just academic indices.
