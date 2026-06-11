# Comprehensive Report for Subtopic: `6.B`

**Total relevant papers:** 47

This report includes problem/motivation, approach, key findings, support for Odin, and limitations/contradictions.

---


## Psychology and Development: Applications from Cognitive and Social Psychology
**Filename:** `I--Breza-&-Kaur_summarized.md`  
**Authors:** Breza, E.; Kaur, S. (2026)  
**ID:** `a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d`  
**Odin Topics:** 5.A, 5.C, 6.A, 6.B, 7.A, 7.B, 8.A, 11.A, 13.A, 13.B  

**TLDR:** Reviews how psychological constraints like self-control and limited cognition affect financial behaviors, and argues that missing markets for behavioral aids amplify poverty, informing personal finance system design.

**Problem & Motivation:** Development economics has focused on external constraints like missing markets, but internal psychological constraints also impede escaping poverty. These biases are amplified in developing countries due to proximity to subsistence, high volatility, weak institutions, and reliance on social ties. The paper reviews evidence across self-control, cognition, mental health, self-beliefs, and social norms to outline a research agenda for behavioral development economics.

**Approach (summary):**
- Provides a conceptual framework using missing markets to explain why behavioral aids are undersupplied.
- Identifies five key features of poverty that amplify psychological constraints: subsistence proximity, volatility, market failures, weak institutions, social ties.
- Reviews field experiments on self-control, including hard commitment (e.g., savings accounts) and soft commitment (e.g., lockboxes, reminders).

**Key Findings (selected):**
- num: 81% increase in total savings from a commitment savings account in the Philippines (Ashraf et al., 2006).
- num: Adding a social monitor increased savings by 36% in rural India (Breza and Chandrasekhar, 2019).
- num: 97.7% of farmers intend to use fertilizer but only 36.4% actually do (Duflo et al., 2011).
- num: 86% of individuals overpredict their savings, with average forecast error of 80% (Augenblick et al., 2023).

**Supports Odin (direct justifications):**
- People systematically underestimate irregular future expenses, leading to overconsumption and savings failures.
- Small transaction costs or physical actions (e.g., unlocking a lockbox) can effectively reduce temptation spending.
- Social observability of savings goals increases actual savings by 36% via reputation concerns.

**Limitations / Contradictions for Odin:**
- The literature on psychology of poverty has mixed replication, especially for priming manipulations.
- Most studies are short-term; long-run welfare effects of commitment devices remain unclear. [unacknowledged]
- The review does not provide precise meta-analytic estimates, limiting quantification of effect sizes.

**Key takeaways:**
- Commitment savings accounts increased savings by 81% in a Philippine field experiment.
- Soft commitment like lockboxes can be as effective as hard financial penalties.
- Financial concerns reduce cognitive performance and worker productivity by 7%.

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
- {'num': 'Random Forest expense classifier achieved 93-96% accuracy, outperforming rule-based systems (75-80%).'}
- {'num': 'LSTM forecasting produced a Mean Absolute Error of 4.7% for monthly expenditure prediction.'}
- {'num': 'Isolation Forest anomaly detection achieved 92% precision.'}
- {'num': '84% of users reported better spending awareness and 78% claimed increased savings control after one month.'}

**Supports Odin (direct justifications):**
- Random Forest achieves 93-96% accuracy for expense categorization, outperforming rule-based systems.
- LSTM forecasting reduces mean absolute error to 4.7% for monthly spending prediction.
- Isolation Forest detects anomalous transactions with 92% precision.

**Limitations / Contradictions for Odin:**
- Usability study limited to 50 participants, may not generalize. [unacknowledged]
- Long-term retention and engagement not evaluated. [unacknowledged]
- Data privacy and security not experimentally validated. [unacknowledged]

**Key takeaways:**
- Random Forest categorizes expenses with 93-96% accuracy.
- LSTM forecasts monthly spending with 4.7% MAE.
- 84% of users report better spending awareness after using the system.

---


## Consumer Expectations Survey Report 1st Quarter 2026
**Filename:** `L--Bangko_Sentral_ng_Pilipinas-2026_summarized.md`  
**Authors:** Bangko Sentral ng Pilipinas (2026)  
**ID:** `b3e5c6d7-8a9f-4b2c-9d1e-2f3a4b5c6d7e`  
**Odin Topics:** 1.C, 2.B, 6.B, 13.A, 13.B  

**TLDR:** Consumer sentiment improved in Q1 2026 with less pessimistic outlook, but year-ahead confidence decreased due to concerns over corruption, inflation, and government policies.

**Problem & Motivation:** Understanding consumer expectations is crucial for economic forecasting and policy formulation. The BSP conducts quarterly surveys to capture sentiment on income, spending, savings, and debt. Prior data showed pessimistic trends, requiring timely assessment of shifts in confidence.

**Approach (summary):**
- Data from 5,358 Philippine households (NCR and AONCR) surveyed 22 January to 5 February 2026.
- Sample drawn from PSA 2023 Geo-Enabled Master Sample using stratified multi-stage probability sampling.
- Confidence index computed as percentage of optimistic minus pessimistic responses.

**Key Findings (selected):**
- num: Overall confidence index improved from -22.2% to -15.8% in Q1 2026.
- num: Year-ahead confidence index decreased from 11.8% to 9.6%.
- num: Saving intention index increased from 4.6% to 12.4%.
- num: Borrowing intention index for next quarter improved from -71.7% to -69.5%.

**Supports Odin (direct justifications):**
- Consumer confidence improved by 6.4 percentage points from Q4 2025 to Q1 2026.
- Saving intention index rose from 4.6% to 12.4% in one quarter.
- Only 26.1% of saving households set aside at least 10% of monthly income.

**Limitations / Contradictions for Odin:**
- Survey conducted before the US-Israel-Iran conflict onset in February 2026 (acknowledged).
- Sample excludes individuals without stable address [unacknowledged].
- Only 5,358 households, may not fully represent young professionals [unacknowledged].

**Key takeaways:**
- Consumer sentiment less pessimistic in Q1 2026 but year-ahead outlook weakened.
- Saving intention index jumped to 12.4%, highest since 2021.
- Majority of households (58.6%) target housing under ₱450,000.

---


## An Intelligent AI-Based Framework for Automated Personal Financial Management
**Filename:** `IA--Patel-&-Singh_summarized.md`  
**Authors:** Patel, A.; Singh, A. (2026)  
**ID:** `f47ac10b-58cc-4372-a567-0e02b2c3d479`  
**Odin Topics:** 3.A, 3.B, 6.A, 6.B, 7.A, 7.B, 7.C, 10.A  

**TLDR:** An AI-based framework aggregates financial data from multiple sources, automatically categorizes transactions using rule-based and ML methods, forecasts expenditures, and provides personalized budget recommendations and alerts.

**Problem & Motivation:** Digital payment systems generate fragmented financial data that manual tracking cannot handle efficiently. Existing finance apps lack intelligent automation, personalization, and predictive insights. This gap leads to poor financial awareness and suboptimal decision-making.

**Approach (summary):**
- Data is aggregated from UPI, banking records, and digital wallets via APIs and secure ingestion.
- Rule-based logic and machine learning classify transactions into categories like food, travel, and bills.
- Historical spending patterns are analyzed to generate personalized dynamic budgets and forecasts.

**Key Findings (selected):**
- Automated transaction categorization reduces manual effort and improves accuracy over manual processes.
- Multi-source aggregation provides a unified real-time view of expenses across platforms.
- Personalized budget limits and real-time alerts improve spending control and reduce overspending.
- Predictive insights based on historical data enable users to forecast future expenditures and plan better.

**Supports Odin (direct justifications):**
- Automated transaction categorization reduces manual effort and improves accuracy.
- Aggregating data from multiple payment sources creates a unified financial view.
- Personalized budget limits based on historical spending improve budget control.

**Limitations / Contradictions for Odin:**
- Relies on quality of input data and third-party AI services. [acknowledged]
- No direct bank API integration for real-time sync; requires manual uploads. [acknowledged]
- Does not include deep learning or advanced NLP for financial assistants. [acknowledged]

**Key takeaways:**
- Automated transaction categorization reduces manual effort and improves accuracy.
- Personalized budget alerts help control overspending effectively.
- Aggregating multiple payment sources provides a unified financial view.

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
- {'Model architecture': 'bidirectional LSTM with 512 hidden units, self-attention with 8 heads, adaptive dropout (0.5→0.3), and softmax output for five purchase intention levels.'}

**Key Findings (selected):**
- {'num': 'Proposed LSTM achieves 94.2% accuracy, 93.8% precision, 94.7% recall, and 94.2% F1-score.'}
- {'num': 'Outperforms standard LSTM by 3.0 percentage points and traditional ML by average 10.7 percentage points (p<0.001).'}
- {'num': 'High-frequency users reach 96.1% accuracy, new users 91.8% (23.6% improvement over traditional methods), high-value customers 96.7%.'}
- Attention weight analysis reveals recency bias (ratio 1.847) and higher importance for behavioral features over demographics.

**Supports Odin (direct justifications):**
- LSTM networks with self-attention achieve 94.2% accuracy in predicting purchase intentions.
- Sequential behavioral features (purchase frequency, browsing duration) are more predictive than demographics (cumulative importance 0.521).
- The model maintains >90% accuracy across user segments including new users (91.8%) and high-frequency users (96.1%).

**Limitations / Contradictions for Odin:**
- Dataset from a single e-commerce platform limits generalizability to PFMS contexts.
- External environmental factors (e.g., economic shocks) are not modeled [unacknowledged].
- Real-time prediction latency and deployment constraints are not evaluated [unacknowledged].

**Key takeaways:**
- LSTM with attention achieves 94.2% accuracy on purchase prediction.
- Behavioral features dominate over demographics (cumulative score 0.521).
- Model generalizes to new users with 91.8% accuracy.

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
- num: Random forest with ensemble feature selection achieved 99.6% accuracy and 100% precision in credit card fraud detection.
- num: XGBoost consistently outperformed deep neural networks across 10 credit scoring datasets, achieving highest AUC and efficiency.
- num: CNN reduced fraud detection cost of failure by 30% and achieved 87.64% AUC on European dataset.
- num: GCN achieved 94.5% fraud detection accuracy, outperforming CNN (93%) by improving recall by 10% via graph-based user relationship analysis.

**Supports Odin (direct justifications):**
- Random forest with ensemble feature selection achieves 99.6% accuracy for fraud detection, suitable for Odin anomaly detection.
- LSTM improves expense forecasting accuracy by 30% over traditional regression models.
- AI personalization increases user engagement by 27% and retention by 15% in personal finance apps.

**Limitations / Contradictions for Odin:**
- Review primarily cites papers up to 2024; rapid ML/DL advances may render some comparisons outdated. [unacknowledged]
- Performance metrics are aggregated across heterogeneous datasets, making direct apples-to-apples comparisons difficult. [unacknowledged]
- The review does not address computational resource constraints of mobile-first deployment, which is critical for Odin. [unacknowledged]

**Key takeaways:**
- XGBoost outperforms deep learning for credit scoring across 10 datasets.
- Random forest achieves 99.6% fraud detection accuracy with feature selection.
- AI personalization lifts user engagement by 27% and retention by 15%.

---


## Foundations and Innovations in Data Fusion and Ensemble Learning for Effective Consensus
**Filename:** `IA--Du-et_al_summarized.md`  
**Authors:** Du, K.-L.; Zhang, R.; Jiang, B.; Zeng, J.; Lu, J. (2025)  
**ID:** `10.3390/math13040587`  
**Odin Topics:** 3.A, 5.C, 6.A, 6.B, 8.A, 8.B, 12.B  

**TLDR:** Surveys ensemble learning methods including bagging, boosting, random forests, and data fusion, analyzing bias‑variance trade‑offs, margin theory, and computational complexities.

**Problem & Motivation:** No single machine learning method universally outperforms others across all problem domains. Ensemble learning combines multiple models to improve predictive accuracy, robustness, and generalization. This survey addresses the need for a structured understanding of ensemble techniques and their theoretical foundations.

