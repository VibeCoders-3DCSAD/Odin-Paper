Predict, Optimize, Deliver: Demand Forecasting and Resource
Optimization for a Market Research Firm
∗
Ma. TheresaGMariano RichardNMonreal
SchoolofGraduateStudies SchoolofGraduateStudies
MapuaUniversity MapuaUniversity
Makati,Philippines Makati,Philippines
mtgmariano@mymail.mapua.edu.ph rmonreal@mapua.edu.ph
Abstract TitleofthePaper:ACMConferenceProceedingsManuscriptSub-
Inprofessionalserviceindustries,wherehumanresourcescould missionTemplate:Thisisthesubtitleofthepaper,thisdocument
drivebothcostandvalue,accurateforecastingandintelligentre- bothexplainsandembodiesthesubmissionformatforauthorsus-
source allocation were critical to sustaining operational perfor- ingWord. InWoodstock’18: ACMSymposiumonNeuralGaze
mance. Tothisend,thispaperdevelopedanintegratedforecast- Detection,June03–05,2018,Woodstock,NY.ACM,NewYork,NY,
ingandoptimizationframeworktoaddressdemanduncertainty USA,10pages. NOTE:Thisblockwillbeautomaticallygenerated
andresourceallocationchallengesinamarketresearchfirm. The whenmanuscriptsareprocessedafteracceptance
studycomparedARIMA,Holt–Winter’sExponentialSmoothing,
ACMReferenceFormat:
Prophet,andLSTMmodelsintermsofservicelevelaccuracy,as- Ma.TheresaGMarianoandRichardNMonreal.2025.Predict,Optimize,
sessedviaMAE,RMSE,andMAPEacrossmultipletraining–test Deliver:DemandForecastingandResourceOptimizationforaMarketRe-
splitsanda30-dayhold-outperiod.Amongtheevaluatedmethods, searchFirm.InThe9thInternationalConferenceonBusinessandInformation
Prophetdemonstratedthehighestoveralleffectiveness,offering Management(ICBIM2025),September19–21,2025,Bangkok,Thailand.ACM,
arobustbalancebetweenforecastaccuracy,interpretability,and NewYork,NY,USA,10pages.https://doi.org/10.1145/3785171.3785187
operationalusability,especiallyforshort-termplanninghorizons.
TheselectedforecastswerethenoperationalizedusingaPyomo- 1 INTRODUCTION
basedprescriptiveoptimizationmodelthatallocatedworkforce
Forthesubjectcompany,whereclientneedsarehighlyvariable,
resourcesinalignmentwithanticipatedservicedemand,subject
effectiveresourceallocationisessentialtomaintainingoperational
toconstraintssuchasemployeeavailabilityandclient-specificre-
efficiencyandprofitability. Consultingcompaniesexperiencefluc-
quirements.ForecastbandsderivedfromRMSEwereintroducedto
tuatingservicerequeststiedtoclientbehaviorandprojecttimelines
simulateover-andunder-forecastingscenarios,strengtheningthe
[1].Sincemanpoweristheprimaryassetinsuchfirms,delaysor
model’sresilienceandresponsivenessinallocationstrategies.The
inefficienciesinstaffingleadtomisseddeadlinesandpotentialrev-
finalframeworkwasdeployedwithinaninteractivePowerBIenvi-
enueloss[2].AccordingtoResource-BasedTheory(RBT),optimal
ronment,providingdynamicvisualizationsandsupportingagile,
internalresourcedeploymentcontributestosustainedcompetitive
cost-effectiveworkforceplanning. Overall,thisstudycontributed
advantage[3],especiallyinoutsourceddeliverymodelssuchasthe
apractical,data-drivenapproachthatbridgedpredictiveanalytics
studiedcompany,whichconducts70%ofitsoperationsthroughits
andoperationalplanning,offeringactionableinsightsforresource
Manila-basedservicecenter.
optimizationinprofessionalserviceindustries.
Inthisstudy,thesubjectfirmhandlesclient-specific“demand”
definedinhoursacrossservicecategories,eachvaryingincom-
CCSConcepts
plexityandprocessingtime.Demandsurgesunpredictably,often
•InformationSystems;•DecisionSupportSystems;•Data requiringoverlappingworkforcedeployment.Forexample,Client
Analytics; 1typicallyrequires2-3full-timeequivalents(FTEs),increasingto4
duringpeakperiods,whileClient2presentsmoreerraticspikes.
Keywords ManualworkforceplanninglikeMSExcelfailstoadapttosuch
ResourceOptimization,predict-then-optimizeFirstAuthor’sName, volatility.WhilelargeenterprisesleverageERPplatformslikeSAP
Initials,andLastName,SecondAuthor’sName,Initials,andLast orOracle[4],smallerfirmsmustchoosebetweenprebuilttools
Name,andThirdAuthor’sName,Initials,andLastName.2018.The andcustommodels[5].Forecastaccuracyiscriticalasfailureslike
thoseexperiencedatHeathrowAirporthaveshownthatpoorde-
∗CorrespondingAuthor mandpredictioncantriggersystemicdisruption[6]. Selectingthe
rightforecastingapproachrequiresevaluatingtrade-offsbetween
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor accuracy,complexity,andinterpretability,especiallyindynamic
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed serviceenvironments[7].
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation
ThisstudyproposedanintegratedsolutionusingaPredict-Then-
onthefirstpage.Copyrightsforthird-partycomponentsofthisworkmustbehonored.
Forallotheruses,contacttheowner/author(s). Optimize(PO)frameworkthatcombinedtime-seriesforecasting
ICBIM2025,Bangkok,Thailand withnetworkflow-basedresourceallocation. Demandwasfirst
©2025Copyrightheldbytheowner/author(s).
forecastedusingfourtechniques,specificallyARIMA,Holt-Winters,
ACMISBN979-8-4007-2217-2/2025/09
https://doi.org/10.1145/3785171.3785187 LSTM,andProphet. Thesewereusedtoinformanoptimization
103

