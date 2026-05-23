Predict, Optimize, Deliver: Demand Forecasting and Resource
Optimization for a Market Research Firm

Ma. Theresa G Mariano∗
School of Graduate Studies
Mapua University
Makati, Philippines
mtgmariano@mymail.mapua.edu.ph

Richard N Monreal
School of Graduate Studies
Mapua University
Makati, Philippines
rmonreal@mapua.edu.ph

Abstract
In professional service industries, where human resources could
drive both cost and value, accurate forecasting and intelligent re-
source allocation were critical to sustaining operational perfor-
mance. To this end, this paper developed an integrated forecast-
ing and optimization framework to address demand uncertainty
and resource allocation challenges in a market research firm. The
study compared ARIMA, Holt–Winter’s Exponential Smoothing,
Prophet, and LSTM models in terms of service level accuracy, as-
sessed via MAE, RMSE, and MAPE across multiple training–test
splits and a 30-day hold-out period. Among the evaluated methods,
Prophet demonstrated the highest overall effectiveness, offering
a robust balance between forecast accuracy, interpretability, and
operational usability, especially for short-term planning horizons.
The selected forecasts were then operationalized using a Pyomo-
based prescriptive optimization model that allocated workforce
resources in alignment with anticipated service demand, subject
to constraints such as employee availability and client-specific re-
quirements. Forecast bands derived from RMSE were introduced to
simulate over- and under-forecasting scenarios, strengthening the
model’s resilience and responsiveness in allocation strategies. The
final framework was deployed within an interactive Power BI envi-
ronment, providing dynamic visualizations and supporting agile,
cost-effective workforce planning. Overall, this study contributed
a practical, data-driven approach that bridged predictive analytics
and operational planning, offering actionable insights for resource
optimization in professional service industries.

CCS Concepts
• Information Systems; • Decision Support Systems; • Data
Analytics;

Keywords
Resource Optimization, predict-then-optimizeFirst Author’s Name,
Initials, and Last Name, Second Author’s Name, Initials, and Last
Name, and Third Author’s Name, Initials, and Last Name. 2018. The

∗Corresponding Author

Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for third-party components of this work must be honored.
For all other uses, contact the owner/author(s).
ICBIM 2025, Bangkok, Thailand
© 2025 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2217-2/2025/09
https://doi.org/10.1145/3785171.3785187

Title of the Paper: ACM Conference Proceedings Manuscript Sub-
mission Template: This is the subtitle of the paper, this document
both explains and embodies the submission format for authors us-
ing Word. In Woodstock ’18: ACM Symposium on Neural Gaze
Detection, June 03–05, 2018, Woodstock, NY. ACM, New York, NY,
USA, 10 pages. NOTE: This block will be automatically generated
when manuscripts are processed after acceptance

ACM Reference Format:
Ma. Theresa G Mariano and Richard N Monreal. 2025. Predict, Optimize,
Deliver: Demand Forecasting and Resource Optimization for a Market Re-
search Firm. In The 9th International Conference on Business and Information
Management (ICBIM 2025), September 19–21, 2025, Bangkok, Thailand. ACM,
New York, NY, USA, 10 pages. https://doi.org/10.1145/3785171.3785187

1 INTRODUCTION
For the subject company, where client needs are highly variable,
effective resource allocation is essential to maintaining operational
efficiency and profitability. Consulting companies experience fluc-
tuating service requests tied to client behavior and project timelines
[1]. Since manpower is the primary asset in such firms, delays or
inefficiencies in staffing lead to missed deadlines and potential rev-
enue loss [2]. According to Resource-Based Theory (RBT), optimal
internal resource deployment contributes to sustained competitive
advantage [3], especially in outsourced delivery models such as the
studied company, which conducts 70% of its operations through its
Manila-based service center.

In this study, the subject firm handles client-specific “demand”
defined in hours across service categories, each varying in com-
plexity and processing time. Demand surges unpredictably, often
requiring overlapping workforce deployment. For example, Client
1 typically requires 2-3 full-time equivalents (FTEs), increasing to 4
during peak periods, while Client 2 presents more erratic spikes.
Manual workforce planning like MS Excel fails to adapt to such
volatility. While large enterprises leverage ERP platforms like SAP
or Oracle [4], smaller firms must choose between prebuilt tools
and custom models [5]. Forecast accuracy is critical as failures like
those experienced at Heathrow Airport have shown that poor de-
mand prediction can trigger systemic disruption [6]. Selecting the
right forecasting approach requires evaluating trade-offs between
accuracy, complexity, and interpretability, especially in dynamic
service environments [7].

This study proposed an integrated solution using a Predict-Then-
Optimize (PO) framework that combined time-series forecasting
with network flow-based resource allocation. Demand was first
forecasted using four techniques, specifically ARIMA, Holt-Winters,
LSTM, and Prophet. These were used to inform an optimization

103ICBIM 2025, September 19–21, 2025, Bangkok, Thailand

Ma. Theresa Mariano and Richard Monreal

