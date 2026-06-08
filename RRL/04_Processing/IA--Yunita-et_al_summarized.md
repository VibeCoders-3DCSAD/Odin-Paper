```yaml
paper_id: 10.1016/j.mex.2025.103462
designation: algorithm-specific
title: Performance analysis of neural network architectures for time series forecasting: A comparative study of RNN, LSTM, GRU, and hybrid models
authors: Yunita, A.; Pratama, M. I.; Almuzakki, M. Z.; Ramadhan, H.; Akhir, E. A. P.; Mansur, A. B. F.; Basori, A. H.
year: 2025
venue: MethodsX
odin_topics:
- 6.A
- 6.B
- 8.B
- 12.B
shorthand_tags:
- /time-series-forecasting
- /rnn-lstm-gru
- /hybrid-models
- /monte-carlo-evaluation
- /algorithm-benchmark
tldr: A benchmark of nine RNN architectures across three time series datasets using Monte Carlo simulation shows no statistically significant differences, but LSTM-based hybrids offer practical advantages in consistency and robustness.
problem_and_motivation: Time series forecasting using neural networks suffers from performance variability due to random weight initialization. The reliability and consistency of RNN, LSTM, GRU, and hybrid architectures for time series analysis remain unclear. A systematic benchmark across diverse datasets is needed to guide architecture selection.
approach:
- Three datasets: sunspot activity (monthly, 3625 records), Indonesian COVID-19 daily cases (634 records), and dissolved oxygen concentration (daily, 1033 records).
- Nine architectures: RNN, LSTM, GRU, RNN-LSTM, RNN-GRU, LSTM-RNN, GRU-RNN, LSTM-GRU, and GRU-LSTM, each with two hidden layers.
- Monte Carlo simulation with 100 independent runs, each with 100 training epochs, using 95% confidence interval trimming.
- Evaluation metrics: MAE, MAPE, RMSE, and computation time; statistical comparison via Friedman test.
- All experiments ran on Google Colab with TensorFlow 2.0, using 70:30 or 80:20 train-test splits.
findings:
- "num: Friedman test showed no statistically significant differences among nine architectures (χ2=12.593, df=8, p=.127)."
- "num: LSTM-GRU hybrid achieved the lowest mean rank (2.23) while vanilla RNN had the highest (8.57)."
- "num: For sunspot forecasting, LSTM-GRU achieved MAE 16.913 ± 0.629 and RMSE 23.205 ± 0.827."
- "num: For COVID-19 case prediction, standalone LSTM performed best with MAE 0.903 ± 0.091 and MAPE 9.036% ± 0.778%."
- "num: For dissolved oxygen forecasting, LSTM-RNN achieved lowest errors (MAE 2.970 ± 0.229, MAPE 7.420% ± 0.585%)."
- Vanilla RNN consistently underperformed across all datasets with highest error rates and variance.
key_figures_tables:
- "Table 3: Performance comparison (MAE, MAPE, RMSE) across three datasets with mean ranks → LSTM-based hybrids rank best despite non-significant test."
- "Table 4: Overall model performance rankings from Friedman test → LSTM-GRU ranked 1st (2.23), RNN last (8.57)."
- "Figure 4: Box plots for sunspot dataset → LSTM-GRU and LSTM-RNN show lowest medians and smallest spreads."
- "Figure 6: Box plots for COVID-19 dataset → LSTM and GRU have tightest error distributions."
- "Figure 8: Box plots for oxygen dataset → LSTM-RNN and LSTM-GRU demonstrate superior accuracy and stability."
key_equations:
- equation: "h_t = g(W·x_t + U·h_{t-1} + b)"
  explanation: "RNN hidden state update."
- equation: "z_t = σ(W_{xz}x_t + W_{hz}h_{t-1} + b_z)"
  explanation: "GRU update gate controls information retention."
- equation: "r_t = σ(W_{xr}x_t + W_{hr}h_{t-1} + b_r)"
  explanation: "GRU reset gate determines previous state relevance."
definitions:
- term: RNN
  definition: "Recurrent neural network, processes sequential data using hidden state recurrence."
- term: LSTM
  definition: "Long short-term memory network with gates to manage long-range dependencies."
- term: GRU
  definition: "Gated recurrent unit, a simplified LSTM variant with update and reset gates."
- term: MAE
  definition: "Mean absolute error, average magnitude of prediction errors in original units."
- term: MAPE
  definition: "Mean absolute percentage error, scale-independent error as percentage."
- term: RMSE
  definition: "Root mean square error, penalizes larger errors quadratically."
- term: Monte Carlo simulation
  definition: "Repeated random sampling to estimate model performance distributions."
- term: Friedman test
  definition: "Non-parametric test for differences across multiple models on multiple datasets."
critical_citations:
- "[Hochreiter & Schmidhuber, 1997] — Introduced LSTM architecture."
- "[Chung et al., 2014] — Empirical evaluation of GRU."
- "[Friedman, 1937] — Original Friedman test for rank-based comparison."
- "[Demšar, 2006] — Statistical comparisons of classifiers over multiple datasets."
- "[Bottou, 1991] — Stochastic gradient learning in neural networks."
relevance:
  topics:
  - code: 6.A
    name: Predictive Modeling in Personal Finance Systems
    justification: "Benchmarks forecasting models directly applicable to spending prediction."
  - code: 6.B
    name: Spending Forecasting Algorithm
    justification: "Evaluates RNN, LSTM, GRU, and hybrids for time series forecasting."
  - code: 8.B
    name: Anomaly Detection Algorithm
    justification: "Time series error analysis informs anomaly detection in spending sequences."
  - code: 12.B
    name: Evaluation of Algorithmic Modules
    justification: "Provides Monte Carlo and Friedman test methodology for reliable model comparison."
  contribution: "This paper provides empirical guidance for selecting neural network architectures for Odin's spending forecasting module by benchmarking LSTM, GRU, and hybrids across three diverse time series datasets. The Monte Carlo evaluation methodology can be adapted for Odin's anomaly detection module to ensure reliable outlier identification under random initialization variability. The finding that no architecture is statistically superior justifies Odin's use of ensemble or dataset-specific selection in its evaluation framework for algorithmic modules. The consistent practical advantages of LSTM-based hybrids (e.g., LSTM-RNN, LSTM-GRU) support prioritizing them for implementation in mobile-first PFMS."
  directly_justifies:
  - "LSTM-based hybrid architectures offer practical advantages in consistency and robustness across diverse temporal patterns."
  - "No statistically significant performance differences exist among nine RNN architectures for time series forecasting (p=0.127)."
  - "Vanilla RNN shows higher error rates and greater forecast variability than LSTM-based models."
  - "Monte Carlo evaluation with 100 iterations quantifies prediction uncertainty more reliably than single-run training."
  limits:
  - "Limited number of datasets (three) reduces statistical power of the Friedman test."
  - "Only two hidden layers used; deeper architectures might yield different performance rankings."
  - "No real-world financial or personal spending data was included, limiting direct transferability to PFMS."
  - "The study did not test on irregularly sampled or sparse time series common in personal finance."
  mapping_rationale: "The paper focuses on time series forecasting algorithms, directly mapping to Odin's spending forecasting (6.A, 6.B) and anomaly detection (8.B) domains because accurate sequence prediction is core to both. The rigorous Monte Carlo and Friedman test evaluation methodology informs system evaluation (12.B). Behavioral profiling (5.A-C) was rejected because no user behavior data or classification is involved. Privacy (10.A-B), retention (11.A-B), and mobile design (9.A-B) are absent. Budget recommendation (7.A-C) was considered borderline since forecasting supports budgeting, but the paper does not address budget constraints or recommendation logic, so rejected. The selected topics capture the algorithmic benchmarking contribution."
limitations:
- "Only three datasets were used, which may limit generalizability to other time series domains."
- "The Friedman test lacked statistical power due to small sample size; non-significant result may mask real differences."
- "Only two hidden layers were tested; performance rankings could change with deeper or shallower architectures."
- "Real-world personal finance data (e.g., transaction streams) was not evaluated [unacknowledged]."
- "Computational efficiency metrics focused only on training time, not inference latency on mobile devices [unacknowledged]."
remember_this:
- "No significant difference among nine RNN architectures (p=0.127)."
- "LSTM-GRU hybrid achieved lowest mean rank of 2.23 across datasets."
- "Vanilla RNN consistently underperformed with highest error rates."
- "LSTM-based hybrids offer practical robustness despite statistical equivalence."
- "Monte Carlo simulation with 100 runs improves model reliability assessment."
```