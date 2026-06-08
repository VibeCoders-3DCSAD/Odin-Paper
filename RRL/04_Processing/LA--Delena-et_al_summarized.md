```yaml
paper_id: "10.1016/j.sasc.2025.200352"
designation: "local"
title: "Predicting student retention: A comparative study of machine learning approach utilizing sociodemographic and academic factors"
authors: "Delen˜a, R. D.; Diab, N. J.; Sacayan, R. R.; Sieras, J. C.; Khalid, S. A.; Macatotong, A. H. T.; Gulam, S. B."
year: 2025
venue: "Systems and Soft Computing"
odin_topics:
  - "12.A"
  - "12.B"
shorthand_tags:
  - "/evaluation-framework"
  - "/algorithm-evaluation"
tldr: "A comparative study of ten machine learning algorithms predicts student retention using sociodemographic and academic data from a Philippine university, with XGBoost achieving highest accuracy."
problem_and_motivation: "Student dropout is a persistent challenge in higher education, especially in developing regions with limited resources for intervention. Traditional approaches based on subjective assessments are insufficient to capture attrition complexity. There is a need for accurate predictive models using machine learning on institutional data."
approach:
  - "Data from Mindanao State University (482 students, 146 variables over 2012–2022) was preprocessed using CRISP-DM and Power BI."
  - "Ten algorithms were evaluated: XGBoost, Gradient Boosting, ANN, Decision Tree, Random Forest, MLP, Logistic Regression, KNN, SVM, and Naïve Bayes."
  - "Models were assessed with train-test split and 5-fold cross-validation using accuracy, precision, recall, F1, MSE, and log loss."
  - "Multicollinearity was reduced via Spearman correlation with a 0.7 threshold, retaining 79 features."
findings:
  - "num: XGBoost achieved 90.66% cross-validated accuracy and 90.72 F1 score, outperforming all other models."
  - "num: Gradient Boosting had 89.42% accuracy and the lowest log loss (0.25), while ANN reached 88.39% accuracy and 91.48% recall."
  - "Naïve Bayes had high recall (97.21%) but excessive false positives (31), limiting practical use."
  - "Decision Tree overfitted, dropping from 90.34% to 84.44% accuracy after cross-validation."
  - "XGBoost produced the lowest misclassifications: 4 false negatives and 5 false positives."
key_figures_tables:
  - "Figure 2: Literature review frequency of factors, models, and metrics → gender and decision trees are most common."
  - "Figure 6: Confusion matrices for all ten models → XGBoost has the most balanced predictions."
  - "Table 6: Dropout detection rates → XGBoost achieved 94.5% recall, highest among models."
  - "Figure 7: 5-fold cross-validation results → XGBoost remains top performer across all metrics."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "EDM"
    definition: "Educational Data Mining, applying ML to institutional data to predict student outcomes."
  - term: "XGBoost"
    definition: "Extreme Gradient Boosting, an optimized gradient boosting algorithm with regularization."
  - term: "CRISP-DM"
    definition: "Cross-Industry Standard Process for Data Mining, a six-phase methodology for data projects."
  - term: "MLP"
    definition: "Multilayer Perceptron, a feedforward artificial neural network with multiple hidden layers."
critical_citations:
  - "[Baker & Yacef, 2009] — Foundational review of educational data mining."
  - "[Romero & Ventura, 2020] — Updated survey of EDM and learning analytics."
  - "[Niyogisubizo et al., 2022] — Stacked ensemble for dropout prediction with XGBoost."
relevance:
  topics:
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      justification: "Paper compares ten ML algorithms using multiple metrics and cross-validation, providing a template for evaluating PFMS models."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      justification: "Rigorous benchmarking identifies XGBoost as top performer, guiding algorithm selection for financial prediction tasks."
  contribution: "The study's comparative evaluation framework can directly inform Odin's system evaluation module for testing spending forecasting or anomaly detection algorithms. The finding that XGBoost outperforms other models on structured tabular data justifies its selection for Odin's predictive components. The use of 5-fold cross-validation to prevent overfitting provides a best practice for Odin's model validation pipeline. The dataset preprocessing methodology (CRISP-DM) offers a structured approach for handling real-world financial data."
  directly_justifies:
    - "XGBoost achieves higher accuracy (90.66%) than other models on imbalanced tabular data."
    - "Cross-validation is necessary to avoid overestimation of model performance from single train-test splits."
    - "Ensemble methods like Gradient Boosting produce more stable generalization than single decision trees."
  limits:
    - "Data from a single institution limits generalizability to other populations."
    - "Only academic and sociodemographic features used; behavioral data not included."
    - "Model interpretability not addressed, which is important for deployment in sensitive domains."
    - "The balanced class distribution (50/50) may not reflect real-world dropout rates."
  mapping_rationale: "The paper focuses on predicting student dropout using machine learning, which is not directly within Odin's financial domains. However, its methodological contributions to algorithm evaluation and model selection are directly applicable to Odin's system evaluation module (12.A) and evaluation of algorithmic modules (12.B). Topics related to user retention (11.A, 11.B) were considered but rejected because the paper addresses educational retention, not financial app engagement dynamics. Behavioral profiling (5.A) was rejected due to lack of financial behavior focus. The paper's rigorous comparative framework and cross-validation practices provide citable justification for how Odin should evaluate its own predictive models."
limitations:
  - "Data sourced from a single institution may limit external validity."
  - "Behavioral and psychosocial dimensions (e.g., LMS engagement, motivation) were not included."
  - "Model interpretability remains a challenge for deployment in education and finance."
  - "The dataset's balanced class distribution (50% dropout, 50% retained) does not reflect real-world attrition rates, which are typically imbalanced."
remember_this:
  - "XGBoost achieved 90.66% cross-validated accuracy for dropout prediction."
  - "Ensemble models like Gradient Boosting consistently outperform single classifiers."
  - "Cross-validation is essential to avoid overfitting in educational data mining."
  - "Naïve Bayes produces excessive false positives despite high recall."
```