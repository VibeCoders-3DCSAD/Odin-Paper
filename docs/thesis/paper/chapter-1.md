# Chapter 1: Introduction (Draft V4)

> **Status of this draft**
>
> - Supersedes `google-drive/chapter-1/GROUP4 - CHAPTER 1 - V3 - 08.28.26.docx` (V3) and the previous working draft (V2.1). V4 merges the V3 reviewer-facing document (which carries the adviser tracked changes and comments below) with the evidence-based revisions introduced in V2.1, and resolves the outstanding verification items that had supporting data available.
> - **Reviewer feedback (ERA MARIE GANNABAN, 2026-09-02, embedded in V3):** (1) state explicitly what will be classified, forecast, optimized, and flagged as anomalous; (2) state how improvements in savings and debt will be measured; (3) include discussion of survey results (e.g., "based on the survey savers do this which leads to…"); (4) state how the identified problems will be resolved. Each comment is addressed in-section and flagged below with `►RESPONSE`.
> - **Verify policy:** every external or statistical claim that is not directly supported by a cited source carries a `<!-- VERIFY: ... -->` marker. In-text citations and the reference list are drawn only from the curated intake in `Odin-Literature/literature/papers/` plus the study's own PUEPS instrument.
> - **Citation policy:** APA 7th edition. Citations are placed only where a source directly supports the claim. A per-claim audit table lives in `chapter-1-evidence-map.md` (same folder).
> - **Model families only:** classification, forecasting, optimization, and anomaly detection (per the thesis title). No named algorithms appear in the draft prose, scope, or methodology. Reference entries reproduce published titles verbatim, which is bibliographic only and not a scope commitment.
> - **Scope reconciliation with V3:** the standalone Admin Module is removed from functional scope. System Admin Module (Web) is retained, per the V3 reviewer-facing document.
> - **PUEPS results are now located** (`docs/assessment-evaluation/survey/PUEPS-responses.csv`, analysis in `PUEPS-findings.md`); Section II quotes response figures directly, resolving the earlier "findings file not located" blocker.

---

## I. Introduction

Finance management encompasses the processes and tools that individuals use to track income, plan expenses, build savings, and manage debt. Historically, it relied on manual methods such as pen-and-paper ledgers and simple mental accounting (El Hajj & Hammoud, 2023; Yadav et al., 2026). Over time, it has evolved into a digital discipline served by budgeting applications, expense trackers, and other financial management software that help individuals record transactions, monitor spending, set financial goals, and organize obligations.

Despite the availability of these tools, many individuals still find personal financial management difficult (Ganong et al., 2025). Common challenges include inconsistent expense tracking, difficulty identifying where money actually goes, unexpected expenses that disrupt planned budgets, and uncertainty about how much will be spent in the coming period. When budgets are not consistently maintained and spending is not well understood, individuals may struggle to set aside savings and may rely on debt to cover shortfalls, which can create financial vulnerability and stress (Danahy et al., 2024; Ganong et al., 2025; Wang-Ly & Newell, 2023).

Digital technology can help address these challenges through organized record-keeping, data analysis, and intelligent insights. Mobile and web applications can consolidate financial information in one place, automate repetitive tracking tasks, and present spending patterns in understandable summaries (Yadav et al., 2026). Advances in data analysis and machine learning further extend this capability by learning from a person's financial behavior, estimating future expenses from historical patterns (Chen et al., 2024; Chen & Tan, 2025), flagging unusual transactions (A. Huang et al., 2025), and proposing budget allocations that adapt to the individual rather than to a generic template.

Within this general context, the specific area of concern of this study is the improvement of personal savings and debt management. Savings provide a buffer against unexpected events and a foundation for short-term and long-term goals, while poorly managed debt can consume income, increase financial stress, and limit future opportunities (Danahy et al., 2024; Yeo et al., 2023; Yoganandham, 2025). For many Filipino working individuals, maintaining adequate savings while servicing obligations, family support, and informal financial commitments remains a persistent difficulty (Abila & Ulibas, 2026) <!-- VERIFY: the cited study covers online freelancers in Laguna only; incidence for the broader NCR target population is now supported by PUEPS findings in Section II -->.

