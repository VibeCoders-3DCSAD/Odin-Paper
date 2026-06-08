```yaml
paper_id: "10.17559/TV-20220430111309"
designation: "international"
title: "An Overview of Forecasting Methods for Monthly Electricity Consumption"
authors: "Krstev, S.; Forcan, J.; Krneta, D."
year: 2023
venue: "Tehnički vjesnik (Technical Gazette)"
odin_topics:
  - "6.A"
  - "6.B"
  - "12.A"
shorthand_tags:
  - "/spending-forecasting"
  - "/forecast-algorithm"
  - "/eval-framework"
tldr: "Compares twelve forecasting methods for monthly electricity consumption, finding neural network autoregression (MAPE 2.67%) outperforms classical time series and machine learning methods."
problem_and_motivation: "Mid-term electricity consumption forecasting is crucial for energy companies but receives less research attention than short-term forecasting. The paper addresses the gap by systematically comparing classical statistical methods against modern machine learning approaches for monthly data. It also investigates whether machine learning provides equal accuracy to traditional time series methods when data is limited."
approach:
  - "Data from DSO in Bosnia and Herzegovina: monthly consumption (Jan 2000 – Mar 2020), 228 training months, 15 test months."
  - "Classical methods: seasonal naïve, ARIMA(1,0,1)(1,1,1), ETS(A,N,A), basic structural model with Kalman filter."
  - "Machine learning methods: linear regression, elastic net, KNN, random forest, XGBM, linear SVM, radial SVM, and neural network autoregression NNAR(3,1,6)."
  - "Feature selection using lm (t-test significance) and PCA on 24 lagged variables."
  - "Evaluation metric: mean absolute percentage error (MAPE); resampling via time-series cross-validation for some models."
findings:
  - "NNAR(3,1,6) achieved the lowest MAPE of 2.67%."
  - "num: ETS(A,N,A) gave MAPE 3.28%, ARIMA 3.36%, BSM 3.87%, seasonal naïve 4.16%."
  - "num: Among machine learning methods, PCA+KNN performed best with MAPE 4.38%."
  - "Classical time series methods generally outperformed most machine learning methods due to small sample size."
  - "For specific months (e.g., April and August 2019), ETS achieved absolute relative error below 1%."
key_figures_tables:
  - "Figure 4: Forecasts from SNAIVE, ARIMA, ETS, BSM → ETS tracks actual consumption most closely."
  - "Figure 8: Bar chart of MAPE by method → NNAR has lowest error, seasonal naïve highest."
  - "Table 2: Accuracy of ML methods with lm/PCA feature selection → PCA+KNN gives 4.38% MAPE."
  - "Table 3: Monthly absolute relative errors for ETS, PCA+KNN, NNAR → NNAR has smallest error for 9 of 15 months."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "MAPE"
    definition: "Mean absolute percentage error, measures forecast accuracy as average absolute percent deviation."
  - term: "ARIMA"
    definition: "Autoregressive integrated moving average, a classical time series model."
  - term: "ETS"
    definition: "Exponential smoothing state-space model (Error, Trend, Seasonal)."
  - term: "BSM"
    definition: "Basic structural model with trend, seasonal, and noise components estimated via Kalman filter."
  - term: "NNAR"
    definition: "Neural network autoregression, a feedforward network with lagged inputs."
critical_citations:
  - "[Makridakis et al., 2018] — statistical vs ML forecasting on univariate series."
  - "[Cerqueira et al., 2019] — sample size determines whether ML outperforms statistics."
relevance:
  topics:
    - code: "6.A"
      name: "Predictive Modeling in Personal Finance Systems"
      justification: "Compares forecasting algorithms (ARIMA, ETS, NNAR) applicable to spending prediction."
    - code: "6.B"
      name: "Spending Forecasting Algorithm"
      justification: "Evaluates neural network autoregression and classical time series for monthly forecasting."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      justification: "Uses MAPE and cross-validation to compare model performance, directly relevant to evaluating forecasting modules."
  contribution: "The paper provides a comparative benchmark of twelve forecasting methods, demonstrating that for small-sample monthly time series, classical methods (ETS, ARIMA) often outperform complex machine learning. This informs Odin's spending forecast module design: a hybrid approach using ETS for cold-start or low-data scenarios and NNAR when sufficient historical data accumulates. The rigorous evaluation framework (MAPE, rolling origin validation) sets a standard for assessing Odin’s predictive algorithms. Additionally, the finding that feature selection (PCA) improves ML accuracy guides preprocessing choices in the forecasting pipeline."
  directly_justifies:
    - "Neural network autoregression achieves 2.67% MAPE for monthly time series forecasting."
    - "ETS and ARIMA produce MAPE below 4% on monthly consumption data with 228 training points."
    - "Classical statistical methods are more accurate than machine learning when sample size is small."
    - "PCA feature selection improves MAPE for KNN from 6.34% to 4.38%."
  limits:
    - "Dataset is electricity consumption, not financial spending; behavioral and seasonal patterns may differ."
    - "Univariate forecasting only; Odin requires multivariate (income, past spending, user declarations)."
    - "Small sample size (228 months) limits generalizability to longer or more granular time series."
  mapping_rationale: "The paper is algorithm-focused, comparing forecasting methods and evaluation metrics. Domains screened: spending forecasting (6.A, 6.B) directly apply because the techniques (ARIMA, ETS, NNAR) are identical to those used in personal finance for predicting future expenditures. Evaluation frameworks (12.A) apply due to the use of MAPE and resampling validation. Behavioral profiling (5.A) and categorization (3.A) are irrelevant as no user behavior or expense labels are analyzed. Budget recommendation (7.A) and anomaly detection (8.A) are not addressed. The paper is international (no Philippine context), so local topics (1.A-2.C) are rejected. Borderline case: mobile-first design (9.A) and data privacy (10.A) are absent. Thus only 6.A, 6.B, and 12.A are selected."
limitations:
  - "Results based on a single utility’s data; may not generalize to other regions or consumption types."
  - "No multivariate or exogenous variables (e.g., weather, price) were included."
  - "The paper does not compare against state-of-the-art deep learning (e.g., LSTM) beyond basic NNAR."
  - "Small sample size may bias ML performance; acknowledged in discussion."
remember_this:
  - "NNAR achieved the lowest MAPE of 2.67% for monthly forecasting."
  - "Classical time series methods outperformed most machine learning methods on small datasets."
  - "MAPE below 4% is achievable with ETS and ARIMA for mid-term forecasting."
  - "PCA feature selection improved KNN MAPE from 6.34% to 4.38%."
```