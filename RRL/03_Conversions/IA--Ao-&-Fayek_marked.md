sensors
SystematicReview
Continual Deep Learning for Time Series Modeling
Sio-IongAo1,*andHaythamFayek2
1 InternationalAssociationofEngineers,Unit1,1/F,HungToRoad,HongKong
2 SchoolofComputingTechnologies,RMITUniversity,Building14,Melbourne,VIC3000,Australia;
haytham.fayek@rmit.edu.au
* Correspondence:siao@graduate.hku.hk
Abstract:Themulti-layerstructuresofDeepLearningfacilitatetheprocessingofhigher-levelabstrac-
tionsfromdata,thusleadingtoimprovedgeneralizationandwidespreadapplicationsindiverse
domainswithvarioustypesofdata.Eachdomainanddatatypepresentsitsownsetofchallenges.
Real-world time series data may have a non-stationary data distribution that may lead to Deep
Learningmodelsfacingtheproblemofcatastrophicforgetting,withtheabruptlossofpreviously
learnedknowledge.Continuallearningisaparadigmofmachinelearningtohandlesituationswhen
thestationarityofthedatasetsmaynolongerbetrueorrequired.Thispaperpresentsasystematic
reviewoftherecentDeepLearningapplicationsofsensortimeseries,theneedforadvancedprepro-
cessingtechniquesforsomesensorenvironments,aswellasthesummariesofhowtodeployDeep
Learningintimeseriesmodelingwhilealleviatingcatastrophicforgettingwithcontinuallearning
methods.Theselectedcasestudiescoverawidecollectionofvarioussensortimeseriesapplications
andcanillustratehowtodeploytailor-madeDeepLearning,advancedpreprocessingtechniques,
andcontinuallearningalgorithmsfrompractical,real-worldapplicationaspects.
Keywords: deeplearning; continuallearning; sensor; timeseries; preprocessing; non-stationary;
catastrophicforgetting
1. Introduction
Time series modeling is a challenging task in data mining and machine learning.
Citation:Ao,S.-I.;Fayek,H.
Populartimeseriesmodelingtasksincludeclassification,anomalydetection,regression,
ContinualDeepLearningforTime
SeriesModeling.Sensors2023,23, forecasting,andclustering. Atimeseriesisasequenceofmeasurementstakenatvarious
7167. https://doi.org/10.3390/ times. Spatialtimeseriesdatareferstomultipletimeseriesdatacorrespondingtodifferent
s23167167 spatiallocations. Thespatial–temporalmodelsfacedifficultiesinaddressingnotonlythe
short-termandlong-termpatternsbutalsothespatialpatterns[1]. Timeseriesdatasets
AcademicEditors:ChimanKwan
have the property of temporal ordering by nature [2]. Generally speaking, time series
andAnabelaOliveira
modelshavethecapabilitytoutilizethefactthatobservationsclosertogetherintimerelate
Received:12June2023 moreclosely. Timeseriesmodelinghasmanyreal-worldapplicationslikeenvironmentand
Revised:31July2023 traffictasks,andsuccessfulmodelingforthetimeserieshasbecomeincreasinglyimportant.
Accepted:10August2023 Forexample,windtimeseriesforecastingisessentialforthedecision-makingofelectric
Published:14August2023 systemoperators.
Time series analysismodels can be dividedbroadlyinto time domain modelsand
frequency domain models. The time domain model investigates the data with respect
totime,whilethefrequencydomainmodelsfocustheanalysisonfrequencyinsteadof
Copyright: © 2023 by the authors.
time[2]. Statisticalmodelslikeautoregressivemodelsandthemovingaveragemodelsare
Licensee MDPI, Basel, Switzerland.
populartimedomainmodels. Preprocessingoperationslikedatacleaning,normalization,
This article is an open access article
differencing,featureselection,etc.,arealsopopulartimedomainmodels. Forthefrequency
distributed under the terms and
domain methods, mathematical models are employed to convert the time series data
conditionsoftheCreativeCommons
between the time and frequency domains. The Fourier transform is a popular, simple,
Attribution(CCBY)license(https://
andbasictransformingtoolforcomputingthefrequencydomainrepresentationofatime
creativecommons.org/licenses/by/
4.0/).
Sensors2023,23,7167.https://doi.org/10.3390/s23167167 https://www.mdpi.com/journal/sensors

Sensors2023,23,7167 2of32
series. Otherpopularpreprocessingoffrequencydomainarewavelettransformation(WT),
empiricalmodedecomposition(EMD),etc.
Overthelastdecade,smartsensorshavebeendeployedonaverylargescale,and
hugeamountsofcontinuousdatahavebeengenerated[3].Machinelearning(ML)methods
canextractvaluableinformationfromdatasetsandhavebeenwidelyemployedforsensory
data in the industry, such as in the sensing and condition monitoring fields [4]. In the
knowledgediscoveryprocess,feedbackisgeneratedateachiterationwiththegoalthat
furtherimprovementcanbeachieved[5]. DeepLearning(DL),aparticulartypeofmachine
learning algorithm with multi-layer structures for processing higher-level abstractions
fromtheinputdataset[6],isverywellsuitedforverylargedatasets,asmostofitslayer
computationscanbeimplementedinparallelanddistributedcomputingtechniquescanbe
appliedeasily. DeepLearningmodelshavebeenshowntoperformsatisfactorilyformany
timeseriesanalysistaskslikeforecasting.
DeepLearning(DL)hasbeendevelopedfromtraditionalneuralnetworkswithlarge-
sizeddeepstructuressince2006. Comparedwithtraditionalmachinelearning,DLlearns
through a general-purpose learning procedure of multiple levels of representation and
identifiesfeaturesautomatically[7]. Ineachlayer,therepresentationisobtainedfromthe
representationofthepreviouslayer,involvingupdatingprocesswithaback-propagation
algorithm. DifferentfromthemoretraditionalMLmethods,theadditionofmorelayers
intheDeepLearningmodelcanfurtherenablethedeepnetworktocopewithscenarios
ofincreasingcomplexity,thusleadingtoimprovedgeneralization. Amulti-layerlearn-
ing structure enables very high performance in complex situations like video, speech,
classificationproblems,andmulti-sensoraggregation.
Deep Learning models have been shown to perform satisfactorily for many time
seriesanalysistasks. Forexample,DeepLearninghasprovenexcellentinhumanactivity
recognition (HAR) tasks, where wearable sensors can connect people with the cyber–
physical system through HAR [8]. Deep Learning has also been employed for tipping-
point prediction, with performance better than traditional early warning systems [9].
Nevertheless, the reliability of these forecasting methods is not guaranteed [10]. Deep
Learningmethodsmayalsofacetheoverfittingproblem. Commonpreprocessingmethods
likesmoothing,transformation,andestimationcanremovethenoiseintimeseriessignalsin
advanceandimprovetheoverallperformanceofthetimeseriesmodels. Theperformance
ofDeepLearningmodelsmayimprovewithpreprocessingoftimeseriesinputs,usually
onconditionsthatthedatadistributionattesttimeissimilartothatattrainingtime.
WhenbuildingMLmodels,itisusuallyassumedthatthedistributionofthedatais
stationary. Whenthestatisticalpropertiesofatimeseriesdonotdependontime,thetime
seriesiscalledstationary[2]. Itispossiblethatatimeseriesisstationaryintermsofone
characteristicwhilenon-stationaryforanothercharacteristic. Mathematically,atimeseries
TS(y )isdefinedtobe(weakly)stationaryifalltimet:
t
E(y t )=E[(y t−1 )]=µ,
Var(y )=σ2<∞,
t
Cov(y
t
,y
t−k
)=γ(k),
where the expected value µ is represented by E(.), the variance σ2 by Var(.), and the
covarianceγbyCov(.),respectively[11]. Ifthestationaryconditionsarenolongertrue,the
non-stationarybehaviorsmayposesignificantdifficultiesfortimeseriesapplicationslike
remotesensing[12].
Inmanyreal-worldapplications,thestationarityofthedatasetsmaynolongerbetrue.
Therearefourbasiccomponentsthatcancausethenon-stationarityinsometimeseries.
Thesefourcomponentsaretrend,seasonal,cyclical,andirregularcomponents[13]. The
trendcomponentreferstolong-termincreasesordecreasesovertime,withexampleslike
long-termpopulationgrowth.Theseasonalcomponentreferstotheexistenceofseasonality

Sensors2023,23,7167 3of32
patterns, like, forexample, timeserieswithyearly, quarterly, ormonthlypatterns. The
cyclicalcomponentreferstothepatternsofupsanddownsofatimeseriesovertheduration
ofacycle. Theeconomictimeseriesdataofeconomicgrowthandtheneconomicrecession
mayhaveacyclicalcomponent. Theirregularcomponentisduetounpredictablefactors
anddoesnotrepeatwithparticularpatterns. Forsometimeseriesdatathatexhibitasimple
trend, seasonal, and cyclical components, DL methods may be deployed directly with
satisfactoryresults,asseeninthefirstpartofSection2. Forsomemorecomplicatedsensor
timeseriesdatasets,advancedpreprocessingtoolsmaybeneeded,asseeninthesecond
partofSection2. Amongthetimeseriesdatasetsthatcannotbehandledwellwithboth
advancedpreprocessingandDLmethods,somemayfitthescenariosforthedeployment
ofCLmethods,whicharedescribedindetailinSection3.
Continuallearningisaparadigmofmachinelearningthatmayhandlesomeofthe
non-stationarysituationswhileimitatingthecapabilityofhumanintelligencetohandlenew
situationsfromtheoldexperienceslearned. CLalgorithmsaredevelopedtomimichuman
intelligencethatwillrarelyforgetallofthelearnedinformation,asthenaturalsystemwill
onlygraduallylosethelearnedinformation[14]. Ontheotherhand, traditionalneural
networks(NNs),whilemimickinghumancognition,lackthisabilityandfacecatastrophic
forgetting(CF).IfDeepLearningmethodsarenaivelyemployedinCLtasks,learningon
shifteddistributionmayleadtoCFproblems. Thecapabilityofhowtolearncontinuallyis
oneofthebiggestunsolvedissuesinML[15],whileforgettinglearnedknowledgeisthe
keyobstacletocontinuallearning[16].
Thissurveyfocusessolelyonreal-worldpracticaltimeseriesapplicationswithDL
andCL.Langeetal.[17]presentedasurveyonCLaboutthestability–plasticitytrade-off
andfocusedontheproblemsofclassificationonly. Themotivationforthemtolimitthe
discussiontoclassificationaloneisthatNNhasbeenverywell-establishedforclassification
tasks. Inthesurvey[18],itwashighlightedthatthemostrecentsurveysusuallycovered
continual learning partially, like biological underpinnings [19–22], visual classification
tasks [23–26], NLP tasks [27,28], and RL [29]. Wang et al. [18] talked about only five
tasksofpracticalCLapplications,i.e.,objectdetection,semanticsegmentation,conditional
generation, reinforcement learning, and NLP. None of the above-mentioned recent CL
surveysfocusedontimeseriesanalysistasksliketimeseriesforecasting. Thefocusofthis
surveyissolelyonthecurrentapplicationcasestudiesofDLforsensortimeseriesdatasets.
ItprovidesasummaryofthedifficultiesthattheDLfacesindeploymentforreal-world
sensorapplicationsandtheadvancedpreprocessingtechniquesforhowtoaddresssomeof
thesepracticaldifficulties. TherearesomecasesthattypicalDLapproaches,togetherwith
advancedpreprocessingtechniques,canhandlewell. Nevertheless,insomeothertime
seriesapplicationcases,continuallearningisfoundtobesuitablefordeployment. The
topicofdeployingCLforsensortimeseriesmodelinghasnotbeensystemicallycoveredin
theseprevioussurveys.
Thispaperisorganizedwiththefollowingsections,coveringtherecenttimeseries
applicationsofDeepLearningandcontinuallearning. InSection2,firstly,thefocusison
thecurrentadvancesindeployingDeepLearningmethodsforsensortimeseriesmodeling.
Then,therecentsensorcasestudiesthatstillrequiredatapreprocessingtechniquesforDL
modulesarehighlighted. InSection3,asummaryofthesensortimeseriesdatasetsand
environmentsthatsuitthedeploymentofcontinuallearningmethodsisundertaken.
2. AdvancesinDeepLearningMethodsforTimeSeriesModeling
DeepLearningiscapableofmodelingthecomplexnon-linearrelationshipsamong
thevariables,whiletraditionalneuralnetworkneedstoassumethatallinputvectorsare
independent,whichmayleadtoitsineffectivenessforsequentialdataprediction[30]. Com-
paringDLwiththeconventionaltimeseriesmethods[13,31],itisfoundthatDeepLearning
modelscangivebetterrepresentationandclassification. Caietal.[31](2019)investigated
theday-aheadmulti-steploadpredictionofcommercialbuildingswithRNNandCNN
againstautoregressiveintegratedmovingaveragewithexogenousinputs(ARIMAX),a

Sensors2023,23,7167 4of32
populartraditionaltimeseriesmethodforthetimeseriesmodelingofloadforecasting.
TheresultsshowthattheCNNapproachwithadirectmulti-stepprocedurecanperform
betterthantheseasonalARIMAXbya22.6%improvementinpredictionaccuracy. This
illustratedthattheDeepLearninghierarchicalstructuremayhavethecapabilitytohan-
dledata-dependentuncertaintybetter. Itisalsoshownthatthelong-termtrendscanbe
exploredbetterwhenthepreprocessingtoolofthemovingaveragesmethodisdeployed
forsmoothingtheshort-termfluctuations. MahmoudandMohammed[13]presenteda
surveyofDeepLearningmodels,suchasCNN,RNN,LSTM,GRU,deepautoencoders
(AEs),restrictedBoltzmannmachines(RBM),deepbeliefnetworks(DBNs),inthetime
seriesforecastingofelectricityloadandprice,solarpower,andfinance,withcomparison
resultsshowingthatDLperformsbetterthanclassicalmethods.
AfterdiscussingtheadvantagesofdeployingDLmethodswithtimeseriesdata,the
followingTable1showsasyntheticsummaryoftheadvancesinDeepLearningtechniques
forreal-worldsensortimeseriesapplications,followedbyadetaileddescriptionofthe
corresponding methods, motivations, and advantages. The following Figure 1 shows
the tree diagram grouping the popular Deep Learning methods for sensor time series
classificationandforecastingtaskscoveredinthissurvey.
Table1.SummaryoftheadvancesinDLtechniquesforsensortimeseriesapplications.
|                  | Application |          | DeepLearning |          |         |
| ---------------- | ----------- | -------- | ------------ | -------- | ------- |
| Ref. FirstAuthor | Year        | Datasets |              | Accuracy | Details |
|                  | Field       |          | Models       |          |         |
Watertreatment
CompareDLanomaly
|     | Timeseries | test-bed,water |                 | Noclear |                     |
| --- | ---------- | -------------- | --------------- | ------- | ------------------- |
|     |            |                | RNN,CNN,hybrid, |         | detectiontimeseries |
[32] Choi 2021 anomaly distributionpipelines, one-size-fits-all
|     |           |             | attention |        | modelswith |
| --- | --------- | ----------- | --------- | ------ | ---------- |
|     | detection | MarsScience |           | method |            |
benchmarkdatasets
Laboratoryrover
|           | Detecting     | Sensortimeseries |                | 54%better        | Combinegraphneural |
| --------- | ------------- | ---------------- | -------------- | ---------------- | ------------------ |
|           | deviationfrom | datasetsofwater  | GraphDeviation |                  | networkswith       |
| [33] Deng | 2021          |                  |                | F-measurethanthe |                    |
|           | normal        | treatmentsystems | Network        |                  | structuredlearning |
nextbestbaseline
|     | patterns | (SWaTandWADI) |     |     | approach |
| --- | -------- | ------------- | --- | --- | -------- |
Notsignificantly
Conductcomparison
betterthan1-NN
|            | Timeseries     | UCRTimeSeries         | MLP,CNN, |                 | betweennearest |
| ---------- | -------------- | --------------------- | -------- | --------------- | -------------- |
| [34] Jiang | 2020           |                       |          | classifierswith |                |
|            | classification | ClassificationArchive | ResNet   |                 | neighborandDL  |
dynamictime
models
warping
SOAperformance
Univariate
|                  | Timeseries     |                      | MLP,CNN,Echo | achievedwith | Conductempirical  |
| ---------------- | -------------- | -------------------- | ------------ | ------------ | ----------------- |
| [35] IsmailFawaz | 2019           | timeseriesdatasetsof |              |              |                   |
|                  | classification |                      | StateNetwork | CNNanddeep   | studyofDNNsforTSC |
theUCR/UEAarchive
ResidualNetworks
|     | Leafandwood |     |     | Accurate | CompareDLmodels |
| --- | ----------- | --- | --- | -------- | --------------- |
Sevenbroad-leaved
terrestriallaser FullyConvolutional separationofleaf onleafandwood
trees(Ulmus
[36] Han 2022 scanningtime NeuralNetwork, andwoody classificationwitha
americana)withaRigel
|     | series |     | LSTM-FCN,ResNet | componentsfrom | timeseriesofgeometric |
| --- | ------ | --- | --------------- | -------------- | --------------------- |
VZ-400i
|     | classification |     |     | pointclouds | features |
| --- | -------------- | --- | --- | ----------- | -------- |
Evaluatedeep
Achievingbest
Campos- Classification Sentinel-2timeseries 2-layerBi-LSTM recurrentnetwork
| [37]     | 2020      |      |         | overallaccuracyof |                    |
| -------- | --------- | ---- | ------- | ----------------- | ------------------ |
| Taberner | oflanduse | data | network |                   | 2-BiLSTMforlanduse |
98.7%
classification
Real-time
|     | classificationof |     |     | Superior | ApplyCNNtofind |
| --- | ---------------- | --- | --- | -------- | -------------- |
Databaseofdriver
[38] Naqvi 2020 normaland CNN performancevs. changesingazefrom
facialemotionandgaze
|     | abnormal |     |     | previousmethods | driver’simages |
| --- | -------- | --- | --- | --------------- | -------------- |
driving
Trafficflow
|            |                 | Trafficflowtimeseries |      | Outperformthe | DeployLSTMfor          |
| ---------- | --------------- | --------------------- | ---- | ------------- | ---------------------- |
| [39] Zheng | 2020 timeseries |                       | LSTM |               |                        |
|            |                 | fromOpenITS           |      | ARIMAandBPNN  | trafficflowforecasting |
forecasting

