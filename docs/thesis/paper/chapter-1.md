# Chapter 1: Introduction (Draft V5)

> **Status of this draft**
>
> - Supersedes the team working draft (V4) and is reconciled against Drive `GROUP4 - CHAPTER 1 - V4 - 09.13.26.docx`, which carried the adviser's embedded comments and suggestions (ERA MARIE GANNABAN, 2026-09-04) and the inline annotations in the Google Doc.
> - Structure, formatting, section navigation, title structuring, and prose clarity were benchmarked against the reference thesis `formats-templates/chapter-1/Reference Thesis (Group 10).docx` (a CS thesis from an earlier batch recommended by the adviser), and adapted to BUDI's consumer-application setting.
> - **Adviser feedback addressed in this draft** (full log in `chapter-1-evidence-map.md`): (1) name the models/algorithms planned and discuss how each will function on the key features; (2) define "category-level" forecasts; (3) clarify what recurring transactions cover; (4) explain how financial accounts are monitored; (5) detail the debt repayment-strategy comparison; (6) add user account management; (7) replace "Reliability" with "Usability" in the ISO/IEC 25010 evaluation block and include its sub-characteristics; (8) name the app-store counterpart for deployment; (9) split "technical scope" from the software toolchain; (10) match the limitations to the objectives, project context, and purpose; (11) keep the National Capital Region locale but make the purposive-sampling approach and respondent distribution explicit; (12) state how the study will collect and obtain approval for the public datasets used.
> - **Scope decisions confirmed with the team (2026-09-13):** the official four-model title is retained; the National Capital Region remains the geographic locale with purposive sampling made explicit; candidate algorithms are named (SVM, SARIMA, Linear Programming/HiGHS, IQR) with final selection left open pending comparative evaluation.
> - **Verify policy:** every external or statistical claim that is not directly supported by a cited source carries a `<!-- VERIFY: ... -->` marker. PUEPS figures were re-transcribed and re-confirmed against `PUEPS-responses.csv` (2026-09-13). In-text citations and the reference list are drawn only from the curated intake in `Odin-Literature/literature/papers/` plus the study's own PUEPS instrument. See `chapter-1-evidence-map.md` for the claim-by-claim audit.

---

## I. Introduction

Finance management encompasses the processes and tools that individuals use to track income, plan expenses, build savings, and manage debt. Historically, individuals managed their personal finances through manual methods such as pen-and-paper ledgers and mental accounting (El Hajj & Hammoud, 2023; Yadav et al., 2026). Over time, financial management has evolved into a digital discipline served by budgeting applications, expense trackers, and other financial management software that help individuals record transactions, monitor spending, set financial goals, and organize obligations.

Despite the availability of these tools, many individuals still find personal financial management difficult (Ganong et al., 2025). Common challenges include inconsistent expense tracking, difficulty identifying where money actually goes, unexpected expenses that disrupt planned budgets, and uncertainty about how much will be spent in the coming period. When budgets are not consistently maintained and spending is not well understood, individuals may struggle to set aside savings and may rely on debt to cover shortfalls, conditions that can create financial vulnerability and stress (Danahy et al., 2024; Ganong et al., 2025; Wang-Ly & Newell, 2023).

Digital technology can help address these challenges through organized record-keeping, data analysis, and intelligent insights. Mobile and web applications can consolidate financial information in one place, automate repetitive tracking tasks, and present spending patterns in understandable summaries (Yadav et al., 2026). Advances in data analysis and machine learning extend this capability further by learning from a person's financial behavior, estimating future expenses from historical patterns (Chen et al., 2024; Chen & Tan, 2025), flagging unusual transactions (A. Huang et al., 2025), and proposing budget allocations that adapt to the individual rather than to a generic template. Applied together, these techniques can move a personal finance application beyond passive record-keeping toward behavior-aware guidance for budgeting, saving, and debt management.

Within this general context, the specific area of concern of this study is the improvement of personal savings and debt management. Savings provide a buffer against unexpected events and a foundation for short-term and long-term goals, while poorly managed debt can consume income, increase financial stress, and limit future opportunities (Danahy et al., 2024; Yeo et al., 2023; Yoganandham, 2025). For many Filipino working individuals, maintaining adequate savings while servicing obligations, family support, and informal financial commitments remains a persistent difficulty (Abila & Ulibas, 2026) <!-- VERIFY: the cited study covers online freelancers in Laguna only; incidence for the broader NCR target population is supported by the PUEPS findings cited in the Project Context -->.

