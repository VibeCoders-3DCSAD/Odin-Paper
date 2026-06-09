Review
Selected Topics in Time Series Forecasting: Statistical Models vs.
Machine Learning
DagTjøstheim
DepartmentofMathematics,UniversityofBergen,5008Bergen,Norway;dag.tjostheim@uib.no
Abstract: Machinelearningforecastingmethodsarecomparedtomoretraditionalpara-
metricstatisticalmodels. Thiscomparisoniscarriedoutregardinganumberofdifferent
situationsandsettings. Asurveyofthemostusedparametricmodelsisgiven. Machine
learningmethods,suchasconvolutionalnetworks,TCNs,LSTM,transformers,random
forest, and gradient boosting, are briefly presented. The practical performance of the
variousmethodsisanalyzedbydiscussingtheresultsoftheMakridakisforecastingcom-
petitions(M1–M6). IalsolookatprobabilityforecastingviaGARCH-typemodelingfor
integertimeseriesandcontinuousmodels. Furthermore,Ibrieflycommentonentropyasa
volatilitymeasure. Cointegrationandpanelsarementioned. Thepaperendswithasection
onweatherforecastingandthepotentialofmachinelearningmethodsinsuchacontext,
includingtheveryrecentGraphCastandGenCastforecasts.
Keywords: timeseriesforecasting;machinelearning;statisticalmodel;neuralnetwork;
randomforest;forecastingcompetition;weatherforecasting
1. IntroductoryRemarks
To be able to succeed in time series forecasting, a repeated past pattern is needed,
andthatpatternhastocontinueintothefuturetosomeextent. Thehighertheregularity
of this pattern, the higher its expected forecastability. In other words, the higher the
disorderisinthehistoryofthetimeseries,themoredifficultitistopredict. Thedisorder
ofatimeseriescanbeformallymeasuredintermsofitsentropy(approximateentropy
and sample entropy), e.g., see Ref. [1]. The concept of entropy comes from the field of
AcademicEditor:AndreaMurari
physics.Ininformationtheory,theShannoninterpretationofentropyisusedtomeasurethe
Received:13December2024
amountsofinformationrequiredtoaccuratelysendandreceivesomemessages(e.g.,see
Revised:28February2025
theexplanationandgedankenexperimentin[2]). Indataanalysis,theconceptofentropy
Accepted:4March2025
hasbeenusedtoanalyzepatternsinmedicaldata,suchasheartrate;later,thisspreadto
Published:7March2025
applicationsinphysiology,finance,climatesciences,andanumberofotherphenomena.
Citation: Tjøstheim,D.Selected
Inpractice,theentropyinaforecastingsituationisseldomlycomputedexplicitly,butitis
TopicsinTimeSeriesForecasting:
StatisticalModelsvs.Machine indirectlyreflectedintheuncertaintyofatimeseriesforecast. Uncertaintycanbegiven
Learning.Entropy2025,27,279. in terms of a probability interval, a confidence interval, or, in more detail, as a forecast
https://doi.org/10.3390/e27030279 distribution,whichattachesprobabilitiesanddistributionstoavarietyofpredictedvalues.
Copyright:©2025bytheauthor. Eventhoughaforecastisoftenjustgivenbyapointforecast,whichmaybeinterpretedas
LicenseeMDPI,Basel,Switzerland. themostlikelyvalueofatimeseriesvariableatafuturetime,itseemstobeincreasingly
Thisarticleisanopenaccessarticle commonnowadaystoletthepointforecastbeaccompaniedbyameasureofuncertainty.
distributedunderthetermsand
This,inasense,canbethoughtofasreflectingtheentropyoftheseries. Itisexplainedin
conditionsoftheCreativeCommons
moredetailattheendofSection5.2. Afewmorecommentsonentropyandforecastability
Attribution(CCBY)license
arealsogiveninSection4.4onforecastingcompetitions.
(https://creativecommons.org/
licenses/by/4.0/).
Entropy2025,27,279 https://doi.org/10.3390/e27030279

Entropy2025,27,279 2of34
Thehistoryoftimeseriesforecastinggoesveryfarback,atleasttotheageofantiquity,
withmoreorlessaccuratepredictionsofastronomiceventsandfutureweather. Presently,
forecastsareusedvirtuallyeverywhere,rangingfrom,say,economicsandopinionpollsto
long-andshort-termweatherforecasts. Someforecastsaremoreorlesspurelystatistical
innature,i.e.,demandforecastingforgroupsofitemsbasedentirelyandexclusivelyon
pastsales,butothertypesofforecasts,suchasfinancialpredictions,areaidedbyeconomic
theory, whereas weather forecasting may depend critically on a geophysical theory of
theatmosphere.
Atpresent,forecastingishelpedbyanenormousincreaseintheavailabilityofdata.
OursistrulytheageofBigData. However,howcanthishelpustomakebetterpredictions?
Isiteasierormoredifficulttoseepatternsinthedatathatcanbeexploitedinforecasting?
Inparallelwiththeincreaseindata,therehasbeenanincreaseintheavailabilityandspeed
ofcomputers. Computerscancertainlydetectpatternsincomplexdatathathumansor
moresimpleanalyzingtechniquescannotdetect. Therearemachinelearning(hereafter
denotedML)techniquesforhandlingsuchpatterns,butaretheyusefulforforecasting? Or
doesthecomputerseepatternsinthenoiseand,inthatway,makemisleadingforecasts?
Iwilltreatthesequestionsinthispaper. ItisareviewwhereIseektoincludevery
recentcontributions. Iemphasizeattemptstofindananswerandtopinpointsituations
whereMLdoesparticularlywellorwhereitdoesnotworksowell. Afrequentcriticism
ofmachinelearningisthatitisablackboxmethod. Nevertheless,cansomethingbesaid
whenitcomestofindingreasonsforitdoingwellinsomesituations,e.g.,beatingsimple
parametricmodels,andnotsowellinothersituations,whereitisbeatenbyothertypesof
models? SeethediscussioninSection4.3andattheendofSection6.
WhatisthepotentialforMLmethodsinthefuture? Arethesemethodsimproving
in quality while parametric models are at a standstill? Moreover, how well can purely
algorithmicMLmethodsbeintegratedintomodelstoalargedegreebasedonphysicsand
non-statisticalfeatures,suchasinweatherforecasting?
Partially, I try to give my review a somewhat personal touch. It is colored by my
research background, which has not been focused directly on forecasting but has been
centeredontopicsclosetotheproblemofforecasting. Hence,Iwilldiscussnonstationarity
andthepatternsofnonstationaritythatarestatisticallyforecastable,suchascointegration.
This has also led to looking at leading lags and Granger causality, as outlined in [3].
In addition, I will mention the possible potential of local Gaussian models presented
in[4,5]. Further,IbrieflylookatGARCH-likestructures,notonlyinvolatilityprediction
forfinancialseries,butinintegertimeseriesmodeling,so-calledPoissonautoregression,
andsimilarrecursiveschemesforcontinuoustimedatadescribedbystochasticdifferential
equationsleadingtotheconnectionwithHawkesprocesses. Thereseemtobeonlylimited
applicationsofMLmethodsinthesecontexts.
Tocompareindividualforecastingmethodsandtypesofmethodsisachallengingtask.
Whatkindofcriteriaormetricsshouldbeused? Anumberofforecastingcompetitions
have been arranged, and I report on some of the main ones in Section 4.4. In most of
these competitions, forecasting accuracy has been used as a yardstick, but then several
measuresofaccuracyexist,andtherankingofmethodsmaydependonthemeasureused.
However,clearly,thereareotherkeymetricsinjudgingforecastingalgorithms,suchas
trainingtime,interpretability,androbustnessagainstnoisydata. Iwillbrieflydiscusseach
ofthesecriteriaforthemethodstreatedinthepresentpaper.
Hereisanoutlineofthepaper:InSection2,ImentiontheHolt-Wintersmodels,which,
in many ways, may be said to have started modern applied forecasting. These models
areintuitive,providegoodresults,andarestillused. Arelated,so-called“θ-model”,has
beendoingwellinforecastingcompetitions. Actually,thismodelwasdeclaredthewinner

Entropy2025,27,279 3of34
oftheM3forecastingcompetition;see[6]. The well-knownARIMAmodels,alsobriefly
discussedinSection2,arerelatedtotheHolt-Wintersmodels. Bothpointforecastsand
intervalforecastscanbeprovidedintheGaussiancaseinparticular.
All of these models are linear (and quite often Gaussian). Section 3 is devoted to
simplenonlinearparametricmodelsandtononparametricforecasting.
Section4is,insomesense,themainpartofthepaper. Here,Idiscussthevarioustypes
ofMLforecasts,suchasthosebasedonneuralnetworksandrandomforest,whicharepos-
siblythetwomaincontendersforsimplerstatisticalmodels. Whataretheirstrengthsand
weaknesses? HowandwhencantheybestrengthenedfurtherbycombiningvariousML
forecastswithclassicstatisticalmodels? Howwelldotheydoinforecastingcompetitions
(coveredinSection4.4)comparedtomoretraditionalmethods? Further,parametricmodels
canbeanalyzedtheoretically. HowaboutMLmethods?
Section5continuesthediscussionofMLmethods. Itreatmultivariatetimeseriesand
panels,nonstationaryeffects,andcointegrationasanalternativeinstrumenttodifferencing
andremovingdeterministictrends. Further,Idiscussforecastingdistributions,including
scores,forecastingcounttimeseriesviaGARCH-typestructures,andanalogsincontinu-
oustimewithpotentialapplicationsinmultivariatefinancialforecastingandcontagion.
Forsomeoftheseproblems,MLmethodsseemlesswelldevelopedthaninforecasting
stationaryone-dimensionalseries.
Finally,inSection6,Ilookatweatherforecasting. Recently,MLmethodshavebeen
introducedatvariousstagesoftheforecastingprocess,sometimeseminentlysuccessful
butatothertimes,afailure. WhatisthefutureofMLforecastinghere? Thisisdiscussedin
lightoftheveryrecentMLmethodsofGraphCastandGenCast.
Idonotgiveanyexplicitforecastingexamplesusingmyownrealdata. Foragreat
numberofsuchexamples,Irefer,instead,tothediscussionandreferencesinSection4.4.
2. ClassicalParametricForecasts
Theearliestforecastingtechniquethatisstillbeingusedisprobablytheexponential
smoothingtechniquebasedonworkin[7,8]. Exponentialsmoothingisanexampleofa
recursivescheme,withsuchschemesbeingextensivelyusedinincreasinglycomplexforms
inmodernnonlinearandMLforecasting. ThebasicideagoesbacktoatleastPoissonasan
extensionofanumericalanalysistechniquefromthe17thcentury,anditwaslateradopted
bythesignal-filteringprocessingcommunityinthe1940s.
Let{y t }beatimeseriesforwhichpredictionsyˆ t+1 attimet+1aresought. Then,the
simplestformofanexponentialsmoothingforecastisgivenby
yˆ t+1 = αy t +(1−α)yˆ t . (1)
By solving recursively, yˆ t+1 is expressed as an exponentially weighted average of the
previousobservationsof{y },fromwhichtheappellationexponentialsmoothingisderived.
t
Theparameterα(0≤ α ≤1)mustbeestimated,usuallyusingleastsquares,andtheinitial
valueyˆ mustbestipulatedby,forexample,takinganaverageoftheearlyvaluesof{y },
0 t
whichareneededforstartingtherecursivescheme.
Simple exponential smoothing does not work well if there is a trend involved. In-
cludingan(instantaneous)trendestimate,{dˆ},resultsinadoubleexponentialsmooth-
t
ingscheme:
yˆ t+1 = αy t +(1−α)yˆ t +dˆ t (2)
dˆ t+1 = β(yˆ t+1 −yˆ t )+(1−β)dˆ t (3)

Entropy2025,27,279 4of34
where α is the data smoothing factor, and β (0 ≤ β ≤ 1) is the trend smoothing factor.
Thesefactorsandtheinitialconditionscanbedeterminedasindicatedaboveforthesimple
schemein(1). Theinclusionofatrendalsomakesiteasiertoforecastseveralstepsahead.
Withthehelpofastudent(PeterWinters),Holtextendedtheschemefurthertocontain
seasonalindices,theHolt-Wintersforecasts,involvingtripleexponentialsmoothing. See
also[9]. Exponentialsmoothingcanbeextendedtomultivariatetimeseries;see[10].
Probablythemostwell-knownclassofparametrictimeseriesistheclassofARIMA
(integratedautoregressivemovingaverage)models. Themajorbreakthroughofthisclass
ofmodelscameintheformofabook[11]. Theauthorsintroduced,inatimeseriescontext,
the classical sequence of statistical modeling: identification, estimation, and diagnostic
checking. TheARIMAmodelsaresowell-knownthatitseemsunnecessarytosaymuch
aboutthemhere,butafewfactswillbementionedforcompleteness. Thesimplestmember
ofthisclassisthepurelyrecursiveautoregressivemodel(themodelsareassumedtohave
azeromean),
y t = a 1 y t−1 +···+a p y t−p +e t , (4)
where a ,...,a are unknown parameters in a pth-order model, and {e } is a series of
1 p t
uncorrelated(ininference,theseareoftenassumedtobeiid(independentidenticallydis-
tributed))variables. Theprocessisstationaryiftherootsofthecharacteristicpolynomial
A(z) = 1−a z−···−a zp are located outside the unit circle in the z-plane. The one-
1 p
step-aheadforecastisgivenbyyˆ t+1 = a 1 y t +···+a p y t−p+1 ,andhigher-orderforecasts
are given by reiterating this equation. The estimation of the parameters is carried out
usingmaximumlikelihoodorquasi-maximumlikelihood,andtheasymptoticconfidence
intervalsandasymptoticdistributionoftheforecastsareeasilyestablishedunderweak
regularityconditions. Theorderisdeterminedbyinspectingtheso-calledpartialautocorre-
lationfunctionorbyusinganAIC-typecriterion.
TheclassofARMA(p,q)modelsisformedbyreplacingthenoiseorinnovationterme
t
withamovingaverageterm,resultingin
y t −a 1 y t−1 −···−a p y t−p = e t +b 1 e t−1 +···+b q e t−q . (5)
Itissomewhatmorecumbersometoobtainparameterestimatesandone-stepormulti-
step forecasts using maximum likelihood or quasi-maximum likelihood, but standard
computerpackagesareavailable,whereforecastconfidenceintervalsarecomputed.
ARMAmodelscanbefurtherextendedtoencompassnonstationarymodelswitha
linearstochasticordeterministictrend. Thisiscarriedoutbyreducingtheseriestoasta-
tionaryseriesbydifferencingtheobservationsuptodtimes,resultinginanARIMA(p,d,q)
model. Often, d = 1issufficient. Themodelscanbeextendedbyincludingaseasonal
componentthat,initself,canbemodeledbyanARIMA-typeprocess. Inthevectortime
seriescase,theARIMAisbasedontheindividualdifferencingofthecomponentseries,
butpresently,thisstructureispredominantlyreplacedbyacointegrationapproach;this
willbebrieflymentionedattheendofSection5.3.
Forecastscanbecomputedusinguncertaintyintervalsfromstandardstatisticalpack-
ages. TheARIMAmodelshavetendedtodowellinforecastingcompetitions. Theyhave
beencomparedtoHolt-Wintersexponentialmodels,butitisnotcorrectthatthesemodels
aremerelyasubsetofARIMAmodels;thisisbecauseHolt-Wintersmodelscontaininstan-
taneousestimatesoftrendsandseasonalcomponents. Thesequantitiesarerecursively
updatedintime,whichisnotthecaseforARIMAmodels.
TheARIMAmodelsareeasilyupdatedtomultivariateseries{y }byreplacingthe
t
scalarparametersa ,...,a andb ,...,b withmatrices. Theidentification,estimation,and
1 p 1 q
validationstepsaremorecomplex. Ausefulreferenceis[12]. Thereareseveralprogram

Entropy2025,27,279 5of34
packagesformoreorlessautomaticallyprocessingmultivariateARIMAmodels(see,e.g.,a
Python3.13packageonforecastingforARIMAmodelsandmoregeneralmachinelearning
forecastsregardingmultivariatetimeseries). Thesemodelscanalsobeallowedtocontaina
possiblemovingaverageexogenousvariable,x ,inadditiontothemultivariateinnovation
t
term e . These are the so-called ARIMAX models. Again, forecasts with uncertainty
t
intervalscanbeobtainedfromprogrampackages.
ThewinneroftheMakridakisM3[6]forecastingcompetitionwasaforecastobtained
usingtheso-calledθ(theta)method. Themethodwasintroducedin[13]. Itismuchmore
completelydescribedinthemonograph[14]. ItcanbeseenasageneralizationofHolt-
Winters-typemodels. Thechoiceofweightparametersandthenumbersoftrendfunctions
(andtheirnature)hasbeenresearchedextensively;thisisreflectedin,e.g.,Ref.[15],ina
comparisonwithmachinelearningforecasts.
Inthegeneralliteratureonthetamodels,therearetwostrands. Thefirstonegives
probabilisticpropertiesofthemethod, startingin[16]; subsequently, anumberoftheo-
reticalresultswascollectedin[14]. Thelatterprovidesacompleteanalysisofthetheta
methodunderaunitroot-generatingprocess,explainingitssuccessintheM3Makridakis
competitionin2000[6]. TheauthorsofRef. [14]alsointroducedthemultivariatetheta
methodandlookedatitsrelationshiptocointegration.
Thesecondstrandexpandsanddetailsvariousimplementationsofthemethod,opti-
mizingthetamodelsandpointingouttheirrelationshipwithstatespacemodels(see[17]).
Arecentgeneralizationofthethetamethodisgivenin[18]. Connectionstoadaptive
learningforecastswerepursuedin[19].
Theconnectionofthethetamethodtotheperhapsmorewell-knownclassofstatespace
modelspromptsashortmentionofthestructureofthelatter. Infact,statespacemodels
areverypowerfulandversatiletoolsforworkingwithtimeseriesandtheirforecasting.
Theywereinitiallydevelopedbyengineersbuthavebeenwidelyadoptedandextended
amongotherapplicationstoeconometrics. Twocentraltextbooksare[20,21]. Statespace
modelsareformulatedbymeansoftwodifferentequations: anequationintermsofthe
states,{α },whichareasetofvariablesthatareusuallyunobserved. Typicalexamplesare
t
trends,seasonalcomponents,ortime-varyingparameters. Thestateequationdescribes
the dynamic law governing the states for two adjacent points in time. The second is
the observation equation, which specifies the relationship between observed data and
unobservedstates. AlinearGaussianversionofsuchasystemcouldlooklikethis:
α t+1 = T t α t +Γ t +R t η t , η t ∼ N(0,Q t ) (6)
y = E α +D +C ε ε ∼ N(0,H ) (7)
t t t t t t t t
withtheinitialconditionα ∼ N(α ,P ). Intheseequations,η andε arethestateand
1 0 0 t t
observationalvectorsofzero-meanGaussiannoises. ThematricesT ,Γ ,R ,Q ,E ,D ,C ,
t t t t t t t
andH aretheso-called(generallytime-varying)systemmatrices,andα andP arethe
t 1 1
initialstateandstatecovariancematrix,respectively.
Oncesuchasystemisfullyspecified,thecoreproblemistoprovideoptimalpredic-
tionsofstatesandtheircovariancesovertime. Thiscanbecarriedoutbylookingbackin
timeusingthewell-knownKalmanfilter.
Givenanysetofdataandaspecificmodel,thesystemisnotfullyspecifiedinmost
casesbecausethiswoulddependonunknownparametermatrices. Anestimationofsuch
parametersissought,carriedoutusingmaximumlikelihooddefinedbypredictionerror
decomposition[20].
Amorerecenttextbookis[22]. Theforecastingaspectiscoveredin,e.g.,Ref.[23].

