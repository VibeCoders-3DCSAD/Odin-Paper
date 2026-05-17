# Evolving Strategies in Machine Learning: A Systematic Review of Concept Drift Detection

## Metadata

```yaml
---
paper_id: "10.3390/info15120786"
designation: international
title: "Evolving Strategies in Machine Learning: A Systematic Review of Concept Drift Detection"
authors: "Hovakimyan, G.; Bravo, J. M."
year: 2024
venue: "Information"
odin_topics: ["5.B", "5.C", "6.A", "8.A"]
shorthand_tags: ["/concept-drift", "/classifier-tradeoffs", "/forecasting-methods-survey", "/temporal-dependency", "/anomaly-taxonomy"]
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

Concept drift detection methods keep machine learning models accurate as data distributions change; this review compares drift detection, window-based, unsupervised, ensemble, and neural network approaches over two decades of research.

## Problem and Motivation

Machine learning models assume static data distributions, but real-world data streams change over time, degrading model performance. This concept drift affects critical applications like fraud detection, financial forecasting, and healthcare monitoring. Prior reviews lacked systematic comparison of diverse detection methodologies and emerging trends.

## Approach

- Systematic review following PRISMA guidelines, using IEEE and Science Direct APIs to identify 450 initial studies.
- T5 NLP model used to screen abstracts, narrowing to 111 eligible studies and finally 65 high-impact papers.
- Methods categorized into five types: drift detection mechanisms (DDM), window-based mechanisms (WBM), unsupervised/semi-supervised (USSM), ensemble methods (EM), and neural networks (NN).
- Quality assessment using adapted Newcastle-Ottawa Scale and CASP checklists, scoring each study 1–5 on methodological clarity, empirical validation, reproducibility, and practical relevance.
- Evaluation metrics include prequential error, handling imbalanced classification, speed (training/prediction time, throughput, latency), and dataset characteristics.

## Findings

1. **45%** of the 111 studies were rated high quality (score 4–5), 41% moderate, and 14% low.
2. Ensemble methods and neural networks achieve **very high accuracy** but incur high computational cost; DDMs and WBMs offer a balance of accuracy and efficiency.
3. Unsupervised/semi-supervised methods excel at novel class detection and handle sparse labeled data.

- Drift detection mechanisms (DDM) use statistical process control with warning (`pmin+2smin`) and drift (`pmin+3smin`) thresholds.
- WBMs like ADWIN detect sudden drifts effectively but are computationally intensive and struggle with gradual drift.
- Challenges remain: imbalanced data, computational efficiency, application to non-tabular data (images, time series), and regression-task drift.

## Key Figures and Tables

- Figure 1: Distribution-based concept drift → virtual drift, real drift, and novel class appearance.
- Figure 2: Pattern-based concept drift → sudden, incremental, gradual, and recurrent drift patterns.
- Table 2: Summary of concept drift types → examples: market crashes (sudden), seasonal sales (recurrent).
- Table 4: Comparison of methods by accuracy, cost, applicability → EMs and NNs have very high accuracy and high cost.
- Table 5: Datasets for concept drift detection → SEA Concepts (abrupt), Hyperplane (gradual), Credit Card Fraud (imbalanced).

## Key Equations

$$ \text{Adjusted Citation Rate} = \frac{\text{Total Number of Citations}}{\text{Years Since Publication}} $$
*Measures paper influence normalized by age.*

$$ Acc_{t+1} = \frac{t \times Acc_t + \delta_{t+1}}{t+1} $$
*Updates model accuracy incrementally as each new instance arrives.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Concept drift | Change in the statistical properties of a target variable over time, degrading model performance. |
| DDM | Drift Detection Mechanism — monitors model error rate using statistical process control to trigger adaptation. |
| WBM | Window-Based Mechanism — uses sliding or adaptive windows to compare historical and new data distributions. |
| USSM | Unsupervised and Semi-Supervised Methods — detect drift using clustering or density estimation with minimal labeled data. |
| EM | Ensemble Method — combines multiple models to improve robustness and accuracy under drift. |
| NN | Neural Network — deep learning models (e.g., ELM, LSTM) that adapt to complex, non-linear drift patterns. |
| ELM | Extreme Learning Machine [think: single-hidden-layer network trained in one step, not iteratively] |
| LSTM | Long Short-Term Memory [think: recurrent network with memory cells that learn what to forget] |
| Prequential error | Accuracy measured sequentially as each test instance arrives, updating incrementally without separate test set. |
| SMOTE | Synthetic Minority Over-sampling Technique — generates synthetic examples to balance imbalanced classes. |
| MOA | Massive Online Analysis — open-source framework for data stream mining and drift detection benchmarking. |

## Critical Citations

- [Gama et al., 2004] — Introduced DDM, the benchmark drift detection method using error rate thresholds.
- [Bifet & Gavalda, 2007] — ADWIN algorithm for adaptive windowing, foundational for stream drift detection.
- [Lu et al., 2019] — Comprehensive review of learning under concept drift, defining taxonomy and challenges.
- [Brzezinski & Stefanowski, 2014] — OAUE ensemble method combining block-based and online learning for drift adaptation.

## Relevance to Odin

**Topics:**

5.B — Profile Dynamics and the Cold-Start Problem

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

8.A — Anomaly Detection in Personal Finance Systems

**Contribution to Odin:**

This paper provides a comprehensive survey of concept drift detection methods, directly informing how Odin's profiling, forecasting, and anomaly detection modules adapt to changing user behavior over time. The comparison of DDM, window-based, ensemble, and neural network methods offers trade-offs between accuracy and computational cost that guide algorithm selection for a mobile-first system. The review's identification of challenges—imbalanced data, computational efficiency, and non-tabular data—maps to Odin's constraints (sparse transactions, mobile resources, transaction sequences). The finding that ensemble methods and neural networks achieve very high accuracy but high cost justifies a hybrid approach: lightweight DDMs for real-time drift detection with periodic retraining.

**Directly justifies:**

- "Concept drift detection mechanisms (DDM) using statistical process control can detect abrupt and gradual changes in user spending patterns by monitoring classification error rates over time."
- "Window-based methods like ADWIN detect sudden drift efficiently but are sensitive to noise and computationally intensive — trade-off relevant for mobile deployment."
- "Unsupervised and semi-supervised methods detect novel spending categories (e.g., new merchant types) without requiring labeled data, addressing Odin's cold-start problem."
- "Ensemble methods achieve very high accuracy across drift types but incur high computational cost; Odin should consider lightweight ensembles or hybrid approaches."
- "Handling imbalanced data (e.g., rare anomalies) remains a challenge; techniques like SMOTE and cost-sensitive learning improve minority class detection in drifting streams."

**Limits of relevance:**

- The review focuses on general concept drift detection, not specifically on personal finance or spending data.
- Most benchmark datasets are synthetic or from domains like electricity markets, not Filipino young professional spending.
- Computational cost comparisons assume server-grade resources; mobile constraints (battery, CPU) are not evaluated.
- The review does not address concept drift in manual-entry transaction data where ground truth for classification may be delayed or missing.

## Limitations

- The review's own methodology uses citation rate as a quality proxy, which may favor older papers. [unacknowledged]
- Most included studies use synthetic or controlled datasets; real-world applicability to personal finance is assumed but not tested.
- No meta-analysis or quantitative pooling of effect sizes across studies.
- Concept drift detection for regression tasks (e.g., spending amount prediction) is explicitly noted as underexplored.
- Unsupervised drift detection methods are less studied; many methods require labeled data streams, which Odin may lack initially.

## Remember This

- 🔑 **45% of studies high quality** — DDM, ADWIN, ensembles, and NNs are the main method families.
- ⚠️ Ensemble and NN methods give **very high accuracy** but high computational cost — balance needed for mobile.
- 💡 Unsupervised methods detect novel classes without labels — key for Odin's cold-start profiling.
- 📌 Challenges remain: imbalanced data, regression drift, and non-tabular (time-series) data — all relevant to spending forecasts.
- ✅ DDM uses warning (`pmin+2smin`) and drift (`pmin+3smin`) thresholds — simple rule for real-time adaptation.