Sensors2023,23,7167 5of32
Table1.Cont.
|                  | Application |          | DeepLearning |          |         |
| ---------------- | ----------- | -------- | ------------ | -------- | ------- |
| Ref. FirstAuthor | Year        | Datasets |              | Accuracy | Details |
|                  | Field       |          | Models       |          |         |
Traffic
|     | predictionand |     |     |     | DeploytheRandom |
| --- | ------------- | --- | --- | --- | --------------- |
Reduced
|     | usermobility |     | Random |     | ConnectivityLSTMfor |
| --- | ------------ | --- | ------ | --- | ------------------- |
[40] Hua 2019 oftelecommu- Traffictimeseries ConnectivityLSTM computing trafficanduser
complexityby30%
|     | nication |     |     |     | mobilityprediction |
| --- | -------- | --- | --- | --- | ------------------ |
problems
|           |                  | Reliabilitytestdataofa |               |                 | EmployDNN               |
| --------- | ---------------- | ---------------------- | ------------- | --------------- | ----------------------- |
|           | Equipment        |                        | DeepLearning  | Significant     |                         |
|           |                  | cylinderinthesmall     |               |                 | frameworkfor            |
| [41] Chen | 2020 reliability |                        | methodbasedon | improvementover |                         |
|           |                  | trolleyofvehicle       |               |                 | reliabilityevaluationof |
|           | prediction       |                        | MLP           | PCAandHMM       |                         |
|           |                  | assemblyplant          |               |                 | cylinder                |
Conductsurveyof
Hybridmodelwith
[42] Lim 2021 Timeseries M4competition(Smyl, Exponential betterperformance commonencodersand
|     | forecasting | 2020) | smoothingRNN |     | decodersfortimeseries |
| --- | ----------- | ----- | ------------ | --- | --------------------- |
thanpuremethods
forecasting
Employgenerative
Strong
|             |             | Publicdatasets      |                    |                | adversarialpredictive |
| ----------- | ----------- | ------------------- | ------------------ | -------------- | --------------------- |
|             | Plantgrowth |                     | Generative         | performance    |                       |
| [43] Yasrab | 2021        | (Arabidopsisand     |                    |                | networkforleafand     |
|             | forecasting |                     | AdversarialNetwork | matchingexpert |                       |
|             |             | Brassicarapaplants) |                    |                | rootpredictive        |
annotation
segmentation
Deploydeepnetwork
Alzheimer’s Timeseriesdatafrom Ensembleofstacked fordetectingcommon
|                 | disease     | Alzheimer’sDisease |                   | Muchbetterthan |                   |
| --------------- | ----------- | ------------------ | ----------------- | -------------- | ----------------- |
| [44] El-Sappagh | 2020        |                    | CNNand            |                | patternsfor       |
|                 | progression | Neuroimaging       |                   | conventionalML |                   |
|                 |             |                    | BidirectionalLSTM |                | classificationand |
|                 | detection   | Initiative         |                   |                |                   |
regressiontasks
Twelvepublic
MLP,ElmanRNN,
datasetscovertime
|     | Twelvetime |                        | LSTM,EchoState |            |                      |
| --- | ---------- | ---------------------- | -------------- | ---------- | -------------------- |
|     |            | seriesapplicationslike |                |            | Evaluatesevenpopular |
|     | series     |                        | Network,GRU,   | LSTMandCNN |                      |
[45] Lara-Benitez 2021 finance,industry,solar DLmodelsintermsof
|     | forecasting |                         | CNN,Temporal  | arethebestchoices |                       |
| --- | ----------- | ----------------------- | ------------- | ----------------- | --------------------- |
|     |             | energy,tourism,traffic, |               |                   | efficiencyandaccuracy |
|     | tasks       | and                     | Convolutional |                   |                       |
Network
internettraffic
Investigating
|          | temporal          |                       |                  |                     | DeveloptheSpectral |
| -------- | ----------------- | --------------------- | ---------------- | ------------------- | ------------------ |
|          |                   | Timeseriesdatasets    |                  | Outstanding         |                    |
|          | correlationsof    |                       | SpectralTemporal |                     | TemporalGraph      |
|          |                   | fromenergy,           |                  | forecastingresults, |                    |
| [46] Cao | 2020 intra-series |                       | GraphNeural      |                     | NeuralNetworkfor   |
|          |                   | electrocardiogram,and |                  | plusadvantageof     |                    |
|          | andthe            |                       | Network          |                     | multivariabletime  |
|          |                   | trafficsectors        |                  | interpretability    |                    |
|          | correlationsof    |                       |                  |                     | seriesforecasting  |
inter-series
|                 | Predictionof  |                       |               |                  | Evaluatemodelsbased    |
| --------------- | ------------- | --------------------- | ------------- | ---------------- | ---------------------- |
|                 |               | Timeseriesdataof      |               | Betterprediction |                        |
|                 | solar         |                       | RNN,LSTM,GRU, |                  | onaccuracy,forecasting |
| [30] Rajagukguk | 2020          | temperature,humidity, |               | resultsthan      |                        |
|                 | irradianceand |                       | CNN-LSTM      |                  | horizon,trainingtime,  |
|                 |               | andwindspeed          |               | conventionalML   |                        |
|                 | photovoltaic  |                       |               |                  | etc.                   |
DeepLearning
|     |     |     | approach,basedon | Particularly |     |
| --- | --- | --- | ---------------- | ------------ | --- |
DeployDLapproach
|     | Solarenergy | Two-yeartimeseriesof | theH20package | suitableforbig |     |
| --- | ----------- | -------------------- | ------------- | -------------- | --- |
forsolarphotovoltaic
[47] Torres 2018 generation PVpowerfroma withthegridsearch solardata,givenits
powerforecastingfor
forecasting rooftopPVplant methodfor strongcomputing thenextday
|     |     |     | hyper-parameter | behavior |     |
| --- | --- | --- | --------------- | -------- | --- |
optimization
|     | Predictionof | SSTtimeseries |     | Outperform | DeployConvLSTMto |
| --- | ------------ | ------------- | --- | ---------- | ---------------- |
seasurface datafrom36-year ConvolutionalLong persistencemodel, capturecorrelationsof
| [48] Xiao | 2019 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
temperature observationsby Short-TermMemory SVR,andtwo SSTacrossbothspace
|     | (SST) | satellite |     | LSTMmodels | andtime |
| --- | ----- | --------- | --- | ---------- | ------- |
Multi-layer perceptron (MLP), recurrent neural network (RNN), Long Short-Term
Memorynetwork(LSTM),convolutionalneuralnetwork(CNN),graphneuralnetworks
(GNN), deep belief network (DBN), autoencoder (AE), and neural networks with an
attention mechanism are popular DL methods that have been used by the authors in
thissurvey.

Sensors 2023, 23, x FOR PEER REVIEW 7 of 35
Sensors2023,23,7167 6of32
Figure1. TreediagramforgroupingthepopularDeepLearningmethodsforsensortimeseries
classification and forecasting tasks covered in this survey [30,32–48] (note: if a paper uses two
methodsseparatelywithsimilarsatisfactoryresults,thepaperwillbelistedunderbothgroups).
2.1. Multi-LayerPerceptron
MLP is the most conventional and simplest Deep Learning structure and is fully
connected(FC)betweenlayers. Alltheneuronsinonelayerareconnectedtoeveryneuron
inthenearbynextlayer. Thismeansthateachtimeseriesrecordisassigneditsownweight,
andthetemporalinformationisnotutilized[35]. DuringthetrainingphaseoftheMLP,
theweightbetweentheneuronsoftwonearbylayerscanbeestimatedbytheminimization

Sensors2023,23,7167 7of32
ofcostfunctionthroughgradientdescentoptimization. Thecomputingofthegradientof
thecostfunctionisusedintheback-propagationalgorithm.
Jiang [34] conducted a comprehensive evaluation of the Deep Learning methods
(MLP,CNN,andResNet)againstaconventionalmachinelearningmethod—thenearest
neighbor. The 1-NN classifiers are deployed with eight different distance measures. A
totalof128univariatetimeseriesdatasetsaboutimage,motion,andsensorfromtheUCR
TimeSeriesClassificationArchive[49]weretestedfortheclassificationperformanceof
themodels. TheexperimentalresultsshowedthattheDeepLearningmethodscouldhave
betterperformancethanthenearestneighbor,buttheirdifferenceisnotsignificantwhen
appropriatedistancemeasuresaredeployedforthenearestneighborbasedonthetypesof
thetimeseriesdatasets.
IsmailFawazetal.[35]comprehensivelyevaluatedtheperformanceofthreepopular
structuresofDeepLearningfortimeseriesclassification(TSC),i.e.,MLP,CNN,andEcho
StateNetwork(ESN).TheDeepLearningmodelsforTSCtaskscanbeclassifiedasgen-
erativeanddiscriminativeapproaches. TheessentialstructureofESNisthereservoir,a
sparselyconnectedrandomRNNwithrandominitializationinthehiddenlayers. Jaeger
andHaas[50]inventedtheESNin2004fortimeseriesforecastingforwirelesscommunica-
tiontasks. Theevaluationwasconductedwiththe85univariatetimeseriesdatasetsofthe
UCR/UEAarchive[51]and13MTSdatasetsfromBaydogan’sarchive[52]. Forunivariate
time series applications, a one-dimensional CNN model is used, and the filter can be
viewedasperforminganon-lineartransformationforthetimeseries. Formultivariatetime
series,thedimensionsofthefilteraresettobethenumberofdimensionsofthetimeseries.
Fortimeseriesclassification,thefinallayeristhediscriminativelayerwhichcanassign
probabilitydistributionfortheclassvariablesofthetimeseriesconcerned. Theresults
supportedthatend-to-endDeepLearningisabletoreachstate-of-the-artperformancefor
TSCtasks.
Chen et al. [41] presented a Deep Learning method based on MLP for equipment
reliabilitypredictionwithsensortimeseriesdata. Conditionmonitoringforequipmentand
itsmaintenancepredictionisimportantforsmartmanufacturing. Itisdesirabletoconduct
maintenancebeforethemachinefailurehappens. Theexperimentwasconductedwitha
reliabilitytestofacylinderinthesmalltrolleyofvehicleassemblyplant. Asittakeslonger
tocompleteeachoperationforanagingcylinder,thecylinderoperationdurationcanserve
asthetimeseriesinputsfortheDeepLearningmethod. TheresultsshowthattheDeep
Learningmethodcanperformmuchbetterthanconventionalmachinelearningmethods.
Lara-Benitezetal.[45]comparedtheperformanceofsevenpopularDeepLearning
algorithms against twelve time series forecasting tasks. Time series forecasting is the
process of utilizing relevant historical time records to determine future values. When
deployingCNNfortimeseriesmodeling,causalconvolutionalfiltersareusedtoensure
thatforecastingismadeonlybasedonpastinformationinthetimeseries[53]. Thesame
asstandardCNN,temporalCNNalsosharesthesameassumptionthattherelationships
amongthetimeseriesvariablesaretime-invariant. Inattentionmechanisms,thetemporal
features of the time series signals can be aggregated with the dynamical generation of
weights by the attention layers. The attention network can pay more attention to the
significanthistoricalevent,nomatterhowfarbackitisinthekey-valuelookupwindow.
The Deep Learning models are MLP, four models of recurrent networks (Elman RNN,
LSTM,EchoStateNetwork,GRU),andtwoconvolutionalnetworks(CNNandTemporal
ConvolutionalNetwork). Thetwelvepublicdatasetscovertimeseriesapplicationslike
finance,industry,solarenergy,tourism,traffic,andinternettraffic. Theevaluationresults
showed that LSTM performs the best, while CNN can also make accurate and stable
forecastingwithlesscomputationalrequirements. Anotherperformancecomparisonof
Deep Learning methods can be found in Torres et al. [54], making a summary of the
satisfactory time series forecasting applications of the popular Deep Learning models
(ENN,LSTM,GRU,BRNN,MLP,CNN,andTCN)inthesectorslikeenergy,environment,
finance, health, industry, and image. The practical tip on how to set hyper-parameters

Sensors2023,23,7167 8of32
hasalsobeencovered. Thefourmaintypesofhyper-parameteroptimizationmethodsare
trial-error,grid,randomandprobabilistic.
Torres et al. [47] proposed a Deep Learning approach that was based on the H20
packagewritteninRwiththegridsearchmethodforhyper-parameteroptimizationand
implementedintheApacheSparkclusterenvironment. Asthemanufacturingcostforsolar
panelsdecreases,solarenergyisbecomingmuchmorepopular. Itispredictedthat30%
ofthetotalelectricitysourceswillbefromsolarenergyinAustraliabytheyear2050[55].
Factors like cloud cover, rainfall, solar radiation, and temperature can affect the gener-
ation of solar energy significantly and make the forecasting of solar energy generation
difficult. The dataset is the two-year time series of PV power with 30 min observation
interval. Itsperformancewascomparedwithpattern-sequence-basedforecasting(PSF)and
conventionalneuralnetworks. TheexperimentalresultssupportedthattheDeepLearning
approachisverysuitableforthesolarenergyforecastingtask.
2.2. RecurrentNeuralNetwork
RNNisdesignedwithastatefortheinformationattimestepssuchthatitcanhandle
sequence data element-wise [56]. As it can maintain the dependencies among the time
series elements, RNN has gained success in different fields such as image captioning,
machinelearningtranslation,speechrecognition[57],andweatherforecasting[58]. Elman
NeuralNetwork(ENN)isanRNNmodelwithanewhiddenlayercalledthecontextlayer,
whichmakesitcapableofdatasequenceprediction. Nevertheless,RNNfacesdifficulties
duetothevanishingandexplodinggradientproblemsduringitstrainingprocess. This
disadvantageofthevanishinggradientproblemcanbeamplifiedwhenconsideringlong-
rangedependentrelationships.
Choietal.[32]focusedonthefrontiertimeseriesanomalydetectionmethodsand
described how the methods model the interrelationship among variables and how the
temporalcontextwaslearned. Timeseriesanomalydetectionisabouttheidentification
ofunexpectedeventsfromthetimeseriesdata. Becauseoftheirlearningcapabilityfor
large-scalesequences,DeepLearningmethodscontributesignificantlytomultivariatetime
seriesanomalydetection. Nevertheless,mostofthesemethodshavebeendevelopedfor
veryspecificapplications,andsufficientdomainknowledgeisnecessary[32]. Benchmark
datasetsofthewatertreatmenttest-bed,thewaterdistributionpipelines,andtheMars
ScienceLaboratoryroverwereusedtocomparetheperformanceofthemethods(RNN,
CNN,hybrid,andattention). TheresulthighlightsthatthereisnosingleDeepLearning
methodthatcanfituniversallywithallthetimeseriestasks. EventhoughemergingDeep
Learningmethodsshowencouragingresultsformultivariatetimeseriesanomalydetection,
mostofthesemethodscannotexplaintherelationshipsamongthesensorsandthushave
limitedabilitytoexplainthedeviationsoftheanomalousevents.
LimandZohren[42]summarizedtherecenttrendsofDeepLearningmodelsandhy-
bridmodels. HybridmethodscombiningquantitativetimeseriesmodelswithDeepLearn-
ingmayaddresstheselimitationsandimprovetheoverallforecastingperformance[42].
A hybrid model may be able to incorporate domain experts to feed the Deep Learning
modelwithpriorinformationwhileaddressingtheissuesassociatedwithsmalldatasets
andoverfitting. ExponentialsmoothingRNN(ES-RNN)servesasagoodexampleofhow
theexponentialsmoothingmodulecanhelptheRNNbyaddressingthenon-stationary
trendsofthetimeseriesbywinningtheM4competition[59].
El-Sappaghetal.[44]presentedanensembleDeepLearningapproachofstackedCNN
andBidirectionalLSTM(Bi-LSTM)modelsforADprogressiondetection. Thetemporal
information from sensor monitoring of chronic disease can be helpful for progression
detection,whiletheprogressionofchronicAlzheimer’sdisease(AD)maybedelayedif
it can be predicted at an early stage. The data of AD patients are heterogeneous multi-
modalities. Bi-LSTMisaspecialtypeofLSTMthatcanexplorethedependenciesofboth
previousandfuturestates[6]. FortimeseriespredictionwithBidirectionalLSTM,oncea
forecastisavailableintraining,thisvaluecanbeutilizedforthesubsequentreadjustment

Sensors2023,23,7167 9of32
process. Thismayresultinadeeperunderstandingofthecontextconcerned. Themodel
canhandlethefusionofthefivedifferenttypesoftimeseriesdataalongwithbackground
knowledge. ThestackedCNNandBi-LSTMmodelsarecapableofextractingbothlocal
andlongitudinalfeaturesofthemodality,andthesystemcanmakepredictionsbasedon
theseresultantfeatures. ThetimeseriesdatafromtheAlzheimer’sDiseaseNeuroimaging
Initiativewereused,andtheresultssupportthesuperiorperformanceoftheproposed
ensembleDeepLearningapproach. Fortraditionalmethodstosucceedinstructuralhealth
monitoring, suitable preprocessing of the raw sensor time series data is nearly always
needed. Dangetal.[60]appliedfourpopularDeepLearningmodels,i.e.,MLP,LSTM,1D
CNN,andCNN,forstructuraldamagedetectionwithrawtimeseriesdata. Nofeature
engineering procedure like extracting structural characteristics was performed. Three
differentstructurescoveringsmalltolargestructuresweretested. Theexperimentalresults
supportthat2DCNNisthemostreliable,eventhoughthecomputationaltimeof2DCNN
isalsothehighestamongthemodels.
2.3. LongShort-TermMemory
Hochreiterand Schmidhuber [61]designedanewRNNmodel, calledLongShort-
TermMemory(LSTM),withaninternalmemoryunitandgatemechanism,foraddressing
theissuesofvanishingandexplodinggradientduringRNNtraining. Aself-feedingloopis
usedintheinnerlayersofLSTMthatcanlearntime-basedcorrelationssuchthatknowledge
frompreviousinputscanbeusedintheanalysisofthepresentinputs. Thethreegates
implementation [6] of LSTM can reduce the effects of the vanishing gradient problem
faced by RNN. The three gates are the forget gate, update gate, and output gate. The
forgetgateistodeterminewhatinformationshouldbekeptornot. Theupdategateis
to determine what new information should be utilized for updating the memory state.
Theoutputgateistodeterminetheoutputvaluethatwillserveastheinputinthenext
hidden unit. This design can enable the keeping of longstanding related information
whileforgettingunrelatedinformation. Thus,LSTMhasthecapabilitytoprocessthelong-
termdependenciesofinformationintemporaldatasetsandisdeployedforapplications
likespeechrecognition,trafficprediction,andweatherforecasting. TheGatedRecurrent
Unit(GRU)isdesignedwithalesscomplexRNNstructurethanLSTM[62]butcanalso
rememberusefulinformationandexplorethelong-termdependenciesofthevariables. A
GRUhasonlytwogates,i.e.,theupdategateandtherelevancegate. Theupdategateisto
determineifthememorystateistoupdateornot. Therelevancegateistodeterminehow
relatedthepreviousmemorystateisforcomputingthenextcandidate. AsGRUhasonly
twogates,itrequiresfewerparametersandcomputationaltimethanLSTM[63]whilestill
keepingthecapabilityforhandlingverylong-rangerelationshipsamongthetimeseries.
HanandSanchez-Azofeifa[36]investigatedtheleafandwoodterrestriallaserscan-
ning (TLS) time series classification with Fully Convolutional Neural Network (FCN),
LSTM-FCN,andResidualNetwork(ResNet). CNNhasbeenfoundtobecapableofper-
formingtimeseriesclassificationsatisfactorily,asitsmultiplefilterscanproducemultiple
discriminationfeaturesforclassificationfromthetemporalinputs[35]. Itisalsofound
thatthecombinedLSTM-FCNmethodcanfurtherimprovethetimeseriesclassification
resultsbyFCN[64]. TLSpointclouddataareusefulforclassifyingtheleafandwoody
components,andthustheleafareaindexandwoodareaindex. TheTLStimeseriespoint
cloudswereobservedfromsevenbroad-leavedtrees(Ulmusamericana). Theexperimental
resultsshowedthatallthreemodelsworkbetterwithmultivariabletimeseriesthanwith
univariabletimeseries. Thethreemodelscanalsoworkbetterthanpreviousmethods,and
allthesethreemodelsproducesimilarperformancesonthetestingtimeseries.
Campos-Taberner et al. [37] investigated the interpretability of a 2-layer Bi-LSTM
networkfortheclassificationoflanduseinValencia,Spain,withSentinel-2timeseriesdata.
Added-noisepermutationprocedurewasemployedinbothtemporalandspectraldomains
for evaluating the impact of different spectral and temporal features on the accuracy
rate. Theexperimentalresultsshowedthattheoverallaccuracyof98.7%achievedbythe

