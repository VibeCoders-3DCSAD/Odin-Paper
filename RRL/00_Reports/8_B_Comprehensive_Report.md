# Comprehensive Report for Subtopic: `8.B`

**Total files:** 38

This report includes problem/motivation, approach, key findings, support for Odin, and limitations/contradictions.

---


## Deep Learning for Credit Risk Prediction: A Survey of Methods, Applications, and Challenges
**Filename:** `IA--Mienye-et_al-2026_summarized.md`  
**Authors:** Mienye, I. D.; Esenogho, E.; Modisane, C. (2026)  
**ID:** `10.3390/info17040395`  
**Odin Topics:** 3.A, 5.C, 6.B, 8.B, 10.A, 12.B  

**TLDR:** Deep learning architectures including MLPs, RNNs, transformers, and GNNs improve credit risk prediction over traditional models when large, rich datasets are available, but face challenges in interpretability, fairness, and operational deployment.

**Problem & Motivation:** Traditional credit risk models like logistic regression fail to capture nonlinear interactions and temporal dynamics in borrower data. Deep learning offers architectures that can model complex patterns, but a systematic review focusing on borrower-level prediction across model families was missing.

**Approach (summary):**
- Searched IEEE Xplore, Scopus, ACM, ScienceDirect, SpringerLink, Web of Science, and Google Scholar using credit-risk and deep learning terms.
- Screened 380 records via PRISMA flow, retaining 140 deep learning application studies and 18 surveys.
- Extracted data on data modality (tabular, sequential, textual, relational), model architecture (MLP, CNN, RNN/LSTM/GRU, Transformer, GNN, hybrid), credit product segment, and evaluation metrics.

**Key Findings (selected):**
- "num: LSTM reduced MAE from 0.095 to 0.072 and RMSE from 0.119 to 0.093 for peer-to-peer default rate forecasting."
- "num: TabNet-Stacking ensemble achieved accuracy 0.979 and AUC 0.941 on the Tianchi credit dataset."
- "num: Residual-enhanced BiLSTM with multi-head attention achieved AUC 0.982 and F1 0.958 on Freddie Mac data."
- Deep models outperform traditional scorecards and ensembles only when trained on sufficiently large, temporally representative datasets.

**Limitations / Contradictions for Odin:**
- "Survey limited to peer-reviewed English-language studies indexed in major databases; does not cover proprietary implementations or regulatory grey literature."
- "Non-trivial portion of deep credit risk studies relies on random splits instead of time-ordered validation, weakening external validity. [unacknowledged]"
- "Interpretability and fairness are often treated as add-ons rather than integrated into training objectives. [unacknowledged]"

**Key takeaways:**
- "Deep learning improves credit risk prediction on large, rich datasets."
- "Time-ordered validation is essential to avoid over-optimistic performance estimates."
- "Calibration metrics like Brier score matter more than AUC alone."

---


## AI-BASED PERSONAL FINANCE MANAGER (AI)
**Filename:** `IA--Sireesha-et_al_summarized.md`  
**Authors:** Sireesha, B.; Kiran Kumar, K.; Lavanya, O.; Keshan, S.; Ramsai, N.; Latheesh Kumar, K. (2026)  
**ID:** `a8b9c0d1-e2f3-4a5b-8c9d-0e1f2a3b4c5d`  
**Odin Topics:** 3.A, 3.B, 5.A, 5.C, 6.A, 6.B, 7.A, 7.B, 7.C, 8.A, 8.B, 12.A, 12.B, 13.A  

**TLDR:** An AI-based personal finance manager using machine learning, deep learning, and reinforcement learning automates expense categorization, spending forecasting, anomaly detection, and personalized budget recommendations.

**Problem & Motivation:** Users struggle to monitor spending, manage budgets, and make informed decisions due to lack of time, financial literacy, or analytical tools. Traditional finance management tools rely on static rules, offering limited personalization and predictive capabilities. An AI-powered solution is needed to automate data analysis, provide personalized insights, and adapt to dynamic user behavior.

**Approach (summary):**
- Data is collected from banking statements, e-commerce receipts, and user inputs then preprocessed via cleaning, normalization, tokenization, and category mapping.
- Random Forest, Gradient Boosting, SVM, and neural networks classify expenses into categories like food, transport, rent, and utilities.
- An LSTM model forecasts monthly expenditures and revenue streams, achieving a Mean Absolute Error of 4.7%.

**Key Findings (selected):**
- num: Random Forest expense classifier achieved 93-96% accuracy, outperforming rule-based systems (75-80%).
- num: LSTM forecasting produced a Mean Absolute Error of 4.7% for monthly expenditure prediction.
- num: Isolation Forest anomaly detection achieved 92% precision.
- num: 84% of users reported better spending awareness and 78% claimed increased savings control after one month.

**Limitations / Contradictions for Odin:**
- Usability study limited to 50 participants, may not generalize. [unacknowledged]
- Long-term retention and engagement not evaluated. [unacknowledged]
- Data privacy and security not experimentally validated. [unacknowledged]

**Key takeaways:**
- Random Forest categorizes expenses with 93-96% accuracy.
- LSTM forecasts monthly spending with 4.7% MAE.
- 84% of users report better spending awareness after using the system.

---


## A Decade of Applied Quantitative Analytics for Philippine Policy: Forecasting, Statistical Forensics, and Predictive Modeling Across Education, Energy, Agriculture, Health, and Finance
**Filename:** `LA--Velasco_summarized.md`  
**Authors:** Velasco, A. (2026)  
**ID:** `10.20944/preprints202603.1811.v1`  
**Odin Topics:** 6.A, 6.B, 8.A, 8.B, 12.A, 12.B  

**TLDR:** Reviews 17 Philippine policy analytics studies (2019-2025), showing progression from descriptive statistics and classical forecasting toward machine learning, deep learning, Benford-based anomaly detection, and explainable AI.

**Problem & Motivation:** Government resource allocation under uncertainty requires quantitative analytics, but no systematic review of applied methods in Philippine policy existed. Understanding methodological progress and gaps across education, energy, agriculture, health, and finance is necessary to guide future analytics infrastructure.

**Approach (summary):**
- Structured narrative review of 17 studies from 2019-2025, coded by domain, dataset, modeling approach, validation strategy, and policy contribution.
- Comparison with international literature on dropout research, electricity forecasting, crop-yield analytics, epidemiological surveillance, Benford auditing, and explainable ML.

**Key Findings (selected):**
- Early studies use descriptive statistics and univariate ARIMA/SARIMA/Holt-Winters; later studies adopt comparative machine learning, neural networks, and LSTM.
- Benford-based anomaly detection screens public health and agricultural data quality as a policy tool.
- Validation rigor is uneven: some studies use holdout splits and error metrics, others rely on residual diagnostics due to short samples.
- Interpretability appears via SHAP in diabetes prediction and theory-guided embedding in stock-index forecasting.

**Limitations / Contradictions for Odin:**
- "Corpus is heterogeneous (journal articles, preprints, SSRN papers) with differing data frequencies, sample sizes, and validation maturity."
- "Some study characteristics had to be reconstructed from metadata when full texts were not equally accessible. [unacknowledged]"
- "Direct numerical comparison across sectors is neither appropriate nor intended by the author."

**Key takeaways:**
- "Reviewed 17 Philippine policy analytics studies from 2019 to 2025."
- "Forecasting evolved from ARIMA to machine learning and LSTM."
- "Benford's law detects anomalies in health and agricultural data."

---


## Research Progress and Trends of Deep Learning in Stock Price Prediction: A Systematic Review from LSTM to Transformer
**Filename:** `IA--Gong_summarized.md`  
**Authors:** Gong, H. (2026)  
**ID:** `d3b5c6e7-f8a9-4b0c-91d2-e3f4a5b6c7d8`  
**Odin Topics:** 6.A, 6.B, 8.A, 8.B, 12.A  

**TLDR:** Systematically reviews deep learning models for stock price prediction from LSTM to Transformer, comparing architectures, datasets, and evaluation metrics.

**Problem & Motivation:** Traditional statistical and machine learning methods fail to capture the non-linear, non-stationary dynamics of stock markets. Deep learning models like LSTM and Transformer have shown superior performance, but a systematic review tracing their evolution from LSTM to hybrid architectures is missing. This gap makes it difficult for researchers to select appropriate models for financial time series forecasting.

**Approach (summary):**
- Conducts a systematic literature review of deep learning models for stock price prediction.
- Analyzes recurrent models (RNN, LSTM, GRU), convolutional models (CNN), Transformer variants, and hybrid models.
- Compares datasets including S&P 500, NIFTY 50, Moroccan market, and limit order book data.

**Key Findings (selected):**
- "num: LSTM achieved 0.46% daily return on S&P 500 constituents (1992-2015) with Sharpe ratio up to 2.34."
- "num: Transformer reduced MAE by 20.73%, MSE by 34.84%, and MAPE by 25.63% compared to LSTM in new energy vehicle stock prediction."
- "num: LSTM-Transformer hybrid reduced MAE and RMSE by over 50% relative to parent models and attained R² of 0.9618 (LSTM: 0.8430, Transformer: 0.7763)."
- Deep learning models consistently outperform traditional statistical methods and shallow machine learning.

**Limitations / Contradictions for Odin:**
- "Systematic review without original empirical validation; relies on cited studies. [unacknowledged]"
- "Focus on stock markets limits direct applicability to personal spending data. [unacknowledged]"
- "Does not address real-time deployment constraints or latency requirements for mobile apps."

**Key takeaways:**
- "LSTM achieves 0.46% daily return with Sharpe ratio 2.34 on S&P 500."
- "Transformer reduces MAE by 20.73% compared to LSTM in stock prediction."
- "LSTM-Transformer hybrid reduces error by over 50% and achieves R² 0.96."

---


## Systematic review of deep and machine learning for financial modeling
**Filename:** `IA--Zlobin-&-Bazylevych_summarized.md`  
**Authors:** Zlobin, M.; Bazylevych, V. (2025)  
**ID:** `10.25140/2411-5363-2025-1(39)-184-195`  
**Odin Topics:** 6.A, 6.B, 8.A, 8.B, 11.A, 11.B, 12.A, 12.B  

**TLDR:** Systematic review of 41 papers on ML/DL for financial classification and regression tasks including credit scoring, fraud detection, stock prediction, and anomaly detection.

**Problem & Motivation:** Financial institutions face datasets that traditional analytical methods cannot process effectively. ML and DL offer improved predictive accuracy but challenges like model interpretability, data quality, and concept drift remain. A systematic synthesis of state-of-the-art methods is needed to identify gaps and guide future research.

