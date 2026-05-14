# Topic Outline

## Development of Odin: A Personal Finance Management System Using Decision Tree, LSTM, and Isolation Forest

---

> **How to read this document**
> `[/shorthand]` tags appear beside every node — use them as folder names or paper-tracking IDs.
> Each numbered topic (1–N) is a major conceptual territory the thesis must cover.
> Each lettered subtopic (A, B, C…) is a research area within that territory and maps to one RRL section.
> Each Roman-numeral sub-subtopic (I, II, III…) is a specific claim or research question the literature must establish.
> Bulleted items beneath a sub-subtopic are the specific instantiations or dimensions of that claim.
> The *Scholar query* below each sub-subtopic is ready to paste into Google Scholar Labs.
> Every section is written through three synthesis lenses: (1) what the literature agrees on, (2) where disagreements or diverging findings exist, and (3) what gaps remain that Odin addresses.

---

## 1. Filipino Young Professionals and the Financial Problem [/fil-yp-problem]

### 1.A Filipino Young Professionals as a Demographic [/fil-yp-demographic]

#### [X] 1.A.I Demographic profile: age range, employment sectors, and geographic concentration [/yp-profile]
> *Scholar query: What is the demographic profile of Filipino young professionals aged 20 to 40 — including their dominant employment sectors, geographic distribution across Metro Manila and urban centers, and household composition — as documented in national surveys or institutional data from the Bangko Sentral ng Pilipinas, Philippine Statistics Authority, or similar sources?*

#### 1.A.II Income structure typology: salaried, freelance, gig, informal, and mixed earners [/income-typology]
> *Scholar query: How do researchers classify the income structures of Filipino young professionals, particularly the distinction between salaried, freelance, gig-economy, informal, and mixed-income earners? I am looking for studies that document the typology of income arrangements among Filipino workers in the millennial and Gen Z age range, and how these income types shape personal finance behavior and spending decisions.*

> **Note:** Literature on regular salaried employees in this demographic is comparatively thin. Pre-survey data from the pilot study may be needed to substantiate claims specific to this income type.

#### 1.A.III Financial literacy levels and the gap between knowledge and behavior [/literacy-behavior-gap]
> *Scholar query: What is the documented level of financial literacy among Filipino young professionals, and what evidence exists that higher financial literacy does not reliably translate into disciplined financial behavior? I am looking for studies that measure both knowledge and actual financial behavior in this demographic — particularly findings that show a gap between what Filipino young adults know about personal finance and what they actually do with their money.*

#### 1.A.IV Prevalence and severity of financial management problems in this demographic [/fin-problem-prevalence]
> *Scholar query: How prevalent and severe are personal financial management problems — such as insufficient savings, debt reliance, and budget non-adherence — among Filipino young professionals aged 20 to 40 in Metro Manila? I am looking for quantitative studies or institutional survey data that document the proportion of this demographic experiencing financial difficulty, the specific nature of those difficulties, and how these problems compare across income types.*

---

### 1.B Financial Structure of Filipino Young Professionals [/fin-structure]

#### [X] 1.B.I Income patterns: frequency, regularity, and amount across employment types [/income-patterns]
> *Scholar query: What are the documented income patterns of Filipino young professionals across different employment types — including the frequency of income receipt such as semi-monthly payroll cycles, the regularity or volatility of income amounts, and how these patterns differ between salaried and variable-income workers? I am looking for empirical studies or institutional data that characterize how Filipino young adults receive their income and how that shapes their financial planning horizons.*

#### 1.B.II Expenditure patterns: category-level allocation across income stability types [/expenditure-patterns]
> *Scholar query: What do empirical studies reveal about the household or personal expenditure patterns of Filipino young professionals when disaggregated by income stability type? I am looking for research that compares how workers with stable salaried income allocate spending across categories differently from those with irregular, freelance, or mixed income — including data from Philippine institutional sources such as FIES or BSP survey instruments.*

#### 1.B.III Financial goals: savings targets, fund accumulation, debt repayment, and investment intentions [/fin-goals]
> *Scholar query: What financial goals do Filipino young professionals most commonly pursue — including short-term savings targets, emergency fund accumulation, debt repayment plans, and longer-term investment intentions — and how do these goals vary by income type, employment status, and demographic characteristics? I am looking for studies that document declared or revealed financial goal-setting behavior in this population.*

#### 1.B.IV Debt structure and debt management behavior [/debt-structure]
> *Scholar query: What is the documented debt structure of Filipino young professionals — including the types of debt they carry, the proportion of income consumed by debt service, and how they manage or fail to manage debt repayment — as reported in national surveys or empirical studies? I am looking for evidence on how debt behavior differs across salaried versus variable-income young professionals and what consequences poor debt management produces.*

---

### 1.C Financial Behavior of Filipino Young Professionals [/fin-behavior]

#### 1.C.I Budgeting practice: prevalence, methods, and time horizons [/budgeting-prevalence]
> *Scholar query: How prevalent is active budgeting practice among Filipino millennials and Gen Z, and what budgeting methods and time horizons — weekly, semi-monthly, or monthly — do they most commonly use? I am looking for studies that measure the proportion of Filipino young adults who maintain a budget, the formats or tools they use, and the behavioral or demographic factors that predict whether someone budgets at all — particularly in Metro Manila or urban Philippine settings.*

#### 1.C.II Financial behavior differences across income stability types [/income-type-behavior-diff]
> *Scholar query: How do the financial management behaviors of Filipino workers with stable income differ from those with variable or irregular income? I am looking for comparative studies that show how income predictability affects budgeting discipline, savings rates, expense prioritization, and financial stress — particularly for young professionals in the Philippines who move between employment types or hold multiple income sources simultaneously.*

#### 1.C.III Budget failure points: irregular tracking, impulse overspending, and unplanned obligatory expenses [/budget-failure-points]
> *Scholar query: What are the most commonly documented failure points in personal finance management among Filipino young adults? I am specifically interested in research that identifies irregular or inconsistent transaction tracking, impulse or unplanned overspending, and the destabilizing effect of sudden obligatory expenses — such as medical costs, family emergencies, or periodic lump-sum payments — as the primary reasons budgets break down in practice.*

#### 1.C.IV Evidence that intelligent adaptive tools outperform financial literacy-only interventions [/intelligent-vs-literacy]
> *Scholar query: What evidence exists that intelligent or adaptive budgeting systems produce better financial behavior outcomes than financial literacy education alone? I am looking for studies that compare the effectiveness of tool-mediated interventions — such as automated tracking, personalized alerts, or algorithmic budget recommendations — against purely instructional or literacy-based approaches, particularly in populations of young adults where behavioral support matters more than knowledge transfer.*

