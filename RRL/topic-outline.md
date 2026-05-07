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
  > *Scholar query: How do researchers classify the income structures of young professionals in the Philippines, particularly the distinction between salaried, freelance, informal, and mixed or gig-economy earners? I am looking for studies that document the typology of income arrangements among Filipino workers in the millennial and Gen Z age range, and how these income types shape personal finance behavior and spending decisions.*

> NOTE: Appears to lack in pertaining to regular employees. May need to substantiate with pre-survey.

- Budgeting time horizons: weekly, semi-monthly, and monthly cycles among Filipino young adults [/budget-time-horizons]
  > *Scholar query: What budgeting time horizons — weekly, semi-monthly, or monthly cycles — do Filipino young adults actually use when planning their personal finances? I am looking for studies that document how the frequency of income receipt, such as semi-monthly payroll disbursements, shapes the temporal window within which Filipinos organize their budgets, and whether irregular income earners adopt different time horizons than salaried workers.*

- Documented expenditure patterns disaggregated by income stability type [/expenditure-patterns]
  > *Scholar query: What do empirical studies reveal about the household or personal expenditure patterns of Filipino young professionals when disaggregated by income stability type? I am looking for research that compares how workers with stable salaried income allocate spending across categories differently from those with irregular, freelance, or mixed income — including data from Philippine institutional sources such as FIES or BSP survey instruments.*

- Prevalence of budgeting practice and methods used in this demographic [/budgeting-prevalence]
  > *Scholar query: How prevalent is active budgeting practice among Filipino millennials and Gen Z, and what budgeting methods do they most commonly use? I am looking for studies that measure the proportion of Filipino young adults who maintain a budget, the formats or tools they use, and the behavioral or demographic factors that predict whether someone budgets at all — particularly in Metro Manila or urban Philippine settings.*

- Failure points: irregular tracking, impulse overspending, unplanned obligatory expenses [/budget-failure-points]
  > *Scholar query: What are the most commonly documented failure points in personal finance management among Filipino young adults? I am specifically interested in research that identifies irregular or inconsistent transaction tracking, impulse or unplanned overspending, and the destabilizing effect of sudden obligatory expenses — such as medical costs, family emergencies, or periodic lump-sum payments — as the primary reasons budgets break down in practice.*

- Financial behavior differences across income stability types: stable vs. variable earners [/income-type-behavior-diff]
  > *Scholar query: How do the financial management behaviors of Filipino workers with stable income differ from those with variable or irregular income? I am looking for comparative studies that show how income predictability affects budgeting discipline, savings rates, expense prioritization, and financial stress — particularly for young professionals in the Philippines who move between employment types or hold multiple income sources simultaneously.*

- Culturally specific financial behaviors: remittances, paluwagan, religious and social contributions, family obligations, holidays, school enrollment [/cultural-obligations]
  > *Scholar query: What culturally specific financial behaviors and obligations are documented among Filipino young adults that Western personal finance frameworks do not adequately account for? I am looking for studies covering practices such as paluwagan participation, regular family remittances, contributions to religious or community events, bayanihan-style financial support, and the financial impact of seasonal obligations like Christmas, school enrollment periods, and town fiestas — particularly how these affect cash flow patterns and budget adherence.*

> NOTE: Add this to the scope of the sub-subtopic:
> Data also includes spikes that are driven by Filipino cultural practices and events, such as:
> Petsa de Peligro: pre-payday spending suppression
> Payday spree: post-payday spending spike
> 13th month pay effect: bonus-driven December spending surge
> Christmas / Ber Months: September to December seasonal spending escalation
> Semana Santa / Holy Week spending: travel and leisure spike
> School enrollment season spending: school fees, uniforms, supplies spike
> Undas / All Saints’ Day spending: travel and reunion-related spike
> MMFF entertainment spike: post-Christmas cinema and leisure spending
> Paluwagan contribution cycle: periodic obligation-driven outflow
> Ambag contribution cycle: periodic shared-expense outflow
> Summer-related consumption spike
> et cetera.

- Case that intelligent adaptive budgeting tools outperform financial literacy-only interventions [/intelligent-vs-literacy]
  > *Scholar query: What evidence exists that intelligent or adaptive budgeting systems produce better financial behavior outcomes than financial literacy education alone? I am looking for studies that compare the effectiveness of tool-mediated interventions — such as automated tracking, personalized alerts, or algorithmic budget recommendations — against purely instructional or literacy-based approaches, particularly in populations of young adults where behavioral support matters more than knowledge transfer.*

---

### A.2 Existing Personal Finance and Budget Management Systems [/existing-pfms]

- Classification and typology of PFMS and PBMS documented in literature [/pfms-typology]
  > *Scholar query: How do recent studies classify and distinguish personal finance management systems and personal budget management systems? I am looking for literature that proposes or applies typologies of these tools — for example, distinguishing between expense tracking apps, budgeting planners, goal-setting tools, and hybrid systems — and that surveys the landscape of such applications with attention to their feature sets, technological approaches, and intended user bases.*

- Feature sets of existing systems and evidence of their effectiveness [/pfms-features]
  > *Scholar query: What are the dominant features found in personal budget management systems, and what evidence exists that these features actually improve users' financial outcomes? I am looking for evaluations or systematic reviews of PFMS applications that assess the impact of specific functionalities — such as transaction categorization, budget setting, visualization dashboards, or alerts — on user financial behavior, adherence to budgets, or savings outcomes.*

> NOTE: Continue here.

- Documented limitations: manual entry burden, no forecasting, no anomaly detection, generic categories [/pfms-limitations]
  > *Scholar query: What limitations of existing personal finance and budgeting applications are most consistently identified in research literature? I am specifically interested in studies that critique the usability cost of manual transaction entry, the absence of predictive or forecasting capabilities, the lack of anomaly or overspending detection, and the use of generic expense categories that do not reflect how actual users organize their spending.*

- Budget recommendation approaches implemented in existing systems [/pfms-budget-rec]
  > *Scholar query: What approaches to budget recommendation are currently implemented in personal finance management systems, as documented in research literature? I am looking for studies that describe how existing PFMS tools generate spending plans or budget allocations for users — whether through static rules, user-configured proportions, or more dynamic algorithmic methods — and what the known strengths and weaknesses of each approach are.*

