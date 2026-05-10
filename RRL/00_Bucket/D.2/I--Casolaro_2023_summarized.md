# Deep Learning for Time Series Forecasting: Advances and Open Problems

## Metadata

```yaml
---
paper_id: "10.3390/info14110598"
designation: international
title: "Deep Learning for Time Series Forecasting: Advances and Open Problems"
authors: "Casolaro, A.; Capone, V.; Iannuzzo, G.; Camastra, F."
year: 2023
venue: "Information"
odin_topics: ["D.1", "D.2"]
shorthand_tags: ["/forecasting-methods", "/temporal-dependency", "/lstm-architecture", "/lstm-vs-alternatives", "/lstm-justification"]
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

This review surveys deep learning architectures for time series forecasting, covering recent advances in GNNs, DGPs, GANs, diffusion models, and Transformers, while identifying four open problems including uncertainty estimation and concept drift.

## Problem and Motivation

Existing reviews of deep learning for time series forecasting lack coverage of recent architectures such as Transformers, Graph Neural Networks, and diffusion models, and do not clearly distinguish between short-term and long-term forecasting. This gap matters because practitioners need up-to-date guidance on which architectures work best for different prediction horizons. Prior surveys also omitted benchmarking recommendations and open problems specific to each architecture.

## Approach

- Literature review focusing on works published since 2016, covering deterministic time series foundations.
- Short-term forecasting architectures: CNNs, TCNs, RNNs (Elman, ESN, LSTM, GRU), GNNs, DGPs, GANs, diffusion models.
- Long-term forecasting architectures: Transformer and its variants (LogTrans, Informer, Autoformer, FEDformer, Pyraformer, Triformer, Non-stationary, PatchTST, Crossformer, Scaleformer).
- Hybrid models combining CNNs, LSTMs, attention mechanisms, and fuzzy logic.
- Benchmarks: M4 (100,000 time series) for short-term; nine multivariate datasets (ETT, Electricity, Traffic, Weather, Exchange, ILI) for long-term.
- Complexity analysis: Transformers have O(L²) time/space; variants reduce to linear via sparse or low-rank attention.

## Findings

- **Table 13 shows Crossformer achieves MSE of 0.173 on ETTm2 (96-step forecast), the lowest among all evaluated Transformer variants.**
- Informer and LogTrans reduce Transformer complexity via sparse attention, but often underperform simpler models like PatchTST.
- LSTM and GRU solve vanishing gradients via gating mechanisms but suffer from short-term memory for very long sequences.
- Deep Gaussian Processes (DGPs) uniquely provide prediction confidence intervals; other deep learning methods lack uncertainty estimates.
- GANs and diffusion models are effective for data augmentation and end-to-end forecasting; TimeGrad and ScoreGrad set benchmarks for probabilistic forecasting.
- Open problems: no uncertainty quantification (except DGPs), overfitting risk, need for long training series, and concept drift under non-stationarity.

## Key Figures and Tables

- Figure 6: LSTM cell architecture with input, forget, output gates → gates control information flow to prevent vanishing gradients.
- Figure 10: Transformer encoder-decoder with self-attention and cross-attention → attention enables parallel processing and long-range dependencies.
- Table 13: Multivariate long-term benchmark results (MSE/MAE) on ETTm1/2, ETTh1/2, Electricity, Traffic, Weather, Exchange, ILI → Crossformer and PatchTST dominate most datasets.
- Table 5: LSTM applications across stock, load, traffic, health, energy (2016–2023) → LSTM is the most widely applied recurrent architecture.
- Table 12: Transformer variants for time series (2019–2023) → rapid innovation in attention mechanisms, decomposition, and channel independence.

## Key Equations

$$x_{t+p} = f(x_{t-1}, \dots, x_{t-q}) + \epsilon_{t+p} \quad \forall p \in [0, P]$$
*Autoregressive model uses past q samples to predict up to P steps ahead.*

$$y(t) = \sum_{a=1}^{q} w(a) X(t - d \cdot a)$$
*Dilated causal 1D convolution: kernel skips d steps to enlarge receptive field without increasing layers.*

$$\vec{h}_t = g(V\vec{x}_t + W\vec{h}_{t-1} + \vec{b})$$
*Vanilla RNN cell: current hidden state depends on input and previous state.*

$$\vec{c}_t = \vec{g}_t \odot \vec{i}_t + \vec{f}_t \odot \vec{c}_{t-1}, \quad \vec{h}_t = \vec{o}_t \odot \tanh(\vec{c}_t)$$
*LSTM cell: input, forget, output gates update cell state and hidden state, preventing gradient issues.*

$$\text{Attention}(K,V,Q) = \text{softmax}\left(\frac{QK^\top}{\sqrt{D_k}}\right)V$$
*Scaled dot-product attention: queries match keys to weight values, core of Transformer parallel processing.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LSTM | Long Short-Term Memory [think: forget gate decides what to discard, input gate what to add, output gate what to expose] |
| GRU | Gated Recurrent Unit [simpler than LSTM: uses update and reset gates] |
| TCN | Temporal Convolutional Network [1D CNN with causal + dilated convolutions for sequential data] |
| GNN | Graph Neural Network [models relationships between variables via adjacency matrix; aggregate and combine neighbors] |
| DGP | Deep Gaussian Process [Bayesian model that outputs mean and variance (uncertainty)] |
| GAN | Generative Adversarial Network [generator vs discriminator; used for time series augmentation or end-to-end forecasting] |
| DDPM | Denoising Diffusion Probabilistic Model [gradually adds noise then learns to reverse; TimeGrad uses this] |
| SDE | Stochastic Differential Equation [continuous diffusion process; unifies DDPM and score-based models] |
| RNN | Recurrent Neural Network [processes sequences one step at a time; suffers vanishing gradients] |
| ESN | Echo State Network [fixed random recurrent weights, no backpropagation through time] |

## Critical Citations

- [Hochreiter & Schmidhuber, 1997] — Original LSTM paper; all gated recurrent architectures derive from this.
- [Vaswani et al., 2017] — Transformer architecture “Attention is All You Need”; foundation of long-term forecasting.
- [Goodfellow et al., 2014] — Generative Adversarial Networks; basis for GAN-based time series generation and forecasting.
- [Song et al., 2020] — Score-based generative modeling via SDEs; unified framework for diffusion models.

## Relevance to Odin

**Topics:**

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

**Contribution to Odin:**

This comprehensive review directly supports Odin’s spending forecasting module by systematically comparing deep learning architectures suitable for sequential spending data. The paper’s detailed explanation of LSTM’s gating mechanisms (Section 3.2.4) justifies why LSTM is preferred over vanilla RNNs or GRUs for capturing irregular spending patterns with long-term dependencies. Benchmark results on multivariate time series (Table 13) provide a performance reference for algorithm selection, even though the domains differ from personal finance. The review also highlights the short-term memory limitation of standard RNNs (Section 3.2.6), reinforcing the necessity of LSTM’s cell state to retain information across spending cycles.

**Directly justifies:**

- “LSTM uses input, forget, and output gates to control information flow, solving the vanishing gradient problem that plagues vanilla RNNs (Section 3.2.4).”
- “On the ETTm2 electricity transformer dataset (15-minute resolution), Crossformer achieved MSE of 0.173 for 96-step ahead forecasting, outperforming Informer (0.615) and Autoformer (0.490) (Table 13).”
- “Transformers have O(L²) time and space complexity, limiting their application to long-sequence forecasting without sparse attention variants (Section 4.1.3).”
- “Deep Gaussian Processes are the only reviewed deep learning method capable of providing prediction confidence intervals; all other architectures lack uncertainty estimates (Section 7).”
- “Recurrent networks have inherent short-term memory: information about an input from 40 steps earlier may be lost after many recurrent steps (Section 3.2.6).”

**Limits of relevance:**

- The review is methodological and domain-agnostic; no empirical results on personal spending data or Filipino financial behavior.
- All benchmark datasets are from electricity, traffic, weather, and finance (exchange rates), not from consumer budgeting.
- No comparison of LSTM against statistical baselines (e.g., ARIMA) specifically for spending forecasting.
- The review does not address mobile-specific constraints (e.g., battery, inference latency) relevant to Odin’s deployment.

## Limitations

- Review excludes anomaly detection algorithms (Isolation Forest, rule-based) and classification methods for user profiling — only forecasting is covered. [unacknowledged]
- No discussion of cold-start forecasting scenarios where little or no user history exists. [unacknowledged]
- The paper itself does not conduct original experiments; all comparisons are compiled from prior work, limiting direct reproducibility.
- Acknowledges overfitting risk and need for long training series (Section 7), which is problematic for sparse individual spending data.
- Concept drift (non-stationarity) is noted as an open problem, but no mitigation strategies are proposed (Section 7).

## Remember This

- 🔑 **Crossformer MSE 0.173** on ETTm2 (96-step) – benchmark for multivariate forecasting.
- 📌 LSTM gates prevent vanishing gradients – essential for spending sequences with gaps.
- 💡 Only Deep Gaussian Processes output confidence intervals – all other deep models are point forecasts.
- ⚠️ Transformers need O(L²) memory – variants like Informer cut complexity to O(L log L).
- 🧠 Four open problems: no uncertainty, overfitting, long series needed, concept drift – all apply to Odin.