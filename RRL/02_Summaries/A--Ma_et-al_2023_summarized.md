# Review of Family-Level Short-Term Load Forecasting and Its Application in Household Energy Management System

## Metadata

```yaml
---
paper_id: "10.3390/en16155809"
designation: algorithm-specific
title: "Review of Family-Level Short-Term Load Forecasting and Its Application in Household Energy Management System"
authors: "Ma, P.; Cui, S.; Chen, M.; Zhou, S.; Wang, K."
year: 2023
venue: "Energies"
odin_topics: ["D.1", "D.2"]
shorthand_tags: ["/forecasting-methods", "/spending-time-series", "/temporal-dependency", "/lstm-architecture", "/lstm-vs-alternatives", "/lstm-spending-applied", "/lstm-justification"]
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

LSTM and hybrid deep learning models achieve higher accuracy than classical methods for household-level time series forecasting, with hybrid CNN-LSTM capturing both short and long-term dependencies.

## Problem and Motivation

Household-level electricity load forecasting is difficult due to high randomness from human behavior and weather, unlike stable system-level loads. Accurate short-term forecasts are critical for home energy management systems (HEMS) to enable demand response and cost reduction. Prior methods (ARIMA, SVR) struggle with non-linear, non-stationary residential data, leaving a gap for deep learning approaches.

## Approach

- Review of deep learning methods for short-term load forecasting (STLF) at household and appliance levels.
- Focus on LSTM (solves gradient problems via memory cells and forget gates), CNN (local feature extraction), and hybrid LSTM–CNN models.
- Discussion of feature extraction techniques: wavelet decomposition (DWT), principal component analysis (PCA), mutual information (MI).
- Coverage of probabilistic load forecasting (PLF) to quantify uncertainty, and adaptive/online learning for dynamic consumption patterns.
- Bottom-up appliance-level forecasting using LSTM or Kalman filters, plus ultra-short-term (hourly) challenges.

## Findings

1. **LSTM outperforms other machine learning algorithms** for household load forecasting due to its ability to learn long-term dependencies (Kong et al.).
2. SVR–LSTM hybrid achieved the highest correlation coefficient **R = 0.9901** with lowest error, beating standalone SVR and LSTM.
3. CNNGRU with attention mechanism reached **92.06% accuracy** for small-range load prediction, reducing prediction time by 75%.
4. Hybrid LSTM–CNN models improve accuracy by combining short-term local pattern capture (CNN) with long-term dependency learning (LSTM).

- Probabilistic forecasting methods provide uncertainty intervals, which are essential for robust HEMS decision-making but traditional statistical PLFs fail on complex loads.
- Bottom-up appliance-level forecasting (predicting each device then aggregating) yields higher accuracy than direct household forecasting, though computationally more expensive.

## Key Figures and Tables

- Figure 1: LSTM block structure and unrolled sequential architecture → memory cell and forget gate solve gradient problems.
- Figure 2: LSTM-based forecasting framework → shows input sequence to output prediction pipeline.
- Figure 4: Load forecasting framework with preprocessing, feature extraction (DWT, CRT), and forecasting → demonstrates multi-stage approach.
- Figure 5: Probabilistic load forecasting framework → uncertainty intervals vs. point forecasts.
- Figure 6: Appliance-level deep learning forecasting model → bottom-up approach using LSTM per device.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LSTM | Long Short-Term Memory — a recurrent neural network with memory cells and gates that remembers relevant past states and forgets irrelevant ones [think: selective memory that learns what to keep]. |
| CNN | Convolutional Neural Network — extracts local patterns by sliding filters across data, originally for images. |
| HEMS | Home Energy Management System — a smart hub that optimizes household electricity use via scheduling and demand response. |
| STLF | Short-Term Load Forecasting — predicting electricity demand hours to days ahead. |
| NILM | Non-Intrusive Load Monitoring — disaggregating total household electricity into appliance-level usage without per-device sensors. |
| PLF | Probabilistic Load Forecasting — provides a range of possible outcomes with likelihoods, not just a single value. |

## Critical Citations

- [Hochreiter & Schmidhuber, 1997] — Introduced LSTM, the foundational architecture for sequence learning that solves gradient vanishing.
- [Kong et al., reference 11] — First demonstrated LSTM outperforms other ML algorithms for household load forecasting.
- [Zheng et al., 2018] — Established that bottom-up appliance-level prediction improves accuracy over direct household forecasting.

## Relevance to Odin

**Topics:**

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

**Contribution to Odin:**

This review directly justifies Odin’s selection of LSTM for the spending forecasting module by documenting LSTM’s superiority over classical methods (ARIMA, SVR) and other ML algorithms on household-level time series data with high randomness. The review’s analysis of hybrid LSTM–CNN models for capturing both short-term local patterns and long-term dependencies informs potential architectural improvements. Although the domain is electricity load, the core forecasting challenge—unpredictable human behavior causing non-stationary, irregular sequences—maps exactly to personal spending data. The discussion of adaptive online learning (e.g., Fekri et al.’s online RNN) supports Odin’s need for models that update as new transaction data arrives.

**Directly justifies:**

- “LSTM solves gradient vanishing/explosion problems in time series forecasting via memory cells and forget gates, making it suitable for irregular spending sequences.”
- “Hybrid LSTM–CNN models capture both short-term local spending patterns and long-term behavioral dependencies, improving forecast accuracy over standalone LSTM.”
- “Bottom-up forecasting—predicting per‑category spending then aggregating—achieves higher accuracy than direct total spending prediction, as verified in appliance-level load forecasting (Zheng et al., 2018).”
- “Online adaptive learning enables forecasting models to continuously update with new data, essential for capturing concept drift in user spending behavior.”
- “Probabilistic forecasting provides uncertainty intervals that robust optimization algorithms require; point forecasts alone are insufficient for risk-aware budget management.”

**Limits of relevance:**

- Domain is household electricity consumption, not financial spending; behavioral drivers differ though time series properties (randomness, human-driven patterns) are analogous.
- No evaluation on Filipino data or cultural spending contexts; all studies use non-Philippine smart meter datasets.
- The review aggregates findings from multiple studies; individual claims need original source verification for precise effect sizes.
- Data requirements (smart meters, hourly granularity) exceed Odin’s manual input model, though the methodological lessons remain applicable.

## Limitations

- Review paper without original experiments; all comparative claims are secondary from cited studies.
- Acknowledges own limitations: data quality issues (missing values, noise), model overfitting risk on small datasets, and lack of interpretability in deep learning models.
- No discussion of cold-start forecasting for new users with zero history — an unacknowledged gap relevant to Odin.
- Focus on short-term (hours/days ahead) rather than monthly spending forecasts; time scales differ.
- [unacknowledged] No comparison of computational cost between LSTM and lighter models (e.g., Kalman filter) on mobile devices — critical for Odin’s mobile‑first constraint.

## Remember This

- 🔑 **LSTM beat other ML models** — its memory cell and forget gate handle irregular, human‑driven sequences.
- 📌 **SVR–LSTM hit R=0.9901** — hybrid models can outperform pure LSTM for time series.
- 💡 Bottom‑up forecasting (per‑category → aggregate) **improves accuracy** over direct total prediction.
- ⚠️ Review paper — no original Odin‑specific data; use for methodology justification, not direct performance claims.
- 🧠 Online adaptive learning captures **concept drift** — Odin’s profile updates need similar retraining logic.
