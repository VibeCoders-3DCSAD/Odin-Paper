# Digital Persona Modeling for Context-Aware Financial Decisioning

## Metadata

```yaml
---
paper_id: "a3f5c8e2-4b6d-4c8e-9a1b-2c3d4e5f6a7b"
designation: algorithm-specific
title: "Digital Persona Modeling for Context-Aware Financial Decisioning"
authors: "Sanhosh, S. R.; Singh, A. K."
year: 2025
venue: "International Journal of Research in Mulidisciplinary Technology"
odin_topics: ["A.2", "C.2", "D.2", "F.2", "H.1"]
shorthand_tags: ["/pfms-gap", "/budget-algo-justification", "/lstm-vs-alternatives", "/classification-vs-clustering", "/classifier-justification", "/privacy-by-design"]
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

LSTM achieves 93.6% accuracy and 92.9% F1-score for context-aware financial decisioning, outperforming Random Forest and K-Means on simulated mobile transaction data.

## Problem and Motivation

Static demographic profiles fail to capture dynamic user behavior and context, limiting financial decision systems to generic guidance. Real-time adaptation to location, device, and intent is necessary for personalized financial services. Existing systems lack a unified framework that integrates behavioral telemetry, psychographic attributes, and privacy-preserving machine learning.

## Approach

- Dataset: Simulated hybrid dataset combining transaction logs, mobile contextual logs (location, device, session time), user profiles, and feedback labels.
- Models: Random Forest for classification (decision type), LSTM for sequential pattern analysis (session time series), K-Means for persona grouping (spending style, risk tolerance).
- Architecture: Five layers – Data Acquisition, Context Engine, Persona Builder, Decisioning Model, and Decision Delivery & Feedback.
- Privacy: Federated learning and local processing to keep user data on device; Privacy Leakage Ratio (PLR) metric.
- Evaluation metrics: Accuracy, precision, recall, F1-score, and PLR.
- Context-aware risk function: R = α₁·C_location + α₂·C_time + α₃·C_device + β·T.

## Findings

1. LSTM Neural Net achieved the highest accuracy (93.6%) and F1-score (92.9%), outperforming Random Forest (91.2% accuracy, 90.1% F1) and K-Means (75.0% accuracy, 71.8% F1).
2. Random Forest performed well for interpretable rule generation on tabular financial history.
3. K-Means had lower F1 (71.8%) as expected for unsupervised clustering.

- Contextual integration (time, location, device) improved decision relevance over static demographic models.
- The proposed framework supports use cases including automated budgeting, micro-investment recommendations, credit risk evaluation, and fraud intent detection.

## Key Figures and Tables

- Table 2: Model performance comparison (accuracy, precision, recall, F1) → LSTM leads with 93.6% accuracy and 92.9% F1.
- Figure 2: System architecture diagram → five-layer pipeline from data acquisition to feedback loop.

## Key Equations

$$S(u,p) = \frac{1}{n} \sum_{i=1}^{n} \frac{|x_{u,i} - x_{p,i}|}{\max(x_i)}$$
*Persona similarity score — lower distance means closer match to predefined persona.*

$$R = \alpha_1 \cdot C_{\text{location}} + \alpha_2 \cdot C_{\text{time}} + \alpha_3 \cdot C_{\text{device}} + \beta \cdot T$$
*Real-time decision risk blends contextual variables and transaction amount.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| DPM | Digital Persona Modeling — dynamic user representation from behavior and context. |
| LSTM | Long Short-Term Memory [think: memory cell that learns what to forget] — sequential deep learning model. |
| RF | Random Forest — ensemble of decision trees for classification. |
| PLR | Privacy Leakage Ratio — measures privacy exposure in gradients (1 minus preserved fraction). |
| Context-aware risk function | Weighted sum of location, time, device, and transaction amount to compute real-time risk. |

## Critical Citations

- [Richardson, 2024] — Real-time payment system challenges in FinTech, grounding the need for adaptive financial decisioning.
- [Garg, Pandey & Pathak, 2024] — Multi-layered AI-IoT framework for adaptive financial services, supporting the proposed architecture.
- [Mishra & Jain, 2023] — IoT-driven customer intelligence for adaptive financial services, relevant to persona-based personalization.

## Relevance to Odin

**Topics:**

A.2 — Existing Personal Finance and Budget Management Systems

C.2 — Budget Recommendation Algorithm

D.2 — LSTM as the Spending Forecasting Algorithm

F.2 — Profile Classification Algorithm

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

**Contribution to Odin:**

This paper directly justifies Odin's selection of LSTM for the spending forecasting module by demonstrating LSTM's superior accuracy (93.6%) over Random Forest and K-Means on sequential transaction data. The persona clustering approach using K-Means provides a foundation for Odin's user profile classification module, showing how behavioral segmentation (spending style, risk tolerance) can be integrated with ML. The context-aware risk function models real-time user state (location, time, device) — applicable to Odin's anomaly detection and budget recommendation in mobile contexts. The privacy-preserving federated learning design (local processing, no raw data leaving device) aligns with Odin's requirement for manual input and local-only data handling.

**Directly justifies:**

- "LSTM achieves 93.6% accuracy and 92.9% F1-score for sequential financial behavior classification, outperforming Random Forest (91.2%) and K-Means (75%) on mobile transaction data."
- "Contextual variables (location, time, device) improve financial decision risk assessment via the function R = α₁C_location + α₂C_time + α₃C_device + βT."
- "K-Means clustering segments users into personas based on spending style and risk tolerance, supporting profile-based personalization without labeled training data."
- "Federated learning and local processing mechanisms preserve user privacy while enabling collaborative model training, measurable via Privacy Leakage Ratio."
- "Digital persona modeling enables real-time adaptation to user intent, device usage patterns, financial literacy indicators, and situational stress."

**Limits of relevance:**

- Dataset is simulated, not real Filipino transaction or spending data — performance on actual Filipino young professionals unknown.
- Contextual variables (GPS location, device type) may require permissions not always available or trusted by users in manual-input scenarios.
- No explicit evaluation of cold-start persona generation for new users with zero transaction history.
- Study focuses on general financial decisioning (credit risk, fraud) rather than personal budget management specifically.

## Limitations

- Heavy reliance on user data (behavior, location, transaction history) increases privacy breach risk — acknowledged but mitigation via federated learning is untested on real users.
- Limited dataset diversity (simulated only) may introduce bias and reduce model generalizability across populations — [unacknowledged].
- Deep learning (LSTM) interpretability remains a black box, reducing trust for regulatory audits — acknowledged.
- Context drift over time: user behavior evolves, requiring continuous learning mechanisms not fully addressed — acknowledged.
- No validation on Filipino cultural spending patterns or income volatility — [unacknowledged].

## Remember This

- 🔑 **LSTM: 93.6% accuracy, 92.9% F1** — beats Random Forest (91.2%) and K-Means (75%) on mobile transaction data.
- 📌 Context-aware risk = α·location + α·time + α·device + β·T — real-time adaptation works.
- 💡 Federated learning keeps data on device — aligns with Odin’s manual-input privacy design.
- ⚠️ Simulated dataset only — real Filipino spending behavior not tested.
