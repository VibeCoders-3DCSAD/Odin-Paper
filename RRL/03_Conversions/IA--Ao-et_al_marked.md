Received27July2025,accepted18August2025,dateofpublication26August2025,dateofcurrentversion8September2025.
DigitalObjectIdentifier10.1109/ACCESS.2025.3602791
A Review of Time Series Prediction Models
Based on Deep Learning
XIQINAO 1,YUJIEGONG2,ANDAIXIANGHE1
1InstituteofBigDataandArtificialIntelligence,AnhuiXinhuaUniversity,Hefei,Anhui230088,China
2SichuangElectronicsCompanyLtd.,Hefei,Anhui230088,China
Correspondingauthor:XiqinAo(aoxiqin@axhu.edu.cn)
ThisworkwassupportedinpartbytheIntelligentInformationProcessingResearchandInnovationTeamunderGrant2024AH010012,
inpartbyAnhuiProvincialUniversityScienceResearchProjectunderGrant2024AH050610,andinpartbytheInstituteofIntelligent
InformationunderGrantyjs202103.
ABSTRACT Time series data, capturing the evolution of specific variables over time, underpins critical
forecasting tasks across diverse domains. While traditional models struggle with the inherent complexity
(nonlinearity, non-stationarity, seasonality) of real-world time series, deep learning (DL) has emerged as
a transformative solution, leveraging its prowess in nonlinear modeling and automated feature extraction.
This paper provides a comprehensive review of recent advancements in DL-based time series prediction
models. We systematically analyze the characteristics, strengths, and limitations of prominent model
families, including Convolutional Neural Networks (CNNs), Recurrent Neural Networks (RNNs) (e.g.,
LSTM, GRU), Transformer variants (e.g., Informer, Autoformer, iTransformer), Graph Neural Networks
(GNNs), and hybrid models. On this basis, we establish a structured, task-oriented framework for model
selectionandcross-comparison,evaluatingthesemodelsacrossessentialdimensionssuchassequencelength
handling,multivariatesupport,interpretability,computationalefficiency,andreal-timeperformance.Finally,
addressingthechallengesandissuesfacedbydeeplearningintimeseriesprediction,thispaperprospects
future research directions, including enhancing model interpretability, optimizing model structures, and
integratingmulti-sourcedataanddomainknowledge.
INDEXTERMS Researchreview,timeseriesprediction,deeplearning.
I. INTRODUCTION Several traditional time series prediction techniques, like
Time series data, a collection of data points arranged in theARIMAmodelanditsvariants,havedemonstratedtheir
chronological order, reflects the trend of specific variables efficacyindealingwithlinearandstationarytimeseriesdata
changing over time [1], [2]. With the rapid development and have managed to attain some degree of success. [6].
of information technology, time series data has experienced However, real-world time series data often exhibit complex
explosive growth in fields such as finance, meteorology, characteristicssuchasnonlinearity,non-stationarity,andsea-
industry, transportation and healthcare, including examples sonality.Traditionalmethodsshowsignificantlimitationsin
likestockpricetrends,temperatureandprecipitationchanges, processing such data, as they struggle to capture deep-level
equipment condition monitoring, traffic flow statistics, and patterns,leadingtoinsufficientpredictionaccuracy.
forecastpatientvitalsigns[3],[4],[5].Accuratelypredicting Over the past few years, deep learning technology has
the future trends of time series data is of great significance achieved remarkable breakthroughs in areas like image
for decision-making, resource optimization, and risk early recognition and natural language processing, and it has
warning.Consequently,timeseriespredictionhasbecomea started to be utilized in time series prediction tasks [7], [8].
significantresearchfocusinbothacademiaandindustry. Deep learning models, through their multi-layer neural net-
workarchitectures,canautomaticallylearncomplexfeatures
and dependencies in time series data, thereby effectively
The associate editor coordinating the review of this manuscript and handlingnonlinearandnon-stationarydataandsignificantly
approvingitforpublicationwasWeiXu . improvingpredictionaccuracyandstability.
2025TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
153696 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ VOLUME13,2025

X.Aoetal.:ReviewofTimeSeriesPredictionModelsBasedonDeepLearning
This paper first systematically discusses the problem of researchers and practitioners face significant challenges in
timeseriesprediction,thenreviewsrelatedresearchmethods, efficientlyandeffectivelyselectingappropriatemodelsbased
and provides a detailed analysis and comparison of deep on intrinsic model properties, data characteristics, and task
learning-based approaches according to different network requirements when tackling specific forecasting problems
types. Finally, the paper prospects the future development (e.g., short-term financial volatility prediction vs. long-
directions of time series prediction technology, including term power load forecasting vs. multivariate traffic flow
| enhancing | model | interpretability, |     | optimizing | network | struc- | prediction). |     |     |     |     |     |     |     |
| --------- | ----- | ----------------- | --- | ---------- | ------- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- |
tures,andintegratingmulti-sourcedata.Thispaperaspiresto (2)Insufficientcross-modelcomparativeanalysisandlim-
offervaluablereferencesforresearchersinrelevantfieldsand ited discussion on integration trends. While the strengths
tofacilitatethefurtheradvancementandapplicationofdeep and weaknesses of various models (CNN, RNN, Trans-
learningtechnologyintimeseriesprediction. former, GNN) have been discussed, there remains a
|     |     |     |     |     |     |     | notable           | deficiency | in  | deep cross-comparisons |                 |     | of  | their core |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ---------- | --- | ---------------------- | --------------- | --- | --- | ---------- |
|     |     |     |     |     |     |     | capabilities—such |            | as  | capturing              | long/short-term |     |     | dependen-  |
II. BASICCONCEPTSANDRELATEDWORK
|     |     |     |     |     |     |     | cies, computational |     |     | efficiency, | robustness |     | to  | noise/non- |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ----------- | ---------- | --- | --- | ---------- |
A. CONCEPTSANDPROBLEMDEFINITION
|     |     |     |     |     |     |     | stationarity/seasonality, |     |     | and | interpretability. |     | Furthermore, |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | ----------------- | --- | ------------ | --- |
Timeseriespredictionreferstothetaskofforecastingfuture
|              |     |            |          |     |                 |        | analysis | of how | recent | model | integrations |     | and | architec- |
| ------------ | --- | ---------- | -------- | --- | --------------- | ------ | -------- | ------ | ------ | ----- | ------------ | --- | --- | --------- |
| values based | on  | historical | observed |     | data using time | series |          |        |        |       |              |     |     |           |
turalinnovations(e.g.,CNN-LSTM,TCN-Attention,GNN-
models.Itscoreliesinanalyzingtimeseriesdata,identifying
|     |     |     |     |     |     |     | Transformer) | address |     | the inherent | limitations |     | of  | traditional |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | --- | ------------ | ----------- | --- | --- | ----------- |
patterns,trends,andperiodiccharacteristics,andconstructing
modelsremainsunderdeveloped.
appropriatepredictionmodelstoachieveaccurateforecasts.
|      |          |            |     |              |          |        | (3) Inadequate |     | coverage | of  | strategies | for | emerging | chal- |
| ---- | -------- | ---------- | --- | ------------ | -------- | ------ | -------------- | --- | -------- | --- | ---------- | --- | -------- | ----- |
| From | a formal | definition |     | perspective, | the time | series |                |     |          |     |            |     |          |       |
lenges.Asapplicationscenariosgrowincreasinglycomplex
| prediction    | problem | can      | be described |       | as follows:   | Given an |          |        |         |            |      |       |                |     |
| ------------- | ------- | -------- | ------------ | ----- | ------------- | -------- | -------- | ------ | ------- | ---------- | ---- | ----- | -------------- | --- |
|               |         |          |              |       |               |          | and data | scales | expand, | challenges | like | model | interpretabil- |     |
| original time | series  | dataset, |              | where | each input is | a set of |          |        |         |            |      |       |                |     |
(cid:8) ,x ,x (cid:9) i t y, c o m p u t a t i o na l e ffi c i e n c y op t i mi z at io n ,fe w - s ho t l ea rn in g ,
| dynamic                        | variables | X t = | x t,1   | t,2 ···                 | t,k at time          | t, with |              |               |          |               |          |          |         |                  |
| ------------------------------ | --------- | ----- | ------- | ----------------------- | -------------------- | ------- | ------------ | ------------- | -------- | ------------- | -------- | -------- | ------- | ---------------- |
|                                |           |       |         |                         |                      |         | o n li n e l | e a r n i n g | c a p ab | i l i ti e s, | a n d d  | o m a in | k n o w | le d g e in te - |
| k being the                    | number    | of    | dynamic | features.               | The output           | of the  |              |               |          |               |          |          |         |                  |
|                                |           |       |         |                         |                      |         | gration      | have become   |          | paramount.    | Existing |          | surveys | provide          |
| modelisthepredictedlabelvaluey |           |       |         | t .Typically,theinputto |                      |         |              |               |          |               |          |          |         |                  |
|                                |           |       |         |                         |                      |         | insufficient | systematic    |          | summarization |          | of       | these   | emerging         |
| themodelisafixed-sizesetI      |           |       |         | ={X t−m                 | ,...X },representing |         |              |               |          |               |          |          |         |                  |
t challenges and targeted critiques of deep learning solutions
continuoustimeseriesdatafromtimet-mtot;theoutputisa
|         | ,...y |                                         |     |     |     |     | designedtoaddressthem. |     |     |     |     |     |     |     |
| ------- | ----- | --------------------------------------- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
| setO={y | t+1   | t+n },representingthemodel’spredictions |     |     |     |     |                        |     |     |     |     |     |     |     |
Thecorecontributionsofthissurveyare:
fornconsecutivetimepointsaftertimet[9].Here,theinput
(1)Establishingastructured,task-orientedanalysisframe-
| contains | k variables, |     | and the | output | consists of | coherent |          |      |          |         |     |     |          |        |
| -------- | ------------ | --- | ------- | ------ | ----------- | -------- | -------- | ---- | -------- | ------- | --- | --- | -------- | ------ |
|          |              |     |         |        |             |          | work for | deep | learning | models. |     | We  | not only | elabo- |
predictedvaluesforntimestamps.
|     |     |     |     |     |     |     | rate on | the core | principles |     | and evolution |     | of mainstream |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ---------- | --- | ------------- | --- | ------------- | --- |
Whenperformingtimeseriesprediction,thefirststepisto
models—includingCNNs,RNNs(LSTM/GRU),Transform-
| collectand | organizeobserved |     |     | datawith | temporalcharacter- |     |                |     |             |        |     |      |          |       |
| ---------- | ---------------- | --- | --- | -------- | ------------------ | --- | -------------- | --- | ----------- | ------ | --- | ---- | -------- | ----- |
|            |                  |     |     |          |                    |     | ers (Informer, |     | Autoformer, | etc.), | and | GNNs | (Section | III)— |
istics.Thesedatacancomefromvariousfields,suchassales
|                |             |        |          |          |               |           | but also    | place    | significant | emphasis          |     | on conducting |     | in-depth |
| -------------- | ----------- | ------ | -------- | -------- | ------------- | --------- | ----------- | -------- | ----------- | ----------------- | --- | ------------- | --- | -------- |
| over a period, | temperature |        | changes, |          | stock prices, | etc. From |             |          |             |                   |     |               |     |          |
|                |             |        |          |          |               |           | comparative | analysis |             | and applicability |     | assessments   |     | of these |
| the original   | time        | series | data,    | valuable | features are  | extracted |             |          |             |                   |     |               |     |          |
models.Thisassessmentisbasedonkeytimeseriescharac-
| through feature |     | engineering | for | effective | use by the | model. |     |     |     |     |     |     |     |     |
| --------------- | --- | ----------- | --- | --------- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
teristics(e.g.,dependencylength,trend/seasonalitystrength,
Properselectionandconstructionoffeaturescansignificantly
|     |     |     |     |     |     |     | inter-variable |     | relationships, |     | noise | levels) | and | core task |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------------- | --- | ----- | ------- | --- | --------- |
enhancetheperformanceofthepredictionmodel.
requirements(e.g.,forecastinghorizon,real-timeconstraints,
interpretabilityneeds).
B. RELATEDWORK (2) Providing in-depth discussions on model synergy and
In recent years, with the explosive growth of deep learning innovation. Beyond analyzing the merits and drawbacks of
models in the field of time series forecasting, a substan- individual models, we focus on the design philosophy of
tial body of related survey literature has emerged [3], [8], hybridmodelsandstructuralinnovations(e.g.,TCN,SCINet)
[10]. These reviews systematically outline the evolutionary andcriticallyexaminetheireffectivenessinovercominglimi-
trajectory of model architectures, their core principles, and tationsinherenttotraditionalmodels(e.g.,gradientvanishing
their applications in specific domains. However, analysis inRNNs,computationalcomplexityofTransformers).
of the existing literature reveals several critical research (3) Placing significant emphasis on cutting-edge chal-
gaps: lenges and pragmatic solutions. We specifically focus on
(1) A lack of practical model selection guidelines. Exist- and critique the latest research advances addressing critical
ing surveys tend to focus either on in-depth analysis of challenges, including model interpretability (e.g., atten-
single-category models (e.g., RNNs, Transformers) or pro- tionweightanalysis),computationalefficiencyoptimization
vide enumerative descriptions of a broad range of models. (e.g.,sparseattention,modeldistillation),online/incremental
Yet, they lack a systematic, application-oriented frame- learning,andtheintegrationofmulti-sourcedataanddomain
| work for      | model | selection | and | comparison. | Consequently, |     | knowledge. |     |     |     |     |     |     |        |
| ------------- | ----- | --------- | --- | ----------- | ------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | ------ |
| VOLUME13,2025 |       |           |     |             |               |     |            |     |     |     |     |     |     | 153697 |