- Budgeting strategies technically implemented in existing systems [/pfms-strategies-impl]
  > *Scholar query: Which established budgeting strategies — such as zero-based budgeting, the envelope method, the 50-30-20 rule, or pay-yourself-first — have been technically implemented within personal finance applications, as documented in the research literature? I am looking for studies or system descriptions that detail how these frameworks are operationalized computationally, what design decisions they require, and how well they transfer to digital implementation.*

- Gap between existing systems and an intelligent, adaptive, locally grounded system for Filipino users [/pfms-gap]
  > *Scholar query: What gap exists in the current landscape of personal finance management systems when evaluated against the needs of Filipino users, particularly young professionals with culturally specific financial obligations and variable income structures? I am looking for research that articulates why existing PFMS tools — typically designed for Western users or generic populations — fail to address local spending norms, income patterns, or the need for intelligent, adaptive, and context-aware budgeting support.*

---

## *B. Mobile-First Design and Deployment Constraints [/mobile-first]

### B.1 Mobile-First Design in Personal Finance Systems [/mobile-pfms-design]

- Definition and distinction: mobile-first vs. desktop-first design in PFMS [/mobile-first-def]
  > *Scholar query: How is mobile-first design defined and distinguished from desktop-first design in the context of personal finance management systems? I am looking for research that articulates the architectural, UX, and technical differences between systems designed primarily for mobile devices versus those ported from desktop, and what implications this design philosophy has for feature prioritization, usability, and adoption.*

- Evidence of mobile-first dominance among younger users in Southeast Asian and emerging markets [/mobile-dominance]
  > *Scholar query: What evidence exists that mobile-first personal finance applications dominate among younger users in Southeast Asia and other emerging markets, including the Philippines? I am looking for adoption studies, usage statistics, or market analyses that document the shift toward mobile as the primary interface for financial management among millennials and Gen Z in mobile-heavy economies where smartphone penetration precedes desktop adoption.*

- Technical constraints on mobile platforms: compute, network connectivity, screen, battery life [/mobile-constraints]
  > *Scholar query: What technical constraints do mobile platforms impose on the deployment of personal finance applications that incorporate machine learning components? I am looking for research that characterizes the limitations of mobile devices — including limited computational power, variable or intermittent network connectivity, small screen real estate, and battery drain concerns — and how these constraints shape the design and capability of intelligent mobile applications.*

- Influence of mobile deployment constraints on ML algorithm selection for embedded modules [/mobile-ml-algo-selection]
  > *Scholar query: How do mobile deployment constraints influence the selection of machine learning algorithms for embedded predictive or anomaly detection modules in mobile applications? I am looking for research that discusses the tradeoffs between model accuracy and inference efficiency, and that provides evidence or criteria for choosing lightweight algorithms suited to resource-constrained mobile environments over more computationally intensive alternatives.*

- Mobile UX patterns that minimize transaction data entry burden [/mobile-ux-entry]
  > *Scholar query: What mobile user experience design patterns are most effective at reducing the friction and cognitive burden of manual transaction data entry in personal finance applications? I am looking for research that evaluates specific design interventions — such as quick-entry modals, voice input, smart defaults, category prediction, or streamlined input flows — that demonstrably reduce the effort required for users to log financial transactions consistently.*

---

## C. Budget Recommendation Theory and Algorithm [/budget-rec]

### C.1 Budgeting Strategies and Budget Recommendation [/budgeting-strategies]

- Core mechanics and structure of documented budgeting strategies [/strategy-mechanics]
  > *Scholar query: What are the core mechanics and structural logic of the major budgeting strategies documented in personal finance literature? I am looking for studies or reviews that explain how strategies like zero-based budgeting, the envelope method, proportional allocation rules such as the 50-30-20 framework, and pay-yourself-first work as allocation systems — including how budget categories are defined, how income is divided, and what behaviors each strategy is designed to reinforce.*

- Comparative strengths and weaknesses of each strategy across income stability types [/strategy-income-fit]
  > *Scholar query: How do the strengths and weaknesses of major budgeting strategies compare when applied to users with different income stability profiles — particularly salaried versus freelance or irregular earners? I am looking for research that assesses which budgeting frameworks perform better for predictable monthly income versus lumpy, delayed, or variable cash flows, and what modifications or adaptations are recommended when applying standard strategies to non-salaried income earners.*

- Multi-strategy distillation: combining elements into one unified system-level configuration [/strategy-distillation]
  > *Scholar query: Is there research on distilling or combining elements from multiple budgeting strategies into a single unified system-level configuration? I am looking for work that proposes hybrid budgeting frameworks — for example, integrating protected essential spending floors from envelope budgeting with proportional allocation rules — or that discusses how a software system can synthesize multiple strategy principles into one coherent, user-facing budgeting engine.*

- Technical implementation of budget recommendation in existing PFMS [/budget-rec-existing]
  > *Scholar query: How is budget recommendation technically implemented in existing personal finance management systems? I am looking for research that describes the computational methods behind budget generation in PFMS tools — whether through hardcoded rules, user-configured templates, constraint-based allocation, or data-driven suggestion engines — and that evaluates the practical performance and usability of these approaches from a system design perspective.*

- Algorithmic approaches to budget recommendation: constraint optimization, MCDM, RL, collaborative filtering [/budget-rec-algorithms]
  > *Scholar query: What algorithmic approaches have been applied to the budget recommendation problem in personal finance research? I am looking for studies that implement or evaluate constraint optimization, multi-criteria decision making, reinforcement learning, or collaborative filtering as mechanisms for generating personalized budget allocations — with attention to how each approach handles user goals, competing spending priorities, income variation, and adaptability over time.*

- Budget period surplus: reset vs. carryforward logic by income type [/surplus-logic]
  > *Scholar query: How should a personal finance system handle budget surplus at the end of a budget period — should unspent funds reset to zero or carry forward to the next period? I am looking for research or system design literature that discusses this design decision, particularly in relation to income type: whether carryforward logic is more appropriate for variable income earners who may experience lean periods following flush ones, versus reset logic for stable salaried users.*

