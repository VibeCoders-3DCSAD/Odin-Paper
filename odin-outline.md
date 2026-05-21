# Outline of Odin: A Personal Finance Management Application for Filipino Working Young Adults Using Random Forest, LSTM, and Isolation Forest Algorithms

---

## System

### Platform

- Mobile-first application
- Web-accessible application

### Target Users

- Filipino working young adults
    - Age range: 20–40
    - Geographic scope: Metro Manila

### Input

- Manual transaction entry
    - Income transactions
    - Expense transactions
    - Transfer transactions
- Recurring transactions
    - Income transactions
    - Expense transactions
- Expense categorization: FIES- and research-grounded taxonomy
- User profile onboarding: income type (stable/variable) × obligation level (flexible/obligated)

### Architecture

- *To be described: overall system architecture*

### Components

#### User Profiles

- Stable-Flexible
- Stable-Obligated
- Variable-Flexible
- Variable-Obligated

##### User Dimensions

- Income stability
    - Stable
    - Unstable/Variable
- Obligation Weight
    - Flexible/Unobligated
    - Obligated

> NOTE: Thresholds should be added here in the future.

#### Expense Categories (FIES-grounded) (preferably add RRL citations)

- Food and beverages
- Alcohol and tobacco
- Clothing and footwear
- Housing, water, electricity, gas, and other fuels
- Furnishings, household equipment, and routine maintenance
- Health
- Transport
- Communication
- Recreation and culture
- Education
- Restaurants and accommodation services
- Miscellaneous goods and services
- Financial obligations (debt payments, insurance premiums)
- Savings and investments

> NOTE: These subcategories should be aggregated into main categories. A loose non-restrictive example is an Essentials category containing food and beverages, housing, water, electricity, gas, and other fuels, health, financial obligations, etc.

#### Transaction Types

- Income (one-time, recurring)
- Expense (one-time, recurring)
- Transfer (between accounts)

#### Financial Flows

- Income flow: income → available balance
- Expense flow: available balance → expense category
- Savings flow: available balance → savings goal
- Debt flow: available balance → debt payment

#### Budget

- Total budget size
- Budget period (time horizon)
- Per-category allocation
- Surplus / deficit tracking

#### Savings Goals

- Goal name and target amount
- Target date
- Contribution amount and frequency
- Progress state (on-track / behind / achieved)

> See if there are savings contribution strategies, much like how there are debt repayment strategies.

#### Debt Accounts

- Debt name and total amount
- Interest rate
- Minimum payment
- Payoff strategy for multiple debts (Avalanche / Snowball)
- Remaining balance and projected payoff date

#### Alerts and Notifications

- Budget overspending alert
- Anomaly alert
- Savings goal milestone notification
- Forecast-based advisory notification

### Modules

#### Financial Behavioral Profile Classification

- Initial classification on onboarding (questionnaire-based)
- Reclassification: triggered by behavioral change detection; system suggests profile update with user confirmation
- Classification algorithm: Random Forest
- Features for classification: *To be determined from BSP, PSA, and pre-survey results*
- Reclassification thresholds (e.g., % change in income volatility, obligation ratio): open research question; to be grounded in RRL
- Explainability: Required — method to be determined from RRL

#### Budget Recommendation

- Basis: current balance + predicted income for selected time horizon
- Time horizons: *To be determined from RRL*
- Budgeting strategies: deconstructed into configurable templates (e.g., 50/30/20, zero-based, pay-yourself-first); benchmarked from RRL and existing PFM apps
- Surplus handling: *To be determined from RRL*
- Recommendation algorithm: Linear Programming (LP)
- Explainability: Required — method to be determined from RRL

#### Forecasting

- Targets
    - Expense forecasting: per-category (daily, weekly, monthly)
    - Income forecasting: income trend projection
    - Savings trajectory: projected savings balance over time
    - Debt payoff projection: projected remaining debt balance over time
- Forecast view: total or per-category (user-selectable)
- Cold-start fallback: uses BSP and FIES population-level data until sufficient user transaction history is accumulated
- Forecasting algorithm: LSTM
- Explainability: Required — method to be determined from RRL

#### Anomaly Detection

- Primary method: Isolation Forest
    - Detects behavioral outliers, including non-threshold deviations (e.g., spending 90% of budget in the first week of the period)
- Supplementary method: rule-based budget overspending detection
- Culturally expected spending spikes (fiestas, holidays, etc.): excluded from anomaly detection
- User whitelist: intentional outliers acknowledged by the user are suppressed from future alerts
- Alert fatigue handling: *To be designed* (e.g., grouping, acknowledgment, cooldown periods)
- Explainability: Required — method to be determined from RRL

