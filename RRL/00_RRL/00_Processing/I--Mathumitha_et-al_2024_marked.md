Artificial Intelligence Review (2024) 57:35
https://doi.org/10.1007/s10462-023-10660-8

Intelligent deep learning techniques for energy consumption
forecasting in smart buildings: a review

R. Mathumitha1 · P. Rathika1 · K. Manimala2

Accepted: 19 December 2023 / Published online: 5 February 2024
© The Author(s) 2024

Abstract
Urbanization increases electricity demand due to population growth and economic activ-
ity. To meet consumer’s demands at all times, it is necessary to predict the future build-
ing energy consumption. Power Engineers could exploit the enormous amount of energy-
related  data  from  smart  meters  to  plan  power  sector  expansion.  Researchers  have  made
many experiments to address the supply and demand imbalance by accurately predicting
the  energy  consumption.  This  paper  presents  a  comprehensive  literature  review  of  fore-
casting  methodologies  used  by  researchers  for  energy  consumption  in  smart  buildings  to
meet future energy requirements. Different forecasting methods are being explored in both
residential  and  non-residential  buildings.  The  literature  is  further  analyzed  based  on  the
dataset, types of load, prediction accuracy, and the evaluation metrics used. This work also
focuses on the main challenges in energy forecasting due to load fluctuation, variability in
weather, occupant behavior, and grid planning. The identified research gaps and the suit-
able  methodology  for  prediction  addressing  the  current  issues  are  presented  with  refer-
ence  to  the  available  literature.  The  multivariate  analysis  in  the  suggested  hybrid  model
ensures the learning of repeating patterns and features in the data to enhance the prediction
accuracy.

Keywords  Energy consumption · Deep learning · Smart meter · Energy forecasting · Smart
building

 *  R. Mathumitha
  mathuramesh25@gmail.com

P. Rathika
rathikaponpandi@gmail.com

K. Manimala
smonimala@gmail.com

1  Department of Electronics and Communication Engineering, PSN College of Engineering

and Technology, Tirunelveli, India

2  Department of Information Science and Technology, College of Engineering, Guindy, Anna

University, Chennai, India

Vol.:(0123456789)1 3

35  Page 2 of 33

1  Introduction

R. Mathumitha et al.

Due  to  the  ongoing  advancement  of  urbanization,  there  has  been  an  increase  in  energy
consumption during the past few decades (Bhosale and Gadekar 2014). 40% of the world’s
electrical energy is consumed by the building sector. The generation of electricity is closely
related to the emission of carbon dioxide  (CO2) due to the predominant use of fossil fuels
in  many  electricity  generation  processes.  Fossil  fuel-based  power  plants,  such  as  those
fueled  by  coal,  oil,  and  natural  gas,  release  significant  amounts  of   CO2  into  the  atmos-
phere when these fuels are burned to produce electricity. Electricity generation produces
CO2 emissions that lead to the greenhouse effect, which traps heat in the atmosphere and
causes a climatic change on a worldwide scale. The more electricity generated from fos-
sil  fuel  sources,  the  higher  the  associated   CO2  emissions.  Burning  fossil  fuels  for  power
generation accounts for over 40% of energy-related CO2 emissions. Therefore, predicting
building energy consumption has gained the utmost importance in tackling the swift rise
of CO2 emissions. Furthermore, this capability empowers power engineers to resolve the
supply and demand gap. Also, this helps to render proficient and impactful choices while
designing, constructing, and operating building structures (Dong et al. 2018). This can be
achieved by improving the overall performance of energy prediction in buildings (Zhang
et  al.  2020a).  A  minimal  improvement  in  forecast  accuracy  can  also  result  in  savings  of
millions  of  rupees  (Zor  et  al.  2020).  Hence,  accurate  load  forecasts  are  also  driven  by  a
significant incentive related to economic motivation (Xu et al. 2019). Numerous method-
ologies  and  computational  techniques  have  been  developed  to  increase  forecast  accuracy
(Agyeman et al. 2020).

The energy forecasting horizon is usually classified by time horizon into three catego-
ries:  long-term  (more  than  a  year),  mid-term  (from  a  month  to  a  year),  and  short-term
(from one day to a month) forecasting (Kiprijanovska et al. 2020; Liu et al. 2020). Fore-
casting  methods  can  be  classified  as  supervised  learning  (neural  network  models  such
as  support  vector  machines  and  classifiers  (Das  et  al.  2020),  extreme  learning  machines
(ELM;  Fu  2018),  random  forests  (Wang  and  Srinivasan  2017),  and  DL  algorithms)  and
unsupervised  learning  (a  variety  of  clustering  algorithms  such  as  k-means  clustering
(Singh  and  Dwivedi  2018),  fuzzy  clustering  (Cheng  and  Li  2008),  and  other  improved
clustering  methods).  The  choice  of  forecasting  method  depends  on  the  forecasting  hori-
zon,  which  refers  to  the  period  for  which  predictions  are  made.  Short-term  forecasting
often uses methods like autoregressive integrated moving average (ARIMA; Farzana et al.
2014),  exponential  smoothing  (Liu  et  al.  2016),  or  recurrent  neural  networks  (RNNs).
Medium-term forecasting may employ seasonal ARIMA, state space models, or machine
learning algorithms. Long-term forecasting (years or more) relies on trend extrapolation,
econometric  models,  or  causal  models.  However,  the  selection  should  also  consider  data
availability, quality, underlying assumptions, and specific problem characteristics. Combi-
nations and overlaps of methods can occur based on the forecasting task. The literature has
extensive research on predicting energy usage for both commercial and residential build-
ings.  Recently,  several  academics  have  concentrated  on  enhancing  the  effectiveness  and
accuracy  of  electricity  consumption  forecasts  using  deep  learning  architectures  (Bandic
and  Kevric  2018;  Munkhdalai  and  Munkhdalai  2019).  Most  of  the  research  community
uses  deep  learning-based  techniques  because  of  their  excellent  results  on  unsupervised
problems.  DL  is  a  complex  computational  model  designed  with  multiple  hidden  layers
that use features as input to represent data with different abstractions. DL algorithms are
used for various learning tasks, especially unsupervised learning. Load forecasting is one

1 3
Page 3 of 33  35

application  that  has  benefited  from  DL  algorithms  in  many  kinds  of  literature.  Recently,
RNNs and convolution neural networks (CNNs) are two powerful architectures proposed in
the literature for the analysis of time series data. For instance, a study presented in Mocanu
et al. 2016 proposed a deep CNN network for day-ahead load forecasting and compared the
results with an (ELM), ARIMA, CNN, and RNN. Several studies also used RNN models
for electricity load prediction, whereas in paper (Ali et al. 2016) used RNN, gated recurrent
unit (GRU), and long-short term memory (LSTM) models for electricity load prediction in
Turkey and extensively decreased the error. The electricity consumption data is time-series
data,  which  comprises  spatial  and  temporal  information.  The  CNN  models  perform  well
for spatial information extraction but are insufficient for temporal information, whereas the
RNN  models  are  insufficient  for  spatial  information  and  can  learn  temporal  information.
Therefore, to develop an optimal model for electricity load prediction, hybrid models are
introduced in the recent literature.

For instance, another study (Kolehmainen et al. 2015) developed a hybrid model com-
bining  CNN  with  LSTM  for  short-term  load  prediction  and  compared  their  results  with
GRU,  attention  LSTM,  LSTM,  and  bidirectional  LSTM.  In  the  paper  (Manembu  et  al.
2018),  they  also  developed  a  hybrid  model  with  a  combination  of  CNN  and  multi-layer
bidirectional  LSTM  and  compared  their  results  with  bidirectional  LSTM,  LSTM,  and
CNN-LSTM. Similarly, another study presented in Choksi et al. (2020) integrated a CNN
with  an  LSTM  auto-encoder  and  compared  the  final  results  with  LSTM,  LSTM  autoen-
coder, and CNN-LSTM. Moreover, studies (Jain et al. 2019; Singh and Yassine 2019) pre-
sented  the  performance  of  a  CNN-GRU  based  model  for  electricity  forecasting.  A  study
(Pirbazari and Sharma 2021) describes solar power forecasting in addition to load forecast-
ing which uses the CNN-LSTM hybrid model with the help of climatic scenarios, and dur-
ing experimental analysis, they have classified the error based on sunny days, and cloudy
days.  In  recent  years,  hybrid  CNN  with  CNN-ESN  (echo  state  network)  and  LSTM-AE
(autoencoder) have the potential to enhance the overall efficiency of the existing forecast-
ing models. In a paper (Khan et al. 2020), they proposed a hybrid CNN with the LSTM-AE
model.  A  CNN  model  extracts  features  from  the  input  data,  which  are  fed  to  an  LSTM
encoder  to  produce  an  encoded  sequence.  The  encoded  sequence  is  decoded  by  another
subsequent  LSTM  decoder  and  forwarded  to  the  final  dense  layer  for  energy  prediction.
In  the  paper  (Liu  et  al.  2022),  the  author  proposed  the  temporal  convolutional  network
model (TCN) architecture and proved with better accuracy than LSTM. Most of the fore-
casting methods are designed to forecast a single or small group of time series. However,
in  the  paper  (Rick  and  Berton  2020),  the  author  focused  on  short-term  forecasting  over
many time series of unequal lengths. The author (Rick and Berton 2020) proposed a deep
learning  approach  based  on  LSTM,  CNN,  and  auto-encoder  for  training  only  one  model
for the many time series. Compared to TCN, they achieved a smaller error rate. The author
suggests  a  hybrid  combination  technique,  called  CESN,  based  on  a  deep  learning  model
combining Convolutional Neural Networks and Echo State Networks, to produce a high-
quality prediction of power consumption (Ghimire et al. 2023). Peak handling is another
difficult area for researchers in load predictions. The occurrences of the peaks are irregular,
and  their  time  of  occurrence  cannot  be  determined  apriori  because  the  customer’s  con-
sumption behavior is uncertain. This poses a challenge in modeling peaks as there is only
a minimal dependency of present consumption on its past data. Thus the peaks have to be
modeled precisely. The available state-of-the-art techniques (Gao et al. 2012) are not able
to make accurate predictions at peak load conditions as machine learning (ML) algorithms
poorly predict peak for hourly mean load prediction. In the paper (Sulaiman et al. 2022),
the author proposed a novel hybrid method based on EMD (extreme mode decomposition)

Intelligent deep learning techniques for energy consumption…1 335  Page 4 of 33

R. Mathumitha et al.

with  ELM  to  handle  peak  residential  loads.  In  the  paper  (Imani  and  Ghassemian  2019),
wavelet decomposition is applied to remove redundant values. In addition, a collaborative
representation is introduced including information on the neighboring points (previous and
future time instances) of the considered load point. Hybrid models exploited well in other
fields like the finance sector to predict stock market trends are not explored that much in
power consumption forecasting. The finance sector benefits from combining LSTM models
with Generative Adversarial Networks (GANs; Zhang, et al. 2015; Polamuri et al. 2022) to
predict stock market trends. Such hybrid models can be applied to capture the stochastic
nature of power consumption data and to generate synthetic datasets for augmentation. The
performance of the hybrid model is very promising, reaching the highest level of accuracy.
However, the best prediction of the electricity load needs further improvement by choosing
an appropriate method.

The main contributions of this paper are:

•  Literature review of the previous research works for energy consumption forecasting in

smart buildings, exploring their contribution and inference

•  Detailed framework for power forecasting
•  Analysis of the various methodologies used in the forecasting of energy consumption

in buildings from various perspectives, their findings, and limitations

•  A research gap in the existing literature is identified and suggestions are given for the

new researchers working in this area

  The  remainder  of  the  paper  is  organized  in  the  following  way.  Section  2  discusses  the
common framework for power forecasting, In Sect. 3, different DL algorithm is discussed
based  on  energy  consumption  forecasting  Then  the  paper  is  followed  by  Sects.  4  and  5.
Section 4 briefly discusses about application of DL using forecasting horizon and Sect. 5
discusses evaluation metrics. Section 6 describes a detailed discussion of energy forecast-
ing methodologies. Finally, the paper concludes with the identification of the research gap
in Sect. 7 and concludes in Sect. 8.

2   Inference from literature

The  literature  survey  has  provided  valuable  insights  into  the  field  of  energy  consump-
tion forecasting in smart buildings. The diverse body of research underscores several key
trends and perspectives that significantly contribute to this critical domain. Power forecast-
ing needs to analyze large amounts of historical power data, especially for high-resolution
forecasting.  Different  ML  techniques  have  been  applied  for  predicting  future  electricity
consumption  for  a  more  ideal  solution,  which  lacks  in  handling  large  datasets.  This  gap
is filled by DL based techniques because they can handle and learn from massive datasets
more  efficiently  than  traditional  ML  models  First  and  foremost,  data-driven  approaches
have  emerged  as  a  fundamental  pillar  in  energy  consumption  forecasting.  Leveraging
advanced machine learning, deep learning, and data analytics techniques, harness histori-
cal  data,  weather  information,  occupancy  patterns,  and  other  relevant  variables  to  create
accurate forecasts, offering a promising avenue for improving energy management in smart
buildings.

Previous  research  in  energy  consumption  forecasting  for  smart  buildings  has
revealed several notable trends and unique perspectives. Consumers are now becoming

1 3
Page 5 of 33  35

prosumers, who not only consume electricity but also generate it, often through renew-
able  energy  sources  like  solar  panels,  wind  turbines,  or  small-scale  hydroelectric  sys-
tems.  Prosumers  are  essentially  consumers  who  become  self-sufficient  energy  produc-
ers, and they may feed surplus energy back into the grid. While the literature primarily
focuses  on  load  forecasting,  recent  trends  in  renewable  energy  forecasting  should  be
considered. The integration of renewable energy sources, such as solar and wind power,
into  the  energy  grid  requires  accurate  forecasting  to  ensure  grid  stability  and  efficient
energy management. Accurate forecasting is crucial for optimizing energy storage sys-
tems, which play a key role in grid integration of renewables and in managing demand
spikes, such as during peak loads. Peak load prediction remains a challenge, and most
machine  learning  algorithms  struggle  to  provide  accurate  forecasts  for  peak  consump-
tion.  Improving  peak  load  prediction  is  crucial  for  efficient  grid  management.  The  lit-
erature  suggests  the  potential  of  hybrid  methods,  such  as  combining  EMD  with  ELM,
wavelet  decomposition,  and  collaborative  representation,  to  enhance  the  accuracy  of
residential load forecasting.

3   Basic forecasting framework

Predicting power consumption is critical for smart grids to manage and conserve energy,
avoid waste, and use it efficiently. Due to the influence of numerous unpredictable situ-
ations  or  the  noisy  disordering  of  smart  meter  data,  it  is  difficult  to  anticipate  power
usage  accurately,  and  the  methods  employed  can  sometimes  yield  inaccurate  results.
Moreover, various techniques based on conventional networks have been developed, but
they cannot predict energy demand efficiently (Cai et al. 2019). Conventional networks
have problems related to short-term memory and learning from scratch. These problems
are easily solved using LSTM, a special type of RNN that has attracted a lot of attention
in  the  field  of  deep  learning.  LSTM  networks  have  a  unique  architecture  that  includes
memory cells and gates. The memory cells allow the network to store and retain infor-
mation over longer sequences, enabling the model to capture and learn from long-term
dependencies in the data. The common schematic diagram used for forecasting power is
shown in Fig. 1.

Fig. 1   Basic block diagram for forecasting power

Intelligent deep learning techniques for energy consumption…1 335  Page 6 of 33

3.1   Smart meter data

R. Mathumitha et al.