ICBIM2025,September19–21,2025,Bangkok,Thailand Ma.TheresaMarianoandRichardMonreal
modelthatrespectedreal-worldconstraintssuchaswork-hourcaps settingssuchasretail[19],energydemand[20],andfinancialfore-
andsharedstaffing.TheresultswerevisualizedinaPowerBIdash- casting [18], making it a compelling choice for firms balancing
boardforoperationaltransparency.Theobjectivewastoenhance usabilitywithprecision.
resourceefficiency,alignstaffingtofluctuatingservicedemand, Toevaluatethesemodelsfairly,thestudyemploysatriadofper-
anddemonstratehowadvancedanalyticscanempowermidsize formancemetrics:RMSE,whichpenalizeslargeforecastdeviations;
firms.Thisworkcontributedbyidentifyingthemostsuitablefore- MAE,whichcapturesaverageabsoluteerror;andMAPE,which
castingmethodforaprofessionalservicingfirm,operationalizing offerspercentage-basedinterpretability[21]. AlthoughMAPEcan
data-drivenallocationstrategies,anddeliveringactionableinsights exaggerateerrorswhenactualvaluesaresmall,thecombinationof
throughausable,visualplatform. ThissupportedSDG8bypro- thesemetricsensuresaholisticassessment.Notably,comparative
motingsustainableemploymentpractices, SDG9byadvancing studiesincallcenterstaffinghighlighthowARIMAandProphet
data-drivendecision-makinginmid-sizedfirms,andSDG17by differintheirsensitivitytothesemetrics[22].
fosteringcollaborationbetweenanalyticsteams,operations,the However, forecasting is only the first step. What follows is
academeandstrategicplanners. thecriticalchallengeofresourceallocation,whichisturningpre-
dictionsintooptimaldeploymentstrategies. Toachievethis,the
studydrewfromnetworkflowoptimization,amethodthathas
2 LITERATUREREVIEW
gainedtractionindomainssuchassemiconductorsupplychains
Timeseriesforecastingassumesthatfutureoutcomesareexten- [23],telecommunications[24],andworkforcemanagement[25].
sionsofhistoricaldata,governedbytrends,seasonality,cycles,and Thesemodelstreatstaffingasaflowproblem,balancingsupply(em-
randomness[8]. Forindustriesthatrelyontime-boundoutputs, ployeeavailability),demand(workloadforecasts),andoperational
particularlythesamplecompanywherestaffinganddemandshift constraints.
rapidly, accurate forecasting becomes crucial. To this end, this Solvingsuchmodelsefficientlyrequiresarobustoptimization
studyinvestigatesfourprominentforecastingmethods,specifically engine. The study thus adopted CPLEX, a solver widely recog-
ARIMA,Holt-Winters,LSTM,andProphet,whileassessingtheir nizedforitsspeedandreliabilityinhandlinglarge-scale,resource-
performanceusingRMSE,MAE,andMAPEmetrics. constrainedschedulingproblems[26–28].CPLEXwasintegrated
WebeginwithARIMA,aclassicalyetwidelyadoptedmodel. viaPythontosolvetheformulatedminimum-costflowproblem,
Itsstrengthisobservedinhandlingstationarytimeseries,with ensuringalignmentbetweenforecasteddemandandresourceavail-
well-documentedapplicationsinsupplychain[9],healthcare[10], abilitywhilehonoringbusinessconstraintslikework-hourcaps,
andcloudresourceplanning[11]. However, asdemandsignals sharedlaborpools,andleaveschedules[29,30].
becomemorevolatileandirregularinmodernserviceoperations, Toensurethesetechnicaloutputsremainactionablefordecision-
ARIMA’slimitationsincapturingseasonalityandnonlineartrends makers, thefinallayerofthesolutionstackinvolveddatavisu-
emergeascriticalgaps,therebymotivatingthesearchformore alization. Here,PowerBIwasselectedforitscost-effectiveness,
adaptivealternatives. nativeMicrosoftintegration,andstrengthinrenderinginteractive
In response, Holt-Winters Exponential Smoothing builds on dashboards [31, 32]. With built-in support for time-series plot-
ARIMA’sstrengthsbyintegratinglevel,trend,andseasonalcom- ting,matrixviews,andslicers[33],itcouldempowerstakeholders
ponentsthroughflexiblesmoothingparameters(𝛼,𝛽,𝛾)[12,13]. toexploreforecasttrends, trackfulfillmentlevels, andsimulate
Thisallowsthemodeltodynamicallyadjusttorecentobservations, resourcingscenarios,bridgingthegapbetweendatascienceand
makingitwell-suitedfordatathatevolveovertime.Dependingon operationalstrategy.
whetherseasonalvariationsremainconstantorscalewithmagni- Despitetheseadvancements,gapsintheliteraturepersist.Most
tude,themodelshiftsbetweenadditiveandmultiplicativeforms forecasting-optimizationframeworkstargetproduct-basedorstatic
[14].Suchadaptabilityhasprovenusefulinreal-timeapplications, planning contexts, with limited relevance to the time-sensitive,
includingepidemiologicalforecasting[14]. high-variancenatureofprofessionalservices.Fewstudiesexplored
Yet,evenwithenhancedseasonalityhandling,bothARIMAand how interpretability and granularity trade-offs influence model
Holt-Wintersassumelargelylinearpatterns.Forserviceenviron- selectioninsuchenvironments.Moreover,visualizationtoolsare
mentscharacterizedbyerraticshiftsandnonlineardependencies, rarelyembeddedintoend-to-endsystems,limitingtheirstrategic
LongShort-TermMemory(LSTM)networksofferamorepowerful impact.
alternative.LSTMmodels,equippedwithmemorycellsandgating Thisresearchaddressedthesegapsbydevelopingaunified,dy-
mechanisms, arecapableoflearningbothshort-andlong-term namic,andinterpretablepipelinethatconnecteddemandforecast-
dependenciesintimeseriesdata[15,16].Asrecentstudiesshow, ing,resourceoptimization,andvisualization,specificallytailored
LSTMhasconsistentlyoutperformedARIMAincapturingdemand totheuniqueoperationaldemandsofprofessionalservicefirms.In
fluctuationsincomplex,high-variancedomainssuchaslogistics doingso,itnotonlyenhancedmodelaccuracyandusabilitybut
andworkforcescheduling[16]. alsoensuredalignmentwithreal-worlddecision-makingneeds.
WhileLSTMoffershighpredictivepower,itoftenlackstrans-
parency. Thistrade-offbetweenaccuracyandinterpretabilityis
partiallyaddressedbyProphet,anopen-sourcemodeldevelopedby
Facebook.Prophetdecomposestimeseriesintotrend,seasonality,
andholidayeffects[17,18],offeringstrongaccuracywithintuitive
parametercontrol. Ithasshownrobustperformanceindiverse
104