#### Savings Goal Tracking

- Goal creation
    - User-defined goal name, target amount, and target date
    - Linked contribution schedule (manual or recurring)
- Progress monitoring
    - Visual progress indicator (amount saved vs. target)
    - On-track / behind / achieved status
    - Projected achievement date based on current contribution rate
- Multiple concurrent goals supported
- Goal prioritization: user-configurable

#### Debt Management

- Debt account creation
    - Debt name, total amount, interest rate, minimum payment
- Payoff strategy selection
    - Avalanche method: highest-interest-first
    - Snowball method: lowest-balance-first
- Payoff tracking
    - Remaining balance per account
    - Projected payoff date per account
    - Total interest projected under selected strategy
- Strategy switching: user may switch between Avalanche and Snowball at any time

### Evaluation (system-level)

#### ISO/IEC 25010:2023

- Quality characteristics to be evaluated: *To be determined from RRL*

#### System Usability Scale (SUS)

- Target score: *To be determined from RRL benchmarks*
- Sample size: *To be determined from RRL guidelines*
- Respondent profile: Filipino working young adults, Metro Manila, mix of stable/variable and flexible/obligated profiles

#### Algorithmic Module Evaluation

- Forecasting: MAE, RMSE, sMAPE — acceptable thresholds TBD in experimental phase
- Anomaly detection: Precision, Recall, F1 — targets TBD
- Profile classification: Accuracy, Precision, Recall, F1 — targets TBD
- Validation method: walk-forward validation; synthetic data generated from BSP, PSA, and pre-survey results

---

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
- FIES-based expense categories
- Four behavioral profiles
- Budget recommendation
- Forecasting (expense, income, savings trajectory, debt payoff projection)
- Anomaly detection
- Savings goal tracking
- Debt management

##### Exclusions

- No bank or e-wallet API integration (due to registration fees)
- No OCR
- No investment tracking
- No multi-currency
- Non-Filipino users outside scope
- Metro Manila only

#### Definition of Terms

- **Personal Finance Management System (PFMS):** A software system designed to help individuals track, plan, and manage personal income, expenses, savings, and debt.
- **Financial behavioral profile:** A classification of a user based on income stability and financial obligation level, used to personalize system recommendations.
> NOTE: See if we can find a more concise terminology for financial behavioral profiles
- **Income stability:** The degree to which a user's income is consistent and predictable across periods (stable vs. variable).
- **Obligation level:** The degree to which a user's expenses are fixed and unavoidable (obligated vs. flexible).
> NOTE: Those two should have defined thresholds.
- **Expense category:** A classification label assigned to a financial transaction, grounded in the PSA Family Income and Expenditure Survey (FIES) taxonomy.
> NOTE: Should be grounded not just in PSA FIES but also other sources, to strengthen rationale.
> NOTE: Categories and subcategories should be explicitly defined.
- **Budget recommendation:** An algorithmically generated allocation of available funds across expense categories for a defined time period.
- **Expense forecasting:** The use of historical transaction data to predict future spending amounts per category.
- **Anomaly detection:** The identification of spending patterns that deviate significantly from a user's established behavioral baseline.
- **Cold-start problem:** The condition in which a system has insufficient user-specific historical data to generate personalized predictions or recommendations.
- **Concept drift:** The phenomenon in which the statistical properties of user financial behavior shift over time, requiring model adaptation.
> NOTE: Maybe call it behavioral drift?
- **Random Forest:** An ensemble machine learning algorithm that constructs multiple decision trees and aggregates their outputs for classification or regression.
- **LSTM (Long Short-Term Memory):** A type of recurrent neural network architecture suited to learning from sequential time-series data.
- **Linear Programming (LP):** A mathematical optimization method used to allocate limited resources subject to defined constraints.
- **Isolation Forest:** An unsupervised anomaly detection algorithm that isolates anomalies by randomly partitioning feature space.
- **Walk-forward validation:** A time-series model evaluation method in which the model is trained on past data and tested on successive future periods, rolling forward incrementally.
- **ISO/IEC 25010:2023:** An international standard defining a quality model for software product evaluation.
- **System Usability Scale (SUS):** A ten-item Likert-scale instrument for measuring perceived system usability.
- **FIES:** Family Income and Expenditure Survey — a nationally representative household survey conducted by the Philippine Statistics Authority (PSA).
- **BSP CFS:** Bangko Sentral ng Pilipinas Consumer Finance Survey — a survey of Filipino household financial behavior and asset/liability structure.
- **Avalanche method:** A debt payoff strategy that prioritizes accounts with the highest interest rate first to minimize total interest paid.
- **Snowball method:** A debt payoff strategy that prioritizes accounts with the lowest outstanding balance first to build repayment momentum.
- **Paluwagan:** An informal rotating savings and credit association practiced in the Philippines.
- **Alert fatigue:** The desensitization of users to system alerts due to excessive frequency or low relevance, resulting in ignored notifications.

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
    - Evidence that intelligent adaptive tools outperform financial literacy-only interventions