Sensors2023,23,7167 10of32
proposedmethodisbetterthanotherclassificationapproaches. Theproposedsystemcan
alsoshowtherelevanceofpredictorsandhighlightthattheredandnear-infraredSentinel-2
bandscontainthemosthelpfulinformation,whilethesummertimeseriesdataismost
usefulamongthetemporalinformation.
ZhengandHuang[39]deployedtheDeepLearningLSTMnetworkfortheforecasting
oftrafficflowtimeseries. Inanintelligenttrafficsystem,theaccurateforecastingoftraffic
flow may help to reduce urban congestion. The traffic flow time series from OpenITS
with5minintervalsintendayswasused,anditsperformancewasevaluatedwiththe
traditionalstatisticalmethod(ARIMA)andtheconventionalmachinelearningmethod
(BPNN).TheresultssupportthesuperiorpredictionaccuracyoftheLSTMmodel,with
themeanabsolutepercentageerrorsofARIMA,BPNN,andLSTMat20.97%,9.06%,and
4.82%,respectively.
Huaetal.[40]deployedtheRandomConnectivityLSTM(RCLSTM)fortrafficpredic-
tionandusermobilityoftelecommunicationproblemsinordertoreducethecomputational
requirementofLSTM.InRCLSTM,theneuronsareconnectedstochastically, andsome
sparsitycanbeachievedinthisrandomsparsegraphmodeltoreducecomputingtime.
RCLSTMisfoundtobesuitableforlatency-stringenttasksliketraffictimeseries. Another
similar task is the evaluation of the traffic time series data from the GEANT backbone
network by Uhlig et al. [65]. The experimental results showed that the forecasting per-
formanceofRCLSTMissimilartothetraditionalLSTMwhilesuccessfullyreducingthe
computationaltime.
Rajagukguketal.[30]investigatedthepredictionperformanceofsolarirradianceand
photovoltaic(PV)powerwithfourDeepLearningmodelsagainstconventionalmachine
learningmethods. Assolarenergyisrenewable,solarphotovoltaicshasgainedpopularity
inthegenerationofelectricity. ForthePVprediction,thepopularinputtimeseriesdata
arethetemperature,humidity,andwindspeed. Theexperimentalresultsconfirmedthat
all four Deep Learning models, i.e., RNN, LSTM, GRU, and CNN-LSTM, can perform
thepredictionbetter,withCNN-LSTMachievingthebestperformancebutalsoneeding
thelongesttrainingtimeperiod. InthehybridmodelCNN-LSTM,theCNNlayerscan
performthefeatureextractionoftheinputtimeseries,whileLSTMforsequenceprediction.
CNN-LSTMhasbeendesignedwiththecapabilitytohandletemporalpredictiontasksand
appliedinmanyreal-worldapplications. Experimentalresultslike[66]alsosupportedthe
consistentlybetterperformancebyCNN-LSTMoverLSTMforprecipitationprediction.
2.4. ConvolutionalNeuralNetwork
CNN is another popular neural network for time series modeling. CNN is a DL
methodofinterconnectedfeedforwardnetworkarchitecturesconsistingofasequenceof
convolution,pooling,activationlayers,and,finally,fullyconnectedlayers[67]. Filtering
operationisperformedintheconvolutionallayersthroughafeaturemap.Localconfluences
offeaturesareidentifiedfromtheprecedinglayerthroughdiscreteconvolution. Thus,this
typeofmodelbecomesknownasaconvolutionalneuralnetwork. Thepoolinglayeris
forreducingtheinputsizeandavoidingoverfitting. Theinputforthelastdenselayeris
theflattenedfeaturesfromtheconvolutionalandpoolinglayers, andtheforecastingis
madeinthisdenselayer. 1DCNNcanbedeployedforsimpleapplications,whilemore
sophisticatedmodels,likeCNN-Net,Enoded-Net,andCNN-LSTM,havemoreadvanced
structureslikelargerkernelsizeanddenserlayers.
Naqvi et al. [38] deployed a CNN model for detecting changes in gaze from the
face and left- and right-eye images. Driver time series data is helpful for the real-time
classificationofnormalandabnormaldrivingand,thus,forreducingaggressivedriving.
Thenear-infrared(NIR)camerasensorisemployedheretoconstructalargedatabaseof
driverfacialemotionandgaze. TheDlibfacialfeaturetrackerswereemployedtoidentify
theregionofinterest(ROI)beforefeedingtotheCNNmodel. Theexperimentalresults
supportedtheoutstandingperformanceoftheCNNmodel.

Sensors2023,23,7167 11of32
2.5. GraphNeuralNetwork
GNNisaneuralnetworkthatprocessesthedatawithrepresentationingraphdomains,
like in chemical compounds, images, and web [68]. Graphs can be classified as cyclic,
directed,undirected,oracombinationofthesethree. GNNshavebeenfoundusefulfor
applicationsincludingchemistry,citationnetworks,environmentalconditionforecasting,
molecularbiology,physics,andsocialnetworks. AfewDNNtopologiesmayindeedbe
viewedasGNN,forexample,withCNNconsideredasaGNNwithgraphsofpixel-per-
gridgrids.
DengandHooi[33]developedaGraphDeviationNetwork(GDN)modelfordiscov-
eringtherelationshipgraphamongthesensorsandfordetectingdeviationfromnormal
patterns.Graphneuralnetworkscanmodelthecomplexpatternsindataofgraphstructure,
withthenodestateinfluencedbyitsneighbornotestates. Velickovicetal.[69]developed
the graph attention network (GAT), which employed the attention function for evalu-
ating the various weights for various neighbors during aggregation. A difficulty for a
typical GNN model is that the graph structure is needed as an input, while this struc-
turemaynotbeknowninadvance. Theproposedsystemconsistsofsensorembedding,
graph-structuredlearning,graph-attention-basedforecasting,andgraphdeviationscoring.
Thesystemistestedwithtwolarge-scalesensortimeseriesdatasetsofwatertreatment
systems(SWaTandWADI).Theexperimentalresultssupportedtheperformanceofthe
proposedsystem,whiletheinterpretableoutputcanassistusersinbetterunderstanding
andlocalizinganomalies.
Caoetal.[46]presentedSpectralTemporalGraphNeuralNetwork(StemGNN)with
GraphFourierTransform(GFT)forcapturinginter-seriescorrelationsandDiscreteFourier
Transform(DFT)fortemporalcorrelations. Adifficultyformultivariatetimeseriesisthe
complexityinvolvingboththetemporalcorrelationsofintra-seriesandthecorrelationsof
inter-seriessimultaneously.ThespectralrepresentationsobtainedwithGFTandDFTenable
theDeepLearningmodulestohaveclearenoughpatternsfortheanalysis.Theexperimental
resultsfromtenreal-worldtimeseriespublicdatasets(fromenergy,electrocardiogram,and
trafficsectors)confirmtheperformanceoftheproposedStemGNN.
2.6. OthersandHybrids
HintonandOsinderoetal.[70]developedthefirstmodelandtrainingalgorithmfora
deepbeliefnetwork(DBN)in2006. DBNhasahierarchicalstructurewithalargenumber
of stacked restricted Boltzmann machines (RBMs) and utilizes a greedy layer-by-layer
learningapproachwithfine-tuning. TheRBMscanefficientlyextractthefeaturesforthe
initializationoffeedforwardneuralnetworks,henceimprovingthenetworkgeneralization
capability. IneachRBM,thereisbothavisiblelayerandaconcealedlayerconsistingof
neurons. WhiletheRBM’slayersareinterconnectedwitheachother,theunitsamongeach
layerarenot.TheupdatingofthenetworkparameterscanbedonewithaSoftMaxclassifier.
Autoencoderutilizesafeaturelearningparadigmthatcanlearnpara-metricmaps
directlyfrominputstocorrespondingrepresentation[71,72]. AnAEconsistsofanencoder
andadecoder. Theencoderisforfeatureextraction,whilethedecoderisformappingthe
featurespacebacktotheinputspace. Thestructureoftheencoderanddecoderisaninput
layer, hidden layers, and an output layer. Back-propagation algorithm is deployed for
updatingtheweightsofthehiddenlayers. DeepAEcanserveasadata-drivenapproach
forlearningfeatureextractionautomatically.
Neuralnetworkswithanattentionmechanismhavesucceededintimeseriesappli-
cations[73]. Thesenetworkscandynamicallycontrolthemappingfromtheinputstothe
outputsintelligentlywithotherknowledgeofthetask. Thetransformermodelisbased
on an encoder–decoder architecture of these networks. The input is fed to the encoder,
whichconsistsofastackofencoders. Then,thetransformercangeneratetheoutputbased
ontheencodedinputandpreviousoutputsinthedecoderaswell. Aclearadvantageof
transformersistheaccesstoanypointsinthepast,nomatterhowfartheirdistancesare,
leadingtothecapabilitytodiscoverthelong-termdependenciesamongthetimeseriesdata.

Sensors2023,23,7167 12of32
Yasrabetal.[43]designedaGenerativeAdversarialNetwork(GAN)forforecasting
the expected growth of the plant. Plant phenotyping is the investigation of plant trait
growthandotherquantitativeparametersandmaybeautomatedwiththehelpofDeep
Learning. GANisusuallydevelopedfromCNNandisformedwithtwonetworks,i.e.,the
generatorandthediscriminator. Bothnetworkscanlearntogetherbycompetingwitheach
othertogeneratenewexamplesofsyntheticdata. Segmentationmasksofshootandroot
weregeneratedtopredicttheplantsysteminthefuture. Twopublicdatasets(Arabidopsis
andBrassicarapaplants)wereused. Theevaluationresultsillustratedthattheproposed
systemcanreachthelevelwithannotationbyanexpert.
Xiaoetal.[48]developedaConvolutionalLongShort-TermMemory(ConvLSTM)
modeltoutilizethespatiotemporalcorrelationsofseasurfacetemperature(SST)forits
short and mid-term prediction. In the global ocean, SST has a significant influence on
the marine ecosystem. SST time series data from 36-year observations by satellite was
usedtoevaluatetheConvLSTMagainstthepersistencemodel,supportvectorregression
model,andLSTMmodels. WhenhandlingspatiotemporaldatabyfullyconnectedLSTM
(FC-LSTM),itisnotedthatthespatialcorrelationscanbelost[66]. Toaddressthisissue,
theConvLSTMreplacestheFC-LSTMmatricmultiplicationwithconvolutionoperation
inthetransitions. Thisistoensurethatthemodelcanexplorebothspatialandtemporal
correlations. TheexperimentalresultsconfirmedthatConvLSTMperformsbetterthan
othermethodsfortheone-to-ten-day-aheadpredictionofSSTtimeseries.
2.7. AdvancedPreprocessingandDeepLearningApplications
Feature engineering can be very important in the data preprocessing stage before
feedingdatatotheDeepLearning modelsbysignificantlyreducingthecomputational
requirementsforunnecessaryfeatures. ItsimportanceishighlightedintheworkofElsayed
andThyssensetal.[74],whichevaluatedthetimeseriesforecastingperformanceofeight
DeepLearningmethodsagainstthetraditionalmachinelearningmethod—theGradient
BoostingRegressionTree(GBRT).Externalfeatureswereutilizedforthetargetvalues,and
dataflatteningcanobtaintheoneinputinstanceforGBRT.Theevaluationwasconducted
withninedatasetscoveringairquality,electricity,finance,solarenergy,andtraffic. The
resultsshowedthatthewindow-basedtransformationcouldenableGBRTtoachievethe
bestforecastingperformanceovertheDeepLearningmodels,coveringvarioustypeslike
matrix factorization, RNNs, LSTMs, and bi-directional LSTM models. It is shown that
simplermachinelearningmodelswithefficientfeatureengineeringcanoutperformthe
frontier Deep Learning methods without feature engineering. Dablander and Bury [9]
highlightedtheimportanceofpreprocessingbyshowingthattheDLmodelcannotextract
enoughrelevantfeaturesforclassifyingthestationaryAR(1)processeswithoutdetrending
orwithaGaussianfilter. Theresultsshowedthatthemethodmightlearnuniquefeatures
relatedtoaLowessfilterinsteadoftherelevantfeaturesofthesystemnearthebifurcation.
Thus,carefulplanningisneededwhendeployingthepreprocessingmodels.
ThefollowingTable2highlightsthemostrecentcasestudiesthatadvancedprepro-
cessing is still needed, along with the Deep Learning methods, for modeling different
popular typesof sensortime series. In Table 2, asynthetic summary ofthe application
fields,theadvancedpreprocessingtechniques,theDLmethods,accuracy,andbriefappli-
cationdetailsispresented,followedbyamoredetaileddescriptionofthecorresponding
methods,motivations,andadvantages. ThefollowingFigure2showsthetreediagram
forgroupingthepopularpreprocessingmethodsforsensortimeseriesclassificationand
forecastingtaskscoveredinthissurvey.

Sensors2023,23,7167 13of32
Table2. Summaryoftheimportanceofadvancedpreprocessingtechniquesforreal-worldsensor
timeseriesDLapplications.
|     |     | Preprocessing | DeepLearning |     |     |
| --- | --- | ------------- | ------------ | --- | --- |
Ref. FirstAuthor Year ApplicationField Methods Models Accuracy Details
ECGtimeseries
DevelopaDL
signalsfor
|     |     | Squeezingand |     | Achievedmore | architectureforthe |
| --- | --- | ------------ | --- | ------------ | ------------------ |
monitoringand
[75] Kanani 2020 stretchingofthesignal 1Dconvolution than99% preprocessingprocess
classificationof
|     |     | alongthetimeaxis |     | accuracy | forincreasedtraining |
| --- | --- | ---------------- | --- | -------- | -------------------- |
cardiovascular
stability
health
Surface
DeployEMDto
|           | electromyography |               |     | Worstresults | segmentedsignalto  |
| --------- | ---------------- | ------------- | --- | ------------ | ------------------ |
|           | timeseriesof     | Empiricalmode |     | fororiginal  |                    |
| [76] Kisa | 2020             |               | CNN |              | obtaintheIntrinsic |
|           | humanmusclesfor  | decomposition |     | signalvs.all |                    |
ModeFunctions(IMFs)
gesture IMFsimages
imagesforCNN
classification
|     | Classifyingeight |     |     | Achievedbest | Evaluatetheimpactof |
| --- | ---------------- | --- | --- | ------------ | ------------------- |
Segmentationand
|           | dailyactivities |                |     | resultswith  | segmentationand |
| --------- | --------------- | -------------- | --- | ------------ | --------------- |
| [8] Zheng | 2018            | transformation | CNN |              |                 |
|           | fromwearable    |                |     | multichannel | transformation  |
methods
|     | sensors |     |     | method | methodsonDLmodels |
| --- | ------- | --- | --- | ------ | ----------------- |
Apply3D
SyntheticAperture 3D-Gamma LSTM, Highaccuracy spatial–temporalfilters
[77] CastroFilho 2020 Radarimagesfor filterandmethodof Bidirectional andKappa andsmoothingwith
ricecropdetection SavitzkyandGolay LSTM (>97%) Savitzky–Golayfilterto
minimizenoise
Presentthe
Atmospheric
|     | Classifyingcrop |                        |                  | Preprocessing | preprocessingpipeline, |
| --- | --------------- | ---------------------- | ---------------- | ------------- | ---------------------- |
|     |                 | correction,filteringof | 1D-convolutions, |               |                        |
|     | typebasedonraw  |                        |                  | canincrease   | includingatmospheric   |
|     |                 | cloudtemporal          | RNN,             |               |                        |
[78] ReBwurm 2020 andpreprocessed classification correction,temporal
|     |     | observations,focusing | self-attention |     |     |
| --- | --- | --------------------- | -------------- | --- | --- |
Sentinel2satellite onvegetativeperiods, model performance selectionofcloud-free
|     | timeseriesdata |     |     | forallmodels | observations,cloud |
| --- | -------------- | --- | --- | ------------ | ------------------ |
andmaskingofcloud
masking,etc.
CNN,Stacked
Deployautomatic
|               |                   |                   | GRU,          | Mosteffective |                       |
| ------------- | ----------------- | ----------------- | ------------- | ------------- | --------------------- |
|               | Classifyingmental |                   |               |               | ICA-ADJUSTto          |
|               |                   | Independent       | Bidirectional | model         |                       |
|               | workloadlevels    |                   |               |               | removethefrequently   |
| [79] Kingphai | 2022              | componentanalysis | GRU,          | performance   |                       |
|               | fromEEGtime       |                   |               |               | contaminatedartifacts |
|               |                   | basedonADJUST     | BGRU-GRU,     | canbe         |                       |
|               | seriessignals     |                   |               |               | componentsbefore      |
|               |                   |                   | LSTM,BiLSTM,  | achieved      |                       |
|               |                   |                   | BiLSTM-LSTM   |               | applyingDLmodels      |
Developanew
|                |                     |                      | Multi-scale   | Achieved      |                    |
| -------------- | ------------------- | -------------------- | ------------- | ------------- | ------------------ |
|                | Anomalydetection    |                      |               |               | ERR-basedthreshold |
|                |                     | Multi-scaleattribute | convolutional | superior      |                    |
| [80] Yokkampon | 2022 ofmultivariate |                      |               |               | settingstrategyto  |
|                |                     | matrices             | variational   | performance   |                    |
|                | sensortimeseries    |                      |               |               | optimizeanomaly    |
|                |                     |                      | autoencoder   | androbustness |                    |
detectionperformance
|          |     |                       | LSTM,         |             | ApplyPearson         |
| -------- | --- | --------------------- | ------------- | ----------- | -------------------- |
|          |     | Correlationmatrixwith |               | Retainedthe |                      |
| Barrera- |     |                       | Stacked-LSTM, |             | correlationmatricfor |
[58] 2022 Rainfallprediction thePearsoncorrelation mainfeatures
| Animas |     |                     | Bidirectional  |               | unsupervisedfeature  |
| ------ | --- | ------------------- | -------------- | ------------- | -------------------- |
|        |     | coefficient         | LSTM           | ofDLmodels    | selection            |
|        |     | Discretewavelet     |                | Performedbest | Proposea             |
|        |     | transformation,fast | Attention,DCN, | forattention  | preprocessingmodelof |
[81] Mishra 2020 Windpredictions Fourier DFF,RNN, andDCNwith discretewavelet
|     |                | Transformation,inverse | LSTM | waveletorFFT | transformationandfast |
| --- | -------------- | ---------------------- | ---- | ------------ | --------------------- |
|     |                | transformation         |      | signal       | Fouriertransformation |
|     | Timeseriesdata |                        |      |              | Proposetransformation |
|     |                | Iterative              |      | Considerably |                       |
fromenergy methodfor
|     |     | transformationsand | LSTM, | improvedthe |     |
| --- | --- | ------------------ | ----- | ----------- | --- |
[10] Livieris 2020 section,stock Augmented CNN-LSTM DLforecasting enforcementof
market,and stationarityofthetime
|     |                | Dickey–Fullertest |     | performance |        |
| --- | -------------- | ----------------- | --- | ----------- | ------ |
|     | cryptocurrency |                   |     |             | series |
Deploytimeseries
decompositionmethod
|           | Trafficflow | Timeseries          | Convolution- | Outperformed |               |
| --------- | ----------- | ------------------- | ------------ | ------------ | ------------- |
| [1] Asadi | 2020        |                     |              |              | forseparating |
|           | timeseries  | decompositionmethod | LSTM         | SOAmodels    |               |
short-term,long-term,
andspatialpatterns

