# Outline of Odin: A Personal Finance Management Application for Filipino Working Young Adults Using Random Forest, LSTM, and Isolation Forest Algorithms

## System

### Platform

- Mobile-first application
- Web-accessible application

### Target Users

- Filipino working young adults
    - Age range: 20–40
    - Geographic scope: Metro Manila

### Input

- Manual transaction entry (income, expense, recurring)
- Expense categorization: FIES‑grounded taxonomy
- User profile onboarding: income type (stable/variable) × obligation level (flexible/obligated)

### Architecture

- *To be described: overall system architecture*

### Module Design

- User profile design
- Expense categorization scheme
- Transaction input design
- Budget recommendation design
- Forecasting model design
- Anomaly detection design
- Savings management design
- Debt management design

### Components

> Insert components, like the profiles, expense categories, transactions (income, expense, transfer), flows (income, expense, goals)

### Modules (functional descriptions)

#### Financial Behavioral Profile Classification

- Initial classification on onboarding (user‑selectable or questionnaire)
- Reclassification: triggered by behavioral change detection; system suggests profile update with user confirmation
- Classification algorithm: Random Forest
- Features for classification: *To be determined from BSP, PSA, and pre‑survey results*
- Thresholds for reclassification (e.g., % change in income volatility, obligation ratio): **To be determined**
- Explainability: Required – method to be added

#### Budget Recommendation

- Basis: Current balance + predicted income for selected time horizon
- Time horizons: *To be determined from RRL*
- Budgeting strategies: Deconstructed into configurable templates (e.g., 50/30/20, zero‑based, pay‑yourself‑first) *should benchmark from RRL and existing PFM apps*
- Surplus handling: *To be determined from RRL*
- Recommendation algorithm: Linear programming (LP)
- Explainability: Required – method to be added

#### Expense Forecasting
- Per‑category forecasting (daily, weekly, monthly)
- Cold‑start fallback: uses BSP and FIES data until sufficient user history
- Forecast view: total or per‑category (user‑selectable)
- Explainability: Required – method to be added

#### Anomaly Detection
- Primary method: Isolation Forest (detects outliers, including non‑threshold deviations e.g., spending 90% of budget in first week)
- Rule‑based budget overage detection (supplementary)
> NOTE: Anomaly detection module can detect anomalies that don't necessarily exceed thresholds
- Culturally expected spikes (fiestas, holidays, etc.): **excluded** from anomaly detection
- User whitelist for intentional outliers
- Alert fatigue handling: *To be designed* (e.g., grouping, acknowledgment)
- Explainability: Required – method to be added

#### Savings Goal Tracking
- Goal creation and targeting
- Progress monitoring

#### Debt Management
- Avalanche method
- Snowball method

### Evaluation (system-level)

#### ISO/IEC 25010:2023
- Quality characteristics to be evaluated: *To be determined from RRL* 

#### System Usability Scale (SUS)
- Target score: *To be determined from RRL benchmarks*
- Sample size: *To be determined* (minimum recommendation: ?)
- Respondent profile: Filipino working young adults, Metro Manila, mix of stable/variable and flexible/obligated

#### Algorithmic Module Evaluation (separate from ISO/SUS)
- Forecasting: MAE, RMSE, sMAPE – *acceptable thresholds TBD in experimental phase*
- Anomaly detection: Precision, Recall, F1 – *targets TBD*
- Profile classification: Accuracy, Precision, Recall, F1 – *targets TBD*
- Validation method: Walk‑forward validation, synthetic data (generated from BSP/PSA/survey)

## Paper

### Introduction

#### Background

- Domain context
- Problem space

#### Problem

- General problem
- Specific problems

#### Objectives

- General objective
- Specific objectives

#### Significance

- Primary beneficiaries
- Secondary beneficiaries

#### Scope and Delimitations

##### Inclusions

- Manual transaction entry, recurring transactions
- FIES‑based categories
- Four behavioral profiles
- Budget recommendation
- Expense forecasting (should income and goal forecasting be included? primarily for the purposes of influencing the budget recommendation module effectively)
- Anomaly detection
- Savings/debt tracking

##### Exclusions

- No bank or e‑wallet API integration (due to registration fees)
- No OCR
- No investment tracking
- No multi‑currency
- Non‑Filipino users outside scope
- Metro Manila only

#### Definition of Terms

### Review of Related Literature

#### Pillars

##### 1. Filipino Working Young Adults and the Financial Problem

- Filipino working young adults
    - Demographic profile
    - Income structure typology
    - Financial literacy levels and the gap between knowledge and behavior
    - Prevalence and severity of personal financial management problems
- Financial structure
    - Income patterns
    - Expense patterns
    - Financial goals
    - Debt structure and debt management behavior
