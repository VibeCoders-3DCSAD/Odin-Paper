# Forecasting Stock Market Prices Using Machine Learning and Deep Learning Models: A Systematic Review, Performance Analysis and Discussion of Implications

## Metadata

```yaml
---
paper_id: "10.3390/ijfs11030094"
designation: algorithm-specific
title: "Forecasting Stock Market Prices Using Machine Learning and Deep Learning Models: A Systematic Review, Performance Analysis and Discussion of Implications"
authors: "Sonkavde, G.; Dharrao, D. S.; Bongale, A. M.; Deokate, S. T.; Doreswamy, D.; Bhat, S. K."
year: 2023
venue: "International Journal of Financial Studies"
odin_topics: ["6.A", "6.B"]
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

Ensemble of Random Forest, XGBoost, and LSTM achieved the lowest RMSE (2.0247) and highest R² (0.9921) for stock price forecasting, outperforming all individual models.

## Problem and Motivation

Stock market price prediction is inherently difficult due to high volatility and the limitations of traditional technical/fundamental analysis. Accurate forecasting directly impacts investors, traders, and financial institutions, yet no single model works universally. Prior systematic reviews lacked a direct empirical comparison of recent ML/DL models alongside a proposed ensemble method.

## Approach

- Systematic review of supervised ML (linear regression, SVM, KNN, Naïve Bayes, logistic regression), time series (ARIMA, FB Prophet), deep learning (LSTM, GRU), and ensemble methods (random forest, XGBoost, bagging, stacking).
- Generic ML pipeline: data loading (Yahoo Finance API), preprocessing, feature selection, 80/20 train-test split, training, evaluation, hyperparameter tuning.
- Implemented SVR, MLPR, KNN, random forest, XGBoost, LSTM, and a novel ensemble (Random Forest + XGBoost + LSTM) on two Indian chemical stocks: TAINIWALCHM (2014–2023) and AGROPHOS (2018–2023).
- Hyperparameter tuning via grid search (e.g., n_estimators, max_depth, learning rate, LSTM layers/dropout).
- Evaluation metrics: Root Mean Square Error (RMSE) and R² score.

## Findings

1. **Ensemble (RF+XGBoost+LSTM) achieved the best performance**: RMSE 2.0247 (TAINIWALCHM) and 1.2658 (AGROPHOS); R² 0.9921 and 0.9897, respectively.
2. XGBoost alone performed strongly: RMSE 2.0686 (TAINIWALCHM) and 1.7618 (AGROPHOS); R² 0.9842 and 0.9379.
3. LSTM (RMSE 5.6241, R² 0.8867) and GRU (MAE 42.8 without sentiment) work well but are outperformed by ensembles.

- Random forest had very high RMSE (87.88) on TAINIWALCHM, showing poor suitability for this stock’s pattern without tuning.
- Hyperparameter tuning is crucial; a lower learning rate may improve generalization at cost of slower convergence.

## Key Figures and Tables

- Figure 7: TAINIWALCHM forecasts (SVR, MLPR, KNN, RF, XGBoost, LSTM, ensemble) → Ensemble plot tracks actual prices most closely.
- Figure 8: AGROPHOS forecasts (same algorithms) → Ensemble again shows tightest fit.
- Table 2: RMSE and R² for all algorithms → Ensemble has lowest RMSE and highest R² on both stocks.
- Table 3: Summary of 14 algorithms with gap analysis and reported performance → LSTM + sentiment improves MAE from 48.47 to 17.69.

## Key Equations

$$fga = \sigma (W_{fg} [h_{t-1}, X_c] + b_f)$$
*Forget gate in LSTM – decides which past information to discard.*

$$Z[t] = \sigma (W^{(z)} x_t + U^{(z)} h_{t-1})$$
*Update gate in GRU – controls how much past state to keep.*

$$y'_t = k + \beta_1 y'_{t-1} + \dots + \beta_p y'_{t-p} + \theta_1 \varepsilon_{t-1} + \dots + \theta_q \varepsilon_{t-q} + \varepsilon_t$$
*ARIMA combines autoregressive and moving average components.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LSTM | Long Short-Term Memory – RNN variant with gates to remember long sequences [think: memory cell with forget/input/output gates]. |
| GRU | Gated Recurrent Unit – simpler RNN with only update and reset gates; trains faster than LSTM. |
| RMSE | Root Mean Square Error – measures average prediction error, penalizing large errors heavily. |
| R² | Coefficient of determination – how much variance the model explains (1 = perfect). |
| XGBoost | Extreme Gradient Boosting – ensemble that builds trees sequentially, each correcting prior errors. |
| Random forest | Ensemble of many decision trees trained on random data subsets; averages their predictions. |
| Ensemble learning | Combining multiple models to improve accuracy and reduce overfitting. |
| Hyperparameter tuning | Searching for optimal settings (e.g., learning rate, tree depth) before training. |

## Critical Citations

- [Di Persio & Honchar, 2017] – Foundational comparison of RNN, LSTM, GRU for financial forecasting.
- [Patel et al., 2015] – Demonstrated random forest for stock direction prediction using trend determinants.
- [Zhu & He, 2022] – Showed XGBoost outperformed ARIMA and LSTM for Amazon stock price.
- [Li & Pan, 2021] – Blending ensemble (LSTM+GRU) reduced RMSE to 186.32 and improved precision.

## Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

**Contribution to Odin:**

This paper directly informs Odin’s spending forecasting module by providing a systematic comparison of candidate algorithms (LSTM, GRU, XGBoost, random forest, ensembles) on time-series financial data. The empirical result that an ensemble of Random Forest, XGBoost, and LSTM achieves the lowest RMSE justifies considering ensemble methods for per-category spending prediction. The paper’s emphasis on hyperparameter tuning as critical to performance supports Odin’s need for a tuning framework when deploying forecasting models on user transaction histories.

**Directly justifies:**

- “Ensemble of Random Forest, XGBoost, and LSTM achieved RMSE of 2.0247 and R² of 0.9921 on stock price data, outperforming individual models.”
- “XGBoost alone achieved RMSE of 2.0686 on one stock and 1.7618 on another, demonstrating gradient boosting’s effectiveness for financial time-series forecasting.”
- “Hyperparameter tuning (e.g., learning rate, tree depth, number of LSTM layers) is crucial; a lower learning rate may improve generalization to new data.”
- “LSTM with sentiment analysis reduced MAE from 48.47 to 17.69, indicating that adding exogenous data improves forecasting accuracy.”

**Limits of relevance:**

- Domain is stock market price prediction, not personal spending forecasting – spending patterns may have different seasonality and noise characteristics.
- Dataset sizes not specified; the ensemble’s performance under cold-start (no user history) is not evaluated.
- Study uses Indian stock data; Filipino spending behavior may not share the same statistical properties.
- No discussion of computational constraints on mobile devices – ensemble of three models may be too heavy for on-device inference.

## Limitations

- No universal solution exists; even AI models fail if not retrained with fresh data (paper acknowledges).
- Ensemble model’s computational cost and inference latency are not analyzed – may be unsuitable for real-time mobile use. [unacknowledged]
- Hyperparameter grid search results are not fully reported for each algorithm, reducing reproducibility.
- The systematic review does not include a PRISMA-style flow or quality assessment of cited papers. [unacknowledged]
- No evaluation on spending or budget adherence data – all experiments are on stock prices only.

## Remember This

- 🔑 **Ensemble RMSE 2.0247** – RF+XGBoost+LSTM beats every single model on both stocks.
- 💡 XGBoost alone nearly matches the ensemble – gradient boosting is a strong starting point.
- ⚠️ Random forest flopped on one stock (RMSE 87.88) – not all ensembles work for every time series.
- 🔍 Hyperparameter tuning is not optional – lower learning rates improve generalization at cost of speed.
- 🧠 LSTM + sentiment analysis cut MAE from 48.47 to 17.69 – external data helps forecasting.
