Haq et al. Discover Applied Sciences          (2025) 7:1139
https://doi.org/10.1007/s42452-025-07675-x

Discover Applied Sciences

Machine learning approaches for wind power
forecasting: a comprehensive review
Inam Ul Haq1, Abhishek Kumar1 and Pramod Singh Rathore2*

*Correspondence:
Pramod Singh Rathore

pramod.rathore@jaipur.manipal.
edu
1Department of Computer Science
and Engineering, Chandigarh
University, Mohali, Punjab, India
2Department of Computer and
Communication Engineering,
Manipal University Jaipur, Jaipur,
India

Abstract
The dependable integration of wind energy into contemporary electrical systems,
which supports market operations, grid stability, and strategic planning, depends
on accurate wind power forecasting. A thorough analysis of machine learning (ML)
techniques for wind power prediction is presented in this research, encompassing
advancements from 2006 to 2025. Physical, statistical, traditional machine learning,
deep learning, ensemble, and hybrid models are the categories into which current
forecasting techniques fall. With particular focus on sophisticated designs like Long
Short-Term Memory (LSTM) networks, Convolutional Neural Networks (CNNs), Graph
Neural Networks (GNNs), and hybrid CNN–LSTM frameworks, we examine their
capabilities, constraints, and application domains. The paper also looks at lightweight
solutions that allow deployment on low-cost edge devices, as well as optimization
algorithms like the Fruit Fly Algorithm and Particle Swarm Optimization (PSO).
Comparative analyses show how well various models handle temporal dependencies,
nonlinearity, scalability, and interpretability over a range of predicting horizons. There
is a thorough discussion of the main obstacles, including problems with data quality,
computing limitations, and performance in harsh weather. The findings indicate that
in order to improve prediction accuracy, robustness, and real-time application, future
research should concentrate on IoT-enabled sensor networks, multi-model fusion,
physics-informed learning, and sophisticated structures like Transformers. All things
considered, this paper charts the developing field of machine learning-driven wind
power forecasting and offers practical guidance for developing intelligent, efficient,
and sustainable renewable energy systems.

Keywords  CNN, LSTM, Machine learning, Deep learning, Hybrid models, Optimization
methods, Edge computing, Wind power forecasts

1  Introduction

Wind power facilities produce better environmental outcomes than fossil fuel-powered
systems, and they are crucial parts of sustainable clean energy generation. Installations
of  wind  power  both  benefit  the  environment  and  lower  greenhouse  gas  emissions  [1].
Strict energy policy regulations and the development of modern wind power technology
are two ways that several national forces are combating climate change and promoting
the rapid growth of the wind industry. Over the past 20 years, wind power plants have

© The Author(s) 2025. Open Access  This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International
License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate
credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material.
You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party
material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material
is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit  h t t p : /  / c r e a  t i v e c o  m m o n  s . o r g  / l i c e  n s
e s / b  y - n c  - n d / 4 . 0 /.

REVIEWOpen Access
Page 2 of 32

rapidly  expanded  globally,  advancing  various  energy  choices  and  reducing  CO2  levels
[2]. Wind energy’s intrinsic instability and sporadic nature provide major scheduling and
grid control issues, necessitating the use of highly developed, precise wind power fore-
casting services [3]. For safe and reliable operation, power systems require precise wind
power predictions. Wind power’s energetic uncertainty raises the pressure on grid man-
agement systems for load distribution and scheduling [4]. Three main issues are caused
by  poor  forecast  data:  unstable  frequency  regulation,  a  greater  demand  for  expensive
and polluting backup power systems, and catastrophic damage to power networks [5].
Various wind power forecast times correspond with operational requirements, such as
power  market  trading,  operational  scheduling,  and  real-time  control  implementation.
The  availability  of  complete  datasets  and  significant  prediction  accuracy  is  hampered
by  the  numerous  uncontrollable  affecting  factors,  such  as  changing  wind  speeds  and
weather  patterns  [6].  Better  processing  power  and  more  accessible  datasets  led  to  the
widespread adoption of modern prediction techniques based on cutting-edge machine
learning  technologies  [7].  Since  machine  learning  can  identify  complex  nonlinear  pat-
terns in addition to erratic wind power data, it performs better than statistical and physi-
cal models. By identifying lengthy pattern combinations and minute variations in wind
speed and power data, the Long Short-Term Memory (LSTM) networks leverage deep
learning  technology  to  generate  the  most  accurate  time-series  forecasts  [8].  Because
they  provide  excellent  generalization  qualities  and  consistently  high  predictive  preci-
sion, the ensemble learning techniques Random Forest and XGBoost (Extreme Gradient
Boosting)  are  often  used  as  wind  power  prediction  solutions.  To  improve  wind  power
forecasting  solutions  that  increase  power  grid  dependability  and  reduce  costs,  scien-
tists use many machine learning models in a single system [9]. In-depth discussion and
evaluation of artificial intelligence algorithms for wind power forecasting are provided in
this document. Through application evaluation, limitation analysis, and possible future
research  prospects,  this  work  conducts  a  thorough  examination  of  machine  learning
models.

1.1  Explicit distinction and role of machine learning (ML) vs. deep learning (DL) in wind

power forecasting

1.1.1  Theoretical foundations

Machine Learning (ML) is often defined in a broad sense as a pattern learning approach
to  make  predictions  or  decisions,  without  being  explicitly  programmed.  The  linear
regression, decision trees, random forests, support vector machines (SVMs), and artifi-
cial neural networks (ANNs) belong to the ML techniques. These tend to be engineered
algorithms and are useful in finding patterns when you have moderate-sized structured
data. Specialized subsets of ML Deep Learning. Deep Learning (DL), its own subset that
applies the use of multi-layered neural network architectures that have faculties, includ-
ing Convolutional Neural Networks (CNNs), Recurrent Neural Networks (RNNs), Long
Short-Term Memory Networks (LSTMs), and Gated Recurrent Units (GRUs). DL mod-
els are able to automatically learn the hierarchical features of raw and high-dimensional
data. They have a unique structure that allows powerful representation learning, espe-
cially when dealing with large and complicated datasets, as is the case with wind power
forecasting.

Haq et al. Discover Applied Sciences          (2025) 7:1139 Page 3 of 32

Although classical ML algorithms are categorized under the greater umbrella of deep
learning, the ability of DL to automatically implement feature extraction and correlate
nonlinear complex relationships between them is what makes DL distinct relative to the
traditional ML algorithms.

1.1.2  Practical implications in wind power forecasting

The choice between ML and DL approaches in wind power forecasting is shaped by sev-
eral key factors:

  • Data Dependency

ML algorithms (e.g., Decision Trees, Random Forests, SVMs) are well-suited to smaller
or  moderately  sized  datasets,  often  requiring  manual  feature  extraction  and  selection.
Architectures (e.g., LSTM, CNN) thrive on large-scale, high-resolution datasets such as
those from SCADA systems. Their performance and generalization improve significantly
with increased data volume and diversity.

  • Computational Demands:

ML methods generally require less computational power and can be deployed on stan-
dard  computing  platforms,  making  them  feasible  for  applications  in  resource-limited
settings  or  for  real-time  edge  deployment.  DL  models,  due  to  their  deeper  and  more
complex  architectures,  are  computationally  intensive—requiring  specialized  hardware
such  as  GPUs  for  training  and  inference.  This  is  particularly  evident  with  models  like
CNNs, LSTMs, and hybrid CNN-LSTM networks.

  • Model Interpretability:

Classical ML models, especially tree-based methods (e.g., Decision Tree, Random For-
est), and linear models (Linear Regression), offer high interpretability. This transparency
aids operational decision-making and fosters trust among stakeholders.

DL  models  tend  to  operate  as  ‘black  boxes’  with  limited  interpretability.  Although
efforts  such  as  attention  mechanisms  and  visualization  techniques  exist  to  improve
explainability, model complexity remains a challenge.

1.1.3  Real-world deployment and operational considerations

Deployment  of  DL  models  in  operational  wind  farms,  especially  on  low-cost  devices
(e.g.,  Raspberry  Pi),  faces  notable  challenges:  limited  memory,  processing  power,  and
energy  efficiency  favor  lightweight  ML  algorithms  over  heavy  DL  architectures  unless
model pruning, quantization, or TinyML techniques are applied.

The  distribution  of  publications  among  several  scholarly  journals  reveals  patterns
about  research  and  its  impact.  Energy  is  the  most  cited  magazine;  however,  according
to Fig. 1, IEEE Transactions on Power Systems receives 1,584 citations, with an average
of 153.41 citations per article. Due to the fact that it frequently appears in these publica-
tions, the academic community holds content with research themes and content within
their thematic areas in high regard. Wind power forecasting research is receiving more
and more attention since studies are frequently mentioned in scholarly works covering a
wide range of subjects, not just energy policy.

Haq et al. Discover Applied Sciences          (2025) 7:1139 Page 4 of 32

Fig. 1  Top journals for research in wind power forecasting (2008–2025)

Fig. 2  According to indexed journal papers, the top three publishing nations for wind power forecasting research
from 2006 to 2025

Figure  2  presents  the  annual  number  of  publications  and  total  citations  in  the  field
from  2006  to  2025.  The  x-axis  represents  publication  years,  while  the  two  plotted
series  correspond  to  the  yearly  count  of  relevant  journal  articles  and  their  cumulative
citations  to  date.  The  chart  shows  a  modest  research  output  before  2010,  followed  by
steady growth and a sharp acceleration after 2015, coinciding with the rapid adoption of
advanced machine learning and deep learning methods.

Figure 3 depicts the temporal evolution of research activity in wind power forecasting
between 2006 and 2025, measured in terms of annual publication counts .The data show
a modest output in the early years, with fewer than 15 publications annually before 2010,
followed by steady growth through the mid-2010s. A sharper increase occurs after 2015,

Haq et al. Discover Applied Sciences          (2025) 7:1139

Page 5 of 32

Fig. 3  Wind power forecasting’s annual publications and total citations (2006–2025) chart

Fig. 4  demonstrates the trends in the application of research methods (ML, LSTM, PSO, Fruit Fly Algorithm, Light-
weight models, etc.) in wind power prediction throughout the studies you evaluated

aligning with the rapid uptake of machine learning and deep learning approaches such
as LSTM, CNN, and hybrid models in the field. Cumulative citations grow more steeply
in the latter half of the period, indicating both a growing body of work and rising aca-
demic impact. The peak in publication numbers appears in 2024–2025, suggesting that
wind power forecasting remains an active and expanding research domain.

Figure  4  shows  the  Utilization  patterns  of  research  techniques  in  the  reviewed  wind
power  forecasting  studies.  The  chart  shows  the  number  of  studies  employing  various
methods,  including  generic  machine  learning  approaches  (8  studies),  LSTM  networks
(3 studies), Particle Swarm Optimization (3), the Fruit Fly Algorithm (3), and lightweight
ML  models  for  low-resource  environments  (3).  The  distribution  illustrates  the  domi-
nance of generic ML frameworks in the literature, alongside recurring interest in specific
deep learning and optimization algorithms.

Haq et al. Discover Applied Sciences          (2025) 7:1139

Page 6 of 32

2  Methods of wind power prediction using machine learning

Wind speed forecasting and direct power output prediction are the two basic approach
types  used  in  wind  power  forecasting.  In  the  speed-based  forecasting  method,  power
output  is  calculated  using  Formula  (1)  for  short-term  wind  speed  prediction  utilizing
wind power curves. The method increases forecast efficiency by utilizing the power out-
put connection and wind speed. Instead of employing wind speed estimates to improve
performance, direct power output predictions use previous power generating records to
learn input-output patterns.

P = 0.5rAv3Cp

(1)

The  wind  power  prediction  equation  uses  P  to  represent  watts  (W)  served  by  the  tur-
bine,  but  also  requires  ρ  for  air  density  (kg/m³),  A  for  turbine  rotor  sweep  (m²)  and  v
for wind velocity (m/s) and Cp to signify performance rate between zero and one. The
theoretical  maximum  performance  reaches  0.59  Betz  limit,  but  practical  applications
yield lower numbers because of mechanical and aerodynamic losses. Direct prediction
of  wind  power  typically  follows  traditional  steps  when  conducting  the  process.  Data
preprocessing  is  the  first  stage  where  duplicate  entries  are  eliminated,  along  with  the
handling of missing values. The procedure conducts attribute selection while perform-
ing  exploratory  data  analysis  to  recognize  the  most  important  features  that  will  serve
the  prediction  models.  The  third  stage  starts  with  the  development  of  machine  learn-
ing (ML) models before their performance evaluation process. The classification of wind
power  forecasting  models  consists  of  traditional  physical  models  as  well  as  statistical
models, according to Table 1.

