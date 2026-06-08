```yaml
paper_id: "10.5281/zenodo.10049652"
designation: "local"
title: "Machine Learning Approaches in Classifying Income Levels"
authors: "Laspiñas, E. L.; Murcia, J. V. B."
year: 2024
venue: "TWIST"
odin_topics:
  - "12.A"
  - "12.B"
shorthand_tags: []
tldr: "Six machine learning classifiers for adult income classification are compared, with RandomForest and Random Tree achieving over 98% accuracy."
problem_and_motivation: "Conventional econometric models struggle to capture non-linear dynamics of income distribution. Machine learning offers a data-driven alternative to improve income level prediction accuracy. This study addresses the gap by systematically comparing multiple classifiers on a real-world dataset."
approach:
  - "Used Adult Income Prediction dataset from Kaggle with 16,281 observations and 13 features including age, occupation, education, and capital gain."
  - "Applied InfoGainAttributeEval and Ranker in Weka for feature selection, identifying 'Relationship' as most predictive."
  - "Evaluated Logistic, J48 (Decision Tree), RandomForest, Random Tree, IBk (k-NN), and NaiveBayes classifiers."
  - "Tuned J48 confidence factors (0.25, 0.50, 0.75) and k-NN k values (3,5,7,9)."
  - "Used 10-fold cross-validation to measure accuracy, precision, recall, F-measure, TP rate, and FP rate."
findings:
  - "num: RandomTree achieved highest accuracy at 98.37%, correctly classifying 16,016 instances."
  - "num: RandomForest achieved 98.35% accuracy with F-measure of 0.983."
  - "num: J48 accuracy improved from 87.21% (C=0.25) to 90.84% (C=0.75)."
  - "num: IBk accuracy decreased from 89.11% (k=3) to 85.74% (k=9), contradicting expected improvement with higher k."
  - "NaiveBayes had lowest accuracy at 82.24%."
  - "Ensemble methods (RandomForest, Random Tree) outperformed single classifiers due to reduced overfitting."
key_figures_tables:
  - "Table 2: Accuracy of six classifiers on training data → RandomTree and RandomForest near 98% accuracy."
  - "Table 3: F-measure and other metrics → RandomTree F-measure 0.984, RandomForest 0.983."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "ML"
    definition: "Machine learning"
  - term: "TP rate"
    definition: "True positive rate"
  - term: "FP rate"
    definition: "False positive rate"
  - term: "J48"
    definition: "Decision tree classifier in Weka"
  - term: "IBk"
    definition: "Instance-based k-nearest neighbor algorithm in Weka"
  - term: "k-NN"
    definition: "k-nearest neighbors"
critical_citations:
  - "[Alejandrino et al., 2023] — Showed k-NN parameter tuning effects."
  - "[Liaw & Wiener, 2002] — RandomForest ensemble method foundation."
relevance:
  topics:
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      justification: "Paper uses 10-fold cross-validation and multiple performance metrics applicable to PFMS evaluation."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      justification: "Compares classifier accuracy, F-measure, precision, recall for income prediction task."
  contribution: "This paper provides a systematic evaluation framework (12.A) using cross-validation and diverse metrics that Odin can adopt for testing its algorithmic modules. The comparison of six classifiers, including ensemble methods, directly supports Odin's need to select optimal algorithms for tasks like spending forecasting or anomaly detection (12.B). The findings on parameter tuning (confidence factor for decision trees, k for k-NN) inform best practices for Odin's model development and validation."
  directly_justifies:
    - "RandomForest and Random Tree achieve over 98% accuracy in binary classification tasks."
    - "Increasing confidence factor in J48 improves accuracy but risks overfitting."
    - "Smaller k values (k=3) yield higher k-NN accuracy for this dataset."
  limits:
    - "Dataset is US-based (Adult Income), not representative of Filipino young professionals."
    - "Paper does not address temporal or sequential spending data relevant to PFMS forecasting."
  mapping_rationale: "The paper focuses on comparing ML classifiers for income level classification, which has no direct link to most Odin domains (behavioral profiling, spending forecasting, budgeting, anomaly detection, savings/debt management). However, the evaluation methodology (12.A) and comparative algorithm performance metrics (12.B) are directly applicable to Odin's system evaluation needs. Topics like 5.C (financial profile classification) were rejected because the paper classifies income, not behavioral profiles. Borderline case 6.B (spending forecasting) was rejected as income is not spending. The paper's contribution is methodological for evaluation, hence selecting 12.A and 12.B."
limitations:
  - "The study only uses a single dataset (Adult Income) and does not test on Philippine data. [unacknowledged]"
  - "No comparison with deep learning methods like neural networks. [unacknowledged]"
  - "The paper does not address class imbalance or feature engineering beyond information gain. [unacknowledged]"
remember_this:
  - "RandomTree and RandomForest both exceeded 98% classification accuracy."
  - "Ensemble methods reduce overfitting and generalize better than single classifiers."
  - "Parameter tuning (confidence factor, k) significantly alters classifier performance."
```