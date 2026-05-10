# A Survey of Deep Anomaly Detection in Multivariate Time Series: Taxonomy, Applications, and Directions

## Metadata

```yaml
---
paper_id: "10.3390/s25010190"
designation: international
title: "A Survey of Deep Anomaly Detection in Multivariate Time Series: Taxonomy, Applications, and Directions"
authors: "Wang, F.; Jiang, Y.; Zhang, R.; Wei, A.; Xie, J.; Pang, X."
year: 2025
venue: "Sensors"
odin_topics: ["D.1", "D.2", "E.1", "E.2"]
shorthand_tags: ["/anomaly-taxonomy", "/anomaly-approaches", "/anomaly-ml-families", "/anomaly-algo-tradeoffs", "/forecasting-methods", "/lstm-architecture"]
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

Deep learning methods for multivariate time series anomaly detection are organized into forecasting, reconstruction, and contrastive approaches, with **46 models** reviewed and a new anomaly type taxonomy proposed.

## Problem and Motivation

Traditional anomaly detection methods (statistical, distance-based, density-based) struggle with high-dimensional multivariate time series and the lack of labeled anomalies. Deep learning offers powerful tools to capture temporal dependencies and inter-variable relationships simultaneously. No prior survey had systematically categorized deep MTSAD methods by learning paradigm and neural architecture with explicit pros and cons.

## Approach

- **Anomaly type taxonomy** – Introduces three categories: point-wise (global/local), pattern-wise (shapelet, trend, cycle), and inter-metric (global, local, temporal-local).
- **Learning paradigms** – Covers unsupervised, semi-supervised, and self-supervised methods; self-supervision creates supervisory signals from unlabeled data.
- **Model inputs** – Most recent MTSAD models use sliding windows (not single points) because anomalies often persist across time.
- **Forecasting methods** – Predict next timestamps; error signals anomalies. Includes CNN-based (DeepAnt, TimesNet), RNN-based (LSTM-NDT, THOC), GNN-based (GDN, MTAD-GAT), and Transformer-based (AnomalyBERT, MAD).
- **Reconstruction methods** – Encode data to latent space and reconstruct; large reconstruction error indicates anomaly. Includes AE (DAGMM, USAD), VAE (OmniAnomaly), GAN (MAD-GAN, TadGAN), Transformer (Anomaly Transformer, TranAD), and Diffusion (DiffusionAE, D3R).
- **Contrastive methods** – Learn by contrasting positive/negative pairs; includes LLM-based (AnomalyLLM), MLP-Mixer (PatchAD), and Transformer (DCdetector, SimAD).
- **Datasets** – Compiles 33 public datasets across 10 domains: astronomy, aerospace, environmental science, IoT, finance, cybersecurity, ICS, healthcare, server monitoring, infrastructure.

## Findings

- Deep learning models for MTSAD outperform classical methods by jointly capturing temporal and inter-variable dependencies.
- Transformer-based models excel at long-range dependencies but may overlook contextual information without adjustments.
- **Reconstruction methods are the most mature**; VAE-based models (OmniAnomaly, InterFusion) handle temporal dependencies among random variables explicitly.
- Contrastive learning (e.g., DCdetector) produces permutation-invariant representations with superior discriminative capability.
- LLMs applied to TSAD require prompt engineering or distillation; they struggle with complex context anomalies and may hallucinate.
- Frequency-domain integration (Dual-TF, CATCH) improves detection by aligning time and frequency granularities.
- Diffusion models (DiffusionAE, D3R) show robustness to varying anomaly ratios and missing data.

## Key Figures and Tables

- Figure 1: Anomaly type classification framework → three main branches: point-wise, pattern-wise, inter-metric anomalies.
- Figure 2: Point-wise (a) and pattern-wise (b) anomalies → red dots/spikes vs. red subsequence regions.
- Figure 3: Inter-metric anomalies → global (a), local (left red), temporal-local (right red).
- Table 1: 46 deep MTSAD models → lists model name, learning paradigm, input type, architecture, and framework.
- Table 2: Public datasets for MTSAD → 33 datasets with domain, samples, dimensions, and anomaly rate.

## Key Equations

$$|x_t - \hat{x}_t| > \delta$$
*Global point anomaly: prediction error exceeds a threshold scaled by context variance.*

$$diss_p(p, \hat{p}) > \delta$$
*Shapelet anomaly: a subsequence deviates significantly from expected pattern shape.*

$$X_k = \sum_{t=0}^{T-1} x_t e^{-i2\pi k t / T}$$
*Discrete Fourier Transform converts time-domain signal to frequency domain for cycle detection.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| MTSAD | Multivariate Time Series Anomaly Detection – finding unusual patterns across multiple related time streams. |
| Point-wise anomaly | A single data point (spike or glitch) that differs from expected value. |
| Pattern-wise anomaly | A subsequence whose shape, trend, or cycle deviates from normal patterns. |
| Inter-metric anomaly | The correlation between two or more metrics breaks down, either globally or locally. |
| Forecasting-based | Predict next value; large prediction error → anomaly. |
| Reconstruction-based | Encode then decode; large reconstruction error → anomaly. |
| Contrastive learning | Learn by pulling similar pairs together and pushing dissimilar pairs apart. |
| VAE | Variational Autoencoder – learns probability distribution of normal data; anomalies have low reconstruction probability. |
| GAN | Generative Adversarial Network – generator mimics normal data, discriminator spots fakes; anomaly scores from discriminator. |
| LSTM [think: memory cell with forget gate] | Long Short-Term Memory – RNN variant that captures long-range dependencies without vanishing gradients. |
| Transformer | Self-attention architecture that processes all time steps in parallel; excels at long-range patterns. |

## Critical Citations

- [Hochreiter & Schmidhuber, 1997] — Original LSTM paper; foundation for RNN-based MTSAD models.
- [Vaswani et al., 2017] — Transformer architecture; basis for Anomaly Transformer, TranAD, and CLFormer.
- [Goodfellow et al., 2014] — Generative Adversarial Networks; used in MAD-GAN, TadGAN, and DCGANs.
- [Zong et al., 2018] — DAGMM; first deep autoencoder + GMM for unsupervised anomaly detection.

## Relevance to Odin

**Topics:**

E.1 — Anomaly Detection in Personal Finance Systems

E.2 — Anomaly Detection Algorithm

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

**Contribution to Odin:**

This survey directly informs Odin’s anomaly detection module by providing a structured taxonomy of anomaly types (point-wise vs. pattern-wise vs. inter-metric) and a comparative analysis of deep learning approaches (forecasting, reconstruction, contrastive). The pros/cons analysis of LSTM-based forecasting methods (e.g., LSTM-NDT, THOC) justifies Odin’s LSTM choice for spending forecasting, while the review of reconstruction methods (VAE, AE, GAN) offers alternatives for behavior-driven anomaly detection if Odin later moves beyond simple rule-based overage alerts. The survey’s discussion of cold-start challenges and the need for unsupervised methods maps directly to Odin’s requirement for anomaly detection without labeled training data.

**Directly justifies:**

- "LSTM-based forecasting methods for multivariate time series anomalies achieve robust detection using non-parametric dynamic thresholding on prediction residuals (LSTM-NDT, 2018)."
- "Reconstruction-based methods using VAEs (OmniAnomaly, InterFusion) explicitly model temporal dependencies among random variables, enabling entity-level anomaly explanation without labeled data."
- "Contrastive learning approaches (DCdetector, SimAD) produce permutation-invariant representations that highlight distributional differences between normal and abnormal data, improving detection robustness."
- "Frequency-domain integration (Dual-TF, CATCH) aligns time and frequency granularities, improving point-level anomaly scoring over time-domain-only methods."
- "Diffusion models (DiffusionAE) smooth out abnormal fragments during reconstruction, yielding higher reconstruction errors for anomalies even under varying training anomaly ratios."

**Limits of relevance:**

- Survey does not evaluate Isolation Forest (Odin’s candidate algorithm) — all reviewed methods are deep learning, which may be computationally heavy for mobile-first Odin.
- No personal finance–specific anomalies or spending patterns are analyzed; the financial domain is mentioned only for fraud detection, not budget adherence.
- All datasets and models are from general MTS domains (aerospace, IoT, cybersecurity) — transferability to Filipino young professional spending data is unvalidated.
- The survey treats unsupervised learning as a strength, but Odin’s anomaly detection may also use rule-based overage alerts (not covered).
- LLM-based methods are nascent and require prompt engineering or fine-tuning; not suitable for Odin’s current resource constraints.

## Limitations

- Survey focuses exclusively on deep learning; classical methods (Isolation Forest, one-class SVM) are mentioned only as background, not compared. [unacknowledged]
- No empirical benchmarking or head-to-head performance metrics across the 46 models — only qualitative pros/cons.
- The proposed anomaly type taxonomy (point-wise, pattern-wise, inter-metric) is descriptive but not validated against real-world financial datasets. [unacknowledged]
- Datasets listed are predominantly from non-financial domains; financial datasets (Creditcard, NAB) are under-represented in the MTSAD literature reviewed.
- Future directions section lacks concrete guidance for personal finance or mobile-constrained applications.

## Remember This

- 🔑 **46 deep learning models** reviewed across forecasting, reconstruction, and contrastive families.
- 📌 Point-wise (single spike) vs. pattern-wise (subsequence) vs. inter-metric (broken correlations) — Odin needs all three for spending anomalies.
- 🧠 LSTM-NDT and OmniAnomaly are cited baselines — justify Odin’s LSTM forecasting and VAE-based reconstruction alternatives.
- 💡 Contrastive learning (DCdetector) highlights normal/abnormal distribution differences without labels — relevant to Odin’s cold-start anomaly detection.
- ⚠️ No Isolation Forest comparison — deep learning trade-offs (accuracy vs. mobile compute) must be evaluated separately.
