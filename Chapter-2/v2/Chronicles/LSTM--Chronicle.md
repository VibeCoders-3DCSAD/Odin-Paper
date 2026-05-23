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

## Source: `10.A/I--Nie_et-al_2024_summarized.md`

**Title:** A Survey of Large Language Models for Financial Applications: Progress, Prospects and Challenges

### TL;DR

LLMs excel at financial sentiment analysis, time series forecasting, and reasoning, but face major challenges in data privacy, interpretability, and computational cost.

### Findings

1. **GPT-4 achieved near-perfect financial literacy test scores**, outperforming earlier models on complex reasoning tasks (Niszczota and Abbas, 2023).
2. LLM-based stock prediction strategies generated monthly three-factor **alpha up to 3%** using policy news analysis (Lu et al., 2023).
3. Fine-tuned LLMs for SQL query generation from financial questions reached **95% accuracy** in reconciliation tasks (Yadav et al., 2024).
4. GPT-4 significantly outperformed BERT and traditional methods in predicting stock returns from news headlines, with gains largest for smaller stocks (Lopez-Lira and Tang, 2023).

- LLMs enable zero-shot anomaly detection in financial markets using multi-agent frameworks, reducing manual intervention.
- Instruction-tuned models like FinGPT improve numerical sensitivity and contextual understanding in sentiment analysis.

### Relevance to Odin

**Topics:**

4.A — Landscape of Existing Personal Finance Systems

5.A — Financial Behavioral Profiles in Personal Finance

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

7.B — Budget Recommendation in Personal Finance Systems

7.C — Budget Recommendation Algorithm

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

9.A — Mobile-First Design Principles and Rationale

10.A — Data Privacy and Security in Personal Finance Systems

10.B — User Trust in Personal Finance Systems

12.A — Evaluation Frameworks for Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This survey directly informs Odin’s algorithm selection across multiple modules by systematically comparing LLM-based approaches for sentiment analysis, time series forecasting, anomaly detection, and reasoning. The documented success of instruction-tuned models like FinGPT in numerical sensitivity and contextual understanding justifies exploring similar fine-tuning for Odin’s transaction categorization and budget recommendation modules. The survey’s detailed discussion of zero-shot vs. fine-tuning tradeoffs, along with inference cost and privacy constraints, provides essential design guidance for Odin’s mobile-first, manual-input architecture where on-device efficiency and data locality are critical.

**Directly justifies:**

- “Instruction-tuned LLMs (e.g., FinGPT) improve numerical sensitivity and contextual understanding in financial sentiment analysis, directly applicable to Odin’s expense categorization from user-entered transaction descriptions.”
- “LLM-based forecasting models using chain-of-thought reasoning achieve explainable stock predictions, supporting Odin’s requirement for transparent spending forecasts.”
- “Zero-shot anomaly detection with LLM-based multi-agent frameworks reduces manual intervention in identifying irregular spending patterns, applicable to Odin’s cold-start user profiles.”
- “Hybrid inference routing (small model for simple queries, large model for complex ones) reduces LLM inference cost by up to 40%, critical for Odin’s mobile deployment without API reliance.”
- “Lookahead bias in financial backtesting can be mitigated using point-in-time training datasets (TimeMachineGPT), a method Odin can adopt when evaluating forecasting module accuracy with historical user data.”

**Limits of relevance:**

- Survey focuses on institutional finance (trading, risk) more than personal budget management; direct transfer of results requires adaptation.
- Most cited studies use high-frequency or API-connected data; Odin’s manual, sparse transaction logs may reduce LLM effectiveness.
- Computational costs of LLMs remain high for pure mobile deployment; edge deployment or small-model distillation is assumed.
- No Philippine-specific financial behavior or cultural spending data is analyzed; applicability to Filipino young professionals requires validation.

### Limitations

- Survey is not systematic; paper selection and categorization may reflect author bias and omit emerging work. [unacknowledged]
- Rapid evolution of LLMs (e.g., Llama 3, GPT-4 Turbo) makes some comparisons outdated by publication time.
- No quantitative meta-analysis or performance ranking across tasks; claims are qualitative or drawn from disparate studies.
- Ignores low-resource language contexts (e.g., Tagalog, mixed English-Filipino code-switching) prevalent in Philippine mobile finance apps. [unacknowledged]
- Does not address manual transaction entry scenarios; all cited work assumes machine-readable or API-accessible data.

---

## Source: `10.A/I--Whitaker_2025_summarized.md`

**Title:** The Role of Big Data Analytics in Behavioral Finance: Understanding Dynamics of Consumer Spending and Saving

### TL;DR

Big data analytics integrates structured and unstructured financial data to uncover behavioral biases and psychological drivers of consumer spending and saving, enabling personalized financial strategies.

### Findings

- Consumer financial behavior is shaped by cognitive biases (overconfidence, loss aversion) and emotions (fear, greed), not just rational factors.
- Big data enables **real-time segmentation** of consumers into behavioral profiles based on spending habits, demographics, and life events.
- Predictive models using historical transaction data can forecast future spending patterns with higher accuracy than traditional methods.
- Social media sentiment analysis provides early indicators of spending shifts and economic confidence.
- Personalized financial products (automated savings, tailored alerts) improve saving rates and spending adherence.

### Relevance to Odin

**Topics:**

4.A — Landscape of Existing Personal Finance Systems

4.B — Limitations and Gaps in Existing Systems

3.A — Expense Categorization Frameworks

3.B — Expense Category Design Considerations

5.A — Financial Behavioral Profiles in Personal Finance

5.B — Profile Dynamics and the Cold-Start Problem

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

10.A — Data Privacy and Security in Personal Finance Systems

10.B — User Trust in Personal Finance Systems

**Contribution to Odin:**

This paper provides a broad methodological justification for integrating big data analytics into each of Odin's core modules — profiling, forecasting, anomaly detection, and categorization. It establishes that structured transaction data combined with behavioral insights (biases, life events) improves prediction accuracy over traditional models, directly supporting Odin's choice of ML-driven forecasting. The paper's extensive discussion of privacy-by-design principles (GDPR, transparency, informed consent) informs Odin's data handling under RA 10173. Although not Filipino-specific, its survey of analytical techniques (clustering for profiles, regression for spending) offers a validated reference for algorithm selection in Odin's design phase.

**Directly justifies:**

- "Clustering algorithms can segment consumers by spending habits, enabling targeted financial strategies — a core requirement for Odin's behavioral profiling module."
- "Predictive analytics using historical transaction data forecasts future per-category spending, directly applicable to Odin's spending forecasting module."
- "Anomaly detection based on transaction patterns identifies unusual spending that deviates from established behavior, supporting Odin's overage alert system."
- "Data privacy regulations (GDPR) mandate informed consent and transparency, which are binding precedents for Odin's compliance with Philippine RA 10173."
- "Algorithmic bias in ML models can perpetuate inequalities, requiring regular audits — a risk Odin must address in its classifier design."

**Limits of relevance:**

- Study is a conceptual review, not an empirical evaluation — no comparative performance metrics for specific algorithms.
- Geography is not Philippine-specific; cultural spending patterns (e.g., family obligations, 13th month pay) are not addressed.
- Assumes availability of large-scale transaction data; Odin relies on manual input, which may limit data volume and velocity.
- Does not address cold-start profiling for new users with no transaction history — a core Odin challenge.

### Limitations

- No original empirical data or comparative algorithm benchmarks — the paper is a literature review, not a primary study. [unacknowledged]
- Focuses on high-volume transaction environments (banking APIs), not manual-entry mobile apps like Odin. [unacknowledged]
- Does not address computational constraints of on-device or mobile-first ML models.
- Lacks discussion of Filipino-specific financial behaviors (e.g., informal credit, remittances).
- Ethical analysis is high-level; no practical framework for implementing privacy-by-design in a mobile PFMS.

---

## Source: `10.A/I--Ying_&_Blaise_2025_summarized.md`

