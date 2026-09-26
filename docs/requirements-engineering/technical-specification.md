# **🛠️ Project**

# **PROJECT SPECIFICATION**

---

# **1\. PROJECT PURPOSE AND SCOPE**

This document defines the project identity, target users, scope, delimitations, limitations, assumptions, glossary, and the TBD Register for the study. It serves as the canonical reference for all project-level decisions.

---

# **2\. PROJECT IDENTITY**

## **2.1 TITLE**

The project title is **"Development of TAYA: A Personal Financial Management App Using SARIMA-Based Seasonal Expense Forecasting for Budget, Savings, and Debt Planning"**.

## **2.2 ACRONYM**

The project acronym is TBD. The current draft lists the letters T, A, Y, A without providing the words they represent.

## **2.3 DESCRIPTION**

**TAYA** is a personal financial management application for Filipinos aged 18 to 59 in the National Capital Region. It uses seasonal expense forecasting to generate personalized budgets, savings contribution plans, and debt repayment plans under financial constraints.

The system temporally disaggregates **2023 Family Income and Expenditure Survey microdata** using **2022 (Quarter 1\) to 2026 (Quarter 2\) Household Final Consumption Expenditure data** to produce seasonally adjusted monthly expense estimates. It performs saver and borrower classification, forecasts per-category expense differences and composition with SARIMA, optimizes personalized budgets and per-goal and per-debt schedules with linear programming under financial constraints, detects unusual expenses with IQR, and composes an actionable financial plan for user approval.

---

# **3\. PROJECT USERS**

## **3.1 CRITERIA**

The target users meet the following criteria.

* **Age**. Users are aged 18 to 59\.  
* **Location**. Users reside in the National Capital Region.  
* **Employment Status**. Users may have any employment status.  
* **Income Level**. Users may have any income level.  
* **Device**. Users use an Android device.  
* **Interest**. Users are interested in or looking to improve their savings and debt planning and management.

## **3.2 USER MODEL**

The application is a **single-user** application. There are no admin, system-admin, or web-management roles. There is no multi-user, household, or workspace architecture.

---

# **4\. SCOPE, DELIMITATIONS, LIMITATIONS, AND ASSUMPTIONS**

## **4.1 SCOPE**

The system provides **offline capability** in core features. The modules with models or algorithms are server-side.

## **4.2 DELIMITATIONS**

The following features are out of scope for this project.

* Bank or e-wallet integration is not included.  
* Automatic transaction import is not included.  
* OCR or receipt scanning is not included.  
* Credit score monitoring is not included.  
* Automated bill payment is not included.  
* Multi-currency support is not included.

The following deployment targets are out of scope.

* iOS development is not included.  
* Public marketplace deployment is not included.

## **4.3 LIMITATIONS**

* The Public User Expectations and Perceptions Survey used purposive sampling of 47 respondents in the National Capital Region, primarily from Taguig, Pasay, Manila, and Makati.  
* Data entry is manual only. There is no bank or e-wallet API integration.  
* HFCE seasonality is quarterly. Monthly seasonality is imputed via disaggregation and is not directly observed.  
* The population series covers 2022 Q1 to 2026 Q2, which is 18 quarters or four and a half years. This is borderline for SARIMA with a seasonal period of 12, which is a known constraint. The 2026 HFCE data is partial and covers only Q1 and Q2.  
* Forecasts are limited to periods and categories with sufficient historical data.  
* Anomaly alerts reflect the user's recorded baseline and not external behavior.  
* New users have no personal forecast or unusual spending alerts baseline until sufficient history accrues. Population-level seasonality partially mitigates this cold-start condition.  
* Population-level seasonality partially mitigates cold-start for expense forecasting only. For unusual expense detection, alerts are disabled until the personal baseline threshold N\_min is met. No population-based anomaly fallback is used.  
* The application is Android-only. iOS and multi-user or admin functionality are out of scope.  
* TAYA provides decision support and not licensed financial, investment, tax, or legal advice.  
* Savings and debt features remain subject to further validation from PUEPS findings and subject matter expert consultation.

## **4.4 ASSUMPTIONS**

* Business data flows remain offline-capable for core features.  
* Modules with models or algorithms are server-side.  
* Philippine seasonal consumption patterns at the population level are informative for individual users.  
* Outputs are decision-support information.  
* Outputs are accompanied by explanations using large language models.  
* Outputs are applied only with user approval.  
* Model outputs must not replace user decisions.  
* Cold-start behavior assumes that population seasonality provides a partial baseline and that personalization improves as history accrues.  
* The final model selection rule is that title algorithms are the named algorithms for this study.  
* The Financial Plan is the central artifact of the system. Every module either enriches it, constrains it, or monitors it.  
* Temporal disaggregation uses FIES-anchored, HFCE-calibrated proportional benchmarking / equiproportional disaggregation with reconciliation. Chow-Lin, Denton, and Litterman are not used.  
* Authentication is online-only. Governance controls such as ownership, consent, and privacy are enforced locally and re-validated at sync.

---

# **5\. PROJECT GLOSSARY**

The following terms are used throughout the specification documents.