model that respected real-world constraints such as work-hour caps
and shared staffing. The results were visualized in a Power BI dash-
board for operational transparency. The objective was to enhance
resource efficiency, align staffing to fluctuating service demand,
and demonstrate how advanced analytics can empower midsize
firms. This work contributed by identifying the most suitable fore-
casting method for a professional servicing firm, operationalizing
data-driven allocation strategies, and delivering actionable insights
through a usable, visual platform. This supported SDG 8 by pro-
moting sustainable employment practices, SDG 9 by advancing
data-driven decision-making in mid-sized firms, and SDG 17 by
fostering collaboration between analytics teams, operations, the
academe and strategic planners.

2 LITERATURE REVIEW
Time series forecasting assumes that future outcomes are exten-
sions of historical data, governed by trends, seasonality, cycles, and
randomness [8]. For industries that rely on time-bound outputs,
particularly the sample company where staffing and demand shift
rapidly, accurate forecasting becomes crucial. To this end, this
study investigates four prominent forecasting methods, specifically
ARIMA, Holt-Winters, LSTM, and Prophet, while assessing their
performance using RMSE, MAE, and MAPE metrics.

We begin with ARIMA, a classical yet widely adopted model.
Its strength is observed in handling stationary time series, with
well-documented applications in supply chain [9], healthcare [10],
and cloud resource planning [11]. However, as demand signals
become more volatile and irregular in modern service operations,
ARIMA’s limitations in capturing seasonality and nonlinear trends
emerge as critical gaps, thereby motivating the search for more
adaptive alternatives.

In response, Holt-Winters Exponential Smoothing builds on
ARIMA’s strengths by integrating level, trend, and seasonal com-
ponents through flexible smoothing parameters (𝛼, 𝛽, 𝛾) [12, 13].
This allows the model to dynamically adjust to recent observations,
making it well-suited for data that evolve over time. Depending on
whether seasonal variations remain constant or scale with magni-
tude, the model shifts between additive and multiplicative forms
[14]. Such adaptability has proven useful in real-time applications,
including epidemiological forecasting [14].

Yet, even with enhanced seasonality handling, both ARIMA and
Holt-Winters assume largely linear patterns. For service environ-
ments characterized by erratic shifts and nonlinear dependencies,
Long Short-Term Memory (LSTM) networks offer a more powerful
alternative. LSTM models, equipped with memory cells and gating
mechanisms, are capable of learning both short- and long-term
dependencies in time series data [15, 16]. As recent studies show,
LSTM has consistently outperformed ARIMA in capturing demand
fluctuations in complex, high-variance domains such as logistics
and workforce scheduling [16].

While LSTM offers high predictive power, it often lacks trans-
parency. This trade-off between accuracy and interpretability is
partially addressed by Prophet, an open-source model developed by
Facebook. Prophet decomposes time series into trend, seasonality,
and holiday effects [17, 18], offering strong accuracy with intuitive
parameter control. It has shown robust performance in diverse

settings such as retail [19], energy demand [20], and financial fore-
casting [18], making it a compelling choice for firms balancing
usability with precision.

To evaluate these models fairly, the study employs a triad of per-
formance metrics: RMSE, which penalizes large forecast deviations;
MAE, which captures average absolute error; and MAPE, which
offers percentage-based interpretability [21]. Although MAPE can
exaggerate errors when actual values are small, the combination of
these metrics ensures a holistic assessment. Notably, comparative
studies in call center staffing highlight how ARIMA and Prophet
differ in their sensitivity to these metrics [22].

However, forecasting is only the first step. What follows is
the critical challenge of resource allocation, which is turning pre-
dictions into optimal deployment strategies. To achieve this, the
study drew from network flow optimization, a method that has
gained traction in domains such as semiconductor supply chains
[23], telecommunications [24], and workforce management [25].
These models treat staffing as a flow problem, balancing supply (em-
ployee availability), demand (workload forecasts), and operational
constraints.

Solving such models efficiently requires a robust optimization
engine. The study thus adopted CPLEX, a solver widely recog-
nized for its speed and reliability in handling large-scale, resource-
constrained scheduling problems [26–28]. CPLEX was integrated
via Python to solve the formulated minimum-cost flow problem,
ensuring alignment between forecasted demand and resource avail-
ability while honoring business constraints like work-hour caps,
shared labor pools, and leave schedules [29, 30].

To ensure these technical outputs remain actionable for decision-
makers, the final layer of the solution stack involved data visu-
alization. Here, Power BI was selected for its cost-effectiveness,
native Microsoft integration, and strength in rendering interactive
dashboards [31, 32]. With built-in support for time-series plot-
ting, matrix views, and slicers [33], it could empower stakeholders
to explore forecast trends, track fulfillment levels, and simulate
resourcing scenarios, bridging the gap between data science and
operational strategy.

Despite these advancements, gaps in the literature persist. Most
forecasting-optimization frameworks target product-based or static
planning contexts, with limited relevance to the time-sensitive,
high-variance nature of professional services. Few studies explored
how interpretability and granularity trade-offs influence model
selection in such environments. Moreover, visualization tools are
rarely embedded into end-to-end systems, limiting their strategic
impact.

This research addressed these gaps by developing a unified, dy-
namic, and interpretable pipeline that connected demand forecast-
ing, resource optimization, and visualization, specifically tailored
to the unique operational demands of professional service firms. In
doing so, it not only enhanced model accuracy and usability but
also ensured alignment with real-world decision-making needs.

104Predict, Optimize, Deliver: Demand Forecasting and Resource Optimization for a Market Research Firm