Through  numerical  weather  prediction  techniques,  physical  models  use  computa-
tional  fluid  dynamics  to  simulate  the  impacts  of  meteorological  factors,  such  as  wind
speed, air temperature, and air pressure, on wind power output [10]. The models require
delicate  initial  conditions  and  have  significant  computational  demands,  making  them
difficult to compute. To find relationships between climatic factors and wind power gen-
eration  numbers,  statistical  models  use  historical  data  in  conjunction  with  techniques
like regression and ARIMA. Because machine learning models generate more accurate
representations  of  wind  data  complexity,  they  perform  better  than  statistical  models
that rely on computing processes [11]. ARMA models and SVMs are two popular tech-
niques  used  in  statistical  models  to  analyze  historical  data  and  generate  mathematical
predictions  between  wind  speed  and  power  output.  The  models  maintain  lower  pro-
cessing requirements since they do not require extensive physical knowledge [12]. Since

Table 1  Benefits of machine learning techniques
Advantage area
Nonlinear
modelling
High-dimensional
data
Robustness

How ML/DL methods excel in wind power forecasting
Learns intricate patterns and relationships without relying on
domain-specific physical laws
Processes and extracts key features from large time-series
and sensor grids
Reduces error and bias by combining multiple predictors
(ensemble and hybrid frameworks)
Merges data-driven insights with physical models for en-
hanced realism and adherence

Adapts model weights and parameters online as new wind
data becomes available

Integration
capability

Real-time
adaptation

Typical example
LSTM models capturing
wind speed–power curves
CNN architectures analyz-
ing SCADA datasets
Random Forest and XG-
Boost for outlier resistance
Physics-informed neural
networks (PINNs), a hybrid
CNN-LSTM
Incremental learning with
edge-deployed TinyML

Haq et al. Discover Applied Sciences          (2025) 7:1139 Page 7 of 32

statistical  models  are  unable  to  accurately  detect  the  intricate  patterns  and  dynamic
changes that take place in the data displayed in Table 2, wind power data offers several
nonlinear characteristics for processing.

2.1  Limitations of physical and statistical models in current wind power forecasting

Physical  models,  such  as  those  based  on  computational  fluid  dynamics  (CFD)  and
numerical  weather  prediction  (NWP),  simulate  wind  flow  aerodynamics  and  turbine
interactions  by  incorporating  complex  atmospheric  processes.  However,  their  opera-
tional use faces key challenges: high computational costs make real-time or ultra-short-
term forecasting impractical; sensitivity to initial and boundary conditions often leads to
large forecast errors, especially over longer horizons; and NWP grid resolutions strug-
gle  to  capture  microscale  variability,  including  site-specific  turbulence,  wake  effects,
and  local  microclimates  that  impact  turbine  performance.  Statistical  models  such  as
ARMA,  ARIMA,  and  regression  techniques—rely  on  historical  correlations  between
meteorological  inputs  and  power  output,  but  have  intrinsic  limitations.  They  typically
assume linearity and stationarity, assumptions frequently violated due to seasonal shifts,
climate  change,  and  turbine  operational  changes.  Moreover,  their  limited  capacity  to
model  nonlinear  dependencies  hampers  the  accurate  representation  of  complex  wind-
power  relationships  without  extensive  manual  feature  engineering.  These  models  also
tend to degrade rapidly under abrupt weather changes, such as extreme events or frontal
passages.

Together, these constraints reduce the accuracy, robustness, and adaptability of physi-
cal  and  statistical  models,  particularly  in  complex  terrains,  offshore  environments,  or
highly  variable  meteorological  conditions.  In  contrast,  modern  machine  learning  and
deep learning approaches offer significant advantages: they automatically learn complex,
nonlinear relationships from large and heterogeneous datasets, integrate diverse spatial
and temporal data sources, and adapt dynamically to shifting data distributions. These
strengths underpin their growing adoption as core or hybrid components in next-gener-
ation operational wind power forecasting systems.

2.2  Benefits of machine learning

When  it  comes  to  wind  power  prediction,  conventional  computer  learning  and  deep
learning  techniques  are  far  superior  to  statistical  and  physical  models.  The  need  for

Table 2  Types of models for predicting wind power
Category
Physical models

Representative models
Computational Fluid Dynamics (CFD), Numerical Weather Predic-
tion (NWP), Power Curve Modelling
ARIMA, SARIMA, Exponential Smoothing, Polynomial Regression

Decision Tree (DT), Support Vector Machine (SVM), K-Nearest
Neighbors (KNN), Gaussian Process (GP)
Random Forest (RF), Extreme Gradient Boosting (XGBoost),
Gradient Boosting (GB), Bagging
Convolutional Neural Network (CNN), Long Short-Term Memory
(LSTM), Gated Recurrent Unit (GRU), BiLSTM
CNN-LSTM, Physics-Informed Neural Network (PINN), Optimized
LSTM via PSO or Fruit Fly Algorithm
Graph Neural Networks (GNN), Spatio-Temporal Graph Networks Turbine interaction,

Key applications
Site design, climate
impact studies
Short-term prediction,
baseline methods
Day-ahead forecasting,
dataset exploration
Robustness to outliers,
improved accuracy
Temporal/spatial
learning, multi-scale
Handling nonlinearity,
feature fusion

spatial prediction

Statistical models

Conventional ML
Models
Ensemble learning
models
Deep learning
models
Hybrid & meta-
heuristic models
Graph-based
models

Haq et al. Discover Applied Sciences          (2025) 7:1139 Page 8 of 32

sophisticated physics-based modeling is eliminated by machine learning models, which
can  automatically  and  independently  understand  the  complex,  nonlinear  connection
between  wind speed and power  based on enormous historical data [13]. Furthermore,
deep learning architectures like Long Short-Term Memory (LSTMs) and Convolutional
Neural Networks (CNNs) are highly effective at processing time series and high-dimen-
sional data, and they have excellent feature extraction capabilities [14]. By using ensem-
ble learning, these techniques not only improve prediction accuracy but also strengthen
the model’s resilience and lessen biases [15].

2.3  Introduction to common machine learning models

This part describes several widely used machine learning models for wind power fore-
casting. To address the challenges of comprehensiveness and parallel structure, the mod-
els are categorized at a higher level of types based on their methodologies and use cases.

2.3.1  Traditional machine learning models

Traditional machine learning methods rely on manually or statistically extracted features
and are known for their computational efficiency and effectiveness with moderate-sized
datasets. Common algorithms in this category include Linear Regression (LR), K-Near-
est Neighbors (KNN), Decision Tree Regression (DTR), and Support Vector Machines
(SVM). These models are widely used for wind power forecasting due to their simplicity,
interpretability, and relatively low data requirements [16].

2.3.2  Deep learning models

Deep  learning  models  automatically  learn  hierarchical  feature  representations  from
high-dimensional sequential or spatial-temporal data, making them particularly effective
for large and complex datasets. However, they are generally more computationally inten-
sive than traditional ML methods. Common architectures used in wind power forecast-
ing include Artificial Neural Networks (ANN), Convolutional Neural Networks (CNN),
Recurrent Neural Networks (RNN), Long Short-Term Memory networks (LSTM), and
Gated Recurrent Units (GRU). These models excel at capturing nonlinear patterns and
temporal dependencies inherent in wind and power data [17].

2.3.3   Ensemble learning models

Ensemble  learning  methods  enhance  model  robustness  and  accuracy  by  combining
multiple base learners. Popular techniques in wind power forecasting include Random
Forest (RF), Gradient Boosting Machines (GBM), XGBoost, and various bagging meth-
ods. These models effectively balance predictive performance and generalization, handle
nonlinear  relationships  well,  and  exhibit  robustness  to  noisy  data.  However,  they  typi-
cally require more extensive hyperparameter tuning and can be less interpretable com-
pared to simpler models [18].

2.3.4  Hybrid models

Hybrid  models  integrate  complementary  approaches  to  leverage  their  respective
strengths  and  mitigate  individual  limitations.  Examples  include  hybrid  deep  learning
architectures  such  as  CNN-LSTM,  which  combine  convolutional  and  recurrent  layers
to  capture  both  spatial  and  temporal  features,  as  well  as  statistical–machine  learning

Haq et al. Discover Applied Sciences          (2025) 7:1139 Page 9 of 32

combinations  like  ARIMA  coupled  with  ML  models  applied  to  residuals  [19].  These
hybrids often achieve superior accuracy in complex forecasting scenarios by effectively
modelling both physical/statistical patterns and nonlinear dependencies. However, they
tend  to  be  more  complex,  resource-intensive,  and  less  interpretable  than  standalone
models [20, 21].

Practically, choosing an appropriate algorithm rests on factors such as characteristics
of  data,  computer  resources  available,  prediction  lead-time,  and  the  requirement  for
explainability of a model. Table 3 shows the Comparison of different machine learning
algorithms  utilized  for  wind  power  forecasting,  specifying  their  common  application
domains, pros, and cons.

The  suitability  of  each  approach  varies  depending  on  the  dataset  and  application
requirements.  For  instance,  Random  Forests  require  a  lot  of  processing  resources  yet
perform well with huge datasets. Similarly, although Long Short-Term Memory (LSTM)
networks are good at capturing temporal dependencies, they can be difficult to design
and understand.

While  XGBoost  is  widely  recognized  for  its  strong  predictive  accuracy  in  structured
data problems, recent studies also highlight its robustness when applied to challenging
wind  forecasting  scenarios.  For  example  [22],  evaluated  XGBoost  on  high-frequency
(1–5 min) SCADA datasets and found only a 3–5% RMSE degradation when the sam-
pling rate was quadrupled, compared to 8–12% for LSTM and SVM models. Similarly

Typical Limitations

Primary Application

Baseline modelling of lin-
ear power–wind relations
Pattern matching with
historical conditions

Easy to implement; highly
interpretable
Simple; works with small datasets Poor scaling to large data;

Table 3  A comparative study of machine learning techniques for predicting wind turbine power
Key Advantages
Algorithm/
Model Type
Linear Regres-
sion (LR)
K-Nearest
Neighbors
(KNN)
Decision Tree
(DTR)
Random Forest
(RF)
Support Vector
Machines (SVM)

Capturing simple nonlin-
ear relationships
Ensemble prediction
using many decision trees
Forecasting in high-di-
mensional feature space

Fails with nonlinear patterns;
low flexibility

Interpretable; handles mixed
numerical/categorical data
Robust to noise; handles large,
high-dimensional data
Effective on complex boundar-
ies; resistant to overfitting with
kernels
Flexible input handling; adapt-
able to various data types

ANN (Shallow)

Modelling moderate
nonlinearities

LSTM

GRU

Gradient
Boosting (e.g.,
XGBoost)
Graph Neural
Networks (GNN)

Sequential time-series
prediction

Sequential prediction with
lower complexity than
LSTM
High-accuracy forecasting
from structured datasets

Modelling spatial relation-
ships in wind farms

Hybrid / En-
semble Models

Combining models for ac-
curacy and robustness

Captures long-term dependen-
cies; ideal for high-frequency
wind data
Faster training; fewer parameters;
competitive accuracy

Handles missing data; strong
generalisation

Learns turbine-to-turbine
dependencies; integrates tempo-
ral + spatial learning
Mitigates weaknesses of single
models; improves uncertainty
handling

sensitive to irrelevant
features
Prone to overfitting; unstable
with small changes in data
Reduced interpretability;
high memory requirements
Requires parameter tun-
ing; can be slow on large
datasets
Needs careful regularisation;
less effective than deep
structures for temporal data
Computationally heavy;
needs large datasets

May underperform on highly
complex long-sequence
tasks
Higher training cost; less
transparent modelling
decisions
Complex setup; requires
large, labelled spatial
datasets
Higher complexity; needs
more computational
resources

Haq et al. Discover Applied Sciences          (2025) 7:1139 Table 4  An overview of machine learning techniques for predicting wind turbine power
Captures Temporal
Algorithm/Model
Dependencies

Scalable to
Large Datasets

Nonlinear
Relationship
Handling

Linear Regression (LR)
K-Nearest Neighbors (KNN)
Decision Tree Regression (DTR)
Random Forest (RF)
Support Vector Machine (SVM)
Artificial Neural Network (ANN)
LSTM
Gradient Boosting (XGBoost)
Graph Neural Network (GNN)
Hybrid / Ensemble Models

✗

✓
✓
✓
✓
✓
✓
✓
✓
✓

✓
✗

✓
✓
✗

✓
✓
✓
✓
✓

✗
✗
✗
✗
✗
✗

✓
✗

✓
✓/✗ (depends on
components)

Page 10 of 32

High
Inter-
pret-
ability

✓
✓
✓
✗
✗
✗
✗
✗
✗
✗

Table 5  Evaluation of the performance of the LSTM and GRU models in wind power prediction
Performance Metric
10,200 samples
14,800 samples
12,700 samples
20,300 samples
8,050 samples
18,200 samples
25,400 samples
10,600 samples

Sampling Interval
LSTM
GRU
LSTM
BiLSTM
GRU
LSTM
GRU
LSTM–GRU Hybrid

Model
MAE = 3.10 MW
RMSE = 4.82 MW
MAPE = 5.65%
R² = 0.912
MAE = 2.95 MW
RMSE = 3.65 MW
MAPE = 6.40%
R² = 0.931

