Journal of Basic and Applied Research International

Volume 30, Issue 6, Page 140-157, 2024; Article no.JOBARI.12619
ISSN: 2395-3438 (P), ISSN: 2395-3446 (O)

A Survey of Time Series Data
Forecasting Methods Based on Deep
Learning

Jiahui Chen a, Tao Chen a, Yishui Wang a
and Lidong Wang a*

a School of Engineering, Hangzhou Normal University, 310018, Hangzhou, Zhejiang, China.

Authors’ contributions

This work was carried out in collaboration among all authors. Authors JC and TC designed the study,
performed the statistical analysis and wrote the first draft of the manuscript. Authors YW and LW
managed the analyses of the study. Author LW managed the literature searches. All authors read and
approved the final manuscript.

Article Information

DOI: https://doi.org/10.56557/jobari/2024/v30i69014

Open Peer Review History:
This journal follows the Advanced Open Peer Review policy. Identity of the Reviewers, Editor(s) and additional Reviewers,
peer review comments, different versions of the manuscript, comments of the editors, etc are available here:

https://prh.ikprress.org/review-history/12619

Review Article

ABSTRACT

Received: 17/10/2024
Accepted: 20/12/2024
Published: 27/12/2024

Time Series Forecasting (TSF) involves predicting future values and trends of data at specific points
or periods by analyzing historical patterns, such as trends and seasonality. With the advent of IoT
sensors, traditional machine learning approaches struggle to handle massive time series datasets.
Recently, deep learning algorithms, exemplified by convolutional neural networks (CNNs), recurrent
neural  networks  (RNNs),  and  Transformer  models,  have  made  significant  progress  in  time  series
forecasting tasks. This paper reviews the common features of time series data, relevant  datasets,
and evaluation metrics for models. It also conducts experimental comparisons of various forecasting
algorithms,  focusing  on  time  and  algorithmic  architectures.  This  paper  conducts  prediction
experiments on several deep learning models using the ETT dataset and presents the final results.
_____________________________________________________________________________________________________

*Corresponding author: E-mail: wld@hznu.edu.cn;

Cite as: Chen, Jiahui, Tao Chen, Yishui Wang, and Lidong Wang. 2024. “A Survey of Time Series Data Forecasting Methods
Based on Deep Learning”. Journal of Basic and Applied Research International 30 (6):140-57.
https://doi.org/10.56557/jobari/2024/v30i69014.

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619

We evaluate model performance using metrics like Mean Absolute Error (MAE) and Mean Squared
Error  (MSE). We  highlight  the  strengths  and  weaknesses  of  deep  learning-based  TSF  methods.
Major deep learning-based time series forecasting methods are introduced and compared. Finally,
challenges  and  future  research  directions  in  applying  deep  learning  to  time  series  forecasting  are
discussed.

Keywords:  Deep  learning;  time  series  forecasting;  recurrent  neural  networks;  gated  recurrent  units;

transformer model.

1. INTRODUCTION

Time  series  data  exist  widely  in  domains  like
finance,  healthcare,  energy,  transportation,  and
meteorology and are easily accessible. However,
with the  widespread use  of sensing devices  and
advancements  in  data  processing,  time  series
data  are  being  generated  at  an  explosive  rate.
Analyzing  these  data  is  crucial  for  extracting
as  weather
valuable
forecasts,
predictions,
financial
analysis,
trend  monitoring,  medical
responses,  and  system  workload  management
(Eslin & Agon, 2012).

information,
traffic

such

flow

flu

trees,

random

seasonality,

to  weather

dependence,

learning  methods
forests,  and
to

Time  Series  Forecasting  is  a  critical  tool  for
making  predictions  based  on  historical  data  that
is  collected  over  time.  By  leveraging  various
learning  models,
statistical  and  machine
businesses  and  researchers  can  predict  future
events,  trends,  and  behaviors  in  areas  ranging
forecasting.  While
from
finance
(like
traditional  machine
decision
linear
regression)  can  be  applied
time  series
forecasting,  they  face  significant  challenges  due
to the unique nature of time series data, including
temporal
non-
stationarity,  and  the  need  for  careful  feature
require
engineering.  These  methods  often
substantial
feature
engineering  to  capture  the  temporal  patterns.
Specifically, traditional statistical models, such as
Support
and
Autoregressive
Models
manual  configuration  of  seasonal  and  trend
components  (Gers  et  al.,  2000;  Durbin  &
Koopman,  2012),  limiting  their  efficiency  and
accuracy  with
large-scale  datasets.  Deep
neural  networks  (DNNs)  offer  an  alternative
due
to  extract  high-level
features and identify complex patterns within and
across  time  series  with  minimal  manual  effort.
However,  DNNs  require  extensive  training  data
fewer  structural
to
due
assumptions.

Vector  Machines

preprocessing

reliance  on

their  ability

(SVM)

(AR),

their

and

to

require

141

in

in

to

this

long-term

