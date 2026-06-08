# A Survey of Machine Learning Methods for Time Series Prediction

## Metadata

```yaml
---
paper_id: "10.3390/app15115957"
designation: algorithm-specific
title: "A Survey of Machine Learning Methods for Time Series Prediction"
authors: "Hall, T.; Rasheed, K."
year: 2025
venue: "Applied Sciences"
odin_topics: ["D.1", "D.2"]
shorthand_tags: ["/forecasting-methods", "/spending-time-series", "/temporal-dependency", "/lstm-vs-alternatives", "/lstm-spending-applied", "/lstm-justification", "/lstm-mobile"]
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

LSTM and LightGBM achieve the highest forecast accuracy across time series tasks, but LightGBM trains 100–1,000× faster, making it the practical default for most applications.

## Problem and Motivation

Existing survey papers cannot draw meaningful comparisons between tree-based and deep learning models because they analyze independent studies using different datasets and implementations. Without controlled comparisons, researchers lack reliable guidance on which model class performs best for a given time series task. No prior survey had restricted inclusion to studies that directly compare both methodologies under identical experimental conditions.

## Approach

- Web of Science search (2017–2024) using terms for XGBoost, LightGBM, CatBoost, and deep learning (LSTM, GRU, CNN, Transformer) yielded 589 papers.
- Inclusion criteria: study must compare at least one tree-based method (XGBoost/LightGBM/CatBoost/RF/GBDT) and one deep learning method (RNN/LSTM/GRU/CNN/Transformer) on the **same dataset**.
- Final set: 79 papers meeting criteria, plus top-cited 2023–2024 papers.
- Two evaluation metrics: First Place Aggregation (FPA = % of studies where model ranked first) and Weighted Rank Aggregation (WRA = normalized rank score from 0 to 1).
- Analyzed performance by task category, dataset size (5 ranges, 0 to >200k samples), time interval, research focus bias, and training time.
- Reviewed results from M5 (retail sales, 42,840 time series) and M6 (stock/ETF) forecasting competitions.

## Findings

1. **LSTM achieved best performance in 58.97% of its evaluations (39 studies), while LightGBM achieved 58.82% (17 studies).** CatBoost scored 66.67% but only 3 evaluations.
2. TBML models **train 126,935% faster on average** (median 5,603%) than deep learning models; inference time: XGBoost 0.001s vs. LSTM 0.311s.
3. On largest datasets (>206k samples), specialized tree-based models (XGBoost/LightGBM/CatBoost) outperform RNNs by **16.67% in FPA** and 0.383 in WRA.
4. On smallest datasets (0–2,173 samples), RNNs outperform specialized tree-based models by **50% in FPA**.
5. Research focus bias: DL-focused papers show DL models 33.8% higher FPA; TBML-focused papers show TBML 66.7% higher FPA. Balanced papers show TBML with a slight edge (15.2% higher FPA).

- M5 competition: LightGBM dominated top 50 submissions; first place used 220 LightGBM models.
- M6 competition: No single best method; data quality and feature engineering mattered more than algorithm choice.

## Key Figures and Tables

- Figure 3: TBML vs. DL class comparison → TBML edges DL by ~2.5% in FPA (54.55% vs. 52.70%).
- Figure 4: Subclass FPA and WRA → RNNs lead at 61.36% FPA; specialized tree-based (SPTB) at 50%.
- Figure 5: Individual model FPA → CatBoost (66.67%, n=3), LSTM (58.97%, n=39), LightGBM (58.82%, n=17).
- Table 3: Best model by dataset size → small: RNN; large: SPTB.

## Key Equations

$$FPA = \frac{N_{first}}{N_{total}} \times 100$$
*Percentage of evaluations where a model ranks first.*

$$WRA = 1 - \frac{(N_{rank} - 1)}{(N_{total} - 1)}$$
*Normalized rank score: 1 = best, 0 = worst in each comparison.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| TBML | Tree-Based Machine Learning — ensemble methods using decision trees (RF, XGBoost, LightGBM, CatBoost). |
| DL | Deep Learning — neural networks with multiple layers (RNN, LSTM, CNN, Transformer). |
| SPTB | Specialized Tree-Based models — the three gradient-boosted tree implementations: XGBoost, LightGBM, CatBoost. |
| LSTM [think: memory cell with forget/input/output gates] | Long Short-Term Memory — RNN variant that remembers patterns over long sequences. |
| GRU | Gated Recurrent Unit — simpler LSTM alternative with two gates (update, reset), faster to train. |
| RNN | Recurrent Neural Network — network with feedback loops that maintain an internal memory state. |
| FPA | First Place Aggregation — metric counting how often a model achieves top rank. |
| WRA | Weighted Rank Aggregation — metric scoring models by their relative rank in each comparison. |
| XGBoost | eXtreme Gradient Boosting — optimized GBDT with regularization and pruning. |
| LightGBM | Light Gradient Boosting Machine — histogram-based GBDT with leaf-wise growth, very fast. |
| CatBoost | Categorical Boosting — GBDT designed for datasets with many categorical features. |

## Critical Citations

- [Chen & Guestrin, 2016] — Original XGBoost paper; foundational for the most-cited TBML implementation.
- [Ke et al., 2017] — LightGBM architecture; dominates M5 competition and large-dataset performance.
- [Prokhorenkova et al., 2018] — CatBoost method; best FPA but limited representation in surveyed studies.
- [Sherstinsky, 2020] — Comprehensive LSTM fundamentals; explains why RNNs excel on sequential data.

## Relevance to Odin

**Topics:**

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

**Contribution to Odin:**

This survey directly informs Odin’s algorithm selection for the spending forecasting module by providing comparative evidence across 79 studies. It shows LSTM as the top-performing deep learning model (58.97% FPA) but also reveals that LightGBM matches LSTM on accuracy while being orders of magnitude faster to train and infer — a critical consideration for Odin as a mobile-first system with computational constraints. The finding that dataset size determines optimal model choice (RNNs better on small data, TBML better on large data) justifies Odin’s need to re-evaluate algorithm choice as user transaction history grows. Additionally, the documented research bias (papers favoring their own model class) warns Odin’s team to prioritize balanced, direct comparisons when reviewing literature.

**Directly justifies:**

- "LSTM achieves the highest forecast accuracy among deep learning models for time series prediction, ranking first in 58.97% of evaluations across 39 comparative studies (Hall & Rasheed, 2025)."
- "LightGBM matches or exceeds LSTM accuracy on large datasets (>200k samples) while training 100–1,000× faster, making it the computationally efficient default for time series forecasting."
- "On small datasets (0–2,173 samples), RNNs like LSTM outperform gradient-boosted trees by 50 percentage points in first-place frequency, supporting LSTM for cold-start user profiles with limited transaction history."
- "Research focus introduces substantial bias: papers emphasizing deep learning show DL models 33.8% higher first-place rates than TBML models in the same comparisons."

**Limits of relevance:**

- Survey covers diverse domains (energy, environment, finance) but not specifically personal budgeting; spending patterns may have different temporal characteristics than retail or stock data.
- All studies use non-Filipino datasets; spending volatility and cultural patterns may differ.
- Computational efficiency claims assume server-grade hardware; mobile inference times may scale differently.
- M5/M6 competitions used retail and financial data with exogenous variables not available in manual entry systems like Odin.

## Limitations

- Survey only includes papers that explicitly compare TBML and DL on identical datasets — may miss domain-specific findings from single-model studies.
- CatBoost results based on only 3 studies; statistical robustness is low. [unacknowledged]
- Transformer and attention-based architectures have only 5 studies; their reported strong performance requires replication.
- Training time comparisons available in only 10 of 79 papers — median advantage may be overestimated.
- No analysis of model performance on irregularly sampled time series or missing data — common in manual expense tracking.

## Remember This

- 🔑 **LSTM first in 58.97% of comparisons** — strongest deep learning model for time series forecasting.
- 💡 LightGBM matches LSTM accuracy but trains **5,600× faster (median)** — default choice for large datasets and mobile constraints.
- 📌 Small datasets (<2,173 samples): RNNs beat tree-based models by **50%** in first-place rate — justifies LSTM for cold-start profiles.
- ⚠️ Research focus bias is real — papers advocating a method see it perform **33–66% better** than balanced papers show.
- 🧠 M5 competition: top 50 entries all used LightGBM ensembles — real-world validation of TBML dominance in retail forecasting.