- Financial behavior
    - Budgeting practice
    - Financial behavior differences across income stability types
    - Budget failure points
    Evidence that intelligent adaptive tools outperform financial literacy-only interventions

##### 2. Filipino Cultural Context in Personal Finance

- Culturally Specific Financial Practices
    - Informal financial mechanisms
    - Family financial obligations
    - Community and religious financial contributions
    - Government-mandated financial obligations
- Seasonal and Cyclical Spending Patterns
    - Calendar-driven spending spikes and suppression cycles
    - Implications of cyclical patterns for forecasting, anomaly detection, and budget recommendation
- User-Declared Financial Preferences
    - Protected expense categories
    - Category and goal prioritization as user-configurable inputs to recommendation logic

##### 3. Expense Categorization in Personal Finance Systems

- Expense Categorization Frameworks
    - Approaches to expense categorization
    - PSA FIES and BSP CFS expenditure categories as the authoritative local standard
    - Limitations of Western category schemas for Filipino spending contexts
- Expense Category Design Considerations
    - Discretionary, essential, obligatory, and financial expense groupings
    - Category ambiguity as a driver of user abandonment
    - Culturally specific categories warranting dedicated treatment

##### 4. Existing Personal Finance and Budget Management Systems

- Landscape of Existing Systems
    - Classification and typology of PFMS and PBMS in the literature
    - Feature sets of existing systems and evidence of their effectiveness
    - Intelligent and adaptive features
- Limitations and Gaps in Existing Systems
    - Documented general limitations
    - Absence of locally grounded systems for Filipino users
    - Design and architecture patterns transferable to Odin from existing systems

##### 5. Financial Behavioral Profiling

- Financial Behavioral Profiles in Personal Finance
    - Role of behavioral profiling in personalizing budget recommendation, forecasting, and anomaly detection
    - Inadequacy of Western behavioral taxonomies for Filipino financial user contexts
    - Behavioral dimensions as meaningful profile differentiators
    - Constructing locally grounded financial profiles from Philippine institutional and behavioral data
- Profile Dynamics and the Cold-Start Problem
    - Concept drift as the framework for progressive profile updates over time
    - Behavioral signals that should trigger profile reassessment
    - Cold-start problem
- Financial Behavioral Profile Classification Algorithm
    - Supervised classification versus clustering for predefined profile categories
    - Candidate classification algorithms for behavioral and financial user profiling
    - Feature selection
    - Cold-start classification
    - Progressive reclassification
    - Tradeoffs across candidate classifiers
    - Evaluation metrics for profile classification

##### 6. Spending Forecasting

- Predictive Modeling in Personal Finance Systems
    - Survey of forecasting methods applied to personal or household spending data
    - Temporal dependency in spending data: prior periods as predictors of subsequent periods
    - Per-category forecasting
    - Cold-start fallback strategies for forecasting with insufficient transaction history
    - Mobile deployment constraints and their effect on forecasting algorithm selection
- Spending Forecasting Algorithm
    - Candidate forecasting algorithms for sequential personal spending data
    - Comparative performance of candidate algorithms on time-series forecasting tasks
    - Algorithm behavior under data sparsity and the cold-start condition
    - Tradeoffs across candidate algorithms
    - Evaluation metrics for spending forecasting

##### 7. Budget Recommendation

- Budgeting Strategies as Domain Knowledge
    - Core mechanics of documented budgeting strategies
    - Comparative strengths and weaknesses across income stability types
    - Behavioral evidence that structured budgeting improves financial outcomes
- Budget Recommendation in Personal Finance Systems
    - Approaches to budget recommendation in existing systems
    - Constraint-based allocation
    - Behavioral evidence for the effectiveness of automated budget recommendations
    - Budget period surplus handling: reset versus carryforward logic
- Budget Recommendation Algorithm
    - Problem formulation
    - Candidate algorithms for budget distribution and financial resource allocation
    - Tradeoffs across candidate algorithms
    - Evaluation metrics for budget recommendation

##### 8. Anomalous Spending Detection

- Anomaly Detection in Personal Finance Systems
    - Definition and taxonomy of financial anomalies in personal spending data
    - Threshold-based overage alerting versus behavioral baseline deviation detection
    - Behavioral evidence for the impact of anomaly and overspending alerts on user financial behavior
    - Alert design: frequency, framing, and format to minimize fatigue while ensuring action
    - Culturally expected high-value spending events and their treatment in anomaly detection
- Anomaly Detection Algorithm
    - Anomaly detection as an ML problem: unsupervised, semi-supervised, and supervised families
    - Candidate anomaly detection algorithms for personal spending data
    - Per-user baseline learning without labeled training data
    - Tradeoffs across candidate algorithms: false positive control, explainability, and mobile feasibility
    - Evaluation metrics for anomaly detection

