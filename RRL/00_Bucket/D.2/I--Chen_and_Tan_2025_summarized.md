# LSTM-Based Consumer Behavior Prediction Model Research

## Metadata

```yaml
---
paper_id: "10.1145/3785706.3785906"
designation: algorithm-specific
title: "LSTM-Based Consumer Behavior Prediction Model Research"
authors: "Chen, S.; Tan, W."
year: 2025
venue: "2025 2nd International Conference on Digital Economy and Computer Science (DECS 2025)"
odin_topics: ["D.1", "D.2"]
shorthand_tags: ["/forecasting-methods", "/spending-time-series", "/temporal-dependency", "/lstm-architecture", "/lstm-vs-alternatives", "/lstm-spending-applied", "/lstm-justification"]
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

Bidirectional LSTM with self-attention achieves **94.2% accuracy** predicting purchase intentions from 80M e-commerce interaction records, outperforming standard LSTM by 3.0 percentage points.

## Problem and Motivation

Traditional machine learning methods (linear regression, decision trees, SVMs) cannot effectively capture temporal dependencies and complex patterns in large-scale, multi-dimensional consumer behavior data. Accurate behavior prediction is critical for e-commerce personalization and inventory management, directly impacting sales revenue where recommendation systems contribute over 35% of sales. Prior work had not systematically applied bidirectional LSTM with attention mechanisms to consumer purchase intention prediction across diverse user segments.

## Approach

- Dataset: 500,000 users, 12 months, 80M interaction records (browsing, search, cart, purchase) from a major e-commerce platform.
- Feature engineering: 128-dimensional features including behavioral sequences (45D), product attributes (25D), temporal features (12D), user demographics (8D), interaction history (38D).
- Model architecture: bidirectional LSTM with 512 hidden units in each direction, self-attention mechanism (8 heads, 64-dim keys), input embedding (256-dim), dropout (scheduled 0.5→0.3).
- Optimization: Adam optimizer, cosine annealing learning rate (0.001→0.0001), weighted cross-entropy loss with L2 regularization (λ=0.001), gradient clipping (threshold 1.0).
- Training: batch size 128, 100 max epochs with early stopping, data augmentation (temporal jitter, noise injection, sliding window) increasing samples by 200%.

## Findings

1. Proposed LSTM achieved **94.2% accuracy**, 93.8% precision, 94.7% recall, and 94.2% F1-score — a **3.0 percentage point improvement** over standard LSTM and 10.7 percentage points over traditional ML methods (p<0.001).
2. High-frequency users: 96.1% accuracy; high-value customers: 96.7% accuracy.
3. **New users achieved 91.8% accuracy** — a 23.6% improvement over traditional ML models by leveraging short-term behavioral features.
4. Behavioral features dominate prediction (cumulative importance 0.521), with purchase frequency sequence (0.187) and product browsing duration (0.156) as top predictors.
- Self-attention weights show strong recency bias (ratio 1.847) for the most recent 7 days of behavior.

## Key Figures and Tables

- Table 2: Model performance comparison → Proposed LSTM beats logistic regression (78.2%) and standard LSTM (91.2%) across all metrics.
- Figure 3: Training loss curves → Proposed LSTM converges at epoch 25 while traditional methods converge slowly with higher final loss.
- Table 3: Performance by user groups → New users gain most from LSTM (+23.6% accuracy over traditional ML).
- Figure 4: Attention weight visualization → Recent 7-day behaviors receive 1.847× higher weights than earlier days.
- Table 4: Feature importance ranking → Purchase frequency (0.187) and browsing duration (0.156) are most predictive.

## Key Equations

$$\alpha_t = \text{softmax}(e_t)$$
*Attention weight for time step t, where e_t is learned energy score.*

$$L = -\sum_{i} w_i y_i \log(\hat{y}_i) + \lambda \|\theta\|_2^2$$
*Weighted cross-entropy loss plus L2 regularization to prevent overfitting.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LSTM | Long Short-Term Memory — a recurrent neural network with gating mechanisms that remembers information over long sequences. |
| Bidirectional LSTM | Processes sequences both forward and backward, capturing past and future context simultaneously. |
| Self-attention | A mechanism that assigns different importance weights to each time step based on its relevance to the prediction. |
| Dropout schedule | Dropout rate that starts high (0.5) then decreases (to 0.3) during training to balance regularization and fine-tuning. |
| Cosine annealing | Learning rate decays smoothly along a cosine curve from high to low values, improving convergence stability. |

## Critical Citations

- [Liu et al., 2025] — Demonstrates deep learning advantages for complex pattern recognition (YOLO-UNet3D framework), supporting the choice of neural networks over traditional methods.
- [Wang et al., 2022] — Baseline comparison of traditional ML limitations in sequential data, motivating the shift to LSTM architectures.

## Relevance to Odin

**Topics:**

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

**Contribution to Odin:**

This paper directly justifies Odin's selection of LSTM for the spending forecasting module by demonstrating that bidirectional LSTM with attention significantly outperforms both traditional ML and standard LSTM on sequential behavior prediction (3.0 percentage point gain). The finding that behavioral features — especially recency-weighted sequences — dominate prediction (cumulative importance 0.521) validates Odin's focus on transaction history rather than static demographics. The model's strong performance on new users (91.8% accuracy using only short-term patterns) is directly applicable to Odin's cold-start problem for Filipino young professionals with limited spending history.

**Directly justifies:**

- "Bidirectional LSTM with self-attention achieves 94.2% accuracy on 80M consumer interaction records, outperforming standard LSTM by 3.0 percentage points (p<0.001)."
- "Behavioral sequence features (purchase frequency, browsing duration) are 2.7× more predictive than demographic features, supporting transaction-focused forecasting over user-profile-focused models."
- "LSTM with recency-weighted attention (recent 7 days weighted 1.847× higher) captures temporal spending patterns critical for per-category budget forecasting."
- "The model achieves 91.8% accuracy on new users without long history, demonstrating that short-term feature windows suffice for cold-start prediction."

**Limits of relevance:**

- Study domain is e-commerce product purchases, not personal financial spending; transaction patterns (impulse vs. planned) may differ.
- Population is Chinese e-commerce users; Filipino young professionals may exhibit different spending cyclicity and category preferences.
- No evaluation on manual transaction entry (Odin's input method) vs. automated tracking — data sparsity and user friction differ.
- Model requires 128-dimensional feature engineering; Odin's simpler transaction logs may need adaptation.

## Limitations

- Dataset is not publicly available, and demographic composition (age, income) is not disclosed, limiting generalizability to Filipino young professionals.
- No comparison to lightweight models suitable for mobile inference (e.g., reduced LSTM, TCN) — computational cost unknown. [unacknowledged]
- Authors acknowledge remaining failure cases: impulsive purchasing, external event-driven consumption, and early adopter behaviors — these map directly to anomaly detection needs.
- Evaluation uses purchase intention (5 classes) rather than continuous spending amounts; Odin forecasts dollar values, not binary purchase probabilities.
- Gradient clipping and mixed-precision training assume GPU availability; Odin's mobile deployment may require quantization or pruning.

## Remember This

- 🔑 **94.2% accuracy** — bidirectional LSTM + attention beats standard LSTM by 3 points on sequential behavior data.
- 📌 New users hit **91.8% accuracy** using short-term features — cold-start is solvable.
- ⚠️ Behavioral features dominate (52% importance) — spend history > demographics.
- 💡 Recent 7 days weighted 1.85× higher — recency is the strongest signal for prediction.
- 🧠 E-commerce domain, not personal finance — but sequential method transfers directly.