These conditions establish the need for a personalized intelligent personal finance management application that improves Filipinos' personal savings and debt (R. Huang et al., 2025; Yadav et al., 2026). Combining organized financial record-keeping with intelligent, behavior-aware financial guidance may provide individuals with reliable information for deciding how much to save, how to allocate income, how to avoid overspending, and how to manage debt more effectively. The succeeding section describes the beneficiaries, the current process, the identified problems, and the proposed system that respond to this need.

---

## II. Project Context

Currently, Filipino working young adults aged 20 to 40 who live or work in the National Capital Region commonly manage their finances through manual recording in notebooks or diaries, through spreadsheets, or through mental tracking. In the PUEPS (2026) pre-survey, 38% of respondents reported keeping track of their finances mentally, 28% reported using spreadsheets, 28% reported manual notebook recording, and 19% reported not tracking their budget at all; 40% reported using a mobile budgeting application such as GCash or Lista. These methods are supplemented by informal practices such as *paluwagan* (rotating savings), *ambag* (shared contributions), family support, and government contributions, which most commercial applications do not capture. The age band of 20 to 40 was adopted because consumer data from the Bangko Sentral ng Pilipinas (2026) indicate that younger, digitally connected Filipino workers are among the most active users of mobile and digital finance services, making them the primary adopters of an application-centered approach to savings and debt <!-- VERIFY: confirm the specific digital-finance uptake figures from the cited BSP report -->. Because the National Capital Region covers a large and heterogeneous population, the survey component of this study uses purposive sampling among working young adults within the region; the PUEPS respondents (47 valid responses) were drawn primarily from Taguig, Pasay, Manila, and Makati.

Based on the constructs of the Public User Expectations and Perception Survey (PUEPS), a pre-survey administered by the researchers as preliminary investigation, several difficulties were confirmed in the existing process. The large majority of respondents (95.7%, 45 out of 47) agreed that managing personal finances is challenging, and 85.1% (40 out of 47) reported difficulty in consistently monitoring their spending. Difficulty in identifying where money actually goes was also common: 66.0% (31 out of 47) experienced this frequently or very frequently, and 80.9% (38 out of 47) at least occasionally. Unexpected or irregular financial obligations emerged as a near-universal disruptor rather than an edge case: 72.3% (34 out of 47) reported that such obligations negatively affect their budgeting frequently or very frequently, and 97.9% (46 out of 47) at least occasionally. Respondents also reported that existing budgeting methods and tools are too complex or time-consuming to maintain regularly (68.1%, 32 out of 47), do not reflect Filipino financial realities and obligations (89.4%, 42 out of 47), provide limited useful insights or recommendations (89.4%, 42 out of 47), and raise privacy and security concerns that discourage full use (83.0%, 39 out of 47). These findings indicate that the core difficulty is not simply inconsistent tracking, but a structural mismatch between existing tools and the irregular, obligation-heavy financial patterns typical of Filipino working young adults.

These problems carry observable consequences. When spending is not consistently tracked and understood, individuals lack a reliable basis for planning, which may lead to overspending before payday, underfunding essential obligations, and failing to set aside savings. This pattern is reflected in the PUEPS results: only 68.1% (32 out of 47) of respondents reported allocating part of their income toward savings every salary period or often, meaning roughly one-third allocated savings only sometimes, rarely, or never. Unmonitored unusual spending may likewise go unnoticed until it strains the budget, and the tension between debt repayment and savings accumulation may cause individuals to defer savings or rely on higher-cost debt (Danahy et al., 2024). Over time, such conditions reduce the individual's ability to build financial resilience and pursue personal goals (Ganong et al., 2025; Wang-Ly & Newell, 2023; Yeo et al., 2023).

To address these concerns, the study proposes the development of BUDI, a personalized intelligent personal finance management (PFM) application for Filipino working young adults in the National Capital Region. BUDI will help individuals track and monitor their income and expenses, manage savings and debt, maintain budgets, and act on spending forecasts and alerts for unusual spending. More specifically, the system will provide structured transaction, income, and obligation records; financial accounts; Filipino-context expense categories; savings goal and debt management; budget guidance; spending forecasts; and alerts for unusual spending. Every major function is connected to an identified problem: consistent recording addresses the difficulty of monitoring spending; category-level summaries and reports address the difficulty of knowing where the money goes; spending forecasts anticipate irregular and seasonal expense spikes before they occur; savings goal and budget features target the conflict between accumulating savings and servicing obligations; anomaly alerts flag unusual spending as it happens rather than only in hindsight; and privacy controls, consent management, data export, and account deletion respond to respondent concerns about financial data security.