**Title:** Leveraging Big Data Analytics in Behavioral Finance: Insights into Consumer Spending and Saving Dynamics

### TL;DR

Big data analytics enables financial institutions to uncover hidden behavioral patterns in consumer spending and saving that traditional models miss, using machine learning and predictive analytics on transaction histories and digital footprints.

### Findings

- **Big data analytics enables accurate customer segmentation** based on spending and saving patterns, allowing targeted marketing and personalized financial products.
- **Predictive models can forecast future spending behaviors** using historical transaction data and external factors like economic conditions or seasonal trends.
- **Sentiment analysis of social media data** reveals public economic sentiment that influences consumer spending (e.g., positive sentiment increases spending, negative sentiment reduces it).
- **Automated savings programs** that analyze spending habits and round up purchases significantly increase saving without user effort.
- **Behavioral nudges and gamification** informed by big data can improve saving rates and financial decision-making.

### Relevance to Odin

**Topics:**

5.A — Financial Behavioral Profiles in Personal Finance

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

7.B — Budget Recommendation in Personal Finance Systems

8.A — Anomaly Detection in Personal Finance Systems

10.A — Data Privacy and Security in Personal Finance Systems

**Contribution to Odin:**

This paper provides a comprehensive survey of big data analytics techniques applicable to Odin's core modules, justifying the use of clustering for behavioral profiling (Topic 5.C) and predictive models for spending forecasting (Topic 6.B). The discussion of automated savings programs and personalized financial advice directly supports Odin's budget recommendation module (Topic 7.B) by showing how spending pattern analysis can trigger saving actions. The paper also highlights anomaly detection as a key application, validating Odin's need to identify unusual spending deviations (Topic 8.A). Finally, the chapter on ethical considerations and data privacy (Topic 10.A) reinforces Odin's privacy-by-design approach and compliance with Philippine data protection law.

**Directly justifies:**

- "Clustering algorithms can segment consumers based on spending behaviors, enabling targeted marketing and personalized financial advice."
- "Predictive analytics using historical transaction data and machine learning models can forecast future spending patterns, accounting for seasonal changes and economic conditions."
- "Automated savings programs that analyze spending habits and round up purchases to transfer the difference to savings accounts increase saving without user effort."
- "Sentiment analysis of social media data can gauge public economic sentiment, which influences consumer spending behavior."
- "Machine learning algorithms used in big data analytics may inadvertently perpetuate algorithmic bias, requiring regular audits and diverse data sources to ensure fairness."

**Limits of relevance:**

- Paper is a conceptual review with no empirical validation of specific algorithms; citations should be for methodological justification, not performance benchmarks.
- Focus is on financial institutions (banks, retailers) rather than individual personal finance management systems — transferability requires adaptation.
- No evaluation of algorithm performance under cold-start conditions (new users with no history), which is critical for Odin.
- Geographically agnostic; findings are not specific to Filipino young professionals or Philippine financial context.

### Limitations

- No empirical data or quantitative results — the paper is a narrative review, limiting its use as evidence for specific algorithm performance.
- Does not address mobile-specific constraints (processing power, offline capability, manual input), which are central to Odin. [unacknowledged]
- Lacks discussion of cold-start problems for new users with no transaction history. [unacknowledged]
- Ethical considerations mentioned but no concrete solutions for algorithmic bias or privacy enforcement in practice.
- Relies on banking API integration for transaction data; Odin uses manual input only, which may affect data availability and model accuracy.

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

## Source: `12.A/I--Mienye_et-al_2026_summarized.md`

**Title:** Deep Learning for Credit Risk Prediction: A Survey of Methods, Applications, and Challenges

### TL;DR

Deep learning models (MLP, CNN, RNN, Transformer, GNN) beat traditional credit scoring on large behavioral datasets, but evaluation integrity, interpretability, and deployment governance remain unsolved.

### Findings

1. HDNN with L1–L2 regularization achieved **80.12% accuracy** for corporate credit, outperforming LR (AUC=0.717) and SVM (AUC=0.738).
2. LSTM for monthly default rate forecasting reduced **MAE from 0.095 to 0.072** and RMSE from 0.119 to 0.093 versus ARIMA, SVM, and ANN.
3. CNN–LSTM–attention model reached AUC=0.92 and F1=0.91 for enterprise credit, beating CNN-only and LSTM-only baselines.
4. RGAT on SME relational graphs achieved AUC=0.799 and KS=0.528; multi-head extension reached AUC=0.799, KS=0.528.
5. TabNet-stacking ensemble on Tianchi dataset (≈800k cases) achieved **AUC=0.941** and accuracy=0.979.

- Transformers (TabTransformer, FT-Transformer) match or exceed XGBoost/CatBoost on high-cardinality tabular data.
- Most studies use random k-fold cross-validation, causing temporal leakage; calibration (Brier, ECE) and cost-sensitive metrics are rarely reported.
- Interpretability (SHAP, attention) and fairness (equalized odds) are treated as post hoc add-ons, not training objectives.

### Relevance to Odin

**Topics:**

4.B — Limitations and Gaps in Existing Systems

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

8.B — Anomaly Detection Algorithm

12.A — Evaluation Frameworks for Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This survey directly informs Odin’s algorithm selection for spending forecasting (LSTM/GRU vs. CNN vs. transformer) and anomaly detection by benchmarking sequential deep learning architectures on financial time series. The paper’s critique of evaluation integrity—temporal leakage, calibration neglect, overreliance on AUC—provides a checklist for Odin’s module-level validation, especially given Odin’s manual transaction input and cold-start constraints. Its synthesis of interpretability (SHAP, attention) and fairness (equalized odds) offers practical guidance for Odin’s user trust and explainability requirements under Philippine data privacy law (RA 10173).

**Directly justifies:**

- "LSTM networks reduce MAE from 0.095 to 0.072 for monthly default forecasting, demonstrating that recurrent architectures capture behavioral drift better than static models."
- "Random k-fold cross-validation causes temporal leakage in credit risk studies; out-of-time splits and rolling-origin validation are required for realistic performance estimates."
- "Deep tabular models (MLP, TabNet) with attentive embeddings match gradient boosting on large datasets (≥300k records) with high-cardinality categorical features."
- "Most deep credit risk studies ignore probability calibration (Brier score, ECE), leading to miscalibrated PD estimates even when AUC improves."
- "GNNs (RGAT, GraphSAGE) capture relational risk propagation (co-applicant, director, supply-chain ties) that tabular models structurally cannot represent."

**Limits of relevance:**

- Survey focuses on credit default (borrower non-repayment), not personal spending budgeting; spending forecasting and anomaly detection in Odin share similar sequential modeling needs but different outcome definitions.
- All studies use banking/transaction data with rich historical sequences; Odin starts from manual input with sparse cold-start histories, limiting direct transfer of reported performance gains.
- No Filipino-specific demographic or income stability analysis; behavioral patterns of South African, US, and Chinese borrowers may not generalize.
- Many benchmark datasets (German Credit, Australian Credit) are small (≤1000 records) and static, unlike Odin’s per-user transaction stream.

### Limitations

- Only peer-reviewed English studies indexed in major databases; proprietary industry implementations and regulatory grey literature excluded.
- No formal risk-of-bias or meta-analysis; reported performance numbers are not standardized across datasets, horizons, or label definitions. [unacknowledged]
- Does not address cold-start profiling or spending forecasting for new users with no transaction history—central to Odin’s design problem.
- Survey’s evaluation recommendations (out-of-time splits, calibration metrics) are not applied to any original model, remaining prescriptive rather than demonstrative. [unacknowledged]
- Privacy-preserving methods (differential privacy, federated learning) are mentioned but not evaluated on credit tasks; practical utility–privacy trade-offs unknown.

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

## Source: `12.B/I--Ahmed_et-al_2023_summarized.md`

**Title:** Deep learning modelling techniques: current progress, applications, advantages, and challenges

### TL;DR

Deep learning models automatically learn hierarchical features from raw data, outperforming traditional ML on large datasets but requiring substantial computational resources and training samples.