**Approach (summary):**
- Review of 41 peer-reviewed papers on ML/DL applications in finance published up to 2025.
- Focus on classification tasks (credit scoring, fraud detection, customer segmentation) and regression tasks (stock price prediction, volatility forecasting, option pricing).
- Comparative analysis of model performance using metrics such as AUC, RMSE, accuracy, precision, recall, and F1-score.

**Key Findings (selected):**
- "num: Random forest with ensemble feature selection achieved 99.6% accuracy and 100% precision in credit card fraud detection."
- "num: XGBoost consistently outperformed deep neural networks across 10 credit scoring datasets, achieving highest AUC and efficiency."
- "num: CNN reduced fraud detection cost of failure by 30% and achieved 87.64% AUC on European dataset."
- "num: GCN achieved 94.5% fraud detection accuracy, outperforming CNN (93%) by improving recall by 10% via graph-based user relationship analysis."

**Limitations / Contradictions for Odin:**
- "Review primarily cites papers up to 2024; rapid ML/DL advances may render some comparisons outdated. [unacknowledged]"
- "Performance metrics are aggregated across heterogeneous datasets, making direct apples-to-apples comparisons difficult. [unacknowledged]"
- "The review does not address computational resource constraints of mobile-first deployment, which is critical for Odin. [unacknowledged]"

**Key takeaways:**
- "XGBoost outperforms deep learning for credit scoring across 10 datasets."
- "Random forest achieves 99.6% fraud detection accuracy with feature selection."
- "AI personalization lifts user engagement by 27% and retention by 15%."

---


## Selected Topics in Time Series Forecasting: Statistical Models vs. Machine Learning
**Filename:** `IA--Tjostheim_summarized.md`  
**Authors:** Tjøstheim, D. (2025)  
**ID:** `10.3390/e27030279`  
**Odin Topics:** 6.A, 6.B, 7.A, 7.B, 7.C, 8.A, 8.B, 12.A, 12.B  

**TLDR:** A survey comparing statistical models and machine learning methods for time series forecasting, analyzing results from M1-M6 forecasting competitions and weather forecasting.

**Problem & Motivation:** The forecasting community lacks a systematic comparison between traditional parametric statistical models and modern machine learning methods across different data regimes and application domains. Understanding when each approach excels is critical for practitioners, yet black-box nature and lack of theoretical results for ML methods raise concerns. This review synthesizes evidence from forecasting competitions and specialized applications to guide method selection.

**Approach (summary):**
- Surveys classical parametric models: exponential smoothing, ARIMA, theta method, and state space models.
- Reviews nonlinear parametric models: threshold autoregression, STAR, and hidden Markov chain models.
- Presents ML methods: CNNs/TCNs, RNNs, LSTM, transformers, random forest, and gradient boosting.

**Key Findings (selected):**
- "num: In M4 competition (100,000 series), only 1 pure statistical method ranked among top 10 most accurate methods."
- "num: Light-GBM gradient boosting outperformed all alternatives in M5 retail sales competition."
- "ML methods excel for high spectral entropy data (noisy, short-interval, irregular time series)."
- "num: GraphCast beats HRES (industry gold standard) in medium-range weather forecasts up to 10 days."

**Limitations / Contradictions for Odin:**
- "Survey is not systematic; author acknowledges personal research background bias."
- "Limited evaluation of multivariate forecasts and exogenous variable influence. [unacknowledged]"
- "No theoretical convergence results for ML methods in forecasting contexts. [unacknowledged]"

**Key takeaways:**
- "Hybrid statistical-ML methods outperform pure approaches."
- "Light-GBM gradient boosting excelled in M5 with 42,480 retail series."
- "ML methods beat statistical models for noisy, high-frequency data."

---


## Online Payment Fraud Detection Using Decission Tree and LSTM Neural Network
**Filename:** `IA--Ranjan-et_al_summarized.md`  
**Authors:** Ranjan, A.; Jangir, A. K.; Abrol, K.; Saurav, S. (2025)  
**ID:** `10.59256/ijsreat.20250505011`  
**Odin Topics:** 8.A, 8.B, 12.B  

**TLDR:** Online payment fraud detection using a hybrid of Decision Tree for interpretable rule-based screening and LSTM for temporal sequence analysis, evaluated on imbalanced transaction datasets.

**Problem & Motivation:** Traditional rule-based fraud detection systems cannot adapt to evolving fraud patterns. The surge in online payment fraud demands real-time, adaptive solutions. A hybrid approach combining interpretable models and temporal deep learning is needed.

**Approach (summary):**
- Data from IEEE-CIS and Kaggle credit card datasets with extreme class imbalance.
- Preprocessing uses SMOTE for oversampling, time-window aggregates, and sequential encoding for LSTM inputs.
- Two-stage hybrid: Decision Trees for rapid rule-based screening, then LSTM with attention for temporal analysis.

**Key Findings (selected):**
- Hybrid Decision Tree-LSTM models outperform standalone classifiers in fraud detection.
- LSTM networks capture long-term behavioral changes missed by static classifiers.
- Decision Trees provide interpretable rules and sub-millisecond latency per transaction.
- SMOTE and class weighting significantly improve sensitivity to fraudulent transactions.

**Limitations / Contradictions for Odin:**
- No empirical results from the authors' own implementation are reported; the paper is primarily a literature review and conceptual architecture. [unacknowledged]
- The proposed hybrid model's real-time performance on production-scale data is not validated. [unacknowledged]

**Key takeaways:**
- Decision Trees execute in less than one millisecond per transaction.
- LSTM networks capture evolving fraud patterns across transaction sequences.
- Hybrid models balance interpretability and temporal intelligence.

---


## Harnessing artificial intelligence and machine learning for fraud detection and prevention in Nigeria
**Filename:** `IA--Montagna_summarized.md`  
**Authors:** Odufisan, O.I.; Abhulimen, O.V.; Ogunti, E.O. (2025)  
**ID:** `10.1016/j.jeconc.2025.100127`  
**Odin Topics:** 8.A, 8.B, 10.A, 10.B  

**TLDR:** AI and ML methods improve fraud detection in Nigeria by analyzing large datasets for anomalies, enabling real-time prevention across banking, e-commerce, healthcare, and education.

**Problem & Motivation:** Traditional rule-based fraud detection fails to adapt to evolving schemes and cannot handle large data volumes. Fraud costs Nigeria billions and erodes trust in digital services. A more adaptive, intelligent solution is needed.

**Approach (summary):**
- This is a literature review synthesizing secondary data from academic publications, industry reports, and global fraud studies.
- It categorizes AI/ML methods into supervised learning (labeled data), unsupervised learning (anomaly detection), and deep learning (CNNs, RNNs).
- Applications are examined across banking, e-commerce, healthcare, and education sectors in Nigeria.

**Key Findings (selected):**
- "num: Online payment fraud is projected to cost firms globally over $343 billion between 2023 and 2027."
- "num: 24 Nigerian commercial banks lost N5.79 billion to fraud in Q2 2023, a 1125% increase from Q1."
- "num: Support Vector Machines achieved over 98% accuracy for phishing email detection."
- "num: A feed-forward neural network achieved a 97% detection rate for fraudulent credit card transactions and phishing websites."

**Limitations / Contradictions for Odin:**
- Data quality and availability remain significant barriers in developing economies.
- Integrating AI with legacy banking systems requires major investment and planning. [unacknowledged]
- Fraudsters continuously evolve tactics, requiring constant retraining of models.

**Key takeaways:**
- Fraud cost Nigerian banks N5.79 billion in Q2 2023 alone.
- Unsupervised learning detects fraud patterns never seen before.
- AI reduces false positives compared to rigid rule-based systems.

---


## Performance analysis of neural network architectures for time series forecasting: A comparative study of RNN, LSTM, GRU, and hybrid models
**Filename:** `IA--Yunita-et_al_summarized.md`  
**Authors:** Yunita, A.; Pratama, M. I.; Almuzakki, M. Z.; Ramadhan, H.; Akhir, E. A. P.; Mansur, A. B. F.; Basori, A. H. (2025)  
**ID:** `10.1016/j.mex.2025.103462`  
**Odin Topics:** 6.A, 6.B, 8.B, 12.B  

**TLDR:** A benchmark of nine RNN architectures across three time series datasets using Monte Carlo simulation shows no statistically significant differences, but LSTM-based hybrids offer practical advantages in consistency and robustness.

**Problem & Motivation:** Time series forecasting using neural networks suffers from performance variability due to random weight initialization. The reliability and consistency of RNN, LSTM, GRU, and hybrid architectures for time series analysis remain unclear. A systematic benchmark across diverse datasets is needed to guide architecture selection.

**Approach (summary):**
- Three datasets: sunspot activity (monthly, 3625 records), Indonesian COVID-19 daily cases (634 records), and dissolved oxygen concentration (daily, 1033 records).
- Nine architectures: RNN, LSTM, GRU, RNN-LSTM, RNN-GRU, LSTM-RNN, GRU-RNN, LSTM-GRU, and GRU-LSTM, each with two hidden layers.
- Monte Carlo simulation with 100 independent runs, each with 100 training epochs, using 95% confidence interval trimming.

**Key Findings (selected):**
- "num: Friedman test showed no statistically significant differences among nine architectures (χ2=12.593, df=8, p=.127)."
- "num: LSTM-GRU hybrid achieved the lowest mean rank (2.23) while vanilla RNN had the highest (8.57)."
- "num: For sunspot forecasting, LSTM-GRU achieved MAE 16.913 ± 0.629 and RMSE 23.205 ± 0.827."
- "num: For COVID-19 case prediction, standalone LSTM performed best with MAE 0.903 ± 0.091 and MAPE 9.036% ± 0.778%."

**Limitations / Contradictions for Odin:**
- "Only three datasets were used, which may limit generalizability to other time series domains."
- "The Friedman test lacked statistical power due to small sample size; non-significant result may mask real differences."
- "Only two hidden layers were tested; performance rankings could change with deeper or shallower architectures."

**Key takeaways:**
- "No significant difference among nine RNN architectures (p=0.127)."
- "LSTM-GRU hybrid achieved lowest mean rank of 2.23 across datasets."
- "Vanilla RNN consistently underperformed with highest error rates."

---


## "Toward Transparent Optimization: A Systematic Review of Explainable AI in Decision-Making Systems"
**Filename:** `IA--Danach-et_al_summarized.md`  
**Authors:** "Danach, K.; Aly, W. H. F.; Tarhini, A.; Laouadi, S." (2025)  
**ID:** `10.29020/nybg.ejpam.v18i4.6707`  
**Odin Topics:** 6.A, 6.B, 7.B, 7.C, 8.A, 8.B, 10.A, 10.B, 12.A, 12.B  