These conditions establish the need for a personalized intelligent personal finance management application that improves Filipinos' personal savings and debt (R. Huang et al., 2025; Yadav et al., 2026). Combining organized financial record-keeping with intelligent, behavior-aware financial guidance may provide individuals with reliable information for deciding how much to save, how to allocate income, how to avoid overspending, and how to manage debt more effectively. The succeeding section describes the beneficiaries, the current process, the identified problems, and the proposed system that respond to this need.

---

## II. Project Context

Currently, Filipino young adults who live or work in the National Capital Region commonly manage their finances through manual recording in notebooks or diaries, spreadsheets, or mental tracking. In the PUEPS (2026) pre-survey, 38% of respondents reported keeping track of their finances mentally, 28% reported using spreadsheets, and 28% reported manual notebook recording; 19% reported not tracking their budget at all <!--- VERIFY: PUEPS figures transcribed from PUEPS-responses.csv (2026-09-07 export) --->. These methods are supplemented by informal practices such as *paluwagan* (rotating savings), *ambag* (shared contributions), family support, and government contributions <!-- VERIFY: confirm incidence against BSP CES 2026 or PUEPS supplementary items -->. Some use generic personal finance applications (40% reported using a mobile budgeting app such as GCash or Lista), but these are typically designed around single-account, Western-style banking and do not account for local income patterns, expenses, and cultural financial practices (Abila & Ulibas, 2026; Bangko Sentral ng Pilipinas, 2026).

