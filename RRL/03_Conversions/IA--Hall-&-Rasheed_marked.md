Review
A Survey of Machine Learning Methods for Time
Series Prediction
TimothyHall*andKhaledRasheed
InstituteforArtificialIntelligence,UniversityofGeorgia,Athens,GA30602,USA;khaled@uga.edu
* Correspondence:timdhall33@gmail.com
Abstract: This study provides a comprehensive survey of the top-performing research
papersinthefieldoftimeseriesprediction,offeringinsightsintothemosteffectivemachine
learningtechniques,includingtree-based,deeplearning,andhybridmethods. Itexplores
keyfactorsinfluencingthemodelperformance,suchasthetypeoftimeseriestask,dataset
size,andthetimeintervalofhistoricaldata. Additionally,thisstudyinvestigatespotential
biasesinmodeldevelopmentandweighsthetrade-offsbetweenthecomputationalcosts
andperformance. Adetailedanalysisofthemostusederrormetricsandhyperparameter
tuning methods in the reviewed papers is included. Furthermore, this study evaluates
theresultsfromprominentforecastingcompetitions, suchasM5andM6, toenrichthe
analysis. Thefindingsofthispaperhighlightthattree-basedmethodslikeLightGBM4.6.0
anddeeplearningmethodslikerecurrentneuralnetworksdeliverthebestperformancein
timeseriesforecasting,withtree-basedmethodsofferingasignificantadvantageinterms
oftheircomputationalefficiency. Thispaperconcludeswithpracticalrecommendations
for approaching time series forecasting tasks, offering valuable insights and actionable
strategiesthatcanenhancetheaccuracyandreliabilityofpredictionsderivedfromtime
seriesdata.
Keywords: timeseriesforecasting;machinelearning;deeplearning;XGBoost;LightGBM;
CatBoost
1. Introduction
AcademicEditors:Lykourgos
MagafasandRuiAraújo ATimeSeriesPredictionistheprocessofpredictingafuturevaluebasedonhistorical
Received:16April2025 sequential observations. Accurate predictions based on time series data play a crucial
Revised:16May2025 roleinawiderangeofdomainswhereforecastingfuturevaluesisessentialforstrategic
Accepted:20May2025 planning,resourcemanagement,anddecisionmaking. Theapplicationsoftimeseriespre-
Published:26May2025
dictionspannumerousfields,includingelectricityconsumptionforecasting,environmental
Citation: Hall,T.;Rasheed,K.A qualityassessments(e.g.,airandwaterquality),meteorologicalpredictions(e.g.,rainfall,
SurveyofMachineLearningMethods
solarradiation,andwindpatterns),medicaldiagnostics(e.g.,forecastingCOVID-19case
forTimeSeriesPrediction.Appl.Sci.
trendsandpneumoniaincidences),trafficflowprediction,andfinancialdomainslikesales
2025,15,5957. https://doi.org/
forecastingandstockmarketanalysis.
10.3390/app15115957
In recent years, models based on Machine Learning (ML) have demonstrated the
Copyright:©2025bytheauthors.
most success in time series forecasting and are able to generalize well to unseen data,
LicenseeMDPI,Basel,Switzerland.
unlikemodelsbasedsolelyonprobabilityandstatistics. Specifically,Tree-BasedMachine
Thisarticleisanopenaccessarticle
distributedunderthetermsand Learning(TBML)andDeepLearning(DL)haveemergedasthemostprominentapproaches,
conditionsoftheCreativeCommons excellinginscenarioswherecomplex,nonlineardependenciesexistwithinthedata. Their
Attribution(CCBY)license abilitytogeneralizetounseendatamakesthemhighlyapplicabletoreal-worldproblems
(https://creativecommons.org/
withdiverseanddynamiccharacteristics.
licenses/by/4.0/).
Appl.Sci.2025,15,5957 https://doi.org/10.3390/app15115957

Appl.Sci.2025,15,5957 2of33
While numerous studies have examined these techniques within specific domains
andseveralsurveypapers[1,2]haveanalyzedvariousapproachestotimeseriespredic-
tionacrossdomains,theexistingliteraturereviewsfaceasignificantlimitation. Current
surveypapersstruggletodrawmeaningfulcomparisonsbetweenmodelsbecausethey
analyzeindependentstudies,eachutilizingdifferentimplementationsanddatasets. This
heterogeneity in experimental setups prevents direct model comparisons and obscures
trueperformancedifferences. Thispaperaddressesthisgapbyexclusivelyreviewingstud-
iesthatcomparebothTBMLmethodsandDLapproacheswithinthesameexperimental
framework. By focusing on research where both methodologies are implemented and
evaluatedbythesameresearchersusingidenticaldatasets,thissurveyenablesmorerobust
conclusionsabouttherelativestrengthsandweaknessesofthesemodelingapproaches.
Theremainderofthispaperisorganizedasfollows:Section2outlinesthemethodology
employedinthissurvey. Section3reviewsTBMLarchitectures,whileSection4examines
DL architectures. Section 5 presents experimental results and discusses findings, and
Section 6 highlights recent time series prediction competitions. Section 7 provides an
overview of the most important takeaways of this paper, and Section 8 provides the
directionforfutureresearch.
2. Methodology
Arigorousandsystematicmethodologyisemployedtoidentifythemostrelevant
researchpapersforthissurvey. WebofScienceisselectedastheprimarydatabasebecause
itisatrustedpublisherandindependentsourceofdatawithcomprehensivecoverageofthe
peer-reviewedscientificliterature. GiventheobjectiveofcomparingTBMLmethodswith
DLapproachesintimeseriesprediction,thispaperestablishesspecificinclusioncriteriafor
articleselection:
1. FocusonTimeSeriesApplications: theresearchmustaddressproblemsinvolving
timeseriesdata;
2. UtilizationofAdvancedTBMLMethods:studiesmustimplementadvancedTBMLar-
chitectures,particularlygradient-boosteddecisiontreesorsimilarstructures(e.g.,XG-
Boost2.1.4,LightGBM,orCatBoost1.2.7);
3. UtilizationofAdvancedNeuralNetwork(NN)Architectures: papersmustexplore
sophisticated NN architectures, including but not limited to recurrent neural net-
works(RNN),feedforwardneuralnetworks(FFNN),convolutionalneuralnetworks
(CNN), long short-term memory networks (LSTM), gated recurrent units (GRU),
orTransformers;
4. DirectComparisonsUsingIdenticalDatasets: theresearchmustpresentcomparative
evaluationsofatleastoneTBMLandoneDLarchitectureunderidenticalexperimental
setups,ensuringconsistentdatasetsandconditions.
Toidentifytherelevantliterature,acomprehensivesearchqueryisdevelopedasfollows:
(ALL=(XGBoost)ORALL=(LightGBM)ORALL=(CatBoost)ORALL=(“gradient
boost*”)) AND (ALL = (“time series”) OR ALL = (“time sequence”) OR ALL = (“tem-
poral series”) OR ALL = (“temporal sequence”) OR ALL = (“time forecast*”)) AND
(ALL = (“LSTM”) OR ALL = (“ANN”) OR ALL = (“CNN”) OR ALL = (“RNN”) OR
ALL = (“transformer”) OR ALL = (“GRU”) OR ALL = (“deep neur*”) OR ALL =
(“deeplear*”)).
Thisqueryyields589paperspublishedbetween2017and2024. Toensurefocuson
themostinfluentialresearch,papersareinitiallyselectedbasedonthecitationcount. From
thetop100most-citedpapers,65articles[3–67]satisfytheinclusioncriteria. Tomaintain
contemporaryrelevanceandcapturerecentdevelopmentsinthefield,additionaltemporal
criteria are implemented: a minimum of 10 papers per year from 2020 to 2024 must be

Appl.Sci.2025,15,5957 3of33
included. Consequently,fourhighlycitedpapersfrom2023[68–71]andthetenmost-cited
articlesfrom2024[72–81]areincorporated. Intotal,thissurveyencompasses79influential
papersinvestigatingthecomparativeperformanceofTBMLandDLapproachesintime
seriesanalysis.
3. Tree-BasedMachineLearningArchitectures
This section will present an overview of the best-performing TBML Architectures,
which are widely utilized for both regression and classification tasks. These include
RandomForests(RF),GradientBoostedDecisionTrees(GBDT),andthreeprominentimple-
mentationsofGBDT:XGBoost,LightGBM,andCatBoost. Figure1providesacomparative
visualization of the structural differences between RF and GBDT. First, this study will
discussafoundationalarchitectureintherealmofTBML:RandomForests.
Figure1.ArchitecturaldifferencesbetweenRFandGBDT,whereattributesuniquetoRFarelabeled
ingreenandthosespecifictoGBDTarelabeledinblue.Solidarrowsrepresentconnectionsconsistent
acrossallarchitectures,anddashedarrowsrepresentdeviationsforspecificarchitectures.
3.1. RandomForests
RandomForests(RF)isanensemblelearningmethodthatconstructsmultipledecision
treesandcombinestheiroutputsthroughaveragingforregressiontasksormajorityvoting
forclassificationtasks.RFusesbootstrappingtotrainindividualdecisiontreesonarandom
subset of the data at each split. This randomization, coupled with its ensemble nature,
enhancestherobustnessofRFcomparedtosingledecisiontrees,significantlyreducingthe
riskofoverfitting.

Appl.Sci.2025,15,5957 4of33
3.2. Gradient-BoostedDecisionTrees
Gradient-BoostedDecisionTrees(GBDTs)areamachinelearningalgorithmthatag-
gregates predictions from multiple weak learners, typically decision trees. GBDTs use
“boosting”tobuildmodelsiteratively,whereeachsubsequentmodelfocusesoncorrecting
mistakes made by previous models. The algorithm achieves this by optimizing a dif-
ferentiable loss function using gradient descent. While Scikit-learn provides a general
implementation of GBDT, the three most prominent and high-performing implemen-
tations discussed in this survey are XGBoost, LightGBM, and CatBoost, each offering
distinctadvantages.
3.2.1. XGBoost
XGBoost,eXtremeGradientBoosting[82],introducedbyTianqiChenin2014,isde-
signedtoaddresskeylimitationsoftraditionalGBDT,particularlycomputationalefficiency
andscalability. XGBoostgainedimmediatepopularityduetoitssignificantspeedimprove-
ments,achievedthroughinnovativeapproachesindecisiontreeconstruction. Unlikethe
greedysplittingmethodsusedinstandardGBDT,XGBoostemploysasimilarityscoreto
evaluatepotentialsplits. Thisscoremeasuresthehomogeneityofobservationswithina
noderelativetothetargetvariabletoassesthegainprovidedbyasplit. Tofurtherreduce
overfitting,XGBoostincorporatesseveraltechniques,includingpruning,wherebranches
withagainbelowathreshold(hyperparametergamma,γ)areremoved. Similarly,XG-
Boosthasseveralregularizationtechniquesthatpreventoverfittingbypenalizingcomplex
decisiontrees.
3.2.2. LightGBM
LightGBM[83],developedbyMicrosoftin2017,sharesmanyfoundationalprinciples
withXGBoostwithanevenlargerfocusonthecomputationalefficiency.LightGBMachieves
asuperiorspeedbyemployinghistogram-basedbinning,whichdiscretizescontinuous
featuresintobins,tradingminoraccuracylossesfordramaticspeedgains. Additionally,
LightGBMintroducesExclusiveFeatureBundling,whichisparticularlyeffectiveformany
real-worlddatasetswithhigh-dimensionalsparsefeaturesbecauseitconsolidatesmutually
exclusivefeaturesintoasinglerepresentation. AnotherinnovationisGradient-BasedOne-
SideSampling,whichprioritizesinstanceswithlargegradientswhilerandomlysampling
smallergradients,optimizingthelearningefficiency. LightGBMalsoutilizesaleaf-wise
treegrowthstrategy,asopposedtothelevel-wisegrowthusedintraditionalGBDTand
XGBoost. Thisapproachselectivelygrowstheleafwiththegreatestpotentialtoimprove
themodel,enablingfasterconvergenceandimprovedaccuracy.
3.2.3. CatBoost
CatBoost [84], developed by Yandex in 2017, is designed with a specific emphasis
on handling datasets with categorical features. One of its key innovations is a unique
implementationoftargetencodingwhichtakestheconceptoftraditionaltargetencoding,
wherecategoricalvaluesarereplacedwiththemeanofthetargetvariableforeachcategory,
andinsteadconstructstheencodingprocessusingonlypreviousdatatoavoiddataleakage.
AnotherdistinguishingfeatureofCatBoostisitsuseofsymmetricdecisiontrees,whereall
leavesatthesamedepthuseidenticalsplittingcriteria. Thisstructurenotonlyaccelerates
training,butalsosignificantlyreducestheinferencetime,anessentialadvantageinsome
time-sensitiveapplicationsofreal-worldforecasting.