---

## 2. Filipino Cultural Context in Personal Finance [/fil-cultural-context]

> **Note:** This topic is a cross-cutting input. The cultural patterns documented here are directly referenced by the expense categorization, behavioral profiling, spending forecasting, budget recommendation, and anomaly detection sections. Literature in this topic should be cited wherever those downstream modules require cultural grounding.

### 2.A Culturally Specific Financial Practices [/cultural-practices]

#### 2.A.I Informal financial mechanisms: paluwagan, rotating savings, and community lending [/informal-fin-mechanisms]
> *Scholar query: What informal financial mechanisms are documented among Filipino households and young professionals — particularly paluwagan (rotating savings and credit associations), community lending, and peer-to-peer borrowing — and how do these practices affect cash flow patterns, budget adherence, and savings behavior? I am looking for studies that characterize participation rates, contribution structures, and the financial consequences of these mechanisms for individual budget management.*

#### 2.A.II Family financial obligations: remittances, breadwinner expectations, and utang na loob [/family-obligations]
> *Scholar query: What culturally specific family financial obligations — including regular remittances to parents or siblings, breadwinner expectations, and the social norm of utang na loob as a felt financial duty — are documented among Filipino young professionals, and how do these obligations affect their personal budget allocation and savings capacity? I am looking for studies that quantify the proportion of income directed toward family support and that characterize the social pressure mechanisms that make these obligations difficult to reduce.*

#### 2.A.III Community and religious financial contributions [/community-religious-contrib]
> *Scholar query: What community and religious financial contributions — including church donations, fiesta preparation costs, bayanihan-type shared expenses, and ambag contributions — are documented as regular outflows among Filipino young adults, and how do these affect personal budget management? I am looking for studies that describe the frequency, amount, and obligatory versus voluntary character of these contributions and their interaction with formal budgeting practice.*

#### 2.A.IV Government-mandated financial obligations: SSS, PhilHealth, and Pag-IBIG contributions [/mandated-contributions]
> *Scholar query: How are SSS, PhilHealth, and Pag-IBIG contributions treated in the personal financial management of Filipino young professionals — particularly the distinction between automatic payroll deductions for employed workers and voluntary self-payment for freelance or self-employed workers? I am looking for research or regulatory documentation that characterizes these contributions as a distinct category of obligatory expense and discusses how their treatment differs across employment types.*

---

### 2.B Seasonal and Cyclical Spending Patterns [/seasonal-patterns]

#### 2.B.I Calendar-driven spending spikes and suppression cycles [/calendar-spending-cycles]
> *Scholar query: What calendar-driven spending spikes and suppression cycles are documented among Filipino households and young professionals? I am looking for empirical or observational studies that characterize how spending behavior changes predictably across the calendar year — including the pre-payday suppression period known as petsa de peligro, the post-payday spending surge, and the seasonal escalation during the ber months leading to Christmas — and that quantify the magnitude of these fluctuations.*

> **Note:** This sub-subtopic should cover the following documented Filipino spending cycle events:
> - *Petsa de peligro*: pre-payday spending suppression in the days before salary release
> - Payday spree: post-payday spending spike immediately following income receipt
> - 13th month pay effect: bonus-driven December spending surge
> - Christmas / Ber Months: September–December seasonal spending escalation
> - *Semana Santa* / Holy Week: travel and leisure spending spike
> - School enrollment season: school fees, uniforms, and supplies spending spike
> - *Undas* / All Saints' Day: travel and family reunion-related spending spike
> - MMFF season: post-Christmas cinema and leisure spending spike
> - Paluwagan contribution cycle: periodic obligation-driven cash outflow
> - *Ambag* / community collection cycle: periodic shared-expense outflow
> - Summer-related consumption spike

#### 2.B.II Implications of cyclical patterns for forecasting, anomaly detection, and budget recommendation [/cyclical-pattern-implications]
> *Scholar query: What are the implications of documented Filipino seasonal and cyclical spending patterns for the design of spending forecasting models, anomaly detection systems, and budget recommendation algorithms? I am looking for research that discusses how failure to account for these patterns produces systematic forecasting errors, anomaly false positives during culturally expected spending spikes, or budget recommendations that are unrealistic during high-obligation periods.*

---

### 2.C User-Declared Financial Preferences [/user-preferences]

> **Note:** This subtopic covers preferences that users *declare* at onboarding or configure over time, as opposed to behavioral patterns inferred from transaction data. The RRL grounding is conservative: literature supports the need for systems to accommodate user-defined priorities rather than prescribing a single allocation logic.

#### 2.C.I Protected expense categories: non-negotiable spending floors declared by users [/protected-categories]
> *Scholar query: What evidence exists that personal finance systems should allow users to designate certain expense categories as protected or non-negotiable — meaning the system will not recommend reducing spending in those categories regardless of optimization pressure — and what categories are most commonly treated this way by Filipino users? I am looking for research that grounds protected category logic in documented user financial behavior rather than treating it as a purely technical design decision.*

#### 2.C.II Category and goal prioritization as user-configurable inputs to recommendation logic [/priority-config]
> *Scholar query: How have personal finance systems implemented user-configurable priority hierarchies — such as allowing users to rank their savings goal above discretionary spending, or to treat debt repayment as higher priority than leisure — as direct inputs to budget recommendation or allocation algorithms? I am looking for system design literature or user studies that evaluate the effect of allowing users to declare their own priority structures on recommendation acceptance and adherence.*

---

## 3. Expense Categorization in Personal Finance Systems [/expense-categorization]

### 3.A Expense Categorization Frameworks [/cat-frameworks]

#### 3.A.I Approaches to expense categorization: user-defined, institutionally derived, ML-generated, and hybrid [/cat-approaches]
> *Scholar query: What approaches to expense categorization have been implemented in personal finance systems, and how do they compare? I am looking for research that evaluates user-defined category taxonomies, institutionally derived category schemes based on national expenditure surveys, machine learning-generated categorizations from transaction descriptions, and hybrid approaches that combine these methods — with attention to the tradeoffs between flexibility, accuracy, and cultural appropriateness for different user populations.*

#### 3.A.II PSA FIES and BSP CFS expenditure categories as the authoritative local standard [/fies-bsp-categories]
> *Scholar query: How are the expenditure categories defined in the PSA Family Income and Expenditure Survey and the BSP Consumer Finance Survey structured, and how can they be mapped to the expense category system of a local Filipino personal finance management application? I am looking for research or documentation that uses these institutional survey instruments as a basis for designing culturally grounded expense taxonomies, and that demonstrates how FIES and BSP CFS categories can inform the default category structure of a PFMS serving Filipino users.*

