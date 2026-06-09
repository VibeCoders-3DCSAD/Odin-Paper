```yaml
paper_id: 10.1016/j.jeconc.2025.100127
designation: international
title: Harnessing artificial intelligence and machine learning for fraud detection and prevention in Nigeria
authors: Odufisan, O.I.; Abhulimen, O.V.; Ogunti, E.O.
year: 2025
venue: Journal of Economic Criminology
odin_topics:
- 8.A
- 8.B
- 10.A
- 10.B
shorthand_tags:
- /anomaly-detection
- /ml-fraud
- /data-privacy
- /user-trust
tldr: AI and ML methods improve fraud detection in Nigeria by analyzing large datasets for anomalies, enabling real-time prevention across banking, e-commerce, healthcare, and education.
problem_and_motivation: Traditional rule-based fraud detection fails to adapt to evolving schemes and cannot handle large data volumes. Fraud costs Nigeria billions and erodes trust in digital services. A more adaptive, intelligent solution is needed.
approach:
- This is a literature review synthesizing secondary data from academic publications, industry reports, and global fraud studies.
- It categorizes AI/ML methods into supervised learning (labeled data), unsupervised learning (anomaly detection), and deep learning (CNNs, RNNs).
- Applications are examined across banking, e-commerce, healthcare, and education sectors in Nigeria.
- Benefits such as real-time analysis, scalability, reduced false positives, and hidden pattern detection are discussed.
- Challenges including data quality, system integration, evolving fraud tactics, and regulatory compliance are analyzed.
findings:
- "num: Online payment fraud is projected to cost firms globally over $343 billion between 2023 and 2027."
- "num: 24 Nigerian commercial banks lost N5.79 billion to fraud in Q2 2023, a 1125% increase from Q1."
- "num: Support Vector Machines achieved over 98% accuracy for phishing email detection."
- "num: A feed-forward neural network achieved a 97% detection rate for fraudulent credit card transactions and phishing websites."
- AI systems enable real-time monitoring, flagging suspicious activity before financial harm occurs.
- Unsupervised learning detects novel fraud schemes not conforming to known patterns.
- Deep learning models like CNNs and RNNs excel at analyzing sequential transaction data and document forgeries.
- Challenges include data privacy regulations (NDPR), algorithmic bias, and integration with legacy systems.
key_figures_tables:
- None.
key_equations:
- equation: None.
  explanation: ""
definitions:
- term: Artificial Intelligence (AI)
  definition: Capability of machines to imitate human intelligence, including reasoning, pattern recognition, and adaptation.
- term: Machine Learning (ML)
  definition: Subset of AI where algorithms learn patterns from data without explicit programming.
- term: Supervised Learning
  definition: ML using labeled data (fraudulent/valid) to train models that classify new transactions.
- term: Unsupervised Learning
  definition: ML that finds hidden patterns or anomalies in unlabeled data, useful for novel fraud schemes.
- term: Deep Learning
  definition: Advanced ML using neural networks (CNNs, RNNs) to process vast data and extract intricate patterns.
- term: Anomaly Detection
  definition: Technique identifying outliers or deviations from normal behavior in datasets.
critical_citations:
- "[Sarker, 2021] — Defines ML and its subset relationship to AI."
- "[Hilal et al., 2022] — Reviews anomaly detection techniques for financial fraud."
- "[Bansal et al., 2024] — Discusses real-time AI analysis and reduced false positives."
- "[Akintaro, 2023] — Reports Nigerian banking fraud loss statistics."
relevance:
  topics:
  - code: 8.A
    name: Anomaly Detection in Personal Finance Systems
    justification: Paper reviews supervised, unsupervised, and deep learning anomaly detection for fraudulent transactions.
  - code: 8.B
    name: Anomaly Detection Algorithm
    justification: Discusses specific algorithms (SVM, Random Forest, neural networks) for fraud detection.
  - code: 10.A
    name: Data Privacy and Security in Personal Finance Systems
    justification: Highlights challenges including data privacy regulations (NDPR) and security requirements.
  - code: 10.B
    name: User Trust in Personal Finance Systems
    justification: States fraud undermines trust in digital financial services and AI can help restore trust.
  contribution: This paper provides a comprehensive review of AI/ML fraud detection methods applicable to financial systems. It identifies anomaly detection as a key technique for real-time transaction monitoring, directly informing Odin's anomaly detection module. The discussion of challenges like data privacy, system integration, and algorithmic bias guides Odin's design for user trust and compliance. Quantitative findings on fraud losses justify the need for robust detection. The taxonomy of supervised, unsupervised, and deep learning helps select appropriate algorithms for Odin's spending anomaly detection.
  directly_justifies:
  - AI systems can analyze transaction data in real-time to flag suspicious activity before financial harm occurs.
  - Supervised learning models trained on historical fraud data can identify patterns and predict future fraudulent transactions.
  - Unsupervised learning detects novel fraud schemes that do not conform to known patterns.
  - Deep learning with RNNs can analyze sequences of transactions to uncover complex fraud typologies.
  - Cross-sector collaboration and data sharing enhance detection of sophisticated fraud networks.
  limits:
  - Data quality and availability remain significant barriers in developing economies.
  - Integrating AI with legacy banking systems requires major investment and planning.
  - Fraudsters continuously evolve tactics, requiring constant retraining of models.
  - Privacy regulations (e.g., NDPR) limit access to large training datasets.
  - Algorithmic bias may unfairly target certain customer segments.
  - The paper is a literature review and does not provide empirical validation of specific models on Nigerian transaction data. [unacknowledged]
  - The authors used ChatGPT for language improvement, which could introduce subtle biases not discussed. [unacknowledged]
  mapping_rationale: This paper focuses on fraud detection using AI/ML, directly supporting Odin's anomaly detection domain (8.A, 8.B). It also addresses data privacy and user trust (10.A, 10.B) as key challenges. Topics related to spending forecasting (6.A, 6.B), budget recommendation (7.A-C), expense categorization (3.A, 3.B), behavioral profiling (5.A-C), retention (11.A, 11.B), and savings/debt (13.A, 13.B) are not covered. Borderline: behavior analysis for fraud is distinct from financial behavioral profiles (5.A), so rejected. The paper's Nigerian context is relevant for generalizability but not specific to Filipino young professionals (1.A-C).
limitations:
- Data quality and availability remain significant barriers in developing economies.
- Integrating AI with legacy banking systems requires major investment and planning. [unacknowledged]
- Fraudsters continuously evolve tactics, requiring constant retraining of models.
- Privacy regulations (e.g., NDPR) limit access to large training datasets.
- Algorithmic bias may unfairly target certain customer segments.
- The paper is a literature review and does not provide empirical validation of specific models on Nigerian transaction data. [unacknowledged]
- The authors used ChatGPT for language improvement, which could introduce subtle biases not discussed. [unacknowledged]
remember_this:
- Fraud cost Nigerian banks N5.79 billion in Q2 2023 alone.
- Unsupervised learning detects fraud patterns never seen before.
- AI reduces false positives compared to rigid rule-based systems.
- Real-time AI monitoring can stop fraudulent transactions as they occur.
- Cross-sector data sharing dramatically improves fraud detection accuracy.
```