Appl.Sci.2025,15,5957 5of33
4. DeepLearningArchitectures
ThissectionpresentsanoverviewofthemostprominentDeepLearning(DL)archi-
tecturesencounteredinthesurveyedliterature. DLwillbeusedinthispapertodescribe
asubsetofmachinelearningthatutilizesneuralnetworkstoperformclassificationand
regressiontasks. Thearchitecturesarecategorizedintofourprimarygroups: Feed-Forward
NeuralNetworks(FFNN),RecurrentNeuralNetworks(RNN),ConvolutionalNeuralNet-
works(CNN),andAttention-basedarchitectures. Figure2presentsavisualrepresentation
ofanFFNN,highlightingthearchitecturalmodificationsrequiredtotransformitintoan
RNNorCNN.
Figure2.ArchitectureofanFFNN,includingthemodificationsneededtotransformitintoaCNN
(labeledinorange)oranRNN(labeledinred).Solidarrowsrepresentconnectionsconsistentacross
allarchitectures,anddashedarrowsrepresentdeviationsforspecificarchitectures.
4.1. Feed-ForwardNeuralNetworks
ThetermFeed-ForwardNeuralNetwork(FFNN)isoftenusedinterchangeablywith
otherterminologiesintheliterature,includingaArtificialNeuralNetwork(ANN),Neu-
ral Network (NN), Multilayer Perceptron (MLP), Back Propagation Neural Network
(BPNN)[45,65],DeepNeuralNetwork(DNN),andDeepFeed-ForwardNeuralNetwork
(DFFNN).Thesenetworksarecharacterizedbyaunidirectionalflowofinformationfrom
inputtooutputnodes,oftentraversingoneormorehiddenlayers(foracomprehensive
overviewoftheimplementationdetailsandmathematicalfoundationofFFNNs,see[85]).
AlthoughthevarioustermsfortheFFNNareusedinterchangeablyinthesurveyed
literature,therearesmallarchitecturaldifferencesthatexistbetweenthesevariants,namely
in their depth. General FFNN models do not require any hidden layers, whereas MLP
modelstypicallycontainoneortwohiddenlayers. DNNsusuallyincorporatemultiple
hidden layers, allowing them to capture more complex patterns in the data. Despite
their widespread use in time series analysis, these architectures require careful feature
engineering to incorporate temporal information effectively and struggle to learn long-
term patterns within the data. These limitations create the need for more specialized

Appl.Sci.2025,15,5957 6of33
architecturesincludingConvolutionalNeuralNetworks(CNNs)andRecurrentNeural
Networks(RNNs).
ConvolutionalNeuralNetworks
ConvolutionalNeuralNetworks(CNN)areatypeofFFNNthatdistinguishthem-
selvesintheirarchitecturaldesignthroughconvolutionallayers. Thebiggestbenefitof
theseconvolutionallayersistosystematicallyscaninputdatatoextractvariousfeatures,
making them well-suited candidates for handling image data as they can detect local
features,combinethemintocomplexpatterns,andstillmaintainspatialrelationshipsbe-
tweenfeatures(foracomprehensiveexaminationofCNNarchitectures,includingdetailed
mathematicalformulationsandimplementationconsiderations,see[86]). Althoughthis
canbeusefulincertaindatasetswhichcontainatimeseriesofimages,CNNmodelslack
theabilitytorememberinformationoverlongerperiodsoftime,suchasRecurrentNeural
Network(RNN)modelsandTransformermodels.
4.2. RecurrentNeuralNetworks
Recurrent Neural Networks (RNN) distinguish themselves through their unique
feedbacklooparchitecture,whereoutputsfromprevioustimestepsarefedbackintothe
network,creatinganinternalmemorystatethatenableslearningfrompastinputs. This
recursiveprocessingallowsRNNmodelstoincorporatehistoricalinformationintocurrent
computations,makingthemparticularlywell-suitedfortimeseriesanalysis,wherecurrent
predictionsoftendependheavilyonhistoricalpatterns.
AmongRNNvariants,LongShort-TermMemory(LSTM)networkshaveemergedas
themostpopularintheliteraturestudiedforthispaper,largelyduetotheirsophisticated
gatingmechanismsthathelpmitigatethevanishinggradientproblemprevalentingeneral
RNNs. LSTMmodelsincorporateaninput,forget,andoutputgatetoregulatetheinforma-
tionflowandenablethenetworktocapturebothlong-termdependenciesandshort-term
patternseffectively[87]. VariantssuchasBidirectionalLSTMs(Bi-LSTMs),whichprocess
sequencesinbothforwardandbackwarddirections,enhancethemodel’sabilitytoleverage
contextualinformationfrombothpastandfuturetimesteps. AnothernotableRNNvariant
istheGatedRecurrentUnit(GRU),whichsimplifiestheLSTMarchitecturebycombining
theinputandforgetgatesintoasingleupdategateandintroducingaresetgate. GRUsare
computationallymoreefficientthanLSTMs,whileretainingacomparableperformancein
capturingsequencedependencies.
4.3. Attention-BasedArchitectures
Attention-Based Architectures, particularly Transformer Models [88], are the least
exploreddeeplearningapproachamongthesurveyedliteratureintimeseriesapplications.
UnlikeRNNs,whichuserecurrentlayerstoprocessdatasequentially,Transformersusea
self-attentionmechanismtoidentifywaysthatdistantdatafeaturesinaseriesarerelated
toeachother. Theyoperatebyprocessingentiresequencesinparallel,makingthemmuch
fastertotrainthanRNNs.TheapplicationofTransformershasmainlybeenusedforNatural
LanguageProcessing(NLP)modelsandlesssofortimeseriesapplications. Amongthe
surveyedliterature,onlyfivepapers[28,33,70,74,77]exploreattention-basedmodelsinthis
domain. EarlyresultssuggestthatTransformerscanoutperformtraditionalRNN-based
modelsintasksrequiringlong-termdependencymodeling, thoughtheirsuitabilityfor
specifictimeseriestaskswarrantsfurtherinvestigation.
5. ExperimentalResultsandDiscussion
WiththefoundationalTBMLandDLarchitecturesestablished,thefollowingsection
outlinesthemethodologyusedtoconducttheanalysispresentedinthissurvey.Theprocess

Appl.Sci.2025,15,5957 7of33
beginswithadetaileddiscussionofdatapreprocessinginSection5.1,wheretheinclusion
and exclusion criteria for models are established. Section 5.2 describes the evaluation
metrics employed to systematically compare the performance of different models. The
resultsoftheanalysisarepresentedinSection5.3,followedbyanin-depthdiscussionof
thesefindingsinSection5.4.
5.1. DataPreprocessing
Theprimaryobjectiveofthissurveyistoevaluateandcomparetheperformanceof
DLmodelsagainstTBMLmethodsfortimeseriesprediction. Tomaintaintheintegrity
and relevance of the analysis, certain models were excluded based on their consistent
underperformanceorlackofapplicability. Linearregression(LR)models, forexample,
are omitted due to their poor performance across most surveyed studies, apart from a
singleinstanceofRidgeRegressionthatshowedpromisingresults[27]. Whilethisexcep-
tionhighlightspotentialavenuesforfutureresearch,itshouldbenotedthatotherRidge
Regressionexamplesinthesurveyedliteratureperformpoorly[61]. DecisionTree(DT)
modelsandSupportVectorMachine(SVM)modelsarealsoexcluded,astheyconsistently
underperformedrelativetoothermethods.
AutoregressiveIntegratedMovingAverage(ARIMA)models,includingvariantslike
Seasonal ARIMA (SARIMA), have historically been popular for time series forecasting.
However,inallsurveyedinstances,thesemodelsareoutperformedbyeitherDLorTBML
methods. Consequently,ARIMA-basedmodelsareexcludedfromthiscomparativeanaly-
sis[6,19,33,36,48,51,55,59,60,62,65]. Adaboost,atree-basedensemblealgorithmdeveloped
in1995,issimilarlyexcludedduetoitsinferiorperformancewhencomparedtosimilar
modernTBMLmethodssuchasXGBoost,LightGBM,andCatBoost. Inallreviewedcases,
Adaboosteitherunderperformedormatchedtheperformanceofthesemoreadvanced
methods[30,64,66,73].
Forthisanalysis,modelsaregroupedintobroaderalgorithmiccategoriestofacilitate
meaningful comparisons. Radial Basis Function Neural Network (RBFN) [6], Neural
NetworkAutoregression(NNAR)[37],andBroadLearningSystem(BLS)[30]modelsare
groupedwithFeed-ForwardNeuralNetworks(FFNNs),whichalsoencompassMLP,ANN,
andDNNarchitectures. WhileConvolutionalNeuralNetworks(CNNs)aretechnically
FFNNs,theiruniqueoperationalcharacteristicsjustifyseparateanalysis. RecurrentNeural
Network(RNN)architectures,includingGRU,LSTM,andBi-LSTM,aregroupedalongside
DeepAR,anautoregressiverecurrentneuralnetwork[78].TheTBMLcategoryencompasses
XGBoost,LightGBM,CatBoost,Bagging,GBDT,andRFmodels.
5.2. EvaluationMetrics
To systematically compare the performance of various models surveyed in the re-
viewed papers, two evaluation metrics are employed. These metrics were designed to
capturedifferentaspectsofthemodelperformance.Thefirstmetric,FirstPlaceAggregation
(FPA),measuresthefrequencywithwhichamodelisidentifiedasthehighest-performing
ortiedforthehighest-performingmodelinthesurveyedstudies. FPAiscalculatedas:
N
FPA= first ×100
N
total
Here, N representsthenumberoftimesthemodelachievesthetoprank, while
first
N is the total number of evaluations in which the model is included. FPA provides
total
astraightforwardmeasureofamodel’sdominanceinperformancecomparisons. Akey
advantageofthismetricisthatitmitigatestheinfluenceofanypoorperformingmodels
presentwithincomparisons.

Appl.Sci.2025,15,5957 8of33
Thesecondmetricutilizesaweightedrankaggregation(WRA)approachtoaccount
fortherelativeperformanceofamodelacrossallcomparisons,notjustfirst-placerankings.
TheWRAscoreiscalculatedas:
(N −1)
WRA=1− rank
(N −1)
total
Here,N denotesthemodel’srankineachcomparison,withonerepresentingthe
rank
toprank. N isthetotalnumberofmodelsinthecomparison. Thismetricassignsascore
total
ofonetothetop-performingmodelandzerotothelowest-performingmodel, offering
anuancedperspectivethataccountsforvaryingnumbersofmodelsacrosscomparisons.
WRAisparticularlyvaluableinscenarioswheretherelativeperformanceofmodelsvaries
significantly,enablingamorecomprehensiveevaluationoftheireffectiveness.
5.3. Results
5.3.1. OverallModelPerformance
Thefirstobjectiveofthispaperistoidentifythemodelsthatexhibitthebestoverall
performanceacrossavarietyoftimeseriespredictiontasksanalyzedinthe79surveyed
studies. The models can broadly be categorized into two classes: Tree-Based Machine
Learning(TBML)modelsandDeepLearning(DL)models. Figure3illustratesthecompara-
tiveperformanceoftheseclassesbasedontheFirstPlaceAggregation(FPA)andWeighted
RankAggregation(WRA)metrics.
Figure3.FPAandWRAscoredistributionforeachclass,includingthecomparativeperformance(%)
betweenthetwoclasses.
TBMLmodelsmarginallyoutperformDLmodelsasaclass,achievingthebestper-
formance(FPA)in54.55%oftasksstudied,withaWRAscoreof0.6910. Incomparison,
DLmodelsperformbest(FPA)in52.70%oftasksandachieveaWRAscoreof0.6486. It
isimportanttonotethattiesforthehighest-performingmodelcontributetoacombined
percentageexceeding100%. Onaverage,TBMLmodelsoutperformDLmodelsbyapprox-
imately2.5%. However,thiscomparisonattheclasslevelprovidesonlyasurface-level
understandingoftheperformancelandscape. Amoregranularanalysisisneededtoassess
theperformanceofsubclasseswithineachcategory.
Figure 4 breaks down the performance of model subclasses within the TBML and
DLcategoriesfortheFPAandWRAmetrics. Notably, the“Attention”subclass, which
exclusivelycomprisesTransformermodels,emergesasthebest-performingmodelinthree

Appl.Sci.2025,15,5957 9of33
tasks, butisonlyevaluatedinfivestudies. Whilethisresultisintriguingandsuggests
apromisingavenueforfurtherresearch,thelimitedsamplesizewarrantscautionwhen
interpretingthesefindings. Consequently,thispaperdoesnotplaceaprimaryfocuson
attention-basedmodels.
Figure4.FPAandWRAscoresforeachmodel.The“ModelUse”legendindicatesthetotalnumber
ofcomparisonsforeachmodel,withspecificcountslabeledabovethebars.
Fromthedetailedsubclassanalysis,itisevidentthatthemosteffectivealgorithmsfor
timeseriespredictionareRecurrentNeuralNetwork(RNN)models,primarilycomprised
ofLSTM,GRU,andgeneralRNNarchitectures,andtheSpecializedTree-BasedModels
(SPTB)category,whichincludesXGBoost,LightGBM,andCatBoost. RNNsdemonstrate
asuperiorperformance,rankingasthebest-performingmodelsin61.36%ofstudiesand

Appl.Sci.2025,15,5957 10of33
achievingaWRAscoreof0.7330.TheyarecloselyfollowedbySPTBmodels,whichperform
bestin50%ofstudiesandachieveaWRAscoreof0.6328.
Tofurtherrefinethisunderstanding,thesubclassesarebrokendownintoindividual
models. Figures5and6presenttheperformanceofeachmodelbasedontheFPAandWRA
metrics,respectively. Amongindividualmodels,CatBoostemergesasthebestperformer
acrossbothmetrics,followedbyTransformers,LSTMs,andLightGBM.
Figure 5. FPA scores for each model. The “Model Use” legend indicates the total number of
comparisonsforeachmodel,withspecificcountslabeledabovethebars.
Figure 6. WRA scores for each model. The “Model Use” legend indicates the total number of
comparisonsforeachmodel,withspecificcountslabeledabovethebars.
However,itisimportanttonotethatlikeAttention-BasedTransformermodels,the
robustnessofCatBoost’sresultsmaybelimited,asitwasthebest-performingmodelinonly
twooutofthethreestudieswhereitwasevaluated. TheLSTMmodel,ontheotherhand,