Sensors2023,23,7167 14of32
Table2.Cont.
|                  |                       | Preprocessing | DeepLearning |          |         |
| ---------------- | --------------------- | ------------- | ------------ | -------- | ------- |
| Ref. FirstAuthor | Year ApplicationField |               |              | Accuracy | Details |
|                  |                       | Methods       | Models       |          |         |
Dataaugmentation
methods(liketime
|     |              |                    |     | Show | Comparedata |
| --- | ------------ | ------------------ | --- | ---- | ----------- |
|     | Surveyofdata | domainandfrequency |     |      |             |
[82] Wen 2021 augmentation domain), Deepgenerative successesin augmentationmethods
|     |     |     | models | timeseries | forenhancingthe |
| --- | --- | --- | ------ | ---------- | --------------- |
methods decomposition-based
|     |     |     |     | tasks | qualityoftrainingdata |
| --- | --- | --- | --- | ----- | --------------------- |
methods,statistical
generativemodels
Achievethe
Developacompression
|           |                  | Discretewavelet   |             | optimal     |                      |
| --------- | ---------------- | ----------------- | ----------- | ----------- | -------------------- |
|           |                  |                   | Resnet,     |             | approachwithdiscrete |
|           | Wirelessnetwork  | transformandthe   |             | trade-off   |                      |
| [83] Azar | 2020             |                   | LSTM-FCN,   |             | wavelettransformand  |
|           | withsmartsensors | error-bound       |             | betweendata |                      |
|           |                  |                   | GRU-FCN,FCN |             | error-bound          |
|           |                  | compressorSqueeze |             | compression |                      |
|           |                  |                   |             | andquality  | compressor           |
KananiandPadole[75]presentedapreprocessingframeworkthatcanincreasethe
electrocardiogram(ECG)classificationaccuracyoftheDeepLearningmethodssignificantly,
withahigherthan99%accuracyrate. ECGtimeseriessignalsareveryefficientforthe
monitoring of cardiovascular health, with abnormal heartbeats detected from the ECG
patterns. ThelabeledMIT-BIHArrhythmiadataset,whichhasECGtimeseriessignalsof
fivedifferentclasses,wastested. Theproposedpreprocessingstepsincludethesqueezing
andstretchingofthesignalalongthetimeaxisandtheamplifyingandshrinkingoftheam-
plitudeofthesignal.Itisshownthatthesetransformationsdonotchangethecharacteristics
ofthesignalsandcanberegardedascompletelylosslesstransformationshere.
Kisa et al. [76] deployed an adaptive preprocessing method with empirical mode
decomposition(EMD)wasproposedtohandlethisnonstationarytimeseries,asthesur-
faceelectromyography(sEMG)timeseriesisnonstationaryandnonlinear. sEMGcanbe
employedtomeasuretheelectricalactivityofhumanmuscles. Therecognitionofhuman
movementsisusefulforapplicationslikehuman–computerinteraction(HCI).ThesEMG
handgesturetimeseriesdatawasobtainedwithasensordeviceofsurfacebipolarelec-
trodeswith30healthyvolunteers. EMDcanserveasanon-linearfiltertodecomposethe
inputtimeseriesintoseveralintrinsicmodefunctions(IMFs). TheoutputsoftheIMFs
werethenfedintotheDeepLearningmodelCNNbasedonResidualNetworks(ResNet)
forgestureclassification. ItisfoundthattheIMFscanimprovethevalidationaccuracyof
theoriginaltimeseriesfrom94.22%toamaximumof99.73%.
Zhengetal.[8]investigatedthesegmentationandtransformationmethodsfortheir
effectivenessindatapreprocessingforDeepLearningalgorithms. InHARtasks,segmen-
tationmethodsareessentialasrawinertialtimeseriescanhaveverylargefluctuations.
Five segmentation options of five different segment lengths were evaluated with four
transformationmethods,i.e.,rawplot,multichannel,spectrogram,andspectrogramwith
shallowfeatures. Theexperimentwasconductedwithdatasetsofeightdailyactivities
fromwearablesensors,carworkshopmaintenanceactivitydata,etc. Theresultsshowed
thattheclassificationaccuracyincreasesalongwithanincreaseinsegmentlength, and
themultichannelmethodcanperformthebestfortheHARtasks. Theoverallaccuracyis
97.2%,whichisbetterthanmanyothermachinelearningmodels.
CastroFilhoetal.[77]appliedatwo-stagenoiseschemeforpreprocessingSARtime
series,asthereareinevitablenoiseslikespecklesforSyntheticApertureRadar(SAR)images.
SAR sensors can be employed for mapping the rice-growing regions and constructing
continuoustimeseriesdata. TheSARdataisveryusefulformonitoringshortphenological
stagesandraisingtheclassificationcapacity. 3D-Gammafilterwasusedtoeliminatethe
speckle, and the method of Savitzky and Golay [84] was employed to smooth the time
series. TheprocessedtimeserieswasfedtotwoDeepLearningmethods,theLongShort-
TermMemorymodelandtheBidirectionalLSTMmodel,formappingricecropswithSAR
sensortimeseriesfromWestRioGrandedoSul(Brazil). Theresultswerecomparedwith

Sensors 2023, 23, x FOR PEER REVIEW 17 of 35
Sensors2023,23,7167 15of32
conventionalmachinelearningmodels,withBiLSTMshowingthebestperformanceinthe
McNemartest.
Figure 2. Tree diagram for grouping the popular preprocessing methods for sensor time series
classificationandforecastingtaskscoveredinthissurvey[1,8,10,58,75–83](note: ifapaperuses
twomethodsseparatelywithsimilarsatisfactoryresults,thepaperwillbelistedunderbothgroups).
ReBwurmandKorner[78]investigatedtheeffectivenessofDeepLearningmodels
for the classification of crop type based on raw and preprocessed Sentinel 2 satellite
time series data. With the advance of remote sensing technologies, the amount of the
Earthobservationtimeseriesdatahasbeengreatlyincreasingoverrecentyears. While
manytraditionalmodelsforremotesensingapplicationsrequirepreprocessingandfeature

Sensors2023,23,7167 16of32
extraction,ReBwurmandKorner[78]checkedifthecurrentDeepLearningmethodsare
abletoutilizetherawtimeseriesdatadirectlywithoutdatapreprocessing. Atmospheric
correction,filteringofcloudtemporalobservations,focusingonvegetativeperiods,and
maskingofclouds,whicharetypicalpreprocessingmethodsforsatellitetimeseries,have
been applied. Additionally, 1D-convolutions, recurrent neural networks (RNN), and
theself-attentionmodeloftheencoderarchitectureoftheTransformernetwork[85]are
deployedandevaluated. Theresultsshowthatself-attentionandRNNcanperformbetter
forrawdata,whilethepreprocessingprocesscanimprovetheresultsforallthreemethods
satisfactorily.
KingphaiandMoshfeghi[79]employedsevenDeepLearningmodels,i.e.,convolu-
tionalneuralnetwork(CNN),StackedGatedRecurrentUnit(SGRU),BidirectionalGRU
(BGRU),BGRU-GRU,LSTM),BidirectionalLSTM(BiLSTM),andBiLSTM-LSTM,forclas-
sifyingmentalworkload(MWL)levelsfromelectroencephalography(EEG)timeseries
signals. MWLcanleadtoabetterunderstandingofhumanperformanceincomplexenvi-
ronments. EEGtimeseriescanbeutilizedforclassifyingthementalworkloadlevelofa
humansubject. ThedatasetSTEWcontainssignalsfrom48subjectsintherestingandwork-
ingstates. PreprocessingisneededbecausethereisusuallynoiseintheEEGsignals. The
independentcomponentanalysisbasedonADJUST(ICA-ADJUST)byMognonetal.[86]
was found to be the most effective preprocessing tool for this dataset by Kingphai and
Moshfeghi[87]. KingphaiandMoshfeghi[79]extractedfourgroupsoffeatures(frequency
domain,timedomain,lineardomain,andnon-lineardomain)fortheDeepLearningmod-
els. The results showed that BiLSTM-LSTM performed best with 94.75% accuracy for
classifyingrestingvs. workingstates,whileBGRU-GRUwasbestforclassifyinglowvs.
moderatevs. highMWLlevelswith83.03%accuracy.
Yokkamponetal.[80]deployedmulti-scaleattributematricesasthepreprocessing
toolfortransformingthemultivariatetimeseriestodevelopamulti-scaleconvolutional
variationalautoencoderforunsupervisedanomalydetectionofmultivariatesensortime
seriesdatasets. Theattributematricescanutilizethepair-wiseinnerproductofthetime
seriesamongsegmentsandeffectivelycharacterizesystemstatesofthetimeseries. The
identificationofanomaliesisaboutdetectingdatapointsthatdeviatesignificantlyfrom
theirexpectedvalues. Therearethreetypesoftimeseriesanomalies: (1)pointanomalies,
which refer to outlier points; (2) contextual anomalies, which differ significantly from
typicalpointsofthesamecontext;and(3)collectiveanomalies,whichrefertotheexistence
ofasubsetoftimeseriesdatapointswithasignificantdifferencefromtheotherpointsin
thewholedataset[88]. Anomalydetectioncanbeemployedinmanyreal-worldcases,like
fraudulenttransactiondetection,sensornetworkfaultanalysis,andabnormalequipment
monitoring. The proposed model was tested with four publicly available benchmark
datasets: thetimeseriesdatabytheAustralianCentreforRemoteSensing,theWafertime
seriesdatasetofsemiconductormicroelectronicsfabrication,theEmotivEEGNeuroheadset
timeseriesdataset,andOpthandwritingdataset. Theexperimentalresultsshowthatthe
modelperformedbetterthanotherbaselinemethods.
IntheinvestigationbyBarrera-Animasetal.[58],beforefeedingthetimeseriesdata
intotheDLmodels,thefeatureselectionprocesswasachievedwiththecorrelationmatrix
(CM),whichiscomputedwiththePearsoncorrelationcoefficientforthe43-dimensional
datasets. Rainfall prediction is complicated because of its nonlinear characters. Spa-
tialinformationlikelatitudeandlongitudeandatmosphericinformationlikehumidity,
pressure,temperature,andwindspeedmaybeutilizedfortheforecastingmodels. Barrera-
Animasetal. investigatedtheeffectivenessofDeepLearningmodels,includingLSTM,
Stacked-LSTM, and Bidirectional LSTM, with the conventional machine learning (ML)
modelXGBoost,andalsoautomatedmachinelearning(AutoML)withtheTPOTtool[89],
whichcanberegardedhereasanensembleofMLmodels. OpenWeatherdataoffiveUK
citiesfrom2000to2020wereevaluated. Highlycorrelatedfeatureswillbeeliminated. The
experimentalresultshighlightedthattheStacked-LSTMwithtwohiddenlayersandthe
BidirectionalLSTMcouldobtainthebestperformanceinrainfallforecasting.

Sensors2023,23,7167 17of32
Mishraetal.[81](2020)evaluatedthewindpredictionswithfiveDeepLearningmeth-
odsagainstthreedatapreprocessingtools. Thefivemethodsaretheattentionmechanism
(Attention)ofsequence-to-sequenceencoder–decoderarchitecture[90],deepconvolutional
network(DCN),deepfeedForward(DFF),recurrentneuralnetwork(RNN),andLSTM.
Thedatasetisthetimeseriesofthetemperatureandwindpowervariable. Discretewavelet
transformationandfastFouriertransformation(FFT)areemployedtotransformthetime
seriesdatasetbeforefeedingtotheDeepLearningmodels,whileinversetransformation
wasappliedtotheDLmodeloutputsbeforemakingpredictions. Theexperimentalresults
showedthatAttentionandDCNworkthebestwithwaveletandFFT,whilesomeother
modelsworkbetterwithnoneedfordatapreprocessing.
Livieris et al. [10] proposed a preprocessing framework to further improve the ef-
ficiency and reliability of the Deep Learning methods. Iterative transformations and
augmentedDickey–Fullertestwereappliedtothetimeseriesdataforobtainingstationary
processed time series data before feeding to the Deep Learning model. The Ljung–Box
Qtestwasemployedtochecktheautocorrelationofthemodel’serrors. Timeseriesdata
fromenergysection,stockmarket,andcryptocurrencyweretested,andtheexperimental
resultsshowedthattheproposedpreprocessingframeworkcouldenhancetheefficiency,
accuracy,andreliabilityoftheDeepLearningLSTMandCNN-LSTMmodelsconsiderably.
Livierisetal.[91]continuedtheirworkontheinvestigationofthepreprocessingframe-
workforDeepLearningmodels. Ontopoftheirpreviousfocusonthetransformationof
non-stationarytimeseriestostationarybydifferencingthetimeseries,therawtimeseries
isnowsubjectfirstlysubjecttotheexponentialsmoothingmethod,whichcantransform
therawdatatoade-noisedversion. Thisprocessistoincreasethequalityofthetimeseries
dataandthusimprovethepredictioncapabilityoftheDeepLearningmodelCNN-LSTM.
Theexperimentalresultswithcryptocurrency,energy,andstockmarketsconfirmedthatthe
preprocessingframeworkcouldsignificantlyachieveitsobjectiveoffurtherimprovement
fortheDeepLearningmodels.
AsadiandRegan[1]employedthetimeseriesdecompositionmethodtoobtainthe
short-term, long-term, and spatial patterns in the proposed preprocessing framework.
Theshort-termpatternsofthespatialtimeserieswereexploredwiththefuzzyclustering
method,whichcangroupneighboringtimeseriestogetheraccordingtothechecksonthe
residualsofthetimeseries. Theseresidualsinspatialtimeseriescanprovidemeaningful
patternswithneighboringlocations,likeshowinghowthetrafficisevolvingintheroad
network. Thetrafficflowtimeseriesdatasetwastested,andthemethodcanobtainbetter
resultsthanboththebaselineandstate-of-the-artmethods.
Wenetal.[82]presentedasurveyofthedataaugmentationmethodsthatarespecif-
icallydesignedforhandlingtimeseriesdatasets. Becausemanyreal-worldapplications
likemedicaltimeseriesoranomalydetectiontimeseriesfacetheproblemofnothaving
enoughlabeleddata,itcanbeveryhelpfultohaveaneffectivewaythatcanenlargethe
sizeandimprovethequalityofthetrainingdataduringdeployingDeepLearningontime
seriesdatasets. Dataaugmentationhasbeenfoundverysuitableforthistask, asitcan
generatedatasyntheticallyforunexploredinputspacewithcorrectlabels. Notonlybasic
dataaugmentationmethods,liketimedomainandfrequencydomain,butalsoadvanced
methods,likedecomposition-basedmethods,statisticalgenerativemodels,anddeepgen-
erativemodels,arecoveredinthesurveybyWenetal. Theseaugmentationmethodsare
foundtobeeffectiveintimeseriesclassification,timeseriesanomalydetection,andtime
seriesforecasting.
Azaretal.[83]developedacompressionmoduleforbothunivariateandmultivari-
atetimeseriesdatawiththediscretewavelettransformandtheerror-boundcompressor
Squeeze(SZ).On-boardprocessingandcompressionalgorithmscanreducetheproblems
associatedwiththetransmissionoflargedatavolumesinapplicationsoftheInternetof
Things(IoT).Thispreprocessingprocedureisespeciallyimportantforthesensorsystems
inIoT,astheymayonlyhaveverylimitedbandwidth,memory,andcomputationalpower.
TheprocessedtimeseriesdataisthensenttotheDeepLearningmodels(Resnet,LSTM-

Sensors2023,23,7167 18of32
FCN,GRU-FCN,FCN)fortimeseriesclassification. TheFullyConvolutionalNetwork
(FCN)deployedhereconsistsofaconvolutionallayerwithfilters,abatchnormalization
layer,andthenaReLUactivationlayer. Theexperimentwasconductedwithtimeseries
datasets(UCR,UCI,andUEA)fromsensorsofECG,motion,etc. Theresultssupported
thatthecompressionapproachcanachieveahighcompressionratio,whileitstimeseries
denoisingcapabilityenablestheDeepLearningmoduletoachievesatisfactoryclassifica-
tionaccuracy.
3. AdvancesinContinualLearningMethodsforTimeSeriesModeling
In the previous section, applications of Deep Learning models and preprocessing
methodsindifferentreal-worldtimeseriesscenarioshavebeenreviewed. Limitationsof
DeepLearningmodelsincludeastrictstaticrequirementfortheunderlyingprocess[92].
Post-deploymentchangesarenotuncommonintherealworld,buttheDLmethodsare
usuallyoffixednetworkstructureafterbeingdeployed.WhenDLmodelsarefedwithdata
notfollowingtheindependentandidenticallydistributed(i.i.d.) assumption,destructive
interferencemayoccurandcauseperformancedegradation[93].Continuallearningmaybe
deployedtoaddressthesedifficultiesfacedbyDLmodelsinsuchawaythatDeepLearning
models may benefit from continual learning to become capable of learning continually
withadaptability.
Amajorcharacteristicofcontinuallearningisitssequentiallearningprocess. Ateach
time,onlyasmallamountoftheinputdataisavailable.OthernamesforCLincludelifelong
learning, sequential learning, and incremental learning. Mathematically, the continual
learningforbothclassificationandtimeseriesregressionproblemscanbeexpressedas
follows[94]: LetT = (T ,...,T )representthemtasksthatarriveinsequence. Fortask
1 m
T(i =1,2,...,m),thereexistNinstancesoflabeledtimeseriesdataD = {(x ,y )}N .
i i i,r i,r r=1
Here, time series x ∈ X is associated with the corresponding target y ∈ Y. For
i,r i i,r i
classificationtasks,thetargetspaceY referstoclasslabels. Fortimeseriesregressiontasks,
i
the target spaceY refers to real numbers. A constraint of continual learning is that for
i
any task T, there exists no access to the data of previous tasks T(j =1,...,i−1). The
i j
common goal of each task is to learn a solver model M, such that M : X →Y , with
i i i i
trainableparametersθ andestimatedtargetyˆ = M(x ;θ ). LetL(y ,yˆ ;θ )represent
i i,r i i,r i i,r i,r i
thetrainingobjectives. Forclassificationproblems,thiscanbethestandardcross-entropy
loss,whilefortimeseriesregressionproblems,thiscanbethesquared-errorloss. Then,
q ∑ N (cid:18) 1−q (cid:19)i ∑ −1 ∑ N (cid:0) (cid:0) (cid:1) (cid:1)
L = L(y ,yˆ ;θ )+ L y ,M xˆ ;θ ;θ
i N i,r i,r i (i−1)N j,r i j,r i i
r=1 j=1r=1
whereNreferstothenumberofinstances,and0< q ≤1referstotheimportanceassigned
todatafromT.
i
There are several popular CL scenarios, like Instance-Incremental Learning (IIL),
Domain-IncrementalLearning(DIL),Task-IncrementalLearning(TIL),Class-Incremental
Learning (CIL), Task-Free Continual Learning (TFCL), and Online Continual Learning
(OCL).Thistaxonomyisbasedonhowtheincrementalbatchesaredividedandwhich
taskidentifiesareavailable[18]. IILreferstoscenarioswherealltrainingsamplesarrivein
batchesandbelongtothesametask. DILreferstoscenarioswheretaskidentitiesarenot
needed;taskshavedifferentinputdistributionsbutthesamedatalabelspace. TILrefersto
scenarioswheretaskidentitiesareavailableduringbothtrainingandtesting,andtasks
havedisjointdatalabelspaces. CILreferstoscenarioswheretaskidentitiesareavailable
onlyduringtrainingandtaskshavedisjointdatalabelspaces. TFCLreferstoscenarios
wherenotaskidentityisavailableandtaskshavedisjointdatalabelspaces. OCLrefersto
scenarioswheretrainingsamplesforeachtaskarrivefromthedatastreamonebyone,and
taskshavedisjointdatalabelspaces.
Fleschetal.[95]highlightedthatforhumancontinuallearning,theextensiveback-
groundstatisticalknowledgegainedfrompreviousunsupervisedtrainingmightbeutilized