Entropy2025,27,279 6of34
ConcerningthekeymetricsmentionedintheIntroduction,theclassicalparametric
forecastingmethodsreportedinthepresentsectionmustbesaidtobeeasytointerpret,
possiblywiththeexceptionofthetheta-typemodels;see[15,24]forasimplificationand
rephrasing of the model in terms of more understandable terms. The training of the
parametricmodelsconsistsofestimatingtheparameters. Thisisverysimplycarriedout
forunivariatemodels,whereashigh-dimensionalARIMAmodelsandstatespacemodels
wouldrequiremoreeffort. Usually,parametricmodelswouldcontainasafeguardagainst
overfittingbyusinganAIC-typecriterionorapenaltyfactor,thuslimitingthenumberof
allowedparameters. Classicalparametricmodelshavehighaccuracyforforecastingin
linearmodels,butitisnotdifficulttofindnonlinearmodelswheretheyfailcompletely.
3. NonlinearandNonparametricForecasts
Up to now, I have been mostly concerned with linear and often Gaussian models.
A claim of the ML methods is that (at least sometimes) they are capable of handling
nonlinearities better than classical parametric models. This means that, in a sense, ML
methods try to capture more of the probabilistic structure of the data. In comparison,
ARIMA models are based solely on statistical moments, e.g., the covariance structure.
ThisisfineifthedataareGaussian,butinthenon-Gaussiancase,onewouldexpectthat
informationmayhavebeenlost.
BeforeIgoovertothemainthemeofthispaper—theconstructionofMLmethods,
includingtheirclaimedabilitytohandlenonlinearitiesinabetterway—itisinstructive
totakealookatclassicalparametricnonlinearmodels,includingalookattheclassical
nonparametricmethodology.
Tomakethingssimple,Iconcentrateonthefirst-orderscalarmodel,whereonlyone
lagisincluded. Goingfrommodeltoforecastisthentrivial.
Themostpopularnonlinearmodelisprobablythethresholdmodelintroducedin[25].
Initssimplestform,itisgivenby
y t = θ 1 y t−1 {s t−1 ≤ c}+θ 2 y t−1 {s t−1 > c}+e t . (8)
Theprocessmovesasamixtureoftwoautoregressiveregimes,withautoregressive
coefficients θ and θ , respectively. Theregimeisdeterminedbythestateprocess, {s },
1 2 t
andathreshold,c. Whens t−1 ≤ c,itmovesaccordingtoθ 1 whens t−1 > caccordingtoθ 2 .
Thestateprocess,s t ,maybeequaltoy t−d foracertaindelay,d. Aninferencetheoryforthe
thresholdprocessisgivenin[26].
Therearenumerousgeneralizationsandapplicationsofthethresholdmodel;see,e.g.,
Refs.[27,28]. Usually,athresholdprocessisassumedtobestationary. Foranonstationary
cointegration-typethresholdprocess,see[29]. Forarecentpaperthatcoverstheuseof
thresholdsinneuralnetworks,see[30].
Thethresholdmodelissometimescriticized,perhapsespeciallyineconometrics,forits
abrupt change between regimes. There is a class of models with continuous transition
between the θ and θ regimes, the so-called STAR models (smooth transition models).
1 2
IntheLSTARmodel,thetransitionismodeledbyalogisticfunction,
y t = (θ 1 +θ 2 G(γ,c,s t−1 ))y t−1 +e t (9)
withGhavingthelogisticform
G(γ,c,s t−1 ) = (1+exp{−γ(s t−1 −c)})−1, γ >0. (10)

Entropy2025,27,279
7of34
Alternatively,anexponentialform,ESTAR,canbeused:
|     |     | G(γ,c,s |     | ) =1−exp{−γ(s |     |     | −c)2} | γ >0. | (11) |
| --- | --- | ------- | --- | ------------- | --- | --- | ----- | ----- | ---- |
|     |     |         | t−1 |               |     |     | t−1   |       |      |
Anearlierversionofthesemodelswasintroducedin[31]. Later,theauthorofRef.[32]
definedafamilyofSTARmodelsthatincludedboththeLSTARandESTARmodelsand
devisedadata-drivenstrategywiththeaimof,amongotherthings,helpingtheuserchoose
betweenthesetwoalternatives. Anumberofgeneralizationsofthesimplemodels(10)
| and(11)exist. | Anupdatecanbefoundin[33]. |     |     |     |     |     |     |     |     |
| ------------- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ThelastclassofparametricnonlinearmodelsisthehiddenMarkovchainautoregres-
siveprocess. Incontrast,forthethresholdmodelsandtheSTARmodels,thestateprocess
=
istypicallygivenbys t y t−d ,adelayoftheobservedprocess,inthehiddenMarkovchain
| autoregressiveprocess. |     |     | {s }isaMarkovchainsothat |     |     |     |     |     |     |
| ---------------------- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |
t
|     |     |     |     |     | y = s | y       | +e  |     |     |
| --- | --- | --- | --- | --- | ----- | ------- | --- | --- | --- |
|     |     |     |     |     | t     | t−1 t−1 | t , |     |     |
where,inthesimplestcase,s t ,canonlytaketwovalues,θ 1 andθ 2 ,say,andwheres t varies
betweenthesetwovaluesaccordingtoa2×2Markovtransitionmatrix. Bothθ andθ
1 2
andtheentriesintheprobabilitytransitionmatrixareunknownandhavetobeestimated.
TheEMalgorithmisoftenusedforthistask[34]. Additionally,themeanandvarianceof
theseriescouldbethesubjectofMarkovregimeshifts[35];seethemorerecenttextbook
referencealso[36].
Foralloftheseclassesofprocesses,itispossibletodoasymptoticinferenceonthe
parameters,andasymptoticconfidenceintervalscanbesecuredundercertainregularity
conditions. Inprinciple,thesecanbetransferredtoasymptoticuncertaintyintervalsforthe
forecasts. However,itseemsmoredifficulttoproduceadistributionaltheoryofforecasts,
unlikethenonparametricmodelsexaminednext.
Thewell-knownkerneldensityestimateforthemarginaldensity, p(y),ofastationary
| timeseries,{y | },givennobservationsy |     |     |     | ,...,y |     | ,isgivenby |     |     |
| ------------- | --------------------- | --- | --- | --- | ------ | --- | ---------- | --- | --- |
|               | t                     |     |     |     | 1      |     | n          |     |     |
n
∑
|     |     |     |     | pˆ(y) | =   | K   | (y −y), |     |     |
| --- | --- | --- | --- | ----- | --- | --- | ------- | --- | --- |
|     |     |     |     |       |     | h   | t       |     |     |
t=1
h−1K(h−1(·)).
where K(·) is a kernel function, h is the bandwidth, and K (·) = Un-
h
dernonrestrictiveconditions,consistencyandasymptoticnormalitycanbeproved. Itis
well-knownthattheoptimal(withrespecttoleastsquaresdeviation)predictoryˆ isgiven
t+1
bytheconditionalmeanofy ,giventhepastvalue. Theconditionalmeanm(y |y)of
|          |                                                   |     | t+1  |       |        |      |           | t+1  |     |
| -------- | ------------------------------------------------- | --- | ---- | ----- | ------ | ---- | --------- | ---- | --- |
| y giveny | = ycanbeestimatedusingtheNadaraya-Watsonestimator |     |      |       |        |      |           |      |     |
| t+1      | t                                                 |     |      |       |        |      |           |      |     |
|          |                                                   |     |      |       |        | ∑    | (         | − y) |     |
|          |                                                   |     |      |       |        | s ≤t | y s K h y | s− 1 |     |
|          |                                                   |     | mˆ(y | |y    | = y) = |      |           | .    |     |
|          |                                                   |     |      | t+1 t |        | ∑    | K ( y     | − y) |     |
|          |                                                   |     |      |       |        |      | s≤t h     | s    |     |
Thiswillalsobeanestimateoftheoptimalpredictorifthepastofy canberepresented
t+1
byy ,e.g.,inthepossiblynonlinearautoregressiveAR(1)casey t+1 = g(y )+e forsome
| t   |     |     |     |     |     |     |     | t t     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
|     |     |     |     |     |     |     | =   | g(y )+e |     |
function,g. InthecaseoftheAR(p)processwithy t+1 t ,...,y t−p t ,thefunctiong
canbeestimated,andconsequently,y
t+1 canbeforecasted,butonequicklyrunsintothe
| curseofdimensionalityas |     |     | pincreases. |     |     |     |     |     |     |
| ----------------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
To avoid the curse of dimensionality, one can use an additive model, where it is
| assumedthatg(y |     | ,...,y | p ) = | g (y )+···+g |            | p (y | p ),resultinginamodel: |     |     |
| -------------- | --- | ------ | ----- | ------------ | ---------- | ---- | ---------------------- | --- | --- |
|                |     | 1      |       | 1 1          |            |      |                        |     |     |
|                |     |        | y     | = g          | (y )+···+g |      | (y                     | )+e |     |
|                |     |        | t+1   |              | 1 t        |      | p t−p                  | t   |     |

Entropy2025,27,279 8of34
forsomecomponentfunctions,g ,...,g . Themodelcanbeestimatedbyso-calledback-
1 p
fitting,whichisthoroughlyexplainedin[37]. Thereareextensionstomodelswithmild
formsofinteractionsbetweenthecomponents;see,e.g.,Ref.[38]. Therelevantvariables
canbeselectedbyusingthelassoroutine,asexplainedin[39].
Theconditionalmeanforecastisoptimalintheleastsquareserrorsense,butitshould
benotedthattherearealternativemeasuresoferrorforforecasting,whichare,infact,often
usedaserrormeasuresincomparingforecastsandforecastingcompetitions. Themost
used are the mean absolute error (MAE) minimized by the median and mean absolute
percentageerror(MAPE).Foradiscussionoftheseandrelatedtopics,Ireferthereader
to[40].
Nonlinearparametricmodelscertainlyhaveanadvantageifthedataarenonlinearly
generated,but,ofcourse,theyloseouttolinearmodelsifthedataarelinearlygenerated.
Ingeneral,thedangerofoverfittingincreaseswithnonlinearmodels,ascanbeseenwith
far worse examples ofout-of-sample forecasts. The training (estimating ofparameters)
naturally takes longer due to the more involved estimation algorithms. These may be
iterative,anditisnotalwaysobviouswhentheiterationshouldbestopped. Often,when
theyareregression-typemodels,theyareusuallynotdifficulttointerpret.
Thenonparametricforecastingalgorithmsarebasedonestimatingtheconditional
meanandare,therefore,easytointerpret. Theirscalabilityisaproblemduetothecurseof
dimensionalitybutcanpartlybeavoidedusingsimplificationssuchasadditivemodels.
4. MachineLearningForecasts
AsemphasizedintheIntroduction,tobeabletomakeforecasts,itisnecessarythatan
observedpatternhasfeaturesthatarepreservedintimewhenmovingintotheforecasting
period.Sincewearedealingwithtimeseries,thisseemstorequiresomekindofstationarity
in the series. However, the strictness or wide-sense stationarity of the series is not an
absoluteprerequisite. Multivariatetimeseriesmaybenonstationary;nevertheless,itmay
bepossibletoforecastifthereisatime-invariantpatterngoverningthenonstationarity,
forexample,viacointegration,wherethereisoneormoretime-invariantlinearcombination
oftheseries,whichresultsina(possibly)multivariatestationarytimeseries.
Foraunivariatetimeseries,therecouldbealinearstochastictrend,whichmaybe
removedbydifferencing,ortherecouldbeapossiblynonlineardeterministictrend,which
mayberemovedbyaregressiondevice. Moreover,heterogeneitymayberemovedusing
a Box-Cox-type transformation [41]. In a local Gaussian approach, further analysis is
facilitatedbytransformingtheseriesintoaGaussianseries;see[4].
A Gaussian AR series is the series that is easiest to handle regarding prediction;
everythingisbasedontheautocorrelationfunction,andtheoptimalleastsquaresforecast,
theconditionalmean,islinearandcanbeexpressedintermsoftheautocorrelationfunction,
which,inturn,givesacompletedescriptionoftheprobabilitystructureintheGaussiancase.
Akeyaspectoftheautoregressiveprocessisitsrecursivedefinition,whereforecasts
can be obtained easily by regressing using the series itself, and forecasts with a more
distanttimehorizoncanbebuiltuprecursively. Therecursivepropertycanalsobebuilt
upfortheARMAandARIMAseriesand,asseeninSection2,forexponentialsmoothing
models using Equations (2) and (3). The recursive mechanism can also be extended to
seasonalforecasts.
Fornonparametricandnonlinearforecasts,similarbutmorecomplicatedrecursive
mechanismsmay,inmanycases,bereliedon.
Common to all of these mechanisms and a prerequisite for them to work well is a
trainingperiod,wherethemodelisbuiltupbyidentification,estimation,anddiagnostic
checking,notonlyintheARIMAcasebutalsofortheexponentialsmoothingmodels.Inthe

Entropy2025,27,279 9of34
trainingperiod,theparametersneedtobeestimated,andthisissimilarwhenregarding
nonlinearparametricmodels. Thenonparametricmethoddoesnotcontainparametersas
such,butthenumberoflagsandthebandwidthneedtobedetermined.
Formachinelearningmethodstobedealtwithregardingthissection,thetrainingis
absolutelyessentialandis,inmanyways,thecentralconceptofthemethodology;thisis
notonlyusedforforecasting;itisusedingeneralwhenfindingapatternthatdescribesthe
dataandwherethispatterncanberecognizedandusedintheanalysiswhennewdataare
comingin. Thereareseveralwaysofdoingthis,butIwillconcentrateontwomethods:
neuralnetworkanalysisandrandomforest,whichseemtohavebeenthemostsuccessful
machinelearning(ML)forecastingmethods.
4.1. ForecastingUsingArtificialNeuralNetworks
Neuralnetworksareusedforanumberofproblemsinprediction,classification,and
clustering. Thesuccessandimpactofneuralnetwork-likeapproachesinmachinelearning
haverecentlybeenrecognizedbythe2024NobelPhysicsPrizeawardedtoJohnHopfield
andGeofferyHinton. Currently,thereisintenseactivityinthisfield,nottheleastinso-
called deep neural network modeling. These are networks with several hidden layers.
Adetailedsurveyofdevelopmentsupto2015isgivenin[42].
I start with a single-layer network. Assume a given data vector, x, which may be
thoughtofasasectionofatimeseries, {y ,...,y }. Inaneuralnetworkapproach,one
1 t
isinterestedintransformingxvialinearcombinationsofitscomponentsandanonlinear
activation function, often of sigmoidal form, of the linear combinations. These linear
transformationsrepresentwhatiscalledahiddenlayer.
Thefirststepinconstructingthehiddenlayeristoformlinearcombinations:
n
∑
h = w + w x
i 0 ij j
j=1
and then possibly subject these terms to an activation function. In the case of just one
hiddenlayer,anoutputlayerintermsofthehiddenlayerisgivenby
m
∑ ′
z = w h
i ij j
j=1
followedbyanotherpossiblynonlinearfunction,dependingontheproblem. Ithasbeen
shown, e.g., Ref. [43], that this system of linear combinations and activation functions
is able to approximate general classes of functions. In a s-step time series forecasting
problem, the output may successively be built up to obtain the forecast yˆ t+s at step s
′
from the input set {y ,...,y }. When using a training set, the weights w and w are
1 t ij ij
determinedbyminimizingalossfunctioninvolving(y t+s ,yˆ t+s ),whereyˆ t+s isbasedonthe
outputlayer. Theerrorfunctionisevaluatedforeachofthesamplescomingintheinput
window. Subsequently,theoutputofthegradientoftheerrorfunctionwithrespecttoy t+s
isevaluated,andtheweightsarerecomputedandupdatedinthedirectionofthegradient
′
usingstochasticgradientdescent. Theweightsw fortheoutputlayerarecomputedfirst.
ij
Then,w isadjustedviathechaindifferentiationruleusingso-calledbackpropagation.
ij
The simple, one-hidden-layer forward scheme has met with considerable success.
Applicationssuchastheembeddingofgraphsandtextprocessingaredescribedin[44],
with emphasis on the work carried out in [45,46]. However, it has turned out that in
manyproblems,includingforecasting,improvedperformancecanbeobtainedusingdeep,
multiple-layernetworks,wherethelearningprocessiscalleddeeplearning.

