# AI-Enabled NLP Framework for Automated Expense Management and Financial Analysis

## Metadata

```yaml
---
paper_id: "10.15662/IJEETR.2026.0802073"
designation: algorithm-specific
title: "AI-Enabled NLP Framework for Automated Expense Management and Financial Analysis"
authors: "Jayaprakashnarayan, N.; Sakthivel, M.; Sachidhanandam, P.; Devi, N. K.; Mughilan, T. S. M."
year: 2026
venue: "International Journal of Engineering & Extended Technologies Research (IJEETR)"
odin_topics: ["A.2", "B.1", "E.1", "E.2", "G.1", "H.1", "J.1"]
shorthand_tags: ["/pfms-gap", "/mobile-ml-algo-selection", "/anomaly-approaches", "/anomaly-algo-justification", "/isolation-forest", "/cat-approaches", "/privacy-by-design", "/eval-frameworks", "/sus"]
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

A transformer-based NLP framework for automatic expense tracking from SMS achieves 96.8% entity extraction accuracy and 94.3% merchant precision using on-device multi-task learning.

## Problem and Motivation

Manual tracking of digital payments across multiple apps and banks is overwhelming, leading to disorganized spending and poor financial awareness. This lack of automated, accurate expense management reduces financial literacy and increases fraud exposure. Prior systems either relied on brittle rules or static cloud models that could not adapt to evolving message formats or preserve user privacy.

## Approach

- Dataset: 124,583 financial SMS messages from 250 participants (42 banks, 18 UPI apps, 23 credit cards) spanning 14 expense categories over 6 months.
- Model: MuRIL transformer (12 layers, 768 hidden) fine-tuned on multilingual and code-mixed (Hinglish) financial text.
- Multi-task learning: Joint entity extraction (BIO tagging with CRF) and transaction classification (14 categories) with loss weights λ_entity=0.7, λ_class=0.3.
- Uncertainty quantification: Token-level entropy and class margin thresholds to flag low-confidence predictions for human review.
- Fraud detection ensemble: Rule-based screening, Isolation Forest, and LSTM autoencoder with weighted voting; 0.917 sensitivity at 0.038 false positive rate.
- On-device deployment: 8-bit quantization (4× size reduction, 98.7% accuracy preserved), encrypted storage, and differential privacy for federated updates.

## Findings

1. Entity extraction achieved **0.968 F1** overall; amount and date extraction exceeded 0.98 F1.
2. Merchant extraction F1 = 0.952; reference number/UPI ID extraction F1 ≈ 0.94.
3. Transaction classification weighted F1 = 0.949; shopping category was hardest (0.924 F1).
4. Fraud detection ensemble sensitivity = 0.917 with 0.038 false positive rate (AUC = 0.956).

- Manual effort reduced by 85.6% based on user-reported time savings.
- On-device latency: 43–127ms across device tiers; battery impact 0.9–2.0%/hour.

## Key Figures and Tables

- Table I: Entity extraction model comparison → Proposed MuRIL multi-task F1=0.968 vs BiLSTM-CRF 0.888.
- Figure 1: Entity extraction performance by model → Transformer-based models outperform CRF and rule-based by >8 points.
- Figure 2: Entity-level F1 by type → Amount (0.988), Merchant (0.952), Reference (0.945).
- Figure 4: Fraud detection ROC curves → Ensemble AUC=0.956 beats individual detectors (LSTM autoencoder 0.94, Isolation Forest 0.91).

## Key Equations

$$L = \lambda_{entity} L_{entity} + \lambda_{class} L_{class}$$
*Combined loss balances entity CRF loss and classification cross-entropy (λentity=0.7, λclass=0.3).*

$$H_{token} = -\sum_{t \in tags} p(t|x) \log p(t|x)$$
*Token entropy measures prediction uncertainty; high entropy flags extraction as needing review.*

$$Margin = p(c_1|x) - p(c_2|x)$$
*Margin between top two class probabilities; low margin triggers human confirmation for categorization.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Entity extraction | Identifying pieces of a transaction: amount, date, merchant, account number. |
| MuRIL | Multilingual BERT model pre-trained on 17 Indian languages and code-mixed text. |
| Multi-task learning | Training one model to do entity extraction and transaction classification simultaneously. |
| Uncertainty quantification | The model flags when it is unsure (low margin, high entropy) for human review. |
| Isolation Forest | Anomaly detection algorithm that isolates outliers by randomly partitioning data. |
| LSTM autoencoder | Sequence model that learns normal patterns; high reconstruction error signals fraud. |
| UPI | Unified Payments Interface – India's instant payment system (similar to Philippine InstaPay). |
| Hinglish | Code-mixed Hindi-English text common in Indian financial SMS messages. |
| F1 score | Harmonic mean of precision and recall; 1.0 is perfect. |
| AUC‑ROC | Probability that a randomly chosen fraud case is ranked higher than a normal case. |

## Critical Citations

- [Hochreiter & Schmidhuber, 1997] — LSTM foundational work used for sequence-based fraud detection.  
- [Vaswani et al., 2017] — Transformer architecture enabling contextual SMS understanding.  
- [Devlin et al., 2019] — BERT pre-training framework adapted to financial domain.  
- [Kumar et al., 2019] — Prior rule-based SMS extraction baseline (0.89 accuracy) that our work outperforms.

## Relevance to Odin

**Topics:**

A.2 — Existing Personal Finance and Budget Management Systems

B.1 — Mobile-First Design in Personal Finance Systems

E.1 — Anomaly Detection in Personal Finance Systems

E.2 — Anomaly Detection Algorithm

G.1 — Expense Categorization in Filipino Personal Finance Contexts

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

J.1 — System Evaluation

**Contribution to Odin:**

This paper directly informs Odin’s expense categorization module by demonstrating that a transformer-based multi-task architecture (MuRIL) achieves 96.8% entity extraction accuracy on real-world SMS data, providing a reproducible baseline for automatic transaction parsing. The ensemble fraud detection framework (Isolation Forest + LSTM autoencoder + rule-based) with 91.7% sensitivity and 3.8% false positive rate justifies Odin’s candidate for anomaly detection, especially the inclusion of Isolation Forest for behavioral deviation. The on-device privacy architecture (quantization, encrypted storage, differential privacy) supports Odin’s design requirement of keeping user data local without banking integration. Finally, the reported System Usability Scale intent and battery/latency benchmarks provide concrete targets for Odin’s mobile-first evaluation under ISO 25010.

**Directly justifies:**

- “A MuRIL-based multi-task transformer achieves 96.8% F1 for extracting transaction entities (amount, date, merchant, account) from mixed-language SMS alerts in a mobile environment.”
- “An ensemble of rule-based screening, Isolation Forest, and LSTM autoencoder detects fraudulent transactions with 91.7% sensitivity and a 3.8% false positive rate on personal transaction streams.”
- “On-device 8-bit quantization reduces model size by 4× while preserving 98.7% of original accuracy, enabling sophisticated NLP on smartphones with 43–127ms latency and 0.9–2.0%/hour battery drain.”
- “Uncertainty quantification (token entropy and class margin) flags low-confidence extractions for human review, preventing automation errors in ambiguous cases.”

**Limits of relevance:**

- Study uses Indian financial messages (UPI, Hindi-English code-mixing); direct transfer to Filipino SMS (Taglish, InstaPay, GCash, Maya) requires validation on local data.
- On-device performance reported on mid-to-high-end Android devices (2–8GB RAM); low-end Philippine devices may experience higher latency or battery drain.
- Cold-start performance (first week of user data) is not evaluated; Odin’s new users may have sparse transaction history.
- Fraud detection ensemble assumes user correction feedback for online learning; Odin’s manual input model may reduce correction frequency.

## Limitations

- Geographic generalization: The dataset is exclusively Indian; Philippine message formats, languages, and payment systems (GCash, Maya, InstaPay) were not tested. [unacknowledged]
- No cold-start evaluation: The reported accuracy assumes historical transaction data; performance for a new user with zero prior messages is unknown. [unacknowledged]
- Manual effort reduction (85.6%) is self-reported; no controlled experiment validated this figure against objective tracking.
- Battery impact (0.9–2.0%/hour) aggregates across all devices; extreme usage (300+ messages/day) may exceed this range on low-end hardware.
- The study does not compare against commercial Filipino expense tracking apps (e.g., Money Lover, TimelyBills) using the same dataset.

## Remember This

- 🔑 **96.8% F1** for SMS transaction extraction – robust on-device NLP even with code-mixed text.  
- 📌 Fraud ensemble hits 91.7% sensitivity at 3.8% false positives – Isolation Forest + LSTM autoencoder works.  
- 💡 4× model size reduction via 8‑bit quantization – 98.7% accuracy preserved for mobile deployment.  
- ⚠️ India‑only dataset – Filipino message formats (GCash, Maya, Taglish) need separate validation.