The  first  step  is  to  collect  smart  meter  data.  Smart  meters  collect  a  huge  range  of  data
related  to  power  consumption  and  weather  data.  It  typically  requires  separate  weather
monitoring  equipment  or  accessing  weather  data  from  weather  stations  (Makonin  2019).
Weather data includes various parameters such as temperature, humidity, wind speed, and
wind speed precipitation. It records data with a timestamp, allowing for real-time monitor-
ing and historical analysis. Hence, the smart meter data becomes time series data (Le and
Vo 2020). The specific data collected can vary based on the utility’s requirements and the
capabilities  of  the  smart  meter.  It’s  important  to  note  that  smart  meters  provide  valuable
insights for consumers and utilities. Privacy and security issues must be considered to pro-
tect sensitive information and ensure responsible data usage.

3.2   Smart meter configuration

Smart  meters  are  advanced  digital  devices  used  to  measure  and  record  electricity  usage
in  residential,  commercial,  and  industrial  environments.  Unlike  traditional  meters,  smart
meters  provide  two-way  communication  between  utilities  and  consumers.  They  can  send
data  back  to  the  utility  company  in  real  time,  which  enables  better  monitoring,  manage-
ment, and optimization of energy usage. Designing a smart meter for building energy con-
sumption forecasting involves several key considerations to ensure accurate data collection,
communication,  and  compatibility  with  forecasting  algorithms.  The  outline  of  the  smart
meter design is depicted in Fig. 2. Here’s a conceptual outline of how a smart meter can
be  designed  to  support  energy  consumption  forecasting  (https:  www. elect ronics- notes.
com/articles/eco-green-engineering/smart-energy-meters/smart-meter-electronic-circuit-
design.php):

3.2.1   Data collection

•  High-Frequency  Data:  The  smart  meter  should  be  capable  of  collecting  energy  con-
sumption  data  at  regular  intervals  (e.g.,  every  15  min  or  hourly)  to  capture  detailed
consumption patterns.

•  Timestamps: Each data point should be associated with a timestamp, enabling chrono-

logical analysis and forecasting.

Fig. 2   Design of Smart meter for building energy consumption forecasting

1 3
Page 7 of 33  35

•  Granular Data: The meter should record various consumption parameters such as active

power, reactive power, voltage, and current.

3.2.2   Communication

•  Two-Way  Communication:  Implement  bidirectional  communication  capabilities  to

allow data transmission to utility companies and receipt of signals or commands.

•  Data  Transmission:  Use  wired  or  wireless  communication  protocols  (e.g.,  cellular,

Wi-Fi, Zigbee) to transmit collected data to central servers or cloud platforms.

3.2.3   Data storage and logging

•  Local Storage: Incorporate local storage to buffer and log data in case of communica-

tion disruptions, ensuring no data loss.

•  Data Logging: Store consumption data along with timestamps in a structured format for

easy retrieval and analysis.

3.2.4   Data quality and accuracy

•  Calibration: Calibrate the smart meter to ensure accurate energy readings and minimize

measurement errors.

•  Quality  Control:  Implement  mechanisms  to  monitor  and  ensure  data  accuracy  over

time. Regular maintenance and calibration checks are essential.

3.2.5   Security and privacy

•  Data Encryption: Encrypt collected data to ensure its security during transmission and

storage.

•  Anonymization:  Protect  consumer  privacy  by  anonymizing  data  before  analysis,  and

removing personally identifiable information.

3.2.6   Compatibility

•  Open  Standards:  Design  the  smart  meter  to  adhere  to  open  communication  protocols

and standards to ensure interoperability with utility systems.

•  Integration:  Ensure  compatibility  with  utility  company  systems  and  energy  manage-

ment platforms to facilitate data integration and usage.

3.2.7   Remote management and updates

•  Remote  Configuration:  Allow  for  remote  configuration  and  parameter  adjustments  to

adapt to changing requirements.

•  Firmware  Updates:  Design  the  smart  meter  to  receive  firmware  updates  remotely  to

improve functionality and security (Munoz and Ruelas 2022).

Intelligent deep learning techniques for energy consumption…1 335  Page 8 of 33

R. Mathumitha et al.

3.2.8   Data analysis and forecasting support

•  Data Preprocessing: Include capabilities for data preprocessing, such as filtering out

noise and handling missing data.

•  Integration with Forecasting Algorithms: Enable integration with energy consump-
tion forecasting algorithms, whether based on time series analysis, deep learning, or
statistical methods.

3.2.9   User interfaces

•  Display  and  User  Interface:  Provide  an  intuitive  display  that  shows  real-time  con-
sumption data to users for energy awareness and management. For integration with
the forecasting algorithm, the is retrieved in Excel or notepad form.

•  Interfaces for Utilities: Implement interfaces that utilities can use to retrieve histori-

cal and real-time consumption data (Jaiswal and Thakre 2022).

3.2.10   Scalability and future‑proofing

•  Scalability: Design the smart meter to handle large volumes of data as the number of

smart meters in deployment increases.

•  Future  Upgrades:  Plan  for  potential  enhancements  in  communication  technologies

and data analytics methods to ensure the meter’s long-term relevance.

The  design  of  a  smart  meter  for  energy  consumption  forecasting  requires  collabo-
ration  between  meter  manufacturers,  utility  companies,  and  data  analytics  experts.  It
should  strike  a  balance  between  accurate  data  collection,  data  security,  interoper-
ability,  and  usability  to  provide  reliable  and  valuable  insights  for  energy  consumption
forecasting.

3.3   Review of smart meter dataset

Smart  meters  usually  collect  data  every  second,  minute,  or  hour.  The  smart  meters
record  detailed  information  about  electricity  consumption,  providing  valuable  insights
into usage patterns and trends. Researchers and analysts often utilize publicly available
smart meter datasets to develop and test energy consumption forecasting models, anom-
aly  detection  algorithms,  and  other  applications  related  to  smart  building  and  energy
management.  Table  1  provides  the  various  datasets,  their  availability  as  public  or  pri-
vate,  along  with  the  website  link,  data  characteristics,  and  a  number  of  papers  refer-
ring  to  the  dataset  of  smart  buildings.  Table  2  provides  a  sample  smart  meter  dataset.
Researchers  carried  out  their  research  using  different  datasets.  Here  are  a  few  limita-
tions and challenges associated with smart meter datasets.

1 3
Page 9 of 33  35

.
x
e
d
n
 i
/
u
d
 e
.
s
s
a
m
u

t
r
a
m

 s
/
t
r
a
m

 s
/
p
h
p

y
n
n
u
S

,
)
1
2
0
2
(

.
l
a

t
e

b
e
e
j
u
M

)
1
2
0
2
(

.
l
a

t
e

s
t
t
e
s
u
h
c
a
s

3

h
t
i

w
d
e
t
c
e
n

s
r
e
t
e
m

t
r
a
m
s

-
n
o
c

s
i

h
c
a
e

.
s
 c
.
s
e
c
a
r
 t
/
/
:
s
p
t
t
h

,
)
9
1
0
2
(

.
l
a

t
e

z
a
N

l
a
i
t
n
e
d
i
s
e
R

-
s
a

M
n
r
e
t
s
e

W

4
2

n
i
m
0
3

,
s
e
m
o
h

6

g
n
o
m
A

c
i
l
b
u
P

+
s
e
c
n
 a
i
l
p
p
 a
/
4
7
3

/
t
 e
s
a
t
a
 d
/
u
d
 e
.
i
c
u

i
d
e
r
 p
+
y
g
r
e
n
e

n
o
i
t
c

s
a
t
a
 d
/
l

 m
/
u
d
 e
.
i
c
u

+
l
a
u
d
 i
v
i
d
n
 I
/
s
t
e

t
c
e
l
 e
+
d
l
o
 h
e
s
u
o
h

.
s
c
 i
.
e
 v
i
h
c
r
 a
/
/
:
s
p
t
t
h

+
r
e
w
o
 p
+
c
i
r

n
o
i
t
p
 m
u
s
n
o
c

.
e
s
r
 e
v
a
t
a
 d
/
/
:
s
p
t
t
h

?
l
m
t
h
 x
.
t
 e
s
a
t
a
d

=
d
 I
t
n
e
t
 s
i
s
r
e
p

.
i
o
 d
/
/
:
s
p
t
t
h
:
i
o
d

/
0
1
9
 7
.
0
 1
/
g
r
o

/
u
d
 e
.
d
 r
a
v
r
a
h

N
R
G
H
3
 N
N
V
D

/

;
)
b
0
2
0
2
,
a
0
2
0
2
(

d
n
a

n
a
v
o
d
l
o
M

,
)
1
2
0
2
(

k
i
w
o
l
S

)
0
2
0
2
(

g
n
a
i
X

l
a
i
t
n
e
d
i
s
e
R

e
c
n
a
r
F

,
s
i
r
a
P

l
a

t
e

,
r
e
t
k
A

)
1
2
0
2
(

l
a
i
t
n
e
d
i
s
e
R

a
d
a
n
a
C

–

)
3
2
0
2
(

.
l
a

t
e
n
a
h
K

d
n
a

l
a
i
t
n
e
d
i
s
e
R

a
e
r
o
K
h
t
u
o
S

e
c
ffi
O

9

6

–

n
i
m
0
1

-
i
s
o
p
e
r

g
n
i
n
r
a
e
l

;

P
E
A

(

y
r
o
t

)

C
P
E
H

I

h

1

–

c
i
l
b
u
P

f
o
e
g
a
s
u

y
l
r
u
o
H

2

y
g
r
e
n
e

–

–

e
t
a
v
i
r
P

y
t
i
c
i
r
t
c
e
l
E

g
n
i
r
u
d

t
e
s
a
t
a
d

n
o
i
t
p
m
u
s
n
o
c

I

9
1
-
D
V
O
C

y
r
o
t
i
s
o
p
e
r

e
c
a
r
t

s
s
a
m
U

3

4

.
s
c
 i
.
e
 v
i
h
c
r
 a
/
/
:
s
p
t
t
h

.
l
a

t
e

n
a
h
K

l
a
i
t
n
e
d
i
s
e
R

m
u
i
g
l
e
B

7
2

n
i
m
1

–

c
i
l
b
u
P

e
n
i
h
c
a
m

I

C
U

1

t
e
s
a
t
a
d
e
h
t

s
r
e
t
e
m
a
r
a
p

d
e
d
r
o
c
e
r

s
r
e
t
e
m

t
r
a
m
s

d
e
l
l
a
t
s
n
i

e
t
i
s
b
e
W

o
t

d
e
r
r
e
f
e
r

r
e
p
a
P

g
n
i
d
l
i
u
b

f
o

e
p
y
T

a
e
r
A

f
o
.
o
N

l
a
v
r
e
t
n
i

e
m
T

i

/
s
e
m
o
h

.
f
o
.
o
N

y
t
i
l
i
b
a
l
i
a
v
A

a
t
a
D

o
n

.

S

s
c
i
t
s
i
r
e
t
c
a
r
a
h
c

g
n
i
d
l
i
u
b

t
r
a
m
s

,
e
t
i
s
b
e
w

r
i
e
h
t

d
n
a

y
t
i
l
i
b
a
l
i
a
v
a

t
e
s
a
t
a
D

1
e
l
b
a
T

Intelligent deep learning techniques for energy consumption…1 3

35  Page 10 of 33

R. Mathumitha et al.

s
u
d
n
 I
/
u
 a
.
m
o
 c
.
d
i

,
)
1
2
0
2
(

a
m
r
a
h
S

r
g
s
u
 a
.
w
w
 w

/
/
:
s
p
t
t
h

d
n
a

i
r
a
z
a
b
r
i
P

l
a
i
t
n
e
d
i
s
e
R

-
s
u
A

,
y
e
n
d
y
S

a
i
l
a
r
t

/
h
c
 r
a
e
s
e
 R

-
r
u
 O
/
y
r
t

t
c
e
l
 e
-
e
m
o
 h
-
r
a
l
o
S

/
e
r
a
h
 s
-
o
 t
-
a
t
a
D

a
t
a
 d
-
y
t
i
c
i
r

/
s
t
 e
s
a
t
a
 d
/
m
o
 c
.
e
l
g

/
a
n
 e
h
t
a
h
 b
n
a
h
e
j

-
a
t
a
 d
-
r
e
t
e
 m

-
t
r
a
m

s

-
d
n
 a
-
a
 r
u
h
t
a
m

y
l
 l
i
e
r
a
b

-
g
a
 k
.
w
w
 w

/
/
:
s
p
t
t
h

-
b
a
l
l

E

,
)
0
2
0
2
(

i
s
s
a
l
A
d
n
a

n
a
b

.
l
a

t
e
m
a
l
s
I

l
l
e
K

,
)
9
1
0
2
(

)
3
2
0
2
(

.
l
a

t
e

l
a
i
t
n
e
d
i
s
e
R

d
n
a

a
r
u
h
t
a

M

r
a
t
t

U

f
o
s
t
c
i
r
t

-
s
i
d

y
l
l
i
e
r
a
B

h
s
e
d
a
r
P

?
l
m
t
h
 x
.
t
 e
s
a
t
a
d

=
d
 I
t
n
e
t
 s
i
s
r
e
p

.
i
o
 d
/
/
:
s
p
t
t
h
:
i
o
d

/
u
d
 e
.
d
 r
a
v
r
a
h

/
0
1
9
 7
.
0
 1
/
g
r
o

4
S
0
E
I
 F
/
N
V
D

h
g
n
i
S

,
)
a
0
2
0
2
(

e
n
i
s
s
a
Y
d
n
a

)
8
1
0
2
(

/
s
e
 l
c
i
t
r
 a
/
m
o
c

8
4
8
1
0
 2
a
t
a
d
s

r
e
l
k
e
T

,
)
0
2
0
2
(

,
)
0
2
0
2
(

.
l
a

t
e

)
0
2
0
2
(

x
u
a
n
e
R

.
e
r
u
t
a
 n
.
w
w
 w

/
/
:
s
p
t
t
h

.
l
a

t
e

,
l
a
t
s
A

e
c
ffi
O

y
n
a
m
r
e
G

/
g
r
 o
.
o
d
o
n
e
 z
/
/
:
s
p
t
t
h

8
 2
4
3
6
0
 5
/
d
r
o
c
e
r

d
i
h
s
a
R

,
)
3
2
0
2
(

)
1
2
0
2
(

.
l
a

t
e

.
l
a

t
e

c
i
d
o
T

l
a
i
t
n
e
d
i
s
e
R

m
o
d
g
n
i
k

d
e
t
i
n
U

.
e
s
r
 e
v
a
t
a
 d
/
/
:
s
p
t
t
h

.
l
a

t
e

r
u
e
m
H

i

l
a
i
t
n
e
d
i
s
e
R

a
d
a
n
a
C

3

5

3
5

9

1
2

a
t
a
d

y
l
h
t
n
o
m

d
n
a

n
i
m
0
3

–

c
i
l
b
u
P

-
c
e
l
e

e
m
o
h

r
a
l
o
S

5

a
t
a
d

y
t
i
c
i
r
t

n
i
m
3

t
r
a
m
s

0
0
1

y
l
r
a
e
N

c
i
l
b
u
P

r
e
t
e

M

t
r
a
m
S

6

s
r
e
t
e
m

a
r
u
h
t
a

M

:
a
t
a
D

y
l
l
i
e
r
a
B
&

–

s

8

–

–

c
i
l
b
u
P

a

,

D
N
O
L
B

l
e
v
e
l
-
g
n
i
d
l
i
u
b

t
e
s
a
t
a
d

e
c
ffi
o

c
i
l
b
u
P

l
a
c
i
r
t
c
e
l
e
T
I
F
E
R

n
i
m
1

e
m
o
h

1

c
i
l
b
u
P

-
e
r
u
s
a
e
m
d
a
o
l

t
e
s
a
t
a
d

s
t
n
e
m

r
e
w
o
P
y
l
e
t
u
n
i
M

t
e
s
a
t
a
d

f
o
c
a
n
a
m
A

l

e
h
T

:
2
s
d
P
M
A

7

8

9

t
e
s
a
t
a
d
e
h
t

s
r
e
t
e
m
a
r
a
p

d
e
d
r
o
c
e
r

s
r
e
t
e
m

t
r
a
m
s

d
e
l
l
a
t
s
n
i

e
t
i
s
b
e
W

o
t

d
e
r
r
e
f
e
r

r
e
p
a
P

g
n
i
d
l
i
u
b

f
o

e
p
y
T

a
e
r
A

f
o
.
o
N

l
a
v
r
e
t
n
i

e
m
T

i

/
s
e
m
o
h

.
f
o
.
o
N

y
t
i
l
i
b
a
l
i
a
v
A

a
t
a
D

o
n

.

S

)
d
e
u
n
i
t
n
o
c
(

1
e
l
b
a
T

1 3

Page 11 of 33  35

/
s
e
 l
c
i
t
r
 a
/
m
o
c

s
a
t
a
 D

/
t
 e
s
a
t
a
d

_
h
t
u
o
 S
_
n
 o
_
s
t
e

f
u
n
a
 m
_
n
a
e
r
o
K

o
t
c
a
 f
_
g
n
 i
r
u
t
c
a

_
y
t
i
c
i
 r
t
c
e
l
 e
_
s
e
i
r

_
n
o
i
t
p
 m
u
s
n
o
c

_
d
n
a
m
e
 d
_
d
n
a

i
t
r
a
 p
_
e
s
 n
o
p
s
e
r

2
2
8
4
 1
/
n
o
 i
t
a
p
i
c

6
5
2

e
l
a
 d
-
k
 u
/
t
e

;
)
9
1
0
2
(

.
l
a

t
e

,
)
1
2
0
2
(

.
l
a

t
e

s
a
v
e
k
s
a
r
a
P

.
l
a

t
e

n
e
h
C

a
m
a
s
O

,
)
2
2
0
2
(

)
9
1
0
2
(

.
l
a

t
e

/
d
c
e
b
 d
/
o
 i
.
b
u
h
t
i
g

l

m
t
 h
.
d
d
e
 r
/
s
k
n
i
l

.
l
a

t
e

r
u
e
m
H

i

)
b
0
2
0
2
(

S
U

.
b
u
h
k
o
 t
/
/
:
s
p
t
t
h

,
)
3
2
0
2
(

.
l
a

t
e

i
u
C

l
a
i
t
n
e
d
i
s
e
R

,
s
t
t
e
s
u
h
c
a
s
s
a

M

s
a
t
a
 d
/
m
o
 c
.
e
d
o
c

n
a
Y

,
)
9
1
0
2
(

e
n
i

h
t
i

w
 s
r
e
p
a
 p
/
/
:
s
p
t
t
h

-
s
s
a
Y
d
n
a

h
g
n
i
S

l
a
i
t
n
e
d
i
s
e
R

K
U

,
d
n
a
l
g
n
E

.
e
r
 a
h
s
g
 fi

/
/
:
s
p
t
t
h

–

y
r
t
s
u
d
n
I

a
e
r
o
K
h
t
u
o
S

3

2

1

s

3

s
e
m
o
h

6

c
i
l
b
u
P

A

:

D
D
E
R

0
1

n
o
i
t
a
g
e
r
g
g
a
s
i
d

y
g
r
e
n
e

r
o
f

t
e
s

a
t
a
d
c
i
l
b
u
p

h
c
r
a
e
s
e
r

s

6

s
e
m
o
h

5

c
i
l
b
u
P

E
L
A
D
K
U

-

1
1

t
e
s
a
t
a
d

n
i
m
1

s
e
i
r
t
s
u
d
n
i

0
1

c
i
l
b
u
P

n
a
e
r
o
K
h
t
u
o
S

2
1

g
n
i
r
u
t
c
a
f
u
n
a
m

s
e
i
r
o
t
c
a
f

t
e
s
a
t
a
d
e
h
t

s
r
e
t
e
m
a
r
a
p

d
e
d
r
o
c
e
r

s
r
e
t
e
m

t
r
a
m
s

d
e
l
l
a
t
s
n
i

e
t
i
s
b
e
W

o
t

d
e
r
r
e
f
e
r

r
e
p
a
P

g
n
i
d
l
i
u
b

f
o

e
p
y
T

a
e
r
A

f
o
.
o
N

l
a
v
r
e
t
n
i

e
m
T

i

/
s
e
m
o
h

.
f
o
.
o
N

y
t
i
l
i
b
a
l
i
a
v
A

a
t
a
D

o
n

.

S

)
d
e
u
n
i
t
n
o
c
(

1
e
l
b
a
T

Intelligent deep learning techniques for energy consumption…1 3

35  Page 12 of 33

R. Mathumitha et al.

/
u
 a
.
v
o
 g
.
a
t
a
 d
/
/
:
s
p
t
t
h

.
l
a

t
e

a
r
e
h
e
B

l
a
i
t
n
e
d
i
s
e
R

a
i
l
a
r
t
s
u
A

–

n
i
m
0
3

–

c
i
l
b
u
P

t
r
a
m
S
d
i
r

G

t
r
a
m
S

3
1

t
e
s
a
t
a
d
e
h
t

s
r
e
t
e
m
a
r
a
p

d
e
d
r
o
c
e
r

s
r
e
t
e
m

t
r
a
m
s

d
e
l
l
a
t
s
n
i

e
t
i
s
b
e
W

o
t

d
e
r
r
e
f
e
r

r
e
p
a
P

g
n
i
d
l
i
u
b

f
o

e
p
y
T

a
e
r
A

f
o
.
o
N

l
a
v
r
e
t
n
i

e
m
T

i

/
s
e
m
o
h

.
f
o
.
o
N

y
t
i
l
i
b
a
l
i
a
v
A

a
t
a
D

o
n

.

S

)
d
e
u
n
i
t
n
o
c
(

1
e
l
b
a
T

-
7
8
b
 9
-
3
a
 e
d
1
2
e
4

-
a
g
 d
-
s
 d
/
t
 e
s
a
t
a
d

a
8
a
5
 1
-
7
c
4
 9
-
0
1
6
4

s
 l
i
a
t
e
 d
/
f
 e
7
0
9
7
7

a
t
 a
d
t
s
u
 s
/
a
t
a
 d
/
g
r
o

.
i
t
 i
-

 m
.
o
r
i
e
v
 a
/
/
:
p
t
t
h

b
a
h
a
W

,
)
2
2
0
2
(

s
o
l
u
o
p
o
n
o
t
n
A

;
)
1
2
0
2
(

.
l
a

t
e

,
)
1
2
0
2
(

.
l
a

t
e

.
l
a

t
e
n
i
e
s
s
u
h
l
A

)
0
2
0
2
(

–

l
a
i
t
n
e
d
i
s
e
R

n
e
d
e
w
S

7
1

s

0
1

s
e
m
o
h

4

c
i
l
b
u
P

A

:

D
E
a
t
a
D
t
s
u
S

4
1

t
e
s
a
t
a
D
c
i
l
b
u
P

c
i
r
t
c
e
l
E
r
o
f

y
g
r
e
n
E

)

