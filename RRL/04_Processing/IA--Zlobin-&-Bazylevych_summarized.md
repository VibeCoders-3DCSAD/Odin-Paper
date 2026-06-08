```yaml
paper_id: 10.25140/2411-5363-2025-1(39)-184-195
designation: international
title: Systematic review of deep and machine learning for financial modeling
authors: Zlobin, M.; Bazylevych, V.
year: 2025
venue: Technical Sciences and Technologies
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 11.A
  - 11.B
  - 12.A
  - 12.B
shorthand_tags:
  - /predictive-modeling
  - /spending-forecast
  - /anomaly-detection
  - /anomaly-algorithm
  - /engagement
  - /retention
  - /eval-framework
  - /eval-algorithm
tldr: Systematic review of 41 papers on ML/DL for financial classification and regression tasks including credit scoring, fraud detection, stock prediction, and anomaly detection.
problem_and_motivation: Financial institutions face datasets that traditional analytical methods cannot process effectively. ML and DL offer improved predictive accuracy but challenges like model interpretability, data quality, and concept drift remain. A systematic synthesis of state-of-the-art methods is needed to identify gaps and guide future research.
approach:
  - Review of 41 peer-reviewed papers on ML/DL applications in finance published up to 2025.
  - Focus on classification tasks (credit scoring, fraud detection, customer segmentation) and regression tasks (stock price prediction, volatility forecasting, option pricing).
  - Comparative analysis of model performance using metrics such as AUC, RMSE, accuracy, precision, recall, and F1-score.
  - Evaluation of traditional ML (logistic regression, decision trees, SVM, random forest, XGBoost) and DL (DBN, CNN, LSTM, GRU, GCN) architectures.
  - Identification of challenges including data quality, model interpretability, fairness, and computational complexity.
findings:
  - "num: Random forest with ensemble feature selection achieved 99.6% accuracy and 100% precision in credit card fraud detection."
  - "num: XGBoost consistently outperformed deep neural networks across 10 credit scoring datasets, achieving highest AUC and efficiency."
  - "num: CNN reduced fraud detection cost of failure by 30% and achieved 87.64% AUC on European dataset."
  - "num: GCN achieved 94.5% fraud detection accuracy, outperforming CNN (93%) by improving recall by 10% via graph-based user relationship analysis."
  - "num: AI personalization increased user engagement by 27%, customer retention by 15%, and conversion rates by 20% in fintech applications."
  - "num: MyFinanceAI pilot with 1,000 users showed 22% increase in monthly savings and 30% improvement in expense forecasting accuracy using LSTM."
  - "num: GRU-CA hybrid model reduced anomaly detection RMSE from 13.28 to 9.74 on S&P 500 data."
  - "num: LSTM achieved 93% accuracy in predicting Vietnamese stock price trends, outperforming linear regression."
  - "num: Hybrid CNN-AdaBoost achieved 96.35% accuracy in electricity theft detection, outperforming standalone models."
  - "num: Achieving perfect fairness in credit scoring would reduce profitability by over 35%, while reducing fairness violations below 0.2 threshold costs only 4.91% profit loss."
key_figures_tables:
  - "Table 1: Comparative analysis of ML/DL models in financial applications → DBN outperforms shallow networks; XGBoost best for credit scoring; random forest 99.6% fraud accuracy."
  - "Table 2: Comparative analysis for option pricing and anomaly detection → BS-ANN lowest pricing error; GRU-CA reduces RMSE from 13.28 to 9.74."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: ML
    definition: Machine learning, algorithms that learn from data without explicit programming.
  - term: DL
    definition: Deep learning, neural networks with multiple hidden layers for complex pattern recognition.
  - term: CNN
    definition: Convolutional neural network, effective for spatial pattern detection in structured data.
  - term: LSTM
    definition: Long short-term memory, recurrent neural network that captures long-term temporal dependencies.
  - term: GCN
    definition: Graph convolutional network, operates on graph-structured data for relationship-aware learning.
  - term: GRU
    definition: Gated recurrent unit, simplified RNN variant that addresses vanishing gradient.
  - term: RMSE
    definition: Root mean square error, standard metric for regression prediction accuracy.
  - term: AUC
    definition: Area under ROC curve, metric for binary classification performance.
  - term: XGBoost
    definition: Extreme gradient boosting, ensemble tree method known for high performance.
critical_citations:
  - "[Gunnarsson et al., 2021] — Deep learning not superior to XGBoost for credit scoring."
  - "[Kozodoi et al., 2021] — Fairness-profit tradeoff quantified in credit scoring."
  - "[Raghavan & Gayar, 2019] — CNN cost reduction in fraud detection."
  - "[Jiang et al., 2019] — GCN outperforms CNN for fraud detection via graph structures."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      justification: Reviews ML/DL models for forecasting financial outcomes.
    - code: 6.B
      name: Spending Forecasting Algorithm
      justification: Cites LSTM improving expense forecasting accuracy by 30% in MyFinanceAI.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      justification: Surveys fraud detection and financial anomaly detection methods.
    - code: 8.B
      name: Anomaly Detection Algorithm
      justification: Compares GCN, GRU-CA, random forest for anomaly detection performance.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      justification: Reports 27% engagement increase from AI personalization in fintech.
    - code: 11.B
      name: Retention Mechanisms and Engagement Design
      justification: Documents 15% retention lift from personalized financial recommendations.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      justification: Uses AUC, RMSE, accuracy, F1-score to compare model performance.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: Provides comparative benchmarks across multiple models and datasets.
  contribution: "This systematic review provides Odin with a benchmark comparison of ML and DL models applicable to spending forecasting, anomaly detection, and user engagement optimization. It validates that XGBoost often outperforms deep learning for credit risk classification, while LSTM and GRU excel at time-series forecasting for expense prediction. The review also quantifies the impact of AI personalization on user retention and engagement, directly informing Odin's retention mechanism design. Finally, it identifies interpretability and fairness challenges that Odin must address when deploying black-box models."
  directly_justifies:
    - "Random forest with ensemble feature selection achieves 99.6% accuracy for fraud detection, suitable for Odin anomaly detection."
    - "LSTM improves expense forecasting accuracy by 30% over traditional regression models."
    - "AI personalization increases user engagement by 27% and retention by 15% in personal finance apps."
    - "Achieving perfect fairness in credit scoring reduces profitability by over 35%, a trade-off Odin must consider."
    - "GRU-CA reduces anomaly detection RMSE by 27% compared to baseline RNN."
  limits:
    - "Review synthesizes existing literature but does not present original experiments on Filipino young professional data."
    - "Most cited studies use non-Philippine datasets (European, US, Chinese, Vietnamese), limiting direct generalizability."
    - "Fairness-profit tradeoffs are quantified for credit scoring, not for spending forecasting or budgeting recommendations."
  mapping_rationale: "This systematic review spans multiple financial ML/DL applications. The domain screen flagged spending forecasting (6.A,6.B) due to LSTM expense prediction results, anomaly detection (8.A,8.B) due to fraud detection benchmarks, user engagement (11.A,11.B) due to personalization lift statistics, and evaluation frameworks (12.A,12.B) due to comparative model metrics. Topics 3.A (expense categorization) were rejected because the paper does not address category taxonomies. Topics 5.A (behavioral profiling) were rejected as no user clustering or profile dynamics are analyzed. Topics 7.A (budgeting strategies) were rejected because budget recommendation algorithms are not discussed. The paper's findings directly justify Odin's choice of XGBoost over deep learning for certain classification tasks and LSTM for spending forecasting, while highlighting the need for explainable AI in regulated environments."
limitations:
  - "Review primarily cites papers up to 2024; rapid ML/DL advances may render some comparisons outdated. [unacknowledged]"
  - "Performance metrics are aggregated across heterogeneous datasets, making direct apples-to-apples comparisons difficult. [unacknowledged]"
  - "The review does not address computational resource constraints of mobile-first deployment, which is critical for Odin. [unacknowledged]"
  - "Concept drift in financial data is mentioned as a challenge but no longitudinal model updating strategies are evaluated. [acknowledged]"
remember_this:
  - "XGBoost outperforms deep learning for credit scoring across 10 datasets."
  - "Random forest achieves 99.6% fraud detection accuracy with feature selection."
  - "AI personalization lifts user engagement by 27% and retention by 15%."
  - "LSTM improves expense forecasting accuracy by 30% over regression."
  - "Perfect fairness in scoring would cut profitability by over 35%."
```