Predict,Optimize,Deliver:DemandForecastingandResourceOptimizationforaMarketResearchFirm ICBIM2025,September19–21,2025,Bangkok,Thailand
3 METHODOLOGY RMSE,MAE,andMAPEtoassessforecastaccuracy.RMSEcaptured
largeerrors,MAEreflectedaveragedeviation,andMAPEmeasured
3.1 DataUnderstanding
relativeerror,thoughitwaslessreliableforlow-demandvalues.To
Toaddresstheresearchquestions,bothquantitativeandqualitative
addressconflictingresults,aweightederrorscorewascomputed
datawerecollected.Historicalactivitiesfromthecompany’stime- as(0.35×MAE)+(0.35×RMSE)+(0.30×MAPE).Theoverall
trackingsystemservedastheprimarydataset,complementedby
scorealsoincorporatedinterpretabilityandtrainingspeed(0.25
operationalinsightsfromtheteam’smanager.Thedatasetspans
each)toreflectpracticaldeployment. Simplerandfastermodels
January2,2018toDecember24,2024andincludessixkeyattributes.
receivedlower(better)scores,whilecomplexorsloweroneslike
Thepredictivephaseusesthefirstfour: 1.) Date(DD/MM/YYYY),
LSTMscoredhigher.Thisensuredaconsistentandfaircomparison
2.)Billable(binary:1forclient-related,revenue-generatingtasks;0
acrossaccuracy,usability,andefficiency.
forinternalactivities),3.)Duration(decimal)(tasklength,capped
at24hours),and4.)Client(binary:1or2).Theprescriptivemodel 3.2.4 Prescriptive Phase. The model was translated as a Mixed-
adds5.)NumberofResources(sixanalystsexcludingQA)and6.) IntegerLinearProgramming(MILP)problem,designedtooptimize
WorkingHoursLimit(8hours/day,extendableto10). theallocationofemployeeswhilemeetingdailydemandrequire-
ments.Itaccountedthefollowingvariablesandparametersshown
3.2 DataAnalysis inTable1.xi ,Ci , trepresentedhoursavailabilityofeachemployee,
whichcouldbeallocatedforagivenclientanddaydependingon
3.2.1 Descriptive/DiagnosticsPhase. Thisphaseinvolvedfourkey
needs. 𝐻𝐶 𝑖 𝑡 representedthedemandnodes,ortheservicelevel
activities. First,summarystatistics(mean,min,max,percentiles,
requirementsofeachclientforagivenday.Aconceptofbacklog
standarddeviation)weregeneratedtocomparedemandvariability
betweenthetwoclients. Second,timeseriesdecompositionusing
wasintroducedthroughthe𝐸𝑖 𝑡−1variable,whichwasthediffer-
enceofhourssupplied,andhoursneededfromthepreviousday.
seasonal_decomposefromstatsmodelswasappliedtoextracttrend
Hoursrequiredbyeachclientandbackloghoursweresubjectto
andseasonalitycomponents.Third,theAugmentedDickey-Fuller
non-negativityconstraints, enforcedthroughwithin=NonNega-
(ADF)testassessedstationarity;ap-value≤0.05indicatessuitabil-
tiveRealsinthepythoncode.Inaddition,overtimeandemployee
ityforARIMAmodeling.Lastly,autocorrelationanalysisusingACF
andPACFplotsprovidedinsightintolagdependencies,guiding
availabilityattributeswererepresentedbyoi,tandyi,t,respectively.
All these were configured to the model via Var() function with
selectionofARandMAtermsinARIMA.
iterationforeachemployee,client,anddays.
3.2.2 PredictivePhase. Thepredictivephasewasimplementedin Theobjectivefunctionaimedtominimizetheexcessresources
GoogleColabusingPython. Keyattributeswereselected, with intermsofhoursavailability,minimizingoperationalcostsand
thedatasetfilteredtobillableentriesandaggregateddaily.Toen- improvingutilizationratewhilesatisfyingdemandrequirementsof
surecontinuity,thetimeserieswasresampledtodailyfrequency eachclient.Thisformulationbalancedresourceutilizationensuring
(freq=’D’)andmissingvalueswereaddressedvialinearinterpo- dailyneedswerecoveredbytheteam.Duetohighconfidentiality,
lation. Thecleaneddatasetwasthensplitinto60:40,70:30,and itwasmodelledthatregularcostwas$5perhour,overtimecostwas
80:20train-testratios.Modeltuningfollowedtoidentifyoptimal $10perhour,andpenaltycostwas$20perhour.Mathematically,
parametersforeachforecastingapproach. itwasexpressedwiththefollowingformulainequation1.
AR F IM ou A r ,f f r o o r m ec t a h s e ti s n ta g ts m mo o d d e e l l s s .ts w a. e a r r e im i a m .m p o le d m el e l n ib te ra d ry u ,w sin as g tu P n y e t d h v o i n a . (cid:205) +𝐶 𝑖 𝑜 ∈ 𝑣 { 𝑒 𝐸 𝑟 1 𝑡 , 𝑖 𝐸 𝑚 2, 𝑒 𝐸3 (cid:0)𝑂 ,𝐸 𝑖 4 , , 𝑡 𝑆 (cid:1) 1, + 𝑆2 𝐶 }, 𝑝 𝑡 𝑒 𝐶 𝑛 𝑟 𝑎 𝑒 𝑙𝑡 𝑔 𝑦 𝑢𝑙 ( 𝑎 𝐸 𝑟 1 ( 𝑡 𝑥 𝑖 + 𝐶 𝐸 1 𝑡 2𝑡 + ) 𝑥 𝑖 𝐶 2 ,𝑡) (1)
gridsearchacrosscombinationsof(p,d,q)parameters,represent-
ingautoregressivelags,differencingforstationarity,andmoving Asshowninequations2to4,thismodelaccountedthreecon-
averageterms, respectively. Holt-WintersExponentialSmooth- straints:(1)Thefirstonewasthedemandsatisfactionconstraint,
ing,viaExponentialSmoothingfromstatsmodels.tsa.holtwinters, followedby(2)workinghourslimit,and(3)employeeavailability
wasconfiguredwithvariouscombinationsoftrendandseasonality constraints. Thefirstconstraintrepresentedthebillablehoursthat
types(additiveormultiplicative),alongwithanoptionaldamped needtobematchedbyemployees.Next,themodelputrestriction
trendcomponenttomodeldecayingtrends[34,35].Prophet,im- onthemaximumhoursofworktoensureemployeewell-being.
portedfromtheprophetlibrary,requiredreformattingthedataset Thethirdconstraintwasdefinedinthey(i,t)expression,ensuring
into‘ds’(date)and‘y’(target). Keyparametersincludedchange- noworkwasassignedtoanemployeeiftheywereoutofoffice.
point_prior_scalefortrendflexibilityandseasonality_prior_scale Thisresultedto0capacityifthevaluewas1.
for capturing recurring patterns, with higher values allowing (cid:213)
greateradaptability[36]. LSTM,adeeplearningmodelbuiltus- 𝑖∈{𝐸1,𝐸2,𝑆1,𝑆2} 𝑥 𝑖 𝐶 1 𝑡 =𝐻𝐶 1 𝑡+𝐸1𝑡−1 (2)
ingTensorFlow,involveddatasequencingfollowedbyatwo-layer (cid:213)
LSTMarchitecturewithreturn_sequences,adropoutlayertomiti- 𝑖∈{𝐸3,𝐸4,𝑆1,𝑆2} 𝑥 𝑖 𝐶 2 𝑡 =𝐻𝐶 2 𝑡+𝐸2𝑡−1 (3)
gateoverfitting,andadenseoutputlayer.Themodelwascompiled 𝑥 𝑖 𝐶 1 ,𝑡+𝑥 𝑖 𝐶 2 ,𝑡 ≤ (cid:0) 8+𝑜 𝑖,𝑡 (cid:1)∗(cid:0) 1− 𝑦 𝑖,𝑡 (cid:1) (4)
usingtheAdamoptimizerandmeansquarederrorlosstoimprove
Afterformulatingtheobjective,keyvariables,andoperationalcon-
trainingaccuracy[37].
straints,themodelproceededtoexecutionbycallingthesolver
3.2.3 ModelEvaluation. Modelswerefirsttunedusingoptimal packageinPyomo. ThestudyutilizedtheCPLEXsolver,imple-
parametersidentifiedthroughmultipletrain-testsplitvalidations. mentedinthecodeassolver=SolverFactory(’cplex_direct’).Unlike
Finalevaluationwasthenconductedona30-dayholdoutsetusing traditionalfile-basedapproaches,whereusersmustwriteorread
105