### Findings

1. **CNN** achieves high image recognition accuracy but requires large labeled datasets and is susceptible to poor labeling.
2. **BiLSTM** outperforms standard LSTM by **37.78%** in time series forecasting accuracy (Siami-Namini et al., 2019).
3. **GenInSAR** (CNN-based) reduced total residue by **>16.5%** compared to alternative InSAR methods.
4. **RNN-LSTM** achieved lower RMSE (0.487) than traditional RNN (0.516) and naive models (0.793) for low-flow prediction.

- Hybrid conventional DL architectures (e.g., CNN-LSTM) are more robust than standalone models.
- Deep learning is susceptible to deception, misclassification, and local minima, limiting online-mode suitability.

### Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper provides a systematic survey of deep learning architectures, enabling Odin’s team to make informed algorithm selections for its forecasting, classification, and anomaly detection modules. The finding that RNN-based models (LSTM, GRU) excel at time series forecasting directly supports Odin’s spending forecasting module design, while the comparative complexity analysis (Table 4) guides mobile-first implementation trade-offs. Although domain-agnostic, the paper’s performance benchmarks and identified limitations (e.g., cold-start data requirements) inform RRL arguments for choosing lightweight, unsupervised, or hybrid models suited to Odin’s manual-input, low-user-history context.

**Directly justifies:**

- “LSTM and GRU outperform traditional RNNs on time series forecasting by mitigating vanishing gradients, with BiLSTM achieving up to 37.78% higher accuracy on sequential data.”
- “Deep learning models automatically generate features from raw data, reducing hand-tuning requirements for transaction categorization in personal finance systems.”
- “Training deep learning models requires large labeled datasets and high computational resources – a key limitation for cold-start user profiles in Odin, favoring unsupervised or lightweight approaches.”
- “Hybrid architectures (e.g., CNN-LSTM) are more robust than standalone models, suggesting Odin’s modules may benefit from combining feature extraction and sequential modeling.”
- “Generative models (GANs, autoencoders) can detect anomalies without labeled training data, applicable to Odin’s anomalous spending detection under sparse user history.”

**Limits of relevance:**

- The paper is a general survey of DL techniques; no experiments on personal finance or transaction data.
- Performance comparisons (e.g., accuracy percentages) come from non-financial domains (image, speech, medical), not directly transferable to spending forecasting.
- The review does not address algorithm performance on irregular, manual-transaction data typical of Odin (no API integration).
- No discussion of culturally specific financial patterns or Filipino demographic context.

### Limitations

- Survey methodology relies on existing literature; no original empirical validation of any DL model.
- Computational complexity analysis is qualitative (Low/Medium/High) without hardware-specific benchmarks. [unacknowledged]
- The paper does not address online learning or incremental model updates, which are relevant to dynamic user behavior in Odin. [unacknowledged]
- Many cited performance metrics are from studies with different evaluation protocols, limiting direct comparability.
- No discussion of privacy-preserving machine learning techniques, a concern for financial apps under RA 10173. [unacknowledged]

---

## Source: `12.B/I--Du_et-al_2025_summarized.md`

**Title:** Foundations and Innovations in Data Fusion and Ensemble Learning for Effective Consensus

### TL;DR

Ensemble learning reduces variance (bagging) or bias (boosting) to improve predictive performance; this survey reviews techniques, theoretical foundations, and trade-offs with deep learning.

### Findings

- Bagging reduces variance by averaging models on bootstrap samples; boosting reduces bias by sequentially focusing on misclassified examples.
- Random forests balance bias and variance by adding feature randomization, achieving robust performance with minimal overfitting.
- XGBoost and LightGBM dominate tabular data benchmarks, often outperforming deep neural networks.
- The C-bound provides a tighter risk estimate for weighted majority vote than Gibbs classifier bounds.
- Dempster–Shafer theory generalizes Bayesian probability but suffers from counterintuitive results under high conflict.
- Multiview learning (CCA, coregularization) improves classification by aligning complementary feature sets.

### Relevance to Odin

**Topics:**

4.A — Landscape of Existing Personal Finance Systems

4.B — Limitations and Gaps in Existing Systems

5.C — Financial Behavioral Profile Classification Algorithm

6.B — Spending Forecasting Algorithm

7.C — Budget Recommendation Algorithm

8.B — Anomaly Detection Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This survey provides a comprehensive methodological reference for Odin’s algorithm selection across multiple modules. It justifies using random forests or gradient boosting for behavioral profile classification (Section 8, 9) by establishing their bias–variance advantages and superior performance on tabular data. The computational trade-off analysis (Table 2) directly informs Odin’s mobile-first design by quantifying inference complexity (O(Bd) for bagging vs. O(Td) for boosting), helping decide between parallelizable ensembles (random forests) vs. sequential ones (XGBoost) under mobile constraints. The comparison between ensemble learning and deep learning (Table 3) supports Odin’s decision to prioritize tree-based ensembles over neural networks for structured transaction data.

**Directly justifies:**

- "Random forests consistently outperform most methods in predictive accuracy and exhibit strong resilience to outliers and noise (Breiman, 2001)."
- "Boosting with decision trees (XGBoost, LightGBM) often surpasses deep neural networks on tabular data, making it the preferred choice for structured financial records."
- "Bagging reduces variance at O(BTd log d) training cost with fully parallelizable base learners; boosting reduces bias sequentially at O(Td log d) but cannot parallelize (Table 2)."
- "Margin theory explains why AdaBoost continues to improve generalization even after training error reaches zero — relevant for iterative refinement of spending forecasts."
- "Dempster–Shafer evidence combination can fuse multiple classifier outputs without requiring prior probabilities, applicable to anomaly detection under uncertainty."

**Limits of relevance:**

- The survey is methodological, not domain-specific; no empirical results on personal finance data are presented.
- All cited performance claims come from general ML benchmarks, not from Philippine spending behavior.
- Computational complexity bounds assume standard hardware; mobile-device constraints (battery, memory) are not directly addressed.
- Deep ensemble techniques (e.g., snapshot ensembles) may exceed Odin’s resource budget.

### Limitations

- No original empirical validation; all comparisons rely on cited literature, which may not generalize to Odin’s user population.
- Theoretical bounds (PAC-Bayes, margin) assume i.i.d. data; financial transaction streams may violate independence. [unacknowledged]
- Survey does not address concept drift or online learning in detail, though Odin requires adaptive profiles.
- Dempster–Shafer combination rule is NP-complete, limiting practicality for real-time mobile inference. [unacknowledged]
- Multiclass ECOC requires at least K times the number of tests, which may be inefficient for many budget categories.

---

## Source: `12.B/I--Hall_&_Rasheed_2025_summarized.md`

**Title:** A Survey of Machine Learning Methods for Time Series Prediction

### TL;DR

Tree-based models (LightGBM, XGBoost) match or beat deep learning (LSTM) for time series forecasting across most tasks, while training 100–1,000× faster.

### Findings

1. TBML models as a class achieved best performance in 54.55% of tasks vs. 52.70% for DL (FPA), with WRA scores 0.691 vs. 0.649 — a ~2.5% edge for TBML.
2. Among individual models, **LSTM had the strongest robust evidence: 58.97% FPA** (39 evaluations) and WRA 0.722.
3. LightGBM achieved 58.82% FPA (17 evaluations); CatBoost had 66.67% FPA but only 3 evaluations.

- TBML models train on average 126,935% faster than DL models (median 5,603% faster).
- In the largest dataset range (206k–11M samples), specialized TBML (SPTB) models outperformed RNNs by 16.67% FPA.
- Research focus bias: DL-focused papers show DL +33.8% FPA over TBML; TBML-focused show TBML +66.7% FPA over DL.
- Hybrid models generally outperform individuals, but standalone CatBoost beat a hybrid CNN-BiLSTM in one study (Saravanan et al., 2024).

### Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This survey directly informs Odin's spending forecasting module by providing empirical benchmarks for algorithm selection across dataset sizes and task types. The finding that LightGBM trains 5,600% faster than LSTM with comparable accuracy supports Odin's mobile-first constraint: efficient retraining on user devices without cloud dependencies. The identified research bias (up to 66.7% performance inflation when papers favor one model class) warns Odin's RRL to prioritize balanced studies when citing comparative claims. Additionally, the M5 competition result—an undergraduate won using LightGBM ensembles—demonstrates the model's accessibility for implementation without deep learning expertise.

**Directly justifies:**

- "LSTM achieved 58.97% first-place frequency across 39 time series forecasting comparisons, the strongest robust evidence among all individual models surveyed."
- "LightGBM trains a median 5,603% faster than deep learning models (up to 905,140% faster in one study) while achieving equivalent or better accuracy on tasks with large datasets."
- "On datasets larger than 200,000 samples, specialized tree-based models (XGBoost, LightGBM, CatBoost) outperform RNNs by 16.67% in first-place frequency."
- "Research focus biases reported model performance: DL-focused papers show DL outperforming TBML by 33.8% FPA, while TBML-focused papers show TBML outperforming DL by 66.7% FPA."
- "Tree-based models dominate energy, transportation, and anomaly detection tasks; RNNs dominate environmental, healthcare, and financial forecasting."

**Limits of relevance:**

- Survey includes no Philippine-specific financial data; domain patterns from retail, energy, or environmental forecasting may not map directly to personal spending behavior.
- Computational advantage measured on server-class hardware (GPUs/CPUs), not on mobile device constraints (battery, thermal throttling).
- M5 competition used retail sales (Walmart unit sales) with 42,840 time series; individual user spending has sparser, more irregular patterns.
- The survey excludes cold-start forecasting evaluation (no prior user data), a critical scenario for new Odin users.
- Attention-based models (Transformers) have only 5 papers in the survey; conclusions about their performance are not statistically robust.

### Limitations

- Attention-based architectures (Transformers) evaluated in only 5 papers; conclusions about their performance lack statistical robustness.
- Training time analysis drawn from only 10 studies; median advantage (5,603%) may not generalize across all hardware configurations. [unacknowledged]
- Survey excludes comparison of feature engineering effort required for TBML vs. DL; TBML often needs manual sequential feature construction. [unacknowledged]
- The weighted rank aggregation assumes linear interpolation between ranks, which may not reflect real performance gaps between models.
- M6 competition found zero correlation between forecasting accuracy and investment performance, but the survey does not explore why—this limits relevance for recommendation modules that combine forecasting with action.

---

## Source: `12.B/I--Kim_et-al_2025_summarized.md`

**Title:** A comprehensive survey of deep learning for time series forecasting: architectural diversity and open challenges

### TL;DR

Time series forecasting has entered a renaissance of architectural diversity, with simple linear models outperforming Transformers on long sequences while Mamba, diffusion, and foundation models rapidly emerge as competitive alternatives.

### Findings

1. LTSF-Linear (a simple MLP) **outperformed Transformer-based models** on long-term forecasting by preserving time-ordering information that attention mechanisms lose.
2. Patching (e.g., PatchTST) restored Transformer superiority over linear models by grouping time points into semantic patches, achieving better performance with longer look-back windows.
3. Channel-independent (CI) strategies often beat channel-dependent (CD) on benchmark datasets due to CI's robustness to distribution shifts, not inherent superiority.
4. Mamba-based models (e.g., S-Mamba, TimeMachine) achieve state-of-the-art results with linear time complexity, overcoming Transformer's quadratic scaling on long sequences.

- Diffusion models excel at probabilistic forecasting by modeling uncertainty through forward/backward noise processes, offering prediction intervals.
- SSMs (state space models) like S4 and Mamba provide efficient long-sequence modeling by compressing essential information into hidden states.

### Relevance to Odin

**Topics:**

4.A — Landscape of Existing Personal Finance Systems

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This survey directly informs Odin's forecasting module design by systematically comparing candidate architectures (LSTM, GRU, TCN, Transformer, Mamba, linear models) and their trade-offs (accuracy, complexity, data requirements). The finding that linear models can outperform Transformers on long sequences justifies evaluating lightweight MLP-based forecasting for Odin's mobile-first constraints. The detailed analysis of channel strategies (CI vs CD) and distribution shift alleviation methods (RevIN, Dish-TS) provides actionable guidance for Odin's cold-start profiling and anomaly detection under changing user behavior.

**Directly justifies:**

- "LTSF-Linear demonstrated that a single linear layer can outperform Transformer-based models on long-term forecasting by preserving time-ordering information, challenging the assumption that attention mechanisms are universally superior for time series."
- "Patching techniques (e.g., PatchTST) enable Transformers to capture locality and achieve state-of-the-art performance by grouping time points into semantic patches of 16–64 points."
- "Channel-independent (CI) strategies show greater robustness to distribution shifts than channel-dependent (CD) strategies, explaining why CI often beats CD on benchmark datasets despite CD's intuitive appeal."
- "RevIN (Reversible Instance Normalization) provides a model-agnostic normalization-denormalization framework that mitigates distribution shift in time series forecasting with minimal computational overhead."
- "Mamba achieves linear time and memory complexity while matching or exceeding Transformer performance on long sequences, making it suitable for resource-constrained mobile deployment."

**Limits of relevance:**

- Survey focuses on general TSF, not personal finance specifically; applicability to Odin's spending forecasting requires validation on financial transaction data.
- Most benchmark datasets (electricity, traffic, weather) differ from individual spending patterns in volatility and sparsity.
- Foundation models (Lag-Llama, TimesFM) require massive pre-training corpora unavailable for Philippine personal finance; zero-shot transfer may be unreliable.
- Mobile deployment constraints (battery, latency, offline operation) are mentioned but not empirically evaluated for any architecture.

### Limitations

- Survey excludes detailed theoretical derivations; researchers must consult original papers for mathematical rigor.
- Performance comparisons across architectures rely on reported benchmark results, which may vary with dataset characteristics and hyperparameter choices. [unacknowledged]
- No empirical validation of any architecture on financial transaction data; domain-specific performance is inferred.
- Mamba and diffusion models are very recent; long-term stability and generalization across diverse time series types are not yet established. [unacknowledged]
- Foundation models for time series are still nascent; current approaches (LLM reprogramming, pre-training) have not demonstrated reliable zero-shot forecasting on small or domain-specific datasets.

---

## Source: `12.B/I--Kolambe_&_Arora_2024_summarized.md`

**Title:** Forecasting the Future: A Comprehensive Review of Time Series Prediction Techniques

### TL;DR

Classical, machine learning, deep learning, and hybrid time series forecasting methods are categorized and compared, with a focus on challenges like non-stationarity and evaluation metrics (MAE, RMSE).

### Findings

- **Deep learning methods (LSTM, GRU) excel at capturing long-term dependencies but lack interpretability**, while classical methods (ARIMA, exponential smoothing) are simple and interpretable but struggle with non-linear patterns.
- Hybrid approaches that combine classical methods with machine learning or deep learning (e.g., ARIMA-NN, ensemble stacking) often outperform individual models by leveraging complementary strengths.
- Key forecasting challenges include non-stationarity (solved via differencing or decomposition), missing values (imputation), and seasonality (STL, SARIMA).
- Evaluation metrics: MAE measures average absolute error; RMSE penalizes larger errors more heavily; MAPE expresses error as percentage for scale-independent comparison.
- Future directions emphasize explainable AI to build trust, probabilistic forecasting to capture uncertainty, and scalable algorithms for big time series data.

### Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This review directly supports Odin's spending forecasting module by surveying candidate algorithms (LSTM, GRU, ARIMA, hybrid models) and their trade-offs in capturing temporal dependencies. The categorization of forecasting challenges — particularly non-stationarity, missing values, and seasonality — informs design decisions for handling Filipino young professionals' irregular income and spending patterns. The evaluation metrics section provides justification for using MAE or RMSE to measure forecasting accuracy in Odin's module-level testing, and the future directions on explainable AI align with Odin's need for user trust through transparency.