- Budget recommendation behavior under lump-sum, delayed, or absent income [/lump-sum-income]
  > *Scholar query: How should a budget recommendation system behave when a user receives income in a lump sum, receives it late, or does not receive it at all during a budget period? I am looking for research on handling non-standard income timing in personal finance systems, including cold-start scenarios where no income has been logged yet, and how algorithms or design rules can generate still-useful budget guidance under these conditions.*

- Minimum user input threshold for generating a useful budget recommendation [/min-user-input]
  > *Scholar query: What is the minimum amount of user-provided input required for a personal finance system to generate a budget recommendation that is meaningful and actionable? I am looking for research on the accuracy-input tradeoff in intelligent PFMS systems, particularly studies that evaluate how much transaction history, onboarding questionnaire data, or declared financial goals are needed before a recommendation engine can produce personalized output rather than a generic population average.*

---

### C.2 Budget Recommendation Algorithm [/budget-rec-algo]

- Problem formulation: resource allocation, optimization, ranking, or hybrid recommendation [/budget-rec-formulation]
  > *Scholar query: How is the budget recommendation problem formally framed in the research literature — as a resource allocation problem, a constrained optimization problem, a ranking task, or a hybrid recommendation problem? I am looking for work that explicitly characterizes the computational structure of budget generation, discusses the assumptions embedded in each framing, and evaluates how different problem formulations affect the tractability, explainability, and user-facing output of the recommendation system.*

- Algorithmic solutions applied to budget distribution and financial resource allocation [/budget-alloc-algos]
  > *Scholar query: What algorithmic solutions have been applied to the problem of distributing a limited financial resource across competing spending categories? I am looking for research on linear programming, multi-objective optimization, goal programming, and related techniques as applied to household or personal budget allocation — with attention to how constraints such as minimum essential spending, savings targets, and category caps are encoded and solved.*

- Algorithm applications specifically within PFMS and PBMS contexts [/budget-algo-pfms]
  > *Scholar query: What algorithms have been specifically applied to generate budget recommendations within personal finance management or personal budget management systems, as documented in recent research? I am looking for implementation studies or system papers that move beyond theoretical formulation and report real results from deploying recommendation algorithms in PFMS contexts — including how users responded to algorithmically generated budgets and how well those budgets performed in practice.*

- Tradeoffs: mobile feasibility, user-facing explainability, adaptability, cold-start performance [/budget-algo-tradeoffs]
  > *Scholar query: What are the key tradeoffs among candidate budget recommendation algorithms when evaluated along dimensions of mobile deployment feasibility, user-facing explainability, adaptability to changing user circumstances, and cold-start performance with limited historical data? I am looking for comparative studies or design analyses that assess these tradeoffs specifically in the context of personal finance systems serving users who may have variable income, limited transaction history, or low algorithmic literacy.*

- Justification of the chosen algorithm over alternatives for Odin's context and constraints [/budget-algo-justification]
  > *Scholar query: How do researchers justify the selection of a specific budget recommendation algorithm over its alternatives when building a personal finance system for a mobile-first, resource-constrained deployment targeting young professionals with variable income? I am looking for documented selection rationales that weigh accuracy, computational cost, cold-start behavior, and explainability — and that explicitly eliminate alternatives based on those criteria rather than simply choosing the most commonly cited method.*

---

## D. Spending Forecasting [/forecasting]

### D.1 Predictive Modeling in Personal Finance Systems [/predictive-modeling-pfms]

- Survey of forecasting methods applied to personal spending data [/forecasting-methods]
  > *Scholar query: What forecasting methods have been applied to personal spending or household expenditure data, and how do they compare in accuracy and practical suitability? I am looking for comparative studies that benchmark approaches such as ARIMA, LSTM, XGBoost, Random Forest, and other time-series or regression models against personal finance or consumer spending datasets — with attention to which methods handle irregular spending patterns, categorical breakdowns, and small individual-level datasets most effectively.*

- Characterization of personal finance transaction data as sequential time-series [/spending-time-series]
  > *Scholar query: How do researchers characterize personal finance transaction data as a sequential time-series problem, and what properties of that data make time-series modeling appropriate? I am looking for studies that analyze the structural characteristics of individual-level spending records — including temporal ordering, autocorrelation, seasonality, and irregular sampling — and that use these properties to motivate the selection of sequential or temporal modeling approaches over non-temporal alternatives.*

- Evidence of temporal dependency in spending: prior periods predict subsequent periods [/temporal-dependency]
  > *Scholar query: What empirical evidence exists that personal spending behavior exhibits temporal dependency — that is, that spending in prior periods is predictive of spending in subsequent periods? I am looking for studies that quantify autocorrelation or lag effects in household or individual-level expenditure data, and that use this evidence to justify the application of sequential models, particularly in contexts where spending patterns repeat across daily, weekly, or monthly cycles.*

- Interaction between mobile constraints and the practical choice of forecasting algorithm [/mobile-forecast-tradeoff]
  > *Scholar query: How do mobile deployment constraints — such as limited memory, processing power, and battery — interact with and constrain the practical choice of spending forecasting algorithm in personal finance applications? I am looking for research that explicitly evaluates the feasibility of running forecasting models on-device or with minimal server round-trips, and that discusses how model size, inference latency, and retraining frequency factor into algorithm selection for mobile-first deployments.*

- Cold-start fallback strategies for forecasting without sufficient transaction history [/forecast-cold-start]
  > *Scholar query: What cold-start fallback strategies are used in forecasting systems when a user does not yet have sufficient transaction history to generate a reliable personalized prediction? I am looking for research on how personal finance or recommender systems handle new users — including population average priors, profile-based initialization, synthetic data augmentation, and conservative or neutral default forecasts — and what evidence exists for the appropriateness of each fallback approach.*

- Per-category spending forecasting across multiple simultaneous expense categories [/per-category-forecast]
  > *Scholar query: How have researchers approached the problem of forecasting spending across multiple expense categories simultaneously, rather than predicting total spending as a single aggregate figure? I am looking for studies that use multi-output or multi-variate forecasting models — such as multi-output LSTM or multi-task learning approaches — applied to disaggregated household or personal expenditure data organized by category, and that report results on per-category prediction accuracy.*

---

### D.2 LSTM as the Spending Forecasting Algorithm [/lstm]

