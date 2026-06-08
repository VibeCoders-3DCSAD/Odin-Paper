```yaml
paper_id: 10.1016/j.heliyon.2023.e20644
designation: international
title: A machine learning ensemble approach to predicting factors affecting the intention and usage behavior towards online groceries applications in the Philippines
authors: Gumasing, M.J.J.; Ong, A.K.S.; Sy, M.A.P.C.; Prasetyo, Y.T.; Persada, S.F.
year: 2023
venue: Heliyon
odin_topics:
  - 1.C
  - 5.A
  - 6.A
  - 11.A
  - 12.B
shorthand_tags:
  - /financial-behavior
  - /behavioral-profile
  - /predictive-modeling
  - /engagement
  - /ml-evaluation
tldr: A machine learning ensemble of random forest and artificial neural network predicts that perceived benefits, perceived vulnerability, behavioral intention, performance expectancy, and perceived severity strongly influence online grocery app usage among Filipino consumers during COVID-19.
problem_and_motivation: Despite the rise of online grocery shopping in the Philippines during COVID-19, factors driving consumer intention and usage behavior remain underexplored. Existing studies using traditional statistical methods have limitations in capturing complex, nonlinear relationships. A holistic measurement integrating health concerns and technology acceptance is needed.
approach:
  - Data from 373 Filipino online grocery consumers collected via 5-point Likert survey.
  - Integrated Protection Motivation Theory (PMT) and Unified Theory of Acceptance and Use of Technology (UTAUT2) with 11 latent variables.
  - Used Random Forest Classifier (optimized over 6400 runs with depth 6, 90:10 train-test split, 96% accuracy).
  - Used Artificial Neural Network with Tanh/Softmax activation, Adam optimizer, 150 epochs, 90 hidden nodes, 96.63% accuracy.
  - Evaluated feature importance via score of importance and Taylor diagram for consistency.
findings:
  - "num: Random Forest achieved 96% accuracy with 0.00 standard deviation at depth 6."
  - "num: Artificial Neural Network achieved 96.63% average testing accuracy."
  - Perceived benefit is the most significant factor (importance score 0.270), followed by perceived vulnerability (0.265) and behavioral intention (0.258).
  - All ten constructs (performance expectancy, effort expectancy, social influence, hedonic motivation, facilitating conditions, perceived benefit, perceived vulnerability, perceived severity, perceived susceptibility, response efficacy) significantly affect behavioral intention or usage behavior.
  - High usage behavior is driven by perceived benefits, perceived vulnerability, performance expectancy, behavioral intention, and perceived severity.
key_figures_tables:
  - "Figure 4: Decision tree from random forest classifier showing perceived benefit as parent node → perceived vulnerability and performance expectancy lead to very high usage."
  - "Table 6: Importance scores ranking perceived benefit highest (100%) and facilitating conditions lowest (58.6%)."
  - "Figure 6: Taylor diagram showing correlation and standard deviation within acceptable 20% RMSE threshold → consistent ensemble."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: UTAUT2
    definition: Unified Theory of Acceptance and Use of Technology, an extension with hedonic motivation, price value, and habit.
  - term: PMT
    definition: Protection Motivation Theory, a health behavior model focusing on threat and coping appraisal.
  - term: ANN
    definition: Artificial Neural Network, a supervised machine learning algorithm mimicking biological neurons.
  - term: RFC
    definition: Random Forest Classifier, an ensemble decision tree algorithm.
critical_citations:
  - "[Venkatesh et al., 2003] — Unified theory of technology acceptance."
  - "[Venkatesh et al., 2012] — Extended UTAUT2 with hedonic motivation."
  - "[Janz & Becker, 1984] — Health belief model foundation for PMT."
  - "[Ong, 2022] — Machine learning ensemble for behavior prediction."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      justification: Paper analyzes Filipino consumers' behavioral intention and usage of online groceries, informing financial behavior patterns.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      justification: Identifies key factors (perceived benefits, vulnerability, etc.) that distinguish user profiles for adoption.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      justification: Uses machine learning (ANN and Random Forest) to predict usage behavior, applicable to spending forecasting.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      justification: Behavioral intention and usage behavior are direct measures of user engagement with the application.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: Evaluates accuracy and feature importance of two ML algorithms for behavior classification.
  contribution: This paper's machine learning ensemble approach could be adapted for Odin's behavioral profiling module to predict user engagement based on perceived benefits and vulnerability. The ranking of factors (perceived benefit > vulnerability > intention > performance expectancy) directly informs spending forecasting by weighting these predictors. The high accuracy of ANN and Random Forest (96%+) validates using such algorithms for Odin's classification tasks, such as anomaly detection or budget recommendation. The integration of PMT with UTAUT2 provides a framework for understanding how health concerns (or financial security concerns) drive app usage, relevant to user retention strategies.
  directly_justifies:
    - Using Random Forest Classifier and Artificial Neural Network together achieves over 96% accuracy in predicting technology usage behavior.
    - Perceived benefit is the most influential factor (importance 0.270) in predicting usage behavior of online applications.
    - Perceived vulnerability and behavioral intention together explain high usage behavior when performance expectancy is also high.
    - All ten constructs from UTAUT2 and PMT significantly affect behavioral intention or usage behavior in a Filipino consumer context.
  limits:
    - Study focuses on online grocery apps, not general PFMS, limiting direct transfer to budgeting or savings features.
    - Sample majority from highly urbanized cities, potentially overrepresenting tech-literate users.
    - Lack of consideration of socio-economic factors like income or education as segmentation variables [unacknowledged].
    - No longitudinal data to assess behavioral change over time [unacknowledged].
  mapping_rationale: The paper was screened against Odin's functional domains: Behavioral profiling, spending forecasting, user retention, and system evaluation were flagged. Topic codes 1.C (Financial Behavior) was selected because the paper empirically measures Filipino consumer intentions and usage. 5.A (Behavioral Profiles) applies as the factor ranking can define distinct user personas. 6.A (Predictive Modeling) applies due to the use of ANN and RFC for classification, which can be repurposed for spending prediction. 11.A (Engagement Dynamics) applies as behavioral intention directly correlates with app usage frequency. 12.B (Evaluation) applies because the paper rigorously evaluates algorithm accuracy and consistency. Rejected codes (e.g., 3.A Expense Categorization, 8.A Anomaly Detection) because the paper does not address transaction categorization or outlier detection. Borderline case 2.A (Cultural Practices) was rejected as the study's Philippine context is demographic rather than culturally specific financial practices.
limitations:
  - Respondents majorly reside in highly urbanized cities, affecting technological literacy representation.
  - Lack of consideration of socio-economic factors for customer segmentation.
  - No validation of model generalizability to other types of financial apps [unacknowledged].
remember_this:
  - Perceived benefit is the strongest predictor of app usage behavior at 100% importance.
  - Random Forest and ANN both achieved over 96% accuracy in predicting user behavior.
  - Integration of health belief model with technology acceptance improves prediction for pandemic contexts.
  - Filipino consumers' online grocery usage is driven by vulnerability and performance expectancy.
```