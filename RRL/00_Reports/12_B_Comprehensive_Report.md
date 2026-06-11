# Comprehensive Report for Subtopic: `12.B`

**Total files:** 54

This report includes problem/motivation, approach, key findings, support for Odin, and limitations/contradictions.

---


## "Proteus: Shapeshifting Desktop Visualizations for Mobile via Multi-level Intelligent Adaptation"
**Filename:** `I--Liu-et_al_summarized.md`  
**Authors:** "Liu, C.; Cheng, S.; Liang, F.; Jiang, Z.; Huang, L.; Athapaththu, K.; Wang, Y." (2026)  
**ID:** `d2b5c3f1-6a7e-4b8c-9d0f-1e2a3b4c5d6e`  
**Odin Topics:** 9.A, 9.B, 12.A, 12.B  

**TLDR:** "Proteus is an LLM-driven multi-agent framework that transforms desktop visualizations into mobile-optimized versions using a novel multi-level design space, outperforming a strong baseline in user studies."

**Problem & Motivation:** "Desktop visualizations are ill-suited for mobile screens due to different viewport sizes and interaction paradigms. Direct scaling causes illegible text, information loss, and interaction failures. Existing responsive visualization techniques treat adaptation as a flat layout puzzle lacking semantic understanding and hierarchical constraint propagation."

**Approach (summary):**
- "The authors propose a multi-level design space with three layers: Global Topology, Reference Frame, and Visual Elements."
- "They develop Proteus, a five-agent LLM system (Semantic Parser, Data Extractor, Design Planner, Frontend Engineer, Visual Critic) that iteratively adapts visualizations."
- "The system accepts HTML/SVG source code and renders mobile-optimized components using TypeScript and Recharts."

**Key Findings (selected):**
- "num: Proteus achieved 91.8% render success rate on 67 visualizations versus 87.8% for the baseline."
- "num: Wilcoxon signed-rank tests showed significant improvements for data fidelity and readability (p < 0.05) and for interaction reasonableness and aesthetics (p < 0.001)."
- "The multi-level design space enables hierarchical constraint propagation from global topology down to individual visual marks."
- "The visual critic agent autonomously evaluates and guides iterative refinement, essential for zero-intervention robustness."

**Limitations / Contradictions for Odin:**
- "High latency for complex SVG/HTML inputs due to large token counts."
- "Preserving subtle aesthetic qualities of bespoke visualizations remains difficult."
- "No task-oriented evaluation of analytic equivalence between desktop and mobile versions. [unacknowledged]"

**Key takeaways:**
- "Proteus achieves 91.8% render success on 67 diverse visualizations."
- "Multi-level design space outperforms flat geometry-centric heuristics."
- "LLM agents with a critic loop enable zero-intervention mobile adaptation."

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


## Comparing deep learning and classical regression approaches for predicting healthcare expenditure and spending: a systematic review
**Filename:** `IA--Lee-et_al_summarized.md`  
**Authors:** Lee, J. T.; Yeh, M. H.-S.; Li, V. C.-S.; Chen, H.-H.; Liu, Y.-H.; Chen, Y.-C.; Wu, D. B.-C. (2026)  
**ID:** `10.1080/13696998.2026.2630598`  
**Odin Topics:** 6.A, 6.B, 7.B, 12.A, 12.B  

**TLDR:** A systematic review of eight studies finds that deep learning models, especially LSTM and CNN-LSTM, improve healthcare cost prediction accuracy by 10-20% for longitudinal data, while tree-based methods remain competitive for cross-sectional tabular data.

**Problem & Motivation:** Healthcare expenditures are rising globally, and accurate individual-level cost prediction is essential for insurance, budgeting, and value-based care. Traditional regression models struggle with nonlinear, high-dimensional, and temporal patterns in health data. This review systematically compares deep learning to classical regression to determine when neural networks add predictive value.

**Approach (summary):**
- The review was preregistered (PROSPERO CRD420251129440) and searched Web of Science, PubMed, Embase, and Scopus through August 2025.
- Eligible studies used real-world individual-level data (claims, EHR, registries) to predict cost outcomes with at least one deep learning architecture and one classical regression comparator.
- Eight studies met inclusion criteria, spanning the US, Europe, and Asia, with sample sizes from 50,000 to over 1.4 million individuals.

**Key Findings (selected):**
- num: Longitudinal deep learning models (LSTM, CNN-LSTM) achieved 10-20% reductions in RMSE/MAE compared to regression and tree-based baselines.
- num: R2 improvements ranged from 0.01 to 0.15, with the highest gains in multi-year claims and medication spending forecasts.
- num: AUROC for high-risk classification reached up to 0.78 in preventable cost prediction.
- Prior costs and utilization were consistently the strongest predictors across all studies.

**Limitations / Contradictions for Odin:**
- "Only eight studies included, with high heterogeneity in designs, populations, and outcomes."
- "No external validation across independent datasets; temporal validation limited."
- "Short prediction horizons (mostly one year) limit assessment of long-term dynamics."

**Key takeaways:**
- "LSTM models reduce spending forecast error by 10-20% over linear regression."
- "Prior spending history is the strongest predictor of future expenditure."
- "Tree-based models match deep learning for cross-sectional tabular data."

---


## LSTM-Based Consumer Behavior Prediction Model Research
**Filename:** `IA--Chen-&-Tan_summarized.md`  
**Authors:** Chen, S.; Tan, W. (2025)  
**ID:** `10.1145/3785706.3785906`  
**Odin Topics:** 5.A, 5.C, 6.A, 6.B, 12.B  

**TLDR:** Predicts consumer purchase intentions using a bidirectional LSTM with self-attention, achieving 94.2% accuracy on 80 million e-commerce interactions.

**Problem & Motivation:** Traditional statistical models and simple machine learning methods fail to capture temporal dependencies and high-dimensional patterns in large-scale consumer data. Deep learning offers potential but requires adaptation for sequential behavior prediction. This study addresses the gap by proposing an LSTM-based model for e-commerce purchase intention forecasting.

**Approach (summary):**
- Dataset contains 500,000 users with over 80 million interaction records (browsing, search, cart, purchase) from a major e-commerce platform over 12 months.
- Preprocessing uses Apache Spark distributed framework, 30-day sliding windows with 50% overlap, generating 128-dimensional feature vectors.
- Model architecture: bidirectional LSTM with 512 hidden units, self-attention with 8 heads, adaptive dropout (0.5→0.3), and softmax output for five purchase intention levels.

**Key Findings (selected):**
- num: Proposed LSTM achieves 94.2% accuracy, 93.8% precision, 94.7% recall, and 94.2% F1-score.
- num: Outperforms standard LSTM by 3.0 percentage points and traditional ML by average 10.7 percentage points (p<0.001).
- num: High-frequency users reach 96.1% accuracy, new users 91.8% (23.6% improvement over traditional methods), high-value customers 96.7%.
- Attention weight analysis reveals recency bias (ratio 1.847) and higher importance for behavioral features over demographics.

**Limitations / Contradictions for Odin:**
- Dataset from a single e-commerce platform limits generalizability to PFMS contexts.
- External environmental factors (e.g., economic shocks) are not modeled [unacknowledged].
- Real-time prediction latency and deployment constraints are not evaluated [unacknowledged].