Appl.Sci.2025,15,5957
11of33
demonstratesastrongandconsistentperformance,achievingFPAof58.97%andaWRA
scoreof0.7222. With39instancesofevaluation, itsresultsaremorestatisticallyrobust.
LightGBMalsoperformswell,withFPAof58.82%andaWRAscoreof0.6608,basedon
17studies. Incontrast,thetwoweakest-performingmodelswereMLPsandgeneralFFNNs.
Neithermodelachievedthehighestrankinanystudy,andtheirWRAscores,0.2265for
MLPand0.1667forFFNN,werethelowestamongallevaluatedmodels. Additionally,itis
notablethatthemostfrequentlycomparedmodelsinthesurveyedpaperswereXGBoost,
RF,andLSTM,with47,43,and39instances,respectively.
5.3.2. Task-SpecificModelPerformanceAnalysis
Whileoverallperformancemetricsprovideahigh-levelcomparisonofthemodels,
theydonotfullycapturehoweacharchitectureperformsonspecifictasks. Accordingly,
the next section explores the task-specific analysis of the model performance. Table 1
providesadetailedlistofthe46uniquetaskscoveredinthesurveyedpapers. Tofacilitate
meaningful comparisons, these tasks are grouped into 10 broader categories based on
sharedcharacteristicsandapplicationdomains(Figure7).
Table1.Illustratesthe46timeseriespredictiontaskspresentinthesurveyedpapers.Thefrequency
columnshowsthenumberofoccurrencesofthetasks,andthegroupcolumnshowstheassigned
categorynumberofeachtask.
| No. |                                                       |                                             | TimeSeriesPredictionTask      | Frequency | Group |
| --- | ----------------------------------------------------- | ------------------------------------------- | ----------------------------- | --------- | ----- |
| 1   |                                                       | TotalElectricityConsumption(Demand)         |                               | 8         | 1     |
| 2   |                                                       |                                             | LoadForecasting               | 2         | 1     |
| 3   |                                                       |                                             | ElectricityTheftPrediction    | 1         | 1     |
| 4   |                                                       |                                             | HeatingLoadPrediction         | 1         | 1     |
| 5   |                                                       | ReturnTemperatureofDistrictHeatingSystem    |                               | 1         | 1     |
| 6   |                                                       | ElectricityConsumptionofanElectricBus       |                               | 1         | 1     |
| 7   |                                                       |                                             | SolarPowerForecasting         | 3         | 2     |
| 8   |                                                       |                                             | WindPowerForecasting          | 2         | 2     |
| 9   |                                                       | RainfallPrediction(IncludingRainfallRunoff) |                               | 2         | 2     |
| 10  |                                                       |                                             | DroughtPrediction             | 2         | 2     |
| 11  | RiverInflowPrediction(IncludingReclaimedWaterVolumes) |                                             |                               | 2         | 2     |
| 12  | SubsurfaceTemperature(IncludingSeaSurfaceTemperature) |                                             |                               | 2         | 2     |
| 13  |                                                       |                                             | ReservoirWaterLevelPrediction | 1         | 2     |
| 14  |                                                       |                                             | FloodFrequency                | 1         | 2     |
| 15  |                                                       |                                             | GroundwaterAvailability       | 1         | 2     |
| 16  |                                                       | IndoorDaylightIlluminancesPrediction        |                               | 1         | 2     |
| 17  |                                                       | CropYield(IncludingCornBiomass,CropHeight)  |                               | 5         | 3     |
| 18  |                                                       |                                             | CropClassification            | 3         | 3     |
19 WaterQualityPrediction(IncludingChlorophyll-aandWastewaterTreatment) 8 4
| 20  |     |     | AirQuality | 1   | 4   |
| --- | --- | --- | ---------- | --- | --- |
21 PassengerDemand(IncludesBikeSharing,UrbanRailPassengerFlow) 3 5
| 22  |                                               |                                               | TravelTimePrediction          | 1   | 5   |
| --- | --------------------------------------------- | --------------------------------------------- | ----------------------------- | --- | --- |
| 23  | FutureTrafficofMobileBaseStationsinUrbanAreas |                                               |                               | 1   | 5   |
| 24  |                                               |                                               | TrafficQueueLength            | 1   | 5   |
| 25  |                                               |                                               | TunnelDeformationPrediction   | 1   | 6   |
| 26  |                                               |                                               | DamStructuralHealthPrediction | 1   | 6   |
| 27  |                                               | HighwayTunnelPavementPerformance              |                               | 1   | 6   |
| 28  | PredictTemperatureTrendofWindTurbineGearbox   |                                               |                               | 1   | 6   |
| 29  |                                               | DischargeCapacityEstimationforLi-IonBatteries |                               | 1   | 6   |
| 30  |                                               |                                               | SinteringProcessPrediction    | 1   | 6   |
| 31  |                                               | StockPrice(IncludingCrypto/StockTrend)        |                               | 3   | 7   |
| 32  |                                               |                                               | HedgeFundReturnPrediction     | 1   | 7   |
| 33  |                                               |                                               | StoreItemDemand               | 1   | 7   |

Appl.Sci.2025,15,5957
12of33
Table1.Cont.
| No. |                                                    | TimeSeriesPredictionTask         |                   | Frequency | Group |
| --- | -------------------------------------------------- | -------------------------------- | ----------------- | --------- | ----- |
| 34  |                                                    |                                  | VegetablesDemand  | 1         | 7     |
| 35  |                                                    | Post-StrokePneumoniaPrediction   |                   | 1         | 8     |
| 36  | PredictPeakDemandDaysofCardiovascularAdmissions    |                                  |                   | 1         | 8     |
| 37  |                                                    | COVID-19NewCasesPrediction       |                   | 1         | 8     |
| 38  |                                                    | AnomalyDetectionforWebServices   |                   | 1         | 9     |
| 39  |                                                    |                                  | LeakDetection     | 1         | 9     |
| 40  |                                                    |                                  | FallDetection     | 1         | 9     |
| 41  | GlobalModelsforVariousTasks(SimulatedandRealWorld) |                                  |                   | 1         | 10    |
| 42  |                                                    | PredictingEmergingResearchTopics |                   | 1         | 10    |
| 43  |                                                    |                                  | LaneChangingRisk  | 1         | 10    |
| 44  |                                                    | PredictiveProcessMonitoring      |                   | 1         | 10    |
| 45  |                                                    |                                  | OilWellProduction | 1         | 10    |
| 46  |                                                    |                                  | CrimePrediction   | 1         | 10    |
Figure7.Distributionoftimeseriespredictiontasksbycategory,includinggroupnumbersandthe
percentagerepresentationofeachcategory.
Foreachtaskcategory,theperformanceofTBMLmodelsandDLmodelsiscompared,
withadditionalfocusonthebest-performingsubclasseswithinthesecategories: RNNs
andSPTBmodels. Figures8and9illustratethecomparativeperformanceofthesemodel
classes using the FPA and WRA metrics, respectively. The results highlight that TBML
modelsconsistentlyoutperformDLmodelsinTaskGroups1,5,9,and10.
Inthesecategories,TBMLmodelsdemonstrateperformanceadvantagesrangingfrom
37.5%to68.85%inWRAscoresand25%to150%inFPAscores. Conversely,DLmodels
showsignificantsuperiorityinTaskGroups2,6,and7,withperformanceimprovementsof
28.57%to97.26%inWRAand50%to500%inFPAcomparedtoTBMLmodels. Amore
nuancedcomparisonbetweenRNNandSPTBmodelsrevealsthatSPTBmodelsperform
notablybetterthanRNNsinTaskGroups5and10,withWRAimprovementsof45.83%
and22.22%andFPAimprovementsof25%and66.67%,respectively,comparedtoRNNs.
Incontrast, RNNmodelsexceloverSPTBmodelsinTaskGroups2, 4, 6, 7, and8, with
performancegainscomparedtoSPTBmodelsrangingfrom31.25%to84.32%inWRAand
50%to260%inFPA.

Appl.Sci.2025,15,5957 13of33
Figure8.FPAscoresforeachmodel.Bluebarsrepresenttheoverallmodeltypes,whileorangebars
highlightthebest-performingmodelclasses.
Figure9.WRAscoresforeachmodel.Bluebarsrepresenttheoverallmodeltypes,whileorangebars
highlightthebest-performingmodelclasses.
5.3.3. ImpactofDatasetSizeonModelPerformance
Beyond examining how the model performance varies across different tasks, it is
equallyimportanttoconsiderhowexternalvariables,suchasthedatasetsize,contributeto
theseperformancedifferences. Thisstudyalsoexamineshowthedatasetsizeinfluences
therelativeperformanceofdifferentmachinelearningmodelsfortimeseriesprediction.
Toensureabalancedanalysis,datasetrangeswereselectedtocontainanequalnumberof
modelcomparisonswithineachrange. TheanalysisconsidersTBMLmodelsandDLmod-
els,aswellastheirtop-performingsubclasses: SPTBmodelsandRNNs. Figures10and11
presenttheperformanceofthesemodelclassesacrossthedatasetrangesusingFPAand
WRAmetrics,respectively.
Inthesmallestdatasetrange(0–2173samples),TBMLmodelsperformcomparablyto
DLmodelsoverall,butRNNssignificantlyoutperformSPTBmodels,achievinganFPA
advantageof50%andaWRAadvantageof0.425. Inthesecondrange(2173–7800samples),

Appl.Sci.2025,15,5957 14of33
DLmodelsdemonstrateaslightedgeoverTBMLmodels,withFPAandWRAgainsof
12.12%and0.0972,respectively. Withinthisrange,RNNsoutperformSPTBmodelswitha
WRAgainof0.1296,whiletheFPAscoresforbothsubclassesareequal.
Figure10. FPApercentageforeachmodelbasedondatasetsize. Bluebarsrepresenttheoverall
modeltypes,whileorangebarsindicatethebest-performingclassofmodels.Thedatasetsizerange
isexclusiveonthelowerboundandinclusiveontheupperbound.
Figure11. WRApercentageforeachmodelbasedondatasetsize. Bluebarsrepresenttheoverall
modeltypes,whileorangebarsindicatethebest-performingclassofmodels.Thedatasetsizerange
isexclusiveonthelowerboundandinclusiveontheupperbound.
Formid-sizeddatasets(7800–35,712samples),TBMLmodelsbegintoshowaslight
advantage over DL models, outperforming them by 8.33% in FPA and 0.0417 in WRA.
However,RNNmodelscontinuetooutperformSPTBmodels,achievinganFPAgainof5%
andaWRAgainof0.0542. Inthesecond-largestdatasetrange(35,712–206,573samples),
TBML models maintain a modest advantage over DL models, with FPA and WRA im-
provementsof4.55%and0.0462,respectively. Similarly,RNNsoutperformSPTBmodels

Appl.Sci.2025,15,5957 15of33
by0.0556inFPA,whilebothachieveequivalentWRAscores. Thelargestdatasetrange
(206,573–11,275,200samples)revealsamoredefinitivetrend. Inthisrange,TBMLmod-
elsoutperformDLmodelsby4.55%inFPAand15.15inWRA.Moreover,SPTBmodels
achievesignificantgainsoverRNNmodels,withanFPAadvantageof16.67%andaWRA
advantageof0.3833.
5.3.4. ImpactofDataTimeIntervalonModelPerformance
Beyond the quantity of data, this study also investigates the temporal granularity
atwhichdataarecollectedtoexploretheimplicationsonthemodelperformance. Asin
previousanalyses,thecomparisonincludesTBMLmodelsandDLmodels,alongwiththeir
top-performingsubsets: SPTBmodelsandRNNs. Figures12and13illustratetheFPAand
WRAscoresacrossdifferenttimeintervalsofthedatasets.
Figure12.FPAscoreforeachmodelbasedontimeintervalofdata.Bluebarsrepresenttheoverall
modeltypes,whileorangebarsindicatethebest-performingclassofmodels.
Figure13.WRAscoreforeachmodelbasedontimeintervalofdata.Bluebarsrepresenttheoverall
modeltypes,whileorangebarsindicatethebest-performingclassofmodels.

Appl.Sci.2025,15,5957 16of33
DLmodelsoutperformTBMLmodelsinthe5/10min,15/30min,and1-monthin-
tervals. Notably, theseintervalshaveamodestrepresentationinthedataset, occurring
six, four, and eight times, respectively. Conversely, TBML models show a slightly bet-
ter performance in the 1/4 h interval (16 occurrences) and the 7/8/15/16-day interval
(3occurrences), with FPA and WRA advantages of 6.25% and 0.0469, and 33.33% and
0.0556,respectively. Thetimeintervalsof8daysand16daysaretestedusingthesame
model,see[9].
AdeepercomparisonofsubclassesrevealsthatRNNmodelsoutperformSPTBmodels
in the 1 min, 5/10 min, 15/30 min, 1-day, and 1-month time intervals. Among these,
the 1-day interval (9 RNN occurrences vs. 12 SPTB occurrences) is particularly signifi-
cant,whereRNNmodelsachieveanotableFPAadvantageof27.78%andaWRAadvan-
tageof0.2509. Ontheotherhand,SPTBmodelssurpassRNNmodelsinthe1/4hand
7/8/15/16-dayintervals. The1/4hinterval(16occurrences)isparticularlynoteworthy,
withSPTBmodelsoutperformingRNNsby18.59%inFPAand0.0785inWRA.
5.3.5. ImpactofResearchFocusonObservedModelPerformance
Whileintrinsicdatacharacteristicsundoubtedlyinfluencethemodelperformance,
itisalsoimportanttostudyhowresearchprioritiesandbiasesshapethemodelperfor-
mance. Thepaperssurveyedinthisstudyexhibitdiverseobjectivesandemphases,ranging
fromdevelopinghybriddeepneuralnetworkstobenchmarkingspecificadvancedTBML
models against DL models, or conducting balanced evaluations across a variety of ML
andDLapproaches. Thissubsectionexamineswhethertheprimaryfocusoftheresearch—
categorizedasTBMLmodels,DLmodels,orabalancedapproach—affectstheobserved
performanceoutcomesoftheevaluatedmodels. Figures14and15presenttheFPAand
WRAscores,respectively,forTBMLandDLmodelsundereachresearchfocuscategory.
Theresultsrevealanoticeablebiasinperformanceoutcomesdependingontheprimary
focusofthepapers:
1. DeepLearning-FocusedPapers:
Whentheprimaryfocusofthepaperisondeeplearningmodels, DLmodels
outperformTBMLmodelssignificantly.TheFPAscoreforDLmodelsis33.79%higher,
andtheWRAscoreis0.2891pointshigherthanTBMLmodels. Thisfindingsuggests
that papers with a DL emphasis may introduce methodological, architectural, or
experimentaladvantagestailoredtohighlighttheDLperformance.
2. Tree-BasedModel-FocusedPapers:
Conversely, when papers focus on TBML models, the observed performance
skewsinfavorofTBMLmodels. Inthiscategory, TBMLmodelsachievea66.67%
higher FPA score and a 0.5694 higher WRA score compared to DL models. These
results indicate that TBML-focused research often optimizes conditions or design
choicesthatfavorthesemethods.
3. BalancedFocusPapers:
Inpaperswithnospecificemphasisoneithermodelclass,TBMLmodelsslightly
outperformDLmodels. TheFPAscoreforTBMLmodelsis15.23%higher,andthe
WRAscoreis0.1771pointshigherthanDLmodels. Thisfindingsuggeststhatwhen
researchisconductedwithoutbiastowardaspecificmodelclass,TBMLmodelsmay
haveaslightadvantage,potentiallyduetotheirrelativesimplicityandrobustnessin
arangeofscenarios.
Besidesexploringinherentdatacharacteristicsorpotentialbiasesthatmayaffecta
model’sperformance,itisimportanttoinvestigatethecomputationalcostrequiredtotrain
amodel.