ICBIM2025,September19–21,2025,Bangkok,Thailand Ma.TheresaMarianoandRichardMonreal
Table1:OptimizationVariablesandParameters
Variable Definition Thresholds
xi ,C1 , t Hourssuppliedbyemployeeiforclient1ondayt 0≤xi ,C1 , t≤8+𝑜 𝑖,𝑡
xi ,C2 , t Hourssuppliedbyemployeeiforclient2ondayt 0≤xi ,C1 , t≤8+𝑜 𝑖,𝑡
𝐻𝐶 1 𝑡 Forecastedhoursrequiredbyclient1ondayt Non-negativerealnumbers
𝐻𝐶 2 𝑡 Forecastedhoursrequiredbyclient2ondayt Non-negativerealnumbers
𝐸1𝑡−1 Unmethoursneededbyclient1fromthepreviousday(backlogs) Non-negativerealnumbers
𝐸2𝑡−1 Unmethoursneededbyclient2fromthepreviousday(backlogs) Non-negativerealnumbers
oi,t Overtimehours 0≤oi,t ≤2
yi,t Indicatorwhetheranemployeeisonleave(1)ornot(0) Binary(0,1)
C𝑟𝑒𝑔𝑢𝑙𝑎𝑟 Costofregularworkinghours $5/hour(hypothetical)
C𝑜𝑣𝑒𝑟𝑡𝑖𝑚𝑒 Costofovertimehours $10/hour(hypothetical)
C𝑝𝑒𝑛𝑎𝑙𝑡𝑦 Penaltycostofunmetdemand/backlogs $20/hour(hypothetical)
datafiles[30],suchasinMATLABorLingo,thisplug-inallowed theeffectivenessoftheproposedsystemwashighlydependenton
seamlessinteractionwithIBM’sCPLEXsolverthroughPythonbind- consistentandaccurateupdatingoftime-trackingdata.
ings[29]. Beyondefficiency,thischoicewasdrivenbyitsseamless
integration and compatibility with the Python-based workflow, 4 RESULTSANDDISCUSSION
ensuringastreamlinedoptimizationprocess.
Thissectionpresentedthefindingsofthetimeseriesanalysisto
3.3 DataVisualization developademandforecastingandresourceallocationmodelfor
a market research firm. The results were organized to address
Customvisualizationsweredevelopedtoenhanceinterpretability
thethreemainresearchquestions:forecastingaccuracy,optimal
andsupportdecision-making. ASankeydiagramwasemployedto
workforcedistribution,andeffectivevisualization.
depicttheflowofbillablehoursfromclientstoemployees,effec-
tivelyillustratingworkloaddistribution. Weeklybarcharts,color-
4.1 DiagnosticPhase
codedbyclient,wereusedtopresenttrendsandforecasteddemand,
whilekeysummarymetricsprovidedanoverviewoftotalweekly ThediagnosticresultsinTable2effectivelymirroredtheopera-
requirements. Thesevisualcomponentsenabledstakeholdersto tionalcharacteristicsofeachclient.Forinstance,theupwardtrend
quicklygraspdemanddynamicsandinformedresourceplanning. inClient1’sdatawasaclearindicationofexpandedsyndicated
researchscopeandconsistentrepeatcontracts. Conversely,the
3.4 EthicalConsiderations volatiletrendobservedforClient2suggestedthevariednature
Thisstudyutilizedactualcompanyoperationsdata,requiringstrict oftheirprojects,whichincludedperiodicbrandreports,ad-hoc
diligenceinresponsibledatahandling. Dataprivacyandconfi- customresearchdemand, orstudiesinnewmarketdomainsor
dentialitywereobservedbyanonymizingtheclientsbeingcatered industries.
inthestudy. Nopersonalidentifiableinformationwascollected
throughoutthecourseofthestudytoadheretodatagovernance 4.2 PredictivePhase
protocolsofthecompany.Theoperationsmanagerwasinformed
Thestudyexaminedfourmodelsandweretestedusingtwoeval-
ontheextentofdatausagetoanswerthestudy’sobjectives. As
uation techniques: 1. multiple data splits for forecast stability
partofdataintegrityandtransparencyprocess,thedataweresolely
checking,and2. holdoutevaluationformodelselection. Thefirst
usedforacademicpurposesonly.Anyprocessinganddatamanip-
approachcheckedifmodelsgeneralizedwellwithvaryingamount
ulationsperformedweredocumentedinthemethodologysection
ofhistoricaldatausedintraining,whereasthesecondonesimu-
ofthestudy.
latedifmodelperformedwellinproductionsetting,wherefuture
valuesweretotallyunknown.
3.5 Limitations
Thisstudyadoptedaquantitativeapproach,whichpresentedcer- 4.2.1 Hyperparametertuningusingmultipledatasplits. Multiple
tainlimitations.First,theanalysiswasrestrictedtooutput-based train-testsplitswereusedtoevaluatemodelrobustnessandopti-
variables,suchasbillablehours,andwasconfinedtogroup-level mizehyperparameters,asshowninFigures1,2,3and4.ForARIMA
assessments;input-levelfactorslikeindividualanalystskill,which andHolt-Winters,largertrainingsizesconsistentlyimprovedMAE
couldenhancethemodel,wereunavailable.Second,theforecasting andRMSE,particularlyforClient1,thoughMAPEremainedvolatile
modelutilizedinternalhistoricaldataanddidnotincorporateexter- forClient2duetovariableprojecttypes.Prophetshowedsensitiv-
naleconomicindicatorsfromtheoutsourcingcountry,whichmay itytochangepointpriorscale,withbetterfitathigherflexibility
influencedemandvariability.Third,cautionwaswarrantedwhen butincreasedrelativeerroratlowersplits,especiallyforClient
usingthetoolforlong-rangeforecasting, asitdidnotconsider 2. LSTMmaintainedstableperformanceacrossallsplits,showing
rarebuthigh-impactevents(e.g.,theCOVID-19pandemic). Lastly, lesssensitivitytotrainingsizebutstrongabsoluteaccuracy.These
106

