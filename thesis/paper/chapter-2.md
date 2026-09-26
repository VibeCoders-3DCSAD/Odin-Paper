# Chapter 2: Review of Related Literature and Studies (Draft V2.0)

> **Status of this draft**
>
> - Working mirror of `google-drive/chapter-2/GROUP4 - CHAPTER 2 - V2 - 09.15.26.docx`; supersedes the earlier V1.0 draft (`chapter-2.md` of 09-03 and `GROUP4 - CHAPTER 2 - V1 - 09.02.26.docx`).
> - Structured per `formats-templates/chapter-2/Writing Chapter 2.docx` (official guideline) with reference to `formats-templates/Reference Thesis (Group 10).docx`.
> - Incorporates Ma'am Era's inline comments on the V2 document: open each discussion with the study's own idea, direct every section to BUDI, combine savings and debt, name personalization explicitly, tie all data types to the system's inputs, rewrite the fragmented sentences, make the methodology BUDI-specific, and produce a full synthesis.
> - Citation policy: APA 7th edition. Citations are placed only where a curated corpus source directly supports the claim; unverified or risky sources are marked with `<!-- VERIFY: ... -->`.
> - Conceptual Model, Tables on Existing Literature, and Research Gaps — previously deferred — are now included.

---

## Introduction

This chapter presents the literature and studies relevant to the development of BUDI, a personalized intelligent finance management application that combines Support Vector Machine (SVM) profile classification, Seasonal Autoregressive Integrated Moving Average (SARIMA) forecasting, linear programming (LP)-based budgeting, and interquartile-range (IQR) anomaly detection to improve Filipinos' savings and debt. The review examines the personal savings and debt behavior of the target user, the functions and intelligent features of existing finance management applications, the models, algorithms, and data used by such systems, the methodology for developing them, and the frameworks used to evaluate them.

The discussion is organized thematically into five major areas that mirror the structure of the study's topical outline. First, the literature on personal savings and debt in the Philippines establishes what improved savings and debt look like for the typical Filipino user. Second, the literature on personalized intelligent finance management applications establishes the functions, forms, and intelligent capabilities expected of the proposed system. Third, the literature on system models and algorithms examines the classification, forecasting, optimization, and anomaly-detection approaches that support each of BUDI's modules, together with the data they require. Fourth, the literature on system development practices grounds the methodology adopted in building the application. Fifth, the literature on system evaluation identifies the metrics and models used to judge the system's usability and acceptance. The reviewed works are analyzed and synthesized to determine existing practices, identify limitations, and establish the research gap addressed by BUDI.

---

## 1. Personal Savings and Debt in the Philippines

### 1.1. The Target User

Understanding the demographic, social, psychological, and economic profile of the target user is essential before designing any personal finance management intervention, because each dimension determines how an individual saves, borrows, and budgets. In the Philippine context, these factors interact strongly: household composition, income stability, social norms, self-control, and financial literacy jointly shape whether an individual builds emergency funds, takes on debt, and follows a budget. The relevance to BUDI is straightforward — the application's personalization engine relies on this profile to classify users, and its savings and debt features must respond to the realities of this profile.

Demographic characteristics such as age, household composition, and stage in life influence financial decision making. Young adults face formative decisions about savings, debt, and budgeting, making them a critical demographic for financial intervention (Bangko Sentral ng Pilipinas [BSP], 2026). In the National Capital Region, income and years of investing correlate positively with the financial well-being of Filipino young professionals aged 25–35, yet the study found investing experience to be considerably low, indicating that this segment has room for targeted financial support (Cruz et al., 2026). Household composition further complicates planning because many Filipino workers support extended family members, so a portion of income is continuously assigned to family obligations (Abila & Ulibas, 2026). These findings imply that BUDI's target-user model must account for shared-family obligations and a young, income-constrained working population rather than assume a single-earner household.

Social and societal factors are equally consequential. Social influence from peers and family shapes financial norms and practices, and parental socialization about money establishes foundational behaviors that persist into adulthood (Bulan & Nemino, 2025; Tangney et al., 2004, as cited in Bulan & Nemino, 2025). Relative income perceptions — comparing one's financial status with others — also affect saving motivation and spending patterns (Wang-Ly & Newell, 2023). On the psychological side, self-control is a critical positive determinant of saving behavior, and the interplay of behavioral intention moderates how strongly self-control translates into actual saving discipline among Filipino MSME owners (Bulan & Nemino, 2025). Financial literacy improves budgeting and investment behavior, although knowledge alone does not automatically produce savings, a distinction that matters when designing behavior-oriented app features (Cumaio et al., 2026; Dheepiga & Sivakumar, 2025). Collectively, these results indicate that BUDI's personalization should weigh behavioral and social signals — not only income — when guiding users.

Economic conditions determine the capacity to save and the burden of debt. Income volatility creates uncertainty that complicates financial planning, and individuals with unstable incomes struggle to maintain consistent saving habits (Ganong et al., 2025; Wang-Ly & Newell, 2023). National data reflect this: only about one in three Filipino adults kept some form of savings in 2021, and more than half relied on family and friends when an emergency expense arose, because emergency funds were present in under one in five households (BSP, 2023). Financial well-being — the subjective perception of security and the ability to meet current and future obligations — depends on both objective conditions and subjective perceptions (Bai, 2023; Erno & Grefalde, 2026) <!-- VERIFY: Erno & Grefalde venue appears anomalous in the source; confirm journal before Google Docs use -->. Budgeting, access to financial services, and prudent debt management therefore matter as much as income level (Claro & Noval, 2025; Sohilauw et al., 2026). For BUDI, this establishes that the target user is financially fragile, income-sensitive, and behavior-driven — precisely the population an intelligent savings-and-debt assistant is expected to serve.

### 1.2. Personal Savings and Debt

Personal savings and debt are two sides of the same financial picture: savings represent the portion of income not consumed and the buffer that keeps individuals out of debt, while debt represents obligations that, when excessive, consume income and erode the capacity to save (Yoganandham, 2025). For this reason, the two are discussed together — a financially healthy individual simultaneously accumulates savings (especially emergency savings) and avoids unmanageable debt. This combined view directly informs BUDI, because the application's budgeting, forecasting, and debt-repayment modules must treat savings capacity and debt burden as linked variables rather than separate features.

Savings serve four functions that matter to the Filipino user: providing financial security and stability, acting as a buffer against unexpected expenses, building financial resilience, and enabling the achievement of short- and long-term goals (Yoganandham, 2025). Emergency savings are the most consequential type. Households with adequate emergency savings withstand income shocks without resorting to high-cost borrowing, whereas households without them fall back on formal and informal loans (BSP, 2023; Danahy et al., 2024). The gap is wide in the Philippines: financial-inclusion dashboards show household banking rose over time, but many savers keep funds at home or in non-bank forms, and family, friends, work, and loans rather than own savings remained the leading emergency-fund sources (BSP, 2023; BSP, 2025). Systematic saving also enables long-term goals such as education, homeownership, and retirement (Yeo et al., 2023). These findings establish the design target for BUDI's savings module: build an automatic, goal-based emergency fund that converts irregular income into consistent savings.

