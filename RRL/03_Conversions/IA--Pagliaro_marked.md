Review
Artificial Intelligence vs. Efficient Markets: A Critical
Reassessment of Predictive Models in the Big Data Era
AntonioPagliaro1,2,3
1 INAFIASFPalermo,ViaUgoLaMalfa,153,I-90146Palermo,Italy;antonio.pagliaro@inaf.it
2 IstitutoNazionalediFisicaNucleareSezionediCatania,ViaSantaSofia,64,I-95123Catania,Italy
3 ICSC—CentroNazionalediRicercainHPC,BigDataeQuantumComputing,I-40121Bologna,Italy
Abstract: Thispapercriticallyexaminesartificialintelligenceapplicationsinstockmar-
ketforecasting,addressingsignificantgapsintheexistingliteraturethatoftenoverlook
thetensionbetweentheoreticalmarketefficiencyandempiricalpredictability. Whilenu-
merousreviewscatalogmethodologies,theyfrequentlyfailtorigorouslyevaluatemodel
performanceacrossdifferentmarketregimesorreconcilestatisticalsignificancewitheco-
nomic relevance. We analyze techniques ranging from traditional statistical models to
advanceddeeplearningarchitectures,findingthatensemblemethodslikeExtraTrees,Ran-
domForest,andXGBoostconsistentlyoutperformsingleclassifiers,achievingdirectional
accuracyofupto86%inspecificmarketconditions. Ouranalysisrevealsthathybridap-
proachesintegratingmultipledatasourcesdemonstratesuperiorperformancebycapturing
complementarymarketsignals,yetmanymodelsshowingstatisticalsignificancefailto
generate economic value after accounting for transaction costs and market impact. By
addressingmethodologicalchallengesincludingbacktestoverfitting,regimechanges,and
implementationconstraints,weprovideanovelcomprehensiveframeworkforrigorous
modelassessmentthatbridgesthedividebetweenacademicresearchandpracticalimple-
mentation. Thisreviewmakesthreekeycontributions: (1)areconciliationoftheEfficient
MarketHypothesiswithAI-drivenpredictabilitythroughanadaptivemarketframework,
(2)amulti-dimensionalevaluationmethodologythatextendsbeyondclassificationaccu-
racytofinancialperformance,and(3)anidentificationofpromisingresearchdirectionsin
explainableAI,transferlearning,causalmodeling,andprivacy-preservingtechniquesthat
AcademicEditors:JinwenLiangand addresscurrentlimitations.
JixinZhang
Keywords: stockmarketprediction;machinelearning;deeplearning;artificialintelligence;
Received:19March2025
Revised:17April2025 technicalanalysis;fundamentalanalysis;sentimentanalysis
Accepted:21April2025
Published:23April2025
Citation: Pagliaro,A.Artificial
1. Introduction
Intelligencevs.EfficientMarkets:A
CriticalReassessmentofPredictive
The debate on the predictability of financial markets remains one of the most con-
ModelsintheBigDataEra.Electronics
troversial in economics. While the Efficient Market Hypothesis (EMH) maintains that
2025,14,1721. https://doi.org/
marketmovementsshouldbetheoreticallyunpredictablesinceallavailableinformation
10.3390/electronics14091721
isalreadyreflectedinassetprices,theemergenceofincreasinglysophisticatedartificial
Copyright:©2025bytheauthor.
intelligencemodelshasreopenedthisfundamentaldebate. Thecentralthesisofthisreview
LicenseeMDPI,Basel,Switzerland.
isthattheinteractionbetweenadvancedAItechniquesandfinancialmarketsrepresents
Thisarticleisanopenaccessarticle
distributedunderthetermsand notmerelyanincrementalimprovementovertraditionalmethodsbutaparadigmshiftin
conditionsoftheCreativeCommons ourunderstandingofmarketdynamicsandpredictability.
Attribution(CCBY)license Thisparadigmshiftemergesfromthreekeydevelopments: First,modernAIsystems
(https://creativecommons.org/
can detect complex, non-linear patterns in high-dimensional financial data that remain
licenses/by/4.0/).
Electronics2025,14,1721 https://doi.org/10.3390/electronics14091721

Electronics2025,14,1721 2of48
invisibletoconventionalstatisticalapproachesandhumananalysts.Second,theintegration
ofdiversedatamodalities—frompriceactionandfinancialstatementstosentimentanalysis
andalternativedatasources—createsamultidimensionalperspectivethattranscendsthe
limitationsofanysingleinformationstream. Third,theadaptivenatureofmodernlearning
algorithmsenablesthemtoevolvealongsidemarkets,potentiallymaintainingpredictive
powerevenasmarketparticipantsincorporatenewinformation.
Despitetheproliferationoffinancialpredictionmodels,significantlimitationsper-
sistinexistingapproaches. Traditionalstatisticalmethodsoftenrelyonassumptionsof
linearityandstationaritythatpoorlymatchfinancialmarketreality,whilemanymachine
learning applications focus excessively on predictive accuracy without addressing eco-
nomic implementation constraints. The disconnect between statistical significance and
economicrelevancerepresentsacriticalgapincurrentresearch,withnumerousstudies
reportingimpressiveclassificationmetricsthatfailtotranslateintoprofitablestrategies
afteraccountingfortransactioncosts,marketimpact,andregimechanges.
Existingreviewshaveprimarilyfocusedonthetaxonomicclassificationofmethods,of-
feringencyclopedicinventoriesoftechniqueswithoutcriticalevaluationoftheirreal-world
viability. Suchreviewstypicallyneglectthreecrucialdimensions: (1)rigorouscross-regime
evaluationtoassessmodelconsistencyacrossdifferentmarketconditions,(2)comprehen-
siveperformanceassessmentbeyondmereclassificationmetrics,and(3)reconciliationof
empiricalpredictabilitywiththeoreticalmarketefficiencyprinciples. Thisreviewaddresses
thesespecificlimitationsbydevelopinganintegratedevaluationframeworkthatbridges
theoretical and practical considerations while providing a coherent explanation for the
apparentcontradictionbetweenmarketefficiencytheoryanddocumentedAIpredictability.
Thepracticalsignificanceofthisshiftextendsbeyondacademicinterest.Evenmarginal
improvementsinforecastaccuracycantranslateintosubstantialfinancialgainswhenap-
pliedatscale. Amere1%improvementindirectionalaccuracy,whenimplementedacross
alargeinvestmentportfoliowithappropriateriskmanagement,cangeneratesignificant
alphawhilemaintainingreasonableriskparameters. Thisexplainswhybothacademicre-
searchersandcommercialentitieshaveacceleratedtheirexplorationofAI-drivenprediction
techniquesdespitetheoreticalobjectionsbasedonmarketefficiency.
It is crucial to distinguish between two fundamental aspects of prediction model
evaluation: statisticalperformance(measuredthroughmetricslikedirectionalaccuracy,
precision,andrecall)andeconomicperformance(evaluatedviafinancialmetricssuchas
Sharperatio,realizedreturns,andmaximumdrawdown). Whilestatisticalmetricsprovide
insights into a model’s classification capabilities, they do not necessarily translate into
economicvalueafteraccountingfortransactioncosts,marketimpact,executionslippage,
andotherreal-worldconstraints. Throughoutthisreview,wecarefullydifferentiatebe-
tweenthesetwoevaluationdimensions,asmodelswithimpressivestatisticalperformance
frequentlyfailtodelivermeaningfuleconomicvalueinpracticalimplementation.
This review systematically evaluates the current state of AI applications in stock
market forecasting through a critical lens that recognizes both their potential and their
limitations. Unlikepreviousstudiesthathavefocusedprimarilyonmethodologicaltax-
onomies,weorganizeouranalysisaroundthefundamentaltensionbetweenincreasing
model complexity and demonstrable financial performance. We evaluate methods not
merelyontheirstatisticalmetricsbutontheirabilitytogenerateconsistentreturnsafter
accountingfortransactioncosts,marketimpact,andchangingmarketregimes.
Thepaperisstructuredasfollows: Section2examinesthetheoreticalfoundationsand
historicalevolutionofpredictivemodels,highlightingthelimitationsoflineareconometric
approachesandthetheoreticalbasisforneuralnetworkapplications. Section3presents
a comprehensive taxonomy of prediction techniques spanning statistical methods, pat-

Electronics2025,14,1721 3of48
ternrecognition,machinelearningmodels,andsentimentanalysis. Sections4–7analyze
each major category in depth, with particular attention to their empirical performance
acrossdifferentmarketsandtimeperiods. Section8exploreshybridandadvancedap-
proachesthatcombinemultiplemethodologies. Section9addressesthecriticalissueof
evaluationmethodologies,emphasizingtheimportanceofproperperformanceassessment
beyondsimpleaccuracymetrics. Section10confrontsthechallengesandlimitationsfac-
ingAI-basedpredictionmodels,includingtheoreticalconstraints,methodologicalissues,
andimplementationbarriers. Finally,Section11outlinespromisingdirectionsforfuture
research,suggestingpathwaystowardmorerobust,interpretable,andpracticallyvaluable
predictionsystems. AsillustratedinFigure1,thevariousAIapproachestotheprediction
of the stock market are deeply interconnected, with hybrid methods in the center that
integratemultipletechniques.
Figure1.InterrelationsofAImethodsinstockmarketprediction.Thediagramillustratestheconnec-
tionsbetweentraditionalMLapproaches,deeplearning,causalmodels,statisticalmethods,pattern
recognition,sentimentanalysis,graphneuralnetworks,andreinforcementlearning,withhybrid
approachesatthecenterintegratingmultiplemethodologies.
ThecentralobjectiveofthisworkistoprovideacriticalevaluationofAIapplications
instockmarketforecasting,addressingthefollowingspecificresearchquestions:
1. Howdoensemblemethodscomparetosingleclassifiersinstockmarketprediction
acrossdifferentmarketconditionsandtimehorizons?

Electronics2025,14,1721
4of48
2. To what extent do hybrid approaches integrating multiple data sources improve
predictiveperformancecomparedtosingle-sourcemodels?
3. HowcantheapparentcontradictionbetweentheEfficientMarketHypothesisand
empirical evidence of AI-driven predictability be reconciled through an adaptive
marketframework?
4. Whatevaluationframeworkbestcapturesbothstatisticalsignificanceandeconomic
relevanceinassessingpredictionmodels?
Byaddressingthesequestions,weaimtoprovideresearchersandpractitionerswitha
comprehensiveunderstandingofthestrengths,limitations,andpracticalapplicationsof
variousAI-basedstockpredictionmethodologies.
2. TheoreticalFoundationsandHistoricalEvolutionofPredictiveModels
2.1. LimitationsofLinearEconometricModels
TraditionalfinancialeconometricsreliesheavilyonlinearmodelsliketheAutoregres-
siveMovingAverage(ARMA),expressedas
|        | p   |          | q         |     |
| ------ | --- | -------- | --------- | --- |
|        | ∑   |          | ∑         |     |
| X = c+ | ϕ   | X t−i +ϵ | + θ ϵ t−i | (1) |
| t      | i   |          | t i       |     |
|        | i=1 |          | i=1       |     |
whereϕ andθ representautoregressiveandmovingaveragecoefficients,respectively.This
i i
formulationmakesseveralcriticalassumptionsthatareoftenviolatedinfinancialmarkets.
Mostimportantly,ARMAmodelsassumestationarity,wherethestatisticalpropertiesof
thetimeseries(mean,variance,andautocorrelation)remainconstantovertime. Financial
time series are frequently non-stationary, exhibiting trends, seasonality, and structural
breaks. Toaddressthislimitation,theIntegrated(I)componentinARIMAmodelsapplies
differencingoperations(∆X
| = X −X |     | )totransformnon-stationarydataintostationary |     |     |
| ------ | --- | -------------------------------------------- | --- | --- |
| t t    | t−1 |                                              |     |     |
processesbeforeapplyingARMAmodeling. Evenwithsuchadjustments,however,these
modelsexhibitcriticallimitationswhenappliedtomodernfinancialmarkets.
• Nonlinear Dynamics: ARMA fails to capture asymmetric volatility clustering ob-
servedinS&P500returns,wherenegativeshocksinduce43%greatervolatilitypersis-
tencethanpositiveshocks[1]. Thisviolatestheassumptionoflinearshockresponse.
• High-Dimensional Interactions: The 2010 Flash Crash demonstrated cross-asset
correlationjumpsexceeding0.8withinminutes,aphenomenonunmodelablethrough
pairwiselinearcoefficients[2].
2.2. NeuralNetworkParadigmShift
Theuniversalapproximationtheoremformalizedby[3]establishedthatfeed-forward
networkswithasinglehiddenlayercanapproximateanyBorelmeasurablefunctiontothe
desiredaccuracy,providingthetheoreticalbasisforfinancialapplications:
|     | (cid:32) |     | (cid:33) |     |
| --- | -------- | --- | -------- | --- |
∑ n
| f(x) | = ϕ | w   | ·x +b | (2) |
| ---- | --- | --- | ----- | --- |
|      |     | i   | i     |     |
i=1
whereϕisanonlinearactivationfunction. Empiricalvalidationcamefroma2007NYSE
studyshowingthree-layerMLPsthatreduceMSEpredictionoftheovernightgapby62%
versusGARCHmodels[4].
RecurrentArchitecturesforTemporalDependencies
SimpleRNNsintroducedmemorythroughhiddenstaterecursion:
| = σ(W |      | +W  | +b )     |     |
| ----- | ---- | --- | -------- | --- |
| h t   | hh h | t−1 | xh x t h | (3) |

Electronics2025,14,1721
5of48
where,intraditionalRNNarchitectures,σistypicallythehyperbolictangent(tanh)activa-
tionfunctionratherthanthelogisticsigmoid. Thetanhfunctionispreferableforhidden
stateupdatesasitproduceszero-centeredoutputsintherange[−1,1],helpingtomitigate
vanishinggradientissuescomparedtothelogisticsigmoidfunction,whichoutputsinthe
rangeof [0,1] andcanleadtoconsistentlypositiveactivationsthatexacerbategradient
vanishing problems when processing long sequences [5]. The severity of this gradient
vanishingproblemdependsonseveralfactorsincludinginputdatacharacteristics,network
architecture,andhyperparametersettings,withthepracticalsequencelengthlimitvarying
fromdozenstohundredsofstepsdependingontheapplicationdomain. LSTMnetworks
solvedthisthroughgatedmemorycells:
| f = σ(W       | ·[h       | ,x ]+b   | ) (ForgetGate)   | (4) |
| ------------- | --------- | -------- | ---------------- | --- |
| t             | f t−1     | t        | f                |     |
| = σ(W         | ·[h       | ]+b      | )                |     |
| i t           | i t−1     | ,x t     | i (InputGate)    | (5) |
| C˜ =tanh(W    | ·[h       | ,x       | ]+b )            | (6) |
| t             | C         | t−1 t    | C                |     |
| C = f ◦C      | +i        | ◦C˜      | (CellState)      | (7) |
| t t           | t−1       | t t      |                  |     |
| o t = σ(W     | o ·[h t−1 | ,x t ]+b | o ) (OutputGate) | (8) |
| h = o ◦tanh(C |           | )        |                  | (9) |
| t t           |           | t        |                  |     |
Applications to DAX index futures demonstrated accuracy of 82% in 10 min interval
predictionsusing512-unitbidirectionalLSTMs[6].
2.3. ModernRegularizationTechniques
Deepnetworks’propensitytooverfitfinancialnoisenecessitatedadvancedregularization:
• TemporalDropout: Therandommaskingofsequenceelementsduringtrainingim-
provedtheNASDAQ-100predictionSharperatioby0.47[7].
• CurriculumLearning: Phasedtrainingfromdailytotick-leveldataenhancedS&P500
volatilityforecasting,witha33%RMSEreduction[8].
• BayesianHyperparameterOptimization: Tree-structuredParzenEstimators(TPEs)
optimized LSTM layers on crude oil futures, achieving 19% lower MAE than grid
search[9].
AttentionMechanisms
Transformerarchitecturesrevolutionizedsequencemodelingthroughself-attention:
(cid:18) QKT(cid:19)
| Attention(Q,K,V) |     | =softmax | √ V | (10) |
| ---------------- | --- | -------- | --- | ---- |
d
k
whereQ,K,andV representquery,key,andvaluematrices. AppliedtoFOREXmarkets,
Vaswanietal.[10]demonstratedthattransformer-basedmodelswithmultiheadattention
mechanismsachieveda57%reductioninpredictionlatencycomparedtoLSTMnetworks
while simultaneously maintaining comparable predictive performance (89% precision).
Thissignificantcomputationalefficiencyimprovementwasachievedthroughthetransform-
ers’inherentlyparallelizablearchitecture,whicheliminatesthesequentialcomputation
requirements of recurrent models, allowing for faster inference without compromising
predictivequality[10].
2.4. CriticalAssessmentofPriorResearch
Previoussurveysonfinancialpredictionmodelshaveoftenfocusedonthetaxonomic
classificationofmethodsratherthancriticalevaluationsoftheirreal-worldapplicability.
Forinstance,studiesbySezeretal.[11],Henriqueetal.[12]categorizedtechniquescompre-

Electronics2025,14,1721 6of48
hensivelybutfailedtoaddressfundamentallimitationsintheirevaluationmethodologies,
particularlyregardingproperstatisticalvalidationandeconomicsignificancetesting.
Severalcriticallimitationspervadetheexistingliterature.First,manystudiesreportim-
pressiveclassificationaccuracywithoutdemonstratingcorrespondingeconomicvalueafterac-
countingfortransactioncosts,slippage,andmarketimpact.Fernández-Rodríguezetal.[13]
demonstratedthatmanypublishedneuralnetworkapproachesshowingstatisticalsignifi-
cancefailedtomaintainprofitabilitywhenrealistictradingfrictionswereincorporated.
Second,methodologicalweaknessesinvalidationproceduresarecommon,withmany
studiesemployingstandardk-foldcross-validationwithoutaccountingfortemporaldepen-
denciesinfinancialdata,leadingtoinformationleakageandoverlyoptimisticperformance
estimates. López de Prado [14] highlighted how this methodological error has led to
numerousfalsediscoveriesinthefinancialmachinelearningliterature.
Third,thereconciliationofpredictivefindingswithmarketefficiencytheoriesremains
inadequateinmostresearch. Studiesoftenreportpredictabilitywithoutaddressingthe
theoretical implications for market efficiency or providing mechanisms through which
theirfindingscoexistwithsemi-strongefficiency. Thistheoreticaldisconnectionlimitsthe
integrationofmachinelearningadvancesintofinancialtheory.
3. TaxonomyofStockMarketPredictionTechniques
Stockmarketpredictiontechniquescanbebroadlyclassifiedintofourmaincategories:
statisticalapproaches,patternrecognitionmethods,machinelearningmodels,andsenti-
mentanalysis.
3.1. StatisticalApproaches
Statisticalmethodsrepresenttheearliestcomputationalapproachestostockprediction.
Thesetechniquesfocusonidentifyingstatisticalrelationshipsandpatternsinhistorical
pricedata. Commonstatisticalmodelsincludethefollowing:
• AutoregressiveIntegratedMovingAverage(ARIMA):Thesemodelscombineau-
toregressive(AR)components, whichcapturethemomentumandmeanreversion
effects in trading markets, with moving average (MA) components, which model
shockeffectsintimeseries.
• ExponentialSmoothingModel(ESM):Thistechniqueappliesanexponentialwin-
dowfunctiontotimeseriesdata, givinggreaterweighttorecentobservationsand
progressivelylessweighttoolderdatapoints.
• Generalized Autoregressive Conditional Heteroskedastic (GARCH): This model
specificallyaddressesthevolatilityclusteringobservedinfinancialtimeseries,where
periodsofhighvolatilitytendtoclustertogether.
Whilestatisticalmodelsofferinterpretabilityandtheoreticalgrounding,theyoften
assumelinearity,stationarity,andnormalityinthedata—assumptionsthatfrequentlydo
notholdinthecomplex,nonlineardomainoffinancialmarkets.
3.2. PatternRecognitionMethods
Patternrecognitionapproachesfocusonidentifyingrecurringvisualpatternsinstock
pricecharts. Thesemethodsinclude:
• PerceptuallyImportantPoints(PIP):Thistechniquereducestimeseriesdimensions
bypreservingsalientpoints,allowingformoreefficientpatternidentification.
• TemplateMatching: Thisapproachmatchespatternsincurrentstockdatawithhistor-
icalpatternsthatprecededspecificmarketmovements.

