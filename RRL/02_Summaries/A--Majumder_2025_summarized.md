# A Review of Anomaly Identification in Finance Frauds Using Machine Learning Systems

## Metadata

```yaml
---
paper_id: "10.48175/IJARSCT-25619"
designation: international
title: "A Review of Anomaly Identification in Finance Frauds Using Machine Learning Systems"
authors: "Majumder, R."
year: 2025
venue: "International Journal of Advanced Research in Science, Communication and Technology"
odin_topics: ["E.1", "E.2"]
shorthand_tags: ["/anomaly-taxonomy", "/anomaly-approaches", "/anomaly-tradeoffs", "/anomaly-ml-families"]
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[ ]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
---
```

## TL;DR

Supervised, semi-supervised, and unsupervised ML methods for financial fraud detection face key challenges: imbalanced datasets and adversarial attacks.

## Problem and Motivation

Traditional fraud detection methods are not adaptable to evolving fraudulent schemes, leading to significant economic losses and eroded public trust in financial institutions. A comprehensive review of machine learning approaches for anomaly identification across banking, insurance, and digital payments was missing to guide system design.

## Approach

- This is a literature review, not an experimental study, covering ML-based anomaly detection in financial fraud.
- Reviews three learning paradigms: supervised (requires labeled normal and anomalous data), semi-supervised (only normal labels), and unsupervised (no labels).
- Surveys algorithms: Logistic Regression, SVM, Decision Trees, Random Forest, KNN, Autoencoders, Isolation Forest, Graph Neural Networks.
- Covers anomaly types: point anomalies (individual outliers), contextual anomalies (normal in one context, abnormal in another), and collective anomalies (a set of connected outliers).
- Identifies key challenges: imbalanced data distributions, adversarial attacks designed to evade detection, and scalability/real-time processing requirements.

## Findings

- ML methods significantly outperform traditional rule-based systems in detecting complex, evolving fraud patterns.
- **Imbalanced datasets** (fraud cases much rarer than legitimate transactions) degrade supervised classifier performance and require specialized techniques.
- Adversarial attacks allow fraudsters to modify transaction patterns to evade detection models.
- Graph Neural Networks capture relational dependencies in linked financial transactions, addressing a key limitation of attribute-value models.
- Unsupervised methods (Isolation Forest, Autoencoders) detect novel fraud patterns without labeled data, ideal for cold-start scenarios.
- Future directions include Explainable AI (XAI), federated learning for privacy preservation, and hybrid ensemble models.

## Key Figures and Tables

- Figure 1: Anomaly detection techniques (supervised, semi-supervised, unsupervised) → Three learning paradigms with different data-labeling requirements.
- Figure 2: Types of anomaly (identity theft, payment fraud, credit card fraud, investment fraud) → Fraud manifests across multiple financial domains.
- Figure 3: Machine learning models (LR, SVM, DT, RF, KNN) → Common algorithms applicable to fraud detection.
- Figure 4: Challenges of financial fraud (imbalanced data, adversarial activities, scalability/real-time) → Three primary technical barriers to deployment.
- Table 1: Summary of anomaly detection studies → Comparative overview of recent ML approaches, datasets, and limitations.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Anomaly detection | Identifying data points that deviate significantly from expected patterns, often signaling fraud. |
| Supervised learning | Training a model on labeled examples of both normal and fraudulent transactions. |
| Semi-supervised learning | Training only on normal transaction data; anything that doesn't fit is flagged as anomalous. |
| Unsupervised learning | Finding anomalies without any labels, assuming anomalies are rare and distinct from normal data. |
| Imbalanced data | A dataset where one class (e.g., fraud) has far fewer examples than another (e.g., legitimate). |
| Adversarial attack | Deliberate manipulation of transaction data to fool a fraud detection model. |
| Graph Neural Network (GNN) | A neural network that operates on graph-structured data, capturing relationships between entities. |
| Isolation Forest (IF) | An unsupervised algorithm that isolates anomalies by randomly partitioning data. |
| Autoencoder (AE) | A neural network that learns to reconstruct normal data; poor reconstruction indicates an anomaly. |

## Critical Citations

- [Ashtiani & Raahemi, 2022] — Systematic literature review on ML and data mining for financial statement fraud detection.
- [Pourhabibi et al., 2020] — Foundational review of graph-based anomaly detection approaches for fraud.
- [Ali et al., 2022] — Comprehensive systematic literature review on ML for financial fraud detection across domains.

## Relevance to Odin

**Topics:**

E.1 — Anomaly Detection in Personal Finance Systems

E.2 — Anomaly Detection Algorithm

**Contribution to Odin:**

This paper directly supports Odin's anomaly detection module by surveying ML methods applicable to financial transaction anomalies, including Isolation Forest and Autoencoders. The review justifies the consideration of unsupervised approaches for Odin's cold-start problem, where no labeled fraud data exists for new users. The detailed discussion of imbalanced data challenges and adversarial attack vulnerabilities informs Odin's algorithm selection and the need for adaptive models that can evolve as fraud patterns change.

**Directly justifies:**

- "Unsupervised anomaly detection methods (Isolation Forest, Autoencoders) can identify fraudulent patterns without requiring labeled training data, making them suitable for cold-start user profiles."
- "Imbalanced datasets where fraudulent transactions constitute a tiny fraction of all transactions severely degrade the performance of supervised classifiers."
- "Adversarial attacks can manipulate transaction features to evade detection, requiring fraud models to be adversarially robust or continuously retrained."
- "Graph Neural Networks capture relational patterns in financial networks that traditional attribute-value models miss, relevant for detecting coordinated fraud across multiple transactions."
- "Real-time processing demands in financial fraud detection require scalable ML architectures that balance accuracy and latency."

**Limits of relevance:**

- The paper focuses on financial fraud (credit card, insurance, investment) rather than personal budget anomalies (e.g., overspending vs. behavioral drift) — but methods generalize.
- No empirical performance benchmarks are provided; this is a qualitative review, not a comparative study.
- The reviewed studies use transaction volumes far larger than a single-user personal finance app; Odin's scale differs.
- Adversarial attack discussion assumes sophisticated fraudsters; less relevant for personal budget anomaly detection in a non-banking app.
- Filipino-specific spending patterns or cultural obligations are not addressed.

## Limitations

- This is a review paper with no original experiments; claims are synthesized from prior work, not empirically validated.
- The paper does not provide comparative performance metrics (e.g., precision, recall, F1) for any reviewed algorithm. [unacknowledged]
- Real-time processing constraints specific to mobile devices (battery, compute) are not discussed. [unacknowledged]
- Federated learning and blockchain solutions are mentioned as future directions but not evaluated for practical deployment.
- The review does not address how anomaly detection systems handle concept drift (evolving normal behavior over time), which is critical for personal finance.

## Remember This

- 🔑 Unsupervised methods (Isolation Forest, Autoencoders) work without labeled fraud data — ideal for Odin's cold-start.
- 📌 Imbalanced data is the #1 challenge: fraud cases are rare, skewing supervised models.
- 💡 Adversarial attacks can fool detectors; Odin's anomaly module must be adaptable.
- 🧠 Graph Neural Networks capture transaction relationships — relevant for detecting complex fraud patterns.
- ✅ This is a qualitative review, not an empirical benchmark — use for method justification, not performance numbers.