Personal debt encompasses consumer debt such as credit cards and personal loans, and housing debt such as mortgages, each with different terms, interest rates, and repayment structures that affect financial well-being (Yoganandham, 2025). The causes of debt are psychological and economic in roughly equal measure. Low self-control, procrastination, and impulse spending drive borrowing beyond need (Bulan & Nemino, 2025), while unemployment, income insufficiency, and emergencies force borrowing to meet basic needs (Francisco et al., 2026). Filipino public-sector employees illustrate the pattern: salary loans are taken for daily living expenses, debt repayment, medical needs, and education, and salary-deduction repayment paradoxically reinforces dependency because take-home pay keeps shrinking, prompting reborrowing (Francisco et al., 2026). At the national level, borrowing has become more common than saving — nearly half of adults held outstanding loans in 2021 and most borrowed from informal sources (BSP, 2023). Digital lending compounds the risk: easier access to credit is associated with reduced financial restraint among wage earners (Esperanza et al., 2025). Excessive debt produces financial stress that affects mental health, productivity, and overall well-being, and it can consume a disproportionate share of income, limiting saving capacity and creating cycles of vulnerability (Danahy et al., 2024; Francisco et al., 2026).

Repayment is as behavioral as it is mathematical. The snowball method pays off the smallest debts first for psychological wins, while the avalanche method pays off the highest-interest debts first for mathematical optimality (Yoganandham, 2025). Avoiding accumulation through disciplined spending and saving is generally preferable to managing existing debt (Yeo et al., 2023). Bibliometric evidence confirms that financial literacy and self-efficacy are central drivers of effective debt management, while impulsivity, overconfidence, and poor self-control undermine debt strategies (Samli et al., 2026). For BUDI, this means the debt module should offer both repayment strategies and reinforcement of the behaviors that prevent reborrowing, because the data show that behavioral, not only mathematical, support is what Filipino borrowers need.

### 1.3. Ways of Improving Personal Savings and Debt

Improving savings and debt requires a multifaceted approach that combines financial planning, resource allocation, skill development, and behavioral change; no single intervention — a budget alone or a lecture on financial literacy — reliably produces improvement by itself (Yoganandham, 2025). This combined logic is what BUDI implements: planning features set goals, budgeting features allocate money, literacy features build knowledge, and behavioral features reinforce habit. The literature reviewed below justifies each of these four levers.

Financial planning is the foundation. Planning involves setting financial goals, creating budgets, and developing strategies to achieve them, and it enables individuals to prioritize spending, allocate resources, and build savings systematically (Yeo et al., 2023). Effective planning must also adapt to changing circumstances and irregular income patterns, so plans that are rigid fail where adaptive ones succeed (Ganong et al., 2025; R. Huang et al., 2025). Resource allocation through budgeting is the most operational of the levers: budgeting helps individuals track income and expenses, identify patterns, and decide between essentials, savings, and discretionary spending, and disciplined budget-following is consistently linked to better financial health and lower debt-trap risk (Dheepiga & Sivakumar, 2025; Prakoso & Apriliani, 2024; Yoganandham, 2025). Conscious "mental budgeting" — mentally classifying and watching expenditures — is associated with higher subjective financial well-being because it makes limits salient (Bai, 2023).

Skill and knowledge improvement strengthens the other levers. Financial-literacy education improves budgeting, saving, and investment decisions, yet several Filipino and Southeast Asian studies caution that knowledge transfers to behavior only when combined with practice, motivation, and access (Claro & Noval, 2025; Cumaio et al., 2026; Dheepiga & Sivakumar, 2025; Encarnacion & Vecina, 2025). Behavioral and habitual improvement is consequently the fourth and decisive lever. Regular saving, prudent spending, and strategic investment are habits built through consistent practice and self-control, and internal motivation sustains them over time (Bulan & Nemino, 2025; Yeo et al., 2023). Digital tools amplify this behavioral channel: e-payment records and dashboards improve monitoring and budgeting, and app nudges such as spending alerts, weekly summaries, and category caps curb impulsive spending, particularly when matched to the user's financial literacy (Yuttama, 2025). These findings collectively justify BUDI's design — an application that does not merely record transactions, but plans, budgets, trains, and reinforces good financial behavior.

---

## 2. Personalized Intelligent Finance Management Applications

### 2.1. Finance Management Functions

Finance management in an application context means managing income, expenses, savings, debts, investments, and budgets through systematic tracking, analysis, and optimization (Yadav et al., 2026). Income management records and analyzes all sources of earnings, including salaries, allowances, and side income; expense management categorizes expenditures to reveal spending patterns and reduction opportunities; and budget management creates spending plans aligned with income, goals, and priorities (Hajj & Hammoud, 2023; Yadav et al., 2026). Savings management supports goal-setting and progress tracking, while debt management tracks obligations, compares repayment strategies, and discourages excessive borrowing (Yoganandham, 2025; Yadav et al., 2026). Investment management adds portfolio tracking and decision support that extend an application beyond day-to-day budgeting (Hajj & Hammoud, 2023). These six functions map one-to-one onto BUDI's modules: income ledgerization, expense categorization, budget allocation, emergency-fund goals, debt-repayment plans, and spending insights.

### 2.2. Forms of Finance Management Applications

Finance management applications take two main forms — mobile applications that offer accessibility and on-the-go tracking, and web-based platforms that provide comprehensive features for detailed analysis (Yadav et al., 2026). The choice between the two depends on user preferences, device availability, and feature requirements, and a mobile-first approach aligns with the digital habits of the younger demographics that dominate smartphone-based financial activity (R. Huang et al., 2025). Institutional and personal experiences support this view: budgeting information systems and intelligent budget-management apps have been delivered as mobile and web applications with strong acceptance when they combined tracking with predictive or analytical capabilities (Ghonaim & El-Sharawy, 2025; Santiago et al., 2025). For BUDI, a mobile-first implementation matches the target user's device reality and the need for always-available expense entry.

### 2.3. Personalization in Finance Management Applications

Personalization tailors financial guidance and recommendations to each user's specific circumstances, preferences, and goals, because no two users share the same income, obligations, or spending psychology (R. Huang et al., 2025; Yadav et al., 2026). Personalization techniques include behavioral profiling, preference learning, adaptive recommendations, and behavior-aware user clustering, which analyze user behavior and financial patterns to deliver relevant insights rather than generic advice (Yang, J., 2024; R. Huang et al., 2025; R Singh, 2025). The benefits are tangible: users report greater engagement, understanding, and trust when guidance is personalized, explainable, and behavior-aware (R. Huang et al., 2025). However, personalization depends on sufficient user data and on algorithms that can turn that data into meaningful customization without overwhelming the user (Yadav et al., 2026; Zhang & Lu, 2026). BUDI operationalizes these findings through its SVM profile classification, which personalizes budgets, forecasts, and alerts to the user's financial profile.

### 2.4. Intelligent Features in Finance Management Applications