Appl.Sci.2025,15,5957 17of33
Figure14.FPAscoreforeachmodelclassbasedonthefocusofthepaper.
Figure15.WRAscoreforeachmodelclassbasedonthefocusofthepaper.
5.3.6. ModelTrainingTimeAnalysis
AnessentialfactortoconsiderwhenevaluatingtheperformanceofMLmodelsistheir
trainingtime,particularlygiventhesignificantcomputationalcostsassociatedwithsome
models. Thetrainingtimedirectlyimpactsthefeasibilityofdeployingthesemodelsin
real-worldapplicationswherecomputationalefficiencyisoftencritical. Ofthesurveyed
papers,tenstudies[4,20,29,43,45,51,55,66,67,74]providetrainingtimecomparisonsforthe
modelsevaluated. Inthesepapers,thetrainingtimeofthebest-performingTBMLmodel
andDLmodelisanalyzed.
TheresultsdemonstratethatTBMLmodelssignificantlyoutperformDLmodelsin
termsoftheirtrainingefficiency(Table2). Notably,thereisonlyoneinstance[29]wherea
DLmodel,anMLP,trainedfasterthanitsTBMLcounterpart(XGBoost).Inthisspecificcase,
theMLPachieveda22.55%reductioninitstrainingtimecomparedtoXGBoost. However,
acrossalltenstudies,TBMLmodelsdemonstratedamarkedadvantage. Onaverage,TBML
modelswere126,934.94%fasterthanDLmodels,withthemediantrainingtimeadvantage

Appl.Sci.2025,15,5957 18of33
being5603.43%faster. ThisstarkdifferenceunderscorestheefficiencyofTBMLmodelsin
scenarioswherecomputationalresourcesandtimeconstraintsarelimitingfactors.
Table2.TBMLtrainingadvantageforeachsurveyedstudythatconductstrainingtimeanalyses.
Metric TBMLTrainingAdvantage(%)
Study[4] 4010.33
Study[20] 181.81
Study[29] −22.55
Study[67] 1251.81
Study[43] 142.66
Study[45] 7196.53
Study[74] 905,140
Study[51] 235,559.39
Study[55] 10,145.98
Study[66] 100,140
Median 5603.43
Mean 126,934.94
In order to assess the impact of data characteristics and computational efficiency
differencesbetweenmodels,itisimportanttoanalyzehowthesemodelperformancesare
quantifiedinthefirstplace.
5.3.7. AnalysisofErrorMetricsinModelEvaluation
Evaluating the model performance requires the use of appropriate error metrics,
which vary depending on whether the task involves classification or regression. This
subsectionprovidesacomprehensiveanalysisoftheerrormetricsemployedacrossthe
surveyedpapers.
ErrorMetricsforClassificationModels
Theclassificationmodelsreviewedinthisstudywereevaluatedusingthefollowing
setofmetrics:
• FalsePositiveRate(FPR);
• KappaCoefficient(KC);
• PositivePredictiveValue(PPV);
• NegativePredictiveValue(NPV);
• Receiver-OperatingCharacteristic(ROC)Curve;
• MatthewsCorrelationCoefficient(MCC);
• AreaUndertheROCCurve(AUC);
• Sensitivity;
• Specificity;
• Recall;
• Precision;
• F1Score;
• Accuracy.
Thefrequencyofthesemetrics’usageisillustratedinFigure16. Themetricnames
arereportedexactlyaslistedinthesurveyedpapers,evenifsomerepresentequivalent
measures(e.g.,recallandsensitivity).
Amongthemostemployedmetrics,Recallwasusedin35.29%ofthestudies,Precision
in41.18%,theF1Scorein47.06%,andAccuracyin76.47%ofthepapers.

Appl.Sci.2025,15,5957 19of33
Figure16.Percentofpapersthatuseeacherrormetricforclassificationtasks.
ErrorMetricsforRegressionModels
Theregressionmodelsreviewedinthisstudywereevaluatedusingthefollowingset
ofmetrics:
• IndexofAgreement(IA);
• NormalizedMeanAbsolutePercentageError(NMAPE);
• PredictionofChangeinDirection(POCID);
• MeanNormalizedBias(MNB);
• NormalizedMeanBiasError(NMBE);
• RootMeanSquaredPercentageError(RMSPE);
• RootSquaredLogarithmicError(RMSLE);
• Mean;
• PercentBias(PBIAS);
• R;
• MeanAbsoluteScaledError(MASE);
• SymmetricMeanAbsoluteError(SMAPE);
• CoefficientofVariationoftheRootMeanSquareError(CVRMSE);
• Nash–SutcliffeEfficiency(NSE);
• Domain-SpecificErrorMetrics;
• MeanSquaredError(MSE);
• MeanAbsolutePercentageError(MAPE);
• R2;
• MeanAbsoluteError(MAE);
• RootMeanSquaredError(RMSE).
TheprevalenceofthesemetricsisdepictedinFigure17.Amongthetraditionalmetrics,
MSEwasusedin22.03%ofthepapers,MAPEin37.29%,R2in45.76%,MAEin55.93%,and
RMSEin67.80%.
5.3.8. HyperparameterOptimizationTechniques
HyperparametertuningisanothercriticalaspectofMLmodeldevelopment,asthe
choice of hyperparameters can significantly influence the performance. Several of the
surveyedarticlesspecifythehyperparameteroptimizationtechniquesemployedintheir
studies. Figure 18 illustrates the relative prevalence of these techniques across the sur-

Appl.Sci.2025,15,5957 20of33
veyedpapers. ThemostusedhyperparameteroptimizationtechniquewasaGridSearch,
followed by Bayesian Optimization (BO), Random Search, Manual Optimization, and
OPTUNAAutomaticHyperparameterTuningSoftware. Lessfrequentlyusedmethods
includedalgorithmssuchastheFireflyAlgorithm(FA)[21],NeuralNetworkIntelligence
(NNI)[33],EnhancedReptileSearchAlgorithm(ERSA)[73],andHiddenDipperThroated
Optimization(HDTO)[78],eachofwhichwasmentionedinonlyonepaper. Whilemany
studiesfocusedonasingleoptimizationapproach,onepaper[45]providedacompara-
tiveevaluationofmultiplehyperparameteroptimizationmethods. Thisstudyfoundthat
BayesianOptimizationoutperformedtechniquessuchasaGridSearchandParticleSwarm
Optimization(PSO)intermsofitssearcheffectiveness. Byleveragingprobabilisticmodels
toguidethesearchprocess,BayesianOptimizationwasabletoreducecomputationalcosts
whileidentifyingoptimalhyperparameterconfigurationsmoreefficiently.
Figure17.Percentofpapersthatuseeacherrormetricforregressiontasks.
Figure18.Usageforeachhyperparameteroptimizationtechnique.

Appl.Sci.2025,15,5957 21of33
Havingexaminedtheperformanceofconventionalmodelarchitectures,thisstudy
nowshiftsfocustohybridmodels,whichintegratemultipleMLandDLarchitectures,and
areacommonapproachtoimprovingthepredictiveperformanceintimeseriestasks.
5.3.9. ComparativeAnalysisofHybridModels
Acrossthesurveyedliterature,hybridmodelsoftenoutperformindividualstand-alone
models,althoughtherearenotableexceptions. Thissectionexaminestheseexceptionsas
wellasprovidesinsightsintotherelativeperformanceofdifferenthybridconfigurations.
PerformanceofHybridModelsvs. IndividualModels
Whilehybridmodelsgenerallyexhibitasuperiorperformance,afewstudieshighlight
caseswhereindividualmodelsoutperformhybrids:
1. Study[44]: a2DCNN,3DCNN,andXGBoostmodeleachoutperformedahybrid
RNN-CNNmodel;
2. Study[80]: RFandXGBoostmodelssurpassedmultiplehybridmodels,including
CNN-LSTM,CNN-GRU,RNN-GRU,andRNN-LSTMconfigurations;
3. Study[81]: aCatBoostmodeloutperformedaspatio-temporalattention-basedCNN
andBi-LSTMhybridmodel.
HybridModelsComparedtoOtherHybrids
Severalpapersexploredtherelativeperformanceofdifferenthybridconfigurations,
providingvaluableinsightsintothedesignconsiderations:
1. Study[45]:ahybridCNN-LSTM-AttentionmodeloutperformedaCNN-LSTMmodel,
whichinturnoutperformedanLSTM-Attentionmodel;
2. Study [48]: CEEMDAN decomposition was applied to both an XGBoost and DL
model. ThehybridXGBoost-CEEMDANmodelperformedbetterthanitsDL-based
counterpart;
3. Study[72]: aBi-LSTM-LightGBMhybridoutperformedaBi-LSTM-FFNNhybrid;
4. Study[73]: LSTMmodelswithdecompositiontechniques,VariationalModeDecom-
position(VMD)andEmpiricalModeDecomposition(EMD),werecompared. The
LSTM-VMDhybridoutperformedtheLSTM-EMDhybrid;
5. Study [74]: an Attention-based Bi-LSTM hybrid model performed better than an
Attention-basedBi-GRUhybridmodel;
6. Study[80]: amongfourhybridDLmodels,CNN-LSTMdemonstratedthebestperfor-
mance,followedbyCNN-GRU,RNN-GRU,andRNN-LSTM;
7. Study[65]:fourhybridmodelswerecompared,withrelativeperformancesasfollows:
LSTM-XGBoost>FFNN-XGBoost>LSTM-MLR>FFNN-MLR;
5.4. Analysis
Thissectionsynthesizesthebiggesttakeawaysfromtheexperimentalresults,highlight-
ingkeyinsights,overarchingtrends,andlimitationsobservedacrossthesurveyedstudies.
ComparativePerformanceofTree-BasedandDeepLearningModels:Theexperimental
results indicate that TBML models and DL models exhibit comparable performances
overall. Amongtheirrespectivesubcategories,SPTBmodelsandRNNsemergeasthebest
performers,furtherunderscoringwhythesemodelsdominatemuchoftheresearchfocus
inthispaper. However,TBMLmodelsdemonstrateaslightoveralledgeduetothestronger
performanceoftheirweakestalgorithms. Notably,RFandGBDToutperformtheweakest
DLmodels.
At the individual algorithm level, CatBoost, LSTM, and LightGBM stand out as
thebest-performingmodels. WhileCatBoosthaslimitedrepresentationinthesurveyed

