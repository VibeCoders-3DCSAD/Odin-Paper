# A comprehensive survey of deep learning for time series forecasting: architectural diversity and open challenges

## Metadata

```yaml
---
paper_id: "10.1007/s10462-025-11223-9"
designation: international
title: "A comprehensive survey of deep learning for time series forecasting: architectural diversity and open challenges"
authors: "Kim, J.; Kim, H.; Kim, H.; Lee, D.; Yoon, S."
year: 2025
venue: "Artificial Intelligence Review"
odin_topics: ["4.A", "5.C", "6.A", "6.B", "8.A", "8.B", "12.B"]
shorthand_tags: ["/forecasting-methods-survey", "/forecast-algo-candidates", "/forecast-algo-comparison", "/anomaly-ml-families", "/anomaly-algo-candidates", "/classification-vs-clustering", "/eval-ml-design"]
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

Time series forecasting has entered a renaissance of architectural diversity, with simple linear models outperforming Transformers on long sequences while Mamba, diffusion, and foundation models rapidly emerge as competitive alternatives.

## Problem and Motivation

Time series forecasting drives decisions in finance, supply chains, and healthcare, but diverse data patterns and domain specificity limit model generalizability. Hidden patterns, channel correlations, and distribution shifts make accurate prediction fundamentally challenging. Prior surveys lacked systematic comparisons across newly emerging architectures (Mamba, diffusion, foundation models) and did not comprehensively address open challenges like causality and feature extraction.

## Approach

- Scope: Surveys deep learning models for time series forecasting from statistical methods (ARIMA) through fundamental DL (MLP, RNN, CNN, GNN) to Transformers and post-Transformer architectures.
- Architecture categories: MLP-based (N-BEATS, TSMixer, FreTS), CNN-based (TimesNet, ModernTCN), RNN-based (LSTM, GRU variants), GNN-based (MSGNet, ForecastGrapher), and hybrid models.
- Transformer improvements: patching techniques (PatchTST), cross-dimension attention (iTransformer, Crossformer), exogenous variable integration (TimeXer), and multi-scale frameworks.
- Emerging architectures: diffusion models (TimeGrad, CSDI, Diffusion-TS), Mamba (S-Mamba, TimeMachine, Bi-Mamba+), and foundation models (Lag-Llama, TimesFM, Chronos).
- Open challenges examined: channel dependency (CI vs CD strategies), distribution shift alleviation (RevIN, Dish-TS), causality integration, feature extraction (decomposition, multi-scale, frequency domain), model combination (ensemble, hybrid), interpretability (TFT, SHAP, LIME), and spatio-temporal forecasting.

## Findings

1. LTSF-Linear (a simple MLP) **outperformed Transformer-based models** on long-term forecasting by preserving time-ordering information that attention mechanisms lose.
2. Patching (e.g., PatchTST) restored Transformer superiority over linear models by grouping time points into semantic patches, achieving better performance with longer look-back windows.
3. Channel-independent (CI) strategies often beat channel-dependent (CD) on benchmark datasets due to CI's robustness to distribution shifts, not inherent superiority.
4. Mamba-based models (e.g., S-Mamba, TimeMachine) achieve state-of-the-art results with linear time complexity, overcoming Transformer's quadratic scaling on long sequences.

- Diffusion models excel at probabilistic forecasting by modeling uncertainty through forward/backward noise processes, offering prediction intervals.
- SSMs (state space models) like S4 and Mamba provide efficient long-sequence modeling by compressing essential information into hidden states.

## Key Figures and Tables

- Figure 3: Evolution of TSF models → from statistical to Transformer to renaissance of diverse architectures.
- Figure 4: Overview of open challenges → channel correlation, distribution shift, causality, feature extraction, interpretability.
- Figure 9: Full vs sparse self-attention patterns → sparse attention reduces O(L²) to O(L log L) but risks information loss.
- Table 5: Transformer taxonomy for TSF → patching, cross-dimension, multi-scale, decoder-only approaches.
- Table 6: Comparison of deep learning backbones → MLP (simple, fast), CNN (local patterns), RNN (sequential), Transformer (global attention), Mamba (efficient long-range).

## Key Equations

$$ˆx_{t+1:t+h} = f(x_{t-p:t})$$
*Univariate forecasting uses past p+1 steps to predict next h values.*

$$ˆX_{t+1:t+h} = f(X_{t-p:t})$$
*Multivariate forecasting extends to vectors of multiple variables.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| TSF | Time series forecasting — predicting future values from historical sequential data. |
| CI / CD | Channel independent (treat each variable separately) vs channel dependent (model variable interactions). |
| LSTM [think: memory cell with forget gate] | Long Short-Term Memory — RNN variant that remembers long sequences via gated cells. |
| SSM | State space model — mathematical framework compressing dynamic system state over time. |
| MAE / MSE | Mean Absolute Error / Mean Squared Error — common forecast error metrics. |
| CRPS | Continuous Ranked Probability Score — evaluates probabilistic forecast distributions. |
| FFT | Fast Fourier Transform — converts time series to frequency domain to reveal periodic patterns. |
| EMD | Empirical Mode Decomposition — non-linear method separating signals into intrinsic modes. |

## Critical Citations

- [Vaswani et al., 2017] — Introduced Transformer with self-attention, foundation for modern TSF architectures.
- [Hochreiter & Schmidhuber, 1997] — LSTM solved vanishing gradient, enabling long-sequence learning in RNNs.
- [Zeng et al., 2023] — LTSF-Linear showed simple linear models can beat Transformers, triggering architecture renaissance.
- [Gu & Dao, 2024] — Mamba introduced selective SSM, achieving linear-time sequence modeling competitive with Transformers.
- [Box et al., 1970] — ARIMA formalized statistical time series forecasting, still a baseline benchmark.

## Relevance to Odin

**Topics:**

4.A — Landscape of Existing Personal Finance Systems

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This survey directly informs Odin's forecasting module design by systematically comparing candidate architectures (LSTM, GRU, TCN, Transformer, Mamba, linear models) and their trade-offs (accuracy, complexity, data requirements). The finding that linear models can outperform Transformers on long sequences justifies evaluating lightweight MLP-based forecasting for Odin's mobile-first constraints. The detailed analysis of channel strategies (CI vs CD) and distribution shift alleviation methods (RevIN, Dish-TS) provides actionable guidance for Odin's cold-start profiling and anomaly detection under changing user behavior.

**Directly justifies:**

- "LTSF-Linear demonstrated that a single linear layer can outperform Transformer-based models on long-term forecasting by preserving time-ordering information, challenging the assumption that attention mechanisms are universally superior for time series."
- "Patching techniques (e.g., PatchTST) enable Transformers to capture locality and achieve state-of-the-art performance by grouping time points into semantic patches of 16–64 points."
- "Channel-independent (CI) strategies show greater robustness to distribution shifts than channel-dependent (CD) strategies, explaining why CI often beats CD on benchmark datasets despite CD's intuitive appeal."
- "RevIN (Reversible Instance Normalization) provides a model-agnostic normalization-denormalization framework that mitigates distribution shift in time series forecasting with minimal computational overhead."
- "Mamba achieves linear time and memory complexity while matching or exceeding Transformer performance on long sequences, making it suitable for resource-constrained mobile deployment."

**Limits of relevance:**

- Survey focuses on general TSF, not personal finance specifically; applicability to Odin's spending forecasting requires validation on financial transaction data.
- Most benchmark datasets (electricity, traffic, weather) differ from individual spending patterns in volatility and sparsity.
- Foundation models (Lag-Llama, TimesFM) require massive pre-training corpora unavailable for Philippine personal finance; zero-shot transfer may be unreliable.
- Mobile deployment constraints (battery, latency, offline operation) are mentioned but not empirically evaluated for any architecture.

## Limitations

- Survey excludes detailed theoretical derivations; researchers must consult original papers for mathematical rigor.
- Performance comparisons across architectures rely on reported benchmark results, which may vary with dataset characteristics and hyperparameter choices. [unacknowledged]
- No empirical validation of any architecture on financial transaction data; domain-specific performance is inferred.
- Mamba and diffusion models are very recent; long-term stability and generalization across diverse time series types are not yet established. [unacknowledged]
- Foundation models for time series are still nascent; current approaches (LLM reprogramming, pre-training) have not demonstrated reliable zero-shot forecasting on small or domain-specific datasets.

## Remember This

- 🔑 **LTSF-Linear beat Transformers** — simple linear models preserve time order better than attention.
- 📌 Patching rescues Transformers — grouping 64 time points restores locality and SOTA performance.
- 💡 CI wins on noisy data — channel independence is robust to distribution shifts, not inherently better.
- 🧠 Mamba offers linear-time long sequences — selective SSM matches Transformer quality with O(L) complexity.
- ⚠️ No financial validation — all findings are from electricity, traffic, weather, not personal spending.