**Approach (summary):**
- Comprehensive literature review of ensemble learning and data fusion techniques.
- Covers bagging, boosting, random forests, stacking, and cascading methods.
- Includes advanced topics: multiclass classification, error‑correcting output codes, Dempster‑Shafer theory, multiple kernel learning, and multiview learning.

**Key Findings (selected):**
- Bagging reduces variance and improves stability, especially for high‑variance models like decision trees.
- Boosting reduces bias by sequentially focusing on misclassified instances but can overfit noisy data.
- Random forests consistently outperform most methods in predictive accuracy and handle missing data effectively.
- The C‑bound provides a more accurate risk indicator for majority voting than the Gibbs classifier's risk.

**Supports Odin (direct justifications):**
- Bagging reduces variance and improves stability for high‑variance models like decision trees.
- Boosting can convert weak learners into strong ones by focusing on misclassified instances.
- Random forests consistently outperform most methods in predictive accuracy and handle missing data effectively.

**Limitations / Contradictions for Odin:**
- Ensemble methods increase computational complexity and storage requirements [acknowledged].
- Dempster’s rule can produce counterintuitive results under high evidence conflict [acknowledged].
- Boosting tends to overfit noisy datasets [acknowledged].

**Key takeaways:**
- Bagging reduces variance by averaging models trained on bootstrap samples.
- Boosting sequentially focuses on misclassified instances to reduce bias.
- Random forests achieve high accuracy and handle missing data effectively.

---


## MACHINE LEARNING TIME SERIES FORECASTING: A COMPREHENSIVE SURVEY AND STOCK MARKET APPLICATION
**Filename:** `IA--Hall_summarized.md`  
**Authors:** Hall, T. (2025)  
**ID:** `d1e2f3a4-b5c6-47d8-9e0f-1a2b3c4d5e6f`  
**Odin Topics:** 6.B, 12.A, 12.B  

**TLDR:** A survey and application demonstrate that LightGBM and recurrent neural networks excel in time series forecasting, with LightGBM offering computational efficiency and a day trading model achieving daily returns 500 times higher than human traders.

**Problem & Motivation:** Existing time series surveys cannot compare models fairly because each study uses different datasets and implementations. Day trading poses exceptional difficulty for human traders due to cognitive biases and slow reaction times. No prior work has applied a unified ML framework to second-by-second trading across all US equities with realistic execution constraints.

**Approach (summary):**
- Survey identified 79 papers from Web of Science (2017-2024) that compare at least one tree-based and one deep learning model under identical experimental conditions.
- Application used two years of second-by-second trade and quote data for all US equities, engineered multi-timeframe technical indicators and stock attributes.
- LightGBM models estimated risk-reward ratios over multiple forward horizons with min-max regularized target and equal weighting.

**Key Findings (selected):**
- num: LightGBM and LSTM/GRU consistently outperform other architectures across time series tasks.
- num: Tree-based methods show a significant computational efficiency advantage over deep learning, often training 10-100x faster.
- num: The best ML day trading model achieved average daily profit of 20,000 basis points with a Sharpe ratio of 15.78 across 999 trades per day.
- num: ML daily returns were more than 500 times higher than top human day traders.

**Supports Odin (direct justifications):**
- LightGBM outperforms deep learning models in computational efficiency for time series forecasting.
- Combining multiple models and diverse features improves forecasting accuracy over any single model.
- High-frequency second-by-second data enables more accurate short-term financial predictions.

**Limitations / Contradictions for Odin:**
- The survey's citation-based selection may bias results toward older, highly cited papers [unacknowledged].
- The day trading model was not tested on out-of-sample periods beyond the two-year window [unacknowledged].
- Human trader benchmark comparisons are approximate, not controlled head-to-head [unacknowledged].

**Key takeaways:**
- LightGBM and LSTM are top performers for time series forecasting.
- Tree-based methods offer major computational speed advantages over deep learning.
- ML day trading model achieved 20,000 bps average daily profit.

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
- num: LSTM model achieved RMSE improvement of approximately 10-15% over traditional machine learning models in aggregated household forecasting.
- num: Transformer with sparse attention achieved inference up to 5 times faster than RNN methods while maintaining comparable accuracy (sMAPE ≈ 0.18 for 1-day forecast).
- num: ARIMA model outperformed regression (8.1% MAPE) and ANN (5.6% MAPE) with 3.8% MAPE for monthly electricity consumption in Saudi Arabia.
- num: Hybrid SARIMA-ANN model (Khashei & Bijari) achieved lowest RMSE of 0.0792 compared to SARIMA alone at 0.0823 for Turkish electricity.

**Supports Odin (direct justifications):**
- LSTM networks effectively learn complex temporal dependencies and can significantly improve forecasting accuracy over classical methods.
- Hybrid models combining statistical and machine learning outperform single models when linear and nonlinear structures cannot be separated.
- No single universal forecasting method exists; algorithm selection must match data characteristics and forecast horizon.

**Limitations / Contradictions for Odin:**
- Review does not provide original empirical validation; all metrics are cited from primary studies.
- External variables (temperature, GDP) used in models are difficult to predict ex ante for operational forecasting.
- Electricity consumption patterns differ from personal spending; direct transferability to PFMS requires adaptation and validation.

**Key takeaways:**
- LSTM models improve forecasting RMSE by 10-15% over traditional methods.
- Transformer models achieve 5x faster inference than RNNs with comparable accuracy.
- No single universal forecasting method exists for all time horizons.

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
- num: Categorization accuracy of 86.2% with precision 0.88, recall 0.85, F1-score 0.86.
- num: Forecasting MAE of 253.47 and RMSE of 318.91 over 30-day horizon.
- System captures seasonal spending patterns and main spending variations.
- User feedback from ten participants was mostly positive on interface intuitiveness and clarity.

**Supports Odin (direct justifications):**
- NLP with keyword matching achieves 86.2% accuracy for transaction categorization.
- ARIMA model can forecast 30-day expenses with MAE 253.47.
- Automated categorization reduces manual effort and improves financial awareness.

**Limitations / Contradictions for Odin:**
- Small sample size for user feedback (n=10) [unacknowledged]
- Categorization depends on static keyword dictionaries, may not generalize to new transaction types.
- No comparison with deep learning baselines for forecasting [unacknowledged]

**Key takeaways:**
- NLP categorization achieved 86.2% accuracy on real transaction data.
- ARIMA forecasting produced MAE of 253.47 for 30-day expenses.
- Automated expense tracking reduces manual errors and improves awareness.

---


## Hybrid Deep Learning Architectures for Time-Series Forecasting
**Filename:** `IA--Chishti_summarized.md`  
**Authors:** Chishti, Snehal More (2025)  
**ID:** `10.15662/IJEETR.2025.0704003`  
**Odin Topics:** 6.A, 6.B  

**TLDR:** Reviews hybrid deep learning architectures combining CNNs, RNNs, transformers, and GNNs for time-series forecasting, showing improved accuracy over standalone models.

**Problem & Motivation:** Traditional statistical models like ARIMA struggle with non-linear complex temporal dependencies in time-series data. Single deep learning models have inherent limitations: RNNs suffer vanishing gradients, CNNs limited local receptive fields, transformers need large data. Hybrid architectures that combine multiple models are needed to leverage complementary strengths.

**Approach (summary):**
- Searched IEEE Xplore, ACM Digital Library, SpringerLink, and Google Scholar for 2024 publications on hybrid deep learning for time-series forecasting.
- Included empirical studies with benchmark datasets and methodological novelty; excluded traditional statistical or standalone DL models.
- Categorized hybrid architectures into CNN-RNN, transformer-based, and GNN-integrated models.

**Key Findings (selected):**
- num: CNN-RNN hybrids outperformed individual CNN or LSTM models by 5-15% in RMSE on energy load forecasting datasets.
- num: GNN-CNN-LSTM hybrids improved spatial-temporal forecasting accuracy by up to 12% in traffic flow prediction.
- Transformer-based Multi-Scale Hybrid Transformer achieved state-of-the-art results on financial and weather datasets.
- Model interpretability remains limited, though attention mechanisms provide some insight.

**Supports Odin (direct justifications):**
- Hybrid CNN-RNN models outperform standalone LSTM by 5-15% in RMSE for time-series forecasting.
- Multi-scale feature extraction improves forecasting accuracy for financial and weather data.
- Graph neural networks capture spatial dependencies in multivariate time-series data.

**Limitations / Contradictions for Odin:**
- Review paper lacks primary empirical experiments on real-world spending data. [unacknowledged]
- Does not address cold-start problem in spending forecasting for new users. [unacknowledged]
- Computational complexity of hybrid models may hinder mobile-first deployment. [unacknowledged]

**Key takeaways:**
- Hybrid CNN-RNN models improve forecasting RMSE by 5-15% over single models.
- Multi-scale transformers capture both short and long-term temporal patterns.
- GNNs enable spatial-temporal forecasting for multivariate sensor data.

---


## Bridging AI and Emotion: Enhanced Models for Personal Finance Manager Applications
**Filename:** `IA--Bader-&-Haraty_summarized.md`  
**Authors:** Bader, S.; Haraty, R. A. (2025)  
**ID:** `10.12785/ijcds/1571107231`  
**Odin Topics:** 3.A, 5.A, 6.A, 6.B, 7.A, 7.B, 8.A, 8.B, 12.B, 13.A  

**TLDR:** An AI-driven financial advisor application integrates anomaly detection, sentiment analysis, and deep learning forecasting (Transformer, TCN, N-BEATS) to provide personalized budgeting, fraud detection, and merchant recommendations.

**Problem & Motivation:** Traditional financial apps rely on static rules and ignore user emotions and unstructured data, leading to poor recommendations and low engagement. There is a gap in leveraging AI to analyze both quantitative transactions and qualitative sentiment for adaptive financial advice.

**Approach (summary):**
- System architecture uses .NET Core 6 backend with Python TensorFlow/Keras for AI modules.
- Data sources: bank transaction logs, MCC merchant codes, account balances, and user profiles.
- Anomaly detection implements Isolation Forest, Local Outlier Factor (LOF), and One-Class SVM models.

**Key Findings (selected):**
- num: Mean Absolute Percentage Error (MAPE) improved from 10.5% to 7.8% when sentiment analysis was incorporated.
- num: Anomaly detection achieved 90% precision, 85% recall, and 0.93 ROC-AUC.
- num: Predictive accuracy within a 90% confidence interval reached 88% alignment with actual user behavior.
- num: Sentiment analysis reduced prediction error by 25% compared to rule-based budgeting systems.

**Supports Odin (direct justifications):**
- Anomaly detection using Isolation Forest and One-Class SVM achieves 90% precision and 85% recall on financial transactions.
- Incorporating sentiment analysis reduces MAPE from 10.5% to 7.8% in spending forecasting.
- Transformer, TCN, and N-BEATS models forecast spending patterns with 88% accuracy within a 90% confidence interval.

**Limitations / Contradictions for Odin:**
- Generalization across diverse financial behaviors and demographics not validated.
- Computational resources required for deep learning models may limit real-time deployment [unacknowledged].
- User trust and human-AI interaction in financial decision-making not studied [unacknowledged].

**Key takeaways:**
- Sentiment analysis improved MAPE from 10.5% to 7.8%.
- Anomaly detection achieved 90% precision and 85% recall.
- Transformer, TCN, and N-BEATS enable personalized spending forecasts.

---


## Deep learning-based time series forecasting
**Filename:** `IA--Song-et_al_summarized.md`  
**Authors:** Song, X.; Deng, L.; Wang, H.; Zhang, Y.; He, Y.; Cao, W. (2025)  
**ID:** `10.1007/s10462-024-10989-8`  
**Odin Topics:** 6.A, 6.B, 8.A, 8.B, 12.A, 12.B  

**TLDR:** A comprehensive review of deep learning-based time series forecasting models from 2014 to 2024, examining their ability to capture temporal dependencies and variable correlations, long-term forecasting optimizations, and loss functions.

**Problem & Motivation:** Traditional time series models like ARIMA fail to capture complex nonlinear correlations and long-term dependencies in real-world data. Deep learning offers potential but the field has rapidly expanded with many architectures. This survey systematically organizes the progress to guide researchers and practitioners.