Sensors2023,23,7167 19of32
forrulelearningatlaterstages,thoughwithseveralconditions,whileDNNsufferscatas-
trophicforgetting(CF)problems. CFcanbeviewedasanissuestemmingfromtheNN
stability–plasticitydilemma,andtheCFeffectisassociatedwiththeabruptlossofprevi-
ouslylearnedknowledge[17]. PlasticityreferstotheNN’sabilitytolearnnewknowledge,
whilestabilitymeansthestoringoflearnedknowledge. CLcanbeemployedinsupervised
learning,semi-supervisedlearning,unsupervisedlearning,andreinforcementlearningas
well. Shaheenetal.[96]discussedtheapplicationsofcontinuallearningforautonomous
systems. Thereal-worldsystemsofvehicleswithself-drivingcapability,unmannedaerial
vehicles,andautonomousroboticswerehighlighted.
VariousdegreesofconstraintsimplificationforsolvingtheCFissueareimposedin
thecurrentmethods. Thereareconstraintssuchasmemory,computationalpower,and
dataprivacy. Nevertheless,thereareissueswhenapplyingthesemethods,forexample,
toorigidconstraintsthatmaybreaktheideaoflearningcontinuallyortootailor-made
forsolvingaparticulartypeofproblemonly. PfulbandGepperth[97]investigatedthe
CFproblemsinDNNwithaverylargenumberofdatasetsinvisualclassification. The
large-scaleexperimentsshowthatnomodelanddatasetisfreeoftheCFproblems,whilst
a few potential workarounds may enable a few models to become practicable in a few
application-levelenvironments. Inspiredbyopen-setrecognition,Prabhuetal.[98]pre-
sentedamodelcalledGDumb,whichisnottailor-madeforCLtasks. GDumbstartswith
storingsamplesgreedilyinmemoryastheyarrive,andduringtesting,itproceedswithnew
modeltrainingwithsamplesonlyinthememory.GDumbisshowntooutperformmanyCL
approachesandmayserveasanalerttothecurrentprogressinCLforclassification,with
theoversimplificationsbysomeexistingCLapproachestotheproblemsresultinginlittle
real-worldapplicationvalue. InthedeepautoencoderNNfortimeseriesforecasting[99],
buffers were deployed with online elastic weight consolidation to learn the probability
distributionofthedatastreamsequentially. ACLmodelwithexplicitmemorystructure
wasusedtoaddressCFintheirFFNNmodelformakinglong-termfinancialinvestment
decisions[100].Chenetal.[101]employedgraphneuralnetworkswithCLstrategies—data
replayandparametersmoothing—fortransferringlearnedknowledgetothecurrentmodel
intheirtrafficflowforecastingframework.
TherelationshipbetweenneuralnetworkarchitecturesandCFwasinvestigated,and
itwasfoundthatthenetworkwidthhasasignificanteffectonforgetting. Nevertheless,
whenincreasingthewidthtoaddressCF,inefficiencyproblemslikelongcomputationtime
andlargeenergywasteinevitablyappear. Langeetal.[17]investigatedmodelcapacity,
weightdecay,dropoutregularization,andthestability–plasticitytrade-offamongcontinual
learners. Lesortetal.[102]investigatedtheeffectsoftheparameterizationsoftheDNN
outputlayeronlearningandforgettinginCL.Theevaluationisconductedinasimplified
learningenvironment,decomposingthemodelasaclassifierpartfortheoutputlayerand
afeatureextractorpartfortherestoftheDNN.Weightsmodifications,interference,and
projection drift can be the causes of CF in the output layer. More knowledge is gained
about the continual learning in output layers. Instead of focusing solely on continual
learning,Mundtetal.[103]presentedaframeworkcombiningconceptsfromCL,open
set recognition, and active learning. This holistic approach shows promising results in
addressingcatastrophicforgettingandrobustnessforopen-worldapplications.
Current limitations for CL applications include the predominant closed-world as-
sumptionwhendeployingmodels, whichrequiresthatanynewdatafollowsthesame
distributionasthoseusedduringtraining. Whenthisclosed-worldassumptionisnolonger
valid,theneuralnetworksmaygivefalsepredictionswithunknownsituationsorwith
corrupteddata[103]. AnotherlimitationisthatmanycurrentworksinCLmaynotoften
considerthescalabilityissueinpotentialapplications,whichmayhaveaverylargenumber
ofsub-tasksand,consequently,hugeamountsofsamples.
WhilstmostoftherecentworksonCLfocusonsupervisedtasks,theover-specializing
ofCLtrainingforasinglesetofenvironmentslimitsCLgeneralizationtoothertypesof
applications[104]. WithmostrecentresearchfocusingontheCLapplicationsforclassifica-

Sensors2023,23,7167 20of32
tiontasks,thislackofattentionmayhindertimeseriesapplicationslikerenewableenergy
forecastingwithCLmodels[99]. DeepLearningmethodswithouttheabilitytoremember
oldknowledgemaynothandlewellinreal-worldapplicationsoftimeseriesforecasting
withnon-stationarysequentialdata[105]. Ontheotherhand,thecurrentCLprojectson
differenttimeseriesregressiontasksareshowingencouragingresults. Phametal.[105]
designed a fast and slow learning network for online time series forecasting, with the
per-layeradapterforfastlearningandassociativememoryforrememberingandrecalling
repeatingpastevents. CLmaybeveryusefulforaddressingfinancialtimeseriesproblems,
whichcanappeareverywhereandarecommonlynon-stationary[100],andfortrafficflow
timeseriesforecasting,whichisessentialforsmarttransportation. Mostcurrentmethodsof
trafficflowforecastingassumestaticnetworks[101]. Yet,real-worldtrafficflownetworks
changeconstantly,likepossiblenetworkmodificationandtheadditionofnewparts[106].
Aftertheabovediscussionillustratestheimportanceofcontinuallearningamongthe
DeepLearningtimeseriesapplications,asyntheticsummaryoftheadvancesincontinual
learning techniques for time series applications is presented in Table 3, followed by a
detaileddescriptionofthecorrespondingmethods,motivations,accuracy,andbriefdetails.
ThefollowingFigure3showsthetreediagramofthetaxonomyofthecontinuallearning
methodsforsensortimeseriesclassificationandforecasting.
Table3.Summaryoftheadvancesincontinuallearningtechniquesfortimeseriesapplications.
|                  | Application | Motivationsfor | ContinualLearning |          |         |
| ---------------- | ----------- | -------------- | ----------------- | -------- | ------- |
| Ref. FirstAuthor | Year        |                |                   | Accuracy | Details |
|                  | Field       | DeployingCL    | Models            |          |         |
Addressingthe
|     | Wearablesensors | catastrophicforgetting |                | Stillneed      | CompareCL |
| --- | --------------- | ---------------------- | -------------- | -------------- | --------- |
|     |                 |                        | A-GEM,ER-Ring, | improvementfor |           |
[107] Sah 2022 foractivity inthenon-stationary approachesforsensor
|     |             |                    | MC-SGD | multitask |         |
| --- | ----------- | ------------------ | ------ | --------- | ------- |
|     | recognition | sequentiallearning |        |           | systems |
training
process
|     | Humanstate |     | Replay,elasticweight | Existing |     |
| --- | ---------- | --- | -------------------- | -------- | --- |
Assesstheabilityof
|     | monitoringof | Overcomingthe | consolidation, | strategies |     |
| --- | ------------ | ------------- | -------------- | ---------- | --- |
existingCLmethods
[108] Matteoni 2022 domain- non-stationary learningwithout struggleto
forknowledge
|     | incremental | environments | forgetting,naiveand | accumulate |     |
| --- | ----------- | ------------ | ------------------- | ---------- | --- |
accumulationovertime
|     | scenario |     | cumulativestrategies | knowledge |     |
| --- | -------- | --- | -------------------- | --------- | --- |
Multipleclinics
|     | withvarious |     | Bufferstrategyto |     | Apply |
| --- | ----------- | --- | ---------------- | --- | ----- |
Temporaldatainclinics
|               | sensorsfor |          | constructthe      | Outperform | uncertainty-based     |
| ------------- | ---------- | -------- | ----------------- | ---------- | --------------------- |
| [93] Kiyasseh | 2021       | areoften |                   |            |                       |
|               | cardiac    |          | continuallearning | GEMandMIR  | acquisitionfunctions, |
non-stationary
|     | arrhythmia |     | modelCLOPS |     | forinstance,replay |
| --- | ---------- | --- | ---------- | --- | ------------------ |
classification
Comparethreemain
|     | Deploymentin | Addressingthe         |               |                |                 |
| --- | ------------ | --------------------- | ------------- | -------------- | --------------- |
|     |              |                       | CLapproaches- | Bestresultsfor | CLapproachesfor |
|     | mobileand    | resourcesrequirements |               |                |                 |
[109] Kwon 2021 embedded andlimitationsofthe regularization,replay replaywith mobileandembedded
|     |         |                   | andreplaywith | exemplars | sensingapplications |
| --- | ------- | ----------------- | ------------- | --------- | ------------------- |
|     | sensing | mobileandembedded |               |           |                     |
|     |         |                   | examples      | schemes   | likeactivity        |
|     | devices | sensingdevices    |               |           |                     |
recognition
EvaluateCL
|     |     |     |     | Highlightthe | approachesin |
| --- | --- | --- | --- | ------------ | ------------ |
Achievingwalk
Sensorsofthe Continuallearningin importanceofa class-incremental
| [110] Cossu | 2021           | learningindifferent |      |       |                    |
| ----------- | -------------- | ------------------- | ---- | ----- | ------------------ |
|             | roboticssystem |                     | RNNs | clear | scenariosforspeech |
environments
|     |     |     |     | specification | recognitionand |
| --- | --- | --- | --- | ------------- | -------------- |
sequenceclassification
Explainability
|          |                  |                     | modulebasedon      |                 | Proposetheconceptual   |
| -------- | ---------------- | ------------------- | ------------------ | --------------- | ---------------------- |
|          |                  | Addressingthelackof |                    | Proposed        |                        |
|          | Identificationof |                     | dimensionreduction |                 | designofexplainability |
| [111] He | 2022             | transparencyforCL   |                    | evaluationscore |                        |
|          | anomalies        |                     | methodsand         |                 | moduleforCL            |
|          |                  | modules             |                    | basedonmetric   |                        |
|          |                  |                     | visualization      |                 | techniques             |
methods

Sensors2023,23,7167 21of32
Table3.Cont.
|                  | Application | Motivationsfor | ContinualLearning |          |         |
| ---------------- | ----------- | -------------- | ----------------- | -------- | ------- |
| Ref. FirstAuthor | Year        |                |                   | Accuracy | Details |
|                  | Field       | DeployingCL    | Models            |          |         |
Developatwo-stage
Incrementalupdating
|     |              | Overcoming |             | Outperform | CLapproachwith |
| --- | ------------ | ---------- | ----------- | ---------- | -------------- |
|     | Videoanomaly |            | ofthememory |            |                |
[112] Doshi 2022 practicalVAD existingmethods featureembeddingand
|     | detection(VAD) | challenges | module, | significantly | kNN-basedRNN |
| --- | -------------- | ---------- | ------- | ------------- | ------------ |
experiencereplay
model
CompareCL
|     | Metal-forming | Providingautomatic    |                   |          |                |
| --- | ------------- | --------------------- | ----------------- | -------- | -------------- |
|     |               |                       | Continuallearning |          | approachesof   |
|     | timeseries    | capabilityforadapting |                   | Improved |                |
|     |               |                       | approachbasedon   |          | regularization |
[113] Maschler 2021 datasetofa formerlylearned performancevs.
|     |               |                | regularization |                  | strategiesonindustrial |
| --- | ------------- | -------------- | -------------- | ---------------- | ---------------------- |
|     | discrete      | knowledgetonew |                | noregularization |                        |
|     |               |                | strategies     |                  | metal-formingdatafor   |
|     | manufacturing | settings       |                |                  |                        |
faultprediction
Real-worldrestrictions
likeindustrial
|     |                 |                   |                   | Promisingresults | Applyelasticweight |
| --- | --------------- | ----------------- | ----------------- | ---------------- | ------------------ |
|     | Faultprediction | espionageandlegal | LSTMalgorithmwith |                  |                    |
|     |                 |                   |                   | forindustrial    | consolidationfor   |
[114] Maschler 2020 inadistributed privacyconcern elasticweight
|     |             |                        |               | automation | distributed,        |
| --- | ----------- | ---------------------- | ------------- | ---------- | ------------------- |
|     | environment | preventthecentralizing | consolidation |            |                     |
|     |             |                        |               | scenarios  | cooperativelearning |
ofdatafromfactories
fortheDLtraining
Developan
|     |     | Addressinghigh-value | Continuallearning |     |     |
| --- | --- | -------------------- | ----------------- | --- | --- |
HMM-basedCL
|     | Auditoryscene | backgroundnoiseand | approachbasedon | Achievehigh |     |
| --- | ------------- | ------------------ | --------------- | ----------- | --- |
[115] Bayram 2020 analysis highcomputational HiddenMarkov accuracy approachwithUED
andretrainingfortime
|     |     | demands | Model |     |     |
| --- | --- | ------- | ----- | --- | --- |
seriesclassification
Prioritized
|            |                  |                    |                     | Ableto          | Formulatethetraffic   |
| ---------- | ---------------- | ------------------ | ------------------- | --------------- | --------------------- |
|            | Evolving         | Addressingthe      | experiencereplay    |                 |                       |
|            |                  |                    |                     | continuously    | flowprediction        |
|            | long-term        | non-stationarydata | strategyfor         |                 |                       |
| [106] Xiao | 2022             |                    |                     | learnandpredict | problemascontinuous   |
|            | streamingtraffic | distributionduring | transferringlearned |                 |                       |
|            |                  |                    |                     | trafficflowover | reinforcementlearning |
|            | flow             | policyevolution    | knowledge           |                 |                       |
|            |                  |                    |                     | time            | task                  |
intothemodel
Transferringthe
|                 |                    |                        | Continuallearning | Outperform    |                    |
| --------------- | ------------------ | ---------------------- | ----------------- | ------------- | ------------------ |
|                 | knowledge          | Addressingproblems     |                   |               | PresentaCLapproach |
|                 |                    |                        | RNNmodelwith      | standard      |                    |
|                 | gainedfromthe      | liketherequirementof   |                   |               | ofanepisodicmemory |
| [116] Schillaci | 2021               |                        | episodicmemory    | memory        |                    |
|                 | greenhouse         | large-scalere-training |                   |               | systemandmemory    |
|                 |                    |                        | replayand         | consolidation |                    |
|                 | researchfacilities | inthenewfacility       |                   |               | consolidation      |
|                 |                    |                        | consolidation     | approaches    |                    |
togreenhouses
|     | In-process | Addressingthelackof |     | Possible | Deploytask-specific |
| --- | ---------- | ------------------- | --- | -------- | ------------------- |
Generator-based
|            | quality | practicalvariability |              | significant | generativemodelsto |
| ---------- | ------- | -------------------- | ------------ | ----------- | ------------------ |
| [94] Gupta | 2021    |                      | RNNcontinual |             |                    |
predictionby amongindustrial performance augmentdatafortarget
manufacturers sensornetworks learningmodule enhancement tasks
As it is NP-Hard to find the optimal CL algorithms which can completely avoid
catastrophicforgetting[117],polynomialtimeheuristicalgorithmshavebeenproposedto
addresstheCFproblems. TheseCLalgorithmscanbeclassifiedintothreefamilies,i.e.,
regularization-basedmethods,replaymethods,andparameterisolationmethods,accord-
ingtothestorageandusagemethodfortask-specificinformationduringthesequential
learningprocess[17]. Combinedapproachesrefertothemixingofthemethodstogether,
andoutstandingresultscanbeobtainedonbenchmarkdatasets[103]. Anotherpossible
taxonomyisofregularization-basedapproach,replay-basedapproach,optimization-based
approach, representation-based approach, and architecture-based approach [18]. This
surveywillfollowthetaxonomyofLangeetal.[17]andMundtetal.[103].

