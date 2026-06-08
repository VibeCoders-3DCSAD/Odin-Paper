```yaml
paper_id: 10.1007/s10462-025-11223-9
designation: international
title: A comprehensive survey of deep learning for time series forecasting: architectural diversity and open challenges
authors: Kim, J.; Kim, H.; Kim, H.; Lee, D.; Yoon, S.
year: 2025
venue: Artificial Intelligence Review
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
  - /evaluation-frameworks
tldr: A comprehensive survey of deep learning for time series forecasting covering MLPs, CNNs, RNNs, GNNs, Transformers, diffusion models, foundation models, and Mamba, with analysis of open challenges.
problem_and_motivation: Time series forecasting is critical for decision-making but faces challenges from data diversity and complexity. Existing surveys lack comprehensive coverage of recent architectural diversification and open challenges. This survey provides a timely synthesis of model evolution and persistent problems.
approach:
  - Reviewed over 200 papers from top AI conferences and arXiv preprints.
  - Categorized models by architecture: statistical, ML, fundamental DL, Transformer, non-Transformer, diffusion, foundation, Mamba.
  - Analyzed open challenges: channel dependency, distribution shift, causality, feature extraction, interpretability, and spatio-temporal forecasting.
  - Provided taxonomy tables (e.g., Table 5, Table 7, Table 9, Table 10) and comparative analysis.
findings:
  - The number of top-tier AI conference papers on time series forecasting has exploded in recent years.
  - num: Simple linear models (LTSF-Linear) can outperform Transformers on long-term forecasting.
  - Patching technique (PatchTST) enables Transformers to achieve state-of-the-art by preserving locality.
  - Channel independence (CI) strategy shows greater robustness to distribution shift than channel dependence (CD).
  - Mamba-based models offer linear-time complexity and selective memory, challenging Transformer hegemony.
  - Diffusion models enable probabilistic forecasting by modeling uncertainty through conditional generation.
key_figures_tables:
  - Figure 2: Number of TSF papers at top AI/ML conferences → Explosive growth over time.
  - Figure 3: Evolution of TSF models from statistical to Transformer to diverse architectures → Renaissance in modeling.
  - Table 5: Taxonomy of Transformer improvements (patching, cross-dimension, exogenous variables) → Key techniques.
  - Table 10: Taxonomy of Mamba models for TSF → Emerging architecture with channel correlation learning.
key_equations:
  - equation: "\\hat{x}_{t+1:t+h} = f(x_{t-p:t})"
    explanation: Univariate forecasting using past p+1 steps.
  - equation: "\\hat{X}_{t+1:t+h} = f(X_{t-p:t})"
    explanation: Multivariate forecasting with vector inputs.
definitions:
  - term: TSF
    definition: Time series forecasting, predicting future values from sequential historical data.
  - term: LTSF
    definition: Long-term time series forecasting with horizons of months or years.
  - term: MTSF
    definition: Multivariate time series forecasting using multiple variables simultaneously.
  - term: CI
    definition: Channel independent strategy, treating each variable separately.
  - term: CD
    definition: Channel dependent strategy, modeling inter-variable correlations.
  - term: SSM
    definition: State space model, a mathematical framework for dynamic systems.
  - term: Mamba
    definition: A selective state space model with linear-time sequence modeling.
critical_citations:
  - "[Vaswani et al., 2017] — Introduced Transformer with self-attention."
  - "[Hochreiter & Schmidhuber, 1997] — LSTM for long-term dependencies."
  - "[Box et al., 1970] — ARIMA statistical forecasting foundation."
  - "[Zeng et al., 2023] — LTSF-Linear showing linear models outperform Transformers."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      justification: Survey covers deep learning models for time series forecasting applicable to spending prediction.
    - code: 6.B
      name: Spending Forecasting Algorithm
      justification: Detailed analysis of Transformer, Mamba, and diffusion models for long-term forecasting.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      justification: Discusses RobustTSF for anomaly-aware forecasting and distribution shift handling.
    - code: 8.B
      name: Anomaly Detection Algorithm
      justification: Reviews methods for handling anomalies in time series (constant, missing, Gaussian).
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      justification: Section 2.4 provides comprehensive evaluation metrics (MAE, MSE, CRPS, etc.).
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: Compares model performance on benchmark datasets like Monash archive.
  contribution: "Odin's spending forecasting module can leverage Transformer-based models like PatchTST and iTransformer, which use patching and cross-dimension attention to improve long-term prediction accuracy. The anomaly detection module can adopt diffusion-based conditional models (e.g., TimeGrad, CSDI) to provide probabilistic forecasts and uncertainty estimates, enhancing detection of irregular spending patterns. System evaluation can be standardized using metrics from Section 2.4, including MAE, MSE, and CRPS, and benchmark datasets from the Monash archive. The survey's analysis of channel dependency and distribution shift informs Odin's design choices between CI and CD strategies for multivariate spending data. Finally, Mamba-based models offer efficient linear-time inference, suitable for mobile-first deployment."
  directly_justifies:
    - "Patching technique (PatchTST) enables longer look-back windows for improved forecasting accuracy."
    - "Channel independent strategy is more robust to distribution shifts in multivariate time series."
    - "Simple linear models can outperform complex Transformers for certain forecasting tasks."
    - "Mamba provides linear-time complexity and selective memory for long sequence forecasting."
    - "Diffusion models enable probabilistic forecasting with uncertainty quantification."
  limits:
    - "Survey is limited to deep learning and excludes detailed statistical model comparisons."
    - "Performance claims may not generalize to Philippine-specific spending patterns."
    - "Computational costs of large foundation models may exceed mobile device constraints."
  mapping_rationale: "This survey focuses on technical aspects of time series forecasting, including predictive modeling (6.A, 6.B), anomaly detection (8.A, 8.B), and evaluation (12.A, 12.B). It does not address behavioral profiling (5.A-5.C), expense categorization (3.A-3.B), budget recommendation (7.A-7.C), mobile-first design (9.A-9.B), data privacy (10.A-10.B), user retention (11.A-11.B), or savings/debt management (13.A-13.B) because the paper contains no citeable claims on these PFMS-specific domains. Borderline topics like distribution shift and feature extraction are methodological and support forecasting algorithms rather than constituting standalone Odin topics."
limitations:
  - "Skipped detailed theoretical backgrounds of models. [unacknowledged]"
  - "Left specific differences in characteristics across time series datasets for future work."
  - "AGI and adaptive modeling (meta-learning, reinforcement learning) could be further explored."
  - "Domain-specific characteristics require expert knowledge not covered in the survey."
remember_this:
  - "Simple linear models can outperform complex Transformers for time series forecasting."
  - "Patching time series into 64-length patches improves Transformer performance."
  - "Channel independence is more robust to distribution shifts than channel dependence."
  - "Mamba offers linear-time sequence modeling, challenging Transformer dominance."
  - "Diffusion models enable probabilistic forecasting by modeling prediction uncertainty."
```