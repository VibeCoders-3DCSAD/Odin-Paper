[WARNING]: Outdated.

# Topic Outline [/odin-outline]

## Development of Odin: A Personal Budget Management System Using LSTM, Classification Algorithm, and Recommendation Algorithm

---

> **How to read this document**
> `[/shorthand]` tags appear beside every node — use them as folder names or paper-tracking IDs.
> Each lettered topic (A–J) is a major conceptual territory the thesis must cover.
> Each numbered subtopic is a research area within that territory (maps to an RRL topic).
> Each bulleted sub-subtopic is a specific claim the literature must establish.
> The *Scholar query* below each bullet is ready to paste into Google Scholar Labs.

---

## A. Target Users and the Financial Problem [/target-users]

### A.1 Spending and Budgeting Behavior of Filipino Young Professionals [/fil-spending-behavior]

- Income structure typology: salaried, freelance, informal, and mixed-income earners [/income-typology]
  > *Scholar query: income structure classification Filipino young professionals salaried freelance informal gig economy personal finance Philippines*

- Budgeting time horizons: weekly, semi-monthly, and monthly cycles among Filipino young adults [/budget-time-horizons]
  > *Scholar query: budgeting time horizon frequency weekly monthly Filipino young adults personal finance planning behavior*

- Documented expenditure patterns disaggregated by income stability type [/expenditure-patterns]
  > *Scholar query: household expenditure patterns income stability type regular irregular Filipino young professionals spending allocation*

- Prevalence of budgeting practice and methods used in this demographic [/budgeting-prevalence]
  > *Scholar query: budgeting behavior prevalence methods Filipino millennials Gen Z personal finance habits financial planning practice*

- Failure points: irregular tracking, impulse overspending, unplanned obligatory expenses [/budget-failure-points]
  > *Scholar query: personal finance management failure irregular transaction tracking overspending unplanned expenses Filipino young adults challenges*

- Financial behavior differences across income stability types: stable vs. variable earners [/income-type-behavior-diff]
  > *Scholar query: financial management behavior differences stable variable irregular income earners Philippines young professionals comparison*

- Culturally specific financial behaviors: remittances, paluwagan, religious and social contributions, family obligations, holidays, school enrollment [/cultural-obligations]
  > *Scholar query: paluwagan rotating savings credit association remittances religious social family financial obligations holiday seasons school enrollment Filipino cultural spending behavior*

- Case that intelligent adaptive budgeting tools outperform financial literacy-only interventions [/intelligent-vs-literacy]
  > *Scholar query: intelligent budgeting system tool effectiveness versus financial literacy intervention behavioral change personal finance young adults*

---

### A.2 Existing Personal Finance and Budget Management Systems [/existing-pfms]

- Classification and typology of PFMS and PBMS documented in literature [/pfms-typology]
  > *Scholar query: personal finance management system budget management application typology classification features literature review 2023 2024*

- Feature sets of existing systems and evidence of their effectiveness [/pfms-features]
  > *Scholar query: personal budget management system dominant features user effectiveness evaluation systematic review*

- Documented limitations: manual entry burden, no forecasting, no anomaly detection, generic categories [/pfms-limitations]
  > *Scholar query: personal finance application limitations manual data entry lack forecasting anomaly detection generic expense categories usability*

- Budget recommendation approaches implemented in existing systems [/pfms-budget-rec]
  > *Scholar query: budget recommendation approach rule-based algorithmic implemented existing personal finance management system*

- Budgeting strategies technically implemented in existing systems [/pfms-strategies-impl]
  > *Scholar query: budgeting strategies zero-based envelope 50-30-20 pay yourself first technically implemented personal finance app*

- Gap between existing systems and an intelligent, adaptive, locally grounded system for Filipino users [/pfms-gap]
  > *Scholar query: gap limitations existing personal finance system intelligent adaptive localized Philippine Filipino context young professionals*

---

## *B. Mobile-First Design and Deployment Constraints [/mobile-first]

### B.1 Mobile-First Design in Personal Finance Systems [/mobile-pfms-design]