Electronics2025,14,1721 7of48
• ChartPatternRecognition: Thesemethodsidentifyfamiliarchartpatternslikegaps,
spikes,flags,pennants,wedges,saucers,triangles,andhead-and-shoulderformations
thattechnicalanalystsbelievehavepredictivevalue.
Patternrecognitionmethodsareparticularlyalignedwithtechnicalanalysis,whichhas
alonghistoryinfinancialforecasting. However,theireffectivenessremainscontroversial
amongacademicresearchers.
3.3. MachineLearningModels
Machinelearningapproacheshavebecomeincreasinglydominantinstockforecasting
research. These methods can be divided into supervised and unsupervised learning
techniques.
3.3.1. SupervisedLearningMethods
• SupportVectorMachines(SVMs): Thesealgorithmsdefineoptimalhyperplanesfor
separatingdataintodifferentclasses.
• DecisionTreesandRandomForests: Tree-basedalgorithmsthatcreatehierarchical
decisionstructuresbasedonfeaturevalues.
• ArtificialNeuralNetworks(ANNs): Computationalmodelsinspiredbythestructure
ofbiologicalneuralnetworks.
• DeepLearningModels: MorecomplexneuralnetworkarchitecturesincludingCon-
volutionalNeuralNetworks(CNNs),RecurrentNeuralNetworks(RNNs),andLong
Short-TermMemory(LSTM)networks.
• Gradient-Boosting Methods: Techniques like XGBoost and AdaBoost that create
strongpredictivemodelsbycombiningmultipleweaklearners.
3.3.2. UnsupervisedLearningMethods
• K-meansClustering: Groupsdatapointsintoclustersbasedonsimilarity.
• HierarchicalClustering: Createsahierarchyofclustersusingeitheragglomerativeor
divisiveapproaches.
• Principal Component Analysis (PCA): Reduces dimensionality while preserving
datavariance.
Machinelearningmodelsareparticularlyvaluableforcapturingnonlinearrelation-
shipsandcomplexpatternsinfinancialdatawithoutrequiringexplicittheoreticalmodels.
3.4. SentimentAnalysis
Sentimentanalysisapproachesleveragetextdatafromnewsarticles, socialmedia,
companyreports,andothertextualsourcestogaugemarketsentiment:
• Lexicon-BasedMethods: Usepredefineddictionariestoassessthesentimentofwords
andphrases.
• MachineLearning-BasedSentimentAnalysis: Employssupervisedlearningtoclas-
sifytextsentiment.
• DeepLearningforSentimentAnalysis: Utilizesneuralnetworkarchitectureslike
BERT(BidirectionalEncoderRepresentationsfromTransformers)formorenuanced
sentimentanalysis.
Sentimentanalysisprovidesawaytoincorporatequalitativeinformationandmarket
psychologyintoquantitativepredictionmodels,potentiallyaddressingfactorsnotcaptured
inpriceandvolumedataalone.
Figure 2 demonstrates the typical data flow in modern stock prediction systems,
highlightingtheprogressionfromdiversedatasourcesthroughvariousprocessingstages
tofinaldecisionsupport.

Electronics2025,14,1721 8of48
Figure2.Dataflowinmodernstockpredictionsystems.Thepipelinedemonstratestheprogression
from diverse data sources through preprocessing and feature engineering to various modeling
approaches,followedbyevaluationanddecisionsupportsystems.Keyperformanceimpactfactors
arehighlightedatthebottomofthediagram.
4. StatisticalApproachesinStockMarketPrediction
Statisticalmodelshavelongservedasthefoundationforquantitativeanalysisinfinan-
cialmarkets. DespitetheemergenceofmorecomplexAImethods,statisticalapproaches
retainvaluefortheirinterpretabilityandcomputationalefficiency.
4.1. ARIMAModels
ARIMA models remain widely used for time series forecasting in finance. These
modelsintegrateautoregressive(AR)components,differencingtoachievestationarity(I),
andmovingaverage(MA)components. StudiesbyAriyoetal.[15]demonstratedthat
ARIMAmodelscanstillcompeteeffectivelywithnewerforecastingtechniques,particularly
forshort-termprediction. Devietal.[16]appliedARIMAtopredicttheNifty50Index,
findingthatthisapproachprovidedreliableforecastswithrelativelylowerrorandvolatility.
KeyadvantagesofARIMAmodelsincludetheirabilitytocaptureshort-termdepen-
denciesindataandtheirtheoreticalfoundationintimeseriesanalysis.However,limitations
includetheirassumptionoflinearityanddifficultyinmodelinglonger-termdependencies.
Moreover,ARIMAmodelsmaystrugglewithfinancialtimeseriesthatexhibitvolatility
clusteringorothercomplex,non-stationarybehaviors.

Electronics2025,14,1721 9of48
4.2. ExponentialSmoothingMethods
Exponential smoothing methods apply weighted averages to time series data,
withweightsdecreasingexponentiallyasobservationsage. DeFariaetal.[17]compared
adaptive exponential smoothing models with neural networks for predicting Brazilian
stockindices,findingcomparableperformancebetweenthetwoapproaches.
Exponential smoothing is particularly valuable for data with seasonal patterns or
trends,anditcanadaptquicklytochangesintheunderlyingdata. However,likeARIMA,
traditionalexponentialsmoothingmethodsmaystrugglewithcomplex,nonlinearpatterns
infinancialdata.
4.3. RegressionModels
Variousregressionmodelshavebeenappliedtostockprediction. Bhuriyaetal.[18]
comparedlinear,polynomial,andRadialBasisFunction(RBF)regressionmodelsforpre-
dictingstockprices,findingthatlinearregressionoutperformedotherregressiontechniques
intheirstudy.
Duttaetal.[19]tookaninnovativeapproachbyusinglogisticregressionwithfinan-
cialratiosasindependentvariablestoclassifycompaniesas“good”or“poor”basedon
their one-year performance. This approach achieved a classification accuracy of 74.6%,
highlightingthevalueoffundamentalanalysisinstockprediction.
4.4. LimitationsofStatisticalApproaches
Whilestatisticalmethodsofferstrongtheoreticalfoundationsandinterpretability,they
faceseveralkeylimitationsinstockmarketprediction:
• LinearityAssumptions:Manystatisticalmethodsassumelinearrelationshipsbetween
variables,whereasstockmarketsfrequentlyexhibitnonlineardynamics.
• StationarityRequirements: ModelslikeARIMArequiredatatobestationary,butfi-
nancialtimeseriesoftendisplaychangingstatisticalpropertiesovertime.
• DifficultywithExogenousVariables: Traditionaltimeseriesmodelsmaystruggleto
incorporateexternalfactorssuchasnewseventsorbroadereconomicindicators.
• LimitedCapabilityforPatternRecognition: Statisticalmodelstypicallycannotcap-
turecomplexvisualpatternsthattechnicalanalystsidentifyinpricecharts.
Theselimitationshavemotivatedthedevelopmentofmoreflexiblemachinelearning
approachesthatcanbetteraddressthecomplexitiesoffinancialmarkets.
4.5. DataConsiderationsAcrossPredictionStudies
Thequality,scope,andprocessingofinputdatafundamentallydeterminetheperfor-
manceofstockpredictionmodels. Thissectionexaminesthedataconsiderationsacrossthe
literature,highlightingbestpracticesandchallenges.
4.5.1. CommonDataSources
Predictionstudiesemploydiversedatasourcesthatcanbecategorizedasfollows:
• MarketData: Themostcommonlyuseddatasourceincludeshistoricalpriceandvol-
umeinformation,typicallyatdailyorintradayfrequencies. Studieslike[6]employed
minute-leveldataforS&P500constituents,whileotherslike[20]utilizedtick-by-tick
dataforhigh-frequencyprediction.
• FundamentalData: Financialstatements,earningsreports,andaccountingmetrics
provideinputsforfundamentalanalysis. Duttaetal.[19]extractedfinancialratios
fromquarterlyreportstoclassifystocks,while[21]combinedfundamentalmetrics
withtechnicalindicators.

Electronics2025,14,1721 10of48
• NewsandSocialMedia:Textualdatafromfinancialnews,socialmedia,andcompany
announcementshasgainedprominence. Bollenetal.[22]analyzed10milliontweets
topredictDJIAmovements,whileDingetal.[23]processedfinancialnewstoextract
eventembeddingsforprediction.
• Alternative Data: Increasingly, studies incorporate non-traditional data sources.
Zhangetal.[24]utilizedweatherdatatopredictenergycommodityprices.
4.5.2. PreprocessingApproaches
Datapreprocessingsignificantlyimpactsmodelperformanceandtypicallyinvolves
thefollowing:
• CleaningandNormalization: Financialtimeseriesoftencontainmissingvaluesand
outliersandrequirenormalization. Commonapproachesincludez-scorestandard-
ization,min–maxscaling,andmissingvalueimputationusingmethodslikeforward
fillingorMICE(MultipleImputationbyChainedEquations).
• Feature Engineering: Raw financial data are transformed into predictive features.
Technicalindicators(e.g.,RSI,MACD,BollingerBands)arecommonlyderivedfrom
price data. Hu et al. [25] created Google Trends indicators by calculating search
intensitychanges,whileChenandChen[26]identifiedperceptuallyimportantpoints
inpriceseriestoreducedimensionality.
• DimensionalityReduction: Giventhehigh-dimensionalnatureoffinancialdata,tech-
niqueslikePrincipalComponentAnalysis(PCA)orautoencodersareoftenemployed.
Baoetal.[27]utilizedstackedautoencoderstocompresshigh-dimensionalfeatures
beforefeedingthemintoLSTMnetworks.
• TemporalAlignment: Aligningdatafromdiversesourceswithdifferentfrequencies
(e.g., dailypricedatawithquarterlyfundamentals)presentssignificantchallenges.
ChenandHao[21]addressedthisthroughtemporalaggregationandforward-filling
techniques.
4.5.3. AlternativeDataProcessing
Alternativedatasourcesrequirespecializedpreprocessing:
• TextProcessing:Newsandsocialmediadataundergotokenization,stemming,andem-
beddinggeneration. MittalandGoel[28]appliedsentimentdictionariestoclassify
tweets,whilemorerecentstudieslikeDingetal.[23]employedwordembeddings
andneurallanguagemodels.
• ImageProcessing: Satelliteimagerytypicallyundergoessegmentation,featureextrac-
tion,andobjectdetectionbeforeintegrationwithfinancialdata.
• SensorData: IoTsensordataoftenrequirenoisefiltering,aggregation,andanomaly
detection. Maetal.[29]processedindustrialsensordatathroughFouriertransforma-
tionsbeforeusingthemtopredictcommoditypricemovements.
5. PatternRecognitioninStockMarketAnalysis
Patternrecognitionapproachesattempttoidentifyrecurringvisualpatternsinstock
pricemovementsthatmayhavepredictivevalue. Thesemethodsarecloselyalignedwith
technicalanalysispracticesthathavebeenusedbytradersforgenerations.
5.1. PerceptuallyImportantPoints
Fuetal.[30]proposedanapproachtoidentifyingpatternsintimeseriesdatausing
PerceptuallyImportantPoints(PIPs),whichfocusonkeyinflectionpointsinpricecharts.
Thistechniquereducesdimensionalitywhilepreservingthemostsalientfeaturesofthe
timeseries,potentiallyallowingformoreefficientpatterndetection.

Electronics2025,14,1721 11of48
Markowska-Kaczmar and Dziedzic [31] implemented a supervised feed-forward
neuralnetworkwithPIPstoidentifypatternsinstockdata.TheirfindingssuggestthatPIPs
caneffectivelydiscoverpatternsinshortenedtimeseriesdatasets,thoughtheapproach
maystruggleiftherearehigh-amplitudefluctuationsbetweenadjacentdatapoints.
5.2. TemplateMatching
Templatematchinginvolvessearchingforpredefinedpatternsinstockpricechartsthat
typicallyprecedespecificmarketmovements. Leighetal.[32]developedabullflagpattern
recognizer using template matching, finding that this approach generated profits that
exceededrandomtrading,challengingsomeaspectsoftheEfficientMarketHypothesis.
Cervelló-Royo et al. [33] extended this work by introducing dynamic parameters
for closing operations and using intraday data. Their approach demonstrated positive
performance on multiple stock indices, providing further evidence against the strictest
interpretationsofmarketefficiency.
5.3. AdvancedPatternRecognition
Chen and Chen [26] developed a hybrid approach combining PIPs and template
matchingtoidentifybullflagpatterns,achievingsuperiorperformancecomparedtoother
patternrecognitionmodels. Theirmodelgeneratedunprecedentedstockindexreturns
whenappliedtoNASDAQandTAIEXindices.
Arévaloetal.[34]extendedprevioustemplatematchingworkbyaddingfiltersbased
onExponentialMovingAverages(EMAs)andpriceranges. Thisrefinedapproachoutper-
formedearliermethods,generatinghigherprofitswithlowerrisk.
Morerecently,Kimetal.[20]builtaPattern-MatchingTradingSystem(PMTS)based
onDynamicTimeWarping(DTW),applyingittotheKOSPI200index. Theirapproach
generatedsolidannualizedreturns,withpatternsprovingespeciallyprofitablenearmarket
clearingtimes.
5.4. EffectivenessandLimitations
Pattern recognition methods have shown promising results in multiple studies,
buttheireffectivenessremainscontroversialinacademicfinance. Someresearchersargue
thattheidentificationofpredictivepatternscontradictstheEfficientMarketHypothesis,
whileotherssuggestthatpatternrecognitionmaysimplybecapturingtemporarymarket
inefficienciesorriskpremiums.
Keylimitationsofpatternrecognitionapproachesincludethefollowing:
• Subjectivity: Patterndefinitionsmayvarybetweenanalysts,leadingtoinconsistent
results.
• OverfittingRisk: Systemsmaybeoptimizedtorecognizepatternsinhistoricaldata
thatlackpredictivevalueforfuturemovements.
• Changing Market Dynamics: Patterns that were predictive in the past may lose
effectivenessasmarketstructuresandparticipantbehaviorsevolve.
• LimitedTheoreticalFoundation: Unlikestatisticalmodels,patternrecognitionoften
lacksstrongtheoreticaljustificationinfinancialeconomics.
Despitetheselimitations,patternrecognitioncontinuestoplayasignificantrolein
algorithmictradingsystems,particularlyforshort-termtradingstrategies.
6. MachineLearningApproaches
Machine learning approaches have gained particular prominence in stock market
predictionresearchduetotheirabilitytocapturecomplex,nonlinearrelationshipswithout

Electronics2025,14,1721 12of48
requiring explicit theoretical models. These methods can be broadly categorized into
supervisedandunsupervisedlearningtechniques.
6.1. SupervisedLearningMethods
6.1.1. SupportVectorMachines
SupportVectorMachines(SVMs)havebeenwidelyappliedinstockpredictiondue
totheireffectivenessinhigh-dimensionalspacesandrobustperformanceonclassification
tasks. Huangetal.[35]appliedSVMstopredictthedirectionofstockmarketmovement,
achievingaccuraciessuperiortootherpredictionmethods.
Shenetal.[36]proposedanapproachcombiningstatisticalcorrelationanalysiswith
SVMs,exploitingrelationshipsamongglobalmarketsandotherproductstopredictthe
nextday’strendinstockprices. Theirmodelachieved77.6%predictionaccuracyonthe
DJIAindex,withevenhigheraccuracyforlonger-termpredictions.
6.1.2. DecisionTreesandRandomForests
DecisiontreesandtheirensemblevariantslikeRandomForestshaveprovenparticu-
larlyeffectiveforstockprediction.
Ensemblemethodscombinemultiplelearningalgorithms:
• RandomForest: Anensembleofdecisiontreesthathasdemonstratedstrongperfor-
manceacrossmultiplestockpredictionstudies. LohrmannandLuukka[37]applied
RandomForesttoclassifyintradayS&P500returnswithhighaccuracy.
• GradientBoosting:MethodslikeXGBoostandAdaBoosthaveshownexcellentperfor-
manceinstockprediction. Deyetal.[38]appliedXGBoosttopredictstockdirection,
achievingaccuraciesof87–99%forthelong-termpredictionofAppleandYahoostocks.
• Bagging Methods: Ampomah et al. [39] evaluated tree-based ensemble machine
learningmodelsinpredictingstockpricedirection,findingthatensemblemethods
consistentlyoutperformedindividualclassifiers.
Ensemblemethodsgenerallyprovidesuperiorperformancecomparedtoindividual
classifiersastheycanreduceoverfittingandcapturemorecomplexpatternsinthedata.
TheimprovedperformanceofensemblemethodslikeRandomForestandXGBoostappears
consistentacrossdifferentmarketsandtimeperiods.
Ballingsetal.[40]benchmarkedensemblemethodsagainstsingleclassifiersforpre-
dictingstockpricedirection,findingthatRandomForestconsistentlyoutperformedother
algorithms.
Basaketal.[41]comparedtree-basedclassifiersforpredictingstockmarketdirection,
findingthatRandomForestandgradient-boosteddecisiontrees(usingXGBoost)facilitated
accurate predictions. Their approach achieved high accuracy for medium- to long-run
predictionofstockpricedirection.
Khanetal.[42]comparedninemachinelearningmodelsforstockmarketprediction,
findingthatRandomForestachievedthehighestaccuracyof91.27%usingtheirproposed
strategy involving 15 min time intervals. Their work also emphasized the importance
of evaluating models based on financial performance metrics rather than classification
accuracyalone.
Recentcomparativestudieshavedemonstratedthesuperiorityofensemblemethods
beyondtraditionalRandomForestsforstockpredictiontasks. Pagliaro[43]foundthat
ExtraTreesClassifiermodelsachievesuperioraccuracy(86.1%)comparedtoRandomForest
methods(73%)whenpredictingsignificantstockpricechangesover10-daywindows.
ThesuperiorperformanceofExtraTreesClassifiermodelsstemsfromtheirunique
randomizedthresholdselectionprocess,whichoffersafavorablebias–variancetradeoff
comparedtotraditionalRandomForestmethods. UnlikeRandomForest,whichoptimizes

Electronics2025,14,1721 13of48
thresholdvalueswhensplittingnodes,ExtraTreesrandomlyselectsthresholdsandchooses
thebestamongtheserandomsplits. Thisadditionalsourceofrandomizationactsasan
effective regularization mechanism, significantly reducing variance (overfitting) while
introducingonlyasmallincreaseinbias. Forhigh-dimensional,noisyfinancialdatawith
non-stationarycharacteristics,thisregularizationeffectisparticularlybeneficialasiten-
hancesmodelrobustnessagainstspuriouspatternsandoutliers. However,thiscomeswith
potentialdisadvantages,includingreducedmodelinterpretabilityandpossiblysuboptimal
performanceinhighlystructureddatasetswhereoptimalthresholdselectionmightcapture
genuinepatternsmoreeffectivelythanrandomizedapproaches.
Thisapproachshowedparticularefficacyinvolatilemarketconditions,outperform-
ing buy-and-hold strategies by 14.35% during the high-interest rate environment of
2022–2023[43].
However,itisimportanttonotethatthesefigurestypicallyrepresent“gross”predic-
tionaccuracybeforeaccountingfortransactioncosts,slippage,andotherimplementation
frictions. Studies that incorporate these real-world trading constraints, such as those
by[6,43],demonstratethatnetperformancemetricsaresubstantiallylower,withreduc-
tionsinrealizedreturnsof15–40%comparedtotheoreticalperformance. Thishighlights
theimportanceofevaluatingmodelsbasedontheirpost-costeconomicperformancerather
thanrelyingsolelyonstatisticalaccuracymetrics.
6.1.3. ArtificialNeuralNetworks
ArtificialNeuralNetworks(ANNs)havebeenextensivelystudiedforstockprediction
duetotheirflexibilityandcapacitytomodelcomplexpatterns. QiuandSong[44]usedan
ANNoptimizedwithageneticalgorithmtopredictthedirectionoftheJapaneseNikkei
225index,achievinganaccuracyof81.27%.
Moghaddametal.[45]appliedfeed-forwardANNswithdifferentarchitecturesto
predicttheNASDAQindex,findingthatnetworkswithmultiplehiddenlayersachieved
superiorperformancecomparedtosimplerarchitectures.
6.1.4. DeepLearningModels
Deep learning models have shown particular promise for stock prediction in re-
centyears.
• RecurrentNeuralNetworks(RNNs): Bernaletal.[32]implementedEchoStateNet-
works(asubclassofRNNs)topredictS&P500stockprices,outperformingtraditional
techniqueswithverylowtesterror.
• LongShort-TermMemory(LSTM):DiPersioandHonchar[46]comparedbasicRNNs,
LSTM,andGatedRecurrentUnits(GRUs)forGooglestockpriceprediction,finding
thatLSTMoutperformedothervariantswith72%accuracyonafive-dayhorizon.
• Convolutional Neural Networks (CNNs): Sezer and Ozbayoglu [47] developed a
CNN-based approach for financial trading, converting time series data to image
representationstoleveragetheCNN’spatternrecognitioncapabilities.
WuandChen[48]comparedARIMAandLSTMmodelsforstockpriceprediction,
finding that ARIMA showed comparable accuracy to LSTM for long-term predictions,
thoughLSTMgenerallyperformedbetterincapturingcomplexpatterns.
6.2. UnsupervisedLearningMethods
Unsupervisedlearningmethodsidentifypatternsandcorrelationsindatawithout
requiringlabeledexamples.