Intelligent features — artificial intelligence (AI), machine learning (ML), and deep learning (DL) capabilities that go beyond recording — are what distinguish modern finance applications from digital ledgers. Reviews of AI in fintech show that ML techniques support credit scoring, fraud detection, automated advisory, and personalization by extracting signal from transaction and behavioral data (Hajj & Hammoud, 2023; Zhang & Lu, 2026). Intelligent expense classification and smart budgeting echo BUDI's own architecture: proposed personal finance management systems classify expenses with supervised classifiers, forecast with time-series models, and flag outliers with clustering or isolation-based detectors (DSouza et al., 2026; Yadav et al., 2026). Deep sequential models such as recurrent neural networks and Long Short-Term Memory (LSTM) networks analyze transaction sequences and forecast future consumer behavior with high accuracy (Chen & Tan, 2025; Ghonaim & El-Sharawy, 2025).

Robo-advisors represent the advisory layer of these systems, combining algorithmic analysis with user preferences to generate personalized recommendations (R. Huang et al., 2025; Hajj & Hammoud, 2023). Anomaly detection completes the intelligent feature set by identifying unusual transactions or spending patterns that may indicate errors, fraud, or problematic financial behavior; such systems establish a baseline of normal behavior and flag deviations for user review (A. Huang et al., 2025). Evidence indicates that static detection thresholds deteriorate over time, so adaptive and dynamically calibrated detectors maintain accuracy as spending behavior changes (A. Huang et al., 2025; Zhong, 2025).

Because intelligent features generate alerts and summaries, their presentation must respect the limits of human working memory. Miller's Law holds that working memory retains roughly seven, plus or minus two, chunks of information (Miller, 1956), and more conservative studies place the limit near four plus or minus one (Cowan, 2001). Consequently, BUDI's insights, alerts, and notifications should convey a small number of high-value items at a time — a few flagged transactions, three to four budget categories, one forecast — rather than overload the user. This presentation principle connects the intelligent-feature literature directly to the application's usability design.

---

## 3. System Models and Algorithms

BUDI's value proposition rests on four computational models, each supporting a distinct module: SVM profile classification assigns users to financial-profile categories, SARIMA forecasting predicts future income and expenses, LP-based budgeting allocates income across expense categories to maximize savings under constraints, and IQR-based anomaly detection flags unusual transactions. This section reviews the literature supporting each model in turn, following the guideline structure of definition, how the model works, previous applications, findings, strengths and limitations, and relevance to the proposed system. Where individual model families have been reviewed, this chapter is deliberately directed to how the findings apply to BUDI's modules, not to the model families in the abstract.

### 3.1. Datasets and Data Preprocessing

The datasets that feed personal finance models are first and foremost time series: chronologically arranged financial transactions that capture spending patterns, income flows, and account balances over time, enabling the analysis of trends, seasonality, and behavioral changes (Chen et al., 2024). Each data type in BUDI is tied to a concrete input the application actually consumes: recorded transactions feed expense categorization and anomaly detection; the history of income and recurring obligations feeds income and expense forecasts; period-end budget states feed budget reallocation; and flagged-transaction history feeds the adaptive behavior of the anomaly module. Where real transaction data are scarce during development, synthetic data generation creates realistic financial profiles for model training and testing (Salvador, 2024). Government surveys such as the Bangko Sentral ng Pilipinas (BSP) Consumer Finance and Consumer Expectations surveys provide the macro-level savings and debt indicators used to contextualize and validate these profiles (BSP, 2023, 2026). Public benchmarks and platform datasets from other countries — such as aggregated credit-card spending and fraud-transaction tables — have supported comparable classification and anomaly-detection studies and are used here only where Philippine data are absent (Agrawal et al., 2025; A. Huang et al., 2025).

Data preprocessing is as decisive as the model itself. Cleaning, normalization, feature engineering, and train-test splitting are standard steps in time-series pipelines (Chen et al., 2024). Transaction-level features — spending categories, frequency patterns, trend indicators, and time-windowed amounts — are the input variables from which classifiers and forecasters learn (Chen & Tan, 2025; Yang et al., 2024b). Outlier handling with interquartile-range (IQR) analysis and z-score thresholds is an established preprocessing practice in financial data pipelines before modeling (Begum, 2025; Chen & Tan, 2025). For BUDI, this means the feature-engineering layer converts raw transaction entries into the category, frequency, and trend variables that the classification, forecasting, and anomaly modules require, and the IQR procedure used in preprocessing is the same statistical logic extended into the production anomaly detector.

### 3.2. Classification Models and Concept Drift

Classification models learn patterns from historical data to predict future states. In personal finance, a classifier assigns a user to a financial-profile category — such as a savings-oriented, stable, at-risk, or debt-prone profile — based on financial behaviors and characteristics (Yadav et al., 2026). This is precisely the task BUDI's profile classification performs, and the literature shows the approach is well established: classifiers predict consumer behavior, wealth quintiles, creditworthiness, and spending risk across financial domains (Ghonaim & El-Sharawy, 2025; Salvador, 2024; Zhang & Hou, 2026).

The central challenge for such classifiers is concept drift — the gradual change in the statistical properties of data over time (Abdullahi et al., 2025). User financial behavior evolves with life changes, economic conditions, and personal development, so a model trained on past spending becomes less accurate as the user's circumstances change (Abdullahi et al., 2025; Chikoore et al., 2026). A systematic review of concept-drift mitigation in time-series applications identifies Support Vector Machines (SVM) as the most effective learner for detecting and adapting to drift in classification and regression tasks, owing to their high detection accuracy and effective memory (Abdullahi et al., 2025). Adaptive credit-scoring studies corroborate this finding: frameworks that retrain or dynamically reweight models as drift is detected maintain accuracy, whereas static models degrade (Chikoore et al., 2026).

Support Vector Machines separate classes by finding a decision boundary that maximizes the margin between them, generalizing well even with moderate data (Abdullahi et al., 2025; Hu et al., 2023) <!-- VERIFY: Hu et al. 2023 is a predict+optimize MILP study; the SVM-margin statement is supported by Abdullahi et al. 2025, and its use for the optimization subtopic is where it belongs -->. Empirical comparisons report that SVM offers strong interpretability and stability, although it trains more slowly than gradient-boosted ensembles on very large datasets (Zhang & Hou, 2026). Ensemble methods such as XGBoost and LightGBM often post the highest raw accuracy in large-scale tasks (Shaha & Gavekar, 2025; Zhang & Hou, 2026), and boosting classifiers have predicted Philippine household wealth quintiles with high accuracy on national survey data (Salvador, 2024). Where the literature is clear is the trade-off: accuracy, interpretability, and training cost must be balanced for the deployment context (Reyes et al., 2024; Zhang & Hou, 2026). For BUDI, this justifies SVM as the primary classifier — its drift resilience, interpretability, and small-data behavior suit a mobile application with a continuously changing user — while noting that the drift literature and boosting benchmarks inform how the model should be monitored and retrained over the user's financial lifecycle.

### 3.3. Time-Series Forecasting

Time-series forecasting predicts future values from historical patterns and is the module that lets BUDI anticipate the user's income and expenses rather than merely record them. Statistical and machine-learning forecasting families both appear in the finance literature, and the choice between them is the core modeling decision for this module (Chen et al., 2024; Chen & Tan, 2025; Sonkavde et al., 2023).