- LSTM architecture: gates, cell state, and the class of sequential problems it solves [/lstm-architecture]
  > *Scholar query: How is the LSTM architecture structured — including its input gate, forget gate, output gate, and cell state — and what class of sequential or time-series problems is it specifically designed to solve? I am looking for foundational or applied literature that explains the gating mechanism as a solution to the vanishing gradient problem in standard RNNs, and that characterizes the types of sequential patterns — long-range dependencies, recurring cycles, trend-plus-seasonality — where LSTM demonstrably outperforms simpler models.*

- Comparative performance of LSTM vs. ARIMA, XGBoost, GRU, and Transformer on time-series tasks [/lstm-vs-alternatives]
  > *Scholar query: How does LSTM compare in forecasting performance against alternative models — including ARIMA, XGBoost, GRU, and Transformer-based architectures — when applied to time-series prediction tasks? I am looking for benchmark studies that report accuracy metrics such as RMSE, MAE, or MAPE across these model families on sequential prediction tasks, and that discuss the conditions under which LSTM maintains a performance advantage versus when alternatives are preferable.*

- LSTM applied to household expenditure, consumption, and personal spending data [/lstm-spending-applied]
  > *Scholar query: What are the documented results of applying LSTM models to household expenditure, consumer spending, or personal finance transaction data? I am looking for applied studies that use LSTM to predict spending at the individual or household level — reporting dataset characteristics, model configurations, accuracy metrics, and practical conclusions about the model's suitability for personal budget forecasting as opposed to aggregate macroeconomic or retail demand prediction.*

- LSTM for simultaneous multi-output, multi-category forecasting [/lstm-multi-output]
  > *Scholar query: How have researchers used LSTM to simultaneously forecast spending across multiple expense categories, rather than predicting a single aggregate output? I am looking for studies that implement multi-output LSTM or multi-task LSTM architectures on disaggregated spending data — describing how shared representations are learned across categories and reporting whether per-category prediction accuracy is competitive with training separate models per category.*

- LSTM feasibility under mobile and resource-constrained deployment [/lstm-mobile]
  > *Scholar query: Is LSTM feasible to deploy in mobile or resource-constrained environments for inference tasks such as spending forecasting, and what techniques are used to make it so? I am looking for research on model compression, quantization, pruning, or distillation applied specifically to LSTM models intended for on-device or low-latency inference — with reported tradeoffs between model size reduction and prediction accuracy loss.*

- Justification of LSTM over surveyed alternatives given Odin's data characteristics and context [/lstm-justification]
  > *Scholar query: What justification is provided in the literature for selecting LSTM over alternative forecasting algorithms when the data exhibits the characteristics typical of individual-level personal finance transactions — including temporal dependency, periodic cycles, category-level granularity, and limited per-user history? I am looking for selection rationales that eliminate ARIMA on grounds of non-stationarity or lack of multivariate support, eliminate tree-based models on grounds of poor sequential generalization, and affirm LSTM as the strongest fit for the task's structural requirements.*

---

## E. Anomaly and Overage Detection [/anomaly-detection]

### E.1 Anomaly Detection in Personal Finance Systems [/anomaly-pfms-domain]

- Definition and taxonomy of financial anomalies detectable in personal spending data [/anomaly-taxonomy]
  > *Scholar query: How do researchers define and classify the types of anomalies that are detectable in personal spending or financial transaction data? I am looking for literature that develops or applies a taxonomy of financial anomalies at the individual or household level — distinguishing between sudden spending spikes, unusual category patterns, behavioral deviations from a user's established baseline, and budget overage events — and that discusses which detection approaches are appropriate for each type.*

- Threshold-based overage alerting vs. behavioral baseline deviation: distinction and scope [/overage-vs-behavioral]
  > *Scholar query: What is the conceptual and technical distinction between threshold-based budget overage alerting and behavioral baseline deviation detection in personal finance systems? I am looking for research that clearly separates these two mechanisms — where overage alerting fires when a user exceeds a predefined budget limit, and baseline deviation detection fires when spending departs from the user's own historical norm regardless of a budget — and that discusses the appropriate scope and limitations of each approach.*

- Detection approaches applied to personal finance data and their reported results [/anomaly-approaches]
  > *Scholar query: What anomaly detection approaches have been applied to personal finance or financial transaction data at the individual level, and what results have they produced? I am looking for comparative or applied studies that implement methods such as Isolation Forest, One-Class SVM, statistical threshold models, or autoencoder-based detection on personal spending records — reporting detection accuracy, false positive rates, and practical suitability for real-world financial monitoring.*

- Tradeoffs between rule-based and algorithmic detection: complexity, explainability, accuracy [/anomaly-tradeoffs]
  > *Scholar query: What are the documented tradeoffs between rule-based anomaly detection and algorithmic or machine learning-based detection in personal finance contexts? I am looking for research that compares these two approaches on dimensions of implementation complexity, user-facing explainability of alerts, accuracy in detecting meaningful anomalies, and sensitivity to false positives — particularly where explainability is critical because users need to understand why a transaction was flagged.*

- Anomaly detection output feeding forward into next budget recommendation cycle [/anomaly-feedback]
  > *Scholar query: Is there research on designing personal finance systems where anomaly detection output feeds forward into the next budget recommendation cycle — for example, where a detected overspending pattern in one period is factored into the budget allocation or warning thresholds for the following period? I am looking for system design literature or implemented PFMS descriptions that close the loop between anomaly detection and budget recommendation rather than treating them as independent modules.*

- Filipino culturally specific high-value spending recognized as expected, not anomalous [/cultural-spending-protection]
  > *Scholar query: How should a personal finance anomaly detection system handle culturally specific high-value spending events that are expected and planned by Filipino users — such as paluwagan contributions, Christmas gift spending, or family remittances — but that might appear anomalous by statistical measures? I am looking for research on protecting or whitelisting culturally normative spending categories from anomaly detection, and on how systems can distinguish between planned extraordinary expenses and genuinely unexpected deviations.*

- Alert design: frequency, format, and framing to minimize alert fatigue while ensuring action [/alert-design]
  > *Scholar query: What does research say about designing anomaly or overspending alerts in mobile personal finance applications to minimize alert fatigue while still prompting user action? I am looking for studies that evaluate alert frequency, notification timing, framing strategies (e.g., loss-framing vs. neutral information), and message format in the context of financial applications — and that report user behavioral responses and the conditions under which alerts are acted on versus dismissed.*

