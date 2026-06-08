```yaml
paper_id: 10.1109/ACCESS.2024.3440631
designation: algorithm-specific
title: Short-Term Load Forecasting: A Comprehensive Review and Simulation Study With CNN-LSTM Hybrids Approach
authors: Kaleemullah, K.; Ahsan, M.; Hasanat, S.M.; Haris, M.; Yousaf, H.; Raza, S.F.; Tandon, R.; Abid, S.; Ullah, Z.
year: 2024
venue: IEEE Access
odin_topics:
  - 6.A
  - 6.B
shorthand_tags:
  - /spending-forecasting
  - /cnn-lstm
tldr: Reviews short-term load forecasting methods and proposes a hybrid CNN-LSTM model that achieves superior accuracy on Pakistan's NTDC grid data.
problem_and_motivation: Accurate short-term load forecasting is critical for power grid stability and economic operation. Existing statistical, intelligent, and hybrid models have limitations in capturing non-linear, non-stationary load patterns. There is a need for more accurate and reliable forecasting methods to improve reserve management.
approach:
  - The paper comprehensively reviews statistical (ARIMA, SARIMA, ES, GLM), intelligent (SVM, DT, RF, GB, MLP, ensemble), and hybrid STLF models with mathematical and graphical analysis.
  - A hybrid CNN-LSTM model is proposed: 1D CNN layers (48, 32, 16 filters) extract spatial features, followed by three LSTM layers (20 units each) capture temporal dependencies, with dropout regularization.
  - Data from Pakistan’s NTDC national grid (hourly, Jan 2019–May 2023) is preprocessed: outlier handling using IQR, feature extraction (hour, month, weekday, holiday), 70/30 train-validation split.
  - Evaluation uses RMSE, MAE, MAPE for single-step and 24-hour forecasting, compared against previous models on NTDC and AEP datasets.
  - Hyperparameters: Adam optimizer, MAE loss, tanh activation in output layer, dropout rate 0.25.
findings:
  - "num: Single-step forecasting on NTDC achieved RMSE 538.71, MAE 371.97, MAPE 2.72."
  - "num: 24-hour forecasting on NTDC achieved RMSE 951.94, MAE 656.35, MAPE 4.72."
  - "num: On AEP dataset, single-step RMSE 126.35, MAE 94.27, MAPE 0.64; 24-hour RMSE 702.97, MAE 507.97, MAPE 3.39."
  - The proposed hybrid CNN-LSTM outperforms standalone benchmarks (Rafi et al. 2021, Alhussein et al. 2020) in both single-step and multi-step horizons.
  - Predicted load closely mirrors actual load, with errors concentrated during off-peak hours.
key_figures_tables:
  - "Figure 12: Proposed model architecture with CNN blocks, LSTM layers, and concatenation → CNN extracts features, LSTM captures temporal dependencies."
  - "Figure 18: Actual vs predicted load over time → Predicted load closely follows actual load."
  - "Figure 19: Comparison with reference model → Proposed model (red) has predictions closer to actual than benchmark (blue)."
  - "Table 8: Single-step performance metrics → Proposed model achieves lowest RMSE, MAE, MAPE across both datasets."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: STLF
    definition: Short-Term Load Forecasting, predicting electricity demand from an hour ahead to days or weeks.
  - term: CNN
    definition: Convolutional Neural Network, used for feature extraction from high-dimensional data.
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network for sequence prediction.
  - term: ARIMA
    definition: Autoregressive Integrated Moving Average, a statistical time series model.
  - term: SVM
    definition: Support Vector Machine, a supervised learning model.
  - term: RMSE
    definition: Root Mean Square Error, a forecasting error metric.
  - term: MAE
    definition: Mean Absolute Error, a forecasting error metric.
  - term: MAPE
    definition: Mean Absolute Percentage Error, a relative forecasting error metric.
critical_citations:
  - "[Rafi et al., 2021] — Benchmark CNN-LSTM model for load forecasting."
  - "[Alhussein et al., 2020] — Benchmark hybrid model for individual household load forecasting."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      justification: "Paper provides comparative evaluation of time series and deep learning models for forecasting, directly applicable to spending prediction in PFMS."
    - code: 6.B
      name: Spending Forecasting Algorithm
      justification: "Proposed CNN-LSTM hybrid offers a concrete algorithm for sequential data forecasting, transferable to user spending patterns."
  contribution: "For Odin's spending forecasting module, the paper validates that hybrid CNN-LSTM architectures outperform statistical and standalone neural models on sequential data. The evaluation metrics (RMSE, MAE, MAPE) provide a template for Odin's algorithm benchmarking. The data preprocessing steps—handling outliers, extracting cyclic features, and creating sliding windows—inform how Odin should prepare transaction histories. The concatenation of CNN-extracted features with LSTM temporal states offers a design pattern for Odin's spending predictor. The explicit comparison of single-step vs. multi-step forecasting helps Odin decide between next-day vs. next-week spending predictions."
  directly_justifies:
    - "Hybrid CNN-LSTM models achieve lower forecasting error than standalone ARIMA, SVM, or LSTM models."
    - "Feature extraction using 1D CNN improves forecasting accuracy by capturing local patterns."
    - "Dropout regularization reduces overfitting in deep forecasting models."
    - "MAE and MAPE are effective loss functions for evaluating spending forecast accuracy."
  limits:
    - "Models were tested only on electricity load data from Pakistan and US grids, not on personal financial transaction data."
    - "The study assumes no missing data; Filipino PFMS data will likely have missing or irregular entries."
    - "No probabilistic forecasting is provided, only point forecasts, limiting risk assessment for Odin users."
  mapping_rationale: "The paper was screened against Odin's functional domains. Spending forecasting (domain 6) was flagged because the paper directly evaluates time-series forecasting algorithms (ARIMA, LSTM, CNN-LSTM) with quantitative metrics. Topic codes 6.A (predictive modeling) and 6.B (spending forecasting algorithm) were selected because the proposed hybrid model and review of methods are directly citable for Odin's spending prediction module. Behavioral profiling (domain 5), anomaly detection (domain 8), and privacy (domain 10) are not addressed. Budget recommendation (domain 7) is tangential—the paper forecasts load, not optimal budgets. Mobile design (domain 9) and retention (domain 11) are absent. Thus only 6.A and 6.B are retained."
limitations:
  - "Tested only on two electricity datasets (NTDC Pakistan, AEP USA); generalizability to Filipino personal finance data is unverified. [unacknowledged]"
  - "The paper does not address concept drift or cold-start scenarios common in personal spending patterns. [unacknowledged]"
  - "Point forecasts only; no uncertainty intervals or probabilistic outputs. [acknowledged in future work]"
  - "Outliers were replaced with 24-hour means, which may not be appropriate for transaction data with genuine spikes."
remember_this:
  - "Hybrid CNN-LSTM achieved MAPE of 2.72 for single-step forecasting."
  - "CNNs extract local features while LSTMs capture long-term dependencies."
  - "Dropout and concatenation improve generalization in forecasting models."
  - "MAE and RMSE are standard metrics for evaluating forecast accuracy."
```