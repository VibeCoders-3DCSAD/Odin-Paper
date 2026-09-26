# Chapter 2: Review of Related Literature and Studies (V3.0)

> **Status of this draft**
>
> - Working mirror of `google-drive/chapter-2/GROUP4 - CHAPTER 2 - V3 - 09.26.26.docx`, the
>   newest Chapter 2 on Drive. Supersedes the V2.0 draft of 09.15.26.
> - Scoped to `google-drive/topical-outline/GROUP4 - TOPICAL OUTLINE - V4 - 09.26.26.docx`.
>   The V4 outline and this V3 chapter were revised together on 09.26: the document's own table
>   of contents is the V4 leaf list, so the structure below already matches the current outline
>   and needed no re-ordering.
> - Project identity changed to **BUDGIE** in this revision, matching Chapter 1 V6
>   (`GROUP4 - CHAPTER 1 - V6 - 09.24.26.docx`) and Topical Outline V4. The V3 `.docx` body
>   still read **TAYA** in all 19 places; those are corrected here. See "Open items" below.
> - **Citation audit applied.** Every author-date citation in the V3 body was resolved against
>   the BUDI-Literature corpus (91 papers). 15 of 20 resolved cleanly, 1 was corrected, 3 are missing
>   from the corpus and carry a `SOURCE NEEDED` marker.
> - Citation policy: APA 7th edition. Nothing is cited from an unverified identity.
> - Figure 1 (Conceptual Model) is a placeholder: the diagram lives in the `.docx` media folder
>   and has not been exported to this repository.

---

## Corrections applied to the V3 body

| # | V3 `.docx` said | Corrected to | Why |
|---|---|---|---|
| 1 | TAYA (19 occurrences) | BUDGIE | Chapter 1 V6 and Topical Outline V4 both adopted BUDGIE; the V3 body was not updated when the project was renamed. |
| 2 | Huang et al. (2025) (3 occurrences) | Huang et al. (2025) | Page 1 of the source lists Anzhong Huang as sole author. |
| 3 | De Zarzà et al. (2024) | de Zarzà et al. (2024) | APA lowercases the particle in a surname. Citation year was already correct; the corpus stem was wrong and has been fixed. |
| 4 | (no reference list) | References section added | The V3 `.docx` had no References section at all. |

---

## Open items for the adviser

1. **Project identity is inconsistent across Drive.** Chapter 1 V6 is itself only partly
   updated: its title page and introduction say BUDGIE, but its Scope and Limitations section
   still describes "the development of BUDI" using **SVM** for profile classification, which
   Outline V4 replaced with a **rule-based** classifier. This chapter follows V4 and uses
   rule-based. Chapter 1 needs a matching pass.
2. **ISO/IEC 25010 characteristic list disagrees three ways.** This chapter and Chapter 1 V6
   both list six characteristics (functional suitability, performance efficiency, reliability,
   security, portability, usability). The fielded instrument
   `GROUP4 - ISO 25010 - V1 - 09.15.2026.docx` instead uses five (it omits portability and
   substitutes maintainability) and files the usability sub-characteristics under performance
   efficiency. The instrument also still carries "Pawpid" pet-adoption wording, a 1-4 SUS scale
   instead of 1-5, and no edition year. The instrument must be rebuilt before fielding, and the
   characteristic list settled once across Chapters 1, 2, and the instrument.
3. **The SARIMA section rests on a single source.** Dasmariñas et al. (2024) is cited seven
   times and is not in the corpus. The adviser's standard for a core algorithm is six to seven
   sources, so this section needs corroboration even once that paper is acquired.

---

# CHAPTER II

## Review of Related Literature and Studies

This chapter presents the literature and studies relevant to the development of BUDGIE. The review examines concepts, technologies, existing systems, and computational approaches that provide the theoretical and empirical foundation of the study.

## Personal Financial Management

Personal financial management (PFM) refers to the systematic process of managing individual income, expenses, savings, and debt to achieve financial goals and maintain financial well-being. According to Yoganandham (2025), financial planning is an indispensable part of modern life, enabling individuals to navigate financial complexities, optimize resource allocation, and safeguard their financial well-being against economic uncertainties. The practice encompasses budgeting, savings management, debt management, and investment planning, all of which contribute to long-term financial security and resilience.

The importance of personal financial management extends beyond individual benefit to broader economic stability. Cumaio et al. (2026) emphasized that individual decisions regarding savings and debt are particularly relevant in developing economies where household financial vulnerability is more pronounced. Their review of global and developing economy contexts established that financial literacy and behavioral finance factors significantly influence saving and debt behaviors, with implications for household financial stability and economic participation. This finding underscores the need for accessible financial management tools that support informed decision-making among vulnerable populations.

In the Philippine context, financial management challenges are compounded by economic pressures and limited access to formal financial services. The Bangko Sentral ng Pilipinas (2026) reported that Filipino consumers in Q2 2026 were less likely to save, possibly because rising prices prompted them to allocate a larger share of their income on expenditures. Households appeared to be more cautious, less inclined to borrow in the next 12 months while still expecting higher spending on basic needs. These results indicate that households are prioritizing essential goods while cutting back on discretionary purchases as they become less optimistic about their financial situation, highlighting the critical need for tools that help Filipinos manage limited resources more effectively.

## Financial Planning

Financial planning is a comprehensive process that involves assessing one's current financial situation, defining financial goals, developing strategies to achieve those goals, and monitoring progress over time. Yoganandham (2025) described financial planning as a systematic approach that enhances the ability to make sound economic decisions, fostering resilience against economic uncertainties and ensuring intergenerational wealth transfer. The process encompasses multiple domains including budgeting, savings, debt management, and investment, all of which must be coordinated to achieve optimal financial outcomes.

The theoretical foundation of financial planning behavior has been extensively examined in the literature. Yeo et al. (2023) conducted a systematic literature review and developed a new theory of financial planning behavior, identifying that financial planning is influenced by a combination of individual characteristics, environmental factors, and behavioral biases. Their review established that effective financial planning requires not only technical knowledge but also behavioral commitment and consistent execution. This finding has important implications for the design of financial management applications, suggesting that systems must support both analytical capabilities and behavioral adherence.