**Approach (summary):**
- Reviews models from 2014-2024 including RNNs, LSTMs, GRUs, CNNs, TCNs, Transformers, and decomposition-based methods.
- Evaluates models on ETT, Electricity, Exchange, Traffic, and ILI datasets with input lengths 36-192 and output horizons 12-336.
- Uses MAE, MSE, MAPE, and R2 metrics with simple time split and sliding window validation.

**Key Findings (selected):**
- num: DLinear, a simple linear model, often outperforms complex Transformers, reducing MSE by up to 27.30% on ILI dataset compared to NS-Transformer.
- num: PatchTST’s patch attention improves MSE by 85.27% on Exchange dataset over vanilla attention.
- num: Shuffling input sequence degrades DLinear and PatchTST by 93-1092% in MSE, while complex models like TDformer improve, indicating poor use of sequential order.
- num: Fedformer achieves best trend and season prediction on artificial data, with MAE improvements of 26.65% (season) and 3.14% (trend) over second-best.

**Supports Odin (direct justifications):**
- DLinear, a simple linear model, often outperforms complex Transformers on time series forecasting tasks.
- Patch-based attention (PatchTST) significantly reduces memory usage while improving accuracy.
- Frequency-domain seasonal extraction outperforms time-domain methods for periodic spending patterns.

**Limitations / Contradictions for Odin:**
- Survey does not propose a novel algorithm; it synthesizes existing work. [unacknowledged]
- All experiments use public datasets (energy, traffic, exchange rates), not personal finance data. [unacknowledged]
- Does not consider real-time or streaming forecasting scenarios common in PFMS. [unacknowledged]

**Key takeaways:**
- Simple linear models (DLinear) often beat complex Transformers on forecasting accuracy.
- Patch-based attention reduces memory by 10.93% while improving MSE by 85.27% on exchange data.
- Frequency-domain methods extract seasonal spending patterns more accurately than time-domain.

---


## Predict, Optimize, Deliver: Demand Forecasting and Resource Optimization for a Market Research Firm
**Filename:** `LA--Mariano-&-Monreal_summarized.md`  
**Authors:** Mariano, M. T. G.; Monreal, R. N. (2025)  
**ID:** `10.1145/3785171.3785187`  
**Odin Topics:** 6.A, 6.B, 12.A, 12.B  

**TLDR:** Compares ARIMA, Holt-Winters, Prophet, and LSTM for demand forecasting and integrates with Pyomo-based optimization for workforce allocation in a market research firm, with Prophet achieving best balance of accuracy and usability.

**Problem & Motivation:** Professional service firms face demand uncertainty and inefficient manual workforce planning. Existing forecasting-optimization frameworks target product-based contexts, not time-sensitive service environments with high variance. There is a need for an integrated, interpretable pipeline that connects demand forecasting, resource optimization, and visualization.

**Approach (summary):**
- Historical time-tracking data from January 2018 to December 2024 (billable hours) for two clients.
- Compared ARIMA, Holt-Winters Exponential Smoothing, Prophet, and LSTM using MAE, RMSE, and MAPE across multiple train-test splits and a 30-day holdout.
- Weighted error score (0.35 MAE + 0.35 RMSE + 0.30 MAPE) plus interpretability and speed (0.25 each) for model selection.

**Key Findings (selected):**
- Prophet achieved the lowest weighted error for Client1 (13.038) and Client2 (27.786), and the best overall score (10.456) after including interpretability and speed.
- LSTM showed stable performance across training splits but higher complexity and data requirements reduced practical viability.
- ARIMA and Holt-Winters performed worse under noisy, volatile demand patterns.
- num: The optimization model achieved near-zero unmet demand under baseline and RMSE-adjusted scenarios, with occasional overutilization (e.g., 106% for shared resource S2).

**Supports Odin (direct justifications):**
- Prophet offers a robust balance between forecast accuracy and interpretability for short-term planning horizons.
- LSTM maintains stable performance across training sizes but requires more data and computational resources.
- Incorporating prediction intervals from RMSE into optimization improves allocation precision under demand uncertainty.

**Limitations / Contradictions for Odin:**
- Analysis restricted to output-based variables; input-level factors like individual analyst skill were unavailable.
- Forecasting model uses internal historical data only and does not incorporate external economic indicators.
- Long-range forecasting caution: rare high-impact events (e.g., COVID-19 pandemic) not considered.

**Key takeaways:**
- Prophet achieved the lowest weighted error score of 10.456.
- Forecast uncertainty bands from RMSE improve resource allocation resilience.
- The predict-then-optimize framework bridges predictive analytics and operational planning.

---


## Toward Transparent Optimization: A Systematic Review of Explainable AI in Decision-Making Systems
**Filename:** `IA--Danach-et_al_summarized.md`  
**Authors:** Danach, K.; Aly, W. H. F.; Tarhini, A.; Laouadi, S. (2025)  
**ID:** `10.29020/nybg.ejpam.v18i4.6707`  
**Odin Topics:** 6.A, 6.B, 7.B, 7.C, 8.A, 8.B, 10.A, 10.B, 12.A, 12.B  

**TLDR:** A systematic review synthesizes the integration of explainable AI (XAI) with optimization methods across healthcare, finance, logistics, and energy, proposing a taxonomy and highlighting trade-offs between performance and interpretability.

**Problem & Motivation:** Optimization-driven AI systems often operate as black boxes, undermining trust, regulatory compliance, and human-AI collaboration in high-stakes decisions. Despite advances in XAI, systematic integration with optimization frameworks remains fragmented and lacks unified taxonomies. This gap hinders the development of transparent, accountable intelligent systems.

**Approach (summary):**
- Conducted a systematic literature search across Scopus, Web of Science, IEEE Xplore, and ACM Digital Library for 2010-2024, retrieving 642 records and including 112 peer-reviewed studies after screening.
- Proposed a structured taxonomy categorizing XAI-optimization integration by explainability level, optimization complexity, and domain specificity.
- Analyzed integration strategies including post-hoc explanations (SHAP, LIME), interpretable models (decision trees, MILP), certificate-based verification, and data-driven frameworks like EXALT.

**Key Findings (selected):**
- num: EXALT framework reduces explanation generation time by 72% compared to post-hoc methods while maintaining 98% solution optimality.
- num: Explainable optimization approaches achieve error reduction rates of 41-68% compared to black-box optimization in healthcare logistics and derivatives pricing.
- Explainability constraints can enhance solution quality by acting as regularizers that embed domain knowledge.
- The trade-off between optimality and interpretability can be favorable, with explainable path constraints increasing solution cost by only a small margin.

**Supports Odin (direct justifications):**
- XAI methods can explain optimization-driven decisions without sacrificing near-optimal performance.
- Explainability constraints can be embedded as multi-objective optimization objectives.
- Certificate-based verification provides formal guarantees for solution properties like feasibility and stability.

**Limitations / Contradictions for Odin:**
- Scalability to large-scale industrial problems remains a significant challenge [unacknowledged].
- Standardization of explainability metrics and evaluation frameworks is lacking [acknowledged].
- Integration with existing enterprise systems and workflows has received limited research attention [unacknowledged].

**Key takeaways:**
- Explainable optimization reduces explanation time by 72% while preserving 98% optimality.
- XAI methods can turn black-box optimizers into transparent, auditable systems.
- The performance-interpretability trade-off is often favorable in practice.

---


## Expense tracker management system using machine learning
**Filename:** `IA--Thakur-&-Jadhav_summarized.md`  
**Authors:** Thakur, R. S.; Jadhav, A. (2025)  
**ID:** `10.14744/sigma.2025.00119`  
**Odin Topics:** 6.A, 6.B, 12.A, 12.B  

**TLDR:** Predicts future expenses using machine learning on household transaction data, finding a voting ensemble regressor achieves 78.11% R-squared.

**Problem & Motivation:** Manual expense tracking is time-consuming and error-prone, while existing apps lack predictive capabilities. There is a need for automated expense prediction to help users manage budgets. This paper addresses the gap by applying machine learning to forecast expenses from past spending patterns.

**Approach (summary):**
- {'Dataset': 'Daily Household Transactions (date, mode, category, subcategory, note, amount, income/expense, currency).'}
- {'Preprocessing': 'MinMax scaling, log1p transformation of amount, TF-IDF vectorization of text fields (min_df=3).'}
- {'Models': 'Individual (XGBoost, Random Forest, SVM, MLP, KNN, Decision Tree, Extra Tree, CatBoost) and ensemble (bagging, boosting, stacking, voting, blending).'}

**Key Findings (selected):**
- {'num': 'XGBoost achieves R-squared of 77.89%, highest among individual models.'}
- {'num': 'Voting ensemble regressor achieves highest R-squared of 78.11% and lowest relative absolute error of 0.1765.'}
- Voting ensemble outperforms bagging, boosting, stacking, and blending.
- RAE is the deciding factor due to similar R2 values across models.

**Supports Odin (direct justifications):**
- Voting ensemble regressor outperforms individual models for expense prediction on household transaction data.
- XGBoost achieves 77.89% R-squared for expense forecasting, second only to voting ensemble.
- Relative absolute error of 0.1765 is the lowest among all tested models.

**Limitations / Contradictions for Odin:**
- Manual data entry required, no automatic transaction fetching. [acknowledged]
- Limited to expense prediction; does not provide budget recommendations. [unacknowledged]
- R2 values around 78% leave substantial unexplained variance. [unacknowledged]

**Key takeaways:**
- Voting ensemble regressor achieves 78.11% R-squared for expense prediction.
- XGBoost outperforms other individual models with 77.89% R2.
- Manual expense entry remains a limitation of the system.

---


## A Comparative Analysis of Budget Forecasting Methods: A Systematic Literature Review Covering the 1983-2024 Period
**Filename:** `IA--Kara-&-Senguler_summarized.md`  
**Authors:** Şengüler, H.; Kara, B. (2025)  
**ID:** `10.1111/pbaf.70008`  
**Odin Topics:** 6.A, 6.B, 12.A  

**TLDR:** A systematic review of 69 studies finds no universally optimal budget forecasting method; performance depends on context, with simple models remaining strong benchmarks and deep learning emerging for short-term forecasts.

**Problem & Motivation:** Budget forecasts are critical for fiscal policy, but the literature lacks a systematic comparative evaluation of forecasting methods across different contexts. Fragmented findings make it difficult for practitioners to choose appropriate methods, and the field has seen rapid methodological diversification without clear guidance.

**Approach (summary):**
- Systematic literature review of 69 peer-reviewed studies comparing budget forecasting methods from 1983-2024.
- Dataset includes only studies that compare multiple methods against actual outcomes, excluding single-method or non-comparative work.
- Analysis includes descriptive statistics, trend analysis of method popularity over time, and network analysis of method-method, method-year, and method-metric co-occurrences using Gephi.

**Key Findings (selected):**
- num: 43% of studies focus on the United States, with developing economies substantially underrepresented.
- Four-phase methodological evolution: statistical methods (1980s), diversification (1990s-2000s), machine learning (2010s), deep learning and hybrid models (2020s).
- MAPE, RMSE, and MAE dominate evaluation metrics (38, 36, 22 studies respectively); directional errors and asymmetric costs largely neglected.
- Studies comparing 3-6 methods receive highest average citations (26 citations), while more than 7 methods show decline in citation impact.

**Supports Odin (direct justifications):**
- Forecasting method choice must be context-sensitive, not universal.
- Simple models like random walk and official forecasts remain strong benchmarks against which complex methods must be compared.
- Studies comparing 3-6 methods achieve highest academic impact, suggesting focused benchmarking over exhaustive comparisons.

**Limitations / Contradictions for Odin:**
- Geographic bias: 43% of studies from US, developing economies underrepresented. [unacknowledged]
- Metric hegemony: directional errors and asymmetric costs of forecast errors neglected. [acknowledged]
- Short training datasets (1-25 observations in 8 studies) raise reliability concerns for data-intensive methods. [acknowledged]

