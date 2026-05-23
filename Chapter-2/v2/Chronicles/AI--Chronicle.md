## Source: `10.A/AI--Bhavana_et-al_2025_summarized.md`

**Title:** AI-Based Wealth Advisory System using Machine Learning and Predictive Analytics for Personalized Budget Planning

### TL;DR

AI Wealth Advisor integrates forecasting, anomaly detection, and explainable AI to deliver personalized budget planning, achieving **95% anomaly detection accuracy** and a 22% improvement in savings in a pilot study.

### Findings

1. Expense classification achieved **91% F1-score** using XGBoost/RF and BERT.
2. Forecasting error was MAE of **$43/month per user** across the pilot.
3. Anomaly detection accuracy = **95%** using Isolation Forest and Autoencoders.
4. Recommendation adoption rate = 41% of suggested actions followed by users.

- Pilot study (100 users) showed a **22% improvement in savings** and 78% of participants reported enhanced financial literacy.
- SUS scores and user satisfaction surveys indicated improved trust and usability due to XAI transparency.

### Relevance to Odin

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

### Limitations

- The paper does not disclose the demographic composition of the pilot sample, limiting generalizability to Filipino young professionals.
- No evaluation of the system under cold-start conditions (users with <30 days of transaction history). [unacknowledged]
- Reliance on banking APIs (Open Banking, PSD2) assumes infrastructure not available in the Philippine context.
- The paper acknowledges algorithmic bias risks but does not test fairness across income or demographic groups.
- Recommendation adoption rate (41%) is reported without longitudinal retention data; long-term user engagement remains unknown.

---

## Source: `10.A/AI--Chahar_et-al_2026_summarized.md`

**Title:** Artificial Intelligence Powered Personal Finance Management System

### TL;DR

An AI-powered personal finance assistant using ML classification, LSTM forecasting, and NLP achieved user satisfaction of **4.4/5** and transaction categorization correctness of **4.2/5** in a prototype survey.

### Findings

1. User satisfaction survey yielded an overall rating of **4.4/5** for the AI‑powered system.
2. Ease of use was rated **4.5/5** – the highest among measured attributes.
3. Goal‑setting functionality received **4.3/5** from users.
4. Transaction categorization correctness was rated **4.2/5**, with ambiguity in vendor‑specific transactions identified as a limitation.

- Users requested improved accuracy for variable or non‑recurring expenses (e.g., dining out).
- The system struggled with irregular income streams and unpredictable spending patterns.
- Survey respondents highly valued the ability to customize budgets based on personal spending habits.

### Relevance to Odin

**Topics:**

3.A — Expense Categorization Frameworks

4.A — Landscape of Existing Personal Finance Systems

4.B — Limitations and Gaps in Existing Systems

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

7.B — Budget Recommendation in Personal Finance Systems

7.C — Budget Recommendation Algorithm

8.A — Anomaly Detection in Personal Finance Systems

10.A — Data Privacy and Security in Personal Finance Systems

10.B — User Trust in Personal Finance Systems

12.A — Evaluation Frameworks for Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly informs Odin’s algorithm selection for expense classification (SVM, Random Forest, LSTM) and spending forecasting (LSTM over ARIMA for sequential dependencies). The user satisfaction survey (4.4/5 overall) provides a benchmark for Odin’s expected usability outcomes. The identified limitation – systems struggle with irregular income and variable spending – validates Odin’s requirement to incorporate income typology into its behavioral profiling. The security and privacy measures (encryption, anonymization, GDPR compliance) justify Odin’s privacy‑by‑design approach under Philippine law (RA 10173).

**Directly justifies:**

- “User satisfaction survey of an AI‑powered personal finance prototype yielded an overall rating of 4.4/5 and ease‑of‑use rating of 4.5/5.”
- “Transaction categorization correctness was rated 4.2/5 by users, with ambiguous vendor‑specific transactions as the primary error source.”
- “Predictive models (ARIMA, LSTM) enable proactive budget planning but struggle with irregular income streams common in gig economy workers.”
- “End‑to‑end encryption and GDPR‑compliant anonymization are necessary for user trust in AI‑driven financial tools.”
- “NLP chatbot interfaces reduce barriers for users unfamiliar with financial terminology, improving engagement.”

**Limits of relevance:**

- The study population is not Filipino; spending patterns and cultural financial obligations may differ substantially.
- User survey sample size and demographics are not reported, limiting generalizability to Filipino young professionals.
- The system assumes bank API integration; Odin relies on manual transaction input only, which may change user behavior and data completeness.
- No objective algorithmic performance metrics (e.g., MAE, F1) are reported – only subjective user ratings.
- Evaluation does not use ISO 25010 or SUS, the frameworks adopted for Odin.

### Limitations

- Data quality issues (incomplete or inaccurate transaction records) degrade prediction and recommendation accuracy – acknowledged by the authors.
- Model adaptability is poor for users with irregular income or unpredictable spending patterns – acknowledged as a key limitation.
- The paper does not evaluate cold‑start performance (new users with no transaction history). [unacknowledged]
- No comparison of different ML models (e.g., LSTM vs. GRU, Random Forest vs. XGBoost) on the same dataset. [unacknowledged]
- The survey results lack statistical significance testing or confidence intervals. [unacknowledged]

---

## Source: `10.A/AI--Guo_2025_summarized.md`

**Title:** Machine Learning Methods in Customer Segmentation and Recommendation Systems

### TL;DR

K-means, DBSCAN, and collaborative filtering improve segmentation and recommendation accuracy by 12–18% in e-commerce, banking, and healthcare, but data quality and privacy remain challenges.

### Findings

1. **Amazon achieved a 12% improvement in recommendation accuracy** by applying DBSCAN over K‑means for handling noisy transaction data.
2. PCA‑based preprocessing improved anomaly detection accuracy by **15%** in banking transactional data.
3. DBSCAN improved patient classification accuracy by **18%** in noisy healthcare datasets (chronic disease management).

- Collaborative filtering faces cold start (new users/items) and scalability issues with large datasets.
- Content‑based filtering depends heavily on metadata quality; poor labels degrade performance.
- Hybrid models combine user behavior and item attributes to overcome individual method limitations.

### Relevance to Odin

**Topics:**

4.A — Landscape of Existing Personal Finance Systems

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

7.B — Budget Recommendation in Personal Finance Systems

8.B — Anomaly Detection Algorithm

10.A — Data Privacy and Security in Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This survey directly informs Odin’s algorithm selection for customer segmentation (financial profiling) and recommendation (budget suggestions). The comparison of K‑means, DBSCAN, and PCA justifies using density‑based clustering (DBSCAN) for outlier detection in transaction data and dimensionality reduction for high‑dimensional spending patterns. The discussion of collaborative filtering’s cold start problem supports Odin’s reliance on content‑based and hybrid approaches when user history is sparse. Reported accuracy gains (12–18%) provide benchmarks for evaluating Odin’s modules.

**Directly justifies:**

- “DBSCAN improves recommendation accuracy by 12% over K‑means when handling noisy data, as demonstrated in Amazon’s e‑commerce platform.”
- “PCA reduces noise and improves anomaly detection accuracy by 15% in banking transactional data, applicable to spending anomaly detection.”
- “Collaborative filtering suffers from cold start and scalability issues; hybrid models overcome these by combining user behavior and item attributes.”
- “The Equifax 2017 data breach exposed 147 million records, underscoring the need for advanced encryption and privacy‑by‑design in financial systems.”

**Limits of relevance:**

- Paper is a literature review, not an original experimental study; claims rely on cited sources.
- Demographics and datasets are not Filipino; spending patterns may differ.
- Domains include e‑commerce and healthcare, not exclusively personal finance; algorithm transferability requires validation.
- No evaluation of cold‑start performance for recommendation algorithms in personal finance contexts.

### Limitations

- Review format lacks original experimental rigor; no unified benchmark across compared methods. [unacknowledged]
- Accuracy improvements (12%, 15%, 18%) come from different studies with different datasets and tasks, limiting direct comparability.
- Privacy discussion is superficial (only Equifax example); no technical details on encryption or anonymization. [unacknowledged]
- Does not address how segmentation and recommendation handle concept drift or user behavior changes over time. [unacknowledged]
- No discussion of computational costs or scalability constraints on mobile devices, relevant to Odin’s mobile‑first design.

---

## Source: `10.A/AI--Shuryhin_&_Zinovatna_2024_summarized.md`

**Title:** Recommendation system for financial decision-making using Artificial intelligence

### TL;DR

Combining Isolation Forest for anomaly detection, ARIMA+LSTM for forecasting, and an LLM for personalized advice produces an ethical financial recommendation system that supports rational spending without manipulation.

### Findings

- Isolation Forest successfully identifies anomalous expenses by isolating shortest-path data points in an unsupervised manner.
- **Combining ARIMA and LSTM via weighted average balances short‑term (seasonal) and long‑term (dependency) patterns, improving forecast stability.**
- LLM integration enables natural‑language, goal‑aligned financial advice that adapts to any income level.
- Ethical safeguards (no manipulation, user‑choice preservation, transparency) are embedded as core design requirements, not afterthoughts.
- OAuth 2.0 and OWASP Top 10 compliance protect user data and support privacy.

### Relevance to Odin

**Topics:**

4.A — Landscape of Existing Personal Finance Systems

4.B — Limitations and Gaps in Existing Systems

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

7.B — Budget Recommendation in Personal Finance Systems

7.C — Budget Recommendation Algorithm

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

10.A — Data Privacy and Security in Personal Finance Systems

10.B — User Trust in Personal Finance Systems

**Contribution to Odin:**

This paper provides a complete, integrated AI architecture for personal finance management, directly mapping to Odin’s forecasting, anomaly detection, and recommendation modules. The hybrid ARIMA+LSTM approach justifies Odin’s spending forecasting algorithm selection, while Isolation Forest offers a well‑documented unsupervised anomaly detection method suitable for cold‑start user profiles. The explicit ethical design — preserving user autonomy, avoiding manipulation, and ensuring transparency — directly supports Odin’s privacy‑by‑design and trust requirements, especially the requirement to avoid gamification and instead provide value‑driven advice.

**Directly justifies:**

- “Isolation Forest detects financial anomalies without labeled training data, using path‑length scoring where s(x,n)≈1 indicates atypical spending.”
- “Combining ARIMA (short‑term seasonality) with LSTM (long‑term dependencies) via weighted average improves forecast stability over either model alone.”
- “LLM‑generated financial advice can be personalized to any income level by conditioning on transaction history, anomaly flags, and forecasted expenses.”
- “Ethical recommendation systems must balance influence with user autonomy, offering multiple options rather than imposing single decisions.”
- “OAuth 2.0 and OWASP Top 10 compliance are baseline requirements for user data protection in financial AI systems.”

**Limits of relevance:**

- Study is conceptual/architectural; no quantitative performance metrics (e.g., MAE, precision@k) are reported for the integrated system.
- User population is not Filipino; income volatility and cultural spending norms (e.g., family obligations) are not addressed.
- The system assumes banking API integration (mentioned in Section 4), whereas Odin is manual‑entry only — may affect data availability for forecasting.
- LLM deployment costs and on‑device feasibility are not evaluated; Odin’s mobile‑first constraints may limit use of cloud‑hosted LLMs.

### Limitations

- No empirical evaluation — the paper presents architecture and models but no accuracy, retention, or usability metrics. [unacknowledged]
- Forecasting combination weight α is not optimized or benchmarked; arbitrary weighting may underperform adaptive methods.
- Isolation Forest anomaly detection thresholds are not specified; real‑world tuning requirements are omitted.
- LLM recommendation quality is not validated against human expert advice or user acceptance studies.
- Ethical claims (non‑manipulation, autonomy) are design intentions, not validated user outcomes. [unacknowledged]

---

## Source: `10.A/AI--Singh_2025_summarized.md`

**Title:** Digital Persona Modeling for Context-Aware Financial Decisioning

### TL;DR

Digital Persona Modeling (DPM) with LSTM, Random Forest, and K-Means improves context-aware financial decisions, achieving **93.6% accuracy** for sequential behavior modeling.

### Findings

1. LSTM achieved **93.6% accuracy** and 92.9% F1-score, outperforming Random Forest (91.2% accuracy, 90.1% F1) and K-Means (75.0% accuracy, 71.8% F1).
2. LSTM's strength lies in capturing temporal dependencies in user behavior and context shifts.

- Random Forest performed well for interpretable rule generation from tabular financial history.
- K-Means clustering produced lower accuracy but enabled unsupervised persona grouping.
- Context-aware risk function (location, time, device, transaction amount) enables real-time fraud intent detection.

### Relevance to Odin

**Topics:**

4.B — Limitations and Gaps in Existing Systems

5.A — Financial Behavioral Profiles in Personal Finance

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

7.B — Budget Recommendation in Personal Finance Systems

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

10.A — Data Privacy and Security in Personal Finance Systems

10.B — User Trust in Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper supports Odin's financial behavioral profiling module by demonstrating that dynamic, multi-layer personas (behavioral, contextual, psychographic) improve decision relevance over static profiles. The use of LSTM for sequential pattern analysis justifies Odin's forecasting module's consideration of temporal dependencies in spending behavior. The framework's privacy-preserving design (federated learning, local processing) aligns with Odin's data privacy requirements under RA 10173. The evaluation metrics (accuracy, F1, PLR) provide a template for Odin's algorithmic module evaluation, and the context-aware risk function directly informs Odin's anomaly detection design for fraud intent.

**Directly justifies:**