In the Philippine setting, Claro and Noval (2025) investigated the regressors of financial well-being among local government employees in Davao del Norte, finding that financial planning practices significantly influence financial well-being outcomes. Their study confirmed that individuals who engage in systematic financial planning report higher levels of financial satisfaction and security. These findings support the development of tools that facilitate and encourage systematic financial planning among Filipino users, particularly those with limited access to professional financial advice.

### Financial Planning Process

The financial planning process typically involves several sequential stages: assessing the current financial situation, establishing financial goals, developing a plan, executing the plan, and reviewing and monitoring progress. Yoganandham (2025) emphasized that each stage requires careful attention and that the process is iterative rather than linear, with reviews and adjustments occurring as circumstances change. The execution and adherence stage is particularly critical, as even well-designed plans fail without consistent implementation.

Cumaio et al. (2026) highlighted that adherence to financial plans is influenced by both individual self-control and environmental factors, with behavioral finance research demonstrating that individuals often struggle to maintain disciplined financial behaviors despite good intentions. Their review suggested that external support mechanisms, such as automated reminders and progress tracking, can improve adherence by reducing reliance on individual willpower. These findings support the integration of monitoring and feedback features in personal financial management applications.

### Financial Goals and Constraints

Financial goals represent the desired outcomes that financial planning seeks to achieve, ranging from short-term objectives such as building an emergency fund to long-term goals such as retirement savings or debt elimination. Yoganandham (2025) noted that effective financial planning requires clear goal definition with specific amounts, timelines, and priorities. The presence of multiple goals creates allocation challenges, as limited resources must be distributed across competing objectives.

Financial constraints represent the limitations within which financial planning must operate, including income levels, fixed expenses, debt obligations, and other commitments. de Zarzà et al. (2024) developed mathematical optimization models for individual and household financial planning, demonstrating that budget allocation can be formulated as a constrained optimization problem that maximizes goal achievement within available resources. Their approach incorporated multiple objectives and constraints, providing a framework for systematic allocation decisions that balance competing priorities.

### Problems in Financial Planning

Filipinos face persistent challenges in improving their savings and managing debt, with multiple factors contributing to financial vulnerability. The Bangko Sentral ng Pilipinas (2026) reported declining savings propensity among Filipino consumers, attributed to rising prices that force households to allocate larger shares of income to basic expenditures. This trend indicates that many Filipinos lack sufficient financial buffers to absorb economic shocks, increasing their vulnerability to financial distress.

Debt management presents particular challenges for Filipino households. Esperanza (2025) examined digital lending efficacy on debt management of wage earners, finding that access to credit without corresponding financial management capabilities can lead to debt accumulation and financial strain. Francisco et al. (2026) investigated causes of salary loan dependency, identifying that inadequate financial planning and limited emergency savings contribute to reliance on loans for routine expenses. These findings highlight the interconnected nature of savings and debt challenges, suggesting that effective interventions must address both dimensions simultaneously.

The gap between financial knowledge and financial behavior represents a significant challenge in personal financial management. Cumaio et al. (2026) noted that while financial literacy has improved in many developing economies, translating knowledge into consistent action remains problematic. Behavioral factors including present bias, loss aversion, and social influences can undermine financial planning efforts even among individuals with adequate financial knowledge. This gap between intention and behavior supports the development of tools that not only provide analytical support but also facilitate behavioral adherence through reminders, progress tracking, and accessible decision support. <!-- SOURCE NEEDED [DEY & AREFIN 2025]: cited for rule-based classification and household budget generation; not in the corpus. Candidate: Dey, S., & Arefin, M. S. (2025). Developing a rule-based system to recommend household budget. Journal of Information Systems Engineering and Management, 10(47s), 148-182. https://jisem-journal.com/index.php/journal/article/view/9230 (preprint: https://www.preprints.org/manuscript/202502.1315/v1) - acquire and ingest before submission. -->

## Personal Financial Management Applications

Personal financial management applications have emerged as tools to support individuals in managing their finances, offering features ranging from basic expense tracking to sophisticated financial planning capabilities. Alenazi and Sas (2023) evaluated budgeting apps and found that while the market has grown rapidly, most applications provide limited support for budgeting compared to tracking, with a significant gap between user needs and application capabilities. Their analysis identified that many apps prioritize transaction recording over proactive financial planning, limiting their potential to improve financial outcomes.

The rapid growth of financial management applications reflects increasing demand for accessible financial tools. Bitrián et al. (2021, as cited by Alenazi & Sas, 2023) noted that financial management apps supporting users to track expenses and create budgets have experienced rapid growth as one of the fastest growing categories of finance apps. However, the availability of tools does not necessarily translate to improved financial outcomes, as many applications lack the sophistication required to address complex financial challenges such as optimizing savings and debt simultaneously.

## Seasonality in Personal Finance

Seasonal variations in income and expenses present significant challenges for personal financial management, particularly in economies where consumption patterns exhibit strong seasonal fluctuations. Dasmariñas et al. (2024) investigated forecasting the impact of COVID-19 on household final consumption expenditure in the Philippines using SARIMA and historical quarterly HFCE data. Their study demonstrated that Philippine household consumption exhibits significant seasonal patterns that can be modeled and forecasted using time-series techniques. However, their research focused on aggregate household consumption rather than applying these patterns to personalized financial planning.

The importance of incorporating seasonality into financial planning is supported by consumption theory and empirical evidence. Seasonal patterns in consumption arise from multiple sources including cultural events, holiday spending, school calendars, and weather-related variations in needs. In the Philippine context, consumption patterns are influenced by factors such as the Christmas season, school enrollment periods, and agricultural cycles, creating predictable fluctuations that affect household budgets. Financial planning tools that ignore these patterns may produce recommendations that are unrealistic or unsustainable. <!-- SOURCE NEEDED [DASMARIÑAS 2024]: cited in Seasonality in Personal Finance and six times across the SARIMA section; not in the corpus. Candidate: Dasmariñas, A. P., De Castro, G., Lazona, B. J., & Usona, L. (2024). Forecasting the impact of COVID-19 on the household final consumption expenditure (HFCE) in the Philippines. PUP Journal of Science & Technology, 14(1), 70-90. https://doi.org/10.70922/ctzevg57 - acquire and ingest before submission. -->

