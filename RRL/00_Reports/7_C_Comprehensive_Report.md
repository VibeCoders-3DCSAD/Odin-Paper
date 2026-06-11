# Comprehensive Report for Subtopic: `7.C`

**Total relevant papers:** 16

This report includes problem/motivation, approach, key findings, support for Odin, and limitations/contradictions.

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


## How reinforcement learning can drive personalized financial wellness
**Filename:** `IA--Pandey-&-Awasthi_summarized.md`  
**Authors:** Pandey, V.; Awasthi, V. (2025)  
**ID:** `10.30574/ijsra.2025.15.1.1244`  
**Odin Topics:** 4.B, 5.A, 5.B, 5.C, 7.A, 7.B, 7.C, 11.A, 12.A, 12.B, 13.A  

**TLDR:** Reinforcement learning with DQN, user persona clustering, and GPT-based conversation produces personalized financial recommendations that improve savings outcomes in a simulated environment.

**Problem & Motivation:** Financial wellness is a pervasive challenge; many individuals struggle with saving, investing, and budgeting effectively. Traditional budgeting tools and robo-advisors provide generic advice that fails to account for individual behavior and needs. This gap motivates an integrated framework combining RL, behavioral analytics, and NLP to deliver real-time personalized guidance.

**Approach (summary):**
- Synthetic dataset of 300 users with income and saving rate generated to simulate diverse financial behaviors.
- K-means clustering (k=3) creates interpretable personas: low-income low-saver, mid-income moderate-saver, high-income high-saver.
- Personal finance management formulated as Markov Decision Process with state (month, savings) and 6 discrete saving actions ($0 to $50).

**Key Findings (selected):**
- num: Learned policy achieved average final savings of $450 across simulations, compared to baseline 2 (always save $50) at $564 and baseline 1 negative.
- RL agent learns to save aggressively near year-end and after shocks to recover from debt.
- K-means clustering produces well-separated personas that can inform policy specialization.
- GPT-4 generates empathetic, personalized responses that incorporate persona context and RL recommendations.

**Supports Odin (direct justifications):**
- Reinforcement learning can learn personalized saving policies that outperform static baselines.
- User persona clustering via K-means enables initial policy customization for different financial behaviors.
- Conversational AI can translate quantitative RL recommendations into empathetic, context-aware advice.

**Limitations / Contradictions for Odin:**
- Synthetic data limits external validity.
- Action space limited to saving amounts, excluding debt and investment choices.
- No real-world deployment or user study. [unacknowledged]

**Key takeaways:**
- DQN agent achieved $450 average savings in simulation.
- K-means clusters users by income and saving rate into three personas.
- Conversational GPT explains RL recommendations naturally.

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


## Dynamic Model for Budget Allocation in via Multi-Criteria Optimization
**Filename:** `IA--Gulbakyt-et_al_summarized.md`  
**Authors:** Gulbakyt, S.; Almaz, A.; Saule, S.; Suhrab, Y. (2025)  
**ID:** `10.47738/jads.v6i4.935`  
**Odin Topics:** 7.A, 7.B, 7.C, 12.A, 12.B  

**TLDR:** A dynamic multi-criteria optimization framework allocates a constrained regional budget across seven activity areas using SQP and genetic algorithms, achieving fair distribution with a Gini coefficient of 0.223.

**Problem & Motivation:** Regional budget allocation by local councils in Kazakhstan suffers from opacity, insufficient public involvement, and lack of data-driven tools. Socioeconomic disparities and declining public trust demand a transparent, equitable, and efficient allocation method that balances citizen satisfaction, strategic priorities, basic needs, and urbanization.

**Approach (summary):**
- Data from four districts in Almaty region: population, income, urbanization coefficients, and synthetically generated citizen votes.
- Objective function maximizes weighted sum of four criteria: citizen satisfaction (0.2), strategic priorities (0.2), basic needs fulfillment (0.3), and urbanization level (0.3).
- Quadratic programming with Sequential Quadratic Programming (SQP) implemented in MATLAB fmincon solver.