---

### E.2 Anomaly Detection Algorithm [/anomaly-algo]

- Anomaly detection as an ML problem: unsupervised, semi-supervised, and supervised families [/anomaly-ml-families]
  > *Scholar query: How is anomaly detection framed as a machine learning problem, and what are the structural differences between unsupervised, semi-supervised, and supervised approaches in this domain? I am looking for survey or overview literature that explains when each family of approaches is appropriate — particularly the case for unsupervised methods when labeled anomaly examples are unavailable, as is typical in personal finance contexts where individual users cannot be expected to annotate their own abnormal transactions.*

- Isolation Forest: mechanism, per-user baseline learning without labeled training data [/isolation-forest]
  > *Scholar query: How does the Isolation Forest algorithm work mechanistically — including its use of random partitioning, path length scoring, and the isolation principle — and how does it learn an anomaly baseline for each user without requiring labeled training examples? I am looking for foundational and applied literature that explains why Isolation Forest is particularly well-suited to unsupervised anomaly detection in settings where the definition of normal behavior is individual-specific and cannot be predetermined.*

- Isolation Forest applied to personal financial transaction and spending data [/isolation-forest-applied]
  > *Scholar query: What results have been reported when Isolation Forest is applied to personal financial transaction or spending data for the purpose of anomaly detection? I am looking for applied studies that use Isolation Forest on individual-level transaction records — describing feature engineering choices, contamination parameter settings, evaluation methodology, and reported precision or recall — particularly in contexts comparable to a personal budget management system tracking daily expenditures.*

- Tradeoffs: mobile feasibility, false positive control, and user-facing explainability [/anomaly-algo-tradeoffs]
  > *Scholar query: What are the tradeoffs of using Isolation Forest for anomaly detection in a mobile personal finance application, particularly with respect to computational feasibility on mobile hardware, control of the false positive rate to avoid unnecessary user alerts, and the ability to explain flagged anomalies in user-facing language? I am looking for research that evaluates these dimensions specifically for Isolation Forest in comparison to alternative anomaly detection methods such as One-Class SVM, LOF, or autoencoder-based approaches.*

- Justification of chosen anomaly detection approach over alternatives for Odin [/anomaly-algo-justification]
  > *Scholar query: How do researchers justify the selection of Isolation Forest over alternative anomaly detection algorithms for a personal finance system serving individual users with no labeled anomaly history, operating under mobile deployment constraints, and requiring per-user adaptive baselines? I am looking for algorithm selection rationales that rule out supervised classifiers due to absence of labels, rule out density-based methods due to scalability, and affirm Isolation Forest based on its unsupervised baseline learning, computational efficiency, and suitability for multivariate spending feature spaces.*

---

## F. User Profiling and Classification [/user-profiling]

### F.1 User Behavioral Profiling in Filipino Personal Finance Contexts [/fil-profiling-domain]

- Role of user profiling in budget recommendation, forecasting fallback, and system personalization [/profiling-role]
  > *Scholar query: What role does user behavioral profiling play in enabling personalization within personal finance management systems — specifically in improving budget recommendation accuracy, providing fallback behavior for new users during cold start, and tailoring forecasting to individual spending patterns? I am looking for system design literature or implemented PFMS studies that demonstrate how assigning users to profile types shapes the output of downstream algorithmic modules rather than treating all users identically.*

- Inadequacy of Western financial behavioral taxonomies for Filipino user contexts [/western-taxonomy-gap]
  > *Scholar query: Why are Western financial behavioral taxonomies and financial personality frameworks inadequate for characterizing Filipino users' financial behavior? I am looking for research that documents the cultural, structural, and institutional differences between Filipino and Western financial contexts — including obligations like paluwagan, family remittances, and community contributions that are absent from Western profiling instruments — and that argues for locally grounded profile construction rather than applying imported frameworks.*

- Filipino-specific financial behavioral patterns documented in BSP CFS and FIES data [/fil-behavioral-patterns]
  > *Scholar query: What Filipino-specific financial behavioral patterns are documented in the BSP Consumer Finance Survey and the PSA Family Income and Expenditure Survey that are relevant to designing a personal finance profiling system? I am looking for analyses of these institutional datasets that reveal distinct spending structures, savings behaviors, obligation patterns, or income characteristics among Filipino households that would meaningfully differentiate user types in a Filipino personal finance management system.*

- Constructing locally grounded financial profiles from Philippine institutional datasets [/fil-profile-construction]
  > *Scholar query: How can locally grounded financial behavioral profiles or user archetypes be constructed from Philippine institutional data sources such as the FIES and BSP CFS? I am looking for methodological literature on deriving user typologies from survey or expenditure datasets — including clustering, segmentation, or expert-informed classification approaches — applied to data that captures Filipino household financial structure rather than adapting profiles from foreign populations.*

- Behavioral dimensions as meaningful profile differentiators: income stability, obligation weight, savings disposition [/profile-dimensions]
  > *Scholar query: What behavioral dimensions — such as income stability, the weight of obligatory versus discretionary spending, and savings orientation or disposition — are most meaningful for differentiating financial user profiles in a personal finance context? I am looking for research that validates these dimensions as discriminating features rather than arbitrary groupings, and that demonstrates how users who differ along these axes actually require different budgeting strategies, recommendation logic, or forecasting approaches.*

- Concept drift as a framework for progressive user profile updates over time [/concept-drift]
  > *Scholar query: How is the concept drift framework applied to adaptive user modeling and profile updates in intelligent systems, and how does it apply to the problem of progressively updating a user's financial behavioral profile as their spending and income patterns evolve? I am looking for literature on drift detection methods and adaptive learning strategies that can serve as the technical grounding for a personal finance system that updates user profiles based on behavioral signal accumulation over time.*

- Behavioral signals that should trigger profile reassessment [/profile-triggers]
  > *Scholar query: What behavioral signals in a personal finance system should trigger a reassessment or reclassification of a user's financial profile? I am looking for research on change-point detection, sustained behavioral shifts, or threshold-based triggers in adaptive user modeling — applied to signals such as sustained income level changes, shifts in the proportion of obligatory versus discretionary spending, or consistent departures from the patterns used to initially classify the user.*

