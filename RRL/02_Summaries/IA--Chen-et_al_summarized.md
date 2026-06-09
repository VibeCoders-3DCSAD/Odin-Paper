```yaml
paper_id: 10.56557/jobari/2024/v30i69014
designation: international
title: A Survey of Time Series Data Forecasting Methods Based on Deep Learning
authors: Chen, J.; Chen, T.; Wang, Y.; Wang, L.
year: 2024
venue: Journal of Basic and Applied Research International
odin_topics:
  - 6.A
  - 6.B
  - 12.A
  - 12.B
shorthand_tags:
  - /spending-forecast
  - /predictive-modeling
  - /eval-framework
  - /eval-algorithm
tldr: Surveys deep learning methods for time series forecasting including RNN, LSTM, GRU, and Transformer, and compares their performance on public datasets.
problem_and_motivation: Traditional statistical models for time series forecasting require extensive manual feature engineering and struggle with large-scale data. Deep learning offers automatic feature extraction but faces challenges like vanishing gradients and difficulty capturing long-range dependencies. This survey systematically reviews deep learning methods to identify strengths and weaknesses for forecasting tasks.
approach:
  - Reviews common time series features, datasets (ETT, ECL, Traffic, Weather, ILI, TE), and evaluation metrics (MSE, MAE, RMSE, MAPE, SMAPE, R²).
  - Describes RNN structure and its vanishing/exploding gradient problem.
  - Explains LSTM gating mechanism (forget, input, output gates) to address gradient issues.
  - Introduces GRU as a simplified LSTM with update and reset gates.
  - Presents Bi-LSTM for bidirectional sequence processing.
  - Details Transformer self-attention, multi-head attention, and positional encoding.
  - Conducts univariate forecasting experiments on ETTm2, Electricity, Traffic, Weather with input length 24 and prediction length 1 using PyTorch.
  - Compares RNN, LSTM, GRU, Transformer, LSTM-RNN using MSE and MAE.
findings:
  - "num: Transformer achieved best performance on ETTm2 with MSE=3.418, MAE=1.399."
  - "num: LSTM achieved minimum MAE on Electricity (1.848) and Traffic (0.020)."
  - "num: GRU achieved minimum MSE on Electricity (19.524) and Traffic (0.00110)."
  - "num: RNN achieved best performance on Weather with MSE=0.007, MAE=0.060."
  - LSTM-RNN generally outperforms standard RNN and shows better results on some datasets.
  - Deep learning models require less manual engineering but need large datasets and are less interpretable.
key_figures_tables:
  - "Figure 10: Prediction curves on ETTm2 dataset → Transformer fits best."
  - "Figure 11: Prediction curves on ECL dataset → LSTM and GRU perform well."
  - "Figure 12: Prediction curves on Weather dataset → RNN best."
  - "Figure 13: Prediction curves on Traffic dataset → GRU lowest MSE."
  - "Table 1: Univariate prediction performance comparison → Transformer best on ETTm2, RNN best on Weather."
key_equations:
  - equation: "MSE = (1/n) Σ(y_i - ŷ_i)^2"
    explanation: "Average squared prediction error."
  - equation: "Attention(Q,K,V) = softmax(QK^T / √d_k) V"
    explanation: "Self-attention mechanism for weighting values."
  - equation: "PE(t)_i = sin(t / 10000^{2i/d}) or cos"
    explanation: "Positional encoding for sequence order."
definitions:
  - term: "TSF"
    definition: "Time Series Forecasting, predicting future values from historical patterns."
  - term: "RNN"
    definition: "Recurrent Neural Network, processes sequences with cyclic connections."
  - term: "LSTM"
    definition: "Long Short-Term Memory, RNN variant with gating to manage long-term dependencies."
  - term: "GRU"
    definition: "Gated Recurrent Unit, simplified LSTM with update and reset gates."
  - term: "Transformer"
    definition: "Deep learning architecture based on self-attention, not recurrence."
  - term: "MSE"
    definition: "Mean Squared Error, average of squared prediction errors."
  - term: "MAE"
    definition: "Mean Absolute Error, average of absolute prediction errors."
critical_citations:
  - "[Vaswani et al., 2017] — Introduced Transformer self-attention."
  - "[Hochreiter & Schmidhuber, 1997] — Proposed LSTM to solve gradient issues."
  - "[Elman, 1990] — Foundational RNN structure."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      justification: "Reviews deep learning models for time series forecasting applicable to spending prediction."
    - code: "6.B"
      name: "Spending Forecasting Algorithm"
      justification: "Compares algorithms (RNN, LSTM, GRU, Transformer) for univariate forecasting tasks."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      justification: "Discusses evaluation metrics (MSE, MAE) and experimental protocols."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      justification: "Provides quantitative performance comparisons across multiple datasets."
  contribution: "This survey provides a structured comparison of deep learning forecasting algorithms relevant to Odin's spending forecasting module. The evaluation metrics and experimental protocol (MSE, MAE on multiple datasets) inform Odin's evaluation framework for algorithmic modules. The discussion of LSTM and Transformer strengths guides algorithm selection for spending prediction. The identification of hybrid models (LSTM-RNN) suggests potential performance improvements."
  directly_justifies:
    - "Deep learning models can automatically extract temporal features from time series data."
    - "Transformer self-attention captures long-range dependencies better than RNNs."
    - "No single model dominates all datasets; model selection depends on data characteristics."
    - "Evaluation should use both MSE and MAE to capture different error aspects."
  limits:
    - "Paper is a survey, not an original algorithm; no novel contribution."
    - "Experiments are univariate only, not multivariate spending data."
    - "Only four datasets used; others excluded due to insufficient periodicity."
  mapping_rationale: "The paper focuses on time series forecasting using deep learning, which directly maps to Odin's spending forecasting domain (6.A, 6.B). It also extensively discusses evaluation metrics and comparative experiments, supporting evaluation frameworks (12.A, 12.B). No coverage of behavioral profiling, expense categorization, mobile design, privacy, retention, savings, or debt management. Budget recommendation (7) is not addressed because the paper does not prescribe budget amounts or strategies; it only forecasts future values. Anomaly detection (8) is not covered. Thus only codes 6.A, 6.B, 12.A, 12.B are selected."
limitations:
  - "Survey format; no novel algorithm proposed."
  - "Univariate experiments may not generalize to multivariate spending data [unacknowledged]."
  - "Excluded datasets with insufficient periodicity, limiting generalizability."
  - "No discussion of real-time forecasting constraints or deployment considerations [unacknowledged]."
remember_this:
  - "Transformer achieved lowest MAE (1.399) on ETTm2 dataset."
  - "No single deep learning model dominates all time series forecasting tasks."
  - "Deep learning automates feature extraction but requires large training data."
  - "Evaluation metrics MSE and MAE are standard for comparing forecasting models."
```