Classical statistical models remain strong for personal finance because monthly income and expense series are short, regular, and highly seasonal. The Seasonal ARIMA (SARIMA) model extends ARIMA with seasonal differencing and seasonal autoregressive and moving-average terms, and is specifically endorsed for consumer finance where seasonality is commonly observed (DSouza et al., 2026). Systematic reviews of budget forecasting over four decades list SARIMA among the dominant statistical methods alongside ARIMA, Holt–Winters, and neural approaches, with MAPE, RMSE, and MAE as the standard evaluation metrics (Kara & Şengüler, 2025). A constrained budgeting framework that forecasts category-level demand with a SARIMAX model and then feeds those forecasts into a constraint-aware optimizer — the same forecast-then-optimize pipeline BUDI uses — reported roughly 2.85% MAPE on aggregate demand and showed that unconstrained point forecasts can violate budget constraints, motivating the optimizer stage (Lu et al., 2025).

Deep-learning forecasting models — convolutional networks, RNN/LSTM, GRU, and Transformers — excel at very large, multivariate time series, but no single architecture dominates across datasets, and their advantage over simpler baselines narrows on the small, regular series that characterize a household budget (Chen et al., 2024). Hybrid and ensemble approaches that blend statistical and ML forecasters perform well on financial series (Sonkavde et al., 2023). What the literature establishes for BUDI is a clear division of labor: SARIMA's seasonal structure and small-sample interpretability make it the appropriate forecaster for monthly income and expense data, while ML/DL alternatives are treated as benchmarks to detect and avoid overfitting on shallow household histories.

### 3.4. Budget Optimization

Budget allocation is naturally modeled as a constrained optimization problem: distribute available income across expense categories, savings, and debt payments to maximize savings while honoring essential expenses and user preferences. Formalizing budgeting this way lets an application compute an optimal plan rather than rely on rules of thumb (De Zarzà et al., 2024; Yoganandham, 2025).

Constrained optimization frameworks for budgeting, which maximize savings across monthly expense categories given income and preferences, are the closest published analogue to BUDI's LP module (De Zarzà et al., 2024) <!-- VERIFY: source filename says 2023 but publication is 2024 (AI 5, 91–114); confirm before formal use -->. The research literature provides the mathematical backbone as well: when the parameters that constrain an optimization problem — such as future income — are unknown, a forecast must first be made, and end-to-end "predict + optimize" approaches train the forecasting and optimization stages together so that predicted parameters remain feasible under the true constraints (Hu et al., 2023). Portfolio and allocation studies add that optimization benefits from robust risk profiling of the user, since the constraint set differs meaningfully between saving- and debt-prone profiles (Sappa, 2024). Combined with the SARIMAX-forecast-to-optimizer evidence (Lu et al., 2025), this literature supports BUDI's design: SARIMA forecasts supply the income parameter, the LP solver maximizes savings within the user's budget constraints, and the constraint weights are personalized from the classification profile.

### 3.5. Anomalous Transaction Detection

Anomaly detection identifies transactions that deviate from the user's established spending patterns, which may indicate errors, fraud, or behavior the user should review. Detection approaches span statistical, heuristic, machine-learning, and deep-learning families, and the choice among them depends on whether the anomaly is a point deviation or a sequence pattern (Sankaewtong et al., 2025; Zhang et al., 2023).

BUDI's anomaly module uses an interquartile-range (IQR) statistical detector: it computes quartiles of recent transaction amounts per category and flags values beyond a calibrated whisker as anomalous. Three strands of literature support this choice. First, statistical methods remain a recognized, if underrepresented, family in transaction anomaly detection, which means the IQR approach occupies a legitimate but less-populated research space that this study contributes to (Sankaewtong et al., 2025). Second, IQR and z-score procedures are standard outlier logic in financial data pipelines, establishing that quartile-based screening is a credible foundation for transaction screening (Begum, 2025; Chen & Tan, 2025). Third, the anomaly-detection literature emphasizes that static thresholds fail under distributional shift: detectors whose thresholds are not updated generate rising false positives as user behavior evolves, while dynamically calibrated thresholds reduce false alarms and preserve recall (A. Huang et al., 2025; Zhong, 2025). Benchmarks of state-of-the-art detectors also show that no single method dominates, and heavier machine-learning detectors trade their small accuracy gains against speed, data, and explainability — all of which matter on-device (Zhang et al., 2023).

For BUDI, the findings are direct: the IQR detector provides a fast, explainable, data-efficient baseline for flagging unusual spending, and it must be paired with periodic recalibration — such as recomputing quartiles on a rolling window of the user's own history — to avoid the degradation documented for static statistical thresholds. This requirement connects the anomaly module to the drift-aware design principles reviewed for classification.

### 3.6. Model Performance Metrics

The four modules are evaluated with the metrics conventional to their tasks. For the classification module, accuracy, precision, recall, and F1 measure how correctly users are placed in savings-, debt-, and spending-profile categories, and are the standard reporting metrics in the reviewed classification and concept-drift studies (Chikoore et al., 2026; Shaha & Gavekar, 2025; Zhang & Hou, 2026). For the forecasting module, the symmetric MAPE, RMSE, and MAE compare predicted against actual income and expenses, and these are the dominant forecast-evaluation metrics in the budget-forecasting literature (Kara & Şengüler, 2025; Lu et al., 2025). For the optimization module, the objective value — savings achieved — is measured against the LP solution's guarantee, with constraint feasibility as the primary validity check (Hu et al., 2023; Lu et al., 2025). For the anomaly module, precision, recall, F1, and the false-positive rate measure how often the detector flags real anomalies without overwhelming the user with noise, and dynamic-threshold studies report exactly these metrics in evaluating calibrated detectors (A. Huang et al., 2025; Shaha & Gavekar, 2025; Zhong, 2025). Where user segmentation and clustering complement the classifier, separation metrics such as the Silhouette coefficient and Davies–Bouldin index complete the picture (Salminen et al., 2023). Reporting all four module families on their own metrics — rather than a single global accuracy — reflects how the reviewed literature evaluates heterogeneous financial-model stacks.

---

## 4. System Methodology

This section explains how BUDI itself is being developed, rather than describing what software engineering or machine learning in general are. The project follows an agile, iterative development process in which the application is built, tested, and refined against feedback in short cycles; this matches the recommended practice for personal finance management systems, where iterative development and continuous user feedback are explicitly advised (Yadav et al., 2026).

The machine-learning workstream follows the standard pipeline that the reviewed literature assumes: data collection, preprocessing, model training, validation, and deployment (Chen et al., 2024). For BUDI, collection means recording the user's actual transactions; preprocessing converts those transactions into the category, frequency, and trend features described in Section 3.1; training fits the SVM, SARIMA, LP, and IQR modules on the user's history; validation uses out-of-sample checks to confirm generalization; and deployment embeds the trained modules in the mobile application. Model selection follows the accuracy-interpretability trade-off established in Section 3.6, preferring the transparent statistical and classical models that suit on-device, personal-scale data (Reyes et al., 2024).

A dedicated survey component feeds the requirements of the personalization layer. The public user-expectations survey collects preferences, pain points, and expectations from prospective Filipino users, and the resulting evidence is used to set feature priorities before each development cycle — the same evidence-based practice that separates BUDI from speculative feature selection. The application is implemented as a mobile-first product using a modern technology stack — React Native (Expo) on the client, an Express/TypeScript API, and a Supabase backend — with the four model families integrated through a lightweight ML service. This stack, and the split of concerns between the application and the model service, was chosen because it allows each model to be trained and improved independently while the app consumes their outputs through standardized interfaces. The development is carried out cross-functionally by a small team spanning application development, data science, and technical documentation, reflecting the interdisciplinary collaboration that intelligent-finance systems require (R. Huang et al., 2025).

