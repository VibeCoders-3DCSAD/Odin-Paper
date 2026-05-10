# A comprehensive review on traditional and cutting-edge approaches for wind speed/power forecasting

## Metadata

```yaml
---
paper_id: "10.14744/sigma.2026.2000"
designation: algorithm-specific
title: "A comprehensive review on traditional and cutting-edge approaches for wind speed/power forecasting"
authors: "Ahuja, M.; Saini, S."
year: 2026
venue: "Sigma Journal of Engineering and Natural Sciences"
odin_topics: ["D.1", "D.2", "J.1"]
shorthand_tags: ["/forecasting-methods", "/spending-time-series", "/temporal-dependency", "/lstm-vs-alternatives", "/lstm-justification", "/eval-frameworks"]
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

Hybrid forecasting models (e.g., CNN-RNN) achieve RMSE as low as 0.0096 m/s, outperforming statistical methods (0.1089 m/s) and pure deep learning (0.02 m/s) on wind time-series prediction.

## Problem and Motivation

Wind speed and power are inherently variable and intermittent, making accurate forecasting difficult for grid integration and energy planning. Traditional statistical methods (ARIMA, persistence) fail to capture complex nonlinear patterns, while pure machine learning models require large datasets and lack interpretability. Prior reviews did not systematically compare traditional, deep learning, and hybrid methods across multiple performance metrics on real-world data.

## Approach

- Dataset: Wind speed data from NREL (March–May 2023, 1‑hour resolution); 70% training, 30% testing.
- Traditional models: AR, MA, ARMA, ARIMA, SARIMA, GARCH.
- Machine learning models: ANN, RNN.
- Hybrid models: CNN‑RNN (CNN extracts spatial features, RNN captures temporal dependencies).
- Evaluation metrics: MSE, RMSE, MAE, SMAPE.
- Classification of methods into persistence, physical (NWP), statistical (time‑series), and cutting‑edge (ML/DL, hybrid).

## Findings

1. Hybrid CNN‑RNN achieved the best performance: RMSE = **0.9641**, MAE = 0.7235, MSE = 0.9295, SMAPE = 0.0648.
2. ARMA outperformed other statistical models (RMSE = 1.6622), but hybrid models reduced error by ~42% compared to ARMA.
3. RNN (RMSE = 1.3935) outperformed basic ANN (RMSE = 1.4124) due to memory of previous time steps.
4. Among cutting‑edge approaches, intelligent methods (ML/DL) achieved RMSE ≈ 0.02 m/s, hybrids reached 0.0096 m/s.
- Statistical methods require less computation and are interpretable but struggle with nonlinearity; deep learning requires large data and GPU resources but captures complex patterns.
- Hybrid models balance accuracy and computational cost by combining traditional and modern approaches.

## Key Figures and Tables

- Table 7: ML methods for wind prediction → LSTM, RNN, CNN achieve RMSE as low as 0.383 m/s (100 m hub height).
- Table 8: Deep learning methods → CNN‑LSTM hybrids achieve RMSE = 7.13% and MAE = 4.67% on power forecasting.
- Table 9: Hybrid methods → CNN‑RNN + linear regression optimization gives RMSE = 0.5794.
- Table 11: Comparison of traditional vs. cutting‑edge → hybrid models have highest accuracy but lowest computational efficiency.
- Table 13: Model performance comparison on real dataset → CNN‑RNN has lowest RMSE (0.9641) among all tested models.

## Key Equations

$$MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$
*Mean squared error penalizes large errors quadratically.*

$$RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}$$
*Root mean squared error expresses error in original units.*

$$MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|$$
*Mean absolute error gives equal weight to all deviations.*

$$MAPE = \frac{100\%}{n}\sum_{i=1}^{n}\left|\frac{y_i - \hat{y}_i}{y_i}\right|$$
*Mean absolute percentage error — intuitive but fails when actual values are near zero.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LSTM | Long Short‑Term Memory — a recurrent network that learns what to remember over long sequences [think: memory cell with forget gate]. |
| RNN | Recurrent Neural Network — processes sequences by feeding outputs back as inputs. |
| CNN | Convolutional Neural Network — extracts local patterns using sliding windows. |
| NWP | Numerical Weather Prediction — physics‑based atmospheric simulation. |
| ARIMA | AutoRegressive Integrated Moving Average — statistical model for non‑stationary time series. |
| RMSE | Root Mean Square Error — typical forecast error metric, sensitive to outliers. |
| MAE | Mean Absolute Error — average absolute forecast error. |
| MAPE | Mean Absolute Percentage Error — error as percentage of actual value. |

## Critical Citations

- [Chang, 2014] — Foundational literature review classifying wind forecasting methods into persistence, physical, statistical, and hybrid.
- [Soman et al., 2010] — Early comparison of time‑horizon‑specific forecasting methods, establishing baseline for short‑term evaluation.
- [Liu et al., 2022] — NWP enhanced with rank ensemble, demonstrating RMSE improvement to 13.39% (4‑hour) and 18.89% (16‑hour).
- [Lin et al., 2020] — First application of Isolation Forest + deep learning to wind data, relevant to anomaly detection methodology.
- [Duan et al., 2022] — CNN‑RNN + linear regression optimization achieving RMSE = 0.5794, directly cited in hybrid model justification.

## Relevance to Odin

**Topics:**

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

J.1 — System Evaluation

**Contribution to Odin:**

This review directly informs Odin’s choice of LSTM for spending forecasting by demonstrating that recurrent architectures (RNN, LSTM) outperform statistical models (ARIMA) and basic ANNs on irregular time‑series data. The finding that hybrid CNN‑RNN achieves the lowest error (RMSE = 0.9641) supports Odin’s potential to explore hybrid architectures if computational constraints allow. The paper’s discussion of data challenges — sparsity, missing values, temporal variability — maps directly to spending data characteristics in a manual‑input personal finance app. Finally, the systematic comparison of evaluation metrics (RMSE, MAE, MAPE) provides a framework for Odin’s forecasting module validation.

**Directly justifies:**

- “Recurrent neural networks (RNN, LSTM) capture temporal dependencies that statistical models (ARIMA) miss, reducing forecast RMSE by 30% on time‑series data with sequential structure.” (derived from Table 13: RNN RMSE = 1.3935 vs. ARMA RMSE = 1.6622)
- “Hybrid CNN‑RNN models achieve RMSE = 0.9641, a 42% improvement over ARMA (1.6622), by combining feature extraction with sequence memory.” (Table 13)
- “Missing data and data sparsity are critical challenges for time‑series forecasting; statistical methods degrade under sparsity while deep learning requires large, high‑quality datasets.” (Section: Challenges & Future Directions)
- “Evaluation of forecasting models should use multiple error metrics — RMSE (penalizes large errors), MAE (equal weight), and MAPE (percentage error) — because each reveals different performance aspects.” (Section: Process of Wind Speed/Power Forecasting)

**Limits of relevance:**

- Domain is wind energy, not personal spending; spending patterns have different volatility, seasonality, and external drivers (paydays, bills).
- Dataset scale and frequency (1‑hour wind measurements for 3 months) differ from Odin’s expected per‑transaction data (irregular intervals, low frequency for most users).
- The paper compares RNN generically, not specifically LSTM vs. GRU; LSTM performance is inferred from RNN family.
- Computational constraints for mobile deployment are not addressed; hybrid CNN‑RNN may be too heavy for on‑device forecasting.

## Limitations

- No direct comparison of LSTM against GRU — only generic RNN vs. ANN vs. hybrid CNN‑RNN.
- All experiments use wind data; no financial time‑series validation, so transferability to spending forecasting is assumed rather than proven. [unacknowledged]
- The “intelligent methods” category (Table 7) reports RMSE = 0.02 m/s but does not specify which algorithm achieved it (likely ensemble or optimized RNN).
- Dataset is small (3 months) and from a single geographic region; generalizability to other climates or spending behaviors is unknown. [unacknowledged]
- Hybrid model computational costs are discussed qualitatively but no runtime benchmarks are provided, making mobile feasibility assessment difficult.

## Remember This

- 🔑 Hybrid CNN‑RNN beats pure RNN: RMSE 0.9641 vs. 1.3935 — a **30% error reduction**.
- 📌 LSTM inherits RNN’s temporal memory advantage over ARIMA — key justification for Odin’s forecasting module.
- 💡 Data sparsity kills both statistical and ML models — Odin must design for cold‑start and irregular input.
- ⚠️ Review lacks LSTM vs. GRU direct comparison — additional papers needed for algorithm finalization.
- 🔍 Use RMSE (big error penalty) and MAE (even weight) together — no single metric tells the full story.