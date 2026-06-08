# Continual Deep Learning for Time Series Modeling

## Metadata
```yaml
---
paper_id: "10.3390/s23167167"
designation: international
title: "Continual Deep Learning for Time Series Modeling"
authors: "Ao, S.-I.; Fayek, H."
year: 2023
venue: "Sensors"
odin_topics: ["6.A", "6.B", "8.A", "8.B", "12.B"]
shorthand_tags: ["/forecasting-methods-survey", "/forecast-algo-candidates", "/anomaly-ml-families", "/anomaly-algo-candidates", "/eval-ml-design"]
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
Continual learning mitigates catastrophic forgetting in deep learning models for non‑stationary time series, with strong results in forecasting and anomaly detection across sensor domains.

## Problem and Motivation
Deep learning models assume stationary data distribution, but real‑world time series often violate this. Non‑stationarity causes catastrophic forgetting — the abrupt loss of previously learned knowledge. Prior surveys focused on classification or computer vision, leaving a gap for time series forecasting and regression tasks.

## Approach
- Survey of deep learning (DL) models for sensor time series: MLP, RNN, LSTM, CNN, GNN, autoencoders, attention networks.
- Review of preprocessing techniques (EMD, wavelet, Fourier, segmentation, data augmentation) that improve DL performance.
- Taxonomy of continual learning (CL) methods: regularization‑based (e.g., elastic weight consolidation), replay‑based, parameter isolation, and combined approaches.
- Evaluation across real‑world sensor datasets: water treatment, traffic, ECG, human activity recognition, industrial fault prediction.
- Benchmarks compare CL against naive retraining and joint training on metrics like forgetting reduction and accuracy.

## Findings
1. CNN with direct multi‑step procedure improves day‑ahead load prediction by **22.6%** over seasonal ARIMAX (Cai et al.).
2. LSTM achieves MAPE of **4.82%** for traffic flow forecasting vs. 20.97% for ARIMA and 9.06% for BPNN (Zheng & Huang).
3. Graph Deviation Network (GDN) improves F‑measure by **54%** over the next best baseline for anomaly detection in water treatment systems.
4. MC‑SGD reduces catastrophic forgetting by **29%** compared to no CL in wearable activity recognition, with lower compute than joint training.
- Preprocessing (e.g., empirical mode decomposition) raises gesture classification accuracy from 94.22% to 99.73%.
- Regularization‑based CL (EWC, LwF) mitigates forgetting but often fails to accumulate knowledge over time; replay with exemplars works best on mobile/embedded devices.

## Key Figures and Tables
- Figure 1: Tree diagram of DL methods for time series (MLP, RNN, CNN, GNN, etc.) → Organizes model families used in surveyed papers.
- Table 1: Summary of DL advances for sensor time series (2019–2022) → Shows accuracy gains and application details across 17 studies.
- Figure 2: Tree diagram of preprocessing methods (decomposition, transformation, augmentation) → Categorizes techniques that boost DL performance.
- Table 3: Summary of CL techniques for time series (regularization, replay, isolation) → Lists motivations, accuracy, and deployment contexts.

## Key Equations
$$ L_i = \frac{1}{N_i}\sum_{r=1}^{N_i} L(y_{i,r}, \hat{y}_{i,r}; \theta_i) + \frac{q}{(i-1)N}\sum_{j=1}^{i-1}\sum_{r=1}^{N} L(y_{j,r}, M(\hat{x}_{j,r}; \theta_i); \theta_i) $$
*Continual learning loss balances new task data and replayed old samples weighted by q.*

## Definitions
| Term / Acronym | Plain‑English Definition |
| -------------- | ------------------------ |
| CL | Continual learning — learning sequentially from new data without forgetting old knowledge. |
| CF | Catastrophic forgetting — abrupt loss of previously learned knowledge when training on new data. |
| LSTM | Long Short‑Term Memory [think: memory cell with gates to keep or discard information over long sequences]. |
| CNN | Convolutional Neural Network — uses sliding filters to detect patterns regardless of position in time. |
| GNN | Graph Neural Network — operates on graph‑structured data, modeling relationships between multiple sensors. |
| EWC | Elastic Weight Consolidation — regularization method that penalizes changes to important weights. |
| EMD | Empirical Mode Decomposition — non‑linear filter that breaks a signal into oscillatory components (IMFs). |

## Critical Citations
- [Hochreiter & Schmidhuber, 1997] — Introduced LSTM, the foundation for most time series forecasting DL models.
- [Kirkpatrick et al., 2017] — Proposed elastic weight consolidation, a core regularization method for continual learning.
- [Choi et al., 2021] — Showed no single DL method universally fits all time series anomaly detection tasks.
- [Shi et al., 2015] — Developed ConvLSTM for spatiotemporal prediction, later applied to SST and precipitation forecasting.

## Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems (This survey reviews state‑of‑the‑art DL forecasting methods including LSTM, CNN‑LSTM, and attention, providing Odin’s RRL with evidence for algorithm selection.)

6.B — Spending Forecasting Algorithm (Compares forecasting accuracy of LSTM (MAPE 4.82%), CNN, and hybrid models, directly supporting Odin’s choice of sequential predictors.)

8.A — Anomaly Detection in Personal Finance Systems (Taxonomizes point, contextual, and collective anomalies in time series and reviews GDN and autoencoder‑based detection, relevant to Odin’s overspending alerts.)

8.B — Anomaly Detection Algorithm (Evaluates unsupervised and graph‑based anomaly detectors (Isolation Forest, GDN, variational autoencoders), with performance benchmarks usable for Odin’s algorithm justification.)

12.B — Evaluation of Algorithmic Modules (Reports quantitative metrics (MAPE, F‑measure, forgetting reduction) and cross‑model comparisons, supplying Odin with evaluation methodology examples.)

**Contribution to Odin:**

This paper supports Odin’s spending forecasting module by benchmarking LSTM, CNN, and hybrid models against traditional statistical methods, showing that deep learning consistently achieves lower error (e.g., 4.82% MAPE for LSTM). It justifies the use of preprocessing (e.g., detrending, wavelet transforms) to handle non‑stationary spending patterns of Filipino users. The review of anomaly detection algorithms (GDN, variational autoencoders, replay buffers) informs Odin’s anomaly detection module, particularly the need for unsupervised methods when labeled transaction anomalies are unavailable. Finally, the survey of continual learning methods (EWC, replay) provides a pathway for Odin to adapt to user behavioral drift over time without catastrophic forgetting.

**Directly justifies:**

- LSTM achieves substantially lower mean absolute percentage error than ARIMA (4.82% vs. 20.97%) for univariate time series forecasting (Zheng & Huang, 2020).
- Preprocessing via empirical mode decomposition improves deep learning classification accuracy from 94.22% to 99.73% for non‑stationary physiological signals (Kisa et al., 2020).
- Graph Deviation Networks detect anomalies in multivariate sensor time series with 54% better F‑measure than the next best baseline (Deng & Hooi, 2021).
- Replay‑based continual learning with exemplars offers the best trade‑off between system performance, storage, and compute for mobile/embedded sensing devices (Kwon et al., 2021).
- No single deep learning model universally fits all time series anomaly detection tasks; domain‑specific tuning remains necessary (Choi et al., 2021).

**Limits of relevance:**

- All case studies come from physical sensors (water, traffic, ECG, wearable) — not financial transaction sequences, which have different noise and sparsity characteristics.
- Findings are from systematic review, not a controlled experiment on personal finance data; Odin would cite individual primary studies rather than this survey for specific performance claims.
- The Philippine young professional context (income instability, family obligations, cash‑based spending) is not addressed; behavioral drift triggers differ from sensor non‑stationarity.
- Continual learning methods for time series are still emerging; most CL research focuses on classification, not forecasting or regression, limiting direct transfer to Odin’s spending prediction.

**Mapping Rationale:**

I screened all ten functional domains. The paper directly contributes to *spending forecasting* (time series prediction algorithms), *anomaly detection* (methods for identifying deviations), and *system evaluation* (benchmark metrics and comparison frameworks). Domains like expense categorization, mobile‑first design, data privacy, and savings/debt management have no substantive coverage. For each selected topic code: 6.A applies because the paper surveys forecasting methods (ARIMA, LSTM, CNN) and their relative performance; 6.B applies because it compares specific forecasting algorithms (e.g., LSTM vs. ARIMA); 8.A applies because it provides a taxonomy of anomalies (point/contextual/collective) and behavioral detection scenarios; 8.B applies because it reviews concrete anomaly detection algorithms (GDN, autoencoders, Isolation Forest); 12.B applies because the paper evaluates model performance using standard metrics (MAPE, F‑measure, accuracy) and discusses validation protocols. I rejected 5.C (behavioral profiling) because the paper does not address user classification or financial profiles. Borderline case: preprocessing (Section 2.7) is relevant to expense categorization only if feature engineering is discussed, but the paper focuses on signal denoising, not category taxonomies, so I did not select 3.A or 3.B.

## Limitations
- The survey aggregates findings from diverse sensor domains (water, traffic, medical); generalizability to personal financial time series is not tested.
- Most cited studies assume high‑frequency, dense sensor data (e.g., 5‑min traffic intervals) unlike Odin’s sparse, manually entered daily/weekly transactions.
- Continual learning methods for regression (e.g., spending amount prediction) receive far less attention than classification; the paper acknowledges this gap.
- [unacknowledged] The paper does not discuss computational cost or latency constraints for mobile‑first deployment, critical for Odin’s on‑device inference.
- [unacknowledged] No analysis of cold‑start scenarios (insufficient user history), which is a core challenge for Odin’s forecasting and profiling modules.

## Remember This
🔑 LSTM achieves 4.82% MAPE for time series forecasting, outperforming ARIMA (20.97%).
📌 Preprocessing via EMD boosts classification accuracy from 94% to over 99% for non‑stationary signals.
🔍 Graph Deviation Networks improve anomaly detection F‑measure by 54% over baseline methods.
🧠 Replay‑based continual learning works best on mobile devices, reducing forgetting by 29% (MC‑SGD).
⚠️ No single DL model works for all anomaly detection tasks — domain‑specific tuning is required.