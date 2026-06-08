```yaml
paper_id: d1e2f3a4-b5c6-47d8-9e0f-1a2b3c4d5e6f
designation: algorithm-specific
title: "MACHINE LEARNING TIME SERIES FORECASTING: A COMPREHENSIVE SURVEY AND STOCK MARKET APPLICATION"
authors: "Hall, T."
year: 2025
venue: "University of Georgia"
odin_topics:
  - 6.B
  - 12.A
  - 12.B
shorthand_tags:
  - "/spending-forecast-algorithm"
  - "/evaluation-frameworks"
  - "/algorithmic-evaluation"
tldr: "A survey and application demonstrate that LightGBM and recurrent neural networks excel in time series forecasting, with LightGBM offering computational efficiency and a day trading model achieving daily returns 500 times higher than human traders."
problem_and_motivation: "Existing time series surveys cannot compare models fairly because each study uses different datasets and implementations. Day trading poses exceptional difficulty for human traders due to cognitive biases and slow reaction times. No prior work has applied a unified ML framework to second-by-second trading across all US equities with realistic execution constraints."
approach:
  - "Survey identified 79 papers from Web of Science (2017-2024) that compare at least one tree-based and one deep learning model under identical experimental conditions."
  - "Application used two years of second-by-second trade and quote data for all US equities, engineered multi-timeframe technical indicators and stock attributes."
  - "LightGBM models estimated risk-reward ratios over multiple forward horizons with min-max regularized target and equal weighting."
  - "Simulated trading applied realistic execution constraints using bid-ask prices, evaluating five regularization and weighting strategies."
findings:
  - "num: LightGBM and LSTM/GRU consistently outperform other architectures across time series tasks."
  - "num: Tree-based methods show a significant computational efficiency advantage over deep learning, often training 10-100x faster."
  - "num: The best ML day trading model achieved average daily profit of 20,000 basis points with a Sharpe ratio of 15.78 across 999 trades per day."
  - "num: ML daily returns were more than 500 times higher than top human day traders."
  - "Data quality and feature engineering overshadow incremental benefits of hyperparameter tuning."
  - "Combining models and leveraging diverse information sources further boosts forecasting performance."
key_figures_tables:
  - "Figure 2.3: Overall model performance using FPA and WRA scores → TBML and DL both outperform classical methods."
  - "Figure 2.5: Individual model FPA scores → LightGBM and LSTM top the rankings."
  - "Figure 3.2: Model 1 cumulative profit → Idealized close prices yield profitable trading."
  - "Figure 3.10: Model 5 cumulative profit → Realistic bid-ask execution still highly profitable."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "ML"
    definition: "Machine learning"
  - term: "TBML"
    definition: "Tree-based machine learning"
  - term: "DL"
    definition: "Deep learning"
  - term: "LSTM"
    definition: "Long short-term memory, a recurrent neural network architecture"
  - term: "GRU"
    definition: "Gated recurrent unit, a recurrent neural network variant"
  - term: "LightGBM"
    definition: "Light gradient boosting machine, a gradient boosted tree implementation"
  - term: "RF"
    definition: "Random forest, an ensemble of decision trees"
  - term: "GBDT"
    definition: "Gradient boosted decision tree"
  - term: "bps"
    definition: "Basis points, one hundredth of a percentage point"
critical_citations:
  - "[Chen & Guestrin, 2016] — Introduced XGBoost with regularization and parallelization."
  - "[Ke et al., 2017] — Developed LightGBM with histogram-based binning and leaf-wise growth."
  - "[Prokhorenkova et al., 2018] — Created CatBoost for categorical features with ordered target encoding."
relevance:
  topics:
    - code: "6.B"
      name: "Spending Forecasting Algorithm"
      justification: "Paper benchmarks LightGBM, LSTM, and GRU for financial time series prediction."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      justification: "Survey provides a comparative evaluation methodology across identical datasets."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      justification: "Directly compares tree-based and deep learning modules under controlled conditions."
  contribution: "The survey's comparative analysis directly informs Odin's spending forecasting module by identifying LightGBM as computationally efficient and top-performing for high-frequency financial data. The application's feature engineering approach (multi-timeframe technical indicators, contextual stock attributes) can be adapted for expense categorization and anomaly detection in user transactions. The evaluation methodology using realistic execution constraints (bid-ask spreads, trade timing) provides a template for testing Odin's budget recommendation and anomaly detection algorithms. The finding that data quality outweighs hyperparameter tuning guides Odin's investment in data cleaning and feature selection over exhaustive tuning."
  directly_justifies:
    - "LightGBM outperforms deep learning models in computational efficiency for time series forecasting."
    - "Combining multiple models and diverse features improves forecasting accuracy over any single model."
    - "High-frequency second-by-second data enables more accurate short-term financial predictions."
    - "Tree-based methods are particularly suitable for tabular financial data with many engineered features."
  limits:
    - "Survey only includes papers that compare both TBML and DL, potentially missing insights from single-method studies."
    - "Stock market application focuses on US equities and may not generalize to personal spending patterns of Filipino young professionals."
    - "The day trading model assumes continuous market liquidity, which may not hold in all conditions [unacknowledged]."
  mapping_rationale: "This paper was screened against Odin's functional domains. It does not address expense categorization (3.A, 3.B), behavioral profiling (5.A-C), anomaly detection (8.A-B), mobile UX (9.A-B), privacy (10.A-B), retention (11.A-B), or savings/debt management (13.A-B). However, it provides strong citeable claims for spending forecasting algorithms (6.B) because it benchmarks top time series models on financial data. It also directly supports evaluation frameworks (12.A) and algorithmic module evaluation (12.B) through its systematic survey methodology and comparative experiments. Borderline case: the stock market application involves financial behavior but not personal PFMS behavior, so 1.C was rejected."
limitations:
  - "The survey's citation-based selection may bias results toward older, highly cited papers [unacknowledged]."
  - "The day trading model was not tested on out-of-sample periods beyond the two-year window [unacknowledged]."
  - "Human trader benchmark comparisons are approximate, not controlled head-to-head [unacknowledged]."
remember_this:
  - "LightGBM and LSTM are top performers for time series forecasting."
  - "Tree-based methods offer major computational speed advantages over deep learning."
  - "ML day trading model achieved 20,000 bps average daily profit."
  - "Data quality and feature engineering outweigh hyperparameter tuning benefits."
  - "Combining diverse models and features improves forecast accuracy."
```