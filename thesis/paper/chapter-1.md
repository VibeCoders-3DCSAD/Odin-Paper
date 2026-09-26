# Development of BUDI: An Intelligent Personal Financial Management App Using SVM Classification, SARIMA Forecasting, LP-Based Budgeting, and IQR Anomaly Detection to Improve Filipinos' Savings and Debt

# Chapter 1: Introduction (V5, Finalized)

> **Status of this draft**
>
> - **Finalized V5.** Supersedes Draft 4.3 (and the Drive `GROUP4 - CHAPTER 1 - V5 - 09.19.26.docx` it was written to reconcile with, re-fetched 2026-09-21). Written to the style and structure of `formats-templates/chapter-1/Writing Chapter 1.md` and the reference thesis `Reference Thesis (Group 10).docx` (Introduction → Project Context → Purpose and Description → General Objectives → Specific Objectives → Scope and Limitations → Operational Definition of Terms; 4–5 paragraphs per major section), as the team's objective-style rewrite.
> - **Scope reconciled against the Drive `GROUP4 - TECHNICAL SPECIFICATION - V1 - 09.20.2026`** (re-fetched 2026-09-21): target users are **Filipinos aged 18–59 living or working in the NCR**; BUDI is a **single-user Android application** with offline-capable core features and server-side intelligent modules; the four intelligent modules use **one selected algorithm each — SVM (profile classification), SARIMA (expense forecasting), LP (budget optimization), and IQR (anomaly detection)**. The paper names the selected models and does **not** present candidate-model comparisons or describe any model as "best performing" — the selected models are simply the algorithms the study uses.
> - **⚠️ Superseded by the Drive `GROUP4 - TECHNICAL SPECIFICATION - V1 - 09.24.2026` (2026-09-24):** the spec was substantially rewritten — project identity is now **TAYA** (SARIMA-based seasonal expense forecasting; acronym words TBD), profile classification is now **rule-based** (the SVM/PFP classifier is no longer the named model), and forecasting uses **temporal disaggregation of FIES 2023 with HFCE 2022 Q1–2026 Q2** around a central Financial Plan artifact. This draft (V5) is reconciled against the older 09.20 spec and needs **re-reconciliation against 09.24** before it can be considered current.
> - **Carried decisions from the Drive V5 docx:** the V5 cover title's "Rule-Based Classification" is treated as a stale leftover; the V5's own Specific Objective 4, the 09.20 technical specification (Models table), and the trained BUDI-ML artifact (`models/pfp/tier3_svm.joblib`) all identify **SVM** as the PFP model, so this draft restores SVM in the title. V5 inline comments this draft resolves: "(how exactly?)" on the savings-and-obligations sentence; "(check if the report is still applicable for individuals aged 18-59)" on the old 20–40 BSP justification; "(needs revision, since the new scope will use one model/algorithm per intelligent module)" on the algorithm paragraph; "(revise or remove…)" on the SO2 comparative-review clause; "(revise since it uses the candidate algos)" on the technical-scope paragraph; "(only include actual operational terms…)" on the definitions intro.
> - **Missing references (corpus gaps to add in `BUDI-Literature/literature/papers/`):** no indexed paper yet for **PSA FIES**, **PSA HFCI (household financial characteristics — the tech spec alternates between "HFCI" and "HFCE"; confirm the exact dataset name, year, and version)**, **BSP CFIS (Consumer Finance and Inclusion Survey)**, or **BSP CFS (Consumer Finance Survey)**. BSP CES 2026 is in the corpus. Every claim these sources would support carries a `<!-- VERIFY: ... -->` marker until the references land.
> - **Verify policy:** every claim not directly supported by a curated intake source carries a `<!-- VERIFY: ... -->` marker. In-text citations and the reference list are drawn only from `BUDI-Literature/literature/papers/` plus the study's own PUEPS instrument. PUEPS figures were re-transcribed against `PUEPS-responses.csv` (2026-09-13). See `chapter-1-evidence-map.md`.
> - **SO6/SO7 aligned to the Drive instruments (2026-09-21):** the evaluation objectives now follow the Drive `GROUP4 - ISO 25010 - V1 - 09.15.2026` (IT-experts quality questionnaire) and `GROUP4 - SYSTEM USABILITY SCALE - V1 - 09.15.2026` questionnaires, which supersede the tech-spec 09.20 characteristics table in the previous draft. This drops Portability and the ISO-side Usability sub-list (usability is measured through SUS) and adds Maintainability. The Drive ISO instrument is a template with residual placeholder content (stray "User Error Protection"/"User Assistance" rows under Performance Efficiency) and the Drive SUS doc prints a 1–4 scale while scoring with 5-point arithmetic — both are flagged for cleaning before deployment.

