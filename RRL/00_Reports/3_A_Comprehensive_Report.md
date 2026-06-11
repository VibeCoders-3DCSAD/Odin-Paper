# Comprehensive Report for Subtopic: `3.A`

**Total files:** 23

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


## Financial Literacy of Public Secondary School Teachers in San Francisco District, Camotes Island, Cebu, Philippines
**Filename:** `L--Montuerto-&-Ferrater-Gimena_summarized.md`  
**Authors:** Montuerto, J. E.; Ferrater-Gimena, J. A. O. (2026)  
**ID:** `10.5281/zenodo.18438866`  
**Odin Topics:** 1.C, 3.A, 7.A, 13.A, 13.B  

**TLDR:** Public secondary school teachers in San Francisco District, Camotes Island demonstrate moderate financial literacy in budgeting, spending, and credit management, but low literacy in savings and investing.

**Problem & Motivation:** Public school teachers in the Philippines face financial difficulties including budget deficits, debt cycles, and reliance on loans. Financial literacy is essential for personal financial management and effective teaching of financial education, yet limited research exists on rural public school teachers' financial literacy.

**Approach (summary):**
- Descriptive-correlational design with 150 teachers from three national high schools.
- Researcher-made survey with two parts: demographic profile and financial literacy items (budgeting, savings, investing, spending, credit/debt).
- Cronbach's alpha of 0.885 confirmed reliability.

**Key Findings (selected):**
- "num: 42% of respondents were aged 24-32 years (mean 36.11), 78.67% female, 68% married, 74% had no other income sources."
- "num: Budgeting aggregate mean 2.96 (moderate), savings 2.42 (low), investing 1.98 (low), spending 3.17 (moderate), credit/debt 3.05 (moderate)."
- "num: Age significantly related to budgeting (p=0.004), savings (p=0.001), investing (p=0.0001), and credit/debt (p=0.001)."
- "num: Educational attainment significantly related to savings (p=0.038) and credit/debt (p=0.001)."

**Limitations / Contradictions for Odin:**
- "Small sample from one rural district; may not represent urban teachers. [unacknowledged]"
- "Cross-sectional design; causality cannot be inferred. [unacknowledged]"
- "Self-reported survey data may overstate financial literacy due to social desirability bias. [unacknowledged]"

**Key takeaways:**
- "Teachers showed low financial literacy in savings (2.42) and investing (1.98)."
- "Age significantly correlates with budgeting, savings, investing, and debt management."
- "Most teachers (74%) have no other income sources beyond salary."

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


## "Budgeting Practices and Challenges of Micro-Entrepreneurs in Maria Aurora Public Market: Toward a Strategic Management Plan"
**Filename:** `L--Delos_Santos-et_al_summarized.md`  
**Authors:** "Delos Santos, D.T.; Austria, M.G.P.; Candelario, C.C.; Garcia, L.E.B.; Gonaranao, B.S." (2026)  
**ID:** `10.4898/jener.v2i3.a32`  
**Odin Topics:** 3.A, 3.B, 7.A, 13.A, 13.B  

**TLDR:** "Micro-entrepreneurs in Maria Aurora Public Market exhibit high financial discipline in income utilization, expense tracking, savings, and financial planning but face major challenges from debt burdens, inflation, and irregular income."

**Problem & Motivation:** "Micro-entrepreneurs in rural Philippine public markets often lack structured budgeting systems, hindering their sustainability and growth despite being economic backbones. Existing research does not focus specifically on Maria Aurora's vendors, leaving a gap in localized understanding of their financial practices and barriers."

**Approach (summary):**
- "Descriptive quantitative design with 68 micro-entrepreneurs sampled via simple random lottery from a population of 82 stall owners, food vendors, and retailers."
- "Self-constructed Likert-scale survey covering four budgeting dimensions (income utilization, expense tracking, savings, financial planning) and two challenge dimensions (financial liability, income generation)."
- "Data analyzed using frequency counts, average weighted means (AWM), and verbal interpretation scales (Never to Always for practices; Not a Challenge to Major Challenge for obstacles)."