X.Aoetal.:ReviewofTimeSeriesPredictionModelsBasedonDeepLearning
III. TIMESERIESPREDICTIONMETHODSBASEDON
DEEPLEARNING
A. OVERVIEWOFDEEPLEARNING
| Time series | prediction   |             | is a            | crucial technology |               | for            | forecast- |     |     |     |     |     |     |     |
| ----------- | ------------ | ----------- | --------------- | ------------------ | ------------- | -------------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| ing future  | trends       | by          | analyzing       | historical         |               | data,          | and it is |     |     |     |     |     |     |     |
| widely      | applied      | in fields   | such            | as financial       |               | market         | analysis, |     |     |     |     |     |     |     |
| weather     | forecasting, |             | and healthcare. |                    | With          | the continuous |           |     |     |     |     |     |     |     |
| advancement | of           | data        | collection      | technologies,      |               | the scale      | and       |     |     |     |     |     |     |     |
| complexity  | of           | time series | data            | have               | significantly | increased.     |           |     |     |     |     |     |     |     |
Traditionalstatisticalmethodsandmachinelearningmodels
| face numerous |       | challenges |           | when dealing  |     | with large-scale, |     |     |     |     |     |     |     |     |
| ------------- | ----- | ---------- | --------- | ------------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| nonlinear     | data, | such       | as high   | computational |     | complexity        | and |     |     |     |     |     |     |     |
| difficulties  | in    | capturing  | nonlinear | relationships |     | within            | the |     |     |     |     |     |     |     |
data[11].Deeplearningmodels,withtheirpowerfulnonlin- FIGURE1. Structureofone-dimensionalconvolutionalnetwork.
| ear modeling   |     | capabilities | and       | automatic | feature | extraction, |      |        |     |     |     |     |     |     |
| -------------- | --- | ------------ | --------- | --------- | ------- | ----------- | ---- | ------ | --- | --- | --- | --- | --- | --- |
| have gradually |     | become       | effective | tools     | for     | addressing  | time |        |     |     |     |     |     |     |
|                |     |              |           |           |         |             |      | 2) TCN |     |     |     |     |     |     |
seriespredictionproblems.
TheTemporalConvolutionalNetwork(TCN)isaninnovative
Deeplearningmodels,particularlydeepneuralnetworks,
|            |          |       |            |         |               |     |           | architecture | that is based     | on     | convolutional |            | neural networks. |        |
| ---------- | -------- | ----- | ---------- | ------- | ------------- | --- | --------- | ------------ | ----------------- | ------ | ------------- | ---------- | ---------------- | ------ |
| are valued | for      | their | capability | to      | automatically |     | extract   |              |                   |        |               |            |                  |        |
|            |          |       |            |         |               |     |           | Unlike       | traditional CNNs, | TCN    | is able       | to capture | long-term        |        |
| high-level | features | from  | data       | through | multiple      |     | layers of |              |                   |        |               |            |                  |        |
|            |          |       |            |         |               |     |           | dependencies | in time           | series | data          | by using   | dilated          | causal |
nonlineartransformations.Deepneuralnetworksbuildrepre-
|     |     |     |     |     |     |     |     | convolutions | and residual | connections |     | [14]. | The core | idea |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------ | ----------- | --- | ----- | -------- | ---- |
sentationsofhistoricaltimeseriesfeaturesthroughmultiple
|     |     |     |     |     |     |     |     | of TCN | is to expand | the receptive |     | field of | convolutions | to  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------------ | ------------- | --- | -------- | ------------ | --- |
nonlinearlayerstouncovertheinternalpatternsoftimeseries
capturelong-rangetemporaldependencieswhileavoidingthe
| data. [12]. | During | the | learning | process | of  | neural networks, |     |     |     |     |     |     |     |     |
| ----------- | ------ | --- | -------- | ------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
leakageoffutureinformation.
relevanthistoricaltimeseriesinformationcanbeconsidered
DilatedcausalconvolutionisthecorecomponentofTCN,
| as being | encoded | into | hidden | variables, |     | which ultimately |     |     |     |     |     |     |     |     |
| -------- | ------- | ---- | ------ | ---------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
combiningtheadvantagesofcausalconvolutionanddilated
becometheoutputofthesehiddenvariablesandthecurrent
convolution[15].However,amajordrawbackofcausalcon-
input.Fordifferentapplicationscenarios,variousimplemen-
|     |     |     |     |     |     |     |     | volution | is that capturing | long-range |     | dependencies |     | requires |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------------- | ---------- | --- | ------------ | --- | -------- |
tationsofhiddenlayersareadoptedindeeplearning,leading
eitherextremelydeepnetworksorlargefilters,whichsignif-
totheuseofdifferentneuralnetworkarchitectures.Through
|     |     |     |     |     |     |     |     | icantly | increases computational |     | complexity. |     | To address | this |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------------------- | --- | ----------- | --- | ---------- | ---- |
research,deeplearning-basedmethodshavebeencategorized
issue,TCNintroducesdilatedconvolution,whichexpandsthe
systematically.
receptivefieldbyincreasingthedilationfactor(d)ofthecon-
volutionalkernel.Thestructureofdilatedcausalconvolution
isillustratedinFigure2.
B. METHODSBASEDONCONVOLUTIONALNEURAL
NETWORKS
1) CNN
| Convolutional |       | Neural       | Networks | (CNNs)      | are | a type | of deep  |     |     |     |     |     |     |     |
| ------------- | ----- | ------------ | -------- | ----------- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
| learning      | model | particularly |          | well-suited | for | image  | recogni- |     |     |     |     |     |     |     |
tionandprocessingtasks.Theircorestrengthliesinfeature
| extraction   | through       | convolutional |          | layers      | and | pooling    | layers. |     |     |     |     |     |     |     |
| ------------ | ------------- | ------------- | -------- | ----------- | --- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| CNNs perform |               | convolution   |          | operations  | on  | input data | using   |     |     |     |     |     |     |     |
| sliding      | convolutional |               | kernels, | effectively |     | extracting | local   |     |     |     |     |     |     |     |
spatial features. By employing a weight-sharing strategy— FIGURE2. Structureofdilatedcausalconvolution.
| where the | same | convolutional |     | kernel | uses | identical | weight |     |     |     |     |     |     |     |
| --------- | ---- | ------------- | --- | ------ | ---- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
parametersacrossdifferentpositionsoftheinput—CNNssig- TCN Residual Block: As the depth of the network
nificantlyreducethenumberofnetworkparameters,thereby increases, TCN training may face issues such as vanish-
improvingcomputationalefficiency[13].CNNconsistofan ing or exploding gradients. To address this problem, TCN
input layer, convolutional layers, pooling layers, fully con- introduces residual connections [16]. Residual connections
nectedlayers,andanoutputlayer,asillustratedinFigure1. alleviate training difficulties in deep networks by directly
CNNs excel at extracting local spatial patterns through addingtheinputtotheoutput,improvingmodelstabilityand
convolutionalfiltersandpoolingoperations,benefitingfrom convergencespeed.ThestructureofaTCNresidualblockis
parameter sharing for efficiency and translation invariance. showninFigure3.
However,standardCNNsoftenstruggletocapturelong-range Insummary,TCNadherestotwoprinciples:theinputand
dependenciesinherentinmanytimeseriesandlackinherent outputlengthsproducedbythenetworkarethesame,andno
mechanismstomodeltemporalorderexplicitly. future information is leaked. These principles are achieved
| 153698 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

X.Aoetal.:ReviewofTimeSeriesPredictionModelsBasedonDeepLearning
|     |     |     |     |     |     |     |     | However, | the method relies | on  | a fixed hierarchical | network |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------------- | --- | -------------------- | ------- |
structure,whichmayleadtoinsufficientadaptabilitytocom-
plexordynamicallychangingtimeseries.
4) COMPARATIVEANALYSISOFCNN-BASEDALGORITHMS
ConvolutionalNeuralNetworks(CNNs)andtheirimproved
|     |     |     |     |     |     |     |     | variants have | demonstrated | excellent | performance | in time |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------------ | --------- | ----------- | ------- |
FIGURE3. StructureofTCNresidualblock.
|     |     |     |     |     |     |     |     | series prediction | tasks, | particularly | when the sample | size is |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ------ | ------------ | --------------- | ------- |
sufficient,astheycaneffectivelyhandleshort-termprediction
through the use of one-dimensional fully convolutional net- tasks. A comparison analysis of CNN-based algorithms is
works(1DFCN)andcausalconvolutions,asillustratedinthe summarizedinTable1.
figureabove.TheformulaforTCNcanbesimplifiedas[17]:
TABLE1. AnalysisofCNN-basedalgorithms.
|     | TCN=1DFCN+causal |     |     |     | convolutions |     | (1) |     |     |     |     |     |
| --- | ---------------- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
3) OTHERCNN-BASEDIMPROVEDMODELS
Inthefieldoftimeseriesprediction,manyresearchershave
improvedtraditionalConvolutionalNeuralNetworks(CNNs)
| by incorporating |     | specific |     | application | scenarios, |     | proposing |     |     |     |     |     |
| ---------------- | --- | -------- | --- | ----------- | ---------- | --- | --------- | --- | --- | --- | --- | --- |
variousefficientCNNvariants.Theseimprovedmodelssig-
| nificantly | enhance |     | the performance |     | of CNNs     | in  | time series   |     |     |     |     |     |
| ---------- | ------- | --- | --------------- | --- | ----------- | --- | ------------- | --- | --- | --- | --- | --- |
| prediction | tasks   | by  | introducing     |     | new network |     | structures or |     |     |     |     |     |
optimizationstrategies.
| In         | 2017, | Borovykh   | et         | al. [18]          | proposed |             | an improved |     |     |     |     |     |
| ---------- | ----- | ---------- | ---------- | ----------------- | -------- | ----------- | ----------- | --- | --- | --- | --- | --- |
| CNN        | model | inspired   | by         | the               | WaveNet  | speech      | sequence    |     |     |     |     |     |
| generation |       | model.     | This model | adopts            | the      | ReLU        | activation  |     |     |     |     |     |
| function   | and   | parametric |            | skip connections, |          | simplifying | the         |     |     |     |     |     |
structure.Experimentsshowthatthismodelperformsexcep-
| tionally | well        | in financial |          | time     | series prediction |               | tasks, not  |     |     |     |     |     |
| -------- | ----------- | ------------ | -------- | -------- | ----------------- | ------------- | ----------- | --- | --- | --- | --- | --- |
| only     | simplifying | the          | training | process  | but               | also          | maintaining |     |     |     |     |     |
| high     | prediction  | accuracy     |          | in noisy | data              | environments. | This        |     |     |     |     |     |
improvementdemonstratesthepotentialofconvolutionalnet-
worksinhandlingcomplextimeseriesdata.
| As              | dataset    | sizes | continue      | to   | grow,      | traditional | CNNs        |     |     |     |     |     |
| --------------- | ---------- | ----- | ------------- | ---- | ---------- | ----------- | ----------- | --- | --- | --- | --- | --- |
| face            | challenges | in    | computational |      | efficiency | when        | process-    |     |     |     |     |     |
| ing large-scale |            | data. | In 2017,      | Dong | et         | al. [19]    | proposed an |     |     |     |     |     |
improvedmodelthatcombinesCNNwiththeK-meansclus-
teringalgorithm.ThismodelemploysK-meansclusteringto
CNN:Suitableforshort-termtimeseriespredictiontasks,
dividelargedatasetsintosmallersubsetsofsimilarsamples especially in scenarios with prominent local features(e.g.,
andsubsequentlytrainsCNNmodelsoneachofthesesubsets ECGabnormalitydetection).
individually.Thisapproachhasshownexcellentperformance TCN:Suitableforlong-sequencepredictiontasks,capable
inpredictiontasksonmillion-scalepowerloaddatasets,sig- ofcapturinglong-termdependencies(e.g.,longtermforecast-
nificantlyimprovingcomputationalefficiencyandprediction ingofurbanpowerload).
accuracy. WaveNet-CNN: Primarily applicable to audio and time
Liuetal.[20]proposedSCINet(SampleConvolutionand series generation tasks(e.g.,speech emotion synthesis), with
Interaction Network), which adopts a hierarchical convo- limitedsuitabilityforothertypesoftimeseriesprediction.
lutional network structure. SCINet uses a binary tree-like Kmeans-CNN: Suitable for large-scale time series pre-
architecture to iteratively extract and aggregate features at diction tasks, effectively handling noise and complexity in
various time resolutions, thereby learning effective repre- data(e.g., Smart grid abnormal power consumption detec-
| sentations |     | that have | improved |     | predictability. |     | Within each | tion). |     |     |     |     |
| ---------- | --- | --------- | -------- | --- | --------------- | --- | ----------- | ------ | --- | --- | --- | --- |
SCI-Block, the time series is split into two parts. As the SCINet: Suitable for time series prediction tasks with
depth of the binary tree grows, the network is able to significant seasonality and trends, capable of capturing
extract more detailed temporal information. In this manner, multi-scale temporal dependencies (e.g.,holiday retail sales
| SCINet | is  | capable | of capturing |     | both short-term |     | and long- | forecast). |     |     |     |     |
| ------ | --- | ------- | ------------ | --- | --------------- | --- | --------- | ---------- | --- | --- | --- | --- |
termdependenciesintimeseriesdataatthesametime,which Beyondthelistedstrengthsandlimitations,CNNvariants
leadstoasubstantialenhancementinpredictionperformance. involvekeytrade-offs:
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     | 153699 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