Electronics2025,14,1721 14of48
• ClusteringMethods: Powelletal.[49]comparedK-meansclusteringwithSVMfor
stockprediction,findingsimilarperformancebetweenthetwoapproaches. Thestudy
highlightedtheimportanceofdistancemetricselectionforclusteringeffectiveness.
• Association Rule Learning: Wu et al. [50] proposed a model combining K-means
clusteringwiththeAprioriAllalgorithmtoextractfrequentpatternsandpredictstock
trends,outperformingotherapproachesintermsofaveragereturns.
• HybridUnsupervisedApproaches: Babuetal.[51]proposedaclusteringmethod
called HAK that combines Hierarchical Agglomerative Clustering and reverse
K-meansclusteringtopredicttheimpactoffinancialreportsonstocks,outperforming
SVMsintermsofaccuracy.
Unsupervisedlearningapproachesareparticularlyvaluableforidentifyingmarket
regimesandsegmentingstocksintogroupswithsimilarbehaviorpatterns. Theseinsights
cantheninformsupervisedlearningmodelsortradingstrategies.
6.3. ComparativeAnalysisofMachineLearningModels
Severalstudieshaveconductedcomparativeanalysesofmultiplemachinelearning
modelsforstockprediction.
Pateletal.[52]comparedANNs,SVMs,RandomForest,andnaiveBayesforpredicting
stockpricedirection,findingthatRandomForestgenerallyoutperformedothertechniques.
Chongetal.[53]conductedasystematicanalysisofdeeplearningnetworksforstock
market prediction, finding that deeper architectures typically outperformed shallower
networksandtraditionalmethods.
Khanetal.[42]comparedninemachinelearningmodelsusingbothtraditionalmethod-
ologyandanovel15mintimeintervalstrategy. Withthetraditionalmethodology,logistic
regression achieved the highest accuracy (85.51%), while, with the proposed strategy,
RandomForestachievedthehighestaccuracy(91.27%).
Thesecomparativestudieshighlightthatnosinglemodelconsistentlyoutperformsall
othersacrossallmarketsandtimeperiods. Performancedependsondatacharacteristics,
featureselection,hyperparametertuning,andevaluationmetrics.However,ensemblemeth-
odslikeRandomForestandgradient-boostingapproachestendtoperformwellconsistently.
Whileourliteratureanalysisconsistentlyshowsthatensemblemethodsoutperform
singleclassifiersacrossvariousstudies,itisimportanttoqualifythisgeneralization. Thesu-
periorityofensemblemethodsisnotuniversalandcanbehighlydataset-dependentand
context-specific. Undercertainmarketconditions—particularlyduringstable,trending
regimeswithclearpatterns—simplersinglemodelsmayperformcompetitivelywhileof-
feringadvantagesininterpretability,computationalefficiency,andeaseofimplementation.
Forinstance, WuandChen[48]demonstratedthatARIMAmodelscanmatchLSTMper-
formanceforlong-termpredictionsintrendingmarkets,andQiuandSong[44]foundthat
optimizedsingleANNsoutperformedcertainensemblemethodsduringperiodsoflow
volatility. Furthermore,theadvantageofensemblemethodsmaydiminishwhendealing
withextremelyhigh-frequencydata,wherelatencyconsiderationsbecomeparamount,orin
marketswithverylimitedhistoricaldata,whereensemblediversitycannotbeeffectively
leveraged. Futurecomparativestudiesshouldsystematicallyevaluatemodelperformance
acrossdifferentmarketregimes,volatilityenvironments,anddatacharacteristicstodevelop
morenuancedguidelinesformodelselectionbasedonspecificforecastingcontexts.
7. SentimentAnalysisforStockPrediction
Sentimentanalysisleveragestextualdatatogaugemarketsentimentandincorporate
qualitativeinformationintoquantitativepredictionmodels. Thisapproachrecognizesthat

Electronics2025,14,1721 15of48
stockmarketsareinfluencednotjustbyfinancialmetricsbutalsobymarketpsychology
andpublicperception.
7.1. News-BasedSentimentAnalysis
News articles provide valuable insights into company developments and market
conditions.
SchumakerandChen[54]analyzedtheeffectsofbreakingnewsonstockpriceswithin
20minafterrelease,usinganSVMderivativemodelwithdifferenttextualrepresentations.
Theyfoundthatthenounphrasesmethodperformedbetterthanbagofwordsandnamed
entitiesmodels.
Kalyanaramanetal.[55]developedasentimentanalysismodeltogaugesentiments
fromnewsarticlesandfeedtheoutputintomachinelearningalgorithms. Theirapproach
achievedanaccuracyof81.82%forpredictingstockprices.
Leeetal.[56]analyzedForm8-Kreports(importantupdatesregardingcompanies)to
predictstockpricemovements,findingthatincorporatingtextanalysisimprovedmodel
accuracyby10%. Theirresearchalsofoundthattheeffectofsentimentanalysisonthese
reportsdiminishesquicklywithtime,suggestingtheyaremostvaluableforshort-term
predictions.
7.2. SocialMedia-BasedSentimentAnalysis
Socialmediaplatformsprovidereal-timeinsightsintopublicsentiment.
Bollen et al. [22] analyzed Twitter data using Google Profile of Mood States and
OpinionFindertounderstandcorrelationswithDJIAclosingprices. ByapplyingaSelf-
OrganizingFuzzyNeuralNetworktoapproximately10milliontweets,theyachievedan
accuracyof87.6%inpredictingdailyDJIAvalues.
Mittal and Goel [28] extended this work with a larger dataset of over 400 million
tweets,achievinganaccuracyof75%andfindingthatboth“calmness”and“happiness”
werepredictiveindicatorsoverarangeofthreetofourdays.
Pagoluetal.[57]implementedasentimentanalysismodelbasedonTwitterdatausing
N-gramandWord2vectechniques,achieving70%accuracyandnotinga71.82%correlation
betweenpriceandsentiments.
7.3. SearchVolumeAnalysis
Searchvolumedataprovideinsightsintopublicinterestandattention:
Huetal.[25]incorporatedGoogleTrendsdataintoneuralnetworkmodelsforpredict-
ingstockmarketdirection. Theirapproachcombinedanimprovedsinecosinealgorithm
with back propagation neural networks, achieving hit ratios of 86.81% for the S&P 500
Index and 88.98% for the Dow Jones Industrial Average Index when including Google
Trendsdata.
Preisetal.[58]showedthatsearchvolumedatafromGoogleTrendscouldbeusedto
detectearlywarningsignsofstockmarketmovements.Theirworkdemonstratedthatchanges
insearchbehaviorprecededmarketmovements,providingvaluablepredictiveinformation.
7.4. CombinedSentimentApproaches
Severalstudieshavecombinedmultiplesentimentsourcesforimprovedprediction.
Dingetal.[23]proposedahybridapproachcombiningsentimentanalysiswithneural
networkmodelsforS&P500indexprediction. Theirdeepconvolutionalneuralnetwork
wastrainedtopredictshort-andlong-terminfluencesofnewsevents,achievingaccuracies
of64.21%forindexpredictionand65.48%forindividualstockpriceprediction.

Electronics2025,14,1721 16of48
Ren et al. [59] developed a model combining support vector machines with senti-
mentanalysistechniquesforShanghaiStockExchangeprediction,achievinganaccuracy
of89.93%.
Sentimentanalysisapproachesofferavaluablecomplementtotraditionaltechnical
andfundamentalanalysis,particularlyforshort-termpredictionhorizons.Byincorporating
publicmoodandattentionmetrics,thesemodelscancaptureaspectsofmarketbehavior
notreflectedinpriceandvolumedataalone.
8. HybridandAdvancedApproaches
Asstockmarketpredictiontechniqueshaveevolved,researchershaveincreasingly
focusedonhybridapproachesthatcombinemultiplemethodologiestoovercomethelimi-
tationsofindividualtechniques. Thesehybridmodelsoftenachievesuperiorperformance
byleveragingthestrengthsofdifferentapproaches.
8.1. HybridTechnicalModels
Manyhybridmodelscombinedifferenttechnicalpredictionapproaches.
Wang et al. [60] proposed a hybrid model combining the Exponential Smoothing
Method(ESM),ARIMA,andBackpropagationNeuralNetwork(BPNN)forweeklystock
priceprediction. Thishybridmodeloutperformedindividualconstituentmodelsonboth
theShenzhenIntegratedIndexandDJIA,withadirectionalaccuracyof70.16%.
Rather etal. [61] developeda hybrid modelintegrating linear (ARIMA,ESM) and
non-linear (RNN) approaches, with weights determined by a genetic algorithm. Their
hybridapproachachievedlowerMeanAbsoluteErrorandMeanSquaredErrorcompared
toconstituentmodels.
Lvetal.[62]evaluatedvariousmachinelearningalgorithmsanddeepneuralnetwork
modelsusingS&P500andCSI300IndexComponentStocks. Theirfindingsindicatedthat
traditionalmachinelearningalgorithmsperformedbetterondirectionalindicatorswithout
transactioncosts,whiledeepneuralnetworksperformedbetterwhentransactioncosts
wereconsidered.
8.2. MultimodalDataIntegration
Somehybridapproachesintegratefundamentallydifferentdatatypes.
Yoshihara et al. [63] combined Deep Belief Networks (DBNs) with RNN-RBM to
predict long-term stock price changes based on significant events, achieving lower test
errorratescomparedtoindividualmodels.
Dingetal.[23]developedaneuraltensornetworkforlearningeventembeddingsand
adeepCNNtomodeltheinfluencesofeventsonstockpricemovements,demonstratinga
6%improvementinS&P500indexpredictioncomparedtostate-of-the-artapproaches.
Huetal.[25]integratedGoogleTrendsdatawithneuralnetworksoptimizedbyanim-
provedsinecosinealgorithm. TheirISCA-BPNNmodelwithGoogleTrendsdataachieved
hitratiosof86.81%fortheS&P500Indexand88.98%fortheDJIAIndex,demonstrating
thevalueofsearchvolumedataforprediction.
8.3. CombinedTechnicalandFundamentalAnalysis
Someapproachesintegratetechnicalandfundamentalanalysis.
Duttaetal.[19]demonstratedtheutilityoffundamentalanalysisthroughfinancial
ratiostoseparategoodstocksfrompoorstocks,comparingtheirone-yearreturnagainst
benchmarkindices.
ChenandHao[21]utilizedaweightedsupportvectormachineandK-nearestneighbor
approachtopredictChinesestockmarketindices,incorporatingbothtechnicalindicators
andfundamentaldata.

Electronics2025,14,1721 17of48
Shenetal.[36]exploitedcorrelationsamongglobalmarketsandotherproductsto
predict stock prices, achieving 77.6% accuracy on DJIA prediction and up to 85% for
longer-termpredictions.
8.4. AdvancedDeepLearningArchitectures
Recentresearchhasfocusedonincreasinglysophisticateddeeplearningarchitectures.
FischerandKrauss[6]appliedLSTMnetworkstofinancialmarketpredictions,demon-
stratingsuperiorperformancecomparedtoRandomForests,deepneuralnetworks,andlo-
gisticregression.
Sezer et al. [11] developed a CNN-based algorithmic trading model using image
representationsoffinancialtimeseriesdata,achievingconsistentprofitabilityacrossmulti-
plemarkets.
Baoetal.[27]proposedadeeplearningframeworkusingstackedautoencodersand
LSTM,findingthattheirapproachoutperformedtraditionalmachinelearningmethodsfor
stockpriceprediction.
8.5. GraphNeuralNetworksforStockPrediction
An emerging trend involves using graph neural networks to model relationships
betweenstocks.
Wang et al. [64] proposed a model integrating knowledge graphs, Graph Convo-
lutional Networks (GCNs), and community detection for stock price prediction. This
approachovercamethelimitationsofexistingmodelsbyaccountingfordeeperinfluencing
factorsandleveragingrelationshipsbetweenstocks.
Zhang[65]developedaconceptual–temporalgraphCNNmodel(CT-GCNN)forpre-
dictingstockpricemovements,exploringmovementsinbothtimeandconceptdimensions
andaccountingforlinkageeffectsamongstockswithinthesameconceptualsegment.
Thesegraph-basedapproachesrepresentapromisingdirectionforstockpredictionby
explicitlymodelingthecomplexrelationshipsbetweendifferentstocksandmarketsectors.
8.6. ReinforcementLearningforTrading
Reinforcementlearning(RL)approacheshavegainedattentionfordevelopingtrading
strategies.
Jang and Seong [66] proposed a deep reinforcement learning approach for stock
portfoliooptimization,connectingwithmodernportfoliotheoryusinga3Dconvolutional
neuralnetworkforfeatureextractionandDeepDeterministicPolicyGradient(DDPG)for
portfoliooptimization.
Wuetal.[67]developedanovelGANwithpiecewiselinearrepresentationforpredict-
ingmarkettradingactions(buying,selling,andholding),outperformingLSTM-basedap-
proaches.
Reinforcementlearningoffersparticularpromiseforportfoliooptimizationandtrad-
ingstrategydevelopmentasitcandirectlyoptimizeforfinancialobjectivesratherthan
intermediatemetricslikepredictionaccuracy.
9. EvaluationMethodologies
Theevaluationofstockpredictionmodelspresentsuniquechallengescomparedto
typicalmachinelearningtasks. Whileclassificationmetricslikeaccuracyarecommonly
reported, they may not directly translate to profitable trading strategies. This section
exploresvariousapproachestomodelevaluation.

Electronics2025,14,1721 18of48
9.1. ClassificationPerformanceMetrics
The evaluation of stock prediction models requires the careful selection of appro-
priatemetricsbasedonthepredictiontaskformulation. Whilestockforecastingcanbe
approached as either a regression problem (predicting actual price/return values) or a
classificationproblem(predictingdirectionalmovementordiscretecategories), classifi-
cationmetricshavebecomeprevalentintheliteratureduetothepracticalimportanceof
directionalaccuracyformanytradingstrategies. Classificationmetricsaremostappropri-
atewhentheresearchquestionfocusesondirectionalmovementorcategoricaloutcomes
(e.g., buy/sell/hold signals), while regression metrics (RMSE, MAE, R2) and financial
performancemetricsaremoresuitablewhenprecisevalueforecastsoreconomicoutcomes
aretheprimaryconcern. Itisimportanttorecognizethateachmetrictypehasinherent
limitations: classificationmetricsmayobscurethemagnitudeoferrors,whileregression
metricsmightfailtocapturetheeconomicsignificanceofdirectionalaccuracy.
Standardclassificationmetricswidelyusedinthestockpredictionliteratureinclude
thefollowing:
• Accuracy:Thepercentageofcorrectpredictions,typicallycalculatedas(TP+TN)/(TP+
TN+FP+FN).
• Precision: Theproportionoftruepositivepredictionsoutofallpositivepredictions,
calculatedasTP/(TP+FP).
• Recall:Theproportionoftruepositivepredictionsoutofallactualpositives,calculated
asTP/(TP+FN).
• F1Score: Theharmonicmeanofprecisionandrecall,providingabalancebetweenthe
twometrics.
• Area Under the ROC Curve (AUC): Measures the model’s ability to distinguish
betweenclassesacrossdifferentthresholdsettings.
These metrics provide valuable insights into a model’s classification performance,
buttheydonotnecessarilyindicatefinancialperformance.
9.2. FinancialPerformanceMetrics
Several studies have emphasized the importance of evaluating models based on
financialperformancemetrics.
• Returns: Measures investment performance, including cumulative return, annual
return,andrisk-adjustedreturn.
• Sharpe Ratio: Evaluates risk-adjusted performance by comparing excess returns
tovolatility.
• MaximumDrawdown: Showsthelargestpeak-to-troughdeclineinportfoliovalue,
indicatingdownsiderisk.
• WinRate: Calculatesthepercentageofprofitabletrades,indicatingtheconsistencyof
returns.
• ProfitFactor: Indicatestheratioofgrossprofitstogrosslosses,indicatingtheoverall
profitabilityofastrategy.
Khanetal.[42]demonstratedthatmodelswithsimilarclassificationaccuracycanpro-
ducesignificantlydifferentfinancialoutcomes. Theirsimulatedtradingresultsshowedthat
RandomForestgeneratedthehighestreturnsdespitenothavingthehighestclassification
accuracyintheirtraditionalmethodology.

Electronics2025,14,1721 19of48
9.3. Statisticalvs. EconomicSignificanceinModelEvaluation
Acriticalshortcominginmuchofthestockmarketpredictionliteratureistheconfla-
tionofstatisticalsignificancewitheconomicrelevance. Thissectionaddressesthisgapand
providesacomprehensiveframeworkfortherigorousevaluationofpredictionmodels.
9.3.1. DistinguishingStatisticalfromEconomicSignificance
Statisticalsignificanceindicatesthatanobservedeffectisunlikelytohaveoccurred
bychance,butrevealsnothingaboutthemagnitudeorpracticalimportanceofthateffect.
Infinancialcontexts,thisdistinctioniscritical.
• StatisticalSignificance: Measureswhetheraresultdiffersfromwhatwouldbeex-
pected under the null hypothesis (typically assessed using p-values or confidence
intervals).
• EconomicSignificance: Measureswhetheraresultmattersinpracticalterms,consid-
eringimplementationcosts,riskadjustment,andreal-worldconstraints.
Harvey[68]highlightedhowstudiesoftenemphasizep-valuesbelowconventional
thresholds (e.g., p < 0.05) without demonstrating that the identified patterns generate
meaningfuleconomicvalueafteraccountingfortransactioncosts,marketimpact,andother
real-worldconstraints.
Table 1 illustrates the disconnect between statistical and economic significance in
severalinfluentialstudies.
Table1.Statisticalvs.economicsignificanceinselectedstudies.
Study StatisticalSignificance EconomicSignificance EvaluationAfterCosts
LoandMacKinlay Strongrejectionof 12%annualexcess Reducedto3–4%after
(1990)[69] randomwalk(p<0.001) returns transactioncosts
BakerandWurgler Sentimentindex Predicted1.3%monthly Notevaluatedafter
(2006)[70] significantatp<0.01 spread implementationcosts
Neuralnetworks Sharperatioof0.9for Sharperatiodroppedto
Guetal.(2020)[71]
outperformatp<0.01 neuralnets 0.4withtransactioncosts
14%profitaftercosts,
DeeplearningLSTM 30%improvementin
Fengetal.(2019)[72] lowerthanbuy-and-hold
significant(p<0.001) directionalaccuracy
inbullmarket
9.3.2. AppropriateStatisticalTestsforFinancialTimeSeries
Financial time series possess characteristics that violate assumptions of standard
statisticaltests.
• Non-normality:Returnsdistributionstypicallyexhibitfattailsandskewness.Shapiro–
WilkorJarque–Beratestsshouldbeusedtochecknormalitybeforeapplyingparamet-
rictests.
• SerialDependence: Financialreturnsoftenshowautocorrelation,heteroskedasticity,
andotherformsofserialdependence. Ljung-BoxorARCHtestsshouldbeappliedto
verifyindependenceassumptions.
• Non-stationarity: Thestatisticalpropertiesoffinancialtimeserieschangeovertime.
AugmentedDickey–FullerorKPSStestscanassessstationarity.
Appropriatestatisticaltestsforevaluatingpredictionperformanceincludethefollowing:
• Diebold–MarianoTest[73]:Testswhethertwoforecastingmethodsdiffersignificantly
inaccuracywhileaccountingforserialcorrelationinforecasterrors.
• ModelConfidenceSet[74]: Identifiesthesetofmodelsthatarestatisticallyindistin-
guishablefromthebestmodel,providingarobustwaytocomparemultipleforecast-
ingmethods.

