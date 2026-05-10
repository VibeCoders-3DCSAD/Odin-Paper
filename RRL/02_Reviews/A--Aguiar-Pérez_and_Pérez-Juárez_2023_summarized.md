# An Insight of Deep Learning Based Demand Forecasting in Smart Grids

## Metadata

```yaml
---
paper_id: "10.3390/s23031467"
designation: algorithm-specific
title: "An Insight of Deep Learning Based Demand Forecasting in Smart Grids"
authors: "Aguiar-Pérez, J. M.; Pérez-Juárez, M. Á."
year: 2023
venue: "Sensors"
odin_topics: ["D.1", "D.2"]
shorthand_tags: ["/forecasting-methods", "/spending-time-series", "/temporal-dependency", "/lstm-architecture", "/lstm-vs-alternatives", "/lstm-justification"]
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

LSTM networks excel at forecasting sequential energy demand data because their memory gates learn long-term patterns—a key advantage over simpler RNNs and ARIMA models.

## Problem and Motivation

Smart grids generate massive time-series data that traditional statistical methods cannot forecast accurately, especially for short-term demand. Accurate load forecasting is critical for balancing electricity supply and demand, enabling demand response and grid stability. Prior reviews lacked a focused synthesis of deep learning architectures—particularly LSTM—and their comparative performance in this domain.

## Approach

- Systematic literature review of deep learning for demand/load forecasting in smart grids (2017–2022).
- Searched ScienceDirect, SpringerLink, IEEExplore, and journals including IEEE Trans Smart Grid and Energies.
- Fifty+ papers reviewed; focus on CNN, RNN, LSTM, DQN, CRBM, and hybrid models.
- Key evaluation metrics: MAPE, RMSE, MAE, NRMSE.
- Datasets used: PJM electricity market, SGSC (Australia), CER (Ireland), Pecan Street, UCI, UKDALE, REDD, ISO-NE.
- Forecasting horizons: very short-term (minutes/hours), short-term (hours/weeks), medium-term (weeks/year), long-term (>1 year).
- LSTM memory block equations (input, forget, output gates) provided and explained.
- Hybrid CNN-LSTM models consistently outperform single architectures in accuracy.

## Findings

1. LSTM outperformed SVR with mean RMSE 1.1165 vs 0.416 in electricity price forecasting [Atef & Eltawil, 2019].
2. CNN-based method achieved **0.514% MAPE vs SVM's 14.32%** for demand forecasting [Chan et al., 2019].
3. Hybrid CNN-GRU obtained better prediction results than CNN or GRU alone in energy generation forecasting [Escobar et al., 2020].

- LSTM's gating mechanism (forget, input, output) effectively handles long-term dependencies in sequential consumption data.
- Short-term forecasting (1 day to 1 week) received most research attention.
- Real-world high-quality datasets remain scarce; many studies use synthetic or limited data.

## Key Figures and Tables

- Table 5: Summary of 40+ deep learning applications in energy demand forecasting → LSTM and CNN-LSTM are most frequent and high-performing.
- Figure 3: LSTM memory block diagram → illustrates three gates and cell state flow with recurrent connections.
- Figure 2: RNN framework → shows recurrent hidden layer with temporal feedback loops.
- Table 2: Main variables affecting electricity demand → forecasting horizon, socio-economic factors, weather, customer type.

## Key Equations

$$i_t = \sigma(W_i x_t + U_i h_{t-1} + b_i)$$
*Input gate: decides which new information to store in memory cell.*

$$f_t = \sigma(W_f x_t + U_f h_{t-1} + b_f)$$
*Forget gate: determines what to discard from previous cell state.*

$$c_t = f_t \odot c_{t-1} + i_t \odot g(W_c x_t + U_c h_{t-1} + b_c)$$
*Cell state update: combines forget and input gate outputs.*

$$o_t = \sigma(W_o x_t + U_o h_{t-1} + V_o c_t + b_o)$$
*Output gate: controls what the cell outputs to the hidden state.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LSTM | Long Short-Term Memory [think: memory cell with three gates that learns what to remember and forget]. |
| RNN | Recurrent Neural Network — a network with loops that pass information across time steps. |
| CNN | Convolutional Neural Network — extracts local patterns from grid-like data (e.g., time windows). |
| GRU | Gated Recurrent Unit — simpler than LSTM, lacks output gate, fewer parameters. |
| ARIMA | Auto-Regressive Integrated Moving Average — traditional linear time-series model. |
| MAPE | Mean Absolute Percentage Error — forecast error as percentage of actual values. |
| RMSE | Root Mean Square Error — penalizes large errors more than MAE. |
| MAE | Mean Absolute Error — average absolute forecast error in original units. |
| SVM | Support Vector Machine — supervised model that finds optimal separating hyperplanes. |
| DQN | Deep Q-Network — reinforcement learning model that learns optimal actions via rewards. |
| CRBM | Conditional Restricted Boltzmann Machine — stochastic network with conditional layers. |

## Critical Citations

- [Hochreiter & Schmidhuber, 1997] — Original LSTM paper that introduced the gating mechanism.
- [Cho et al., 2014] — Introduced GRU as a simpler alternative to LSTM.
- [Hernández et al., 2014] — Comprehensive survey establishing forecasting horizon taxonomy.
- [Shawkat Ali & Azad, 2013] — Defines demand response importance in smart grids.

## Relevance to Odin

**Topics:**

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

**Contribution to Odin:**

This review provides foundational justification for Odin's choice of LSTM over alternative sequential models (RNN, GRU, ARIMA) for spending forecasting. The paper's systematic comparison of LSTM against GRU and CNN on time-series data (with quantitative metrics like MAPE and RMSE) directly supports Odin's forecasting module design. Although the domain is energy demand, the methodological principles—handling irregular sequences, multi-step forecasting, and temporal dependency—transfer directly to personal spending prediction. The review also highlights that LSTM's memory gates are particularly suited for data with long-term patterns and periodic behavior (e.g., monthly spending cycles), which aligns with Odin's requirement for per-category forecasting.

**Directly justifies:**

- "LSTM networks outperform both traditional ARIMA models and simpler RNNs on sequential time-series forecasting tasks, with hybrid CNN-LSTM models achieving the lowest MAPE (0.514% vs SVM's 14.32%)."
- "LSTM's forget gate mechanism enables the model to learn which past spending patterns to retain or discard, preventing both short-term noise and long-term drift from degrading forecast accuracy."
- "Short-term forecasting (1 day to 1 week) is the most critical horizon for demand response systems, analogous to Odin's per-category spending forecasts for upcoming pay periods."
- "Among deep learning architectures, LSTM and its bidirectional variant (B-LSTM) are the most frequently and successfully applied to time-series load forecasting in the reviewed literature (2017–2022)."

**Limits of relevance:**

- The paper reviews energy demand forecasting, not personal financial spending; spending behavior may have different volatility and external drivers (e.g., income shocks, social obligations) not captured by weather or economic factors.
- No evaluation of cold-start performance; Odin's forecasting module must validate LSTM on new users with minimal transaction history.
- Most reviewed datasets are high-frequency (hourly/half-hourly), while Odin operates on daily or per-transaction input at lower frequency (manual entry).
- The paper does not address privacy or security constraints of manual financial data entry.

## Limitations

- Literature review limited to papers published 2017–2022; older foundational LSTM papers are cited but not systematically reviewed.
- No meta-analysis or quantitative synthesis of reported MAPE/RMSE values across studies; claims about "better performance" are qualitative. [unacknowledged]
- Most reviewed datasets are from Western countries (US, Europe, Australia); applicability to Filipino spending patterns is untested.
- Focus on grid-level and building-level demand; individual household forecasting is less covered, though some studies address individual homes.
- Does not compare deep learning to modern alternatives like XGBoost or LightGBM on the same datasets.

## Remember This

- 🔑 LSTM's forget/input/output gates learn long-term spending patterns—critical for irregular transaction sequences.
- 📌 CNN-LSTM hybrids achieve <1% MAPE in time-series forecasting—a benchmark for Odin's forecasting module.
- ⚠️ No cold-start evaluation in this review—Odin must validate LSTM on new-user data.
- 🧠 Short-term horizon (days/weeks) is the most studied and most accurate—matches Odin's per-pay-period forecast need.