Convolutional  Neural  Networks  (CNNs),  as  one
of the most representative  network architectures
in  deep  learning  (Shaowei  et  al.,  2023),  hold
broad  application  prospects
field.
Compared
traditional  methods,  CNNs
feature
demonstrate  superior  capabilities
extraction  and  information  mining.  While  CNNs
are  highly  effective  for  processing  image  data,
they face limitations  when  applied to time series
data,  such  as  sequences,  speech,  and  text.
Specifically, CNNs struggle to capture long-range
dependencies in time series. Although increasing
the depth of convolutional layers can expand the
receptive  field,  it  often  remains  insufficient  for
modeling
dependencies  within
sequences.  In  1990,  Jeffrey  Elman  introduced
the
foundational  concept  and  structure  of
Recurrent  Neural  Networks  (RNNs)  in  his  paper
in  Time.  Elman's  model
Finding  Structure
introduced  the  concept  of  a  hidden  layer  (or
internal  state),  which  stores  information  about
previous  elements  in  a  sequence  and  uses  it  to
predict  the  next  element.  This  breakthrough
opened  the  door  for  RNN  applications  in  natural
language  processing,  time  series  analysis,  and
other  domains.  Subsequently,  RNNs  evolved  to
address  issues  like  vanishing  and  exploding
gradients  in  long-sequence  processing  through
variants  such  as  Long  Short-Term  Memory
(LSTM)  networks  and  Gated  Recurrent  Units
(GRU).  In  2017,  Vaswani  et  al.  proposed  the
Transformer  architecture,  introducing  the  self-
attention  mechanism—a  key
that
enables
processing  sequence  data.  The  Transformer's
long-term
self-attention  mechanism  captures
dependencies,
of
addressing
traditional  RNNs  in  long-range  prediction  and
parallel  computation.  As  a  result,  Transformers
have  achieved  remarkable  performance  in  time
series forecasting tasks.

performance

exceptional

innovation

limitations