Electronics2025,14,1721 20of48
• White’sRealityCheck[75]andHansen’sSPATest[76]: Testwhetheranymodelina
setoutperformsabenchmark,adjustingfordatasnoopingbiases.
• Giacomini–WhiteTest[77]: Evaluatesconditionalpredictiveability,whichismore
relevantfortime-varyingmodels.
• Bootstrap Methods [78]: Provide distribution-free inference when the underlying
distributionsareunknownorcomplex.
Notably,CampbellandThompson[79]demonstratedthatevenpredictionmodelswith
verylowR2(e.g.,0.5%)cangenerateeconomicvalueifproperlyimplemented,highlighting
thedisconnectionbetweentraditionalstatisticalmeasuresandeconomicutility.
9.3.3. MultipleHypothesisTestinginFinancialPrediction
Thepracticeoftestingnumerouspotentialpredictors,modelspecifications,orparam-
etercombinationscreatesseveremultipletestingproblems:
• Withastandardsignificancelevelof0.05,testing100independentstrategieswouldbe
expectedtoyield5“significant”resultsbypurechance.
• Financialresearchoftenimplicitlyteststhousandsofcombinations,leadingtoamas-
sivemultipletestingproblemthatstandardp-valuesfailtoaddress.
Theprobabilityoffalsediscoveriesincreasesdramaticallywiththenumberoftests
performed. Appropriatecorrectionsformultipletestingincludethefollowing:
• BonferroniCorrection:Adjuststhesignificancethresholdbydividingitbythenumber
oftests(e.g.,for100tests,significancethresholdbecomes0.05/100=0.0005).
• Benjamini–HochbergProcedure[80]: Controlsthefalsediscoveryrate(FDR)rather
thanthefamily-wiseerrorrate,offeringmorepowerwhilelimitingfalsepositives.
• Holm’s Step-Down Procedure [81]: Provides stronger controls than Benjamini–
HochbergbutlessconservativethanBonferroni.
• FalseDiscoveryProportionControl[82]: Limitstheproportionoffalsediscoveries
whilemaximizingtruediscoveries.
Harveyetal.[83]arguedthatgiventheextentofmultipletestinginfinance,amini-
mumt-statisticthresholdof3.0(correspondingtop<0.003)shouldreplacetheconventional
1.96thresholdwhenevaluatingnewfactorsorpredictors.
9.3.4. StructuralBreaksandTime-VaryingParameters
Financialmarketsundergostructuralchangesduetoregulatoryshifts,technological
innovations,andevolvingmarketparticipantbehavior. Theseshiftscreatechallengesfor
statisticalinference:
• Parameters estimated from past data may no longer apply in the current market
environment.
• Significantrelationshipsmayreverseordisappearfollowingstructuralbreaks.
• Traditional statistical tests assume parameter stability, leading to false conclusions
whenthisassumptionisviolated.
Methodstoaccountforstructuralbreaksincludethefollowing:
• Andrews–QuandtTest[84]: Detectsunknownstructuralbreakpointsintimeseries
regression.
• Bai–PerronTest[85]: Identifiesmultiplestructuralbreaksintimeseriesdata.
• Time-VaryingParameterModels[86]: Allowcoefficientstoevolvegraduallyover
time,capturingchangingrelationships.
• Regime-Switching Models [87]: Model discrete shifts between different market
regimeswithdistinctparameters.

Electronics2025,14,1721 21of48
PesaranandTimmermann[88]demonstratedhowfailuretoaccountforstructural
breakscanleadtosubstantialforecasterrors,evenwhenmodelsappearstatisticallysignifi-
cantin-sample.
9.3.5. ComprehensiveFrameworkforModelEvaluation
InTable2,weproposeacomprehensiveframeworkforevaluatingpredictionmod-
elsthatgoesbeyondsimplestatisticalsignificance,whilethecomprehensiveevaluation
frameworkdepictedinFigure3illustratesthemulti-dimensionalapproachrequiredforthe
properassessmentofstockpredictionmodels.
Table2.Proposedframeworkforcomprehensivemodelevaluation.
Dimension Metrics/Methods KeyConsiderations
• Istheeffectstatisticallysignificantafteraccountingfor
• Multiple-testingadjustedp-values
Statistical multipletesting?
• Modelconfidencesets
Validity • Howmanyalternativespecificationsweretried?
• White’sRealityCheck
• Isthemodelgenuinelysuperiortosimpleralternatives?
• Standardizedeffectsizes(Cohen’sd,etc.) • Istheeffectsizeeconomicallymeaningful?
• Economicperformancemetrics(Sharperatio, • How does the magnitude compare to known risk
EffectMagnitude
alpha,etc.) factors?
• Forecasterrormetrics(RMSE,MAE,etc.) • Doestheeffectpersistaftertransactioncosts?
• Doesperformancedecayout-of-sample?
• Walk-forwardtesting • Is validation methodology appropriate for financial
Out-of-Sample
• Combinatorialpurgedcross-validation timeseries?
Validation
• Holdoutsetsfromdifferenttimeperiods • Isthereatemporalgapbetweentrainingandtesting
periods?
• Doesthemodelperformconsistentlyacrossdifferent
• Performanceinbull/bearmarkets
Robustness marketconditions?
• Performanceacrossvolatilityregimes
AcrossRegimes • Arethereperiodswherethemodelconsistentlyfails?
• Cross-marketvalidation
• Doesperformancetransfertorelatedmarkets?
• How sensitive is performance to small parameter
• Localsensitivityanalysis changes?
Parameter
• MonteCarlosimulations • Areresultsdrivenbyafewoutlierobservations?
Sensitivity
• Extremescenariotesting • How does the model perform under extreme
conditions?
• Transactioncostmodels • Canthestrategybeimplementedatscale?
Implementation
• Liquidityconstraints • Howdotradingfrictionsaffectperformance?
Feasibility
• Executionsimulations • Whatcapacityconstraintsexist?

Electronics2025,14,1721 22of48
Figure3.Modelevaluationframeworkforstockmarketprediction.Theframeworkencompasses
fourkeydimensions: statisticalevaluation,financialperformance,modelrobustness,andpracti-
calimplementation, withintegrationatthecenterhighlightingtheholisticapproachneededfor
comprehensivemodelassessment.
9.3.6. CriticalAssessmentofKeyStudies
Re-examininginfluentialstudiesthroughthismorerigorouslensrevealssignificant
limitations.
• Brocketal. (1992)[89]: Whilefindingstatisticalsignificancefortechnicaltradingrules
ontheDowJonesIndex,theydidnotaccountformultipletestingacrossthemanyrule
parameterizations. Sullivanetal.[90]latershowedthatafterpropermultipletesting
adjustments,fewrulesremainedsignificant.
• Loetal. (2000)[91]: TheyidentifiedstatisticallysignificanttechnicalpatternsinUS
stocksbutreportedeconomicgainsofonly0.7–2.2%,likelyinsufficienttoovercome
transactioncosts. Noadjustmentformultipletestingacrossthemanypatternswas
examined.
• FischerandKrauss(2018)[6]: TheyreportedimpressiveperformanceofLSTMnet-
worksforS&P500stockpredictionbutdidnotsystematicallyevaluaterobustness
across different market regimes. Their strongest results came during the unusual
post-2008bullmarket,raisingquestionsaboutgeneralizability.
• Guetal. (2020)[71]: Whileemployingproperout-of-samplevalidationanddemon-
stratingsuperiorperformanceofneuralnetworks,theiranalysisdidnotfullyaccount
for survivorship bias in the dataset or evaluate performance under different mar-
ketregimes.
9.3.7. ImplicationsforAI-BasedStockPredictionResearch
Thechallengesofstatisticalinferenceinfinancialpredictionhavespecificimplications
forAI-basedapproaches:
• Theflexibilityofdeeplearningmodels,withnumeroushyperparametersandarchi-
tecturalchoices,exacerbatesmultipletestingconcerns. Researchersshouldreportall
modelvariationsattemptedandapplyappropriatecorrections.

Electronics2025,14,1721 23of48
• Theblack-boxnatureofcomplexAImodelsmakesitdifficulttodistinguishgenuine
patterndiscoveryfromoverfitting. Techniqueslikefeatureimportanceanalysis,partial
dependenceplots,andSHAPvaluescanhelpassesswhethermodelsarecapturing
economicallyplausiblerelationships.
• AI models trained on specific market regimes may fail to generalize to new condi-
tions. Time-stratifiedvalidation,wheremodelsaretestedondistinctmarketregimes
(e.g., high/low volatility, bull/bear markets), provides more realistic performance
estimates.
• Ensembleapproachesthatcombinemultiplemodelswithdifferentassumptionsmay
provide more robust predictions than single models, mitigating the risk of statisti-
calflukes.
By applying these more rigorous standards to the evaluation of stock prediction
models,researcherscandevelopmorereliableinsightsandpractitionerscanbetterassess
whichapproachesarelikelytodelivergenuinevalue.
9.3.8. PracticalImplementationGuideforComprehensiveEvaluation
Toimplementtheproposedevaluationframeworkinpractice,researchersandpracti-
tionersshouldfollowthesesteps:
1. InitialStatisticalAssessment:
• Establish baseline performance using traditional metrics (accuracy, precision,
F1-score)
• Conductappropriatestatisticaltestsbasedondatacharacteristics:
– Fornormallydistributedpredictionerrors: t-testsorANOVA
– For non-normal distributions: Wilcoxon signed-rank or Mann–Whitney
Utests
– Fortimeseriespredictions:Diebold–Marianotesttocompareforecastaccuracy
• Apply multiple testing corrections based on the number of model configura-
tionstested:
– Bonferronicorrectionfor<10modelconfigurations(conservative)
– Benjamini–Hochbergprocedureforlargernumbers(controlsfalsediscov-
eryrate)
– White’sRealityCheckorHansen’sSPAforcomparingmultiplemodelstoa
benchmark
2. EconomicSignificanceTesting:
• Implementtradingsimulationsincorporatingrealisticassumptions:
– Transactioncosts(variablebymarketcapitalizationandvolume)
– Marketimpactmodels(especiallyforlargepositions)
– Executiondelaysandslippage
• Calculateeconomicperformancemetrics:
– Risk-adjustedreturns(Sharperatio,Sortinoratio)
– Maximumdrawdownandrecoveryperiods
– Win/lossratiosandprofitfactors
• Comparetoappropriateeconomicbenchmarks:
– Risk-matchedbuy-and-holdportfolios
– Industryorfactor-basedportfolios
– Analystconsensusforecasts
3. RobustnessTesting:

Electronics2025,14,1721 24of48
• Testperformanceacrossdistinctmarketregimes:
– Bullvs. bearmarkets
– Highvs. lowvolatilityperiods
– Risingvs. fallinginterestrateenvironments
• Conductsensitivityanalysis:
– Parameterperturbationtests
– Featureimportanceanalysis
– Randomseedvariationforstochasticmodels
• Performwalk-forwardvalidation:
– Expandingwindowapproachforgrowingdatasets
– Rollingwindowapproachformaintainingconsistenttrainingsize
– Purgedcross-validationtopreventinformationleakage
4. ImplementationFeasibilityAssessment:
• Evaluatecomputationalrequirements:
– Trainingtimeandhardwarerequirements
– Inferencelatencyfortime-sensitiveapplications
– Memoryandstoragerequirements
• Assessscalabilityconstraints:
– Positionsizingandliquiditylimitations
– Strategycapacityestimates
– Marketimpactwithincreasedcapitaldeployment
• Consideroperationalrequirements:
– Datacollectionandprocessingpipeline
– Modelretrainingfrequency
– Monitoringandfailoversystems
CaseStudy: ApplyingtheFrameworktoanLSTM-BasedPredictionSystem
To illustrate the practical application of this framework, consider an LSTM-based
system for predicting S&P 500 constituent stocks similar to [6]. The evaluation would
proceedasfollows:
1. InitialStatisticalAssessment: Themodelachieves53.2%directionalaccuracy,which
ismodestbutstatisticallysignificantwhencomparedtoa50%randombenchmark(p<0.01
usingtheDiebold–Marianotest). AfterapplyingBenjamini–Hochbergcorrectionfortesting
20hyperparameterconfigurations,theresultremainssignificant(adjustedp=0.032).
2. EconomicSignificanceTesting: Implementingasimulatedtradingstrategywithtrans-
actioncostsoffivebasispointspertradeand1-dayexecutiondelayreducestheannualized
Sharperatiofrom1.12(withoutfrictions)to0.77(withfrictions). Thisremainsabovethe
buy-and-holdSharperatioof0.51forthesameperiod,confirmingeconomicsignificance.
3. RobustnessTesting: Performanceremainsconsistentinbullmarkets(Sharpe=0.81)
andbearmarkets(Sharpe=0.69),indicatingrobustnessacrossregimes. Sensitivityanalysis
showsstableperformancewithupto20%variationinhyperparameters,andwalk-forward
validationmaintainssimilarperformancetocross-validation.
4. ImplementationFeasibility: ThemodelrequiresretrainingweeklyonGPUhardware,
withinferencepossiblewithin50msperstock. Scalabilityanalysisindicatesstrategyca-
pacityofapproximatelyUSD100millionbeforesignificantmarketimpactwouldreduce
returns,makingitsuitableforsmalltomedium-sizedfundsbutnotlargeinstitutionalin-
vestors.

Electronics2025,14,1721 25of48
Thiscomprehensiveevaluationprovidesarealisticassessmentofthemodel’spractical
valuebeyondsimpleaccuracymetrics.
9.4. ComprehensiveBenchmarkingApproaches
MeaningfulevaluationofAI-basedpredictionmodelsrequirescomparisonagainst
appropriatebenchmarksthatgobeyondsimpleheuristics. Thissectionexpandstherange
ofbenchmarkstoincludemoresophisticatedalternatives.
9.4.1. TraditionalFinancialModels
Beyondsimplebuy-and-holdstrategies,traditionalfinancialmodelsprovideimpor-
tantbenchmarks:
• FactorModels: TheFama-Frenchthree-factorandfive-factormodelsaccountforsize,
value,profitability,andinvestmentpatternsinstockreturns. Thesemodelsprovide
more rigorous benchmarks than market indices alone. As demonstrated by [71],
comparingAIpredictionsagainstfactormodelforecastshelpsisolatetheincremental
valueofmachinelearningapproaches.
• ARIMAandGARCHVariants: Thesetraditionaltimeseriesmodelscaptureautore-
gressivepatternsandvolatilityclustering. WuandChen[48]showedthatARIMA
modelsremaincompetitivewithLSTMnetworksforlonger-horizonforecasts,making
themvaluablebenchmarkcomparisons.
• EconometricModels: VectorAutoregression(VAR)models,ErrorCorrectionModels
(ECMs), and other econometric approaches provide theoretically grounded bench-
marks. Rapachetal.[92]employedVARmodelsincorporatingmultipleeconomic
variablesasbenchmarksforforecastingaggregatemarketreturns.
9.4.2. ExpertandConsensusForecasts
Humanexpertforecastsserveasimportantbenchmarksthatincorporatequalitative
judgment:
• AnalystConsensusEstimates: Aggregatedforecastsfromfinancialanalystsprovide
benchmarksthatincorporatefundamentalanalysisanddomainexpertise. Bradshaw
et al. [93] demonstrated that consensus analyst forecasts contain information not
capturedbyquantitativemodelsalone.
• Survey-BasedForecasts: Surveysofprofessionalforecasters,suchastheSurveyof
ProfessionalForecasters(SPF)ortheWallStreetJournalEconomicForecastingSurvey,
offeralternativebenchmarksformacroeconomicvariablesthatinfluencemarkets.
• Market-ImpliedForecasts:Options-impliedvolatility,forwardrates,andothermarket-
derivedforecastsrepresentthecollectivewisdomofmarketparticipants. Christof-
fersen et al. [94] showed that option-implied volatility forecasts often outperform
statisticalmodels,makingthemvaluablebenchmarks.
9.4.3. Industry-SpecificModels
Sectorandindustry-specificmodelsaccountfortheuniquecharacteristicsofdifferent
marketsegments:
• CommodityMarkets:Modelsincorporatingstoragetheory,convenienceyield,andsea-
sonality patterns provide appropriate benchmarks for commodity-related stocks.
ChengandXiong[95]developedcommodity-specificbenchmarksthatoutperform
generalfinancialmodelsforresourcesectorstocks.
• FinancialInstitutions: Modelsincorporatingfactorslikeyieldcurvedynamics,credit
spreads, and regulatory capital constraints provide suitable benchmarks for bank

Electronics2025,14,1721 26of48
stocks. Englishetal.[96]demonstratedthatspecializedmodelsaccountingforinterest
ratesensitivityoffersuperiorbenchmarksforfinancialinstitutionstocks.
• TechnologySector: Growthmodelsincorporatingnetworkeffects,R&Dproductivity,
andtechnologyadoptioncyclesprovideappropriatebenchmarksfortechnologystocks.
PastorandVeronesi[97]developedtechnology-sector-specificbenchmarksthatcapture
theuniquevaluationdynamicsofhigh-growthtechnologyfirms.
9.5. Simulation-BasedEvaluation
Simulation-basedapproachesprovideamorerealisticassessmentofmodelperformance:
• Backtesting: Testing a model on historical data to simulate trading decisions and
evaluatefinancialoutcomes.
• Out-of-SampleTesting: Evaluatingmodelsondatanotusedfortrainingtoassess
generalizationperformance.
• Walk-ForwardAnalysis: Asequentialtestingapproachwheremodelsareretrainedas
newdatabecomeavailable.
Backtestingallowsfortheinclusionofrealistictradingconstraintsliketransaction
costs,slippage,andliquidityconsiderationsthatmaysignificantlyimpactactualtrading
performance. Khanetal.[42]usedafinancialsimulationmodeltoevaluateninemachine
learningmodels,incorporatingtransactioncostsandotherrealistictradingparameters.
9.6. StatisticalValidationTechniques
Variousstatisticaltechniqueshelpensuretherobustnessofpredictionmodels:
• Cross-Validation: Dividingdataintomultiplesubsetsfortrainingandvalidationto
ensureconsistentperformance.
• BootstrapResampling: Generatingmultipledatasetsbysamplingwithreplacement
toassessmodelstability.
• StatisticalHypothesisTesting: Comparingmodelperformanceagainstrandompre-
dictionsorsimplebenchmarkstoestablishstatisticalsignificance.
Thesetechniqueshelpaddressconcernsaboutdatasnoopingandoverfitting,which
areparticularlyrelevantinfinancialpredictionwherethesignal-to-noiseratiomaybelow.
9.7. BenchmarkComparisons
Meaningfulevaluationrequirescomparisonagainstappropriatebenchmarks:
• Buy-and-Hold Strategy: A passive investment approach that serves as a common
benchmark.
• SimpleTechnicalIndicators: Basictradingrulesbasedonmovingaveragesorother
commonindicators.
• Market Indices: Comparison against relevant market indices to assess relative
performance.
Arévaloetal.[34]comparedtheirpatternrecognitiontradingsystemagainstboththe
approachofCervelló-Royoetal.[33]andabuy-and-holdstrategy,demonstratingsuperior
performanceintermsofbothprofitandrisk.
9.8. Multi-CriteriaEvaluation
Giventhemultifacetednatureoftradingperformance,manystudiesemploymulti-
criteriaevaluationframeworks:
• Risk–ReturnAnalysis:Evaluatingbothreturnsandassociatedriskstoprovideamore
completeperformancepicture.