**Key Findings (selected):**
- SQP converged in under 100 iterations to objective value 18,519,864.85 thousand tenge.
- GA achieved objective value 18,520,000.00 thousand tenge after 500 generations.
- num: The difference between methods is 135.15 thousand tenge (0.0007% of total budget).
- Healthcare (22.05%) and transport (21.11%) received largest allocations; education smallest (7.03%).

**Supports Odin (direct justifications):**
- Multi-criteria optimization can balance user satisfaction, savings goals, and spending necessities in personal budget allocation.
- SQP provides fast convergence for well-defined budget constraints, suitable for real-time recommendations.
- Genetic algorithms offer robustness against local optima when user preferences are uncertain or conflicting.

**Limitations / Contradictions for Odin:**
- Synthetic citizen voting data reduces external validity. [unacknowledged]
- Weight coefficients lack systematic sensitivity analysis or stakeholder validation. [unacknowledged]
- Constraint violation persists at convergence (0.47% of budget), though authors acknowledge it as a trade-off.

**Key takeaways:**
- SQP and GA achieved nearly identical optimal budget allocations, differing by only 0.0007%.
- Healthcare and transport received the largest shares (22% and 21%) due to strategic weight.
- Gini coefficient of 0.223 indicates fair distribution across seven activity areas.

---


## Goal Programming Model in Financial Planning of the International Development Bank
**Filename:** `IA--Aboud_summarized.md`  
**Authors:** Aboud, S. F. (2025)  
**ID:** `10.21070/acopen.10.2025.12858`  
**Odin Topics:** 7.A, 7.C, 12.A  

**TLDR:** Goal programming optimizes conflicting financial objectives (revenue, expenses, profit, assets) in a bank's financial planning, achieving near-optimal resource allocation.

**Problem & Motivation:** Financial institutions struggle to balance multiple conflicting objectives like profit maximization, cost control, and liquidity. Traditional planning models cannot accommodate competing goals under resource constraints. A quantitative method is needed to prioritize and trade off these objectives.

**Approach (summary):**
- {'Data': 'Annual reports of International Development Bank for Investment and Finance (Iraq) from 2016 to 2024.'}
- {'Method': 'Weighted-preemptive hybrid goal programming with seven prioritized goals and assigned weights.'}
- Solved using WINQSB software.

**Key Findings (selected):**
- {'num': 'The model achieved near-optimal solutions with minimal deviations across all seven goals.'}
- {'num': 'Revenue goal met with negative deviation 0.1884 billion.'}
- {'num': 'Expenses goal met with deviation 0.1873 billion.'}
- {'num': 'Net profit met with deviation 0.3006 billion.'}

**Supports Odin (direct justifications):**
- Goal programming can resolve conflicting financial objectives by assigning priorities and weights.
- Near-optimal solutions are achievable with minimal deviation from targets.
- Preemptive ordering ensures higher-priority goals are satisfied before lower ones.

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
- num: BET achieves the highest Recall@20 (0.1753) and NDCG@20 (0.1483) on Gowalla with LightGCN at 80% sparsity.
- num: At 95% sparsity on Gowalla with LightGCN, BET obtains 0.0627 Recall@5 and 0.1037 NDCG@5, outperforming CIESS by 22% and 21% respectively.
- num: On Yelp2018 with LightGCN at 80% sparsity, BET reaches 0.0873 Recall@20, exceeding the best baseline by 4%.
- BET guarantees strict memory budget satisfaction, unlike ESAPN and OptEmbed which often exceed target sparsity.

**Supports Odin (direct justifications):**
- A table-level action that sets embedding sizes for all users simultaneously can strictly enforce a memory budget.
- DeepSets-based fitness prediction reduces the number of full model evaluations from O(number of candidates × iterations) to O(iterations).
- Ranking users and items by frequency and allocating larger embeddings to frequent entities improves recommendation quality under sparsity.

