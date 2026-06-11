# Comprehensive Report for Subtopic: `3.A`

**Total relevant papers:** 26

This report includes problem/motivation, approach, key findings, support for Odin, and limitations/contradictions.

---


## AI-Enabled NLP Framework for Automated Expense Management and Financial Analysis
**Filename:** `IA--Jayaprakashnarayan-et_al_summarized.md`  
**Authors:** Jayaprakashnarayan, N.; Sakthivel, M.; Sachidhanandam, P.; Kanjana Devi, N.; Manivel Mughilan, T.S. (2026)  
**ID:** `10.15662/IJEETR.2026.0802073`  
**Odin Topics:** 3.A, 3.B, 8.A, 8.B, 10.A, 10.B, 12.A, 12.B  

**TLDR:** An AI-enabled NLP framework using transformer-based models and multi-task learning automates transaction extraction (96.8% accuracy) and categorization (94.3% merchant precision) from financial SMS messages with on-device privacy.

**Problem & Motivation:** Digital payments generate overwhelming transaction data, making personal finance management complex and error-prone. Existing rule-based or supervised systems are brittle, unable to adapt to changing message formats or evolving fraud patterns. There is a need for a self-adaptive, privacy-preserving NLP framework that operates on mobile devices.

**Approach (summary):**
- Curated dataset of 124,583 financial SMS messages from 250 Indian participants across 42 banks and 18 UPI apps, annotated with transaction entities and 14 expense categories.
- Hybrid architecture combining MuRIL transformer encoder (12 layers, 768 hidden) with rule-based verification for entity extraction and multi-task learning for classification.
- Multi-task objective jointly optimizes token-level CRF for entities and sequence-level softmax for expense categories, with dynamic loss weights (0.7/0.3).

**Key Findings (selected):**
- num: 96.8% overall F1-score for transaction entity extraction (proposed MuRIL multi-task vs 94.0% for FinBERT).
- num: 94.3% precision in merchant identification across code-mixed and varied formats.
- num: 91.7% sensitivity and 3.8% false positive rate for ensemble fraud detection (AUC-ROC 0.956).
- num: 85.6% reduction in manual expense tracking effort based on user-reported time savings.

**Supports Odin (direct justifications):**
- The proposed NLP framework achieves 96.8% accuracy in extracting transaction entities from financial SMS messages.
- Multi-task learning improves transaction classification F1 by 1.2% over single-task fine-tuning.
- Ensemble fraud detection achieves 91.7% sensitivity with only 3.8% false positives, suitable for user-facing alerts.

**Limitations / Contradictions for Odin:**
- Geographic generalizability not evaluated; results may not transfer to non-Indian payment ecosystems. [unacknowledged]
- On-device model quantization causes 1.3% accuracy loss compared to full-precision model, affecting millions of transactions.
- Battery impact of 2% per hour on low-end devices may reduce user adoption for high-volume users (300+ daily transactions).

**Key takeaways:**
- Transaction extraction achieves 96.8% F1 using transformer multi-task learning on Indian financial SMS.
- Ensemble fraud detection yields 91.7% sensitivity with only 3.8% false positives.
- On-device processing reduces manual expense tracking effort by 85.6% while preserving privacy.

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


## Financial Literacy of Public Secondary School Teachers in San Francisco District, Camotes Island, Cebu, Philippines
**Filename:** `L--Montuerto-&-Ferrater-Gimena_summarized.md`  
**Authors:** Montuerto, J. E.; Ferrater-Gimena, J. A. O. (2026)  
**ID:** `10.5281/zenodo.18438866`  
**Odin Topics:** 1.C, 3.A, 7.A, 13.A, 13.B  

**TLDR:** Public secondary school teachers in San Francisco District, Camotes Island demonstrate moderate financial literacy in budgeting, spending, and credit management, but low literacy in savings and investing.