- Automatic system-initiated vs. user-confirmed profile update mechanisms [/profile-update-mechanism]
  > *Scholar query: Should profile updates in adaptive personal finance systems be system-initiated automatically based on detected behavioral change, or should they require explicit user confirmation? I am looking for research on user trust, transparency, and the design of profile update mechanisms — including the tradeoffs between automated reclassification that may surprise users and user-confirmed flows that provide agency but may introduce delay or be ignored.*

- Cold-start problem and profile-average fallback for new users without behavioral history [/profiling-cold-start]
  > *Scholar query: How is the cold-start problem handled in personalized financial systems for new users who have no behavioral transaction history yet? I am looking for research on profile-average or population prior fallback strategies — where a new user is initially assigned to a default profile based on onboarding input or demographic similarity — and on how quickly systems can transition from generic to personalized behavior as user data accumulates.*

---

### F.2 Profile Classification Algorithm [/profile-classification-algo]

- Supervised classification vs. clustering for predefined profile categories [/classification-vs-clustering]
  > *Scholar query: When should supervised classification be chosen over clustering for assigning users to financial behavioral profiles, particularly when the profile categories are predefined by domain knowledge rather than discovered from data? I am looking for research that discusses the suitability of supervised versus unsupervised approaches in the context of fixed profile taxonomies — arguing that classification is appropriate when profiles are already specified and the task is to assign users, not to discover new groupings.*

- Classification algorithms documented for behavioral and financial user profiling [/classifier-candidates]
  > *Scholar query: What classification algorithms have been applied to behavioral or financial user profiling tasks — including logistic regression, support vector machines, Random Forest, gradient boosting, and neural network classifiers — and what results do they produce in terms of accuracy, interpretability, and feature importance? I am looking for comparative studies that benchmark multiple classifiers on user profile or customer segmentation tasks using behavioral or financial feature sets, reporting performance metrics and practical tradeoffs.*

- Feature selection: onboarding questionnaire responses vs. early transaction behavioral data [/classifier-features]
  > *Scholar query: What features are most appropriate for classifying a user's financial behavioral profile — questionnaire responses collected during onboarding, early transaction behavioral data, or a combination of both? I am looking for research on feature selection and feature engineering for financial user profiling classifiers, including evidence on which input types produce more accurate profile assignments and how the feature set should change as the system accumulates more behavioral data beyond the onboarding stage.*

- Cold-start classification: initial model training without labeled real user data [/classifier-cold-start]
  > *Scholar query: How can a supervised user profile classifier be trained when no labeled real user data exists at system launch — a cold-start training problem? I am looking for research on approaches such as synthetic data generation, expert-defined feature distributions, transfer learning from proxy datasets, or simulation-based training that allow a classification model to be deployed before the system has acquired real behavioral data from actual users.*

- Progressive reclassification: periodic batch, continuous, or drift-triggered profile updates [/progressive-reclassification]
  > *Scholar query: What strategies exist for progressively reclassifying users into updated financial behavioral profiles over time — including periodic batch reclassification, continuous online learning, and drift-triggered reassessment? I am looking for research that evaluates these update strategies in terms of classification stability, responsiveness to genuine behavioral change, and resistance to noise-driven spurious reclassifications — particularly in financial contexts where profile stability matters for user trust and recommendation consistency.*

- Tradeoffs across candidate classifiers: predictive accuracy, interpretability, mobile feasibility [/classifier-tradeoffs]
  > *Scholar query: What are the tradeoffs among candidate classification algorithms for financial user profiling when evaluated along dimensions of predictive accuracy, interpretability of predictions, and mobile deployment feasibility? I am looking for comparative analyses that show how algorithms like logistic regression, decision trees, Random Forest, SVM, and neural networks perform differently when the deployment environment is a resource-constrained mobile application and when the classification decision must be explainable to users or auditable by the development team.*

- Justification of the chosen classifier for Odin's four-profile structure and use context [/classifier-justification]
  > *Scholar query: How should a classification algorithm be selected and justified for a four-class predefined financial user profiling task in a mobile personal finance system serving Filipino young professionals, where the training data is synthetic at launch and the classifier must be deployable on constrained hardware? I am looking for selection rationales that weigh accuracy, mobile feasibility, interpretability, and cold-start viability — and that explicitly compare and eliminate alternative classifiers rather than defaulting to one without documented justification.*

---

## G. Expense Categorization [/expense-categories]

### G.1 Expense Categorization in Filipino Personal Finance Contexts [/expense-cat-domain]

- Approaches to expense categorization: user-defined, institutionally derived, ML-generated, hybrid [/cat-approaches]
  > *Scholar query: What approaches to expense categorization have been implemented in personal finance systems, and how do they compare? I am looking for research that evaluates user-defined category taxonomies, institutionally derived category schemes based on national expenditure surveys, machine learning-generated categorizations from transaction descriptions, and hybrid approaches that combine these methods — with attention to the tradeoffs between flexibility, accuracy, and cultural appropriateness for different user populations.*

- Limitations of Western expense category schemas for Filipino spending contexts [/western-cat-limitations]
  > *Scholar query: In what ways do Western-designed expense category schemas fail to adequately represent Filipino spending patterns and financial obligations? I am looking for research or design literature that identifies specific mismatches — such as the absence of categories for paluwagan contributions, family remittances, bayanihan-type sharing, or multi-household financial support — and that argues for the inadequacy of importing foreign categorization schemes into Filipino personal finance applications without significant local adaptation.*

- PSA FIES and BSP CFS expenditure categories and their mapping to a local PFMS [/fies-bsp-mapping]
  > *Scholar query: How are the expenditure categories defined in the PSA Family Income and Expenditure Survey and the BSP Consumer Finance Survey structured, and how can they be mapped to the expense category system of a local Filipino personal finance management application? I am looking for research or documentation that uses these institutional survey instruments as a basis for designing culturally grounded expense taxonomies, and that demonstrates how FIES and BSP CFS categories can inform the default category structure of a PFMS serving Filipino users.*