---

## 5. System Evaluation

### Metrics

System evaluation for BUDI measures not only that the models perform well but that the application is usable, accepted, and demonstrably improves the user's savings and debt — an improvement the study must be able to measure. Perceived usefulness, defined as the user's belief that the system improves their financial management, is the first such measure (Rane et al., 2024). Performance expectancy, the user's expectation that the system enhances financial outcomes, is the second, and facilitating conditions — the availability of the technical infrastructure, training, and support needed to use the system — form the third (Rane et al., 2024). Together these constructs, drawn from established technology-acceptance literature, are applied to BUDI through a survey instrument that asks prospective users about the usefulness, expected benefit, and ease of use of the application.

### Models and Theories for Evaluation

The Technology Acceptance Model (TAM) evaluates technology adoption from perceived usefulness and perceived ease of use, which shape attitudes, intentions, and actual use (Rane et al., 2024; Santiago et al., 2025). The Unified Theory of Acceptance and Use of Technology (UTAUT) extends this with social influence, facilitating conditions, and related factors, providing a more comprehensive account of acceptance in diverse consumer contexts (Rane et al., 2024). Both frameworks have been applied to financial-technology adoption, including intelligent and AI-based financial services, and their constructs appear directly in the acceptance literature's clusters around perceived usefulness, ease of use, and user acceptance (Rane et al., 2024). For a system evaluation, TAM/UTAUT are complemented by usability measurement — the System Usability Scale (SUS), a widely used instrument for judging perceived usability — and by software-quality models such as ISO/IEC 25010, which frame functional suitability, reliability, and usability as explicit quality characteristics (Brooke, 1996; ISO/IEC, 2011). BUDI's evaluation plan therefore combines model-performance metrics (Section 3.6), a SUS-based usability assessment, and a TAM/UTAUT acceptance survey, so that both the models and the product are judged with established instruments.

---

## Synthesis

The reviewed literature converges on several points that directly shape BUDI. First, savings and debt in the Philippines are heavily influenced by the user's demographic, social, psychological, and economic circumstances: income instability, household obligations, self-control, and financial literacy jointly determine whether a Filipino saves, borrows, or struggles to budget (Abila & Ulibas, 2026; Bulan & Nemino, 2025; Ganong et al., 2025; Wang-Ly & Newell, 2023). Philippine surveys show that saving is rare, borrowing is common, emergency funds are scarce, and financial literacy is low, establishing an urgent and measurable need for a tool that improves savings and debt (BSP, 2023, 2025).

Second, the technology to meet that need already exists in pieces. Intelligent finance applications have demonstrated the value of expense classification, smart budgeting, forecasting, and anomaly alerts (DSouza et al., 2026; Yadav et al., 2026), and the relevant computational approaches are mature: SVM classification with concept-drift adaptation (Abdullahi et al., 2025; Chikoore et al., 2026), SARIMA seasonal forecasting (DSouza et al., 2026; Kara & Şengüler, 2025), constrained budget optimization (De Zarzà et al., 2024; Lu et al., 2025), and statistical anomaly detection with dynamic threshold calibration (A. Huang et al., 2025; Zhong, 2025; Zhang et al., 2023).

Third, existing systems each solve part of the problem but not the whole. Foundational frameworks for intelligent personal finance management enumerate the same classification–forecasting–optimization–anomaly stack as BUDI, but they remain architectural proposals without implementation or evaluation (De Zarzà et al., 2024; Yadav et al., 2026). Multi-agent wealth advisors deliver personalization and explainability but target investment portfolios rather than everyday savings and debt (R. Huang et al., 2025). Budget-management apps provide tracking and risk classification but do not integrate the four-model stack (Ghonaim & El-Sharawy, 2025). Reviewed systems therefore demonstrate the components BUDI needs while leaving the integration itself open.

Fourth, this integration exposes the research gap. Most reviewed intelligent-finance literature originates in Western, developed-economy, or investment-focused contexts, with limited attention to Filipino mass-market users and their specific savings and debt realities (BSP, 2023, 2026; Cumaio et al., 2026). Concept drift in personal spending profiles is only beginning to be addressed in adaptive credit-scoring work, and it has not been studied for household budgeting classifiers in a developing-economy mobile application (Abdullahi et al., 2025; Chikoore et al., 2026). The literature is also thin on the simultaneous, personalized combination of profile classification, seasonal forecasting, budget optimization, and anomaly detection within a single platform — the exact configuration BUDI proposes (DSouza et al., 2026; Yadav et al., 2026).

Finally, the proposed study responds to this gap by developing BUDI: a Filipino-focused, mobile-first application integrating SVM profile classification, SARIMA forecasting, LP-based budgeting, and IQR anomaly detection, personalized to each user's financial profile and evaluated with model metrics, usability instruments, and acceptance frameworks that the literature endorses (Brooke, 1996; Rane et al., 2024). In doing so, the study contributes a contextualized implementation of a four-model intelligent finance architecture to a population the current literature largely leaves unmodeled.

---

## Tables on Existing Literature

The table below compares the intelligent finance management systems reviewed in this chapter, following the guideline's comparison dimensions (purpose, target users, major features, technologies/models, results, strengths, limitations, relevance to BUDI).

| System / Study | Purpose | Target users | Major features | Technologies / models | Results / findings | Strengths | Limitations | Relevance to BUDI |
|---|---|---|---|---|---|---|---|---|
| Wealth-Voyager (R. Huang et al., 2025) | Intelligent wealth management advisory | Individual investors | Multi-agent advisory, strategy allocation, explainable conversational guidance | LLM-based multi-agent framework (AlphaForge + DualAdvisor) | Better risk-adjusted returns in a six-week pilot; improved user engagement and trust | Personalization and transparency by design; user-tested | Investment portfolio focus; short evaluation window; small user study | Source of the personalization and explainability principles BUDI applies to savings guidance |
| Intelligent PFM System / IPFMS (Yadav et al., 2026) | Smart budgeting and real-time expense tracking | General personal finance users | Expense classification, budget forecasting, anomaly alerts | Logistic regression / RF / SVM classifiers; ARIMA, Prophet, LSTM forecasters; K-Means/DBSCAN/isolation-forest anomaly | None reported (architectural proposal) | Explicitly assembles the same model stack as BUDI | No implementation or evaluation; low-tier venue | Direct architectural blueprint for BUDI's four-module design |
| RNN Budget Management App (Ghonaim & El-Sharawy, 2025) | Mobile budget and risk management | Mobile app users (Arabic/English) | Transaction risk classification, budget management | RNN classifier over Kaggle financial-transaction data | 97.45% classification accuracy | Mobile-first; high accuracy on real transaction data | Single model; no concept drift; categories are derived | Validates on-device transaction classification in a budget app |
| Constrained Budgeting Framework (De Zarzà et al., 2024) | Savings-maximizing budget allocation | Individual and cooperative households | Constraint-based budget optimization with LLM guidance | Constraint-based optimization / LP-style allocation model | Demonstrates feasible savings-maximizing plans (qualitative) | Formalizes budgeting as optimization — closest analogue to BUDI's LP module | No quantitative evaluation; LLM integration informal; cooperative scale exceeds BUDI scope | Supports the LP-based budgeting module and its constraint formulation |
| SARIMAX + Constrained Optimizer (Lu et al., 2025) | Demand forecast then constraint-aware budgeting | Marketing/budget planners | Category demand forecasting feeding a constrained optimization stage | SARIMAX model + constrained optimizer; Monte Carlo stress testing | ~2.85% MAPE on total demand; point forecasts can violate constraints | Exact BUDI pattern: forecast-then-optimize; error-aware | Not a consumer mobile app; enterprise framing | Justifies the SARIMA-to-LP pipeline used in BUDI |
| BUDI (proposed) | Personalized savings-and-debt improvement for Filipinos | Filipino individuals with irregular or fixed incomes | Profile classification, expense tracking, income/expense forecast, LP budget plan, emergency-fund goals, debt repayment, anomaly alerts, personalized insights | SVM classification w/ concept drift; SARIMA forecasting; LP optimization; IQR anomaly detection | To be established by model metrics, SUS, and TAM/UTAUT evaluation | Single integrated, personalized platform for the four model families; localized to Philippine incomes, obligations, and savings norms | Not yet evaluated; depends on available transaction data | The present study |

