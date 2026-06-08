Article
Review of Methods and Models for Forecasting
Electricity Consumption
KamilMisiurek* ,TadeuszOlkuski andJanuszZys´k
FacultyofEnergyandFuels,AGHUniversityofKrakow,30-059Kraków,Poland;olkuski@agh.edu.pl(T.O.);
jazysk@agh.edu.pl(J.Z.)
* Correspondence:kmisiurek@agh.edu.pl
Abstract
Thisarticlepresentsacomprehensivereviewofmethodsusedforforecastingelectricity
consumption. The studies analyzed by the authors encompass both classical statistical
modelsandmodernapproachesbasedonartificialintelligence,includingmachine-learning
anddeep-learningtechniques. Electricityloadforecastingiscategorizedintofourtime
horizons:veryshortterm,shortterm,mediumterm,andlongterm. Theauthorsconducted
acomparativeanalysisofvariousmodels,suchasautoregressivemodels,neuralnetworks,
fuzzylogicsystems,hybridmodels,andevolutionaryalgorithms. Particularattentionwas
paidtotheeffectivenessofthesemethodsinthecontextofvariableinputdata,suchas
weatherconditions,seasonalfluctuations,andchangesinenergyconsumptionpatterns.
Thearticleemphasizesthegrowingimportanceofaccurateforecastsinthecontextofthe
energytransition,integrationofrenewableenergysources,andthemanagementofthe
evolvingelectricitysystem,shapedbydecentralization,renewableintegration,anddata-
intensiveforecastingdemands. Inconclusion,theauthorshighlightthelackofauniversal
forecastingapproachandtheneedforfurtherresearchonhybridmodelsthatcombine
interpretabilitywithhighpredictiveaccuracy. Thisreviewcanserveasavaluableresource
fordecision-makers,gridoperators,andresearchersinvolvedinenergysystemplanning.
Keywords: electricityconsumption;forecasting;review;time-stepforecasting
AcademicEditor:ZhongkaiYi
1. Introduction
Received:3July2025
Revised:21July2025
Electricityisafundamentalpillarofmodernsociety,poweringeverythingfromhouse-
Accepted:25July2025
holdappliancestoindustrialmachineryanddigitalinfrastructure. Theefficientproduction,
Published:29July2025
distribution,andconsumptionofelectricityarecrucialforeconomicgrowth,technological
Citation: Misiurek,K.;Olkuski,T.;
innovation,andimprovingqualityoflife. However,theincreasingdemandforelectricity,
Zys´k,J.ReviewofMethodsand
coupledwiththeneedtoreducecarbonemissions,presentssignificantchallenges. Balanc-
ModelsforForecastingElectricity
Consumption.Energies2025,18,4032. ingsupplyanddemand,integratingrenewableenergy,andmodernizingaginggridsare
https://doi.org/10.3390/ keyissuesthatrequireinnovativesolutionsandaccurateforecastingtoensureasustainable
en18154032 andreliableenergyfuture[1]. Advancedmachine-learningalgorithmsanddata-driven
Copyright:©2025bytheauthors. predictivemodelsplayacrucialroleinoptimizingenergyconsumption,enhancinggridef-
LicenseeMDPI,Basel,Switzerland. ficiency,andfacilitatingtheseamlessintegrationofrenewableenergysources[2,3].Figure1
Thisarticleisanopenaccessarticle shows the consumption of primary energy (in TWh) in selected countries from 1998 to
distributedunderthetermsand
2023. ThelargestgrowthwasrecordedinChina,whereconsumptionmorethantripled,
conditionsoftheCreativeCommons
exceeding45,000TWhin2023,wellaheadoftheUnitedStates,whichremainsstableat
Attribution(CCBY)license
around25,000TWh. Poland,likeotherEuropeancountries(e.g.,France,Sweden),hasa
(https://creativecommons.org/
licenses/by/4.0/). muchlowerandrelativelystablelevelofconsumption[4]. Oneofthemostpressingissues
Energies2025,18,4032 https://doi.org/10.3390/en18154032

Energies2025,18,4032 2of27
inenergymanagementistheimbalancebetweenproductionandconsumption. Addition-
ally,therelianceoncoalforelectricitygenerationhasposedenvironmentalandregulatory
challenges,pushingthecountriestowardcleanerbutmorevariableenergysourceslike
windandsolar. Thisvariabilityintroducesnewcomplexitiesinforecasting,asrenewable
energygenerationisinherentlylesspredictablethantraditionalfossilfuel-basedsystems.
Anothercriticalproblemistheaginginfrastructure,whichcanleadtoinefficiencyand
vulnerabilitiesintheenergygrid. Modernizingthegridtoaccommodatedecentralized
energysourcesandsmarttechnologiesisessentialbutrequiressignificantinvestmentand
planning. Furthermore,thegrowingemphasisonsustainabilityandcarbonneutralityadds
anotherlayerofcomplexity,aspolicymakersandenergyprovidersmustbalanceimmediate
energyneedswithlong-termenvironmentalgoals.
Accurateforecastingofelectricityconsumptionisthereforemoreimportantthanever.
Itenablesbetterplanning,reducestheriskofshortages,andsupportstheintegrationof
renewable energy sources. Load forecasting plays a critical role in various operational
decisions, including management, planning, scheduling, and load dispatching. As a
result,achievingpreciseforecastingisessentialforensuringthereliable,secure,andstable
functioningofelectricpowersystems. Inaccurateforecastscanleadtosignificanteconomic
lossesforpowercompanies,drivingupoperatingcosts. Researchindicatesthatevena
1%increaseinforecastingerrorcanresultinanadditionalUSD10millioninoperating
expensesannually[5].
Figure1.Primaryenergyconsumptioninselectedcountries(1998–2023).Ownstudybasedon[6].
In this article, we will explore the methodologies and models used for forecasting
electricity consumption. By examining various approaches from traditional statistical
methodstoadvancedmachine-learningtechniquesweaimtoprovideaclearunderstanding
oftheirstrength, limitations, andapplicabilityindifferentcontext[7]. Thisreviewwill
highlightthechallengesinherentinforecasting,suchasdealingwithvariablerenewable
energyinputs,changingconsumptionpatterns,andtheneedforreal-timedataprocessing.
Byexploringthesemethods,weaimtoofferinsightsintohowrobustforecastingmodels
canbedevelopedtonavigatethecomplexitiesoftheevolvingenergylandscape[8].

Energies2025,18,4032 3of27
2. MethodsandMaterials
Inthispaper,wehaveconductedacomprehensivereviewofexistingstudiesonfore-
castingelectricityconsumption. Ourreviewencompassesresearchandreviewarticlesfrom
2024andearlier,withaparticularfocusonrecentworkspublishedoverthepast5years.
Additionally, we have included classical studies that highlight the key developmental
trendsinthefieldofelectricityconsumptionforecasting.
Followingthisapproach,weperformedacomparativeanalysisofstudiesthatexplore
variousmethodsusedforforecastingelectricityconsumption,evaluatingthembasedon
severalcriteria. ThefindingsofthisanalysisarethoroughlydetailedinSection3,which
isdividedintofoursubsections. Eachsubsectionprovidesacomparativeevaluationof
methodscorrespondingtodifferentforecastinghorizons. Section4summarizesthemain
outcomes of our review and identifies potential directions for future research. Various
statisticalmetricswereemployedinthearticle. However,itshouldbeemphasizedthatthis
reviewaimstosynthesizeandanalyzefindingspresentedinthescientificliterature. The
reportedvaluesofthesestatisticalindicatorsarederivedfromthecitedstudiesanddonot
resultfromtheauthors’ownexperiments.
Electricity load forecasting is divided into four categories based on the time do-
main: (i)long-termloadforecasting(LTLF),(ii)medium-termloadforecasting(MTLF),
(iii)short-termloadforecasting(STLF),and(iv)veryshort-termloadforecasting(VSTLF),
asillustratedinFigure2withtheirrespectivetimedistributions[9]. Variousforecasting
methodshavebeenappliedtothesetimedomains,includingknowledge-basedexpertsys-
tems,statisticaltechniques,artificialintelligence(AI)approachessuchasmachine-learning
models,hybridtechniques,anddeep-learningmodels[10–12].
Figure2. Categoriesofelectricalloadforecastingbasedonvarioustimehorizonsandtheircorre-
spondingoperationaldomains[9,13].
TraditionalStatisticalMethodsinElectricityForecasting
Whilemachine-learninganddeep-learningapproacheshavegainedsignificanttrac-
tion in electricity load forecasting, conventional statistical methods continue to play a
vitalroleinboththeoreticalstudiesandreal-worldimplementations. Theseestablished
techniquesproveespeciallyusefulwhendealingwithdata-scarceenvironments,restricted
processing capabilities, or situations requiring transparent and explainable forecasting
models. Amongclassicalapproaches,ARIMA/SARIMA(AutoRegressiveIntegratedMov-
ingAverage/SeasonalARIMA)modelsremainparticularlyvaluable,asdemonstratedby

Energies2025,18,4032 4of27
theauthors’analysisisthisstudy[13]. Theyareclassicalstatisticalmodelswidelyused
intime-seriesforecasting. TheARIMAmodelwasformallyintroducedintheearly1970s
by Box and Jenkins as part of their influential methodology for time-series forecasting.
ARIMAisdesignedfornon-stationarydataandincorporatesdifferencingtoremovetrends,
allowingformoreaccuratemodelingoftheunderlyingstructure.SARIMAextendsARIMA
byalsoaddressingseasonalpatternsthroughseasonaldifferencing. Thesemodelsarepar-
ticularlyeffectivewhenthetimeseriesexhibitsautocorrelationandconsistentseasonal
cycles. Despitetheriseofmachine-learningmethods,ARIMAandSARIMAremainpop-
ular due to their interpretability, simplicity, and solid performance in many real-world
applications[14].
Exponentialsmoothingisatime-seriesforecastingmethodthatappliesdecreasing
weights topast observations, placingmoreemphasis on recent data. The Holt-Winters
method is an extension of this technique that accounts for both trend and seasonality,
makingitsuitableforserieswithsystematicpatterns. Holt-Wintersiswidelyusedinoper-
ationalsettingsduetoitssimplicity,lowcomputationalcost,andreasonableperformance
withlimiteddata. Althoughitmaynotcapturecomplexnonlinearities,itremainsarobust
baselinemodelinmanypracticalapplications[15].
Linearregressionisafoundationalstatisticaltechniqueusedtomodeltherelationship
betweenadependentvariableandoneormoreexplanatoryvariables. Inthecontextof
electricityconsumptionforecasting,itcancapturelineartrendsovertimeandincorporate
externalfactorssuchastemperature,economicindicators,orcalendareffects. Themodelis
valuedforitsinterpretabilityandeaseofimplementation,especiallyinsettingswithsmall
datasetsorwheremodeltransparencyisrequired. However,itspredictiveaccuracymay
belimitedinhighlynonlinearorcomplexsystems. Linearregressionisoftenusedasa
benchmarkmodeloracomponentofhybridforecastingframeworks[16].
Insummary,traditionalstatisticalmethodssuchasARIMA,Holt-Wintersexponential
smoothing, and linear regression continue to serve as essential tools in electricity load
forecasting. Overthepast2decades,however,thefieldhaswitnessedarapidevolution
with the emergence of machine-learning and deep-learning techniques. These modern
approachesoffergreaterflexibilityinhandlingcomplex,high-dimensional,andnonlinear
data structures, paving the way for more accurate and adaptive forecasting systems in
dynamicenergyenvironments.
3. TypesofLoadForecasting—ComparativeAnalysisofMethods
Forecastingelectricityconsumptionisacrucialtoolforinformedmanagementdeci-
sionsandeffectiveplanningofelectricityexpenditures. Ananalysisofscientificresearch
highlights two key points: first, there is no universal method for predicting electricity
consumption,andsecond,theincreasingdemandforhigherforecastingaccuracydrives
the development of new approaches. As a result, we have conducted a review of the
methodologicalfoundationsofelectricityconsumption. Whilesimilarreviewshavebeen
out in previous studies [6–8], this work stands out by providing review of the newest
articleswithanevaluationoftheirpotentialadvantagesandrisks. Next,wewillexamine
thespecificobjectivesassociatedwitheachtypeofforecasting.
Veryshort-termandshort-termobjectivesplayacrucialroleineffectivelymanaging
electricity demand and assessing opportunities for energy storage. Accurate forecasts
for a day or several days ahead help mitigate peak loads. Research indicates that very
short-andshort-termforecastingisparticularlyrelevantforplanningelectricitydemandin
regionalenergysystems,aswellasinmicrogrids,whichincludeindividuallargeconsumers
such as buildings (offices, schools, hotels, etc.), infrastructure facilities, and industrial
enterprises[17].

Energies2025,18,4032 5of27
Medium-termforecastingisessentialforplanningelectricityproductionandmain-
tainingthepowergrid. Monthlyforecasting,inparticular,iscriticalfortheoperationof
thermalpowerplants,whichplayacentralroleincoaldispatchandelectricitytrade[18].
Long-termforecastingisusedforstrategicplanningofenergysystemdevelopment
atthenationallevel,withinspecificsectors,andforplanningcapitalinvestmentorma-
jorinfrastructureandproductionfacilitymaintenance. Togeneratelong-termforecasts,
multipledevelopmentscenariosaretypicallyconsidered,suchasGDPgrowthorproduc-
tionrate. Moreover,preciselong-termforecastsarefundamentalfordesigningeffective
environmentalstrategies,suchasindustrialdecarbonization[13,19].
Thechoiceofforecastingmethodsdependsonthetimehorizon. Currently,themost
commonlyusedmethodsincludeclassicalanddeepmachine-learningalgorithms,genetic
algorithms, wavelet analysis, and singular spectral analysis. However, the selection of
methods varies depending on the specific problem being addressed and the structure
of the available data. Interestingly, numerous studies have shown that traditional fore-
castingmethodscanachieveaccuracylevelscomparabletothoseofmoreadvancedand
computationallydemandingintelligenttechniques[20,21].
In the subsequent sections, we will examine the most widely adopted and recom-
mendedforecastingapproachesdiscussedintheliterature,organizedbasedontheirre-
spectiveforecastingtimehorizons[17].
3.1. VeryShort-TermLoadForecasting
Veryshort-termelectricityloadforecastingisacriticalprocessusedtopredictelectric-
itydemandinintervalsasbriefas30min,usuallyperformed1dayahead. Thisforecasting
playsacrucialroleintheeffectivemanagementandoperationofpowersystems,ensur-
ingthatelectricitysupplyalignswithdemandwhilebalancingeconomicefficiencyand
operationalrequirements[22].
Reference[22],discussesthemethodologyforveryshort-termelectricloadforecasting
usingtheIntervalType-1FuzzyInferenceSystem(IT-1FIS).Theforecastingisconducted
1 dayinadvanceat30minintervals,whichiscrucialforoperationalplanning,maintenance,
andcostoptimizationinenergymanagement. Thestudyfocusesontheimpactofdifferent
timedifferencesettingsonforecastaccuracy. Traditionally, forecastingisperformedby
analyzinghistoricaldatafromthesamedayoftheweekinpreviousyears. Theauthors
propose an alternative approach, where instead of analyzing past Fridays, data from
previousweekdays(Thursday,Wednesday,andTuesday)areused. Theresultsindicate
thattheclassicalmethod(usingpastFridays)producedalowerforecasterror(0.4695%)
comparedtothealternativeapproach(0.6123%).
InRef.[23],thefocusisonresidentialloadforecastingusingaLongShort-TermMem-
ory(LSTM)recurrentneuralnetwork(RNN)[24]. Thestudyaddressesthechallengesof
predictingelectricityconsumptionattheindividualhouseholdlevel,wherehighvolatility
andunpredictabilitymakeaccurateforecastingdifficult. Theforecastingmodelemploys
a time step of 30 min, meaning it generates real smart meter readings from residential
households,providingadetailedviewofenergyusagepatterns. TheLSTM-basedmodel
is trained and tested against benchmark forecasting methods, including Backpropaga-
tionNeuralNetworks(BPNN),K-NearestNeighbors(KNN),ExtremeLearningMachines
(ELM),andempiricalmethodssuchasmeanandameanabsolutepercentageerror(MAPE)
minimizationpredictors. TheresultsindicatethattheLSTMmodeloutperformsallother
methods in predicting very short-term residential electricity consumption. The study
evaluates forecasting accuracy using Root Mean Square Error (RMSE) and Root Mean
Square Percentage Error (RMSPE), showing that the LSTM model achieves lower error
ratesthantraditionalapproaches. TheRMSEresultsindicateasignificantimprovementin