#### 3.A.III Limitations of Western category schemas for Filipino spending contexts [/western-cat-limitations]
> *Scholar query: In what ways do Western-designed expense category schemas fail to adequately represent Filipino spending patterns and financial obligations? I am looking for research or design literature that identifies specific mismatches — such as the absence of categories for paluwagan contributions, family remittances, or multi-household financial support — and that argues for the inadequacy of importing foreign categorization schemes into Filipino personal finance applications without significant local adaptation.*

---

### 3.B Expense Category Design Considerations [/cat-design]

#### 3.B.I Discretionary, essential, obligatory, and financial expense groupings [/cat-groupings]
> *Scholar query: How have personal finance systems and financial behavior researchers structured the grouping of expense categories into higher-level classifications — such as essential versus discretionary, or obligatory versus voluntary — and what evidence supports these groupings as meaningful for budget recommendation and behavioral monitoring? I am looking for research that grounds multi-tier category hierarchies in actual spending behavior data rather than arbitrary convention.*

#### 3.B.II Category ambiguity as a driver of user abandonment [/cat-ambiguity]
> *Scholar query: What evidence exists that ambiguous or poorly designed expense categories — where users are uncertain which category a transaction belongs to — are a significant driver of frustration and abandonment in personal finance applications? I am looking for usability studies or qualitative research that identifies category ambiguity as a distinct failure mode, separate from general data entry burden, and that discusses design strategies for reducing it.*

#### 3.B.III Culturally specific categories warranting dedicated treatment: paluwagan, remittances, and religious obligations [/cultural-expense-categories]
> *Scholar query: What culturally specific expense types in Filipino financial practice warrant dedicated categories in a personal finance management system, rather than being absorbed into generic miscellaneous or social expense buckets? I am looking for literature that documents the financial significance and regularity of paluwagan contributions, family remittances, religious and community donations, and similar obligations — and that makes the case that these represent distinct behavioral and budgeting domains that should be tracked separately.*

---

## 4. Existing Personal Finance and Budget Management Systems [/existing-pfms]

### 4.A Landscape of Existing Systems [/pfms-landscape]

#### 4.A.I Classification and typology of PFMS and PBMS in the literature [/pfms-typology]
> *Scholar query: How do recent studies classify and distinguish personal finance management systems and personal budget management systems? I am looking for literature that proposes or applies typologies of these tools — for example, distinguishing between expense tracking apps, budgeting planners, goal-setting tools, and hybrid systems — and that surveys the landscape of such applications with attention to their feature sets, technological approaches, and intended user bases.*

#### 4.A.II Feature sets of existing systems and evidence of their effectiveness [/pfms-features]
> *Scholar query: What are the dominant features found in personal budget management systems, and what evidence exists that these features actually improve users' financial outcomes? I am looking for evaluations or systematic reviews of PFMS applications that assess the impact of specific functionalities — such as transaction categorization, budget setting, visualization dashboards, or alerts — on user financial behavior, adherence to budgets, or savings outcomes.*

#### 4.A.III Intelligent and adaptive features: forecasting, anomaly detection, and recommendation in existing systems [/pfms-intelligent-features]
> *Scholar query: What intelligent or adaptive features — such as spending forecasting, anomaly or overspending detection, and personalized budget recommendation — have been implemented in existing personal finance management systems, and what results have they produced? I am looking for system papers or evaluations that document ML-driven or algorithmic features in PFMS tools, reporting accuracy, user acceptance, and behavioral impact where available.*

---

### 4.B Limitations and Gaps in Existing Systems [/pfms-gaps]

#### 4.B.I Documented limitations: manual entry burden, absence of forecasting, generic categories, no profiling [/pfms-limitations]
> *Scholar query: What limitations of existing personal finance and budgeting applications are most consistently identified in research literature? I am specifically interested in studies that critique the usability cost of manual transaction entry, the absence of predictive or forecasting capabilities, the lack of anomaly or overspending detection, the use of generic expense categories that do not reflect actual user spending, and the absence of behavioral user profiling.*

#### 4.B.II Absence of locally grounded systems for Filipino users [/pfms-local-gap]
> *Scholar query: What gap exists in the current landscape of personal finance management systems when evaluated against the needs of Filipino users, particularly young professionals with culturally specific financial obligations and variable income structures? I am looking for research that articulates why existing PFMS tools — typically designed for Western users or generic populations — fail to address local spending norms, income patterns, or the need for intelligent, adaptive, and context-aware budgeting support.*

#### 4.B.III Design and architecture patterns transferable to Odin from existing systems [/pfms-transferable]
> *Scholar query: What design decisions, system architectures, or implementation patterns from existing personal finance management systems — regardless of their target population — are transferable to a locally grounded, mobile-first, intelligent PFMS serving Filipino young professionals? I am looking for system papers that provide reusable architectural, algorithmic, or UX insights beyond their specific deployment context.*

---

## 5. Financial Behavioral Profiling [/behavioral-profiling]

### 5.A Financial Behavioral Profiles in Personal Finance [/profile-domain]

#### 5.A.I Role of behavioral profiling in personalizing budget recommendation, forecasting, and anomaly detection [/profiling-role]
> *Scholar query: What role does user behavioral profiling play in enabling personalization within personal finance management systems — specifically in improving budget recommendation accuracy, providing fallback behavior for new users during cold start, and tailoring forecasting and anomaly detection to individual spending patterns? I am looking for system design literature or implemented PFMS studies that demonstrate how assigning users to profile types shapes the output of downstream algorithmic modules.*

#### 5.A.II Inadequacy of Western behavioral taxonomies for Filipino financial user contexts [/western-taxonomy-gap]
> *Scholar query: Why are Western financial behavioral taxonomies and financial personality frameworks inadequate for characterizing Filipino users' financial behavior? I am looking for research that documents the cultural, structural, and institutional differences between Filipino and Western financial contexts — and that argues for locally grounded profile construction rather than applying imported frameworks.*

#### 5.A.III Behavioral dimensions as meaningful profile differentiators: income stability and obligation weight [/profile-dimensions]
> *Scholar query: What behavioral dimensions — such as income stability and the weight of obligatory versus discretionary spending — are most meaningful for differentiating financial behavioral user profiles? I am looking for research that validates these dimensions as discriminating features rather than arbitrary groupings, and that demonstrates how users who differ along these axes require different budgeting strategies, recommendation logic, or forecasting approaches.*

#### 5.A.IV Constructing locally grounded financial profiles from Philippine institutional and behavioral data [/fil-profile-construction]
> *Scholar query: How can locally grounded financial behavioral profiles or user archetypes be constructed from Philippine institutional data sources such as the FIES and BSP CFS, or from observed transaction behavior? I am looking for methodological literature on deriving user typologies from survey or expenditure datasets — including clustering, segmentation, or expert-informed classification approaches — applied to data that captures Filipino household financial structure.*

