```yaml
paper_id: 10.20944/preprints202603.1811.v1
designation: local
title: A Decade of Applied Quantitative Analytics for Philippine Policy: Forecasting, Statistical Forensics, and Predictive Modeling Across Education, Energy, Agriculture, Health, and Finance
authors: Velasco, A.
year: 2026
venue: Preprints.org
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 12.A
  - 12.B
shorthand_tags:
  - /predictive-modeling
  - /spending-forecasting
  - /anomaly-detection
  - /anomaly-detection-algorithm
  - /evaluation-frameworks
  - /evaluation-algorithmic
tldr: Reviews 17 Philippine policy analytics studies (2019-2025), showing progression from descriptive statistics and classical forecasting toward machine learning, deep learning, Benford-based anomaly detection, and explainable AI.
problem_and_motivation: Government resource allocation under uncertainty requires quantitative analytics, but no systematic review of applied methods in Philippine policy existed. Understanding methodological progress and gaps across education, energy, agriculture, health, and finance is necessary to guide future analytics infrastructure.
approach:
  - Structured narrative review of 17 studies from 2019-2025, coded by domain, dataset, modeling approach, validation strategy, and policy contribution.
  - Comparison with international literature on dropout research, electricity forecasting, crop-yield analytics, epidemiological surveillance, Benford auditing, and explainable ML.
findings:
  - Early studies use descriptive statistics and univariate ARIMA/SARIMA/Holt-Winters; later studies adopt comparative machine learning, neural networks, and LSTM.
  - Benford-based anomaly detection screens public health and agricultural data quality as a policy tool.
  - Validation rigor is uneven: some studies use holdout splits and error metrics, others rely on residual diagnostics due to short samples.
  - Interpretability appears via SHAP in diabetes prediction and theory-guided embedding in stock-index forecasting.
  - Random forests performed best for rice and corn forecasting; NNAR best for measles incidence.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: ARIMA
    definition: Autoregressive Integrated Moving Average, a classical time-series forecasting model.
  - term: SARIMA
    definition: Seasonal ARIMA, extending ARIMA with seasonal components.
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network for sequence prediction.
  - term: RMSE
    definition: Root Mean Square Error, a forecast accuracy metric.
  - term: MAE
    definition: Mean Absolute Error, a forecast accuracy metric.
  - term: MAPE
    definition: Mean Absolute Percentage Error, a scale-independent forecast accuracy metric.
  - term: SHAP
    definition: SHapley Additive exPlanations, a method for model interpretability.
  - term: NNAR
    definition: Neural Network AutoRegressive, a neural network for time series.
critical_citations:
  - "[Rumberger & Lim, 2008] — Foundational review of dropout causes."
  - "[Deyle & Sugihara, 2011] — Generalized theorems for nonlinear state-space reconstruction."
  - "[van Klompenburg et al., 2020] — Systematic review of crop yield prediction ML."
  - "[World Health Organization, 2021] — Routine health data monitoring during COVID-19."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      justification: Reviews forecasting methods (ARIMA, ML, LSTM) applicable to spending prediction.
    - code: 6.B
      name: Spending Forecasting Algorithm
      justification: Compares classical and machine learning forecast models for time-series policy problems.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      justification: Benford-based statistical forensics detects data anomalies in health and agriculture.
    - code: 8.B
      name: Anomaly Detection Algorithm
      justification: Newcomb-Benford analysis provides a low-cost screening mechanism for unusual patterns.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      justification: Discusses validation practices including holdout splits, error metrics, and benchmarking.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: Compares model performance (RMSE, MAE, MAPE) across sectors and methods.
  contribution: The paper validates that Odin's spending forecasting module should support both classical time-series baselines (ARIMA, SARIMA) and machine learning benchmarks (random forests, LSTM) for robustness. It justifies including a Benford-based anomaly detection module to screen transaction or aggregate data for quality issues before analysis. The review also informs Odin's evaluation framework by emphasizing transparent validation (holdout sets, error metrics) and the need for uncertainty quantification.
  directly_justifies:
    - "Forecasting performance improves when nonlinear models like LSTM are compared against linear ARIMA baselines."
    - "Benford-based anomaly detection can screen routine data for unusual reporting behavior at low cost."
    - "Validation for time-series forecasting should use holdout splits or rolling-origin evaluation, not only residual diagnostics."
    - "Interpretability methods like SHAP make predictive models more actionable for users."
  limits:
    - "Paper reviews general policy analytics, not personal finance specifically."
    - "No direct evaluation of user-facing PFMS algorithms or behavioral profiling."
    - "Quantitative performance numbers are not reported in this review, only comparative statements."
  mapping_rationale: The paper strongly supports forecasting (domains 6.A,6.B) through extensive discussion of ARIMA, SARIMA, Holt-Winters, random forests, neural networks, and LSTM applied to time-series problems. Anomaly detection (8.A,8.B) is directly addressed via Newcomb-Benford analysis for health and agricultural data. Evaluation frameworks (12.A,12.B) appear throughout the validation comparisons. Topics related to behavioral profiling (5.A-5.C), budgeting (7.A-7.C), expense categorization (3.A-3.B), mobile design (9.A-9.B), privacy (10.A-10.B), retention (11.A-11.B), and savings/debt (13.A-13.B) have no coverage and were rejected. The paper is a review, not an algorithm-specific study, so designation is local due to Philippine institutional affiliation.
limitations:
  - "Corpus is heterogeneous (journal articles, preprints, SSRN papers) with differing data frequencies, sample sizes, and validation maturity."
  - "Some study characteristics had to be reconstructed from metadata when full texts were not equally accessible. [unacknowledged]"
  - "Direct numerical comparison across sectors is neither appropriate nor intended by the author."
  - "External validation and operational deployment evidence are largely absent from the reviewed studies. [unacknowledged]"
remember_this:
  - "Reviewed 17 Philippine policy analytics studies from 2019 to 2025."
  - "Forecasting evolved from ARIMA to machine learning and LSTM."
  - "Benford's law detects anomalies in health and agricultural data."
  - "Validation practices remain uneven across sectors."
  - "Interpretability via SHAP is a growing priority."
```