Predict,Optimize,Deliver:DemandForecastingandResourceOptimizationforaMarketResearchFirm ICBIM2025,September19–21,2025,Bangkok,Thailand
Table2:DiagnosticResults
Aspect Client1 Client2
TrendComponent Moderatelyincreasingtrend Moderatelyincreasingtrend
SeasonalComponent Weak Weak
ResidualComponent Random Random
ACFBehavior Slowlydecays,suggestingMAcomponent Slowlydecays,suggestingMAcomponent
PACFBehavior Significantlagat1and2,suggestingAR Significantlagat1and2,suggestingAR
component component
Stationarity Stationaryseries Stationaryseries
ModelType Additive Additive
Figure1:ARIMAModelPerformanceMetricsAcrossSettingsandTrainingSplits.ForClient1,increasingtrainingsizeimproved
modelaccuracy. Client2showedstrongerabsoluteperformance(lowerMAE,RMSE),buthigherMAPE,indicatinglarger
relativeerrorsensitivity.
resultsunderscoredtheimportanceofsplit-basedvalidationforse- 4.3 PrescriptivePhase
lectingoptimalconfigurationstailoredtodatavolumeanddemand ForecastedservicedemandwasoperationalizedusingaPyomo-
volatility. basedoptimizationmodel,testedacrossthreescenarios:baseline
forecasts, positive RMSE-adjusted forecasts (to simulate under-
forecasting),andnegativeRMSE-adjustedforecasts(tosimulate
4.2.2 HoldoutEvaluation. A30-dayholdoutevaluationconfirmed
over-forecasting).Themodelstrictlyrespectedcapacityconstraints,
thattheAdditiveProphetmodeloutperformedallothers,yielding
ensuringnoemployeeexceededthe10-hourdailycapandaligned
thelowestweightederrorforClient1(13.038)andshowingstrong
resourceallocationswithforecasteddemandacrossalldates,achiev-
resultsforClient2(27.786),asshowninTable3.Prophet’sstrength
ingnear-zerogaps.AsreflectedinFigure5,exclusivityruleswere
inhandlingtrendshiftsandevent-triggeredvariationsmadeitmore
enforced,assigningfixedanalyststoeachclientwhilesharedre-
adaptivetobothstableandvolatiledemandpatterns,outperform-
sources(S1,S2)flexiblyabsorbedloadvariations.Utilizationanaly-
ingARIMAandHolt-Winters,particularlyundernoisyconditions.
sisconfirmedefficientdeployment,thoughslightoverutilization
AlthoughLSTMshowedcompetitiveaccuracy,itshighercomplex-
(e.g., 106%forS2), showninTable5, inhigh-demandscenarios
ityanddatarequirementsreduceditspracticalviability. When
flaggedareasformanagerialattention.
interpretabilityandspeedwerefactoredin,Prophetachievedthe
CostanalysisinFigure6revealedthatsmalldiscrepanciesinshort-
lowestoverallscore(10.456),showninTable4,validatingitssuit-
termforecastscouldcompoundintosignificantcostgapsovertime,
abilityforoperationalforecastinginresource-constrainedservice
reinforcingthevalueofdynamic,short-horizonplanning.Weekly
environments.
107

ICBIM2025,September19–21,2025,Bangkok,Thailand Ma.TheresaMarianoandRichardMonreal
Figure2: Holt-Winter’sModelPerformanceMetricsAcrossSettingsandTrainingSplits. ForClient1,themodelachieved
lowesterrorsathighertrainingsizes. Incontrast,Client2displayedmorevolatileresultswithhighMAPEvalues,especially
underadditivetrend-seasonalitysettings,indicatingsensitivitytoseasonalityassumptionsandlowerrobustnesscomparedto
othermodels.
Figure3:ProphetModelPerformanceMetricsAcrossSettingsandTrainingSplits.Resultsshowedvariabilityacrosssettings,
particularlyforClient2inlowertrainsplits,indicatingmodelsensitivitytoparametertuning.
orbi-weeklyuseofthetoolwasfoundoptimal,asitallowedfor insightsforbalancingservicelevels,workforcecapacity,andlabor
cost-effectiveandresponsivestaffingalignedwithshiftingdemand. costsinvolatileserviceenvironments.
Thisprescriptiveframeworknotonlyoptimizedresourceuseun-
derrealisticoperationalconstraintsbutalsodeliveredactionable
108

