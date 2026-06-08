Article

Not peer-reviewed version

A Decade of Applied Quantitative
Analytics for Philippine Policy:
Forecasting, Statistical Forensics, and
Predictive Modeling Across Education,
Energy, Agriculture, Health, and Finance

Adran Velasco *

Posted Date: 24 March 2026

doi: 10.20944/preprints202603.1811.v1

Keywords: quantitative analytics; forecasting; statistical forensics; predictive modeling

Preprints.org is a free multidisciplinary platform providing preprint service
that is dedicated to making early versions of research outputs permanently
available and citable. Preprints posted at Preprints.org appear in Web of
Science, Crossref, Google Scholar, Scilit, Europe PMC.

Copyright: This open access article is published under a Creative Commons CC BY 4.0
license, which permit the free download, distribution, and reuse, provided that the author
and preprint are cited in any reuse.

Preprints.org (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 24 March 2026

doi:10.20944/preprints202603.1811.v1

Disclaimer/Publisher’s Note: The statements, opinions, and data contained in all publications are solely those of the individual author(s) and
contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting
from any ideas, methods, instructions, or products referred to in the content.

Article
A Decade of Applied Quantitative Analytics for
Philippine Policy: Forecasting, Statistical Forensics,
and Predictive Modeling Across Education, Energy,
Agriculture, Health, and Finance

Adran Velasco

Central Luzon State University, Philippines; adrian.velasco@clsu.edu.ph

Abstract

Quantitative analytics has assumed a growing role in Philippine policy research as government and
sectoral databases have become increasingly central to planning, monitoring, and resource allocation.
This review synthesizes recent work in education, energy, agriculture, health, and finance to examine
how forecasting, statistical forensics, and predictive modeling have been applied to Philippine policy
problems.  Across  these  sectors,  the  literature  shows  a  clear  methodological  progression  from
descriptive diagnostics and classical time-series models toward comparative machine learning, deep
learning,  explainable  artificial  intelligence,  nonlinear  embedding,  and  Benford-based  anomaly
detection. Several  recurring  strengths emerge,  particularly the  consistent use  of  official  Philippine
datasets, transparent model benchmarking, and close alignment with practical policy concerns such
as dropout reduction, electricity and crop planning, disease surveillance, and financial forecasting.
At the same time, important limitations remain, including limited multivariate and spatial modeling,
uneven  validation  practices,  and  relatively  little  attention  to  uncertainty  quantification  and
operational  deployment.  In  comparison  with  the  broader  international  literature,  the  strongest
contributions are those that position analytics as a support tool for planning and monitoring, while
the main gaps lie in external validation, richer explanatory structures, and decision-oriented system
integration. The evidence suggests that the next phase of Philippine policy analytics should move
beyond isolated single-series applications toward integrated frameworks that combine forecasting,
data-quality  assessment,  explainable  modeling,  and  sector-specific  decision  thresholds  for  routine
governance.

Keywords: quantitative analytics; forecasting; statistical forensics; predictive modeling

1. Introduction

Quantitative analytics  now  occupies a  central  place  in  public-sector  decision-making  because
governments  must  allocate  scarce  resources  under  uncertainty  while  responding  to  nonstationary
social,  epidemiological,  agricultural,  and  economic  conditions.  In  education,  dropout  is  widely
understood as a cumulative process shaped by household, school, and community factors rather than
a  single  event,  which  makes  descriptive  proﬁling  and  risk  monitoring  policy-relevant.  In  energy,
forecasting research has moved from classical statistical models toward machine learning and hybrid
systems,  especially  when  seasonality,  nonlinear  demand  shifts,  and  structural  breaks  matter.  In
agriculture, forecast quality increasingly depends on whether models can use both conventional time
series and richer covariates, while in health surveillance, routine data quality itself has become an
analytical object rather than a background assumption. In nonlinear ﬁnancial forecasting, state-space
reconstruction  and  recurrent  models  have  gained  traction  because  linear  speciﬁcations  often  fail
under regime shifts and complex temporal dependence (Rumberger & Lim, 2008; Sabates et al., 2010;
Ugbehe et al., 2025; van Klompenburg et al., 2020; Deyle & Sugihara, 2011; Ramadevi & Bingi, 2022).

© 2026 by the author(s). Distributed under a Creative Commons CC BY  license.

Preprints.org (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 24 March 2026

doi:10.20944/preprints202603.1811.v1

2  of  8

Within the Philippine setting, this shift is particularly important because the country’s policy
environment depends heavily on oﬃcial statistical and surveillance systems, including datasets from
the  Philippine  Statistics  Authority,  Department  of  Energy,  Department  of  Health,  and  related
repositories. The reviewed corpus captures a coherent research program organized around applied
policy  problems  rather  than  purely  methodological  novelty:  dropout  proﬁling  in  education,
electricity and coal demand in energy, rice and corn forecasting in agriculture, dengue and measles
surveillance in health, anomaly detection in public data, and stock-index prediction in ﬁnance. Taken
together,  these  studies  make  it  possible  to  examine  not  just  model  performance,  but  also  how
analytical techniques have been translated into policy language across sectors (Parreño, 2019, 2022a,
2022b, 2022c, 2023a, 2023b, 2023c, 2023d, 2024b, 2024c, 2024d, 2024e, 2024f, 2024g; Parreño & Anter,
2024, 2025; Parreño, 2025).

2. Review Method

A structured narrative review was conducted using a core internal corpus of 17 studies spanning
2019  to  2025.  Each  study  was  coded  on  ﬁve  dimensions:  domain,  dataset,  modeling  approach,
validation  strategy,  and  policy  contribution.  The  education  subset  included  one  SSRN  paper  on
dropout  reasons,  one  journal  article  using  Philippine  Statistics  Authority  data  on  school  non-
attendance,  and  one  gender-disparity  study  based  on  regional  dropout  data.  The  energy  subset
covered  national  electricity  consumption,  Davao  del  Sur  electricity  demand,  coal  production  and
consumption, national monthly system peak demand, and ASEAN per-capita electricity stationarity.
The agriculture subset covered quarterly rice and corn forecasts using classical methods, machine-
learning forecasts for the same crops, and a Benford-based audit of crop statistics. The health subset
covered dengue-data quality, surveillance anomaly detection, underreporting during the COVID-19
period, measles forecasting, and diabetes-risk prediction. The ﬁnance subset consisted of a nonlinear
LSTM study of the Philippine Stock Exchange Index (Parreño, 2019, 2022a, 2022b, 2022c, 2023a, 2023b,
2023c, 2023d, 2024b, 2024c, 2024d, 2024e, 2024f, 2024g; Parreño & Anter, 2024, 2025; Parreño, 2025).

External  comparison  literature  was  then  used  to  position  the  corpus  against  broader
developments  in  dropout  research,  electricity  forecasting,  crop-yield  analytics,  epidemiological
surveillance, Benford-based auditing, and nonlinear or explainable machine learning. Priority was
given to peer-reviewed reviews, oﬃcial organizational reports, and major domain studies with clear
methodological or policy relevance. This made it possible to distinguish sector-speciﬁc ﬁndings from
broader methodological trends and to identify where the reviewed studies align with, extend, or lag
behind the wider literature (David et al., 2018; Idrovo et al., 2011; Guo et al., 2017; Tasin et al., 2023;
Misiurek et al., 2025; Morillas-Jurado et al., 2021; World Health Organization, 2021).

3. Results by Sector

3.1. Education

The  education  studies  are  descriptive  and  policy-diagnostic  rather  than  predictive,  but  they
establish an important baseline for Philippine social analytics. The 2019 study used national dropout-
related statistics to identify the principal reasons for non-completion. The 2023 journal article drew
on Philippine Statistics Authority data on the proportion of 6–24-year-olds not attending school and
compared  2008  with  2013  using  descriptive  statistics  and  percentage  change  analysis  in  R,
highlighting cost of schooling and employment-seeking as major drivers. The 2025 gender-focused
study  used  regional  dropout  rates  disaggregated  by  sex  from  the  Philippine  Institute  for
Development  Studies,  applying  trend  analysis  and  statistical  testing  to  show  that  male  dropout
remained systematically higher, with strong regional heterogeneity and especially elevated burdens
in historically disadvantaged regions. In domain terms, these studies belong toeducation policy and
inequality analysis; in dataset terms, they rely on national and regional administrative statistics; in
method terms, they use descriptive proﬁling, comparative trend analysis, and inferential testing; in
validation  terms,  they  rely  on  internal  consistency  and  statistical  signiﬁcance  rather  than  out-of-

© 2026 by the author(s). Distributed under a Creative Commons CC BY  license.

Preprints.org (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 24 March 2026

doi:10.20944/preprints202603.1811.v1

3  of  8

sample prediction; and in policy terms, they support targeted retention, aﬀordability, and region-
speciﬁc intervention design (Parreño, 2019, 2023a; Parreño & Anter, 2025).

Compared with the wider literature, these education studies are closely aligned with the view
that  dropout  is  multicausal  and  stratiﬁed  by  gender  and  disadvantage,  but  they  remain  mainly
descriptive.  Internationally,  dropout  research  often  moves  beyond  pattern  description  toward
multilevel  risk  modeling,  longitudinal  event-history  analysis,  and  school-process  variables,  while
Philippine  evidence  has  also  emphasized  boys’  persistent  disadvantage  in  participation  and
completion (Rumberger & Lim, 2008; Sabates et al., 2010; David et al., 2018). The main strength of the
reviewed  education  work  is  policy  readability:  the  ﬁndings  are  straightforward,  directly
interpretable,  and  anchored  in  oﬃcial  statistics.  The  main  gap  is  explanatory  depth.  There  is  still
substantial room for linking dropout proﬁles to poverty, labor-market pull factors, school quality,
geography, and post-pandemic learning loss through multivariate and spatial models.

3.2. Energy

The  energy  studies  show the  clearest  progression  from  classical  time-series  modeling  toward
comparative  and  structural  analysis.  The  national  electricity-consumption  study  used  48  annual
observations  from  1973  to  2020,  split  into  43  training  points  and  5  testing  points,  and  selected  an
ARIMA  speciﬁcation  through  a  Box–Jenkins  procedure  using  ACF/PACF  diagnostics  and
information  criteria.  The  Davao  del  Sur  study  used  22  annual  observations,  applied  Box–Cox
transformation and diﬀerencing, and selected an ARIMA model through residual diagnostics, but
acknowledged the absence of out-of-sample validation because the sample was too short. The coal
study  forecast  both  production  and  consumption  using  ARIMA,  checked  residual  autocorrelation
and  normality,  and  translated  the  resulting  gap  between  production  and  consumption  into  an
import-dependence interpretation. These three studies belong to energy planning; their datasets are
oﬃcial  historical  annual  series;  their  methods  are  univariate  ARIMA-based  forecasting;  their
validation ranges from holdout testing to residual diagnostics only; and their policy contribution lies
in long-horizon planning, capacity assessment, and import-dependence awareness (Parreño, 2022a,
2022b, 2022c).

The later energy studies are more comparative and methodologically ambitious. The system-
peak-demand  paper  used  monthly  Department  of  Energy  data  from  2001  to  2020  and  compared
SARIMA  with  neural-network  forecasting  using  RMSE,  MAE,  and  MAPE,  ﬁnding  stronger
performance from the nonlinear benchmark. The ASEAN stationarity paper moved away from point
forecasting and instead asked whether shocks to per-capita electricity consumption are persistent or
transitory,  applying  KPSS-type  stationarity  testing  with  structural  breaks  and  ﬁnding  substantial
persistence outside Brunei. In domain terms, these are still energy-policy studies, but their datasets
are richer in frequency or cross-country structure; their methods include seasonal time-series models,
neural networks, and structural-break stationarity tests; their validation uses error metrics or formal
hypothesis  testing;  and  their  policy  contribution  shifts  from  simple  projection  toward  resilience
planning  and  shock  persistence.  This  pattern  matches  the  broader  literature,  which  now  treats
electricity forecasting as a spectrum ranging from classical statistical baselines to machine-learning
and  hybrid  systems,  especially  when  nonlinearities,  renewables  integration,  and  multiple  forecast
horizons matter (Parreño, 2023c, 2024g; Kula et al., 2012; Husein & Kara, 2023; Ugbehe et al., 2025;
Misiurek et al., 2025).

A recurring strength in this sector is disciplined benchmarking: even when models are simple,
they are usually chosen through transparent diagnostics and evaluated with standard forecast errors.
A  recurring  gap  is  the  dominance  of  univariate  modeling.  Weather,  fuel  prices,  sectoral  demand
composition,  policy  shocks,  and  macroeconomic  drivers  are  mostly  absent,  and  probabilistic
forecasting is not yet routine. The reviewed work is therefore strongest as an operational baseline
and weakest where scenario-based or multivariate planning is needed.

© 2026 by the author(s). Distributed under a Creative Commons CC BY  license.

Preprints.org (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 24 March 2026

doi:10.20944/preprints202603.1811.v1

4  of  8

3.3. Agriculture

The  agriculture  studies  illustrate  a  transition  from  classical  seasonal  forecasting  to  machine
learning and then to data-quality forensics. The 2023 quarterly rice-and-corn study used Philippine
production  data  from  1987  to  2023  and  compared  SARIMA  with  Holt–Winters  under  additive
seasonality, ﬁnding lower RMSE and MAPE for Holt–Winters. The 2024 machine-learning study used
145 quarterly observations for rice and corn up to the ﬁrst quarter of 2023 and compared random
forests, echo-state networks, neural network autoregression, and support-vector variants, reporting
the best overall performance for random forests. In domain terms, both studies support agricultural
planning  and  food  security;  in  dataset  terms,  both  rely  on  oﬃcial  quarterly  production  series;  in
method  terms,  the  progression  is  from  seasonal  exponential  smoothing  and  SARIMA  toward
machine-learning comparison; in validation terms, both emphasize forecast-error benchmarking; and
in policy terms, both support production planning, resource allocation, and import-buﬀer decisions
(Parreño, 2023b; Parreño & Anter, 2024).

The crop-statistics forensic paper adds a distinct contribution by asking whether the agricultural
data themselves exhibit expected ﬁrst-digit patterns under Newcomb–Benford analysis. That moves
the discussion from forecast accuracy to statistical reliability. This is important because the broader
agricultural forecasting literature increasingly stresses that yield prediction improves when diverse
covariates such as temperature, rainfall, soil, and remote sensing are incorporated, but these advances
still depend on trustworthy base data (van Klompenburg et al., 2020; Jabed & Azmi Murad, 2024).
The strength of the reviewed agricultural work is that it combines forecast comparison with a nascent
data-audit  perspective.  The  main  gap  is  that  most  models  still  use  aggregate  time  series  without
climate  covariates,  subnational  spatial  detail,  or  formal  uncertainty  intervals,  which  limits  their
usefulness for adaptive food-security policy.

3.4.Health

The health studies are the most diverse and show the strongest convergence of forecasting and
statistical  forensics.  The  dengue-data  paper  and  the  broader surveillance-anomaly  paper  both  use
Newcomb–Benford analysis as a screening device for epidemiological data quality. In domain terms,
they sit at the intersection of public health surveillance and statistical auditing; in dataset terms, they
use  surveillance  counts  for  dengue  or broader  communicable  disease  reporting;  in  method  terms,
they apply ﬁrst-digit conformity testing; in validation terms, they assess consistency with expected
digit distributions rather than predictive performance; and in policy terms, they provide a low-cost
screening  mechanism  for  identifying  unusual  reporting  behavior  that  may  merit  further
investigation. This is consistent with the wider literature, where Benford-based methods are treated
as early-warning audit tools rather than deﬁnitive proof of manipulation or underreporting (Idrovo
et al., 2011; Morillas-Jurado et al., 2021).

The forecasting studies deepen this line of work. The underreporting paper used comparative
forecast  analysis  during  the  COVID-19  period  and  concluded  that  signiﬁcant  underreporting  of
several  diseases  likely  occurred  when  health-system  attention  shifted  toward  the  pandemic.  The
measles study used weekly incidence data from 2017 to late 2023, transformed cumulative counts
into  weekly  diﬀerences,  imputed  missing  values,  split  the  data  80:20  into  training  and  validation
samples,  and  compared  SARIMA,  Holt–Winters,  echo-state  networks,  and  NNAR,  with  NNAR
performing  best  overall.  In  domain  terms,  these  are  outbreak-monitoring  and  service-disruption
studies; in dataset terms, they rely on routine public health surveillance series; in method terms, they
combine  time-series  forecasting,  neural  network  benchmarks,  and  comparative  performance
evaluation; in validation terms, they use explicit train–validation designs and error metrics; and in
policy  terms,  they  support  surge  preparedness,  immunization  planning,  and  monitoring  of  silent
surveillance deterioration. This aligns with a broader public-health literature that treats routine data
as operational intelligence, especially during system shocks, and uses machine learning for dengue
and related disease forecasting where seasonality and nonlinear dynamics are strong (World Health
Organization, 2021; Guo et al., 2017).

© 2026 by the author(s). Distributed under a Creative Commons CC BY  license.

Preprints.org (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 24 March 2026

doi:10.20944/preprints202603.1811.v1

5  of  8

The diabetes study extends the health portfolio from surveillance forecasting to individual-level
predictive modeling. It used tabular diabetes data, applied principal component analysis for feature
engineering,  compared  several  advanced  learners  including  boosting  variants  and  support-vector
machines, tuned hyperparameters by grid search, used an 80:20 train–test split, and employed SHAP
values  for  interpretability.  In  domain  terms,  this  is  clinical  risk  prediction;  in  dataset  terms,  it  is
patient-level  tabular  data;  in  method  terms,  it  uses  supervised  machine  learning,  dimensionality
reduction, and explainable AI; in validation terms, it uses standard supervised holdout evaluation;
and  in  policy  terms,  it  points  toward  risk  stratiﬁcation  that  is  more  actionable  for  providers  than
opaque black-box predictions alone. Relative to the broader literature, the main strength is the explicit
inclusion of interpretability. The main gap is external validation and deployment evidence, which
remain central concerns in clinical AI (Parreño, 2024f; Tasin et al., 2023).

3.5. Finance

The  ﬁnance  contribution  centers  on  nonlinear  time-series  prediction  of  the  Philippine  Stock
Exchange  Index.  The  study  used  Takens-style  embedding  to  reconstruct  the  system’s  dynamics,
handled  missingness  with  chained  equations,  and  then  estimated  an  LSTM  model  on  the
reconstructed series. In domain terms, this belongs to ﬁnancial forecasting; in dataset terms, it uses
market-index time series; in method terms, it combines chaos-informed phase-space reconstruction
with deep learning; in validation terms, it reports training/validation behavior together with actual-
versus-predicted comparisons; and in policy terms, the contribution is less about direct regulation
than about showing that Philippine ﬁnancial series may beneﬁt from nonlinear representations when
conventional linear models are insuﬃcient. This is consistent with wider work showing that chaotic
or  nonlinear  forecasting  frameworks  can  strengthen  machine-learning  performance  in  complex
temporal  systems,  although  comparative  evidence  across  asset  classes  remains  mixed  (Parreño,
2024c; Deyle & Sugihara, 2011; Ramadevi & Bingi, 2022).

3.6. Cross-Cutting Methodological Trends

Five methodological trends recur across the corpus. First, oﬃcial Philippine administrative data
are the dominant empirical base, which strengthens policy relevance. Second, the early phase of the
corpus is dominated by descriptive statistics and classical univariate forecasting, especially ARIMA,
SARIMA, and Holt–Winters. Third, later studies increasingly adopt comparative machine learning,
including random forests, neural networks, boosted methods, and LSTM. Fourth, a distinct forensics
strand  emerges  through  Benford-based  anomaly  detection,  treating  data  quality  as  a  substantive
policy problem. Fifth, interpretability becomes more explicit in the health-prediction work through
SHAP and in the stock-index study through theory-guided embedding rather than purely brute-force
prediction (Parreño, 2022a, 2022c, 2023b, 2023c, 2023d, 2024c, 2024d, 2024f; Parreño & Anter, 2024).

Validation rigor, however, is uneven. Some studies use explicit holdout sets or train–validation
splits and compare models with standard error metrics, while others depend primarily on residual
diagnostics or signiﬁcance testing because samples are short or the goal is descriptive rather than
predictive. This unevenness is understandable in applied public-data settings, but it also marks the
clearest  methodological  gap  in  the  corpus.  Relative  to  current  best  practice,  future  work  would
beneﬁt  from  rolling-origin  evaluation,  cross-validation  adapted  to  time  dependence,  external
validation across regions or periods, and calibrated uncertainty intervals. That need is visible across
energy, agriculture, health, and clinical prediction alike (Ugbehe et al., 2025; Misiurek et al., 2025; van
Klompenburg et al., 2020; World Health Organization, 2021).

3.7. Policy Implications

Several policy implications follow directly. In education, descriptive diagnostics already justify
more  sharply  targeted  aﬀordability  and  retention  interventions,  especially  where  male  dropout  is
persistently  higher  and  where  schooling  competes  with  labor-market  entry.  In  energy,  reliable

© 2026 by the author(s). Distributed under a Creative Commons CC BY  license.

Preprints.org (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 24 March 2026

doi:10.20944/preprints202603.1811.v1

6  of  8

baseline  forecasting  remains  essential,  but  planning  agencies  would  beneﬁt  from  upgrading  from
single-model  projections  to  ensemble  systems  that  account  for  structural  breaks  and  demand
nonlinearity. In agriculture, production forecasting should be integrated with data-quality audits and
gradually expanded to include climate and spatial covariates. In health, the strongest immediate use
case is a dual system in which routine surveillance forecasts are paired with anomaly-screening tools
so that unusual patterns trigger investigation before they distort program response (Parreño, 2023a,
2023c, 2023d, 2024d, 2024g; Parreño & Anter, 2025; World Health Organization, 2021).

For the Philippines speciﬁcally, the reviewed studies suggest that policy analytics should not
treat forecasting, anomaly detection, and explainability as separate agendas. Education systems need
predictive risk models built on the descriptive foundations already established. Energy systems need
scenario-aware  forecasting  that  incorporates  structural  persistence.  Agricultural  planning  needs
subnational  and  climate-sensitive  modeling.  Public  health  systems  need  routine-data  governance,
especially  in  periods  of  service  disruption  and  immunization  stress.  Clinical  prediction  needs
external validation before operational use. The most promising direction is therefore an integrated
analytics architecture in which oﬃcial time series are continuously monitored for quality, forecasted
with  sector-appropriate  models,  and  interpreted  through  policy  thresholds  rather  than  model
accuracy alone.

4. Limitations

The  corpus  is  coherent  but  heterogeneous.  It  includes  journal  articles,  a  preprint,  and  SSRN
papers, and the studies diﬀer substantially in frequency of data, forecast horizon, sample size, and
maturity of validation design. Because the evidence base mixes descriptive, predictive, and forensic
studies, direct numerical comparison across sectors is neither appropriate nor intended. In addition,
some study characteristics had to be reconstructed from publisher pages, abstracts, or metadata when
full texts were not equally accessible. These limitations do not weaken the central conclusion that the
corpus  documents  a  meaningful  evolution  in  Philippine  applied  analytics,  but  they  do  caution
against overinterpreting performance diﬀerences across domains.

5. Conclusions

The reviewed body of work shows a clear maturation in Philippine policy-oriented quantitative
analytics.  The  earliest  studies  established  descriptive  and  univariate  forecasting  baselines  using
oﬃcial  administrative  data.  Later  studies  broadened  the  toolkit  to  comparative  machine  learning,
structural-break  testing,  nonlinear  embedding,  deep  learning,  explainable  AI,  and  Benford-based
statistical  forensics.  Across  education,  energy,  agriculture,  health,  and  ﬁnance,  the  strongest
contributions  are  transparency,  policy  relevance,  and  practical  engagement  with  real  Philippine
datasets. The main next step is not merely to seek marginal gains in predictive accuracy, but to build
integrated  sectoral  analytics  that  are  multivariate,  uncertainty-aware,  externally  validated,  and
operationally linked to actual decisions. That is the path by which applied quantitative analytics can
move from useful academic exercise to durable policy infrastructure in the Philippines.

References

1.  David, C. C., Albert, J. R. G., & Vizmanos, J. F. V. (2018). Boys are still left behind in basic education (PIDS

Policy

Notes

No.

2018-20).

Philippine

Institute

for

Development

Studies.

https://doi.org/10.62986/pn2018.20

2.  Deyle, E. R., & Sugihara, G. (2011). Generalized theorems for nonlinear state space reconstruction. PLoS

ONE, 6(3), e18295. https://doi.org/10.1371/journal.pone.0018295

3.  Guo, P., Liu, T., Zhang, Q., Wang, L., Xiao, J., Zhang, Q., Luo, G., Li, Z., He, J., Zhang, Y., & Ma, W. (2017).

Developing a dengue forecast model using machine learning: A case study in China. PLoS Neglected Tropical

Diseases, 11(10), e0005973. https://doi.org/10.1371/journal.pntd.0005973

© 2026 by the author(s). Distributed under a Creative Commons CC BY  license.

Preprints.org (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 24 March 2026

doi:10.20944/preprints202603.1811.v1

7  of  8

4.  Husein, J. G., & Kara, S. M. (2023). Are shocks to electricity consumption permanent or transitory? Evidence

from a panel stationarity test with gradual structural breaks for 25 OECD countries. Applied Econometrics

and International Development, 23(1), 57-76.

5.

Idrovo, A. J., Fernández-Niño, J. A., Bojórquez-Chapela, I., & Moreno-Montoya, J. (2011). Performance of

public health surveillance systems during the influenza A(H1N1) pandemic in the Americas: Testing a new

method

based

on

Benford’s

Law.

Epidemiology

and

Infection,

139(12),

1827-1834.

https://doi.org/10.1017/S095026881100015X

6.

Jabed, M. A., & Azmi Murad, M. A. (2024). Crop yield prediction in agriculture: A comprehensive review

of machine learning and deep learning approaches, with insights for future research and sustainability.

Heliyon, 10, e40836. https://doi.org/10.1016/j.heliyon.2024.e40836

7.  Kula,  F.,  Aslan,  A.,  &  Ozturk,  I.  (2012).  Is  per  capita  electricity  consumption  stationary?  Time  series

evidence

from  OECD  countries.  Renewable  and  Sustainable  Energy  Reviews,  16(1),  501-503.

https://doi.org/10.1016/j.rser.2011.08.015

8.  Misiurek,  K.,  Olkuski,  T.,  &  Zyśk,  J.  (2025).  Review  of  methods  and  models  for  forecasting  electricity

consumption. Energies, 18(15), 4032. https://doi.org/10.3390/en18154032

9.  Morillas-Jurado, F. G., Caballer-Tarazona, M., & Caballer-Tarazona, V. (2021). Applying Benford’s Law to

monitor death registration data: A management tool for the COVID-19 pandemic. Mathematics, 10(1), 46.

10.  Parreño, S. J. (2019). Reasons for school dropout in the Philippines. SSRN. https://doi.org/10.2139/ssrn.4148093

11.  Parreño,  S.  J.  (2022a).  Forecasting  electricity  consumption  in  the  Philippines  using  ARIMA  models.

International

Journal

of

Machine

Learning

and

Computing,

12(6),

279-285.

https://doi.org/10.18178/ijmlc.2022.12.6.1112

12.  Parreño,  S.  J.  (2022b).  Analysis  and  forecasting  of  electricity  demand  in  Davao  del  Sur,  Philippines.

International

Journal

on

Soft  Computing,  Artificial

Intelligence

and  Applications,

11(2).

https://doi.org/10.5121/ijscai.2021.11202

13.  Parreño, S. J. (2022c). Application of time series analysis in forecasting coal production and consumption

in

the

Philippines.

ICTACT

Journal

on

Soft

Computing,

13(1),

2798-2804.

https://doi.org/10.21917/ijsc.2022.0398

14.  Parreño,  S.  J.  (2023a).  School  dropouts  in  the  Philippines:  Causes,  changes  and  statistics.  Sapienza:

International Journal of Interdisciplinary Studies, 4(1), e23002. https://doi.org/10.51798/sijis.v4i1.552

15.  Parreño,  S.  J.  (2023b).  Forecasting  quarterly  rice  and  corn production  in the  Philippines:  A comparative

study of seasonal ARIMA and Holt-Winters models. ICTACT Journal on Soft Computing, 14(2), 3224-3231.

https://doi.org/10.21917/ijsc.2023.0452

16.  Parreño,  S.  J.  (2023c).  Forecasting  the  total  non-coincidental  monthly  system  peak  demand  in  the

Philippines:  A  comparison  of  seasonal  autoregressive  integrated  moving  average  models  and  artificial

neural  networks.

International

Journal

of  Energy  Economics

and  Policy,

13(5),

544-552.

https://doi.org/10.32479/ijeep.14240

17.  Parreño, S. J. (2023d). Assessing the quality of dengue data in the Philippines using Newcomb-Benford law.

Sapienza: International Journal of Interdisciplinary Studies, 4(3), e23039. https://doi.org/10.51798/sijis.v4i3.662

18.  Parreño, S. J. (2024b). Analyzing crop production statistics of the Philippines using the Newcomb-Benford

law. Multidisciplinary Science Journal, 6(6), e2024079. https://doi.org/10.31893/multiscience.2024079

19.  Parreño,  S.  J.  (2024c).  Chaos  theory  enhanced  LSTM  model  of  the  Philippine  stock  exchange  index.  SN

Computer Science, 5(6), 779. https://doi.org/10.1007/s42979-024-03160-1

20.  Parreño,  S.  J.  (2024d).  Epidemiological  anomaly  detection  in  Philippine  public  health  surveillance  data

through  Newcomb-Benford

analysis.

Journal

of

Public

Health,

46(3),

e483-e493.

https://doi.org/10.1093/pubmed/fdae062

21.  Parreño, S. J. (2024e). Evaluating the underreporting of diseases in the Philippines during the COVID-19 pandemic

through comparative forecast analysis. Research Square. https://doi.org/10.21203/rs.3.rs-3837011/v1

22.  Parreño,  S.  J.  (2024f).  Enhanced  diabetes  prediction  using  principal  component  analysis  and  advanced  machine

learning algorithms. SSRN. https://doi.org/10.2139/ssrn.4932796

© 2026 by the author(s). Distributed under a Creative Commons CC BY  license.

Preprints.org (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 24 March 2026

doi:10.20944/preprints202603.1811.v1

8  of  8

23.  Parreño, S. J. (2024g). Assessing the stationarity of per capita electricity consumption: Time series analysis

in  ASEAN  countries.

International

Journal  of  Energy  Economics  and  Policy,  14(2),  46-52.

https://doi.org/10.32479/ijeep.15357

24.  Parreño, S. J. E., & Anter, M. C. J. (2024). New approach for forecasting rice and corn production in the

Philippines

through  machine

learning  models.  Multidisciplinary  Science  Journal,  6(9),  2024168.

https://doi.org/10.31893/multiscience.2024168

25.  Parreño, S. J. E., & Anter, M. C. J. V. (2025). Examining gender disparities in dropout rates in the Philippines:

A  comparative  analysis.  Sapienza:  International  Journal  of  Interdisciplinary  Studies,  6(2),  e25027.

https://doi.org/10.51798/sijis.v6i2.954

26.  Parreño,  S.  J.  E.  (2025).  Forecasting  measles  incidence  in  the  Philippines:  A  comparative  analysis  of

SARIMA,  Holt-Winters,  ESN,  and  NNAR  models.  Multidisciplinary  Science  Journal,  7(7),  2025356.

https://doi.org/10.31893/multiscience.2025356

27.  Ramadevi,  B.,  &  Bingi,  K.  (2022).  Chaotic  time  series  forecasting  approaches  using  machine  learning

techniques: A review. Symmetry, 14(5), 955. https://doi.org/10.3390/sym14050955

28.  Rumberger,  R.  W.,  &  Lim,  S.  A.  (2008).  Why  students  drop  out  of  school:  A  review  of  25  years  of  research.

California Dropout Research Project.

29.  Sabates, R., Westbrook, J., Akyeampong, K., & Hunt, F. (2010). School drop out: Patterns, causes, changes and

policies. UNESCO.

30.  Tasin,  I.,  Nabil,  T.  U.,  Islam,  S.,  &  Khan,  R.  (2023).  Diabetes  prediction  using  machine  learning  and

explainable AI techniques. Healthcare Technology Letters, 10, 1-10. https://doi.org/10.1049/htl2.12039

31.  Ugbehe, P. O., Diemuodeke, O. E., & Aikhuele, D. O. (2025). Electricity demand forecasting methodologies

and applications: A review. Sustainable Energy Research, 12, 19. https://doi.org/10.1186/s40807-025-00149-z

32.  van Klompenburg, T., Kassahun, A., & Catal, C. (2020). Crop yield prediction using machine learning: A

systematic

literature

review.  Computers

and

Electronics

in  Agriculture,

177,

105709.

https://doi.org/10.1016/j.compag.2020.105709

33.  World  Health Organization.  (2021).  Analysing  and  using  routine  data  to  monitor  the  effects  of  COVID-19 on

essential health services: Practical guide for national and subnational decision-makers.

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those

of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s)

disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or

products referred to in the content.

© 2026 by the author(s). Distributed under a Creative Commons CC BY  license.