X.Aoetal.:ReviewofTimeSeriesPredictionModelsBasedonDeepLearning
| Long-range      | vs.           | Efficiency/Complexity: |         |                  | TCN    | and        | SCINet     |     |     |     |     |     |     |     |     |
| --------------- | ------------- | ---------------------- | ------- | ---------------- | ------ | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| address         | standard      | CNNs’                  | limited | receptive        |        | field      | (TCN via   |     |     |     |     |     |     |     |     |
| dilated         | convolutions, | SCINet                 |         | via hierarchical |        | decomposi- |            |     |     |     |     |     |     |     |     |
| tion). However, |               | this significantly     |         | increases        |        | model      | depth,     |     |     |     |     |     |     |     |     |
| complexity,     | and           | computational          |         | cost,            | making | them       | less effi- |     |     |     |     |     |     |     |     |
cientandhardertotrain/tunethanshallowCNNs.
AutomatedFeaturesvs.Interpretability/Specificity:While
| powerful  | for local     | pattern |        | extraction, | the    | learned   | fea- |     |     |     |     |     |     |     |     |
| --------- | ------------- | ------- | ------ | ----------- | ------ | --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| tures are | often opaque. |         | Models | like        | SCINet | (designed | for  |     |     |     |     |     |     |     |     |
trends/seasonality)orK-means-CNN(dependentoncluster-
ing)riskpoorgeneralizationifdatacharacteristicsmismatch
| their design | assumptions, |     | and | offer | limited | insight | into fea- |     |     |     |     |     |     |     |     |
| ------------ | ------------ | --- | --- | ----- | ------- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
tureimportance.
SelectionImplication:PrioritizeTCN/SCINetonlyifcap-
FIGURE5. StructureofLSTM.
| turing long-term/multi-scale |     |     |     | dependencies |     | is critical | and |     |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | ------------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
resourcesallow.SimplerCNNsorothermodels(e.g.,RNNs
|              |          |     |        |            |     |                |     | due to issues | like  | vanishing | gradients |          | and exploding |     | gra-   |
| ------------ | -------- | --- | ------ | ---------- | --- | -------------- | --- | ------------- | ----- | --------- | --------- | -------- | ------------- | --- | ------ |
| for moderate | lengths) |     | may be | preferable |     | for efficiency | or  |               |       |           |           |          |               |     |        |
|              |          |     |        |            |     |                |     | dients. In    | order | to tackle | this      | problem, | Hochreiter    |     | et al. |
interpretability.
|     |     |     |     |     |     |     |     | introduced | the Long   | Short-Term |     | Memory       | (LSTM) | network |      |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | ---------- | --- | ------------ | ------ | ------- | ---- |
|     |     |     |     |     |     |     |     | back in    | 1997 [23]. | LSTM       | is  | an extension |        | of RNN  | that |
C. METHODSBASEDONRECURRENTNEURAL
|     |     |     |     |     |     |     |     | effectively | captures | and | stores | long-term | dependencies |     | by  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | ------ | --------- | ------------ | --- | --- |
NETWORKS
introducinga‘‘gatingmechanism.’’LSTMcanextractimpor-
1) RNN
|     |     |     |     |     |     |     |     | tant features | from | input | data | and retain | this | information |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---- | ----- | ---- | ---------- | ---- | ----------- | --- |
RecurrentNeuralNetworks(RNNs)areatypeofdeeplearn-
|     |     |     |     |     |     |     |     | over extended | periods, |     | making | it particularly |     | effective | in  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | --- | ------ | --------------- | --- | --------- | --- |
ingmodelproposedbyJordanin1990,specificallydesigned
|     |     |     |     |     |     |     |     | long-term | time | series | prediction | tasks. | The | fundamental |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---- | ------ | ---------- | ------ | --- | ----------- | --- |
tohandledatawithtemporalcharacteristics[21].Thedesign
|               |        |                  |     |       |             |             |          | structure    | of LSTM | is composed |       | of three | gating | units: | the   |
| ------------- | ------ | ---------------- | --- | ----- | ----------- | ----------- | -------- | ------------ | ------- | ----------- | ----- | -------- | ------ | ------ | ----- |
| philosophy    | ofRNNs | isbased          |     | onthe | ideathat    | ‘‘humancog- |          |              |         |             |       |          |        |        |       |
|               |        |                  |     |       |             |             |          | Forget Gate, | the     | Input       | Gate, | and the  | Output | Gate.  | These |
| nition relies | on     | past experiences |     | and   | memories,’’ |             | enabling |              |         |             |       |          |        |        |       |
gatesareresponsibleforcontrollingtheforgetting,updating,
| them to | process | temporal | dependencies |     | in  | time | series data |     |     |     |     |     |     |     |     |
| ------- | ------- | -------- | ------------ | --- | --- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
andoutputtingofinformation,respectively.Thestructureof
| by memorizing | historical |     | information. |     | Initially, |     | RNNs saw |     |     |     |     |     |     |     |     |
| ------------- | ---------- | --- | ------------ | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
LSTMisillustratedinFigure5.
widespreadapplicationinnaturallanguageprocessingtasks,
|               |          |     |             |     |              |     |          | The Gated | Recurrent |        | Unit (GRU)      | is  | an improved |        | model |
| ------------- | -------- | --- | ----------- | --- | ------------ | --- | -------- | --------- | --------- | ------ | --------------- | --- | ----------- | ------ | ----- |
| like language | modeling |     | and machine |     | translation. |     | However, |           |           |        |                 |     |             |        |       |
|               |          |     |             |     |              |     |          | proposed  | based     | on the | Long Short-Term |     | Memory      | (LSTM) |       |
theyhavealsodemonstratedoutstandingperformanceintime
|                   |     |        |            |     |           |      |        | network.         | GRU | retains      | the core | idea    | of LSTM, | i.e.,       | cap- |
| ----------------- | --- | ------ | ---------- | --- | --------- | ---- | ------ | ---------------- | --- | ------------ | -------- | ------- | -------- | ----------- | ---- |
| series prediction |     | tasks, | especially | in  | scenarios | that | demand |                  |     |              |          |         |          |             |      |
|                   |     |        |            |     |           |      |        | turing long-term |     | dependencies |          | through | gating   | mechanisms, |      |
thecaptureoflong-termdependencies.Themostbasicstruc-
butitsnetworkstructureismoresimplified.GRUintegrates
| ture of     | an RNN | is shown | in     | Figure | 4, consisting |        | of four  |             |        |              |     |           |      |        |        |
| ----------- | ------ | -------- | ------ | ------ | ------------- | ------ | -------- | ----------- | ------ | ------------ | --- | --------- | ---- | ------ | ------ |
|             |        |          |        |        |               |        |          | the ‘‘input | gate’’ | and ‘‘forget |     | gate’’ of | LSTM | into a | single |
| components: | the    | input    | x, the | output | y, the        | hidden | state h, |             |        |              |     |           |      |        |        |
i i i ‘‘update gate’’ and adds a ‘‘reset gate’’ to manage the flow
andtheRNNcell[22].
|     |     |     |     |     |     |     |     | of information. |     | This design | not | only | reduces | the number |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----------- | --- | ---- | ------- | ---------- | --- |
ofmodelparametersandcomputationalcomplexitybutalso
|     |     |     |     |     |     |     |     | mitigates    | the vanishing |     | and exploding |        | gradient | problems | to  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- | --- | ------------- | ------ | -------- | -------- | --- |
|     |     |     |     |     |     |     |     | some extent. | [24].         | The | structure     | of GRU | [25]     | is shown | in  |
Figure6.
FIGURE4. StructureofasimpleRNN.
| RNNs     | are naturally           |            | suited    | for sequential |               | data     | by main-  |     |     |     |     |     |     |     |     |
| -------- | ----------------------- | ---------- | --------- | -------------- | ------------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| taining  | a hidden                | state that | acts      | as a           | memory        | of past  | inputs.   |     |     |     |     |     |     |     |     |
| Standard | RNNs                    | process    | sequences |                | step-by-step, |          | allowing  |     |     |     |     |     |     |     |     |
| them to  | model temporal          |            | order     | explicitly.    | However,      |          | they are  |     |     |     |     |     |     |     |     |
| prone to | the vanishing/exploding |            |           | gradient       |               | problem, | which     |     |     |     |     |     |     |     |     |
| severely | limits their            | ability    | to        | capture        | long-term     |          | dependen- |     |     |     |     |     |     |     |     |
cies.
FIGURE6. StructureofGRU.
2) LSTMANDGRU:GATEDARCHITECTURES Long Short-Term Memory (LSTM) networks overcome
While RNNs excel at processing time series data, they the gradient limitations of RNNs through a sophisticated
encounter difficulties in capturing long-term dependencies gating mechanism (Forget Gate, Input Gate, Output Gate)
| 153700 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

X.Aoetal.:ReviewofTimeSeriesPredictionModelsBasedonDeepLearning
andamemorycell,enablingselectiveretentionandupdating TheevolutionfromRNNstoLSTM/GRUinvolvesfunda-
of information over long sequences. Gated Recurrent Units mentaltrade-offs:
(GRU)offerastreamlinedalternativebymergingtheforget Memoryvs.Cost/Parallelism:Gatingmechanisms(LSTM’s
and input gates into an update gate and introducing a reset 3 gates, GRU’s 2 gates) effectively solve the vanishing gra-
gate,reducingcomputationalcomplexitywhileoftenachiev- dientproblem,enablinglong-termmemory.Thiscomesata
ingcomparableperformancetoLSTM. high computational cost per step and inherently sequential
LSTM/GRU have been widely applied to various time processing, severely limiting training parallelism and speed
series forecasting tasks, including network traffic predic- compared to CNNs/Transformers. GRU offers a lower-cost
tion [26], power load forecasting [27], equipment failure alternativetoLSTMwithcomparableperformanceinmany
| prediction [28], | electric |     | vehicle charging |     | demand | predic- | cases. |     |     |     |     |     |     |     |
| ---------------- | -------- | --- | ---------------- | --- | ------ | ------- | ------ | --- | --- | --- | --- | --- | --- | --- |
tion[29],trafficflowprediction[30],ande-commercesales Flexibility vs. Overfitting/Data Hunger: Their general-
forecastingduringpromotions[31],[32]. purposesequentialmodelingcapabilityisversatile.However,
|     |     |     |     |     |     |     | this power | increases | overfitting |     | risk | (especially | for | smaller |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ----------- | --- | ---- | ----------- | --- | ------- |
3) COMPARATIVEANALYSISOFRNN-BASEDALGORITHMS datasets)andoftendemandsmoredatathansimplermodels
Recurrent neural network-based algorithms have long been toachieverobustness.
essential methods for solving time series prediction tasks. Selection Implication: Choose LSTM/GRU when mod-
They are often embedded as modules in other algorithms eling order and causality is paramount for medium/long
to achieve better prediction performance and served as the dependencies,andsequentialprocessingisacceptable.GRU
primarymodels fortimeseriesdata predictionbefore2017, is often the pragmatic default; use LSTM if maximum rep-
|                 |     |               |              |     |          |     | resentational | power | is needed. |     | Consider | alternatives |     | (TCN, |
| --------------- | --- | ------------- | ------------ | --- | -------- | --- | ------------- | ----- | ---------- | --- | -------- | ------------ | --- | ----- |
| with widespread |     | applications. | A comparison |     | analysis | of  |               |       |            |     |          |              |     |       |
RNN-basedalgorithmsissummarizedinTable2. Transformer)forverylongsequencesorwhenparallelspeed
iscritical.
TABLE2. AnalysisofRNN-basedalgorithms.
|     |     |     |     |     |     |     | D. METHODSBASEDONTRANSFORMER |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | 1) TRANSFORMER               |     |     |     |     |     |     |     |
TheTransformermodelwasintroducedbyVaswanietal.in
2017andwasinitiallyutilizedinnaturallanguageprocessing
tasks.ItscoreideareliesentirelyontheSelf-AttentionMech-
anismtocapturelong-rangedependenciesinsequences[33].
|     |     |     |     |     |     |     | Unlike traditional |           | Recurrent | Neural        |         | Networks    | (RNNs)      | and |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --------- | --------- | ------------- | ------- | ----------- | ----------- | --- |
|     |     |     |     |     |     |     | Convolutional      | Neural    | Networks  |               | (CNNs), | the         | Transformer |     |
|     |     |     |     |     |     |     | discards           | recurrent | and       | convolutional |         | operations, | depending   |     |
solelyonattentionmechanismsforsequencemodeling.This
|     |     |     |     |     |     |     | design not | only | significantly |     | enhances | parallel | computing |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ------------- | --- | -------- | -------- | --------- | --- |
capabilitiesbutalsoenablesprocessingoflongersequences
|     |     |     |     |     |     |     | while dramatically |     | improving |     | training |     | and | inference |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --------- | --- | -------- | --- | --- | --------- |
efficiency.
|     |     |     |     |     |     |     | The overall | architecture |     | of  | the Transformer |     | follows | an  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | --- | --- | --------------- | --- | ------- | --- |
Encoder-Decoderframework[34],asillustratedinFigure7.
Boththeencoderanddecoderconsistofmultiplestackedlay-
ers,eachcontainingMulti-HeadSelf-Attentionmechanisms
| RNN: A | foundational |     | model suitable | for | short-term | time |     |     |     |     |     |     |     |     |
| ------ | ------------ | --- | -------------- | --- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
andFeed-ForwardNeuralNetworks.
seriespredictiontasks,especiallyinscenarioswithprominent
|     |     |     |     |     |     |     | The Transformer |     | architecture |     | revolutionized |     |     | sequence |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------------ | --- | -------------- | --- | --- | -------- |
localfeatures(e.g.,short-termstockpricefluctuations,sensor
|                   |          |     |              |      |                |     | modeling         | by relying | solely |            | on the | self-attention   |     | mecha- |
| ----------------- | -------- | --- | ------------ | ---- | -------------- | --- | ---------------- | ---------- | ------ | ---------- | ------ | ---------------- | --- | ------ |
| data prediction). | However, |     | it struggles | with | long sequences |     |                  |            |        |            |        |                  |     |        |
|                   |          |     |              |      |                |     | nism, dispensing |            | with   | recurrence |        | and convolution. |     | This   |
andgradientissues.
allowsittocapturelong-rangedependencieseffectivelyand
| LSTM: Addresses |     | RNN’s | gradient | problems |     | through |     |     |     |     |     |     |     |     |
| --------------- | --- | ----- | -------- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
enablesmassiveparallelizationduringtraining.However,the
| gating mechanisms, |     | making | it suitable | for | long-sequence |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | ------ | ----------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
self-attentionmechanismhasquadratictimeandspacecom-
| prediction tasks | (e.g., | power     | load forecasting, |     | weather | data    |                 |      |         |     |          |        |     |          |
| ---------------- | ------ | --------- | ----------------- | --- | ------- | ------- | --------------- | ---- | ------- | --- | -------- | ------ | --- | -------- |
|                  |        |           |                   |     |         |         | plexity (O(L2)) | with | respect | to  | sequence | length | L,  | posing a |
| prediction)      | where  | long-term | dependencies      |     | need to | be cap- |                 |      |         |     |          |        |     |          |
significantchallengeforverylongtimeseriesforecasting.
tured.Itsdrawbacksincludehighcomputationalcomplexity.
| GRU: A | simplified |     | version | of LSTM, | ideal | for |     |     |     |     |     |     |     |     |
| ------ | ---------- | --- | ------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
small/medium-scale datasets or resource-constrained sce- 2) INFORMER
narios (e.g., traffic flow prediction, promotional sales While the Transformer model exhibits powerful sequence
forecasting).Whileefficient,itsperformancemaylagbehind modeling capabilities, its self-attention mechanism suffers
LSTMincomplextasks. from quadratic growth in time and space complexity as
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 153701 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