Energies2025,18,4032 6of27
forecastingprecision,whilethelowerRMSPEvaluesconfirmthemodel’sabilitytocapture
variationsinconsumptionpatternseffectively. Additionally,thestudyexaminestheeffect
ofaggregatingindividualhouseholdforecasts,findingthatthisapproachresultsinlower
errorscomparedtodirectlyforecastingtotalload. TheLSTMmodelachievesanRMSEim-
provementofapproximately10–15overtraditionalmachine-learningmodelsinaggregated
forecastingscenarios. ThestudyconcludesthatLSTMnetworkseffectivelylearncomplex
temporaldependenciesinresidentialenergyconsumptionandcansignificantlyimprove
forecastingaccuracy. FutureresearchshouldfocusonoptimizingLSTMhyperparameters
andincorporatingexternalfactorssuchasweatherdataandapplianceusagetofurther
enhancepredictions. Thestudyalsosuggeststhathybridforecastingmodels,combining
LSTMwithstatisticaltechniques,mayfurtherimproveloadforecastingreliability.
The article [25] introduces a hybrid approach that combines convolutional neural
networksandlongshort-termmemorynetworkstoforecastresidentialenergyusage. The
CNNcomponentextractsspatialfeaturesandreducesnoisesfrommultivariatetime-series
data,whiletheLSTMcomponentcaptureslong-termtemporaldependenciesandirregular
trends. Themodelemploysaslidingwindowalgorithmtosegmentcontinuousdatainto
fixedintervals,typically60minwindows,allowingittocapturebothlocalandglobalpat-
ternseffectively.Quantitatively,theCNN-LSTMmodelachievesameansquareerror(MSE)
of0.3738,ameanabsoluteerror(MAE)of0.3493,andameanabsolutepercentageerror
(MAPE)of34.84,outperformingtraditionalmethodssuchaslinearregressionandstan-
daloneLSTMmodels. Overall,thestudydemonstratesthatthehybridCNN-LSTMmodel
isarobustandeffectivetoolforforecastingresidentialenergyconsumptionacrossvarious
timeresolutions,offeringvaluableinsightsforenergymanagementandoptimization.
The article [26] presents a model for forecasting electricity consumption in Spain
using a deep LSTM network. The model predicts electricity consumption with a 4 h
forecast horizon based on historical data recorded at 10 min intervals over a period of
9.5years. Theoptimizationofthenetwork’shyperparameterswasconductedusingtwo
methods: random search and a heuristic algorithm inspired by the propagation of the
SARS-CoV-2virus,knownastheCoronavirusOptimizationAlgorithm(CVOA).Thetime
step used in the forecasting model is based on a historical window of 168 past values,
covering a full day and 4 additional hours, to predict the next 24 values, equivalent
to 4 hours ahead. The model’s performance was evaluated using typical error metrics.
TheMAPEindicatestherelativeaccuracyofthemodel,withthebest-performingLSTM
model, optimized using random search, achieving a MAPE of 1.4472%, outperforming
other forecasting techniques such as Temporal Fusion Transformers (TFT), Deep Feed-
Forward Neural Networks (DFFNN), linear regression, decision trees, random forests,
andgradientboosting. Themostsignificantchallengesinaccuracywereobservedduring
springmonthsandinAugust,whiletheworstpredictionsoccurredonholidayperiods
suchasChristmasEve.
Thearticle[27]showsamethodologyforpeakloadforecastinginanopen-pitmine
usingadvancedmachine-learningtechniques.Akeyaspectoftheanalysisistheapplication
oftheFastForestQuantileRegression(FFQR)model,whichenablesprecisepredictionsof
energyconsumptionundervariousoperationalconditions[28]. Theforecastingprocess
beginswithcollectinghistoricaldataonenergyconsumption,machine-operatinghours,
and production indicators. These data are then processed and validated using k-fold
cross-validation,ensuringtheirhighqualityandaccuracy. FFQRwaschosenastheprimary
algorithmduetoitsabilitytomodeldifferentenergyconsumptionscenariosanditsrobust-
nessagainstunforeseenchangesinthedata. Twoexperimentswereconducted,varying
thenumberofdecisiontreesandleavesinthemodeltooptimizeforecastingaccuracy. The
resultsdemonstratedthattheFFQRmodelachieveshigheffectivenessinpredictingenergy

Energies2025,18,4032
7of27
consumption,allowingbettermanagementofthepowergridandminimizingoperational
costs. Peakloadforecastingisacrucialcomponentofsmartenergymanagementinopen-
pitmining,supportingthetransitiontoEnergy4.0strategiesandensuringmoreefficient
utilizationofenergyresources[29].
Thepaper[30]presentsamodelbasedontheTransformerarchitecture,designedfor
1-day forecasting of electricity consumption (short-term) based on data from Baghdad,
Iraq,collectedevery15minsince2015. Themodelusesaself-attentionmechanismthat,
according to the authors and the literature they cited, handles long time dependencies
betterthantraditionalRNNsorLSTMs. Beforeusingthemodel,thedatawerethoroughly
processed(cleaning,gapfilling,scaling,dimensionreduction)toensurehigh-qualityinputs.
Themodelachievedalowpredictionerror—RMSE≈2.0andahighcorrelationcoefficient
(CC)betweenactualandpredictedvalues. Theresultsprovethatthetransformerapproach
iscompetitivewithexistingmethodsandissuitableforpracticaluseinforecastingenergy
demandinrealsystems.
The reference [31] presents a new approach to electrical load forecasting based on
Transformer architecture with sparse attention. The motivation was to overcome the
limitationsoftraditionaldeep-learningmethods,suchasRNNandCNN,intime-series
forecasting, especially parallelization problems and long dependencies. The proposed
modelusessparseattention,includingaBigBirdimplementation,toeffectivelyaddressthe
quadraticmemorycostsassociatedwithlongdatasequencesinTransformers. Themodel
architectureisbasedonanencoderanddecoder,alsohandlingmultidimensionalinput
datasuchasweatherinformationtoimproveaccuracy. Experimentswereconductedon
publicdatasets(fromtheUnitedKingdom,theUnitedStates,andSpain)forshort-term
(1day)andlonger-term(1week)forecasts. Theresultsshowedthatthemodelachieves
comparableaccuracytothebestRNNmethodswhilebeinguptofivetimesfasterinthe
inferenceprocess,confirmingitsscalabilityandefficiency. Table1providesasummary
oftheforecastingmethodsforveryshort-termelectricityconsumption, asdiscussedin
thissection.
Table1.Summaryofveryshort-termloadforecastingconsumptionmethods.
| Forecasting | Authors/ |           | Model/    | Forecast | Accuracy  |            | Disadvantages/ |
| ----------- | -------- | --------- | --------- | -------- | --------- | ---------- | -------------- |
| No.         |          | InputData |           |          |           | Advantages |                |
| Method      | Source   |           | Algorithm | Horizon  | (Metrics) |            | Limitations    |
Interval
|             |             | Historicaldata | Interval    | Very       |          |             |                  |
| ----------- | ----------- | -------------- | ----------- | ---------- | -------- | ----------- | ---------------- |
| Type-1Fuzzy | Jamaaluddin |                |             |            | Forecast | Goodforvery |                  |
|             |             | from           | Type-1Fuzzy | short-term |          |             | Sensitivetoinput |
| 1 Inference | etal.(2020) |                |             |            | error=   | short-term  |                  |
|             |             | short-term     | Inference   | (every     |          |             | dataselection    |
| System      | [22]        |                |             |            | 0.4695%  | forecasts   |                  |
|             |             | forecasts      | System      | 30min)     |          |             |                  |
(IT-1FIS)
Historical
| LSTM      |         |        |           |     |       | Veryeffective |               |
| --------- | ------- | ------ | --------- | --- | ----- | ------------- | ------------- |
|           | Weicong | energy | LSTM(Long |     | RMSE= |               | Requireslarge |
| Recurrent |         |        |           |     |       | fornonlinear  |               |
2 Kongetal. consumption Short-Term upto24h 3.2%,MAPE datasetsand
| Neural  |            |              |         |     |       | patterns,can |                    |
| ------- | ---------- | ------------ | ------- | --- | ----- | ------------ | ------------------ |
|         | (2017)[23] | data,weather | Memory) |     | =5.1% |              | computationalpower |
| Network |            |              |         |     |       | detecttrends |                    |
data
CNNfor
|          | Tae-Young | Time-series |             |            | Lowest     | Combines   |                   |
| -------- | --------- | ----------- | ----------- | ---------- | ---------- | ---------- | ----------------- |
|          |           |             | feature     | Short-term |            |            |                   |
| CNN-LSTM | Kim,      | datafromthe |             |            | RMSE       | spatialand |                   |
|          |           |             | extraction+ | (individ-  |            |            | Highcomputational |
| 3 Neural | Sung-Bae  | UCIMachine  |             |            | comparedto | temporal   |                   |
Network Cho(2019) Learning LSTMfor ualhou- other features, demands
|     |      |            | time-series | seholds) |         |              |     |
| --- | ---- | ---------- | ----------- | -------- | ------- | ------------ | --- |
|     | [25] | Repository |             |          | methods | reducesnoise |     |
modeling
Spanish
|          | J.F.Torres,F. |              | DeepLSTM     |     |             |               |                     |
| -------- | ------------- | ------------ | ------------ | --- | ----------- | ------------- | ------------------- |
|          |               | electricity  |              |     | Best        |               | Highmodel           |
|          | Martínez-     |              | +hyperpa-    |     |             | Bestaccuracy  |                     |
| DeepLSTM |               | consumption  |              |     | performance |               | complexity,requires |
| 4        | Álvarez,A.    |              | rameter      | 4h  |             | forshort-term |                     |
| Network  |               | data(9years, |              |     | (errorbelow |               | hyperparameter      |
|          | Troncoso      |              | optimization |     |             | forecasting   |                     |
|          |               | 10min        |              |     | 1.5%)       |               | tuning              |
|          | (2022)[26]    |              | (CVOA)       |     |             |               |                     |
intervals)

Energies2025,18,4032
8of27
Table1.Cont.
| Forecasting | Authors/ |           | Model/    | Forecast | Accuracy  |            | Disadvantages/ |
| ----------- | -------- | --------- | --------- | -------- | --------- | ---------- | -------------- |
| No.         |          | InputData |           |          |           | Advantages |                |
| Method      | Source   |           | Algorithm | Horizon  | (Metrics) |            | Limitations    |
Oussama
Laayati,
|            |         | Energy       |            | Short-term  | Optimal     | Effectivein  |                  |
| ---------- | ------- | ------------ | ---------- | ----------- | ----------- | ------------ | ---------------- |
| FastForest | Mostafa |              | FastForest |             |             |              | Specialized      |
|            |         | consumption  |            | (load       | accuracyin  | industrial   |                  |
| 5 Quantile | Bouzi,  |              | Quantile   |             |             |              | applicationinthe |
|            |         | datafroman   |            | forecasting | peakload    | mining       |                  |
| Regression | Ahmed   |              | Regression |             |             |              | miningindustry   |
|            |         | open-pitmine |            | inamine)    | forecasting | applications |                  |
Chebak
(2022)[27]
Captures
long-term
|              |             | Historical  | Transformer |       | RMSE≈2%,    |                | Requireslarge   |
| ------------ | ----------- | ----------- | ----------- | ----- | ----------- | -------------- | --------------- |
| Transformer- | Mahmood     |             |             |       |             | dependencies,  |                 |
|              |             | electricity | (self-      | 1day  | high        |                | datasetsandhigh |
| 6 baseddeep  | etal.(2022) |             |             |       |             | handles        |                 |
|              |             | consumption | attention   | ahead | correlation |                | computational   |
| learning     | [30]        |             |             |       |             | non-linearity, |                 |
|              |             | inBaghdad   | mechanism)  |       | coefficient |                | resources       |
competitive
performance
RMSE≈
Fastinference
|             |            | Historical   | Transformer |         | 0.060,MAE | (upto5×−10   |                      |
| ----------- | ---------- | ------------ | ----------- | ------- | --------- | ------------ | -------------------- |
|             |            | power        |             |         |           |              | Limitedbenefitfrom   |
|             |            |              | withsparse  |         | ≈0.051,   | ×fasterthan  |                      |
| Sparse      |            | consumption  |             |         |           |              | weatherdata;         |
|             | Chan&Yeo   |              | attention   | 1day,up | sMAPE≈    | TSRNN),high  |                      |
| 7 Attention |            | (London,AEP, |             |         |           |              | requirestuning;fixed |
|             | (2024)[31] |              | (BigBird),  | to1week | 0.18(AEP, | scalability, |                      |
| Transformer |            | REE);        |             |         |           |              | attentionvariantmay  |
|             |            |              | encoder–    |         | 1day);    | workson      |                      |
|             |            | optionally   |             |         |           |              | limitflexibility     |
|             |            |              | decoder     |         | inference | householdand |                      |
weatherdata
|     |     |     |     |     | time:8.8ms | citylevels |     |
| --- | --- | --- | --- | --- | ---------- | ---------- | --- |
3.2. Short-TermLoadForecasting
This part of the article will focus on short-term load forecasting (STFL), a critical
componentinenergymanagementandpowersystemoperations. STFLaimstopredict
electricityconsumptionovershorttimehorizons,typicallyrangingfromadaytoseveral
weeks [32]. Accurate short-term load forecasting is essential for balancing supply and
demand,optimizingenergydispatch,andreducingoperationalcostsinmodernsmartgrids.
Severalapproacheshaveatime-seriesforecastingmethodthatmodelslineardependencies
inelectricityconsumptiondata. ARIMAiseffectiveforstationarytimeseriesbutstruggles
withcomplex,nonlinearrelationships[7]. SeasonalARIMAorSARIMAisaspecialformof
ARIMAmodelthatisusedmainlytomodelawiderangeofseasonaldata. Thisisattained
byincorporatinganadditionalseasonalparametertohandleaperiodofseasonality. Linear
regressionisoneofthesimplestandmostwidelyusedstatisticalmethodsforforecasting
electricity consumption. It establishes a relationship between electricity consumption
(dependentvariable)andoneormoreindependentvariables,suchastemperature,timeof
day,dayoftheweek,andeconomicfactors.Themodelassumesthatelectricityconsumption
changeslinearlywiththeseinfluencingfactors,allowingforeasyinterpretationofresults.
In its basic form, simple linear regression uses a single predictor (e.g., temperature) to
estimatefutureconsumption,whilemultiplelinearregression(MLR)incorporatesseveral
variables to improve accuracy. Despite its ease of implementation and interpretability,
linearregressionhaslimitations;itstrugglestocapturenonlineardependenciesandsudden
fluctuations in energy demand. As a result, it is often used as a baseline model or in
combinationwithmachine-learningtechniquesformoreaccurateshort-termelectricity
loadforecasting[33,34].
Thestudyaimed[35]toapplyunivariateBox-Jenkinstime-seriesanalysis(ARIMA)
tomodelandforecastmonthlyelectricityconsumptionintheEasternProvinceofSaudi
Arabia. Additionally,thestudycomparedtheeffectivenessofthisapproachwithregression
modelsandmachine-learningtechniques.Theselectedmodel,theARIMAmodel,achieved
anaveragepercentageerrorof3.8%,whichwasbetterthanregressionmodels(8.1%)and
artificial neural networks (5.6%). The ARIMA model had a 70% lower absolute error
and 58% lower mean square error than the moving average (MA) model. All actual