---

### 5.B Profile Dynamics and the Cold-Start Problem [/profile-dynamics]

#### 5.B.I Concept drift as the framework for progressive profile updates over time [/concept-drift]
> *Scholar query: How is the concept drift framework applied to adaptive user modeling and profile updates in intelligent systems, and how does it apply to progressively updating a user's financial behavioral profile as their spending and income patterns evolve? I am looking for literature on drift detection methods and adaptive learning strategies that serve as the technical grounding for a system that updates user profiles based on behavioral signal accumulation over time.*

#### 5.B.II Behavioral signals that should trigger profile reassessment [/profile-triggers]
> *Scholar query: What behavioral signals in a personal finance system should trigger a reassessment or reclassification of a user's financial behavioral profile? I am looking for research on change-point detection, sustained behavioral shifts, or threshold-based triggers in adaptive user modeling — applied to signals such as sustained income level changes, shifts in the proportion of obligatory versus discretionary spending, or consistent departures from the patterns used to initially classify the user.*

#### 5.B.III Cold-start problem: profile-average fallback for users without behavioral history [/profiling-cold-start]
> *Scholar query: How is the cold-start problem handled in personalized financial systems for new users who have no behavioral transaction history? I am looking for research on profile-average or population prior fallback strategies — where a new user is initially assigned to a default profile based on onboarding input or demographic similarity — and on how quickly systems can transition from generic to personalized behavior as user data accumulates.*

---

### 5.C Financial Behavioral Profile Classification Algorithm [/profile-classification-algo]

#### 5.C.I Supervised classification versus clustering for predefined profile categories [/classification-vs-clustering]
> *Scholar query: When should supervised classification be chosen over clustering for assigning users to financial behavioral profiles, particularly when the profile categories are predefined by domain knowledge rather than discovered from data? I am looking for research that discusses the suitability of supervised versus unsupervised approaches in the context of fixed profile taxonomies — arguing that classification is appropriate when profiles are already specified and the task is to assign users, not to discover new groupings.*

#### 5.C.II Candidate classification algorithms for behavioral and financial user profiling [/classifier-candidates]
> *Scholar query: What classification algorithms have been applied to behavioral or financial user profiling tasks — including decision trees, logistic regression, support vector machines, Random Forest, and gradient boosting classifiers — and what results do they produce in terms of accuracy, interpretability, and feature importance? I am looking for comparative studies that benchmark multiple classifiers on user profile or customer segmentation tasks using behavioral or financial feature sets.*

#### 5.C.III Feature selection: onboarding questionnaire data versus accumulated transaction behavioral data [/classifier-features]
> *Scholar query: What features are most appropriate for classifying a user's financial behavioral profile — questionnaire responses collected during onboarding, early transaction behavioral data, or a combination of both? I am looking for research on feature selection and feature engineering for financial user profiling classifiers, including evidence on which input types produce more accurate profile assignments and how the feature set should evolve as behavioral data accumulates.*

#### 5.C.IV Cold-start classification: training a classifier without labeled real user data at launch [/classifier-cold-start]
> *Scholar query: How can a supervised user profile classifier be trained when no labeled real user data exists at system launch? I am looking for research on approaches such as synthetic data generation, expert-defined feature distributions, or simulation-based training that allow a classification model to be deployed before the system has acquired real behavioral data from actual users.*

#### 5.C.V Progressive reclassification: periodic, continuous, and drift-triggered profile update strategies [/progressive-reclassification]
> *Scholar query: What strategies exist for progressively reclassifying users into updated financial behavioral profiles over time — including periodic batch reclassification, continuous online learning, and drift-triggered reassessment? I am looking for research that evaluates these update strategies in terms of classification stability, responsiveness to genuine behavioral change, and resistance to noise-driven spurious reclassifications.*

#### 5.C.VI Tradeoffs across candidate classifiers: predictive accuracy, interpretability, and mobile feasibility [/classifier-tradeoffs]
> *Scholar query: What are the tradeoffs among candidate classification algorithms for financial user profiling when evaluated along dimensions of predictive accuracy, interpretability of predictions, and mobile deployment feasibility? I am looking for comparative analyses that show how algorithms differ when the deployment environment is a resource-constrained mobile application and when the classification decision must be explainable or auditable.*

#### 5.C.VII Evaluation metrics for profile classification: accuracy, precision, recall, and F1-score [/classifier-eval-metrics]
> *Scholar query: What evaluation metrics are appropriate for assessing the performance of a supervised classification model applied to financial behavioral user profiling, and how are accuracy, precision, recall, and F1-score interpreted and applied in this context? I am looking for research that discusses metric selection for multi-class classification tasks where class imbalance may exist and where the cost of misclassification differs across profile types.*

---

## 6. Spending Forecasting [/spending-forecasting]

### 6.A Predictive Modeling in Personal Finance Systems [/predictive-modeling-domain]

#### 6.A.I Survey of forecasting methods applied to personal or household spending data [/forecasting-methods-survey]
> *Scholar query: What forecasting methods have been applied to personal spending or household expenditure data, and how do they compare in accuracy and practical suitability? I am looking for comparative studies that benchmark approaches such as ARIMA, LSTM, gradient boosting, and other time-series or regression models against personal finance or consumer spending datasets — with attention to which methods handle irregular spending patterns, categorical breakdowns, and small individual-level datasets most effectively.*

#### 6.A.II Temporal dependency in spending data: prior periods as predictors of subsequent periods [/temporal-dependency]
> *Scholar query: What empirical evidence exists that personal spending behavior exhibits temporal dependency — that is, that spending in prior periods is predictive of spending in subsequent periods? I am looking for studies that quantify autocorrelation or lag effects in household or individual-level expenditure data, and that use this evidence to justify the application of sequential models, particularly in contexts where spending patterns repeat across daily, weekly, or monthly cycles.*

#### 6.A.III Per-category forecasting: multi-output prediction across simultaneous expense categories [/per-category-forecast]
> *Scholar query: How have researchers approached the problem of forecasting spending across multiple expense categories simultaneously, rather than predicting total spending as a single aggregate figure? I am looking for studies that use multi-output or multi-variate forecasting models applied to disaggregated household or personal expenditure data organized by category, and that report results on per-category prediction accuracy.*