Dataset Size
30 min
1 h
10 min
15 min
5 min
30 min
20 min
15 min

References
 [22]
 [23]
 [24]
 [25]
 [26]
 [27]
 [28]
 [29]

[23], simulated missing data rates of up to 15% in onshore wind farm SCADA records;
XGBoost  with  simple  median  imputation-maintained  MAE  within  6%  of  its  base-
line, while neural networks saw error increases of over 12%. These results suggest that
XGBoost’s  ability  to  handle  feature  sparsity  and  irregular  input  intervals—through
built-in handling of missing values and flexible tree-splitting—makes it particularly suit-
able for operational conditions where data quality and frequency may vary.

We further validated the durability of XGBoost by demonstrating its superior perfor-
mance over Random Forest and linear regression by 6.4% and 18.2% MAE, respectively,
in our supplemental benchmark utilizing the public GEFCom2014 dataset, down-sam-
pled  to  5-minute  intervals,  and  with  10%  of  input  features  randomly  masked.  Table  4
lists a number of machine learning techniques used to forecast wind turbine power out-
put, along with some remarks about their particular circumstances.

The  performance  comparison  of  the  LSTM  and  GRU  models  in  wind  power  predic-
tion is displayed in Table 5. The task’s characteristics, the dataset’s size, and the available
resources all influence the decision between the Long Short-Term Memory (LSTM) and
Gated Recurrent Units (GRU) layers. Due to their exceptional performance, LSTMs and
GRUs  have  both  been  and  remain  highly  popular  in  NLP.  Overall,  GRUs  are  generally
more  effective  than  LSTMs  for  low-complexity  tasks.  High-complexity  tasks  that  ben-
efit  LSTMs.  GRUs,  on  the  other  hand,  are  more  resource-efficient,  which  makes  them
appropriate for building deeper networks that require rapid training. For deeper neuro-
nal learning with GRUs, more resources are required. But with LSTMs, more resources

Haq et al. Discover Applied Sciences          (2025) 7:1139 Page 11 of 32

Table 6  Performance comparison of the LSTM and GRU models for wind power prediction
Feature
Trainable Parameters More parameters – higher capacity but

LSTM

Training Speed
Model Complexity
Best Suited For

Resource Demand

greater computation cost
Slower due to complex gating structure
Higher – three gates + cell state
High-complexity, long-sequence forecasting
tasks
Needs more GPU/CPU and memory

Memory
Management

Dedicated cell state with input, forget, and
output gates for long-term dependencies.

GRU
Fewer parameters – lighter and faster
to train
Faster thanks to simpler architecture
Lower – two gates, no separate cell state
Lower-complexity or moderate-length
sequence forecasting
More efficient – better for limited
hardware
A single hidden state manages both
long-term memory and gate control.

Table 7  LSTM and GRU performance (RMSE) comparison using SCADA and weather data for tasks
of different complexity
Task
Complexity

Dataset Source

LSTM GRU

Notes

Perfor-
mance
Metric
RMSE

Low

Medium

High

SCADA data (Northern Europe,
2015–2022)
SCADA + ERA5 reanalysis
(2010–2021)
Hybrid SCADA & NWP data
(complex terrain sites)

0.85

0.83

RMSE

0.78

0.80

RMSE

0.74

0.76

Both models perform similarly
on simple tasks.
LSTM is slightly better at cap-
turing temporal dependencies
LSTM shows marginally better
accuracy but higher computa-
tional cost
Consistent preprocessing and
hyperparameter tuning

Experimental
Setup
  GRU  is  competitive  on  smaller  tasks  with  lower  computing  cost,  while  LSTM  exhibits  marginally  greater  accuracy  on
difficult tasks

NVIDIA RTX 3080 GPU, Tensor-
Flow 2.10, Optuna tuning

–

–

–

are required. Table 6 compares the performance of the LSTM and GRU models in wind
power prediction.

Memory and time dependency were the main differences between RNNs, LSTMs, and
GRUs in the model’s evolution. RNNs tend to retain information from past inputs, but
they struggle to handle long-term dependencies. In order to get around this, LSTMs use
specific  memory  cells  with  gates  that  allow  long-term  dependencies  to  be  stored  and
retrieved.  Although  LSTMs  and  GRUs  are  simpler  to  operate,  they  often  have  similar
performance and efficiency ratios, with a higher effectiveness-to-cost ratio. Table 7 sum-
marizes  the  comparative  performance  of  LSTM  and  GRU  models  across  forecasting
tasks  of  varying  complexity  using  SCADA  and  meteorological  datasets.  For  low-com-
plexity  tasks  based  primarily  on  SCADA  data  from  Northern  European  coastal  wind
farms  (2015–2025),  both  models  achieve  similar  accuracy,  with  GRU  slightly  outper-
forming LSTM in RMSE.

In medium-complexity scenarios integrating SCADA and ERA5 reanalysis data (2010–
2024), LSTM demonstrates a modest advantage, effectively capturing temporal depen-
dencies.  For  high-complexity  tasks  involving  hybrid  SCADA  and  numerical  weather
prediction data from complex terrain sites, LSTM again achieves marginally better accu-
racy at the cost of increased computational demand. All experiments were conducted on
an NVIDIA RTX 3080 GPU using TensorFlow 2.10 with Optuna-based hyperparameter
tuning,  ensuring  consistent  preprocessing  and  evaluation  protocols.  This  comparison
highlights  that  while  both  models  are  competitive,  LSTM  may  offer  improved  perfor-
mance on more complex forecasting tasks, albeit with greater resource requirements.

Haq et al. Discover Applied Sciences          (2025) 7:1139 Page 12 of 32

3  Feature selection and data preprocessing in wind power prediction

The  models  reviewed  and  evaluated  in  this  study  are  based  on  both  publicly  available
and proprietary wind power datasets. The primary sources are as follows:

SCADA-based operational data, obtained from Supervisory Control and Data Acqui-
sition  (SCADA)  systems  in  utility-scale  wind  farms,  covers  diverse  climatic  and  topo-
graphical  settings  such  as  coastal  sites  in  Northern  Europe,  flat  inland  farms  in  North
America,  and  complex  terrain  locations  in  East  Asia.  Data  spans  from  2015  to  2025
(site-dependent) and includes high-frequency (1–10 min) measurements of wind speed,
direction,  temperature,  and  power  output.  Each  site  provides  approximately  8000–
25,000 samples across six to ten meteorological and operational variables. These data-
sets,  referenced  in  [22–29],  are  either  publicly  available  (e.g.,  NREL  Wind  Integration
National Dataset) or obtained via collaboration (restricted access).

Meteorological  and  NWP  data,  sourced  from  national  meteorological  agencies  and
numerical weather prediction (NWP) model outputs such as ECMWF ERA5 reanalysis,
encompass offshore sites in the North Sea, continental U.S. locations, and Asia–Pacific
wind  corridors.  Historical  coverage  ranges  from  2010  to  2024,  with  hourly  resolution
for wind speed, air temperature, and atmospheric pressure, and spatial resolutions from
0.25° × 0.25° to 0.1° × 0.1°. Dataset sizes vary from ~ 100,000 to over 1 million time–loca-
tion records, with ERA5 data openly accessible via the Copernicus Climate Data Store.

Benchmark  public  datasets,  including  the  Global  Energy  Forecasting  Competition
datasets  (GEFCom2012,  GEFCom2014)  and  NREL  MET  and  Turbine  Data,  provide
widely  used  open-access  resources  containing  hourly  wind  power  and  meteorological
data  (GEFCom)  or  high-frequency  SCADA  and  mast  data  (NREL)  for  multiple  wind
farms.

In wind power forecasting, selecting the most relevant input features enhances both
prediction accuracy and computational efficiency. Three widely used methods are Recur-
sive  Feature  Elimination  (RFE),  Lasso  regression,  and  tree-based  feature  importance.
RFE iteratively removes the least important features based on model performance, offer-
ing model-agnostic minimal subsets but can be computationally intensive and sensitive
to noise; for example, applying RFE with XGBoost on the GEFCom2014 dataset reduced
variables  from  25  to  12  and  improved  LSTM  RMSE  by  ~ 7.7%.  Lasso  regression  uses
L1  regularization  to  shrink  some  coefficients  to  zero,  enabling  fast  embedded  feature
selection,  especially  effective  in  high-dimensional  linear  settings;  on  Northern  Euro-
pean SCADA data, Lasso cut predictors from 20 to 8, reducing training time by 30% and
improving  Random  Forest  MAPE  from  5.42  to  4.95%.  Tree-based  feature  importance,
derived from methods like Random Forest or XGBoost, measures each feature’s contri-
bution to splits and model performance, capturing nonlinear interactions and showing
robustness to multicollinearity; for instance, top features from XGBoost on fused ERA5
and SCADA data accounted for 85% of predictive power, allowing a pruned CNN-LSTM
to  run  20%  faster  without  MAE  loss.  Comparative  analysis  reveals  that  RFE  yields  the
most compact feature sets for small to medium datasets, tree-based importance is best
suited  for  nonlinear  problems,  and  Lasso  excels  at  rapid  screening  in  primarily  linear,
high-dimensional contexts. In practice, hybrid approaches combining Lasso pre-filtering
with tree-based ranking often strike the optimal balance among accuracy, interpretabil-
ity, and efficiency.

Haq et al. Discover Applied Sciences          (2025) 7:1139 Page 13 of 32

3.1  Methods of data preprocessing

Both  proprietary  and  publicly  accessible  wind  power  datasets  served  as  the  basis  for
the models examined and assessed in this study. The following are the primary sources:
(1)  SCADA-based  operational  data  from  utility-scale  wind  farms’  Supervisory  Control
and Data Acquisition (SCADA) systems, which cover a variety of topographical and cli-
matic environments, including complex terrain locations in East Asia, flat inland farms
in  North  America,  and  coastal  sites  in  Northern  Europe.  High-frequency  (1–10  min)
measurements of wind speed, direction, temperature, and power output are included in
the data, which covers the years 2015–2022 (location dependent). About 8,000–25,000
samples covering six to ten operational and climatic variables are provided by each sta-
tion. These datasets, which are cited in [24], can be acquired through partnership (lim-
ited  access)  or  are  publicly  accessible  (NREL  Wind  Integration  National  Dataset,  for
example).  Weather  and  NWP  information  from  national  weather  services  and  NWP
model  results,  including  ECMWF  ERA5  reanalysis,  includes  North  Sea  offshore  loca-
tions,  continental  U.S.  locations,  and  Asia-Pacific  wind  corridors.  With  hourly  resolu-
tions for wind speed, air temperature, and atmospheric pressure, and spatial resolutions
ranging from 0.25° x 0.25° to 0.1° × 0.1°, the historical coverage spans from 2010 to 2021.
ERA5 data is publicly available through the Copernicus Climate Data Store, and dataset
sizes range from about 100,000 to more than one million time-location records. Com-
monly used open-access resources that contain hourly wind power and meteorological
data  (GEFCom)  or  high-frequency  SCADA  and  mast  data  (NREL)  for  multiple  wind
farms are benchmark public datasets, such as the Global Energy Forecasting Competi-
tion datasets (GEFCom2012, GEFCom2014) and NREL MET and Turbine Data.

Thorough  data  purification  makes  it  possible  to  efficiently  prepare  and  clean  data,
which improves a model’s capacity to spot patterns, raises forecast accuracy, and reduces
biases.  This  stage  is  essential  for  developing  reliable  forecasting  models  that  improve
grid  operations  efficiency  and  energy  market  accessibility,  which  in  turn  helps  with
decision-making  that  improves  wind  power  prediction  accuracy.  Furthermore,  clean
and  trustworthy  datasets  for  machine  learning  are  produced  by  eliminating  noise  and
outlier artifacts. Data points that do not fit into predicted values can be removed with
the  aid  of  unsupervised  techniques  such  as  supervised  boxplots  or  z-scores.  Several
interpolation techniques, including spline and linear, can be used to fill in missing data
that results from severe weather, miscommunications, or sensor failures. Large volumes
of  missing  data  or  material  that  is  not  representative  can  be  easily  removed.  To  put  it
briefly, by setting the dataset using these techniques, the model is prevented from pro-
ducing predictions that could undermine its intended outcome. Large missing datasets
must  also  be  removed  because  it  would  be  pointless  to  try  to  measure  out  unlabelled
artifacts. Lastly, fixing missing data may simply be as easy as eliminating it. Preprocess-
ing  includes  removing  noise  and  outliers  from  the  surrounding  dataset,  in  addition  to
addressing missing values. By doing this, we guarantee that our models are dependable
and effective for their intended use. Missing values are mostly caused by malfunction-
ing sensors, poor communication, and inclement weather. It is crucial to guarantee the
precision and dependability of wind power data prediction models. Digital filters are one
of the preprocessing methods that improve the quality of wind power data records while
reducing noise levels. Problems with the communication infrastructure, environmental
variables,  and  sensor  disparities  produce  noise  that  obstructs  important  patterns  and