X.Aoetal.:ReviewofTimeSeriesPredictionModelsBasedonDeepLearning
|     |     |     |     |     |     |     | via a fully | connected |     | layer | to generate | the | final | prediction |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | --- | ----- | ----------- | --- | ----- | ---------- |
outcomes.
3) AUTOFORMER
|     |     |     |     |     |     |     | Prior to | the proposal |     | of Autoformer, |     | Transformer-based |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | --- | -------------- | --- | ----------------- | --- | --- |
modelsprimarilyreliedonself-attentionmechanismstocap-
|     |     |     |     |     |     |     | ture long-term |     | dependencies |     | in sequences. |     | However, | when |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------ | --- | ------------- | --- | -------- | ---- |
handlingcomplextimeseriesdatawithlong-termfuturehori-
zons,traditionalTransformermodelsoftenstruggletoeffec-
|     |     |     |     |     |     |     | tively capture | reliable |     | dependencies. |     | Additionally, |     | although |
| --- | --- | --- | --- | --- | --- | --- | -------------- | -------- | --- | ------------- | --- | ------------- | --- | -------- |
|     |     |     |     |     |     |     | Informer       | improves | the | efficiency    | of  | long-sequence |     | process- |
ingthroughsparseself-attentionmechanisms,itsinformation
|     |     |     |     |     |     |     | utilization | still | faces | bottlenecks. |     | To address | these | issues, |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ----- | ------------ | --- | ---------- | ----- | ------- |
researchersproposedAutoformer,anovelarchitecturebased
|     |     |     |     |     |     |     | on an Auto-Correlation |             |        | Mechanism |          | and           | series  | decompo-  |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | ----------- | ------ | --------- | -------- | ------------- | ------- | --------- |
|     |     |     |     |     |     |     | sition. Autoformer     |             | embeds |           | series   | decomposition |         | into the  |
|     |     |     |     |     |     |     | model’s                | fundamental |        | modules,  | endowing |               | it with | the capa- |
bilityforprogressivedecompositionofcomplextimeseries.
|     |     |     |     |     |     |     | Simultaneously, |     | it replaces |     | the | traditional | self-attention |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----------- | --- | --- | ----------- | -------------- | --- |
FIGURE7. Structureoftransformer.
|     |     |     |     |     |     |     | mechanism | with | the | auto-correlation |     | mechanism, |     | signifi- |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---- | --- | ---------------- | --- | ---------- | --- | -------- |
cantlyenhancinginformationutilizationefficiency[37].The
the sequence length increases, limiting its effectiveness overallstructureofAutoformerisillustratedinFigure9.
| in long-sequence |          | prediction |          | tasks [35]. | To address        | this, |     |     |     |     |     |     |     |     |
| ---------------- | -------- | ---------- | -------- | ----------- | ----------------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| researchers      | proposed | the        | Informer | model       | for long-sequence |       |     |     |     |     |     |     |     |     |
forecasting.Informerintroducesthreekeyinnovations:
| ProbSparse | Self-Attention |     | Mechanism: |     | Reduces | the time |     |     |     |     |     |     |     |     |
| ---------- | -------------- | --- | ---------- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
andspacecomplexityfromO(L2
)toO(LlogL),whereLis
thesequencelength.
| Self-Attention  |     | Distilling    | Mechanism: |          | Shortens  | the input |     |     |     |     |     |     |     |     |
| --------------- | --- | ------------- | ---------- | -------- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| sequence length |     | by distilling |            | dominant | features, | thereby   |     |     |     |     |     |     |     |     |
reducingcomputationalandmemorycosts.
FIGURE9. Structureofautoformer.
| Generative-Style |     | Decoder: | Directly |     | generates | predictions |     |     |     |     |     |     |     |     |
| ---------------- | --- | -------- | -------- | --- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
inasingleforwardstepduringinference,ratherthanusinga
|     |     |     |     |     |     |     | The | encoder | and | decoder | parts | of  | Autoformer | both |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------- | ----- | --- | ---------- | ---- |
step-by-stepautoregressiveapproach,significantlyreducing
|     |     |     |     |     |     |     | include | three | modules: | the | auto-correlation |     | mechanism, |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----- | -------- | --- | ---------------- | --- | ---------- | --- |
predictiontime.
|             |              |     |     |              |       |         | series decomposition, |         |             | and | feed-forward |          | networks.  | The |
| ----------- | ------------ | --- | --- | ------------ | ----- | ------- | --------------------- | ------- | ----------- | --- | ------------ | -------- | ---------- | --- |
| The overall | architecture |     | of  | the Informer | model | [36] is |                       |         |             |     |              |          |            |     |
|             |              |     |     |              |       |         | encoder               | focuses | on modeling |     | the          | seasonal | components | of  |
illustratedinFigure8.
|     |     |     |     |     |     |     | the sequence,  | and         | the         | output               | containing | past        | seasonal           | com-       |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ----------- | ----------- | -------------------- | ---------- | ----------- | ------------------ | ---------- |
|     |     |     |     |     |     |     | ponents        | is provided |             | as cross-information |            |             | to the             | decoder    |
|     |     |     |     |     |     |     | for prediction |             | processing. | The                  | decoder    | is          | mainly             | divided    |
|     |     |     |     |     |     |     | into two       | parts:      | cumulative  | operations           |            | for         | the trend-cyclical |            |
|     |     |     |     |     |     |     | components     | and         | stacked     | auto-correlation     |            |             | mechanisms         | for        |
|     |     |     |     |     |     |     | the seasonal   | components  |             | output               | by         | the encoder |                    | [38]. Each |
decoderlayercontainsaninnerauto-correlationmechanism
|     |     |     |     |     |     |     | and an encoder-decoder |      |     | auto-correlation |        | mechanism,  |     | which       |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | ---- | --- | ---------------- | ------ | ----------- | --- | ----------- |
|     |     |     |     |     |     |     | respectively           | help | the | model            | refine | predictions |     | and extract |
seasonalcharacteristicsfrompastsequences.
| FIGURE8. Structureofinformer. |     |     |     |     |     |     | 4) ITRANSFORMER |     |          |     |        |              |              |     |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --------------- | --- | -------- | --- | ------ | ------------ | ------------ | --- |
|                               |     |     |     |     |     |     | ITransformer    | was | proposed |     | by Liu | et al. [39], | iTransformer |     |
The overall architecture of Informer retains the encoder- fundamentally rethinks how multivariate time series are
decoderstructure.Theencoderismainlymadeupofstacked processed within the Transformer framework. Unlike tra-
ProbSparseSelf-AttentionLayersandSelf-AttentionDistill- ditional approaches that treat time points as tokens and
ingLayers.ThedecoderislargelycomposedofProbSparse variables as features (channel dimensions), iTransformer
Self-Attention and Multi-Head Self-Attention mechanisms. invertsthedimensions:ittreatseachvariableasatokenand
Lastly, the output from the decoder is further processed embeds the temporal points of that variable as the token’s
| 153702 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

X.Aoetal.:ReviewofTimeSeriesPredictionModelsBasedonDeepLearning
features. The overall structure of iTransformer is illustrated prediction.Conformerextractscorrelationfeaturesfrommul-
inFigure10.Keyinnovationsinclude: tivariate time series using Fast Fourier Transform (FFT),
|     |     |     |     |     |     |     |     | effectively | modeling    | relationships |          | between      | multiple    | vari-         |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | ------------- | -------- | ------------ | ----------- | ------------- |
|     |     |     |     |     |     |     |     | ables and   | capturing   | patterns      |          | at different | time        | scales (e.g., |
|     |     |     |     |     |     |     |     | monthly,    | weekly,     | daily,        | hourly). | To           | enhance     | long-period   |
|     |     |     |     |     |     |     |     | prediction  | efficiency, | Conformer     |          | employs      | a sliding   | window        |
|     |     |     |     |     |     |     |     | method,     | where       | each position |          | computes     | attention   | weights       |
|     |     |     |     |     |     |     |     | only with   | neighboring |               | nodes    | within       | the window, | reducing      |
timecomplexitytoO(L).Furthermore,Conformerintroduces
|           |                          |     |     |     |     |     |     | stationary | and         | instant recurrent |             | network    | modules, | encoding      |
| --------- | ------------------------ | --- | --- | --- | --- | --- | --- | ---------- | ----------- | ----------------- | ----------- | ---------- | -------- | ------------- |
|           |                          |     |     |     |     |     |     | input time | series      | with GRU          | to          | compensate | for      | global infor- |
|           |                          |     |     |     |     |     |     | mation     | loss caused | by                | the sliding | window     | method,  | further       |
| FIGURE10. | StructureofiTransformer. |     |     |     |     |     |     |            |             |                   |             |            |          |               |
boostingpredictioncapabilities.
(a) Variable-as-Token: Each multivariate series is trans- In2023,Kimetal.proposedScaleformer[45],itaddresses
| formed | into a | sequence | of tokens, | where | each | token | repre- |             |          |              |     |         |     |              |
| ------ | ------ | -------- | ---------- | ----- | ---- | ----- | ------ | ----------- | -------- | ------------ | --- | ------- | --- | ------------ |
|        |        |          |            |       |      |       |        | multi-scale | temporal | dependencies |     | through |     | a dual adap- |
sentsonevariable.Thetokenembeddingcontainstheentire tive mechanism comprising: (1) scale-aware attention that
historicalsequenceofthatsinglevariable. dynamically selects optimal attention granularity (e.g.,
| (b) Multivariate |     | Self-Attention: |     | The | self-attention |     | mech- |     |     |     |     |     |     |     |
| ---------------- | --- | --------------- | --- | --- | -------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
hourly/daily/weeklybins),and(2)gatedresourceallocation
anism operates directly on these variable tokens, learning that learns to distribute computational resources between
| the complex | dependencies |     | and | interactions |     | between | dif- |     |     |     |     |     |     |     |
| ----------- | ------------ | --- | --- | ------------ | --- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
localandglobalattentionheads.Thisarchitecturerepresents
ferent variables. This is a stark contrast to models using a significant advancement in computational efficiency for
channel-independentembeddingsorsimpleconcatenation. ultra-long-horizon forecasting, though its predefined scale
| (c) Temporal |     | Modeling |     | via Feed-Forward |     | Networks |     |     |     |     |     |     |     |     |
| ------------ | --- | -------- | --- | ---------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
binsmayconstrainadaptabilitytoirregulartemporalpatterns.
(FFNs): The powerful FFN layers within each Transformer In2023,Zhangetal.developedCrossFormer[46].Cross-
blockarethenresponsibleformodelingtheintricatetempo- Former introduces a novel cross-scale attention mechanism
ral patterns within each individual variable’s sequence. The that explicitly models multi-periodicity through: (1) hier-
inverted structure allows the FFNs to focus solely on the archical feature extraction at predefined temporal scales
temporaldimensionpervariable.
(e.g.,24h/168h/720h),(2)learnablefusionofperiodiccompo-
iTransformer leverages the Transformer’s token rela- nentsviagatingmechanisms,and(3)phase-awarealignment
tionships and FFN’s non-linear fitting to effectively cap- for drifting seasonality. This architecture provides state-of-
ture cross-variable correlations while maintaining temporal the-art modeling of complex periodic patterns, though its
modeling. It significantly outperforms models like Auto- fixedscaledefinitionsmaylimiteffectivenessforirregularly
| former/FEDformer |     | [40] | in multivariate |     | forecasting |     | due to |     |     |     |     |     |     |     |
| ---------------- | --- | ---- | --------------- | --- | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
sampledornon-stationarytimeseries.
| its simplicity. |     | Gains | are less | pronounced |     | on univariate |     |     |     |     |     |     |     |     |
| --------------- | --- | ----- | -------- | ---------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
tasks,anditrepresentsaparadigmshiftprioritizingvariable
| dimensions. |     |     |     |     |     |     |     | 6) COMPARATIVEANALYSISOFTRANSFORMER-BASED |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- |
ALGORITHMS
5) OTHERTRANSFORMER-BASEDMETHODS
|     |     |     |     |     |     |     |     | Transformer-based |     | algorithms |     | are now | widely | used in var- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ---------- | --- | ------- | ------ | ------------ |
WiththesuccessofTransformermodelsinnaturallanguage ious artificial intelligence tasks. Building models on the
processing, an increasing number of studies have applied Transformer framework can break through the limitations
them to time series prediction tasks [41]. Below are several of traditional algorithms, enabling simultaneous capture of
improvedTransformer-basedmodelsandtheirapplicationsin short-term and long-term dependencies, effectively solving
timeseriesprediction. long-sequence prediction challenges, and supporting paral-
In 2020, Wu et al. [42] proposed the Adversarial Sparse lel processing. A comparison analysis of transformer-based
Transformer(AST).BasedonSparseTransformer[43],AST algorithmsissummarizedinTable3.
incorporates ideas from Generative Adversarial Networks Transformer-basedalgorithmshavedemonstratedremark-
(GANs) to enhance prediction performance through adver- ablecapabilitiesinlong-rangedependencymodeling,though
sarialtraining.ASTadoptsanencoder-decoderarchitecture, they present distinct trade-offs. The Informer architecture
enablinghigh-fidelitymulti-steppredictionsatthesequence achievesefficientlong-sequenceprocessingthroughitsProb-
level. Experiments show that dependencies between time Sparse attention mechanism, while Autoformer enhances
series steps exhibit sparsity, and AST improves prediction periodicity modeling via series decomposition and auto-
performancegloballythroughadversarialtraining.Compared correlation mechanisms. Newer variants address specific
to traditional autoregressive decoders, the encoder-decoder- limitations: iTransformer’s inverted architecture (channel-
basedASTdemonstratessuperioraccuracyandstability. independent processing) significantly improves multivari-
In 2023, Li et al. [44] proposed Conformer, a Trans- ate forecasting robustness but sacrifices short-term feature
formermodeltailoredformultivariatelong-periodtimeseries sensitivity; Scaleformer’s adaptive computation allocation
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 153703 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

X.Aoetal.:ReviewofTimeSeriesPredictionModelsBasedonDeepLearning
TABLE3. Analysisoftransformer-basedalgorithms. maintainsadvantagesingeneralsequence-to-sequencetasks
withmoderatelengths.
InterpretabilityremainschallengingacrossallTransformer
variants. While attention visualization offers partial insight,
modelsincreasinglyrelyonpost-hocmethodslikeSHAP[47]
andLIME[48]forfeatureattribution.
SHAP: A game-theoretic approach that assigns each fea-
ture (variable at a specific time) an importance value for a
particularprediction.Itishighlyvaluableforquantifyingthe
contributionofdifferentdriversinmultivariateforecasts(e.g.,
‘‘What was the impact of temperature vs. humidity on the
predictedenergyload?’’).
LIME:Approximatesthecomplexmodellocallyarounda
specificpredictionwithasimpler,interpretablemodel(e.g.,
linear regression). This helps in understanding the model’s
behaviorforindividualforecasts(e.g.,‘‘Whydidthemodel
predictaspikeintrafficatthisparticularhour?’’).
E. METHODSBASEDONGRAPHNEURALNETWORKS
Inmultivariatetimeseriesforecasting,variablesoftenexhibit
complex interdependencies that traditional methods may
struggletocaptureeffectively.Inrecentyears,GraphNeural
Networks(GNNs)[49]havedemonstratedpowerfulcapabil-
itiesinmodelingrelationaldependencies.GNNsaddressthis
by representing time series data as graph structures, where
graph convolution operations capture spatial dependencies
between variables, and temporal convolution operations
modeltemporaldependencieswithinthesequences.Thisdual
mechanismenableseffectivepredictionofmultivariatetime
series [50]. Recent advances further extend this paradigm
throughspatiotemporalframeworks(e.g.,MTGNN,STGCN)
that unify spatial and temporal modeling in an end-to-end
architecture. The basic framework of GNNs is illustrated in
Figure11.
FIGURE11. StructureofGNN.
optimizesultra-long-horizonefficiencyatthecostofprede- 1) MAINCATEGORIESOFGRAPHNEURAL
finedscaleconstraints;CrossFormerprovidesstate-of-the-art NETWORK-BASEDMETHODS
multi-periodicitymodelingthroughexplicitcross-scaleatten- (a)SpatialGraphConvolution-BasedMethods
tion, though its fixed temporal bins limit irregular pattern Thisapproachutilizesgraphconvolutionoperationstocap-
adaptability. turespatialdependenciesintimeseriesdata.Bytransforming
For applications requiring extreme sequence lengths time series data into graph structures, graph convolution
(>10,000 steps), Scaleformer currently provides the opti- propagatesinformationacrossthegraph,integratingfeatures
mal efficiency-accuracy balance. When handling high- from neighboring nodes. The advantage of spatial graph
dimensional multivariate series with independent channels convolution is its ability to effectively capture local spatial
(e.g.,multi-sensorindustrialsystems),iTransformerdemon- dependencies, making it well-suited to data with explicit
strates superior noise robustness. CrossFormer excels in spatial structures. However, it also has limitations, such as
domains with strong inherent periodicities (epidemiology, lowercomputationalefficiencyforlarge-scalegraphdataand
energydemand),whiletheoriginalTransformerarchitecture challengesinhandlingdynamicgraphstructures.
153704 VOLUME13,2025