**Directly justifies:**

- "LSTM networks address the vanishing gradient problem and capture long-range temporal dependencies in sequential data, making them suitable for spending forecasting over multi-month horizons."
- "Hybrid methods that combine ARIMA with neural networks often outperform individual models by leveraging both linear and non-linear pattern extraction."
- "Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) are standard accuracy metrics for time series forecasting, with RMSE penalizing larger errors more heavily."
- "Non-stationarity in time series — where statistical properties change over time — can be addressed via differencing or decomposition into trend, seasonal, and residual components."
- "Probabilistic forecasting using Gaussian processes or Bayesian methods provides uncertainty estimates alongside point predictions, which is critical for user-facing budget alerts."

**Limits of relevance:**

- The review is domain-agnostic; no findings are specific to personal finance or Filipino spending behavior.
- No empirical comparisons or performance numbers are provided — only qualitative method characteristics.
- Cold-start forecasting (new users with no transaction history) is not discussed.
- The review assumes regularly sampled data; Odin's manual input may produce irregular intervals not fully addressed.

### Limitations

- No empirical evaluation or benchmark results — the review synthesizes existing literature without novel quantitative comparisons.
- Limited discussion of mobile-specific constraints (e.g., on-device computation, battery, storage) for deploying forecasting models. [unacknowledged]
- Ignores the cold-start problem common in personal finance apps where users have no historical data.
- Does not address domain adaptation or transfer learning across different user populations (e.g., Western vs. Filipino).
- Future directions mention explainable AI but do not provide concrete implementation guidance for time series.

---

## Source: `12.B/I--Kontopoulou_et-al_2023_summarized.md`

**Title:** A Review of ARIMA vs. Machine Learning Approaches for Time Series Forecasting in Data Driven Networks

### TL;DR

Machine learning models generally outperform ARIMA for time series forecasting, but ARIMA remains competitive on small, linear datasets; hybrid ARIMA-ML models consistently beat both.

### Findings

- **LSTM and GRU achieve RMSE values up to 40 times smaller than ARIMA for COVID‑19 case prediction in non‑linear data regimes** (ArunKumar et al., 2022).
- Hybrid ARIMA‑NARNN improved RMSE by 35.3% over ARIMA alone for COVID‑19 forecasting (Prajapati et al., 2021).
- ARIMA outperforms ML on small datasets (≤ few hundred points) and when the time series is approximately linear (e.g., linear load patterns, low‑volatility stock prices).
- Tree‑based models (XGBoost) require fewer data and features than deep learning for comparable accuracy, and dominated recent forecasting competitions (M4, M5).
- In 15+ comparison studies, ARIMA was superior only in specific conditions: strong seasonality (wind speed), very small value ranges, or when data granularity is coarse.

### Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

8.A — Anomaly Detection in Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This review directly informs Odin's spending forecasting module by providing a clear decision framework: LSTM and hybrid ARIMA-ML are best for non-linear, irregular spending patterns, while ARIMA alone suffices for cold-start users with very short history. The finding that tree‑based models (XGBoost) achieve competitive accuracy with fewer data and less feature engineering than deep learning justifies considering LightGBM or XGBoost as lighter alternatives for mobile deployment. The review also establishes standard evaluation metrics (RMSE, MAPE) and cautions that dataset size and linearity determine algorithm superiority—critical for Odin's early adoption phase.

**Directly justifies:**

- "LSTM and GRU achieve RMSE values up to 40 times lower than ARIMA for non‑linear time series, but ARIMA works better on small (≤500 points) or linear datasets."
- "Hybrid ARIMA-ML models consistently outperform individual models; ARIMA‑NARNN improved RMSE by 35.3% over ARIMA alone in COVID‑19 forecasting."
- "Tree‑based models like XGBoost require fewer training data and features than deep learning while delivering similar or better forecasting accuracy."
- "ARIMA fails on highly non‑linear or chaotic series (e.g., COVID‑19 deaths, Bitcoin volatility) but remains robust for short‑term, stable, or seasonal univariate series."

**Limits of relevance:**

- Review aggregates studies from finance, health, weather — personal spending data has different periodicity (daily/weekly) and lower volatility.
- Most benchmark datasets are large (years of hourly data); Odin's manual input yields sparse, short histories, favoring simpler models.
- Philippine cultural spending patterns (e.g., remittances, 13th month) not represented in any reviewed study.
- Deep learning models in review require non‑trivial compute; mobile deployment constraints not discussed.
- No direct comparison of cold‑start performance except inference that ARIMA handles small data better.

### Limitations

- The review itself does not perform original experiments; conclusions depend on quality and bias of included studies. [unacknowledged]
- Most compared studies optimize ARIMA manually but use default ML hyperparameters, potentially disadvantaging ARIMA.
- Publication bias likely: studies where ML fails may be underrepresented.
- No discussion of real‑time or streaming forecast updates, which matter for Odin's progressive reclassification.
- Computational cost and memory footprint of each model are not quantitatively compared — essential for mobile‑first design.

---

## Source: `12.B/I--Misiurek_et-al_2025_summarized.md`

**Title:** Review of Methods and Models for Forecasting Electricity Consumption

### TL;DR

No single method works for all electricity data; deep learning excels on volatile individual loads, ARIMA on stable aggregate series, and hybrid models offer the best balance.

### Findings

1. **LSTM networks achieved 10–15% RMSE improvement** over traditional ML models on high-volatility household load forecasting.
2. Hybrid CNN-LSTM reduced MSE to 0.3738 on residential data, outperforming standalone LSTM by capturing both spatial and temporal features.
3. Transformer-based models with sparse attention reached **up to 5× faster inference** than RNNs while maintaining comparable accuracy (RMSE ≈ 0.06 on AEP dataset).
4. ARIMA models achieved MAPE as low as 3.14% on stable aggregate consumption with clear seasonality, outperforming regression (8.1%) and ANN (5.6%) in that context.
5. Hybrid SARIMA-ANN models reduced RMSE from 0.0823 to 0.0792 compared to SARIMA alone, demonstrating benefit when linear and nonlinear structures are inseparable.

- No universal model exists; optimal choice depends on data volatility, seasonality, forecast horizon, and computational constraints.

### Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This review directly informs Odin's spending forecasting module by providing a structured, evidence-based comparison of candidate algorithms (LSTM, GRU, Transformer, ARIMA) across different data characteristics — volatility, seasonality, and sparsity. The finding that LSTM outperforms traditional models on high-volatility individual-level data (10–15% RMSE improvement) justifies selecting recurrent neural networks for forecasting per-category spending from user transaction histories, which are inherently irregular and volatile. The mapping of methods to data types (Table 5) offers a decision framework: if Odin users have stable, seasonal spending patterns, ARIMA may suffice; if patterns are erratic, deep learning is justified. Additionally, the review's coverage of evaluation metrics (MAPE, RMSE, MAE) and hybrid architectures supports Odin's algorithm evaluation and potential ensemble designs.

**Directly justifies:**

- "LSTM achieves 10–15% lower RMSE than traditional machine learning models on high-volatility individual-level time series data (Kong et al., 2017)."
- "Hybrid CNN-LSTM models reduce MSE to 0.3738 on residential energy data by capturing both local and global temporal patterns (Kim & Cho, 2019)."
- "Transformer-based models with sparse attention achieve up to 5× faster inference than RNNs while maintaining comparable forecasting accuracy (Chan & Yeo, 2024)."
- "No universal forecasting method exists; algorithm selection must align with data volatility, seasonality, forecast horizon, and computational constraints."
- "Standard evaluation metrics for forecast accuracy include MAPE, RMSE, and MAE, which are directly applicable to Odin's spending forecasting module."

**Limits of relevance:**