BUDI will support these functions through four model families, each with a defined input and output. **Classification** will assign the user a personal financial profile from recorded income, expenses, obligations, and spending behavior, providing the basis for personalized guidance. **Forecasting** will estimate future total and category-level expenses from the user's chronological transaction history, income patterns, and recurring obligations. **Optimization** will propose budget allocations that respect the user's obligations, savings targets, and preferences (Hu et al., 2023). **Anomaly detection** will flag transactions that deviate from the user's established spending baseline and notify the user through anomaly alerts. Because the models must remain reliable as user circumstances change over time, each family will be evaluated during the data modeling phase (Abdullahi et al., 2025) <!-- VERIFY: applicability of the concept-drift findings to personal-finance classification -->; the candidate algorithms and how each is expected to function on the key features are described in the succeeding section.

---

## III. Purpose and Description of the Study

The purpose of this study is to develop BUDI, a personalized intelligent PFM application intended to help Filipino working young adults aged 20 to 40 who live or work in the National Capital Region improve their personal savings and debt management. The application aims to provide organized financial information, behavior-aware guidance, spending forecasts, and debt and savings support that are adapted to the user's actual financial situation. Specifically, the study addresses related concerns: how to model the user's financial profile, how much and when the user is likely to spend, how available income should be allocated across expenses, obligations, and savings, and how unusual spending that threatens the budget should be identified, so that savings and debt outcomes improve over time.

BUDI will be an Android mobile application, with a React for Web companion, that works offline-first by storing financial records locally and synchronizing through a Supabase/PostgreSQL backend when connectivity is available. Its major functions include user authentication and account management, onboarding and financial profile assessment, financial account and income source management, transaction and recurring transaction recording, financial obligation tracking, budget management, savings goal management, debt management, expense forecasting, anomaly alerts, and financial reports, together with system-admin monitoring functions on the web. Expense categories will reflect Filipino financial realities such as family support, government contributions, *paluwagan*, and *ambag*. The application will also provide privacy controls, consent management, data export, and account deletion, designed in accordance with Republic Act No. 10173 (Data Privacy Act of 2012) and its implementing rules and regulations as enforced by the National Privacy Commission.

Within the system, the researchers will utilize and evaluate candidate algorithms for each model family, and each model will function directly on the feature it supports. The candidate considered for personal financial profile classification is a **Support Vector Machine (SVM)**, which will take the user's recorded income, expenses, obligations, and spending behavior as input and assign a financial profile used to personalize guidance and alerts. The candidate for financial forecasting is a **Seasonal Autoregressive Integrated Moving Average (SARIMA)** model, which will fit the user's chronological transaction history to estimate future total and category-level expenses for weekly, semi-monthly, or monthly periods once sufficient observations are available. The candidate for budget optimization is a **Linear Programming (LP)** formulation solved with the **HiGHS** solver, which will allocate available income across expense and savings categories while treating user-defined savings targets and essential obligations as hard constraints. The candidate for anomaly detection is an **Interquartile Range (IQR)-based statistical threshold**, which will compare each new transaction against the user's recorded baseline and flag spending that falls outside the established range. The final algorithm for each family will be selected during the data modeling phase based on comparative performance against the metrics in Specific Objective 4. All model outputs will be presented as decision-support information accompanied by an explanation and will be applied only with the user's approval.

Improvement in savings and debt will be measured through observable, trackable indicators computed from the user's recorded financial data: the savings rate (the proportion of recorded income not used for expenses), the growth and completion of savings goals, the reduction in unusual-spending alerts over time, and the repayment progress of recorded debts such as outstanding loan and credit card balances. These indicators are computed from the user's recorded transactions and reported over time, allowing the study to document changes in saving and debt behavior attributable to using BUDI, subject to the validation items listed in the Scope and Limitations. The same indicators correspond to the features respondents valued most: 94% considered spending forecasts helpful for planning, 98% welcomed alerts for unusual spending, and 100% wanted personalized suggestions with explanations (PUEPS, 2026).