---

## I. Introduction

Personal financial management (PFM) encompasses the tools, systems, applications, and processes that individuals use to manage income and expenses and to improve savings and debt allocations. Historically, individuals managed their finances through manual records and mental tracking; over time, PFM has evolved into a digital discipline served by budgeting applications, expense trackers, and other financial software that help users record transactions, monitor spending, set financial goals, and organize obligations (El Hajj & Hammoud, 2023; Yadav et al., 2026). These tools serve individuals across income levels and employment arrangements and offer varying degrees of automation and analytical capability.

Despite the availability of these tools, many individuals continue to find financial management difficult. Common challenges include inconsistent expense tracking, difficulty identifying where money actually goes, unexpected expenses that disrupt planned budgets, and uncertainty about how much will be spent in the coming period (Ganong et al., 2025). When budgets are not consistently maintained and spending is not well understood, individuals may struggle to set aside savings and may rely on debt to cover shortfalls, conditions that can create financial vulnerability and stress (Danahy et al., 2024; Ganong et al., 2025). The consequences are most visible in savings and debt outcomes: savings provide a buffer against unexpected events and a foundation for short- and long-term goals, while poorly managed debt can consume income, increase financial stress, and limit future opportunities (Yeo et al., 2023; Yoganandham, 2025).

Information systems and data-driven technologies can address these challenges through organized record-keeping, data analysis, and intelligent insights. Mobile applications can consolidate financial information in one place, automate repetitive tracking tasks, and present spending patterns in understandable summaries (Yadav et al., 2026). Machine learning extends this capability by learning from a person's financial behavior: estimating future expenses from historical patterns (Chen et al., 2024; Chen & Tan, 2025), flagging unusual transactions (A. Huang et al., 2025), and proposing budget allocations that adapt to the individual rather than a generic template. Recent reviews organize these techniques specifically for intelligent personal financial management systems (D'Souza et al., 2026). Applied together, these techniques can move a PFM application beyond passive record-keeping toward behavior-aware guidance for budgeting, saving, and debt management.

Within this general context, the specific area of concern of this study is the improvement of personal savings and debt management. For Filipino working individuals, maintaining savings while servicing household obligations, informal financial commitments, and varying income streams remains a persistent difficulty (Abila & Ulibas, 2026) <!-- VERIFY: the cited study covers online freelancers in Laguna only; incidence for the broader NCR target population is supported by the PUEPS findings cited in the Project Context -->. Existing PFM applications often emphasize generic expense tracking and budgeting. Few are localized to Filipino financial realities — including family support, informal group savings arrangements, and government-mandated contributions — and few prioritize savings and debt outcomes over general money management.

These conditions establish the need for a localized, intelligent PFM application that prioritizes savings and debt management for Filipino users aged 18 to 59 in the National Capital Region (NCR). Combining organized financial record-keeping with intelligent, behavior-aware guidance may provide individuals with reliable information for deciding how much to save, how to allocate income, how to avoid overspending, and how to manage debt more effectively (R. Huang et al., 2025; Yadav et al., 2026). By integrating profile classification, expense forecasting, budget optimization, and anomalous transaction detection within a single application, such a system can deliver personalized, data-driven support that reflects the user's actual financial circumstances. This study proposes the development and evaluation of BUDI to determine its potential in improving savings and debt outcomes among the target population.

## II. Project Context

Filipinos aged 18 to 59 who live or work in the National Capital Region commonly manage their finances through manual recording in notebooks or diaries, through spreadsheets, or through mental tracking. In the Public User Expectations and Perception Survey (PUEPS), a pre-survey administered by the researchers as preliminary investigation, 38% of the 47 respondents reported keeping track of their finances mentally, 28% reported using spreadsheets, 28% reported manual notebook recording, 19% reported not tracking their budget at all, and 40% reported using e-wallets or budgeting applications such as GCash or Lista (PUEPS, 2026). These methods are supplemented by informal practices such as *paluwagan* (rotating savings), *ambag* (shared contributions), family support, and government contributions, which most commercial applications do not capture. Consumer data from the Bangko Sentral ng Pilipinas (BSP) indicate substantial participation in mobile and digital financial services, supporting an application-centered approach to savings and debt for this user group (Bangko Sentral ng Pilipinas, 2026) <!-- VERIFY: confirm the specific digital-finance uptake figures from the cited BSP Consumer Expectations Survey report -->. Because the NCR covers a large and heterogeneous population, the survey component of this study uses purposive sampling; the 47 valid PUEPS responses were drawn primarily from Taguig, Pasay, Manila, and Makati.