Sensors 2023, 23, x FOR PEER REVIEW 25 of 35
Sensors2023,23,7167 22of32
Figure3. Treediagramofthetaxonomyofthecontinuallearningmethodsforsensortimeseries
classificationandforecasting[93,94,106–116](note: ifapaperusestwomethodsseparatelywith
similarsatisfactoryresults,thepaperwillbelistedunderbothgroups).

Sensors2023,23,7167 23of32
3.1. Regularization-BasedMethods
Regularization-basedmethodsneedtoutilizeanextraregularizationtermintheloss
function for combining previous knowledge during the learning process of new data.
Regularizationmethodsfocusedonhowtopreservepreviousknowledge. Extralossterms
canbedeployedtopreservetheimportantweightsgainedfromthelearningofformer
tasks. Elasticweightconsolidation(EWC)[118],learningwithoutforgetting(LWF)[119],
andknowledgedistillation[120]arepopularregularizationapproaches.
Sah et al. [107] investigated the performance of three recent continual learning ap-
proaches(A-GEM[121],ER-Ring[122],andMC-SGD[123])foraddressingthecatastrophic
forgetting in wearable sensors for activity recognition. In a wearable sensor system, it
isnecessarytohavethecapabilitytomonitorandrecognizeactivitiesacrossusers. This
sequentiallearningprocessisnon-stationaryandchallengingforDeepLearningmethods.
ThePAMAP2dataset[124]ofhumanactivityrecognition,consistingofsensortimeseries
dataofeightsubjectsandtwelvedailyactivities,isusedfortheevaluation. Theresults
showedthatMC-SGDperformedthebestbyreducingnearly29%oftheforgetting,while
itscomputationaltimeisstillmuchlessthanthejoint-tasktrainingtime.
Matteonietal.[108]developedtwobenchmarksofhumanstatemonitoringofdomain-
incrementalscenariosforCLmodels. Innon-stationaryenvironments,recurrentneural
networksfortimeseriesdatacanbeoflargeimportance[110], andinvestigationofthe
networkpropertiesinthesesituationsmayleadtoabetterunderstandingandapplications
ofCLmodels. AsignificantobstaclethathindersthedevelopmentofCLmodelsisthe
shortageofenoughstandardbenchmarksoftimeseriesdatasetsfortheevaluationofthe
CLmodels. ThetwobenchmarkswerederivedfromdatasetsWESAD[125]andASCER-
TAIN [126] of time series classification from physiological sequence data. Different CL
modelswereinvestigatedwiththesetwobenchmarkstounderstandtheeffectsofcatas-
trophicforgettingonrecurrentneuralnetworks. FourcommonCLmodels,i.e.,replay[20],
elastic weight consolidation (EWC) [118], learning without forgetting (LwF) [119], and
naiveandcumulativestrategies,weretested. TheresultsshowedthatalltheCLmodelscan
mitigateforgetting,butbesidesthereplaymodel,allothermodelsstillcannotaccumulate
knowledgeovertime.
Kwonetal.[109]comprehensivelyinvestigatedtheperformanceofthreeCLapproaches
—regularization,replay,andreplaywithexamplesfordeploymentinmobileandembedded
sensing devices. Most of the existing continual learning methods do not consider the
resource requirements and limitations of mobile and embedded sensing devices [127].
Threedatasetsofhumanactivityrecognition,twodatasetsofgesturerecognition,andone
datasetofemotionrecognitionwereinvestigatedtofindthetrade-offsbetweensystem
performance,storagerequirements,computationalpowerrequirements,andpeakmemory
requirements among the CL approaches. The results showed that the CL approach of
replyingwithexemplarsworksbestafterconsideringallthetrade-offs.
Maschler et al. [113] evaluated the performance of a continual learning approach
basedonregularizationstrategies,whichmimicthehumanbrainsynapticconsolidation,
forindustrialapplication. Existingmethodsforanomalydetectionoftenlacktheflexibility
toadapttochangesinthemanufacturingprocesses[113], whilecontinuallearningcan
help overcome this issue by providing the automatic capability for adapting formerly
learned knowledge to new settings. Real-world metal-forming time series dataset of a
discretemanufacturingprocesswastested,showingpromisingresultsfortheregularization
strategiesoverthemultilayerLSTMapproachwithnoregularization. Onlineelasticweight
consolidationisfoundtoprovidebetterperformancethanelasticweightconsolidation.
Maschler et al. [128] evaluated the performance of the regularization strategies against
theopen-accesslithium-ionbatterydegradationdataset[129]withtheLSTMapproach
for remaining useful lifetime prediction for lithium-ion batteries. The results of these
degradationdatasetsreinforcethefindingsforthediscretemanufacturingprocess.Network
monitoringcanproduceahugeamountofmultivariatetimeseriesdatathatareuseful
forusage,likenetworkanomalydetection. Gonzalezetal.[130]outlinedtheirconceptual

Sensors2023,23,7167 24of32
frameworkofvariationalautoencodersanddilatedconvolutionalnetworksfornetwork
anomalydetection. Thedeepgenerativereplayisexploredforextendingthecontinual
learning capability to the proposed system. The teacher generative model can create
syntheticdatatoimitateprevioustrainingexamples, whilethenewstudentmodelcan
learnfromcurrentnewdataandalsothesesyntheticdataatthesametime. Thiscontinual
learningmodulemayhelptoaddresscatastrophicforgetting.
Maschleretal.[114]proposedanLSTMalgorithmwithelasticweightconsolidationfor
faultpredictioninadistributedenvironment. Continuallearninghasthepotentialtoserve
asadistributedapproachforfulfillingtheindustrialautomationneed,withDeepLearning
performingfaultpredictionforindustrialautomation. Thisisbecausemanyreal-world
restrictionslikeindustrialespionageandlegalprivacyconcernpreventthecentralizingof
datafromfactoriesforthetrainingoftheDeepLearningmodels. NASAturbofanengine
dataset[131]wasusedforperformanceevaluation. Theexperimentalresultsshowedthat
theirapproachcouldperformeffectivelywithdistributeddatasetswithnorequirementfor
centralizeddatastorage,satisfyingtherequirementsofmanyreal-worldmanufacturers.
Schillacietal.[116]developedacontinuallearningRNNmodelwithepisodicmemory
replayandconsolidationdrivenbypredictionerrorsfortransferringtheknowledgegained
fromthegreenhouseresearchfacilitiestoreal-worldgreenhouses.WithouttheCLcapability,
thisprocessmayotherwisebeexpensiveandriskyforthecropduetoproblemslikethe
requirementoflarge-scalere-traininginthenewfacility. Sensortimeseriesdatamayhelp
tobetterunderstandthecausalmodelsofadynamicsystem,andthisisveryusefulfor
real-worldapplications. Currently,popularcausaldiscoverymethodsutilizeonlystatic
dataorpre-processedtimeseriesdatainadvance,makingthemnotverysuitableforreal-
worldroboticscases. Continuallearningmayaddressthislimitationinthecausaldiscovery
methods [132] but is under-investigated for robot application [133]. Castri et al. [133]
focusedontheconstraint-basedmethodsforcausaldiscoveryandoutlinedtheirapproach
ofre-learningthecausalmodelduringobservedscenariochangesandduringanewsetof
interventions. Thenewinferencematricofthecausalmodelischeckedagainstthematric
oftheoldcausalmodeltodiscoverthestillvalidcausallinksfromtheoldmodelforthe
newmodel. Thisapproachofonlysmallincrementalchangescanhelptheroboticsystem
addresstheCFproblem. CLmodulecanalsohelptheroboticsystemaddressthehardware
resource limitation. Sensors in a greenhouse can produce time series data like climate
time series and leave temperature time series. A better understanding of the complex
greenhouse and modeling of these greenhouse time series data can help to predict the
effectsofinterventionbetter,thusincreasingthecropyield. Memoryretentionisbasedon
congruenceagainstpriorknowledgeretainedinthemodel,andtheexperimentalresults
showed that this memory replay strategy could enhance the performance of standard
memoryconsolidationapproaches.
3.2. ReplayMethods
Replaymethodsneedtostoreeithertherawsamplesorthegeneratedpseudo-samples
fromthegenerativealgorithm. Thesestoredprevioussamplescanbereplayedtoaddress
forgettingduringthelearningofnewtasks. Difficultiesforthisapproachmayincludethe
demandforresourcesoflargestoragecapabilityandtheprivacyconcernsforstoringand
deployingsamplesinreal-worldapplications. Pseudo-rehearsaltechniquescanhandle
thesedifficultieswithagenerativemodelinsteadofstoringpastsamplesdirectly.
Kiyassehetal.[93]utilizedthereplaybufferstrategytoconstructthecontinuallearning
modelCLOPSfromthetemporaldatainclinics,whichisoftennon-stationary,asmultiple
clinical sites with various sensors are involved. Acquisition based on uncertainty was
deployedforthereplayofbufferinstances.Fourclinicalenvironmentsinvolvingtransitions
betweendatamodalities,diseases,clinics,andtimearesuitablenon-stationaryscenarios
totesttheperformanceofthecontinuallearningapproach. TheresultsshowthatCLOPS
performsbetterinthreescenariosthanthetwootherfrontiermethods—GEM[134]and
MIR[135]. He[111]alsofocusedonthetarget-domainincrementalapplicationscenario

Sensors2023,23,7167 25of32
and data-domain incremental application scenario of continual learning and described
howtheirpreviousframework,CLeaR,canbeextendedtolearninputssuccessively. The
frameworkutilizesthestorageofbuffereddatabyanoveltydetector. Theapplicationof
continuallearningtotheregressionscenarioforpowerforecastingwasoutlined.
Doshi and Yilmaz [112] proposed a new continual learning approach for video
anomalydetection. SensorsandcamerasinCCTVsystemsaregeneratinghugeamountsof
real-timevideotemporaldata,anddatasizemaybetoobigtobeinvestigatedbyhumans.
Thereiscurrentlylimitedresearchonthecontinuallearningofthenewvideodata[112].
TheCLcapabilitywasachievedintwoways,bytheincrementalupdatingofthememory
moduleandbyexperiencereplay. Anew,morecomprehensivedatasetwascreated,con-
sistingoftrainingsegmentsinsplitsandtestsegmentstakenfromacamerainastreetin
NewOrleans,USA.Threeexistingbenchmarkdatasets,i.e.,UCSDPed2,CUHKAvenue,
andShanghaiTech,arealsoevaluated. Theexperimentalresultsshowthattheproposed
approachcanperformexcellentlyinovercomingpracticalVADchallenges.
Xiao et al. [106] have recently formulated the evolving long-term streaming traffic
flowproblemofsensortimeseriesdataasacontinuousreinforcementlearningtask. With
theadvancesinDeepQ-Networks(DQNs),whichenablethelearningofcomplicatedrein-
forcementtasks,theresearchonreinforcementlearning(RL)hasgrownenormously[136].
AgentsinDeepRLhaveshownoutstandingperformanceinsettingswithnarrowtasks,
butRLagentsfaceproblemsliketheover-fittingtendencyandthelackofgeneralization
capability to new variations [137]. This is in sharp contrast with the human ability to
learn continually and be adaptive to new scenarios over a lifetime, which is called CL.
DQNs face CF problems [118]. With the policy evolution leading to the non-stationary
data distribution, the CL concept can be applied in RL [104]. In this way, CL methods
maybeusedtoaddresstheCF,andsolvingthisissueiscrucialiftheartificialagentsare
going to have the capability to learn continuously [138]. The continual learner has the
advantageofadaptingandrecoveringefficientlytochangesencounteredovertime[29].
Here,thenextflowvaluepredictoristheagent,thenexttimeseriesflowvalueinthesensor
istheagent,andthedynamicalsensorandtransportationnetworkistheenvironmentstate.
Thegoalistoteachtheautonomousagenttomimicsensorpatternsandtoplanthenext
visitaccordingtothesensorprofile. Prioritizedexperiencereplaystrategyisdeployedto
transferlearnedknowledgeintothemodel,andKLdivergencetoutilizelong-termpattern
intomodelinduction.
3.3. ParameterIsolationMethods
Inparameterisolationmethods,specificmodelparametersareassignedtoeachtask
such that possible forgetting can be avoided. The methods address the CF issues with
theisolationoftask-specificparametersandthendynamicallyadaptthestructureofthe
model.Newmodulesaredeployedforthelearningofnewtaskswhilekeepingtheformerly
learnedparametersunchanged. Aproblemassociatedwiththisapproachisthepotential
growth of network parameters required. Progressive networks [139] and dynamically
expandablenetworks[140]arepopulararchitecturalmethods.
3.4. CombinedApproaches
Combinedapproachesrefertothemixingofthemethodstogether[103].
Cossu et al. [110] conducted a review and evaluation of the continual learning in
RNNs,differentfromthetypicalCLfocusesonfeedforwardandconvolutionalmodels.
Sequentialdataisverypopularinreal-worldapplicationslikerobotics. Thesensorsofthe
roboticssystemcanfeedtherobotwithtimeseriesinputforitswalk,learningindifferent
environments. Yet,asthecurrentfocusofcontinuallearningisonreinforcementlearning
through computer vision, there is not much research on sequential data processing for
continuallearning[110]. Twobenchmarksofspeechrecognitionandhand-drawnsketches
were proposed for the evaluation of different CL methods. The results show that the
forgettingissuesbecomemoreseriousforlongersequences.

Sensors2023,23,7167 26of32
He [111] presented the outline of their explainability module based on techniques
like dimension reduction methods and visualization methods. Currently, there is not
muchresearchwithafocusontheexplainabilityofthecontinuallearningalgorithms[141],
resultingintheproblemslikealackoftransparencyfortheCLmodules. Themodulecan
notonlyprovidethecapabilityofexplanationandvisualizationfortheupdatedneural
networkoftheCLmodulebutalsofortheidentifiedanomaliesaswell. Theidentification
ofanomaliescanbeachievedwithmachinelearningapproachesliketheDeepSupport
VectorDataDescriptionalgorithm,unsupervisedforestalgorithm,andtransformer-based
unsupervisedalgorithm. Thebasicguidelineisthatnoveltiesofscoreshigherthanthe
thresholdshouldbelabeledasanomaliesinsteadoflabelingthemasnewtasksfortheCL.
BayramandInce[115]presentedacontinuallearningapproachbasedontheHidden
MarkovModel(HMM)fortheauditorysceneanalysis(ASA)task. Sensorsystemscan
be deployed to measure the time series data of dynamical acoustic events, and event
recognitionisabouttheidentificationoftheeventsfromtheseacousticsignals. High-value
backgroundnoiseandhighcomputationaldemandsrestrictthedeploymentofcontinual
learningapproachesforthisreal-worldASA.AhierarchicalHMMmoduleisemployedto
evaluateacousticeventrecognitionandunknowneventdetection. Thenewknowledge
gainedfromtheHMMmoduleisusedfortheretrainingofanewHMMmodelinreal-
time in the continual learning module. Multiple acoustic events were evaluated with
theproposedapproachinreal-time,andpromisingresultsofhigheffectivenessandhigh
accuracywereobtained.
Guptaetal.[94]addressedthelackofpracticalvariabilityamongtheindustrialsensor
networksbydeployinganadditional,conditionalmoduletotheirgenerator-basedRNN
continuallearningmodule.Real-timesensortimeseriesdatamaybeusedforthein-process
qualitypredictionbymanufacturers. Therearedifficultiesinlimitingtheapplicationsof
DeepLearningmethodsforqualityprediction,withthemaindifficultiesbeingthecon-
tinuouschangesinthemanufacturingenvironments. Inreal-worldapplicationsofDeep
Learningalgorithms,variousfactoriesmayhavevarioussettings,andtheirsensorenviron-
mentsmaybedifferent. Nevertheless,thecurrentcontinuallearningapproachesdonot
considerthepracticalvariabilityamongthetotalnumbersandtypesofsensorsdeployed
indifferentmanufacturingenvironments[94]. Ininjectionmolding,itisnotuncommon
toproducenewproducts,andthepre-trainedmodelscannotadapttothisnewprocess
well. Tercanetal.[142]developedaCLapproachforthismanufacturingscenariobasedon
thememory-awaresynapsesmethodforthetrainingofANNwithvariousmanufacturing
products. Theexperimentalresultsofinjectionmoldingproductionsupportthatthetrans-
ferofnetworkweightsgainedfromsimilartaskscaneffectivelyraisetheefficiencyofthe
proposedapproach. Graphneuralnetworkwasemployedinthisconditioningmoduleto
controlthedeploymentdynamicsoftheircontinuallearningmodulesuchthattheoverall
systemcanadapttothedifferentsensorsettingsindifferentreal-worldmanufacturingenvi-
ronments[94]. Real-worlddatasets(DSADS[143],HAR[144],andTurbofan—FD001[145])
weretestedbyrandomlyremoving40%ofthesensorsforeachtask. Theexperimental
resultssupportthattheirproposedconditioningGNNmodulecaneffectivelyenhancethe
capabilityofthecontinuallearningmodule.
To summarize, promising results were obtained by the most recent research of CL
applications with sensor time series data records for time series classification and time
seriesforecastingtasks.
4. Conclusions
ThissurveyhaspresentedanoverviewofhowtodeployDeepLearningmethods,
advancedpreprocessingmethods,andcontinuallearningmethodsfortimeseriesclassifica-
tionandforecastingindifferentreal-worldpracticalscenarios. Thereviewhassummarized
theencouragingresultsthatCLcanbedeployedinfieldsbeyondclassificationtasks. The
non-stationary nature of the datasets in many fields poses challenges for conventional
machinelearningandDeepLearningwhileservingasgoodplatformsforinnovativeCL