**Problem & Motivation:** Public school teachers in the Philippines face financial difficulties including budget deficits, debt cycles, and reliance on loans. Financial literacy is essential for personal financial management and effective teaching of financial education, yet limited research exists on rural public school teachers' financial literacy.

**Approach (summary):**
- Descriptive-correlational design with 150 teachers from three national high schools.
- {'Researcher-made survey with two parts': 'demographic profile and financial literacy items (budgeting, savings, investing, spending, credit/debt).'}
- Cronbach's alpha of 0.885 confirmed reliability.

**Key Findings (selected):**
- num: 42% of respondents were aged 24-32 years (mean 36.11), 78.67% female, 68% married, 74% had no other income sources.
- num: Budgeting aggregate mean 2.96 (moderate), savings 2.42 (low), investing 1.98 (low), spending 3.17 (moderate), credit/debt 3.05 (moderate).
- num: Age significantly related to budgeting (p=0.004), savings (p=0.001), investing (p=0.0001), and credit/debt (p=0.001).
- num: Educational attainment significantly related to savings (p=0.038) and credit/debt (p=0.001).

**Supports Odin (direct justifications):**
- Public school teachers allocate earnings primarily to essential household commodities (weighted mean 3.39).
- Teachers save only 20% of earnings for emergencies (weighted mean 2.79) and show low savings account use (2.44).
- Teachers lack correct investment knowledge (2.21) and avoid Bitcoin/online investments (1.70).

**Limitations / Contradictions for Odin:**
- Small sample from one rural district; may not represent urban teachers. [unacknowledged]
- Cross-sectional design; causality cannot be inferred. [unacknowledged]
- Self-reported survey data may overstate financial literacy due to social desirability bias. [unacknowledged]

**Key takeaways:**
- Teachers showed low financial literacy in savings (2.42) and investing (1.98).
- Age significantly correlates with budgeting, savings, investing, and debt management.
- Most teachers (74%) have no other income sources beyond salary.

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


## Budgeting Practices and Challenges of Micro-Entrepreneurs in Maria Aurora Public Market: Toward a Strategic Management Plan
**Filename:** `L--Delos_Santos-et_al_summarized.md`  
**Authors:** Delos Santos, D.T.; Austria, M.G.P.; Candelario, C.C.; Garcia, L.E.B.; Gonaranao, B.S. (2026)  
**ID:** `10.4898/jener.v2i3.a32`  
**Odin Topics:** 3.A, 3.B, 7.A, 13.A, 13.B  

**TLDR:** Micro-entrepreneurs in Maria Aurora Public Market exhibit high financial discipline in income utilization, expense tracking, savings, and financial planning but face major challenges from debt burdens, inflation, and irregular income.

**Problem & Motivation:** Micro-entrepreneurs in rural Philippine public markets often lack structured budgeting systems, hindering their sustainability and growth despite being economic backbones. Existing research does not focus specifically on Maria Aurora's vendors, leaving a gap in localized understanding of their financial practices and barriers.

**Approach (summary):**
- Descriptive quantitative design with 68 micro-entrepreneurs sampled via simple random lottery from a population of 82 stall owners, food vendors, and retailers.
- Self-constructed Likert-scale survey covering four budgeting dimensions (income utilization, expense tracking, savings, financial planning) and two challenge dimensions (financial liability, income generation).
- Data analyzed using frequency counts, average weighted means (AWM), and verbal interpretation scales (Never to Always for practices; Not a Challenge to Major Challenge for obstacles).

**Key Findings (selected):**
- num: Overall income utilization AWM=3.63 (Always), expense tracking AWM=3.48 (Always), savings AWM=3.49 (Always), financial planning AWM=3.57 (Always).
- num: Financial liability AWM=3.27 (Major Challenge), income generation AWM=3.40 (Major Challenge).
- num: Highest-ranked practice: setting financial goals (AWM=3.77).
- num: Lowest-ranked practice: categorizing expenses into fixed vs variable costs (AWM=3.20).

