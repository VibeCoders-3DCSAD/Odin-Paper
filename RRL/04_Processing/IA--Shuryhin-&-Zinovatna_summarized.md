```yaml
paper_id: 10.15276/aait.07.2024.24
designation: algorithm-specific
title: Recommendation system for financial decision-making using Artificial intelligence
authors: Shuryhin, K. A.; Zinovatna, S. L.
year: 2024
venue: Applied Aspects of Information Technology
odin_topics:
  - 2.C
  - 6.A
  - 6.B
  - 7.B
  - 7.C
  - 8.A
  - 8.B
  - 10.A
  - 10.B
shorthand_tags:
  - /user-preferences
  - /predictive-modeling
  - /spending-forecast
  - /budget-recommendation
  - /recommendation-algorithm
  - /anomaly-detection
  - /anomaly-algorithm
  - /data-privacy
  - /user-trust
tldr: Combines Isolation Forest for anomaly detection, ARIMA and LSTM for budget forecasting, and large language models to generate personalized financial recommendations while addressing ethical concerns like privacy and user autonomy.
problem_and_motivation: Cognitive biases lead to irrational financial decisions, and AI-enhanced marketing can manipulate consumer behavior. Existing recommendation systems in finance often lack personalization, fail to account for user autonomy, or ignore ethical considerations. There is a need for an intelligent system that provides unbiased, personalized financial advice without manipulation.
approach:
  - Input data includes user transaction history, spending anomalies, budget forecasts, and user parameters like risk tolerance and financial goals.
  - Isolation Forest isolates anomalies by building binary trees and calculating path lengths; anomaly score near 1 indicates anomalous expense.
  - ARIMA(p,d,q) models short-term dependencies with autoregressive and moving average components after differencing for stationarity.
  - LSTM captures long-term dependencies using forget, input, and output gates with cell state updates.
  - Final forecast is a weighted average of ARIMA and LSTM predictions, with alpha controlling model influence.
  - Large language model (LLaMa 3.1) receives preprocessed data and generates personalized recommendations through context formation and evaluation against user characteristics.
  - System architecture follows event-driven microservices with AWS SageMaker for model deployment, Spring Cloud Gateway for routing, and OAuth 2.0 for authentication.
  - Ethical principles include confidentiality, fairness, transparency, and preserving user autonomy without manipulation.
  - No quantitative evaluation metrics are reported; system is described as a design and prototype implementation.
findings:
  - Isolation Forest effectively identifies atypical financial actions by isolating deviations from normal spending patterns.
  - Combining ARIMA (short-term) and LSTM (long-term) improves budget forecast stability and accuracy.
  - LLM-generated recommendations adapt to different income levels and user-specific risk levels, goals, and preferences.
  - The system promotes responsible financial behavior without imposing decisions, enhancing user awareness and autonomy.
  - Ethical safeguards include OAuth 2.0, OWASP Top 10 principles, and rejection of manipulative or judgemental advice.
key_figures_tables:
  - Figure 1: Diagram of request to LLM for personalized financial recommendation → LLM input includes transaction history, forecasts, anomalies.
  - Figure 2: Example LLM response providing structured advice on expense reduction → Recommendations are actionable and contextual.
  - Figure 3: Interaction of AI components within system → Isolation Forest, ARIMA+LSTM, and LLM feed into each other.
  - Figure 4: ERD for recommendation system → Database schema covers users, transactions, budgets, goals, subscriptions, categories.
  - Figure 5: Main page screenshot → User interface shows financial overview and AI-driven insights.
  - Figure 6: Use of AI models for anomaly detection → Visualization of anomaly scores and flagged transactions.
key_equations:
  - equation: E(h(x)) = c(n) + \frac{2(ln(n-1) - \frac{n-1}{n})}{n}
    explanation: Expected path length in Isolation Forest.
  - equation: s(x,n) = 2^{-\frac{E(h(x))}{c(n)}}
    explanation: Anomaly score; near 1 for anomalies, 0.5 for normal.
  - equation: y_t = c + \phi_1 y_{t-1} + ... + \phi_p y_{t-p} + \theta_1 \epsilon_{t-1} + ... + \theta_q \epsilon_{t-q} + \epsilon_t
    explanation: ARIMA(p,d,q) model equation.
  - equation: f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)
    explanation: Forget gate in LSTM.
  - equation: \hat{y}_t = \alpha \cdot \hat{y}_t^{ARIMA} + (1-\alpha) \cdot \hat{y}_t^{LSTM}
    explanation: Weighted average combination of forecasts.
definitions:
  - term: ARIMA
    definition: AutoRegressive Integrated Moving Average, a time series forecasting model.
  - term: LSTM
    definition: Long Short-Term Memory, a recurrent neural network for long-term dependencies.
  - term: Isolation Forest
    definition: Anomaly detection algorithm that isolates outliers via random binary trees.
  - term: LLM
    definition: Large Language Model, used here to generate personalized financial advice.
  - term: RS
    definition: Recommender System, provides personalized item or action suggestions.
  - term: AIC
    definition: Akaike Information Criterion, used for model selection.
critical_citations:
  - "[Zibriczky, 2016] — Surveys recommender systems in finance."
  - "[Milano et al., 2020] — Analyzes ethical challenges of recommender systems."
  - "[Chua et al., 2023] — Model for user acceptance of AI investment advice."
  - "[Fieberg et al., 2023] — GPT-4 can provide personalized investment portfolios."
relevance:
  topics:
    - code: 2.C
      name: User-Declared Financial Preferences
      justification: System uses user risk level, goals, and preferences as input context.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      justification: ARIMA and LSTM models forecast future spending.
    - code: 6.B
      name: Spending Forecasting Algorithm
      justification: Weighted combination of ARIMA and LSTM is the forecasting algorithm.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      justification: LLM generates personalized budget advice based on forecasts and anomalies.
    - code: 7.C
      name: Budget Recommendation Algorithm
      justification: LLM with context formation and evaluation steps constitutes the recommendation algorithm.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      justification: Isolation Forest detects anomalous expenses to flag irrational spending.
    - code: 8.B
      name: Anomaly Detection Algorithm
      justification: Isolation Forest with path length calculation is the implemented algorithm.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      justification: System uses OAuth 2.0, OWASP principles, and AWS security practices.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      justification: Ethical design, transparency, and autonomy support build user trust.
  contribution: This paper provides an end-to-end architecture for a PFMS recommendation engine that combines anomaly detection, hybrid time-series forecasting, and LLM-based personalization. For Odin, the anomaly detection module (Isolation Forest) can directly flag irregular spending patterns among Filipino young professionals. The weighted ARIMA+LSTM forecasting module offers a robust baseline for predicting seasonal and cyclic spending unique to the Philippine context. The ethical framework described—emphasizing user autonomy and transparent advice—directly informs Odin's design for data privacy and user trust modules.
  directly_justifies:
    - Isolation Forest can identify atypical financial transactions by isolating deviations from normal behavior.
    - Weighted combination of ARIMA and LSTM improves budget forecast accuracy over either model alone.
    - LLMs can generate personalized financial recommendations that adapt to user income level and risk tolerance.
    - Ethical recommendation systems must preserve user autonomy and avoid manipulative advice.
    - OAuth 2.0 and OWASP principles are suitable for securing personal financial data in a PFMS.
  limits:
    - No empirical evaluation or quantitative performance metrics are reported for any module.
    - The paper does not address cold-start scenarios for new users with limited transaction history.
    - User testing on actual financial decision outcomes is absent.
    - The system is designed for general users, not specifically for Filipino young professionals or their cultural financial practices.
  mapping_rationale: The paper was screened against Odin’s functional domains. Spending forecasting (domains 6.A, 6.B) and anomaly detection (8.A, 8.B) are directly addressed by ARIMA+LSTM and Isolation Forest. Budget recommendation (7.B, 7.C) is covered by the LLM-based advice generation. User-declared preferences (2.C) appear as input parameters. Data privacy and user trust (10.A, 10.B) are explicitly discussed in the ethics section. Domains such as behavioral profiling (5.A–C), expense categorization (3.A–B), mobile-first design (9.A–B), user retention (11.A–B), system evaluation (12.A–B), and savings/debt management (13.A–B) were rejected because the paper provides no substantive claims about them – it mentions financial goals but no goal management algorithm, and no evaluation framework beyond architecture description.
limitations:
  - No quantitative validation of forecasting or anomaly detection accuracy. [unacknowledged]
  - The system's LLM component is described only conceptually; no ablation study or comparison with rule-based baselines. [unacknowledged]
  - Ethical claims are not operationalized or measured (e.g., how to verify user autonomy). [unacknowledged]
  - The paper does not address scalability or latency constraints for real-time mobile use. [unacknowledged]
remember_this:
  - Anomaly detection uses Isolation Forest with path length scoring.
  - Forecasts combine ARIMA for short-term and LSTM for long-term trends.
  - Large language model generates personalized financial advice from transaction and forecast data.
  - System explicitly designed to avoid manipulation and preserve user autonomy.
  - Ethical safeguards include OAuth 2.0, OWASP, and transparent recommendations.
```