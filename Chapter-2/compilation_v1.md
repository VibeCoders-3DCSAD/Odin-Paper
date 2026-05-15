# An Insight of Deep Learning Based Demand Forecasting in Smart Grids
*by Aguiar-Pérez, J. M., Pérez-Juárez, M. Á., 2023*

## TL;DR
LSTM networks excel at forecasting sequential energy demand data because their memory gates learn long-term patterns—a key advantage over simpler RNNs and ARIMA models.

## Topics
D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

## Contribution to Odin
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

---

# Next.js-Powered AI Platform for Smart Expense Tracking, Budgeting and Insights
*by Badiger, R., Robin, R., Moraas, T., Naik, V. G., Karthikeyan, A. N., 2026*

## TL;DR
Spend AI combines XGBoost categorization (91.3% F1) and Gemini LLM insights in a Next.js platform, cutting manual expense logging by 78%.

## Topics
A.2 — Existing Personal Finance and Budget Management Systems

C.1 — Budgeting Strategies and Budget Recommendation

C.2 — Budget Recommendation Algorithm

D.1 — Predictive Modeling in Personal Finance Systems

E.1 — Anomaly Detection in Personal Finance Systems

G.1 — Expense Categorization in Filipino Personal Finance Contexts

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

I.1 — User Retention and Engagement in Personal Finance Systems

J.1 — System Evaluation

## Contribution to Odin
This paper provides a production-ready blueprint for Odin’s expense categorization module, showing that XGBoost achieves 91.3% F1 on 18 categories – directly applicable to Odin’s FIES‑based classification task. The Gemini + RAG insight pipeline informs Odin’s budgeting and anomaly alerting modules, demonstrating how LLMs can generate natural-language spending advice grounded in user data. The 78% reduction in manual effort supports Odin’s retention strategy (value‑driven engagement over gamification). While Odin uses LSTM for forecasting, the Prophet-based approach here offers a simpler cold‑start alternative that may be cited as a baseline comparison.

**Directly justifies:**
- “XGBoost achieves 91.3% weighted F1-score for transaction categorization across 18 spending categories on a 4,200‑transaction test set.”
- “Manual expense-logging effort is reduced by approximately 78% using ML-based automated categorization compared to conventional apps.”
- “Gemini LLM with retrieval-augmented generation produces structured financial insights that 84% of users find useful for spending decisions.”
- “Row-level security in Supabase PostgreSQL enforces per-user financial data isolation at the database level, meeting privacy requirements for personal finance apps.”
- “Prophet time-series forecasting provides per-category expenditure predictions with 90% credible intervals, requiring only three months of history for reliable forecasts.”

**Limits of relevance:**
- Study population is Indian (UPI‑centric); Filipino spending patterns and payment channels (e.g., GCash, Maya) may differ.
- Odin uses LSTM for forecasting; this paper uses Prophet – can be cited as an alternative but not a direct justification for LSTM.
- Platform relies on manual entry or CSV import; Odin also uses manual input, but the paper does not evaluate entry friction reduction for first-time users.
- Cold-start categorization accuracy for users with fewer than 50 transactions is not reported; Odin faces the same challenge.
- No evaluation of long-term retention or behavioral drift beyond pilot user feedback.

---

# ARTIFICIAL INTELLIGENCE-DRIVEN PERSONAL FINANCE SOLUTION
*by Bashshar, S. A., Imran, M., Kumar, P. S., Goud, E. S., Venunath, M., Prasad, M. L. M., 2025*

## TL;DR
NLP‑based transaction categorization reaches 86.2% accuracy; ARIMA forecasts 30‑day expenses with MAE 253.47.

## Topics
A.2 — Existing Personal Finance and Budget Management Systems

D.1 — Predictive Modeling in Personal Finance Systems

G.1 — Expense Categorization in Filipino Personal Finance Contexts

## Contribution to Odin
This paper directly informs Odin’s expense categorization module by demonstrating that a Random Forest classifier with TF‑IDF achieves 86.2% accuracy on raw transaction descriptions, providing a baseline for FIES‑grounded category mapping. The ARIMA forecasting results (MAE 253.47 on six‑month data) serve as a statistical benchmark against which Odin’s LSTM‑based forecasting module can be compared, especially for cold‑start or low‑data scenarios. Although the system is web‑based, its modular architecture and use of lightweight SQLite align with Odin’s manual‑input, mobile‑first design constraints.

**Directly justifies:**
- “Random Forest with TF‑IDF achieves 86.2% categorization accuracy on financial transaction descriptions using a 1,000+ labeled dataset.”
- “ARIMA forecasts 30‑day expenses with MAE 253.47 and RMSE 318.91 on six months of historical spending data.”
- “Overlaps between semantically similar categories (e.g., Dining vs. Groceries) remain a challenge, requiring more domain‑specific training data.”
- “User feedback indicates that clear visualizations and forward forecasts improve perceived financial control and engagement.”

**Limits of relevance:**
- Study population is not Filipino; spending patterns and category relevance may differ.
- No mobile‑specific evaluation (web interface only); Odin’s mobile constraints may alter categorization and forecasting performance.
- Dataset size (1,000+ transactions) is small; Odin’s classification module will need more data or transfer learning.
- ARIMA assumes stationarity and may not capture irregular spending spikes common among young professionals.

---

# AI-Based Wealth Advisory System using Machine Learning and Predictive Analytics for Personalized Budget Planning
*by Bhavana, B. R., Pavan, D., Darshan, T. H. Guru, 2025*

## TL;DR
An AI wealth advisor using forecasting, anomaly detection, and explainable AI achieved **95% anomaly detection accuracy** and 22% savings improvement in a 100-user pilot.

## Topics
A.2 — Existing Personal Finance and Budget Management Systems

C.2 — Budget Recommendation Algorithm

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

E.1 — Anomaly Detection in Personal Finance Systems

E.2 — Anomaly Detection Algorithm

G.1 — Expense Categorization in Filipino Personal Finance Contexts

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

J.1 — System Evaluation

## Contribution to Odin
This paper validates the multi-module architecture Odin intends to implement — forecasting, anomaly detection, classification, and recommendation — all in a single AI-driven personal finance system. The reported 95% anomaly detection accuracy using Isolation Forest and Autoencoders directly supports Odin's algorithm selection for the anomaly detection module. The 22% savings improvement and 41% recommendation adoption rate provide benchmarks for Odin's budget recommendation and user engagement design. Although the pilot population is not Filipino, the system's use of XAI (SHAP/LIME) and privacy safeguards (differential privacy, federated learning) align with Odin's requirements for user trust and data protection.

**Directly justifies:**
- "Isolation Forest combined with Autoencoders detected anomalous transactions with 95% accuracy on real-world financial data."
- "An ensemble of ARIMA, Prophet, and LSTM achieved a per-user monthly forecasting error of $43 MAE — a benchmark for Odin's spending forecasting module."
- "Expense classification using XGBoost and BERT reached 91% F1-score, supporting the use of transformer-based NLP for transaction categorization."
- "Contextual bandit and reinforcement learning recommendation engines achieved a 41% adoption rate for personalized budget suggestions."
- "Explainable AI (SHAP and LIME) improved user trust by translating anomaly scores into plain-English reasons (e.g., '38% higher grocery spend due to festival')."

**Limits of relevance:**
- Pilot conducted in India; spending patterns, income volatility, and financial infrastructure differ from the Philippines.
- Sample size of 100 users is small; statistical significance and generalizability are limited.
- System assumes banking API integration (PSD2/Open Banking); Odin uses only manual input, which may affect data richness and forecasting accuracy.
- No mobile-specific usability evaluation reported (SUS mentioned but no score provided).

---

# Dive into Time-Series Anomaly Detection: A Decade Review
*by Boniol, P., Liu, Q., Huang, M., Palpanas, T., Paparrizos, J., 2024*

## TL;DR
A process-centric taxonomy organizes a decade of time-series anomaly detection into distance, density, and prediction-based methods, revealing a surge in deep learning approaches after 2016.

## Topics
E.1 — Anomaly Detection in Personal Finance Systems

E.2 — Anomaly Detection Algorithm

D.2 — LSTM as the Spending Forecasting Algorithm

J.1 — System Evaluation

## Contribution to Odin
This survey directly informs Odin’s anomaly detection module by providing a structured taxonomy of candidate algorithms, including Isolation Forest (a leading candidate) and LSTM-based detectors (relevant to the forecasting module). The meta-analysis shows that prediction-based methods (LSTM/autoencoder) dominate recent research, justifying Odin’s choice of LSTM for forecasting while also supporting its use for anomaly detection via prediction error. The detailed review of evaluation metrics—especially the recommendation of VUS-ROC over point‑adjusted metrics—guides how Odin should measure anomaly detection performance in a time‑series context.

**Directly justifies:**
- “Isolation Forest isolates anomalies by random partitioning; anomalies require fewer partitions than normal points, enabling unsupervised detection without labeled training data.”
- “LSTM‑based anomaly detection uses prediction error on normal training data — a higher error indicates an anomaly (Malhotra et al., 2015).”
- “Between 2020 and 2023, prediction‑based methods (including LSTM and autoencoders) represent nearly 50% of new time‑series anomaly detection methods.”
- “Volume Under the Surface (VUS-ROC) is the recommended evaluation measure for time‑series anomaly detection due to its robustness to label noise and detector lag (Paparrizos et al., 2022).”
- “No single anomaly detection method outperforms all others across datasets; model selection (e.g., using simple classification baselines) is essential and can double accuracy (Sylligardos et al., 2023).”

**Limits of relevance:**
- The survey is domain‑agnostic; financial spending anomalies (e.g., budget overages) are not specifically analyzed.
- All findings are based on benchmark datasets from diverse fields (sensors, space, medicine), not Filipino personal finance data.
- Many methods assume clean training data (semi‑supervised) or streaming sensors; Odin’s manual input and cold‑start profiles may violate those assumptions.
- The evaluation metrics discussion does not address human‑centric metrics like usability or user trust.

---

# An Introduction to Machine Learning Methods for Fraud Detection
*by Compagnino, A. A., Maruccia, Y., Cavuoti, S., Riccio, G., Tutone, A., Crupi, R., Pagliaro, A., 2025*

## TL;DR
Machine learning fraud detection models face severe class imbalance and concept drift; even well-tuned Random Forest misses over 60% of frauds in real banking data.

## Topics
D.2 — LSTM as the Spending Forecasting Algorithm

E.1 — Anomaly Detection in Personal Finance Systems

E.2 — Anomaly Detection Algorithm

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

J.1 — System Evaluation

## Contribution to Odin
This review directly informs Odin’s anomaly detection module by benchmarking Isolation Forest as an unsupervised outlier detector that requires no labeled fraud data — critical for Odin’s cold‑start user profiles where no historical “fraud” (i.e., budget overage or unusual spending) labels exist. The paper’s demonstration that even well‑tuned Random Forest achieves only 0.34 recall on real banking data provides a sobering baseline: Odin cannot rely on supervised classifiers alone for behavioral anomaly detection and should prioritize ranking‑based (Recall@K) or cost‑sensitive evaluation over accuracy. The discussion of LSTM for sequential transaction analysis justifies Odin’s forecasting module architecture, while the coverage of concept drift and class imbalance highlights challenges Odin will face as user spending patterns evolve over time and legitimate overspending is rare.

**Directly justifies:**
- “Isolation Forest isolates anomalies without labeled training data by randomly partitioning feature space, making it applicable to cold‑start anomaly detection in personal finance systems.”
- “Supervised classifiers like Random Forest achieve high accuracy (98%) but miss two‑thirds of actual frauds (recall ≤0.36) on imbalanced banking data — accuracy is a misleading metric for rare event detection.”
- “LSTM networks model long‑range temporal dependencies in transaction sequences, outperforming feedforward networks for detecting sequential fraud patterns.”
- “Recall@0.5% — the proportion of frauds caught when reviewing only the top 0.5% of highest‑scoring transactions — provides an operationally relevant evaluation metric when manual review capacity is limited.”
- “Class_weight adjustments do not resolve extreme class imbalance; data‑level techniques (SMOTE) or hybrid unsupervised‑supervised architectures are required.”

**Limits of relevance:**
- The paper focuses on financial fraud (theft, money laundering), not personal budget anomalies (overspending, category deviation) — Odin’s anomaly detection targets behavioral rule violations, not criminal fraud.
- Case study datasets are from European banking transfers; spending patterns and fraud typologies differ from Filipino young professional budgets.
- Models evaluated on transaction‑level fraud flags; Odin requires user‑level behavioral profiling over time, a different unit of analysis.
- No evaluation of explainability methods (SHAP/LIME) on the case study data, though the paper recommends them for regulatory compliance.

---

# Optimized Financial Planning: Integrating Individual and Cooperative Budgeting Models with LLM Recommendations
*by de Zarzà, I., de Curtò, J., Roig, G., Calafate, C. T., 2024*

## TL;DR
LLM-generated budget advice, when used as bounds in linear optimization, produces personalized allocations that align with standard financial planning principles and improve savings over unguided spending.

## Topics
C.1 — Budgeting Strategies and Budget Recommendation

C.2 — Budget Recommendation Algorithm

## Contribution to Odin
This paper directly informs Odin’s budget recommendation module by presenting a linear optimization framework that maximizes savings under income and expense constraints. The use of user-defined preference weights (w_zo) provides a template for personalizing category-level budget allocations, which maps to Odin’s requirement for behavior-driven recommendations. Although Odin does not use LLMs, the optimization model itself — and the concept of using AI-generated bounds to guide allocation — offers a citable justification for constraint-based approaches over static budgeting. The cooperative household extension, while not directly applicable to Odin’s single-user scope, demonstrates how preference weights can reconcile multiple objectives, relevant to any multi-criteria budget recommendation.

**Directly justifies:**
- "Linear optimization with non‑negativity and total‑expense constraints can maximize monthly savings given income and spending category bounds."
- "User‑defined preference weights per expense category allow a budget recommendation algorithm to respect individual financial priorities."
- "LLM‑generated allocation percentages serve as feasible initial solutions for optimization problems in personal finance, reducing the cold‑start burden on new users."
- "Cooperative budgeting models can achieve higher total household savings by pooling incomes and sharing fixed expenses like rent."

**Limits of relevance:**
- Odin does not integrate LLMs; the paper’s core innovation (LLM recommendations as bounds) is not directly implementable without an LLM API.
- All evaluations use synthetic data with US dollar incomes; no validation on Filipino young professionals or Philippine expense categories.
- The cooperative model assumes multiple users sharing finances; Odin is single-user only.
- No comparison to other budget recommendation algorithms (e.g., rule‑based, reinforcement learning) is provided.

---

# Machine Learning for Fraud Detection in Digital Banking: A Systematic Literature Review
*by George, M. Z. H., Alam, M. K., Hasan, M. T., 2023*

## TL;DR
Supervised learning dominates fraud detection, but deep learning (especially LSTM) and hybrid models are rapidly rising, with precision-recall metrics and interpretability frameworks essential for real-world banking deployment.

## Topics
D.2 — LSTM as the Spending Forecasting Algorithm

E.1 — Anomaly Detection in Personal Finance Systems

E.2 — Anomaly Detection Algorithm

J.1 — System Evaluation

## Contribution to Odin
This systematic review directly supports Odin’s anomaly detection module by consolidating evidence that hybrid models (e.g., unsupervised anomaly detection followed by supervised classification) reduce false positives while improving recall — a critical trade-off for a personal budget manager where false alerts erode user trust. The review’s finding that LSTM and RNN architectures excel at modeling sequential transaction data justifies Odin’s selection of LSTM for spending forecasting, even though the paper’s domain is fraud detection rather than forecasting. Finally, the emphasis on PR-AUC over ROC-AUC for imbalanced data provides a concrete evaluation guideline for Odin’s anomaly detection algorithm, where fraudulent (or anomalous) spending is rare relative to normal transactions.

**Directly justifies:**
- “LSTM and RNN architectures capture sequential dependencies in transaction streams, outperforming traditional models on temporal patterns (21 reviewed studies, 7,300+ citations).”
- “Hybrid models combining unsupervised anomaly detection with supervised classification reduce false positive rates while improving recall compared to single-paradigm approaches (Carcillo et al., 2021).”
- “PR-AUC is the preferred evaluation metric for imbalanced financial datasets, as ROC-AUC overstates performance when fraud prevalence is below 1% (Krawczyk, 2016).”
- “Interpretability frameworks such as SHAP and LIME are essential for deploying black-box models in regulated environments, providing auditable explanations for each alert.”
- “Unsupervised anomaly detection (clustering, density-based methods, autoencoders) is essential for identifying novel fraud patterns without labeled data — directly applicable to cold-start anomaly detection in personal finance systems.”

**Limits of relevance:**
- The paper focuses on financial fraud (theft, account takeover), not spending anomalies (budget overages, behavioral deviations). The severity and user reaction differ.
- All reviewed studies use banking transaction data (credit cards, wire transfers), not personal budget entries with category labels. Spending patterns may have different temporal signatures.
- Odin relies on manual transaction input, while fraud detection systems typically integrate directly with bank APIs. Data volume and latency constraints differ.
- The review does not evaluate algorithm performance on Filipino spending behavior or income typology.

---

# A Survey of Machine Learning Methods for Time Series Prediction
*by Hall, T., Rasheed, K., 2025*

## TL;DR
LSTM and LightGBM achieve the highest forecast accuracy across time series tasks, but LightGBM trains 100–1,000× faster, making it the practical default for most applications.

## Topics
D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

## Contribution to Odin
This survey directly informs Odin’s algorithm selection for the spending forecasting module by providing comparative evidence across 79 studies. It shows LSTM as the top-performing deep learning model (58.97% FPA) but also reveals that LightGBM matches LSTM on accuracy while being orders of magnitude faster to train and infer — a critical consideration for Odin as a mobile-first system with computational constraints. The finding that dataset size determines optimal model choice (RNNs better on small data, TBML better on large data) justifies Odin’s need to re-evaluate algorithm choice as user transaction history grows. Additionally, the documented research bias (papers favoring their own model class) warns Odin’s team to prioritize balanced, direct comparisons when reviewing literature.

**Directly justifies:**
- "LSTM achieves the highest forecast accuracy among deep learning models for time series prediction, ranking first in 58.97% of evaluations across 39 comparative studies (Hall & Rasheed, 2025)."
- "LightGBM matches or exceeds LSTM accuracy on large datasets (>200k samples) while training 100–1,000× faster, making it the computationally efficient default for time series forecasting."
- "On small datasets (0–2,173 samples), RNNs like LSTM outperform gradient-boosted trees by 50 percentage points in first-place frequency, supporting LSTM for cold-start user profiles with limited transaction history."
- "Research focus introduces substantial bias: papers emphasizing deep learning show DL models 33.8% higher first-place rates than TBML models in the same comparisons."

**Limits of relevance:**
- Survey covers diverse domains (energy, environment, finance) but not specifically personal budgeting; spending patterns may have different temporal characteristics than retail or stock data.
- All studies use non-Filipino datasets; spending volatility and cultural patterns may differ.
- Computational efficiency claims assume server-grade hardware; mobile inference times may scale differently.
- M5/M6 competitions used retail and financial data with exogenous variables not available in manual entry systems like Odin.

---

# AI-Enabled NLP Framework for Automated Expense Management and Financial Analysis
*by Jayaprakashnarayan, N., Sakthivel, M., Sachidhanandam, P., Devi, N. K., Mughilan, T. S. M., 2026*

## TL;DR
A transformer-based NLP framework for automatic expense tracking from SMS achieves 96.8% entity extraction accuracy and 94.3% merchant precision using on-device multi-task learning.

## Topics
A.2 — Existing Personal Finance and Budget Management Systems

B.1 — Mobile-First Design in Personal Finance Systems

E.1 — Anomaly Detection in Personal Finance Systems

E.2 — Anomaly Detection Algorithm

G.1 — Expense Categorization in Filipino Personal Finance Contexts

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

J.1 — System Evaluation

## Contribution to Odin
This paper directly informs Odin’s expense categorization module by demonstrating that a transformer-based multi-task architecture (MuRIL) achieves 96.8% entity extraction accuracy on real-world SMS data, providing a reproducible baseline for automatic transaction parsing. The ensemble fraud detection framework (Isolation Forest + LSTM autoencoder + rule-based) with 91.7% sensitivity and 3.8% false positive rate justifies Odin’s candidate for anomaly detection, especially the inclusion of Isolation Forest for behavioral deviation. The on-device privacy architecture (quantization, encrypted storage, differential privacy) supports Odin’s design requirement of keeping user data local without banking integration. Finally, the reported System Usability Scale intent and battery/latency benchmarks provide concrete targets for Odin’s mobile-first evaluation under ISO 25010.

**Directly justifies:**
- “A MuRIL-based multi-task transformer achieves 96.8% F1 for extracting transaction entities (amount, date, merchant, account) from mixed-language SMS alerts in a mobile environment.”
- “An ensemble of rule-based screening, Isolation Forest, and LSTM autoencoder detects fraudulent transactions with 91.7% sensitivity and a 3.8% false positive rate on personal transaction streams.”
- “On-device 8-bit quantization reduces model size by 4× while preserving 98.7% of original accuracy, enabling sophisticated NLP on smartphones with 43–127ms latency and 0.9–2.0%/hour battery drain.”
- “Uncertainty quantification (token entropy and class margin) flags low-confidence extractions for human review, preventing automation errors in ambiguous cases.”

**Limits of relevance:**
- Study uses Indian financial messages (UPI, Hindi-English code-mixing); direct transfer to Filipino SMS (Taglish, InstaPay, GCash, Maya) requires validation on local data.
- On-device performance reported on mid-to-high-end Android devices (2–8GB RAM); low-end Philippine devices may experience higher latency or battery drain.
- Cold-start performance (first week of user data) is not evaluated; Odin’s new users may have sparse transaction history.
- Fraud detection ensemble assumes user correction feedback for online learning; Odin’s manual input model may reduce correction frequency.

---

# Detection of Fraudulent Transaction Issues in the Payment Card Industry using Machine Learning: A Comprehensive Survey
*by Kalideen, M. R., 2025*

## TL;DR
A comprehensive survey of machine learning techniques for payment card fraud detection, comparing supervised, unsupervised, deep learning, and ensemble methods while highlighting imbalanced data, interpretability, scalability, and privacy challenges.

## Topics
E.1 — Anomaly Detection in Personal Finance Systems

E.2 — Anomaly Detection Algorithm

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

J.1 — System Evaluation

## Contribution to Odin
This survey directly informs Odin's anomaly detection module by cataloging algorithms suitable for imbalanced financial transaction data, where fraud (or overspending) is rare. The discussion of precision-recall trade-offs guides Odin's alert design: prioritizing recall to catch overspending vs. precision to avoid annoying users with false alarms. Privacy-preserving ML techniques like federated learning justify Odin's manual-input-only approach as a deliberate privacy advantage rather than a limitation. Finally, the emphasis on XAI supports Odin's need for explainable anomaly alerts to build trust among Filipino young professionals.

**Directly justifies:**
- "Fraudulent transactions constitute less than 1% of all payment card transactions, creating a severe class imbalance that requires specialized handling (oversampling, cost-sensitive learning, or ensemble methods)."
- "Ensemble methods like Random Forest outperform single classifiers on imbalanced fraud datasets by reducing overfitting and improving generalization."
- "Explainable AI is necessary for regulatory compliance and user trust in financial fraud detection systems; black-box models are problematic in high-stakes environments."
- "Federated learning enables collaborative model training without sharing raw transaction data, preserving customer privacy while still improving model accuracy."

**Limits of relevance:**
- Paper focuses on payment card fraud (criminal activity), not personal spending anomalies (budget overages) — the behavioral context differs.
- No Philippines-specific data or cultural spending patterns are analyzed.
- Most cited studies use bank-integrated transaction streams; Odin relies on manual user input, which may have different data sparsity and latency characteristics.
- The survey does not address mobile-first implementation constraints (e.g., on-device inference, battery, network latency).

---

# A Comparative Analysis of Budget Forecasting Methods: A Systematic Literature Review Covering the 1983–2024 Period
*by Kara, B., Şengüler, H., 2025*

## TL;DR
No single forecasting method is universally best; context dictates choice, with **43%** of studies on the US.

## Topics
D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

J.1 — System Evaluation

## Contribution to Odin
This systematic review directly supports Odin’s forecasting module by demonstrating that LSTM is suited for short-term (3.3-year horizon), context-sensitive forecasting—exactly Odin’s use case for monthly spending prediction. The review’s finding that no single method is universally best justifies Odin’s design decision to benchmark LSTM against simpler alternatives (ARIMA, regression) rather than assume superiority. The dominance of MAPE, RMSE, and MAE as evaluation metrics (38, 36, 22 studies respectively) provides empirical grounding for Odin’s choice of these same metrics to assess forecasting accuracy. Although the paper examines public sector budgets, the methodological comparisons (LSTM vs. ARIMA vs. XGBoost) and the finding that ML/DL methods excel on short, nonlinear sequences apply directly to personal spending time series.

**Directly justifies:**
- “LSTM’s average forecasting horizon of 3.3 years indicates suitability for short-term spending forecasts, while linear models (AR, MA) are better for long-term projections.”
- “MAPE is the most frequently used accuracy metric in forecasting comparisons (38 of 69 studies), establishing it as the standard for evaluating prediction error in financial time series.”
- “Studies comparing 3–6 methods receive the highest citation impact (average 26 citations), suggesting that focused, multi-model benchmarking yields the most credible evidence.”
- “43% of forecasting research concentrates on the United States, revealing a geographic bias that limits generalizability; Odin’s Philippine context requires local validation.”
- “Deep learning methods (LSTM, ANN) are consistently applied to short-term forecasts, while traditional statistical methods dominate long horizons—a division of labor directly applicable to Odin’s monthly spending predictions.”

**Limits of relevance:**
- Public budget forecasting focuses on macroeconomic aggregates (tax revenue, deficits), not individual-level spending categories or behavioral patterns.
- Geographic concentration on US data (43%) means findings may not replicate in the Philippine young professional context with different income volatility and spending norms.
- LSTM’s data requirements (hundreds of observations) may challenge Odin’s cold-start phase when users have little history.
- The review does not address mobile-specific constraints (compute, battery, offline operation) that affect algorithm selection for Odin.

---

# A Review of ARIMA vs. Machine Learning Approaches for Time Series Forecasting in Data Driven Networks
*by Kontopoulou, V. I., Panagopoulos, A. D., Kakkos, I., Matsopoulos, G. K., 2023*

## TL;DR
Machine learning models generally outperform ARIMA in time series forecasting, but ARIMA remains competitive for small, linear datasets; hybrid models consistently beat both.

## Topics
D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

## Contribution to Odin
This review directly supports Odin's choice of LSTM over ARIMA for the spending forecasting module by systematically aggregating evidence that deep learning models outperform ARIMA on non-linear, real-world time series across multiple domains. The finding that ARIMA can be superior only for small, linear datasets (e.g., cold-start conditions) informs Odin's fallback strategy: use ARIMA for users with minimal transaction history, then transition to LSTM as data accumulates. The review's conclusion that hybrid ARIMA-ML models consistently beat standalone approaches suggests a potential future enhancement for Odin's forecasting module.

**Directly justifies:**
- "Deep learning models (LSTM, GRU) achieve up to 40× lower RMSE than ARIMA on non-linear time series with sufficient training data (ArunKumar et al., 2022, as reviewed by Kontopoulou et al., 2023)."
- "ARIMA outperforms machine learning models only when datasets are small, exhibit limited value ranges, or follow linear relationships — conditions that do not hold for mature user spending histories."
- "Hybrid ARIMA-ML models, where ARIMA captures linear components and ML models residuals, consistently improve forecasting accuracy over standalone ARIMA by margins of 20–35% across multiple domains."
- "The No Free Lunch theorem (Wolpert & Macready, 1997) implies no single forecasting method dominates all time series; algorithm selection must match data characteristics."

**Limits of relevance:**
- The review aggregates findings from diverse domains (finance, weather, health, networks) — no study specifically targets personal spending time series of young professionals.
- Most compared studies use high-frequency data (daily/hourly); Odin operates on monthly manual entries, which may reduce LSTM's advantage.
- The superior ML performance assumes large training datasets; Odin's cold-start users may see better results from ARIMA initially.
- No comparison includes Filipino-specific spending patterns or income volatility.

---

# Comparing deep learning and classical regression approaches for predicting healthcare expenditure and spending: a systematic review
*by Lee, J. T., Yeh, M. H.-S., Li, V. C.-S., Chen, H.-H., Liu, Y.-H., Chen, Y.-C., Wu, D. B.-C., 2026*

## TL;DR
Sequential deep learning models (LSTM, CNN-LSTM) reduce prediction error by 10–20% over regression for longitudinal healthcare cost forecasting, but tree-based methods remain competitive for cross-sectional tabular data.

## Topics
D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

J.1 — System Evaluation

## Contribution to Odin
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

---

# A Constrained, Data-Driven Budgeting Framework Integrating Macro Demand Forecasting and Marketing Response Modeling
*by Lu, Y., Zhou, H., Zhang, Y., 2025*

## TL;DR
Multivariate VAR improves total demand forecast accuracy to **2.85% MAPE**; optimal marketing spend sits below ratio caps due to diminishing returns and revenue uncertainty.

## Topics
C.1 — Budgeting Strategies and Budget Recommendation

C.2 — Budget Recommendation Algorithm

D.1 — Predictive Modeling in Personal Finance Systems

J.1 — System Evaluation

## Contribution to Odin
This paper directly supports Odin’s budget recommendation module by demonstrating a constraint‑based optimization framework that respects hard spending limits (e.g., income‑based caps) while handling diminishing‑returns benefits. The use of Hill saturation functions provides a method to model saturating utility per spending category – directly analogous to how Odin might model that excess budget in a category yields lower marginal value. The paper’s Monte Carlo evaluation of constraint satisfaction under demand uncertainty offers a template for Odin to report confidence levels (e.g., “95% chance you will stay under budget”) rather than deterministic recommendations. Although the domain is enterprise FP&A, the algorithmic structure (forecast → response → constrained optimization) maps cleanly to Odin’s spending forecasting and budget recommendation modules.

**Directly justifies:**
- “Multivariate VAR achieves 2.85% MAPE for aggregate demand forecasting on quarterly PCE data, outperforming seasonal naïve (2.86%) and SARIMAX (2.92%).”
- “Hill saturation models with diminishing returns produce marginal ROI curves that identify saturating spend levels – radio saturates after moderate spend, newspaper provides near‑zero marginal value.”
- “Optimal marketing spend under uncertainty is strictly below the nominal ratio cap (0.97% vs 1.5%) to maintain constraint satisfaction; spending at the cap risks violation in ~40% of scenarios.”
- “A budget planner can trade off expected profit and volatility via a risk‑aversion parameter λ, with higher λ reducing spend (e.g., from 0.97% to 0.90% of revenue).”

**Limits of relevance:**
- Enterprise focus (firm‑level budgeting, marketing mix) not personal finance; the objective (operating profit) differs from Odin’s user‑level adherence.
- Data sources are US‑centric (PCE, Advertising dataset) and not grounded in Filipino spending behavior.
- Marketing response uses a cross‑sectional toy dataset without temporal dynamics (adstock effects), limiting direct transfer to Odin’s user‑level spending patterns.
- No cold‑start evaluation – all models assume historical data, while Odin must handle new users with no transaction history.