ICBIM 2025, September 19–21, 2025, Bangkok, Thailand

3 METHODOLOGY
3.1 Data Understanding
To address the research questions, both quantitative and qualitative
data were collected. Historical activities from the company’s time-
tracking system served as the primary dataset, complemented by
operational insights from the team’s manager. The dataset spans
January 2, 2018 to December 24, 2024 and includes six key attributes.
The predictive phase uses the first four: 1.) Date (DD/MM/YYYY),
2.) Billable (binary: 1 for client-related, revenue-generating tasks; 0
for internal activities), 3.) Duration (decimal) (task length, capped
at 24 hours), and 4.) Client (binary: 1 or 2). The prescriptive model
adds 5.) Number of Resources (six analysts excluding QA) and 6.)
Working Hours Limit (8 hours/day, extendable to 10).

3.2 Data Analysis
3.2.1 Descriptive/Diagnostics Phase. This phase involved four key
activities. First, summary statistics (mean, min, max, percentiles,
standard deviation) were generated to compare demand variability
between the two clients. Second, time series decomposition using
seasonal_decompose from statsmodels was applied to extract trend
and seasonality components. Third, the Augmented Dickey-Fuller
(ADF) test assessed stationarity; a p-value ≤ 0.05 indicates suitabil-
ity for ARIMA modeling. Lastly, autocorrelation analysis using ACF
and PACF plots provided insight into lag dependencies, guiding
selection of AR and MA terms in ARIMA.

3.2.2 Predictive Phase. The predictive phase was implemented in
Google Colab using Python. Key attributes were selected, with
the dataset filtered to billable entries and aggregated daily. To en-
sure continuity, the time series was resampled to daily frequency
(freq=’D’) and missing values were addressed via linear interpo-
lation. The cleaned dataset was then split into 60:40, 70:30, and
80:20 train-test ratios. Model tuning followed to identify optimal
parameters for each forecasting approach.

Four forecasting models were implemented using Python.
ARIMA, from the statsmodels.tsa.arima.model library, was tuned via
grid search across combinations of (p, d, q) parameters, represent-
ing autoregressive lags, differencing for stationarity, and moving
average terms, respectively. Holt-Winters Exponential Smooth-
ing, via ExponentialSmoothing from statsmodels.tsa.holtwinters,
was configured with various combinations of trend and seasonality
types (additive or multiplicative), along with an optional damped
trend component to model decaying trends [34, 35]. Prophet, im-
ported from the prophet library, required reformatting the dataset
into ‘ds’ (date) and ‘y’ (target). Key parameters included change-
point_prior_scale for trend flexibility and seasonality_prior_scale
for capturing recurring patterns, with higher values allowing
greater adaptability [36]. LSTM, a deep learning model built us-
ing TensorFlow, involved data sequencing followed by a two-layer
LSTM architecture with return_sequences, a dropout layer to miti-
gate overfitting, and a dense output layer. The model was compiled
using the Adam optimizer and mean squared error loss to improve
training accuracy [37].

3.2.3 Model Evaluation. Models were first tuned using optimal
parameters identified through multiple train-test split validations.
Final evaluation was then conducted on a 30-day holdout set using

RMSE, MAE, and MAPE to assess forecast accuracy. RMSE captured
large errors, MAE reflected average deviation, and MAPE measured
relative error, though it was less reliable for low-demand values. To
address conflicting results, a weighted error score was computed
as (0.35 × MAE) + (0.35 × RMSE) + (0.30 × MAPE). The overall
score also incorporated interpretability and training speed (0.25
each) to reflect practical deployment. Simpler and faster models
received lower (better) scores, while complex or slower ones like
LSTM scored higher. This ensured a consistent and fair comparison
across accuracy, usability, and efficiency.

3.2.4 Prescriptive Phase. The model was translated as a Mixed-
Integer Linear Programming (MILP) problem, designed to optimize
the allocation of employees while meeting daily demand require-
ments. It accounted the following variables and parameters shown
in Table 1. xi, Ci, t represented hours availability of each employee,
which could be allocated for a given client and day depending on
needs. 𝐻𝐶𝑖𝑡 represented the demand nodes, or the service level
requirements of each client for a given day. A concept of backlog
was introduced through the 𝐸𝑖𝑡 −1variable, which was the differ-
ence of hours supplied, and hours needed from the previous day.
Hours required by each client and backlog hours were subject to
non-negativity constraints, enforced through within=NonNega-
tiveReals in the python code. In addition, overtime and employee
availability attributes were represented by oi,tand yi,t, respectively.
All these were configured to the model via Var() function with
iteration for each employee, client, and days.

The objective function aimed to minimize the excess resources
in terms of hours availability, minimizing operational costs and
improving utilization rate while satisfying demand requirements of
each client. This formulation balanced resource utilization ensuring
daily needs were covered by the team. Due to high confidentiality,
it was modelled that regular cost was $5 per hour, overtime cost was
$10 per hour, and penalty cost was $20 per hour. Mathematically,
it was expressed with the following formula in equation 1.