Entropy2025,27,279 10of34
Aprimeadvantageofdeeplearningisthathiddenunitscanbeconnectedtoeachother
recursivelyintime. Thisistakenupamongseveralothersourcesintheliteraturein[47].
They consider a somewhat extended multivariate, one-step-ahead forecast framework,
whereforcomponenti,
yˆ i,t+1 = f(y i,t:p ,x i,t:q ,s i ) (12)
where y i,t:p = {y i,t ,...,y i,t−p }, and x i,t:q = {x i,t ,...,x i,t−q } are exogenous variables of
componentioverthelook-backwindowoflength p;s representsstaticmeta-data,e.g.,the
i
location of a meteorological station, for climate data. The function f is the prediction
functionlearnedbythemodel. Itcontainsweightfunctionsandhiddenunitsofthehidden
layers,which,aswillbeseenbelow,canbechoseninvariousways.
Convolutionneuralnetworks(CNNs)and(TCNs): Convolutionneuralnetworks
(CNNs)[48]wereoriginallydesignedforspatialdata;however,theyhavebeenadapted
toatimeseriessituation. Foranintermediatelayer,l,eachconvolutionisacausalfilter.
Intermsofhiddenvectorunits,ittakestheform
h ℓ = A((w⋆h)(ℓ,t)) (13)
t
withtheconvolutionbetweenweightsandhiddenunitsgivenby
p
(w⋆h)(ℓ,t) = ∑ w(ℓ,τ)h ℓ .
t−τ
τ=0
In(13),hℓ isanintermediatestateatlayerℓ,andwisafixedmatrixofconvolutionweights
t
atlayerℓ. ThefunctionAisanactivationfunction,e.g.,asigmoidalfunction.
In a time series context, convolution neural networks are often named temporal
convolutionalnetworks(TCNs). ThecontrastwiththespatialCNNsmainlyconsistsof
theirfocusonthedatatypesandthestructureoftheirconvolutionallayers. Inparticular,
TCNsemploytemporalanddilatedconvolutionstocapturemorelong-rangedependencies
andcomplextemporalpatterns,whereasCNNsusespatialconvolutionstodetectlocal
patternsandfeaturesinimages.
A basic TCN publication is [49], which is concerned with action segmentation in
computervision. TheTCNalgorithmhasbeencomparedtootherrecurrentnetworkslike
RNNandLSTM,whichwillbetreatednext. AnadvantageofTCNsisthat, duetothe
parallelnatureoftheconvolutions,theycantrainfasterandmoreefficientlythanLSTMs.
ExamplesofcomparisonsofforecastingpotentialforTCN,RNN,andLSTMare[50,51].
TheoutcomeoftheseinvestigationsandsimilarexperimentsisthatTCNscancompeteon
parwithRNNandLSTM,butthissomewhatdependsonthedatatype.
Asingle,causalCNNlayerisequivalenttoanautoregressivemodel.
Recurrentneuralnetworks(RNNs):Recurrentneuralnetworks(RNNs)donotrequire
anexplicitfixedlook-backwindow,asisthecaseforCNNs.Giventhenaturalinterpretation
oftimeseriesforecastsassequencesofinputsandtargets,manyapplicationsfortemporal
timeseriespredictionhavebeendeveloped[52–54].Attheircore,RNNcellunitscontainan
internalmemorystate,whichactsasacompactmemoryofpastinformation. Thememory
stateisrecursivelyupdatedfromnewobservationsateachtimestep.
Recurrentneuralnetworkswereoriginallybasedonworkinthe1980s. Sincethen,
a number of different RNN architectures have been developed. Just to give a flavor of
thesenetworks,Ipresentthemodelequationsforthethree-layer(onehiddenlayer)Elman
network. Theyare
h t = σ h (W h x t +U h h t−1 +b h ), (14)
z = σ (W h +b ) (15)
t z z t z

Entropy2025,27,279 11of34
where x isaninputvector, h isahiddenlayervector, z isanoutputvector, W and U
t t t
areparametermatrices, bisaparametervector,andσ andσ areactivationfunctions.
h z
Equations(14)and(15)showtherecursivestructureofthenetwork.
TheElmannetworkandthesimilarJordannetworkareknowntobesimplerecurrent
networks(SRNs). Thereexistconsiderablymorecomplicatedrecurrentnetworkswitha
numberoflayersthaninCNNnetworks,buttheideaofrecursionintimeiskept.
Longshort-termmemory(LSTM)recurrentnetworks: Thelong-termgradientsthat
arebackpropagatedinclassicRNNscantendtozeroorexplode. Theproblemiscompu-
tational. Theso-calledlongshort-termmemory(LSTM)recurrentnetworkisdesignedto
counterthisproblem. LSTMunitspracticallysolvethevanishinggradientproblembecause
LSTMunitsallowgradientstoflowunchanged. LSTMcanstillsometimessufferfromthe
explodinggradientproblem.
ThevanishinggradientproblemwasfirstanalyzedinadiplomathesisbySeppHochre-
iterattheTechnologicalUniversityofMünchenundertheguidanceofSeppSchmidhuber.
Afterhavingbeenpublishedasatechnicalreportandasaconferenceproceeding,thefull
LSTMpaperappearedin1997inNeuralComputation[55]. Sincethen,therehavebeen
substantialandappliedadvancesregardingthemethod. Now,theoriginalLSTMpaper
standswithaheftycountofmorethan67,000citations. Thepaperhasbecomethemost
cited neural network article of the 20th century, and it has been applied with consider-
ablesuccesstotopicssuchasunsegmented,connectedhandwriting,speechrecognition,
machine translation, robot control, video games, and healthcare. LSTM is particularly
well-suitedtoclassifying,processing,andmakingpredictionsoftimeseriesdatasincethere
canbelagsofunknowndurationbetweenimportanteventsintimeseries.
AcommonLSTMunitiscomposedofacellunit,aninputgate,anoutputgate,anda
forgetgate. Thecellremembersvaluesoverarbitrarytimeintervals,andthethreegates
regulatetheflowofinformationintoandoutofthecell.
Transformers:In2017,apaperwiththeendearingtitle“Attentionisallyouneed”[56]
waspublished. “Attention”ishereatechnicalmachinelearningtermreferringtoamethod
thatdeterminestherelativeimportanceofeachcomponentinasequencerelativetothe
othercomponentsinthatsequence. Thetermhasitsorigininnaturallanguageprocessing,
withtheimportancebeingrepresentedbyassigningweightstoeachwordinasentence
(moregenerally,attentionencodesvectorscalledtokenembeddingsacrossafixed-width
sequencethatcanrangefromtenstomillionsoftokensinsize). Thetitleofthe[56]paper
refers to the fact that the authors were able to do away with the recursive structure of
machinelearningmethodslikeRNNandLSTMandbuildonlanguageprocessingconcepts
instead. This meant that parallelization could be implemented with enormous savings
inprocessingtimeandcouldalsobesaidtolaythefoundationforartificialintelligence
routineslikeChatGPT.
Themethodologypresentedin[56]hasrecentlyhadaverybigimpact. Thismodelofa
neuralnetworkthatlearnscontextand,thus,meaninginsequentialdata,likethewordsin
asentence,hasbeennamedthetransformermodel(withtheaddedfactthattransformers
canuseparallelprocessingtoincreasespeed). Transformersare,inmanycases,replacing
convolutionalandrecurrentneuralnetworks(CNNsandRNNs)asthemostpopulardeep
learningmodels. Indeed, 70percentofarXivpapersonAIpostedinthelasttwoyears
mentiontransformers. Oneexampleoffurtherdevelopmentofanaspectoftransformer
methodologyis[57].
Thetechnologyis,inprinciple,validforanysequenceofdata,includingtimeseries
andmolecularsequencesandtheirapplicationinmedicine,leadingtoalargegrowthinuse
inanumberoffields. Thestructureoftransformersalsoallowsthemtobeabletomodel
long-rangedependence[58];see[59].

Entropy2025,27,279 12of34
Iwillreturntotransformerforecastinginthesectiononweatherforecasting—Section6.
4.2. RandomForestandGradientBoosting
RandomforestandgradientboostingseemtobethemainMLcompetitorstoneu-
ral network-based models in forecasting. Both of these methods can be used both for
classificationand prediction. Theyaredescribedwell inchapters10, 15, and 16in [60].
Bothofthesemethodsarerandomtreemethodsandusebootstraprealizationsefficiently
toformnewtrees. Randomforestusesaveragesofforecastsgeneratedbyindependent
bootstrap-generatedtreesandcanberuninparallel. Gradientboostingrunssequentially,
wherethenewtreemodelissoughttocorrecttheerrorsofthepreviousone.
The procedure of random forest is a special case of a bagging procedure, where
a final predictor or classifier is obtained by using the average of predictors/classifiers
obtainedbybootstrappingtheoriginaldataandcreatingaregressiontreeandaforecast
foreachbootstraprealization. Ablockbootstraphastobeusedintimeseriesforecasting.
Theadvantageofthis“ensembleaveraging”liesinthepossiblevariancereductionintaking
averages. Thevariancereductionislargestifthebootstrappedtreesareindependent. Inthe
randomforestalgorithm,onetriestoreducedependencebyusingarandommechanismin
thegrowthofeachbootstraptree.
Forforecastingpurposes,thetreestructureusedisregressiontrees. Therangeofthe
explanatoryvariablesisrandomlysplitintoregions(sequentially)intime;whenthetree
isfullygrown,thepredictedvalueforeachsub-region(possiblyobtainedusingseveral
splits)isgivenbyaconstantdeterminedbyaleastsquaresalgorithmonthetrainingsetfor
eachbootstraprealizationofthedata. Thefinalpredictedvalueforagivenvalue,x,ofthe
explanatoryvariablesisthenobtainedbytakingtheaverageoftheregionalizedvaluesfor
theregionsxbelongstoforthevariousbootstrappedtrees. Sincethebootstraprealizations
canberunandworkedoninparallel,efficientcomputationtimemaynotbetoolong,even
foralargenumberofbootstraps.
Where the point of random forest is variance reduction, the purpose of gradient
boosting is more directed towards bias reduction. Again, the aim is to obtain suitable
regressiontrees. However,inthiscase,thebootstraprealizationsarenotjustruninparallel.
Now,aregressiontreeissoughtbycorrectingthepredictionerrorinthetrainingperiod
ofthepreviousregressiontree. Thisisasequentialprocedure,anditiscontinueduntil
theentirevalidationpartofthetrainingdatasetisaccuratelypredictedorapredefined
maximumnumberofmodelsisreached.Duringthisprocess,theweightoftheoriginaldata
pointsischangedsothatpointsthatareincorrectlypredictedaregivenmoreweight. Inthis
way,anadaptiveboostingprocedureisconstructed. TheauthorsofRef.[61]developed
thefirstversionofAdaBoost,andtheyreceivedtheprestigious2003Gödelprizefortheir
work. Comparedtorandomforest,theresultsofgradientboostingaremoresensitiveto
parametersettingsduringtraining. However,usingthecorrectparametersettings,theuser
expectstoobtainbettertestresultsthanrandomforest.
The sequential procedure involved in gradient boosting may make the procedure
impracticalifalargesetofdatawithmanybootstrapgenerationsisinvolved. Approximate
methods and more time-efficient algorithms, e.g., the so-called light-GBM, have been
suggested;see,inparticular,[62].
4.3. XAI
Thereareanumberofreportsonthegeneralscalabilityofmachinelearningalgorithms;
see,e.g.,Ref.[63]. Thesameisthecasefortheorderoftrainingtimesrequired;atableis
givenin[64].

Entropy2025,27,279 13of34
ThereareotherMLmethodsthatcanbeappliedtoforecasting: supportvectorma-
chines,ridgeregression,andthelassoprocess. Thelatterincludesregularizationtermsto
avoidoverfitting. Itisclaimedthatanensemblemethodlikerandomforestitselfavoids
overfitting by using the ensemble operation. Much more details can be found in [60].
Abriefoverviewoftheoverfittingproblemiscontainedin[65].
Asismentionedrepeatedlyinthispaper, thelargestproblemofmachinelearning
methods is their black box nature. Both neural network and random forest prediction
algorithms produce forecasts, but they are not simply expressible in terms of theinput
variables (features) of the model. It is understandable that skepticism arises towards
machine learning when it is difficult to understand or (intuitively) explain how each
featurecontributestothemodel. Thesituationisverydifferentfromforecastsformedfrom
generalizedlinearregressionmodels,whereonecanfindanaturalmeasureofhoweach
inputvariablecontributestotheforecast. Isitpossibletofindsimilarmeasuresforthe
contributionofeachinputfeatureinamachinelearningcontext?
Work on this problem has actually started and has, in fact, spawned a whole new
discipline: “Explainableartificialintelligence”,XAI,wheretheaimisto“explain”black
boxmodels. Arecentsurveyofthisfieldisgivenin[66],wheretheproblemisdiscussed
broadlyandpartlyfromaphilosophicalpointofview. Therearealsopapersdevotedtothis
probleminspecialresearchareas,e.g.,openingtheblackboxinapplicationsingenetics,
suchasin[67],wherethreegeneraltechniquesarebeingusedtoprobethekindsofchanges
in the output are being caused by the alternative weighting of structures in the model.
Sensitivity analysis can be used to examine the effects of modifying the input features.
Themodelin[68],whichistreatedinSection5.3,wastestedbyundergoingsuchsensitivity
analyses. Afinalstrategymentionedin[67]isthesurrogatestrategy,wheretheblackbox
modelissoughttobereplacedbyasimpler,moreinterpretablemodel,whichstillprovides
agoodapproximation.
Therearealsotechniquesthatseektoattributeaconcretevaluetotheimportanceof
eachinputfeature,thusconstituting,inasense,ageneralizationoftheimportancemeasure
ofeachinputvariableinageneralizedlinearregressionmodel. Themostusedtechnique
isprobablytheSHAPvalue,whichisrelatedtotheShapleyvalueincompetitivegames.
TheShapleyvaluewasintroducedbyLloydShapleyin1951,see[69],forwhichhewas
laterawardedtheNobelPrizeineconomics. Toputthisintoourpresentcontext(asin[70]),
letFbethesetofallfeatures. TheShapleymethod,inprinciple,requiresretrainingamodel
onallfeaturesubsets,S ⊆ F. Themethodassignsanimportancevaluetoeachfeature,i,
thatrepresentstheeffectofthemodelpredictionofincludingthatfeature. Tocomputethis
effectfortheithfeature,amodel, f S∪i ,istrainedwiththatfeaturepresent,andanother
model, f ,istrainedwiththefeaturewithheld. Thesepredictionsfromthetwomodels
S
are compared to the current input forming the difference f S∪i (x S∪i )− f S (x S ), where x S
representsthevaluesoftheinputfeaturesinthesetS. Sincetheeffectofwithholdinga
featuredependsontheotherfeaturesinthemodel,theprecedingdifferencesarecomputed
for all possible subsets, S ⊆ F−i. The Shapley values are then computed and used as
featureattributions(importance). Theyareweightedaveragesofallpossibledifferences
∑
|S|!(F−|S|−1)!
ϕ i = [f S∪i (x S∪i )− f(x s )]
F!
S⊆F−i
where|S|isthenumberofelementsinS.
In[70](alsosee[71]),theShapleyvaluesareintegratedinanadditiveregression-type
frameworktocreateSHAPvalues(SHapleyAdditiveexPlanations). Thisframeworkalso
servesasacommonframeworkforfiveotherexplanationmodels,withLIME(localinter-
pretablemodel-agnosticexplanations)describedin[72]amongthem. Somestabilityissues

Entropy2025,27,279 14of34
arehighlightedin[73]. Basedontheunificationattainedin[70],theauthorsindicatethat
thenewmethodsshowimprovedcomputationalperformanceand/orbetterconsistency
withhumanintuitionthanpreviousapproaches. Asanexampleamongnumerousappli-
cationsofSHAPinexplainingmachinelearningmodels,realhospitaldataareexamined
in[74].
Itshouldberemarkedthattheaboveexamplesmarkonlythebeginningoftheproblem
ofopeningtheblackboxformachinelearningmodels. ArathercriticalevaluationofXAI
iscontainedin[75]. Moreover,ratherlimitedattentionhasbeengiventothisissueinthe
forecastingcompetitionstreatedinthenextsubsection. Onereasonforthisisprobablydue
totheratherlateappearanceofXAImethods. Thereissurelyaneedforcompetitionsthat
compareXAIpossibilitiesforvariousmodels.
4.4. Statisticalvs. MLMethods: EvidencefromForecastingCompetitions
Anumberofforecastingcompetitionshavebeenarrangedtofindthe“best”forecasts
and to evaluate statistical forecasts against ML forecasts and simple models vs. more
complicatedones. SpyrosMakridakis,inparticular,hasorganizedanumberofforecasting
competitions, starting in 1982 with the M1 competition and then continuing with the
M2–M6competitions,withtheresultspublishedin1982,1993,2000,2020,2022,and2024
(see below for exact references). The scope has been somewhat varied, and so has the
numberofparticipantsandthenumberandversionsofmethodsrepresented. Forthemost
recentones,majorMLandstatisticalmethodshavebeenincluded. IntheM1competition,
the number of time series sought to be predicted was 1001; in M3, it was 3003, and
in M4, it was 100,000. A history of forecasting competitions up to 2020 is given in [76].
Theforecastingcompetitionsdescribedbytheforecastorganizersthemselvescanbefound
in[6,77–81].
ThegeneraltendencyinthecourseofthesecompetitionsisthatMLmethodshave
beenmoresuccessful. Inthefirstcompetition,simplestatisticalmodelsoftheexponential
smoothing type did better than the more complex ARIMA models. In M3 in the year
2000,severalMLmethodsdidpartake,butthewinnerwasthethetamethoddescribed
in Section 2, a relatively simple parametric extension of exponential smoothing -type
models. TheM1–M3competitionshadarelativelysmallnumberoftimeseriesavailable
for prediction. The M4 competition represented a very significant extension, featuring
100,000timeseries,anditisalso(todate)thecompetitionwiththemostgeneraltypesof
series;itwasalsothefirstwherepredictionintervalswereevaluatedinadditiontopoint
forecasts. Itseemsreasonabletogiveabriefreviewofthatcontest. Thetimeseriesdiffered
insamplingfrequency: yearly, quarterly, monthly, daily, andhourly, withabouthalfof
the series sampled on a monthly basis. The series was taken from the following areas:
business,economics,industry,demographics,education,laborandwages,government,
households,bonds,stocks,insurance,loans,realestate,transportation,naturalresources,
and the environment. The sheer amount of time series and their spread is, of course,
commendable,but,atthesametime,thiscouldbediscouragingforthecompetitorsdue
to the amount of labor required. There was also a relatively large number of dropouts
becausetheforecastingteamswerediscouragedwhentheycomparedtheirresultstosimple
benchmarkforecastingmethodssuppliedbytheorganizers. Nevertheless,61forecasting
methodsendedupbeingrepresented.
The length of the time series varied considerably, with the minimum number of
observationsinthetrainingsetbeing13foryearly,16forquarterly,42formonthly,80for
weekly,93fordaily,and700forhourlyseries. However,onaverage,thelengthoftheseries
wasmuchlongerthantheseriesintheM3contest. Theforecastswereevaluatedinseveral