C
S
G
S
(

y
t
i

C

t
c
e
j
o
r
p

1 3

Table 2   Sample smart meter
dataset (Makonin 2019)

Page 13 of 33  35

Date

Hour Temperature Humidity

Pressure

Power

(Celsius)

(%)

(mm Hg)

(kW)

01-06-2012

01-06-2012
01-06-2012
01-06-2012
01-06-2012

1

2
3
4
5

13.8

13.3
13
12.5
12.7

83

84
83
86
85

101.47

101.39
101.39
101.26
101.21

1.011

0.451
0.505
0.441
0.468

3.3.1   Limitation in dataset selection

•  The availability of certain datasets may change over time. A dataset that was acces-
sible during the initial stages of a project may become unavailable, which could dis-
rupt ongoing research or analysis.

•  Metadata,  which  provides  context  and  additional  information  about  the  data,  may  be
lacking  in  some  datasets.  This  absence  can  make  it  challenging  to  interpret  the  data
accurately.

•  Working  with  large  datasets  can  pose  limitations  in  terms  of  storage,  computational
resources, and processing time, particularly for researchers with limited infrastructure.

3.3.2   Challenges in datasets selection

Selecting effective power consumption datasets can be challenging, as it involves various
considerations and potential pitfalls. Here are some challenges that might be encountered
during the selection of datasets.

(A)
Data availability
Availability of quality  power consumption data can be a significant challenge. Not all
regions  or  utilities  provide  access  to  detailed  consumption  data  in  realtime  setups,  espe-
cially  for  research  or  non-commercial  purposes.  There  is  a  need  to  create  a  benchmark
dataset for power prediction research. Exploring open data initiatives and repositories that
may  host  publicly  available  power  consumption  data.  The  research  also  suggests  that  in
the absence of a real-time setup, there is a need to develop simulation software or tools to
generate.
(B)
Data preprocessing
Due  to  several  number  of  reasons,  including  faults  in  meter  sensors,  variable  weather
conditions, and abnormal customer consumption patterns, the raw powerconsumption data
often requires preprocessing to clean, normalize, and transform it for analysis. This can be
time-consuming and may introduce errors if not donecarefully.

(C)
Data granularity
The  level  of  granularity  in  the  data  can  be  a  challenge.  Some  datasets  might  provide
data at a very high temporal resolution (e.g., every minute), while others mightonly offer
daily or monthly averages. The level of granularity that needs to be depends on the spe-
cific research or analysis goals. Therefore, the selection of datasetsmust match the level of
granularity needed for the specific analysis.

Intelligent deep learning techniques for energy consumption…1 335  Page 14 of 33

R. Mathumitha et al.

(D)
Data heterogeneity
The different utilities and regions may use different data formats and collection meth-
ods. The data needs to deal with various sources, and integrating heterogeneousdata can be
complex. So, the data collection requires standardization in a data format.

3.4   Data pre‑processing

Next,  the  data  is  split  into  training  and  testing  sets.  Smart  meters  collect  data  that  may
contain missing, redundant, and outlier values. To address these issues, preprocessing tech-
niques are applied to both the training and testing sets. Before training the model, the data
needs to be refined. Therefore, before training, the input raw dataset is refined by adding
missing values and removing outliers.

Missing  values  in  smart  meter  data  can  occur  due  to  communication  failures,  techni-
cal  malfunctions,  meter  installation/replacement,  data  processing  errors,  or  intentional
anonymization/aggregation (Dahunsi and Olawumi 2021). These factors can lead to gaps
in  the  data,  where  certain  time  intervals  or  measurements  are  not  captured  or  recorded.
This may lead to incorrect data collection.

Redundant values refer to duplicate or repetitive entries in the smart meter data. They
can  arise  from  issues  like  data  transmission  errors,  system  glitches,  or  multiple  data
sources providing overlapping or identical information (Ali et al. 2016). Redundant values
can skew the analysis and inflate the importance of certain data points if not properly iden-
tified and handled.

Outlier  values  in  smart  meter  data  are  extreme  or  unusual  measurements  that  deviate
significantly from the expected or normal range. Outliers can occur due to meter malfunc-
tions,  data  transmission  errors,  incorrect  sensor  readings,  or  anomalies  in  the  underlying
processes being measured (Wang et al. 2018). Outliers can negatively impact the accuracy
and  reliability  of  data  analysis  and  forecasting  models  if  not  detected  and  appropriately
treated.

Similarly, power consumption patterns vary widely and networks are sensitive to them.
Hence, the data normalization techniques are applied to keep the dataset within the normal
range. (Pascanu et al. 2013; Khan et al. 2020a; Rick and Berton 2020).

3.5   Training deep learning model and error metrics

Then, the normalized data is fed to the deep learning model to create a final model. Then,
the final model is used for testing to provide forecasted power as output at every instant of
time.

For  analyzing  and  verifying  the  effectiveness  of  the  model  With  different  kinds  of
experiments, its performance is evaluated and analyzed using error metrics and cross-val-
idation (Ghimire et al. 2023). The quality of the prediction model was evaluated using the
error metrics used.

This  is  the  common  framework  used  by  the  researchers.  But  still,  the  researchers  can
incorporate some advanced techniques to make the framework give more accurate results.
The framework excels in integrating a wide array of data sources, including real-time data,
and making effective use of this information for forecasting. This results in more accurate
and dynamic predictions.

1 3
Page 15 of 33  35

There  exist  several  strategies  to  deal  with  multistep  forecasting  problems  (Gao  et  al.
2012): the recursive strategy, which performs one-step predictions and feeds the result as
the last input for the next prediction; the direct strategy, which builds one model for each
time step; and the multi-output approach, which outputs the complete forecasting horizon
vector using just one model. The SISO strategy belongs to the time series problem. As sug-
gested in recent forecasting studies (Sulaiman et al. 2022; Imani and Ghassemian 2019),
the single input and single output (SISO) strategy is not performed in most of the studies.
The recursive approach is particularly useful for capturing short-term patterns and trends
in the data. By using the most recent prediction as input, it can quickly adjust to changes in
the time series, making it responsive to short-term fluctuations.

The Key Component and Innovation in the framework is integrating hybrid deep learn-
ing  models.  TCNs  are  employed  to  capture  long-range  dependencies  in  time  series  data.
This innovative architecture provides an alternative to traditional RNNs and LSTMs, mak-
ing it suitable for complex temporal patterns in power consumption.

4   Application of deep learning for forecasting energy consumption

Deep  learning  methods  are  promising  for  time  series  forecasting,  such  as  automatically
learning  temporal  dependencies  and  automatically  handling  temporal  structures  such
as  trends  and  seasonality  (Bandic  and  Kevric  2018).  In  the  paper  (Pirbazari  and  Sharma
2021), they have used several common algorithms in time series forecasting, e.g., support
vector regression (SVR), ARIMA, LSTM, etc. for training. RNNs can be extended to deep
recurrent  neural  networks  (DRNNs)  in  various  ways  (Cai  et  al.  2019).  According  to  the
RNN framework, we can deepen the hidden function, the transition function, and the hid-
den  output  function  to  create  a  DRNN  (Cai  et  al.  2019).  There  are  different  variants  of
DRNN, but the focus is on the widely known LSTM network and GRU network used in the
context of electricity predictions. Because the LSTM and GRU techniques have long term
dependencies. A multilayer perceptron neural network (MLP) is a unique form of feedfor-
ward network called a universal approximation. Due to its simplicity, it is one of the most
widely used neural network frameworks. (Pascanu, et al. 2013).

In the paper (Dehalwar et al. 2017), LSTM neural networks are used to perform predic-
tion operations. They proved that stationarization of the wavelet transform could improve
the  LSTM  prediction  results.  Finally,  the  prediction  results  are  synthesized  using  the
inverse stationary wavelet transform. In a paper (Lara-benitez 2020), the researchers sug-
gested a TCN model with (DenseNet) densely connected convolution networks. In a paper
(Mocanu  et  al.  2016),  they  present  a  hybrid  intelligent  technique  that  combines  a  CNN
with a multi-layer bidirectional long-short term memory (M-BDLSTM) method. In paper
(Rahman et al. 2018), for very short term forecasting, proposed a hybrid electricity demand
forecasting model that combines LSTM and CNN. The input sequence consists of multi-
ple pairs and the key value is the power demand value. Context values contain contextual
information  such  as  temperature,  humidity,  and  time  of  year.  In  a  paper  (Spiliotis  et  al.
2020), for a small industry profile, they performed a 30-min energy consumption forecast.
Instead of the conventional MSE, the pinball loss was used as a guideline for adjusting the
LSTM  neural  network’s  parameters.  Pinball  loss  is  indeed  a  term  used  in  the  context  of
training  and  tuning  parameters  for  LSTM  models,  particularly  in  time  series  forecasting.
Pinball loss, also known as quantile loss or quantile regression loss, is a loss function used
to  train  models  to  estimate  conditional  quantiles  of  a  target  variable.  In  the  case  of  time

Intelligent deep learning techniques for energy consumption…1 335  Page 16 of 33

R. Mathumitha et al.

y
t
i
d
i
m
u
h

r
o
o
d
n
i

n
i

d
n
u
o
f

e
r
e
w
s
r
o
r
r
e

e
g
r
a
L

f
o

y
c
a
r
u
c
c
a

n
a

d
e
n
i
a
t
b
o

l
e
d
o
m

t
n
e
r
r
u
c
e
r

e
h
T

)
k
r
o
w
t
e
n