Sensors2023,23,7167 27of32
applicationsinfutureworks. Anotherveryinterestingdirectionisthatfurtherexperiments
maybedonetoassesstheimpactofarchitecturesversuspreprocessingalgorithmssuchthat
theroleofspecificalgorithmscanbebetterunderstood. Thisisbecause,asobservedinthis
survey,here,themajorityoftheauthorsfocusonthepracticaldeploymentofDLandDL
modelssolely,withoutfurtherevaluatingtheinfluencesofwithandwithoutpreprocessing
algorithmsineachsensorenvironment.
AuthorContributions: Conceptualization,S.-I.A.;formalanalysis,S.-I.A.andH.F.;investigation,
S.-I.A.andH.F.;methodology,S.-I.A.andH.F.;writing,S.-I.A.andH.F.Allauthorshavereadand
agreedtothepublishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
InstitutionalReviewBoardStatement:Notapplicable.
InformedConsentStatement:Notapplicable.
Data Availability Statement: Data sharing is not applicable to this article as no new data were
createdoranalyzedinthisstudy.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.
References
1. Asadi,R.;Regan,A.ASpatial-TemporalDecompositionBasedDeepNeuralNetworkforTimeSeriesForecasting. Appl. Soft
Comput.2020,87,105963.[CrossRef]
2. Ao,S.I.AppliedTimeSeriesAnalysisandInnovativeComputing;Springer:Dordrecht,TheNetherlands,2010;ISBN978-90-481-8768-3.
[CrossRef]
3. Plageras,A.P.;Psannis,K.E.;Stergiou,C.;Wang,H.;Gupta,B.B.EfficientIoT-BasedSensorBigDataCollection-Processingand
AnalysisinSmartBuildings.FutureGener.Comput.Syst.2018,82,349–357.[CrossRef]
4. Ao,S.I.;Gelman,L.;Karimi,H.R.;Tiboni,M.AdvancesinMachineLearningforSensingandConditionMonitoring.Appl.Sci.
2022,12,12392.[CrossRef]
5. Ao,S.I.DataMiningandApplicationsinGenomics;Springer:Dordrecht,TheNetherlands,2008;ISBN978-1402089749.[CrossRef]
6. Goodfellow,I.;Bengio,Y.;Courville,A.DeepLearning;MITPress:Cambridge,MA,USA,2016.
7. LeCun,Y.;Bengio,Y.;Hinton,G.DeepLearning.Nature2015,521,436–444.[CrossRef]
8. Zheng,X.C.;Wang,M.;Ordieres-Meré,J.ComparisonofDataPreprocessingApproachesforApplyingDeepLearningtoHuman
ActivityRecognitionintheContextofIndustry4.0.Sensors2018,18,2146.[CrossRef][PubMed]
9. Dablander,F.;Bury,T.DeepLearningforTippingPoints:PreprocessingMatters.Proc.Natl.Acad.Sci.USA2022,119,e2207720119.
[CrossRef]
10. Livieris,I.E.;Stavroyiannis,S.;Pintelas,E.;Pintelas,P.ANovelValidationFrameworktoEnhanceDeepLearningModelsin
Time-SeriesForecasting.NeuralComput.Appl.2020,32,17149–17167.[CrossRef]
11. Guerrier,S.;Molinari,R.;Xu,H.;Zhang,Y.AppliedTimeSeriesAnalysiswithR.2019.Availableonline:http://ts.smac-group.com
(accessedon28July2023).
12. Rhif, M.; Abbes,A.B.; Farah,I.R.; Martinez, B.; Sang, Y.WaveletTransformApplicationfor/inNon-StationaryTime-Series
Analysis:AReview.Appl.Sci.2019,9,1345.[CrossRef]
13. Mahmoud,A.;Mohammed,A.ASurveyonDeepLearningforTime-SeriesForecasting.MachineLearningandBigDataAnalytics
Paradigms:Analysis,ApplicationsandChallenges.Stud.BigData2021,77,365–392.
14. French,R.CatastrophicForgettinginConnectionistNetworks.TrendsCogn.Sci.1999,3,128–135.[CrossRef]
15. Lee,S.;Goldt,S.;Saxe,A.ContinualLearningintheTeacher-StudentSetup:ImpactofTaskSimilarity.InProceedingsofthe38th
InternationalConferenceonMachineLearning,PMLR,Virtual,18–24July2021;Volume139.
16. Shin,H.;Lee,J.K.;Kim,J.;Kim,J.ContinualLearningwithDeepGenerativeReplay.arXiv2017,arXiv:1705.08690.
17. DeLange,M.;Aljundi,R.;Masana,M.;Parisot,S.;Jia,X.;Leonardis,A.;Slabaugh,G.;Tuytelaars,T.AContinualLearningSurvey:
DefyingForgettinginClassificationTasks.IEEETrans.PatternAnal.Mach.Intell.2022,44,3366–3385.
18. Wang,L.;Zhang,X.;Su,H.;Zhu,J.AComprehensiveSurveyofContinualLearning:Theory,MethodandApplication.arXiv
2023,arXiv:2302.00487v2.
19. Hadsell,R.;Rao,D.;Rusu,A.A.;Pascanu,R.EmbracingChange:ContinualLearninginDeepNeuralNetworks.TrendsCogn.Sci.
2020,24,1028–1040.[CrossRef]
20. Hayes, T.L.; Krishnan, G.P.; Bazhenov, M.; Siegelmann, H.T.; Sejnowski, T.J.; Kanan, C.ReplayinDeepLearning: Current
ApproachesandMissingBiologicalElements.NeuralComput.2021,33,2908–2950.[PubMed]
21. Jedlicka,P.; Tomko,M.; Robins,A.; Abraham,W.C.ContributionsbyMetaplasticitytoSolvingtheCatastrophicForgetting
Problem.TrendsNeurosci.2022,45,656–666.[CrossRef][PubMed]

Sensors2023,23,7167 28of32
22. Kudithipudi,D.;Aguilar-Simon,M.;Babb,J.;Bazhenov,M.;Blackiston,D.;Bongard,J.;Brna,A.P.;ChakravarthiRaja,S.;Cheney,
N.;Clune,J.;etal.BiologicalUnderpinningsforLifelongLearningMachines.Nat.Mach.Intell.2022,4,196–210.[CrossRef]
23. Kilickaya,M.;Weijer,J.V.;Asano,Y.TowardsLabel-EfficientIncrementalLearning:Asurvey.arXiv2023,arXiv:2302.00353.
24. Mai,Z.;Li,R.;Jeong,J.;Quispe,D.;Kim,H.;Sanner,S.OnlineContinualLearninginImageClassification:AnEmpiricalSurvey.
Neurocomputing2022,469,28–51.[CrossRef]
25. Masana,M.;Twardowski,B.;Weijer,J.V.OnClassOrderingsforIncrementalLearning.arXiv2020,arXiv:2007.02145.
26. Qu,H.;Rahmani,H.;Xu,L.;Williams,B.;Liu,J.RecentAdvancesofContinualLearninginComputerVision: AnOverview.
arXiv2021,arXiv:2109.11369.
27. Biesialska,M.;Biesialska,K.;Costajussa,M.R.ContinualLifelongLearninginNaturalLanguageProcessing:Asurvey.InProceed-
ingsofthe28thInternationalConferenceonComputationalLinguistics,Barcelona,Spain,8–13December2020;pp.6523–6541.
28. Ke,Z.;Liu,B.ContinualLearningofNaturalLanguageProcessingTasks:ASurvey.arXiv2022,arXiv:2211.12701.
29. Khetarpal,K.;Riemer,M.;Rish,I.;Precup,D.TowardsContinualReinforcementLearning:AReviewandPerspectives.J.Artif.
Intell.Res.2022,75,1401–1476.[CrossRef]
30. Rajagukguk,R.A.;Ramadhan,R.A.A.;Lee,H.J.AReviewonDeepLearningModelsforForecastingTimeSeriesDataofSolar
IrradianceandPhotovoltaicPower.Energies2020,13,6623.[CrossRef]
31. Cai,M.;Pipattanasomporn,M.;Rahman,S.Day-AheadBuilding-LevelLoadForecastsusingDeepLearningvs. Traditional
Time-SeriesTechniques.Appl.Energy2019,236,1078–1088.[CrossRef]
32. Choi,K.;Yi,J.;Park,C.;Yoon,S.DeepLearningforAnomalyDetectioninTime-SeriesData:Review,Analysis,andGuidelines.
IEEEAccess2021,9,120043–120065.
33. Deng, A.; Hooi, B. Graph Neural Network-Based Anomaly Detection in Multivariate Time Series. In Proceedings of the
Thirty-FifthAAAIConferenceonArtificialIntelligence,Online,2–9February2021.
34. Jiang,W.TimeSeriesClassification:NearestNeighborversusDeepLearningModels.SNAppl.Sci.2020,2,721.
35. IsmailFawaz,H.;Forestier,G.;Weber,J.;Idoumghar,L.;Muller,P.A.DeepLearningforTimeSeriesClassification:AReview.
DataMin.Knowl.Discov.2019,33,917–963.
36. Han,T.;Sanchez-Azofeifa,G.A.ADeepLearningTimeSeriesApproachforLeafandWoodClassificationfromTerrestrialLiDAR
PointClouds.RemoteSens.2022,14,3157.[CrossRef]
37. Campos-Taberner,M.;García-Haro,F.J.;Martínez,B.;Izquierdo-Verdiguier,E.;Atzberger,C.;Camps-Valls,G.;Gilabert,M.A.
UnderstandingDeepLearninginLandUseClassificationBasedonSentinel-2TimeSeries.Sci.Rep.2020,10,17188.
38. Naqvi,R.A.;Arsalan,M.;Rehman,A.;Rehman,A.U.;Loh,W.K.;Paul,A.DeepLearning-BasedDriversEmotionClassification
SysteminTimeSeriesDataforRemoteApplications.RemoteSens.2020,12,587.[CrossRef]
39. Zheng,J.;Huang,M.TrafficFlowForecastthroughTimeSeriesAnalysisBasedonDeepLearning.IEEEAccess2020,8,82562–82570.
[CrossRef]
40. Hua,Y.;Zhao,Z.;Li,R.;Chen,X.;Liu,Z.;Zhang,H.DeepLearningwithLongShort-TermMemoryforTimeSeriesPrediction.
IEEECommun.Mag.2019,57,114–119.[CrossRef]
41. Chen,B.;Liu,Y.;Zhang,C.;Wang,Z.TimeSeriesDataforEquipmentReliabilityAnalysiswithDeepLearning.IEEEAccess2020,
8,105484–105493.[CrossRef]
42. Lim,B.;Zohren,S.TimeSeriesForecastingwithDeepLearning:ASurvey.Phil.Trans.R.Soc.A2021,379,20200209.
43. Yasrab,R.;Zhang,J.;Smyth,P.;Pound,M.PredictingPlantGrowthfromTime-SeriesDataUsingDeepLearning.RemoteSens.
2021,13,331.[CrossRef]
44. El-Sappagh,S.;Abuhmed,T.;RiazulIslam,S.M.;Kwak,K.S.MultimodalMultitaskDeepLearningModelforAlzheimer’sDisease
ProgressionDetectionBasedonTimeSeriesData.Neurocomputing2020,412,197–215.
45. Lara-Benitez,P.;Carranza-Garcia,M.;Riquelme,J.AnExperimentalReviewonDeepLearningArchitecturesforTimeSeries
Forecasting.Int.J.NeuralSyst.2021,31,2130001.[CrossRef]
46. Cao,D.;Wang,Y.;Duan,J.;Zhang,C.;Zhu,X.;Huang,C.;Tong,Y.;Xu,B.;Bai,J.;Tong,J.;etal.SpectralTemporalGraphNeural
NetworkforMultivariateTime-seriesForecasting. InProceedingsofthe34thConferenceonNeuralInformationProcessing
Systems,Vancouver,BC,Canada,6–12December2020.
47. Torres,J.F.;Troncoso,A.;Koprinska,I.;Wang,Z.;Martínez-Álvarez,F.DeepLearningforBigDataTimeSeriesForecastingApplied
toSolarPower.InProceedingsoftheInternationalJointConferenceSOCO’18-CISIS’18-ICEUTE’18.SOCO’18-CISIS’18-ICEUTE’18
2018,SanSebastián,Spain,6–8June2018;AdvancesinIntelligentSystemsandComputing.Springer:Cham,Switzerland,2019;
Volume771.
48. Xiao,C.;Chen,N.;Hu,C.;Wang,K.;Xu,Z.;Gai,Y.;Xu,L.;Chen,Z.;Gong,J.ASpatiotemporalDeepLearningModelforSea
SurfaceTemperatureFieldPredictionusingTime-seriesSatelliteData.Environ.Model.Softw.2019,120,104502.[CrossRef]
49. Dau,H.A.;Keogh,E.;Kamgar,K.;Yeh,C.C.M.;Zhu,Y.;Gharghabi,S.;Ratanamahatana,C.A.;Chen,Y.;Hu,B.;Begum,N.;etal.
TheUCRTimeSeriesClassificationArchive.2018.Availableonline:https://www.cs.ucr.edu/~eamonn/time_series_data_2018/
(accessedon20May2023).
50. Jaeger,H.;Haas,H.HarnessingNonlinearity:PredictingChaoticSystemsandSavingEnergyinWirelessCommunication.Science
2004,304,78–80.
51. Bagnall,A.;Lines,J.;Bostrom,A.;Large,J.;Keogh,E.TheGreatTimeSeriesClassificationBakeoff:AReviewandExperimental
EvaluationofRecentAlgorithmicAdvances.DataMin.Knowl.Discov.2017,31,606–660.[PubMed]

Sensors2023,23,7167 29of32
52. Baydogan,M.G.MultivariateTimeSeriesClassificationDatasets.2015.Availableonline:http://www.mustafabaydogan.com
(accessedon28February2019).
53. Borovykh,A.;Bohte,S.;Oosterlee,C.W.ConditionalTimeSeriesForecastingwithConvolutionalNeuralNetworks.arXiv2017,
arXiv:1703.04691.
54. Torres,J.F.;Hadjout,D.;Sebaa,A.;Martinez-Alvarez,F.;Troncoso,A.DeepLearningforTimeSeriesForecasting:ASurvey.Big
Data2021,9,3–21.[PubMed]
55. ClimateCommission.TheCriticalDecade:Australia’sFuture—SolarEnergy;ClimateCommission:Manila,Philippines,2013.
56. Chollet,F.;Allaire,J.DeepLearningwithR;ManningPublications:ShelterIsland,NY,USA,2018.
57. Fan,C.;Wang,J.;Gang,W.;Li,S.Assessmentofdeeprecurrentneuralnetwork-basedstrategiesforshort-termbuildingenergy
predictions.Appl.Energy2019,236,700–710.[CrossRef]
58. Barrera-Animas,A.Y.;Oyedele,L.O.;Bilal,M.;Akinosho,T.D.;Delgado,J.M.D.;Akanbi,L.A.Rainfallprediction:Acomparative
analysisofmodernmachinelearningalgorithmsfortime-seriesforecasting.Mach.Learn.Appl.2022,7,100204.
59. Smyl,S.AHybridMethodofExponentialSmoothingandRecurrentNeuralNetworksforTimeSeriesForecasting.Int.J.Forecast.
2020,36,75–85.[CrossRef]
60. Dang,H.V.;MKohsin,R.;Nguyen,T.V.;Bui-Tien,T.;Nguyen,H.X.DeepLearning-BasedDetectionofStructuralDamageusing
Time-SeriesData.StructureandInfrastructureEngineering.Struct.Infrastruct.Eng.2021,17,1474–1493.[CrossRef]
61. Hochreiter,S.;Schmidhuber,J.LongShort-TermMemory.NeuralComput.1997,9,1735–1780.[CrossRef]
62. Cho,K.;VanMerrienboer,B.;Gulcehre,C.;Bahdanau,D.;Bougares,F.;Schwenk,H.;Bengio,Y.Learningphraserepresentations
usingRNNencoder-decoderforstatisticalmachinetranslation.InProceedingsofthe2014ConferenceonEmpiricalMethodsin
NaturalLanguageProcessing(EMNLP),Doha,Qatar,14–21October2014;pp.1724–1734.
63. Wang,F.;Yu,Y.;Zhang,Z.;Li,J.;Zhen,Z.;Li,K.WaveletDecompositionandConvolutionalLSTMNetworksBasedImproved
DeepLearningModelforSolarIrradianceForecasting.Appl.Sci.2018,8,1286.[CrossRef]
64. He,K.;Zhang,X.;Ren,S.;Sun,J.DeepResidualLearningforImageRecognition.IndianJ.Chem.-Sect.BOrg.Med.Chem.2015,45,
1951–1954.
65. Uhlig,S.;Quoitin,B.;Lepropre,J.;Balon,S.ProvidingPublicIntradomainTrafficMatricestotheResearchCommunity.SIGCOMM
Comput.Commun.Rev.2006,36,83–86.[CrossRef]
66. Shi,X.;Chen,Z.;Wang,H.;Yeung,D.Y.;Wong,W.K.;Woo,W.C.ConvolutionalLSTMNetwork:AMachineLearningApproach
forPrecipitationnowcasting.Adv.NeuralInf.Process.Syst.2015,28,802–810.
67. Yamashita,R.;Nishio,M.;Do,R.K.G.;Togashi,K.ConvolutionalNeuralNetworks:AnOverviewandApplicationinRadiology.
InsightsImaging2018,9,611–629.[PubMed]
68. Scarselli,F.;Gori,M.;Tsoi,A.C.;Hagenbuchner,M.TheGraphNeuralNetworkModel.IEEETrans.NeuralNetw.2009,20,61–80.
[CrossRef][PubMed]
69. Velickovic,P.;Cucurull,G.;Casanova,A.;Romero,A.;Lio,P.;Bengio,Y.GraphAttentionNetworks.arXiv2017,arXiv:1710.10903.
70. Hinton,G.E.;Osindero,S.;Teh,Y.-W.AFastLearningAlgorithmforDeepBeliefNets. NeuralComput. 2006,18,1527–1554.
[CrossRef]
71. Ma,M.;Sun,C.;Chen,X.DeepCouplingAutoencoderforFaultDiagnosiswithMultimodalSensoryData. IEEETrans. Ind.
Inform.2018,14,1137–1145.[CrossRef]
72. Lei,Y.;Karimi,H.R.;Cen,L.;Chen,X.;Xie,Y.Processessoftmodelingbasedonstackedautoencodersandwaveletextreme
learningmachineforaluminumplant-wideapplication.ControlEng.Pract.2021,108,104706.[CrossRef]
73. MohammdiFarsani,E.;Pazouki,E.ATransformerSelfAttentionModelforTimeSeriesForecasting.J.Electr.Comput.Eng.Innov.
2021,9,1–10.
74. Elsayed,S.;Thyssens,D.;Rashed,A.;Jomaa,H.S.;Schmidt-Thieme,L.DoWeReallyNeedDeepLearningModelsforTimeSeries
Forecasting?arXiv2021,arXiv:2101.02118v2.
75. Kanani,P.;Padole,M.ECGHeartbeatArrhythmiaClassificationUsingTime-SeriesAugmentedSignalsandDeepLearning
Approach.ProcediaComput.Sci.2020,171,524–531.[CrossRef]
76. Kisa, D.H.; Ozdemir, M.A.; Guren, O.; Akan, A. EMG based Hand Gesture Classification using Empirical Mode Decom-
position Time-Series and Deep Learning. In Proceedings of the 2020 Medical Technologies Congress, Antalya, Turkey,
19–20November2020.
77. CastroFilho,H.C.;CarvalhoJunior,O.A.;Carvalho,O.L.F.;Bem,P.P.;Moura,R.S.;Albuquerque,A.O.;Silva,C.R.;Ferreira,P.H.G.;
Guimaraes,R.F.;Gomes,R.A.T.RiceCropDetectionUsingLSTM,Bi-LSTM,andMachineLearningModelsfromSentinel-1Time
Series.RemoteSens.2020,12,2655.[CrossRef]
78. RuBwurm,M.;Korner,M.Self-AttentionforRawOpticalSatelliteTimeSeriesClassification.J.Photogramm.RemoteSens.2020,
169,421–435.
79. Kingphai,K.;Moshfeghi,Y.EEG-basedMentalWorkloadLevelEstimationusingDeepLearningModels.InErgonomics&Human
Factors;CIEHF:Birmingham,UK,2022.
80. Yokkampon,U.; Mowshowitz,A.; Chumkamon,S.; Hayashi,E.RobustUnsupervisedAnomalyDetectionwithVariational
AutoencoderinMultivariateTimeSeriesData.IEEEAccess2022,10,57835–57849.[CrossRef]
81. Mishra,S.;Bordin,C.;Taharaguchi,K.;Palu,I.ComparisonofDeepLearningModelsforMultivariatePredictionofTimeSeries
WindPowerGenerationandTemperature.EnergyRep.2020,6,273–286.[CrossRef]