Entropy2025,27,279 15of34
ways,mostlybasedonrelativeabsolutedeviation,withanaveragetakenoverforecasting
horizons,whichvariedfrom3foryearlydatato48forhourlydata.
ThewinnerofthecompetitionwasSlakeSmall,adatascientistatUmberTechnologies.
Hemixedexponentialsmoothing-typemodelswithRNrecursivedeeplearningmethods,
which are described in more detail in [82]. His hybrid method perhaps represented a
mainresultofthecompetition,namelytheimprovednumericalaccuracyofcombining
forecastingmethodsandthesuperiorityofahybridapproachthatutilizesbothstatistical
andMLfeatures.
Combininghaslongbeenconsideredausefulpracticeintheforecastingliterature,
going all the way back to the classical paper of [83] for purely statistical methods and
up to the ensemble methods for random forest and gradient boosting. Intuitively, it
is understandable that the combining principle can lead to improvements, as different
methods pick up different forecasting potentials of the data, but the exact theory that
explainstheimprovementismorescarce;see,e.g.,Ref.[84]. Morespecifically,fortheM4
competition,therewasonly1purepointforecaststatisticalmethodamongthetop10most
accuratemethods,whileallofthe10leastaccuratemethodswereeitherpurelystatistical
orpurelyML.Similarresultswereobtainedforintervalforecasting.
Itseemsthatmostofthemethodswereappliedtoindividualseries,withonlyafew
attemptstoexploitmultipleseriestoextrapolatetheindividualones. Similarly,exogenous
variablesdonotseemtohavebeenused(possiblynotthepointofthecompetitionand
perhapsnotsoeasilyavailable).
AnotherissuenotdealtwithbyMakridakisetal. andbyothersimilarcontestsisthat
therewasnoemphasisonso-calledblackswans,i.e.,intheevaluationoftheforecasts,it
wasnotregisteredwhetheraforecastingmethodinsomecasesdiddisastrouslybadly;this
wouldbemissedinanevaluationbasedonaverageperformanceovertheseries.The“black
swans”may,insomecases,becausedbythick-taileddistributions[85]. Theorganizers
remarkthatthisphenomenonwasoutsidethescopeoftheM4competitionbutstatedthat
anotherforecastcompetitionisneededforcloserexaminationtoanalyzetheimplications
ofblackswansforriskmanagementanddecision-making.
AtotaloffiveMLmethods,fourpureandonecombinationofsolelyMLmethods,
didnotdowell. Theseresultswereinagreementwith[24]. However,itcouldbepossible
thatthisispartlyduetotheMLmethodsusedinthecompetition. Forexample,itdoesnot
seemthatthebest-developedrandomforestorgradientboosting processesparticipated.
Thesetypesofcriticism(partlypointedoutbytheorganizersthemselves)andsome
additionalonesaretakenupin[86]. Theyrefertotheresultsofarecentcompetitionof
145,000seriesonwebtrafficdatarunbytheKagglecorporationandhostedataboutthe
sametime. ThetimeseriesintheKaggledatahadamuchhigherspectralentropy(defined
by−
(cid:82)π
f(λ)log f(λ)dλ,where f(λ)isthespectraldensityoftheseries). Thismeansthat
−π
theserieswerenoisierandmoredifficulttopredict. Further,manymoreserieshad(much)
shortertimeintervalsbetweenthesamples. FortheMakridakisdatamentionedabove,
theemphasisisonmonthlydata(48%),whereasonly0.4%wereweekly,4.2%daily,and
0.4%hourly.
In[86],FryandBrundagstatethatatGoogle,asisthecasewithmanyothernet-based
companies,thereisanincreasingdegreeofsituationswhereonehastodealwithshort
timeintervals,e.g.,even5minintervals,andsometimesirregulartimeintervals. Forthese
data with higher spectral entropy, it has turned out that ML methods have been doing
increasinglywell,andin[86],FryandBrundagestatethatMLmethodshave,infact,beena
game-changerforthiskindofforecast. Atthesametime,theyreiteratethatmoreemphasis
should be put on multivariate and hierarchies of time series, as well as on predicting

Entropy2025,27,279 16of34
extremeevents. Theystatethatperhapsmoreattentionshouldbeputonpredictinghigher
quantilesinaforecastdistributionthanonproducingasingle-pointforecast.
Perhapsasareactiontothis,anewM5forecastcompetitionwaslaunched[80],which
focusedonretailsalesforecastingapplicationsandusedreal-lifehierarchicallystructured
salesdatawithintermittentanderraticcharacteristics. Thecompetitionattractedmany
participantswhowereeagertoexperimentwitheffectiveforecastingsolutionsinreal-life
situations faced by numerous retail companies on a daily basis. Many of the series in
thecompetitionwerecharacterizedbyintermittency,involvingsporadicunitsaleswith
manyzeroes.
Thedatasetusedcomprisedtheunitsalesof3049productssoldbyWalmartinthe
USA.Thedatawereorganizedintheformofgroupedtimeseriesaggregatedbasedon
theirtype(categoryanddepartment)andsellinglocations(storesandstates),withatotal
of42,480seriesin12cross-sectionalaggregationlevels. Asaperformancemeasure,ascaled
leastsquarescriterionaveragedoverseveralforecastinghorizonswasused.
Again, simple methods like exponential smoothing did fairly well. However, this
time,theywereclearlybeatenbythebestMLmethods. Thelight-GBMversionofgradient
boosting mentioned in Section 4.2 turned out to have superior forecasting capabilities
comparedtoallotheralternatives,anditwasusedinpracticebyallofthe50competitors.
This is consistent with the claim of [86] regarding the superiority of ML methods for
thisandsimilartypesofseries. Somewhatcuriously,thefirstprizewaswonbyasenior
undergraduateatKungHeeUniversityofSouthKoreawiththeteamappellationYJ.STU.
Heusedanequal-weightedaverageofvariouslight-GBMalgorithms.
ThemostrecentoftheMakridakisforecastingcompetitionsisM6[81]. Participants
wereaskedtoforecast100financialassetsandtomakecorrespondingfinancialinvestments.
Surprisingly, there was virtually no correlation between the best forecasts and the best
investmentdecisions;itturnedouttobeverydifficulttobeatthestandardS&Pmarket
index. Theauthorsdowarnthattheparticipantstoalimiteddegreecarriedoutthestudy
accordingtotheintentionsoftheorganizers. Itwasintendedthatthecompetitionsshould
have12non-overlappingsubmissionperiods,witheach28daysafterthepreviousone.
Asaresult,thecompetitionlastedforalmostoneyear. However,onlyasmallpercentage
oftheteamsupdatedtheirforecastregularlyduringthedurationofthecompetition. Many
teamssimplysubmittedonceortwiceattheverybeginningofthecompetition. Again,
awinningteamwasdirectedbyagraduatestudent.
ItissatisfyingthatMLtechniqueshavethepotentialtoobtainbetterforecasts,andthey
doincreasethetoolboxofforecasters. However,therearereasonsforsomereservations
and criticisms directed towards ML methods. A primary reason, as mentioned, is that
theyareblackboxforecastsbasedonpatternrecognitionofdatatypes. Someattempts,
see,e.g.,Ref.[68](whoobtaintheirbestresultsusingrandomforestroutines),havebeen
madetolookintothisbycomparingparticularcasesofbenchmarkforecasts,changing
theparametersofanMLforecast,andseekingtoexplainthecorrespondingchangesin
theforecasts. SeeSection5.3forfurthermentionsofthispaper. Basically, MLmethods
arenotimmediatelyinterpretable,ase.g.,anARtimeseriesmodel;however,asindicated
inSection4.3,attemptstoopentheblackboxhavestartedtoemerge. Moreover,another
distinct difference is the lack of theoretical results on the asymptotics of ML methods.
Thebeginningoftheoreticaldevelopmentmayberepresentedin[87].
Summingup,regardingtheresultsfromtheMakridakiscompetitionsandothersimilar
competitionsliketheKagglecompetitions,thereseemstobeadefinitetrendwherethe
MLforecastsareimproving,andatleast,insomeareasasthosewithhighspectralentropy
aresuperiortostatisticalforecasts. However,limitationsofthesecompetitions,otherthan
theblackboxcriticismofMLmethods,havebeenpointedout. Forexample,theyhave

Entropy2025,27,279 17of34
essentiallybeencarriedoutforunivariateseries. Theystartedoutbyusingmoreorless
purepointforecasts. Intervalpredictionhasbeenincreasinglyincluded,butthereisstilla
lackofclearresultsonforecastingdistributionsandextremequantiles. Moreover,there
isalackofsystematicallyevaluatingmultivariateforecasts, theinfluenceofexogenous
variables,andtheeffectofnonstationarityonmultivariatesystems. Thenextsectionwill
bedevotedtosomeofthesethemes.
5. MLvs. StatisticalModelsinSomeOtherSituations
BasedonthecontentsandcriticismsoftheMakridakiscompetitions,itcanbestated
thattheydonotconstituteacompletecoverageofallaspectsoftheforecastingproblem.
Inthissection,Iwilllookbrieflyandsomewhatunsystematicallyatsomeofthemissing
aspects. Eachofthesesubjectareaswouldbenefitfromasystematicstudyinaframework
ofM-typeforecastcompetitions. Ordinarystatisticalmodelsseemtostilldominateinthese
areas,buttherehasbeensomerecentworkonMLmethods.
5.1. ProbabilityForecast
Sometimes, one is not satisfied with an interval for measuring forecast error and
would like more detailed information in terms of forecast distribution. This is easily
obtainedforalinearGaussianmodel,e.g.,anAR(p)model,asdefinedin(4),wherethe
forecastdistributionisobtainedasN(a 1 y t−1 +···+a p y t−p ,σ e 2),whereσ e 2isthevariance
in the error process {e }. Similar reasoning can be put forward for an additive model
t
withaGaussianerrorprocess. Inamoregeneralsituationforamultivariateseries{y },
t
inprinciple,kernelestimatescanbeusedtoobtainestimatesoftheconditionaldistribution
p(y t+1 |(y t ,...,y t−p )) = p( p y ( t y + t 1 , , . y . t . , + ... y , t y − t p − ) p ) (16)
butthecurseofdimensionalitycomesintoplayformoderatedimensionsof{y}andfor
moderateorders, p. Inaddition,thedenominatormaybeclosetozerointheestimatesof
thetail,whichmaycauseinstability.
A possible alternative may be to use local Gaussian estimates, as detailed in [4],
inparticular,chapters9and10onlocalGaussiandensityandconditionaldensityestimation;
seealso[88].
A very recent conditional probability model coupled with the theory of diffusion
processeshasrecentlyobtainedverygoodresultsinweatherforecasting;seetheendof
Section6.
Indealingwithforecastdistributions,onemeetsthefundamentalproblemofhowto
comparethem. Whenisonedistributionsignificantlybetterthananother? Thisproblemis
equallyvalidforpointforecastsandhasbeendiscussedintheclassicalpaper[89]. They
introduceaprocessfortestingwhetheronepredictorissignificantlybetterthananother.
TheauthorsofRef.[90]treatasimilarproblemforprobabilityforecasts.
Actually,Gneitingandcolleagueshavediscussedanumberoffundamentalquestions
relatedtoprobabilityforecasting;see,e.g.,theeditorial[91]byGneitingand[92]. Inpar-
ticular,heandhiscoauthorsexaminetheprocessofforecastingextremeevents[93]and
combiningprobabilityforecastsin[94].
TheMLliteratureonprobabilisticforecastingismoresparse. Onerelativelyrecent
contributionis[95]. Theauthorsconcentrateonfindingforecastsofquantiles,whichisa
veryrelevantexpressionoftheprobabilitydistribution,perhapsineconomicsandfinance
inparticular. SeveralversionsofaDeepARquantileestimatehavedonewellcomparedto
moretraditionalbenchmarkestimateswhencomparedtothoseforwardedalreadyin[96].

Entropy2025,27,279
18of34
AsplineapproachcoupledwithanRNN,seeSection4.1,isadvocatedin[97],whereas
theauthorsof[98]useacopulaapproach.
5.2. VolatilityForecastingandaMachineLearningExample
Volatility is an all-important concept in the analysis of financial risk. Rob Engle
receivedtheNobelPrizeforhiscontributionstothisfield,inparticular,in[99,100]. There-
sultingmodelsaretheARCH/GARCHmodels,whicharenowwellrepresentedinany
textbookineconometrics. TheGARCHmodelfortheinstantaneousconditionalvariance
σ2isgivenby
t
|     |          | p     | q      |     |     |
| --- | -------- | ----- | ------ | --- | --- |
|     |          | ∑     | ∑      |     |     |
|     | σ 2 = ω+ | α ε + | β σ 2  |     |     |
|     | t        | i t−i | j t −j |     |     |
i=1 j=1
where ω is a constant term, and {ε } is the heteroscedastic error term. There are many
t
specializedversionsoftheGARCHmodel,e.g.,EGARCH,thattakecareoftheleverage
effectofvolatility,
|             | p     |              |      | q        |     |
| ----------- | ----- | ------------ | ---- | -------- | --- |
|             | ∑     |              |      | ∑        |     |
| logσ 2 = ω+ | (α ε  | +γ (|ε| −E|ε | |))+ | β logσ 2 |     |
| t           | i t−i | i t−i        | t−i  | j t −j   |     |
|             | i=1   |              | j=1  |          |     |
wherethenewparameterγ i capturestheasymmetricimpactofnewswithnegativeshocks.
Analternativeclassofvolatilitymodelsistheso-calledSV(Stochasticvolatility)models;
see,e.g.,Ref.[101].
Theincreaseduseofhigh-frequencydatahasledtotheintroductionofanewinstanta-
neousvarianceconcept:realizedvolatility. High-frequencydatacanreallybelookedatasa
processwhereeventstakeplacecontinuouslyintime. Asimplemodelforthepriceprocess
P forafinancialassetiisgivenby
it
= +σ
|     | dlogP | it µ i | it dW t |     |     |
| --- | ----- | ------ | ------- | --- | --- |
whereµ i isthedrift,σ it istheinstantaneousvolatility,andW t isthestandardBrownian
motion. In practice, a discrete approximation is used. The mid-price return for asset i
duringthetimeinterval(t−1,t]isconsideredgivenby
|     |     | (cid:16) | (cid:17) |     |     |
| --- | --- | -------- | -------- | --- | --- |
P it
|     | r   | =log | .   |     |     |
| --- | --- | ---- | --- | --- | --- |
|     | it  | P    |     |     |     |
i,t−1
Refs.[102,103]arguedthatthesumofsquaredintradayreturnsisaconsistentestimator
(cid:82)t σ2ds,
of the unobservable theoretical integrated variance, where h is the look-back
t−h is
horizon, such as 10 min, 30 min, 1 day, etc. The realized volatility can be based on the
logarithm (to reduce the impact of extreme values). Ref. [104] specifically defined the
followingduringaperiod(t−h,t]:
t
|     | (h) | =log (cid:0) ∑ | r2(cid:1) |     |      |
| --- | --- | -------------- | --------- | --- | ---- |
|     | RV  |                | is .      |     | (17) |
it
s=t−h+1
witha5minreturninterval.
Previously,forecastingvolatilitywasbasedonparametricmodels. Veryrecently,the
authorsof[105]usedMLmethodsandsetupasimpleforecastingcomparisonbetween
severalmodels. Amongotherthings,theybasedthemselveson(17)butwitha1minreturn
interval. Ref.[105]arguesthat,generallyspeaking,therearetwobroadfamiliesofmodels
usedtoforecastdailyvolatility: (i)GARCHandSVmodelsthatemploydailyreturnsand
(ii)modelsthatusedailyRVs. Previouswell-establishedstudieshaveshownthatduetothe
utilizationofavailableintradayinformation,dailyRVisasuperiorproxyforunobserved

Entropy2025,27,279 19of34
dailyvolatilitywhencomparedtotheparametricvolatilitymeasuresgeneratedfromthe
GARCHandSVmodelsofdailyreturns[103,106,107].
Twoquestionscanbeasked. Ithasbeenobservedthatinassetmarkets,thereseems
tobeacommonintradaystructurethatissharedamongthevolatilityoftheassets. Itis
termedcommonality. Thefirstquestionis,canintradaycommonalitystructurebeutilized
in improving volatility forecasts? The second question has to do with the main theme
of the present paper: Can forecasts based on parametric models be improved upon by
MLmethods?
Bothquestionsareconsideredin[105]intheirhandlingofdata. Theyuseadataset
composedofthetop100componentsfortheS&Pindexfortheperiodbetween1July2011
and30June2021. Afterfilteringawaythesharesforwhichdatadidnotexistfortheentire
period,93stockswerekept. Theaveragerealizedvolatilitycommonalityforthemarketis
RV
(h)
=
1 ∑ n
RV
(h)
M,t n it
i=1
andbecauseameasureofthecommonalityisused,theR2valueoftheregressionis
RV
(h)
= α +β RV
(h)
+ε
it i i M,t it
whichisinspiredbypriorstudies,asin[108,109].
Thedataweresubjectedtoanumberofmethods,bothparametricandML,andthe
outcomeswerecomparedforaone-datasetvolatilityforecastingcompetition.
Thetwoquestionsweretreatedforanumberofmodelsforinstantaneousvolatility
anditsdevelopmentintime. AmongthemodelsincludedwereseasonalARIMA,HAR
models(cf.[110]),ordinaryleastsquares,leastabsoluteshrinkage,XGBoost(essentiallya
gradientboosttechnique,asdescribedbeforeinSection4.2),multilayerperceptron(MLP)
(amultilayerfeedforwardneuralnetwork),andlongshort-termmemory(thisistheLSTM
modelingroutinedescribedearlier).
Forthesemodels,andwiththedatasetdividedintoatrainingperiodandavalidation
period,anextensivedataanalysisandcomparisonwascarriedout. Consistentwiththe
M5competition,theMLmethods,inparticular,theneuralnetwork-basedmethodsMLP
andLSTM,gavethebestvolatilityforecasts. Moreover,formostmodels,takingadvantage
of the commonality information leads to better forecasts. Finally, contrary to the M6
competition,theforecastingevidenceseemstobeconsistentwiththeresultsobtainedin
constructinginvestmentportfoliosbasedonforecasts. Muchmoredetailandanumber
ofrelatedreferencescanbefoundin[105]. Itshouldalsobementionedthatinthestudy
offorecastingthevolatilityofcryptocurrencies[111],itwasfoundthatforecastscanbe
improvedbycombiningGARCH-typemodelswithMLforecasts.
AsremarkeduponinSections1and4.4,analternativemeasureofuncertaintyofdata
isgivenbyentropy. IntheKagglecompetitionreferredtoinSection4.4,theimportanceof
theentropymeasurewasstressed. Theuseofentropyinfinancialtimeseries(alsopointing
outtherelationshiptovolatility)hasbeenmentionedinseveralrecentpublications.
In [112], structural entropy is introduced, and the new measure and volatility are
remarkablycorrelatedforanassetpriceseries;seealso[113,114]. Relatedto[111]is[115],
andbothdealwithcryptocurrency. Finally,Ref.[116]usedentropyinthedescriptionof
suddenshocks,whereas[2]studiedentropy-correctedgeometricBrownianmotion.

