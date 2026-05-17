# A Survey of Machine Learning Methods for Time Series Prediction

## Metadata

```yaml
---
paper_id: "10.3390/app15115957"
designation: international
title: "A Survey of Machine Learning Methods for Time Series Prediction"
authors: "Hall, T.; Rasheed, K."
year: 2025
venue: "Applied Sciences"
odin_topics: ["6.A", "6.B", "12.B"]
shorthand_tags: ["/forecasting-methods-survey", "/forecast-algo-candidates", "/forecast-algo-comparison", "/forecast-algo-tradeoffs", "/forecast-eval-metrics"]
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

Tree-based models (LightGBM, XGBoost) match or beat deep learning (LSTM) for time series forecasting across most tasks, while training 100–1,000× faster.

## Problem and Motivation

Existing time series prediction surveys analyze independent studies that use different datasets and implementations, making direct model comparisons impossible. This prevents researchers from knowing whether performance differences come from the model or the experimental setup. No prior survey systematically compared tree-based and deep learning methods under identical conditions across multiple task types and dataset sizes.

## Approach

- Surveyed 79 papers (2017–2024) from Web of Science that compare at least one tree-based ML (TBML) and one deep learning (DL) method on the same dataset.
- Defined two metrics: First Place Aggregation (FPA = Nfirst/Ntotal × 100) and Weighted Rank Aggregation (WRA = 1 − (Nrank−1)/(Ntotal−1)).
- Grouped models into TBML (Random Forest, GBDT, XGBoost, LightGBM, CatBoost) and DL (FFNN, CNN, RNN/LSTM/GRU, Transformers).
- Analyzed performance by task category (10 groups), dataset size (5 ranges from <2k to >11M samples), and data time interval.
- Measured training time advantage across 10 studies that reported explicit comparisons.
- Reviewed hyperparameter optimization techniques (Grid Search, Bayesian Optimization, OPTUNA) and hybrid model configurations.
- Synthesized results from M5 (retail sales, 42,840 time series) and M6 (stock/ETF, 12-month) forecasting competitions.

## Findings

1. TBML models as a class achieved best performance in 54.55% of tasks vs. 52.70% for DL (FPA), with WRA scores 0.691 vs. 0.649 — a ~2.5% edge for TBML.
2. Among individual models, **LSTM had the strongest robust evidence: 58.97% FPA** (39 evaluations) and WRA 0.722.
3. LightGBM achieved 58.82% FPA (17 evaluations); CatBoost had 66.67% FPA but only 3 evaluations.

- TBML models train on average 126,935% faster than DL models (median 5,603% faster).
- In the largest dataset range (206k–11M samples), specialized TBML (SPTB) models outperformed RNNs by 16.67% FPA.
- Research focus bias: DL-focused papers show DL +33.8% FPA over TBML; TBML-focused show TBML +66.7% FPA over DL.
- Hybrid models generally outperform individuals, but standalone CatBoost beat a hybrid CNN-BiLSTM in one study (Saravanan et al., 2024).

## Key Figures and Tables

- Figure 3: FPA/WRA by class (TBML vs. DL) → TBML edges DL by ~2.5% average across all tasks.
- Figure 4: Subclass performance → RNNs highest FPA (61.4%), SPTB second (50%).
- Figure 10: Dataset size impact → SPTB dominates at largest scale (16.7% FPA advantage over RNN).
- Table 2: Training time advantage → TBML up to 905,140% faster (median 5,603%) across 10 studies.
- Table 3: Summary best models by data characteristic → SPTB for large datasets, RNN for small/medium.

## Key Equations

$$FPA = \frac{N_{\text{first}}}{N_{\text{total}}} \times 100$$
*Frequency a model ranks first; higher means more dominant.*

$$WRA = 1 - \frac{(N_{\text{rank}} - 1)}{(N_{\text{total}} - 1)}$$
*Rank-based score where 1 = top performer, 0 = worst, adjusting for comparison size.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| TBML | Tree-Based Machine Learning — ensemble methods using decision trees (Random Forest, GBDT). |
| DL | Deep Learning — neural networks with multiple hidden layers. |
| SPTB | Specialized Tree-Based models — gradient-boosted implementations (XGBoost, LightGBM, CatBoost). |
| RNN | Recurrent Neural Network — neural net with memory of previous inputs; LSTM and GRU are variants. |
| LSTM | Long Short-Term Memory [think: forget gate keeps long patterns, input gate captures new events] |
| GRU | Gated Recurrent Unit — simplified LSTM with fewer gates, faster training. |
| FFNN | Feed-Forward Neural Network — information flows only forward; no memory of past inputs. |
| CNN | Convolutional Neural Network — detects local patterns; good for image or spatial time series. |
| GBDT | Gradient Boosted Decision Tree — builds trees sequentially, each correcting previous errors. |
| FPA | First Place Aggregation — percentage of comparisons where a model finishes first or tied-first. |
| WRA | Weighted Rank Aggregation — continuous score from 0 (worst) to 1 (best) across all comparisons. |

## Critical Citations

- [Chen & Guestrin, 2016] — XGBoost's scalable tree boosting system; foundational to all SPTB comparisons.
- [Ke et al., 2017] — LightGBM's histogram-based binning and leaf-wise growth; basis for speed advantage claims.
- [Prokhorenkova et al., 2018] — CatBoost's symmetric trees and target encoding; cited for categorical feature handling.
- [Sherstinsky, 2020] — LSTM fundamentals; cited to explain gating mechanisms for long-term dependencies.
- [Makridakis et al., 2022] — M5 competition results; provides real-world evidence of LightGBM dominance in retail forecasting.

## Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This survey directly informs Odin's spending forecasting module by providing empirical benchmarks for algorithm selection across dataset sizes and task types. The finding that LightGBM trains 5,600% faster than LSTM with comparable accuracy supports Odin's mobile-first constraint: efficient retraining on user devices without cloud dependencies. The identified research bias (up to 66.7% performance inflation when papers favor one model class) warns Odin's RRL to prioritize balanced studies when citing comparative claims. Additionally, the M5 competition result—an undergraduate won using LightGBM ensembles—demonstrates the model's accessibility for implementation without deep learning expertise.

**Directly justifies:**

- "LSTM achieved 58.97% first-place frequency across 39 time series forecasting comparisons, the strongest robust evidence among all individual models surveyed."
- "LightGBM trains a median 5,603% faster than deep learning models (up to 905,140% faster in one study) while achieving equivalent or better accuracy on tasks with large datasets."
- "On datasets larger than 200,000 samples, specialized tree-based models (XGBoost, LightGBM, CatBoost) outperform RNNs by 16.67% in first-place frequency."
- "Research focus biases reported model performance: DL-focused papers show DL outperforming TBML by 33.8% FPA, while TBML-focused papers show TBML outperforming DL by 66.7% FPA."
- "Tree-based models dominate energy, transportation, and anomaly detection tasks; RNNs dominate environmental, healthcare, and financial forecasting."

**Limits of relevance:**

- Survey includes no Philippine-specific financial data; domain patterns from retail, energy, or environmental forecasting may not map directly to personal spending behavior.
- Computational advantage measured on server-class hardware (GPUs/CPUs), not on mobile device constraints (battery, thermal throttling).
- M5 competition used retail sales (Walmart unit sales) with 42,840 time series; individual user spending has sparser, more irregular patterns.
- The survey excludes cold-start forecasting evaluation (no prior user data), a critical scenario for new Odin users.
- Attention-based models (Transformers) have only 5 papers in the survey; conclusions about their performance are not statistically robust.

## Limitations

- Attention-based architectures (Transformers) evaluated in only 5 papers; conclusions about their performance lack statistical robustness.
- Training time analysis drawn from only 10 studies; median advantage (5,603%) may not generalize across all hardware configurations. [unacknowledged]
- Survey excludes comparison of feature engineering effort required for TBML vs. DL; TBML often needs manual sequential feature construction. [unacknowledged]
- The weighted rank aggregation assumes linear interpolation between ranks, which may not reflect real performance gaps between models.
- M6 competition found zero correlation between forecasting accuracy and investment performance, but the survey does not explore why—this limits relevance for recommendation modules that combine forecasting with action.

## Remember This

- 🔑 **LSTM: 59% first-place rate** — strongest robust performer across 39 studies.
- 💡 LightGBM trains **5,600× faster** than DL with comparable accuracy — ideal for mobile retraining.
- 📌 On large datasets (>200k samples), tree-based models beat RNNs by **16.7%** .
- ⚠️ Research bias inflates reported performance by up to 67% — cite only balanced studies.
- 🧠 M5 winner (undergraduate) used LightGBM ensembles — low expertise barrier to high accuracy.