In  modern  domains,  time  series  forecasting
methods  are  already  well-established.  For
instance,  Facebook's  visual  interactive  network
(VIN)  employs  bidirectional  LSTM  to  effectively
capture  temporal  information  in  videos  (Michael

in

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619

et  al.,  2024).  Chinese  researchers  have  also
achieved  significant  results  in  tasks  such  as
image  captioning  and  video  classification.  For
example,  the  Chinese  Academy  of  Sciences
proposed  the  spatio-temporal  attention  network
(STAN),  which  uses  bidirectional  GRU
to
enhance video classification accuracy (Hanen et
al.,  2024).  Photovoltaics  (PV),  one  of  the  most
promising  renewable  energy  sources,  requires
accurate  power  forecasting  to  ensure  the  safe
operation  and  economic
integration  of  PV
systems  in  smart  grids.  Mohamed  Abdel-Nasser
et al. proposed an LSTM-RNN-based method for
predicting  PV  system  output  power,  providing  a
useful  tool  for  smart  grid  planning  and  control
(Abdel-Nasser  &  Mahmoud,  2019;  Qiang  et  al.,
2020).  Qiang  Cui  et  al.  introduced  a  Multi-View
Recurrent  Neural  Network  (MV-RNN)  model  to
handle  sequence  recommendations  and  cold-
start  issues.  By  integrating  visual  and  textual
information,  MV-RNN  mitigates
cold-start
problems,  dynamically  captures  user  interests,
generates  personalized  ranking  lists,  addresses
missing modality issues, and alleviates cold-start
challenges (Qiang et  al., 2020).  Shaowei Pan  et
al.  proposed  a  hybrid  model  (CNN-LSTM-SA),
combining  Convolutional  Neural  Networks
(CNNs),  LSTM  networks,  and  self-attention
mechanisms  (SA).  This  model  achieved  optimal
performance in capturing fundamental trends and
predicting  specific  values  for  oil  well  production
(Shaowei  et  al.,  2023).  In  the  field  of  speech
their  variants  have
recognition,  RNNs  and
achieved
For
breakthroughs.
example, Microsoft's deep neural network (DNN)
combined  with  LSTM  demonstrated  excellent
performance in speech recognition competitions.
Domestic  companies  such  as  iFLYTEK  and
also
Sogou
adopted  RNN-based
technologies
improve  speech  recognition
accuracy (Fang et al., 2021). In hydrological time
series  forecasting,  Muhammad  Waqas  et  al.
demonstrated  the  effectiveness  of  RNNs  and
LSTMs  in  modeling  nonlinear  and  time-varying
hydrological  systems,  making  them  a  research
hotspot
(Waqas  &  Humphries,  2024.  The
Transformer's self-attention mechanism excels in
long-range  dependencies,  offering
capturing
superior
temporal  modeling  capabilities  and
advantages in handling time series data (Wen et
al.,  2023).  Liu  et  al.  proposed  a  de-stationary
framework to address over-stabilization issues in
processing raw time series data (Liu et al., 2022).
Additionally,  Liu  et  al.  recently  introduced  an
inverted  input  approach  that  reassigns  roles
between
the
feedforward  neural  network  (Liu  et  al.,  2024),

the  attention  module  and

significant

have

to

to

learn

encodings

effectively enhancing SOTA model performance.
In  2023,  Zhang  et  al.    proposed  a  multi-scale
pyramid  Transformer  model  called  MTPNet
(Zhang  et  al.,  2024).  The  use  of  multi-layer
Transformer  structures  with  different  scales  has
solved  the  problem  of  time  dependent  modeling
for  fixed  or  constrained  scales.  Some  studies,
learnable
such  as  the  BERT  model,  adopt
position
positional
embeddings  from  time  series  through  training.
For  instance,  Jin  et  al.,  (2021)  proposed  the
TrafficBERT  model  for  traffic  flow  prediction.
Additionally,  Li  et  al.,  (2019)  replaced  traditional
position  encodings  with
learnable  position
embeddings  in  the  LogSparse  Transformer.  In
the
2021,  Wu  et  al.,
Autoformer  model,  which  is  a  self-correlation
long-term
decomposition
Transformer
forecasting.
attention
mechanisms  address  the  quadratic  complexity
issue,  they  limit  the  utilization  of  information.
Furthermore,  due
temporal
patterns  in  long-term  predictions,  self-attention
mechanisms
reliable
dependencies.  Therefore,  Autoformer  was
decomposition
designed  with
architecture,  which
time  series
decomposition into the Transformer model for the
first  time.  This  architecture  includes  sequence
decomposition
self-correlation
units,
mechanisms,  and
corresponding  encoder-
decoder components.

deep
integrates

for
sparse

the  complex

introduced

Although

struggle

capture

(2021)

to

to

a

2  EVALUATION
DATASETS
FORECASTING

METRICS
TIME

AND
SERIES

FOR

2.1  Evaluation  Metrics  for  Time  Series

Forecasting

the  performance  of

Evaluation metrics are tools used to  assess and
analyze
time  series
forecasting  models,  serving  as  key  criteria  for
measuring  model
performance.  Common
evaluation  metrics  for  time  series  forecasting
include:

Mean Squared Error (MSE): This measures the
average  squared  difference  between  predicted
and  actual  values,  reflecting  the  overall  error
between  the  predictions  and  actual  outcomes.  It
is calculated as follows:

         (1)

142

21)ˆ(1ˆ,iiniyynyyMSE−==）（

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619

Root  Mean  Squared  Error  (RMSE):  This is the
square root of MSE, assigning higher weights to
larger errors and emphasizing the stability of the
prediction results. It is calculated as follows:

(2)

Mean  Absolute  Error  (MAE):  This  represents
the mean  absolute difference between  predicted
and  actual  values,  reducing  the  influence  of
outliers. It is calculated as follows:

(3)

Mean Absolute Percentage Error (MAPE): This
metric  considers  the  relative  magnitude  of  the
actual  values,  avoiding  the  cancellation  effect  of
positive  and  negative  errors.  It  is  calculated  as
follows:

(4)

model,

application

and  Transformer  models  when

for

,  all

Except
the  evaluation  metrics
mentioned  above  are  better  when  their  values
are  smaller.  The  choice  of  evaluation  metric
depends  on  the  specific  situation.  Typically,  a
combination  of  multiple  metrics
to
comprehensively
analyze
enabling  deeper  insights.  Due  to  the  differences
in
characteristics
focus  of  Recurrent  Neural  Network
models
handling  time  series  data,  researchers  prioritize
different  metrics  when  evaluating  algorithm
performance.

is  used

(RNN)

and

the

the

the

RNN models, with their memory capability, excel
at  capturing  long-term  dependencies  in  time
series.  Consequently,  evaluation  metrics
for
RNNs  often  emphasize  the  ability  to  model  the
overall  structure  of
time  series  and
adaptability  to  various  tasks.  Researchers  may
use  a  diverse  range  of  evaluation  metrics  to
thoroughly  assess  the  performance  of  these
algorithms.  On  the  other  hand,  Transformer
their  self-attention  mechanism
models,  with
for  parallel  computation,  are  more
allowing
efficient  and
focus  heavily  on  predictive
accuracy.  As  such,  researchers  commonly  use
MAE  (Mean  Absolute  Error)  and  MSE  (Mean
Squared  Error)  to  measure  the  performance  of
Transformers.

Symmetric  Mean  Absolute  Percentage
Error  (SMAPE):  This is a  modification of MAPE
that  avoids  excessively  large  values  when  the
actual  values  are  very  small.  It  is  calculated  as
follows:

2.2 Datasets

2.2.1 ETT

the  explained

the  goodness  of

Coefficient  of  Determination
known  as
fit,
divides
total  variance  to  measure  the  proportion  of
variance  in  the  dependent  variable  explained  by
the  independent  variables.  It  is  calculated  as
follows:

variance  by

(R²):  Also
this  metric

the

(5)

(6)

explore

long-term

the  dataset  was  divided

The  ETT  dataset,  provided  by  the  State  Grid
Corporation  of  China,  consists  of  minute-level
recordings  of  transformer  oil  temperatures  from
two counties in  the same  province during 2016–
2018.  Each  dataset  contains  1,051,200  data
prediction
points.  To
granularity,
subsets  based  on  sampling  intervals  of  15
minutes  and  1  hour,  resulting  in  four  subsets:
ETTm1,  ETTm2,  ETTh1,  and  ETTh2.  These
subsets  contain  69,680  and  17,420  data  points,
respectively.  Each  data  point  includes  seven
target  variable  (oil
features,  comprising
the
temperature)  and  six
load
features.

types  of  power

into

In  the  formulas  (1)  to  (6)  mentioned  above,

is

2.2.2 ECL

the true value,
mean of

, and

 is the predicted value,
is the variance.

 is the

ECL  (Electricity  Consuming  Load):  Electricity
Consumption Load dataset from 2012–2014.

143

21)ˆ(1ˆ,iiniyynyyRMSE−==）（|)ˆ(|1ˆ,1iiniyynyyMAE−==）（iiiniyyynyyMAPEˆ%100ˆ,1−==）（2/|ˆ|ˆ%100ˆ,1）（）（iiiiniyyyynyySMAPE+−==VarMSEyynyynyyRiiniiini−=−−−===1)(1)ˆ(11ˆ,21212）（yyˆyyVar2R

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619

2.2.3 Traffic

Traffic:  Traffic
Department of Transportation (2015–2016).

dataset

from  California's

2.2.4 Weather

Weather:  The  weather  dataset,  provided  by  the
meteorological station of the Max Planck Institute
for  Biogeochemistry,  records  21  meteorological
indicators such as air pressure, temperature, and
humidity collected every 10 minutes from 2020 to
2021.

2.2.5 ILI

ILI:  The  influenza  dataset,  provided  by  the
Centers  for  Disease  Control  and  Prevention  in
the  United  States,  records  the  ratio  of  influenza
like  disease  patients  to  the  total  number  of
patients per week from 2002 to 2021.

2.2.6 TE

Tennessee  Eastman  (TE)  is  a  representative
chemical  process  proposed  by  an  American
chemical  company,  consisting  of  a  gas-liquid
separator, a circulating compressor, a stripper, a
condenser,  a  reactor,  and  other  components.
The TE chemical process can simulate 21 types
of
industrial  production  processes.
These  faults  are  mainly  divided  into  6  types,

faults

in

including  constant  position,  sticking,  step,
random  variable,  slow  drift,  and  five  unknown
faults.  The  variable  parameters  of  this  process
include  41  measured  variables  (XMEAS  (1)  -
XMEAS  (41))  and  12  manipulated  variables
(XMV (1) - XMV (12)), for a total of 53 observed
variables.

3  TIME  SERIES  PREDICTION  MODEL

BASED ON DEEP LEARNING

3.1 RNN

The  RNN  model  consists  of  the  following  three
main components:

(1)  Input  Layer:  Receives

input  data  and
passes  it  to  the  hidden  layer.  The  input
includes  not  only  static  data  but  also
historical information from the sequence.
(2)  Hidden  Layer:  The  core  component  that
captures
temporal  dependencies.  The
output of the hidden layer depends on both
the current input and the hidden state from
the previous timestep.

(3)  Output  Layer:  Generates

final
prediction  based  on  the  output  of  the
hidden layer.

the

The  structure  of  the  RNN  is  illustrated  in  the
diagram below:

Fig. 1. RNN structure diagram

144

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619

The  diagram  shows  the  basic  structure  of  an

RNN, where

represents the output information,

represents  the  hidden  layer  output  at  the
 represents the hidden layer

current timestep,

from

the  previous

output
represents  the  current  input.  Functions
,
 are  activation  functions,  while

timestep,  and

 and
,

represent  weight  matrices.  RNNs  work  by
continuously cycling the same neuron over time.
The  calculation  for  the  current  timestep  is  given
by:

output  layer  then  generates  the  final  output
using  another  weight  matrix  and  activation
function.

Although  RNNs  are  effective  for  processing
sequential  data,  they  suffer  from  issues  like
vanishing  and  exploding  gradients.  For  long
sequences,  the  gradients  may  become  very
small (vanish) or excessively large (explode) due
to  repeated  multiplication.  To  address  these
problems, variants of RNNs, such as Long Short-
Term  Memory  (LSTM)  networks  and  Gated
Recurrent Units (GRU), have been developed.

         (7)

3.2 Long Short-Term Memory (LSTM)

                                   (8)

The  working  principle  of  RNNs  can  be
summarized  in  the  following  steps:  At  each

timestep,  the  RNN  unit  receives  the  input

 for

the  current  timestep  and  the  hidden  state
from the previous timestep. Based on these, the
 using  a
hidden  layer  computes  a  new  state

nonlinear  function  (such  as  Tanh  or  ReLU).  The

LSTM
is  a  specialized  RNN  architecture
proposed  by  Hochreiter  and  Schmidhuber  in
1997.  It  was  designed  to  overcome  the  gradient
vanishing  and  exploding  problems  encountered
long
in
standard  RNNs  when  handling
sequences.  The  core  of  an  LSTM
its
sophisticated  gating  mechanism,  which  controls
the  flow  of  information  in  and  out  of  the  unit.  A
typical  LSTM  unit  comprises
following
components:  forget  gate,  input  gate,  cell  state,
and output gate. Below is its structure diagram:

the

is

3.2.1 Forget Gate

Fig. 2. LSTM structure diagram

 and  the  current  input

In an LSTM, the first step is determining which information should be filtered out from the cell state by
the forget gate. This operation is achieved through the forget gate's structure. The forget gate reads
the  previous  output
,  applies  a  Sigmoid  nonlinear  transformation,  and
. Each value in this vector ranges from 0 to 1, where 1 indicates complete retention
outputs a vector
and  0  indicates  complete  discard.  This  vector  is  then  multiplied  element-wise  with  the  cell  state
.For example, in a language model, the cell state may encode the gender information of the subject in
the current sentence, ensuring the correct pronoun is selected. When a new subject is identified, the
forget gate removes the prior subject's gender information to make room for the new information.

145

toth1th−tx1f2fWUV)(11bWhUxfhttt++=−)(2cVhfott+=tx1th−thtot1h−txtft-1C

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619

Fig. 3. Forgetting gate structure diagram

The  mathematical  formula  for  the  forget  gate  is
as follows:

        (9)

here (

)and (

) are the weight matrix and bias

vector,  (

)  is  the  previous  hidden  state,(

)  is

the  current
activation function.

input,  and

 is

the  Sigmoid

3.2.2 Input gate

The  information  update  mechanism  in  Long
Short-Term  Memory  (LSTM)  networks  involves
the  following  two  steps  to  determine  how  new
information is stored in the cell state:

(1)  Input  Gate  activation  function.  This  is  a
layer  composed  of  a  sigmoid  activation
function  that  determines  which  values  will
be updated to the cellular state. This layer
outputs  a  vector  between  0  and  1,  where
each  element  corresponds  to  the  updated
weight of the corresponding element in the
candidate cell state.

(2)  Generation  of  candidate  cell  states.  This
layer, formed by a tanh activation function,
creates  a  vector  of  potential  new
information containing values that might be
integrated  into  the  current  cell  state.  This
newly  generated  vector  is  then  multiplied
element-wise  by  the  output  of  the  input
gate to determine the actual values added
to the cell state.

.

Fig. 4. Input door structure diagram

146

)],[(1fttftbxhWf+=−fWfb1th−tx

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619

The mathematical expressions for these two steps are as follows:

             (10)

(11)

here  (

)and  (

)，(

)and（ ）  are  the  parameter  matrices  and  bias  vectors,  (

)  is  the  hidden

state from the previous timestep, (

) is the current input,

and tanh are activation functions.

The  next  step  updates  the  cell  state
added information:

 by  combining  the  information  to  be  forgotten  and  the  newly

Fig. 5. Update cell structure diagram

LSTM  cells  need  to  multiply  the  previous  state  with ,  discard  the  information  that  needs  to  be

discarded, and then add

. This is the new output state .

3.2.3 Output gate

Fig. 6. Output Gate Structure Diagram

The mathematical formula for the output gate is as follows:

(12)

147

)],[(1ittitbxhWi+=−)],[tanh(~1cttctbxhWC+=−iWibcWcb1th−txtCt-1CtfttCi~tC)],[(10tt0tbxhWo+=−

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619

(13)

here  (

)and  (

)  are  the  parameter  matrices  and  bias  vectors,  (

)  is  the  previous  timestep's

hidden state, (

) is the current input, and

 is the sigmoid activation function.

3.3 Gated Recurrent Units (GRU)

GRU is a simplified variant of LSTM that retains the gating mechanisms (update and reset gates) to
control the flow of information while omitting the separate memory cell. GRUs have fewer parameters
than  LSTMs,  resulting  in  higher  computational  efficiency  and,  in  some  cases,  similar  or  better
performance. The core components of GRU include:

Fig. 7. GRU structure diagram

3.3.1 Update gate

to  1,  more  past  information  is  retained.  The
formula is:

The  update  gate  determines  how  much  of  the
previous
timestep's  hidden  state  should  be
retained  in  the  current  hidden  state.  It  outputs
values  between  0  and  1,  where  higher  values
indicate greater retention of past information and
lower  values  suggest  reliance  on  current  input.
The formula is:

     (14)

)  and  (

here  (
and  bias  vectors,(

)  are  the  parameter  matrices
)  is  the  previous  hidden

state,  (
sigmoid activation function.

)  is  the  current  input,  and

 is  the

3.3.2 Reset gate

       (15)

here (
)and(
bias vectors.

) are the parameter matrices and

At  each  time  step,  the  GRU  unit  processes
information through the following steps:

(1)  Calculate update and reset gates

According  to  the  above  formula,  calculate  the

) and (

) respectively, and the
update gates (
outputs  of  these  gates  will  control  the  update  of
hidden  states  and  the  degree  of  preservation  of
historical information.

The  reset  gate  determines  the  extent  to  which
the  previous  hidden  state
the
computation of the candidate hidden state. When
the  reset  gate  output  is  close  to  0,  most  of  the
previous  information  is  ignored;  when  it  is  close

influences

(2) Calculate candidate hidden states

GRU  uses  reset  gates  to  control  the  degree  of
dependence  on  previously  hidden  states  and
calculate candidate hidden states.

148

)tanh(tttCoh=0W0bt1h−tx)],[(1zttztbxhWz+=−zWzb1th−tx)],[(1tttttbxhWr+=−rWrbtztr

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619

The  calculation  formula  for  candidate  hidden
states is:

       (16)

Among  them,  (

)  represents  combining

the hidden state of the previous time step (

)

with  the  reset  gate  (
influence,  and  (
matrix and bias.

)  to  control  its  degree  of
)  are  the  parameter

)  and  (

(3) Update Hidden State

The  final  step  is  to  use  the  update  gate  (
calculate the current hidden state (

):

)  to

3.4 Bi-LSTM Model

The  Bi-LSTM  (Bidirectional  Long  Short-Term
Memory)  network  is  an  improved  version  of  the
LSTM  network.  It  combines  two  LSTMs:  one
processes  the  sequence  from  the  beginning  to
the  end,  while  the  other  processes  it  in  reverse,
from  the  end  to  the  beginning.  This  architecture
excels  in  several  tasks  compared  to  standard
LSTM  networks.  Bi-LSTM  is  a  time-recurrent
neural network that stacks forward and backward
LSTM  layers  together.  The  output  is  determined
by  the  hidden  states  of  these  two  LSTM  layers.
Bi-LSTM  combines  the  traditional  forward  and
backward  time  sequences,  leveraging  LSTM's
sensitivity  to  sequence  order  to  construct  a
bidirectional network. The concatenated vector of
forward  and  backward
outputs
processes  provides
the  complete  hidden
representation of Bi-LSTM, as shown below:

from

the

Here,

controls  the  retention  of  past

Here,

is  the  output  from  the  forward  LSTM

       (17)

      (18)

and

information,
new
information. This formula ensures that the current
hidden state incorporates both historical and new
information effectively.

 introduces

layer,  and
is  the  output  from  the  backward
LSTM  layer.  These  outputs  are  combined  using
element-wise  summation.  The  internal  structure
of  Bi-LSTM  cells  is  identical  to  that  of  standard
LSTMs and is thus not elaborated further.

Fig. 8. Bi LSTM Structure Diagram

149

)],[tanh(~1bxhrWhtttt+=−1−tthr1th−trWbtzthttttthzhzh~)1(1+−=−1)1(−−tthztthz~btftthhh=fthbth

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619

3.5 Transformer Model

and

other

2017.  The

The  Transformer  is  a  deep  learning  architecture
primarily  used  for  natural  language  processing
(NLP)
sequence-to-sequence
tasks.  It  was  first  proposed  by  Vaswani  et  al.
in
the  self-attention
Transformer  architecture  is
mechanism,  which  allows
in
to  excel
it
processing  sequential  data.  The  Transformer
employs  a  self-attention-based  encoder-decoder
structure.

the

innovation

key

of

(1)  Encoder:  Composed  of  stacked  identical
layers,  each  layer  includes  two  sub-layers:  a
multi-head  self-attention  mechanism  and  a
feedforward
position-wise
network.  Normalization
residual
connections  are  applied  to  the  input  and  output
of the multi-head self-attention module.

layers  and

connected

fully

is  composed  of  stacked  identical  layers.  Each
decoder  layer  adds  a  third  sub-layer,  which
performs multi-head attention over the encoder's
output.  Residual  connections  and  normalization
layers  are  applied
to  each  sub-layer.  The
following
the  architecture  diagram  of
is
Transformer.

3.5.1 Self-Attention mechanism

The self-attention mechanism is the core concept
of  the  Transformer.  It  enables  the  model  to
consider  all  positions  in  the  input  sequence
simultaneously,  unlike  recurrent  or  convolutional
neural  networks  that  process  sequentially.  The
varying
self-attention  mechanism
attention  weights  to  different  parts  of  the  input
sequence,
semantic
relationships  more  effectively.  The  mathematical
expression for self-attention is as follows:

capturing

assigns

thereby

(2)  Decoder:  The  decoder  generates  the  output
sequence  using  the  representation  produced  by
the encoder. Similar to the encoder, the decoder

      (19)

Fig. 9. Transformer architecture diagram

150

)VdQKsoftmax(Q,K,V)Attention(kT=

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619

),  and  value  vector  (

Firstly,  extract  the  query  vector  (
(
)  from  the  embedded
vector.  Next,  determine  a  score  for  each  vector:
.  Score  normalization
the  score  is  equal  to

),  key  vector

(division
)  is  used  for  gradient  stability.  Next,
use  the  softmax  activation  function  to  process
the  scores.  The  weighted  score  of  each  input
vector  is  obtained  by  taking  the  softmax  dot
product value. Sum up to produce the final result.

3.5.2 Multi-head attention mechanism

information

the  model

from  other

The  Transformer  model  employs  a  multi-head
self-attention mechanism to enhance its ability to
capture  dependencies  among  elements  in  a
sequence.  The  core  principle  of  the  attention
mechanism is that each token in a sequence can
aggregate
tokens,
enabling
to  better  understand
contextual  relationships.  This  is  achieved  by
mapping  a  query,  a  set  of  key-value  pairs,  and
an  output  (each  represented  as  vectors)  into  an
attention  function.  The  output  is  computed  as  a
weighted  sum  of  the  values,  where  the  weights
are  determined  by  a  compatibility
function
between  the  query  and  the  corresponding  keys.
Multi-head  attention  is  equivalent  to  combining
attention
multiple
mechanisms.
the
processing of the query (
), and value
(
)  vectors,  resulting  in  a  final  output  that
integrates  information  from  different  attention
heads.

dot-product
It  effectively  parallelizes

scaled

), key (

3.5.3 Positional encoding

order.  Positional

Since  the  Transformer  model  does  not  rely  on
recursion  or  convolution,  it  requires  a  method
to  capture  the  relative  or  absolute  position  of
tokens  within  a  sequence  to  effectively  utilize
is
sequential
introduced  at  the  input  level  of  the  encoder  and
decoder  stacks.  These  positional  encodings  are
added  to  the  input  embeddings,  sharing  the
same  dimensional  space.  They  are  calculated
using  sine  and  cosine  functions  at  different
frequencies as follows:

encoding

 is  the  position  in  the  sequence,

 is  the
Here,
vector  dimension,  and
 is  the  natural  number
used for indexing. By mapping each position to a
unique
frequency  using  sine  and  cosine
functions,  and  converting  the  frequency  into  an
element  in  the  embedding  vector  using  the
corresponding  sine  and  cosine  functions,  the
model can capture the position information when
processing the input sequence.

3.6 Comparison of Deep Learning Models

Datasets:  This  study  conducted  experiments
using
the  ETTm2,  Electricity,  Traffic,  and
Weather datasets. Other datasets were excluded
due to insufficient periodicity, seasonality, or data
volume.

Experiment  Details:  To  ensure  consistency,  all
models used an input sequence length of 24 and
the  ETTm2,
a  prediction
length  of  1.  For
Electricity,  and  Weather  datasets,
first
the
variable was selected for prediction, representing
the high-useful load of an electric transformer oil
electricity
user's
temperature,
consumption,
pressure,
respectively.  For  the  Traffic  dataset,  the  third
variable  was  selected,  representing  the  hourly
road  occupancy  rate  recorded  by  a  sensor.  All
models  were  trained  using  the  Adam  optimizer,
with MSE (Mean Squared Error) and MAE (Mean
Absolute  Error)  as  evaluation  metrics.  PyTorch
was used for implementation.

hourly
atmospheric

a
and

the  ETTm2  dataset,  where
the  dataset,

Fig.  10  shows  the  prediction  curves  of  four
the
models  on
horizontal  axis  represents
the
vertical  axis  represents  the  numerical  size,  the
blue curve represents the actual data value, and
the red curve represents the predicted value.

Fig.  11  The  prediction  curves  of  four  models  on
the  ECL  dataset,  where  the  horizontal  axis
represents
the  vertical  axis
represents  the  numerical  size,  the  blue  curve
represents  the  actual  data  value,  and  the  red
curve represents the predicted value.

the  dataset,

(20)

Fig.  12  The  prediction  curves  of  four  models  on
the  Weather  dataset,  where  the  horizontal  axis
represents  the  number  of  test  sets,  the  vertical
axis  represents  the  numerical  size,  the  blue
curve  represents  the  actual  data  value,  and  the
red curve represents the predicted value.

151

QKVKQ•kdQKV+===12k,i10000tcos2k,i10000tsinPE(t)2k/d2k/ditdk

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619

(a) RNN model

(b) LSTM model

(c) GRU model

 (d) Transformer model

(e) LSTM-RNN model

Fig. 10. The prediction curves of four models on the ETTm2 dataset

(a) RNN model

  (b) LSTM model

152

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619

(c) GRU model

     (d) Transformer model

(e) LSTM-RNN model

Fig. 11. The prediction curves of four models on the ECL dataset

(a) RNN model

  (b) LSTM model

(c) GRU model

   (d) Transformer model

153

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619

(e) LSTM-RNN model

Fig. 12. The prediction curves of four models on the Weather dataset

(a) RNN model

  (b) LSTM model

(c) GRU model

        (d) Transformer model

(e) LSTM-RNN model

Fig. 13. The prediction curves of four models on the Traffic dataset

154

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619

Table 1. Comparison of univariate prediction performance of four deep learning models

Model
RNN

LSTM

GRU

Transformer

LSTM-RNN

Evaluating indicator   ETTm2
MSE
MAE
MSE
MAE
MSE
MAE
MSE
MAE
MSE
MAE

3.459
1.404
3.480
1.414
3.454
1.402
3.418
1.399
3.454
1.404

Electricity  Weather
21.603
2.014
19.821
1.848
19.524
1.889
19.541
2.025
21.583
1.941

0.007
0.060
0.008
0.066
0.007
0.062
0.827
0.341
0.007
0.062

Traffic
0.00112
0.021
0.00120
0.020
0.00110
0.021
0.00122
0.021
0.00125
0.021

Fig.  13  The  prediction  curves  of  four  models  on
the  Traffic  dataset,  where  the  horizontal  axis
represents  the  number  of  test  sets,  the  vertical
axis  represents  the  numerical  size,  the  blue
curve  represents  the  actual  data  value,  and  the
red curve represents the predicted value.

We compare and analyze the performance of the
four  deep  learning  models  mentioned  above  (as
shown in Table 1).

The experimental data of various models listed in
Table 1 were analyzed and summarized in depth,
and the conclusion is as follows: the Transformer
model  achieved  the  best  performance  on  the
ETTm2  dataset,  with  minimum  MAE  and  MSE
values. The LSTM model achieved the minimum
MAE  on  the  Electricity  and  Traffic  datasets,  i.e.
the minimum tie error. The GRU model achieved
the  minimum  mean  square  error  (MSE)  on  the
Electricity  and  Traffic  datasets.  The  RNN  model
achieved  the  best  performance  on  the  Weather
dataset,  with  minimum  MAE  and  MSE  values.
The LSTM-RNN model generally outperforms the
standard RNN and also shows better results than
the  ordinary  LSTM  model  on  the  ETTm2  and
Weather  datasets.  Overall,  in  most  cases,  the
combination  of  the  two  results  in  a  certain
performance improvement.

to

to

lower

human

relatively

innovative

forecasting  methods

learning
identify
techniques  can  accurately
complex  patterns  within  and  across  time  series
with
resource
requirements.  However,  these  models  rely  on
fewer structural assumptions, making them more
challenging to interpret and often requiring larger
learn  accurate  models.
training  datasets
Additionally,  since  different  sample  types  exhibit
distinct distribution patterns, a single fixed model
cannot  be  universally  applied,  necessitating  the
use  of  multiple  regression  algorithms.  This  has
led
that
combine  traditional  statistical  models  with  deep
learning.  These  hybrid  approaches  have
significantly  addressed  the  limitations  of  both
techniques.  In  recent  years,  many  deep  neural
network  models  for  time  series  analysis  have
been  proposed.  These  methods  not  only  enable
models  to  automatically  extract  features  and
learn  complex  temporal  patterns  but  also  apply
assumptions like temporal smoothing, enhancing
model  interpretability.  As  research  on  neural
network
to  advance,
deep  learning  has  become  one  of  the  hottest
research  topics  in  machine  vision.  Based  on  a
review of literature on time series forecasting and
deep  learning,  this  paper  primarily  explores  four
deep learning models for time series forecasting.

technologies  continues

4. SUMMARY AND OUTLOOK

4.2 Outlook

4.1 Summary

traditional

Although
statistical  modeling
techniques  incorporate  structural  assumptions
into  models,  making  them  easier  to  understand,
they  often  require  independent  modeling  of  time
series  data  in  modern  predictive  applications.
This  approach  significantly  increases  labor  and
computational costs. Therefore, it is necessary to
techniques  capable  of
find  more  efficient
simultaneously  handling  varying  degrees  of
relationships among two or more variables. Deep

Deep learning has achieved significant results in
the field  of time series prediction,  and the future
prospects  are  even  more  exciting.  With  the
continuous advancement of technology, we have
reason  to  believe  that  deep  learning  will  play  a
temporal  prediction,
in
more
bringing
to  various
industries.

revolutionary  changes

important  role

Firstly, at the algorithmic level, deep learning will
be  further  optimized  and  improved.  At  present,
models  such  as  RNN,  LSTM,  and  GRU  have

155

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619

achieved  good  results  in  time  series  prediction.
In the future, new deep learning models such as
Transformers  and  graph  neural  networks  are
expected
time-series  data,
to  better  handle
improve prediction accuracy and stability.

for  stock  price  prediction,

Secondly,  at  the  application  level,  deep  learning
will  play  an  important  role  in  more  fields.  For
example, in the financial field, deep learning can
be  used
risk
management, etc; In the field of energy, it can be
used  for  power  load  forecasting,  new  energy
generation
field  of
transportation,  it  can  be  used  for  traffic  flow
prediction,  flight  delay  prediction,  etc.  With  the
continuous accumulation  of data, the application
of  deep  learning  in  time  series  prediction  will
become more widespread.

forecasting,  etc;

the

In

In addition, cross domain fusion of deep learning
temporal  prediction  will  also  become  a
in
development
trend.  For  example,  combining
deep learning with statistics, chaos theory, etc. is
expected  to  further  improve  the  generalization
ability  and  robustness  of  prediction  models.  At
the same time, by combining domain knowledge,
deep learning can achieve finer grained temporal
prediction,  providing  decision-makers  with  more
targeted recommendations.

Finally,  with  the  continuous  improvement  of
computing  power,  the  real-time  performance  of
deep  learning  in  temporal  prediction  will  be
guaranteed. In the future, real-time prediction will
become  possible,  providing  more  accurate  and
real-time decision support for various industries.

5. CONCLUSION

It

first

This  paper  presents  a  systematic  review  of  time
forecasting  methods  based  on  deep
series
learning.
the  background,
introduces
significance, and various methods of time series
forecasting. Then, it provides a detailed overview
of  representative  deep  learning  models  in  this
domain,
including  RNN,  LSTM,  GRU,  and
Transformer  models.  Subsequently,  it  conducts
comparative  prediction  experiments  on  public
datasets and evaluates the performance of these
future  research
it  explores
models.  Finally,
directions
time  series
in
learning
forecasting,  offering  valuable  insights  for  further
advancements in this field.

for  deep

DISCLAIMER (ARTIFICIAL INTELLIGENCE)

Author(s)  hereby  declare  that  NO  generative  AI
technologies  such  as  Large  Language  Models

(ChatGPT,  COPILOT,  etc)  and
text-to-image
generators  have  been  used  during  writing  or
editing of this manuscript.

COMPETING INTERESTS

Authors  have  declared
interests exist.

that  no  competing

REFERENCES

Abdel-Nasser,  M.,  &  Mahmoud,  K.  (2019).
Accurate  photovoltaic  power  forecasting
models  using  deep  LSTM-RNN.  Neural
Computing  and  Applications,  31(7),  2727-
2740.

Durbin, J., & Koopman, S. J. (2012). Time series
analysis by state space methods (2nd ed.).
OUP Oxford.

Eslin, G. P., & Agon, C. (2012). Time-series data
mining. ACM  Computing  Surveys (CSUR),
45(1), 1-34.

Fang,  W.,  Chen,  Y.,  et  al.  (2021).  Survey  on
research  of  RNN-based  spatio-temporal
sequence prediction algorithms. Journal on
Big Data, 3(3), 97-110.

Gers,  F.  A.,  Schmidhuber,  J.,  &  Cummin,  S.  F.
(2000).  Learning
forget:  Continual
to
prediction with LSTM. Neural Computation,
12(10), 2451-2471.

Hanen, B., Ali, A. B., & Riadh, I. F. (2024). A Bi-
GRU-based  encoder–decoder  framework
for  multivariate  time  series  forecasting.
Soft Computing, 28(9-10), 6775-6786.
Jin,  K.  H.,  Wi,  J.  A.,  Lee,  E.  J.,  et  al.  (2021).
TrafficBERT: Pre-trained model with large-
flow
scale  data
with
forecasting.
Applications, 186, 115738.

long-range

Systems

Expert

traffic

for

Li,  S.  Y.,  Jin,  X.  Y.,  Xuan,  Y.,  et  al.  (2019).
Enhancing  the  locality  and  breaking  the
memory bottleneck of Transformer on time
In  Proceedings  of
series
forecasting.
NeurIPS 2019, 5244-5254.

Liu,  Y.,  Hu,  T.,  Zhang,  H.,  et  al.  (2024).
ITransformer:  Inverted  transformers  are
effective  for  time  series  forecasting.  In
Proceedings
International
Conference  on  Learning  Representations
(ICLR 2024).

the

of

Liu,  Y.,  Wu,  H.  X.,  Wang,  J.  M.,  et  al.  (2022).
Non-stationary  transformers:  Exploring  the
forecasting.
stationarity
Advances
Information
Processing Systems, 35, 9881-9893.
Michael, E. N., Bansal, C. R., Ismail, A. A. A., et
al.  (2024).  A  cohesive  structure  of  Bi-

time  series
Neural

in

in

156

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619

directional
memory
long-short-term
(BiLSTM)-GRU  for  predicting  hourly  solar
222,
radiation.  Renewable  Energy,
119943-.

Qiang, C., Shu, W., Qiang, L., et al. (2020). MV-

A
Network

Multi-View
for

Recurrent
RNN:
Sequential
Neural
Recommendation.  IEEE  Transactions  on
Knowledge  and  Data  Engineering,  32(2),
317-331.

Shaowei, P., Bo, Y., Shukai, W., et al. (2023). Oil
well  production  prediction  based  on  CNN-
LSTM
self-attention
with
model
mechanism. Energy, 284.

Shaowei, P., Bo, Y., Shukai, W., et al. (2023). Oil
well  production  prediction  based  on  CNN-
LSTM
self-attention
with
model
mechanism. Energy, 284.

Vaswani,  A.,  Shazeer,  N.,  Parmar,  N.,  et  al.
(2017). Attention is all you need. Advances

in Neural Information Processing Systems,
30, 5998-6008.

Waqas, M., & Humphries, W. U. (2024). A critical
review  of  RNN  and  LSTM  variants  in
hydrological
series  predictions.
MethodsX, 13102946-102946.

time

Wen, Q. S., Zhou, T., Zhang, C. L., et al. (2023).
Transformers  in  time  series:  A  survey.  In
Proceedings  of
International  Joint
Conference  on  Artificial  Intelligence  (IJCAI
2023), 6778-6786.

the

Wu, H. X., Xu, J. H., Wang, J. M., et  al.  (2021).
Autoformer:  Decomposition
transformers
with  auto-correlation  for  long-term  series
forecasting.  In  Proceedings  of  NeurIPS
2021, 34, 22419-22430.

Zhang,  Y.  F.,  Wu,  R.,  Dascalu,  S.  M.,  et  al.
transformer  pyramid
time  series

(2024).  Multi-scale
networks
for  multivariate
forecasting. IEEE Access, 14731-14741.

Disclaimer/Publisher’s  Note:  The  statements,  opinions  and  data  contained  in  all  publications  are  solely  those  of  the  individual
author(s)  and contributor(s) and  not  of the  publisher  and/or the  editor(s).  This  publisher  and/or the  editor(s)  disclaim  responsibility for
any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.
_________________________________________________________________________________
© Copyright (2024): Author(s). The licensee is the journal publisher. This is an Open Access article distributed under the terms
of  the  Creative  Commons  Attribution  License  (http://creativecommons.org/licenses/by/4.0),  which  permits  unrestricted  use,
distribution, and reproduction in any medium, provided the original work is properly cited.

Peer-review history:
The peer review history for this paper can be accessed here:
https://prh.ikprress.org/review-history/12619

157