Entropy2025,27,279 20of34
5.3. MultivariateForecasts,IncludingExogenousVariables,Panels,andCointegration
WhilemultivariateMLmethodshavecreptuprelativelyrecently,multivariatedata
andmodelshavebeenusedforalongtimeinmultivariatestatisticalanalysis. Thevector
autoregressivemodel,VAR,is
y t = A 1 y t−1 +···+A p y t−p +e t (18)
where{y }isavectordataprocess,A,i =1,...,pareautoregressivematrices,and{e }is
t i t
avectorinnovationprocess;thishasbeenusedextensivelyineconometrics,finance,and
otherfields. Thispureautoregressivemodelmaybecomplementedbyasetofexogenous
variables{x },resultingintheVARXmodel. Suchmultivariatemodelswerelargelynot
t
presentintheMakridakiscompetitions,butclearly,theycanbeimportantinforecasting.
Ifthereisdependencebetweenthecomponentsofavectorprocess,theintuitiveuseofthe
dependencyinformationshouldleadtoimprovedforecastsoftheindividualseries.
So,arethereanysystematicforecastingexerciseswhereclassicalautoregressive-type
models are compared with ML methods? It seems that, thus far, as for the volatility
case,thereareonlyspecificexamplesofsuchcomparisons,andthesemostlypertainto
asituationwhereasinglevariabletimeseries,{y },dependsonqexplanatoryvariables,
t
{x },...,{x }. Onesuchexamplethatgivesagoodillustrationis[68],whereforecasting
1t qt
theinflationoftheUSconsumerpriceindexwasstudied. Thepossibledriversofinfla-
tionaretakenfromtheso-calledFRED-MBdatabase,whichisalargemonthlydatabase
designedforanalysisindata-richenvironments. ThedataperiodisfromJanuary1960to
December2015,with672monthlyobservations. Thereare122explanatoryvariables. All
variablesweretransformedtoachievestationarity.
Thebenchmarkmodelsincludeunivariateautoregressive,randomwalk,andunob-
servedcomponentstochasticvolatilitymodels. Anumberofothermodels,includingML
models,weretried. Forecastswerecomputedfor3-,6-,and12-monthhorizons. Theau-
thorsfoundthat,overall,randomforestoutperformedtheothermethods(itdoesnotseem
thattheLSTMalgorithmwasincludedinthestudy,though). AsmentionedinSection4.4,
theauthorsattemptedtoobtainmoreinsightintotheblackboxconstitutingrandomforest
inthiscase.
AnexamplewhereLSTMdoeswellcomparedtoothermethodsinmultivariatetime
series forecasting is in [117]. The LSTM method is extended with a so-called attention
mechanism (see Section 4.1) for the general use of the attention mechanism under the
descriptionoftransformers. However,randomforest-typeforecastswerenotincludedin
theapplicationofforecastingtosolarenergydata,amongotherthings.
Anexampleoftheuseofexplanatoryvariablesregardingtheclimateispresented
in [118]. Temperatures in five Chinese cities were sought to be explained using dew
pointtemperature,relativehumidity,airpressure,andcumulativewindspeeddata. Ina
comparisonwiththelassomethodandordinaryleastsquares,LSTMmethodsperformed
best. Randomforestandgradientboostingmethodswerenotincluded.
Finally,Ref. [119]isapaperonthepredictionofsoilmovement,wheremultivariate
methodsdidbetterthanunivariateversions,andLSTM-typeforecastswereoutperformed
bygeneralparametricstatisticalmodelslikeseasonalARmodels. Thereseemtoberela-
tivelyfewdatasamplesinthisinvestigation.
Incasetherearemanytimeseries,panelmodelsaretraditionallyusedinsteadofVAR
models. Aquitegenerallinearpanelmodelcanbestatedas
′
y = α +µ +β x +u (19)
it i t i it it

Entropy2025,27,279 21of34
wherey isthedependentvariableformemberiofthepanelattimet,with1≤i ≤ Nand
it
1 ≤ t ≤ T,andwheretheapostrophe(’)standsfortransposed. Moreover,x isavector
it
ofexplanatoryvariables, forwhichtheinfluenceon y isdeterminedbythecoefficient
it
vector β. Thescalarsα andµ arespecificpanelmemberandtimeeffects,respectively.
i i t
Finally, u isaresidualterm. Theparametersα, µ ,and β maybedeterministic(fixed
it i t i
effect)orrandom.
Model(19)issometimestermedastaticpanel,whereasthetermdynamicpanelis
reservedforthemodel
′
y it = α i +µ t +a i y i,t−1 +β i x it +u it (20)
withanexplicitdependenceonpasty-s. Ofcourse,bothmodelsmaybegeneralizedto
containhigher-ordertimelagsfortheyandxvariables. Apanelmayalsobeunbalanced,
wherethenumberofobservations,T,maybeallowedtodependoni,T = T,butIwillnot
i
beconcernedwiththesegeneralizations.Actually,Iwillintroduceseveralrestrictionsof(19)
and(20). First,oneormoreofthetermsintheseequationsmaybeomitted. Second,ifthe
parametersarenotallowedtodependoni,thepanelissaidtobehomogeneous,whereas
dependenceonileadstoaheterogeneouspanel. Inthelattercase,itissimplesttotreatthe
casewheretheparametersarerandomandhavethesamedistributionforeachi. Often,
independenceoveriisaddedasanextraassumption,andthetaskofestimationmaybe
reducedtosimplyestimatingthemeanoftheparameters. Ingeneral,averagingtechniques
canbeusedforhandlingheterogeneouseffects,whiledifferencingandcointegration(see
below)mayrepresentinstrumentsfortreatingnonstationaryeffects.
Thetheoryofpanelshasconcentratedquitealotoninferenceinparametricmodels.
However,thepotentialuseofpanelsinforecastingisobvious. Arecentsurveyofpanel
forecastingusingrelativelytraditionallinearpanelmodelsisgivenin[120].
Nonlinear models do exist, and recently, neural networks have been included in
themodelingofnonlinearities; see[121]. Theauthorsfindsignificantforecastinggains
regardingfeedforwardneuralnetworkswhencomparedtolinearpanelsandnonlinear
time series models when examining predictive power for new COVID-19 cases. They
werealsoabletofindsomeoftheasymptoticpropertiesoftheirmethodusingarguments
originallydevelopedin[87].
Forseveralforecastingmethods,thereisnospecialdevicefortakingcareofnonstation-
arity. FortraditionalmultivariateARIMAmodels,however,individualdifferencingofthe
componentswasthefavoritetool;thishasalsobeenusedforpanels. Withtheintroduction
ofcointegrationmodels,thishaschanged,andaninitialstepwouldconsistoflookingfor
(linear)cointegratingrelationships;thecointegratingVARmodelcouldberestatedasa
so-callederrorcorrectionmodel.
Let{y }beavectoroftimeseriesvariablesthatare(individually)ofthe I(1)class;i.e.,
t
theycanbemadestationaryusingdifferencing. Then,byreparametrizing,oneobtainsthe
VECM(vectorerrorcorrectionmodel)
∆y t = αβ ′ [1,t,y ′ t−1 ] ′ +Γ 1 ∆y t−1 +···+Γ k−1 ∆y t−k+1 +Φd t +µ+ε t (21)
wherethematricesαandβhaveacointegrationframeworkinterpretationofEquation(18),
and Γ 1 ,...,Γ k−1 and Φ are coefficient matrices; µ is a coefficient vector, d t is a vector
containingthestationary,I(0),variables,andε isaprocessofresidualtermsoftenassumed
t
inthemodeltobeiidnormallydistributed. See,e.g.,Refs.[122,123].
IsitpossibletocoupleMLmethodswiththeconceptofcointegration? Anexample
of this can be seen in [124]. Their first step is to include a nonlinear term in the error-
correctingmodel,forexample,aSTARmodel,asintroducedinSection3. Then,thelinear
partissubtractedfromthefullmodel,andthenonlinearpartissoughttobere-estimated

Entropy2025,27,279 22of34
usingrandomforest. Inthisway,amixedrandomforestcointegrationmodelisobtained.
The model is applied to weekly forecasts of a gasoline price process cointegrated with
internationaloilpricesandexchangerates. Thismixedmodelprovidedbetterforecasts
thanapurelyparametricmodel.
Itshouldbementionedthatdeeplearningforecastshavealsobeenusedinportfolio
constructionforcointegratedstocks. Theinterestedreaderisreferredto[125].
5.4. GARCH-TypeSchemesforIntegerandContinuousTimeSeries
Lately,therehasbeenanincreasinginterestinintegertimeseries. Thesearetimeseries
consistingofcountswithalownumberineachtimeperiod,soacontinuousapproximation
ofthecountsdoesnotworkwell.
There are two main classes of integer time series models: the INAR class and the
INGARCH model. In the INAR model, a convolution trick is used to obtain integer
time series that follows an AR model. In the INGARCH model, a recursion is used on
aparameterofaninteger-baseddistribution. TheuseofMLmethodsforbothclassesis
verylimited(tomyknowledge). ArecentarticleforINARfuzzyseriesis[126]. Negative
binomiallikelihoodanalysiswithMLwasbrieflymentionedin[52];seealso[127].
Here,IwillplaceemphasisonINGARCHmodelsduetotheirmanygeneralizations
tomultivariatemodelsandcontinuoustimemodelswithconnectionstoso-calledHawkes
processesandmultivariatetimeseriesinfinance. ThemoststraightforwardINGARCH
modelisPoissonautoregression. Earlierattemptsarerepresented,mainlyusingsecond-
ordertheory,in[128]and,morerecently,in[129].Amorethoroughintroductiontoinference
theoryandergodicityisgivenin[130],focusingonPoissonautoregression.
Let{y }beanintegertimeseries,andletFy,λ betheσ-algebrageneratedby{y ,s ≤
t t s
t,λ }. Here, {λ } is the time-varying random intensity of a Poisson process {y }. The
0 t t
first-orderPoissonautoregressivemodelisgivenbythefollowingGARCH-likerecursion:
y t |F t y − ,λ 1 ∼Poisson(λ t ) λ t = d+aλ t−1 +by t−1 (22)
where d, a, and b are the parameters to be estimated. Probabilistic properties and an
asymptotictheoryareestablishedin[130]. Itisobvioushowforecastscanbedevelopedin
thisscheme,andforecastswereusedintestsoffittingfinancialdatain[130].
Anumberofgeneralizationshavebeendevelopedtocoverhigher-ordermodelsand
nonlinearmodels,likethresholdandexponentialautoregressiveconsiderations. Further,
logarithmicintensity,alternativeintegerdistributions,likethenegativebinomialinthe
recursivescheme,andmultivariatecaseshavebeenexamined. Someselectedreferences
canbefoundin[131]. Again,tomyknowledge,machinelearningmethodshavenotyet
beenusedmuch,althoughonecouldeasilythinkofsituationswheresuchanapproach
couldbeuseful,inparticular,forhigh-dimensionalandnonlinearintegertimeprocesses.
AgeneralizationtocontinuoustimeregardingtheGARCH-likestructurecanbefound
in[132,133]forself-excitedjumpprocesses. Let{T }denotethetimesofeventsinapoint
n
process. Weintroducethecountingprocessassociatedwiththepointprocess,
∑
N(t) = 1 Tn ≤t
Tn ≤t
which counts the number of events up to time t. The corresponding σ algebra is FN,
t
generatedby{N(s),0≤ s ≤ t}. Astochasticintensityprocess,{λ },correspondingto(22)
t
cannowbegeneratedusingaGARCH-likestochasticdifferentialequation:
dλ = α(λ −λ(t))dt+βdN(t). (23)
t 0

Entropy2025,27,279 23of34
Themodelin(23)canbeextendedtothemultivariatecase,whereonecomponentmayexcite
anothercomponent. Applicationstofinancialdataarepresentedin[133]. Theauthorsalso
brieflydiscussnonlinearmodelsofthistype. Inthelinearcase,themodelsgeneratedbyre-
cursioncanbeconsideredasaparsimoniousformofHawkesprocesses,wheretheintensity
(cid:82)
isgeneratedbyacontinuousmovingaveragemechanismwithλ(t) = g(t−s)dN(s)for
somefunction,g. Theseprocesseswereoriginallyintroducedinthestudyoftheintensity
ofearthquakesbutwerelaterusedinfinance;see[134].
Thequestionofpredictingtheintensityprocessisanactualone. Itis,again,straight-
forwardtousetherecursiveequationitself,butcanmachinelearningmethodsbeused?
Someideasarepresentedin[135].
Theintensityprocessintheseapplicationsreplacesatime-varyingparameterbyusing
astochasticprocess. Aquitegeneralframeworkfortime-varyingparametersisdeveloped
in[136]. Themechanismusedtoupdatetheparametersovertimeisthescaledscoreof
the likelihood function. The authors remark that this approach provides a unified and
consistentframeworkforintroducingtime-varyingparametersinawideclassofnonlinear
models, with the GARCH model, autoregressive conditional intensity cases, and types
ofPoissoncountmodelsamongthem. Numerousfollow-uppapershaveaddressedthe
applicationofsuchmodelstoforecasting. Arecentsurveypaperis[137]. Iamnotawareof
machinelearningforecastsforthismodel.
Inthissection,ourfinalrecursivesystemwillbearecursivesystemforadynamic
network.WiththeincreasinguseoftheinternetandBigData,theanalysisoflargenetworks
isbecomingmoreandmoreimportant. Thereisawidefieldofapplications,whichranges
oversuchdiverseareasasfinance,medicine,andsociology,includingcriminalnetworks.
Abroadoverviewcanbefoundinarecentbook[138]. Morefoundationalproblemsare
coveredin[139].
Both research and applications have been overwhelmingly concentrated on static
networks.However,achangeseemstobetakingplacepresentlysincethestaticassumption
isanuntenableoneinmanypracticalcases. Astimegoeson,newnodesareaddedtothe
network,othersvanish,andthestrengthoftheconnectionbetweennodesmaybechanged
orevensevered. Thisrealizationhasledtoarapidincreaseininterestindynamicnetworks,
noted,forinstance,inthelastsectionof [140],whereasubstantialportionofthefollowing
materialistakenfrom.
Arecentexampleofrigorousstatisticalmodelingregardingadynamicnetworkis[141].
The authors modeled the network structure by using a network vector autoregressive
model. Thismodelassumesthattheresponseofeachnodeatagiventimepointisalinear
combinationof(a)itspreviousvalue,(b)theaverageofconnectedneighbors,(c)asetof
node-specificcovariates,and(d)independentnoise. Moreprecisely,ifnisthenumberof
nodes,lety betheresponsecollectedfromtheithsubject(node)attimet. Further,assume
it
thataq-dimensionalnode-specificrandomvectorx = (x ,...,x ) ′ ∈Rq canbeobserved.
i i1 iq
Then,themodelfory isgivenby
it
y it = β 0 +x i
′
γ+β 1 n i
−1∑
a ij y j,t−1 +β 2 y i,t−1 +ε it . (24)
j̸=i
Here,n = ∑ a representsthetotalnumberofneighborsofthenode,v,associatedwith
i j̸=i ij i
′
y,soitisthedegreeofv. Thetermx γistheimpactofcovariatesonnodev,whereas
i i i
n i
−1∑
j̸=i a ij y j,t−1 istheaverageimpactfromtheneighborsofv i . Thetermβ 2 y i,t−1 denotes
the standard autoregressive impact. Finally, the error terms, {ε }, are assumed to be
it
independentofthecovariatesandareiidnormallydistributed.
Thereareanumberofdifferencesbetweenthenetworkvectorautoregressionmodeled
usingEquation(24)andafulldynamicnetworkembedding. Eveniftheautoregressive