* **Bangko Sentral ng Pilipinas (BSP)**. The central bank of the Philippines, responsible for monetary policy, financial supervision, and payment systems.  
* **Borrower**. A user who has outstanding debt obligations and is working to manage or repay them.  
* **Budget**. A plan for allocating income across expense categories, savings goals, and debt repayments within a specified period.  
* **Cold-Start**. The condition of a new user who has insufficient transaction history for personalized model training.  
* **Debt**. Money owed by a user to a creditor, typically with defined repayment terms.  
* **Debt Plan**. A structured schedule for repaying debts over time, including payment amounts and timelines.  
* **Decision-Support**. A system function that provides information and recommendations to assist user decision-making without replacing user judgment.  
* **Descriptive-Developmental**. A research design that describes existing conditions and develops a system or intervention based on those findings.  
* **Family Income and Expenditure Survey (FIES)**. A PSA survey that collects annual data on family income, expenses, and related socioeconomic characteristics.  
* **Financial Plan**. The central output artifact of the system, combining budget allocations, savings schedules, debt schedules, and explanations.  
* **Household Final Consumption Expenditure (HFCE)**. A PSA dataset that measures quarterly household consumption spending by category.  
* **Personal Financial Management (PFM)**. The practice of managing personal income, expenses, savings, and debt to achieve financial goals.  
* **Philippine Statistics Authority (PSA)**. The Philippine government agency responsible for national statistics, including FIES and HFCE data.  
* **Public User Expectations and Perception Survey (PUEPS)**. A survey instrument used in this study to gather user expectations and perceptions.  
* **Saver**. A user who prioritizes setting aside funds for future goals.  
* **Savings**. Funds set aside from current income for future use or goals.  
* **Savings Plan**. A structured schedule for contributing to savings goals over time.  
* **Seasonal Auto-Regressive Integrated Moving Average (SARIMA)**. A statistical forecasting model that captures seasonal patterns in time series data.  
* **Subject Matter Expert**. An individual with specialized knowledge in a relevant domain who provides validation or guidance.

---

# **7\. PROJECT TBD REGISTER**

The following items remain unresolved and require decisions before implementation and final documentation can proceed. Each item is listed with its owner tab and current status.

- [x] ~~Temporal disaggregation method. The method may be Chow-Lin, Denton, Litterman, or another approach. The owner tab is Models. The status is TBD.~~  
- [ ] Savings and debt categories and primary sources. These categories and their sources are needed for model input and evaluation. The owner tab is Models. The status is TBD.  
- [ ] SME validation of thresholds. Subject matter expert validation has not yet been performed. The owner tab is Models. The status is TBD.  
- [ ] Rule-Based Classifier formulas and dimensions. These require definition. The owner tab is Models. The status is TBD.  
- [ ] Rule-Based Classifier label availability. The availability of labeled data for evaluation remains undetermined. The owner tab is Models. The status is TBD.  
- [ ] SARIMA blending mechanism and cold-start threshold. The exact blending mechanism and the history threshold for personalization remain undefined. The owner tab is Models. The status is TBD.  
- [ ] Category alignment between FIES and HFCE. This alignment is required before disaggregation and forecasting. The owner tab is Models. The status is TBD.  
- [ ] IQR detector threshold calibration. The thresholds for unusual expense detection remain undefined. The owner tab is Models. The status is TBD.  
- [x] ~~Cold-start anomaly behavior. The behavior of the IQR detector for new users remains undefined. The owner tab is Models. The status is TBD.~~  
- [x] ~~Financial Planning placement in architecture. The Financial Planning module may be hosted in the api-gateway or deployed as a separate container. The owner tab is System. The status is TBD.~~  
- [ ] Event bus selection. The event bus may be Kafka or RabbitMQ. The owner tab is System. The status is TBD.  
- [ ] Cloud provider selection. The cloud provider for deployment remains TBD. The owner tab is System. The status is TBD.  
- [ ] Orchestration and infrastructure details. The orchestration platform and infrastructure details remain TBD. The owner tab is System. The status is TBD.  
- [ ] NFR numeric targets. Numeric targets for non-functional requirements remain TBD. The owner tab is System. The status is TBD.  
- [ ] API contracts, schemas, and data dictionary. These artifacts remain TBD. The owner tab is System. The status is TBD.  
- [ ] Deployment and DevOps specifics. The deployment and DevOps procedures remain TBD. The owner tab is System. The status is TBD.  
- [ ] Auth and governance online and offline assignment. The assignment of authentication and governance responsibilities between online and offline modes remains TBD. The owner tab is System. The status is TBD.  
- [ ] Data foundation container. Whether the data foundation is deployed as a service or batch job remains TBD. The owner tab is System. The status is TBD.  
- [x] ~~Financial Planning container. Whether the Financial Planning module is deployed as a separate container remains TBD. The owner tab is System. The status is TBD.~~  
- [ ] LLM explanation service placement. The architectural home for LLM-based Financial Plan explanation generation (in-container within api-gateway, a separate microservice, or an external hosted LLM API call) remains undefined, along with its NFR implications against the p95 ≤ 2,000 ms ML-route target and its offline-capability handling. The owner tab is System. The status is TBD.  
- [ ] Feedback loop mechanism. The specific mechanism for the feedback loop remains TBD. The owner tab is System. The status is TBD.  
- [ ] KPIs for savings and debt improvement. These KPIs are needed for evaluation alignment. The owner tab is Paper. The status is TBD.  
- [ ] Portability testing details. Portability is included in the ISO/IEC 25010 evaluation. The specific testing approach remains TBD. The owner tab is Paper. The status is TBD.  
- [ ] Final research gap definition. The proposed gap statement requires validation through a broader literature review. The owner tab is Paper. The status is pending.  
- [ ] Final research problem wording. The research problem statement is drafted but not yet approved. The owner tab is Paper. The status is TBD.  
- [ ] Main research question final wording. The main research question is proposed and pending approval. The owner tab is Paper. The status is TBD.  
- [ ] Novelty claim. The novelty claim depends on a thorough literature review not yet shown. The owner tab is Paper. The status is pending.  
- [ ] Theoretical and conceptual framework. The theoretical and conceptual framework remains TBD. The owner tab is Paper. The status is TBD.