- "LSTM achieves 93.6% accuracy on sequential financial behavior patterns, outperforming Random Forest (91.2%) for context-aware decisioning."
- "Context-aware risk function incorporating location, time, device, and transaction amount enables real-time fraud intent detection."
- "K-Means clustering produces persona groups from spending style and risk tolerance without labeled data, supporting cold-start profiling."
- "Random Forest provides interpretable rule generation for financial risk classification, balancing accuracy and explainability."
- "Digital Persona Modeling shifts financial AI from static rules to dynamic, personalized agents, addressing limitations of generic advice tools."

**Limits of relevance:**

- Dataset is synthetic and simulated, not based on real Filipino financial behavior or spending patterns.
- No validation on mobile app with manual transaction input (Odin's core constraint; the study assumes rich contextual sensors).
- The study does not address cold-start profiling for new users with no transaction history.
- Contextual sensing (GPS, device type) may raise privacy concerns not fully addressed for the Philippine regulatory context.

### Limitations

- Data privacy concerns: heavy reliance on sensitive user data (location, behavior) increases breach risk. [acknowledged]
- Limited dataset diversity: synthetic data may lack geographic, cultural, and demographic variation, introducing bias. [acknowledged]
- Model generalizability: LSTM, RF, and K-Means may not generalize across unseen or fast-evolving financial ecosystems. [acknowledged]
- Interpretability challenges: deep learning models act as black boxes, reducing trust for audits and users. [acknowledged]
- No real-world deployment or user study with actual Filipino young professionals. [unacknowledged]

---

## Source: `10.A/AI--Zlobin_&_Bazylevych_2025_summarized.md`

**Title:** SYSTEMATIC REVIEW OF DEEP AND MACHINE LEARNING FOR FINANCIAL MODELING

### TL;DR

XGBoost outperforms all models in credit scoring, random forest achieves **99.6%** fraud detection accuracy, and LSTM reaches 93% stock prediction accuracy, but model interpretability remains the key barrier to adoption in finance.

### Findings

1. Random forest with ensemble feature selection achieved **99.6% accuracy and 100% precision** in credit card fraud detection (F1‑score 99.6%).
2. XGBoost consistently outperformed all deep learning models across 10 credit scoring datasets (highest AUC, lowest Brier score, and highest expected maximum profit).
3. LSTM networks predicted Vietnamese stock price trends with **93% accuracy**, outperforming linear regression models.
4. GRU‑CA hybrid model reduced anomaly detection RMSE on S&P 500 data from 13.28 to **9.74** (≈27% improvement) by adding a contextual attention module.
5. GCN achieved 94.5% fraud detection accuracy vs. CNN’s 93% on insider threat data, improving recall by 10 percentage points.

- CNN‑AdaBoost hybrid reached 96.35% accuracy for electricity theft detection, beating standalone CNN and AdaBoost.
- BS‑ANN hybrid option pricing model reduced pricing errors and achieved the lowest standard deviation among all tested models.
- AI personalization in fintech increased customer retention by 15% and engagement by 27% via collaborative filtering.

### Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

6.B — Spending Forecasting Algorithm

8.B — Anomaly Detection Algorithm

10.A — Data Privacy and Security in Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This systematic review directly supports Odin’s algorithm selection decisions across three core modules. For financial behavioral profiling (Topic 5.C), the paper shows XGBoost outperforms deep learning on tabular credit data – informing Odin’s classifier choice for user profile classification from transaction history. For spending forecasting (Topic 6.B), LSTM’s 93% stock trend accuracy and the hybrid GRU‑CA’s 27% RMSE reduction provide benchmarks for Odin’s sequential prediction module. The review also highlights federated learning as a privacy‑preserving technique (Topic 10.A), aligning with Odin’s data privacy requirements under RA 10173. Finally, the detailed reporting of performance metrics (accuracy, AUC, RMSE, F1) offers a template for evaluating Odin’s algorithmic modules (Topic 12.B).

**Directly justifies:**

- “XGBoost consistently outperforms deep neural networks across 10 retail credit scoring datasets on AUC, Brier score, and expected maximum profit, while being computationally cheaper.”
- “Random forest with ensemble feature selection achieves 99.6% fraud detection accuracy and 100% precision, making it suitable for real‑time anomaly detection in personal finance apps.”
- “LSTM networks achieve 93% accuracy in predicting stock price trends, outperforming linear regression and demonstrating the value of sequential memory for financial time series.”
- “The GRU‑CA hybrid model reduces anomaly detection RMSE by 27% (13.28 → 9.74) on S&P 500 data by adding a contextual attention mechanism that weights relevant market features.”
- “Federated learning enables collaborative model training across decentralized data sources while preserving data privacy – a necessary capability for financial apps that cannot share user transaction data.”

**Limits of relevance:**

- Review focuses on enterprise and market‑level finance (credit scoring, stock trading), not personal budget management systems.
- All cited studies use banking API or exchange data; Odin relies on manual transaction input, which may affect algorithm performance (sparser, less frequent data).
- No evaluation of mobile deployment constraints (CPU, memory, battery) for the reviewed deep learning models.
- Findings from Ukrainian, U.S., Vietnamese, and Chinese datasets may not fully generalize to Filipino young professionals’ spending behavior.
- Budget recommendation (Odin Topic 7) is not covered; no direct evidence for constraint‑based allocation algorithms.

### Limitations

- The review does not quantify computational costs (training time, memory) for each model, only mentions that deep learning is “considerably more computationally expensive.” [unacknowledged]
- Concept drift is identified as a major challenge, but no surveyed paper evaluates model adaptation or retraining strategies – a critical gap for long‑deployed personal finance systems. [unacknowledged]
- All fraud detection studies assume balanced or SMOTE‑corrected datasets; real‑world fraud rates (<1%) may degrade reported performance.
- The review excludes mobile‑specific constraints (offline operation, intermittent connectivity) that affect real‑time anomaly detection and forecasting.
- No paper in the review addresses budget recommendation or allocation; relevance to Odin’s core recommendation module is indirect.

---

## Source: `10.B/AI--Alammar_et-al_2026_summarized.md`

**Title:** Explainable AI (XAI) for transparent resource allocation in public safety communications networks

### TL;DR

SLIRA, a hybrid SHAP–LIME framework with Bayesian uncertainty, achieves near-optimal resource allocation while reducing fairness gaps by 40% and improving temporal stability by 31% in public safety networks.

### Findings

1. SLIRA achieved **0.981 ± 0.008 normalized utility** – within 2% of the optimal solver (1.000) but with 40.2% lower fairness gap.
2. Fairness gap dropped from 0.087 (solver) to **0.052 ± 0.008** – a 40% relative improvement.
3. Temporal stability gained 31.5% over the solver baseline, reaching very high consistency (0.967 in long‑run monitoring).

- SLIRA uniquely provides regulatory‑grade explainability: explanations actively govern allocation updates, not just post‑hoc diagnostics.
- Bayesian uncertainty estimates allow confidence‑aware decisions – a capability absent in solvers and black‑box models.

### Relevance to Odin

**Topics:**

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

10.B — User Trust in Personal Finance Systems

12.A — Evaluation Frameworks for Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper provides a template for making Odin’s anomaly detection and budget recommendation modules explainable to users. By integrating SHAP (global explanation of spending patterns) and LIME (local explanation for a single flagged transaction), Odin could justify why a particular expense is anomalous or why a budget limit was suggested – directly addressing user trust. The SLIRA framework’s fairness‑constrained, uncertainty‑aware design also informs how Odin’s evaluation module can measure explanation fidelity and stability, going beyond raw algorithm accuracy. Although the domain is emergency networks, the XAI methodology is fully transferable to personal finance, where users need to understand and trust AI‑driven alerts and recommendations.

**Directly justifies:**

- “A hybrid SHAP–LIME explanation mechanism can reduce the fairness gap in resource allocation by 40% while maintaining near‑optimal utility (within 2% of an optimal solver).”
- “Bayesian uncertainty quantification over explanations enables confidence‑aware decisions, essential when users must decide whether to act on an AI‑generated anomaly alert.”
- “Explanation consistency tracked over time (final value 0.967) ensures that interpretability does not degrade as user behavior patterns evolve.”
- “Regulatory‑grade explainability – where explanations actively govern allocation updates – produces higher temporal stability (+31.5%) than post‑hoc explanation methods.”

**Limits of relevance:**

- The study uses synthetic PSN traffic data, not real personal financial transactions; spending pattern complexity may differ.
- User trust was not measured directly with human subjects; the paper reports only algorithmic explainability metrics.
- Fairness constraints are applied to protected groups (e.g., police vs. medical); Odin’s fairness concerns involve income levels or spending categories, not demographic groups.
- The evaluation assumes a centralized controller with full state observability; Odin’s mobile‑first, manual‑input setting has sparser and noisier data.

### Limitations

- Synthetic dataset with controlled burst patterns; generalizability to real‑world emergency (or financial) data is unvalidated.
- User trust and human interpretability were not measured via user studies – only algorithmic consistency and fidelity. [unacknowledged]
- Fairness constraints assume known protected groups; Odin does not collect such attributes, so adaptation would require different fairness definitions.
- Runtime analysis (10.6 ms per step) was performed on a workstation; mobile device constraints are not considered.
- No comparison against other XAI methods (e.g., DeepLIFT, Integrated Gradients) to establish relative advantage.

---

## Source: `11.B/AI--Awasthi_&_Pandey_2025_summarized.md`

**Title:** How reinforcement learning can drive personalized financial wellness

### TL;DR

A DQN-based reinforcement learning agent, combined with K‑Means user personas and GPT‑powered conversation, learns personalized saving recommendations that outperform baseline strategies in a simulated personal finance environment.

### Findings

1. The learned DQN policy achieved an **average final savings of ~$450** across test episodes, significantly outperforming the “save $0” baseline (often negative) and closing the gap to the ideal “always save $50” benchmark (~$564 expected).
2. Training curves (Figure 2) show average episode reward rising from ~$20 to **$100–$120** over 5,000 episodes, demonstrating clear learning.
3. Persona clustering (Figure 1) produced interpretable groups, enabling persona‑conditioned policies (e.g., debt‑averse reward shaping for low‑income users).

- The conversational agent successfully wrapped numeric recommendations (e.g., “save $50”) into empathetic, persona‑appropriate explanations with follow‑up engagement questions.

### Relevance to Odin

**Topics:**

5.A — Financial Behavioral Profiles in Personal Finance

5.C — Financial Behavioral Profile Classification Algorithm

7.B — Budget Recommendation in Personal Finance Systems

7.C — Budget Recommendation Algorithm

11.B — Retention Mechanisms and Engagement Design

**Contribution to Odin:**

This paper directly justifies Odin’s use of unsupervised clustering (K‑Means) to build user personas from behavioral data (income, saving rate), enabling the system to tailor financial recommendations from the start — even before observing a new user’s transaction history. The MDP formulation of personal finance as a sequential decision problem provides a formal blueprint for Odin’s budget recommendation module, where actions (e.g., how much to save or allocate to a category) are learned to maximize long‑term financial wellness rather than following static rules. The integration of a conversational AI (GPT) as an interface layer demonstrates how Odin can explain recommendations in natural language, adapt tone to persona, and potentially collect user feedback — a mechanism shown to boost engagement and trust, directly supporting Odin’s value‑driven retention strategy.

**Directly justifies:**

- “Unsupervised clustering (K‑Means) on behavioral features (income, saving rate) produces interpretable user personas that can condition a recommendation policy, addressing the cold‑start problem in financial profiling.”
- “Deep Q‑Network (DQN) learns saving policies that improve final savings by >$400 over a naive baseline in a stochastic monthly budgeting environment, proving RL’s applicability to personal finance decision support.”
- “A conversational AI interface powered by GPT‑4 can translate RL numeric actions into empathetic, persona‑aware advice, improving user engagement and perceived trust without requiring fine‑tuning.”
- “Reward shaping in the MDP (e.g., penalizing debt for a low‑income persona) allows a single RL agent to produce different behaviors for different user types, enabling personalization without separate models.”

**Limits of relevance:**

- The simulated environment is highly simplified (fixed income, only one discretionary spending category, binary shock). Real‑world deployment would require more complex state and action spaces (multiple spending categories, debt vs. saving trade‑offs).
- User personas derived only from income and saving rate; Odin’s profiling should incorporate additional dimensions (e.g., spending volatility, family obligations, financial goals).
- No evaluation on real user data or live deployment; performance claims are from a synthetic environment.
- The paper does not address manual transaction entry (Odin’s scope) vs. API‑based data ingestion, which may affect state update frequency and data completeness.

### Limitations

- Environment and user data are entirely synthetic; external validity to real Filipino young professionals is unproven.
- The action space only controls saving amount; no joint actions for debt repayment, investment, or category‑level budgeting. [unacknowledged]
- Reward is final net savings only — does not penalize extreme frugality or user discomfort, which could lead to unrealistic recommendations.
- DQN with a discretized state table was used for the core experiment; the paper mentions neural DQN but does not provide comparative results. [unacknowledged]
- No user study or engagement metrics; the claim that conversational AI boosts trust is argued from prior literature, not measured.

---

## Source: `11.B/AI--Simeonov_et-al_2025_summarized.md`

**Title:** Analysing community-level spending behaviour contributing to high carbon emissions using stochastic block models

### TL;DR

Stochastic block modeling on bipartite spending networks identifies consumer groups with homogeneous carbon emission profiles, enabling scalable targeted interventions.

### Findings

1. Unweighted SBM produced clusters where customer transaction counts per MCC were tightly clustered around the mean, with near‑zero standard deviation.
2. **Weighted SBM (spending normalised by category average) produced clusters where percentage spending per category fell within one median absolute deviation (MAD) of the population median for 71/80 clusters (≥30 customers).**
3. Under half‑MAD threshold, 43/80 clusters still aligned; unweighted SBM had <50% within one MAD.
4. Specific emission drivers emerged per cluster: grocery (cluster 22), taxi (clusters 17‑18), service stations (clusters 3,11,12), public transport (cluster 20).

- Hierarchical SBM revealed nested community structures, allowing analysis at multiple granularity levels.

### Relevance to Odin

**Topics:**

4.A — Landscape of Existing Personal Finance Systems

4.B — Limitations and Gaps in Existing Systems

5.A — Financial Behavioral Profiles in Personal Finance

5.C — Financial Behavioral Profile Classification Algorithm

11.B — Retention Mechanisms and Engagement Design

**Contribution to Odin:**

This paper demonstrates that stochastic block modeling identifies consumer spending communities without requiring demographic or socio‑economic features, directly informing Odin’s financial behavioral profiling module. The finding that weighted SBM preserves average spending across communities while isolating category‑level emission drivers justifies using SBM over k‑means for Odin’s user classification, particularly when the goal is to test behavioural interventions across groups with identical spending patterns but different external characteristics. The paper’s emphasis on scalable, group‑level targeting (rather than individual nudges) supports Odin’s retention strategy: value‑driven engagement via community‑specific budget recommendations rather than gamification.

**Directly justifies:**

- “Stochastic block models detect consumer spending communities without demographic features, achieving near‑zero variance in category‑level transaction counts within clusters.”
- “Weighted SBM produces clusters where percentage spending per category falls within one median absolute deviation of the population median, enabling ceteris paribus analysis of external factors.”
- “Hierarchical SBM allows analysis at multiple granularity levels: lower levels capture fine‑grained habits, higher levels capture broad spending archetypes.”
- “Community detection on bipartite spending networks identifies which merchant categories drive emissions for each consumer group, enabling targeted behavioural interventions.”

**Limits of relevance:**

- Study population is UK‑based with higher environmental consciousness; Filipino young professionals may exhibit different spending patterns and carbon intensities.
- Carbon multipliers are UK‑specific (LCFS/UKMRIO); not directly transferable to Philippines without local input‑output data.
- Dataset excludes direct debits (utilities, rent) and cash transactions; Odin’s manual input model would capture these, but the SBM approach was not tested on such categories.
- SBM computational cost increases with dataset size; Odin’s mobile‑first constraints may require lighter community detection methods for real‑time profiling.

### Limitations

- Static network assumption: SBM does not account for temporal changes in spending behaviour; consumer profiles may drift over time. [unacknowledged]
- Computational expense: SBM inference is slower than k‑means, especially for million‑scale datasets; may limit real‑time profiling on mobile.
- Sample bias: customers are sustainability‑oriented and predominantly young; generalisability to average Filipino consumers is unknown.
- Missing high‑emission categories: utility payments (direct debit) and rent are underrepresented, potentially underestimating true emission footprints.
- No direct comparison to other clustering algorithms (k‑means, hierarchical) on the same dataset; the claimed advantages over distance‑based methods are referenced from literature, not empirically demonstrated.

---

## Source: `12.A/AI--Lee_et-al_2026_summarized.md`

**Title:** Comparing deep learning and classical regression approaches for predicting healthcare expenditure and spending: a systematic review

### TL;DR

Deep learning models (LSTM, CNN-LSTM) reduce healthcare cost prediction error by 10–20% over classical regression in longitudinal settings, but tree-based methods remain competitive for cross-sectional tabular data.

### Findings

1. Sequential deep models (LSTM, CNN-LSTM) achieved **10–20% lower RMSE/MAE** than classical regression in longitudinal cost forecasting tasks.
2. R² improvements of 0.01 to 0.15 for deep models over baselines; AUROC up to 0.78 for high-risk classification.
3. Stacked LSTM reduced RMSE by ~19% over ARIMA for medication spending time series.

- Shallow feedforward neural networks underperformed random forest on cross-sectional tabular data (adj-R² 0.316 vs 0.475).
- Prior costs and utilization were consistently the strongest predictors across all studies.
- Tree-based methods (random forest, GBM) remained highly competitive for cross-sectional, low-dimensional cost prediction.

### Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

12.A — Evaluation Frameworks for Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This systematic review directly informs Odin's spending forecasting module by benchmarking sequential deep learning architectures (LSTM, CNN-LSTM) against classical regression and tree-based methods on longitudinal expenditure data. The finding that LSTM reduces prediction error by 10–20% over regression on temporal sequences justifies selecting LSTM or hybrid models for Odin's per-category spending forecasting, especially given Odin's manual transaction input which generates sequential user history. The review's proposed Complexity–Performance Hypothesis provides a guiding principle for Odin's algorithm selection: match model capacity to data complexity — simple cold-start users may benefit from tree-based models, while established users with rich transaction histories justify LSTM. Finally, the evaluation metrics reported (RMSE, MAE, R²) establish a benchmark for Odin's module-level performance assessment.

**Directly justifies:**

- "Sequential deep learning models (LSTM, CNN-LSTM) reduce prediction error by 10–20% over classical regression on longitudinal cost data with temporal dependencies."
- "Tree-based methods (random forest, gradient boosting) outperform shallow feedforward neural networks on cross-sectional tabular data, suggesting they are better baselines for cold-start user profiles with limited history."
- "Prior costs and utilization are consistently the strongest predictors across all studies — Odin's forecasting module should heavily weight historical transaction sequences rather than demographic features alone."
- "The Complexity–Performance Hypothesis states that predictive accuracy is maximized when model capacity is matched to data complexity: simple data → simple models; rich temporal data → deep sequential models."

**Limits of relevance:**

- The prediction target is healthcare expenditure, not general personal spending; spending patterns differ in volatility and seasonality.
- All studies use institutional or claims data with automatic capture, not manual transaction entry as in Odin.
- No study includes Filipino populations or addresses cultural spending obligations (e.g., family remittances, 13th-month pay cycles).
- Prediction horizons are typically one year; Odin's forecasting may operate on monthly or weekly intervals.
- External validation across datasets is absent, limiting generalizability claims.

### Limitations

- Only eight studies were included, with substantial heterogeneity in design, data sources, and outcome definitions — no meta-analysis possible.
- No full external validation across independent datasets was performed in any included study. [unacknowledged]
- Prediction horizons were limited to one year in most studies, ignoring longer-term expenditure dynamics.
- Calibration, fairness, and decision-curve analyses were rarely reported.
- Social determinants of health and behavioral predictors were almost entirely omitted from model inputs. [unacknowledged]

---

## Source: `12.A/AI--Mehta_et-al_2025_summarized.md`

**Title:** Clustering and Similarity Learning in Financial Markets: A Tutorial for the Practitioners

### TL;DR

Clustering and similarity learning have evolved from static industry codes to adaptive, data‑driven frameworks integrating tabular, time‑series, text, and graph data for peer discovery across financial asset classes.

### Findings

- Adaptive, data‑driven similarity systems outperform static taxonomies (GICS, SIC) by capturing actual risk, liquidity, and thematic exposures.
- Evaluation must shift from abstract indices to operational validity: substitution fidelity for bonds, category reproducibility for funds, and segment utility for investors.
- Multimodal fusion (tabular + time‑series + text + graphs) is essential for robust peer discovery, especially in sparse or illiquid markets.
- Supervised similarity (Random Forest proximities, metric learning) aligns distance functions with task‑specific labels (e.g., fund categories, client segments).
- Open‑set similarity flags outliers (e.g., novel fund styles, market anomalies) beyond learned clusters.
- Investor clustering on transaction data reveals misalignments between elicited risk profiles and actual behavior, improving KYC and personalization.

### Relevance to Odin

**Topics:**

5.A — Financial Behavioral Profiles in Personal Finance

5.C — Financial Behavioral Profile Classification Algorithm

8.A — Anomaly Detection in Personal Finance Systems

12.A — Evaluation Frameworks for Personal Finance Systems

**Contribution to Odin:**

This paper directly informs Odin’s behavioral profiling and classification module by surveying clustering methods (k‑means, hierarchical, kernel metric learning) that can group users by transaction patterns, risk tolerance, and financial behavior. The discussion of supervised similarity (Random Forest proximities, contrastive learning) provides algorithmic justifications for cold‑start profiling and progressive reclassification as user data accumulates. Although the paper targets institutional investment, its emphasis on operational evaluation metrics (stability, segment utility) and open‑set outlier detection directly supports Odin’s anomaly detection and ISO 25010 evaluation requirements.

**Directly justifies:**

- “Clustering investors on transaction data reveals misalignments between self‑assessed risk profiles and actual trading behavior, supporting dynamic reclassification.”
- “Random Forest proximities produce interpretable, task‑specific similarity without requiring labeled ground truth, applicable to cold‑start user profiling.”
- “Open‑set similarity frameworks flag observations that fall outside all learned clusters — directly applicable to detecting anomalous spending patterns or new behavioral profiles.”
- “Evaluation of clustering must prioritize substitution fidelity and segment utility over abstract indices — a principle transferable to Odin’s module‑level performance metrics.”

**Limits of relevance:**

- Domain is institutional investment management, not personal budget management; transaction data volumes and risk objectives differ.
- Methods assume access to rich time‑series and textual data (e.g., prospectuses, filings) that Odin may not collect.
- No validation on Filipino young professionals or manual entry financial data.
- Some advanced methods (graph neural networks, multimodal transformers) exceed Odin’s computational scope for a mobile‑first system.

### Limitations

- Hyperparameter sensitivity: clustering outcomes vary with distance metric and preprocessing — acknowledged but not fully mitigated.
- Interpretability: deep similarity models (Siamese, GNNs) operate as black boxes, complicating fiduciary compliance.
- No universal ground truth for similarity — results depend on task and regime, making cross‑study comparison difficult. [unacknowledged]
- Most case studies use U.S. or European data; applicability to Philippine financial behavior and spending patterns is untested.
- Computational cost of multimodal fusion may exceed mobile‑first deployment constraints. [unacknowledged]

---

## Source: `12.B/AI--Agrawal_et-al_2025_summarized.md`

**Title:** Analyzing and Rewarding Credit Card Spending Habits in India: a Machine Learning Approach

### TL;DR

K-Means clustering segments credit card users by card type, and an optimized reward formula achieves **R² = 0.99** in predicting reward points.

### Findings

1. **K-Means achieved the highest silhouette score (0.42)** for card‑type based segmentation, outperforming DBSCAN and GMM.
2. **Random Forest achieved R² = 0.99** with lowest RMSE and MAE, beating Linear Regression and XGBoost.
3. Synthetic dataset reward points ranged **0–3500**, whereas original‑dataset‑based rewards capped at 1000.
- Clusters cleanly separated Platinum (high luxury/travel spend) from Silver (low essential spend).
- Expense‑type bonuses (travel +3, luxury +2) drove higher rewards for discretionary categories.
- Card Promotion Date (+2) and Income Category (+1) further personalized allocations.

### Relevance to Odin

**Topics:**

4.A — Landscape of Existing Personal Finance Systems

4.B — Limitations and Gaps in Existing Systems

5.A — Financial Behavioral Profiles in Personal Finance

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly justifies Odin’s choice of K‑Means for user segmentation in the financial behavioral profiling module, demonstrating that card‑type (a proxy for spending tier) produces interpretable clusters with silhouette score 0.42. The multi‑factor reward formula (RCT, ET, IC, NoC, AR) provides a template for Odin’s budget recommendation algorithm — weights can be repurposed as budget allocation coefficients. The finding that Random Forest achieves R²=0.99 with low error supports using ensemble regression for any prediction task in Odin (e.g., spending forecasting or reward points). Although the domain is credit card rewards, the method of clustering users based on spending patterns and validating with regression is transferable to cold‑start profile classification.

**Directly justifies:**

- “K‑Means clustering achieves a silhouette score of 0.42 for segmenting users by spending behavior, outperforming DBSCAN and GMM in financial transaction data.”
- “Random Forest regression achieves R²=0.99 for predicting reward points, with lower RMSE and MAE than XGBoost or Linear Regression.”
- “A multi‑factor scoring function (RCT, ET, IC, NoC, AR) personalizes allocations; expense type bonuses (e.g., travel +3) incentivize discretionary spending.”
- “Synthetic data with rich features (income category, attrition risk, card promotion date) yields wider reward distribution (0–3500) than sparse original data (capped at 1000).”

**Limits of relevance:**

- Study uses Indian credit card data; Filipino young professional spending patterns may differ (e.g., lower luxury spend, higher remittance/family obligations).
- Reward optimization domain differs from budget recommendation; the formula weights are suggestive, not directly adoptable without re‑calibration.
- Synthetic dataset (not real transaction logs) limits external validity for real‑world performance.
- No evaluation of temporal drift or seasonal adaptation beyond festive peak observations.

### Limitations

- Original dataset lacked user‑level identifiers and had outdated dates; synthetic generation may not capture real‑world noise. [unacknowledged]
- Clustering was validated only on card type as ground truth; no external behavioral outcome (e.g., retention) measured.
- Reward formula weights (e.g., RCT = 2.0 for Platinum) are arbitrary and not optimized via user feedback.
- Real‑time adaptability claimed but not demonstrated — system still batch‑based.
- No comparison with deep learning or transformer‑based sequence models for spending prediction.

---

## Source: `12.B/AI--Bader_&_Haraty_2025_summarized.md`

**Title:** Bridging AI and Emotion: Enhanced Models for Personal Finance Manager Applications

### TL;DR

Sentiment analysis integration reduces financial forecasting error by **25%** (MAPE 7.8% vs 10.5%) and anomaly detection achieves 92% accuracy with 90% precision in a personal finance manager.

### Findings

1. Sentiment analysis improved MAPE from **10.5% to 7.8%** – a **25% relative reduction** in prediction error.
2. Anomaly detection achieved **precision 90%**, recall 85%, F1‑score 87.5%, and ROC‑AUC **0.93**.
3. Predictive accuracy within 90% confidence interval reached **88%** alignment with actual user behavior.
4. **N‑BEATS was the best performer** (RMSE 0.057), followed by Transformer (0.062) and TCN (0.074).

- Sentiment‑aware models captured spending fluctuations more accurately than non‑sentiment versions, especially for N‑BEATS.
- Real‑time anomaly alerts with user feedback loops reduced false positives over time.

### Relevance to Odin

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

### Limitations

- Generalization across diverse financial behaviors and demographics not tested – Filipino young professionals may exhibit different patterns.
- Computational efficiency of deep learning models not benchmarked for mobile or low‑resource environments. [unacknowledged]
- User trust and adoption measured only via satisfaction surveys; no behavioral economics analysis of how users respond to sentiment‑based advice.
- Cold‑start scenario (new user with zero transactions) completely unaddressed – all models require historical data. [unacknowledged]
- Sentiment classification depends on text quality; manual‑input transactions may lack the descriptive richness of bank‑derived data.

---

## Source: `12.B/AI--Balbal_&_Birant_2026_summarized.md`

**Title:** RFM-Net: A Convolutional Neural Network for Customer Segment Classification

### TL;DR

RFM-Net, a lightweight CNN trained on Recency-Frequency-Monetary features, classifies customers into seven segments with **94.33% accuracy**, outperforming prior methods by 13.17%.

### Findings

1. RFM‑Net achieved **94.33% weighted accuracy** (10‑fold CV) on Online Retail I.
2. Weighted precision = 0.9466, recall = 0.9433, F‑measure = 0.9429.
3. Relative accuracy improvement of **13.17%** over previously reported results on the same dataset.
4. Two‑layer CNN with learning rate 0.01 and 32 filters gave optimal performance; deeper layers reduced accuracy.

- Recency ranked as most important feature (importance score 0.5358), followed by Frequency (0.4217) and Monetary (0.2642).

### Relevance to Odin

**Topics:**

5.A — Financial Behavioral Profiles in Personal Finance

5.C — Financial Behavioral Profile Classification Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly supports Odin’s financial behavioral profiling module by demonstrating that a lightweight CNN can classify users into behavioral segments using only three transaction-derived features (Recency, Frequency, Monetary). The finding that Recency is the most important predictor (importance 0.5358) informs feature selection for Odin’s profile classification — recency of spending (days since last transaction) may be a strong signal for user engagement state. The paper’s comparative benchmarking against MLP, logistic regression, and tree‑based models provides empirical justification for considering a compact CNN over traditional classifiers when the feature space is small but interactions are nonlinear.

**Directly justifies:**

- “A two‑layer CNN with 32 filters achieves 94.33% accuracy classifying users into seven behavioral segments using only Recency, Frequency, and Monetary features.”
- “Recency is the most important predictor of customer segment (importance 0.5358), followed by Frequency (0.4217) and Monetary (0.2642).”
- “Shallow CNNs (2–3 layers) outperform deeper architectures on low‑dimensional structured financial data, as deeper layers increase overfitting and reduce accuracy.”
- “RFM‑Net’s total parameter count of 6,823 (≈26.65 KB) enables real‑time inference on mobile devices, supporting mobile‑first deployment.”

**Limits of relevance:**

- Dataset is UK e‑commerce retail, not Philippine personal finance — spending patterns (e.g., gift purchases vs. daily essentials) differ.
- Segments are defined by marketing taxonomy (Champions, Hibernating), not directly aligned with Odin’s budget‑based behavioral profiles.
- Labels are derived from rule‑based RFM scores, introducing circularity; the CNN learns an expert mapping rather than discovering latent structures.
- No evaluation on cold‑start users — the dataset assumes established transaction histories.

### Limitations

- Labels generated from RFM rules, then used as ground truth for CNN — model learns a predefined mapping rather than discovering new segments. [unacknowledged]
- Feature set limited to R, F, M; does not include demographic or category‑level spending data that could improve profile granularity.
- Dataset from UK retail (2010–2011) may not generalize to 2020s Filipino young professionals with different spending habits and digital behaviors.
- No temporal validation or concept drift analysis — segment stability over time not assessed.
- Model interpretability is limited compared to rule‑based RFM; the paper suggests future SHAP/LIME integration.

---

## Source: `12.B/AI--Begum_2025_summarized.md`

**Title:** Machine Learning in Financial Risk and Behavior Analysis: Predictive Insights on Bankruptcy, Fraud, and Consumer Trends in the USA

### TL;DR

Gradient boosting (XGBoost AUC 0.93) and LSTM networks outperform logistic regression in bankruptcy prediction; stacking ensemble achieves F1 0.89 for fraud detection; LSTM beats ARIMA in consumer spending forecasts (MAE 2.8 vs 4.2).

### Findings

1. **Bankruptcy AUC:** XGBoost **0.93**, LightGBM 0.91, LSTM 0.92, ANN 0.89, Logistic Regression 0.76 — gradient boosting and LSTM dominate linear models.
2. **Fraud detection F1:** Stacking ensemble **0.89** (precision 0.91); GRU recall 0.89 vs XGBoost 0.81 — sequence models capture multi‑transaction fraud better.
3. **Forecasting error:** LSTM MAE 2.8, RMSE 3.3; ARIMA MAE 4.2, RMSE 5.1 — LSTM handles nonlinear trends and holiday spikes.

- Isolation Forest precision only 0.65 — works as anomaly supplement, not standalone solution.
- K‑Means silhouette 0.68 (well‑separated clusters); DBSCAN Davies‑Bouldin 0.52 (good separation but ε‑sensitive).
- Month‑to‑month contracts have highest churn; longer contracts improve retention.

### Relevance to Odin

**Topics:**

4.B — Limitations and Gaps in Existing Systems

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper benchmarks multiple ML families (gradient boosting, LSTM, GRU, Isolation Forest, clustering) on financial prediction tasks, providing direct evidence for algorithm selection in Odin’s forecasting and anomaly detection modules. The comparison of LSTM vs ARIMA on consumer spending sequences (MAE 2.8 vs 4.2) justifies choosing a sequential deep learning model over a statistical one for per‑category spending forecasts. The fraud detection results show that a stacking ensemble of supervised classifiers plus a GRU‑RNN achieves the highest F1 (0.89), which informs Odin’s design for anomalous spending detection. Additionally, the use of SMOTE for class imbalance and the evaluation metrics (AUC, F1, MAE, silhouette) offer a template for Odin’s module‑level validation.

**Directly justifies:**

- “LSTM achieves 32% lower MAE than ARIMA (2.8 vs 4.2) on consumer spending forecasting, demonstrating superior capture of nonlinear temporal patterns.”
- “A stacking ensemble of XGBoost, Random Forest, and GRU achieves F1 = 0.89 and precision = 0.91 for sequence‑based anomaly detection — outperforming any single classifier.”
- “K‑Means clustering yields a silhouette score of 0.68 on customer spending features, confirming that transaction frequency and amount can separate behavioral segments effectively.”
- “Isolation Forest precision is only 0.65 on imbalanced financial data, making it unsuitable as a standalone anomaly detector but useful as a supplementary method.”

**Limits of relevance:**

- All datasets are US‑based (corporate financials, payment processors) — spending patterns and fraud typologies may differ in the Philippines.
- The paper focuses on enterprise‑level bankruptcy and credit card fraud, not personal budget anomalies or overspending alerts.
- No evaluation of cold‑start performance (new users with no history) — critical for Odin’s initial user profiling.
- Models are trained on static, pre‑collected data — real‑time continuous learning is not tested.

### Limitations

- Relies on proprietary US datasets — no public data for replication or validation in other geographies.
- No cold‑start evaluation for any model — unknown performance for new users with no spending history [unacknowledged].
- Class imbalance in fraud (2% fraud rate) is addressed with SMOTE, but real‑world fraud may be even rarer.
- Consumer forecasting evaluated only on aggregated retail sales, not on individual user spending sequences.
- Does not address privacy‑preserving ML or on‑device deployment constraints relevant to mobile PFMS.

---

## Source: `12.B/AI--Caroprese_et-al_2025_summarized.md`

**Title:** Modelling Concept Drift in Dynamic Data Streams for Recommender Systems

### TL;DR

A stream-based data generator using user/item embeddings and concept drift detection produces realistic synthetic preference data for evaluating recommender systems.

### Findings

1. On the MIND dataset, **HR@5 averaged ~0.6–0.8** across batches; drift detection flagged changes aligned with news topic shifts.
2. On the Amazon Video Games dataset (original orientation, many items), synthetic frequency distributions diverged from real data due to insufficient item preferences.
3. **Inverting users and items** (fewer items than users) produced close frequency matches; HR@5 reached ~0.8 after adaptation.
4. On Yoochoose, a single major drift reduced HR@5 from ~0.7 to ~0.5, with recovery within batches.

- BPR outperformed a variational autoencoder on the inverted Amazon dataset (**HR@5 ~0.8 vs ~0.6**) when new items appeared over time; VAE was better on stable MIND data.
- A model trained only on the first regime performed poorly on later regimes, confirming drift necessity.

### Relevance to Odin

**Topics:**

5.B — Profile Dynamics and the Cold-Start Problem

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

8.A — Anomaly Detection in Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly informs Odin's need to detect and adapt to changes in user financial behavior (concept drift). The drift detection framework (monitoring loss on incoming transaction shards, triggering retraining when error rises) justifies a similar mechanism in Odin's profiling and forecasting modules: as a user's spending patterns shift (e.g., new job, holiday season), the system must update its behavioral profile and budget recommendations. The embedding‑based BPR model, while designed for recommendations, provides a template for representing users in a latent financial space. The paper's evaluation of continual learning (generating synthetic samples to retain past knowledge) supports Odin's design of a lightweight online update strategy without storing full history. The comparative analysis of BPR vs VAE under item‑arrival drift (inverted Amazon) shows that adaptive models outperform static ones when new categories appear — directly relevant to Odin's handling of new expense types or merchants.

**Directly justifies:**

- “Concept drift in user preferences can be detected online by monitoring a loss function on test shards using HDDMW, triggering model retraining when error exceeds Hoeffding bounds.”
- “When a drift is detected, extending the latent dimension (ΔK) and penalizing deviation from prior embeddings (Ld loss) balances adaptation with stability.”
- “A model trained only on historical data (first regime) degrades sharply on later regimes; continual learning with synthetic sample replay maintains performance.”
- “On streams with many new items appearing over time, an adaptive BPR model achieves HR@5 ~0.8, outperforming a fixed‑catalog VAE (HR@5 ~0.6).”
- “Cold‑start handling (new users/items) is identified as a future direction, but the proposed graph‑based drift modeling provides a foundation for addressing it.”

**Limits of relevance:**

- Domain is e‑commerce/news recommendation, not personal finance; spending behavior drift may have different temporal characteristics.
- Uses implicit binary feedback (click/read), whereas Odin has transaction amounts and categories.
- No evaluation on financial data or Philippine user populations.
- Cold‑start solution is not implemented; only mentioned as future work.
- Assumes ability to sample negative items uniformly at random, which may not hold for sparse financial transactions.

### Limitations

- The approach assumes geometric closeness in latent space as the preference model; other preference structures (e.g., Markovian) are not handled. [unacknowledged]
- Synthetic generation fidelity depends heavily on sufficient item preferences; fails when items outnumber users (Amazon original orientation).
- Drift detection using loss on test shards requires a held‑out set; not evaluated in pure online settings where labels arrive late.
- The method extends latent dimensions on drift but does not prune obsolete dimensions, potentially increasing memory over time. [unacknowledged]
- No user study or qualitative validation that generated drifts match real preference evolution in financial contexts.

---

## Source: `12.B/AI--Chowdhury_et-al_2025_summarized.md`

**Title:** A SYSTEMATIC REVIEW OF DEMAND FORECASTING MODELS FOR RETAIL E-COMMERCE ENHANCING ACCURACY IN INVENTORY AND DELIVERY PLANNING

### TL;DR

Deep learning (LSTM, transformers) and hybrid ARIMA-ML models consistently outperform traditional statistical methods, improving forecast accuracy by up to 20% in volatile e-commerce demand scenarios.

### Findings

1. Machine learning models (31 studies, 4,800 citations) **improve RMSE and MAPE by up to 20% over statistical methods** in short‑term, high‑frequency forecasting.
2. Deep learning models (22 studies, 3,900 citations) excel at capturing nonlinear patterns, long‑term dependencies, and multivariate inputs, especially for SKU‑level demand.
3. Hybrid ARIMA‑ML/DL models (18 studies, 2,500 citations) balance interpretability and accuracy, performing well during promotional spikes and structural breaks.
4. External data integration (27 studies, 5,000 citations) — weather, sentiment, clickstream — significantly enhances forecast performance in volatile, promotion‑sensitive categories.

- Traditional models (ARIMA, Holt‑Winters) remain relevant for stable, seasonal demand and as benchmarks, but fail under nonlinearity and external shocks.

### Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This systematic review directly informs Odin's spending forecasting module by providing a comparative analysis of candidate algorithms (LSTM, GRU, ARIMA, hybrid models) and their performance trade-offs. The finding that LSTM and GRU capture temporal dependencies in irregular, high‑frequency transaction sequences justifies selecting recurrent neural networks over simpler methods for forecasting per‑category spending. The review's benchmarking of evaluation metrics (MAE, RMSE, MAPE) supports Odin's module evaluation framework under ISO 25010, and the discussion of hybrid models offers a path to balance accuracy with interpretability when explaining budget recommendations.

**Directly justifies:**

- "LSTM and GRU networks capture long‑range temporal dependencies and nonlinear demand patterns, outperforming traditional statistical models by up to 20% in RMSE/MAPE on volatile retail data."
- "Machine learning models (random forests, gradient boosting) provide 15–20% accuracy improvement over ARIMA for short‑term forecasting with multivariate inputs such as promotions and web traffic."
- "Hybrid ARIMA‑ML/DL models balance interpretability and accuracy, making them suitable for production systems where explainability is required alongside predictive power."
- "Integration of external variables (weather, sentiment, economic indicators) significantly enhances forecast accuracy in volatile environments, a principle applicable to personal finance with income volatility and cultural spending cycles."

**Limits of relevance:**

- Domain is retail e‑commerce inventory and delivery planning, not personal spending behavior — spending patterns may have different volatility drivers.
- No evaluation of cold‑start forecasting (new users with no transaction history), which is critical for Odin's initial user experience.
- External data sources (e.g., social media sentiment, weather) may not be available or relevant for personal finance.
- All reviewed studies use international datasets; Filipino‑specific income volatility and cultural obligations (e.g., remittances, family support) are not addressed.

### Limitations

- Traditional models underperform under nonlinear, promotional, or external shock conditions — acknowledged in the review.
- Hybrid models are underutilized in operational systems due to design complexity and maintenance overhead — acknowledged.
- No discussion of mobile‑specific constraints (computational limits, offline operation) for deploying deep learning models — [unacknowledged].
- Generalizability to personal finance domain is untested; spending behavior may have different stationarity and seasonality properties — [unacknowledged].
- All studies come from international contexts (US, China, Europe); no Philippine‑specific validation of forecasting models — [unacknowledged].

---

## Source: `12.B/AI--Krstev_et-al_2023_summarized.md`

**Title:** An Overview of Forecasting Methods for Monthly Electricity Consumption

### TL;DR

Neural network autoregression (NNAR) achieved the lowest forecasting error (MAPE = 2.67%) for monthly electricity consumption, outperforming classical time series and other machine learning methods.

### Findings

1. NNAR(3,1,6) achieved the **lowest MAPE of 2.67%** — the best among all twelve methods.
2. Classical time series performed better than most ML methods: ETS(A,N,A) at 3.28%, ARIMA at 3.36%, BSM at 3.87%, seasonal naïve at 4.16%.
3. Best ML result came from PCA+KNN with MAPE 4.38%; worst was PCA+XGBM at 7.35%.

- For small sample sizes (228 monthly observations), statistical methods (ETS, ARIMA) outperformed most ML methods except NNAR — consistent with prior findings that ML requires larger data.
- Absolute relative errors varied by month; NNAR gave <1% error for five months (Mar, Aug, Sep, Dec 2019, Jan 2020).

### Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper provides a direct benchmark for Odin’s spending forecasting module by comparing twelve forecasting methods on monthly time series data. The finding that NNAR (neural network autoregression) achieves the lowest MAPE (2.67%) justifies considering neural network architectures for per-category spending prediction, even on modest-sized historical datasets (228 months). The observation that classical methods (ETS, ARIMA) outperform most ML methods when sample size is limited directly informs Odin’s cold-start strategy: for new users with few transactions, a simpler statistical forecaster may be more accurate than a complex ML model until sufficient spending history accumulates.

**Directly justifies:**

- "Neural network autoregression (NNAR) achieved 2.67% MAPE on monthly consumption forecasting, outperforming ARIMA (3.36%) and ETS (3.28%) on a 228-month univariate time series."
- "For small to medium-sized time series (under ~250 observations), classical statistical methods (ETS, ARIMA) produce lower forecast error than most machine learning models, with the exception of neural networks."
- "PCA-based feature selection improved MAPE for 6 of 7 ML methods compared to linear-model feature selection, reducing error by up to 2 percentage points."
- "Seasonal naïve forecasting — repeating the same month’s value from the prior year — achieved 4.16% MAPE, serving as a simple baseline for evaluating more complex forecasting algorithms."

**Limits of relevance:**

- Domain is electricity consumption, not personal spending; temporal patterns and volatility differ.
- Dataset is aggregated monthly consumption, whereas Odin operates on per-transaction daily or weekly spending.
- No evaluation of cold-start performance (forecasting with <12 months of history), which is critical for new Odin users.
- The study assumes stationary seasonality (annual cycle); Filipino spending may have multiple cycles (monthly paydays, 13th-month pay, holidays).

### Limitations

- Only univariate forecasting (past consumption alone); Odin’s spending could benefit from exogenous variables (income, priorities) not considered here.
- No explicit cold-start evaluation — all models trained on ≥19 years of data; performance with limited history is unknown. [unacknowledged]
- Dataset is from Bosnia and Herzegovina; seasonal and trend patterns may not generalize to Metro Manila’s tropical climate and financial calendar.
- MAPE can be misleading when actual values are near zero (common in spending categories); the paper does not discuss this limitation.
- Neural network architecture (NNAR) is relatively simple (single hidden layer); deeper architectures like LSTM were cited but not implemented for MTLF.

---

## Source: `12.B/AI--Leibiker_&_Talmon_2023_summarized.md`

**Title:** A Recommendation System for Participatory Budgeting

### TL;DR

Predicting missing voter preferences in participatory budgeting using binary classification (XGBoost) achieves higher budget allocation accuracy than sampling, enabling all voters to participate with fewer inputs.

### Findings

- Classification (XGBoost) outperformed MF and FM across all sampling setups.
- Online and offline-popularity sampling achieved higher FA scores than random sampling.
- At 10% sample degree, classification-online matched the FA score of sampling at 30% sample degree, requiring less voter input.
- FA and SD improved monotonically with sample degree and LV degree (sanity test confirmed).
- Classification-online and classification-offline-popularity performed best overall, especially at low sample degrees (0.1–0.3).

### Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

7.C — Budget Recommendation Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper demonstrates that binary classification (XGBoost) outperforms collaborative filtering methods (MF, FM) for predicting missing user preferences from partial inputs, directly informing Odin's cold-start profile classification module. The evaluation framework—using FA score to measure budget allocation correctness rather than just ballot accuracy—provides a template for Odin's module-level evaluation beyond simple classification metrics. Although the domain is public budgeting, the technique of adaptively sampling the most controversial items (online controversial) to maximize prediction accuracy with minimal user input is directly transferable to Odin's preference elicitation for budget recommendation.

**Directly justifies:**

- "XGBoost with weighted loss functions handles imbalanced approval data (≈10% approval rate) and improves prediction of minority class compared to MF and FM."
- "Online adaptive sampling (revealing most controversial projects first) yields higher prediction accuracy than random sampling when collecting partial user preferences from sparse data."
- "Fractional Allocation (FA) score—sum of correctly predicted winning project costs divided by total budget—captures financial impact of prediction errors better than per-item accuracy metrics."
- "Greedy approval (funding highest-approved projects until budget exhausted) serves as a baseline budget allocation rule that balances popularity and cost constraints."

**Limits of relevance:**

- Domain is public participatory budgeting (collective spending), not personal budget management (individual spending).
- Data from Warsaw, Poland; not representative of Filipino young professionals' financial behavior or cultural spending patterns.
- No temporal dynamics or sequential transaction history; predictions are static per ballot, not time-series forecasting.
- Evaluation assumes full ground truth ballots exist; Odin's cold-start has no prior user data.

### Limitations

- Only tested on approval-based combinatorial PB; other PB variants (e.g., cumulative voting) not evaluated.
- Data from a single country (Poland); generalizability to other cultural contexts unknown. [unacknowledged]
- No comparison to deep learning methods (e.g., neural collaborative filtering).
- Interactive correction loop (voter refining predictions) proposed but not implemented or tested.
- Real-time deployment constraints (latency, mobile compute) not considered. [unacknowledged]

---

## Source: `12.B/AI--O'Connor_et-al_2025_summarized.md`

**Title:** A Review of Electricity Price Forecasting Models in the Day-Ahead, Intra-Day, and Balancing Markets

### TL;DR

Hybrid and ensemble models dominate day-ahead forecasting; recurrent neural networks lead intra-day; simple regularized models like LEAR outperform complex DL in volatile balancing markets due to overfitting.

### Findings

- Hybrid and ensemble models (XGB, LSTM-CNN) consistently outperform standalone models in day-ahead markets.
- LSTM and GRU dominate intra-day forecasting due to effective capture of short-term dependencies.
- **LEAR (LASSO-elastic net AR) outperforms complex DL models in balancing markets**, where volatility and data sparsity cause overfitting.
- Simple naive models remain competitive baselines in real-time markets due to strong autocorrelations.
- MAPE is unsuitable for balancing markets because prices approach zero, inflating errors.

### Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper's comparative review of forecasting algorithms directly informs Odin's spending forecasting module selection. The finding that LEAR outperforms complex DL models in volatile, data-sparse environments (balancing market) justifies using regularized linear models for cold-start or sparse user spending data. The paper's analysis of evaluation metrics (MAPE's failure near zero) guides Odin's choice of MAE or sMAPE for spending forecast evaluation. The observation that simpler models avoid overfitting in high-volatility contexts supports Odin's algorithm selection for users with short transaction histories.

**Directly justifies:**

- "Regularized AR models (LEAR) outperform LSTM and GRU in volatile, data-sparse markets by avoiding overfitting."
- "MAPE is unreliable when values approach zero; MAE or sMAPE are preferred for sparse or near-zero spending periods."
- "Hybrid CNN-LSTM architectures capture both local patterns and sequential dependencies, improving forecast accuracy."
- "XGB and LGBM balance accuracy and computational cost, making them suitable for mobile deployment with moderate data volumes."

**Limits of relevance:**

- Domain is electricity prices, not personal spending; volatility patterns and seasonality differ.
- No user behavior or cultural spending factors considered.
- No mobile-specific constraints (latency, battery, offline operation) analyzed.
- Cold-start problem (new users with no history) is not explicitly addressed.

### Limitations

- Focuses only on point forecasting, not probabilistic forecasts that provide uncertainty bounds. [unacknowledged]
- No standard benchmark for intra-day or balancing markets — results are not directly comparable across studies.
- MAPE is widely used despite known flaws; the review critiques it but does not propose a unified alternative.
- Discussion of data sparsity in balancing markets is relevant but no specific cold-start solution is offered. [unacknowledged]
- Computational cost comparisons between models are qualitative; no runtime benchmarks are provided.

---

## Source: `12.B/AI--Polytarchos_2025_summarized.md`

**Title:** Credit Card Fraud Detection Through Deep Learning and Real-Time Data Streams: A Comparison and New Directions

### TL;DR

Real-time clustering (BEReTiC) offers lower false positives (0.003%) than deep learning (0.007%) but lower classification accuracy (66% vs 92% for total funds range).

### Findings

1. LSTM achieved **92% accuracy** predicting “total funds range” – the highest among all labels; MLP reached only 78% for the same label.
2. Deep learning detected 788/1000 injected fraudulent transactions with 1,340 false positives (0.007% misclassification rate).
3. Real‑time clustering detected 619/1000 injected frauds with 574 false positives – a **0.003% misclassification rate** (lower than deep learning).

- Real‑time accuracy per label was substantially lower (e.g., 66% for total funds range) due to cold‑start: the system lacks historical data early in the stream.
- Real‑time clustering adapts to new fraud patterns without retraining; deep learning requires periodic retraining to handle concept drift.

### Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

6.B — Spending Forecasting Algorithm

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly informs Odin’s anomaly detection module by benchmarking batch‑trained deep learning (LSTM/MLP) against a real‑time unsupervised clustering algorithm (BEReTiC), highlighting the accuracy‑vs‑latency trade‑off essential for mobile‑first personal finance. The finding that real‑time clustering achieves lower false positives (0.003%) without data preprocessing supports Odin’s design for manual entry and cold‑start users where labeled fraud data is unavailable. Although the domain is credit card fraud, the comparative methodology and algorithm candidates (LSTM for time‑series, unsupervised clustering for anomalies) transfer directly to spending anomaly detection and behavioral profile classification in Odin.

**Directly justifies:**

- “LSTM achieved 92% accuracy predicting customer total funds range on a 17.5M transaction dataset, demonstrating its strength in time‑series demographic classification.”
- “Real‑time unsupervised clustering (BEReTiC) detected fraud with a 0.003% misclassification rate and 574 false positives, compared to deep learning’s 0.007% rate and 1,340 false positives.”
- “Real‑time clustering adapts to new fraud patterns without retraining, while deep learning requires periodic retraining to handle concept drift.”
- “Cold‑start significantly reduces real‑time clustering accuracy (66% vs 92% for deep learning), a critical design consideration for new Odin users with no transaction history.”

**Limits of relevance:**

- Study uses credit card fraud data from Greece; Filipino young professionals’ spending anomalies may differ (e.g., family obligations, informal transfers).
- Domain is fraud detection, not personal budget anomaly detection (overspending vs budget thresholds), though the unsupervised method is transferable.
- Datasets are bank‑provided and labeled; Odin uses manual input without ground‑truth fraud labels.
- Real‑time clustering’s lower accuracy may be unacceptable for core classification tasks in Odin unless hybridized.

### Limitations

- No cross‑validation on a held‑out test set from a different time period; generalization to future fraud patterns unassessed. [unacknowledged]
- Synthetic fraud injection may not replicate real fraudsters’ adaptive tactics, overestimating detection rates.
- Real‑time clustering’s accuracy never reaches deep learning’s level even after full data ingestion – a permanent trade‑off.
- Dataset not publicly available (NDA), preventing replication or adaptation to Philippine spending data.
- No evaluation of computational resource usage on mobile devices; Odin’s mobile‑first constraint is not addressed.

---

## Source: `12.B/AI--Scrivano_2025_summarized.md`

**Title:** Time-Series Forecasting Using Deep Learning and Data Mining Models

### TL;DR

Transformer models reduced MAE by **12–17%** over LSTM and TCN on retail datasets, while Gradient Boosting Machines achieved the lowest MAPE (8.0%) on financial data.

### Findings

1. **Transformer models achieved 12–17% lower MAE than LSTM and TCN on retail datasets** (Table 1: LSTM MAE 34500, Transformer MAE 27500).
2. Gradient Boosting Machine outperformed Random Forest across all three domains, achieving MAPE as low as 8.0% on finance data (Table 3: GBM MAPE 8.0% vs Random Forest 8.7%).
3. TCN attained 20% higher accuracy in early-stage anomaly detection from industrial sensor data compared to traditional methods.

- LSTM reduced mean absolute error by 15% over conventional methods in web traffic prediction when encoding day-of-week patterns.
- Transformer and Gradient Boosting showed strongest probabilistic forecasting performance (quantile loss coverage).

### Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

8.B — Anomaly Detection Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly informs Odin's algorithm selection for spending forecasting and anomaly detection by providing comparative benchmarks on real-world time-series data. The finding that Transformers reduce MAE by 12–17% over LSTM on retail sequences supports evaluating attention-based models for transaction forecasting in Odin's forecasting module. Gradient Boosting Machines' superior performance on structured financial data (8.0% MAPE) justifies their use for behavioral profiling classification, particularly given Odin's need for interpretability. The paper's evaluation framework (MAE, RMSE, MAPE, quantile loss) aligns with Odin's multi-metric assessment requirements for algorithmic modules under ISO 25010.

**Directly justifies:**

- "Transformer models achieved 12–17% lower MAE than LSTM and TCN on retail time-series forecasting tasks (Table 1: LSTM MAE 34500, Transformer MAE 27500)."
- "Gradient Boosting Machines outperformed Random Forest across energy, finance, and retail datasets, achieving MAPE as low as 8.0% on finance data (Table 3)."
- "Temporal Convolutional Networks attained 20% higher accuracy in early-stage anomaly detection from sensor data compared to traditional methods, supporting TCN as a candidate for Odin's anomaly detection module."
- "LSTM networks reduced mean absolute error by 15% over conventional methods when encoding temporal metadata such as day-of-week patterns, applicable to Odin's calendar-aware spending forecasts."

**Limits of relevance:**

- Datasets are not specific to personal finance or individual spending transactions; results are from energy, retail, and financial market data.
- Anomaly detection examples are industrial sensor data (machinery vibration), not financial anomalies like budget overages.
- No evaluation on cold-start conditions (new users with no transaction history), a critical gap for Odin's profiling module.
- Computational demands of Transformers may exceed mobile constraints; the paper does not address mobile deployment.

### Limitations

- Models require large, high-quality datasets; many real-world domains (including personal finance for new users) lack such data.
- Transformer computational demands limit deployment in resource-constrained environments (mobile devices). [unacknowledged]
- Generalizability across domains is not guaranteed; the paper notes that hybrid models need careful calibration to avoid overfitting.
- Probabilistic forecasting evaluation remains nascent; the paper highlights uncertainty quantification as a persistent gap.
- No comparison of model performance on irregularly sampled or sparse time-series, which characterizes manual transaction entry. [unacknowledged]

---

## Source: `12.B/AI--Wu_et-al_2026_summarized.md`

**Title:** Test-Time Adaptation for Non-stationary Time Series: From Synthetic Regime Shifts to Financial Markets

### TL;DR

Updating batch‑normalization statistics at test time is a safe default for financial forecasting, while updating affine parameters helps under smooth drift but can hurt on noisy real markets.

### Findings

1. Under synthetic gradual drift on ETTh1, norm_only reduced MAE from 0.28 to 0.22 (R² improved from -0.31 to -0.02), but structural switches caused large errors (R² = -20.8) even with bn_stats.
2. On QQQ direction classification, bn_stats achieved **52.5% accuracy vs. 50.3% for no_tta** (DM p = 0.022), while norm_only dropped to 46.3%.
3. Diebold–Mariano tests: bn_stats significantly better than no_tta on SPY (DM = -2.78, p=0.005) and QQQ (DM = -2.29, p=0.022); norm_only significantly worse on both (p<0.001).
4. In backtests, bn_stats produced the highest Sharpe ratio on SPY (1.93 vs. 1.75 for no_tta) and QQQ (4.08 vs. 3.21 for no_tta); norm_only underperformed (Sharpe 1.54 and 1.35).

- Rolling metrics show TTA gains concentrated in pandemic and early recovery periods when distributional change is strongest.
- Uncertainty fallback mitigated harmful norm_only updates but did not fully prevent overfitting on noisy windows.

### Relevance to Odin

**Topics:**

5.B — Profile Dynamics and the Cold‑Start Problem

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly informs Odin’s spending forecasting module by demonstrating when lightweight test‑time adaptation (bn_stats vs. norm_only) improves forecast accuracy under distribution shifts – a core challenge as user spending patterns evolve. The finding that simple BN statistics refresh outperforms gradient‑based norm_only on noisy real‑world data (equity markets) provides a strong justification for using a conservative, zero‑gradient adaptation strategy in Odin’s forecasting pipeline, especially given manual transaction input which may produce irregular, noisy sequences. The paper’s use of Diebold–Mariano tests and Newey–West adjustments offers a template for evaluating Odin’s module‑level performance under non‑stationary user behavior.

**Directly justifies:**

- “Refreshing batch‑normalization statistics at test time (bn_stats) improves direction accuracy on QQQ from 50.3% to 52.5% (p = 0.022) without requiring gradient updates.”
- “Gradient‑based norm‑only adaptation can hurt performance on noisy financial series – on QQQ accuracy dropped to 46.3% despite drift control and uncertainty fallback.”
- “Quadratic drift penalty and uncertainty‑triggered fallback (80th percentile of entropy/augmentation variance) reduce harmful updates, but do not fully prevent overfitting on short windows.”
- “Diebold–Mariano tests with Newey–West HAC variance estimation provide statistically rigorous comparison of forecast losses under autocorrelated daily errors.”
- “Synthetic gradual drift (mean/variance shift) is well handled by norm‑only adaptation (MAE 0.22 vs. 0.28), suggesting value for slow concept drift in user spending patterns.”

**Limits of relevance:**

- Financial returns have different dynamics than personal spending sequences (e.g., lower signal‑to‑noise, heavy tails).
- The study uses daily prices; Odin’s transactions are irregular and user‑logged, not regularly spaced.
- No evaluation on cold‑start users – all models had historical training windows before deployment.
- Benchmark datasets (ETT, equity indices) are not from personal finance or Filipino context.

### Limitations

- All financial experiments use daily OHLCV only; no user‑level transaction data or personal budgets. [unacknowledged]
- Synthetic shifts on ETT are stylized and may not capture real spending pattern changes (e.g., payday cycles, unexpected expenses). [unacknowledged]
- Backtest strategy is a simple directional bet (long/neutral) ignoring transaction costs and slippage, so Sharpe ratios are upper bounds.
- Uncertainty threshold τ = 80th percentile was set on validation; optimal threshold may vary across users or regimes.
- Only one backbone size (TCN hidden 64) and fixed window length (L=96); sensitivity to input frequency (e.g., daily vs. weekly) not explored.

---

## Source: `12.B/AI--Yunita_et-al_2025_summarized.md`

**Title:** Performance analysis of neural network architectures for time series forecasting: A comparative study of RNN, LSTM, GRU, and hybrid models

### TL;DR

No statistically significant difference among nine RNN architectures (p=.127), but LSTM-based hybrids consistently outperform standalone models across three real-world datasets.

### Findings

1. **Friedman test showed no statistically significant difference** among nine architectures (χ² = 12.593, df = 8, p = .127).
2. **LSTM-GRU achieved the lowest mean rank (2.23)** across all datasets; vanilla RNN had the highest mean rank (8.57).
3. **LSTM-RNN performed best on sunspot (MAE=16.96, RMSE=23.39)** and oxygen datasets (MAE=2.97, MAPE=7.42%, RMSE=4.04).
4. **Standalone LSTM was best for COVID-19 forecasting** (MAE=0.90, MAPE=9.04%, RMSE=1.16), beating hybrids on percentage error.
5. **Vanilla RNN had fastest training (<20s per iteration) but highest errors** — e.g., sunspot MAPE=50.94% vs. LSTM-RNN’s 37.28%.

- Hybrid models generally had slightly longer training times but more stable predictions (narrower boxplot spreads).

### Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly informs Odin’s spending forecasting module by benchmarking nine RNN-family algorithms under controlled, repeatable conditions. The finding that LSTM-based hybrids (especially LSTM-RNN and LSTM-GRU) perform best across diverse temporal patterns justifies their selection for forecasting user spending, where transaction sequences have irregular intervals and varying volatility. The Monte Carlo evaluation protocol — 100 runs to account for random initialization — provides a methodological template for Odin’s own algorithm validation, ensuring that reported performance is not due to lucky weight initializations.

**Directly justifies:**

- “LSTM-RNN hybrid achieves the lowest MAE (2.97) and MAPE (7.42%) on a real‑world sensor time series, outperforming standalone LSTM and GRU.”
- “No statistically significant difference among nine RNN architectures (p=.127) suggests that practical considerations — computational cost and stability — should guide model selection, not just point estimates.”
- “Monte Carlo simulation with 100 iterations reveals that LSTM‑based hybrids have narrower error spreads than standalone RNN, indicating more consistent forecasts under random initialization.”
- “Vanilla RNN’s MAPE on sunspot data (50.94%) is 13 percentage points worse than LSTM‑RNN (37.28%) — a gap that would materially degrade spending forecasts for volatile categories.”

**Limits of relevance:**

- Datasets are non‑financial (sunspots, disease cases, oxygen levels); spending transaction sequences may have different autocorrelation structures.
- All models were evaluated on univariate time series; Odin’s forecasting may benefit from multivariate inputs (e.g., day of week, income timing).
- Training used 100 epochs per run; Odin’s on‑device or cloud training budget may be more constrained.
- No explicit evaluation of cold‑start performance (fewer than 30 transactions), which is critical for new Odin users.

### Limitations

- Only three datasets used — small sample size may have masked true performance differences (paper acknowledges this).
- Friedman test non‑significance could be due to low statistical power, not genuine equivalence. [unacknowledged]
- No hyperparameter tuning — all models used fixed architectures (2 hidden layers, 64 units per layer) — may favor certain models.
- Paper removed outliers by trimming 2.5% from Monte Carlo results; this may discard legitimate extreme forecast errors that matter in budgeting.
- No comparison with traditional statistical baselines (ARIMA, exponential smoothing) — only neural architectures are benchmarked.

---

## Source: `3.A/AI--Pratama_&_Putri_2024_summarized.md`

**Title:** User Profiling Based on Financial Transaction Patterns: A Clustering Approach for User Segmentation

### TL;DR

K-means clustering on transaction amount, time, and type identifies three user segments with distinct spending behaviors, achieving a moderate Silhouette Score of 0.33.

### Findings

1. Three distinct clusters identified: Cluster 0 (purchases, ~11 AM Monday, mean amount 1877), Cluster 1 (transfers, ~1:35 PM Wednesday, mean amount 4147), Cluster 2 (purchases, ~11 AM Friday, mean amount 1970).
2. **Silhouette Score of 0.33** indicates moderate cluster separation with some overlap.
3. Cluster distribution: Cluster 2 highest transaction count (>20), Cluster 0 lowest (<15).

- PCA and t-SNE visualizations show clear separation between clusters in reduced dimensions.
- One-month dataset limits detection of seasonal or long-term behavioral trends.

### Relevance to Odin

**Topics:**

3.A — Expense Categorization Frameworks

5.A — Financial Behavioral Profiles in Personal Finance

5.C — Financial Behavioral Profile Classification Algorithm

8.A — Anomaly Detection in Personal Finance Systems

**Contribution to Odin:**

This paper directly informs Odin's financial behavioral profiling module by demonstrating that K-means clustering on transaction amount, time, and type can segment users into interpretable behavioral groups. The use of transaction type (purchase vs. transfer) as a feature aligns with Odin's expense categorization design. Although the dataset is simulated and not Filipino, the methodology provides a baseline for user segmentation that Odin can adapt using real transaction histories from manual inputs. The moderate Silhouette Score (0.33) also justifies considering alternative clustering algorithms (e.g., DBSCAN) for better separation.

**Directly justifies:**

- "K-means clustering on transaction amount, hour of day, day of week, and transaction type produces three distinct user segments with different spending behaviors."
- "A Silhouette Score of 0.33 indicates moderate cluster separation, suggesting density-based methods like DBSCAN may improve segmentation quality."
- "Transaction amount, time of day, and day of week are effective features for profiling financial users without requiring labeled training data."
- "Purchase-focused clusters (Clusters 0 and 2) differ by day of week (Monday vs. Friday), revealing weekly spending cycles."

**Limits of relevance:**

- Dataset is simulated, not real user transactions — real-world noise and irregularity may affect cluster quality.
- Single month of data — cannot capture seasonal spending patterns or behavioral drift over time.
- Geography not specified — findings may not generalize to Filipino young professionals' spending habits.
- Silhouette Score of 0.33 is moderate — clusters overlap, limiting practical deployment without refinement.
- No evaluation of how clusters evolve when new transaction data arrives (cold-start or concept drift).

### Limitations

- Dataset limited to one month of simulated transactions — cannot capture seasonal or long-term behavioral patterns.
- Silhouette Score of 0.33 indicates only moderate cluster separation — overlapping clusters may cause misclassification. [unacknowledged]
- No validation with domain experts to confirm whether identified clusters are financially meaningful or actionable.
- K-means assumes spherical clusters of equal size — may not fit real transaction distributions with outliers.
- Dataset size and composition not fully disclosed (only transaction counts shown in figures), limiting reproducibility.

---

## Source: `5.A/AI--Pretnar_et-al_2025_summarized.md`

**Title:** Mental Accounting Through Two-stage Budgeting Under Bounded Rationality

### TL;DR

A structural model of two-stage budgeting with cognitive constraints reveals that low-income consumers update only half their budgets weekly, and relaxing these constraints can cause some to overspend into bankruptcy.

### Findings

1. Best‑fitting model uses a **$1 numeracy threshold**; consumers update on average **2.11 out of 4 budgets per week** (baseline: 2.48 updates).
2. **78%** of consumers are ex‑ante “budget prioritizers” (reduce budget after over‑spending), but only **11%** show the same pattern in realized spending.
3. Most common type (**37‑38%**): ex‑ante budget prioritizer but ex‑post spendthrift (increase spending regardless of prior over/under‑spending).
4. Relaxing cognitive constraints (forcing full weekly updates) makes **68%** of consumers worse off; **3.3%** go bankrupt under the $1‑threshold model.
5. Bankrupt consumers had significantly fewer budget updates before relaxation (**1.25 vs 2.11 per week**), indicating sticky budgets served as a self‑discipline mechanism.

### Relevance to Odin

**Topics:**

5.A — Financial Behavioral Profiles in Personal Finance

5.C — Financial Behavioral Profile Classification Algorithm

7.A — Budgeting Strategies as Domain Knowledge

7.B — Budget Recommendation in Personal Finance Systems

8.A — Anomaly Detection in Personal Finance Systems

**Contribution to Odin:**

This paper provides a rigorous, data‑driven typology of how consumers use budgets (budget prioritizers, spending followers, spendthrifts, frugal savers), which directly informs the design of Odin’s behavioral profiling module. The finding that sticky budgets act as a self‑discipline mechanism for a subset of users justifies Odin’s default design: not forcing frequent budget re‑evaluations and allowing users to set their own update frequency. The counterfactual result that relaxing attention constraints can lead to bankruptcy warns against overly aggressive nudging (e.g., push notifications that demand weekly budget reviews), supporting Odin’s principle of value‑driven retention rather than gamified or high‑frequency interventions.

**Directly justifies:**

- “Low‑income consumers update only 2.11 of 4 budgets per week on average, providing evidence that narrow choice bracketing is the norm, not the exception.”
- “Ex‑ante budget prioritizers (78% of consumers) reduce budgets after over‑spending, but 37‑38% become ex‑post spendthrifts — a ‘planning fallacy’ pattern where intentions fail to control actual spending.”
- “Relaxing cognitive constraints makes 68% of consumers worse off, and 3.3% go bankrupt, proving that sticky budgets can be a beneficial self‑control device for financially vulnerable users.”
- “Bankrupt consumers had significantly fewer budget updates (1.25 per week) before the constraint was relaxed, showing that low attention is not a flaw but a protective discipline for some.”
- “A $1 absolute numeracy threshold fits the data better than percentage thresholds, suggesting consumers think in dollar‑unit changes rather than relative percentages.”

**Limits of relevance:**

- Study population is low‑income North American prepaid card users; Filipino young professionals may have different income volatility and cultural spending obligations.
- The model assumes manual budget setting by consumers; Odin uses algorithm‑recommended budgets, which may alter adherence dynamics.
- Data lacks explicit budget observations (only expenditure); inferences are model‑dependent and require validation on budgeting‑aware datasets.

### Limitations

- No independent budget observations exist to validate latent inferences; results are model‑dependent.
- The sample consists entirely of underbanked prepaid card users; findings may not generalize to banked or credit‑using populations. [unacknowledged]
- The model assumes strong separability and Stone‑Geary utility, which restricts substitution patterns.
- The counterfactual experiment forces all consumers to update all budgets every week; real‑world interventions (e.g., app notifications) are less extreme.
- Filipino cultural practices (family obligations, informal finance, seasonal spending) are not represented in the data or model.

---

## Source: `5.A/AI--Rabinovich_et-al_2025_summarized.md`

**Title:** Mapping Financial Mindsets: A Two-Stage Unsupervised Framework for Behavioral Profiling Using High-Dimensional Psychometric Data

### TL;DR

Two-stage unsupervised learning (UMAP + spectral clustering) identifies psychologically interpretable financial behavior profiles from psychometric data, validated across proprietary (N=337) and nationally representative U.S. (N=5,897) datasets.

### Findings

1. Silhouette scores: **0.569** (proprietary) and 0.500 (CFPB) — clear cluster separation in embedded space.
2. Cluster stability: mean ARI = 0.916 (proprietary) and 0.814 (CFPB) across random seeds; subsample ARI = 0.970–0.994.
3. Demographics explain little cluster variance: McFadden pseudo-R² = 0.091 (proprietary) and 0.061 (CFPB).

- Cluster membership explains 44% (CFPB) and 61% (proprietary) of variance in perceived financial health — far exceeding demographics (R²=0.25 and 0.16).
- Supervised ensemble classifier assigns new individuals to existing clusters with **79.2% accuracy** (5-fold CV), enabling cold-start profiling.
- Seven interpretable clusters emerged per dataset, ordered along a global functioning gradient with distinct psychological configurations.

### Relevance to Odin

**Topics:**

5.A — Financial Behavioral Profiles in Personal Finance

5.B — Profile Dynamics and the Cold-Start Problem

5.C — Financial Behavioral Profile Classification Algorithm

**Contribution to Odin:**

This paper directly informs Odin's financial behavioral profiling module by providing a validated unsupervised framework (UMAP + spectral clustering) that identifies psychologically meaningful profiles from psychometric survey data — exactly the type of input Odin will collect from users (e.g., attitudes, motivations, self-reported behaviors). The two-stage design, which separates within-domain scoring from cross-domain clustering, is directly applicable to Odin's need to combine multiple behavioral indicators (financial literacy, spending attitudes, self-regulation) into a coherent user profile without manual category definitions. Most critically, the paper demonstrates that a supervised classifier can assign new users to existing clusters with 79% accuracy — a solution to Odin's cold-start profiling problem, where new users have no transaction history and must be classified using an initial questionnaire.

**Directly justifies:**

- "Two-stage unsupervised learning (UMAP + spectral clustering) identifies psychologically coherent financial behavior profiles with silhouette scores of 0.50–0.57, demonstrating internal validity without ground-truth labels."
- "A supervised ensemble classifier achieves 79.2% accuracy assigning new individuals to existing clusters, enabling cold-start behavioral profiling for users with no transaction history."
- "Demographic variables (age, education, income) explain only 6–9% of variance in cluster membership, confirming that psychometric profiles capture behavioral variation not reducible to socioeconomic status."
- "Cluster membership accounts for 44% of variance in perceived financial health in a nationally representative sample, exceeding the 25% explained by demographics alone."

**Limits of relevance:**

- All data are from U.S. populations; Filipino financial behaviors, cultural obligations (e.g., family remittances, utang na loob), and psychometric scale validity may differ substantially.
- Cross-sectional design; no evidence on whether profiles change over time or respond to interventions — Odin's profiling dynamics (topic 5.B) will require longitudinal adaptation.
- Proprietary sample is modest (N=337) and skewed younger; cluster stability in smaller or more homogeneous populations (e.g., Metro Manila young professionals) is untested.
- Framework requires a sufficiently rich psychometric instrument (≥5 domains, ≥5 items per domain) — may need adaptation for shorter onboarding surveys.

### Limitations

- Cross-sectional data cannot assess how profiles evolve with life events or financial habits — a key unknown for Odin's dynamic profiling. [unacknowledged]
- Self-report measures may introduce social desirability and recall bias, affecting the geometry of learned representations.
- Proprietary dataset is modest (N=337) and drawn from a convenience sample (advisors, students, voluntary users) — not representative of any population.
- Hyperparameter sensitivity (UMAP n_neighbors, spectral clustering gamma) requires manual tuning; no fully automated selection procedure provided.
- No validation on non-U.S. or non-English populations; applicability to Filipino cultural and economic context is untested.

---

## Source: `5.A/AI--Yachamaneni_et-al_2025_summarized.md`

**Title:** Credit Card Customer Profiling Using Self-Supervised Representation Learning on Multi-Source Financial Data

### TL;DR

Self-supervised learning on multi-source financial data produces richer customer profiles than K-Means or XGBoost, improving credit risk AUC to 0.91 and churn F1 to 0.81.

### Findings

1. SSL achieved Silhouette score 0.56 vs K-Means 0.35 and XGBoost 0.41.
2. SSL reached credit risk AUC **0.91** vs XGBoost 0.84 and K-Means 0.71.
3. SSL churn prediction F1-score 0.81 vs XGBoost 0.69 and K-Means 0.58.

- Ablation: Removing temporal encoding dropped AUC by 4.2%; removing web activity dropped 3.8%; removing pretext tasks dropped 2.7%.

### Relevance to Odin

**Topics:**

5.A — Financial Behavioral Profiles in Personal Finance

5.C — Financial Behavioral Profile Classification Algorithm

**Contribution to Odin:**

This paper demonstrates that self-supervised learning on multi-source financial data (transactions, demographics, credit, web activity) produces superior customer profiles compared to traditional clustering or supervised methods. For Odin's financial behavioral profiling module, SSL offers a label-efficient way to learn user representations from transaction history alone (since Odin has no web activity or credit data, but the principle of using sequential transaction data with temporal encoding applies). The finding that temporal encoding provides the largest performance gain (4.2% AUC drop when removed) directly justifies Odin's use of sequential modeling for spending forecasting and profile classification.

**Directly justifies:**

- "Self-supervised learning on unlabeled transaction sequences improves clustering coherence by 60% over K-Means (Silhouette 0.56 vs 0.35) without requiring labeled data."
- "Temporal encoding of transaction timestamps yields the single largest contribution to predictive accuracy, with removal causing a 4.2% drop in credit risk AUC."
- "Contrastive learning and masked attribute prediction enable robust customer representations that generalize to downstream tasks such as risk assessment and churn prediction."
- "Multi-modal integration (transaction, demographic, credit, web) outperforms any single modality, but transaction and temporal signals dominate."

**Limits of relevance:**

- Study uses credit card data from a private bank, not personal budgeting data; spending patterns differ (credit vs debit/cash).
- No Filipino demographic data; cultural and income patterns may not generalize.
- Web activity and credit bureau reports are unavailable in Odin's manual-input, no-banking-integration scope.
- Odin does not perform churn prediction or credit risk assessment, but the representation learning method transfers to spending forecasting and profile classification.

### Limitations

- Dataset not publicly available; reproducibility unknown. [unacknowledged]
- No evaluation of cold-start performance — model assumes sufficient historical data per customer. [unacknowledged]
- SSL pretext tasks require careful design; effectiveness may vary with data volume (Odin's per-user data is sparse early on).
- Paper does not address model interpretability, which is critical for financial user trust.

---

## Source: `5.B/AI--Liao_2026_summarized.md`

**Title:** A Dynamic Intrusion Detection System Integrating Concept Drift Detection and Incremental Learning

### TL;DR

Concept drift detection and incremental learning must be tightly integrated to maintain intrusion detection performance when network traffic distributions change over time.

### Findings

- Concept drift detection must distinguish adversarial drift (attacker evasion) from benign drift (legitimate environment evolution) to select appropriate update strategies.
- Micro-level monitoring (per-cluster drift detection) overcomes class imbalance by turning a global imbalanced problem into locally balanced subproblems.
- The stability-plasticity dilemma is the core theoretical challenge: too much stability causes rigidity; too much plasticity induces catastrophic forgetting.
- A closed-loop perception-decision-execution-evaluation cycle enables autonomous model adaptation without full retraining.
- **Explainability and resource awareness are necessary for practical deployment** — the coordinator must output rationales and respect computational constraints.

### Relevance to Odin

**Topics:**

5.B — Profile Dynamics and the Cold-Start Problem

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

**Contribution to Odin:**

This paper's framework for integrating concept drift detection with incremental learning directly supports Odin's need to adapt to changing user financial behavior over time — such as income shifts, new spending patterns, or evolving financial obligations. The stability-plasticity dilemma formalizes the design trade-off Odin faces between retaining learned user profiles and updating them as behavior drifts. Although the paper addresses network intrusion detection, its theoretical model of drift detection (identifying when a user's financial behavior changes) and adaptive incremental learning (updating the profile classifier or anomaly detector without full retraining) is transferable to Odin's behavioral profiling and anomaly detection modules.

**Directly justifies:**

- "Concept drift detection identifies when a user's spending behavior shifts significantly, enabling model updates without waiting for scheduled retraining."
- "Micro-level drift monitoring — tracking changes within behavioral clusters rather than global statistics — detects subtle shifts in minority patterns (e.g., anomalous spending) that global metrics would miss."
- "The stability-plasticity dilemma forces a design choice: Odin's profile classifier must balance retaining long-term user traits (stability) with adapting to new patterns (plasticity)."
- "A closed-loop perception-decision-execution-evaluation cycle allows Odin to autonomously trigger model updates when drift is detected, then verify improvement."
- "Resource-aware adaptation (Pareto trade-offs between detection performance, response speed, and computational cost) is essential for Odin's mobile-first, offline-capable deployment."

**Limits of relevance:**

- Paper is theoretical — no empirical validation or quantitative performance metrics are provided.
- Domain is network security, not personal finance; the specific types of concept drift (e.g., adversarial evasion) may not map directly to benign financial behavior drift.
- No discussion of cold-start conditions (new users with no transaction history) — a core Odin problem.
- Assumes continuous data streaming; Odin's manual input produces sparse, irregular transaction data.

### Limitations

- Entirely theoretical; lacks any experimental validation or real-world dataset evaluation. [unacknowledged]
- No quantitative comparison of drift detection methods (e.g., control charts vs. hypothesis testing) in the proposed framework.
- Assumes sufficient data volume for micro-level clustering; may fail in sparse transaction environments like Odin's manual input.
- Does not address how drift detection thresholds should be set or tuned for different domains. [unacknowledged]
- Discussion of incremental learning assumes labeled data for updates; Odin's anomaly detection is largely unsupervised.

---

## Source: `5.C/AI--Gouni_2025_summarized.md`

**Title:** Evolution of Machine Learning: A Foundation for Intelligent Systems

### TL;DR

Machine learning evolved from supervised classifiers to deep learning and unsupervised anomaly detection, enabling real-time fraud detection with lower false positives.

### Findings

- Supervised ensemble methods (random forests, gradient boosting) outperform single classifiers, especially on imbalanced fraud data.
- Autoencoders detect anomalies via reconstruction error without labeled data, capturing non-linear relationships linear methods miss.
- LSTMs address the vanishing gradient problem, maintaining contextual awareness across long transaction histories for card-not-present fraud.
- CNNs automatically extract hierarchical features from raw transaction data, reducing manual feature engineering.
- Hybrid multi-tier detection pipelines (high-sensitivity flagging + high-specificity intervention) balance accuracy and operational efficiency.
- Concept drift in transaction patterns requires adaptive models; static unsupervised methods increase false positives over time.
- Real-time deep learning deployment requires GPUs/TPUs, distributed computing, and online learning mechanisms.

### Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

**Contribution to Odin:**

This survey directly informs Odin’s algorithm selection across three modules. For anomaly detection, the paper establishes autoencoders and clustering as viable unsupervised methods that do not require labeled fraud data — a critical property for Odin’s cold-start spending anomaly detection. For spending forecasting, the discussion of LSTMs and GRUs for sequential transaction data justifies their consideration as candidates for predicting per-category spending over time. For behavioral profile classification, the comparison of ensemble methods (random forests, gradient boosting) against single classifiers provides a basis for selecting a robust classifier given Odin’s imbalanced user activity data. Although the domain is credit card fraud, the methodological foundations transfer directly to personal finance anomaly detection and sequential prediction.

**Directly justifies:**

- “Autoencoders detect anomalies via reconstruction error without labeled data, making them applicable to cold-start user profiles where fraudulent (anomalous) spending has no prior examples.”
- “LSTM networks capture long-term dependencies in transaction sequences, outperforming standard RNNs by addressing the vanishing gradient problem — relevant to spending forecasting over months of user history.”
- “Random forests aggregate predictions across multiple decision trees, improving robustness against novel patterns compared to single decision trees, with reasonable real-time computational requirements.”
- “Concept drift in transaction patterns necessitates adaptive models; static anomaly detectors increase false positives over time as legitimate user behavior evolves.”
- “Hybrid detection pipelines with multiple sensitivity layers (high-sensitivity flagging + high-specificity intervention) balance detection accuracy and operational efficiency.”

**Limits of relevance:**

- Domain is credit card fraud, not personal budget anomaly detection; spending anomalies (overspending) differ from fraud (unauthorized use).
- No empirical benchmarks on personal finance datasets; all reported performance comparisons are from fraud detection literature.
- Filipino young professional spending patterns and cultural obligations are not addressed.
- Real-time processing assumptions (GPUs/TPUs, sub-millisecond latency) may exceed Odin’s mobile-first deployment constraints.
- Paper does not evaluate algorithm performance under manual transaction entry (vs. automated bank feeds).

### Limitations

- The paper is a survey, not an original empirical study; no new experiments or quantitative results are presented.
- Performance claims (e.g., “ensemble methods outperform single classifiers”) are cited from other works without meta-analysis or replication. [unacknowledged]
- Geographic and demographic context is absent; findings assume Western financial infrastructure and consumer behavior.
- No discussion of mobile-specific constraints (battery, compute, offline operation) for deploying deep learning models. [unacknowledged]
- The survey focuses on fraud detection, so applicability to personal finance budget recommendation and forecasting is inferred, not tested.

---

## Source: `6.A/AI--Sonkavde_et-al_2023_summarized.md`

**Title:** Forecasting Stock Market Prices Using Machine Learning and Deep Learning Models: A Systematic Review, Performance Analysis and Discussion of Implications

### TL;DR

Ensemble of Random Forest, XGBoost, and LSTM achieved the lowest RMSE (2.0247) and highest R² (0.9921) for stock price forecasting, outperforming all individual models.

### Findings

1. **Ensemble (RF+XGBoost+LSTM) achieved the best performance**: RMSE 2.0247 (TAINIWALCHM) and 1.2658 (AGROPHOS); R² 0.9921 and 0.9897, respectively.
2. XGBoost alone performed strongly: RMSE 2.0686 (TAINIWALCHM) and 1.7618 (AGROPHOS); R² 0.9842 and 0.9379.
3. LSTM (RMSE 5.6241, R² 0.8867) and GRU (MAE 42.8 without sentiment) work well but are outperformed by ensembles.

- Random forest had very high RMSE (87.88) on TAINIWALCHM, showing poor suitability for this stock’s pattern without tuning.
- Hyperparameter tuning is crucial; a lower learning rate may improve generalization at cost of slower convergence.

### Relevance to Odin

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

### Limitations

- No universal solution exists; even AI models fail if not retrained with fresh data (paper acknowledges).
- Ensemble model’s computational cost and inference latency are not analyzed – may be unsuitable for real-time mobile use. [unacknowledged]
- Hyperparameter grid search results are not fully reported for each algorithm, reducing reproducibility.
- The systematic review does not include a PRISMA-style flow or quality assessment of cited papers. [unacknowledged]
- No evaluation on spending or budget adherence data – all experiments are on stock prices only.

---

## Source: `6.A/AI--Ullah_et-al_2024_summarized.md`

**Title:** Short-Term Load Forecasting: A Comprehensive Review and Simulation Study With CNN-LSTM Hybrids Approach

### TL;DR

Hybrid CNN-LSTM model achieves superior short-term load forecasting accuracy (RMSE 538.71, MAPE 2.72% single-step) by combining CNN feature extraction with LSTM temporal sequencing.

### Findings

1. Single-step forecast on NTDC: **RMSE 538.71, MAE 371.97, MAPE 2.72** — substantially better than reference [79] (RMSE 1038.04, MAPE 5.35).
2. 24-hour forecast on NTDC: RMSE 951.94, MAE 656.35, MAPE 4.72 — outperforming both [79] and [55].
3. On AEP dataset: single-step RMSE 126.35, MAE 94.27, MAPE 0.64; 24-hour RMSE 702.97, MAPE 3.39.

- LSTM layers capture long-term temporal dependencies that statistical models (ARIMA, SARIMA) miss due to stationarity assumptions.
- CNNs effectively extract local patterns (trends, periodicities) from high-dimensional time series inputs.

### Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

**Contribution to Odin:**

This paper directly informs Odin’s spending forecasting module by providing a rigorous, comparative evaluation of time series forecasting methods — from statistical (ARIMA, SARIMA) to intelligent (SVM, RF, MLP) to hybrid (CNN-LSTM). Although the domain is electrical load, the methodological findings transfer directly to predicting sequential spending data: CNN layers extract local spending patterns (e.g., weekly cycles), and LSTM layers capture long-term behavioral drift. The demonstrated superiority of CNN-LSTM over pure LSTM or statistical models on irregular, high-dimensional sequential data justifies Odin’s selection of a hybrid architecture for per-category spending prediction. The paper’s evaluation metrics (RMSE, MAE, MAPE) and preprocessing techniques (outlier detection via IQR, cyclical feature encoding) are directly adoptable for Odin’s algorithm performance measurement and data pipeline.

**Directly justifies:**

- "Hybrid CNN-LSTM reduces single-step forecasting MAPE to 2.72% compared to 5.35% for LSTM-only models — sequential feature extraction combined with temporal memory outperforms either alone."
- "ARIMA and SARIMA models assume stationarity and linearity, making them unsuitable for spending data with non-stationary behavioral shifts and nonlinear category interactions."
- "Outlier detection using IQR (Q1-1.5×IQR, Q3+1.5×IQR) effectively identifies anomalous load values; same method applies to spending anomaly detection in cold-start profiles."
- "Hour, day-of-week, and holiday encodings as categorical features significantly improve forecast accuracy — analogous temporal features (payday cycles, weekend spending) are essential for Odin’s forecasting inputs."

**Limits of relevance:**

- Domain mismatch: electrical load forecasting vs. personal spending forecasting — spending patterns have different volatility drivers (income, obligations, discretionary choice).
- Data scale and frequency: NTDC hourly grid data is high-frequency and macro-level; Odin uses sparse, user-entered transaction data (often daily or weekly).
- No evaluation on cold-start profiles or sparse user activity — the model assumes dense historical sequences.
- Filipino cultural spending patterns (family obligations, 13th month, etc.) are not considered; the algorithm’s feature set would need adaptation.
- Paper assumes no missing data (after outlier replacement); Odin’s manual entry inherently creates irregular gaps.

### Limitations

- Study exclusively uses power grid data; no validation on financial transaction sequences. [unacknowledged]
- Outlier handling replaces anomalies with mean values — this would mask genuine anomalous spending that Odin must detect. [unacknowledged]
- Model complexity (three CNN blocks, three LSTM layers) may be overkill for mobile deployment with limited compute and battery.
- No probabilistic forecasting (quantiles, confidence intervals) — Odin may need uncertainty estimates for budget alerts. (Acknowledged as future work in conclusion.)
- Authors treat all national holidays uniformly — personal finance calendars are more nuanced (e.g., holiday spending spikes vs. utility load dips).

---

## Source: `9.A/AI--Qu_et-al_2024_summarized.md`

**Title:** Budgeted Embedding Table For Recommender Systems

### TL;DR

BET guarantees strict memory budget compliance while improving recommendation accuracy by adaptively sizing each user and item embedding via set-based fitness prediction.

### Findings

1. On Gowalla with LightGCN at 90% sparsity, BET achieves **0.1620 Recall@20 and 0.1376 NDCG@20**, outperforming CIESS (0.1589/0.1353) and all other baselines.
2. BET strictly meets target sparsity (80%, 90%, 95%) whereas ESAPN and OptEmbed deviate (67–83%).
3. Paired t-tests show BET significantly beats best baseline in most settings (p < 0.05).

- DeepSets-based fitness predictor improves performance over a simple predictor and over random selection alone (Table 2).
- Increasing candidate actions m to 100 yields best results; performance stabilizes after 40 iterations.

### Relevance to Odin

**Topics:**

9.A — Mobile-First Design Principles and Rationale

**Contribution to Odin:**

This paper provides a method to compress embedding tables under strict memory budgets while preserving model accuracy, directly supporting Odin’s mobile-first design where on-device storage and compute are constrained. Although BET targets recommender systems, its budget-aware action sampling and set-based fitness prediction are general techniques applicable to any embedding-based ML module Odin might employ (e.g., user behavioral profiling or category embedding). The paper demonstrates that hard memory caps can be enforced without manual coefficient tuning, which is critical for deploying Odin on diverse mobile hardware in Metro Manila.

**Directly justifies:**

- "BET achieves strict memory budget compliance without manually tuned trade-off coefficients, overcoming a key limitation of sparsification and RL-based embedding compression methods."
- "The set-based fitness predictor reduces evaluation cost from O(mT) to O(T), enabling efficient architecture search under mobile constraints."
- "On Yelp2018 with LightGCN at 90% sparsity, BET achieves 0.0816 NDCG@20 versus 0.0762 for the best baseline CIESS, demonstrating that adaptive per-entity embedding sizes improve accuracy under identical memory budgets."
- "BET guarantees that total embedding parameters never exceed a pre-specified cap by using a bounded sampler that directly allocates parameters from probabilistic distributions."

**Limits of relevance:**

- Paper focuses on recommender systems (user–item interaction prediction), not personal finance management or budgeting.
- Datasets are user–item click/interaction logs, not financial transaction records with seasonal or cultural patterns.
- No evaluation on cold-start scenarios or very sparse user histories, which are common in new PFMS users.
- Mobile constraints are assumed but not tested on actual mobile hardware or battery-limited environments.

### Limitations

- Hyperparameter sensitivity: number of sampled actions m and iterations T require tuning (optimal m=100, T=50).
- Fitness predictor may overfit if action diversity is low; the random selection strategy mitigates this but adds variance.
- Evaluation only on two datasets (Gowalla, Yelp2018); generalizability to other domains (e.g., finance) not tested. [unacknowledged]
- Does not address streaming or continually evolving user/item sets; future work noted but not implemented.
- Selective retraining still requires training top 5 actions from scratch, which adds final computational cost.