**Key Findings (selected):**
- "num: Overall income utilization AWM=3.63 (Always), expense tracking AWM=3.48 (Always), savings AWM=3.49 (Always), financial planning AWM=3.57 (Always)."
- "num: Financial liability AWM=3.27 (Major Challenge), income generation AWM=3.40 (Major Challenge)."
- "num: Highest-ranked practice: setting financial goals (AWM=3.77)."
- "num: Lowest-ranked practice: categorizing expenses into fixed vs variable costs (AWM=3.20)."

**Limitations / Contradictions for Odin:**
- "Single-site study (Maria Aurora Public Market) limits external validity."
- "Reliance on self-reported Likert scales may introduce social desirability and recall bias. [unacknowledged]"
- "Mixed methods promised in introduction but only quantitative data collected; no qualitative triangulation. [unacknowledged]"

**Key takeaways:**
- "Income utilization discipline is high with AWM=3.63 (Always)."
- "Managing multiple debts is the top financial liability challenge (AWM=3.42)."
- "Only 3.22 AWM for depositing savings in banks shows low formal integration."

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
- num: Rational consumers with fixed obligatory consumption will go to ruin regardless of utility function concavity.
- num: With impulsive consumption and minimum subsistence, probability of avoiding ruin decays exponentially as exp(-cT) for sufficiently large T.
- num: Lookahead of k steps yields utility advantage of Ω(k) over no lookahead under bounded income.
- Algorithmic persuasion and obligatory consumption create value capture, where consumers adopt externally imposed values without critical reflection.

**Limitations / Contradictions for Odin:**
- "Model uses simple intertemporal consumption framework without debt or liabilities."
- "Does not incorporate behavioral economics insights like present bias or loss aversion."
- "Macroeconomic factors like inflation and recessions not modeled."

**Key takeaways:**
- Fixed obligatory consumption guarantees financial ruin even for rational agents.
- Algorithmic impulse triggers make ruin exponentially more likely over time.
- Knowing work schedules 2 weeks ahead yields significantly higher utility.

---


## Analysis of the Food and Income Expenditure Survey 2023 Among Filipino Households
**Filename:** `L--Ama_summarized.md`  
**Authors:** Ama, Nathan Andrie (2025)  
**ID:** `10.20944/preprints202508.0349.v1`  
**Odin Topics:** 3.A, 6.A, 6.B, 7.A, 7.B  

**TLDR:** Analysis of 163,268 Filipino households shows food expenditure is income inelastic (elasticity 0.58), rural households spend more on food than urban, and bread and meat dominate food spending.

**Problem & Motivation:** Food constitutes the largest household expenditure in the Philippines, yet understanding how income, geography, and household characteristics drive food spending patterns is limited. Existing studies lack integrated spatial and predictive analysis of food insecurity. This gap hinders targeted food security and poverty policies.

**Approach (summary):**
- Data from 2023 Family Income and Expenditure Survey (FIES) of 163,268 Filipino households.
- Principal Component Analysis (PCA) identified dominant income sources: retail, transport, farming, and remittances.
- Spatial mapping at province level revealed clustering of food expenditure across regions.

**Key Findings (selected):**
- "num: Income elasticity of food expenditure is 0.58, indicating food is a necessity good."
- "num: Rural households spend a median of ₱102,467 on food vs urban ₱80,700 (p<.001)."
- "num: GAM explained 27.2% deviance in food insecurity, with per capita income as strongest predictor (edf=6.71, χ²=16,981.31, p<.001)."
- Bread accounts for 29.5% of food spending, followed by meat (14.8%) and fish (14.2%).

**Limitations / Contradictions for Odin:**
- Cross-sectional design limits causal interpretation.
- Lacks dietary diversity and nutritional status measures [unacknowledged] in relation to PFMS.
- Spatial analysis only at province level, obscuring intra-provincial disparities.

**Key takeaways:**
- Food spending elasticity is 0.58, confirming Engel's law for Filipino households.
- Rural households spend more on food than urban households despite lower expectations.
- Bread and meat dominate Filipino food budgets, accounting for over 44% of food spending.

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
- num: Users who followed AI recommendations increased average monthly savings by 12–18%.
- num: 45% of users reduced discretionary spending on non-essential items.
- num: Overspending prediction engine achieved approximately 85% precision.
- num: API response times under 200 ms provided a responsive user experience.