X.Aoetal.:ReviewofTimeSeriesPredictionModelsBasedonDeepLearning
(b)TemporalConvolution-BasedMethods to link water demand time series across different regions,
Temporalconvolutionmethodsprimarilyfocusonextract- capturing both spatial and temporal dependencies. Specifi-
ing temporal dependencies through temporal convolution cally, GCRNN integrates spatial information through graph
modules.Thesemethodsexcelatprocessingsequentialinfor- convolution operations and captures temporal dynamics via
mationintimeseriesdataandperformwellinpredictingdata recurrent neural networks. Experiments demonstrate that
withsignificanttemporaldynamics.However,theymayover- GCRNN effectively predicts water demand, providing reli-
lookspatialdependenciesinthedata,leadingtosuboptimal ablesupportforwaterresourcemanagement.
performancewhendealingwithcomplexspatialstructures. Yu et al. proposed a deep learning framework based on
(c)Spatial-TemporalIntegratedMethods Spatio-Temporal Graph Convolutional Network (STGCN)
Thisapproachconstructsaspatiotemporalparallelfeature for traffic flow forecasting. Addressing the issue that tradi-
extractionframeworkthatsimultaneouslyconsidersbothspa- tional methods struggle to capture complex spatio-temporal
tialandtemporaldependenciesintimeseriesdata.Forexam- dependenciesinmid-to-long-termpredictions,STGCNcon-
ple, emerging frameworks like STGCN (Spatio-Temporal structs a fully convolutional structure of spatio-temporal
Graph Convolutional Network) and MTGNN (Multivariate convolution blocks by combining graph convolution with
TimeSeriesGraphNeuralNetwork)jointlymodelspatialand gatedtemporalconvolution,effectivelyintegratingthetopo-
temporaldependenciesthrough: logical information of the traffic network and dynamic
STGCN(Spatio-TemporalGraphConvolutionalNetwork) temporal features. The research results verify the efficiency
is a graph neural network framework specifically designed andscalabilityofspatio-temporalgraphconvolutionintraf-
for spatiotemporal data with fixed topology. Its core inno- fic prediction, providing a practical solution for intelligent
vation lies in the cascaded architecture of spatial-temporal transportationsystems.
convolutions.Themethodadoptsasandwichstructure(GCN- Wu et al. proposed an end-to-end framework named
TCN-GCN), where graph convolutional networks (GCN) in MTGNN for modeling dynamic spatio-temporal dependen-
the spatial dimension capture spatial dependencies between cies. The innovation of this method lies in its ability to
nodes(e.g.,connectionsbetweensensorsintrafficnetworks), automaticallylearnthedynamicgraphstructureamongvari-
while dilated causal convolutions (TCN) in the temporal ables through trainable node embeddings, without the need
dimensionextractmulti-scaletemporalfeatures[51]. forapredefinedadjacencymatrix.Italsocapturesmulti-scale
MTGNN (Multivariate Time Series Graph Neural Net- temporal patterns by combining dilated causal convolution
work)isagraphneuralnetworkframeworkthatisspecifically withgatingmechanisms.Experimentsshowthatitstraining
tailoredformultivariatetimeseriesforecasting.Itscoreinno- efficiencyandgeneralizationabilityaresuperiortotraditional
vation lies in end-to-end dynamic graph structure learning graphneuralnetworks,providingageneralsolutionformul-
andjointspatiotemporaldependencymodeling.Themethod tivariatetimeseriespredictionwithoutexplicitstructure.
automaticallyinfersimplicitrelationshipsbetweenvariables Lanetal.proposedadynamicspatial-temporal(DSTAGNN)
through trainable node embeddings, generating dynamic aware graph based on a data-driven strategy to replace the
adjacency matrices that overcome the limitations of tra- predefined static graph commonly used in traditional graph
ditional GNNs relying on prior knowledge. For temporal convolution. They considered that historical data contains
modeling, MTGNN employs dilated causal convolution to the intrinsic dynamic information of the road network’s
capturemulti-scaletemporalpatterns,combinedwithgating spatial structure. Additionally, the paper designed a new
mechanismstofilternoise[52] graph neural network architecture. This architecture can
Compared to approaches that model spatial and tempo- not only represent the dynamic spatial correlation between
ral dependencies separately, these integrated methods often nodeswithanimprovedmulti-headattentionmechanismbut
demonstratesuperiorperformanceonbenchmarks. also capture extensive dynamic temporal correlation from
multi-receptive-fieldfeaturesthroughmulti-scalegatedcon-
volution.Extensiveexperimentsonreal-worlddatasetsshow
2) TIMESERIESPREDICTIONRESEARCHBASEDONGRAPH that the performance of the proposed algorithm has been
NEURALNETWORKS improved[55].
In recent years, the application of Graph Neural Networks HGCN-MA(HierarchicalGraphConvolutionwithMulti-
(GNNs)intimeseriespredictionhasgrownsignificantly,par- scaleAttention)proposedbyWangetal.[56],thisarchitec-
ticularlyinmultivariatetimeseriesforecasting[53].Bymod- turecapturesmulti-granularityspatio-temporaldependencies
eling spatial dependencies between variables, GNNs have throughthreekeyinnovations:(1)hierarchicalgraphpooling
substantially improved prediction performance. An increas- and up-sampling operations that aggregate regional pat-
ingnumberofscholarsarenowapplyingGNNstotimeseries ternsatdifferentspatialresolutions,(2)multi-scaleattention
predictionresearch. mechanismsthatdynamicallyfusehourly,daily,andweekly
Ariele and Brunod et al. [54] proposed a Graph Con- temporalfeatures,and(3)adaptiveedgeweightingthatmod-
volutional Recurrent Neural Network (GCRNN) to predict els evolving relationships between nodes. This hierarchical
water demand in supply systems within the same geo- approach effectively captures regional-to-local dependen-
graphical region. This method constructs a graph structure cies in urban systems, though its fixed pooling ratios
VOLUME13,2025 153705

X.Aoetal.:ReviewofTimeSeriesPredictionModelsBasedonDeepLearning
TABLE4. AnalysisofGNN-basedalgorithms. approaches(e.g.,MTGNN)bridgethisgapbutincreasecom-
plexity.
|     |     |     |     | Spatial GCNs: |     | Ideal for | traffic/weather |     | prediction |     | with |
| --- | --- | --- | --- | ------------- | --- | --------- | --------------- | --- | ---------- | --- | ---- |
fixedsensors.
TemporalCNNs:Bestforunivariateorspatiallyindepen-
dentseries.
|     |     |     |     | Integrated | Methods: | Essential |     | for dynamic | systems |     | (e.g., |
| --- | --- | --- | --- | ---------- | -------- | --------- | --- | ----------- | ------- | --- | ------ |
finance,IoT).
|     |     |     |     | Recent spatio-temporal |     |          | GNN | innovations     |     | focus    | on  |
| --- | --- | --- | --- | ---------------------- | --- | -------- | --- | --------------- | --- | -------- | --- |
|     |     |     |     | dynamic relationship   |     | modeling |     | and multi-scale |     | aggrega- |     |
tion.HGCN-MA’shierarchicalapproacheffectivelycaptures
regional-to-localdependencies.Forhigh-stakesapplications
likedisasterforecasting,STAN’sdual-pathisolationofspa-
tialandtemporalfeaturesprovidescriticalmodelingfidelity.
F. HYBRIDMODELS:INTEGRATINGDEEPLEARNING
WITHSTATISTICALMETHODS
|     |     |     |     | Recent studies   | have        | demonstrated     |     | that          | combining |            | deep |
| --- | --- | --- | --- | ---------------- | ----------- | ---------------- | --- | ------------- | --------- | ---------- | ---- |
|     |     |     |     | learning models  |             | with traditional |     | statistical   |           | methods    | or   |
|     |     |     |     | domain-specific  | constraints |                  | can | significantly |           | enhance    | pre- |
|     |     |     |     | diction accuracy | and         | robustness       |     | [58].         | Hybrid    | approaches |      |
leveragethestrengthsofbothparadigms—statisticalmodels
forcapturinglinearpatternsanddeeplearningformodeling
nonlineardynamics—providingamorecomprehensivesolu-
tiontocomplextimeseriesforecastingtasks.
1) STATISTICAL-DEEPLEARNINGINTEGRATION
Thiscategoryintegratesclassicalstatisticalforecastingmod-
|     |     |     |     | els (e.g., ARIMA, |     | ETS) | with | deep | neural | networks | to  |
| --- | --- | --- | --- | ----------------- | --- | ---- | ---- | ---- | ------ | -------- | --- |
leveragetheircomplementarystrengths.
|     |     |     |     | ARIMA-RNN | Hybrid | [59] | combines |     | ARIMA | for | linear |
| --- | --- | --- | --- | --------- | ------ | ---- | -------- | --- | ----- | --- | ------ |
require careful hyperparameter tuning for optimal spatial componentmodelingwithRNNsfornonlinearresidualpro-
partitioning. cessing.TheARIMAmodulefirstcaptureslineartrendsand
| STAN | (Spatio-Temporal | Attention Network) | developed |              |       |               |            |     |             |     |     |
| ---- | ---------------- | ------------------ | --------- | ------------ | ----- | ------------- | ---------- | --- | ----------- | --- | --- |
|      |                  |                    |           | seasonality, | while | the residuals | (nonlinear |     | components) |     | are |
by Chen et al. [57], STAN introduces a dual-path isola- fed into an RNN for refinement. On the Electricity Load
tion framework featuring: (1) a spatial path using graph Dataset,thishybridachieved15%MAEreductioncompared
isomorphism networks with edge gating to filter irrele- to standalone models. This approach exemplifies effective
vant connections, (2) a temporal path employing dilated error-correctionsynergybetweenstatisticalanddeeplearning
| causalconvolutionswithadaptivereceptivefieldsthatauto- |     |     |     | paradigms. |     |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
matically adjust to changing event durations, and (3) a ETSformer [60] integrates exponential smoothing state
cross-attentionfusionmodulethatlearnsinteractionweights space models (ETS) into Transformers through two inno-
between spatio-temporal features. The dual-path isolation vations:i)ExponentialSmoothingAttentionreplacingstan-
provides exceptional modeling fidelity for critical phenom- dard self-attention for efficient recurrence, and ii) built-in
ena like natural disasters, though its multi-stage training seasonal-trend decomposition layers. It reduces inference
protocoldemandssignificantcomputationalresources. latency by 37% vs. Autoformer on ETT data while main-
|     |     |     |     | taining accuracy. |     | This framework |     | sets | new | standards | for |
| --- | --- | --- | --- | ----------------- | --- | -------------- | --- | ---- | --- | --------- | --- |
3) COMPARATIVEANALYSISOFGNN-BASEDALGORITHMS interpretableandefficientstatistical-neuralfusion.
| Graph Neural | Networks | (GNNs) have emerged | as powerful |     |     |     |     |     |     |     |     |
| ------------ | -------- | ------------------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
toolsformodelingrelationaldependenciesintimeseriesdata. 2) DECOMPOSITION-BASEDHYBRIDMODELS
By combining spatial and temporal modeling capabilities, These models explicitly decompose time series into inter-
GNN-based methods offer unique advantages for various pretable components (trend, seasonality, residuals) using
prediction tasks. A comparative analysis of three key GNN statisticalorlearnablemethods,withdeepnetworksmodeling
| approachesissummarizedinTable4. |     |     |     | residualsorsub-components. |     |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- |
Spatial methods excel in structured environments, while BEATS [61] employs iterative decomposition blocks
temporal methods prioritize sequence modeling. Integrated where each block: i) extracts features via FCN, ii) projects
| 153706 |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

