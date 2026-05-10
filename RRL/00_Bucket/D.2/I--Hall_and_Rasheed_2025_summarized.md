```markdown
# MACHINE LEARNING TIME SERIES FORECASTING: A COMPREHENSIVE SURVEY AND STOCK MARKET APPLICATION

## Metadata

```yaml
---
paper_id: "f5c8a4e2-9b3d-4a7c-8e1f-6d2b5a9e7c3a"
designation: algorithm-specific
title: "MACHINE LEARNING TIME SERIES FORECASTING: A COMPREHENSIVE SURVEY AND STOCK MARKET APPLICATION"
authors: "Hall, T."
year: 2025
venue: "University of Georgia"
odin_topics: ["D.1", "D.2"]
shorthand_tags: ["/forecasting-methods", "/lstm-justification", "/lstm-vs-alternatives"]
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

Tree‑based models (LightGBM) and RNNs (LSTM) outperform other time‑series forecasting methods, with LightGBM delivering massive computational efficiency gains over deep learning.

## Problem and Motivation

Existing surveys cannot directly compare time‑series models because they analyze independent studies with different datasets and implementations, preventing reliable conclusions about relative performance. This gap is critical for practitioners who need to select the best forecasting method for their domain. No prior work systematically compared tree‑based and deep learning methods under identical experimental conditions across diverse time‑series tasks.

## Approach

- Survey of 79 papers (2017‑2024) that compare at least one tree‑based (TBML) and one deep learning (DL) model on identical datasets.
- Model classes: TBML (RF, GBDT, XGBoost, LightGBM, CatBoost) vs DL (FFNN, CNN, RNN, LSTM, GRU, Transformer).
- Evaluation metrics: First Place Aggregation (FPA = % of comparisons where model ranks best) and Weighted Rank Aggregation (WRA = scaled score from 1 for best to 0 for worst).
- Analyzed performance across dataset size, time interval, research focus, training time, and 46 unique task categories.
- Reviewed M5 and M6 forecasting competitions for additional validation.

## Findings

1. TBML models marginally outperform DL overall (FPA 54.55% vs 52.70%; WRA 0.691 vs 0.649).
2. RNN models (LSTM/GRU) rank best in **61.36%** of comparisons (WRA 0.733); specialized TBML (XGBoost/LightGBM/CatBoost) rank best in 50% (WRA 0.633).
3. **TBML models train 126,385% faster on average (median 5,603%)** than DL models.
4. Dataset size >200k samples favors TBML; smaller datasets favor DL.
- Research focus biases results: DL‑focused papers show DL outperforming TBML by 33.8% FPA; TBML‑focused papers show TBML outperforming by 66.7% FPA.
- LightGBM dominated the M5 competition (top 50 submissions all used it).

## Key Figures and Tables

- Figure 2.3: Overall FPA/WRA scores → TBML edge ≈2.5% over DL.
- Figure 2.4: Subclass performance → RNNs highest FPA (61.4%), SPTB second (50%).
- Table 2.1: 46 unique time‑series tasks grouped into 10 categories.
- Figures 2.10‑2.11: Dataset size impact → TBML dominates largest datasets (>200k samples).
- Figures 2.14‑2.15: Research focus bias → papers favor their own model class.

## Key Equations

$$FPA = \frac{N_{\text{first}}}{N_{\text{total}}} \times 100$$
*Frequency a model is top‑ranked across comparisons.*

$$WRA = 1 - \frac{N_{\text{rank}} - 1}{N_{\text{total}} - 1}$$
*Weighted rank score: 1 for best, 0 for worst.*