The challenge of seasonal expense forecasting is compounded by data limitations in many contexts. While population-level seasonality can be estimated from aggregate data sources such as the Philippine Statistics Authority's HFCE dataset, individual-level seasonal patterns may differ based on personal circumstances, location, and preferences. Dasmariñas et al. (2024) demonstrated that national-level consumption patterns can be forecasted with reasonable accuracy, providing a foundation for population-based seasonal forecasting. However, the application of these patterns to individual users requires careful adaptation to personal circumstances.

## Saver and Borrower Profile Classification

Understanding individual financial behavior patterns is essential for delivering personalized financial management support. Profile classification enables systems to tailor recommendations and strategies based on user characteristics, improving relevance and effectiveness. Laspiñas and Murcia (2024) applied machine learning approaches to classify income levels, demonstrating that financial characteristics can be systematically categorized to support targeted interventions. Their study confirmed that rule-based and statistical approaches can effectively segment users based on financial attributes.

The classification of individuals as savers or borrowers has theoretical foundations in behavioral finance and practical implications for financial planning. Cumaio et al. (2026) reviewed the literature on saving and debt behaviors, identifying that individuals exhibit distinct patterns in their financial decision-making based on psychological factors, demographic characteristics, and contextual influences. Savers prioritize setting aside funds for future goals, while borrowers have outstanding debt obligations that require management. Some individuals exhibit both characteristics, while others may be classified as neither.

The application of profile classification in financial management systems enables differentiated intervention strategies. Dey and Arefin (2025) developed a rule-based system for household budget generation, demonstrating that personalized recommendations based on user characteristics can improve budget relevance and adherence. Their approach incorporated multiple user attributes to generate tailored budget recommendations, supporting the value of profile-based personalization. In the context of savings and debt management, profile classification can inform the prioritization of goals, the aggressiveness of savings targets, and the urgency of debt reduction strategies.

## Budget Creation and Optimization

Budget creation is a fundamental component of personal financial management, providing a framework for allocating income across expense categories, savings goals, and debt repayments. Lu et al. (2025) described a budget as simultaneously a forecast, a commitment device, and a control system, serving multiple functions in financial management. In modern financial planning, budgeting processes must accommodate rapid changes in consumer behavior and the expectation that financial plans can be refreshed quickly as conditions change.

The optimization of budget allocation under constraints represents a mathematical challenge that has been addressed through various computational approaches. Gulbakyt et al. (2025) developed a dynamic model for budget allocation via multi-criteria optimization, demonstrating that mathematical optimization can generate allocation recommendations that balance multiple objectives. de Zarzà et al. (2024) applied optimization techniques to financial planning, incorporating both individual and cooperative budgeting scenarios with LLM-based recommendations. Their work demonstrated that optimization approaches can generate feasible and effective budget allocations under realistic constraints.

The practical application of budget optimization in consumer financial applications requires balancing analytical sophistication with usability. Santiago et al. (2025) developed a budget and financial management information system for public elementary schools, incorporating analytics and predictive insights for allocation decisions. Their system demonstrated that optimization and forecasting techniques can be integrated into practical financial management tools, supporting improved allocation decisions. However, the complexity of optimization models must be managed to ensure that recommendations are understandable and actionable for users without technical expertise.

## Unusual Expenses Detection

The detection of unusual expenses is an important function in personal financial management, enabling users to identify transactions that deviate from their normal spending patterns and may require attention. Huang et al. (2025) examined dynamic calibration of decision thresholds for financial anomaly detection, demonstrating that effective anomaly detection requires careful threshold setting that balances sensitivity with specificity. Their study verified approaches using payment platform information and data, confirming the applicability of anomaly detection techniques to financial transaction monitoring.

Anomaly detection in financial contexts presents unique challenges due to the inherent variability in spending patterns and the need to avoid excessive false alarms. Zhong (2025) developed an adaptive anomaly detection threshold for financial data quality monitoring based on time series features, demonstrating that threshold adaptation can improve detection performance across varying conditions. The study highlighted the importance of incorporating temporal patterns into anomaly detection, as what constitutes an unusual expense may vary by time period due to seasonal and cyclical factors.

The application of anomaly detection in personal financial management systems must account for individual spending patterns. Unlike fraud detection in institutional settings, personal expense anomaly detection must be calibrated to each user's baseline behavior. This personalization requirement creates cold-start challenges for new users who lack sufficient transaction history to establish a reliable baseline. The literature suggests that population-level patterns can partially mitigate cold-start conditions while personalization improves as user history accumulates.

## Financial Plan Composition and Execution

The composition of a comprehensive financial plan that integrates budget allocations, savings schedules, debt repayments, and monitoring mechanisms represents the culmination of personal financial management processes. Yoganandham (2025) emphasized that financial planning must address multiple domains simultaneously, as decisions in one area affect outcomes in others. For example, aggressive debt repayment may reduce funds available for savings, while excessive savings may leave insufficient resources for debt obligations.

The execution and adherence phase of financial planning is critical for achieving desired outcomes. Yeo et al. (2023) found that financial planning behavior is influenced by both capability and motivation factors, with adherence requiring ongoing commitment and support. Their review suggested that feedback mechanisms and progress monitoring can improve adherence by providing users with visibility into their progress and early warning of deviations from plans. These findings support the integration of monitoring and alerting features in financial management applications.

## Models and Algorithms

### Seasonal Auto-Regressive Integrated Moving Average (SARIMA)

The Seasonal Auto-Regressive Integrated Moving Average (SARIMA) model is a statistical time-series forecasting algorithm that extends the ARIMA model to incorporate seasonal patterns. SARIMA is defined by parameters (p, d, q)(P, D, Q, s), where p represents autoregressive terms, d represents differencing for stationarity, q represents moving average terms, and P, D, Q, and s represent the corresponding seasonal components with s denoting the seasonal period. According to Dasmariñas et al. (2024), SARIMA has been effectively applied to Philippine household consumption data, demonstrating its suitability for modeling seasonal patterns in economic time series.

The SARIMA model works by combining autoregressive and moving average components with seasonal differencing to capture both short-term dynamics and recurring seasonal patterns. The model uses lagged values and residual errors to extract linear trends and seasonal patterns from historical time series data. This capability makes SARIMA particularly well-suited for forecasting expenses that exhibit regular seasonal fluctuations, such as increased spending during holiday periods or school enrollment seasons.