Haq et al. Discover Applied Sciences          (2025) 7:1139 Page 14 of 32

lowers  model  performance.  Savitzky-Golay  filtering  is  used  to  smooth  data  while  pre-
serving  important  local  characteristics.  Basic  data  simplification  is  achieved  by  simple
moving average filters, but the Savitzky–Golay filter matches polynomials with data in
sliding windows and uses moving polynomials to create new centre values. In contrast,
the widely used simple moving average (SMA) method smooths data by replacing each
point  with  the  mean  of  its  neighbours  within  a  fixed  window.  While  SMA  is  compu-
tationally  simple  and  effective  at  reducing  high-frequency  noise,  it  can  also  attenuate
peaks and flatten sharp transitions, potentially distorting signal features that carry use-
ful  predictive  information.  The  Savitzky–Golay  filter,  by  fitting  successive  polynomial
curves to local windows, not only reduces noise but also preserves important local struc-
tures such as maxima, minima, and gradients. This makes it especially advantageous in
wind power forecasting contexts where the shape of short-term fluctuations can indicate
rapid changes in wind conditions and turbine output [24–30]. This technique smoothes
the  data  while  preserving  significant  peaks  and  troughs,  which  is  crucial  for  accurate
wind power forecast results [25]. Users can maximize noise reduction while maintaining
key features depending on certain data conditions because it allows them to change both
the window’s dimensions and polynomial degrees. Filtering applications produce data-
sets that are smoother and more reliable, allowing predictive models to spot important
patterns and produce accurate and reliable forecasts. Research shows that the Savitzky–
Golay filter improves wind speed and power prediction results.

Data  cleaning,  including  removal  of  erroneous  outliers,  imputation  of  missing  val-
ues, sensor fault detection, and normalization of feature scales, directly improves model
stability  and  generalization.  In  our  benchmark  using  the  [GEFCom2014]  wind  power
dataset, applying these preprocessing steps before training an LSTM model reduced the
RMSE from 0.312 to 0.276 (an improvement of ~ 11.5%) and MAE from 0.248 to 0.216
(~ 12.9%  improvement).  This  aligns  with  reports  in  literature:  showed  that  identifying
and removing anomalous SCADA records improved short-term prediction accuracy by
8–15%  across  Random  Forest,  XGBoost,  and  CNN  models;  found  that  dimensionality
reduction and removal of inconsistent data reduced overfitting and improved MAPE by
up to 9% for coastal wind farm forecasting.

These improvements stem from eliminating noisy and misleading training examples,
allowing  algorithms  to  learn  more  meaningful  wind–power  relationships.  Such  gains
are  especially  important  in  operational  deployments,  where  raw  SCADA  data  often
contains erroneous points due to sensor drift, communication glitches, or maintenance
downtime.

3.1.1  Comparative analysis of Temporal horizons and regional accuracy variations

The accuracy of prediction on the horizons of wind power forecasting largely depends
on  the  forecasting  time  frame  as  well  as  the  geographical  location  of  implementation.
Although the forecasts are divided using the temporal classification framework diagram
(Table 8), into the following different categories ultra-short-term, short-term, mid-term
and  long-term,  a  major  question  is  how  the  standard  measures  of  accuracy,  say  Mean
Absolute  Error  (MAE)  and  Root  Mean  Square  Error  (RMSE),  vary  systematically  with
time scales across the various categories and in different regional conditions.

Temporal scale effects.

Haq et al. Discover Applied Sciences          (2025) 7:1139 Page 15 of 32

Table 8  Categorization of wind power forecasts by time scale
Forecast Horizon
Very Short-Term

Time Range
Within a few minutes

Ultra-Short-Term

Within 30 min

Short-Term

30 min – several hours

Mid-Term

Seasonal

Annual

A few days – a few months

Several months – 1 year

1 year or more

Long-Term

Multiple years

Typical Applications
Instant turbine output control; rapid grid
stability adjustments
Real-time dispatch and scheduling; immediate
wind farm operation control
Day-ahead electricity market bidding; daily
grid operation and scheduling
Maintenance planning; seasonal operation
preparation; medium-term market transactions
Seasonal supply planning; long-term resource
allocation strategies
Policy formulation; infrastructure investment
planning; capacity expansion assessment
Site selection; climate feasibility studies; strate-
gic energy policy development

  • Ultra-short-term forecasts (minutes to an hour) typically yield the lowest error values
due to reduced uncertainty in meteorological inputs and minimal impact from large-
scale  weather  system  variability.  For  example,  MAE  values  often  fall  below  2–3%,
with RMSE under 5%, when SCADA data with high temporal resolution is leveraged.
  • Long-term  forecasts  (months  to  years)  inherently  accumulate  higher  uncertainty
from atmospheric variability, seasonal oscillations, and climate anomalies. Empirical
studies  show  MAE  frequently  exceeding  10%,  with  RMSE  rising  above  15%,  even
when incorporating ensemble numerical weather prediction (NWP) models.

Regional variability.

Geographic regions exhibit differing error patterns due to climate characteristics, ter-

rain complexity, and data infrastructure:

  • Flat  inland  regions  (e.g.,  US  Midwest,  Inner  Mongolia,  parts  of  Northern  Europe)
often support more accurate short-term predictions due to less turbulence and more
predictable  wind  regimes.  Ultra-short-term  RMSE  in  these  environments  can  be
20–30% lower than in mountainous terrain.

  • Coastal  and  offshore  sites  benefit  from  steadier  wind  flows,  with  both  short-  and
long-term models showing reduced error spread compared to continental interiors
influenced by synoptic variability.

  • Complex  terrain  (mountainous  or  forested  areas)  introduces  higher  variability  in
wind speed, leading to increased errors across all horizons—particularly long-term
forecasts, where RMSE can be 30–50% higher than in flat terrain locations.

Interaction between temporal and regional factors.

  • Comparative multi-site analyses demonstrate that temporal accuracy decay is steeper
in complex and data-sparse environments. For example, an ultra-short-term forecast
in offshore Denmark might have an RMSE of ~ 4%, while its one-year forecast may
still retain an RMSE below 12%, whereas in mountainous Southern China, equivalent
figures may be ~ 6% and ~ 20%, respectively.

Implications for model selection and deployment.

The above patterns underscore that temporal classification should be complemented

with region-specific calibration and horizon-sensitive model choice:

Haq et al. Discover Applied Sciences          (2025) 7:1139 Page 16 of 32

  • Ultra-short-term, high-frequency forecasts in coastal/offshore regions can effectively

exploit lightweight ML methods or hybrid physical–data-driven approaches.

  • Long-term forecasting in complex terrains may require downscaling NWP outputs

and integrating stochastic ensemble strategies to manage uncertainty growth.

A dedicated understanding of the interplay between time horizon and geographical vari-
ability enhances both the interpretability of forecast performance metrics and the prac-
tical relevance of deployed models.

3.2  Feature selection’s effect on model performance

With  its  ability  to  choose  key  data  features  from  large  datasets,  feature  selection  is  a
crucial step in improving the accuracy of wind power predictions. The process of gath-
ering  wind  power  data  involves  entering  several  factors,  including  wind  direction  and
speed, temperature and pressure readings, and details regarding turbine operations [26].
Using these features increases the accuracy of decision-making, but adding extraneous
or redundant variables will make the model more complex and lead to overfitting, which
lowers accuracy levels. Since feature selection identifies key traits that produce simpli-
fied models and provide speed and comprehension for interpretation, it can address the
issues  of  noise  and  computational  cost  [27].  In  order  to  improve  model  optimization,
model  importance  evaluation  strategies  include  progressive  feature  elimination  using
Recursive Feature Elimination (RFE) and feature significance analysis utilizing Random
Forest to ascertain the impact on impurity reduction. This approach to choosing leading
variables improves model generalization, prevents overfitting, and provides crucial wind
power generation elements to produce effective model predictions [28]. The identifica-
tion of key factors influencing wind power output, as well as crucial characteristics such
as wind direction and speed, as well as the behaviour of temperature and air pressure, is
made possible by a combination of techniques.

Prior  to  building  predictive  modelling  frameworks,  wind  power  analysis  necessitates
the extraction of periodic components and temporal relationships from the data. Data
extraction  methods  such  as  the  Fourier  transform  and  the  wavelet  transform  are  used
to find pattern frequencies and produce temporal features that improve model perfor-
mance  [29,  31–33].  When  working  with  time-series  data,  the  technological  technique
of lag embedding assists in extracting historical data information that helps the model
make predictions for the present.

3.3  Model configurations and hyperparameter optimization

To  ensure  reproducibility  and  transparency  of  the  reported  performance  results,  the
configurations  of  the  evaluated  machine  learning  (ML)  models  and  their  training  pro-
cesses are described below.

3.3.1  Model architecture and input configuration

The  LSTM  networks  were  configured  with  two  hidden  layers  comprising  64  and  32
units, respectively, using a tanh activation function and a dropout rate of 0.2. The input
consisted of a 60-minute time-lagged sequence window, with output predictions ranging
from 10 to 30 min ahead. GRU networks followed an identical input–output structure
for a fair comparison, utilizing two hidden layers of 48 and 24 units, tanh activation, and
a  dropout  rate  of  0.2.  The  CNN  models  included  a  single  1D  convolutional  layer  with

Haq et al. Discover Applied Sciences          (2025) 7:1139 Page 17 of 32

64  filters  (kernel  size = 3),  followed  by  max-pooling,  two  dense  layers  with  128  and  64
units,  ReLU  activation,  and  a  dropout  rate  of  0.25.  For  XGBoost,  the  parameters  were
set to a maximum depth of 6, learning rate of 0.1, 500 estimators, a subsample ratio of
0.8, and a column sample by tree ratio of 0.8. Random Forest: 200 decision trees, max
features = sqrt, min samples split = 2.

3.3.2  Training process

The  dataset  was  split  chronologically  into  70%  training,  15%  validation,  and  15%  test-
ing  sets  to  prevent  data  leakage.  For  deep  learning  models,  the  Adam  optimizer  with
a  learning  rate  of  0.001  and  mean  squared  error  (MSE)  loss  function  was  employed,
while ensemble/tree-based models utilized their built-in Gini or MSE split criteria. Deep
learning models were trained with a mini-batch size of 64, a maximum of 200 epochs,
and early stopping based on validation loss with a patience of 10 epochs.

3.3.3  Hyperparameter optimization methodology

Hyperparameter  tuning  was  performed  using  a  grid  search  for  traditional  machine
learning  models  and  Bayesian  optimization  for  deep  learning  models  via  the  Optuna
library. The search space for LSTM/GRU networks included the number of layers (1–3),
units per layer (16–128), dropout rates (0–0.4), and learning rates (1 × 10⁻⁴ to 1 × 10⁻²).
For XGBoost, the search space comprised maximum depth (3–10), learning rate (0.01–
0.3),  and  subsample  ratio  (0.5–1.0).  The  best-performing  configurations  were  selected
based on the lowest validation RMSE.

3.3.4  Computational environment

Experiments were conducted using an NVIDIA RTX 3080 GPU with TensorFlow 2.10
and Scikit-learn 1.2 for model training and evaluation. For lightweight edge device test-
ing,  a  Raspberry  Pi  4B  (4  GB  RAM)  was  employed,  utilizing  TensorFlow  Lite  models
where applicable to assess deployment feasibility under resource-constrained conditions.

4  Particular uses of machine learning models for forecasting wind power

According  to  Table  8,  the  time  scale  establishes  the  classification  of  wind  power  fore-
casting  into  ultra-short-term,  short-term,  medium-term,  and  long-term  forecasting
categories.

Effective  short-term  forecasts  of  wind  power  generation  are  critical  to  grid  stability
and power system scheduling. Researchers show that prediction accuracy increases sig-
nificantly  when  contemporary  machine  learning  techniques  are  combined  with  tradi-
tional modeling methodologies [34]. The use of CNN-LSTM models outperformed the
conventional  Random  Forest  and  Support  Vector  Regression  (SVR)  techniques,  yield-
ing more accurate prediction results. CNN-LSTM models efficiently track actual power
flows,  which  makes  them  suitable  for  addressing  wind  energy  integration  challenges
arising  from  intermittent  power  generation,  according  to  research  based  on  year-long
power output projections. According to a recent study, improvements, predicting high
accuracy, are just as important as computing efficiency performance [35].

Accurate  forecasts  of  wind  power  developments  in  incredibly  short  timeframes  are
vital  to  operational  grid  management.  When  researchers  employ  noise-enhanced  data
augmentation  strategies  to  improve  model  stability  and  generalization  capabilities,  the

Haq et al. Discover Applied Sciences          (2025) 7:1139 Page 18 of 32

predictive model’s robustness rises [36]. Dynamic learning models, such as LSTM, have
been  shown  in  numerous  experiments  to  be  highly  effective  at  tracking  temporal  pat-
terns over short periods. Because they highlight the relevance of high-quality data sets
combined with efficient training strategies for accurate predictions in short periods, the
models perform better than static benchmarks [37].

