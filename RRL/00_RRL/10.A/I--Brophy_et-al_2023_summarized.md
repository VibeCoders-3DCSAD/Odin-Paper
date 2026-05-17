# Generative Adversarial Networks in Time Series: A Systematic Literature Review

## Metadata

```yaml
---
paper_id: "10.1145/3559540"
designation: international
title: "Generative Adversarial Networks in Time Series: A Systematic Literature Review"
authors: "Brophy, E.; Wang, Z.; She, Q.; Ward, T."
year: 2023
venue: "ACM Computing Surveys"
odin_topics: ["8.A", "8.B", "10.A", "12.B"]
shorthand_tags: ["/anomaly-ml-families", "/anomaly-algo-candidates", "/anomaly-unsupervised-baseline", "/anomaly-eval-metrics", "/data-sensitivity", "/privacy-by-design", "/eval-ml-design"]
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

Time series GANs can generate high-quality synthetic data, detect anomalies, and preserve privacy, but training instability and lack of standardized evaluation remain open challenges.

## Problem and Motivation

Despite GANs' success in computer vision, their application to time series data—where temporal dependencies matter—remains underexplored and fragmented. Time series data shortage, missing values, and privacy regulations create urgent need for generative models that can synthesize realistic sequences without exposing sensitive information. No prior systematic review focused specifically on time series GAN architectures, evaluation metrics, or privacy-preserving mechanisms.

## Approach

- Classification of time series GANs into **discrete variants** (token sequences like text) and **continuous variants** (real-valued signals like medical data).
- Reviewed architectures: SeqGAN, C-RNN-GAN, RCGAN, TimeGAN, SigCWGAN, Quant GAN, NR-GAN, SC-GAN, SynSigGAN.
- Loss functions: minimax GAN, Wasserstein loss, feature matching, supervised + unsupervised combined loss (TimeGAN).
- Evaluation metrics: MMD, DTW, Wasserstein distance, TSTR (Train on Synthetic, Test on Real), classification accuracy as proxy for generation quality.
- Privacy techniques: differential privacy (DPGAN), federated learning (FedGAN), membership inference attacks to test re-identification risk.

## Findings

1. **GANs successfully generate realistic continuous time series** (ECG, EEG, music, financial data) with preserved temporal dynamics.
2. Discrete time series generation remains harder because small gradient changes don't map to token spaces; SeqGAN uses policy gradient and Monte Carlo search to work around this.
3. **TimeGAN outperforms RCGAN, C-RNN-GAN, and WaveGAN** by combining unsupervised GAN training with supervised autoregressive loss, preserving temporal dynamics better.
4. Privacy-preserving GANs (differential privacy, federated learning) can resist membership inference attacks, but data quality degrades as privacy guarantees tighten.
5. No standardized benchmark dataset or evaluation metric exists for time series GANs—unlike image GANs where FID and IS are consensus.

## Key Figures and Tables

- Figure 2: GAN architecture diagram → generator and discriminator play minimax game.
- Figure 3: Discrete vs. continuous time series plots → discrete has countable domain, continuous is real-valued signal.
- Table 1: Popular datasets (EEG, ECG, MIMIC-III, S&P 500) → no standardized benchmark for time series GANs.
- Table 2: GAN architectures by application and evaluation metrics → metrics vary widely across domains.
- Table 3-4: Sine wave and ECG generation results → LSTM-CNN with MSE loss achieves lowest MMD and DTW.

## Key Equations

$$ \min_G \max_D V(G,D) = \mathbb{E}_{x \sim p_{data}}[\log D(x)] + \mathbb{E}_{z \sim p_z}[\log(1 - D(G(z)))] $$
*Original GAN minimax objective: generator tries to fool discriminator.*

$$ \text{MMD}[F,X,Y] = \left[ \frac{1}{m^2}\sum_{i,j}k(x_i,x_j) - \frac{2}{mn}\sum_{i,j}k(x_i,y_j) + \frac{1}{n^2}\sum_{i,j}k(y_i,y_j) \right]^{1/2} $$
*Maximum Mean Discrepancy measures distribution similarity without density estimation.*

$$ W_p(\mu,\nu) = \left( \inf_{\gamma \in \Gamma(\mu,\nu)} \int_{X \times Y} d^p(x,y) \, d\gamma(x,y) \right)^{1/p} $$
*Wasserstein distance: cost to transform one distribution into another.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| GAN | Generative Adversarial Network — two neural networks (generator and discriminator) competing to create realistic synthetic data. |
| Time series | Sequence of values dependent on time, either continuous (every moment) or discrete (sampled intervals). |
| Mode collapse | GAN failure where generator produces only one type of output, losing diversity. |
| MMD | Maximum Mean Discrepancy — measures how different two probability distributions are using kernel functions. |
| DTW | Dynamic Time Warping — aligns two time series by stretching/compressing time to find optimal match. |
| TSTR | Train on Synthetic, Test on Real — evaluation method that trains a classifier on synthetic data and tests on real data. |
| Differential privacy | Mathematical guarantee that a model's output doesn't reveal whether any specific individual was in the training set. |
| LSTM | Long Short-Term Memory [think: RNN with a memory cell that learns what to forget] |
| RNN | Recurrent Neural Network — neural network with loops to process sequences. |

## Critical Citations

- [Goodfellow et al., 2014] — Introduced GAN minimax objective; foundational to all GAN research.
- [Yu et al., 2017 (SeqGAN)] — First framework to generate discrete sequences with GANs via policy gradient.
- [Esteban et al., 2017 (RCGAN)] — First to propose TSTR evaluation and apply GANs to medical time series.
- [Yoon et al., 2019 (TimeGAN)] — Combined supervised autoregressive loss with GAN to preserve temporal dynamics.
- [Dwork, 2006] — Defined differential privacy, the basis for privacy-preserving GANs.

## Relevance to Odin

**Topics:**

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

10.A — Data Privacy and Security in Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This review directly informs Odin's anomaly detection module by establishing GANs as a viable unsupervised method for detecting irregular spending patterns without labeled training data — critical for cold-start users. The paper's discussion of evaluation metrics (MMD, DTW, TSTR) provides a framework for validating Odin's anomaly detection algorithm, especially since spending data has strong temporal dependencies. Additionally, the review's coverage of differential privacy and membership inference attacks informs Odin's privacy-by-design requirements under RA 10173, showing that GAN-generated synthetic transaction data can be shared or used for testing without re-identification risk.

**Directly justifies:**

- "Unsupervised GANs (MAD-GAN) detect anomalies in multivariate time series without labeled data, achieving superior performance over shallow statistical methods on ECG and taxi datasets."
- "Train on Synthetic, Test on Real (TSTR) evaluation — training a classifier on synthetic data and testing on real data — provides a proxy for generation quality when ground truth distributions are unknown."
- "Differentially private GANs (DPGAN) add calibrated noise to gradients during training, providing mathematical guarantees against membership inference attacks at the cost of some data fidelity."
- "TimeGAN's hybrid loss (unsupervised GAN + supervised autoregressive) preserves temporal dynamics better than pure GANs, as measured by lower discriminative and predictive scores."
- "No standardized benchmark dataset for time series GANs means researchers must choose evaluation metrics (MMD, DTW, Wasserstein) appropriate to their specific data characteristics."

**Limits of relevance:**

- Review covers general time series (medical, audio, financial) — not personal spending transaction sequences specifically.
- GAN training requires significant computational resources and stable data distributions; real-time anomaly detection on a mobile device may be infeasible.
- Differential privacy methods trade off data quality for privacy — the acceptable degradation for spending forecasting is unknown.
- Most reviewed GANs generate full sequences, not point anomalies; applying them to Odin's per-transaction alerting requires adaptation.
- No Filipino financial data context; spending pattern morphology differs from ECG or stock price signals.

## Limitations

- No standardized benchmark dataset or evaluation metric for time series GANs — each paper uses different data and metrics, making comparisons difficult. [unacknowledged]
- Training instability and mode collapse remain unsolved for many architectures; papers report only successful runs.
- Privacy evaluations (membership inference attacks) are not uniformly applied; some GANs claim privacy without differential privacy guarantees.
- Sequence length handled by reviewed GANs is typically short (≤200 timesteps); longer spending histories may cause performance degradation. [unacknowledged]
- Real-time generation for anomaly detection is not discussed — most GANs are trained offline and used for batch generation.

## Remember This

- 🔑 **Unsupervised anomaly detection** — GANs detect outliers without labeled data, crucial for Odin's cold-start users.
- 📌 **No benchmark exists** — each time series GAN paper uses different datasets and metrics, so compare carefully.
- 💡 **TSTR evaluation** — train on synthetic, test on real; a proxy for generation quality when real distribution is unknown.
- ⚠️ **Differential privacy degrades quality** — stronger privacy guarantees mean less realistic synthetic data; find the trade-off.
- 🧠 **TimeGAN beats pure GANs** — adding autoregressive loss preserves temporal dynamics better than standard GANs.