The inputs required for SARIMA modeling include a sufficiently long time series of historical data, with the seasonal period determining the minimum data requirements. For monthly data with annual seasonality, a minimum of several years of observations is typically required to reliably estimate seasonal parameters. Dasmariñas et al. (2024) used quarterly HFCE data for their analysis, demonstrating that seasonal patterns can be captured even with quarterly observations, though monthly data provides finer resolution for forecasting applications.

SARIMA produces forecasts of future values along with confidence intervals that quantify uncertainty. The model output includes point forecasts for each future period and measures of forecast uncertainty that can inform decision-making under uncertainty. This output characteristic is valuable for financial planning applications, where users benefit from understanding not only expected values but also the range of plausible outcomes.

The application of SARIMA in financial forecasting has been extensively documented. Dasmariñas et al. (2024) applied SARIMA to forecast the impact of COVID-19 on Philippine household consumption, demonstrating that the model could capture both seasonal patterns and the effects of extraordinary events. However, the study also noted limitations, including the model's assumption of linear relationships and its sensitivity to structural breaks in the data. These limitations suggest that SARIMA is most appropriate for stable time series with consistent seasonal patterns.

The strengths of SARIMA include its interpretability, established theoretical foundation, and ability to quantify forecast uncertainty. The model provides explicit parameters that describe the relationship between current and past values, supporting understanding of the underlying dynamics. However, SARIMA also has limitations, including its assumption of linearity and its requirement for sufficient historical data. For personal financial management applications, these limitations are partially mitigated by the availability of population-level data that can supplement individual user data, particularly for new users.

In the context of the proposed study, SARIMA serves as the forecasting engine for seasonal expense prediction. The model will be trained on temporally disaggregated monthly expense estimates derived from PSA FIES and HFCE data, producing forecasts of per-category expense differences and composition. These forecasts will inform budget optimization and financial plan composition, providing users with seasonally-adjusted expense projections that account for predictable fluctuations in spending patterns.

#### Performance Metrics for SARIMA

The performance of SARIMA models is evaluated using multiple metrics that assess different aspects of forecast accuracy. Mean Absolute Error (MAE) measures the average magnitude of forecast errors, providing an interpretable measure of typical forecast deviation in original units. Dasmariñas et al. (2024) used MAE among other metrics in their evaluation, demonstrating its utility for comparing forecast accuracy across different model specifications.

Root Mean Square Error (RMSE) measures the standard deviation of forecast errors, penalizing larger errors more heavily through its squared formulation. This metric is particularly useful for assessing whether a model produces occasional large errors that could lead to significant planning miscalculations. Dasmariñas et al. (2024) reported RMSE values in their SARIMA evaluation, providing benchmarks for assessing model performance.

Symmetric Mean Absolute Percentage Error (SMAPE) expresses forecast accuracy as a percentage, enabling comparison across time series with different scales. This metric is valuable for financial forecasting applications where absolute error magnitudes may vary considerably across categories. The symmetry property of SMAPE addresses the asymmetry of traditional MAPE when actual values approach zero, making it more appropriate for expense categories that may have low or zero values in some periods.

Mean Directional Accuracy (MDA) measures the proportion of forecasts that correctly predict the direction of change, whether the value will increase or decrease. This metric is particularly relevant for financial planning applications, where knowing whether expenses will rise or fall may be more important than the precise magnitude of change. MDA complements magnitude-based metrics by assessing the model's ability to capture directional patterns.

### Rule-Based Classification

Rule-based algorithms classify inputs using explicit if-then rules derived from domain knowledge or empirical analysis. Unlike machine learning approaches that learn patterns from data, rule-based systems apply predetermined rules that encode expert knowledge or established criteria. Dey and Arefin (2025) developed a rule-based system for household budget generation, demonstrating that rule-based approaches can effectively generate personalized recommendations based on user characteristics.

The rule-based approach offers several advantages for financial profile classification. The rules are transparent and interpretable, enabling users to understand why they received a particular classification. This transparency supports user trust and facilitates explanation generation, which is important for financial applications where users need to understand the basis for recommendations. Additionally, rule-based systems do not require labeled training data, which may be unavailable for many financial classification tasks.

The inputs for rule-based classification in the proposed study include questionnaire answers and cash flow transaction history. The rules compute financial-condition dimensions including Emergency Fund Coverage (EFC), Debt-Service-to-Income (DSTI), Financial Margin (FM), and Credit Card Behavior (CCB). These dimensions are then combined using threshold rules to produce profile classifications of saver, borrower, both, or neither.

The rule-based algorithm produces a profile classification along with associated dimensions and a profile explanation. The profile classification informs downstream processing, including budget optimization and financial plan composition. The explanation provides users with insight into their classification, supporting understanding and acceptance of subsequent recommendations.

The application of rule-based algorithms in financial contexts has been documented in multiple studies. Laspiñas and Murcia (2024) applied machine learning approaches including rule-based methods to classify income levels, demonstrating that systematic classification can support targeted financial interventions. Dey and Arefin (2025) applied rule-based logic to budget generation, showing that expert-derived rules can produce reasonable recommendations without requiring training data.

The evaluation of rule-based classification presents unique challenges due to the absence of ground-truth labels. In the proposed study, evaluation will employ rule-derived reference labels for self-consistency checking, boundary-case test sets for edge conditions, and subject matter expert spot checks. This multi-faceted approach addresses the limitations of evaluating rule-based systems without human-labeled data.

#### Performance Metrics for Rule-Based Classification

Accuracy measures the overall proportion of correct classifications, providing a summary measure of classification performance. For rule-based systems, accuracy assessment requires a labeled dataset that may be constructed through expert annotation or derived from the rules themselves. The proposed study will use rule-derived reference labels for self-consistency evaluation, supplemented by boundary-case testing.

Precision measures the proportion of positive predictions that are correct, assessing the system's ability to avoid false positives. In the context of profile classification, precision indicates how often users classified as borrowers (for example) actually exhibit borrower characteristics. High precision is important for ensuring that recommendations are appropriate for the assigned profile.

Recall measures the proportion of actual positive cases that are correctly identified, assessing the system's ability to avoid false negatives. Recall indicates how many users who should be classified as borrowers (for example) are actually classified as such. High recall is important for ensuring that users who need debt management support receive appropriate recommendations.

The F1-score is the harmonic mean of precision and recall, providing a balanced measure that accounts for both types of classification errors. This metric is particularly useful when the costs of false positives and false negatives are similar, providing a single summary measure of classification quality.

