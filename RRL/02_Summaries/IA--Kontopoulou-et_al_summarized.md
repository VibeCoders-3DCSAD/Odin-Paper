```yaml
paper_id: 10.3390/fi15080255
designation: international
title: A Review of ARIMA vs. Machine Learning Approaches for Time Series Forecasting in Data Driven Networks
authors: Kontopoulou, V. I.; Panagopoulos, A. D.; Kakkos, I.; Matsopoulos, G. K.
year: 2023
venue: Future Internet
odin_topics:
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 8.A
  - 8.B
  - 12.A
  - 12.B
shorthand_tags:
  - /spending-forecast
  - /budget-recommendation
  - /anomaly-detection
  - /evaluation-framework
tldr: A review comparing ARIMA statistical models with machine learning and hybrid approaches for time series forecasting across finance, health, weather, utilities, and network applications.
problem_and_motivation: The scientific literature lacks an extensive summary comparing ARIMA with machine learning and deep learning time series forecasting methods. Although machine learning models are increasingly used, their claimed superiority over classical statistical methods is not always systematically evaluated. This review addresses that gap by synthesizing comparative studies across multiple application domains.
approach:
  - Reviewed published literature comparing ARIMA with SVM, decision tree, deep learning (LSTM, GRU, CNN), and hybrid models.
  - Organized findings by application domain: finance (bitcoin, stocks), healthcare (COVID-19 cases), weather (wind, drought), utilities (energy, water), and network traffic.
  - Extracted performance metrics including RMSE, MAPE, MAE, MSE, R2, NSE from each comparative study.
  - Evaluated conditions under which ARIMA outperforms ML models, such as small datasets, linear patterns, or seasonal univariate series.
findings:
  - Machine learning and deep learning models generally outperform ARIMA in time series forecasting across most applications reviewed.
  - num: Deep learning models (LSTM, GRU) achieved RMSE values up to 40 times smaller than ARIMA for COVID-19 case forecasting in several countries (Arun Kumar et al., 2022).
  - num: ARIMA outperforms machine learning models for small datasets, limited value ranges, or strongly linear and seasonal univariate series (e.g., drought forecasting with R2 >0.9 vs. SVM's 0.83).
  - Hybrid models combining ARIMA with machine learning (e.g., ARIMA-SVM, ARIMA-NARNN, ARIMA-CNN) consistently outperform both individual approaches.
  - The optimal forecasting method depends on dataset characteristics: linearity, seasonality, sample size, and geographic region.
key_figures_tables:
  - Table 2: Summary of ARIMA vs. SVM comparison studies → SVM often outperforms ARIMA except for linear or drought data.
  - Table 4: Summary of ARIMA vs. deep learning studies → LSTM generally better but ARIMA wins for small or seasonal univariate data.
  - Table 5: Summary of ARIMA vs. hybrid models → Hybrid models always outperform pure ARIMA.
  - Table 6: Advantages and disadvantages of ARIMA vs. AI for forecasting → ARIMA is explainable, low complexity, suitable for small data; AI needs large data, more compute.
key_equations:
  - equation: MSE = (1/N) * Σ(y_t - ŷ_t)^2
    explanation: Mean squared error for forecast accuracy.
  - equation: MAPE = (1/N) * Σ|(y_t - ŷ_t)/y_t|
    explanation: Mean absolute percentage error.
  - equation: ∇^d x_t = c + Σφ_i ∇^d x_{t-i} + Σθ_i ε_{t-i}
    explanation: General ARIMA model with differencing.
definitions:
  - term: ARIMA
    definition: AutoRegressive Integrated Moving Average, a statistical time series forecasting model.
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network for sequential data.
  - term: GRU
    definition: Gated Recurrent Unit, a simplified recurrent neural network.
  - term: RMSE
    definition: Root Mean Square Error, a forecast accuracy metric.
  - term: MAPE
    definition: Mean Absolute Percentage Error, a scale-independent accuracy metric.
critical_citations:
  - "[Zhang, 2003] — Proposed hybrid ARIMA-ANN framework for linear and nonlinear modeling."
  - "[Box & Jenkins, 2015] — Classic text defining ARIMA methodology."
  - "[Makridakis et al., 2018] — Highlighted concerns about ML forecasting without baseline comparisons."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      justification: Reviews forecasting methods directly applicable to spending prediction.
    - code: 6.B
      name: Spending Forecasting Algorithm
      justification: Compares ARIMA and ML models for time series forecasting, informing algorithm choice.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      justification: Forecasting accuracy underpins budget recommendation strategies.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      justification: Findings on ML superiority guide budget algorithm selection.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      justification: Includes anomaly detection study (Priyadarshini et al.) where ARIMA outperformed others.
    - code: 8.B
      name: Anomaly Detection Algorithm
      justification: ARIMA and SARIMA shown effective for anomaly detection in time series.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      justification: Paper catalogs error metrics (RMSE, MAPE, MAE) for model evaluation.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: Comparative performance assessment of forecasting algorithms.
  contribution: This review informs Odin's spending forecasting module (6.A/6.B) by establishing that LSTM and hybrid models generally outperform ARIMA, but ARIMA remains viable for small datasets or linear spending patterns. For budget recommendation (7.A/7.B), the review suggests that hybrid ARIMA-ML models provide the highest accuracy. The evaluation framework (12.A/12.B) can adopt the standardized metrics (RMSE, MAPE, MAE) used across reviewed studies. For anomaly detection (8.A/8.B), the paper highlights cases where ARIMA excels, offering a baseline for detecting irregular transactions.
  directly_justifies:
    - Machine learning models generally provide more accurate time series forecasts than ARIMA for non-linear spending data.
    - Hybrid ARIMA-ML models consistently outperform pure ARIMA or pure ML models in forecasting tasks.
    - ARIMA is preferable for small datasets or when spending patterns are linear and seasonal.
    - Evaluation of forecasting models should use multiple metrics including RMSE, MAPE, and MAE.
  limits:
    - Review based on selected studies; comprehensive meta-analysis not performed.
    - Primary focus on univariate forecasting; multivariate spending patterns less covered.
    - Real-time or online learning considerations for personal finance apps not addressed.
  mapping_rationale: This paper directly supports Odin's spending forecasting (6.A,6.B) and budget recommendation (7.A,7.B) domains because time series forecasting of financial variables is core to those modules. The comprehensive comparison of ARIMA, machine learning, and hybrid models provides actionable guidance for algorithm selection. Evaluation frameworks (12.A,12.B) are supported through detailed discussion of error metrics. Anomaly detection (8.A,8.B) was included due to one cited study on smart home IoT where ARIMA outperformed, though the paper does not focus on anomalies. Topics related to behavioral profiling (5.A-C) and savings/debt (13.A,B) were rejected because the paper does not address user behavior or financial goal management.
limitations:
  - ARIMA parameter selection depends on forecaster skill and experience.
  - Machine learning models require large datasets and higher computational resources. [unacknowledged]
  - Review does not cover real-time forecasting requirements for mobile personal finance applications. [unacknowledged]
  - Paper does not address data privacy or user trust implications of ML models. [unacknowledged]
remember_this:
  - Machine learning outperforms ARIMA for most non-linear time series.
  - Hybrid ARIMA-ML models always beat either method alone.
  - ARIMA works best for small, linear, or seasonal univariate data.
  - RMSE values for deep learning can be 40 times lower than ARIMA for some tasks.
```