- Cultural expense types warranting dedicated categories: paluwagan, remittances, religious obligations [/cultural-expense-types]
  > *Scholar query: What culturally specific expense types in Filipino financial practice warrant dedicated categories in a personal finance management system, rather than being absorbed into generic miscellaneous or social expense buckets? I am looking for literature that documents the financial significance and regularity of paluwagan contributions, family remittances, religious and community donations, and similar obligations — and that makes the case that these represent distinct behavioral and budgeting domains that should be tracked separately.*

- Institutional basis for protected expense categories and minimum spending floors [/protected-categories]
  > *Scholar query: What institutional or regulatory basis exists for designating certain expense categories as protected or essential — meaning they carry minimum spending floors that a personal finance system should not allow budget recommendations to undercut? I am looking for research or policy literature grounded in BSP financial inclusion guidelines, Philippine social protection frameworks, or financial wellness standards that establishes which spending categories are considered non-negotiable necessities for Filipino households.*

- Expense category design in existing PFMS explicitly serving Filipino users [/fil-pfms-categories]
  > *Scholar query: How have existing personal finance management applications designed their expense category systems to serve Filipino users specifically, and what evidence is there that these designs reflect local spending norms rather than Western defaults? I am looking for system descriptions, UX research, or user studies of Filipino-facing PFMS tools that document category design decisions — particularly how local obligations, cultural expense types, and Philippine-specific deductions are handled.*

- SSS and Pag-IBIG contributions: automatic deductions for employees vs. voluntary entries for variable-income users [/sss-pagibig]
  > *Scholar query: How should SSS, Pag-IBIG, and PhilHealth contributions be categorized and handled in a personal finance management system when the user population includes both regular employees (for whom these are automatic salary deductions) and self-employed or freelance workers (for whom contributions are voluntary and manually paid)? I am looking for research or system design literature that distinguishes these two cases and discusses how a PFMS should represent mandated social contributions differently depending on a user's employment type.*

---

## *H. Data Privacy, Security, and User Trust [/privacy-security]

### H.1 Data Privacy, Security, and User Trust in Personal Finance Systems [/privacy-pfms-domain]

- Sensitivity classification of personal financial data in literature [/data-sensitivity]
  > *Scholar query: How is personal financial data classified in terms of sensitivity and privacy risk in the research literature? I am looking for studies that characterize individual-level transaction records, income data, spending patterns, and budget information as particularly sensitive personal information — discussing the harms that can follow from unauthorized access or misuse, and situating this classification within broader frameworks for categorizing personal data by risk level.*

- Technical security standards for financial application data handling [/security-standards]
  > *Scholar query: What technical security standards and best practices apply to personal finance application data handling — including encryption at rest and in transit, authentication and access control mechanisms, data minimization principles, and secure API design? I am looking for literature that describes industry or research-level security requirements for mobile financial applications handling sensitive personal transaction data, and that evaluates how well existing systems comply with these standards.*

- User trust in personal finance applications and its effect on data-sharing and logging behavior [/user-trust]
  > *Scholar query: How does user trust in a personal finance application affect their willingness to share financial data and maintain consistent transaction logging behavior? I am looking for empirical studies that measure the relationship between perceived trustworthiness — including privacy policy clarity, data security assurances, and brand reputation — and users' actual data-sharing behavior in PFMS applications, particularly among younger users who may be simultaneously privacy-conscious and habitual app users.*

- Privacy concern as a driver of inconsistent or withheld transaction logging [/privacy-logging]
  > *Scholar query: Is there evidence that privacy concern drives users to withhold or inconsistently log transactions in personal finance applications — and if so, what types of transactions are most commonly omitted? I am looking for research that documents the relationship between perceived data sensitivity and logging completeness, and that discusses how privacy anxiety around financial data leads to gaps in the transaction record that then degrade the quality of ML-driven personalization and forecasting.*

- Philippine regulatory framework: RA 10173, BSP data governance guidelines, NPC issuances [/ph-privacy-law]
  > *Scholar query: What is the Philippine regulatory framework governing the collection, storage, and processing of personal financial data in mobile applications — including the Data Privacy Act of 2012 (Republic Act 10173), BSP data governance circulars, and National Privacy Commission issuances? I am looking for legal or compliance literature that describes how these regulations apply to a locally developed personal finance management system, what obligations they impose on the system developer, and how compliance can be demonstrated in system design.*

- Privacy-by-design principles applied in comparable financial system research [/privacy-by-design]
  > *Scholar query: How have privacy-by-design principles been applied in the design and development of personal finance or financial management systems, as documented in research literature? I am looking for studies that describe specific implementation strategies — such as data minimization, purpose limitation, user consent management, and on-device processing — that embed privacy protection into the system architecture rather than treating it as a compliance checkbox, with attention to how these principles are operationalized in mobile financial applications.*

- Privacy implications specific to manual self-reported financial data without banking API integration [/manual-data-privacy]
  > *Scholar query: What privacy implications are specific to personal finance systems that rely entirely on manual, self-reported transaction data rather than automated banking API integration? I am looking for research that discusses the privacy risk profile of self-reported financial data — considering that users must actively disclose sensitive spending information — and how the absence of banking integration changes the threat model, data governance obligations, and user trust dynamics compared to systems that pull data automatically from financial institutions.*

---

## I. User Retention and Engagement [/retention]

### I.1 User Retention and Engagement in Personal Finance Systems [/retention-pfms-domain]

- Relationship between transaction data completeness and downstream ML model performance [/data-completeness-ml]
  > *Scholar query: How does the completeness and consistency of user-logged transaction data affect the performance of downstream machine learning models — such as spending forecasting and anomaly detection — in personal finance systems? I am looking for research that quantifies the degradation in model accuracy caused by gaps, omissions, or inconsistent logging frequency in individual-level transaction histories, and that identifies the minimum data completeness threshold required for ML modules to produce reliable and actionable outputs.*

- Drop-off patterns in personal finance apps: when users stop logging and why [/drop-off-patterns]
  > *Scholar query: What are the documented drop-off and attrition patterns in personal finance applications — specifically, at what point in their usage journey users stop logging transactions, and what factors predict early abandonment? I am looking for longitudinal studies or user behavior analyses that track when engagement falls off (e.g., after the first week, first month, after a missed budget cycle) and that identify the behavioral, motivational, or usability triggers that cause users to stop maintaining their financial records.*

