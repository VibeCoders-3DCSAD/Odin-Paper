future internet
Review
A Review of ARIMA vs. Machine Learning Approaches for
Time Series Forecasting in Data Driven Networks
VaiaI.Kontopoulou1 ,AthanasiosD.Panagopoulos2,* ,IoannisKakkos1 andGeorgeK.Matsopoulos1
1 BiomedicalEngineeringLaboratory,SchoolofElectricalandComputerEngineering,NationalTechnical
UniversityofAthens,15780Athens,Greece;vaiakontop@biomed.ntua.gr(V.I.K.);
ikakkos@biomed.ntua.gr(I.K.);gmatsopoulos@biomed.ntua.gr(G.K.M.)
2 SchoolofElectricalandComputerEngineering,NationalTechnicalUniversityofAthens,
15780Athens,Greece
* Correspondence:thpanag@ece.ntua.gr
Abstract:Inthebroadscientificfieldoftimeseriesforecasting,theARIMAmodelsandtheirvariants
havebeenwidelyappliedforhalfacenturynowduetotheirmathematicalsimplicityandflexibility
inapplication. However,withtherecentadvancesinthedevelopmentandefficientdeployment
ofartificialintelligencemodelsandtechniques,theviewisrapidlychanging,withashifttowards
machineanddeeplearningapproachesbecomingapparent,evenwithoutacompleteevaluation
ofthesuperiorityofthenewapproachovertheclassicstatisticalalgorithms.Ourworkconstitutes
anextensivereviewofthepublishedscientificliteratureregardingthecomparisonofARIMAand
machinelearningalgorithmsappliedtotimeseriesforecastingproblems,aswellasthecombination
ofthesetwoapproachesinhybridstatistical-AImodelsinawidevarietyofdataapplications(finance,
health,weather,utilities,andnetworktrafficprediction).OurreviewhasshownthattheAIalgorithms
displaybetterpredictionperformanceinmostapplications,withafewnotableexceptionsanalyzedin
ourDiscussionandConclusionssections,whilethehybridstatistical-AImodelssteadilyoutperform
theirindividualparts,utilizingthebestalgorithmicfeaturesofbothworlds.
Keywords: ARIMA;machinelearning;deeplearning;hybrid;networks;finance;health;weather;
MSE;RMSE;MAE;MAPE
Citation:Kontopoulou,V.I.;
Panagopoulos,A.D.;Kakkos,I.;
Matsopoulos,G.K.AReviewof
ARIMAvs.MachineLearning
1. Introduction
ApproachesforTimeSeries
ForecastinginDataDrivenNetworks. Inthecontextofacademicbibliography,thetoolsandmethodsofMachineandDeep
FutureInternet2023,15,255. Learningconstituteanalternativeapproachtostatisticalmethodsfortimeseriesforecasting.
https://doi.org/10.3390/fi15080255 However,theavailabledatawithregardtotheirrelativeperformanceintermsofaccuracy
andcomputationaldemandsislimited[1]. ArtificialIntelligence,whichisasupersetof
AcademicEditor:FilipePortela
machine and deep learning, has expanded during the last decade in multiple fields of
Received:13July2023 entrepreneurial and academic activity, with applications regarding the financial sector,
Revised: 27July2023 medical care, industry, retail, supply chain, utilities, and networks [2]. Nevertheless,
Accepted:28July2023 theclassicalapproachwithrespecttotheanalysisandforecastingoftimeseriesismostly
Published:30July2023
basedonintegratedautoregressivemovingaverage(ARIMA)models,andtheirvarious
versions [3]. Moreover, a core issue of the existing academic literature in the field of
machinelearningforecastingtechniquesisthefactthatthemajorityofpublicationspointto
adequateaccuracyvalues,withoutaproperfoundation,meaningwithoutapreestablished
Copyright: © 2023 by the authors.
comparisonwiththeresultsofsimplestatisticalmethodsandpredictionmodels[1].
Licensee MDPI, Basel, Switzerland.
Inthepresentstudy,wewillattemptareviewofARIMA,MachineLearning,andDeep
This article is an open access article
Learningtechniqueswithregardtotheirrelativeperformanceintimeseriesforecasting.
distributed under the terms and
The strategy behind our review is to present a selection of academic papers in which
conditionsoftheCreativeCommons
Attribution(CCBY)license(https:// the performance of machine learning, deep learning, and hybrid prediction models is
creativecommons.org/licenses/by/ comparedwiththeperformanceoftheARIMAorSARIMA(SeasonalARIMA)algorithms
4.0/). based on a variety of metrics. The results of these studies are presented in Tables 2–5.
FutureInternet2023,15,255.https://doi.org/10.3390/fi15080255 https://www.mdpi.com/journal/futureinternet

FutureInternet2023,15,255 2of31
The scientific works presented in this review consist of research in the financial sector
(withaspecialfocusontheapplicationofbitcoinpriceprediction), inthehealthsector
(withaspecialfocusontheapplicationsofpredictingparametersandvariablesrelatedto
thediseaseofCOVID-19),inthefieldofweatherforecasting(windspeed,drought,solar
energyproduction,etc.),inthefieldofutilityparametersforecasting(offeranddemandof
energy,waterconsumption,oilproduction,etc.),andinnetworkparametersprediction
(bothtransportationandwebnetworktrafficprediction).
1.1. DataDrivenNetworks
Thetitleofthepresentworkrefersto“datadrivennetworks”,fromthepointofviewof
dataandmodelsusedintimeseriesforecasting. Bigdatacollectionisofutmostimportance
tomodernforecastingapplications,especiallyforthetrainingofefficientmachinelearning
predictivemodels,duetothefactthattheproblemofforecastingincreasesincomplexityas
thevolumeanddimensionalityofavailabledatasourcesincrease. Inrecentapplications
andstudyfieldsregardingtimeseriesforecasting,thecollectionofdatareliesonlarge-scale
networksofsensorsanddatacollectionpointsduetothedistributednatureofthetarget
applications. Theanalysisandforecastsbasedonthesedatasetsarealsofedtolarge-scale
network applications (e.g., large-scale weather forecasts, health strategy planning on a
nationalandgloballevel,salesmanagementonaglobalscale,etc.).
Ontheotherhand,theterm“datadrivennetworks”alsoreferstothetrainingand
efficientdeploymentofthemodelsproposedfortimeseriesforecastingbythescientific
community. Especially in the case of machine learning models, whose application is
mostly data- and problem-agnostic, data availability in sufficient quantity is crucial to
successfulforecasting.
1.2. ScientificContributions
The present work attempts to address the existing gap in the scientific literature,
regarding an extensive summary/review of the studies comparing the application of
ARIMAandmachinelearningtechniquesintimeseriesforecastingapplications. Thisisthe
onlysuchreview,accordingtotheauthors’bestknowledge.
Ourworkcomparestimeseriesforecastingstudiesacrossmultipleapplicationsand
data sources, and it consists of mostly recent comparative studies published after 2018
(withtheexceptionoftheworksofZhangetal.[4]andNieetal.[5]). Duetothemultitude
ofdifferentdatasourcesandforecastingchallenges,weattemptamultilateral,sampled
viewoftheexistingliterature, presentingstudiesfromfivebasicdatacategories(finan-
cial,medical,weather,utilities,andnetworkcharacteristics). Fortheabovereasons,our
workconstitutesacontemporary,multifaced,reviewoftheexistingliteraturecomparing
theARIMAstatisticalapproachwithitsmachinelearningcounterparts. Ourstudyalso
summarizesthemainperformancemetricsofthealgorithmspresentedineachstudy,thus
enablinganintuitivereviewandcomparisonofthemethodsineachforecastingapplication.
Apracticalevaluation(Section5)ofthestudiesinwhichtheARIMAmodelsoutperform
theirmachinelearningcounterpartsresultsinanenumerationoftheapplication,dataset,
andmodel-dependentcharacteristicsthatdrivethechoiceoftheoptimalforecastingmodel
inanyparticularapplication.
1.3. RationaleandStructure
Therationalebehindthestructureofourreviewisbasedonorganizingthecollected
scientificliteraturefirstinrelationtothemachinelearningmodelbeingcomparedwith
ARIMAandsecondinrelationtothefieldofforecastingapplications. Inthatscope,thefirst
model category to be presented in detail is ARIMA, which is the center of our review,
andthenweorganizethemachinelearningapproachesbymodelcategory. Foreachofthe
categories,wepresentthetheoreticalbackground,andthenwedemonstratetherelevant
scientificliteratureorganizedbyapplicationcategory. Thesameprincipleappliestothe
categoryofhybridforecastingmodels,meaningthecombinationofARIMAandmachine

FutureInternet2023,15,255 3of31
learningalgorithms. Finally, weevaluatethereviewedscientificliteratureintotal, and
basedonthefindingthatmachinelearningmodelsoutperformtheARIMAapproachin
themajorityofforecastingapplications,weaimtouncovertheconditionsunderwhichwe
haveasuperiorARIMAforecastingresult.
Atthispoint,itisimportanttonotethatourworkdoesnotproposeanewtimeseries
forecastingmodel,butratherconstitutesanorganizedreviewofthepublishedscientific
literature comparing the ARIMA approach to different machine learning, and hybrid
prediction models. We consider this aspect of our work crucial to the feasibility of our
studybecauseweaimtocomparetheoptimizedARIMAandmachinelearningmodelson
thesamedatasets. Therefore,althoughthescientificliteratureapplyingindividualARIMA
ormachinelearningmodelstoforecastingproblemsisextensive,webaseourstudyonly
ontheexplicitcomparisonsofthethreecategoriesofmodels(ARIMA,machinelearning,
andhybrid).
The present work is organized as follows: The problem of time series forecasting,
which—alongwiththeARIMAtechnique—constitutesthecenterofourwork,ispresented
inSection2,alongwiththemorphologicalcharacteristicsofthetimeseriesthataffectthe
choiceoftheforecastingalgorithmandtheirrespectiveresults. Areviewisalsocarriedout
regardingthetimeseriesdatasourcesandtheirinherentcharacteristicsthatpredetermine
the format of the data to be analyzed and, consequently, the choice of the forecasting
algorithms. InSections3and4, weperformatheoreticalreviewofthealgorithmsand
machinelearningmodelsthatwillbepresentedinthecontextoftheattemptedcomparisons,
andsubsequently,wepresenttherelevantscientificliterature,organizedbyfieldofresearch
(financialsector,medicalcare,etc.). Specifically,inSection3.1,werefertothecomparison
of the SVM model with the classic ARIMA statistical technique, while in Section 3.2,
thetheoryandapplicationsofdecisiontree-basedmodelsareanalyzed. Section4presents
therationalebehindthedevelopmentofhybridforecastingmodelswithareviewofthe
indicative scientific literature. In any case, the hybrid models chosen for presentation
andanalysisareacombinationoftheARIMAtechniquewithaspecificmachinelearning
model. Section5constitutesapracticalevaluationofthereviewedliterature,withafocus
onextractingtheconditionsunderwhichtheARIMAapproachexhibitssuperiorpredictive
performancecomparedwiththemachinelearningmodels. Finally,Section6coversthe
conclusionsofourreview.
2. Background: DataandAutoregressiveModels
2.1. TimeSeriesData: Forecasting
Timeisthecentralcharacteristicthatdistinguishestimeseriesfromothertypesofdata.
Thispropertyoftheirsisbothalimitationandastructuralelementofthedatacollection,
aswellasasourceofadditionalinformationfortheiranalysis[6]. Essentially,timeseries
dataisanytypeofinformationpresentedasanorderedsequenceandcanbedefinedasa
collectionofobservationsofsomevariable,organizedintoequallyspacedtimeintervals[7].
Thequestionofforecastingisoneofthemostdifficultandessentialproblemsthat
timeseriesanalysismustdealwith. Theperformanceandaccuracyoftheanalysisresults
varydependingonthetypeofdataanditsassumptions. Inadditiontotheseparameters,
the analysis is also affected by factors inherent to the respective field of research, such
as the periodicity of the time series, unforeseen events, changes in the structure of the
organizationsorstructuresfromwhichthedataarecollected,etc.[8]. The“No-Free-Lunch”
theorem proves that it is not possible to have a forecasting method that gives optimal
performance for all possible time series [9]. There is a significant amount of research
literatureonpredictivemodels,andtheresultsofthesestudiesindicatetheexistenceoftwo
macro-categoriesofmethods: statisticalmethodsandmachinelearningmethods. Inthe
continuationofourpaper,wewillrefertothefollowingcategoriesoftimeseriesforecasting
models: (a)statisticalmodels,(b)machineanddeeplearningand(c)hybridmodels[10].
Thecomparisonoftheforecastingresultsoftheaforementionedmodelsinthecontext
ofthestudiespresentedinthepresentworkisbasedonvariousmetrics,figureofmerits,