Energies2025,18,4032 9of27
consumption values fell within the 95% confidence interval of the forecasts, indicating
high model accuracy. Seasonality was a key factor in achieving accurate predictions,
as peak electricity consumption occurred in summer due to increased demand for air
conditioning. The ARIMA model outperformed both regression and machine-learning
models in forecasting monthly electricity consumption. It did not require additional
variables (e.g., temperature, population), making it a more universal forecasting tool.
The strong fit to test data suggests that this model can be effectively used for energy
consumptionplanninginregionswithdistinctseasonality. Inconclusion,ARIMAisan
effectivemethodforshort-termforecastingofmonthlyelectricityconsumption,surpassing
regressionandmachine-learningapproachesinpredictionaccuracy. Thismodelcanbe
successfully applied to energy management and planning in areas with clear seasonal
consumptionpatterns.
Thestudy[29]aimedtousetheBox-JenkinsARIMAmodeltoforecastmonthlyhouse-
holdelectricityconsumptionintheEasternProvinceofSaudiArabia. Thestudyutilizes
5yearsofhistoricaldataformodeltrainingandevaluatesitsforecastingaccuracyusing
the 6th year’s data Although the article dates back to the previous century, it may still
providevaluableinsightsintotheconclusionsdrawnbyresearchersatthattime.. Scientists
usedtheARIMAapproach,whichdemonstratessuperiorforecastingperformance. The
optimalmodelisamultiplicativecombinationofseasonalandnon-seasonalautoregressive
components,bothofthefirstorder,withfirstdifferencingappliedatbothseasonaland
non-seasonal levels. The ARIMA model achieves an average percentage error of 3.8%,
outperformingregressionmodels(8.1%)andabductivenetworkmodels(5.6%). Themean
squareforecastingerrorisalsosignificantlylower,reducedbyfactorsof3.2and1.6,re-
spectively. ThestudyhighlightstheadvantagesofARIMAmodels,includinglowerdata
requirements,fewerparameters,andhigheraccuracycomparedtoregression-basedand
machine-learning-basedmodels. Whilemachine-learningtechniquesallowforautomated
modeldiscovery,ARIMAremainsarobustchoiceduetoitsinterpretabilityandreduced
dependencyonexternalvariables. Thefindingssuggestthattime-seriesanalysiscaneffec-
tivelycaptureseasonalandlong-termelectricityconsumptiontrends,makingitavaluable
toolforenergyplanningandmanagement.
Thearticle[36]showsdevelopingareal-timeenergymonitoringsystemandusing
ArtificialNeuralNetworks(ANNs)toforecastpeakelectricalconsumption60minahead
inalargegovernmentbuilding. ThestudycomparedtheANNmodel’sperformancewith
threeotherforecastingmethods,whichareSimpleMovingAverage(SMA),LinearRegres-
sion,andMultivariateAdaptiveRegressionSplines(MARSplines). TheLinearRegression
model was developed using a 90-day dataset and included the following independent
variables: L ofday,typeofday,HVACenergyconsumption,outdoortemperature,and
time
humidity. Theregressionequationwasappliedtoa24htestperiod,anditsperformance
wasevaluated. However,theLinearRegressionmodelwastheleastaccurateamongthe
testedmethods, withaMAPEof17.3%andAbsoluteMaximumError(AME)of45.1%,
makingittheweakestmodelintermsofforecastingpeakelectricaldemand. Incontrast,
theANNmodelsignificantlyoutperformedallothermodels,achievingaMAPEof3.9%
andAMEof8.2%. TheANNmodelwasdesignedusingkeybuildingparameterssuchas
HVACenergyconsumption,timeofday,typeofday,outdoortemperature,andhumidity
asinputs. Itwasabletodynamicallyadjusttocomplexpatternsinenergyconsumption,
making it the most effective forecasting approach. The Simple Moving Average model
wasalsotested,usinga60minwindowofpastdatatopredictthenext60min. Ithada
MAPEof7.7%andanAMEof26.2%,performingbetterthanLinearRegressionbutstill
farlessaccuratethanANN.TheMARSplinesmodel,whichisanonparametricregression
technique, wasincludedasanotherbenchmarkmethod. Itofferedimprovedflexibility

Energies2025,18,4032 10of27
overtraditionalregressionbutstillunderperformedcomparedtoANN.TheMAPEfor
MARSplineswas7.0%,andtheAMEwas22.5%,makingitthesecond-bestmethodafter
ANN.Overall,thestudyconcludedthatANNsprovidethebestforecastingaccuracyfor
short-term peak electrical demand in large buildings, outperforming statistical models
suchasLinearRegression,SMA,andMARSplines. TheANN-basedforecastingapproach
demonstrated its ability to effectively reduce peak demand charges by providing real-
timepredictiveinsights,enablingbuildingmanagementtotakeproactivestepstoreduce
energyconsumption.
Thestudy[33]explorestheuseofANNforshort-termloadforecastinginmicrogrids.
Thestudyanalyzesvariouspredictionmodelsandexaminestheimpactofdifferentinput
variables,includingsolarradiation,onforecastaccuracy.
Theresearchismotivatedbytheincreasingcomplexityofmodernpowersystems,
particularlywiththeintegrationofrenewableenergysourcesanddistributedgeneration,
whichmakesdemandforecastingmorechallenging. ThestudyisbasedontheCEDER-
CIEMAT microgrid in SPAIN, using two datasets: one covering 4.5 years of electricity
consumptiondata,andanothercovering4monthsthatincludessolarradiationdata. The
forecastingmodelsuseamulti-layerperceptron(MLP)neuralnetworkandtestdifferent
learningalgorithms,suchasLevenberg-Marquardt,gradientdescent,andresilientprop-
agation. Severalinputconfigurationsaretested, includingpreviousdataconsumption,
workdayclassification,anddayoftheweekandmonth. Thestudyevaluatesmodelperfor-
manceusingMAPEasthekeymetric. Thebest-performingmodelincludesprevious-day
consumption,workdayclassification,andmonthasinput. ThismodelachievesaMAPEof
15.34%whentrainedonthelargerdatasetand16.69%whentrainedonthesmallerdataset.
Surprisingly,addingsolarradiationasaninputvariabledoesnotimproveforecastaccuracy.
Thestudyalsofindsthatamodeltrainedononly3monthsofdatacanachievesimilar
accuracytoonetrainedon3yearsofdata. Theresultshighlightthechallengesofload
forecastinginmicrogridsduetohighvariabilityindemandprofiles. Thefindingssuggest
thatwhileANNmodelsareeffectiveforSTFL,carefulselectionofinputvariablesiscrucial.
Futureresearchwillexploreadditionalfactorsinfluencingdemandpatternsandvalidate
newmodelsinmicrogridenvironments.
The study [37] uses an ensemble deep-learning method combining three models:
Long Short-Term Memory, Gated Recurrent Unit (GRU), and Temporal Convolutional
Networks(TCN).Thedatasetincludes14yearsofmonthlyelectricityconsumptiondata
from nearly 2000 clients in Bejaia, Algeria. The proposed models are evaluated using
statisticalmetricssuchasMAE,MAPE,andRMSE.Theresultsshowthattheensemble
modelssignificantlyoutperformindividualmodelsandtraditionalforecastingmethods,
providing more accurate electricity consumption predictions. The research concludes
that ensemble deep-learning approaches offer substantial improvements in forecasting
performance and can be effectively used by energy suppliers like Sonelgaz to enhance
electricityplanningandmanagement.
Thearticle[38]presentsanovelhybridapproachthatintegratesclassicalstatistical
techniquesandmachinelearningfornationalelectricitydemandforecasting. Thestudy
addressestheneedforlong-termforecastswithhigh-resolutiondata,essentialforenergy
systemplanningandinvestment. UsinghourlyelectricityconsumptiondatafromUkraine
between2013and2020,themodeldecomposesdemandintolong-term,medium-term,and
short-termcomponents. Thelong-termtrendismodeledusingmacroeconomicregression
analysis,themedium-termmodelincorporatestemperatureandcalendarregressorswhile
combiningARIMAandLSTMapproachestocaptureresidualpatterns,andtheshort-term
modelaccountsforhourlyseasonalityusingcalendar-basedregressionandARMAmodels
for residuals. The results show that the best-performing model is a hybrid approach

Energies2025,18,4032 11of27
combining multiple regression models with LSTM for residual forecasting, achieving
an accuracy of 96.83% over a 2-year test period with 17,520 time steps. The short-term
forecastinganalysisconfirmedthatdailyelectricityconsumptionpatternsremainedstable
over the years, and ARMA models effectively captured hourly variations, making the
use of LSTM unnecessary for short-term residual prediction. The study demonstrates
thatintegratingstatisticalandmachine-learningmethodsenhancesforecastingaccuracy
byaddressingdifferenttimescaleswhileallowingforinterpretabilityinenergydemand
drivers. However,themodel’srelianceonaccuratemacroeconomicandweatherforecasts
posesachallengeforlong-termpredictions. Theauthorssuggestthatthemethodology
canbeappliedtoothercountriesandemphasizetheimportanceofautomationforfuture
implementations[39].
Thestudy[40]focusesonshort-term(daily)andmiddle-term(yearly)electricityload
forecasting at a local level within the French distribution grid. The authors propose a
semi-parametric approach based on Generalized Additive Models (GAMs) to estimate
therelationshipbetweenelectricitydemandandvariousexplanatoryvariables,suchas
temperature(currentandlagged),calendareffects(daysoftheweek,holidays,andspecial
tariffs),andseasonalpatterns(daily,weekly,andyearlycycles). GAMsofferflexibilityby
modelingnonlinearrelationships,makingthemwell-suitedforanalyzinglargedatasets.
Thedatasetusedinthisstudyconsistsofelectricityconsumptionrecordedevery10minutes
from2260substationsacrossFrancebetween2006and2011,combinedwithtemperature
data from 63 weather stations. Each substation was assigned to the nearest relevant
weather station. The results show that the middle-term forecasts achieved a median
Mean Absolute Percentage Error of 8%, which was reduced to 6% after applying an
additionaldetrendingstep. Forshort-termforecasting, incorporatinglaggedelectricity
consumptionsignificantlyimprovedaccuracy,loweringMAPEto5%. Comparedtonaïve
benchmarks, such as using the previous year’s load, the proposed models performed
significantlybetter. Thestudyhighlightstheeffectiveness,interpretability,andscalability
of GAM-based models for electricity load forecasting. However, the authors suggest
potentialimprovements,suchasautomaticvariableselectionusingtechniqueslikeLASSO,
integratingadditionalweatheranddemographicvariables,anddevelopingmultivariate
modelstocapturedependenciesbetweensubstations. Thefindingsdemonstratethatsemi-
parametricadditivemodelsprovideapromisingbalancebetweenaccuracy,interpretability,
andcomputationalefficiencyforelectricitydemandforecasting.
The article [41] explores short-term forecasting of renewable energy consumption
andgenerationinaPeer-to-Peer(P2P)energytradingsysteminWesternAustralia. The
researchisbasedonreal-timeenergydatacollectedfromsmartmetersinstalledinresi-
dential households between August 2018 and April 2019, with a time resolution of 5 s.
Thedatasetincludesenergyimportedfromandexportedtothegrid,rooftopphotovoltaic
(PV)generation,householdenergyconsumption,andoutdoortemperature. Avarietyof
forecastingmethodsweretested,includingstatisticalmodels,traditionalmachine-learning
techniques, and deep learning models. The results demonstrate that the LSTM model
significantlyoutperformsallotherapproaches,achievingthelowestRMSEandMAEfor
bothenergyconsumptionandgenerationforecasting. TheoptimizedLSTMmodelsuccess-
fullycapturedtheperiodicityandtemporaldependenciesofenergypatterns,makingit
moreaccuratethanclassicalmethodslikeARIMA,VAR,andlinearregression,aswellas
AutoML-basedmodels,suchasthoseimplementedinRapidMiner. Classicalmodelsfailed
to capture the complex nonlinear relationships in energy generation and consumption,
leadingtohighererrors. Machine-learningmodelsimplementedinRapidMiner(including
GradientBoostedTrees,RandomForest,andSVM)alsounderperformedcomparedtothe
deep-learning-basedLSTMmodel. Thestudyhighlightsthatdeep-learningapproaches,

Energies2025,18,4032 12of27
particularlyLSTMnetworks,providesignificantaccuracyimprovementsinshort-termen-
ergyforecastingduetotheirabilitytoretainlong-termdependenciesandadapttodynamic
energyconsumptionpatterns. Theauthorssuggestfurtherimprovementsbyintegrating
ConvolutionalNeuralNetworks(CNNs)withLSTMtoenhancefeatureextractionand
employingadvancedhyperparametertuningtechniques.
Thestudy[32]investigatesshort-termforecastingofphotovoltaicpowerproduction
inaself-consumptionsystemusinghybriddeep-learningmodels. Theauthorspropose
twohybridmodels, CNN-LSTMandConvLSTM,whichcombineCNNandLSTMnet-
works. ThesemodelsaimtocapturebothspatialandtemporaldependenciesinPVpower
generationdata. TheirperformanceiscomparedagainstastandardLSTMmodel,which
serves as the baseline. The study employs two datasets, an univariate dataset, which
onlyincludeshistoricalPVpoweroutput,andamultivariatedataset,whichincorporates
additionalweatherfeaturessuchastemperature,windspeed,humidity,cloudcover,and
solarirradiation. Theforecastscovertimehorizonsrangingfrom1dayto1weekahead.
ThemodelsareevaluatedbyusingRMSE,MAE,andMAPE.Shorterforecasthorizons
yieldedmoreaccuratepredictionsacrossallmodels. The1-day-aheadforecastperformed
thebest,withCNN-LSTMandConvLSTMachievingthelowesterrorrates. Hybridmodels
(CNN-LSTMandConvLSTM)outperformedthestandaloneLSTMmodelacrossallforecast
horizons. This confirms that integrating CNN with LSTM enhances feature extraction
and learning capabilities. Multivariate datasets improved forecast accuracy for longer
horizons,highlightingtheimportanceofincorporatingweather-relatedvariablesinPV
powerprediction. Theaccuracyofallmodelsdeclinedastheforecasthorizonincreased,
butthehybridmodelsretainedasignificantedgeoverthebaselineLSTM.
Thearticle[42]proposesadaptingtheTransformerarchitectureforelectricalloadfore-
casting. TheproposedTransformer-basedmodeladdressestheselimitationsbyleveraging
itsinherentparallelprocessingcapabilitiesandisdesignedtohandlediversedatastreams
toensureportabilityandreproducibility. TheauthorsmodifiedthestandardNLPTrans-
formerworkflowbyintroducinganN-spacetransformationmoduleandanoveltechnique
forincorporatingcontextualfeaturesdirectlywithintheTransformerarchitecture. Thisap-
proachaimstoimproveforecastingaccuracywhileovercomingtheperformancechallenges
ofdeep-learningmodelsinloadforecasting. Evaluationacross20distinctdatastreams
andvariousforecastinghorizonsdemonstratedthattheadaptedTransformersuccessfully
handlestimeserieswithcontextualdataandoutperformsstate-of-the-artSeq2Seqmodels.
Thereference[43]appliesaTransformer-basedmodeltoforecastelectricvehicle(EV)
chargingdemand. Theaimofthestudywastoaccuratelypredicthourlyenergydemandat
EVchargingstations,whichiscrucialforinfrastructuremanagementandnetworkstability.
ThemodelwastestedonactualdatafromaGermanchargingstationoperator,including
chargingtime,sessionlength,energyvolume,andlocationID.Themodelarchitectureused
aTransformerEncoderwithaself-attentionmechanismtocapturetemporalandseasonal
dependencieswithouttheneedtoprocessthedatasequentially,asinRNNorLSTM.The
inputdataincludedatimewindowof24h,andthemodelforecasteddemandforthenext
24h—whichmeansforecastingwithatimestepof1h,24hahead. Themodelachieved
better results (lower MAE and RMSE) than the classic LSTM and GRU, demonstrating
itseffectivenessinenvironmentswithhighdatavariability. Theauthorsemphasizethat
thisapproachcanbeanimportanttoolfornetworkoperators,especiallyinthecontextof
increasingEVanddynamicloads.
Thisscientificpaper[44]introducesanewandimprovedmethodforforecastingthe
outputofrenewableenergysourceslikesolarandwindpower. Accuratepredictionsare
vital because the variability of these energy sources can make managing the electrical
gridchallenging. TheauthorsproposeanovelsystemcalledH-Transformer,whichisa