Electronics2025,14,1721
27of48
• PerformanceAcrossMarketRegimes: Assessinghowmodelsperformindifferent
marketconditions(bullmarkets,bearmarkets,sidewaysmarkets).
ConsistencyofPerformance:
|     |     | •   |     | Evaluatingmodelsbasedontheconsistencyoftheir |     |     |
| --- | --- | --- | --- | -------------------------------------------- | --- | --- |
predictionsacrossdifferenttimeperiodsandmarketconditions.
Thismulti-dimensionalapproachtoevaluationprovidesamorenuancedunderstand-
ingofmodelperformancethansinglemetricslikeaccuracyorreturnsalone.
9.9. ComparativeAnalysisofPerformanceAcrossStudies
Tofacilitatedirectcomparisonbetweendifferentapproaches,Table3presentsacom-
prehensiveoverviewofperformancemetricsacrosskeystudiesinthefield. Thiscompar-
isonrevealsseveralimportantpatterns: ensemblemethodsconsistentlyachievehigher
directionalaccuracythansingleclassifiers,hybridapproachesintegratingalternativedata
sourcesoftenshowsuperiorperformance,anddeeplearningmodelsgenerallyoutperform
traditionalapproachesatshortertimehorizonswhiletree-basedensemblemethodsexcel
atmediumtolongerhorizons.
Notably,thereportedperformancemetricsvarysubstantiallybasedonmarketcondi-
tions,evaluationperiods,andimplementationdetails. Studiesthatincorporatetransaction
costsandothermarketfrictionstypicallyreportmoremodestbutrealisticperformance
figures. Thisunderscorestheimportanceofcomprehensiveevaluationframeworksthat
considerbothstatisticalsignificanceandeconomicrelevance,asdiscussedinSection9.3.
Table3.ComparativeanalysisofperformancemetricsacrosskeyAIstockpredictionstudies.
Study ModelType Dataset/Market Directional Sharpe Returns Transaction KeyFindings
|     |     |     | Accuracy(%) | Ratio | (%) | CostsIncluded |
| --- | --- | --- | ----------- | ----- | --- | ------------- |
ExtraTreesoutperformed
Pagliaro(2023)
ExtraTreesClassifier S&P500 86.1 1.93 14.35 Yes RandomForest(73%)for10-day
[43]
windows
| Fischerand |     |     |     |     |     | LSTMoutperformedDNN, |
| ---------- | --- | --- | --- | --- | --- | -------------------- |
S&P500
Krauss(2018) LSTM 53.2 0.77 45.93 Yes RandomForest,andlogistic
constituents
| [6]        |              |           |       |      |       | regression                    |
| ---------- | ------------ | --------- | ----- | ---- | ----- | ----------------------------- |
| Khanetal.  |              |           |       |      |       | 15minintervalsprovidedoptimal |
|            | RandomForest | NASDAQ100 | 91.27 | 1.62 | 20.38 | Yes                           |
| (2023)[42] |              |           |       |      |       | predictionwindow              |
Huetal.(2018) BPNNwithGoogle S&P500and GoogleTrendsdatasignificantly
|      |        |      | 86.81 | 1.36 | 19.63 | Yes                        |
| ---- | ------ | ---- | ----- | ---- | ----- | -------------------------- |
| [25] | Trends | DJIA |       |      |       | improvedpredictionaccuracy |
Deyetal.(2016) XGBoost Appleand 87–99 N/A 32.46 No XGBoostshowedsuperior
| [38]        |                      | Yahoostocks |     |     |     | accuracyforlong-termprediction |
| ----------- | -------------------- | ----------- | --- | --- | --- | ------------------------------ |
| Bollenetal. | Self-OrganizingFuzzy |             |     |     |     | Twittersentimentanalysis       |
(2011)[22] NeuralNetwork DJIA 87.6 1.28 15.27 Yes improvedpredictionaccuracy
| Ballingsetal. |                   | Europeanand  |             |             |            | RandomForestconsistently         |
| ------------- | ----------------- | ------------ | ----------- | ----------- | ---------- | -------------------------------- |
|               | Ensemblemethods   |              | 68.2        | 0.82        | 9.68       | Yes                              |
| (2015)[40]    |                   | USstocks     |             |             |            | outperformedsingleclassifiers    |
| Dingetal.     | NeuralTensor      |              |             |             |            | Eventembeddingsimproved          |
|               |                   | S&P500       | 64.21       | 0.63        | 6.89       | No                               |
| (2015)[23]    | Network+DeepCNN   |              |             |             |            | indexpredictionby6%              |
| Wangetal.     | KnowledgeGraph+   | Chinese      |             |             |            | Graph-basedapproaches            |
|               |                   |              | 73.8        | 1.43        | 17.62      | Yes                              |
| (2023)[64]    | GCN               | A-shares     |             |             |            | capturedinter-stockrelationships |
|               |                   |              | 62.3(LSTM)  | 0.72(LSTM)  | 8.3(LSTM)  | LSTMshowedadvantagefor           |
| WuandChen     | LSTMvs.ARIMA      | S&P500       |             |             |            | Yes short-termprediction,ARIMA   |
| (2023)[48]    |                   | constituents |             |             |            |                                  |
|               |                   |              | 58.1(ARIMA) | 0.51(ARIMA) | 5.9(ARIMA) | comparableforlong-termforecasts  |
| JangandSeong  | DeepReinforcement |              |             |             |            | RL-basedportfoliooptimization    |
|               |                   | S&P500       | N/A         | 1.76        | 21.35      | Yes                              |
| (2023)[66]    | Learning(DDPG)    |              |             |             |            | outperformedbenchmarkindices     |
Imagerepresentationoffinancial
| Sezeretal. |     | BIST100Index |     |     |     |     |
| ---------- | --- | ------------ | --- | --- | --- | --- |
CNN(image-based) 72.5 0.91 10.75 Yes timeseriesimprovedpattern
| (2018)[47] |     | (Turkey) |     |     |     |     |
| ---------- | --- | -------- | --- | --- | --- | --- |
recognition
10. ChallengesandLimitations
DespitesignificantadvancesinAI-basedstockmarketprediction,severalimportant
challengesandlimitationsremain.

Electronics2025,14,1721 28of48
10.1. TheoreticalChallenges
• Efficient Market Hypothesis: The EMH suggests that predictable patterns should
quicklydisappearastheybecomeknown,creatingafundamentalchallengeforpredic-
tionmodels.
• Non-Stationarity: Financialmarketsarenon-stationaryenvironments,meaningthat
statistical properties change over time, potentially invalidating models trained on
historicaldata.
• ComplexCausality: Stockpricesareinfluencedbyacomplexweboffactorsincluding
macro-economicconditions,companyfundamentals,marketsentiment,andglobal
events,makingcausalmodelingextremelydifficult.
10.2. TheEfficientMarketHypothesisParadoxandAI-BasedPrediction
10.2.1. ReconcilingPredictionModelswithMarketEfficiency
TheapparentsuccessofAI-basedpredictionmodelspresentsatheoreticalparadox
whenconsideredalongsidetheEfficientMarketHypothesis(EMH).Ifmarketsaretruly
efficientaspositedbythestrongformofEMH,thenpredictablepatternsshouldbequickly
identifiedandarbitragedawaybymarketparticipants,renderingsystematicprediction
impossible. Yet empirical evidence suggests that prediction models can achieve above-
chanceaccuracy. Thissectionexploresthisparadoxanditsimplications.
ThetraditionalEMHframeworkcanbereconciledwithpredictivemodelingthrough
severaltheoreticalandpracticalconsiderations:
• Degrees of Market Efficiency: Markets may not be uniformly efficient across all
assets,timeframes,andconditions. Lo’sAdaptiveMarketHypothesis[98]proposes
thatmarketefficiencyisnotanall-or-nothingpropertybutevolvesdynamicallyas
market participants adapt. This evolutionary perspective suggests that temporary
inefficienciescanexistandbeexploitedbeforebeingarbitragedaway.
• ImplementationConstraints: Evenwheninefficienciesareidentified,practicallimita-
tionsoftenpreventtheircompleteelimination:
– Transactioncostscreatea“no-arbitrageband”withinwhichinefficienciescanpersist
– Capitalconstraintslimitarbitragecapacity
– Riskaversionmaydetertradersfromfullyexploitingidentifiedpatterns
– Institutionalconstraintssuchasinvestmentmandatesmaypreventcertainmarket
participantsfromengaginginarbitrage
• MarketMicrostructure: High-frequencypatternsmaypersistduetostructuralele-
mentsofmarkets:
– Orderflowdynamicscreatepredictableshort-termpricepressures
– Marketmakerinventorymanagementgeneratesmean-revertingpatterns
– Regulatorycircuitbreakersandtradinghaltscreatepredictablerecoverypatterns
10.2.2. EmpiricalEvidenceofPersistentAnomalies
Severalwell-documentedmarketanomalieshavepersisteddespitebeingwidelyknown:
• Momentum Effect: Jegadeesh and Titman’s [99] momentum strategy continues to
showeffectivenessacrossmultiplemarketsdecadesafterpublication,thoughwith
diminishedmagnitude[100].
• Post-EarningsAnnouncementDrift: Stockpricescontinuetodriftinthedirection
ofearningssurprisesforweeksfollowingannouncements,despitethispatternbeing
documentedsincethe1960s[101,102].

Electronics2025,14,1721 29of48
• Calendar Effects: Seasonal patterns like the January effect and day-of-week ef-
fects have weakened but not disappeared entirely despite their widespread publi-
cation[103].
The persistence of these anomalies suggests that knowledge of a pattern does not
necessarilyeliminateit,contradictingthestrongestformsofEMH.
10.2.3. AI’sRoleinanAdaptiveMarketFramework
AImethodsmayofferadvantageswithinthisadaptivemarketframework:
• PatternComplexity: Machinelearningalgorithmscanidentifycomplex,non-linear
patternsthatmaybeinvisibletohumantradersorsimplestatisticaltests,creatinga
temporaryinformationadvantage.
• Adaptation Speed: Deep learning models can be retrained as market conditions
change,potentiallyadaptingfasterthanthemarket’soveralladjustmentprocess.
• Multi-dimensionalAnalysis: AIsystemscansimultaneouslyprocessdiversedata
sources(pricedata,fundamentals,sentiment,alternativedata)atscalesbeyondhuman
capacity,identifyinginefficienciesattheintersectionofmultiplefactors.
• Temporal Advantage: Even if patterns eventually disappear, early identification
throughsuperiorcomputationalmethodsmayprovideatemporaryedgebeforemar-
ketsfullyincorporateinformation.
A critical review by Gu et al. [71] demonstrated that machine learning methods
systematicallyoutperformedtraditionalapproachesinpredictingthecross-sectionofstock
returns, with the advantage persisting even after accounting for transaction costs and
publishedanomalies. ThissuggeststhatAImayindeedidentifyexploitablepatternsbefore
theyarearbitratedaway.
10.2.4. EpistemologicalLimitations
Despitetheseconsiderations,fundamentalepistemologicalquestionsremain.
• PublicationEffect: DoespublishingAImethodsforstockpredictionacceleratetheir
obsolescence?
• PerformanceDecay: HowquicklydotheadvantagesofAIpredictionmethodsdecay
overtime?
• Distinguishing Skill from Luck: Given the low signal-to-noise ratio in financial
markets,whatthresholdofevidenceisneededtoestablishthatAIpredictionsreflect
genuineinefficienciesratherthanstatisticalartifacts?
ThesequestionssuggestthatwhileAIpredictionmethodsmayidentifytemporary
inefficiencies,theireffectivenessislikelytobedynamicratherthanstatic,requiringcontin-
uousinnovationtomaintainanypredictiveadvantage.
ThehistoricalevolutionofpredictionmethodologiesshowninFigure4reflectsthe
progressionfromsimplestatisticalmethodstocomplexAIapproaches,eachattemptingto
captureincreasinglysubtlemarketinefficiencies.

Electronics2025,14,1721 30of48
Figure4.Evolutionandinterrelationshipofstockmarketpredictionmethodologiesfromthe1950sto
2020s.ThetimelineshowstheprogressionfromstatisticalmethodsthroughtraditionalMLanddeep
learningtoadvancedapproacheslikegraphneuralnetworks,reinforcementlearning,andcausal
inference,withkeyparadigmshiftshighlightedatthebottom.
10.3. MarketMicrostructureandTime-ScaleDependentPredictability
Marketmicrostructure—thestudyofhowspecifictradingmechanismsaffectprice
formation—playsacrucialroleindeterminingtheeffectivenessofpredictionmodelsacross
differenttimehorizons. WhileseveralstudieshavedemonstratedtheefficacyofAImodels
for marketprediction, their performancevaries significantly based onthe time scaleof
prediction,largelyduetodifferentmicrostructuralfactorsdominatingateachlevel.
10.3.1. Time-ScaleHierarchyofPredictability
Predictioneffectivenessexhibitsdistinctivepatternsacrossdifferenttimehorizons,
whichcanbecategorizedasfollows:
• Ultra-high-frequencydomain(millisecondstoseconds): Atthisscale,predictability
isprimarilydrivenbyorderflowimbalances,marketmakerinventorymanagement,
andlatencyarbitrageopportunities. Researchhasfoundthatorderbookimbalances
can predict short-term price movements with high accuracy, while market maker
positioning creates micro-patterns that persist despite their theoretical inefficiency
accordingtotheEMH.
• Intraday time scales (minutes to hours): At this intermediate frequency, market
impacteffectsfrominstitutionalorderexecutioncreatetemporarypricepressuresand
mean-reversionpatterns. Largeorderssplitintosmallertranchescreatepredictable
price trajectories that AI models can potentially exploit. As noted in our review,
Khanetal.[42]foundthat15minintervalsprovideanoptimalwindowformachine
learningmodels,withRandomForestachieving91.27%accuracyatthisscale.

Electronics2025,14,1721 31of48
• Dailyandweeklyhorizons:Asthetimescaleextends,informationdiffusionratesand
behavioralfactorsbecomemoresignificant. Marketunderreactionandoverreaction
patternscreatemulti-daypredictability. Ouranalysisshowsthatensemblemethods
like Extra Trees Classifiers maintain effectiveness at this scale, with Pagliaro [43]
reportingaccuracyratesof86.1%for10-daywindows.
• Monthlyandlongerhorizons: Atthisscale,fundamentalfactorsandmacroeconomic
conditionsdominate. Traditionalstatisticalmethodsbecomemorecompetitivewith
advanced AI approaches, as demonstrated by Campbell and Thompson [79], who
foundthatsimplemodelswithverylowR2 valuescanstillgenerateeconomicvalue
atlongerhorizons.
10.3.2. Liquidity-BasedPredictability
Marketliquidityvariationscreatedifferentialpredictabilityacrosssecurities:
• Marketdepthvariationsacrossdifferentsecuritiescreatevaryinglevelsofpriceimpact,
withlessliquidsecuritiestypicallyexhibitinghigherpredictability.
• Bid–askspreaddynamicscangeneratepredictablepatterns,particularlyduringperi-
odsofliquiditystress.
• Orderbookshapeprovidespredictivesignalsthatarestrongerinmarketswithlower
tradingvolume,withseveralstudiessuggestingthatdeeplearningmodelstrained
on limit order book data show significantly higher accuracy for small-cap versus
large-capstocks.
10.3.3. MarketDesignEffects
Thespecificrulesandmechanismsofmarketoperationcreatemicrostructuralpatterns:
• Tradinghalts,circuitbreakers,andothermarketrulescreatediscontinuitiesthatAI
models can learn to anticipate, including predictable recovery patterns following
tradinghaltsthatpersistdespitewidespreadknowledgeoftheirexistence.
• Differentexchangemechanisms(continuousauctionvs. periodiccallauctions)gener-
atedistinctpredictabilitypatterns,withhigh-frequencytradingstrategiesperforming
differentlyundercontinuousversusdiscrete-timetradingmechanisms.
• Fragmentationacrossmultipletradingvenuescreatescross-venuearbitrageopportuni-
ties,withresearchsuggestingthatpredictabilityincreaseswithmarketfragmentation.
10.3.4. Cross-AssetandCross-MarketInformationFlow
Informationtransmissioncreatesexploitablepatterns:
• Informationtypicallyflowsfrommoreliquidtolessliquidassets,creatingapredictabil-
itygradient.Ithasbeenwelldocumentedhowpricediscoveryinfuturesmarketsoften
leadsthecorrespondingcashindicesbyseveralminutes,creatingpredictablepatterns.
• Pricediscoveryprocessoccursatdifferentratesacrossrelatedinstruments,allowing
for the measurement of information share across markets and the identification of
priceleadership.
• Modelsleveragingtheseinformationtransmissiondelayshaveshownstrongerperfor-
manceatspecifictimescales. Severalstudiesinourreview,includingShenetal.[36]
andHuetal.[25],demonstratedimprovedaccuracybyincorporatingcross-market
signals, with prediction accuracy improvements of 2–5% when integrating related
marketdata.
Oursynthesisoftheliteraturerevealsclearpatternsinhowpredictiveaccuracyvaries
acrosstimescales:

Electronics2025,14,1721 32of48
• Short time horizons (seconds to minutes): Deep learning approaches like LSTM
networkstendtoexcel,asdemonstratedbyFischerandKrauss[6],whofoundthat
LSTMmodelsoutperformtraditionalapproachesinshort-termforecastingtasks.
• Mediumtimehorizons(minutestohours): RandomForestmodelsshowparticular
strength,withKhanetal.[42]reporting91.27%accuracyusing15minintervals.
• Daily prediction windows: Ensemble methods remain effective, with tree-based
methodslikeXGBoostshowingstrongperformance,asreportedbyDeyetal.[38].
• Multi-day to weekly horizons: Extra Trees Classifier models have demonstrated
superioraccuracy(86.1%)for10-daypredictionwindowsaccordingtoPagliaro[43].
• Longerhorizons: TheadvantageofcomplexAImethodsdiminishes,withtraditional
statisticalapproachesbecomingmorecompetitive,asCampbellandThompson[79]
demonstrated.
Thesefindingsrevealimportantinsights: deeplearningapproachestendtoexcelat
shortertimehorizonswherecomplexmicrostructuralpatternspredominate,whileensem-
blemethodslikeExtraTreesandRandomForestdemonstratesuperiorperformanceatinter-
mediatetolongerhorizonswherefundamentalsandtrendfactorsbecomemoresignificant.
Thistime-scale-dependentperformancehasprofoundimplicationsformodelselection,
featureengineering,andimplementationstrategies. Itsuggeststhatoptimalprediction
systemsshouldemploydifferentalgorithmicapproachesbasedontheintendedtrading
frequency, with hybrid models potentially offering the best solution for multi-horizon
forecasting.
10.3.5. MarketCapitalizationEffectsonPredictability
Ouranalysisalsorevealsasignificantrelationshipbetweenmarketcapitalizationand
predictability. Smaller-cap stocks generally exhibit higher predictability across all time
scales. This pattern is consistent with the notion that market efficiency increases with
liquidityandattention,makinglarger,moreheavilytradedsecuritieslesssusceptibleto
predictivemodeling. Thisalignswiththefindingsofseveralstudiesinourreviewthat
showdegradedmodelperformancewhenmovingfrombroadermarketindicestolarge-cap
stocksubsets.
Thesemicrostructuralconsiderationsprovideessentialcontextforunderstandingboth
thetheoreticalandpracticallimitationsofAI-basedstockmarketprediction. Theyhelp
explainwhycertainmodelssucceedinspecificcontextswhilefailinginothersandwhy
evensuccessfulstrategiesmayhavelimitedcapacityordurationbeforemarketadaptation
eliminatestheiredge.
10.4. DataChallenges
• DataQuality: Financialdatamaycontainerrors,missingvalues,orinconsistencies
thatcanimpactmodelperformance.
• Limited History: Many newer financial instruments have limited historical data,
makingitdifficulttotrainrobustmodels.
• SurvivorshipBias: Datasetsthatincludeonlycurrentlyexistingcompaniescancreate
survivorshipbias,potentiallyleadingtooverlyoptimisticpredictions.
• FeatureSelection: Identifyingthemostrelevantfeaturesamongnumerouspotential
predictors remains challenging, with different features potentially having varying
importanceacrossdifferentmarketregimes.
10.5. MethodologicalChallenges
• Overfitting:ThecomplexityofmodernMLmodelscreatessignificantriskofoverfitting
tohistoricalpatternsthatlackpredictivevalueforfuturemovements.

