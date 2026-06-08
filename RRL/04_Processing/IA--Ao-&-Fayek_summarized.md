```yaml
paper_id: 10.3390/s23167167
designation: international
title: Continual Deep Learning for Time Series Modeling
authors: Ao, S.-I.; Fayek, H.
year: 2023
venue: Sensors
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 12.A
  - 12.B
shorthand_tags:
  - /predictive-modeling
  - /spending-forecasting
  - /anomaly-detection
  - /anomaly-algorithm
  - /evaluation-framework
  - /algorithm-evaluation
tldr: Surveys deep learning for sensor time series, highlighting non-stationarity challenges and continual learning methods to mitigate catastrophic forgetting.
problem_and_motivation: Real-world time series often exhibit non-stationary distributions, causing deep learning models to suffer catastrophic forgetting. Traditional methods assume stationarity, limiting deployment in dynamic environments. This survey identifies the gap in applying continual learning to time series forecasting and anomaly detection.
approach:
  - Conducts systematic review of deep learning for sensor time series from 2018-2023.
  - Categorizes methods into deep learning architectures (MLP, RNN, LSTM, CNN, GNN) and preprocessing techniques.
  - Evaluates continual learning approaches (regularization, replay, parameter isolation) for time series tasks.
  - Uses case studies from water treatment, healthcare, traffic, and manufacturing domains.
  - Compares performance of DL models with and without preprocessing on benchmark datasets like UCR, SWaT, and WADI.
findings:
  - "num: CNN with direct multi-step procedure improved prediction accuracy by 22.6% over seasonal ARIMAX for building load forecasting."
  - "num: Graph Deviation Network achieved 54% better F-measure than the next best baseline for anomaly detection in water treatment systems."
  - "num: LSTM achieved mean absolute percentage error of 4.82% for traffic flow forecasting versus 20.97% for ARIMA and 9.06% for BPNN."
  - "num: Empirical mode decomposition preprocessing improved gesture classification accuracy from 94.22% to 99.73% using CNN."
  - "num: MC-SGD continual learning reduced catastrophic forgetting by 29% for activity recognition on wearable sensors."
  - "num: 2-layer Bi-LSTM achieved 98.7% overall accuracy for land use classification from Sentinel-2 time series data."
  - "num: Attention and deep convolutional networks performed best with wavelet and FFT preprocessing for wind prediction."
  - Continual learning approaches (replay, EWC, LwF) mitigate forgetting but only replay accumulates knowledge over time.
  - No single deep learning method fits all time series anomaly detection tasks; domain knowledge remains necessary.
  - Simple machine learning models with feature engineering can outperform frontier deep learning methods without preprocessing.
key_figures_tables:
  - "Figure 1: Tree diagram of deep learning methods for sensor time series classification and forecasting → Groups MLP, RNN, LSTM, CNN, GNN, and hybrids."
  - "Figure 2: Tree diagram of preprocessing methods for sensor time series → Covers EMD, wavelet, ICA, segmentation, and data augmentation."
  - "Figure 3: Taxonomy of continual learning methods for sensor time series → Divides into regularization, replay, and parameter isolation."
  - "Table 1: Summary of DL technique advances for sensor time series applications → Lists 18 studies with accuracy and details."
  - "Table 2: Importance of advanced preprocessing for real-world sensor DL applications → Shows 14 studies where preprocessing improved results."
  - "Table 3: Advances in continual learning techniques for time series applications → Summaries 12 CL studies with motivations and results."
key_equations:
  - equation: "E(y_t) = E(y_{t-1}) = \\mu, \\quad Var(y_t) = \\sigma^2 < \\infty, \\quad Cov(y_t, y_{t-k}) = \\gamma(k)"
    explanation: Weak stationarity conditions for time series.
  - equation: "L_i = \\frac{1}{N} \\sum_{r=1}^{N} L(y_{i,r}, \\hat{y}_{i,r}; \\theta_i) + \\frac{q}{(i-1)N} \\sum_{j=1}^{i-1} \\sum_{r=1}^{N} L(y_{j,r}, M(\\hat{x}_{j,r}; \\theta_i); \\theta_i)"
    explanation: Continual learning objective balancing current and previous tasks.
definitions:
  - term: CL
    definition: Continual learning, a paradigm for sequential learning without catastrophic forgetting.
  - term: CF
    definition: Catastrophic forgetting, abrupt loss of previously learned knowledge when learning new tasks.
  - term: DL
    definition: Deep learning, multi-layer neural networks for hierarchical feature extraction.
  - term: RNN
    definition: Recurrent neural network, designed for sequence data with internal state.
  - term: LSTM
    definition: Long short-term memory, RNN variant with gates to handle long-term dependencies.
  - term: CNN
    definition: Convolutional neural network, uses filters to extract local patterns.
  - term: GNN
    definition: Graph neural network, processes data with graph structure.
  - term: EMD
    definition: Empirical mode decomposition, decomposes signal into intrinsic mode functions.
  - term: EWC
    definition: Elastic weight consolidation, regularization method for continual learning.
critical_citations:
  - "[Kirkpatrick, 2017] — Introduced elastic weight consolidation for overcoming catastrophic forgetting."
  - "[Hochreiter & Schmidhuber, 1997] — Proposed LSTM to address vanishing gradient in RNNs."
  - "[Goodfellow et al., 2016] — Standard deep learning textbook cited for foundational concepts."
  - "[French, 1999] — Early work defining catastrophic forgetting in connectionist networks."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      justification: Reviews deep learning for time series forecasting (load, traffic, solar, rainfall).
    - code: 6.B
      name: Spending Forecasting Algorithm
      justification: Compares LSTM, CNN, and hybrid models for sequence prediction tasks.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      justification: Covers multivariate time series anomaly detection with DL and continual learning.
    - code: 8.B
      name: Anomaly Detection Algorithm
      justification: Evaluates graph neural networks and variational autoencoders for anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      justification: Systematically compares DL models against traditional methods and baselines.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: Assesses preprocessing, feature engineering, and continual learning impacts on performance.
  contribution: "This survey provides a systematic evaluation framework for comparing deep learning architectures (LSTM, CNN, GNN) against traditional time series methods, directly applicable to Odin's spending forecasting module. The review of anomaly detection algorithms, including graph deviation networks and variational autoencoders, informs the design of Odin's anomaly detection system. The analysis of preprocessing techniques (EMD, wavelet, ICA) and data augmentation offers guidance for improving Odin's expense categorization accuracy. The continual learning taxonomy (regularization, replay, parameter isolation) supports Odin's need to adapt to changing user spending patterns without catastrophic forgetting."
  directly_justifies:
    - "CNN with direct multi-step procedure can improve forecasting accuracy by 22.6% over ARIMAX."
    - "No single deep learning method fits all time series anomaly detection tasks."
    - "Simple models with feature engineering can outperform deep learning without preprocessing."
    - "Continual learning with replay buffers accumulates knowledge over time while mitigating forgetting."
    - "Empirical mode decomposition as preprocessing increased classification accuracy from 94.22% to 99.73%."
  limits:
    - "Survey focuses on sensor time series (wearables, satellites, industrial) not personal finance transaction data."
    - "Most reviewed studies assume closed-world stationarity; real-world PFMS data may have different properties."
    - "Computational and memory requirements of continual learning methods for mobile devices are underexplored."
    - "None identified."
  mapping_rationale: "This paper is a methodological survey on deep learning and continual learning for time series forecasting and anomaly detection. It does not address Filipino young professionals or cultural financial practices, so topics 1.A-2.C are rejected. The core contributions fall under predictive modeling (6.A) and spending forecasting algorithms (6.B) due to extensive coverage of LSTM, CNN, and hybrid models for time series prediction. Anomaly detection (8.A and 8.B) is covered via graph neural networks and variational autoencoders. Evaluation frameworks (12.A and 12.B) are relevant because the paper systematically compares algorithms and preprocessing techniques. Topics like behavioral profiling (5.A-C), budget recommendation (7.A-C), or UX design (9.A-B) are not addressed. The mapping prioritizes algorithmic modules that Odin could directly implement."
limitations:
  - "Survey primarily synthesizes existing literature without new empirical experiments. [unacknowledged]"
  - "Focus on sensor time series limits generalizability to financial transaction sequences. [unacknowledged]"
  - "Computational cost of continual learning on mobile devices is not quantitatively assessed. [unacknowledged]"
remember_this:
  - "LSTM achieved 4.82% MAPE for traffic forecasting versus 20.97% for ARIMA."
  - "Empirical mode decomposition preprocessing raised accuracy from 94.22% to 99.73%."
  - "No single deep learning method works for all anomaly detection tasks."
  - "Replay-based continual learning accumulates knowledge over time better than regularization."
  - "Feature engineering can make simple models outperform deep learning without preprocessing."
```