**TLDR:** "A systematic review synthesizes the integration of explainable AI (XAI) with optimization methods across healthcare, finance, logistics, and energy, proposing a taxonomy and highlighting trade-offs between performance and interpretability."

**Problem & Motivation:** "Optimization-driven AI systems often operate as black boxes, undermining trust, regulatory compliance, and human-AI collaboration in high-stakes decisions. Despite advances in XAI, systematic integration with optimization frameworks remains fragmented and lacks unified taxonomies. This gap hinders the development of transparent, accountable intelligent systems."

**Approach (summary):**
- "Conducted a systematic literature search across Scopus, Web of Science, IEEE Xplore, and ACM Digital Library for 2010-2024, retrieving 642 records and including 112 peer-reviewed studies after screening."
- "Proposed a structured taxonomy categorizing XAI-optimization integration by explainability level, optimization complexity, and domain specificity."
- "Analyzed integration strategies including post-hoc explanations (SHAP, LIME), interpretable models (decision trees, MILP), certificate-based verification, and data-driven frameworks like EXALT."

**Key Findings (selected):**
- "num: EXALT framework reduces explanation generation time by 72% compared to post-hoc methods while maintaining 98% solution optimality."
- "num: Explainable optimization approaches achieve error reduction rates of 41-68% compared to black-box optimization in healthcare logistics and derivatives pricing."
- "Explainability constraints can enhance solution quality by acting as regularizers that embed domain knowledge."
- "The trade-off between optimality and interpretability can be favorable, with explainable path constraints increasing solution cost by only a small margin."

**Limitations / Contradictions for Odin:**
- "Scalability to large-scale industrial problems remains a significant challenge [unacknowledged]."
- "Standardization of explainability metrics and evaluation frameworks is lacking [acknowledged]."
- "Integration with existing enterprise systems and workflows has received limited research attention [unacknowledged]."

**Key takeaways:**
- "Explainable optimization reduces explanation time by 72% while preserving 98% optimality."
- "XAI methods can turn black-box optimizers into transparent, auditable systems."
- "The performance-interpretability trade-off is often favorable in practice."

---


## Harnessing artificial intelligence and machine learning for fraud detection and prevention in Nigeria
**Filename:** `IA--Odufisan-et_al_summarized.md`  
**Authors:** Odufisan, O.I.; Abhulimen, O.V.; Ogunti, E.O. (2025)  
**ID:** `10.1016/j.jeconc.2025.100127`  
**Odin Topics:** 5.A, 8.A, 8.B, 10.A, 10.B  

**TLDR:** AI and ML enable real-time anomaly detection, behavior analysis, and risk scoring to combat fraud across Nigeria's banking, e-commerce, healthcare, and education sectors.

**Problem & Motivation:** Traditional fraud detection methods (rule-based, manual) fail to keep pace with evolving fraud schemes and large data volumes, causing economic losses and eroding trust in Nigeria's digital economy. Fraud threatens financial stability, hinders growth, and undermines digital inclusion. A paradigm shift to adaptive, intelligent systems was missing.

**Approach (summary):**
- Literature review of academic publications, industry reports, government records, and global fraud studies.
- Secondary data on fraud trends, technological adoption, and sectoral impacts across banking, e-commerce, healthcare, and education.
- Primary data from unstructured interviews with stakeholders in Nigerian banking, e-commerce, healthcare, and educational sectors.

**Key Findings (selected):**
- "num: 24 commercial banks lost N5.79 billion to fraud in Q2 2023, a 1125% increase from Q1."
- "num: 94.35% of bank fraud losses came from fraudulent loans."
- "num: SVM achieved over 98% accuracy for phishing email detection."
- "num: Feed-forward neural network achieved 97% detection rate for credit card fraud and phishing websites."

**Limitations / Contradictions for Odin:**
- "Primary data limited to unstructured interviews and anecdotal evidence; no large-scale quantitative study. [unacknowledged]"
- "Does not provide a specific, reproducible algorithm for anomaly detection; remains a high-level review. [unacknowledged]"
- "Ethical concerns like algorithmic bias are mentioned but not explored in depth. [unacknowledged]"

**Key takeaways:**
- "Anomaly detection with ML achieved 97% accuracy for credit card fraud."
- "Real-time analysis enables proactive fraud prevention before losses occur."
- "Behavioral profiling reduces false positives by learning user baselines."

---


## "Credit Card Fraud Detection Through Deep Learning and Real-Time Data Streams: A Comparison and New Directions"
**Filename:** `IA--Polytarchos_summarized.md`  
**Authors:** Polytarchos, E. (2025)  
**ID:** `10.47852/bonviewFSI52026108`  
**Odin Topics:** 5.A, 8.A, 8.B, 12.A, 12.B  

**TLDR:** Compares deep learning (LSTM, MLP) and real-time data stream analysis (BEReTiC) for credit card fraud detection, finding deep learning achieves 92% accuracy but slower adaptation, while real-time clustering offers faster detection with lower false positives.

**Problem & Motivation:** Existing fraud detection methods either rely on batch-trained deep learning requiring extensive preprocessing and retraining, or real-time systems with lower initial accuracy. There is a lack of comprehensive empirical comparison between these paradigms on high-volume financial data. This gap prevents system designers from making informed deployment decisions.

**Approach (summary):**
- Used two proprietary datasets: IND (17.5M individual transactions) and SUM (1.2M purchase summaries) with customer demographic and behavioral labels.
- Injected 1000 synthetic fraudulent transactions by assigning average behavioral profiles of one customer to another customer's transactions.
- Deep learning pipeline trained LSTM and MLP models to predict customer labels (e.g., total funds range) and computed Scale of Suspicious Transaction (SST) from ensemble misclassification consensus.

**Key Findings (selected):**
- "num: Deep learning LSTM achieved 92% accuracy predicting total funds range and 86% for age range."
- "num: Deep learning detected 788 of 1000 injected fraudulent transactions with 1340 false positives (0.007% misclassification rate)."
- "num: Real-time clustering detected 619 of 1000 injected frauds with 574 false positives (0.003% misclassification rate)."
- Real-time clustering had lower classification accuracy (e.g., 66% for total funds range) due to cold-start before building customer fingerprints.

**Limitations / Contradictions for Odin:**
- "Real-time clustering suffers from cold-start: initial customer fingerprints are incomplete, lowering early accuracy. [acknowledged]"
- "Dataset is proprietary and not publicly available. [unacknowledged]"
- "No comparison to existing production fraud detection systems or industry benchmarks. [unacknowledged]"

**Key takeaways:**
- "Deep learning LSTM achieved 92% accuracy predicting customer total funds range."
- "Real-time clustering detected 619 of 1000 frauds with only 574 false alarms."
- "Hybrid integration of batch and streaming methods is proposed as future direction."

---


## A Survey of Deep Anomaly Detection in Multivariate Time Series: Taxonomy, Applications, and Directions
**Filename:** `IA--Wang-et_al_summarized.md`  
**Authors:** Wang, F.; Jiang, Y.; Zhang, R.; Wei, A.; Xie, J.; Pang, X. (2025)  
**ID:** `10.3390/s25010190`  
**Odin Topics:** 6.A, 6.B, 8.A, 8.B, 12.A  

**TLDR:** A comprehensive survey categorizing deep learning methods for multivariate time series anomaly detection into forecasting, reconstruction, and contrastive approaches, with analysis of datasets and future directions.

**Problem & Motivation:** Traditional anomaly detection methods face limitations in handling high-dimensional multivariate time series with complex temporal and inter-variable dependencies. Deep learning offers powerful representation learning but lacks a structured taxonomy for multivariate time series anomaly detection. This survey addresses the gap by organizing recent deep learning methods and identifying open challenges.

**Approach (summary):**
- Conducted a structured review of deep learning for multivariate time series anomaly detection.
- Proposed a taxonomy based on learning paradigms (unsupervised, semi-supervised, self-supervised) and model architectures (CNN, RNN, GNN, Transformer, etc.).
- Organized methods into three strategies: forecasting-based, reconstruction-based, and contrastive-based.

**Key Findings (selected):**
- "num: 46 deep learning models are reviewed and categorized."
- Forecasting methods using Transformers outperform others in handling long-range dependencies.
- Reconstruction methods using VAEs and GANs struggle with subtle anomalies and mode collapse.
- Contrastive learning, especially with LLMs, shows promise for few-shot anomaly detection.

**Limitations / Contradictions for Odin:**
- "Focuses on general MTSAD without personal finance-specific validation [unacknowledged]."
- "Deep learning models require large training datasets, limiting applicability to users with sparse transaction history [unacknowledged]."
- "Evaluation metrics are not standardized across studies, making comparisons difficult (acknowledged as future direction)."

**Key takeaways:**
- "Survey reviews 46 deep learning models for multivariate time series anomaly detection."
- "Transformer-based methods outperform RNNs in capturing long-range temporal dependencies."
- "Contrastive learning and LLMs offer promising few-shot anomaly detection capabilities."

---


## Optimizing Business Decision-Making Through AI-Enhanced Business Intelligence Systems: A Systematic Review of Data-Driven Insights in Financial and Strategic Planning
**Filename:** `IA--Siddiqui_summarized.md`  
**Authors:** Siddiqui, N. A. (2025)  
**ID:** `10.71292/sdmi.v2i01.21`  
**Odin Topics:** 6.A, 6.B, 8.A, 8.B, 10.A, 10.B, 11.A, 11.B, 12.A, 12.B  

**TLDR:** AI-enhanced Business Intelligence systems improve financial forecasting accuracy by 32-45%, reduce fraudulent transactions by 47%, increase customer engagement by 38%, and optimize supply chain efficiency by 23%.

**Problem & Motivation:** Traditional BI systems struggle with real-time processing and unstructured data, limiting predictive capabilities. AI integration offers potential for improved decision-making but lacks systematic synthesis of its impact on financial and strategic planning.

**Approach (summary):**
- This systematic review follows PRISMA guidelines for transparent and rigorous literature analysis.
- Searched Scopus, Web of Science, IEEE Xplore, ScienceDirect, and Google Scholar for 2012-2024.
- Initial pool of 2,450 articles reduced to 98 high-quality peer-reviewed studies after screening.

**Key Findings (selected):**
- "num: 32-45% improvement in financial forecasting accuracy with AI-powered BI"
- "num: 47% decrease in fraudulent transactions and 60% reduction in false positives"
- "num: 38% increase in customer engagement and 22% improvement in conversion rates"
- "num: 23% increase in supply chain operational efficiency and 17% reduction in logistics costs"