Based on the constructs of the PUEPS, several difficulties were confirmed in the existing process. The large majority of respondents (95.7%, 45 out of 47) agreed that managing personal finances is challenging, and 85.1% (40 out of 47) reported difficulty in consistently monitoring their spending. Difficulty in identifying where money actually goes was also common: 66.0% (31 out of 47) experienced this frequently or very frequently, and 80.9% (38 out of 47) at least occasionally. Unexpected or irregular financial obligations affected budgeting frequently or very frequently for 72.3% (34 out of 47) of respondents, and 97.9% (46 out of 47) at least occasionally. Respondents also reported that existing budgeting methods and tools are too complex or time-consuming to maintain regularly (68.1%, 32 out of 47), do not reflect Filipino financial realities and obligations (89.4%, 42 out of 47), provide limited useful insights or recommendations (89.4%, 42 out of 47), and raise privacy and security concerns that discourage full use (83.0%, 39 out of 47) (PUEPS, 2026). These findings indicate that the core difficulty is not simply inconsistent tracking, but a structural mismatch between existing tools and the irregular, obligation-heavy financial patterns typical of the target users.

These difficulties carry observable consequences for savings and debt. When spending is not consistently tracked and understood, individuals lack a reliable basis for planning, which may lead to overspending before payday, underfunding essential obligations, and failing to set aside savings. This pattern is reflected in the PUEPS results: only 68.1% (32 out of 47) of respondents reported allocating part of their income toward savings every salary period or often, meaning roughly one-third allocated savings only sometimes, rarely, or never (PUEPS, 2026). Unmonitored unusual spending may go unnoticed until it strains the budget, and the tension between debt repayment and savings accumulation may cause individuals to defer savings or rely on higher-cost debt (Danahy et al., 2024). Over time, such conditions reduce the individual's ability to build financial resilience and pursue personal goals (Ganong et al., 2025; Wang-Ly & Newell, 2023; Yeo et al., 2023).

To address these concerns, the study proposes the development of BUDI (Bawas Utang, Dagdag Ipon), an intelligent personal financial management application for Filipinos aged 18 to 59 in the National Capital Region. BUDI will help users track income and expenses, manage savings and debt, maintain budgets, and act on spending forecasts and alerts for unusual spending. Every major function is connected to an identified problem: consistent recording addresses the difficulty of monitoring spending; category-level summaries and reports address the difficulty of knowing where the money goes; spending forecasts anticipate irregular and seasonal expense spikes before they occur; savings goal and budget features target the conflict between accumulating savings and servicing obligations; anomaly alerts flag unusual spending as it happens rather than only in hindsight; and privacy controls, consent management, data export, and account deletion respond to respondent concerns about financial data security. These capabilities correspond to the features respondents valued most: 94% considered spending forecasts helpful for planning, 98% welcomed alerts for unusual spending, and all respondents wanted personalized suggestions with explanations (PUEPS, 2026).

BUDI will support these functions through four intelligent modules: personal financial profile classification, expense forecasting, budget optimization, and anomalous transaction detection. Profile classification will assign the user a personal financial profile from recorded income, expenses, obligations, and spending behavior, providing the basis for personalized guidance. Expense forecasting will estimate future total and category-level expenses from the user's chronological transaction history, income patterns, and recurring obligations. Budget optimization will propose allocations that respect the user's obligations, savings targets, and preferences. Anomalous transaction detection will flag transactions that deviate from the user's established spending baseline and notify the user through anomaly alerts. Because these modules operate on continually recorded financial behavior, they must remain reliable as a user's circumstances change over time (Abdullahi et al., 2025) <!-- VERIFY: applicability of the concept-drift findings to personal-finance profile classification -->.

## III. Purpose and Description of the Study

The purpose of this study is to develop BUDI, an intelligent personal financial management application intended to help Filipinos aged 18 to 59 who live or work in the National Capital Region improve their personal savings and debt management. The application aims to provide organized financial information, behavior-aware guidance, spending forecasts, and savings and debt support that are adapted to the user's actual financial situation. Specifically, the study addresses four related concerns: how to model the user's financial profile, how much and when the user is likely to spend, how available income should be allocated across expenses, obligations, and savings, and how unusual spending that threatens the budget should be identified, so that savings and debt outcomes improve over time.