**Key takeaways:**
- LSTM with attention achieves 94.2% accuracy on purchase prediction.
- Behavioral features dominate over demographics (cumulative score 0.521).
- Model generalizes to new users with 91.8% accuracy.

---


## Using Item Personality-Based Profiling in Music Recommender Systems
**Filename:** `LA--de_Goma-et_al_summarized.md`  
**Authors:** de Goma, J.; Anonuevo, J. N.; Pangan, G. N.; Deang, J. J.; Villaluz, A. (2025)  
**ID:** `10.1145/3779657.3779698`  
**Odin Topics:** 5.A, 5.C, 12.B  

**TLDR:** Incorporating Big Five personality profiles into a hybrid LightFM recommender improves music recommendation accuracy over pure collaborative filtering, especially for cold-start users.

**Problem & Motivation:** Music recommender systems struggle with user variability and the cold-start problem. Traditional collaborative filtering fails to capture diverse user preferences. Personality-based profiling offers a potential solution but has accuracy issues.

**Approach (summary):**
- Data collected from 208 Mapua students via survey (10-item BFI, 100 song ratings, top 5 genres) plus Million Song Dataset playcounts.
- LightFM hybrid model with user features (BFI T-scores, genre preferences) and item features (sonic features: acousticness, danceability, energy, etc., and item personality profiles as proportions).
- Item personality profile computed as proportion of users who liked the item with a given Big Five degree.

**Key Findings (selected):**
- num: Hybrid WARP model achieved training precision 0.23, recall 0.75, AUC 0.82; validation precision 0.46, recall 0.64, AUC 0.57.
- Pure CF overfitted (training AUC 1.00, validation AUC 0.56) and performed worse on unseen data.
- Online evaluation: hybrid Model A had mean user satisfaction 4.15 vs pure CF 3.55 (p<0.05).
- Hybrid model achieved precision 0.57, recall 0.62, F1 0.58 on user feedback, outperforming pure CF (0.41/0.46/0.40).

**Limitations / Contradictions for Odin:**
- "Small song dataset (100 songs) limits recommendation variation. [unacknowledged]"
- "Personality data available for less than 20% of users, causing sparsity. [acknowledged]"
- "Online evaluation sample size of 20 new users is small. [unacknowledged]"

**Key takeaways:**
- Hybrid WARP model achieved 0.46 precision and 0.64 recall on validation.
- Personality profiling reduces cold-start problems in recommender systems.
- User satisfaction improved by 0.6 points with personality integration.

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


## "MACHINE LEARNING TIME SERIES FORECASTING: A COMPREHENSIVE SURVEY AND STOCK MARKET APPLICATION"
**Filename:** `IA--Hall_summarized.md`  
**Authors:** "Hall, T." (2025)  
**ID:** `d1e2f3a4-b5c6-47d8-9e0f-1a2b3c4d5e6f`  
**Odin Topics:** 6.B, 12.A, 12.B  

**TLDR:** "A survey and application demonstrate that LightGBM and recurrent neural networks excel in time series forecasting, with LightGBM offering computational efficiency and a day trading model achieving daily returns 500 times higher than human traders."

**Problem & Motivation:** "Existing time series surveys cannot compare models fairly because each study uses different datasets and implementations. Day trading poses exceptional difficulty for human traders due to cognitive biases and slow reaction times. No prior work has applied a unified ML framework to second-by-second trading across all US equities with realistic execution constraints."

**Approach (summary):**
- "Survey identified 79 papers from Web of Science (2017-2024) that compare at least one tree-based and one deep learning model under identical experimental conditions."
- "Application used two years of second-by-second trade and quote data for all US equities, engineered multi-timeframe technical indicators and stock attributes."
- "LightGBM models estimated risk-reward ratios over multiple forward horizons with min-max regularized target and equal weighting."

**Key Findings (selected):**
- "num: LightGBM and LSTM/GRU consistently outperform other architectures across time series tasks."
- "num: Tree-based methods show a significant computational efficiency advantage over deep learning, often training 10-100x faster."
- "num: The best ML day trading model achieved average daily profit of 20,000 basis points with a Sharpe ratio of 15.78 across 999 trades per day."
- "num: ML daily returns were more than 500 times higher than top human day traders."

**Limitations / Contradictions for Odin:**
- "The survey's citation-based selection may bias results toward older, highly cited papers [unacknowledged]."
- "The day trading model was not tested on out-of-sample periods beyond the two-year window [unacknowledged]."
- "Human trader benchmark comparisons are approximate, not controlled head-to-head [unacknowledged]."

**Key takeaways:**
- "LightGBM and LSTM are top performers for time series forecasting."
- "Tree-based methods offer major computational speed advantages over deep learning."
- "ML day trading model achieved 20,000 bps average daily profit."

---


## Review of Methods and Models for Forecasting Electricity Consumption
**Filename:** `IA--Misiurek-et_al_summarized.md`  
**Authors:** Misiurek, K.; Olkuski, T.; Zysk, J. (2025)  
**ID:** `10.3390/en18154032`  
**Odin Topics:** 6.A, 6.B, 12.A, 12.B  

**TLDR:** A comprehensive review of electricity consumption forecasting methods across four time horizons, comparing classical statistical models with modern machine learning and deep learning techniques.

**Problem & Motivation:** Accurate electricity forecasting is critical for balancing supply and demand, integrating renewable energy, and modernizing grids. Inaccurate forecasts cause significant economic losses, with a 1% increase in error costing an additional USD 10 million annually. Existing methods range from classical ARIMA to advanced deep learning, but no universal approach exists.

**Approach (summary):**
- Reviewed over 100 studies on electricity load forecasting published up to 2024, with emphasis on works from the last 5 years.
- Categorized forecasting horizons into very short-term (30 min), short-term (day to weeks), medium-term (months to years), and long-term (decades).
- Compared classical statistical methods (ARIMA, SARIMA, Holt-Winters, linear regression) against machine learning (ANN, Random Forest) and deep learning (LSTM, CNN-LSTM, Transformer).

**Key Findings (selected):**
- "num: LSTM model achieved RMSE improvement of approximately 10-15% over traditional machine learning models in aggregated household forecasting."
- "num: Transformer with sparse attention achieved inference up to 5 times faster than RNN methods while maintaining comparable accuracy (sMAPE ≈ 0.18 for 1-day forecast)."
- "num: ARIMA model outperformed regression (8.1% MAPE) and ANN (5.6% MAPE) with 3.8% MAPE for monthly electricity consumption in Saudi Arabia."
- "num: Hybrid SARIMA-ANN model (Khashei & Bijari) achieved lowest RMSE of 0.0792 compared to SARIMA alone at 0.0823 for Turkish electricity."

**Limitations / Contradictions for Odin:**
- "Review does not provide original empirical validation; all metrics are cited from primary studies."
- "External variables (temperature, GDP) used in models are difficult to predict ex ante for operational forecasting."
- "Electricity consumption patterns differ from personal spending; direct transferability to PFMS requires adaptation and validation."

**Key takeaways:**
- "LSTM models improve forecasting RMSE by 10-15% over traditional methods."
- "Transformer models achieve 5x faster inference than RNNs with comparable accuracy."
- "No single universal forecasting method exists for all time horizons."

---