**Supports Odin (direct justifications):**
- Micro-entrepreneurs struggle to categorize expenses into fixed and variable costs, justifying automated expense categorization in Odin.
- High debt repayment pressure reduces capital for business needs, supporting a debt management module with repayment planning.
- Low tendency to deposit savings in banks (AWM=3.22) indicates Odin should facilitate micro-savings accounts with low barriers.

**Limitations / Contradictions for Odin:**
- Single-site study (Maria Aurora Public Market) limits external validity.
- Reliance on self-reported Likert scales may introduce social desirability and recall bias. [unacknowledged]
- Mixed methods promised in introduction but only quantitative data collected; no qualitative triangulation. [unacknowledged]

**Key takeaways:**
- Income utilization discipline is high with AWM=3.63 (Always).
- Managing multiple debts is the top financial liability challenge (AWM=3.42).
- Only 3.22 AWM for depositing savings in banks shows low formal integration.

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


## Proof of concept of centralized personal finance application
**Filename:** `I--Sipila_summarized.md`  
**Authors:** Sipilä, M. (2025)  
**ID:** `5c3a2f1e-4b6d-4c8e-9a7b-2d1f3e4a5b6c`  
**Odin Topics:** 3.A, 3.B, 4.A, 4.B, 12.A  

**TLDR:** Design and development of a centralized personal finance proof-of-concept application using DSRM, consolidating asset tracking, cash flow visualization, and automated reporting to reduce manual effort and errors for a stakeholder.

**Problem & Motivation:** Personal finance management is hindered by fragmented tools and manual processes that cause errors and scalability issues. Existing applications focus on narrow functions and lack centralized data integration. A proof-of-concept is needed to automate updates and provide unified financial oversight.

**Approach (summary):**
- Followed Design Science Research Methodology (DSRM) with stakeholder questionnaire and iterative feedback.
- Developed a Flutter frontend, .NET backend, and MongoDB database for asset tracking, cash flow, and PDF reports.
- Integrated Google Sheets API for stock prices and HexaRate API for daily exchange rates.

**Key Findings (selected):**
- The proof-of-concept eliminated manual spreadsheet formula errors and reduced repetitive data entry.
- Stakeholder reported high satisfaction with automated visualizations and PDF report generation.
- All 'must have' functional requirements were met except authentication, which was deferred.
- System improved data reliability and user confidence compared to fragmented baseline tools.

**Supports Odin (direct justifications):**
- Manual financial tracking systems are prone to errors and do not scale.
- Automated data retrieval reduces user workload and improves data reliability.
- Task-based testing is an effective evaluation method for PFM prototypes.

**Limitations / Contradictions for Odin:**
- No user authentication or authorization implemented, a critical security gap for financial data.
- Full automation of bank/broker data fetching not achieved; still requires manual CSV or form input for transactions.
- Evaluated with only one stakeholder, limiting external validity.

**Key takeaways:**
- Centralized PFM reduces error-prone manual consolidation across tools.
- Automated stock price and exchange rate fetching saves significant time.
- DSRM provides an effective structured process for prototype development.

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


## Enhancing Financial Literacy in Young Adults: An Android-Based Personal Finance Management Tool
**Filename:** `I--Imawan-et_al_summarized.md`  
**Authors:** Imawan, R.; Putra, W. P.; Alqahtani, R.; Milakis, E. D.; Dumchykov, M. (2025)  
**ID:** `10.58536/j-hytel.166`  
**Odin Topics:** 3.A, 3.B, 9.A, 9.B, 11.A, 11.B, 12.A, 13.A  

**TLDR:** An Android-based personal finance management app for young adults features income/expense tracking, budgeting, goal setting, and notifications, achieving a 4.6/5 usability score.

**Problem & Motivation:** Young adults face unique financial challenges including limited experience and high online loan usage. Existing financial tools overlook the interactive, mobile-first needs of this demographic. Without targeted intervention, financial illiteracy may perpetuate debt and instability.