---

## Research Gaps

The following gaps are drawn from, and supported by, the reviewed literature.

| Type of Gap | Gap identified | Supported by |
|---|---|---|
| Contextual Gap | Most intelligent finance-management research targets developed economies and investment-focused users; little work models Filipino mass-market savings and debt behavior within an application | Cumaio et al., 2026; BSP, 2023, 2026 |
| Integration Gap | Existing systems implement classification, forecasting, optimization, or anomaly detection separately; limited work integrates all four in one personalized platform | Yadav et al., 2026; DSouza et al., 2026; R. Huang et al., 2025 |
| Technological Gap | Prediction modules seldom feed a constraint-aware budgeting optimizer; forecast-then-optimize pipelines for personal budgets are rare outside enterprise marketing budget settings | Lu et al., 2025; De Zarzà et al., 2024 |
| Methodological Gap | Concept drift in personal spending-profile classification is studied in credit-scoring contexts but not for household budgeting classifiers in mobile applications | Abdullahi et al., 2025; Chikoore et al., 2026 |
| Feature Gap | Reviewed systems that detect anomalous transactions rely on heavier ML detectors; a fast, explainable, statistically grounded detector that recalibrates to the user's own history is not commonly provided | A. Huang et al., 2025; Zhong, 2025; Zhang et al., 2023 |
| Data Gap | Philippine household financial modeling is limited to survey-based classification (e.g., wealth quintiles); transaction-level datasets tied to a deployed Filipino mobile application are absent | Salvador, 2024; BSP, 2023 |
| Evaluation Gap | Few intelligent finance applications for developing economies are evaluated simultaneously with model metrics, usability (SUS), and acceptance frameworks (TAM/UTAUT) | Rane et al., 2024; Santiago et al., 2025 |

---

## Conceptual Model of the Study

The conceptual model summarizes the major components of the study and how they relate. An Input–Process–Output (IPO) model is used because the study is a system-development project whose components are knowledge, data, software and hardware inputs; a sequence of processes; and the developed system as output.

### IPO Diagram

```
INPUT                                         PROCESS                                        OUTPUT
Knowledge Requirements                        Requirements Analysis                          Developed [BUDI]:
  User requirements (survey)                    Personalization target-user                    Personalized Intelligent
  Financial domain concepts                     profile definition                             Finance Management App
  Behavioral and psychological factors        Algorithm / Model Implementation                with expected capabilities:
  Business and design rules                     - SVM profile classification                   - Expense & income tracking
Data Requirements                               - SARIMA income/expense forecasting            - Budget allocation (LP-based)
  Transaction records (income, expense)         - LP-based budgeting                            - Smart alerts for anomalies
  Time-series history                           - IQR anomaly detection                         - Forecasts of future income
  Budget states and goals                      System Analysis and Design                       and expenses
  Synthetic personas for development            - Mobile-first app architecture                - Personalized insights and
  Government survey context (BSP/FIES)          - Model-service integration                      actionable advice
Software Requirements                          Development
  Python (modeling) / React Native (Expo)       - Iterative development cycles
  Express/TypeScript API, Supabase             Testing
  scikit-learn / statsmodels / LP solver        - Model performance metrics
Hardware Requirements                           - Unit and integration tests
  Mobile devices / server resources            Evaluation
  Development workstations                      - SUS usability assessment
                                                - TAM/UTAUT acceptance survey
                                                - Savings-and-debt impact measurement
```

### Discussion of the Conceptual Framework

The Input box assembles what the study needs before any process begins. Knowledge requirements capture the user requirements gathered through the public user-expectations survey, the personal-finance domain concepts and behavioral determinants reviewed in this chapter, and the design rules derived from the topical outline. Data requirements specify the raw materials of the computational models: the user's recorded transactions; the time-series history of income and expenses that drives the SARIMA forecaster; period-end budget states and savings/debt goals that drive the LP optimizer; synthetic personas that let models be trained and tested before sufficient real data accumulate; and government surveys such as the BSP consumer surveys that provide the macro context validating the profiles. Software and hardware requirements bound the technical implementation — Python-based modeling tooling for the model service, React Native (Expo) for the mobile client, an Express/TypeScript API with a Supabase backend, and the devices and workstations used to build and run the system.

The Process box sequences the major activities of the study. Requirements analysis converts the knowledge inputs into a fixed personalization target-user profile and feature set. Algorithm/model implementation develops the four computational modules — the SVM profile classifier, the SARIMA forecaster, the LP budget optimizer, and the IQR anomaly detector — consistent with the model-selection and metric evidence reviewed in Sections 3 and 6. System analysis and design then organizes these modules into the application's architecture, separating the app from the model service. Development proceeds in iterative cycles, and testing validates both the models (through their performance metrics) and the application (through integration and acceptance checks). Finally, evaluation applies the SUS questionnaire, the TAM/UTAUT instruments, and the savings-and-debt impact measurement to judge the finished system.

The Output box is the primary product — the developed BUDI application — together with its expected capabilities: accurate expense and income tracking; LP-optimized budget allocations that maximize savings under the user's constraints; smart anomaly alerts that flag unusual transactions without overwhelming the user; forecasts of future income and expenses from the SARIMA module; and personalized insights that convert the user's own data into actionable, memory-respectful guidance. The diagram is relationship-preserving: each output capability traces to a specific input (for example, forecasts trace to the time-series history inputs, and personalized budgets trace to the behavioral and goal inputs) mediated by the corresponding process. This model therefore holds the study together: the literature reviewed in this chapter supplies the inputs and the process rationale, and the evaluated application is the output that closes the research gap identified in the synthesis.

---

## References

Abdullahi, M., Alhussian, H., Aziz, N., Abdulkadir, S. J., Baashar, Y., Alashhab, A. A., & Afrin, A. (2025). A systematic literature review of concept drift mitigation in time-series applications. *IEEE Access, 13*, 119387–119418. https://doi.org/10.1109/ACCESS.2025.3587231

