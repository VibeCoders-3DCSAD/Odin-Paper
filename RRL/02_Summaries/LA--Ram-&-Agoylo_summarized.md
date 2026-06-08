```yaml
paper_id: 10.54554/jtec.2025.17.02.004
designation: algorithm-specific
title: Optimized Random Forest Classifier for Students Lifestyle Prediction Using Behavioral Data: A Machine Learning Approach
authors: Ram, M. L.; Agoylo, J. C. Jr.
year: 2025
venue: Journal of Telecommunication, Electronic and Computer Engineering
odin_topics:
  - 5.C
  - 12.B
shorthand_tags:
  - /profile-classification
  - /algorithm-evaluation
tldr: Random Forest classifier predicts lifestyle categories from behavioral data with 75.07% accuracy, validated on 93 students.
problem_and_motivation: Machine learning for lifestyle classification remains underexplored despite its potential. Balancing accuracy and generalization is a key challenge. Parameter optimization is needed to mitigate overfitting in behavioral analytics.
approach:
  - Data source: Half a Million Lifestyle Dataset from Kaggle with 500,000 records.
  - Preprocessing removed missing values, selected 9 behavioral features, and encoded gender numerically.
  - Random Forest classifier trained with 40 decision trees to balance overfitting and generalizability.
  - Model evaluated using accuracy, precision, recall, and F1 score on a train-test split.
  - Real-world validation on 93 students via a Python-based input program with anonymous responses.
  - Oversampling and fairness metrics applied to mitigate classification bias.
findings:
  - "num: Accuracy of 75.07% on test data, with precision 75.16%, recall 75.07%, and F1 score 74.40%."
  - Training accuracy reaches 100% with 30+ trees, indicating overfitting despite strong memorization.
  - Testing accuracy stabilizes around 75% beyond 20 trees, with optimal tree count 30-40.
  - Real-world classification of 93 students: 41 Fitness Enthusiast, 50 Health-Conscious, 1 Eco-Friendly, 1 Social Media Influencer.
  - Model maintains 75.07% accuracy on real-world user inputs, matching test performance.
key_figures_tables:
  - "Figure 1: Causal paradigm linking behavioral patterns (independent) to lifestyle categories (dependent) → ML maps behavior to lifestyle."
  - "Figure 2: Random Forest classifier with multiple decision trees and majority voting → Ensemble method for lifestyle prediction."
  - "Figure 3: Accuracy vs number of trees shows training accuracy 100% after 30 trees, test accuracy ~75% → Overfitting observed beyond optimal tree count."
  - "Table 1: Performance metrics accuracy 0.7507, precision 0.7516, recall 0.7507, F1 0.7440 → Balanced classification performance."
  - "Table 2: Prediction results on 93 students show majority as Health-Conscious (50) and Fitness Enthusiast (41) → Most respondents exhibit active, health-aware behaviors."
key_equations:
  - equation: "Accuracy = (TP + TN) / (TP + TN + FP + FN)"
    explanation: "Proportion of correct predictions over total."
  - equation: "Precision = TP / (TP + FP)"
    explanation: "Correct positive predictions among all positive predictions."
  - equation: "Recall = TP / (TP + FN)"
    explanation: "Correct positive predictions among actual positives."
  - equation: "F1 Score = 2 * (Precision * Recall) / (Precision + Recall)"
    explanation: "Harmonic mean of precision and recall."
  - equation: "O(T * N * log N * F)"
    explanation: "Time complexity of Random Forest with T trees, N samples, F features."
definitions:
  - term: Random Forest (RF)
    definition: Ensemble of decision trees that votes by majority for classification.
  - term: TP
    definition: True positive – correctly predicted positive sample.
  - term: TN
    definition: True negative – correctly predicted negative sample.
  - term: FP
    definition: False positive – incorrectly predicted positive sample.
  - term: FN
    definition: False negative – incorrectly predicted negative sample.
critical_citations:
  - "[Jayaprakash et al., 2020] — Improved RF for academic performance prediction."
  - "[Chaturvedi et al., 2021] — Ensemble learning for student lifestyle query classification."
  - "[Nachouki et al., 2023] — RF for student grade prediction with feature importance analysis."
relevance:
  topics:
    - code: 5.C
      name: Financial Behavioral Profile Classification Algorithm
      justification: "Paper presents a Random Forest algorithm for classifying behavioral lifestyles, directly applicable to profile classification methods."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: "Provides accuracy, precision, recall, F1, and overfitting analysis for the classification module."
  contribution: "This paper offers a validated Random Forest classifier that Odin can adapt for financial behavioral profiling. Its parameter tuning approach (optimal tree count 30-40) directly informs how to balance overfitting and generalizability in Odin's classification modules. The evaluation framework with fairness metrics provides a template for assessing algorithmic modules. The real-world deployment on 93 students demonstrates a practical pipeline for user input collection and prediction, which Odin can replicate for mobile-first behavioral classification."
  directly_justifies:
    - "Random Forest achieves 75% accuracy on behavioral classification tasks with balanced precision and recall."
    - "Using more than 30-40 decision trees causes overfitting without improving test accuracy."
    - "Predefined lifestyle categories may not capture full behavioral complexity."
    - "Self-reported behavioral data introduces potential bias that requires mitigation techniques."
  limits:
    - "Predefined lifestyle categories (Fitness Enthusiast, Health-Conscious, etc.) may not generalize to financial behavior profiles."
    - "Self-reported data introduces response bias; no objective behavioral measurement."
    - "Real-world validation limited to 93 students from a single Philippine university."
    - "Model not tested on longitudinal or temporally varying behavioral data."
  mapping_rationale: "The paper was screened against Odin's functional domains. It does not address spending forecasting, budget recommendation, anomaly detection, expense categorization, mobile design, privacy, retention, savings, or debt management. It falls squarely under Behavioral Profiling & Classification (Domain 5) because it classifies individuals into lifestyle categories using behavioral features. Specifically, it provides a classification algorithm (5.C) with evaluation metrics (12.B). Topics 5.A (profiles themselves) and 5.B (profile dynamics) were rejected because the paper defines non-financial lifestyle categories and does not address cold-start or temporal dynamics. Borderline case: the algorithm could inform financial profile classification, so 5.C was retained."
limitations:
  - "Lifestyle categories are predefined and may not capture the full spectrum of individual behaviors."
  - "Self-reported behavioral data introduces potential bias. [unacknowledged]"
  - "Real-world test sample of 93 students is small and from a single institution, limiting generalizability. [unacknowledged]"
  - "No temporal validation or assessment of classification stability over time. [unacknowledged]"
remember_this:
  - "Random Forest accuracy of 75.07% on lifestyle prediction."
  - "Overfitting occurs with more than 30 decision trees."
  - "Optimal tree count between 30 and 40 balances accuracy and efficiency."
  - "Most students classified as health-conscious or fitness enthusiasts."
  - "Self-reported behavioral data requires bias mitigation."
```