---

# Review of Family-Level Short-Term Load Forecasting and Its Application in Household Energy Management System
*by Ma, P., Cui, S., Chen, M., Zhou, S., Wang, K., 2023*

## TL;DR
LSTM and hybrid deep learning models achieve higher accuracy than classical methods for household-level time series forecasting, with hybrid CNN-LSTM capturing both short and long-term dependencies.

## Topics
D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

## Contribution to Odin
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

---

# A Review of Anomaly Identification in Finance Frauds Using Machine Learning Systems
*by Majumder, R., 2025*

## TL;DR
Supervised, semi-supervised, and unsupervised ML methods for financial fraud detection face key challenges: imbalanced datasets and adversarial attacks.

## Topics
E.1 — Anomaly Detection in Personal Finance Systems

E.2 — Anomaly Detection Algorithm

## Contribution to Odin
This paper directly supports Odin's anomaly detection module by surveying ML methods applicable to financial transaction anomalies, including Isolation Forest and Autoencoders. The review justifies the consideration of unsupervised approaches for Odin's cold-start problem, where no labeled fraud data exists for new users. The detailed discussion of imbalanced data challenges and adversarial attack vulnerabilities informs Odin's algorithm selection and the need for adaptive models that can evolve as fraud patterns change.

**Directly justifies:**
- "Unsupervised anomaly detection methods (Isolation Forest, Autoencoders) can identify fraudulent patterns without requiring labeled training data, making them suitable for cold-start user profiles."
- "Imbalanced datasets where fraudulent transactions constitute a tiny fraction of all transactions severely degrade the performance of supervised classifiers."
- "Adversarial attacks can manipulate transaction features to evade detection, requiring fraud models to be adversarially robust or continuously retrained."
- "Graph Neural Networks capture relational patterns in financial networks that traditional attribute-value models miss, relevant for detecting coordinated fraud across multiple transactions."
- "Real-time processing demands in financial fraud detection require scalable ML architectures that balance accuracy and latency."

**Limits of relevance:**
- The paper focuses on financial fraud (credit card, insurance, investment) rather than personal budget anomalies (e.g., overspending vs. behavioral drift) — but methods generalize.
- No empirical performance benchmarks are provided; this is a qualitative review, not a comparative study.
- The reviewed studies use transaction volumes far larger than a single-user personal finance app; Odin's scale differs.
- Adversarial attack discussion assumes sophisticated fraudsters; less relevant for personal budget anomaly detection in a non-banking app.
- Filipino-specific spending patterns or cultural obligations are not addressed.

---

# A Review of Machine Learning and Deep Learning Approaches for Fraud Detection Across Financial and Supply Chain Domains
*by Martínez, O., Sánchez, P., Alcaraz, E., 2025*

## TL;DR
Ensemble methods (XGBoost, LightGBM, Random Forest) consistently outperform deep learning on tabular fraud data, while two-phase semi-supervised frameworks (Isolation Forest + self-training SVM) achieve strong performance with only 1.2% labeled data.

## Topics
D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

E.1 — Anomaly Detection in Personal Finance Systems

E.2 — Anomaly Detection Algorithm

F.2 — Profile Classification Algorithm

J.1 — System Evaluation

## Contribution to Odin
This review directly informs Odin’s algorithm selection across multiple modules. For the anomaly detection module, it provides a direct comparison of Isolation Forest (unsupervised, fast) against supervised alternatives, and shows that a two‑phase unsupervised‑plus‑semi‑supervised framework achieves strong performance with minimal labeled data — critical for Odin’s cold‑start user problem. For spending forecasting, the review benchmarks LSTM against GRU and XGBoost on sequential transaction data, reporting LSTM’s 89‑92% AUC‑ROC but also its higher computational cost, justifying a trade‑off analysis. For user profile classification, the review evaluates Random Forest, XGBoost, and SVM classifiers on high‑dimensional imbalanced data, providing evidence for classifier choice. Finally, the review’s emphasis on evaluating with AUC‑PR (not just accuracy) and using temporal train‑test splits sets a standard for Odin’s system evaluation under ISO 25010.

**Directly justifies:**
- "Ensemble methods (XGBoost, LightGBM, Random Forest) consistently achieve AUC‑ROC of 0.90‑0.93 on imbalanced fraud datasets, outperforming deep neural networks on tabular data."
- "Isolation Forest pre‑filtering reduces data volume by 76% while capturing 94% of anomalies, enabling effective semi‑supervised learning with only 1.2% labeled data — directly applicable to Odin’s cold‑start anomaly detection."
- "LSTM networks achieve 89‑92% AUC‑ROC for sequential transaction fraud detection, but require 3‑5x longer training than XGBoost and GPU acceleration for real‑time inference."
- "Borderline‑SMOTE improves fraud recall by 12‑15% over standard SMOTE on the IEEE‑CIS dataset, making it the preferred oversampling method for extreme class imbalance."

**Limits of relevance:**
- Review focuses on fraud detection (malicious transactions), not spending anomalies (budget overages or unusual but legitimate spending) — Odin’s anomaly detection is behavioral, not criminal.
- Benchmark datasets (European credit card, IEEE‑CIS) are from Western institutions; spending patterns and fraud typologies may differ in the Philippine young professional context.
- LSTM performance reported (89‑92% AUC‑ROC) is on transaction sequences of 10‑50 items; Odin’s forecasting module uses per‑category spending time series, which may have different temporal dependencies.
- Privacy‑preserving techniques (federated learning, differential privacy) are discussed but their accuracy‑privacy trade‑off (5‑15% loss) may be unacceptable for Odin’s resource‑constrained mobile setting.

---

# Harnessing artificial intelligence and machine learning for fraud detection and prevention in Nigeria
*by Odufisan, O. I., Abhulimen, O. V., Ogunti, E. O., 2025*

## TL;DR
AI and ML detect fraud in real time via anomaly detection, behavior analysis, and risk scoring, outperforming static rule-based systems across Nigeria’s banking, e‑commerce, healthcare, and education sectors.

## Topics
E.1 — Anomaly Detection in Personal Finance Systems

E.2 — Anomaly Detection Algorithm

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

## Contribution to Odin
This paper directly validates the use of unsupervised anomaly detection and behavior analysis for identifying unusual financial transactions, which parallels Odin’s need to detect spending anomalies. It benchmarks supervised and deep learning methods (97% detection rate) that Odin could adapt for user profile classification or expense categorization. The discussion of data privacy regulations (Nigeria Data Protection Regulation) and ethical biases in AI models reinforces Odin’s requirement for privacy‑by‑design and transparent logging.

**Directly justifies:**
- “Unsupervised anomaly detection identifies novel fraud patterns without labeled training data, making it applicable to cold‑start user profiles in personal finance systems.”
- “Feed‑forward neural networks achieve 97% detection accuracy for fraudulent transactions, supporting deep learning as a candidate for Odin’s anomaly detection algorithm.”
- “Real‑time analysis of transaction sequences using RNNs can flag unusual spending patterns before financial harm occurs.”
- “Reducing false positives through continuous model retraining is essential for maintaining user trust in automated financial alerts.”

**Limits of relevance:**
- Findings are from Nigerian fraud detection (banking, e‑commerce, healthcare, education), not directly from personal spending behavior or budgeting contexts.
- The 97% detection rate comes from a study on credit card fraud and phishing, not on spending anomalies within a budget management app.
- Nigerian data privacy regulations differ from Philippine law (Data Privacy Act of 2012), though the principle of privacy‑by‑design applies.
- The paper does not evaluate algorithm performance on sparse or irregular transaction data typical of manual‑input personal finance systems.

---

# Artificial Intelligence vs. Efficient Markets: A Critical Reassessment of Predictive Models in the Big Data Era
*by Pagliaro, A., 2025*

## TL;DR
Ensemble methods like Extra Trees and Random Forest consistently outperform single classifiers in stock market prediction, but statistical significance rarely translates into economic value after transaction costs.

## Topics
D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

J.1 — System Evaluation