Electronics2025,14,1721 33of48
• ParameterSensitivity: Manymodelsarehighlysensitivetohyperparametersettings,
requiringextensivetuningandvalidation.
• BlackBoxModels:Advanceddeeplearningmodelsoftenlackinterpretability,making
itdifficulttounderstandthebasisfortheirpredictions.
• TransferLearning: Modelstrainedononemarketortimeperiodmaynottransfer
effectivelytoothercontexts,limitingtheirpracticalutility.
10.6. ImplementationChallenges
• Transaction Costs: Trading costs can significantly reduce or eliminate theoretical
profitsfrompredictionmodels.
• ExecutionSlippage: Delaysbetweenpredictionandexecutioncanleadtodifferent
pricesthananticipated.
• MarketImpact: Largetradescanthemselvesmovethemarket,potentiallyreducingor
eliminatingpredictedprofitopportunities.
• RegulatoryConstraints: Tradingstrategiesmaybesubjecttoregulatoryrestrictions
thatlimittheirimplementation.
10.7. ReproducibilityChallenges
Financialpredictionresearchfacesasignificantreproducibilitycrisisthatmeritscareful
consideration. Thissectionexaminestheextentofthischallengeanditsimplicationsfor
evaluatingAIpredictionmodels.
10.7.1. TheReplicationCrisisinFinancialPrediction
The replication crisis in financial prediction research represents a fundamental
challenge to the field’s credibility. Several meta-analyses have quantified the scope of
thisproblem:
• Harveyetal.[83]conductedacomprehensivereviewof316publishedfinancialanoma-
liesandfoundthat60–80%failedtoreplicatewhensubjectedtomorestringentstatisti-
caltests,withmostpublishedresultslikelyrepresentingfalsepositives.
• Houetal.[104]re-examined452cross-sectionalanomaliesanddiscoveredthat65%
failedtoreplicatewithupdateddataandpropercontrolsformicrocapstocks.
• ChenandZimmermann[105]documentedthattheaveragereturnpredictabilityof
publishedstrategiesdeclinedbyabout32%afterpublication,suggestingeitherdata
miningormarketadaptation.
Thiscrisisextendstomachinelearningapplicationsinfinance,wherethecombination
offlexiblemodels,numeroushyperparameters,andlimiteddataexacerbatesreproducibil-
itychallenges.
10.7.2. CaseStudiesinFailedReplication
AsshowninTable4,severalnotablecasesillustratethereproducibilitychallengesin
financialprediction.

Electronics2025,14,1721 34of48
Table4.Examplesofinitiallypromisingmethodswithsubsequentreplicationfailures.
Method/Study OriginalClaim ReplicationOutcome
Januaryeffectprovidesexcess Schwert[107]foundthattheeffect
CalendarEffects[106]
returnsof3% disappearedpost-publication
Movingaveragestrategies
Sullivanetal.[90]foundnosignificance
TechnicalAnalysis[89] generatesignificantabnormal
aftermultipletestingcorrection
returns
ANNspredictIBMdailystock Refutedbysubsequentstudieswith
NeuralNetworks[108]
returns out-of-sampletesting[109]
Mediapessimismpredicts LoughranandMcDonald[111]showed
SentimentAnalysis[110]
marketdownturns sensitivitytolexiconchoice
LSTMoutperformsclassic LopezdePrado[112]showedresults
DeepLearning[6]
models sensitivetodatapreparation
10.7.3. RootCausesofReplicationFailures
Severalsystematicfactorscontributetothereplicationcrisis:
• PublicationBias: Journalstendtopublishstudieswithpositiveandsignificantresults,
creatingabiasedliteraturethatoverrepresentssuccessfulpredictions.
• BacktestOverfitting: Baileyetal.[113]demonstratedthattherepeatedbacktestingof
strategiesagainstthesamehistoricaldatainevitablyleadstofalsediscoveriesthrough
theoptimizationofstrategyparameters.
• P-hacking:Someengageinthepracticeoftestingmultiplehypotheses,models,orspec-
ificationsuntilstatisticallysignificantresultsareachieved,withoutappropriatecorrec-
tionsformultipletesting.
• DataSnooping: LópezdePrado[14]identifiedthatstandardcross-validationfailsin
sequentialdata,leadingtoinformationleakageandinflatedperformanceestimates.
• Non-stationarity: Financial markets evolve over time, and patterns discovered in
oneperiodmaynotpersistinfutureperiodsduetochangingmarketconditionsor
adaptationbymarketparticipants.
10.7.4. MethodologicalStandardsforRobustFinancialPredictionResearch
Toaddressthesechallenges,weproposethefollowingmethodologicalstandardsfor
futureresearch:
• ProperOut-of-SampleTesting: Researchersshouldmaintainatrulyuntouchedvali-
dationdatasetforfinalmodelevaluation. Walk-forwardanalysis,wheremodelsare
retrainedasnewdatabecomeavailable, providesamorerealisticassessmentthan
standardcross-validation.
• MultipleTestingCorrections: Studiesshouldapplyfamily-wiseerrorratecontrols
(e.g.,Bonferronicorrection)orfalsediscoveryratemethods(e.g.,Benjamini–Hochberg
procedure)whentestingmultiplehypothesesormodelspecifications.
• CombinatorialPurgedCross-Validation: AsproposedbyLópezdePrado[14],this
techniquepreventsinformationleakageinfinancialtimeseriesbypurgingoverlapping
observationsandembargoestoaccountforserialcorrelation.
• StatisticalPowerAnalysis: Researchersshouldconductaprioripoweranalysisto
ensurethatsamplesizesareadequatefordetectingtheexpectedeffectsizes,reducing
theriskofbothfalsepositivesandfalsenegatives.
• RegisteredReports: Followingpracticesfrommedicalresearch,pre-registeringhy-
potheses,datacollectionprocedures,andanalysisplansbeforeconductingresearch
canmitigatep-hackingandpublicationbias.
• CodeandDataSharing:Makingcodeanddatapubliclyavailableenablesindependent
verificationandimprovesreproducibility.

Electronics2025,14,1721 35of48
• EnsembleMethods:Combiningmultiplemodelswithdifferentassumptionsandstart-
ingpointscanprovidemorerobustpredictionsandmitigatetheimpactofindividual
modeloverfitting.
10.7.5. ImplicationsforAI-BasedStockPrediction
ThereplicationcrisishasprofoundimplicationsforAI-basedstockpredictionresearch:
• Modelperformancereportedintheacademicliteratureshouldbetreatedwithgreater
skepticism,particularlywhenout-of-sampletestingislimitedorabsent.
• Thecomplexityofdeeplearningmodels,withtheirnumeroushyperparametersand
architecturalchoices,makesthemparticularlysusceptibletooverfittinganddifficult
toreplicate.
• AImodelstrainedonhistoricalmarketdatamayinadvertentlycapturenoiserather
thansignals,especiallywhenthenoise-to-signalratioishigh.
• Methods that explicitly account for estimation uncertainty, such as Bayesian ap-
proaches,mayprovidemorereliableinsightsthanpointestimatesofpredictedreturns
orprobabilities.
Addressingthereplicationcrisisrequiresafundamentalshiftinhowfinancialpredic-
tionresearchisconducted,evaluated,andapplied,withgreateremphasisonmethodologi-
calrigorandrealisticperformanceassessment.
10.8. EvaluationChallenges
• PerformanceMetrics: Differentevaluationmetricscanleadtodifferentconclusions
aboutmodelperformance.
• Backtest Overfitting: The excessive optimization of models to historical data can
createmisleadingperformancemetrics.
• Out-of-Sample Validation: Proper out-of-sample validation is essential but often
implementedinconsistentlyacrossstudies.
• PublicationBias: Theremaybepublicationbiastowardmodelsthatshowpositive
results,potentiallycreatinganoverlyoptimisticviewofthefield’sprogress.
Thesechallengeshighlighttheneedforcontinuedmethodologicalinnovation,rigorous
validationapproaches,andrealisticexpectationsaboutthecapabilitiesandlimitationsof
AI-basedstockpredictionmodels.
10.9. HardwareImplicationsandComputationalEfficiency
AnoftenoverlookedyetcriticalaspectofAI-basedstockpredictionsystemsistheir
varyingcomputationalrequirements. Differentapproachespresentsubstantialtrade-offs
betweenpredictionaccuracyandcomputationalefficiencythatdirectlyimpacttheirpracti-
calimplementation.
10.9.1. ComputationalRequirementsAcrossModelClasses
Table5summarizesthecomputationalcharacteristicsofmajormodelclassesusedin
stockprediction,highlightingthesignificantvariationinresourcedemands.

Electronics2025,14,1721
36of48
Table5.Computationalrequirementsofdifferentstockpredictionmodels.
|                             |               | Inference | Memory       | Hardware     |
| --------------------------- | ------------- | --------- | ------------ | ------------ |
| ModelType                   | TrainingTime  |           |              |              |
|                             |               | Latency   | Requirements | Acceleration |
| Statistical(ARIMA,ESM)      | VeryLow       | VeryLow   | Minimal      | NotRequired  |
| DecisionTrees               | Low           | VeryLow   | Low          | NotRequired  |
| RandomForest/ExtraTrees     | Medium        | Low       | Medium       | Beneficial   |
| GradientBoosting(XGBoost)   | Medium        | Low       | Medium       | Beneficial   |
| SupportVectorMachines       | Medium-High   | Medium    | Medium       | Beneficial   |
| ShallowNeuralNetworks       | Medium        | Low       | Medium       | Beneficial   |
| ConvolutionalNeuralNetworks | High          | Medium    | High         | Required     |
| LSTM/RNN                    | VeryHigh      | High      | High         | Required     |
| Transformer-basedModels     | ExtremelyHigh | High      | VeryHigh     | Required     |
| GraphNeuralNetworks         | VeryHigh      | High      | VeryHigh     | Required     |
Ouranalysisrevealsseveralkeyfindingsregardingcomputationalefficiency.
10.9.2. HardwareAccelerationRequirements
Deeplearningmodelsdemonstratefundamentallydifferentscalingpropertiescom-
paredtotraditionalapproaches:
• GPUAcceleration: FischerandKrauss[6]reportedthatLSTMmodelsrequiredGPU
acceleration to achieve practical training times, with a 15x speedup compared to
CPU-onlytraining. TheirimplementationonanNVIDIATeslaV100required36hfor
training,comparedtoestimatedweeksonCPUarchitectures.
• MemoryBandwidth: Wangetal.[60]notedthattheirknowledgegraph-basedGCN
implementation was primarily memory-bandwidth limited rather than compute-
bound,withloadingtheentiremarketgraphrequiring24GBofGPUmemory.
• InferenceLatency: Forhigh-frequencyapplications,Sezeretal.[11]foundthatCNN
modelsachieved2msinferencetimesonGPUsbut45msonCPUs,makinghardware
accelerationessentialforreal-timeapplicationsrequiringsub-10msresponsetimes.
| 10.9.3. ComputationalEfficiencyvs. | PredictionAccuracy |     |     |     |
| ---------------------------------- | ------------------ | --- | --- | --- |
Ouranalysisrevealsanimportantaccuracy–efficiencyfrontier:
• Ensemble Method Efficiency: While ensemble methods like Random Forest and
ExtraTreesshowsuperiorpredictionaccuracy(asshowninTable3),theyoffersignifi-
cantlybettercomputationalefficiencythandeeplearningapproaches. Pagliaro[43]
demonstratedthatExtraTreesmodelscouldbetrainedinunder10minonastandard
workstationwhileachieving86.1%directionalaccuracy.
• ModelPruningandQuantization: StudiesbyWuetal.[50]demonstratedthatthe
quantizationandpruningofLSTMmodelscouldreducememoryrequirementsby
75%andinferencetimeby60%withonlya1.2%reductioninaccuracy,suggesting
significantopportunitiesforoptimization.
• BatchProcessingEfficiency: Khanetal.[42]showedthatbatchpredictionapproaches
could amortize computational costs, with batch sizes of 64–128 providing optimal
throughputonGPUhardwarefordailypredictiontasks.
10.9.4. DeploymentConsiderations
Thehardwarerequirementsdirectlyinfluencedeploymentoptionsandoperatingcosts:
• Cloud vs. On-Premises: Complex models like transformers and GNNs typically
requirecloud-basedGPUclustersfortraining,incurringsignificantoperationalex-
penses. Basedoncurrentcloudproviderpricing,trainingastate-of-the-arttransformer

Electronics2025,14,1721 37of48
modelformarketpredictioncancostbetweenUSD2000and10,000incomputere-
sourcesalone.
• EnergyEfficiency: Theenergyconsumptionofdifferentmodelsvariesdramatically:
traditionalmethodsandtree-basedensemblescanbedeployedonenergy-efficient
CPU servers, while deep learning approaches may require 10–100× more energy
duringbothtrainingandinferencephases.
• Specialized Hardware: Field-Programmable Gate Arrays (FPGAs) have shown
promise for the low-latency deployment of certain model types, with Jang and
Seong[66]reporting5×lowerlatencyforreinforcementlearninginferencecompared
toGPUimplementations.
10.9.5. ImplicationsforResearchandApplication
Thesecomputationalconsiderationshaveseveralimportantimplications.
First, accurate performance comparisons must account for computational costs; a
modelwith2%higheraccuracybut50×highercomputationalrequirementsmaynotbe
practicallysuperiorinmanyapplications. Second,thechoiceofmodelarchitectureshould
beguidedbydeploymentconstraints,particularlyforreal-timeorhigh-frequencytrading
applicationswherelatencyiscritical.
Finally,futureresearchdirectionsshouldincludebenchmarkingbothpredictionaccu-
racyandcomputationalefficiencyacrossdifferenthardwareplatforms.Thedevelopmentof
moreefficientmodelarchitecturesspecificallydesignedforfinancialtimeseriesprediction
representsanimportantfrontier,potentiallyincreasingtheaccessibilityandpracticalityof
AI-driventradingstrategiesbeyondlargeinstitutionalinvestorswithsubstantialcomputa-
tionalresources.
10.10. Cross-MarketGeneralizability
Whilethisreviewsynthesizesfindingsfromstudiesacrossvariousmarkets,important
questions remain regarding the generalizability of prediction methods across different
marketstructures,geographicregions,andeconomicconditions.
10.10.1. MarketStructureEffects
Differentmarketmicrostructuressignificantlyimpactmodelperformance:
• TradingMechanismDifferences: Studiescomparingpredictionmodelperformance
between auction markets (like NYSE) and dealer markets (like NASDAQ) reveal
systematicdifferences. Boehmeretal.[114]foundthatensemblemethodsachieve
5–8%higheraccuracyinauctionmarketscomparedtodealermarkets,likelydueto
differencesinpriceformationprocessesandtransparency.
• OrderBookDepth:Marketswithdeeperorderbooksshowdifferentpredictabilitypat-
ternscomparedtoshallowmarkets. Deeplearningapproachesexploitinglimitorder
bookdatashowsignificantlyhighereffectivenessinmarketswithrichmicrostructure
dataavailability,asdemonstratedby[115].
• TradingHours: Continuousversuscallauctionmarketsandmarketswithdifferent
tradinghourstructuresexhibitdistinctpredictabilitypatterns. SezerandOzbayoglu
[47] found that CNN-based models trained on Asian markets required significant
adaptationtomaintainperformancewhenappliedtoEuropeanmarketswithdifferent
tradingsessionstructures.
10.10.2. GeographicandEconomicVariations
Predictivemodelsdisplayvaryingdegreesoftransferabilityacrossgeographicregions:

Electronics2025,14,1721 38of48
• Developedvs. EmergingMarkets: Whileensemblemethodsshowconsistencyacross
US and European markets [40], their performance in emerging markets like Brazil
and India demonstrates greater variation. Models optimized for the S&P 500 saw
performancedegradationwhenappliedtotheIndianNiftyindexwithoutrecalibration,
suggestingthatmarketmaturityimpactspredictability.
• MarketEfficiencyVariations: Marketswithdifferentlevelsofinformationalefficiency
requiredifferentmodelingapproaches. Urquhart[116]demonstratedthatemerging
markets show higher degrees of predictability using technical approaches, while
developedmarketsrequiremoresophisticatedalternativedataintegrationtoachieve
comparableresults.
• RegulatoryEnvironment: Differingregulatorystructures,particularlyregardingshort
selling,marginrequirements,andcircuitbreakers,impactmodeltransferability. Mod-
elstrainedinmarketswithunrestrictedshortsellingrequiredsignificantmodification
tomaintainperformanceinmarketswithshort-sellingrestrictions.
10.10.3. ResearchDesignforCross-MarketValidation
Toaddressgeneralizabilitychallenges,werecommendthefollowingresearchapproaches:
• Multi-Market Training: Training models on diverse markets simultaneously can
improve generalizability. Cao et al. [117] demonstrated that models trained on a
combinationofUS,European,andAsianmarketdatashowedimprovedrobustness
whentestedonout-of-samplemarketscomparedtosingle-markettraining.
• TransferLearning: Adoptingtransferlearningapproacheswheremodelspre-trained
ondata-richmarketsarefine-tunedforspecifictargetmarkets. ZhangandJacobsen
[103]employedthisapproachtoadaptmodelsfromUSmarketstosmallerEuropean
exchanges, achieving 85% of the original performance with only 20% of the target
markettrainingdata.
• Meta-Features: Developingmarket-invariantfeaturesthatcapturefundamentaleco-
nomicrelationshipsratherthanmarket-specificpatterns.
• Systematic Comparison Studies: Conducting more research explicitly comparing
identicalmethodologiesacrossdifferentmarkets. Followingprotocolssimilartothose
established in [118], who systematically applied identical models across 21 equity
markets,wouldprovidevaluableinsightsintogeneralizabilityconstraints.
Future research should focus specifically on identifying which aspects of market
structureandeconomicconditionsmostsignificantlyimpactmodeltransferability,poten-
tiallyleadingtoageneralizedframeworkforadaptingpredictionmodelsacrossdiverse
globalmarkets.
11. FutureResearchDirections
OurcriticalexaminationofAI-basedstockmarketpredictionresearchhasrevealed
severalsignificantgapsandunresolvedchallengesthatwarrantfurtherinvestigation.Based
onthelimitationsidentifiedthroughoutthisreview,weproposethefollowingresearch
directionsthatdirectlyaddressthemostpressingissuesinthefield.
Thegapbetweentheoreticalmodelperformanceandpracticalimplementationrepre-
sentsoneofthemostsignificantchallengesidentifiedinourreview. Manystudiesreport
impressivepredictionaccuracybutfailtodemonstrateeconomicvalueafteraccountingfor
transactioncostsandreal-worldconstraints. Futureresearchmustbridgethisgapthrough
morerealisticevaluationframeworksandimplementation-focusedstudies.
Similarly, the tension between the Efficient Market Hypothesis and documented
predictabilitypatternsrequiresmoresophisticatedtheoreticalmodelsthatcanexplainthis
apparentcontradiction. Theadaptivemarketframeworkweproposeoffersapromising

Electronics2025,14,1721 39of48
foundationbutneedsfurtherdevelopmentandempiricalvalidationacrossdiversemarket
conditionsandtimeframes.
Athirdcriticalgapinvolvesmodeltransferabilityacrossdifferentmarketregimes,
assetclasses,andgeographicregions. Ouranalysisrevealsthatmostpredictionmodels
demonstratesignificantperformancedegradationwhenappliedtodifferentmarketsor
timeperiodsthanthoseusedfortraining,highlightingtheneedformorerobustapproaches
totransferlearninganddomainadaptation.
Finally,thefieldstilllacksstandardizedbenchmarksandevaluationprotocolsthat
wouldenablemeaningfulcomparisonbetweendifferentmethodologies. Thisstandardiza-
tionisessentialforrigorousscientificprogressandpracticalimplementationguidance.
Thefollowingsubsectionsoutlinespecificresearchdirectionsthataddressthesefun-
damentalgapswhileleveragingemergingtechnologiesandmethodologicalinnovations.
11.1. AlternativeDataSources
Researchersareincreasinglyexploringnon-traditionaldatasourcesforstockprediction:
• SatelliteImagery: Usingsatellitedatatomonitoreconomicactivity,suchasparking
lotoccupancyorconstructionprogress.
• Internet of Things (IoT) Data: Leveraging IoT sensors to track physical economic
indicatorsinreal-time.
• AlternativeTextSources:Analyzingspecializedpublications,expertforums,andother
textsourcesbeyondmainstreammediaandsocialnetworks.
• PrivateCompanyData:Incorporatingdatafromprivatecompaniesandsupplychains
thatmayprovideearlysignalsofpubliccompanyperformance.
11.2. ExplainableAIforFinance
AsregulatoryscrutinyofAIinfinanceincreases,thereisgrowinginterestindevelop-
ingmoreinterpretablemodels:
• RuleExtraction: Techniquesforextractinginterpretablerulesfromcomplexmodels
likeneuralnetworks.
• FeatureImportanceAnalysis: Methodsforidentifyingwhichfeaturescontributemost
significantlytopredictions.
• Local Explanation Methods: Approaches like LIME (Local Interpretable Model-
agnosticExplanations)andSHAP(SHapleyAdditiveexPlanations)thatexplainindi-
vidualpredictions.
• AttentionMechanisms: Neuralnetworkarchitectureswithattentioncomponentsthat
highlightwhichpartsoftheinputcontributemosttotheprediction.
ExplainableAIapproachesnotonlyaddressregulatoryconcernsbutcanalsohelptraders
andinvestorsbetterunderstandmodelpredictionsandmakemoreinformeddecisions.
11.3. TransferLearningandDomainAdaptation
Transferlearningtechniquesadaptedforfinancialmarketscouldaddresschallenges
relatedtolimiteddataandchangingmarketconditions:
• Cross-Market Transfer: Transferring knowledge from well-established markets to
emergingmarketswithlimitedhistoricaldata.
• TemporalTransfer: Adaptingmodelsacrossdifferentmarketregimes(e.g.,bullmar-
kets,bearmarkets,high-volatilityperiods).
• Cross-AssetTransfer: Leveragingpatternslearnedfromoneassetclasstoimprove
predictionsforrelatedassetclasses.