**Limitations / Contradictions for Odin:**
- "Data governance complexities and integration issues hinder widespread AI-BI adoption."
- "Algorithmic transparency remains a challenge; many AI models operate as black boxes."
- "Bias in AI models due to skewed training data can reinforce discriminatory outcomes."

**Key takeaways:**
- "AI-enhanced BI improves forecasting accuracy by 32-45%."
- "Fraud detection reduces transactions by 47% with 60% fewer false positives."
- "Customer engagement increases by 38% using AI-driven segmentation."

---


## A comprehensive survey of deep learning for time series forecasting: architectural diversity and open challenges
**Filename:** `IA--Kim-et_al_summarized.md`  
**Authors:** Kim, J.; Kim, H.; Kim, H.; Lee, D.; Yoon, S. (2025)  
**ID:** `10.1007/s10462-025-11223-9`  
**Odin Topics:** 6.A, 6.B, 8.A, 8.B, 12.A, 12.B  

**TLDR:** A comprehensive survey of deep learning for time series forecasting covering MLPs, CNNs, RNNs, GNNs, Transformers, diffusion models, foundation models, and Mamba, with analysis of open challenges.

**Problem & Motivation:** Time series forecasting is critical for decision-making but faces challenges from data diversity and complexity. Existing surveys lack comprehensive coverage of recent architectural diversification and open challenges. This survey provides a timely synthesis of model evolution and persistent problems.

**Approach (summary):**
- Reviewed over 200 papers from top AI conferences and arXiv preprints.
- Categorized models by architecture: statistical, ML, fundamental DL, Transformer, non-Transformer, diffusion, foundation, Mamba.
- Analyzed open challenges: channel dependency, distribution shift, causality, feature extraction, interpretability, and spatio-temporal forecasting.

**Key Findings (selected):**
- The number of top-tier AI conference papers on time series forecasting has exploded in recent years.
- num: Simple linear models (LTSF-Linear) can outperform Transformers on long-term forecasting.
- Patching technique (PatchTST) enables Transformers to achieve state-of-the-art by preserving locality.
- Channel independence (CI) strategy shows greater robustness to distribution shift than channel dependence (CD).

**Limitations / Contradictions for Odin:**
- "Skipped detailed theoretical backgrounds of models. [unacknowledged]"
- "Left specific differences in characteristics across time series datasets for future work."
- "AGI and adaptive modeling (meta-learning, reinforcement learning) could be further explored."

**Key takeaways:**
- "Simple linear models can outperform complex Transformers for time series forecasting."
- "Patching time series into 64-length patches improves Transformer performance."
- "Channel independence is more robust to distribution shifts than channel dependence."

---


## Time-Series Forecasting Using Deep Learning and Data Mining Models
**Filename:** `IA--Scrivano_summarized.md`  
**Authors:** Scrivano, A. (2025)  
**ID:** `c3d5e7f9-1a2b-3c4d-5e6f-7a8b9c0d1e2f`  
**Odin Topics:** 6.B, 8.B, 12.B  

**TLDR:** A review comparing traditional statistical, deep learning (RNN, LSTM, CNN, Transformer), and data mining models for time-series forecasting, finding Transformers and Gradient Boosting Machines achieve superior accuracy across finance, energy, and retail domains.

**Problem & Motivation:** Traditional time-series models like ARIMA fail to capture non-linear dynamics and complex patterns in real-world data. Deep learning and data mining methods offer improved accuracy but require systematic evaluation across domains. This review synthesizes current methodologies to guide model selection.

**Approach (summary):**
- Data collected from stock exchanges, meteorological records, smart grids, and retail transactions.
- Preprocessing included differencing, smoothing, log transforms, feature extraction (lagged variables, moving averages), and normalization.
- Model selection based on task: RNN/LSTM for temporal dependencies, CNN/TCN for spatial hierarchies, Transformers for attention-based long-range dependencies.

**Key Findings (selected):**
- "num: LSTM achieved 15% reduction in MAE over conventional methods in web traffic prediction."
- "num: TCN attained 20% higher accuracy in early-stage anomaly detection compared to traditional methods."
- "num: Transformer reduced MSE by 12% and MAE by 17% over recurrent and convolutional models in retail."
- "num: Gradient Boosting Machine outperformed Random Forest with MAE of 170 vs 185 in energy dataset."

**Limitations / Contradictions for Odin:**
- "The review lacks specific guidance for personal finance domains; results are from aggregate datasets not individual-level transactions."
- "Computational constraints of Transformers may limit deployment on mobile devices [unacknowledged]."
- "Generalizability to Filipino financial behaviors and spending patterns is untested [unacknowledged]."

**Key takeaways:**
- "Transformers achieve 12-17% lower forecast errors than recurrent models."
- "Gradient Boosting Machines offer strong accuracy with lower computational cost."
- "Probabilistic forecasting quantifies uncertainty essential for risk-aware decisions."

---


## A Review of Time Series Prediction Models Based on Deep Learning
**Filename:** `IA--Ao-et_al_summarized.md`  
**Authors:** Ao, X.; Gong, Y.; He, A. (2025)  
**ID:** `10.1109/ACCESS.2025.3602791`  
**Odin Topics:** 6.A, 6.B, 8.A, 8.B, 12.A, 12.B  

**TLDR:** Reviews deep learning models for time series prediction, including CNNs, RNNs/LSTM/GRU, Transformers, GNNs, and hybrids, with a task-driven model selection framework.

**Problem & Motivation:** Traditional time series methods like ARIMA struggle with nonlinear, non-stationary, and seasonal real-world data. Deep learning offers powerful nonlinear modeling and automatic feature extraction, but existing surveys lack practical model selection guidelines, deep cross-comparisons, and systematic coverage of emerging challenges like interpretability and efficiency.

**Approach (summary):**
- Systematically analyzes CNN-based models (TCN, SCINet, Kmeans-CNN) and their trade-offs in long-range dependency capture versus computational cost.
- Reviews RNN family (vanilla RNN, LSTM, GRU) focusing on gating mechanisms that solve vanishing gradients for long sequences.
- Examines Transformer variants (Informer, Autoformer, iTransformer, Conformer, Scaleformer, CrossFormer) with emphasis on self-attention complexity and efficiency innovations.

**Key Findings (selected):**
- num: ARIMA-RNN hybrid achieved 15% MAE reduction on electricity load dataset compared to standalone models.
- num: ETSformer reduced inference latency by 37% versus Autoformer on ETT data while maintaining accuracy.
- num: PatchTST achieved 23% lower MSE than Informer with 60% less GPU memory consumption.
- Transformer variants with ProbSparse attention (Informer) reduce time complexity from O(L^2) to O(L log L).

**Limitations / Contradictions for Odin:**
- The paper is a survey, not an empirical study; claims about model performance are aggregated from cited primary research.
- Comparative tables lack statistical significance testing across different datasets. [unacknowledged]
- Real-time performance metrics are discussed qualitatively without standardized benchmarks. [unacknowledged]

**Key takeaways:**
- LSTM and GRU solve vanishing gradients for medium-length sequence forecasting.
- Transformer variants achieve O(L log L) complexity for sequences over 1000 steps.
- PatchTST reduces GPU memory by 60% via sub-series tokenization.

---


## Machine Learning Methods in Customer Segmentation and Recommendation Systems
**Filename:** `IA--Guo_summarized.md`  
**Authors:** Guo, Y. (2025)  
**ID:** `10.1051/shsconf/202521802012`  
**Odin Topics:** 5.B, 8.A, 8.B  

**TLDR:** Reviews machine learning methods for customer segmentation and recommendation systems, comparing collaborative filtering, content-based filtering, and hybrid models with case studies from e-commerce, banking, and healthcare.

**Problem & Motivation:** Traditional customer segmentation using demographics fails to handle modern dataset complexity and scale. Machine learning offers scalable, automated solutions but faces challenges like cold start, data quality, and privacy. There is a need to compare methods and identify best practices across industries.

**Approach (summary):**
- Reviews traditional segmentation (demographic/geographic) and its limitations.
- Compares K-means clustering, DBSCAN, and PCA for customer segmentation with trade-offs.
- Evaluates collaborative filtering (user-based and item-based) and its cold start and scalability issues.

**Key Findings (selected):**
- "num: DBSCAN improves recommendation accuracy by 12% compared to K-means in handling noisy data."
- "num: PCA reduces noise and improves anomaly detection accuracy by 15% in banking fraud detection."
- "num: Patient classification accuracy improved by 18% using DBSCAN in noisy healthcare datasets."
- Collaborative filtering suffers from cold start and scalability issues with large user-item matrices.

**Limitations / Contradictions for Odin:**
- "Data quality issues (incomplete, noisy, biased data) can lead to poor model performance. [acknowledged]"
- "Privacy risks, exemplified by the 2017 Equifax breach, require stronger encryption and protection. [acknowledged]"
- "Bias in training datasets can produce unfair recommendations; paper calls for bias-detection algorithms. [acknowledged]"

**Key takeaways:**
- Collaborative filtering requires interaction history, causing cold start problems.
- DBSCAN handles noisy data and outperforms K-means by 12% for recommendations.
- PCA improves anomaly detection accuracy by 15% in banking fraud detection.

---


## An Introduction to Machine Learning Methods for Fraud Detection
**Filename:** `IA--Compagnino-et_al_summarized.md`  
**Authors:** Compagnino, A. A.; Maruccia, Y.; Cavuoti, S.; Riccio, G.; Tutone, A.; Crupi, R.; Pagliaro, A. (2025)  
**ID:** `10.3390/app15211787`  
**Odin Topics:** 8.A, 8.B, 12.A, 12.B, 10.A, 10.B  

**TLDR:** Reviews machine learning for financial fraud detection, covering supervised, unsupervised, and deep learning approaches, datasets, performance metrics, and case studies highlighting class imbalance and recall challenges.

**Problem & Motivation:** Financial fraud causes severe economic and social damage, with 56% of companies experiencing fraud. Traditional detection methods are increasingly inadequate against evolving fraudulent activities. A systematic analysis of ML techniques bridging academic research and operational reality is missing.

**Approach (summary):**
- Systematic literature search across Scopus, IEEE Xplore, ACM Digital Library, and Web of Science for articles published 2014-2023.
- Classification of fraud types into external (credit card, loan, insurance) and internal (financial statement, money laundering, tax, asset misappropriation).
- Review of supervised methods (Random Forest, XGBoost, SVM, etc.), unsupervised methods (Isolation Forest, Autoencoders, K-Means), and deep learning (LSTM, CNN, RNN, GAN).