Energies2025,18,4032
13of27
hybridmodeldesignedtotacklethisuncertainty. Ituniquelycombinesamoretraditional,
straightforwardforecastingmethodcalledSARIMA(whichhandlesclear,linearpatterns)
withacutting-edgeTransformerneuralnetwork.TheTransformercomponentisspecifically
usedtopredictthe“leftover”complex,non-linearpatternsthatSARIMAmightmiss,and
thesystemalsointegratesexternalinformationlikeweatherdataforbetteraccuracy. The
H-Transformerworksinthreestages: first,SARIMAmakesaninitialprediction;then,the
Transformeranalyzesandforecaststheerrorsfromthatfirstprediction;finally,thesetwo
forecastsarecombined. Thisintelligentdesignaimstocapitalizeonthestrengthsofboth
linear and advanced non-linear modeling. The model’s settings are fine-tuned using a
smartoptimizationtechniquecalledBayesianOptimization. Throughextensivetestson
five different datasets of wind speed and solar energy, the H-Transformer consistently
showedbetterpredictionaccuracythanvariousstandalonemachine-learningmodels. It
alsofrequentlyoutperformedotherhybridforecastingapproaches,provingtobeahighly
effectiveandreliabletoolforshort-termrenewableenergyforecasting. Table2providesa
summaryoftheforecastingmethodsforshort-termelectricityconsumption,asdiscussed
inthissection.
Table2.Summaryofshort-termloadforecastingconsumptionmethods.
| Forecasting | Authors/   |                | Model/      | Forecast   | Accuracy  |               | Disadvantages/   |
| ----------- | ---------- | -------------- | ----------- | ---------- | --------- | ------------- | ---------------- |
| No.         |            | InputData      |             |            |           | Advantages    |                  |
| Method      | Source     |                | Algorithm   | Horizon    | (Metrics) |               | Limitations      |
|             |            |                | ARIMA,      |            |           | Well-known,   |                  |
|             | TayKim     | Electricity    | Holt-       | Short-term |           | easyto        | Limitedforhighly |
| Time-Series |            |                |             |            | MAPE,     |               | nonlineardata,   |
| 1           | Gaiketal.  | consumption    | Winters,    | (daily,    |           | implement,    |                  |
| Models      |            |                |             |            | RMSE,MAE  |               | needsstationary  |
|             | (2018)[36] | historicaldata | Exponential | hourly)    |           | goodforstable |                  |
input
|     |     |     | Smoothing |     |     | demand |     |
| --- | --- | --- | --------- | --- | --- | ------ | --- |
ANNadaptsto
Artificial Government ANN,SMA, Short-term nonlinear Requiresalotof
JasonGrant
Neural building Linear (hourly, MAPE= patternsbetter trainingdata,
| 2   | etal.(2014) |     |     |     |     |     |     |
| --- | ----------- | --- | --- | --- | --- | --- | --- |
Networks electricity Regression, 60min 3.9%,AME than sensitiveto
[37]
| (ANN) |     | demand | MARSplines | ahead) |     | traditional | hyperparameters |
| ----- | --- | ------ | ---------- | ------ | --- | ----------- | --------------- |
methods
Effectivefor
| Artificial | Luis         |                 |     | Short-term |      |             |                 |
| ---------- | ------------ | --------------- | --- | ---------- | ---- | ----------- | --------------- |
|            |              | Electricityload |     |            |      | complexload | Computationally |
| Neural     | Hernández-   |                 |     | (distribu- |      |             |                 |
| 3          |              | indistribution  | ANN |            | MAPE | patterns,   | expensive,      |
| Networks   | Callejoetal. |                 |     | tion       |      |             |                 |
|            |              | networks        |     |            |      | adaptive    | black-boxnature |
| (ANN)      | (2014)[34]   |                 |     | system)    |      |             |                 |
learning
LSTM,GRU,
|          |           | 14yearsof |          |            |     | Combines    |      |
| -------- | --------- | --------- | -------- | ---------- | --- | ----------- | ---- |
|          |           |           | Temporal |            |     |             | High |
| Ensemble | D.Hadjout | monthly   |          | Short-term |     | strengthsof |      |
4 Deep etal.(2022) electricity Convolu- (monthly, MAPE, multiple computationalcost,
|          |      |             | tional   |           | RMSE,MAE |             | requireslarge |
| -------- | ---- | ----------- | -------- | --------- | -------- | ----------- | ------------- |
| Learning | [38] | consumption |          | regional) |          | models,high |               |
|          |      |             | Networks |           |          |             | datasets      |
|          |      | (Algeria)   |          |           |          | accuracy    |               |
(TCN)
Hybrid
Hourlyelectricity
|                | T.González  |              |        | Short-term |           | approach      |                  |
| -------------- | ----------- | ------------ | ------ | ---------- | --------- | ------------- | ---------------- |
| Hybrid         |             | demand,      | Hybrid |            | MAPE      |               |                  |
|                | Grandón     |              |        | (hourly,   |           | improves      | Complexmodel,    |
| 5 Statistical& |             | temperature, | ARIMA+ |            | (96.83%   |               |                  |
|                | etal.(2023) |              |        | national   |           | accuracy,good | hightrainingcost |
| MLModel        |             | calendar     | LSTM   |            | accuracy) |               |                  |
|                | [39]        |              |        | level)     |           | forlong-term  |                  |
variables
forecasts
| Semi-      |            |                 |             |             |      | Interpretable, |                  |
| ---------- | ---------- | --------------- | ----------- | ----------- | ---- | -------------- | ---------------- |
|            |            | Electricityload | Generalized | Short&      |      |                | Requiresaccurate |
| Parametric | Yannig     |                 |             |             |      | flexible,good  |                  |
|            |            | from2260        | Additive    | Medium-     |      |                | temperature      |
| 6 Additive | Goudeetal. |                 |             |             | MAPE | for network-   |                  |
|            |            | substations,    | Models      | term(daily, |      |                | predictions,     |
| Models     | (2013)[41] |                 |             |             |      | level          |                  |
|            |            | temperature     | (GAM)       | yearly)     |      |                | complextuning    |
| (GAM)      |            |                 |             |             |      | forecasting    |                  |

Energies2025,18,4032
14of27
Table2.Cont.
| Forecasting | Authors/ |           | Model/    | Forecast | Accuracy  |            | Disadvantages/ |
| ----------- | -------- | --------- | --------- | -------- | --------- | ---------- | -------------- |
| No.         |          | InputData |           |          |           | Advantages |                |
| Method      | Source   |           | Algorithm | Horizon  | (Metrics) |            | Limitations    |
RMSE,MAE,
|     |     | PVplantpower |     |     |     | Hybridmodels |     |
| --- | --- | ------------ | --- | --- | --- | ------------ | --- |
MAPE
| Deep |     | output,weather |     |     |     | captureboth | Computationally |
| ---- | --- | -------------- | --- | --- | --- | ----------- | --------------- |
(CNN-LSTM
Learning AliAgga features Short-term spatialand expensive,requires
|     |     |     | CNN-LSTM, |     | and |     |     |
| --- | --- | --- | --------- | --- | --- | --- | --- |
7 (Hybrid etal.(2021) (temperature, (1dayto temporal alargedatasetand
|           |      |            | ConvLSTM |        | ConvLSTM |               |            |
| --------- | ---- | ---------- | -------- | ------ | -------- | ------------- | ---------- |
| CNN-LSTM, | [32] | windspeed, |          | 7days) |          | dependencies, | fine-tuned |
outperform
| ConvLSTM) |     | humidity,cloud  |     |     |          | improving | hyperparameters |
| --------- | --- | --------------- | --- | --- | -------- | --------- | --------------- |
|           |     | cover,sunhours) |     |     | standard | accuracy  |                 |
LSTM)
|     |     | Hourlyelectricity | Transformer |     | RMSE= | Highaccuracy, | Trainedona |
| --- | --- | ----------------- | ----------- | --- | ----- | ------------- | ---------- |
Transformer- demand(dataset: encoder- 0.021,MAE= captures single-household
L’Heureux
| based |             | UCIIndividual | decoder |          | 0.015,MAPE | temporal | dataset; |
| ----- | ----------- | ------------- | ------- | -------- | ---------- | -------- | -------- |
| 8     | etal.(2023) |               |         | 24hahead |            |          |          |
time-series Household architecture =3.12%(on dependencies, performancemay
[43]
forecasting ElectricPower withself- normalized suitablefor varyonaggregated
|     |     | Consumption) | attention |     | data) | non-lineardata | data |
| --- | --- | ------------ | --------- | --- | ----- | -------------- | ---- |
Highaccuracy,
|     |     | HourlyEV | Transformer |     | RMSE= | captures | FocusedonEV |
| --- | --- | -------- | ----------- | --- | ----- | -------- | ----------- |
Transformer- chargingsessions with 24hahead 0.015,MAE= chargingonly;
|     | Koohfaretal. |     |     |     |     | tempo- |     |
| --- | ------------ | --- | --- | --- | --- | ------ | --- |
9 baseddeep (ACNdataset, multi-head (short- 0.010,MAPE resultsmaynot
|          | (2023)[44] |            |       |       |       | ral/sequential |                  |
| -------- | ---------- | ---------- | ----- | ----- | ----- | -------------- | ---------------- |
| learning |            | LosAngeles | self- | term) | =2.2% |                | generalizetofull |
patternsinEV
|     |     | area) | attention |     | (normalized) |     | griddemand |
| --- | --- | ----- | --------- | --- | ------------ | --- | ---------- |
demand
High
|              |     | Multivariate |        |     | RMSE     |             |               |
| ------------ | --- | ------------ | ------ | --- | -------- | ----------- | ------------- |
|              |     |              |        |     |          | performance | Complex       |
| Transformer- |     | renewable    | Hybrid |     | (solar): |             |               |
|              |     |              |        |     |          | onmultiple  | architecture; |
basedhybrid Padilhaetal. energydata CNN–GRU– 1to24h 0.003–0.011;
| 10  |     |     |     |     |     | sources;hybrid | requirestuning |
| --- | --- | --- | --- | --- | --- | -------------- | -------------- |
deep (2022)[45] (solarirradiance, Transformer ahead RMSE architecture andlargedatafor
| learning |     | wind,tempe-  | model |     | (wind):     |          |                   |
| -------- | --- | ------------ | ----- | --- | ----------- | -------- | ----------------- |
|          |     |              |       |     |             | enhances | fulleffectiveness |
|          |     | rature,etc.) |       |     | 0.029–0.073 |          |                   |
learning
3.3. Medium-TermLoadForecasting
ThispartofthearticlewillfocusonMedium-TermLoadForecasting,whichplaysa
bigroleinenergyplanningandgridmanagementbypredictingelectricitydemandovera
periodofseveralmonthstoafewyears.
Thestudy[45]comparedtheperformanceofARIMAandANNmodelstopredict
Taiwan’s energy consumption over different time horizons, including a medium-term
periodof1year,butalso3years,5years,and10years. Thesingle-variableARIMAmodel
demonstratedhighaccuracyforthe1-yearprediction, withaMAPEof3.14%, whichis
classifiedas“highlyaccurate”accordingtoLewis[46]. TheARIMAmodelisalinearstatis-
ticalapproachthatreliesonhistoricaldatatoforecastfuturetrends,makingitparticularly
effectiveforstationarytime-seriesdata. Inthisstudy,theARIMAmodelwasappliedto
asinglevariable—energyconsumption—andoutperformedthesingle-variableANNs1
modelinmosttimeframes,exceptforthemediumterm(3years),wherethe2008financial
crisislikelyimpacteditsaccuracy. TheARIMAmodel’sstrengthliesinitsabilitytohandle
linearrelationshipsanditssimplicity,asitdoesnotrequireadditionalexplanatoryvariables
likeGDPorpopulation. However,itsperformancecanbelimitedincasesofextremenon-
linearityorwhenexternalshocks(e.g.,economiccrises)disrupthistoricaltrends. Despite
theselimitations,theARIMAmodelprovedtobeareliableandpracticaltoolforenergy
consumptionforecasting,especiallyformedium-termandlong-termpredictions,whereit
consistentlydeliveredhighlyaccurateresults. Thismakesitavaluablebenchmarkmodel
forcomparisonwithmorecomplexapproacheslikeANNs. Inthestudy,theANNmodels
weredesignedtopredictTaiwan’senergyconsumptionusingdifferentcombinationsof
inputvariables,suchasenergyconsumption(ENG),GDP,population(POP),andexports
(EXP).Inthisarticle,exportreferstothevalueofgoodsandservicesexportedfromTaiwan
to other countries. It is a key economic factor used in energy consumption forecasting
models,ashigherexportlevelsoftencorrelatewithincreasedindustrialproductionand

Energies2025,18,4032 15of27
energydemand[47]. Themodelsrangedfromsimplesingle-variablesetups(e.g.,ANNs1,
whichonlyusedenergyconsumption)tomorecomplexmultivariableconfigurations(e.g.,
ANNs10,whichincludedenergyconsumption,exports,population,andGDP).Thegoal
wastodeterminewhichvariableshadthemostsignificantimpactonpredictionaccuracy
acrossdifferenttimehorizons(shortterm,mediumterm,medium–longterm,andlong
term). Forthe1-yearpredictionhorizon,theANNs8model,whichincludedenergycon-
sumptionandexports,achievedthehighestaccuracywithaMAPEof0.32%,indicating
thatexportsplayacrucialroleinshort-termenergyconsumptionforecasting. Incontrast,
theANNs5model,whichusedenergyconsumptionandpopulation,performedbestfor
long-term predictions (10 years), suggesting that population growth is a key driver of
energy demand over extended periods. The study also found that while adding more
variables(e.g.,GDP,population,exports)generallyimprovedpredictionaccuracy,simpler
modelswithfewervariables(e.g.,ANNs8orANNs5)oftenperformedjustaswelloreven
betterincertaintimeframes. Thishighlightstheimportanceofselectingtherightvariables
forspecificpredictionhorizons,asoverlycomplexmodelsmaynotalwaysyieldbetter
results. Overall,theANNmodelsdemonstratedflexibilityandeffectivenessincapturing
bothlinearandnonlinearrelationshipsinenergyconsumptiondata,makingthemvaluable
toolsforpolicymakersandenergyplannersinTaiwan.
Thearticle[48]focusesonpredictingthemaximumhourlyelectricityconsumption
perdayinSlovakiausingGreyModels(GM)andArtificialNeuralNetworks,aimingto
developmoreaccurateforecastingmodelsthantheofficialpredictionsprovidedbySEPS
(SlovakTransmissionSystemOperator). ThestudyutilizedGreyModelsfortrendanalysis
andamulti-layerfeed-forwardback-propagationneuralnetworkforcapturingcomplex
consumptionpatterns,withahybridmodelcombiningbothapproachestoimproveac-
curacy. Themodelsweretrainedondatafrom2010–2018andtestedondatafrom2019
and2020,withtheANNmodelachievingthebestresults,particularlyin1-yearhorizon
forecasts, while the GM model performed well in medium-term 2-year horizon predic-
tions. Thehybridmodel,combiningANNandGMinan85/15ratio,showedslightbut
measurable improvements in accuracy. All proposed models outperformed the official
SEPSpredictions,evenduringtheCOVID-19pandemicin2020,whichdisruptedenergy
consumptionpatterns.Thestudyconcludesthatthehybridmodel,alongwithGreyModels
andANN,offersareliableapproachforforecastingelectricityconsumptioninSlovakia,
providingvaluabletoolsforenergyindustryplanningandmanagement.
Thestudy[49]explorespredictingelectricityconsumptioninindustrialenterprises
with continuous production processes, using the ARIMA model. The study aimed to
develop accurate forecasting models that address the challenges of predicting energy
consumptioninindustrialsettings, wheretraditionalmethodsmaystruggleduetothe
complexity of the data. The article outlines a detailed algorithm for forecasting energy
consumptionusingARIMA,includingstepsfordifferencing,determiningautoregression
andmovingaverageorders,andutilizingtheDickey-Fullertesttocheckstationarity,along
with autocorrelation (ACF) and partial autocorrelation (PACF) functions to determine
model parameters. The ARIMA model was applied to predict energy consumption in
a metallurgical enterprise, and the comparison between actual and forecasted values
showedhighaccuracy,withaforecastingerrorof6%. Theresultsdemonstratethatthe
ARIMA model is suitable for predicting energy consumption in industrial enterprises
withcontinuousproductionprocesses. ThestudyconcludesthattheARIMAmodelisan
effectivetoolforenergyconsumptionforecasting,providinghighaccuracyandreliability,
anditcanbeusedforplanningandoptimizingenergyuseinindustrialenterprises,thereby
improvingenergyefficiency.