## ARTIFICIAL INTELLIGENCE-DRIVEN PERSONAL FINANCE SOLUTION
**Filename:** `IA--Bashshar-et_al_summarized.md`  
**Authors:** Bashshar, S. A.; Imran, M.; Kumar, P. S.; Goud, E. S.; Venunath, M.; Prasad, M. L. M. (2025)  
**ID:** `a2b8c9d0-e1f2-34a5-b678-90c1d2e3f4a5`  
**Odin Topics:** 3.A, 3.B, 6.A, 6.B, 12.A, 12.B  

**TLDR:** An AI-powered personal finance assistant uses NLP for transaction categorization and ARIMA for expense forecasting, achieving 86% categorization accuracy and MAE of 253.47.

**Problem & Motivation:** Manual tracking fails to provide real-time insights and predictive capabilities, leading to poor budgeting and low savings. Digital payments increase transaction volume, making it hard for individuals to understand spending habits. Existing systems lack automation and forecasting.

**Approach (summary):**
- Data is collected from user-uploaded CSV files containing transaction date, description, amount, and type.
- Preprocessing removes extraneous characters, normalizes fields, and applies tokenization, stopword removal, and lemmatization using NLTK.
- Transaction categorization uses keyword matching against domain-specific dictionaries without manual labeling.

**Key Findings (selected):**
- "num: Categorization accuracy of 86.2% with precision 0.88, recall 0.85, F1-score 0.86."
- "num: Forecasting MAE of 253.47 and RMSE of 318.91 over 30-day horizon."
- System captures seasonal spending patterns and main spending variations.
- User feedback from ten participants was mostly positive on interface intuitiveness and clarity.

**Limitations / Contradictions for Odin:**
- "Small sample size for user feedback (n=10) [unacknowledged]"
- "Categorization depends on static keyword dictionaries, may not generalize to new transaction types."
- "No comparison with deep learning baselines for forecasting [unacknowledged]"

**Key takeaways:**
- "NLP categorization achieved 86.2% accuracy on real transaction data."
- "ARIMA forecasting produced MAE of 253.47 for 30-day expenses."
- "Automated expense tracking reduces manual errors and improves awareness."

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


## Optimized Random Forest Classifier for Students Lifestyle Prediction Using Behavioral Data: A Machine Learning Approach
**Filename:** `LA--Ram-&-Agoylo_summarized.md`  
**Authors:** Ram, M. L.; Agoylo, J. C. Jr. (2025)  
**ID:** `10.54554/jtec.2025.17.02.004`  
**Odin Topics:** 5.C, 12.B  

**TLDR:** Random Forest classifier predicts lifestyle categories from behavioral data with 75.07% accuracy, validated on 93 students.

**Problem & Motivation:** Machine learning for lifestyle classification remains underexplored despite its potential. Balancing accuracy and generalization is a key challenge. Parameter optimization is needed to mitigate overfitting in behavioral analytics.

**Approach (summary):**
- Data source: Half a Million Lifestyle Dataset from Kaggle with 500,000 records.
- Preprocessing removed missing values, selected 9 behavioral features, and encoded gender numerically.
- Random Forest classifier trained with 40 decision trees to balance overfitting and generalizability.

**Key Findings (selected):**
- "num: Accuracy of 75.07% on test data, with precision 75.16%, recall 75.07%, and F1 score 74.40%."
- Training accuracy reaches 100% with 30+ trees, indicating overfitting despite strong memorization.
- Testing accuracy stabilizes around 75% beyond 20 trees, with optimal tree count 30-40.
- Real-world classification of 93 students: 41 Fitness Enthusiast, 50 Health-Conscious, 1 Eco-Friendly, 1 Social Media Influencer.

**Limitations / Contradictions for Odin:**
- "Lifestyle categories are predefined and may not capture the full spectrum of individual behaviors."
- "Self-reported behavioral data introduces potential bias. [unacknowledged]"
- "Real-world test sample of 93 students is small and from a single institution, limiting generalizability. [unacknowledged]"

**Key takeaways:**
- "Random Forest accuracy of 75.07% on lifestyle prediction."
- "Overfitting occurs with more than 30 decision trees."
- "Optimal tree count between 30 and 40 balances accuracy and efficiency."

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


## WEKA-BASED DECISION-TREE MODEL FOR USER SUBSCRIPTION PLAN PREDICTION
**Filename:** `LA--Guban-et_al_summarized.md`  
**Authors:** Guban, J. C. R.; Menderico, C. D. R.; Montalban, D. M. G. (2025)  
**ID:** `a1b2c3d4-e5f6-5123-89ab-cdef01234567`  
**Odin Topics:** 5.A, 5.C, 6.A, 12.A, 12.B  

**TLDR:** A J48 decision tree model predicts streaming subscription plans from user demographics and behaviors, achieving 72% accuracy with country as the strongest predictor.

**Problem & Motivation:** Streaming platforms lack interpretable models to understand how user attributes like age, device, and country jointly influence subscription plan selection. This gap hinders targeted marketing and plan optimization. The study addresses this by developing a transparent decision-tree classifier.

**Approach (summary):**
- Used 2,500 anonymized user records with five attributes: country, age, gender, device type, subscription start month.
- Applied J48 algorithm in WEKA with an 80/20 train-test split.
- Evaluated using accuracy, Kappa statistic, precision, recall, F-measure, and ROC area.

**Key Findings (selected):**
- "num: 72% overall accuracy on the test set."
- "num: Kappa statistic of 0.5797 indicates moderate agreement."
- Country identified as most influential predictor, followed by age and device type.
- Younger smartphone users subscribing later in the year tend to choose Premium plans in the US.

**Limitations / Contradictions for Odin:**
- Dataset limited to five user attributes, excluding behavioral indicators such as watch time or session frequency.
- Only J48 algorithm tested; ensemble methods not explored.
- Model not validated on a different dataset or in a real-time setting.

**Key takeaways:**
- J48 decision tree predicts subscription plans with 72% accuracy.
- Country is the strongest predictor, followed by age and device.
- All United Kingdom users consistently choose Standard plan.

---


## Expense tracker management system using machine learning
**Filename:** `IA--Thakur-&-Jadhav_summarized.md`  
**Authors:** Thakur, R. S.; Jadhav, A. (2025)  
**ID:** `10.14744/sigma.2025.00119`  
**Odin Topics:** 6.A, 6.B, 12.A, 12.B  

**TLDR:** Predicts future expenses using machine learning on household transaction data, finding a voting ensemble regressor achieves 78.11% R-squared.

**Problem & Motivation:** Manual expense tracking is time-consuming and error-prone, while existing apps lack predictive capabilities. There is a need for automated expense prediction to help users manage budgets. This paper addresses the gap by applying machine learning to forecast expenses from past spending patterns.

**Approach (summary):**
- Dataset: Daily Household Transactions (date, mode, category, subcategory, note, amount, income/expense, currency).
- Preprocessing: MinMax scaling, log1p transformation of amount, TF-IDF vectorization of text fields (min_df=3).
- Models: Individual (XGBoost, Random Forest, SVM, MLP, KNN, Decision Tree, Extra Tree, CatBoost) and ensemble (bagging, boosting, stacking, voting, blending).

**Key Findings (selected):**
- num: XGBoost achieves R-squared of 77.89%, highest among individual models.
- num: Voting ensemble regressor achieves highest R-squared of 78.11% and lowest relative absolute error of 0.1765.
- Voting ensemble outperforms bagging, boosting, stacking, and blending.
- RAE is the deciding factor due to similar R2 values across models.