# **📑 Paper**

# **PAPER SPECIFICATION**

---

# **1\. PAPER PURPOSE AND SCOPE**

This document defines the research framing, research problem, research questions, evaluation methodology, and references for the study. It serves as the canonical reference for all paper-level decisions.

---

# **2\. PAPER RESEARCH FRAMING**

## **2.1 PAPER PROBLEM**

Filipinos aged 18 to 59 in the National Capital Region continue to face persistent challenges in improving their savings and managing debt (Bangko Sentral ng Pilipinas, 2023; Bulan & Nemino, 2025; Cruz et al., 2026; Esperanza et al., 2025; Francisco et al., 2026). While personal financial management applications exist, many prioritize generic expense tracking and budgeting rather than savings-and-debt outcomes (Alenazi & Sas, 2023). Few are localized to Filipino financial realities or account for Philippine seasonal consumption patterns. There is limited localized, evidence-based research on personal financial management systems that integrate profile classification, seasonality-aware expense forecasting, budget creation, and unusual expense detection specifically to improve savings and debt. This study develops and evaluates **TAYA** as a closed-loop, seasonality-aware savings-debt plan pipeline that addresses these gaps.

## **2.2. PAPER ANCHORS**

The study focuses on savings and debt management rather than general money management (Cumaio et al., 2026; Yoganandham, 2025). It compares against personal financial management applications that specifically aim to improve savings and debt, not generic personal financial management applications. The **Financial Plan** is the primary artifact. The study is descriptive-developmental and does not test hypotheses. Seasonality is a defining feature of the system.

## **2.3 PAPER GAP**

The following gap statement is proposed and validated against the curated RRL corpus (BUDI-Literature).

Existing studies have investigated household budgeting and financial optimization primarily using income, expense requirements, savings objectives, and predefined allocation rules (Gulbakyt et al., 2025; Lu et al., 2025). **De Zarzà et al. (2024)** developed mathematical optimization models for individual and household financial planning, while **Dey and Arefin (2025)** proposed a rule-based system for household budget generation. However, neither study explicitly incorporated Philippine seasonal consumption patterns into expense forecasting and personalized financial planning.

In the Philippine context, **Dasmariñas et al. (2024)** investigated forecasting national household consumption using SARIMA and historical quarterly HFCE data. However, their research focused on aggregate household consumption rather than applying Philippine seasonal consumption patterns to personalized financial planning.