**Approach (summary):**
- Waterfall model used for systematic development with phases: requirements analysis, design, implementation, testing, deployment.
- Requirements gathered via interviews and surveys with Indonesian higher education students to identify key processes like income/expense tracking and budget projection.
- Application built with Laravel backend, Flutter frontend, and local SQLite database for offline functionality.

**Key Findings (selected):**
- num: Overall application satisfaction score of 4.6/5, rated 'Excellent'.
- num: 78% of users rated likelihood of continued use at 4 or 5 on Likert scale.
- num: Usability aspect scored 4.72, engagement 4.74, and functionality 4.70.
- Users praised intuitive design, accurate tracking, and motivational reminders for consistent engagement.

**Supports Odin (direct justifications):**
- Mobile-first design with intuitive navigation achieves excellent usability scores (4.6/5).
- Automated notifications encourage consistent financial tracking and habit formation.
- Progress bars on financial goals motivate users to set and achieve savings targets.

**Limitations / Contradictions for Odin:**
- Short two-week evaluation period limits assessment of long-term habit formation.
- Sample of 50 Indonesian university students may not represent all young adult populations.
- No control group to isolate app effects from other factors [unacknowledged].

**Key takeaways:**
- Overall user satisfaction score of 4.6 out of 5.
- Automated notifications reinforce consistent financial tracking habits.
- Progress bars on financial goals increase user motivation.

---


## Development of Budget Management System Using Visual Basic .NET and MySQL Database: A Desktop Application for Personal Financial Tracking
**Filename:** `I--Janobe_summarized.md`  
**Authors:** Janobe, J. (2025)  
**ID:** `10.59431/jda.v4i1.660`  
**Odin Topics:** 3.A, 3.B, 4.A, 4.B, 10.A, 10.B  

**TLDR:** A desktop budget management system using Visual Basic .NET and MySQL enables offline income/expense tracking, automatic balance calculation, and local data storage for privacy.

**Problem & Motivation:** Many individuals struggle with financial discipline due to limited access to reliable, private, and offline tools. Existing cloud-based solutions raise privacy concerns and require internet connectivity, while manual methods are error-prone. There is a need for a simple, secure, desktop-based budget management system that operates offline and respects user autonomy.

**Approach (summary):**
- The system was developed following the Software Development Life Cycle (SDLC) with Visual Basic .NET 2015 and MySQL 5.7.
- It uses a two-tier client-server architecture with ADO.NET for database connectivity and the MySQL Connector/NET driver.
- The database schema (db_budget) includes a transactions table with amount, transaction_type (Received/Expense), remarks, and transaction_date fields.

**Key Findings (selected):**
- num: Performance tests showed transaction operations under 0.5 seconds and data retrieval under 1 second for up to 5,000 entries.
- The system accurately distinguishes income from expenses and calculates current balance with color-coded feedback (green for surplus, red for deficit).
- Usability testing confirmed users of varying technical backgrounds completed all tasks successfully with minimal guidance.
- The system operates fully offline, storing all data locally without internet dependency or subscription costs.

**Supports Odin (direct justifications):**
- Offline financial tracking systems can operate reliably without internet connectivity (Janobe, 2025).
- Local data storage eliminates risks of cloud-based data breaches (Janobe, 2025).
- Simple income/expense categorization with remarks suffices for basic personal finance tracking (Janobe, 2025).

**Limitations / Contradictions for Odin:**
- Manual installation process requires technical knowledge to configure MySQL via XAMPP [unacknowledged].
- Single-user design prevents collaborative household budgeting (acknowledged).
- No automated backup or export features (acknowledged).

**Key takeaways:**
- Offline operation with local storage preserves financial data privacy.
- System processes 5,000 transactions with under 1 second retrieval time.
- Simple income/expense tracking suffices for many users seeking control.

---


## Analyzing and Rewarding Credit Card Spending Habits in India: a Machine Learning Approach
**Filename:** `IA--Agrawal-et_al_summarized.md`  
**Authors:** Agrawal, R.; Khanna, A.; Hamdare, S. (2025)  
**ID:** `10.1007/s44196-025-00899-0`  
**Odin Topics:** 3.A, 5.A, 5.C, 11.A, 11.B, 12.B  

