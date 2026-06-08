```yaml
paper_id: 10.1016/j.sctalk.2024.100387
designation: local
title: When machine learning meets econometrics: Can it build a better measure to predict multidimensional poverty and examine unmeasurable economic conditions?
authors: Onsay, E. A.; Rabajante, J. F.
year: 2024
venue: Science Talks
odin_topics:
  - 12.A
  - 12.B
shorthand_tags:
  - /evaluation-frameworks
  - /algorithm-evaluation
tldr: Random forest outperforms econometric and other ML models in predicting multidimensional poverty for indigenous communities in the Philippines, achieving 0.9208 R-squared and 95.94% accuracy.
problem_and_motivation: Traditional poverty measurement methods are costly, labor-intensive, and time-consuming, making it difficult for policymakers to target interventions. Indigenous communities face complex, multifaceted socioeconomic conditions that generic poverty research fails to capture. There is a need for disaggregated, cost-effective methods to measure multidimensional poverty.
approach:
  - Data comes from a complete census of indigenous communities in Goa, Camarines Sur, Philippines (1,660 indigenous households, 8,022 persons).
  - Blends econometric causality tests (logit and probit) with ML models including random forest, LightGBM, XGBoost, SVM, and linear regression.
  - Uses 15 multidimensional indicators (health, housing, water, education, income, peace/order) as predictors of poverty.
  - Evaluates regressors using RMSE, MSE, and R-square; classifiers using accuracy.
  - Benchmarks random forest against linear regression, decision tree, bagging, AdaBoost, GaussianNB, and perceptron.
findings:
  - "num: Random forest regressor achieved the highest R-square of 0.92075 for impoverished societies."
  - "num: Random forest classifier attained 95.94% accuracy in pipeline algorithms and 90.69% at random."
  - "num: Random forest had the lowest RMSE (0.3298) compared to LightGBM (0.3642) and XGBoost (0.4001)."
  - "num: For indigenous communities, random forest R-square was 0.9208 and MSE 0.5497."
  - "num: 82% of indigenous people live in poverty and 71% lack food access."
  - Random forest identifies explanatory factors, nonlinear correlations, and feature importance driving poverty classification.
  - Econometric tests confirmed causal relationships between the 15 predictors and poverty outcomes.
key_figures_tables:
  - "Figure 4: RMSE comparison of ML regressors → Random forest lowest (0.3298)."
  - "Figure 6: R-square of ML regressors → Random forest highest (0.92075)."
  - "Figure 7: Accuracy of ML classifiers → Random forest highest (95.94% pipeline)."
  - "Figure 12: MSE for indigenous communities → Random forest lowest (0.5497)."
  - "Figure 13: R-square for indigenous communities → Random forest highest (0.9208)."
  - "Figure 14: Accuracy for indigenous tribes → Random forest highest (90.69% random, 94.89% pipeline)."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: ML
    definition: Machine learning
  - term: RMSE
    definition: Root mean square error
  - term: MSE
    definition: Mean square error
  - term: IP
    definition: Indigenous people
critical_citations:
  - "[Onsay & Rabajante, 2024] — Provides the dataset and poverty measurement approach."
  - "[Hastie et al., 2009] — Foundational ML methods used in the paper."
  - "[Alkire, 2005] — Capability approach for multidimensional poverty."
relevance:
  topics:
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      justification: Paper benchmarks multiple ML models using RMSE, MSE, R-square, and accuracy.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: Compares random forest against LightGBM, XGBoost, linear regression, and others.
  contribution: The paper provides a comparative evaluation framework that Odin can adopt for assessing spending forecasting algorithms. It demonstrates that random forest outperforms linear regression and gradient boosting methods on regression and classification metrics. The use of RMSE, R-square, and accuracy as primary evaluation metrics directly maps to Odin's need for algorithmic module assessment. The paper's approach of combining econometric causality tests with ML validation can inform Odin's model selection pipeline.
  directly_justifies:
    - "Random forest achieves higher R-square (0.9208) than linear regression (0.4221) for prediction tasks."
    - "Random forest classification accuracy reaches 95.94% in pipeline algorithms."
    - "RMSE for random forest is 0.3298, lower than LightGBM (0.3642) and XGBoost (0.4001)."
    - "Feature importance from random forest identifies key predictors for targeted interventions."
  limits:
    - "Paper focuses on poverty prediction, not personal financial spending patterns."
    - "Models were trained on census data from a single Philippine municipality, limiting direct transferability to PFMS contexts."
    - "No comparison with deep learning methods like neural networks."
  mapping_rationale: The paper was screened against all Odin functional domains. It does not address behavioral profiling, spending forecasting, budget recommendation, anomaly detection, expense categorization, mobile design, data privacy, user retention, or savings/debt management. However, its extensive comparison of ML algorithms using standard regression and classification evaluation metrics (RMSE, MSE, R-square, accuracy) directly supports topics 12.A (Evaluation Frameworks) and 12.B (Evaluation of Algorithmic Modules). Borderline consideration of topic 6.B (Spending Forecasting Algorithm) was rejected because the paper predicts poverty status rather than spending amounts or patterns. Thus only the two evaluation-related codes are included.
limitations:
  - "Results are specific to rural poverty in the Philippines; generalizability to other domains like personal finance is untested [unacknowledged]."
  - "Paper acknowledges time required to build trustworthy datasets but does not discuss real-time prediction constraints."
  - "Models rely on census data updated every two years, which may not capture rapid changes in financial behavior [unacknowledged]."
remember_this:
  - Random forest achieved 0.9208 R-square for poverty prediction.
  - Random forest classifier accuracy was 95.94% in pipeline algorithms.
  - Random forest had the lowest RMSE (0.3298) among regressors.
  - Feature importance from random forest identifies key poverty predictors.
```