Entropy2025,27,279 24of34
modeldoesintroducesome(stationary)dynamicsintime,theparametersarestatic;i.e.,
nonewnodesareallowed,andtherelationshipbetweenthemisalsostatic,asmodeled
bythematrixA = {a }. Fromthispointofview,astheauthorsof[141]arefullyaware,
ij
themodel(24)isnotrealisticintermsofthedynamicsthattakeplaceinpracticeformany
networks. Ontheotherhand,theintroductionofastochasticmodelthatcanbeanalyzed
usingtraditionalmethodsofinferenceistobelauded. Aworthwhilenextstepistotryto
combinemorerealisticmodelswithastochasticstructure(e.g.,regime-typemodelsforthe
parameters,asin[142].Thehopeisthatitwillbeamenabletostatisticalinference.Ref.[143]
treatsdynamicnetworkswithafixednumberofnodesbutonlywherethedependence
betweennodesismodeledbyadoublystochasticmatrix.
For some very recent contributions to network autoregression, see [144] and the
referencestherein. In[145], theauthorsconsiderinteger-valuednetworkvariablesand
analyzelinearandlog-linearPoissonautoregressivenetworks. Thisismotivatedbythe
factthatmanynetvariablestakediscretevalues. In[146],nonlinearmodelsandtestsfor
linearityareintroduced.
An interesting recent publication is [147]; the authors study time series networks
forbothintegerandcontinuous-valueddata. Thenonlinearityisprovidedbyasmooth
linkfunction. Theauthorsstudiedstabilityconditionsforsuchmultivariatesystemsand
developedquasi-maximumlikelihoodestimateswhenthedimensionofthenetworkwas
increasing. Theyalsodeveloplinearitytests.
Again,forecastscan,inprinciple,beformeddirectlyfromtherecursiveequations. I
donotknowofinstanceswherethedynamicnetworkmodelandMLhavebeenappliedto
thesamedataset.
6. WeatherForecasting
Iwillfinishthispaperbylookingataproblemwherethemainthrustoftheexisting
forecastsdependsona(numerical)physicalmodel,namelyweatherforecasting. Whatare
theinteractions, ifany, betweenthisnumericalphysicalmodelandMLtechniqueslike
neuralnetworksandrandomforest? Isitpossibletocompletelydoawaywithnumerical
weatherforecasting(NWP)andbaseaweatherforecastentirelyonML?NWPisverytime-
consumingandrequiresextensivecomputerresources. Forthefastestandmosteffective
MLmethods,onemightthinkthattherecouldbeagaininprocessingtime,and,ofcourse,
thehopeisthat,ultimately,MLmayincreasetheaccuracyofweatherforecasting.
ManualNWPwasfirstattemptedin[148]inBritainin1922,andearlycomputer-aided
weather forecasts were produced in the 1950s by a group led by John von Neuman at
thePrincetonInstituteofAdvancedStudies;see[149]. Theearlyhistoryisalsooutlined
in[150,151]. Modernweatherpredictionreliesextensivelyonmassivenumericalsimula-
tionsystemsthatareroutinelyoperatedbynationalweatheragenciesallovertheworld.
StatisticalanalysisplaysamajorpartinthestepwiseprocedurethatNWPconsistsof.
InordertoperformNWP,avarietyofobservationsregardingatmosphere,land,and
oceanarecollectedallovertheworld,creatingaglobalobservationnetwork,nottheleast
in terms of satellite measurements. Although millions of different direct and indirect
measurements are obtained each day, these raw data must be transformed and refined
before they can be input into the numerical weather model. This stage is called data
assimilation(DA).Thedataarethenprojectedintoadiscretemodelgrid(interpolatedin
time)andadjustedtobeconsistentintermsofstatevariables(e.g.,temperature,pressure,
wind,etc.). DAalsotakescareofmeasurementerrors,suchasbiasesbetweendifferent
spatial instruments. The obtained initial Earth system after the DA step constitutes an
optimizedestimateoftherealconditions,cf.[152].

Entropy2025,27,279 25of34
Given these initial conditions, the core of the NWP model consists of numerically
solvingthecoupledpartialdifferentialsystem(theNavier-Stokesequations)describingthe
atmosphereintermsofmomentum,mass,andenthalpy.
TheNavier-Stokesequationsforfluidmotion,v,underlyingatmosphericflowarethe
following,cf.[153],p. 14:
∇·v =0 (25)
(cid:16)∂v (cid:17)
ρ +v·∇v = −∇p+µ∇2v+ρg (26)
∂t
where ρ is density, p is pressure, g is acceleration, and µ is a parameter. The Navier-
Stokesequationsareaccompaniedbyasetofthermodynamicequationsthatinterrelate
temperature,pressure,andhumiditywithintheatmosphere:
∂ρ
+∇·(ρv) =0 (Continuityequation) (27)
∂t
∂T q
+v·∇T = (Energyequation) (28)
∂t c
p
Dp
= −ρc ∇·v (Pressureequation) (29)
p
Dt
whereTisthetemperature,andc isapressureparameter. Theresultingsolutiongivesthe
p
atmosphericstateineachmodelgridcell.
This is very demanding computationally, and the solution can only be given over
a relatively coarse grid. A postprocessing stage (mainly statistical in nature, possibly
involvingML)is,therefore,neededtoobtaindataonafinergrid.
Over the past decades, the ability of NWP models to predict a future atmospheric
statehascontinuouslyimproved. ContemporaryglobalNWPmodelsarenotonlyableto
predictthesynoptic-scaleweatherpatternforseveraldays,buttheyhaveincreasedintheir
abilitytopredictregionaleventssuchas,e.g.,majorprecipitationevents.
TheincreasingsuccessofoperationalNWPmodelsisduetoimprovementsinallthe
stepsinvolvedintheNWPworkflowandthenewcapabilities(e.g.,satellitemeasurements)
of the global Earth observation system. The NWP model improvements can, therefore,
berelatedinparttoresolutionenhancement. Thecontinuousrefinementofgridspacing
hasalsorequiredreformulatingthedynamicalcoresoftheNWPmodels,wherethedis-
cretizedNavier-Stokesequationsaresolved. Simulatingtheatmosphereatthekilometer
scale brings with it the demand for highly parallelizable algorithms for the dynamical
core[154]. Simultaneously,remarkableprogresshasbeenachievedindesigningdiscretiza-
tion approaches that enable the grid scale dynamics to follow the conservation laws of
energy,entropy,andmass. Suchphysicalconservationlawsmaycauseproblemsinapure
MLapproach. Anextensiveoverviewofcontemporarydynamicalcorearchitectureand
spatio-temporalforecastingcanbefoundin[155].
ThegeneraldevelopmentofML,spanningovermuchmorethanweatherforecasting
and,inparticular,ofdeeplearning(DL),hashadahistoryofadvancesandsetbacks;see,
e.g.,Ref.[156]. Nowadays,MLhasseenseveralinstancesofsuccess. Recentdevelopments
are due to vastly increased computer capabilities, not the least due to massive parallel
processing. This is the case with, for example, TCNs and transformers, as reported in
Section4.1. ThishascarriedwithitthehopethatanMLsystemforweatherforecasting
maybefasterthanthepresentNWPsystem,allowingformoreefficientprocessingofvery
largedatasets. Finally,largebenchmarkdatasetshavebecomeavailableontheinternet.
Asaresultofthisdevelopment,highlycomplexneuralnetworksystemswithmorethan
106 parameters have enabled a breakthrough in image recognition, speech recognition,
gaming,andvideoanalysis.

Entropy2025,27,279 26of34
Theweatherandclimatecommunityis,ofcourse,awareofthepowerfuladvancesin
ML.However,accordingtoRef.[156],therehavestillbeenreservationsagainstMLmethods,
possiblyduetotheblackboxnatureofMLmethodsandalsothelackofimplementation
ofphysicalconservationlaws,asmentionedabove;see[157]. Moreover,Ref.[158]argued
thattraditionalMLmethodsmaynotyetbefullysuitableforEarthSystemdata;theyclaim
thatnewnetworktopologiesareneededthatnotonlyexploitlocalneighborhoods(evenat
differentscales)butalsolong-rangerelationships,forexample,significantrelationships
orlinksbetweenweatherphenomenaatwidelyseparatedlocationsonEarth,suchasthe
effectsfromtheElNiñoSouthernOscillation(ENSO)).ItmaybeofinterestthatbothTCNs
andtransformersrepresentpotentialtoolsformodelinglong-rangerelationships. See[159]
foranexampleoftransformersbeingusedinlong-termforecasting.
Forsometimenow,therehavebeenanumberofusesofMLmethods,butthesehave
mainlybeenwithinmoreisolatedpartsoftheweatherpredictionproblem, suchasthe
preprocessingandpostprocessingstagesmentionedearlier. Inthepreprocessingstage,
MLmethodscan,forinstance,beusedintheinterpolationofdatatoaregulargrid. The
postprocessingtechniqueshavebeenreviewedinseveralpapers,suchas[160,161].
Onesurvey[160]discussesboththeuseofparametricstatisticaldistributionsandML
methods. Distribution-basedpostprocessingapproachesspecifyaparametricmodelfora
forecastdistribution. Theparametersoftheforecastdistributionsarethenlinkedtothe
predictorsfromtheNWPsystemviaregressionequations. Flexibleadditiveregression
functionsaresuggestedin[162]. Despitethesepowerfulvariants,theneedtoselectasuit-
ableparametricfamilytodescribethedistributionofatargetvariableremainsalimitation
forparametricpostprocessingmethodsandoftennecessitateselaboratefine-tuning.
WhenitcomestoMLmethods,randomforesthasbeenusedinavarietyofpostpro-
cessingsituations,see,e.g.,Ref.[163]. Onechallengeis,again,theinterpretabilityofML
approaches. However,inweatherforecasting,attemptshavealsobeenmadetobreakopen
theblackbox;see,e.g.,Ref.[164],whichreviewsmethodsfordecidingwhichpredictorsare
mostimportantforamodelandforaparticularforecast. Amorerecentsurveyiscontained
in[157]. TheauthorsdiscussapplicationsofSHAPandLIME,asmentionedinSection4.3,
tometeorologicalMLroutines. Theyindicatehowtheseinterpretativeaidsmayhavethe
potentialtogainmoreinsightintopredictions,uncoveringnovelmeteorologicalrelation-
shipscapturedbymachinelearning. Further,theypointoutchallengesaroundachieving
deepermechanisticinterpretationsalignedwithphysicalprinciples. Refs.[165,166]should
alsobementioned.
Ingeneral,combiningforecasts(alsoinpostprocessing)hasbeenconsidered.Ref.[167]
does this in the context of an ensemble Kalman filter. Again, one challenge regarding
blendingforecastsistomaintaintherealisticphysicalfeaturesoftheNWPmodel. Thereis,
though,aclearshift[160]fromphysicalmodelingapproachestodata-drivenapproaches.
This shift is perhaps particularly transparent for the recent method of transformers, as
discussed in Section 4.1. In [168], a transformer-based neural network is used in the
postprocessing phase in predicting near-surface temperature, and in [169], hierarchical
transformers are used in the postprocessing of temperature and precipitation forecasts.
Moreover,transformersareusedinprecipitationnowcastingin[170].
Theseexamplesarerestrictedinthattheyarenotfullweatherforecasts. Thisisalso
thecasewithsomeTCN(again,seeSection4.1)applications. Ref. [171]usedTCNand
LSTMforweatherforecastingusingtimeseriesdatafromlocalweatherstations. TCNis
alsoanimportantcomponentin[172]inahybridmodelforwindpowerforecasting.
DespiteitspublicationinAnnalsofAppliedStatistics,Ref. [161]representsamore
theoreticalapproachtopostprocessing. Theauthorsstressthataccuratemodelingofmulti-
variatedependenciesiscrucialinmanypracticalapplicationsingeneraland,particularly,

Entropy2025,27,279 27of34
inNWP.Inseveralapproachestopostprocessing,ensemblepredictionsarefirstpostpro-
cessedseparatelyineachmargin,andmultivariatedependenciesarenextestablishedvia
copulas. Ref. [161]proposesamultivariatepostprocessingmethodbasedongenerative
machinelearningasanoutputofageneralneuralnetworktoavoidsomeofthelimitations
regardingthetwo-stagecopulaapproach. Thisresultsinanewclassofnonparametric
data-drivendistributionalregressionmodels.
WhilethiskindofpostprocessingstillrequiresacoreofNWPorisrestrictedtooneor
afewmeteorologicalvariables,simultaneously,intensiveworkhasbeengoingontotry
toestablishaschemeofweatherforecaststhatarebasedentirelyonstatisticaland/orML
approaches. Veryrecently,therehasbeenremarkableprogressinthisarea,whichmayeven
beabreakthrough.
ThegroupbehindthisbreakthroughistheGoogleDeepMindgroup. Theyhavetaken
ideasfromthemechanismoftransformersandusedtheminawidercontext. Theyare
extendingtheframeworktographs,whichseemstobeamorefittingmodelenvironment
forweatherforecastsduetotheobservations(nodes)beingscatteredoverspaceandwith
dependencenotonlybetweenneighboringpointsbutalsooverlargerdistancesreferring
tolong-rangemeteorologicalphenomena.
A gentle introduction to graph neural networks is given in [173]. The connection
betweentransformersandgraphneuralnetworks,withtheformerasaspecialcaseofthe
latter,isdescribedinaGraphDeepLearningLabreport[174].
TheGraphCastmoduledevelopedforweatherforecastingbytheGoogleDeepMind
group is described in a Science 2023 article [175]; see also [176]. GraphCast is able to
makemedium-rangeweatherforecastswithunprecedentedaccuracy. Accordingtothe
authors,itpredictsweatherconditionsupto10daysinadvancemoreaccuratelyandmuch
faster(inheritedfromthefasttransformerroutineset-up)thantheindustrygoldstandard
weathersimulationsystem—HighResolutionForecast(HRES)producedbytheEuropean
CentreforMediumRangeWeatherForecasts. GraphCastcanalsoofferearlierwarningsof
extremeweatherevents.
GraphCastmakesforecastsatthehighresolutionof0.25degreeslongitude/latitude
(28km×28kmattheequator). Thatismorethanamilliongridpointscoveringtheentire
surfaceoftheEarth. Ateachgridpoint,themodelpredictsfiveEarth-surfacevariables—
includingtemperature,windspeedanddirection,andmeansealevelpressure—andsix
atmosphericvariables. GraphCastisautoregressive;itcanbe“rolledout”byfeedingits
ownpredictionsbackinasinputtogenerateanarbitrarilylongtrajectoryofweatherstates.
The model was trained using 39 years (1979–2017) of historical data from existing
archives.AtrainingobjectivewastoaveragethemeansquarederrorsbetweenGraphCast’s
predictedstatesoverasetofautoregressivestepsandthecorrespondingdatafoundinthe
archives. MuchmoredetailscanbefoundintheSciencepaper.
WhatmakestheGoogleDeepMindgroupespeciallyimpressiveisthatthegrouphas
comeupwithanothermodulethatseemstobeonthelevelofGraphCast,ifnotbetter. Itis
describedinalate2024Naturepaper[177]. ItusestheappellationGenCastandisbased
onconditionalprobabilities,aformofconditionalindependence,usingdiffusionmodeling.
IthasthesameresolutionasGraphCastandroughlythesametrainingperiod;itbeatsthe
ENSmodel,theensembleforecastoftheEuropeanCentreforMediumRangeForecasting,
inspeedandaccuracyin97.2%of1320targets.
Dotheseadvancesmeanthatnumericalweatherpredictionmodelscanbediscarded
infavorofmachinelearningmethods? Thisisnotaviewpointheldbyscientistsinthisarea.
In[178],GraphCastiscritizisedforitspossiblelackofphysicalconsistency. Furthermore,
explainability, in spite of recent advances, is still an issue that needs further attention.

Entropy2025,27,279 28of34
Rare events are hard to model due to the difficulty of having limited data during the
trainingperiod.
Canmachinelearningmethodsbeextendedtocoverreallylong-rangeperiodsand
evengivecluestopossibleclimatemodeling? Thisquestionisraisedamongothersina
Csiroreport[179]. Itispointedoutthatwhileweatherpredictionisa“big-data”problem,
climateprojectionsrepresenta“small-data”problem,withrelativelylittleavailabledata.
Ontheotherhand, thereseemstobeeveryreasontocontinuethesearchforgood
machinelearningmethodsinweatherprediction,nottheleastasanextremelyvaluable
(andfast)complementtonumericalweatherforecasting.Hybridmodelsofphysicalmodels
andAImodelsmaybeofspecialinterest. InarecentNaturepaper,theauthorsofRef.[180]
discussthepossibilityofcouplingthephysicsofgeneralcirculationmodelswithmachine
learningmodelstoobtainahybridmodelthatmaybeabletoproduceusefulsimulations
oflong-rangeweatherorevenclimateprocesses. Similarargumentsareusedin[158].
Ref. [156] concludes that the research on pure ML methods in weather forecasting
isstillinitsinfancy; thespecificpropertiesofweatherdatarequirethedevelopmentof
newapproachesbeyondtheclassicalconceptsfromcomputervision,speechrecognition,
and other typical ML tasks. The author’s conclusion is that there may be potential for
end-to-end(“pure”)MLweatherforecastapplicationstoproduceequalorbetterquality
forecastsforspecificend-userdemands,especiallyifthesesystemscanexploitsmall-scale
patternsintheobservationaldatathatarenotresolvedinthetraditionalNWPmodelchain.
WhetherMLandDLwillevolveenoughtoreplacemostorallofthecurrentNWPsystems
cannotbeansweredatthispoint. Inanycase,accordingtoRef. [158],onemightarguefor
moreinteractionbetweenphysicalanddeeplearningsystems.
Funding:Thisresearchreceivednoexternalfunding.
InstitutionalReviewBoardStatement:Notapplicable.
DataAvailabilityStatement:Notapplicable.
Acknowledgments:Iamgratefultotwoanonymousrefereesforanumberofveryusefulsuggestions
thathaveledtosubstantialimprovementstothepaper.
ConflictsofInterest:Theauthordeclaresnoconflictsofinterest.
References
1. Delgado-Bonal,A.;Marchak,A. Approximateentropyandsampleentropy:Acomprehensivetutorial. Entropy2019,21,541.
[CrossRef]
2. Gupta,R.;Drzazga-Szczesniak,E.;Kais,S.;Szczesnial,D.EntropycorrectedgeometricBrownianmotion. Sci.Rep.2024,14,28384.
[CrossRef][PubMed]
3. Otneim,H.;Berentsen,G.;Tjøstheim,D. Locallead-lagrelationshipsandnonlinearGrangercausality:Anempiricalanalysis.
Entropy2022,24,378.[CrossRef][PubMed]
4. Tjøstheim,D.;Otneim,H.;Støve,B. StatisticalModelingUsingLocalGaussianApproximation;AcademicPress: NewYork,NY,
USA,2022.
5. Tjøstheim,D.;Otneim,H.;Støve,B. Statisticaldependence:BeyondPearson’sρ. Stat.Sci.2022,37,90–109.[CrossRef]
6. Makridakis,S.;Hibon,M.TheM3-competition:Results,conclusionandimplications. Int.J.Forecast.2000,16,451–476.[CrossRef]
7. Brown,R. ExponentialSmoothingforPredictingDemand;LittleCompany:Cambridge,MA,USA,1956.
8. Holt,C. Forecastingtrendsandseasonalsbyexponentialsmoothingaverages. Off.Nav.Res.Memo.1957,52; reprintedinInt.J.
Forecast.2004,20,5–10.
9. Billah, B.; King, M.; Snyder, R.; Koehler, A. Exponentialsmoothingmodelselectionforforecasting. Int. J.Forecast. 2006,
22,239–247.[CrossRef]
10. Pfeffermann,D.;Allon,J. Multivariateexponentialsmoothing:Methodandpractice. Int.J.Forecast.1989,5,83–98.[CrossRef]
11. Box,G.;Jenkins,G. TimeSeriesAnalysis.ForecastingandControl;Holden-Day:SanFrancisco,CA,USA,1970.
12. Tsay,R. MultivariateTimeSeriesAnalysis:WithRandFinancialApplications;Springer:NewYork,NY,USA,2017.