Electronics2025,14,1721 40of48
• Meta-Learning: Developingmodelsthatcanquicklyadapttonewmarketconditions
withminimalretraining.
11.4. MultimodalLearning
Integratingmultipledatamodalitiescouldprovidemorerobustpredictionsbycaptur-
ingcomplementaryinformation:
• Text–Price Integration: Combining price data with textual data from news, social
media,andcompanyreports.
• Financial–Alternative Data: Integrating traditional financial data with alternative
datasourceslikesatelliteimageryorconsumerspendingpatterns.
• Cross-Market Integration: Modeling relationships between different markets and
assetclassestobettercaptureglobaleconomicdynamics.
• Temporal–SpatialIntegration: Combiningtimeseriesanalysiswithspatialanalysisto
capturegeographicandtemporalpatternsinmarketbehavior.
11.5. CausalityandCounterfactualAnalysis
Researchers can move beyond correlations to understand causal relationships in
financialmarkets:
• Causal Discovery: Identifying causal relationships between economic factors and
stockpricemovements.
• Counterfactual Analysis: Developing models that can reason about what would
happenunderdifferentscenarios.
• InterventionModels: Creatingmodelsthataccountfortheimpactofpolicychanges
ormarketinterventions.
• RobustPredictors: Developingpredictionmodelsthatrelyonstablecausalmecha-
nismsratherthanephemeralstatisticalcorrelations.
11.6. ReinforcementLearningforPortfolioManagement
Extendingreinforcementlearningbeyondindividualstockpredictiontoholisticport-
foliomanagement:
• Multi-AssetRL:Developingreinforcementlearningapproachesthatsimultaneously
managemultipleassets.
• Risk-Aware RL: Incorporating risk constraints and preferences into reinforcement
learningframeworks.
• Multi-PeriodOptimization: Addressingthechallengesoflong-termportfolioopti-
mizationunderuncertainty.
• HierarchicalRL:Usinghierarchicalreinforcementlearningtomanagedifferentinvest-
menttimehorizonsandobjectives.
11.7. FederatedandPrivacy-PreservingLearning
As data privacy regulations tighten, developing approaches that preserve privacy
whileleveragingdistributeddataisimportant:
• Federated Learning: Training models across multiple institutions without sharing
rawdata.
• DifferentialPrivacy: Implementingprivacy-preservingtechniquesthatprotectindi-
vidualdatapointswhileallowingpopulation-levelanalysis.
• SecureMulti-PartyComputation:Enablingcollaborativemodeldevelopmentwithout
exposingproprietarydataorstrategies.
• HomomorphicEncryption: Performingcomputationsonencrypteddatatopreserve
confidentiality.

Electronics2025,14,1721 41of48
Thesetechniquescouldpotentiallyunlocknewdatasourcesandcollaborationsthat
arecurrentlyrestrictedduetoprivacyconcerns.
11.8. EthicalConsiderationsandMarketImpact
AsAI-drivenpredictionsystemsbecomemoresophisticatedandwidelydeployed,
severalimportantethicalconsiderationsemerge:
• MarketFairnessandAccess: AdvancedAIsystemsrequiresubstantialcomputational
resourcesanddataaccess,potentiallycreatingorexacerbatinginequalitiesbetween
market participants with different resource levels. This raises questions about fair
marketaccessandwhetherregulationsshouldensurealevelplayingfield.
• SystemicRisk:ThewidespreadadoptionofsimilarAImodelscouldleadtocorrelated
tradingbehaviors,potentiallyamplifyingmarketmovementsandincreasingsystemic
risk. The2010FlashCrashdemonstratedhowalgorithmictradingcancontributeto
marketinstability,andmoresophisticatedAIsystemsmayintroducenewformsof
systemicvulnerability.
• TransparencyandExplainability: Asmodelsbecomemorecomplex,theirdecision-
makingprocessesbecomelesstransparent. This“blackbox”natureraisesconcerns
aboutaccountability,particularlywhenthesesystemsmanagesignificantcapitalor
influencemarketmovements.
• MarketManipulation: AIsystemsmightidentifyandexploitpatternsthateffectively
constitutemarketmanipulation,evenifnotexplicitlyprogrammedtodoso.Thisraises
questionsabouttheresponsibilityofthedevelopersanddeployersofsuchsystems.
• SocialImpact: ThebroadersocietalimpactsofAI-drivenmarkets—includingeffects
onwealthdistribution,capitalallocationefficiency,andeconomicstability—warrant
carefulconsideration. Marketsserveimportantsocialfunctionsbeyondprofitgener-
ation,andAIsystemsoptimizedsolelyforreturnsmaynotadequatelyservethese
broaderpurposes.
Theseethicalconsiderationssuggesttheneedforinterdisciplinaryapproachescom-
biningtechnicalexpertisewithinsightsfromeconomics,law,andethics. Futureresearch
shouldexploreframeworksforresponsibleAIdeploymentinfinancialmarkets,including
appropriategovernancestructures,monitoringsystems,andregulatoryapproachesthat
balanceinnovationwithmarketintegrityandsocialwelfare.
11.9. PracticalImplementationandFinancialImplications
ThetranslationofAIpredictionsintoactionabletradingstrategiesrequiresthecareful
considerationofpracticalimplementationchallengesandfinancialimplications.
11.9.1. FromPredictionstoTradingDecisions
Convertingmodeloutputsintoeffectivetradingdecisionspresentsseveralchallenges:
• DecisionThresholds:Determiningappropriatethresholdsforconvertingprobabilistic
predictions into discrete trading decisions significantly impacts performance. Fis-
cher and Krauss [6] demonstrated that LSTM-based predictions, while statistically
significant,generatedeconomicallymeaningfulreturnsonlywhenimplementedwith
optimizeddecisionthresholdsthatvariedbymarketvolatilityregime.
• PositionSizing: Theallocationofcapitalbasedonpredictionconfidencefundamen-
tallyaffectsrisk–returnprofiles. Pagliaro[43]showedthatimplementingconfidence-
weightedpositionsizingwithExtraTreesClassifierpredictionsincreasedSharperatios
by31%comparedtouniformpositionsizing.
• Holding Periods: Optimizing holding periods based on prediction horizons and
marketconditionscansignificantlyenhanceperformance. Khanetal.[42]foundthat

Electronics2025,14,1721 42of48
dynamicholdingperiodsadjustedforvolatilityoutperformedfixedholdingperiods
evenwhenusingidenticalpredictionmodels.
11.9.2. PortfolioConstructionConsiderations
TheintegrationofAIpredictionsintoportfolioconstructioninvolvesthefollowing:
• Diversification Effects: The proper diversification of model-driven positions can
reduceriskwithoutproportionatelyreducingreturns. JangandSeong[66]demon-
stratedthatreinforcementlearningapproachesthatexplicitlyaccountforcorrelations
between AI-predicted positions achieved 27% lower maximum drawdowns while
maintainingsimilarreturns.
• RiskConstraints: Implementingrisklimitsandconstraintsensuresportfoliostability
acrossmarketconditions. Wuetal.[67]showedthatincorporatingdownsiderisk
measures like Conditional Value at Risk (CVaR) into GAN-based trading models
improvedworst-casescenariooutcomeswhilesacrificingonlymarginalreturns.
• Multi-ModelIntegration: Combiningpredictionsfromdiversemodelscanenhance
robustness. Wangetal.[64]foundthatensemblingpredictionsfromgraph-basedmod-
elswithtraditionaltree-basedapproachesreducedpredictionvarianceandimproved
consistencyacrossmarketregimes.
11.9.3. TransactionCostOptimization
Transactioncostsfundamentallyimpacttheeconomicviabilityofprediction-based
strategies:
• TradingFrequencyOptimization: Theoptimaltradingfrequencydependsonthe
relationshipbetweensignaldecayandtransactioncosts. Lvetal.[62]demonstrated
thatdailyrebalancingwasoptimalfordeeplearningmodelsappliedtoliquidlarge-
capstocks,whileweeklyrebalancingprovedmoreeffectiveforlessliquidsmall-cap
stocksduetohighertransactioncosts.
• SmartOrderRouting: Executionalgorithmsthatminimizemarketimpactcanpre-
servestrategyreturns. Studieshaveshownthatimplementationshortfallduetosub-
optimalexecutioncanreducetheoreticalstrategyreturnsby15–40%inpractice[119].
• Tax Efficiency: For investment applications, tax consequences of trading activity
significantlyimpactafter-taxreturns. Incorporatingtax-awareexecutionrulesinto
prediction-based strategies improves after-tax returns annually while maintaining
pre-taxperformance.
11.9.4. InstitutionalImplementationChallenges
ThedeploymentofAIpredictionsystemsininstitutionalcontextspresentsunique
challenges:
• GovernanceFrameworks: EstablishingappropriateoversightandgovernanceforAI
tradingsystemsremainschallenging.
• AlignmentwithInvestmentPolicy: EnsuringAIpredictionmodelsoperatewithin
institutionalinvestmentpolicyconstraintsrequirescarefuldesign. Bartrametal.[120]
demonstrated approaches for incorporating ESG constraints, concentration limits,
andotherpolicyrequirementsintoprediction-basedportfolioconstruction.
• PerformanceAttribution: AccuratelyattributingperformanceinAI-augmentedin-
vestment processes presents analytical challenges. Daul et al. [121] developed a
frameworkfordecomposingreturnsintocomponentsattributabletotheAIprediction
modelversustraditionalfactors,providinggreatertransparencyforstakeholders.

Electronics2025,14,1721 43of48
Future research should focus on bridging the gap between theoretical model per-
formanceandpracticalimplementation,withparticularemphasisondevelopingrobust
frameworksfortranslatingstatisticaladvantagesintosustainableeconomicvalueacross
diversemarketconditionsandinstitutionalcontexts.
12. Conclusions
Thiscomprehensivereviewhascriticallyexaminedartificialintelligenceapplications
instockmarketforecasting,synthesizingfindingsacrossstatisticalmethods,patternrecog-
nitionapproaches,machinelearningmodels,sentimentanalysistechniques,andhybrid
systems. Ourcriticalreviewoftheliteraturerevealsseveralfundamentalinsightsthathave
significantimplicationsforboththeoryandpractice.
12.1. KeyFindingsandTheoreticalImplications
First,oursynthesisoftheliteraturedemonstratesaclearmethodologicalevolutionin
predictiveapproaches,withensemblemethods—particularlyRandomForest,ExtraTrees,
andgradientboostingtechniques—consistentlydemonstratingsuperiorpredictiveperfor-
manceacrossmultiplemarketsandtimehorizons. Yetthisevolutionraisesanunresolved
tension between the Efficient Market Hypothesis and empirical evidence of AI-driven
predictability. Weproposethatanadaptivemarketframeworkprovidesamorecoherent
explanationfortheseseeminglycontradictoryobservations,accountingforimplementation
constraints, varying degrees of market efficiency across assets and time scales, and the
dynamicevolutionofmarketparticipants’informationprocessingcapabilities.
Second,ourcriticalreviewofexistingstudiesestablishesthatdataintegrationsignifi-
cantlyenhancespredictivepower,withhybridapproachesincorporatingalternativedata
sourcesconsistentlyoutperformingsingle-methodapproaches.However,thisbenefitcomes
withtrade-offsininterpretability,computationalcomplexity,andpracticalimplementation
challengesthatmanystudiesfailtoaddressadequately.
12.2. MethodologicalContributionsandPracticalImplications
Basedonourcomprehensiveassessmentofexistingresearch,wehaveidentifiedthat
properevaluationofstockpredictionmodelsrequiresmovingbeyondsimpleclassification
metricstoconsiderfinancialperformanceunderrealisticconstraints. Thesubstantialgap
between statistical significance and economic relevance—with many models showing
impressiveaccuracybutfailingtogeneratevalueafteraccountingfortransactioncostsand
marketimpact—highlightsacriticallimitationincurrentevaluationmethodologies.
Ourproposedcomprehensiveevaluationframeworkaddressesthisgapbyintegrating
statisticalvalidation,economicsignificancetesting,robustnessassessmentacrossdifferent
marketregimes,andimplementationfeasibilityanalysis. Thismulti-dimensionalapproach
providesamorerealisticassessmentofmodelvalue,revealingthatperformancevariessub-
stantiallyacrossdifferenttimehorizons,marketcapitalizations,andeconomicconditions,
insightsthatareoftenobscuredinsingle-dimensionevaluations.
12.3. UnansweredQuestionsandFutureDirections
Despitesignificantadvances,severalcriticalquestionsremainunanswered. Thefield
has not adequately resolved the trade-off between model complexity and robustness,
with more complex models often demonstrating superior in-sample performance but
questionablegeneralizationacrossdifferentmarketregimes. Similarly,thebalancebetween
short-termpredictability(wheretechnicalfactorsdominate)andlong-termforecastability
(wherefundamentalsprevail)representsanongoingchallengethatfutureresearchmust
addressmoresystematically.

Electronics2025,14,1721 44of48
Lookingforward,promisingresearchdirectionsemergefromtheseunresolvedten-
sions: (1)thedevelopmentofexplainableAIapproachesthatmaintainpredictivepower
while offering interpretability; (2) the application of transfer learning techniques to ad-
dress market regime changes; (3) the integration of causal inference methods to move
beyondcorrelationtoidentifystablemarketmechanisms;(4)theextensionofreinforcement
learningbeyondpredictiontoportfoliooptimization;and(5)privacy-preservinglearning
techniquesthatcouldunlockcollaborativemodelingwhilerespectingproprietarydata.
The continued evolution of AI applications in financial markets carries profound
implicationsnotonlyforinvestmentpracticebutalsoforourtheoreticalunderstandingof
marketefficiency,pricediscovery,andsystemicrisk. Asthesetechnologiesbecomemore
sophisticatedandwidelydeployed,theirrecursiveimpactonmarketdynamics—where
predictionsinfluencetheveryphenomenabeingpredicted—willrequireincreasingatten-
tionfromresearchers,practitioners,andregulatorsalike. Theultimatechallengeremainsin
developingmodelsthatcanadapttomarketsthatarethemselvesadaptingtothemodels,a
complexco-evolutionarysystemthatdefiessimplecharacterizationbutmaybeincreasingly
understoodthroughtheadvancedmethodologiesexaminedinthisreview.
Funding:Thisresearchreceivednoexternalfunding.
DataAvailabilityStatement:Dataiscontainedwithinthearticle.
Acknowledgments:TheauthoracknowledgessupercomputingresourcesandsupportfromICSC—
CentroNazionalediRicercainHighPerformanceComputing,BigDataandQuantumComputing—
andhostingentity,fundedbyEuropeanUnion—NextGenerationEU.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.
References
1. Andersen,T.G.;Bollerslev,T.;Diebold,F.X.;Labys,P.ModelingandForecastingRealizedVolatility.Econometrica2003,71,579–625.
[CrossRef]
2. Cont,R.VolatilityClusteringinFinancialMarkets:EmpiricalFactsandAgent-BasedModels.Quant.Financ.2014,14,1547–1561.
3. Hornik,K.MultilayerFeedforwardNetworksareUniversalApproximators.NeuralNetw.1989,2,359–366.[CrossRef]
4. White,H.ArtificialNeuralNetworks:ApproximationandLearningTheory;Blackwell:Hoboken,NJ,USA,1992.
5. Pascanu,R.;Mikolov,T.;Bengio,Y.Onthedifficultyoftrainingrecurrentneuralnetworks.InProceedingsofthe30thInternational
ConferenceonMachineLearning,Atlanta,GA,USA,17–19June2013;pp.1310–1318.
6. Fischer,T.;Krauss,C.Deeplearningwithlongshort-termmemorynetworksforfinancialmarketpredictions.Eur.J.Oper.Res.
2018,270,654–669.[CrossRef]
7. Gal,Y.;Ghahramani,Z.ATheoreticallyGroundedApplicationofDropoutinRNNs.InProceedingsoftheAdvancesinNeural
InformationProcessingSystems29:AnnualConferenceonNeuralInformationProcessingSystems2016,Barcelona,Spain,5–10
December2016.
8. Bengio, Y.; Louradour, J.; Collobert, R.; Weston, J. Curriculum Learning. In Proceedings of the 26th Annual International
ConferenceonMachineLearning,Montreal,QC,Canada,14–18June2009;pp.41–48.
9. Bergstra,J.S.;Bardenet,R.;Bengio,Y.;Kégl,B.AlgorithmsforHyper-ParameterOptimization.InProceedingsoftheAdvancesin
NeuralInformationProcessingSystems24:25thAnnualConferenceonNeuralInformationProcessingSystems2011,Granada,
Spain,12–14December2011.
10. Vaswani,A.;Shazeer,N.;Parmar,N.;Uszkoreit,J.;Jones,L.;Gomez,A.N.;Kaiser,L.;Polosukhin,I.AttentionIsAllYouNeedin
FinancialTimeSeries.J.Comput.Financ.2023,26,45–67.
11. Sezer,O.B.;Gudelek,M.U.;Ozbayoglu,A.M.Financialtimeseriesforecastingwithdeeplearning:Asystematicliteraturereview:
2005–2019.Appl.SoftComput.2020,90,106181.[CrossRef]
12. Henrique,B.M.;Sobreiro,V.A.;Kimura,H.Literaturereview:Machinelearningtechniquesappliedtofinancialmarketprediction.
ExpertSyst.Appl.2019,124,226–251.[CrossRef]
13. Fernández-Rodríguez,F.;Sosvilla-Rivero,S.;Andrada-Félix,J.TechnicalanalysisintheMadridstockexchange.FEDEAWorking
Paper1999,No.99-05.[CrossRef]
14. LópezdePrado,M.Adatasciencesolutiontothemultiple-testingcrisisinfinancialresearch.J.Financ.DataSci.2019,1,99–110.
[CrossRef]