### Linear Programming

Linear programming (LP) is a mathematical optimization technique that finds the best outcome in a mathematical model whose requirements are represented by linear relationships. The technique involves maximizing or minimizing a linear objective function subject to linear equality and inequality constraints. de Zarzà et al. (2024) applied optimization techniques to financial planning, demonstrating that budget allocation can be formulated as a constrained optimization problem solvable using linear programming methods.

The linear programming approach to budget optimization involves defining decision variables representing allocation amounts, an objective function representing the goal to be maximized (such as total savings and debt progress), and constraints representing limitations on allocations. The solution to the linear program provides the optimal allocation that maximizes the objective while satisfying all constraints.

The inputs for linear programming in the proposed study include the expense forecast from SARIMA, the user's saver and borrower profile, the user's savings goals, the user's debts, the user's income, and the user's fixed expenses. These inputs define the objective function and constraints for the optimization problem.

The linear programming solver produces a budget allocation, per-goal savings contribution schedules, per-debt repayment schedules, feasibility status, and an explanation. The feasibility status indicates whether a feasible solution exists that satisfies all constraints, which is important for identifying situations where user goals are infeasible given their resources.

The application of linear programming in financial contexts has been documented in multiple studies. Gulbakyt et al. (2025) developed a dynamic model for budget allocation via multi-criteria optimization, demonstrating that optimization techniques can generate effective allocation recommendations. de Zarzà et al. (2024) applied optimization to individual and cooperative budgeting scenarios, showing that linear programming can accommodate multiple objectives and constraints.

The strengths of linear programming include its ability to find optimal solutions, its established theoretical foundation, and its computational efficiency for problems of moderate size. The HiGHS solver, which will be used in the proposed study, provides an open-source implementation capable of solving large-scale linear programs efficiently. However, linear programming also has limitations, including its requirement for linear relationships and its inability to handle uncertainty directly.

#### Performance Metrics for Linear Programming

Constraint satisfaction rate measures the proportion of constraints that are satisfied by the optimal solution. In financial planning applications, this metric indicates whether all user requirements and limitations are respected in the allocation. A high constraint satisfaction rate indicates that the solver successfully found solutions that meet all specified conditions.

Budget utilization rate measures the proportion of available income that is allocated in the budget. This metric indicates whether the optimization fully utilizes available resources or leaves funds unallocated. High utilization may indicate aggressive allocation, while low utilization may indicate conservative assumptions or infeasible constraints that prevent full allocation.

Deviation from user preferences measures the extent to which the optimized allocation differs from user-specified priorities or preferences. This metric assesses whether the optimization respects user preferences or overrides them in pursuit of objective maximization. Low deviation indicates that recommendations align with user priorities, supporting acceptance and adherence.

### Inter-quartile Range (IQR)

The Inter-Quartile Range (IQR) method is a statistical technique for identifying outliers in data by measuring the spread of the middle 50% of values. The IQR is calculated as the difference between the third quartile (75th percentile) and the first quartile (25th percentile). Values falling below Q1 - 1.5×IQR or above Q3 + 1.5×IQR are typically considered outliers. Huang et al. (2025) examined dynamic calibration of decision thresholds for financial anomaly detection, demonstrating that statistical methods can effectively identify unusual financial transactions.

The IQR method works by establishing a baseline range of normal values and flagging values that fall outside this range as anomalies. This approach is non-parametric, meaning it does not assume a particular distribution of the data, making it robust to non-normal distributions that are common in financial data. The method is also computationally efficient, requiring only the calculation of quartiles from historical data.

The inputs for IQR detection in the proposed study include new transactions and a seasonally-aware baseline. The seasonal baseline accounts for predictable variations in spending patterns, ensuring that seasonal fluctuations are not incorrectly flagged as anomalies. This adaptation is important for financial applications where spending patterns vary systematically across time periods.

The IQR detector produces unusual expense alerts that notify users of transactions deviating significantly from their baseline. The alerts include information about the transaction and the degree of deviation, supporting user evaluation of whether the expense warrants attention. Users can acknowledge alerts, providing feedback that can inform future threshold calibration.

The application of IQR and related anomaly detection methods in financial contexts has been documented in multiple studies. Huang et al. (2025) applied dynamic threshold calibration for financial anomaly detection, demonstrating that effective detection requires careful threshold setting. Zhong (2025) developed adaptive anomaly detection thresholds based on time series features, showing that threshold adaptation can improve detection performance across varying conditions.

The strengths of the IQR method include its simplicity, interpretability, and robustness to non-normal distributions. The method does not require training a complex model, making it suitable for applications with limited data. However, the IQR method also has limitations, including its sensitivity to the choice of multiplier (typically 1.5) and its inability to incorporate multiple variables simultaneously.

#### Performance Metrics for IQR

Accuracy measures the overall proportion of correct anomaly classifications, providing a summary measure of detection performance. For anomaly detection, accuracy assessment requires labeled data indicating which transactions are truly anomalous, which may be constructed through expert annotation or user feedback.

Precision measures the proportion of detected anomalies that are true anomalies, assessing the system's ability to avoid false alarms. In the context of unusual expense detection, high precision indicates that most alerts correspond to genuinely unusual expenses, reducing alert fatigue and maintaining user attention to important notifications.

Recall measures the proportion of true anomalies that are detected, assessing the system's ability to identify all unusual expenses. High recall indicates that few unusual expenses are missed, providing comprehensive monitoring of spending patterns.

The F1-score provides a balanced measure combining precision and recall, useful when both false positives and false negatives have similar costs. For expense anomaly detection, the F1-score summarizes the system's overall detection quality.

### Model and Algorithm Integration

The integration of multiple models and algorithms creates a comprehensive pipeline that addresses the full spectrum of personal financial management functions. Each algorithm contributes specialized capabilities: SARIMA provides seasonal expense forecasting, rule-based classification assigns financial profiles, linear programming optimizes budget allocation, and IQR detects unusual expenses. The integration of these components produces synergistic benefits that exceed the capabilities of individual algorithms.

