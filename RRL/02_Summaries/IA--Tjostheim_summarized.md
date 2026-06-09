```yaml
paper_id: 10.3390/e27030279
designation: international
title: Selected Topics in Time Series Forecasting: Statistical Models vs. Machine Learning
authors: Tjøstheim, D.
year: 2025
venue: Entropy
odin_topics:
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 7.C
  - 8.A
  - 8.B
  - 12.A
  - 12.B
shorthand_tags:
  - /predictive-modeling
  - /spending-forecast
  - /budgeting-strategies
  - /budget-recommendation
  - /budget-algorithm
  - /anomaly-detection
  - /anomaly-algorithm
  - /evaluation-frameworks
  - /algorithm-evaluation
tldr: A survey comparing statistical models and machine learning methods for time series forecasting, analyzing results from M1-M6 forecasting competitions and weather forecasting.
problem_and_motivation: The forecasting community lacks a systematic comparison between traditional parametric statistical models and modern machine learning methods across different data regimes and application domains. Understanding when each approach excels is critical for practitioners, yet black-box nature and lack of theoretical results for ML methods raise concerns. This review synthesizes evidence from forecasting competitions and specialized applications to guide method selection.
approach:
  - Surveys classical parametric models: exponential smoothing, ARIMA, theta method, and state space models.
  - Reviews nonlinear parametric models: threshold autoregression, STAR, and hidden Markov chain models.
  - Presents ML methods: CNNs/TCNs, RNNs, LSTM, transformers, random forest, and gradient boosting.
  - Analyzes forecasting competition results from M1 (1982) to M6 (2024) with varying series counts and frequencies.
  - Examines specialized applications: volatility forecasting, inflation prediction using 122 explanatory variables, and weather forecasting with GraphCast.
  - Discusses explainable AI (XAI) techniques including SHAP values for opening black-box models.
findings:
  - "num: In M4 competition (100,000 series), only 1 pure statistical method ranked among top 10 most accurate methods."
  - "num: Light-GBM gradient boosting outperformed all alternatives in M5 retail sales competition."
  - "ML methods excel for high spectral entropy data (noisy, short-interval, irregular time series)."
  - "num: GraphCast beats HRES (industry gold standard) in medium-range weather forecasts up to 10 days."
  - "num: In volatility forecasting with commonality information, MLP and LSTM gave best forecasts among compared models."
  - "Hybrid methods combining statistical and ML features consistently outperform pure approaches."
  - "Random forest outperformed other methods for forecasting US inflation using 122 explanatory variables."
  - "Transformers enable parallel processing and long-range dependence modeling, replacing RNNs in many applications."
  - "M6 competition found virtually no correlation between best forecasts and best investment decisions."
  - "GenCast (diffusion-based) beats ENS ensemble forecast in 97.2% of 1320 targets."
key_figures_tables:
  - "None."
key_equations:
  - equation: "\\hat{y}_{t+1} = \\alpha y_t + (1-\\alpha)\\hat{y}_t"
    explanation: "Simple exponential smoothing forecast recursion."
  - equation: "y_t = a_1 y_{t-1} + \\dots + a_p y_{t-p} + e_t"
    explanation: "pth-order autoregressive model for point forecasts."
  - equation: "y_t = \\theta_1 y_{t-1} \\mathbf{1}_{\\{s_{t-1} \\le c\\}} + \\theta_2 y_{t-1} \\mathbf{1}_{\\{s_{t-1} > c\\}} + e_t"
    explanation: "Threshold autoregression with two regimes."
  - equation: "h_t = \\sigma_h(W_h x_t + U_h h_{t-1} + b_h)"
    explanation: "Recurrent neural network hidden state update."
  - equation: "\\lambda_t = d + a\\lambda_{t-1} + b y_{t-1}"
    explanation: "Poisson autoregression (INGARCH) intensity recursion."
definitions:
  - term: ARIMA
    definition: "Autoregressive Integrated Moving Average - classical linear time series model."
  - term: ML
    definition: "Machine learning - data-driven algorithms including neural networks and random forests."
  - term: LSTM
    definition: "Long Short-Term Memory - recurrent network designed to avoid vanishing gradients."
  - term: TCN
    definition: "Temporal Convolutional Network - CNN adapted for time series with causal convolutions."
  - term: GARCH
    definition: "Generalized Autoregressive Conditional Heteroskedasticity - volatility forecasting model."
  - term: VAR
    definition: "Vector Autoregression - multivariate linear time series model."
  - term: XAI
    definition: "Explainable Artificial Intelligence - methods to interpret black-box models."
  - term: SHAP
    definition: "SHapley Additive exPlanations - game-theoretic feature importance values."
critical_citations:
  - "[Box & Jenkins, 1970] — Defined ARIMA modeling sequence (identification, estimation, diagnostics)."
  - "[Hochreiter & Schmidhuber, 1997] — Introduced LSTM, most cited neural network of 20th century."
  - "[Vaswani et al., 2017] — Attention Is All You Need, transformer architecture foundation."
  - "[Makridakis et al., 2020] — M4 competition with 100,000 series, hybrid methods dominant."
  - "[Lam et al., 2023] — GraphCast achieves unprecedented medium-range weather forecast accuracy."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      justification: "Reviews forecasting methods (ARIMA, ML) that underpin spending prediction."
    - code: 6.B
      name: Spending Forecasting Algorithm
      justification: "Compares statistical vs ML algorithms for time series prediction, directly applicable to spending."
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      justification: "Forecasting accuracy determines budget adherence feasibility."
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      justification: "Survey's findings on ML superiority for noisy data inform budget recommendation design."
    - code: 7.C
      name: Budget Recommendation Algorithm
      justification: "Light-GBM and hybrid methods shown effective for intermittent retail sales (analogous to irregular spending)."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      justification: "Forecast errors are a primary signal for anomaly detection; reviews evaluation metrics."
    - code: 8.B
      name: Anomaly Detection Algorithm
      justification: "Discusses threshold models and LSTM for detecting deviations in time series."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      justification: "Critiques forecasting competition metrics (MAE, MAPE, quantile scores) and their limitations."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: "Compares ML vs statistical methods across multiple competitions (M1-M6) and real-world datasets."
  contribution: "This survey provides Odin's forecasting module with empirical evidence that hybrid statistical-ML methods outperform pure approaches, especially for noisy or high-frequency data. It identifies Light-GBM gradient boosting as state-of-the-art for intermittent retail-like series, informing spending forecast algorithm selection. The review of forecasting competition evaluation metrics (MAE, MAPE, quantile scores) directly shapes Odin's evaluation framework for budget recommendation and anomaly detection modules. The discussion of XAI techniques including SHAP values offers a path to interpretability for Odin's black-box ML components, addressing user trust requirements. Finally, the GraphCast example demonstrates how transformer and graph neural network architectures enable long-range dependency modeling, relevant to seasonal spending patterns."
  directly_justifies:
    - "Hybrid statistical-ML forecasting methods consistently outperform pure statistical or pure ML approaches."
    - "Light-GBM gradient boosting is superior for intermittent, erratic time series with many zero values."
    - "ML methods excel when data have high spectral entropy (noisy, short intervals, irregular sampling)."
    - "SHAP values provide a unified framework for explaining black-box forecast contributions by feature."
    - "Forecast accuracy should be accompanied by uncertainty intervals or forecast distributions, not just point forecasts."
  limits:
    - "Survey focuses on univariate series; multivariate forecasting with exogenous variables is underexplored in competitions."
    - "Black-box nature of ML methods remains a concern despite emerging XAI techniques."
    - "Forecasting competitions did not systematically evaluate extreme event ('black swan') performance."
    - "Limited coverage of ML methods for integer time series, panel data, and dynamic networks."
  mapping_rationale: "This paper is a general survey of time series forecasting methods, not specific to Filipino young professionals or PFMS. However, it directly supports Odin's forecasting, budgeting, anomaly detection, and evaluation domains. Selected codes 6.A/6.B because spending forecasting is a core Odin function and the paper compares predictive algorithms. Codes 7.A/7.B/7.C are included because budget recommendation relies on forecast accuracy; the M5 competition's intermittent retail sales data closely mirrors irregular personal spending. Anomaly detection (8.A/8.B) is justified by the paper's discussion of forecast errors as signals and threshold models. Evaluation codes (12.A/12.B) apply because the paper critically analyzes competition metrics and comparative methodology. Rejected codes (e.g., 3.A/3.B on categorization, 5.A on behavioral profiling, 9.A/9.B on mobile design, 10.A/10.B on privacy) as the paper provides no citeable claims on those topics. The paper's international scope and lack of Philippine-specific content make it 'international' designation."
limitations:
  - "Survey is not systematic; author acknowledges personal research background bias."
  - "Limited evaluation of multivariate forecasts and exogenous variable influence. [unacknowledged]"
  - "No theoretical convergence results for ML methods in forecasting contexts. [unacknowledged]"
  - "Forecasting competitions may have selection bias; top methods often unpublished commercial algorithms."
  - "Weather forecasting section is descriptive; no quantitative comparison of pure ML vs NWP on same benchmarks."
remember_this:
  - "Hybrid statistical-ML methods outperform pure approaches."
  - "Light-GBM gradient boosting excelled in M5 with 42,480 retail series."
  - "ML methods beat statistical models for noisy, high-frequency data."
  - "GraphCast and GenCast achieve unprecedented weather forecast accuracy."
```