```yaml
paper_id: 10.1145/3626520
designation: international
title: Rare Category Analysis for Complex Data: A Review
authors: Zhou, D.; He, J.
year: 2023
venue: ACM Computing Surveys
odin_topics:
  - 8.A
  - 8.B
  - 12.A
  - 12.B
shorthand_tags:
  - /anomaly-detection
  - /rare-category
  - /imbalanced-learning
  - /survey
tldr: Reviews state-of-the-art techniques for rare category analysis in complex data, covering exploration, exploitation, representation, and interpretation under challenges of rarity, label scarcity, non-separability, heterogeneity, and dynamics.
problem_and_motivation: Rare categories are often most important in high-impact domains like fraud detection and disease diagnosis, but traditional anomaly detection yields many uninteresting anomalies. Existing methods fail to identify rare categories that are compact and statistically significant. A systematic review of techniques addressing rarity, non-separability, heterogeneity, and dynamics is missing.
approach:
  - Surveys over 100 papers on rare category analysis from data mining and machine learning.
  - Organizes techniques into four tasks: exploration (unsupervised), exploitation (semi-supervised), representation learning, and interpretation.
  - Covers static and dynamic data, including tabular, time-series, and graph-structured data.
  - Discusses homogeneous and heterogeneous settings with data and task heterogeneity.
  - Provides evaluation using public benchmark datasets like UNSW-NB15, HDFS, and Tox21.
  - Summarizes representative algorithms in a table with data type and task.
findings:
  - "num: Only 0.1% of Sloan sky survey images are anomalies; 99% of those anomalies are uninteresting, leaving 0.001% as useful rare categories."
  - "num: To detect a rare category with proportion 0.01%, random sampling requires approximately 10,000 labeling requests."
  - "num: NNDM algorithm guarantees identification of at least one example from each minority class with probability 1-δ after O(2α/r^2) iterations."
  - Rare categories are compact in feature space and non-separable from majority classes, requiring specialized detection algorithms.
  - Graph-based methods like GRADE compute a global similarity matrix to capture sharp local density changes near rare category boundaries.
key_figures_tables:
  - "Figure 1: Sloan sky images showing known objects (top) vs anomalies (bottom) → Most anomalies are uninteresting diffraction spikes; few lead to discoveries."
  - "Figure 2: Venn diagram relationship between anomalies and rare category examples → Rare categories are a subset of anomalies that are compact and interesting."
  - "Table 2: Publicly accessible real-world datasets for rare category analysis → Lists tabular, time-series, and graph datasets with rare category descriptions."
  - "Table 3: Representative algorithms by data type and task → Majority of methods are unsupervised or semi-supervised; visualization/interpretation is underexplored."
key_equations:
  - equation: "Hyberball(x_i, r) = {x | x in D, ||x - x_i|| <= r}"
    explanation: "Hyper-ball centered at x_i with radius r for local density estimation."
  - equation: "S = (I - α D^{-1/2} A D^{-1/2})^{-1}"
    explanation: "Global similarity matrix for graph-based rare category detection."
  - equation: "P(y = rarecategory | x) >= C * ∏_{v=1}^V P(y = rarecategory | x^v)"
    explanation: "Lower bound for multi-view rare category posterior probability."
definitions:
  - term: "Rare category analysis"
    definition: "Problem of detecting, characterizing, representing, and interpreting rare examples from underrepresented minority classes in a highly imbalanced dataset."
  - term: "Smoothness assumption (majority class)"
    definition: "Distribution of each majority class's support region is sufficiently smooth."
  - term: "Compactness assumption (minority class)"
    definition: "Minority class examples can be represented as a compact cluster in feature space."
critical_citations:
  - "[Hawkins, 1980] — Defined outliers as observations from a different mechanism."
  - "[He & Carbonell, 2008] — Proposed NNDM nearest-neighbor rare category detection."
  - "[Pelleg & Moore, 2005] — First active learning framework for rare category exploration."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      justification: "Reviews anomaly detection techniques for rare patterns like fraud."
    - code: 8.B
      name: Anomaly Detection Algorithm
      justification: "Surveys algorithms including NNDM, GRADE, MUVIR, and GNN-based methods."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      justification: "Provides benchmark datasets and evaluation protocols for rare category tasks."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: "Compares representative methods across data types and tasks in a summary table."
  contribution: "Odin's anomaly detection module (8.B) can directly apply reviewed algorithms such as NNDM and GRADE to identify rare fraudulent transactions. The spending forecasting module (6.A) may incorporate rare category exploration to detect emerging spending patterns that deviate from historical norms. Odin's evaluation framework (12.A) can adopt the public benchmark datasets (e.g., Fraud, UNSW-NB15) and the comparative methodology from Table 3. The survey's discussion of data heterogeneity (C4) and dynamics (C5) informs Odin's design for multi-source financial data and evolving user behavior."
  directly_justifies:
    - "Rare categories are compact in feature space and non-separable from majority classes."
    - "num: To detect a rare category comprising 0.01% of data, random sampling requires approximately 10,000 labels."
    - "Graph-based rare category detection using similarity matrix S outperforms random sampling."
    - "Multi-view integration via product of view-specific posteriors improves rare category detection."
  limits:
    - "Survey does not provide empirical meta-analysis or direct performance comparisons across algorithms."
    - "Focus is on general rare category analysis, not specifically on personal finance or PFMS constraints."
    - "Real-time or mobile-specific considerations (e.g., latency, battery) are not addressed."
  mapping_rationale: "The paper was screened against Odin's functional domains. Anomaly detection (domain 8) is a direct match because rare category analysis addresses fraud, intrusion, and outlier detection in high-impact settings. System evaluation (domain 12) applies because the survey extensively reviews evaluation datasets, metrics, and representative baselines. Topics 5 (behavioral profiling) and 6 (spending forecasting) were rejected because the paper does not address financial behavior profiles or forecasting specifically. Topic 13 (savings/debt) was irrelevant. Borderline cases like representation learning (Section 4.1) could inform profiling but lack explicit financial context, so they were excluded. The selected codes 8.A, 8.B, 12.A, 12.B capture the most directly transferable contributions."
limitations:
  - "The survey does not address computational efficiency constraints of mobile PFMS. [unacknowledged]"
  - "User privacy and data security concerns in rare category detection are not discussed. [unacknowledged]"
  - "Real-time detection requirements for streaming financial transactions are not explicitly evaluated. [unacknowledged]"
  - "The reviewed methods assume labeled data from oracles, which may not be feasible for personal finance users."
remember_this:
  - "Rare categories are a subset of anomalies that are both statistically significant and compact."
  - "num: 99% of anomalies are uninteresting noise; only 1% are useful rare categories."
  - "Labeling rare categories is expensive due to extreme class imbalance as low as 0.01%."
  - "Graph neural networks can effectively detect rare patterns in temporal graphs."
  - "Multi-view integration improves rare category detection from heterogeneous data sources."
```