D'Souza et al. (2026) reviewed machine learning techniques for intelligent personal finance management systems, identifying that effective systems integrate multiple techniques including forecasting, classification, and anomaly detection. Their review noted that budgeting and expense analysis often utilize methods such as Exponentially Weighted Moving Averages, clustering, Random Forests, ARIMA, and LSTM models to reveal spending patterns and manage budget constraints. The integration of multiple techniques enables comprehensive analysis that addresses different aspects of financial management.

The integration architecture in the proposed study employs a pipeline design where outputs from one stage inform subsequent stages. Profile classification establishes the user context that influences budget optimization. Expense forecasting provides predictions that constrain budget allocation. Budget optimization generates schedules that are monitored for deviation. Unusual expense detection identifies transactions requiring attention. The Financial Planning module composes these outputs into a coherent plan for user approval.

The performance of the integrated system is evaluated through multiple levels of metrics. Individual algorithm metrics assess the performance of each component. System-level performance indicators assess the overall effectiveness of the integrated pipeline. This multi-level evaluation approach, demonstrated by Srisamai and Siriruk (2023) in their inventory management study, provides comprehensive assessment of both technical and operational performance. <!-- SOURCE NEEDED [SRISAMAI & SIRIRUK 2023]: cited for the multi-level evaluation framework; not in the corpus and the exact paper is unconfirmed. Likely: Srisamai, K., & Siriruk, P. Demand forecasting to reduce dead stock and loss sales: a case study of the wholesale electric equipment and part company. 13th Annual International Conference on Industrial Engineering and Operations Management (IEOM), 2023. - confirm this is the intended source and obtain the proceedings page numbers and DOI before submission. -->

#### Performance Indicators for Model Integration

Savings rate measures the ratio of savings contributions to monthly income, providing an indicator of the user's progress toward building financial reserves. This indicator is derived from the Savings Goal Management and Budget Management modules, reflecting the allocation decisions generated by the optimization process.

Savings goal progress measures the ratio of funded periods to total periods planned for each goal, indicating progress toward specific savings objectives. This indicator reflects adherence to the savings schedule generated by the budget optimization process.

Alert frequency measures the number of unusual-expense alerts per month, providing an indicator of spending volatility and the system's detection activity. High alert frequency may indicate irregular spending patterns or overly sensitive detection thresholds.

Debt progress measures the ratio of principal paid to the planned amount per debt, indicating progress toward debt reduction. This indicator reflects adherence to the debt repayment schedule generated by the optimization process.

Plan adherence measures the ratio of actual allocation to recommended allocation, providing an indicator of the user's compliance with system recommendations. High plan adherence indicates that recommendations are realistic and acceptable to users.

## Methodology

### Agile Development Lifecycle

The study employs the Agile software development methodology, providing an iterative and incremental framework that enables continuous refinement of both system features and prediction models based on ongoing feedback and evaluation results. The Agile methodology is particularly appropriate for BUDGIE's development given the complexity of integrating multiple machine learning models with a mobile application, as the iterative nature of Agile enables progressive refinement of both the algorithmic components and the user interface.

### Agile Kanban

Agile Kanban is the specific Agile variant employed in this study. Kanban emphasizes continuous delivery through visualization of workflow, limiting work-in-progress, and managing flow. The Kanban board provides visibility into the development process, enabling the team to identify bottlenecks and optimize workflow. This approach supports the iterative development of BUDGIE's multiple modules while maintaining flexibility to accommodate changing requirements and feedback.

### Data Collection

Data collection for BUDGIE encompasses multiple sources that provide the foundation for model training and system evaluation. The PSA 2023 Family Income and Expenditure Survey (FIES) provides annual income totals, annual expense totals, family size, per-capita income, and decile ranking. This dataset serves as the source for temporal disaggregation, providing annual expense estimates that are disaggregated to monthly resolution.

The PSA 2022-2026 Household Final Consumption Expenditure (HFCE) provides quarterly household consumption data that serves as the source for seasonal patterns in disaggregation. The HFCE dataset covers the period from 2022 Q1 to 2026 Q2, providing 18 quarters of data for estimating seasonal patterns. While this series length is borderline for SARIMA with a seasonal period of 12, it provides sufficient data for initial model development.

The Public User Expectations and Perceptions Survey (PUEPS) provides user expectations and preliminary investigation data. This survey employed purposive sampling of 47 respondents in the National Capital Region, primarily from Taguig, Pasay, Manila, and Makati. The survey results inform the user requirements and evaluation criteria for BUDGIE.

### Model Development

Model development follows the standard machine learning pipeline of data preprocessing, feature engineering, model training, cross-validation, performance evaluation, and model integration. The temporal disaggregation process transforms annual FIES data into monthly estimates using HFCE-calibrated proportional benchmarking. This process produces seasonally adjusted monthly expense estimates that serve as the foundation for SARIMA forecasting.

The SARIMA model is trained on the disaggregated monthly series, with seasonal orders determined from the population-level data. The model produces monthly multipliers per category and population-level baseline forecasts that inform budget optimization. Personal forecast blending occurs when sufficient user history is available, with the blend weight increasing linearly from zero to one as history grows from 24 to 48 months.

The rule-based classifier is developed from domain knowledge and financial planning principles. The classification rules incorporate four financial-condition dimensions: Emergency Fund Coverage, Debt-Service-to-Income, Financial Margin, and Credit Card Behavior. These dimensions are computed from user questionnaire responses and transaction history, then combined using threshold rules to produce profile classifications.

The linear programming solver is implemented using the HiGHS solver, an open-source optimization library capable of solving large-scale linear programs. The solver incorporates the expense forecast, user profile, savings goals, debts, income, and fixed expenses as inputs, producing optimized budget allocations and schedules.

### System Development

BUDGIE is developed as a mobile application using React Native with Expo SDK 55, providing cross-platform compatibility with primary support for Android devices. The backend services are implemented using Node.js 24 LTS with Express 5.1, with Supabase providing authentication and data storage. The model and algorithm microservice is implemented using Python 3.14 with FastAPI, providing REST APIs for classification, forecasting, optimization, and anomaly detection.

The system architecture follows a microservices pattern with separate containers for the API gateway, classifier, forecaster, detector, transaction service, and solver. This architecture supports independent scaling and deployment of components while maintaining loose coupling through event-driven communication. Core features are offline-capable with local caching, while modules with models or algorithms are server-side with graceful degradation during connectivity loss.

## System Evaluation

### Software Quality Evaluation