**Limitations / Contradictions for Odin:**
- "Manual transaction entry creates user adoption friction."
- "Lacks direct banking integration, planned for future using open banking APIs."
- "Initial recommendation engine performance required real-world data to improve [unacknowledged]."

**Key takeaways:**
- "AI recommendations increased savings by 12-18% for active users."
- "Multilingual support boosted usability for 87% of non-English speakers."
- "Interactive dashboards drive more frequent financial engagement."

---


## Development and Evaluation of My Money Manager: An Intelligent Mobile App for Personalized Financial Insight
**Filename:** `I--Parameswaran-&-Saad_summarized.md`  
**Authors:** Parameswaran, S.; Saad, S. Z. (2025)  
**ID:** `10.32890/jdsd2025.3.2.9`  
**Odin Topics:** 3.A, 3.B, 8.A, 9.A, 9.B, 12.A, 13.A  

**TLDR:** My Money Manager mobile app uses algorithmic expense categorization and 90-day spending analysis to provide personalized savings recommendations and anomaly detection, with a usability study showing high effectiveness in tracking and habit improvement.

**Problem & Motivation:** Existing personal finance apps lack intelligent analysis and personalized guidance, often offering generic one-size-fits-all advice that fails to account for individual spending patterns. Most apps do not differentiate fixed versus variable expenses or detect abnormal spending behaviors, leading to irrelevant recommendations.

**Approach (summary):**
- Iterative and incremental development methodology with agile principles and user-centered design.
- Android app following Model-View-Controller pattern and Material Design guidelines.
- Key calculations: monthly income, expenses, savings, income/expense ratio, budget status, category expense, and category percentage.

**Key Findings (selected):**
- "num: 82.8% of users confirmed income and expense tracking was efficient and reliable."
- "num: 74.3% reported the app encouraged them to manage finances more effectively."
- "num: 71.4% agreed that financial insights helped guide their financial decision-making."
- "num: 77.1% rated navigation, adding entries, and setting budgets as very easy (strongly agree)."

**Limitations / Contradictions for Odin:**
- "Small sample size (n=35) limits statistical power and generalizability."
- "No longitudinal follow-up to assess sustained behavior change or retention."
- "Financial insights comprehension was problematic for 14.3% of users, but no redesign was tested. [unacknowledged]"

**Key takeaways:**
- "82.8% of users found income and expense tracking reliable."
- "74.3% reported improved financial management habits."
- "Only 37.1% strongly agreed financial insights were easy to understand."

---


## Simple Financial Management in Housewife Communities: A Qualitative Study on Daily Financial Management Patterns
**Filename:** `I--Efendi-&-Widagdo_summarized.md`  
**Authors:** Efendi, M. I.; Widagdo, C. S. (2025)  
**ID:** `10.59890/ijaeam.v3i3.18`  
**Odin Topics:** 1.C, 2.A, 2.B, 3.A, 5.A, 7.A, 13.A, 13.B  

**TLDR:** Housewives in Salatiga develop adaptive financial strategies including informal recording, expenditure prioritization, community-based savings groups, and risk management despite limited formal literacy.

**Problem & Motivation:** Housewives manage daily household finances but have lower formal financial literacy (36.1% vs 40.6% for men) and face structural disadvantages. Research overlooks their sophisticated adaptive strategies and community-based financial systems.

**Approach (summary):**
- Qualitative case study in Salatiga, Central Java, involving 25 housewives as primary financial managers.
- Data collection through semi-structured interviews (60-90 minutes), non-participant observation of community activities, and document analysis.
- Analysis using ATLAS.ti with open, axial, and selective coding, plus member checking for validation.

**Key Findings (selected):**
- num: 5 of 8 informants perform routine manual expense recording; others use mental envelopes or digital apps inconsistently.
- Housewives prioritize primary needs (food, school fees, bills) over secondary and tertiary needs using mental accounting.
- Strategies include gradual purchasing, cash buffers (e.g., Rp50,000), and informal shop credit for liquidity gaps.
- Income diversification through home-based activities yields Rp300,000–Rp500,000 monthly additional income.