Sensors2023,23,7167 30of32
82. Wen,Q.S.;Sun,L.;Yang,F.;Song,X.;Gao,J.;Wang,X.;Xu,H.TimeSeriesDataAugmentationforDeepLearning: ASurvey.
In Proceedings of the Thirtieth International Joint Conference on Artificial Intelligence (IJCAI-21), Montréal, QC, Canada,
19–27August2021;pp.4653–4660.
83. Azar, J.; Makhoul, A.; Couturier, R.; Demerjian, J.RobustIoTTimeSeriesClassificationwithDataCompressionandDeep
Learning.Neurocomputing2020,398,222–234.[CrossRef]
84. Savitzky,A.;Golay,M.J.E.SmoothingandDierentiationofDatabySimplifiedLeastSquaresProcedures.Anal.Chem.1964,36,
1627–1639.[CrossRef]
85. Vaswani, A.; Shazeer, N.; Parmar, N.; Uszkoreit, J.; Jones, L.; Gomez, A.N.; Kaiser, L.; Polosukhin, I. Attention is all you
need.InProceedingsoftheAdvancesinNeuralInformationProcessingSystems,LongBeach,CA,USA,4–9December2017;
pp.5998–6008.
86. Mognon,A.;Jovicich,J.;Bruzzone,L.;Buiatti,M.Adjust:AnAutomaticEEGArtifactDetectorBasedontheJointUseofSpatial
andTemporalFeatures.Psychophysiology2011,48,229–240.
87. Kingphai,K.;Moshfeghi,Y.OnEEGPreprocessingRoleinDeepLearningEffectivenessforMentalWorkloadClassification.
InInternationalSymposiumonHumanMentalWorkload: ModelsandApplications;Springer: Berlin/Heidelberg,Germany,2021;
pp.81–98.
88. Chalapathy,R.;Chawla,S.DeepLearningforAnomalyDetection:ASurvey.arXiv2019,arXiv:1901.03407.
89. Le,T.T.;Fu,W.;Moore,J.H.ScalingTree-BasedAutomatedMachineLearningtoBiomedicalBigDatawithaFeatureSetSelector.
Bioinformatics2020,36,250–256.[CrossRef]
90. Bahdanau, D.; Cho, K.; Bengio, Y. Neural Machine Translation by Jointly Learning to Align and Translate. arXiv 2014,
arXiv:1409.0473.
91. Livieris,I.;Stavroyiannis,S.;Iliadis,L.;Pintelas,P.SmoothingandStationarityEnforcementFrameworkforDeepLearning
Time-SeriesForecasting.NeuralComput.Appl.2021,33,14021–14035.[CrossRef][PubMed]
92. He,Y.;Huang,Z.;Sick,B.TowardApplicationofContinuousPowerForecastsinaRegionalFlexibilityMarket.InProceedingsof
the2021InternationalJointConferenceonNeuralNetworks(IJCNN),Shenzhen,China,18–22July2021;pp.1–8.
93. Kiyasseh,D.;Zhu,T.;Clifton,D.AClinicalDeepLearningFrameworkforContinuallyLearningfromCardiacSignalsacross
Diseases,Time,Modalities,andInstitutions.Nat.Commun.2021,12,4221.[CrossRef]
94. Gupta,V.;Narwariya,J.;Malhotra,P.;Vig,L.;Shroff,G.ContinualLearningforMultivariateTimeSeriesTaskswithVariable
InputDimensions.InProceedingsofthe2021IEEEInternationalConferenceonDataMining(ICDM),Auckland,NewZealand,
7–10December2021;pp.161–170.
95. Flesch,T.;Balaguer,J.;Dekker,R.;Nili,H.;Summerfield,C.ComparingContinualTaskLearninginMindsandMachines.Proc.
Natl.Acad.Sci.USA2018,115,E10313–E10322.[CrossRef][PubMed]
96. Shaheen, K.; Hanif, M.A.; Hasan, O.; Shafique, M. Continual Learning for Real-World Autonomous Systems: Algorithms,
ChallengesandFrameworks.J.Intell.Robot.Syst.2022,105,9.
97. Pfulb,B.;Gepperth,A.AComprehensive,Application-OrientedStudyofCatastrophicForgettinginDNNs.InProceedingsofthe
InternationalConferenceonLearningRepresentations(ICLR),NewOrleans,LA,USA,6–9May2019.
98. Prabhu,A.;Torr,P.;Dokania,P.Gdumb:ASimpleApproachthatQuestionsOurProgressinContinualLearning.InEuropean
ConferenceonComputerVision;Springer:Berlin/Heidelberg,Germany,2020;pp.524–540.
99. He,Y.;Sick,B.CLeaR:AnAdaptiveContinualLearningFrameworkforRegressionTasks.AIPerspect.2021,3,2.
100. Philps, D.; Weyde, T.; Garcez, A.D.A.; Batchelor, R. Continual Learning Augmented Investment Decisions. arXiv 2019,
arXiv:1812.02340v4.
101. Chen,X.;Wang,J.;Xie,K.TrafficStream:AStreamingTrafficFlowForecastingFrameworkBasedonGraphNeuralNetworks
andContinualLearning.InProceedingsoftheThirtiethInternationalJointConferenceonArtificialIntelligence,Montreal,QC,
Canada,19–27August2021.
102. Lesort, T.; George, T.; Rish, I. Continual learning in Deep Neural Networks: An Analysis of the Last Layer. arXiv 2021,
arXiv:2106.01834.
103. Mundt,M.;Hong,Y.;Pliushch,I.;Ramesh,V.AWholisticViewofContinualLearningwithDeepNeuralNetworks:Forgotten
LessonsandtheBridgetoActiveandOpenWorldLearning.NeuralNetw.2023,160,306–336.
104. Bagus,B.;Gepperth,A.;Lesort,T.BeyondSupervisedContinualLearning:AReview.InProceedingsoftheEuropeanSymposium
onArtificialNeuralNetworks,ComputationalIntelligenceandMachineLearning,Bruges,Belgium,5–7October2022.
105. Pham,Q.;Liu,C.;Sahoo,D.;Hoi,S.C.LearningFastandSlowforOnlineTimeSeriesForecasting.arXiv2022,arXiv:2202.11672v2.
106. Xiao,Y.;Liu,M.;Zhang,Z.;Jiang,L.;Yin,M.;Wang,J.StreamingTrafficFlowPredictionBasedonContinuousReinforcement
Learning.arXiv2022,arXiv:2212.12767v1.
107. Sah, R.K.; Mirzadeh, S.I.; Ghasemzadeh, H. Continual Learning for Activity Recognition. In Proceedings of the 2022 44th
AnnualInternationalConferenceoftheIEEEEngineeringinMedicine&BiologySociety(EMBC),Scotland,UK,11–15July2022;
pp.2416–2420.
108. Matteoni,F.;Cossu,A.;Gallicchio,C.;Lomonaco,V.;Bacciu,D.ContinualLearningforHumanStateMonitoring.InProceedings
oftheESANN2022Proceedings,EuropeanSymposiumonArtificialNeuralNetworks,ComputationalIntelligenceandMachine
Learning,Bruges,Belgium,5–7October2022.

Sensors2023,23,7167 31of32
109. Kwon,Y.D.;Chauhan,J.;Kumar,A.;Hui,P.;Mascolo,C.ExploringSystemPerformanceofContinualLearningforMobileand
EmbeddedSensingApplications.InProceedingsofthe2021IEEE/ACMSymposiumonEdgeComputing(SEC),SanJose,CA,
USA,14–17December2021;pp.319–332.
110. Cossu,A.;Carta,A.;Lomonaco,V.;Bacciu,D.ContinualLearningforRecurrentNeuralNetworks:AnEmpiricalEvaluation.
NeuralNetw.2021,143,607–627.[CrossRef][PubMed]
111. He,Y.AdaptiveExplainableContinualLearningFrameworkforRegressionProblemswithFocusonPowerForecasts.arXiv2022,
arXiv:2108.10781v2.
112. Doshi, K.; Yilmaz, Y. Rethinking Video Anomaly Detection—A Continual Learning Approach. In Proceedings of the 2022
IEEE/CVFWinterConferenceonApplicationsofComputerVision(WACV),Waikoloa,HI,USA,4–8January2022;pp.3036–3045.
113. Maschler,B.;Pham,T.T.H.;Weyrich,M.Regularization-basedContinualLearningforAnomalyDetectioninDiscreteManufac-
turing.InProceedingsofthe54thCIRPConferenceonManufacturingSystems,ProcediaCIRP,Virtual,22–24September2021;
Volume104,pp.452–457.
114. Maschler,B.;Vietz,H.;Jazdi,N.;Weyrich,M.ContinualLearningofFaultPredictionforTurbofanEnginesusingDeepLearning
withElasticWeightConsolidation.InProceedingsofthe202025thIEEEInternationalConferenceonEmergingTechnologiesand
FactoryAutomation,Vienna,Austria,8–11September2020;pp.959–966.
115. Bayram,B.;Ince,G.RealTimeAuditorySceneAnalysisusingContinualLearninginRealEnvironments.Eur.J.Sci.Technol.2020,
215–226,EjosatSpecialIssue2020(HORA).[CrossRef]
116. Schillaci,G.;Schmidt,U.;Miranda,L.PredictionError-DrivenMemoryConsolidationforContinualLearning:OntheCaseof
AdaptiveGreenhouseModels.KI—KünstlicheIntell.2021,35,71–80.
117. Knoblauch,J.;Husain,H.;Diethe,T.OptimalContinualLearninghasPerfectMemoryandisNP-HARD.InProceedingsofthe
37thInternationalConferenceonMachineLearning,Virtual,13–18July2020;pp.5327–5337.
118. Kirkpatrick,J.;Pascanu,R.;Rabinowitz,N.;Veness,J.;Desjardins,G.;Rusu,A.A.;Milan,K.;Quan,J.;Ramalho,T.;Grabska-
Barwinska,A.;etal.OvercomingCatastrophicForgettinginNeuralNetworks.Proc.Natl.Acad.Sci.USA2017,114,3521–3526.
[CrossRef]
119. Li,Z.;Hoiem,D.LearningwithoutForgetting.IEEETrans.PatternAnal.Mach.Intell.2017,40,2935–2947.[CrossRef]
120. Wei,H.R.;Huang,S.;Wang,R.;Dai,X.;Chen,J.OnlineDistillingfromCheckpointsforNeuralMachineTranslation.InProceedings
ofthe2019ConferenceoftheNorthAmericanChapteroftheAssociationforComputationalLinguistics: HumanLanguage
Technologies,Minneapolis,MN,USA,2–7June2019;Volume1,pp.1932–1941.
121. Chaudhry, A.; Ranzato, M.; Rohrbach, M.; Elhoseiny, M. Efficient Lifelong Learning with A-GEM. In Proceedings of the
InternationalConferenceonLearningRepresentations,Vancouver,Canada,30April-3May2018.
122. Chaudhry,A.;Rohrbach,M.;Elhoseiny,M.;Ajanthan,T.;Dokania,P.K.;Torr,P.H.S.;Ranzato,M.OnTinyEpisodicMemoriesin
ContinualLearning.arXiv2019,arXiv:1902.10486.
123. Mirzadeh,S.I.;Farajtabar,M.;Gorur,D.;Pascanu,R.;Ghasemzadeh,H.LinearModeConnectivityinMultitaskandContin-
ual Learning. In Proceedings of the ICLR 2021: The Ninth International Conference on Learning Representations, Virtual,
3–7May2021.
124. Reiss,A.;Stricker,D.IntroducingaNewBenchmarkedDatasetforActivityMonitoring.InProceedingsofthe16thInternational
SymposiumonWearableComputers,NewcastleUK,18–22June2012;pp.108–109.
125. Schmidt,P.;Reiss,A.;Duerichen,R.;Marberger,C.;VanLaerhoven,K.IntroducingWESAD,aMultimodalDatasetforWearable
StressandAffectDetection.InProceedingsofthe20thACMInternationalConferenceonMultimodalInteraction,ICMI2018,
NewYork,NY,USA,16–20October2018;pp.400–408.
126. Subramanian,R.;Wache,J.;Abadi,M.K.;Vieriu,R.L.;Winkler,S.;Sebe,N.ASCERTAIN:EmotionandPersonalityRecognition
usingCommercialSensors.IEEETrans.Affect.Comput.2018,9,147–160.[CrossRef]
127. Lee, S.W.; Kim, J.H.; Jun, J.; Ha, J.W.; Zhang, B.T. Overcoming Catastrophic Forgetting by Incremental Moment Matching.
InAdvancesinNeuralInformationProcessingSystems;CurranAssociates,Inc.:RedHook,NY,USA,2017;Volume30,pp.4652–4662.
128. Maschler,B.;Tatiyosyan,S.;Weyrich,M.Regularization-BasedContinualLearningforFaultPredictioninLithium-IonBatteries.
ProcediaCIRP2022,112,513–518.[CrossRef]
129. Eker,O.;Camci,F.;Jennions,I.MajorChallengesinPrognostics:StudyonBenchmarkingPrognosticsDatasets.InProceedings
ofthe20121stEuropeanConferenceofthePrognosticsandHealthManagementSociety,Dresden,Germany,3–6July2012;
pp.148–155.
130. Gonzalez,G.G.;Casas,P.;Fernandez,A.;Gomez,G.StepstowardsContinualLearninginMultivariateTime-SeriesAnomaly
DetectionusingVariationalAutoencoders.InProceedingsofthe22ndACMInternetMeasurementConference,IMC’22,Nice,
France,25–27October2022.
131. Saxena,A.;Goebel,K.TurbofanEngineDegradationSimulationDataSet;NASAAmesPrognosticsDataRepository:MoffettField,
CA,USA,2008.
132. Glymour,C.;Zhang,K.;Spirtes,P.ReviewofCausalDiscoveryMethodsBasedonGraphicalModels.Front.Genet.2019,10,524.
[CrossRef][PubMed]
133. Castri,L.;Mghames,S.;Bellotto,N.FromContinualLearningtoCausalDiscoveryinRobotics.arXiv2023,arXiv:2301.03886v1.
134. Lopez-Paz,D.;Ranzato,M.GradientEpisodicMemoryforContinualLearning.Adv.Neural.Inf.Process.Syst.2017,30,6467–6476.

Sensors2023,23,7167 32of32
135. Aljundi,R.;Caccia,L.;Belilovsky,E.;Caccia,M.;Lin,M.;Charlin,L.;Tuytelaars,T.OnlineContinualLearningwithMaximal
InterferedRetrieval.Adv.Neural.Inf.Process.Syst.2019,32,11849–11860.
136. Mnih, V.; Kavukcuoglu, K.; Silver, D.; Rusu, A.A.; Veness, J.; Bellemare, M.G.; Graves, A.; Riedmiller, M.; Fidjeland, A.K.;
Ostrovski,G.;etal.Human-LevelControlthroughDeepReinforcementLearning.Nature2015,518,529–533.[CrossRef]
137. Bengio,E.;Pineau,J.;Precup,D.InterferenceandGeneralizationinTemporalDifferenceLearning.arXiv2020,arXiv:2003.06350.
138. Atkinson, C.; McCane, B.; Szymanski, L.; Robins, A. Pseudo-Rehearsal: Achieving Deep Reinforcement Learning without
CatastrophicForgetting.Neurocomputing2021,428,291–307.
139. Rusu,A.A.;Rabinowitz,N.C.;Desjardins,G.;Soyer,H.;Kirkpatrick,J.;Kavukcuoglu,K.;Pascanu,R.;Hadsell,R.Progressive
NeuralNetworks.arXiv2016,arXiv:1606.04671.
140. Yoon,J.;Yang,E.;Lee,J.;Hwang,S.J.LifelongLearningwithDynamicallyExpandableNetworks.arXiv2017,arXiv:1708.01547.
141. He,Y.;Huang,Z.;Sick,B.DesignofExplainabilityModulewithExpertsintheLoopforVisualizationandDynamicAdjustment
of Continual Learning. In Proceedings of the AAAI-22 Workshop on Interactive Machine Learning, Vancouver, Canada,
28February-1March2022.
142. Tercan,H.;Deibert,P.;Meisen,T.ContinualLearningofNeuralNetworksforQualityPredictioninProductionUsingMemory
AwareSynapsesandWeightTransfer.J.Intell.Manuf.2022,33,283–292.[CrossRef]
143. Altun,K.;Barshan,B.HumanActivityRecognitionusingInertial/MagneticSensorUnits.InInternationalWorkshoponHuman
BehaviorUnderstanding;Springer:Berlin/Heidelberg,Germany,2010;pp.38–51.
144. Anguita,D.;Ghio,A.;Oneto,L.;Parra,X.;Reyes-Ortiz,J.L.HumanActivityRecognitiononSmartphonesusingaMulticlass
Hardware-FriendlySupportVectorMachine.InInternationalWorkshoponAmbientAssistedLiving;Springer:Berlin/Heidelberg,
Germany,2012;pp.216–223.
145. Saxena,A.;Goebel,K.;Simon,D.;Eklund,N.DamagePropagationModelingforAircraftEngineRun-to-FailureSimulation.
InProceedingsofthe2008InternationalConferenceonPrognosticsandHealthManagement,Denver,CO,USA,6–9October
2008;pp.1–9.
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.