(cid:205)𝑖 ∈ {𝐸1,𝐸2,𝐸3,𝐸4,𝑆1,𝑆2},𝑡 𝐶𝑟𝑒𝑔𝑢𝑙𝑎𝑟 (𝑥𝑖𝐶1𝑡 + 𝑥𝑖𝐶2, 𝑡)
+𝐶𝑜𝑣𝑒𝑟𝑡𝑖𝑚𝑒 (cid:0)𝑂𝑖,𝑡 (cid:1) + 𝐶𝑝𝑒𝑛𝑎𝑙𝑡 𝑦 (𝐸1𝑡 + 𝐸2𝑡 )

(1)

As shown in equations 2 to 4, this model accounted three con-
straints: (1) The first one was the demand satisfaction constraint,
followed by (2) working hours limit, and (3) employee availability
constraints. The first constraint represented the billable hours that
need to be matched by employees. Next, the model put restriction
on the maximum hours of work to ensure employee well-being.
The third constraint was defined in the y(i,t) expression, ensuring
no work was assigned to an employee if they were out of office.
This resulted to 0 capacity if the value was 1.

(cid:213)

𝑖 ∈ {𝐸1,𝐸2,𝑆1,𝑆2}

𝑥𝑖𝐶1𝑡 = 𝐻𝐶1𝑡 + 𝐸1𝑡 −1

(2)

(cid:213)

𝑖 ∈ {𝐸3,𝐸4,𝑆1,𝑆2}

𝑥𝑖𝐶2𝑡 = 𝐻𝐶2𝑡 + 𝐸2𝑡 −1
𝑥𝑖𝐶1, 𝑡 + 𝑥𝑖𝐶2, 𝑡 ≤ (cid:0)8 + 𝑜𝑖,𝑡 (cid:1) ∗ (cid:0)1 − 𝑦𝑖,𝑡 (cid:1)
After formulating the objective, key variables, and operational con-
straints, the model proceeded to execution by calling the solver
package in Pyomo. The study utilized the CPLEX solver, imple-
mented in the code as solver = SolverFactory(’cplex_direct’). Unlike
traditional file-based approaches, where users must write or read

(3)

(4)

105ICBIM 2025, September 19–21, 2025, Bangkok, Thailand

Ma. Theresa Mariano and Richard Monreal

Variable
xi, C1, t
xi, C2, t
𝐻𝐶1𝑡
𝐻𝐶2𝑡
𝐸1𝑡 −1
𝐸2𝑡 −1
oi,t
yi,t
C𝑟𝑒𝑔𝑢𝑙𝑎𝑟
C𝑜𝑣𝑒𝑟𝑡𝑖𝑚𝑒
C𝑝𝑒𝑛𝑎𝑙𝑡 𝑦

Table 1: Optimization Variables and Parameters

Definition

Hours supplied by employee i for client 1 on day t
Hours supplied by employee i for client 2 on day t
Forecasted hours required by client 1 on day t
Forecasted hours required by client 2 on day t
Unmet hours needed by client 1 from the previous day (backlogs)
Unmet hours needed by client 2 from the previous day (backlogs)
Overtime hours
Indicator whether an employee is on leave (1) or not (0)
Cost of regular working hours
Cost of overtime hours
Penalty cost of unmet demand/backlogs

Thresholds
0 ≤ xi, C1, t ≤ 8 + 𝑜𝑖,𝑡
0 ≤ xi, C1, t ≤ 8 + 𝑜𝑖,𝑡
Non-negative real numbers
Non-negative real numbers
Non-negative real numbers
Non-negative real numbers
0 ≤ oi,t ≤ 2
Binary (0,1)
$5/hour (hypothetical)
$10/hour (hypothetical)
$20/hour (hypothetical)

data files [30], such as in MATLAB or Lingo, this plug-in allowed
seamless interaction with IBM’s CPLEX solver through Python bind-
ings [29]. Beyond efficiency, this choice was driven by its seamless
integration and compatibility with the Python-based workflow,
ensuring a streamlined optimization process.

3.3 Data Visualization
Custom visualizations were developed to enhance interpretability
and support decision-making. A Sankey diagram was employed to
depict the flow of billable hours from clients to employees, effec-
tively illustrating workload distribution. Weekly bar charts, color-
coded by client, were used to present trends and forecasted demand,
while key summary metrics provided an overview of total weekly
requirements. These visual components enabled stakeholders to
quickly grasp demand dynamics and informed resource planning.

3.4 Ethical Considerations
This study utilized actual company operations data, requiring strict
diligence in responsible data handling. Data privacy and confi-
dentiality were observed by anonymizing the clients being catered
in the study. No personal identifiable information was collected
throughout the course of the study to adhere to data governance
protocols of the company. The operations manager was informed
on the extent of data usage to answer the study’s objectives. As
part of data integrity and transparency process, the data were solely
used for academic purposes only. Any processing and data manip-
ulations performed were documented in the methodology section
of the study.

3.5 Limitations
This study adopted a quantitative approach, which presented cer-
tain limitations. First, the analysis was restricted to output-based
variables, such as billable hours, and was confined to group-level
assessments; input-level factors like individual analyst skill, which
could enhance the model, were unavailable. Second, the forecasting
model utilized internal historical data and did not incorporate exter-
nal economic indicators from the outsourcing country, which may
influence demand variability. Third, caution was warranted when
using the tool for long-range forecasting, as it did not consider
rare but high-impact events (e.g., the COVID-19 pandemic). Lastly,