**Key takeaways:**
- No single forecasting method is universally optimal for all contexts.
- MAPE, RMSE, and MAE dominate evaluation but ignore directional error costs.
- Deep learning (LSTM) excels short-term (3-5 years), simple models for long-term (14+ years).

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
- {'Model selection based on task': 'RNN/LSTM for temporal dependencies, CNN/TCN for spatial hierarchies, Transformers for attention-based long-range dependencies.'}

**Key Findings (selected):**
- num: LSTM achieved 15% reduction in MAE over conventional methods in web traffic prediction.
- num: TCN attained 20% higher accuracy in early-stage anomaly detection compared to traditional methods.
- num: Transformer reduced MSE by 12% and MAE by 17% over recurrent and convolutional models in retail.
- num: Gradient Boosting Machine outperformed Random Forest with MAE of 170 vs 185 in energy dataset.

**Supports Odin (direct justifications):**
- Transformers reduce forecast error by 12-17% compared to recurrent models in retail data.
- Gradient Boosting Machines achieve MAE of 170 on energy data, outperforming Random Forest.
- TCNs provide 20% higher early-stage anomaly detection accuracy than traditional methods.

**Limitations / Contradictions for Odin:**
- The review lacks specific guidance for personal finance domains; results are from aggregate datasets not individual-level transactions.
- Computational constraints of Transformers may limit deployment on mobile devices [unacknowledged].
- Generalizability to Filipino financial behaviors and spending patterns is untested [unacknowledged].

**Key takeaways:**
- Transformers achieve 12-17% lower forecast errors than recurrent models.
- Gradient Boosting Machines offer strong accuracy with lower computational cost.
- Probabilistic forecasting quantifies uncertainty essential for risk-aware decisions.

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
- {'num': 'ARIMA-RNN hybrid achieved 15% MAE reduction on electricity load dataset compared to standalone models.'}
- {'num': 'ETSformer reduced inference latency by 37% versus Autoformer on ETT data while maintaining accuracy.'}
- {'num': 'PatchTST achieved 23% lower MSE than Informer with 60% less GPU memory consumption.'}
- Transformer variants with ProbSparse attention (Informer) reduce time complexity from O(L^2) to O(L log L).

**Supports Odin (direct justifications):**
- LSTM and GRU are suitable for long-sequence prediction tasks such as power load forecasting.
- Gated Recurrent Units offer lower computational cost than LSTM with comparable performance.
- Transformer variants like Informer achieve O(L log L) complexity for efficient long-sequence processing.

**Limitations / Contradictions for Odin:**
- The paper is a survey, not an empirical study; claims about model performance are aggregated from cited primary research.
- Comparative tables lack statistical significance testing across different datasets. [unacknowledged]
- Real-time performance metrics are discussed qualitatively without standardized benchmarks. [unacknowledged]

**Key takeaways:**
- LSTM and GRU solve vanishing gradients for medium-length sequence forecasting.
- Transformer variants achieve O(L log L) complexity for sequences over 1000 steps.
- PatchTST reduces GPU memory by 60% via sub-series tokenization.

---


## A Predictive Framework for Annual Financial Planning using Deep Learning Models
**Filename:** `IA--Singh-et_al_summarized.md`  
**Authors:** Singh, U.; Anand, U.; Singh, V. (2025)  
**ID:** `5e8f3a2b-1c4d-4e5f-8a9b-0c1d2e3f4a5b`  
**Odin Topics:** 6.A, 6.B, 12.A, 12.B  

**TLDR:** A deep learning framework using LSTM and GRU networks accurately forecasts annual expenses, outperforming traditional statistical methods like ARIMA and linear regression.

**Problem & Motivation:** Traditional forecasting methods (linear regression, ARIMA) fail to capture non-linear and dynamic patterns in financial data, limiting accuracy for long-term annual planning. Deep learning offers potential but lacks comprehensive evaluation for annual expense forecasting. This gap hinders proactive fiscal decision-making.

**Approach (summary):**
- Data from public government expenditure portals and synthetic augmentation using Gaussian/exponential distributions.
- Preprocessing: forward-fill missing values, min-max normalization, sliding window of 12 months to create sequences.
- Models: RNN baseline, LSTM, and GRU implemented in TensorFlow/Keras with grid search for hyperparameters.

**Key Findings (selected):**
- num: LSTM achieved MAE 1872.56, RMSE 2614.32, and MAPE 7.02%, the lowest among all models.
- num: GRU performed slightly worse with MAE 1950.45 and MAPE 7.48%, still outperforming RNN.
- num: RNN had MAE 2450.13 and MAPE 9.85%, showing gradient vanishing issues.
- Deep learning models capture long-term dependencies and seasonal variations better than ARIMA and linear regression.

**Supports Odin (direct justifications):**
- LSTM achieves 7.02% MAPE for annual expense forecasting, outperforming GRU and RNN.
- Deep learning models capture long-term dependencies and seasonal patterns better than ARIMA.
- Sliding window of 12 months is effective for annual expense prediction.

**Limitations / Contradictions for Odin:**
- Dependency on high-quality, complete datasets; incomplete or noisy data may hinder performance. [unacknowledged]
- Performance may vary with different time horizons (e.g., monthly or quarterly). [unacknowledged]
- Models could be sensitive to overfitting on smaller datasets if not carefully tuned.

**Key takeaways:**
- LSTM forecasts annual expenses with 7.02% MAPE, beating GRU and RNN.
- Deep learning outperforms ARIMA and linear regression for non-linear financial patterns.
- Sliding window of 12 months effectively captures seasonal spending cycles.

---


## AI: Proactive Workforce and Financial Guardians – Transforming Enterprise Systems from Reactive to Predictive
**Filename:** `IA--Pahuja_summarized.md`  
**Authors:** Pahuja, H. (2025)  
**ID:** `10.5281/zenodo.16628566`  
**Odin Topics:** 6.A, 6.B, 8.A, 13.A, 10.A, 10.B, 12.A  

**TLDR:** Proposes an architectural framework using Generative AI and agentic AI to transform reactive enterprise HR and financial systems into predictive, proactive platforms with digital assistants and financial guardianship.

**Problem & Motivation:** Traditional HR and FinTech platforms operate in silos, requiring manual intervention and providing retrospective insights. This fragmentation delays responses and impedes employee satisfaction and financial decision-making. Organizations need predictive AI systems that anticipate needs and deliver personalized guidance.

**Approach (summary):**
- The framework is derived from qualitative analysis of enterprise AI implementations across industries and assessment of performance metrics.
- Digital HR assistants leverage Generative AI, NLP, sentiment analysis, and privacy-preserving architectures for query resolution and onboarding.
- Agentic AI for financial services uses predictive analytics, reinforcement learning for micro-savings, and cash flow forecasting.

**Key Findings (selected):**
- Digital HR assistants reduce administrative burden and enable HR professionals to focus on strategic initiatives.
- Agentic AI with reinforcement learning generates more accumulated savings than fixed rule-based methodologies.
- Proactive financial interventions substantially reduce overdraft incidents and late payment penalties.
- Phased deployment models significantly outperform all-at-once approaches for AI implementation.

**Supports Odin (direct justifications):**
- Reinforcement learning-based savings automation generates more accumulated savings than fixed rule-based methods (Pandey & Awasthi, 2025).
- Proactive financial monitoring substantially reduces overdraft incidents and late payment penalties (Abikoye et al., 2024).
- Phased deployment with continuous ROI tracking improves AI implementation success rates (Bashir, 2024).

**Limitations / Contradictions for Odin:**
- No empirical validation of the proposed framework with real-world user data. [unacknowledged]
- Assumes enterprise-scale infrastructure not applicable to lightweight PFMS. [unacknowledged]
- Does not consider cultural or behavioral differences specific to Filipino users. [unacknowledged]

**Key takeaways:**
- Agentic AI enables micro-savings automation that adapts to user behavior.
- Predictive cash flow models can prevent overdraft fees through timely interventions.
- Phased deployment with ROI tracking increases AI adoption success.

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
- {'num': 'Multivariate VAR improves aggregate demand accuracy with ≈2.85% MAPE.'}
- {'num': 'Newspaper spend has near-zero marginal ROI; radio saturates quickly, TV saturates slowly.'}
- Optimal marketing spend lies below the SG&A ratio cap due to diminishing returns.
- {'num': 'Spending at the deterministic cap yields ≈40% violation probability under demand uncertainty.'}

**Supports Odin (direct justifications):**
- Optimal budgets may be below ratio caps due to diminishing returns.
- Spending at a deterministic cap yields 40% violation probability under demand uncertainty.
- Multivariate forecasting improves aggregate demand accuracy over univariate baselines.

**Limitations / Contradictions for Odin:**
- Macro PCE and Advertising datasets are not internally consistent; response-to-dollar normalization is arbitrary. [acknowledged]
- No adstock or carryover effects in marketing response, limiting dynamic budgeting. [acknowledged]
- Constraint calibration uses a single firm (Apple); results may not transfer to other sectors. [acknowledged]

**Key takeaways:**
- Optimal budgets often sit below ratio caps due to diminishing returns.
- VAR forecasting achieved 2.85% MAPE for aggregate demand proxy.
- Newspaper spend showed near-zero marginal ROI in the Advertising dataset.

---


## AI-Based Wealth Advisory System using Machine Learning and Predictive Analytics for Personalized Budget Planning
**Filename:** `IA--Bhavana-et_al_summarized.md`  
**Authors:** Bhavana, B. R.; Pavan, D.; Darshan, T. H. Guru (2025)  
**ID:** `10.15662/IJARCST.2025.0805004`  
**Odin Topics:** 3.A, 3.B, 6.A, 6.B, 7.A, 7.B, 7.C, 8.A, 8.B, 10.A, 10.B, 12.A, 12.B, 13.A  

**TLDR:** An AI wealth advisory system integrates classification, forecasting, anomaly detection, and explainable AI to deliver personalized budget planning, achieving 95% anomaly detection accuracy and a 22% improvement in savings.

**Problem & Motivation:** Most personal finance applications are reactive, limited to expense tracking without proactive wealth management or personalized AI-driven advice. A gap exists in consumer-centric financial advisory systems that are both predictive and interpretable, particularly for users with low financial literacy. This paper addresses the need for an intelligent system that combines forecasting, anomaly detection, and explainable recommendations to improve financial outcomes.

**Approach (summary):**
- Data sources include transaction logs, household expenditure surveys, and macroeconomic indicators from World Bank/IMF.
- Preprocessing involves cleaning, normalization, NLP-based categorization (BERT), anonymization, and KNN imputation.
- Classification uses XGBoost, Random Forest, and BERT; forecasting uses ARIMA, Prophet, LSTM, and Transformers in an ensemble.

**Key Findings (selected):**
- num: 95% anomaly detection accuracy achieved in pilot testing.
- num: 22% improvement in savings among participants.
- num: 78% of participants reported enhanced financial literacy.
- num: Expense classification achieved 91% F1-score.

**Supports Odin (direct justifications):**
- AI-based wealth advisory systems can achieve 95% anomaly detection accuracy on personal transaction data.
- Explainable AI methods like SHAP and LIME enhance user trust in personal finance systems.
- Personalized budget recommendations using contextual bandits achieve 41% user adoption rate.

**Limitations / Contradictions for Odin:**
- Small pilot sample (100 users) limits statistical power and generalizability. [unacknowledged]
- Paper does not specify the exact composition of transaction datasets, raising reproducibility concerns. [unacknowledged]
- Potential bias in recommendation algorithms mentioned but not empirically mitigated. [acknowledged]

**Key takeaways:**
- Anomaly detection accuracy reached 95% in pilot testing.
- Savings improved by 22% among system users.
- Expense classification achieved 91% F1-score.

---


## Machine Learning in Financial Risk and Behavior Analysis: Predictive Insights on Bankruptcy, Fraud, and Consumer Trends in the USA
**Filename:** `IA--Begum_summarized.md`  
**Authors:** Begum, M. (2025)  
**ID:** `f47ac10b-58cc-4372-a567-0e02b2c3d479`  
**Odin Topics:** 5.A, 5.C, 6.A, 6.B, 8.A, 8.B  

**TLDR:** Evaluates machine learning models for bankruptcy prediction, fraud detection, and consumer spending forecasting, finding gradient boosting and LSTM outperform traditional methods.

