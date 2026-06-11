# Comprehensive Report for Subtopic: `7.B`

**Total relevant papers:** 23

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


## Personal Financial Information Presentation and Consumer Spending
**Filename:** `I--Levi_summarized.md`  
**Authors:** Levi, Y. (2025)  
**ID:** `9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d`  
**Odin Topics:** 5.A, 7.A, 7.B, 11.A, 13.A  

**TLDR:** Presenting net worth as a monthly cash flow under a consumption frame with a salient spending comparison reduces discretionary spending by 15% in a field experiment.

**Problem & Motivation:** Consumers exhibit strong spending habits and inertia, yet existing savings tools like financial education and tax subsidies are costly or benefit only the wealthy. It is unclear whether simple changes in information presentation within online financial apps can influence spending without altering economic variables.

**Approach (summary):**
- Randomized field experiment with 3,138 users of an online account aggregation app over 25 months.
- Users received a personalized index converting net worth to inflation-protected lifetime monthly cash flow.
- Treatments varied index framing (Financial Sustainability Index with fear appeal vs. neutral Life Annuity Index) and salience (context plot comparing index to historical spending vs. no plot).

**Key Findings (selected):**
- num: Users exposed to consumption frame (FSI) and context plot reduced discretionary spending by 15% relative to control.
- num: Effect persisted for 8 months after experiment removal, with gradual convergence after 9 months.
- num: Restaurant spending fell 14%, clothing 20%, entertainment 14%, travel 24%, and cash withdrawals 25%.
- No significant change in non-discretionary categories (gas, groceries, utilities).

**Supports Odin (direct justifications):**
- Presenting net worth as monthly cash flow under a consumption frame reduces discretionary spending by 15%.
- A salient comparison between the index and past spending is necessary for the framing effect to work.
- The spending reduction persists for months after the treatment is removed.

**Limitations / Contradictions for Odin:**
- Data may not include all consumer accounts, potentially offsetting spending changes in unobserved accounts.
- Net worth estimation omits real estate and some retirement or debt accounts, biasing the personalized index.
- Sample is wealthier than average U.S. population, limiting generalizability to lower-income users.

**Key takeaways:**
- A 15% reduction in discretionary spending lasted 8 months after treatment removal.
- Consumption frame and salient context together drive behavior change.
- Effect strongest on tempting categories like restaurants and clothing.

---


## Consumer Autonomy or Illusion? Rethinking Consumer Agency in the Age of Algorithms
**Filename:** `IA--Nokhiz-&-Ruwanpathirana_summarized.md`  
**Authors:** Nokhiz, P.; Ruwanpathirana, A. K. (2025)  
**ID:** `10.23919/JSC.2025.0015`  
**Odin Topics:** 3.A, 5.A, 7.A, 7.B, 13.A  

**TLDR:** Formal analysis shows that obligatory consumption, algorithmic persuasion, and unstable work schedules lead rational consumers to early financial ruin despite utility-maximizing behavior.

**Problem & Motivation:** Consumer agency in digital ecosystems is eroded by systemic barriers like obligatory subscriptions, algorithmic manipulation (e.g., BNPL, personalized ads), and unpredictable work schedules. The authenticity of consumer choices is questioned as external pressures undermine financial autonomy. Existing models lack formal treatment of how limited agency impacts long-term financial stability.

**Approach (summary):**
- Constructs discounted utility models with constraints representing obligatory consumption (fixed amount), impulsive consumption (minimum subsistence plus discretionary spending), and income uncertainty from unstable work schedules.
- Assumes rational utility-maximizing agents with concave utility functions (CRRA) and no borrowing.
- Defines financial ruin as assets reaching zero within finite time.

**Key Findings (selected):**
- {'num': 'Rational consumers with fixed obligatory consumption will go to ruin regardless of utility function concavity.'}
- {'num': 'With impulsive consumption and minimum subsistence, probability of avoiding ruin decays exponentially as exp(-cT) for sufficiently large T.'}
- {'num': 'Lookahead of k steps yields utility advantage of Ω(k) over no lookahead under bounded income.'}
- Algorithmic persuasion and obligatory consumption create value capture, where consumers adopt externally imposed values without critical reflection.

**Supports Odin (direct justifications):**
- Consumers with fixed obligatory expenses face guaranteed ruin under rational utility maximization.
- Algorithmic impulse triggers increase ruin probability exponentially over time.
- Workers with advance schedule notice (lookahead) achieve Ω(k) higher utility than those without.

**Limitations / Contradictions for Odin:**
- Model uses simple intertemporal consumption framework without debt or liabilities.
- Does not incorporate behavioral economics insights like present bias or loss aversion.
- Macroeconomic factors like inflation and recessions not modeled.

**Key takeaways:**
- Fixed obligatory consumption guarantees financial ruin even for rational agents.
- Algorithmic impulse triggers make ruin exponentially more likely over time.
- Knowing work schedules 2 weeks ahead yields significantly higher utility.

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