the effectiveness of the proposed system was highly dependent on
consistent and accurate updating of time-tracking data.

4 RESULTS AND DISCUSSION
This section presented the findings of the time series analysis to
develop a demand forecasting and resource allocation model for
a market research firm. The results were organized to address
the three main research questions: forecasting accuracy, optimal
workforce distribution, and effective visualization.

4.1 Diagnostic Phase
The diagnostic results in Table 2 effectively mirrored the opera-
tional characteristics of each client. For instance, the upward trend
in Client 1’s data was a clear indication of expanded syndicated
research scope and consistent repeat contracts. Conversely, the
volatile trend observed for Client 2 suggested the varied nature
of their projects, which included periodic brand reports, ad-hoc
custom research demand, or studies in new market domains or
industries.

4.2 Predictive Phase
The study examined four models and were tested using two eval-
uation techniques: 1. multiple data splits for forecast stability
checking, and 2. holdout evaluation for model selection. The first
approach checked if models generalized well with varying amount
of historical data used in training, whereas the second one simu-
lated if model performed well in production setting, where future
values were totally unknown.

4.2.1 Hyperparameter tuning using multiple data splits. Multiple
train-test splits were used to evaluate model robustness and opti-
mize hyperparameters, as shown in Figures 1, 2, 3 and 4. For ARIMA
and Holt-Winters, larger training sizes consistently improved MAE
and RMSE, particularly for Client 1, though MAPE remained volatile
for Client 2 due to variable project types. Prophet showed sensitiv-
ity to changepoint prior scale, with better fit at higher flexibility
but increased relative error at lower splits, especially for Client
2. LSTM maintained stable performance across all splits, showing
less sensitivity to training size but strong absolute accuracy. These

106Predict, Optimize, Deliver: Demand Forecasting and Resource Optimization for a Market Research Firm

ICBIM 2025, September 19–21, 2025, Bangkok, Thailand

Aspect

Trend Component
Seasonal Component
Residual Component
ACF Behavior
PACF Behavior

Stationarity
Model Type

Table 2: Diagnostic Results

Client 1

Client 2

Moderately increasing trend
Weak
Random
Slowly decays, suggesting MA component
Significant lag at 1 and 2, suggesting AR
component
Stationary series
Additive

Moderately increasing trend
Weak
Random
Slowly decays, suggesting MA component
Significant lag at 1 and 2, suggesting AR
component
Stationary series
Additive

Figure 1: ARIMA Model Performance Metrics Across Settings and Training Splits. For Client 1, increasing training size improved
model accuracy. Client 2 showed stronger absolute performance (lower MAE, RMSE), but higher MAPE, indicating larger
relative error sensitivity.

results underscored the importance of split-based validation for se-
lecting optimal configurations tailored to data volume and demand
volatility.

4.2.2 Holdout Evaluation. A 30-day holdout evaluation confirmed
that the Additive Prophet model outperformed all others, yielding
the lowest weighted error for Client 1 (13.038) and showing strong
results for Client 2 (27.786), as shown in Table 3. Prophet’s strength
in handling trend shifts and event-triggered variations made it more
adaptive to both stable and volatile demand patterns, outperform-
ing ARIMA and Holt-Winters, particularly under noisy conditions.
Although LSTM showed competitive accuracy, its higher complex-
ity and data requirements reduced its practical viability. When
interpretability and speed were factored in, Prophet achieved the
lowest overall score (10.456), shown in Table 4, validating its suit-
ability for operational forecasting in resource-constrained service
environments.

4.3 Prescriptive Phase
Forecasted service demand was operationalized using a Pyomo-
based optimization model, tested across three scenarios: baseline
forecasts, positive RMSE-adjusted forecasts (to simulate under-
forecasting), and negative RMSE-adjusted forecasts (to simulate
over-forecasting). The model strictly respected capacity constraints,
ensuring no employee exceeded the 10-hour daily cap and aligned
resource allocations with forecasted demand across all dates, achiev-
ing near-zero gaps. As reflected in Figure 5, exclusivity rules were
enforced, assigning fixed analysts to each client while shared re-
sources (S1, S2) flexibly absorbed load variations. Utilization analy-
sis confirmed efficient deployment, though slight overutilization
(e.g., 106% for S2), shown in Table 5, in high-demand scenarios
flagged areas for managerial attention.
Cost analysis in Figure 6 revealed that small discrepancies in short-
term forecasts could compound into significant cost gaps over time,
reinforcing the value of dynamic, short-horizon planning. Weekly

107ICBIM 2025, September 19–21, 2025, Bangkok, Thailand

Ma. Theresa Mariano and Richard Monreal

Figure 2: Holt-Winter’s Model Performance Metrics Across Settings and Training Splits. For Client 1, the model achieved
lowest errors at higher training sizes. In contrast, Client 2 displayed more volatile results with high MAPE values, especially
under additive trend-seasonality settings, indicating sensitivity to seasonality assumptions and lower robustness compared to
other models.

Figure 3: Prophet Model Performance Metrics Across Settings and Training Splits. Results showed variability across settings,
particularly for Client 2 in lower train splits, indicating model sensitivity to parameter tuning.