Entropy2025,27,279 29of34
13. Assimakopoulus, V.; Nikolopoulos, K. The theta model: A decomposition approach to forecasting. Int. J. Forecast. 2000,
16,521–530.[CrossRef]
14. Nikolopoulos,K.;Thomakos,D. ForecastingwiththeThetaMethod:TheoryandAppliaction;Wiley:NewYork,NY,USA,2019.
15. Ahmed, N.; Atiya, A.; Gayar, N.E.; El-Shishiny, H. An empirical comparison of machine learning models for time series
forecasting. Econom.Rev.2010,29,594–621.[CrossRef]
16. Hyndman,R.;Billah,B. Unmaskingthethetamethod. Int.J.Forecast.2003,19,287–290.[CrossRef]
17. Fiorucci,J.;Pellegrini,T.;Louzada,F.;Petropolus,F.;Koehler,A. Modelsforoptimizingthethetamethodandtheirrelationship
tostatespacemodels. Int.J.Forecast.2010,32,1151–1161.[CrossRef]
18. Spilotis,E.;Assimakopoulus,V.;Makridakis,S. Generalizingthethetamethodforautomaticforecasting. Eur.J.Oper.Res.2020,
284,550–558.[CrossRef]
19. Kyriazi,F.;Thomakos,D.;Guerard,J. Adaptivelearningforecastingwithapplicationsinforecastingagriculturalprices. Int.J.
Forecast.2019,35,1356–1369.[CrossRef]
20. Harvey,A. ForecastingStructuralTimeSeriesModelsandtheKalmanFilter;CambridgeUniversityPress:Cambridge,UK,1990.
21. Durbin,J.;Koopman,S. TimeSeriesAnalysisbyStateSpaceMethods;OxfordUniversityPress:Oxford,UK,2012.
22. Casals,J.;Garcia-Hiernaux,A.;Jerez,M.;Sotoca,S.;Trindade,A. State-SpaceMethodsforTimeSeriesAnalysis:Theory,Applications
andSoftware;ChapmanHall/CRCPress:BocaRaton,FL,USA,2016.
23. Villagas,M.;Pedregal,D. Supplychaindecisionsupportsystemsbasedonanovelhierarchicalforecastingapproach. Decis.
SupportSyst.2018,114,29–36.[CrossRef]
24. Makridakis,S.;Spiliotis,E.;Assimakopoulos,V. Statisticalandmachinelearningforecastingmethods: Concernsandways
forward. PLoSONE2018,13,e0194889.[CrossRef]
25. Tong,H.;Lim,K. Thresholdautoregression,limitcyclesandcyclicaldata(withdiscussion). J.R.Stat.Soc.Ser.B1980,42,245–292.
[CrossRef]
26. Chan,K. Consistencyandlimitingdistributionoftheleastsquaresestimatorofathresholdautoregressivemodel. Ann.Stat.
1993,21,521–533.[CrossRef]
27. Tong,H. Non-LinearTimeSeries.ADynamicalSystemApproach;OxfordUniversityPress:Oxford,UK,1990.
28. Tsay,R. Testingandmodelingmultivariatethresholdmodels. J.Am.Stat.Assoc.1998,93,1188–1202.[CrossRef]
29. Cai,B.;Gao,J.;Tjøstheim,D. Anewclassofbivariatethresholdcointegrationmodels. J.Bus. Econ. Stat. 2017,35,288–305.
[CrossRef]
30. Yang,L.;Bai,H.;Ren,M. Thresholdquantileregressionneuralnetwork. Appl.Econ.Lett.2024,31,1675–1685.[CrossRef]
31. Haggan,V.;Ozaki,T. Modellingnonlinearrandomvibrationsusinganamplitude-dependentautoregressivetimeseriesmodel.
Biometrika1981,68,189–196.[CrossRef]
32. Teräsvirta,T. Specification,estimationandevaluationofsmoothtransitionautoregressivemodels. J.Am. Stat. Assoc. 1994,
89,208–218.
33. vanDijk,D.;Teräsvirta,T.;Franses,P. Smoothtransitionautoregressivemodels—Asurveyofrecentdevelopments. Econom.Rev.
2002,21,1–47.[CrossRef]
34. Dempster,A.;Laird,N.;Rubin,D. MaximumlikelihoodfromincompletedataviatheEMalgorithm. J.R.Stat.Soc.Ser.B1977,
39,1–22.[CrossRef]
35. Hamilton,J. Analysisoftimeseriessubjecttochangesinregimes. J.Econom.1990,45,39–70.[CrossRef]
36. Guidolin,M.;Pedio,M. EssentialofTimeSeriesforFinancialApplications;AcademicPress:NewYork,NY,USA,2018.
37. Hastie,T.;Tibshirani,R. GeneralizedAdditiveModels;CRCPress:BocaRaton,FL,USA,1990.
38. Sperlich,S.;Tjøstheim,D.;Yang,L. Nonparametricestimationandtestingofinteractioninadditivemodels. Econom.Theory2002,
18,197–251.[CrossRef]
39. Huang,J.;Horowitz,J.;Weai,F. Variableselectionsinnonparametricadditivemodels. Ann.Stat.2010,38,2282–2313.[CrossRef]
40. Kolassa,S. Whythebestpointforecastsdependsontheerrororaccuracymeasure. Int.J.Forecast.2020,36,208–211.[CrossRef]
41. Box,G.;Cox,D. Ananalysisoftransformations. J.R.Stat.Soc.Ser.B1964,26,211–252.[CrossRef]
42. Schmidhuber,J. Deeplearninginneuralnetworks:Anoverview. NeuralNetw.2015,61,85–117.[PubMed]
43. Hornik,K.; Stinchcombe,M.; White,H. Multilayerfeedforwardnetworkareuniversalapproximators. NeuralNetw. 1989,
2,359–366.[CrossRef]
44. Tjøstheim,D.;Jullum,M.;Løland,A.Statisticalembedding:Beyondprincipalcomponents. Stat.Sci.2023,38,411–439.[CrossRef]
45. Mikolov,T.;Chen,K.;Corrado,G.;Dean,J.Efficientestimationofwordrepresentationsinvectorspace.arXiv2013,arXiv:1301.3781.
46. Mikolov,T.;Sutskever,I.;Chen,K.;Corrado,G.;Dean,J.Distributedrepresentationofwordsandphrasesandtheircomposability.
InProceedingsoftheAdvancesinNeuralInformationProcessingSystems26:ProceedingsAnnual27thConferenceonNeural
InformationProcessingSystems,LakeTahoe,NV,USA,5–10December2013.
47. Lim,B.;Zohren,S. Timeseriesforecastingwithdeeplearning:Asurvey. Philos.Trans.R.Soc.A2021,379,20200209.[CrossRef]
[PubMed]

Entropy2025,27,279 30of34
48. Gu, J.; Wang, Z.; Kuen, J.; Ma, L.; Shahroudy, A.; Shuai, B.; Liu, T.; Wang, X.; Wang, G.; Cai, J.; etal. Recentadvancesin
convolutionneuralnetworks. PatternRecognit.2018,77,354–377.[CrossRef]
49. Lea, C.; Vidal, R.; Reiter, A.; Hager, G. Temporal convolution networks: A unified approach to action segmentation. In
ProceedingsoftheComputerVision-ECCV2016,Amsterdam,TheNetherlands,8–10and15–16October2016.
50. Wan,R.;Mei,S.;Wang,J.;Liu,M.;Yang,F. Multivariatetemporalconvolutionnetwork:Adeepneuralnetworksapproachfor
multivariatetimeseriesforecasting. Electronics2019,8,876.[CrossRef]
51. Gopali,S.;Abri,F.;Namini,S.;Namin,A. AcomparisonofTCNandLSTMmodelsindetectinganomaliesintimeseriesdata. In
Proceedingsofthe2021IEEEInternationalConferenceonBigData,Orlando,FL,USA,15–18December2021.
52. Salinas, D.; Bohlke-Schneider, M.; Callot, L.; Medico, R.; Gasthaus, J. High-dimensionalmultivariateforecastingwithlow
rankGaussiancopulaprocesses. InAdvancesinNeuralInformationProcessingSystems;MITPress:Cambridge,MA,USA,2019;
pp.7796–7805.
53. Rangupuram,S.;Seeger,M.;Gasthaus,J.;Stella,L.;Wang,Y.;Januschowski,T.Deepstatespacemodelsfortimeseriesforecasting.
InAdvancesinNeuralInformationProcessingSystems;MITPress:Cambridge,MA,USA,2018.
54. Lim,B.;Zohren,S.;Roberts,S. LearningindependentBayesianfilteringstepsfortimeseriesprediction. InProceedingsofthe
InternationalJointConferenceonNeuralNetworks,Glasgow,UK,19–24July2020.
55. Hochreiter,S.;Schmidhuber,J. Longshort-termmemory. NeuralComput.1997,9,1735–1780.[CrossRef]
56. Vaswani,A.;Shazeer,N.;Parmar,N.;Urzkoreit,J.;Jones,L.;Gomez,A.;Kaiser,L.;Polosukhin,I. Attentionisallyouneed. arXiv
2017,arXiv:1706.03762v7.
57. Han,K.;Xiao,A.;Wu,E.;Guo,J.;Xu,C.;Wang,Y. Transformerintransformer. arXiv2021,arXiv:2103.00112v3.
58. Su,L.;Zuo,X.;Li,R.;Wang,X.;Zhao,H.;Huang,B. Asystematicreviewfortransformer-basedlong-termseriesforecasting.
Artif.Intell.Rev.2025,58,80.[CrossRef]
59. Grigsby, J.; Wang, Z.; Nguyen, N.; Qi, Y. Long-range transformers for dynamic spatiotemporal forecasting. arXiv 2021,
arXiv:2109.12218v3.
60. Hastie,T.;Tibshirani,R.;Friedman,J. TheElementsofStatisticalLearning;Springer:NewYork,NY,USA,2019.
61. Freund,Y.;Schapire,F. Adecision-theoreticgeneralizationofonlinelearningandanapplicationtoboosting. J.Comput.Syst.Sci.
1997,55,119–139.[CrossRef]
62. Ke,G.;Meng,Q.;Finley,T.;Wang,T.;Chen,W.;Ma,W.;Ye,Q.;Liu,T.-Y. Light-GBMAhighlyefficientgradientboostingtree.In
AdvancesinNeuralInformationProcessingSystems;Gyon,I.,Luxburg,U.,Bengio,S.,Wallach,H.,Fergus,K.,Vishwanathan,S.,
Garnett,R.,Eds.;CurranAssociates,Inc.:NewYork,NY,USA,2017.
63. Wang,M.;Hamidian,N.;Wisam,E. WhatAretheBestPracticesforScalingMachineLearningAlgorithmswithBigData. Posted
onLinkedinApril2024.Availableonline:https://www.linkedin.com/advice/0/what-best-practices-scaling-machine-learning-
algorithms-nxh1c(accessedon12December2024).
64. Palifka,B. UnderstandingMachineLearningAlgorithms:TrainingTimeandInferenceTimeComplexity. PostedonLinkedin
August2024.Availableonline:https://www.linkedin.com/pulse/understanding-machine-learning-algorithms-training-time-
bill-palifka-sqike(accessedon12December2024).
65. Ying,X. Anoverviewofoverfittinganditssolutions. J.Phys.Conf.Ser.2018,1168,022022.[CrossRef]
66. Hassija,V.;Chamola,V.;Mahapatra,A.;Singai,A.;Goel,D.;Huang,K.;Scardapane,S.;Spinelli,I.;Mahmud,M.;Hussain,A.
Interpretingblack-boxmodels:Areviewonexplainableartificialintelligence. Cogn.Comput.2024,16,45–74.[CrossRef]
67. Azodi,C.;Tang,J.;Shiu,S.H. Openingtheblackbox:Interpretablemachinelearningforgenetists. TrendsGenet.2020,36,442–453.
[CrossRef]
68. Medeiros,M.;Vasconcelos,G.;Veiga,Á.;Zilberman,E. Forecastinginflationinadata-richenvironment:Thebenefitsofmachine
learningmethods. J.Bus.Econ.Stat.2021,39,98–119.[CrossRef]
69. Shapley,L. Notesonthen-PersonGame-II:TheValueofann-PearsonGame; PDF-Document;RandCorporation:SantaMonica,CA,
USA,1951.
70. Lundberg, S.; Lee, S.I. Aunifiedapproachtointerpretingmodelpredictions. InProceedingsoftheNIPS’17: Proceedings
ofthe31stInternationalConferenceonNeuralInformationProcessingSystems,LongBeach,CA,USA,4–9December2017;
pp.4765–4774.
71. Lundberg,S.;Erion,G.;Lee,S.I. Consistentindividualizedfeatureattributionfortreeensembles. arXiv2018,arXiv:1802.03888.
72. Ribeiro,M.;Singh,S.;Guestrin,C. WhyshouldItrustyou?:Explainingthepredictionsofanyclassifier. InProceedingsofthe
ACMSIGKDDInternationalConferenceonKnowledgeDiscovryandDataMining,SanFrancisco,CA,USA,13–17August2016;
pp.1135–1144.
73. Visami,G.;Bagli,E.;Chesani,F.;Poluzzi,A.;Capuzzo,D. StatisticalstabilityindicesforLIMEobtainingreliableexplanationsfor
machinelearningmodels. arXiv2020,arXiv:2001.11757v2.
74. Nohara, Y.; Matsumoto, K.; Soejima, H.; Nakashima, N. Explanation of machine learning models using Shapley additive
explanationandapplicationforrealdatainhospital. Comput.MethodsProgramsBiomed.2022,214,106584.[CrossRef]

Entropy2025,27,279 31of34
75. Rudin,C. Stopexplainingblackboxmachinelearningmodelsforhighstakesdecisionanduseinterpretablemodelsinstead. Nat.
Mach.Intell.2019,1,206–2015.[CrossRef][PubMed]
76. Hyndman,R. Abriefhistoryofforecastingcompetitions. Int.J.Forecast.2020,36,7–14.[CrossRef]
77. Makridakis,S.;Andersen,A.;Carbone,R.;Fildes,R.;Hibon,M.;Lewandowski,R.;Newton,J.;Parzen,E.;Winkler,R. The
accuracyofextrapolation(timeseries)methods:Resultsofaforecastingcompetition. J.Forecast.1982,1,11–153.[CrossRef]
78. Makridakis, S.; Chatfield, C.; Hibon, M.; Lawrance, M.; Mills, T.; Ord, K.; Simmons, L. The M2 competition: A real-time
judgementallybasedforecastingstudy. Int.J.Forecast.1993,9,5–22.[CrossRef]
79. Makridakis,S.;Spiliotis,E.;Assimakopoulos,V. TheM4competition: 100,000timeseriesand61forecastingmethods. Int. J.
Forecast.2020,36,54–74.[CrossRef]
80. Makridakis,S.;Spiliotis,E.;Assimakopoulos,V. M5accuracycompetition:Results,findingandconclusions. Int.J.Forecast.2022,
38,1346–1364.[CrossRef]
81. Makridakis,S.;Spiliotis,E.;Holly,R.;Petropoulos,F.;Swanson,N.;Gaba,A. TheM6forecastingcompetition:Bridgingthegap
betweenforecastingandinvestmentdecisions. arXiv2023,arXiv:2310.13357.[CrossRef]
82. Small,S. Ahybridmethodofexponnetialsmoothingandrecurrentneuralmetworksintimeseriesforecasting. Int.J.Forecast.
2020,36,75–85.[CrossRef]
83. Bates,J.;Granger,C. ThecombinationofForecasts. J.Oper.Res.1969,20,451–468.[CrossRef]
84. Claeskens,G.;Magnus,J.;Vasnev,A.;Wang,W.Theforecastcombinationpuzzle:Asimpletheoreticalexplanation. Int.J.Forecast.
2016,32,754–762.[CrossRef]
85. Taleb,N. BlackSwan—TheImpactoftheHighlyImprobable;RandomHouse:NewYork,NY,USA,2010.
86. Fry,C.;Brundage,M. TheM3forecastingcompetition—Apractioneer’sview. J.Forecast.2020,36,156–160.[CrossRef]
87. Farrel,M.;Liang,T.;Misra,S. Deepneuralnetworksforestimationandinference. Econometrica2021,89,181–213.[CrossRef]
88. Otneim,H.;Tjøstheim,D. ConditionaldensityestimationusinglocalGaussiancorrelation. Stat. Comput. 2018,28,303–321.
[CrossRef]
89. Diebold,F.;Mariano,R. Comparingpredictiveaccuracy. J.Bus.Econ.Stat.1995,29,253–263.[CrossRef]
90. Gneiting,T.;Ranjan,R. Comparingdensityforecastsusingthreshold-andquantile-scoringrules. J.Bus. Econ. Stat. 2011,
29,411–422.[CrossRef]
91. Gneiting,T. Editorial:Probabilisticforecasting. J.R.Stat.Soc.Ser.A2008,171,319–321.[CrossRef]
92. Gneiting,T.;Katzfuss,M. Probabilisticforecasting. Annu.Rev.Stat.ItsAppl.2014,1,125–131.[CrossRef]
93. Lerch,S.;Thorarinsdottir,T.;Ravazzolo,F.;Gneiting,T. Forecaster’sdilemma:Extremeeventsandforecastevaluation. Stat.Sci.
2017,32,106–127.[CrossRef]
94. Gneiting,T.;Ranjan,R. Combiningpredictivedistributions. Electron.J.Stat.2013,7,1747–1782.[CrossRef]
95. Salinas,D.;Flunkert,V.;Gasthaus,J.;Januschowsi,T. DeepAR:Probabilisticforecastingwithautoregressiverecurrentnetworks.
Stat.Sci.2020,36,1181–1191.[CrossRef]
96. Croston,J. Forecastingandstockcontrolforintermittentdemands. Oper.Res.Q.1972,23,289–304.[CrossRef]
97. Gasthaus,J.;Benidis,K.;Wang,Y.;Rangapuram,S.;Salinas,D.;Flunkert,V.;Januschowski,T. Probabilisticforecastingwithspline
quantilefunctionRNNs. InProceedingsofthe22ndInternationalConferenceonArtificialIntelligenceandStatisticsAIS-TATS,
Naha,Japan,16–18April2019.
98. Wen,R.;Torkkola,K. Deepgenerativequantile-copulamodelsforprobabilisticforecasting. ICMLTimeSeriesWorkshop.arXiv
2019,arXiv:1907.10697.
99. Engle,R. AutoregressiveconditionalheteroscedasticitywithestimatesofthevarianceofUnitedKingdominflation. Econometrica
1982,50,987–1007.[CrossRef]
100. Engle,R.;Bollerslev,T. Modellingthepersistenceofconditionalvariances. Econom.Rev.1986,5,1–50.[CrossRef]
101. Shephard,N.;Andersen,T. Stochasticvolatility:Originsandoverview.InHandbookofFinancialTimeSeries;Andersen,T.,Davis,
R.,Kreiss,J.P.,Mikosch,T.,Eds.;Springer:NewYork,NY,USA,2009;pp.233–254.
102. Andersen,T.;Bollerslev,T.;Diebold,F.;Ebens,H. Thedistributionofrealizedstockreturnvolatility. J.Financ. Econ. 2001,
61,43–76.[CrossRef]
103. Barndorff-Nielsen,O.;Shephard,N. Econometricanalysisofrealizedvolatilityanditsuseinestimatingstochasticvolatility
models. J.R.Stat.Soc.Ser.B2002,64,253–280.[CrossRef]
104. Liu,L.;Patton,A.;Sheppard,K. Doesanythingbeat5-minuteRV:Acomparisonofrealizedmeasuresacrossmultipleasset
classes. J.Econom.2015,187,293–311.[CrossRef]
105. Zhang,C.;Zhang,Y.;Cucuringu,M.;Qian,Z. Volatilityforecastingwithmachinelearningandintradaycommonality. Financ.
Econom.2024,22,492–530.[CrossRef]
106. Andersen, T.; Bollerslev, T.; Meddahl, N. Analyticalevaluationofvolatilityforecasts. Int. Econ. Rev. 2004, 45,1079–1110.
[CrossRef]