- Definition and distinction: mobile-first vs. desktop-first design in PFMS [/mobile-first-def]
  > *Scholar query: mobile-first design approach definition personal finance management system versus desktop-first application architecture*

- Evidence of mobile-first dominance among younger users in Southeast Asian and emerging markets [/mobile-dominance]
  > *Scholar query: mobile-first personal finance application adoption younger users Southeast Asia Philippines emerging market dominance evidence*

- Technical constraints on mobile platforms: compute, network connectivity, screen, battery life [/mobile-constraints]
  > *Scholar query: mobile application technical constraints limited computational resources network bandwidth battery personal finance machine learning deployment*

- Influence of mobile deployment constraints on ML algorithm selection for embedded modules [/mobile-ml-algo-selection]
  > *Scholar query: machine learning algorithm selection mobile deployment constraints lightweight inference model size forecasting anomaly detection personal finance*

- Mobile UX patterns that minimize transaction data entry burden [/mobile-ux-entry]
  > *Scholar query: mobile user experience design minimize transaction data entry burden personal finance app input friction reduction*

---

## C. Budget Recommendation Theory and Algorithm [/budget-rec]

### C.1 Budgeting Strategies and Budget Recommendation [/budgeting-strategies]

- Core mechanics and structure of documented budgeting strategies [/strategy-mechanics]
  > *Scholar query: budgeting strategies core mechanics zero-based budgeting envelope method pay yourself first proportional allocation comparison personal finance*

- Comparative strengths and weaknesses of each strategy across income stability types [/strategy-income-fit]
  > *Scholar query: budgeting strategy effectiveness comparison stable variable irregular income type strengths weaknesses salaried freelance personal finance*

- Multi-strategy distillation: combining elements into one unified system-level configuration [/strategy-distillation]
  > *Scholar query: hybrid budgeting strategy distillation unified system configuration combining multiple approaches personal finance implementation*

- Technical implementation of budget recommendation in existing PFMS [/budget-rec-existing]
  > *Scholar query: budget recommendation technical implementation existing personal finance management system rule-based algorithmic user configured*

- Algorithmic approaches to budget recommendation: constraint optimization, MCDM, RL, collaborative filtering [/budget-rec-algorithms]
  > *Scholar query: budget recommendation algorithm constraint optimization multi-criteria decision making reinforcement learning collaborative filtering personal finance*

- Budget period surplus: reset vs. carryforward logic by income type [/surplus-logic]
  > *Scholar query: budget surplus handling carryforward reset period income type variable stable personal finance application design*

- Budget recommendation behavior under lump-sum, delayed, or absent income [/lump-sum-income]
  > *Scholar query: budget recommendation lump-sum delayed irregular absent income handling cold-start personal finance system design*

- Minimum user input threshold for generating a useful budget recommendation [/min-user-input]
  > *Scholar query: minimum user input requirements budget recommendation accuracy tradeoff intelligent personal finance system cold-start onboarding*

---

### C.2 Budget Recommendation Algorithm [/budget-rec-algo]

- Problem formulation: resource allocation, optimization, ranking, or hybrid recommendation [/budget-rec-formulation]
  > *Scholar query: budget recommendation problem formulation resource allocation optimization ranking prediction hybrid personal finance algorithm literature*

- Algorithmic solutions applied to budget distribution and financial resource allocation [/budget-alloc-algos]
  > *Scholar query: resource allocation budget distribution financial planning algorithm linear programming multi-objective optimization literature results*

- Algorithm applications specifically within PFMS and PBMS contexts [/budget-algo-pfms]
  > *Scholar query: budget recommendation algorithm applied personal finance budget management system context evaluation results literature 2023 2024 2025*

- Tradeoffs: mobile feasibility, user-facing explainability, adaptability, cold-start performance [/budget-algo-tradeoffs]
  > *Scholar query: budget recommendation algorithm tradeoffs explainability mobile feasibility cold-start adaptability comparison personal finance evaluation*