Predict,Optimize,Deliver:DemandForecastingandResourceOptimizationforaMarketResearchFirm ICBIM2025,September19–21,2025,Bangkok,Thailand
Figure4:LSTMModelPerformanceMetricsAcrossSettingsandTrainingSplits.Resultsshowedstableperformanceacrossall
splitsandhyperparameters,withClient1showingslightlyhigheraccuracy.
Table3:SummaryofWeightedErrorMetrics
| Model |     | Client | MAE(0.35) | RMSE(0.35) | MAPE(0.30) | WeightedError |
| ----- | --- | ------ | --------- | ---------- | ---------- | ------------- |
Metrics
| ARIMA(2,0,1)              |     | 1   | 5.970 | 7.528 | 54.799  | 21.164 |
| ------------------------- | --- | --- | ----- | ----- | ------- | ------ |
| Holt-Winter(None,None)    |     | 1   | 5.182 | 7.076 | 46.644  | 18.284 |
| AdditiveProphet(cps=0.1)  |     | 1   | 4.748 | 6.639 | 30.175  | 13.038 |
| LSTM(lookback=7,units=32) |     | 1   | 4.755 | 6.639 | 42.386  | 16.703 |
| ARIMA(0,0,0)              |     | 2   | 4.253 | 4.785 | 71.669  | 24.664 |
| Holt-Winter(None,Add)     |     | 2   | 3.335 | 4.535 | 102.363 | 33.463 |
| AdditiveProphet(cps=0.5)  |     | 2   | 3.317 | 4.057 | 84.017  | 27.786 |
| LSTM(lookback=7,units=32) |     | 2   | 3.170 | 4.036 | 84.369  | 27.833 |
Table4:OverallModelSelection
Model AverageError Interpretability Speed(0.25) WeightedScore Rank
|             | (0.50) | (0.25) |     |       |        |     |
| ----------- | ------ | ------ | --- | ----- | ------ | --- |
| ARIMA       | 22.914 | 0.250  |     | 0.250 | 11.582 | 2   |
| Holt-Winter | 25.874 | 0.250  |     | 0.250 | 13.062 | 4   |
| Prophet     | 20.412 | 0.500  |     | 0.500 | 10.456 | 1   |
| LSTM        | 22.268 | 1.000  |     | 1.000 | 11.634 | 3   |
4.4 VisualizationPhase utilization,andfreecapacity,helpingidentifystaffingimbalances.
Forecasteddemandandoptimizedresourceallocationswerevisual- KPIcardsmonitoredtotaldemand,assignedhours,unmetdemand,
izedthroughaninteractivePowerBIdashboard,enablingreal-time overtimecost,andservicefulfillment,providingactionableindi-
operationalinsightsasshowninFigure7.Keyslicersallowedman- catorsforperformanceandrisk. Together,thesetoolsfacilitated
dynamic,data-drivenworkforceplanningalignedwithfluctuating
agerstofilterbyclient,staff,scenario,anddaterange,supporting
servicerequirements.
| agiledecision-makingunderuncertainty. |     | Visualelementssuchas |     |     |     |     |
| ------------------------------------- | --- | -------------------- | --- | --- | --- | --- |
Sankeydiagramsandbarchartshighlightedworkloaddistribution,
109

ICBIM2025,September19–21,2025,Bangkok,Thailand Ma.TheresaMarianoandRichardMonreal
Table5:OptimizedAverageResourceUtilization
|     | Employees | Baseline | Adjusted(-) | Adjusted(+) |
| --- | --------- | -------- | ----------- | ----------- |
|     | E1        | 89%      | 59%         | 97%         |
|     | E2        | 55%      | 4%          | 96%         |
|     | E3        | 100%     | 74%         | 75%         |
|     | E4        | 25%      | 0%          | 100%        |
|     | S1        | 88%      | 72%         | 42%         |
|     | S2        | 71%      | 28%         | 106%        |
Figure5:ResourceDistributionbyForecastScenario
Figure6:CumulativeAllocationCostbyForecastScenario
| 5 CONCLUSIONANDRECOMMENDATION |     | 5.2 | Recommendation |     |
| ----------------------------- | --- | --- | -------------- | --- |
5.1 Conclusion Giventhecriticalroleoftrainingsizeinforecastingaccuracy,this
studyrecommendedestablishingarobustdatawarehousingframe-
TheProphetmodelwasseenasthemosteffectiveapproach,balanc-
worktoensuretheavailability,continuity,andtemporalintegrity
ingaccuracyandoperationalusability,particularlyinshort-term
ofhistoricaldata,particularlyduringsystemtransitions.Forfuture
| planningcontexts. | Itsperformanceimprovedwithlarger, | regu- |     |     |
| ----------------- | --------------------------------- | ----- | --- | --- |
research,researchersmayincorporateadaptivelearningmecha-
larlyupdateddatasets,enablingdynamic,data-drivendecisions.
nismsandreal-timeanalysistosupportcontinuousimprovement
Incorporatingpredictionintervalsintotheoptimizationphaseen-
ofbothforecastingandoptimizationprocessesindynamicservice
hancedallocationprecisionbyaccountingfordemanduncertainty.
environments.Furthermore,expandingthemodeltoincludeinput-
Optimizationoutputsrespectedkeyconstraintssuchasworking
basedvariables(e.g.,skilllevels,projectcomplexity)andintegrating
hours,employeeavailability,andresourceassignments(dedicated
externaleconomicindicatorscouldfurtherenhancepredictiveac-
| vs. shared). | IntegratedwithinaninteractivePowerBIdashboard, |     |     |     |
| ------------ | ---------------------------------------------- | --- | --- | --- |
curacy.
thecombinedforecasting-optimizationsystemprovidedactionable
insightsthroughvisualtoolslikeSankeydiagramsandKPIpanels,
supportingagileresponsesinvolatileserviceenvironments.
110