**TLDR:** K-Means clustering segments credit card users by spending habits, and a multi-factor reward points formula optimized with Random Forest achieves R2=0.99.

**Problem & Motivation:** Credit card reward programs in India use static, one-size-fits-all structures that fail to incentivize high-value discretionary spending or retain affluent customers. Existing methods lack real-time adaptability and personalization, especially during peak seasons like festivals. A data-driven framework is needed to align rewards with individual spending behaviors.

**Approach (summary):**
- Used original Kaggle dataset and generated synthetic dataset with Faker library to add features like income category, attrition risk, and expense type.
- Applied K-Means clustering to segment users into four clusters (Platinum, Gold, Silver, Signature) based on monthly spend, transaction frequency, and credit utilization.
- Engineered features including card promotion bonus, expense type bonus, income category bonus, and penalties for multiple cards to calculate reward points.

**Key Findings (selected):**
- num: Random Forest achieved R2=0.99, lowest RMSE and MAE among models.
- num: Mean reward points increased to approximately 1000 using synthetic dataset with additional features versus 400 in original.
- K-Means clustering achieved silhouette score 0.42, outperforming DBSCAN, Hierarchical, and GMM.
- Clusters clearly separated Platinum (high spending/luxury/travel) from Silver (low spending/essentials).

**Supports Odin (direct justifications):**
- K-Means clustering effectively segments users by spending behavior with silhouette score 0.42.
- Including expense type bonuses (e.g., +3 for travel) increases reward point distribution range.
- Random Forest achieves R2=0.99 for predicting reward points, minimizing prediction errors.

**Limitations / Contradictions for Odin:**
- Uses synthetic dataset instead of real credit card transaction data. [unacknowledged]
- Reward point multipliers are arbitrary and not calibrated with actual bank policies.
- Temporal analysis limited to 15 months of synthetic data, lacking long-term validation. [unacknowledged]

**Key takeaways:**
- K-Means silhouette score 0.42 outperforms DBSCAN and GMM for spending segmentation.
- Random Forest achieves R2=0.99, nearly perfect reward point prediction accuracy.
- Adding six behavioral factors expands reward range from 0-1000 to 0-3500.

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


## EMPOWERING YOUNG ADULTS THROUGH FINANCIAL MANAGEMENT: IMPLICATIONS FOR ACHIEVING THE SDGS AMONG INDONESIAN STUDENTS IN THE PHILIPPINES
**Filename:** `I--Kusumaningsih-et_al_summarized.md`  
**Authors:** Kusumaningsih, A.; Mariana; Handayani, S. (2024)  
**ID:** `f47ac10b-58cc-4372-a567-0e02b2c3d479`  
**Odin Topics:** 1.C, 3.A, 7.A, 13.A  

**TLDR:** Indonesian students in the Philippines prioritize long-term savings and use digital tools for budgeting but face uncontrolled spending and peer pressure, revealing gaps between financial knowledge and practice.

**Problem & Motivation:** International students encounter unique financial challenges such as currency fluctuations, unfamiliar banking systems, and social pressures that hinder effective money management. Poor financial handling can lead to stress and academic difficulties, yet tailored interventions for this demographic are lacking. Understanding these factors is essential to support financial well-being and contribute to poverty reduction and responsible consumption (SDGs).

**Approach (summary):**
- Qualitative descriptive design using online surveys and semi-structured interviews with Indonesian students enrolled in Philippine universities.
- Purposive sampling captured diversity in age, gender, and academic background; 88% of respondents aged 18-24, 65% female.
- Surveys included closed and open questions on budgeting, saving, investment, and technology use; interviews explored personal financial philosophies and challenges.