- Justification of the chosen algorithm over alternatives for Odin's context and constraints [/budget-algo-justification]
  > *Scholar query: budget recommendation algorithm selection justification comparison alternatives mobile personal finance Filipino young professionals context*

---

## D. Spending Forecasting [/forecasting]

### D.1 Predictive Modeling in Personal Finance Systems [/predictive-modeling-pfms]

- Survey of forecasting methods applied to personal spending data [/forecasting-methods]
  > *Scholar query: forecasting methods comparison ARIMA LSTM XGBoost Random Forest personal finance household spending prediction accuracy*

- Characterization of personal finance transaction data as sequential time-series [/spending-time-series]
  > *Scholar query: personal finance transaction data time-series sequential structure characterization temporal properties spending behavior*

- Evidence of temporal dependency in spending: prior periods predict subsequent periods [/temporal-dependency]
  > *Scholar query: temporal dependency autocorrelation spending behavior prior period prediction personal finance sequential influence evidence*

- Interaction between mobile constraints and the practical choice of forecasting algorithm [/mobile-forecast-tradeoff]
  > *Scholar query: forecasting algorithm selection mobile deployment constraints lightweight model personal finance inference time memory footprint*

- Cold-start fallback strategies for forecasting without sufficient transaction history [/forecast-cold-start]
  > *Scholar query: cold-start forecasting fallback strategy insufficient transaction history personal finance new user population average prior*

- Per-category spending forecasting across multiple simultaneous expense categories [/per-category-forecast]
  > *Scholar query: per-category spending forecast multiple simultaneous expense categories personal finance multi-output model household expenditure*

---

### D.2 LSTM as the Spending Forecasting Algorithm [/lstm]

- LSTM architecture: gates, cell state, and the class of sequential problems it solves [/lstm-architecture]
  > *Scholar query: LSTM long short-term memory architecture input forget output gate cell state sequential dependency time-series overview*

- Comparative performance of LSTM vs. ARIMA, XGBoost, GRU, and Transformer on time-series tasks [/lstm-vs-alternatives]
  > *Scholar query: LSTM versus ARIMA XGBoost GRU Transformer time-series forecasting comparison performance accuracy benchmark*

- LSTM applied to household expenditure, consumption, and personal spending data [/lstm-spending-applied]
  > *Scholar query: LSTM applied household expenditure personal spending consumption forecasting personal finance budget prediction results*

- LSTM for simultaneous multi-output, multi-category forecasting [/lstm-multi-output]
  > *Scholar query: LSTM multi-output simultaneous multi-category forecasting spending expense categories household personal finance model*

- LSTM feasibility under mobile and resource-constrained deployment [/lstm-mobile]
  > *Scholar query: LSTM mobile deployment resource-constrained lightweight model compression quantization pruning inference optimization embedded*

- Justification of LSTM over surveyed alternatives given Odin's data characteristics and context [/lstm-justification]
  > *Scholar query: LSTM justified selection personal finance sequential spending Filipino mobile deployment temporal dependency comparison alternatives*

---

## E. Anomaly and Overage Detection [/anomaly-detection]

### E.1 Anomaly Detection in Personal Finance Systems [/anomaly-pfms-domain]

- Definition and taxonomy of financial anomalies detectable in personal spending data [/anomaly-taxonomy]
  > *Scholar query: financial anomaly definition taxonomy types personal spending transaction data detectable categories classification*

- Threshold-based overage alerting vs. behavioral baseline deviation: distinction and scope [/overage-vs-behavioral]
  > *Scholar query: threshold budget overage alert versus behavioral baseline deviation anomaly detection personal finance distinction scope design*

- Detection approaches applied to personal finance data and their reported results [/anomaly-approaches]
  > *Scholar query: anomaly detection approaches personal finance transaction data Isolation Forest One-Class SVM rule-based statistical results comparison*

- Tradeoffs between rule-based and algorithmic detection: complexity, explainability, accuracy [/anomaly-tradeoffs]
  > *Scholar query: rule-based versus algorithmic anomaly detection personal finance explainability accuracy complexity false positive rate tradeoff*