l
a
r
u
e
n

p
e
e
d
(

N
N
D
d
n
a
N
N
R

)
0
2
0
2
(

.
l
a

t
e

n
o
s
w
a
M

s
n
o
i
t
a
t
i

m
L

i

s
c
i
r
t
e
m

r
o
r
r
e

g
n
i
t
s
a
c
e
r
o
f

d
n
a

s
g
n
i
d
n
fi
h
c
r
a
e
s
e
R

d
o
h
t
e

M

s
e
c
n
e
r
e
f
e
R

s
g
n
i
d
n
fi
d
n
a

,
s
n
o
i
t
a
t
i

m

i
l

,
k
r
o
w
d
e
t
a
l
e
r

g
n
i
n
r
a
e
l

p
e
e
d

f
o

y
r
a
m
m
u
s

e
h
T

3
e
l
b
a
T

n
i

n
w
o
h
s

t
o
n
e
r
e
w
s
c
i
r
t
e
m

r
o
r
r
e

d
e
n
o
i
t
n
e
m
e
h
T

d
n
a
E
A
M

,

E
S
M

r
o
f

2
0
.
0

d
n
a

,
1
0
.
0

,
4
0
0
0
.
0

n
o
i
t
c
e
s

t
l
u
s
e
r

e
h
t

E
S
M
R

s
n
o
i
t
c
i
d
e
r
p

%
2
8
.
6
9

-

E
A
M
T
S
L
h
t
i

w
N
N
C

)
a
0
2
0
2
(

.
l
a

t
e

n
a
h
K

h
g
u
o
n
e

s
e
g
n
a
h
c

l
a
n
o
i
t
a
r
e
p
o

/
r
e
h
t
a
e
w
e
r
u
t
u
f

y
b

d
e
t
c
e
ff
a

e
b

y
a
m
y
c
a
r
u
c
c
A

4
.
0
E
S
M
R
h
t
i

w

r
o
r
r
e

n
o
i
t
c
i
d
e
r
p

e
h
t

,

N
N
R
D

r
o
F

e
c
i
t
c
a
r
p

l
a
e
r

o
t

y
l
p
p
a

t
o
n

y
a
m
s
i
h
T

5
.
0
s
i

e
u
l
a
v
E
S
M
R

r
o
r
r
e

e
h
t

,
l
e
d
o
m
s
i
h
t

h
t
i

W

N
N
A
d
n
a
N
N
D

)
6
1
0
2
(

.
l
a

t
e

g
n
a
W

N
N
R
D

)
8
0
0
2
(

.
l
a

t
e

n
a
m
h
a
R

p
e
e
d

t
o
n

s
i

t
a
h
t

g
n
i
n
i
a
r
t

n
i

s
t
l
u
s
e
r

a
t
a
d

d
e
t
i

m
L

i

e
c
n
a
m
r
o
f
r
e
p

e
c
n
a
h
n
e

o
t

n
w
o
h
s
N
N
D

N
N
D

)
8
0
0
2
(

.
l
a

t
e

g
n
e
h
C

6
.
1
E
S
M
R

d
e
t
i

m

i
l

s
a
w
s
c
i
r
t
e
m

f
o

n
o
i
t
a
z
i
l
i
t

U

h
t
i

w
y
c
a
r
u
c
c
a

r
e
t
t
e
b
s
e
v
i
g
N
B
D
h
t
i

w
n
o
i
t
c
a
r
t
x
E

g
n
i
n
r
a
e
L
p
e
e
D

)
6
1
0
2
(

.
l
a

t
e

u
n
a
c
o
M

s
e
g
n
a
h
c

l
a
n
o
i
t
a
r
e
p
o

o
t

y
t
i
l
i
b
a
t
p
a
d
A

t
r
a

r
o
i
r
p

n
a
h
t

e
l
b
a
i
l
e
r

e
r
o
m
s
i

N
B
D

N
B
D

)
8
1
0
2
(

.
l
a

t
e

u
F

7
0
.
0

f
o
E
P
A
M

a

h
t
i

w

,

N
N
R
d
e
d
n
e
t
x
e

d
o
h
t
e
m

r
o
r
r
e
-
d
n
a
-
l
a
i
r
t

a

s
e
s
u

t
I

e
h
t

h
t
i

w
d
e
v
r
e
s
b
o

s
a
w
y
c
a
r
u
c
c
a

t
s
e
b

e
h
T

N
N
R
e
c
n
a
h
n
E

)
5
1
0
2
(

.
l
a

t
e

u
l
g
o
i
r
g
E

g
n
i
d
l
i
u
b

e
n
o

o
t

d
e
n
fi
n
o
c

s
i

t
I

s
s
e
l

s
e
m
u
s
n
o
c
N
N
A
O
S
P

-

,
6
1
0
.
0
E
P
A
M
h
t
i

W

l
a
i
c
fi

i
t
r
a
(

N
N
A

-
)

m
h
t
i
r
o
g
l
a

c
i
t
e
n
e
G

(

A
G

)
5
1
0
2
(

.
l
a

t
e

i

L

.
n
u
r

o
t

e
m

i
t

m
r
a
w
s

e
l
c
i
t
r
a
p
(

O
S
P
d
n
a

)
k
r
o
w
t
e
n

l
a
r
u
e
n

N
N
A

-
)
n
o
i
t
a
z
i
m

i
t
p
o

1 3

Page 17 of 33  35

series forecasting with LSTM models, it is often used to estimate and optimize quantiles of
the predicted distribution for different forecasting horizons.

Table  3  depicts  the  summary  of  previous  work  related  to  deep  learning.  In  the  table,
research  findings  and  their  corresponding  accuracy  were  mentioned.  The  limitations  of
each  method  were  tabulated.  From  the  table,  inferred  that  the  evaluation  metrics  play  a
vital role in prediction accuracy. And also input data contributes more to DL performance
and forecasting accuracy, especially weather variables.

5   Various applications of forecasting using forecasting horizon

Electricity load forecasting plays an important role in the planning and operation of energy
systems. It is the process of predicting future power consumption using historical load pro-
files and weather information. Electricity prediction is categorized into three groups. These
include short-term forecasts, typically ranging from days to weeks, medium-term forecasts,
typically  ranging  from  weeks  to  a  year,  and  long-term  forecasts,  typically  ranging  from
a year or more (Sajjad et al. 2020). The decision-making process, such as the scheduling
of  generation  amount,  maintenance  and  investment  plan,  and  so  on,  is  supported  by  the
expected  amount  of  energy  demand  (Le  et  al.  2020).  Based  on  different  applications  of
forecasting in the electrical field, it is classified into two categories.

5.1   Based on HVAC

The energy consumption of a building is impacted by several factors, including the build-
ing’s structure, HVAC system, occupant behavior, and lighting (Liu et al. 2020). Predict-
ing building energy usage can be categorized into five main types: heating energy, cool-
ing energy, combined heating and cooling energy, total building energy consumption, and
other factors (Mocanu et al. 2016). Anticipating power consumption has become essential
for enhancing power management and fostering collaboration between a building’s energy
consumption and the electrical grid (Xu et al. 2019). Accurate predictions play a crucial
role in enabling efficient power management, such as helping suppliers generate the right
amount  of  electricity  to  meet  demand.  Energy/cost  investment  funds  and  general  control
execution are legitimately impacted by how accurately energy use is estimated (Cai et al.
2019).

5.2   Based on power grid planning

It is crucial to categorize and forecast the energy consumption of residential buildings using
historical data based on the impact of dynamic real-time changes on both the supply and
demand sides to provide adequate decision-making for planning power transmission con-
figuration  patterns  that  maintain  regional  characteristics.  Short  and  very  short  term  fore-
casting techniques for energy consumption are useful for domestic energy demand manage-
ment, electricity price market design, energy efficiency, and maintenance planning for large
and  complex  smart  grids  (Abuella  and  Chowdhury  2017;  Khan  et  al.  2019;  Tokgoz  and
Unal 2018). Forecasting aims to provide as accurate predictions as possible, utilizing the
wealth of available data (Kim and Cho 2019b; Ullah et al. 2019). In recent years, numerous
approaches have been suggested to harness this information for making predictions (Afra-
siabi et al. 2020). These forecasting techniques effectively anticipate energy consumption

Intelligent deep learning techniques for energy consumption…1 335  Page 18 of 33

R. Mathumitha et al.

Fig. 3   Related works by forecast-
ing horizon

References

10%

30%

60%

Short term

Medium-Long term

Long-term

by establishing connections between energy and its consuming systems, thereby minimiz-
ing inefficiencies arising from over or undersupply and undersupply (Mocanu et al. 2016).
Figure 3 shows the forecasting horizon in the works of literature. It depicts the percent-
age  of  literature  that  contributes  to  Short  term,  Medium  term,  and  Long  term  forecast-
ing. Most of the literature concentrates more on short-term forecasting. Short-term energy
prediction is preferred over medium and long-term prediction due to its higher accuracy,
immediate applicability for real-time decision making, optimal resource allocation, contri-
bution to grid stability, and reliance on up-to-date data. The more predictable patterns and
behaviors  of  energy  consumption  in  the  short  term,  along  with  the  availability  of  timely
data, make short-term energy prediction more reliable and actionable for efficient energy
management  and  operational  adjustments  in  response  to  changing  demand  and  supply
dynamics.

6   Evaluation metrics

To validate the predictive models, a variety of accuracy criteria are employed. The most
commonly  used  are  mean  squared  error  (MSE),  root  mean  squared  error  (RMSE),  coef-
ficient  of  variation  of  root  mean  square  error  (CV-RMSE),  mean  absolute  error  (MAE),
mean absolute percentage error (MAPE), and determination coefficient (R2). The evalua-
tion metrics used to validate forecasting models are shown in Fig. 3. Each of these metrics
has a specific function. MSE is a commonly used metric in the context of forecasting and
predictive modeling to evaluate the accuracy of a forecasting model’s predictions. It meas-
ures the average squared difference between the predicted values and the actual (observed)
values. It is a way to quantify how well the forecasting model’s predictions match the actual
outcomes. RMSE is widely utilized to examine the accuracy of various anticipating crite-
ria because it is generally offered as an expectation quality estimation (Kim et al. 2019).
CV-RMSE can standardize the expected error and provide a useful unitless metric. MAE
relies on absolute error and can indicate the normal distance between expected and actual
values. Large errors are eliminated because the measurement mathematically enhances the
error (Wang et al. 2019). MAPE exhibits rate accuracy and mitigates the impact of abso-
lute error caused by a single exception (Kim et al. 2019). R2 evaluates how well the model

1 3
Table 4   Evaluation metrics
equation

S. no

Evaluation metrics

Equations

Page 19 of 33  35

1

2

3

4

5

RMSE

MAE

MAPE

CV-RMSE

R2

1
n
n ∑
n
1

1(xpred − xact)2
xpred − xact
�
�
xpred −xact
�
�
�
�
xact
�
�
�
�
1
1(xpred − xact)2
n
�
�
n ∑

n
1

�
1
n ∑
1
n ∑
1
x �
1 − ∑
∑

n

1(xpred −xact )2
n
1(xact −xact )

2

fits the real information and provides a measure of model consistency (Amasyali and El-
Gohary 2018).

The five evaluation metrics are listed in Table 4. Let n be the number of test data, xpred
be the value predicted by the proposed algorithm, and xact be the actual value in the quanti-
tative, xact be the average of the actual value.

7   Discussion

Based  on  the  review  of  previous  research  work,  a  detailed  summary  of  building  energy
consumption  forecasting  methods  is  presented  in  Table  5.  The  summary  includes  the
contribution of each paper and inference from that work was discussed briefly. And also,
explains the lists of buildings used, the network used, the input parameters used, and the
types of forecasting used.

All  prediction  methods  discussed  in  the  literature  have  weaknesses,  which  depend  on
the approach chosen. A table comparing different forecasting methods is provided to help
you easily identify which forecasting model type to use. Due to the relevance of informa-
tion for planning, a lot of effort is required when it comes to power forecasting. As stated
in  the  literature,  numerous  strategies  have  been  used.  Based  on  the  survey,  it  is  obvious
that DL has been proven to outperform other prediction approaches in terms of accuracy.
It has been discovered that linear models, which were previously relegated because of their
inability to solve nonlinear problems, are nevertheless applicable in the context of energy
projections. RNNs are effective in solving nonlinear issues with great prediction accuracy.
Despite  the  power  of  RNN’s  as  discussed  in  the  literature,  it  has  a  significant  drawback,
called the problem of vanishing gradient For this reason, few researchers have applied tra-
ditional RNNs. DRNN improved the boundary vanishing gradient by introducing memory
(Kaur  and  Ahuja  2017).  Therefore,  LSTM  with  GRU  is  currently  used  in  the  context  of
energy prediction because it can model complex functions with high accuracy.

Accurate customer-level energy forecasting has a direct impact on overall system effi-
ciency.  However,  it  is  difficult  to  predict  building  energy  consumption,  especially  in  the
medium  and  long  term  changes  in  climatic  conditions,  thermal  system  performance,
and  patterns  in  occupancy.  Therefore,  current  state-of-the-art  technology  cannot  contain
building-level uncertainty due to many influencing factors. These can include changes in
weather, occupant behavior, changes in building structure and operations, missing data in
datasets, computation time impacting forecast accuracy, and more. As reported in the lit-
erature,  few  researchers  have  used  occupancy  profiles  in  predictive  models  (Nepal  2020;

Intelligent deep learning techniques for energy consumption…1 335  Page 20 of 33

R. Mathumitha et al.

s
a
h

l
e
d
o
m
d
e
s
o
p
o
r
p

e
h
T

,

N
N
C

(

s
e
l
u
d
o
m
e
e
r
h
t

y
l
l
u
f
(

C
F

,

-

E
A
M
T
S
L

r
e
w
o
p

g
n
i
t
c
i
d
e
r
p

r
o
f

)
)
r
e
y
a
l

d
e
t
c
e
n
n
o
c

n
o
i
t
p
m
u
s
n
o
c

a
t
a
d

r
a
d
n
e
l
a
c

d
n
a

)
r
e
t
e
m

-

E
A
M
T
S
L

g
n
i
d
l
i
u
b

l
a
i
t
n
e
d
i
s
e
r

-
u
l
a
v
e

e
r
e
w
s
l
e
d
o
m

,
h
c
r
a
e
s
e
r

e
h
t

n
i

d
e
t
a

d
e
s
o
p
o
r
p

y
e
h
t

d
n
a

g
n
i
t
s
a
c
e
r
o
f

d
e
s
a
b

N
N
C
d
i
r
b
y
h

l
a
e
d
i

n
a

-

E
A
M
T
S
L
e
h
t

h
t
i

w

l
e
d
o
m

m
r
e
t

t
r
o
h
S

t
r
a
m
S
(

l
a
c
i
r
o
t
s
i
H

h
t
i

w
N
N
C
d
i
r
b
y
H

-
n
o
n

d
n
a

l
a
i
t
n
e
d
i
s
e
R

-
g
n
i
n
r
a
e
l

p
e
e
d

l
a
r
e
v
e
S

)
a
0
2
0
2
(

.
l
a

t
e

n
a
h
K

t
e
s
a
t
a
d
e
h
t

t
u
o
b
a

n
o
i
t

f
o

n
o
i
s
u
l
c
n
i

e
h
t

d
n
a

s
i

s
e
l
b
a
i
r
a
v

r
e
h
t
a
e
w

g
n
i
s
s
i

m

-
r
e
e
n
i
g
n
e

e
r
u
t
a
e
f

g
n
i
s
u

g
n
i
r
e
t
s
u
l
c

e
h
t

n
o

s
u
c
o
f

t
o
n

s
e
o
d
t
u
B

.
g
n
i

m
h
t
i
r
o
g
l
a

s
e
r
u
t
a
e
f

g
n
i
n
i
a
t
b
o

n
o

y
l
n
i
a
m
d
e
s
u
c
o
F

-
l
a
b
m

i

t
s
o
m

s
i

s
e
g
n
e
l

e
s
i
r
a

s

m
e
l
b
o
r
p
e
c
n
a

-
l
a
h
c

r
o
j
a
m
e
h
t

f
o

e
n
O

r
a
d
n
e
l
a
c

d
n
a

)
r
e
t
e
m

a
t
a
d

y
n
a
p
m
o
c
n
o
i
t
u
b
i
r
t
s
i
d

y
t
i
c
i
r
t
c
e
l
e

d
e
n
w
o

f
o

s
s
e
n
e
v
i
t
c
e
ff
e

p
e
e
d

d
e
t
s
e
g
g
u
s

e
h
t

e
h
t

e
h
t

,
y
g
e
t
a
r
t
s

g
n
i
n
r
a
e
l

l
a
n
o
i
t
i
d
d
a

e
v
fi
s
e
n
i

-
g
n
i
n
r
a
e
l

e
n
i
h
c
a
m

-

m
a
x
e

o
s
l
a

y
d
u
t
s

s
l
e
d
o
m
d
e
s
a
b

-
i
g
o
l
o
r
o
e
t
e
m

,
)
r
e
t
e
m