Appl.Sci.2025,15,5957 22of33
papers,itishighlysimilartoLightGBMandXGBoost—bothofwhichhadmuchgreater
representationanddemonstratedastrongperformance—furthersupportingtheconclusion
thatCatBoostisatop-performingmodel. Ontheotherhand,attention-basedarchitectures
(e.g.,Transformers)alsoshowstrongpotential,butunlikeCatBoost,therearenodirectly
comparable algorithms in this category with more extensive research in the surveyed
papers. Thislackofbroaderrepresentationunderscorestheneedforthefurthervalidation
ofTransformersthroughmoreillustrativestudies.
Domain-SpecificPerformance: Performanceanalysisacrossapplicationdomainsre-
vealsdistinctadvantagesforspecificmodelgroups:
• TBMLModels: theseoutperformintasksrelatedtoenergyandutilities,transportation
andurbanmobility,anomalydetection,andmiscellaneousapplications;
• DL Models: these outperform in tasks related to environmental and meteorologi-
calpredictions,structuralandmechanicalhealthmonitoring,andfinancial/market
trendforecasting;
• SPTBModels: theseoutperformintasksrelatedtotransportationandmiscellaneous
applications,whileRNNmodelsdominateinenvironmental,healthcare,andfinance-
relatedtasks;
• RNNModels: theseoutperformintasksrelatedtoEnvironmentalandMeteorological
Predictions, Water and Air Quality, Structural and Mechanical Health Monitoring,
StockMarket/Finance/MarketTrends,andHealthcareandBiomedicalPredictions.
Itisimportanttonotethatthedatasetincludesrelativelysmallrepresentationsfor
somecategories(rangingfrom3.85%to21.8%ofthetotalpapers). Asaresult,thefindings
presentedheredonotpresentdefinitiveevidencethatanyonetypeofmodelisdominant
withinagivendomain. Instead,theyhighlightinterestingpatternsandtrendsthatmerit
further investigation and validation with larger datasets. However, there are several
explanationsthatcanaccountfortheperformancedifferentialbetweenmodels.
TBMLmodelsexcelinareaswithtabular,noisy,missing,andcategoricaldata,making
themespeciallysuitableforthedomainofutilities, transportation, urbanmobility, and
anomalydetection,whichofteninvolvestructured,tabulardatasetsthatmayhavemany
sparsefeatures. TBMLmodelsareespeciallyequippedforanomalydetectionastheyare
abletousethetreesplittingcriteriatocapturefeatureinteractionswithoutneedingmuch
explicitfeatureengineering. Similarly,SPTBalgorithmsexcelintransportationandmiscel-
laneousapplicationsastheyareoptimizedforspeedanddonotrequireextensivefeature
engineering,makingthemcompatibleforawidearrayofmiscellaneousapplications. DL
modelsoutperforminenvironmental/meteorologicalpredictionsandmechanicalhealth
monitoringduetotheirabilitytoeffectivelycaptureunstructuredandspatial–temporal
patternsinthedata. Additionally,DLmodelsperformbetterinfinancial/markettrendfore-
castingasthesemodelsarebetterabletohandlelaggedeffectsandtemporaldependencies,
withlessfeatureengineeringthanTBMLmodels. Specifically,RNNmodelsexcelinawide
rangeoftasksincludingWaterandAirQuality,EnvironmentalandMeteorologicalPredic-
tions,StructuralandMechanicalHealthMonitoring,StockMarket/Finance/MarketTrends,
andHealthcare/BiomedicalPredictionsduetotheiruniqueabilitytorememberlong-term
dependencies. Patternsinthesedomainscanspanoverdays,weeks,andevenmonths,
andRNNmodelslikeLSTMareabletorememberthisinformationthroughmemorygates
withoutmanualfeatureengineering.
DatasetSize:Ananalysisoftheinfluenceofthedatasetsizeontherelativeperformance
of machine learning models for time series prediction reveals some interesting trends.
In ML tasks with the least amount of data, DL models perform comparably to TBML
modelsoverall. However,RNNmodelsdemonstrateasignificantadvantageoverSPTB
models. Asthedatasetsizeincreases,DLmodelsbegintoshowaslightedgeoverTBML

Appl.Sci.2025,15,5957 23of33
models in the lower mid-sized range (2173–7800 samples), although the gap narrows
in the upper mid-sized range (7800–35,712 samples). Across this range, RNN models
continue to outperform SPTB models, though the margin diminishes, reflecting SPTB
models’growingrobustnesswithincreasingdata. Forlargerdatasets,TBMLmodelsgain
aclearadvantageoverDLmodels, withtheirperformancegapwideningatthelargest
dataset range (206,573–11,275,200samples). This trend demonstrates the scalability of
TBMLmodels,particularlySPTBmodels,inhandlingvastamountsofdata.
ThereasonthatDLandspecificallyRNNmodelsareabletoperformbetteronsmaller
datasetsthanTBMLmodelsistheyarebetterabletohandlelatentrepresentationsifsequen-
tialinputsarestrong,evenonsmallamountsofdata. TBMLmodelslackinducitvebias
forsequencelearningandthusmaystuggleonsmalldatsetsifnotgiventheappropriately
engineeredsequentialfeatures. Conversely,TBMLmodels,specificallySPTBmodels,out-
performDLmodelsonlargerdatsetsasthesealgorithmsaremuchmorecomputationally
efficientatdealingwithlargeamountsofdatawhileremainingrobusttonoise,missing
values, or irrelevant features, allowing them to quickly capture complex patterns. DL
models are comparatively computationally expensive, harder to optimize, and require
carefulpreprocessingfornoisydata. WhenDLmodelsarenotgivenadequatetraining
resourcesorarenotcarefullyoptimized,theyconsistentlyunderperformrelativetotheir
TBMLcounterparts. Itisworthpointingoutthatthesegeneralizationsdonotholdtrue
inallcircumstances. Study[15]showcasesthatDLmodelssuchasLSTMstrugglewith
overfittingandgeneralization,especiallyonsmalldatasets,duetothenatureofthemodel
architecture(therearealargernumberofweightsanddeviationtermsforlearning). The
easiestwaytoovercomethislimitationistoexpandthedataset,asshowninstudy[16]. If
therearenootherdataavailable,thenDLmodelsmayfallshorttootherTBMLmethods.
Study [67] demonstrates that in situations where no extra data are available, gradient-
boostedTBMLtechniquesshowasuperiorgeneralizationabilityandthusleadtohigher
predictionaccuracy.
Temporal Resolution: This study examines the impact of time interval lengths on
theperformanceofMLmodelsfortimeseriesprediction. However,noconsistentpattern
ortrendemergesacrossthetimeintervals. DLmodelsperformbetterinsomeintervals,
whileTBMLperformsbetterinothers. Assuch, thereisnocommonthreadthatunites
theseresultsacrossalltemporalresolutionsstudied. Thereasonforthismayindicatethat
otheraspectsofthedatacompositionordomain-specifictasksaremoreimportantand
impactful on the model performance, leaving weak-to-nonexistent trends for temporal
resolutiondifferences.
InfluenceofResearchFocus: Anotablefindingistheinherentbiasinperformanceout-
comesdependingontheresearchfocusofthepaper. DLmodelssignificantlyoutperform
TBMLmodelsinpapersfocusedonDLtechniques,andviceversaforTBML-focusedre-
search. Thissuggeststhatresearchersmaydevotedisproportionateattentiontooptimizing
modelsalignedwiththeirresearchfocuswhileinvestinglesseffortinmodelstheyareusing
forcomparativeefforts. Readersshouldexercisecautionwheninterpretingcomparative
resultsinsuchstudies. Instudieswithnospecificfocus,TBMLmodelsslightlyedgeout
DL models, providing an interesting case for their superior performance in “bias-free”
papers. ApotentialexplanationforthisdisparityisthattheaccuracyofDLmodelsismore
dependentontheregularizationtechniquesusedandhyperparmetervalueschosenfor
testingcomparedtoTBMLmodels. WhenresearchersarebiasedtowardsDLmethods,
theymayspendmoretimeonthisaspectofmodeldevelopmentcomparedtoTBMLmodel
development,causingDLmethodstoperformbetter. Ifresearchersdonotinvestenough
timeoreffortinthisareaofmodeldevelopemnt,thenTBMLmodelsaremorelikelyto
outperformDLmethods.

Appl.Sci.2025,15,5957 24of33
ComputationalEfficiency:Oneofthemostimpactfulfindingsisthedisparityintraining
timesbetweenTBMLandDLmodels. TBMLmodelswerefoundtobe,onaverage,two-
to-fourordersofmagnitudefasterthanDLmodels.ThismakesTBMLmodelsparticularly
appealingforreal-worldapplicationswherecomputationalcostisacriticalconsideration.
ErrorMetrics: Popularerrormetricsforevaluatingclassificationandregressiontasks
mayprovidevaluablebenchmarksforfutureresearch. Theseincludeclassificationmet-
ricssuchasRecall,Precision,theF1Score,andAccuracy,aswellasRegressionMetrics
suchasRMSE,MAE,MAPE,andMSE.Futureresearchmaybenefitfromaligningeval-
uationmethodswiththesemetricstoensurecomparabilityacrossstudies. Additionally,
researchersmaywanttoconsiderusinganovelweightedqualityevaluationindex(WQE)
proposedby[89],whichcombinesthefourmostpopularregressionmetrics(RMSE,MAE,
MAPE,andR2)intoasingleunifiedevaluationstandardthatmoreholisticallycapturesthe
modelperformance.
HyperparameterOptimization: Agridsearchisthemostfrequentlyusedhyperpa-
rameteroptimizationmethod,butitisalsothemostcomputationallyintensive. Bayesian
Optimizationoffersapromisingalternative,providingasimilarperformancewithmuch
lowercomputationaldemands. MethodssuchasOPTUNA’sautomatichyperparameter
tuningsoftwarearealsoemergingasviableoptionsforhyperparametertuning.
HybridModels: Thisstudyfindsstrongevidencethatcombiningmodelsgenerally
enhancestheirperformance,asevidencedbynumeroussurveyedpapersthatimplement
hybridapproaches. Thesehybridmodelsconsistentlyoutperformindividualmodels,with
their performance often improving as more models are integrated. There are notable
exceptions to this trend, discussed in Section 5.3.9, where individual models show a
superiorperformancecomparedtohybrids. Theseindividualmodelexamplesexclusively
involveSPTBmodels,furtherunderscoringtherobustperformanceofthesealgorithms.
When comparing hybrid configurations, the results reveal that combinations of SPTB
modelswithRNNmodelsyieldparticularlystrongoutcomes. Additionally,hybridmodels
incorporatingeitherSPTBorRNNarchitectureswithattention-basedorCNNmodelsalso
demonstratenotableperformanceimprovements.
Anecdotal Findings: Beyond the quantitative analysis across all surveyed papers,
severalanecdotalobservationsofferadditionalinsights:
1. FeatureSensitivity: GBDTmodelsarelessaffectedbyredundantorremovedfeatures,
whereas the ANN performance drops significantly when redundant features are
added[8];
2. FeatureSelection: Whenallfeaturesareprovided,XGBoostconsistentlydeliversthe
best performance. However, when variables are selected using forward selection,
otherDLmodelsbegintooutperformit. Interestingly,theXGBoostmodelutilizing
all features outperforms the XGBoost model that uses only the forward-selected
features[15];
3. Domain-SpecificFindings: LightGBMproducesmoreaccurateresultsfortopresearch
termsinemergingtopics,eventhoughitgenerallyhashighererrorsthanNN[37];
4. InferenceTime: Onestudyreportedinferencetimesfortheirmodels. Theycompared
an XGBoost model (0.001 s) with an LSTM model (0.311 s) and a Bi-LSTM model
(1.45s),findingXGBoosttobe311timesfasterthanBi-LSTMand1450timesfaster
thanLSTM.Thisdrasticallyfasterinferencetimeemphasizesitspracticalityintime-
sensitiveapplications[74];
5. Simulatedvs. Real-WorldData: LightGBMmatchestheneuralnetworkperformance
onsimulateddata,butoutperformsonreal-worlddatasets[51];
6. Time-SeriesImageData: CNNmodelsexcelinpredictiontasksinvolvingtime-series
imagedata[3,23,44].

Appl.Sci.2025,15,5957 25of33
6. M5andM6ForecastingCompetitions
Besides looking at research papers that focus on using ML models for real world
applicationsintimeseriesprediction,competitionsthatchallengeteamstocreatemodels
for a common dataset provide valuable insights into the comparative performance of
machine learning methods. These contests enable direct comparisons under the same
controlledconditions. Amongsuchcompetitions,theMForecastingCompetitionsstand
outasthemostprominent,well-structured,andwell-funded. Thissectionfocusesonthe
twomostrecentiterations: theM5andM6ForecastingCompetitions.
6.1. M5ForecastingCompetition
TheM5ForecastingCompetition,heldin2020,focusedonpredictingretailsalesusing
real-worlddatawhichconsistedof42,840timeseriesofWalmartunitsales.Thecompetition
hadtwocomponents: theAccuracyCompetitionandtheUncertaintyCompetition,each
with a prize pool of USD 50,000. These incentives attracted thousands of participants,
creatingalargedatasetforanalysis.
6.1.1. M5AccuracyCompetition
The M5 Accuracy Competition [90] tasked participants with providing the most
accurate point forecasts, evaluated using a Weighted Root Mean Squared Scaled Error
(WRMSSE)metric. Atotalof5507teamsfrom101countriesparticipated,withLightGBM
emergingasthedominantmodelamongthetop50bestperformingteams. Briefinsights
fromthetopfivemodelsincludethefollowing:
1. First Place: combined recursive and non-recursive LightGBM models to create
220 models, where the average of 6 models was used to forecast the series, each
exploitingadifferentlearningapproachandtrainingset;
2. SecondPlace: created50LightGBMmodels,5foreachofthe10stores,utilizingaDL
neuralnetworktoadjustmultipliersbasedonhistoricalsalesdataforeachstore;
3. Third Place: employed 43 recursive neural networks (LSTMs) incorporating over
100features;
4. FourthPlace: created40non-recursiveLightGBMmodels;
5. FifthPlace: utilizedsevenrecursiveLightGBMmodels.
Nearlyallofthetop50submissionsappliedthelastfour28-daywindowsofdatafor
cross-validationtofine-tunethehyperparameters. Manytop-performingteams,including
1stand3rdplace,usedexogenousfeatureslikespecialdaysandzero-salesperiodsintheir
models. Theresearchersofthischallengeconcludedthatthecompetitionreinforcedthe
valueofmodelcombination,cross-learning,andcross-validation. Newfindingsincluded
thesuperiorperformanceoftheLightGBMmodelcomparedtoallothers,aswellasthe
importanceofexogenous/explanatoryvariablesusedforforecasting.
6.1.2. M5UncertaintyCompetition
TheUncertaintycompetition[91]taskedparticipantswithforecastingthedistribution
ofrealizedvalues,requiringpredictionsofninequantiles(0.005,0.025,0.165,0.250,0.500,
0.750, 0.835, 0.975, and 0.995). The Weighted Scaled Pinball Loss function was used to
evaluatetheperformance.Althoughthiscompetitionwaslesspopular,attracting892teams,
therelianceonLightGBMmodelsremainedconsistent,withfourofthetopfivesubmissions
incorporating it in their frameworks. Brief insights from the top five models include
thefollowing:
1. First Place: utilized 126 LightGBM models, one for each quantile and aggrega-
tionlevel;