**Limitations / Contradictions for Odin:**
- Manual data entry required, no automatic transaction fetching. [acknowledged]
- Limited to expense prediction; does not provide budget recommendations. [unacknowledged]
- R2 values around 78% leave substantial unexplained variance. [unacknowledged]

**Key takeaways:**
- Voting ensemble regressor achieves 78.11% R-squared for expense prediction.
- XGBoost outperforms other individual models with 77.89% R2.
- Manual expense entry remains a limitation of the system.

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


## Predictive Modeling for Loan Eligibility Assessment: A Comparative Study of Logistic Regression, Random Forest, and Support Vector Machine with Detailed Oversampling
**Filename:** `LA--Pandiin-&-Matias_summarized.md`  
**Authors:** Pandiin, J. D.; Matias, J. B. (2025)  
**ID:** `c7b3a1d9-6e5f-4c2a-8b9d-1f3e5a7c9d2b`  
**Odin Topics:** 12.A, 12.B  

**TLDR:** Compares Logistic Regression, Random Forest, and SVM for loan eligibility prediction using oversampling and genetic algorithm feature selection, finding Random Forest most balanced with 85% accuracy.

**Problem & Motivation:** Manual loan approval processes are inefficient and prone to error. Existing machine learning approaches lack robust feature selection and class imbalance handling. A comparative evaluation of optimized classifiers is needed for fair and accurate loan decisions.

**Approach (summary):**
- Data from Kaggle loan dataset with binary target variable Loan_Status.
- Oversampling applied to minority class to address imbalance.
- Feature selection using Correlation, RFE, SelectKBest, Lasso, and Genetic Algorithm optimization.

**Key Findings (selected):**
- Random Forest achieved highest accuracy (85%), precision (86%), recall (84%), F1-score (85%) with Lasso feature selection.
- num: Random Forest cross-validation mean accuracy 92%.
- num: Credit History most important feature (26.8%), followed by Applicant Income (19.7%) and Loan Amount (19.2%).
- SVM achieved 99% recall but low precision (63%), indicating many false positives.

**Limitations / Contradictions for Odin:**
- Only one dataset from Kaggle, limiting generalizability.
- No comparison with deep learning methods.
- Feature selection via GA may overfit to training data [unacknowledged].

**Key takeaways:**
- Random Forest with Lasso feature selection achieved 88.5% accuracy.
- Credit history is the most important predictor at 26.8%.
- SVM has near-perfect recall but high false positives.

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


## A Constrained, Data-Driven Budgeting Framework Integrating Macro Demand Forecasting and Marketing Response Modeling
**Filename:** `IA--Lu-et_al_summarized.md`  
**Authors:** Lu, Y.; Zhou, H.; Zhang, Y. (2025)  
**ID:** `10.51903/jtie.v4i3.466`  
**Odin Topics:** 6.A, 6.B, 7.A, 7.B, 7.C, 12.B  

**TLDR:** Integrates macro demand forecasting, marketing response with diminishing returns, and accounting constraints into a budget optimization framework under uncertainty.

**Problem & Motivation:** Budgeting must combine macroeconomic signals, channel-level marketing effectiveness, and hard accounting constraints. Existing approaches treat these components separately and ignore uncertainty, leading to suboptimal or constraint-violating allocations.

**Approach (summary):**
- Uses quarterly PCE components (durable, nondurable, services) from FRED as macro demand proxy.
- Compares seasonal naïve, SARIMAX, gradient boosting, and VAR in rolling backtest (2018Q1-2025Q3).
- Estimates marketing response from Advertising dataset (TV, radio, newspaper) using OLS, ridge, lasso, GBR, and Hill saturation model.

**Key Findings (selected):**
- num: Multivariate VAR improves aggregate demand accuracy with ≈2.85% MAPE.
- num: Newspaper spend has near-zero marginal ROI; radio saturates quickly, TV saturates slowly.
- Optimal marketing spend lies below the SG&A ratio cap due to diminishing returns.
- num: Spending at the deterministic cap yields ≈40% violation probability under demand uncertainty.

**Limitations / Contradictions for Odin:**
- "Macro PCE and Advertising datasets are not internally consistent; response-to-dollar normalization is arbitrary. [acknowledged]"
- "No adstock or carryover effects in marketing response, limiting dynamic budgeting. [acknowledged]"
- "Constraint calibration uses a single firm (Apple); results may not transfer to other sectors. [acknowledged]"

**Key takeaways:**
- "Optimal budgets often sit below ratio caps due to diminishing returns."
- "VAR forecasting achieved 2.85% MAPE for aggregate demand proxy."
- "Newspaper spend showed near-zero marginal ROI in the Advertising dataset."

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


## Credit Card Customer Profiling Using Self-Supervised Representation Learning on Multi-Source Financial Data
**Filename:** `IA--Yachamaneni-et_al_summarized.md`  
**Authors:** Yachamaneni, T.; Kotadiya, U.; Arora, A. S. (2025)  
**ID:** `10.63282/3050-9262.IJAIDSML-V6I1P118`  
**Odin Topics:** 5.A, 5.C, 6.A, 11.B, 12.B  

**TLDR:** Self-supervised representation learning on multi-source financial data (transactions, demographics, credit, web activity) outperforms K-Means and XGBoost in customer profiling, credit risk prediction, and churn detection.

**Problem & Motivation:** Traditional supervised customer profiling requires costly labeled data and fails to leverage unlabeled multi-source data. Static feature engineering cannot capture temporal dynamics or generalize across behavioral shifts. There is a need for scalable, privacy-friendly profiling that extracts rich representations from heterogeneous financial data without manual labels.

**Approach (summary):**
- A multi-source dataset of 100,000 customers with transaction logs, demographics, credit bureau reports, and web activity was collected.
- Separate encoders handle each modality: temporal encoders for sequences, feedforward layers for static features, and embeddings for categorical variables.
- SSL pretext tasks include masked attribute prediction, temporal order prediction, and augmented view prediction.

**Key Findings (selected):**
- "num: Proposed SSL achieves Silhouette score of 0.56, compared to K-Means (0.35) and XGBoost (0.41)."
- "num: SSL attains AUC of 0.91 for credit risk prediction, outperforming XGBoost (0.84)."
- "num: SSL reaches F1 of 0.81 for churn prediction, versus XGBoost (0.69)."
- "num: Removing temporal encoding causes a 4.2% drop in AUC, the largest decrease among ablated components."

**Limitations / Contradictions for Odin:**
- "Single private bank dataset may not generalize across diverse Filipino young professionals. [unacknowledged]"
- "Interpretability of SSL representations is not addressed, limiting regulatory acceptance. [acknowledged as gap]"
- "No comparison to other SSL methods (e.g., SimCLR, MoCo) on financial data. [unacknowledged]"

**Key takeaways:**
- "SSL outperforms XGBoost by 7 points in AUC for credit risk prediction."
- "Temporal encoding is the most critical component, causing a 4.2% drop."
- "Multi-source data including web activity boosts profiling accuracy by 3.8%."

---


## A SYSTEMATIC REVIEW OF DEMAND FORECASTING MODELS FOR RETAIL E-COMMERCE ENHANCING ACCURACY IN INVENTORY AND DELIVERY PLANNING
**Filename:** `IA--Chowdury-et_al_summarized.md`  
**Authors:** Chowdhury, A. R.; Paul, R.; Rozony, F. Z. (2025)  
**ID:** `10.63125/mbbfw637`  
**Odin Topics:** 6.A, 6.B, 12.A, 12.B  