a
t
a
d

r
a
d
n
e
l
a
c

d
n
a

l
a
c

s
n
a
e
m
K
-
n
o
i
t
a
z
i
m

i
t
p
o

R
V
S
d
n
a
m
h
t
i
r
o
g
l
a

l
a
i
t
n
e
d
i
s
e
r

f
o

d
a
e
h
a

d
n
a
m
e
d

y
t
i
c
i
r
t
c
e
l
e

m
r
e
t

t
r
o
h
S

t
r
a
m
S
(

l
a
c
i
r
o
t
s
i
H

m
r
a
w
s

e
l
c
i
t
r
a
P

g
n
i
d
l
i
u
b

l
a
i
t
n
e
d
i
s
e
R

h
t
n
o
m
e
n
O
g
n
i
t
c
i
d
e
r
P

)
8
1
0
2
(

u
F

a
t
a
d

r
a
d
n
e
l
a
c

d
n
a

)
r
e
t
e
m

m
h
t
i
r
o
g
l
a

g
n
i

-
r
e
t
s
u
l
c

d
e
s
a
b
-
y
t
i
s
n
e
d

s
a
w
x
e
d
n
i

n
o
i
t
a
u
l
a
v
e

-
u
s
n
u

y
b

d
e
m
r
o
f
r
e
p

g
n
i
r
e
t
s
u
l
c

d
e
s
i
v
r
e
p

d
n
a
m
h
t
i
r
o
g
l
a

g
n
i

a

g
n
i
s
u

e
n
o
d

s
a
w

–

t
r
a
m
S
(

l
a
c
i
r
o
t
s
i
H

-
r
e
t
s
u
l
c

d
e
s
a
b
-
y
t
i
s
n
e
D

g
n
i
d
l
i
u
b

l
a
i
t
n
e
d
i
s
e
R

n
o
i
t
c
e
t
e
d

l
a
m
r
o
n
b
A

)
9
1
0
2
(

.
l
a

t
e

i
e

W

-
a
m
r
o
f
n
i

d
e
l
i
a
t
e
d

t
o
N

m
r
e
t

t
r
o
h
S

t
r
a
m
S
(

l
a
c
i
r
o
t
s
i
H

N
S
E
-

N
N
C
d
i
r
b
y
H

-
t
n
e
m
n
r
e
v
o
g

l
a
r
e
d
e
F

s
s
e
s
s
a

d
n
a

e
r
a
p
m
o
c

o
T

)
3
2
0
2
(

.
l
a

t
e

e
r
i

m
i
h
G

e
c
n
e
r
e
f
n
I

g
n
i
t
s
a
c
e
r
o
f

f
o

e
p
y
T

s
r
e
t
e
m
a
r
a
p

t
u
p
n
I

d
e
s
u

k
r
o
w
t
e
N

g
n
i
d
l
i
u
b

f
o

e
p
y
T

n
o
i
t
u
b
i
r
t
n
o
C

s
e
c
n
e
r
e
f
e
R

e
c
n
e
r
e
f
n
i

d
n
a

,
n
o
i
t
u
b
i
r
t
n
o
c

r
i
e
h
t

,
s
r
e
p
a
p

h
c
r
a
e
s
e
r

s
u
o
i
v
e
r
p

f
o

y
r
a
m
m
u
S

5
e
l
b
a
T

1 3

Page 21 of 33  35

s
a
w
e
u
q
i
n
h
c
e
t

A
M
R
A

I

s
e
m

i
t

e
t
a
r
e
n
e
g

o
t

d
e
s
u

-
p
m
u
s
n
o
c

y
g
r
e
n
e

s
e
i
r
e
s

n
a

,
d
a
e
t
s
n
I

.
e
n
o
d
t
o
n

a
t
a
d

n
o
i
t

e
s
u
a
c
e
b

s
s
e
c
o
r
p

o
t

e
m

i
t

f
o

e
g
a
r
o
t
s

e
g
r
a
l

e
h
t

f
o

e
r
o
m
k
o
o
t

t
i

,
d
o
h
t
e
m

g
n
i
t
s
i
x
e

n
a

o
t

d
e
r
a
p
m
o
C

)

B
T
(

a
t
a
d

r
a
d
n
e
l
a
c

d
n
a

)
r
e
t
e
m

a
t
a
d

r
e
t
s
u
l
c

-
t
u
p
m
o
c

d
e
t
u
b
i
r
t
s
i
d

n
o

t
l
i
u
b

r
e
t
s
u
l
c

g
n
i

-
c
e
ff
e
-
t
s
o
c

,
d
r
a
d
n
a
t
s

n
a

h
t
i

w
e
r
a
w
d
r
a
h

e
v
i
t

-
i
t
a
m
e
h
t
a
m

t
n
e
i
c
ffi
e

d
e
r
o
l
i
a
t

m
h
t
i
r
o
g
l
a

-
s
s
e
c
o
r
p

a
t
a
d

g
i
b

l
a
c

r
o
f

e
h
t

e
z
i
l
a
u
s
i
v

d
n
a

g
n
i

n
o
i
t
p
m
u
s
n
o
c

y
g
r
e
n
e

n
o
i
t
a
z
i
l
i
t
u

e
h
t

h
g
u
o
r
h
T

m
r
e
t
-
t
r
o
h
S

t
r
a
m
S
(

l
a
c
i
r
o
t
s
i
H

d
e
t
s
o
o
B

t
n
e
i
d
a
r
G

g
n
i
d
l
i
u
b

l
a
i
t
n
e
d
i
s
e
R

d
o
h
t
e
m
e
l
b
m
e
s
n
e

n
A

n
a
s
a
v
i
n
i
r
S
d
n
a

g
n
a
W

e
c
n
e
r
e
f
n
I

g
n
i
t
s
a
c
e
r
o
f

f
o

e
p
y
T

s
r
e
t
e
m
a
r
a
p

t
u
p
n
I

d
e
s
u

k
r
o
w
t
e
N

g
n
i
d
l
i
u
b

f
o

e
p
y
T

n
o
i
t
u
b
i
r
t
n
o
C

s
e
c
n
e
r
e
f
e
R

)
d
e
u
n
i
t
n
o
c
(

5
e
l
b
a
T

n
a
c

s
l
e
d
o
m

,
s
e
i
g
e
t
a
r
t
s

g
n
i
n
r
a
e
l

e
l
b
m
e
s
n
e

f
o

t
n
e
i
l
i
s
e
r

e
r
o
m

r
e
v
i
l
e
d

s
e
m
o
c
t
u
o

e
s
i
c
e
r
p

d
n
a

l
a
u
d
i
v
i
d
n
i

o
t

d
e
r
a
p
m
o
c

s
e
u
q
i
n
h
c
e
t

n
o
i
t
c
i
d
e
r
p

-
i
g
o
l
o
r
o
e
t
e
m

,
)
r
e
t
e
m

a
t
a
d

r
a
d
n
e
l
a
c

d
n
a

l
a
c

-
o
g
l
a

e
e
r
t

n
o
i
s
s
e
r
g
e
r

-
e
c
n
e
u
q
e
s

d
n
a
m
h
t
i
r

e
c
n
e
u
q
e
s
-
o
t

M
T
S
L

-
n
e
d
i
s
e
r

r
o
f

d
n
a
m
e
d

y
g
r
e
n
e

t
s
a
c
e
r
o
f

o
t

g
n
i
d
l
i
u
b

l
a
i
t

)
7
1
0
2
(

f
o

n
o
i
t
a
n
i
m
a
x
e

e
h
T

–

t
r
a
m
S
(

l
a
c
i
r
o
t
s
i
H

-
s
e
r
g
o
r
p

d
e
s
i
v
r
e
p
u
s
n
U

g
n
i
d
l
i
u
b

l
a
i
t
n
e
d
i
s
e
R

-
o
r
p

d
e
s
i
v
r
e
p
u
s
n
u

n
A

i
d
e
v
i
w
D
d
n
a

h
g
n
i

S

n
o
i
t
p
m
u
s
n
o
c

y
g
r
e
n
e

e
h
t

s
e
d
u
l
c
x
e

s
n
r
e
t
t
a
p

-
g
n
o
l

d
n
a
m
r
e
t
-
t
r
o
h
s

-
i
l
p
p
a

e
l
p
i
t
l
u
m
m
r
e
t

h
t
o
b

f
o

g
n
i
t
s
a
c
e
r
o
f

n
o
i
t
i
d
d
a

n
i

,
e
g
a
s
u
e
c
n
a

n
o
i
t
p
m
u
s
n
o
c

y
g
r
e
n
e

o
t

s
n
o
i
t
c
i
d
e
r
p

r
a
d
n
e
l
a
c

d
n
a

)
r
e
t
e
m

a
t
a
d

l
a
t
n
e
m
e
r
c
n
i

e
v
i
s

a
t
a
d

g
n
i
n
i
m

l
a
t
n
e
m
e
r
c
n
i

e
v
i
s
s
e
r
g

-
a
h
c
e
m
g
n
i
n
i
m
a
t
a
d

o
t

d
e
y
o
l
p
m
e

s
i

m
s
i
n

r
e
t
e
m

t
r
a
m
s

e
z
y
l
a
n
a

n
o
i
t
p
m
u
s
n
o
c

y
g
r
e
n
e

t
n
e
u
q
e
r
f

g
n
i
s
u

a
t
a
d

g
n
i
n
i
m
n
r
e
t
t
a
p

)
8
1
0
2
(

s
a
w
g
n
i
s
s
e
c
o
r
p
-
e
r
p

a
t
a
D

n
o
i
t
a
z
i
l
a
u
s
i
V

t
r
a
m
S
(

l
a
c
i
r
o
t
s
i
H

g
n
i
t
u
p
m
o
c

d
e
t
u
b
i
r
t
s
i
D

g
n
i
d
l
i
u
b

l
a
i
t
n
e
d
i
s
e
R

a

s
e
z
i
l
i
t
u

k
r
o
w
s
i
h
T

)
0
2
0
2
(

.
l
a

t
e

a
t
p
u
G

Intelligent deep learning techniques for energy consumption…1 3

35  Page 22 of 33

R. Mathumitha et al.

c
fi
i
c
e
p
s

a

n
i

d
e
t
a
u
l
a
v
e

g
n
i
t
t
e
s

c
i
t
a
m

i
l
c

r
a
d
n
e
l
a
c

d
n
a

,
l
a
c
i
g
o
l

a
t
a
d

-
r
e
h
t

s
’
g
n
i
d
l
i
u
b

a

g
n
i

d
e
s
a
b

r
o
i
v
a
h
e
b

l
a
m

d
i
r
b
y
h

a

g
n
i
y
o
l
p
m
e

,
a
t
a
d

d
e
t
c
e
l
l
o
c

n
o

h
c
a
o
r
p
p
a

s
a
w
n
o
i
t
p
m
u
s
n
o
c

e
r
e
h

t
s
a
c
e
r
o
f

r
a
d
n
e
l
a
c

d
n
a

)
r
e
t
e
m

a
t
a
d

g
n
i
d
l
i
u
b

g
n
i
t
a
m

i
t
s
e

n
o
i
t
p
m
u
s
n
o
c

y
g
r
e
n
e

-
a
n
i
b
m
o
c

a

g
n
i
s
u

d
n
a
N
N
C

f
o

n
o
i
t

k
r
o
w
t
e
n
M
T
S
L
D
B
M

-

d
l
o
h
e
s
u
o
h

d
e
t
i

m

i
l

e
h
T

r
o
f

d
e
t
n
u
o
c
c
a

s
a
w

g
n
i
t
s
a
c
e
r
o
f

r
a
d
n
e
l
a
c

d
n
a

)
r
e
t
e
m

-
e
v
a
w
y
r
a
n
o
i
t
a
t
s

d
n
a

a
t
a
d

m
r
o
f
s
n
a
r
t

t
e
l

n
i
h
t
i

w
s
d
a
o
l

y
g
r
e
n
e

s
g
n
i
d
l
i
u
b

l
a
i
t
n
e
d
i
s
e
r

y
g
r
e
n
e

e
g
a
n
a
m
o
t

m
r
e
t
-
t
r
o
h
s

g
n
i

s
m
e
t
s
y
s

m
r
e
t
-
t
r
o
h
S