- Domain is electricity consumption, not personal spending; electricity has daily/seasonal cycles and weather dependency, while spending patterns are driven by income, obligations, and lifestyle — though both are time series with autocorrelation.
- Data source differences: electricity studies use smart meters (automated, high-frequency); Odin uses manual user input (sparse, potentially lower frequency and accuracy).
- No evaluation of cold-start forecasting (new users with no history) — a critical gap for Odin that this review does not address.
- Computational constraints of mobile devices are not discussed; deep learning inference speed and battery impact remain unexamined.

### Limitations

- Review paper synthesizes existing studies rather than presenting original experiments; conclusions depend on the quality and context of cited works.
- Focus on electricity consumption only; generalizability to financial spending time series is assumed but not tested. [unacknowledged]
- Does not address forecasting under manual data entry constraints (e.g., irregular logging, missing entries, user fatigue) — core to Odin's manual-input design. [unacknowledged]
- Minimal discussion of computational feasibility on mobile hardware or in-browser inference, which is essential for Odin's mobile-first architecture. [unacknowledged]
- The hybrid and deep learning methods reported often require large training datasets; applicability to Odin's smaller per-user transaction histories is uncertain.

---

## Source: `12.B/I--Saeedian_2024_summarized.md`

**Title:** A Comparative Review of Electricity Load Forecasting Methods Across Temporal Horizons

### TL;DR

LSTM and hybrid models outperform statistical methods like SARIMA for nonlinear time series forecasting, with LSTM achieving MAPE as low as 2.42% in short-term electricity demand.

### Findings

1. LSTM achieved **2.42% MAPE** for short-term forecasting, outperforming SARIMA (which did not report comparable MAPE) and ARIMA (MAPE >5%).
2. Hybrid models (e.g., CNN-LSTM, ETS+LSTM) reduced MAPE by up to 25% over standalone models.
3. Transformer-based models (LDTformer, Autoformer) achieved MAE as low as 0.173 and SMAPE of 0.0186 for 4-week forecasts.

- SARIMA works well for stable seasonal patterns but fails on nonlinear, high-frequency, or volatile data.
- k-NN is interpretable but computationally expensive for large datasets; tree-based ensembles (XGBoost, LightGBM) balance accuracy and efficiency.
- No single model is universally optimal; selection depends on horizon, data volume, and need for interpretability.

### Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

8.A — Anomaly Detection in Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly supports Odin's spending forecasting module by providing a comprehensive comparison of time series forecasting algorithms (SARIMA, LSTM, XGBoost, Transformer) and their trade-offs in accuracy, interpretability, and data requirements. The finding that LSTM outperforms statistical models on nonlinear, irregular sequences justifies Odin's use of sequential deep learning for per-category spending prediction, even though the domain is electricity rather than personal finance. The review of error metrics (MAE, MAPE, RMSE) establishes standard evaluation practices that Odin can adopt for module-level validation. Additionally, the discussion of anomaly detection methods (e.g., extreme weather identification) maps directly to Odin's anomalous spending detection — both require identifying deviations from learned patterns.

**Directly justifies:**

- "LSTM achieves 2.42% MAPE on short-term forecasting tasks, significantly outperforming SARIMA and ARIMA on nonlinear time series data."
- "Hybrid models combining statistical decomposition (ETS, ARIMA) with LSTM reduce forecasting error by up to 25% compared to standalone models."
- "XGBoost achieves the lowest MAPE (1.88%) among machine learning models for short-term forecasting, balancing accuracy and computational efficiency."
- "Quantile regression enables probabilistic forecasting, capturing uncertainty in demand — applicable to spending forecasts with confidence intervals."
- "For anomaly detection, Bagging-XGBoost robustly identifies extreme deviations (weather events); similar unsupervised or ensemble methods can flag spending outliers without labeled data."

**Limits of relevance:**

- Domain is electricity load, not personal spending — transaction patterns differ in scale, frequency, and drivers (e.g., income vs. temperature).
- Paper assumes abundant historical data (smart meters, weather stations); Odin's cold-start scenario (new users with no history) is not addressed.
- Many hybrid models require significant computational resources and tuning, which may exceed Odin's mobile-first constraints.
- Geographic and cultural context is Western/global; Filipino-specific spending seasonality (e.g., 13th month pay, remittances) is not discussed.

### Limitations

- Review is qualitative comparative analysis, not a controlled benchmark — performance claims aggregated from multiple studies with different datasets and preprocessing.
- No evaluation of forecasting methods under cold-start conditions (new users, no history) — a critical gap for Odin. [unacknowledged]
- Focuses on electricity load; assumes stationarity and seasonality that may not perfectly align with irregular human spending behavior.
- Deep learning and hybrid models require large datasets and high computational power — practical deployment constraints not quantified.
- Probabilistic forecasting methods (quantile regression, prediction intervals) are mentioned but not deeply evaluated for real-time use.

---

## Source: `4.A/I--D'Souza_et-al_2026_summarized.md`

**Title:** A Comprehensive Review of Machine Learning Techniques for Intelligent Personal Finance Management Systems

### TL;DR

A systematic review of ML techniques for PFMS finds fragmented research across budgeting, forecasting, anomaly detection, and group finance, with a clear shift from rule-based to adaptive, data-driven systems.

### Findings

- Budgeting has evolved from static rule enforcement to behavior-aware approaches (EWMA, clustering, LSTM) that capture temporal spending patterns.
- **The literature remains fragmented, with limited emphasis on unified system-level integration across budgeting, forecasting, anomaly detection, and collaborative finance.**
- Forecasting methods range from linear statistical models (ARIMA) to non-linear deep learning (LSTM/GRU) and hybrid ARIMA-LSTM ensembles that combine both strengths.
- Anomaly detection in PFMS is inherently unsupervised; Isolation Forest is highlighted as superior to density-based methods for scalable deviation detection.
- Group expense management has advanced from manual ledgers to graph-based settlement optimization and ML-based payer prediction.
- Deep learning models (LSTM) require substantial historical data and computational resources, limiting applicability for users with sparse records.

### Relevance to Odin

**Topics:**

4.A — Landscape of Existing Personal Finance Systems

4.B — Limitations and Gaps in Existing Systems

5.A — Financial Behavioral Profiles in Personal Finance

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

7.A — Budgeting Strategies as Domain Knowledge

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

**Contribution to Odin:**

This review provides direct comparative evidence for Odin's algorithm selection across multiple modules. The finding that LSTM captures long-term expenditure dependencies but requires substantial historical data justifies Odin's forecasting module design — using LSTM only after sufficient user history accumulates, with fallback to ARIMA during cold-start. The comparative analysis of anomaly detection techniques supports Odin's choice of Isolation Forest over One-Class SVM or autoencoders, citing its superior scalability and unsupervised deviation isolation. The paper's explicit observation that PFMS research remains fragmented across budgeting, forecasting, and anomaly detection directly justifies Odin's integrated system-level approach, where all three components share a unified data pipeline. Additionally, the review's emphasis on interpretability trade-offs (LSTM low interpretability vs. EWMA high) informs Odin's XAI layer requirements for user trust.

**Directly justifies:**

- "EWMA provides high interpretability and low data requirements but fails to capture seasonal variations or non-linear spending shifts."
- "LSTM captures long-term dependencies in expenditure sequences but requires substantial historical data and computational resources, limiting applicability for users with sparse records."
- "Isolation Forest achieves superior anomaly detection capability relative to density-based and boundary-based alternatives in PFMS environments, operating in O(n log n) time without labeling."
- "Statistical models like ARIMA are more resilient in data-sparse settings but require stationarity through preprocessing techniques such as differencing."
- "The literature remains fragmented — budgeting, forecasting, anomaly detection, and collaborative finance are rarely examined together within a cohesive PFMS framework."

**Limits of relevance:**

- Review is not specific to Filipino financial behavior, spending patterns, or cultural obligations (e.g., remittances, family support).
- No evaluation of mobile-first constraints or manual transaction entry scenarios; assumes digital transaction logs.
- Qualitative comparison lacks quantitative performance benchmarks (e.g., MAE, F1 scores) under Philippine user conditions.
- Does not address data privacy, RA 10173 compliance, or user trust mechanisms specific to local context.