**Key Findings (selected):**
- "num: Random Forest achieved AUPRC of 0.619 on banking test set (prevalence 2.37%) but fraud recall was only 0.34."
- "num: XGBoost on ULB2013 dataset achieved AUPRC of 0.867, outperforming Logistic Regression (0.724) and KNN (0.585)."
- "num: Class_weight='balanced' and 'balanced_subsample' did not improve recall (stuck at 0.36) compared to default on bank transfer dataset."
- "num: Recall@0.5% for Random Forest was 0.202, capturing about 24 of 119 frauds when screening top 0.5% of transactions."

**Limitations / Contradictions for Odin:**
- "The review does not propose a novel algorithm or system, only synthesizes existing literature."
- "Case studies use tree-based ensembles only; deep learning and hybrid methods were not empirically tested. [unacknowledged]"
- "The low recall achieved (0.34-0.36) suggests standard supervised models are insufficient, but the paper does not implement or evaluate the recommended hybrid solutions."

**Key takeaways:**
- "Random Forest achieved AUPRC 0.619 but fraud recall only 0.34 on real banking data."
- "Class_weight adjustments did not improve recall beyond 0.36 in imbalanced fraud detection."
- "AUPRC is preferred over ROC for evaluating models on imbalanced datasets."

---


## Long Short-Term Memory Networks: A Comprehensive Survey
**Filename:** `IA--Krichen-&-Mihoub_summarized.md`  
**Authors:** Krichen, M.; Mihoub, A. (2025)  
**ID:** `10.3390/ai6090215`  
**Odin Topics:** 6.A, 6.B, 8.A, 8.B, 12.B  

**TLDR:** LSTM networks capture long-range dependencies in sequential data via memory cells and gating mechanisms, overcoming RNN vanishing gradient limitations.

**Problem & Motivation:** Traditional RNNs suffer from vanishing gradients, making long-range dependency learning difficult. LSTM was designed to retain information over extended sequences. This gap limits performance in tasks like language modeling, time series forecasting, and speech recognition.

**Approach (summary):**
- The survey uses a narrative review approach synthesizing LSTM literature across NLP, time series, and speech domains.
- Core LSTM components: cell state, hidden state, and input/forget/output gates with sigmoid and tanh activations.
- Variants covered: Bidirectional LSTM (forward+backward context), Stacked LSTM (multiple layers), and Attention Mechanisms.

**Key Findings (selected):**
- LSTM mitigates vanishing gradient, enabling long-term memory retention vs. standard RNN.
- num: Bidirectional LSTM achieves over 90% accuracy in 60-minute traffic speed prediction.
- num: Stacked LSTM for bearing fault diagnosis achieves over 99% accuracy from raw signals.
- Attention-augmented LSTM improves stock price prediction and load forecasting over plain LSTM.

**Limitations / Contradictions for Odin:**
- "High computational complexity requires significant GPU/TPU resources [unacknowledged for small-scale PFMS]."
- "LSTMs need large labeled datasets; overfits when data is scarce. [acknowledged]"
- "Long training times and sensitive hyperparameters hinder rapid prototyping. [acknowledged]"

**Key takeaways:**
- "LSTM uses forget, input, and output gates to control information flow over time."
- "Bidirectional LSTM achieves over 90% accuracy for 60-minute traffic prediction."
- "Stacked LSTM reaches 99% fault diagnosis accuracy from raw sensor signals."

---


## A Review of Anomaly Identification in Finance Frauds Using Machine Learning Systems
**Filename:** `IA--Majumder_summarized.md`  
**Authors:** Majumder, R. Q. (2025)  
**ID:** `10.48175/IJARSCT-25619`  
**Odin Topics:** 4.B, 8.A, 8.B  

**TLDR:** A review of machine learning methods for financial fraud detection, covering supervised, unsupervised, and graph-based techniques, and highlighting challenges like imbalanced data and adversarial attacks.

**Problem & Motivation:** Traditional fraud detection methods lack adaptability to evolving fraudulent techniques, causing significant economic losses. Machine learning offers improved detection but faces challenges in imbalanced data, interpretability, and real-time processing. This gap motivates the need for a systematic review of ML approaches for financial fraud.

**Approach (summary):**
- Conducts a literature review of ML-based anomaly detection for financial fraud.
- Covers supervised, semi-supervised, and unsupervised learning methods.
- Examines algorithms including logistic regression, SVM, decision trees, random forest, KNN, and autoencoders.

**Key Findings (selected):**
- "num: Fraud detection models using deep learning and GNNs outperform traditional ML on complex fraud patterns."
- "num: Autoencoder-based anomaly detection with XGBoost achieves effective fraud classification."
- "num: Training on over 12 million records with IF, LOF, and AE enables anomaly alerts before transaction confirmation."
- Unsupervised methods like Isolation Forest and autoencoders can detect new fraud patterns without labeled data.

**Limitations / Contradictions for Odin:**
- "Review does not include empirical benchmarks comparing algorithm performance. [unacknowledged]"
- "Lacks discussion of computational cost for real-time deployment on mobile devices. [unacknowledged]"
- "Privacy-preserving techniques like federated learning are mentioned as future work but not evaluated. [unacknowledged]"

**Key takeaways:**
- "Deep learning and GNNs outperform traditional ML on complex fraud patterns."
- "Imbalanced data and adversarial attacks are major challenges for detection systems."
- "Unsupervised methods like autoencoders work without labeled fraud data."

---


## "Recurrent Neural Networks: A Comprehensive Review of Architectures, Variants, and Applications"
**Filename:** `IA--Mienye-et_al-2024_summarized.md`  
**Authors:** "Mienye, I. D.; Swart, T. G.; Obaido, G." (2024)  
**ID:** `10.3390/info15090517`  
**Odin Topics:** 3.A, 6.A, 6.B, 8.A, 8.B, 12.B  

**TLDR:** "Recurrent neural networks and their variants enable effective processing of sequential data for applications including time series forecasting, anomaly detection, and natural language processing."

**Problem & Motivation:** "Previous reviews of RNNs do not fully capture the latest advancements in architectures and applications across a broad range of fields. A comprehensive review is needed to assess theoretical advancements and practical implementations to help shape future research."

**Approach (summary):**
- "Surveys foundational RNN architectures including basic RNN, LSTM, and GRU."
- "Reviews advanced variants such as bidirectional LSTM, peephole LSTM, echo state networks, and independently recurrent neural networks."
- "Examines hybrid models combining RNNs with CNNs, attention mechanisms, and transformers."

**Key Findings (selected):**
- "num: LSTM and GRU effectively mitigate vanishing gradient problems in sequential modeling."
- "num: Bidirectional RNNs improve context understanding by processing sequences in both directions."
- "Hybrid CNN-RNN models outperform standalone RNNs in video analysis and time series forecasting."
- "Attention mechanisms integrated with RNNs enhance long-range dependency modeling."

**Limitations / Contradictions for Odin:**
- "Training RNNs on long sequences remains computationally intensive compared to transformer architectures."
- "RNNs are often perceived as black-box models with limited interpretability, a challenge acknowledged but not solved."
- "Bias in training data can lead to unfair predictions; the review notes this but offers no mitigation for financial applications."

**Key takeaways:**
- "LSTM and GRU solve vanishing gradient problems in sequential data."
- "Bidirectional processing captures both past and future context."
- "Hybrid CNN-RNN models excel at spatiotemporal forecasting."

---


## ENHANCING FINANCIAL SERVICES THROUGH BIG DATA AND AI-DRIVEN CUSTOMER INSIGHTS AND RISK ANALYSIS
**Filename:** `IA--Yang-et_al_summarized.md`  
**Authors:** Yang, T.; Xin, Q.; Zhan, X.; Zhuang, S.; Li, H. (2024)  
**ID:** `10.60087/jklst.vol3.n3.p53-62`  
**Odin Topics:** 5.A, 5.C, 6.A, 8.A, 8.B, 11.A, 11.B, 12.A, 12.B  

**TLDR:** Supervised learning with XGBoost and face recognition enables customer profiling, profit prediction, fraud detection, and churn analysis in financial services.

**Problem & Motivation:** Financial institutions need accurate customer identification and risk analysis to improve loan approval and risk management. Traditional statistical models struggle with massive data and complex financial behaviors. Machine learning offers advantages in processing large datasets and discovering hidden patterns.

**Approach (summary):**
- Constructed six feature systems from customer attributes, debit/credit card transactions, loan applications, trends, and page visit behavior.
- Used supervised learning as basis for AI pricing model to combine man-machine decision making.
- Applied XGBoost for profit modeling at account level, modeling revenue, default probabilities, and loss rates.

**Key Findings (selected):**
- "num: Profit quartile spread across risk ranges increases with risk level, indicating challenge in high-risk areas."
- "num: Learning rate limited to 0.001-0.01 with thousands of trees to prevent overfitting."
- Revenue model and total profit model show poor forecasting performance but better ranking performance.
- Hump-shaped relationship between profit component and risk is retained between predicted and actual curves.

**Limitations / Contradictions for Odin:**
- "Model performance is poor for revenue and total profit forecasting at high risk levels."
- "No discussion of data privacy implications for customer profiling. [unacknowledged]"
- "Lacks validation on non-US or Filipino demographic data. [unacknowledged]"

**Key takeaways:**
- XGBoost profit models outperform risk-only models in ranking profitability.
- Profit and risk have a non-monotonic hump-shaped relationship.
- Community discovery algorithms effectively detect gang fraud in credit data.

---


## Evolving Strategies in Machine Learning: A Systematic Review of Concept Drift Detection
**Filename:** `IA--Hovakimyan-&-Bravo_summarized.md`  
**Authors:** Hovakimyan, G.; Bravo, J.M. (2024)  
**ID:** `10.3390/info15120786`  
**Odin Topics:** 5.B, 5.C, 6.A, 6.B, 8.A, 8.B, 12.A, 12.B  

**TLDR:** A systematic review of concept drift detection methods categorizes them into DDMs, WBMs, USSMs, ensembles, and neural networks, highlighting trade-offs between accuracy and computational cost.

**Problem & Motivation:** Machine learning models typically assume static data distributions, but real-world streams undergo concept drift, causing performance degradation. This affects domains like fraud detection, finance, healthcare, and recommendation systems. A comprehensive, up-to-date synthesis of drift detection methodologies was missing to guide researchers and practitioners.

**Approach (summary):**
- PRISMA guidelines used to screen 490 studies from IEEE and ScienceDirect APIs, narrowing to 65 high-impact papers.
- T5 NLP model applied to summarize abstracts for efficient screening and data extraction.
- Quality assessment using adapted Newcastle-Ottawa Scale and CASP checklists, rating studies on methodology, validation, and reproducibility.

**Key Findings (selected):**
- "num: 45% of studies were high quality (score 4-5), 41% moderate, 14% low."
- "DDMs offer high accuracy with low computational cost, suitable for real-time applications."
- "Ensemble methods and neural networks provide very high accuracy but at high computational cost."
- "Window-based methods balance accuracy and efficiency, effective for streaming environments."

