```yaml
paper_id: 10.3390/app13116515
designation: international
title: Concept Drift Adaptation Methods under the Deep Learning Framework: A Literature Review
authors: Xiang, Q.; Zi, L.; Cong, X.; Wang, Y.
year: 2023
venue: Applied Sciences
odin_topics:
  - 6.A
  - 6.B
  - 8.A
  - 8.B
  - 12.B
shorthand_tags:
  - /predictive-modeling
  - /forecasting-algorithm
  - /anomaly-detection
  - /anomaly-algorithm
  - /algorithm-evaluation
tldr: A literature review of concept drift adaptation methods under deep learning, covering discriminative, generative, hybrid, and other learning approaches for handling non-stationary data streams.
problem_and_motivation: Data distribution changes cause concept drift, degrading deep learning model performance in dynamic environments like epidemics and big data. Existing reviews lack focus on deep learning frameworks for concept drift adaptation. This gap motivated the paper.
approach:
  - Review of concept drift definition, causes, and types (abrupt, incremental, gradual, recurring).
  - Classification of methods into discriminative learning (MLP, RNN, LSTM, CNN), generative learning (AE, GAN, RBM, SOM), hybrid learning, and others (deep transfer, deep reinforcement learning).
  - Summary of update modes (parameter vs structure) and detection modes (active vs passive).
  - Compilation of common datasets (KDD Cup, Electricity, Weather, Spam, CoverType) and evaluation metrics (accuracy, F1, MCC, MAE, MSE, RMSE, hidden node count, execution time).
  - Discussion of future directions including full drift type coverage, data processing, multi-model integration, and visualization.
findings:
  - "num: Most concept drift adaptation methods focus on abrupt, incremental, and gradual drift, with recurring drift least addressed."
  - "Parameter updates are more common than structural updates due to faster convergence."
  - "Active detection modes help explain drift occurrence but require additional memory and CPU."
  - "Hybrid learning and discriminative learning methods dominate the literature."
  - "LSTM-based methods are widely used for anomaly detection and time-series forecasting under concept drift."
  - "Evaluation metrics for deep learning-based drift adaptation include hidden nodes count, layers, parameters, and execution time."
key_figures_tables:
  - "Figure 1: causes of concept drift (virtual, real, hybrid) → shows how each type affects decision boundaries."
  - "Figure 2: types of concept drift (abrupt, incremental, gradual, recurring) → illustrates drift transition patterns over time."
  - "Table 1: discriminant learning methods summary → lists algorithms with detection modes, update modes, drift types, and limitations."
key_equations:
  - equation: "P_{t0}(x,y) \\neq P_{t1}(x,y)"
    explanation: "Definition of concept drift when joint probability changes over time."
definitions:
  - term: LSTM
    definition: Long short-term memory, a recurrent neural network variant that handles vanishing gradients and long time lags.
  - term: RNN
    definition: Recurrent neural network with feedback connections for sequence data.
  - term: CNN
    definition: Convolutional neural network with shared weights and local connectivity.
  - term: AE
    definition: Autoencoder, an unsupervised neural network for learning efficient codings.
  - term: GAN
    definition: Generative adversarial network with generator and discriminator.
  - term: DTL
    definition: Deep transfer learning, transferring knowledge from a pre-trained model to a new task.
  - term: DRL
    definition: Deep reinforcement learning, combining deep learning with reinforcement learning.
critical_citations:
  - "[Schlimmer and Granger, 1986] — introduced concept drift."
  - "[Gama et al., 2014] — survey on concept drift adaptation."
  - "[Lu et al., 2018] — review of learning under concept drift."
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      justification: Reviews time-series forecasting methods (LSTM, RNN) that adapt to concept drift for spending prediction.
    - code: 6.B
      name: Spending Forecasting Algorithm
      justification: Discusses online adaptive recurrent neural networks and hybrid models directly applicable to spending forecasting.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      justification: Surveys deep learning anomaly detection (AE, LSTM, GAN) with concept drift handling for irregular transaction detection.
    - code: 8.B
      name: Anomaly Detection Algorithm
      justification: Summarizes algorithms like I-LSTM, MemStream, and DCA-DNN for detecting anomalies under changing data distributions.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: Provides evaluation metrics (accuracy, F1, MCC, hidden node count, execution time) and datasets for benchmarking drift adaptation.
  contribution: "This paper provides a systematic taxonomy of concept drift adaptation methods under deep learning, which can directly inform Odin's spending forecasting module by identifying suitable algorithms such as LSTM with adaptive sliding windows. It also reviews anomaly detection techniques that can be integrated into Odin's anomaly detection system to handle changing user spending patterns. The evaluation metrics and datasets discussed can guide the validation of Odin's algorithmic modules under concept drift scenarios. Additionally, the distinction between parameter and structure updates helps design efficient model update strategies for Odin's mobile-first architecture."
  directly_justifies:
    - "Concept drift adaptation methods can improve the accuracy of predictive models in non-stationary environments."
    - "LSTM-based methods with active drift detection are effective for time-series forecasting under gradual and abrupt drift."
    - "Parameter update mechanisms enable faster model adaptation than structural updates."
    - "Hybrid models combining LSTM with autoencoders or CNNs improve robustness to concept drift."
    - "Active drift detection explains the cause of drift but adds memory and computational overhead."
  limits:
    - "The review is a literature survey, not an empirical study; it does not provide novel algorithms or comparative benchmarks."
    - "Many reviewed methods have update delays and high computational costs when deployed on resource-constrained devices. [unacknowledged]"
    - "The review does not empirically compare the performance of different methods on a common financial dataset. [unacknowledged]"
  mapping_rationale: "This paper focuses on concept drift adaptation in deep learning for time-series and anomaly detection. Functional domains flagged: spending forecasting (6.A, 6.B) because drift directly affects prediction accuracy; anomaly detection (8.A, 8.B) as many methods target anomaly detection under drift; system evaluation (12.B) due to comprehensive metrics discussion. Topic codes 5.A (behavioral profiling) and 7.A (budgeting) were rejected because the paper does not address user behavior or budget strategies. Code 3.A (categorization) was not selected. Borderline case 12.A (evaluation frameworks) was narrowed to 12.B (algorithmic evaluation) as the metrics are module-specific rather than full-system evaluation."
limitations:
  - "The paper does not provide empirical comparisons of the reviewed methods."
  - "It focuses on deep learning and excludes shallow learning concept drift methods. [unacknowledged]"
  - "Most discussed methods assume labeled data, limiting applicability to unsupervised scenarios. [unacknowledged]"
remember_this:
  - "Concept drift causes deep learning models to fail in dynamic data streams."
  - "num: Most methods adapt to abrupt drift, but recurring drift remains challenging."
  - "Parameter updates are preferred for faster convergence than structural updates."
  - "Hybrid models combining LSTM with other networks improve drift robustness."
  - "Active drift detection explains drift but adds memory overhead."
```