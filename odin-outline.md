# Odin — Full Scope Outline

---

## System

### Platform

- Mobile-first application
- Web-accessible application

---

### Target Users

- Filipino working young adults
    - Age range: 20–40
    - Geographic scope: Metro Manila

### Input

#### Manual transaction entry

- Income entry
- Expense entry
- Recurring transaction scheduling

#### Expense categorization

- FIES-grounded category taxonomy

#### User profile onboarding

- Income type (stable / variable)
- Financial obligation level (flexible / obligated)

---

### Modules

#### Financial Behavioral Profile Classification

- Four user profiles
    - Stable-Flexible
    - Stable-Obligated
    - Variable-Flexible
    - Variable-Obligated
- Initial classification on onboarding
- Reclassification triggered by behavior change
- Classification algorithm: Random Forest Algorithm

#### Budget Recommendation

- Profile-informed budget generation
- Income vs. expense basis: TBD
- Budget time horizons: TBD
- Budgeting strategies distilled: TBD
- Surplus handling: TBD
- Recommendation algorithm: TBD



#### Expense Forecasting

- Per-category forecasting
    - Daily
    - Weekly
    - Monthly
- Cold-start fallback mechanism

#### Anomaly Detection

- Rule-based budget overage detection

#### Savings Goal Tracking

- Goal creation and targeting
- Progress monitoring

#### Debt Management

- Avalanche method
- Snowball method

---

### Evaluation

- ISO/IEC 25010:2023
- System Usability Scale (SUS)

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

- Inclusions
- Exclusions

#### Definition of Terms

---

### Review of Related Literature

#### Overview

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

---

#### Synthesis

---

### Research Methodology

#### Research Design

- Research paradigm
- Development methodology

#### System Architecture (Move this to "## System")

- Overall architecture
- Module interaction design

#### System Design (Move this to "## System")

- User profile design
- Expense categorization scheme
- Transaction input design
- Budget recommendation design
- Forecasting model design
- Anomaly detection design
- Savings and debt management design

#### Evaluation Design

- ISO/IEC 25010:2023 quality model application
- SUS instrument and administration
- Respondent profile
- Evaluation procedure