**Limitations / Contradictions for Odin:**
- "Small sample (25 housewives) from one city limits external validity."
- "Self-reported financial practices may suffer from social desirability bias. [unacknowledged]"
- "No longitudinal data to assess stability of adaptive strategies over time. [unacknowledged]"

**Key takeaways:**
- "num: 5 of 8 housewives manually record expenses; others use envelope systems."
- "Community arisan groups act as forced savings with social discipline."
- "Housewives create micro emergency funds of Rp50,000 to Rp200,000."

---


## Unraveling the Retirement Spending Habits in Siquijor, Philippines: Promoting Support Policies for Retirees
**Filename:** `L--Mansueto-et_al_summarized.md`  
**Authors:** Mansueto, R. R.; Juguilon, J. L. A.; Jumawan, R. C.; Pelegrin, M. A. L. (2025)  
**ID:** `10.32996/jbms.2025.7.2.6`  
**Odin Topics:** 2.A, 3.A, 3.B, 13.A, 13.B  

**TLDR:** Retirees in Siquijor prioritize utilities and groceries over housing, spend moderately on medications, and allocate little to emergency savings or insurance.

**Problem & Motivation:** Financial literacy gaps leave many retirees unprepared for post-employment life. Understanding how retirees in Siquijor allocate financial resources is needed to inform policy interventions. This study addresses the lack of detailed spending pattern data for this population.

**Approach (summary):**
- Purposive sample of 179 retirees permanently out of the workforce in Siquijor, Philippines.
- Structured survey using Likert scale (1-5) to rate spending frequency across 14 expense categories.
- Weighted mean and composite mean analysis to summarize spending frequency trends.

**Key Findings (selected):**
- "num: Utilities spending frequency weighted mean = 3.94 (Often), groceries = 3.80 (Often), housing = 3.02 (Seldom)."
- "num: Prescription medications spending = 3.60 (Often), preventive care = 3.36 (Seldom)."
- "num: Financial support to adult children/grandchildren = 3.46 (Often), gifting for occasions = 3.11 (Seldom)."
- "num: Emergency funds allocation = 3.25 (Seldom), life insurance premiums = 2.92 (Seldom)."

**Limitations / Contradictions for Odin:**
- "Sample size of 179 is moderate and purposive, not random."
- "Self-reported data may introduce recall or social desirability bias."
- "No longitudinal tracking; only cross-sectional snapshot."

**Key takeaways:**
- "Utilities (3.94) and groceries (3.80) are the top essential expenses for retirees."
- "Emergency savings allocation is low at 3.25, indicating financial vulnerability."
- "Financial support to grandchildren (3.46) is a key cultural spending category."

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


## Do Remittances Boost Household Spending: New Evidence from Migrants’ Household Survey
**Filename:** `L--Bayangos-&-Lubangco_summarized.md`  
**Authors:** Bayangos, V. B.; Lubangco, C. K. (2024)  
**ID:** `d4f8c2a1-5e6b-4c7d-9a8b-1f2e3d4c5b6a`  
**Odin Topics:** 1.C, 3.A, 5.A, 6.A, 13.A, 13.B  

**TLDR:** Remittances increase household spending in the Philippines, but financial constraints limit welfare gains for poorer households, while macroeconomic factors like exchange rates and transfer costs drive remittance flows.

**Problem & Motivation:** Understanding how remittances affect household consumption and the factors driving remittance flows is critical for maximizing development impact in remittance-dependent economies like the Philippines. Prior research leaves gaps in the nuanced relationship between remittances, consumption patterns, and macroeconomic determinants. This study provides new evidence using household surveys and financial sector data.

**Approach (summary):**
- Analyzed Survey on Overseas Filipinos (SOF) 2007-2022 (nationally representative, 1.96M OFWs in 2022) and Family Income and Expenditure Survey (FIES) 2018/2021.
- Used logistic regressions (odds ratios) to assess determinants of saving vs investing behavior of migrant households.
- Applied propensity score matching (PSM) to estimate average treatment effects of remittances on consumption shares for poor vs non-poor households.