- Anomaly detection output feeding forward into next budget recommendation cycle [/anomaly-feedback]
  > *Scholar query: anomaly detection feedback loop budget recommendation adjustment next cycle personal finance management system documented*

- Filipino culturally specific high-value spending recognized as expected, not anomalous [/cultural-spending-protection]
  > *Scholar query: culturally specific spending Filipino paluwagan remittances religious festival protected category anomaly detection exclusion design*

- Alert design: frequency, format, and framing to minimize alert fatigue while ensuring action [/alert-design]
  > *Scholar query: anomaly alert design frequency format framing user experience alert fatigue minimization personal finance mobile application*

---

### E.2 Anomaly Detection Algorithm [/anomaly-algo]

- Anomaly detection as an ML problem: unsupervised, semi-supervised, and supervised families [/anomaly-ml-families]
  > *Scholar query: anomaly detection machine learning families unsupervised semi-supervised supervised approaches comparison overview personal finance transactions*

- Isolation Forest: mechanism, per-user baseline learning without labeled training data [/isolation-forest]
  > *Scholar query: Isolation Forest algorithm mechanism unsupervised per-user baseline anomaly detection without labeled training data overview*

- Isolation Forest applied to personal financial transaction and spending data [/isolation-forest-applied]
  > *Scholar query: Isolation Forest applied personal finance financial transaction spending anomaly detection results evaluation*

- Tradeoffs: mobile feasibility, false positive control, and user-facing explainability [/anomaly-algo-tradeoffs]
  > *Scholar query: Isolation Forest mobile deployment feasibility false positive rate control explainability personal finance user-facing comparison*

- Justification of chosen anomaly detection approach over alternatives for Odin [/anomaly-algo-justification]
  > *Scholar query: anomaly detection algorithm selection justification Isolation Forest alternatives personal finance mobile behavioral Filipino context*

---

## F. User Profiling and Classification [/user-profiling]

### F.1 User Behavioral Profiling in Filipino Personal Finance Contexts [/fil-profiling-domain]

- Role of user profiling in budget recommendation, forecasting fallback, and system personalization [/profiling-role]
  > *Scholar query: user behavioral profiling role budget recommendation forecasting fallback personalization personal finance management system*

- Inadequacy of Western financial behavioral taxonomies for Filipino user contexts [/western-taxonomy-gap]
  > *Scholar query: Western financial behavioral taxonomy profile inadequacy Filipino Southeast Asian cultural differences personal finance context*

- Filipino-specific financial behavioral patterns documented in BSP CFS and FIES data [/fil-behavioral-patterns]
  > *Scholar query: Filipino financial behavior patterns spending saving obligations BSP Consumer Finance Survey FIES PSA data institutional*

- Constructing locally grounded financial profiles from Philippine institutional datasets [/fil-profile-construction]
  > *Scholar query: Filipino financial profile construction behavioral archetypes segments FIES BSP CFS data-driven local context*

- Behavioral dimensions as meaningful profile differentiators: income stability, obligation weight, savings disposition [/profile-dimensions]
  > *Scholar query: behavioral dimensions financial user profile income stability obligation weight savings flexibility disposition differentiators*

- Concept drift as a framework for progressive user profile updates over time [/concept-drift]
  > *Scholar query: concept drift adaptive user behavioral modeling profile update progressive personal finance system learning over time*

- Behavioral signals that should trigger profile reassessment [/profile-triggers]
  > *Scholar query: behavioral signals trigger profile reassessment income change spending shift obligation increase personal finance adaptive system*

- Automatic system-initiated vs. user-confirmed profile update mechanisms [/profile-update-mechanism]
  > *Scholar query: automatic versus user-confirmed profile update mechanism behavioral system design personal finance reclassification transparency*

- Cold-start problem and profile-average fallback for new users without behavioral history [/profiling-cold-start]
  > *Scholar query: cold-start personalized financial system new user profile-average population prior fallback approaches documented personal finance*

