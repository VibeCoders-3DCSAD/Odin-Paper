```yaml
paper_id: 10.3390/s25010190
designation: international
title: A Survey of Deep Anomaly Detection in Multivariate Time Series: Taxonomy, Applications, and Directions
authors: Wang, F.; Jiang, Y.; Zhang, R.; Wei, A.; Xie, J.; Pang, X.
year: 2025
venue: Sensors
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 12.A
shorthand_tags:
  - /predictive-modeling
  - /spending-forecast
  - /anomaly-detection
  - /anomaly-algorithm
  - /eval-framework
tldr: A comprehensive survey categorizing deep learning methods for multivariate time series anomaly detection into forecasting, reconstruction, and contrastive approaches, with analysis of datasets and future directions.
problem_and_motivation: Traditional anomaly detection methods face limitations in handling high-dimensional multivariate time series with complex temporal and inter-variable dependencies. Deep learning offers powerful representation learning but lacks a structured taxonomy for multivariate time series anomaly detection. This survey addresses the gap by organizing recent deep learning methods and identifying open challenges.
approach:
  - Conducted a structured review of deep learning for multivariate time series anomaly detection.
  - Proposed a taxonomy based on learning paradigms (unsupervised, semi-supervised, self-supervised) and model architectures (CNN, RNN, GNN, Transformer, etc.).
  - Organized methods into three strategies: forecasting-based, reconstruction-based, and contrastive-based.
  - Compiled public datasets from multiple domains including aerospace, cybersecurity, healthcare, and finance.
  - Discussed evaluation metrics and open research directions.
findings:
  - "num: 46 deep learning models are reviewed and categorized."
  - Forecasting methods using Transformers outperform others in handling long-range dependencies.
  - Reconstruction methods using VAEs and GANs struggle with subtle anomalies and mode collapse.
  - Contrastive learning, especially with LLMs, shows promise for few-shot anomaly detection.
  - Public datasets vary widely in anomaly rates, from 0.03% to 36%.
key_figures_tables:
  - "Figure 1: Classification framework for multivariate time series anomaly types → Anomalies split into intra-metric and inter-metric categories."
  - "Figure 2: Examples of point-wise and pattern-wise anomalies → Point anomalies are spikes; pattern anomalies are discordant subsequences."
  - "Figure 4: General pipeline for deep MTSAD → Data processing, anomaly detection strategy, application domains."
  - "Table 1: Overview of 46 deep anomaly detection models → Models categorized by backbone, learning paradigm, and input type."
  - "Table 2: Public datasets for MTSAD → Anomaly rates range from 0.03% to 36% across domains."
key_equations:
  - equation: "|x_t - \\hat{x}_t| > \\delta"
    explanation: "Threshold for global point anomaly detection."
  - equation: "X_k = \\sum_{t=0}^{T-1} x_t e^{-i2\\pi k t / T}"
    explanation: "Discrete Fourier Transform for frequency domain analysis."
definitions:
  - term: MTSAD
    definition: Multivariate Time Series Anomaly Detection
  - term: CNN
    definition: Convolutional Neural Network
  - term: RNN
    definition: Recurrent Neural Network
  - term: GNN
    definition: Graph Neural Network
  - term: VAE
    definition: Variational Autoencoder
  - term: GAN
    definition: Generative Adversarial Network
  - term: LLM
    definition: Large Language Model
  - term: DFT
    definition: Discrete Fourier Transform
  - term: FFT
    definition: Fast Fourier Transform
critical_citations:
  - "[Hundman et al., 2018] — Pioneered LSTM with nonparametric thresholding."
  - "[Zong et al., 2018] — First deep AE-GMM for anomaly detection."
  - "[Xu et al., 2022] — Introduced association discrepancy for Transformers."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      justification: Survey covers forecasting-based anomaly detection methods applicable to spending prediction.
    - code: 6.B
      name: Spending Forecasting Algorithm
      justification: Detailed review of RNN, Transformer forecasting models.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      justification: Comprehensive taxonomy of deep anomaly detection techniques directly relevant to fraud or outlier detection in PFMS.
    - code: 8.B
      name: Anomaly Detection Algorithm
      justification: Compares algorithms across reconstruction, forecasting, and contrastive paradigms.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      justification: Discusses public datasets, evaluation metrics, and benchmarking challenges.
  contribution: "Odin's anomaly detection module (8.A, 8.B) can leverage forecasting-based methods like LSTM and Transformer to identify unusual spending patterns by comparing predicted vs. actual transactions. The reconstruction-based approaches (e.g., VAE, GAN) reviewed in this paper inform Odin's ability to detect subtle anomalies in multivariate financial time series without labeled data. The survey's evaluation framework insights (12.A) guide Odin's benchmarking strategy for anomaly detection accuracy and false positive rates. Contrastive learning techniques, including LLM-based methods, suggest future enhancements for Odin's cold-start anomaly detection."
  directly_justifies:
    - "Deep learning models outperform statistical methods for multivariate time series anomaly detection in high-dimensional data."
    - "Transformer-based anomaly detectors capture long-range temporal dependencies better than RNNs."
    - "Reconstruction error alone is insufficient for detecting subtle anomalies in noisy data."
    - "Public benchmark datasets for anomaly detection have anomaly rates ranging from 0.03% to 36%."
  limits:
    - "Survey does not provide empirical comparisons or benchmark results across methods."
    - "Focus on general MTSAD rather than personal finance domain specifically."
    - "Limited discussion of real-time or resource-constrained deployment considerations."
  mapping_rationale: "The survey was screened against Odin's functional domains. The anomaly detection domain (8) is directly relevant as the paper provides a comprehensive taxonomy of deep learning methods for multivariate time series anomaly detection. Spending forecasting (6) is also relevant because forecasting-based methods are a major category reviewed. System evaluation (12) applies due to the survey's detailed coverage of public datasets and evaluation metrics. Behavioral profiling (5), budget recommendation (7), expense categorization (3), mobile-first design (9), data privacy (10), user retention (11), and savings/debt management (13) were rejected as the paper does not address these topics. Borderline case: predictive modeling (6.A) is included because forecasting errors directly indicate anomalies, which Odin can use for spending anomaly detection."
limitations:
  - "Focuses on general MTSAD without personal finance-specific validation [unacknowledged]."
  - "Deep learning models require large training datasets, limiting applicability to users with sparse transaction history [unacknowledged]."
  - "Evaluation metrics are not standardized across studies, making comparisons difficult (acknowledged as future direction)."
remember_this:
  - "Survey reviews 46 deep learning models for multivariate time series anomaly detection."
  - "Transformer-based methods outperform RNNs in capturing long-range temporal dependencies."
  - "Contrastive learning and LLMs offer promising few-shot anomaly detection capabilities."
  - "Anomaly rates in public datasets vary from 0.03% to 36% across domains."
```