BUDI is an Android application built with the Expo and React Native toolchain. It works offline-first by storing financial records locally and synchronizing through a Supabase/PostgreSQL backend when connectivity is available. It is a single-user application: the only users of the system are individuals who manage their own personal finances within it, and the application does not include admin, system-admin, or web-management roles. Its major functions include user authentication and account management, user profiling, onboarding and financial profile assessment, cash flow management, recurring expense management, billers and remittances, income source management, savings goal management, budget management, debt management, expense forecasting, anomaly alerts, and financial reports. Expense categories will reflect Filipino financial realities such as family support, government contributions, paluwagan, and ambag. The application will also provide privacy controls, consent management, data export, and account deletion, designed in accordance with Republic Act No. 10173 (Data Privacy Act of 2012) and its implementing rules and regulations as enforced by the National Privacy Commission.

The system will use one selected algorithm per intelligent module, each functioning directly on the feature it supports. The Personal Financial Profile (PFP) Classification module will use the Support Vector Machine (SVM), a supervised classifier applied to income and wealth classification and to comparative evaluations of machine learning models on financial tasks (Laspiñas & Murcia, 2024; Reyes et al., 2024; Salvador, 2024) <!-- VERIFY: confirm the final venue for Salvador (2024) before submission -->; clustering-based segmentation of transaction patterns informs the feature basis for profiling (Pratama & Putri, 2024). The Expense Forecasting module will use the Seasonal Autoregressive Integrated Moving Average (SARIMA) model to analyze the user's categorized transaction history and estimate future total and category-level expenses, consistent with statistical time-series models being the standard approach for financial and expense forecasting (Sonkavde et al., 2023). The Budget Optimization module will use Linear Programming (LP) to generate budget allocations that satisfy the user's constraints and preferences, informed by constrained, data-driven budgeting formulations in the literature (Hu et al., 2023; Lu et al., 2025). The Anomalous Expense Detection module will use the Interquartile Range (IQR) method to identify transactions that fall outside the user's normal spending baseline, a statistical threshold approach evaluated in time-series and financial anomaly detection studies (Zhang et al., 2023; Zhong, 2025). All model outputs will be presented as decision-support information accompanied by explanations and will be applied only with the user's approval.

Improvement in savings and debt will be measured through observable indicators computed from the user's recorded financial data: the savings rate (the proportion of recorded income not used for expenses), the growth and completion of savings goals, the reduction in unusual-spending alerts over time, and the repayment progress of recorded debts such as outstanding loan and credit card balances. For the savings-rate indicator, debt principal repayments and transfers between the user's own accounts are treated as allocations rather than expenses, so that repaying debt does not reduce the computed savings rate. These indicators are computed from the user's recorded transactions and reported over time, allowing the study to document changes in saving and debt behavior associated with using BUDI. BUDI is expected to improve financial decision-making by providing a clear picture of income, expenses, savings, and debt and by making likely future conditions more visible, which may support more consistent budgeting, better prioritization of savings, more controlled spending, and more deliberate debt repayment. Beyond the individual user, the study contributes to financial inclusion efforts in the Philippines by adapting intelligent financial tools to local income patterns and obligations, and it aligns with the United Nations Sustainable Development Goals, particularly SDG 1 (No Poverty) and SDG 8 (Decent Work and Economic Growth) <!-- VERIFY: confirm claim alignment against the UN SDG framework wording -->.

### General Objectives

The general objective of the study is to develop BUDI, an intelligent personal financial management application for Filipinos aged 18 to 59 who live or work in the National Capital Region, using SVM profile classification, SARIMA forecasting, LP-based budgeting, and IQR anomaly detection to improve their personal savings and debt management. The system aims to classify the user's personal financial profile, forecast future spending, optimize budget allocations, and detect anomalous transactions in a way that supports, rather than replaces, the user's financial decisions.

#### Specific Objectives

To fulfill the general objective, the researchers have constructed the following specific objectives:

1. Examine the fundamental financial management behaviors, challenges, and needs of Filipinos aged 18 to 59 who live or work in the National Capital Region, using the PUEPS pre-survey as preliminary investigation.
2. Explore existing finance management systems and applications, including architectural patterns, feature sets, and analytical capabilities, to identify gaps in localization, behavioral adaptation, intelligence features, and contextual sensitivity that BUDI aims to address.
3. Analyze and preprocess data from the Bangko Sentral ng Pilipinas (BSP) consumer finance surveys, the Philippine Statistics Authority (PSA) Family Income and Expenditure Survey, and synthetically generated Filipino financial personas to prepare suitable datasets for model training, validation, and testing. Publicly available reports and microdata from the BSP and the PSA Data Archive (PSADA) will be used; survey responses collected directly by the researchers will be handled under the study's informed-consent and data-protection procedures <!-- VERIFY: confirm exact PSA/BSP dataset names (e.g., HFCI or HFCE), years, versions, and access date -->.
4. Train and evaluate the four models of BUDI — the Personal Financial Profile Classification model, the Budget Optimization model, the Expense Forecasting model, and the Anomalous Expense Detection model — using the following algorithms and metrics:
   1. Personal Financial Profile Classification (Support Vector Machine):
      1. Accuracy
      2. Precision
      3. Recall
      4. F1-Score
   2. Budget Optimization (Linear Programming):
      1. Constraint Satisfaction Rate (adherence to hard constraints such as budget ceiling, minimum floors, and profile rules)
      2. Budget Utilization Rate (proportion of available funds allocated)
      3. Deviation from User Preferences (deviation of the allocation from the user's category priorities and preferences)
   3. Expense Forecasting (Seasonal Autoregressive Integrated Moving Average, SARIMA):
      1. Mean Absolute Error (MAE)
      2. Symmetric Mean Absolute Percentage Error (SMAPE)
      3. Mean Directional Accuracy (MDA)
      4. Root Mean Square Error (RMSE)
   4. Anomalous Expense Detection (Interquartile Range, IQR):
      1. Accuracy
      2. Precision
      3. Recall
      4. F1-Score
5. Design the application with the following features:
   1. Dashboard – provides a quick overview of expense forecasts, recent transactions, budget plans and health, savings goals, debts, and anomalous transaction alerts.
   2. User Authentication – allows users to securely register, log in, log out, and recover their accounts.
   3. User Profiling – allows users to complete a financial behavior questionnaire and receive a personalized profile that identifies their saver type and borrower type, helping tailor recommendations, budget plans, and savings and debt guidance to their habits.
   4. User Onboarding – guides new users through financial preferences, income sources, expense categories, current savings goals, and current debts.
   5. Cash Flow Management – allows users to record, view, categorize, update, and monitor income and expense transactions.
   6. Recurring Expense Manager – allows users to manage scheduled income such as salaries and allowances, scheduled expenses such as subscriptions and bills, savings contributions, and debt repayments.
   7. Billers and Remittances – allows users to create, update, and delete current bills, essential expenses, payment schedules, and upcoming financial commitments.
   8. Income Sources Manager – allows users to manage salaries, allowances, side income, and other sources of earnings, while organizing associated cash, bank accounts, and e-wallets based on recorded transactions and balances, without direct bank or e-wallet API integration.
   9. Savings Goal Management – allows users to define targets such as emergency funds, tuition, rent, medical expenses, or planned purchases; record contributions; monitor cumulative progress; and project goal completion.
   10. Budget Management – allows users to create and monitor spending plans, prioritize essential expenses, and reduce the risk of underfunding necessities.
   11. Debt Management – allows users to record debts, track balances and payments, compare repayment strategies such as the snowball or avalanche methods to project payoff timelines, and identify potential debt risks caused by insufficient budgets or known upcoming expenses.
   12. User Settings – allows users to manage their profile, preferences, notifications, security, and application configurations.
   13. Financial Reports – allows users to view summaries and reports of income, expenses, savings, and debt for specified periods and categories, including personalized spending forecasts and anomaly alerts for unusual expenses or spending patterns that differ from their normal spending pattern.
6. Test the functionality, performance efficiency, usability, reliability, security, and maintainability of the system.
7. Evaluate the system using the System Usability Scale (SUS) and metrics based on the ISO/IEC 25010 software quality model. The evaluation will cover:
   1. System Usability Scale (SUS)
   2. ISO/IEC 25010:
      1. Functional Suitability: functional completeness, functional correctness, and functional appropriateness
      2. Performance Efficiency: response time, latency, and throughput
      3. Reliability: faultlessness, availability, fault tolerance, and recoverability
      4. Security: confidentiality, integrity, non-repudiation, accountability, authenticity, and resistance
      5. Maintainability: co-existence, modifiability, and testability
8. Deploy the intelligent personal financial management application to the Android platform and document its result.

## IV. Scope and Limitations

### Scope

The primary focus of this study is the development of BUDI, an intelligent personal financial management application for Filipinos aged 18 to 59 who live or work in the National Capital Region (NCR), Philippines, which serves as the geographical research locale. The locale and target users are relevant because they reflect the income patterns, cost of living, digital habits, and financial practices that the application is designed to support, as captured in the BSP consumer surveys and the study's PUEPS instrument (Bangko Sentral ng Pilipinas, 2026; PUEPS, 2026). Because the NCR covers a large and heterogeneous population, the survey component uses purposive sampling; PUEPS respondents were drawn primarily from Taguig, Pasay, Manila, and Makati. The study and its system development activities are conducted during the 2026–2027 academic year.

The functional scope of BUDI covers the user-facing features of the Android mobile application: user authentication and account management, user profiling, onboarding and financial profile assessment, cash flow management, recurring expense management, billers and remittances, income source management, savings goal management, budget management, debt management, expense forecasting, anomaly alerts, and financial reports, together with privacy-related functions such as consent management, data export, and account deletion. This list corresponds exactly to the features enumerated in Specific Objective 5. The application is single-user: it does not include admin, system-admin, or web-management roles. BUDI will support offline transaction entry through local storage and synchronize changes when connectivity becomes available.

The technical scope of the study covers the four intelligent modules and the data used to develop them. The modules will employ the following selected algorithms: Support Vector Machine (SVM) for personal financial profile classification, Seasonal Autoregressive Integrated Moving Average (SARIMA) for expense forecasting, Linear Programming (LP) for budget optimization, and Interquartile Range (IQR) for anomalous expense detection. Training and evaluation data will be drawn from publicly available Philippine sources — including the PSA Family Income and Expenditure Survey, PSA household financial characteristics data, and the BSP consumer finance and consumer expectations surveys, including microdata accessed through the PSA Data Archive (PSADA) <!-- VERIFY: confirm exact dataset names, years, versions, and access date --> — and from synthetically generated Filipino financial personas, together with the study's own PUEPS responses collected under informed consent. Forecasting will be limited to periods and categories where sufficient historical observations are available; anomaly alerts will be based on the user's recorded financial baseline; and all model outputs will be presented as decision-support information subject to user approval. Separately, the application will be developed with the Expo and React Native toolchain for the Android platform, an Express.js and Node.js backend, and Supabase/PostgreSQL with local SQLite for offline synchronization; these are the software tools of the development platform and are distinct from the models and data described above.

### Limitations

The study is limited in several respects, and each limitation is acknowledged against the corresponding objective, project context, or purpose.

The PUEPS pre-survey is based on purposive sampling of 47 respondents in the National Capital Region, drawn primarily from Taguig, Pasay, Manila, and Makati; findings may not fully represent Filipino individuals outside the region, users outside the 18–59 age range, or users with substantially different financial conditions.

The public Philippine datasets used are primarily household-level or aggregate data without complete individual transaction histories, so synthetic personas and transactions will be generated for model training and evaluation; model performance on synthetic data may differ from real-world performance, and synthetic-to-real generalization is currently in progress.

Because the application relies on manual financial data entry, it does not include bank or e-wallet API integration, automatic transaction importing, receipt scanning, or credit-score monitoring; recorded balances are monitored through user-entered transactions, and the quality of model outputs depends on the completeness and accuracy of user-entered records.

Forecasts are limited to periods and categories with sufficient historical data, and anomaly alerts reflect the user's recorded baseline rather than external behavior; the models may not fully anticipate sudden changes in income or spending, and models that learn from continually changing financial behavior must remain reliable as user circumstances evolve (Abdullahi et al., 2025) <!-- VERIFY: applicability of the concept-drift findings to personal-finance classification -->. Until sufficient transaction history accrues, new users have no forecast or anomaly-detection baseline; forecasting and anomaly alert features surface as pending rather than active during this cold-start period.

The application is developed primarily for the Android platform and is a single-user application; development and distribution on other platforms such as iOS, and any multi-user or administrative functionality, are outside the scope of this study.

BUDI is intended to provide financial decision support and not licensed financial, investment, tax, or legal advice; savings and debt features remain subject to further validation from the PUEPS findings and subject matter expert consultation.

## V. Operational Definition of Terms

The following terms are defined operationally, based on how they are identified, processed, measured, and utilized within BUDI.

**Ambag.** An informal shared contribution arrangement in the Philippines, included as an expense category in BUDI to reflect localized financial practices.

**Anomaly Alert.** A notification presented to the user when one or more transactions are flagged by the anomaly detection module as deviating from the user's normal spending patterns.

**Anomalous Expense Detection.** The BUDI module that uses the Interquartile Range (IQR) method to identify transactions that deviate significantly from the user's established spending baseline.

**Budget Optimization.** The BUDI module that uses Linear Programming (LP) to generate budget allocations that respect the user's obligations, constraints, and preferences.

**BUDI (Bawas Utang, Dagdag Ipon).** An intelligent personal financial management application developed to improve savings and debt management among Filipinos aged 18 to 59 in the National Capital Region.

**Cold Start.** The period when a new BUDI user has insufficient transaction history for expense forecasting or anomaly detection, during which these features surface as pending.

**Decision Support.** Model outputs that inform user decisions without replacing them, accompanied by explanations and applied only with user approval.

**Descriptive-Developmental.** The research design used in this study, which focuses on describing and developing a system without hypothesis testing.

**Expense Forecasting.** The BUDI module that uses the Seasonal Autoregressive Integrated Moving Average (SARIMA) model to predict future total and category-level expenses based on the user's historical transaction data.

**Financial Baseline.** A rolling statistical reference computed from the user's recent, category-level recorded transactions (for example, the median, mean, or interquartile range of category spending over a defined lookback window), which serves as the reference for anomaly detection, forecasting, and budget guidance <!-- VERIFY: the exact baseline construction rule, including statistic and lookback window, is finalized in the ML modeling phase -->.

**HFCI (Household Financial Characteristics and Income).** The PSA dataset used in this study for household financial characteristics <!-- VERIFY: confirm the exact dataset name (HFCI or HFCE), year, and version to be cited -->.

**IQR (Interquartile Range).** The statistical method used by the Anomalous Expense Detection module to identify transactions that fall outside the user's normal spending patterns.

**LP (Linear Programming).** The optimization technique used by the Budget Optimization module to generate budget allocations.

**Paluwagan.** An informal group savings arrangement common in the Philippines, included as an expense category in BUDI to reflect localized financial practices.

**Personal Financial Profile (PFP) Classification.** The BUDI module that uses the Support Vector Machine (SVM) to categorize users according to their financial characteristics.

**PUEPS.** The pre-survey used as preliminary investigation for this study, involving 47 respondents in the National Capital Region.

**Purposive Sampling.** A non-probability sampling technique in which respondents are selected based on specific criteria relevant to the research objectives; in this study, it was used to select Filipinos aged 18 to 59 in the National Capital Region who are relevant to the personal savings and debt context of the study.

**SARIMA (Seasonal Autoregressive Integrated Moving Average).** The time-series forecasting model used by the Expense Forecasting module to predict future expenses.

**Savings.** The portion of recorded income not used for expenses during a specified period, determined by comparing the user's recorded income with recorded expenses and savings transactions; debt principal repayments and transfers between the user's own accounts are treated as allocations, not expenses.

**Savings-Debt-First PFM.** A PFM approach that prioritizes improving savings and debt outcomes over generic expense tracking.

**Spending Pattern.** The observable trends and regularities in a user's recorded transactions, including recurring expenses, category distributions, and timing of expenditures, which provide the basis for classification, forecasting, optimization, anomaly detection, and budget guidance.

**SVM (Support Vector Machine).** The machine learning algorithm used by the Personal Financial Profile Classification module to categorize users.

**Synthetic Filipino Financial Personas.** Artificially generated user profiles and transaction data used for model training, validation, and testing in the absence of granular behavioral transaction data from public Philippine datasets.

---

## References

Abdullahi, M., Alhussian, H., Aziz, N., Abdulkadir, S. J., Baashar, Y., Alashhab, A. A., & Afrin, A. (2025). A systematic literature review of concept drift mitigation in time-series applications. *IEEE Access*. https://doi.org/10.1109/ACCESS.2025.3587231

Abila, J. P., & Ulibas, R. (2026). Analyzing the financial management practices and resilience of online freelancers in Laguna amid digital platform taxation. *International Journal of Multidisciplinary Educational Research and Innovation, 4*(2), Article 9.

Bangko Sentral ng Pilipinas. (2026). *Consumer expectations survey report: 2nd quarter 2026*. Monetary and Economics Sector, Department of Economic Statistics.

Chen, J., Chen, T., Wang, Y., & Wang, L. (2024). A survey of time series data forecasting methods based on deep learning. *Journal of Basic and Applied Research International, 30*(6), 140–157.

Chen, S., & Tan, W. (2025). LSTM-based consumer behavior prediction model research. In *Proceedings of the 2025 2nd International Conference on Digital Economy and Computer Science (DECS 2025)*.

D'Souza, M., Bhegade, P., Bhalekar, P., & Bhavsar, Y. (2026). A comprehensive review of machine learning techniques for intelligent personal finance management systems [Manuscript]. P.E.S. Modern College of Engineering, Pune.

Danahy, R., Lillard, D., Loibl, C., & Montalto, C. P. (2024). Financial stress among college students: New data about student loan debt, lack of emergency savings, social and personal resources. *Journal of Consumer Affairs*. https://doi.org/10.1111/joca.12581

El Hajj, M., & Hammoud, J. (2023). Unveiling the influence of artificial intelligence and machine learning on financial markets: A comprehensive analysis of AI applications in trading, risk management, and financial operations. *Journal of Risk and Financial Management, 16*(10), Article 434. https://doi.org/10.3390/jrfm16100434

Ganong, P., Noel, P. J., Patterson, C., Vavra, J. S., & Weinberg, A. (2025). *Earnings instability* (Working Paper No. 34227). National Bureau of Economic Research.

Hu, X., Lee, J. C. H., & Lee, J. H. M. (2023). Two-stage predict+optimize for mixed integer linear programs with unknown parameters in constraints. In *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*.

Huang, A., Zhang, X., Wang, Y., Tsai, S., Zhou, P., & Chen, L. (2025). Dynamic calibration of decision thresholds for financial anomaly detection: Verification with payment platform information and data. *Journal of Global Information Management, 33*(1).

Huang, R., Zhao, Z., Chen, S., Wu, X., & Zhao, J. L. (2025). Wealth-Voyager: Navigating intelligent wealth management with a multi-agent framework. In *Proceedings of the 2025 International Conference on Generative Artificial Intelligence for Business (GAIB 2025)*.

Laspiñas, E. L., & Murcia, J. V. B. (2024). Machine learning approaches in classifying income levels. *TWIST, 19*(2), 92–97. https://doi.org/10.5281/zenodo.10049652

Lu, Y., Zhou, H., & Zhang, Y. (2025). A constrained, data-driven budgeting framework integrating macro demand forecasting and marketing response modeling. *Journal of Technology Informatics and Engineering, 4*(3), 493–520. https://doi.org/10.51903/jtie.v4i3.466

Pratama, S. F., & Putri, N. A. (2024). User profiling based on financial transaction patterns: A clustering approach for user segmentation. *International Journal for Applied Information Management, 4*(4), 217–228.

PUEPS. (2026). *ODIN public user expectations and perception survey (Responses)* [Data set]. Research Group 4, College of Computing and Information Sciences, University of Makati.

Reyes, J. M., Santos, L. P., & Perez, A. (2024). A comparative analysis of machine learning models for predictive analytics in finance. *International Journal of Applied Mathematics and Computing, 1*(1), 14–20. https://doi.org/10.62951/ijamc.v1i1.3

Salvador, E. L. V. (2024). Use of boosting algorithms in household-level poverty measurement: A machine learning approach to predict and classify household wealth quintiles in the Philippines [Manuscript].

Sonkavde, G., Dharrao, D. S., Bhat, S. K., Doreswamy, D., Bongale, A. M., & Deokate, S. T. (2023). Forecasting stock market prices using machine learning and deep learning models: A systematic review, performance analysis and discussion of implications. *International Journal of Financial Studies, 11*(3), Article 94. https://doi.org/10.3390/ijfs11030094

Wang-Ly, N., & Newell, B. R. (2023). *How income volatility influences saving decisions: Evidence from the lab* (SSRN Working Paper No. 4509925). https://ssrn.com/abstract=4509925

Yadav, S., Kumar, V., & Maurya, A. (2026). Intelligent personal finance management system for smart budgeting and real-time expense tracking: Design and development. *International Scientific Journal of Engineering and Management, 5*(4). https://doi.org/10.55041/ISJEM06330

Yeo, K. H. K., Lim, W. M., & Yii, K.-J. (2023). Financial planning behaviour: A systematic literature review and new theory development. *Journal of Financial Services Marketing, 29*, 979–1001. https://doi.org/10.1057/s41264-023-00249-1

Yoganandham, G. (2025). Mastering economic and financial sources with reference to budgeting, savings, early investing, debt management and the power of financial planning – A comprehensive analysis. *Degres Journal*.

Zhang, A., Deng, S., Cui, D., Yuan, Y., & Wang, G. (2023). An experimental evaluation of anomaly detection in time series. *Proceedings of the VLDB Endowment, 16*(11), 3165–3178. https://doi.org/10.14778/3611540.3611555

Zhong, M. (2025). *Adaptive anomaly detection threshold for financial data quality monitoring based on time series features* [Master's thesis, University of Chicago].