The identified research gap is the lack of an integrated personal financial management system that incorporates Philippine seasonal consumption patterns, derived from HFCE data, into personalized expense forecasting, and applies these forecasts to generate personalized budgets, savings contribution schedules, and debt repayment plans under financial constraints (D'Souza et al., 2026; Yadav et al., 2026).

## **2.4 PAPER DESIGN**

The research design is descriptive-developmental. The study does not test hypotheses.

## **2.5 PAPER LOCALE**

The research locale is the National Capital Region (NCR), Philippines.

## **2.6 PAPER PERIOD**

The research period is the University of Makati (UMak) Academic Year 2026-2027.

---

# **3\. PAPER RESEARCH QUESTIONS**

## **3.1 PAPER QUESTION**

The main research question is: How is TAYA developed and evaluated as a seasonality-aware, closed-loop savings-debt plan pipeline for Filipinos aged 18 to 59 in the National Capital Region?

## **3.2 PAPER SUB-QUESTIONS**

The following sub-questions guide the study.

* What financial management behaviors, challenges, and needs do Filipino users in the National Capital Region have regarding savings and debt (Bulan & Nemino, 2025; Claro & Noval, 2025; Cruz et al., 2026; Esperanza et al., 2025; Francisco et al., 2026; Yeo et al., 2023)?  
* What gaps exist in existing personal financial management applications and algorithms for savings and debt improvement, particularly regarding Philippine seasonality (Alenazi & Sas, 2023; D'Souza et al., 2026; Yadav et al., 2026)?  
* How can PSA FIES 2023, PSA HFCE 2022 Q1 to 2026 Q2, and PUEPS data be prepared and temporally disaggregated for model training, validation, and testing (Dasmariñas et al., 2024)?  
* How is the seasonality-aware savings-debt plan pipeline designed, and how do its stages interact (D'Souza et al., 2026; Yadav et al., 2026)?  
* How accurately does the temporal disaggregation method reproduce seasonal consumption patterns?  
* How do the modules with models or algorithms perform in terms of their respective evaluation metrics? These modules are Saver and Borrower Classification, Expense Forecasting, Budget Creation, and Unusual Expense Detection (Gulbakyt et al., 2025; A. Huang et al., 2025; Kara & Şengüler, 2025; Laspiñas & Murcia, 2024; Lu et al., 2025; Zhong, 2025).  
* How does TAYA perform in terms of functionality, performance efficiency, usability, reliability, security, and portability (Santiago et al., 2025)?  
* How do users perceive TAYA's effect on their savings and debt management (Bulan & Nemino, 2025; Yeo et al., 2023)?

---

# **4\. PAPER EVALUATION**

## **4.1 COVERAGE**

The evaluation covers **functionality**, **performance efficiency**, **usability**, **reliability**, **security**, and **portability**.

## **4.2 INSTRUMENTS**

The evaluation uses the System Usability Scale (SUS) and the ISO/IEC 25010 quality model.

## **4.3 ISO/IEC 25010 CHARACTERISTICS**

The evaluation addresses the following ISO/IEC 25010 characteristics.

* **Functional Suitability**. This covers functional completeness, correctness, and appropriateness.  
* **Performance Efficiency**. This covers time behavior and capacity.  
* **Reliability**. This covers availability, fault tolerance, recoverability, and data integrity.  
* **Security**. This covers confidentiality, integrity, and authenticity.  
* **Portability**. This covers adaptability and installability.  
* **Usability**. This covers appropriateness recognizability, learnability, user error protection, user interface aesthetics, and accessibility.

## **4.4 KEY PERFORMANCE INDICATORS**

The following KPI table is adopted for evaluation alignment with the **Models Specification**.

KPI	Definition	Source

1. Savings rate	Monthly savings contributions / monthly income	Savings module \+ budget solver  
2. Savings goal progress	Funded weeks/months vs plan for each goal	Savings schedule, LP output  
3. Anomaly alert frequency	Unusual-expense alerts per month	IQR detector  
4. Debt repayment progress	Principal paid vs plan per debt	Debt schedule, LP output  
5. Plan adherence	Actual allocation vs recommended allocation	Financial Plan diff

These KPIs align with the main research question’s savings-debt indicators and should be matched to Models-tab metrics: MAE, SMAPE, MDA, RMSE, constraint satisfaction rate, budget utilization rate, and Precision/Recall/F1.

---

# **5\. PAPER REFERENCES**

Alenazi, M., & Sas, C. (2023). Evaluating budgeting apps: Limited support for budgeting compared to tracking. *Proceedings of the BCS HCI 2023 Conference (Electronic Workshops in Computing)*. [https://doi.org/10.14236/ewic/BCSHCI2023.1](https://doi.org/10.14236/ewic/BCSHCI2023.1)

Bangko Sentral ng Pilipinas. (2023). *Financial inclusion in the Philippines dashboard: As of fourth quarter 2023*. Bangko Sentral ng Pilipinas.

Bulan, P. J., & Nemino, M. R. (2025). The interplay of behavioral intention on the relationship between self-control and saving behavior among MSME business owners. *International Journal of Management Studies and Social Science Research, 7*(2), 139–150. [https://doi.org/10.56293/IJMSSSR.2025.5518](https://doi.org/10.56293/IJMSSSR.2025.5518)

Claro, D. M. L., & Noval, J. E. G. (2025). The regressors of financial well-being among LGU employees in Davao del Norte. *ISRG Journal of Economics & Business Management, 3*(6), 171–187. [https://doi.org/10.5281/zenodo.17775590](https://doi.org/10.5281/zenodo.17775590)

Cruz, M. A. T. D., Jurada, P. H. G., Recreo, C. R., Mandigma, M. B. S., & Magbata, E. V. S. (2026). Dependence of Filipino young professionals' well-being on their investing years and income in the National Capital Region. *Review of Integrative Business and Economics Research, 15*(2), 902–919.

Cumaio, S., Serrasqueiro, Z., & Madaleno, M. (2026). Linking financial literacy and behavioural finance to saving and debt behaviours: A literature review of global and developing economy contexts. *Journal of Risk and Financial Management, 19*(6), Article 425. [https://doi.org/10.3390/jrfm19060425](https://doi.org/10.3390/jrfm19060425)

Dasmariñas, A. P., De Castro, G. H., Lazona, B. J. M., & Usona, L. P. (2024). Forecasting the impact of COVID-19 on the household final consumption expenditure (HFCE) in the Philippines. *PUP Journal of Science & Technology, 14*(1), 70–90. [https://doi.org/10.70922/ctzevg57](https://doi.org/10.70922/ctzevg57)

D'Souza, M., Bhegade, P., Bhalekar, P., & Bhavsar, Y. (2026). A comprehensive review of machine learning techniques for intelligent personal finance management systems [Manuscript]. P.E.S. Modern College of Engineering, Pune.

de Zarzà, I., de Curtò, J., Roig, G., & Calafate, C. T. (2024). Optimized financial planning: Integrating individual and cooperative budgeting models with LLM recommendations. *AI, 5*(1), 91–114. [https://doi.org/10.3390/ai5010006](https://doi.org/10.3390/ai5010006)

Dey, S., & Arefin, M. S. (2025). Developing a rule-based system to recommend household budget. *Journal of Information Systems Engineering and Management, 10*(47s), 148–182. [https://doi.org/10.52783/jisem.v10i47s.9230](https://doi.org/10.52783/jisem.v10i47s.9230)

Esperanza, D. N., Bithay, L. L., Jesus, J. B., Ople-Alviola, C., Sumilhig, J. M., & Basilisco, G. L. (2025). Digital lending efficacy on debt management of wage earners. *ASEAN Journal of Management & Innovation, 12*(2), 111–127.

Francisco, A., Legal, G., & Legal, F. (2026). Causes of salary loan dependency: Basis for strengthening financial literacy program. *International Journal of Multidisciplinary Educational Research and Innovation, 4*(1), 705–728.

Gulbakyt, S., Almaz, A., Saule, S., & Suhrab, Y. (2025). Dynamic model for budget allocation via multi-criteria optimization. *Journal of Applied Data Sciences, 6*(4), 3075–3088. <!-- VERIFY: no DOI printed; confirm volume/issue before Google Docs use -->

Huang, A., Zhang, X., Wang, Y., Tsai, S., Zhou, P., & Chen, L. (2025). Dynamic calibration of decision thresholds for financial anomaly detection: Verification with payment platform information and data. *Journal of Global Information Management, 33*(1). [https://doi.org/10.4018/JGIM.395852](https://doi.org/10.4018/JGIM.395852)

Kara, B., & Şengüler, H. (2025). A comparative analysis of budget forecasting methods: A systematic literature review covering the 1983–2024 period. *Public Budgeting & Finance*. [https://doi.org/10.1111/pbaf.70008](https://doi.org/10.1111/pbaf.70008)

Laspiñas, E. L., & Murcia, J. V. B. (2024). Machine learning approaches in classifying income levels. *TWIST, 19*(2), 92–97. [https://doi.org/10.5281/zenodo.10049652](https://doi.org/10.5281/zenodo.10049652)

Lu, Y., Zhou, H., & Zhang, Y. (2025). A constrained, data-driven budgeting framework integrating macro demand forecasting and marketing response modeling. *Journal of Technology Informatics and Engineering, 4*(3), 493–520. [https://doi.org/10.51903/jtie.v4i3.466](https://doi.org/10.51903/jtie.v4i3.466)

Santiago, R. L. T., Villarica, M. V., & Bernardino, M. P. (2025). Budget and financial management information system for public elementary schools: Analytics and predictive insights for MOOE allocation using linear regression. *International Journal of Advanced Research in Computer Science, 16*(3), 128–150.

Yadav, S., Kumar, V., & Maurya, A. (2026). Intelligent personal finance management system for smart budgeting and real-time expense tracking: Design and development. *International Scientific Journal of Engineering and Management, 5*(4). [https://doi.org/10.55041/ISJEM06330](https://doi.org/10.55041/ISJEM06330)

Yeo, K. H. K., Lim, W. M., & Yii, K.-J. (2023). Financial planning behaviour: A systematic literature review and new theory development. *Journal of Financial Services Marketing, 29*, 979–1001. [https://doi.org/10.1057/s41264-023-00249-1](https://doi.org/10.1057/s41264-023-00249-1)

Yoganandham, G. (2025). Mastering economic and financial sources with reference to budgeting, savings, early investing, debt management and the power of financial planning — A comprehensive analysis. *Degres Journal, 10*(1), 25–40.

Zhong, M. (2025). Adaptive anomaly detection threshold for financial data quality monitoring based on time series features. In *Proceedings of the International Conference on Advanced and Intelligent Computing Systems (AICSS 2025)*. ACM. [https://doi.org/10.1145/3776759.3776850](https://doi.org/10.1145/3776759.3776850)

# **⚙️ System**

# **SYSTEM SPECIFICATION**

---

# **1\. SYSTEM PURPOSE AND SCOPE**

This document defines the system architecture, deployment model, application modules, external interfaces, and pipeline orchestration for the system. It serves as the canonical reference for all system-level decisions.

---

# **2\. SYSTEM ARCHITECTURE**

## **2.1 SYSTEM HIGH-LEVEL ARCHITECTURE**

The system is composed of the following subsystems.

### **2.1.1. MOBILE CLIENT**

The mobile client is Android-first and stores data locally.

### **2.1.2. BACKEND SERVICES**

The backend services provide authentication, synchronization, and online-only operations.

### **2.1.3. MODEL AND ALGORITHM MICROSERVICE**

The model and algorithm microservice consists of FastAPI microservices that serve the Rule-Based Classifier, the SARIMA Forecaster, the Linear Programming Solver, and the IQR Detector.

## **2.2 SYSTEM SYNCHRONIZATION**

Core features are offline-capable. Modules with models or algorithms are server-side with local caching. A sync queue stores domain operations. Conflict resolution follows a delete-wins rule, then per-field last-write-wins. Idempotency is achieved through operation IDs and applied-operation tracking. Tombstones are used for deletes. Ownership validation is performed both locally and remotely.

## **2.3 SYSTEM DEPLOYMENT**

The deployment architecture consists of the following containers and ports.

* **api-gateway** runs on port 8000 and routes and aggregates ML requests. It also hosts the Financial Planning module.  
* **classifier** runs on port 8001 and performs saver and borrower classification using rule-based logic.  
* **forecaster** runs on port 8002 and performs expense forecasting using SARIMA.  
* **detector** runs on port 8003 and performs unusual expense detection using IQR.  
* **transaction-service** runs on port 8004 and handles transaction ingestion and event publishing.  
* **solver** runs on port 8005 and performs budget creation using linear programming.

## **2.4 SYSTEM INTEGRATION**

The integration architecture is loose coupling, event-driven, fail-safe, and composable. Module failures degrade gracefully. The event bus is TBD and may be Kafka or RabbitMQ. The cloud provider is TBD. The orchestration platform is TBD.

## **2.5 SYSTEM TECHNOLOGY STACK**

The mobile frontend uses:

* Expo SDK 55  
* React Native 0.83  
* React Native Web 0.21  
* React Native Paper  
* NativeWind and Tailwind CSS 4  
* @expo/vector-icons.

The main backend uses:

* Node.js 24 LTS  
* Express 5.1  
* Supabase

Local storage uses:

* SQLite

The model and algorithm microservice uses:

* Python 3.14  
* FastAPI  
* PyTorch  
* scikit-learn  
* statsmodels for SARIMA

Package and tooling use:

* pnpm  
* Python virtual environment

Deployment uses:

* Docker containers

Cloud provider remains TBD.

## **2.6 SYSTEM INTERFACES AND ENDPOINTS**

The sync API exposes two endpoints.

* The first is POST /taya/api/sync/push.  
* The second is POST /taya/api/sync/pull.

The Model and Algorithm Microservice API is accessed via the gateway and exposes the following endpoints: **\[TBD: validate listed endpoints\]**

* For the Rule-Based Classifier, the endpoints are:  
  * POST /api/v1/profile/classify  
  * POST /api/v1/profile/batch  
  * GET /api/v1/profile/user/{id}/history  
  * GET /api/v1/profile/user/{id}/latest  
* For the SARIMA Forecaster, the endpoints are:  
  * POST /api/v1/forecast/predict  
  * POST /api/v1/forecast/batch  
  * GET /api/v1/forecast/user/{id}/history.  
* For the IQR Detector, the endpoints are:  
  * POST /api/v1/anomaly/detect  
  * POST /api/v1/anomaly/batch  
  * GET /api/v1/anomaly/user/{id}/alerts  
  * GET /api/v1/anomaly/user/{id}/baseline.  
* For the Linear Programming Solver, the endpoints are:  
  * POST /api/v1/budget/optimize  
  * GET /api/v1/budget/user/{id}/schedules.  
* The gateway also provides convenience endpoints:  
  * GET /api/v1/user/{id}.

Each service exposes /health, /ready, and /metrics. Authentication uses Google OAuth and email/password with email verification. Data formats are JSON. Model artifacts use .joblib, .pkl, and .pth extensions. Data export is provided as a downloadable file.

---

# **3\. SYSTEM MODULES**

The system provides the following modules.

## **3.1. DASHBOARD MODULE**

The Dashboard provides an overview of the user's financial status.

## **3.2. USER AUTHENTICATION MODULE**

User Authentication manages login and registration.

## **3.3. SAVER AND BORROWER CLASSIFICATION MODULE**

Saver and Borrower Classification collects and stores user characteristics and produces a profile indicating saver, borrower, both, or neither, along with associated dimensions.

## **3.4. USER ONBOARDING MODULE**

User Onboarding guides new users through initial setup.

## **3.5. CASH FLOW MANAGEMENT MODULE**

Cash Flow Management tracks income and expenses.

## **3.6. RECURRING EXPENSE MANAGEMENT MODULE**

The Recurring Expense Management handles repeating expenses.

## **3.7. BILLERS AND REMITTANCES MODULE**

Billers and Remittances manage bill payments and remittances.

## **3.8. INCOME SOURCE MANAGEMENT MODULE**

The Income Sources Management tracks multiple income streams.

## **3.9. SAVINGS GOAL MANAGEMENT MODULE**

Savings Goal Management allows users to set and track savings goals.

## **3.10. BUDGET MANAGEMENT MODULE**

Budget Management provides budget creation and monitoring.

## **3.11. DEBT MANAGEMENT MODULE**

Debt Management tracks debts and repayment progress.

## **3.12. USER SETTINGS MODULE**

User Settings allows configuration of preferences.

## **3.13. FINANCIAL REPORTS MODULE**

Financial Reports generates summaries and reports.

## **3.14. FINANCIAL PLANNING MODULE**

Financial Planning combines all module outputs into the central artifact, which is the Financial Plan. This module has no associated model or algorithm. It is hosted in the **api-gateway** container and is not deployed as a separate container.

---

# **4\. ADDITIONAL SYSTEM FEATURES**

Additional confirmed features include privacy controls, consent management, data export, account deletion, offline transaction entry, and synchronization when connectivity is available.

* Privacy controls and consent management belong to User Settings.  
* Data export and account deletion belong to User Settings.  
* Offline transaction entry belongs to Cash Flow Management.  
* Synchronization when connectivity is available belongs to backend services.  
* Authentication is online-only.  
* Governance controls are enforced locally on the device and re-validated remotely at next sync.  
* Data export and account deletion are initiated online and queued if offline.

Expense categories reflect Filipino financial realities. These categories include family support, government contributions, paluwagan, and ambag.

---

# **5\. SYSTEM NON-FUNCTIONAL REQUIREMENTS**

NFR	Proposed target  
Availability	≥ 99.5% for services; 100% for core offline features  
API latency	p95 ≤ 500 ms; ML routes forecast/alert/budget solve ≤ 2,000 ms  
LP solve time	≤ 1,000 ms per budget period using HiGHS  
App cold start	≤ 3 s on a mid-range Android device  
Sync queue	≤ 50 MB retained; push/pull latency p95 ≤ 5 s on 4G  
Data export	≤ 60 s for a single-user dataset  
Usability (SUS)	≥ 68 acceptable  
Security	No plaintext secrets; OWASP Top 10 reviewed; RA 10173-aligned export/consent

---

# **6\. SYSTEM PIPELINE**

## **6.1 SYSTEM PIPELINE DESCRIPTION**

The primary feature of the system is an explainable, seasonality-aware savings-debt plan pipeline. It turns population seasonal consumption patterns and a user's transaction history into an optimized financial plan, monitors deviations, and adjusts recommendations with user approval. The **Financial Plan** is the central artifact. Every module either enriches it, constrains it, monitors it, or composes it.

## **6.2 SYSTEM PIPELINE FLOW**

The pipeline depends on the output of the model training step. Temporal Disaggregation produces seasonally adjusted monthly expense estimates that anchor the **Expense Forecasting** module (see "Temporal Disaggregation" at Models). These estimates are consumed by the Expense Forecasting module at Stage 1\.

## **6.3 SYSTEM PIPELINE STAGES**

The pipeline consists of six stages, numbered zero through five. Detailed algorithms and metrics for each module are specified in the **Models Specification** (see "Model and Algorithm Details" at Models).

### **6.3.1 STAGE 0: SAVER AND BORROWER CLASSIFICATION**

This stage establishes the user's financial profile using questionnaire answers and cash flow transaction history. The process is rule-based. The output is a profile indicating saver, borrower, both, or neither, along with associated dimensions. The profile is consumed by the **Budget Creation** module and the **Financial Planning** module.

### **6.3.2 STAGE 1: EXPENSE FORECASTING**

This stage predicts future expense difference and composition using SARIMA. The inputs are the seasonally adjusted monthly estimates from the model training step and the user's transaction history. The output is the per-category period-over-period expense difference and the forecasted expense composition. This output is consumed by the **Budget Creation** module and the **Financial Planning** module.

### **6.3.3 STAGE 2: BUDGET CREATION**

This stage converts the forecast and profile into a feasible allocation that maximizes savings and debt progress under financial constraints. The process is hierarchical linear programming using the HiGHS solver. The output is a budget allocation, per-goal savings contribution schedules, per-debt repayment schedules, feasibility status, and an explanation. This output is consumed by the **Financial Planning** module.

### **6.3.4 STAGE 3: UNUSUAL EXPENSE DETECTION**

This stage monitors deviations from the user's recorded baseline. The process is inter-quartile range detection. The output is an unusual expense alert. This output is consumed by the **Financial Planning** module and the user.

### **6.3.5 STAGE 4: FINANCIAL PLANNING**

This stage combines all module outputs into the central artifact, which is the **Financial Plan**. The inputs are the profile, forecast, budget, schedules, alerts, and goals. The process uses rule-based conflict resolution to combine outputs, drafted as follows and pending team and advisor confirmation:

* **R1 — Feasibility Gate.** If the Linear Programming Solver returns an infeasible feasibility status, the Financial Plan composes in advisory mode: no final schedule numbers are presented, and the explanation names the violated constraint and surfaces relaxation options. Finalization is blocked until the user acts.  
* **R2 — Alert Override.** If an unacknowledged IQR alert is active at composition time, the Financial Plan still composes but is marked pending review; the alert is surfaced first in the Financial Plan, and the affected schedule is flagged provisional pending user acknowledgment.  
* **R3 — Alert Escalation.** If alert severity crosses a threshold (calibration TBD, see IQR Detector threshold calibration), Stage 4 pauses any automatic Stage 2 re-solve until the user reviews the anomaly.  
* **R4 — Profile Confidence Flag.** If the profile is Neither/holding, or the user is below the SARIMA cold-start threshold N\_min, the Financial Plan composes using the population-level forecast but is annotated with a low-confidence notice.  
* **R5 — Explanation Composition.** Per-module explanation strings (profile explanation, LP explanation) are concatenated into one composed narrative field. The LLM explanation layer (architectural placement TBD, see Project TBD Register) performs stylistic synthesis only and does not introduce new financial content.

The output is the **Financial Plan**, which includes the budget, savings schedules, debt schedules, and explanations. This output is consumed by the user.

### **6.3.6 STAGE 6: FEEDBACK LOOP**

Updates the plan based on user feedback and new data. Mechanism:

* Collect user plan approvals/rejections, new transactions, and alert acknowledgements.  
* When personal history ≥ N\_min, trigger refresh of the personal SARIMA forecast and re-run budget optimization.  
* Below threshold, refresh the scaled population-baseline forecast.  
* Cadence: weekly scheduled refresh plus on-demand refresh on significant data change.  
* Updated plan is re-fed into Stage 1 and presented for approval.

# **🤖 Models**

# **MODEL AND ALGORITHM SPECIFICATION**

---

## **1\. MODEL AND ALGORITHM PURPOSE AND SCOPE**

This document defines the data foundation, models, algorithms, evaluation metrics, and model-specific limitations for the system. It serves as the canonical reference for all model-related decisions.

---

# **2\. MODEL TRAINING**

## **2.1 MODEL TRAINING DATA**

The system draws on the following data sources for training.

### **2.1.1 PSA 2023 FIES (Vols. 1 to 2\)**

The source link is [Household-based Surveys](https://psada.psa.gov.ph/catalog/Household-based_Surveys/about). This source provides annual income totals, annual expense totals, family size, per-capita income, and decile ranking. It is the source for temporal disaggregation.

### **2.1.2 PSA 2022-2026 HFCE (2022 Q1 to 2026 Q2)**

The source link is [Household Final Consumption Expenditure by Purpose](https://openstat.psa.gov.ph/PXWeb/pxweb/en/DB/DB__2B__NA__QT__2HFCE/?tablelist=true). This source provides quarterly household consumption. It is the source for seasonal patterns in disaggregation.

### **2.1.3 PUEPS**

The year and version are TBD. The source link is TBD. This source provides user expectations and preliminary investigation data.

## **2.2 MODEL DATA NOTES**

The FIES 2023 dataset and the HFCE 2022 Q1 to 2026 Q2 dataset are locked. The 2026 HFCE data is partial and covers only Q1 and Q2. The FIES 2023 dataset is accessed through the PSA Data Archive. The savings and debt categories and their primary sources remain TBD. The validation of thresholds by subject matter experts has not yet been performed and remains TBD. The temporal disaggregation method remains TBD.

## **2.3 MODEL DATA LIMITATIONS**

The FIES public use files are anonymized in accordance with RA 10173 and the PSA disclosure policy. The dataset represents the general NCR population, and age and employment linkage is absent. HFCE data is quarterly, and monthly seasonality is imputed. The population series length is 18 quarters, which is borderline for SARIMA with a seasonal period of 12\. The KPIs for savings and debt improvement remain TBD.

## **2.4. MODEL DATA DISAGGREGATION**

Temporal Disaggregation is a model training step that produces the seasonally adjusted monthly expense estimates used by the Expense Forecasting module.

* Inputs: PSA FIES 2023 Volumes 1 and 2, annual data per category; PSA HFCE 2022 Q1 to 2026 Q2, quarterly data per category.  
* Process: Temporal disaggregation.  
* Adopted method: FIES-anchored, HFCE-calibrated temporal disaggregation with proportional benchmarking / equiproportional disaggregation with reconciliation.  
* Output: Seasonally adjusted monthly expense estimates per category.  
* Evaluation criteria: Disaggregation accuracy against held-out quarters, seasonal pattern plausibility, and SME review.

---

# **3\. MODEL AND ALGORITHM DETAILS**

This section provides detailed specifications for each model.

## **3.1 RULE-BASED CLASSIFIER**

The purpose of the Rule-Based Classifier is to establish the user’s financial profile so that the **Linear Programming Solver** and **Financial Planning** module can weigh goals and constraints appropriately.

* The inputs are:  
  * Questionnaire answers  
  * Cash flow transaction history.  
* The process is:  
  * Rule-based mathematical rules and statistics using financial\_rules\_v1.  
  * The four financial-condition dimensions are:  
    * EFC: liquid savings / average monthly essential expenses.  
    * DSTI: 100 × required debt payments / monthly disposable income.  
    * FM: disposable income − debt payments − basic living costs.  
    * CC: revolving-months count in a 12-month window.  
  * The saver/borrower/both/neither profile is composed as follows, subject to confirmation against primary sources:  
    * Borrower	DSTI \> 40% or FM \< 0  
    * Saver	EFC ≥ 3 months or CC transactor  
    * Both	Both borrower and saver conditions hold  
    * Neither / holding	Neither condition holds  
* The outputs are:  
  * Profile indicating saver, borrower, both, or neither.  
  * Associated profile dimensions.  
  * Profile explanation.  
* The evaluation criteria are:  
  * Accuracy, precision, recall, and F1-score if labeled data is available.  
  * No human-labeled ground-truth corpus exists.  
  * Use rule-derived reference labels for self-consistency.  
  * Use a hand-built boundary-case test set: exact-at-40% DSTI, EFC at 3.0, and 12-month credit-card window edges.  
  * Use SME spot checks.

## **3.2 SARIMA FORECASTER**

The purpose of the SARIMA Forecaster is to predict future expense difference and composition while accounting for Philippine seasonality, so that the Linear Programming Solver can allocate realistically and the Financial Planning module can explain expected changes.

* The inputs are the seasonally adjusted monthly estimates from Temporal Disaggregation and the user's transaction history.  
* The process uses Seasonal Auto-Regressive Integrated Moving Average.  
  * Implementation note: The served forecaster is a pooled SARIMA on a user-normalized monthly series with (1,1,0)(1,0,0,12) and a 24-month seasonal-identification floor. The per-user population↔personal blend is the selected V1.1 design and is pending offline experiment. The v3 RF research pipeline is not served.  
  * Fit SARIMA per category on the seasonally adjusted monthly series from Temporal Disaggregation. This produces:  
    * Monthly multipliers per category.  
    * Population-level baseline forecast.  
    * Seasonal specification using P, D, Q, and seasonal period 12\.  
  * Fit SARIMA on the user’s monthly series per category with seasonal orders fixed from the population specification. This applies when the user has sufficient history.  
    * Cold-start threshold: N\_min \= 24 months.  
    * Blend rule: Above threshold, weight the personal forecast linearly from 0→1 as user history goes N\_min→2×N\_min, clamping to the population monthly multipliers. Below threshold, use the scaled population baseline forecast.  
  * Use the population baseline forecast scaled to the user’s income or recent expense level when the user is below the history threshold. Include a disclosure that personalization improves over time.  
* The outputs are the per-category period-over-period expense difference and the forecasted expense composition. For each category, the difference is forecasted amount minus current period amount, or minus the same period last year deseasonalized, expressed in pesos. Composition is forecasted category amount divided by total forecasted expenses, expressed as a percentage.  
* The evaluation criteria are MAE, SMAPE, MDA, RMSE, a comparison against a seasonal naive baseline, and the contribution of disaggregation accuracy.  
* The known limitations are:  
  * HFCE data is quarterly and monthly seasonality is imputed.  
  * Population series is 18 quarters, which is short for SARIMA with seasonal period 12\.  
  * FIES↔HFCE category alignment must be verified and published.

## **3.3 LINEAR PROGRAMMING SOLVER**

The purpose of the Linear Programming Solver is to convert the forecast and profile into a feasible allocation that maximizes savings and debt progress under financial constraints.

* The inputs are the expense forecast, the user's saver and borrower profile, the user's savings goals, the user's debts, the user's income, and the user's fixed expenses. Whether to include the user's budget constraints as a separate input remains TBD.  
* The process is hierarchical linear programming using the HiGHS solver.  
* The outputs are a budget allocation, per-goal savings contribution schedules, per-debt repayment schedules, feasibility status, and an explanation. The generation rules for per-goal and per-debt schedules remain TBD. The feasibility actions remain TBD.  
* The evaluation criteria are constraint satisfaction rate, budget utilization rate, and deviation from user preferences.

## **3.4 INTER-QUARTILE RANGE DETECTOR**

The purpose of the IQR Detector is to monitor deviations from the user's recorded baseline and surface alerts that may require plan adjustment.

* The inputs are new transactions and a seasonally aware baseline. Cold-start unusual expense detection remains TBD.  
* The process is inter-quartile range detection. Threshold calibration remains TBD.  
* The output is an unusual expense alert.  
* The evaluation criteria are accuracy, precision, recall, and F1-score.

The limitations are that the seasonal baseline is quarterly only, and alerts reflect the user's recorded baseline rather than external behavior.

## **3.5 FINANCIAL PLANNING**

Financial Planning is a module that combines all module outputs into the central artifact, which is the **Financial Plan**. This module has no associated model or algorithm; it uses drafted rule-based conflict resolution logic (see "Stage 4: Financial Planning" at System). Evaluation metrics for this module remain TBD, though the Paper Specification's Plan Adherence KPI (actual allocation vs. recommended allocation, sourced from the Financial Plan diff) is a candidate.

# **💉 Inject Updates Here**
