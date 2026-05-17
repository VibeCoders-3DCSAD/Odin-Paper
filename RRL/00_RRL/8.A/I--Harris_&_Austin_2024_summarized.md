# Comparative Study of Supervised and Unsupervised Machine Learning Approaches in Banking Applications

## Metadata

```yaml
---
paper_id: "6ba7b810-9dad-11d1-80b4-00c04fd430c8"
designation: international
title: "Comparative Study of Supervised and Unsupervised Machine Learning Approaches in Banking Applications"
authors: "Harris, F.; Austin, V."
year: 0000
venue: "Unknown"
odin_topics: ["5.C", "6.A", "8.A", "8.B"]
shorthand_tags: ["/classification-vs-clustering", "/classifier-candidates", "/classifier-tradeoffs", "/forecasting-methods-survey", "/anomaly-ml-families", "/anomaly-algo-candidates"]
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

Supervised learning excels at prediction with labeled data (credit scoring, fraud detection), while unsupervised learning discovers hidden patterns without labels (customer segmentation, anomaly detection).

## Problem and Motivation

Banking institutions lack clear guidance on when to apply supervised versus unsupervised machine learning for specific operational tasks. Selecting the wrong approach wastes labeled data or fails to capture hidden patterns, undermining decision quality. No prior work provided a systematic comparative framework mapping each method's strengths to banking use cases.

## Approach

- Source: Literature review of existing ML applications in banking (no primary dataset).
- Supervised methods covered: linear/logistic regression, decision trees, SVM, neural networks.
- Unsupervised methods covered: k-means/hierarchical clustering, PCA, isolation forests, autoencoders.
- Comparison dimensions: data requirements, predictive accuracy, interpretability, implementation complexity.
- Hybrid models discussed: unsupervised pre-processing followed by supervised prediction.

## Findings

- Supervised learning requires labeled historical data but achieves high accuracy for tasks like credit scoring and fraud detection.
- Unsupervised learning operates on unlabeled data, making it suitable for exploratory analysis and anomaly detection.
- Interpretability is higher in supervised models (e.g., decision trees) than in unsupervised clustering outputs.
- **No single approach dominates; choice depends on labeled data availability and whether the goal is prediction or pattern discovery.**
- Hybrid models (unsupervised clustering then supervised classification) improve fraud detection and customer insights.

## Key Figures and Tables

None.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Supervised learning | Training on input-output pairs to predict labels for new data. |
| Unsupervised learning | Finding patterns or groups in data without predefined labels. |
| Classification | Predicting a discrete category (e.g., fraud/legitimate). |
| Clustering | Grouping similar data points together (e.g., customer segments). |
| Dimensionality reduction | Reducing number of features while preserving key information (e.g., PCA). |
| Hybrid model | Combining unsupervised pre-processing with supervised prediction. |

## Critical Citations

- [Arora & Kaur, 2019] — Direct comparison of supervised vs unsupervised for credit card fraud detection.
- [Carcillo et al., 2019] — Demonstrates combining unsupervised and supervised learning improves fraud detection.
- [Lessmann et al., 2015] — Benchmark of classification algorithms for credit scoring.
- [Liu & Wu, 2020] — Comparison of supervised and unsupervised methods for transaction anomaly detection.

## Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

**Contribution to Odin:**

This paper provides a high-level framework for choosing between supervised and unsupervised learning that directly informs Odin's module design decisions. For Odin's spending forecasting module, the paper justifies using supervised regression (e.g., on historical transaction sequences) because labeled past spending data is available. For Odin's anomalous spending detection, the paper supports unsupervised methods (e.g., clustering or isolation forests) to flag deviations without requiring labeled fraud data — critical for cold-start users. The discussion of hybrid approaches also suggests a pipeline where unsupervised clustering first segments users by spending behavior, then supervised models predict per-segment budgets or anomalies.

**Directly justifies:**

- "Supervised learning achieves high predictive accuracy for financial tasks such as credit scoring and fraud detection when sufficient labeled historical data is available."
- "Unsupervised learning detects anomalies without labeled training data, making it applicable to cold-start user profiles where no prior fraud examples exist."
- "Clustering algorithms (k-means, hierarchical) can identify distinct customer spending segments, enabling personalized budget recommendations."
- "Hybrid models combining unsupervised pre-processing with supervised classification improve detection of emerging fraud patterns not present in training labels."

**Limits of relevance:**

- Domain is banking (credit, fraud) not personal budget management — transaction types and user goals differ.
- No empirical performance numbers (accuracy, precision, recall) are reported; claims are qualitative.
- Paper does not address mobile-specific constraints (offline, compute, latency) relevant to Odin.
- Not grounded in Philippine financial behavior or demographic data.

## Limitations

- Literature review lacks systematic search criteria or meta-analysis; conclusions are narrative.
- No quantitative comparison (e.g., accuracy benchmarks) across algorithms — limits ability to justify specific model choices.
- Ignores cold-start scenarios where neither labeled data nor stable patterns exist. [unacknowledged]
- Does not address time-series or sequential dependencies in spending data, critical for forecasting.
- All examples are from banking; applicability to voluntary personal finance tracking (no mandatory compliance) is assumed but untested.

## Remember This

- 📌 Supervised = needs labels → use for forecasting from past spending.
- 🔍 Unsupervised = finds patterns without labels → use for cold-start anomaly detection.
- 🔄 Hybrid models (cluster then classify) boost fraud detection — adaptable to Odin's user segmentation.
- 💡 No single algorithm wins; choice depends on labeled data availability and prediction vs. discovery goal.
- ⚠️ Paper offers no numbers — use as conceptual guide, not performance benchmark.