**Limitations / Contradictions for Odin:**
- Does not address cold-start users or items; frequency-based ranking fails for new entities. [unacknowledged]
- May not generalize to streaming recommendation where user/item sets grow over time (mentioned as future work).
- Requires a pre-trained full embedding table, which itself may be infeasible for extremely large-scale systems. [unacknowledged]

**Key takeaways:**
- BET guarantees strict memory budget adherence without manual coefficient tuning.
- DeepSets fitness predictor cuts evaluation cost from O(S*T) to O(T) full trainings.
- At 95% sparsity, BET achieves 0.0627 Recall@5 on Gowalla with LightGCN.

---


## A User-Centric Exploration of Axiomatic Explainable AI in Participatory Budgeting.
**Filename:** `IA--Hashemi-et_al_summarized.md`  
**Authors:** Hashemi, M.; Darejeh, A.; Cruz, F. (2024)  
**ID:** `10.1145/3675094.3677599`  
**Odin Topics:** 7.B, 7.C, 10.B, 12.A, 12.B  

**TLDR:** Using axioms as linear constraints, an integer linear programming approach generates explanations for participatory budgeting outcomes, improving user understanding and perceived fairness but not consistently affecting trust.

**Problem & Motivation:** Participatory budgeting mechanisms lack transparency despite satisfying desirable axioms. Existing voting rules are complex, making outcomes difficult for users to understand. There is a need for explainable AI approaches that justify budget allocations using axiomatic properties.

**Approach (summary):**
- Proposes an integer linear programming (ILP) formulation where axioms (feasibility, exhaustiveness, utilitarian welfare) serve as constraints.
- Uses Gurobi optimizer to enumerate all allocations satisfying the constraints, then explains why a specific outcome was chosen or rejected.
- Evaluates the approach with a pilot user study of 26 participants via Mechanical Turk.

**Key Findings (selected):**
- num: 72.4% of participants found explanations extremely or very helpful for understanding the system's decision.
- num: 63.3% of participants preferred general explanations over counterfactual explanations.
- num: 30% reported a positive impact on perceived fairness of the system after explanations; none reported a negative impact.
- num: Trust increased in 27% of cases, decreased in 20%, and remained unchanged in 50% after receiving explanations.

**Supports Odin (direct justifications):**
- Providing axiomatic explanations improves user understanding of budget allocation decisions.
- General explanations are preferred over counterfactual explanations in participatory budgeting.
- Explanations based on axioms positively impact perceived fairness of the system.

**Limitations / Contradictions for Odin:**
- Small sample size (N=26) limits generalizability of user findings.
- Study only used two simple cases with three projects and greedy rule; complex scenarios may yield different results.
- Could not draw definitive conclusions about trust due to mixed and inconclusive results [unacknowledged].

**Key takeaways:**
- 72.4% of users found axiomatic explanations helpful for understanding budget decisions.
- Explanations improved perceived fairness in participatory budgeting.
- User trust was inconsistently affected by explanations, with 20% reporting decreased trust.

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


## A Recommendation System for Participatory Budgeting
**Filename:** `IA--Leibiker-&-Talmon_summarized.md`  
**Authors:** Leibiker, G.; Talmon, N. (2023)  
**ID:** `f5a3b2c1-4d5e-6f7a-8b9c-0d1e2f3a4b5c`  
**Odin Topics:** 5.B, 6.A, 7.B, 7.C, 11.A, 12.B  

**TLDR:** Machine learning recommendation systems estimate voter preferences from partial ballots in participatory budgeting, improving prediction accuracy and budget allocation.

**Problem & Motivation:** Voters in participatory budgeting face information overload when many projects are considered, leading to low participation and poor decisions. Existing methods require complete ballots, which is cognitively burdensome. A solution using recommendation systems can reduce this burden while maintaining allocation quality.

**Approach (summary):**
- Used ten real-world participatory budgeting datasets from Warsaw, Poland (2020-2023), with 2,614 to 10,424 voters and 67 to 111 projects per instance.
- Defined three sampling settings: random (k projects chosen uniformly), offline (choose k projects by popularity, consensus, or controversy), and online adaptive (iteratively choose most controversial projects).
- Applied prediction modules: Matrix Factorization, Factorization Machines, and binary classification using XGBoost with class weighting for imbalance.