X.Aoetal.:ReviewofTimeSeriesPredictionModelsBasedonDeepLearning
interpretable trend (polynomial) and seasonal (harmonic) TABLE5. Analysisofhybridmodels.
components,and3)passesresidualsdownstream.Theinter-
| pretable | variant | (N-BEATS-I) |     | won the | M4  | competition. | Its |     |     |     |     |     |     |     |
| -------- | ------- | ----------- | --- | ------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
hierarchicaldecompositionprovidesunprecedentedaccuracy
andexplainabilityforheterogeneoustimeseries.
| PatchTST | [62] | introduces | patching |     | - splitting | series | into |     |     |     |     |     |     |     |
| -------- | ---- | ---------- | -------- | --- | ----------- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- |
overlappingsub-seriesasTransformertokens-enablingeffi-
cientlong-horizonmodeling.Whencombinedwithstatistical
| methods    | (e.g.,       | ARIMA         | for patch-level |           | trends),      | it         | achieves |     |     |     |     |     |     |     |
| ---------- | ------------ | ------------- | --------------- | --------- | ------------- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| 23% lower  | MSE          | than Informer |                 | with      | 60%           | less GPU   | mem-     |     |     |     |     |     |     |     |
| ory. Its   | segment-wise |               | processing      | redefines |               | efficiency | for      |     |     |     |     |     |     |     |
| ultra-long | sequences    | while         | maintaining     |           | compatibility |            | with     |     |     |     |     |     |     |     |
statisticaltechniques.
3)DOMAIN-CONSTRAINEDHYBRIDMODELS
| Incorporates |           | physical | laws,     | operational |     | constraints, |           |     |     |     |     |     |     |     |
| ------------ | --------- | -------- | --------- | ----------- | --- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- |
| or domain    | knowledge | as       | inductive | biases      | or  | loss         | functions |     |     |     |     |     |     |     |
withindeeparchitectures.
| Physics-Informed |               | Hybrids    | [63]       | integrate    |                      | domain        | knowl- |     |     |     |     |     |     |     |
| ---------------- | ------------- | ---------- | ---------- | ------------ | -------------------- | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| edge via         | dynamically   | weighted   |            | ensembles    | of                   | physics-based |        |     |     |     |     |     |     |     |
| simulators       | (‘‘experts’’) |            | and deep   | learners.    |                      | For power     | load   |     |     |     |     |     |     |     |
| forecasting,     | they          | explicitly | model      | interactions |                      | between       | sea-   |     |     |     |     |     |     |     |
| sonal trends     | and           | external   | factors    | like         | temperature/economic |               |        |     |     |     |     |     |     |     |
| indicators.      | This          | approach   | guarantees |              | physical             | plausibility  |        |     |     |     |     |     |     |     |
whilecapturingcomplexnonlineardynamics.
| GNN-Statistical |             | Hybrids | combines |        | Graph | Neural     | Net-  |                                   |     |        |         |          |     |              |
| --------------- | ----------- | ------- | -------- | ------ | ----- | ---------- | ----- | --------------------------------- | --- | ------ | ------- | -------- | --- | ------------ |
|                 |             |         |          |        |       |            |       | b: DOMAINCOMPLIANCEVS.FLEXIBILITY |     |        |         |          |     |              |
| works with      | statistical | models  |          | (e.g., | VAR,  | structural | equa- |                                   |     |        |         |          |     |              |
|                 |             |         |          |        |       |            |       | Domain-constrained                |     | models | enforce | physical |     | plausibility |
tions),thesehybridsenforceexplicitrelationalconstraintsin
|     |     |     |     |     |     |     |     | (e.g., energy | conservation |     | in  | Physics-Informed |     | Hybrids) |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------------ | --- | --- | ---------------- | --- | -------- |
multivariateforecasting.Examplesincludesupply-chainnet-
|     |     |     |     |     |     |     |     | or relational | causality | (GNN-VAR), |     | but | require | significant |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | ---------- | --- | --- | ------- | ----------- |
workswhereGNNscapturespatialdependencieswhileVAR
|     |     |     |     |     |     |     |     | expert knowledge |     | for | constraint | design | and | risk over- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | ---------- | ------ | --- | ---------- |
modelstemporalcausality.Theyprovideauditablerelational
regularization.
reasoningcriticalforhigh-stakesdomainslikeeconomicsand
epidemiology.
|     |     |     |     |     |     |     |     | c: EFFICIENCYCHALLENGES |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |
WhilePatchTSTreducesGPUmemoryby60%viasub-series
3) COMPARATIVEANALYSISOFHYBRIDMODELS
|     |     |     |     |     |     |     |     | tokenization | and | ETSformer | cuts | inference | latency | by 37% |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------- | ---- | --------- | ------- | ------ |
Hybridmodels,whichsynergisticallyintegratedeeplearning via recurrence, most hybrids (e.g., N-BEATS with 30+
withstatisticalmethodsordomainknowledge,haveemerged
|     |     |     |     |     |     |     |     | blocks) remain |     | computationally |     | intensive | versus | end-to-end |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------------- | --- | --------- | ------ | ---------- |
asapowerfulparadigmfortimeseriesprediction.Acompar-
deepmodels.
ativeanalysisofthehybridmodelsissummarizedinTable5. FutureDirections:
| Hybrid | models | significantly |     | enhance | prediction |     | accuracy |     |     |     |     |     |     |     |
| ------ | ------ | ------------- | --- | ------- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
AutomatedFusion:End-to-endjointtraining(e.g.,differ-
androbustnessbysynergisticallyintegratingstatisticalmeth- entiableARIMAlayers)toreplacestagedpipelines.
| ods (e.g., | linear | patterns, | interpretable |     | decomposition) |     | with |             |     |                |     |            |               |      |
| ---------- | ------ | --------- | ------------- | --- | -------------- | --- | ---- | ----------- | --- | -------------- | --- | ---------- | ------------- | ---- |
|            |        |           |               |     |                |     |      | Lightweight |     | Decomposition: |     | Integrated | architectures | like |
deeplearning(nonlineardynamics,automaticfeaturelearn-
PatchTST’stokenizationthatavoiditerativeresiduals.
ing). However, they involve critical trade-offs across three Universal Constraints: Template libraries for domain
dimensions:
knowledge(e.g.,physicslossfunctions)toreducecustomiza-
tionoverhead.
a: ACCURACY-RICHNESSVS.COMPLEXITY
Decomposition-basedhybrids(e.g.,N-BEATS,Autoformer, IV. SYSTEMATICEVALUATIONANDTASK-DRIVEN
PatchTST) excel in capturing multi-scale components but MODELSELECTION
incur computational redundancy from iterative decomposi- A. COMPARATIVEANALYSISOFMODELCATEGORIES
tion(N-BEATS)orpatchingoperations(PatchTST). Time series forecasting plays a critical role in numer-
Stat-DL integrations (e.g., ETSformer, ARIMA-RNN) ous fields, with different types of neural network models
improve interpretability through explicit statistical founda- exhibiting distinct characteristics. This section analyzes the
tions(e.g.,exponentialsmoothinginETSformer),yetdepend strengthsand limitationsofthefive majormodelcategories
heavily on underlying assumptions (stationarity, known discussed (CNN-based, RNN-based, Transformer-based,
seasonality). GNN-based,HybridModels)andprovidesacomprehensive
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 153707 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