**Key Findings (selected):**
- "num: OFW households allocated 9.9% of cash remittances to savings on average (2008-2022), while 75% allocated nothing to investments."
- "num: 57.2% of cash remittances were sent through banks in 2022; telegraphic transfer fees average 6-7% of remittance value."
- "num: A 1% increase in telegraphic transfer fees reduces cash remittances by approximately 12.5%."
- Poor remittance-receiving households show smaller shifts in expenditure shares (e.g., food reduction -1.28% vs -1.48% for non-poor).

**Limitations / Contradictions for Odin:**
- "Endogeneity between remittances and consumption may bias OLS results, though PSM partially addresses this. [unacknowledged]"
- "The SOF question on remittance allocation only started in 2008 and lacks itemized non-food categories."
- "Small sample of immigrant households (n=522) limits generalizability of comparisons."

**Key takeaways:**
- "OFW households save 9.9% of cash remittances on average, but 50% save nothing."
- "Transfer fees of 6-7% significantly reduce remittance flows."
- "Remittances increase non-food spending only for non-poor households."

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


## Family Income in Relation to Budgeting of Accounting Students in A University
**Filename:** `L--Jumawan-Powao-et_al_summarized.md`  
**Authors:** Jumawan-Powao, A. R.; Tubat, K. T.; Cellero, R. C. L.; Alibangbang, A. D. C.; Capilitan, M. K. T. (2024)  
**ID:** `10.11594/ijmaber.05.08.03`  
**Odin Topics:** 3.A, 5.A, 7.A, 13.A  

**TLDR:** Family income positively correlates with allowance but inversely relates to budgeting among accounting students, with no significant sex difference in budgeting practices.

**Problem & Motivation:** College students face growing financial management challenges, yet the relationship between family income and student budgeting remains underexplored, especially for dependents. Previous studies failed to highlight students as non‑earners while addressing sex differences. This study investigates how family income affects budgeting behavior and whether sex moderates this relationship.

**Approach (summary):**
- Quantitative descriptive‑correlation design with random sampling using Slovin’s formula.
- Sample of 269 accounting students from Jose Rizal Memorial State University.
- Modified survey questionnaire with 4‑point Likert scale measuring budgeting across fixed expenses, flexible expenses, and savings.

**Key Findings (selected):**
- num: Students from lower‑income families demonstrate stronger budgeting practices than those from higher‑income families.
- No significant difference in budgeting between male and female respondents (p = 0.709).
- Allowance amount is significantly related to budgeting behavior, with lower allowance associated with more careful budgeting (p = 0.001).
- Family income shows a significant positive correlation with student allowance (r = 0.265, p = 0.001).

**Limitations / Contradictions for Odin:**
- Sample confined to accounting students, limiting generalizability to non‑accounting majors. [unacknowledged]
- Self‑reported Likert scale data may not reflect actual spending behavior. [unacknowledged]
- No longitudinal tracking of budgeting changes over time.

**Key takeaways:**
- Lower family income correlates with stronger student budgeting.
- Sex does not affect budgeting behavior in this sample.
- Students prioritize savings over flexible spending.

---


## How and when does a used (vs. unused) account affect consumption behavior?
**Filename:** `I--Yin_summarized.md`  
**Authors:** Yin, S.; Sharif, M. A. (2024)  
**ID:** `10.1037/xge0001541`  
**Odin Topics:** 5.A, 3.A, 7.A  

**TLDR:** Consumers are more likely to spend remaining resources from a used account than from an unused account with the same absolute amount because they value the resources less.

**Problem & Motivation:** No prior research has examined how the mere fact that an account has been used (vs. unused) influences future spending, holding absolute balance constant. Understanding this effect is important for predicting consumer behavior in gift cards, checking accounts, and reward programs. The gap is a lack of empirical evidence on within-account relative comparisons and their behavioral consequences.

**Approach (summary):**
- Seven experimental studies (total N = 8,667) using MTurk and Prolific participants in the US.
- Manipulated used accounts (e.g., $10 left from $100 gift card) versus unused accounts ($10 gift card) across gift cards, checking accounts, and credit card reward points.
- Measured spending likelihood (0-100 scale) and perceived valuation (0-100 scale) as mediator.