#### 6.A.IV Cold-start fallback strategies for forecasting with insufficient transaction history [/forecast-cold-start]
> *Scholar query: What cold-start fallback strategies are used in forecasting systems when a user does not yet have sufficient transaction history to generate a reliable personalized prediction? I am looking for research on how personal finance or recommender systems handle new users — including population average priors, profile-based initialization, and conservative default forecasts — and what evidence exists for the appropriateness of each fallback approach.*

#### 6.A.V Mobile deployment constraints and their effect on forecasting algorithm selection [/mobile-forecast-constraints]
> *Scholar query: How do mobile deployment constraints — such as limited memory, processing power, and battery life — affect the practical selection of a spending forecasting algorithm in personal finance applications? I am looking for research that evaluates the feasibility of running forecasting models on-device or with minimal server dependency, and that discusses how model size, inference latency, and retraining frequency factor into algorithm selection for mobile-first deployments.*

---

### 6.B Spending Forecasting Algorithm [/forecasting-algo]

#### 6.B.I Candidate forecasting algorithms for sequential personal spending data [/forecast-algo-candidates]
> *Scholar query: What algorithms are most commonly applied to sequential personal or household spending forecasting tasks, and what are the documented strengths and weaknesses of each? I am looking for comparative literature covering statistical approaches such as ARIMA and exponential smoothing, tree-based methods such as gradient boosting, and deep learning approaches such as LSTM and GRU — with attention to how each handles non-linearity, temporal dependency, and sparse individual-level data.*

#### 6.B.II Comparative performance of candidate algorithms on time-series forecasting tasks [/forecast-algo-comparison]
> *Scholar query: How do candidate forecasting algorithms compare in empirical benchmark studies on time-series prediction tasks relevant to personal spending — particularly comparisons between ARIMA, LSTM, GRU, gradient boosting, and hybrid models? I am looking for studies that report quantitative accuracy metrics such as RMSE, MAE, MAPE, and SMAPE across these model families and that discuss the conditions under which each maintains a performance advantage.*

#### 6.B.III Algorithm behavior under data sparsity and the cold-start condition [/forecast-algo-sparsity]
> *Scholar query: How do forecasting algorithms perform when applied to sparse, low-frequency, or newly initialized datasets — such as those produced by manual transaction entry from a new user with no history? I am looking for research that evaluates algorithm robustness under limited data conditions and that recommends fallback or warm-start strategies specific to the data sparsity regime.*

#### 6.B.IV Tradeoffs across candidate algorithms: accuracy, computational cost, interpretability, and mobile feasibility [/forecast-algo-tradeoffs]
> *Scholar query: What are the key tradeoffs among candidate spending forecasting algorithms when evaluated along dimensions of predictive accuracy, computational cost, user-facing interpretability, and suitability for mobile deployment? I am looking for comparative analyses or design discussions that explicitly weigh these dimensions in the context of personal finance systems running on resource-constrained mobile devices.*

#### 6.B.V Evaluation metrics for spending forecasting: MAE, RMSE, SMAPE, and MDA [/forecast-eval-metrics]
> *Scholar query: What evaluation metrics are most appropriate for assessing the performance of a spending forecasting model in a personal finance context, and how are MAE, RMSE, SMAPE, and mean directional accuracy interpreted and applied? I am looking for research that justifies metric selection for personal expenditure forecasting tasks — particularly the choice between scale-dependent and scale-independent metrics, and the relevance of directional accuracy for user-facing forecast display.*

---

## 7. Budget Recommendation [/budget-recommendation]

### 7.A Budgeting Strategies as Domain Knowledge [/budgeting-strategies-domain]

> **Note:** This subtopic establishes the domain knowledge that motivates the recommendation module's constraint logic and allocation structure. Budgeting strategies are treated here as theoretical grounding — the literature basis for why certain design decisions (minimum floors, savings prioritization, category caps) are valid — rather than as user-selectable configurations. User-configurable preferences are covered under Topic 2.C.

#### 7.A.I Core mechanics of documented budgeting strategies [/strategy-mechanics]
> *Scholar query: What are the core mechanics and structural logic of the major budgeting strategies documented in personal finance literature — including zero-based budgeting, the envelope method, proportional allocation rules such as 50-30-20, and pay-yourself-first? I am looking for studies or reviews that explain how each strategy defines categories, divides income, and allocates spending — and what behaviors each strategy is designed to reinforce.*

#### 7.A.II Comparative strengths and weaknesses across income stability types [/strategy-income-fit]
> *Scholar query: How do the strengths and weaknesses of major budgeting strategies compare when applied to users with different income stability profiles — particularly stable salaried versus irregular or freelance earners? I am looking for research that assesses which budgeting frameworks perform better for predictable monthly income versus lumpy or variable cash flows, and what modifications are recommended for non-standard income patterns.*

#### 7.A.III Behavioral evidence that structured budgeting improves financial outcomes [/budgeting-evidence]
> *Scholar query: What behavioral evidence exists that structured budgeting — as opposed to informal or no budgeting — produces measurable improvements in savings rates, debt reduction, and spending discipline? I am looking for empirical studies, including randomized experiments or longitudinal analyses, that demonstrate the effect of budget adherence on financial outcomes across a range of user populations.*

---

### 7.B Budget Recommendation in Personal Finance Systems [/budget-rec-domain]

#### 7.B.I Approaches to budget recommendation in existing systems: rule-based, optimization-based, and data-driven [/budget-rec-approaches]
> *Scholar query: What approaches to budget recommendation have been implemented in personal finance management systems, and how do they compare? I am looking for research that describes rule-based systems with fixed allocation proportions, constraint-based optimization approaches that maximize savings subject to spending floors, and data-driven or ML-based recommendation engines — with attention to the tradeoffs between simplicity, adaptability, and user acceptance.*

#### 7.B.II Constraint-based allocation: income floors, spending caps, and protected category logic [/constraint-allocation]
> *Scholar query: How is constraint-based allocation implemented in budget recommendation systems — specifically the logic of income-based spending caps, minimum spending floors for essential categories, and the protection of non-negotiable expense categories from optimization pressure? I am looking for research or system design literature that describes how these constraints are encoded and solved, and what happens to recommendation quality when constraints are violated or infeasible.*

#### 7.B.III Behavioral evidence for the effectiveness of automated budget recommendations [/budget-rec-evidence]
> *Scholar query: What behavioral evidence exists that automated or algorithmic budget recommendations — as opposed to self-directed budgeting — improve financial outcomes such as savings rates, budget adherence, and debt reduction? I am looking for experimental or quasi-experimental studies that isolate the effect of recommendation system output on user financial behavior.*

#### 7.B.IV Budget period surplus handling: reset versus carryforward logic [/surplus-handling]
> *Scholar query: How should a personal finance system handle budget surplus at the end of a period — should unspent funds reset to zero or carry forward? I am looking for research or system design literature that discusses this decision, particularly in relation to income type: whether carryforward logic is more appropriate for variable income earners who may experience lean periods following flush ones, versus reset logic for stable salaried users.*

