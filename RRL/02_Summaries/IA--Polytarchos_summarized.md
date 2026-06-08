```yaml
paper_id: 10.47852/bonviewFSI52026108
designation: international
title: "Credit Card Fraud Detection Through Deep Learning and Real-Time Data Streams: A Comparison and New Directions"
authors: Polytarchos, E.
year: 2025
venue: FinTech and Sustainable Innovation
odin_topics:
  - 5.A
  - 8.A
  - 8.B
  - 12.A
  - 12.B
shorthand_tags:
  - /behavioral-profiles
  - /anomaly-detection
  - /anomaly-algorithm
  - /evaluation-framework
  - /algorithm-evaluation
tldr: Compares deep learning (LSTM, MLP) and real-time data stream analysis (BEReTiC) for credit card fraud detection, finding deep learning achieves 92% accuracy but slower adaptation, while real-time clustering offers faster detection with lower false positives.
problem_and_motivation: Existing fraud detection methods either rely on batch-trained deep learning requiring extensive preprocessing and retraining, or real-time systems with lower initial accuracy. There is a lack of comprehensive empirical comparison between these paradigms on high-volume financial data. This gap prevents system designers from making informed deployment decisions.
approach:
  - Used two proprietary datasets: IND (17.5M individual transactions) and SUM (1.2M purchase summaries) with customer demographic and behavioral labels.
  - Injected 1000 synthetic fraudulent transactions by assigning average behavioral profiles of one customer to another customer's transactions.
  - Deep learning pipeline trained LSTM and MLP models to predict customer labels (e.g., total funds range) and computed Scale of Suspicious Transaction (SST) from ensemble misclassification consensus.
  - Real-time pipeline used BEReTiC system with dynamic clustering (CluNN algorithm), Gower similarity, and SCoDe2 deviation detection, processing raw streams without preprocessing.
  - Evaluated both on classification accuracy per label, fraud detection rate, false positives, and misclassification rate.
findings:
  - "num: Deep learning LSTM achieved 92% accuracy predicting total funds range and 86% for age range."
  - "num: Deep learning detected 788 of 1000 injected fraudulent transactions with 1340 false positives (0.007% misclassification rate)."
  - "num: Real-time clustering detected 619 of 1000 injected frauds with 574 false positives (0.003% misclassification rate)."
  - Real-time clustering had lower classification accuracy (e.g., 66% for total funds range) due to cold-start before building customer fingerprints.
  - Real-time approach required no data cleansing, adapted instantly to new fraud patterns via concept drift detection, and had lower latency.
  - Hybrid model integrating offline deep learning with online clustering is proposed to combine high accuracy and real-time adaptability.
key_figures_tables:
  - "Table 1: Classification accuracy by label for LSTM, MLP, and real-time clustering → LSTM highest at 92% for total funds range."
  - "Table 2: Fraud detection performance → Deep learning detected more frauds (788 vs 619) but more false positives (1340 vs 574)."
  - "Table 3: Methodology trade-offs → Deep learning high accuracy/high latency vs real-time moderate accuracy/low latency."
key_equations:
  - equation: "SST = \\frac{\\text{# misclassifying classifiers}}{\\text{total classifiers}}"
    explanation: "Scale of Suspicious Transaction from 0 to 1."
definitions:
  - term: BEReTiC
    definition: "Best Effort Real-Time Clustering and Classification adapter, a patented system for streaming data analysis."
  - term: SST
    definition: "Scale of Suspicious Transaction, percentage of classifiers that misclassified a transaction's customer labels."
  - term: SLT
    definition: "Scale of Legitimate Transaction, complement of SST."
  - term: CSST
    definition: "Confidence of SST, product of individual classifier accuracies comprising the SST."
  - term: SCoDe2
    definition: "Sample collector and deviation detector module that monitors stream statistics."
  - term: CluNN
    definition: "Clustering algorithm used by BEReTiC for dynamic cluster formation."
  - term: Gower similarity
    definition: "Metric combining categorical and numerical data for similarity comparisons."
  - term: LSTM
    definition: "Long Short-Term Memory recurrent neural network for time series."
  - term: MLP
    definition: "Multilayer perceptron, a simple feedforward neural network."
critical_citations:
  - "[Polytarchos et al., 2024] — Patent describing BEReTiC methodology."
  - "[Goodfellow et al., 2020] — Foundational GAN paper for synthetic data generation."
  - "[Large et al., 2019] — Ensemble weighting scheme used for SST."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      justification: "Paper classifies customers into categories (total funds range, age, occupation) using transaction patterns."
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      justification: "Core focus is detecting fraudulent transactions as anomalies in spending behavior."
    - code: 8.B
      name: Anomaly Detection Algorithm
      justification: "Compares LSTM-based and BEReTiC clustering algorithms for anomaly detection."
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      justification: "Provides comparative evaluation methodology with accuracy, false positives, and misclassification rate."
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: "Evaluates both batch deep learning and real-time streaming modules side-by-side."
  contribution: "This paper directly informs Odin's anomaly detection module by providing empirical comparison between batch-trained deep learning and real-time streaming clustering. The SST metric offers a method to quantify transaction suspiciousness using ensemble classifier consensus. The BEReTiC system demonstrates how raw transaction streams can be processed without cleansing, enabling instant fraud alerts. The proposed hybrid model suggests Odin could use offline LSTM for baseline scoring and online clustering for adaptive drift handling."
  directly_justifies:
    - "Deep learning models can achieve 92% accuracy in classifying customer financial behavior patterns from transaction history."
    - "Real-time clustering on raw data streams achieves lower false positive rate (0.003%) than batch deep learning (0.007%) for fraud detection."
    - "A hybrid model combining offline deep learning with online clustering is proposed for optimal fraud detection performance."
    - "Cold-start in real-time systems reduces initial classification accuracy until sufficient customer fingerprint is built."
  limits:
    - "Real-time clustering accuracy (66% for total funds) is substantially lower than deep learning (92%) due to cold-start."
    - "Dataset is proprietary and not publicly available, limiting reproducibility."
    - "Only two deep learning architectures (LSTM, MLP) were compared; no comparison to existing production fraud systems."
    - "Synthetic fraud injection may not fully represent real-world fraud patterns."
  mapping_rationale: "Functional domains screened: anomaly detection (primary), behavioral profiling (customer label classification), system evaluation (comparative study). Selected topic codes: 5.A (behavioral profiles via customer classification into total funds range, age, etc.), 8.A and 8.B (core anomaly detection for fraudulent transactions, both algorithmic approaches), 12.A and 12.B (evaluation framework and algorithm comparison). Rejected codes: 6.A/6.B (no spending forecasting, only classification), 7.A/B/C (no budgeting), 9.A/B (no mobile design), 10.A/B (no privacy discussion), 11.A/B (no engagement/retention), 13.A/B (no savings/debt management). Borderline: 5.A is included because the paper explicitly predicts behavioral labels (e.g., 'total funds range' as a proxy for financial capacity)."
limitations:
  - "Real-time clustering suffers from cold-start: initial customer fingerprints are incomplete, lowering early accuracy. [acknowledged]"
  - "Dataset is proprietary and not publicly available. [unacknowledged]"
  - "No comparison to existing production fraud detection systems or industry benchmarks. [unacknowledged]"
  - "Computational cost and latency measurements are not reported quantitatively. [unacknowledged]"
remember_this:
  - "Deep learning LSTM achieved 92% accuracy predicting customer total funds range."
  - "Real-time clustering detected 619 of 1000 frauds with only 574 false alarms."
  - "Hybrid integration of batch and streaming methods is proposed as future direction."
  - "Real-time approach requires no data cleansing and adapts to new fraud patterns instantly."
```