---

### F.2 Profile Classification Algorithm [/profile-classification-algo]

- Supervised classification vs. clustering for predefined profile categories [/classification-vs-clustering]
  > *Scholar query: supervised classification versus clustering predefined categories financial user profiling comparison suitability fixed profiles*

- Classification algorithms documented for behavioral and financial user profiling [/classifier-candidates]
  > *Scholar query: classification algorithm behavioral financial user profiling logistic regression SVM Random Forest neural network comparison results*

- Feature selection: onboarding questionnaire responses vs. early transaction behavioral data [/classifier-features]
  > *Scholar query: feature selection financial user profiling onboarding questionnaire transaction history classification input behavioral data*

- Cold-start classification: initial model training without labeled real user data [/classifier-cold-start]
  > *Scholar query: classification cold-start training without labeled real user data synthetic data augmentation financial profiling initial deployment*

- Progressive reclassification: periodic batch, continuous, or drift-triggered profile updates [/progressive-reclassification]
  > *Scholar query: progressive reclassification user profile update strategies periodic continuous drift-triggered behavioral change personal finance*

- Tradeoffs across candidate classifiers: predictive accuracy, interpretability, mobile feasibility [/classifier-tradeoffs]
  > *Scholar query: classification algorithm tradeoff predictive accuracy interpretability explainability mobile deployment feasibility comparison personal finance*

- Justification of the chosen classifier for Odin's four-profile structure and use context [/classifier-justification]
  > *Scholar query: financial user profile classifier justification four-class predefined Filipino mobile personal finance system selection comparison*

---

## G. Expense Categorization [/expense-categories]

### G.1 Expense Categorization in Filipino Personal Finance Contexts [/expense-cat-domain]

- Approaches to expense categorization: user-defined, institutionally derived, ML-generated, hybrid [/cat-approaches]
  > *Scholar query: expense transaction categorization approaches user-defined institutional machine learning hybrid personal finance system comparison*

- Limitations of Western expense category schemas for Filipino spending contexts [/western-cat-limitations]
  > *Scholar query: Western expense category schema limitations Filipino Southeast Asian spending context personal finance inadequacy cultural mismatch*

- PSA FIES and BSP CFS expenditure categories and their mapping to a local PFMS [/fies-bsp-mapping]
  > *Scholar query: PSA Family Income Expenditure Survey FIES BSP Consumer Finance Survey expenditure categories Filipino personal finance system mapping*

- Cultural expense types warranting dedicated categories: paluwagan, remittances, religious obligations [/cultural-expense-types]
  > *Scholar query: paluwagan remittances religious social obligations dedicated expense category personal finance Filipino cultural spending literature*

- Institutional basis for protected expense categories and minimum spending floors [/protected-categories]
  > *Scholar query: protected expense categories minimum spending floor essential non-negotiable BSP institutional basis personal finance system design*

- Expense category design in existing PFMS explicitly serving Filipino users [/fil-pfms-categories]
  > *Scholar query: expense category design Filipino-specific personal finance application local versus Western categories user-centered design*

- SSS and Pag-IBIG contributions: automatic deductions for employees vs. voluntary entries for variable-income users [/sss-pagibig]
  > *Scholar query: SSS Pag-IBIG PhilHealth contribution classification automatic deduction regular employee voluntary freelance self-employed personal finance categorization*

---

## *H. Data Privacy, Security, and User Trust [/privacy-security]

### H.1 Data Privacy, Security, and User Trust in Personal Finance Systems [/privacy-pfms-domain]

- Sensitivity classification of personal financial data in literature [/data-sensitivity]
  > *Scholar query: personal financial data sensitivity classification privacy personal information legal protection literature personal finance application*

- Technical security standards for financial application data handling [/security-standards]
  > *Scholar query: financial application security standards encryption authentication data minimization access control personal finance best practices*

- User trust in personal finance applications and its effect on data-sharing and logging behavior [/user-trust]
  > *Scholar query: user trust personal finance mobile application data sharing transaction logging behavior design factors determinants*