---

### 7.C Budget Recommendation Algorithm [/budget-rec-algo]

#### 7.C.I Problem formulation: resource allocation, constrained optimization, or hybrid recommendation [/budget-rec-formulation]
> *Scholar query: How is the budget recommendation problem formally framed in the research literature — as a resource allocation problem, a constrained optimization problem, a ranking task, or a hybrid recommendation problem? I am looking for work that explicitly characterizes the computational structure of budget generation and evaluates how different problem formulations affect the tractability, explainability, and user-facing output of the recommendation system.*

#### 7.C.II Candidate algorithms for budget distribution and financial resource allocation [/budget-rec-algo-candidates]
> *Scholar query: What algorithmic solutions have been applied to the problem of distributing a limited financial resource across competing spending categories? I am looking for research on linear programming, multi-objective optimization, goal programming, reinforcement learning, and related techniques as applied to household or personal budget allocation — with attention to how constraints such as minimum essential spending, savings targets, and category caps are encoded and solved.*

#### 7.C.III Tradeoffs across candidate algorithms: mobile feasibility, explainability, adaptability, and cold-start performance [/budget-rec-algo-tradeoffs]
> *Scholar query: What are the key tradeoffs among candidate budget recommendation algorithms when evaluated along dimensions of mobile deployment feasibility, user-facing explainability, adaptability to changing user circumstances, and cold-start performance with limited historical data? I am looking for comparative studies or design analyses that assess these tradeoffs specifically in the context of personal finance systems serving users with variable income and limited transaction history.*

#### 7.C.IV Evaluation metrics for budget recommendation: MAPE, RMSE, and variance analysis [/budget-rec-eval-metrics]
> *Scholar query: What evaluation metrics are appropriate for assessing the performance of a budget recommendation algorithm in a personal finance context — specifically the use of MAPE, RMSE, and variance analysis to measure how closely algorithmic recommendations match optimal or user-validated allocations? I am looking for research that justifies these metrics for recommendation evaluation tasks and discusses how to construct a ground truth or reference allocation for comparison.*

---

## 8. Anomalous Spending Detection [/anomaly-detection]

### 8.A Anomaly Detection in Personal Finance Systems [/anomaly-domain]

#### 8.A.I Definition and taxonomy of financial anomalies in personal spending data [/anomaly-taxonomy]
> *Scholar query: How do researchers define and classify the types of anomalies that are detectable in personal spending or financial transaction data? I am looking for literature that develops or applies a taxonomy of financial anomalies at the individual or household level — distinguishing between sudden spending spikes, unusual category patterns, behavioral deviations from a user's established baseline, and budget overage events — and that discusses which detection approaches are appropriate for each type.*

#### 8.A.II Threshold-based overage alerting versus behavioral baseline deviation detection [/overage-vs-deviation]
> *Scholar query: What is the conceptual and technical distinction between threshold-based budget overage alerting and behavioral baseline deviation detection in personal finance systems? I am looking for research that separates these two mechanisms — where overage alerting fires when a user exceeds a predefined budget limit, and baseline deviation detection fires when spending departs from the user's own historical norm regardless of a budget — and that discusses the appropriate scope and limitations of each approach.*

#### 8.A.III Behavioral evidence for the impact of anomaly and overspending alerts on user financial behavior [/anomaly-behavioral-evidence]
> *Scholar query: What behavioral evidence exists that anomaly detection alerts or overspending notifications in personal finance applications produce measurable changes in user financial behavior — such as reduced spending, increased budget adherence, or improved savings? I am looking for experimental or quasi-experimental studies that isolate the effect of alert delivery on subsequent financial decisions.*

#### 8.A.IV Alert design: frequency, framing, and format to minimize fatigue while ensuring action [/alert-design]
> *Scholar query: What does research say about designing anomaly or overspending alerts in mobile personal finance applications to minimize alert fatigue while still prompting user action? I am looking for studies that evaluate alert frequency, notification timing, and framing strategies in the context of financial applications — and that report user behavioral responses and the conditions under which alerts are acted on versus dismissed.*

#### 8.A.V Culturally expected high-value spending events and their treatment in anomaly detection [/cultural-spending-anomaly]
> *Scholar query: How should a personal finance anomaly detection system handle culturally specific high-value spending events that are expected and planned by Filipino users — such as paluwagan contributions, Christmas gift spending, or family remittances — but that might appear anomalous by statistical measures? I am looking for research on protecting or whitelisting culturally normative spending from anomaly detection, and on how systems can distinguish between planned extraordinary expenses and genuine deviations.*

---

### 8.B Anomaly Detection Algorithm [/anomaly-algo]

#### 8.B.I Anomaly detection as an ML problem: unsupervised, semi-supervised, and supervised families [/anomaly-ml-families]
> *Scholar query: How is anomaly detection framed as a machine learning problem, and what are the structural differences between unsupervised, semi-supervised, and supervised approaches? I am looking for survey or overview literature that explains when each family is appropriate — particularly the case for unsupervised methods when labeled anomaly examples are unavailable, as is typical in personal finance contexts where individual users cannot be expected to annotate their own abnormal transactions.*

#### 8.B.II Candidate anomaly detection algorithms for personal spending data [/anomaly-algo-candidates]
> *Scholar query: What anomaly detection algorithms have been applied to personal finance or financial transaction data, and what results have they produced? I am looking for comparative or applied studies that implement methods such as Isolation Forest, One-Class SVM, Local Outlier Factor, statistical threshold models, or autoencoder-based detection on personal spending records — reporting detection accuracy, false positive rates, and practical suitability for real-world financial monitoring.*

#### 8.B.III Per-user baseline learning without labeled training data [/anomaly-unsupervised-baseline]
> *Scholar query: How do unsupervised anomaly detection algorithms learn a normal baseline for each individual user without requiring labeled training examples, and what mechanisms make this per-user calibration robust to behavioral variation? I am looking for foundational and applied literature that explains isolation-based, density-based, and reconstruction-based approaches to individual baseline modeling — particularly in settings where the definition of normal behavior is user-specific and cannot be predetermined.*

#### 8.B.IV Tradeoffs across candidate algorithms: false positive control, explainability, and mobile feasibility [/anomaly-algo-tradeoffs]
> *Scholar query: What are the tradeoffs among candidate anomaly detection algorithms for personal finance applications — particularly with respect to control of the false positive rate to avoid unnecessary user alerts, the ability to explain flagged anomalies in user-facing language, and computational feasibility on mobile hardware? I am looking for research that evaluates these dimensions for methods such as Isolation Forest, One-Class SVM, and autoencoder-based approaches in financial or resource-constrained contexts.*