t
r
a
m
S
(

l
a
c
i
r
o
t
s
i
H

k
r
o
w
t
e
n

l
a
r
u
e
n
M
T
S
L

g
n
i
d
l
i
u
b

l
a
i
t
n
e
d
i
s
e
R

-
t
c
i
d
e
r
p

r
o
f

d
o
h
t
e
m
A

)
4
1
0
2
(

.
l
a

t
e

a
n
a
z
r
a
F

y
l
r
u
o
h
-
b
u
s

o
t
n
i

n
w
o
d

-
p
m
u
s
n
o
c

r
e
w
o
p

a

e
h
t

r
o
f

e
l
fi
o
r
p

n
o
i
t

n
e
k
o
r
b

,
d
a
e
h
a

y
a
d

s
l
a
v
r
e
t
n
i

r
a
d
n
e
l
a
c

d
n
a

,
l
a
c
i
g
o
l

a
t
a
d

g
n
i

o
t

N
N
A
n
a

d
n
a

n
o
i
t

-
c
a
r
t
x
e

t
n
e
n
o
p
m
o
c

r
e
w
o
p

e
h
t

t
s
a
c
e
r
o
f

e
h
t

r
o
f

e
l
fi
o
r
p

e
g
a
s
u

y
a
d

g
n
i
w
o
l
l
o
f

d
e
d
i
v
o
r
p

h
c
a
o
r
p
p
a

e
h
T

m
r
e
t

t
r
o
h
s

-
o
r
o
e
t
e
m

,
l
a
c
i
r
o
t
s
i
H

N
N
A

-
d
l
i
u
b

l
a
i
t
n
e
d
i
s
e
r
-
n
o
N

g
n
i
y
o
l
p
m
e

e
u
q
i
n
h
c
e
t

A

)
0
2
0
2
(

.
l
a

t
e

i
s
k
o
h
C

y
g
r
e
n
e

r
u
o
h
-
e
n
o

t
x
e
N

m
r
e
t

t
r
o
h
S

t
r
a
m
S
(

l
a
c
i
r
o
t
s
i
H

-

M
T
S
L
D
B
M
d
n
a
N
N
C

g
n
i
d
l
i
u
b

l
a
i
t
n
e
d
i
s
e
R

r
o
f

h
c
a
o
r
p
p
a

n
A

)
9
1
0
2
(

.
l
a

t
e
m
K

i

e
c
n
e
r
e
f
n
I

g
n
i
t
s
a
c
e
r
o
f

f
o

e
p
y
T

s
r
e
t
e
m
a
r
a
p

t
u
p
n
I

d
e
s
u

k
r
o
w
t
e
N

g
n
i
d
l
i
u
b

f
o

e
p
y
T

n
o
i
t
u
b
i
r
t
n
o
C

s
e
c
n
e
r
e
f
e
R

)
d
e
u
n
i
t
n
o
c
(

5
e
l
b
a
T

s
a
w
h
c
a
o
r
p
p
a

s
i
h
T

m
r
e
t

t
r
o
h
S

-
o
r
o
e
t
e
m

,
l
a
c
i
r
o
t
s
i
H

d
o
h
t
e
m
d
i
r
b
y
H

g
n
i
d
l
i
u
b

l
a
i
t
n
e
d
i
s
e
R

-
t
a
c
i
l
p
e
r

r
o
f

d
o
h
t
e
m
A

)
0
2
0
2
(

.
l
a

t
e

n
e
W

l
a
u
t
r
i
v

a

n
i

e
u
q
i
n
h
c
e
t

s
a
w

t
a
h
t

t
n
e
m
n
o
r
i
v
n
e

d
e
t
a
e
r
c

r
a
d
n
e
l
a
c

d
n
a

,
l
a
c
i
g
o
l

)
e
n
i
h
c
a
m

r
o
t
c
e
v

t
r
o
p

g
n
i

-
e
m

i
t

a

s
e
t
a
r
g
e
t
n
i

t
a
h
t

a
t
a
d

n
a

h
t
i

w

l
e
d
o
m
s
e
i
r
e
s

e
h
t

e
c
n
a
h
n
e

o
t

N
N
A

-
t
c
i
d
e
r
p

f
o

y
c
a
r
u
c
c
a

l
a
m
r
e
h
t

g
n
i
d
l
i
u
b

g
n
i

s
d
a
o
l

e
h
t

d
e
t
a
u
l
a
v
e

y
e
h
T

m
r
e
t

g
n
o
L

-
o
r
o
e
t
e
m

,
l
a
c
i
r
o
t
s
i
H

-
p
u
s
(

M
V
S
d
n
a
N
N
A

-
d
l
i
u
b

l
a
i
t
n
e
d
i
s
e
r
-
n
o
N

d
o
h
t
e
m
d
e
n
i
b
m
o
c
A

)
6
1
0
2
(

.
l
a

t
e

b
r
a
H

1 3

Page 23 of 33  35

d
e
t
a
l
e
r

h
t
o
b
(

s
c
i
t
s
i
r
e
t

)
e
t
a
m

i
l
c

d
n
a

r
e
w
o
p

o
t

s
n
i
a
m
e
r

s

m
e
t
s
y
s

n
o
i
t

-
p
m
u
s
n
o
c

r
e
w
o
p

n
o

-
c
a
r
a
h
c

f
o

e
c
n
e
u
fl
n
i

d
e
h
s
i
n
fi
n
u

a
t
a
d

d
n
a
m
h
t
i
r
o
g
l
a

n
o
i
t

M
T
S
L

n
o
i
t
p
m
u
s
n
o
c

y
g
r
e
n
e

-
r
e
t
e
d

y
l
e
t
a
r
u
c
c
a

o
t

y
g
r
e
n
e

g
n
i
d
l
i
u
b

e
n
i
m

e
g
a
s
u

e
h
t

e
r
o
l
p
x
e

o
t

d
e
r
i
u
q
e
r

n
o
i
t
a
z
i
m

i
t
p
o

r
e
t
e
m
a
r
a
p

e
u
q
i
n
h
c
e
t

a
t
a
d

s
t
s
a
c
e
r
o
f

m
r
e
t
-
t
r
o
h
s

y
g
r
e
n
e

g
n
i
d
l
i
u
b

f
o

g
n
i
h
s
i
l
p
m
o
c
c
a

r
o
f

e
g
a
s
u

s
i

h
c
r
a
e
s
e
r

r
e
h
t
r
u
F

m
r
e
t

t
r
o
h
S

r
a
d
n
e
l
a
c

d
n
a

l
a
c
i
r
o
t
s
i
H

d
o
h
t
e
m
e
l
b
m
e
s
n
e

g
n
i
d
l
i
u
b

l
a
i
t
n
e
d
i
s
e
R

e
u
q
i
n
h
c
e
t

e
l
b
m
e
s
n
e

n
A

)
b
0
2
0
2
(

.
l
a

t
e

g
n
a
h
Z

e
c
n
e
r
e
f
n
I

g
n
i
t
s
a
c
e
r
o
f

f
o

e
p
y
T

s
r
e
t
e
m
a
r
a
p

t
u
p
n
I

d
e
s
u

k
r
o
w
t
e
N

g
n
i
d
l
i
u
b

f
o

e
p
y
T

n
o
i
t
u
b
i
r
t
n
o
C

s
e
c
n
e
r
e
f
e
R

e
h
t

g
n
i
d
r
a
g
e
r

h
c
r
a
e
s
e
R

m
r
e
t

t
r
o
h
S

r
a
d
n
e
l
a
c

d
n
a

l
a
c
i
r
o
t
s
i
H

-
a
z
i
m

i
t
p
o
e
n
i
s
o
c

e
n
i
s

g
n
i
d
l
i
u
b

l
a
i
t
n
e
d
i
s
e
R

g
n
i
t
s
a
c
e
r
o
f

r
o
f

l
e
d
o
m
A

)
0
2
0
2
(

.
l
a

t
e

u
m
o
S

)
d
e
u
n
i
t
n
o
c
(

5
e
l
b
a
T

c
fi
i
c
e
p
s

a

n
i
d
e
t
a
u
l
a
v
e

g
n
i
t
t
e
s

c
i
t
a
m

i
l
c

r
a
d
n
e
l
a
c

d
n
a

,
l
a
c
i
g
o
l

a
t
a
d

U
R
G
d
n
a
N
N
C
g
n
i
s
u

d
e
c
n
a
h
n
e

r
o
f

d
e
s
u

s
i

g
n
i
n
r
a
e
l

e
c
n
e
u
q
e
s

s
e
i
t
i
l
i
b
a

s
s
o
r
c
a

s
t
h
g
i
s
n
i

l
a
c
i
s
y
h
p

t
a
h
t

e
g
a
s
u

y
g
r
e
n
e

g
n
i

d
n
a

a
t
a
d

d
a
o
l

s
e
z
i
l
i
t
u

n
o
i
t
c
i
d
e
r
p

e
s
r
e
v
i
d

s
o
i
r
a
n
e
c
s

a
t
a
d

d
n
a

n
o
i
s
s
e
r
g
e
R

s
c
i
t
s
i
r
u
e
h

g
n
i

-
p
m
u
s
n
o
c

y
g
r
e
n
e

g
n
i

-
i
s
y
h
p

d
n
a

a
t
a
d

d
a
o
l

s
e
g
a
r
e
v
e
l

t
a
h
t

n
o
i
t

s
u
o
i
r
a
v

n
i

s
t
h
g
i
s
n
i

l
a
c

s
o
i
r
a
n
e
c
s

e
v
i
t
c
i
d
e
r
p

-
t
c
i
d
e
r
p

r
o
f

e
u
q
i
n
h
c
e
t

A

m
r
e
t

g
n
o
L

r
a
d
n
e
l
a
c

d
n
a

l
a
c
i
r
o
t
s
i
H

s
s
e
c
o
r
P
n
a
i
s
s
u
a
G

-
d
l
i
u
b

l
a
i
t
n
e
d
i
s
e
r
-
n
o
N

-
t
s
a
c
e
r
o
f

r
o
f

d
o
h
t
e
m
A

)
8
1
0
2
(

.
l
a

t
e

h
s
a
k
a
r
P

f
o

n
o
i
t
c
e
l
e
s

d
o
o
g

a

n
e
v
i
g

a

r
o
f

s
t
u
p
n
i

n
o
i
s
i
c
e
r
p

a
t
a
d

g
n
i

-
p
m
u
s
n
o
c

d
a
o
l

e
t
a
m

n
o
i
t

s
e
r
i
u
q
e
r

h
c
a
o
r
p
p
a

s
i
h
T

m
r
e
t
-
t
r
o
h
S

r
a
d
n
e
l
a
c

d
n
a

l
a
c
i
r
o
t
s
i
H

N
N
R
d
n
a

M
T
S
L

-
d
l
i
u
b

l
a
i
t
n
e
d
i
s
e
r
-
n
o
N

-
i
t
s
e

o
t

h
c
a
o
r
p
p
a

n
A

)
0
2
0
2
(

.
l
a

t
e

n
u
S

s
a
w
h
c
a
o
r
p
p
a

s
i
h
T

m
r
e
t

t
r
o
h
S

-
o
r
o
e
t
e
m

,
l
a
c
i
r
o
t
s
i
H

U
R
G
d
n
a
N
N
C

g
n
i
d
l
i
u
b

l
a
i
t
n
e
d
i
s
e
R

d
e
t
c
a
r
t
x
e

e
r
a

s
e
r
u
t
a
e
F

)
0
2
0
2
(

.
l
a

t
e

d
a
j
j
a
S

Intelligent deep learning techniques for energy consumption…1 3

35  Page 24 of 33

R. Mathumitha et al.

t
n
e
w
r
e
d
n
u

h
c
a
o
r
p
p
a

e
h
T

m
r
e
t

t
r
o
h
S

r
a
d
n
e
l
a
c

d
n
a

l
a
c
i
r
o
t
s
i
H

d
n
a

g
n
i
n
r
a
e
l

r
e
f
s
n
a
r
t

g
n
i
d
l
i
u
b

l
a
i
t
n
e
d
i
s
e
R

-
e
r
p

r
o
f

e
u
q
i
n
h
c
e
t

A

)
0
2
0
2
(

.
l
a

t
e

e
L

e
c
n
e
r
e
f
n
I

g
n
i
t
s
a
c
e
r
o
f

f
o

e
p
y
T

s
r
e
t
e
m
a
r
a
p

t
u
p
n
I

d
e
s
u

k
r
o
w
t
e
N

g
n
i
d
l
i
u
b

f
o

e
p
y
T

n
o
i
t
u
b
i
r
t
n
o
C

s
e
c
n
e
r
e
f
e
R

n
i

y
l
e
v
i
s
u
l
c
x
e

g
n
i
t
s
e
t

s
e
r
u
t
c
u
r
t
s

l
a
i
t
n
e
d
i
s
e
r

-
n
o
n

n
i

d
a
o
l

r
e
w
o
p

e
h
t

s
g
n
i
d
l
i
u
b

l
a
i
t
n
e
d
i
s
e
r

e
c
u
d
e
r

o
t

d
e
s
o
p
o
r
p

s
a
w
y
g
o
l
o
n
h
c
e
t

s
i
h
T

a
t
a
d

M
T
S
L

-
c
a
f
i
t
l
u
m
e
h
t

g
n
i
t
c
i
d

y
g
r
e
n
e

c
i
r
t
c
e
l
e

d
e
t
e

a

n
i

n
o
i
t
p
m
u
s
n
o
c

g
n
i
d
l
i
u
b

t
r
a
m
s

m
r
e
t

g
n
o
L

r
a
d
n
e
l
a
c

d
n
a

l
a
c
i
r
o
t
s
i
H

d
n
a

-

s
n
a
e
m
K
g
n
i
d
u
l
c
n
i

l
a
i
t
n
e
d
i
s
e
R
-
n
o
N

d
a
o
l

r
e
w
o
p

g
n
i
d
l
i
u
b
A

)
0
2
0
2
(

.
l
a

t
e

l
a
p
e
N

a
t
a
d

A
M
R
A

I

d
i
r
b
y
h

a

g
n
i
s
u

y
g
e

-
t
a
r
t
s

n
o
i
t
a
m

i
t
s
e

h
c
a
o
r
p
p
a

)
d
e
u
n
i
t
n
o
c
(

5
e
l
b
a
T

1 3

)

%

(

e
g
a
t
n
e
c
r
e
P

80%

70%

60%

50%

40%

30%

20%

10%

0%

72%

Page 25 of 33  35

18%

Non-Residential

Residential

Building type

10%

Both

Fig. 4   Comparison chart between building type

Zhao and Magoules 2020; Ma et al. 2019), and only one study (Das et al. 2020) considered
building design.

From  the  statistical  report  of  this  review  paper,  about  72%  of  the  research  reviewed
focused on developing methods to predict building energy use in non-residential buildings,
18% on residential buildings, and just 10% on both. It is depicted in Fig. 4.

Regarding  the  forecast  horizon,  about  68%  of  the  studies  focused  on  short-term  fore-
casts,  27%  on  long-term  forecasts,  and  5%  on  medium-term  forecasts.  A  comparison  of
building types and prediction horizon is shown in Fig. 5. This explains the increasing use
of demand-side management strategies such as shifting of load, which allows the loads to
shift from peak hours to off-peak hours and knowing the energy consumption of building
for 24 h. It should be noted that the short-term horizon has expanded in recent studies since
it has proven to be quite useful in predicting the supply of energy resources in buildings.

About 54% of the research focused on the use of calendar and historical data in predic-
tion methods, 41% focused on the use of weather, calendar data, and historical and 3% on
historical, occupancy rates and focusing on the use of calendar data. Only 2% of the stud-
ies  used  calendar,  weather,  occupancy,  and  historical  data.  These  phenomena  may  arise
from the  reliance on diverse sensors to  capture  building energy  consumption, while data

e
g
a
t
n
e
c
r
e
P

50%
45%
40%
35%
30%
25%
20%
15%
10%
5%
0%

47%

10%

11%

5%

0%

0%

14%

9%

4%

Short-term

Medium-term

Long-term

Residential

Non-Residential

Both

Forecasting Horizon

Fig. 5   Comparison chart between type of building and Forecast horizon

Intelligent deep learning techniques for energy consumption…1 3
35  Page 26 of 33

R. Mathumitha et al.

)

%