Energies2025,18,4032 16of27
Thearticle[50]analyzesdifferentforecastingmodelsforTurkishelectricityconsump-
tion, comparing single time-series models like SARIMA with hybrid machine-learning
modelssuchasSARIMA-ANNsandSARIMA-MLPs. Themainobjectiveofthestudywas
todeterminethemostaccurateforecastingmodelforelectricityconsumptioninTürkiyeby
evaluatingbothtraditionalstatisticalmodelsandadvancedhybridmodels. Theresearchers
testedvarioushybridmodels,includingtheZhangadditivehybridmodel,themultiplica-
tiveWangetal. model,andthecombinedmodelbyKhashei&Bijari[51–53]. Thestudy
examinedhowthesemodelshandlelinearandnonlinearcomponentsofthetimeseries,
whichareoftendifficulttoseparateinelectricityconsumptiondata. Theresultsconfirm
that hybrid models are more effective than single models when forecasting electricity
consumptioninTürkiye. TheKhashei&Bijari(SARIMA-ANNs)hybridmodelisthemost
suitableapproachwhenlinearandnonlinearstructurescannotbeeasilyseparatedand
hadthelowestRMSE(0.0792)andMAE(0.04463),makingitthemostaccuratemodel. The
traditional SARIMA model performed worse, with an RMSE of 0.0823 and an MAE of
0.0523. Machine-learningtechniques,particularlyANNswiththeGRpropalgorithm,can
significantlyenhanceforecastingaccuracy. Incaseswhereelectricityconsumptionpatterns
arehighlycomplexandnonlinear,traditionalstatisticalmodelslikeSARIMAmaynotbe
sufficient. Thestudysuggeststhatfutureforecastingapproachesshouldintegratehybrid
techniquestoachievemorereliablepredictionsforelectricitydemandplanning.
Thestudy[54]presentsanoptimizeddeep-learning-basedLSTMmodelforelectric
loadforecasting. Theresearchfocusesonenhancingforecastingaccuracythroughfeature
selection and the use of a genetic algorithm (GA) to optimize time lags and the LSTM
networkarchitecture. Thedatasetusedforvalidationconsistsofelectricityconsumption
data from metropolitan France. The LSTM model was compared against conventional
machine-learningmodels,includinglinearregression,k-nearestneighbors,randomforests,
gradientboosting,andartificialneuralnetworks. Amongthese,theExtraTreesRegres-
sor model performed best and was used as a benchmark. Feature importance analysis
revealed that time lags played a crucial role in forecasting accuracy, whereas weather-
relatedvariables,suchastemperature,hadalimitedinfluence. TheGAwasappliedto
determinetheoptimalnumberoftimelagsandhiddenlayersintheLSTMmodel,ensuring
improvedpredictiveperformancewhileavoidingoverfitting. Theresultsshowedthatthe
optimizedLSTMmodelsignificantlyoutperformedconventionalmachine-learningmodels.
TheLSTMmodelachievedarootmeansquareerror(RMSE)of378comparedto513.8for
theExtraTreesmodel,representinganimprovementofapproximately26.4%. Similarly,the
MAEfortheLSTMmodelwas270.4,comparedto344fortheExtraTreesmodel,yieldinga
21.4%improvement. ThecoefficientofvariationforRMSE(CVRMSE)wasalsoreduced
from1.95%intheExtraTreesmodelto1.31%intheLSTMmodel. Thestudyevaluated
bothshort-term(2weeks)andmedium-term(upto4months)forecastinghorizons. For
short-termpredictions,theRMSEwas339,whileformedium-termpredictions,itranged
between258and294,dependingontheforecastingwindow. TheCVRMSEforshort-term
forecastswas0.61%,whileformedium-termforecasts,itaveraged0.56%,indicatingstable
andreliableperformanceovervaryingforecastingperiods. Theproposedapproachdemon-
stratedtheeffectivenessofdeeplearningincapturingcomplextime-seriespatternsand
optimizingforecastingperformance.Byleveragingfeatureselectionandgeneticalgorithms,
theLSTMmodelprovidesarobustsolutionforelectricloadforecasting,outperforming
traditionalmachine-learningmodelsinbothaccuracyandstability.
Thestudy[55]explorestheapplicationoftime-seriesmodelsforforecastingenergy
consumptioninIndia,withaparticularfocusonelectricityconsumption. Threemodels
wereused: theGrey-Markovmodel,theGreymodelwitharollingmechanism,andSingu-
larSpectrumAnalysis(SSA).TheGreymodelwitharollingmechanismwasspecifically

Energies2025,18,4032
17of27
employedtopredictelectricityconsumptiontrends. Theresearchanalyzedhistoricalelec-
tricityconsumptiondatafrom1970to2007,revealingasignificantincreasefrom43.7TWh
to443.1TWh. Duetotherapidgrowthinenergydemand,accurateforecastingiscrucialfor
energypolicyplanningandsustainability. Forelectricityconsumptionforecasting,theGrey
modelwitharollingmechanismwaschosenduetoitssuitabilityforcapturingexponential
growthtrendsintime-seriesdata. Themodelwastrainedusing5yearsofhistoricaldata
topredictthenextyear’sconsumption. Twoout-of-sampleforecastswereperformedto
validatethemodel,andtheresultsshowedaMAPEof3.4%. Thepredictionaccuracyfor
thelast2yearsofvalidationdatawas96.9%and95.1%,demonstratingthemodel’seffec-
tiveness. Thestudyconcludedthatthistime-seriesapproachprovidesaviableandaccurate
alternativeforelectricityconsumptionforecasting. Comparedtotheprojectionsfromthe
PlanningCommissionofIndia,themodeldemonstratedcomparableorevenbetterfore-
castingaccuracy,makingitausefultoolforenergyplanninganddecision-making. Table3
providesasummaryoftheforecastingmethodsformedium-termelectricityconsumption,
asdiscussedinthissection.
Table3.Summaryofmedium-termloadforecastingconsumptionmethods.
| Forecasting | Authors/ |           | Model/    | Forecast | Accuracy  |            | Disadvantages/ |
| ----------- | -------- | --------- | --------- | -------- | --------- | ---------- | -------------- |
| No.         |          | InputData |           |          |           | Advantages |                |
| Method      | Source   |           | Algorithm | Horizon  | (Metrics) |            | Limitations    |
Short-term
|          |     |     |     | (1year),    |     | ARIMA       |            |
| -------- | --- | --- | --- | ----------- | --- | ----------- | ---------- |
| ARIMAand |     |     |     | Medium-term |     | suitablefor | ARIMAneeds |
artificial Feng-Kuang Taiwan’s ARIMA, (3years), lineardata, stationarydata,
| 1        | Chuangetal. | energycon- |     |             | RMSE,MAE |              |              |
| -------- | ----------- | ---------- | --- | ----------- | -------- | ------------ | ------------ |
| neural   |             |            | ANN | Medium-long |          | ANNbetterfor | ANNrequires  |
|          | (2013)[46]  | sumption   |     |             |          |              |              |
| networks |             |            |     | (5years),   |          | non-linear   | largedataset |
|          |             |            |     | Long-term   |          | patterns     |              |
(10years)
Slovakia’s
|              | Michal      | daily       |             | One-year- |          | Hybridmodels | Requires          |
| ------------ | ----------- | ----------- | ----------- | --------- | -------- | ------------ | ----------------- |
| Greymodels,  |             |             | Greymodels, |           |          |              |                   |
|              | Pavlicko    | maximum     |             | aheadand  |          | moreaccurate | high-qualitydata, |
| 2 ANN,hybrid |             |             | ANN,hybrid  |           | RMSE,MAE |              |                   |
|              | etal.(2022) | electricity |             | two-year- |          | thanofficial | limited           |
models [49] consump- models aheadforecasts forecasts interpretability
tion
Short-term
Usefulfor
| Time-series |            |             |       | (1year),    |       |              |                  |
| ----------- | ---------- | ----------- | ----- | ----------- | ----- | ------------ | ---------------- |
|             |            | Industrial  |       |             |       | continuous   | Limited          |
| modelsfor   |            |             |       | Medium-term |       |              |                  |
|             | Rakhmonov  | enterprises |       |             |       | production   | applicabilityfor |
| industrial  |            |             |       | (3years),   | MAPE, |              |                  |
| 3           | I.U.etal.  | electricity | ARIMA |             |       | enterprises, | non-stationary   |
| electricity |            |             |       | Medium-long | RMSE  |              |                  |
|             | (2023)[50] | consump-    |       |             |       | automatic    | industrial       |
| consump-    |            |             |       | (5years),   |       |              |                  |
|             |            | tion        |       |             |       | component    | processes        |
| tion        |            |             |       | Long-term   |       |              |                  |
|             |            |             |       | (10years)   |       | adjustment   |                  |
Hybrid
|        |      |         | SARIMA, | Short-term |           |              |                 |
| ------ | ---- | ------- | ------- | ---------- | --------- | ------------ | --------------- |
| models | Ebru | Turkish |         |            |           | Hybridmodels | Computationally |
|        |      |         | ANNs,   | (daily,    | RMSE,MAE, |              |                 |
(SARIMA- Çag˘layan- electricity outperform intensive,requires
| 4       |            |          | MLPs,  | monthly)and | sMAPE, |               |                |
| ------- | ---------- | -------- | ------ | ----------- | ------ | ------------- | -------------- |
| ANNs,   | Akayetal.  | consump- |        |             |        | singlemodels, | hyperparameter |
|         |            |          | hybrid | medium-term | MASE   |               |                |
| SARIMA- | (2024)[51] | tion     |        |             |        | highaccuracy  | tuning         |
|         |            |          | models | (yearly)    |        |               |                |
MLPs)
LSTM
| LSTMwith |     | France | LSTM, | Short-term |     | outperforms | High |
| -------- | --- | ------ | ----- | ---------- | --- | ----------- | ---- |
feature SalahBouktif metropolitan feature (half-hourlyto MLmodels,
|     |     |     |     |     | RMSE,MAE, |     | computationalcost, |
| --- | --- | --- | --- | --- | --------- | --- | ------------------ |
5 selection& etal.(2018) electricity selection, weekly)and optimallag
|         |      |          |         |             | CV(RMSE) |           | sensitiveto |
| ------- | ---- | -------- | ------- | ----------- | -------- | --------- | ----------- |
| genetic | [55] | consump- | genetic | medium-term |          | selection |             |
hyperparameters
| algorithm |     | tion | algorithm | (monthly) |     | improves |     |
| --------- | --- | ---- | --------- | --------- | --- | -------- | --- |
results
Grey-Markov
| Grey- |     |     | Grey- |     |     |     |     |
| ----- | --- | --- | ----- | --- | --- | --- | --- |
model
| Markov,   |        |         | Markov,   |           |       |          | Limitedfor   |
| --------- | ------ | ------- | --------- | --------- | ----- | -------- | ------------ |
|           | Ujjwal | India’s |           | Long-term | MAPE, | provides |              |
| GreyModel |        |         | GreyModel |           |       |          | nonlinearand |
6 withrolling Kumaretal. energycon- withrolling (multiple prediction accurate highlydynamic
|            | (2010)[56] | sumption |            | years) | accuracy | forecasts, |         |
| ---------- | ---------- | -------- | ---------- | ------ | -------- | ---------- | ------- |
| mechanism, |            |          | mechanism, |        |          |            | changes |
96.9%accuracy
| SSA |     |     | SSA |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
forelectricity

Energies2025,18,4032 18of27
3.4. Long-TermLoadForecasting
Long-termloadforecasting(LTLF)hasapivotalroleinenergyplanningandmanage-
ment,enablingutilities,policymakers,andgridoperatorstoanticipatefutureelectricity
demandoverextendedperiods,typicallyrangingfromseveralyearstodecades. Accurate
long-termforecastssupportinvestmentdecisionsinpowergeneration,transmission,and
distributioninfrastructure,ensuringastableandefficientenergysupply. Variousmethods,
includingstatisticalmodelslikeARIMAandmachine-learningapproaches,areemployed
topredictconsumptionpatternsbasedonhistoricaldata,economicgrowth,population
expansion,andtechnologicaladvancements. Aselectricitydemandcontinuestoevolve
duetourbanization,industrialization,andtheintegrationofrenewableenergysources,
reliablelong-termforecastingbecomesincreasinglyvitalforsustainableenergyplanning
andpolicydevelopment[56].
Thearticle[57]presentsamethodologythatintegratesthebottom-upapproachwith
hierarchicallinearmodelsandBayesianinferencetoforecastlong-termelectricityconsump-
tion. Thisapproachallowsforamoredetailedandstructuredanalysisbybreakingdown
electricityconsumptionattheprocesslevelandaggregatingresultsforanentireindustrial
sector. Bayesianinference,combinedwithMarkovChainMonteCarlo(MCMC)methods,
enablesuncertaintyquantification,makingtheforecastsmorereliable. Thestudyapplies
thismethodologytotheBrazilianpulpandpaperindustry,analyzinghistoricalelectric-
ityconsumptionfrom2008to2014andprojectingitupto2050. Themodelsuccessfully
capturespastconsumptionpatternswithhighaccuracy(MAPE=2%)andgeneratesproba-
bilisticforecastsratherthansingle-pointestimates. Theresultsindicateasteadyincreasein
electricityconsumption,reaching170PJby2050inascenariowherenoenergyefficiency
measures(EEMs)areapplied. However,implementingcost-effectiveEEMscouldreduce
consumptionby25%,leadingtoatotalof128PJin2050.Comparedtodeterministicmodels,
theBayesianstochasticmodelprovidesprobabilitydistributionsforeachforecastedyear,
offeringcredibleintervalsthataidindecision-making. Thestudyhighlightstheimportance
ofincorporatingenergyefficiencymeasuresandpresentsdifferenttechnologicaldiffusion
scenarios,showingthatproactivepoliciescansignificantlyreduceenergydemand. The
findingscontributetolong-termenergyplanning,offeringanovelprobabilisticapproach
thatenhancestherobustnessofelectricityconsumptionforecasts.
Thearticle[58]presentsaregression-basedapproachtoforecastingmonthlyelectricity
demandinSouthKorea. Theproposedmodelintegrateskeyexternalvariables,including
weatherconditions(temperature,solarradiation),calendardata(workingdays,holidays),
andindustrialactivity(numberofregisteredfactories),whichsignificantlyinfluenceelec-
tricityconsumption. Thestudyaimstoidentifythemostimpactfulfactorsandconstruct
aregressionmodelthatprovidesaccuratemid-termforecasts. Thedatasetcovershistori-
calelectricityconsumptionfrom2012to2021,andthemodelisusedtopredictmonthly
demand for 2022 and 2023. The data sources include the International Energy Agency
(IEA)forelectricityconsumption,theKoreanMeteorologicalAdministrationforweather
data, the Korean Statistical Information Service (KOSIS) for industrial activity, and the
WHOCOVID-19Dashboardforpandemic-relatedimpacts. Theregressionmodelcaptures
seasonaltrends,temperatureeffects,industrialproductionlevels,andcalendarinfluences,
improvingforecastingaccuracy. Theregressionequationincludeskeypredictorssuchas
electricityconsumptionfromthesamemonthinthepreviousyear(seasonality),month
asacategoricalvariable(seasonalfluctuations),averagetemperature(non-lineareffects
onenergydemand),numberofworkingdays(calendarinfluence),numberofholidays
(reducedindustrialactivity),numberofregisteredfactories(industrialelectricityconsump-
tion),andaninteractiontermbetweenindustrialactivityandseasonality. Additionally,the
studyincorporateslog-transformedCOVID-19casestoexaminethepandemic’simpact