**TLDR:** A systematic review of 72 studies finds machine learning and deep learning models outperform traditional statistical methods for demand forecasting in retail e-commerce, especially with volatile data and external variables.

**Problem & Motivation:** Retail e-commerce faces volatile demand and complex logistics, requiring accurate forecasting. Existing literature lacks a comprehensive synthesis of forecasting models for inventory and delivery planning. This review addresses that gap by evaluating 72 studies to guide model selection.

**Approach (summary):**
- Followed PRISMA guidelines for systematic review of 72 peer-reviewed articles from Scopus, Web of Science, IEEE Xplore, and ScienceDirect (2010–2024).
- Used keyword combinations including “demand forecasting,” “retail e-commerce,” “machine learning,” and “deep learning” to identify relevant studies.
- Categorized forecasting models into four groups: traditional statistical, machine learning, deep learning, and hybrid approaches.

**Key Findings (selected):**
- Traditional statistical models (ARIMA, Holt-Winters) remain relevant for stable, seasonal demand but fail under nonlinearity and promotional spikes.
- num: Machine learning models (random forests, gradient boosting) improve forecast accuracy by up to 20% over statistical methods in high‑SKU environments.
- Deep learning models (LSTM, GRU, CNN) capture long‑range dependencies and outperform other methods for erratic and intermittent demand.
- Hybrid ARIMA‑ML/DL models balance interpretability and accuracy, reducing forecasting error during flash sales and disruptions.

**Limitations / Contradictions for Odin:**
- The review only includes English‑language peer‑reviewed studies, potentially missing relevant industry reports. [unacknowledged]
- Performance comparisons across studies use different datasets and evaluation protocols, making direct aggregation difficult. [acknowledged in discussion]
- The paper does not address real‑time deployment constraints or inference latency for forecasting models.

**Key takeaways:**
- Forecasting accuracy can reduce inventory costs by up to 25%.
- Machine learning models beat statistical methods by 20% in volatile settings.
- Deep learning captures long‑term spending patterns better than ARIMA.

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


## AI-Powered Financial Insights Platform
**Filename:** `IA--Reddy-et_al_summarized.md`  
**Authors:** Reddy, S. T.; C., S.; G., T.; BG, D.; Gupta, S. (2024)  
**ID:** `c3b5c3d0-8f3a-5a1c-9e2a-4f7b8c9d0e1f`  
**Odin Topics:** 3.A, 3.B, 6.A, 6.B, 7.B, 7.C, 10.A, 10.B, 12.A, 12.B, 13.A, 13.B  

**TLDR:** A full-stack AI personal finance platform with conversational CA advisor, receipt scanner, portfolio tracker, EMI calculator, and LSTM spending forecast.

**Problem & Motivation:** Indian working-class and students lack affordable, personalized financial advisory. Existing apps like Mint are US-only, and Indian investment platforms lack budgeting and AI advice. No unified system covers budgeting, investment, EMI, tax planning with user-specific data.

**Approach (summary):**
- Built Next.js 15 full-stack with PostgreSQL, Prisma, and Clerk authentication.
- Conversational AI uses Groq LLAMA 3.1 8B/70B for intent parsing, investment advice, and CA Arjun persona.
- Receipt scanner uses Google Gemini 1.5 Flash with multimodal prompt extracting amount, merchant, category.

**Key Findings (selected):**
- "num: Dashboard initial load 420ms to first meaningful content."
- "num: Receipt scan average 2.1 seconds with >92% accuracy (citing prior research)."
- "num: Live portfolio fetch for 10 holdings in 1.4 seconds."
- "num: EMI schedule creation for 60 months takes 180ms DB round-trip."

**Limitations / Contradictions for Odin:**
- "Geographical and regulatory focus on India limits external validity. [unacknowledged]"
- "Dependency on third-party APIs (Yahoo Finance, MFAPI.in) introduces failure risk. [acknowledged]"
- "Requires 3 months of user financial context for AI to provide accurate advice (cold-start). [acknowledged]"

**Key takeaways:**
- "Receipt scanner achieves sub-2.1s processing with >92% accuracy."
- "LLAMA 3.1 8B delivers sub-200ms intent classification."
- "Dashboard initial load at 420ms using SSR and Suspense."

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


## When machine learning meets econometrics: Can it build a better measure to predict multidimensional poverty and examine unmeasurable economic conditions?
**Filename:** `LA--Onsay-&-Rabajante-2024b_summarized.md`  
**Authors:** Onsay, E. A.; Rabajante, J. F. (2024)  
**ID:** `10.1016/j.sctalk.2024.100387`  
**Odin Topics:** 12.A, 12.B  

**TLDR:** Random forest outperforms econometric and other ML models in predicting multidimensional poverty for indigenous communities in the Philippines, achieving 0.9208 R-squared and 95.94% accuracy.

**Problem & Motivation:** Traditional poverty measurement methods are costly, labor-intensive, and time-consuming, making it difficult for policymakers to target interventions. Indigenous communities face complex, multifaceted socioeconomic conditions that generic poverty research fails to capture. There is a need for disaggregated, cost-effective methods to measure multidimensional poverty.

**Approach (summary):**
- Data comes from a complete census of indigenous communities in Goa, Camarines Sur, Philippines (1,660 indigenous households, 8,022 persons).
- Blends econometric causality tests (logit and probit) with ML models including random forest, LightGBM, XGBoost, SVM, and linear regression.
- Uses 15 multidimensional indicators (health, housing, water, education, income, peace/order) as predictors of poverty.

**Key Findings (selected):**
- "num: Random forest regressor achieved the highest R-square of 0.92075 for impoverished societies."
- "num: Random forest classifier attained 95.94% accuracy in pipeline algorithms and 90.69% at random."
- "num: Random forest had the lowest RMSE (0.3298) compared to LightGBM (0.3642) and XGBoost (0.4001)."
- "num: For indigenous communities, random forest R-square was 0.9208 and MSE 0.5497."

**Limitations / Contradictions for Odin:**
- "Results are specific to rural poverty in the Philippines; generalizability to other domains like personal finance is untested [unacknowledged]."
- "Paper acknowledges time required to build trustworthy datasets but does not discuss real-time prediction constraints."
- "Models rely on census data updated every two years, which may not capture rapid changes in financial behavior [unacknowledged]."

**Key takeaways:**
- Random forest achieved 0.9208 R-square for poverty prediction.
- Random forest classifier accuracy was 95.94% in pipeline algorithms.
- Random forest had the lowest RMSE (0.3298) among regressors.

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


## Budgeted Embedding Table For Recommender Systems
**Filename:** `IA--Qu-et_al_summarized.md`  
**Authors:** Qu, Y.; Chen, T.; Nguyen, Q. V. H.; Yin, H. (2024)  
**ID:** `10.1145/3616855.3635778`  
**Odin Topics:** 4.A, 4.B, 7.B, 7.C, 12.B  

**TLDR:** Proposes Budgeted Embedding Table (BET) for efficient embedding size search in recommender systems under strict memory budgets using table-level actions and a fitness predictor.