**Problem & Motivation:** Traditional financial risk assessment methods struggle to capture nonlinear patterns, behavioral dynamics, and real-time anomalies. Machine learning offers improvements but faces challenges in generalizability, interpretability, and real-time adaptability. This paper proposes a unified ML framework to address these gaps across bankruptcy, fraud, and consumer behavior domains.

**Approach (summary):**
- For bankruptcy prediction, six models are trained: Logistic Regression, Random Forest, Gradient Boosting (XGBoost, LightGBM), SVM, ANN, and LSTM on financial ratios from SEC EDGAR and Moody's data.
- Fraud detection uses unsupervised Isolation Forest plus supervised classifiers (Logistic Regression, Random Forest, XGBoost) with SMOTE, a stacking ensemble, and a GRU-based RNN for sequential patterns.
- Consumer behavior analysis applies K-Means and DBSCAN clustering for customer segmentation, and ARIMA with LSTM for time-series forecasting of spending.

**Key Findings (selected):**
- num: XGBoost achieves the highest AUC (0.93) for bankruptcy prediction, followed by LSTM (0.92) and LightGBM (0.91).
- num: Stacking ensemble for fraud detection yields F1 of 0.89 and precision of 0.91, outperforming individual classifiers.
- num: LSTM reduces MAE to 2.8 and RMSE to 3.3 for consumer spending forecasting, compared to ARIMA's MAE of 4.2 and RMSE of 5.1.
- num: K-Means clustering produces a silhouette score of 0.68, indicating well-separated customer segments.

**Supports Odin (direct justifications):**
- LSTM achieves lower MAE (2.8) than ARIMA (4.2) for spending forecasting in consumer behavior.
- Stacking ensemble for fraud detection yields F1 of 0.89 and precision of 0.91.
- XGBoost reaches 0.93 AUC for bankruptcy prediction, demonstrating gradient boosting's strength on financial ratios.

**Limitations / Contradictions for Odin:**
- Models were trained on static historical datasets, not on live data streams.
- Real-world deployment would require continuous retraining and monitoring for evolving financial conditions.
- The study does not incorporate macroeconomic indicators or unstructured data (e.g., news, social media).

**Key takeaways:**
- XGBoost achieves 0.93 AUC for bankruptcy prediction.
- Stacking ensemble reaches 0.89 F1 in fraud detection.
- LSTM reduces MAE from 4.2 to 2.8 compared to ARIMA.

---


## A Survey of Machine Learning Methods for Time Series Prediction
**Filename:** `IA--Hall-&-Rasheed_summarized.md`  
**Authors:** Hall, T.; Rasheed, K. (2025)  
**ID:** `10.3390/app15115957`  
**Odin Topics:** 6.A, 6.B, 8.A, 8.B, 12.A, 12.B  

**TLDR:** A survey of 79 papers comparing tree-based and deep learning methods for time series prediction finds that LightGBM, LSTM, and CatBoost perform best, with tree-based methods offering greater computational efficiency.

**Problem & Motivation:** Existing surveys cannot draw meaningful comparisons between forecasting models due to heterogeneous experimental setups across independent studies. This gap prevents robust conclusions about relative strengths and weaknesses of tree-based versus deep learning approaches. This survey addresses the gap by exclusively reviewing studies that compare both methodologies using identical datasets.

**Approach (summary):**
- Searched Web of Science with query combining TBML and DL terms, yielding 589 papers from 2017-2024.
- Selected top 100 most-cited papers, then applied inclusion criteria requiring direct comparison of TBML and DL on identical datasets.
- Included 79 papers with balanced yearly representation from 2020 to 2024.

**Key Findings (selected):**
- num: TBML models achieve best performance in 54.55% of tasks (FPA) with WRA 0.6910, while DL models achieve 52.70% FPA with WRA 0.6486.
- num: RNN models (LSTM, GRU) are best in 61.36% of studies with WRA 0.7330, followed by SPTB models (XGBoost, LightGBM, CatBoost) at 50% FPA and 0.6328 WRA.
- num: CatBoost achieves highest individual FPA and WRA, but LSTM shows more robust performance (58.97% FPA, 0.7222 WRA over 39 evaluations).
- num: TBML models are on average 126,935% faster to train than DL models, with median advantage of 5,603%.

**Supports Odin (direct justifications):**
- LightGBM and LSTM are among the best-performing algorithms for time series forecasting tasks.
- Tree-based methods are significantly more computationally efficient than deep learning methods (median 5603% faster training).
- On large datasets (>200k samples), tree-based models outperform deep learning models.

**Limitations / Contradictions for Odin:**
- The analysis of task categories has relatively small sample sizes (3.85% to 21.8% of papers), limiting statistical certainty.
- Transformer-based architectures are underrepresented with only five papers, limiting generalizability.
- The paper does not address real-time or streaming time series prediction scenarios. [unacknowledged]

**Key takeaways:**
- LightGBM and LSTM are top performers for time series forecasting.
- Tree-based methods train 5603% faster on average than deep learning.
- Dataset size determines best model: small data favors RNNs, large data favors TBML.

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
- {'Categorized forecasting models into four groups': 'traditional statistical, machine learning, deep learning, and hybrid approaches.'}

**Key Findings (selected):**
- Traditional statistical models (ARIMA, Holt-Winters) remain relevant for stable, seasonal demand but fail under nonlinearity and promotional spikes.
- {'num': 'Machine learning models (random forests, gradient boosting) improve forecast accuracy by up to 20% over statistical methods in high‑SKU environments.'}
- Deep learning models (LSTM, GRU, CNN) capture long‑range dependencies and outperform other methods for erratic and intermittent demand.
- Hybrid ARIMA‑ML/DL models balance interpretability and accuracy, reducing forecasting error during flash sales and disruptions.

**Supports Odin (direct justifications):**
- Machine learning models improve forecasting accuracy by up to 20% over statistical methods in volatile demand environments.
- Integration of external data like weather and social media sentiment enhances demand forecast precision.
- Hybrid ARIMA‑ML models balance interpretability and accuracy for short‑term forecasts.

**Limitations / Contradictions for Odin:**
- The review only includes English‑language peer‑reviewed studies, potentially missing relevant industry reports. [unacknowledged]
- Performance comparisons across studies use different datasets and evaluation protocols, making direct aggregation difficult. [acknowledged in discussion]
- The paper does not address real‑time deployment constraints or inference latency for forecasting models.

**Key takeaways:**
- Forecasting accuracy can reduce inventory costs by up to 25%.
- Machine learning models beat statistical methods by 20% in volatile settings.
- Deep learning captures long‑term spending patterns better than ARIMA.

---


## Mental Accounting Through Two-stage Budgeting Under Bounded Rationality
**Filename:** `IA--Pretnar-et_al_summarized.md`  
**Authors:** Pretnar, N.; Olivola, C. Y.; Montgomery, A. (2025)  
**ID:** `10.21203/rs.3.rs-7730348/v1`  
**Odin Topics:** 5.A, 5.C, 6.A, 6.B, 7.A, 13.A, 13.B  

**TLDR:** A model of two-stage budgeting with cognitive constraints shows consumers exhibit heterogeneous bounded rationality, updating only half of budgets weekly, with mental accounting affecting spending and savings.

**Problem & Motivation:** Classical two-stage budgeting assumes perfect fungibility and ex-post budget adherence. Behavioral evidence suggests consumers use mental accounting and sticky budgets, but field evidence is lacking. This paper quantifies how cognitive constraints and budget rigidities explain observed expenditure patterns.

**Approach (summary):**
- Builds a dynamic model with planner/doer structure, mental accounting state variable, and sparse budget updates.
- Uses weekly agent-level expenditure data from 2,509 low-income prepaid debit card users spanning September 2013 to January 2016.
- Estimates structural parameters via Bayesian MCMC with latent change-point inference, sampling over four million parameters.

**Key Findings (selected):**
- num: Consumers update only 2.48 budgets per week on average (out of 4 categories) in baseline, 2.11 with $1 numeracy threshold.
- num: 68% of consumers do not benefit from forced weekly full budget updates; 3.3% go bankrupt under forced attention in $1-threshold model.
- Ex-ante most consumers (79%) are budget prioritizers (mental accounting), but ex-post a plurality (43-47%) are spendthrifts who increase spending regardless of prior over/under-spending.
- {'Heterogeneous rationality': 'most consumers are neither fully rational (always update all budgets) nor fully bounded (never update).'}

**Supports Odin (direct justifications):**
- Consumers update only a subset of budgets each period due to cognitive constraints.
- Forcing full budget attention reduces welfare for 68% of consumers.
- Bankrupt consumers exhibit stickier budgets and planning fallacy syndrome.

**Limitations / Contradictions for Odin:**
- Data limited to low-income prepaid debit card users, not generalizable. [unacknowledged]
- Model assumes strong separability and Stone-Geary utility, potentially unrealistic. [unacknowledged]
- Latent budgeting inference is model-dependent and lacks direct validation. [acknowledged]

**Key takeaways:**
- 2.11 average weekly budget updates under $1 numeracy threshold.
- 68% of users worse off with full budget attention.
- Bankrupt consumers have only 1.25 updates per week.

---


## A Comparative Review of Electricity Load Forecasting Methods Across Temporal Horizons
**Filename:** `IA--Saeedian_summarized.md`  
**Authors:** Saeedian, Z. (2024)  
**ID:** `b7c4e2d1-9a8f-4c3b-8e2d-1f5a7c9b3e6d`  
**Odin Topics:** 6.A, 6.B, 12.A, 12.B  

**TLDR:** Reviews electricity load forecasting methods across short, medium, and long horizons, comparing statistical, machine learning, deep learning, and hybrid models for temporal pattern capture.

**Problem & Motivation:** Accurate load forecasting is critical for grid stability and renewable integration. Existing methods face challenges with nonlinearity, uncertainty, and data availability. A structured comparison across time horizons is missing.

**Approach (summary):**
- Reviews literature on short-term (minutes to 1 week), medium-term (1 week to 1 month), and long-term (beyond 1 month) forecasting.
- Categorizes methods into statistical (ARIMA, SARIMA, regression), machine learning (SVR, tree-based), deep learning (LSTM, Transformer), and hybrid models.
- Evaluates models based on accuracy, interpretability, computational cost, and data requirements.

**Key Findings (selected):**
- num: LSTM achieved MAPE of 2.42% for Turkish electricity consumption, outperforming SARIMA.
- num: XGBoost achieved lowest MAPE of 1.88% for short-term forecasting in Algeria.
- num: Hybrid ETS+RD-LSTM reduced MAPE by up to 25% over standalone models.
- Statistical models like ARIMA work for stable seasonal patterns but fail with nonlinearity.

**Supports Odin (direct justifications):**
- LSTM achieves higher accuracy than SARIMA for electricity consumption forecasting.
- XGBoost outperforms other machine learning models for short-term load forecasting with MAPE of 1.88%.
- Hybrid models combining statistical and deep learning methods reduce forecasting error by up to 25%.

**Limitations / Contradictions for Odin:**
- Based on published literature and benchmark datasets, real-world constraints not modeled.
- Hybrid model performance varies significantly across datasets and implementations.
- Probabilistic forecasting methods were only lightly discussed.

**Key takeaways:**
- LSTM achieves 2.42% MAPE for electricity forecasting.
- XGBoost outperforms other models with 1.88% MAPE.
- Hybrid models reduce error by up to 25%.

---


## Recurrent Neural Networks: A Comprehensive Review of Architectures, Variants, and Applications
**Filename:** `IA--Mienye-et_al-2024_summarized.md`  
**Authors:** Mienye, I. D.; Swart, T. G.; Obaido, G. (2024)  
**ID:** `10.3390/info15090517`  
**Odin Topics:** 3.A, 6.A, 6.B, 8.A, 8.B, 12.B  

**TLDR:** Recurrent neural networks and their variants enable effective processing of sequential data for applications including time series forecasting, anomaly detection, and natural language processing.

**Problem & Motivation:** Previous reviews of RNNs do not fully capture the latest advancements in architectures and applications across a broad range of fields. A comprehensive review is needed to assess theoretical advancements and practical implementations to help shape future research.