**Key Findings (selected):**
- "num: Participants were more likely to spend from a used vs. unused gift card (60.6 vs. 44.8, d = 0.44, p < .001)."
- "num: Valuation significantly mediated the used vs. unused effect on spending (a´b = -0.91, 95% CI [-1.96, -0.025])."
- "num: The effect strengthened as the proportion remaining decreased: spending likelihood dropped 7.99 points per 20% decrease in remaining proportion in used accounts (p < .001)."
- When no original amount was specified, participants spent as if the account was used, not unused.

**Limitations / Contradictions for Odin:**
- "Results may not generalize to non-US cultures or languages. [unacknowledged]"
- "The effect was not tested with very large account sizes (e.g., thousands of dollars). [unacknowledged]"
- "Studies primarily used forced-choice spending scenarios; real-world longitudinal behavior not observed."

**Key takeaways:**
- "Used accounts increase spending likelihood by 15-16 percentage points over unused accounts."
- "Lower perceived valuation of remaining resources mediates the used-account effect."
- "Spending rises as the remaining proportion drops from 60% to 20% in used accounts."

---


## Impact of financial literacy, mental budgeting and self control on financial wellbeing: Mediating impact of investment decision making
**Filename:** `I--Bai_summarized.md`  
**Authors:** Bai, R. (2023)  
**ID:** `10.1371/journal.pone.0294466`  
**Odin Topics:** 3.A, 5.A  

**TLDR:** Financial literacy, mental budgeting, and self-control positively affect subjective financial wellbeing, with investment decision making partially mediating these relationships.

**Problem & Motivation:** Financial stress harms mental health and productivity. Understanding cognitive factors like financial literacy, mental budgeting, and self-control that influence subjective financial wellbeing is needed. The mediating role of investment decision making in these relationships has not been fully examined.

**Approach (summary):**
- Data were collected from 449 Chinese university students via convenience sampling using physical and electronic channels.
- The study employed Partial Least Squares Structural Equation Modeling (PLS-SEM) for path analysis and mediation testing.
- Financial literacy was measured with 7 items, mental budgeting with 4 items, and self-control with 5 items from the Brief Self-Control Scale.

**Key Findings (selected):**
- num: Financial literacy has a direct positive effect on financial wellbeing (beta = 0.299, p < 0.001).
- num: Mental budgeting has a direct positive effect on financial wellbeing (beta = 0.102, p < 0.001).
- num: Self-control has a direct positive effect on financial wellbeing (beta = 0.182, p < 0.001).
- num: Investment decision making partially mediates the effect of financial literacy on financial wellbeing (indirect effect = 0.017, p = 0.034).

**Limitations / Contradictions for Odin:**
- Student sample limits generalizability to broader populations.
- Cross-sectional design cannot establish causality.
- Self-reported measures may be subject to social desirability bias.

**Key takeaways:**
- Financial literacy has direct beta 0.299 on financial wellbeing.
- Mental budgeting directly improves financial wellbeing.
- Self-control influences financial wellbeing via investment decisions.

---


## "Consumer Finance Survey 2021"
**Filename:** `L--Bangko_Sentral_ng_Pilipinas-2021_summarized.md`  
**Authors:** "Bangko Sentral ng Pilipinas" (2021)  
**ID:** `f47ac10b-58cc-4372-a567-0e02b2c3d479`  
**Odin Topics:** 1.A, 1.B, 1.C, 2.A, 2.C, 3.A, 4.A, 4.B, 5.A, 10.B, 13.A, 13.B  

**TLDR:** The 2021 Consumer Finance Survey by the Bangko Sentral ng Pilipinas provides comprehensive data on income, expenditure, assets, liabilities, and demographics of Filipino households, revealing trends in financial inclusion, digital adoption, and debt during the COVID-19 pandemic.

**Problem & Motivation:** There were significant data gaps on household wealth and indebtedness in the Philippines, as existing surveys like FIES and APIS had limited coverage of assets and liabilities. Collecting detailed financial condition data was necessary to inform evidence-based socio-economic policies and monetary decisions. The survey aimed to provide a comprehensive picture of household balance sheets, income sources, spending patterns, and demographic characteristics.