**Key Findings (selected):**
- num: 92% of students have long-term financial goals (savings 31.6%, investment 22.8%, further education 19.3%).
- num: Only 26.9% stick to their budget despite 85% rating financial planning as very important.
- num: 46.2% save 10% of monthly income, and 42.3% have tried investing, but 61.5% have not invested further.
- num: 63.9% use digital tools for financial management, yet only 23.1% rate them as very effective.

**Supports Odin (direct justifications):**
- Only 26.9% of young adults stick to their budget despite 85% acknowledging its importance.
- Peer influence affects 23.4% of students' spending decisions, often overriding financial plans.
- 63.9% use digital tools but only 23.1% find them very effective, indicating a usability and literacy gap.

**Limitations / Contradictions for Odin:**
- Qualitative design with limited sample size; findings may not be statistically representative. [unacknowledged]
- No longitudinal data to assess whether financial behaviors change over time. [unacknowledged]
- Relies on self‑reported data, which may be subject to social desirability bias. [unacknowledged]

**Key takeaways:**
- Only 26.9% of young adults follow their budget.
- Peer pressure is a top barrier for 23.4% of students.
- Digital tool effectiveness is perceived as low at 23.1%.

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


## Financial Practices among Foundation University Employees: Basis for Financial Plan
**Filename:** `L--Paghasian_summarized.md`  
**Authors:** Paghasian, M. F. (2024)  
**ID:** `10.69569/jip.2024.0198`  
**Odin Topics:** 1.C, 3.A, 5.A, 13.A, 13.B  

**TLDR:** Foundation University employees demonstrate strong financial practices in income management, expenditure tracking, and saving, but lack emergency funds; positive practices correlate with higher investment levels.

**Problem & Motivation:** Employees' financial practices impact well-being and job satisfaction, yet many lack adequate financial literacy and emergency funds. Understanding these practices is needed to design effective financial wellness programs.

**Approach (summary):**
- Survey of 191 regular and probationary employees at Foundation University using a validated questionnaire.
- Measured financial practices across income, expenditure, saving, and investment domains using Likert scales.
- Used weighted means, multiple linear regression, Kruskal-Wallis, and Mann-Whitney U tests for analysis.

**Key Findings (selected):**
- Employees agree on prudent income management (mean 3.81) including budgeting and avoiding debt.
- Employees lack emergency funds (mean 3.40, only moderately agree).
- Expenditure practices are strong (mean 3.83) with use of discounts and avoiding impulse buys.
- Saving practices are sound (mean 3.84) prioritizing debt reduction before saving.

**Supports Odin (direct justifications):**
- Employees with strong saving patterns allocate more to monthly investments (coef 6594.35, p=0.040).
- Only moderate agreement on seeking financial advisor advice (mean 3.17) indicates opportunity for automated guidance.
- 61.26% of employees use regular savings accounts, suggesting preference for low-risk liquid investments.

**Limitations / Contradictions for Odin:**
- Only regular and probationary employees included, not all staff.
- Confidentiality concerns led to some withheld income and investment data.
- Busy schedules caused delays and missing responses.

**Key takeaways:**
- Employees lack emergency funds despite strong other practices.
- Saving and investment practices positively predict monthly investment levels.
- Expenditure discipline negatively correlates with investment amounts.

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


## Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking
**Filename:** `I--Alenazi-&-Sas_summarized.md`  
**Authors:** Alenazi, M.; Sas, C. (2023)  
**ID:** `10.14236/ewic/BCSHCI2023.1`  
**Odin Topics:** 3.A, 3.B, 4.A, 4.B, 7.A  

**TLDR:** A functionality review of 45 top-rated budgeting apps finds that one third lack budgeting support and most fail to differentiate accounts and transactions as mental accounting theory suggests.

**Problem & Motivation:** Digital budgeting apps are popular but little research has evaluated their functionality. The gap is understanding whether apps support budgeting informed by mental accounting theory beyond simple expense tracking.

