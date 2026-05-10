Sigma J Eng Nat Sci, Vol. 44, No. 1, pp. 637−662, February, 2026

Sigma Journal of Engineering and Natural Sciences
Web page info: https://sigma.yildiz.edu.tr
DOI: 10.14744/sigma.2026.2000

Review Article

A comprehensive review on traditional and cutting-edge approaches for
wind speed/power forecasting

Muskaan AHUJA1*

, Sanju SAINI1

1Department of Electrical Engineering, Deenbandhu Chhotu Ram University of Scince and Technology,
Murthal , Sonipat, 131029, India

ARTICLE INFO

Article history
Received: 04 April 2024
Revised: 08 October 2024
Accepted: 14 November 2024

Keywords:
Deep Learning Methods;
Hybrid Methods; Intelligent
Methods; Physical Methods;
Statistical Methods; Traditional
Approaches; Wind Forecasting

ABSTRACT

Wind forecasting is essential for improving the effectivness of wind energy in overall power
system. İt helps in the areas like improving stability of grid , energy planning and to support
the effective market operation. This paper is an attempt to examine traditional as well as ad-
vanced forecasting methods, from the classical statistical approaches to modern data-driven
and hybrid techniques. The traditional techniques including time-series analysis as well as the
numerical weather prediction (NWP) techniques are quite good but are incapable of capturing
the  complexity  and  variation  patterns  of  wind  pattern.  While  the  cutting-edge  techniques,
including the machine learning & deep learning have helped to increase the forecasting accu-
racy, hybrid models, have given increasingly promising results as they offer a balance between
the high accuracy and computational requirements by merging the traditional and modern
approaches used for wind speed and/power forecasting. This study shows the significant value
achieved by hybrid approachs, reporting Root Mean Square Error (RMSE) values of 0.1089
m/s for statistical approach, 0.02 m/s for intelligent approaches, and 0.0096 m/s for hybrid ap-
proaches. Using a real-world wind dataset, the performance of several widely used forecasting
models is evaluated and compared. This study provide an symmetrical analysis of advantages
and  disadvantages  of  various  forecasting  approaches  across  different  time  scale  &  weather
condition.  It  also  elaborates  persistent  challenges,  e.g.,  limited  data  availability  and  the  re-
quirement for better model interpretability as well as real-time adaptability. The review con-
cludes that although data-driven and hybrid models currently achieve the best performance,
additional research is needed to enhance interpretability and data integration. This research
improve reviews on wind forecasting, highlighting latest developments and practical uses. İt
also provide helpful guide for researchers and idustry experts to understand present & future
opportunities in the field.

Cite this article as: Ahuja M, Saini S. A comprehensive review on traditional and cutting-edge
approaches for wind speed/power forecasting. Sigma J Eng Nat Sci 2026;44(1):637−662.

*Corresponding author.
*E-mail address: 20001902004muskaanahuja@dcrustm.org

This paper was recommended for publication in revised form
Editor-in-Chief Ahmet Selim Dalkilic

