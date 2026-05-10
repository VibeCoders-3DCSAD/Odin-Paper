# Transformer Architectures in Time Series Analysis: A Review

## Metadata
```yaml
---
paper_id: "b3c7a9e1-5f6d-4b8c-9a2d-1e4f7a8b9c0d"
designation: international
title: "Transformer Architectures in Time Series Analysis: A Review"
authors: "Thundiyil, S.; Picone, J.; McKenzie, S."
year: 0000
venue: "Unknown"
odin_topics: ["D.1", "D.2", "E.2"]
shorthand_tags: ["/forecasting-methods", "/spending-time-series", "/temporal-dependency", "/lstm-vs-alternatives", "/anomaly-ml-families", "/isolation-forest"]
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[ ]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
---
```

## TL;DR

Transformer architectures using self-attention outperform traditional methods like LSTM on long-term time series forecasting, achieving up to 38% MSE reduction in benchmark datasets.

## Problem and Motivation

Traditional time series models (ARIMA, LSTM, GRU) have limited success capturing long-term dependencies critical for applications such as finance, healthcare, and climate forecasting. Inaccurate long-term context leads to poor predictions and missed rare events. No prior review systematically compared state-of-the-art transformer variants for time series forecasting, classification, and segmentation.

## Approach

- Reviews 11 transformer architectures applied to time series: LogTrans, TFT, InParformer, Informer, SageFormer, Autoformer, Pyraformer, W-Transformers, FEDformer, CrossFormer++, Transformer-XL.
- Covers traditional methods: ARIMA, LSTM, GRU, RNN, CNNs, reinforcement learning, nonparametric methods.
- Transformer core: scaled dot-product self-attention and multi-head attention enabling long-range dependencies without recurrence.
- LogTrans: hybrid CNN-transformer with Separate-Combiner (SeCo) module for biomedical image segmentation.
- Temporal Fusion Transformer (TFT): gated residual networks, LSTM encoders, multi-head attention for multi-horizon forecasting.
- Autoformer: decomposition architecture with autocorrelation mechanism; evaluated on six benchmark datasets.
- FEDformer: frequency-enhanced decomposed transformer using Fourier and wavelet transforms for long-term forecasting.
- W-Transformers: wavelet-based preprocessing (MODWT) for non-stationary univariate time series.
- Isolation Forest and One-class SVM mentioned as anomaly detection methods for time series data.
- Evaluations on ETT, Electricity, Exchange, Traffic, Weather, and ILI datasets.

## Findings

1. Autoformer achieved a **38% average MSE reduction** across six benchmarks (energy, traffic, economics, weather, disease) compared to prior state-of-the-art.
2. FEDformer reduced MSE by 14.8% relative to Autoformer, with over 20% improvement on Exchange and ILI datasets.
3. Pyraformer decreased MSE by 24.8–28.9% on ETTh1 for prediction lengths of 168, 336, and 720 steps.
4. InParformer outperformed FEDformer on Exchange dataset with MSE reduction up to 15.1%.
5. Transformer-XL reduced state-of-the-art perplexity from 20.5 to 18.3 on WikiText-103.
- Traditional RNNs and LSTMs struggle with long-term dependencies due to vanishing gradients; self-attention addresses this directly.

## Key Figures and Tables

- Table 5: Summary of 11 transformer architectures → key features and application areas (forecasting, segmentation, language modeling).
- Figure 4: Original Transformer with scaled dot-product attention → foundation for all reviewed variants.
- Figure 12: Autoformer architecture with decomposition and autocorrelation → enables 38% MSE reduction.
- Table 2: Comparison of modern approaches (LSTM, GRU, CNN, DeepAR, Prophet) → advantages and disadvantages.

## Key Equations

$$Attention(Q, K, V) = softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$
*Scaled dot-product attention—core mechanism weighting input relevance.*