**Problem & Motivation:** Existing lightweight embedding methods rely on manually tuned trade-off coefficients that fail to strictly meet memory budgets and perform inefficient instance-by-instance search. The implicit memory complexity term cannot guarantee parameter usage caps, and RL-based approaches require costly per-instance optimization. A method is needed that directly enforces memory budgets while scaling to large user/item sets.

**Approach (summary):**
- Uses two real-world datasets, Gowalla and Yelp2018, with up to 1.56M interactions.
- Defines a bounded sampler that draws embedding sizes for all users and items from probabilistic distributions, ensuring total parameter usage is capped.
- Employs a DeepSets-based fitness predictor that evaluates table-level actions without full model retraining.

**Key Findings (selected):**
- "num: BET achieves the highest Recall@20 (0.1753) and NDCG@20 (0.1483) on Gowalla with LightGCN at 80% sparsity."
- "num: At 95% sparsity on Gowalla with LightGCN, BET obtains 0.0627 Recall@5 and 0.1037 NDCG@5, outperforming CIESS by 22% and 21% respectively."
- "num: On Yelp2018 with LightGCN at 80% sparsity, BET reaches 0.0873 Recall@20, exceeding the best baseline by 4%."
- BET guarantees strict memory budget satisfaction, unlike ESAPN and OptEmbed which often exceed target sparsity.

**Limitations / Contradictions for Odin:**
- "Does not address cold-start users or items; frequency-based ranking fails for new entities. [unacknowledged]"
- "May not generalize to streaming recommendation where user/item sets grow over time (mentioned as future work)."
- "Requires a pre-trained full embedding table, which itself may be infeasible for extremely large-scale systems. [unacknowledged]"

**Key takeaways:**
- "BET guarantees strict memory budget adherence without manual coefficient tuning."
- "DeepSets fitness predictor cuts evaluation cost from O(S*T) to O(T) full trainings."
- "At 95% sparsity, BET achieves 0.0627 Recall@5 on Gowalla with LightGCN."

---


## Adaptive Financial Literacy Enhancement through Cloud-Based AI Content Delivery: Effectiveness and Engagement Metrics
**Filename:** `IA--Li-et_al_summarized.md`  
**Authors:** Li, M.; Liu, W.; Chen, C. (2024)  
**ID:** `f47ac10b-58cc-4372-a567-0e02b2c3d479`  
**Odin Topics:** 5.A, 10.A, 10.B, 11.A, 11.B, 12.A, 12.B, 13.A, 13.B  

**TLDR:** Cloud-based AI adaptive learning for financial literacy improves knowledge acquisition (+37.8% vs +19.2%) and financial behaviors like savings (+24.3%) and debt reduction (-18.6%) over 12 months.

**Problem & Motivation:** Financial literacy rates remain persistently low globally, with only 33% of adults classified as financially literate. Traditional content delivery fails to account for individual learning preferences, resulting in suboptimal knowledge transfer and engagement. Limited personalization and rapid knowledge decay necessitate adaptive approaches.

**Approach (summary):**
- Data from 15,000 users across three Southeast Asian countries.
- Recurrent neural networks process temporal user interaction sequences for personalized content delivery.
- Bayesian knowledge tracing and reinforcement learning optimize content sequencing and adaptation.

**Key Findings (selected):**
- "num: Adaptive platform achieved 37.8% knowledge gain vs 19.2% for traditional methods."
- "num: Savings rates increased by 24.3% at 12-month follow-up."
- "num: Investment diversification improved by 31.7% and debt reduced by 18.6%."
- Sequential pattern analysis predicts knowledge acquisition success with 78.3% accuracy.

**Limitations / Contradictions for Odin:**
- No discussion of demographic representativeness. [unacknowledged]
- Potential self-selection bias in user sample. [unacknowledged]
- Absence of cost-benefit analysis for implementation. [unacknowledged]

**Key takeaways:**
- Adaptive AI increased financial knowledge by 37.8% over traditional methods.
- Savings rates rose 24.3% and debt fell 18.6% at 12-month follow-up.
- Engagement profiles predict learning success with 78.3% accuracy.

---


## A Survey of Time Series Data Forecasting Methods Based on Deep Learning
**Filename:** `IA--Chen-et_al_summarized.md`  
**Authors:** Chen, J.; Chen, T.; Wang, Y.; Wang, L. (2024)  
**ID:** `10.56557/jobari/2024/v30i69014`  
**Odin Topics:** 6.A, 6.B, 12.A, 12.B  

**TLDR:** Surveys deep learning methods for time series forecasting including RNN, LSTM, GRU, and Transformer, and compares their performance on public datasets.

**Problem & Motivation:** Traditional statistical models for time series forecasting require extensive manual feature engineering and struggle with large-scale data. Deep learning offers automatic feature extraction but faces challenges like vanishing gradients and difficulty capturing long-range dependencies. This survey systematically reviews deep learning methods to identify strengths and weaknesses for forecasting tasks.

**Approach (summary):**
- Reviews common time series features, datasets (ETT, ECL, Traffic, Weather, ILI, TE), and evaluation metrics (MSE, MAE, RMSE, MAPE, SMAPE, R²).
- Describes RNN structure and its vanishing/exploding gradient problem.
- Explains LSTM gating mechanism (forget, input, output gates) to address gradient issues.

**Key Findings (selected):**
- "num: Transformer achieved best performance on ETTm2 with MSE=3.418, MAE=1.399."
- "num: LSTM achieved minimum MAE on Electricity (1.848) and Traffic (0.020)."
- "num: GRU achieved minimum MSE on Electricity (19.524) and Traffic (0.00110)."
- "num: RNN achieved best performance on Weather with MSE=0.007, MAE=0.060."

**Limitations / Contradictions for Odin:**
- "Survey format; no novel algorithm proposed."
- "Univariate experiments may not generalize to multivariate spending data [unacknowledged]."
- "Excluded datasets with insufficient periodicity, limiting generalizability."

**Key takeaways:**
- "Transformer achieved lowest MAE (1.399) on ETTm2 dataset."
- "No single deep learning model dominates all time series forecasting tasks."
- "Deep learning automates feature extraction but requires large training data."

---


## User Cold Start Problem in Recommendation Systems: A Systematic Review
**Filename:** `LA--Yuan-et_al_summarized.md`  
**Authors:** Yuan, H.; Hernandez, A.A. (2023)  
**ID:** `10.1109/ACCESS.2023.3338705`  
**Odin Topics:** 4.B, 5.A, 5.B, 5.C, 6.A, 10.A, 10.B, 11.A, 12.A, 12.B  

**TLDR:** A systematic review of 45 papers (2016-2023) categorizes user cold start solutions into data-driven and method-driven approaches, analyzing evaluation metrics and future directions.

**Problem & Motivation:** Existing systematic reviews on user cold start are scarce, outdated, or fail to distinguish between user and item cold start problems. Solutions for these two problems differ, yet prior work often conflates them. A focused, up-to-date review is needed to guide researchers.

**Approach (summary):**
- Followed systematic literature review guidelines (Kitchenham 2007) with seven steps: research questions, search strings, database selection (IEEE, ACM, Web of Science), inclusion/exclusion criteria, paper search, pre-selection, full reading, and classification.
- Search strings combined terms like "recommendation system", "user cold start", and "cold start".
- 1480 papers initially retrieved; after title/abstract screening and inclusion/exclusion criteria, 45 papers from 2016-2023 were selected for deep analysis.

