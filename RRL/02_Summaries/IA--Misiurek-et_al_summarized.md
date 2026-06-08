```yaml
paper_id: 10.3390/en18154032
designation: international
title: Review of Methods and Models for Forecasting Electricity Consumption
authors: Misiurek, K.; Olkuski, T.; Zysk, J.
year: 2025
venue: Energies
odin_topics:
  - 6.A
  - 6.B
  - 12.A
  - 12.B
shorthand_tags:
  - /forecasting
  - /time-series
  - /evaluation
tldr: A comprehensive review of electricity consumption forecasting methods across four time horizons, comparing classical statistical models with modern machine learning and deep learning techniques.
problem_and_motivation: Accurate electricity forecasting is critical for balancing supply and demand, integrating renewable energy, and modernizing grids. Inaccurate forecasts cause significant economic losses, with a 1% increase in error costing an additional USD 10 million annually. Existing methods range from classical ARIMA to advanced deep learning, but no universal approach exists.
approach:
  - Reviewed over 100 studies on electricity load forecasting published up to 2024, with emphasis on works from the last 5 years.
  - Categorized forecasting horizons into very short-term (30 min), short-term (day to weeks), medium-term (months to years), and long-term (decades).
  - Compared classical statistical methods (ARIMA, SARIMA, Holt-Winters, linear regression) against machine learning (ANN, Random Forest) and deep learning (LSTM, CNN-LSTM, Transformer).
  - Evaluated hybrid models combining statistical decomposition with neural networks, such as SARIMA-ANN and regression-LSTM.
  - Analyzed performance using error metrics including MAPE, RMSE, MAE, and sMAPE from cited literature.
  - Examined input data types: national aggregates, sector-specific, individual smart meter readings, and industrial operational data.
  - Included optimization techniques like genetic algorithms, Coronavirus Optimization Algorithm, and Bayesian optimization for hyperparameter tuning.
  - Assessed probabilistic forecasting methods such as quantile regression and pinball loss guided LSTM.
  - No original experiments; synthesized findings from existing studies as a review article.
findings:
  - "num: LSTM model achieved RMSE improvement of approximately 10-15% over traditional machine learning models in aggregated household forecasting."
  - "num: Transformer with sparse attention achieved inference up to 5 times faster than RNN methods while maintaining comparable accuracy (sMAPE ≈ 0.18 for 1-day forecast)."
  - "num: ARIMA model outperformed regression (8.1% MAPE) and ANN (5.6% MAPE) with 3.8% MAPE for monthly electricity consumption in Saudi Arabia."
  - "num: Hybrid SARIMA-ANN model (Khashei & Bijari) achieved lowest RMSE of 0.0792 compared to SARIMA alone at 0.0823 for Turkish electricity."
  - "num: Optimized LSTM with genetic algorithm improved RMSE by 26.4% over ExtraTrees regressor (378 vs 513.8)."
  - No single universal forecasting method exists; effectiveness depends on time horizon, data availability, and application context.
  - Deep learning models (LSTM, CNN-LSTM) consistently outperform classical methods for highly nonlinear and volatile data, such as individual household consumption.
  - Hybrid models combining statistical and machine learning approaches provide superior accuracy and robustness across most forecasting horizons.
key_figures_tables:
  - "Figure 1: Primary energy consumption in selected countries (1998-2023) → China's consumption more than tripled, exceeding 45,000 TWh in 2023."
  - "Figure 2: Categories of electrical load forecasting by time horizon and operational domains → Distinguishes VSTLF (30 min), STLF (day-weeks), MTLF (months-years), LTLF (decades)."
  - "Table 1: Summary of very short-term load forecasting methods → LSTM and hybrid CNN-LSTM show lowest errors for 30-min to 4-hour horizons."
  - "Table 2: Summary of short-term load forecasting methods → ANN and ensemble deep learning achieve MAPE as low as 3.9% for hourly peak demand."
  - "Table 3: Summary of medium-term load forecasting methods → ARIMA effective for stable trends; hybrid models improve accuracy during economic shocks."
  - "Table 4: Summary of long-term load forecasting methods → Regression with economic variables achieves MAPE around 2%; neural networks capture nonlinear trends."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: ARIMA
    definition: AutoRegressive Integrated Moving Average, a classical time-series forecasting model for non-stationary data.
  - term: SARIMA
    definition: Seasonal ARIMA that extends ARIMA to handle seasonal patterns.
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network architecture that captures long-term dependencies.
  - term: CNN
    definition: Convolutional Neural Network, used for spatial feature extraction from time-series data.
  - term: MAPE
    definition: Mean Absolute Percentage Error, a common forecasting accuracy metric.
  - term: RMSE
    definition: Root Mean Square Error, a metric penalizing larger errors more heavily.
critical_citations:
  - "[Box & Jenkins, 1970] — Introduced ARIMA methodology foundational to time-series forecasting."
  - "[Kong et al., 2017] — Demonstrated LSTM effectiveness for short-term residential load forecasting."
  - "[Torres et al., 2022] — Showed deep LSTM with hyperparameter optimization achieves MAPE below 1.5%."
  - "[Chan & Yeo, 2024] — Proposed sparse attention Transformer that is 5x faster than RNN methods."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      justification: Reviews forecasting models (ARIMA, LSTM, Transformer) applicable to spending prediction.
    - code: 6.B
      name: Spending Forecasting Algorithm
      justification: Directly compares algorithm performance for time-series forecasting across horizons.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      justification: Documents error metrics (MAPE, RMSE, MAE) used to benchmark forecasting models.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: Compares multiple algorithms (statistical, ML, deep learning) under standardized metrics.
  contribution: This paper provides a systematic comparison of forecasting algorithms that directly informs Odin's spending forecasting module (6.B). The evaluation metrics and experimental protocols (MAPE, RMSE, cross-validation) are directly reusable for Odin's system evaluation framework (12.A). The analysis of hybrid models (e.g., SARIMA-ANN) offers a blueprint for combining interpretability with accuracy in Odin's budget recommendation algorithms (7.C). The discussion of data variability and model selection guides Odin's handling of irregular spending patterns and cold-start scenarios (5.B).
  directly_justifies:
    - "LSTM networks effectively learn complex temporal dependencies and can significantly improve forecasting accuracy over classical methods."
    - "Hybrid models combining statistical and machine learning outperform single models when linear and nonlinear structures cannot be separated."
    - "No single universal forecasting method exists; algorithm selection must match data characteristics and forecast horizon."
    - "Attention-based transformers achieve comparable accuracy to RNNs with up to 5x faster inference."
  limits:
    - "The paper focuses on electricity consumption, not personal financial spending; spending patterns may have different seasonality and drivers."
    - "Review synthesizes existing results without original empirical validation on financial data."
  mapping_rationale: "This paper is a review of forecasting methods for electricity consumption. The functional domains flagged were Spending Forecasting (6.A, 6.B) because the core subject is predictive modeling of time-series data, and System Evaluation (12.A, 12.B) because the paper extensively discusses error metrics and comparative benchmarks. Topics related to behavioral profiling (5.A-5.C), budgeting (7.A-7.C), anomaly detection (8.A-8.B), and other PFMS-specific domains were rejected because the paper does not address personal finance, user behavior, or financial transactions. Borderline topics like 7.B (Budget Recommendation) could be indirectly informed by forecasting accuracy, but the paper lacks any domain knowledge about budgeting strategies. The selected topics 6.A, 6.B, 12.A, and 12.B are directly supported by the paper's comparative analysis of algorithms and evaluation frameworks."
limitations:
  - "Review does not provide original empirical validation; all metrics are cited from primary studies."
  - "External variables (temperature, GDP) used in models are difficult to predict ex ante for operational forecasting."
  - "Electricity consumption patterns differ from personal spending; direct transferability to PFMS requires adaptation and validation."
remember_this:
  - "LSTM models improve forecasting RMSE by 10-15% over traditional methods."
  - "Transformer models achieve 5x faster inference than RNNs with comparable accuracy."
  - "No single universal forecasting method exists for all time horizons."
  - "Hybrid statistical-ML models outperform pure statistical or pure ML approaches."
  - "ARIMA remains highly effective for stable, seasonal data with limited external variables."
```