Appl.Sci.2025,15,5957 26of33
2. SecondPlace: combinedrecursiveLightGBMmodels,statisticalmethods,andsimple
timeseriesforecastingtechniques;
3. ThirdPlace:employedahybridapproachintegratingLightGBMandneuralnetworks;
4. FourthPlace: usedtwoLSTM-basedneuralnetworks;
5. FifthPlace: implemented280LightGBMmodelsinacomprehensiveensemble.
AMonteCarlosimulation,usedbythesixth-placeteam,wastheonlytop-50method
notinvolvingLightGBM,XGBoost,orneuralnetworks. ThefindingsfromtheUncertainty
competitionmirroredthoseoftheAccuracycompetition, reaffirmingthedominanceof
LightGBM and the importance of model combination. A notable observation was the
stark contrast in participant expertise: while the Accuracy competition was won by an
undergraduate student with limited knowledge in the domain of retail sales, the Un-
certaintycompetitionwasdominatedbyKagglemastersandgrandmasterswithstrong
statisticalbackgrounds.
6.2. M6ForecastingCompetition
TheM6forecastingcompetitionfrom2022to2023[92]markedasignificantevolution
intheMseries. WithaprizepoolofUSD300,000,itattracted226teamstoparticipate. The
challengerevolvedaroundcreatinginvestmentportfoliosusingreal-timedatafrom50U.S.
stocksand50exchange-tradedfunds(ETFs). Unlikeprioriterations,theM6competition
emphasizedbothforecastingandinvestmentdecisionmaking, awardingprizesforthe
forecastingaccuracy,investmentperformance,andoverallperformance. Participantswere
givenflexibilityintheirdatasourcesandmethodologies. Whileorganizersprovidedanop-
tionaldatasetofadjustedclosingvalues,teamscouldchoosetheirowndata,frequency,and
supportinginformation,suchaseconomicindicatorsornews. Thecompetitionspanned
12 months, with teams submitting monthly forecasts and investment strategies for the
subsequent20tradingdays.
Thewinnersinforecasting,investment,andthecombined“duathlon”categoryall
useddistinctmethods. ThetopforecastingmodelusedaBayesiandynamicfactormodel.
Thebest-performinginvestmentmodelreliedonAutoTS,anopen-sourcelibraryforproba-
bilistictimeseriesforecasting. Theduathlonchampionemployedameta-learningmodel
using NNs, which ranked fourth in forecasting. Notably, an XGBoost-based approach
securedsecondplaceinbothforecastingandtheduathlon. Interestingly,theteamthatwon
theinvestmentchallengeplaced92ndinforecasting,andthesecond-placeinvestmentteam,
whichusedatypeofexponentialsmoothingmodel(ATA),ranked110thinforecasting.
In fact, the researchers found zero correlation between forecasting and the investment
performance,emphasizingthatateam’sabilitytoaccuratelypredictastock’sfutureprice
wasnotthedrivingfactorincreatingthemostprofitableinvestmentportfolio.
Theresearcherswerenotsurprisedthatthebestperformingmethodsincludedboth
conventionaleconometrictimeseriesmethodsaswellassophisticatedmachinelearning
methodsbecauseoftheuniquechallengespresentinfinancialforecastingincludingexternal
factors,seasonality,stochastictrends,etc.ThekeytakeawayfromtheM6competitionisthat
thechoiceofdataandtheirusageareascriticalastheforecastingtechniquesthemselvesin
achievingsuperiorresults.
6.3. TakeawaysfromM5andM6ForecastingCompetitions
OneofthemostnotabletakeawaysfromtheM5competitionwasthedominanceof
LightGBM.Itseaseofuseallowedevenrelativelyinexperiencedparticipantstoexcel,as
evidencedbythefirst-placefinisherintheM5AccuracyCompetition,anundergraduate
student. Mosttop-performingteamsreliedonensemblesofLightGBMmodels,leveraging
itsefficiencyinhandlinglargedatasets. TheresultsoftheM5competitionalsoemphasized

Appl.Sci.2025,15,5957 27of33
theimportanceofcombiningmultiplemodels. Mosttopteamsutilizedensembles,often
containinghundredsofindividualmodels,toenhancetheaccuracyoftheirpredictions.
Across both the M5 and M6 competitions, cross-validation (CV) and hyperparameter
tuningemergedasindispensablecomponentsofsuccessfulforecastingmethodologies. All
top-performingteamsemployedthoroughCVtooptimizetheirmodels.
OnecriticaltakeawayfromtheM6competitionwastheimportanceofthedataquality,
feature engineering, and the inclusion of exogenous variables. Unlike the M5 competi-
tion, where all participants worked with a standardized dataset, M6 participants were
responsibleforsourcingtheirowndata. Thecomplexityofthiscompetition,includingthe
uniquechallengesinthefinancialdomain, alsoresultedinthenumberofparticipating
teamstodecreasetolessthan4%oftheM5competition’sturnout(despiteasubstantial
increaseinincentives). Theresultsofthecompetitionshowednoclearconsensusonthe
best-performing methodology and suggest that the importance of the data quality and
strongfeatureengineering,includingtheexogenousvariableschosen,oftenoutweighsthe
importanceinthechoiceofthepredictionmodelitself.
7. Conclusions
Thissurveyofmachinelearningmethodsfortimeseriespredictionilluminatesseveral
key strategies for approaching time series forecasting tasks. Table 3 provides a visual
overviewofthebest-performingmodelsfromtheresearchinthisstudybasedonthedata
characteristicschosen. Basedonthesefindings,thefollowingapproachisrecommended
forresearchersandpractitionerstacklingtimeseriespredictionproblems.
Firstandforemost,thedomainanddataplayapivotalroleindeterminingthesuccess
ofaforecastingmodel. Carefuldomainanalysistoidentifythemostimpactfuldatasources,
coupledwithmeticulousfeatureengineeringtoextractandconstructrelevantfeatures,
should be the initial focus. The importance of high-quality data and strong exogenous
features cannot be overstated, as evidenced by both the findings of this study and the
resultsofrecentforecastingcompetitions. Investingsignificanteffortinthisphaseislikely
toyieldthegreatestdividendsinthepredictiveperformance. Oncethedataareprepared,
startingwithaTree-BasedMachineLearning(TBML)modellikeLightGBM—orCatBoost
for datasets with a high proportion of categorical features—is a logical choice. These
gradient-boostingmethodsofferseveraladvantages: theyarecomputationallyefficient,
requirelessfeatureselection,andhavedemonstratedacompetitiveorsuperiorperformance
comparedtodeeplearningapproachesinvarioussettings. Suchmodelsserveasalow-cost
baselineforexperimentationanditerativeimprovement.
Themodelevaluationshouldbeguidedbytask-specificmetrics. Forregressionprob-
lems,metricssuchastheMeanAbsoluteError(MAE)orRootMeanSquaredError(RMSE)
areappropriate,whileclassificationtasksshoulduseRecall,Precision,theF1Score,and
Accuracy. Hyperparametertuningisanothercriticalcomponentofthemodelingprocess.
If prior knowledge exists about potential hyperparameter values, a grid search can be
employedforsystematicexploration. Otherwise,techniqueslikeBayesianOptimizationor
librariessuchasOPTUNAarerecommendedfortheirabilitytoefficientlyexplorelarge
parameterspacesandidentifyoptimalconfigurations. Iftheinitialmodelfailstomeetthe
desiredperformancestandardsorfurtherenhancementsarerequired,RecurrentNeural
Networks (RNNs), such as LSTMs or GRUs, are a logical next step. When building a
deeplearningmodel,itiscrucialtocarefullyselectandpreprocessfeaturestooptimize
the model’s performance and ensure it delivers the best results. As with earlier stages,
hyperparametertuningshouldbeemployedtomaximizetheperformance. Finally,com-
biningmodels—suchastheinitialTBMLmodelwithadeeplearningmodel—canoften
yieldsuperiorresults. Ensemblemethodsleveragethestrengthsofmultiplemethodologies,

Appl.Sci.2025,15,5957
28of33
capturingdiversepatternsandmitigatingweaknessesinherenttoanysingleapproach,as
demonstratedinthisstudy.
Table3.Summarytableofbest-performingmodelsforeachdatacharacteristic.
DatasetSize Best-PerformingModelClass Best-PerformingModelSubclass
|     |                           | Small(0–2173)       | TBML/DL | RNN      |
| --- | ------------------------- | ------------------- | ------- | -------- |
|     | Small/Medium(2173–7800)   |                     | DL      | SPTB/RNN |
|     |                           | Medium(7800–35,712) | TBML    | RNN      |
|     | Medium/Large(35,712)      |                     | TBML    | SPTB/RNN |
|     | Large(206,573-11,275,200) |                     | TBML    | SPTB     |
TaskCategory Best-PerformingModelClass Best-PerformingModelSubclass
|                                         |                                | EnergyandUtilities | TBML | SPTB     |
| --------------------------------------- | ------------------------------ | ------------------ | ---- | -------- |
|                                         | EnvironmentalandMeteorological |                    | DL   | RNN      |
|                                         | AgricultureandCropManagement   |                    | TBML | SPTB     |
|                                         |                                | WaterandAirQuality | TBML | RNN      |
|                                         | TransportationandUrbanMobility |                    | TBML | SPTB     |
| StructuralandMechanicalHealthMonitoring |                                |                    | DL   | RNN      |
| StockMarket,Finance,andMarketTrends     |                                |                    | DL   | RNN      |
| HealthcareandBiomedicalPredictions      |                                |                    | TBML | RNN      |
|                                         |                                | AnomalyDetection   | TBML | SPTB/RNN |
|                                         |                                | Other              | TBML | SPTB     |
TimeInterval Best-PerformingModelClass Best-PerformingModelSubclass
|     |                        | 1min     | TBML/DL | RNN  |
| --- | ---------------------- | -------- | ------- | ---- |
|     |                        | 5,10min  | DL      | RNN  |
|     |                        | 15,30min | DL      | RNN  |
|     |                        | 1,4h     | TBML    | SPTB |
|     |                        | 1day     | TBML/DL | RNN  |
|     | 1week,8day,15day,16day |          | TBML    | SPTB |
|     |                        | 1month   | DL      | RNN  |
ComputationalEfficiency Best-PerformingModelClass Best-PerformingModelSubclass
|     |     | TrainingTime  | TBML | SPTB |
| --- | --- | ------------- | ---- | ---- |
|     |     | Inferencetime | TBML | SPTB |
Inconclusion,effectivetimeseriespredictionisacombinationofdomainknowledge,
data quality, rigorous preprocessing, and the strategic application of the best machine
learningmethodologies. StartingwithscalableandinterpretableTBMLmodels,fine-tuning
their parameters, and iteratively incorporating advanced techniques like DL provides
anefficientframeworkfortacklingtimeseriesforecastingchallenges. Byfollowingthis
approach,researchersandpractitionerscanmaximizethepredictiveaccuracywhileopti-
mizingcomputationalcostsinavarietyofdomains.
8. FutureWork
There are several areas of future work that researchers could focus on to expand
the insights of this paper, especially in areas of growing importance in the field of DL.
Oneoftheseareasthatwasbrieflytoucheduponinthispaperandthatwarrantsfuture
researchisTransformer-basedarchitectures. Theinitialresearchindicatesthattransformers
excel in long-range dependency modeling and thus perform well in the reviewed pa-
pers[28,33,70,74,77],showcasingaperformanceonparwiththebest-performingmodelsin
theliterature. Asthereareonlyfiveresearchpapersincludedinthisstudy,futureresearch
shouldinvestigatethevalidityofthisbyexploringmorerecentpaperswheretransformer
modelsarebeingappliedtotimeseriesapplications. Oneofthebiggestchallengesthat