Electronics2025,14,1721 45of48
15. Ariyo,A.A.;Adewumi,A.O.;Ayo,C.K.ComparisonofARIMAandartificialneuralnetworksmodelsforstockpriceprediction.J.
Appl.Math.2014,2014,614342.
16. Devi,B.U.;Sundar,D.;Alli,P.AneffectivetimeseriesanalysisforstocktrendpredictionusingARIMAmodelforNiftyMidcap-50.
Int.J.DataMin.Knowl.Manag.Process2013,3,65–78.
17. DeFaria,E.L.;Albuquerque,M.P.;Gonzalez,J.L.;Cavalcante,J.PredictingtheBrazilianstockmarketthroughneuralnetworks
andadaptiveexponentialsmoothingmethods.ExpertSyst.Appl.2009,36,12506–12509.[CrossRef]
18. Bhuriya,D.;Kausha,G.;Sharma,A.;Singh,U.Stockmarketpredictionusingalinearregression. InProceedingsofthe2017
InternationalconferenceofElectronics,CommunicationandAerospaceTechnology(ICECA),Coimbatore,India,20–22April
2017;pp.510–513.
19. Dutta,A.;Bandopadhyay,G.;Sengupta,S.PredictionofstockperformanceinIndianstockmarketusinglogisticregression.Int.J.
Bus.Inf.2012,7,105–136.
20. Kim,S.;Lee,H.S.;Ko,H.;Jeong,S.H.;Byun,H.W.;Oh,K.J.Patternmatchingtradingsystembasedonthedynamictimewarping
algorithm.Sustainability2018,10,4641.[CrossRef]
21. Chen, Y.; Hao, Y. A feature weighted support vector machine and K-nearest neighbor algorithm for stock market indices
prediction.ExpertSyst.Appl.2017,80,340–355.[CrossRef]
22. Bollen,J.;Mao,H.;Zeng,X.Twittermoodpredictsthestockmarket.J.Comput.Sci.2011,2,1–8.[CrossRef]
23. Ding,X.;Zhang,Y.;Liu,T.;Duan,J.Deeplearningforevent-drivenstockprediction.InProceedingsofthe24thInternational
ConferenceonArtificialIntelligence(IJCAI),BuenosAires,Argentina,25–31July2015;pp.2327–2333.
24. Zhang,D.;Dai,X.;Wang,Q.;Lau,C.K.M.ImpactsofweatherconditionsontheUScommoditymarketssystemicinterdependence
acrossmulti-timescales.EnergyEcon.2023,123,106732.[CrossRef]
25. Hu,H.;Tang,L.;Zhang,S.;Wang,H.PredictingthedirectionofstockmarketsusingoptimizedneuralnetworkswithGoogle
Trends.Neurocomputing2018,285,188–195.[CrossRef]
26. Chen,T.L.;Chen,F.Y.Anintelligentpatternrecognitionmodelforsupportinginvestmentdecisionsinstockmarket.Inf.Sci.2016,
346,261–274.[CrossRef]
27. Bao,W.;Yue,J.;Rao,Y.Adeeplearningframeworkforfinancialtimeseriesusingstackedautoencodersandlong-shortterm
memory.PLoSONE2017,12,e0180944.[CrossRef]
28. Mittal, A.; Goel, A.StockPredictionUsingTwitterSentimentAnalysis; CS229; StanfordUniversity: Stanford, CA,USA,2012;
Volume15.
29. Ma,L.; Wang,X.; Wang,X.; Wang,L.; Shi,Y.; Huang,M.TCDA:TruthfulCombinatorialDoubleAuctionsforMobileEdge
ComputinginIndustrialInternetofThings.IEEETrans.Mob.Comput.2022,21,4125–4138.[CrossRef]
30. Fu,T.C.;Chung,F.L.;Luk,R.;Ng,C.M.Preventingmeaninglessstocktimeseriespatterndiscoverybychangingperceptually
importantpointdetection.InFuzzySystemsandKnowledgeDiscovery:SecondInternationalConference,FSKD2005,Changsha,China,
27–29August2005,Proceedings,PartI2;Springer:Berlin/Heidelberg,Germany,2005;pp.1171–1174.
31. Markowska-Kaczmar, U.; Dziedzic, M. Discovery of technical analysis patterns. In Proceedings of the 2008 International
MulticonferenceonComputerScienceandInformationTechnology,Wisla,Poland,20–22October2008;pp.137–142.
32. Leigh,W.;Frohlich,C.J.;Hornik,S.;Purvis,R.L.;Roberts,T.L.Tradingwithastockchartheuristic.IEEETrans.Syst.ManCybern.
PartSyst.Humans2008,38,93–104.[CrossRef]
33. Cervelló-Royo,R.;Guijarro,F.;Michniuk,K.Stockmarkettradingrulebasedonpatternrecognitionandtechnicalanalysis:
ForecastingtheDJIAindexwithintradaydata.ExpertSyst.Appl.2015,42,5963–5975.[CrossRef]
34. Arévalo,R.;García,J.;Guijarro,F.;Peris,A.Adynamictradingrulebasedonfilteredflagpatternrecognitionforstockmarket
priceforecasting.ExpertSyst.Appl.2017,81,177–192.[CrossRef]
35. Huang,W.;Nakamori,Y.;Wang,S.Y.Forecastingstockmarketmovementdirectionwithsupportvectormachine.Comput.Oper.
Res.2005,32,2513–2522.[CrossRef]
36. Shen,S.;Jiang,H.;Zhang,T.StockMarketForecastingUsingMachineLearningAlgorithms.Master’sThesis,Departmentof
ElectricalEngineering,StanfordUniversity,Stanford,CA,USA,2012.
37. Lohrmann,C.;Luukka,P.ClassificationofintradayS&P500returnswitharandomforest.Int.J.Forecast.2019,35,390–407.
38. Dey,S.;Kumar,Y.;Saha,S.;Basak,S.Forecastingtoclassification:PredictingthedirectionofstockmarketpriceusingXtreme
GradientBoosting.WorkingPaper,2016.
39. Ampomah, E.K.; Qin, Z.; Nyame, G.Evaluationoftree-basedensemblemachinelearningmodelsinpredictingstockprice
directionofmovement.Information2020,11,332.[CrossRef]
40. Ballings,M.;VandenPoel,D.;Hespeels,N.;Gryp,R.Evaluatingmultipleclassifiersforstockpricedirectionprediction.Expert
Syst.Appl.2015,42,7046–7056.[CrossRef]
41. Basak,S.;Kar,S.;Saha,S.;Khaidem,L.;Dey,S.R.Predictingthedirectionofstockmarketpricesusingtree-basedclassifiers.North
Am.J.Econ.Financ.2018,47,552–567.[CrossRef]

Electronics2025,14,1721 46of48
42. Khan,A.H.;Shah,A.;Ali,A.;Shahid,R.;Zahid,Z.U.;Sharif,M.U.;Jan,T.;Zafar,M.H.Aperformancecomparisonofmachine
learningmodelsforstockmarketpredictionwithnovelinvestmentstrategy.PLOSONE2023,18,e0286362.[CrossRef]
43. Pagliaro,A.ForecastingSignificantStockMarketPriceChangesUsingMachineLearning:ExtraTreesClassifierLeads.Electronics
2023,12,4551.[CrossRef]
44. Qiu,M.;Song,Y.Predictingthedirectionofstockmarketindexmovementusinganoptimizedartificialneuralnetworkmodel.
PLoSONE2016,11,e0155133.[CrossRef][PubMed]
45. Moghaddam,A.H.;Moghaddam,M.H.;Esfandyari,M.Stockmarketindexpredictionusingartificialneuralnetwork.J.Econ.
Financ.Adm.Sci.2016,21,89–93.[CrossRef]
46. DiPersio,L.;Honchar,O.RecurrentneuralnetworksapproachtothefinancialforecastofGoogleassets.Int.J.Math.Comput.
Simul.2017,11,7–13.
47. Sezer,O.B.;Ozbayoglu,A.M.Algorithmicfinancialtradingwithdeepconvolutionalneuralnetworks: Timeseriestoimage
conversionapproach.Appl.SoftComput.2018,70,525–538.[CrossRef]
48. Wu,H.;Chen,S.;Ding,Y.ComparisonofARIMAandLSTMforstockpriceprediction.Financ.Eng.RiskManag.2023,6,01026.
49. Powell,N.;Foo,S.Y.;Weatherspoon,M.Supervisedandunsupervisedmethodsforstocktrendforecasting.InProceedingsofthe
200840thSoutheasternSymposiumonSystemTheory(SSST),NewOrleans,LA,USA,16-18March2008;pp.203–205.
50. Wu,K.P.;Wu,Y.P.;Lee,H.M.StocktrendpredictionbyusingK-meansandAprioriAllalgorithmforsequentialchartpattern
mining.J.Inf.Sci.Eng.2014,30,669–686.
51. Babu,M.S.;Geethanjali,N.;Satyanarayana,B.Clusteringapproachtostockmarketprediction. Int. J.Adv. Netw. Appl. 2012,
3,1281.
52. Patel,J.; Shah,S.; Thakkar,P.; Kotecha,K.Predictingstockandstockpriceindexmovementusingtrenddeterministicdata
preparationandmachinelearningtechniques.ExpertSyst.Appl.2015,42,259–268.[CrossRef]
53. Chong,E.;Han,C.;Park,F.C.Deeplearningnetworksforstockmarketanalysisandprediction:Methodology,datarepresentations,
andcasestudies.ExpertSyst.Appl.2017,83,187–205.[CrossRef]
54. Schumaker,R.P.;Chen,H.Textualanalysisofstockmarketpredictionusingbreakingfinancialnews:TheAZFintextsystem.
ACMTrans.Inf.Syst.(Tois)2009,27,12.[CrossRef]
55. Kalyanaraman,V.;Kazi,S.;Tondulkar,R.;Oswal,S.Sentimentanalysisonnewsarticlesforstocks.InProceedingsofthe20148th
AsiaModellingSymposium,Taipei,Taiwan,23–25September2014;pp.57–62.
56. Lee,H.;Surdeanu,M.;MacCartney,B.;Jurafsky,D.Ontheimportanceoftextanalysisforstockpriceprediction.InProceedings
of the 9th International Conference on Language Resources and Evaluation (LREC), Reykjavik, Iceland, 26–31 May 2014;
pp.1170–1175.
57. Pagolu,V.S.;Reddy,K.N.;Panda,G.;Majhi,B.SentimentanalysisofTwitterdataforpredictingstockmarketmovements. In
Proceedingsofthe2016InternationalConferenceonSignalProcessing,Communication,PowerandEmbeddedSystem(SCOPES),
Paralakhemundi,India,3–5October2016;pp.1345–1350.
58. Preis,T.;Moat,H.S.;Stanley,H.E.QuantifyingtradingbehaviorinfinancialmarketsusingGoogleTrends.Sci.Rep.2013,3,1684.
[CrossRef]
59. Ren,R.;Wu,D.D.;Liu,T.Forecastingstockmarketmovementdirectionusingsentimentanalysisandsupportvectormachine.
IEEESyst.J.2018,13,760–770.[CrossRef]
60. Wang,J.J.;Wang,J.Z.;Zhang,Z.G.;Guo,S.P.Stockindexforecastingbasedonahybridmodel.Omega2012,40,758–766.[CrossRef]
61. Rather,A.M.;Agarwal,A.;Sastry,V.N.Recurrentneuralnetworkandahybridmodelforpredictionofstockreturns.ExpertSyst.
Appl.2015,42,3234–3241.[CrossRef]
62. Lv,D.;Yuan,S.;Li,M.;Xiang,Y.Anempiricalstudyofmachinelearningalgorithmsforstockdailytradingstrategy.Math.Probl.
Eng.2019.[CrossRef]
63. Yoshihara,A.;Fujikawa,K.;Seki,K.;Uehara,K.Predictingstockmarkettrendsbyrecurrentdeepneuralnetworks.InProceedings
ofthePacificRimInternationalConferenceonArtificialIntelligence,GoldCoast,Australia,1–5December2014;pp.759–769.
64. Wang,T.;Guo,J.;Shan,Y.;Zhu,Y.Aknowledgegraph–GCN–communitydetectionintegratedmodelforlarge-scalestockprice
prediction.Appl.SoftComput.2023,145,110595.[CrossRef]
65. Zhang,F.Conceptual-temporalgraphconvolutionalneuralnetworkmodelforstockpricemovementpredictionandapplication.
SoftComput.2023,27,6329–6344.
66. Jang,J.;Seong,N.Deepreinforcementlearningforstockportfoliooptimizationbyconnectingwithmodernportfoliotheory.
ExpertSyst.Appl.2023,218,119556.[CrossRef]
67. Wu,J.L.;Tang,X.R.;Hsu,C.H.Apredictionmodelofstockmarkettradingactionsusinggenerativeadversarialnetworkand
piecewiselinearrepresentationapproaches.SoftComput.2023,27,8209–8222.[CrossRef]
68. Harvey,C.R.Presidentialaddress:Thescientificoutlookinfinancialeconomics.J.Financ.2017,72,1399–1440.[CrossRef]
69. Lo,A.W.;MacKinlay,A.C.Whenarecontrarianprofitsduetostockmarketoverreaction? Rev. Financ. Stud. 1990,3,175–205.
[CrossRef]

Electronics2025,14,1721 47of48
70. Baker,M.;Wurgler,J.Investorsentimentandthecross-sectionofstockreturns.J.Financ.2006,61,1645–1680.[CrossRef]
71. Gu,S.;Kelly,B.;Xiu,D.Empiricalassetpricingviamachinelearning.Rev.Financ.Stud.2020,33,2223–2273.[CrossRef]
72. Feng,F.;Chen,H.;He,X.;Ding,J.;Sun,M.;Chua,T.S.Enhancingstockmovementpredictionwithadversarialtraining. In
Proceedingsofthe28thInternationalJointConferenceonArtificialIntelligence,Macao,China,10–16August2019;pp.5843–5849.
73. Diebold,F.X.;Mariano,R.S.Comparingpredictiveaccuracy.J.Bus.Econ.Stat.1995,13,253–263.[CrossRef]
74. Hansen,P.R.;Lunde,A.;Nason,J.M.Themodelconfidenceset.Econometrica2011,79,453–497.[CrossRef]
75. White,H.Arealitycheckfordatasnooping.Econometrica2000,68,1097–1126.[CrossRef]
76. Hansen,P.R.Atestforsuperiorpredictiveability.J.Bus.Econ.Stat.2005,23,365–380.[CrossRef]
77. Giacomini,R.;White,H.Testsofconditionalpredictiveability.Econometrica2006,74,1545–1578.[CrossRef]
78. Politis,D.N.;Romano,J.P.Multivariatedensityestimationwithgeneralflat-topkernelsofinfiniteorder.J.Multivar.Anal.1999,
68,1–25.[CrossRef]
79. Campbell,J.Y.;Thompson,S.B.Predictingexcessstockreturnsoutofsample: Cananythingbeatthehistoricalaverage? Rev.
Financ.Stud.2008,21,1509–1531.[CrossRef]
80. Benjamini,Y.;Hochberg,Y.Controllingthefalsediscoveryrate:Apracticalandpowerfulapproachtomultipletesting.J.R.Stat.
Soc.Ser.(Methodological)1995,57,289–300.[CrossRef]
81. Holm,S.Asimplesequentiallyrejectivemultipletestprocedure.Scand.J.Stat.1979,6,65–70.
82. Romano,J.P.;Shaikh,A.M.;Wolf,M.Controlofthefalsediscoveryrateunderdependenceusingthebootstrapandsubsampling.
Test2007,17,417.[CrossRef]
83. Harvey,C.R.;Liu,Y.;Zhu,H....andthecross-sectionofexpectedreturns.Rev.Financ.Stud.2016,29,5–68.
84. Andrews,D.W.Testsforparameterinstabilityandstructuralchangewithunknownchangepoint.Econometrica1993,61,821–856.
[CrossRef]
85. Bai,J.;Perron,P.Estimatingandtestinglinearmodelswithmultiplestructuralchanges.Econometrica1998,66,47–78.[CrossRef]
86. Primiceri,G.E.Timevaryingstructuralvectorautoregressionsandmonetarypolicy.Rev.Econ.Stud.2005,72,821–852.[CrossRef]
87. Hamilton,J.D.Anewapproachtotheeconomicanalysisofnonstationarytimeseriesandthebusinesscycle.Econometrica1989,
57,357–384.[CrossRef]
88. Pesaran, M.H.; Timmermann, A. Selection of estimation window in the presence of breaks. J. Econom. 2007, 137, 134–161.
[CrossRef]
89. Brock,W.;Lakonishok,J.;LeBaron,B.Simpletechnicaltradingrulesandthestochasticpropertiesofstockreturns.J.Financ.1992,
47,1731–1764.[CrossRef]
90. Sullivan,R.;Timmermann,A.;White,H.Data-snooping,technicaltradingruleperformance,andthebootstrap.J.Financ.1999,
54,1647–1691.[CrossRef]
91. Lo, A.W.; Mamaysky, H.; Wang, J. Foundations of technical analysis: Computational algorithms, statistical inference, and
empiricalimplementation.J.Financ.2000,55,1705–1765.[CrossRef]
92. Rapach,D.E.;Strauss,J.K.;Zhou,G.Out-of-sampleequitypremiumprediction: Combinationforecastsandlinkstothereal
economy.Rev.Financ.Stud.2010,23,821–862.[CrossRef]
93. Bradshaw,M.T.;Drake,M.S.;Myers,J.N.;Myers,L.A.Are-examinationofanalysts’superiorityovertime-seriesforecastsof
annualearnings.Rev.Account.Stud.2012,17,944–968.[CrossRef]
94. Christoffersen,P.;Jacobs,K.;Chang,B.Y.Forecastingwithoption-impliedinformation.Handb.Econ.Forecast.2013,2,581–656.
95. Cheng,I.H.;Xiong,W.Thefinancializationofcommoditymarkets.Annu.Rev.Financ.Econ.2013,5,419–441.
96. English,W.B.;VandenHeuvel,S.J.;Zakrajšek,E.Interestrateriskandbankequityvaluations.J.Monet.Econ.2018,98,80–97.
[CrossRef]
97. Pastor,L.;Veronesi,P.Technologicalrevolutionsandstockprices.Am.Econ.Rev.2009,99,1451–1483.[CrossRef]
98. Lo,A.W.Theadaptivemarketshypothesis:Marketefficiencyfromanevolutionaryperspective.J.Portf.Manag.2004,30,15–29.
[CrossRef]
99. Jegadeesh,N.;Titman,S.Returnstobuyingwinnersandsellinglosers:Implicationsforstockmarketefficiency.J.Financ.1993,48,
65–91.[CrossRef]
100. Bhattacharya,D.;Li,W.H.;Sonaer,G.Hasmomentumlostitsmomentum? Rev. Quant. Financ. Account. 2020,55,1145–1179.
[CrossRef]
101. Bernard,V.L.;Thomas,J.K.Post-earnings-announcementdrift:Delayedpriceresponseorriskpremium?J.Account.Res.1989,27,
1–36.[CrossRef]
102. Ke,B.;Ramalingegowda,S.Doinstitutionalinvestorsexploitthepost-earningsannouncementdrift?J.Account.Econ.2005,39,
25–53.[CrossRef]
103. Zhang,C.Y.;Jacobsen,B.TheHalloweenindicator,“SellinMayandgoaway”:Everywhereandallthetime.J.Int.MoneyFinanc.
2021,110,102268.[CrossRef]
104. Hou,K.;Xue,C.;Zhang,L.Replicatinganomalies.Rev.Financ.Stud.2020,33,2019–2133.[CrossRef]

Electronics2025,14,1721 48of48
105. Chen,A.Y.;Zimmermann,T.Publicationbiasandthecross-sectionofstockreturns.Rev.AssetPricingStud.2022,12,454–488.
106. Lakonishok,J.;Smidt,S.Areseasonalanomaliesreal?Aninety-yearperspective.Rev.Financ.Stud.1988,1,403–425.[CrossRef]
107. Schwert,G.W.Anomaliesandmarketefficiency.Handb.Econ.Financ.2003,1,939–974.
108. White,H.Economicpredictionusingneuralnetworks: ThecaseofIBMdailystockreturns. InProceedingsoftheIEEE1988
InternationalConferenceonNeuralNetworks,SanDiego,CA,USA,24-27July1988;pp.451–458.
109. Bishop,C.M.NeuralNetworksforPatternRecognition;OxfordUniversityPress:Oxford,UK,1995.
110. Tetlock,P.C.Givingcontenttoinvestorsentiment:Theroleofmediainthestockmarket.J.Financ.2007,62,1139–1168.[CrossRef]
111. Loughran,T.;McDonald,B.Whenisaliabilitynotaliability?Textualanalysis,dictionaries,and10-Ks.J.Financ.2011,66,35–65.
[CrossRef]
112. LópezdePrado,M.AdvancesinFinancialMachineLearning;JohnWiley&Sons:Hoboken,NJ,USA,2018.
113. Bailey,D.H.;Borwein,J.M.;LópezdePrado,M.;Zhu,Q.J.Pseudo-mathematicsandfinancialcharlatanism:Theeffectsofbacktest
overfittingonout-of-sampleperformance.Not.Am.Math.Soc.2014,61,458–471.[CrossRef]
114. Boehmer,E.;Jones,C.M.;Zhang,X.Potentialpilotproblems:Treatmentspilloversinfinancialregulatoryexperiments.J.Financ.
Econ.2019,134,355–373.
115. Zhang,Z.;Zohren,S.;Roberts,S.DeepLOB:Deepconvolutionalneuralnetworksforlimitorderbooks.IEEETrans.SignalProcess.
2019,67,3001–3012.[CrossRef]
116. Urquhart,A.TheinefficiencyofBitcoin.Econ.Lett.2016,148,80–82.[CrossRef]
117. Cao,J.;Chen,J.;Hull,J.C.Aneuralnetworkapproachtounderstandingimpliedvolatilitymovements.Quant.Financ.2020,20,
781–797.[CrossRef]
118. Huck, N.Largedatasetsandmachinelearning: Applicationstostatisticalarbitrage. Eur. J.Oper. Res. 2019, 278, 330–342.
[CrossRef]
119. Frazzini,A.;Israel,R.;Moskowitz,T.J.Tradingcosts.J.Financ.Econ.2018,138,293–316.[CrossRef]
120. Bartram,S.M.;Branke,J.;Motahari,M.ArtificialIntelligenceinAssetManagement;CFAInstituteResearchFoundation: Char-
lottesville,VA,2021.
121. Daul,S.;Jaisson,T.;Nagy,A.Performanceattributionofmachinelearningmethodsforstockreturnsprediction.J.Financ.Data
Sci.2022,8,86–104.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.