**Key Findings (selected):**
- num: 45 papers were selected from 1480 initial search results, with the highest number (11) published in 2020.
- Data-driven strategies commonly use cross-domain and social network data to provide additional user information for cold-start users.
- Method-driven strategies increasingly apply meta-learning, deep learning (DNN, GNN, GAN), and attention mechanisms to learn from limited user interactions.
- num: Most literature (over 70% of analyzed papers) uses ranking metrics such as NDCG@K and Hit@K for evaluation, rather than rating prediction metrics.

**Limitations / Contradictions for Odin:**
- "No experimental validation of the surveyed methods. [unacknowledged]"
- "Only 45 papers analyzed; may not capture all recent advances."
- "Does not address domain-specific challenges of personal finance systems. [unacknowledged]"

**Key takeaways:**
- "45 papers from 2016-2023 were analyzed for user cold start."
- "Data-driven and method-driven are the two main solution categories."
- "Meta-learning and deep learning are increasingly applied to cold start."

---


## Deep Learning for Time Series Forecasting: Advances and Open Problems
**Filename:** `IA--Casolaro-et_al_summarized.md`  
**Authors:** Casolaro, A.; Capone, V.; Iannuzzo, G.; Camastra, F. (2023)  
**ID:** `10.3390/info14110598`  
**Odin Topics:** 6.A, 6.B, 12.A, 12.B  

**TLDR:** Reviews deep learning architectures for time series forecasting, covering CNNs, RNNs, GNNs, Transformers, and generative models with benchmarks for short-term and long-term prediction.

**Problem & Motivation:** Existing surveys on deep learning for time series forecasting lack coverage of recent architectures like Transformers and diffusion models, and do not distinguish between short-term and long-term forecasting. This gap limits practitioners' ability to select appropriate models for different prediction horizons. The paper provides a comprehensive review to address these shortcomings.

**Approach (summary):**
- Reviews literature from 2016 onward, focusing on deep learning for time series forecasting.
- Covers CNNs, TCNs, RNNs (ESN, LSTM, GRU), GNNs, Deep Gaussian Processes, GANs, and diffusion models for short-term forecasting.
- Covers Transformer and its variants (LogTrans, Informer, Autoformer, FEDformer, etc.) for long-term forecasting.

**Key Findings (selected):**
- "num: Transformer variants like PatchTST achieve MSE of 0.149 on Weather dataset for 96-step prediction, outperforming LSTM and TCN."
- "num: Autoformer and FEDformer show lower MSE than Informer and LogTrans on most long-term benchmarks."
- Deep Gaussian Processes can provide confidence intervals, unlike other deep learning methods.
- Transformers face memory bottleneck (O(L^2) complexity) and local agnosticism.

**Limitations / Contradictions for Odin:**
- "Assumes time series stationarity, concept drift remains an open problem. [unacknowledged]"
- "Deep learning models require long time series to estimate millions of parameters."
- "Most methods cannot estimate prediction confidence intervals except Deep Gaussian Processes."

**Key takeaways:**
- "PatchTST achieves 0.149 MSE on Weather 96-step forecasting."
- "Transformers reduce complexity but suffer from local agnosticism."
- "Deep Gaussian Processes uniquely provide uncertainty intervals."

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


## A machine learning ensemble approach to predicting factors affecting the intention and usage behavior towards online groceries applications in the Philippines
**Filename:** `LA--Gumasing-et_al_summarized.md`  
**Authors:** Gumasing, M.J.J.; Ong, A.K.S.; Sy, M.A.P.C.; Prasetyo, Y.T.; Persada, S.F. (2023)  
**ID:** `10.1016/j.heliyon.2023.e20644`  
**Odin Topics:** 1.C, 5.A, 6.A, 11.A, 12.B  

**TLDR:** A machine learning ensemble of random forest and artificial neural network predicts that perceived benefits, perceived vulnerability, behavioral intention, performance expectancy, and perceived severity strongly influence online grocery app usage among Filipino consumers during COVID-19.

**Problem & Motivation:** Despite the rise of online grocery shopping in the Philippines during COVID-19, factors driving consumer intention and usage behavior remain underexplored. Existing studies using traditional statistical methods have limitations in capturing complex, nonlinear relationships. A holistic measurement integrating health concerns and technology acceptance is needed.

**Approach (summary):**
- Data from 373 Filipino online grocery consumers collected via 5-point Likert survey.
- Integrated Protection Motivation Theory (PMT) and Unified Theory of Acceptance and Use of Technology (UTAUT2) with 11 latent variables.
- Used Random Forest Classifier (optimized over 6400 runs with depth 6, 90:10 train-test split, 96% accuracy).

**Key Findings (selected):**
- "num: Random Forest achieved 96% accuracy with 0.00 standard deviation at depth 6."
- "num: Artificial Neural Network achieved 96.63% average testing accuracy."
- Perceived benefit is the most significant factor (importance score 0.270), followed by perceived vulnerability (0.265) and behavioral intention (0.258).
- All ten constructs (performance expectancy, effort expectancy, social influence, hedonic motivation, facilitating conditions, perceived benefit, perceived vulnerability, perceived severity, perceived susceptibility, response efficacy) significantly affect behavioral intention or usage behavior.

**Limitations / Contradictions for Odin:**
- Respondents majorly reside in highly urbanized cities, affecting technological literacy representation.
- Lack of consideration of socio-economic factors for customer segmentation.
- No validation of model generalizability to other types of financial apps [unacknowledged].

**Key takeaways:**
- Perceived benefit is the strongest predictor of app usage behavior at 100% importance.
- Random Forest and ANN both achieved over 96% accuracy in predicting user behavior.
- Integration of health belief model with technology acceptance improves prediction for pandemic contexts.

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


## Purchasing Intentions Analysis of Hybrid Cars Using Random Forest Classifier and Deep Learning
**Filename:** `LA--Ong-et_al_summarized.md`  
**Authors:** Ong, A.K.S.; Cordova, L.N.Z.; Longanilla, F.A.B.; Caprecho, N.L.; Javier, R.A.V.; Borres, R.D.; German, J.D. (2023)  
**ID:** `10.3390/wevj14080227`  
**Odin Topics:** 5.C, 6.A, 12.B  

**TLDR:** Random forest classifier (94% accuracy) and deep learning neural network (96.6% accuracy) predict Filipino drivers’ hybrid car purchase intentions, with perceived environmental concern and attitude as top factors.

**Problem & Motivation:** Hybrid cars are not widely adopted in the Philippines despite their environmental benefits. Limited studies use machine learning to analyze purchasing intentions for hybrid cars in developing countries. Understanding these intentions can guide automakers and support sustainable transportation goals.

**Approach (summary):**
- Surveyed 1048 Filipino drivers with a driver’s license using convenience and snowball sampling.
- Adapted questionnaire from prior hybrid car intention study with 12 latent variables from PEPB and UTAUT2 frameworks.
- Applied Decision Tree, Random Forest Classifier (RFC), and Deep Learning Neural Network (DLNN) to predict behavioral intention.

**Key Findings (selected):**
- num: Deep learning neural network achieved 96.60% accuracy in predicting behavioral intention.
- num: Random forest classifier achieved 94% accuracy at 90:10 train-test split with Gini and best splitter.
- Perceived environmental concern (PENC) was the most important factor (100% normalized importance), followed by attitude (96.32%) and perceived behavioral control (94.50%).
- Basic decision tree produced much lower accuracy (max 72.32%) due to random tree generation per iteration.