In  order  to  address  the  operational  diversity  of  wind  farms,  researchers  combined
probabilistic machine learning techniques with geographical features to create spatially
transferable models. Regardless of the site location, the predictive models show a track
record of accuracy in projecting the amounts of electricity produced. The investigation
shows how machine learning models reduce computational processing while performing
in sync with real measurements. The technique supports dynamic, real-time operations
in wind energy systems that need geographic flexibility [38].

Utilizing CNNs in conjunction with LSTMs yields precise wind power forecasts due to
their complementary skills in analyzing spatial and temporal data; hybrid models exhibit
consistent  performance  across  locations  with  varying  climatic  and  topographical  fea-
tures; these models are crucial due to their adaptability to diverse applications in global
renewable energy environments; grid integration benefits from this approach as it inte-
grates multiple environmental factors to maintain renewable energy solutions [39–44].

The six wind power forecasting categories are shown in Fig. 5 in a chronological order
that makes it simple to compare their forecast horizons and common uses. While very
short-term  predictions  (within  minutes)  allow  for  instant  stability  adjustments  and
ultra-fast  dispatch  decisions,  ultra-short-term  forecasts  (less  than  30  min)  facilitate
real-time  turbine  and  grid  control  with  quick  response  to  abrupt  wind  changes.  Daily
operations, market bidding, and day-ahead scheduling are all influenced by short-term
projections, which range from 30 min to several hours. Day-to-month projections help
in  resource  allocation  and  maintenance  planning.  Long-term  infrastructure  develop-
ment, investment, and policy decisions are supported by annual forecasts (one year or
more),  whereas  supply  and  storage  system  planning  is  guided  by  seasonal  predictions
(several months to a year). This timeline helps readers rapidly connect forecasting hori-
zons to their real-world applications by graphically illustrating the shift from immediate
operational management to strategic, long-range planning.

4.1  Forecasting wind power for low-cost devices

The  feasibility  of  cost-effective  wind  power  forecast  systems  for  resource-constrained
environments  is  demonstrated  by  the  use  of  lightweight  machine  learning  models  on
Raspberry  Pi  devices.  Models  can  produce  effective  predictions  without  consuming  a
lot of processing resources when optimized model architectures, network layer pruning
techniques, and pre-trained architecture selection are used. This method makes it pos-
sible  to  develop  scalable  distributed  predictive  systems  that  reduce  reliance  on  central
infrastructure and expedite wait times [45]. Strong opportunities for deploying machine

Fig.  5  Timeline-style  visualization  of  wind  power  forecasting  categories.  Each  category  is  positioned  along  a
chronological axis with its approximate time range and examples of typical application scenarios

Haq et al. Discover Applied Sciences          (2025) 7:1139
Page 19 of 32

learning models are created by the Raspberry Pi range of contemporary low-cost hard-
ware,  particularly  when  working  with  inaccessible  or  resource-constrained  areas  [46].
Computational methods that combine network pruning, layer simplification, and param-
eter optimization to produce accurate wind power forecasts. Small wind power projects
and  areas  with  limited  computer  infrastructure  benefit  greatly  from  this  deployment
strategy.  These  portable  models  improve  decision-response  times,  provide  a  flexible
solution  for  wind  power  forecasting  operations,  and  allow  for  real-time,  efficient  fore-
casting at the site while reducing dependency on centralized facilities [47]. The low-cost
Raspberry  Pi  platforms  and  their  energy-efficient  features  are  used  to  power  machine
learning models. Due to their lower processing speed, memory storage, and computing
power, the devices are limited in their ability to perform in comparison to high-perfor-
mance systems. Because these systems must handle large data arrays utilizing intricate
algorithms  and  real-time  execution,  their  limits  pose  challenges  for  resource-intensive
applications like wind power prediction [48]. In order to overcome these challenges, sci-
entists developed optimization strategies to increase model efficiency while maintaining
forecast accuracy. Feature selection is a data processing strategy that focuses on deter-
mining the key characteristics of data that should be retained [49]. In data processing,
dimension  reduction  enhances  generalization  accuracy,  prevents  model  overfitting,
and  boosts  system  performance  and  memory  capacity.  Doctors  utilize  model  pruning,
which finds unnecessary elements in neural networks, such as individual nodes, connec-
tions, and layers, for model optimization. This data compression tool is useful for indus-
try applications since it improves algorithm processing speed and memory use without
compromising predicted accuracy. By removing unnecessary weights and entire layers,
weight  pruning  and  structural  pruning  are  popular  techniques  for  adapting  models  to
low-resource devices [50].

Additional  quantization  techniques  reduce  accuracy  levels  by  using  integer  values,
such as 8-bit rather than floating-point 32-bit format, which reduces processing power
and  memory  use.  Along  with  effective  designs  designed  for  these  platforms,  workers
in  low-cost  platforms  can  benefit  from  unique  algorithms  known  as  MobileNet  and
TinyML. When these operational methods are combined, low-cost applications can use
the  fewest  resources  possible  to  perform  wind  power  forecast  capabilities.  Predictive
analytics applications in renewable energy systems are growing as a result of new tech-
nological  developments  that  enable  the  implementation  of  machine  learning  solutions
in a variety of real-world settings, particularly in distant or underresourced places [51].

4.2  Forecasting wind power in particular situations

When  wakes  are  present  and  yaw  control  is  activated,  wind  farms’  power  output  is
significantly  reduced.  Through  dynamic  adjustments  to  yaw  parameters,  the  study
suggested inspector adaptation as a wind farm control technique that maximizes perfor-
mance results [52]. The goal of machine learning techniques is to estimate wind turbine
fatigue load and power output under yaw adjustment situations. Because the SVR model
accounts  for  both  wake  effects  and  yaw  misalignment,  it  provides  accurate  and  effec-
tive predictions. The suggested model outperforms traditional methods for yaw control
optimization in terms of accuracy and robustness [53]. This approach can reduce wind
farm  structural  fatigue  and  maximize  power  output.  When  active  yaw  control  devices

Haq et al. Discover Applied Sciences          (2025) 7:1139 Page 20 of 32

are  used,  the  suggested  framework  increases  the  prediction  accuracy  of  power  output
estimates and fatigue loads.

When complicated weather patterns are brought about by climate change, it becomes
more  difficult  to  anticipate  wind  power.  Accurate  forecasting  is  challenging  due  to  a
combination of fluctuating wind resources and changing meteorological conditions that
increase  the  frequency  of  catastrophic  events.  The  requirement  for  difficult  barriers
necessitates models that combine advanced techniques with domain-specific knowledge
[54].  Combining  machine  learning  methods  with  gray  models  turns  out  to  be  a  viable
remedy.  Because  grey  models  enable  users  to  see  patterns  in  wind  power  data  under
uncertain conditions, they are a useful method for handling both restricted and uncer-
tain  data  sets.  Because  machine  learning  excels  at  huge  data  analysis  and  relationship
discovery,  our  hybrid  prediction  system  achieves  higher  accuracy  outcomes  by  com-
bining  grey  models  with  machine  learning  techniques.  Grey  models  are  supported  by
machine learning algorithms that analyze large amounts of meteorological data and use
nonlinear pattern recognition to produce better forecasts. By improving the forecasting
system’s ability to adapt to weather variations, the combination increases the accuracy of
wind power predictions [55].

Accurate  wind  power  forecasting  in  extreme  weather  events  (e.g.,  typhoons,  cold
fronts,  thunderstorms)  remains  challenging  because  of  rapid  wind  speed  fluctua-
tions, data sparsity during rare events, and nonlinear atmospheric interactions. Recent
advances address these issues through:

Transfer  learning  and  domain  adaptation  fine-tuned  LSTM  models  pre-trained  on
large historical datasets using limited storm-period data, reducing MAE by 12% under
typhoon conditions [56].

Physics-informed neural networks (PINNs) Wang et al. (2022) integrated turbulent flow
equations into a deep learning framework, improving RMSE by up to 15% during frontal
passages [57].

Under complex terrain (e.g., mountainous, coastal–inland transition zones), wind flow

heterogeneity can undermine purely statistical learning. Effective approaches include:

Hybrid  CFD–ML  workflows  CFD  simulations  generate  high-resolution  flow  fields  to
augment  measurement  datasets,  which  are  then  modelled  with  gradient  boosting  or
CNN–LSTM architectures [58].

High-resolution  NWP–ML  fusionCombining  mesoscale  WRF  output  with  local
SCADA inputs in a multivariate LSTM improved day-ahead forecasting accuracy by 9%
in alpine sites [59].

Graph  Neural  Networks  (GNNs)  :GNN  frameworks  have  been  shown  to  model  spa-
tial–temporal dependencies between turbines in irregular terrain, improving short-term
RMSE by 6–8% [60].

These  proven  techniques  provide  quantifiable  gains  in  forecast  performance  without
depending on conjecture, underscoring the significance of firmly establishing replicable
evidence as the foundation for methodological discussion.

5  Analysing and improving machine learning model performance

An essential step in determining the operational and reliable features of wind power pre-
diction  models  in  real-world  technological  contexts  is  testing  them.  Standard  metrics,
such as Mean Squared Error (MSE), Mean Absolute Error (MAE), and the R2 coefficient,

Haq et al. Discover Applied Sciences          (2025) 7:1139 Page 21 of 32

are used to assess wind power forecasts. In order to facilitate model comparison, stan-
dard  performance  measures  provide  numerical  results  that  quantify  forecast  accuracy
and system stability. Researchers and practitioners can assess and improve wind power
prediction technologies that are prepared for practical deployment in uncertain environ-
ments by using standard measures.

  • Mean Squared Error (MSE): Larger errors resulting from the squaring process are
given more weight in this metric, which computes the average squared discrepancies
between  anticipated  and  actual  values.  It  is  especially  helpful  for  penalizing  large
variations in wind power projections since it is sensitive to outliers. Its sensitivity to
extreme values, meanwhile, can occasionally overemphasize infrequent occurrences.

MSE = n1t = 1

n(yt

y∧t)2

−

∑

  • Mean Absolute Error (MAE): MAE is a simpler indicator of average error size than
MSE since it concentrates on the absolute differences between expected and actual
values. Because MAE is less impacted by outliers, it is a useful addition to MSE for
evaluating overall model performance without unduly penalizing sporadic significant
errors. We use commonly used statistical error metrics in wind power prediction to
assess forecasting model accuracy.

MAE = n1t = 1

n

yt
|

−

y∧t

|

∑

  • R² Coefficient (Coefficient of Determination): The degree to which the predictions
account for the variation in the actual data is shown by the R² score. Strong predictive
power is demonstrated by a model that explains the majority of the variance in the
target variable, as indicated by an R2 value near 1. It is employed to assess the model’s
stability, generalizability, and goodness of fit under various circumstances.

R2 = 1

−

t = 1n

yt −

y−

2

t = 1n (yt −

y∧t) 2

∑

(

)

∑

XGBoost regression models produce good results with low MSE metrics and strong R2
statistics when used to anticipate short-term wind power generation from SCADA data.
Wind  speed  observations,  power  production  measurements,  and  turbine  operational
data provided by SCADA systems at regular data collection intervals are all useful to the
prediction  models.  Because  it  employs  regularization  to  prevent  overfitting  and  effec-
tively manages big datasets and missing values, XGBoost has great efficacy as a gradient
boosting method [61].

PSO  is  an  optimization  method  that  runs  possible  solutions  as  “particles”  through
each simulation process using the social group behaviors of flocks or schools. Particulate
movements result from both the swarm’s ideal placements and its knowledge. To choose
the  best  parameter  values  to  settle  on,  the  algorithm  iteratively  repeats  its  procedure.
The  best  use  of  PSO’s  optimization  capabilities  is  as  a  tool  for  determining  the  ideal
hyperparameters for difficult machine learning techniques like support vector machines
and  neural  networks.  Through  parameter  modifications  made  possible  by  PSO,  pre-
diction errors are reduced and model accuracy is increased [62]. Fruit flies’ instinctive
food-searching  behavior  serves  as  the  model  for  the  Fruit  Fly  Algorithm.  The  method
evaluates parameters using an objective function and makes successive tweaks until the

Haq et al. Discover Applied Sciences          (2025) 7:1139 Page 22 of 32

best  answer  is  found.  In  addition  to  being  effective  for  situations  requiring  little  com-
puter power, researchers have observed that the Fruit Fly Algorithm is straightforward
and reliable [63].

The  optimization  techniques  offer  a  number  of  benefits  due  to  their  effectiveness,
ability  to  manage  non-linear  connections,  and  flexibility  in  responding  to  the  numer-
ous  complexities  included  in  wind  power  data.  These  optimization  techniques  exhibit
the capacity to quickly converge near optimal solutions and easily adjust to unique data
patterns  present  in  various  wind  farms.  By  applying  these  strategies,  prediction  mod-
els are able to reduce prediction mistakes and improve forecasting precision. Because it
improves  wind  power  prediction  functions,  the  application  of  parameter  optimization
approaches  results  in  improved  grid  scheduling,  wind  farm  management,  and  power
market  operations,  all  of  which  effectively  assist  the  exploitation  of  renewable  energy
[64].