**Limitations / Contradictions for Odin:**
- "Handling imbalanced data in streaming environments remains a significant challenge."
- "Computational efficiency of ensembles and neural networks limits real-time deployment."
- "Application of drift detection to non-tabular data (images, complex time-series) is underexplored."

**Key takeaways:**
- "45% of reviewed drift detection studies were high quality."
- "Ensembles and neural networks offer highest accuracy but high cost."
- "Window-based methods balance accuracy and efficiency for streams."

---


## Exploring Machine Learning for Credit Card Fraud Detection from a Philippine Perspective
**Filename:** `LA--Blancaflor-et_al_summarized.md`  
**Authors:** Blancaflor, E.; Asuncion, K. D.; Reyes, H. J.; Verzosa, M. (2024)  
**ID:** `10.1145/3698062.3698088`  
**Odin Topics:** 8.A, 8.B, 12.B  

**TLDR:** Evaluates machine learning models (SVM, ANN, k-NN, Naive Bayes, logistic regression) for credit card fraud detection in the Philippines, finding ANN achieves up to 98.44% accuracy.

**Problem & Motivation:** Credit card fraud in the Philippines increased 21% since COVID-19, with traditional fraud prevention systems inadequate due to large data volumes, imbalanced distributions, concept drift, and real-time detection needs. There is a need to customize machine learning algorithms to the Philippine economic, technological, and social context to improve fraud detection effectiveness.

**Approach (summary):**
- Data source: credit card transaction data from the Philippines (dataset size not specified).
- Methods evaluated: logistic regression, k-Nearest Neighbors, Naive Bayes, Support Vector Machines, and Artificial Neural Networks with GA and SMOTE enhancements.
- Evaluation metrics: accuracy, sensitivity, specificity, precision, Matthews Correlation Coefficient, and balanced classification rate.

**Key Findings (selected):**
- "num: ANN-SMOTE achieved the best performance with up to 98.44% accuracy."
- "num: k-NN achieved 97.69% accuracy and Naive Bayes 97.92% accuracy."
- "num: Logistic regression had the lowest accuracy at 54.86%."
- A trade-off exists between model accuracy and explainability; logistic regression is better for regulatory compliance.

**Limitations / Contradictions for Odin:**
- "No explicit dataset size or transaction volume provided. [unacknowledged]"
- "All reported accuracies are from cited secondary sources, not original experiments. [unacknowledged]"
- "Real-time detection challenges mentioned but no latency or throughput benchmarks given."

**Key takeaways:**
- "ANN-SMOTE achieves 98.44% accuracy for fraud detection."
- "Imbalanced data handling is critical for anomaly detection."
- "Explainability trade-off matters for regulatory compliance."

---


## Optimizing Recurrent Neural Networks: A Study on Gradient Normalization of Weights for Enhanced Training Efficiency
**Filename:** `IA--Wu_X.-et_al_summarized.md`  
**Authors:** Wu, X.; Xiang, B.; Lu, H.; Li, C.; Huang, X.; Huang, W. (2024)  
**ID:** `10.3390/app14156578`  
**Odin Topics:** 6.A, 6.B, 8.B, 12.B  

**TLDR:** Weight gradient normalization (WGN) stabilizes RNN training by normalizing gradient mean and variance, reducing vanishing/exploding gradients and improving convergence.

**Problem & Motivation:** RNNs suffer from vanishing and exploding gradients due to recurrent weight reuse and activation saturation. Existing solutions like gradient clipping or batch normalization have limitations such as slow convergence or complex tuning. A statistically principled method that normalizes weight gradients is missing.

**Approach (summary):**
- Uses Simple-RNN and LSTM models with tanh or ReLU activation on MNIST, PTB, ETTm1, and UCR datasets.
- Normalizes gradients per iteration: (grad - mean) / (std + δ) before weight update.
- Compares against standard SGD with fixed learning rates, also gradient clipping and GRU in appendix.

**Key Findings (selected):**
- "num: WGN reduces perplexity on PTB from 125.27 to 110.89 (11.48% improvement) for 2-layer LSTM."
- "num: On ETTm1, MAE at 24-step prediction improves from 0.802 to 0.778 (3.00%) for 1-layer LSTM."
- "num: MAE at 96-step prediction improves from 0.635 to 0.592 (6.77%) for 1-layer RNN."
- "num: On MNIST, 2-layer LSTM with WGN achieves 99.11% accuracy vs 98.42% without."

**Limitations / Contradictions for Odin:**
- "WGN may not improve accuracy for shallow RNN architectures."
- "Small dataset performance can degrade due to incomplete batch sampling."
- "Computational overhead (7-8x SGD) limits real-time deployment."

**Key takeaways:**
- "Weight gradient normalization reduces gradient problems and accelerates convergence."
- "WGN improves perplexity by 11.48% on language modeling tasks."
- "The method is sensitive to learning rate; optimal η between 0.0001 and 0.005."

---


## Recommendation system for financial decision-making using Artificial intelligence
**Filename:** `IA--Shuryhin-&-Zinovatna_summarized.md`  
**Authors:** Shuryhin, K. A.; Zinovatna, S. L. (2024)  
**ID:** `10.15276/aait.07.2024.24`  
**Odin Topics:** 2.C, 6.A, 6.B, 7.B, 7.C, 8.A, 8.B, 10.A, 10.B  

**TLDR:** Combines Isolation Forest for anomaly detection, ARIMA and LSTM for budget forecasting, and large language models to generate personalized financial recommendations while addressing ethical concerns like privacy and user autonomy.

**Problem & Motivation:** Cognitive biases lead to irrational financial decisions, and AI-enhanced marketing can manipulate consumer behavior. Existing recommendation systems in finance often lack personalization, fail to account for user autonomy, or ignore ethical considerations. There is a need for an intelligent system that provides unbiased, personalized financial advice without manipulation.

**Approach (summary):**
- Input data includes user transaction history, spending anomalies, budget forecasts, and user parameters like risk tolerance and financial goals.
- Isolation Forest isolates anomalies by building binary trees and calculating path lengths; anomaly score near 1 indicates anomalous expense.
- ARIMA(p,d,q) models short-term dependencies with autoregressive and moving average components after differencing for stationarity.

**Key Findings (selected):**
- Isolation Forest effectively identifies atypical financial actions by isolating deviations from normal spending patterns.
- Combining ARIMA (short-term) and LSTM (long-term) improves budget forecast stability and accuracy.
- LLM-generated recommendations adapt to different income levels and user-specific risk levels, goals, and preferences.
- The system promotes responsible financial behavior without imposing decisions, enhancing user awareness and autonomy.

**Limitations / Contradictions for Odin:**
- No quantitative validation of forecasting or anomaly detection accuracy. [unacknowledged]
- The system's LLM component is described only conceptually; no ablation study or comparison with rule-based baselines. [unacknowledged]
- Ethical claims are not operationalized or measured (e.g., how to verify user autonomy). [unacknowledged]

**Key takeaways:**
- Anomaly detection uses Isolation Forest with path length scoring.
- Forecasts combine ARIMA for short-term and LSTM for long-term trends.
- Large language model generates personalized financial advice from transaction and forecast data.

---


## Recurrent Neural Networks (RNNs): Architectures, Training Tricks, and Introduction to Influential Research
**Filename:** `IA--Das-et_al_summarized.md`  
**Authors:** Das, S.; Tariq, A.; Santos, T.; Kantareddy, S. S.; Banerjee, I. (2023)  
**ID:** `10.1007/978-1-0716-3195-9_4`  
**Odin Topics:** 6.A, 6.B, 8.A, 8.B  

**TLDR:** Recurrent neural networks including LSTM, GRU, bidirectional, deep RNNs, and attention mechanisms process sequential data for tasks like language modeling and time-series analysis.

**Problem & Motivation:** Standard feedforward networks cannot handle sequential dependencies because they treat each input independently. RNNs address this with recurrent connections but suffer from vanishing or exploding gradients, limiting their ability to capture long-term dependencies. Gated architectures like LSTM and GRU were introduced to mitigate these issues.

**Approach (summary):**
- Introduces six RNN architectures: SimpleRNN, LSTM, GRU, bidirectional RNN, deep RNN, and attention-based Transformers.
- Describes training challenges including vanishing and exploding gradients, then presents skip connections, leaky units, and gradient clipping as solutions.
- Surveys applications in language modeling: text classification with many-to-one RNNs, extractive and abstractive summarization, neural machine translation with encoder-decoder, and image-to-text translation with attention.

**Key Findings (selected):**
- LSTM uses three gates (input, forget, output) to control information flow through a cell state.
- GRU uses two gates (reset and update), reducing computational cost compared to LSTM while handling long-term dependencies.
- Attention mechanisms allow models to focus on relevant parts of the input sequence, improving translation and captioning performance.
- Skip connections preserve gradients via additive or concatenative paths, helping deeper RNN training.

**Limitations / Contradictions for Odin:**
- "Paper is a survey; no empirical validation on financial data [unacknowledged]."
- "Does not compare RNN performance on spending datasets [unacknowledged]."
- "Training tricks are discussed generically without personal finance context [unacknowledged]."

**Key takeaways:**
- LSTM uses three gates to control long-term memory flow.
- GRU has two gates, making it computationally lighter than LSTM.
- Attention mechanisms enable sequence models to focus on relevant input parts.

---


## MACHINE LEARNING FOR FRAUD DETECTION IN DIGITAL BANKING: A SYSTEMATIC LITERATURE REVIEW
**Filename:** `IA--George-et_al_summarized.md`  
**Authors:** George, M. Z. H.; Alam, M. K.; Hasan, M. T. (2023)  
**ID:** `10.63125/913ksy63`  
**Odin Topics:** 8.A, 8.B, 12.A, 12.B  

**TLDR:** Supervised learning dominates digital banking fraud detection, but deep learning, anomaly detection, and hybrid models show superior adaptability for imbalanced transaction data.

**Problem & Motivation:** Rule-based fraud detection systems are rigid and unable to adapt to evolving fraud tactics in digital banking. Machine learning offers scalability and predictive accuracy, yet prior reviews lack integration of deep learning, hybrid models, and cross-regional comparisons. A systematic synthesis is needed to consolidate fragmented evidence across methodological and regulatory contexts.

**Approach (summary):**
- The study followed PRISMA guidelines for systematic literature review, covering Scopus, Web of Science, IEEE Xplore, ACM Digital Library, and SSRN.
- Search terms combined machine learning, fraud detection, digital banking, anomaly detection, and deep learning with Boolean operators.
- Initial identification yielded 2,346 records; after deduplication, screening, and eligibility review, 118 studies were included.