**Approach (summary):**
- Surveys foundational RNN architectures including basic RNN, LSTM, and GRU.
- Reviews advanced variants such as bidirectional LSTM, peephole LSTM, echo state networks, and independently recurrent neural networks.
- Examines hybrid models combining RNNs with CNNs, attention mechanisms, and transformers.

**Key Findings (selected):**
- num: LSTM and GRU effectively mitigate vanishing gradient problems in sequential modeling.
- num: Bidirectional RNNs improve context understanding by processing sequences in both directions.
- Hybrid CNN-RNN models outperform standalone RNNs in video analysis and time series forecasting.
- Attention mechanisms integrated with RNNs enhance long-range dependency modeling.

**Supports Odin (direct justifications):**
- Bidirectional RNNs improve context understanding in sequential classification tasks.
- LSTM networks effectively capture long-term dependencies in time series data.
- Attention-enhanced RNNs outperform standard RNNs in anomaly detection.

**Limitations / Contradictions for Odin:**
- Training RNNs on long sequences remains computationally intensive compared to transformer architectures.
- RNNs are often perceived as black-box models with limited interpretability, a challenge acknowledged but not solved.
- Bias in training data can lead to unfair predictions; the review notes this but offers no mitigation for financial applications.

**Key takeaways:**
- LSTM and GRU solve vanishing gradient problems in sequential data.
- Bidirectional processing captures both past and future context.
- Hybrid CNN-RNN models excel at spatiotemporal forecasting.

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
- num: Dashboard initial load 420ms to first meaningful content.
- num: Receipt scan average 2.1 seconds with >92% accuracy (citing prior research).
- num: Live portfolio fetch for 10 holdings in 1.4 seconds.
- num: EMI schedule creation for 60 months takes 180ms DB round-trip.

**Supports Odin (direct justifications):**
- Multi-modal transformer models like Gemini achieve >92% OCR accuracy for receipts.
- LSTM networks can forecast cash flow trajectories in personal finance apps.
- LLAMA 3.1 70B with structured JSON prompts reduces hallucination for investment recommendations.

**Limitations / Contradictions for Odin:**
- Geographical and regulatory focus on India limits external validity. [unacknowledged]
- Dependency on third-party APIs (Yahoo Finance, MFAPI.in) introduces failure risk. [acknowledged]
- Requires 3 months of user financial context for AI to provide accurate advice (cold-start). [acknowledged]

**Key takeaways:**
- Receipt scanner achieves sub-2.1s processing with >92% accuracy.
- LLAMA 3.1 8B delivers sub-200ms intent classification.
- Dashboard initial load at 420ms using SSR and Suspense.

---


## A Survey of Large Language Models for Financial Applications: Progress, Prospects and Challenges
**Filename:** `IA--Nie-et_al_summarized.md`  
**Authors:** Nie, Y.; Kong, Y.; Dong, X.; Mulvey, J. M.; Poor, H. V.; Wen, Q.; Zohren, S. (2024)  
**ID:** `arxiv:2406.11093`  
**Odin Topics:** 5.A, 6.A, 6.B, 7.A, 7.B, 8.A, 8.B, 10.A, 10.B, 12.A, 12.B  

**TLDR:** A survey of large language models applied to finance, covering linguistic tasks, sentiment analysis, time series forecasting, financial reasoning, and agent-based modeling, along with challenges and benchmarks.

**Problem & Motivation:** Financial applications require processing vast unstructured data and complex reasoning. Traditional deep learning methods struggle with long-term dependencies and context understanding. LLMs offer advanced contextual understanding and transfer learning, but a comprehensive overview of their financial applications and challenges is lacking.

**Approach (summary):**
- The survey categorizes existing literature into key application areas: linguistic tasks, sentiment analysis, financial time series analysis, financial reasoning, and agent-based modeling.
- It analyzes domain-specific LLMs (FinBERT, BloombergGPT, etc.) and compares zero-shot vs fine-tuning approaches.
- The paper compiles datasets, benchmarks, and code resources for financial LLM research.

**Key Findings (selected):**
- num: ChatGPT can achieve a monthly three-factor alpha of up to 3% when generating portfolios from policy news.
- FinBERT shows enhanced resilience against adversarial attacks compared to keyword-based sentiment methods.
- LLM-based agents with layered memory (FINMEM) improve trading decisions in volatile financial environments.
- Zero-shot LLMs can forecast time series without explicit training by tokenizing numerical data appropriately.

**Supports Odin (direct justifications):**
- LLMs can forecast stock returns from news headlines with higher Sharpe ratios than traditional models (Lopez-Lira & Tang, 2023).
- Instruction-tuned LLMs enhance financial sentiment analysis numerical sensitivity (Zhang et al., 2023).
- Multi-agent LLM frameworks improve anomaly detection efficiency in financial markets (Park, 2024).

**Limitations / Contradictions for Odin:**
- Lookahead bias in backtesting financial LLMs requires careful data anonymization.
- High computational cost and inference speed limit real-time deployment.
- Lack of standardized evaluation benchmarks for LLM-based trading strategies.

**Key takeaways:**
- LLMs can achieve 3% monthly alpha in portfolio generation from policy news.
- Zero-shot LLMs forecast time series without task-specific training.
- Multi-agent LLM systems enhance anomaly detection and sentiment analysis.

---


## Forecasting the Future: A Comprehensive Review of Time Series Prediction Techniques
**Filename:** `IA--Kolambe-&-Arora_summarized.md`  
**Authors:** Kolambe, M.; Arora, S. (2024)  
**ID:** `3c5b4f2a-8e6d-4c9a-b1e3-9f7d2c8a5e1b`  
**Odin Topics:** 6.A, 6.B, 12.A, 12.B, 8.A  

**TLDR:** From classical ARIMA to deep learning LSTM, time series forecasting techniques are comprehensively reviewed, including hybrid methods, challenges, and evaluation metrics.

**Problem & Motivation:** Time series forecasting is critical for finance, economics, weather, and industrial processes. Traditional methods struggle with complex patterns and dynamics in real-world data. This review synthesizes key advancements and guides method selection.

**Approach (summary):**
- Surveys classical methods including ARIMA, exponential smoothing, Prophet, and STL decomposition.
- Covers machine learning approaches: regression, decision trees, random forests, SVM, and gradient boosting.
- Reviews deep learning techniques: RNN, LSTM, GRU, and Transformer-based models.

**Key Findings (selected):**
- Classical methods like ARIMA work for simple trends and seasonality but fail on complex patterns.
- LSTM and GRU effectively capture long-term dependencies in time series data.
- Hybrid methods that combine decomposition with deep learning improve forecast accuracy.
- Noisy data, outliers, and missing values remain major challenges for forecasting models.

**Supports Odin (direct justifications):**
- Classical methods like ARIMA fail on complex patterns, motivating deep learning for spending forecasting.
- LSTM networks effectively capture long-term dependencies in sequential data.
- Hybrid models combining decomposition and neural networks improve forecast accuracy.

**Limitations / Contradictions for Odin:**
- Lacks empirical validation of any specific forecasting method on real-world datasets. [unacknowledged]
- Does not address computational efficiency or latency, which are critical for real-time personal finance applications. [unacknowledged]

**Key takeaways:**
- Time series forecasting methods range from classical ARIMA to deep learning LSTM.
- Hybrid models often outperform pure classical or deep learning approaches.
- MAE and RMSE are essential for evaluating forecast accuracy.

---


## The Evolution of Recurrent Neural Networks in Handling Long-Term Dependencies in Sequential Data
**Filename:** `IA--Ramachandran_summarized.md`  
**Authors:** Ramachandran, K. K. (2024)  
**ID:** `a1b2c3d4-e5f6-4789-abc0-def123456789`  
**Odin Topics:** 6.A, 6.B  

**TLDR:** Recurrent neural networks evolved from vanilla RNNs to LSTM, GRU, attention, and transformers to effectively capture long-term dependencies in sequential data such as time series.

**Problem & Motivation:** Vanilla RNNs struggle to retain information over long sequences due to vanishing and exploding gradients. This limitation hinders performance in tasks like time-series forecasting and language modeling. Advanced architectures like LSTM and GRU were developed to overcome these issues.

**Approach (summary):**
- Reviews RNN evolution from Elman (1990) to LSTMs (1997), GRUs (2014), attention mechanisms, and transformers (2017).
- Analyzes vanishing/exploding gradient problems and how gating mechanisms in LSTM/GRU mitigate them.
- Compares LSTM and GRU architectures on parameters, gates, and computational efficiency.

**Key Findings (selected):**
- LSTM and GRU architectures effectively mitigate the vanishing gradient problem through gating mechanisms.
- GRUs offer comparable performance to LSTMs with fewer parameters and faster training.
- Transformer models using self-attention outperform RNNs on very long sequences due to parallel computation.
- Vanilla RNNs show performance degradation as sequence length increases (Graph 1).

**Supports Odin (direct justifications):**
- LSTM networks effectively handle long-term dependencies in time-series forecasting (Section 5.2).
- GRUs provide comparable performance to LSTMs with faster training (Table 1).
- Vanilla RNNs degrade in accuracy over long sequences (Graph 1).

**Limitations / Contradictions for Odin:**
- Focuses on architectural review without empirical comparison on standardized financial benchmarks [unacknowledged].
- Does not address computational cost or model size for mobile deployment [unacknowledged].
- No quantitative performance metrics (e.g., error rates) are reported for specific tasks [unacknowledged].

**Key takeaways:**
- LSTM uses three gating mechanisms to control memory flow.
- GRU has two gates and trains faster than LSTM.
- Vanilla RNNs lose accuracy beyond short time steps.

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

**Supports Odin (direct justifications):**
- Isolation Forest can identify atypical financial transactions by isolating deviations from normal behavior.
- Weighted combination of ARIMA and LSTM improves budget forecast accuracy over either model alone.
- LLMs can generate personalized financial recommendations that adapt to user income level and risk tolerance.

**Limitations / Contradictions for Odin:**
- No quantitative validation of forecasting or anomaly detection accuracy. [unacknowledged]
- The system's LLM component is described only conceptually; no ablation study or comparison with rule-based baselines. [unacknowledged]
- Ethical claims are not operationalized or measured (e.g., how to verify user autonomy). [unacknowledged]

**Key takeaways:**
- Anomaly detection uses Isolation Forest with path length scoring.
- Forecasts combine ARIMA for short-term and LSTM for long-term trends.
- Large language model generates personalized financial advice from transaction and forecast data.

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
- num: Transformer achieved best performance on ETTm2 with MSE=3.418, MAE=1.399.
- num: LSTM achieved minimum MAE on Electricity (1.848) and Traffic (0.020).
- num: GRU achieved minimum MSE on Electricity (19.524) and Traffic (0.00110).
- num: RNN achieved best performance on Weather with MSE=0.007, MAE=0.060.

**Supports Odin (direct justifications):**
- Deep learning models can automatically extract temporal features from time series data.
- Transformer self-attention captures long-range dependencies better than RNNs.
- No single model dominates all datasets; model selection depends on data characteristics.

**Limitations / Contradictions for Odin:**
- Survey format; no novel algorithm proposed.
- Univariate experiments may not generalize to multivariate spending data [unacknowledged].
- Excluded datasets with insufficient periodicity, limiting generalizability.

**Key takeaways:**
- Transformer achieved lowest MAE (1.399) on ETTm2 dataset.
- No single deep learning model dominates all time series forecasting tasks.
- Deep learning automates feature extraction but requires large training data.

---


## Single and Multiple Separate LSTM Neural Networks for Multiple Output Feature Purchase Prediction
**Filename:** `IA--Ciric-et_al_summarized.md`  
**Authors:** Ciric, M.; Predic, B.; Stojanovic, D.; Ciric, I. (2023)  
**ID:** `10.3390/electronics12122616`  
**Odin Topics:** 3.A, 6.A, 6.B, 12.A, 12.B  

**TLDR:** Compares single multivariate LSTM against separate LSTM networks for predicting next purchase day and product category from customer transaction data, finding separate networks better for category prediction and single multivariate better for timing.