Appl.Sci.2025,15,5957 29of33
facesattention-basedarchitecturesistheirsignificantcomputationalcost. Aninteresting
areatoexploreinaddressingthisispre-trainedtransformermodels[93]. Thesemodelscan
bepre-trainedonlargecollectionsofunrelatedtimeseriesdata,enablingtheimproved
performanceoftrainingondatasetsacrossdomains.
Other areas that future researchers could focus on include Diffusion Models and
NeuralOrdinaryDifferentialEquationModels. DifferentialEquationModelshaveshown
successintext,image,andvideoapplicationsandrecentlyhavestartedtobeappliedtotime
seriesforecastingusecases(foracomprehensivereviewofdiffusionmodelsfortimeseries
applications,see[94]). Futureresearchshouldfocusoncombattingtheexceptionallyhigh
computationalcostassociatedwiththeDiffusionModelsappliedtotimeseriesapplications
whilemaintaininghighaccuracy. Similarly,NeuralOrdinaryDifferentialEquationsoffera
modelingframeworkthatprovidesaprincipledapproachforforecastingcontinuoustime
seriesdatabycombiningneuralnetworkswiththemathematicsofdifferentialequations
(for a comprehensive review of Neural Ordinary Differential Equations for time series
applications,see[95]). NeuralOrdinaryDifferentialEquationsinvolvesolvingdifferential
equationsatatrainingandinferencetimewhichcanbecomputationallyveryexpensive.
Futureresearchinthisfieldshouldfocusonreducingthesecomputationaldemandsby
developingmoreefficientsolverstoincreasethepracticalityofthisDLarchitecturefortime
seriesforecastingapplications.
AuthorContributions: Conceptualization,T.H.andK.R.;methodology,T.H.;software,T.H.;vali-
dation,T.H.;formalanalysis,T.H.;investigation,T.H.;resources,T.H.;datacuration,T.H.;writing—
originaldraftpreparation, T.H.; writing—reviewandediting, K.R.andT.H.; visualization, T.H.;
supervision,K.R.;projectadministration,T.H.andK.R.;fundingacquisition,K.R.Allauthorshave
readandagreedtothepublishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement:Theoriginalcontributionspresentedinthisstudyareincludedinthis
article.Furtherinquiriescanbedirectedtothecorrespondingauthor.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.
References
1. Lim,B.;Zohren,S.Time-seriesforecastingwithdeeplearning:Asurvey.Philos.Trans.R.Soc.AMath.Phys.Eng.Sci.2021,379,
20200209.[CrossRef]
2. Liu,Z.;Zhu,Z.;Gao,J.;Xu,C.ForecastMethodsforTimeSeriesData:ASurvey.IEEEAccess2021,9,91896–91912.[CrossRef]
3. Zhong,L.;Hu,L.;Zhou,H.Deeplearningbasedmulti-temporalcropclassification. RemoteSens. Environ. 2019,221,430–443.
[CrossRef]
4. Ke,J.;Zheng,H.;Yang,H.;Chen,X.Short-termforecastingofpassengerdemandunderon-demandrideservices: Aspatio-
temporaldeeplearningapproach.Transp.Res.PartCEmerg.Technol.2017,85,591–608.[CrossRef]
5. Ju,Y.;Sun,G.;Chen,Q.;Zhang,M.;Zhu,H.;Rehman,M.U.AModelCombiningConvolutionalNeuralNetworkandLightGBM
AlgorithmforUltra-Short-TermWindPowerForecasting.IEEEAccess2019,7,28309–28318.[CrossRef]
6. Rafi,S.H.;NahidAl,M.;Deeba,S.R.;Hossain,E.AShort-TermLoadForecastingMethodUsingIntegratedCNNandLSTM
Network.IEEEAccess2021,9,32436–32448.[CrossRef]
7. Galicia,A.;Talavera-Llames,R.;Troncoso,A.;Koprinska,I.;Martínez-Álvarez,F.Multi-stepforecastingforbigdatatimeseries
basedonensemblelearning.Knowl.-BasedSyst.2019,163,830–841.[CrossRef]
8. Bagherzadeh, F.; Mehrani, M.-J.; Basirifard, M.; Roostaei, J. Comparative study on total nitrogen prediction in wastewater
treatmentplantandeffectofvariousfeatureselectionmethodsonmachinelearningalgorithmsperformance.J.WaterProcessEng.
2021,41,102033.[CrossRef]
9. Kang,Y.;Ozdogan,M.;Zhu,X.;Ye,Z.;Hain,C.;Anderson,M.Comparativeassessmentofenvironmentalvariablesandmachine
learningalgorithmsformaizeyieldpredictionintheUSMidwest.Environ.Res.Lett.2020,15,064005.[CrossRef]

Appl.Sci.2025,15,5957 30of33
10. Chakraborty, D.; Elzarka, H.Advancedmachinelearningtechniquesforbuildingperformancesimulation: Acomparative
analysis.J.Build.Perform.Simul.2019,12,193–207.[CrossRef]
11. Zheng,J.;Zhang,H.;Dai,Y.;Wang,B.;Zheng,T.;Liao,Q.;Liang,Y.;Zhang,F.;Song,X.Timeseriespredictionforoutputof
multi-regionsolarpowerplants.Appl.Energy2020,257,114001.[CrossRef]
12. Zhang,Y.;Li,C.;Jiang,Y.;Sun,L.;Zhao,R.;Yan,K.;Wang,W.Accuratepredictionofwaterqualityinurbandrainagenetwork
withintegratedEMD-LSTMmodel.J.Clean.Prod.2022,354,131724.[CrossRef]
13. Mazzia,V.;Khaliq,A.;Chiaberge,M.ImprovementinLandCoverandCropClassificationbasedonTemporalFeaturesLearning
fromSentinel-2DataUsingRecurrent-ConvolutionalNeuralNetwork(R-CNN).Appl.Sci.2020,10,238.[CrossRef]
14. Barrera-Animas,A.Y.;Oyedele,L.O.;Bilal,M.;Akinosho,T.D.;Delgado,J.M.D.;Akanbi,L.A.Rainfallprediction:Acomparative
analysisofmodernmachinelearningalgorithmsfortime-seriesforecasting.Mach.Learn.Appl.2022,7,100204.[CrossRef]
15. Shin,Y.;Kim,T.;Hong,S.;Lee,S.;Lee,E.;Hong,S.;Lee,C.;Kim,T.;Park,M.S.;Park,J.;etal. PredictionofChlorophyll-a
ConcentrationsintheNakdongRiverUsingMachineLearningMethods.Water2020,12,1822.[CrossRef]
16. Luo, J.; Zhang, Z.; Fu, Y.; Rao, F. Time series prediction of COVID-19 transmission in America using LSTM and XGBoost
algorithms.ResultsPhys.2021,27,104462.[CrossRef]
17. Gong,M.;Bai,Y.;Qin,J.;Wang,J.;Yang,P.;Wang,S.Gradientboostingmachineforpredictingreturntemperatureofdistrict
heatingsystem:AcasestudyforresidentialbuildingsinTianjin.J.Build.Eng.2020,27,100950.[CrossRef]
18. Wang,Z.;Hong,T.;Li,H.;AnnPiette,M.Predictingcity-scaledailyelectricityconsumptionusingdata-drivenmodels.Adv.Appl.
Energy2021,2,100025.[CrossRef]
19. Yang,Y.;Heppenstall,A.;Turner,A.;Comber,A.Usinggraphstructuralinformationaboutflowstoenhanceshort-termdemand
predictioninbike-sharingsystems.Comput.Environ.UrbanSyst.2020,83,101521.[CrossRef]
20. Wei,Z.;Zhang,T.;Yue,B.;Ding,Y.;Xiao,R.;Wang,R.;Zhai,X.Predictionofresidentialdistrictheatingloadbasedonmachine
learning:Acasestudy.Energy2021,231,120950.[CrossRef]
21. ZahoorAli,K.;Muhammad,A.;Javaid,N.;Malik,N.S.;Shafiq,M.;Choi,J.-G.ElectricityTheftDetectionUsingSupervised
LearningTechniquesonSmartMeterData.Sustainability2020,12,8023.[CrossRef]
22. Hussein, E.A.; Thron, C.; Ghaziasgar, M.; Bagula, A.; Vaccari, M. Groundwater Prediction Using Machine-Learning Tools.
Algorithms2020,13,300.[CrossRef]
23. Su,H.;Wang,A.;Zhang,T.;Qin,T.;Du,X.;Yan,X.-H.Super-resolutionofsubsurfacetemperaturefieldfromremotesensing
observationsbasedonmachinelearning.Int.J.Appl.EarthObs.Geoinf.2021,102,102440.[CrossRef]
24. Kumar,V.;Kedam,N.;Sharma,K.V.;Mehta,D.J.;Caloiero,T.AdvancedMachineLearningTechniquestoImproveHydrological
Prediction:AComparativeAnalysisofStreamflowPredictionModels.Water2023,15,2527.[CrossRef]
25. Jing,Y.;Hu,H.;Guo,S.;Wang,X.;Chen,F.Short-TermPredictionofUrbanRailTransitPassengerFlowinExternalPassenger
TransportHubBasedonLSTM-LGB-DRS.IEEETrans.Intell.Transp.Syst.2021,22,4611–4621.[CrossRef]
26. Li,Y.;Bao,T.;Gao,Z.;Shu,X.;Zhang,K.;Xie,L.;Zhang,Z.Anewdamstructuralresponseestimationparadigmpoweredby
deeplearningandtransferlearningtechniques.Struct.HealthMonit.2022,21,770–787.[CrossRef]
27. Yu,G.;Zhang,S.;Hu,M.;Wang,Y.K.PredictionofHighwayTunnelPavementPerformanceBasedonDigitalTwinandMultiple
TimeSeriesStacking.Adv.Civ.Eng.2020,2020,8824135.[CrossRef]
28. Torres,J.F.;Martínez-Álvarez,F.;Troncoso,A.AdeepLSTMnetworkfortheSpanishelectricityconsumptionforecasting.Neural
Comput.Appl.2022,34,10533–10545.[CrossRef]
29. Ge,Y.;Wang,Q.;Wang,L.;Wu,H.;Peng,C.;Wang,J.;Xu,Y.;Xiong,G.;Zhang,Y.;Yi,Y.Predictingpost-strokepneumoniausing
deepneuralnetworkapproaches.Int.J.Med.Inform.2019,132,103986.[CrossRef]
30. Li, G.; Zhang, A.; Zhang, Q.; Wu, D.; Zhan, C.PearsonCorrelationCoefficient-BasedPerformanceEnhancementofBroad
LearningSystemforStockPricePrediction.IEEETrans.CircuitsSyst.IIExpressBriefs2022,69,2413–2417.[CrossRef]
31. Sundararajan,K.;Garg,L.;Srinivasan,K.;AliKashif,B.;Jayakumar,K.;Ganapathy,G.P.;SenthilKumaran,S.;Meena,T.A
ContemporaryReviewonDroughtModelingUsingMachineLearningApproaches.Comput.Model.Eng.Sci.2021,128,447–487.
[CrossRef]
32. Wu,W.;Chen,J.;Yang,Z.;Tindall,M.L.ACross-SectionalMachineLearningApproachforHedgeFundReturnPredictionand
Selection.Manag.Sci.2021,67,4577–4601.[CrossRef]
33. LópezSantos,M.;García-Santiago,X.;EchevarríaCamarero,F.;BlázquezGil,G.;CarrascoOrtega,P.ApplicationofTemporal
FusionTransformerforDay-AheadPVPowerForecasting.Energies2022,15,5232.[CrossRef]
34. Shangguan,Q.;Fu,T.;Wang,J.;Fang,S.e.;Fu,L.Aproactivelane-changingriskpredictionframeworkconsideringdriving
intentionrecognitionanddifferentlane-changingpatterns.Accid.Anal.Prev.2022,164,106500.[CrossRef][PubMed]
35. Prodhan,F.A.;Zhang,J.;Yao,F.;Shi,L.;PangaliSharma,T.P.;Zhang,D.;Cao,D.;Zheng,M.;Ahmed,N.;Mohana,H.P.Deep
LearningforMonitoringAgriculturalDroughtinSouthAsiaUsingRemoteSensingData.RemoteSens.2021,13,1715.[CrossRef]
36. Khan,P.W.;Byun,Y.C.;Park,N.;WaqasKhan,P.;Byun,Y.-C.;Lee,S.-J.;Park,N.MachineLearningBasedHybridSystemfor
ImputationandEfficientEnergyDemandForecasting.Energies2020,13,2681.[CrossRef]

