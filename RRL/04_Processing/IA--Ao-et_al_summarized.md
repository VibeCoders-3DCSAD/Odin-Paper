```yaml
paper_id: 10.1109/ACCESS.2025.3602791
designation: international
title: A Review of Time Series Prediction Models Based on Deep Learning
authors: Ao, X.; Gong, Y.; He, A.
year: 2025
venue: IEEE Access
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 12.A
  - 12.B
shorthand_tags:
  - /spending-forecasting
  - /anomaly-detection
  - /model-evaluation
tldr: Reviews deep learning models for time series prediction, including CNNs, RNNs/LSTM/GRU, Transformers, GNNs, and hybrids, with a task-driven model selection framework.
problem_and_motivation: Traditional time series methods like ARIMA struggle with nonlinear, non-stationary, and seasonal real-world data. Deep learning offers powerful nonlinear modeling and automatic feature extraction, but existing surveys lack practical model selection guidelines, deep cross-comparisons, and systematic coverage of emerging challenges like interpretability and efficiency.
approach:
  - Systematically analyzes CNN-based models (TCN, SCINet, Kmeans-CNN) and their trade-offs in long-range dependency capture versus computational cost.
  - Reviews RNN family (vanilla RNN, LSTM, GRU) focusing on gating mechanisms that solve vanishing gradients for long sequences.
  - Examines Transformer variants (Informer, Autoformer, iTransformer, Conformer, Scaleformer, CrossFormer) with emphasis on self-attention complexity and efficiency innovations.
  - Covers Graph Neural Networks (GNNs) including spatial-temporal integrated methods (STGCN, MTGNN, HGCN-MA, STAN) for multivariate interdependencies.
  - Discusses hybrid models that combine deep learning with statistical methods (ARIMA-RNN, ETSformer, N-BEATS, PatchTST) and domain constraints.
  - Provides a comparative analysis across categories based on sequence length, multivariate support, interpretability, computational efficiency, and real-time performance.
  - Proposes a task-driven model selection framework mapping problem characteristics to optimal model classes.
  - Meta-analysis of cross-dataset trends identifying which architectures dominate under specific data conditions.
findings:
  - num: ARIMA-RNN hybrid achieved 15% MAE reduction on electricity load dataset compared to standalone models.
  - num: ETSformer reduced inference latency by 37% versus Autoformer on ETT data while maintaining accuracy.
  - num: PatchTST achieved 23% lower MSE than Informer with 60% less GPU memory consumption.
  - Transformer variants with ProbSparse attention (Informer) reduce time complexity from O(L^2) to O(L log L).
  - GNN-based models (STGCN, MTGNN) outperform channel-independent methods when strong spatial or relational dependencies exist between variables.
  - iTransformer inverts tokenization (variables as tokens, time points as features) for superior multivariate forecasting without predefined graphs.
  - Decomposition-based hybrids (Autoformer, N-BEATS) consistently top benchmarks for data with strong seasonality and trends.
key_figures_tables:
  - Figure 1: Structure of one-dimensional convolutional network → Basic CNN architecture for time series.
  - Figure 2: Structure of dilated causal convolution → TCN expands receptive field without increasing depth.
  - Figure 5: Structure of LSTM → Three-gate mechanism (forget, input, output) for long-term dependency capture.
  - Figure 7: Structure of Transformer → Encoder-decoder with multi-head self-attention and feed-forward networks.
  - Figure 12: Task-driven model selection framework → Maps sequence length, multivariate needs, and constraints to optimal model class.
  - Table 6: Comparative analysis of model categories → Summarizes strengths and limitations across CNN, RNN, Transformer, GNN, Hybrid.
key_equations:
  - equation: TCN = 1DFCN + causal convolutions
    explanation: TCN combines fully convolutional network with causality constraint.
definitions:
  - term: TCN
    definition: Temporal Convolutional Network using dilated causal convolutions and residual connections for sequence modeling.
  - term: LSTM
    definition: Long Short-Term Memory network with forget, input, and output gates to control information flow.
  - term: GRU
    definition: Gated Recurrent Unit merging LSTM's input and forget gates into an update gate.
  - term: ProbSparse Self-Attention
    definition: Attention mechanism reducing complexity from O(L^2) to O(L log L) by selecting dominant query-key pairs.
  - term: Auto-Correlation Mechanism
    definition: Replaces self-attention with period-based dependencies in Autoformer.
critical_citations:
  - "[Hochreiter & Schmidhuber, 1997] — Introduced LSTM gating to solve vanishing gradients."
  - "[Vaswani et al., 2017] — Transformer with self-attention enabling parallel sequence processing."
  - "[Zhou et al., 2021] — Informer with ProbSparse attention for long-sequence forecasting."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      justification: Surveys deep learning models for spending pattern prediction.
    - code: 6.B
      name: Spending Forecasting Algorithm
      justification: Compares LSTM, GRU, Transformer variants for long-sequence forecasting tasks.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      justification: Reviews CNN-based methods for ECG abnormality and power consumption anomalies.
    - code: 8.B
      name: Anomaly Detection Algorithm
      justification: Discusses Kmeans-CNN and TCN for detecting irregular patterns in time series.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      justification: Provides comparative analysis across model categories on multiple benchmarks.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: Proposes task-driven selection framework based on sequence length, latency, and dependencies.
  contribution: This review directly informs Odin's spending forecasting module by benchmarking LSTM, GRU, and Transformer variants on long-sequence prediction tasks. For anomaly detection, the survey identifies CNN-based models (TCN, Kmeans-CNN) as effective for irregular pattern detection. The task-driven selection framework provides a systematic evaluation methodology for Odin's algorithmic modules, matching problem characteristics (sequence length, real-time constraints) to optimal model classes. Hybrid models like ARIMA-RNN and PatchTST offer paths for balancing accuracy and computational efficiency in resource-constrained mobile environments.
  directly_justifies:
    - LSTM and GRU are suitable for long-sequence prediction tasks such as power load forecasting.
    - Gated Recurrent Units offer lower computational cost than LSTM with comparable performance.
    - Transformer variants like Informer achieve O(L log L) complexity for efficient long-sequence processing.
    - Decomposition-based hybrids (N-BEATS, Autoformer) excel when data contains strong seasonal and trend components.
    - TCN captures long-range dependencies using dilated convolutions without gradient issues.
  limits:
    - The review focuses on general time series prediction, not specifically on personal finance or spending data.
    - No empirical validation on Filipino young professional financial data. [unacknowledged]
    - Mobile-first constraints (latency, memory, battery) are mentioned but not deeply evaluated for each model. [unacknowledged]
    - User trust and data privacy implications of deep learning models are not discussed. [unacknowledged]
  mapping_rationale: The paper was screened against Odin's functional domains. Spending forecasting (domains 6.A, 6.B) is directly supported by extensive coverage of RNNs, Transformers, and hybrid models for long-sequence prediction. Anomaly detection (8.A, 8.B) is supported by CNN variants (TCN, Kmeans-CNN) applied to irregular pattern detection. System evaluation (12.A, 12.B) maps to the paper's comparative analysis and task-driven selection framework. Topics related to behavioral profiling (5.A-C), budget recommendation (7.A-C), mobile UX (9.A-B), data privacy (10.A-B), retention (11.A-B), and savings/debt (13.A-B) were rejected because the paper does not address these domains. The paper's international designation is appropriate as it is not authored by a Philippine institution.
limitations:
  - The paper is a survey, not an empirical study; claims about model performance are aggregated from cited primary research.
  - Comparative tables lack statistical significance testing across different datasets. [unacknowledged]
  - Real-time performance metrics are discussed qualitatively without standardized benchmarks. [unacknowledged]
remember_this:
  - LSTM and GRU solve vanishing gradients for medium-length sequence forecasting.
  - Transformer variants achieve O(L log L) complexity for sequences over 1000 steps.
  - PatchTST reduces GPU memory by 60% via sub-series tokenization.
  - Hybrid models combine statistical decomposition with deep learning for interpretability.
  - GNNs outperform other methods when variables have strong spatial or relational dependencies.
```