**Problem & Motivation:** Predicting both the timing and product category of a customer's next purchase from historical transaction data is challenging because input features are multidimensional and outputs are heterogeneous. Existing methods often treat these predictions separately or use single models that underperform on one of the tasks. A systematic comparison of single versus multiple dedicated LSTM architectures for this multi-output problem was missing.

**Approach (summary):**
- Data from a medical device vendor: 7.5M transactions, ~10,100 customers with ≥4 orders, anonymized.
- Product categories defined using GPI (generic product identifier) with 100 drug groups (2‑character tiers) or 16 aggregated categories.
- Input features: time series of days between consecutive purchases and multi-hot encoded vectors of drug groups/categories present in each purchase.

**Key Findings (selected):**
- num: Dedicated LSTM network for drug group/category prediction improved recall for realized purchases by 15–50% across all datasets.
- Single multivariate LSTM network produced better results for next purchase day prediction than a dedicated network.
- Using all 100 drug groups gave higher metrics than using 16 aggregated categories for category prediction.
- For 100+ purchases dataset, a dedicated LSTM correctly predicted at least one purchased drug category for 95.7% of customers.

**Supports Odin (direct justifications):**
- A dedicated LSTM network for spending category prediction achieves 15-50% higher recall than a joint model.
- Single multivariate LSTM for next purchase day prediction outperforms a dedicated day-only network.
- Using fine-grained category labels (100 groups) yields better prediction than aggregated categories (16 groups).

**Limitations / Contradictions for Odin:**
- GPI classification system is specific to medical drugs; not generalizable to all expense categories without adaptation.
- Data comes from B2B medical supply, not young professionals' personal finance. [unacknowledged]
- Does not compare against traditional statistical baselines (ARIMA, exponential smoothing). [unacknowledged]

**Key takeaways:**
- Dedicated LSTM for category prediction improves recall by 15-50% over a joint model.
- Single multivariate LSTM is better for predicting timing of next purchase.
- Fine-grained product categories (100 groups) predict better than aggregated ones.

---


## An Overview of Forecasting Methods for Monthly Electricity Consumption
**Filename:** `IA--Krstev-et_al_summarized.md`  
**Authors:** Krstev, S.; Forcan, J.; Krneta, D. (2023)  
**ID:** `10.17559/TV-20220430111309`  
**Odin Topics:** 6.A, 6.B, 12.A  

**TLDR:** Compares twelve forecasting methods for monthly electricity consumption, finding neural network autoregression (MAPE 2.67%) outperforms classical time series and machine learning methods.

**Problem & Motivation:** Mid-term electricity consumption forecasting is crucial for energy companies but receives less research attention than short-term forecasting. The paper addresses the gap by systematically comparing classical statistical methods against modern machine learning approaches for monthly data. It also investigates whether machine learning provides equal accuracy to traditional time series methods when data is limited.

**Approach (summary):**
- Data from DSO in Bosnia and Herzegovina: monthly consumption (Jan 2000 – Mar 2020), 228 training months, 15 test months.
- Classical methods: seasonal naïve, ARIMA(1,0,1)(1,1,1), ETS(A,N,A), basic structural model with Kalman filter.
- Machine learning methods: linear regression, elastic net, KNN, random forest, XGBM, linear SVM, radial SVM, and neural network autoregression NNAR(3,1,6).

**Key Findings (selected):**
- NNAR(3,1,6) achieved the lowest MAPE of 2.67%.
- num: ETS(A,N,A) gave MAPE 3.28%, ARIMA 3.36%, BSM 3.87%, seasonal naïve 4.16%.
- num: Among machine learning methods, PCA+KNN performed best with MAPE 4.38%.
- Classical time series methods generally outperformed most machine learning methods due to small sample size.

**Supports Odin (direct justifications):**
- Neural network autoregression achieves 2.67% MAPE for monthly time series forecasting.
- ETS and ARIMA produce MAPE below 4% on monthly consumption data with 228 training points.
- Classical statistical methods are more accurate than machine learning when sample size is small.

**Limitations / Contradictions for Odin:**
- Results based on a single utility’s data; may not generalize to other regions or consumption types.
- No multivariate or exogenous variables (e.g., weather, price) were included.
- The paper does not compare against state-of-the-art deep learning (e.g., LSTM) beyond basic NNAR.

**Key takeaways:**
- NNAR achieved the lowest MAPE of 2.67% for monthly forecasting.
- Classical time series methods outperformed most machine learning methods on small datasets.
- MAPE below 4% is achievable with ETS and ARIMA for mid-term forecasting.

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
- {'Organized findings by application domain': 'finance (bitcoin, stocks), healthcare (COVID-19 cases), weather (wind, drought), utilities (energy, water), and network traffic.'}
- Extracted performance metrics including RMSE, MAPE, MAE, MSE, R2, NSE from each comparative study.

**Key Findings (selected):**
- Machine learning and deep learning models generally outperform ARIMA in time series forecasting across most applications reviewed.
- {'num': 'Deep learning models (LSTM, GRU) achieved RMSE values up to 40 times smaller than ARIMA for COVID-19 case forecasting in several countries (Arun Kumar et al., 2022).'}
- {'num': "ARIMA outperforms machine learning models for small datasets, limited value ranges, or strongly linear and seasonal univariate series (e.g., drought forecasting with R2 >0.9 vs. SVM's 0.83)."}
- Hybrid models combining ARIMA with machine learning (e.g., ARIMA-SVM, ARIMA-NARNN, ARIMA-CNN) consistently outperform both individual approaches.

**Supports Odin (direct justifications):**
- Machine learning models generally provide more accurate time series forecasts than ARIMA for non-linear spending data.
- Hybrid ARIMA-ML models consistently outperform pure ARIMA or pure ML models in forecasting tasks.
- ARIMA is preferable for small datasets or when spending patterns are linear and seasonal.

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
- num: CNN with direct multi-step procedure improved prediction accuracy by 22.6% over seasonal ARIMAX for building load forecasting.
- num: Graph Deviation Network achieved 54% better F-measure than the next best baseline for anomaly detection in water treatment systems.
- num: LSTM achieved mean absolute percentage error of 4.82% for traffic flow forecasting versus 20.97% for ARIMA and 9.06% for BPNN.
- num: Empirical mode decomposition preprocessing improved gesture classification accuracy from 94.22% to 99.73% using CNN.

**Supports Odin (direct justifications):**
- CNN with direct multi-step procedure can improve forecasting accuracy by 22.6% over ARIMAX.
- No single deep learning method fits all time series anomaly detection tasks.
- Simple models with feature engineering can outperform deep learning without preprocessing.

**Limitations / Contradictions for Odin:**
- Survey primarily synthesizes existing literature without new empirical experiments. [unacknowledged]
- Focus on sensor time series limits generalizability to financial transaction sequences. [unacknowledged]
- Computational cost of continual learning on mobile devices is not quantitatively assessed. [unacknowledged]

**Key takeaways:**
- LSTM achieved 4.82% MAPE for traffic forecasting versus 20.97% for ARIMA.
- Empirical mode decomposition preprocessing raised accuracy from 94.22% to 99.73%.
- No single deep learning method works for all anomaly detection tasks.

---


## Impact of Mental Representation on Consumer Behaviors: Implications for Mental Budgeting and Prediction Algorithm Preferences
**Filename:** `I--Fei_summarized.md`  
**Authors:** Fei, L. (2023)  
**ID:** `123e4567-e89b-12d3-a456-426614174000`  
**Odin Topics:** 3.A, 5.A, 6.B, 7.A, 7.C, 12.A  

**TLDR:** Mental representation of expenditures forms a hierarchical taxonomy that predicts spending adjustment based on taxonomic distance, and people prefer prediction algorithms that replicate the event being predicted.

**Problem & Motivation:** Consumers often deviate from budgets, but existing budgeting theories assume single-level categories and cannot explain how people adjust spending across related items. Understanding how mental representation drives spending decisions and algorithm preferences is crucial for improving personal finance systems.

**Approach (summary):**
- Study 1a used successive pile-sort with 27 MTurk participants to elicit hierarchical taxonomies of 38 common expenditures, recovering consensus via Cultural Consensus Model.
- Study 1b tested stability of taxonomies over three months with 50 participants.
- Studies 2a-2c measured self-reported spending adjustment and substitutability/complementarity ratings to isolate taxonomic distance effects.

**Key Findings (selected):**
- num: 27 participants showed consensus in hierarchical expenditure representations (first latent root ratio > 3:1).
- num: Taxonomic distance significantly predicted spending adjustment, with closer items adjusted 31% more than distant items (Study 2a).
- Taxonomic distance effects persisted even after controlling for substitutability and complementarity (Study 2c).
- num: In grocery data, a sale on an item increased spending on taxonomically close items by 12% compared to distant items.

**Supports Odin (direct justifications):**
- Overspending on an item leads to greater spending reduction on taxonomically close items than distant items.
- Users prefer prediction algorithms that replicate the event's generative process over statistical models with equal accuracy.
- Hierarchical expenditure taxonomies are consensual and stable over time, enabling personalization from cold start.

**Limitations / Contradictions for Odin:**
- Lab studies use hypothetical scenarios; real behavior may differ. [unacknowledged]
- Grocery data analysis cannot confirm individual budget tracking; assumes average effects.
- Sample sizes in pile-sort studies (N=27, N=50) are modest for consensus modeling.

**Key takeaways:**
- Taxonomic distance predicts spending adjustment more than substitutability alone.
- Consumers share a consensual hierarchical representation of common expenditures.
- People prefer prediction algorithms that replicate the event's generative process.

---


## An Insight of Deep Learning Based Demand Forecasting in Smart Grids
**Filename:** `IA--Aguiar-Perez-&-Perez-Juarez_summarized.md`  
**Authors:** Aguiar-Pérez, J. M.; Pérez-Juárez, M. Á. (2023)  
**ID:** `10.3390/s23031467`  
**Odin Topics:** 6.A, 6.B  

**TLDR:** Deep learning models, especially LSTM and CNN, effectively forecast electricity demand in smart grids using large datasets.

**Problem & Motivation:** Smart grids generate massive data requiring modern data-driven forecasting. Traditional electrical grids did not consider demand forecasting, leading to inefficiencies. Balancing supply and demand is critical for power system efficiency.

**Approach (summary):**
- Literature review of deep learning for demand forecasting in smart grids.
- Searched scientific databases (Scopus, SpringerLink, IEEE Xplore, etc.) using keywords like “Deep Learning”, “LSTM”, “load forecasting”.
- Limited search to last 6 years and reviewed papers from key journals and conferences.

**Key Findings (selected):**
- {'num': 'LSTM achieved MAPE of 1.71% for 30-minute predictions and 5.1% for 1-week predictions [82].'}
- {'num': 'Pyramid-CNN improved MAPE up to 10% over LSTM for individual household demand [85].'}
- {'num': 'CNN-based method achieved MAE of 0.514% versus SVM’s 14.32% for demand forecasting [101].'}
- {'num': 'LSTM reduced RMSE by 19.5% compared to ARIMA for smart home load forecasting [120].'}

**Supports Odin (direct justifications):**
- LSTM networks significantly improve short-term forecasting accuracy compared to ARIMA.
- Combining CNN with LSTM outperforms isolated models for multivariate time series.
- Deep learning requires large datasets to achieve performance gains over conventional methods.

**Limitations / Contradictions for Odin:**
- Real testbeds with high-quality data are not common. [unacknowledged]
- Most researchers focused on short-term forecasting; long-term forecasting less explored.
- Limited discussion of training/validation split and data cleaning methodology in reviewed papers.

**Key takeaways:**
- LSTM achieved MAPE of 1.71% for 30-minute energy demand forecasts.
- Combining CNN and LSTM improves prediction accuracy over isolated models.
- Deep learning requires large datasets to outperform ARIMA and SVM.

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
- num: SVR-LSTM hybrid achieved correlation coefficient 0.9901, outperforming traditional SVR and LSTM.
- num: CNNGRU with attention mechanism reached 92.06% accuracy in small-range load prediction and reduced prediction time by 75%.
- num: Principal component analysis reduced 12 weather factors to 3 dimensions with 93.93% cumulative contribution rate.
- Bottom-up forecasting by aggregating appliance-level predictions improves accuracy over direct household-level forecasting.

