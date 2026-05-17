# AI-Based Wealth Advisory System using Machine Learning and Predictive Analytics for Personalized Budget Planning

## Metadata

```yaml
---
paper_id: "10.15662/IJARCST.2025.0805004"
designation: algorithm-specific
title: "AI-Based Wealth Advisory System using Machine Learning and Predictive Analytics for Personalized Budget Planning"
authors: "Bhavana, B. R.; Pavan, D.; Darshan, G. T. H."
year: 2025
venue: "International Journal of Advanced Research in Computer Science & Technology (IJARCST)"
odin_topics: ["3.A", "4.A", "4.B", "5.C", "6.A", "6.B", "7.B", "7.C", "8.A", "8.B", "10.A", "10.B", "12.A", "12.B"]
shorthand_tags: ["/pfms-intelligent-features", "/pfms-limitations", "/classifier-candidates", "/classifier-eval-metrics", "/forecasting-methods-survey", "/forecast-algo-candidates", "/forecast-eval-metrics", "/budget-rec-approaches", "/budget-rec-algo-candidates", "/anomaly-algo-candidates", "/anomaly-eval-metrics", "/privacy-by-design", "/explainability-trust", "/sus", "/eval-ml-design"]
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

AI Wealth Advisor integrates forecasting, anomaly detection, and explainable AI to deliver personalized budget planning, achieving **95% anomaly detection accuracy** and a 22% improvement in savings in a pilot study.

## Problem and Motivation

Existing personal finance apps focus on reactive expense tracking rather than proactive wealth management, leaving users without predictive or adaptive capabilities. This gap contributes to poor financial literacy, unsustainable debt, and vulnerability to fraud, especially in emerging economies. No prior system combined classification, forecasting, anomaly detection, and explainable AI into a consumer-centric, personalized financial advisory solution.

## Approach

- **Datasets:** Transaction data (banking APIs), household expenditure surveys (U.S., India), macroeconomic indicators (World Bank, IMF), and European Credit Card Fraud Dataset for anomaly detection.
- **Preprocessing:** Cleaning, normalization, NLP-based categorization (merchant codes), anonymization (GDPR/CCPA), and KNN imputation for missing values.
- **Feature engineering:** Financial ratios (savings-to-income), behavioral patterns (spending spikes, seasonality), temporal features, and statistical anomaly features (z-scores, volatility).
- **Classification models:** XGBoost, Random Forest, and BERT for expense categorization; evaluated by F1-score and accuracy.
- **Forecasting models:** Ensemble of ARIMA, Prophet, LSTM, and Transformers; evaluated by MAE, RMSE, and R².
- **Anomaly detection:** Isolation Forest, Autoencoders, and GAN-based detectors; evaluated by ROC-AUC and Precision-Recall AUC.
- **Recommendation engine:** Contextual bandits and reinforcement learning for adaptive budget and savings suggestions.
- **Explainable AI (XAI):** SHAP and LIME provide natural language explanations (e.g., “Your grocery spending is 38% higher due to festival purchases”).
- **Privacy safeguards:** AES-256 encryption (at rest), TLS 1.3 (in transit), differential privacy, federated learning, and role-based access.
- **Evaluation metrics:** Classification (accuracy, precision, recall, F1), forecasting (MAE, RMSE, R²), anomaly detection (AUC), recommendation adoption rate, System Usability Scale (SUS).

## Findings

1. Expense classification achieved **91% F1-score** using XGBoost/RF and BERT.
2. Forecasting error was MAE of **$43/month per user** across the pilot.
3. Anomaly detection accuracy = **95%** using Isolation Forest and Autoencoders.
4. Recommendation adoption rate = 41% of suggested actions followed by users.

- Pilot study (100 users) showed a **22% improvement in savings** and 78% of participants reported enhanced financial literacy.
- SUS scores and user satisfaction surveys indicated improved trust and usability due to XAI transparency.

## Key Figures and Tables

None.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| AI | Artificial Intelligence – machines simulating human decision-making. |
| ML | Machine Learning – algorithms that learn from data without explicit rules. |
| XAI | Explainable AI – methods that make model outputs understandable to humans. |
| NLG | Natural Language Generation – converting data into plain English text. |
| LSTM | Long Short-Term Memory [think: neural network with a memory cell that learns what to forget] – a type of recurrent neural network for sequence prediction. |
| RNN | Recurrent Neural Network – neural network with loops for processing sequences. |
| ARIMA | AutoRegressive Integrated Moving Average – statistical model for time series forecasting. |
| GBDT | Gradient Boosted Decision Trees – ensemble method that builds trees sequentially to correct errors. |
| SHAP | SHapley Additive exPlanations – game-theory-based method to explain feature importance. |
| LIME | Local Interpretable Model-agnostic Explanations – explains individual predictions by approximating the model locally. |
| BERT | Bidirectional Encoder Representations from Transformers – deep learning model for understanding text context. |
| GAN | Generative Adversarial Network – two neural networks competing to generate realistic synthetic data. |
| SUS | System Usability Scale – standardized questionnaire measuring perceived usability. |
| AES | Advanced Encryption Standard – symmetric encryption algorithm for data protection. |
| TLS | Transport Layer Security – protocol for secure internet communication. |
| PII | Personally Identifiable Information – data that can identify a specific individual. |
| GDPR | General Data Protection Regulation – EU privacy law. |
| CCPA | California Consumer Privacy Act – US state privacy law. |
| KNN | K-Nearest Neighbors – algorithm that classifies based on closest training examples. |
| ROC | Receiver Operating Characteristic – curve showing true positive rate vs false positive rate. |
| AUC | Area Under the Curve – single metric summarizing ROC performance. |
| MAE | Mean Absolute Error – average absolute difference between predicted and actual values. |
| RMSE | Root Mean Square Error – square root of average squared errors, penalizing large errors more. |
| R² | R-squared – proportion of variance in the outcome explained by the model. |
| Anomaly detection | Identifying data points that deviate significantly from normal patterns. |
| Federated learning | Training models across decentralized devices without sharing raw data. |
| Differential privacy | Adding controlled noise to query results to prevent identifying individuals. |

## Critical Citations

- [Mohammed et al., 2021] — Autoencoder+Isolation Forest achieving 96% fraud detection accuracy, forming the anomaly detection baseline.
- [Zhang et al., 2022] — Hybrid ARIMA+GBDT reducing MAE by 18%, justifying ensemble forecasting approach.
- [Ribeiro et al., 2016] — LIME for model-agnostic interpretability, enabling explainable AI integration into black-box models.
- [Lundberg & Lee, 2017] — SHAP for consistent feature attribution, critical for user trust and regulatory acceptance.

## Relevance to Odin

**Topics:**

3.A — Expense Categorization Frameworks

4.A — Landscape of Existing Personal Finance Systems

4.B — Limitations and Gaps in Existing Systems

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

7.B — Budget Recommendation in Personal Finance Systems

7.C — Budget Recommendation Algorithm

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

10.A — Data Privacy and Security in Personal Finance Systems

10.B — User Trust in Personal Finance Systems

12.A — Evaluation Frameworks for Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly informs Odin’s expense categorization module by benchmarking XGBoost, Random Forest, and BERT, achieving 91% F1-score – a strong candidate for Odin’s classification task. The ensemble forecasting approach (ARIMA, Prophet, LSTM, Transformers) provides a validated architecture for Odin’s spending forecasting module, with reported MAE of $43/user/month as a baseline. The integration of Isolation Forest and Autoencoders for anomaly detection (95% accuracy) directly supports Odin’s anomalous spending detection requirements, while the use of SHAP and LIME for explainable AI demonstrates how to build user trust – a core Odin design principle. The paper’s pilot evaluation using SUS and adoption metrics offers a template for Odin’s system evaluation plan.

**Directly justifies:**

- “Anomaly detection using Isolation Forest and Autoencoders achieved 95% accuracy on financial transaction data, enabling real-time fraud and unusual spending alerts.”
- “Ensemble forecasting combining ARIMA, Prophet, LSTM, and Transformers produced a mean absolute error of $43 per user per month on spending prediction.”
- “XGBoost and BERT-based expense classification reached 91% F1-score, demonstrating that structured and unstructured transaction data can be categorized effectively without banking APIs.”
- “Contextual bandits and reinforcement learning for budget recommendation achieved a 41% adoption rate for suggested actions, indicating user acceptance of AI-driven advice.”
- “Explainable AI using SHAP and LIME translated anomaly scores into natural language (e.g., ‘grocery spending 38% higher due to festival’), which improved user trust and financial literacy for 78% of pilot participants.”

**Limits of relevance:**

- Pilot study population not described – unknown whether findings generalize to Filipino young professionals.
- System assumes banking API access for transaction data; Odin relies on manual input only, which may affect anomaly detection and forecasting accuracy.
- No cold-start evaluation – performance for new users with limited transaction history is not reported.
- Anomaly detection dataset (European credit card fraud) differs from Philippine spending patterns; cultural expense norms may alter false positive rates.
- Forecasting MAE of $43 is absolute dollar value; applicability to Philippine peso and lower average incomes requires recalibration.

## Limitations

- The paper does not disclose the demographic composition of the pilot sample, limiting generalizability to Filipino young professionals.
- No evaluation of the system under cold-start conditions (users with <30 days of transaction history). [unacknowledged]
- Reliance on banking APIs (Open Banking, PSD2) assumes infrastructure not available in the Philippine context.
- The paper acknowledges algorithmic bias risks but does not test fairness across income or demographic groups.
- Recommendation adoption rate (41%) is reported without longitudinal retention data; long-term user engagement remains unknown.

## Remember This

- 🔑 **95% anomaly detection accuracy** – Isolation Forest + Autoencoders beat supervised methods on unlabeled transaction data.
- 📌 91% F1-score for expense categorization – XGBoost and BERT work without banking APIs, using merchant codes and NLP.
- 💡 Ensemble forecasting (ARIMA+Prophet+LSTM) gave **$43 MAE per user** – a benchmark for Odin’s spending prediction module.
- ⚠️ No cold-start evaluation – unknown if accuracy holds for new Odin users with sparse transaction history.
- ✅ SHAP+LIME explanations boosted financial literacy for 78% of users – XAI is critical for user trust in Odin.