Based on the constructs of the Public User Expectations and Perception Survey (PUEPS) administered by the researchers as a preliminary investigation, several difficulties were identified in the existing process. ►RESPONSE (reviewer #3): the survey results show that the majority of the 47 Filipino working adults in NCR who responded find personal financial management challenging (96%), have difficulty consistently monitoring their spending (85%), and struggle to identify where most of their money is spent (66% reported this frequently or very frequently). Unexpected or irregular expenses frequently disrupt budget plans (72%), and a majority reported that existing budgeting applications are too complex or time-consuming to maintain (68%), do not reflect Filipino financial realities and obligations (89%), provide limited useful insights or recommendations (89%), and raise privacy and data security concerns (83%). Only 53% regularly track their daily or monthly expenses, and only 26% regularly allocate part of their income toward savings or emergency funds <!-- VERIFY: figures transcribed from PUEPS-responses.csv (2026-09-07 export) -->.

These problems carry observable consequences. When spending is not consistently tracked and understood, individuals lack a reliable basis for planning, which may lead to overspending before payday, underfunding essential obligations, and failing to set aside savings. Unmonitored unusual spending may go unnoticed until it becomes a strain on the budget, and the tension between debt repayment and savings may cause individuals to defer savings or accumulate high-interest debt (Danahy et al., 2024) <!-- VERIFY: generalization beyond the debt-stress findings -->. Over time, such conditions reduce the individual's ability to build financial resilience and pursue personal goals (Ganong et al., 2025; Wang-Ly & Newell, 2023; Yeo et al., 2023).

►RESPONSE (reviewer #4): To resolve the identified problems, the study proposes the development of BUDI, a personalized intelligent PFM application for Filipino working young adults. BUDI addresses each identified difficulty directly: consistent transaction, income, obligation, and account records resolve the difficulty of monitoring spending (85%); category-level summaries and reports address knowing where the money goes (66%); spending forecasts anticipate the coming period's expenses (cited by 94% of respondents as helpful for planning); budget guidance and savings/debt features target the conflict between building savings and servicing obligations; and anomaly alerts flag unusual spending that would otherwise strain the budget (98% of respondents welcomed such alerts). Every major function is thus connected to an identified problem (R. Huang et al., 2025; Yadav et al., 2026).

►RESPONSE (reviewer #1): BUDI will support these functions through four model families, each with a defined input and output. **Classification** will assign the user a personal financial profile (classify *what*: the user's financial state, such as income stability, obligation level, and tolerance) from recorded income, expenses, obligations, and behavior. **Forecasting** will estimate future total and category-level expenses (forecast *what*: next-period spending) from chronological transaction history and income patterns. **Optimization** will propose budget allocations (optimize *what*: how available funds are distributed across categories) that respect the user's obligations and preferences. **Anomaly detection** will flag transactions that deviate from the user's established spending baseline (detect *what*: unusual or excessive spending). Models that learn from continually changing financial behavior must also remain reliable as user circumstances evolve over time (Abdullahi et al., 2025) <!-- VERIFY: applicability of the concept-drift findings to personal-finance classification -->.

---

## III. Purpose and Description of the Study

The purpose of this study is to develop BUDI, a personalized intelligent PFM application intended to help Filipino working young adults aged 20 to 40 who live or work in the National Capital Region improve their personal savings and debt management. The application aims to provide organized financial information, behavior-aware guidance, spending forecasts, and debt and savings support that are adapted to the user's actual financial situation.

BUDI will be an Android mobile application, with a React for Web companion, that works offline-first by storing financial records locally and synchronizing when connectivity is available. Its major functions include user authentication and onboarding, financial account and income source management, transaction and recurring transaction recording, financial obligation tracking, budget management, savings goal management, debt management, expense forecasting, anomaly alerts, and financial reports. Expense categories will reflect Filipino financial realities such as family support, government contributions, *paluwagan*, and *ambag*. The application will also provide privacy controls, consent management, data export, and account deletion features.

Within the system, each model processes user-provided data to produce decision-support outputs. The classification model uses the user's recorded income, expenses, obligations, and behavior to assign a financial profile; the forecasting model uses chronological transaction history, recurring expenses, obligations, and income patterns to estimate future spending for weekly, semi-monthly, or monthly periods once sufficient data is available; the optimization model incorporates the user's priorities and constraints to suggest budget allocations; and the anomaly detection model compares new transactions against the user's baseline to flag unusual spending. Every intelligent output will be accompanied by an explanation and will require user approval before any recommendation is applied.

►RESPONSE (reviewer #2): Improvement in savings and debt will be measured through observable, trackable indicators inside the application: the savings rate (the proportion of recorded income not used for expenses), the growth and completion of savings goals, the reduction of unusual-spending alerts over time, and the repayment progress of recorded debts such as outstanding loan and credit card balances. These indicators are computed from the user's recorded financial data and reported over time, so the study can document changes in saving and debt behavior attributable to using BUDI, subject to the validation items listed in the Scope and Limitations.

BUDI is expected to improve the user's financial decision-making by providing a clear picture of income, expenses, savings, and debt, and by making likely future conditions more visible. This may support more consistent budgeting, better prioritization of savings, more controlled spending, and more deliberate debt repayment. At a broader level, the study contributes to financial inclusion efforts and aligns with the United Nations Sustainable Development Goals, particularly SDG 1 (No Poverty) and SDG 8 (Decent Work and Economic Growth), by supporting the financial resilience of Filipino workers <!-- VERIFY: confirm claim alignment against the UN SDG framework wording -->.

### Objectives

The general objective of the study is to develop a personalized PFM application that helps Filipino working young adults improve their savings and debt by classifying their personal financial profile, forecasting their future spending, optimizing their budget allocations, and detecting anomalous transactions.

#### Specific Objectives

To fulfill the general objective, the researchers have constructed the following specific objectives:

1. Examine the fundamental financial management behaviors, challenges, and needs of Filipino working young adults.  
2. Explore existing finance management systems and applications, including architectural patterns, feature sets, and analytical capabilities, to identify gaps in localization, behavioral adaptation, intelligence features, and contextual sensitivity that BUDI aims to address.  
3. Analyze and preprocess data from the Bangko Sentral ng Pilipinas (BSP) Consumer Finance Survey, the Philippine Statistics Authority (PSA) Family Income and Expenditure Survey, and synthetically generated Filipino financial personas to prepare suitable datasets for model training, validation, and testing.  
4. Train and evaluate the four models of BUDI — the Personal Financial Profile Classification model, the Budget Optimization model, the Financial Forecasting model, and the Anomalous Transaction Detection model — using the following metrics:  
   1. Personal Financial Profile Classification  
      1. Accuracy  
      2. Precision  
      3. Recall  
      4. F1-Score  
   2. Budget Optimization  
      1. Constraint Satisfaction Rate (adherence to hard constraints such as budget ceiling, minimum floors, profile rules)  
      2. Budget Utilization Rate (proportion of available funds allocated)  
      3. Deviation from User Preferences (deviation of the allocation from the user's category priorities and preferences)  
   3. Financial Forecasting  
      1. Mean Absolute Error (MAE)  
      2. Symmetric Mean Absolute Percentage Error (SMAPE)  
      3. Mean Directional Accuracy (MDA)  
      4. Root Mean Square Error (RMSE)  
   4. Anomalous Expenses Detection  
      1. Accuracy  
      2. Precision  
      3. Recall  
      4. F1-Score  
5. Design the application with the following features:  
   1. User Module (Mobile):  
      1. Dashboard providing a quick overview of expense forecasts, recent transactions, budget plans and health, savings goals, debts, and anomalous transaction alerts.  
      2. User Authentication allows users to securely register, log in, log out, and recover their accounts.  
      3. User Onboarding guiding new users through profile setup, financial preferences, income, expenses, debts, accounts, and savings goals.  
      4. Transactions allow users to record, view, categorize, update, and monitor financial transactions.  
      5. Recurring Transactions allowing users to manage scheduled income, expenses, bills, and other repeated transactions.  
      6. Financial Obligations helping users track bills, essential expenses, payment schedules, and upcoming financial commitments.  
      7. Income Sources allow users to manage salaries, allowances, side income, and other sources of funds.  
      8. Financial Accounts allow users to organize and monitor cash, bank accounts, e-wallets, and other financial accounts.  
      9. Savings Goal Management for defining targets such as emergency funds, tuition, rent, medical expenses, or planned purchases; recording contributions, monitoring cumulative progress, and projecting goal completion.  
      10. Budget Management helps users create and monitor spending plans, prioritize essential expenses, and reduce the risk of underfunding necessities.  
      11. Debt Management helps users record debts, track balances and payments, compare repayment strategies, view payoff projections, and identify potential debt risks caused by insufficient budgets or known upcoming expenses.  
      12. Settings allow users to manage their profile, preferences, notifications, security, and application configurations.  
      13. Anomaly Alerts identifying unusual expenses and notifying users of spending patterns that differ from their normal financial behavior.  
      14. Financial Forecasting providing personalized total and category-level spending forecasts based on each user's categorized transaction history, recurring expenses, financial obligations, and income patterns for weekly, semi-monthly, or monthly periods once sufficient data is available.  
   2. System Admin Module (Web):  
      1. System Admin Authentication allows system administrators to securely log in and access authorized system-management functions.  
      2. System Monitoring for monitoring system health, user and transaction volumes, availability, P99 latency, throttling events, errors, and heavy system loads.  
      3. System Admin Settings allowing system administrators to change their password and log out of the system.  
6. Test the functionality, performance efficiency, usability, and reliability of the system.  
7. Evaluate the system using metrics based on the ISO/IEC 25010 software quality model. The evaluation will cover:  
   1. ISO/IEC 25010:  
      1. Functional suitability: completeness, correctness, and appropriateness;  
      2. Performance efficiency: response time, latency, throughput, and capacity;  
      3. Reliability: availability, fault tolerance, and recoverability;  
      4. Security: confidentiality, integrity, and authenticity;  
      5. Portability: adaptability and installability.  
8. Deploy the personal finance management application to the mobile platform and document its result.

---

## IV. Scope and Limitations

The study will be conducted in the National Capital Region (NCR), Philippines, which serves as the geographical research locale. The intended users are Filipino working young adults aged 20 to 40 who live or work in NCR and who face financial obligations, savings, and debt concerns (Bangko Sentral ng Pilipinas, 2026; PUEPS, 2026) <!-- VERIFY: specific NCR figures -->. The locale and demographic are relevant because they reflect the income patterns, cost of living, digital habits, and financial practices that the application is designed to support, as captured in the PUEPS survey instrument.

The functional scope of BUDI covers the user-facing modules of an Android mobile application: identity and account management, onboarding and financial profile assessment, financial account management, income and obligation management, transaction and recurring transaction management, budget management, savings goal management, debt management, expense forecasting, anomaly alerts, financial reports, and privacy-related functions such as consent, data export, and account deletion. The application will support offline transaction entry through local storage and synchronize changes when connectivity becomes available.

The technical scope includes the four models previously described. Candidate algorithms for each family may be evaluated during the data modeling phase, and the final selection for each model will be based on the study's defined evaluation metrics, computational requirements, interpretability, and suitability for integration into the application. Forecasting will be limited to periods and category levels where sufficient historical observations are available, anomaly alerts will be based on the user's recorded financial baseline, and all recommendations will be presented as decision-support information subject to user approval. The application will be developed with React for Web, the Expo and React Native toolchain for Android, an Express.js and Node.js backend, and Supabase/PostgreSQL with local SQLite for offline synchronization.

The study is limited in several respects. Findings may not fully represent Filipino working individuals outside NCR, non-working individuals, users outside the age range, or users with substantially different financial conditions. The public Philippine datasets used are primarily household-level or aggregate data (e.g., the Bangko Sentral ng Pilipinas consumer surveys (Bangko Sentral ng Pilipinas, 2026) and the Philippine Statistics Authority Family Income and Expenditure Survey <!-- VERIFY: confirm exact dataset years and access date -->) without complete individual transaction histories, so synthetic personas and transactions will be generated for model training and evaluation, and model performance on synthetic data may differ from real-world performance. Because the application relies on manual financial data entry, it does not include bank or e-wallet API integration, automatic transaction importing, receipt scanning, or credit-score monitoring, and the quality of intelligent outputs depends on the completeness and accuracy of user-entered records. The application is developed primarily for the Android platform, with development and distribution in other platforms such as iOS outside the scope of this study. BUDI is intended to provide financial decision support and not licensed financial, investment, tax, or legal advice, and savings and debt features remain subject to further validation from the PUEPS findings and subject matter expert consultation.

---

## V. Operational Definition of Terms

This section defines the significant terminologies operationally, based on how they are identified, processed, measured, and utilized within the BUDI personal finance management application.

**Anomaly** - A transaction or spending pattern that substantially differs from the user's established financial behavior based on the system's anomaly-detection threshold.

**Anomaly Alert** - A notification presented to the user when one or more transactions are flagged by the anomaly detection model as deviating from the user's normal spending patterns.

**Anomaly Detection** - The model family that analyzes transaction records to identify unusual spending amounts, frequencies, categories, or patterns relative to the user's financial baseline.

**Budget** - The planned allocation of a user's available income among expense and savings categories for a specified period.

**Budget Optimization** - The model family that proposes spending and savings allocations that respect the user's obligations, constraints, and preferences.

**Classification** - The model family that assigns a user a personal financial profile based on measured financial indicators such as income level, spending pattern, savings behavior, recurring obligations, and transaction history.

**Debt** - A recorded financial obligation that the user must repay, including loans, credit card balances, and other borrowed amounts.

**Expense Categorization** - The system's process of assigning each recorded expense to a predefined category based on the transaction description, transaction type, or user-selected classification.

**Financial Forecasting** - The model family that estimates future financial values or trends using historical, chronologically arranged transaction data processed by the applicable model.

**Financial Obligation** - A recurring or required payment recorded by the user, including bills, loans, rent, subscriptions, government contributions, and other scheduled financial commitments.

**Financial Profile** - The classification of a user based on measurable financial indicators and recorded financial behavior, used to personalize guidance and recommendations.

**Income** - The total monetary inflows recorded in the system during a specified period, identified through transactions classified as salary, allowance, business income, or other sources of funds.

**Optimization** - The model family that determines allocations or recommendations that best satisfy the user's goals, constraints, and preferences.

**Personal Finance Management (PFM)** - A system or application that helps individuals manage their personal finances, including budgeting, expense tracking, savings, debt management, and financial planning.

**Savings** - The portion of recorded income that is not used for expenses during a specified period, determined by comparing the user's recorded income with recorded expenses and savings transactions.

**Spending Pattern** - The observable trends and regularities in a user's recorded transactions, including recurring expenses, category distributions, and timing of expenditures, which provide the basis for classification, forecasting, optimization, anomaly detection, and budget guidance.

**Synthetic Financial Data** - Artificially generated transaction records used to test the system and evaluate its model functions when actual user financial records are unavailable or insufficient.

**Time-Series Data** - The user's financial transaction records arranged chronologically according to their recorded dates, enabling analysis of changes in income, expenses, savings, and spending behavior over time.

**Transaction Data** - The recorded financial entries entered into the system, including date, amount, description, category, and transaction type, which serve as the primary data source for analysis and prediction.

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