X.Aoetal.:ReviewofTimeSeriesPredictionModelsBasedonDeepLearning
TABLE6. Comparativeanalysisofmodelcategories. Based on table 8, to address the gap in practical model
|     |     |     |     | selection, | we propose | a       | task-driven     |     | framework | (Figure | 12)   |
| --- | --- | --- | --- | ---------- | ---------- | ------- | --------------- | --- | --------- | ------- | ----- |
|     |     |     |     | that maps  | key        | problem | characteristics |     | to        | optimal | model |
classes:
(<1000
|     |     |     |     | a) For | short-to-medium |     | sequences |     |     | steps) | with |
| --- | --- | --- | --- | ------ | --------------- | --- | --------- | --- | --- | ------ | ---- |
prominentlocalpatterns:
PrioritizeCNN/TCNmodels(e.g.,ECGanomalydetection).
Iftemporalorderiscritical,uselightweightRNNvariants
(GRU).
b) Forlongsequences(>1000steps):
|     |     |     |     | Adopt Transformer |     | architectures |     | (e.g., | Informer | for | effi- |
| --- | --- | --- | --- | ----------------- | --- | ------------- | --- | ------ | -------- | --- | ----- |
ciency,Autoformerforseasonaldata).
Ifcomputationalresourcesarelimited,considerTCNasan
alternative.
c) Formultivariateserieswithinterdependencies:
|     |     |     |     | Select GNN-based |     | models | (e.g., | MTGNN |     | for dynamic |     |
| --- | --- | --- | --- | ---------------- | --- | ------ | ------ | ----- | --- | ----------- | --- |
graphs,STGCNforfixedtopologies).
|     |     |     |     | For variable-specific |     |     | temporal | patterns, |     | iTransformer | is  |
| --- | --- | --- | --- | --------------------- | --- | --- | -------- | --------- | --- | ------------ | --- |
preferred.
d) Understrictlatency/memoryconstraints:
ChooseGRUorKmeans-CNNforsmall-scaledata.
PatchTST+ARIMA)
|     |     |     |     | Employ | hybrid | models | (e.g., |     |     |     | for |
| --- | --- | --- | --- | ------ | ------ | ------ | ------ | --- | --- | --- | --- |
resource-efficientlong-horizonforecasting.
|     |     |     |     | Example:               | In  | traffic | flow prediction |     | (long | sequences   | +   |
| --- | --- | --- | --- | ---------------------- | --- | ------- | --------------- | --- | ----- | ----------- | --- |
|     |     |     |     | spatial dependencies), |     |         | STGCN           | or  | MTGNN | outperforms |     |
puretemporalmodels.Conversely,forhigh-frequencystock
+
|     |     |     |     | volatility | (short | sequences |     | low latency |     | needs), | TCN is |
| --- | --- | --- | --- | ---------- | ------ | --------- | --- | ----------- | --- | ------- | ------ |
optimal.Thisframeworkbridgestheoreticalcapabilitieswith
pragmaticdeploymentconsiderations.
|     |     |     |     | Selecting | a forecasting |     | model | also | requires | navigating |     |
| --- | --- | --- | --- | --------- | ------------- | --- | ----- | ---- | -------- | ---------- | --- |
core,oftencompeting,priorities:
|     |     |     |     | Modeling           | Power | vs.      | Efficiency: |                | High | capacity | for  |
| --- | --- | --- | --- | ------------------ | ----- | -------- | ----------- | -------------- | ---- | -------- | ---- |
|     |     |     |     | complex/long-range |       | patterns |             | (Transformers, |      | GNNs,    | deep |
comparison of their key attributes, summarized in Tables 6 TCN/LSTM) demands significant computation. Simpler
| and7. |     |     |     | models(basicCNN,linear)areefficientbutlimited. |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Generally speaking, CNN-based models are suitable for SequentialFidelityvs.ParallelSpeed:RNNs(LSTM/GRU)
short-termtimeseriespredictiontasks(e.g.,short-termstock naturally handle order/causality but train slowly (sequen-
price fluctuations, sensor data prediction), particularly in tial).CNNs/Transformersleverageparallelismforspeedbut
scenarios with prominent local features. RNN-based mod- require explicit mechanisms (causal convolutions, masking)
| els excel | in long-sequence | prediction tasks | (e.g., power | forcausality. |     |     |     |     |     |     |     |
| --------- | ---------------- | ---------------- | ------------ | ------------- | --- | --- | --- | --- | --- | --- | --- |
load forecasting, speech recognition), effectively capturing Automatic Learning vs. Interpretability: Deep models
long-termdependencies.Transformer-basedmodelsareideal excel at feature learning but are ‘‘black boxes.’’ Simpler
for long-sequence and global dependency modeling tasks statisticalmodelsorhybridsoffermoretransparencybutneed
(e.g., machine translation, text generation), leveraging their manualfeatureengineeringorlackflexibility.
powerful parallel computing capabilities. GNN-based mod- Generalization vs. Specialization: General models
els are well-suited for multivariate time series prediction (LSTM/GRU,vanillaTransformer)needmoredata.Special-
tasks (e.g., traffic flow forecasting, social network analy- izedmodels(Autoformerforseasonality,SCINetfortrends,
sis),especiallyinscenarioswherevariablesexhibitcomplex GNNs for relational data) can be data-efficient if their bias
interdependencies. Hybrid models are suitable for complex matchesthedata,butfailifassumptionsbreak.
temporal tasks that require simultaneous capture of local There is no universally optimal model. Selection should
featuresandlong-termdependencies(e.g.,combiningCNNs beguided bymatching themodel’s strengthsto thespecific
with ARIMA to handle short-term fluctuations under high- problem requirements and constraints. Prioritizing the most
frequency noise) or integration of domain knowledge with critical trade-offs for a given task is essential. Table 8 and
data-driven modeling (e.g., GNNs incorporating VAR for the preceding category-specific analyses serve as valuable
multivariatespatialcorrelationanalysis). frameworkstoinformthisdecision-makingprocess.
| 153708 |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

X.Aoetal.:ReviewofTimeSeriesPredictionModelsBasedonDeepLearning
TABLE7. Multi-dimensionalcomparisonofdeeplearningmodelsfortimeseriesforecasting.
FIGURE12. Task-drivenmodelselectionframework.
architecturalparadigmsorspecificvariantsexcelunderpar-
B. CROSS-MODELANDCROSS-DATASETTREND
ANALYSIS(META-ANALYSIS) ticulardatacharacteristicsandtaskrequirements.
While Sections III and IV-A-C provide detailed analyses (1)Long-TermDependenciesinMultivariateSettings
of individual models and categories, this section synthe- Transformer Variants Dominate: Models based on the
sizes broader trends observed across diverse time series Transformer architecture, particularly those incorporating
|          |                       |              |                 | efficient attention | mechanisms | (e.g.,Informer’s | ProbSparse |
| -------- | --------------------- | ------------ | --------------- | ------------------- | ---------- | ---------------- | ---------- |
| datasets | and prediction tasks, | drawing upon | empirical find- |                     |            |                  |            |
ings from numerous benchmark studies [3], [4], [8], [10]. attention, Autoformer’s series decomposition and auto-
Thismeta-analysisaimstoidentifypatternsregardingwhich correlation), consistently demonstrate superior performance
| VOLUME13,2025 |     |     |     |     |     |     | 153709 |
| ------------- | --- | --- | --- | --- | --- | --- | ------ |

X.Aoetal.:ReviewofTimeSeriesPredictionModelsBasedonDeepLearning
in capturing very long-range dependencies (\>1000 steps) (3) Addressing Computational Cost & Real-Time
withinmultivariatedatasets(e.g.,ETT,Electricity)[36],[37]. Constraints:
Their ability to model global dependencies directly gives RNNs/GRUs Remain Relevant: For medium-length
themanedgeoversequentialmodelslikeRNNs/LSTMsfor sequences (\∼100-1000 steps) and scenarios demanding
ultra-longhorizons. low-latencyinference,GRUs(andtoalesserextent,LSTMs)
GNNs for Structured Multivariate Dependencies: When remain competitive due to their lower computational over-
strong spatial or relational dependencies exist between headperstepcomparedtoTransformers[25],[30].TCNalso
variables (e.g., traffic sensor networks, supply chains), offers a strong parallelizable alternative for these sequence
GNN-based models (STGCN, MTGNN) significantly out- lengths[14].
perform models treating channels independently [51], [52]. Lightweight Transformers & Hybrids: Efficient Trans-
MTGNN’sabilitytolearndynamicgraphstructuresendows former variants (Informer, PatchTST) and hybrid models
itwithparticularrobustnessinscenarioswhererelationships combining simple statistical methods with deep learning
evolve. (e.g.,ARIMA-RNN,PatchTST+statisticalsmoothing)pro-
iTransformer’s Emergence: Recent work on iTrans- videviablepathwaysfordeploymentinresource-constrained
former[39]showsremarkablepromise,oftenachievingstate- or real-time environments [59], [62]. PatchTST’s patching
of-the-artresultsonmultivariatebenchmarkswithoutrelying mechanismsignificantlyreducesmemoryfootprint.
on predefined graphs. Its inverted architecture (variables as (4)TheRoleofHybridModels:
tokens, time points as features) proves highly effective for Accuracy & Robustness:Decomposition-based hybrids
capturing inter-variable dependencies while leveraging the (N-BEATS, Autoformer) frequently top benchmark leader-
Transformer’s FFN for temporal modeling, demonstrating boardsduetotheirabilitytoseparateandmodeldifferenttem-
stronggeneralizationacrossdiversemultivariatedomains. poral components [37], [61]. Domain-constrained hybrids
(2)TransformerVariantGeneralizationAcrossDomains demonstrate superior robustness and data efficiency when
Informer for Efficiency:Informer establishes itself as a domainknowledgeisaccuratelyincorporated[63].
robust and efficient baseline for long-sequence forecast- Interpretability: Hybrids, especially N-BEATS-I (inter-
ing across various domains (energy, traffic, finance) due to pretable version) and models integrating statistical com-
its ProbSparse attention and distilling mechanism [36]. Its ponents (ETSformer [60]), offer significantly enhanced
computational advantages make it a practical choice when interpretabilitycomparedtopuredeeplearningblackboxes.
resourcesareconstrained. (5) Emerging Trend Recent models like iTransformer
Autoformer for Strong Seasonality/Trends: Autoformer (unifying multivariate dependency and temporal modeling
exhibits exceptional generalization capabilities in domains within a standard Transformer block) and PatchTST (sim-
characterized by prominent seasonal and trend compo- plifyinglong-horizonforecastingviasub-seriestokenization)
nents(e.g.,energyload,weather,retailsales)[37].Itsbuilt-in suggest a move towards simpler, more unified architectures
seriesdecompositionandauto-correlationmechanismarekey that maintain high performance while reducing complex,
tothisstrength. custom-designed components. This contrasts with earlier
Decomposition is Key: A recurring theme among the trendsofincreasingmodelspecialization(e.g.,Autoformer’s
mostgeneralizableTransformervariants(Autoformer,FED- specificdecompositionblocks).
former [40], PatchTST [58]) is the explicit or implicit
incorporation of time series decomposition. This architec- V. CONCLUSION
tural bias aligns well with the inherent structure of many Driven by rapid advancements in information technology,
real-worldtimeseries,enhancingrobustnessacrossdifferent time series data has proliferated across numerous fields,
domains. and deep learning-based time series prediction models have
iTransformer’sStrongMultivariateGeneralization:iTrans- become a focal point of research and application in both
former demonstrates impressive generalization specifically academiaandindustry.Thispapercomprehensivelyreviews
in the multivariate forecasting setting, often outperforming theapplicationofvariousmainstreamdeeplearningmodels
otherTransformervariants(likeAutoformerandFEDformer) in time series prediction, including key technologies such
onstandardbenchmarks,highlightingtheeffectivenessofits asRecurrentNeuralNetworks(RNN),ConvolutionalNeural
variable-centrictokenizationapproachfordiversemultivari- Networks (CNN), Transformer models, Graph Neural Net-
atedata. works(GNN),andhybridmodels,whileelaboratingontheir
Trade-off: Specialization vs. Generality: While models fundamental principles, structural characteristics, strengths,
likeScaleformer[45]offerextremeefficiencyforultra-long andreal-worldusecasesindifferentdomains.
horizons, and CrossFormer [46] excels at modeling com- Throughanin-depthexplorationofthesemodels,itisevi-
plex multi-periodicity, their performance gains can be more dentthatdifferentdeeplearningarchitecturespossessunique
sensitivetospecificdatacharacteristics(e.g.,definedseason- advantagestailoredtospecifictypesoftimeseriesprediction
alities)comparedtothemorebroadlyapplicableInformeror tasks. RNNs demonstrate strengths in handling data with
Autoformer. PatchTST offers a good balance of efficiency long-termdependencies;CNNsexcelatextractinglocalfea-
andgeneralitythroughitspatchingstrategy. turesfromtimeseries;Transformersleveragetheirpowerful
153710 VOLUME13,2025

X.Aoetal.:ReviewofTimeSeriesPredictionModelsBasedonDeepLearning
parallel computing capabilities and global attention mecha- [4] J.A.Milleretal.,‘‘Deeplearningandfoundationmodelsfortimeseries
nisms to capture complex dependencies in long sequences; forecasting:Acomprehensivesurvey,’’IEEETrans.PatternAnal.Mach.
|     |     |     |     |     |     |     | Intell., | vol. 46, no. 5, pp. | 1234–1247, | May | 2024. [Online]. | Available: |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------------- | ---------- | --- | --------------- | ---------- | --- |
andGNNsintegratetopologicalstructurestopreciselymodel
https://arxiv.org/abs/2401.13912
| interdependencies |     | within | time series. | Hybrid | models | can |                 |              |              |        |               |           |     |
| ----------------- | --- | ------ | ------------ | ------ | ------ | --- | --------------- | ------------ | ------------ | ------ | ------------- | --------- | --- |
|                   |     |        |              |        |        |     | [5] D. Salinas, | V. Flunkert, | J. Gasthaus, | and T. | Januschowski, | ‘‘DeepAR: |     |
Probabilisticforecastingwithautoregressiverecurrentnetworks,’’Int.J.
| enhance | prediction | robustness | and | interpretability |     | by com- |     |     |     |     |     |     |     |
| ------- | ---------- | ---------- | --- | ---------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
Forecasting,vol.36,no.3,pp.1181–1191,Jul.2020.
biningthemodelingoflinearandnonlinearfeatureswiththe
|     |     |     |     |     |     |     | [6] S. Makridakis, | E. Spiliotis, | and | V. Assimakopoulos, |     | ‘‘Statistical | and |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | ------------- | --- | ------------------ | --- | ------------- | --- |
incorporationofphysicalconstraintsordomainknowledge.
machinelearningforecastingmethods:Concernsandwaysforward,’’PLoS
ONE,vol.13,no.3,Mar.2018,Art.no.e0194889.
| However, | despite | significant | progress | in  | deep | learning- |     |     |     |     |     |     |     |
| -------- | ------- | ----------- | -------- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
[7] W.LiandK.L.E.Law,‘‘Deeplearningmodelsfortimeseriesforecasting:
basedtimeseriesprediction,challengesremain.Forinstance,
Areview,’’IEEEAccess,vol.12,pp.92306–92327,2024.
the interpretability of models continues to be a critical [8] H.I.Fawaz,G.Forestier,J.Weber,L.Idoumghar,andP.-A.Müller,‘‘Deep
|               |           |     |                         |     |       |       | learning | for time series | classification: | A review,’’ | Data | Mining | Knowl. |
| ------------- | --------- | --- | ----------------------- | --- | ----- | ----- | -------- | --------------- | --------------- | ----------- | ---- | ------ | ------ |
| issue in deep | learning. | In  | practical applications, |     | users | often |          |                 |                 |             |      |        |        |
Discovery,vol.33,no.4,pp.917–963,2019.
requireinsightsintothemodel’sdecision-makingprocessand
[9] S.Haben,M.Voss,andW.Holderbaum,‘‘Timeseriesforecasting:Core
prediction rationale to enhance data analysis and decision- conceptsanddefinitions,’’inCoreConceptsandMethodsinLoadFore-
making. Additionally, the high computational complexity casting.Cham,Switzerland:Springer,2023,pp.55–66.
|     |     |     |     |     |     |     | [10] G.E.P.Box,G.M.Jenkins,andG.C.Reinsel,TimeSeriesAnalysis: |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
ofdeeplearningmodelsdemandssubstantialcomputational ForecastingandControl,5thed.,Hoboken,NJ,USA:Wiley,2015.
resourcesandtime.Addressingcomputationalefficiencyfor [11] W.PedryczandS.-M.Chen,DeepLearning:AlgorithmsandApplications.
large-scaletimeseriesdataremainsanunresolvedchallenge. Cham,Switzerland:Springer,2020.
|     |     |     |     |     |     |     | [12] X.Kong,W.Zhang,Z.Li,Y.Wang,L.Zhao,H.Chen,S.Liu,andQ.Yang, |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
Future research directions for deep learning-based time ‘‘Deeplearningfortimeseriesforecasting:Asurvey,’’Int.J.Mach.Learn.
seriespredictionmodelsmayfocusonthefollowingareas: Cybern.,vol.123,pp.456–489,Jan.2025.
(a) Enhancing Model Interpretability: Developing visu- [13] Y.Nie,Y.Chen,J.Guo,S.Li,Y.Xiao,W.Gong,andR.Lan,‘‘Animproved
CNNmodelinimageclassificationapplicationonwaterturbidity,’’Sci.
alization tools and explanation methods (e.g., attention Rep.,vol.15,no.1,p.11264,Apr.2025.
analysis,featureimportanceattribution)toimprovethetrans- [14] S.Bai,J.Z.Kolter,andV.Koltun,‘‘Anempiricalevaluationofgeneric
convolutionalandrecurrentnetworksforsequencemodeling,’’inProc.
parencyofmodeldecisionsandpredictions.
35thInt.Conf.Mach.Learn.(ICML),2018,pp.4321–4330.
(b))OptimizingEfficiency:Exploringmoreefficientalgo- [15] A. van den Oord, S. Dieleman, H. Zen, K. Simonyan, O. Vinyals, A.
rithms and architectures (e.g., model compression, neural Graves,N.Kalchbrenner,A.Senior,andK.Kavukcuoglu,‘‘WaveNet:A
generativemodelforrawaudio,’’2016,arXiv:1609.03499.
architecturesearch,efficientattentionmechanisms)toreduce
|     |     |     |     |     |     |     | [16] K.He,X.Zhang,S.Ren,andJ.Sun,‘‘Deepresiduallearningforimage |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
computationalcomplexityandimprovescalability.
recognition,’’inProc.IEEEConf.Comput.Vis.PatternRecognit.(CVPR),
Jun.2016,pp.770–778.
| (c) Integrating |     | Multi-Source | Data | and | Domain | Knowl- |               |                   |     |          |                 |             |     |
| --------------- | --- | ------------ | ---- | --- | ------ | ------ | ------------- | ----------------- | --- | -------- | --------------- | ----------- | --- |
|                 |     |              |      |     |        |        | [17] Y. Chen, | Y. Kang, Y. Chen, | and | Z. Wang, | ‘‘Probabilistic | forecasting |     |
edge:Enhancingmodelgeneralizationandaccuracythrough
withtemporalconvolutionalneuralnetwork,’’Neurocomputing,vol.399,
| the effective | fusion | of heterogeneous |     | data | sources | (e.g., |     |     |     |     |     |     |     |
| ------------- | ------ | ---------------- | --- | ---- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- |
pp.491–501,Jul.2020,doi:10.1016/j.neucom.2020.03.011.
|                 |       |           |                 |                   |             |     | [18] A.Borovykh,S.M.Bohté,andC.W.Oosterlee,‘‘Conditionaltimeseries |                    |        |             |            |          |     |
| --------------- | ----- | --------- | --------------- | ----------------- | ----------- | --- | ------------------------------------------------------------------ | ------------------ | ------ | ----------- | ---------- | -------- | --- |
| sensor data,    | text, | images)   | and             | the incorporation |             | of  |                                                                    |                    |        |             |            |          |     |
|                 |       |           |                 |                   |             |     | forecasting                                                        | with convolutional | neural | networks,’’ | J. Comput. | Finance, |     |
| domain-specific |       | expertise | (e.g., physical | laws,             | operational |     |                                                                    |                    |        |             |            |          |     |
vol.22,no.4,pp.73–91,2018.
constraints). [19] X.S.Dong,L.J.Qian,andL.Huang,‘‘Short-termloadforecastingin
(d) Advancing Data Preprocessing and Feature Engineer- smartgrid,’’inProc.IEEEInt.Conf.BigDataSmartComput.,May2017,
pp.119–125.
| ing: Improving |     | data quality | and model | usability |     | through |                                                                |     |     |     |     |     |     |
| -------------- | --- | ------------ | --------- | --------- | --- | ------- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                |     |              |           |           |     |         | [20] M.Liu,A.Zeng,M.Chen,Z.Xu,Q.Lai,L.Ma,andQ.Xu,‘‘SCINet:Time |     |     |     |     |     |     |
refined preprocessing techniques (e.g., handling missing seriesmodelingandforecastingwithsampleconvolutionandinteraction,’’
values, normalization, decomposition) and feature extrac- inProc.Adv.NeuralInf.Process.Syst.,2021,pp.5816–5828.
|     |     |     |     |     |     |     | [21] J. Elman, | ‘‘Finding structure | in  | time,’’ Cognit. | Sci., | vol. 14, | no. 2, |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------------------- | --- | --------------- | ----- | -------- | ------ |
tion/selection strategies (e.g., automated feature learning, pp.179–211,Jun.1990,doi:10.1016/0364-0213(90)90002-e.
domain-informedfeatures). [22] Z.C.Lipton,J.Berkowitz,andC.Elkan,‘‘Acriticalreviewofrecurrent
In conclusion, deep learning has introduced new oppor- neuralnetworksforsequencelearning,’’2015,arXiv:1506.00019.
|     |     |     |     |     |     |     | [23] S.HochreiterandJ.Schmidhuber,‘‘Longshort-termmemory,’’Neural |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
tunities and breakthroughs in time series prediction. While Comput.,vol.9,no.8,pp.1735–1780,Nov.1997.
challengespersist,ongoingtechnologicaladvancementswill [24] S.-H. Noh, ‘‘Analysis of gradient vanishing of RNNs and performance
enable these models to play an increasingly vital role comparison,’’Information,vol.12,no.11,p.442,Oct.2021.
|     |     |     |     |     |     |     | [25] K.Cho,B.vanMerriënboer,C.Gulcehre,D.Bahdanau,F.Bougares,H. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
across diverse fields. They will provide robust support for Schwenk,andY.Bengio,‘‘LearningphraserepresentationsusingRNN
decision-making,riskassessment,andresourceoptimization, encoder-decoderforstatisticalmachinetranslation,’’inProc.Conf.Empir.
MethodsNaturalLang.Process.(EMNLP),Oct.2014,pp.1724–1734.
| propelling | intelligent | development |     | in various | industries | to  |                                                                     |     |     |     |     |     |     |
| ---------- | ----------- | ----------- | --- | ---------- | ---------- | --- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|            |             |             |     |            |            |     | [26] A.Casado-Mansilla,D.López-de-Ipiña,M.S.Z.B.Garbi,K.Tsagarakis, |     |     |     |     |     |     |
newheights.
P.D.Moschonas,V.Kelli,andI.Karydis,‘‘Webtraffictimeseriesfore-
castingusingLSTMneuralnetworkswithdistributedtraining,’’Appl.Sci.,
vol.11,no.16,p.421,Aug.2021.
REFERENCES [27] Y. S. Cheng, X. M. Wang, and H. Li, ‘‘A deep learning time series
featureextractionmodel,’’Autom.ElectricPowerSyst.,vol.47,no.12,
[1] R.J.HyndmanandG.Athanasopoulos,Forecasting:PrinciplesandPrac- pp.123–130,2023.
tice,3rded.,Melbourne,VIC,Australia:OTexts,2021.
|     |     |     |     |     |     |     | [28] X.Wang,J.Wu,C.Liu,H.Yang,Y.Du,andW.Niu,‘‘Faulttimeseries |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
[2] A.Casolaro,V.Capone,G.Iannuzzo,andF.Camastra,‘‘Deeplearning prediction based on LSTM recurrent neural network,’’ J. Beijing Univ.
fortimeseriesforecasting:Advancesandopenproblems,’’Information,
AeronauticsAstronautics,vol.44,no.4,pp.772–784,2018.
vol.14,no.11,p.598,Nov.2023,doi:10.3390/info14110598.
|     |     |     |     |     |     |     | [29] X. | Lin, Y. Li, Z. | Wang, | H. Zhang, | and | L. Liu, | ‘‘A |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------------- | ----- | --------- | --- | ------- | --- |
[3] X.Kong,Z.Chen,W.Liu,K.Ning,L.Zhang,S.M.Marier,Y.Liu,Y.Chen, method for predicting electric vehicle charging load,’’ CN
andF.Xia,‘‘Deeplearningfortimeseriesforecasting:Asurvey,’’IEEE Patent 1,16,910789 A, Oct. 2023. [Online]. Available:
Trans.Knowl.DataEng.,vol.33,no.3,pp.1096–1117,Mar.2025. https://www.xjishu.com/zhuanli/55/202310612121.html
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     | 153711 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