**Supports Odin (direct justifications):**
- LSTM networks effectively capture long-term dependencies in sequential household load data.
- Hybrid CNN-LSTM models improve accuracy over single-model approaches for irregular time series.
- Probabilistic forecasting provides uncertainty intervals essential for robust decision-making under variability.

**Limitations / Contradictions for Odin:**
- Data quality issues (missing values, noise) affect prediction accuracy.
- Deep learning models risk overfitting, especially with small datasets.
- Real-time performance and uncertainty from user behavior remain challenging.

**Key takeaways:**
- LSTM with empirical mode decomposition improves household load prediction accuracy.
- Hybrid CNN-LSTM models outperform single models on irregular time series data.
- Probabilistic forecasting captures uncertainty missed by point forecasts.

---


## Recurrent Neural Networks and Long Short-Term Memory Networks: Tutorial and Survey
**Filename:** `IA--Ghojogh-&-Ghodsi_summarized.md`  
**Authors:** Ghojogh, B.; Ghodsi, A. (2022)  
**ID:** `5e1f5b6d-4b3a-4c2e-8f7a-1d2c3b4a5e6f`  
**Odin Topics:** 5.C, 6.A, 6.B, 8.A, 8.B  

**TLDR:** A tutorial and survey of recurrent neural networks, long short-term memory networks, and their variants including GRU, bidirectional processing, and ELMo.

**Problem & Motivation:** Standard RNNs suffer from gradient vanishing or explosion when learning long-term dependencies in sequences. This makes it difficult for the network to remember information from distant past time steps. LSTM and its variants address this by introducing gating mechanisms that learn when to retain or forget information.

**Approach (summary):**
- Introduces RNN as a dynamical system with parameter sharing and backpropagation through time (BPTT) for training.
- Analyzes gradient vanishing and explosion in long-term dependencies, linking to eigenvalues of the weight matrix.
- Presents solutions: close-to-identity weight matrix, long delays, leaky units, and echo state networks.

**Key Findings (selected):**
- Gradient vanishing occurs when the largest eigenvalue of the weight matrix is less than one; gradient explosion when greater than one.
- LSTM gates allow the network to learn when to clear the state, enabling both short-term and long-term dependency handling.
- Bidirectional LSTM outperforms unidirectional LSTM for offline tasks where future context is available.
- GRU simplifies LSTM by merging gates while achieving comparable performance on many sequence tasks.

**Supports Odin (direct justifications):**
- Recurrent neural networks are effective for sequence prediction tasks such as spending forecasting.
- LSTM networks mitigate gradient vanishing, enabling learning of long-term dependencies in financial time series.
- Bidirectional processing improves accuracy when future transaction data is available for offline analysis.

**Limitations / Contradictions for Odin:**
- The paper is a tutorial and survey, not original research; no new empirical results are presented. [unacknowledged]
- It does not compare LSTM variants on financial datasets, limiting direct applicability to PFMS. [unacknowledged]
- Discussion of computational complexity and mobile feasibility is absent. [unacknowledged]

**Key takeaways:**
- LSTM gates learn when to remember or forget information over long sequences.
- Gradient vanishing is controlled by keeping weight matrix eigenvalues near one.
- Bidirectional processing uses future context for better offline sequence understanding.

---


## Machine Learning Techniques for Optimizing Recurring Billing and Revenue Collection in SaaS Payment Platforms
**Filename:** `IA--Dlamini_summarized.md`  
**Authors:** Dlamini, A. (0)  
**ID:** `8a7b6c5d-4e3f-2a1b-9c8d-7e6f5a4b3c2d`  
**Odin Topics:** 5.A, 6.A, 6.B, 8.A, 8.B, 11.A, 11.B  

**TLDR:** Machine learning techniques optimize recurring billing, detect anomalies, forecast churn and revenue, and adapt pricing in SaaS payment platforms.

**Problem & Motivation:** Recurring billing in SaaS platforms suffers from payment failures, fraud, and churn due to dynamic user behavior and rigid rule-based systems. Traditional methods lack adaptability to evolving patterns and high-volume transactional data. Machine learning offers scalable solutions for proactive revenue management.

**Approach (summary):**
- Data preprocessing includes cleansing, normalization, missing value imputation, and feature engineering from payment logs and usage metrics.
- Linear and logistic regression with regularization provide interpretable baselines for fraud and churn prediction.
- Ensemble methods like random forests and gradient boosting machines achieve high accuracy by combining multiple weak learners.

**Key Findings (selected):**
- Ensemble methods like gradient boosting achieve high accuracy in fraud detection and churn forecasting.
- Autoencoders effectively detect anomalous transactions by measuring reconstruction error without labeled fraud data.
- Reinforcement learning optimizes dunning schedules and pricing strategies, maximizing revenue while minimizing churn.
- Linear algebra techniques (PCA, SVD) reduce dimensionality, improving computational efficiency and interpretability.

**Supports Odin (direct justifications):**
- Machine learning models can forecast the probability of successful recurring payments.
- Ensemble methods like random forests enhance fraud detection accuracy in payment systems.
- Autoencoders identify anomalous transactions by measuring reconstruction error.

**Limitations / Contradictions for Odin:**
- Lacks quantitative empirical results or benchmark comparisons. [unacknowledged]
- Does not address real-time inference latency constraints for mobile PFMS. [unacknowledged]
- Privacy-preserving methods (federated learning) are mentioned but not evaluated. [unacknowledged]

**Key takeaways:**
- Ensemble tree models often outperform linear baselines for churn and fraud prediction.
- Autoencoders provide unsupervised anomaly detection without labeled fraud data.
- Reinforcement learning dynamically optimizes pricing and dunning strategies.

---


## Test-Time Adaptation for Non-stationary Time Series: From Synthetic Regime Shifts to Financial Markets
**Filename:** `IA--Wu_Y.-et_al_summarized.md`  
**Authors:** Wu, Y.; Deng, Q.; Chung, W.; Li, M. (0)  
**ID:** `f81d4fae-7dec-11d0-a765-00a0c91e6bf6`  
**Odin Topics:** 6.A, 6.B, 12.A, 12.B  

**TLDR:** Test-time adaptation using batch-normalization statistics refresh or norm-only affine parameter updates improves or harms forecasting accuracy depending on shift type, with bn_stats as a safe default for financial markets.

**Problem & Motivation:** Real-world time series like financial prices are non-stationary, causing models trained on past data to lose accuracy under distribution shifts. Existing test-time adaptation methods lack causal, parameter-efficient frameworks for streaming forecasting. This paper studies when small-footprint TTA helps or hurts under synthetic and real regime shifts.

**Approach (summary):**
- Freeze backbone and update only normalization affine parameters (γ,β) using unsupervised objectives on recent unlabeled windows.
- For classification: minimize entropy and enforce temporal consistency via weak time-preserving augmentations.
- For regression: minimize prediction variance across augmentations and optionally distill from an EMA teacher.

**Key Findings (selected):**
- num: On SPY directional classification, bn_stats achieves 0.525 accuracy vs no_tta 0.504 and norm_only 0.512.
- num: Under gradual synthetic drift, norm_only reduces MAE to 0.22 (R2 0.31) vs no_tta 0.28 (R2 -0.31).
- num: BN-Stats yields Sharpe ratio 1.930 on SPY and 4.080 on QQQ, higher than no_tta (1.746, 3.205) and norm_only (1.544, 1.349).
- Diebold-Mariano tests show bn_stats significantly better than no_tta on SPY (p=0.0054) and QQQ (p=0.0220).

**Supports Odin (direct justifications):**
- Batch-normalization statistics refresh is a safe default for financial time series forecasting.
- Norm-only adaptation can hurt performance on noisy equity markets and should be used with uncertainty control.
- Uncertainty-triggered fallback prevents harmful gradient updates when entropy or variance is high.

**Limitations / Contradictions for Odin:**
- Synthetic shift generators are stylized and cannot cover all real dynamics [unacknowledged].
- Only one backbone architecture (TCN) is used for main results; findings may not generalize to other backbones [unacknowledged].
- No comparison to online learning or continual learning baselines [unacknowledged].

**Key takeaways:**
- BN statistics refresh improves Sharpe ratio from 1.75 to 1.93 on SPY.
- Norm-only adaptation helps gradual drift but hurts noisy markets.
- Uncertainty fallback prevents harmful updates in high entropy days.

---


## Artificial Intelligence Powered Personal Finance Management System
**Filename:** `IA--Chahar-et_al_summarized.md`  
**Authors:** Chahar, P.; Vishwakarma, Y. K.; Mishra, R.; Paliwal, G. (0)  
**ID:** `10.2139/ssrn.6377518`  
**Odin Topics:** 3.A, 3.B, 6.A, 6.B, 7.A, 7.B, 8.A, 10.A, 11.A, 12.A  

**TLDR:** An AI-powered personal finance assistant using machine learning and natural language processing to provide dynamic budget recommendations, expense classification, spending forecasts, and financial education.

**Problem & Motivation:** Traditional financial tools lack adaptability and personalization, leading to poor savings and debt. Existing systems offer generic advice and do not adapt to diverse income streams or user behavior. An intelligent, adaptive system is needed to improve financial literacy and decision-making.

**Approach (summary):**
- Data is collected via bank APIs or CSV uploads and preprocessed with normalization and text cleaning.
- Supervised ML models (Random Forest, SVM, LSTM) are trained on labeled transaction data with TF-IDF and word embeddings for classification.
- Time series forecasting (ARIMA, LSTM) predicts future expenses and income for proactive planning.

**Key Findings (selected):**
- {'num': 'Expense classification accuracy rated 4.2/5 by users.'}
- {'num': 'Overall user satisfaction score 4.4/5.'}
- {'num': 'Ease of use rated 4.5/5.'}
- Predictive models struggle with irregular income and fluctuating spending patterns.

**Supports Odin (direct justifications):**
- Expense classification can be automated using Random Forest and SVM with text vectorization.
- LSTM models predict future spending with lower MAE than ARIMA for irregular patterns.
- Personalized budget recommendations improve user goal achievement by 4.3/5 rating.

**Limitations / Contradictions for Odin:**
- Models struggle with irregular income streams and fluctuating expenses.
- Data quality and accessibility issues affect prediction reliability.
- User trust remains a barrier due to lack of explainability. [unacknowledged]

**Key takeaways:**
- Expense classification accuracy rated 4.2/5 by users.
- Overall user satisfaction score 4.4/5 indicates positive reception.
- LSTM and ARIMA forecast spending but fail with irregular income.

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
- num: Weighted F1-score of 0.913 across 18 spending categories.
- num: Manual expense-logging effort reduced by approximately 78% compared to conventional approaches.
- High-frequency categories (Food & Dining, Transport, Utilities) achieve F1 above 0.95.
- 84% of pilot users found AI-generated insights useful or very useful.

**Supports Odin (direct justifications):**
- XGBoost with temporal features achieves 91.3% weighted F1-score for transaction categorization.
- LLM-generated insights using RAG are rated useful by 84% of users.
- Prophet forecasting requires at least 3 months of historical data for reliable predictions.

**Limitations / Contradictions for Odin:**
- {'Cold-start problem': 'categorization accuracy lower for new users with fewer than 50 transactions.'}
- {'LLM hallucination risk': 'Gemini may generate imprecise guidance despite RAG.'}
- {'Manual data entry dependency': 'users may not maintain complete records without banking API.'}

**Key takeaways:**
- XGBoost achieves 91.3% F1-score for transaction categorization.
- LLM insights rated useful by 84% of pilot users.
- Manual expense logging effort reduced by 78%.

---


## 📌 Note for the Agent

The summaries above contain **essential extracts** – enough to understand the paper's relevance to Odin, including supporting evidence and limitations.
If you need additional details not shown here (e.g., **critical citations, definitions, equations, full methodology, or the complete mapping rationale**),
**ask the user to send the original summary file (`<filename>_summarized.md`) or the converted MarkItDown file(`<filename>_marked.md`)** for the specific paper(s) of interest.
Do not invent missing information. Acknowledge gaps when they exist.