BUDI is expected to improve the user's financial decision-making by providing a clear picture of income, expenses, savings, and debt, and by making likely future conditions more visible. This may support more consistent budgeting, better prioritization of savings, more controlled spending, and more deliberate debt repayment. Beyond the individual user, the study contributes to financial inclusion efforts in the Philippines by adapting intelligent financial tools to local income patterns and obligations, and it aligns with the United Nations Sustainable Development Goals, particularly SDG 1 (No Poverty) and SDG 8 (Decent Work and Economic Growth), by supporting the financial resilience of Filipino workers <!-- VERIFY: confirm claim alignment against the UN SDG framework wording -->.

### General Objectives

The general objective of the study is to develop BUDI, a personalized intelligent PFM application for Filipino working young adults aged 20 to 40 who live or work in the National Capital Region, using classification, forecasting, optimization, and anomaly detection models to improve their personal savings and debt management. The system aims to classify the user's personal financial profile, forecast future spending, optimize budget allocations, and detect anomalous transactions in a way that supports, rather than replaces, the user's financial decisions.

#### Specific Objectives

To fulfill the general objective, the researchers have constructed the following specific objectives:

1. Examine the fundamental financial management behaviors, challenges, and needs of Filipino working young adults aged 20 to 40 in the National Capital Region, using the PUEPS pre-survey as preliminary investigation.  
2. Explore existing finance management systems and applications, including architectural patterns, feature sets, and analytical capabilities, to identify gaps in localization, behavioral adaptation, intelligence features, and contextual sensitivity that BUDI aims to address, including a comparative review of algorithms commonly applied to financial classification, forecasting, optimization, and anomaly detection tasks in existing literature.  
3. Analyze and preprocess data from the Bangko Sentral ng Pilipinas (BSP) Consumer Finance Survey, the Philippine Statistics Authority (PSA) Family Income and Expenditure Survey, and synthetically generated Filipino financial personas to prepare suitable datasets for model training, validation, and testing. Publicly available reports and microdata from the BSP and the PSA Data Archive (PSADA) will be used; survey responses collected directly by the researchers will be handled under the study's informed-consent and data-protection procedures.  
4. Train and evaluate the four models of BUDI — the Personal Financial Profile Classification model, the Budget Optimization model, the Financial Forecasting model, and the Anomalous Transaction Detection model — using the following candidate algorithms and metrics, with the final algorithm for each family selected based on comparative performance:  
   1. Personal Financial Profile Classification (candidate: Support Vector Machine):  
      1. Accuracy  
      2. Precision  
      3. Recall  
      4. F1-Score  
   2. Budget Optimization (candidate: Linear Programming solved with the HiGHS solver):  
      1. Constraint Satisfaction Rate (adherence to hard constraints such as budget ceiling, minimum floors, profile rules)  
      2. Budget Utilization Rate (proportion of available funds allocated)  
      3. Deviation from User Preferences (deviation of the allocation from the user's category priorities and preferences)  
   3. Financial Forecasting (candidate: Seasonal Autoregressive Integrated Moving Average):  
      1. Mean Absolute Error (MAE)  
      2. Symmetric Mean Absolute Percentage Error (SMAPE)  
      3. Mean Directional Accuracy (MDA)  
      4. Root Mean Square Error (RMSE)  
   4. Anomalous Expense Detection (candidate: Interquartile Range-based statistical threshold):  
      1. Accuracy  
      2. Precision  
      3. Recall  
      4. F1-Score  
5. Design the application with the following features:  
   1. User Module (Mobile):  
      1. Dashboard – provides a quick overview of expense forecasts, recent transactions, budget plans and health, savings goals, debts, and anomalous transaction alerts.  
      2. User Authentication – allows users to securely register, log in, log out, and recover their accounts.  
      3. User Account Management – allows users to manage their account and profile information.  
      4. User Onboarding – guides new users through profile setup, financial preferences, income sources, expense categories, financial accounts, current savings goals, and current debts.  
      5. Transactions – allows users to record, view, categorize, update, and monitor income and expense transactions.  
      6. Recurring Transactions – allows users to manage scheduled income such as salaries and allowances, scheduled expenses such as subscriptions and bills, savings contributions, and debt repayments.  
      7. Financial Obligations – allows users to create, update, and delete current bills, essential expenses, payment schedules, and upcoming financial commitments.  
      8. Income Sources – allows users to manage salaries, allowances, side income, and other sources of earnings.  
      9. Financial Accounts – allows users to organize and monitor cash, bank accounts, and e-wallets based on recorded transactions and balances (without bank or e-wallet API integration).  
      10. Savings Goal Management – allows users to define targets such as emergency funds, tuition, rent, medical expenses, or planned purchases; record contributions; monitor cumulative progress; and project goal completion.  
      11. Budget Management – allows users to create and monitor spending plans, prioritize essential expenses, and reduce the risk of underfunding necessities.  
      12. Debt Management – allows users to record debts, track balances and payments, compare repayment strategies such as the snowball or avalanche methods to project payoff timelines, and identify potential debt risks caused by insufficient budgets or known upcoming expenses.  
      13. User Settings – allows users to manage their profile, preferences, notifications, security, and application configurations.  
      14. Anomaly Alerts – allows users to receive notifications of unusual expenses and spending patterns that differ from their normal financial behavior.  
      15. Financial Forecasting – allows users to view personalized total and category-level spending forecasts based on each user's categorized transaction history, recurring expenses, financial obligations, and income patterns, for weekly, semi-monthly, or monthly periods once sufficient data is available.  
      16. Financial Reports – allows users to view summaries and reports of income, expenses, savings, and debt for specified periods and categories.  
   2. System Admin Module (Web):  
      1. System Admin Authentication – allows system administrators to securely log in and access authorized system-management functions.  
      2. System Monitoring – monitors system health, user and transaction volumes, availability, latency, throttling events, errors, and heavy loads.  
      3. System Admin Settings – allows system administrators to change their password and log out of the system.  
6. Test the functionality, performance efficiency, usability, reliability, and security of the system.  
7. Evaluate the system using the System Usability Scale (SUS) and metrics based on the ISO/IEC 25010 software quality model. The evaluation will cover:  
   1. ISO/IEC 25010:  
      1. Functional Suitability: completeness, correctness, and appropriateness;  
      2. Performance Efficiency: response time, latency, throughput, and capacity;  
      3. Reliability: availability, fault tolerance, and recoverability;  
      4. Security: confidentiality, integrity, and authenticity;  
      5. Portability: adaptability and installability;  
      6. Usability: appropriateness recognizability, learnability, user error protection, user interface aesthetics, and accessibility.  
8. Deploy the personalized intelligent finance management application to the Android platform through the Google Play Store and document its result.

---

## IV. Scope and Limitations

### Scope

The primary focus of this study is the development of BUDI, a personalized intelligent PFM application for Filipino working young adults aged 20 to 40 who live or work in the National Capital Region (NCR), Philippines, which serves as the geographical research locale. The locale and demographic are relevant because they reflect the income patterns, cost of living, digital habits, and financial practices that the application is designed to support, as captured in the Bangko Sentral ng Pilipinas consumer surveys and the study's PUEPS instrument (Bangko Sentral ng Pilipinas, 2026; PUEPS, 2026). Because the NCR covers a large and heterogeneous population, the survey component uses purposive sampling among working young adults within the region; PUEPS respondents were drawn primarily from Taguig, Pasay, Manila, and Makati. The study and its system development activities are conducted during the 2025–2026 academic year.

The functional scope of BUDI covers the user-facing modules of the Android mobile application: user authentication and account management, onboarding and financial profile assessment, financial account and income source management, transaction and recurring transaction management, financial obligation management, budget management, savings goal management, debt management, expense forecasting, anomaly alerts, and financial reports, together with privacy-related functions such as consent management, data export, and account deletion, and the system-admin monitoring functions on the web. This list corresponds exactly to the features enumerated in Specific Objective 5. The application will support offline transaction entry through local storage and synchronize changes when connectivity becomes available.

The technical scope of the study covers the four model families and the data used to develop them. Candidate algorithms for classification (Support Vector Machine), forecasting (Seasonal Autoregressive Integrated Moving Average), optimization (Linear Programming with the HiGHS solver), and anomaly detection (Interquartile Range-based thresholding) will be evaluated during the data modeling phase, and the final algorithm for each family will be selected based on the evaluation metrics defined in Specific Objective 4, computational requirements, interpretability, and suitability for integration into the application. Training data will be drawn from publicly available Philippine sources — the Bangko Sentral ng Pilipinas Consumer Finance Survey and the Philippine Statistics Authority Family Income and Expenditure Survey, including microdata accessed through the PSA Data Archive (PSADA) <!-- VERIFY: confirm exact dataset years and access date --> — and from synthetically generated Filipino financial personas, together with the study's own PUEPS responses collected under informed consent. Forecasting will be limited to periods and categories where sufficient historical observations are available, anomaly alerts will be based on the user's recorded financial baseline, and all model outputs will be presented as decision-support information subject to user approval. Separately, the application will be developed with React for Web, the Expo and React Native toolchain for Android, an Express.js and Node.js backend, and Supabase/PostgreSQL with local SQLite for offline synchronization; these are the software tools of the development platform and are distinct from the models and data described above.

### Limitations

The study is limited in several respects, and each limitation is acknowledged against the corresponding objective, project context, or purpose.

The PUEPS pre-survey is based on purposive sampling of 47 respondents in the National Capital Region, drawn primarily from Taguig, Pasay, Manila, and Makati; findings may not fully represent Filipino working individuals outside the region, non-working individuals, users outside the 20-to-40 age range, or users with substantially different financial conditions.

The public Philippine datasets used are primarily household-level or aggregate data without complete individual transaction histories, so synthetic personas and transactions will be generated for model training and evaluation; model performance on synthetic data may differ from real-world performance.

Because the application relies on manual financial data entry, it does not include bank or e-wallet API integration, automatic transaction importing, receipt scanning, or credit-score monitoring; recorded balances are monitored through user-entered transactions, and the quality of model outputs depends on the completeness and accuracy of user-entered records.

Forecasts are limited to periods and categories with sufficient historical data, and anomaly alerts reflect the user's recorded baseline rather than external behavior; the models may not fully anticipate sudden changes in income or spending, and models that learn from continually changing financial behavior must remain reliable as user circumstances evolve (Abdullahi et al., 2025) <!-- VERIFY: applicability of the concept-drift findings to personal-finance classification -->.

The application is developed primarily for the Android platform, with development and distribution on other platforms such as iOS outside the scope of this study.

BUDI is intended to provide financial decision support and not licensed financial, investment, tax, or legal advice; savings and debt features remain subject to further validation from the PUEPS findings and subject matter expert consultation.

---

## V. Operational Definition of Terms

This specific section of the paper defines significant terminologies operationally, based on how they are identified, processed, measured, and utilized within the BUDI personal finance management application.

**Anomaly** – A transaction or spending pattern that substantially differs from the user's established financial behavior based on the system's anomaly-detection threshold.

**Anomaly Alert** – A notification presented to the user when one or more transactions are flagged by the anomaly detection model as deviating from the user's normal spending patterns.

**Anomaly Detection** – The model family that analyzes transaction records to identify unusual spending amounts, frequencies, categories, or patterns relative to the user's financial baseline.

**Budget** – The planned allocation of a user's available income among expense and savings categories for a specified period.

**Budget Optimization** – The model family that proposes spending and savings allocations that respect the user's obligations, constraints, and preferences.

**Category-Level Spending Forecast** – An estimate of future spending for a specific expense category (e.g., food, transportation, utilities, family support) derived from the user's categorized transaction history.

**Classification** – The model family that assigns a user a personal financial profile based on measured financial indicators such as income level, spending pattern, savings behavior, recurring obligations, and transaction history.

**Debt** – A recorded financial obligation that the user must repay, including loans, credit card balances, and other borrowed amounts.

**Expense Categorization** – The system's process of assigning each recorded expense to a predefined category based on the transaction description, transaction type, or user-selected classification.

**Financial Forecasting** – The model family that estimates future financial values or trends using historical, chronologically arranged transaction data processed by the applicable model.

**Financial Obligation** – A recurring or required payment recorded by the user, including bills, loans, rent, subscriptions, government contributions, and other scheduled financial commitments.

**Financial Profile** – The classification of a user based on measurable financial indicators and recorded financial behavior, used to personalize guidance and recommendations.

**Income** – The total monetary inflows recorded in the system during a specified period, identified through transactions classified as salary, allowance, business income, or other sources of funds.

**Optimization** – The model family that determines allocations or recommendations that best satisfy the user's goals, constraints, and preferences.

**Personal Finance Management (PFM)** – A system or application that helps individuals manage their personal finances, including budgeting, expense tracking, savings, debt management, and financial planning.

**Purposive Sampling** – A non-probability sampling technique in which respondents are selected based on specific criteria relevant to the research objectives. In this study, it was used to select Filipino working young adults aged 20 to 40 in the National Capital Region who are relevant to the personal savings and debt context of the study.

**Recurring Transaction** – A scheduled income, expense, savings, or debt transaction that repeats at defined intervals (e.g., weekly, semi-monthly, monthly) without requiring the user to manually re-enter it each period.

**Savings** – The portion of recorded income that is not used for expenses during a specified period, determined by comparing the user's recorded income with recorded expenses and savings transactions.

**Spending Pattern** – The observable trends and regularities in a user's recorded transactions, including recurring expenses, category distributions, and timing of expenditures, which provide the basis for classification, forecasting, optimization, anomaly detection, and budget guidance.

**Synthetic Financial Data** – Artificially generated transaction records used to test the system and evaluate its model functions when actual user financial records are unavailable or insufficient.

---

## References

Abdullahi, M., Alhussian, H., Aziz, N., Abdulkadir, S. J., Baashar, Y., Alashhab, A. A., & Afrin, A. (2025). A systematic literature review of concept drift mitigation in time-series applications. *IEEE Access*. https://doi.org/10.1109/ACCESS.2025.3587231

Abila, J. P., & Ulibas, R. (2026). Analyzing the financial management practices and resilience of online freelancers in Laguna amid digital platform taxation. *International Journal of Multidisciplinary Educational Research and Innovation, 4*(2), Article 9.

Bangko Sentral ng Pilipinas. (2026). *Consumer expectations survey report: 2nd quarter 2026*. Monetary and Economics Sector, Department of Economic Statistics.

Chen, J., Chen, T., Wang, Y., & Wang, L. (2024). A survey of time series data forecasting methods based on deep learning. *Journal of Basic and Applied Research International, 30*(6), 140–157.

Chen, S., & Tan, W. (2025). LSTM-based consumer behavior prediction model research. In *Proceedings of the 2025 2nd International Conference on Digital Economy and Computer Science (DECS 2025)*.

Danahy, R., Lillard, D., Loibl, C., & Montalto, C. P. (2024). Financial stress among college students: New data about student loan debt, lack of emergency savings, social and personal resources. *Journal of Consumer Affairs*. https://doi.org/10.1111/joca.12581

El Hajj, M., & Hammoud, J. (2023). Unveiling the influence of artificial intelligence and machine learning on financial markets: A comprehensive analysis of AI applications in trading, risk management, and financial operations. *Journal of Risk and Financial Management, 16*(10), Article 434. https://doi.org/10.3390/jrfm16100434

Ganong, P., Noel, P. J., Patterson, C., Vavra, J. S., & Weinberg, A. (2025). *Earnings instability* (Working Paper No. 34227). National Bureau of Economic Research.

Hu, X., Lee, J. C. H., & Lee, J. H. M. (2023). Two-stage predict+optimize for mixed integer linear programs with unknown parameters in constraints. In *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*.

Huang, A., Zhang, X., Wang, Y., Tsai, S., Zhou, P., & Chen, L. (2025). Dynamic calibration of decision thresholds for financial anomaly detection: Verification with payment platform information and data. *Journal of Global Information Management, 33*(1).

Huang, R., Zhao, Z., Chen, S., Wu, X., & Zhao, J. L. (2025). Wealth-Voyager: Navigating intelligent wealth management with a multi-agent framework. In *Proceedings of the 2025 International Conference on Generative Artificial Intelligence for Business (GAIB 2025)*.

PUEPS. (2026). *ODIN public user expectations and perception survey (Responses)* [Data set]. Research Group 4, College of Computing and Information Sciences, University of Makati.

Wang-Ly, N., & Newell, B. R. (2023). *How income volatility influences saving decisions: Evidence from the lab* (SSRN Working Paper No. 4509925). https://ssrn.com/abstract=4509925

Yadav, S., Kumar, V., & Maurya, A. (2026). Intelligent personal finance management system for smart budgeting and real-time expense tracking: Design and development. *International Scientific Journal of Engineering and Management, 5*(4). https://doi.org/10.55041/ISJEM06330

Yeo, K. H. K., Lim, W. M., & Yii, K.-J. (2023). Financial planning behaviour: A systematic literature review and new theory development. *Journal of Financial Services Marketing, 29*, 979–1001. https://doi.org/10.1057/s41264-023-00249-1

Yoganandham, G. (2025). Mastering economic and financial sources with reference to budgeting, savings, early investing, debt management and the power of financial planning – A comprehensive analysis. *Degres Journal*.