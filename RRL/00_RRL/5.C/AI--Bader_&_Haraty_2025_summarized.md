# Bridging AI and Emotion: Enhanced Models for Personal Finance Manager Applications

## Metadata

```yaml
---
paper_id: "10.12785/ijcds/1571107231"
designation: algorithm-specific
title: "Bridging AI and Emotion: Enhanced Models for Personal Finance Manager Applications"
authors: "Bader, S.; Haraty, R. A."
year: 2025
venue: "International Journal of Computing and Digital Systems"
odin_topics: ["4.A", "4.B", "5.A", "5.C", "6.A", "6.B", "7.B", "8.A", "8.B", "12.B"]
shorthand_tags: ["/pfms-typology", "/pfms-limitations", "/profiling-role", "/classifier-candidates", "/forecasting-methods-survey", "/forecast-algo-candidates", "/budget-rec-approaches", "/anomaly-taxonomy", "/anomaly-algo-candidates", "/eval-ml-design"]
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

Sentiment analysis integration reduces financial forecasting error by **25%** (MAPE 7.8% vs 10.5%) and anomaly detection achieves 92% accuracy with 90% precision in a personal finance manager.

## Problem and Motivation

Existing financial advisory apps rely on static rule‑based structures that ignore user sentiment, spending behavior, and emotional context, leading to irrelevant recommendations and low engagement. This lack of personalization reduces user satisfaction and undermines trust in digital financial planning tools. No prior system integrated semantic AI, adaptive learning, and anomaly detection in a unified, user‑centric architecture.

## Approach

- **Dataset**: Bank transaction logs, merchant category codes (MCC), account balances, and user profiles – aggregated from multiple tables.
- **Sentiment analysis**: Fine‑tuned BERT and GPT on transaction descriptions to classify 10 emotion types (e.g., Stressed, Adventurous).
- **Anomaly detection**: Isolation Forest, Local Outlier Factor (LOF), and One‑Class SVM – real‑time scoring with alerts for deviations >5%.
- **Predictive models**: Transformer, Temporal Convolutional Network (TCN), and N‑BEATS for spending forecasting.
- **Evaluation metrics**: MAPE (prediction error), precision/recall, ROC‑AUC for anomalies; K‑fold cross‑validation and grid search.
- **Integration**: Backend in .NET Core 6; front‑end dashboard with spending charts, budget widgets, and merchant recommendation engine.

## Findings

1. Sentiment analysis improved MAPE from **10.5% to 7.8%** – a **25% relative reduction** in prediction error.
2. Anomaly detection achieved **precision 90%**, recall 85%, F1‑score 87.5%, and ROC‑AUC **0.93**.
3. Predictive accuracy within 90% confidence interval reached **88%** alignment with actual user behavior.
4. **N‑BEATS was the best performer** (RMSE 0.057), followed by Transformer (0.062) and TCN (0.074).

- Sentiment‑aware models captured spending fluctuations more accurately than non‑sentiment versions, especially for N‑BEATS.
- Real‑time anomaly alerts with user feedback loops reduced false positives over time.

## Key Figures and Tables

- Figure 13 (Transformer without SA): Predicted vs. actual spending with time lag – MAPE not shown but trend capture partial.
- Figure 14 (TCN without SA): MAPE ~5% error, most predictions close to actual.
- Figure 15 (N‑BEATS without SA): Predicted line smooth, misses variability – suggests need for sentiment.
- Figure 16 (Transformer with SA): MAPE improved, tighter fit – sentiment adds precision.
- Table 1: Comparison vs. traditional fraud systems and budgeting apps – our model shows 90% precision vs. 70–80% for others.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| NLP | Natural Language Processing – teaching computers to understand human text. |
| BERT | Bidirectional Encoder Representations from Transformers – a deep learning model for understanding context in text. |
| GPT | Generative Pre‑trained Transformer – a model for generating and analyzing text. |
| LSTM | Long Short‑Term Memory [think: memory cell that learns what to keep and what to forget] – a neural network for sequences. |
| TCN | Temporal Convolutional Network – uses layered convolutions to predict time‑series data. |
| N‑BEATS | Neural basis expansion analysis for interpretable time series forecasting – breaks forecasts into trend and seasonality. |
| MCC | Merchant Category Code – a four‑digit code that classifies a business (e.g., 5812 for restaurants). |
| SVM | Support Vector Machine – finds a boundary that separates normal data from anomalies. |
| LOF | Local Outlier Factor – detects anomalies by comparing local density around a data point. |
| ROC‑AUC | Receiver Operating Characteristic – Area Under Curve – measures how well a model separates normal vs. abnormal. |
| MAPE | Mean Absolute Percentage Error – average prediction error as a percentage. |
| RMSE | Root Mean Squared Error – standard deviation of prediction errors. |

## Critical Citations

- [Goodfellow et al., 2016] — Foundational deep learning reference that underpins the paper’s neural architectures.
- [Bollen et al., 2011] — Demonstrated that Twitter mood predicts stock market moves, directly motivating sentiment analysis in finance.
- [Chandola et al., 2009] — Comprehensive anomaly detection survey that informs the choice of Isolation Forest and LOF.
- [El Abaji & Haraty, 2025] — Related work on combining AI, sentiment, and financial models for Bitcoin forecasting, establishing prior art in sentiment‑driven financial AI.

## Relevance to Odin

**Topics:**

4.A — Landscape of Existing Personal Finance Systems

4.B — Limitations and Gaps in Existing Systems

5.A — Financial Behavioral Profiles in Personal Finance

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

7.B — Budget Recommendation in Personal Finance Systems

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly informs Odin’s forecasting, anomaly detection, and user profiling modules. The finding that sentiment analysis reduces MAPE by 25% justifies integrating emotional signals into Odin’s spending predictor – a feature absent from most budget apps. The anomaly detection benchmark (90% precision, 0.93 AUC) provides a target for Odin’s fraud and over‑spending alerts, while the multi‑model comparison (Transformer vs. TCN vs. N‑BEATS) offers evidence for algorithm selection under different data characteristics. Although the study uses bank‑linked transactions, the methodology transfers directly to Odin’s manual‑input context because the core models operate on transaction descriptions and amounts, not API data.

**Directly justifies:**

- “Integrating sentiment analysis into financial forecasting reduces MAPE from 10.5% to 7.8% – a 25% error reduction over models without emotional context.”
- “Anomaly detection using Isolation Forest and One‑Class SVM achieves 90% precision and 85% recall on financial transactions, outperforming rule‑based systems (typically 70–80%).”
- “N‑BEATS outperforms Transformer and TCN for spending forecasting (RMSE 0.057 vs 0.062 and 0.074), making it the leading candidate for Odin’s forecasting module.”
- “Real‑time anomaly alerts with user feedback loops improve model precision over time, reducing false positives without retraining from scratch.”

**Limits of relevance:**

- Dataset is from Lebanese / international sources, not Filipino – spending patterns and cultural categories may differ.
- The application assumes access to rich transaction descriptions (e.g., merchant names, item details); Odin’s manual input may provide sparser text, potentially reducing sentiment analysis accuracy.
- Computational requirements of Transformer and N‑BEATS may exceed mobile‑first constraints; Odin would need to run these server‑side or use lighter variants.
- No evaluation of cold‑start performance (users with no transaction history) – a critical gap for Odin’s new user onboarding.

## Limitations

- Generalization across diverse financial behaviors and demographics not tested – Filipino young professionals may exhibit different patterns.
- Computational efficiency of deep learning models not benchmarked for mobile or low‑resource environments. [unacknowledged]
- User trust and adoption measured only via satisfaction surveys; no behavioral economics analysis of how users respond to sentiment‑based advice.
- Cold‑start scenario (new user with zero transactions) completely unaddressed – all models require historical data. [unacknowledged]
- Sentiment classification depends on text quality; manual‑input transactions may lack the descriptive richness of bank‑derived data.

## Remember This

- 🔑 **MAPE fell 25%** – sentiment analysis cuts forecast error from 10.5% to 7.8%.
- 📌 **Anomaly detection hits 90% precision** – Isolation Forest matches Odin’s fraud alert needs.
- 💡 N‑BEATS (RMSE 0.057) beats Transformer and TCN – strongest candidate for spending forecasting.
- ⚠️ No cold‑start evaluation – unknown if these gains hold for new Odin users with zero history.