#### 8.B.V Evaluation metrics for anomaly detection: accuracy, precision, recall, and F1-score [/anomaly-eval-metrics]
> *Scholar query: What evaluation metrics are most appropriate for assessing the performance of an anomaly detection model in a personal finance context — specifically the interpretation and application of accuracy, precision, recall, and F1-score when anomalous spending events are rare relative to normal transactions? I am looking for research that addresses class imbalance in anomaly evaluation and justifies the preference for recall-oriented metrics in contexts where missing a genuine overage carries higher cost than a false alert.*

---

## 9. Mobile-First Design [/mobile-first]

### 9.A Mobile-First Design Principles and Rationale [/mobile-first-rationale]

#### 9.A.I Definition and distinction: mobile-first versus desktop-first design in PFMS [/mobile-first-def]
> *Scholar query: How is mobile-first design defined and distinguished from desktop-first design in the context of personal finance management systems? I am looking for research that articulates the architectural, UX, and technical differences between systems designed primarily for mobile versus those ported from desktop, and what implications this design philosophy has for feature prioritization, usability, and adoption.*

#### 9.A.II Mobile penetration and financial exclusion as the empirical basis for mobile-first deployment [/mobile-penetration-rationale]
> *Scholar query: What evidence of mobile device penetration and limited banking infrastructure in the Philippines supports the case for mobile-first deployment of a personal finance management application? I am looking for national survey data or institutional reports that document smartphone ownership rates, mobile internet access, and the asymmetry between mobile penetration and formal financial account ownership — particularly for young professionals in Metro Manila.*

#### 9.A.III Technical constraints: compute, connectivity, screen size, and battery life [/mobile-technical-constraints]
> *Scholar query: What technical constraints do mobile platforms impose on the deployment of personal finance applications that incorporate machine learning components? I am looking for research that characterizes the limitations of mobile devices — including limited computational power, variable or intermittent network connectivity, small screen real estate, and battery drain — and how these constraints shape the design and capability of intelligent mobile applications.*

---

### 9.B Mobile UX Design for Personal Finance [/mobile-ux-design]

#### 9.B.I UX patterns that minimize manual transaction entry burden [/mobile-ux-entry]
> *Scholar query: What mobile user experience design patterns are most effective at reducing the friction and cognitive burden of manual transaction data entry in personal finance applications? I am looking for research that evaluates specific design interventions — such as quick-entry modals, smart defaults, category prediction, or streamlined input flows — that demonstrably reduce the effort required for users to log financial transactions consistently.*

#### 9.B.II Glanceable visualizations and dashboard design for financial data on small screens [/mobile-dashboard-design]
> *Scholar query: What design principles govern the presentation of personal financial data — such as spending summaries, budget progress, and forecast displays — on small mobile screens? I am looking for research on glanceable visualization design, information hierarchy for financial dashboards, and the tradeoffs between data density and legibility in mobile personal finance interfaces.*

#### 9.B.III Offline resilience and data synchronization in mobile financial applications [/mobile-offline-sync]
> *Scholar query: How is offline resilience implemented in mobile financial applications, and what synchronization strategies are used to reconcile locally stored data with a remote database when connectivity is restored? I am looking for research or system design literature that evaluates the technical approaches to offline-capable mobile finance apps — including local caching, conflict resolution, and the user experience implications of intermittent connectivity.*

---

## 10. Data Privacy, Security, and User Trust [/privacy-security]

### 10.A Data Privacy and Security in Personal Finance Systems [/privacy-security-domain]

#### 10.A.I Sensitivity classification of personal financial data and associated privacy risks [/data-sensitivity]
> *Scholar query: How is personal financial data classified in terms of sensitivity and privacy risk in the research literature? I am looking for studies that characterize individual-level transaction records, income data, and spending patterns as particularly sensitive personal information — discussing the harms that can follow from unauthorized access or misuse, and situating this classification within broader frameworks for categorizing personal data by risk level.*

#### 10.A.II Technical security standards for mobile financial application data handling [/security-standards]
> *Scholar query: What technical security standards and best practices apply to mobile personal finance application data handling — including encryption at rest and in transit, authentication and access control mechanisms, and data minimization principles? I am looking for literature that describes industry or research-level security requirements for mobile financial applications handling sensitive personal transaction data.*

#### 10.A.III Philippine regulatory framework: RA 10173 and NPC issuances applicable to a PFMS [/ph-privacy-law]
> *Scholar query: What is the Philippine regulatory framework governing the collection, storage, and processing of personal financial data in mobile applications — specifically the Data Privacy Act of 2012 (Republic Act 10173) and relevant National Privacy Commission issuances? I am looking for legal or compliance literature that describes how these regulations apply to a locally developed personal finance management system and what obligations they impose on the developer.*

#### 10.A.IV Privacy-by-design principles applied in financial system research [/privacy-by-design]
> *Scholar query: How have privacy-by-design principles been applied in the design and development of personal finance or financial management systems? I am looking for studies that describe specific implementation strategies — such as data minimization, purpose limitation, user consent management, and on-device processing — that embed privacy protection into the system architecture, with attention to how these principles are operationalized in mobile financial applications.*

---

### 10.B User Trust in Personal Finance Systems [/user-trust-domain]

#### 10.B.I User trust in personal finance applications and its effect on data-sharing and logging behavior [/user-trust-behavior]
> *Scholar query: How does user trust in a personal finance application affect their willingness to share financial data and maintain consistent transaction logging behavior? I am looking for empirical studies that measure the relationship between perceived trustworthiness — including privacy policy clarity, data security assurances, and brand reputation — and users' actual data-sharing behavior in PFMS applications.*

#### 10.B.II Explainability of algorithmic outputs as a trust-building mechanism [/explainability-trust]
> *Scholar query: How does the explainability of algorithmic outputs — such as budget recommendations, spending forecasts, and anomaly alerts — affect user trust in personal finance applications? I am looking for research that measures the relationship between the provision of explanations for system-generated advice and users' trust, acceptance, and adherence to that advice — including studies where explanation backfired or decreased trust.*

#### 10.B.III Privacy concern as a driver of inconsistent or withheld transaction logging [/privacy-logging-behavior]
> *Scholar query: Is there evidence that privacy concern drives users to withhold or inconsistently log transactions in personal finance applications? I am looking for research that documents the relationship between perceived data sensitivity and logging completeness, and that discusses how privacy anxiety leads to gaps in the transaction record that degrade ML-driven personalization and forecasting.*

---