Appl.Sci.2025,15,5957 31of33
37. Liang,Z.;Mao,J.;Lu,K.;Ba,Z.;Li,G.Combiningdeepneuralnetworkandbibliometricindicatorforemergingresearchtopic
prediction.Inf.Process.Manag.2021,58,102611.[CrossRef]
38. Cui,Z.;Qing,X.;Chai,H.;Yang,S.;Zhu,Y.;Wang,F.Real-timerainfall-runoffpredictionusinglightgradientboostingmachine
coupledwithsingularspectrumanalysis.J.Hydrol.2021,603,127124.[CrossRef]
39. Shen,M.;Luo,J.;Cao,Z.;Xue,K.;Qi,T.;Ma,J.;Liu,D.;Song,K.;Feng,L.;Duan,H.Randomforest:Anoptimalchlorophyll-
aalgorithmforopticallycomplexinlandwatersufferingatmosphericcorrectionuncertainties. J.Hydrol. 2022, 615, 128685.
[CrossRef]
40. Teinemaa,I.;Dumas,M.;Leontjeva,A.;Maggi,F.M.Temporalstabilityinpredictiveprocessmonitoring.DataMin.Knowl.Discov.
2018,32,1306–1338.[CrossRef]
41. Kwon,D.H.;Kim,J.B.;Han,Y.H.TimeSeriesClassificationofCryptocurrencyPriceTrendBasedonaRecurrentLSTMNeural
Network.J.Inf.Process.Syst.2019,15,694–706.[CrossRef]
42. Geng,L.;Che,T.;Ma,M.;Tan,J.;Wang,H.CornBiomassEstimationbyIntegratingRemoteSensingandLong-TermObservation
DataBasedonMachineLearningTechniques.RemoteSens.2021,13,2352.[CrossRef]
43. Ngarambe,J.;Irakoze,A.;Yun,G.Y.;Kim,G.ComparativePerformanceofMachineLearningAlgorithmsinthePredictionof
IndoorDaylightIlluminances.Sustainability2020,12,4471.[CrossRef]
44. Seydi,S.T.;Amani,M.;Ghorbanian,A.ADualAttentionConvolutionalNeuralNetworkforCropClassificationUsingTime-Series
Sentinel-2Imagery.RemoteSens.2022,14,498.[CrossRef]
45. Pan,S.;Yang,B.;Wang,S.;Guo,Z.;Wang,L.;Liu,J.;Wu,S.OilwellproductionpredictionbasedonCNN-LSTMmodelwith
self-attentionmechanism.Energy2023,284,128701.[CrossRef]
46. Paudel,D.;deWit,A.;Boogaard,H.;Marcos,D.;Osinga,S.;Athanasiadis,I.N.Interpretabilityofdeeplearningmodelsforcrop
yieldforecasting.Comput.Electron.Agric.2023,206,107663.[CrossRef]
47. Ghimire,S.; Nguyen-Huy,T.; Al-Musaylh,M.S.; Deo,R.C.; Casillas-Pérez,D.; Salcedo-Sanz,S.Anovelapproachbasedon
integrationof convolutional neuralnetworks andecho state networkfor dailyelectricity demand prediction. Energy 2023,
275,127430.[CrossRef]
48. Zhu,X.;Guo,H.;Huang,J.J.;Tian,S.;Zhang,Z.AhybriddecompositionandMachinelearningmodelforforecastingChlorophyll-
aandtotalnitrogenconcentrationincoastalwaters.J.Hydrol.2023,619,129207.[CrossRef]
49. Ravichandran, T.; Gavahi, K.; Ponnambalam, K.; Burtea, V.; Mousavi, S.J. Ensemble-based machine learning approach for
improvedleakdetectioninwatermains.J.Hydroinform.2021,23,307–323.[CrossRef]
50. Li,L.;Dai,S.;Cao,Z.;Hong,J.;Jiang,S.;Yang,K.Usingimprovedgradient-boosteddecisiontreealgorithmbasedonKalman
filter(GBDT-KF)intimeseriesprediction.J.Supercomput.2020,76,6887–6900.[CrossRef]
51. Hewamalage,H.;Bergmeir,C.;Bandara,K.Globalmodelsfortimeseriesforecasting:ASimulationstudy.PatternRecognit.2022,
124,108441.[CrossRef]
52. Li,Y.;Yang,C.;Sun,Y.DynamicTimeFeaturesExpandingandExtractingMethodforPredictionModelofSinteringProcess
QualityIndex.IEEETrans.Ind.Inform.2022,18,1737–1745.[CrossRef]
53. Srivastava,P.R.;Eachempati,P.DeepNeuralNetworkandTimeSeriesApproachforFinanceSystems:PredictingtheMovement
oftheIndianStockMarket.J.Organ.EndUserComput.2021,33,204–226.[CrossRef]
54. Ting,P.Y.;Wada,T.;Chiu,Y.L.;Sun,M.T.;Sakai,K.;Ku,W.S.;Jeng,A.A.K.;Hwu,J.S.FreewayTravelTimePredictionUsingDeep
HybridModel—TakingSunYat-SenFreewayasanExample.IEEETrans.Veh.Technol.2020,69,8257–8266.[CrossRef]
55. Shi,J.;He,G.;Liu,X.AnomalyDetectionforKeyPerformanceIndicatorsThroughMachineLearning.InProceedingsofthe2018
InternationalConferenceonNetworkInfrastructureandDigitalContent(IC-NIDC),Guiyang,China,22–24August2018;pp.1–5.
56. Joseph,R.V.;Mohanty,A.;Tyagi,S.;Mishra,S.;Satapathy,S.K.;Mohanty,S.N.AhybriddeeplearningframeworkwithCNNand
Bi-directionalLSTMforstoreitemdemandforecasting.Comput.Electr.Eng.2022,103,108358.[CrossRef]
57. Safat,W.;Asghar,S.;Gillani,S.A.EmpiricalAnalysisforCrimePredictionandForecastingUsingMachineLearningandDeep
LearningTechniques.IEEEAccess2021,9,70080–70094.[CrossRef]
58. Qiu,H.;Luo,L.;Su,Z.;Zhou,L.;Wang,L.;Chen,Y.Machinelearningapproachestopredictpeakdemanddaysofcardiovascular
admissionsconsideringenvironmentalexposure.BMCMed.Inform.Decis.Mak.2020,20,83.[CrossRef]
59. Ribeiro,A.M.N.C.;doCarmo,P.R.X.;Endo,P.T.;Rosati,P.;Lynn,T.Short-andVeryShort-TermFirm-LevelLoadForecastingfor
Warehouses:AComparisonofMachineLearningandDeepLearningModels.Energies2022,15,750.[CrossRef]
60. Priyadarshi,R.;Panigrahi,A.;Routroy,S.;Garg,G.K.Demandforecastingatretailstageforselectedvegetables:Aperformance
analysis.J.Model.Manag.2019,14,1042–1063.[CrossRef]
61. Chen,H.;Guan,M.;Li,H.AirQualityPredictionBasedonIntegratedDualLSTMModel. IEEEAccess2021,9,93285–93297.
[CrossRef]
62. Ibañez,S.C.;Dajac,C.V.G.;Liponhay,M.P.;Legara,E.F.T.;Esteban,J.M.H.;Monterola,C.P.ForecastingReservoirWaterLevels
UsingDeepNeuralNetworks:ACaseStudyofAngatDaminthePhilippines.Water2022,14,34.[CrossRef]

Appl.Sci.2025,15,5957 32of33
63. PhamHoang,V.;TrinhTan,D.;TieuKhoi,M.;HoangVuong,P.;TanDat,T.;KhoiMai,T.;HoangUyen,P.;TheBao,P.Stock-Price
ForecastingBasedonXGBoostandLSTM.Comput.Syst.Sci.Eng.2022,40,237–246.[CrossRef]
64. Farsi,M.ApplicationofensembleRNNdeepneuralnetworktothefalldetectionthroughIoTenvironment.Alex.Eng.J.2021,60,
199–211.[CrossRef]
65. Nan,S.;Tu,R.;Li,T.;Sun,J.;Chen,H.Fromdrivingbehaviortoenergyconsumption: Anovelmethodtopredicttheenergy
consumptionofelectricbus.Energy2022,261,125188.[CrossRef]
66. Comert,G.;Khan,Z.;Rahman,M.;Chowdhury,M.Greymodelsforshort-termqueuelengthpredictionsforadaptivetraffic
signalcontrol.ExpertSyst.Appl.2021,185,115618.[CrossRef]
67. Liu,S.;Zeng,A.;Lau,K.;Ren,C.;Chan,P.-w.;Ng,E.Predictinglong-termmonthlyelectricitydemandunderfutureclimaticand
socioeconomicchangesusingdata-drivenmethods:AcasestudyofHongKong.Sustain.CitiesSoc.2021,70,102936.[CrossRef]
68. Abdikan,S.;Sekertekin,A.;Narin,O.G.;Delen,A.;BalikSanli,F.AcomparativeanalysisofSLR,MLR,ANN,XGBoostandCNN
forcropheightestimationofsunflowerusingSentinel-1andSentinel-2.Adv.SpaceRes.2023,71,3045–3059.[CrossRef]
69. Phan,Q.T.;Wu,Y.K.;Phan,Q.D.;Lo,H.Y.ANovelForecastingModelforSolarPowerGenerationbyaDeepLearningFramework
withDataPreprocessingandPostprocessing.IEEETrans.Ind.Appl.2023,59,220–231.[CrossRef]
70. Guan,S.;Wang,Y.;Liu,L.;Gao,J.;Xu,Z.;Kan,S.Ultra-short-termwindpowerpredictionmethodbasedonFTI-VACA-XGB
model.ExpertSyst.Appl.2024,235,121185.[CrossRef]
71. Wang,X.; Li,Y.; Qiao,Q.; Tavares,A.; Liang,Y.WaterQualityPredictionBasedonMachineLearningandComprehensive
WeightingMethods.Entropy2023,25,1186.[CrossRef]
72. Li, Z.; Ma, E.; Lai, J.; Su, X.Tunneldeformationpredictionduringconstruction: Anexplainablehybridmodelconsidering
temporalandstaticfactors.Comput.Struct.2024,294,107276.[CrossRef]
73. Pavlov-Kagadejev,M.;Jovanovic,L.;Bacanin,N.;Deveci,M.;Zivkovic,M.;Tuba,M.;Strumberger,I.;Pedrycz,W.Optimizing
long-short-termmemorymodelsviametaheuristicsfordecompositionaidedwindenergygenerationforecasting.Artif.Intell.
Rev.2024,57,45.[CrossRef]
74. Zrira,N.;Kamal-Idrissi,A.;Farssi,R.;Khan,H.A.TimeseriespredictionofseasurfacetemperaturebasedonBiLSTMmodelwith
attentionmechanism.J.SeaRes.2024,198,102472.[CrossRef]
75. Mangukiya,N.K.;Sharma,A.Alternatepathwayforregionalfloodfrequencyanalysisindata-sparseregion. J.Hydrol. 2024,
629,130635.[CrossRef]
76. Zhang,L.;Wang,C.;Hu,W.;Wang,X.;Wang,H.;Sun,X.;Ren,W.;Feng,Y.Dynamicreal-timeforecastingtechniqueforreclaimed
watervolumesinurbanriverenvironmentalmanagement.Environ.Res.2024,248,118267.[CrossRef]
77. Zhao,Z.-h.;Wang,Q.;Shao,C.-s.;Chen,N.;Liu,X.-y.;Wang,G.-b.Astatedetectionmethodofoffshorewindturbines’gearbox
bearingbasedonthetransformerandGRU.Meas.Sci.Technol.2024,35,025903.[CrossRef]
78. Singh, R.B.; Patra, K.C.; Samantra, A.; Singh, R.B.; Patra, K.C.; Pradhan, B.; Samantra, A.HDTO-DeepAR:Anovelhybrid
approachtoforecastsurfacewaterqualityindicators.J.Environ.Manag.2024,352,120091.[CrossRef]
79. Inbar,O.;Avisar,D.Enhancingwastewatertreatmentthroughartificialintelligence:Acomprehensivestudyonnutrientremoval
andeffluentqualityprediction.J.WaterProcessEng.2024,61,105212.[CrossRef]
80. Oyucu,S.;Dümen,S.;Duru,I˙.;Aksöz,A.;Biçer,E.DischargeCapacityEstimationforLi-IonBatteries:AComparativeStudy.
Symmetry2024,16,436.[CrossRef]
81. Saravanan,K.S.;Bhagavathiappan,V.PredictionofcropyieldinIndiausingmachinelearningandhybriddeeplearningmodels.
ActaGeophys.2024,72,4613–4632.[CrossRef]
82. Chen,T.; Guestrin,C.XGBoost: AScalableTreeBoostingSystem. InProceedingsofthe22ndACMSIGKDDInternational
ConferenceonKnowledgeDiscoveryandDataMining,SanFrancisco,CA,USA,13–17August2016;pp.785–794.
83. Ke,G.;Meng,Q.;Finley,T.;Wang,T.;Chen,W.;Ma,W.;Ye,Q.;Liu,T.-Y.LightGBM:Ahighlyefficientgradientboostingdecision
tree.InProceedingsofthe31stInternationalConferenceonNeuralInformationProcessingSystems,LongBeach,CA,USA,4–9
December2017;pp.3149–3157.
84. Prokhorenkova,L.;Gusev,G.;Vorobev,A.;Dorogush,A.V.;Gulin,A.CatBoost: Unbiasedboostingwithcategoricalfeatures.
InProceedingsofthe32ndInternationalConferenceonNeuralInformationProcessingSystems,Montréal,QC,Canada,3–8
December2018;pp.6639–6649.
85. Svozil,D.;Kvasnicka,V.;Pospichal,J.í.Introductiontomulti-layerfeed-forwardneuralnetworks.Chemom.Intell.Lab.Syst.1997,
39,43–62.[CrossRef]
86. Gu, J.; Wang, Z.; Kuen, J.; Ma, L.; Shahroudy, A.; Shuai, B.; Liu, T.; Wang, X.; Wang, G.; Cai, J.; et al. Recent advances in
convolutionalneuralnetworks.PatternRecognit.2018,77,354–377.[CrossRef]
87. Sherstinsky,A.FundamentalsofRecurrentNeuralNetwork(RNN)andLongShort-TermMemory(LSTM)network.Phys.D
NonlinearPhenom.2020,404,132306.[CrossRef]

Appl.Sci.2025,15,5957 33of33
88. Vaswani,A.;Shazeer,N.;Parmar,N.;Uszkoreit,J.;Jones,L.;Gomez,A.N.;Kaiser,Ł.;Polosukhin,I.Attentionisallyouneed.
InProceedingsofthe31stInternationalConferenceonNeuralInformationProcessingSystems,LongBeach,CA,USA,4–9
December2017;pp.6000–6010.
89. Yu,Z.;He,X.;Montillet,J.-P.;Wang,S.;Hu,S.;Sun,X.;Huang,J.;Ma,X.AnimprovedICEEMDAN-MPA-GRUmodelforGNSS
heighttimeseriespredictionwithweightedqualityevaluationindex.GPSSolut.2025,29,113.[CrossRef]
90. Makridakis,S.;Spiliotis,E.;Assimakopoulos,V.M5accuracycompetition: Results,findings,andconclusions. Int. J.Forecast.
2022,38,1346–1364.[CrossRef]
91. Makridakis,S.;Spiliotis,E.;Assimakopoulos,V.;Chen,Z.;Gaba,A.;Tsetlin,I.;Winkler,R.L.TheM5uncertaintycompetition:
Results,findingsandconclusions.Int.J.Forecast.2022,38,1365–1385.[CrossRef]
92. Makridakis,S.;Spiliotis,E.;Hollyman,R.;Petropoulos,F.;Swanson,N.;Gaba,A.TheM6ForecastingCompetition:Bridgingthe
GapBetweenForecastingandInvestmentDecisions.Int.J.Forecast.2024,inpress.[CrossRef]
93. Woo,G.;Liu,C.;Kumar,A.;Xiong,C.;Savarese,S.;Sahoo,D.Unifiedtrainingofuniversaltimeseriesforecastingtransformers.
InProceedingsofthe41stInternationalConferenceonMachineLearning,Vienna,Austria,21–27July2024;p.2178.
94. Lin,L.;Li,Z.;Li,R.;Li,X.;Gao,J.Diffusionmodelsfortime-seriesapplications:Asurvey.Front.Inf.Technol.Electron.Eng.2024,
25,19–41.[CrossRef]
95. Oh,Y.;Kam,S.;Lee,J.;Lim,D.-Y.;Kim,S.;Bui,A.ComprehensiveReviewofNeuralDifferentialEquationsforTimeSeries
Analysis.arXiv2025.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.