**Approach (summary):**
- Searched Google Play and Apple Store UK with keywords 'budget', 'budgeting', 'finance' yielding 1335 apps.
- Applied inclusion criteria: free, top-rated (≥4 stars, ≥1000 reviews), no bank access required, resulting in 45 apps.
- Analyzed app descriptions and performed expert evaluation of all 45 apps on Android and 5 on iOS.

**Key Findings (selected):**
- num: 33 out of 45 apps support budgeting, but only 26 use multiple budgets (money envelopes).
- num: 7 apps use a single budget for all expenses; 4 of the 26 apps offer multiple budgets only as a premium feature.
- num: 44 apps support depositing funds, 45 support expenses, but only 11 support saving accounts.
- num: 35 apps support transfer transactions between accounts.

**Supports Odin (direct justifications):**
- Budgeting apps often fail to differentiate between tracking expenses and monitoring against allocated budgets.
- Only 58% of top-rated apps use multiple budgets (money envelopes) as mental accounting theory suggests.
- Income and expense accounts are conflated in most budgeting apps, limiting accurate financial tracking.

**Limitations / Contradictions for Odin:**
- Expert evaluation may not reflect actual user behavior [unacknowledged].
- Only UK app stores, limiting cultural generalizability to Filipino users [unacknowledged].
- No evaluation of premium features or user engagement metrics [unacknowledged].

**Key takeaways:**
- One third of top budgeting apps lack proper budgeting support.
- Only 26 of 45 apps use multiple money envelopes for budgeting.
- Most apps conflate income and expense accounts.

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


## Consumer Finance Survey 2021
**Filename:** `L--Bangko_Sentral_ng_Pilipinas-2021_summarized.md`  
**Authors:** Bangko Sentral ng Pilipinas (2021)  
**ID:** `f47ac10b-58cc-4372-a567-0e02b2c3d479`  
**Odin Topics:** 1.A, 1.B, 1.C, 2.A, 2.C, 3.A, 4.A, 4.B, 5.A, 10.B, 13.A, 13.B  

**TLDR:** The 2021 Consumer Finance Survey by the Bangko Sentral ng Pilipinas provides comprehensive data on income, expenditure, assets, liabilities, and demographics of Filipino households, revealing trends in financial inclusion, digital adoption, and debt during the COVID-19 pandemic.

**Problem & Motivation:** There were significant data gaps on household wealth and indebtedness in the Philippines, as existing surveys like FIES and APIS had limited coverage of assets and liabilities. Collecting detailed financial condition data was necessary to inform evidence-based socio-economic policies and monetary decisions. The survey aimed to provide a comprehensive picture of household balance sheets, income sources, spending patterns, and demographic characteristics.

**Approach (summary):**
- Sample of 18,000 households drawn from PSA's 2013 Master Sample (two-stage cluster sampling) covering all regions including BARMM.
- Face-to-face interviews using structured CAPI questionnaire, translated into six major languages, conducted from March to December 2022.
- Reference period for income and expenditure was calendar year 2021; assets and liabilities as of interview date.

**Key Findings (selected):**
- num: 91.5% of households had wage income in 2021, up from 73.7% in 2018.
- num: Only 29.3% of households carried any debt, down from 40.4% in 2018.
- num: 35.3% owned deposit accounts, significantly up from 9.7% in 2018.
- num: 24.3% owned electronic money accounts, up from 0.3% in 2018.

**Supports Odin (direct justifications):**
- Filipino households spend 55.4% of their budget on food at home.
- Only 35.3% of households have a formal deposit account.
- E-money account ownership reached 24.3% during the pandemic.

**Limitations / Contradictions for Odin:**
- Estimates with coefficients of variation above 20 percent should be interpreted with caution.
- Recall bias may affect income and expenditure values reported for the previous year.
- Non-sampling errors from intentional under-reporting of assets and liabilities. [unacknowledged]

**Key takeaways:**
- Wage income source increased to 91.5% of households during the pandemic.
- Debt prevalence dropped to 29.3% as households reduced borrowing.
- Digital financial assets grew rapidly: e-money accounts up to 24.3%.

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