**Key Findings (selected):**
- num: 36 supervised learning studies accumulated over 9,200 citations, confirming dominance of decision trees, logistic regression, and SVMs.
- num: 27 unsupervised learning studies received over 6,800 citations, essential for detecting novel fraud patterns without labels.
- num: 21 deep learning studies (RNNs, CNNs, autoencoders) garnered over 7,300 citations, enabling sequential transaction modeling.
- num: 19 hybrid model studies exceeded 5,600 citations, demonstrating superior precision‑recall balance and adaptability.

**Limitations / Contradictions for Odin:**
- Extreme class imbalance handling remains uneven; many studies report results without calibrated costs.
- ROC‑AUC persists as a headline metric even when PR‑AUC is more decision‑relevant for skewed data.
- Reproducibility constrained by private datasets; few studies release code or standardized benchmarks. [unacknowledged]

**Key takeaways:**
- Supervised learning accounts for 36 of 118 reviewed studies.
- Deep learning models exceed 7,300 citations despite recent publication.
- Hybrid models outperform single‑paradigm detectors in precision‑recall balance.

---


## Transformer Architectures in Time Series Analysis: A Review
**Filename:** `IA--Thundiyil_summarized.md`  
**Authors:** Thundiyil, S.; Picone, J.; McKenzie, S. (2023)  
**ID:** `d8c5e6f1-3a2b-4c7d-9e0f-1a2b3c4d5e6f`  
**Odin Topics:** 6.A, 6.B, 8.A, 8.B, 12.A, 12.B  

**TLDR:** Reviews transformer architectures for time series forecasting, classification, and anomaly detection, comparing traditional and modern methods with emphasis on long-term dependencies.

**Problem & Motivation:** Traditional time series methods like ARIMA and RNNs struggle with long-term dependencies. Transformers offer self-attention to capture extended context, but require adaptation for time series data. This review synthesizes advances in transformer variants for forecasting and anomaly detection.

**Approach (summary):**
- Reviews 11 transformer-based architectures including LogTrans, Informer, Autoformer, and FEDformer.
- Compares traditional methods (AR, MA, ARIMA, spectral analysis) with modern deep learning approaches.
- Describes key innovations: ProbSparse attention, autocorrelation mechanism, pyramidal attention, and frequency decomposition.

**Key Findings (selected):**
- "num: Autoformer achieved a 38% average MSE reduction over existing methods on six benchmarks."
- "num: FEDformer yielded a 14.8% relative MSE reduction compared to Autoformer, and over 20% on Exchange and ILI."
- "num: InParformer achieved MSE 0.260 and MAE 0.323 on ETTm2 for prediction length 192."
- "num: Pyraformer reduced MSE by 24.8%, 28.9%, 26.2% on ETTh1 for prediction lengths 168, 336, 720 respectively."

**Limitations / Contradictions for Odin:**
- "No empirical validation on personal finance datasets. [unacknowledged]"
- "Does not address real-time inference constraints for mobile deployment. [unacknowledged]"
- "Review lacks discussion of privacy-preserving forecasting techniques. [unacknowledged]"

**Key takeaways:**
- "Transformers outperform RNNs for long-term forecasting tasks."
- "Autoformer yields 38% average MSE reduction across six benchmarks."
- "Self-attention enables modeling of extended temporal dependencies without recurrence."

---


## A Review of ARIMA vs. Machine Learning Approaches for Time Series Forecasting in Data Driven Networks
**Filename:** `IA--Kontopoulou-et_al_summarized.md`  
**Authors:** Kontopoulou, V. I.; Panagopoulos, A. D.; Kakkos, I.; Matsopoulos, G. K. (2023)  
**ID:** `10.3390/fi15080255`  
**Odin Topics:** 6.A, 6.B, 7.A, 7.B, 8.A, 8.B, 12.A, 12.B  

**TLDR:** A review comparing ARIMA statistical models with machine learning and hybrid approaches for time series forecasting across finance, health, weather, utilities, and network applications.

**Problem & Motivation:** The scientific literature lacks an extensive summary comparing ARIMA with machine learning and deep learning time series forecasting methods. Although machine learning models are increasingly used, their claimed superiority over classical statistical methods is not always systematically evaluated. This review addresses that gap by synthesizing comparative studies across multiple application domains.

**Approach (summary):**
- Reviewed published literature comparing ARIMA with SVM, decision tree, deep learning (LSTM, GRU, CNN), and hybrid models.
- Organized findings by application domain: finance (bitcoin, stocks), healthcare (COVID-19 cases), weather (wind, drought), utilities (energy, water), and network traffic.
- Extracted performance metrics including RMSE, MAPE, MAE, MSE, R2, NSE from each comparative study.

