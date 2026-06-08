```yaml
paper_id: a1b2c3d4-e5f6-5123-89ab-cdef01234567
designation: local
title: WEKA-BASED DECISION-TREE MODEL FOR USER SUBSCRIPTION PLAN PREDICTION
authors: Guban, J. C. R.; Menderico, C. D. R.; Montalban, D. M. G.
year: 2025
venue: Unknown
odin_topics:
  - 5.A
  - 5.C
  - 6.A
  - 12.A
  - 12.B
shorthand_tags:
  - /behavioral-profile
  - /classification
  - /predictive-modeling
  - /evaluation
tldr: A J48 decision tree model predicts streaming subscription plans from user demographics and behaviors, achieving 72% accuracy with country as the strongest predictor.
problem_and_motivation: Streaming platforms lack interpretable models to understand how user attributes like age, device, and country jointly influence subscription plan selection. This gap hinders targeted marketing and plan optimization. The study addresses this by developing a transparent decision-tree classifier.
approach:
  - Used 2,500 anonymized user records with five attributes: country, age, gender, device type, subscription start month.
  - Applied J48 algorithm in WEKA with an 80/20 train-test split.
  - Evaluated using accuracy, Kappa statistic, precision, recall, F-measure, and ROC area.
  - Derived interpretable decision rules from the tree structure.
findings:
  - "num: 72% overall accuracy on the test set."
  - "num: Kappa statistic of 0.5797 indicates moderate agreement."
  - Country identified as most influential predictor, followed by age and device type.
  - Younger smartphone users subscribing later in the year tend to choose Premium plans in the US.
  - All United Kingdom users consistently select Standard plan regardless of attributes.
key_figures_tables:
  - "Table 1: Performance metrics including accuracy 72% → Model achieves solid predictive power."
  - "Table 3: Per-class precision, recall, F-measure, ROC area → Standard class performs best (ROC 0.871)."
  - "Table 4: Confusion matrix with diagonal counts 123,119,118 → Balanced classification across three plans."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: J48
    definition: An implementation of the C4.5 decision tree algorithm in WEKA.
  - term: WEKA
    definition: Waikato Environment for Knowledge Analysis, a machine learning software suite.
  - term: ROC
    definition: Receiver Operating Characteristic curve for classifier performance evaluation.
  - term: Kappa statistic
    definition: Measure of inter-rater agreement for classification tasks.
critical_citations:
  - "[Chaurasia & Pal, 2019] — Netflix subscription prediction using data mining."
  - "[Aouad et al., 2023] — Large decision trees generalize with proper validation."
  - "[Hsiao, 2023] — 70% accuracy benchmark for commercial applications."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      justification: Paper segments users into subscription plan profiles based on demographics.
    - code: 5.C
      name: Financial Behavioral Profile Classification Algorithm
      justification: J48 decision tree classifies user subscription choices as a proxy for financial behavior.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      justification: Predicts subscription plan choice using supervised learning.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      justification: Uses accuracy, precision, recall, and ROC area to assess model performance.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: Evaluates J48 tree via confusion matrix and per-class metrics.
  contribution: This paper demonstrates that an interpretable decision tree can predict user subscription plan choices from demographic and behavioral attributes, offering a template for Odin's user profiling module. The feature importance ranking (country, age, device) provides a heuristic for cold-start profiling when behavioral data is sparse. The evaluation methodology using multi-class metrics (precision, recall, ROC) directly informs Odin's algorithmic validation pipeline.
  directly_justifies:
    - A decision tree with 72% accuracy can reliably predict subscription plan from five user attributes.
    - Country is the strongest predictor of plan choice, explaining most variance.
    - Younger smartphone users are more likely to select premium plans when subscribing later in the year.
  limits:
    - Dataset limited to five attributes, excluding behavioral signals like watch time or frequency.
    - Model trained on streaming subscription data, not personal finance spending.
    - No cross-validation or hyperparameter tuning reported.
  mapping_rationale: This paper maps to behavioral profiling (5.A, 5.C) because it classifies users into discrete subscription plan categories based on attributes, analogous to financial behavior profiles. Predictive modeling (6.A) applies as it forecasts user choices. Evaluation frameworks (12.A, 12.B) are relevant due to detailed performance metrics. Topics related to budgeting, anomaly detection, and savings were rejected as the paper does not address those. Borderline case of 7.B (budget recommendation) was excluded because subscription plan prediction is not budget recommendation per se, though it could inform plan selection.
limitations:
  - Dataset limited to five user attributes, excluding behavioral indicators such as watch time or session frequency.
  - Only J48 algorithm tested; ensemble methods not explored.
  - Model not validated on a different dataset or in a real-time setting.
remember_this:
  - J48 decision tree predicts subscription plans with 72% accuracy.
  - Country is the strongest predictor, followed by age and device.
  - All United Kingdom users consistently choose Standard plan.
  - Younger smartphone users who subscribe late tend to pick Premium plans.
```