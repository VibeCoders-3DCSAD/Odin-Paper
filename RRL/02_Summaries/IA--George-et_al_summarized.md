```yaml
paper_id: 10.63125/913ksy63
designation: international
title: MACHINE LEARNING FOR FRAUD DETECTION IN DIGITAL BANKING: A SYSTEMATIC LITERATURE REVIEW
authors: George, M. Z. H.; Alam, M. K.; Hasan, M. T.
year: 2023
venue: ASRC Procedia: Global Perspectives in Science and Scholarship
odin_topics:
  - 8.A
  - 8.B
  - 12.A
  - 12.B
shorthand_tags:
  - /anomaly-detection
  - /anomaly-detection-algorithm
  - /evaluation-frameworks
  - /evaluation-metrics
tldr: Supervised learning dominates digital banking fraud detection, but deep learning, anomaly detection, and hybrid models show superior adaptability for imbalanced transaction data.
problem_and_motivation: Rule-based fraud detection systems are rigid and unable to adapt to evolving fraud tactics in digital banking. Machine learning offers scalability and predictive accuracy, yet prior reviews lack integration of deep learning, hybrid models, and cross-regional comparisons. A systematic synthesis is needed to consolidate fragmented evidence across methodological and regulatory contexts.
approach:
  - The study followed PRISMA guidelines for systematic literature review, covering Scopus, Web of Science, IEEE Xplore, ACM Digital Library, and SSRN.
  - Search terms combined machine learning, fraud detection, digital banking, anomaly detection, and deep learning with Boolean operators.
  - Initial identification yielded 2,346 records; after deduplication, screening, and eligibility review, 118 studies were included.
  - Included studies were categorized into supervised learning (n=36), unsupervised/anomaly detection (n=27), hybrid models (n=19), deep learning (n=21), and evaluation/interpretability (n=15).
  - Cross-regional analysis examined Europe (PSD2/GDPR), North America (fintech-led), and emerging economies (infrastructure-dependent).
findings:
  - num: 36 supervised learning studies accumulated over 9,200 citations, confirming dominance of decision trees, logistic regression, and SVMs.
  - num: 27 unsupervised learning studies received over 6,800 citations, essential for detecting novel fraud patterns without labels.
  - num: 21 deep learning studies (RNNs, CNNs, autoencoders) garnered over 7,300 citations, enabling sequential transaction modeling.
  - num: 19 hybrid model studies exceeded 5,600 citations, demonstrating superior precision‑recall balance and adaptability.
  - Evaluation metrics must prioritize PR‑AUC and cost‑sensitive measures over accuracy due to extreme class imbalance.
  - Explainability frameworks (SHAP, LIME) are critical for regulatory compliance and user trust in black‑box models.
  - European fraud analytics is shaped by PSD2/SCA and GDPR, North America by model risk governance and API ecosystems, emerging economies by mobile‑first adoption and infrastructure maturity.
key_figures_tables:
  - Figure 1: Digital Banking Fraud Detection Framework → Overview of fraud types and detection components.
  - Figure 4: Fraud Detection Machine Learning Framework → Classification of supervised, unsupervised, deep learning paradigms.
  - Figure 5: Deep Learning Fraud Detection Framework → Sequence models and representation learning for transaction monitoring.
  - Figure 7: Real-Time Banking Fraud Detection Framework → Latency constraints and threshold tuning.
  - Figure 12: Fraud Detection Research Trends Analysis → Citation growth across supervised, unsupervised, deep, hybrid methods.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Fraud detection
    definition: Identification and classification of fraudulent transactions after they occur in digital banking systems.
  - term: Supervised learning
    definition: ML paradigm using labeled transaction data to train classifiers like decision trees or SVMs.
  - term: Unsupervised learning
    definition: ML approach detecting anomalies without labeled examples, using clustering or density estimation.
  - term: Anomaly detection
    definition: Identifying statistical deviations from normal behavior to flag potential fraud.
  - term: PR-AUC
    definition: Precision‑recall area under curve, preferred over ROC‑AUC for highly imbalanced fraud datasets.
critical_citations:
  - "[Ngai et al., 2011] — Early survey establishing supervised learning in fraud detection."
  - "[Carcillo et al., 2021] — Demonstrated hybrid unsupervised‑supervised reduces false positives."
  - "[Lundberg & Lee, 2017] — SHAP framework for model explainability in finance."
  - "[Krawczyk, 2016] — Foundational work on imbalanced learning challenges."
relevance:
  topics:
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      justification: Paper reviews unsupervised anomaly detection for identifying novel fraud patterns in transaction data.
    - code: 8.B
      name: Anomaly Detection Algorithm
      justification: Compares clustering, DBSCAN, autoencoders, and graph neural networks for fraud anomaly detection.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      justification: Emphasizes PR‑AUC, F1‑score, and cost‑sensitive metrics over accuracy for imbalanced fraud data.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: Details interpretability tools (SHAP/LIME) and cross‑regional performance benchmarking.
  contribution: The systematic review provides Odin’s anomaly detection module with empirical evidence that hybrid models (supervised+unsupervised) outperform single‑paradigm detectors on imbalanced transaction data. For Odin’s evaluation framework, it justifies using PR‑AUC and cost‑sensitive thresholds instead of accuracy. The cross‑regional analysis informs Odin’s design for Philippine young professionals by highlighting how regulatory and infrastructure contexts shape feature engineering and real‑time deployment constraints.
  directly_justifies:
    - Hybrid models combining supervised and unsupervised learning reduce false positives while improving recall in fraud detection.
    - PR‑AUC is a more reliable metric than ROC‑AUC for evaluating models on highly imbalanced financial datasets.
    - Explainability frameworks like SHAP and LIME are necessary for regulatory compliance in personal finance systems.
    - Deep learning architectures (RNN, CNN) capture sequential transaction patterns that traditional classifiers miss.
  limits:
    - Reproducibility is limited by private banking datasets and opaque feature pipelines [unacknowledged].
    - Robustness under distributional shift and adversarial manipulation is inconsistently assessed across studies [unacknowledged].
    - Theoretical integration with criminological frameworks (e.g., fraud triangle) is underutilized in computational models.
    - Cross‑dataset and cross‑jurisdiction generalization is infrequently examined, limiting portability claims.
  mapping_rationale: The paper focuses on machine learning for fraud detection, which directly maps to Odin’s anomaly detection domain (8.A, 8.B) because fraud detection is a canonical anomaly detection task in personal finance. The systematic review also heavily discusses evaluation metrics (precision, recall, PR‑AUC, cost sensitivity) and interpretability frameworks, which fall under system evaluation (12.A, 12.B). Topics related to behavioral profiling (5.A‑C), spending forecasting (6.A‑B), budget recommendation (7.A‑C), expense categorization (3.A‑B), mobile design (9.A‑B), user retention (11.A‑B), and savings/debt management (13.A‑B) were rejected because the paper does not provide citeable claims in those domains. Data privacy (10.A‑B) is mentioned but not as a central finding, so it was excluded.
limitations:
  - Extreme class imbalance handling remains uneven; many studies report results without calibrated costs.
  - ROC‑AUC persists as a headline metric even when PR‑AUC is more decision‑relevant for skewed data.
  - Reproducibility constrained by private datasets; few studies release code or standardized benchmarks. [unacknowledged]
  - Robustness to distributional shift and adversarial manipulation is inconsistently assessed.
  - Theoretical articulation lags empirical progress; criminological constructs are rarely formalized in models. [unacknowledged]
remember_this:
  - Supervised learning accounts for 36 of 118 reviewed studies.
  - Deep learning models exceed 7,300 citations despite recent publication.
  - Hybrid models outperform single‑paradigm detectors in precision‑recall balance.
  - PR‑AUC is preferred over ROC‑AUC for imbalanced fraud data.
  - Explainability frameworks are essential for regulated banking environments.
```