Abila, J. P., & Ulibas, R. (2026). Analyzing the financial management practices and resilience of online freelancers in Laguna amid digital platform taxation. *International Journal of Multidisciplinary Educational Research and Innovation, 4*(2), 118–131.

Agrawal, R., Hamdare, S., & Khanna, A. (2025). Analyzing and rewarding credit card spending habits in India: A machine learning approach. *International Journal of Computational Intelligence Systems, 18*, Article 165. https://doi.org/10.1007/s44196-025-00899-0

Bai, R. (2023). Impact of financial literacy, mental budgeting and self control on financial wellbeing: Mediating impact of investment decision making. *PLoS ONE, 18*(11), Article e0294466. https://doi.org/10.1371/journal.pone.0294466

Bangko Sentral ng Pilipinas. (2023). *Financial inclusion in the Philippines dashboard: As of fourth quarter 2023*. Bangko Sentral ng Pilipinas.

Bangko Sentral ng Pilipinas. (2025). *Bangko Sentral ng Pilipinas annual report 2025*. Bangko Sentral ng Pilipinas.

Bangko Sentral ng Pilipinas. (2026). *Consumer expectations survey report: 2nd quarter 2026*. Department of Economic Statistics, Bangko Sentral ng Pilipinas.

Begum, M. (2025). Machine learning in financial risk and behavior analysis: Predictive insights on bankruptcy, fraud, and consumer trends in the USA. *Journal of Data & Digital Innovation, 2*(1), 36–54.

Brooke, J. (1996). SUS: A "quick and dirty" usability scale. In P. W. Jordan, B. Thomas, B. A. Weerdmeester, & I. L. McClelland (Eds.), *Usability evaluation in industry* (pp. 189–194). Taylor & Francis.

Bulan, P. J., & Nemino, M. R. (2025). The interplay of behavioral intention on the relationship between self-control and saving behavior among MSME business owners. *International Journal of Management Studies and Social Science Research, 7*(2), 139–150. https://doi.org/10.56293/IJMSSSR.2025.5518

Chen, J., Chen, T., Wang, Y., & Wang, L. (2024). A survey of time series data forecasting methods based on deep learning. *Journal of Basic and Applied Research International, 30*(6), 140–157.

Chen, S., & Tan, W. (2025). LSTM-based consumer behavior prediction model research. In *Proceedings of the 2025 2nd International Conference on Digital Economy and Computer Science (DECS 2025)*. ACM. https://doi.org/10.1145/3785706.3785906

Chikoore, R., Ojo, S. O., & Kogeda, O. P. (2026). Adaptive credit scoring model with concept drift detection and adaptation technique for a dynamic environment. *IEEE Access, 14*, 90371–90405. https://doi.org/10.1109/ACCESS.2026.3703181

Claro, D. M. L., & Noval, J. E. G. (2025). The regressors of financial well-being among LGU employees in Davao del Norte. *ISRG Journal of Economics & Business Management, 3*(6), 171–187. https://doi.org/10.5281/zenodo.17775590

Cowan, N. (2001). The magical number 4 in short-term memory: A reconsideration of mental storage capacity. *Behavioral and Brain Sciences, 24*(1), 87–114. https://doi.org/10.1017/S0140525X01003922

Cruz, M. A. T. D., Jurada, P. H. G., Recreo, C. R., Mandigma, M. B. S., & Magbata, E. V. S. (2026). Dependence of Filipino young professionals' well-being on their investing years and income in the National Capital Region. *Review of Integrative Business and Economics Research, 15*(2), 902–919.

Cumaio, S., Serrasqueiro, Z., & Madaleno, M. (2026). Linking financial literacy and behavioural finance to saving and debt behaviours: A literature review of global and developing economy contexts. *Journal of Risk and Financial Management, 19*(6), Article 425. https://doi.org/10.3390/jrfm19060425

Danahy, R., Lillard, D., Loibl, C., & Montalto, C. P. (2024). Financial stress among college students: New data about student loan debt, lack of emergency savings, social and personal resources. *Journal of Consumer Affairs, 58*(2), 692–709. https://doi.org/10.1111/joca.12581

De Zarzà, I., de Curtò, J., Roig, G., & Calafate, C. T. (2024). Optimized financial planning: Integrating individual and cooperative budgeting models with LLM recommendations. *AI, 5*(1), 91–114. https://doi.org/10.3390/ai5010006

Dheepiga, S., & Sivakumar, N. (2025). How financial literacy influences budgeting, investment, and savings behaviors. *International Research Journal of Business Studies, 18*(1), 101–114.

DSouza, M., Bhegade, P., Bhalekar, P., & Bhavsar, Y. (2026). A comprehensive review of machine learning techniques for intelligent personal finance management systems. *[Preprint, P.E.S Modern College of Engineering, Pune].* <!-- VERIFY: preprint-style review; confirm venue -->

Encarnacion, M. J. G., & Vecina, R. A. P. (2025). Improving financial performance through financial literacy, good financial practice and fintech adoption. *Divine Word International Journal of Management and Humanities, 4*(2), 1688–1707.

Erno, G. Y. L., & Grefalde, J. Q. (2026). Behavioral and psychological drivers of sustainable saving and financial resilience among community households. <!-- VERIFY: source venue string appears anomalous; confirm journal and volume/issue -->

Esperanza, D. N., Bithay, L. L., Jesus, J. B., Ople-Alviola, C., Sumilhig, J. M., & Basilisco, G. L. (2025). Digital lending efficacy on debt management of wage earners. *ASEAN Journal of Management & Innovation, 12*(2), 111–127.

Francisco, A., Legal, G., & Legal, F. (2026). Causes of salary loan dependency: Basis for strengthening financial literacy program. *International Journal of Multidisciplinary Educational Research and Innovation, 4*(1), 705–728.

Ganong, P., Noel, P. J., Patterson, C., Vavra, J. S., & Weinberg, A. (2025). *Earnings instability* (NBER Working Paper No. 34227). National Bureau of Economic Research.

Ghonaim, W. A., & El-Sharawy, E. E. (2025). An intelligent budget management mobile application based on a recurrent neural network. *International Journal of Theoretical and Applied Research, 4*(2), 840–852. https://doi.org/10.21608/IJTAR.2025.427658.1148

Hajj, M. E., & Hammoud, J. (2023). Unveiling the influence of artificial intelligence and machine learning on financial markets: A comprehensive analysis of AI applications in trading, risk management, and financial operations. *Journal of Risk and Financial Management, 16*(10), Article 434. https://doi.org/10.3390/jrfm16100434

Hu, X., Lee, J. C. H., & Lee, J. H. M. (2023). Two-stage predict+optimize for mixed integer linear programs with unknown parameters in constraints. In *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*.

Huang, A., Zhang, X., Wang, Y., Tsai, S., Zhou, P., & Chen, L. (2025). Dynamic calibration of decision thresholds for financial anomaly detection: Verification with payment platform information and data. *Journal of Global Information Management, 33*(1). https://doi.org/10.4018/JGIM.395852

Huang, R., Zhao, Z., Chen, S., Wu, X., & Zhao, J. L. (2025). Wealth-Voyager: Navigating intelligent wealth management with a multi-agent framework. In *Proceedings of the 2025 International Conference on Generative Artificial Intelligence for Business (GAIB 2025)*. ACM. https://doi.org/10.1145/3766918.3766944

