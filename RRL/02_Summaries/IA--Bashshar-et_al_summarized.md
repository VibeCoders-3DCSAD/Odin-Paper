```yaml
paper_id: a2b8c9d0-e1f2-34a5-b678-90c1d2e3f4a5
designation: algorithm-specific
title: ARTIFICIAL INTELLIGENCE-DRIVEN PERSONAL FINANCE SOLUTION
authors: Bashshar, S. A.; Imran, M.; Kumar, P. S.; Goud, E. S.; Venunath, M.; Prasad, M. L. M.
year: 2025
venue: International Journal of Engineering Science and Advanced Technology (IJESAT)
odin_topics:
  - 3.A
  - 3.B
  - 6.A
  - 6.B
  - 12.A
  - 12.B
shorthand_tags:
  - /cat/nlp
  - /pred/arima
  - /eval/metrics
  - /cat/keyword
  - /ui/django
tldr: An AI-powered personal finance assistant uses NLP for transaction categorization and ARIMA for expense forecasting, achieving 86% categorization accuracy and MAE of 253.47.
problem_and_motivation: Manual tracking fails to provide real-time insights and predictive capabilities, leading to poor budgeting and low savings. Digital payments increase transaction volume, making it hard for individuals to understand spending habits. Existing systems lack automation and forecasting.
approach:
  - Data is collected from user-uploaded CSV files containing transaction date, description, amount, and type.
  - Preprocessing removes extraneous characters, normalizes fields, and applies tokenization, stopword removal, and lemmatization using NLTK.
  - Transaction categorization uses keyword matching against domain-specific dictionaries without manual labeling.
  - Expense forecasting applies ARIMA (AutoRegressive Integrated Moving Average) with AIC for parameter selection on 6 months of historical data.
  - Evaluation metrics include accuracy, precision, recall, F1-score for categorization and MAE, RMSE for forecasting.
  - System implemented in Python with Django web framework and SQLite database.
findings:
  - "num: Categorization accuracy of 86.2% with precision 0.88, recall 0.85, F1-score 0.86."
  - "num: Forecasting MAE of 253.47 and RMSE of 318.91 over 30-day horizon."
  - System captures seasonal spending patterns and main spending variations.
  - User feedback from ten participants was mostly positive on interface intuitiveness and clarity.
  - Confusion matrix shows overlap between similar categories like Dining and Groceries.
key_figures_tables:
  - "Figure 1: Proposed architecture with data preprocessing, NLP categorization, ARIMA forecasting → Modular design enables automation."
  - "Figure 3: 30-day expense forecast vs actual historical expenses → Forecast captures seasonal trends."
  - "Figure 5: Earnings overview dashboard → Visual interface helps users understand financial data."
key_equations:
  - equation: "Y_t = \\phi_1 Y_{t-1} + \\phi_2 Y_{t-2} + ... + \\phi_p Y_{t-p} + \\epsilon_t"
    explanation: "AR component: value depends on past values."
  - equation: "Y_t = \\epsilon_t + \\theta_1 \\epsilon_{t-1} + \\theta_2 \\epsilon_{t-2} + ... + \\theta_q \\epsilon_{t-q}"
    explanation: "MA component: linear combination of past error terms."
definitions:
  - term: NLP
    definition: Natural Language Processing, used to interpret transaction descriptions.
  - term: NLTK
    definition: Natural Language Toolkit, Python library for text processing.
  - term: ARIMA
    definition: AutoRegressive Integrated Moving Average, time-series forecasting model.
  - term: MAE
    definition: Mean Absolute Error, average magnitude of forecast errors.
  - term: RMSE
    definition: Root Mean Square Error, square root of average squared forecast errors.
  - term: AIC
    definition: Akaike Information Criterion, used for model selection.
critical_citations:
  - "[Arrieta et al., 2019] — Defined XAI concepts applicable to finance."
  - "[Budiherwanto, 2025] — Showed commercial IPAs lack domain-specific forecasting."
  - "[Buckley et al., 2021] — Demonstrated NLP with domain knowledge improves extraction accuracy."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      justification: "Paper implements NLP-based automatic transaction categorization."
    - code: 3.B
      name: Expense Category Design Considerations
      justification: "Uses predefined domain dictionaries for categories like Food, Travel, Utilities."
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      justification: "Applies ARIMA time-series model for expense forecasting."
    - code: 6.B
      name: Spending Forecasting Algorithm
      justification: "ARIMA with AIC parameter selection produces 30-day forecasts."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      justification: "Reports accuracy, precision, recall, F1, MAE, RMSE for system modules."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: "Separately evaluates categorization and forecasting with standard metrics."
  contribution: "This paper directly justifies Odin's expense categorization module (3.A) through NLP-based transaction classification achieving 86.2% accuracy. The ARIMA forecasting module (6.B) is supported by demonstrated low MAE of 253.47 and RMSE of 318.91. The evaluation framework (12.A) validates using standard metrics like accuracy, precision, recall, and F1-score. The modular architecture (9.A) aligns with mobile-first design principles for scalability and extensibility. Automated categorization and forecasting reduce manual effort and improve financial awareness, supporting user engagement (11.A)."
  directly_justifies:
    - "NLP with keyword matching achieves 86.2% accuracy for transaction categorization."
    - "ARIMA model can forecast 30-day expenses with MAE 253.47."
    - "Automated categorization reduces manual effort and improves financial awareness."
    - "Modular architecture enables future extensions like anomaly detection."
  limits:
    - "Paper does not address cold-start problem for new users without transaction history."
    - "Categorization relies on static keyword dictionaries, limiting adaptability to new transaction types."
    - "User experience evaluation used only ten participants, which may not generalize."
    - "No comparison with deep learning models (e.g., LSTM) for forecasting [unacknowledged]."
  mapping_rationale: "This paper focuses on AI-driven expense categorization and forecasting, directly aligning with Odin's domains of Expense Categorization (3.A, 3.B) and Spending Forecasting (6.A, 6.B). The thorough reporting of accuracy, MAE, and RMSE supports Evaluation Frameworks (12.A, 12.B). No coverage of behavioral profiling (5.A-C), anomaly detection (8.A-B), savings/debt management (13.A-B), or Filipino-specific demographics (1.A-C), so those topics are rejected. The paper is international (Indian authors) and algorithm-specific (NLP, ARIMA), hence designation 'algorithm-specific'."
limitations:
  - "Small sample size for user feedback (n=10) [unacknowledged]"
  - "Categorization depends on static keyword dictionaries, may not generalize to new transaction types."
  - "No comparison with deep learning baselines for forecasting [unacknowledged]"
  - "User experience evaluation lacks quantitative usability metrics like task completion time."
remember_this:
  - "NLP categorization achieved 86.2% accuracy on real transaction data."
  - "ARIMA forecasting produced MAE of 253.47 for 30-day expenses."
  - "Automated expense tracking reduces manual errors and improves awareness."
  - "Modular Django design allows future integration of anomaly detection."
```