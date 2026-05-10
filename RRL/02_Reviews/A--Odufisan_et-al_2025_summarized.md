# Harnessing artificial intelligence and machine learning for fraud detection and prevention in Nigeria

## Metadata

```yaml
---
paper_id: "10.1016/j.jeconc.2025.100127"
designation: international
title: "Harnessing artificial intelligence and machine learning for fraud detection and prevention in Nigeria"
authors: "Odufisan, O. I.; Abhulimen, O. V.; Ogunti, E. O."
year: 2025
venue: "Journal of Economic Criminology"
odin_topics: ["E.1", "E.2", "H.1"]
shorthand_tags: ["/anomaly-ml-families", "/anomaly-approaches", "/anomaly-tradeoffs", "/data-sensitivity"]
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[X]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
---
```

## TL;DR

AI and ML detect fraud in real time via anomaly detection, behavior analysis, and risk scoring, outperforming static rule-based systems across Nigeria’s banking, e‑commerce, healthcare, and education sectors.

## Problem and Motivation

Static rule‑based and manual fraud detection methods cannot adapt to rapidly evolving fraud schemes, leaving organizations vulnerable. Fraud undermines trust, diverts resources, and stifles innovation, with Nigerian banks alone losing N5.79 billion to fraud in Q2 2023. Prior work lacked a comprehensive review of AI/ML applications across multiple Nigerian sectors and their specific fraud typologies.

## Approach

- Data sources: secondary from academic publications, industry reports, government records, and global fraud studies; primary via unstructured interviews with Nigerian stakeholders.
- Supervised learning: trains on labeled historical fraud data to classify new transactions (e.g., credit card fraud detection).
- Unsupervised learning: uses anomaly detection to uncover novel fraud patterns without labeled examples.
- Deep learning: CNNs analyze images (signatures/IDs) for forgeries; RNNs analyze sequential transaction patterns.
- Applications: user authentication (biometrics), behavior analysis (spending baselines), anomaly detection (real‑time deviation), risk scoring, and text analysis (phishing detection).

## Findings

1. Nigerian commercial banks’ fraud losses rose **1,125%** from Q1 to Q2 2023, totaling N5.79 billion; fraudulent loans accounted for 94.35% of losses.
2. Global online payment fraud is projected to reach $107 billion by 2029, a 14% increase from 2024.
3. A deep learning feed‑forward neural network achieved a **97% detection rate** for fraudulent credit card transactions and phishing websites.
4. SVM for phishing email detection achieved over 98% accuracy using text analysis.

- AI systems enable real‑time analysis, scalability to massive datasets, reduced false positives, and detection of subtle hidden patterns.
- Fraudsters constantly adapt, requiring continuous retraining of AI models; static AI systems become vulnerable.

## Key Figures and Tables

None.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| AI | Artificial intelligence – machines that mimic human reasoning, learning, and pattern recognition. |
| ML | Machine learning – a subset of AI where algorithms learn patterns from data without explicit rules. |
| Supervised learning | Training on labeled data (fraud/legitimate) to classify new examples. |
| Unsupervised learning | Finds hidden patterns or anomalies without labeled outcomes. |
| Deep learning | ML using multi‑layer neural networks (CNNs, RNNs) to extract complex features. |
| CNN | Convolutional neural network – excels at image pattern recognition (e.g., forgery detection). |
| RNN | Recurrent neural network – analyzes sequential data (e.g., transaction timelines). |
| Anomaly detection | Identifying data points that deviate significantly from normal patterns. |
| False positive | A legitimate transaction incorrectly flagged as fraudulent. |

## Critical Citations

- [Sarker, 2021] – Foundational taxonomy of ML algorithms and real‑world applications.  
- [Hilal et al., 2022] – Comprehensive review of anomaly detection techniques for financial fraud.  
- [Bansal et al., 2024] – Argues real‑time analysis and scalability as key AI advantages over rule‑based systems.  
- [Afriyie et al., 2023] – Demonstrates supervised learning’s effectiveness for credit card fraud prediction.  

## Relevance to Odin

**Topics:**

E.1 — Anomaly Detection in Personal Finance Systems

E.2 — Anomaly Detection Algorithm

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

**Contribution to Odin:**

This paper directly validates the use of unsupervised anomaly detection and behavior analysis for identifying unusual financial transactions, which parallels Odin’s need to detect spending anomalies. It benchmarks supervised and deep learning methods (97% detection rate) that Odin could adapt for user profile classification or expense categorization. The discussion of data privacy regulations (Nigeria Data Protection Regulation) and ethical biases in AI models reinforces Odin’s requirement for privacy‑by‑design and transparent logging.

**Directly justifies:**

- “Unsupervised anomaly detection identifies novel fraud patterns without labeled training data, making it applicable to cold‑start user profiles in personal finance systems.”
- “Feed‑forward neural networks achieve 97% detection accuracy for fraudulent transactions, supporting deep learning as a candidate for Odin’s anomaly detection algorithm.”
- “Real‑time analysis of transaction sequences using RNNs can flag unusual spending patterns before financial harm occurs.”
- “Reducing false positives through continuous model retraining is essential for maintaining user trust in automated financial alerts.”

**Limits of relevance:**

- Findings are from Nigerian fraud detection (banking, e‑commerce, healthcare, education), not directly from personal spending behavior or budgeting contexts.
- The 97% detection rate comes from a study on credit card fraud and phishing, not on spending anomalies within a budget management app.
- Nigerian data privacy regulations differ from Philippine law (Data Privacy Act of 2012), though the principle of privacy‑by‑design applies.
- The paper does not evaluate algorithm performance on sparse or irregular transaction data typical of manual‑input personal finance systems.

## Limitations

- Data quality and availability: AI models require large, high‑quality datasets; Nigerian financial data may be incomplete or siloed.
- Integration with legacy systems: replacing rule‑based fraud detection with AI requires costly infrastructure changes. [unacknowledged]
- Fraud tactics evolve continuously, requiring constant retraining; static AI models become obsolete quickly.
- Ethical concerns: algorithmic bias could unfairly target specific user groups; the paper notes this but offers no mitigation framework.
- No validation of these methods on Filipino spending data or personal budget management systems. [unacknowledged]

## Remember This

- 🔑 **97% detection rate** – deep learning (feed‑forward NN) beats traditional rules for fraud.
- 📌 Unsupervised anomaly detection works without labeled data – perfect for Odin’s cold‑start users.
- ⚠️ AI models need continuous retraining – fraudsters evolve; spending patterns drift, too.
- 💡 Real‑time analysis cuts false positives – critical for user trust in financial alerts.
- 🧠 Privacy laws (NDPR) and algorithmic bias are non‑negotiable design constraints.