Energies2025,18,4032 19of27
on electricity demand. Correlation analysis confirms that temperature, industrial pro-
duction,andseasonalfactorsplayasignificantroleinpredictingelectricityconsumption.
Toevaluatetheperformanceoftheproposedmodel,thestudycomparesitwithvarious
forecastingtechniques,includingtraditionaltime-seriesmodels(Holt–Winters,SARIMA,
Prophet),machine-learningmethods(RandomForest,XGBoost,LightGBM,RNN,LSTM),
and ensemble approaches (combinations of multiple models). The results demonstrate
thattheregressionmodeloutperformsalltestedmethods, achievingaMAPEof2.01%,
thelowestamongallmodels. BenchmarkmodelssuchasSARIMAandLSTMperformed
worse,withMAPEvaluesexceeding4%,highlightingtheefficiencyoftheregressionap-
proachinhandlingmid-termloadforecasting. Onekeyfindingisthatmachine-learning
modelsdidnotconsistentlyoutperformtheregressionmodel,particularlyduetolimited
availablemonthlydata. WhileMLmodelsgenerallyperformwellwithlargedatasets,the
studysuggeststhatawell-structuredregressionmodelwithcarefullyselectedvariables
canachievesuperiorperformancewithsmallerdatasets. Furthermore,ensemblemethods
improved the accuracy of individual models but failed to surpass the performance of
the proposed regression model. The study concludes that considering external factors
suchasindustrialactivity,calendareffects,andweatherconditionssignificantlyenhances
forecastingaccuracy. Thefindingsareparticularlyrelevantforenergypolicymakers,grid
operators,andindustryplanners,providingareliableandinterpretabletoolformid-term
electricitydemandforecasting. Theresearchalsosuggeststhatfutureworkshouldexplore
additionaleconomicindicators,hybridmodelscombiningstatisticalandmachine-learning
approaches,andadaptivelearningtechniquestofurtherenhancepredictiveaccuracy.
Thisstudy[59]examineslong-termelectricityconsumptionforecastinginAlgeriaby
comparingtwoforecastingmodels: ARIMAandGM.Theresearchhighlightsthecritical
roleofelectricityconsumptionineconomicdevelopmentandenergysecurity,emphasizing
theneedforaccurateforecastingmethodstosupportstrategicplanningandpolicy-making.
The study utilizes annual electricity consumption data from 1982 to 2020, dividing the
datasetintoatrainingperiod(1980–2015)andatestingperiod(2016–2021). BothARIMA
andGMmodelsareappliedtoforecastconsumptiontrends,withperformanceevaluated
using the MAPE metric. The results indicate that the ARIMA model significantly out-
performstheGMmodel,withamuchlowerMAPEvalueof4.47%forARIMAvs. 67.95
forGM,demonstratingsuperiorpredictiveaccuracy. TheARIMAmodelisthenusedto
generateforecastsfrom2022–2030,predictingasteadyincreaseinelectricityconsumption,
withvaluesrisingfrom65,333GWhin2022to76,976GWhin2030. Thestudyunderscores
theimportanceofrobustforecastingtechniquesinguidingAlgeria’senergypolicies,in-
frastructuredevelopment, andsustainableenergystrategies. Thefindingssuggestthat
ARIMAisamorereliablemodelforelectricityconsumptionforecasting, whiletheGM
model,despiteitslowerdatarequirements,islessaccurateinlong-termpredictions.
Thestudy[60]forecastsrenewableenergyconsumptionandgrossfinalenergycon-
sumption(GFEC)insixEuropeancountries(France,Germany,Italy,Spain,Turkey,andthe
UK)fortheperiod2020–2030,basedonhistoricaldatafrom2004–2018. Theforecasting
method applies an optimized fractional nonlinear grey Bernoulli model (OFANGBM),
enhancedwithgeneticalgorithm(GA)optimization,whichimprovespredictiveaccuracy
overthetraditionalFANGBMmodel. Keyfindingsindicatethattotalenergyconsumption
(GFEC)andrenewableenergyconsumption(RES)willincreaseacrossallcountries,with
the highest share of renewables in 2030 expected in the UK (29.7%) and Spain (27.5%),
whileTurkeyisprojectedtohavethelowestshare(15.1%). Germanywillhavethehighest
absoluterenewableenergyconsumption(53.8Mtoe),whileItalyandTurkeywillexperi-
enceslowergrowth. Thestudyhighlightsthatsomecountriesmaystruggletomeettheir
renewableenergytargets,emphasizingtheneedforstrategicpolicyplanning. Theresults

Energies2025,18,4032 20of27
demonstratethattheOFANGBMmodeloutperformspreviousgreyforecastingapproaches,
providingmorereliablepredictionsforenergypolicymakers.
Thestudy[61]focusesonlong-termelectricityconsumptionforecastinginItalyusing
linearregressionmodelsbasedonhistoricaldatafrom1970to2007. Theforecastingmodels
incorporatekeyeconomicanddemographicvariables,particularlyGDP,GDPpercapita,
andpopulationgrowth,toestimatefutureelectricitydemand. Theresultsindicatethat
GDPisthemostsignificantdriverofelectricityconsumption,withastrongpositivecor-
relationbetweeneconomicgrowthandenergydemand. Forecastssuggestthatelectricity
consumptioninItalywillcontinuetogrowatanaverageannualrateofapproximately2%
until2030. ModelsthatincludeGDPandpopulationprovidethemostaccuratepredictions,
while those relying solely on GDP per capita are less effective. The study compares its
forecastswithofficialprojectionsfromTerna(Italy’stransmissionsystemoperator)and
CESI(aresearchinstitute),findingthatthedevelopedmodelsaligncloselywithofficial
estimates,withdeviationsrangingfrom±1%(best-case)to±11%(worst-case). Thisvalida-
tionhighlightsthereliabilityofsimpleregression-basedforecastingmethodsforlong-term
energyplanning. Oneofthekeypolicyimplicationsisthatelectricitypriceshavealimited
impactonconsumption,makingthemanineffectivetoolfordemandregulation. Instead,
forecastingenergyconsumptionshouldbecloselylinkedtoGDPgrowthprojections,as
economicexpansionremainstheprimaryfactorinfluencingenergydemand. Thearticle
aboutItalyisfrom2009, andthemodelproposedhadlittleincommonwiththeactual
conditionsandchallengesfacedbytheItalianenergysectorinthefollowingyears.
Thestudy[62]examineselectricityconsumptionforecastinginBrazil’sindustrialsec-
torusingstatisticaltime-seriesmodelsandartificialneuralnetworks(ANNs). Theresearch
comparestheeffectivenessoftraditionalforecastingapproaches,includingHolt-Winters,
SARIMA,DynamicLinearModel(DLM),andTBATS,againstAI-basedmodelssuchas
NeuralNetworkAutoregression(NNAR)andMLP.Monthlyelectricityconsumptiondata
fromJanuary1979toDecember2020wereused,withmodelstrainedondatafrom1979
to 2018 and tested on the 2019–2020 period. The results indicate that the MLP model
achievedthehighestaccuracy,outperformingallstatisticalmodels,withaMAPEof3.41%.
Incomparison,SARIMAhadthehighesterrorat6.17%,whileTBATSandHolt-Winters
performedmoderatelywellwithMAPEvaluesof3.77%and4.09%,respectively. Thestudy
highlightsthateconomiccrises,particularlyin2001,2009,and2020,significantlyimpacted
electricityconsumptionpatterns. AI-basedmodels,particularlyMLP,demonstratedsupe-
riorcapabilityincapturingnonlineartrendsandseasonalvariations. Thefindingssuggest
thatwhiletraditionalmodelsremainusefulforshort-termforecasting,neuralnetworks
providemorerobustlong-termpredictions.
Thearticle[63]focusesonlong-termelectricityconsumptionforecastinginIndonesia
usingANNs. ThestudyaimstocomparetheaccuracyofANN-basedpredictionswith
officialgovernmentforecastsfromRUPTL(ElectricitySupplyBusinessPlan),developedby
Indonesia’sMinistryofEnergyandMineralResources. TheANN-basedforecastingmodel
was compared with traditional forecasting methods, including exponential smoothing,
ARIMA,andlinearregression. Thestudyutilizedhistoricalelectricityconsumptiondata
from2000to2018,incorporatingkeyvariablessuchasGDP,population,andthenumberof
PLNelectricitycustomers. TheresultsshowedthatANNsachievedhighaccuracyintrain-
ing,withaminimalMSE=0.019560comparedtoexponentialsmoothingMSE=24.04682.
However,forecastsfor2019–2025showedsignificantdeviationsfromofficialRUPTLpro-
jections. TheANNmodelpredictedelectricityconsumptionof249.34TWhin2025,while
RUPTLestimated360.93TWh. Thisdiscrepancyisprimarilyduetothelimitednumber
ofinputvariablesintheANNmodel,asRUPTLincorporatesadditionaleconomicfactors
suchasinflation,electrificationrates,andenergyprices. Inconclusion,ArtificialNeural

Energies2025,18,4032 21of27
Networksprovedhighlyeffectiveinmodelinghistoricalelectricityconsumption,buttheir
applicationforlong-termforecastingrequiresincorporatingadditionaleconomicvariables.
Thearticle[56]exploreslong-termelectricityconsumptionforecastingforbothde-
velopinganddevelopedeconomies, focusingonIranandtheUnitedStates. Thestudy
appliesANNoptimizedusingImprovedParticleSwarmOptimization(IPSO)toenhance
forecastingaccuracy. Themodeluseshistoricaldatafrom1967to2009andpredictsenergy
consumptiontrendsfrom2010to2030,incorporatingeconomicanddemographicindicators
suchasGDP,energyimportsandexports,andpopulation. TheresultsindicatethatANN
modelsoptimizedwithIPSOoutperformtraditionalregressionmodels,achievingMAPE
valuesof1.94%forIranand1.51%fortheUnitedStates,significantlyimprovingpredictive
accuracy. The study finds that economic indicators provide better forecasting accuracy
thanrelyingsolelyonhistoricalenergyconsumptiondata. TheforecastsshowthatIran’s
energyconsumptionwillincrease2.73timesby2030,whereastheUSwillexperiencea
muchslowergrowthrateofapproximately1.09%annuallyduetoeffectivedemand-side
management(DSM)policies. TheIPSOalgorithmenhancesclassicalPSObyintroducing
mutationoperatorsthatpreventprematureconvergenceandimproveglobalsearchcapa-
bilities. ThefindingssuggestthatAI-basedforecastingmodels,particularlyIPSO-ANN,
provide a reliable tool for long-term energy planning, particularly when incorporating
macroeconomicvariables.
Thearticle[64]exploresadeep-learningapproachforelectricityconsumptionfore-
casting,focusingoncapturingbothshort-termandlong-termtemporaldependenciesin
time-seriesdata. TraditionalmethodslikeARIMAandGaussianProcessesoftenstruggle
withmodelingmulti-scalepatterns,leadingtosuboptimalforecastingaccuracy. Toaddress
thisissue,theauthorsproposeLong-andShort-termTime-seriesNetwork(LSTNet),adeep
neuralnetworkarchitecturedesignedtohandlecomplextemporaldependenciesinenergy
consumptiondata. LSTNetintegratesCNNstoextractshort-termlocalpatterns,RNNsto
modellong-termdependencies,andanmARcomponentstoenhancepredictionstability.
Themodelisevaluatedonreal-worlddatasetsofelectricityconsumption,demonstrating
its superiority over classical statistical models and standard deep-learning approaches
like LSTM and GRU. The results show that LSTNet significantly improves long-term
forecastingaccuracybyeffectivelycapturingperiodictrendsandexternalinfluenceson
energy demand. The article presents a novel approach to probabilistic individual load
forecastingusinganLSTMnetworkguidedbythePinballLossfunction. Unliketraditional
load forecasting methods that focus on aggregated demand, the increasing availability
ofsmartmeterdataenablesmoreaccuratemodelingofindividualenergyconsumption
patterns. Oneofthemainchallengesinindividualloadforecastingisthestochasticand
non-stationarynatureofenergyconsumption,whichlimitstheeffectivenessofclassical
methodssuchasARIMA,linearregression,andSVR.Toaddressthis,thestudyproposes
anLSTM-basedmodelcapableofcapturingbothshort-termfluctuationsandlong-term
dependenciesintime-seriesdata. Insteadofprovidingpointestimates,themodelgenerates
quantileforecasts,allowingamorecomprehensiverepresentationofuncertaintyinenergy
demandpredictions. Themaincontributionsofthisresearchincludetheintegrationof
LSTMwithPinballLoss,whichestimatesanentiredistributionoffuturedemandrather
thanasinglepredictedvalue,andthedevelopmentofamulti-outputquantilemodel,which
enablesthesimultaneousforecastingofmultiplequantileswithlowercomputationalcost.
Thestudycomparestheproposedmodelagainstotherprobabilisticforecastingtechniques,
including QRNN, Quantile Gradient Boosting Regression Tree (QGBRT), and standard
LSTMwitherrorestimation. ExperimentswereconductedusingtheSmartMeteringElec-
tricity Customer Behavior Trials (CBTs) dataset from Ireland, covering both individual
consumersandsmallandmediumenterprises(SMEs). TheresultsindicatethatPinball