Published by Yıldız Technical University Press, İstanbul, Turkey
© Author. This is an open access article under the CC BY-NC license (http://creativecommons.org/licenses/by-nc/4.0/).

Sigma J Eng Nat Sci, Vol. 44, No. 1, pp. 637−662, February, 2026

maintenance  schedules,  infrastructure  development  along
with maintaining system reliability.

Following are the major benefits of precise wind speed

•

and/or power forecasting :
•  Wind speed and/or power forecasting helps in improv-
ing/maintaining the system balance, avoid the outages,
and ensuring steady performance of grid.
It supports the optimal operation of turbine and reduces
the operating costs.
It also contributes to the economic dispatch, unit com-
mitment  along  with  power  system  decision-making
process. [6].
It also helps to improve the weather measurement tech-
nique and design. Due to this weather and energy, fore-
casting can be enhanced.

•

•

•  More accurate wind forecasting helps in improving the
utilization  of  renewable  energy,  lowers  emissions  and
thus contributes to cleaner air.

•  Higher accuracy of prediction results in better turbine
protection, maintenance scheduling and to reduce dis-
ruptions when extreme weather conditions occur.

•  Accurate  forecasting  improves  reliance  on  renewable
energy, lowering emissions and contributing to cleaner
air.
The  forecasting  of  wind  depends  on  various  weather
parameters such as direction, humidity, temperature, speed,
and pressure. The traditional and cutting-edge approaches
are typically used to obtain precise forecasting, as shown in
Figure 2.

Traditional approaches include the persistence method,
physical  method,  and  statistical  method.  Cutting-edge
approaches,  such  as  machine  learning  and  artificial  intel-
ligence  techniques,  and  hybrid  techniques.  Traditional
approaches are stable, interpretable, and simple, while cut-
ting-edge  approaches  improve  accuracy,  adaptability,  data

638

INTRODUCTION

Several  organizations  are  moving  toward  the  produc-
tion  of  renewable  energy  in  the  current  energy  scenario.
The  sustainable  energy  sources  enhance  the  reliability
and  reduce  the  carbon  impact  of  power  systems  [1,2].
Wind energy is one of the most effective renewable energy
sources.  However,  because  of  its  intrinsic  variability  and
intermittent nature, integrating it into modern power net-
works is extremely difficult [3]. The need to switch to alter-
native  energy  sources  is  further  highlighted  by  the  rising
price of crude oil. Wind power continues to be one of the
most appealing renewable options because of its great effi-
ciency and low emissions. The installed wind power capac-
ity in India is shown in Figure 1.

Forecasting  of  wind  speed  and  power  is  essential  for
many tasks in the wind energy sector and for the general
functioning  of  the  power  system  [4].  For  those  involved
in  the  electrical  market,  such  as  energy  dealers  and  wind
farm operators, forecasting is crucial. Operators to sched-
ule  maintenance  and  improve  turbine  performance  use
predictions  of  wind  speed  and  power.  They  can  reduce
unplanned  outages  and  related  expenses  by  scheduling
maintenance during times of low wind by predicting wind
conditions [5]. When market-related decisions need to be
taken under uncertain circumstances, accurate forecasting
is also helpful.

Moreover, the long-term planning for wind farms and
further  extension  of  transmission  lines  is  supported  by
wind and/or power forecasts. Accurate wind forecasting is
also helpful to reduce the gap between planned and actually
generated  power,  thus  reducing  the  financial  risk  of  con-
tributors to the energy market. In brief, wind forecasting is
very  much  essential  for  using  the  wind  energy  efficiently,
smooth integration of grid, market operations, planning of

Figure 1. Installation capacity of wind power.

Sigma J Eng Nat Sci, Vol. 44, No. 1, pp. 637−662, February, 2026

639

Wind Pr ediction
Methods

Tr aditional
Methods

Cutting-Edge
Methods

Per sistanceMethod

Physical Method

Statistical Method

Ar tificial
Intelligent Method

Machine Lear ning
Method

Hybr id Method

Figure 2. Classification of wind speed/power prediction methods.

integration,  and  uncertainty  handling.  Both  approaches
have  their  significance  and  can  be  complementary,  pro-
viding  a  range  of  tools  and  techniques  for  wind  speed/
power  forecasting  that  can  be  tailored  to  specific  needs
and requirements. Other classifications of wind forecasting
schemes are (i) weather-based forecasting and (ii) time-se-
ries-based  forecasting  approaches  [7].  For  weather-based
forecasting models, the accuracy of wind forecasts is heav-
ily dependent on the morphology of the terrain at the loca-
tion  of  the  wind  turbines.  On  the  other  hand,  Statistical
methods  anticipate  future  values  only  based  on  historical
wind speed readings [8].

Research Gaps and Novelty

Many  previous  researches  have  been  done  on  wind
speed  and  wind  power  forecasting,  which  are  extensive
and cover a wide range of methods like traditional meth-
ods,  deep  learning  and  data-driven  methos,  and  hybrid
methods.  This  review  paper  differentiates  itself  from  pre-
vious works by providing a technically rigorous analysis of
traditional as well as state-of-the-art forecasting methods,
resulting in the following core contributions:
•  This  paper  comparess  the  traditional  and  modern
approaches  using  multiple  metrics,  while  previous
researches rely on individual models. The evaluation of
predictive/forecasting model is done on the basis of fac-
tors such as scalability, accuracy of forecasting, compu-
tational complexity as well as suitability across changing
forecasting horizons.

•  This review presents a complete examination of recent
developments,  including  future  hybrid  architectures
and novel learning techniques such as ensemble-based

and  deep  reinforcement  based  frameworks,  covered
minimally in present academic discourse.

•  This  paper  examines  the  real-world  models  ,  focuses
on  geographical  issues,  considers  grid  integration,
and  the  explores  the  need  for  support  during  real-life
conditions.

•  The  work  identifies  the  main  research  gap  and  gives
future direction for further improvement by making use
of IoT sensors in case of high-resolution data along with
a transparent model for improving accuracy.
Main goals of this paper are as follows::

•  To  provide  an  intensive  review  of  prior  research  on

•

wind speed/power prediction techniques.
Identification  of  gaps,  unresolved  questions,  and/or
areas requiring further investigation.

•  To  evaluate  traditional,  machine  learning,  and  hybrid
approaches  across  multiple  performance  metrics,  pro-
ficiency,  precision,  and  applicability  for  forecasting  of
wind, and evaluation of the latest hybrid machine learn-
ing algorithms.

•  A discussion on the working of models in real-life con-

ditions or applications.

•  To make contributions in advancing knowledge in field

of wind speed and/power prediction/forecasting.
The review provides guidance on forecasting methodol-
ogies which enable grid operators to adjust with variability
of wind power with higher precision, thus supporting more
stable  as  well  as  reliable  grid  operation.  This  paper  may
help the wind farm operators to choose the best models for
forecasting/prediction so as to improve the performance of
turbines and to reduce the unwanted mechanical stress. By
using cutting-edge techniques, wind farms will get highly
efficient  wind  power/energy.  The  participants  of  market

640

Sigma J Eng Nat Sci, Vol. 44, No. 1, pp. 637−662, February, 2026

can  easily  manage  the  varitions  in  generation  of  wind  by
knowledge of strength, and limitations of different forecast-
ing techniques discussed in this review.

The  review  is  also  helpful  to  scholars  in  highlighting
research gaps, providing opportunities alongwith new ideas
for  development  of  novel  models  with  innovative  ideas.
Moreover, this work is helpful to improve the efficiency and
accuracy of prediction/forecasting techniques. This review
also provides motivation to engineers to create more reli-
able as well as accurate prediction/forecasting systems. Its
findings  can  help  to  develop  standards  and  best  practices
for incorporating wind energy into the present grid infra-
structure,  ensuring  that  the  most  appropriate  forecasting
technologies  are  used.  This  study  analyzes  the  forecast-
ing results in several climate conditions, helping planners
prepare  for  climate-driven  shifts  in  wind  behaviors  and
thereby  supporting  the  maintenance  of  long-term  wind
energy viability.

CLASSIFICATION OF WIND SPEED/POWER
PREDICTION METHODS

Wind prediction methods can be classified into several
categories  based  on  their  approach,  complexity,  and  data
sources, and these categories are discussed below:

Traditional Approaches

The  time  series  and  statistical  methods  are  involove
in  traditional  approach  for  wind  forecasting  and  these
approaches are briefly discussed in Table 1.

Persistence Methods

Persistence is the humblest approach to predicting the
wind.  Persistence  forecasting  is  a  basic  and  straightfor-
ward  method  used  in  wind  speed/power  forecasting.  It
relies  on  the  assumption  that  the  future  wind  conditions
will be similar to the most recent past conditions. In some

incredibly  short  periods  of  predictions  (a  few  minutes  to
hours) [9], this simpler approach is even more reliable than
a Numerical Weather Prediction model. The model’s preci-
sion falls dramatically as the prediction lead time increases.
On  a  functional  level,  the  most  recent  available  wind
power  measurements,  as  provided  by  the  SCADA  system
[10], should be used. Persistence forecasting offers simplic-
ity and real-time applicability; it has limitations in capturing
changing  wind  conditions,  incorporating  external  factors,
and providing accurate forecasts beyond short time inter-
vals.  Every  forecast  technique  should  be  measured  com-
pared to the standard of the classic persistence approach to
evaluate  how  much  better  it  may  be  than  persistence-de-
rived forecasts [11].

Physical Methods

In  [12],  various  weather  based  models,  and  complex
atmospheric models are used for wind forecasting. Obstacle
shelter, local surface roughness and fluctuations, wind farm
layouts, orography influences, within wind farms, increas-
ing  local  wind  velocity,  speed  up  or  down,  and  wind  tur-
bine power curves are among the factors taken into account
in  these  models.  For  downscaling,  the  physical  method
employs  a  meso  or  micro-scale  model  that  interpolates
these wind speed projections to the level of wind producers
[13].

Figure  3  shows  the  forecasted  wind  speed  and  power
generated by the NWP model. Different NWP models are
utilized  in  a  model  chain  with  varied  hierarchical  levels
[14]. Meteorological observations made by meteorologists,
weather  monitoring  stations,  satellites,  and  other  sources
around the world serve as the model chain’s starting point
[15].  Long-term  wind  speed  predictions  are  better  served
by NWP (Numerical Weather Prediction) techniques and
have  been  found  to  save  up  to  20%  in  fossil  fuel.  Some
researchers related to the NWP technique for wind predic-
tion are given in Table 2.

Table 1. Classification of traditional models for wind forecasting

Category Method

Description

Persistence
methods

‘Persistence method’

Assumes that future wind conditions will be similar to the most recent past conditions.

‘Climatology method’

Uses long-term historical data to predict future wind patterns.

Physical
methods

‘Numerical weather
prediction (NWP) models’

Utilizes complex mathematical models based on atmospheric physics to simulate and
predict wind behavior.

Statistical
methods

‘Computational fluid
dynamics (CFD) models’

Uses numerical analysis and algorithms to solve and analyze problems involving fluid
flows, applied to wind behavior around structures and terrains.

‘Mesoscale models’

Focuses on atmospheric processes at the mesoscale (1-1000 km) to predict wind
patterns over larger regions.

‘Time series analysis’

Analyzes historical wind data to identify patterns and forecast future values.

‘Regression analysis’

‘ARIMA models’

Identifies relationships between wind speed and other variables (e.g., temperature,
pressure) to make predictions.

Auto-Regressive Integrated Moving Average models for capturing temporal
dependencies in wind data.

Sigma J Eng Nat Sci, Vol. 44, No. 1, pp. 637−662, February, 2026

641

Numer ical
Weather
Pr ediction
Data

Physical Model
of Wind
For ecasting

Wind Speed,
Dir ection,
Temp., ..

Power  Cur ve
Wake Effect

Pr edicted
Power

Land For m

Ther mal
Satisfaction

Contour
Line

…….

Geogr aphic Data

Figure 3. Physical model.

Table 2. Physical method for wind speed/power prediction

Authors

Title

Techniques

Accuracy

“Nested ensemble NWP approach for wind energy assessment”

NWP

RMSE=1.753

“A meteorological statistic model for short-term wind power forecasting” NWP,

RMSE= 1.6513

“A research on wind power forecasting techniques”

Liu et al.
(2022) [19]

“Numerical weather prediction enhanced wind power forecasting:
Rank ensemble and probabilistic fluctuation awareness”

Kalman filtering

NWP

NWP

Not determined

RMSE4=13.39%
RMSE16=18.89%

Al-Yahyai et al.
(2011) [16]

Marcos Lima et al.
(2017) [17]

Saini and Ahuja
(2019) [18]

Physical approaches are being used to improve the NWP
approach in the direction of achieving precise weather fore-
casts [20]. In [21], it is reported that the physical approaches
require a lot of computation, and they are displayed on super-
computers. The physical methods need weather parameters
for  precise  forecasting  [22].  Physical  systems  improve  the
final  output  (wind  prediction)  utilizing  the  unprocessed
information from Numerical Weather Prediction, depending
on the physics of the sub-atmospheric boundary layer [23].

Statistical Methods

Statistical modeling techniques are widely used in wind
speed/power  forecasting  to  capture  the  relationships  and
patterns in historical data. These techniques employ statis-
tical  principles  and  methods  to  analyze  past  observations
and  generate  forecasts.  The  correlation  between  online
average power data and other variables is examined using
statistical methods. Statistical models are easier to develop
and  maintain  than  other  models.  The  drawback  of  this
strategy is that the forecast inaccuracy rises as the forecast
period  rises  [11].  The  following  are  the  details  of  various
statistical models for wind speed/power forecasting:

Regression analysıs models ınclude the following:

Linear Regression

Simple linear regression models the relationship between
a dependent variable (e.g., wind speed) and a single indepen-
dent variable (e.g., temperature). Multiple linear regression
models extend simple linear regression by including multiple
independent variables to predict the dependent variable.

Non-Linear Regression

It  models  relationships  that  cannot  be  adequately
described with linear models. Techniques include polyno-
mial regression and other forms of regression that can han-
dle more complex relationships between variables.

Time  Series  Analysis  and  ARIMA  Models  include  the

following:

Moving Averages

•  Simple moving average (SMA)

Computes  the  arithmetic  mean  of  a  fixed  window  of
previous data points, providing a smoothed representation
of the time series.

642

Sigma J Eng Nat Sci, Vol. 44, No. 1, pp. 637−662, February, 2026

• Weighted moving average (WMA)

Follows the same principle as SMA but assigns varying
weights to the observations within the window, with more
emphasis typically placed on recent values.

•

Integrated (I) component
Applies  differencing  to  the  raw  data  to  remove  trends
or other non-stationary behavior, making the series more
suitable for modeling.

Exponential Smoothing
•  Simple exponential smoothing (SES)

Applies  exponentially  decreasing  weights  to  historical
observations,  giving  the  strongest  influence  to  the  most
recent data. It is most suitable for time series without evi-
dent trends or seasonal patterns.
•  Holt’s linear trend method

Extends  SES  by  incorporating  a  trend  component  in
addition to the level, enabling improved forecasting for data
exhibiting a linear trend but lacking seasonality.
•  Holt–Winters method

Builds upon Holt’s approach by adding a seasonal com-
ponent, making it appropriate for time series that simulta-
neously exhibit trend and seasonality.

ARMA (Autoregressive Moving Average) Models

It  combine  autoregressive  (AR)  and  moving  average
(MA)  processes  to  represent  a  time  series  using  both  its
lagged values and historical error terms [24]. These mod-
els capture short-term temporal dependencies as well as the
effects of past disturbances. Four general modeling strate-
gies are commonly adopted:
1.  Component-wise decomposition: Wind speed is sep-
arated  into  lateral  and  longitudinal  components  and
modeled independently.

2.  Dual  ARMA  modeling:  Separate  ARMA  models  are
used for wind speed and wind direction, and the results
are combined for forecasting.

3.  Vector  auto-regression  (VAR):  A  multivariate  frame-
work is used to forecast multiple interrelated wind char-
acteristics simultaneously.

4.  Reduced  VAR  models:  A  simplified  VAR  structure  is
implemented to reduce computational complexity while
maintaining prediction capability.
The ARMA model order is defined by both AR and MA
orders, indicating how many past values and past errors are
included in the model.

ARIMA (Autoregressive Integrated Moving Average) Models
ARIMA models extend ARMA by introducing a differ-
encing step to enforce stationarity—meaning that the mean
and  variance  of  the  series  remain  constant  over  time.  An
ARIMA model is defined by three parameters:
•  Autoregressive (AR) component

Represents  the  relationship  between  the  current  value
and  several  lagged  observations.  AR  models  assume  the
time series can be expressed as a linear combination of its
historical  values  plus  random  noise  [25].  They  are  effec-
tive  for  modeling  short-term  structure,  trends,  and  serial
correlations.  Because  wind  speed  exhibits  sequential
dependence  and  inherent  variability,  ARMA  and  ARIMA
frameworks are often well-suited for its prediction.

•  Moving average (MA) component

This component uses the effect of past forecast/predic-
tion errors values on the present value. MA models repre-
sent the present values as a linear combination of previous
ones.  The  model’s  order  helps  to  determine  how  many
lagged error values are considered.

State-Space Models

State-space  models  help  to  represent  the  underlying
process in terms of combination of unobserved-states and
observations.  They  help  in  providing  more  flexibility  to
capture complex relationships and these can help to handle
different data patternsThese models include Kalman filter
aswell as Bayesian models. Statistical modeling techniques
provide  a  solid  framework  for  analyzing  and  forecasting
wind  speed/power  data.  The  choice  of  the  appropriate
model depends on the characteristics of the data, the pres-
ence of trends or seasonal patterns, and the desired forecast-
ing horizon. These techniques have been widely employed
in  practice  and  form  the  foundation  for  more  advanced
and hybrid models used in wind speed/power forecasting.
Literature work on wind forecasting using statistical meth-
ods has been done by some researchers. The AR, ARMA,
ARIMA, Bayesian approach, and grey forecasts are all statis-
tical approaches. These approaches can be utilized to tackle
difficulties  in  fields  such  as  engineering,  economics,  and
science disciplines that include a large amount of data and
interdependent  explanations.  For  wind  speed  prediction,
[26]  proposed  a  combination  of  two  models,  i.e.,  ARMA
and  wavelet  transform.  The  low-frequency  characteristics
of  the  entire  wind  speed  are  extracted  using  the  wavelet
transform. In [27], an Auto Regression Integrated Moving
Average approach outperforms the BPNN (back propaga-
tion  neural  network)  in  forecasting  short-term  intermis-
sions. In [28], a Bayesian methodology has been proposed
to describe the wind resource and estimate one-hour-ahead
wind  speeds.  The  modeling  outcome  has  shown  that  the
Bayesian  approach  can  be  operative  for  the  prediction  of
wind speed and power.

For  predicting  short-term  fluctuations  in  wind  power,
an approach that depends on a Markov-switching auto-re-
gressive (AR) approach with a time-varying coefficient was
developed in [29]. The approach has the advantage of being
simple to use in calculating full predictive densities. In [30],
the authors propose an autoregressive conditional hetero-
scedastic (ARCH) model. In [31], the hourly average wind
speed is predicted using the autoregressive moving average
and the persistence model. Authors in [32] have examined
the  use  of  an  auto-regressive  integrated  moving  average
approach  for  time-series  forecasting  using  wind  speed
observations. For short-term forecasts, the ARIMA model

Sigma J Eng Nat Sci, Vol. 44, No. 1, pp. 637−662, February, 2026

643

has been demonstrated to outperform the ANN model [33].
In [34], three different samples of wind speed data are used
to test the validity of the ARIMA model that is being pro-
posed.  Given  that  the  hour-ahead  forecast  takes  no  more
than five minutes to compile, the proven prediction inaccu-
racy of less than 16% is quite an accomplishment. In [35],
Time series analysis, ARIMA, and Ordinary Least Squares
(OLS) multiple regression have been used to predict wind
speeds.  In  [36],  Non-stationary  annual  wind  speed  data
are  analyzed  using  the  Fractional  Autoregressive  Moving
Average  (FARIMA)  Model.  A  comparison  has  been  con-
ducted  between  the  F-ARIMA  model  and  the  Persistence
and ARIMA models in [37], and it has been found that the
F-ARIMA  model  is  superior  at  capturing  the  long-term

and  short-term  properties  of  time-series  observations.
In  [38],  Wind  Speed  Forecasting  Based  on  Second  Order
Blind Identiﬁcation (SOBI) and Autoregressive (AR) Model
has resulted in higher accuracy compared with direct fore-
casting. In [39], short-term wind power forecasts based on
ARX  models  have  been  shown  to  give  better  accuracy  in
forecasting. Some researchers related to the statistical tech-
niques for wind prediction are given in Table 3.

Wind  is  a  stochastic  variable,  it  is  difficult  to  antici-
pate due to its non-stationary and nonlinear features [45].
Statistical  weather  forecasting  models  have  also  outper-
formed  numerical  weather  forecasting  models  [46].  The
above literature survey helps to identify the strengths and
limitations of statistical methods as listed in Table 4.

Table 3. Statistical Methods for Wind Speed/Power Prediction

Authors

Li et al.
(2022) [40]

Wang et al.
(2020) [41]

Title

Techniques

Accuracy

“A Wind Speed Correction Method Based on Modified Hidden
Markov Model for Enhancing Wind Power Forecast.

Markov

“Forecasted Scenarios of Regional Wind Farms Based on Regular
Vine Copulas”

KDE, R-vine

RMSE = 3.093
MAE = 2.451

RMSE = 0.1089
MAE = 0.075

Mararakanye et al.
(2022) [42]

Incorporating Spatial and Temporal Correlations to Improve
Aggregation of Decentralized Day-Ahead Wind Power Forecasts”

KNN, KDE

MAE = 3.18;
RMSE = 4.63; R2 = 0.94

Yu et al.
(2020) [43]

Dong et al.
(2022) [44]

Probabilistic Prediction of Regional Wind Power Based on Spatio-
temporal Quintile Regression.

SQR

“Power Prediction Based on Multi-class Autoregressive Moving
Average Model with Logistic Function”

ARMA

RMSE = 16.62%;
MAE = 11.23%

RMSE = 127.10
MAPE = 1.25%

Table 4. Strengths and limitations of statistical methods

Parameters

Strengths

Statistical models can work with readily available
historical wind data.

Limitations

Less Accuracy with data sparsity

Data availability

Simplicity

Interpretability

Computational
speed

Adaptability

Assumption
flexibility

Forecast updates

Implementation is simple and easy

Difficult to capture complex nonlinear data.

Results are interpretable, aiding in
understanding the factors affecting wind speed.

Less computational power required

May not observe all relevant weather variables.

Its prediction accuracy is low for highly dynamic and
nonlinear wind patterns.

Use for short-term and long-term wind
predictions.

It may not easily identify extreme events and rapid wind
variability.

Flexibility in choosing the appropriate statistical
distribution (e.g., normal, Weibull) for wind data.

It can be updated with new data easily, making it
suitable for real-time applications.

Assumptions about the data distribution may not always hold.

Less accuracy in clamite changing regions.

Noise handling

Easily handle noisy data

Low performance in highly non-linear wind condition

Historical patterns

Use for long-term wind speed patterns and trends. May not account for sudden shifts or local microclimatic

influences.

Risk assessment

Provides a foundation for risk assessment and
resource allocation.

It may not be suitable for critical applications requiring
high precision.

Model transparency Transparency in model structure and parameters

makes it accessible to a wider audience.

Lack of robustness in situations where statistical
assumptions are violated.

644

Sigma J Eng Nat Sci, Vol. 44, No. 1, pp. 637−662, February, 2026

CUTTING-EDGE APPROACHES

The cutting-edge approaches use advanced approaches
and data for more accurate wind forecasting. Table 5. Shows
the  classification  of  cutting-edge  approaches  for  wind
forecasting.

Machine Learning and AI Methods

Machine  learning  methods  can  determine  intricate
nonlinear  correlations  and  patterns  in  wind  speed/power
data that conventional statistical models may not capture.
This can lead to improved forecasting accuracy, especially
for  long-term  and  nonlinear  predictions.  Machine  learn-
ing  algorithms  can  adapt  and  learn  from  new  data  [47].
Machine  learning  algorithms  can  automatically  select  rel-
evant features from a large set of potential predictors. This
helps  in  identifying  the  most  important  factors  influenc-
ing wind speed/power, eliminating irrelevant features, and
reducing model complexity[48].

The  machine  learning  approaches  used  for  the  pre-
diction  of  solar  radiation  [49],  wind  potential  [50],  and
short-term  traffic  flow  [51].  And  handle  large  data  with
complex  computation.  Machine
learning  approaches
give  highly  accurate  outcomes  for  wind  forecasting  at
various  time  scale  intervals  from  from  single  turbine  to
entire wind farm [52,53]. RBF (Radial basis function) out-
performs  both  linear  and  nonlinear  functions  in  neural
networks, and it is best suited for the prediction of wind
speed  [54,55].  Genetic  algorithms  (GA)  which  are  algo-
rithms  based  on  evolution  thus  expressing  individual
qualities  through  genetics  [56].  Approximate  reasoning
is  possible  using  fuzzy  sets  and  fuzzy  logic.  Fuzzy  logic
is a field of study that depends on generalization and CI
(computational intelligence) principles. The fuzzy simula-
tion outperformed the persistent technique in predicting
wind  speed  as  of  30  minutes-2  hrs.  ahead.  In  [57],  vari-
ous neural networks are used to predict wind speed such
as  Long  Short-Term  Memory  (LSTM),  Artificial  Neural
Network (ANN), Convolutional Neural Network (CNN),
and  Convolutional  LSTM  (ConvLSTM)  hybrid  model.
These  algorithms  can  capture  temporal  dependencies

and long-term patterns in wind speed/power data, mak-
ing them effective for predicting future values. In [58], a
grouped  strategy  has  been  provided  for  predicting  wind
power 10 minutes ahead of time. A persistence approach,
a  BPNN  (Back  Propagation  Neural  Network),  and  an
RBFNN (Radial Basis Function Neural Network) are com-
bined in the suggested method. Table 6. Provide insights
into  the  underlying  algorithms  used  in  machine  learn-
ing-based forecasting models. It includes the classification
of machine learning algorithms in four broad classes, i.e.,
supervised  learning,  unsupervised  learning,  deep  learn-
ing, and ensemble methods. Further sub-classification of
each category, along with a brief description of the appli-
cations of each algorithm, is also given.

Table 7 and Table 8 respectively summarize the state-of-
the-art contributions from various researchers in the field
of machine learning and deep learning methods for wind
prediction.

Wind forecasting is done utilizing an upgraded form of
EMD (EEMD), complementary ensemble EMD (CEEMD),
and complete ensemble EMD with adaptive noise (CEEMD)
in [105] (CEEMDAN). Even though EMD looked to beat
many  conventional  approaches  (Persistence  &  ARMA),
the  authors  state  that  there  seemed  to  be  a  problem  with
approach  mixing  [106],  in  which  different  IMFs  contain
signals in the same frequency range.

Hybrid Methods

In  recent  years,  attention  has  switched  to  hybrid  fore-
casting  systems,  i.e.  combination  of  two  or  more  two  or
more  prediction  methods  and  then  aggregating  them  as
shown in Figure 4 [107]. Machine learning techniques can
be  combined  with  traditional  statistical  models  to  create
hybrid models.

Combining  an  autoregressive  integrated  moving  aver-
age (ARIMA) model with machine learning algorithms can
improve forecasting accuracy by incorporating both statis-
tical  properties  and  complex  patterns  in  the  data.  Hybrid
methods such as ANN-ARIMA [108], PSO-ANFIS [109],
and  WT-NN  (Wavelet  transform  Neural  Network)  [110].
For a short period of wind power prediction in Portugal, an

Table 5. Classification of cutting-edge approaches

Category

Approaches

Detail

Machine Learning
& AI approaches

‘Supervised Learning’

Prediction is based on labeled data by using random foreast, regression, aupport
vector machine, and decision trees.

‘Unsupervised Learning’

Prediction is based on unlabeled data and identify pattern using clustring.

‘Deep Learning,

For complex sequence prediction various neural networks are used like CNN
(Convolutional neural network), RNN ( recurrent neural networks), and LSTM
(long short-term memory) networks

‘Ensemble Methods’

Enhance prediction accuracy by combining multiple algorithms.

Hybrid approaches

‘Combination
Techniques’

Enhance the accuracy by combination of two approaches

Sigma J Eng Nat Sci, Vol. 44, No. 1, pp. 637−662, February, 2026

645

Table 6. Algorithms for machine learning-based models

Algorithm
category

Supervised
learning

Algorithm

Detail

Application

‘Linear Regression’

İt provide relationship between a dependent
variable and a single independent variable.

Appropriate for linear relationships
between variables.

‘Decision Trees’

‘Random Forests’

‘Support Vector
Machines (SVM)’

leverages decision rules constructed from
variables to divide data into branches.

Analyzes interactions and non-linear
correlations between features.

A number of decision trees that have been
trained on variable subsets of characteristics
and data.

Evaluates which hyperplane best matches
the data for regression or divides the data
into several classes.

Avoids overfitting in comparison to single
trees and offers reliable forecasts.

Appropriate for complicated interactions
and high-dimensional spaces.

‘K-Nearest Neighbors
(KNN)’

Forecasting based on the k-nearest training
examples in the feature space.

Easy to use and efficient for low-noise
brief datasets.

Unsupervised
learning

‘K-Means Clustering’

Partitions data into k clusters based on
feature similarity.

Finds trends and clusters in wind data.

‘Hierarchical
Clustering’

Uses divisive techniques to create a
hierarchy of clusters.

Recognizes the relation between wind
speed patterns and data structure.

Deep learning

‘Artificial Neural
Networks (ANN)’

Layers of interconnected neurons acquire
the ability to map inputs to outputs.

Identifies intricate, non-linear
interactions; processing and huge
quantities of data are needed.

‘Recurrent Neural
Networks (RNN)’

Long Short-Term
Memory (LSTM)
Networks

Convolutional Neural
Networks (CNN)

Ensemble
methods

Bagging (Bootstrap
Aggregating)

RNN retains memories through
connections that form a temporal sequence.

Suitable for anticipating time series based
on historical trends.

An distinctive kind of RNN with long-term
dependency learning capabilities.

Useful in identifying long-term patterns
and trends in time series forecasting.

Although it may be used to 1D time series,
this neural network is mainly used for
image recognition.

Increases accuracy and stability by
averaging predictions from several models
trained on various subsets.

Captures local patterns and trends in
wind data.

Reduce variation and overfitting for better
predictions.

Boosting

Sequentially trains models, focusing on the
errors of previous models.

Enhance the forecasting accuracy by
reducing bias and variance.

Historical
Measured Data

Weather Data

Figure 4. Hybrid model.

Determinis tic
Forecasting Model

Probabilis tic
Forecasting Model

Probabilis tic wind
Power Forecas ting

646

Sigma J Eng Nat Sci, Vol. 44, No. 1, pp. 637−662, February, 2026

Table 7. Machine Learning Methods for Wind Speed/Power Prediction

Authors

Jyothi et al.
(2016) [59]

Xu and Mao
(2016) [60]

Catalão et al.
(2009) [61]

Mabel et al.
(2008) [62]

Singh et.al.
(2007) [63]

Marugán et al.
(2018) [64]

Sharma et al.
(2018) [65]

Sideratos et al.
(2012) [66]

Title

“Very-short-term wind power forecasting through
Adaptive wavelet neural network”

Techniques

Accuracy

WNN, ANN, ANFIS MSE = 0.25

“Short-term wind power forecasting based on elman
neural network with particle swarm optimization”

ENN, PSO

“An artiﬁcial neural network approach for short-
term wind power forecasting in Portugal”

“Analysis of wind power generation and prediction
using ANN: A case study”

ANN

ANN

“Wind power estimation using artificial neural
network”

ANN, Kalman
filtering

“A survey of artiﬁcial neural network in wind energy
systems”

“A review of wind power and wind speed
forecasting”

ANN

ANN

RMSE = 0.367

ERMS = 16.55%

RMSE = 0.0362

RMSE = 0.0806

Not determined

more than 80%
of accuracy

RMSE = 2.849 (1 hr)

“Probabilistic wind power forecasting using radial
basis function neural networks”

RBFNN

--

Ramadevi and Bingi
(2022) [67]

“Chaotic time series forecasting approaches using
machine learning techniques: A review”

Machine learning

Not determined

Zhou et al.
(2022) [68]

Lee et al.
(2020) [69]

Tu et al.
(2020) [70]

Tan et al.
(2020) [71]

“Performance ımprovement of very short-term
prediction intervals for regional wind power based
on composite conditional nonlinear quantile
regression”

WMTSM and
conditional
LP (CLP)

“Wind power prediction using ensemble learning-
based models”

“Short term wind power prediction based on data
regression and enhanced support vector machine”

Ensemble learning
models
(GRF, RF, XGB)

EBSO and LSSVM

“Ultra-Short-Term Wind Power Prediction by Salp
Swarm Algorithm-Based Optimizing Extreme
Learning Machine”

SSA-ELM

Huang et al.
(2023) [72]

“Priori-guided and data-driven hybrid model for
wind power forecasting”

Priori-guided and
data-driven hybrid
model

Both MAE and RMSE
of less than 10%

R2 = 98.9;
RMSE = 50.36;
MAE = 23.63

MAE (m/s): 0.723
RMSE (m/s): 0.932

MAPE = 1.2677
RMSE = 0.2576

MAE = 0.0861,
RMSE = 0.1262,
R2 = 0.8333,
AR = 87.38%

“A hybrid intelligent framework for forecasting
short-term hourly wind speed based on machine
learning”

Intelligent hybrid
model

MAPE = 2.62 and
RMSE = 0.14

Wang et al.
(2023) [73]

Pombo et al.
(2022) [74]

Moayyed et al.
(2022) [75]

Liu et al.
(2023) [76]

Nascimento et al.
(2023) [77]

“Assessing stacked physics-informed machine
learning models for co-located wind–solar power
forecasting”

Stacked physics-
informed machine
learning model

“A Cyber-Secure generalized supermodel for wind
power forecasting based on deep federated learning
and image processing. Energy Convers”

Cyber-secure
generalized
supermodel

“An online transfer learning model for wind
turbine power prediction based on spatial feature
construction and system-wide update”

A transformer-based deep neural network with
wavelet transform for forecasting wind speed and
wind energy”

Online transfer
learning model

Discrete wavelet
transform

RMSE = 5% and
R2 = 0.95

RMSE = 0.02,
MAE = 0.007
MAPE = 0.60

MAE = 84.837
RMSE = 134.837

100 m RMSE [m/s] = 0.383
150 m RMSE [m/s] = 0.368
120 m RMSE [m/s] = 0.375

RMSE [kW] = 76.18

Sobolewski et al.
(2023) [78]

“Gradient boosting-based approach for short-
and medium-term wind turbine output power
prediction”

Goddard earth
observing system
model

Yu et al.
(2023) [79]

Wang et al.
(2023) [80]

Research on Hierarchical Control Strategy of ESS
in Distribution Based on GA-SVR Wind Power
Forecasting.

“Short-Term Wind Power Prediction by an Extreme
Learning Machine Based on an Improved Hunter–
Prey Optimization Algorithm”

SVR

RMSE/MW = 14.7435

RMSE (kW) = 50.55

Improved hunter-prey
optimization (IHPO
algorithm-based
extreme learning
machine (ELM)

Sigma J Eng Nat Sci, Vol. 44, No. 1, pp. 637−662, February, 2026

647

Table 8. Deep learning method for wind speed/power prediction

Authors

Title

Lin et al.
(2020) [81]

“Wind power prediction based on high-
frequency SCADA data along with isolation
forest and deep learning neural networks”

Ahuja and Saini
(2023) [82]

“Recurrent Neural Network for Chaotic Wind
Speed Time Series Prediction”

Wang and Li
(2023) [83]

Mert
(2021) [84]

“Wind speed interval prediction based on
multidimensional time series of Convolutional
Neural Networks”

“Agnostic deep neural network approach to the
estimation of hydrogen production for solar-
powered systems”

Hu et al.
(2020) [85]

“Very Short-Term Spatial and Temporal Wind
Power Forecasting: A Deep Learning Approach”.

Dong et al.
(2022) [86]

“Spatio-temporal Convolutional Network Based
Power Forecasting of Multiple Wind Farms”

Jalai et al.
(2022) [87]

“New Hybrid Deep Neural Architectural
Search-Based Ensemble Reinforcement
Learning Strategy forWind Power Forecasting”

Sun and Zhao
(2020) [88]

“Short-Term Wind Power Forecasting Based on
VMD Decomposition, ConvLSTM Networks
and Error Analysis”

Miao et al.
(2021) [89]

“Ultra-Short-Term Prediction of Wind Power
Based on Sample Similarity Analysis”

Liao and Yang
(2022) [90]

“Wind GMMN: Scenario Forecasting for Wind
Power Using Generative Moment Matching
Networks”

Techniques

“Deep Learning Neural Network
(DLNN) & SCADA”

Accuracy

MSE = 0.0032

RNN

CNN

“Agonistic Deep learning neural
network”

“A convolution-based spatial–
temporal wind power predictor
(CSTWPP)”

“The spatiotemporal
convolutional network
(STCN) with a directed graph
convolutional structure”

“Adeep-optimized convolutional
LSTM-based ensemble
reinforcement learning strategy
(DOCLER)”

“A variational mode
decomposition (VMD) and
convolutional long short-term
memory network (Conv LSTM)
model”

“The CNN-MLSTMs-T Model”

RMSE = 0.2497

RMSE1 = 0.2805
RMSE2 = 0.3021
RMSE3 = 0.2838

RMSE = 0.0703

MASE = 190.02
RMSE = 7.49

MAEs = 3.17%
RMSEs = 2.88%,

RMSE = 7.1322%
MAE = 4.6713%

MRE(KW) = 0.016
MAE(KW) = 792
MSE(KW) = 568,305
RMSE(KW) = 1252.32

RMSE = 0.1998;
MAE = 0.1523

“Generative moment matching
network (GMMN)”

RMSE = 127.10;
MAE = 0.6855 MW

Huang
(2022) [91]

“Wind Power Generation Forecast Based on
Multi-Step Informer Network”

“Multi-step informer network
(MSIN)”

Wu and Jiang
(2022) [92]

“Short-TermWind Power Prediction Based
on Data Decomposition and Combined Deep
Neural Network”

“Long short-term memory
neural network (LSTM) with
the improved particle swarm
optimization algorithm (IPSO)”

Multi-step informer
Network (MSIN) improves
forecast accuracy by 29%
compared with the
informer network for RMSE

MAE = 2.92668;
RMSE = 3.59604

Yu, et al.
(2022) [93]

Liu et al.
(2023) [94]

“Short-term wind power prediction for
regional wind farms based on spatial-temporal
characteristic distribution. Renew”

“Spatiotemporally multiple
clustering and I–CNN-BILSTM
deep learning network.”

“A unified multi-step wind speed forecasting
framework based on numerical weather
prediction grids and wind farm monitoring data”

“The unified forecast based on
STC-DPN And The single-site
error correction of TCN-LSTM”

MAE = 18.64,
RMSE = 28.45

MAE = 2.071,
RMSE = 2.431,

Hossain et al.
(2021) [95]

“Very short-term forecasting of wind power
generation using hybrid deep learning model”

“Hybrid deep learning model”

Garg and
Krishnamurthi
(2023) [96]

“A CNN encoder decoder LSTM model for
sustainable wind power predictive analytics”

“CNN-ED-LSTM model”

MAE = 1.59,
RMSE = 3.73
and MAPE = 8.13.

MSE = 0.0102
MAPE = 46.24
MAE = 0.0623
RMSE = 0.1012

648

Sigma J Eng Nat Sci, Vol. 44, No. 1, pp. 637−662, February, 2026

Table 8. Deep learning method for wind speed/power prediction (continued)

Authors

Title

Techniques

Accuracy

Zhang et al.
(2021) [97]

“Power prediction of a wind farm cluster based
on spatiotemporal correlations”

“Long short-term memory
(LSTM) neural network”

RMSE (MW) = 0.94
MAE (MW) = 0.67
MAPE (%) = 49.71

RMSE = 129.3
MAE = 81.1

Zhang et al.
(2020) [98]

Lliao et al.
(2022) [99]

Tian et al.
(2022) [100]

Yildiz et al.
(2021) [101]

Liu et al.
(2023) [102]

Wang et al.
(2023) [103]

“Short-term wind power forecasting approach
based on Seq2Seq model using NWP data”

“Seq2Seq model”

“Short-term power prediction for renewable
energy using hybrid graph convolutional network
and long short-term memory approach”

“Long short-term memory
(LSTM)”

RMSE (MW) = 1.27
MAE (MW) = 0.90

“Developing a wind power forecasting system
based on deep learning with attention mechanism”

“A deep learning model
(gated recurrent unit, GRU)”

RMSE = 111.9766

“An improved residual-based convolutional
neural network for very short-term wind power
forecasting”

“Short-term wind power forecasting based on
feature analysis and error correction”

“Artificial intelligent power forecasting for wind
farm based on multi-source data fusion”

“Residual CNN-based deep
forecasting method”

1-h ahead.

RMSE = 0.9947

“Bidirectional long short-term

RMSE/MW = 1.0822

memory network (BiLSTM)”

“The encoder-decoder
framework is constructed with
LSTM as the basic Unit”

RMSE = 0.1243

RMSE (%) = 10.23

Xiao et al.
(2023) [104]

“Wind power short-term forecasting method
based on LSTM and multiple error correction”

LSTM

NNWT technique that depends on the integration of ANN
and  WT  (wavelet  transform)  has  been  proposed,  which
has  proven  to  be  both  new  and  effective.  Its  MAPE  out-
performs persistence, ARIMA, and NN techniques with an
average value of 6.97 percent and a calculation time of less
than 10 seconds. Wavelet- SVM (Support vector machine)
optimized  by  GA  (genetic  algorithm)  [111],  Kalman  fil-
ter-ANN  (KF+ANN)  [112],  WT-  SVM-GA  (Wavelet-
Support vector machine) optimized by genetic algorithm &
EMD+SVM (Support vector machine with empirical mode
decomposition) [113] are some work reported in this liter-
ature. To build a unique grouped simulation for wind speed
forecast, authors in [114] have proposed combining EMD
with feature selection. Hybrid forecasting approaches have
lately become popular due to their extra benefits over tra-
ditional single forecasting methods. Candenas and Rivera
established  a  wind  forecasting  model  that  is  based  on
ARIMA-ANN  [115]  with  a  fixed  prediction  horizon.  For
the prediction of multi-step wind speed, a hybrid approach
that includes WDT (wavelet decomposition transform), an
exciting  learning  machine,  and  adjustment  for  extremes
methodology  is  proposed  in  [116].  Li  et  al.  proposed  a
mixed technique that depends on continuous and flexible
weight  for  predicting  short  periods  of  wind  speeds  [117].
In [118] to identify oscillations brought on by nearby wind
generators  and  send  the  necessary  inputs  to  modeling,
a  novel  short-period  wind  forecasting  approach  is  being
deployed.  In  [119],  an  attribute  selection  model  depend-
ing  upon  a  k-means  cluster,  and  an  MLPNN  (multi-layer
perceptron neural network) were created to forecast short

periods of wind speed. For a short period wind speed pre-
diction,  correlation-based  DWT,  LSSVM,  and  GARCH.
The  contributions  to  the  LSSVR  (Least  Squares  Support
Vector  Regression)  wind  speed  forecasts  are  evaluated
using  correlation  coefficients  among  different  sub-series
introduced  by  [120].  State-of-the-art  hybrid  models  for
wind prediction are detailed in Table 9.

In  [142],  authors  have  proposed  and  validated  an
improved  BFGS
(Broyden-Fletcher-Goldfarb-Shanno)
neural network (using four wind speed datasets) and wave-
let transform-signal processing method for short periods of
wind speed forecasts. After wavelet decomposition, correla-
tion coefficients are calculated for each sub-series to iden-
tify  their  comparative  relevance.  In  this  study  [143],  the
hybrid  model  possesses  a  more  accurate  forecasting  abil-
ity than the other models, and the level of accuracy of the
hybrid model is different from that of the GRNN, BPNN,
LSSVM,  CS-BPNN,  WOA-LSSVM,  EMD-WOA-LSSVM,
and  EEMD-WOA-LSSVM.  In  this  study,  a  system  that
combines NWP and hybrid wind forecasting ANN models
is proposed. This hybrid forecasting approach is beneficial
in improving the perception of wind power in China [144].
In  [145],  two  grouped  models  for  wind  power  and  speed
prediction: ARIMA-ANN & ARIMA-SVM have been pro-
posed.  This  research  systematically  and  comprehensively
analyzes the use of the suggested hybrid models. In [146],
authors have employed a new hybrid wind speed forecast
approach  that  is  dependent  on  a  BPNN  and  the  knowl-
edge of using periodic exponential forecasting adjustment
to  remove  seasonal  impacts  from  authentic  wind  speed

Sigma J Eng Nat Sci, Vol. 44, No. 1, pp. 637−662, February, 2026

649

Table 9. Hybrid method for wind speed/power prediction

Authors

Title

Techniques

Accuracy

Hong et al.
(2019) [121]

“Hybrid deep learning-based neural network for
24-h ahead wind power forecasting”

CNN-MFNN, CNN- RBFNN,
CNN- RBFNN-DGF

Foley et al.
(2012) [122]

Shetty et al.
(2016) [123]

Peng et al.
(2013) [124]

Wang et al.
(2018) [125]

“Current methods and advances in the
forecasting of wind power generation”

NWP, statistical, machine
learning

“Optimized radial basis function neural
network model for wind power prediction”

RBFNN, FCM, PSO-FCM,
Extreme Learning Machine

MSE = 0.0034 at
no. of center 60 model 1

“A hybrid strategy of short-term wind power
prediction”

“A novel hybrid forecasting system of wind
speed based on a newly developed multi-
objective sine cosine algorithm (MOSCA)”

ANN+ Physical

CEEMD- MOSCA- WNN

Saini and Ahuja
(2017) [126]

“Wind speed prediction using wavelet
transform and artificial neural network”

ANN, WT

Saini and Ahuja
(2019) [127]

“Wind speed prediction using wavelet transform
and GA trained artificial neural network”

ANN, WT, GA

Duan et al.
(2022) [128]

“A combined short-term wind speed forecasting
model based on CNN–RNN and linear
regression optimization considering error”

CNN-RNN

Zhang et al.
(2022) [97]

“A comprehensive wind speed prediction system
based on Monte Carlo and artificial intelligence
algorithms”

AI

Zou et al.
(2022) [129]

“Forecasting of short-term load using the
MFF-SAM-GCN model”

Aisyah et al.
(2022) [130]

“Exploratory Weather Data analysis for
electricity load forecasting using svm and grnn,
case study in Bali, Indonesia”

“A multi-feature fusion
self-attention mechanism
graph convolutional network
(MFF-SAM-GCN) forecasting
model”

GRNN, SVM

Zhao et al.
(2023) [131]

“Hybrid VMD-CNN-GRU-based model
for short-term forecasting of wind power
considering spatio-temporal features”

VMD-CNN-GRU

Che et al.
(2023) [132]

Hu et al.
(2021) [133]

“Ultra-short-term probabilistic wind power
forecasting with spatial-temporal multi-scale
features and K-FSDW based weight”

“Hybrid forecasting method for wind power
integrating spatial correlation and corrected
numerical weather prediction”

 Wen et al.
(2022) [134]

“A new hybrid model for power forecasting of a
wind farm using spatial–temporal correlations”

I-CNN-BILSTM

“The hybrid forecasting
method based on the
corrected NWP data and the
SC”

“KHC algorithm for
clustering, components
extraction and selection
with SVD, and building SVR
forecast model”

Hu et al.
(2021) [135]

“An improved deep belief network based hybrid
forecasting method for wind power”

“GBRBM-DBN consists of the
PCA, NWP, and SC for wind
power Forecasting”

RMSE = 2.6018,
MAPE = 0.2859,
MAE = 2.3857

RMSE of Winter = 375.2369
RMSE of Spring = 352.2999
RMSE of Summer = 221.3698
RMSE of Autumn = 194.2075

Not Described

MAE = 757.25 (KW)
NRMSE = 2.01%

RMSE1 = 0.078693
RMSE2 = 0.118740
RMSE3 = 0.192665
RMSE4 = 0.143523

RMSE = 0.1576

RMSE1 = 0.1172
RMSE2 = 0.1017
RMSE3 = 0.2104
RMSE4 = 0.1876

RMSE = 0.5794

RMSE = 0.0284
SMAPE = 9.453%
MBE = 0.025
R2 = 0.989

The GRNN model gives the CC
value of 0.956, RMSE of 28.82
The SVR model gives a CC
value of 0.965 and an RMSE of
44.40.

RMSE = 1.5651,
MAE = 0.8161,
MAPE = 11.62%,
and R2 = 0.9964.

MAPE (%) = 4.86,
MAE = 18.64,
and RMSE = 28.45.

RMSE = 1.238,

MAPE = 0.325,

MAE = 0.7002

MAE = 0.273
RMSE = 0.343

650

Sigma J Eng Nat Sci, Vol. 44, No. 1, pp. 637−662, February, 2026

Table 9. Hybrid method for wind speed/power prediction (continued)

Authors

Title

Gu et al.
(2023) [136]

Al-Duais and
Al-Sharpi
(2023) [137]

Yan et al.
(2022) [138]

“Short-term wind power forecasting and
uncertainty analysis based on FCM–WOA–
ELM–GMM”

Techniques

FCM-WOA-ELM-GMM
Model

“A unique Markov chain Monte Carlo method
for forecasting wind power utilizing time series
model”

“Seasonal autoregressive
integrated moving average
(SARIMA) model”

“Uncovering wind power forecasting
uncertainty sources and their propagation
through the whole modeling chain. renew.
sustain”

“Historical wind climate
model and

RMSE = 13%
MAE = 20.7%

physical model”

Xiong et al.
(2022) [139]

“Short-term wind power forecasting based on
Attention mechanism and deep learning”

“AMC-LSTM hybrid model”

Accuracy

MAE = 3.8%,
RMSE = 5.24%

RMSE = 13.09
MAPE = 1.03

MSE = 0.8951
MAE = 0.0505
RMSE = 0.0946

RMSE = 1.8313

Zhang et al.
(2023) [140]

Wu et al.
(2024) [142]

“Deterministic and probabilistic prediction
of wind power based on a hybrid intelligent
model”

“Interpretable wind speed forecasting with
metrological feature exploring and two-stage
decomposition”

“XGBoost, Tree, SVR,
and BPNN methods”

IEEMD-EWT-JADE-TFT

RMSE = 0.1063

information. The outcomes of the tests have revealed that
the proposed strategy outperformed a single BPNN.

In  [147],  authors  employed  a  hybrid  method  depend-
ing on the integration of ANN and WT for a short period
of wind energy forecasting in Portugal. Using the wavelet
approach, the wind power series is decomposed into a set
of effective constituent sequences. Results of the tests indi-
cate that the proposed hybrid approach for predicting wind
production  has  a  proportion  of  promise.  Hybrid  models’
main purpose is to integrate the advantages of each model
to  attain  global  forecasting  performance  [148].  In  [149],
forecasting the average daily wind speed using a predicting
scheme based on discrete wavelet transform (DWT) asso-
ciated with Artificial Neural Networks (ANN ) is proposed,
and the results show that, when using ANN for prediction,
the  db4  wavelet  with  a  5-level  decomposition  is  the  most
appropriate wavelet for wind speed forecasting in the three
considered  regions.  Also,  the  proposed  scheme  exhibits
high precision and accuracy for one-day-ahead wind speed
forecasting in terms of RMSE and MAPE. In [150], authors
have  employed  a  grouped  intellectual  model  termed  an
ANFIS  (Adaptive  Neural  Fuzzy  Inference  System)  that
combines  two  AI  approaches,  Fuzzy  Logic,  and  ANN,  to
estimate wind constraint and energy production shortly. In
[151], depending on wavelet and classical time series anal-
ysis  approaches,  a  new  short-period  prediction  algorithm
is  employed.  An  adaptive  neuro-fuzzy  inference  system
(ANFIS) is utilized in [152] to anticipate wind direction 2.5
minutes ahead, taking into account both direction & speed.
In this study, artificial intelligence techniques, such as the
ANN  algorithm,  are  utilized  to  anticipate  wind  power
[153]. To predict wind power, four alternative approaches

were applied. It has been discovered that the Genetic algo-
rithm  outperforms  the  other  models  when  it  comes  to
training data sets.

In [154], three approaches for predicting wind speed are
proposed. Which hybrid models proposed, such as Wavelet
packet-BFGS  (Broyden–Fletcher–Goldfarb–Shanno),  have
been demonstrated to be superior to Wavelet packet-ARI-
MA-BFGS. Second, Wavelet packet-BFGS has been discov-
ered to be superior to Wavelet-BFGS. In [155], four different
models for the prediction of wind power are presented. The
two  learning  algorithms,  the  backpropagation  algorithm
and  the  genetic  algorithm,  along  with  a  combination  of
these  models,  are  used  for  the  prediction  of  wind  power.
The genetic algorithm performs better for both the training
data sets than the other models. In [156], the system con-
sists  of  two  main  parts:  a  point  prediction  module  based
on  a  nonlinear  combination  and  an  interval  prediction
module based on fuzzy clustering. It is of great significance
to  explore  the  predictability  and  modeling  of  wind  speed
comprehensively. Unlike previous works, the authors have
implemented a BP neural network using MOEA/D (Multi-
objective evolutionary algorithm based on decomposition)
optimization  as  a  novel  nonlinear  combination  mecha-
nism to derive final prediction results, which enhances the
accuracy of point prediction and improves final prediction
accuracy. Wind speed predictions in a short period utiliz-
ing  mathematical  models  that  include  ANN  and  Hybrid
time-series models are given in [157].

The  back  propagation  neural  network  (BPNN)  algo-
rithm is integrated with GA and PSO in [158] to create an
integrated  prediction  model  for  short-period  wind  farms.
The output power is calculated using climatic data gathered

Sigma J Eng Nat Sci, Vol. 44, No. 1, pp. 637−662, February, 2026

651

by a WSN (wireless sensor network), which is then sent into
the BP neural network as an input variable. In [159], BPNN
is a basic prediction method, and the proposed prediction
method  is  validated  by  the  output  power  prediction  of  a
real wind farm. A support vector machine (SVM) is chosen
as  another  basic  prediction  method  to  test  the  versatility
of the proposed improved prediction method. The results
show that the proposed wind power prediction method can
improve the prediction accuracy by about 8%.

In [160], the SARIMA-EEMD-LSTM hybrid prediction
model is used to forecast wind speed time series at 15-, 30-,
and 60-minute intervals. Thus, hybrid methods can effec-
tively  forecast  wind  speed/power  wind  power  generation
fluctuations must be anticipated by power system operators
to control grid operations and plan rotating backup power
[161]. Authors in [162] have utilized a fusion of neural net-
works and fuzzy logic approaches to precisely estimate the
production of a wind farm. A self-organised map that cate-
gorises the input data into distinct groups is used.

It  is  found  that  there  is  a  significant  improvement  in
prediction accuracy achieved through hybrid models, with
Root Mean Square Error values of 0.1089 m/sec for statisti-
cal methods from Table 3, 0.02 m/sec for intelligent meth-
ods from Table 7, and 0.0096 m/sec for hybrid approaches
from Table 9.

Organization  of  Wind  Prediction  According  to  time
Scale Horizons

Methodologies  based  on  prediction  period  may  be
classified as extremely short-period predicting, short-term
predicting,  long-term  predicting,  and  long-term  predict-
ing.  Wind  prediction  organization  based  on  time  scale  is
discussed below:
•  Very Short-Term (Seconds to Minutes):

The  significance  of  these  predictions  lies  in  their
necessity  for  jobs  that  demand  accuracy  in  real-time  or

near-real-time  scenarios.  The  applications  of  the  technol-
ogy  encompass  a  range  of  areas,  including  wind  energy
production  control,  wind  gust  prediction,  and  emergency
response in the context of severe weather occurrences.
•  Short-Term (Minutes to Hours):

This  wind  forecasting  is  used  in  various  sectors  like
managing  transportation,  power  system  management,
wind farm operation, traffic systems, and several outdoor
activities.
•  Medium-Term (Hours to Days):

This  forecasting  is  important  for  various  sectors  that
depend on weather conditions, such as scheduling for gen-
eration,  several-day  span  forecasting  planning,  construc-
tion market operation, etc.
•  Long-Term (Days to Weeks):

These  forecasts  are  employed  in  various  sectors  such
as  large-scale  infrastructure  planning,  assessing  climate
change impacts, and choosing the best site for wind farm
installation.
•  Seasonal (Months to Seasons):

The seasonal wind forecasting is used in various fields,
including  agriculture,  energy  infrastructure  investment,
and long-range climate projections.
•  Climate (Years to Decades):

The significance of climate-scale wind predictions is to
enhance  our  comprehension  of  long-term  wind  patterns
and their potential impacts on regional and global climate
systems.  The  applications  of  the  research  encompass  cli-
mate analysis, the formulation of policies, and the creation
of measures for adaptation. Table 10 gives a classification of
state-of-the-art work on the basis of forecasting horizons.

Comparison of Traditional and Cutting-Edge Approaches
Based  on  findings  from  numerous  research  studies,  a
comparison of the traditional and cutting-edge approaches

Table 10. Classification of the review works based on the forecasting time scale

Time Scale

Reviewed Work

Ultra Short-term

[88,89]

[73,78,81,83,88,94,101,105,137]

[80,88,92,93,95,96,98,106,146]

[49,88,90,142]

Short term

[76,77,80-82,91,99,102,104,134-136,139,142-144]

[77,89,136,139,142]

[77,89,136,139,142]

[77,136,139,141,142]

[77,139,141,142]

[77,139,141]

[45-47,77,93,97,136,138,140,141]

[74,75,91,141]

Time Resolution

5 min

10 min

15 min

30 min

1 h

2 h

3 h

4 h

6 h

12 h

24 h

48 h

Medium-term

[142]

72 h–1 week

652

Sigma J Eng Nat Sci, Vol. 44, No. 1, pp. 637−662, February, 2026

Table 11. Comparison between traditional and Cutting-Edge approaches

Metric

Accuracy

Computational
efficiency

Ease of
ımplementation

Traditional approaches

Machine learning approaches Hybrid approaches

Average

High

Very high

It requires low computational
resources, so effeciency is
high.

It requires significant
computational resources, so the
effeciency is average.

It depends on the complexity of the
hybrid model, so the effeciency is low.

Easy to implement

Complex to implement and often
considered a “black box.”

İt involves integrating multiple models,
which increases complexity.

Data requirements Work with small datsets

İt requires large, high-quality
datasets

Scalability

Easily scalable on standard
hardware.

Scalable but requires specialized
infrastructure like GPUs.

It requires substantial data and
preprocessing, especially when integrating
different models.

Low to moderate; scaling depends on the
integration of traditional and machine
learning components.

Energy consumption Low

High

Very high

Interpretability

Applicability
to short-term
forecasting

Applicability to
medium-term
forecasting

Applicability
to long-term
forecasting

High; models are generally
easy to understand and
explain.

Low; often difficult to interpret
the inner workings of the model.

Low to moderate; interpretability depends
on the combination of methods used.

High

Average

Low

High

High

High

Very high.

Very high

High

on  the  basis  of  accuracy,  resources,  robustness,  and  data
requirements etc. is given in Table 11.

From  Table  11,  it  can  be  inferred  that  although
Traditional  methods  offer  ease  of  use  and  interpretabil-
ity,  they  are  often  sufficient  for  short-term  forecasts.  The
Cutting-edge approaches provide significant improvements
in accuracy and adaptability, especially for complex, non-
linear wind forecasting problems. They are better suited for
environments with rapidly changing conditions and where
higher  computational  resources  are  available.  It  is  equally
important to consider the Practical implications of differ-
ent forecasting techniques in real-world applications. Table
12 represents the implications of different forecasting tech-
niques, particularly in terms of their adaptability to differ-
ent geographical contexts and real-time operational needs.

Process of Wind Speed/Power Forecasting

The procedure for training and validation of wind data
for  both  techniques,  such  as  traditional  &  cutting-edge
approaches, is shown in Figure 5. Many steps of wind fore-
casting that are represented in Figure 5 were discussed in
the previous section. The various types of data pre-process-
ing and advanced techniques reported in this study are used
to improve the performance of wind forecasting. The most
important among these are:

•  Data  Cleaning:  Addressing  missing  observations
through  methods  such  as  imputation  and  eliminating
outliers  to  ensure  dataset  consistency  and  accuracy.
This  reduces  systematic  errors  and  increases  model
robustness.

•  Standarization:  It  is  applied  to  input  variables  on  a
comparable scale, there by enhance the stability, train-
ing, and overall efficiency.

•  Feature  Extraction:  It  is  the  process  of  choosing  and
transforming  essential  features  from  primary  data,  to
enhance  models  performance  such  as  derived  indica-
tors, lag based features etc.

•  Time Series Decomposition: By applying decomposi-
tion, the time series is divided into seasonal, tendency,
and remaining components. After decomposition, each
can be trained separately, and then the results outcomes
more precise.
•  Dimensionality

(Principal
Reduction:
Component  Analysis)  can  be  used  to  increase  gener-
alization,  computing  complexity,  and  dimensionality
reduction.
These  steps  help  to  improve  the  data  quality  ,  predic-
tion  accuracy,  decrease  noise,  and  thus  help  to  produce
more reliable as well as stable predictions. Moreover, stan-
dard  evaluation  metrics  that  can  be  used  for  identifying

PCA

Sigma J Eng Nat Sci, Vol. 44, No. 1, pp. 637−662, February, 2026

653

Table 12. Practical implications of different forecasting techniques

Forecasting technique

Adaptability to geographical contexts

Real-time operational needs

‘Statistical methods’

Average adaptability

‘Physical models’

High adaptability across diverse regions

Low computational demand, suitable for short-
term forecasts but less effective in dynamic
weather conditions.

High computational resources required; effective
for medium to long-term forecasts but slower in
real-time.

‘Machine learning’

‘Hybrid models’

‘Ensemble methods’

High adaptability, especially when trained on
region-specific data, can handle complex, non-
linear relationships.

Requires substantial computational resources
and real-time data input; performance improves
with data availability.

Enhanced adaptability by leveraging the strengths
of multiple methods; flexible across various
terrains and climates.

Balances computational demand and accuracy;
effective in both short-term and long-term
forecasting, with real-time application potential.

Highly adaptable, as they aggregate diverse models
to improve overall accuracy across different
regions.

Moderate to high computational demand; offers
improved reliability in real-time operations due
to averaging out model errors.

the accuracy and use of wind prediction/forecasting mod-
els by having a comparison of predicted and actual values.
Common metrics include:

 MSE: It stands for mean square error (MSE), which is
commonly used in wind forecasting, but is an underutilized
method. If the MSE indicates a higher value, then the mod-
el’s performance is low, and vice versa. This method can be
used where unexpected data may offer perceptive informa-
tion about the issue. MSE is calculated by Eqn 1.

A precise, comprehensible indicator of prediction accu-
racy is offered by MAE. Because it does not need squaring
the errors, it is less affected by outliers than RMSE.Lower
MAE  values  indicate  better  model  performance,  with  0
being the ideal score (perfect predictions).

MAPE: Mean  Absolute Percentage Error (MAPE) is a
commonly used statistical measure for evaluating the accu-
racy of forecasting or prediction models. It is widely used
in various areas, i.e., data analytics, statistics, and econom-
ics, and it demonstrates average error as a percentage of the
actual value.

(1)

RMSE:  The  root  mean  square  error  (RMSE)  refers  to
the  square  root  of  the  mean  squared  error  (MSE).  The
introduction  occurs  when  the  magnitude  of  the  error  is
equivalent to the magnitude of the objective. It is calculated
by Eq. 2.

(2)

RMSE penalizes larger errors more heavily than MAE
due to the squaring of errors. It is helpful for analyzing the
variance of errors because it gives a measure of the standard
deviation of prediction errors. Better model performance is
shown by lower RMSE values; 0 is the optimal score.

MAE:  The  average  of  the  absolute  variations  between
the  expected  and  predicted  values  is  known  as  the  mean
absolute error, or MAE. The average gives equal weight to
each individual difference. Compared to the MSE, this sta-
tistic is less affected by outliers. The MAE is determined by:

(3)

(4)

If the MAPE indicates a lower value, then the model’s
performance is highly accurate & vice versa. The MAPE is
sensitive  when  actual  values  are  close  to  zero,  which  may
outcomes in division by zero error.

R2:  It  demonstrates  the  total  variance  percentage  of
data  that  can  be  analyzed  by  the  model  performance.  It
gives a measure of predicted values matched to the actual
outcomes.

(5)

Traditional  forecasting  techniques  are  typically  evalu-
ated using metrics such as RMSE, MAE, and occasionally
MAPE. Such methods focus on capturing temporal depen-
dencies and recurring cycles in wind speed or power data,
using  error  measures  that  reflect  deviations  from  histori-
cal  averages.  While  the  cutting-edge  approaches  are  eval-
uated by using RMSE, MAE, MAPE, and R2 metrics. And
enhance the performance of these approaches by adjusting
model sturucture, hyper parameters.

654

Sigma J Eng Nat Sci, Vol. 44, No. 1, pp. 637−662, February, 2026

Start

Data collection

Data cleaning  &
preprocessing

Data splitting
(training, validation, testing)

Model selection for traditional models
(AR, MA, ARIMA,SVR etc. )

Model selection for AI models
(Neural network, Random forest etc. )

Model training
(fit model to training data)

Cross validation and testing the
data

Calculate matrix
(MAE,RMSE, MAPE)

Deployment
(Deploy finalized model for
forecasting)

stop

Figure 5. Flow chart of models training and validation.

Numerical Case Study

Data Description

In  this  section,  some  popular  Wind  speed  forecasting

models are compared using a real-world dataset.

The  wind  speed  data  is  collected  from  open  websites
(https://maps.nrel.gov/wind-prospector/). The dataset was

Sigma J Eng Nat Sci, Vol. 44, No. 1, pp. 637−662, February, 2026

655

collected  from  March  1st,  2023  to  May  2023  with  a  time
resolution of 1 hour. The first 70% of the data points were
used  as  training  samples,  and  the  remaining  30  %  of  the
data points were used as test data.

Experimental Setting

The models compared in the case studies can be divided
into  four  groups:  traditional  benchmark  models,  machine
learning  models,  deep  learning  models,  and  hybrid  deep
models.  Six  traditional  benchmark  models  were  selected,
namely AR, MA, ARMA, ARIMA, SARIMA, and GARCH.
The Machine Learning and deep Learning models used were
ANN, RNN, and hybrid CNN-RNN models. In hybrid mod-
els, CNN was used to extract features, which were then fed
into the other deep models to make wind speed forecasts.

RESULTS AND DISCUSSION

The  wind  speed  forecasting  results  of  different  models
are presented in Table 13. It can be seen that the hybrid intel-
ligent model shows the best performance. This phenomenon
shows  that  nonlinear  models  characterize  the  fluctuations
of WS/WP more accurately and are more suitable than lin-
ear models for WS/WP forecasting. In order to measure the
forecasting  performance  of  different  models,  four  forecast-
ing  error  indicators  were  used:  mean  square  error  (MSE),
root mean square error (RMSE), mean absolute percentage
error  (MAPE),  and  symmetric  mean  absolute  percentage
error (SMAPE). Mean Squared Error (MSE) and Root Mean
Squared Error (RMSE) are used to give more weight to only
larger errors, while MAE is used to give equal weightage to
all  types  of  errors,  and  SMAPE  is  used  to  assessi  percent-
age-based  errors  only,  thus  making  them  suitable  for  dif-
ferent  perspectives.  ARMA  model  included  in  traditional
statistical  approaches  shows  superior  performance  with
values  of  RMSE,  SMAPE,  MAE,  and  MSE  respectively  as
1.6622, 0.1178, 1.3537, and 2.7632, respectively. Due to tem-
poral dependencies, this model is efficient for wind predic-
tions & is also more accurate for forecasting short-term data
as compared to otherer statistical models.

There are some neural network models which are more
advanced, e.g., Recurrent Neural Networks (RNN) models,
mainly used to improve the forecasting accuracy. The RNN
model has better performance than basic ANN models with
values of RMSE, SMAPE, MAE, and MSE as 1.3935, 0.0924,
1.0382,  and  1.9420,  respectively  as  reported  in  literature.
Main qualities of a RNN includes retaining the information
from  previous  time  steps.  This  model  is  helpful  for  wind
speed forecasting that has influence on future patterns. In
contrast,  traditional  ANN  model(s)  lack  these  qualities,
thus their ability to captue (fully) the time-dependent struc-
ture  (in  the  data)  is  limited.  CNNs  have  shown  superior
performance  for  wind  prediction/forecasting  with  RMSE,
SMAPE, MAE, and MSE values of 1.6622, 0.1178, 1.3537,
and  2.7632,  respectively.  To  further  improve  forecast-
ing/prediction  accuracy  in  the  future,  hybrid  CNN-RNN
models are used to extract the spatial features and capture
temporal dependencies at the same time. The CNN-RNN
approach  is  found  to  be  effective  for  forecasting  of  wind
speed, thus showcasing more reliable and accurate forecast-
ing as compared to simple neural networks models. These
models have helped to achieve RMSE, SMAPE, MAE, and
MSE values of 0.9641, 0.0648, 0.7235, and 0.9295, respec-
tively which is far better than basic ANN & RNN models.

This study surveys various wind-forecasting techniques,
which  include  traditional,  machine  learning  based,  and.  It
has evaluated short-term and long-term forecasting models
for different time scales and location (s). Table 13 is showcas-
ing  a  comparison  of  various  models’  performance,showing
that the use of machine learning based model can decrease
the  error  by  30%  in  comparison  to  traditional  approach,
while  the  use  of  hybrid  approach  helps  to  further  enhance
the accuracy, i.e., reduces error. The prior survey(s) in this
field  only  focused  on  general  challenges  such  as  quality  &
availability  of  data  along  with  improvement  in  forecast-
ing  accuracy.  This  study  further  outlines  future  directions
of research, e.g., using the Internet of Things (IoT) for the
purpose of real-time forecasting and development of various
adaptive models considering changes in climate.

Table 13. Comparison between all models’ performance

Techniques

Conventional statistical models

Intelligence models

Metrics

AR

MA

ARMA

ARIMA

SARIMA

GARCH

ANN

RNN

Hybrid model

CNN-RNN

MSE

2.7640

2.7715

2.7632

3.2792

2.9123

4.8473

1.9951

1.9420

0.9295

MAE

1.3522

1.3571

1.3537

1.5569

1.4178

1.5793

1.0848

1.0382

0.7235

RMSE

1.6625

1.6647

1.6622

1.8108

1.7065

2.2016

1.4124

1.3935

0.9641

SMAPE

0.1177

0.1180

0.1178

0.1178

0.1219

0.1629

0.0969

0.0924

0.0648

656

CONCLUSION

Sigma J Eng Nat Sci, Vol. 44, No. 1, pp. 637−662, February, 2026

Area  of  wind  forecasting  covers  a  wide  range  of  tra-
ditional  as  well  as  cutting-edge  approaches.  Traditional
approaches have been utilized since many years, and have
been  proven  to  be  reliable  in  many  applications.  These
approaches are generally simple, interpretable, and requir-
ing  fewer  computational  resources.  These  include  the
methods  like  persistence  models,  numerical  weather  pre-
diction  (NWP),  etc.  and  have  formed  the  foundation  of
wind forecasting inspite of having some limitations like less
accuracy, and difficulty in handling sophisticated non-lin-
ear patterns.

Cutting-edge  approaches  use  data  processing  tech-
niques. These techniques easily deal with challenges of deal-
ing with high-dimensional data and composite forecasting.
These  techniques  are  capable  of  providing  high  accuracy
and  flexibility  alongwith  managing  variable  climate  con-
ditions.  Hybrid  models,  integrating  multiple  forecasting
methodologies with use of diverse data source(s), are likely
to dominate the future of wind prediction. Accurate fore-
casting  is  in  fact  critical  for  optimizing  the  generation  of
renewable  energy,  efficiently  managing  the  operations  of
power grid, and supporting the development of a sustain-
able energy system. This paper reviews the current research
and  highlights  the  future  directions  to  increase  the  accu-
racy of wind forecasting and is of great help for researchers
and practitioners.

Challenges & Future Directions

Data collection and data availability are main concerns
strongly related with wind forecasting challenges and future
directions. Major obstacles in this field are as follows:
1.  Data sparstiy: Wind time series data is not available for
some time intervals and sometimes for some geograph-
ical location. This issue poses challenge in analyzing the
model performance.

2.  Data  resolution:  Low-resolution  data  (wind)  reduces
forecast  accuracy  for  short-term  predictions  which
requires  high-frequency  information.  There  may  be
requirement  of  recording  of  Wind  measurements  at
varying  temporal  intervals  (e.g.,  hourly  or  every  15
minutes).

3.  Data  quality  and  calibration:  Small  errors  may  lead
to a big mistake in prediction produced by sensor mis-
calibration  of  sensor  and/or  equipment  malfunction.
Therefore,  regular  cheking  and  device  maintaince  are
essential.

4.  Missing  data:  Missed  datasets  are  very  common  Due
to sensor failures and/or other technical issues, problem
of missing data becomes common. For reliable forecast-
ing, it becomes essential to handle missing data values.
5.  Spatial variability: Due to topography and local geog-
raphy, Wind speed variation is observed over short dis-
tances. Recording this variability becomes challenging
in absence of time-grained spatial data.

Table 14. Research Gaps In Future Research Directions of Wind Speed/Power Prediction

Underexplored Field

Research Gap

Future Research Directions

Integration of IoT technologies for
real-time data acquisition

Limited use of IoT devices in capturing high-
resolution, real-time environmental data.

Develop and deploy IoT networks for
continuous data collection to improve
forecasting accuracy and responsiveness.

Use of machine learning which are
interpretable

Long-term wind power forecasting

Extreme weather event prediction

Geographical and terrain variability

Energy storage integration

Social and environmental impact
assessment

Most machine learning models are complex
and lack transparency, making them hard to
interpret.

Focus on developing explainable AI
techniques that offer transparency while
maintaining prediction accuracy.

Existing models primarily focus on short-
term forecasting; long-term predictions
remain less accurate.

Research into hybrid models combining
machine learning and climate models to
improve long-term forecasts.

Poor accuracy in forecasting wind speed/
power during extreme weather conditions
like storms or hurricanes.

Develop specialized models that can
accurately predict wind patterns under
extreme conditions, incorporating climate
change factors.

Inadequate adaptation of forecasting models
to complex terrains and diverse geographic
regions.

Create region-specific models that account
for local topography and microclimates,
leveraging high-resolution geographic data.

Insufficient research on integrating wind
forecasting with energy storage management
systems.

Explore real-time integration of forecasting
models with energy storage solutions to
optimize grid stability and energy use.

Limited consideration of the socio-
environmental impacts of wind power
forecasting and deployment.

Conduct interdisciplinary research assessing
the social and environmental implications of
wind forecasting technologies.

Sigma J Eng Nat Sci, Vol. 44, No. 1, pp. 637−662, February, 2026

657

6.  Temporal variability: It includes random fluctuations,
rapid as well as seasonal change in wind data, making
accurate wind forecasting difficult.

7.  Long-Term trends and climate change: Nature of wind
data is stochastic, nonlinear, and non-stationary. Which
makes it necessary to provide high-quality data (over a
long period of time) for accurate forecasting.

8.  Data  consistency:  Variations  in  datasets  caused  by
Changes in location of station and/or sensor, and meth-
ods  of  measurement  can  make  datasets  variable  and
must be avoided to ensure high prediction accuracy.
9.  Data privacy and access: Due to proprietary concerns,
it becomes difficult to get the historical wind data.
10. Data  integration:  Merging  of  datasets  from  various
sources  is  generally  seen  in  prediction  which  is  also
challenging.
In  the  current  era,  although  wind  forecasting  has
improved  a  lot  by  using  various  modern  approaches,  yet
further  improvement  is  necessary  for  increasing  the  fore-
casting  reliability.  Future  research  work  should  focus  on
development  of  the  best  methods  which  helps  to  balance
the  forecasting  accuracy  and  computational  efficiency.  It
is necessary that data from actual wind farms needs to be
validated model-wise, while considering wind farm obser-
vations  and  various  atmospheric  conditions  incorporated
via simulation studies. Table 14 highlights the unexplored
fields, research gaps and directions for future work in the
area of wind speed and/power forecasting.

In  conclusion,  however  previous  reviews  have  estab-
lished a base to understand various wind forecasting meth-
ods, this paper is an extension of that work and provides a
comprehensive, quantitative as well as a prospective evalu-
ation. For improving the wind speed and power prediction,
this paper helps to identify the gaps in literature and is pro-
viding useful insights. It covers methodologies for improve-
ments, discusses theoretical concerns, points out real-world
applications while strengthening the present knowledge. It
is providing the researchers, business professionals, and all
other stakeholders with a solid foundation for the purpose
of enhancing the wind energy forecasting tools.

AUTHORSHIP CONTRIBUTIONS

Authors equally contributed to this work.

DATA AVAILABILITY STATEMENT

The  authors  confirm  that  the  data  that  supports  the
findings of this study are available within the article. Raw
data that support the finding of this study are available from
the corresponding author, upon reasonable request.

CONFLICT OF INTEREST

The  author  declared  no  potential  conflicts  of  interest
with respect to the research, authorship, and/or publication
of this article.

ETHICS

There are no ethical issues with the publication of this

manuscript.

STATEMENT ON THE USE OF ARTIFICIAL
INTELLIGENCE

Artificial  intelligence  was  not  used  in  the  preparation

of the article.

REFERENCES

  [1]  Dhiman  HS,  Deb  D,  Foley  AM.  Bilateral  Gaussian
wake  model  formulation  for  wind  farms:  A  fore-
casting-based approach. Renew Sustain Energy Rev
2020;127:109873. [CrossRef]

  [2]  Dhiman HS, Deb D, Guerrero JM. Hybrid machine
intelligent  SVR  variants
forecasting
and  ramp  events.  Renew  Sustain  Energy  Rev
2019;108:369–379. [CrossRef]

for  wind

  [3]  Dhiman HS, Deb D, Foley AM. Lidar assisted wake
redirection in wind farms: A data-driven approach.
Renew Energy 2020;152:484–493. [CrossRef]

  [4]  Wu YK, Hong JS. A literature review of wind fore-
casting technology in the world. In: IEEE Lausanne
PowerTech Conference; 2007. p.504–509. [CrossRef]

  [5]  Wang X, Guo P, Huang X. A review of wind power
forecasting  models.  Energy  Procedia  2011;12:770–
778. [CrossRef]

  [6]  Kumar  J,  Charles  R,  Kumar  DV,  Majid  MA.  Wind
in  India.  Energy  Environ

energy  programme
2019;30:1135–1189. [CrossRef]

  [7]  Okumus  O,  Dinler  A.  Current  status  of  wind  energy
forecasting and a hybrid method for hourly predictions.
Energy Convers Manag 2016;123:362–371. [CrossRef]

  [8]  Ying C, Yunu D, Jie D, Zhibao C, Rongfu S, Hai Z.
A statistical approach of wind power forecasting for
grid scale. AASRI Proced 2012;2:121–126. [CrossRef]

  [9]  Chang  WY.  A  literature  review  of  wind  forecasting
methods. J Power Energy Eng 2014;2:161–168. [CrossRef]
[10]  Milborrow  D.  Forecasting  for  scheduled  delivery

wind power. Wind Power Mon 2003.

[12]

[11]  Lange  M,  Focken  U.  New  developments  in  wind
energy forecasting. In: Proc IEEE Power Energy Soc
Gen Meet; 2008. p. 1–8. [CrossRef]
Soman  SS,  Zareipour  H,  Malik  O,  Mandal  P.  A
review  of  wind  power  and  wind  speed  forecasting
methods  with  different  time  horizons.  In:  IEEE
Power Energy Soc Gen Meet; 2010. [CrossRef]
[13]  Landberg  L.  A  mathematical  look  at  a  physical
power  prediction  model.  Wind  Energy  1998;1:23–
28. [CrossRef]

[14]  Kariniotakis  G,  Pinson  P,  Siebert  N,  Giebel  G,
Barthelmie R. The state of the art in short-term pre-
diction of wind power from an offshore perspective.
In: SeaTech Week–Ocean Energy Conference; 2004.

658

Sigma J Eng Nat Sci, Vol. 44, No. 1, pp. 637−662, February, 2026

[15]  Foley  AM,  Leahy  PG,  McKeogh  EJ.  Wind  power
forecasting  and  prediction  methods.  In:  Int  Conf
Environ Electr Eng (EEEIC); 2010. p. 61–64. [CrossRef]
[16]  Yahyai  A,  Sultan  Y,  Charabi  Y,  Badi  AA,  Gastli  A.
Nested  ensemble  NWP  approach  for  wind  energy
assessment. Renew Energy 2012;37:150–160. [CrossRef]
[17]  Lima JM, Guetter AK, Freitas SR, Panetta J, Mattos
JGZ.  A  meteorological–statistic  model  for  short-
term  wind  power  forecasting.  J  Control  Autom
Electr Syst 2017;28:679–691. [CrossRef]
Saini S, Ahuja M. A research on wind power fore-
casting  techniques.  Int  J  Recent  Technol  Eng
2019;8:578–580.

[18]

[19]  Liu  C,  Zhang  X,  Mei  S,  Zhen  Z,  Jia  M,  Li  Z,  et  al.
Numerical weather prediction enhanced wind power
forecasting:  Rank  ensemble  and  probabilistic  fluc-
tuation  awareness.  Appl  Energy  2022;313:118769.
[CrossRef]

[31]  Milligan  M.  IEA  task  25:  Design  and  operation  of
power  systems  with  large  amounts  of  wind  power.
IEA Rep 2003.

[32]  Palomares-Salas  JC,  de  La  Rosa  JJG,  Ramiro  JG,
Melgar  J,  Agüera  A,  Moreno  A.  Comparison  of
models for wind speed forecasting. 2009.

[33]  Tyass A, Bellat A, Raihani A, Mansouri K, Khalili T.
Wind  speed  prediction  based  on  seasonal  ARIMA
model. E3S Web Conf 2022. [CrossRef]

[34]  Palomino  K,  Reyes  F,  Núñez  J,  Valencia  G,  Acosta
RH.  Wind  speed  prediction  based  on  univariate
ARIMA  and  OLS  on  the  Colombian  Caribbean
coast.  J  Eng  Sci  Technol  Rev  2020;13:200–205.
[CrossRef]

[35]  Das  J,  Banerjee  R.  Estimation  of  long-range  cor-
relations  and  FARIMA  modeling  of  wind  speed
in  Maharashtra.  In:  IEEE  PES  Asia-Pacific  Power
Energy Eng Conf; 2017. p.1–6. [CrossRef]

[20]  Zhao  X,  Wang  S,  Li  T.  Review  of  evaluation  crite-
ria  and  main  methods  of  wind  power  forecasting.
Energy Procedia 2011;12:761–769. [CrossRef]

[36]  Kavasseri  RG,  Seetharaman  K.  Day-ahead  wind
speed  forecasting  using  f-ARIMA  models.  Renew
Energy 2009;34:1388–1393. [CrossRef]

[21]  Valdivia-Bautista  SM,  Domínguez-Navarro

JA,
Pérez-Cisneros  M,  Vega-Gómez  CJ,  Castillo-Téllez
B.  Artificial  intelligence  in  wind  speed  forecasting:
A review. Energies 2023;16. [CrossRef]
Shawon SMRH, Saaklayen MA, Liang X. Wind speed
forecasting by conventional statistical methods and
machine learning techniques. In: IEEE Electr Power
Energy Conf; 2021. p.304–309. [CrossRef]

[22]

[23]  Erdem  E,  Shi  J.  ARMA-based  approaches  for  fore-
casting the tuple of wind speed and direction. Appl
Energy 2011; 88:1405–1414. [CrossRef]

[24]  Aggarwal SK, Gupta M. Wind power forecasting: A
review  of  statistical  models.  Int  J  Energy  Sci  2013;
3:1–10.

[25]  Wang JQZ, Zhang X. Wind power forecasting based
on  time  series  ARMA  model.  IOP  Conf  Ser  Earth
Environ Sci 2018;199. [CrossRef]

[26]  Ling-ling L, Li JH, He PJ, Wang CS. The use of wave-
let  theory  and  ARMA  model  in  wind  speed  pre-
diction. In: Int Conf Electr Power Equip Switching
Technol; 2011. p.395–398. [CrossRef]

[27]  Miranda  MS,  Dunn  RW.  One-hour-ahead  wind
speed  prediction  using  a  Bayesian  methodology.
In:  IEEE  Power  Eng  Soc  Gen  Meet;  2006.  p.  1–6.
[CrossRef]

[28]  Le Goff Latimier R, Le Bouedec E, Monbet V, Monbet
Markov  V.  Switching  autoregressive  modeling  of
wind power forecast errors. 2020; p.189. [CrossRef]
Song  Z,  Jiang  Y,  Zhang  Z.  Short-term  wind  speed
forecasting  with  Markov-switching  model.  Appl
Energy 2014;130:103–112. [CrossRef]

[29]

[30]  Torres  JL,  García  A,  de  Blas  M,  de  Francisco  A.
Forecast of hourly average wind speed with ARMA
models in Navarre (Spain). Sol Energy 2005;79:65–
77. [CrossRef]

[37]  Narayana  M,  Putrus  G,  Jovanovic  M,  Leung  PS.
Predictive  control  of  wind  turbines  by  considering
wind  speed  forecasting  techniques.  In:  Int  Univ
Power Eng Conf; 2009. p.1–4.

[38]  Firat  U,  Engin  SN,  Murat  S,  Ertuzun  AB.  Wind
speed forecasting based on second order blind iden-
tification  and  autoregressive  model.  In:  Int  Conf
Mach Learn Appl; 2010. p.686–691. [CrossRef]
[39]  Duran  MJ,  Cros  D,  Riquelme  J.  Short-term  wind
power forecast based on ARX models. J Energy Eng
2007;133:172–180. [CrossRef]

[40]  Li M, Yang M, Yu Y, Lee WJ. A wind speed correc-
tion  method  based  on  modified  hidden  Markov
model  for  enhancing  wind  power  forecast.  IEEE
Trans Ind Appl 2022;58:656–666. [CrossRef]

[41]  Wang  Z,  Wang  W,  Liu  C,  Wang  B.  Forecasted  sce-
narios of regional wind farms based on regular vine
copulas. J Mod Power Syst Clean Energy 2022;8:77–
85. [CrossRef]

[42]  Mararakanye N, Dalton A, Bekker B. Incorporating
spatial and temporal correlations to improve aggre-
gation of decentralized day-ahead wind power fore-
casts. IEEE Access 2022;10:116182–116195. [CrossRef]
[43]  Yu Y, Han X, Yang M, Yang J. Probabilistic predic-
tion  of  regional  wind  power  based  on  spatiotem-
poral  quantile  regression.  IEEE  Trans  Ind  Appl
2020;56:6117–6127. [CrossRef]

[44]  Dong Y, Ma S, Zhang H, Yang G. Wind power pre-
diction based on multi-class autoregressive moving
average model with logistic function. J Mod Power
Syst Clean Energy 2022;10:1184–1193. [CrossRef]
Sun  W,  Liu  M.  Wind  speed  forecasting  using
FEEMD echo state networks with RELM in Hebei,
China.  Energy  Convers  Manag  2016;114:197–208.
[CrossRef]

[45]

Sigma J Eng Nat Sci, Vol. 44, No. 1, pp. 637−662, February, 2026

659

[46]  Babu  CN,  Reddy  BE.  A  moving-average  filter
based  hybrid  ARIMA–ANN  model  for  forecasting
time series data. Appl Soft Comput 2014;23:27–38.
[CrossRef]

[47]  Bhaskar K, Singh SN. AWNN-assisted wind power
forecasting  using  feed-forward  neural  network.
IEEE Trans Sustain Energy 2012;3:306–315. [CrossRef]
[48]  Demolli  H,  Sakir  AS,  Ecemis  A,  Gokcek  M.  Wind
power  forecasting  based  on  daily  wind  speed  data
using machine learning algorithms. Energy Convers
Manag 2019;198:111823. [CrossRef]

[49]  Cicek ZIE, Ozturk ZK. Short-term traffic flow fore-
casting using artificial neural networks. Sigma J Eng
Nat Sci 2018;9:405–414.

[50]  Kose B, Duz M, Guneser MT, Recebli Z. Estimating
wind  energy  potential  with  predicting  Burr  LSM
parameters: A different approach. Sigma J Eng Nat
Sci 2018;36:389–404.

[51]  Qasem  M,  Filik  UB.  Solar  radiation  forecasting  by
using  deep  neural  networks  in  Eskisehir.  Sigma  J
Eng Nat Sci 2021;39:159–169. [CrossRef]
Samuel GS, Salimath GF, Porselvi T, Karthikeyan V.
Improved prediction of wind speed using machine
learning. J Phys Conf Ser 2021;1964:1–5. [CrossRef]

[52]

[53]  Kumar SP. Improved prediction of wind speed using
machine learning. EAI Endorsed Trans Energy Web
2019;6:1–7. [CrossRef]

[54]  Tao  D,  Hong  FX.  Wind  speed  prediction  model
based  on  radial  basis  functional  neural  network.
Adv Mater Res 2012;383:5656–5662. [CrossRef]
[55]  Zhang Y, Guifang P, Bing C, Han J, Zhao Y, Zhang
C.  Short-term  wind  speed  prediction  model  based
on  GA-ANN  improved  by  VMD.  Renew  Energy
2020;156:1373–1388. [CrossRef]
[56]  Engelbrecht  AP.  Computational
England: Wiley; 2007. [CrossRef]
Ibrahim M, Alsheikh A, Al-Hindawi Q, Al-Dahidi S,
Elmoaqet H. Short-time wind speed forecast using
artificial  learning-based  algorithms.  Comput  Intell
Neurosci 2020;2020:1–15. [CrossRef]

intelligence.

[57]

[58]  Chang  WY.  Short-term  wind  power  forecasting
using  the  enhanced  particle  swarm  optimiza-
tion-based  hybrid  method.  Energies  2013;6:4879–
4896. [CrossRef]
Jyothi MN, Rao PVR. Very-short-term wind power
forecasting  through  adaptive  wavelet  neural  net-
work. In: Proc Biennial Int Conf Power Energy Syst
(PESTSE); 2016. p.1–6. [CrossRef]

[59]

[60]  Xu  L,  Mao  J.  Short-term  wind  power  forecasting
based on Elman neural network with particle swarm
optimization. In: Chinese Control Decis Conf; 2016.
p.2678–2681. [CrossRef]

[62]  Mabel  MC,  Fernandez  E.  Analysis  of  wind  power
generation and prediction using ANN: A case study.
Renew Energy 2008;33:986–992. [CrossRef]
Singh S, Bhatti TS, Kothari DP. Wind power estima-
tion  using  artificial  neural  network.  J  Energy  Eng
2007;133:46–52. [CrossRef]

[63]

[65]

[64]  Pliego  AM,  Márquez  FPG,  Pinar  Perez  JM,  Ruiz-
Hernández  D.  A  survey  of  artificial  neural  net-
works
in  wind  energy  systems.  Appl  Energy
2022;228:1822–1836. [CrossRef]
Sharma  R,  Singh  D.  A  review  of  wind  power  and
wind speed forecasting. J Eng Res Appl 2018;8:1–9.
Sideratos  G,  Hatziargyriou  ND.  Probabilistic  wind
power  forecasting  using  radial  basis  function  neu-
ral networks. IEEE Trans Power Syst 2012;27:1788–
1796. [CrossRef]

[66]

[67]  Ramadevi B, Bingi K. Chaotic time series forecast-
ing approaches using machine learning techniques:
A review. Symmetry (Basel) 2022;14:955. [CrossRef]

[68]  Zhou Y, Sun Y, Wang S, Mahfoud RJ, Alhelou HH, et
al. Performance improvement of very short-term pre-
diction  intervals  for  regional  wind  power  based  on
composite conditional nonlinear quantile regression. J
Mod Power Syst Clean Energy 2022;10:60–70. [CrossRef]
[69]  Lee J, Wang W, Harrou F, Sun Y. Wind power predic-
tion  using  ensemble  learning-based  models.  IEEE
Access 2020;8:61517–61527. [CrossRef]

[70]  Tu CS, Hong CM, Huang HS, Chen CH. Short-term
wind  power  prediction  based  on  data  regression
and  enhanced  support  vector  machine.  Energies
2020;13:6319. [CrossRef]

[71]  Tan  L,  Han  J,  Zhang  H.  Ultra-short-term  wind
power  prediction  by  salp  swarm  algorithm-based
optimizing extreme learning machine. IEEE Access
2020;8:44470–44484. [CrossRef]

[72]  Huang Y, Liu GP, Hu WS. Priori-guided and data-
driven  hybrid  model  for  wind  power  forecasting.
ISA Trans 2023;134:380–395. [CrossRef]

[73]  Wang YL, Yang P, Zhao SY, Chevallier JL, Xiao QT. A
hybrid intelligent framework for forecasting short-
term hourly wind speed based on machine learning.
Expert Syst Appl 2022;213:119223. [CrossRef]
[74]  Pombo  DV,  Rincón  MJ,  Bacher  P,  Bindner  HW,
Spataru  SV,  Sørensen  PE.  Assessing  stacked  phys-
ics-informed  machine  learning  models  for  co-lo-
cated wind–solar power forecasting. Sustain Energy
Grids Netw 2023;32:100943. [CrossRef]

[75]  Moayyed  H,  Moradzadeh  A,  Mohammadi-Ivatloo
B, Aguiar AP, Ghorbani R. A cyber-secure general-
ized supermodel for wind power forecasting based
on  deep  federated  learning  and  image  processing.
Energy Convers Manag 2022;267:115852. [CrossRef]

[61]  Catalão JPS, Pousinho HMI, Mendes VMF. An arti-
ficial neural network approach for short-term wind
power  forecasting  in  Portugal.  In:  Int  Conf  Intell
Syst Appl Power Syst; 2009. p.1–5. [CrossRef]

[76]  Liu L, Wang JJ, Li PP, Wei L. An online transfer learn-
ing model for wind turbine power prediction based
on  spatial  feature  construction  and  system-wide
update. Appl Energy 2023;340:121049. [CrossRef]

660

Sigma J Eng Nat Sci, Vol. 44, No. 1, pp. 637−662, February, 2026

[78]

[77]  Nascimento EGS, Melo TA, Moreira DM. A trans-
former-based  deep  neural  network  with  wavelet
transform  for  forecasting  wind  speed  and  wind
energy. Energy 2023;278:127678. [CrossRef]
Sobolewski  RA,  Tchakorom  M,  Couturier  R.
Gradient  boosting-based  approach  for  short-  and
medium-term  wind  turbine  output  power  predic-
tion. Renew Energy 2023;203:142–160. [CrossRef]
[79]  Yu  L,  Meng  G,  Pau  G,  Wu  Y,  Tang  Y.  Research  on
hierarchical  control  strategy  of  ESS  in  distribution
based on GA-SVR wind power forecasting. Energies
2023;16:2079. [CrossRef]

[80]  Wang  X,  Li  J,  Shao  L,  Liu  H,  Ren  L,  Zhu  L.  Short-
term wind power prediction by an extreme learning
machine based on an improved hunter–prey optimi-
zation algorithm. Sustainability 2023;15:991. [CrossRef]
[81]  Lin Z, Liu X, Collu M. Wind power prediction based
on  high-frequency  SCADA  data  along  with  isola-
tion forest and deep learning neural networks. Int J
Electr Power Energy Syst 2020;118. [CrossRef]
[82]  Ahuja  M,  Saini  S.  Recurrent  neural  network  for
chaotic wind speed time series prediction. In: IEEE
India Int Conf Power Electron (IICPE); 2023. p.1–6.
[CrossRef]

[91]  Huang X, Jiang A. Wind power generation forecast
based  on  multi-step  informer  network.  Energies
2022;15:6642. [CrossRef]

[92]  Wu X, Jiang S, Lai CS, Zhao Z, Lai LL. Short-term
wind  power  prediction  based  on  data  decomposi-
tion  and  combined  deep  neural  network.  Energies
2022;15:6734. [CrossRef]

[93]  Yu G, Liu C, Tang B, Chen R, Lu L, et al. Short-term
wind  power  prediction  for  regional  wind  farms
based  on  spatial–temporal  characteristic  distribu-
tion. Renew Energy 2022;199:599–612. [CrossRef]
[94]  Liu X, Zhang L, Wang J, Zhou Y, Gan W. A unified
multi-step wind speed forecasting framework based
on  numerical  weather  prediction  grids  and  wind
farm monitoring data. Renew Energy 2023;211:948–
963. [CrossRef]

[95]  Hossain  MA,  Chakrabortty  RK,  Elsawah  SD,  Ryan
MJ. Very short-term forecasting of wind power gen-
eration  using  hybrid  deep  learning  model.  J  Clean
Prod 2021;296:126564. [CrossRef]

[96]  Garg  S,  Krishnamurthi  R.  A  CNN  encoder–
decoder  LSTM  model  for  sustainable  wind  power
predictive  analytics.  Sustain  Comput  Inform  Syst
2023;38:100869. [CrossRef]

[83]  Wang  J,  Li  Z.  Wind  speed  interval  prediction
based  on  multidimensional  time  series  of  convo-
lutional  neural  networks.  Eng  Appl  Artif  Intell
2023;121:105987. [CrossRef]

[97]  Zhang J, Liu D, Li Z, Han X, Liu H, Dong C, et al.
Power  prediction  of  a  wind  farm  cluster  based
on
spatiotemporal  correlations.  Appl  Energy
2021;302:117568. [CrossRef]

[84]  Mert  İ.  Agnostic  deep  neural  network  approach
to  the  estimation  of  hydrogen  production  for
solar-powered  systems.  Int  J  Hydrogen  Energy
2021;46:6272–6285. [CrossRef]

[85]  Hu  T,  Wu  W,  Guo  Q,  Sun  H,  Shi  L,  Shen  X.  Very
short-term  spatial  and  temporal  wind  power  fore-
casting:  A  deep  learning  approach.  CSEE  J  Power
Energy Syst 2020;6:434–443.

[87]

[86]  Dong X, Sun Y, Li Y, Wang X, Pu T. Spatio-temporal
convolutional  network-based  power  forecasting
of  multiple  wind  farms.  J  Mod  Power  Syst  Clean
Energy 2022;10:388–398. [CrossRef]
Jalali SMJ, Osorio GJ, Ahmadian S, Lotfi M, Campos
VMA,  et  al.  New  hybrid  deep  neural  architectural
search-based  ensemble  reinforcement
learning
strategy for wind power forecasting. IEEE Trans Ind
Appl 2022;58:15–27. [CrossRef]
Sun  Z,  Zhao  M.  Short-term  wind  power  forecast-
ing  based  on  VMD  decomposition,  ConvLSTM
IEEE  Access
error  analysis.
networks  and
2020;8:134422–134434. [CrossRef]

[88]

[89]  Miao C, Li H, Wang X, Li H. Ultra-short-term pre-
diction  of  wind  power  based  on  sample  similarity
analysis. IEEE Access 2021;9:72730–72742. [CrossRef]
[90]  Liao  W,  Yang  Z,  Chen  X,  Li  Y.  Wind  GMMN:
Scenario forecasting for wind power using genera-
tive moment matching networks. IEEE Trans Artif
Intell 2022;3:843–850. [CrossRef]

[98]  Zhang  Y,  Li  Y,  Zhang  G.  Short-term  wind  power
forecasting approach based on Seq2Seq model using
NWP data. Energy 2020;213:118371. [CrossRef]
[99]  Liao  WL,  Bak-Jensen  B,  Pillai  JR,  Yang  Z,  Liu  K.
Short-term power prediction for  renewable  energy
using hybrid graph convolutional network and long
short-term memory approach. Electr Power Syst Res
2022;211:108614. [CrossRef]

[100]  Tian  CN,  Niu  T,  Wei  W.  Developing  a  wind  power
forecasting system based on deep learning with atten-
tion mechanism. Energy 2022;257:124750. [CrossRef]

[101]  Yildiz  C,  Acikgoz  H,  Korkmaz  D,  Budak  U.  An
improved  residual-based  convolutional  neural  net-
work  for  very  short-term  wind  power  forecasting.
Energy Convers Manag 2021;228:113731. [CrossRef]

[102]  Liu Z, Li X, Zhao H. Short-term wind power fore-
casting based on feature analysis and error correc-
tion. Energies 2023;16:4249. [CrossRef]

[103]  Wang  Q,  Wang  Y,  Zhang  K,  Liu  Y,  Qiang  W,  Wen
QH. Artificial intelligent power forecasting for wind
farm  based  on  multi-source  data  fusion.  Processes
2023;11:1429. [CrossRef]

[104]  Xiao  Z,  Tang  F,  Wang  M.  Wind  power  short-term
forecasting  method  based  on  LSTM  and  multiple
error correction. Sustainability 2023;15:3798. [CrossRef]
[105]  Jung  J,  Broadwater  RP.  Current  status  and  future
advances  for  wind  speed  and  power  forecasting.
Renew Sustain Energy Rev 2014;31:762–777. [CrossRef]

Sigma J Eng Nat Sci, Vol. 44, No. 1, pp. 637−662, February, 2026

661

[106]  Huang NE, Wu Z. Ensemble empirical mode decom-
position: A noise-assisted data analysis method. 2008.
[107]  Phan QT, Phan QD, Wu YK. A hybrid wind power
forecasting  model  with  XGBoost  and  data  pre-
processing  considering  different  NWPs.  Appl  Sci
2021;11:1–19. [CrossRef]

[108]  Cadenas  E,  Rivera  W.  Wind  speed  forecasting  in
three  different  regions  of  Mexico  using  a  hybrid
ARIMA–ANN model. Renew Energy 2010;35:2732–
2738. [CrossRef]

[109]  Pousinho HMI, Mendes VMF, Catalão JPS. A hybrid
PSO–ANFIS  approach  for  short-term  wind  power
prediction  in  Portugal.  Energy  Convers  Manag
2011;52:397–402. [CrossRef]

[110]  Adedeji  PA,  Akinlabi  S,  Madushele  N,  Olatunji
OO.  Wind  turbine  power  output  very  short-term
forecast:  A  comparative  study  of  data  clustering
techniques  in  a  PSO–ANFIS  model.  J  Clean  Prod
2020;254:120135. [CrossRef]

[111]  Ye H, Yang B, Han Y, Li Q, Deng J, Tian S. Wind speed
and  power  prediction  approaches:  Classifications,
methodologies,  and  comments.  Front  Energy  Res
2022;10:1–5. [CrossRef]

[112]  Shukur OB, Lee MH. Daily wind speed forecasting
through hybrid KF–ANN model based on ARIMA.
Renew Energy 2015;76:637–647. [CrossRef]

[113]  Liu  D,  Niu  D,  Wang  H,  Fan  L.  Short-term  wind
speed forecasting using wavelet transform and sup-
port  vector  machines  optimized  by  genetic  algo-
rithm. Renew Energy 2014;62:592–597. [CrossRef]
[114]  Zhang  C,  Wei  H,  Zhao  J,  Liu  T,  Zhu  T,  Zhang  K.
Short-term wind speed forecasting using empirical
mode  decomposition  and  feature  selection.  Renew
Energy 2016;96:727–737. [CrossRef]

[115]  Mi  XW,  Liu  H,  Li  YF.  Wind  speed  forecasting
method  using  wavelet,  extreme  learning  machine
and  outlier  correction  algorithm.  Energy  Convers
Manag 2017;151:709–722. [CrossRef]

[116]  Li H, Wang J, Lu H, Guo Z. Research and application
of a combined model based on variable weight for
short-term  wind  speed  forecasting.  Renew  Energy
2018;116:669–684. [CrossRef]

[117]  Jiang P, Wang Y, Wang J. Short-term wind speed fore-
casting using a hybrid model. Energy 2017;119:561–
577. [CrossRef]

[118]  Azimi  R,  Ghofrani  M,  Ghayekhloo  M.  A  hybrid
wind power forecasting model based on data min-
ing  and  wavelets  analysis.  Energy  Convers  Manag
2016;127:208–225. [CrossRef]

[119]  Jiang  Y,  Huang  G,  Peng  X,  Li  Y,  Yang  Q.  A  novel
wind  speed  prediction  method:  Hybrid  of  correla-
tion-aided DWT, LSSVM and GARCH. J Wind Eng
Ind Aerodyn 2018;174:28–38. [CrossRef]

[120]  Liu H, Duan Z, Han FZ, Li YF. Big multi-step wind
speed forecasting model based on secondary decom-
position,  ensemble  method  and  error  correction

algorithm.  Energy  Convers  Manag  2018;156:525–
541. [CrossRef]

[121]  Hong  YY,  Rioflorido  CPP.  A  hybrid  deep  learn-
ing-based neural network for 24-h ahead wind power
forecasting. Appl Energy 2019;250:530–539. [CrossRef]

[122]  Foley  M,  Leahy  PG,  Marvuglia  A,  McKeogh  EJ.
Current  methods  and  advances  in  forecasting  of
wind power generation. Renew Energy 2012;37:1–8.
[CrossRef]

[123]  Shetty RP, Sathyabhama APSP, Rai AA. Optimized
radial basis function neural network model for wind
power prediction. In: Proc Int Conf Cogn Comput
Inf Process (CCIP); 2016. p.1–6. [CrossRef]

[124]  Peng H, Liu F, Yang X. A hybrid strategy of short-
term  wind  power  prediction.  Renew  Energy
2013;50:590–595. [CrossRef]

[125]  Wang J, Yang W, Tong N. A novel hybrid forecast-
ing  system  of  wind  speed  based  on  a  multi-objec-
tive  sine  cosine  algorithm.  Energy  Convers  Manag
2018;163:134–150. [CrossRef]

[126]  Saini  S,  Ahuja  M.  Wind  speed  prediction  using
wavelet transform and artificial neural network. Int
J Res Electron Commun Eng 2017;5:161–168.
[127]  Saini  S,  Ahuja  M.  Wind  speed  prediction  using
wavelet  transform  and  GA-trained  artificial  neural
network. J Adv Res Dyn Control Syst 2019:198–204.
[CrossRef]

[128]  Duan J, Chang M, Chen X, Wang W, Zuo H, Bai Y,
et al. A combined short-term wind speed forecast-
ing model based on CNN–RNN and linear regres-
sion optimization considering error. Renew Energy
2022;200:788–808. [CrossRef]

[129]  Zou Y, Feng W, Zhang J, Li J. Forecasting of short-
load  using  the  MFF-SAM-GCN  model.

term
Energies 2022;15:3140. [CrossRef]

[130]  Aisyah  S,  Simaremare  AA,  Adytia  D,  Aditya  IA,
Alamsyah A. Exploratory weather data analysis for
electricity load forecasting using SVM and GRNN.
Energies 2022;15:3566. [CrossRef]

[131]  Zhao Z, Yun S, Jia L, Guo J, Meng Y, He N. Hybrid
VMD–CNN–GRU-based model for short-term fore-
casting of wind power considering spatio-temporal
features.  Eng  Appl  Artif  Intell  2023;121:105982.
[CrossRef]

[132]  Che JX, Yuan F, Deng D, Jiang ZY. Ultra-short-term
probabilistic  wind  power  forecasting  with  spatial–
temporal  multi-scale  features  and  K-FSDW-based
weight. Appl Energy 2023;331:120479. [CrossRef]
[133]  Hu S, Xiang Y, Zhang HC, Xie SY. Hybrid forecasting
method for wind power integrating spatial correla-
tion  and  corrected  numerical  weather  prediction.
Appl Energy 2021;293:116951. [CrossRef]

[134]  Wen SK, Li YT, Su Y. A new hybrid model for power
forecasting  of  a  wind  farm  using  spatial–tempo-
ral  correlations.  Renew  Energy  2022;198:155–168.
[CrossRef]

662

Sigma J Eng Nat Sci, Vol. 44, No. 1, pp. 637−662, February, 2026

[135]  Hu S, Xiang Y, Huo D, Jawad SQ. An improved deep
belief network-based hybrid forecasting method for
wind power. Energy 2021;224:120185. [CrossRef]
[136]  Gu B, Hu H, Zhao J, Zhang HT, Liu X. Short-term
wind  power  forecasting  and  uncertainty  analysis
based  on  FCM–WOA–ELM–GMM.  Energy  Rep
2023;9:807–819. [CrossRef]

[137]  Al-Duais FS, Al-Sharpi RS. A Markov chain Monte
Carlo method for forecasting wind power using time
series models. Alex Eng J 2023;74:51–63. [CrossRef]

[138]  Yan  J,  Möhrlen  CN,  Göçmen  TF,  Kelly  M,  Wessel
A,  Giebel  G.  Uncovering  wind  power  forecasting
uncertainty sources and their propagation through
the  modeling  chain.  Renew  Sustain  Energy  Rev
2022;165:112519. [CrossRef]

[139]  Xiong B, Lou L, Meng XY, Wang X, Ma H, Wang Z.
Short-term wind power forecasting based on atten-
tion  mechanism  and  deep  learning.  Electr  Power
Syst Res 2022;206:107776. [CrossRef]

[140]  Zhang J, Zhang R, Zhao Y, Qiu J, Bu S, Zhu Y, et al.
Deterministic  and  probabilistic  prediction  of  wind
power based on a hybrid intelligent model. Energies
2023;16:4237. [CrossRef]

[141]  Wu  B,  Yu  S,  Peng  L,  Wang  L.  Interpretable  wind
speed
feature
forecasting  with  meteorological
exploration  and  two-stage  decomposition.  Energy
2024;294:1–28. [CrossRef]

and  artificial  neural  networks.  Rev  Intell  Artif
2019;33:447–452. [CrossRef]

[149]  Negnevitsky M, Johnson PL, Santoso S. Short-term
wind power forecasting using hybrid intelligent sys-
tems. In: Proc IEEE Power Eng Soc Gen Meet; 2007.
p.1–4. [CrossRef]

[150]  Liu  H,  Tian  HQ,  Chen  C,  Li  YF.  A  hybrid  statisti-
cal method to predict wind speed and wind power.
Renew Energy 2010;35:1857–1861. [CrossRef]
[151]  Kassa Y, Zhang JH, Zheng DH, Wei D. Short-term
wind power prediction using ANFIS. In: Proc IEEE
Int  Conf  Power  Renew  Energy  (ICPRE);  2016.
p.388–393. [CrossRef]

[152]  Pinson P, Kariniotakis GN. Wind power forecasting
using fuzzy neural networks enhanced with online
prediction  risk  assessment.  In:  Proc  IEEE  Bologna
Power Tech; 2003. p. 2. [CrossRef]

[153]  Potter  CW,  Negnevitsky  M.  Very  short-term  wind
forecasting  for  Tasmanian  power  generation.  IEEE
Trans Power Syst 2006;21:965–972. [CrossRef]
[154]  Liu H, Tian HQ, Pan DF, Li YF. Forecasting models
for wind speed using wavelet, wavelet packet, time
series  and  artificial  neural  networks.  Appl  Energy
2013;107:191–208. [CrossRef]

[155]  Moorthy CB, Agrawal A, Deshmukh MK. Artificial
intelligence  techniques  for  wind  power  prediction:
A case study. Indian J Sci Technol 2015;8. [CrossRef]

[142]  Zhang Y, Zhao Y, Shen X, Zhang J. A comprehensive
wind speed prediction system based on Monte Carlo
and  artificial  intelligence  algorithms.  Appl  Energy
2022;305:117815. [CrossRef]

[156]  Nie  Y,  Bo  H,  Zhang  W,  Zhang  H.  Research  on
hybrid wind speed prediction system based on arti-
ficial  intelligence  and  double  prediction  scheme.
Complexity 2020;2020:1–22. [CrossRef]

[143]  Du P, Wang J, Yang W, Niu T. Multi-step ahead fore-
casting  in  electrical  power  systems  using  a  hybrid
forecasting  system.  Renew  Energy  2018;122:533–
550. [CrossRef]

[144]  Zhao  P,  Wang  J,  Xia  J,  Dai  Y,  Sheng  Y,  Yue  J.
Performance evaluation and accuracy enhancement
of  a  day-ahead  wind  power  forecasting  system  in
China. Renew Energy 2012;43:234–241. [CrossRef]

[145]  Shi  J,  Guo  J,  Zheng  S.  Evaluation  of  hybrid  fore-
casting  approaches  for  wind  speed  and  power
generation  time  series.  Renew  Sustain  Energy  Rev
2012;16:3471–3480. [CrossRef]

[146]  Guo  ZH,  Wu  J,  Lu  HY,  Wang  JZ.  A  case  study  on
a  hybrid  wind  speed  forecasting  method  using  BP
neural  network.  Knowl  Based  Syst  2011;24:1048–
1056. [CrossRef]

[147]  Catalão  JPS,  Pousinho  HMI,  Mendes  VMF.  Short-
term wind power forecasting in Portugal by neural
networks  and  wavelet  transform.  Renew  Energy
2011;36:1245–1251. [CrossRef]

[148]  Berrezzek  F,  Khelil  K,  Bouadjila  T.  Efficient  wind
speed  forecasting  using  discrete  wavelet  transform

[157]  Ferreira M, Santos A, Lucio P. Short-term forecast of
wind  speed  through  mathematical  models.  Energy
Rep 2019;5:1172–1184. [CrossRef]

[158]  Ma L, Li B, Yang ZB, Du J, Wang J. A new combina-
tion prediction model for short-term wind farm out-
put power based on meteorological data collected by
WSN. Int J Control Autom 2014;7:171–180. [CrossRef]
[159]  Mao M, Cao Y, Chang L. Improved fast short-term
wind  power  prediction  model  based  on  superpo-
sition  of  predicted  error.  In:  Proc  IEEE  Int  Symp
Power  Electron  Distrib  Gener  Syst  (PEDG);  2013.
p.1–6. [CrossRef]

[160]  Chang  WY.  Comparison  of  three  short-term
wind  power  forecasting  methods.  Adv  Mater  Res
2013;684:671–675. [CrossRef]

[161]  Chang WY. An RBF neural network combined with
OLS algorithm and genetic algorithm for short-term
wind power forecasting. J Appl Math 2013;2013:1–9.
[CrossRef]

[162]  Sideratos  G,  Hatziargyriou  ND.  An  advanced  sta-
tistical  method  for  wind  power  forecasting.  IEEE
Trans Power Syst 2007;22:258–265. [CrossRef]

