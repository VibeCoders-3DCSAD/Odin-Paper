# Comprehensive Report for Subtopic: `7.C`

**Total files:** 13

This report includes problem/motivation, approach, key findings, support for Odin, and limitations/contradictions.

---


## AI-Driven Personal Finance Management: Predictive Expense Forecasting and Behavioural Clustering
**Filename:** `IA--Vinitha-et_al_summarized.md`  
**Authors:** Vinitha, C.; Krishna, A.H.; Reddy, E.M.; Javari, P. (2026)  
**ID:** `2c3d4e5f-6a7b-8c9d-0e1f-2a3b4c5d6e7f`  
**Odin Topics:** 3.A, 5.A, 5.C, 6.A, 6.B, 7.B, 7.C  

**TLDR:** Combines LSTM for expense forecasting and K-Means for spending behavior clustering with VADER sentiment analysis, achieving 99.93% prediction accuracy.

**Problem & Motivation:** Manual financial tracking is complex, time-consuming, and error-prone. Traditional tools store transactions but lack advanced analytics for future expense prediction. Users struggle to interpret spending patterns and link qualitative feelings to quantitative data.

**Approach (summary):**
- System built with Django, MySQL, and OTP authentication via SMTP for secure access.
- LSTM model with MSE loss and Adam optimizer trained on historical daily expenses over 1000 epochs.
- K-Means clustering groups expenses by category and amount to reveal spending patterns.

**Key Findings (selected):**
- "num: LSTM achieved 99.93% accuracy and MSE of 35.41 on expense prediction."
- K-Means clustering visualizes distinct spending behavior patterns across expense categories.
- Budget recommendation suggests investment amounts from predicted surplus (e.g., 8,661 units surplus).
- VADER sentiment analysis enables continuous system improvement based on user feedback.

**Limitations / Contradictions for Odin:**
- "Evaluation uses only accuracy and MSE; no real-world user study or longitudinal validation. [unacknowledged]"
- "Potential overfitting of LSTM with 1000 epochs on small dataset not discussed. [unacknowledged]"
- "No baseline comparison to traditional statistical methods (e.g., ARIMA). [unacknowledged]"

**Key takeaways:**
- "LSTM predicts daily expenses with 99.93% accuracy."
- "K-Means reveals hidden spending patterns from transaction data."
- "Budget recommendation uses predicted surplus for investment advice."

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

**Limitations / Contradictions for Odin:**
- Relies on quality of input data and third-party AI services. [acknowledged]
- No direct bank API integration for real-time sync; requires manual uploads. [acknowledged]
- Does not include deep learning or advanced NLP for financial assistants. [acknowledged]

**Key takeaways:**
- Automated transaction categorization reduces manual effort and improves accuracy.
- Personalized budget alerts help control overspending effectively.
- Aggregating multiple payment sources provides a unified financial view.

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


## Goal Programming Model in Financial Planning of the International Development Bank
**Filename:** `IA--Aboud_summarized.md`  
**Authors:** Aboud, S. F. (2025)  
**ID:** `10.21070/acopen.10.2025.12858`  
**Odin Topics:** 7.A, 7.C, 12.A  

**TLDR:** Goal programming optimizes conflicting financial objectives (revenue, expenses, profit, assets) in a bank's financial planning, achieving near-optimal resource allocation.

**Problem & Motivation:** Financial institutions struggle to balance multiple conflicting objectives like profit maximization, cost control, and liquidity. Traditional planning models cannot accommodate competing goals under resource constraints. A quantitative method is needed to prioritize and trade off these objectives.

**Approach (summary):**
- Data: Annual reports of International Development Bank for Investment and Finance (Iraq) from 2016 to 2024.
- Method: Weighted-preemptive hybrid goal programming with seven prioritized goals and assigned weights.
- Solved using WINQSB software.

**Key Findings (selected):**
- num: The model achieved near-optimal solutions with minimal deviations across all seven goals.
- num: Revenue goal met with negative deviation 0.1884 billion.
- num: Expenses goal met with deviation 0.1873 billion.
- num: Net profit met with deviation 0.3006 billion.

**Limitations / Contradictions for Odin:**
- The model uses annual data, not high-frequency spending data typical of PFMS. [unacknowledged]
- User-specific preferences or behavioral dynamics are absent. [unacknowledged]
- No comparison with baseline or alternative algorithms. [unacknowledged]

**Key takeaways:**
- Goal programming balances revenue, expenses, profit, and assets with minimal deviations.
- The preemptive method satisfies higher-priority goals before lower ones.
- Achieved near-optimal solutions in a multi-objective banking scenario.

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


## Optimized Financial Planning: Integrating Individual and Cooperative Budgeting Models with LLM Recommendations
**Filename:** `IA--de_Zarza-et_al_summarized.md`  
**Authors:** de Zarzà, I.; de Curtò, J.; Roig, G.; Calafate, C.T. (2024)  
**ID:** `10.3390/ai5010006`  
**Odin Topics:** 7.A, 7.B, 7.C, 13.A, 2.C  

**TLDR:** Integrates LLM recommendations into individual and cooperative budgeting optimization models to maximize savings while respecting user preferences and constraints.

**Problem & Motivation:** Financial planning is complex and overwhelming for non-experts. Traditional methods lack personalization and adaptability to dynamic needs. There is a need for accessible, AI-driven budgeting tools that combine mathematical optimization with practical recommendations.

**Approach (summary):**
- Synthetic financial data for ten households with normally distributed income and expenses across rent, groceries, utilities, and entertainment.
- Optimization models for individual and cooperative budgeting maximizing savings subject to non‑negativity and income constraints.
- Uses GPT‑4 to generate percentage‑based allocation recommendations for expense categories, savings, debt, and investments.

**Key Findings (selected):**
- LLM‑generated recommendations align with established financial planning principles such as emergency funds, retirement savings, and consumption smoothing.
- num: The LLM‑recommended savings allocation included 20% for emergency funds, 15% for retirement, and 10% for non‑retirement savings.
- Cooperative budgeting with LLM advice leads to more balanced allocations across household members.
- Long‑term LLM recommendations incorporate life‑cycle model principles, including consumption smoothing and future event planning.

**Limitations / Contradictions for Odin:**
- "LLM recommendations may contain hallucinations or errors [unacknowledged] (paper proposes mitigations but does not test them empirically)."
- "The simulation uses synthetic data; real‑world validation is missing [unacknowledged]."
- "Long‑term dependencies are acknowledged but not modeled in the optimization equations [acknowledged] (paper discusses future work)."

**Key takeaways:**
- "LLM recommendations can allocate 20% of income to emergency funds."
- "Cooperative budgeting with LLM increases household savings potential."
- "Optimization with LLM bounds outperforms LLM‑only advice in simulations."

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