Energies2025,18,4032
22of27
LossGuidedLSTMachievedthelowestforecasterroramongalltestedmodels,improv-
ingaccuracyby2.19%to7.52%forindividualconsumersand3.79%to25.80%forSMEs.
Thestudyalsohighlightsthatforecastingerrorsarehighestduringmorningandevening
peakhours,particularlybetween7:00–8:00and17:30–22:00forresidentialconsumers,and
9:30–20:00forSMEs,confirmingthatenergyusageismostvolatileduringtheseperiods.
The findings suggest that quantile-based forecasting is essential for managing demand
uncertaintyandoptimizingenergydistributionstrategies,makingthismethodparticularly
valuablefordemandresponseprograms,smarttariffs,andenergystorageoptimizationin
residentialandcommercialsectors. Table4providesasummaryoftheforecastingmethods
forlong-termelectricityconsumption,asdiscussedinthissection.
Table4.Summaryoflong-termloadforecastingconsumptionmethods.
| Forecasting | Authors/ |           | Model/    | Forecast | Accuracy  |            | Disadvantages/ |
| ----------- | -------- | --------- | --------- | -------- | --------- | ---------- | -------------- |
| No.         |          | InputData |           |          |           | Advantages |                |
| Method      | Source   |           | Algorithm | Horizon  | (Metrics) |            | Limitations    |
Historical
|             |            |                 | Hierarchical |           | Qualitative   |              |                  |
| ----------- | ---------- | --------------- | ------------ | --------- | ------------- | ------------ | ---------------- |
|             |            | consumptionof   |              |           |               | Captures     |                  |
|             |            |                 | Linear       |           | matchto       |              | Complex,         |
| Bottom-up   | F.L.C.da   | Brazilianpulp   |              |           |               | uncertainty, |                  |
|             |            |                 | Model+       |           | actual        |              | requiresdetailed |
| 1 Bayesian  | Silvaetal. | andpaper        |              | 2015–2050 |               | detailed     |                  |
|             |            |                 | Bayesian     |           | 2008–2014;    |              | sector-specific  |
| forecasting | (2019)[58] | industry,energy |              |           |               | sectoral     |                  |
|             |            |                 | Inference    |           | probabilistic |              | data             |
|             |            | efficiency      |              |           |               | modeling     |                  |
|             |            |                 | (MCMC)       |           | forecasts     |              |                  |
scenarios
Multiple
Linear
Weather,
|             |            |               | Regression+ |             |         |                | Limitedto       |
| ----------- | ---------- | ------------- | ----------- | ----------- | ------- | -------------- | --------------- |
| Regression- |            | calendardata, |             |             |         | Simple,        |                 |
|             | G.-C.Lee   |               | Ensemble    | 24months    |         |                | mid-term,relies |
| 2 based     |            | industrial    |             |             | MAPE≈2% | interpretable, |                 |
|             | (2024)[59] |               | comparison  | (2022–2023) |         |                | onexternaldata  |
| method      |            | activity      |             |             |         | highaccuracy   |                 |
|             |            |               | withML      |             |         |                | accuracy        |
(SouthKorea)
(LightGBM,
LSTM)
|       |     | Annual      |              |     | ARIMA      |          |             |
| ----- | --- | ----------- | ------------ | --- | ---------- | -------- | ----------- |
|       |     |             | ARIMA(1,1,0) |     |            | Goodwith | GM(1,1)less |
| ARIMA |     | electricity |              |     | betterthan |          |             |
3 and R.Kadrietal. consumptionin andGrey Multi-decade GM(1,1) limiteddata accurate,
|           | (2023)[60] |                | Model        | (1982–2020) |              | (GM),ARIMA    | sensitivetodata |
| --------- | ---------- | -------------- | ------------ | ----------- | ------------ | ------------- | --------------- |
| GM(1,1)   |            | Algeria        |              |             | (lower       |               |                 |
|           |            |                | GM(1,1)      |             |              | robust        | volatility      |
|           |            | (1982–2020)    |              |             | MAPE)        |               |                 |
| Optimized |            | GFECandRES     |              |             | APE&         |               |                 |
|           |            |                | OFANGBM(1,1) |             |              | Handlessmall  | Limitedto       |
| Grey      | U.S¸ahin   | data(France,   |              |             | comparison   |               |                 |
| 4         |            |                | withGA       | 2020–2030   |              | datasets,     | specificRES     |
| Bernoulli | (2021)[61] | Germany,Italy, |              |             | withnational |               |                 |
|           |            |                | optimization |             |              | interpretable | context         |
| Model     |            | etc.)          |              |             | targets      |               |                 |
|           |            | GDP,           | Co-          |             | Deviation    |               |                 |
Linear V.Bianco GDP/capita, integrated Long-term from Simple, Lowprecisionin
|              |             | population, | and        |                | national   | consistentwith |           |
| ------------ | ----------- | ----------- | ---------- | -------------- | ---------- | -------------- | --------- |
| 5 Regression | etal.(2009) |             |            | projectionfrom |            |                | extreme   |
|              |             | electricity | stationary |                | forecasts: | national       |           |
| (Italy)      | [62]        |             |            | historicaldata |            |                | scenarios |
|              |             | consumption | regression |                | −1%to      | forecasts      |           |
|              |             | (1970–2007) | models     |                | −11%       |                |           |
| Artificial   |             |             |            |                | Betterthan |                |           |
R.
| Neural |           | GDP,population, | Artificial |     | government | Highaccuracy |                  |
| ------ | --------- | --------------- | ---------- | --- | ---------- | ------------ | ---------------- |
|        | Adhiswara |                 |            |     |            |              | Black-boxnature, |
6 Network electrification Neural 2019–2025 SimpleE fornonlinear
|          | etal.(2019) |       |         |     |       |        | data-intensive |
| -------- | ----------- | ----- | ------- | --- | ----- | ------ | -------------- |
| (Indone- |             | ratio | Network |     | model | trends |                |
[63]
| sia) |     |     |     |     | (qualitative) |     |     |
| ---- | --- | --- | --- | --- | ------------- | --- | --- |
Regression F.J.Ardakani, GDP,energy IPSO- Cross-country Complexity
MAPE:
| andANN | M.M.     | imports/exports, | optimized |           |              | comparison, | requires       |
| ------ | -------- | ---------------- | --------- | --------- | ------------ | ----------- | -------------- |
| 7      |          |                  |           | 2010–2030 | 1.94%(Iran), |             |                |
| (Iran, | Ardehali | population       | ANNvs.    |           |              | optimized   | socio-economic |
1.51%(USA)
| USA)          | (2014)[57]  | (1967–2009)     | regression  |               |             | models       | data            |
| ------------- | ----------- | --------------- | ----------- | ------------- | ----------- | ------------ | --------------- |
|               |             |                 | LSTM        |               | Betterthan  | Handles      | Requires        |
|               |             | Smartmeterdata  |             | Short-to-mid- |             |              |                 |
|               |             |                 | guidedby    |               | traditional | uncertainty, | high-resolution |
| Probabilistic | YiWangetal. | (Ireland),      |             | term,         |             |              |                 |
| 8             |             |                 | pinballloss |               | andLSTM     | workson      | smartdata,      |
| LSTM          | (2019)[64]  | residentialand  |             | high-         |             |              |                 |
|               |             |                 | (quantile   |               | baseline    | individual   | computation-    |
|               |             | commercialloads |             | resolution    |             |              |                 |
|               |             |                 | regression) |               | models      | level        | heavy           |

Energies2025,18,4032 23of27
3.5. ProblemsofSelectingForecastingMethodsintheContextofDataVariation: Reviewand
Recommendations
Theliteratureonelectricityforecastinganalyzesdataofvaryingaggregationlevels,
rangingfromnationalaggregatestoindividualsmartmeterreadings. Methodselection
must account for both the temporal forecast horizon and the specific characteristics of
thedataset,includingitsstructure, resolution, andavailability. Consequently, keydata
categoriesnecessitatetheapplicationofdistinctapproaches,whichwecanseeinTable5.
Table5.Mappingofforecastingmethodstodatatypesandapplications.
DataClassification CommonForecastingMethods TypicalApplications
ARIMA,SARIMA,ANN,Linear Strategicenergypolicyformulation,generation
National-scaleaggregateddemand
Regression,Prophet capacitydevelopment
HybridARIMA+ANNarchitectures,LSTM Electricitypricingstructures,localizedpower
Sector-specificconsumption
networks,FeedforwardNeuralNetworks, distributionmanagement,energy
(residential/commercial/utility)
Transformermodels demandprofiling
Consumerdemandoptimization,irregular
LSTMvariants,CNN-LSTMhybrids,Transformer
Individualsmartmetermeasurements consumptionidentification,intelligentnetwork
architectures,SparseAttentionmodels
regulation,P2Ptradingsystems
ARIMAformulations,GreySystemTheorymodels, Productionprocessefficiencyimprovements,
Industrialoperationaldata standardFeedforwardNeuralNetworks,Hybrid facility-levelloadpredictions,industrial
Grey-ANNmodels energyoptimization
Itiscrucialtorecognizethattheserecommendationsarenotdefinitiveandshouldbe
consideredinconjunctionwiththeuniqueattributesoftheforecastingtask,suchasdata
availability,forecastgranularity,andreal-timedemands. However,aclearcomprehension
ofthelinkbetweendatatypologyandmodelingapproachprovidesinvaluableguidance
forselectingoptimalforecastingmethodologiesacrossbothacademicresearchandpractical
operationalsettings.
4. Conclusions
Forecastingelectricityconsumptionisacriticalissuefortheeffectivemanagement
ofenergysystemsandinfrastructuredevelopmentplanning. Thisarticlereviewsawide
rangeofmethods—fromclassicalstatisticalmodels,suchasARIMA,toadvancedartificial
intelligencetechniques,includingdeep-learningmodels. Differentforecasttimehorizons
anddiversesourcesofinputdataweretakenintoaccount. Basedonthestudiesanalyzed,a
numberofconclusionscanbedrawnabouttheeffectivenessofthevariousapproaches,their
applications,andlimitations. Theseconclusionsprovideabasisforfurtherdiscussionof
thedirectionsofdevelopmentofforecastingmethodsinthecontextoftheenergytransition
andthegrowingshareofrenewableenergysources.
Thereviewedstudiesonveryshort-termelectricityloadforecastingindicatethatLSTM
modelsareparticularlyeffectiveinforecastinghousehold-levelelectricityconsumption,
especiallyinthepresenceofhighdatavolatility.Hybridmodels,suchasCNN-LSTM,allow
forthesimultaneouscaptureofbothlocalandglobalpatternsintime-seriesdata,leading
toimprovedforecastingaccuracy. Thefuzzylogic-basedapproach(IT-1FIS)canalsobe
effectiveforveryshort-termforecasts,providedthatinputdataisappropriatelyselected.
Theuseofadvancedhyperparameteroptimizationtechniques,suchastheCVOA,further
enhancespredictiveperformance.Inindustrialapplications,suchasopen-pitminingFFQR,
has proven to be highly effective in forecasting peak loads, supporting smarter energy
managementinthecontextofIndustry4.0strategies.
Thereviewedstudiesonshort-termloadforecastinghighlightthediversityandevo-
lutionofmodelingapproaches,rangingfromtraditionalstatisticalmethodslikeARIMA
andlinearregressiontomoreadvancedmachine-learninganddeep-learningmodels,such

Energies2025,18,4032 24of27
asANNs,LSTM,andhybridarchitectures. WhileARIMAproveseffectiveincapturing
seasonalityinstructuredtime-seriesdata,itslimitationsinhandlingnonlinearpatternsare
evident. ArtificialNeuralNetworksconsistentlyoutperformclassicalmodelsincomplex
environments,especiallyinbuildings,microgrids,andpeer-to-peersystems,duetotheir
abilitytomodeldynamicandnonlinearrelationships. Hybridandensemblemodels,par-
ticularlythosecombiningCNNsandLSTMsorintegratingstatisticalandmachine-learning
techniques,demonstratesuperiorforecastingaccuracyandrobustness,especiallyinthe
presenceofmultipleinputvariableslikeweatherdata. Overall,theresultsconfirmthat
whilesimplermodelsremainusefulforbaselinecomparisonsandinterpretableapplica-
tions,deep-learning-basedsolutionsofferthehighestaccuracyandadaptabilityformodern
short-termelectricityconsumptionforecastingchallenges.
Conclusionsarisingfrommedium-termloadforecasting,coveringperiodsfromsev-
eralmonthstoafewyears,emphasizetherelevanceofbothtraditionalandmodernfore-
castingtechniquesforstrategicenergyplanning. ARIMAmodels,duetotheirsimplicity
andeffectivenessforstationarytimeseries,performedwellinforecastingenergyconsump-
tion, particularly in scenarios with stable historical trends and limited external shocks.
However,inmoredynamicenvironmentsorwhenexternalfactorslikeeconomiccrises
affectconsumptionpatterns,machine-learningmodels—especiallyANNs—demonstrated
superiorflexibilityandaccuracy,particularlywhenenhancedwithrelevantinputvariables
suchasexports,population,orGDP.Hybridapproaches,combiningstatisticalmethods
withANNsorGreyModels,showedmeasurableimprovementsinpredictiveperformance,
asobservedinSlovakiaandTürkiye. Inindustrialsettings,ARIMAcontinuedtoprove
effective, especially in enterprises with continuous production processes. Studies em-
ployingensembledeep-learningarchitectures(e.g.,LSTM+GRU+TCN)oroptimization
algorithmslikegeneticalgorithmsdemonstratedthatmodeltuningandfeatureselection
significantlyimpactforecastaccuracyandstabilityovermulti-monthperiods. Additionally,
methodssuchasGrey-MarkovmodelsandSingularSpectrumAnalysisofferedreliable
resultsforlong-rangeforecastinginrapidlydevelopingeconomieslikeIndia,particularly
whendatavolumeorqualitywaslimited. Overall,theresultsindicatethatwhileclassical
modelsremainusefulasbaselinesorforspecificapplications,hybridanddeep-learning
modelsoffersuperiorperformanceformedium-termelectricityforecasting,providedthey
arecarefullycalibratedandcontextualizedtotheapplicationenvironment.
Areviewofresearchonlong-termloadforecastingshowsthatthereisnoone-size-fits-
allmodel,butthebestresultsareachievedbymethodstailoredtothespecificdatacontext
andforecastgoal. ARIMAmodelsremaineffectivewithstable,lineartimeseries,especially
with limited availability of external variables. Regression models perform well when
reliabledataoneconomicfactors(e.g.,GDP,population,industrialactivity)areavailable,
offeringhighaccuracyandinterpretability. Neuralnetworks,ontheotherhand,especially
ANNs and LSTMs, provide better representation of nonlinear trends and responses to
disturbingfactors(e.g., crises, pandemic), especiallyafteroptimizinghyperparameters.
Hybridmodels(e.g.,SARIMA-ANN,CNN-LSTM,regression+LSTM),whichcombinethe
simplicityofstatisticalmodelswiththeflexibilityofmachinelearning,andprobabilistic
models,whichofferadistributionofpossiblevaluesinsteadofasingleforecast,perform
best,supportingriskmanagement. Inpractice,itisworthwhiletouseamixedapproach,in
whichclassicalmodelsactasareference,andstrategicforecastsarebasedonAImodels
supportedbyanalysisofeconomicvariablesanddevelopmentscenarios.
Whenchoosingforecastingmodels, asignificantlimitationistheirdependenceon
externalvariablesliketemperature,economicindicators,orcalendareffects. Whilethese
variablesoftenboostretrospective(expost)accuracy,theiruseinreal-time(exante)forecast-
ingischallengingduetouncertaintyorunavailability. Predictingvariablessuchasaverage

Energies2025,18,4032 25of27
monthlytemperatureorGDPaccuratelyenoughforshort-termoperationalmodelscanbe
particularlydifficult. Therefore,manypracticalforecastingsystemsemployhybriddesigns
that blend autoregressive elements with restricted exogenous data, or they use lagged
proxiesforuncertaininputs. Recognizingthisinherenttrade-offiscrucialfordeveloping
reliable,deployableforecastingsystems.
Thisarticleprovidesacomprehensiveandstructuredreviewofelectricityloadforecast-
ingmethodsacrossdifferenttimehorizons,rangingfromveryshorttermtolongterm. By
systematicallycomparingtraditionalstatisticaltechniqueswithmodernmachine-learning
anddeep-learningapproaches,thearticlehighlightstheirrespectivestrengths,limitations,
and suitability in various forecasting contexts. A key contribution of this work is the
synthesis of findings across multiple application domains—residential, industrial, and
nationalenergysystems—showinghowthechoiceofforecastingmodelshouldalignwith
dataavailability,volatility,andstrategicplanningneeds. Moreover,thearticleemphasizes
the growing importance of hybrid and probabilistic models, offering practical insights
intomodelselectionandoptimizationstrategies. Thisreviewsupportsresearchers,energy
planners, and decision-makers in identifying effective forecasting solutions, especially
inthecontextofincreasingenergysystemcomplexityandtheintegrationofrenewable
energysources.
AuthorContributions:Conceptualization,K.M.,T.O.,andJ.Z.;methodology,K.M.,T.O.,andJ.Z.;
software,K.M.,T.O.,andJ.Z.;validation,K.M.,T.O.,andJ.Z.;formalanalysis,K.M.,T.O.,andJ.Z.;
investigation,K.M.,T.O.,andJ.Z.;resources,K.M.,T.O.,andJ.Z.;datacuration,K.M.,T.O.,andJ.Z.;
writing—originaldraftpreparation,K.M.,T.O.,andJ.Z.;writing—reviewandediting,K.M.,T.O.,
andJ.Z.;visualization,K.M.,T.O.,andJ.Z.;supervision,K.M.,T.O.,andJ.Z.;projectadministration,
K.M.,T.O.,andJ.Z.;fundingacquisition,K.M.,T.O.,andJ.Z.Allauthorshavereadandagreedtothe
publishedversionofthemanuscript.
Funding: ThisworkreceivedfinancialsupportfromthefundingofAGHUniversityofKrakow,
FacultyofEnergyandFuels(grantnumber16.16.210.476).
DataAvailabilityStatement:Nodatasetsweregeneratedoranalyzedduringthecurrentstudy.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.
References
1. MinisterstwoKlimatuiS´rodowiska.PolitykaEnergetycznaPolskido2040r.2021.Availableonline:https://www.gov.pl/web/
klimat/polityka-energetyczna-polski(accessedon25April2025).
2. Waheed,W.;Xu,Q.TheCOVID-19pandemic’simpactonuserconsumption: Ashifttowardsveryefficientloadforecasting.
Sustain.EnergyGridsNetw.2024,39,101426.[CrossRef]
3. Khan,N.;Haq,I.U.;Khan,S.U.;Rho,S.;Lee,M.Y.;Baik,S.W.DB-Net:AnoveldilatedCNNbasedmulti-stepforecastingmodel
forpowerconsumptioninintegratedlocalenergysystems.Int.J.Electr.PowerEnergySyst.2021,133,107023.[CrossRef]
4. PSE.Raport2022KSEZestawienieDanychIlos´ciowychDotycza˛cychFunkcjonowaniaksew2022Roku;PSE:Warszawa,Poland,2022.
Availableonline:https://www.pse.pl/dane-systemowe/funkcjonowanie-kse/raporty-roczne-z-funkcjonowania-kse-za-rok/
raporty-za-rok-2022(accessedon14February2025).
5. Singh,P.;Dwivedi,P.;Kant,V.Ahybridmethodbasedonneuralnetworkandimprovedenvironmentaladaptationmethodusing
ControlledGaussianMutationwithrealparameterforshort-termloadforecasting.Energy2019,174,460–477.[CrossRef]
6. Ritchie,H.;Roser,M.EnergyProductionandConsumption.OurWorldinData.Availableonline:https://ourworldindata.org/
energy-production-consumption(accessedon17July2025).
7. LeiteCoelhoDaSilva,F.; DaCosta,K.; CanasRodrigues,P.; Salas,R.; López-Gonzales,J.L.StatisticalandArtificialNeural
NetworksModelsforElectricityConsumptionForecastingintheBrazilianIndustrialSector.Energies2022,15,588.[CrossRef]
8. Krstev,S.;Forcan,J.;Krneta,D.AnOverviewofForecastingMethodsforMonthlyElectricityConsumption.Teh.Vjesn.Tech.Gaz.
2023,30,993–1001.[CrossRef]
9. Azeem,A.;Ismail,I.;Jameel,S.M.;Harindran,V.R.ElectricalLoadForecastingModelsforDifferentGenerationModalities:A
Review.IEEEAccess2021,9,142239–142263.[CrossRef]