Software quality evaluation employs the ISO/IEC 25010:2023 quality model, which defines characteristics that collectively assess the fitness of a software system for its intended use. The evaluation addresses functional suitability, performance efficiency, reliability, security, portability, and usability, providing comprehensive assessment of system quality.

The System Usability Scale (SUS) provides a standardized instrument for assessing perceived usability. The SUS consists of ten items rated on a five-point scale, producing a score from 0 to 100 that indicates usability relative to established benchmarks. A score of 68 or higher is considered acceptable, representing above-average usability. The SUS will be administered to target users following interaction with BUDGIE, providing quantitative assessment of usability.

Functional suitability assessment verifies that BUDGIE provides functions that meet stated and implied needs, encompassing functional completeness, correctness, and appropriateness. The evaluation includes verification that all required features operate correctly according to their defined requirements, with particular attention to critical financial computations and transaction processing.

Performance efficiency assessment measures BUDGIE's time behavior, resource utilization, and capacity under defined conditions. The evaluation includes response time measurement with a target of p95 API response ≤2,000 ms, error rate assessment with a target of <1% under baseline load, and capacity testing to verify support for 150 concurrent virtual users.

Reliability assessment measures BUDGIE's ability to perform required functions consistently and without failure. The evaluation includes availability measurement with a target of ≥99.5% successful responses, fault tolerance assessment with a target of <1% failed requests during recoverable faults, recoverability testing to verify return to baseline within 60 seconds after simulated failure, and data integrity verification with a target of zero duplicate or missing transactions.

Security assessment measures BUDGIE's ability to protect data and resources against unauthorized access. The evaluation includes confidentiality testing to verify that 100% of protected endpoints reject requests without valid authentication, and authenticity testing to verify that invalid credentials result in 401/403 responses.

Portability assessment measures BUDGIE's ability to be installed and executed in supported environments. The evaluation includes installability testing to verify successful clean installation, adaptability testing to verify configuration through environment variables, and build success rate measurement.

### Model Performance Evaluation

Model performance evaluation assesses the accuracy and effectiveness of the algorithms employed in BUDGIE. Each algorithm is evaluated using metrics appropriate to its function, providing objective assessment of model capabilities.

The SARIMA forecaster is evaluated using MAE, SMAPE, MDA, and RMSE, with comparison against a seasonal naive baseline. These metrics assess different aspects of forecast accuracy, including average error magnitude, percentage error, directional accuracy, and error variance. The evaluation includes assessment of disaggregation accuracy to verify that temporal disaggregation preserves seasonal patterns.

The rule-based classifier is evaluated using accuracy, precision, recall, and F1-score. Given the absence of human-labeled ground-truth data, evaluation employs rule-derived reference labels for self-consistency assessment, boundary-case test sets for edge condition verification, and subject matter expert spot checks for validation.

The linear programming solver is evaluated using constraint satisfaction rate, budget utilization rate, and deviation from user preferences. These metrics assess whether the solver produces feasible solutions that respect constraints, fully utilize available resources, and align with user priorities.

The IQR detector is evaluated using accuracy, precision, recall, and F1-score. The evaluation assesses the detector's ability to identify unusual expenses while minimizing false alarms, using labeled data constructed through expert annotation or user feedback.

## Synthesis

The reviewed literature establishes that personal financial management is a critical capability for individual financial well-being, with particular relevance in developing economies where household financial vulnerability is pronounced. Empirical findings confirm that Filipinos face persistent challenges in savings and debt management, compounded by economic pressures and limited access to professional financial advice. Traditional approaches to financial management, including manual budgeting and generic expense tracking applications, fail to address the complex, interconnected nature of savings and debt challenges or to account for Philippine-specific factors such as seasonal consumption patterns.

Within this context, computational approaches including time-series forecasting, rule-based classification, mathematical optimization, and statistical anomaly detection form an integrated framework for personalized financial management. SARIMA modeling captures seasonal patterns in expense data, enabling forecasts that account for predictable fluctuations in spending. Rule-based classification assigns financial profiles that inform differentiated intervention strategies. Linear programming optimizes budget allocation under constraints, generating schedules that maximize savings and debt progress. IQR detection identifies unusual expenses that may require attention. The integration of these techniques creates synergistic benefits that exceed the capabilities of individual approaches.

Existing personal financial management applications have achieved significant adoption but exhibit limitations in their support for savings and debt outcomes. Most applications prioritize generic expense tracking over personalized financial planning, lacking the analytical sophistication required to optimize allocation across competing goals under constraints. The literature reveals a gap between the capabilities of existing systems and the needs of users seeking to improve their financial outcomes through systematic planning and disciplined execution.

The identified research gap is the lack of an integrated personal financial management system that incorporates Philippine seasonal consumption patterns into personalized expense forecasting and applies these forecasts to generate personalized budgets, savings contribution schedules, and debt repayment plans under financial constraints. While individual techniques have been validated in isolation or in different contexts, limited attention has been given to their integrated deployment within a single platform designed specifically for Filipino users. This gap is addressed by the proposed study through the development and evaluation of BUDGIE, a seasonality-aware savings-debt plan pipeline that combines profile classification, seasonal expense forecasting, budget optimization, and unusual expense detection to support improved financial planning among Filipinos aged 18 to 59 in the National Capital Region.

## Conceptual Model of the Study

The conceptual framework of the study follows an Input-Process-Output (IPO) model that illustrates the systematic development and evaluation of BUDGIE. The model is structured around four components: Input, Process, Output, and Evaluation.

<!-- FIGURE 1 PLACEHOLDER: conceptual model (IPO) diagram. Source image is in the

     Chapter 2 V3 .docx media folder and has not been exported to the repository. -->

Figure 1. Conceptual Model of the Study

The Input component identifies the knowledge, software, hardware, and data requirements necessary for the conduct of the study. Knowledge requirements encompass the theoretical foundations and computational techniques employed in BUDGIE. Software requirements specify the development tools and technologies used. Hardware requirements define the computing resources needed for development and testing. Data requirements identify the datasets used for model training and system evaluation.

The Process component describes the activities involved in developing BUDGIE, including requirements analysis, system design, module implementation, algorithm integration, and testing. The Agile Kanban methodology guides the development process, providing an iterative framework that enables continuous refinement based on feedback and evaluation results.

