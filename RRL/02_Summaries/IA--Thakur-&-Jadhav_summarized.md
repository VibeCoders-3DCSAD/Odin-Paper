```yaml
paper_id: 10.14744/sigma.2025.00119
designation: algorithm-specific
title: Expense tracker management system using machine learning
authors: Thakur, R. S.; Jadhav, A.
year: 2025
venue: Sigma Journal of Engineering and Natural Sciences
odin_topics:
  - 6.A
  - 6.B
  - 12.A
  - 12.B
shorthand_tags:
  - /predictive-modeling
  - /spending-forecasting
  - /evaluation-frameworks
  - /algorithm-evaluation
tldr: Predicts future expenses using machine learning on household transaction data, finding a voting ensemble regressor achieves 78.11% R-squared.
problem_and_motivation: Manual expense tracking is time-consuming and error-prone, while existing apps lack predictive capabilities. There is a need for automated expense prediction to help users manage budgets. This paper addresses the gap by applying machine learning to forecast expenses from past spending patterns.
approach:
  - Dataset: Daily Household Transactions (date, mode, category, subcategory, note, amount, income/expense, currency).
  - Preprocessing: MinMax scaling, log1p transformation of amount, TF-IDF vectorization of text fields (min_df=3).
  - Models: Individual (XGBoost, Random Forest, SVM, MLP, KNN, Decision Tree, Extra Tree, CatBoost) and ensemble (bagging, boosting, stacking, voting, blending).
  - Evaluation: 70/30 train-test split, metrics R2, MAE, MSE, relative absolute error (RAE).
  - Baseline comparison across all models using hit-and-trial hyperparameter tuning.
findings:
  - num: XGBoost achieves R-squared of 77.89%, highest among individual models.
  - num: Voting ensemble regressor achieves highest R-squared of 78.11% and lowest relative absolute error of 0.1765.
  - Voting ensemble outperforms bagging, boosting, stacking, and blending.
  - RAE is the deciding factor due to similar R2 values across models.
key_figures_tables:
  - Table 2: Performance metrics of individual and ensemble models → Voting ensemble has highest R2 78.11%.
key_equations:
  - equation: R^2 = 1 - \frac{SS_{res}}{SS_{tot}}
    explanation: Proportion of variance explained by the model.
  - equation: MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|
    explanation: Average absolute prediction error.
  - equation: MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2
    explanation: Average squared prediction error.
  - equation: RAE = \frac{\sum_{i=1}^{n}|y_i - \hat{y}_i|}{\sum_{i=1}^{n}|y_i - \bar{y}|}
    explanation: Normalized measure of prediction accuracy.
definitions:
  - term: XGBoost
    definition: Extreme Gradient Boosting, an efficient sequential tree ensemble method.
  - term: Ensemble Learning
    definition: Combining multiple models to improve predictive performance.
  - term: R-squared
    definition: Coefficient of determination measuring model fit.
  - term: MAE
    definition: Mean Absolute Error, average magnitude of errors.
  - term: MSE
    definition: Mean Squared Error, average squared difference.
  - term: RAE
    definition: Relative Absolute Error, total absolute error relative to a simple predictor.
  - term: log1p
    definition: Natural logarithm of (1 + x), used to transform skewed amounts.
  - term: TF-IDF
    definition: Term frequency-inverse document frequency for text vectorization.
critical_citations:
  - "[Doan and Kalita, 2015] — Provides regression model selection methodology."
  - "[Odegua, 2019] — Empirical study of ensemble techniques (bagging, boosting, stacking)."
  - "[Mienye and Sun, 2022] — Survey of ensemble learning concepts and algorithms."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      justification: Benchmarks multiple ML models for expense prediction.
    - code: 6.B
      name: Spending Forecasting Algorithm
      justification: Voting ensemble regressor as a spending forecasting algorithm.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      justification: Uses R2, MAE, MSE, RAE to compare models.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: Systematic comparison of individual and ensemble regressors.
  contribution: The paper directly informs Odin's spending forecasting module by demonstrating that voting ensemble regression achieves 78.11% R2 for expense prediction. The evaluation metrics (R2, MAE, RAE) provide a benchmark for Odin's algorithmic evaluation framework. The preprocessing steps (log1p transformation, TF-IDF vectorization) are applicable to Odin's expense categorization and forecasting pipelines. The comparison of individual vs. ensemble methods guides algorithm selection for Odin's predictive modules.
  directly_justifies:
    - Voting ensemble regressor outperforms individual models for expense prediction on household transaction data.
    - XGBoost achieves 77.89% R-squared for expense forecasting, second only to voting ensemble.
    - Relative absolute error of 0.1765 is the lowest among all tested models.
    - Manual expense entry remains necessary in the proposed system.
  limits:
    - Dataset is specific to Indian household transactions; generalizability to Filipino young professionals is untested. [unacknowledged]
    - Rely on manual expense entry via forms; no automated bank synchronization. [acknowledged in future work]
    - No comparison with deep learning methods beyond MLP. [unacknowledged]
    - Evaluation metrics show small absolute differences; practical significance not discussed. [unacknowledged]
  mapping_rationale: The paper focuses on machine learning for expense prediction, directly supporting spending forecasting (6.A, 6.B). Its systematic evaluation of multiple models and metrics aligns with evaluation frameworks (12.A, 12.B). Topics related to behavioral profiling (5.A-5.C), budget recommendation (7.A-7.C), anomaly detection (8.A-8.B), and mobile design (9.A-9.B) are not addressed. Categorization (3.A) is mentioned only as a basic feature without novel framework, so excluded. The paper is algorithm-specific and international, hence designation algorithm-specific.
limitations:
  - Manual data entry required, no automatic transaction fetching. [acknowledged]
  - Limited to expense prediction; does not provide budget recommendations. [unacknowledged]
  - R2 values around 78% leave substantial unexplained variance. [unacknowledged]
  - No user study or real-world deployment evaluation. [unacknowledged]
remember_this:
  - Voting ensemble regressor achieves 78.11% R-squared for expense prediction.
  - XGBoost outperforms other individual models with 77.89% R2.
  - Manual expense entry remains a limitation of the system.
  - Preprocessing uses log1p and TF-IDF for financial text data.
  - Relative absolute error of 0.1765 is the best among all models.
```