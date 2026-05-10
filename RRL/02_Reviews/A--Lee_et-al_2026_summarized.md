# Comparing deep learning and classical regression approaches for predicting healthcare expenditure and spending: a systematic review

## Metadata

```yaml
---
paper_id: "10.1080/13696998.2026.2630598"
designation: algorithm-specific
title: "Comparing deep learning and classical regression approaches for predicting healthcare expenditure and spending: a systematic review"
authors: "Lee, J. T.; Yeh, M. H.-S.; Li, V. C.-S.; Chen, H.-H.; Liu, Y.-H.; Chen, Y.-C.; Wu, D. B.-C."
year: 2026
venue: "Journal of Medical Economics"
odin_topics: ["D.1", "D.2", "J.1"]
shorthand_tags: ["/forecasting-methods", "/spending-time-series", "/lstm-vs-alternatives", "/lstm-justification", "/eval-frameworks", "/eval-pfms-applied"]
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

Sequential deep learning models (LSTM, CNN-LSTM) reduce prediction error by 10–20% over regression for longitudinal healthcare cost forecasting, but tree-based methods remain competitive for cross-sectional tabular data.

## Problem and Motivation

Healthcare cost prediction models using traditional regression struggle with nonlinear, high-dimensional, or temporally dependent data. Accurate cost forecasts are critical for insurance underwriting, budget planning, and risk adjustment. Prior work lacked systematic comparisons between deep learning architectures and classical methods across different data contexts.

## Approach

- Systematic review of 8 studies meeting inclusion criteria: real-world individual-level health data, deep learning + classical regression comparator, quantitative performance reporting.
- Databases: Web of Science, PubMed, Embase, Scopus through August 2025. PROSPERO-registered (CRD420251129440).
- Study geographies: United States (n=5), Europe (Germany, France; n=2), Asia (China; n=1). Sample sizes: 50,000 to >1.4 million.
- Deep learning architectures: feedforward DNN (n=2), LSTM/stacked LSTM (n=4), CNN-LSTM hybrid (n=1), V-GAN (n=1).
- Comparators: LASSO, ridge, GLM, Random Forest, Gradient Boosting Machine.
- Performance metrics: R²/adjusted R² (n=5), RMSE (n=5), MAE (n=4), AUC (n=2).

## Findings

1. In longitudinal designs (multi-year claims, time-series), LSTM and CNN-LSTM hybrids achieved **10–20% lower RMSE/MAE** than regression and tree-based models.
2. R² improvements from deep learning over classical methods ranged from 0.01 to 0.15 across studies.
3. AUROC for high-cost patient classification reached up to 0.78 using sequential deep models.
4. For cross-sectional tabular data, Random Forest (adj-R² 0.475) outperformed shallow neural networks (adj-R² 0.316) and GLM (adj-R² 0.347).

- Prior costs and utilization were the strongest predictors across all models; social determinants and free-text features were rarely incorporated.
- The authors propose the Complexity–Performance Hypothesis: deep learning advantages emerge when model capacity matches data complexity (longitudinal, multimodal).

## Key Figures and Tables

- Figure 2: Model performance by data complexity → Deep learning excels in longitudinal/multimodal regimes; tree-based leads in cross-sectional tabular settings.
- Table 1: Characteristics of included studies → Eight studies span US, Europe, Asia; sample sizes up to 1.4M.
- Table 2: Comparative model performance → LSTM reduces RMSE by ~19% over ARIMA; CNN-LSTM achieves R² ~0.8–0.9.
- Table 3: Neural network architectures by data type → Recurrent models for time-dependent data; feedforward for static features.
- Table 4: Challenges and strategies for deep learning in cost prediction → Lists limited interpretability, short horizons, data diversity.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LSTM | Long Short-Term Memory [think: memory cell that learns what to forget] — recurrent neural network for sequence prediction. |
| CNN | Convolutional Neural Network — extracts local patterns from spatial or sequential data. |
| RMSE | Root Mean Square Error — measures average prediction error with heavier penalty for large mistakes. |
| MAE | Mean Absolute Error — average absolute prediction error. |
| R² | Coefficient of determination — proportion of variance explained by the model. |
| AUROC | Area Under Receiver Operating Characteristic curve — discrimination ability for binary classification. |
| GLM | Generalized Linear Model — regression family for non-normal outcomes. |
| GBM | Gradient Boosting Machine — ensemble method building trees sequentially. |

## Critical Citations

- [LeCun et al., 2015] — Foundational deep learning review establishing neural network capacity and representation learning.
- [Esteva et al., 2019] — Comprehensive guide to deep learning applications in healthcare, cited as motivation.
- [Drewe-Boss et al., 2022] — Key included study demonstrating DNN outperforms ridge regression for German health costs.

## Relevance to Odin

**Topics:**

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

J.1 — System Evaluation

**Contribution to Odin:**

This systematic review directly informs Odin's choice of LSTM for the spending forecasting module by providing empirical evidence that sequential deep learning models outperform regression and tree-based methods on longitudinal expenditure data. The finding that prior spending is the strongest predictor aligns with Odin's design to use historical transaction sequences as the primary input. The paper's Complexity–Performance Hypothesis justifies Odin's algorithm selection: because Odin forecasts per-category spending from multi-month transaction sequences (longitudinal, time-dependent data), LSTM is the appropriate high-capacity model. Additionally, the review's evaluation framework (RMSE, MAE, R²) provides a benchmark for Odin's own model validation.

**Directly justifies:**

- "Sequential deep learning models, particularly LSTM and CNN–LSTM hybrids, consistently outperform regression and tree-based algorithms on longitudinal healthcare cost prediction, achieving 10–20% reductions in RMSE/MAE."
- "Prior costs and utilization are consistently the strongest predictors of future spending — historical transaction sequences should be the primary input for personal finance forecasting models."
- "Shallow feed-forward neural networks perform similarly to or worse than classical regressions on cross-sectional tabular data, warning against using simple DNNs without sequential structure for spending prediction."
- "Tree-based methods (Random Forest, GBM) remain highly competitive for cross-sectional prediction but are outperformed by LSTM on temporally rich data — Odin's forecasting module should prioritise LSTM over ensemble methods."

**Limits of relevance:**

- Healthcare expenditure data differs from personal consumption spending (e.g., food, transport) in distribution, volatility, and behavioral drivers.
- All eight studies use claims or electronic health records from high-income countries (US, Germany, France, China); Filipino young professional spending patterns may differ.
- The review does not evaluate cold-start performance (new users with no history), which is critical for Odin.
- Prediction horizons in reviewed studies (1 year) are longer than Odin's typical monthly forecasting window.

## Limitations

- Only eight studies met inclusion criteria; high heterogeneity prevents quantitative meta-analysis. [unacknowledged]
- No external validation across independent datasets or time periods in most included studies.
- Short prediction horizons (predominantly one-year) limit generalizability to longer-term forecasting. [unacknowledged]
- Social determinants and behavioral predictors were rarely incorporated — Odin's user profiling may need to address this gap.
- The Complexity–Performance Hypothesis is inductively derived from a small evidence base and requires further validation.

## Remember This

- 🔑 **10–20% lower RMSE** — LSTM beats regression/GBM on longitudinal spending sequences.
- 📌 Prior spending is the strongest predictor — Odin's LSTM should rely on historical transactions.
- 💡 For cross-sectional tabular data, Random Forest often beats shallow neural nets (adj-R² 0.475 vs 0.316).
- ⚠️ No cold-start evaluation in any reviewed study — unknown how LSTM performs for new Odin users with zero history.
- ✅ R² gains of 0.01–0.15 and AUROC up to 0.78 — deep learning improves high-cost detection.