$$Multihead(Q, K, V) = Concat(head_1, ..., head_h)W^O$$
*Multi-head attention—captures different relationship types in parallel.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LSTM | Long Short-Term Memory [think: RNN with forget gates to retain long sequences] |
| GRU | Gated Recurrent Unit—simpler than LSTM, fewer parameters |
| RNN | Recurrent Neural Network—processes sequences but suffers from vanishing gradients |
| ARIMA | Autoregressive Integrated Moving Average—classical statistical forecasting model |
| Transformer | Neural network using only self-attention, no recurrence or convolution |
| Self-attention | Mechanism that computes importance weights between all sequence positions |
| Positional encoding | Adds order information to input embeddings since attention is permutation-invariant |
| Autoformer | Transformer variant with built-in seasonal-trend decomposition and autocorrelation |
| FEDformer | Frequency Enhanced Decomposed Transformer using Fourier/wavelet transforms |
| Isolation Forest | Anomaly detection algorithm that isolates outliers via random partitioning |
| MSE | Mean Squared Error—forecasting accuracy metric (lower is better) |
| MAE | Mean Absolute Error—another accuracy metric |

## Critical Citations

- [Vaswani et al., 2017] — Original Transformer introducing self-attention; foundation for all reviewed architectures.
- [Box et al., 2015] — Classic Box-Jenkins ARIMA methodology; baseline for traditional forecasting.
- [Wu et al., 2022] — Autoformer paper demonstrating 38% MSE reduction via autocorrelation.
- [Zhou et al., 2022] — FEDformer with frequency enhancement achieving 14.8% MSE gain over Autoformer.

## Relevance to Odin

**Topics:**

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

E.2 — Anomaly Detection Algorithm

**Contribution to Odin:**

This review directly informs Odin's forecasting module by establishing that traditional LSTM models have fundamental limitations in capturing long-term dependencies—a critical requirement for spending patterns that include rare large purchases and seasonal fluctuations. The paper provides empirical benchmarks (e.g., 38% MSE reduction from Autoformer) that justify considering transformer-based alternatives, though computational trade-offs for mobile deployment must be weighed. Additionally, the review identifies Isolation Forest as a top-ranked anomaly detection algorithm for time series, supporting Odin's current candidate algorithm choice for the anomaly detection module.

**Directly justifies:**

- "Autoformer achieves 38% average MSE reduction over existing methods on energy, traffic, and weather forecasting benchmarks, demonstrating the superiority of transformer-based architectures for long-term time series."
- "Traditional RNNs and LSTMs have limited success modeling long-term context due to vanishing gradients, making them less suitable for spending time series where rare events (e.g., annual insurance payments) matter."
- "Isolation Forest is ranked among the top anomaly detection algorithms for time series data, alongside One-class SVM and autoencoders, supporting its selection for Odin's anomaly detection module."
- "Self-attention enables direct modeling of dependencies between distant time points without sequential recurrence, addressing a key weakness of LSTM for irregular spending patterns."
- "FEDformer's frequency-enhanced decomposition achieves over 20% MSE improvement on datasets without clear periodicity, relevant to variable-income user spending."

**Limits of relevance:**

- Review paper synthesizes existing results from healthcare, climate, and language domains; no personal finance or spending-specific benchmarks are provided.
- Computational complexity of transformers (O(L^2) in sequence length) may exceed mobile constraints; only Informer and Pyraformer address efficiency with O(L log L) attention.
- Findings are based on large-scale datasets (electricity, traffic, weather); applicability to sparse, user-level spending data in a cold-start scenario is unvalidated.
- No Filipino demographic or income typology data; spending behavior patterns may differ from the reviewed domains.

## Limitations

- Review paper does not provide original empirical comparisons; all performance claims are sourced from individual architecture papers. [unacknowledged]
- Focus on healthcare, climate, and language tasks; no dedicated section on personal finance or consumer spending time series.
- Computational resource requirements for transformer models are discussed only briefly, with no guidance for mobile or resource-constrained deployment.
- Anomaly detection coverage is limited to a single paragraph (Isolation Forest, One-class SVM); no evaluation of these methods on time series anomalies.
- Transformer-XL and CrossFormer++ are evaluated primarily on language and image tasks, not time series forecasting—applicability to financial sequences is indirect.

## Remember This

- 🔑 **38% MSE reduction** — Autoformer beats LSTMs on long-term benchmarks; self-attention is key.
- 📌 FEDformer adds frequency transforms for another 14.8% gain — consider hybrid time-frequency approaches.
- ⚠️ Traditional LSTM struggles with long-term context — Odin's forecasting may need transformer alternatives if spending shows rare spikes.
- 💡 Isolation Forest confirmed as top anomaly detector — supports Odin's current algorithm choice.
- 🧠 No mobile deployment data — transformer efficiency (O(L log L) variants like Informer) needs validation on phones.