**Limitations / Contradictions for Odin:**
- "Limited constructs from adapted questionnaire; self-administered online survey may introduce response bias. [unacknowledged]"
- "Only drivers with a license and social media presence were sampled, excluding non-digital or non-licensed populations."
- "Only two machine learning algorithms (RFC and DLNN) were used; other algorithms like Naïve Bayes or k-NN were not tested."

**Key takeaways:**
- "Deep learning achieved 96.6% accuracy for predicting purchase intentions."
- "Perceived environmental concern was the most important factor."
- "Random forest classifier reached 94% accuracy with Gini and best splitter."

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


## Forecasting Stock Market Prices Using Machine Learning and Deep Learning Models: A Systematic Review, Performance Analysis and Discussion of Implications
**Filename:** `IA--Sonkavde-et_al_summarized.md`  
**Authors:** Sonkavde, G.; Dharrao, D. S.; Bongale, A. M.; Deokate, S. T.; Doreswamy, D.; Bhat, S. K. (2023)  
**ID:** `10.3390/ijfs11030094`  
**Odin Topics:** 6.A, 6.B, 12.A, 12.B  

**TLDR:** A systematic review and comparative analysis of machine learning, deep learning, and ensemble models for stock price forecasting, with an implemented ensemble of Random Forest, XG-Boost, and LSTM achieving superior RMSE and R2 scores.

**Problem & Motivation:** Stock market prediction remains challenging due to unpredictable dynamics and limitations of traditional technical and fundamental analysis. Recent advances in machine learning and deep learning offer improved forecasting capabilities, but a comprehensive review with practical model comparisons is lacking. This paper addresses the gap by reviewing state-of-the-art algorithms and implementing an ensemble model for empirical evaluation.

**Approach (summary):**
- Data from Yahoo Finance for TAINIWALCHM and AGROPHOS stocks (2014-2023 for first, 2018-2023 for second).
- Implemented SVR, MLPR, KNN, Random Forest, XG-Boost, LSTM, and an ensemble of Random Forest+XG-Boost+LSTM.
- Evaluation metrics were RMSE and R2 score.

**Key Findings (selected):**
- num: Ensemble model (Random Forest+XG-Boost+LSTM) achieved RMSE 2.0247 and R2 0.9921 on TAINIWALCHM, best among all models.
- num: On AGROPHOS, ensemble achieved RMSE 1.2658 and R2 0.9897, outperforming individual algorithms.
- XG-Boost performed well with RMSE 2.0686 and R2 0.9842 on TAINIWALCHM.
- Random forest showed high R2 (0.9818) but very high RMSE (87.88) on TAINIWALCHM due to scale sensitivity.

**Limitations / Contradictions for Odin:**
- The study is a systematic review with a limited empirical case study (two stocks, one sector). [unacknowledged]
- Hyperparameter tuning is critical but the paper does not provide a systematic method for selecting optimal grids. [acknowledged]
- Stock market models degrade over time as market conditions evolve, requiring continuous retraining. [acknowledged]

**Key takeaways:**
- Ensemble of Random Forest, XG-Boost, and LSTM achieved R2 above 0.99 on test stocks.
- Hyperparameter tuning via grid search is critical for model performance.
- No universal model exists for stock or spending forecasting.

---


## Review of Family-Level Short-Term Load Forecasting and Its Application in Household Energy Management System
**Filename:** `IA--Ma-et_al_summarized.md`  
**Authors:** Ma, P.; Cui, S.; Chen, M.; Zhou, S.; Wang, K. (2023)  
**ID:** `10.3390/en16155809`  
**Odin Topics:** 6.A, 6.B, 12.B  

**TLDR:** Deep learning methods (LSTM, CNN, hybrid) improve short-term household load forecasting accuracy; probabilistic forecasting addresses uncertainty; these enable home energy management system scheduling.

**Problem & Motivation:** Household electricity consumption is rising and lacks consistent patterns due to human behavior, making system-level forecasting methods inadequate. Accurate short-term load forecasting is essential for home energy management systems to optimize energy use and reduce costs. Existing methods have limitations in accuracy, uncertainty handling, and real-time adaptability.

**Approach (summary):**
- Surveys deep learning models (LSTM, CNN, hybrid) for load forecasting with emphasis on sequence learning and feature extraction.
- Analyzes feature extraction techniques including wavelet decomposition, principal component analysis, and mutual information.
- Discusses adaptive online learning methods to handle dynamic load patterns and concept drift.

**Key Findings (selected):**
- "num: SVR-LSTM hybrid achieved correlation coefficient 0.9901, outperforming traditional SVR and LSTM."
- "num: CNNGRU with attention mechanism reached 92.06% accuracy in small-range load prediction and reduced prediction time by 75%."
- "num: Principal component analysis reduced 12 weather factors to 3 dimensions with 93.93% cumulative contribution rate."
- Bottom-up forecasting by aggregating appliance-level predictions improves accuracy over direct household-level forecasting.

**Limitations / Contradictions for Odin:**
- "Data quality issues (missing values, noise) affect prediction accuracy."
- "Deep learning models risk overfitting, especially with small datasets."
- "Real-time performance and uncertainty from user behavior remain challenging."

**Key takeaways:**
- "LSTM with empirical mode decomposition improves household load prediction accuracy."
- "Hybrid CNN-LSTM models outperform single models on irregular time series data."
- "Probabilistic forecasting captures uncertainty missed by point forecasts."

---


## Predicting the Filipino Household Income Using Naive Bayes Classification Algorithm
**Filename:** `LA--Apus-et_al_summarized.md`  
**Authors:** Apus, J. O.; Mantalaba, K. D. V.; Mackno, A. J. B.; Bokingkito, P. B. Jr. (0)  
**ID:** `a1b2c3d4-e5f6-4789-9a8b-7c6d5e4f3a2b`  
**Odin Topics:** 6.A, 12.B  

**TLDR:** Uses Naive Bayes on FIES data to predict Filipino household income classes, achieving 93% accuracy with bagging ensemble.

**Problem & Motivation:** Poverty reduction requires identifying vulnerable households. Existing studies use socio-demographic variables, but household expenditure and income variables remain unexplored for classification. This gap limits targeted interventions.

**Approach (summary):**
- Data from 2018 FIES with 41,545 instances and 60 features.
- Data cleaning handled missing values using mode for categorical, mean/median for numeric.
- Feature selection used univariate chi-squared test, selecting 13 features with highest scores.

**Key Findings (selected):**
- "num: Bagging ensemble achieved 93% accuracy, precision 0.93, recall 0.94, F1 0.94."
- "num: Boosting ensemble achieved 89% accuracy."
- Poor income class had most true positives; Rich class had fewest due to fewer instances.
- Model with >80% accuracy is considered good per literature.

**Limitations / Contradictions for Odin:**
- "Dataset only covers 2018, not updated annually. [unacknowledged]"
- "Feature independence assumption of Naive Bayes may reduce real-world accuracy. [unacknowledged]"
- "Only two ensemble methods tested; other algorithms not compared."

**Key takeaways:**
- "Naive Bayes with bagging yields 93% accuracy for income classification."
- "Food expenditure is the strongest predictor of income class."
- "Seven income brackets from Poor to Rich are used."

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