```yaml
paper_id: 10.3390/wevj14080227
designation: algorithm-specific
title: Purchasing Intentions Analysis of Hybrid Cars Using Random Forest Classifier and Deep Learning
authors: Ong, A.K.S.; Cordova, L.N.Z.; Longanilla, F.A.B.; Caprecho, N.L.; Javier, R.A.V.; Borres, R.D.; German, J.D.
year: 2023
venue: World Electric Vehicle Journal
odin_topics:
  - 5.C
  - 6.A
  - 12.B
shorthand_tags:
  - /behavioral-classification
  - /predictive-modeling
  - /algorithm-evaluation
tldr: Random forest classifier (94% accuracy) and deep learning neural network (96.6% accuracy) predict Filipino drivers’ hybrid car purchase intentions, with perceived environmental concern and attitude as top factors.
problem_and_motivation: Hybrid cars are not widely adopted in the Philippines despite their environmental benefits. Limited studies use machine learning to analyze purchasing intentions for hybrid cars in developing countries. Understanding these intentions can guide automakers and support sustainable transportation goals.
approach:
  - Surveyed 1048 Filipino drivers with a driver’s license using convenience and snowball sampling.
  - Adapted questionnaire from prior hybrid car intention study with 12 latent variables from PEPB and UTAUT2 frameworks.
  - Applied Decision Tree, Random Forest Classifier (RFC), and Deep Learning Neural Network (DLNN) to predict behavioral intention.
  - Optimized hyperparameters for each algorithm using different train-test splits and criteria (Gini, entropy).
  - Validated models using Taylor diagram comparing root mean square error and correlation.
findings:
  - num: Deep learning neural network achieved 96.60% accuracy in predicting behavioral intention.
  - num: Random forest classifier achieved 94% accuracy at 90:10 train-test split with Gini and best splitter.
  - Perceived environmental concern (PENC) was the most important factor (100% normalized importance), followed by attitude (96.32%) and perceived behavioral control (94.50%).
  - Basic decision tree produced much lower accuracy (max 72.32%) due to random tree generation per iteration.
  - DLNN with tanh hidden layers and sigmoid output layer outperformed RFC.
  - Habit was the least significant factor (70.90% normalized importance).
key_figures_tables:
  - Figure 2: Optimum random forest tree with PENC as root node → PENC and attitude dominate prediction.
  - Figure 3: DLNN architecture with three hidden layers (50,50,20 nodes) → 96.6% accuracy.
  - Figure 4: Taylor diagram validating all MLAs except basic decision tree → DLNN and RFC acceptable.
  - Table 5: Normalized importance scores ranking all 12 factors → PENC highest, habit lowest.
key_equations:
  - equation: "tanh(x) = \\frac{2}{1+e^{-2x}} - 1"
    explanation: Activation function for hidden layers enabling nonlinear mapping.
  - equation: "sigmoid(x) = \\frac{1}{1+e^{-x}}"
    explanation: Output layer activation for probability prediction.
definitions:
  - term: PEPB
    definition: Pro-environmental Theory of Planned Behavior, extending TPB with environmental concern and authority support.
  - term: UTAUT2
    definition: Unified Theory of Acceptance and Use of Technology 2, including hedonic motivation, price value, and habit.
  - term: STPB
    definition: Sustainability Theory of Planned Behavior, integrating PEPB, sustainability domains, and UTAUT2.
  - term: RFC
    definition: Random Forest Classifier, an ensemble method that builds multiple decision trees and selects the best.
  - term: DLNN
    definition: Deep Learning Neural Network, a neural network with multiple hidden layers.
critical_citations:
  - "[German et al., 2022] — Developed PEPB framework used in this study."
  - "[Venkatesh et al., 2012] — Originated UTAUT2 model for technology acceptance."
  - "[Ong et al., 2023] — Previous SEM study on hybrid car intentions, used for comparison."
relevance:
  topics:
    - code: 5.C
      name: Financial Behavioral Profile Classification Algorithm
      justification: Uses RFC and DLNN to classify significant latent factors affecting purchase intention.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      justification: Applies predictive modeling (classification) to forecast behavioral intention from latent variables.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: Compares accuracy of DT, RFC, and DLNN using Taylor diagram and normalized importance scores.
  contribution: "This paper demonstrates that ensemble machine learning methods (random forest and deep learning) can achieve over 94% accuracy in predicting purchase intentions from psychosocial and environmental factors. For Odin, similar ML approaches could be applied to forecast spending behavior or classify financial profiles of Filipino young professionals. The study also provides a methodology for comparing multiple algorithms (DT, RFC, DLNN) and validating them with correlation and error metrics, which directly informs Odin’s evaluation of algorithmic modules. The finding that perceived environmental concern and attitude are top predictors suggests that non-financial attitudes may be important inputs for behavioral models in PFMS."
  directly_justifies:
    - "Random forest classifier achieved 94% accuracy in predicting behavioral intentions from 12 latent variables."
    - "Deep learning neural network with tanh activation outperformed random forest with 96.6% accuracy."
    - "Perceived environmental concern is the most important predictor (100% normalized importance)."
    - "Habit was the least significant factor (70.9%), suggesting it may not strongly predict intention for novel products."
  limits:
    - "Study focuses on hybrid car purchase intention, not personal financial management or spending behavior."
    - "Convenience and snowball sampling may limit generalizability to all Filipino young professionals."
    - "Only drivers with licenses and active on social media were included, potentially biasing results toward younger, digitally connected demographics."
  mapping_rationale: "This paper is algorithm-specific, focusing on RFC and DLNN for behavioral prediction. It does not address expense categorization (3.A, 3.B), budget recommendation (7.A–C), anomaly detection (8.A–B), mobile design (9.A–B), privacy (10.A–B), retention (11.A–B), or savings/debt management (13.A–B). However, its use of ML to classify influential factors aligns with financial behavioral profile classification (5.C). The predictive modeling approach (6.A) is transferable to spending forecasting in Odin. The systematic evaluation of multiple algorithms with accuracy and correlation metrics directly supports evaluation of algorithmic modules (12.B). Codes 5.A and 5.B were rejected because the paper does not define dynamic profiles or address cold-start problems. Code 6.B (spending forecasting algorithm) was rejected because the target is purchase intention, not spending amounts over time."
limitations:
  - "Limited constructs from adapted questionnaire; self-administered online survey may introduce response bias. [unacknowledged]"
  - "Only drivers with a license and social media presence were sampled, excluding non-digital or non-licensed populations."
  - "Only two machine learning algorithms (RFC and DLNN) were used; other algorithms like Naïve Bayes or k-NN were not tested."
  - "Cross-sectional design cannot confirm causal relationships among latent variables."
remember_this:
  - "Deep learning achieved 96.6% accuracy for predicting purchase intentions."
  - "Perceived environmental concern was the most important factor."
  - "Random forest classifier reached 94% accuracy with Gini and best splitter."
  - "Habit was the weakest predictor of behavioral intention."
```