##### 9. Mobile-First Design

- Mobile-First Design Principles and Rationale
    - Definition and distinction: mobile-first versus desktop-first design in PFMS
    - Mobile penetration and financial exclusion as the empirical basis for mobile-first deployment
    - Technical constraints: compute, connectivity, screen size, and battery life
- Mobile UX Design for Personal Finance
    - UX patterns that minimize manual transaction entry burden
    - Glanceable visualizations and dashboard design for financial data on small screens
    - Offline resilience and data synchronization in mobile financial applications

##### 10. Data Privacy, Security, and User Trust

- Data Privacy and Security in Personal Finance Systems
    - Sensitivity classification of personal financial data and associated privacy risks
    - Technical security standards for mobile financial application data handling
    - Philippine regulatory framework: RA 10173 and NPC issuances applicable to a PFMS
    - Privacy-by-design principles applied in financial system research
- User Trust in Personal Finance Systems
    - User trust in personal finance applications and its effect on data-sharing and logging behavior
    - Explainability of algorithmic outputs as a trust-building mechanism
    - Privacy concern as a driver of inconsistent or withheld transaction logging

##### 11. User Retention and Engagement

- Engagement Dynamics in Personal Finance Applications
    - Relationship between transaction data completeness and downstream ML model performance
    - Drop-off patterns in personal finance apps: when users stop logging and why
    - Manual data entry as the primary engagement friction point in PFMS
- Retention Mechanisms and Engagement Design
    - Non-gamification retention mechanisms: smart notifications, frictionless input, and value feedback loops
    - Demonstrated system value as an intrinsic retention driver
    - Goal-setting features and progress visualization as engagement mechanisms

##### 12. System Evaluation

- Evaluation Frameworks for Personal Finance Systems
    - Evaluation frameworks, metrics, and methodologies documented for PFMS
    - ISO/IEC 25010:2023 quality characteristics and their application to a PFMS
    - System Usability Scale: instrument design, scoring, administration, and benchmarks
    - Combining ISO 25010 and SUS as a joint evaluation framework
    - ISO 25010 and SUS applied in PFMS or comparable financial application evaluations
- Evaluation of Algorithmic Modules
    - Evaluation design for ML modules in intelligent PFMS: walk-forward validation and out-of-sample testing
    - Acknowledged limitations of ISO 25010 and SUS for evaluating intelligent system components
    - Sample size and respondent profile guidelines for SUS-based evaluations

##### Clarifications (apporve/reject these, then remove after)

- **Pillar 5 (Financial Behavioral Profiling)** – Will address: cold‑start classification (onboarding questionnaire), reclassification thresholds as open research question, feature selection from BSP/PSA, evaluation metrics.
- **Pillar 6 (Spending Forecasting)** – Will address: cold‑start fallback using BSP/FIES data, mobile deployment constraints.
- **Pillar 7 (Budget Recommendation)** – Will address: LP as candidate algorithm, explainability gap, surplus handling benchmarks from RRL, time horizon benchmarks from RRL.
- **Pillar 8 (Anomalous Spending Detection)** – Will address: Isolation Forest, exclusion of culturally expected spikes, whitelisting for user‑acknowledged outliers.
- **Pillar 10 (Data Privacy, Security, User Trust)** – Will address: RA 10173 compliance, data anonymization, server-side ML processing, user consent and info sections in app.
- **Pillar 12 (System Evaluation)** – Will address: combining ISO 25010 and SUS; evaluation of ML modules (walk‑forward, synthetic data); sample size guidelines from literature.

### Research Methodology

#### Research Design

- Research paradigm: *To be specified* (e.g., pragmatism)
- Descriptive methodology: *To be specified*
- Experimental methodology: *To be specified*
- Developmental methodology: agile development methodology

#### Evaluation Design (detailed from above)

- ISO 25010 operationalization
- SUS instrument, administration, target score, sample size
- ML module evaluation: metrics, validation method, synthetic data generation
- Evaluation procedure (phases: offline ML testing → qualitative pilot → SUS with 30 users after 14 days)

#### Ethical Considerations

- Informed consent for financial data collection
- Compliance with RA 10173 (Data Privacy Act)
- Data anonymization before server transmission
- User rights: data access, correction, deletion
- App disclaimers: all intelligent features are informational; user retains final financial decisions
- Institutional ethics clearance: *To be confirmed*

#### Data Collection for ML Training

- Synthetic data generated from BSP, PSA, and pre‑survey results
- No real user data used for training without consent
- Pilot user data (with consent) may supplement synthetic data