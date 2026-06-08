```yaml
paper_id: c3d5e7f9-1a2b-3c4d-5e6f-7a8b9c0d1e2f
designation: international
title: Time-Series Forecasting Using Deep Learning and Data Mining Models
authors: Scrivano, A.
year: 2025
venue: Unknown
odin_topics:
  - 6.B
  - 8.B
  - 12.B
shorthand_tags:
  - /spending-forecast-algorithm
  - /anomaly-detection-algorithm
  - /evaluation-framework
tldr: A review comparing traditional statistical, deep learning (RNN, LSTM, CNN, Transformer), and data mining models for time-series forecasting, finding Transformers and Gradient Boosting Machines achieve superior accuracy across finance, energy, and retail domains.
problem_and_motivation: Traditional time-series models like ARIMA fail to capture non-linear dynamics and complex patterns in real-world data. Deep learning and data mining methods offer improved accuracy but require systematic evaluation across domains. This review synthesizes current methodologies to guide model selection.
approach:
  - Data collected from stock exchanges, meteorological records, smart grids, and retail transactions.
  - Preprocessing included differencing, smoothing, log transforms, feature extraction (lagged variables, moving averages), and normalization.
  - Model selection based on task: RNN/LSTM for temporal dependencies, CNN/TCN for spatial hierarchies, Transformers for attention-based long-range dependencies.
  - Training used backpropagation with Adam/RMSProp, data augmentation, and rolling cross-validation.
  - Evaluation used MAE, RMSE, MAPE, and quantile loss for probabilistic forecasts.
  - Compared deep learning (RNN, LSTM, TCN, Transformer) and data mining (Random Forest, Gradient Boosting) on three benchmark datasets.
findings:
  - "num: LSTM achieved 15% reduction in MAE over conventional methods in web traffic prediction."
  - "num: TCN attained 20% higher accuracy in early-stage anomaly detection compared to traditional methods."
  - "num: Transformer reduced MSE by 12% and MAE by 17% over recurrent and convolutional models in retail."
  - "num: Gradient Boosting Machine outperformed Random Forest with MAE of 170 vs 185 in energy dataset."
  - Transformers exhibited strongest probabilistic forecasting capabilities in quantile loss assessment.
  - RNNs suffered from gradient degradation in long sequences, underperforming LSTMs.
key_figures_tables:
  - "Table 1: LSTM, TCN, Transformer MAE/MSE on retail → Transformer best."
  - "Table 2: Deep learning models across energy, finance, retail → Transformer consistently superior."
  - "Table 3: Random Forest vs Gradient Boosting → Gradient Boosting superior."
  - "Figure 1: Quantile-based confidence intervals for energy markets → risk-aware decision making."
  - "Figure 2: Temporal forecast errors in retail → Transformers most stable."
  - "Figure 3: Convergence of data mining models on financial data → efficient learning."
  - "Figure 4: Quantile loss assessment → Transformers best at handling predictive uncertainty."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: RNN
    definition: Recurrent Neural Network, a class of neural networks for sequential data.
  - term: LSTM
    definition: Long Short-Term Memory, an RNN variant with gating mechanisms.
  - term: TCN
    definition: Temporal Convolutional Network, uses dilated convolutions for time series.
  - term: MAE
    definition: Mean Absolute Error, average absolute forecast error.
  - term: RMSE
    definition: Root Mean Square Error, square root of average squared errors.
  - term: MAPE
    definition: Mean Absolute Percentage Error, relative error metric.
  - term: GBM
    definition: Gradient Boosting Machine, ensemble method using boosted decision trees.
critical_citations:
  - "[Hochreiter & Schmidhuber, 1997] — introduced LSTM for temporal dependencies."
  - "[Vaswani, 2017] — introduced Transformer attention mechanism."
  - "[Friedman, 2001] — developed Gradient Boosting Machines."
  - "[Breiman, 2001] — developed Random Forests."
  - "[Box et al., 2015] — foundational ARIMA models."
relevance:
  topics:
    - code: 6.B
      name: Spending Forecasting Algorithm
      justification: Benchmarks LSTM, Transformer, and GBM for temporal prediction.
    - code: 8.B
      name: Anomaly Detection Algorithm
      justification: Reports 20% higher anomaly detection accuracy with TCN.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: Compares models using MAE, RMSE, MAPE, and quantile loss.
  contribution: "This review surveys state-of-the-art forecasting algorithms and evaluation metrics that directly inform Odin's spending forecasting module (6.B) and anomaly detection module (8.B). It provides empirical comparisons showing Transformers and Gradient Boosting as top performers, guiding algorithm selection for high-accuracy predictions. The probabilistic forecasting discussion supports uncertainty-aware budget recommendations. The evaluation framework (MAE, RMSE, quantile loss) offers a validated toolkit for assessing Odin's algorithmic modules."
  directly_justifies:
    - "Transformers reduce forecast error by 12-17% compared to recurrent models in retail data."
    - "Gradient Boosting Machines achieve MAE of 170 on energy data, outperforming Random Forest."
    - "TCNs provide 20% higher early-stage anomaly detection accuracy than traditional methods."
    - "Quantile loss functions enable probabilistic forecasts essential for risk-aware decision making."
  limits:
    - "None identified."
  mapping_rationale: "The paper focuses on general time-series forecasting without specific attention to personal finance or Filipino demographics. It was screened against Odin's functional domains: spending forecasting (6.A/6.B) and anomaly detection (8.A/8.B) are directly supported by empirical comparisons of predictive models. Evaluation frameworks (12.A/12.B) are also relevant due to detailed metric discussions. Behavioral profiling (5.A-5.C), budget recommendation (7.A-7.C), and mobile UX (9.A-9.B) were rejected because the paper does not address user classification, budgeting strategies, or interface design. Data privacy (10.A) is mentioned only briefly in future directions, not as a core contribution, so it was excluded. Borderline case: the paper's discussion of federated learning and differential privacy could support 10.A, but these are not empirically evaluated or central to the paper's claims."
limitations:
  - "The review lacks specific guidance for personal finance domains; results are from aggregate datasets not individual-level transactions."
  - "Computational constraints of Transformers may limit deployment on mobile devices [unacknowledged]."
  - "Generalizability to Filipino financial behaviors and spending patterns is untested [unacknowledged]."
remember_this:
  - "Transformers achieve 12-17% lower forecast errors than recurrent models."
  - "Gradient Boosting Machines offer strong accuracy with lower computational cost."
  - "Probabilistic forecasting quantifies uncertainty essential for risk-aware decisions."
  - "Data quality and volume remain critical constraints for deep learning models."
```