**Key Findings (selected):**
- Machine learning and deep learning models generally outperform ARIMA in time series forecasting across most applications reviewed.
- num: Deep learning models (LSTM, GRU) achieved RMSE values up to 40 times smaller than ARIMA for COVID-19 case forecasting in several countries (Arun Kumar et al., 2022).
- num: ARIMA outperforms machine learning models for small datasets, limited value ranges, or strongly linear and seasonal univariate series (e.g., drought forecasting with R2 >0.9 vs. SVM's 0.83).
- Hybrid models combining ARIMA with machine learning (e.g., ARIMA-SVM, ARIMA-NARNN, ARIMA-CNN) consistently outperform both individual approaches.

**Limitations / Contradictions for Odin:**
- ARIMA parameter selection depends on forecaster skill and experience.
- Machine learning models require large datasets and higher computational resources. [unacknowledged]
- Review does not cover real-time forecasting requirements for mobile personal finance applications. [unacknowledged]

**Key takeaways:**
- Machine learning outperforms ARIMA for most non-linear time series.
- Hybrid ARIMA-ML models always beat either method alone.
- ARIMA works best for small, linear, or seasonal univariate data.

---


## Continual Deep Learning for Time Series Modeling
**Filename:** `IA--Ao-&-Fayek_summarized.md`  
**Authors:** Ao, S.-I.; Fayek, H. (2023)  
**ID:** `10.3390/s23167167`  
**Odin Topics:** 6.A, 6.B, 8.A, 8.B, 12.A, 12.B  

**TLDR:** Surveys deep learning for sensor time series, highlighting non-stationarity challenges and continual learning methods to mitigate catastrophic forgetting.

**Problem & Motivation:** Real-world time series often exhibit non-stationary distributions, causing deep learning models to suffer catastrophic forgetting. Traditional methods assume stationarity, limiting deployment in dynamic environments. This survey identifies the gap in applying continual learning to time series forecasting and anomaly detection.

**Approach (summary):**
- Conducts systematic review of deep learning for sensor time series from 2018-2023.
- Categorizes methods into deep learning architectures (MLP, RNN, LSTM, CNN, GNN) and preprocessing techniques.
- Evaluates continual learning approaches (regularization, replay, parameter isolation) for time series tasks.

**Key Findings (selected):**
- "num: CNN with direct multi-step procedure improved prediction accuracy by 22.6% over seasonal ARIMAX for building load forecasting."
- "num: Graph Deviation Network achieved 54% better F-measure than the next best baseline for anomaly detection in water treatment systems."
- "num: LSTM achieved mean absolute percentage error of 4.82% for traffic flow forecasting versus 20.97% for ARIMA and 9.06% for BPNN."
- "num: Empirical mode decomposition preprocessing improved gesture classification accuracy from 94.22% to 99.73% using CNN."

**Limitations / Contradictions for Odin:**
- "Survey primarily synthesizes existing literature without new empirical experiments. [unacknowledged]"
- "Focus on sensor time series limits generalizability to financial transaction sequences. [unacknowledged]"
- "Computational cost of continual learning on mobile devices is not quantitatively assessed. [unacknowledged]"

**Key takeaways:**
- "LSTM achieved 4.82% MAPE for traffic forecasting versus 20.97% for ARIMA."
- "Empirical mode decomposition preprocessing raised accuracy from 94.22% to 99.73%."
- "No single deep learning method works for all anomaly detection tasks."

---


## Rare Category Analysis for Complex Data: A Review
**Filename:** `IA--Zhou-&-He_summarized.md`  
**Authors:** Zhou, D.; He, J. (2023)  
**ID:** `10.1145/3626520`  
**Odin Topics:** 8.A, 8.B, 12.A, 12.B  

**TLDR:** Reviews state-of-the-art techniques for rare category analysis in complex data, covering exploration, exploitation, representation, and interpretation under challenges of rarity, label scarcity, non-separability, heterogeneity, and dynamics.

**Problem & Motivation:** Rare categories are often most important in high-impact domains like fraud detection and disease diagnosis, but traditional anomaly detection yields many uninteresting anomalies. Existing methods fail to identify rare categories that are compact and statistically significant. A systematic review of techniques addressing rarity, non-separability, heterogeneity, and dynamics is missing.

**Approach (summary):**
- Surveys over 100 papers on rare category analysis from data mining and machine learning.
- Organizes techniques into four tasks: exploration (unsupervised), exploitation (semi-supervised), representation learning, and interpretation.
- Covers static and dynamic data, including tabular, time-series, and graph-structured data.

**Key Findings (selected):**
- "num: Only 0.1% of Sloan sky survey images are anomalies; 99% of those anomalies are uninteresting, leaving 0.001% as useful rare categories."
- "num: To detect a rare category with proportion 0.01%, random sampling requires approximately 10,000 labeling requests."
- "num: NNDM algorithm guarantees identification of at least one example from each minority class with probability 1-δ after O(2α/r^2) iterations."
- Rare categories are compact in feature space and non-separable from majority classes, requiring specialized detection algorithms.

**Limitations / Contradictions for Odin:**
- "The survey does not address computational efficiency constraints of mobile PFMS. [unacknowledged]"
- "User privacy and data security concerns in rare category detection are not discussed. [unacknowledged]"
- "Real-time detection requirements for streaming financial transactions are not explicitly evaluated. [unacknowledged]"

**Key takeaways:**
- "Rare categories are a subset of anomalies that are both statistically significant and compact."
- "num: 99% of anomalies are uninteresting noise; only 1% are useful rare categories."
- "Labeling rare categories is expensive due to extreme class imbalance as low as 0.01%."

---


## "Data Science and Business Analytics Approaches to Financial Wellbeing: Modeling Consumer Habits and Identifying At-Risk Individuals in Financial Services"
**Filename:** `IA--Machireddy_summarized.md`  
**Authors:** "Machireddy, J." (2023)  
**ID:** `a1b2c3d4-e5f6-7890-1234-567890abcdef`  
**Odin Topics:** 5.A, 5.B, 5.C, 6.A, 8.A, 8.B, 10.A, 10.B, 13.B  

**TLDR:** "Data science models using transaction data and digital footprints can profile consumer financial behavior, identify at-risk individuals, and support ethical risk management through explainable AI."

**Problem & Motivation:** "Financial hardship from over-indebtedness and income volatility affects many consumers, leading to defaults and economic instability. Traditional credit scoring uses limited variables and static updates, failing to capture real-time behavioral signals. There is a need for data-driven approaches to model financial habits and detect early warning signs."

**Approach (summary):**
- "Extract behavioral features from transactional data including income volatility, discretionary spending percentage, and liquidity trends."
- "Apply machine learning models such as gradient boosting, hidden Markov models, and autoencoders for risk prediction and anomaly detection."
- "Incorporate psychological traits and contextual factors like life events and economic conditions to enrich consumer profiles."

**Key Findings (selected):**
- "Transactional and digital footprint data enable dynamic financial health portraits that shift in real time."
- "Machine learning models can detect early warning signs of financial distress such as income drops or rising credit reliance before default occurs."
- "Explainable AI techniques improve consumer trust and allow regulators to verify fair decision-making."
- "Consumer segmentation by financial vulnerability allows targeted interventions like debt relief or budgeting tools."

**Limitations / Contradictions for Odin:**
- "No empirical results or quantitative evaluation of proposed models."
- "Does not address the cold-start problem for new users with no transaction history."
- "Real-time streaming infrastructure requirements are assumed but not detailed."

**Key takeaways:**
- "Transaction data alone is insufficient; psychological and contextual factors improve risk models."
- "Explainable AI like SHAP is necessary for regulatory compliance and consumer trust."
- "Consumer segmentation enables targeted interventions such as debt restructuring or coaching."

---


## Concept Drift Adaptation Methods under the Deep Learning Framework: A Literature Review
**Filename:** `IA--Xiang-et_al_summarized.md`  
**Authors:** Xiang, Q.; Zi, L.; Cong, X.; Wang, Y. (2023)  
**ID:** `10.3390/app13116515`  
**Odin Topics:** 6.A, 6.B, 8.A, 8.B, 12.B  

**TLDR:** A literature review of concept drift adaptation methods under deep learning, covering discriminative, generative, hybrid, and other learning approaches for handling non-stationary data streams.

**Problem & Motivation:** Data distribution changes cause concept drift, degrading deep learning model performance in dynamic environments like epidemics and big data. Existing reviews lack focus on deep learning frameworks for concept drift adaptation. This gap motivated the paper.

**Approach (summary):**
- Review of concept drift definition, causes, and types (abrupt, incremental, gradual, recurring).
- Classification of methods into discriminative learning (MLP, RNN, LSTM, CNN), generative learning (AE, GAN, RBM, SOM), hybrid learning, and others (deep transfer, deep reinforcement learning).
- Summary of update modes (parameter vs structure) and detection modes (active vs passive).

**Key Findings (selected):**
- "num: Most concept drift adaptation methods focus on abrupt, incremental, and gradual drift, with recurring drift least addressed."
- "Parameter updates are more common than structural updates due to faster convergence."
- "Active detection modes help explain drift occurrence but require additional memory and CPU."
- "Hybrid learning and discriminative learning methods dominate the literature."

**Limitations / Contradictions for Odin:**
- "The paper does not provide empirical comparisons of the reviewed methods."
- "It focuses on deep learning and excludes shallow learning concept drift methods. [unacknowledged]"
- "Most discussed methods assume labeled data, limiting applicability to unsupervised scenarios. [unacknowledged]"

**Key takeaways:**
- "Concept drift causes deep learning models to fail in dynamic data streams."
- "num: Most methods adapt to abrupt drift, but recurring drift remains challenging."
- "Parameter updates are preferred for faster convergence than structural updates."

---


## Comparative Study of Supervised and Unsupervised Machine Learning Approaches in Banking Applications
**Filename:** `IA--Harris-&-Austin_summarized.md`  
**Authors:** Harris, F.; Austin, V. (0)  
**ID:** `b7c9a6d2-5e3f-4a1b-8c7d-9e2f3a4b5c6d`  
**Odin Topics:** 8.A, 8.B  

**TLDR:** Supervised learning achieves high accuracy for credit scoring and fraud detection using labeled data, while unsupervised learning excels at anomaly detection and customer segmentation without labels.

**Problem & Motivation:** Banking institutions need to leverage machine learning on vast datasets but face choices between supervised and unsupervised approaches. Each approach has distinct strengths and limitations for tasks like fraud detection and customer segmentation. A systematic comparison is missing to guide practitioners on optimal selection based on data availability and objectives.

**Approach (summary):**
- Conducts a literature-based comparative analysis of supervised and unsupervised machine learning in banking.
- Examines supervised algorithms: regression, decision trees, SVMs, and neural networks for labeled data tasks.
- Examines unsupervised algorithms: clustering (k-means, hierarchical) and dimensionality reduction (PCA) for unlabeled data.

**Key Findings (selected):**
- Supervised learning provides higher predictive accuracy when labeled data is sufficient.
- Unsupervised learning enables discovery of hidden patterns without labeling costs.
- Hybrid models that use unsupervised for feature extraction then supervised for prediction improve overall performance.
- Credit scoring and fraud detection are best served by supervised learning.

**Limitations / Contradictions for Odin:**
- The paper is a conceptual comparison without empirical validation on real banking datasets. [unacknowledged]
- It does not address class imbalance issues in fraud detection datasets, though referenced works do. [unacknowledged]
- The interpretability trade-offs between supervised and unsupervised models are discussed but not quantified.

**Key takeaways:**
- Supervised learning needs labeled data but gives high accuracy.
- Unsupervised learning finds hidden patterns without labels.
- Hybrid models combine strengths of both approaches.

---


## A Comprehensive Review of Machine Learning Techniques for Intelligent Personal Finance Management Systems
**Filename:** `IA--D'Souza-et_al_summarized.md`  
**Authors:** D'Souza, M.; Bhegade, P.; Bhalekar, P.; Bhavsar, Y. (0)  
**ID:** `b9c5f2d1-3a4e-4b5c-8d6e-7f8a9b0c1d2e`  
**Odin Topics:** 5.A, 6.A, 6.B, 7.A, 7.B, 7.C, 8.A, 8.B, 12.A, 12.B  

**TLDR:** Reviews machine learning techniques for intelligent personal finance management across budgeting, forecasting, anomaly detection, and group expense management, highlighting a shift from rule-based to adaptive, data-driven systems.

**Problem & Motivation:** Current research on PFMS is fragmented across budgeting, forecasting, anomaly detection, and group expense management, limiting cohesive intelligent solutions. Most traditional systems lack adaptability and personalization, relying on rigid rules. A systematic review comparing machine learning models across these components is missing.

**Approach (summary):**
- Conducts a qualitative literature survey of personal finance management systems from 1997 to 2021.
- Compares statistical methods (ARIMA, EWMA), machine learning (Isolation Forest, clustering), and deep learning (LSTM, GRU).
- Evaluates techniques across four dimensions: budgeting, forecasting, anomaly detection, and group expense management.

**Key Findings (selected):**
- Rule-based budgeting is transparent but cannot adapt to non-linear spending changes.
- LSTM captures long-term dependencies but requires large historical data and lacks interpretability.
- Isolation Forest efficiently detects anomalies in unlabeled data and scales well.
- Hybrid ARIMA-LSTM models combine linear trend modeling with non-linear residual learning.

**Limitations / Contradictions for Odin:**
- "Qualitative survey without quantitative meta-analysis or statistical significance testing."
- "Lacks systematic search protocol and inclusion/exclusion criteria [unacknowledged]."
- "Does not address data privacy, security, or regulatory compliance in depth [unacknowledged]."

**Key takeaways:**
- "LSTM captures long-term spending patterns but is opaque and data-hungry."
- "Isolation Forest is efficient for unsupervised anomaly detection without labels."
- "Hybrid ARIMA-LSTM models balance linear and non-linear forecasting strengths."

---


## Next.js-Powered AI Platform for Smart Expense Tracking, Budgeting and Insights
**Filename:** `IA--Badiger-et_al_summarized.md`  
**Authors:** Badiger, R.; Robin, R.; Moraas, T.; Naik, V. G.; Karthikeyan, A. N. (0)  
**ID:** `e5c5f2a3-4b5c-6d7e-8f9a-0b1c2d3e4f5a`  
**Odin Topics:** 3.A, 3.B, 6.A, 6.B, 7.A, 7.B, 7.C, 8.A, 8.B, 12.A, 12.B  

**TLDR:** A Next.js-based AI platform integrates XGBoost transaction categorization, Gemini LLM insights, and Prophet forecasting, achieving 91.3% F1-score and reducing manual effort by 78%.

**Problem & Motivation:** Digital payment growth in India produces vast personal financial data, but individuals lack effective tools to interpret and act on it. Traditional budgeting methods fail to provide real-time, context-aware insights. Existing AI-driven systems suffer from limited personalization, opaque recommendations, and poor multi-channel support.

**Approach (summary):**
- System built on Next.js 14 with Clerk authentication, Supabase PostgreSQL, and Prisma ORM.
- XGBoost classifier maps transactions to 18 categories using merchant, amount, and temporal features.
- Gemini LLM generates insights via RAG prompting with user spending summaries and anomaly scores.

**Key Findings (selected):**
- "num: Weighted F1-score of 0.913 across 18 spending categories."
- "num: Manual expense-logging effort reduced by approximately 78% compared to conventional approaches."
- High-frequency categories (Food & Dining, Transport, Utilities) achieve F1 above 0.95.
- 84% of pilot users found AI-generated insights useful or very useful.

**Limitations / Contradictions for Odin:**
- Cold-start problem: categorization accuracy lower for new users with fewer than 50 transactions.
- LLM hallucination risk: Gemini may generate imprecise guidance despite RAG.
- Manual data entry dependency: users may not maintain complete records without banking API.

**Key takeaways:**
- XGBoost achieves 91.3% F1-score for transaction categorization.
- LLM insights rated useful by 84% of pilot users.
- Manual expense logging effort reduced by 78%.

---


## Note for the Agent

The summaries above contain **essential extracts** – enough to understand each paper's relevance to Odin, including supporting evidence and limitations.
If you need additional details not shown here (e.g., **critical citations, definitions, equations, full methodology, or the complete mapping rationale**),
**ask the user to send the original summary file (`<filename>_summarized.md`) or the converted MarkItDown file(`<filename>_marked.md`)** for the specific paper(s) of interest.
Do not invent missing information. Acknowledge gaps when they exist.