X.Aoetal.:ReviewofTimeSeriesPredictionModelsBasedonDeepLearning
[30] R.Fu,Z.Zhang,andL.Li,‘‘UsingLSTMandGRUfortrafficflowpre- [55] S.Lan,Y.Ma,W.Huang,W.Wang,H.Yang,andP.Li,‘‘DSTAGNN:
diction,’’inProc.31stYouthAcademicAnnu.Conf.Chin.Assoc.Automat., Dynamicspatial-temporalawaregraphneuralnetwork,’’inProc.39thInt.
| 2016,pp.324–328. |     |     |     |     |     |     | Conf.Mach.Learn.(ICML),2022,pp.11906–11917. |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- |
[31] Y. Qi, J. Li, H. Wang, Z. Wang, J. Tang, and D. He, ‘‘A deep neural [56] Y.Wang,Z.Liu,J.Zhang,H.Li,X.Chen,andL.Wang,‘‘Hierarchical
frameworkforsalesforecasting,’’inProc.28thACMInt.Conf.Inf.Knowl.
spatio-temporalgraphnetworkswithmulti-scaleattention,’’inProc.Neu-
| Manage.,vol.2019,pp.299–308. |     |     |     |     |     |     | ralIPS,2023. |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
[32] S.Xin,C.Li,Z.Li,T.Zhang,Y.Wang,andY.Yu,‘‘Multi-taskbasedsales [57] L.Chen,R.Senanayake,K.H.W.Brooks,M.J.Kochenderfer,andM.
predictions,’’inProc.28thACMInt.Conf.Inf.Knowl.Manage.,2019, Pavone, ‘‘STAN: Spatio-temporal attention for dynamic hazard predic-
| pp.2823–2831. |     |     |     |     |     |     | tion,’’inProc.ICML,2024. |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |
[33] A.Vaswani,N.Shazeer,N.Parmar,J.Uszkoreit,L.Jones,A.N.Gomez, [58] T.Tuncer,U.Kaya,E.Sefer,O.Alacam,andT.Hoser,‘‘Assetpriceand
Ł.Kaiser,andI.Polosukhin,‘‘Attentionisallyouneed,’’inProc.31stInt. direction prediction via deep 2D transformer and convolutional neural
Conf.NeuralInf.Process.Syst.,vol.30,2017,pp.5998–6008. networks,’’inProc.3rdACMInt.Conf.AIFinance,2022,pp.79–86.
[34] T.Andeen,J.Gonski,J.Hirschauer,J.Hoff,G.Matos,andJ.Parsons,
|     |     |     |     |     |     |     | [59] G. P. | Zhang, ‘‘A | hybrid ARIMA-LSTM |     | model | for forecasting,’’ | IEEE |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | ----------------- | --- | ----- | ------------------ | ---- |
‘‘Readout for calorimetry at future colliders: A snowmass 2021 white Trans. Neural Netw. Learn. Syst., vol. 28, no. 10, pp.2322–2333,
| paper,’’2022,arXiv:2204.00098. |     |     |     |     |     |     | Oct.2017. |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
[35] S. Sia, A. Dalmia, and S. J. Mielke, ‘‘Tired of topic models? Clusters [60] G.Woo,C.Liu,D.Sahoo,A.Kumar,andS.Hoi,‘‘ETSformer:Exponen-
ofpretrainedwordembeddingsmakeforfastandgoodtopicstoo!’’in
tialsmoothingtransformersfortimeseriesforecasting,’’inProc.ICLR,
| Proc.Conf.EmpiricalMethodsNaturalLang.Process.(EMNLP),2020, |     |     |     |     |     |     | 2023. |     |     |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
pp.1691–1700,doi:10.18653/v1/2020.emnlp-main.135. [61] B. N. Oreshkin, D. Carpov, N. Chapados, and Y. Bengio, ‘‘N-BEATS:
[36] H.Zhou,S.Zhang,J.Peng,S.Zhang,J.Li,H.Xiong,andW.Zhang, Neuralbasisexpansionanalysis,’’Int.J.Forecasting,vol.36,no.3,pp.
| ‘‘Informer: | Beyond | efficient | transformer | for | long sequence | time-series | 1181–1191,2020. |     |     |     |     |     |     |
| ----------- | ------ | --------- | ----------- | --- | ------------- | ----------- | --------------- | --- | --- | --- | --- | --- | --- |
forecasting,’’ in Proc. 35th AAAI Conf. Artif. Intell. (AAAI), 2021, [62] Y.Nie,N.H.Nguyen,P.Sinthong,andJ.Kalagnanam,‘‘PatchTST:Patch-
pp.11106–11115. based models for time series forecasting,’’ in Proc. ICML, 2023, pp.
[37] H.Wu,J.Xu,J.Wang,andM.Long,‘‘Autoformer:Decompositiontrans- 18789–18808.
formersforautomaticforecasting,’’inProcAdv.NeuralInf.Process.Syst., [63] A.Incremona,G.DeNicolao,F.Fusco,B.J.Eck,andS.Tirupathi,‘‘Aggre-
vol.34,2021,pp.22419–22430. gationofnonlinearlyenhancedexpertswithapplicationtoelectricityload
[38] S.Yu,H.Wang,Z.Li,X.Chen,andL.Zhang,‘‘Trafficstateprediction forecasting,’’Appl.SoftComput.,vol.112,Nov.2021,Art.no.107857,
usingautoformer,’’Comput.-AidedCiv.Infrastruct.Eng.,vol.39,no.18, doi:10.1016/j.asoc.2021.107857.
pp.2774–2787,2024.
[39] Y.Liu,T.Hu,H.Zhang,H.Wu,S.Wang,L.Ma,andM.Long,‘‘ITrans- XIQINAOwasborninAnhui,China,in1987.She
former:Invertedtransformersareeffectivefortimeseriesforecasting,’’in received the bachelor’s degree from Chongqing
|     |     |     |     |     |     |     |     |     | University | of  | Technology, | in 2010, | the mas- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----------- | -------- | -------- |
Proc.ICLR,2024.
[40] T. Zhou, Z. Ma, Q. Wen, X. Wang, L. Sun, and R. Jin, ‘‘FEDformer: ter’sdegreefromHefeiUniversityofTechnology,
Frequencyenhanceddecomposedtransformerforlong-termseriesfore- in2013,andthePh.D.degreeincomputerscience
casting,’’ in Proc. Int. Conf. Mach. Learn. (ICML), Baltimore, MD, from National University, Manila, Philippines,
| USA,2022,pp.11168–11186. |     |     |     |     |     |     |     |     | in2024. |     |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
[41] A.H.B.GeziciandE.Sefer,‘‘Deeptransformer-basedassetpriceand She is currently an Associate Professor and
directionprediction,’’IEEEAccess,vol.12,pp.24164–24178,2024.
workswithAnhuiXinhuaUniversity.Herresearch
[42] S.Wu,X.Xiao,Q.Ding,P.Zhao,Y.Wei,andJ.Huang,‘‘Adversarial
|     |     |     |     |     |     |     |     |     | focuses | on the | application | of deep | learning in |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ----------- | ------- | ----------- |
sparsetransformerfortimeseriesforecasting,’’inProc.Adv.NeuralInf.
|     |     |     |     |     |     |     | various fields, | including | but not | limited | to time series | prediction, | natural |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --------- | ------- | ------- | -------------- | ----------- | ------- |
Process.Syst.,vol.33,2020,pp.17105–17115.
[43] R. Child, S. Gray, A. Radford, and I. Sutskever, ‘‘Generating long languageprocessing,andindustrialoptimization.SheisamemberofChina
sequenceswithsparsetransformers,’’2019,arXiv:1904.10509. ComputerFederation(CCF).
[44] Y. Li, H. Zhang, C. Wang, J. Liu, X. Chen, and L. Wang, ‘‘Towards YUJIEGONGwasborninAnhui,China,in1987.
long-termtime-seriesforecasting:feature,pattern,anddistribution,’’IEEE
Hereceivedthebachelor’sdegreefromChongqing
Trans.Knowl.DataEng.,vol.35,no.12,pp.12415–12427,Dec.2023.
UniversityofTechnology,in2010,andthemas-
[45] T.Kim,J.Kim,Y.Tae,C.Park,J.-H.Choi,andJ.Choo,‘‘Scaleformer:
ter’sdegreefromHefeiUniversityofTechnology,
| Reversible | instance | normalization |     | for accurate | time-series | forecasting |     |     |     |     |     |     |     |
| ---------- | -------- | ------------- | --- | ------------ | ----------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
in2013.
| against      | distribution | shift,’’ | in Proc. | 11th Int. | Conf. Learn. | Represent. |     |     |                                        |     |     |     |     |
| ------------ | ------------ | -------- | -------- | --------- | ------------ | ---------- | --- | --- | -------------------------------------- | --- | --- | --- | --- |
| (ICLR),2023. |              |          |          |           |              |            |     |     | HeiscurrentlytheDeputyGeneralManagerof |     |     |     |     |
theSecurityDivision,SichuangElectronicsCom-
| [46] Z. Zhang, | A.  | Zhang, W. Yang, | Z. Wang, | and | M. Long, | ‘‘Crossformer: |     |     |      |                   |     |            |            |
| -------------- | --- | --------------- | -------- | --- | -------- | -------------- | --- | --- | ---- | ----------------- | --- | ---------- | ---------- |
|                |     |                 |          |     |          |                |     |     | pany | Ltd., responsible | for | overseeing | operations |
Transformerutilizingcross-dimensiondependencyformultivariatetime
|     |     |     |     |     |     |     |     |     | and | maintenance | project | management, | market |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ----------- | ------ |
series,’’inProc.NeuralIPS,2023.
[47] S.LundbergandS.Lee,‘‘Aunifiedapproachtointerpretingmodelpredic- expansionintheoperationsandmaintenancesec-
tions,’’inProc.Adv.NeuralInf.Process.Syst.,2017. tor, and strategic planning. His work integrates deep learning techniques
[48] M.T.Ribeiro,S.Singh,andC.Guestrin,‘‘‘WhyshouldItrustyou?’’’ forintelligentsecuritysystemoptimization.HeisalsocertifiedasanITSS
inProc.ACMSIGKDDInt.Conf.Knowl.DiscoveryDataMining,2016,
OperationandMaintenanceStandardsEvaluationExpertinChina.
pp.1135–1144.
|     |     |     |     |     |     |     |     |     | AIXIANG | HE  | was born | in Susong, | Anqing, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | -------- | ---------- | ------- |
[49] Z.Zhang,P.Cui,andW.Zhu,‘‘Deeplearningongraphs:Asurvey,’’IEEE
|     |     |     |     |     |     |     |     |     | Anhui, | China, | in 1978. She | received | the degree |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | ------------ | -------- | ---------- |
Trans.Knowl.DataEng.,vol.34,no.1,pp.249–270,Jan.2020.
[50] Z.LiuandJ.Zhou,IntroductiontoGraphNeuralNetworks.SanMateo, in electronic technology from Hefei Union Uni-
CA,USA:MorganKaufmann,2020. versity, China, in 2001, the bachelor’s degree
[51] B. Yu, H. Yin, and Z. Zhu, ‘‘Spatio-temporal graph convolutional net- in e-commerce from Beijing Normal University,
works,’’ in Proc. 27th Int. Joint Conf. Artif. Intell. (IJCAI), 2018, pp. China,in2008,themaster’sdegreeincomputer
3634–3640.
applicationfromAnhuiUniversity,China,in2011,
[52] Z.Wu,S.Pan,G.Long,J.Jiang,X.Chang,andC.Zhang,‘‘Connecting
|     |     |     |     |     |     |     |     |     | and the | Ph.D. | degree in | computer | science from |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----- | --------- | -------- | ------------ |
thedots:Multivariatetimeseriesforecastingwithgraphneuralnetworks,’’
NationalUniversity,Manila,Philippines,in2024.
inProc.26thACMSIGKDDInt.Conf.Knowl.DiscoveryDataMining, Since2001,shehasbeenanAssociateProfes-
Aug.2020,pp.753–763.
|               |        |                    |     |             |        |                 | sor with Anhui | Xinhua | University. | She | presided | more than | three quality |
| ------------- | ------ | ------------------ | --- | ----------- | ------ | --------------- | -------------- | ------ | ----------- | --- | -------- | --------- | ------------- |
| [53] P. Celik | and E. | Sefer, ‘‘Analyzing |     | transaction | graphs | via motif-based |                |        |             |     |          |           |               |
engineeringprojectsofAnhuiProvincialDepartmentofEducationandone
graphrepresentationlearningforcryptocurrencypriceprediction,’’Com-
majoronlineteachingreformresearchprojectofAnhuiProvince.Shehas
put.Econ.,vol.2025,pp.1–22,Apr.2025.
[54] A. Zanfei, B. M. Brentan, A. Menapace, M. Righetti, and M. Her- publishedmorethantenresearcharticlesindomesticandforeignjournals,
rera,‘‘Graphconvolutionalrecurrentneuralnetworksforwaterdemand including three by EI and one by CSCD. Her research interests include
forecasting,’’ Water Resour. Res., vol. 58, no. 7, Jul. 2022, doi: machinelearningandnaturallanguageprocessing.
10.1029/2022wr032299.
| 153712 |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |