```yaml
paper_id: 10.1080/13696998.2026.2630598
designation: international
title: Comparing deep learning and classical regression approaches for predicting healthcare expenditure and spending: a systematic review
authors: Lee, J. T.; Yeh, M. H.-S.; Li, V. C.-S.; Chen, H.-H.; Liu, Y.-H.; Chen, Y.-C.; Wu, D. B.-C.
year: 2026
venue: Journal of Medical Economics
odin_topics:
  - 6.A
  - 6.B
  - 7.B
  - 12.A
  - 12.B
shorthand_tags:
  - /predictive-modeling
  - /spending-forecast-algorithm
  - /budget-recommendation
  - /evaluation-frameworks
  - /algorithm-evaluation
tldr: A systematic review of eight studies finds that deep learning models, especially LSTM and CNN-LSTM, improve healthcare cost prediction accuracy by 10-20% for longitudinal data, while tree-based methods remain competitive for cross-sectional tabular data.
problem_and_motivation: Healthcare expenditures are rising globally, and accurate individual-level cost prediction is essential for insurance, budgeting, and value-based care. Traditional regression models struggle with nonlinear, high-dimensional, and temporal patterns in health data. This review systematically compares deep learning to classical regression to determine when neural networks add predictive value.
approach:
  - The review was preregistered (PROSPERO CRD420251129440) and searched Web of Science, PubMed, Embase, and Scopus through August 2025.
  - Eligible studies used real-world individual-level data (claims, EHR, registries) to predict cost outcomes with at least one deep learning architecture and one classical regression comparator.
  - Eight studies met inclusion criteria, spanning the US, Europe, and Asia, with sample sizes from 50,000 to over 1.4 million individuals.
  - Deep learning models included feedforward DNN, LSTM, stacked LSTM, CNN-LSTM, multi-view networks, and variance-based GAN.
  - Comparators included GLM, ridge, lasso, random forest, gradient boosting, and ARIMA.
  - Performance metrics included RMSE, MAE, R2, AUROC, precision@k, and cost-capture.
  - No study performed full external validation; most used internal train-validation-test splits or temporal holdouts.
findings:
  - num: Longitudinal deep learning models (LSTM, CNN-LSTM) achieved 10-20% reductions in RMSE/MAE compared to regression and tree-based baselines.
  - num: R2 improvements ranged from 0.01 to 0.15, with the highest gains in multi-year claims and medication spending forecasts.
  - num: AUROC for high-risk classification reached up to 0.78 in preventable cost prediction.
  - Prior costs and utilization were consistently the strongest predictors across all studies.
  - For cross-sectional, low-dimensional tabular data, shallow neural networks performed similarly to GLM and were often outperformed by random forests.
  - When unstructured or multimodal inputs (e.g., EMR text) were available, deep learning achieved clear advantages.
  - num: A multi-view DNN integrating structured and textual data reduced prediction error by 12-15% over baselines.
  - Stacked LSTM improved RMSE by nearly 19% over ARIMA for medication spending time series.
  - Recurrent neural networks increased test R2 from 0.14-0.17 to 0.30 for per-member-per-month expenditures.
  - num: CNN-LSTM ensembles achieved R2 values around 0.8-0.9 in patient-level forecasting.
key_figures_tables:
  - "Figure 2: Conceptual model performance by data complexity → Deep learning excels for longitudinal/multimodal data, tree-based for cross-sectional tabular."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: LSTM
    definition: Long short-term memory, a recurrent neural network architecture for sequential data.
  - term: CNN
    definition: Convolutional neural network, used for spatial or temporal feature extraction.
  - term: GLM
    definition: Generalized linear model, a flexible extension of linear regression.
  - term: RMSE
    definition: Root mean square error, a measure of prediction error.
  - term: MAE
    definition: Mean absolute error, a robust measure of prediction error.
  - term: AUROC
    definition: Area under the receiver operating characteristic curve, a discrimination metric.
  - term: R2
    definition: Coefficient of determination, proportion of variance explained.
critical_citations:
  - "[Drewe-Boss et al., 2022] — Deep neural network outperforms ridge regression in German claims."
  - "[Yang et al., 2018] — RNN improves R2 from 0.14 to 0.30 for Medicaid expenditures."
  - "[Kaushik et al., 2017] — Stacked LSTM reduces RMSE by 19% over ARIMA."
  - "[Lewis et al., 2021] — LSTM/CNN achieve AUROC 0.78 for preventable cost prediction."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      justification: Compares deep learning vs regression for cost/spending prediction.
    - code: 6.B
      name: Spending Forecasting Algorithm
      justification: Directly evaluates LSTM, CNN-LSTM for longitudinal spending forecasting.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      justification: Improved spending forecasts inform budget recommendations.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      justification: Systematic review defines evaluation metrics (RMSE, MAE, R2, AUC).
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: Benchmarks deep learning against classical and tree-based models.
  contribution: "This systematic review provides evidence that sequential deep learning models (LSTM, CNN-LSTM) reduce spending forecast error by 10-20% compared to linear models when historical transaction sequences are available. For Odin's spending forecasting module, this justifies adopting recurrent architectures over simpler regression for users with multi-month expense histories. The review also establishes that tree-based models remain strong baselines for cross-sectional or low-dimensional data, guiding Odin's model selection strategy. Finally, it highlights that prior spending and utilization are the strongest predictors, validating Odin's focus on historical transaction data."
  directly_justifies:
    - "LSTM and CNN-LSTM can reduce spending forecast error by 10-20% compared to linear regression models."
    - "R2 improvements of 0.01-0.15 are achievable when moving from linear to sequential deep learning."
    - "Prior spending amounts are the most important predictors for future expenditure."
    - "Shallow feedforward neural networks offer no advantage over GLM on cross-sectional tabular data."
    - "Tree-based methods (random forest, gradient boosting) remain competitive for non-temporal spending prediction."
  limits:
    - "Evidence based on only eight heterogeneous studies, limiting statistical generalizability."
    - "No external validation across independent datasets; all studies used single-database designs."
    - "Prediction horizons are mostly one year; long-term multi-year forecasting not well evaluated."
    - "Social determinants of health and behavioral predictors were rarely incorporated."
    - "Calibration and fairness analyses were largely absent. [unacknowledged]"
  mapping_rationale: "This paper maps primarily to Spending Forecasting (6.A, 6.B) because it directly compares algorithms for predicting individual-level expenditure from longitudinal data. Budget Recommendation (7.B) is relevant since accurate forecasts underpin budget suggestions. Evaluation Frameworks (12.A, 12.B) apply because the review systematically compares model performance metrics. Behavioral profiling (5.A-5.C) and anomaly detection (8.A,8.B) are not addressed. The paper is international (authors from Taiwan, Singapore) and not local to the Philippines, but the methodological insights transfer to Odin's spending prediction module."
limitations:
  - "Only eight studies included, with high heterogeneity in designs, populations, and outcomes."
  - "No external validation across independent datasets; temporal validation limited."
  - "Short prediction horizons (mostly one year) limit assessment of long-term dynamics."
  - "Social determinants and behavioral factors rarely incorporated. [unacknowledged]"
  - "Calibration and fairness not evaluated in any included study. [unacknowledged]"
remember_this:
  - "LSTM models reduce spending forecast error by 10-20% over linear regression."
  - "Prior spending history is the strongest predictor of future expenditure."
  - "Tree-based models match deep learning for cross-sectional tabular data."
  - "Deep learning gains emerge only with longitudinal or multimodal data."
  - "R2 improvements of 0.01 to 0.15 are typical for sequence-based forecasts."
```