(

e
g
a
t
n
e
c
r
e
P

40%

30%

20%

10%

0%

35%

32%

12%

7%

6 %

3%

3%

0%

0%

0%

2%

0%

His+cal

His+cal+wea

His+cal+occ

His+cal+occ+wea

Residential

Non-Residential

Both

Fig. 6   Comparison chart between type of building and input parameters. His indicates Historical, cal indi-
cates calendar, wea represents weather, and occ indicates Occupancy

concerning occupancy often remains unaccounted for due to the intricate data acquisition
process, which can vary based on the building’s characteristics. In Fig. 6. comparison chart
between the type of building and input parameters was given. On the other hand, the avail-
ability of this data will further improve the accuracy of the predictions.

In  summary,  the  analysis  of  methodologies  for  energy  consumption  forecasting  has
revealed  the  prominence  of  deep  learning,  the  importance  of  feature  selection,  and  the
influence of weather and occupancy patterns. There is a need for real-time data integration,
the  adoption  of  ensemble  and  hybrid  models,  the  emphasis  on  explainability  and  behav-
ioral  insights,  and  the  consideration  of  energy  efficiency  measures.  These  findings  and
observations collectively contribute to the advancement of accurate and actionable energy
consumption forecasts for smart buildings. The novel deep learning architectures, includ-
ing  CNN-LSTM,  CNN-LSTM  autoencoders,  and  TCN,  have  been  proposed  to  address
the  complexities  of  energy  consumption  time  series  data  and  to  achieve  better  forecast-
ing results. While machine learning algorithms have advanced the field of energy forecast-
ing, challenges remain, particularly in peak load prediction. Ongoing research focuses on
improving the accuracy of these models and addressing their limitations.

These findings and insights reflect the dynamic nature of the field of power forecasting,
with  researchers  continually  developing  and  refining  methodologies  to  address  the  com-
plexities  of  energy  consumption  and  integrate  renewable  energy  sources  for  a  more  sus-
tainable energy system. These critical observations reflect the ongoing evolution of energy
forecasting methodologies, with a focus on enhancing accuracy, addressing challenges, and
adapting to the changing energy landscape.

8   Research gap

Energy  demand  forecasting  is  a  useful  tool  for  identifying,  measuring,  and  managing
demand  flexibility.  Nowadays,  renewable  resources  play  a  vital  role  in  energy  genera-
tion. The review of such vast existing research work suggested the necessity to address the
obstacles in the future. Further research work needs to focus on the following:

Research  gap-1  A  key  component  that  reduces  the  prediction  accuracy  is  the  weather
(temperature,  humidity,  etc.).  Therefore,  future  studies  should  concentrate  on  the
impact of weather variables on power forecasting and incorporate weather components

1 3

Page 27 of 33  35

by analyzing the contribution and impact of each variable on the consumption profile.
(Mocanu et al. 2016).
Implication-1  A  deeper  understanding  of  how  weather  influences  power  consumption
can  lead  to  more  energy-efficient  practices.  For  instance,  businesses  and  households
can  optimize  their  energy  use  by  adjusting  their  consumption  patterns  in  response  to
weather forecasts, potentially reducing costs and environmental impact.
Avenues  -1  A  detailed  analysis  is  needed  about,  how  weather-informed  forecasts  can
optimize energy storage systems. To determine how renewable energy generation can be
better aligned with weather patterns to match demand. A Study needs how consumers
respond to weather-informed energy consumption predictions. To investigate the effec-
tiveness of behavioral interventions based on weather forecasts in reducing energy con-
sumption.
Research  gap-2  Based  on  the  knowledge  from  the  works  of  literature,  no  study  takes
into account the functionality of the buildings in terms of space and share percentages,
nor is there one that uses ML approaches and future weather scenarios to evaluate the
effects  of  global  climatic  change  on  the  energy  performance  of  urban  buildings.  This
will be a worthwhile area for research.
Implication-2 Research in this area can contribute to more sustainable urban develop-
ment by optimizing the energy performance of buildings, which is crucial for reducing
carbon emissions and mitigating the effects of climate change in urban areas.
Avenues-2  To  develop  and  refine  energy  simulation  models  that  incorporate  detailed
building functionality data, real-world weather scenarios, and ML techniques for accu-
rate  predictions  of  energy  consumption.  The  creation  of  databases  that  consolidate
building functionality data, historical weather data, and building energy usage data.
Research  gap-3  Future  lines  of  research  should  encourage  considering  various  time
scales, different environmental conditions, and various horizons like hours, months, and
years. To enable the efficient use of electrical energy across various industries and smart
grids, these horizons can be used (Mocanu et al. 2016).
Implication-3  This  research  approach  promotes  multi-temporal  energy  planning  that
spans  various  time  scales.  It  enables  utilities,  industries,  and  smart  grid  operators  to
develop comprehensive strategies for optimizing energy use, production, and distribu-
tion. For long-term forecasts, the model needs a huge number of data to make efficient
predictions. Therefore, research in this area can drive the development of data collection
technologies and data analytics tools that are tailored to various time scales and environ-
mental conditions. Addressing different time horizons allows for more accurate energy
demand forecasting. Short-term forecasts (hours) help manage grid stability, while long-
term forecasts (months and years) inform infrastructure investments.
Avenues-3  Invest  in  advanced  data  collection  and  data  analytics  tools  to  process  and
analyze diverse data sources, enabling precise multi-temporal forecasting and decision-
making.
Research gap4- Challenges such as compensation for forecasting errors, problems with
dynamic  model  selection,  the  creation  of  adaptive  predictive  models,  and  data  integ-
rity  must  be  addressed  by  current  techniques.  (Singh  and  Dwivedi  2018).  Improving
energy management requires achieving high accuracy in the use of energy forecasts. In
any  instance,  this  necessitates  the  selection  of  appropriate  estimating  models  that  are
prepared to capture each of the predicted array’s features, which is a task fraught with
uncertainty (Wen et al. 2020).
Implication 4 Improving the accuracy of energy forecasts can enhance grid stability and
resilience. Grid operators can better anticipate demand fluctuations, reducing the risk of

Intelligent deep learning techniques for energy consumption…1 335  Page 28 of 33

R. Mathumitha et al.

blackouts and ensuring the reliability of energy supply, even in the face of unexpected
events. Energy markets rely on accurate energy forecasts. Addressing these challenges
can lead to more efficient market operations, better matching supply and demand, and
potentially reducing price volatility.
Avenues-4 Developing advanced forecasting models that integrate dynamic model selec-
tion and adaptive predictive capabilities to improve forecasting accuracy and robustness
in the face of changing conditions.
Research  gap-5  Most  research  has  been  done  on  predicting  power  usage  in  a  single
building, but there hasn’t been much done to aggregate the power usage across a wider
area using a large number of data samples to assure the model’s accuracy.
Implication-5 Accurate and aggregated energy data can facilitate the design of targeted
energy  efficiency  programs  that  address  the  specific  needs  of  a  region  or  community,
resulting in reduced energy waste. By aggregating data, it becomes easier to manage the
integration of renewable energy sources into the grid. This research can lead to better
strategies for balancing energy supply and demand.
Avenues-5  Develop  real-time  monitoring  and  control  systems  that  provide  actionable
insights  and  allow  for  dynamic  adjustments  in  energy  use  and  distribution  based  on
aggregated data. Most of the real-time datasets are not publicly available on the website.
So there is a need for a benchmark dataset for this domain.

 The identified research gaps in the area of energy consumption forecasting have significant
implications for improving the accuracy and sustainability of energy management. Focus-
ing on the impact of weather variables, integrating building functionality with DL, address-
ing long-term forecasting challenges, and considering various time scales can lead to more
precise  predictions,,  better  energy  planning,  and  enhanced  grid  efficiency.  The  identified
gaps impact the field by reducing the accuracy and efficiency of energy consumption fore-
casts in smart buildings. Inaccurate forecasts can result in suboptimal energy management,
increased costs, and a failure to meet peak demand. Research in this area can support smart
city initiatives by providing accurate and comprehensive data on energy consumption pat-
terns across various sectors, enabling better urban planning and resource allocation.

9   Conclusion

The 40% rise in the amount of electricity used in residential and commercial is because of
the recent increase in urbanization. Accurately predicting electricity demand has become
crucial. Forecasting can be used to meet the supply and demand gap for electrical energy.
Since it helps decision-makers and planners in government, this forecast is important on a
global scale. To increase the accuracy of energy consumption predictions, new automated
paradigms  are  required.  This  paper  reviews  the  recent  advanced  forecasting  methods.
While analyzing other methods, DL gives better results. DNN has recently been effectively
used in this context. Furthermore, the study provides taxonomies for these methodologies
based  on  various  forecasting  horizons  and  data  sources  utilized  to  predict  future  energy
usage. As a result, this assessment can help researchers identify research gaps that require
addressing in the future and come up with novel approaches to enhance power forecasting
in  commercial  and  residential  buildings.  This  review  paper  presented  the  significance  of
smart meter data for energy forecasting. Researchers can take the initiative to extract use-
ful information from the smart meter for the benefit of society. The review of prior works

1 3
Page 29 of 33  35

will provide useful guidance to future researchers. Based on the continuation of this review
paper, a novel hybrid deep learning approach will be proposed for improving forecasting
accuracy in residential buildings from short to long term horizon.

Author contributions  RM prepared the Tables and figures; PR prepared the content and KM designed the
research gap.

Declarations

Conflict of interest  The authors declare no competing interests.

Open  Access  This  article  is  licensed  under  a  Creative  Commons  Attribution  4.0  International  License,
which  permits  use,  sharing,  adaptation,  distribution  and  reproduction  in  any  medium  or  format,  as  long
as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Com-
mons licence,  and indicate if changes were made. The images or other third party material in this article
are  included  in  the  article’s  Creative  Commons  licence,  unless  indicated  otherwise  in  a  credit  line  to  the
material. If material is not included in the article’s Creative Commons licence and your intended use is not
permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly
from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

References

Abuella  M,  Chowdhury  B  (2017)  Random  forest  ensemble  of  support  vector  regression  models  for  solar
power forecasting. In: 2017 IEEE power & energy society innovative smart grid technologies confer-
ence (ISGT). IEEE Xplore. https:// doi. org/ 10. 1109/ ISGT. 2017. 80860 27.

Afrasiabi  M  et  al  (2020)  Deep-based  conditional  probability  density  function  forecasting  of  residential

loads. IEEE Trans Smart Grid 11:3646–3657

Agyeman KA, Kim G, Jo H, Park S, Han S (2020) An ensemble stochastic forecasting framework for vari-

able distributed demand loads. Energies. https:// doi. org/ 10. 3390/ en131 02658

Akter R et al (2021) Analysis and prediction of hourly energy consumption based on long short-term mem-
ory  neural  network.  In:  2021  ınternational  conference  on  ınformation  networking  (ICOIN).  IEEE
Xplore. https:// doi. org/ 10. 1109/ ICOIN 50884. 2021. 93339 68

Alhussein M et al (2020) Hybrid CNN-LSTM model for short-term individual household load forecasting.

IEEE Access 8:180544–180557. https:// doi. org/ 10. 1109/ ACCESS. 2020. 30282 81

Ali  U,  Buccella  C,  Cecati  C  (2016)  Households  electricity  consumption  analysis  with  data  mining  tech-

niques. In: IECON Proceedings of the Industrial Electronic Conference, pp. 3966–3971

Amasyali K, El-Gohary NM (2018) A review of data-driven building energy consumption prediction stud-

ies. Renew Sustain Energy Rev 81:1192–1205. https:// doi. org/ 10. 1016/j. rser. 2017. 04. 095

Antonopoulos I et al (2021) Data-driven modelling of energy demand response behaviour based on a large-

scale residential trial. Energy and AI 4:100071. https:// doi. org/ 10. 1016/j. egyai. 2021. 100071

El Astal M-T et al. (2020) Office appliances ıdentification and monitoring using deep leaning based energy
disaggregation for smart buildings. In: IECON 2020 the 46th annual conference of the IEEE ındustrial
electronics society. https:// doi. org/ 10. 1109/ IECON 43393. 2020. 92551 27

Bandic L, Kevric J (2018) Near zero-energy home prediction of appliances energy consumption using the
reduced  set  of  features  and  random  decision  tree  algorithms.  Proc.  Int.  Symp.  Innov.  Interdiscipl.
Appl. Adv. Technol. Cham. 59:164–171

Behera DK et al (2022) XGBoost regression model-based electricity tariff plan recommendation in smart
grid environment. Int J Innovative Comput Appl 13:79–87. https:// doi. org/ 10. 1504/ ijica. 2022. 123223

Bhosale H, Gadekar D (2014) A review paper on big data and Hadoop. Int J Sci Res 4:1–7
Cai H, Shen S et al (2019) Predicting the energy consumption of residential buildings for regional electricity

supply-side and demand-side management. IEEE Access 7:30386–30397

Chen  R  et  al  (2022)  MultiCycleNet:  multiple  cycles  self-boosted  neural  network  for  short-term  electric

household load forecasting. Sustain Cities Soc 76:103484. https:// doi. org/ 10. 1016/j. scs. 2021. 103484
Cheng J, Li Q (2008) Reliability analysis of structures using artificial neural network based genetic algo-

rithms. Comput Methods Appl Mech Eng 197:3742–3750

Intelligent deep learning techniques for energy consumption…1 335  Page 30 of 33

R. Mathumitha et al.

Choksi KA, Jain S, Pindoriya NM (2020) Feature based clustering technique for investigation of domestic
load profiles and probabilistic variation assessment: smart meter dataset. Sustain Energy Grids Netw
22:1–11

Cui  L  et  al  (2023)  Intelligent  power  grid  energy  supply  forecasting  and  economic  operation  management
using  the  snake  optimizer  algorithm  with  Bigur-attention  model.  Front.  Energy  Res.  11:1273947.
https:// doi. org/ 10. 3389/ fenrg. 2023. 12739 47

Dahunsi FM, Olawumi AE et al (2021) A systematic review of data pre-processing methods and unsuper-
vised  mining  methods  used  in  profiling  smart  meter  data.  AIMS  Electron  Electr  Eng  5:284–314.
https:// doi. org/ 10. 3934/ elect reng. 20210 15

Das A et al (2020) Occupant-centric miscellaneous electric loads prediction in buildings using state-of-
the-art deep learning methods. Elsevier Appl Energy 269:115–135. https:// doi. org/ 10. 1016/j. apene
rgy. 2020. 115135

Dehalwar  V  et  al.  (2017)  Electricity  load  forecasting  for  urban  area  using  weather  forecast.  In:  2016
IEEE ınternational conference on power and renewable energy (ICPRE). IEEE Xplore. https:// doi.
org/ 10. 1109/ ICPRE. 2016. 78712 31

Dong C, Du L, Ji F, Song Z, Zheng Y et al. (2018) Forecasting smart meter energy usage using distrib-
uted systems and machine learning. In: IEEE 20th international conference on high performance
computing and communications. https:// doi. org/ 10. 1109/ HPCC/ Smart City/ DSS. 2018. 00216
Ellabban O, Alassi A (2019) Integrated economic adoption model for residential grid-connected photo-
voltaic  systems:  an  Australian  case  study.  Energy  Rep  5:310–326.  https:// doi. org/ 10. 1016/j. egyr.
2019. 02. 004

Egrioglu  E  et  al  (2015)  Recurrent  multiplicative  neuron  model  artificial  neural  network  for  non-
time  series  forecasting.  Neural  Proces  Lett  41:249–258.  https:// doi. org/ 10. 1007/

linear
s11063- 014- 9342-0

Farzana  S  et  al  (2014)  Multi-model  prediction  and  simulation  of  residential  building  energy  in  urban

areas of Chongqing, South West China. Energy Build 81:161–169

Fu G (2018) Deep belief network based ensemble approach for cooling load forecasting of air-condition-

ing system. Elsevier Energy 148:269–282. https:// doi. org/ 10. 1016/j. energy. 2018. 01. 180

Gao PX et al (2012) On hourly home peak load prediction. 2012 IEEE Third İnt Conf Smart Grid Com-

mun. https:// doi. org/ 10. 1109/ Smart GridC omm. 2012. 64859 77

Ghimire S et al (2023) A novel approach based on integration of convolutional neural networks and echo
state  network  for  daily  electricity  demand  prediction.  Energy.  https:// doi. org/ 10. 1016/j. energy.
2023. 127430

Gupta R, Al-Ali AR, Zualkernana IA, Das SK (2020) Big data energy management, analytics and visu-

alization for residential areas. IEEE Access 8:156153–156164

Harb H et al (2016) Development and validation of grey-box models for forecasting the thermal response

of occupied buildings. Energy Build 117:199–207. https:// doi. org/ 10. 1016/j. enbui ld. 2016. 02. 021

Himeur Y et al (2020a) A novel approach for detecting anomalous energy consumption based on micro-

moments and deep neural networks. Cogn Comput 12:1387–1401

Himeur  Y  et  al  (2020b)  Effective  non-intrusive  load  monitoring  of  buildings  based  on  a  novel  multi-
descriptor  fusion  with  dimensionality  reduction.  Appl  Energy  279:115872.  https:// doi. org/ 10.
1016/j. apene rgy. 2020. 115872

https:// www. elect ronics- notes. com/ artic les/ eco- green- engin eering/ smart- energy- meters/ smart- meter-

elect ronic- circu it- design. php

https:// data. gov. au/ datas et/ ds- dga- 4e21d ea3- 9b87- 4610- 94c7- 15a8a 77907 ef/ detai ls
https:// www. nature. com/ artic les/ sdata 201848
https:// www. ceicd ata. com/ en/ korea/ elect ricity- gener  ation- and- consu mption/ elect ricity- consu mption-
seoul#: ~: text= Korea% 20Ele ctric ity% 3A% 20Con sumpt ion% 3A% 20Seo ul% 20data% 20is% 20upd
ated% 20mon thly% 2C% 20ave ragin g,kWh% 20mn% 20in% 20May% 201998
https:// www. kaggle. com/ datas ets/ jehan bhath ena/ smart- meter- data- mathu ra- and- barei lly
https:// www. ausgr id. com. au/ Indus  try/ Our- Resea rch/ Data- to- share/ Solar- home- elect ricity- data
Imani M, Ghassemian H (2019) Residential load forecasting using wavelet and collaborative representa-
tion transforms. Appl Energy 253:113505. https:// doi. org/ 10. 1016/j. apene rgy. 2019. 113505

Islam  SN  et  al.  (2020)  Load  profile  segmentation  using  residential  energy  consumption  data.  In:  2020
ınternational conference on smart grids and energy systems (SGES). IEEE Xplore. https:// doi. org/
10. 1109/ SGES5 1519. 2020. 00112

Jain S, Choksi KA, Pindoriya NM (2019) Rule-based classification of energy theft and anomalies in con-

sumers load demand profile. IET Smart Grid 2:612–624

Jaiswal  DM,  Thakre  MP  (2022)  Modeling  &  designing  of  smart  energy  meter  for  smart  grid  applica-

tions. Glob Transitions Proc 3:311–316. https:// doi. org/ 10. 1016/j. gltp. 2022. 03. 017

1 3

Page 31 of 33  35

Kaur  H,  Ahuja  S  (2017)  Time  series  analysis  and  prediction  of  electricity  consumption  of  health  care
institution using ARIMA model. Proceedings of sixth international conference on soft computing
for problem solving. Springer

Kell  AJM  et  al  (2023)  Optimizing  a  domestic  battery  and  solar  photovoltaic  system  with  deep  rein-
forcement learning. In: 2022 IEEE ınternational conference on big data (big data). IEEE Xplore.
https:// doi. org/ 10. 1109/ BigDa ta556 60. 2022. 10021 028

Khan  S  et  al  (2019)  Electricity  load  forecasting  for  each  day  of  week  using  deep  CNN.  Advances  in

intelligent systems and computing. Springer, pp 1107–1119

Khan  ZA  et  al  (2020a)  Towards  efficient  electricity  forecasting  in  residential  and  commercial  buildings:
a  novel  hybrid  CNN  with  a  LSTM-AE  based  framework.  Sensors  20:1399.  https:// doi. org/ 10. 3390/
s2005 1399

Khan ZA et al (2020b) Electrical energy prediction in residential buildings for short-term horizons using

hybrid deep learning strategy. Appl Sci 10:8634. https:// doi. org/ 10. 3390/ app10 238634

Khan ZA et al (2023) Modelling electricity consumption during the COVID19 pandemic: datasets, models,
results  and  a  research  agenda.  Energy  and  Buildings  294:113204.  https:// doi. org/ 10. 1016/j. enbui ld.
2023. 113204

Kim T-Y, Cho S-B (2019b) Predicting residential energy consumption using CNN-LSTM neural networks.

Energy 182:72–81

Kim M, Choi W, Jeon Y, Liu L et al (2019) A hybrid neural network model for power demand forecasting.

Energies 12:931. https:// doi. org/ 10. 3390/ en120 50931

Kiprijanovska I, Stankoski S, Ilievski I, Jovanovski S, Gams M et al (2020) Day-ahead household electrical

energy consumption forecasting using deep learning. Energies. https:// doi. org/ 10. 3390/ en131 02672

Kolehmainen  M,  Mononen  M,  Niska  H  (2015)  A  data  mining  approach  for  producing  small  area  sta-
tistics-based  load  profiles  for  distribution  network  planning.  IEEE  Int  Conf  Industrial  Technol
2015:1236–1240

Lara-benitez P (2020) Temporal convolutional networks applied to energy-related series forecasting. Appl

Sci. https:// doi. org/ 10. 3390/ app10 072322

Le T et al (2020) Multiple electric energy consumption forecasting using a cluster-based strategy for transfer

learning in smart building. Sensors 20:2668. https:// doi. org/ 10. 3390/ s2009 2668

Li K et al (2015) Building’s electricity consumption prediction using optimized artificial neural networks
and principal component analysis. Energy Build 108:106–113. https:// doi. org/ 10. 1016/j. enbui ld. 2015.
09. 002

Liu  T,  Liu  K,  Fang  P,  Zhao  J  (2016)  A  hybrid  model  of  AR  and  PNN  method  for  building  thermal  load
forecasting.  Theory,  methodology,  tools  and  applications  for  modeling  and  simulation  of  complex
systems, vol 643. Springer, pp 146–155

Liu T, Tan Z, Chengliang Xu, Chen H, Li Z (2020) Study on deep reinforcement learning techniques for
building  energy  consumption  forecasting.  Energy  Build.  https:// doi. org/ 10. 1016/j. enbui ld. 2019.
109675

Liu  M  et  al  (2022)  Short-term  load  forecasting  based  on  improved  TCN  and  DenseNet.  IEEE  Access

10:115945–115957

Ma Z, Zhang C, Zhang C (2019) Review of machine learning applications in power system. In: 2019 IEEE
ınnovative smart grid technologies—Asia (ISGT Asia). IEEE Xplore. https:// doi. org/ 10. 1109/ ISGT-
Asia. 2019. 88813 30.

Makonin  S  (2019)  HUE:  the  hourly  usage  of  energy  dataset  for  buildings  in  British  Columbia.  Harvard

Dataverse 23:103774. https:// doi. org/ 10. 7910/ DVN/ N3HGRN

Manembu P, Engineering I, Nielsen PS, et al. (2018) Multi-grained household load profile analysis using
smart  meter  data  :  the  case  of  Indonesia.  In:  2018  2nd  Borneo  international  conference  on  applied
mathematics and engineering (BICAME), pp. 213–217.

Mawson VJ et al (2020) Deep learning techniques for energy forecasting and condition monitoring in the
manufacturing sector. Energy Build 217: 109966. https:// doi. org/ 10. 1016/j. enbui ld. 2020. 109966
Mocanu E, Nguyen PH, Gibescu M, Kling WL (2016) Deep learning for estimating building energy con-

sumption. Sustain Energy Grids Net 6:91–99

Moldovan  D,  Slowik  A  (2021)  Energy  consumption  prediction  of  appliances  using  machine  learning  and
multi-objective binary grey wolf optimization for feature selection. Appl Soft Comput 111:107745.
https:// doi. org/ 10. 1016/j. asoc. 2021. 107745

Mujeeb S et al (2021) Electricity theft detection with automatic labeling and enhanced RUSBoost classifica-
tion using differential evolution and jaya algorithm. IEEE Access 9:128521–128539. https:// doi. org/
10. 1109/ ACCESS. 2021. 31026 43

Munkhdalai L, Munkhdalai T et al (2019) An endto-end adaptive input selection with dynamic weights for

forecasting multivariate time series. IEEE Access 7:99099–99114

Intelligent deep learning techniques for energy consumption…1 335  Page 32 of 33

R. Mathumitha et al.

Munoz O, Ruelas A et al (2022) Design and development of an IoT smart meter with load control for home
energy management systems. Smart IoT Syst Renew Energy Resour 22:7536. https:// doi. org/ 10. 3390/
s2219 7536

Naz A et al (2019) Short-term electric load and price forecasting using enhanced extreme learning machine

optimization in smart grids. Energies 12:866. https:// doi. org/ 10. 3390/ en120 50866

Nepal B et al (2020) Electricity load forecasting using clustering and ARIMA model for energy manage-

ment in buildings. Jpn Archit Rev 3:62–76. https:// doi. org/ 10. 1002/ 2475- 8876. 12135

Osama S et al (2019) An efficient algorithm for extracting appliance-time association using smart meter

data. Heliyon 5:e02226. https:// doi. org/ 10. 1016/j. heliy  on. 2019. e02226

Paraskevas  L  et  al  (2021)  Domestic  smart  metering  infrastructure  and  a  method  for  home  appliances

identification using low-rate power consumption data. IET Smart Cities 3:91–106
Pascanu R et al. (2013) How to construct deep recurrent neural networks. arXiv preprint.
Pirbazari AM, Sharma E et al (2021) An ensemble approach for multi-step ahead energy forecasting of

household communities. IEEE Access 9:36218–36240

Polamuri  SR  et  al  (2022)  Multi-model  generative  adversarial  network  hybrid  prediction  algo-
rithm  (MMGAN-HPA)  for  stock  market  prices  prediction.  J  King  Saud  Univ—Comput  Inf  Sci
34:7433–7444

Prakash A, Xu S, Rajagopal R, Noh HR (2018) Building energy load forecasting using physically-based

Kernel models. Energies 11:862. https:// doi. org/ 10. 3390/ en110 40862

Rahman A, Srikumar V, Smith AD (2008) Predicting electricity consumption for commercial and resi-

dential buildings using deep recurrent neural networks. Appl Energy 212:372–385

Rashid H et al. (2021) Evaluation of non-intrusive load monitoring algorithms for appliance-level anom-
aly  detection.  In:  ICASSP  2019—2019  IEEE  ınternational  conference  on  acoustics,  speech  and
signal processing. IEEE Xplore. https:// doi. org/ 10. 1109/ ICASSP. 2019. 86837 92

Renaux  DPB  et  al  (2020)  A  dataset  for  non-ıntrusive  load  monitoring:  design  and  implementation:

energy data analytics for smart meter data. Energies. https:// doi. org/ 10. 3390/ en132 05371

Rick R, Berton L (2020) Energy forecasting model based on CNN-LSTM-AE for many time series with

unequal lengths. Eng Appl Artif Intell. https:// doi. org/ 10. 1016/j. engap pai. 2022. 104998

Sajjad M et al (2020) A novel CNN-GRU-based hybrid approach for short-term residential load forecast-

ing. IEEE Access 8:143759–143768

Singh P, Dwivedi P (2018) Integration of new evolutionary approach with artificial neural network for

solving short term load forecast problem. Appl Energy 217:537–549

Singh  S,  Yassine  A  (2018)  Big  data  mining  of  energy  time  series  for  behavioral  analytics  and  energy

consumption forecasting. Energies 11:458. https:// doi. org/ 10. 3390/ en110 20452

Singh S, Yassine A (2019) Mining energy consumption behavior patterns for households in smart grid.

IEEE Trans Emerg Topic Comput 7:404–419

Somu N et al (2020) A hybrid model for building energy consumption forecasting using long short term
memory networks. Appl Energy 261:114131. https:// doi. org/ 10. 1016/j. apene rgy. 2019. 114131
Spiliotis E et al (2020) Cross-temporal aggregation: Improving the forecast accuracy of hierarchical elec-
tricity consumption. Appl Energy 261:114339. https:// doi. org/ 10. 1016/j. apene rgy. 2019. 114339
Sulaiman SM, Aruna Jeyanthy P, Devaraj D, Shihabudheen KV (2022) A novel hybrid short-term elec-
tricity forecasting technique for residential loads using empirical mode decomposition and extreme
learning  machines.  Comput  Electr  Eng  98:107663.  https:// doi. org/ 10. 1016/j. compe leceng. 2021.
107663

Sun  G  et  al  (2020)  Short-term  building  load  forecast  based  on  a  data-mining  feature  selection  and

LSTM-RNN method. IEEJ Trans Electr Electron Eng. https:// doi. org/ 10. 1002/ tee. 23144

Sunny MR et al. (2021). Residential energy management: a machine learning perspective. In: 2020 IEEE
green  technologies  conference  (GreenTech).  IEEE  Xplore.  https:// doi. org/ 10. 1109/ Green  Tech4
6478. 2020. 92897 37

Tekler  ZD  et  al  (2020)  ROBOD,  room-level  occupancy  and  building  operation  dataset.  Build  Simul

15:2127–2137

Todic T et al (2023) An active learning framework for the low-frequency non-intrusive load monitoring

problem. Appl Energy 341:121078. https:// doi. org/ 10. 1016/j. apene rgy. 2023. 121078

Tokgoz  A,  Unal  G  (2018)  A  RNN  based  time  series  approach  for  forecasting  turkish  electricity  load.
In: Proceedings of the 26th signal processing and communications applications conference (SIU).
https:// doi. org/ 10. 1109/ SIU. 2018. 84043 13.

Ullah  FUM  et  al  (2019)  Short-term  prediction  of  residential  power  energy  consumption  via  CNN  and

multi-layer bi-directional LSTM networks. IEEE Access 8:123369–123380

Wahab A et al (2021) A novel technique for short-term load forecasting using sequential models and fea-

ture engineering. IEEE Access 9:96221–96232. https:// doi. org/ 10. 1109/ ACCESS. 2021. 30934 81

1 3
Page 33 of 33  35

Wang Z, Srinivasan RS (2017) A review of artificial intelligence based building energy use prediction:
contrasting the capabilities of single and ensemble prediction models. Renew Sustain Energy Rev
75:796–808

Wang H et al (2016) Deep belief network based deterministic and probabilistic wind speed forecasting

approach. Appl Energy 182:80–93

Wang Y, Chen Q, Hong T et al (2018) Review of smart meter data analytics: applications, methodolo-

gies, and challenges. IEEE Trans Smart Grid 10:3125–3148

Wang Y et al (2019) Probabilistic individual load forecasting using pinball loss guided LSTM. Appl Energy

235:10–20

Wei  Y  et  al  (2019)  Prediction  of  occupancy  level  and  energy  consumption  in  office  building  using  blind

system identification and neural networks. Appl Energy 240:276–294

Wen  L,  Zhou  K,  Yang  S  (2020)  Load  demand  forecasting  of  residential  buildings  using  a  deep  learning

model. Electr Power Syst Res 179:106073. https:// doi. org/ 10. 1016/j. epsr. 2019. 106073

Xiang L et al (2020) Prediction model of household appliance energy consumption based on machine learn-

ing. J Phys: Conf Ser. https:// doi. org/ 10. 1088/ 1742- 6596/ 1453/1/ 012064

Xu L, Wang S, Tang R (2019) Probabilistic load forecasting for buildings considering weather forecasting
uncertainty  and  uncertain  peak  load.  Appl  Energy  237:180–195.  https:// doi. org/ 10. 1016/j. apene rgy.
2019. 01. 022

Yan K et al (2019) A hybrid LSTM neural network for energy consumption forecasting of individual house-

holds. IEEE Access 7:157633–157642

Zhang K et al (2015) Stock market prediction based on generative adversarial network. Procedia Comput

Sci 147:400–406

Zhang W, Dong X, Li H, Xu J, Wang D (2020a) Unsupervised detection of abnormal electricity consump-
tion  behavior  based  on  feature  engineering.  Artif  Intell  Technol  Electr  Power  Syst  8:55483–55500.
https:// doi. org/ 10. 1109/ ACCESS. 2020. 29800 79

Zhang G, Tian C, Li C, Zhang JJ, Zuo W (2020b) Accurate forecasting of building energy consumption via
a novel ensembled deep learning method considering the cyclic feature. Energy 201:117531. https://
doi. org/ 10. 1016/j. energy. 2020. 117531

Zhao H-X, Magoules F (2020) A review on the prediction of building energy consumption. Renew Sustain

Energy Rev 16:3586–4359

Zor  K,  Çelik  Ö,  Timur  O,  Teke  A  (2020)  Short-term  building  electrical  energy  consumption  forecasting
by employing gene expression programming and GMDH networks. Energies. https:// doi. org/ 10. 3390/
en130 51102

Publisher’s Note  Springer Nature remains neutral with regard to jurisdictional claims in published maps and
institutional affiliations.

Intelligent deep learning techniques for energy consumption…1 3