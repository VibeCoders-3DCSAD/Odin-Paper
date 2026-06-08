```yaml
paper_id: 10.3390/ijfs11030094
designation: international
title: Forecasting Stock Market Prices Using Machine Learning and Deep Learning Models: A Systematic Review, Performance Analysis and Discussion of Implications
authors: Sonkavde, G.; Dharrao, D. S.; Bongale, A. M.; Deokate, S. T.; Doreswamy, D.; Bhat, S. K.
year: 2023
venue: International Journal of Financial Studies
odin_topics:
- 6.A
- 6.B
- 12.A
- 12.B
shorthand_tags:
- /forecasting
- /ensemble
- /evaluation
tldr: A systematic review and comparative analysis of machine learning, deep learning, and ensemble models for stock price forecasting, with an implemented ensemble of Random Forest, XG-Boost, and LSTM achieving superior RMSE and R2 scores.
problem_and_motivation: Stock market prediction remains challenging due to unpredictable dynamics and limitations of traditional technical and fundamental analysis. Recent advances in machine learning and deep learning offer improved forecasting capabilities, but a comprehensive review with practical model comparisons is lacking. This paper addresses the gap by reviewing state-of-the-art algorithms and implementing an ensemble model for empirical evaluation.
approach:
- Data from Yahoo Finance for TAINIWALCHM and AGROPHOS stocks (2014-2023 for first, 2018-2023 for second).
- Implemented SVR, MLPR, KNN, Random Forest, XG-Boost, LSTM, and an ensemble of Random Forest+XG-Boost+LSTM.
- Evaluation metrics were RMSE and R2 score.
- Hyperparameter tuning performed using grid search with defined parameter grids for each algorithm.
- Training/testing split was 80/20.
findings:
- num: Ensemble model (Random Forest+XG-Boost+LSTM) achieved RMSE 2.0247 and R2 0.9921 on TAINIWALCHM, best among all models.
- num: On AGROPHOS, ensemble achieved RMSE 1.2658 and R2 0.9897, outperforming individual algorithms.
- XG-Boost performed well with RMSE 2.0686 and R2 0.9842 on TAINIWALCHM.
- Random forest showed high R2 (0.9818) but very high RMSE (87.88) on TAINIWALCHM due to scale sensitivity.
- LSTM with sentiment analysis improved RMSE from 55.99 to 23.07 in cited studies.
- GRU trains faster than LSTM and achieves comparable accuracy with fewer parameters.
- Hyperparameter tuning is crucial for stock forecasting performance.
key_figures_tables:
- Figure 7: Forecasting plots for TAINIWALCHM across SVR, MLPR, KNN, RF, XG-Boost, LSTM, and ensemble → Ensemble shows closest fit to actual prices.
- Figure 8: Forecasting plots for AGROPHOS across all seven models → Ensemble consistently outperforms individual models.
- Table 2: RMSE and R2 comparison for all algorithms on both stocks → Ensemble has lowest RMSE and highest R2 on both datasets.
- Table 3: Summary of existing algorithms with gap analysis and performance metrics → Provides benchmarking reference for model selection.
key_equations:
- equation: O = S_x + K
  explanation: Linear regression output with slope S_x and constant K.
- equation: D(h_i, p_r) = sqrt(∑_{l=1}^{n} (p_r - h_i)^2)
  explanation: Euclidean distance for KNN prediction.
- equation: i_gate = σ(W_ip [h_{t-1}, X_c] + b_i)
  explanation: LSTM input gate sigmoid activation.
- equation: f_gate = σ(W_fg [h_{t-1}, X_c] + b_f)
  explanation: LSTM forget gate controlling memory discard.
- equation: Z[t] = σ(W^{(z)} x_t + U^{(z)} h_{t-1})
  explanation: GRU update gate equation.
definitions:
- term: LSTM
  definition: Long Short-Term Memory, an RNN variant that captures long-term dependencies via gating mechanisms.
- term: GRU
  definition: Gated Recurrent Unit, an RNN with two gates (reset and update) that trains faster than LSTM.
- term: RMSE
  definition: Root Mean Square Error, a regression evaluation metric measuring prediction error.
- term: R2
  definition: Coefficient of determination, proportion of variance explained by the model.
- term: XG-Boost
  definition: Extreme Gradient Boosting, an ensemble method using sequential decision trees with gradient descent.
- term: ARIMA
  definition: Autoregressive Integrated Moving Average, a classical time series forecasting model.
- term: FBProphet
  definition: Facebook's time series forecasting library handling seasonality and holiday effects.
critical_citations:
- "[Di Persio and Honchar, 2017] — RNN, LSTM, GRU for Google stock forecasting."
- "[Zhu and He, 2022] — XG-Boost outperforms ARIMA and LSTM on Amazon stock."
- "[Li and Pan, 2021] — Blending ensemble (LSTM+GRU) reduces MSE."
- "[Xu et al., 2020] — E-SVR-RF ensemble using bagging improves forecasting."
relevance:
  topics:
  - code: 6.A
    name: Predictive Modeling in Personal Finance Systems
    justification: Review of ML/DL models for financial time series forecasting.
  - code: 6.B
    name: Spending Forecasting Algorithm
    justification: Methods like LSTM, XG-Boost, and ensembles applicable to spending prediction.
  - code: 12.A
    name: Evaluation Frameworks for Personal Finance Systems
    justification: Systematic comparison using RMSE, R2, and hyperparameter tuning protocols.
  - code: 12.B
    name: Evaluation of Algorithmic Modules
    justification: Benchmarking of individual vs. ensemble models with quantitative metrics.
  contribution: This systematic review provides a benchmarking framework for ML/DL algorithms that can directly inform Odin's spending forecasting module selection. The implemented ensemble of Random Forest, XG-Boost, and LSTM demonstrates that hybrid models achieve superior predictive accuracy (R2 > 0.99) compared to individual algorithms, offering a template for Odin's forecasting pipeline. The detailed evaluation using RMSE and R2 establishes a validation protocol that Odin can adopt for its algorithmic modules. The emphasis on hyperparameter tuning via grid search highlights a critical step for optimizing PFMS prediction performance. Finally, the identification of limitations (e.g., model degradation over time) guides Odin's need for continuous retraining strategies.
  directly_justifies:
  - Ensemble methods combining tree-based and recurrent models outperform individual algorithms for time series forecasting.
  - Hyperparameter tuning via grid search significantly improves forecasting accuracy in financial applications.
  - LSTM captures long-term dependencies and mitigates vanishing gradient issues in RNNs.
  - XG-Boost provides efficient gradient boosting with configurable random forest ensembles.
  - No universal model exists; model selection requires empirical evaluation on target data.
  limits:
  - The paper focuses on stock market data, not personal spending data, which may have different volatility patterns.
  - Only two Indian stocks from the chemical sector were tested, limiting generalizability to other domains.
  - The ensemble model's complexity (three algorithms stacked) may require high computational resources for real-time PFMS.
  - Sentiment analysis integration was reviewed but not implemented in the main ensemble.
  mapping_rationale: The paper was screened against Odin's functional domains. Spending forecasting (domain 6) is directly relevant because the paper reviews and benchmarks predictive models (linear regression, tree-based, RNNs, ensembles) for financial time series, which parallels user spending prediction. System evaluation (domain 12) applies because the paper provides a structured evaluation framework with RMSE, R2, and hyperparameter tuning methodology. Topics 7.A/7.B (budget recommendation) were rejected because the paper does not discuss budgeting strategies or recommendation algorithms. Topics 8.A/8.B (anomaly detection) were rejected as anomaly detection is not a focus. Topics 5.A-5.C (behavioral profiling) were rejected; the paper lacks user behavior analysis. The ensemble method's superior performance justifies selecting 6.B for algorithm guidance.
limitations:
- The study is a systematic review with a limited empirical case study (two stocks, one sector). [unacknowledged]
- Hyperparameter tuning is critical but the paper does not provide a systematic method for selecting optimal grids. [acknowledged]
- Stock market models degrade over time as market conditions evolve, requiring continuous retraining. [acknowledged]
- No comparison with state-of-the-art transformers or attention-based models (e.g., Transformer, TFT). [unacknowledged]
- The ensemble model's computational cost is not quantified. [unacknowledged]
remember_this:
- Ensemble of Random Forest, XG-Boost, and LSTM achieved R2 above 0.99 on test stocks.
- Hyperparameter tuning via grid search is critical for model performance.
- No universal model exists for stock or spending forecasting.
- LSTM and GRU mitigate vanishing gradient problems in RNNs.
- Evaluation metrics RMSE and R2 are standard for regression forecasting tasks.
```