or bi-weekly use of the tool was found optimal, as it allowed for
cost-effective and responsive staffing aligned with shifting demand.
This prescriptive framework not only optimized resource use un-
der realistic operational constraints but also delivered actionable

insights for balancing service levels, workforce capacity, and labor
costs in volatile service environments.

108Predict, Optimize, Deliver: Demand Forecasting and Resource Optimization for a Market Research Firm

ICBIM 2025, September 19–21, 2025, Bangkok, Thailand

Figure 4: LSTM Model Performance Metrics Across Settings and Training Splits. Results showed stable performance across all
splits and hyperparameters, with Client 1 showing slightly higher accuracy.

Table 3: Summary of Weighted Error Metrics

Model

Client

MAE (0.35)

RMSE (0.35)

MAPE (0.30)

ARIMA (2,0,1)
Holt-Winter (None,None)
Additive Prophet (cps=0.1)
LSTM (lookback=7, units=32)
ARIMA (0,0,0)
Holt-Winter (None,Add)
Additive Prophet (cps=0.5)
LSTM (lookback=7, units=32)

1
1
1
1
2
2
2
2

5.970
5.182
4.748
4.755
4.253
3.335
3.317
3.170

7.528
7.076
6.639
6.639
4.785
4.535
4.057
4.036

54.799
46.644
30.175
42.386
71.669
102.363
84.017
84.369

Table 4: Overall Model Selection

Weighted Error
Metrics

21.164
18.284
13.038
16.703
24.664
33.463
27.786
27.833

Model

ARIMA
Holt-Winter
Prophet
LSTM

Average Error
(0.50)

Interpretability
(0.25)

Speed (0.25)

Weighted Score

Rank

22.914
25.874
20.412
22.268

0.250
0.250
0.500
1.000

0.250
0.250
0.500
1.000

11.582
13.062
10.456
11.634

2
4
1
3

4.4 Visualization Phase
Forecasted demand and optimized resource allocations were visual-
ized through an interactive Power BI dashboard, enabling real-time
operational insights as shown in Figure 7. Key slicers allowed man-
agers to filter by client, staff, scenario, and date range, supporting
agile decision-making under uncertainty. Visual elements such as
Sankey diagrams and bar charts highlighted workload distribution,

utilization, and free capacity, helping identify staffing imbalances.
KPI cards monitored total demand, assigned hours, unmet demand,
overtime cost, and service fulfillment, providing actionable indi-
cators for performance and risk. Together, these tools facilitated
dynamic, data-driven workforce planning aligned with fluctuating
service requirements.

109ICBIM 2025, September 19–21, 2025, Bangkok, Thailand

Ma. Theresa Mariano and Richard Monreal

Table 5: Optimized Average Resource Utilization

Employees

Baseline

Adjusted (-)

Adjusted (+)

E1
E2
E3
E4
S1
S2

89%
55%
100%
25%
88%
71%

59%
4%
74%
0%
72%
28%

97%
96%
75%
100%
42%
106%

Figure 5: Resource Distribution by Forecast Scenario

Figure 6: Cumulative Allocation Cost by Forecast Scenario

5 CONCLUSION AND RECOMMENDATION
5.1 Conclusion
The Prophet model was seen as the most effective approach, balanc-
ing accuracy and operational usability, particularly in short-term
planning contexts. Its performance improved with larger, regu-
larly updated datasets, enabling dynamic, data-driven decisions.
Incorporating prediction intervals into the optimization phase en-
hanced allocation precision by accounting for demand uncertainty.
Optimization outputs respected key constraints such as working
hours, employee availability, and resource assignments (dedicated
vs. shared). Integrated within an interactive Power BI dashboard,
the combined forecasting-optimization system provided actionable
insights through visual tools like Sankey diagrams and KPI panels,
supporting agile responses in volatile service environments.

5.2 Recommendation
Given the critical role of training size in forecasting accuracy, this
study recommended establishing a robust data warehousing frame-
work to ensure the availability, continuity, and temporal integrity
of historical data, particularly during system transitions. For future
research, researchers may incorporate adaptive learning mecha-
nisms and real-time analysis to support continuous improvement
of both forecasting and optimization processes in dynamic service
environments. Furthermore, expanding the model to include input-
based variables (e.g., skill levels, project complexity) and integrating
external economic indicators could further enhance predictive ac-
curacy.

110Predict, Optimize, Deliver: Demand Forecasting and Resource Optimization for a Market Research Firm

ICBIM 2025, September 19–21, 2025, Bangkok, Thailand

Figure 7: Resource Mapping and Utilization Dashboard

Acknowledgments
The author would like to extend sincere gratitude to the company
for granting access to operational data and valuable domain in-
sights, which were instrumental in the successful completion of
this study. The author also acknowledged the valuable input and
encouragement of the project panel members, Dr. Ardvin Kester
Ong, Dr.
John Xavier Chavez, and Dr. Eric Blancaflor, whose
feedback helped refine the analytical framework and ensured the
study’s practical relevance. Deepest appreciation was likewise ex-
tended to Dr. Richard N. Monreal, Capstone Project Adviser, for
his mentorship and critical guidance at every stage of this research.

