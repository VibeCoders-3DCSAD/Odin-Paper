# Data-Driven Decision Making in Scholarship Programs: Leveraging Decision Trees and Clustering Algorithms

## Metadata

```yaml
---
paper_id: "f8c3e1a2-7b5d-4a1e-9c2f-3d4e5f6a7b8c"
designation: algorithm-specific
title: "Data-Driven Decision Making in Scholarship Programs: Leveraging Decision Trees and Clustering Algorithms"
authors: "Espiritu, F. V.; Natividad, M. C. B.; Velasco, R. A."
year: 2024
venue: "INTERNATIONAL JOURNAL IN INFORMATION TECHNOLOGY IN GOVERNANCE, EDUCATION AND BUSINESS"
odin_topics: ["5.C", "10.A", "12.B"]
shorthand_tags: ["/classifier-candidates", "/classifier-eval-metrics", "/ph-privacy-law", "/privacy-by-design", "/eval-ml-design"]
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

Decision trees (C4.5) and K-means clustering improved scholarship application success rates by 31% and achieved 80% predictive accuracy in a Philippine government program.

## Problem and Motivation

The BRO-Ed Scholarship program in Isabela province faced a 541% surge in applications (from 5,368 to 34,426 per cycle), overwhelming its manual review process. This subjective, time-consuming approach increased the risk of missing qualified applicants and slowed program operations. No systematic, data-driven method existed to evaluate scholarship applications at scale for underprivileged students in this context.

## Approach

- Dataset: 58,892 historical scholarship application records from the BRO-Ed program, reduced to 57,342 unique entries after duplicate removal.
- Preprocessing: Missing value handling (5% missing), outlier detection, standardization, normalization, and categorical encoding.
- Decision tree algorithm: C4.5 for classification, selecting split attributes by highest information gain ratio.
- Clustering algorithm: K-means to group similar applications and identify common characteristics among successful applicants.
- Online platform: Handlebars.js (frontend), Node.js/Express.js (backend), MySQL (database), W3.CSS (responsive UI).
- Evaluation metrics: Accuracy, precision, recall, F1-score computed from TP/TN/FP/FN counts.

## Findings

1. Predictive accuracy for successful scholarship outcomes reached **80%** , while failure prediction accuracy was 70%.
2. Online registration system improved success rates by **31%** compared to traditional manual methods.
3. Duplicate removal eliminated 3,100 duplicate entries, improving dataset quality and integrity.
4. High-impact success factors: parental occupation (small farmer), academic performance (GPA), and financial need.
5. User satisfaction surveys showed high preference for the online system due to ease of use and accessibility.

## Key Figures and Tables

- Table 1: Duplicate removal → 3,100 duplicates eliminated, unique entries rose from 55,792 to 57,342.
- Table 3: Technological framework → Handlebars.js + Node.js + Express.js + MySQL + W3.CSS.
- Figure 4: Impact of online registration → 31% higher success rate than traditional methods.
- Figure 5: Predictive accuracy → 80% for success prediction, 70% for failure prediction.
- Figure 7: F1-scores across categories → balanced performance across all classification categories.

## Key Equations

$$Accuracy = (TP + TN) / (TP + TN + FP + FN)$$
*Overall correct predictions divided by total predictions.*

$$Precision = TP / (TP + FP)$$
*Of all predicted positives, how many were actually positive.*

$$Recall = TP / (TP + FN)$$
*Of all actual positives, how many were correctly identified.*

$$F1\text{-}score = 2 \times (Precision \times Recall) / (Precision + Recall)$$
*Harmonic mean balancing precision and recall.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| C4.5 | Decision tree algorithm that splits data using information gain ratio (like a flow chart that asks the most useful question first). |
| K-means | Clustering algorithm that groups data points into K clusters based on similarity (like sorting applicants into piles by shared traits). |
| PII | Personally Identifiable Information — data that can identify a specific person. |
| RA 10173 | Philippine Data Privacy Act of 2012 — the national law governing personal data protection. |
| TP/TN/FP/FN | True Positive, True Negative, False Positive, False Negative — counts used to evaluate classifier performance. |
| Information gain ratio | Metric that measures how much a feature reduces uncertainty about the target variable. |

## Critical Citations

- [Yağcı, 2022] — Foundation for using ML algorithms to predict student outcomes in educational contexts.
- [Alyahyan & Düştegör, 2020] — Systematic review of predictive success factors, informing feature selection.
- [Sugiyarti et al., 2018] — Direct precedent for integrating data mining into scholarship grantee selection.
- [Delima, 2019] — Prior Philippine study on predicting scholarship grants using data mining techniques.

## Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

10.A — Data Privacy and Security in Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper demonstrates the implementation of decision tree (C4.5) and K-means clustering algorithms for classification and pattern recognition in a Philippine government context — directly applicable to Odin's financial behavioral profiling module. Its use of accuracy, precision, recall, and F1-score provides a ready‑to‑cite evaluation framework for Odin's classifier selection and benchmarking. Most importantly, the paper's explicit adherence to the Philippine Data Privacy Act (RA 10173), including data anonymization, informed consent, and security measures, offers a practical precedent for Odin's privacy‑by‑design requirements under local law.

**Directly justifies:**

- "C4.5 decision trees achieved 80% predictive accuracy on a binary classification task using mixed categorical and numerical data in a Philippine government program."
- "K-means clustering revealed underlying applicant groups and common success characteristics, supporting unsupervised pattern discovery in classification pipelines."
- "Compliance with RA 10173 (Data Privacy Act of 2012) was operationalized through data anonymization, access controls, encryption, and transparent communication with stakeholders."
- "Accuracy, precision, recall, and F1‑score were jointly reported as evaluation metrics for a classification algorithm in a resource‑constrained Philippine setting."

**Limits of relevance:**

- Domain is scholarship applicant selection, not personal financial behavior or spending patterns — classification features differ substantially.
- No comparison of decision trees against other classifiers (e.g., logistic regression, random forest, LSTM) — limits algorithm justification strength.
- Dataset is administrative scholarship records, not user transaction histories — cold‑start and concept drift dynamics are unaddressed.
- The online system is web‑based, not mobile‑first; mobile‑specific constraints (offline sync, low bandwidth) are not considered.

## Limitations

- Generalizability to personal finance domains is untested — scholarship applicant features (GPA, parental occupation) do not map to spending behavior.
- No cross‑validation or train/test split reported — reported 80% accuracy may be optimistic. [unacknowledged]
- The study does not compare C4.5 or K‑means against alternative algorithms (e.g., random forest, hierarchical clustering) to justify selection.
- Ethical discussion of data anonymization does not address re‑identification risks in small‑population contexts like Isabela province. [unacknowledged]
- User satisfaction and success rate improvements conflate the online system's effect with data mining — causal attribution is unclear.

## Remember This

- 🔑 **80% accuracy** for decision trees on a Philippine government classification task — a usable benchmark for Odin's profiling module.
- 📌 **31% higher success rate** from online system integration — shows tangible value of data‑driven decision support.
- 🧠 RA 10173 compliance precedent — anonymization, encryption, and consent procedures are directly transferable to Odin's privacy design.
- ✅ Precision, recall, and F1‑score were all reported — a complete evaluation template for Odin's classifier comparisons.
- ⚠️ Domain mismatch — scholarship applicant classification ≠ financial behavior profiling; use only as method precedent, not evidence of financial patterns.