## Contribution to Odin
This review directly informs Odin's spending forecasting module by providing a critical comparison of LSTM against ensemble methods (Extra Trees, Random Forest) in time-series prediction, including trade-offs in accuracy, computational cost, and economic relevance. The paper's comprehensive evaluation framework — distinguishing statistical significance from real-world value after accounting for transaction costs (or, in Odin's case, manual entry friction and user retention costs) — justifies a rigorous validation protocol for Odin's ISO 25010 and SUS evaluation. The documented risk of backtest overfitting and the need for walk-forward validation are directly applicable to Odin's time-series forecasting and anomaly detection modules, ensuring that reported performance metrics reflect genuine generalizability rather than noise.

**Directly justifies:**
- "Ensemble methods like Extra Trees achieve 86.1% directional accuracy in financial time series, outperforming LSTM (53.2%) for medium-horizon (10-day) predictions, suggesting that Odin's forecasting module should benchmark LSTM against tree-based ensembles."
- "Transaction costs and implementation frictions reduce net performance by 15–40% compared to theoretical metrics — a finding that applies to Odin's manual entry friction and user dropout, requiring evaluation with realistic user-behavior constraints."
- "Standard k-fold cross-validation fails for time-series data due to information leakage; combinatorial purged cross-validation or walk-forward validation is required for valid performance estimation in spending forecasting."
- "60–80% of published predictive anomalies fail replication under multiple testing corrections — Odin's algorithm selection must be validated on out-of-sample data across different user cohorts and time periods."

**Limits of relevance:**
- Domain difference: Stock market prediction (high-frequency, efficient markets) vs. personal spending forecasting (irregular, behavioral, low-frequency) — method transfer requires adaptation.
- No Filipino demographic data: Findings on volatility clustering and market regimes come from U.S. and European markets; spending behavior of Filipino young professionals may differ.
- Review paper, not original empirical study: Specific numerical claims (e.g., 86.1% accuracy) originate from cited primary studies (Pagliaro, 2023); Odin should cite the original when possible.
- No anomaly detection or budget recommendation coverage: The paper focuses on forecasting accuracy, not outlier detection or allocation algorithms.

---

# An Intelligent AI-Based Framework for Automated Personal Financial Management
*by Patel, A., Singh, A., 2026*

## TL;DR
An AI-based personal finance framework automates transaction categorization and budgeting, reducing manual effort while providing predictive spending insights and real-time dashboards.

## Topics
A.2 — Existing Personal Finance and Budget Management Systems

C.1 — Budgeting Strategies and Budget Recommendation

D.1 — Predictive Modeling in Personal Finance Systems

G.1 — Expense Categorization in Filipino Personal Finance Contexts

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

## Contribution to Odin
This paper directly informs Odin's expense categorization module by validating the hybrid rule-based + ML approach for transaction classification — a design decision Odin must make. The adaptive budgeting method described (dynamic budgets derived from historical spending) supports Odin's budget recommendation module, demonstrating that personalization improves budget adherence. Although the system targets Indian digital payments (UPI), the architectural pattern of multi-source aggregation, background processing, and real-time dashboards maps directly to Odin's mobile-first design requirements. The paper's emphasis on security and data privacy (encryption, authentication) reinforces Odin's H.1 topic justification.

**Directly justifies:**
- "Automated transaction categorization using rule-based logic combined with machine learning reduces manual effort and improves accuracy compared to manual entry."
- "Dynamic budget planning based on historical spending patterns improves budget control and reduces overspending."
- "Real-time alerts on approaching budget thresholds help users maintain financial discipline."
- "Predictive analytics using historical expenditure data enables future expense forecasting and enhances financial planning."
- "Multi-source data aggregation into a unified interface reduces the need for users to manage expenses across multiple applications."

**Limits of relevance:**
- Study population is Indian (UPI users), not Filipino; spending patterns and digital payment behaviors may differ.
- No specific algorithm names or performance metrics (e.g., accuracy percentages, precision/recall) are reported — only qualitative claims.
- The system assumes API access to bank/UPI data; Odin relies on manual transaction input only, which may affect automation claims.
- No evaluation on cold-start users (no transaction history) — a critical gap for Odin's new user scenario.

---

# A SYSTEMATIC REVIEW OF DEMAND FORECASTING MODELS FOR RETAIL E-COMMERCE ENHANCING ACCURACY IN INVENTORY AND DELIVERY PLANNING
*by Chowdhury, A. R., Paul, R., Rozony, F. Z., 2025*

## TL;DR
A systematic review of 72 studies finds that deep learning models (LSTM, transformers) outperform traditional statistical methods in volatile e-commerce demand forecasting, with hybrid and context-aware models offering balanced accuracy and interpretability.

## Topics
D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

## Contribution to Odin
This systematic review provides a comprehensive benchmark of LSTM against alternative forecasting models (ARIMA, GRU, random forests, transformers) in volatile, high-frequency transaction environments — directly analogous to Odin's per-category spending forecasting. The finding that LSTM reduces MAPE by up to 20% over statistical methods in promotion-sensitive retail data justifies Odin's selection of LSTM over simpler baselines for the spending forecasting module. The review also highlights that hybrid models (ARIMA+LSTM) offer improved robustness during demand shifts, which could inform Odin's cold-start forecasting strategy or adaptive model retraining. While the domain is retail e-commerce, the time-series characteristics (seasonality, irregular spikes, external influences) mirror personal spending patterns, making the evidence transferable.

**Directly justifies:**
- "LSTM outperforms ARIMA and exponential smoothing by up to 20% in MAPE for volatile, high-frequency demand data (Chowdhury et al., 2025)."
- "Deep learning models (LSTM, GRU, transformers) capture long-term dependencies and nonlinear patterns that statistical models miss, making them suitable for per-category spending forecasting."
- "Hybrid ARIMA-LSTM models achieve lower forecasting errors than standalone models in datasets with structural breaks (e.g., promotions or sudden demand shifts)."
- "External data integration (e.g., sentiment, economic indicators) enhances forecast accuracy beyond historical sales alone, suggesting potential for incorporating calendar events or behavioral signals into spending forecasts."

**Limits of relevance:**
- The review focuses on retail e-commerce (product demand), not personal spending, which may have different volatility drivers (income shocks vs. promotions).
- All studies are from non-Philippine contexts; Filipino spending behavior patterns may differ in seasonality and cultural obligations.
- The review does not address cold-start scenarios with no historical user data.
- Implementation in mobile resource-constrained environments (on-device inference, battery, memory) is not discussed.

---

# Deep learning-based time series forecasting
*by Song, X., Deng, L., Wang, H., Zhang, Y., He, Y., Cao, W., 2025*

## TL;DR
Complex deep learning time series forecasting models often underperform simpler linear models due to overfitting and inability to effectively use sequential order information.

## Topics
D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

## Contribution to Odin
This systematic review directly supports Odin’s spending forecasting module by comparing LSTM against GRU, Transformers, and simple linear models across multiple time series domains. The finding that DLinear (a single linear layer) often beats complex models warns Odin’s team not to default to LSTM without testing simpler baselines. The shuffling experiment provides a diagnostic method to verify that Odin’s chosen model actually uses temporal order – a critical requirement for spending prediction. The observation that complex models overfit on longer lookback windows informs Odin’s design: with sparse manual transaction data, a simpler model may generalize better than an LSTM.

**Directly justifies:**
- "LSTM's gating mechanism mitigates vanishing gradient and captures long-term temporal correlations in sequential data, but simpler linear models can outperform LSTM on certain datasets, requiring empirical validation."
- "Shuffling the input time series and measuring prediction accuracy drop is a valid method to test whether a model truly leverages sequential order – a property essential for spending forecasting."
- "Extending the lookback window from 48 to 192 time steps degrades accuracy for Transformer-based models (Autoformer, ETSformer) due to overfitting and noise, suggesting that for small mobile datasets, shorter windows may be optimal."
- "Patch-based attention (PatchTST) reduces computational complexity while improving long-term accuracy, offering a potential alternative to LSTM for mobile deployment where resources are constrained."

**Limits of relevance:**
- Experiments use energy, traffic, exchange, and illness data – not personal spending transactions from Filipino young professionals.
- All datasets are dense, regularly sampled time series; Odin’s manual input produces sparse, irregular data, which may change model rankings.
- Computational complexity comparisons do not simulate mobile hardware constraints (battery, CPU).
- The review does not evaluate cold-start performance, which is critical for new Odin users with no spending history.

---

# Expense tracker management system using machine learning
*by Thakur, R. S., Jadhav, A., 2025*

## TL;DR
A voting ensemble regressor achieves **78.11% R-squared** and the lowest relative absolute error (0.1765) for expense prediction, outperforming individual models like XGBoost.

## Topics
A.2 — Existing Personal Finance and Budget Management Systems

D.1 — Predictive Modeling in Personal Finance Systems

G.1 — Expense Categorization in Filipino Personal Finance Contexts

## Contribution to Odin
This paper directly informs Odin's spending forecasting module by demonstrating that ensemble methods (specifically voting regressor) achieve higher prediction accuracy (78.11% R²) than individual models like XGBoost on household transaction data. The systematic comparison of eight ML models against five ensemble techniques provides a benchmark for algorithm selection when Odin's forecasting module is implemented. Additionally, the paper's expense categorization approach (predefined + custom categories) and web-based dashboard design offer practical implementation patterns for Odin's expense categorization and user interface modules.

**Directly justifies:**
- "A voting ensemble regressor achieves 78.11% R-squared for expense prediction, outperforming XGBoost (77.89%) and other individual models on a household transaction dataset."
- "Ensemble methods (bagging, boosting, stacking, voting, blending) consistently improve predictive accuracy over single models for personal expense forecasting."
- "Expense categorization into predefined categories (food, transportation, entertainment, utilities) with custom category support is a viable design pattern for personal finance systems."
- "Log transformation of expense amounts (log1p) and TF-IDF vectorization of textual category data are effective preprocessing steps for machine learning-based expense tracking."

**Limits of relevance:**
- Dataset is from Indian households (Indian Rupee); spending patterns and category relevance may differ from Filipino young professionals.
- The web application is not mobile-first; Odin requires mobile-first design, and interface assumptions may not transfer directly.
- No LSTM or time-series specific models were tested; forecasting uses regression on aggregated features, not sequential spending data.
- Prediction task is total expense amount, not per-category spending as in Odin's forecasting module.

---

# Selected Topics in Time Series Forecasting: Statistical Models vs. Machine Learning
*by Tjøstheim, D., 2025*

## TL;DR
Machine learning methods outperform statistical models on high-entropy and intermittent time series (M5 competition), but hybrid statistical‑ML approaches achieve the best overall forecasting accuracy.

## Topics
D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

J.1 — System Evaluation

## Contribution to Odin
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

---

# A Survey of Deep Anomaly Detection in Multivariate Time Series: Taxonomy, Applications, and Directions
*by Wang, F., Jiang, Y., Zhang, R., Wei, A., Xie, J., Pang, X., 2025*

## TL;DR
Deep learning methods for multivariate time series anomaly detection are organized into forecasting, reconstruction, and contrastive approaches, with **46 models** reviewed and a new anomaly type taxonomy proposed.

## Topics
E.1 — Anomaly Detection in Personal Finance Systems

E.2 — Anomaly Detection Algorithm

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

## Contribution to Odin
This survey directly informs Odin’s anomaly detection module by providing a structured taxonomy of anomaly types (point-wise vs. pattern-wise vs. inter-metric) and a comparative analysis of deep learning approaches (forecasting, reconstruction, contrastive). The pros/cons analysis of LSTM-based forecasting methods (e.g., LSTM-NDT, THOC) justifies Odin’s LSTM choice for spending forecasting, while the review of reconstruction methods (VAE, AE, GAN) offers alternatives for behavior-driven anomaly detection if Odin later moves beyond simple rule-based overage alerts. The survey’s discussion of cold-start challenges and the need for unsupervised methods maps directly to Odin’s requirement for anomaly detection without labeled training data.

**Directly justifies:**
- "LSTM-based forecasting methods for multivariate time series anomalies achieve robust detection using non-parametric dynamic thresholding on prediction residuals (LSTM-NDT, 2018)."
- "Reconstruction-based methods using VAEs (OmniAnomaly, InterFusion) explicitly model temporal dependencies among random variables, enabling entity-level anomaly explanation without labeled data."
- "Contrastive learning approaches (DCdetector, SimAD) produce permutation-invariant representations that highlight distributional differences between normal and abnormal data, improving detection robustness."
- "Frequency-domain integration (Dual-TF, CATCH) aligns time and frequency granularities, improving point-level anomaly scoring over time-domain-only methods."
- "Diffusion models (DiffusionAE) smooth out abnormal fragments during reconstruction, yielding higher reconstruction errors for anomalies even under varying training anomaly ratios."

**Limits of relevance:**
- Survey does not evaluate Isolation Forest (Odin’s candidate algorithm) — all reviewed methods are deep learning, which may be computationally heavy for mobile-first Odin.
- No personal finance–specific anomalies or spending patterns are analyzed; the financial domain is mentioned only for fraud detection, not budget adherence.
- All datasets and models are from general MTS domains (aerospace, IoT, cybersecurity) — transferability to Filipino young professional spending data is unvalidated.
- The survey treats unsupervised learning as a strength, but Odin’s anomaly detection may also use rule-based overage alerts (not covered).
- LLM-based methods are nascent and require prompt engineering or fine-tuning; not suitable for Odin’s current resource constraints.

---

# Rare Category Analysis for Complex Data: A Review
*by Zhou, D., He, J., 2023*

## TL;DR
Rare category examples are statistically significant anomalies that form compact clusters, requiring specialized detection, characterization, representation, and interpretation methods beyond standard outlier detection.

## Topics
D.1 — Predictive Modeling in Personal Finance Systems

E.1 — Anomaly Detection in Personal Finance Systems

E.2 — Anomaly Detection Algorithm

F.2 — Profile Classification Algorithm

## Contribution to Odin
This survey directly informs Odin’s anomaly detection module by defining rare category examples as compact, statistically significant anomalies—distinct from uninteresting noise—which justifies a two‑stage approach (filter noise, then detect behavioral outliers). The review’s taxonomy of exploration (no labels) and exploitation (few labels) maps to Odin’s cold‑start problem: new users have no spending history, so an exploration‑style active sampling strategy (e.g., NNDM) could identify suspicious transactions before any labeled fraud data exists. For profile classification, the discussion of multi‑view integration (MUVIR) and local high‑order clustering provides candidate methods for classifying users into behavioral profiles using heterogeneous features (income, spending frequency, category preferences).

**Directly justifies:**
- “Rare category examples are a subset of anomalies that are both statistically significant and compact in feature space; uninteresting anomalies (noise) must be filtered out before flagging spending alerts.”
- “Nearest‑neighbor‑based density change detection (NNDM) guarantees identification of rare categories with O(α/r²) queries, applicable to Odin’s cold‑start anomaly detection where no labeled fraud data exists.”
- “Multi‑view rare category detection (MUVIR) integrates multiple data sources (transaction amount, merchant category, time) by approximating posterior product, improving detection accuracy under weak view dependence.”
- “Local high‑order clustering (HOSPLOC) detects star‑shaped fraud patterns in identity networks; similar structural anomalies may appear in expense categorization conflicts (e.g., a single transaction miscategorized across many users).”

**Limits of relevance:**
- Survey synthesizes existing research; it provides no empirical benchmark comparing algorithm performance on personal finance transaction data.
- All reviewed methods assume access to a labeling oracle (domain expert), which Odin may not have for real‑time anomaly alerts.
- Findings on graph‑based rare patterns (e.g., synthetic ID rings) assume relational data (PII networks) that Odin does not collect (manual input only, no user‑user edges).
- No discussion of mobile‑specific constraints (limited compute, battery, offline operation) that would affect algorithm selection for Odin.

---

# AI Wealth Navigator: An Integrated Platform for Smart Budgeting, Financial Learning, and Personalized Policy Guidance
*by Yadav, A., Prakash, R. S., Iqubal, S. M., Gebremicahea, M. G., 2025*

## TL;DR
An integrated AI platform combining smart budgeting, adaptive financial learning, and policy recommendation achieved 94% receipt scan accuracy and user ratings above 4.6/5 across 50 users.

## Topics
A.2 — Existing Personal Finance and Budget Management Systems

C.1 — Budgeting Strategies and Budget Recommendation

C.2 — Budget Recommendation Algorithm

G.1 — Expense Categorization in Filipino Personal Finance Contexts

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

J.1 — System Evaluation

## Contribution to Odin
This paper directly supports Odin’s expense categorization module by demonstrating that AI‑powered OCR receipt scanning achieves 94% accuracy, justifying a move away from purely manual entry. The budgeting module’s use of LLMs to generate personalized savings alerts and spending insights provides a benchmark for Odin’s budget recommendation algorithm, even though Odin does not use LLMs. The human evaluation with 50 users offers a low‑cost, feasible evaluation template for Odin’s ISO 25010 and SUS testing, particularly the use of 5‑point ratings for perceived relevance and empathy.

**Directly justifies:**
- “OCR‑based receipt scanning achieved 94% accuracy on both digital and physical receipts, reducing manual categorization errors and user entry friction.”
- “Personalized budgeting insights powered by an LLM received a 4.8/5 user rating, indicating that AI‑driven, context‑aware advice improves perceived financial control.”
- “A policy recommendation engine that matches user profiles (income, location, demographics) to government schemes uncovered previously unknown benefits for over 70% of users, demonstrating the value of profile‑driven suggestions.”
- “A 50‑user survey using simple Likert scales (1–5) can effectively measure platform relevance and empathy, offering a lightweight evaluation method for early‑stage personal finance systems.”

**Limits of relevance:**
- The study was conducted in India and Ethiopia, not the Philippines; cultural spending norms and government scheme structures differ.
- Odin relies on manual transaction input, while this paper emphasizes automated receipt scanning — the accuracy claim may not transfer to a fully manual workflow.
- Evaluation used only 50 users and asked about empathy and relevance, not ISO 25010 or SUS; direct comparability to Odin’s evaluation framework is limited.
- The platform uses Gemini LLM, a large model with infrastructure demands (API cost, latency) that Odin’s mobile‑first, offline‑capable design may not support.

---

# Goal Programming Model in Financial Planning of the International Development Bank
*by Aboud, M. S. F., 2025*

## TL;DR
Goal programming balances seven conflicting financial objectives (revenue, expenses, profit, assets, loans, equity, management ratio) with near-zero deviations for an Iraqi development bank.

## Topics
C.1 — Budgeting Strategies and Budget Recommendation

C.2 — Budget Recommendation Algorithm

## Contribution to Odin
This paper directly informs Odin's budget recommendation module by demonstrating that goal programming (a multi-objective optimization method) can balance competing financial targets (revenue, expenses, profit, assets) under resource constraints. While the case study is an Iraqi bank, the algorithmic approach — weighted and preemptive goal programming — maps directly to Odin's problem of allocating a limited budget across spending categories while respecting priority constraints (e.g., savings first, then essentials, then discretionary). The paper provides a quantitative justification for using deviation-minimization over single-objective maximization when user goals conflict (e.g., "maximize savings" vs. "minimize expense tracking burden").

**Directly justifies:**
- "Goal programming achieves near-optimal financial plans under conflicting objectives by minimizing weighted deviations from multiple targets, as demonstrated on a nine-year bank dataset solved with WINQSB."
- "Preemptive goal programming — ranking goals by priority and satisfying higher-priority targets before lower ones — provides a mathematically sound mechanism for budget recommendation when users have non-negotiable savings or expense caps."
- "The weighted method allows differential importance assignment to under-achievement (d⁻) vs. over-achievement (d⁺), enabling Odin to penalize overspending more severely than undersaving."
- "Goal programming handles both upper-bound constraints (e.g., expenses ≤ target) and lower-bound constraints (e.g., revenue ≥ target) simultaneously, matching Odin's budget constraints (spending limits per category) and savings floors."

**Limits of relevance:**
- Domain mismatch: bank-level financial planning (institutional) vs. personal budget management (individual) — principles transfer, but scale and behavioral factors differ.
- Geography: Iraqi financial context; Filipino young professionals' spending patterns and income volatility not addressed.
- Method assumes static target values over time; Odin requires adaptive targets based on user spending history.
- No user interaction or behavioral feedback loop — the model is deterministic and not personalized beyond priority rankings.

---

# The Role of Artificial Intelligence in Enhancing Financial Decision-Making and Administrative Efficiency: A Systematic Review
*by Al-E'mari, S., Sanjalawe, Y., Al-E'mari, A., 2025*

## TL;DR
AI enhances financial decision-making through predictive analytics and fraud detection, cutting legal review time by 99% at JPMorgan Chase.

## Topics
A.2 — Existing Personal Finance and Management Systems

D.1 — Predictive Modeling in Personal Finance Systems

E.1 — Anomaly Detection in Personal Finance Systems

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

J.1 — System Evaluation

## Contribution to Odin
This systematic review provides high-level justification that AI/ML models (predictive analytics, anomaly detection) are effective in financial contexts, supporting Odin's module-level design choices even without algorithm-specific comparisons. The paper's documented efficiency gains from AI automation (e.g., 99% time reduction) can be cited when arguing that Odin's modules should prioritize automation over manual user configuration. The extensive discussion of data privacy challenges (GDPR, PII protection, encryption requirements) directly informs Odin's privacy-by-design requirements for manual transaction data in the Philippine context. The paper's case study analysis framework (KPIs: time savings, error reduction, accuracy) aligns with Odin's planned ISO 25010 evaluation approach.

**Directly justifies:**
- "AI-powered predictive analytics enables forecasting of financial patterns using historical transaction data, supporting per-category spending prediction in personal budget management systems."
- "Machine learning-based anomaly detection systems identify unusual transaction patterns in real-time, outperforming traditional rule-based fraud detection by 35% in financial applications."
- "RPA implementations in administrative functions achieve 50-60% efficiency gains and 40-80% processing time reductions, justifying automation of routine budgeting tasks."
- "Data privacy regulations like GDPR mandate privacy-by-design, anonymization, and encryption for AI systems handling personal financial information — requirements applicable to Philippine personal finance apps."
- "AI-driven financial decision-making requires transparent, explainable models (XAI) to maintain user trust and regulatory compliance, particularly for credit or budget recommendations."

**Limits of relevance:**
- Paper is a systematic review, not a primary study on specific algorithms (LSTM, Isolation Forest) — provides contextual justification but not comparative benchmarks
- Case studies focus on large enterprises (JPMorgan Chase, BlackRock) with resources far beyond Odin's scope
- Geography is Jordan and international; no Filipino-specific financial behavior data
- Administrative efficiency focus (RPA, HR, scheduling) is only partially relevant to Odin's five financial modules
- No evaluation of cold-start performance for new users with minimal transaction history — a core Odin constraint

---

# Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking
*by Alenazi, M., Sas, C., 2023*

## TL;DR
Only 26 of 45 top-rated budgeting apps (58%) support envelope-based multiple budgets; one third offer only expense tracking with no budgeting functionality.

## Topics
A.2 — Existing Personal Finance and Budget Management Systems

C.1 — Budgeting Strategies and Budget Recommendation

G.1 — Expense Categorization in Filipino Personal Finance Contexts

## Contribution to Odin
This paper directly justifies Odin’s design decision to prioritize envelope-based multiple budgets over simple tracking or single-budget approaches. The finding that only 58% of top-rated apps support money envelopes reveals a market gap that Odin can fill by implementing theoretically grounded budgeting. The paper’s analysis of inconsistent account terminology (income vs expense) informs Odin’s need for clear distinction between available funds and spending categories. Additionally, the documented lack of transfer transaction support (or allowing transfers from empty accounts) warns Odin’s design team to implement balance-checked transfers to preserve budget integrity.

**Directly justifies:**
- “Only 26 of 45 top-rated budgeting apps (58%) implement envelope-based multiple budgets; one third provide no budgeting functionality beyond expense tracking.”
- “Most budgeting apps fail to distinguish between income accounts (money-in) and expense accounts (money-out), leading to cognitive confusion and overspending risk.”
- “Four of the reviewed apps store transactions directly on the home screen without linking to any account container, preventing proper budget tracking.”
- “Thirty-five apps support transfer transactions, but 33 allow transfers even when the source account has insufficient funds — a design flaw Odin must avoid.”

**Limits of relevance:**
- Study population and app stores are UK-based; Filipino app usage patterns and financial behaviors may differ.
- The review excluded apps requiring bank account integration; Odin is manual-only, so this exclusion does not affect applicability.
- No user study was conducted; findings are based solely on expert functionality review, not actual usage data or retention metrics.

---

# Reimagining social protection: financialised futures among ageing migrant domestic workers in Asia
*by Amrith, M., 2026*

## TL;DR
Filipino migrant domestic workers enrol in financial literacy courses to shift from a family-first breadwinner mindset towards self-responsibility and personal savings for retirement.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

C.1 — Budgeting Strategies and Budget Recommendation

## Contribution to Odin
This paper informs Odin’s understanding of Filipino financial behavior by documenting how deeply ingrained family obligations override personal savings goals — a key constraint that budget recommendation UI must address. The finding that financial literacy courses teach migrants to set boundaries on family money requests directly supports Odin’s design principle of helping users prioritise personal savings without guilt. Although the study focuses on older migrant workers, the “breadwinner” mindset and cultural obligations to kin are equally relevant to Filipino young professionals who support parents or siblings.

**Directly justifies:**
- “Only 5% of overseas Filipinos in Singapore contribute to the state pension system, leaving most without formal retirement savings.”
- “Filipino migrant workers describe a ‘breadwinner mentality’ — the belief that all earnings must be sent to family — which leads to decades of work without accumulating personal savings.”
- “Financial literacy courses explicitly teach migrants how to say ‘no’ to family money requests, reframing self-savings as legitimate rather than selfish.”
- “Migrant women who shift to a ‘financially-smart’ identity report greater confidence in refusing family demands and investing in their own future.”

**Limits of relevance:**
- Study population is ageing migrant domestic workers (45–65), not young professionals (20–40) — but the cultural tension between family obligations and self-savings likely generalises.
- Qualitative ethnography provides behavioral insights, not algorithmic benchmarks or quantitative performance metrics for budgeting systems.
- Context is Singapore/Hong Kong labour migration with no permanent residency; Odin users are local Filipinos with different employment structures.
- Focus is on retirement social protection, not day-to-day personal budget management within a mobile app.

---

# Understanding Millennials’ Financial Behavior: The Role of Fintech Adoption, Financial Literacy, and the Mediating Effect of Financial Attitudes in a Crisis-Affected Emerging Economy
*by Aoun, D., Rahal, R., Sfeir, L., Al Maalouf, N. J., 2026*

## TL;DR
FinTech adoption and financial literacy positively affect millennials’ financial behavior, with financial attitudes mediating the literacy‑behavior link in Lebanon’s crisis context.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

A.2 — Existing Personal Finance and Budget Management Systems

C.1 — Budgeting Strategies and Budget Recommendation

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

I.1 — User Retention and Engagement in Personal Finance Systems

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

## Contribution to Odin
This paper justifies Odin’s inclusion of financial attitude as a mediating variable in user profiling, demonstrating that knowledge alone does not directly predict behavior without attitudinal reinforcement. The finding that FinTech adoption has a positive but smaller effect (β=0.144) than attitude (β=0.414) informs Odin’s design priority: fostering positive attitudes through intuitive UX and trust‑building features may drive behavior change more effectively than just providing financial literacy content. For Odin’s budget recommendation module, the study suggests that user attitudes toward saving and risk should be incorporated as input features to improve adherence, especially in volatile economic contexts.

**Directly justifies:**
- “Financial attitude (β=0.414) is a stronger predictor of financial behavior than financial literacy (β=0.337) or FinTech adoption (β=0.144) among millennials in a crisis economy.”  
- “Financial attitude fully mediates the relationship between financial literacy and financial behavior, implying that literacy interventions alone are insufficient without attitudinal change.”  
- “Higher FinTech adoption improves financial management behavior (p<0.001), supporting the value of digital budgeting tools.”  
- “Institutional trust erosion amplifies the role of subjective attitudes over objective knowledge in shaping financial behavior.”

**Limits of relevance:**
- Study conducted in Lebanon, a different emerging market; Filipino cultural and economic context may differ (e.g., remittance culture, different crisis drivers).  
- Self‑reported financial behavior may not reflect actual transactional behavior; Odin uses manual input but could still face same bias.  
- No objective financial literacy measure; relies on perceived literacy.  
- Cross‑sectional design; cannot infer causality or track behavior change over time.

---

# Examining Mobile-First Database Solutions for East African Markets in Detail
*by Arinze, E. D., 2024*

## TL;DR
Mobile-first database solutions with offline sync, real-time updates, and strong encryption are critical for reliable app performance in East Africa's low-bandwidth, high-mobile-penetration markets.

## Topics
B.1 — Mobile-First Design in Personal Finance Systems

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

I.1 — User Retention and Engagement in Personal Finance Systems

## Contribution to Odin
This paper directly supports Odin’s mobile‑first architecture by establishing that offline data synchronization and local storage are non‑negotiable for apps targeting users with intermittent internet – a condition common among Filipino young professionals. The security requirements (TLS, at‑rest encryption, RBAC) inform Odin’s privacy‑by‑design implementation, which must comply with Philippine data privacy law. The finding that seamless mobile experiences increase user retention justifies Odin’s decision to prioritize manual input simplicity over gamification, as retention in financial apps hinges on perceived reliability and data safety.

**Directly justifies:**
- “Mobile-first databases must include offline local storage and caching to maintain usability in regions with unreliable or low‑bandwidth networks.”
- “End‑to‑end encryption (E2EE) and TLS for data in transit are baseline security requirements for any mobile financial app handling user spending data.”
- “Real‑time data synchronization across devices improves user trust and engagement, but requires conflict resolution strategies to prevent data corruption.”
- “Policy and regulatory support (e.g., data protection laws, infrastructure investment) are necessary for mobile‑first solutions to achieve digital inclusion – a lesson relevant to deploying Odin at scale in the Philippines.”

**Limits of relevance:**
- The paper focuses on East African markets, not the Philippines; however, Metro Manila faces similar mobile penetration and connectivity variability.
- No empirical evaluation of user retention or specific ML modules; relevance is architectural and security‑oriented, not algorithmic.
- The paper does not address personal finance systems specifically; the findings are cross‑domain (healthcare, agriculture, finance).

---

# AI-Powered Personalization in Digital Banking: A Review of Customer Behavior Analytics and Engagement
*by Ashrafuzzaman, M., Parveen, R., Sumiya, M. A., Rahman, A., 2025*

## TL;DR
Behavior analytics and predictive models power AI personalization in digital banking, boosting engagement and retention, but measurement inconsistencies and privacy gaps remain unresolved.

## Topics
A.2 — Existing Personal Finance and Budget Management Systems

B.1 — Mobile-First Design in Personal Finance Systems

D.1 — Predictive Modeling in Personal Finance Systems

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

I.1 — User Retention and Engagement in Personal Finance Systems

## Contribution to Odin
This review directly informs Odin's user profiling and behavioral classification modules by demonstrating that behavior analytics (transaction frequency, login patterns, spending sequences) are the preferred segmentation method over static demographics — a finding that justifies Odin's behavior-driven profile updates. The paper's documentation of predictive analytics for churn and product recommendation validates Odin's spending forecasting module's use of sequential data, while its emphasis on transparency, consent dashboards, and explainable AI (XAI) provides concrete design requirements for Odin's privacy-by-design approach under Philippine data privacy law. Although focused on banking rather than personal budget management, the engagement-retention link (68% retention for personalized services vs. 49% for non-personalized) directly supports Odin's value-driven retention strategy over gamification.

**Directly justifies:**
- "Behavior-based segmentation using unsupervised learning (e.g., K-means clustering) replaces demographic profiling in digital finance, enabling real-time targeting based on transaction frequency and spending patterns."
- "Predictive analytics models that process sequential behavioral data (login frequency, bill payment timing) achieve higher engagement lift than reactive recommendation systems, justifying LSTM's suitability for spending forecasting."
- "Customers provided with AI-driven personalized financial recommendations show 19-percentage-point higher 90-day retention compared to non-personalized controls (source: comparable retention gap cited across multiple studies in the review)."
- "Transparency mechanisms — consent dashboards, personalized privacy notices, and explainable AI (XAI) prompts — are necessary for user trust in AI personalization systems processing personal financial data."
- "Emerging market deployments of AI personalization rely on alternative data (utility payments, mobile money activity, airtime top-ups) when traditional credit histories are unavailable — directly applicable to thin-file Filipino users."

**Limits of relevance:**
- Study population is global banking customers, not specifically Filipino young professionals; cultural spending norms and income volatility patterns may differ.
- The review synthesizes digital banking (full-service bank accounts, credit products), not pure personal budget management apps like Odin (no banking integration, manual input only).
- All cited algorithms (ML, NLP, recommender systems) are described at conceptual level; no empirical benchmarks or comparative performance metrics (e.g., LSTM vs. GRU) are provided.
- Ethical and legal frameworks discussed (GDPR, CCPA) differ from Philippine Data Privacy Act provisions; specific compliance mappings require separate validation.
- Longitudinal effectiveness evidence is identified as a research gap — the review itself notes that most personalization studies lack time-series evaluation.

---

# Impact of financial literacy, mental budgeting and self control on financial wellbeing: Mediating impact of investment decision making
*by Bai, R., 2023*

## TL;DR
Higher financial literacy, mental budgeting, and self-control each improve subjective financial wellbeing among Chinese university students; investment decisions partially mediate these relationships.

## Topics
C.1 — Budgeting Strategies and Budget Recommendation

## Contribution to Odin
This paper provides behavioral evidence that mental budgeting — the cognitive practice of categorizing and tracking expenses — is positively associated with financial wellbeing, independent of actual income or wealth. For Odin’s budget recommendation module, this justifies designing features that explicitly support mental budgeting behaviors, such as clear per-category spending limits and real-time tracking. The finding that self-control also predicts financial wellbeing reinforces Odin’s design priority of reducing impulsive spending friction (e.g., alerts before overspending) rather than relying solely on user discipline. Although the study uses Chinese student data and no algorithmic intervention, its psychological framework validates the importance of budgeting strategies as a core module in a PBMS.

**Directly justifies:**
- "Mental budgeting has a significant direct positive effect on subjective financial wellbeing (β = 0.102, p < 0.001) after controlling for financial literacy and self-control."
- "Individuals who practice mental budgeting — mentally categorizing and tracking expenses — exhibit higher financial wellbeing and better investment decision-making behavior."
- "Self-control directly predicts financial wellbeing (β = 0.182, p < 0.001), supporting system designs that help users resist impulsive spending."
- "Investment decision making partially mediates the effect of mental budgeting on financial wellbeing, indicating that budgeting habits translate into better long-term financial outcomes."

**Limits of relevance:**
- Sample comprises Chinese university students, not Filipino young professionals; income patterns and cultural spending norms may differ.
- No algorithm or ML method is tested; the study is purely observational and cross-sectional.
- Financial wellbeing is self-reported and subjective, not measured via objective spending or saving data.
- The mediation effect size is small (indirect β 0.016–0.019), suggesting other unmeasured factors dominate.

---

# Financial Education in the Age of Artificial Intelligence: A Systematic Review with Text Mining and Natural Language Processing
*by Balcazar-Paiva, E. S., Haro-Sarango, A. F., Villanueva-Calderón, J. A., 2026*

## TL;DR
A systematic review of 50 studies (2020–2025) finds AI in financial education is technically framed with slight optimism but lacks longitudinal evidence and standardized metrics for sustained behavioral change.

## Topics
A.2 — Existing Personal Finance and Budget Management Systems

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

## Contribution to Odin
This systematic review contextualizes the broader AI-in-finance landscape, helping Odin's RRL justify the selection of specific algorithms by showing that the field lacks standardized evaluation metrics and longitudinal evidence – a limitation Odin's evaluation plan (ISO 25010 + SUS) directly addresses. The review's finding that ethics clusters (privacy, bias, fairness) are structural conditions, not add-ons, supports Odin's design decision to prioritize data privacy via manual input only (no banking integration). Although focused on financial education rather than budget management, the paper's discussion of AI-mediated decision-making and user trust (e.g., robo-advisor adoption transparency) informs Odin's approach to user-facing explanations of anomaly detection and budget recommendations.

**Directly justifies:**
- "Systematic reviews of AI in financial domains confirm a persistent lack of standardized metrics and longitudinal designs, limiting claims about sustained behavioral impact."
- "Privacy, fairness, and algorithmic bias are not peripheral ethical concerns but structural conditions for responsible AI deployment in personal finance systems."
- "Transparency is a decisive determinant of user adoption for automated financial tools (robo-advisors), reinforcing Odin's need for explainable anomaly and budget recommendation outputs."
- "The literature's discursive neutral-to-positive framing of AI capabilities does not translate into proven long-term effectiveness – a gap that Odin's module-specific algorithm benchmarking can address."

**Limits of relevance:**
- Paper focuses on financial *education*, not personal budget *management* systems; direct analogies to spending forecasting or anomaly detection are indirect.
- All studies reviewed are international (global) with no Philippine-specific data; cultural spending behaviors and digital readiness differ.
- Sentiment analysis on abstracts captures framing, not causal effectiveness; cannot be cited as evidence that any algorithm works in practice.
- Review excludes grey literature and non-peer-reviewed sources; may miss applied industry insights relevant to PBMS design.

---

# Psychology and Development: Applications from Cognitive and Social Psychology
*by Breza, E., Kaur, S., 2026*

## TL;DR
Poverty amplifies psychological constraints (self-control, cognition, mental health, social norms) through missing markets and high stakes, creating persistent behavioral distortions and justifying policy interventions as market corrections.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

C.1 — Budgeting Strategies and Budget Recommendation

D.1 — Predictive Modeling in Personal Finance Systems

E.1 — Anomaly Detection in Personal Finance Systems

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

G.1 — Expense Categorization in Filipino Personal Finance Contexts

I.1 — User Retention and Engagement in Personal Finance Systems

## Contribution to Odin
This review directly justifies Odin’s emphasis on psychological constraints across multiple modules. The finding that soft commitments (lockboxes, labeled envelopes) often outperform hard financial penalties informs Odin’s budget recommendation and anomaly detection design — users are more likely to engage with low‑friction behavioral aids. The documentation of planning fallacy and retrieval failures (Augenblick et al. 2023) supports Odin’s forecasting module as a cognitive aid that helps users recall irregular expenses. Evidence that cash‑on‑hand improves cognitive performance (Kaur et al. 2025) suggests Odin’s spending forecasting can reduce financial worries by providing predictability, indirectly improving user decision quality. The review’s framework that missing markets for behavioral aids justify intervention — not paternalism — provides a normative foundation for Odin’s proactive nudges (reminders, spending alerts).

**Directly justifies:**
- “Soft commitment devices (labeled lockboxes, appointment reminders) are as effective as hard financial penalties and avoid welfare losses from forfeited deposits (Dupas & Robinson, 2013; Derksen et al., 2025).”
- “Planning fallacy and retrieval failures cause households to underestimate future irregular expenses by 43%, leading to overspending and reduced savings — correctable by prompting category‑based recall (Augenblick et al., 2023).”
- “Cash‑on‑hand increases worker productivity by 7% by reducing attentional mistakes, not through income effects; this cognitive channel applies to financial decision‑making in budgeting apps (Kaur et al., 2025).”
- “Social norms against below‑market wages create wage floors: workers reject 10% wage cuts when observable but accept them in private, showing that perceived social approval shapes labor supply (Breza et al., 2025b).”
- “Cognitive behavioral therapy improves economic outcomes by changing self‑efficacy and reducing overoptimistic beliefs, not only by alleviating clinical depression (Bhat et al., 2022).”

**Limits of relevance:**
- The review synthesizes global evidence; specific spending patterns, income volatility, and social norms in the Philippines may differ from the cited contexts (India, Kenya, Ghana, etc.).
- Most cited studies involve formal savings accounts or bank integration; Odin relies entirely on manual transaction input, which may weaken or strengthen some psychological effects (e.g., mental accounting via envelopes works well manually).
- The review does not test any algorithm directly; it provides behavioral mechanisms, not ready‑to‑implement ML models for forecasting or classification.

---

# Artificial Intelligence Powered Personal Finance Management System
*by Chahar, P., Vishwakarma, Y., Mishra, R., Paliwal, G., 2026*

## TL;DR
AI-powered personal finance assistant with machine learning and NLP achieved 4.4/5 user satisfaction, 4.5/5 ease of use, and 4.2/5 transaction categorization accuracy.

## Topics
A.2 — Existing Personal Finance and Budget Management Systems

C.1 — Budgeting Strategies and Budget Recommendation

C.2 — Budget Recommendation Algorithm

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

E.1 — Anomaly Detection in Personal Finance Systems

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

G.1 — Expense Categorization in Filipino Personal Finance Contexts

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

J.1 — System Evaluation

## Contribution to Odin
This paper provides a modular AI system design (classification, forecasting, recommendation, NLP) that directly parallels Odin’s five‑module architecture, offering a validated precedent for combining multiple ML techniques in a personal finance app. The user satisfaction results (4.4/5 overall, 4.5/5 ease of use) establish benchmark targets for Odin’s ISO/IEC 25010 and SUS evaluations. The explicit discussion of challenges with irregular income and variable expenses reinforces Odin’s need to handle income volatility common among Filipino young professionals. The paper’s security and privacy layer (encryption, GDPR) justifies Odin’s data protection requirements even without banking integration.

**Directly justifies:**
- “Automated expense classification using Random Forest, SVM, and LSTM achieved user‑rated accuracy of 4.2/5 in a prototype personal finance system.”
- “Predictive analytics for spending forecasting are feasible with time series models (ARIMA, LSTM), but accuracy degrades for users with irregular income patterns.”
- “User satisfaction surveys in AI‑powered PFMS reported ease of use (4.5/5) and goal‑setting functionality (4.3/5) as strong drivers of engagement.”
- “End‑to‑end encryption and role‑based access control are essential security measures for user trust in AI‑driven personal finance tools.”
- “Supervised ML models for expense categorization require large labeled datasets, which may not be available during cold‑start for new users.”

**Limits of relevance:**
- Study population is Indian university‑affiliated, not Filipino young professionals; spending behavior and income typology may differ.
- Evaluation uses subjective satisfaction ratings (4‑point scale) rather than objective metrics like MAE or F1‑score for algorithm performance.
- No comparison against baseline (non‑AI) tools; claims of improvement over static budgeting are unsupported by comparative data.
- Prototype relies on bank API integration; Odin’s manual‑only input model may alter classification and forecasting dynamics.
- Sample size and demographic breakdown of survey participants not reported, limiting generalizability.

---

# What UK Fintechs Can Learn From African Mobile Money Models
*by Chepkutwo, D., 2025*

## TL;DR
African mobile money models succeed through frugal design, agent networks, community trust, and offline resilience — lessons UK fintechs can adopt to serve excluded users.

## Topics
A.2 — Existing Personal Finance and Budget Management Systems

B.1 — Mobile-First Design in Personal Finance Systems

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

I.1 — User Retention and Engagement in Personal Finance Systems

## Contribution to Odin
This paper justifies Odin’s mobile-first design by emphasizing that simplicity and reliability (not feature bloat) drive adoption among financially anxious users — directly applicable to Filipino young professionals. Its analysis of agent networks as trust infrastructure supports Odin's potential to integrate community-based onboarding or support channels without banking APIs. The finding that frugal, offline-resilient design improves retention among low-income and digitally excluded populations counters the assumption that “more features = better engagement,” guiding Odin’s UX prioritization.

**Directly justifies:**
- “Frugal fintech design focusing on 4–5 core functions (send, receive, pay bills, save, loan) achieves higher adoption among low-literacy and financially anxious users than feature-rich apps.”
- “Agent networks serve as human trust anchors, resolving disputes and onboarding users where digital-only support fails — a model applicable to cash-based or manual-entry systems like Odin.”
- “USSD and SMS fallback channels increase retention in populations with unreliable internet or older devices, reducing digital exclusion.”
- “Tiered KYC (starting with just a phone number) enables rapid onboarding for previously unbanked users, a principle that can inform Odin’s minimal-data profile creation.”

**Limits of relevance:**
- The paper is a conceptual essay, not a peer-reviewed empirical study; its claims lack quantitative validation.
- African mobile money models rely on telco-led infrastructure (SIM-based wallets, airtime integration) that differs from Odin’s manual-input, no-banking-integration scope.
- Filipino young professionals are not directly studied; cultural and economic differences (e.g., prevalence of informal community savings groups) may moderate applicability.
- No specific algorithm or forecasting method is discussed, limiting direct relevance to Odin’s ML modules (LSTM, Isolation Forest).

---

# A qualitative investigation of financial decision-making and enabling factors among ethnic minority young adults in Hong Kong
*by Cho, E. Y.-N., 2024*

## TL;DR
Ethnic minority young adults in Hong Kong save roughly one-third of income, use digital budgeting tools, and struggle with self-control and high living costs.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

A.2 — Existing Personal Finance and Budget Management Systems

C.1 — Budgeting Strategies and Budget Recommendation

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

G.1 — Expense Categorization in Filipino Personal Finance Contexts

I.1 — User Retention and Engagement in Personal Finance Systems

## Contribution to Odin
This paper directly informs Odin's understanding of Filipino young adults' financial behavior, even though the study was conducted in Hong Kong. The finding that many participants saved one-third of income and prioritized food and transportation aligns with Philippine FIES data patterns. The identified barriers to budgeting — time consumption, stress, self-control struggles — justify Odin's design emphasis on reducing entry friction and providing automated tracking. The paper's documentation of digital tool usage (budgeting apps) and parental monitoring strategies supports Odin's assumption that Filipino young professionals may value both automation and social accountability features.

**Directly justifies:**
- "Ethnic minority young adults (including Filipinos) in Hong Kong save approximately 30% of monthly income, with food and transportation consuming the largest budget share."
- "Budgeting is perceived as tedious, time-consuming, and stress-inducing, leading many to abandon tracking — a friction point Odin's automated categorization must address."
- "Digital budgeting apps (Mobills, Spendee, Excel) are actively used and accepted by young adults, supporting Odin's mobile-first approach."
- "Informal borrowing from family is common and not always repaid, suggesting that debt management features in Odin should distinguish informal loans from formal credit."
- "Fraud victimization occurs despite protective tactics, highlighting the need for in-app scam alerts and financial literacy content within Odin."

**Limits of relevance:**
- Study population is ethnic minority young adults in Hong Kong, not specifically Filipino young professionals in Metro Manila — cultural context and financial systems differ.
- Findings are qualitative and descriptive, not quantitative or algorithm-focused; cannot justify algorithm selection directly, only user behavior assumptions.
- Participants were relatively well-educated (half with bachelor's degrees) and English-proficient, which may not represent lower-literacy Filipino users.
- Hong Kong's financial infrastructure (Octopus card, MPF, high living costs) differs from the Philippines; spending ratios may not transfer directly.

---

# Robo-Advice: Transforming Households into Rational Economic Agents
*by D'Acunto, F., Rossi, A. G., 2023*

## TL;DR
Robo-advice transforms biased household decision-makers into rational economic agents by providing fully informed benchmarks, correcting distorted beliefs, and minimizing transaction costs across consumption, saving, and debt management.

## Topics
A.2 — Existing Personal Finance and Budget Management Systems

C.1 — Budgeting Strategies and Budget Recommendation

C.2 — Budget Recommendation Algorithm

E.1 — Anomaly Detection in Personal Finance Systems

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

I.1 — User Retention and Engagement in Personal Finance Systems

## Contribution to Odin
This review directly justifies Odin's robo-advice-like architecture by synthesizing evidence that automated, data-driven financial guidance improves spending, saving, and debt management outcomes across diverse populations. The paper's documentation of income aggregators' effects on spending awareness informs Odin's expense categorization and anomaly detection modules, while goal-setting findings validate budget recommendation as a retention mechanism. The discussion of algorithmic aversion versus appreciation highlights design trade-offs for Odin's user onboarding and trust-building features, particularly relevant given Filipino young professionals' potential unfamiliarity with automated financial tools.

**Directly justifies:**
- "Income aggregators that display a household's complete balance sheet reduce nondurable spending and overdraft fees by making financial red flags salient (Olafsson & Pagel, 2018; Carlin, Olafsson & Pagel, 2023)."
- "Goal setting through robo-advisors increases monthly savings by €60 for users earning €1,200, with stronger effects for less educated, lower-income, and impatient individuals (Gargano & Rossi, 2020)."
- "Overspending alerts that compare current category spending to recent personal history reduce daily spending by 5%, with cumulative effects that do not fully revert (Lee, 2019)."
- "Providing information about peers' spending causes overspenders to cut consumption substantially more than underspenders increase it, an asymmetric effect aligned with policymakers' aims (D'Acunto, Rossi & Weber, 2019)."
- "Algorithmic aversion varies across age and demographic groups; households without forecasting experience show algorithmic appreciation, preferring algorithms to humans (Logg, Minson & Moore, 2019; Rossi & Utkus, 2020a)."

**Limits of relevance:**
- This is a conceptual review, not an empirical study with algorithm-specific performance metrics (no LSTM, Isolation Forest, or comparative model benchmarks).
- All studies cited originate from Western or developed Asian countries (US, Canada, Iceland, Italy, France, Singapore, India) — not the Philippine context.
- Robo-advisors studied often integrate with bank accounts via open banking APIs; Odin relies on manual transaction input, which may alter engagement dynamics and data completeness.
- The review does not address cold-start problems for new users with no transaction history, a core Odin design constraint.

---

# A Comprehensive Review of Machine Learning Techniques for Intelligent Personal Finance Management Systems
*by D'Souza, M., Bhegade, P., Bhalekar, P., Bhavsar, Y., 2026*

## TL;DR
This review systematically compares ML techniques for budgeting, forecasting, anomaly detection, and group finance in PFMS, highlighting LSTM for temporal dependencies and Isolation Forest for unsupervised anomaly detection.

## Topics
A.2 — Existing Personal Finance and Budget Management Systems

C.1 — Budgeting Strategies and Budget Recommendation

C.2 — Budget Recommendation Algorithm

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

E.1 — Anomaly Detection in Personal Finance Systems

E.2 — Anomaly Detection Algorithm

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

## Contribution to Odin
This review directly informs Odin's algorithm selection across multiple modules by providing comparative trade-offs (interpretability vs. adaptability, data requirements vs. scalability). For the forecasting module, it justifies LSTM over simpler statistical models by demonstrating LSTM's ability to capture long-term non-linear dependencies in spending sequences — a key requirement for Filipino young professionals with irregular income patterns. For anomaly detection, the review establishes Isolation Forest as the preferred unsupervised method for PFMS because it scales efficiently, requires no labeled data, and isolates behavioral deviations rather than fraud — exactly matching Odin's need to detect unusual spending without historical fraud labels. The review also highlights the necessity of explainable AI layers (e.g., post-hoc attribution) when deploying complex models, which informs Odin's design priority of user trust.

**Directly justifies:**
- "LSTM networks capture long-range temporal dependencies in expenditure sequences through gated memory mechanisms, but require substantial historical data and offer low inherent interpretability."
- "Isolation Forest isolates anomalous spending observations via random partitioning with O(n log n) complexity, operating without labeled data by assuming anomalies are rare and structurally distinct."
- "Hybrid ARIMA-LSTM ensembles combine linear trend modeling (ARIMA) with non-linear residual learning (LSTM) to improve forecast robustness across varying financial conditions."
- "Unsupervised anomaly detection methods dominate PFMS because labeled personal spending data defining 'inefficient' behavior is practically unavailable for individual users."
- "Rule-based budgeting and anomaly detection are transparent and low-cost but fail to adapt to seasonal or multi-feature spending patterns, leading to high false-positive rates during holidays or one-time purchases."

**Limits of relevance:**
- Review focuses on general PFMS techniques; no Filipino-specific spending behavior or income typology data is presented.
- Comparative analysis is qualitative, not benchmarked on real-world Philippine financial datasets.
- Group expense management (bill splitting, settlement optimization) is not within Odin's current scope (single-user system).
- Computational trade-offs cited (e.g., LSTM resource intensity) assume server-grade or mobile constraints; Odin's mobile-first deployment may require additional optimization not discussed.

---

# FINANCIAL LITERACY AND DIGITAL SAVINGS BEHAVIOR OF GEN Z IN THE FINTECH ERA: A SYSTEMATIC LITERATURE REVIEW
*by Dewi, A. K., 2025*

## TL;DR
Financial literacy and fintech synergistically shape Gen Z's saving behavior; gamification and auto-reminders build discipline and reduce high-cost loan reliance.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

C.1 — Budgeting Strategies and Budget Recommendation

I.1 — User Retention and Engagement in Personal Finance Systems

## Contribution to Odin
This paper supports Odin's budget recommendation module by showing that fintech features (auto-debit, gamification, real-time transparency) directly improve saving discipline — a behavior analogous to budget adherence. The finding that financial literacy and fintech interact synergistically justifies Odin's design choice to embed educational cues within the app rather than relying on external literacy programs. Retention data from the synthesized studies (e.g., gamification increasing motivation) informs Odin's value-driven engagement strategy, prioritising practical features over extrinsic gamification. Although the paper focuses on saving rather than budgeting, the mechanisms (reduced friction, positive reinforcement) map directly to Odin's goal of encouraging users to stay within category limits.

**Directly justifies:**
- “Fintech features such as auto-debit, real-time balance transparency, and gamification improve saving discipline among Gen Z users by reducing entry friction and providing positive reinforcement.”
- “Financial literacy explains 72% of variation in Gen Z's fintech-enabled saving behavior, indicating that improving literacy is critical for system effectiveness.”
- “The synergy between financial literacy and fintech reduces reliance on high-cost loans and improves long-term financial resilience.”
- “Gamification elements in savings apps increase user motivation and promote consistent saving habits without requiring advanced financial knowledge.”

**Limits of relevance:**
- Study population is Indonesian; Filipino young professionals may differ in financial behaviors, cultural obligations, and fintech adoption patterns.
- Paper is a systematic literature review, not primary empirical research; specific effect sizes (e.g., 72%) are drawn from individual studies, not meta-analyzed.
- Focus on saving behavior, not directly on budget adherence or spending forecasting; translation to Odin's modules requires analogical reasoning.
- Fintech environment in the reviewed studies often assumes banking integration (auto-debit from accounts), whereas Odin relies on manual input only.

---

# Human-AI Collaboration in Customer Behavior Research: Personalizing Financial Services
*by Duvalla, V. R., 2025*

## TL;DR
Human-AI collaboration in financial services improves customer segmentation granularity (up to 15 distinct behavioral segments) and retention via predictive churn analysis, blending AI pattern recognition with human contextual intelligence.

## Topics
D.1 — Predictive Modeling in Personal Finance Systems

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

F.2 — Profile Classification Algorithm

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

I.1 — User Retention and Engagement in Personal Finance Systems

## Contribution to Odin
This paper directly informs Odin's user profile classification module by demonstrating that multi-dimensional behavioral segmentation using clustering and RNNs captures up to 15 distinct patterns, far exceeding demographic-only approaches. The human-in-the-loop framework with confidence-based escalation justifies Odin's planned design for anomaly detection and budget recommendation reviews, where uncertain predictions flag human oversight. Privacy-preserving techniques like federated learning support Odin's privacy-by-design commitment given manual transaction input and Philippine data privacy law (RA 10173). The reported retention lift from predictive churn analysis (not gamification) aligns with Odin's value-driven engagement strategy.

**Directly justifies:**
- "Integrated data platforms improve customer experience metrics by 40%, supporting Odin's need to unify manually entered transactions across categories for consistent profiling."
- "RNN implementations achieve higher predictive accuracy for future financial behaviors than conventional ML, applicable to Odin's spending forecasting module (though Odin uses LSTM specifically)."
- "Human-in-the-loop collaboration improves model prediction accuracy by 35%, justifying Odin's inclusion of human review for anomaly alerts or budget recommendations."
- "Federated learning enables personalization without centralized sensitive data, aligning with Odin's local-only storage and privacy-by-design for Filipino users."
- "Predictive churn analysis using customer behavior sequences enables proactive retention — a direct alternative to gamification for Odin's engagement strategy."

**Limits of relevance:**
- The paper focuses on general financial services (banking, wealth management), not specifically personal budget management systems like Odin.
- All quantitative findings are derived from enterprise banking environments with automated data feeds; Odin relies on manual transaction input, which may affect behavioral pattern detection.
- Population and geography are not specified but implicitly Western; Filipino cultural spending norms and income volatility are not addressed.
- The paper is a conceptual review synthesizing secondary sources, not an original empirical study with controlled experiments in a PFMS context.

---

# Simple Financial Management in Housewife Communities: A Qualitative Study on Daily Financial Management Patterns
*by Efendi, M. I., Widagdo, C. S., 2025*

## TL;DR
Housewives in resource-constrained Indonesian communities develop sophisticated adaptive financial strategies—including mental accounting, communal savings (arisan), and social insurance—that challenge conventional financial literacy narratives.

## Topics
A.2 — Existing Personal Finance and Budget Management Systems

C.1 — Budgeting Strategies and Budget Recommendation

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

G.1 — Expense Categorization in Filipino Personal Finance Contexts

## Contribution to Odin
This paper informs Odin’s budget recommendation module by detailing how low-resource users naturally employ mental accounting and tiered prioritization (primary/secondary/tertiary), suggesting that Odin’s budget recommendation should allow flexible, goal‑based envelopes rather than rigid category limits. The identified patterns of financial communication (open, partial, minimal) and negotiation strategies provide behavioral dimensions that Odin’s user profile classifier (F.2) could infer from transaction and interaction data. Although the study focuses on Indonesian housewives, the adaptive strategies—income diversification, informal risk pooling, and consumption optimization—reveal generalizable user behaviors that Odin must accommodate for variable‑income young professionals.

**Directly justifies:**
- “Housewives with no formal financial training develop mental accounting systems that categorize money by purpose, mirroring the envelope budgeting strategy used in mobile finance apps.”
- “Expenditure prioritization follows a stable three‑tier hierarchy (primary needs > secondary needs > tertiary needs), which can serve as default budget structure for new Odin users.”
- “Community‑based norms discourage debt for consumption and encourage saving ‘even a little’—a principle Odin could implement as a default savings recommendation.”
- “Financial communication patterns (open, partial, minimal) and conflict resolution strategies (transparency, value demonstration) are observable behaviors that can inform dynamic user profiling.”

**Limits of relevance:**
- Study population is Indonesian housewives, not Filipino young professionals; income volatility patterns and cultural obligations differ.
- No quantitative performance metrics for any algorithm; findings are qualitative and behavioral only.
- Manual recording systems (paper books, envelopes) do not evaluate digital or mobile interfaces.
- Community‑based informal financial systems (arisan, jimpitan) lack direct parallels in individual‑centric mobile budgeting.
- Findings reflect spousal financial dynamics that may not apply to single or unmarried users.

---

# A Systematic Literature Review on Personal Financial Management Practices: Budgeting, Investment, Debt, and Saving
*by Elliyana, E., Maricar, R., Toalib, R., 2025*

## TL;DR
Financial literacy and digital tools boost budgeting, saving, investing, and debt management, yet social and behavioral factors limit their effectiveness.

## Topics
A.2 — Existing Personal Finance and Budget Management Systems

B.1 — Mobile-First Design in Personal Finance Systems

C.1 — Budgeting Strategies and Budget Recommendation

## Contribution to Odin
This systematic review directly supports Odin’s budget recommendation module by establishing budgeting as the foundational behavior that unlocks saving and reduces debt — justifying the system’s emphasis on automated budget allocation. The finding that digital financial tools (e.g., budgeting apps) improve financial discipline when combined with basic literacy informs Odin’s mobile-first design and suggests that the app must embed educational cues alongside budgeting features. The review’s documentation of persistent behavioral biases (present bias, optimism bias) and the mediating role of self-efficacy validates Odin’s need for behavior-driven profile updates and nudge mechanisms, rather than purely knowledge-based interventions.

**Directly justifies:**
- “Structured budgeting reduces impulsive spending and builds saving discipline; it is the single most foundational PFM behavior across 47 studies.”
- “Digital financial tools such as mobile budgeting apps increase saving frequency and financial control, but only when users have baseline digital financial literacy.”
- “Financial literacy without self-regulation mechanisms (e.g., commitment devices, present-bias mitigation) fails to translate into sustained behavior change.”
- “Peer influence and social norms significantly affect budgeting and saving intentions; PFM systems must account for social factors, not just individual knowledge.”
- “In emerging economies, financial inclusion (85.1%) outpaces financial literacy (49.7%), creating a risk that access without understanding leads to over-indebtedness.”

**Limits of relevance:**
- Review includes no Filipino-specific primary data; findings from Indonesia and other emerging economies are the closest geographical proxy but may not fully reflect Philippine cultural and regulatory contexts.
- Most reviewed studies are cross-sectional; causal claims about digital tools and behavior change are limited.
- The review does not evaluate any ML-based forecasting, anomaly detection, or classification algorithms — only high-level digital tool adoption.
- Behavioral interventions discussed (nudges, commitment devices) are not implemented or tested within a mobile PFM app; applicability to Odin’s specific UX requires additional validation.

---

# THE ROLE OF DIGITAL BANKING FEATURES IN BANK SELECTION AN ANALYSIS OF CUSTOMER PREFERENCES FOR ONLINE AND MOBILE BANKING
*by Faisal, N., Nahar, J., Waliullah, M., Borna, R. S., 2024*

## TL;DR
Convenience (24/7 access, ease of use) is the top driver of digital banking adoption, followed by security and AI‑driven personalization, according to 112 studies.

## Topics
B.1 — Mobile‑First Design in Personal Finance Systems

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

I.1 — User Retention and Engagement in Personal Finance Systems

## Contribution to Odin
This systematic review validates that mobile banking users prioritize convenience (24/7 access, intuitive interfaces) — directly supporting Odin’s mobile‑first design as a non‑negotiable requirement. The finding that transparent security policies and multi‑factor authentication build user trust informs Odin’s privacy‑by‑design approach, especially given the sensitivity of manual transaction data. Retention data (90‑day loyalty effects from personalization) argues for value‑driven engagement mechanisms over gamification, which aligns with Odin’s no‑gamification scope.

**Directly justifies:**
- “User convenience — 24/7 availability, easy navigation, fast transactions — is cited by 47 of 112 studies as the single most important driver of digital banking adoption.”
- “Robust security measures (encryption, multi‑factor authentication, fraud detection) and transparent data usage policies are critical for building and maintaining user trust (42 studies).”
- “AI‑driven personalization improves user satisfaction and retention, with younger, tech‑savvy users showing the strongest preference (36 studies).”
- “The COVID‑19 pandemic forced rapid digital infrastructure upgrades, demonstrating that system resilience during disruptions is a competitive advantage (31 studies).”

**Limits of relevance:**
- The review covers banking, not personal budget management systems; feature priorities (e.g., loan applications) may differ for a pure budgeting app.
- All studies are from international contexts; Filipino cultural and income‑level preferences are not specifically addressed.
- The findings are synthesised from existing literature; no new primary data on Odin’s specific modules (forecasting, anomaly detection) is provided.
- Personalization findings rely on AI and bank‑level analytics; Odin’s minimal user input design may limit the depth of personalization possible.

---

# Dynamic Model for Budget Allocation in via Multi-Criteria Optimization
*by Gulbakyt, S., Almaz, A., Saule, S., Suhrab, Y., 2025*

## TL;DR
Multi-criteria optimization with SQP and GA allocates a regional budget across seven sectors, achieving near-identical objective values (0.0007% difference) and a Gini coefficient of 0.223.

## Topics
C.2 — Budget Recommendation Algorithm

## Contribution to Odin
This paper directly informs Odin’s budget recommendation module by demonstrating how multi-criteria optimization (SQP and GA) can allocate a constrained budget across competing categories. The comparison of deterministic (SQP) versus stochastic (GA) methods provides a design trade-off for Odin: SQP offers fast, precise solutions suitable for near-real-time recalculation, while GA provides robustness against local optima at higher computational cost. Although the domain is regional government, the mathematical formulation — weighted criteria subject to min/max bounds and equality constraints — maps directly to personal budget allocation where users have income limits, fixed expenses, and variable priorities.

**Directly justifies:**
- “SQP achieves rapid convergence (under 100 iterations) for constrained quadratic programming problems, making it suitable for real-time budget recalculations in mobile personal finance apps.”
- “GA reaches near-identical solutions to SQP (0.0007% difference) but requires 500 generations, trading speed for global search robustness — useful when user preferences are uncertain or non-convex.”
- “Multi-criteria optimization with weighted citizen satisfaction, strategic priorities, basic needs, and urbanization produces a Gini coefficient of 0.223, indicating equitable resource distribution across sectors — a fairness metric applicable to evaluating budget recommendation algorithms.”
- “Constraint-based allocation with min/max bounds ensures all categories receive at least a minimum threshold (basic needs) and no category dominates excessively, directly analogous to protecting essential spending categories (e.g., food, rent) in personal budgets.”

**Limits of relevance:**
- Domain is regional public sector budgeting (Kazakhstan), not personal finance; behavior of users vs. citizens differs.
- Synthetic citizen voting data — no real preference elicitation; Odin would need actual user input.
- Weights (0.2,0.2,0.3,0.3) are expert-defined without sensitivity analysis; Odin would require user-adaptable or learned weights.
- No validation with real-world budget outcomes; the model remains conceptual pending pilot testing.

---

# A User-Centric Exploration of Axiomatic Explainable AI in Participatory Budgeting
*by Hashemi, M., Darejeh, A., Cruz, F., 2024*

## TL;DR
Users find axiomatic explanations helpful for understanding system decisions and perceiving fairness, but trust impact is mixed — 27% increased trust, 23% decreased.

## Topics
H.1 — Data Privacy, Security, and User Trust

J.1 — System Evaluation

## Contribution to Odin
This paper directly informs Odin’s design priority of user trust and explainability in automated budget allocation. Although the domain is public participatory budgeting, the finding that axiom-based explanations improve perceived fairness and understanding applies directly to Odin’s budget recommendation module, where users may question why a particular category allocation was suggested. The mixed trust result (23% decreased trust post-explanation) serves as a critical warning: explanations can backfire. Odin’s evaluation plan (ISO 25010, SUS) should explicitly measure explanation impact on trust, not just usability.

**Directly justifies:**
- “Axiom-based explanations improved user understanding in 72.4% of participants, supporting the use of transparent, rule-based justifications in automated budgeting systems.”
- “Explanations increased perceived fairness in 30% of users and caused no fairness decrease, indicating that even simple rule-based explanations enhance outcome legitimacy.”
- “Providing explanations decreased trust in 23% of users — a non-trivial backfire effect that must be measured, not assumed, when adding XAI to a personal finance system.”

**Limits of relevance:**
- Study uses public participatory budgeting (voting on public projects), not personal budget allocation. Users’ relationship to the outcome differs (collective vs. individual).
- Small sample (n=26) and pilot-stage findings; no statistical significance reported.
- Greedy rule is simpler than Odin’s planned constraint optimization or ML-based recommendation; explanatory mechanism may not generalize directly.
- No Filipino participants; cultural attitudes toward algorithmic explanations may vary.

---

# A User Profile System for the Finance Platform of Commerce
*by Hu, Z., Qiu, Y., Hu, S., Cheng, Z., Qiu, S., 2024*

## TL;DR
K-means clustering groups users by shared characteristics, enabling precise marketing and risk control in a finance platform user profile system.

## Topics
F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

F.2 — Profile Classification Algorithm

## Contribution to Odin
This paper directly informs Odin’s user profile classification module by demonstrating how clustering (K-means) can segment users based on shared financial and behavioral characteristics. Although Odin requires a classification algorithm (not unsupervised clustering), the paper’s discussion of tag weighting methods (entropy, Delphi) and multi‑layer data processing (explicit + implicit acquisition) provides design justification for feature selection and cold‑start profiling. The system architecture separating individual profiles, group profiles, and behavior trends supports Odin’s need for behavior‑driven profile updates over time.

**Directly justifies:**
- "K-means clustering, an unsupervised learning algorithm, groups users by minimizing the distance to centroids across features such as income, expenditure, and transaction history."
- "User profiling enables precise marketing and risk control in financial platforms by analyzing behavior and preferences without account‑manager dependency."
- "Fact tags (statistical aggregates) and model tags (derived via business logic) with weighting methods like entropy weight or analytic hierarchy process improve profile accuracy."
- "Individual user profiles, group user profiles, and behavior trend analysis are three core modules of a complete user profile system."

**Limits of relevance:**
- Study context is Chinese enterprise commerce finance, not Filipino personal budget management.
- K-means is a clustering method, whereas Odin requires a classification algorithm for assigning users to predefined behavioral profiles.
- No empirical validation or accuracy metrics are provided for the profile system.
- Implicit data collection (logging behavior) raises privacy considerations not addressed in the paper; Odin relies on manual input only.

---

# Enhancing Financial Literacy in Young Adults: An Android-Based Personal Finance Management Tool
*by Imawan, R., Putra, W. P., Alqahtani, R., Milakis, E. D., Dumchykov, M., 2025*

## TL;DR
An Android-based personal finance app achieved an **"Excellent" 4.6/5** usability score from 50 young adults, with income/expense tracking and goal setting driving consistent engagement.

## Topics
A.2 — Existing Personal Finance and Budget Management Systems

B.1 — Mobile-First Design in Personal Finance Systems

C.1 — Budgeting Strategies and Budget Recommendation

G.1 — Expense Categorization in Filipino Personal Finance Contexts

I.1 — User Retention and Engagement in Personal Finance Systems

J.1 — System Evaluation

## Contribution to Odin
This paper validates the feature set Odin intends to implement (income/expense tracking, budgeting, goal setting, notifications) by demonstrating high user satisfaction (4.6/5) and self‑reported behavior change in a young adult population. The finding that visual goal progress bars and reminders are the strongest engagement drivers directly informs Odin's retention design — prioritizing value‑driven feedback over gamification. Although the study uses a basic Likert scale rather than ISO 25010 or SUS, its evaluation approach provides a benchmark for Odin's own usability testing with 50 users. The application's reliance on manual transaction entry (no bank integration) matches Odin's scope, making the engagement patterns directly transferable.

**Directly justifies:**
- "An Android‑based PFM app with income/expense tracking, budget projection, and goal setting achieved an overall usability score of **4.6/5 (Excellent)** from 50 young adults after two weeks of use."
- "Seventy‑eight percent of users rated their intention to continue using the app as 5/5, indicating that core tracking features alone can drive retention without gamification."
- "Visual progress bars for financial goals and automated reminders were cited as the most effective features for maintaining consistent tracking behavior."
- "Users request deeper spending trend analysis and customizable budget categories — gaps that Odin's predictive modules (forecasting, anomaly detection) are designed to fill."

**Limits of relevance:**
- Study population is Indonesian, not Filipino; cultural spending norms and income volatility may differ, though both are Southeast Asian emerging economies.
- Evaluation period was only two weeks; long‑term habit formation and retention beyond initial enthusiasm are not measured.
- No AI/ML features are present; the paper cannot justify algorithm selection for Odin's forecasting, anomaly detection, or profile classification modules.
- Usability evaluation used an ad‑hoc Likert scale, not the ISO 25010 or SUS frameworks Odin requires for formal evaluation.

---

# Innovations in UI/UX Design of Mobile Applications: Trends, Practices and Challenges
*by Jamal, A., Hashmat, S., 2025*

## TL;DR
Mobile UI/UX design is shifting toward AI-driven personalization, gesture/voice interactions, and inclusive design, while struggling with small screens, cross-platform consistency, and rapid user expectations.

## Topics
B.1 — Mobile-First Design in Personal Finance Systems

I.1 — User Retention and Engagement in Personal Finance Systems

## Contribution to Odin
This review directly informs Odin's mobile-first design strategy by consolidating proven practices such as progressive disclosure, performance optimization, and inclusive accessibility — all critical for a manual-input budget app targeting Filipino young professionals. The emphasis on AI-driven personalization supports Odin's adaptive budget recommendation and user profiling modules, showing how real-time behavior tracking can tailor UI without overwhelming users. Retention mechanisms identified in the paper — continuous feedback loops and value-driven engagement — justify Odin's decision to avoid gamification and instead rely on utility and clarity to keep users active.

**Directly justifies:**
- "Mobile-first design prioritizes core functionality on small screens through progressive disclosure and icon-based navigation, reducing cognitive load."
- "AI-driven personalization increases user engagement by automatically adapting interfaces based on real-time behavior and context."
- "Performance optimization (reduced asset sizes, local caching) directly impacts user retention — lag causes rapid app abandonment."
- "Inclusive design practices (screen readers, scalable text, voice navigation) are essential for serving users with varying abilities and situational constraints."
- "Cross-platform frameworks (Flutter, React Native) enable consistent UX across iOS and Android while reducing development overhead."

**Limits of relevance:**
- Review paper synthesizes existing studies; no original empirical validation of trends in a financial or Filipino context.
- Discussion of personalization and AI is generic; does not evaluate specific algorithms (e.g., LSTM, Isolation Forest) relevant to Odin's modules.
- Filipino cultural spending behaviors and income volatility patterns are not addressed.
- No evaluation of manual transaction entry workflows, which differ from automated banking integrations.

---

# DIGITIZATION IN RETAIL BANKING: A REVIEW OF CUSTOMER ENGAGEMENT AND FINANCIAL PRODUCT ADOPTION IN SOUTH ASIA
*by Kowsar, M. M., Islam, S., Mohiuddin, M., Siddiqui, N. A., 2025*

## TL;DR
Mobile internet and national digital ID systems in South Asia have expanded financial inclusion, but persistent rural-urban infrastructure gaps and low digital literacy limit equitable adoption of credit and insurance products.

## Topics
A.2 — Existing Personal Finance and Budget Management Systems

B.1 — Mobile-First Design in Personal Finance Systems

D.1 — Predictive Modeling in Personal Finance Systems

E.1 — Anomaly Detection in Personal Finance Systems

I.1 — User Retention and Engagement in Personal Finance Systems

## Contribution to Odin
This systematic review directly supports Odin’s mobile-first design priority by documenting that mobile penetration (>85%) and mobile broadband (>95%) are the primary access channels in developing economies, justifying Odin’s mobile-only scope. The review’s findings on AI-driven personalization and behavioral nudges (e.g., automated savings prompts, spending summaries) provide evidence for Odin’s budget recommendation and forecasting modules to incorporate real-time personalization rather than static templates. Additionally, the documented gap between account access and active usage (dormant accounts, low transaction diversity) reinforces Odin’s focus on engagement-centered retention mechanisms over simple onboarding, and the review’s identification of digital literacy as a barrier suggests Odin must prioritize simple UX and local language support for Filipino young professionals.

**Directly justifies:**
- “Digitally engaged customers are 2.3 times more likely to open secondary financial products than non-engaged counterparts, demonstrating that engagement drives cross-product adoption (Verma & Sinha, 2018).”
- “AI-powered chatbots and robo-advisors providing 24/7 financial guidance increase customer satisfaction and retention, with platforms using behavioral analytics reporting higher cross-product uptake.”
- “Mobile internet access significantly influences account ownership, use of savings tools, and participation in credit programs in South Asia (Haleem et al., 2022).”
- “Inclusion metrics that measure only account access overstate progress; usage frequency, transaction diversity, and platform retention are more meaningful indicators of financial empowerment.”
- “Personalized savings prompts, spending summaries, and goal-setting tools increase transaction frequency and deepen platform loyalty in mobile-first banking environments.”

**Limits of relevance:**
- Study focuses on South Asia (India, Bangladesh, Pakistan), not the Philippines; cultural spending norms and regulatory environments differ.
- The review emphasizes retail banking (accounts, loans, insurance) rather than personal budget management systems like Odin.
- Algorithm-specific details (e.g., LSTM architecture, Isolation Forest configuration) are absent; the review discusses AI/ML only at a high level.
- Findings assume bank-integrated digital services (e.g., direct account linking), whereas Odin relies on manual transaction input.
- No evaluation of cold-start user profiles or algorithm performance for new users with no transaction history.

---

# The Influence of E-Wallets on The Consumptive Behavior Generation Z: Systematic Review
*by Kuswardhani, E. L., Sari, M. A. N. P., Yuniawan, A., Kusumawardhani, A., 2025*

## TL;DR
Digital wallets increase Generation Z’s spending frequency and impulsivity by reducing the psychological “pain of paying” through frictionless, gamified interfaces.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

C.1 — Budgeting Strategies and Budget Recommendation

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

I.1 — User Retention and Engagement in Personal Finance Systems

## Contribution to Odin
This systematic review directly informs Odin’s user profiling and budgeting modules by demonstrating that frictionless digital payments increase impulsive spending among young adults — a baseline behavioral pattern Odin must account for when classifying users and recommending budgets. The finding that most e‑wallet apps lack budgeting tools (Rahi et al., 2022) justifies Odin’s inclusion of spending summaries, category alerts, and goal‑setting features as core engagement mechanisms. Although the review focuses on e‑wallets (not budget management systems), its identification of psychological triggers (push notifications, gamification, cashback) provides a cautionary framework: Odin should avoid reinforcing spending and instead use similar engagement techniques to encourage savings and adherence.

**Directly justifies:**
- “E‑wallet usage among Generation Z shows a significant positive correlation with increased spending frequency and impulse buying, driven by reduced perceived payment friction (Yeo et al., 2021; Wang et al., 2021).”
- “Most e‑wallet applications lack integrated budgeting tools or spending categorization, causing users to rely on balance visibility alone and report post‑spending regret (Rahi et al., 2022; Lestari et al., 2021).”
- “Promotional features such as cashback and limited‑time offers create a perceived ‘value‑saving’ effect that motivates unplanned purchases, even when the spending itself is unnecessary (Liu et al., 2021; Lestari et al., 2021).”
- “Push notifications and gamification elements (streaks, loyalty tiers) condition repeat spending habits through habit loops, making consumption less deliberate and more automatic over time.”
- “Digital payment systems reduce the psychological ‘pain of paying’ by decoupling consumption from the awareness of spending actual money (Thaler, 1985; Kim & Choi, 2023).”

**Limits of relevance:**
- The review synthesizes studies from multiple countries (including Indonesia and India), not specifically the Philippines; Filipino cultural spending priorities and digital payment adoption rates may differ.
- The focus is on e‑wallets as spending tools, not on personal budget management systems; findings on feature design (e.g., cashback) may not directly translate to Odin, which has no gamification or promotional mechanics.
- The reviewed studies are largely cross‑sectional and self‑reported; causality between e‑wallet use and consumptive behavior is not firmly established.
- The population is general Generation Z (ages 18–27), not specifically young professionals with stable income; Odin’s target may have different spending discipline.

---

# Proteus: Shapeshifting Desktop Visualizations for Mobile via Multi-level Intelligent Adaptation
*by Liu, C., Cheng, S., Liang, F., Jiang, Z., Huang, L., Athapaththu, K., Wang, Y., 2026*

## TL;DR
A multi-level design space and LLM-driven multi-agent system transform desktop visualizations into mobile-optimized versions, achieving 91.8% render success and significantly higher readability and interaction quality than baseline.

## Topics
B.1 — Mobile-First Design in Personal Finance Systems

J.1 — System Evaluation

## Contribution to Odin
This paper provides a validated framework for adapting any desktop visualization to mobile screens while preserving data fidelity and usability — directly applicable to Odin’s need to display budget charts, spending forecasts, and anomaly alerts on small mobile viewports. The multi-level design space (topology → reference frame → elements) offers a structured checklist for Odin’s mobile UX design, ensuring that decisions like axis transposition or tooltip injection are made systematically rather than ad hoc. The user study methodology (5 dimensions, within-subjects, Wilcoxon signed-rank) and the 91.8% render success benchmark provide a rigorous evaluation template for Odin’s own ISO 25010 and SUS assessments.

**Directly justifies:**
- “Desktop-to-mobile visualization adaptation requires coordinated decisions across global layout, reference frames, and visual elements — a flat list of heuristics is insufficient.”
- “LLM-driven multi-agent systems can achieve 91.8% render success on diverse real-world charts, outperforming baselines without structured design knowledge (p < 0.05 for fidelity and readability).”
- “Externalizing dense annotations into scrollable panels (e.g., ‘Key insights’) and converting hover interactions into dedicated sliders preserves information while respecting touch constraints.”
- “User evaluations of mobile adaptations should include separate ratings for data fidelity, perceptual readability, interaction reasonableness, and visual aesthetics — all improved significantly by hierarchical planning.”

**Limits of relevance:**
- Domain is general visualization, not personal finance — but Odin’s charts (budget, spending, forecasts) share the same mobile legibility constraints.
- Study participants were visualization-experienced, not Filipino young professionals — usability findings may generalize but need local validation.
- The system requires vector source code (SVG/HTML); Odin’s own generated charts are code-based, so the method is directly applicable.
- No evaluation of cold-start or partial data scenarios; Odin’s early-user phase may require additional adaptation rules.

---

# Explainable and Context-Aware Financial Nudges via Event-Driven Microservices
*by Mandaleeka, A. P., 2025*

## TL;DR
A modular, event-driven microservices framework with SHAP-based explanations delivers context-aware financial nudges that users understand and trust.

## Topics
A.2 — Existing Personal Finance and Budget Management Systems

C.1 — Budgeting Strategies and Budget Recommendation

C.2 — Budget Recommendation Algorithm

E.1 — Anomaly Detection in Personal Finance Systems

I.1 — User Retention and Engagement in Personal Finance Systems

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

## Contribution to Odin
This paper directly informs Odin’s design by showing how explainability (via SHAP) can be embedded into a real‑time financial nudging pipeline, addressing user trust – a critical gap for manual‑input apps. The event‑driven microservices architecture provides a blueprint for Odin’s modular deployment, where each intelligent module (forecasting, anomaly detection, budget recommendation) could expose explainability hooks. Although the paper evaluates on synthetic data, its claim that SHAP‑based explanations increase perceived relevance and trust justifies Odin’s inclusion of an XAI layer, especially for the anomaly detection and budget recommendation modules.

**Directly justifies:**
- “SHAP provides local interpretability with formal guarantees of fairness and consistency, making it suitable for financial systems where trust and transparency are critical.”
- “Contextual triggers (e.g., time, location, prior habits) increase user engagement compared to static, generic alerts.”
- “Explainability (e.g., SHAP outputs converted to natural language) boosts users’ perceived relevance and trust in automated financial advice.”
- “A microservices architecture using Kafka for event streaming enables modular, scalable, and fault‑tolerant financial nudging without blocking user interactions.”

**Limits of relevance:**
- Paper reports no quantitative adherence, retention, or accuracy metrics – only qualitative claims and synthetic evaluation.
- The proposed system assumes open banking APIs (e.g., Plaid) for transaction ingestion; Odin relies on manual input, which changes the data availability and latency profile.
- Findings are not specific to Filipino users; cultural spending patterns and financial literacy levels may alter nudge effectiveness.
- SHAP’s computational cost in real‑time may be prohibitive for mobile‑first deployment without optimizations (caching, asynchronous generation).

---

# Integration of Explainability in Recommender Systems to Enhance Enterprise Value Strategies
*by Montagna, A., 2024*

## TL;DR
Balancing business value and explainability in recommender systems improves user trust and adoption without catastrophic accuracy loss, demonstrated by the XVMF model.

## Topics
C.2 — Budget Recommendation Algorithm

J.1 — System Evaluation

## Contribution to Odin
This thesis directly informs Odin's budget recommendation module by demonstrating that value-aware optimization (analogous to maximizing user budget adherence or savings) can be quantitatively balanced with explainability, a critical requirement for user trust in personal finance apps. The XVMF model provides a tunable framework where Odin could prioritize either recommendation value (e.g., surplus allocation efficiency) or explanation quality (e.g., "why this budget limit") via hyperparameters. Furthermore, the systematic VARS taxonomy helps Odin designers evaluate candidate algorithms (RL, constraint optimization, post-processing) for budget recommendation based on their value optimization approach. The critique of graph-based explainable systems highlights the need for Odin to adopt quantitative evaluation metrics rather than qualitative examples when justifying explainability features.

**Directly justifies:**
- "Value-aware recommender systems that maximize profit or CTR can be extended with explainability regularization without complete loss of recommendation accuracy (XVMF achieves 0.2493% NDCG vs MF 0.1281% on Yelp)."
- "The trade-off between business value and explainability is controlled by hyperparameters (λ, δ); optimal balance occurs at low values (λ=0.001, δ=0.001 for Yelp), beyond which both metrics degrade sharply."
- "83% of graph-based explainable recommender systems lack quantitative evaluation of explanation quality, relying on qualitative case studies — a gap Odin's evaluation framework should avoid."
- "Explainable Matrix Factorization (EMF) with neighborhood-based explainability power (Eui) improves explanation coverage but requires careful tuning to avoid accuracy loss."

**Limits of relevance:**
- Thesis uses product recommendation datasets (Yelp, Amazon) with item profit as business value; Odin's budget recommendation involves different value constructs (user adherence, savings rate).
- Experiments are offline and do not measure actual user trust or adoption in a financial context.
- The XVMF model assumes item-level business value is known and static; Odin's budget categories may have dynamic or user-defined value weights.
- No Filipino demographic or spending behavior data used; cultural factors affecting explanation preferences are unaddressed.

---

# Intelligent UI’s: Revolutionizing Financial Transaction Systems Through AI and Event-Driven Architecture
*by Musunuri, H., 2025*

## TL;DR
Event-driven UIs with behavioral biometrics reduce transaction friction by 78% and cut fraud detection false positives by 37.8% while improving completion rates 31.6%.

## Topics
B.1 — Mobile-First Design in Personal Finance Systems

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

I.1 — User Retention and Engagement in Personal Finance Systems

J.1 — System Evaluation

## Contribution to Odin
This paper justifies Odin’s mobile-first UI decisions by quantifying how event-driven architectures and predictive adaptation reduce task completion time by over 50% — directly supporting the design of Odin’s manual transaction input flow. The behavioral analytics findings (97.6% user identification after 14 seconds) validate continuous, frictionless authentication as a security model for Odin, eliminating password fatigue. The documented 24.8% reduction in support calls from contextual guidance informs Odin’s help system design, and the phased migration success rates (3.7× higher) provide a practical roadmap for incremental feature rollout.

**Directly justifies:**
- “Event-driven financial interfaces reduce transaction processing time by 53.7% for standard operations and 61.2% for complex multi-step processes (n=127 institutions).”
- “Behavioral biometrics achieve user identification accuracy of 97.6% after just 14 seconds of active interaction, enabling continuous authentication without explicit user steps.”
- “Adaptive, context-aware interfaces increase transaction completion rates by 31.6% and reduce abandonment caused by cognitive overload.”
- “Phased migration implementing event-driven architecture as a facade over legacy systems delivers 27.3% customer satisfaction improvement within six months with 42% less investment than full replacement.”
- “Progressive disclosure reduces visual search time by 41.8% and error rates by 31% in complex multi-step financial transactions.”

**Limits of relevance:**
- Paper focuses on financial transaction systems (payments, fraud) rather than personal budget management; applicability to spending forecasting or budget recommendation is indirect.
- All studies conducted outside the Philippines (USA, India, global institutions); Filipino young professional behavior patterns not examined.
- Relies on backend integration with bank systems; Odin uses only manual transaction input, which may alter the performance gains from predictive pre-population.
- No evaluation of cold-start scenarios (new users with no interaction history) — a key Odin requirement.

---

# The Mediating Role of Financial Well-Being in the Relationship between Financial Behavior and Stress Among Irregular Income Workers
*by Nurkhalida, K., Renanita, T., 2025*

## TL;DR
Financial well-being fully mediates the relationship between financial behavior and stress in irregular income workers aged 20–40, meaning behavior reduces stress only indirectly through improved well-being.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

C.1 — Budgeting Strategies and Budget Recommendation

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

## Contribution to Odin
This paper directly informs Odin’s user profiling and budget recommendation modules by demonstrating that financial well-being is the mechanism through which financial behavior (including budgeting) reduces stress—particularly for irregular income workers, which matches Odin’s target demographic. The finding that behavior alone does not directly lower stress justifies Odin’s focus on improving financial well-being (e.g., through smart budget recommendations and stability signals) rather than simply tracking transactions. While the study is from Indonesia, the psychological mechanism likely generalizes to Filipino young professionals with irregular income, supporting Odin’s design to prioritize well-being as an intermediate outcome.

**Directly justifies:**
- “Financial behavior does not directly reduce stress among irregular income workers aged 20–40; its effect is fully mediated by financial well-being (indirect effect = -0.5045, 95% CI excludes zero).”
- “Financial behavior positively predicts financial well-being in irregular income workers (β = 0.6566, p < .001), indicating that better budgeting and saving practices improve perceived financial stability.”
- “Higher financial well-being is associated with significantly lower stress levels (β = -0.6761, p < .001), a relationship that holds even when controlling for financial behavior.”
- “Irregular income workers—who face income volatility and uncertainty—require financial behavior improvements to first raise financial well-being before stress reduction occurs.”

**Limits of relevance:**
- Study population is Indonesian, not Filipino; cultural and economic differences (e.g., social security systems, cost of living) may affect generalizability.
- No algorithmic or ML component; relevance is behavioral and psychological, not computational.
- Cross-sectional design cannot establish causality, only mediation pathways.
- Self-reported data may be subject to social desirability and recall bias.

---

# Behavior-Driven Personalization Framework to Improve Repeat Usage in Mobile-Enabled Financial Ecosystems
*by Omotayo, K., Uzoka, A., Okolo, C., Olinmah, F., Adanigbo, O., 2023*

## TL;DR
Behavior-driven personalization using real-time user actions, dynamic segmentation, and adaptive triggers increases repeat usage in mobile financial ecosystems.

## Topics
B.1 — Mobile-First Design in Personal Finance Systems

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

F.2 — Profile Classification Algorithm

I.1 — User Retention and Engagement in Personal Finance Systems

## Contribution to Odin
This paper directly informs Odin's User Profile Classification module (F.2) by providing a dynamic segmentation engine that updates user profiles based on real-time behavioral data rather than static demographics. The personalized trigger system and continuous feedback loop justify Odin's retention strategy (I.1) through contextual nudges and adaptive UI, avoiding gamification in favor of value-driven engagement. The emphasis on goal-aligned personalization (promoting saving and budgeting) aligns with Odin's mission to improve financial health among Filipino young professionals. Although the framework is conceptual and not Filipino-specific, its behavioral principles (loss aversion, heuristics, nudging) are universally applicable and can guide Odin's algorithm selection for profile classification and retention mechanisms.

**Directly justifies:**
- "Behavior-driven personalization using real-time user actions improves repeat usage in mobile financial ecosystems by delivering contextually relevant nudges and adaptive UI."
- "A segmentation engine that dynamically categorizes users into behavioral cohorts (habitual, casual, value-seeking) enables tailored personalization strategies without requiring static demographic inputs."
- "Continuous feedback loops based on reinforcement learning principles refine personalization by learning from user responses to interventions, reducing notification fatigue over time."
- "Goal-aligned personalization that promotes saving and budgeting over excessive spending builds user trust and long-term engagement."
- "Personalization systems must incorporate transparency, consent, and restraint to avoid exploitative practices in financial decision-making."

**Limits of relevance:**
- Paper proposes a conceptual framework without empirical validation; claims are theoretical and untested.
- Authors and study context are Nigerian and US-based, not Philippine; behavioral patterns may differ.
- Framework assumes real-time data streaming infrastructure (Kafka, cloud warehouses) that may exceed Odin's current scope.
- No specific classification algorithm is provided; Odin would need to implement a concrete classifier (e.g., decision tree, clustering).
- Cold-start problem (new users with no behavioral history) is not addressed.

---

# Optimizing Banking Application Interfaces: A User-Centric Perspective on Consent Management in Digital Banking Environments
*by Pakarinen, O., 2025*

## TL;DR
Two-layer consent management (category overview + detailed permissions) improved user understanding and perceived control over data-sharing decisions in digital banking usability tests.

## Topics
B.1 — Mobile-First Design in Personal Finance Systems

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

I.1 — User Retention and Engagement in Personal Finance Systems

## Contribution to Odin
This paper directly informs Odin’s approach to data privacy and user trust by demonstrating that a two‑layer consent interface (category overview + detailed permissions) increases users’ perceived control and confidence. Odin, as a mobile‑first personal budget manager handling sensitive financial data, must present consent choices clearly to avoid user skimming and mistrust. The finding that visual badges (e.g., green/yellow for consent states) and progressive disclosure reduce cognitive load justifies similar design decisions in Odin’s own consent or data‑sharing settings. Although the study focuses on banking, the same user‑centered principles apply to any financial app that requests permission to store or analyze spending data.

**Directly justifies:**
- “Two‑layer consent management (category overview then detailed permissions) improves user confidence and perceived control compared to dense, single‑screen legal text.”
- “Visual status badges (green = all accepted, yellow = partial) help users quickly assess their consent state without reading every item.”
- “Users ignore long consent descriptions; concise, labelled categories with on‑demand tooltips reduce cognitive load and increase engagement.”
- “Usability testing with iterative simplification reduced task completion time and hesitation in consent management flows.”

**Limits of relevance:**
- Study population is not Filipino; banking customer behavior in Finland/Europe may differ from Filipino young professionals.
- Prototype tested in a controlled environment, not a live banking app with real financial consequences.
- No evaluation of long‑term trust or retention effects beyond immediate usability metrics.
- Consent management for data sharing is not identical to Odin’s core budgeting features, but the UI principles transfer.

---

# EXPLORING TWO DECADES OF PERSONAL FINANCIAL PLANNING: A SYSTEMATIC LITERATURE REVIEW
*by Pande, S., Mazhar, S. S., Khan, F. S., Khan, B. A., Haque, E., Mir, M. A., 2024*

## TL;DR
A 20-year systematic literature review shows growing scholarly interest in personal financial planning, the rise of digital tools like mobile apps, and persistent gaps in understanding financial behaviors across socioeconomic groups.

## Topics
A.2 — Existing Personal Finance and Budget Management Systems

B.1 — Mobile-First Design in Personal Finance Systems

## Contribution to Odin
This review confirms that mobile applications and digital planning tools have become central to personal financial management, directly supporting Odin’s mobile-first design decision. The identification of persistent gaps in understanding financial behaviors across socioeconomic groups justifies Odin’s focus on a specific demographic (Filipino young professionals) rather than assuming universal patterns. The paper’s finding that financial literacy influences planning practices can be cited to argue that intelligent systems like Odin must supplement user literacy through automated recommendations and behavioral nudges. Although the review is bibliometric rather than algorithmic, it provides RRL-level evidence that the domain has matured and that technology-mediated planning is now the norm.

**Directly justifies:**
- “Mobile applications and robo-advisors have made financial information and services easily accessible, enabling individuals to manage their finances.” (Haridan et al., 2020, cited in review)
- “There is a lack of clear identification of the cause-related constructs critical to individuals' financial processes” – a gap that Odin’s behavioral profiling module can address.
- “People with better financial literacy have better practices (budgeting, monitoring expenditures, managing debt)” – justifying Odin’s role as a literacy-supporting tool.
- “FinTech has democratized investment opportunities and connected unbanked individuals to banking services” – supporting Odin’s inclusion of budgeting for underserved young professionals.

**Limits of relevance:**
- The review is bibliometric, not empirical; it reports on publication trends, not causal effects of digital tools on outcomes.
- No specific algorithm (LSTM, Isolation Forest, etc.) is evaluated, so it cannot justify algorithm selection directly.
- Findings are global; Filipino cultural and economic specificities are not addressed.
- The review does not distinguish between manual vs. automated transaction entry, a key Odin design constraint.

---

# Development and Evaluation of My Money Manager: An Intelligent Mobile App for Personalized Financial Insight
*by Parameswaran, S., Saad, S. Z., 2025*

## TL;DR
A personal finance Android app with fixed-variable expense differentiation and 90-day spending pattern analysis achieved **82.8% user validation** for income-expense tracking and 74.3% for improved financial habits.

## Topics
A.2 — Existing Personal Finance and Budget Management Systems

B.1 — Mobile-First Design in Personal Finance Systems

C.1 — Budgeting Strategies and Budget Recommendation

E.1 — Anomaly Detection in Personal Finance Systems

G.1 — Expense Categorization in Filipino Personal Finance Contexts

J.1 — System Evaluation

## Contribution to Odin
This paper provides direct empirical validation that users value fixed-vs-variable expense differentiation and anomaly detection — both features Odin's expense categorization and anomaly detection modules require. The finding that 31.4% of users somewhat disagreed about data security serves as a critical warning for Odin's privacy-by-design requirements, especially given the sensitivity of Filipino financial data. The usability evaluation framework (six-point Likert across four dimensions) offers a tested template for Odin's ISO 25010 and SUS evaluation protocol, while the 35-participant sample size provides a benchmark for Odin's target evaluation scale.

**Directly justifies:**
- "Users reported 82.8% validation for income-expense tracking features, indicating that reliable manual transaction logging is the most valued capability in personal finance apps."
- "Only 11.4% of users strongly agreed their financial data was secure in a standard Android PFMS app, demonstrating that data security is the weakest trust dimension requiring explicit design attention."
- "Fixed vs. variable expense differentiation addresses a critical gap identified in existing PFMS literature (Shaikh et al., 2022) and was implemented successfully in a working mobile application."
- "Financial insight comprehension received only 37.1% 'Strongly Agree' for ease of use, indicating that data visualization quality directly impacts perceived usefulness of analytical features."
- "A 35-participant usability evaluation with six-point Likert scales provides sufficient signal to identify both strengths (tracking) and weaknesses (security, insight clarity) in PFMS design."

**Limits of relevance:**
- Study population is Malaysian, not Filipino; cultural spending norms and financial inclusion contexts differ, though both are Southeast Asian emerging economies.
- The app uses rule-based categorization, not ML classification — Odin's approach is more sophisticated but the user validation patterns remain instructive.
- No algorithm performance metrics (accuracy, precision, recall) are reported — only user perception data, which cannot justify model selection.
- The 35-participant sample is small for generalizable claims about usability across demographic segments.
- Data security concerns reflect user perception, not objective security auditing results.

---

# Integrating Financial Management and Gamification: A Systematic Literature Review and Future Research Agenda
*by Prasetyo, A. P., Santoso, H. B., Putra, P. O. H., 2023*

## TL;DR
A systematic review of 53 studies (2018–2022) finds that gamification in personal finance is under-researched, with most work in education; self-determination theory and technology acceptance models dominate, and future research should explore cultural factors and financial contexts.

## Topics
A.2 — Existing Personal Finance and Budget Management Systems

I.1 — User Retention and Engagement in Personal Finance Systems

## Contribution to Odin
Although Odin explicitly excludes gamification, this review’s synthesis of behavioral intention theories (TPB, SDT) provides foundational justification for Odin’s engagement design: users’ perceived usefulness and autonomy support directly influence continued use, independent of game elements. The finding that only 17.2% of gamification research addresses finance highlights a broader gap in understanding user motivation in PFM — a gap Odin’s non-gamified, value-driven forecasting and anomaly detection can fill. The paper’s identification of cultural factors as an underexplored moderator directly supports Odin’s need for Filipino-specific behavioral research. Further, the scarcity of longitudinal studies on sustained behavior change informs Odin’s evaluation plan, which will track retention over time.

**Directly justifies:**
- “Financial behavior research predominantly uses the Theory of Planned Behavior (50% of studies), which underpins the intention-action relationship central to budget adherence.”
- “Self-Determination Theory (14.3% of gamification studies) explains user motivation through autonomy, competence, and relatedness — applicable to non-gamified features like personalized budget recommendations.”
- “Only 17.2% of gamification research focuses on finance, leaving a significant gap in understanding how to drive engagement in PFM apps without gamification.”
- “Most gamification studies use cross-sectional surveys; longitudinal evidence on sustained behavior change is lacking, highlighting a method gap Odin’s evaluation could address.”

**Limits of relevance:**
- The paper is a systematic literature review, not an empirical study; its claims are synthesized from others, not original findings on causality.
- No Filipino-specific data; cultural factors are identified as a research gap, not studied.
- Odin explicitly excludes gamification, so direct application of gamification-element findings is limited to informing what not to do or transferring psychological theory.
- Publication window ends in 2022; newer studies (2023 onward) on PFM engagement are not included.

---

# Modeling the Future: A Comprehensive Analysis of Modeling Languages in the Development of Next-Generation Academic Information Systems (2016–2026)
*by Pratama, A. R., 2026*

## TL;DR
High-fidelity BPMN modeling reduces post-implementation logic errors by 22% and raises perceived ease of use by 18%, bridging the adoption gap in academic information systems.

## Topics
B.1 — Mobile-First Design in Personal Finance Systems

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

I.1 — User Retention and Engagement in Personal Finance Systems

J.1 — System Evaluation

## Contribution to Odin
Though the domain is academic, this paper’s findings on mobile‑first modeling directly justify Odin’s mobile‑native design priority. The measured 30% engagement deficit when ignoring mobile constraints provides a quantitative rationale for prioritizing responsive UX over desktop‑first assumptions. The paper also validates that structured usability evaluation (TAM/UTAUT) predicts adoption, supporting Odin’s planned use of SUS and ISO 25010. Finally, the concept of “frictionless security” (biometrics, SSO) informs Odin’s privacy‑by‑design choices without creating user resistance.

**Directly justifies:**
- “Non‑mobile‑native system models produce a 30% lower engagement rate in core transaction modules (registration/payment), demonstrating that mobile‑first design is a prerequisite for user adoption.”
- “High‑fidelity process modeling (BPMN) raises perceived ease of use by 18%, a margin that can differentiate successful from failing personal finance apps.”
- “Security‑by‑design must be modeled as invisible frictionless layers (e.g., biometrics, single sign‑on); visible security barriers lead to shadow IT workarounds.”
- “User adoption rates correlate strongly with modeling clarity – systems modeled for human workflows achieve 75–80% adoption versus 40–45% for structure‑only blueprints.”

**Limits of relevance:**
- Domain is academic administration, not personal finance; workflows differ (course registration vs. budget tracking).
- Geographic context is unspecified (author from Indonesia, data from unspecified HEIs) – not Filipino‑specific.
- Evaluation used TAM/UTAUT, not ISO 25010 or SUS; Odin’s primary frameworks are different but conceptually adjacent.
- No direct test of spending behavior, anomaly detection, or forecasting algorithms.

---

# Making maps & visualizations for mobile devices: A research agenda for mobile-first and responsive cartographic design
*by Roth, R. E., Çöltekin, A., Delazari, L., Denney, B., Mendonça, A., Ricker, B. A., Shen, J., Stachoň, Z., Wu, M., 2024*

## TL;DR
Mobile-first cartographic design requires rethinking scale, projections, symbols, labels, and interaction — this paper lists 20 research challenges to adapt cartography for small screens, touch, and mobile contexts.

## Topics
B.1 — Mobile-First Design in Personal Finance Systems

## Contribution to Odin
This paper directly informs the mobile-first design of Odin’s interface. Odin is a mobile-FIRST personal budget management app targeting Filipino young professionals, and its usability depends on adapting cartographic principles to small screens, touch interaction, and variable environmental conditions. The paper’s synthesis of constraints (e.g., small screen, limited bandwidth, battery life) and enablements (e.g., location services, multimodal input) provides a checklist for Odin’s UI/UX planning. Although the paper focuses on maps, its findings on glanceable visualizations, energy-aware color schemes, and thumb‑based interaction layout are directly transferable to Odin’s budget dashboards and spending charts.

**Directly justifies:**
- “Mobile-first design constrains visual complexity: 91% of mobile map apps omit legends, requiring symbols that are immediately interpretable without external reference.”
- “Thumb‑based UI widgets (bottom navigation tabs, floating action buttons, pull‑up menus) improve interaction efficiency on handheld devices compared to top‑ or left‑aligned desktop layouts.”
- “Imagery basemaps and dark mode color schemes reduce energy consumption and preserve battery life, but only 25% of mobile apps offer a dark basemap option.”
- “Gaze‑contingent displays and multimodal (voice, haptic) feedback can reduce visual attention demands when users are moving—relevant to Odin’s use while commuting.”

**Limits of relevance:**
- The paper addresses cartographic maps, not financial dashboards; direct transfer of symbolization guidelines requires validation for bar charts and spending categories.
- Most empirical findings come from navigation and wayfinding tasks, not financial management.
- Energy‑aware design assumes OLED screens; Odin’s target device mix may include IPS LCD screens with different power profiles.
- The research agenda is conceptual; specific design recommendations are not yet empirically validated for personal finance apps.

---

# Digital Persona Modeling for Context-Aware Financial Decisioning
*by Sanhosh, S. R., Singh, A. K., 2025*

## TL;DR
LSTM achieves 93.6% accuracy and 92.9% F1-score for context-aware financial decisioning, outperforming Random Forest and K-Means on simulated mobile transaction data.

## Topics
A.2 — Existing Personal Finance and Budget Management Systems

C.2 — Budget Recommendation Algorithm

D.2 — LSTM as the Spending Forecasting Algorithm

F.2 — Profile Classification Algorithm

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

## Contribution to Odin
This paper directly justifies Odin's selection of LSTM for the spending forecasting module by demonstrating LSTM's superior accuracy (93.6%) over Random Forest and K-Means on sequential transaction data. The persona clustering approach using K-Means provides a foundation for Odin's user profile classification module, showing how behavioral segmentation (spending style, risk tolerance) can be integrated with ML. The context-aware risk function models real-time user state (location, time, device) — applicable to Odin's anomaly detection and budget recommendation in mobile contexts. The privacy-preserving federated learning design (local processing, no raw data leaving device) aligns with Odin's requirement for manual input and local-only data handling.

**Directly justifies:**
- "LSTM achieves 93.6% accuracy and 92.9% F1-score for sequential financial behavior classification, outperforming Random Forest (91.2%) and K-Means (75%) on mobile transaction data."
- "Contextual variables (location, time, device) improve financial decision risk assessment via the function R = α₁C_location + α₂C_time + α₃C_device + βT."
- "K-Means clustering segments users into personas based on spending style and risk tolerance, supporting profile-based personalization without labeled training data."
- "Federated learning and local processing mechanisms preserve user privacy while enabling collaborative model training, measurable via Privacy Leakage Ratio."
- "Digital persona modeling enables real-time adaptation to user intent, device usage patterns, financial literacy indicators, and situational stress."

**Limits of relevance:**
- Dataset is simulated, not real Filipino transaction or spending data — performance on actual Filipino young professionals unknown.
- Contextual variables (GPS location, device type) may require permissions not always available or trusted by users in manual-input scenarios.
- No explicit evaluation of cold-start persona generation for new users with zero transaction history.
- Study focuses on general financial decisioning (credit risk, fraud) rather than personal budget management specifically.

---

# Recommendation system for financial decision-making using Artificial intelligence
*by Shuryhin, K. A., Zinovatna, S. L., 2024*

## TL;DR
A system that combines Isolation Forest for anomaly detection, ARIMA and LSTM for budget forecasting, and a large language model to generate personalized, ethically-grounded financial recommendations.

## Topics
A.2 — Existing Personal Finance and Budget Management Systems

C.1 — Budgeting Strategies and Budget Recommendation

C.2 — Budget Recommendation Algorithm

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

E.1 — Anomaly Detection in Personal Finance Systems

E.2 — Anomaly Detection Algorithm

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

## Contribution to Odin
This paper directly validates Odin’s design choice to use Isolation Forest for anomaly detection, as the algorithm requires no labeled training data – a critical advantage for cold‑start users. The hybrid ARIMA+LSTM forecasting approach offers a justified alternative to pure LSTM: ARIMA captures short‑term seasonality (e.g., weekly spending cycles) while LSTM handles irregular long‑term patterns, directly applicable to Odin’s spending forecasting module. The integration of an LLM to generate personalized, non‑judgmental advice informs Odin’s budget recommendation module, particularly the requirement to explain recommendations and respect user autonomy. Finally, the explicit discussion of ethical principles (privacy, fairness, transparency) provides a framework for Odin’s data privacy and user trust requirements, including the use of OAuth 2.0 and privacy‑by‑design.

**Directly justifies:**
- "Isolation Forest detects financial anomalies without requiring labeled training data, making it suitable for cold‑start user profiles where no historical anomaly examples exist."
- "Combining ARIMA (short‑term) and LSTM (long‑term) forecasts via a weighted average captures both seasonal fluctuations and long‑term dependencies, improving forecast stability over either model alone."
- "Large language models can generate personalized financial recommendations by integrating transaction history, forecasted expenses, anomaly flags, and user‑specified risk tolerance and goals."
- "Ethically‑designed recommendation systems must balance AI influence with user autonomy, avoiding manipulation and supporting rational decision‑making through transparent, non‑judgmental advice."
- "OAuth 2.0 and privacy‑by‑design principles (e.g., OWASP Top 10) are essential for securing user financial data and maintaining trust in AI‑powered personal finance systems."

**Limits of relevance:**
- Study is a system design proposal with no empirical evaluation – no accuracy, retention, or usability metrics are reported.
- Population and geography are not specific to the Philippines; spending patterns and financial infrastructure differ.
- The system assumes integration with banking APIs for transaction data; Odin uses manual input only, which may affect data availability and forecast quality.
- The architecture relies on cloud services (AWS SageMaker, SQS) that may not be feasible for a purely mobile‑first, offline‑capable system like Odin.
- No comparison of LLM‑based advice against rule‑based or simpler recommendation methods is provided.

---

# Proof of concept of centralized personal finance application
*by Sipilä, M., 2025*

## TL;DR
A centralized personal finance PoC reduced manual effort and improved data reliability by automating asset tracking, cash flow visualization, and report generation, validated through task-based testing with a stakeholder.

## Topics
A.2 — Existing Personal Finance and Budget Management Systems

J.1 — System Evaluation

## Contribution to Odin
This paper provides a concrete example of designing and evaluating a PFM system using DSRM, directly applicable to Odin’s own development methodology. The evaluation approach — task-based testing with a single stakeholder plus structured questionnaires — offers a low-cost, high-fidelity validation model for Odin’s PoC phase before user recruitment. Although the system lacks AI/ML algorithms, its focus on automation, data integration, and reporting informs Odin’s non‑algorithmic design decisions, such as dashboard layout and report generation.

**Directly justifies:**
- "Task-based user testing with a single stakeholder successfully validated core PFM functionalities, indicating that small-sample qualitative evaluation is feasible for PoC systems."
- "Automated daily exchange rate fetching and stock price retrieval reduced manual update errors in a multi‑currency asset tracking context."
- "Generating PDF reports from aggregated backend data eliminated a multi‑step manual quarterly reporting process, cutting hours of work per cycle."
- "MongoDB’s flexible schema allowed evolving financial data models without schema migrations — a design insight for Odin’s early development."

**Limits of relevance:**
- Single stakeholder (n=1); findings may not generalize to broader Filipino young professional population.
- No ML/AI components; relevance is limited to system design and evaluation methodology, not algorithmic selection.
- European context (Finnish/Swedish financial APIs, multi‑currency needs) differs from Philippine financial infrastructure.
- No user authentication implemented; security claims are untested.

---

# On the human-centered AI transformation of banking: Exploring the impact of behavioral finance & AI on banking transformation
*by van Thiel, D., 2025*

## TL;DR
Integrating psychometric and behavioral finance principles with AI (random forests, neural nets) improves digital advice adoption and inclusive credit scoring, achieving 30% higher approval and 23% lower default rates during market volatility.

## Topics
A.2 — Existing Personal Finance and Budget Management Systems

D.1 — Predictive Modeling in Personal Finance Systems

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

I.1 — User Retention and Engagement in Personal Finance Systems

## Contribution to Odin
This dissertation directly informs Odin’s **predictive modeling module** (D.1) by demonstrating that random forests and neural networks achieve 18–21% higher AUROC than logistic regression for default prediction (Chapter 5), justifying Odin’s algorithm selection for spending forecasting even though the domain is credit risk. The **user profile classification module** (F.1) benefits from the psychometric segmentation model (Chapter 3), which identifies three stable factors (convenience, financial literacy, rigidity) that predict digital advice adoption — applicable to Odin’s four behavioral profiles. The **customer experience findings** (Chapter 2) show that experiential attributes (honesty, reliability, co-creation) drive satisfaction more than price, guiding Odin’s mobile-first design and retention strategies (I.1). Although the study uses Western populations, the psychometric credit scoring model’s ability to predict payment behavior without traditional credit history (Chapter 4, 6) provides a validated method for Odin’s cold-start profiling of new Filipino users.

**Directly justifies:**
- "Random forest models improve AUROC by 18.8–21.3% over logistic regression for individual default prediction across mortgages and credit cards (p < 0.001)."
- "Three psychometric factors — convenience (eigenvalue 1.89), financial illiteracy (1.0), and rigidity (0.51) — segment financial advice users and predict adoption of robo-advisors."
- "Psychometric credit scoring correctly predicts 72.2% of good payers and 67.5% of arrears in low-income consumers (Gini 0.56), enabling cold-start credit assessment."
- "During the COVID-19 state of emergency, psychometric scoring increased approval rates by 30% and lowered default rates by 23% compared to traditional models."
- "Financial skills (−0.57 correlation) and positive debt attitude (+0.22) are the strongest psychometric predictors of payment behavior, more predictive than age or income."

**Limits of relevance:**
- All studies conducted in Western markets (UK, NL, US, CZ); Filipino spending behavior and cultural obligations not directly measured.
- Predictive models focus on credit default (mortgages, credit cards), not spending forecasting — though methodology transfers.
- The AI models tested are random forests and neural networks, not LSTM (Odin’s current forecasting algorithm).
- Some data sources (e.g., credit bureau data in UK experiment) are unavailable in Philippine context.
- Psychometric questionnaires require user self-reporting, which introduces social desirability bias and may not scale as seamlessly as passive behavioral data.

---

# The Role of Big Data Analytics in Behavioral Finance: Understanding Dynamics of Consumer Spending and Saving
*by Whitaker, K., 2025*

## TL;DR
Big data analytics combined with behavioral finance reveals hidden psychological and social drivers of consumer spending and saving, enabling personalized financial products and real-time behavioral interventions.

## Topics
A.2 — Existing Personal Finance and Budget Management Systems

D.1 — Predictive Modeling in Personal Finance Systems

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

## Contribution to Odin
This paper provides a high-level justification for integrating big data analytics into personal finance systems, which directly supports Odin's design rationale. It validates the use of predictive analytics (spending forecasting module) and customer segmentation (user profiling module) based on transaction and behavioral data. Although the paper lacks specific algorithm benchmarks, its emphasis on real-time behavioral nudges and automated savings features aligns with Odin's goal of intelligent, non-gamified engagement. The discussion of privacy concerns (GDPR, consent, anonymization) informs Odin's data governance strategy for Filipino users.

**Directly justifies:**
- "Predictive analytics using historical transaction data can forecast future spending patterns, supporting Odin's spending forecasting module."
- "Clustering algorithms segment consumers by spending habits, enabling behavior-driven user profiles without labeled training data."
- "Automated savings programs that analyze spending patterns improve saving rates with minimal user input — applicable to Odin's budget recommendation logic."
- "Sentiment analysis of social media correlates with discretionary spending, suggesting external data could enhance forecasting accuracy."
- "Algorithmic bias audits are necessary when using ML for financial decisions, directly relevant to Odin's fairness requirements."

**Limits of relevance:**
- Paper is a conceptual review with no empirical results or algorithm comparisons — cannot justify LSTM over GRU or Isolation Forest over other methods.
- No Philippine-specific data or cultural context; Filipino spending/ saving patterns may differ from Western assumptions.
- Recommends data sources (social media, open banking) that Odin does not use (manual input only).
- Privacy discussion focuses on GDPR/CCPA, not Philippine data privacy law (R.A. 10173).

---

# Study of an Adaptive Financial Recommendation Algorithm Using Big Data Analysis and User Interest Pattern with Fuzzy K‑Means Algorithm
*by Yang, J., 2024*

## TL;DR
Fuzzy K-means clustering with neural collaborative filtering improves financial product recommendation accuracy and clustering quality compared to existing methods.

## Topics
C.2 — Budget Recommendation Algorithm

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

F.2 — Profile Classification Algorithm

## Contribution to Odin
This paper directly informs Odin’s user profile classification module by demonstrating that fuzzy K-means clustering effectively segments users based on financial behavior patterns without requiring hard cluster boundaries. The neural collaborative filtering approach provides a viable algorithm candidate for Odin’s budget recommendation module, as it learns from user interaction data (e.g., spending choices) and adapts to changing preferences over time. Although the paper focuses on investment products, the same hybrid architecture (clustering + neural recommendation) can be repurposed for spending category recommendations and budget allocation. The use of Hadoop MapReduce for scalability is less relevant for Odin’s mobile-first scope, but the algorithm’s linear processing time justifies feasibility on smaller datasets.

**Directly justifies:**
- "Fuzzy K-means clustering achieves a silhouette coefficient of 0.690, demonstrating that financial users can be segmented into distinct, well-separated behavioral profiles without crisp boundaries."
- "Neural collaborative filtering (NCF) with multi-layer perceptron reduces MSE by approximately 20% compared to ANFIS on financial recommendation tasks."
- "Combining fuzzy clustering with NCF improves Precision@5 to 0.85, significantly outperforming static collaborative filtering methods."
- "The adaptive user profile approach updates recommendations in real time as new interaction data arrives, addressing concept drift in user financial behavior."

**Limits of relevance:**
- Paper addresses investment product recommendations, not budget allocations per spending category — the mapping is methodological, not domain-identical.
- Dataset and user profiles are not Filipino; no validation on Philippine spending patterns or income typology.
- Assumes availability of rich interaction history (binary interest matrix); Odin’s manual transaction input may yield sparser data.
- No evaluation of cold-start performance for new users with zero history — a key Odin requirement.

---

# Leveraging Big Data Analytics in Behavioral Finance: Insights into Consumer Spending and Saving Dynamics
*by Ying, H., Blaise, M., 2025*

## TL;DR
Big data analytics uncovers psychological and behavioral drivers of spending and saving, enabling personalized financial strategies through machine learning and predictive models.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

D.1 — Predictive Modeling in Personal Finance Systems

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

## Contribution to Odin
This paper provides high-level justification for Odin’s reliance on behavioral insights rather than purely rational economic models. It supports the use of predictive analytics (Odin’s forecasting module) and customer segmentation (Odin’s user profiling module) as valid approaches in personal finance systems. The discussion of data privacy and algorithmic bias informs Odin’s design requirements for transparency and user trust, though the paper offers no specific implementation guidance.

**Directly justifies:**
- “Consumer spending is influenced by cognitive biases and emotional factors, not just rational economic calculations — justifying Odin’s behavioral profiling approach.”
- “Clustering algorithms can segment customers based on spending habits, enabling personalized financial strategies applicable to Odin’s user profile classification.”
- “Automated savings programs that analyze spending patterns and transfer small amounts increase saving without user effort — a potential design cue for Odin’s budget recommendation.”
- “Predictive analytics using historical transaction data can forecast future spending behaviors, supporting Odin’s LSTM-based forecasting module.”

**Limits of relevance:**
- The paper is a conceptual review with no empirical data, benchmarks, or algorithm comparisons — it provides no quantitative evidence for any claim.
- All examples and case studies are from large financial institutions (Chase, Capital One) or retailers (Amazon, Walmart), not personal budget management systems for individuals.
- No Filipino or Southeast Asian context is discussed; spending and saving behaviors may differ culturally.
- The paper assumes access to rich transaction data and banking integration, while Odin relies on manual input only.

---

# Cash Management Practices and the Financial Performance of Micro-Enterprises
*by Aguilar, T. S., Chavez, M. M., Rayos, C. M. D., Remoquin, K. J. A., Melo, M. C. F., 2024*

## TL;DR
Proper budgeting and cash flow management strongly correlate with higher sales growth, profitability, and liquidity in 163 Philippine micro-enterprises.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

C.1 — Budgeting Strategies and Budget Recommendation

## Contribution to Odin
This paper documents specific budgeting gaps among Filipino micro‑enterprise owners—not sticking to budgets, irregular cash flow reviews, and difficulty converting assets to cash—which mirror likely challenges for Filipino young professionals using a personal budget app. The finding that structured budgeting correlates strongly with financial performance (rho up to 0.536) justifies Odin’s investment in budget recommendation features that encourage adherence, not just allocation. Although the study targets enterprises, its identified failure points (e.g., not updating cash flow plans, spending more than earned) directly inform Odin’s design requirements for simple, behavior‑focused nudges and real‑time feedback.

**Directly justifies:**
- “Micro‑enterprise owners who stick to prepared budgets show significantly higher profitability (rho = 0.536) and liquidity (rho = 0.526).”
- “Cash flow management—especially monitoring inflows and outflows—has a stronger relationship with sales growth (rho = 0.648) than budgeting does.”
- “The weakest cash management practice among Filipino micro‑enterprises is adjusting cash flow plans when needed (mean 2.58/4), indicating a need for automated adjustment tools.”

**Limits of relevance:**
- Study population is micro‑enterprise owners (business context), not young professionals managing personal finances; behavioral drivers may differ.
- No algorithm or ML method is evaluated; relevance is to user needs and budgeting strategy, not to specific models.
- Survey data are self‑reported and cross‑sectional; causality is not established.
- Geographic scope is rural Oriental Mindoro; Metro Manila young professionals may face different income volatility and expense patterns.

---

# Wealth Creation for Expanding the Middle Class in the Philippines
*by Albert, J. R. G., Briones, R. M., Rivera, J. P. R., 2024*

## TL;DR
The Philippine middle class, defined as households with per capita income 2–12 times the poverty line, grew to **39.8%** of the population by 2021 but the pandemic reversed gains from the 43.5% peak in 2018.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

G.1 — Expense Categorization in Filipino Personal Finance Contexts

## Contribution to Odin
This paper provides empirically grounded baseline data on how Filipino households across income classes allocate spending, directly informing Odin’s expense categorization module grounded in FIES categories. The income typology (2–12x poverty line) helps define the target user segment — young professionals likely fall into lower-middle to middle-middle income ranges, with predictable expenditure shares on food, transport, health, and education. The finding that 79.5% of middle-class workers hold permanent jobs supports Odin’s spending forecasting module assumption of stable income patterns, while OFW remittance data (8.5% of income) highlights an irregular income source that must be handled by both forecasting and anomaly detection. Although the paper is macroeconomic, its micro-level household expenditure breakdowns are directly citable for justifying Odin’s category structure and spending pattern baselines in the Philippine context.

**Directly justifies:**
- “As of 2021, 39.8% of Filipinos belong to the middle class, with average family size 3.6 — smaller than low-income families — indicating higher discretionary spending capacity per capita.”
- “Middle-class households allocate 8.8% of expenditure to transportation, 3.2% to health, and 1.3% to education, providing baseline category weights for Odin’s budget recommendation logic.”
- “40.6% of middle-class Filipinos aged 15+ have completed college, suggesting digital literacy and readiness for mobile-first financial management tools.”
- “OFW remittances contribute 8.5% of total income for middle-class families — an irregular income stream that Odin’s forecasting and anomaly detection modules must accommodate.”
- “The COVID-19 pandemic reduced the middle-class share from 43.5% (2018) to 39.8% (2021), demonstrating income shock vulnerability that Odin’s anomaly detection should monitor as behavioral deviation.”

**Limits of relevance:**
- The paper focuses on macroeconomic wealth creation policy, not personal budget management systems or mobile app design.
- Data is from 2021, post-pandemic disruptions may not represent long-term stable spending patterns for young professionals.
- Income-based classification does not directly map to Odin’s behavioral profiles (Stable-Flexible, Variable-Obligated, etc.).
- No analysis of digital financial app usage or transaction-level data — only survey aggregates.
- The middle class definition includes older adults (not limited to 20–40 age range), so per-category spending shares may differ for young professionals specifically.

---

# Budgeting Practices Among Below Minimum Wage Earners: A Case Study of Sales Personnel of Local Enterprises in Pagadian City
*by Alvarina, C. C., Handumon, H. O., Peralta, J. M. B., Paguia, M. A., Alfanta, M. P., 2025*

## TL;DR
Below-minimum-wage sales personnel in Pagadian City prioritize essentials (food, utilities, childcare) and supplement income through side hustles, demonstrating tight budgeting and emergency savings despite financial stress.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

C.1 — Budgeting Strategies and Budget Recommendation

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

## Contribution to Odin
This paper directly informs Odin’s understanding of how low-income Filipino workers prioritize spending (childcare, food, utilities), which can guide the expense categorization module (G.1) and default budget templates for users with constrained incomes. The documented coping strategies—tight budgeting, expense tracking, and emergency fund creation—validate the need for Odin’s budget recommendation module to emphasize essential costs and savings goals rather than discretionary optimization. Although Odin targets young professionals in Metro Manila, the behavioral patterns of below-minimum-wage earners provide a lower-bound reference for financial stress and resource allocation, useful for profiling extreme cases.

**Directly justifies:**
- “Below-minimum-wage sales personnel in Pagadian City allocate budget to childcare (10/10), food (9/10), and utilities (6/10), reflecting essential spending hierarchies in low-income Filipino households.”
- “Workers supplement primary salary through government aid, online selling, thrift items, and side dishes, demonstrating income diversification as a coping strategy.”
- “Challenges include managing multiple expenses (5/10), limited healthcare access (3/10), and insufficient savings (2/10), highlighting common budget failure points among low earners.”
- “Positive budgeting practices—tracking expenses, utilizing resources, and creating emergency funds—improve financial well-being even under low income.”

**Limits of relevance:**
- Study focuses on below-minimum-wage earners, while Odin targets young professionals (20–40) who may have higher disposable income.
- Small sample size (n=10) and single city (Pagadian City) — findings may not generalize to Metro Manila.
- Qualitative design provides no statistical validation or algorithm-relevant data for Odin’s ML modules (forecasting, anomaly detection, classification).
- Demographic age range unspecified; not limited to young professionals.

---

# Beyond Awareness: Examining Financial Behaviors Among Public School Teachers in the Philippines
*by Am-una, A., 2026*

## TL;DR
Public school teachers in Baguio City show moderately positive financial behaviors, but these reflect "conscious constraint"—disciplined management of scarce resources—not true financial security.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

C.1 — Budgeting Strategies and Budget Recommendation

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

## Contribution to Odin
This paper directly informs Odin's user profiling and budget recommendation modules by documenting how Filipino earners experience budgeting as high-friction under income constraints—a finding that justifies Odin's focus on reducing behavioral friction over pure financial education. The identification of "conscious constraint" (disciplined management without surplus) provides a behavioral baseline for Odin's profile classification: users may report "good" budgeting habits not from mastery but from necessity, which affects how the anomaly detection module interprets overspending. The finding that marital status and employment rank significantly affect financial behavior supports Odin's decision to include these demographic variables in user profile classification rather than relying solely on spending patterns.

**Directly justifies:**
- "Budgeting is performed at moderately positive levels (M=2.68) but perceived as the most difficult financial behavior (M=2.17), indicating that frequency of budgeting does not measure financial mastery."
- "No significant difference in financial behaviors between seminar attendees and non-attendees (p=.991) demonstrates that awareness-driven financial education alone does not change behavior under structural income constraints."
- "Married teachers exhibit significantly lower financial behavior scores than single teachers (p=.034) due to household financial obligations, not lack of knowledge."
- "Master Teachers (higher rank) achieve higher financial behavior scores (M=3.00) than non-Master Teachers (M=2.65) through accumulated financial capacity, not just knowledge."

**Limits of relevance:**
- Study population is public school teachers, not the target Filipino young professional demographic (ages 20–40) in Metro Manila; income and obligation structures may differ.
- Data collected in Baguio City only; spending patterns and cost-of-living pressures may not generalize to Metro Manila.
- No evaluation of any ML or algorithmic approach—behavioral findings only, not method-specific.
- Cross-sectional design cannot establish causality between demographic factors and behavior changes.

---

# Analysis of the Food and Income Expenditure Survey 2023 Among Filipino Households
*by Ama, N. A., 2025*

## TL;DR
Food spending is income‑inelastic (elasticity = 0.58) — as Filipino household income rises 1%, food expenditure rises only 0.58%, confirming Engel’s Law.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

G.1 — Expense Categorization in Filipino Personal Finance Contexts

## Contribution to Odin
This paper provides empirical, nationally representative data on how Filipino households actually spend on food across categories (bread 29.5%, meat 14.8%, fish 14.2%), directly grounding Odin’s expense categorization module in local FIES behavior rather than Western assumptions. The PCA‑derived income source typology (retail/transport, farming, fishing, remittances, informal services) offers a data‑driven foundation for Odin’s user profile classification — enabling the system to distinguish users by dominant income type, which affects spending volatility and budget recommendation needs. The Engel curve elasticity (0.58) quantifies how spending on food (a necessity) scales with income, which can calibrate Odin’s spending forecasting module: lower‑income users will allocate a larger share of any income increase to food, while higher‑income users shift proportionally more to non‑food categories. The finding that rural households spend more on food and have higher per capita income than urban households challenges simple income‑based assumptions and suggests Odin must incorporate geography and cost‑of‑living adjustments.

**Directly justifies:**
- “Filipino households allocate 29.5% of total food expenditure to bread, 14.8% to meat, 14.2% to fish, 7.2% to vegetables, and 4.5% to fruit (2023 FIES, n=163,268).”
- “Income elasticity of food demand among Filipino households is 0.58 — a 1% income rise increases food spending only 0.58%, confirming food as a necessity (Engel’s Law).”
- “Principal Component Analysis of 10 income sources reveals five distinct livelihood clusters: retail/transport, informal/miscellaneous, crop farming (positive vs. fishing negative), forestry vs. remittances, and remittances/forestry — these can inform user profiling.”
- “Rural households have higher median per capita income (₱6,000) and higher food spending (₱102,467) than urban households (₱5,000 and ₱80,700), indicating geography‑dependent spending patterns that a budget system must account for.”
- “Generalized Additive Model (AUC 0.86) shows household size, per capita income, and urban/rural status have strong nonlinear effects on food insecurity — similar nonlinearities likely affect budget adherence.”

**Limits of relevance:**
- The study covers all Filipino households, not specifically young professionals (20–40) — spending patterns may differ for this subset.
- Data are from 2023, but Odin targets current and future users; spending shares may shift with inflation or post‑pandemic recovery.
- Food expenditure categories are broad (e.g., “meat” and “bread”) — Odin needs more granular categorization (e.g., restaurant vs. grocery, specific subtypes).
- The paper does not analyze discretionary vs. non‑discretionary spending thresholds, which are central to budgeting.

---

# The plight of teachers on the twice-a-month salary release: Financial literacy and survival
*by Amado, M. A., 2026*

## TL;DR
Twice-a-month salary release improves short-term financial planning for teachers, but financial stress persists; higher financial literacy directly enables better budgeting and survival strategies.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

C.1 — Budgeting Strategies and Budget Recommendation

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

## Contribution to Odin
This paper provides empirical evidence on how income regularity (twice-a-month) affects budgeting behavior and financial stress among Filipino salaried professionals — directly informing Odin’s assumptions about user income patterns. The finding that financial literacy moderates management effectiveness (mean 4.21 for literate teachers vs. baseline) supports Odin’s design priority of embedding financial education within the app rather than assuming user literacy. The documented survival strategies (strict expense prioritization at mean 4.46, supplementary income seeking at 3.87) define baseline user behaviors that Odin’s budget recommendation and anomaly detection modules must accommodate or improve.

**Directly justifies:**
- "Twice-a-month salary release yields an overall perceived financial well‑being score of 4.18 (Agree) among Filipino teachers, indicating improved short‑term planning but persistent stress between pay periods."
- "Financial literacy positively influences financial management under bi‑monthly pay (overall mean 4.21), with higher‑literacy teachers better handling unexpected expenses (mean 4.37)."
- "Teachers prioritize essential expenses over non‑essentials (mean 4.46) as the primary coping strategy, more than any other financial behavior."
- "Despite perceived advantages (overall 4.23), financial stress between pay periods remains (mean 3.63 for 'increases likelihood of stress')."
- "Teachers actively seek supplementary income (mean 3.87) and financial advice (mean 3.90) as survival mechanisms between salary releases."

**Limits of relevance:**
- Study population is public school teachers, not the broader young professional demographic; income levels and spending priorities may differ from Odin’s target users.
- Geography is Claveria North District (Masbate), which may not fully represent Metro Manila’s cost of living and financial behavior.
- Descriptive survey design only — no causal inference; self-reported perceptions may not reflect actual transaction-level behavior.
- No comparison to other salary frequencies (e.g., once‑monthly) within the same sample, limiting claims about relative advantage.
- Does not evaluate digital financial tools or app‑based interventions, only non‑digital coping strategies.

---

# Peer Influence and Adolescent Spending: Insights into High School Students’ Buying Behavior
*by Anaya, K. K. O., Piquero, J. R. M., Romero, C. J. P., Sales, Y. L. M., Suñga, P. A. N., Ibañez, M. M., Ramos, R. I. A., Asi, G. M., 2024*

## TL;DR
Implicit peer pressure shows a weak positive correlation (r = 0.273) with impulsive buying among Filipino senior high school students, explaining only 7.45% of the variance.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

## Contribution to Odin
This paper provides empirical evidence on Filipino adolescent spending behavior, specifically the weak but significant link between implicit peer pressure and impulsive buying. Although Odin targets young professionals (20–40), the findings inform the behavioral profiling module (F.1) by identifying social influence as a measurable dimension of spending patterns. The result that peer pressure explains only 7.45% of variance reinforces that Odin’s profile classification must incorporate multiple stronger predictors (e.g., income type, financial literacy) rather than over-weighting social factors. Additionally, the study’s use of a Filipino sample grounds its claims in the local context, making it more applicable than purely international studies.

**Directly justifies:**
- “Implicit peer pressure explains only 7.45% of the variance in impulsive buying among Filipino senior high school students (R² = 0.0745, p = 0.004).”
- “Filipino SHS students exhibit moderate impulsive buying behavior (M = 3.06 on a 5‑point scale), indicating that unplanned purchases are a regular but not dominant feature of their spending.”
- “Low implicit peer pressure overall (M = 2.24) suggests that Filipino adolescents rarely feel compelled to spend to maintain social status, challenging assumptions that peer influence is a primary driver of youth spending.”
- “The strongest impulse trigger among Filipino students is seeing a good deal (M = 3.43), not peer pressure — highlighting the role of marketing and perceived value over social conformity.”

**Limits of relevance:**
- Demographic mismatch: high school students vs. Odin’s target of young professionals (20–40); spending priorities and income sources differ substantially.
- Single faith‑based institution in Cavite, not representative of all Filipino young adults.
- Weak effect size (r = 0.273) limits the practical utility of peer pressure as a standalone predictor in Odin’s models.
- No financial literacy or budgeting behavior measured — the paper does not address budget adherence or forecasting.

---

# Martime Students’ Financial Knowledge, Attitude, and Behavior
*by Apao, A. A., Cayanpat, R. A. B., Edullantes Jr., Y. P., Cabañero, K. E. S., Hechanova, J. M. T., Candia, H. G., 2025*

## TL;DR
High financial knowledge and positive attitudes among Filipino maritime students do not translate into better financial behavior, revealing a gap between knowing and doing.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

## Contribution to Odin
This paper directly informs Odin's user profiling module by demonstrating that financial knowledge and positive attitudes are weak predictors of actual spending behavior among Filipino young adults. The finding that maritime students report “Very High” behavior yet show no statistically significant link to knowledge or attitude suggests that self‑reported financial discipline may not reflect real‑world actions — a critical insight for Odin’s behavior‑driven profile classification. The knowledge‑behavior gap justifies Odin’s design choice to rely on observed transaction data (e.g., anomaly detection, spending forecasting) rather than self‑assessed literacy or attitude surveys.

**Directly justifies:**
- “Financial knowledge and financial behavior showed a non‑significant negative correlation (r = -0.46, p = 0.652) among Filipino maritime students, indicating that knowing financial concepts does not translate into responsible money management.”
- “Financial attitude and financial behavior were positively but not significantly correlated (r = 0.59, p = 0.558), meaning even positive money mindsets fail to reliably produce better financial habits.”
- “Mean self‑reported financial behavior was 3.85 (Very High), yet no statistically meaningful relationship existed with either knowledge or attitude — self‑assessment is a poor proxy for actual behavior.”
- “Parental influence and informal learning produced high knowledge and attitude scores, but structured financial education with practical application is needed to close the behavior gap — supporting Odin’s active nudging over passive advice.”

**Limits of relevance:**
- Study population is maritime students, not the full spectrum of Filipino young professionals (ages 20–40); income patterns (lump‑sum seafarer pay) may not generalize.
- All measures are self‑reported Likert scales; no objective transaction data was collected, so actual behavior may differ from claimed behavior.
- Sample size (n=100) from a single private institution limits generalizability to lower‑income or non‑maritime young Filipinos.
- No longitudinal data — the study cannot determine whether the knowledge‑behavior gap persists after students enter the workforce.

---

# The Impact of Psychological, Economic, Social Aspects, and Interest Rate Variations on Working Millennials' Saving Patterns Through Digital Banking
*by Ataza, C., Porcel, M., Resabal, L., Sandoval, A., Bragas, C., 2024*

## TL;DR
Interest rate variations (β=0.878) and psychological aspects (β=0.430) significantly increase saving patterns of working millennials via digital banking, but social aspects decrease it (β=-0.182).

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

## Contribution to Odin
This paper provides empirical evidence on factors that drive saving behavior among Filipino working millennials, directly informing Odin’s user profile classification module. The finding that psychological aspects (self-control, financial anxiety, planning horizon) significantly affect saving patterns justifies incorporating psychological constructs into Odin’s profile dimensions. The negative effect of social aspects suggests that Odin should prioritize personal financial goals and avoid over‑relying on social comparison features, which could backfire. Interest rate sensitivity, while not directly controllable by Odin, indicates that the budget recommendation module could frame surplus allocation in terms of “future returns” (e.g., savings growth) to motivate user action. Although the study focuses on saving rather than spending, its behavioral insights are directly transferable to budgeting and expense management.

**Directly justifies:**
- “Psychological aspects (β=0.430, p=0.006) have a significant positive effect on saving patterns of working millennials using digital banking (Ataza et al., 2024).”
- “Interest rate variations (β=0.878, p<0.001) are the strongest predictor of saving patterns, explaining 70% of variance in the model.”
- “Social aspects (β=-0.182, p=0.016) negatively affect saving patterns, meaning higher social influence reduces saving behavior among Filipino working millennials.”
- “Economic aspects such as income stability and employment status were not significant predictors of saving patterns in this sample (p=0.293).”
- “The full regression model (psychological, economic, social, interest rate) explains 75.34% of variance in saving patterns, demonstrating the importance of multi‑factor behavioral models.”

**Limits of relevance:**
- Small sample size (N=51) and purposive sampling limit generalizability to all Filipino young professionals.
- Study measures saving patterns, not spending or budgeting behavior; Odin focuses on budget adherence, which may have different drivers.
- No longitudinal data; causal claims cannot be made from this cross‑sectional survey.
- All data are self‑reported Likert scales, subject to social desirability and recall bias.
- Sample drawn only from Metro Manila; rural or other urban Filipino populations may differ.

---

# Peso By Peso: Comparing Adaptive Practices of Solo Parents Across Income Levels in Balanga City, Bataan, and Olongapo City, Zambales
*by Avelino, Z. L., Piol, J. A. S., Gutierrez, W. B., Ibabao, E. J. A., Fadera, D. T., 2026*

## TL;DR
Income level significantly affects solo parents' financial management and lifestyle modifications (p<.001), with Olongapo City respondents showing stronger adaptive behaviors than those in Balanga City.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

## Contribution to Odin
This paper directly informs Odin's understanding of how income level drives financial adaptation among Filipino solo parents, a demographic that overlaps with Odin's target young professionals (ages 25–34 comprise 59% of respondents). The finding that lower-income individuals modify financial practices more aggressively supports Odin's need for income-typology-aware budgeting recommendations. The observed 0.515 correlation between financial adaptation and work-child balance difficulties suggests that user profile classification must incorporate non-financial life constraints. Although the study is not about digital finance apps, its quantitative evidence on income-behavior differences validates Odin's decision to segment users by income bracket and tailor budget recommendations accordingly.

**Directly justifies:**
- "Income level has a highly significant effect on financial management and lifestyle modifications among Filipino solo parents (χ²(5)=47.4, p<.001)."
- "Solo parents earning below ₱10,000/month engage in more aggressive budget cutting and secondary income seeking than higher-income brackets."
- "Perception of government support varies significantly by income level (χ²(5)=23.6, p<.001), indicating that program design must account for income-based access barriers."
- "Olongapo City solo parents report stronger adaptive financial behaviors (mean 3.52) than Balanga City (mean 2.45), demonstrating that geographic and governance context shapes financial coping strategies."
- "Financial adaptation strongly correlates with difficulties balancing work and child education (ρ=0.515), suggesting that lifestyle constraints directly influence how users manage their finances."

**Limits of relevance:**
- Study focuses on solo parents, not exclusively on young professionals; age overlap exists (25–34) but parenthood status may change spending priorities.
- No evaluation of digital or mobile financial tools — all data from survey self-reports of general financial behavior.
- Sample includes many informal-sector workers (vendors, factory workers); Odin targets professionals with potentially more stable income patterns.
- Findings are descriptive correlations, not causal; no algorithm or ML method is tested or proposed.
- Geographic scope limited to two Luzon cities; may not generalize to other Philippine regions.

---

# Consumer Finance Survey Report 2021
*by Bangko Sentral ng Pilipinas, 2021*

## TL;DR
Filipino households earned ₱190k average annual income in 2021, spent 55% of it on food at home, held ₱435k median net worth, and only 29% carried debt.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

D.1 — Predictive Modeling in Personal Finance Systems

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

G.1 — Expense Categorization in Filipino Personal Finance Contexts

## Contribution to Odin
This survey provides the authoritative empirical baseline for Filipino household spending patterns, income sources, and asset ownership, directly grounding Odin’s expense categorization module (G.1) in the PCOICOP framework used by the Philippine government. The detailed per-category expenditure shares (e.g., 55.4% food at home, 10.6% housing+utilities) supply realistic priors and validation targets for Odin’s spending forecasting (D.1) and budget recommendation algorithms. The income typology (wage, entrepreneurial, government transfers) and demographic profiles (age, education, health insurance) inform user profiling (F.1) and cold-start behavior assumptions. The finding that 92.8% own mobile phones but only 35.3% have bank accounts strongly justifies Odin’s mobile-first, manual-input, no-banking-integration design.

**Directly justifies:**
- "Filipino households allocated 55.4% of total expenditure to food at home in 2021, making it the single largest budget category and a mandatory anchor for any budget recommendation system targeting this population."
- "Only 29.3% of households carried any debt, with past due bills (16.4%) more common than formal loans (15.2%) — anomaly detection in Odin should prioritize budget overage alerts over debt-based indicators."
- "Mobile phone ownership reached 92.8% while deposit account ownership was only 35.3% — Odin’s mobile-first, manual transaction input design matches actual Filipino financial behavior."
- "Average annual PEU income was ₱189,842 (median ₱144,000), with 40.4% of respondents aged 25-44 — this income range defines the target young professional segment for Odin."
- "The survey’s expenditure categories follow the 2020 PCOICOP, which aligns with FIES and BSP Consumer Finance Survey — Odin can directly adopt these category definitions for local regulatory alignment."

**Limits of relevance:**
- Survey covers all Filipino households, not specifically young professionals; young-adult subset extraction is possible but not pre-aggregated.
- Data collected during COVID-19 pandemic (2021) may overstate emergency government transfers and understate normal discretionary spending.
- No algorithmic or predictive modeling is presented; the relevance is purely descriptive and foundational for category design and baseline statistics.
- Geographic granularity is at regional/urban-rural level, not at the individual user level needed for personalization calibration.

---

# CONSUMER EXPECTATIONS SURVEY REPORT 1st Quarter 2026
*by Bangko Sentral ng Pilipinas, 2026*

## TL;DR
Filipino consumer sentiment improved in Q1 2026 but spending outlook softened, with the saving intention index rising to **12.4%** and year-ahead inflation forecast at 2.7%.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

G.1 — Expense Categorization in Filipino Personal Finance Contexts

## Contribution to Odin
This BSP survey provides primary empirical data on Filipino household spending intentions, saving rates, and income‑group differences — directly grounding Odin’s spending categories and budget recommendation baselines in local behavior. The finding that 73.9% of savers allocate less than 10% of income to savings (and only 40.2% of OFW households save at all) justifies Odin’s focus on low‑touch, high‑value recommendations rather than aggressive saving goals. Spending outlook declines across food, transport, and personal care categories signal where young professionals may be most price‑sensitive, informing per‑category budget constraints.

**Directly justifies:**
- “73.9% of Filipino households that save put aside less than 10% of monthly income — budget recommendation algorithms must assume very low savings elasticity.”
- “Spending outlook for Q2 2026 fell most sharply for food (−7.4 ppt), transportation (−4.0 ppt), and personal care (−3.9 ppt), while water and electricity outlook improved — critical for setting realistic per‑category spending thresholds in a Philippine PFMS.”
- “High‑income households (40.3% of sample) had current‑quarter CI of -7.9%, compared to -24.7% for low‑income households — profile classification must separate income‑group expectations.”
- “Only 40.2% of OFW‑receiving households allocate remittances to savings, and just 17.1% to house purchase — most remittances go to immediate needs (food: 96.1%, education: 69.9%).”

**Limits of relevance:**
- Survey covers all Filipino households, not specifically young professionals aged 20–40; income bands may not align exactly with Odin’s target demographic.
- Expectations data (intentions) may not match actual spending behavior; Odin uses transaction history for forecasting, not survey proxies.
- No granular transaction‑level data — cannot derive category spending distributions; only directional changes are reported.
- Inflation and interest rate expectations are aggregate, not tied to individual spending categories.

---

# Street Vendors' Stories: Informal Borrowing Practices and Implications on Business
*by Bara-Labitad, J., 2025*

## TL;DR
Filipino street vendors borrow PHP 5,000–10,000 from "5-6" lenders at 20% interest over two months, gaining short-term inventory benefits but facing debt cycles and financial strain.

## Topics
None — contextual only.

## Contribution to Odin
This paper does not contribute to any Odin module. It describes informal borrowing practices of street vendors in a Philippine public market, a demographic and context distinct from Odin's target users (young professionals aged 20–40 in Metro Manila). The paper contains no AI, ML, or statistical models applicable to spending forecasting, anomaly detection, budget recommendation, user profiling, or expense categorization. Its findings on financial exclusion and debt cycles, while relevant to Filipino financial behavior broadly, do not provide algorithmic justifications, design decisions, or evaluation methods that Odin's RRL would cite. The paper's methodology (descriptive statistics, thematic analysis) and subject matter (informal lending, not personal budget management) fall outside Odin's scope.

**Directly justifies:**
None — this paper does not provide citable claims that directly justify any Odin design decision.

**Limits of relevance:**
Not applicable — paper is outside Odin's scope.

---

# Do Remittances Boost Household Spending: New Evidence from Migrants’ Household Survey
*by Bayangos, V. B., Lubangco, C. K., 2024*

## TL;DR
Remittances boost household spending in the Philippines, but poor households face binding financial constraints that limit welfare gains, and high transfer costs reduce remittance inflows.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

G.1 — Expense Categorization in Filipino Personal Finance Contexts

## Contribution to Odin
This paper directly informs Odin's user profiling (F.1) by demonstrating that income status (poor vs non-poor) fundamentally changes how additional funds are allocated — poor households cannot shift from food to education/health even when receiving remittances. This finding justifies a design priority for Odin's budget recommendation module: the algorithm must account for binding financial constraints and not assume fungibility for users with low discretionary income. The paper also provides empirical budget shares for FIES-aligned spending categories (food, education, health, housing, durable goods, clothing), which validates Odin's choice of FIES/BSP as the categorization grounding (G.1). Finally, the observed heterogeneity in saving/investing behavior by migrant status and education level supports Odin's need for behavior-driven profile classification rather than static demographic rules.

**Directly justifies:**
- "Poor Filipino households exhibit binding financial constraints: remittance receipts do not increase education or health spending shares, while non-poor households show significant increases of 0.40–0.50 percentage points."
- "50% of OFW households allocate nothing to savings, and 75% allocate nothing to investments — immediate consumption dominates, with over 90% of cash remittances spent directly."
- "Higher regional unemployment rates increase remittance inflows (altruistic motive), while higher regional wages reduce them — indicating that household financial vulnerability drives remittance dependence."
- "OFWs save more than immigrants (10.35% vs 7.40%), supporting the exchange motive: migrants intending to return remit more for future liquidity."

**Limits of relevance:**
- Study focuses on remittance-receiving OFW households, not the general population of Filipino young professionals (age 20–40 non-migrant workers).
- No ML or algorithmic methods — findings are behavioral/economic, not directly applicable to algorithm selection for forecasting or anomaly detection.
- Spending data is cross-sectional (FIES 2018/2021), not time-series, limiting claims about dynamic budgeting behavior.
- Remittance context differs from earned income — Odin users rely on salary/wages, not external transfers, which may change spending elasticity.

---

# Influence of Digital Wallets on the Financial Behavior of HEI's Students
*by Bongado, M. B., Magallanes, A. R., Semaña, C. M., 2025*

## TL;DR
Digital wallet use explains 45.4% of variance in financial behavior among Filipino HEI students, with positive effects on cash management and budgeting.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

I.1 — User Retention and Engagement in Personal Finance Systems

## Contribution to Odin
This paper provides empirical evidence that Filipino students perceive digital wallets as easy to use and useful, and that such perceptions positively correlate with responsible financial behaviors like budgeting and cash management. For Odin's budget recommendation and expense categorization modules, the finding that digital wallet usage explains 45% of financial behavior variance supports the value of integrating mobile-first financial tools with active budgeting features. The strong role of perceived trust and security (mean = 2.99, albeit with high variability) underscores the importance of transparent privacy and security design in Odin to drive adoption and sustained use.

**Directly justifies:**
- "Digital wallet usage accounts for 45.4% of variance in financial behavior among Filipino HEI students (R² = 0.454, p < .001), indicating a substantive link between mobile financial tools and budgeting discipline."
- "Perceived ease of use, usefulness, and trust are key determinants of digital wallet adoption in the Philippine student population, with mean agreement scores of 2.95–2.99 on a 4-point scale."
- "Students who report stronger intention to use digital wallets also demonstrate higher levels of cash management and financial planning (β = 0.673, p < .001)."
- "Perceived trust shows the widest variability (SD = 1.24), suggesting that trust-building features are critical for user acceptance of financial apps in the Philippines."

**Limits of relevance:**
- Study population is HEI students, not young professionals (Odin's target), though both are digital-native Filipinos with similar financial behaviors.
- Focuses on general financial behavior (cash management, budgeting) rather than specific ML-based forecasting or anomaly detection.
- Cross-sectional design cannot establish causality; Odin would rely on this as correlational evidence only.
- No direct evaluation of budgeting algorithms or recommendation systems — only user-reported behavior.

---

# The Traditional Way of Saving Money Versus the Modern Style of Investment: The Financial Management Styles of Sorsogon State University (Sorsu) Bulan Campus Faculty Members
*by Bongalonta, M. B., Bongalonta, M. M., Gigantoca, S. E., 2024*

## TL;DR
Filipino university faculty save using both traditional (piggy banks, paluwagan, bank deposits) and modern methods, but rising costs, low financial literacy, poor debt management, and delayed salaries limit **60% to saving only 0–15% of income**.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

C.1 — Budgeting Strategies and Budget Recommendation

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

## Contribution to Odin
This paper provides empirical evidence on actual saving behaviors, budgeting practices, and financial pain points of Filipino professionals (university faculty). It directly informs Odin’s user profiling module (F.1) by documenting that users often save only after expenses (“expense‑first” budgeting), rely on informal mechanisms like paluwagan, and face high debt and utility costs that crowd out savings. For the budgeting strategy and recommendation module (C.1), the finding that 60% save ≤15% of income and that variable/unexpected expenses are a primary barrier justifies designing adaptive budget recommendations that prioritize emergency fund building and automated “save first” nudges. Although the sample is faculty (not young professionals), the behavioral patterns are generalizable to Filipino professionals with regular salary income.

**Directly justifies:**
- “60% of Filipino state university faculty save only 0–15% of monthly income, with the majority using expense‑first budgeting (savings = income – expenses) rather than saving first.”
- “Increasing cost of utilities and unexpected day‑to‑day expenses are the most frequently cited barriers to saving, overwhelming any fixed savings plan.”
- “Poor debt management (loans from GSIS and Land Bank) consumes most of the salary before it is received, leaving minimal or no savings.”
- “Informal saving mechanisms (paluwagan, piggy bank) remain prevalent, but paluwagan often leads to default and debt rather than net saving due to lack of regulation.”

**Limits of relevance:**
- Sample is university faculty (majority aged 35–50, permanent), not the target 20–40 young professional range; income stability and expense composition may differ.
- No evaluation of any AI, ML, or algorithmic system; findings are purely descriptive.
- Self‑reported financial data may understate debt or overstate saving intentions.
- Geography: Sorsogon (provincial) vs. Metro Manila; cost structures and financial access vary.

---

# Financial Management Practices of Employees at Bureau Of Internal Revenue
*by Cabiles, S., 2025*

## TL;DR
BIR employees show strong budgeting and saving habits but inconsistent spending and investing, with debt accumulation and impulse spending as key barriers, calling for structured workplace financial literacy programs.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

C.1 — Budgeting Strategies and Budget Recommendation

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

## Contribution to Odin
This paper provides field data on actual financial management practices of Filipino employees, directly grounding Odin’s user profiling and budgeting strategy design. It reveals a consistent pattern: strong saving and budgeting habits coexist with weak investing and inconsistent spending verification – a behavioral profile that Odin’s classification module (F.1) should capture. The value‑action gap in investing (knowledge without action) informs how Odin might design nudges or simplified investment recommendations. Although the sample is not exclusively young professionals, the challenges (debt, impulse spending, low digital tool adoption) mirror those Odin aims to address.

**Directly justifies:**
- “Filipino government employees demonstrate strong budgeting discipline (emergency fund mean 4.32/5, expense tracking 4.03/5) but weak investing practices (overall mean 3.47/5).”
- “Debt accumulation and lack of understanding of interest rates are the most severe self‑reported financial management challenges (rank 1 and 2).”
- “There is a value‑action gap in investing: employees believe they have investment knowledge (mean 3.98) but rarely use investment apps (mean 2.92).”
- “Financial literacy engagement is perceived to improve decision‑making (mean 4.54), yet knowledge application remains inconsistent (mean 4.14), indicating a need for habit‑building features.”

**Limits of relevance:**
- Sample is BIR employees in Sorsogon City, not specifically Filipino young professionals aged 20–40; includes older generations.
- No evaluation of digital budgeting tools or ML‑based recommendations; purely descriptive survey.
- Self‑reported data may overstate positive financial behaviors.
- Does not test any algorithm or forecasting method relevant to Odin’s forecasting or anomaly detection modules.

---

# How does financial literacy affect financial behavior over the life cycle? Evidence from Filipino households
*by Cacnio, F., Romarate, M., 2024*

## TL;DR
Higher financial literacy among young Filipino adults (18-39) does not guarantee spending within income, but improves loan payment timeliness, retirement planning, and insurance uptake across age groups.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

## Contribution to Odin
This paper directly informs Odin's user profiling module by providing empirical evidence that Filipino young adults (18-39) exhibit higher financial literacy than older cohorts but are paradoxically less likely to spend within their income. The finding that financial aptitude (actual use of loans, deposits, surplus) strongly predicts retirement planning and insurance uptake suggests that Odin's profile classification should include observed transaction behaviors, not just survey-based attitudes. Additionally, the segmentation into three validated age groups (young, middle, senior) provides a demographic baseline for Odin's behavioral profile dimensions, supporting the design of adaptive budget recommendations that account for life-stage differences.

**Directly justifies:**
- "Filipino young adults (18-39) have the highest financial literacy index score (0.392) among age groups, but higher literacy correlates with lower likelihood of spending within income (OR 0.435, p<0.01)."
- "Financial aptitude — measured by loan, deposit, and surplus activities — is a stronger predictor of long-term financial behaviors (pension: OR 85.48; insurance: OR 46.81) than financial attitude."
- "Only 2% of Filipino adults answered all six basic financial literacy questions correctly, indicating very low objective knowledge despite some positive attitudes."
- "Middle-aged and senior Filipinos are significantly less likely to spend less than or equal to their income compared to young adults, suggesting life stage affects budget adherence independent of literacy."

**Limits of relevance:**
- Data from 2018; spending patterns may have shifted post-pandemic.
- Financial literacy index lacks a pure knowledge component (CFS had no knowledge questions), so findings reflect attitude and aptitude only.
- Sample excludes very low-income households (below ₱10K annual income), limiting generalizability to the poorest segments.
- Causal direction assumed (literacy → behavior); reverse causality or mutual reinforcement not tested.

---

# BUY NOW, PAY LATER: SHOPEE ONLINE STORE USERS EXPERIENCES ON SHOPEE PAY LATER FEATURE (SPAY LATER)
*by Calanog, V. C., Paderan, M. J. D., Adove, R. C. A., Bathan, C. M. N., Catibog, D. N., Rivera, G. R., Mangarin, J. A., 2025*

## TL;DR
Shopee Pay Later users in Batangas use the feature primarily for essential purchases during financial constraints, finding it convenient and helpful for budgeting, though technical issues and overspending risks exist.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

C.1 — Budgeting Strategies and Budget Recommendation

## Contribution to Odin
This qualitative study provides direct evidence of Filipino young professionals' financial behavior and budgeting practices when using deferred payment services. It informs Odin's understanding of how users manage cash flow constraints, prioritize essential spending, and adopt budgeting strategies such as pre-payment planning and needs-over-wants decision-making. The findings on user challenges (e.g., unexpected fees, transaction errors) and best practices (e.g., monitoring due dates) can guide Odin's budget recommendation and alert design to support responsible spending rather than enabling overextension.

**Directly justifies:**
- "Spay Later users report using the feature primarily for household necessities (e.g., toiletries, kitchen essentials) and high-cost essential purchases during financial constraints."
- "Participants developed enhanced savings and budgeting skills, including pre-payment planning and tracking due dates, to avoid late fees."
- "Challenges such as transaction errors and unexpected fees (e.g., 2% GCash charge) negatively impact user satisfaction with credit-based purchasing."
- "Mindful purchasing and prioritizing needs over wants are identified as best practices for avoiding financial pitfalls when using deferred payment services."

**Limits of relevance:**
- Study focuses on BNPL (credit) rather than budgeting or spending forecasting within a personal finance management system.
- Small sample (n=10) from a single municipality (Balayan, Batangas) limits generalizability to all Filipino young professionals.
- Qualitative only; no quantitative measures of budgeting effectiveness or spending adherence.
- Participants are active Shopee users with Gold/Platinum status, potentially biasing toward positive experiences.

---

# The Impact of AUP-CES Livelihood Initiatives, Leadership and Management in Buklod Bahayan
*by Carpizo, E., Balitar, J., Balila, J., 2024*

## TL;DR
AUP-CES livelihood initiatives and management training enabled Buklod Bahayan residents to build a resilient cooperative that provides income, loans, camaraderie, and crisis support.

## Topics
None — contextual only.

## Contribution to Odin
This paper does not address personal finance applications, budgeting algorithms, user profiling, or mobile systems. It is included as a methodological reference for how structured training and capacity‑building can transform a community’s financial resilience. No Odin module or RRL claim is directly supported.

**Directly justifies:**
- None applicable to Odin’s system design or literature review.

**Limits of relevance:**
- Domain is community‑based cooperative management, not personal finance software.
- Qualitative, single‑site study; no quantitative generalizability to app users.
- Focuses on low‑income homeowners, not young professionals (Odin’s primary demographic).

---

# The Gig Economy: Financial Challenges and Opportunities Faced by Freelancers
*by Casalhay, S. F., Guevarra, C. M., Bragas, C. M., 2025*

## TL;DR
Freelancers in Metro Manila face persistent income volatility and lack of traditional benefits; budgeting and saving strategies are common but insufficient for long-term financial security.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

C.1 — Budgeting Strategies and Budget Recommendation

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

I.1 — User Retention and Engagement in Personal Finance Systems

## Contribution to Odin
This paper provides empirical evidence on the financial behaviors and pain points of Filipino freelancers—a relevant segment of Odin’s target user base (young professionals in Metro Manila). It directly informs Odin’s **budget recommendation module** by documenting real-world budgeting strategies (e.g., percentage-based allocation, weekly budgeting for irregular income) that designers can use as baselines or contrast points for algorithmic recommendations. The qualitative findings on income volatility and financial stress justify Odin’s **anomaly detection** and **forecasting modules**, as freelancers explicitly report that unpredictable earnings disrupt planning. Additionally, the paper’s documentation of user coping mechanisms (manual tracking, spreadsheets, digital wallets) highlights opportunities for Odin’s **expense categorization** and **user profile classification** to reduce friction and improve financial visibility.

**Directly justifies:**
- “Freelancers in Metro Manila experience income instability driven by seasonal fluctuations, client cancellations, delayed payments, and short-term projects—making long-term financial planning difficult.”
- “Freelancers commonly use budgeting strategies such as allocating 30% of income to savings and 70% to expenses, but these methods are often reactive and insufficient for financial security.”
- “Banks view freelancers as unstable borrowers without proof of stable income, forcing them to rely on cash, budgeting, and alternative tools instead of credit.”
- “Financial uncertainty causes anxiety, stress, and delayed major life decisions (e.g., moving, travel, professional development investments) among gig workers.”
- “Digital financial tools (budgeting apps, spreadsheets, e-wallets) help with day-to-day tracking but cannot solve the underlying problem of income irregularity or delayed client payments.”

**Limits of relevance:**
- Qualitative study with N=50; findings are exploratory and not statistically generalizable to all Filipino young professionals.
- Focuses on freelancers broadly, not specifically on the 20–40 age bracket or on users of personal budget management systems.
- Does not evaluate any algorithmic or ML-based financial tool; relevance is behavioral and contextual, not technical.
- No longitudinal data; coping strategies and outcomes were self-reported at a single point in time.

---

# Exploring Parental Expectations on Children Helping Parents out in Lower Middle-Income Families
*by Casilan, J. J., Baclagan, T., 2024*

## TL;DR
Lower middle-income Filipino parents see children helping out as a non‑obligatory, voluntary act that honors parents, driven by poverty awareness and *utang na loob*, not required.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

## Contribution to Odin
This paper directly informs Odin’s user behavioral profiling module by grounding it in Filipino cultural expectations around financial reciprocity within families. It shows that young professionals’ spending and saving behaviors are shaped by a non‑obligatory but valued practice of helping parents, which may affect discretionary income allocation. The finding that *utang na loob* operates as gratitude rather than debt refines how Odin should interpret financial “obligations” in its profiling logic. Although qualitative, the paper provides culturally specific constructs (*kusang loob*, *tagasalo*) that can be used to design survey items or classification features for Filipino users.

**Directly justifies:**
- “Filipino youth’s top aspiration is to help parents and siblings financially (Magsambol, 2022), positioning family support as a primary driver of personal financial behavior.”
- “Parents from lower middle‑income families view helping out as a voluntary, autonomous act — not a mandatory debt — which implies that financial ‘obligation’ in budgeting systems should be modeled as a fluid cultural value rather than a fixed liability.”
- “Children help in areas including bill payments, groceries, and home upgrades — directly reducing household expenses and altering the spending patterns of young professionals who live with or near their parents.”
- “*Kusang loob* (willingness) and *kabutihang loob* (kindness) are central to identifying a supporting child; these constructs can inform user profile dimensions for Odin’s classification algorithm.”

**Limits of relevance:**
- Qualitative study with only 10 participants; findings are not statistically generalizable.
- Focus is on parental expectations, not on the financial behavior of young professionals themselves.
- No quantitative model or algorithm is presented; relevance is conceptual and cultural, not technical.
- Income bracket (lower middle‑class) may not represent all Filipino young professional users of Odin.

---

# Revisiting the Filipino Value Utang na Loob: Contextual Perceptions, Implications and Inputs to Sustaining the Filipino Psychology Discussions
*by Casiño, R. M. Z., Serrano, L. L., Granada, M. I. D., 2025*

## TL;DR
Utang na loob strengthens social ties when rooted in goodwill, but its misuse creates emotional pressure and turns the value into a toxic obligation.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

## Contribution to Odin
This paper provides cultural grounding for Odin’s user profiling module by showing that Filipino young professionals view utang na loob as both a positive reciprocal value and a toxic obligation. Understanding this duality explains why users may prioritize family remittances or “padrino” expenses over personal budget limits — directly informing Odin’s behavior-driven profile classification. Even without financial data, the paper’s qualitative findings support the need to include culturally specific obligation triggers (e.g., medical bills for relatives, land inheritance disputes) as features in the classifier.

**Directly justifies:**
- “Filipino young professionals perceive utang na loob as an indefinite obligation that can override personal financial priorities, even after material repayment of a debt.”
- “Family-based utang na loob forces recipients to provide financial help to relatives abroad when illness strikes, regardless of the recipient’s own budget capacity.”
- “Political exploitation of utang na loob through the Padrino system conditions users to expect reciprocal favors, potentially affecting trust in automated budget recommendations that lack human reciprocity.”
- “College-aged Filipinos (18–21) label utang na loob a ‘toxic trait’ when it is used to extort more than was given, a belief shaped by observed misuse in family and political contexts.”

**Limits of relevance:**
- Paper is entirely qualitative with no quantitative spending data; does not measure how much utang na loob affects actual budget adherence.
- Sample is limited to 13 college students in one institution (Manuel S. Enverga University Foundation) — not representative of all Filipino young professionals.
- No direct link to personal finance apps or spending forecasting; relevance is cultural-contextual, not algorithmic.
- Findings on “toxic” perception may reflect generational bias that older Filipinos (40+) do not share.

---

# The Effect of Online Buying Decision on Personal Budget of Business Administration Students
*by Cervantes, J. Z., Custora, J. M. G., Duguran, J. C. C., Malacaya, A. S., Mendoza, J., Panga, R. B., Waminal, E. D., 2025*

## TL;DR
Social media exposure and instant gratification drive unplanned online purchases, which strongly correlate (r=0.61) with poor budget management among Filipino business students.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

E.1 — Anomaly Detection in Personal Finance Systems

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

## Contribution to Odin
This paper directly informs Odin’s anomaly detection and user profiling modules by identifying specific behavioral triggers (social media, instant gratification, marketing tactics) that cause unplanned spending among Filipino young adults. The strong correlation (r=0.61) between online buying decisions and poor budget management provides empirical justification for detecting overspending anomalies driven by impulse purchases rather than genuine needs. The finding that age and civil status affect saving behaviors (p<0.05) supports Odin’s need to segment users by demographic factors when initializing behavioral profiles. Although the study focuses on students, its population (ages 18–24, largely female) overlaps with Odin’s target of young professionals, making the behavioral patterns directly applicable to the system’s design.

**Directly justifies:**
- “Social media exposure (likes, comments, influencer promotions) significantly shapes purchase intentions among Filipino young adults, leading to unplanned expenditures that disrupt personal budgets (mean agreement 3.02/4.00).”
- “Instant gratification motives — buying to relieve stress, improve mood, or express identity — drive impulsive online purchases, which correlate strongly (r=0.612, p<0.05) with poor budget management.”
- “Age and civil status significantly affect allowance spending and savings (p<0.05), indicating that demographic profile should inform user classification in personal finance systems.”
- “Discounts, flash sales, and visually appealing advertisements heighten the urge to make unplanned purchases — a finding that supports Odin’s anomaly detection logic for overage alerts triggered by promotional events.”

**Limits of relevance:**
- Study population is students, not employed young professionals; income sources and spending priorities may differ for Odin’s target users.
- No algorithm or ML model is evaluated — relevance is behavioral, not technical, and cannot directly justify algorithm selection.
- Data collected via self‑report questionnaire, not objective transaction logs; correlation does not imply causation.
- Sample limited to one campus in Bukidnon; generalizability to Metro Manila young professionals requires validation.

---

# Effects of Filipino Consumers’ Financial Attitudes, Subjective Norms, and Perceived Behavioral Control on Intentions to Formal Banking: Towards Financial Inclusion
*by Co, M., Centeno, D.D.G., 2023*

## TL;DR
Subjective norms (having a banked household member) and perceived behavioral control significantly predict unbanked Filipinos’ intention to save surplus money in formal banks, but attitudes do not.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

## Contribution to Odin
This paper directly informs Odin's user profiling module (F.1) by identifying specific psychological and demographic factors that predict financial behavior intentions among Filipinos. The finding that subjective norm (household member with a bank account) has the largest marginal effect (10.16%) suggests that Odin's profiling should consider social influence and household financial context, not just individual attributes. Additionally, the significant effects of income typology (middle-income individuals more likely to intend banking, high-income less likely) and age (millennials more likely than baby boomers) provide empirical grounding for Odin's demographic-based behavioral segmentation. Although the paper targets banking inclusion rather than budget management, the behavioral mechanisms — perceived control over saving, social norms, and education — are directly transferable to understanding why Filipino young professionals might adopt or reject a personal budget management system.

**Directly justifies:**
- "Having a banked household member increases an unbanked Filipino's intention to save surplus money in a formal bank by 10.16 percentage points (p<0.001), demonstrating the strong effect of social proximity on financial behavior intentions."
- "College-educated Filipinos are 7.95% more likely to intend formal banking than non-graduates, indicating educational attainment as a key segmentation variable for financial behavior change."
- "Middle-income Filipinos show 3.18% higher banking intention than low-income, but high-income individuals show 10.14% lower intention, suggesting that income's effect on financial intentions is non-linear."
- "Millennials (aged 14–32 in 2014) have significantly higher banking intentions than baby boomers (2.8% higher probability), supporting age-based targeting for financial products."
- "Perceived behavioral control — specifically believing one earns enough to save — increases banking intention by 1.42%, highlighting self-efficacy as a modifiable psychological lever."

**Limits of relevance:**
- The study measures intention to save in banks, not intention to use a budget management app; transfer requires analogy but the psychological constructs are similar.
- Data from 2014 may not reflect current digital finance behaviors post-pandemic (e.g., GCash, Maya adoption).
- Sample includes all Filipino adults, not specifically young professionals aged 20–40; however, millennials (14–32 in 2014) overlap with Odin's target age range.
- Attitude toward banking was not significant, which contradicts some TPB findings; caution needed when extrapolating to attitudes toward budgeting apps.
- No explicit measure of spending or budgeting behavior; only surplus saving intention.

---

# Navigating Financial Struggle: The Ripple Effect of Inflation Rates on Working Students
*by D, A. G., R, V. M., G, L. B. L., 2024*

## TL;DR
Rising inflation forces Filipino working students to prioritize necessities, cut discretionary spending, and seek government aid — with 216,000 students (8% of college population) balancing work and study.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

C.1 — Budgeting Strategies and Budget Recommendation

## Contribution to Odin
This paper provides qualitative evidence of how Filipinos (working students, a similar demographic to young professionals) actually manage scarce funds under inflation — directly informing Odin’s understanding of spending behavior and budgeting strategies. The finding that students prioritize necessities over discretionary spending and rely on simple heuristics (e.g., packing lunch, avoiding impulse buys) can guide Odin’s budget recommendation module to adopt low-friction, rule-based strategies rather than complex optimization for users with irregular income. While the study focuses on students, the coping mechanisms and financial pressures (transport, food, school materials) mirror those of Metro Manila young professionals, making the behavioral insights directly transferable to Odin’s design assumptions.

**Directly justifies:**
- “Working students prioritize food, utility bills, and school materials over discretionary spending, reducing impulsive purchases.”
- “Inflation forces Filipino students to cut non-essential expenses, packing lunch and avoiding fast food to save money.”
- “Government financial aid is sought but access barriers (disqualification, limited slots) limit its effectiveness for working students.”
- “Balancing work and study under financial pressure reduces study time and nutritional intake, affecting academic performance.”
- “Rising transport and food costs are the most immediate financial pain points for Filipino students, mirroring young professionals’ concerns.”

**Limits of relevance:**
- Study population is high school students, not young professionals aged 20–40 — spending priorities and income sources differ.
- Small convenience sample (n=6 qualitative, n=10 quantitative) limits generalizability.
- No algorithm or ML component; relevance is behavioral, not technical.
- Findings are descriptive and qualitative; no model performance metrics applicable to Odin’s modules.
- Inflation data (average 9.28% from 1957–2011) may be outdated for current Philippine economy.

---

# The Impact of Personal Budgeting Skills on College Students’ Financial Stability
*by Dela Torre, J. M. Y., Jangao, J. P. P., Maghilum, J. T., Man-onan, R. J. H., Pepito, S. G. Jr, Rapirap, G. P. Jr, Cervantes, J. Z., 2025*

## TL;DR
Strong budgeting skills (planning, goal setting, expense tracking) correlate strongly with financial stability in college students, reducing stress and increasing savings.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

C.1 — Budgeting Strategies and Budget Recommendation

## Contribution to Odin
This paper provides empirical evidence from a Filipino student population that structured budgeting practices (planning, goal setting, expense tracking) strongly correlate with financial stability outcomes. Although the sample is college students rather than young professionals, the behavioral patterns — limited allowances, financial stress, and reliance on manual tracking — closely mirror the constraints Odin assumes (manual input, no banking integration). The strong correlation (r = 0.7247) supports Odin’s core premise that improving budgeting skills via intelligent features can reduce user financial stress and increase savings. The finding that some students struggle to adhere to budgets or use digital tools directly justifies Odin’s design priority of low-friction, behavior-driven budgeting assistance over passive static templates.

**Directly justifies:**
- "Filipino college students with stronger personal budgeting skills report significantly lower financial stress and higher savings (r = 0.7247, p < 0.01)."
- "Budget planning, financial goal setting, and expense tracking are the three core budgeting practices that drive financial stability in a Philippine higher education context."
- "A substantial minority of students struggle to adhere to budgets or consistently monitor expenses using digital tools, indicating a gap that intelligent budgeting systems can address."
- "Even with very limited monthly allowances (86% of students receive ≤₱3,000/month), structured budgeting habits enable savings and reduce financial anxiety."

**Limits of relevance:**
- Study population is college students (ages 18–25), not young professionals (20–40); income sources (allowances vs. salaries) and spending categories differ.
- No evaluation of specific budgeting algorithms or digital tools — the paper measures self-reported skill levels, not system performance.
- Single institution in Bukidnon, not Metro Manila; spending patterns and cost of living may not generalize to Odin’s target urban context.
- Correlation does not establish causation; budgeting skills and financial stability may be jointly influenced by unmeasured factors (e.g., family background, financial literacy).

---

# Budgeting Practices and Challenges of Micro-Entrepreneurs in Maria Aurora Public Market: Toward a Strategic Management Plan
*by Delos Santos, D. T., Austria, M. G. P., Candelario, C. C., Garcia, L. E. B., Gonaranao, B. S., 2026*

## TL;DR
Micro-entrepreneurs in Maria Aurora public market show strong budgeting discipline (AWM 3.48–3.63) but face major challenges from financial liability (AWM 3.27) and income volatility (AWM 3.40), requiring strategic interventions.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

A.2 — Existing Personal Finance and Budget Management Systems

C.1 — Budgeting Strategies and Budget Recommendation

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

G.1 — Expense Categorization in Filipino Personal Finance Contexts

## Contribution to Odin
This paper provides empirical data on how Filipino micro-entrepreneurs manage irregular income, separate (or fail to separate) personal and business funds, and cope with financial shocks — directly informing Odin's understanding of spending behavior among Filipinos who may have side businesses or variable income. The finding that entrepreneurs frequently fail to categorize expenses into fixed vs. variable costs (AWM 3.20, lowest in expense tracking) justifies Odin's design priority of automated, guided categorization rather than assuming users will manually tag transactions. The documented preference for informal saving (paluwagan) over formal banking (savings deposit AWM only 3.22) informs Odin's user profile classification: users may distrust formal financial institutions, affecting how they interact with budget recommendations. The major challenges of income volatility (AWM 3.40) and debt pressure (AWM 3.27) support Odin's anomaly detection and forecasting modules — irregular income patterns must be anticipated, and sudden debt payments should trigger alerts.

**Directly justifies:**
- "Filipino micro-entrepreneurs in public markets prioritize business expenses over personal wants (AWM 3.67) but struggle to categorize costs as fixed vs. variable (AWM 3.20), indicating a gap between discipline and technical financial literacy."
- "Income generation challenges from inflation and fuel prices (AWM 3.48) and fluctuating supply costs (AWM 3.45) are major concerns, supporting the need for inflation-adjusted budget recommendations in personal finance systems."
- "Only 3.22 AWM for depositing savings in banks or cooperatives — Filipino micro-entrepreneurs prefer informal, liquid saving methods such as cash-on-hand or paluwagan over formal accounts."
- "Managing multiple financial obligations is the top financial liability challenge (AWM 3.42), suggesting that personal finance systems must support debt tracking and prioritization features."
- "The proposed 'Two-Wallet System' and 'Salary Method' for separating personal and business funds reflect a culturally grounded intervention that Odin could adopt as a onboarding principle for users with mixed personal/business finances."

**Limits of relevance:**
- Study population is micro-entrepreneurs (business owners), not young professionals managing only personal finances — but many Filipino young professionals have side businesses or variable income, making findings transferable.
- Geography is Maria Aurora, Aurora — a semi-rural public market context; Metro Manila young professionals may face different spending pressures (e.g., higher rent, transportation costs).
- No digital tool use was measured; all practices are manual/paper-based, so conclusions about digital budgeting adoption cannot be drawn.
- Sample size (68) is modest; statistical power for subgroup analyses is limited.
- The paper does not evaluate any ML or algorithmic approach — relevance is behavioral and contextual, not technical.

---

# Financial literacy and sustainable planning assessment among Filipino millennials
*by Dimaunahan, D. S. F., Santiago, A. F. B., Eusebio, M. C. C., Loteriña, S. M. M., Ong, A. K. S., Chavez, J. X. S., 2025*

## TL;DR
Low financial literacy among Filipino millennials does not directly drive financial planning; monthly income, expenses, and occupation matter more, with goal acceptance being the strongest predictor of planning behavior.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

C.1 — Budgeting Strategies and Budget Recommendation

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

F.2 — Profile Classification Algorithm

## Contribution to Odin
This paper directly supports Odin's user profile classification module by demonstrating that income, occupation, and expenses (not financial literacy) are the strongest predictors of financial planning behavior among Filipino millennials — justifying a behavior-driven profiling approach rather than a knowledge-based one. The finding that goal acceptance (β = 0.924) dominates planning behavior suggests Odin's profile dimensions should include goal-related constructs (commitment, specificity, acceptance, difficulty) as classification features. Although financial literacy proved insignificant, the paper's demographic predictors map precisely to Odin's planned profile variables (income type, occupation, spending patterns), providing local Philippine evidence for feature selection in the classifier. The study also confirms that Filipino millennials actively engage in financial planning despite low literacy, which supports Odin's assumption that users will manually input transaction data without requiring financial expertise.

**Directly justifies:**
- "Monthly expenses (β = 0.205) and monthly income (β = 0.180) are the strongest demographic predictors of financial planning behavior among Filipino millennials, outweighing the effect of financial literacy."
- "Goal acceptance (β = 0.924) and goal commitment (β = 0.809) show very strong direct effects on financial planning, indicating these psychological constructs should inform user profile dimensions."
- "Only 2% of Filipino adults correctly answer six financial literacy questions, and financial literacy shows no significant direct effect on financial planning (p = 0.153) — behavior is driven by needs and goals, not knowledge."
- "Filipino millennials do not typically analyze their financial situation or consult experts before making financial decisions, supporting manual-input system design over automated advisory features."

**Limits of relevance:**
- Study confined to Makati City only — not representative of all Filipino young professionals, particularly those in rural or lower-income areas.
- Sample limited to millennials (ages 28–43 at time of study); findings may not apply to Gen Z or Gen X users Odin might target.
- Used only "The Big Three" literacy measure; other literacy dimensions (e.g., digital financial literacy) were not tested.
- Study is correlational, not experimental or predictive — supports feature justification but not algorithm benchmarking.
- Data self-reported via survey, not observed financial behavior, which may introduce social desirability bias.

---

# Family dynamics in Filipino transnational families: the role of non-migrant mothers
*by Domingo, P., 2026*

## TL;DR
Non-migrant mothers sustain OFW family cohesion through intensive mothering and father-child mediation, but this also reproduces mediated patriarchy and financial surveillance.

## Topics
None — contextual only.

## Contribution to Odin
This paper does not address personal finance systems, budgeting algorithms, or PFMS design. It is included only as background on Filipino family dynamics and financial adaptation under migration stress. The findings about irregular remittances and maternal co-provider roles may inform understanding of Filipino young professionals’ household budgeting behaviors (Topic 1) or cultural obligations (Topic 1 `/cultural-obligations`), but no direct system design implication.

**Directly justifies:**
- None for Odin’s RRL or module decisions.

**Limits of relevance:**
- Qualitative sociology, not computational or PFMS-focused.
- No algorithm, evaluation metric, or mobile design insight.
- Philippine context but not young professionals (mothers of adolescents; average husband migration 12.3 years).

---

# Knowledge, Attitudes, and Practices in Financial Literacy among Business Administration Students in Urban College in the Philippines
*by Espiritu, M., 2025*

## TL;DR
Financial literacy knowledge, attitudes, and practices among Filipino business students vary significantly by age, sex, and year level, with a strong positive correlation among the three dimensions (R=0.697).

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

## Contribution to Odin
This paper provides direct empirical evidence on the financial knowledge, attitudes, and practices of Filipino young adults (ages 18–30, the same demographic as Odin’s target users). The finding that KAP are strongly correlated (R=0.697) justifies Odin’s design assumption that improving financial knowledge through the system can positively influence spending behavior. The significant demographic differences (by age, sex, income, year level) inform Odin’s user profiling module, indicating that budget recommendations and educational interventions should adapt to these variables. Although the study focuses on students rather than young professionals in the workforce, the spending and money management challenges are highly similar in urban Metro Manila.

**Directly justifies:**
- “Financial literacy knowledge, attitudes, and practices are strongly correlated among Filipino young adults (R=0.697, p<0.001), meaning improvements in one dimension likely lift the others.”
- “Age, sex, and year level significantly affect financial knowledge and practices (p<0.05), therefore user profiling must incorporate these demographic factors.”
- “Monthly family income does not significantly affect financial knowledge (p=0.092) but does affect attitudes (p=0.038) and practices (p<0.001) — income alone is insufficient to predict financial capability.”
- “Mean scores for budgeting and expense-tracking practices ranged from 3.00 to 3.13 (Agree), indicating that even business students have room for improvement in hands-on financial management.”
- “First-year students show different financial literacy levels than fourth-year students (p<0.001), suggesting that financial education accumulates over time — a finding that supports Odin’s learning curve design.”

**Limits of relevance:**
- Sample comprises college students, not the broader population of Filipino young professionals (ages 20–40) who may have different income sources and spending obligations.
- Single institution in Quezon City may not represent all urban young Filipinos, especially those in lower-income or non-academic settings.
- Self-reported attitudes and practices may suffer from social desirability bias; actual behavior could differ.
- The study measures general financial literacy, not specific budgeting or spending behaviors in a mobile app context.

---

# Ka-abag o Babag? Exploring the Lived Experiences in the Context of Financial Well-being of Microfinance Borrowers
*by Estorba, V. L., Relativo, J. L. C., Rellon, S. B. S., Regis, K. J. M., 2025*

## TL;DR
Microfinance acts as both a lifeline (ka-abag) and a debt trap (babag) for low-income Filipino women, providing short-term relief while perpetuating stress, cyclical debt, and emotional strain.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

## Contribution to Odin
This paper provides qualitative evidence of how low-income Filipino borrowers prioritize spending (education, health, daily subsistence) and cope with financial strain through budgeting, income diversification, and emotional regulation. These behavioral patterns directly inform Odin’s user profiling module by revealing real-world expenditure priorities and coping mechanisms that a profile classifier must account for. The finding that borrowers experience debt as both a tool and a trap underscores the need for Odin’s budget recommendation and anomaly detection modules to be sensitive to users’ financial vulnerability — for example, flagging over-borrowing risk rather than assuming all credit use is productive. Although the study focuses on microfinance borrowers in a rural setting, its insights into Filipino financial decision-making under income instability are transferable to Odin’s target demographic of young professionals in Metro Manila, who face similar pressures (e.g., family remittances, irregular income, emergency spending).

**Directly justifies:**
- “Filipino low-income borrowers prioritize education spending and health emergencies over other categories, often borrowing specifically to cover school fees and medical costs.”
- “Chronic income instability forces borrowers to engage in daily budgeting and ‘hustling’ (multiple income streams) as primary coping strategies, not as elective financial optimization.”
- “Debt-related psychological distress in Filipino borrowers includes insomnia, fear of legal consequences, and suicidal ideation — design implications for non-judgmental alerting in personal finance apps.”
- “Microfinance insurance benefits provide significant emotional relief during crises, suggesting that financial apps with embedded safety features (e.g., emergency buffers) may reduce user stress.”
- “Borrowers who develop financial discipline through repeated borrowing cycles report increased sense of control — a behavior that Odin’s budgeting module could reinforce through positive feedback.”

**Limits of relevance:**
- Study population is rural, female, and low-income (microfinance borrowers) — not directly young professionals in Metro Manila, though income instability and family obligations overlap.
- Qualitative findings are context-specific to Argao, Cebu; not statistically generalizable but analytically transferable.
- No direct evaluation of digital financial tools — all borrowing is through MFIs with in-person collections, so mobile app dynamics are inferred, not measured.
- The study does not quantify spending patterns or provide algorithmic benchmarks; its value is behavioral and motivational insight.

---

# Financial freedom of Filipinos in personal finance management
*by Flores, C., 2025*

## TL;DR
Cash, debt, risk, and wealth management practices among Filipino corporate employees do not significantly predict financial freedom, despite moderate self-assessed competence.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

## Contribution to Odin
This paper provides direct empirical evidence on the personal finance practices, attitudes, and gaps among Filipino corporate employees — a population that overlaps with Odin's target young professionals. It informs Odin's user profiling module by documenting cultural behaviors (traditional alkansya usage, utang cycles, fear of bank savings, "come-what-may" attitude) that can be operationalized as profile dimensions. The finding that standard CDRW practices do not predict financial freedom suggests Odin should look beyond basic finance metrics and incorporate behavioral economics or social factors into its budget recommendation and anomaly detection logic. Although the study uses regression instead of ML, its descriptive statistics on emergency fund unpreparedness and high debt reliance justify Odin's emphasis on automated savings nudges and debt-prioritization features.

**Directly justifies:**
- "57% of Filipino corporate respondents keep their savings in traditional alkansya or at home due to perceived bank insecurity, leading to low emergency fund preparedness."
- "Majority of respondents agree that paying off high-interest debt first and paying more than the minimum balance are effective debt management strategies."
- "Filipino employees exhibit a 'come-what-may' attitude toward financial planning, which hinders budgeting and investment practices."
- "Life insurance uptake in the Philippines is low because Filipinos perceive it as an unnecessary expense, intangible, or a lack of funds — not as a risk management tool."
- "Linear regression showed that cash, debt, risk, and wealth management combined do not significantly predict financial freedom (p > 0.05), indicating other unmeasured factors (e.g., financial literacy, social pressures) are more influential."

**Limits of relevance:**
- Sample is limited to large corporations in Metro Manila; findings may not generalize to self-employed, informal sector, or provincial Filipino young professionals.
- Study uses self-reported survey data with potential social desirability bias; actual behavior may differ.
- No digital or mobile finance context; Odin's mobile-first design is not addressed.
- Regression found no significance, suggesting the CDRW framework may be incomplete — use cautiously as justification for excluding these variables.

---

# Understanding the Impulse Buying Behavior in the Digital Age: Influential Factors in Online Consumer Behavior
*by Gabatin, R., Sierra, S., Maniago, M., Capole, A., Torres, R., 2025*

## TL;DR
Website ease and payment options increase urgency, strongly predicting impulse buying (β=0.804, p<0.001) among Filipino online shoppers.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

## Contribution to Odin
This paper directly informs Odin’s understanding of impulse spending as a component of Filipino young professionals’ financial behavior, grounding module designs in local behavioral data. The finding that consumer characteristics (shopping lifestyle, income) significantly drive urgency and impulse buying justifies including these features in Odin’s user profile classification (F.1) to better predict spending deviations. Although the study focuses on e-commerce, its insights apply to any digital environment where users make spending decisions—Odin’s manual transaction interface can similarly trigger unplanned purchases if designed without friction controls. The mediation results also suggest that website ease and payment options indirectly affect spending, which can guide Odin’s interface design to either nudge or mitigate impulsive entries.

**Directly justifies:**
- “Among Filipino online shoppers, urgency to buy has a strong direct effect on impulse buying (β=0.804, p<0.001), the largest path in the model.”
- “Consumer characteristics (shopping lifestyle and income) significantly influence urgency to buy (β=0.562, p<0.001) and directly affect impulse buying (β=0.109, p=0.016).”
- “Social-related factors do not directly drive impulse buying but strongly shape website perception (β=0.868, p<0.001), which then affects urgency.”
- “Marketing-related factors (discounts) do not directly cause impulse buying but strongly shape consumer characteristics (β=0.714, p<0.001).”
- “Age and gender do not moderate the urgency–impulse relationship, suggesting these demographic variables are less critical than behavioral traits in explaining impulse spending.”

**Limits of relevance:**
- The study measures self-reported impulse buying intentions, not actual transaction-level spending data.
- The sample is limited to one city (Cabuyao, Laguna) and may not represent all Filipino young professionals.
- The paper does not evaluate financial outcomes (e.g., budget overages, savings impact) of impulse buying.
- Findings are cross-sectional; causal direction is assumed from the SOR framework but not experimentally proven.

---

# Financial Literacy and Financial Health of Public Junior High School Teachers
*by Garcia, E., 2025*

## TL;DR
Public junior high school teachers in Quezon City show high financial literacy (mean 4.02/5) but are only “financially coping” (61.2/100), with critical gaps in emergency funds and retirement planning.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

C.1 — Budgeting Strategies and Budget Recommendation

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

## Contribution to Odin
This paper provides empirical baseline data on Filipino professionals’ spending, saving, and borrowing behaviors that directly inform Odin’s user profiling module. The finding that most teachers lack emergency funds (38.07 vulnerability score) and month-end surplus (39.00) justifies Odin’s design priority of promoting automated savings and anomaly detection for unexpected expenses. Demographic differences (sex, age, number of children, income) across financial health dimensions support Odin’s need for behavior-driven user profiles that adapt to personal circumstances rather than using static templates.

**Directly justifies:**
- “Public junior high school teachers in Quezon City have a mean emergency fund adequacy score of 38.07 (Financially Vulnerable), indicating most lack six months of living expenses.”
- “Teachers’ mean month-end surplus score is 39.00, meaning the majority have no money remaining after monthly expenses, limiting their capacity to absorb financial shocks.”
- “Female teachers exhibit significantly higher overall financial literacy than males (mean rank 126.87 vs 103.67, p=0.017), suggesting gender-informed profiling may improve budgeting recommendations.”
- “Debt service consumes a large portion of monthly income (mean 78.44 on a 0–100 scale), leaving little room for savings—anomaly detection should flag high debt-to-income ratios as financial strain indicators.”
- “Retirement planning literacy is the lowest among all dimensions (mean 3.75/5), highlighting a gap that Odin’s budgeting module could address with personalized long-term goal setting.”

**Limits of relevance:**
- Sample consists of public school teachers (mean age 41+), not the target 20–40 young professional demographic.
- Findings are self-reported, not derived from actual transaction data, limiting direct comparability to Odin’s behavioral logs.
- No evaluation of digital financial tools or algorithm-based recommendations; purely descriptive survey.
- Geography limited to one district of Quezon City; may not generalize to other Philippine urban areas.

---

# The Concept of Utang Na Loob Among Filipino Working Millennials
*by Donato, A., Panentan, G., Castro, J., Gavino, R., 2023*

## TL;DR
Filipino working millennials perceive utang na loob as a self-imposed obligation to reciprocate kindness, primarily expressed through financial support to family, which motivates work but can also become a personal burden.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

## Contribution to Odin
This paper directly informs Odin's user profiling module by providing qualitative evidence that Filipino working millennials prioritize financial support to family as an expression of utang na loob, creating a predictable spending category (remittances/allowances to parents and siblings) that Odin's expense categorization must accommodate. The finding that utang na loob both motivates work and creates financial burden (borrowing, inability to save) supports Odin's anomaly detection logic: sudden reductions in family-related spending may signal financial distress rather than behavioral change. Understanding that millennials feel self-imposed obligation to provide financial support helps Odin's budget recommendation algorithm distinguish between discretionary wants and culturally protected obligations.

**Directly justifies:**
- "Filipino working millennials feel a self-imposed obligation to provide financial allowances to parents, cover household expenses, and buy family necessities as the primary expression of utang na loob."
- "Utang na loob increases work motivation but can lead to personal financial sacrifice, including reduced personal spending, inability to save, and borrowing from peers."
- "Millennials prioritize experiential reciprocity (vacations, quality time) over material gifts when repaying utang na loob to parents, indicating a generational shift in spending allocation."
- "Utang na loob extends to workplace relationships, where financial assistance to colleagues and loyalty to employers are forms of reciprocation."

**Limits of relevance:**
- Study limited to Tuguegarao City, Cagayan; regional differences in utang na loob expression across the Philippines may exist.
- Qualitative design with N=30 provides no generalizable spending percentages or statistical weights for budget recommendation algorithms.
- No direct measurement of actual spending amounts or income percentages allocated to family support.
- Focus on utang na loob as a cultural value, not on financial management systems or algorithms.

---

# From Surge to Stability: Digital Payments Driving a Steady Transition: 2024 Status of Digital Payments in the Philippines
*by Mesina-Romero, B., Masangkay, M. C., Franco, M., Yambao, M. A. V., Delgado, K., Bueno, P. N., Lingat, P. J., Natividad, G. M., Lapus, A. R., Manuel, R. M., Yñigo, K. T., 2024*

## TL;DR
Digital payments reached **57.4%** of retail transaction volume in the Philippines by 2024, driven by merchant payments (66.4% share) and person-to-person transfers (20.6% share).

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

G.1 — Expense Categorization in Filipino Personal Finance Contexts

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

## Contribution to Odin
This BSP report provides authoritative, national-scale data on how Filipinos actually make payments — knowledge that grounds Odin’s expense categorization and user behavior assumptions. The finding that merchant payments (P2B) dominate digital volume (66.4%) confirms that retail spending is the core use case, directly informing which expense categories (e.g., groceries, dining, transport) should be prioritized in Odin’s FIES/CFS-based taxonomy. Additionally, the report’s documentation of BSP consumer redress and merchant acquisition regulations (Circulars 1195 and 1198) offers citable evidence of the regulatory emphasis on trust and security — justifying Odin’s privacy-by-design approach even without banking integration.

**Directly justifies:**
- “Merchant payments account for 66.4% of digital payment volume in the Philippines (2024), indicating that retail spending is the primary transaction type for Filipino consumers, which directly maps to Odin’s expense categorization module.”
- “Only 24.6% of government collections (P2G) were digital in 2024, showing that a large share of taxes and fees are still paid via cash — a relevant constraint for young professionals who may have irregular cash-based government payments.”
- “InstaPay transaction volume grew 67.8% year-on-year, demonstrating rapid adoption of real-time account-to-account transfers among Filipinos, supporting the design assumption that users are comfortable with digital financial interfaces.”
- “BSP Circular No. 1195 requires timely notifications and fund return for failed EFTs, establishing consumer protection norms that Odin can cite when designing transparent manual transaction logging and error handling.”

**Limits of relevance:**
- Report focuses on payment infrastructure and aggregate volumes, not individual spending behavior or budgeting practices.
- No demographic breakdown by age (young professionals) or income type — cannot be used to claim specific patterns for Odin’s target user segment.
- Data covers all retail payments, not just those made by individuals; business and government transactions inflate some categories (e.g., B2B supplier payments).
- Manual transaction input (Odin’s scope) is not measured or discussed; the report assumes digital payment initiation, not manual logging.

---

# FINANCIAL HARDSHIPS OF TRICENARIANS EDUCATORS: PREPARING FOR THE FUTURE AMID DEBT CHALLENGES
*by Navarro, R. L., Bantulo, J. S., 2026*

## TL;DR
Tricenarian Filipino teachers face persistent debt, mental burden, and work disruption despite using manual budgeting and loans to cope.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

C.1 — Budgeting Strategies and Budget Recommendation

## Contribution to Odin
This paper provides empirical evidence of how Filipino professionals in their thirties actually manage money: manual envelope budgeting, handwritten tracking, and reliance on digital apps for expense monitoring. These findings directly inform Odin’s expense categorization and budget recommendation modules by revealing that users prefer low‑friction, visual, and rule‑based budgeting methods (e.g., separating needs from wants, weekly budget cycles). The documented financial strain and debt cycles justify Odin’s focus on automated alerts for over‑category spending and its avoidance of gamification in favor of value‑driven retention. Although the study focuses on educators, the behaviors (limited income, family obligations, irregular expense timing) mirror those of Filipino young professionals generally.

**Directly justifies:**
- “Tricenarian Filipino teachers manually track expenses using envelope systems and handwritten lists, indicating a preference for tangible, low‑tech budgeting methods over complex automation.”
- “Debt pressure forces users to prioritize fixed bills (housing, utilities, loan payments) over discretionary spending, suggesting that budget recommendation algorithms must accommodate fixed‑expense constraints.”
- “Participants reported reduced teaching focus due to financial worry, establishing that financial strain degrades professional performance — a finding that supports Odin’s design goal of reducing user cognitive load.”
- “Weekly budget cycles (rather than monthly) were preferred by one participant for tighter control, implying that Odin’s forecasting module should support per‑week or per‑cut‑off period views.”

**Limits of relevance:**
- Participants are public school teachers, not the full spectrum of young professionals; income stability (government salary schedule) differs from private‑sector or freelance workers.
- No quantitative evaluation of budgeting tool effectiveness; findings are qualitative and context‑specific.
- Rural location (Kiamba, Sarangani) may not represent Metro Manila young professionals who have better access to banking and digital infrastructure.
- The study does not test any automated budget recommendation or ML algorithm.

---

# NURSING CAREER TOWARDS FINANCIAL INDEPENDENCE
*by Nduka, P., Benedicto, E. G., 2026*

## TL;DR
Filipino nurses face persistent income-expense deficits due to low government salary grades and high family obligations, leaving most unable to save for emergencies or retirement.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

C.1 — Budgeting Strategies and Budget Recommendation

G.1 — Expense Categorization in Filipino Personal Finance Contexts

## Contribution to Odin
This paper provides real-world evidence of income-expense mismatches among Filipino young professionals (nurses aged 26–39), directly informing Odin’s spending forecasting and budget recommendation modules. The finding that single breadwinners face chronic monthly deficits while single independents can cover basics but cannot save justifies designing distinct budget recommendation logic by user profile type (e.g., breadwinner vs. living alone). The paper’s identification of specific expense categories (rent, utilities, food, dependents’ schooling, remittances) grounded in Philippine urban living supports Odin’s FIES/BSP-based categorization schema. Furthermore, the proposed financial literacy workshops on budgeting and debt management validate Odin’s assumption that users need more than tracking — they need strategy guidance.

**Directly justifies:**
- “Majority of Filipino nurses (53.57%) support four or more dependents, creating a structural income-expense deficit that prevents long-term savings.”
- “Single nurses living alone can meet basic needs (rent, food, utilities) but cannot accumulate savings, indicating that ‘functional independence’ differs from ‘resilience independence.’”
- “Single adult breadwinners report ‘barely anything left’ after family support, with chronic anxiety about covering monthly expenses — a behavioral pattern that anomaly detection should flag as overage risk, not discretionary spending.”
- “Structured financial literacy on budgeting, debt management, and cooperative savings is nurses’ top requested intervention, supporting Odin’s educational component over gamification for retention.”

**Limits of relevance:**
- Study population is nurses, not the general young professional population; income and obligation structures may differ (e.g., nursing has standardized government salary grades).
- No quantitative income/expense amounts are reported; only qualitative deficits and percentages, limiting direct calibration of forecasting models.
- Single nurses living alone sample is very small (n=3), so findings for that subgroup are tentative.
- The study does not evaluate any digital financial tool; relevance is behavioral and categorical, not algorithmic.

---

# The Moderating Effect of Access to Finance on Myopic Decision-Making and Business Performance of Low-income Household Micro-Enterprises in Manila
*by Ong, H., Keh, K., Lui, N., Santos, A., Suarez, E., 2026*

## TL;DR
Myopic decision-making among low-income micro-entrepreneurs in Manila significantly reduces business performance (p < 0.001), but better access to finance moderates this negative effect (p = 0.005).

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

## Contribution to Odin
This paper directly informs Odin’s user profiling module (F.1) by empirically demonstrating that myopic decision-making (especially temporal myopia) is a measurable behavioral pattern among low-income Filipinos in Manila. The finding that access to finance significantly moderates the negative impact of myopia (p = 0.005) supports Odin’s budget recommendation module (C.1) design: features that simulate “access to future funds” (e.g., surplus-to-savings nudges) could mitigate short‑term bias. Although the study focuses on micro‑enterprise owners, the behavioral insight applies to young professionals who face similar income volatility and survival pressures, justifying a profile dimension for short‑term vs. long‑term orientation in Odin’s classifier.

**Directly justifies:**
- “Myopic decision-making has a significant negative effect on business performance among low-income micro-entrepreneurs in Manila (p < 0.001).”
- “Access to finance significantly moderates the relationship between myopic decision-making and business performance (p = 0.005), reducing the harm of short‑sighted choices.”
- “Temporal myopia (short‑term financial focus) scores highest (mean 2.96) among low-income sari-sari store owners, indicating a strong tendency to cut long‑term investments for immediate gains.”
- “Low-income households in Manila have very limited access to formal lending institutions (mean 1.49/5), forcing reliance on informal, costly credit.”

**Limits of relevance:**
- Study population is micro‑enterprise owners (sari‑sari stores), not personal finance users; findings may not fully generalize to young professionals with different income sources and spending patterns.
- Myopia measured via self‑reported Likert scales, not objective transactional data; potential social desirability bias.
- Correlational design (no causal inference); the moderation effect is statistical, not experimentally identified.
- Business performance metrics (profitability, customer satisfaction) differ from personal budget adherence outcomes.

---

# Personal Financial Management Practices of Average earning households within Indigenous Communities of Mountain Province: Exploring Their Strategies and Challenges
*by Rosario, E., 2025*

## TL;DR
Indigenous households in Bontoc blend strict budgeting and kinship-based reciprocity (og-ogfo, bayanihan, paluwagan) to manage income insufficiency, prioritizing cultural obligations over individual wealth accumulation.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

C.1 — Budgeting Strategies and Budget Recommendation

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

G.1 — Expense Categorization in Filipino Personal Finance Contexts

## Contribution to Odin
This paper directly informs Odin's user profiling (F.1) and expense categorization (G.1) by documenting how cultural obligations (og-ogfo, ritual contributions, kinship aid) override individual financial goals in Filipino indigenous contexts — a pattern that may generalize to Metro Manila young professionals with strong family ties. The finding that households prioritize "protected categories" (education, health, ritual expenses) even under scarcity provides empirical grounding for Odin's budget recommendation module to treat certain expenses as non-negotiable. Additionally, the documented reliance on informal reciprocity (paluwagan, og-ogfo) rather than formal credit suggests that Odin's anomaly detection should flag sudden drops in discretionary spending as potential cultural obligations (e.g., a wedding contribution) instead of overspending.

**Directly justifies:**
- "Indigenous Filipino households prioritize kinship obligations (og-ogfo, ritual contributions) over personal savings goals, redefining financial resilience as collective rather than individual."
- "Micro-savings of ₱50–₱100 per day through informal methods (coin jars, paluwagan) are more common than formal emergency funds among low-income Filipino households."
- "Health and education expenses are treated as non-discretionary priorities, but out-of-pocket costs still destabilize budgets even with PhilHealth coverage."
- "Households follow a sequenced coping response: budget tightening → kinship mobilization → savings drawdown → formal credit only as last resort."
- "Cultural expense types (ritual offerings, community contributions) are not optional; they function as investments in future reciprocity and social standing."

**Limits of relevance:**
- Study population is Indigenous rural households in Mountain Province, not young professionals in Metro Manila; urban financial pressures (rent, transport, digital services) differ significantly.
- No digital finance or mobile app usage documented; findings reflect cash-based, informal systems that may not translate to Odin's manual input interface.
- Qualitative design with N=12; findings are not statistically generalizable but provide behavioral patterns usable for hypothesis generation.
- Cultural practices (og-ogfo, supon) are specific to Cordillera Indigenous groups; Metro Manila young professionals may have weaker or different kinship obligations.

---

# The Shift to Gig Economy: How Traditional Employment Stacks Up Against Platform-Based Independent Workers
*by Torres, R. C., Bartolome, Z. M. I., Jimena, L. G., Paner, J. P., 2025*

## TL;DR
Traditional employees have higher debt-to-income ratios than gig workers, but both groups show similar financial literacy, social support, and job satisfaction levels.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

## Contribution to Odin
This paper directly informs Odin's user profiling module (F.1) by providing empirical evidence on how employment type (traditional vs. gig) shapes financial indicators — specifically DTI ratios and financial literacy — among Filipino workers. The finding that gig workers maintain lower DTI ratios despite income volatility suggests more cautious debt behavior, which Odin's profile classification could use as a behavioral signal. The parity in financial literacy across both groups indicates that Odin cannot assume traditional employees have superior financial knowledge; instead, the system must design budget recommendations and financial nudges that work for both stable and volatile income profiles. Although the paper does not target budgeting directly, its comparative framework on financial behavior across income types justifies Odin's decision to treat income stability as a key profiling dimension.

**Directly justifies:**
- "Traditional employees have a significantly higher median DTI ratio (40) than gig workers (31.41), indicating greater debt burden despite more stable income (p < 0.001)."
- "No statistically significant difference in financial literacy exists between traditional employees and gig workers (median 9 for both, p = 0.267), meaning employment type does not predict financial knowledge."
- "Gig workers report similar job satisfaction levels to traditional employees (3.67 vs. 3.56, p = 0.797), with autonomy and flexibility cited as key satisfiers despite income instability."
- "Social support networks do not differ significantly between groups (p = 0.135), though some gig workers report zero access to professional guidance, indicating uneven distribution."

**Limits of relevance:**
- The study population includes five Philippine provinces but not specifically Metro Manila, where Odin's target young professionals are concentrated; urban income and spending patterns may differ.
- Sample includes both ride-hailing and online freelancing gig workers; Odin's user base may skew toward white-collar young professionals, not delivery or transport workers.
- No direct measurement of budgeting behavior, spending categories, or savings rates — only DTI and self-reported financial literacy.
- Cross-sectional design captures a snapshot; Odin's profiling requires understanding how behavior changes over time (concept drift).

---

# A Systematic Review of Mobile Banking, Fintech Innovations, and Regulatory Gaps to Achieve Financial Inclusion in the Philippines
*by Velez, G., 2025*

## TL;DR
GCash reduced cash dependency by 41% in urban and 29% in rural Philippines, but digital divides, gender gaps, and low financial literacy (34% understand security) persist.

## Topics
A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

A.2 — Existing Personal Finance and Budget Management Systems

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

## Contribution to Odin
This systematic review provides critical baseline data on Filipino financial behavior, digital adoption gaps, and user trust deficits — directly informing Odin’s design assumptions about its target demographic. The finding that only 34% of low-income users understand digital security justifies Odin’s privacy-by-design approach and plain-language security explanations. Gender and rural-urban disparities (women as 22% of fintech borrowers, rural adoption 1.8x lower) validate Odin’s focus on manual input (no banking API dependency) and culturally grounded categorization. The paper also confirms that platforms like GCash have normalized digital payments, supporting Odin’s mobile-first assumption for young professionals.

**Directly justifies:**
- “As of 2021, 68% of Filipino adults were unbanked, making manual-entry personal finance systems like Odin necessary where banking APIs are unavailable (BSP, 2023; Velez, 2025).”
- “GCash reduced cash dependency by 41% in urban Metro Manila and 29% in rural areas — digital payments are now mainstream, enabling mobile-first budget management.”
- “Only 34% of low-income Filipino users understand digital payment security features — Odin must embed financial literacy prompts and transparent privacy controls.”
- “Women-owned MSMEs represent just 22% of fintech borrowers despite 39% of entrepreneurs — gender-neutral system design may exclude women; Odin’s profiling must account for gendered spending patterns.”
- “Rural adoption rates are 1.8 times lower than urban, driven by infrastructure gaps — Odin’s offline-capable manual input design directly addresses this limitation.”

**Limits of relevance:**
- The review covers all Filipino adults, not specifically young professionals (20–40); spending patterns may differ for Odin’s target age bracket.
- No evaluation of algorithm performance or ML models; relevance is contextual (user behavior, trust, and infrastructure), not algorithmic.
- Data on GCash and Maya reflects commercial fintech; Odin is a budgeting tool, not a payment platform, so adoption figures inform only user readiness, not direct feature equivalence.
- The 34% security literacy figure is from low-income users generally, not specifically Odin’s college-educated young professional segment.

---
