# Selected Topics in Time Series Forecasting: Statistical Models vs. Machine Learning

## Metadata

```yaml
---
paper_id: "10.3390/e27030279"
designation: international
title: "Selected Topics in Time Series Forecasting: Statistical Models vs. Machine Learning"
authors: "Tjøstheim, D."
year: 2025
venue: "Entropy"
odin_topics: ["D.1", "D.2", "J.1"]
shorthand_tags: ["/forecasting-methods", "/spending-time-series", "/temporal-dependency", "/lstm-architecture", "/lstm-vs-alternatives", "/lstm-spending-applied", "/lstm-justification", "/eval-frameworks", "/eval-pfms-applied"]
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

Machine learning methods outperform statistical models on high-entropy and intermittent time series (M5 competition), but hybrid statistical‑ML approaches achieve the best overall forecasting accuracy.

## Problem and Motivation

Practitioners lack systematic guidance on when statistical versus machine learning forecasting methods perform best across different data characteristics (entropy, intermittency, sampling frequency). This uncertainty leads to suboptimal model selection in real‑world applications ranging from retail demand to financial volatility. Prior forecasting competitions focused on univariate, low‑entropy series and did not fully evaluate ML’s potential on short‑interval, irregular, or high‑dimensional data.

## Approach

- Surveys classical parametric models: exponential smoothing (Holt‑Winters), ARIMA, theta method, and state‑space models (Kalman filter).
- Reviews nonlinear parametric models: threshold autoregression (TAR), smooth transition (STAR), and Markov‑switching models.
- Covers nonparametric forecasting (kernel, additive models) with curse‑of‑dimensionality caveats.
- Describes deep learning architectures: CNNs/TCNs, RNNs, LSTM (solves vanishing gradient), and transformers (“Attention is all you need”).
- Explains ensemble tree methods: random forest (bagging, variance reduction) and gradient boosting (sequential bias reduction, light‑GBM variant).
- Introduces explainable AI (XAI): SHAP values (Shapley additive explanations) for feature importance in black‑box models.
- Synthesizes evidence from Makridakis forecasting competitions (M1–M6), Kaggle web traffic data, and volatility forecasting with intraday commonality.
- Discusses extensions: probability forecasting, GARCH‑type models for integer/continuous time (INGARCH, Hawkes processes), cointegration + random forest hybrids, and weather forecasting (GraphCast, GenCast).

## Findings

1. In the M4 competition (100,000 series), hybrid methods combining statistical and ML components produced the top 10 most accurate forecasts; pure statistical or pure ML methods dominated the 10 least accurate.
2. **Light‑GBM gradient boosting dominated the M5 competition (intermittent retail sales), used by all 50 top competitors.**
3. GenCast (diffusion‑based probabilistic model) beat the ENS ensemble forecast in 97.2% of 1,320 weather targets (Nature 2024).
4. ML methods (MLP, LSTM) outperformed parametric models in volatility forecasting when intraday commonality information was included (93 stocks, 10‑year S&P data).
5. Random forest produced the best inflation forecasts among 122 explanatory variables (FRED‑MB database, 1960–2015).

- Transformers enable parallel processing, replacing RNN/LSTM recursive structures for long‑range dependence.
- XAI methods (SHAP, LIME) partially open the black box but face stability and interpretability challenges.

## Key Figures and Tables

None.

## Key Equations

$$ \hat{y}_{t+1} = \alpha y_t + (1 - \alpha) \hat{y}_t $$
*Exponential smoothing: weighted average of current value and previous forecast.*

$$ y_t = a_1 y_{t-1} + \cdots + a_p y_{t-p} + e_t $$
*AR(p) model: current value as linear combination of p past values plus noise.*

$$ y_t = \theta_1 y_{t-1} \mathbb{I}\{s_{t-1} \le c\} + \theta_2 y_{t-1} \mathbb{I}\{s_{t-1} > c\} + e_t $$
*Threshold autoregression: switches between two linear regimes based on a state process.*

$$ h_t = \sigma_h(W_h x_t + U_h h_{t-1} + b_h) $$
*RNN hidden state recurrence: memory updated from input and previous hidden state.*

$$ \lambda_t = d + a \lambda_{t-1} + b y_{t-1}, \quad y_t | \mathcal{F}_{t-1} \sim \text{Poisson}(\lambda_t) $$
*Poisson INGARCH: GARCH‑like recursion for count time series intensity.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| ARIMA | AutoRegressive Integrated Moving Average — linear model with differencing for nonstationary data. |
| LSTM | Long Short‑Term Memory — RNN variant with gates that prevent gradient vanishing [think: memory cell with forget/input/output gates]. |
| RNN | Recurrent Neural Network — neural net with cycles that maintain a hidden state over time. |
| TCN | Temporal Convolutional Network — CNN adapted for time series using causal convolutions. |
| Transformer | Neural architecture using attention instead of recurrence; enables parallel processing. |
| XAI | Explainable Artificial Intelligence — methods to interpret black‑box ML predictions. |
| SHAP | SHapley Additive exPlanations — game‑theory‑based feature importance scores. |
| GARCH | Generalized AutoRegressive Conditional Heteroskedasticity — volatility clustering model for financial returns. |
| VAR | Vector AutoRegression — multivariate linear model where each variable depends on lags of all others. |
| VECM | Vector Error Correction Model — VAR for cointegrated I(1) variables. |
| NWP | Numerical Weather Prediction — physics‑based atmospheric simulation. |
| Entropy (spectral) | Measure of time series disorder/predictability; higher entropy = harder to forecast. |

## Critical Citations

- [Box & Jenkins, 1970] — Established ARIMA modeling framework (identification‑estimation‑diagnostics) still used as baseline.
- [Hochreiter & Schmidhuber, 1997] — Original LSTM paper that solved vanishing gradient; >67,000 citations.
- [Vaswani et al., 2017] — “Attention is all you need” introduced transformers, enabling parallelization and long‑range dependence.
- [Makridakis et al., 2020] — M4 competition results showing hybrid statistical‑ML methods outperform pure approaches.
- [Makridakis et al., 2022] — M5 competition where light‑GBM gradient boosting beat all alternatives on intermittent retail data.

## Relevance to Odin

**Topics:**

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

J.1 — System Evaluation

**Contribution to Odin:**

This paper provides a comprehensive, evidence‑based comparison of forecasting methods that directly informs Odin’s spending forecasting module. The finding that LSTM outperforms alternatives in volatility forecasting with commonality (Zhang et al., 2024) supports Odin’s LSTM selection for per‑category spending predictions. The M5 competition results demonstrate that gradient boosting (light‑GBM) is superior for intermittent, zero‑inflated time series — a property relevant to Odin’s manual transaction data where many categories may have zero spending in a given period. The paper’s review of evaluation metrics (MAE, MAPE, forecast distributions) and the M4/M5 competition designs provide a methodological template for Odin’s ISO 25010 + SUS evaluation.

**Directly justifies:**

- “LSTM and MLP neural networks produced the best volatility forecasts among all models tested (including HAR, ARIMA, XGBoost) when intraday commonality information was included (Zhang et al., 2024, on 93 S&P stocks over 10 years).”
- “Light‑GBM gradient boosting dominated the M5 forecasting competition on intermittent retail sales data, characterized by many zero values and erratic unit sales — a pattern analogous to manual per‑category spending entry.”
- “Hybrid forecasting methods that combine statistical (exponential smoothing) and ML (RNN) components achieved top accuracy in the M4 competition, outperforming both pure statistical and pure ML approaches.”
- “Transformers and TCNs enable faster training than LSTMs due to parallelization, but LSTM remains competitive and better suited for shorter sequences where recursive state matters.”
- “The black‑box nature of ML forecasts remains a limitation; SHAP values provide one method to attribute feature importance, though stability issues exist.”

**Limits of relevance:**

- The paper focuses on general time series forecasting (retail, finance, weather), not specifically personal finance or budgeting behavior.
- All empirical results use non‑Filipino data (US, European, global) — demographic and cultural spending patterns may differ.
- Mobile‑specific constraints (battery, compute, offline operation) are not discussed; all ML comparisons assume server‑class hardware.
- Manual transaction entry (Odin’s scope) vs. automated bank feeds affects data frequency and noise levels; the paper does not address this distinction.

## Limitations

- No systematic comparison of ML methods on personal finance transaction data — domain gap limits direct applicability.
- Most cited competitions (M1–M6) evaluated point forecasts primarily; probability/interval forecasting evaluation is less mature. [unacknowledged]
- XAI methods (SHAP, LIME) are still criticized for instability and lack of deep mechanistic interpretation; the paper notes but does not resolve this.
- The review does not address cold‑start forecasting (new users with no history) — a critical scenario for Odin’s early adoption phase. [unacknowledged]
- Computational complexity (training time, memory) of LSTM vs. light‑GBM on mobile devices is not evaluated; all benchmarks assume cloud/server environments.

## Remember This

- 🔑 **Light‑GBM beat all competitors in M5** — intermittent data (many zeros) favors gradient boosting over LSTM or ARIMA.
- 📌 **LSTM + MLP won volatility forecasting** — with intraday commonality, neural nets outperformed GARCH and HAR models.
- 💡 **Hybrid statistical‑ML > pure ML or pure stats** — M4 showed combined methods dominate top‑10 accuracy rankings.
- ⚠️ **ML remains a black box** — SHAP helps but has stability issues; interpretability still lags behind linear models.
- ✅ **GenCast beat ENS in 97.2% of 1,320 targets** — diffusion‑based probabilistic forecasting sets new weather benchmark.