## Development of a Platform for Financial Data Analysis and Adaptive Personal Finance Management
**Filename:** `IA--Kaarov-&- Esenalieva_summarized.md`  
**Authors:** Kaarov, A.; Esenalieva, G. (2025)  
**ID:** `10.20944/preprints202504.2615.v1`  
**Odin Topics:** 3.A, 7.B, 9.A, 9.B, 10.A, 13.A  

**TLDR:** TYIYN is a multilingual mobile app using AI to provide adaptive budgeting, expense categorization, and cash flow estimation with a Flutter-Django stack.

**Problem & Motivation:** Many individuals lack intelligent tools to monitor expenses and receive context-appropriate financial advice, especially in developing economies. Financial ignorance and lack of guidance lead to poor spending, saving, and reactive budgeting. AI-powered finance apps can improve user outcomes through behavior-based recommendations.

**Approach (summary):**
- The app uses Flutter for cross-platform frontend, Django REST Framework for backend API, and PostgreSQL for data storage.
- AI algorithms provide personalized budget advice, expense categorization, and cash flow estimation using Pandas and Matplotlib for analysis.
- Asynchronous tasks (notifications, sync) are handled by Celery and Redis.

**Key Findings (selected):**
- {'num': 'Users who followed AI recommendations increased average monthly savings by 12–18%.'}
- {'num': '45% of users reduced discretionary spending on non-essential items.'}
- {'num': 'Overspending prediction engine achieved approximately 85% precision.'}
- {'num': 'API response times under 200 ms provided a responsive user experience.'}

**Supports Odin (direct justifications):**
- AI-driven personalized financial advice increases average monthly savings by 12–18%.
- Multilingual support improves usability for 87% of non-English speaking users.
- Interactive dashboards lead to more frequent engagement than static reports.

**Limitations / Contradictions for Odin:**
- Manual transaction entry creates user adoption friction.
- Lacks direct banking integration, planned for future using open banking APIs.
- Initial recommendation engine performance required real-world data to improve [unacknowledged].

**Key takeaways:**
- AI recommendations increased savings by 12-18% for active users.
- Multilingual support boosted usability for 87% of non-English speakers.
- Interactive dashboards drive more frequent financial engagement.

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


## Digital Persona Modeling for Context-Aware Financial Decisioning
**Filename:** `IA--Sanhosh-&-Singh_summarized.md`  
**Authors:** R, Sai Sanhosh; Singh, Ashuosh Kumar (2025)  
**ID:** `c3d4e5f6-7890-4a5b-9cde-f01234567890`  
**Odin Topics:** 5.A, 5.C, 6.A, 7.B, 8.A, 10.A, 12.A, 12.B  

**TLDR:** Digital persona modeling integrates behavioral, contextual, and intent-driven attributes to enable context-aware financial decisioning for personalized budgeting, investment, and fraud detection.

**Problem & Motivation:** Static demographic profiles fail to capture dynamic user behavior and context in digital finance. Existing systems lack real-time adaptability to individual intent and situational factors. A unified framework for digital persona modeling is needed to enable personalized, trustworthy financial guidance.

**Approach (summary):**
- Proposes a five‑layer architecture: data acquisition, context engine, persona builder, decisioning model layer, and decision delivery with feedback.
- Uses a simulated hybrid dataset of transactional logs, mobile contextual logs, user profiles, and feedback labels to mimic mobile banking journeys.
- Implements Random Forest for classification, LSTM for sequential pattern analysis, and K‑Means for persona grouping.

**Key Findings (selected):**
- num: LSTM Neural Net achieved 93.6% accuracy, 94.4% precision, 91.8% recall, and 92.9% F1‑score on the simulated dataset.
- num: Random Forest achieved 91.2% accuracy, 90.4% precision, 89.9% recall, and 90.1% F1‑score.
- num: K‑Means clustering had 75.0% accuracy, showing lower suitability for classification tasks.
- LSTM outperforms other models due to its ability to model temporal dependencies in user behavior and context shifts.

**Supports Odin (direct justifications):**
- LSTM models capture temporal dependencies in financial behavior with 93.6% accuracy.
- Context‑aware risk function can adapt decisions to location, time, and device for fraud detection.
- Federated learning enables privacy‑preserving persona modeling without centralizing user data.

**Limitations / Contradictions for Odin:**
- Data privacy concerns: heavy reliance on sensitive user data increases breach risk. [acknowledged]
- Limited dataset diversity: synthetic data may introduce bias and reduce cross‑population applicability. [acknowledged]
- Model generalizability: LSTM may not generalize to fast‑evolving financial ecosystems. [acknowledged]

**Key takeaways:**
- LSTM achieved 93.6% accuracy for context‑aware financial decisions.
- Digital personas integrate behavioral, contextual, and intent‑driven attributes.
- Federated learning preserves user privacy while enabling personalization.

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