##### 2. Filipino Cultural Context in Personal Finance

- Culturally Specific Financial Practices
    - Informal financial mechanisms (paluwagan, utang)
    - Family financial obligations
    - Community and religious financial contributions
    - Government-mandated financial obligations
- Seasonal and Cyclical Spending Patterns
    - Calendar-driven spending spikes and suppression cycles
    - Implications for forecasting, anomaly detection, and budget recommendation
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
    - Classification and typology of PFMS in the literature
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
    - Cold-start problem in profile classification
- Financial Behavioral Profile Classification Algorithm
    - Supervised classification versus clustering for predefined profile categories
    - Candidate classification algorithms for behavioral and financial user profiling
    - Feature selection from BSP, PSA, and pre-survey data
    - Cold-start classification via onboarding questionnaire
    - Progressive reclassification: thresholds as an open research question grounded in RRL
    - Tradeoffs across candidate classifiers
    - Evaluation metrics for profile classification

##### 6. Spending Forecasting

- Predictive Modeling in Personal Finance Systems
    - Survey of forecasting methods applied to personal or household spending data
    - Temporal dependency in spending data: prior periods as predictors of subsequent periods
    - Per-category forecasting
    - Cold-start fallback strategies using BSP and FIES population-level data
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
    - Budget period surplus handling: reset versus carryforward logic (benchmarked from RRL)
    - Time horizon selection: benchmarked from RRL
- Budget Recommendation Algorithm
    - Problem formulation
    - LP as the candidate algorithm: rationale and constraint structure
    - Explainability of LP outputs
    - Tradeoffs across candidate algorithms
    - Evaluation metrics for budget recommendation

##### 8. Anomalous Spending Detection

- Anomaly Detection in Personal Finance Systems
    - Definition and taxonomy of financial anomalies in personal spending data
    - Threshold-based overspending alerting versus behavioral baseline deviation detection
    - Behavioral evidence for the impact of anomaly and overspending alerts on user financial behavior
    - Alert design: frequency, framing, and format to minimize fatigue while ensuring action
    - Culturally expected high-value spending events (fiestas, holidays) and their exclusion from anomaly detection
    - User whitelisting for intentional outlier suppression
- Anomaly Detection Algorithm
    - Anomaly detection as an ML problem: unsupervised, semi-supervised, and supervised families
    - Isolation Forest as the primary candidate: rationale and mechanics
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
    - Philippine regulatory framework: RA 10173 (Data Privacy Act) and NPC issuances applicable to a PFMS
    - Privacy-by-design principles applied in financial system research
    - Data anonymization before server transmission
    - Server-side ML processing as a privacy-preserving architecture choice
- User Trust in Personal Finance Systems
    - User trust in personal finance applications and its effect on data-sharing and logging behavior
    - Explainability of algorithmic outputs as a trust-building mechanism
    - Privacy concern as a driver of inconsistent or withheld transaction logging
    - User consent mechanisms and in-app transparency features

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

### Research Methodology

#### Research Design

- Research paradigm: *To be specified*
- Descriptive methodology: *To be specified*
- Experimental methodology: *To be specified*
- Developmental methodology: Agile development methodology

#### Evaluation Design

- ISO 25010 operationalization: quality characteristics mapped to system features
- SUS instrument, administration, target score, sample size
- ML module evaluation: metrics per module, walk-forward validation, synthetic data generation from BSP/PSA/pre-survey
- Evaluation procedure
    - Phase 1: Offline ML module testing (walk-forward validation on synthetic data)
    - Phase 2: Qualitative pilot (small-group usability observation)
    - Phase 3: SUS administration (30 users after 14-day usage period)

#### Ethical Considerations

- Informed consent for financial data collection
- Compliance with RA 10173 (Data Privacy Act)
- Data anonymization before server transmission
- User rights: data access, correction, deletion
- App disclaimers: all intelligent features are informational; user retains final financial decisions
- Institutional ethics clearance: *To be confirmed*

#### Data Collection for ML Training

- Synthetic data generated from BSP, PSA, and pre-survey results
- No real user data used for training without consent
- Pilot user data (with consent) may supplement synthetic data