FutureInternet2023,15,255 4of31
whosemathematicalformulasareexpressedbelow,wherey
t istherealvalueoftheseries
atthetimepointt,yˆ isthecorrespondingforecastedvaluegivenbythemodel,andNis
t
thetimeperiodoftheforecast:
MeanSquaredError(MSE)
|     |     |     | 1 ∑ N       |     |     |
| --- | --- | --- | ----------- | --- | --- |
|     |     | MSE | = (y −yˆ)2. |     | (1) |
|     |     |     | t           | t   |     |
N
t=1
The popular error metric RMSE is used in the scientific literature in place of MSE
(samescaleofthevariable),anditisthesquarerootoftheMSEmetric.
MeanAbsolutePercentageError(MAPE)
N
|     |     |      | 1 ∑ y t −yˆ | t|. |     |
| --- | --- | ---- | ----------- | --- | --- |
|     |     | MAPE | = |         |     | (2) |
N y
|     |     |     | t=1 | t   |     |
| --- | --- | --- | --- | --- | --- |
=MeanAbsoluteError(MAE)
1 N
|     |     | MAE | = ∑ |y −yˆ|. |     |     |
| --- | --- | --- | ------------ | --- | --- |
|     |     |     | t            | t   | (3) |
N
t=1
Coefficientofdetermination(R2)
Itisastatisticalmeasuretoindicatetheproportionofthedependentvariablevariation
inamodelthatcanbepredictedfromthevariationintheindependentmodelvariables,
anditisametricusedtodeterminehowwellourmodelfitsasetofobservations.
MeanAbsoluteDeviation(MAD)
|     |     |       | 1 N           |     |     |
| --- | --- | ----- | ------------- | --- | --- |
|     |     | MAD = | ∑ |(y −m(Y)|, |     | (4) |
t
N
t=1
wherem(X)isthemeanvalueoftheforecastedvaluesforthespecifictimerange.
Nash–Sutcliffemodelefficiencycoefficient(NSE)
It is a metric used to assess the predictive capacity of hydrological models. It is
computedusingthefollowingmathematicalformula:
|                                 |     |     | ∑N (Yt−Yt                  | )2  |       |
| ------------------------------- | --- | --- | -------------------------- | --- | ----- |
|                                 |     | =1− | t=1 o                      | m   |       |
|                                 |     | NSE |                            | ,   | (5)   |
|                                 |     |     | ∑N (Yt−Y¯                  | )2  |       |
|                                 |     |     | t=1 o                      | o   |       |
| whereY¯                         |     |     | isthemodeleddischargeandYt |     |       |
| isthemeanofobserveddischarges,Y |     |     |                            |     | isthe |
| o                               |     |     | m                          |     | o     |
observeddischargeattimet.
Kolmogorov-Smirnovtest(K-Sdistance)
TheKolmogorov–Smirnovtestquantifiesadistancemetricbetweenthedistributionof
ourmodeloutputsandareferencedistributiondefinedbythenullhypothesisofourstudy.
NormalizedMeanAbsoluteError(NMAE)
Thismetricisusedspecificallyintheenergyforecastingdomain,beingabletogener-
alizeunderdifferentupperboundingconditions.
N
|     |         |     | 1 ∑ |y t −yˆ | t |   |     |
| --- | ------- | --- | ------------ | ----- | --- |
|     | NMAE(%) |     | =            | ×100, | (6) |
|     |         |     | N C          |       |     |
t=1
whereCisthecapacityofthepowerplant.

FutureInternet2023,15,255 5of31
2.2. TimeSeriesData: Characteristics
Dataderivedfromtimeseriesmayhavethefollowingcharacteristics[6]:
• Trend: Thischaracteristicisassociatedwiththepresenceofanupward,downward,or
stablecourseoftheseries,withrespecttothetimedimension.
• Seasonality: This characteristic indicates the existence of periodic patterns in the
behaviorofthetimeseries,whichrepeatwithafixedfrequency.
• Stationarity: Stationaryisatimeserieswhosestatisticalproperties(average,variance,
dispersionofvalues,etc.) arestableovertime. Astationarytimeserieswithnotrend
implies that its fluctuations around its mean have a constant width. Furthermore,
theautocorrelationofstatictimeseriesremainsconstantovertime. Basedonthese
assumptions,atimeseriesofthisformcanbethoughtofasacombinationofsignal
andnoise[11].
Inadditiontothesebasiccharacteristics,someofthemorecommonpatternsseenin
timeseriesdataarethefollowing[7]:
-Cyclicbehavior: Incontrasttoseasonalpatterns,cyclicalpatternsappearwhenthe
factorsinfluencingthedataofeachtimeseriesarenotdistinguishedbyafixedorknown
frequency. Thisparticularpatternmainlyconcernsstudiesrelatedtofinancialdata,where
cyclical behavior is observed according to the cycles of the economy and the business
environment. Theaveragedurationofthesecyclesisusuallylongerthanthedurationof
seasonalpatterns,oftheorderoftwoyears.
-Diurnality: Referstotheinherentpatternsobservedintimeseriesoriginatingfrom
aparticularapplicationthathaveadailyormonthlyrepeatcycle. Datarelatedtosolar,
orweatherobservationsaresomeexamplesindicatingthisproperty.
-Outliers: Regarding the detection of anomalies and outliers in time series data,
the analysis focuses on identifying abnormal changes, both desirable and undesirable,
inthedataset.
-Whitenoise: Thischaracteristicreferstothecaseswherethedatadoesnotfollowa
specificpattern.
2.3. TimeSeriesDataSources
Timeseriesdatacancomefromamultitudeofsourcesandsystemswithdifferent
classesofcharacteristics,complexity,volume,andfrequencyofacquisition.Somecategories
ofsourcesofthiskindofdataareindustrialproduction,thefinancialsector,theconsumer
electronicsindustry,healthsystemstructures,retailtrade,meteorology,andgenerallyany
measurableandquantifiablemanifestationofhumanlifeanditsenvironment. Especially
inrecentyears,throughtheexponentialgrowthofdatasources,timeseriesanalysisand
forecastingsystemshavebeenrequiredtoapproachmodelsofever-increasingdimension
andcomplexity.
Timeseriesfromcomplexsystemscapturethedynamicbehaviorandcausesofthe
underlying processes and provide a practical means of predicting and monitoring the
evolution of the system state. However, the non-linearity and non-stationarity that of-
ten characterize the underlying processes of these systems pose a strong challenge to
the process of accurate prediction. For most real-world systems, their dynamical state
vector field is a nonlinear function of the state variables, meaning that the relationship
connectingthesystem’sintrinsicstatevariablestotheirautoregressivetermsandexoge-
nousvariablesisnonlinear. Thetimeseriesresultingfromsuchcomplexsystemsshow
aperiodic(chaotic)patternseveninsteadystates. Furthermore,sincereal-worldsystems
oftenevolveundertransientconditions,thesignalsobtainedfromthemtendtoexhibit
variousformsofnon-stationarity. However,themethodsthatdominatetheliteratureon
theanalysisandforecastingoftimeseriesderivedfromsuchsystemsfocusmainlyonthe
forecastingoflinearandstaticprocesses. AccordingtotheworkofChengetal.[12],con-
ventionalforecastingapproaches,suchasARIMAtechniques,cannotadequatelycapture
theevolutionofthesesystemsfromtheperspectivesofforecastingaccuracy,computational

FutureInternet2023,15,255 6of31
workload,andsensitivitytothequantityandqualityofaprioriinputinformation. This
findingpromptsustoassumethatthesuccessoftheusedpredictionmethod,bothinthe
categoryofclassicalalgorithmsandinthecategoryofmachinelearninganddeeplearning
techniques,dependstoalargeextentonthecomplexityofthesystemdescribedbythedata.
Fromthispointofview,artificialintelligencehasanadvantageoverARIMAtechniques,
aswillbeseenfromtheresultsofthestudiespresentedlaterinthepaper. Atthispoint,it
mustbementionedthatanumberofnon-lineartransformationsexistforoptimizingthe
ARIMAmodelsinnon-linearforecastingapplications,whichwewillrefertointheARIMA
theoreticalbackgroundofourstudy. Onthisnote,thereareafewnotableexceptionswhere
theperformanceofclassicaltechniquesexceedsthatofartificialintelligencemethods.These
resultswillbecommentedonintheconclusionsofourresearch.
2.4. AutoRegressiveIntegratedMovingAverage(ARIMA)Models
TheARIMAmodelisageneralizationoftheARMAmodel(AutoRegressiveMoving
Averagemodel),suitableforhandlingnon-stationarytimeseries. AstheclassicalARMA
modeltakesforgrantedthestationarityofthetimeseriesitisaskedtoanalyze,theman-
agementofinherentlynon-stationarytimeseriesrequirestheirtransformationintoastatic
dataseriesbyeliminatingseasonalityandtrends,throughafinite-pointdifferentiation[3].
Asmentionedearlier,astationarytimeseriescanbethoughtofasacombinationofsignal
andnoise. TheARIMAmodelhandlesthetimesignal,afterfirstseparatingitfromthe
noise, and outputs its prediction for a subsequent time point [11]. As indicated by the
method’sacronym,itsstructuralcomponentsarethefollowing[13]:
• AR:Autoregression. Aregressionmodelthatusesthedependencerelationshipbe-
tweenanobservationandanumberoflaggedobservations(modelparameterp).
• I:Integration.Calculatingthedifferencesbetweenobservationsatdifferenttimepoints
(modelparameterd),aimingtomakethetimeseriesstationary.
• MA:MovingAverage. Thisapproachconsidersthedependencethatmayexistbe-
tweenobservationsandtheerrortermscreatedwhenamovingaveragemodelisused
onobservationsthathaveatimelag(modelparameterq).
TheARmodeloforderp,AR(p),canbewrittenasalinearprocessasfollows:
p
∑
x t = c+ φ i x t−i +(cid:101) t , (7)
i=1
where x thestaticvariable, c aconstant, theterms φ areautocorrelationcoefficientsat
t i
thetimedelaysteps1,2,...,pand(cid:101) arethesamplesoftheGaussianwhitenoiseseries,
t
withzeromeanandσ2variance.
Asimplemovingaveragemodeloforderq,MA(q),canbegivenas:
q
∑
x t = µ+ θ i (cid:101) t−i , (8)
i=0
whereµ,istheexpectedvalueof x (itmostlyequalsto0),θ theweightsappliedtothe
t i
currentandpastvaluesofthestochastictermofthetimeseries,andθ =1. Weconsider(cid:101)
0 t
tobeaGaussianwhitenoiseseries,withzeromeanandσ2variance.
(cid:101)
Bycombiningthesetwomodels,autoregressionandmovingaverage,wecreatethe
ARMAmodelofclass(p,q):
p q
∑ ∑
x t = c+ φ i x t−i +(cid:101) t + θ i (cid:101) t−i , (9)
i=1 i=0
whereφ (cid:54)= 0,θ (cid:54)= 0,σ2 > 0.Theparametersp,qconstitutetheorderoftheARandMA
i i (cid:101)
modelsrespectively.

FutureInternet2023,15,255 7of31
ThegeneralformofanARIMAmodeliswrittenasARIMA(p,d,q),includingthe
integration term that guarantees the stationarity of the time series [13], and it can be
expressedas:
p q
∇dx t = c+ ∑ φ i ∇dx t−i + ∑ θ i (cid:101) t−i , (10)
i=1 i=0
where∇d isadifferentialfactor,introducingadifferenceoforderd,aimingtoremovethe
nonstationarityofthetimeseriesx [14].
t
Table1displaysthebasicparametercombinationsforthenonseasonalARIMAmodels.
Table 1. Nonseasonal ARIMA models for time series forecasting. Random-walk and random-
trend, autoregressiveandexponentialsmoothingmodelsconstitutespecificcasesofthegeneral
ARIMAmodels.Theadditionalpresenceofaconstantinthemodels,accountsforanyunderlying
trendormeaninthedata, inordertoimprovetheirpredictionsandoverallperformanceinthe
forecastingtasks.
ForecastingEquation ARIMA(p,d,q)
first-orderautoregressivemodel ARIMA(1,0,0)
randomwalk ARIMA(0,1,0)
differencedfirst-orderautoregressivemodel ARIMA(1,1,0)
simpleexponentialsmoothing ARIMA(0,1,1)
simpleexponentialsmoothingwithgrowth ARIMA(0,1,1)
linearexponentialsmoothing ARIMA(0,2,1)
linearexponentialsmoothing ARIMA(0,2,2)
damped-trendlinearexponentialsmoothing ARIMA(1,1,2)
2.4.1. ARIMAParameterDetermination
TheoptimalselectionoftheARIMAp,d,andqparametersiscrucialtothesuccess
oftheforecastingprocedure. Thecombinationofthepandqparametersisbasedonthe
examination of the autocorrelation function (ACF) and partial autocorrelation function
(PACF)plotsforthespecificdataset,whilethedparameterischoseninordertostationarize
thetimeseries.
Inmostofthescientificliteraturepresentedintherestofthiswork,itisoftenneeded
toidentifythebest-performingARIMAmodelamonganumberofdifferentARIMA(p,d,q)
modelsforaspecificforecastingapplication. Inthesecases,theselectioncriteriainclude
theAkaike(AIC)andBayesian(BIC)informationcriteria. TheAICmeasuresthequalityof
aforecastingmodel,keepingabalancebetweenoverfittingandmodelcomplexity. Inthe
caseofBIC,thesameruleapplies,butwithahigherpenaltyforcomplexmodels. Inboth
criteria,lowervaluessignifyabettermodel.
There have been many attempts to automate the selection of the ARIMA model
parametersovertheyears,usingdifferenttestsinordertodeterminetheoptimalvaluesfor
bothseasonalandnon-seasonalmodels. Theauto.arimafunctioninR[15]constitutesa
popularheuristicmethodforparameterselectioninanARIMAapplication,anditisbased
onasimplestep-wisealgorithm:
1. Start with a small number of basic ARIMA models and select the one with the
minimumAICvalue.
2. ConsideruptoanumberofvariationsoftheselectedmodelandcalculatetheAIC
valueforeachone. WheneveramodelwithalowerAICisfound,itreplacesthereference
model,andtheprocedureisrepeated. Thealgorithmfinisheswhenwecannotfindamodel
closetothereferencemodelwithalowerAICvalue.
AvalidARIMAmodelisalwaysreturnedbytheabovealgorithmduetothefactthat
themodelspaceisfiniteandthatatleastoneofthestartingmodelswillbeacceptedasa
solution[16].

FutureInternet2023,15,255 8of31
2.4.2. ARIMAVariants
Incasesofseasonaltimeseries,itispossible,duringtheanalysis,fortheforecasting
modeltobepartiallyshapedbynon-seasonal,short-durationfeaturesofthedata. Con-
sequently,theformulationofaseasonalARIMAmodelisrequired,whichincorporates
seasonal and non-seasonal factors into a combined model. The general form of a sea-
sonalARIMAmodelisrepresentedbytheformula: ARIMA(p,d,q)x(P,D,Q) wherepis
S
thenon-seasonalARorder,disthenon-seasonaldifferencingorder,qisthenon-seasonal
MAorder,PistheseasonalARorder,Distheseasonaldifferencingorder,Qistheseasonal
MAorderandSistherecurrencetimerangeoftheseasonalpattern. Themostimportant
stepincalculatingaseasonalARIMAmodelisdeterminingthevaluesoftheparameters
(p,d,q)and(P,D,Q).
The ARIMA technique has evolved over the years, resulting in the development
of many variants of this model, such as the SARIMA (Seasonal ARIMA) and ARIMAX
(ARIMAwithExplanatoryVariable)techniques. Thesemodelsperformwellintermsof
short-term forecasts, but their performance is severely degraded for long-term predic-
tions[8].
2.4.3. AdvantagesandDisadvantages
TheARIMAtechniquepresentsseveraladvantages,amongwhicharetheuseofan
onlinelearningenvironment,theindependencebetweensamplesizeandstoragecosts,
aswellasthefactthatparameterestimationcanbeperformedonline,inanefficientand
scalable way. The disadvantages of this technique are the subjectivity of its progress
evaluation, the fact that the reliability of the selected model may depend on the skill
and experience of the specific forecaster, and the existence of several limitations to the
parametersandclassesofpossiblemodels. Aconsequenceofalltheselimitationsisthefact
thatthefinalchoiceofthepredictionmodelcanbeadifficulttask[17].
AnotherimportantaspectoftheapplicationoftheARIMAtotimeseriesforecastingis
thelinearityofthedatasetitaimstopredict. ThebasicformoftheARIMAalgorithmsis
designedtohandlelineardatarelationships. However,theirscopeofsuccessfulapplication
inforecastingcanbesignificantlyextended,consideringthevarioustransformationsavail-
able,whichextendthemethod’scapabilitytohandlenon-lineartimeseries. Awidelyused
familyofsuchtransformations,includingbothlogarithmicandpowertransformations,is
theBox-Coxtoolset[18],dependingontheλparameteranddefinedas:
(cid:40)
log(y ) if λ =0
t
w = . (11)
t yλ−1
t otherwise
λ
Basedonthevalueofλ,thenewtimeseriescanbetransformedinordertoimprove
theforecastingmodel.
3. MachineLearningModels
Inthepresentwork,thefieldofmachinelearningisregardedasasubsetofthefield
ofartificialintelligence,andasupersetofthefieldofdeeplearningmethods. Inthatscope,
we present the SVM and Decision Tree-based approaches to the problem of time series
forecastingforthemachinelearningfamilyofmethodsandthebasicdeeplearningmodels
thatareusedbythepublicationspresentedintherestofthestudy. Themodelsweselected
to present do not form an exhaustive list of machine learning techniques; rather, they
representsomeofthemainalgorithmiccategoriesusedintherecentscientificliteraturefor
benchmarkingtheARIMAmodelsagainstmachinelearningtechniques.
3.1. SupportVectorMachines(SVM)
Itisasupervisedlearningtechniqueinthefieldofmachinelearningusedfordata
classification. ThegoalofSVMsistofindanappropriate,foreachclassificationproblem,
hyperlayerpartitionofthedataspace(Figure1),withtheaimofcorrectlyclassifyingthe

FutureInternet2023,15,255 9of31
datawhileachievingthemaximumpossibleclassificationmargin[19]. Thishyperplane
maximizesadistancemetricbetweenclassificationclasses. Theclassificationofthedata
iscompletedintwosteps: Inthefirststep,thesupportvectormachineisfedwithaset
ofdataandtheirlabels, i.e.,theinformationabouttheclasstowhicheachonebelongs.
Duringthisstep,thealgorithmsiterativelyoptimizesomemathematicalcriterionbasedon
thelabeleddata. Thetrainingdatathatconstrainthemaximumallowablemarginbetween
classesconstitutethesupportvectors[11]. InFigure2,thesequenceoftheSVMprocessing
stepsisdepictedgraphically.
Inthefieldoftimeseriesforecasting,theregressionvariantoftheSVMmodel(sup-
portvectorregression(SVR))isusedinthescientificliteraturewithincreasingfrequency.
Thedifferencebetweenthisparticularmethodologyandthetraditionaltimeseriesfore-
castingalgorithmsisitsdata-drivenapproachtotheforecastingproblem,incontrasttothe
model-drivenclassicalapproach. IntrainingtheappropriateSVRmodelfortimeseries
prediction,theindependentvariablesutilizedinthescientificliteraturearethelagsofthe
dependentvariablexofthespecificforecastingproblem. TheSVRmodelisoptimizedfora
varyingnumberoflagsbasedonaspecifiederrormetric.
Figure1.Anexampleofalinearlyseparableproblemoftwoclassesinthetwodimensionalspace.
Thesupportvectorsaredefinedbythethreesamplesonthelinesthatdefinethemarginofoptimal
separationbetweenthetwoclasses.
Figure2.Agraphofthesupportvectormachinemodelarchitecture.Thesupportvectorsthatdefine
theregressiveprocessarecreatedbythefeaturespaceandtheoutputspaceconsistsoftheforecasted
timeseries,whichrepresenttheobjectivevariable.

FutureInternet2023,15,255 10of31
Table2.SummaryofARIMAandSVMComparisonStudiesinTimeSeriesForecasting.Intheworks
ofSinghetal.andZhangetal.theARIMAparameterswereoptimizedforeachobservationsite.
| Article | Algorithms           |     | Metrics | Dataset   |
| ------- | -------------------- | --- | ------- | --------- |
|         | ARIMA(2,1,2)×(2,1,2) | 12  | RMSE    | goldprice |
Makalaetal.[20]
SVM MAPE
|                | SVM |     | MAE | COVID-19confirmedcases |
| -------------- | --- | --- | --- | ---------------------- |
| Singhetal.[21] |     |     | MSE |                        |
RMSE
|     | ARIMA(0,1,2)×(1,0,1) | 30  | MAPE | solarenergygeneration |
| --- | -------------------- | --- | ---- | --------------------- |
Atiqueetal.[22] SVM
ANN
|     | ARIMA(0,1,12) |     | MSE | ambientnoiselevels |
| --- | ------------- | --- | --- | ------------------ |
day
ARIMA(0,1,10)
|     | night |     | RMSE |     |
| --- | ----- | --- | ---- | --- |
Tiwarietal.[23]
SVM MAPE
R2
R2
|     | ARIMA |     |     | droughtforecasting |
| --- | ----- | --- | --- | ------------------ |
WNN MSE
Zhangetal.[24]
SVM NSE
K-Sdistance
|                 | ARIMA(2,1,1)      |     | MAPE | shorttimeloadforecasting |
| --------------- | ----------------- | --- | ---- | ------------------------ |
| AlAminetal.[25] | SVM(fornon-linear |     | MSE  |                          |
loadpattern)
|     | ARIMA |     | various | urbanwaterconsumption |
| --- | ----- | --- | ------- | --------------------- |
Liuetal.[26] BP
SVM
3.1.1. FinancialData
In the scientific literature related to time series forecasting applications, SVM and
ARIMAtechniquesarecontrastedinanalyzingdatafromawidevarietyofsources(Table1).
Intheeconomicdomain,theworkofMakalaetal.[20]comparedthecapabilitiesofclassical
ARIMA and SVMs in predicting the daily price of gold. The results of the study show
thatthepredictionusingSVMsoutperformsARIMAbasedontherootmeansquareerror
(RMSE) and mean absolute percentage error (MAPE) metrics, with RMSE = 0.028 and
MAPE=2.5forSVMandRMSE=36.18andMAPE=2897forARIMA,respectively. This
particularresearchalsosupportsthepopularizationoftheuseofSVMtechniquesinthe
pricepredictionofanyproductduetotheaccuracyoftheirresults.
3.1.2. HealthcareData
Regarding the field of medical care, in the work of Singh et al. [21], least-squares
ARIMAandSVMmodelsareappliedtodataonthedailyconfirmedcasesofSARS-CoV-2in
thefivecountrieswiththehighestnumberofcasesduringthetimeperiodofpublicationof
thispaper(Italy,Spain,France,UnitedKingdom,andtheUSA),withtheaimofpredicting
thenumberofconfirmedcasesoveraperiodofonemonthinthesecountries. TheARIMA
parameterswereoptimizedseparatelyforeachcountry. Accordingtotheconclusionsof
thispaper,ARIMAandLeastSquaresSVMmodelshavedifferenthandlingapproachesfor
datacomingfromdifferentcountries: theresearchresultsindicateadropinerrors(MAE,
MSE,andRMSE)andanincreaseinpredictionaccuracy(coefficientdetermination)using
theleastsquaresSVMmodel,withapercentagedifferenceof80%inthepredictionofthe
numberofconfirmedcasesforSpainwithrespecttotheARIMAtechniqueandadifference
of60%forthepredictionsconcerningItalyandFrance.

FutureInternet2023,15,255 11of31
3.1.3. EnergyandNoisePrediction
ThesuperiorityofSVMmodelsfortimeseriesforecastinginrelationtotheclassical
statisticalapproachofARIMAisalsoindicatedbytheresultsoftheworkofAtiqueetal.[22],
regardingthepredictionofthesolarenergycollectedbyasolarpanelduringacalendar
year. This work also highlights the need to improve the overall prediction accuracy of
the models. In the same direction, the study of Tiwari et al. [23] focuses on time series
modelingusingconventionalSVMandARIMAtechniqueson3yearsofnoisetimeseries
data,fromJanuary2015toDecember2017. Thestudycomparedtheperformanceofthe
radialbasisfunctionSVMmodelwiththeARIMAmodel,resultinginthesuperiorityof
theSVMmodelovertheARIMAmodelintermsofmarginoferrorandadaptabilityto
datanon-linearity.
3.1.4. Weather
Inadifferentfieldofresearch,theworkofZhangetal.[24]investigatedandcompared
the prediction abilities of ARIMA, Wavelet Neural Network (WNN), and SVM models
fordroughttimeseriesintheSanjiangPlaininChina. Themodelsofthisresearchwere
basedonthepredictionofSPEI(standardprecipitationevapotranspirationindex)values
collectedduringtheperiod1979–2016fromsevenmeteorologicalstationsinthestudyarea.
Foreachofthesites,theparametersoftheseasonalARIMAmodelwereoptimizedusing
Akaike’sInformationCriterion(AIC).Thecomparisonbetweentherawdatavaluesandthe
predictionsresultedinthefollowingR2andNSE(Nash-Sutcliffecoefficientofperformance)
values: 0.837and0.831fortheWNNnetwork,0.833and0.827fortheSVMnetwork,while
thecorrespondingvaluesoftheclassicalARIMAalgorithmswereabove0.9. Inaddition,
theARIMAmodelshadsmallerMSEvaluesandbetteroverallperformancethantheother
twomodels,whiletheanalysisofvarianceshowedthattheARIMAmodelshadaclear
advantageovertheothertwomodelsinpredictingthedroughtintheSanjiangPlainin
Chinabasedonvariousperformanceindicators(R2,MSE,NSE,andKolmogorov-Smirnov
distance). Accordingtotheresultsofthestudy,WNNandSVMmachinelearningmodels
donotnecessarilyperformbetterthantraditionalARIMAmodelsindroughtprediction.
Differentmethodscanbeusedtoanalyzedatafromdifferentregions,andthecharacteristics
ofthedatashouldbecarefullyanalyzedinordertoselecttheappropriatepredictionmodel.
3.1.5. Utilities
TheresearchofAlAminetal.[25]onpowergridloadforecastingconcludesthatthe
SVMmodelcanpredicttheenergyconsumptionprofilepatternandachievehigheraccuracy
than ARIMA models. However, SVM failed to predict the magnitude of consumption
peaks in some cases, which is related to unpredictable changes in consumer behavior.
The comparison of the two models also highlights the fact that SVM performs better
in the case of non-linear consumption patterns, while ARIMA exhibits better behavior
in the linear load approximation. Finally, in the work of Liu et al. [26], ARIMA, Back-
PropagationNeuralNetwork,SVM,andhybridEEMD-ARIMA,EEMD-BP,andEEMD-
SVM (ensemble empirical mode decomposition) models were compared in predicting
hourlywaterconsumptioninShanghaicityinChina. ThisworkshowsthattheSVMmodel
outperformstheARIMAandthatthehybridEEMD-SVMmodelhasthebestperformance
(basedonvariousmetrics),whileitappearsthattheuseofEEMDdecompositionimproves
thepredictionaccuracyofthealgorithms. Theresearchalsoconcludesthattheoptimal
lengthofthetrainingtimeseriesforhybridalgorithmsisoveroneweek.
3.2. DecisionTreesandRandomForests
Anothermajorcategoryofmachinelearningalgorithmsappliedtotheproblemoftime
seriesforecastingisthesetoftree-basedmodels. Thiscategory,althoughunderrepresented
inthescientificliteratureincomparisontoitsdeeplearningcounterparts,isattheforefront
ofmanyrecentforecastingcompetitions’leaderboards[27].

FutureInternet2023,15,255 12of31
Intimeseriesforecasting,decisiontreesformasuccessionofbinarydecisionsasso-
ciatedtosupervisedfeaturesoftheuseddataset,whichdrivetheforecastingprocedure
basedontheminimizationofthedatavariance[28]. Themodelingofthedecisiontreefor
timeseriesisbasedontheclassificationandregressiontreealgorithm(CART),developed
byBreimanetal.[29].
Randomforestsareformedbyaggregatingthedecisionsofanumberoftreesona
specificproblem. Intimeseriesforecasting,theuseofrandomforestregressionalgorithms
has the advantage of a lower model variance in relation to other machine learning ap-
proaches[30]. Twoofthemostprominentmodelsthatalsodisplaysuperiorperformance
in forecasting competitions are XGBoost and Lightgbm. XGBoost constitutes an imple-
mentationoftheGradientBoostinglearningmethod,namelythatitcombinesanumber
of weak learners into a strong learner in a linear fashion. Both CART and linear classi-
fierscanbeusedasbasemodelsfortheXGBoostalgorithm,whileasecond-orderTaylor
expansion of the cost function entails an enhanced information profile. The Lightgbm
modelisanotherimplementationoftheGradientBoostingDecisionTreealgorithm(GBDT),
basedontwonoveltechniques:gradient-basedone-sidesamplingandtheexclusivefeature
bundling[31].
In the scientific literature presented in later sections of this work, the XGBoost al-
gorithm appears in comparison to ARIMA and deep learning models in the work by
Paliarietal.[32]. Inthisparagraph,wewillpresentsomecomparativeresultsderivedfrom
thepopularMakridakisforecastingcompetitions,aswellasfromtherecentlypublished
scientificliterature.
Table3. SummaryofARIMAandDecisionTree-basedmodels’ComparisonStudiesinTimeSe-
riesForecasting.
| Article | Algorithms           |     | Metrics | Dataset                     |
| ------- | -------------------- | --- | ------- | --------------------------- |
|         | ARIMA(0,1,1)×(0,1,1) |     | MAE     | infectiousdiseaseprediction |
12
| Alimetal.[33] | XGBoost |     | RMSE |     |
| ------------- | ------- | --- | ---- | --- |
MAPE
|             | ARIMA(3,1,0)×(1,1,0) | 12  | MAE  | infectiousdiseaseprediction |
| ----------- | -------------------- | --- | ---- | --------------------------- |
|             | XGBoost              |     | MPE  |                             |
| Lvetal.[34] |                      |     | MAPE |                             |
RMSE
MASE
|               | ARIMA(0,1,1)×(0,1,1) | 7   | MAE  | COVID-19confirmedcases |
| ------------- | -------------------- | --- | ---- | ---------------------- |
| Fangetal.[35] | XGBoost              |     | RMSE |                        |
MAPE
|     | ARIMA(0,1,1) |     | MAE | annualriceproduction |
| --- | ------------ | --- | --- | -------------------- |
|     | XGBoost      |     | MPE |                      |
Noorunnaharetal.[36]
RMSE
MAPE
|     | ARIMA |     | RMSE | retailsalesvolume |
| --- | ----- | --- | ---- | ----------------- |
LSTM MAE
| Zhangetal.[37] | Prophet |     |     |     |
| -------------- | ------- | --- | --- | --- |
GBDT
XGBoost
|                        | ARIMA(2,1,1) |     | MSE  | shorttimeloadforecasting |
| ---------------------- | ------------ | --- | ---- | ------------------------ |
| Priyadarshinietal.[38] | SARIMA       |     | RMSE |                          |
LSTM MAE
LightGBM
Prophet
VAR
|     | various |     | various | retailunitsales(M5) |
| --- | ------- | --- | ------- | ------------------- |
Makridakisetal.[39]
multiplecategories(M4)

FutureInternet2023,15,255 13of31
Althoughlimited,thescientificliteraturefocusedonthecomparisonofARIMAap-
proacheswithdecisiontree-basedforecastingalgorithmsexpandsonavarietyofapplica-
tions. Itis,however,interestingtonotethatthemajorityofforecastingapplicationsusing
tree-basedapproachesconsistofhybridmodels,whichwewillrefertointhesectionon
hybridARIMAmodels:
3.2.1. HealthcareData
TheworkofAlimetal.[33]iscenteredaroundthepredictionofbrucellosisoccurrences
inmainlandChina,withdataacquiredoverhaperiodof10years. TheXGBoostmodelwas
usedincomparisontoanoptimizedseasonalARIMAmodel,andtheresultsofthestudy
indicatedthesuperiorityofthetree-basedapproachtothespecificpredictiontask. Ina
similarsetting,theworkofLvetal.[34]aimsatpredictingtheoccurrencesofhemorrhagic
feverwithrenalsyndromedisease,inmainlandChina.TheXGBoostalgorithmisonceagain
beingusedandcomparedwithanoptimizedseasonalARIMAmodelusingmultipleerror
metricsforone-stepandmultiple-steppredictions. Furthermore,theXGBoostalgorithm’s
performance overpasses the classical approach scores on multiple metrics, indicating
improvedpredictionaccuracyandmodelstabilityforthenon-linearpredictiontask. It
isalsonotedintheconclusionsofthestudythatmultisteppredictionmodelsaremore
practicalthanone-stepapproachesinthetaskofinfectiousdiseaseforecasting. Asuperior
performanceoftheXGBoostalgorithmagainsttheARIMAapproachisalsoderivedfrom
theresultsofthestudybyFangetal.[35],regardingthepredictionofCOVID-19casesinthe
US.However,itisnotedthat,toacertainextent,theARIMAmodelcanbemorepractical
inreal-worldforecastingapplicationsduetoitscharacteristicofprovidingforecastsovera
longertimeframe,whereastheXGBoostapproachimplementsaone-step-aheadprediction.
Thetree-basedmodelalsoneedsnewdatainordertoprovideaccurateforecastsforthe
futureofthediseaseintheUS.
3.2.2. Utilities
Intheutilitiesfield,theworkofNoorunnaharetal.[36]focusesonthepredictionof
annualriceproductioninBangladesh,comparingtheforecastingaccuracyofanoptimized
ARIMAmethod(basedontheAICcriterion)totheXGBoostalgorithm. BasedontheMAE,
MPE,RMSE,andMAPEerrormetrics,theXGBoostmodel’sperformanceinthetestset
wasfoundtobesuperiortotheperformanceoftheARIMAmodel.
Inaslightlydifferentfieldofapplications,theworkofZhangetal.[37]aimstopredict
retailsalesvolumeutilizinganXGBoostmodelandbenchmarkingitsresultsagainstthe
classicARIMAapproach(withoutpreprocessingduetothestationarityofthedataset),
aclassicGradientBoostingDecisionTree(GBDT)algorithm,anLSTMdeeplearningmodel,
andtheforecastingtoolProphet. Theresultsofthisstudyindicatedthatthetree-based
approaches, trained with weather and temperature features, give the best forecasting
performanceamongthefivemodels,whiletheARIMAmodelhastheworstperformance.
Furthermore,itisinterestingtonotethatwhilethetree-basedmodels’resultsaresimilar,
theXGBoostmodelrequiressignificantlyfewertrainingiterationsthantheGBDTapproach,
whilebothtree-basedmodelsrequirefewerdataandfewerfeaturesincontrasttothedeep
learningmodels.
Finally,aninterestingARIMAcomparisontodecisiontreemodelswasfoundinthesci-
entificliteratureregardinganomalydetectioninasmarthomeIoTbyPriyadarshinietal.[38].
Thedatasetwascomprisedofenergyconsumptiondatafrommultiplehomeappliancesand
themachinelearningmodelsweretrainedusingadditionalweatherinformation. Itwas
shownthattheARIMAmodeloutperformseveryothermodelconsideredforthisstudy,
followedbySARIMA,LightGBM,Prophet,VAR,andLSTM,respectively. Thecomparison
wasbasedontheMAE,MSE,andRMSEerrormetrics.

FutureInternet2023,15,255 14of31
3.2.3. ForecastingCompetitions
Asalreadymentioned,tree-basedalgorithmsfortimeseriesforecastinghaveappeared
prominentlyinmanyrecentforecastingcompetitions. TheM5competition[39],focusing
onthepredictionofretailunitsalesformultipleproductcategoriesandlocations,featured
predictionmodelsbasedontreesinthetopscoreranks. Theleadingmodelsforboththe
accuracyanduncertaintyforecastingtasksarebasedonGBDTs,withavisibleprevalence
oftree-basedmodelsovertheirdeeplearningandstatisticalcounterpartsthroughoutthe
competition[27]. Thesophisticationofthetree-basedmodels’characteristicsregarding
featureprocessing,choiceoflossfunction,executiontime,anddefaultparameterselection
are some of the main reasons for their superior performance in the forecasting tasks.
The ranking of the GBDT models over the deep learning approaches had already been
specifiedintheM4competitionresults. Inthatcase,however,themodelsthatdominated
thecompetitionleaderboardweremostlyhybridapproaches[40]. TheM4competition
featuredmultipleforecastingcategories,andthedominantmodelsusedamoretailor-made
approach for each problem than the prevailing M5 models, which treated their GBDT
componentssuchasblackboxes[27].
3.3. DeepLearningModels
Deeplearningisasubsetofmachinelearningandisessentiallyasetofneuralnetwork
modelswiththreeormorelayers. Theseneuralnetworksaimtosimulatethebehaviorof
thehumanbrain,allowingthedeeplearningalgorithmtobetrainedusinglargevolumes
ofdata. Asingle-layerneuralnetworkcanmakeapproximatepredictions,whileadditional
hiddenlayerscanhelpoptimizethenetwork’spredictionaccuracy[41].
Table4containsasummaryofthestudiescomparingARIMAandDeepLearning
modelsintimeseriesforecasting.InthestudyofMenculinietal.,threeARIMAmodelsare
tested,correspondingtoeachofthealimentaryproducts’forecastedprices,whileinthework
ofArunKumaretal.,the(S)ARIMAparametersareoptimizedforeachcountryseparately.
Before referring to specific applications of deep learning networks in time series
forecasting,wewillgiveabriefoverviewofthetypesandcharacteristicsofneuralnetworks
thatwewillrefertointhecontinuationofthework[13]:
3.3.1. ArtificialNeuralNetworks(ANN)
Thisparticularclassofnetworksconsistsofnetworkswithatleastthreelayers: the
inputlayer,oneormorehiddenlayers,andtheoutputlayer. Thenumberoffeaturesin
theinputdatadeterminesthenumberofnodesintheinputlayer,whichareconnectedto
thenodesofthehiddenlayersthrough“synapses”. Eachsynapsehasaspecificweighting
factorthatmultipliesitsinputsignal,andthesetofthesefactorsessentiallydetermines
whichsignalorinputcanpassandwhichcannot. Aneuralnetworkistrainedbyadjusting
thesynapseweights. Inthehiddenlayers, thenodesapplyanactivationfunction(e.g.,
sigmoidorhyperbolictangent)totheweightedsumoftheinputstotransformtheinputs
intooutputsignals. Theoutputlayergeneratesavectorofprobabilitiesforthevarious
outputsandselectstheonewiththeminimumerrorrateorcostusingtheSoftMaxfunction.
Tofindtheoptimalvaluesoftheerrors, theyare“re-propagated”throughthenetwork
from the output layer to the hidden layers, resulting in an iterative adjustment of the
synapse weights. The model is trained when the cost function is minimized through
this iterative process. The basic ANN architecture is presented in Figure 3. The model
capacityandcomplexityincreasewhenmorehiddenlayersandlayernodesareaddedto
themodelarchitecture.

FutureInternet2023,15,255 15of31
Figure3.Basicarchitectureofanartificialneuralnetwork.Byincreasingthenumberofhiddenlayers
(depthofthenetwork),wealsoincreasethecapacityofthemodel.
3.3.2. RecurrentNeuralNetworks(RNN)
Here,thegoalistopredictthenextstepofasequenceofobservationsbasedonthe
previousvaluesofthesequence.Infact,theideabehindRNNsistoexploitthesuccessionof
observationswiththegoalofextractingknowledgefrompreviousstagesofadatasequence
inordertopredictitsfuturebehavior. InRNNs,thehiddenlayersactasbufferstostore
theinformationgatheredinearlierstagesofreadingthesuccessivedatavalues. RNNsare
called“recursive”becausetheyperformthesametaskforeachelementofthesequence,
typically using information gathered earlier in the process to predict future, unknown
datavalues. ThearchitectureandlogicbehindtheRNNbuildingblocksarepresentedin
Figure4. ThemainchallengewithatypicalRNNisthelimitationoftheamountofdata
theycanholdintheir“memory”ateachtrainingstep. Thisproblemissolvedbyusing
the“memorylane”,aconceptintroducedbyrecurrentlong-shorttermmemorynetworks
(Long-ShortTermMemoryrecurrentneuralnetworks,LSTMs).
Figure4.Buildingblockofarecurrentneuralnetwork.

FutureInternet2023,15,255 16of31
3.3.3. Long-ShortTermMemoryNetworks(LSTM)
LSTMisaspecialkindofRNNwithadditionalfeaturesformemorizingthesequence
ofdata,namely,rememberingthetrendofthedatauntilsomepointintimeisrendered
possible through some gates along with a memory line. Each LSTM is a set of cells, or
systemunits,wheredatastreamsarerecordedandstored. Cellssimulateatransmission
line that connects one unit to another, carrying data from the past and gathering it for
thepresent. TheLSTMcellarchitectureisdepictedinFigure5. Threetypesofgatesare
involvedineveryLSTMtocontrolthestateofeachcell:
• Theforgetgateoutputsanumberbetween0and1,where1indicatesfullretentionof
thecontent,while0indicatesfulldiscardingofit.
• Thememorygatechooseswhichofthenewdatawillbestoredineachcell.
• Theoutputgatedecidestheoutputofthecell. Thevalueoftheoutputisbasedonthe
currentstateofthecell,alongwiththefilterednewdata.
LSTMnetworkshavetheabilityto“learn”long-termdependenciesinthedatastream
and are widely used in tasks that work with sequential data, for example, time series.
LSTMssufferfromthevanishinggradientproblem[42],wherebywhenthetimestepis
largeenough,thevalueofthegradientcanbecomeverysmall. Thisproblemoccursas
thenetworkfeedstheoutputsbacktotheinputandrunsthealgorithmwhiletheweights
hardlychangeatall[43].
Figure5. BuildingblockofaLong-shorttermmemorynetwork. Thevariablescandhrepresent
the current state and the hidden state of the LSTM cell, while the input is represented by the x
variable.Thesigmoidgatesinsidetheblockconstitutetheforget,inputandoutputgaterespectively.
Thecurrentstateisupdatedwithrespecttotheinput,accordingtothesumofthecurrentstateanda
combinationoftheinputandthehiddenstateoftheblock.
Themajorityofrecentworks(2019-)comparingtheARIMAmethodwithdeeplearning
techniques in time series forecasting choose LSTM networks or their variants, due to
the memory they introduce in the forecasting process and to deal with the vanishing
gradientproblem.

FutureInternet2023,15,255 17of31
Table4.SummaryofstudiescomparingARIMAandDeepLearningmodelsintimeseriesforecasting.
|     | Article |     | Algorithms | Metrics |     | Dataset      |
| --- | ------- | --- | ---------- | ------- | --- | ------------ |
|     |         |     | LSTM       | RMSE    |     | stockindices |
Naminietal.[8]
BiLSTM
ARIMA(5,1,0)
|     |                  |     |      | MAE    |     | dailystockprice |
| --- | ---------------- | --- | ---- | ------ | --- | --------------- |
|     | Paliarietal.[32] |     | LSTM | (R)MSE |     |                 |
XGBoost
|                 |     |     | ARIMA(6,1,5) | RMSE |     | bitcoinprice |
| --------------- | --- | --- | ------------ | ---- | --- | ------------ |
|                 |     |     | FFNN         | MAPE |     |              |
| Nguyenetal.[44] |     |     | CNN          |      |     |              |
LSTM
SVR
|     |               |     | ARIMA(1,1,0) | RMSE |     | bitcoinprice |
| --- | ------------- | --- | ------------ | ---- | --- | ------------ |
|     | Yamaketal.[6] |     | LSTM         | MAPE |     |              |
GRU
|     |     |     | ARIMA(1,1,0) | precisionrate |     | bitcoinprice |
| --- | --- | --- | ------------ | ------------- | --- | ------------ |
Huaetal.[45]
|     |     |     | LSTM         | timeefficiency |                        |     |
| --- | --- | --- | ------------ | -------------- | ---------------------- | --- |
|     |     |     | ARIMA(3,1,3) | RMSE           | short-termbitcoinprice |     |
|     |     |     | LSTM         | MAPE           |                        |     |
Latifetal.[46]
MAE
MAD
|     |     |     | ARIMA(0,1,0) | (R)MSE |     | financialbudget |
| --- | --- | --- | ------------ | ------ | --- | --------------- |
Rhanouietal.[47]
|                    |               |     | LSTM         | MAE  |                     |               |
| ------------------ | ------------- | --- | ------------ | ---- | ------------------- | ------------- |
|                    |               |     | Prophet      | MAE  | wholesalefoodprices |               |
| Menculinietal.[48] |               |     | LSTM         | MAPE |                     |               |
|                    |               |     | CNN          | RMSE |                     |               |
|                    |               |     | ARIMA(0,1,1) | RMSE |                     | oilproduction |
|                    | Ningetal.[49] |     | LSTM         | MAE  |                     |               |
Prophet
|     |                 |     | ARIMA(2,2,5) | MSE  |     | COVID-19cases |
| --- | --------------- | --- | ------------ | ---- | --- | ------------- |
|     |                 |     | LSTM         | MAPE |     |               |
|     | Kirbasetal.[50] |     | NARNN        | PSNR |     |               |
SMAPE
R-value
|     |     |     | ARIMA  | MSE  |     | COVID-19trends |
| --- | --- | --- | ------ | ---- | --- | -------------- |
|     |     |     | SARIMA | RMSE |     |                |
ArunKumaretal.[51]
RNN-GRU
RNN-LSTM
|     | DeSaaetal.[52] |                      | customCNN/LSTM | MSE  |                     | temperatureforecast |
| --- | -------------- | -------------------- | -------------- | ---- | ------------------- | ------------------- |
|     |                |                      | ARIMA(5,0,6)   | RMSE |                     | airqualityindex     |
|     | Vermaetal.[53] |                      | Prophet        | MAPE |                     |                     |
|     |                |                      | LSTM           | MAE  |                     |                     |
|     |                | ARIMA(2,0,3)×(2,1,3) |                | MSE  | short-termwindspeed |                     |
24
|     | Liuetal.[54] |     | LSTM | MAE |     |     |
| --- | ------------ | --- | ---- | --- | --- | --- |
|     |              |     | GRU  | R2  |     |     |
ARIMA(1,1,0)
|     |     |     |     | RMSE |     | CO 2 levelsforecast |
| --- | --- | --- | --- | ---- | --- | ------------------- |
Spyrouetal.[17]
|     |     |     | LSTM         | MAE  |     |            |
| --- | --- | --- | ------------ | ---- | --- | ---------- |
|     |     |     | ARIMA(1,1,2) | RMSE |     | webtraffic |
Zhouetal.[55]
|     |     |     | LSTM         | MAE  |     |                 |
| --- | --- | --- | ------------ | ---- | --- | --------------- |
|     |     |     | ARIMA(6,1,0) | RMSE |     | cellulartraffic |
Azarietal.[56]
LSTM

FutureInternet2023,15,255 18of31
FinancialData
Intheareaofeconomicforecasting,theworksofNaminietal.[8]andPaliarietal.([13,32])
focusonstockmarketindexforecasting,comparingtheperformanceofLSTMnetworksand
autoregressiveARIMAmodels. Inthefirstpaper,thecomparisonincludesbi-directional
LSTMnetworks(BiLSTMs)whichenhancethetrainingprocessofdeeplearningalgorithms
by dually feeding the input data to the network (1) from input to output and (2) from
outputtoinput. ThispaperperformsabehavioralanalysisofLSTM,BiLSTM,andARIMA
algorithmsandcomparestheirperformances. Theaimofthepaperistoinvestigatethe
contribution of additional training layers to the determination of the required network
parameters,andaccordingtoitsresults,theenhancementofthetrainingprocessthrough
theuseofbidirectionalLSTMnetworksimprovesthepredictionsoffinancialindicators.
Inparticular,ithasbeenobservedthatthepredictionsoftheBiLSTMmodelsarebetter
thanthoseoftheLSTMandARIMAalgorithms,whiletheLSTMmodelsequilibratemuch
fasterthantheBiLSTMnetworks.
The work of Paliari et al., on the other hand, deals with the ARIMA, LSTM, and
XGBoostcomparisonschemes. TheXGBoostalgorithmisanimplementationoftheclassof
gradientboostingalgorithms,whichbuildsamachinelearningmodelfromsimplermodels
(usuallydecisiontrees)withthegoalofimprovingthefinalperformance. Accordingtothe
resultsofthiswork,LSTMandXGBoostalgorithmsgivebetterforecastingresultsthan
ARIMAformostpricesets,whileARIMAachieveslowererrorvaluesintwoofthestock
pricesets,whosedatavaluesaresignificantlylowerthantherest,whichseemstoaffectthe
resultsoftheanalysis. Inthisparticularcase,ARIMAoutperformedbothmachinelearning
methodsinincorporatingfeaturesizewhileignoringunits. Ontheotherhand,LSTMgives
betterresultsthantheothertwomethods,achievingthelowesterrorscoresinmostofthe
considereddatasets.
Movingontooneofthemostpopularforecastingtasksinthefinancialsector,pre-
dicting the extremely volatile price of bitcoin is an investment, and as a result, there is
anever-increasinginterestinmaterializingthiskindofforecastingstudy. Therearetwo
mainmethodsofpredictingthepriceofbitcoin. Thefirstmethodisbasedonbitcoinprice
timeseries,whilethesecondexploitstherelationshipbetweenthebitcoinpriceandother
indicatorssuchasthestockprice,oilprice,goldprice,etc.
TheworkofNguyenetal.[44]focusesonbitcoinpricepredictionthroughthefirst
method, whichisbasedontimeseries. TheARIMAmodelandmachinelearningalgo-
rithmssuchasFeedforwardNeuralNetworks(FFNN),ConvolutionalNeuralNetworks
(CNN),LSTM,andSupportVectorRegression(SVR)areusedcomparativelyintermsofthe
predictabilityofbitcointimeseries. Furthermore,hybridmodelsareproposedtoimprove
theprediction,whichwewillrefertointherestofourwork. ARIMA(6,1,5)modelis
selectedtopredictbitcoinprice,whileneuralnetworksaretrainedwithsamplingevery1to
14samples,andavariablenumberoftrainingepochsfrom100,200,and500. Afterthecom-
putationalexperiment,anFFNNmodelisusedwithasamplingper5time-steps,9hidden
nodes,and100trainingepochs. AlsoselectedistheCNNmodel,withitscharacteristics
beingasamplingstepequalto5,6hiddennodes,and200epochs. AnLSTMmodelwitha
samplingstepequalto5,100hiddenunits,and100trainingepochsisalsoused. SVRuses
an“rbf”kernelandasamplingstepequalto4. TheresultsoftheRMSEandMAPEmetrics
showed that ARIMA had the lowest prediction error of the “short-term” bitcoin price,
theLSTMnetworkgaveanequallygoodresult,andamongtherest,theworst-performing
networkwasCNN.
TheworkofYamaketal.[6]usesthetimeseriesbitcoinpricedatasettomakepre-
dictions and compare ARIMA, LSTM, and GRU models. Specifically, the GRU (Gated
RecurrentUnit)network,suchastheLSTM,belongstothecategoryofrecurrentneural
networks(RNNs). UnlikeLSTM,however,ithasasimplerstructureasitdoesnotusean
outputgatebutanupdategateandaresetgate. Thesegatesarevectorsthat“decide”what
informationwillappearintheoutput. TheresultsoftheworkshowthattheARIMAmodel
givesbetterresultsthanthedeeplearningmodelsforboththepredictionerrorandthe

FutureInternet2023,15,255 19of31
balancingtimeofthealgorithms. ARIMAgivesvaluesof2.76%and302.53forMAPEand
RMSE,respectively. However,GRUperformsbetterthanLSTM,with3.97%and381.34
MAPEandRMSE,respectively.
InasimilardirectiontoYamaketal.’sworkmovesHua[45]’sworkonbitcoinprice
predictionusingARIMAandLSTMalgorithms. Thispaperconcludesthatbothmethods
cangivegoodpredictionresults,whileafterthetrainingperiod,theLSTMnetworkshows
higherpredictionefficiencyandaccuracy. Ingeneral,usingasmalleramountofpastdata
forforecasting,LSTMcanleadtobetterresultsthanARIMA,whichisquiteefficientin
makingpredictionsintheshortterm,butastheforecastingintervalincreases,itshowsa
decreaseintheaccuracyrate.
BitcoinpricepredictionthroughARIMAandLSTMalgorithmsisalsocarriedoutin
the work of Latif et al. [46] where the forecast is made for the next day using the static
forecastmethod,withorwithoutre-estimatingtheforecastmodelateachstep.Twotraining
andtestsetsareconsideredtoevaluatethepredictions: Inthefirsttrainingset,ARIMA
outperformed LSTM, but in the second training sample, LSTM outperformed ARIMA.
Furthermore,inthetwocontrolsetforecastingperiods,LSTMwithmodelre-estimationat
eachstepoutperformedARIMA.TheLSTMcanproduceforecastsclosertoactualhistorical
values than the ARIMA model. LSTM can predict the direction as well as the price of
thetimeseriesatthegiventimeperiod,whileARIMAonlyfollowsthetrendofbitcoin
pricesandisunabletopredicttheactualpricesveryaccurately. Thispaperconcludesthat
althoughtheaccuracymetricsindicateasatisfactoryperformanceoftheARIMAalgorithm,
theARIMApredictionbasedontheerrormetricsismuchlesssatisfactorythantheLSTM
model. TheauthorsofthepaperemphasizethattheARIMAmodelwasabletoachievea
correctpredictionduetotheupwardtrendofthebitcoinpricetimeseriesandthatifthe
trendwasdownward,ARIMAcouldnothavegivenacorrectprediction.
TheworkofRhanouietal.[47]residesinthefinancialsectorbutconcernsitselfwith
thepredictionofthebudgetconsumedbyagovernmentorganization. Furthermore,the
superiorityofLSTMsisevidentoverARIMAduetotheirincreasedabilityinidentifying
non-linearstructuresinfinancialtimeseries.
Utilities
TheworkofMenculinietal.[48]comparestheARIMAtechniquewithProphet,ascal-
ableforecastingtoolavailablefromMetabasedonageneralizedadditivemodel,anddeep
learning models LSTM and CNN (convolutional neural networks). The study regards
datafromthreewholesalealimentaryproductprices,andtheparametersoftheARIMA
approach to the forecasting problem correspond to each of the datasets. The findings
showedthatwhiletheProphetmodelisfasttotrainandrequiresnodatapreprocessing,
itisnotabletocomeclosetotheperformanceoftheothermodels,anditsuseisrecom-
mendedonlywhensimplicityandspeedofpredictionarethemainrequirementsofthe
analysis. Incontrast,ARIMAmodelsandLSTMneuralnetworksperformsimilarlyforthe
forecastingtaskunderconsideration,whilethecombinationofCNNandLSTMachieves
thebestoverallaccuracybutrequiresmoretimetotunethehyperparameters. Therefore,
whenfairlyaccurateforecastsandshortforecastextractiontimesarerequiredinaparticular
multivariatedataset,thepapersuggeststheuseofsimpleLSTMmodelsoverunivariate
ARIMAmodels.
Finally,theworkofNingetal.[49]dealswiththepredictionofoilproductiontime
series,consistingofdataonfluctuationsintheoperationsofaspecificwellanditsreservoirs.
Threealgorithmsarestudiedtoaddressthelimitationsoftraditionalproductionforecasting:
theARIMAmethod,theLSTMnetwork,andtheProphetforecastingtool. Theadvantages
of machine learning models are workflow simplicity, fast and reliable prediction for a
typicaldecliningproductioncurve. AnimportantfeatureoftheProphetmodelistheability
itprovidestorecordwinterfluctuationsinproduction,whichcan,byalertingtheoperator,
prevent potential failures. The application of ARIMA, LSTM, and Prophet methods to
65wellsintheDJbasinshowsthatARIMAandLSTMtechniquesperformbetterthanthe

FutureInternet2023,15,255 20of31
Prophetmodel,possiblybecausenotalloilproductiondataincludesseasonalvariations.
Inaddition,wellsinnearbyreservoirscanbestudiedusingthesameparametervaluesin
ARIMAandLSTMmodelstopredictoilproductionusingatransferredlearningframework.
Inparticular,ARIMAisobservedtobeeffectiveinpredictingtheoilproductionrateof
wellsacrosstheDJbasin.
Althoughthemajorityofworksdealingwiththecomparisonofclassicalstatistical
analysismethodswithmachineanddeeplearningmethodsintimeseriesforecastingare
basedonapplicationsinthefinancialsector,wewillalsorefertoworksrelatedtothefields
ofmedicalcare,theenvironment,andtechnology.
HealthcareData
Inthehealthsector,thenumberofstudiesdealingwithpredictiveprocessesrelatedto
theCOVID-19diseasehasincreasedinrecentyearsforobviousreasons. Thesuperiorityof
LSTMsoverclassicalARIMAisindicatedonceagainintheworkofKirbasetal.[50],in
whichthenumberoftotalconfirmedcasesofthediseaseindifferentEuropeancountries
ismodeled.
TheworkofArunKumaretal.[51]comparesdeeplearning(RecurrentNeuralNet-
works,GRU,andLSTM)andstatistical(ARIMAandSARIMA)techniquestopredictthe
totalnumberofconfirmedactiveandrecoveredcasesaswellasthenumberofdeathsfrom
theCOVID-19disease. GRU,LSTM,ARIMAandSARIMAmodelsweretrained,tested,
andoptimizedforpredictingCOVID-19trends. Thebestmodelwasselectedbasedon
thelowestvaluesoftheMSEandRMSEmetrics. Formosttimeseriesdatafordifferent
countries,themodelsbasedondeeplearning(LSTMandGRU)outperformthestatistical
ARIMAandSARIMAmodels,withRMSEvalues40timessmallerthanthoseoftheARIMA
models. However, for some countries, statistical models outperformed deep learning
models. Duetothehighlydynamicnatureofdisease-specificdata,theinformationthey
containdependsonthecountryoforigin,aswellasthetimeatwhichtheyweregenerated.
Theshapeofthedatacomingfromsomecountriesisnon-linearwhileARIMAmodelsare
showntoperformbetterinmodelingdatathatfollowslinearrelationships. Ontheother
hand, RNNmodels performedbetterin countrieswhose datawere non-linear. Forthe
number of confirmed cases, SARIMA statistical models behaved best for India, Russia,
Peru,Chile,andtheUnitedKingdom,whileARIMAperformedbestforBrazil. ForMexico
andIran,theLSTMmodelperformedbest,whiletheGRUmodelperformedbestforthe
USAandSouthAfrica. Fortherecoveredpatients,theARIMAmodelperformedbestfor
theUSA,Russia,andChile,whiletheSARIMAmodelperformedbestforBrazil,India,and
SouthAfrica. ForMexico,PeruandtheUnitedKingdom,theGRUmodelperformedbetter
thantherestofthemodels. SimilarlyforIran,theLSTMmodelhadthebestperformance
comparedwiththerestofthemodels. Forforecastingthedeathdata,theLSTMmodel
outperformed the rest for Brazil, Russia, South Africa, Peru and the United Kingdom.
For the countries India and Iran, the GRU models performed best. On the other hand,
theSARIMA-basedmodelsperformedwellfortheUSA,Mexico,andChile,whereas,onthe
contrary,theARIMAmodelsofallcountrieshavethehighestvaluesoftheRMSEandMSE
metrics,whichsuggeststhattheclassicalapproachisnotsuitableformodelingdeathsfrom
COVID-19. Recordeddiseasecasualtieshadanon-linearrelationshipwithtime,which
cannot be modeled with simple ARIMA models. Therefore, SARIMA models that can
captureseasonality,aswellasRNNs,havebetterforecastingperformanceincountrieswith
non-lineardatarelationships.
WeatherandEnvironmentalParameterStudies
Anotherpopularfieldofforecastinginthescientificliteratureisweatherforecasting,
whichisadifficulttaskduetothechaoticnatureofatmosphericvariations.
TheworkofDeSaaetal.[52]comparesclassicalARIMAwithdeeplearningmodels,
aimingtoderivetemperaturepredictions. Theuseddeeplearningmodelconsistsofone-
dimensionalconvolutionallayerstoextractthespatialfeaturesofthedata,andlayersbased

FutureInternet2023,15,255 21of31
ontheLSTMarchitecturetoextractthetemporalfeatures. Thetwomodelsareappliedto
theanalysisoftemperaturedatafromtheSzegedareainHungary,withanhourlysampling
frequency. Theexperimentalresultsclearlyindicatethatthedeeplearningmodelhasa
superiorperformanceintermsofaccuracyovertheARIMAmodelasitwasabletoachieve
alowerrootmeansquareerrorvalue. TheMSEobtainedbythedeeplearningmodelis
21%lowerthanthatoftheARIMAmodel.
IntheworkofVermaetal.[53],ARIMA,Prophet,andLSTMmodelsarecompared
inpredictingtheAirQualityIndex(AQI)valuesforthecityofDelhi,India. According
tothesurveyresults,theProphetmodelperformsthebestintermsofthemeanabsolute
percentage error (MAPE) metric; however, it is greatly outperformed by the other two
models in the remaining metrics, namely the root mean square error (RMS) and mean
absoluteerror(MAE).Inaddition,itappearsthattheLSTMmodeloutperformstheARIMA
modelintermsofallthreemetricsandthereforecanbeconsideredthebest-performing
modelforthisdataset.
In a slightly different field of research, the work of Liu et al. [54] deals with the
forecastingoftimeseriesconsistingofmeasuredwindspeedsincoastalareasofScotland
withanhourlysamplingfrequency. Thedatasetsusedhavebeencollectedusingaspecial
setup with three measuring positions. The models compared in terms of time series
forecastingabilitywereseasonalARIMA(SARIMA)anddeeplearningmodelsGRUand
LSTM.Tomaximizeperformance,bothSARIMAanddeeplearningmodelstunedtheir
hyperparameters through a combination of manual search and grid search. Based on
thesixresearchmetricsused,theSARIMAapproachoutperformeddeeplearning-based
algorithmsinpredictionperformance. TheauthorsofthispaperarguethattheSARIMA
approachismoresuitablefordealingwithoffshorewindspeedforecastingbecauseofits
abilitytodirectlysupportmakingpredictionsofseasonalelementsonunivariatedatasets.
Furthermore,theSARIMAmodelrequiresthesettingofonlysixparameters(p,q,d,P,Q,
D),whilemanymorehyperparametersneedtobeevaluatedinGRUandLSTM,suchas
thenumberofnodesineachlayer,thenumberoflayers,thesizeoftheinput,thenumber
oftrainingepochs,theoptimizer,thechosenactivationfunction,theinitializationofthe
kernelfunction,andsoon. Although,inrecentdecades,muchattentionhasbeenpaidto
thedevelopmentofsuitablemodelstoachieveaccurateoffshorewindspeedforecasting,
conventionalneuralnetworksprovetobedeficientinproducingshort-termtimeseries
forecasts. Thesemodelsshowproblemsofoverfittingor“entrapment”atlocalextremes.
The SARIMA approach is a simpler and more efficient tool than deep learning-based
modelsforpredictingoffshorewindspeedtimeseries.
AnotherexampleofenvironmentaltimeseriesforecastingistheworkofSpyrouetal.[17],
wheretheLSTMalgorithmiscomparedwithclassicalARIMAintermsofpredictingcarbon
dioxidelevelsintheportareaofIgoumenitsa. Abatchsizeof100,1000,and7000wasused
fortraining,andtheperformanceofthemodelswasevaluatedusingtheRMSEandMAE
metrics. Itisshownthroughtheanalysisresultsthatforabatchsizeof7000,theLSTM
modelgivesagoodpredictionresultbasedontheRMSEandMAEmetricsintermsof
modeltrainingandvalidationlosses. RegardingthecomparisonoftheLSTMmodelwith
theARIMAmodel,itbecomesevidentthatARIMAgivesbetterpredictions,whileLSTM
alsoperformsquitewell.
NetworkTraffic
TheworkofZhouetal.[55]focusesonthepredictionofwebtraffic,akeycomponent
innetworkmanagementandtrafficregulation. Inthispaper,theARIMAiscomparedwith
anLSTMmodelintheforecastingtask,andtheirresultsarecomparable,withtheLSTM
displayingaslightlybetterperformancethantheclassicalapproach. Inasimilarresearch
field,Azarietal.[56]forecastmeasuredusertrafficandtrafficburstsincellularnetworks
using an ARIMA classical algorithm and an LSTM model. While the LSTM approach
displaysabetterforecastingresultthanARIMA,thisobservationisheavilylinkedtothe
lengthofthedatasetanditsgranularity,bothofwhichmustbelargeenough. Itisalso

FutureInternet2023,15,255 22of31
observedthattheclassicalalgorithms,underspecifictimeintervalanddatagranularity
circumstances,canperformclosetotheoptimalLSTMprediction.
Theresults,ontheonehand,demonstratethesuperiorperformanceofLSTMover
ARIMAingeneral,especiallywhenthelengthofthetrainingdatasetislargeenoughandits
granularityisfineenough. Ontheotherhand,theresultsshedlightonthecircumstances
inwhichARIMAperformsclosetooptimalwithlowercomplexity.
4. HybridModels
Attemptingtocombinethebestmodelingfeaturesofbothclassicalstatisticalalgo-
rithmsandmachinelearningmodels,alargepartofthetimeseriesforecastingscientific
literatureisconcernedwiththedevelopmentofcombinationsofforecastingmodels. We
willinitiallyrefertothemotivationsbehindthedevelopmentofhybridmodelsand,in-
dicatively, emphasize some applications from various fields of research while focusing
on the characteristics of the given problem and how these are modeled by the trained
predictionmodels.
Hybridtimeseriesforecastingmodelsaredevelopedinthescientificliteraturebased
onthreemainfactors:
First,becauseofthepracticaldifficultyindeterminingwhetherthetimeseriesunder
consideration has been produced by linear or non-linear underlying processes, as well
asthedifficultyinchoosingoneforecastingmethodovertheothersforaparticulartask
andforecastingenvironment. Theusualpracticetodealwiththisparticularproblemis
essentiallytodevelop,train(inthecaseofmachinelearningalgorithms),andtestmorethan
onepredictivemodel,whilefactorssuchassamplinguncertaintyandthedispersionofthe
samplingprocessmakeitdifficulttogeneralizethechosenmodel.Consequently,combining
severalalgorithmstocreateacomplexpredictionmodelcanfacilitatetheselectionprocess.
Thesecondreasonfordevelopinghybridmodelsisthefactthattimeseriesproduced
byrealprocesses,inthemajorityofcases,donothaveapurelylinearornon-linearprofile
butcontainacombinationoflinearandnon-linearpatterns. Inthesecases,singlestatistical
orneuralmodelsarenotsufficientfortimeseriesmodelingandforecastingsincethesimple
versionoftheARIMAmodelcannotdealwithnon-linearrelationships,whiletheneural
network model alone is not able to handle linear and non-linear patterns equally well.
Therefore, by combining ARIMA models with machine learning models, the complex
autocorrelationstructuresinthedatacanbemodeledmoreaccurately.
Thethirdfactortoconsideristhefactthatinthescientificliteratureontimeseries
forecasting,itisalmostuniversallyacceptedthatthereisnooneforecastingmethodthat
is better than all others for every forecasting situation. This is largely due to the fact
thatarealproblemisoftencomplexinnature,andanysinglemodelmaynotbeableto
capturethedifferentpatternsequallywell. Therefore,thecombinationofdifferentmodels
can increase the probability of detecting different patterns in the data and improve the
predictionperformance. Inaddition,thecombinatorialmodelismorerobusttoapossible
structuralchangeinthedata[4].
Regardingthecombinationofdifferentforecastingalgorithmsinbuildinganefficient
hybridmodel,variousworkflowsareproposed,accordingtotheforecastingproblemat
handaswellasitsscientificapproach.
IntheclassicworkbyZhangetal.[4],ahybridmodelcombiningARIMAandneural
networksisproposed,aimingtoexploitthecapabilitiesofeachmodelintermsoflinear
andnon-linearmodeling,respectively. Theproposedmethodologyconsistsoftwosteps:
Inthefirststep,theARIMAmodelisusedtoanalyzethelinearpartoftheproblem,while
inthesecondstep,aneuralnetworkisdevelopedtomodeltheresidualsoftheARIMA
model. SincetheclassicalARIMAmodelcannotcapturethenon-linearstructureofthe
data, the residuals of the linear model will contain information about the non-linearity.
The outputs of the neural network can be used as predictors for the error terms of the
ARIMAmodel. Theresultsofthisresearchshowedthatthehybridmodelimprovesthe
predictionaccuracyofbothindividualmodels. Theproposedhybridapproachispresented

FutureInternet2023,15,255 23of31
graphicallyinFigure6. AsimilarapproachisusedbyBiswasetal.[57],Prajapatietal.[58],
and Nie et al. [5] in different research fields and with a different selection of machine
learningalgorithms,combinedwiththeARIMAmodel.
Figure6.FlowchartofhybridArimaandMachineLearningmodelfortimeseriesforecasting.This
particularworkflowisnottheonlyoneusedinthescientificliterature.Differentcombinationsofthe
ARIMAandMLmodelshavebeenproposed([5,44]),basedonthenatureoftheforecastingproblem
andthemodelingapproach.
4.1. FinancialData
Inthefieldofbitcoinpricepredictionresearch, whichwehaveencounteredinnu-
merousworks([6,44,45])thedevelopmentofhybridforecastingmodelsisawidelyused
practice. TheworkofNguyenetal.[44]whichwealreadymentionedinthedeeplearn-
ingmodelsparagraph,usescombinationsofARIMAwithFFNN,CNN,LSTM,andSVR
modelstomakebitcoinpricetimeseriespredictions,aswellastocomparethesehybrid
models. Thisparticularworkusesadifferenthybridstrategythantheonepresentedin
Figure6,namely,itutilizeseachalgorithm(ARIMAandML-based)withrespecttothe
fluctuationlevelobservedfordifferenttimeseriesintervals. Theflowchartofthisapproach
isdepictedinFigure7. TheresultsoftheworkbasedontheRMSEandMAPEmetrics,
showthattheperformancesofthefourhybridmodelsareveryclose,withthebestbeing
givenbythecombinationofARIMAwiththeCNNmodel. Anotherexampleofahybrid
modelapplicationinthefinancialdomainistheworkbyZhengetal.
4.2. Weather
Intermsofweatherforecasting,researchbyBiswasetal.[57]suggestsusingacom-
binationofregressionandmachinelearningmodelstopredictwindenergyproduction
overone,two,andsevendaytimehorizons. Theforecastisbasedonweatherdatasuch
aswindspeedanddirection,airtemperatureandpressure,anddensityattheheightof
themeasurementnode. Thepreliminaryresultsofthisstudyindicatethatthecombination
of ARIMA with Random Forest algorithms (ARIMA-RF) as well as the combination of
ARIMAwithBayesianRegressionandClassificationTrees(BCART)helptoimprovethe
forecastingaccuracycomparedwiththeclassicalforecastingalgorithmofARIMA.

FutureInternet2023,15,255 24of31
Figure7.FlowchartofhybridArimaandMachineLearningfortimeseriesforecasting,basedonthe
fluctuationinterval.
4.3. HealthcareData
In the field of medical care and specifically regarding the prediction of COVID-19
cases,theworkofPrajapatietal.[58]movesonthreelevels: Modelingtheoveralltrendin
thenumberofcasesovertime,short-termforecastingontheorderoftendaysincountries
withextremelyhighpopulationdensitysuchasIndia,anddeterminingwhichalgorithm
presentsthebestmetricsperformanceinaccuratelymodelingthelinearandnon-linear
characteristicsofthecasecounttimeseries. Variousindividualpredictionmodelsbased
ontheProphet, Holt-Winters, LSTM,andARIMAalgorithmswereused, aswellasthe
ARIMA-NARNN(NonlinearAutoregressiveNeuralNetwork)hybridmodel. Thesimple
ARIMAalgorithmperformedbetterthanotherindividualmodels;however,thehybrid
combinationofARIMAandNARNNhadthebestoverallperformance,withRMSEvalues
almost35.3%betterthanARIMA.
4.4. Utilities
InrelationtotheapplicationsofSVMsintimeseriesforecasting,theworkofNieetal.[5]
dealswithshort-termloadforecastinginenergytransmissionsystems. Short-termload
isavariablethatisaffectedbymanyfactors,andforthisreason,itisdifficulttomakean
accuratepredictionwithasinglemodel. UtilizingtheARIMAalgorithmtoforecastthe
basiclinearpartoftheloadandtheSVMalgorithmtoforecastthesensitive,non-linearpart
oftheload,thepaperpresentsaforecastingmethodbasedonahybridARIMAandSVM
model. ARIMAisusedtoforecastthedailyload,andthentheSVMmodelisused,aiming
tocorrectthedeviationsfromthepreviousforecasts. Duetotheirgeneralizationabilityand
fastcomputation,SVMsshowexcellentperformanceinextractingthenonlinearpartofthe
loadandcanbeusedtoachievethecorrectionofthedatadeviation. TheARIMA-SVM
hybridmodeleffectivelycombinestheadvantagesofARIMAandSVMsandthroughthe
simulationofalargesampleofdata,theresultsshowthatthishybridmodelismuchbetter
thanthetwoforecastingmodelsappliedseparately.
4.5. NetworkTraffic
Finally,inthefieldofnetworkparameterforecasting,wepresenttheworkofMaetal.[59],
wheretheARIMAalgorithmiscombinedwiththeMultiLayerPerceptronandtheMultidi-
mensionalSupportVectorRegressionmodelsinahybridapproachtothenetwork-wide
trafficstateforecastingproblem. Anincreasedpredictiveperformanceisobservedinrela-
tiontothestatisticalforecastingmethodincaseswherethenetworktrafficisconsidered

FutureInternet2023,15,255 25of31
both at a local and global scale with the incorporation of the hybrid prediction model.
Aninterestingchangeinthehybridmodelworkflowwithrespecttothepreviouslymen-
tionedstudiesisthefactthatinthiscasetheARIMAalgorithmisusedaftertheneural
networkinordertopost-processtheMLmodelresiduals. Thisisalso,accordingtothe
authors,“necessaryandawarrantatleastforthesituationwherethetimeseriesdataare
notsufficientlylong”.
Thespecificworkaimstopredictthetrafficstateforasmallcityareabasedonthe
measurementandpredictionofthreemacroscopictrafficvariables: trafficvolume,speed,
andoccupancy.Thedatasetiscomprisedoftimeseriescollectedfromanetworkofdetectors
alongtheHighwayAyaloninTelAviv,Israel. Theproposedapproachcannotonlycapture
thenetwork-wideco-movementpatternoftrafficflowsinthetransportationsystembutalso
seizelocation-specifictrafficcharacteristicsaswellasthesharpnonlinearityofmacroscopic
trafficvariables.Thecasestudyindicatesthattheaccuracyofpredictioncanbesignificantly
improvedwhenbothnetwork-scaletrafficfeaturesandlocation-specificcharacteristicsare
takenintoaccount.
5. DiscussionandPracticalEvaluation
Inthispaper,aseriesofworksondifferentareasoftimeseriesanalysisandforecasting
were selectively presented, with the aim of comparing the classic ARIMA forecasting
algorithmswithmachinelearninganddeeplearningmodels. Asweseeintheconsolidated
representationofthesetasksinTables2–5theusedmetrics,basedonwhichthecomparison
ofeachalgorithmwiththeARIMAtechniquewasperformed,aresimilarforthemajority
ofthetasks.
Table5.SummaryofstudiescomparingARIMAandHybridModelsintimeseriesforecasting.
Article Algorithms Metrics Dataset
ARIMA/ANN MSE variety
Zhangetal.[4]
MAD
ARIMA/FFNN RMSE bitcoinprice
ARIMA/CNN MAPE
Nguyenetal.[44]
ARIMA/LSTM
ARIMA/SVR
ARIMA/RF NMAE windpower
Biswasetal.[57]
ARIMA/BCART
Prajapatietal.[58] ARIMA/NARNN RMSE COVID-19cases
short-termload
ARIMA/SVM MAPE
Nieetal.[5] forecasting
RMSE
NN/ARIMA MSE network-wide
Maetal.[59]
MSVR/ARIMA MAPE traffic
In the comparisons of the individual machine learning models with the ARIMA
algorithm,alargepartoftheapplicationsindicatethesuperiorityoftheformerbasedon
themetricsused. However,therewereasubsetofstudiesinwhichARIMAdemonstrated
higherpredictiveaccuracy. Wewillrefertothesestudiesintherestofthepresentchapter
inordertopracticallyevaluatetheperformanceoftheARIMAagainstthemachinelearning
modelsandtouncoverthecircumstances(eitherdatasetormodel-dependent)underwhich
thestatisticalapproachexhibitssuperiorperformanceinthetaskoftime-seriesforecasting.
ARIMAoverSVMModels
InthecaseofSVMalgorithms,intheworkofZhangetal.[24]ondroughtprediction,
theARIMAalgorithmhadclearlybetterpredictionperformancebasedonvariousmetrics,
compared with the selected WNN and SVM models (Section 3.1.4). According to the
authorsofthispaper,WNNandSVMmachinelearningmodelsarenotalwayssuperiorto

FutureInternet2023,15,255 26of31
traditionalARIMAmodelsindroughtprediction. Differentforecastingmethodscanbe
usedfordifferentgeographicregions,anditwouldbesubsequentlyadvisedforthedata
characteristicstobeinvestigatedinordertoselecttheappropriateforecastingmodel.
ThisconclusionisconsistentwiththeresultoftheworkofAlAminetal.[25],inwhich
ARIMAperformedbetterthanSVMnetworksinloadpredictionwhentheloadwaslinear
(Section3.1.5). AsARIMAismuchmorerobustandefficientatanalyzinglineartimeseries,
itschoiceovermachinelearningalgorithmsshouldprimarilydependonthelinearityof
thedata. Inadifferentapplicationfield,theworkbyPriyadarshinietal.[38]indicatedthe
superiorityofARIMA,andSARIMAforecastingovermultipledeeplearningandtree-based
forecastingmodelsregardinganomalydetectioninanIoTsetting. However,thisparticular
publicationisfocusedontheapplicationathandratherthanonthemodelcomparison.
ARIMAoverDeepLearningModels
In the case of individual deep learning models vs. ARIMA, by introducing LSTM
networks and the property of memory in the forecasting process, these models gain a
greatadvantageoverclassicalstatisticalforecastingmethods,andthisisshownbytheir
dominanceoverARIMAintherelevantliterature. However,thereareexceptionstothis
rule,whichwewillrefertobelow.
IntheworkofPaliarietal.[32]onstockindexforecasting,theLSTMandXGBoost
algorithmsgavebetterforecastingresultsthanARIMAforallbuttwodatasets,whose
datavaluesweresignificantlylowerthantherest(Paragraph“FinancialData”). Thisfact
probablyindicatesanadvantageofstatisticalmethodswhenthedataischaracterizedbya
limitedrangeofvalues.
ARIMAmethodsprevailoverdeeplearningalgorithmsinbitcoinpriceprediction
applicationsintheworksofNguyenetal.[44]andYamaketal.[6],andthisresultmaybe
duetoseveralfactors,asthechosenvaluesofthemodelparametersandthetotalamount
ofdatacanaffecttheresultsoftheanalysis. ThevolumeofdataintheworkofYamaketal.
isrelativelysmall,andRNNmodelsusuallyperformwellonmorevoluminousdatasets,
aspreviousstudieshaveshown(Paragraph“FinancialData”). Regardingthisparticular
observation, it is worth mentioning the related work of Cerqueira et al. [60], according
towhichmachinelearningmethodsimprovetheirrelativepredictiveperformanceover
classicalpredictionalgorithmsasthedatasamplesizegrows.
IntheworkofHuaetal.[45],ARIMAisquiteeffectiverelativetoLSTMsinmaking
bitcoinpricepredictionsintheshortterm,butastimegoeson,itshowsadecreasingrate
ofaccuracy(Paragraph“FinancialData”).
IntheworkofArunKumaretal.[51],theauthorsattempttopredicttheratesofcon-
firmedcases,recoveredpatients,anddeathsfromtheCOVID-19diseaseindifferentcoun-
triesoftheworld. Formostcross-countrytimeseriesdata,thedeeplearning-basedmodels
(LSTM and GRU) outperform the statistical ARIMA and SARIMA models, with RMSE
values40timessmallerthanthoseoftheARIMAmodels. However,insomecountries,
statisticalmodelsoutperformeddeeplearningmodels(Paragraph“HealthcareData”). Due
tothehighlydynamicnatureofdisease-specificdata,theinformationtheycontaindepends
onthecountryoforiginaswellasthetimeatwhichtheyweregenerated. Theshapeof
thedatacomingfromsomecountriesisnon-linear,whileARIMAmodelsareshownto
performbetterinmodelingdatathatfollowslinearrelationships. Ontheotherhand,RNN
modelsperformedbetterincountrieswhosedatawerenon-linear. Theseresultsonceagain
confirmtheconclusionmadeabove,namelythatsinceARIMAismuchmorerobustand
efficientinlineartimeseriesanalysis,itschoiceovermachinelearningalgorithmsshould
primarilydependonthelinearityofthedata. Inthiswork,itisalsointerestingthatwhile
ARIMAis,accordingtotheresults,anidealchoiceformodelingtheratesofconfirmed
casesandrecoveredpatientsforsomecountrieswhosedatahavetheappropriateprofile,its
performanceisneverthelessverypoorformodelingthenumberofdeathsfromCOVID-19
inallcountries, whichislikelyrelatedtotheincreasingcomplexityofthedataandthe
conditionsthatleadtothedeathofpatientsingeneral.

FutureInternet2023,15,255 27of31
IntheworkofLiuetal.[54],whichconcernsthepredictionoftimeseriesconsisting
ofthemeasuredwindspeedincoastalareas,theSARIMAapproachoutperformeddeep
learning-basedalgorithmsinpredictionperformance(Paragraph“WeatherandEnviron-
mentalParameterStudies”). TheauthorsofthispaperarguethattheSARIMAapproach
ismoresuitablefordealingwithoffshorewindspeedforecastingbecauseofitsabilityto
directlysupportmakingpredictionsofseasonalelementsonunivariatedatasets.
Finally,intheworkofSpyrouetal.[17],ARIMAagainoutperformsLSTMmodelsin
predictingharborareaCO2levels,whichislikelyrelatedtothenatureoftheforecastdata
(Paragraph“WeatherandEnvironmentalParameterStudies”).
HybridModelsoverARIMA
Ontheotherhand,asfarasthehybridforecastingmodelsareconcerned,inanycase
andinthecontextofthiswork,theyresultinbetterforecastingperformancecompared
withthesingleARIMAmodel,astheycombinemodelingfeaturesbothfromthepointof
viewofclassicalstatisticalalgorithmsandonthepartofmachinelearningmodels,making
themcapableofdealingwithpredictivedataatmultiplelevelsofanalysis.
FinalRemarks
Therearevariousconclusionsderivedfromthescientificliteraturecitedintheprevi-
ousparagraphs.
At first, we observe that the optimal choice of a forecasting algorithm can be dif-
ferent, for different versions of a dataset (e.g., different geographic regions in drought
forecasting[24],differentcountriesinmodelingratesofconfirmedandrecoveredcases
of COVID-19 [50]) within the same forecasting task. The particular differences in the
datasets’nature,alsoinferredfromtheoptimalmodelchoice,canbeofgreatvalueina
multitudeofforecastingandmodelingtasksandcanbeanimportantsourceofinformation
forregioncharacterization.
Ontheotherhand,insomeapplications,itisthedatasetcharacteristicsinherenttothe
specificdatadrivennetworkthatdrivethemodelingchoice. Theseasonalityofthedata
collected(e.g.,windspeedforecasting[54]),thenumberoftargetvariables,aswellasa
multitudeofunderlyingcausesandfeatures(e.g.,forecastingthenumberofCOVID-19
deaths[50])canshapethenatureofaforecastingapplication. Inouropinion,thesystem-
atic characterization of applications and datasets would be of great value to modeling
applicationsinordertofullyexploitthecapabilitiesofbigdataanddata-drivennetworks.
The ARIMA also exhibits better predictive performance than its machine learning
counterparts,incaseswheretheavailabledatasetischaracterizedbyalimitedrangeof
valuesoralimitedtime-span([6,32,45]). Thisobservationcanbeattributedtothefactthat
machinelearning,andespeciallydeeplearningmodels,requirealargeamountofdatato
traineffectively. Asaresult,theirperformancecanbeinferiortostatisticalapproachesfor
smalldatasetsorforshort-termforecasting.
ThealgorithmicnatureoftheARIMAmodelsprovidessomeinsightintotheirim-
plementationvalueintheproblemoftimeseriesforecasting. Incomparisontocomplex
machinelearningmodels,ARIMAisarelativelyexplainableandintuitiveapproachthat
iswidelyusedduetoitsflexibilityandreliability. However,itsfocusonlineartimede-
pendenciesinthedataaswellasitsunivariatemodelingapproachrenderitunsuitablefor
standaloneapplicationinforecastingcomplexreal-worldproblems.
Apartfromthedetailsofthetimeseriesdata,whichcanbeadeterminingfactorinthe
choicebetweenARIMAandmachinelearningmodels,animportantaspectoftheproblem
regards the computational and time complexity of the two approaches. In the case of
machinelearningforecastingmodels,awiderrangeofresourcesisneeded,regardingthe
storageofthenetworkarchitectureandweights,thetrainingtime,andthenetworkopti-
mizationprocedure,allofwhicharenotnecessaryintheapplicationofclassicalstatistical
algorithms. Furthermore,astheforecastingproblemathandbecomesmorecomplexand
acquireslongertimedependencies,sodoesitsartificialintelligencemodelingapproach.

FutureInternet2023,15,255 28of31
InTable6,wepresentsomeaggregatedresultsandobservationsbasedonthepractical
evaluationoftheARIMAversusthemachinelearningapproachtotheproblemoftime
seriesforecasting.
Table6. AdvantagesanddisadvantagesofARIMAoverArtificialIntelligencemodels,regarding
timeseriesforecastingtasks.
| Criterion | ARIMA |     | ArtificialIntelligence |     |
| --------- | ----- | --- | ---------------------- | --- |
Explainable Regardedasa“blackbox”
Flexiblespecification Needtraining
|       | Reliableperformance         |     | Needoptimization           |     |
| ----- | --------------------------- | --- | -------------------------- | --- |
| Model | Designedtomodeldependencies |     | Betteratmodelling          |     |
|       | thatcanbelinearizable       |     | non-lineartimedependencies |     |
throughasingletransformation
|     | Parameterspecification |     | Standardtrainingprocedure |     |
| --- | ---------------------- | --- | ------------------------- | --- |
dependingonuser-experience
|     | Suitableforsmalldatasets  |     | Needlargedatasetstotrain |     |
| --- | ------------------------- | --- | ------------------------ | --- |
|     | Missingvaluesnotimportant |     | Difficultmodelling       |     |
whenvaluesaremissing
|     | Multipleseasonality |     | Complexmodelling |     |
| --- | ------------------- | --- | ---------------- | --- |
nothandlednatively
Dataset
|     | Designedforunivariateseries |     | Handlemultivariatedatasets |     |
| --- | --------------------------- | --- | -------------------------- | --- |
|     | Sensitivetooutliers         |     | Dependonmodelcomplexity    |     |
Assumedataintegrated Dataagnostic
ofafiniteorder
|     | Handlesindependentforecastingtasks |     | Jointforecastofmultipletimeseries |     |
| --- | ---------------------------------- | --- | --------------------------------- | --- |
|     | Lowtimecomplexity                  |     | Trainingandvalidationneeded       |     |
ingeneral(dependingonthemodel)
Complexity
|     | Smallcomputationalrequirements |     | Hardwareandcomputational |     |
| --- | ------------------------------ | --- | ------------------------ | --- |
[61] demandshigher(dependingonmodel)
6. Conclusions
While the classical statistical approach to the problem of time series forecasting is
stillpracticallyrelevant,recentadvancesinthemachinelearningfieldhaveintroduced
to the scientific community a variety of different models and a multitude of possible
combinationsofsuchmodelsandtheirstatisticalcounterparts. Nevertheless,theARIMA
methodisprevailinginseveralcases,duetothenatureofspecificforecastingapplications
anddatasets.Furthermore,evenconsideringthesheerforceofthemachinelearningmodels
andtheirnumerouspredictivecapabilities,theyhavesignificantlylargercomputational
demandsincontrasttotheclassicstatisticalmodels. Thedetailsoftheforecastingproblem
athand,theavailableresources,andthepreviousscientificapproachestoaspecifictask
shouldallbeconsideredpriortoproceedingwithasingleforecastingstrategy.
Author Contributions:
|     | Conceptualization, | Investigation, | V.I.K.; Methodology | V.I.K. and A.D.P.; |
| --- | ------------------ | -------------- | ------------------- | ------------------ |
Validation,V.I.K.,A.D.P.andI.K.;Writing—originaldraftV.I.K.,A.D.P.andI.K.;Writing—review&
editingV.I.K.,A.D.P.,I.K.andG.K.M.Allauthorshavereadandagreedtothepublishedversionof
themanuscript.
Funding:Thisresearchreceivednoexternalfunding.
DataAvailabilityStatement:Notapplicable.
Acknowledgments:Wewouldliketoexpressourgratitudetothereviewersofthispaperfortheir
insightfulcommentsandsuggestions,whichhavehelpedusimprovethequalityofthefirstversion
ofourmanuscript.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.

FutureInternet2023,15,255 29of31
References
1. Makridakis,S.;Spiliotis,E.;Assimakopoulos,V. StatisticalandMachineLearningforecastingmethods: Concernsandways
forward. PLoSONE2018,13,e0194889.[CrossRef]
2. Dwivedi,Y.K.;Hughes,L.;Ismagilova,E.;Aarts,G.;Coombs,C.;Crick,T.;Duan,Y.;Dwivedi,R.;Edwards,J.;Eirug,A.;etal.
Artificial Intelligence (AI): Multidisciplinary perspectives on emerging challenges, opportunities, and agenda for research,
practiceandpolicy. Int.J.Inf.Manag.2021,57,101994.
3. Box,G.E.;Jenkins,G.M.;Reinsel,G.C.;Ljung,G.M. TimeSeriesAnalysis:ForecastingandControl;JohnWiley&Sons:Hoboken,NJ,
USA,2015.
4. Zhang, G.P. TimeseriesforecastingusingahybridARIMAandneuralnetworkmodel. Neurocomputing2003, 50,159–175.
[CrossRef]
5. Nie,H.;Liu,G.;Liu,X.;Wang,Y.HybridofARIMAandSVMsforshort-termloadforecasting. EnergyProcedia2012,16,1455–1460.
[CrossRef]
6. Yamak,P.T.;Yujian,L.;Gadosey,P.K. Acomparisonbetweenarima,lstm,andgrufortimeseriesforecasting. InProceedingsof
the20192ndInternationalConferenceonAlgorithms,ComputingandArtificialIntelligence,Sanya,China,20–22December
2019;pp.49–55.
7. TimeSeriesData. Availableonline:https://www.clarify.io/learn/time-series-data(accessedon12July2023).
8. Siami-Namini,S.;Tavakoli,N.;Namin,A.S. Acomparativeanalysisofforecastingfinancialtimeseriesusingarima,lstm,and
bilstm. arXiv2019,arXiv:1911.09512.
9. Wolpert,D.H.;Macready,W.G. Nofreelunchtheoremsforoptimization. IEEETrans.Evol.Comput.1997,1,67–82.[CrossRef]
10. Bauer,A.;Züfle,M.;Herbst,N.;Kounev,S. Bestpracticesfortimeseriesforecasting(tutorial). InProceedingsofthe2019IEEE
4thInternationalWorkshopsonFoundationsandApplicationsofSelf*Systems(FAS*W),Umea,Sweden,16–20June2019;pp.
255–256.
11. Rundo,F.;Trenta,F.;diStallo,A.L.;Battiato,S. Machinelearningforquantitativefinanceapplications:Asurvey. Appl.Sci.2019,
9,5574.[CrossRef]
12. Cheng,C.;Sa-Ngasoongsong,A.;Beyca,O.;Le,T.;Yang,H.;Kong,Z.;Bukkapatnam,S.T. Timeseriesforecastingfornonlinear
andnon-stationaryprocesses:Areviewandcomparativestudy. IIETrans.2015,47,1053–1071.[CrossRef]
13. Siami-Namini,S.;Tavakoli,N.;Namin,A.S. AcomparisonofARIMAandLSTMinforecastingtimeseries. InProceedingsofthe
201817thIEEEinternationalconferenceonmachinelearningandapplications(ICMLA),Orlando,FL,USA,17–20December
2018;pp.1394–1401.
14. Xue,B.;Tong,N.;Xu,X.;He,X. DynamicalShort-TermPredictionofRainAttenuationinWBand:ATime-SeriesModelwith
SimplerStructureandHigherAccuracy. IEEEAntennasPropag.Mag.2019,61,77–86.[CrossRef]
15. RDocumentation:Auto.Arima:FitBestARIMAModeltoUnivariateTimeSeries. Availableonline:https://www.rdocumentation.
org/packages/forecast/versions/8.21/topics/auto.arima(accessedon12July2023).
16. Hyndman,R.J.;.Khandakar,Y. AutomaticTimeSeriesForecasting: TheforecastPackageforR. J.Stat. Softw. 2008,27,1–22.
[CrossRef]
17. Spyrou, E.D.; Tsoulos, I.; Stylios, C. Applying and comparing LSTM and ARIMA to predict CO levels for a time-series
measurementsinaportarea. Signals2022,3,235–248.[CrossRef]
18. Box,G.E.;Cox,D.R. Ananalysisoftransformations. J.R.Stat.Soc.Ser.BStat.Methodol.1964,26,211–243.[CrossRef]
19. Cortes,C.;Vapnik,V. Supportvectormachine. Mach.Learn.1995,20,273–297.[CrossRef]
20. Makala,D.;Li,Z. PredictionofgoldpricewithARIMAandSVM. J.Phys.Conf.Ser.2021,1767,012022.[CrossRef]
21. Singh,S.;Parmar,K.S.;Makkhan,S.J.S.;Kaur,J.;Peshoria,S.;Kumar,J. StudyofARIMAandleastsquaresupportvectormachine
(LS-SVM)modelsforthepredictionofSARS-CoV-2confirmedcasesinthemostaffectedcountries. ChaosSolitonsFractals2020,
139,110086.[CrossRef][PubMed]
22. Atique,S.;Noureen,S.;Roy,V.;Bayne,S.;Macfie,J. Timeseriesforecastingoftotaldailysolarenergygeneration:Acomparative
analysisbetweenARIMAandmachinelearningtechniques. InProceedingsofthe2020IEEEGreenTechnologiesConference
(GreenTech),OklahomaCity,OK,USA,1–3April2020;pp.175–180.
23. Tiwari,S.;Kumaraswamidhas,L.;Garg,N. Comparisonofsvmandarimamodelintime-seriesforecastingofambientnoise
levels. InAdvancesinEnergyTechnology:SelectProceedingsofEMSME2020;Springer:Singapore,2022;pp.777–786.
24. Zhang,Y.;Yang,H.;Cui,H.;Chen,Q. ComparisonoftheabilityofARIMA,WNNandSVMmodelsfordroughtforecastingin
theSanjiangPlain,China. Nat.Resour.Res.2020,29,1447–1464.[CrossRef]
25. AlAmin,M.A.;Hoque,M.A. ComparisonofARIMAandSVMforshort-termloadforecasting. InProceedingsofthe20199th
AnnualInformationTechnology,ElectromechanicalEngineeringandMicroelectronicsConference(IEMECON),Jaipur,India,
13–15March2019;pp.1–6.
26. Liu,X.;Zhang,Y.;Zhang,Q. ComparisonofEEMD-ARIMA,EEMD-BPandEEMD-SVMalgorithmsforpredictingthehourly
urbanwaterconsumption. J.Hydroinformatics2022,24,535–558.[CrossRef]
27. Januschowski,T.; Wang,Y.; Torkkola,K.; Erkkilä,T.; Hasson,H.; Gasthaus,J. Forecastingwithtrees. Int. J.Forecast. 2022,
38,1473–1481.[CrossRef]
28. Das,R.;Middya,A.I.;Roy,S. HighgranularandshorttermtimeseriesforecastingofPM2.5airpollutant—Acomparativereview.
Artif.Intell.Rev.2022,55,1253–1287.[CrossRef]

FutureInternet2023,15,255 30of31
29. Breiman,L.;JeromeFriedman,C.J.S.R.O. ClassificationandRegressionTrees;ChapmanandHall/CRC:BocaRaton,FL,USA,1984.
30. How Can Times Series Forecasting Be Done Using Random Forest? Available online: https://analyticsindiamag.com/
how-can-times-series-forecasting-be-done-using-random-forest/#:~:text=A%20random%20forest%20regression%20model,
forecasting%20for%20achieving%20better%20results.&text=Traditional%20time%20series%20forecasting%20models,to%20
handle%20the%20continuous%20variables(accessedon12July2023).
31. Sun,X.;Liu,M.;Sima,Z. AnovelcryptocurrencypricetrendforecastingmodelbasedonLightGBM. Financ. Res. Lett. 2020,
32,101084.[CrossRef]
32. Paliari,I.;Karanikola,A.;Kotsiantis,S. AcomparisonoftheoptimizedLSTM,XGBOOSTandARIMAinTimeSeriesforecasting.
InProceedingsofthe202112thInternationalConferenceonInformation,Intelligence,Systems&Applications(IISA), Chania
Crete,Greece,12–14July2021;pp.1–7.
33. Alim,M.;Ye,G.H.;Guan,P.;Huang,D.S.;Zhou,B.S.;Wu,W. ComparisonofARIMAmodelandXGBoostmodelforprediction
ofhumanbrucellosisinmainlandChina:Atime-seriesstudy. BMJOpen2020,10,e039676.[CrossRef]
34. Lv,C.X.;An,S.-Y.;Qiao,B.-J.;Wu,W. TimeseriesanalysisofhemorrhagicfeverwithrenalsyndromeinmainlandChinabyusing
anXGBoostforecastingmodel. BMCInfect.Dis. 2021,21,839.[CrossRef]
35. Fang,Z.;Yang,S.;Lv,C.;An,S.;Wu,W. Applicationofadata-drivenXGBoostmodelforthepredictionofCOVID-19intheUSA:
Atime-seriesstudy. BMJOpen2022,12,e056685.[CrossRef][PubMed]
36. Noorunnahar,M.;Chowdhury,A.H.;Mila,F.A. AtreebasedeXtremeGradientBoosting(XGBoost)machinelearningmodelto
forecasttheannualriceproductioninBangladesh. PLoSONE2023,18,e0283452.[CrossRef]
37. Zhang,L.;Bian,W.;Qu,W.;Tuo,L.;Wang,Y. TimeseriesforecastofsalesvolumebasedonXGBoost. J.Phys.Conf.Ser.2021,
1873,012067.[CrossRef]
38. Priyadarshini,I.;Alkhayyat,A.;Gehlot,A.;Kumar,R. Timeseriesanalysisandanomalydetectionfortrustworthysmarthomes.
Comput.Electr.Eng.2022,102,108193.[CrossRef]
39. Makridakis,S.;Spiliotis,E.;Assimakopoulos,V. TheM5competition:Background,organization,andimplementation. Int.J.
Forecast.2022,38,1325–1336.[CrossRef]
40. Bojer,C.S.;Meldgaard,J.P.Kaggleforecastingcompetitions:Anoverlookedlearningopportunity. Int.J.Forecast.2021,37,587–603.
[CrossRef]
41. DeepLearning. Availableonline:https://www.ibm.com/topics/deep-learning(accessedon12July2023).
42. Hochreiter,S.;Schmidhuber,J. Longshort-termmemory. NeuralComput.1997,9,1735–1780.[CrossRef]
43. Azari,A. Bitcoinpriceprediction:AnARIMAapproach. arXiv2019,arXiv:1904.05315.
44. Nguyen,D.T.;Le,H.V. PredictingthepriceofbitcoinusinghybridARIMAandmachinelearning. InProceedingsoftheFuture
DataandSecurityEngineering: 6thInternationalConference, FDSE2019, NhaTrangCity, Vietnam, 27–29November2019;
Proceedings6;Springer:Berlin/Heidelberg,Germany,2019;pp.696–704.
45. Hua,Y. BitcoinpricepredictionusingARIMAandLSTM. E3SWebConf.2020,218,01050.[CrossRef]
46. Latif,N.;Selvam,J.D.;Kapse,M.;Sharma,V.;Mahajan,V. ComparativePerformanceofLSTMandARIMAfortheShort-Term
PredictionofBitcoinPrices. Australas.Account.Bus.Financ.J.2023,17,256–276.[CrossRef]
47. Rhanoui,M.;Yousfi,S.;Mikram,M.;Merizak,H. Forecastingfinancialbudgettimeseries:ARIMArandomwalkvsLSTMneural
network. IAESInt.J.Artif.Intell.2019,8,317.[CrossRef]
48. Menculini,L.;Marini,A.;Proietti,M.;Garinei,A.;Bozza,A.;Moretti,C.;Marconi,M. Comparingprophetanddeeplearningto
ARIMAinforecastingwholesalefoodprices. Forecasting2021,3,644–662.[CrossRef]
49. Ning,Y.;Kazemi,H.;Tahmasebi,P. Acomparativemachinelearningstudyfortimeseriesoilproductionforecasting:ARIMA,
LSTM,andProphet. Comput.Geosci.2022,164,105126.[CrossRef]
50. Kırbas¸,I˙.;Sözen,A.;Tuncer,A.D.;Kazancıog˘lu,F.S¸.ComparativeanalysisandforecastingofCOVID-19casesinvariousEuropean
countrieswithARIMA,NARNNandLSTMapproaches. ChaosSolitonsFractals2020,138,110015.[CrossRef]
51. ArunKumar,K.;Kalaga,D.V.;Kumar,C.M.S.;Kawaji,M.;Brenza,T.M. ComparativeanalysisofGatedRecurrentUnits(GRU),
longShort-Termmemory(LSTM)cells,autoregressiveIntegratedmovingaverage(ARIMA),seasonalautoregressiveIntegrated
movingaverage(SARIMA)forforecastingCOVID-19trends. Alex.Eng.J.2022,61,7585–7603.[CrossRef]
52. DeSaa,E.;Ranathunga,L. ComparisonbetweenARIMAandDeepLearningModelsforTemperatureForecasting. arXiv2020,
arXiv:2011.04452.
53. Verma,P.;Reddy,S.V.;Ragha,L.;Datta,D.Comparisonoftime-seriesforecastingmodels. InProceedingsofthe2021International
ConferenceonIntelligentTechnologies(CONIT),Hubli,India,25–27June2021;pp.1–7.
54. Liu,X.;Lin,Z.;Feng,Z. Short-termoffshorewindspeedforecastbyseasonalARIMA-AcomparisonagainstGRUandLSTM.
Energy2021,227,120492.[CrossRef]
55. Zhou,K.;Wang,W.Y.;Hu,T.;Wu,C.H. ComparisonofTimeSeriesForecastingBasedonStatisticalARIMAModelandLSTM
withAttentionMechanism. J.Phys.Conf.Ser.2020,1631,012141.[CrossRef]
56. Azari, A.; Papapetrou, P.; Denic, S.; Peters, G. CellularTrafficPredictionandClassification: AComparativeEvaluationof
LSTMandARIMA. InDiscoveryScience;KraljNovak,P.,Šmuc,T.,Džeroski,S.,Eds.;SpringerInternationalPublishing:Cham,
Switzerland,2019;pp.129–144.

FutureInternet2023,15,255 31of31
57. Biswas,A.K.;Ahmed,S.I.;Bankefa,T.;Ranganathan,P.;Salehfar,H. Performanceanalysisofshortandmid-termwindpower
predictionusingARIMAandhybridmodels. InProceedingsofthe2021IEEEPowerandEnergyConferenceatIllinois(PECI),
Urbana,IL,USA,1–2April2021;pp.1–7.
58. Prajapati, S.; Swaraj, A.; Lalwani, R.; Narwal, A.; Verma, K. Comparison of traditional and hybrid time series models for
forecastingCOVID-19cases. arXiv2021,arXiv:2105.03266.
59. Ma,T.;Antoniou,C.;Toledo,T. Hybridmachinelearningalgorithmandstatisticaltimeseriesmodelfornetwork-widetraffic
forecast. Transp.Res.PartCEmerg.Technol.2020,111,352–372.[CrossRef]
60. Cerqueira,V.;Torgo,L.;Soares,C. Machinelearningvsstatisticalmethodsfortimeseriesforecasting:Sizematters. arXiv2019,
arXiv:1909.13316.
61. Computational Complexity of Machine Learning Algorithms. Available online: https://medium.com/datadailyread/
computational-complexity-of-machine-learning-algorithms-16e7ffcafa7d(accessedon12July2023).
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.