## 11. User Retention and Engagement [/retention]

### 11.A Engagement Dynamics in Personal Finance Applications [/engagement-dynamics]

#### 11.A.I Relationship between transaction data completeness and downstream ML model performance [/data-completeness-ml]
> *Scholar query: How does the completeness and consistency of user-logged transaction data affect the performance of downstream machine learning models — such as spending forecasting and anomaly detection — in personal finance systems? I am looking for research that quantifies the degradation in model accuracy caused by gaps or inconsistent logging, and that identifies the minimum data completeness threshold required for ML modules to produce reliable outputs.*

#### 11.A.II Drop-off patterns in personal finance apps: when users stop logging and why [/drop-off-patterns]
> *Scholar query: What are the documented drop-off and attrition patterns in personal finance applications — specifically, at what point in their usage journey users stop logging transactions, and what factors predict early abandonment? I am looking for longitudinal studies or user behavior analyses that track when engagement falls off and identify the motivational or usability triggers that cause users to stop maintaining their financial records.*

#### 11.A.III Manual data entry as the primary engagement friction point in PFMS [/entry-friction]
> *Scholar query: Is manual transaction data entry the primary source of engagement friction and user abandonment in personal finance management systems? I am looking for usability research and user studies that identify data entry burden as the dominant barrier to sustained engagement and that measure its specific contribution to drop-off rates relative to other friction sources.*

---

### 11.B Retention Mechanisms and Engagement Design [/retention-mechanisms-design]

#### 11.B.I Non-gamification retention mechanisms: smart notifications, frictionless input, and value feedback loops [/retention-mechanisms]
> *Scholar query: What retention mechanisms in personal finance applications are effective at sustaining user engagement without relying on gamification — specifically well-timed smart notifications, minimized input friction, and value-feedback loops showing users the benefits of their logged data? I am looking for evidence-based research that evaluates these non-gamification approaches in terms of their effect on long-term retention and logging consistency.*

#### 11.B.II Demonstrated system value as an intrinsic retention driver [/value-driven-retention]
> *Scholar query: Does demonstrated system value — such as accurate spending forecasts, useful budget recommendations, or actionable anomaly alerts — function as an intrinsic retention driver in personal finance applications? I am looking for research that connects the perceived accuracy and usefulness of intelligent PFMS outputs to user motivation to continue logging, and that frames value delivery rather than incentive design as the primary mechanism for long-term retention.*

#### 11.B.III Goal-setting features and progress visualization as engagement mechanisms [/goal-engagement]
> *Scholar query: How do goal-setting features and visual representations of progress toward financial goals — such as savings trackers or debt repayment progress bars — function as engagement mechanisms in personal finance applications? I am looking for research that measures the effect of goal progress visualization on sustained app usage, logging frequency, and financial behavior outcomes.*

---

## 12. System Evaluation [/system-eval]

### 12.A Evaluation Frameworks for Personal Finance Systems [/eval-frameworks]

#### 12.A.I Evaluation frameworks, metrics, and methodologies documented for PFMS and PBMS [/eval-frameworks-survey]
> *Scholar query: What evaluation frameworks, metrics, and methodologies have been documented for assessing the quality of personal finance management and personal budget management systems? I am looking for literature that surveys how PFMS tools are formally evaluated — including functional accuracy testing, user satisfaction measurement, usability assessment, and behavioral outcome tracking — and that identifies which approaches are most appropriate for systems combining intelligent modules with user-facing interfaces.*

#### 12.A.II ISO/IEC 25010:2023 quality characteristics and their application to a PFMS [/iso-25010]
> *Scholar query: How are the quality characteristics defined in ISO/IEC 25010:2023 — including functional suitability, performance efficiency, usability, reliability, security, and portability — applied to the evaluation of a software system such as a personal finance management application? I am looking for research that operationalizes these quality characteristics into measurable evaluation criteria for a PFMS context.*

#### 12.A.III System Usability Scale: instrument design, scoring, administration, and benchmarks [/sus]
> *Scholar query: What is the design, scoring methodology, administration procedure, and intended scope of the System Usability Scale as a usability evaluation instrument? I am looking for foundational and applied literature that explains the SUS questionnaire structure, how the ten-item scale is scored, what benchmarks exist for interpreting that score, and what types of systems the instrument is appropriately applied to.*

#### 12.A.IV Combining ISO 25010 and SUS as a joint evaluation framework [/iso-sus-combined]
> *Scholar query: Is there research that proposes or implements a combined evaluation framework using both ISO/IEC 25010 and the System Usability Scale? I am looking for studies that use these instruments jointly — describing how they complement each other and how their results are integrated into a coherent evaluation methodology for intelligent software systems.*

#### 12.A.V ISO 25010 and SUS applied in PFMS or comparable financial application evaluations [/eval-pfms-applied]
> *Scholar query: What examples exist of ISO/IEC 25010 and the System Usability Scale being applied to evaluate personal finance management systems or comparable financial applications? I am looking for applied evaluation studies that report how quality characteristics were operationalized, what SUS scores were obtained, and how the findings supported conclusions about system fitness for purpose.*

---

### 12.B Evaluation of Algorithmic Modules [/eval-algo-modules]

#### 12.B.I Evaluation design for ML modules in intelligent PFMS: walk-forward validation and out-of-sample testing [/eval-ml-design]
> *Scholar query: What evaluation design principles apply specifically to machine learning modules embedded in personal finance systems — particularly the use of walk-forward validation rather than k-fold cross-validation for time-series forecasting, and out-of-sample testing across different user cohorts for classification and anomaly detection? I am looking for research that discusses why standard ML evaluation protocols must be adapted for temporal financial data and user-heterogeneous deployments.*

#### 12.B.II Acknowledged limitations of ISO 25010 and SUS for evaluating intelligent system components [/eval-limitations]
> *Scholar query: What are the acknowledged limitations of ISO/IEC 25010 and the System Usability Scale as evaluation instruments when applied to systems with intelligent or ML-driven components? I am looking for critical literature that identifies where these frameworks fall short — such as the absence of coverage for adaptive behavior, AI explainability, or algorithmic fairness — and what supplementary evaluation approaches are recommended.*

#### 12.B.III Sample size and respondent profile guidelines for SUS-based evaluations [/sus-sample-size]
> *Scholar query: What sample size and respondent profile recommendations exist for conducting a valid SUS-based usability evaluation, and what sample sizes do comparable studies use in practice? I am looking for research on the statistical properties of SUS that inform minimum sample size decisions and the sample sizes reported in published SUS evaluations of mobile or personal finance applications.*

---

*Topics marked with discussion-pending items are flagged for advisor and panel review before the corresponding RRL section is finalized.*