# Dive into Time-Series Anomaly Detection: A Decade Review

## Metadata

```yaml
---
paper_id: "5c8e6f2a-3d4b-4e8f-9a2c-1b3e5f7a9d2b"
designation: international
title: "Dive into Time-Series Anomaly Detection: A Decade Review"
authors: "Boniol, P.; Liu, Q.; Huang, M.; Palpanas, T.; Paparrizos, J."
year: 2024
venue: "Unknown"
odin_topics: ["E.1", "E.2", "D.2", "J.1"]
shorthand_tags: ["/anomaly-taxonomy", "/anomaly-approaches", "/anomaly-ml-families", "/lstm-architecture", "/isolation-forest", "/eval-frameworks"]
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

A process-centric taxonomy organizes a decade of time-series anomaly detection into distance, density, and prediction-based methods, revealing a surge in deep learning approaches after 2016.

## Problem and Motivation

Research communities in time-series anomaly detection remain disconnected, using different datasets, baselines, and evaluation measures, making it impossible to identify the best method for a given use case. The exploding volume of IoT time series creates an abundance of anomalies, yet no unified framework exists to compare methods fairly. Prior surveys focused on general-purpose anomaly detection or only briefly covered time-series methods, lacking a comprehensive taxonomy and meta-analysis.

## Approach

- Collect and group anomaly detection algorithms into a process-centric taxonomy with three first-level categories: distance-based, density-based, and prediction-based.
- Further split into nine second-level categories: proximity, clustering, discord (distance); distribution, graph, tree, encoding (density); forecasting, reconstruction (prediction).
- Perform meta-analysis of 40+ years of literature, tracking trends by category, supervision level, and univariate/multivariate capability.
- List existing benchmarks (NAB, Yahoo, Exathlon, KDD21, TODS, TimeEval, TSB-UAD, TSB-AD) with their properties.
- Review evaluation measures, including threshold-based (precision, recall, F-score) and threshold‑independent (AUC, Range‑AUC, Volume Under the Surface).

## Findings

1. Number of anomaly detection methods remained constant until 2016, then **increased sharply** — prediction‑based methods (LSTM and autoencoder) represent **almost 50%** of new methods introduced between 2020‑2023.
2. Between 1980‑2000, 65% of methods were unsupervised; between 2012‑2018, that dropped to 50%.
3. Before 2016, most methods targeted multivariate time series; after 2016, univariate methods dominate due to growing interest in subsequence anomalies.

- Deep learning libraries (TensorFlow, PyTorch) accelerated adoption of LSTM and autoencoder‑based detectors.
- No single anomaly detection method outperforms all others across all datasets — model selection is essential.

## Key Figures and Tables

- Figure 8: Complete taxonomy tree with methods mapped on y‑axis by publication year → shows dominance of prediction‑based methods after 2016.
- Figure 20: Number of methods per time interval and cumulative per category → prediction‑based (reconstruction + forecasting) overtakes distance and density after 2016.
- Table 4: Summary of 8 benchmarks (NAB to TSB‑AD) with #time series, avg length, anomaly type, dimensions → TSB‑AD is the largest (1,070 curated series).
- Figure 22: Illustration of evaluation measures (threshold‑based, AUC, Range‑AUC, VUS) → VUS‑ROC is recommended for robustness.

## Key Equations

$$rd_k(A,B) = max(k\text{-}distance(B), d(A,B))$$
*Reachability distance: the larger of the k-th neighbor distance or direct distance.*

$$LOF_k(A) = \frac{\sum_{B \in N_k(A)} lrd_k(B) / |N_k(A)|}{lrd_k(A)}$$
*Local Outlier Factor: average local density of neighbors divided by own density.*

$$S(x,n) = 2^{-\frac{E[h(x)]}{c(n)}}, \quad c(n) = H(n-1) - \frac{2(n-1)}{n}$$
*Isolation Forest anomaly score: shorter average path length → higher anomaly probability.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Point anomaly | Single value far outside the normal range. |
| Contextual anomaly | Value within global range but abnormal for a specific local window. |
| Collective anomaly | A subsequence whose pattern does not repeat any previously observed pattern. |
| Discord | Subsequence whose distance to its nearest neighbor is the largest among all subsequences. |
| Matrix Profile | Time series of distances from each subsequence to its nearest neighbor. |
| LSTM | Long Short-Term Memory [think: cell with forget/input/output gates that learns what to remember and forget]. |
| Autoencoder | Neural network that compresses input to a latent space and reconstructs it; reconstruction error signals anomalies. |
| GAN | Generative Adversarial Network [think: generator creates fake data, discriminator tries to spot fakes]. |
| VUS-ROC | Volume Under the Surface of ROC curves over varying buffer lengths; threshold‑free metric for subsequence anomalies. |

## Critical Citations

- [Hawkins, 1980] — Foundational definition of an outlier as an observation deviating so much that it suggests a different generating mechanism.
- [Breunig et al., 2000] — Introduced Local Outlier Factor (LOF), the basis for many proximity‑based time‑series detectors.
- [Liu et al., 2008] — Isolation Forest, a tree‑based anomaly detector that isolates anomalies with fewer random partitions.
- [Malhotra et al., 2015] — First application of LSTM to time‑series anomaly detection using prediction error as anomaly score.
- [Paparrizos et al., 2022] — Proposed VUS (Volume Under the Surface) as a robust evaluation measure for time‑series anomalies.

## Relevance to Odin

**Topics:**

E.1 — Anomaly Detection in Personal Finance Systems

E.2 — Anomaly Detection Algorithm

D.2 — LSTM as the Spending Forecasting Algorithm

J.1 — System Evaluation

**Contribution to Odin:**

This survey directly informs Odin’s anomaly detection module by providing a structured taxonomy of candidate algorithms, including Isolation Forest (a leading candidate) and LSTM-based detectors (relevant to the forecasting module). The meta-analysis shows that prediction-based methods (LSTM/autoencoder) dominate recent research, justifying Odin’s choice of LSTM for forecasting while also supporting its use for anomaly detection via prediction error. The detailed review of evaluation metrics—especially the recommendation of VUS-ROC over point‑adjusted metrics—guides how Odin should measure anomaly detection performance in a time‑series context.

**Directly justifies:**

- “Isolation Forest isolates anomalies by random partitioning; anomalies require fewer partitions than normal points, enabling unsupervised detection without labeled training data.”
- “LSTM‑based anomaly detection uses prediction error on normal training data — a higher error indicates an anomaly (Malhotra et al., 2015).”
- “Between 2020 and 2023, prediction‑based methods (including LSTM and autoencoders) represent nearly 50% of new time‑series anomaly detection methods.”
- “Volume Under the Surface (VUS-ROC) is the recommended evaluation measure for time‑series anomaly detection due to its robustness to label noise and detector lag (Paparrizos et al., 2022).”
- “No single anomaly detection method outperforms all others across datasets; model selection (e.g., using simple classification baselines) is essential and can double accuracy (Sylligardos et al., 2023).”

**Limits of relevance:**

- The survey is domain‑agnostic; financial spending anomalies (e.g., budget overages) are not specifically analyzed.
- All findings are based on benchmark datasets from diverse fields (sensors, space, medicine), not Filipino personal finance data.
- Many methods assume clean training data (semi‑supervised) or streaming sensors; Odin’s manual input and cold‑start profiles may violate those assumptions.
- The evaluation metrics discussion does not address human‑centric metrics like usability or user trust.

## Limitations

- The survey does not provide empirical head‑to‑head comparisons across all methods; it cites external benchmarks instead. [unacknowledged]
- Many deep learning methods (LSTM, autoencoder) require large training sets, which may not be available for new Odin users.
- The taxonomy excludes methods that combine multiple anomaly types (e.g., hybrid point+sequence detection) in a single unified framework.
- Real‑world deployment considerations (latency, memory on mobile devices) are not addressed.
- The paper focuses on univariate and multivariate time series but does not handle irregularly sampled or non‑continuous timestamps common in manual expense entry.

## Remember This

- 🧠 **50% of new anomaly methods (2020‑2023)** — prediction‑based (LSTM/autoencoder) now dominate the field.
- 🔑 Isolation Forest isolates anomalies faster — random partitioning works without labels.
- 📌 **VUS-ROC** is the go‑to evaluation metric for time‑series anomalies, not point‑adjusted F1.
- ⚠️ No single best detector exists — model selection can **double accuracy** over any individual method.
- 💡 LSTM predicts the next value; high prediction error = anomaly — unifies forecasting and detection.
