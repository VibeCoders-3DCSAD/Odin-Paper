```yaml
paper_id: "10.1038/s41598-025-14364-7"
designation: "international"
title: "Analysing community-level spending behaviour contributing to high carbon emissions using stochastic block models"
authors: "Simeonov, O.; Restocchi, V.; Goddard, B. D."
year: 2025
venue: "Scientific Reports"
odin_topics:
  - "5.A"
  - "5.C"
shorthand_tags:
  - "/behavioral-profiles"
  - "/classification-algorithm"
tldr: "Stochastic block models on bipartite customer-merchant networks identify consumer groups with similar spending and carbon emission patterns, enabling targeted sustainability interventions."
problem_and_motivation: "Reducing carbon emissions requires understanding consumer spending behavior at scale. Financial transaction data can estimate emissions, but grouping consumers with similar spending patterns remains challenging for designing effective interventions. Existing clustering methods often rely on demographic data or focus on single categories."
approach:
  - "Used debit card transaction data from 1,362 UK customers from a sustainable banking FinTech (ekko), filtering to 272 customers with ≥30 transactions across ≥10 MCC categories."
  - "Constructed bipartite network with customers and merchant categories as nodes, weighted by transaction counts or normalized spending amounts."
  - "Applied degree-corrected nonparametric hierarchical stochastic block model (SBM) for community detection, running 100 iterations to stabilize entropy."
  - "Estimated carbon emissions per transaction using carbon multipliers from Trendl et al. (2023) based on LCFS and UKMRIO data."
  - "Validated scalability on synthetic dataset of 1 million transactions and 3,000 customers."
findings:
  - "num: Weighted SBM produced communities where spending percentages across categories fell within one median absolute deviation of the population median for 71 of 80 clusters."
  - "num: Unweighted SBM identified clusters with distinct emission profiles; e.g., clusters 17 and 18 had high emissions from taxicabs, while clusters 3,11,12 from service stations."
  - "num: Logistic regression using age and deprivation index predicted customer retention with AUC 0.744; younger and more deprived customers had higher dropout probability."
  - "num: Median carbon emission rate was 685 grams per GBP spent, slightly lower than previous studies."
  - "SBM approach scales to larger datasets, completing analysis of millions of transactions in minutes."
key_figures_tables:
  - "Figure 4: Heatmap of percent carbon emissions per MCC across clusters → Grocery dominates most clusters, but transport varies."
  - "Figure 5: Heatmap of weighted SBM spending percentages → Cluster spending matches population median within 1 MAD."
  - "Figure 7: Emissions vs transaction count/spending for taxicabs → Cluster 17 high transaction count, cluster 18 high spending per transaction."
  - "Figure 9: Logistic regression retention probability → Younger, deprived customers more likely to drop out."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "SBM"
    definition: "Stochastic Block Model, a probabilistic model for community detection in networks."
  - term: "MCC"
    definition: "Merchant Category Code, a four-digit code classifying merchant type."
  - term: "MAD"
    definition: "Median Absolute Deviation, a robust measure of statistical dispersion."
  - term: "IMD"
    definition: "Index of Multiple Deprivation, UK measure of area-level deprivation."
  - term: "LCFS"
    definition: "Living Cost and Food Survey, UK household expenditure survey."
  - term: "UKMRIO"
    definition: "UK Multi-Region Input-Output dataset for economic and environmental flows."
critical_citations:
  - "[Trendl et al., 2023] — Provides carbon multipliers for transaction data."
  - "[Peixoto, 2014] — Hierarchical SBM methodology used."
  - "[Wells et al., 2025] — Comparable UK household carbon segmentation using k-means."
relevance:
  topics:
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      justification: "Identifies consumer communities with distinct spending and emission patterns."
    - code: "5.C"
      name: "Financial Behavioral Profile Classification Algorithm"
      justification: "Uses stochastic block modeling as algorithm to classify spending behavior."
  contribution: "Odin can use the SBM approach to cluster users into behavioral profiles based solely on transaction patterns without requiring demographic data, addressing cold-start profile assignment. The weighted SBM variant that normalizes spending by category averages enables Odin to compare spending behaviors across different user groups while controlling for category-level spending differences. The paper's demonstration of carbon emission profiling per cluster directly supports Odin's anomaly detection for high-emission spending categories and targeted nudges for sustainable behavior."
  directly_justifies:
    - "Financial transaction data can reliably estimate carbon emissions at individual level."
    - "Stochastic block models effectively cluster consumers by spending patterns without demographic features."
    - "Consumer clusters exhibit distinct carbon emission profiles driven by specific merchant categories."
    - "Weighted SBM produces communities with comparable spending proportions across categories."
  limits:
    - "Dataset biased toward environmentally conscious UK customers, not generalizable to Filipino young professionals."
    - "Transaction data missing utility and subscription payments made via direct debit."
    - "SBM is static and computationally expensive for very large datasets."
    - "Carbon multipliers assume uniform intensity within merchant categories."
  mapping_rationale: "The paper primarily addresses behavioral profiling (5.A) and classification algorithms (5.C) as it applies stochastic block modeling to identify consumer spending communities. While expense categorization (3.A) is implicit through MCC usage, the paper does not propose new categorization frameworks or design considerations. It does not address budgeting, anomaly detection, forecasting, or savings/debt management. The socio-economic analysis of retention touches on engagement but is not central. Therefore only 5.A and 5.C were selected."
limitations:
  - "Dataset represents sustainability-oriented subsample, limiting generalizability. [unacknowledged]"
  - "Utility and subscription payments are underrepresented due to direct debit exclusion. [acknowledged]"
  - "SBM static nature does not capture temporal changes in spending behavior. [acknowledged]"
  - "Computational expense for very large datasets may limit real-time applications. [unacknowledged]"
  - "Carbon intensity assumed constant per MCC, masking product-level variation. [acknowledged]"
remember_this:
  - "Weighted SBM aligns cluster spending with population medians within one MAD."
  - "Median carbon emission rate is 685 grams per GBP spent."
  - "Younger and deprived customers have higher dropout probability in paid sustainable banking."
  - "Unweighted SBM identifies clusters with dominant emission sources like taxicabs or fuel."
```