- Privacy concern as a driver of inconsistent or withheld transaction logging [/privacy-logging]
  > *Scholar query: privacy concern financial data withholding incomplete transaction logging personal finance application user behavior retention*

- Philippine regulatory framework: RA 10173, BSP data governance guidelines, NPC issuances [/ph-privacy-law]
  > *Scholar query: Republic Act 10173 Data Privacy Act Philippines BSP NPC financial data governance compliance personal finance application*

- Privacy-by-design principles applied in comparable financial system research [/privacy-by-design]
  > *Scholar query: privacy by design principles applied financial management system personal finance data protection research implementation*

- Privacy implications specific to manual self-reported financial data without banking API integration [/manual-data-privacy]
  > *Scholar query: self-reported manual financial data privacy implications no banking integration personal finance application design*

---

## I. User Retention and Engagement [/retention]

### I.1 User Retention and Engagement in Personal Finance Systems [/retention-pfms-domain]

- Relationship between transaction data completeness and downstream ML model performance [/data-completeness-ml]
  > *Scholar query: transaction data completeness logging consistency effect machine learning model performance personal finance forecasting anomaly detection*

- Drop-off patterns in personal finance apps: when users stop logging and why [/drop-off-patterns]
  > *Scholar query: user drop-off attrition retention personal finance application transaction logging cessation behavior patterns reasons*

- Manual data entry as the primary engagement friction point in PFMS [/entry-friction]
  > *Scholar query: manual transaction data entry friction primary engagement barrier personal finance application usability burden*

- Non-gamification retention mechanisms: smart notifications, frictionless input, feedback loops, goal-setting [/retention-mechanisms]
  > *Scholar query: non-gamification retention mechanisms personal finance app notifications frictionless input immediate value feedback goal setting effectiveness*

- Minimum viable interaction frequency for a personal finance app to deliver perceived value [/min-interaction-freq]
  > *Scholar query: minimum interaction frequency personal finance application engagement perceived usefulness value delivery threshold*

- Demonstrated system value — accurate forecasts, actionable alerts — as intrinsic retention driver [/value-driven-retention]
  > *Scholar query: perceived system value demonstrated accuracy forecast alert retention engagement personal finance intrinsic motivation driver*

---

## *J. System Evaluation [/system-eval]

### J.1 System Evaluation in Personal Finance and Budget Management Systems [/eval-pfms-domain]

- Evaluation frameworks, metrics, and methodologies documented for PFMS and PBMS [/eval-frameworks]
  > *Scholar query: personal finance budget management system evaluation framework metrics methodology literature review 2023 2024 2025*

- ISO/IEC 25010:2023 quality characteristics and their application to evaluating a PFMS [/iso-25010]
  > *Scholar query: ISO IEC 25010 2023 software product quality characteristics model evaluation application system study*

- System Usability Scale: instrument design, scoring, administration, and scope [/sus]
  > *Scholar query: System Usability Scale SUS instrument scoring administration reliability validity usability evaluation*

- SUS applied specifically to mobile-first applications [/sus-mobile]
  > *Scholar query: System Usability Scale SUS mobile application usability evaluation results benchmark score*

- Combining ISO 25010 and SUS as a joint evaluation framework [/iso-sus-combined]
  > *Scholar query: ISO 25010 SUS combined joint evaluation framework software system study implementation results*

- ISO 25010 and SUS applied in PFMS or comparable financial application evaluations [/eval-pfms-applied]
  > *Scholar query: ISO 25010 SUS applied personal finance budget management system evaluation study results comparable*

- Acknowledged limitations of SUS and ISO 25010 as evaluation instruments [/eval-limitations]
  > *Scholar query: System Usability Scale SUS ISO 25010 acknowledged limitations evaluation instrument scope validity critique*

- Sample size and respondent profile guidelines for SUS-based evaluations [/sus-sample-size]
  > *Scholar query: SUS System Usability Scale evaluation sample size respondent profile recommendation guidelines comparable study*

---

* Flagged; to be discussed further.