- Manual data entry as the primary engagement friction point in PFMS [/entry-friction]
  > *Scholar query: Is manual transaction data entry the primary source of engagement friction and user abandonment in personal finance management systems, and what evidence supports this? I am looking for usability research and user studies that identify data entry burden as the dominant barrier to sustained engagement — distinct from other friction sources like onboarding complexity or notification overload — and that measure its specific contribution to drop-off rates relative to other usability factors.*

- Non-gamification retention mechanisms: smart notifications, frictionless input, feedback loops, goal-setting [/retention-mechanisms]
  > *Scholar query: What retention mechanisms in personal finance applications are effective at sustaining user engagement without relying on gamification — specifically mechanisms such as well-timed smart notifications, minimized input friction, value-feedback loops showing users the benefits of their logged data, and goal-setting features? I am looking for evidence-based research that evaluates these non-gamification approaches in terms of their effect on long-term retention, logging consistency, and perceived application value.*

- Minimum viable interaction frequency for a personal finance app to deliver perceived value [/min-interaction-freq]
  > *Scholar query: What is the minimum frequency of user interaction with a personal finance application — in terms of how often they log transactions or check their dashboard — required for the application to deliver meaningful perceived value? I am looking for research that identifies an engagement threshold below which users are unlikely to benefit from PFMS features like forecasting or alerts, and above which the system has enough behavioral data to generate useful personalized outputs.*

- Demonstrated system value — accurate forecasts, actionable alerts — as intrinsic retention driver [/value-driven-retention]
  > *Scholar query: Does demonstrated system value — such as accurate spending forecasts, useful budget recommendations, or actionable anomaly alerts — function as an intrinsic retention driver in personal finance applications, sustaining engagement without extrinsic rewards? I am looking for research that connects the perceived accuracy and usefulness of intelligent PFMS outputs to user motivation to continue logging, and that frames value delivery rather than incentive design as the primary mechanism for long-term retention.*

---

## *J. System Evaluation [/system-eval]

### J.1 System Evaluation in Personal Finance and Budget Management Systems [/eval-pfms-domain]

- Evaluation frameworks, metrics, and methodologies documented for PFMS and PBMS [/eval-frameworks]
  > *Scholar query: What evaluation frameworks, metrics, and methodologies have been documented in research for assessing the quality of personal finance management and personal budget management systems? I am looking for literature that surveys how PFMS tools are formally evaluated — including functional accuracy testing, user satisfaction measurement, usability assessment, and behavioral outcome tracking — and that identifies which evaluation approaches are most commonly used and most appropriate for systems that combine intelligent modules with user-facing interfaces.*

- ISO/IEC 25010:2023 quality characteristics and their application to evaluating a PFMS [/iso-25010]
  > *Scholar query: How are the quality characteristics defined in ISO/IEC 25010:2023 — including functional suitability, performance efficiency, compatibility, usability, reliability, security, maintainability, and portability — applied to the evaluation of a software system such as a personal finance management application? I am looking for research that operationalizes these quality characteristics into measurable evaluation criteria for a PFMS context, and that discusses which characteristics are most critical and how they are assessed in practice.*

- System Usability Scale: instrument design, scoring, administration, and scope [/sus]
  > *Scholar query: What is the design, scoring methodology, administration procedure, and intended scope of the System Usability Scale as a usability evaluation instrument? I am looking for foundational and applied literature that explains the SUS questionnaire structure, how the ten-item scale is scored to produce a composite usability rating, what benchmarks exist for interpreting that score, and what types of systems and evaluation contexts the instrument is appropriately applied to versus where its use may be limited.*

- SUS applied specifically to mobile-first applications [/sus-mobile]
  > *Scholar query: How has the System Usability Scale been applied to evaluate mobile-first applications, and what SUS score benchmarks and distribution patterns have been reported in mobile application usability studies? I am looking for research that uses SUS specifically in the context of mobile app evaluation — reporting score distributions, comparing results across different mobile application types, and discussing any modifications or considerations required when using SUS for mobile interfaces as opposed to desktop systems.*

- Combining ISO 25010 and SUS as a joint evaluation framework [/iso-sus-combined]
  > *Scholar query: Is there research that proposes or implements a combined evaluation framework using both ISO/IEC 25010 and the System Usability Scale for assessing software system quality? I am looking for studies that use these two instruments jointly — describing how they complement each other (ISO 25010 covering broader software quality characteristics and SUS capturing user-perceived usability) and how their results are integrated or reported together in a coherent evaluation methodology.*

- ISO 25010 and SUS applied in PFMS or comparable financial application evaluations [/eval-pfms-applied]
  > *Scholar query: What examples exist of ISO/IEC 25010 and the System Usability Scale being applied to evaluate personal finance management systems or comparable financial applications? I am looking for applied evaluation studies that use these instruments on PFMS tools — reporting how quality characteristics were operationalized, what SUS scores were obtained, what the evaluation findings revealed about system quality, and how the results were used to support conclusions about the system's fitness for purpose.*

- Acknowledged limitations of SUS and ISO 25010 as evaluation instruments [/eval-limitations]
  > *Scholar query: What are the acknowledged limitations of the System Usability Scale and ISO/IEC 25010 as evaluation instruments, particularly when applied to mobile applications with intelligent or ML-driven components? I am looking for critical literature that identifies where SUS falls short — such as its insensitivity to specific usability dimensions, its reliance on post-task self-report, or its lack of coverage for AI-driven features — and where ISO 25010's quality model may inadequately capture qualities relevant to adaptive or personalized systems.*

- Sample size and respondent profile guidelines for SUS-based evaluations [/sus-sample-size]
  > *Scholar query: What sample size and respondent profile recommendations exist for conducting a valid SUS-based usability evaluation, and what do comparable studies use in practice? I am looking for research on the statistical properties of SUS that inform minimum sample size decisions — including evidence on the reliability of SUS scores as a function of sample size, recommendations for respondent recruitment criteria, and the sample sizes reported in published SUS evaluations of mobile or personal finance applications that can serve as precedents.*

---

* Flagged; to be discussed further.