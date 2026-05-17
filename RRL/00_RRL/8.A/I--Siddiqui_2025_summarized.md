# OPTIMIZING BUSINESS DECISION-MAKING THROUGH AI-ENHANCED BUSINESS INTELLIGENCE SYSTEMS: A SYSTEMATIC REVIEW OF DATA-DRIVEN INSIGHTS IN FINANCIAL AND STRATEGIC PLANNING

## Metadata

```yaml
---
paper_id: "10.71292/sdmi.v2i01.21"
designation: international
title: "OPTIMIZING BUSINESS DECISION-MAKING THROUGH AI-ENHANCED BUSINESS INTELLIGENCE SYSTEMS: A SYSTEMATIC REVIEW OF DATA-DRIVEN INSIGHTS IN FINANCIAL AND STRATEGIC PLANNING"
authors: "Siddiqui, N. A."
year: 2025
venue: "STRATEGIC DATA MANAGEMENT AND INNOVATION"
odin_topics: ["4.A", "4.B", "5.C", "6.A", "8.A"]
shorthand_tags: ["/pfms-intelligent-features", "/pfms-limitations", "/classifier-candidates", "/forecasting-methods-survey", "/anomaly-ml-families"]
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

AI-enhanced BI systems improve financial forecasting accuracy by **32–45%** and reduce fraudulent transactions by 47%, significantly boosting data-driven decision-making.

## Problem and Motivation

Traditional BI tools rely on static reports and structured data, failing to process real-time or unstructured information for predictive insights. This limits organizations’ ability to make agile, forward-looking financial and strategic decisions. Prior work lacked a comprehensive synthesis of AI-driven BI’s measurable impact across forecasting, fraud detection, and customer analytics.

## Approach

- Systematic review following PRISMA guidelines, analyzing 98 high-quality peer-reviewed articles from an initial pool of 2,450.
- Databases: Scopus, Web of Science, IEEE Xplore, ScienceDirect, Google Scholar (2012–2024).
- Inclusion: studies on AI-powered BI, ML, predictive analytics, or decision-making with empirical or theoretical contributions.
- Exclusion: traditional BI without AI, opinion pieces, non-English, or lacking methodology.
- Thematic analysis across financial forecasting, fraud detection, customer segmentation, and supply chain optimization.

## Findings

1. AI-powered BI improves **financial forecasting accuracy by 32–45%** and reduces unexpected financial losses by 28%.
2. Fraud detection systems cut fraudulent transactions by **47%** and reduce false positives by up to 60%, detecting fraud 40% faster than rule-based systems.
3. Customer engagement rises 38% and conversion rates 22% with AI-driven personalized marketing.
4. Supply chain efficiency increases 23%, logistics costs drop 17%, inventory turnover improves 20%.

- 62% of organizations face data integration challenges; 41% cite lack of AI explainability; 36% report algorithmic bias.

## Key Figures and Tables

- Figure 2: Benefits of AI-based decision making in finance → forecasting, fraud detection, risk assessment all show >25% improvement.
- Figure 8: Stacked area chart of AI-driven BI findings → forecasting accuracy and fraud reduction are the largest gains.
- Table 1: Identified research gaps → missing long-term impact studies and cross-industry AI-BI frameworks.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| BI | Business Intelligence — systems that analyze data to support business decisions. |
| AI | Artificial Intelligence — machines performing tasks that normally require human intelligence. |
| ML | Machine Learning — algorithms that learn patterns from data without explicit programming. |
| NLP | Natural Language Processing — AI that understands and generates human language. |
| PRISMA | Preferred Reporting Items for Systematic Reviews and Meta-Analyses — a guideline for transparent literature reviews. |
| LSTM | Long Short-Term Memory — a type of neural network good at remembering sequences [think: memory cell with forget gate]. |

## Critical Citations

- [Duan et al., 2019] — Establishes AI’s evolution from descriptive to predictive/prescriptive analytics in BI.
- [Sarker, 2022] — Provides foundational taxonomy of AI-based modeling techniques for decision support.
- [Dwivedi et al., 2021] — Outlines multidisciplinary challenges and opportunities for AI in information management.

## Relevance to Odin

**Topics:**

4.A — Landscape of Existing Personal Finance Systems

4.B — Limitations and Gaps in Existing Systems

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

8.A — Anomaly Detection in Personal Finance Systems

**Contribution to Odin:**

This systematic review provides benchmark performance ranges (32–45% forecasting improvement, 47% fraud reduction) that Odin can cite when justifying the expected value of its spending forecasting and anomalous spending detection modules. The review’s identification of data integration challenges (62% of organizations) and AI explainability concerns (41%) directly informs Odin’s design emphasis on privacy-by-design and transparent ML for user trust. Though focused on enterprise BI, the ML families surveyed (LSTM, random forests, isolation forest analogues) are directly transferable to Odin’s personal finance algorithms, and the finding that classification (customer segmentation) improves marketing engagement supports Odin’s behavioral profiling as a retention driver.

**Directly justifies:**

- “AI-powered predictive analytics improve financial forecasting accuracy by 32–45% in real-world business settings, providing a benchmark for personal finance spending forecasts.”
- “Machine learning fraud detection systems reduce false positives by up to 60% and detect anomalies 40% faster than rule-based systems, supporting unsupervised anomaly detection for Odin.”
- “Customer segmentation using clustering algorithms and behavioral analytics increases engagement by 38%, validating Odin’s profiling module as a retention mechanism.”
- “Data integration inconsistencies affect 62% of AI-driven BI adopters, reinforcing Odin’s need for clean, manually entered transaction data as a design constraint.”

**Limits of relevance:**

- Enterprise financial data context (corporate transactions, supply chains) differs from individual consumer spending patterns.
- No user-level behavioral data or cold-start evaluation — findings assume rich historical datasets, not sparse personal finance logs.
- Geographic and cultural specificity absent; findings from global studies may not directly map to Filipino young professionals.
- Focus on business decision-making rather than personal budgeting; forecasting targets revenue/risk, not per-category spending adherence.

## Limitations

- The review synthesizes existing literature but does not perform primary experiments; effect sizes are aggregated from diverse studies with varying methodologies.
- No validation of reported improvements (32–45% forecasting, 47% fraud reduction) in a personal finance or Philippine context. [unacknowledged]
- Data governance and bias challenges are discussed but no solutions are empirically tested.
- Excludes non-English and gray literature, potentially missing region-specific insights for Southeast Asia.
- The paper does not address mobile-first constraints (e.g., on-device processing, limited bandwidth) relevant to Odin’s deployment. [unacknowledged]

## Remember This

- 🔑 **+32–45% forecast accuracy** — AI-driven BI reliably improves predictions, applicable to spending forecasting.
- 💡 47% less fraud and 60% fewer false positives — unsupervised anomaly detection works without labeled data.
- 📌 38% higher engagement from AI segmentation — behavioral profiling drives retention, not gamification.
- ⚠️ 62% face data integration issues — clean manual input (Odin’s design) avoids this enterprise headache.