The Output component represents the primary deliverable of the study, which is the Development of BUDGIE as a personal financial management application that uses SARIMA-based seasonal expense forecasting for improved financial planning.

The Evaluation component describes the assessment activities that verify the quality and effectiveness of BUDGIE. Software quality evaluation employs ISO/IEC 25010:2023 and the System Usability Scale. Model performance evaluation assesses each algorithm using appropriate metrics. System performance evaluation measures savings rate, savings goal progress, alert frequency, debt progress, and plan adherence.

## Outstanding Source Requests

The following sources are cited in this chapter but are not yet in the RRL corpus. Each
`SOURCE NEEDED` marker in the text names the passage that depends on it. All three are real,
locatable works; each still has to be acquired, ingested into BUDI-Literature, and re-cited from
its verified metadata rather than from this provisional entry.

| Cited as | Status | Resolution |
| --- | --- | --- |
| Dasmariñas et al. (2024) | Confirmed, 7 citations, absent from corpus | Dasmariñas, A. P., De Castro, G., Lazona, B. J., & Usona, L. (2024). *PUP Journal of Science & Technology, 14*(1), 70-90. https://doi.org/10.70922/ctzevg57 |
| Dey and Arefin (2025) | Confirmed, 3 citations, absent from corpus | Dey, S., & Arefin, M. S. (2025). *Journal of Information Systems Engineering and Management, 10*(47s), 148-182. |
| Srisamai and Siriruk (2023) | 1 citation, paper identity unconfirmed | Likely the 13th IEOM conference paper on demand forecasting and dead stock. Confirm before citing. |

Dasmariñas et al. is the priority. It is the single load-bearing source for the seasonal
forecasting argument and is cited seven times, which leaves the SARIMA section of this chapter
resting on one paper. The adviser's standard for a core algorithm is six to seven sources, so the
SARIMA section needs corroboration beyond this paper regardless of the intake decision.

Two further dependencies are not academic citations and do not need sourcing, but are listed so
the evidence map stays complete: the PSA FIES and HFCE datasets, and the group's own PUEPS
instrument.

## References

Alenazi, M., & Sas, C. (2023). Evaluating budgeting apps: Limited support for budgeting compared to tracking. In *Proceedings of the British Computer Society HCI International Conference (BCSHCI 2023)* (pp. 1-12). British Computer Society. https://doi.org/10.14236/ewic/BCSHCI2023.1

Bangko Sentral ng Pilipinas. (2026). *Consumer expectations survey report: 2nd quarter 2026*. Monetary and Economics Sector, Department of Economic Statistics.

Claro, D. M. L., & Noval, J. E. G. (2025). The regressors of financial well-being among LGU employees in Davao del Norte. *ISRG Journal of Economics, Business and Management, 3*(6).

Cumaio, S., Serrasqueiro, Z., & Madaleno, M. (2026). Linking financial literacy and behavioural finance to saving and debt behaviours: A literature review of global and developing economy contexts. *Journal of Risk and Financial Management, 19*(6), 425. https://doi.org/10.3390/jrfm19060425

de Zarzà, I., de Curtò, J., Roig, G., & Calafate, C. T. (2024). Optimized financial planning: Integrating individual and cooperative budgeting models with LLM recommendations. *AI, 5*, 91-114.

D'Souza, M., Bhegade, P., Bhalekar, P., & Bhavsar, Y. (2026). A comprehensive review of machine learning techniques for intelligent personal finance management systems [Unpublished manuscript]. Department of Artificial Intelligence and Machine Learning, P.E.S Modern College of Engineering.

Esperanza, D. N. (2025). Digital lending efficacy on debt management of wage earners. *ASEAN Journal of Management & Innovation, 12*(2), 111-127.

Francisco, A. A., Legal, G. A., & Legal, F. (2026). Causes of salary loan dependency: Basis for strengthening financial literacy program. *International Journal of Multidisciplinary Educational Research and Innovation, 4*(1), 705-728.

Group 4. (2026). *Public user expectations and perceptions survey (PUEPS)* [Unpublished raw survey instrument]. III-DCSAD, University of Makati.

Gulbakyt, S., Almaz, A., Saule, S., & Suhrab, Y. (2025). Dynamic model for budget allocation in via multi-criteria optimization. *Journal of Applied Data Sciences, 6*(4), 3075-3088.

Huang, A., Zhang, X., Wang, Y., Tsai, S., Zhou, P., & Chen, L. (2025). Dynamic calibration of decision thresholds for financial anomaly detection: Verification with payment platform information and data. *Journal of Global Information Management, 33*(1), 1-26. https://doi.org/10.4018/JGIM.395852

Laspiñas, E. L., & Murcia, J. V. B. (2024). Machine learning approaches in classifying income levels. *TWIST, 19*(2), 92-97. https://doi.org/10.5281/zenodo.10049652#134

Lu, Y., Zhou, H., & Zhang, Y. (2025). A constrained, data-driven budgeting framework integrating macro demand forecasting and marketing response modeling. *Journal of Technology Informatics and Engineering, 4*(3), 493-520. https://doi.org/10.51903/jtie.v4i3.466

Philippine Statistics Authority. (2023). *Family income and expenditure survey 2023*. PSA.

Philippine Statistics Authority. (2026). *Household final consumption expenditure, 2022-2026 quarter 2*. PSA.

Santiago, R. L. T., Villarica, M. V., & Bernardino, M. P. (2025). Budget and financial management information system for public elementary schools: Analytics and predictive insights for MOOE allocation using linear regression. *International Journal of Advanced Research in Computer Science, 16*(3), 128-137. http://dx.doi.org/10.26483/ijarcs.v16i3.7256

Yeo, K. H. K., Lim, W. M., & Yii, K.-J. (2023). Financial planning behaviour: A systematic literature review and new theory development. *Journal of Financial Services Marketing, 29*, 979-1001. https://doi.org/10.1057/s41264-023-00249-1

Yoganandham, G. (2025). Mastering economic and financial sources with reference to budgeting, savings, early investing, debt management and the power of financial planning: A comprehensive analysis. *Degres Journal*. ISSN 0376-8163.

Zhong, M. (2025). Adaptive anomaly detection threshold for financial data quality monitoring based on time series features. In *2025 International Symposium on Artificial Intelligence and Computational Social Sciences (AICSS 2025)*. ACM. https://doi.org/10.1145/3776759.3776850
