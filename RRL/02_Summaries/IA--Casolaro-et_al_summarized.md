```yaml
paper_id: 10.3390/info14110598
designation: international
title: Deep Learning for Time Series Forecasting: Advances and Open Problems
authors: Casolaro, A.; Capone, V.; Iannuzzo, G.; Camastra, F.
year: 2023
venue: Information
odin_topics:
  - 6.A
  - 6.B
  - 12.A
  - 12.B
shorthand_tags:
  - /forecasting-models
  - /spending-prediction
  - /evaluation-frameworks
  - /algorithm-evaluation
tldr: Reviews deep learning architectures for time series forecasting, covering CNNs, RNNs, GNNs, Transformers, and generative models with benchmarks for short-term and long-term prediction.
problem_and_motivation: Existing surveys on deep learning for time series forecasting lack coverage of recent architectures like Transformers and diffusion models, and do not distinguish between short-term and long-term forecasting. This gap limits practitioners' ability to select appropriate models for different prediction horizons. The paper provides a comprehensive review to address these shortcomings.
approach:
  - Reviews literature from 2016 onward, focusing on deep learning for time series forecasting.
  - Covers CNNs, TCNs, RNNs (ESN, LSTM, GRU), GNNs, Deep Gaussian Processes, GANs, and diffusion models for short-term forecasting.
  - Covers Transformer and its variants (LogTrans, Informer, Autoformer, FEDformer, etc.) for long-term forecasting.
  - Presents benchmark datasets for short-term (M4) and long-term (ETT, Traffic, Weather, etc.) forecasting.
  - Compares performance of Transformer variants using MSE/MAE metrics across multiple prediction lengths.
findings:
  - "num: Transformer variants like PatchTST achieve MSE of 0.149 on Weather dataset for 96-step prediction, outperforming LSTM and TCN."
  - "num: Autoformer and FEDformer show lower MSE than Informer and LogTrans on most long-term benchmarks."
  - Deep Gaussian Processes can provide confidence intervals, unlike other deep learning methods.
  - Transformers face memory bottleneck (O(L^2) complexity) and local agnosticism.
  - Open problems include uncertainty estimation, overfitting, need for long time series, and concept drift.
key_figures_tables:
  - "Table 13: Multivariate long-term forecasting benchmarks → Crossformer and PatchTST generally achieve lowest MSE across datasets."
  - "Figure 6: LSTM cell architecture with input, forget, output gates → Gating mechanisms control information flow to capture long-term dependencies."
  - "Figure 10: Transformer encoder-decoder with attention → Attention replaces recurrence to enable parallelization and long-range dependency capture."
key_equations:
  - equation: "x_{t+p} = f(x_{t-1},...,x_{t-q}) + \\epsilon_{t+p}"
    explanation: "Defines time series forecasting as function of past q samples."
  - equation: "\\text{Attention}(Q,K,V) = \\text{softmax}\\left(\\frac{QK^\\top}{\\sqrt{D_k}}\\right)V"
    explanation: "Scaled dot-product attention computes weighted sum of values."
definitions:
  - term: TCN
    definition: "Temporal Convolutional Network using causal and dilated convolutions for sequence modeling."
  - term: LSTM
    definition: "Long Short-Term Memory network with gating mechanisms to avoid vanishing gradients."
  - term: Transformer
    definition: "Architecture relying solely on attention mechanisms without recurrence."
  - term: DDPM
    definition: "Denoising Diffusion Probabilistic Model using forward noise injection and reverse denoising."
critical_citations:
  - "[Vaswani et al., 2017] — Introduced Transformer architecture foundational to long-term forecasting."
  - "[Hochreiter & Schmidhuber, 1997] — LSTM cell addressing vanishing gradient problem."
  - "[Makridakis et al., 2020] — M4 competition benchmark for short-term forecasting."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      justification: "Reviews deep learning models directly applicable to spending forecasting."
    - code: 6.B
      name: Spending Forecasting Algorithm
      justification: "Provides algorithms (LSTM, TCN, Transformer) for time series prediction."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      justification: "Discusses benchmark datasets and metrics for forecasting evaluation."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: "Comparative tables (Table 13) evaluate multiple forecasting algorithms."
  contribution: "This review informs Odin's spending forecasting module by providing a taxonomy of deep learning models suitable for short-term and long-term prediction. The comparative benchmarks (Table 13) directly support algorithm selection for Odin's forecasting engine. The discussion of open problems (uncertainty estimation, concept drift) guides Odin's design choices for robustness. The survey's coverage of attention mechanisms and Transformer variants offers pathways for handling irregular spending patterns."
  directly_justifies:
    - "LSTM and GRU networks effectively capture temporal dependencies in spending data (Casolaro et al., 2023)."
    - "Transformer-based models achieve superior long-term forecasting accuracy on multivariate time series benchmarks."
    - "Deep Gaussian Processes can provide prediction intervals, addressing uncertainty in spending forecasts."
    - "Benchmark datasets like M4 and ETT enable systematic evaluation of forecasting algorithms."
  limits:
    - "The paper is a general survey, not specific to personal finance or Filipino young professionals."
    - "No empirical validation on actual spending data."
    - "Focuses on accuracy metrics, not on interpretability or computational efficiency for mobile deployment. [unacknowledged]"
  mapping_rationale: "The paper was screened against Odin's functional domains. Spending forecasting (domains 6.A, 6.B) is the primary match, as the entire paper reviews time series forecasting architectures applicable to predicting user spending. The benchmark discussion (Section 6) aligns with system evaluation (domains 12.A, 12.B), providing evidence for evaluating forecasting modules. Behavioral profiling (5.A, etc.) and anomaly detection (8.A, 8.B) were considered but rejected because the paper does not address user profiling or anomaly detection algorithms specifically for personal finance; its anomaly mentions are generic. Mobile-first design (9) and data privacy (10) are absent. Thus topics 6.A, 6.B, 12.A, 12.B were selected."
limitations:
  - "Assumes time series stationarity, concept drift remains an open problem. [unacknowledged]"
  - "Deep learning models require long time series to estimate millions of parameters."
  - "Most methods cannot estimate prediction confidence intervals except Deep Gaussian Processes."
  - "Overfitting risk increases with model complexity."
remember_this:
  - "PatchTST achieves 0.149 MSE on Weather 96-step forecasting."
  - "Transformers reduce complexity but suffer from local agnosticism."
  - "Deep Gaussian Processes uniquely provide uncertainty intervals."
  - "LSTM and GRU remain strong for short-term forecasting."
```