In  wind  power  forecasting,  hyperparameter  optimization  methods  vary  in  complex-
ity  and  efficiency.  Traditional  grid  search  performs  an  exhaustive  exploration  over
predefined  parameter  ranges,  ensuring  full  coverage  but  at  a  high  computational  cost,
especially  in  high-dimensional  spaces.  Bayesian  Optimization  (BO)  leverages  probabi-
listic  surrogate  models  to  balance  exploration  and  exploitation,  often  achieving  com-
parable  or  better  accuracy  than  nature-inspired  metaheuristics  like  Particle  Swarm
Optimization  (PSO)  and  the  Fruit  Fly  Algorithm  (FOA)  with  fewer  evaluations.  For
example,  BO  tuned  LSTM  models  for  short-term  forecasting  in  about  30  trials  com-
pared to roughly 80 trials for PSO. However, in higher-dimensional or irregular search
spaces, such as those for hybrid CNN-LSTM architectures, metaheuristics like PSO and
FOA can outperform BO by better escaping local minima and not relying heavily on sur-
rogate model assumptions. Grid search remains useful primarily for small search spaces
or benchmarking. Recent hybrid approaches combining BO for coarse tuning followed
by PSO for fine-tuning have shown promise, achieving faster convergence without sacri-
ficing final accuracy.

5.1  Integrating hybrid models and ensemble learning techniques

Ensemble learning techniques that combine CNN-LSTM hybrid models with XGBoost
and Random Forest are beneficial for wind power prediction because they take advan-
tage  of  the  unique  characteristics  of  several  models.  Organizations  can  achieve  higher
forecast  accuracy  rates  and  dependability  standards  by  combining  many  base  models
into  an  ensemble  [65].  The  Random  Forest  approach  combats  model  overfitting  and
enhances generalization skills by combining predictions from several decision trees. By
gradually adjusting prediction mistakes, the XGBoost model uses gradient boosting to
enhance model performance.

CNN  and  LSTM  architectures  work  well  together  to  create  hybrid  models  that  can
handle  complex  wind  power  data  formats.  Convolutional  Neural  Networks  are  excel-
lent  at  recognizing  patterns,  which  allows  them  to  analyze  the  spatial  relationships
between incoming data components quickly. Both long-term trends and temporal con-
nections  within  datasets  can  be  successfully  inferred  using  Long  Short-Term  Memory
(LSTM) networks. Better wind power forecasting is made possible by CNN-LSTM mod-
els, which integrate temporal sequence modeling from LSTMs with spatial information
from CNNs [66].

Haq et al. Discover Applied Sciences          (2025) 7:1139 Page 23 of 32

The primary advantage of these methods is their capacity to increase both prediction
robustness  and  accuracy.  By  connecting  disparate  operational  strengths  across  pre-
diction  domains  and  filtering  individual  model  faults  through  perspective  integration,
ensemble learning, and hybrid models work together. This approach produces accurate
short-  and  long-term  forecast  results  by  effectively  managing  the  variability  of  wind
power data. Ensemble and hybrid models, which have demonstrated their importance as
predictive tools, are crucial for wind power prediction and renewable energy grid inte-
gration [67].

Using  nonlinear  wind  speed  fluctuations  and  shifting  error  patterns,  these  scientists
demonstrated a mix of statistical and machine learning techniques for wind power inter-
val  forecasting.  After  doing  an  assessment,  the  researchers  found  that  LSTM  was  the
best  regression  technique  for  increasing  accuracy  and  predicting  uncertainty.  Enhanc-
ing  wind  power  insertion  into  power  networks  is  made  possible  by  this  methodology.
Through  their  prediction  intervals,  the  evaluation  findings  of  five  nonlinear  machine
learning algorithms showed that they could accurately estimate genuine wind power val-
ues [68].

The  study  shows  that  accurate  electricity  demand  forecasting  is  crucial  for  modern
power systems, with traditional statistical methods like ARIMA offering limited ability
to capture complex nonlinear patterns. Machine learning approaches such as SVM, Ran-
dom Forest, and ANN improve accuracy but still face challenges in modeling long-term
temporal  dependencies.  Deep  learning  techniques,  especially  RNNs  and  LSTMs,  have
proven  effective  in  handling  sequential  and  time-dependent  energy  data,  with  LSTMs’
memory capabilities outperforming simple RNNs in many studies. Hybrid models com-
bining RNN and LSTM have emerged as a promising solution, leveraging the strengths
of both architectures to improve forecast precision, as demonstrated in prior research,
achieving  high  R²  and  low  error  rates.  This  foundation  supports  the  proposed  RNN–
LSTM  approach,  which  builds  on  these  advancements  to  deliver  superior  short-term
electricity demand predictions [69].

The proposed hybrid model integrates the LightGBM algorithm with Grid Search opti-
mization to achieve high predictive accuracy and computational efficiency. To enhance
interpretability, it incorporates Shapley Additive explanations (SHAP) and Local Inter-
pretable Model-Agnostic Explanations (LIME), providing transparent insights into fea-
ture  importance.  A  comprehensive  comparison  with  other  classification  algorithms,
evaluated using accuracy, recall, and F1 score, demonstrates the hybrid model’s superior
performance,  achieving  99.91%  accuracy. This  approach  not  only  offers  practical  value
for handling large datasets in real-world power systems but also advances the theoretical
and practical aspects of failure prediction for sustainable and reliable energy infrastruc-
tures [70].

This study identifies low urban wind speeds and high turbulence intensity as the pri-
mary challenges limiting the development of urban wind energy. It emphasizes the need
for further research focused on advanced urban wind resource assessment methods and
innovative wind energy harvester designs to enhance the efficiency and feasibility of har-
nessing wind power in urban environments [71]. More detailed information about the
characteristics, methods, and technology covered in each citation is provided in Table 9.
According  to  the  papers  consulted,  Fig.  5  shows  the  usage  patterns  of  research
approaches  employed  in  wind  power  prediction.  Machine  learning  (8  studies),  LSTM

Haq et al. Discover Applied Sciences          (2025) 7:1139 Page 24 of 32

Table 9  Provide more precise information on the characteristics, methods, and technology
included in each source
Citation
[45]

Existing Research
Lightweight machine learning models on low-
cost devices like Raspberry Pi for wind power
prediction in resource-limited environments.
Portability and energy efficiency of low-cost de-
vices like Raspberry Pi for implementing machine
learning models.
Real-time, on-site predictions reduce dependency
on centralized infrastructure with lightweight
models.
Computational limitations of low-cost devices
and challenges in wind power prediction.

Feature selection to improve model efficiency by
retaining essential features from the data.

Model pruning techniques (weight pruning and
structured pruning) are used to make models
suitable for low-resource devices.
Quantization and efficient algorithms like Mo-
bileNet and TinyML for low-cost devices perform-
ing wind power prediction.
Wind farm control strategy using modifier adapta-
tion for yaw control to improve power output.

Use of Support Vector Regression (SVR) to predict
fatigue loads and power output under yaw
control.
Impact of climate change and complex meteoro-
logical conditions on wind power prediction.

Integration of grey models with machine learning
to improve prediction accuracy in wind power
forecasting.
Machine learning models like LSTM and CNNs are
used to analyze meteorological data and improve
wind power forecasting.
Machine learning algorithms for icing detection
and prediction on turbine blades to improve
operational efficiency.
Advancements addressing complexities in wind
power prediction, supporting sustainable energy
amidst climate change.
Use of XGBoost regression for short-term wind
power prediction using SCADA system data.

Impact of turbulence intensity on ultra-short-
term wind power prediction; turbulence doesn’t
significantly improve accuracy.
Optimization methods like Particle Swarm Optimi-
zation (PSO) and the Fruit Fly Algorithm are used
for improving wind power prediction models.
PSO is applied to optimize hyperparameters for
machine learning models like neural networks
and support vector machines.
Use of the Fruit Fly Algorithm for optimizing
parameters in wind power prediction models.

Main Features/Techniques
Lightweight models, edge computing,
Raspberry Pi, wind power forecasting, cost-
effectiveness, and real-time predictions.
Portability, energy efficiency, distributed
computing, machine learning on low-cost
devices, and deployment flexibility.
Decentralized systems, real-time wind power
prediction, low-latency, and reducing depen-
dency on centralized infrastructure.
Computational limitations, memory con-
straints, processing power limitations, and
wind power prediction challenges.
Feature selection, dimensionality reduc-
tion, improved processing speed, reduced
memory usage, and preventing overfitting.
Model pruning, weight pruning, structured
pruning, reduced computational load, and
memory optimization.
Quantization, model efficiency, MobileNet,
TinyML, reduced computation precision, low-
cost devices, and memory savings.
Yaw control, modifier adaptation, wind farm
management, power output optimization,
and active yaw control.
Support Vector Regression (SVR), fatigue load
prediction, yaw misalignment correction, and
accurate power output forecasting.
Climate change impact, meteorological
variability, wind power prediction accuracy
challenges, and extreme weather conditions.
Grey models, machine learning integration,
nonlinear relationships, uncertainty handling,
improved prediction robustness.
LSTM (Long Short-Term Memory), CNN
(Convolutional Neural Networks), time-series
forecasting, and spatial and temporal data.
Icing detection, predictive maintenance, sen-
sor data analysis, turbine blade optimization,
and operational efficiency.
Sustainable energy solutions, climate adapta-
tion, prediction model advancements, and
addressing data complexities.
XGBoost, regression modeling, SCADA system
data, short-term forecasting, high-frequency
data processing.
Turbulence intensity, ultra-short-term wind
power prediction, meteorological variables,
model accuracy analysis.
PSO (Particle Swarm Optimization), Fruit Fly
Algorithm, hyperparameter tuning, optimiza-
tion of machine learning models.
PSO for hyperparameter optimization, neural
networks, support vector machines, and tun-
ing model parameters.
Fruit Fly Algorithm, optimization, parameter
tuning, and improvement of prediction
accuracy.

[46]

[47]

[48]

[49]

[50]

[51]

[52]

[53]

[54]

[55]

[56]

[57]

[58]

[59]

[60]

[61]

[62]

[63]

Haq et al. Discover Applied Sciences          (2025) 7:1139 Page 25 of 32

Table 9  (continued)

Citation
[64]

[65]

[66]

[67]

[68]

Existing Research
Benefits of PSO and the Fruit Fly Algorithm in
improving model accuracy for wind power
prediction.
Ensemble learning methods like XGBoost and
Random Forest to improve wind power predic-
tion accuracy.
Hybrid CNN-LSTM models to capture both spatial
and temporal dependencies in wind power data.

Effectiveness of ensemble and hybrid models
in managing uncertainty and variability in wind
power data.
Integration of machine learning and statistical
approaches for interval forecasting in wind power
prediction, LSTM enhances forecast accuracy.

Main Features/Techniques
Optimization efficiency, reduced prediction
errors, model accuracy improvement, PSO,
Fruit Fly Algorithm.
Ensemble learning, Random Forest, XGBoost,
aggregation of model predictions, improved
generalization, and accuracy.
Hybrid models, CNN-LSTM, spatial dependen-
cies, temporal dependencies, complex data
handling, and improved prediction accuracy.
Ensemble learning, hybrid models, uncer-
tainty management, data variability, robust
predictions, and long-term forecasting.
LSTM (Long Short-Term Memory), statistical
approaches, interval forecasting, uncertainty
quantification, and forecast accuracy.

Fig. 6  Techniques employed in wind power prediction research frequently

(3 studies), PSO (3 studies), Fruit Fly Algorithm (3 studies), and lightweight models (3
studies) are the primary research approaches employed. In order to improve prediction
accuracy, real-time performance, and computing efficiency, this study explores ensemble
learning  in  conjunction  with  hybrid  models,  feature  selection,  and  quantization  tech-
niques.  The  study  demonstrates  how  researchers  use  deep  learning  models  (LSTM,
CNN) and optimization techniques (PSO, Fruit Fly Algorithm) in conjunction with real-
time edge computing solutions for wind power forecasting (Fig. 6).

Figure 7 displays a line graph that illustrates the patterns in the application of various
methods in wind power prediction studies over time. It shows how research has changed
from  2015  to  2025  using  approaches  like  machine  learning,  optimization  (PSO,  Fruit
Fly), deep learning (LSTM, CNN), edge computing, and ensemble learning.

6  Key observations

Although  advanced  machine  learning  models  like  LSTM  and  CNN,  along  with
ensemble  techniques  such  as  Random  Forest  and  XGBoost,  show  strong  poten-
tial  for  wind  power  forecasting,  significant  challenges  remain  in  achieving  real-time

Haq et al. Discover Applied Sciences          (2025) 7:1139

Page 26 of 32

Fig. 7  Trends in Wind Power Forecasting Methods from 2015 to 2025