### Limitations

- The review is qualitative; no meta-analysis or quantitative pooling of results across studies.
- Limited discussion of cold-start scenarios for new users with no transaction history — a critical gap for Odin. [unacknowledged]
- Group expense management section is less relevant to Odin's personal-budget-only scope.
- Does not address mobile deployment constraints (battery, compute, offline sync) despite PFMS often being mobile-first. [unacknowledged]
- No evaluation of user retention or engagement mechanisms linked to ML feature adoption.

---

## Source: `4.A/I--Ma_et-al_2023_summarized.md`

**Title:** Review of Family-Level Short-Term Load Forecasting and Its Application in Household Energy Management System

### TL;DR

LSTM neural networks outperform classical time-series models for household-level load forecasting by learning long-term dependencies, and hybrid CNN-LSTM models further improve accuracy.

### Findings

1. LSTM-based frameworks achieve **higher prediction accuracy** than ARIMA, SVR, and Random Forest on household load data due to memory cells and gating mechanisms that capture long-term dependencies.
2. A hybrid SVR-LSTM model achieved the highest correlation coefficient (**R = 0.9901**) and lowest error on microgrid load data, outperforming standalone SVR and LSTM.
3. A CNN-GRU model with attention mechanism reached **92.06% accuracy** for small-range load prediction and reduced prediction time by **75%** compared to general deep learning models.

- Bottom-up forecasting (appliance-level then aggregation) improves accuracy over direct household-level forecasting, but LSTM in this mode is computationally expensive; Kalman filters offer a lighter alternative.
- Probabilistic load forecasting captures uncertainty (e.g., confidence intervals) better than single-value deterministic forecasts, essential for robust HEMS scheduling.
- Online adaptive RNNs that continuously learn from new data can handle concept drift caused by changing user behavior patterns.

### Relevance to Odin

**Topics:**

4.A — Landscape of Existing Personal Finance Systems

5.A — Financial Behavioral Profiles in Personal Finance

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

**Contribution to Odin:**

This review directly supports Odin's spending forecasting module by systematically comparing deep learning architectures (LSTM, CNN, hybrid) for time-series prediction on irregular, behavior-driven data – exactly the challenge Odin faces with manual transaction histories. The finding that LSTM captures long-term dependencies better than classical models (ARIMA, SVR) justifies selecting LSTM or a hybrid as the forecasting algorithm. The review's discussion of adaptive online learning to handle concept drift (changing user behavior) informs Odin's requirement that behavioral profiles update over time. Although the domain is electricity consumption, the methodological insights transfer directly to financial transaction sequences, which also exhibit temporal dependence and user-specific patterns.

**Directly justifies:**

- "LSTM networks achieve superior accuracy over ARIMA, SVR, and Random Forest on non-linear, non-stationary household time-series data, making them the preferred architecture for spending forecasting in personal finance systems."
- "Hybrid CNN-LSTM models can capture both short-term local patterns (via CNN) and long-term dependencies (via LSTM), improving forecast accuracy on irregular sequences."
- "Probabilistic forecasting methods (quantile regression, Bayesian deep learning) provide uncertainty intervals alongside point predictions, enabling risk-aware budget recommendations."
- "Online adaptive RNNs that continuously learn from new data can handle concept drift caused by changing user behavior, addressing the cold-start and profile-update problems in financial profiling."
- "Bottom-up forecasting – predicting category-level spending first then aggregating – reduces error compared to direct total spending prediction, analogous to appliance-level then household total in load forecasting."

**Limits of relevance:**

- Domain is electricity load, not financial spending; spending patterns have different drivers (income, prices, preferences vs. weather, appliance schedules).
- The review focuses on short-term forecasting (hours to days), while Odin primarily needs monthly and weekly budget forecasting.
- Data availability differs: smart meters provide high-frequency automatic readings; Odin relies on sparse, manual transaction entries.
- Many deep learning models discussed require substantial historical data; Odin's cold-start scenario (new users with little history) may need lighter algorithms (e.g., Kalman filters mentioned in the paper).

### Limitations

- The paper is a review, not a primary study; claimed performance numbers (e.g., 92.06% accuracy) come from cited works, not validated in a single controlled experiment.
- No direct comparison of forecasting algorithms on a standardized household load dataset; each study uses different data, time horizons, and evaluation metrics.
- Computational efficiency of LSTM and hybrid models for mobile deployment is not addressed – a critical constraint for Odin's mobile-first design. [unacknowledged]
- The review does not discuss handling of missing or sparse data (e.g., users who forget to log transactions), which is central to Odin's manual input model. [unacknowledged]
- All cited studies are from non-Philippine contexts; cultural spending patterns and income volatility in Metro Manila may alter forecasting performance.

---

## Source: `5.B/I--Xiang_et-al_2023_summarized.md`

**Title:** Concept Drift Adaptation Methods under the Deep Learning Framework: A Literature Review

### TL;DR

Deep learning models fail when data distributions change over time; adaptation methods using discriminative, generative, hybrid, transfer, or reinforcement learning maintain prediction accuracy under concept drift.

### Findings

1. **Parameter updates (weight adjustments) dominate over structure updates** because they converge faster and handle abrupt drift effectively.
2. Active drift detection (e.g., ADWIN, STEPD, CUSUM) appears in ~half of discriminative and generative methods; passive continuous updating is common in hybrid approaches.
3. **Abrupt drift is the most frequently addressed type**, while recurring drift receives least attention despite reappearing in cyclical domains.
4. LSTM‑based adaptation (I‑LSTM, AD‑LSTM, Fog‑DeepStream) achieves strong results in anomaly detection and power forecasting by weighting newer data higher.
5. Autoencoder‑based generative methods (ARCUS, MemStream) enable unsupervised drift adaptation for high‑dimensional anomaly detection without labels.
6. Hybrid LSTM+CNN and LSTM+AE models overcome catastrophic forgetting and improve long‑term prediction under gradual and recurring drift.
7. Deep reinforcement learning (DeepPocket, DeepBreath) adapts investment portfolios to market drift but requires long training times.

### Relevance to Odin

**Topics:**

5.B — Profile Dynamics and the Cold‑Start Problem

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

**Contribution to Odin:**

This review provides the theoretical foundation for why Odin’s behavioral profiles, spending forecasts, and anomaly detectors must adapt over time. User financial behavior drifts due to job changes, salary adjustments, new obligations (e.g., rent, family support), or seasonal spending (holidays, 13th month pay). Without concept drift adaptation, a model trained on a user’s past transactions becomes obsolete. The paper’s taxonomy of drift types (abrupt, incremental, gradual, recurring) directly informs Odin’s profiling module design — recurring drift justifies storing past profile states for seasonal reuse, while abrupt drift detection (using methods like ADWIN or STEPD) triggers immediate model updates. The comparison between parameter updates (faster, suits abrupt drift) and structure updates (more flexible, suits recurring drift) guides Odin’s implementation choices for forecasting and anomaly detection algorithms.

**Directly justifies:**

- "User financial behavior evolves over time (concept drift); a static spending forecast model becomes inaccurate within months unless updated via drift adaptation."
- "Parameter updates (e.g., retraining only the last layer) converge faster than full structure updates, making them suitable for detecting abrupt changes in spending patterns after a job loss or salary increase."
- "Recurring drift (e.g., higher spending every December) can be handled by storing and reactivating past profile states, reducing computational overhead."
- "Unsupervised drift detection using autoencoder reconstruction error enables anomaly detection in spending without requiring labeled fraud data, applicable to Odin’s cold‑start problem."
- "LSTM‑based models with time‑weighted sampling (I‑LSTM) improve anomaly detection under drift by assigning higher importance to recent transactions."

**Limits of relevance:**