References
[1] Ugboko, L. N., & Ehugbo, I. (2021). Effect of resource utilization techniques on
competitive advantage of selected firms in Nigerian telecommunications industry.
International Journal of Academic Multidisciplinary Research (IJAMR), 5(11),
106-117. Retrieved from https://www.researchgate.net/publication/359504374_
Effect_of_Resource_Utilization_Techniques_on_Competitive_Advantage_of_
Selected_Firms_in_Nigerian_Telecommunications_Industry

[2] Sharma, S., & Singh, S. (2022). RLS model for forecasting resource fulfilment in
IT and consulting industry. Metamorphosis: A Journal of Management Research,
21(1), 1–10. https://doi.org/10.1177/09726225221075086

[3] Boadi-Sarpong, A. B., Agyei, P. A., Mensah, E., & Boateng, P. A. (2023). Resource
allocation strategies for maintaining competitiveness and achieving innovation
success. International Journal of Research and Scientific Innovation (IJRSI), 10(7).

https://doi.org/10.51244/IJRSI.2023.10724

[4] Gartner. (n.d.). NetSuite planning and budgeting alternatives & competitors.
Gartner Peer Insights. Retrieved from https://www.gartner.com/reviews/market/
financial-planning-software/vendor/oracle/product/netsuite-planning-and-
budgeting/alternatives

[5] AltexSoft. (2022, March 1). Demand forecasting methods: Using machine learning
to see the future of sales. AltexSoft. Retrieved from https://www.altexsoft.com/
blog/demand-forecasting-methods-using-machine-learning/

[6] Business Money. (2022, July 25). Demand forecasting: What happens when
it fails. Business Money. Retrieved from https://www.business-money.com/
announcements/demand-forecasting-what-happens-when-it-fails/

[7] Sutanto, E. M. (2000). Forecasting: The key to successful human resource
management. Jurnal Manajemen & Kewirausahaan, 2(1), 1–8. Retrieved from
https://www.researchgate.net/publication/50434617

[8] Jose, J. (2022). Introduction to time series analysis and its applications. Christ
University. Retrieved from https://www.researchgate.net/publication/362389180_
INTRODUCTION_TO_TIME_SERIES_ANALYSIS_AND_ITS_APPLICATIONS
[9] Ghosh, S. (2020). Forecasting of demand using ARIMA model. American Journal
of Applied Mathematics and Computing, 1(2), 13–18. https://ajamc.smartsociety.
org/wp-content/uploads/2020/09/paper4.pdf

[10] Girotra, R. (2022). Workforce planning using time series (Master’s dissertation).
Trinity College Dublin. https://publications.scss.tcd.ie/theses/diss/2022/TCD-
SCSS-DISSERTATION-2022-070.pdf

[11] Devi, K. L., & Valli, S. (2023). Time series-based workload prediction using the
statistical hybrid model for the cloud environment. Computing, 105(2), 353–374.
https://doi.org/10.1007/s00607-022-01129-7

[12] Kumar, L., Khedlekar, S., & Sharma, R. (2024). A comparative assessment of Holt-
Winters exponential smoothing and autoregressive integrated moving average
for inventory optimization in supply chains. Supply Chain Analytics, 8, Article
100084. https://doi.org/10.1016/j.sca.2024.100084

111ICBIM 2025, September 19–21, 2025, Bangkok, Thailand

Ma. Theresa Mariano and Richard Monreal

[13] Wang, C.-C., Chien, C.-H., & Trappey, A. J. C. (2021). On the application of
ARIMA and LSTM to predict order demand based on short lead time and on-time
delivery requirements. Processes, 9(7), 1157. https://doi.org/10.3390/pr9071157

[14] Swapnarekha, H., Behera, H. S., Nayak, J., Naik, B., & Kumar, P. S. (2021). Multi-
plicative Holt’s Winter model for trend analysis and forecasting of COVID-19
spread in India. SN Computer Science, 2, Article 416. https://doi.org/10.1007/
s42979-021-00808-0

[15] Yadav, M., Patil, R., Bhirud, B., & Chavle, P. L. (2023). LSTM model-based
demand forecasting in supply chain using efficient optimizer. Retrieved
from https://www.researchgate.net/publication/373555323_LSTM_Model_based_
Demand_Forecasting_in_Supply_Chain_using_Efficient_Optimizer

[16] Terrada, L., El Khaili, M., & Ouajji, H. (2022). Demand forecasting model using
deep learning methods for supply chain management 4.0. International Journal
of Advanced Computer Science and Applications, 13(5), 704–711. https://doi.org/
10.14569/IJACSA.2022.0130581

[17] Facebook Research. (2017, February). Prophet: Forecasting at scale. Facebook
Research. Retrieved from https://research.facebook.com/blog/2017/2/prophet-
forecasting-at-scale/

[18] Sharma, K., Bhalla, R., & Ganesan, G. (2022). Time series forecasting using FB-
Prophet. In R. Zwiggelaar, G. Ganesan, Q. S. Cheng, K.-L. Du, & S. R. Satti (Eds.),
Proceedings of the Algorithms, Computing and Mathematics Conference 2022
(ACM 2022) (pp. 59–64). CEUR Workshop Proceedings, Vol-3445. https://ceur-
ws.org/Vol-3445/PAPER_07.pdf