Predict,Optimize,Deliver:DemandForecastingandResourceOptimizationforaMarketResearchFirm ICBIM2025,September19–21,2025,Bangkok,Thailand
Figure7:ResourceMappingandUtilizationDashboard
Acknowledgments https://doi.org/10.51244/IJRSI.2023.10724
[4] Gartner.(n.d.).NetSuiteplanningandbudgetingalternatives&competitors.
Theauthorwouldliketoextendsinceregratitudetothecompany
GartnerPeerInsights.Retrievedfromhttps://www.gartner.com/reviews/market/
forgrantingaccesstooperationaldataandvaluabledomainin- financial-planning-software/vendor/oracle/product/netsuite-planning-and-
sights,whichwereinstrumentalinthesuccessfulcompletionof budgeting/alternatives
[5] AltexSoft.(2022,March1).Demandforecastingmethods:Usingmachinelearning
thisstudy.Theauthoralsoacknowledgedthevaluableinputand toseethefutureofsales.AltexSoft.Retrievedfromhttps://www.altexsoft.com/
encouragementoftheprojectpanelmembers,Dr. ArdvinKester blog/demand-forecasting-methods-using-machine-learning/
[6] BusinessMoney.(2022,July25).Demandforecasting: Whathappenswhen
Ong, Dr. John Xavier Chavez, and Dr. Eric Blancaflor, whose
itfails.BusinessMoney.Retrievedfromhttps://www.business-money.com/
feedbackhelpedrefinetheanalyticalframeworkandensuredthe announcements/demand-forecasting-what-happens-when-it-fails/
study’spracticalrelevance.Deepestappreciationwaslikewiseex- [7] Sutanto, E. M. (2000). Forecasting: The key to successful human resource
management.JurnalManajemen&Kewirausahaan,2(1),1–8.Retrievedfrom
tendedtoDr. RichardN.Monreal,CapstoneProjectAdviser,for
https://www.researchgate.net/publication/50434617
hismentorshipandcriticalguidanceateverystageofthisresearch. [8] Jose,J.(2022).Introductiontotimeseriesanalysisanditsapplications.Christ
University.Retrievedfromhttps://www.researchgate.net/publication/362389180_
INTRODUCTION_TO_TIME_SERIES_ANALYSIS_AND_ITS_APPLICATIONS
References
[9] Ghosh,S.(2020).ForecastingofdemandusingARIMAmodel.AmericanJournal
[1] Ugboko,L.N.,&Ehugbo,I.(2021).Effectofresourceutilizationtechniqueson ofAppliedMathematicsandComputing,1(2),13–18.https://ajamc.smartsociety.
competitiveadvantageofselectedfirmsinNigeriantelecommunicationsindustry. org/wp-content/uploads/2020/09/paper4.pdf
InternationalJournalofAcademicMultidisciplinaryResearch(IJAMR),5(11), [10] Girotra,R.(2022).Workforceplanningusingtimeseries(Master’sdissertation).
106-117.Retrievedfromhttps://www.researchgate.net/publication/359504374_ TrinityCollegeDublin.https://publications.scss.tcd.ie/theses/diss/2022/TCD-
Effect_of_Resource_Utilization_Techniques_on_Competitive_Advantage_of_ SCSS-DISSERTATION-2022-070.pdf
Selected_Firms_in_Nigerian_Telecommunications_Industry [11] Devi,K.L.,&Valli,S.(2023).Timeseries-basedworkloadpredictionusingthe
[2] Sharma,S.,&Singh,S.(2022).RLSmodelforforecastingresourcefulfilmentin statisticalhybridmodelforthecloudenvironment.Computing,105(2),353–374.
ITandconsultingindustry.Metamorphosis:AJournalofManagementResearch, https://doi.org/10.1007/s00607-022-01129-7
21(1),1–10.https://doi.org/10.1177/09726225221075086 [12] Kumar,L.,Khedlekar,S.,&Sharma,R.(2024).AcomparativeassessmentofHolt-
[3] Boadi-Sarpong,A.B.,Agyei,P.A.,Mensah,E.,&Boateng,P.A.(2023).Resource Wintersexponentialsmoothingandautoregressiveintegratedmovingaverage
allocationstrategiesformaintainingcompetitivenessandachievinginnovation forinventoryoptimizationinsupplychains.SupplyChainAnalytics,8,Article
success.InternationalJournalofResearchandScientificInnovation(IJRSI),10(7). 100084.https://doi.org/10.1016/j.sca.2024.100084
111