- The review focuses on deep learning; Odin may use lighter models (e.g., gradient boosting, logistic regression) for resource‑constrained mobile deployment.
- Most evaluated datasets are not financial (e.g., electricity, weather, network intrusion); financial transaction patterns have different drift characteristics (e.g., slower, more seasonal).
- Many methods require labeled data for drift detection; Odin’s manual transaction input produces sparse labels (user‑corrected categories), limiting supervised drift detection.
- Computational overhead of active drift detection (e.g., STEPD, CUSUM) may conflict with mobile‑first, battery‑sensitive design.

### Limitations

- Review does not quantitatively compare adaptation methods across standard financial benchmarks — lacks performance metrics (e.g., MAE improvement, detection delay). [unacknowledged]
- Most cited methods were evaluated on public datasets (Electricity, Weather, KDD Cup) that differ from personal transaction streams in volume, sparsity, and label availability.
- No discussion of concept drift adaptation under cold‑start conditions (new users with no history), which is critical for Odin.
- The paper acknowledges that recurring drift is under‑addressed — yet recurring seasonal spending is highly relevant to Filipino young professionals (13th month pay, Christmas, back‑to‑school).
- Many active detection methods (ADWIN, STEPD, CUSUM) require tuning hyperparameters (window sizes, thresholds) that are not transferable across users without calibration.

---

## Source: `5.C/I--D'Souza_et-al_2026_summarized.md`

**Title:** A Comprehensive Review of Machine Learning Techniques for Intelligent Personal Finance Management Systems

### TL;DR

A qualitative review of machine learning for personal finance systems finds that adaptive budgeting, hybrid forecasting, unsupervised anomaly detection, and automated group settlement each outperform static rule-based approaches, but integration remains fragmented.

### Findings

- Budgeting has evolved from static thresholds to adaptive methods (EWMA, clustering, LSTM) that capture temporal spending patterns.
- **No unified intelligent PFMS framework exists; component-level research remains fragmented.**
- Hybrid ARIMA–LSTM forecasting improves robustness by combining linear trends and non-linear residuals.
- Isolation Forest outperforms density-based and boundary-based anomaly detectors in unlabeled personal finance data.
- Explainable AI (XAI) is emerging as critical for user trust in ML-driven PFMS.

### Relevance to Odin

**Topics:**

4.A — Landscape of Existing Personal Finance Systems

4.B — Limitations and Gaps in Existing Systems

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

7.A — Budgeting Strategies as Domain Knowledge

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

**Contribution to Odin:**

This review directly informs Odin's algorithm selection across multiple modules by providing a comparative analysis of candidate techniques. For spending forecasting, it justifies hybrid ARIMA–LSTM over standalone methods by demonstrating complementary handling of linear trends and non-linear residuals. For anomaly detection, it establishes Isolation Forest as the preferred unsupervised method for unlabeled personal spending data, which matches Odin's cold-start condition. The review's explicit finding that no unified intelligent PFMS exists supports Odin's integrated design ambition. Although the paper lacks empirical benchmarks, its qualitative trade-off analysis (interpretability vs. adaptability) guides Odin's design decisions between transparent rule-based heuristics and more powerful but opaque deep learning models.

**Directly justifies:**

- "Budgeting mechanisms have progressed from static rule enforcement to adaptive approaches (EWMA, clustering, LSTM) that capture temporal spending patterns and support personalized budget limits."
- "Isolation Forest outperforms density-based and boundary-based anomaly detection methods for unlabeled personal finance data, offering high scalability and adaptability."
- "Hybrid ARIMA–LSTM forecasting improves robustness across diverse financial conditions by combining linear trend modeling with non-linear residual learning."
- "No unified intelligent PFMS framework integrating budgeting, forecasting, anomaly detection, and group finance exists; component-level research remains fragmented."
- "Explainable AI is a critical requirement for user trust and accountability in ML-driven personal finance decision-support systems."

**Limits of relevance:**

- Qualitative review with no empirical performance numbers (e.g., MAE, F1 scores) — Odin cannot cite specific accuracy benchmarks from this paper.
- Not specific to Filipino young professionals or Metro Manila context; spending patterns and income volatility differ.
- Does not address mobile-first deployment constraints (battery, compute, offline capability) relevant to Odin.
- Group expense management section is not directly applicable to Odin (single-user system).

### Limitations

- Qualitative synthesis only — no quantitative meta-analysis or benchmark comparisons across models.
- Literature reviewed is fragmented; the paper itself acknowledges that no integrated system exists. [unacknowledged]
- Does not address cold-start problem for new users with no spending history — a core Odin challenge.
- No discussion of privacy, data protection (RA 10173), or user trust beyond mentioning XAI.
- Forecasting horizon specificity (short-term vs long-term) is discussed but not tied to real-world PFMS evaluation.

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

## Source: `6.A/I--Mathumitha_et-al_2024_summarized.md`

**Title:** Intelligent deep learning techniques for energy consumption forecasting in smart buildings: a review

### TL;DR

Deep learning models, especially hybrid CNN-LSTM architectures, consistently outperform traditional time series methods for building energy forecasting by automatically learning temporal dependencies.

### Findings

- **72% of reviewed studies focused on non-residential buildings**, 18% on residential, and 10% on both.
- **68% of studies used short-term forecasting (days to weeks)**; only 5% used medium-term.
- Hybrid CNN-LSTM models achieve the highest reported accuracy, reducing RMSE by up to 40% compared to standalone RNNs or ARIMA.
- LSTM and GRU effectively handle vanishing gradient problems that limit traditional RNNs.
- Weather variables (temperature, humidity) are the most influential external factors after historical consumption.
- Peak load prediction remains a persistent challenge — most ML models underperform during irregular demand spikes.

### Relevance to Odin

**Topics:**

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

**Contribution to Odin:**

This review directly informs Odin's spending forecasting module by systematically comparing time series forecasting algorithms. The finding that hybrid CNN-LSTM models achieve lower error than standalone RNNs or ARIMA justifies evaluating hybrid architectures for per-category spending prediction. The review's emphasis on LSTM's ability to handle long-term dependencies and irregular patterns is directly applicable to Odin's transaction sequences, which are sparse and exhibit weekly/monthly cycles. Although the domain is building energy, the methodological comparisons of forecast horizons, input features (historical + calendar + weather → analogous to historical spending + calendar events), and error metrics transfer cleanly to financial time series.

**Directly justifies:**

- "Hybrid CNN-LSTM architectures reduce RMSE by up to 40% compared to standalone RNNs or ARIMA in time series forecasting tasks with irregular patterns."
- "LSTM and GRU overcome the vanishing gradient problem that limits traditional RNNs, enabling effective learning of long-term dependencies in sequential transaction data."
- "Short-term forecasting (days to weeks) accounts for 68% of reviewed studies, reflecting its higher accuracy and immediate operational value — a principle applicable to Odin's per-month budget forecasting."
- "Weather variables are the most influential external factor after historical consumption; by analogy, calendar events (paydays, holidays, bill due dates) should be key inputs to spending forecasts."

**Limits of relevance:**

- Domain is building energy consumption, not personal financial transactions; spending patterns have different drivers (income, discretionary choice) than thermostatic loads.
- Review reports aggregated findings from many studies; no single controlled experiment comparing algorithms on financial data.
- Most reviewed datasets are high-frequency (minute/hourly) smart meter data; Odin uses daily or per-transaction manual entries, which are sparser.
- Peak load prediction challenges in energy may not directly parallel anomalous spending detection, which has different behavioral causes.

### Limitations

- Review does not conduct its own experiments; all performance claims are aggregated from primary studies with varying datasets and evaluation protocols.
- No critical assessment of publication bias — studies reporting positive results for deep learning may be overrepresented. [unacknowledged]
- Limited discussion of computational cost or mobile deployment constraints, which are critical for Odin's mobile-first design.
- All reviewed studies use automated smart meter data; none use manually entered transaction data, so cold-start and user entry friction are not addressed.
- Geographic scope is global; none of the datasets or building types reflect Philippine climate or occupancy patterns.