Entropy2025,27,279 32of34
107. Izzeldin,M.;Hassan,M.;Pappas,V.;Tsionas,M. ForecastingrealisedvolatilityusingARFIMAandHARmodels. Quant.Financ.
2019,19,1627–1638.[CrossRef]
108. Karolyi,G.;Lee,K.H.;Dijk,M.V. Understandingcommonalityinliquidityaroundtheworld. J.Financ.Econ.2012,105,82–112.
[CrossRef]
109. Dang,T.;Moshirian,F.;Zhang,B. Commonalityinnewsaroundtheworld. J.Financ.Econ.2015,116,82–110.[CrossRef]
110. Corsi,F. Asimpleapproximatelong-memorymodelofrealizedvolatility. J.Financ.Econ.2009,7,174–196.[CrossRef]
111. Amirshahi,B.;Lahmiri,S. HybriddeeplearningandGARCH-familymodelsforforecastingvolatilityofcryptocurrencies. Mach.
Learn.Appl.2023,12,100465.[CrossRef]
112. Almog,A.;Shmuli,E.Structuralentropy:Monitoringcorrelation-basednetworksovertimewithapplicationstofinancialmarkets.
Sci.Rep.2019,9,10832.[CrossRef]
113. Wang,S.;Khan,S.;Munir,M.;Alhajj,R.;Khan,Y. Entropy-basedfinancialassetpricing:EvidencefromPakistan. PLoSONE2022,
17,e0278236.[CrossRef]
114. Musmeci,N.;Aste,T.;Matteo,T. Interplaybetweenpastmarketcorrelationstructurechangesandvolatilityoutbursts. Sci.Rep.
2016,6,36320.[CrossRef][PubMed]
115. Rodriguez-Rodriguez,N.;Miramontes,O. Shannonentropy:AneconophysicalapproachtoCryptocurrencyportfolios. Entropy
2022,24,1583.[CrossRef]
116. Drzazga-Szczesniak,E.;Szczpanik,P.;Kaczmarek,A. Entropyoffinancialtimeseriesduetotheshockofwar. Entropy2023,
25,823.[CrossRef][PubMed]
117. Shih,S.Y.;Sun,F.K.;Lee,H.Y.Temporalpatternattentionformultivaritetimeseriesforecasting. Mach.Learn.2019,108,1421–1441.
[CrossRef]
118. Nketiah, E.; Chenlong, L.; Yingchuan, J.; Aram, S. Recurrent neural network modeling of multivariate time series and its
applicationtotemperatureforecasting. PLoSONE2023,18,e0285713.[CrossRef]
119. Kumar,P.;Priyanka,P.;Dhanya,J.;Uday,K.;Dutt,V. Analyzingtheperformanceofunivariateandmultivariatemachinelearning
modelsinsoilmovementprediction:Acomparisonstudy. IEEEAccess2023,11,62368–62381.[CrossRef]
120. Pesaran,M.;Pick,A.;Timmerman,A. Forecastingwithpaneldata:Estimationuncertaintyversusparameterheterogeneity. arXiv
2024,arXiv:2401.11198v1.[CrossRef]
121. Chronopoulos,I.;Chrysikou,K.;Kapetanios,G.;Mitchell,J.;Raftapostolos,A. Deepneuralnetworkestimationinpanelmodels.
arXiv2023,arXiv:2305.19921.
122. Engle,R.;Granger,C. Cointegrationanderrorcorrection:Representation,estimationandtesting. Econometrica1987,55,251–276.
[CrossRef]
123. Johansen,S. Statisticalanalysisofcointegratingvectors. J.Econ.Dyn.Control1988,12,231–254.[CrossRef]
124. Escribano,A.;Wang,D. Mixedrandomforest,cointegration,andforecastinggasolineprices. Int.J.Forecast.2021,37,1442–1462.
[CrossRef]
125. Du,J. Mean-varianceportfoliooptimizationwithdeeplearningbased-forecastsforcointegratedstocks. ExpertSyst.Appl.2022,
201,117005.[CrossRef]
126. El-Menshawry,M.;Ellwa,M.;EL-Essa,L.;El-Morshedy,M.;Sagheer,R. Enhancingintegertimeseriesmodelestimationthrough
neural-basedfuzzytimeseriesanalysis. Symmetry2024,16,660.[CrossRef]
127. Snyder, R.; Ord, J.; Beaumont, A. Forecastingtheintermittentdemandforslow-movinginventories. Int. J.Forecast. 2012,
28,485–496.[CrossRef]
128. Rydberg,T.;Shephard,N.BINmodelsfortrade-tradedata.Modellingthenumberoftradesinafixedtimeinterval. InEconometric
SocietyWorldCongress2000ContributedPapers;EconometricSociety:NewHaven,CT,USA,2000.
129. Ferland,R.;Latour,A.;Oraichi,D. Integer-valuedGARCHprocess. J.TimeSer.Anal.2006,27,923–942.[CrossRef]
130. Fokianos,K.;Rahbek,A.;Tjøstheim,D. Poissonautoregression. J.Am.Stat.Assoc.2009,104,1430–1439.[CrossRef]
131. Weiss,C. AnIntroductiontoDiscrete-ValuedTimeSeries;Wiley:NewYork,NY,USA,2018.
132. Eyjolfsson,H.;Tjøstheim,D. Self-exitingjumpprocesseswithapplicationstoenergymarkets. Ann. Inst. Stat. Math. 2018,
70,373–393.[CrossRef]
133. Eyjolfsson, H.; Tjøstheim, D. Multivariate self-exciting jump processes with applications to financial data. Bernoulli 2023,
29,2167–2191.[CrossRef]
134. Aït-Sahalia,Y.;Cacho-Diaz,J.;Laeven,R. Modelingfinancialcontagionusingmutuallyexcitingjumpprocesses. J.Financ.Econ.
2015,117,585–606.[CrossRef]
135. Malaviya,J. SurveyonmodelingintensityfunctionofHawkesprocessusingneuralmodels. arXiv2020,arXiv:2014.11092v1.
136. Creal,D.;Koopman,S.;Lucas,A. Generalizedautoregressivescoremodelswithapplications. J.Appl.Econom.2013,28,777–795.
[CrossRef]
137. Artemova,M.;Blasques,F.;vonBrummelen,J.;Koopman,S. Score-drivenmodels:Methodologyandtheory. InOxfordResearch
EncyclopediaofEconomicsandFinance;OxfordUniversityPress:Oxford,UK,2022.

Entropy2025,27,279 33of34
138. Newman,M. Networks,2nded.;OxfordUniversityPress:Oxford,UK,2020.
139. Crane,H. ProbabilisticFoundationsofStatisticalNetworkAnalysis;ChapmanandHall:London,UK,2018.
140. Tjøstheim,D.;Jullum,M.;Løland,A. Somerecenttrendsinembeddingsoftimeseriesanddynamicnetworks. J.TimeSer.Anal.
2023,44,686–709.[CrossRef]
141. Zhu,X.;Pan,R.;Li,G.;Liu,Y.;Wang,H. Networkvectorautoregression. Ann.Stat.2017,45,1096–1123.[CrossRef]
142. Ludkin,M.;Eckley,I.;Neal,P. Dynamicstochasticblockmodels:Parameterestimationanddetectionincommunitystructure.
Stat.Comput.2018,28,1201–1213.[CrossRef]
143. Krampe,J. Timeseriesmodelingondynamicnetworks. Electron.J.Stat.2019,13,4945–4976.[CrossRef]
144. Armillotta,M.;Fokianos,K.;Krikidis,I. Generalizedlinearmodelsnetworkautoregression. InProceedingsoftheInternational
ConferenceonNetworkScience,Porto,Portugal,8–11February2022.
145. Armillotta,M.;Fokianos,K. Poissonnetworkautoregression. arXiv2021,arXiv:2104.06296v3.
146. Armillotta,M.;Fokianos,K. Testinglinearityfornetworkautoregressivemodels. arXiv2022,arXiv:2202.03852v1.
147. Armilotta,M.;Fokianos,K. Nonlinearnetworkautoregression. Ann.Stat.2023,51,2526–2552.[CrossRef]
148. Richardson,L. WeatherPredictionbyNumericalProcess;CambridgeMathematicalLibrary:Cambridge,UK,1922.
149. Wiin-Nielsen,A. Thebirthofnumericalweatherprediction. Tellus1991,43,36–52.[CrossRef]
150. Lynch,P. Theorigensofcomputerweatherpredictionandclimatemodeling. J.Comput.Phys.2008,227,4331–4344.[CrossRef]
151. Bauer,P.;Thorpe,A.;Brunet,G. Thequietrevolutionofnumericalweatherforecasting. Nature2015,525,47–55.[CrossRef]
152. Bannister,R. Areviewofoperationalmethodsofvariationalandensemblevariationaldataassimilation. Q.J.R.Meteorol.Soc.
2007,143,607–633.[CrossRef]
153. Chen,L.;Han,B.;Wang,X.;Zhao,J.;Yang,W.;Yang,Z. Machinelearningmethodsinweatherandclimateapplications. Appl.Sci.
2023,13,12019.[CrossRef]
154. Krasnopolsky,V.;Fox-Rabinovitz,M.;Hou,Y.;Lord,S.;Belochiski,A. Accurateandfastneuralnetworkemulationsofmodel
radiationtotheNCEPcoupledclimateforecastsystem:Climatesimulationsandseasonalpredictions. Mon.WeatherRev.2010,
138,1822–1842.[CrossRef]
155. Markakis,E.;Papadopoulos,A.;Perakis,P. Spatio-temporalforecasting:Asurvey. arXiv2018,arXiv:1806.06571.
156. Schultz,M.;Betancourt,C.;Gong,B.;Kleinert,F.;Langgut,M.;Leufen,L.;Mozaffari,A.;Stadtler,S. Candeeplearningbeat
numericalweatherforecasting? Philos.Trans.A2020,379,1–22.
157. Yang,R.;Hu,J.;Li,Z.;Mu,J.;Yu,T.;Li,J.X.;Dasgupta,A.;Xiong,H. Interpretablemachinelearningforweatherandclimate
prediction:Areview. Atmos.Environ.2024,338,120797.[CrossRef]
158. Reichstein,M.; Camps-Valls,G.; Stevens,B.; Jung,M.; Denzler,J.; Carvalhais,J. Deeplearningandprocessunderstanding
ofdata-drivenearthsystemscience. Nature2019,566,195–204; 2024updatebyReichstein,Baghirov,JungandKraft,EGU
abstract2024.[CrossRef]
159. Lee,T.;Roy,S.;Kumar,A.;Ramachandran,R.;Nair,U. LongtermforecastingofenvironmentvariablesofMERRA2basedon
transformers. InProceedingsoftheEuropeanGeosciencesUnion(EGU)GeneralAssembly2023,Vienna,Austria,24–28April
2023;NASAHeadquarterReport.
160. Vannitsen,S.;Bremnes,J.B.;Demaeyer,J.;Evans,G.;Flowerdew,J.;Hemri,S.;Lerch,S.;Roberts,N.;Theis,S.;Atencia,A.;etal.
Statisticalpostprocessingforweatherforecasts:Review,challenges,andavenuesinabigDataWorld. Bull.Am.Meteor.Soc.2021,
102,E681–E699.[CrossRef]
161. Chen,J.;Janke,T.;Steinke,F.;Lerch,S. Generativemachinelearningmethodsformultivariatepostprocessing. Ann.Appl.Stat.
2024,18,159–183.[CrossRef]
162. Righby,R.;Stasinopoulos,D. Generalizedadditivemodelsforlocation,scaleandshape. J.R.Stat.SociteySer.C2005,54,507–554.
[CrossRef]
163. McGovern,A.;Elmore,K.;Gagne,D.;Haupt,S.;Kartens,C.;Lagerquist,R.;Smith,T.;Williams,J. Usingartificialintelligenceto
improvereal-timedecision-makingforhigh-impactweather. Bull.Am.Meteor.Soc.2017,98,2073–2090.[CrossRef]
164. McGoverns,A.;Jergerson,G.;Elmore,K.;Homeyer,C.;Smith,T. Understandingthephysicalimplicationsofmachinelearning.
Bull.Am.Meteor.Soc.2019,100,2175–2199.[CrossRef]
165. Molnar, C. InterpretableMachineLearning. AGuideforMakingBlackBoxModelsExplainable; IndependentlyPublished, 2022.
Availableonline:https://christophm.github.io/interpretable-ml-book/(accessedon12December2024).
166. Miftachov,R.;Keilbar,G.;Härdle,W. Shapleycurves:Asmoothingperspective. J.Bus.Econ.Stat.2024,42,1–12.[CrossRef]
167. Nerini,D.;Foresti,L.;Leuenberger,D.;Robert,S.;German,U. AreducedspaceensembleKalmanfilterapproachforflow-
dependentintegrationforradarextrapolationnowcastsandNWPprecipitationensembles. Mon.WeatherRev.2019,147,987–1006.
[CrossRef]
168. Alerskans,E.;Nyborg,J.;Birk,M.;Kaas,E. Atransformerneuralnetworkforpredictingnear-surfacetemperature. Meteorol.
Appl.2022,29,e2098.[CrossRef]

Entropy2025,27,279 34of34
169. Bouallegue,Z.;Weyn,J.;Clare,M.;Dramsch,J.;Dueben,P.;Chantry,M. Improvingmedium-rangeensembleweatherforecasts
withhierarchicalensembletransformers. Artif.Intell.EarthSyst.2024,3,e230027.[CrossRef]
170. Piron,M.J.;Wang,X.;Kim,H.;Kwon,H. Precipitationnowcastingusingtransformer-basedgenerativemodelsandtransfer
learningforimproveddisasterpreparedness. Int.J.Appl.EarthObs.Geoinf.2024,132,103962.[CrossRef]
171. Hewage,P.;Behera,A.;Trovati,M.;Pereira,E.;Ghahremani,M.;Palmieri,F.;Liu,Y. Temporalconvolutionneural(TCN)network
foraneffectiveweatherforecastingusingtimeseriesdatafromthelocalweatherstation. SpringerNat.Link2020,24,16453–16482.
172. Zhu,J.;Su,L.;Li,Y. WindpowerforecastingbasedonnewhybridmodelwithTCNresidualmodification. EnergyAI2022,
10,100199.[CrossRef]
173. Sanchez-Lengeling, B.; Reif, E.; Pearce, A.; Wiltschko, A. A gentle introduction to graph neural networks. Distill 2021, 6.
[CrossRef]
174. Joshi,C. TransformersAreGraphNeuralNetworks; NTUGraphDeepLearningLab:Singapore,2020.
175. Lam, R.; Sanchez-Gonzales, A.; Willson, M.; Wirnsberger, P.; Battaglia, P.; Fortunato, M.; Alet, F.; Ravuri, S.; Ewalds, T.;
Eaton-Rosen,Z.;etal. Learningskillfulmedium-rangeglobalweatherforecasting. Science2023,382,1416–1421.[CrossRef]
176. Keisler,R. Forecastingglobalweatherwithgraphneuralnetworks. arXiv2022,arXiv:2202.07575.
177. Price,I.;Sanchez-Gonzales,A.;Alet,F.;Andersson,T.;El-Kadi,A.;Masters,D.;Ewalds,T.;Stott,J.;Mohamed,S.;Battaglia,
P.;etal. Probabilisticweatherforecastingwithmachinelearning. Nature2024,637,84–90.[CrossRef]
178. Bonavita, M. On some limitaions of current machine learning weather prediction models. Geophys. Res. Lett. 2024, 51,
e2023GL107377.[CrossRef]
179. Kitsios,V. AIWeatherModelsCanNowBeattheBestTraditionalForecasts; CSIROreport;CSIRO:Canberra,Australia,2024.
180. Kochkow,D.;Yuval,J.;Langmore,I.;Norgaard,P.;Smith,J.;Mooers,G.;Klöwer,M.;Lottes,J.;Rasp,S.;Düben,P.;etal. Neural
generalcirculationmodelsforweatherandclimate. Nature2024,632,1060–1066.[CrossRef][PubMed]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.