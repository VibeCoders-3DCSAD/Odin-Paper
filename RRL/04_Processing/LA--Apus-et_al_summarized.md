```yaml
paper_id: a1b2c3d4-e5f6-4789-9a8b-7c6d5e4f3a2b
designation: algorithm-specific
title: Predicting the Filipino Household Income Using Naive Bayes Classification Algorithm
authors: Apus, J. O.; Mantalaba, K. D. V.; Mackno, A. J. B.; Bokingkito, P. B. Jr.
year: 0
venue: International Journal of Computing and Digital Systems
odin_topics:
  - 6.A
  - 12.B
shorthand_tags:
  - /predictive-modeling
  - /model-evaluation
tldr: Uses Naive Bayes on FIES data to predict Filipino household income classes, achieving 93% accuracy with bagging ensemble.
problem_and_motivation: Poverty reduction requires identifying vulnerable households. Existing studies use socio-demographic variables, but household expenditure and income variables remain unexplored for classification. This gap limits targeted interventions.
approach:
  - Data from 2018 FIES with 41,545 instances and 60 features.
  - Data cleaning handled missing values using mode for categorical, mean/median for numeric.
  - Feature selection used univariate chi-squared test, selecting 13 features with highest scores.
  - Labeled income classes into 7 brackets (Poor to Rich) based on monthly income.
  - Split data 80/20 train/test.
  - Implemented Naive Bayes with bagging and boosting ensembles using Python sklearn.
  - Evaluated using confusion matrix, precision, recall, F1, accuracy.
findings:
  - "num: Bagging ensemble achieved 93% accuracy, precision 0.93, recall 0.94, F1 0.94."
  - "num: Boosting ensemble achieved 89% accuracy."
  - Poor income class had most true positives; Rich class had fewest due to fewer instances.
  - Model with >80% accuracy is considered good per literature.
key_figures_tables:
  - "Table II: Standard income brackets for Philippine households → defines 7 classes."
  - "Table III: Selected features from univariate test → top feature is Total Food Expenditure (7.23)."
  - "Figure 3: Confusion matrix for bagging ensemble → high diagonal values indicate good classification."
  - "Figure 4: Confusion matrix for boosting ensemble → lower accuracy than bagging."
key_equations:
  - equation: "Precision = \\frac{TP}{TP+FP}"
    explanation: "True positives divided by all positive predictions."
  - equation: "Recall = \\frac{TP}{TP+FN}"
    explanation: "True positives divided by all actual positives."
  - equation: "F1 = 2 \\times \\frac{Precision \\times Recall}{Precision + Recall}"
    explanation: "Harmonic mean of precision and recall."
  - equation: "Accuracy = \\frac{TP+TN}{TP+TN+FP+FN}"
    explanation: "Correct predictions over total predictions."
definitions:
  - term: FIES
    definition: Family Income and Expenditure Survey by Philippine Statistics Authority.
  - term: Naive Bayes
    definition: Probabilistic classifier assuming feature independence.
  - term: Bagging
    definition: Bootstrap aggregating to reduce variance.
  - term: Boosting
    definition: Iterative method adjusting observation weights.
  - term: Precision
    definition: Ratio of true positives to predicted positives.
  - term: Recall
    definition: Ratio of true positives to actual positives.
  - term: F1-score
    definition: Weighted average of precision and recall.
  - term: Accuracy
    definition: Fraction of correct predictions.
critical_citations:
  - "[Liu et al., 2013] — Bayesian classifier optimization foundation."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      justification: Paper uses Naive Bayes to predict income classes from expenditure data.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: Reports accuracy, precision, recall, F1 for bagging and boosting.
  contribution: "This paper justifies using Naive Bayes for income classification in Odin's spending forecasting module. The bagging ensemble technique provides a reference accuracy baseline for evaluating predictive models. Feature selection via chi-squared test can inform Odin's expense categorization feature importance. The evaluation metrics (precision, recall, F1) offer a template for Odin's system evaluation framework."
  directly_justifies:
    - "Naive Bayes with bagging achieves 93% accuracy on household income prediction."
    - "Expenditure features like food and transportation are strong predictors of income class."
    - "Models with accuracy above 80% are acceptable for poverty targeting."
  limits:
    - "Only uses FIES data from 2018, not longitudinal."
    - "Does not include young professional-specific features."
    - "Income classes are broad; may not capture nuanced financial behavior."
    - "Naive Bayes assumes feature independence, which may not hold."
  mapping_rationale: "The paper was screened against Odin's functional domains. Predictive modeling (domain Spending forecasting) was flagged because the paper presents a classification algorithm for income prediction, which can inform spending power estimation. System evaluation (domain System evaluation) was flagged due to detailed accuracy metrics. Topics 1.B and 1.C were rejected because the paper focuses on general households, not specifically young professionals, and does not analyze financial behavior. Topic 6.B (spending forecasting) was rejected as the target is income class, not spending. Topic 7.B (budget recommendation) was considered but lacks direct budgeting application. Borderline case 5.A (behavioral profiles) was rejected because income class is a demographic label, not behavioral. Thus only 6.A and 12.B are selected."
limitations:
  - "Dataset only covers 2018, not updated annually. [unacknowledged]"
  - "Feature independence assumption of Naive Bayes may reduce real-world accuracy. [unacknowledged]"
  - "Only two ensemble methods tested; other algorithms not compared."
  - "No external validation on other datasets."
remember_this:
  - "Naive Bayes with bagging yields 93% accuracy for income classification."
  - "Food expenditure is the strongest predictor of income class."
  - "Seven income brackets from Poor to Rich are used."
  - "Models above 80% accuracy are considered good."
```