ISO/IEC. (2011). *ISO/IEC 25010:2011 — Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models*. International Organization for Standardization.

Kara, B., & Şengüler, H. (2025). A comparative analysis of budget forecasting methods: A systematic literature review covering the 1983–2024 period. *Public Budgeting & Finance*. https://doi.org/10.1111/pbaf.70008

Lu, Y., Zhou, H., & Zhang, Y. (2025). A constrained, data-driven budgeting framework integrating macro demand forecasting and marketing response modeling. *Journal of Technology Informatics and Engineering, 4*(3), 493–520. https://doi.org/10.51903/jtie.v4i3.466

Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. *Psychological Review, 63*(2), 81–97. https://doi.org/10.1037/h0043158

Prakoso, T., & Apriliani, R. (2024). Budgeting and saving effectiveness as the main pillar of sustainable personal financial management. *Indonesian Journal of Islamic Economics and Finance, 4*(2), 257–272. https://doi.org/10.37680/ijief.v4i2.6187

Rane, N. L., Choudhary, S. P., & Rane, J. (2024). Acceptance of artificial intelligence technologies in business management, finance, and e-commerce: Factors, challenges, and strategies. *Studies in Economics and Business Relations, 5*(2), 23–44. https://doi.org/10.48185/sebr.v5i2.1333

Reyes, J. M., Santos, L. P., & Perez, A. (2024). A comparative analysis of machine learning models for predictive analytics in finance. *International Journal of Applied Mathematics and Computing, 1*(1), 14–20. https://doi.org/10.62951/ijamc.v1i1.3

R Singh, S. S., & Singh, A. K. (2025). Digital persona modeling for context-aware financial decisioning. *International Journal of Research in Multidisciplinary Technology, 1*(4), 1–14.

Salminen, J., Mustak, M., Sufyan, M., & Jansen, B. J. (2023). How can algorithms help in segmenting users and customers? A systematic review and research agenda for algorithmic customer segmentation. *Journal of Marketing Analytics, 11*, 677–692. https://doi.org/10.1057/s41270-023-00235-5

Salvador, E. L. V. (2024). Use of boosting algorithms in household-level poverty measurement: A machine learning approach to predict and classify household wealth quintiles in the Philippines. *[Preprint submitted to Elsevier].* <!-- VERIFY: preprint; no DOI/venue confirmed -->

Samli, F. B., Zaini, Z., & Yusof, K. S. (2026). A bibliometric analysis of how financial behaviour drives effective debt management. *Labuan Bulletin of International Business & Finance, 24*(1), 114–129.

Sankaewtong, K., Kim, T., Tessone, C. J., & Ikeda, Y. (2025). SoK: Advances in anomaly detection techniques for cryptoasset transactions. *IEEE Access, 13*, 202576–202602. https://doi.org/10.1109/ACCESS.2025.3636560

Santiago, R. L. T., Villarica, M. V., & Bernardino, M. P. (2025). Budget and financial management information system for public elementary schools: Analytics and predictive insights for MOOE allocation using linear regression. *International Journal of Advanced Research in Computer Science, 16*(3), 128–150.

Sappa, A. (2024). AI based portfolio optimization and customer risk profiling in fintech platforms. *Research Briefs on Information & Communication Technology Evolution, 10*, Article 11. https://doi.org/10.69978/rebicte.v10i.205

Shaha, P., & Gavekar, V. (2025). Enhancing online fraud detection: Leveraging machine learning and behavioral indicators for improved accuracy and real-time detection. *EPJ Web of Conferences, 328*, Article 01003. https://doi.org/10.1051/epjconf/202532801003

Sohilauw, M. I., Rosdiana, Arifin, A. H., Nasir, & Yunus, M. K. (2026). Income, saving behavior, and household financial decision-making: A moderated-mediation analysis of behavioral and economic factors in Indonesia. *Journal of Economics, Entrepreneurship, Management Business and Accounting, 4*(4), 1–22. https://doi.org/10.61255/jeemba.v4i4.844

Sonkavde, G., Dharrao, D. S., Bongale, A. M., Deokate, S. T., Doreswamy, D., & Bhat, S. K. (2023). Forecasting stock market prices using machine learning and deep learning models: A systematic review, performance analysis and discussion of implications. *International Journal of Financial Studies, 11*(3), Article 94. https://doi.org/10.3390/ijfs11030094

Wang-Ly, N., & Newell, B. R. (2023). *How income volatility influences saving decisions: Evidence from the lab* (SSRN Working Paper No. 4509925). https://ssrn.com/abstract=4509925

Yadav, S., Kumar, V., & Maurya, A. (2026). Intelligent personal finance management system for smart budgeting and real-time expense tracking: Design and development. *International Scientific Journal of Engineering and Management, 5*(4). https://doi.org/10.55041/ISJEM06330

Yang, J. (2024). Study of an adaptive financial recommendation algorithm using big data analysis and user interest pattern with fuzzy K-means algorithm. *International Journal of Computational Intelligence Systems, 17*, Article 310. https://doi.org/10.1007/s44196-024-00719-x <!-- VERIFY: methodological precedent for adaptive user clustering/interest patterns; confirm exact match before formal use -->

Yang, T., Xin, Q., Zhan, X., Zhuang, S., & Li, H. (2024b). Enhancing financial services through big data and AI-driven customer insights and risk analysis. *Journal of Knowledge Learning and Science Technology, 3*(3), 53–62. https://doi.org/10.60087/jklst.vol3.n3.p53-62

Yeo, K. H. K., Lim, W. M., & Yii, K. J. (2023). Financial planning behaviour: A systematic literature review and new theory development. *Journal of Financial Services Marketing, 29*, 979–1001. https://doi.org/10.1057/s41264-023-00249-1

Yoganandham, G. (2025). Mastering economic and financial sources with reference to budgeting, savings, early investing, debt management and the power of financial planning — A comprehensive analysis. *Degres Journal, 10*(1), 25–40.

Yuttama, F. R. (2025). Behavioral shifts in digital finance: How e-payment influences consumer spending and financial literacy. *Journal of Management and Entrepreneurship Research, 6*(4), 358–371. https://doi.org/10.34001/jmer.2025.12.06.4-80

Zhang, A., Deng, S., Cui, D., Yuan, Y., & Wang, G. (2023). An experimental evaluation of anomaly detection in time series. *Proceedings of the VLDB Endowment, 17*(3), 483–496. https://doi.org/10.14778/3632093.3632110

Zhang, H., & Hou, Y. (2026). Consumer behavior data mining and analysis using machine learning algorithms. *Procedia Computer Science, 281*, 1463–1468.

Zhang, Z., & Lu, M. (2026). Artificial intelligence-driven transformation in financial technology: Applications, agents and challenges. *Engineered Science, 41*, Article 2245. https://doi.org/10.30919/es2245

Zhong, M. (2025). Adaptive anomaly detection threshold for financial data quality monitoring based on time series features. In *Proceedings of the International Conference on Advanced and Intelligent Computing Systems (AICSS 2025)*. ACM. https://doi.org/10.1145/3776759.3776850