[19] Negre, P., Alonso, R. S., Prieto, J., García, Ó., & de-la-Fuente-Valentín, L. (2024).
Prediction of footwear demand using Prophet and SARIMA. Expert Systems with
Applications, 234, 124512. https://reunir.unir.net/handle/123456789/17524
[20] Long, C., Yu, C., & Li, T. (2022). Prophet-based medium and long-term electricity
load forecasting research. Journal of Physics: Conference Series, 2356, 012002.
https://doi.org/10.1088/1742-6596/2356/1/012002

[21] Jierula, A., Wang, S., OH, T.-M., & Wang, P. (2021). Study on accuracy metrics
for evaluating the predictions of damage locations in deep piles using artificial
neural networks with acoustic emission data. Applied Sciences, 11(5), 2314. https:
//doi.org/10.3390/app11052314

[22] Seder, A., & Alnasser, R. (2023). Workforce management for Salik call cen-
ter (Master’s thesis). Rochester Institute of Technology. Retrieved from https:
//scholarworks.rit.edu/cgi/viewcontent.cgi?article$=$12635&context$=$theses
[23] Wang, Y., Zhang, H., Yuan, C., Li, X., & Jiang, Z. (2024). A network flow approach
to optimal scheduling in supply chain logistics. arXiv. https://doi.org/10.48550/
arXiv.2411.17544

[24] Wang, C. C. (2022). Network flow optimization using reinforcement learning
(Doctoral dissertation). Aalborg University. https://vbn.aau.dk/ws/portalfiles/
portal/549541544/PHD_CCW.pdf

[25] Ercsey, Z., & Kovács, Z. (2023). Multicommodity network flow model of a human
resource allocation problem considering time periods. Central European Journal
of Operations Research. https://doi.org/10.1007/s10100-023-00868-y

[26] Mohammadi, S., PourKarimi, L., & Reinert, K. (2023). A mathematical pro-
gramming approach for resource allocation of data analysis workflows on
heterogeneous clusters. The Journal of Supercomputing, 79(17), 19019–19048.
https://doi.org/10.1007/s11227-023-05325-w

[27] Fang, Z., Wu, Q., & Guan, D. (2022). Towards optimal resources allocation in
cloud manufacturing: New task decomposition strategy and service composition
model. Security and Communication Networks, 2022, Article 5019584. https:
//doi.org/10.1155/2022/5019584

[28] Kia, R., Shahnazari-Shahrezaei, P., & Zabihi, S. (2016). Solving a multi-objective
mathematical model for a multi-skilled project scheduling problem by CPLEX
solver. Proceedings of the 2016 IEEE International Conference on Industrial
Engineering and Engineering Management (IEEM), 1220–1224. https://doi.org/
10.1109/IEEM.2016.7798072

[29] Pyomo Developers. (n.d.). Pyomo CPLEX direct solver module. Pyomo Docu-
mentation. Retrieved March 18 2025, from https://pyomo.readthedocs.io/en/6.8.
1/_modules/pyomo/solvers/plugins/solvers/cplex_direct.html

[30] OR Stack Exchange. (n.d.). Difference between CPLEX direct and CPLEX
in Pyomo SolverFactory. OR Stack Exchange. Retrieved March 18 2025,
from https://or.stackexchange.com/questions/9412/difference-between-cplex-
direct-and-cplex-in-pyomo-solverfactory

[31] Lavanya, A., Sindhuja, S., Gaurav, L., & Ali, W. (2023). A comprehensive review
of data visualization tools: Features, strengths, and weaknesses. International
Journal of Computer Engineering in Research Trends, 10(1), 10–20. https://doi.
org/10.22362/ijcert/2023/v10/i01/v10i0102

[32] Tirupati, K. K., Joshi, A., Singh, S. P., Chhapola, A., Jain, S., & Gupta, A. (2024).
Leveraging Power BI for enhanced data visualization and business intelligence.
Universal Research Reports, 10(2), 676–711. https://doi.org/10.36676/urr.v10.i2.
1375

[33] Microsoft. (n.d.). Power BI visualization types for reports and Q&A. Microsoft
Learn. Retrieved March 2025, from https://learn.microsoft.com/en-us/power-
bi/visuals/power-bi-visualization-types-for-reports-and-q-and-a

[34] Pleños, M. C. F. (2022). Time series forecasting using Holt-Winters exponential
smoothing: Application to abaca fiber data. Problems of World Agriculture, 22(2),
17–29. https://doi.org/10.22630/PRS.2022.22.2.6

[35] StatsModels. (n.d.). statsmodels.tsa.holtwinters.ExponentialSmoothing. StatsMod-
els Documentation. Retrieved February 26,2025, from https://www.statsmodels.
org/dev/generated/statsmodels.tsa.holtwinters.ExponentialSmoothing.html
[36] Facebook. (n.d.). Trend changepoints in Prophet. Facebook Prophet Documenta-
tion. Retrieved February 26,2025, from https://facebook.github.io/prophet/docs/
trend_changepoints.html

[37] Arya, M., & Sastry, G. H. (2023). Effective LSTM neural network with Adam
optimizer for improving frost prediction in agriculture data stream. In A. E.
Hassanien, M. A. Elhoseny, & A. T. Azar (Eds.), Modelling and development of
intelligent systems (pp. 3–17). Springer. https://doi.org/10.1007/978-3-031-27034-
5_1

112