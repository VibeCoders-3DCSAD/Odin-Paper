# Concept Drift Adaptation Methods under the Deep Learning Framework: A Literature Review

## Metadata

```yaml
---
paper_id: "10.3390/app13116515"
designation: international
title: "Concept Drift Adaptation Methods under the Deep Learning Framework: A Literature Review"
authors: "Xiang, Q.; Zi, L.; Cong, X.; Wang, Y."
year: 2023
venue: "Applied Sciences"
odin_topics: ["5.B", "5.C", "6.A", "6.B", "8.A", "8.B"]
shorthand_tags: ["/concept-drift", "/progressive-reclassification", "/forecasting-methods-survey", "/forecast-algo-candidates", "/anomaly-ml-families"]
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

Deep learning models fail when data distributions change over time; adaptation methods using discriminative, generative, hybrid, transfer, or reinforcement learning maintain prediction accuracy under concept drift.

## Problem and Motivation

Data streams in dynamic environments (epidemics, financial markets) undergo distribution changes called concept drift, which renders pre‑trained deep learning models obsolete and inaccurate. Without adaptation, predictive systems produce unreliable outputs, leading to poor decisions in applications like anomaly detection, forecasting, and investment. Prior surveys covered shallow or ensemble methods but lacked a systematic review of deep‑learning‑based drift adaptation.

## Approach

- Definition: Concept drift occurs when joint probability distribution Pt(x,y) changes over time (abrupt, incremental, gradual, or recurring).
- Three causal types: virtual drift (P(x) changes), real drift (P(y|x) changes), and hybrid drift (both change).
- General adaptation pipeline: data stream → deep learning model → drift detection (active or passive) → model update (parameter or structure update).
- Discriminative learning methods (MLP, RNN, LSTM, CNN): detect drift via error rate, sliding windows, or statistical tests; update weights or add/prune neurons.
- Generative learning methods (AE, GAN, RBM, SOM): use reconstruction error or KL divergence to detect drift; retrain or adjust hidden nodes.
- Hybrid learning: combine LSTM with CNN, AE, or ARIMA; use ensemble weighting or attention modules to adapt.
- Other methods: deep transfer learning (patch networks, knowledge distillation) and deep reinforcement learning (online policy updates).

## Findings

1. **Parameter updates (weight adjustments) dominate over structure updates** because they converge faster and handle abrupt drift effectively.
2. Active drift detection (e.g., ADWIN, STEPD, CUSUM) appears in ~half of discriminative and generative methods; passive continuous updating is common in hybrid approaches.
3. **Abrupt drift is the most frequently addressed type**, while recurring drift receives least attention despite reappearing in cyclical domains.
4. LSTM‑based adaptation (I‑LSTM, AD‑LSTM, Fog‑DeepStream) achieves strong results in anomaly detection and power forecasting by weighting newer data higher.
5. Autoencoder‑based generative methods (ARCUS, MemStream) enable unsupervised drift adaptation for high‑dimensional anomaly detection without labels.
6. Hybrid LSTM+CNN and LSTM+AE models overcome catastrophic forgetting and improve long‑term prediction under gradual and recurring drift.
7. Deep reinforcement learning (DeepPocket, DeepBreath) adapts investment portfolios to market drift but requires long training times.

## Key Figures and Tables

- Figure 1: Causes of concept drift (virtual, real, hybrid) → real drift changes decision boundary, virtual drift does not.
- Figure 2: Four drift types (abrupt, incremental, gradual, recurring) → recurring drift reuses past concepts.
- Figure 3: General adaptation process under deep learning → drift detection + model update loop.
- Table 1: Discriminative learning methods (MLP/RNN/LSTM/CNN) → most use active detection and parameter updates.
- Table 2: Generative learning methods (AE/GAN/RBM/SOM) → predominantly unsupervised, many address abrupt+incremental drift.

## Key Equations

$$ \exists x : P_{t0}(x,y) \neq P_{t1}(x,y) $$
*Concept drift occurs when joint distribution changes from time t0 to t1.*

$$ P(y|x) = \frac{P(y) \cdot P(x|y)}{P(x)} $$
*Real drift can also arise from changes in P(y) or P(x|y) via Bayes’ rule.*

$$ T(v_o, v_r, n_o, n_r) = \frac{|v_o/n_o - v_r/n_r| - 0.5 \times (1/n_o + 1/n_r)}{\sqrt{\mu + (1-\mu) \times (1/n_o + 1/n_r)}} $$
*STEPD drift detection compares accuracy between overall and recent windows.*

$$ D_{KL}(G \parallel Q) = \sum_{z \in Z} G(z) \log\left(\frac{G(z)}{Q(z)}\right) $$
*Kullback‑Leibler divergence measures distribution change in generative drift detection.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Concept drift | Change in the underlying statistical distribution of streaming data over time. |
| Abrupt drift | Concept changes suddenly in a short time (e.g., market crash). |
| Incremental drift | Concept drifts slowly and continuously (e.g., gradual economic recovery). |
| Gradual drift | Old and new concepts alternate before stabilizing (e.g., equipment failing intermittently). |
| Recurring drift | Previous concepts reappear later (e.g., seasonal spending patterns). |
| Virtual drift | Only input distribution P(x) changes; decision boundary unchanged. |
| Real drift | Conditional distribution P(y/x) changes; model must relearn. |
| ADWIN | Adaptive sliding window that detects drift by comparing means of two sub‑windows. |
| STEPD | Statistical Test of Equal Proportions — compares recent vs. overall accuracy. |
| CUSUM | Cumulative sum test for change detection in sequential data. |
| LSTM [think: memory cell with forget gate] | Long Short‑Term Memory; RNN variant that handles long sequences and mitigates vanishing gradients. |
| AE | Autoencoder; unsupervised neural network that learns compressed representations via reconstruction. |
| GAN | Generative Adversarial Network; generator‑discriminator pair that learns data distribution. |
| DTL | Deep Transfer Learning; transfers knowledge from pre‑trained model to new task with minimal data. |
| DRL | Deep Reinforcement Learning; combines deep perception with reward‑based decision making. |

## Critical Citations

- [Schlimmer & Granger, 1986] — First formal definition of concept drift; foundational for all drift adaptation research.
- [Gama et al., 2014] — Seminal survey on concept drift adaptation methods; defines active vs. passive modes and evaluation metrics.
- [Lu et al., 2018] — Comprehensive review covering drift types, detection algorithms, and applications in data‑driven decision support.
- [Xu et al., 2020] — I‑LSTM method with time‑weighted sampling; directly cited for anomaly detection under drift in IoT.

## Relevance to Odin

**Topics:**

5.B — Profile Dynamics and the Cold‑Start Problem

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

**Contribution to Odin:**

This review provides the theoretical foundation for why Odin’s behavioral profiles, spending forecasts, and anomaly detectors must adapt over time. User financial behavior drifts due to job changes, salary adjustments, new obligations (e.g., rent, family support), or seasonal spending (holidays, 13th month pay). Without concept drift adaptation, a model trained on a user’s past transactions becomes obsolete. The paper’s taxonomy of drift types (abrupt, incremental, gradual, recurring) directly informs Odin’s profiling module design — recurring drift justifies storing past profile states for seasonal reuse, while abrupt drift detection (using methods like ADWIN or STEPD) triggers immediate model updates. The comparison between parameter updates (faster, suits abrupt drift) and structure updates (more flexible, suits recurring drift) guides Odin’s implementation choices for forecasting and anomaly detection algorithms.

**Directly justifies:**

- "User financial behavior evolves over time (concept drift); a static spending forecast model becomes inaccurate within months unless updated via drift adaptation."
- "Parameter updates (e.g., retraining only the last layer) converge faster than full structure updates, making them suitable for detecting abrupt changes in spending patterns after a job loss or salary increase."
- "Recurring drift (e.g., higher spending every December) can be handled by storing and reactivating past profile states, reducing computational overhead."
- "Unsupervised drift detection using autoencoder reconstruction error enables anomaly detection in spending without requiring labeled fraud data, applicable to Odin’s cold‑start problem."
- "LSTM‑based models with time‑weighted sampling (I‑LSTM) improve anomaly detection under drift by assigning higher importance to recent transactions."

**Limits of relevance:**

- The review focuses on deep learning; Odin may use lighter models (e.g., gradient boosting, logistic regression) for resource‑constrained mobile deployment.
- Most evaluated datasets are not financial (e.g., electricity, weather, network intrusion); financial transaction patterns have different drift characteristics (e.g., slower, more seasonal).
- Many methods require labeled data for drift detection; Odin’s manual transaction input produces sparse labels (user‑corrected categories), limiting supervised drift detection.
- Computational overhead of active drift detection (e.g., STEPD, CUSUM) may conflict with mobile‑first, battery‑sensitive design.

## Limitations

- Review does not quantitatively compare adaptation methods across standard financial benchmarks — lacks performance metrics (e.g., MAE improvement, detection delay). [unacknowledged]
- Most cited methods were evaluated on public datasets (Electricity, Weather, KDD Cup) that differ from personal transaction streams in volume, sparsity, and label availability.
- No discussion of concept drift adaptation under cold‑start conditions (new users with no history), which is critical for Odin.
- The paper acknowledges that recurring drift is under‑addressed — yet recurring seasonal spending is highly relevant to Filipino young professionals (13th month pay, Christmas, back‑to‑school).
- Many active detection methods (ADWIN, STEPD, CUSUM) require tuning hyperparameters (window sizes, thresholds) that are not transferable across users without calibration.

## Remember This

- 🔑 **Concept drift = data distribution changes** — static models fail; adaptation is non‑negotiable for Odin’s long‑term accuracy.
- 📌 Four drift types: abrupt (job loss), incremental (salary growth), gradual (new habit forming), recurring (holiday spending) — each needs different handling.
- 💡 Parameter updates (re‑train last layer) beat full retraining for abrupt drift — faster and mobile‑friendly.
- 🔍 Unsupervised AE‑based drift detection works without labeled data — perfect for Odin’s cold‑start anomaly detection.
- ⚠️ Recurring drift is underexplored — Odin’s seasonal spending patterns may require novel adaptation logic.
