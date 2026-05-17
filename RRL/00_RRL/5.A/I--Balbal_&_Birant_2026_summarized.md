# RFM-Net: A Convolutional Neural Network for Customer Segment Classification

## Metadata

```yaml
---
paper_id: "10.3390/app16052223"
designation: algorithm-specific
title: "RFM-Net: A Convolutional Neural Network for Customer Segment Classification"
authors: "Balbal, K. F.; Birant, D."
year: 2026
venue: "Applied Sciences"
odin_topics: ["5.A", "5.C", "12.B"]
shorthand_tags: ["/profiling-role", "/classifier-candidates", "/classifier-eval-metrics", "/eval-ml-design"]
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

RFM-Net, a lightweight CNN trained on Recency-Frequency-Monetary features, classifies customers into seven segments with **94.33% accuracy**, outperforming prior methods by 13.17%.

## Problem and Motivation

Traditional RFM-based segmentation relies on rule-based logic that struggles to capture nonlinear patterns in customer behavior. Deep learning offers stronger generalization but is rarely applied to structured RFM data. No prior work combined a compact CNN with RFM rules for supervised customer segment classification.

## Approach

- Dataset: Online Retail I (541,909 records, UK e‑commerce, 2010–2011) and Online Retail II (1,067,371 records).
- RFM feature engineering: Recency (days since last purchase), Frequency (invoice count), Monetary (total spend) → discretized into 1–5 scores per quintile thresholds.
- Label generation: Rule‑based mapping of RFM score triplets to seven segments (Champions, Loyal, Potential Loyalists, Need Attention, About to Sleep, At Risk, Hibernating).
- CNN architecture: 2 Conv2D layers (32 then 64 filters), MaxPooling2D, Flatten, Dense(64), Softmax output (7 classes). Only 6,823 trainable parameters.
- Evaluation: 10‑fold cross‑validation, weighted accuracy, precision, recall, F‑measure.

## Findings

1. RFM‑Net achieved **94.33% weighted accuracy** (10‑fold CV) on Online Retail I.
2. Weighted precision = 0.9466, recall = 0.9433, F‑measure = 0.9429.
3. Relative accuracy improvement of **13.17%** over previously reported results on the same dataset.
4. Two‑layer CNN with learning rate 0.01 and 32 filters gave optimal performance; deeper layers reduced accuracy.

- Recency ranked as most important feature (importance score 0.5358), followed by Frequency (0.4217) and Monetary (0.2642).

## Key Figures and Tables

- Figure 4: Feature importance → R > F > M, matches churn prediction literature.
- Figure 5: Confusion matrix → Champions 94.3% correct; Potential Loyalists 96.9% correct.
- Table 9: Comparative results → RFM‑Net (94.33%) beats PARM (90%), Ret‑DNN (90%), XGBoost (92.1%).
- Table 10: Baseline comparison → RFM‑Net outperforms LR (90.32%), MLP (85.5%), KNN (92.39%), Bagging DT (90.68%).

## Key Equations

$$R_c = (d_{ref} - d_c^{last}).days$$
*Recency = days since customer’s last purchase.*

$$F_c = | \{ x.InvoiceNo \mid \forall x \in T_c \} |$$
*Frequency = count of unique invoices per customer.*

$$M_c = \sum_{x \in T_c} (x.Quantity \times x.UnitPrice)$$
*Monetary = total spending across all transactions.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| RFM | Recency, Frequency, Monetary — three metrics summarizing customer transaction behavior. |
| CNN | Convolutional Neural Network — a deep learning model that learns local patterns in input features. |
| Champions | Highest‑value segment: very recent, frequent, high‑spending customers. |
| Hibernating | Lowest‑value segment: long inactive, low frequency and spend. |
| Weighted accuracy | Accuracy averaged across classes, weighted by class size — accounts for class imbalance. |

## Critical Citations

- [Christy et al., 2021] — Foundation for RFM ranking as an effective customer segmentation approach.
- [Talaat et al., 2023] — Prior RFM + deep learning integration; RFM‑Net improves upon its accuracy (87.6% → 94.33%).
- [Chen et al., 2012] — Original source of the Online Retail dataset used in RFM‑Net.

## Relevance to Odin

**Topics:**

5.A — Financial Behavioral Profiles in Personal Finance

5.C — Financial Behavioral Profile Classification Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly supports Odin’s financial behavioral profiling module by demonstrating that a lightweight CNN can classify users into behavioral segments using only three transaction-derived features (Recency, Frequency, Monetary). The finding that Recency is the most important predictor (importance 0.5358) informs feature selection for Odin’s profile classification — recency of spending (days since last transaction) may be a strong signal for user engagement state. The paper’s comparative benchmarking against MLP, logistic regression, and tree‑based models provides empirical justification for considering a compact CNN over traditional classifiers when the feature space is small but interactions are nonlinear.

**Directly justifies:**

- “A two‑layer CNN with 32 filters achieves 94.33% accuracy classifying users into seven behavioral segments using only Recency, Frequency, and Monetary features.”
- “Recency is the most important predictor of customer segment (importance 0.5358), followed by Frequency (0.4217) and Monetary (0.2642).”
- “Shallow CNNs (2–3 layers) outperform deeper architectures on low‑dimensional structured financial data, as deeper layers increase overfitting and reduce accuracy.”
- “RFM‑Net’s total parameter count of 6,823 (≈26.65 KB) enables real‑time inference on mobile devices, supporting mobile‑first deployment.”

**Limits of relevance:**

- Dataset is UK e‑commerce retail, not Philippine personal finance — spending patterns (e.g., gift purchases vs. daily essentials) differ.
- Segments are defined by marketing taxonomy (Champions, Hibernating), not directly aligned with Odin’s budget‑based behavioral profiles.
- Labels are derived from rule‑based RFM scores, introducing circularity; the CNN learns an expert mapping rather than discovering latent structures.
- No evaluation on cold‑start users — the dataset assumes established transaction histories.

## Limitations

- Labels generated from RFM rules, then used as ground truth for CNN — model learns a predefined mapping rather than discovering new segments. [unacknowledged]
- Feature set limited to R, F, M; does not include demographic or category‑level spending data that could improve profile granularity.
- Dataset from UK retail (2010–2011) may not generalize to 2020s Filipino young professionals with different spending habits and digital behaviors.
- No temporal validation or concept drift analysis — segment stability over time not assessed.
- Model interpretability is limited compared to rule‑based RFM; the paper suggests future SHAP/LIME integration.

## Remember This

- 🔑 **94.33% accuracy** — lightweight CNN (6,823 params) beats prior methods by 13.17%.
- 📌 Recency drives classification most (0.536 importance) — “last spend date” is your strongest signal.
- 💡 Two‑layer CNN outperforms deeper nets — shallow is better for low‑dim structured finance data.
- ⚠️ Labels come from RFM rules, not ground truth — model learns expert mapping, not latent segments.
- 🧠 RFM features alone (no demographics) achieve high accuracy — strong baseline for Odin’s profiling module.