**Approach (summary):**
- "Sample of 18,000 households drawn from PSA's 2013 Master Sample (two-stage cluster sampling) covering all regions including BARMM."
- "Face-to-face interviews using structured CAPI questionnaire, translated into six major languages, conducted from March to December 2022."
- "Reference period for income and expenditure was calendar year 2021; assets and liabilities as of interview date."

**Key Findings (selected):**
- "num: 91.5% of households had wage income in 2021, up from 73.7% in 2018."
- "num: Only 29.3% of households carried any debt, down from 40.4% in 2018."
- "num: 35.3% owned deposit accounts, significantly up from 9.7% in 2018."
- "num: 24.3% owned electronic money accounts, up from 0.3% in 2018."

**Limitations / Contradictions for Odin:**
- "Estimates with coefficients of variation above 20 percent should be interpreted with caution."
- "Recall bias may affect income and expenditure values reported for the previous year."
- "Non-sampling errors from intentional under-reporting of assets and liabilities. [unacknowledged]"

**Key takeaways:**
- "Wage income source increased to 91.5% of households during the pandemic."
- "Debt prevalence dropped to 29.3% as households reduced borrowing."
- "Digital financial assets grew rapidly: e-money accounts up to 24.3%."

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
- num: Expense classification accuracy rated 4.2/5 by users.
- num: Overall user satisfaction score 4.4/5.
- num: Ease of use rated 4.5/5.
- Predictive models struggle with irregular income and fluctuating spending patterns.

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


## Leveraging Big Data Analytics in Behavioral Finance: Insights into Consumer Spending and Saving Dynamics
**Filename:** `I--Ying-&-Blaise_summarized.md`  
**Authors:** Ying, H.; Blaise, M. (0)  
**ID:** `5c9a5e3a-8b4a-5c1e-9f2d-4a7b8c9d0e1f`  
**Odin Topics:** 2.B, 3.A, 5.A, 6.A, 10.A, 10.B, 11.A, 13.A  

**TLDR:** Big data analytics combined with behavioral finance reveals how psychological biases and digital footprints influence consumer spending and saving patterns, enabling personalized financial strategies.

**Problem & Motivation:** Traditional financial models assume rational decision-making and overlook psychological, social, and contextual drivers of consumer behavior. This gap limits the ability to design effective personalized financial products and interventions. The paper argues that big data techniques can capture these multidimensional factors at scale to improve financial inclusion and resilience.

**Approach (summary):**
- Reviews the characteristics of big data (volume, velocity, variety, veracity) in financial contexts.
- Identifies data sources: transaction histories, social media, mobile apps, surveys, and web analytics.
- Proposes descriptive, predictive, and prescriptive analytics to uncover spending and saving patterns.

**Key Findings (selected):**
- Big data enables segmentation of consumers based on spending habits and cognitive biases.
- Predictive analytics can forecast future spending behaviors from historical transaction data.
- Social media sentiment analysis provides contextual insights that influence spending decisions.
- Automated savings programs that analyze spending patterns can increase saving rates.

**Limitations / Contradictions for Odin:**
- The paper is a non‑empirical review without original experiments or data.
- No specific machine learning model or evaluation metrics are provided.
- Ethical concerns like algorithmic bias are raised but no mitigation strategies are proposed [unacknowledged].

**Key takeaways:**
- Big data reveals hidden psychological drivers of consumer spending.
- Behavioral segmentation enables personalized financial products and alerts.
- Predictive analytics forecasts spending patterns from transaction history.

---


## Note for the Agent

The summaries above contain **essential extracts** – enough to understand each paper's relevance to Odin, including supporting evidence and limitations.
If you need additional details not shown here (e.g., **critical citations, definitions, equations, full methodology, or the complete mapping rationale**),
**ask the user to send the original summary file (`<filename>_summarized.md`) or the converted MarkItDown file(`<filename>_marked.md`)** for the specific paper(s) of interest.
Do not invent missing information. Acknowledge gaps when they exist.