Energies2025,18,4032 26of27
10. Kaytez,F.;Taplamacioglu,M.C.;Cam,E.;Hardalac,F.Forecastingelectricityconsumption:Acomparisonofregressionanalysis,
neuralnetworksandleastsquaressupportvectormachines.Int.J.Electr.PowerEnergySyst.2015,67,431–438.[CrossRef]
11. Zang,H.;Xu,R.;Cheng,L.;Ding,T.;Liu,L.;Wei,Z.;Sun,G.ResidentialloadforecastingbasedonLSTMfusingself-attention
mechanismwithpooling.Energy2021,229,120682.[CrossRef]
12. Galicia,A.;Talavera-Llames,R.;Troncoso,A.;Koprinska,I.;Martínez-Álvarez,F.Multi-stepforecastingforbigdatatimeseries
basedonensemblelearning.Knowl.BasedSyst.2019,163,830–841.[CrossRef]
13. Klyuev, R.V.; Morgoev, I.D.; Morgoeva, A.D.; Gavrina, O.A.; Martyushev, N.V.; Efremenkov, E.A.; Mengxu, Q.Methodsof
ForecastingElectricEnergyConsumption:ALiteratureReview.Energies2022,15,8919.[CrossRef]
14. Ediger, V.S¸.; Akar, S. ARIMA forecasting of primary energy demand by fuel in Turkey. Energy Policy 2007, 35, 1701–1708.
[CrossRef]
15. Shumway,R.H.; Stoffer,D.S.TimeSeriesAnalysisandItsApplications: WithRExamples; SpringerTextsinStatistics; Springer
InternationalPublishing:Cham,Switzerland,2017;ISBN978-3-319-52451-1.
16. Holt,C.C.Forecastingseasonalsandtrendsbyexponentiallyweightedmovingaverages.Int.J.Forecast.2004,20,5–10.[CrossRef]
17. Hawkins,D.M.OntheInvestigationofAlternativeRegressionsbyPrincipalComponentAnalysis. Appl. Stat. 1973,22,275.
[CrossRef]
18. Zhang,Y.;Ma,R.;Liu,J.;Liu,X.;Petrosian,O.;Krinkin,K.ComparisonandExplanationofForecastingAlgorithmsforEnergy
TimeSeries.Mathematics2021,9,2794.[CrossRef]
19. Ahmad,T.;Zhang,H.;Yan,B.Areviewonrenewableenergyandelectricityrequirementforecastingmodelsforsmartgridand
buildings.Sustain.CitiesSoc.2020,55,102052.[CrossRef]
20. Qiu,X.;Zhang,L.;Ren,Y.;Suganthan,P.;Amaratunga,G.Ensembledeeplearningforregressionandtimeseriesforecasting.In
Proceedingsofthe2014IEEESymposiumonComputationalIntelligenceinEnsembleLearning(CIEL),Orlando,FL,USA,9–12
December2014;IEEE:Orlando,FL,USA,2014;pp.1–6.
21. Bedi,J.;Toshniwal,D.Deeplearningframeworktoforecastelectricitydemand.Appl.Energy2019,238,1312–1326.[CrossRef]
22. Jamaaluddin;Robandi,I.;Anshory,I.TimeDifferenceCalculationSettingsforVeryShortTermElectricLoadForecastingUsing
IntervalType-1FuzzyInferenceSystem(IT-1FIS).IOPConf.Ser.Mater.Sci.Eng.2020,874,012011.[CrossRef]
23. Kong,W.;Dong,Z.Y.;Jia,Y.;Hill,D.J.;Xu,Y.;Zhang,Y.Short-TermResidentialLoadForecastingBasedonLSTMRecurrent
NeuralNetwork.IEEETrans.SmartGrid2019,10,841–851.[CrossRef]
24. Zhou,X.;Lin,W.;Kumar,R.;Cui,P.;Ma,Z.Adata-drivenstrategyusinglongshorttermmemorymodelsandreinforcement
learningtopredictbuildingelectricityconsumption.Appl.Energy2022,306,118078.[CrossRef]
25. Kim,T.-Y.;Cho,S.-B.PredictingresidentialenergyconsumptionusingCNN-LSTMneuralnetworks.Energy2019,182,72–81.
[CrossRef]
26. Torres,J.F.;Martínez-Álvarez,F.;Troncoso,A.AdeepLSTMnetworkfortheSpanishelectricityconsumptionforecasting.Neural
Comput.Appl.2022,34,10533–10545.[CrossRef][PubMed]
27. Laayati,O.;Bouzi,M.;Chebak,A.SmartEnergyManagementSystem:DesignofaMonitoringandPeakLoadForecastingSystem
foranExperimentalOpen-PitMine.Appl.Syst.Innov.2022,5,18.[CrossRef]
28. Zahid,M.;Chen,Y.;Jamal,A.;Mamadou,C.Z.FreewayShort-TermTravelSpeedPredictionBasedonDataCollectionTime-
Horizons:AFastForestQuantileRegressionApproach.Sustainability2020,12,646.[CrossRef]
29. Carvalho,A.;Chouchene,A.;Lima,T.;Charrua-Santos,F.CognitiveManufacturinginIndustry4.0towardCognitiveLoad
Reduction:AConceptualFramework.Appl.Syst.Innov.2020,3,55.[CrossRef]
30. Mahmood,A.M.;AbdulZahra,M.M.;Hamed,W.;Bashar,B.S.;Abdulaal,A.H.;Alawsi,T.;Adhab,A.H.ElectricityDemand
PredictionbyaTransformer-BasedModel.MajlesiJ.Electr.Eng.2022,16,97.
31. Chan,J.W.;Yeo,C.K.ATransformerbasedapproachtoelectricityloadforecasting.Electr.J.2024,37,107370.[CrossRef]
32. Agga,A.;Abbou,A.;Labbadi,M.;ElHoum,Y.Short-termselfconsumptionPVplantpowerproductionforecastsbasedon
hybridCNN-LSTM,ConvLSTMmodels.Renew.Energy2021,177,101–112.[CrossRef]
33. Hyndman,R.J.;Athanasopoulos,G.Forecasting:PrinciplesandPractice;OTexts:Melbourne,Australia,2018.
34. Hernández,L.;Baladrón,C.;Aguiar,J.;Calavia,L.;Carro,B.;Sánchez-Esguevillas,A.;Pérez,F.;Fernández,Á.;Lloret,J.Artificial
NeuralNetworkforShort-TermLoadForecastinginDistributionSystems.Energies2014,7,1576–1598.[CrossRef]
35. Sajjad,M.;Khan,Z.A.;Ullah,A.;Hussain,T.;Ullah,W.;Lee,M.Y.;Baik,S.W.ANovelCNN-GRU-BasedHybridApproachfor
Short-TermResidentialLoadForecasting.IEEEAccess2020,8,143759–143768.[CrossRef]
36. Lee,Y.W.;Tay,K.G.;Choy,Y.Y.ForecastingElectricityConsumptionUsingTimeSeriesModel.Int.J.Eng.Technol.2018,7,218–223.
[CrossRef]
37. Grant,J.;Eltoukhy,M.;Asfour,S.Short-TermElectricalPeakDemandForecastinginaLargeGovernmentBuildingUsingArtificial
NeuralNetworks.Energies2014,7,1935–1953.[CrossRef]
38. Hadjout,D.;Torres,J.F.;Troncoso,A.;Sebaa,A.;Martínez-Álvarez,F.Electricityconsumptionforecastingbasedonensemble
deeplearningwithapplicationtotheAlgerianmarket.Energy2022,243,123060.[CrossRef]

Energies2025,18,4032 27of27
39. GonzálezGrandón,T.;Schwenzer,J.;Steens,T.;Breuing,J.Electricitydemandforecastingwithhybridclassicalstatisticaland
machinelearningalgorithms:CasestudyofUkraine.Appl.Energy2024,355,122249.[CrossRef]
40. Mustaqeem;Ishaq,M.;Kwon,S.Short-TermEnergyForecastingFrameworkUsinganEnsembleDeepLearningApproach.IEEE
Access2021,9,94262–94271.[CrossRef]
41. Goude,Y.;Nedellec,R.;Kong,N.LocalShortandMiddleTermElectricityLoadForecastingWithSemi-ParametricAdditive
Models.IEEETrans.SmartGrid2014,5,440–446.[CrossRef]
42. Abu-Salih, B.; Wongthongtham, P.; Morrison, G.; Coutinho, K.; Al-Okaily, M.; Huneiti, A. Short-term renewable energy
consumptionandgenerationforecasting:AcasestudyofWesternAustralia.Heliyon2022,8,e09152.[CrossRef]
43. L’Heureux,A.;Grolinger,K.;Capretz,M.A.M.Transformer-BasedModelforElectricalLoadForecasting.Energies2022,15,4993.
[CrossRef]
44. Koohfar,S.;Woldemariam,W.;Kumar,A.PredictionofElectricVehiclesChargingDemand:ATransformer-BasedDeepLearning
Approach.Sustainability2023,15,2105.[CrossRef]
45. GalindoPadilha,G.A.;Ko,J.;Jung,J.J.;DeMattosNeto,P.S.G.Transformer-BasedHybridForecastingModelforMultivariate
RenewableEnergy.Appl.Sci.2022,12,10985.[CrossRef]
46. Chuang,F.-K.;Hung,C.-Y.;Chang,C.-Y.;Kuo,K.-C.DeployingArimaandArtificialNeuralNetworksModelstoPredictEnergy
ConsumptioninTaiwan.Sens.Lett.2013,11,2333–2340.[CrossRef]
47. Meade,N.Industrialandbusinessforecastingmethods,Lewis,C.D.,BoroughGreen,Sevenoaks,Kent:Butterworth,1982.Price:
£9.25.Pages:144.J.Forecast.1983,2,194–196.[CrossRef]
48. Zhang,M.;Zhang,S.;Lee,C.-C.;Zhou,D.EffectsoftradeopennessonrenewableenergyconsumptioninOECDcountries:New
insightsfrompanelsmoothtransitionregressionmodelling.EnergyEcon.2021,104,105649.[CrossRef]
49. Pavlicko,M.;Vojteková,M.;Blažeková,O.ForecastingofElectricalEnergyConsumptioninSlovakia.Mathematics2022,10,577.
[CrossRef]
50. Rakhmonov,I.U.;Niyozov,N.N.;Kurbonov,N.N.;Umarov,B.S.Forecastingofelectricityconsumptionbyindustrialenterprises
withacontinuousnatureofproduction.E3SWebConf.2023,384,01030.[CrossRef]
51. Çag˘layan-Akay,E.;Topal,K.H.ForecastingTurkishelectricityconsumption: Acriticalanalysisofsingleandhybridmodels.
Energy2024,305,132115.[CrossRef]
52. Zhang, G.P. Time series forecasting using a hybrid ARIMA and neural network model. Neurocomputing 2003, 50, 159–175.
[CrossRef]
53. Khashei,M.;Bijari,M.AnovelhybridizationofartificialneuralnetworksandARIMAmodelsfortimeseriesforecasting.Appl.
SoftComput.2011,11,2664–2675.[CrossRef]
54. Wang,L.;Zou,H.;Su,J.;Li,L.;Chaudhry,S.AnARIMA-ANNHybridModelforTimeSeriesForecasting.Syst.Res.Behav.Sci.
2013,30,244–259.[CrossRef]
55. Bouktif,S.;Fiaz,A.;Ouni,A.;Serhani,M.OptimalDeepLearningLSTMModelforElectricLoadForecastingusingFeature
SelectionandGeneticAlgorithm:ComparisonwithMachineLearningApproaches.Energies2018,11,1636.[CrossRef]
56. Kumar,U.;Jain,V.K.Timeseriesmodels(Grey-Markov,GreyModelwithrollingmechanismandsingularspectrumanalysis)to
forecastenergyconsumptioninIndia.Energy2010,35,1709–1716.[CrossRef]
57. Ardakani,F.J.;Ardehali,M.M.Long-termelectricalenergyconsumptionforecastingfordevelopinganddevelopedeconomies
basedondifferentoptimizedmodelsandhistoricaldatatypes.Energy2014,65,452–461.[CrossRef]
58. Da Silva, F.L.C.; Cyrino Oliveira, F.L.; Souza, R.C. A bottom-up bayesian extension for long term electricity consumption
forecasting.Energy2019,167,198–210.[CrossRef]
59. Lee,G.-C.ARegression-BasedMethodforMonthlyElectricLoadForecastinginSouthKorea.Energies2024,17,5860.[CrossRef]
60. Kadri,R.;Kahoui,H.;Sahed,A.ElectricityConsumptionForecastinginAlgeria:AComparisonofARIMAandGM(1,1)Models.
Glob.Bus.2023,8,15–24.[CrossRef]
61. S¸ahin,U.FutureofrenewableenergyconsumptioninFrance,Germany,Italy,Spain,TurkeyandUKby2030usingoptimized
fractionalnonlineargreyBernoullimodel.Sustain.Prod.Consum.2021,25,1–14.[CrossRef][PubMed]
62. Bianco,V.;Manca,O.;Nardini,S.ElectricityconsumptionforecastinginItalyusinglinearregressionmodels.Energy2009,34,
1413–1421.[CrossRef]
63. Adhiswara,R.;Abdullah,A.G.;Mulyadi,Y.Long-termelectricalconsumptionforecastingusingArtificialNeuralNetwork(ANN).
J.Phys.Conf.Ser.2019,1402,033081.[CrossRef]
64. Wang,Y.;Gan,D.;Sun,M.;Zhang,N.;Lu,Z.;Kang,C.ProbabilisticindividualloadforecastingusingpinballlossguidedLSTM.
Appl.Energy2019,235,10–20.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.