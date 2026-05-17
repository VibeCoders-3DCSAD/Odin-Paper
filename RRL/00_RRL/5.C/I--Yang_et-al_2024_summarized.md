# ENHANCING FINANCIAL SERVICES THROUGH BIG DATA AND AI-DRIVEN CUSTOMER INSIGHTS AND RISK ANALYSIS

## Metadata

```yaml
---
paper_id: "10.60087/jklst.vol3.n3.p53-62"
designation: international
title: "ENHANCING FINANCIAL SERVICES THROUGH BIG DATA AND AI-DRIVEN CUSTOMER INSIGHTS AND RISK ANALYSIS"
authors: "Yang, T.; Xin, Q.; Zhan, X.; Zhuang, S.; Li, H."
year: 2024
venue: "Journal of Knowledge Learning and Science Technology"
odin_topics: ["4.A", "4.B", "5.A", "5.C", "6.A"]
shorthand_tags: ["/pfms-intelligent-features", "/pfms-limitations", "/profiling-role", "/classifier-candidates", "/forecasting-methods-survey"]
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

Supervised learning and XGBoost enable accurate customer profiling and profit‑based risk modeling in financial services, improving loan approval and risk management.

## Problem and Motivation

Traditional financial risk monitoring relies on expert experience and static statistical models, which perform poorly in fast‑changing markets and fail to capture complex risk‑profit relationships. Effective risk monitoring is essential for financial system stability, investor protection, and market efficiency. Prior work lacked integrated feature systems and profit‑based modeling at the account level that could handle non‑monotonic risk‑profit curves.

## Approach

- Dataset: 150,000 loans originated in 2012, tracked through December 2015, from multiple bank datasets.
- Built six feature systems: customer attributes, debit card transactions, credit card installments, loan applications, trend characteristics (past month consumption and borrowing ratio), and product page visit behavior.
- Used supervised learning as the basis for an AI pricing model to enable accurate customer identification and targeting.
- For profit modeling, applied XGBoost with grid search for tree depth and learning rate, 5‑fold cross‑validation, and early stopping by AUC; learning rate limited to 0.001–0.01 with thousands of trees.
- Face recognition via deep neural networks trained on tens of millions to billions of face images.
- Fraud detection using relationship graphs and community discovery algorithms (LOUVAIN, LPA, SLPA).

## Findings

1. The profit‑based model’s forecasting performance for revenue and total profit is poor, but **ranking performance is significantly better** than risk‑based models alone.
2. The hump‑shaped relationship between profit components and risk is preserved between predicted and actual curves.
3. Profit quartile spread across risk ranges increases with risk level, indicating greater prediction challenge in high‑risk areas.

- XGBoost hyperparameter tuning achieved optimal out‑of‑sample mean square error for regression and classification error for default probability.
- Face recognition features extracted by deep learning place same‑person photos close in feature space and different persons far apart.
- Community discovery algorithms effectively identify gang fraud by analyzing multi‑level associations (first to third degree) using common information like same WIFI or area.

## Key Figures and Tables

- Figure 2: Profit graph showing net credit losses vs. risk → Hump‑shaped curve and increasing profit spread at higher risk levels.
- Table 1: Hyperparameter search results for XGBoost submodels → Optimal tree depth and learning rate ranges for revenue, default probability, and loss rate models.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| XGBoost | Extreme Gradient Boosting — a scalable tree‑based ML algorithm that handles non‑linear relationships. |
| Supervised learning | ML that learns from labeled input‑output pairs to predict outcomes on new data. |
| Deep neural networks | Multiple‑layer neural networks that automatically learn hierarchical features from raw data. |
| Community discovery algorithms | Methods (LOUVAIN, LPA, SLPA) that find tightly connected groups (gangs) in graph data. |
| AUC | Area Under the ROC Curve — a measure of a classifier’s ability to separate positive from negative classes. |

## Critical Citations

- [Thomas, 2000] — Foundational work on automated credit scoring using external and internal account data.
- [Finlay, 2008; 2010] — Demonstrated that continuous financial behavior models outperform binary default models for profit prediction.
- [Fitzpatrick & Mues, 2021] — Extended profit prediction algorithms to P2P lending contexts.
- [Verbraken et al., 2014] — Showed profit‑based modeling enables optimal profit threshold calculation beyond default scores.

## Relevance to Odin

**Topics:**

4.A — Landscape of Existing Personal Finance Systems

4.B — Limitations and Gaps in Existing Systems

5.A — Financial Behavioral Profiles in Personal Finance

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

**Contribution to Odin:**

This paper directly supports Odin’s financial behavioral profiling module by demonstrating how supervised learning on six feature types (transactions, loans, online behavior) constructs accurate customer portraits. Although the context is bank lending, the feature engineering approach — especially trend characteristics and transaction frequency windows — is transferable to Odin’s expense categorization and forecasting modules. The paper’s use of XGBoost for profit‑based modeling, with explicit handling of non‑linear and non‑monotonic relationships, provides algorithmic justification for Odin’s spending forecasting and budget recommendation modules, where user profitability is not a goal but the methodology for ranking and prediction remains applicable.

**Directly justifies:**

- “Supervised learning using six feature systems (debit/credit transactions, loan applications, trend characteristics, and online behavior) achieves accurate customer portraits for targeting and risk management.”
- “XGBoost with grid search, cross‑validation, and early stopping by AUC provides superior ranking performance for profit prediction compared to risk‑only models, preserving the hump‑shaped profit‑risk relationship.”
- “Profit‑based modeling delivers more actionable information than risk‑based modeling in higher risk ranges, where profit variability increases.”
- “Community discovery algorithms (LOUVAIN, LPA, SLPA) applied to relationship graphs effectively identify fraud gangs using shared attributes like WIFI or geographic area.”

**Limits of relevance:**

- Geography and demographic: The study does not use Filipino data or focus on young professionals; findings on profit‑based modeling assume institutional lending, not personal budget management.
- Domain mismatch: Odin has no profit‑maximization objective; the ranking and prediction methodology is relevant, but the utility function differs.
- Data infrastructure: The paper assumes access to bank‑level transaction and loan databases, which Odin (manual input only) does not have; however, feature construction logic remains applicable to user‑entered data.
- Time period: Dataset from 2012–2015 may not reflect recent spending behaviors or fintech innovations.
- No evaluation of cold‑start user profiling or sparse transaction histories, which are central to Odin’s challenges.

## Limitations

- The paper lacks explicit validation of customer profiling accuracy on individual consumer segments (e.g., young professionals). [unacknowledged]
- No discussion of privacy or data protection implications of AI‑driven profiling, despite using sensitive financial and behavioral data. [unacknowledged]
- The profit‑based model’s poor forecasting performance limits its direct use for prediction tasks; only ranking is reliable.
- Reliance on historical bank data (2012–2015) may not generalize to post‑pandemic financial behaviors or mobile‑first fintech apps.
- The paper does not address how feature systems would adapt to manual transaction entry (vs. API‑fetched bank data). [unacknowledged]

## Remember This

- 🔑 **150,000 loans** — dataset scale proves ML methods work on real financial portfolios.
- 📌 XGBoost beats risk‑only models for ranking profitable customers, even when forecasting is weak.
- 💡 Six feature types (transactions, loans, trends, page visits) enable accurate customer portraits.
- ⚠️ Profit‑based modeling useful for ranking, not precise prediction — high‑risk range has wider profit spread.
