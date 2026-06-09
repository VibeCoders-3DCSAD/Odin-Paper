```yaml
paper_id: d3b5c6e7-f8a9-4b0c-91d2-e3f4a5b6c7d8
designation: international
title: Research Progress and Trends of Deep Learning in Stock Price Prediction: A Systematic Review from LSTM to Transformer
authors: Gong, H.
year: 2026
venue: ITM Web of Conferences
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 12.A
shorthand_tags:
  - predictive-modeling
  - spending-forecast
  - anomaly-detection
  - anomaly-algorithm
  - evaluation-framework
tldr: Systematically reviews deep learning models for stock price prediction from LSTM to Transformer, comparing architectures, datasets, and evaluation metrics.
problem_and_motivation: Traditional statistical and machine learning methods fail to capture the non-linear, non-stationary dynamics of stock markets. Deep learning models like LSTM and Transformer have shown superior performance, but a systematic review tracing their evolution from LSTM to hybrid architectures is missing. This gap makes it difficult for researchers to select appropriate models for financial time series forecasting.
approach:
  - Conducts a systematic literature review of deep learning models for stock price prediction.
  - Analyzes recurrent models (RNN, LSTM, GRU), convolutional models (CNN), Transformer variants, and hybrid models.
  - Compares datasets including S&P 500, NIFTY 50, Moroccan market, and limit order book data.
  - Evaluates models using RMSE, MAE, MAPE, directional accuracy, Sharpe ratio, and R².
  - Discusses empirical results from Fischer & Krauss (2018), Wang et al. (2022), Zhao et al. (2025), and others.
  - Identifies challenges in data noise, overfitting, interpretability, and computational efficiency.
  - Outlines future directions: multimodal fusion, explainable AI, real-time adaptive learning, and state space models.
findings:
  - "num: LSTM achieved 0.46% daily return on S&P 500 constituents (1992-2015) with Sharpe ratio up to 2.34."
  - "num: Transformer reduced MAE by 20.73%, MSE by 34.84%, and MAPE by 25.63% compared to LSTM in new energy vehicle stock prediction."
  - "num: LSTM-Transformer hybrid reduced MAE and RMSE by over 50% relative to parent models and attained R² of 0.9618 (LSTM: 0.8430, Transformer: 0.7763)."
  - Deep learning models consistently outperform traditional statistical methods and shallow machine learning.
  - Hybrid models and multimodal fusion are the dominant development trend in time series forecasting.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network with gating mechanisms to avoid vanishing gradients.
  - term: GRU
    definition: Gated Recurrent Unit, a simplified variant of LSTM with fewer gates.
  - term: Transformer
    definition: Architecture based solely on self-attention, no recurrence or convolution.
  - term: CNN
    definition: Convolutional Neural Network, uses local receptive fields for feature extraction.
  - term: GNN
    definition: Graph Neural Network, operates on graph-structured data.
  - term: RMSE
    definition: Root Mean Square Error, sensitive to large deviations.
  - term: MAE
    definition: Mean Absolute Error, average absolute deviation.
  - term: MAPE
    definition: Mean Absolute Percentage Error, relative error metric.
  - term: DA
    definition: Directional Accuracy, correctness of predicted price movement direction.
critical_citations:
  - "[Fischer & Krauss, 2018] — First large-scale LSTM stock prediction with Sharpe ratio evidence."
  - "[Wang et al., 2022] — Transformer outperforms LSTM by 20-25% in error metrics."
  - "[Zhao et al., 2025] — LSTM-Transformer hybrid reduces error over 50% with R² 0.96."
  - "[Lahebb & Benaly, 2024] — Comparison of ARIMA, LSTM, Transformer on Moroccan market."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      justification: Reviews time-series forecasting models applicable to spending prediction.
    - code: 6.B
      name: Spending Forecasting Algorithm
      justification: LSTM and Transformer algorithms can forecast future spending patterns.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      justification: Discusses anomaly detection in financial time series (e.g., market jumps, outliers).
    - code: 8.B
      name: Anomaly Detection Algorithm
      justification: Self-attention and hybrid models for detecting unusual transactions.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      justification: Comprehensive evaluation metrics (RMSE, MAE, Sharpe ratio) inform system benchmarking.
  contribution: "Odin's spending forecasting module can directly adopt LSTM-Transformer hybrid models to improve prediction accuracy, as evidenced by over 50% error reduction. The anomaly detection system can leverage self-attention mechanisms from Transformers to identify unusual spending patterns with higher sensitivity. Evaluation frameworks within Odin should incorporate directional accuracy and Sharpe ratio metrics from this review to assess both predictive fit and economic value. The cold-start problem in behavioral profiling may benefit from transfer learning techniques discussed in future trends, enabling rapid adaptation to new users."
  directly_justifies:
    - "LSTM-Transformer hybrid reduces prediction error by over 50% compared to single models."
    - "Transformer models achieve 20-25% lower error than LSTM in long-range dependency tasks."
    - "Deep learning models consistently outperform traditional methods in financial time series forecasting."
    - "Directional accuracy and Sharpe ratio are essential for evaluating real-world usability."
  limits:
    - "Paper focuses on stock market data, not personal transaction histories or spending behavior."
    - "Results may not generalize to lower-frequency, irregular individual spending patterns."
    - "No discussion of privacy-preserving techniques or mobile-first constraints."
  mapping_rationale: "The paper is a systematic review of deep learning for stock price prediction, not personal finance. However, its methods for time series forecasting and anomaly detection are directly transferable to Odin's spending forecasting (6.A, 6.B) and anomaly detection (8.A, 8.B). The evaluation metrics discussed (12.A) inform Odin's system evaluation framework. Rejected topics include behavioral profiling (5.A-C) because the paper does not address user financial behavior or profiles. Data privacy (10) and mobile design (9) are absent. Borderline cases like user retention (11) were rejected as no engagement dynamics are discussed."
limitations:
  - "Systematic review without original empirical validation; relies on cited studies. [unacknowledged]"
  - "Focus on stock markets limits direct applicability to personal spending data. [unacknowledged]"
  - "Does not address real-time deployment constraints or latency requirements for mobile apps."
  - "No discussion of model interpretability methods like SHAP or LIME in depth."
remember_this:
  - "LSTM achieves 0.46% daily return with Sharpe ratio 2.34 on S&P 500."
  - "Transformer reduces MAE by 20.73% compared to LSTM in stock prediction."
  - "LSTM-Transformer hybrid reduces error by over 50% and achieves R² 0.96."
  - "Hybrid and multimodal models are the dominant trend in time series forecasting."
  - "Directional accuracy and Sharpe ratio are critical for real-world financial systems."
```