$$RR_t = \frac{\sum w_i \cdot \text{MaxUpswing}_i}{\sum w_i \cdot \text{MaxDrawdown}_i}$$
*Risk‑reward ratio for day trading entry decisions.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LSTM | Long Short‑Term Memory; RNN variant with gating to remember long patterns [think: memory cell with forget/input/output gates]. |
| RNN | Recurrent Neural Network; processes sequences via internal memory state. |
| TBML | Tree‑Based Machine Learning; ensemble methods using decision trees. |
| DL | Deep Learning; neural networks with multiple hidden layers. |
| LightGBM | Gradient boosting framework using histogram binning for speed. |
| XGBoost | Extreme Gradient Boosting; popular tree‑based model with regularization. |
| CatBoost | Gradient boosting optimized for categorical features. |
| FPA | First Place Aggregation; % of comparisons where a model is top‑ranked. |
| WRA | Weighted Rank Aggregation; normalized score from 1 (best) to 0 (worst). |

## Critical Citations

- [Chen & Guestrin, 2016] — XGBoost foundation; most frequently compared model in the survey.
- [Ke et al., 2017] — LightGBM; dominant model in M5 competition and fastest TBML.
- [Makridakis et al., 2022] — M5 results confirming LightGBM superiority on retail sales.
- [Barber et al., 2014] — Benchmark of elite human day traders: 28.1 basis points/day net profit.

## Relevance to Odin

**Topics:**

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

**Contribution to Odin:**

This paper directly justifies Odin’s selection of LSTM for spending forecasting by demonstrating that RNNs (including LSTM) perform best across 61.36% of time‑series tasks, including financial data. The finding that LightGBM trains 126,385% faster than DL models while achieving competitive accuracy informs Odin’s computational trade‑offs for mobile deployment — if real‑time retraining is needed, a tree‑based fallback may be preferable. The survey’s conclusion that data quality and feature engineering outweigh algorithm choice reinforces Odin’s core design: investing in FIES‑grounded expense categorization and behavioral features will likely yield greater forecasting gains than chasing more complex models.

**Directly justifies:**

- “RNN architectures (LSTM/GRU) are the best‑performing models for time‑series forecasting, ranking first in 61.36% of comparative studies across 46 tasks.”
- “LightGBM trains 126,385% faster than deep learning models on average (median 5,603%), making it suitable for resource‑constrained mobile environments.”
- “Research focus introduces strong bias: papers favoring a model class show that class outperforming by 33–67% FPA, so Odin’s literature review must prioritize balanced comparative studies.”
- “For datasets larger than 200,000 samples, tree‑based models (including LightGBM) outperform deep learning models — relevant if Odin scales to many users.”

**Limits of relevance:**

- Survey includes no Filipino‑specific financial data; spending pattern seasonality or income volatility may differ from benchmark datasets.
- Stock market application uses second‑by‑second trade data, not personal transaction data (weekly/monthly) — the temporal granularity gap limits direct method transfer.
- Computational advantage of LightGBM assumes batch offline training, not real‑time mobile inference; mobile‑specific benchmarks are absent.
- Human trader benchmark (Barber et al.) from Taiwan, not Philippines; cultural and market structure differences may affect relevance.

## Limitations

- Survey excludes papers that do not compare both TBML and DL, potentially missing novel architectures like pure Transformer forecasts. [unacknowledged]
- FPA/WRA metrics treat all tasks equally, ignoring differences in difficulty, dataset size, or evaluation rigor.
- Stock market day‑trading model assumes commission‑free execution and ignores slippage; never tested with real money.
- No validation of model performance on Philippine stock market or personal finance transaction data.
- Training time comparison based on only 10 papers; hardware differences may affect absolute speed figures.

## Remember This

- 🔑 **LSTM wins 61% of comparisons** — strongest sequential model for spending forecasting.
- ⚡ LightGBM trains **126,385% faster** — massive compute advantage over deep learning.
- 📊 Dataset size >200k flips advantage to TBML — Odin’s early data may favor DL initially.
- 🧠 Feature engineering beats algorithm choice — data quality is king, not model complexity.
- ⚠️ Research focus biases results — always check if a paper fairly compares both sides.
```