**Key Findings (selected):**
- num: At 10% sample degree, classification-online and offline-popularity setups produced higher FA scores than the sampling method.
- num: Classification-offline-popularity achieved the maximal FA score when collecting half of the votes (sample degree 0.5).
- num: As sample degree increased, FA score increased and Symmetric Distance decreased across most LV degree levels.
- Classification techniques consistently outperformed Matrix Factorization and Factorization Machines in prediction accuracy.

**Supports Odin (direct justifications):**
- Machine learning classification on partial user ballots improves budget allocation accuracy compared to naive sampling.
- Adaptive online preference elicitation reduces information overload without sacrificing prediction quality.
- Fractional Allocation score is an effective metric for evaluating budget recommendation systems with incomplete inputs.

**Limitations / Contradictions for Odin:**
- Experiments conducted only on Warsaw PB datasets; results may not generalize to other cultural or demographic contexts. [unacknowledged]
- Assumes existence of a training set of voters with full ballots (LV group), which may be unavailable in pure cold-start scenarios. [unacknowledged]
- Does not address privacy concerns of collecting partial preferences from all voters. [unacknowledged]

**Key takeaways:**
- Classification online achieves higher FA scores than sampling at 10% data collection.
- Fractional Allocation score increases with more exposed preferences.
- Adaptive controversial selection improves prediction over random sampling.

---


## AI Wealth Navigator: An Integrated Platform for Smart Budgeting, Financial Learning, and Personalized Policy Guidance
**Filename:** `IA--Yadav-et_al_summarized.md`  
**Authors:** Yadav, A.; Prakash, R. S.; Iqubal, S. M.; Gebremicahea, M. G. (0)  
**ID:** `f5c8d3e6-9a4b-4c7d-8e2f-1a3b5c7d9e0f`  
**Odin Topics:** 3.A, 3.B, 7.B, 7.C, 9.A, 9.B, 10.A, 10.B, 11.A, 11.B, 13.A  

**TLDR:** AI Wealth Navigator integrates adaptive financial learning, AI-driven budget tracking with receipt scanning, and personalized government policy recommendations using LLMs into a single platform.

**Problem & Motivation:** Personal finance apps remain fragmented, separating budgeting, education, and policy navigation. Users lack cohesive tools to maximize financial well-being, especially in regions with low financial literacy like India. Existing solutions fail to provide personalized, integrated guidance across all three domains.

**Approach (summary):**
- Built a web platform using Next.js, Supabase, Prisma, Inngest, and Arcjet for secure, scalable performance.
- Integrated Gemini LLM for personalized financial recommendations and adaptive learning roadmaps based on user literacy and progress.
- Developed an AI-powered budget tracker with receipt OCR (94% accuracy) and real-time visual insights.

**Key Findings (selected):**
- num: Receipt scanner achieved 94% accuracy on digital and physical receipts.
- num: Over 70% of users discovered previously unknown government programs tailored to their profiles.
- User ratings: budgeting insights 4.8/5, policy recommendations 4.7/5, learning roadmap 4.6/5.
- Arcjet blocked all simulated security threats, ensuring data protection.

**Supports Odin (direct justifications):**
- Receipt scanning with AI achieves 94% accuracy, reducing manual entry errors.
- Personalized policy recommendations increase user discovery of relevant government schemes by over 70%.
- Integrating financial learning, budgeting, and policy guidance into one platform reduces fragmentation.

**Limitations / Contradictions for Odin:**
- Small sample size (50 users) for human evaluation, limiting generalizability.
- No longitudinal study to measure retention or sustained behavior change.
- Reliance on full user profiles for policy matching may raise privacy concerns (acknowledged as minor drawback by authors).

**Key takeaways:**
- Receipt OCR achieved 94% accuracy on digital and physical receipts.
- Over 70% of users found new government schemes via policy engine.
- Unified platform integrates budgeting, learning, and policy recommendations.

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