deployment—particularly  on  low-cost  devices  in  remote  locations.  Further  research  is
required to address operational issues caused by power fluctuations and system adjust-
ments during extreme weather events. Equally crucial is analyzing how diverse climatic
conditions  influence  model  performance  to  ensure  reliable  predictions.  Additionally,
integrating wind power forecasting with other renewable energy sources could enhance
global energy management. Techniques such as pruning, quantization, and effective fea-
ture  engineering  can  help  improve  model  efficiency  and  generalization,  making  them
suitable for edge computing applications in remote wind farms.

6.1  Model applicability in different scenarios

While  metrics  like  MAE,  RMSE,  and  MAPE  are  useful  for  benchmarking,  selecting
the  right  wind  power  forecasting  model  also  depends  on  the  operational  context.  Key
considerations  include  data  availability,  forecast  horizon,  geographic  setting,  compu-
tational  capacity,  and  interpretability  requirements.  In  data-rich  environments  such
as  large  SCADA  archives  or  offshore  wind  farms,  deep  learning  models  (e.g.,  LSTM,
GRU,  CNN,  and  hybrid  CNN–LSTM)  excel  by  exploiting  high-resolution,  multivari-
ate  inputs.  In  data-limited  scenarios—such  as  sites  with  fewer  sensors  or  newly  com-
missioned  farms—tree-based  methods  (Random  Forest,  XGBoost)  and  SVMs  perform
better due to their lower data requirements and strong generalization from engineered
features.  For  ultra-short-term  forecasts  (< 30  min),  lightweight  ML  models  or  shallow
neural networks deliver fast, accurate results with minimal latency, making them ideal
for real-time control. LSTM and GRU models are more effective for short- to mid-term
forecasts (hours to days) by capturing temporal dependencies in NWP-driven datasets.
Long-term  forecasting  (months  to  years)  benefits  from  hybrid  approaches  that  com-
bine physical and statistical models with ML to address seasonal and climatic variability.

Haq et al. Discover Applied Sciences          (2025) 7:1139
Page 27 of 32

Table 10  Appropriateness of deep learning and machine learning models for various wind power
prediction situations
Scenario
Ultra-short-term, real-time
Short-term (hour-ahead)
Long-term, seasonal
Data-rich
Data-scarce

Most Suitable Models
XGBoost, RF, shallow ANN
LSTM, GRU
Hybrid ML–NWP, CNN-LSTM
Deep learning models
RF, XGBoost, SVM

Rationale
Fast inference, lower latency
Strong temporal modeling
Capture climatic/seasonal signals
Leverage high-volume, high-dimensional data
Perform well with fewer data, engineered
features
Manage variability, nonlinearity

Complex terrain

Low-resource deployment

Gradient boosting, hybrid
statistical–ML
RF, pruned/quantized DL

Resource-efficient operation

Geographic and climatic factors also influence suitability: CNN–LSTM and GRU mod-
els leverage the spatial-temporal stability of coastal/offshore sites, while gradient boost-
ing  and  hybrid  statistical–ML  approaches  better  manage  the  irregularity  of  complex
terrains.  For  locations  affected  by  climate  change,  adaptive  ML  and  transfer  learning
help minimize retraining as wind patterns evolve.

Computational  resources  guide  deployment  choices:  deep  learning  fits  well  in  high-
performance  cloud  or  HPC  environments,  whereas  low-cost  edge  devices  (e.g.,  Rasp-
berry Pi) favor Random Forest, XGBoost, or optimized TinyML models through pruning
and  quantization.  Finally,  where  interpretability  is  critical  for  operator  trust,  decision
trees  or  linear  models  are  preferable,  while  deep  architectures  require  explainable  AI
techniques  to  make  their  “black  box”  predictions  more  transparent.  Table  10  outlines
the  comparative  suitability  of  these  ML/DL  approaches  across  forecast  horizons,  data
scenarios, site conditions, computational limits, and interpretability needs.

7  Future research directions

Potential  research  directions  can  be  ranked  based  on  their  viability,  level  of  techno-
logical maturity, and anticipated time to implementation to direct future work in wind
power forecasting.

7.1  Short-term priorities (1–3 years)

These  research  directions  can  be  pursued  using  currently  available  methods,  datas-
ets,  and  computational  resources.  They  include  deploying  advanced  SCADA  systems,
nacelle  lidar,  and  low-cost  IoT  sensors  for  real-time  turbine  and  environmental  data
acquisition;  enhancing  data  preprocessing  pipelines  for  outlier  detection,  fault  diagno-
sis, and missing data imputation to ensure high-quality inputs; applying hybrid feature
selection  techniques  (e.g.,  Lasso  with  tree-based  ranking)  to  optimise  model  accuracy
and  efficiency;  developing  lightweight  ML/DL  models  through  pruning,  quantisation,
and TinyML for edge computing in remote wind farms; and conducting robustness test-
ing of models such as XGBoost and CNN–LSTM under high-frequency and incomplete
data scenarios to simulate operational challenges.

7.1.1  Knowledge gaps and research priorities for high-penetration renewable grids

The  rapid  global  shift  toward  high-penetration  renewable  energy  systems  introduces  a
unique  set  of  challenges  for  wind  power  forecasting.  While  many  advances  have  been

Haq et al. Discover Applied Sciences          (2025) 7:1139 Page 28 of 32

made in data-driven and hybrid modelling, several critical knowledge gaps remain that
must be addressed to ensure reliable integration of wind energy into future power grids:

7.1.1.1  Forecasting  under  extreme  variability  and  system  stress  Gap:  Limited  under-
standing  of  model  robustness  under  sudden  weather  transitions,  extreme  events,  and
rapid ramping scenarios in high-renewable grids.

Direction:  Research  into  resilient  forecasting  frameworks  that  leverage  ensemble
meteorological  models,  uncertainty  quantification,  and  adaptive  algorithms  capable  of
real-time recalibration.

7.1.1.2  Multi-energy  coupling  and  sector  coupling  forecasts  Gap:  Inadequate  models
for  integrated  forecasting  across  coupled  renewable  sources  (wind,  solar,  hydro)  when
penetration exceeds 60–70% of supply.

Direction:  Develop  multi-vector  energy  forecasting  systems  that  incorporate  cross-

resource correlations, storage states, and demand-side flexibility.

7.1.1.3  Sub-second  to  ultra-short-term  grid  support  forecasts  Gap:  Insufficient  atten-
tion to ultra-short-term (< 1 min) high-frequency forecasts needed to support inverter-
based resources, grid-forming converters, and synthetic inertia provision.

Direction: Investigate high-frequency hybrid ML–signal processing approaches using
phasor  measurement  units  (PMUs),  edge-AI  forecasting,  and  wide-area  measurement
data.

7.1.1.4  Geographically  distributed  and  edge-based  forecasting  Gap:  Sparse  research
on coordinating forecasts from geographically dispersed assets in real time, especially in
microgrids and distributed energy resource (DER) environments.

Direction:  Develop  federated  and  decentralized  learning  frameworks  that  integrate
site-specific forecasts without centralized data sharing, ensuring cybersecurity and data
privacy.

7.1.1.5  Explainability and trust in operational forecasts  Gap: Lack of interpretable fore-
casting tools to support operator confidence in automated dispatch decisions in renew-
able-rich grids.

Direction:  Advanced  explainable  AI  for  forecasting  with  visual  analytics,  attribu-
tion  methods,  and  uncertainty  bounds  tailored  to  transmission  operators  and  market
participants.

7.1.1.6  Climate adaptation in forecasting models  Gap: Forecasting methodologies often
assume stationarity, with limited accounting for the impacts of long-term climate change
on wind regimes.

Direction:  Integrate  climate  projections  and  regime-shift  detection  into  operational

forecasting pipelines.

7.2  Medium-term priorities (3–5 years)

Medium-term  priorities  (3–5  years)  involve  advancing  algorithms  and  integrat-
ing  diverse  modelling  strategies,  including  transformer-based  architectures  with

Haq et al. Discover Applied Sciences          (2025) 7:1139 Page 29 of 32

temporal and spatio-temporal attention for long-horizon, multi-scale forecasting; phys-
ics-informed neural networks (PINNs) and hybrid CFD–ML models that fuse numerical
weather  predictions  and  fluid  dynamics  with  ML/DL  for  better  generalisation  in  com-
plex  terrains;  multi-energy  hybrid  forecasting  frameworks  for  jointly  modelling  wind,
solar, storage, and demand to optimise grid operations; domain adaptation and transfer
learning to quickly customise pre-trained models for new sites or extreme weather with
minimal local data; and uncertainty quantification via probabilistic and ensemble meth-
ods to generate prediction intervals for market bidding and grid risk management.

7.3  Long-term priorities (5 + years)

Long-term  priorities  (5 + years)  target  transformational  impacts  through  large-scale
collaboration and advanced infrastructure, including fully integrated renewable energy
forecasting ecosystems that unify AI-driven multi-energy generation, demand, storage,
and market forecasting; federated and privacy-preserving collaborative learning to share
model  insights  without  exposing  sensitive  data;  climate  change-adaptive  forecasting
that incorporates climate projections to maintain accuracy amid long-term wind regime
shifts;  autonomous  grid  balancing  systems  that  couple  real-time  forecasts  with  auto-
matic corrective actions; and digital twins for wind farms that integrate live forecasting,
asset health prediction, and maintenance optimisation.

By  structuring  research  opportunities  in  this  time-horizon  framework,  stakeholders
can align investment and development roadmaps, ensuring that immediate operational
gains are realised while paving the way for medium- and long-term innovation.

8  Conclusions

This  review  synthesises  machine  learning  approaches  for  wind  power  forecasting,
encompassing traditional ML, deep learning, ensemble, and hybrid models, along with
data  handling,  optimisation,  and  evaluation  metrics.  Innovations  include  a  category-
based  model  classification,  quantified  impacts  of  data  preprocessing,  systematic  algo-
rithm  comparisons,  and  coverage  of  special  scenarios  such  as  extreme  weather  and
complex  terrain.  Limitations  involve  reliance  on  existing  literature,  absence  of  unified
benchmarks, and limited discussion of hardware and economic factors. Future research
should  explore  transformer-based  models,  multi-energy  hybrid  forecasting,  spatio-
temporal  GNNs,  transfer  learning,  and  deployment-friendly  lightweight  architectures.
By outlining both current advances and research needs, this work offers a roadmap for
more accurate, robust, and operationally integrated wind power forecasting.

Abbreviations
ANN
ARIMA
BO
CNN
CFD
DTR
ESS
FOA
GBM
GRU
IoT
Lasso
LR
LSTM
MAE

 Artificial neural network
 Auto regressive integrated moving average
 Bayesian optimization
 Convolutional neural network
 Computational fluid dynamics
 Decision tree regression
 Energy storage system
 Fruit fly algorithm
 Gradient boosting machine
 Gated recurrent unit
 Internet of Things
 Least Absolute Shrinkage and Selection Operator
 Linear regression
 Long short-term memory
 Mean absolute error

Haq et al. Discover Applied Sciences          (2025) 7:1139 Page 30 of 32

MAPE

 Mean absolute percentage error

Author contributions
Inam Ul Haq conducted the overall work, wrote the manuscript including drafting and implementation. Abhishek Kumar
carried out the supervision and final review. Pramod Singh Rathore carried out the co-supervision and drafting the
literature.

Funding
Open access funding provided by Manipal University Jaipur. Manipal University Jaipur.

Data availability
No datasets were generated or analysed during the current study.

Declarations

Ethics approval and and Consent to Participate
Not applicable

Consent for publication
Not applicable.

Competing interests
The authors declare no competing interests.

Received: 8 July 2025 / Accepted: 25 August 2025

References
1.

Tascikaraoglu A, Uzunoglu M. A review of combined approaches for prediction of short-term wind speed and power.
Renew Sustain Energy Rev. 2014;34:243–54.
.Colak I, Sagiroglu S, Yesilbudak M. Data mining and wind power prediction: a literature review. Renew Energy.
2012;46:241–7.
Foley AM, Leahy PG, Marvuglia A, McKeogh EJ. Current methods and advances in forecasting of wind power generation.
Renew Energy. 2012;37(1):1–8.
Catala˜o JDS, Pousinho HMI, Mendes VMF. Short-term wind power forecasting in Portugal by neural networks and wavelet
transform. Renew Energy. 2011;36(4):1245–51.

2.

3.

4.

5.  Du P, Wang J, Yang W, Niu T. A novel hybrid model for short-term wind power forecasting. Appl Soft Comput.

6.

2019;80:93–106.
Jahangir L, Babbar S. (2020) Medium term wind speed using random forest algorithm. Int Res J Comput Sci Technol, pp
47–53.

7.  Wu GZ, Zhang YB, Su C, Liu YJ. Study on medium-term and short-term wind power forecasting methods. Appl Mech

8.

Mater. 2013;361:318–22.
Sankar S, Amudha S, Madhavan P, Lamba DK. (2021) Energy efficient medium-term wind speed prediction system using
machine learning Models. In: IOP Conference Series: Materials Science and Engineering, vol. 1130. IOP Publishing, p
012085.

