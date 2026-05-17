# Deep learning modelling techniques: current progress, applications, advantages, and challenges

## Metadata

```yaml
---
paper_id: "10.1007/s10462-023-10466-8"
designation: international
title: "Deep learning modelling techniques: current progress, applications, advantages, and challenges"
authors: "Ahmed, S. F.; Alam, M. S. B.; Hassan, M.; Rozbu, M. R.; Ishtiak, T.; Rafa, N.; Mofijur, M.; Ali, A. B. M. S.; Gandomi, A. H."
year: 2023
venue: "Artificial Intelligence Review"
odin_topics: ["5.C", "6.A", "6.B", "8.A", "8.B", "12.B"]
shorthand_tags: ["/forecasting-methods-survey", "/forecast-algo-candidates", "/forecast-algo-comparison", "/classifier-candidates", "/classifier-eval-metrics", "/anomaly-algo-candidates", "/anomaly-eval-metrics", "/eval-ml-design"]
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

Deep learning models automatically learn hierarchical features from raw data, outperforming traditional ML on large datasets but requiring substantial computational resources and training samples.

## Problem and Motivation

Conventional machine learning methods cannot efficiently process raw data and require manual feature engineering, limiting their scalability with big data. Deep learning overcomes this by using multiple nonlinear transformation layers to extract increasingly abstract features directly from input. Prior surveys focused on narrow application domains, leaving a gap in comprehensive reviews of the full range of DL architectures.

## Approach

- Systematic literature review using Scopus and refereed journals from major publishers (Elsevier, Springer, Nature, etc.).
- Search keywords included “Deep learning”, “Deep learning architecture”, and specific model names (CNN, RNN, LSTM, GAN, etc.).
- Inclusion criteria: peer-reviewed academic articles pertinent to DL modelling techniques.
- Final selection: 419 articles after applying exclusion criteria (e.g., insufficient references, high repetition).
- Comparative analysis based on strengths, weaknesses, and performance metrics (accuracy, complexity).

## Findings

1. **CNN** achieves high image recognition accuracy but requires large labeled datasets and is susceptible to poor labeling.
2. **BiLSTM** outperforms standard LSTM by **37.78%** in time series forecasting accuracy (Siami-Namini et al., 2019).
3. **GenInSAR** (CNN-based) reduced total residue by **>16.5%** compared to alternative InSAR methods.
4. **RNN-LSTM** achieved lower RMSE (0.487) than traditional RNN (0.516) and naive models (0.793) for low-flow prediction.

- Hybrid conventional DL architectures (e.g., CNN-LSTM) are more robust than standalone models.
- Deep learning is susceptible to deception, misclassification, and local minima, limiting online-mode suitability.

## Key Figures and Tables

- Table 2: Summary of 20+ DL models with applications, outcomes → wide domain specificity; no one-size-fits-all.
- Table 3: Advantages and challenges of DL models → key trade-offs: automatic feature extraction vs. high compute cost.
- Table 4: Performance vs. complexity comparison (CNN, RNN, LSTM, BiLSTM, AE) → BiLSTM high accuracy, medium–high complexity.

## Key Equations

$$f^{k}_{l}(p,q) = \sum_{c} \sum_{x,y} i_{c}(x,y) \odot e^{k}_{l}(u,v)$$
*CNN convolution: kernel slides over input to produce feature maps.*

$$i_t = \sigma(W^i x_t + U^i h_{t-1} + b^i),\quad f_t = \sigma(W^f x_t + U^f h_{t-1} + b^f),\quad o_t = \sigma(W^o x_t + U^o h_{t-1} + b^o)$$
*LSTM gates control information flow: input, forget, output.*

$$z = \sigma(W_z h_{t-1} + U_z x_t),\quad r = \sigma(W_r h_{t-1} + U_r x_t),\quad h_t = (z \otimes c) \otimes ((1-z) \otimes h_{t-1})$$
*GRU update and reset gates address vanishing gradient in RNNs.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| DL | Deep learning – multi-layer neural networks that learn hierarchical features. |
| ML | Machine learning – algorithms that improve with experience without explicit programming. |
| CNN | Convolutional neural network – uses convolution kernels to extract spatial features from images. |
| RNN | Recurrent neural network – processes sequences by maintaining a hidden state (memory). |
| LSTM | Long short-term memory [think: memory cell with forget/input/output gates to control long-term dependencies]. |
| GRU | Gated recurrent unit – simpler than LSTM with update and reset gates. |
| BiLSTM | Bidirectional LSTM – processes sequences forward and backward, capturing context from both directions. |
| GAN | Generative adversarial network – two networks (generator, discriminator) compete to produce realistic synthetic data. |
| AE | Autoencoder – compresses input to lower dimension and reconstructs it, learning efficient representations. |
| DBN | Deep belief network – stack of restricted Boltzmann machines for unsupervised feature learning. |
| CapsNet | Capsule neural network – preserves spatial hierarchies and part-whole relationships. |
| ReLU | Rectified Linear Unit – activation function $f(x)=\max(0,x)$, avoids vanishing gradient. |

## Critical Citations

- [Goodfellow et al., 2014] — Introduced generative adversarial networks (GANs), enabling realistic synthetic data generation.
- [Lecun et al., 2015] — Seminal Nature survey defining deep learning as representation learning with multiple abstraction levels.
- [Schmidhuber, 2015] — Comprehensive overview of deep neural network history and architectures.
- [Siami-Namini et al., 2019] — Empirical comparison showing BiLSTM outperforms LSTM by 37.78% in time series forecasting.

## Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper provides a systematic survey of deep learning architectures, enabling Odin’s team to make informed algorithm selections for its forecasting, classification, and anomaly detection modules. The finding that RNN-based models (LSTM, GRU) excel at time series forecasting directly supports Odin’s spending forecasting module design, while the comparative complexity analysis (Table 4) guides mobile-first implementation trade-offs. Although domain-agnostic, the paper’s performance benchmarks and identified limitations (e.g., cold-start data requirements) inform RRL arguments for choosing lightweight, unsupervised, or hybrid models suited to Odin’s manual-input, low-user-history context.

**Directly justifies:**

- “LSTM and GRU outperform traditional RNNs on time series forecasting by mitigating vanishing gradients, with BiLSTM achieving up to 37.78% higher accuracy on sequential data.”
- “Deep learning models automatically generate features from raw data, reducing hand-tuning requirements for transaction categorization in personal finance systems.”
- “Training deep learning models requires large labeled datasets and high computational resources – a key limitation for cold-start user profiles in Odin, favoring unsupervised or lightweight approaches.”
- “Hybrid architectures (e.g., CNN-LSTM) are more robust than standalone models, suggesting Odin’s modules may benefit from combining feature extraction and sequential modeling.”
- “Generative models (GANs, autoencoders) can detect anomalies without labeled training data, applicable to Odin’s anomalous spending detection under sparse user history.”

**Limits of relevance:**

- The paper is a general survey of DL techniques; no experiments on personal finance or transaction data.
- Performance comparisons (e.g., accuracy percentages) come from non-financial domains (image, speech, medical), not directly transferable to spending forecasting.
- The review does not address algorithm performance on irregular, manual-transaction data typical of Odin (no API integration).
- No discussion of culturally specific financial patterns or Filipino demographic context.

## Limitations

- Survey methodology relies on existing literature; no original empirical validation of any DL model.
- Computational complexity analysis is qualitative (Low/Medium/High) without hardware-specific benchmarks. [unacknowledged]
- The paper does not address online learning or incremental model updates, which are relevant to dynamic user behavior in Odin. [unacknowledged]
- Many cited performance metrics are from studies with different evaluation protocols, limiting direct comparability.
- No discussion of privacy-preserving machine learning techniques, a concern for financial apps under RA 10173. [unacknowledged]

## Remember This

- 🔑 **BiLSTM beats LSTM by 37.78%** in time series forecasting – strong candidate for Odin’s spending prediction.
- 💡 Hybrid models (CNN-LSTM) are more robust than single architectures – consider for multi-module tasks.
- ⚠️ DL needs large labeled datasets – cold-start profiles in Odim require unsupervised or lightweight alternatives.
- 🔍 Autoencoders and GANs detect anomalies without labels – useful for Odin’s anomaly detection module.
- 📌 No one-size-fits-all DL model – selection must balance accuracy, complexity, and domain specificity.