ICBIM2025,September19–21,2025,Bangkok,Thailand Ma.TheresaMarianoandRichardMonreal
[13] Wang,C.-C.,Chien,C.-H.,&Trappey,A.J.C.(2021).Ontheapplicationof [26] Mohammadi, S., PourKarimi, L., &Reinert, K.(2023).Amathematicalpro-
ARIMAandLSTMtopredictorderdemandbasedonshortleadtimeandon-time grammingapproachforresourceallocationofdataanalysisworkflowson
deliveryrequirements.Processes,9(7),1157.https://doi.org/10.3390/pr9071157 heterogeneousclusters.TheJournalofSupercomputing,79(17),19019–19048.
[14] Swapnarekha,H.,Behera,H.S.,Nayak,J.,Naik,B.,&Kumar,P.S.(2021).Multi- https://doi.org/10.1007/s11227-023-05325-w
plicativeHolt’sWintermodelfortrendanalysisandforecastingofCOVID-19 [27] Fang,Z.,Wu,Q.,&Guan,D.(2022).Towardsoptimalresourcesallocationin
spreadinIndia.SNComputerScience,2,Article416.https://doi.org/10.1007/ cloudmanufacturing:Newtaskdecompositionstrategyandservicecomposition
s42979-021-00808-0 model.SecurityandCommunicationNetworks,2022,Article5019584.https:
[15] Yadav, M., Patil, R., Bhirud, B., &Chavle, P.L.(2023).LSTMmodel-based //doi.org/10.1155/2022/5019584
demand forecasting in supply chain using efficient optimizer. Retrieved [28] Kia,R.,Shahnazari-Shahrezaei,P.,&Zabihi,S.(2016).Solvingamulti-objective
fromhttps://www.researchgate.net/publication/373555323_LSTM_Model_based_ mathematicalmodelforamulti-skilledprojectschedulingproblembyCPLEX
Demand_Forecasting_in_Supply_Chain_using_Efficient_Optimizer solver.Proceedingsofthe2016IEEEInternationalConferenceonIndustrial
[16] Terrada,L.,ElKhaili,M.,&Ouajji,H.(2022).Demandforecastingmodelusing EngineeringandEngineeringManagement(IEEM),1220–1224.https://doi.org/
deeplearningmethodsforsupplychainmanagement4.0.InternationalJournal 10.1109/IEEM.2016.7798072
ofAdvancedComputerScienceandApplications,13(5),704–711.https://doi.org/ [29] PyomoDevelopers.(n.d.).PyomoCPLEXdirectsolvermodule.PyomoDocu-
10.14569/IJACSA.2022.0130581 mentation.RetrievedMarch182025,fromhttps://pyomo.readthedocs.io/en/6.8.
[17] FacebookResearch.(2017,February).Prophet:Forecastingatscale.Facebook 1/_modules/pyomo/solvers/plugins/solvers/cplex_direct.html
Research.Retrievedfromhttps://research.facebook.com/blog/2017/2/prophet- [30] OR Stack Exchange. (n.d.). Difference between CPLEX direct and CPLEX
forecasting-at-scale/ in Pyomo SolverFactory. OR Stack Exchange. Retrieved March 18 2025,
[18] Sharma,K.,Bhalla,R.,&Ganesan,G.(2022).TimeseriesforecastingusingFB- from https://or.stackexchange.com/questions/9412/difference-between-cplex-
Prophet.InR.Zwiggelaar,G.Ganesan,Q.S.Cheng,K.-L.Du,&S.R.Satti(Eds.), direct-and-cplex-in-pyomo-solverfactory
ProceedingsoftheAlgorithms,ComputingandMathematicsConference2022 [31] Lavanya,A.,Sindhuja,S.,Gaurav,L.,&Ali,W.(2023).Acomprehensivereview
(ACM2022)(pp.59–64).CEURWorkshopProceedings,Vol-3445.https://ceur- ofdatavisualizationtools:Features,strengths,andweaknesses.International
ws.org/Vol-3445/PAPER_07.pdf JournalofComputerEngineeringinResearchTrends,10(1),10–20.https://doi.
[19] Negre,P.,Alonso,R.S.,Prieto,J.,García,Ó.,&de-la-Fuente-Valentín,L.(2024). org/10.22362/ijcert/2023/v10/i01/v10i0102
PredictionoffootweardemandusingProphetandSARIMA.ExpertSystemswith [32] Tirupati,K.K.,Joshi,A.,Singh,S.P.,Chhapola,A.,Jain,S.,&Gupta,A.(2024).
Applications,234,124512.https://reunir.unir.net/handle/123456789/17524 LeveragingPowerBIforenhanceddatavisualizationandbusinessintelligence.
[20] Long,C.,Yu,C.,&Li,T.(2022).Prophet-basedmediumandlong-termelectricity UniversalResearchReports,10(2),676–711.https://doi.org/10.36676/urr.v10.i2.
loadforecastingresearch.JournalofPhysics:ConferenceSeries,2356,012002. 1375
https://doi.org/10.1088/1742-6596/2356/1/012002 [33] Microsoft.(n.d.).PowerBIvisualizationtypesforreportsandQ&A.Microsoft
[21] Jierula,A.,Wang,S.,OH,T.-M.,&Wang,P.(2021).Studyonaccuracymetrics Learn.RetrievedMarch2025,fromhttps://learn.microsoft.com/en-us/power-
forevaluatingthepredictionsofdamagelocationsindeeppilesusingartificial bi/visuals/power-bi-visualization-types-for-reports-and-q-and-a
neuralnetworkswithacousticemissiondata.AppliedSciences,11(5),2314.https: [34] Pleños,M.C.F.(2022).TimeseriesforecastingusingHolt-Wintersexponential
//doi.org/10.3390/app11052314 smoothing:Applicationtoabacafiberdata.ProblemsofWorldAgriculture,22(2),
[22] Seder,A., &Alnasser,R.(2023).WorkforcemanagementforSalikcallcen- 17–29.https://doi.org/10.22630/PRS.2022.22.2.6
ter(Master’sthesis).RochesterInstituteofTechnology.Retrievedfromhttps: [35] StatsModels.(n.d.).statsmodels.tsa.holtwinters.ExponentialSmoothing.StatsMod-
//scholarworks.rit.edu/cgi/viewcontent.cgi?article$=$12635&context$=$theses elsDocumentation.RetrievedFebruary26,2025,fromhttps://www.statsmodels.
[23] Wang,Y.,Zhang,H.,Yuan,C.,Li,X.,&Jiang,Z.(2024).Anetworkflowapproach org/dev/generated/statsmodels.tsa.holtwinters.ExponentialSmoothing.html
tooptimalschedulinginsupplychainlogistics.arXiv.https://doi.org/10.48550/ [36] Facebook.(n.d.).TrendchangepointsinProphet.FacebookProphetDocumenta-
arXiv.2411.17544 tion.RetrievedFebruary26,2025,fromhttps://facebook.github.io/prophet/docs/
[24] Wang,C.C.(2022).Networkflowoptimizationusingreinforcementlearning trend_changepoints.html
(Doctoraldissertation).AalborgUniversity.https://vbn.aau.dk/ws/portalfiles/ [37] Arya,M.,&Sastry,G.H.(2023).EffectiveLSTMneuralnetworkwithAdam
portal/549541544/PHD_CCW.pdf optimizerforimprovingfrostpredictioninagriculturedatastream.InA.E.
[25] Ercsey,Z.,&Kovács,Z.(2023).Multicommoditynetworkflowmodelofahuman Hassanien,M.A.Elhoseny,&A.T.Azar(Eds.),Modellinganddevelopmentof
resourceallocationproblemconsideringtimeperiods.CentralEuropeanJournal intelligentsystems(pp.3–17).Springer.https://doi.org/10.1007/978-3-031-27034-
ofOperationsResearch.https://doi.org/10.1007/s10100-023-00868-y 5_1
112