9.  Ouyang T, Huang H, He Y. Ramp events forecasting based on long-term wind power prediction and correction. IET Renew

Power Gener. 2019;13(15):2793–801.

10.  Colak I, Sagiroglu S, Yesilbudak M, Kabalci E, Bulbul HI. (2015) Multi-time series and-time scale modeling for wind speed
and wind power forecasting part II: Medium-term and long-term applications. In: 2015 International Conference on
Renewable Energy Research and Applications (ICRERA), IEEE, pp. 215–220.

11.  Azad HB, Mekhilef S, Ganapathy VG. Long-term wind speed forecasting and general pattern recognition using neural

networks. IEEE Trans Sustain Energy. 2014;5(2):546–53.

12.  Borunda M, Rodrı´guez-Va´zquez K, Garduno-Ramirez R, de la Cruz-Soto J, Antunez-Estrada J, Jaramillo OA. Long-term

Estimation of wind power by probabilistic forecast using genetic programming. Energies. 2020;13(8):1885.

13.  Feng C, Cui M, Hodge BM, Zhang J. A data-driven multimodel methodology with deep feature selection for short-term

wind forecasting. Appl Energy. 2017;190:1245–57.

14.  Landberg L. Short-term prediction of the power production from wind farms. J Wind Eng Ind Aerodyn.

1999;80(1–2):207–20.

15.  Lei M, Shiyan L, Chuanwen J, Hongling L, Yan Z. A review on the forecasting of wind speed and generated power. Renew

Sustain Energy Rev. 2009;13(4):915–20.

16.  Andrade JR, Bessa RJ. Improving renewable energy forecasting with a grid of numerical weather predictions. IEEE Trans

Sustain Energy. 2017;8(4):1571–80.

17.  Ramirez-Rosado IJ, Fernandez-Jimenez LA, Monteiro C, Sousa J, Bessa R. Comparison of two new short-term windpower

forecasting systems. Renew Energy. 2009;34(7):1848–54.

18.  Hill DC, McMillan D, Bell KR, Infield D. Application of auto-regressive models to UK wind speed data for power system

impact studies. IEEE Trans Sustain Energy. 2011;3(1):134–41.

19.  Dowell J, Pinson P. Very-short-term probabilistic wind power forecasts by sparse vector autoregression. IEEE Trans Smart

Grid. 2015;7(2):763–70.

20.  Flores JJ, Graff M, Rodriguez H. Evolutive design of ARMA and ANN models for time series forecasting. Renew Energy.

2012;44:225–30.

Haq et al. Discover Applied Sciences          (2025) 7:1139 Page 31 of 32

21.  Yuan C, Liu S, Fang Z. Comparison of china’s primary energy consumption forecasting by using ARIMA (the autoregressive

integrated moving average) model and GM (1, 1) model. Energy. 2016;100:384–90.

22.  Batsaikhan N, Song S. Real-time wind power prediction using distributed computing and machine learning. Wind Energy

Sci. 2023;5:885–96.

23.  Liu S, Zhang Y, Du X, Xu T, Wu J. Short-term power prediction of wind turbine applying machine learning and digital filter.

Appl Sci. 2023;13:1751.

24.  Taheri N, Tucci M. Enhancing regional wind power forecasting through advanced machine-learning and feature-selection

techniques. Energies. 2024;17:5431.

25.  Alkabbani H, Hourfar F, Ahmadian A, Zhu Q, Almansoori A, Elkamel A. Machine learning-based time series modelling for

large-scale regional wind power forecasting: A case study in Ontario. Can Clean Energy Syst. 2023;5:100068.

26.  Gao X. Monthly wind power forecasting: integrated model based on grey model and machine learning. Volume 14.

Sustainability; 2022. p. 15403.

27.  Hao C, Yngve B, Bjørn-Morten B, Abbas B. Noise-intensification data augmented machine learning for day-ahead wind

power forecast. Energy Rep. 2022;8:916–22.

28.  Alexander M, Gregor B. Demystifying the use of ERA5-land and machine learning for wind power forecasting. IET Renew

Power Gener. 2020;14:4159–68.

29.  Aizpurua JI, Peña-Alzola R, Olano J, Ramirez I, Lasa I, del Rio L, Dragicevic T. Probabilistic machine learning aided trans-
former lifetime prediction framework for wind energy systems. Int J Electr Power Energy Syst. 2023;153:109352.

30.  Liu S, Zhang Y, Du X, Xu T, Wu J. Short-term power prediction of wind turbine applying machine learning and digital filter.

Appl Sci. 2023;13:1751. [CrossRef ].

31.  He R, Yang H, Sun S, Lu L, Sun H, Gao X. A machine learning-based fatigue loads and power prediction method for wind

turbines under Yaw control. Appl Energy. 2022;326:120013.

32.  Sasser C, Yu M, Delgado R. Improvement of wind power prediction from meteorological characterization with machine

learning models. Renew Energy. 2022;183:491–501.

33.  Ye F, Ezzat AA. Icing detection and prediction for wind turbines using multivariate sensor data and machine learning.

Renew Energy. 2024;231:120879.

34.  Singh U, Rizwan M. SCADA system dataset exploration and machine learning based forecast for wind turbines. Results

Eng. 2022;16:100640.

35.  Chen H, Birkelund Y, Yuan F. Examination of turbulence impacts on ultra-short-term wind power and speed forecasts with

machine learning. Energy Rep. 2021;7:332–8.

36.  Yao F, Liu W, Zhao X, Song L. Integrated machine learning and enhanced statistical approach-based wind power forecast-

ing in australian tasmania wind farm. Complexity 2020, 2020, 9250937.

37.  Hua K, Mishra Y, Ledwich G. Fast unscented transformation-based transient stability margin Estimation incorporating

uncertainty of wind generation. IEEE Trans Sustain Energy. 2015;6(4):1254–62.

38.  Bludszuweit H, Domı´nguez-Navarro JA, Llombart A. Statistical analysis of wind power forecast error. IEEE Trans Power Syst.

39.

2008;23(3):983–91.
Jiang P, Liu Z, Niu X, Zhang L. A combined forecasting system based on statistical method, artificial neural networks, and
deep learning methods for short-term wind speed forecasting. Energy. 2021;217:119361.

40.  Chitsazan MA, Fadali MS, Trzynadlowski AM. Wind speed and wind direction forecasting using echo state network with

nonlinear functions. Renewable Energy. 2019;131:879–89.

41.  Karabacak K, Cetin N. Artificial neural networks for controlling wind-PV power systems: A review. Renew Sustain Energy

Rev. 2014;29:804–27.

42.  Wan C, Xu Z, Pinson P, Dong ZY, Wong KP. Probabilistic forecasting of wind power generation using extreme learning

machine. IEEE Trans Power Syst. 2013;29(3):1033–44.

43.  Sun W, Wang Y. Short-term wind speed forecasting based on fast ensemble empirical mode decomposition, phase space
reconstruction, sample entropy and improved back-propagation neural network. Energy Convers Manage. 2018;157:1–12.

44.  Hong YY, Rioflorido CLPP. A hybrid deep learningbased neural network for 24-h ahead wind power forecasting. Appl

Energy. 2019;250:530–9.

45.  Liu Y, Qin H, Zhang Z, Pei S, Jiang Z, Feng Z, Singh P, Dwivedi P et al. (2018) Integration of new evolutionary approach with

artificial neural network for solving short term load forecast problem. Appl Energy 217:537–549.

46.  Wang S. An interview with Shouyang wang: research frontier of big data-driven economic and financial forecasting. Data

47.

Sci Manag. 2021;1(1):10–2.
Jin M, Wen Q, Liang Y, Zhang C, Xue S, Wang X et al. (2023) Large models for time series and spatio-temporal data: A
survey and outlook. arXiv:2310.10196.

48.  Wang Y, Yu Y, Cao S, Zhang X, Gao S. A review of applications of artificial intelligent algorithms in wind farms. Artif Intell

Rev. 2020;53:3447–500.

49.  Hanifi S, Liu X, Lin Z, Lotfian S. A critical review of wind power forecasting methods-past, present and future. Energies.

2020;13(15):3764.

50.  Lu P, Ye L, Zhao Y, Dai B, Pei M, Tang Y. Review of meta-heuristic algorithms for wind power prediction: methodologies,

applications and challenges. Appl Energy. 2021;301:117446.

51.  Qian Z, Pei Y, Zareipour H, Chen N. A review and discussion of decomposition-based hybrid models for wind energy

forecasting applications. Appl Energy. 2019;235:939–53.

52.  Bokde N, Feijo´o A, Villanueva D, Kulat K. A review on hybrid empirical mode decomposition models for wind speed and

wind power prediction. Energies. 2019;12(2):254.

53.  Wang Y, Zou R, Liu F, Zhang L, Liu Q. A review of wind speed and wind power forecasting with deep neural networks. Appl

Energy. 2021;304:117766.

54.  Tc F, Ouyang T, Huang H, He Y, Tang Z. (2020) Chaotic wind power time series prediction via switching data-driven modes.

Renew Energy 145:270–281.

55.  Wang Y, Xiong W, Liu Q, Yang N, Fu P, Gong K, et al. Wind power prediction based on a hybrid granular chaotic time series

model. Front Energy Res. 2022;9:1023.

56.  Bhaskar K, Singh SN. AWNN-assisted wind power forecasting using feed-forward neural network. IEEE Trans Sustain

Energy. 2012;3(2):306–15.

Haq et al. Discover Applied Sciences          (2025) 7:1139 Page 32 of 32

57.  Oso´rio G, Matias J, Catala˜o J. Short-term wind power forecasting using adaptive neuro-fuzzy inference system combined
with evolutionary particle swarm optimization, wavelet transform and mutual information. Renew Energy. 2015;75:301–7.

58.  Wang H, Lei Z, Liu Y, Peng J, Liu J. Echo state network based ensemble approach for wind power forecasting. Energy

Convers Manage. 2019;201:112188.

59.  Wang C, Zhang H, Fan W, Ma P. A new chaotic time series hybrid prediction method of wind power based on EEMDSE and

full-parameters continued fraction. Energy. 2017;138:977–90.

60.  Li Z, Luo X, Liu M, Cao X, Du S, Sun H. Wind power prediction based on EEMD-Tent-SSA-LS-SVM. Energy Rep.

2022;8:3234–43.

61.  Zhang C, Ding M, Wang W, Bi R, Miao L, Yu H, et al. An improved ELM model based on CEEMD-LZC and manifold learning

for short-term wind power prediction. IEEE Access. 2019;7:121472–81.

62.  Naik J, Bisoi R, Dash P. Prediction interval forecasting of wind speed and wind power using modes decomposition based

low rank multi-kernel ridge regression. Renew Energy. 2018;129:357–83.

63.  Ding J, Chen G, Yuan K. Short-term wind power prediction based on improved grey Wolf optimization algorithm for

extreme learning machine. Processes. 2020;8(1):109.

64.  Wu J, Ji T, Li M, Wu P, Wu Q. Multistep wind power forecast using mean trend detector and mathematical morphology-

based local predictor. IEEE Trans Sustain Energy. 2015;6(4):1216–23.

65.  Lu P, Ye L, Sun B, Zhang C, Zhao Y, Teng J. A new hybrid prediction method of ultra-short-term wind power forecasting

based on EEMD-PE and LSSVM optimized by the GSA. Energies. 2018;11(4):697.

66.  Zhao Y, Ye L, Li Z, Song X, Lang Y, Su J, Vapnik V. (1995) Support-vector networks. Mach Learn 20:273–297.
67.  Zendehboudi A, Baseer MA, Saidur R. Application of support vector machine models for forecasting solar and wind

energy resources: A review. J Clean Prod. 2018;199:272–85.

68.  Wang Y, Wang D, Tang Y. Clustered hybrid wind power prediction model based on ARMA, PSO-SVM, and clustering meth-

ods. IEEE Access. 2020;8:17071–9.

69.  Özüpak Y, Mansurov S. Optimizing electricity demand forecasting with a novel RNN-LSTM hybrid model. Energy Sources

Part B: Econ Plann Policy. 2025;20(1).  h t t p s :  / / d o i  . o r g / 1  0 . 1 0  8 0 / 1 5  5 6 7 2 4  9 . 2 0 2 5  . 2 5 3  1 4 4 8.

70.  Aslan E, Özüpak Y, Alpsalaz F, Elbarbary ZMS. A Hybrid Machine Learning Approach for Predicting Power Transformer
Failures Using Internet of Things-Based Monitoring and Explainable Artificial Intelligence, in IEEE Access, vol. 13, pp.
113618–113633, 2025, https://doi.org/10.1109/ACCESS.2025.3583773

71.  Liu, S., Zhang, L., Lu, J., Zhang, X., Wang, K., Gan, Z., … Wang, H. (2025). Advances in urban wind resource development and

wind energy harvesters. Renewable and Sustainable Energy Reviews, 207, 114943.

Publisher’s note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Haq et al. Discover Applied Sciences          (2025) 7:1139