JournalofAppliedBigDataAnalytics,Decision-Making,andPredictiveModellingSystems
Data Science and Business Analytics Approaches to Financial Wellbe-
ing: Modeling Consumer Habits and Identifying At-Risk Individuals in
Financial Services
JeshwanthReddyMachireddy1
1IndependentResearcher
Abstract
Banksandotherfinancialinstitutionsareincreasinglyusingdatascienceandbusinessanalyticstosupportconsumerfinancialwellness
throughbehaviormodelingandtargetingpotentialfinancialdistress.Inparticular,thisstudydiscussesthreesignificantareas:consumer
financialbehaviormodelingfromtransactionhistoryanddigitalfootprints,applicationofanalyticstopopulationsegmentationandexposure
tofinance,andtheoperationalandethicalfoundationforapplyingthesesolutionsresponsibly.Thisarticlegivesathoroughexplanationof
howconsumerexpenditurebehaviorandhigh-volumetransactionaldatacanbeusedtoestablishfinancialhabits.Itdescribesmethodsof
consumerpopulationsegmentationandfinancialvulnerabilityassessmentwithadvancedmachinelearningmodelsandreal-timedatastreams
toidentifyearlywarningsignsofpersonalfinancialrisk.Oneofthekeythemesisriskmanagementbyconsumerswithanemphasisonusing
explainableartificialintelligence(AI)tomakeriskassessmenttransparentandequitable.Discussioncombinespsychologicalandcontextual
informationwithhistoricalfinancialinformationtocreatestrongerconsumerprofiles,acknowledgingthatattitudes,lifeevents,andpersonal
circumstanceshaveaneffectonfinancialhealth.Ethicalaspectsareexploredindetail,includingethicaldeploymentmodelsforsuchtechnolo-
giesthatprotectprivacy,avoidbias,andcomplywithinternationalregulatorystandards.Approachestodeployingtheapplicationofreal-time
analyticsandexplainablemodelsarealsocovered,withfocusonintegrationandscalabilityacrossmultiplemarkets.Throughintegrationof
criticalalgorithmicmethods,conceptualmodels,andinternationalcasestudies,thepaperexplainshowdata-basedintelligencecanimproves
financialservicesanddeliverconsumerfinancialstabilityandresilience.
Keywords: Analytics,ConsumerBehavior,EthicalAI,FinancialVulnerability,MachineLearning,RiskManagement,TransactionData
POLARPUBLICATIONSc2023.ThisdocumentislicensedundertheCreativeCommonsAttribution4.0InternationalLicense(CCBY4.0).Underthetermsof
thislicense,youarefreetoshare,copy,distribute,andtransmittheworkinanymediumorformat,andtoadapt,remix,transform,andbuildupontheworkfor
anypurpose,evencommercially,providedthatappropriatecreditisgiventotheoriginalauthor(s),alinktothelicenseisprovided,andanychangesmadeare
indicated.Toviewacopyofthislicense,visithttp://creativecommons.org/licenses/by/4.0/.
1. Introduction scorestoconstructdynamicportraitsoffinancialhealththat
shiftinrealtime.
Financialwell-beingistheabilityofindividualstocomfortably
spendtheirfinancialassets,toberesilienttoeconomicshocks Consumers’financialbehaviorcanbemodeledusingdata
andbeconfidentintheirfinancialfuture[1]. Intheworld,the analytics,enablingdangersignsthattheindividualislikely
majorityofpeopleareweigheddownbyfinancialhardshipdue tobeatrisktobedetectedearlyon. Forexample,asudden
toover-indebtedness,incomevolatility,andlackofsufficient dropinincomedeposits,risingrelianceonshort-termcredit,
savings. Theseproblemsimpactnotjustindividualconsumers orevenfrequentbillsbeingoverlookedcanallpointtowards
butalsoraiseissuesforpolicymakersandfinancialinstitutions, a customer facing financial difficulties. By using machine
sincegeneralizedfinancialriskcanleadtohigherdefaultrates, learningalgorithmsandstatisticaltechniques,thesesignals
reducedconsumerconfidence,andeconomicinstabilitymore canbeautomaticallyextractedfromhugecustomerdatabases,
broadly. Undertheseconditions,fosteringconsumerfinancial allowinginstitutionstoidentifyat-riskindividualsevenbe-
well-beinghasbecomeakeysocialpolicyandfinancialservices fore a loan default or an account overdraft actually occurs.
goal, and it has sparked interest in innovative methods to Mostimportantly,suchmodelscanalsoincorporatenotjust
monitorandsupportthefinancialwell-beingofconsumers. overtfinancialindicatorsbutlessoverttrends—likegambling
transactionsorcashloans—rising,thatcansignalmoreovert
Datascienceandbusinessanalyticsinnovationoffersro-
financialdistress[2]. Real-timeanalyticscapabilitiescanman-
bustabilitiesforaddressingthischallengebyharnessingthe
agereal-timestreamingoftransactionalinformationsothat
massiveamountsofdatageneratedwithinconsumers’finan-
the changes in behavior are identified as soon as they hap-
cialactivity. Millionsofpayments—creditcardtransactions
pen,andtheninterventionsorassistancecanbescheduled
andutilitybills,andmobilemoneytransactions—dailyleave
accordingly.
adeepdigitalfootprintofconsumerbehavior. Thesetrans-
action records, carefully examined, can reveal expenditure, Atthesametime,businessanalyticsmethodsareapplied
saving,andborrowinghabitstypicalofanindividual’sfinan- todivideconsumerpopulationsbyfinancialbehaviorandvul-
cial conduct and potential risks. Traditional credit scoring nerability. Instead of handling customers as a bulk quan-
systemshavetypicallyutilizedarestrictedsetofvariables(i.e., tity differentiated only by credit history or income, banks
paymenthistoryanddebtoutstanding)toquantifyrisk,but andfintechcompaniesaredividingcustomersintomorenu-
increasingfinancialdigitizationnowenablesamuchmore ancedcategories—financiallyhealthy,coping,orvulnerable
detailedapproach. Byviewingdetailedhistoriesoftransac- segments—byclusteringalgorithmsandmulti-dimensional
tionsandotherbehavioraldata,bankscanseepaststaticcredit riskindices. Itallowsfortargetedstrategies: offeringprecise
CreativeCommonsCCBY4.0 1–18

DataScienceandBusinessAnalyticsApproachestoFinancialWellbeing:ModelingConsumerHabitsandIdentifyingAt-RiskIndividualsinFinancialServices
|     |                   | .          |     |     |                  | ¢   |     |                   | (cid:138) |     |
| --- | ----------------- | ---------- | --- | --- | ---------------- | --- | --- | ----------------- | --------- | --- |
|     | Over-Indebtedness |            |     |     | IncomeVolatility |     |     | LackofSavings     |           |     |
|     |                   | •Debttraps |     |     | •economyrisks    |     |     | •Noemergencyfunds |           |     |
•Paydayloanreliance •Unpredictablecashflow •Livingpaycheck-to-paycheck
|     | •Interestcompounding |           |     |                          | •Jobinsecurity   |     |     | •Retirementgaps     |           |     |
| --- | -------------------- | --------- | --- | ------------------------ | ---------------- | --- | --- | ------------------- | --------- | --- |
|     |                      | (cid:254) |     |                          |                  | Ł   |     |                     | (cid:130) |     |
|     | RisingDefaultRates   |           |     | ErodedConsumerConfidence |                  |     |     | EconomicInstability |           |     |
|     | •Loandelinquencies   |           |     |                          | •Bankingdistrust |     |     | •Marketvolatility   |           |     |
|     |                      |           |     |                          | •Reducedspending |     |     | •ReducedGDPgrowth   |           |     |
•Creditcardcharge-offs
|     | •Repossessions       |     |     |     | •Hoardingbehaviors      |     |     | •Systemicriskcascades |     |     |
| --- | -------------------- | --- | --- | --- | ----------------------- | --- | --- | --------------------- | --- | --- |
|     |                      | ı   |     |     |                         | 6   |     |                       |     |     |
|     | StaticCreditModels   |     |     |     | OpaqueRiskSignals       |     |     |                       |     |     |
|     | •Outdatedriskfactors |     |     |     | •Missedgamblingpatterns |     |     |                       |     |     |
•Undetectedcashadvances
•Limitedbehavioraldata
|     | •Infrequentupdates |     |     |     | •Hiddendebtcycles |     |     |     |     |     |
| --- | ------------------ | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- |
Figure1.ChallengesinFinancialWell-being:SystemicRisksandAnalyticalLimitations
Segment IncomePattern DebtBehavior SavingsBehavior CreditUsage
| FinanciallyHealthy |     |     | Stable    |     |     | Low-risk      |     | Regular    |     | Moderate |
| ------------------ | --- | --- | --------- | --- | --- | ------------- | --- | ---------- | --- | -------- |
| Coping             |     |     | Irregular |     |     | Moderate-risk |     | Occasional |     | High     |
| Vulnerable         |     |     | Volatile  |     |     | High-risk     |     | Minimal    |     | VeryHigh |
Table1.Segmentprofilesbasedonbehavioralfinancialtraits.
| Feature               |     |     | DataType    |     | UsedInModeling |     | IndicatesRisk |            | ChangeOverTime |           |
| --------------------- | --- | --- | ----------- | --- | -------------- | --- | ------------- | ---------- | -------------- | --------- |
| IncomeDeposits        |     |     | Numeric     |     |                | Yes |               | Yes        |                | Yes       |
| MissedPayments        |     |     | Categorical |     |                | Yes |               | Yes        |                | Yes       |
| Short-termLoans       |     |     | Binary      |     |                | Yes |               | Yes        |                | Sometimes |
| TransactionCategories |     |     | Categorical |     |                | Yes |               | Indirectly |                | Yes       |
| OverdraftEvents       |     |     | Count       |     |                | Yes |               | Yes        |                | Yes       |
Table2.Behavioralfeaturesusedinfinancialriskmodeling.
ModelType Transparency Interpretability Real-timeCapability BiasRisk
| LogisticRegression |     |     | High    |     |     | High    |     | Moderate |     | Low    |
| ------------------ | --- | --- | ------- | --- | --- | ------- | --- | -------- | --- | ------ |
| RandomForest       |     |     | Medium  |     |     | Medium  |     | High     |     | Medium |
| GradientBoosting   |     |     | Low     |     |     | Low     |     | High     |     | High   |
| NeuralNetworks     |     |     | VeryLow |     |     | VeryLow |     | High     |     | High   |
Table3.Comparisonofcommonmachinelearningmodelsforfinancialbehavioranalysis.
financial advice or hardship assistance programs to identi- regulatorsalikeneedtobeabletolookintowhyanindividual
fiedvulnerableindividuals,anddesigningpreventativefinan- washighlightedashighriskorgroupedintoaparticularclass.
cialwell-beingprogramsforthosewhoarevulnerable-to-be. Inaddition,thefinancialsectorhastoimplementthesedata-
Throughthetrackingoffinancialwell-beingandvulnerability drivenintelligenceintoitsworkingsinanappropriatemanner
attheindividualandsegmentlevels,institutionscanbetter suchthatthefrontlineemployeesanddecision-makersuse
targetresourcesandmeasurethesuccessofinterventionsover themforthebenefitofconsumersratherthanexploitingtheir
time. situation. Governancecontrolsandcross-functionalcollab-
oration(datascientists,riskmanagers,complianceofficers,
Theuseofsophisticatedalgorithmsandbigpersonaldata
inthisareaposesseriousethicalandpracticalconcerns. Per- consumeradvocates)needtoleveragethesetoolsethicallyand
sonalfinancialdataishighlysensitive,anditsanalysisneedsto establishconfidence.
beprivacy-friendlyanddataprotectionlaw-compliantacross Thispaperexaminestheaboveissuesinmoredepth,describ-
borders. Besides,thereisalsoariskthatautomatedriskpro- inghowanalyticsanddatasciencepracticescanbeharnessed
filing willin some way discriminate against certaingroups todrivefinancialwell-beinginaconsumer-centricmanner.
orreinforcepre-existingbiases,forexamplewheretradition- Section2beginswithconsiderationsofmodelingfinancialbe-
allydisadvantagedgroupshavethinneronlinefootprintsor haviorfromtransactionaldata,expenditurehabits,andother
unrepresentativefinancialpatterns. Aconcern,therefore,to digitalfootprints,withaspecialemphasisonreal-timeanalyt-
highlightexplainableAIandopenmodelling: customersand icsandleadingalgorithmicapproaches[3].Section3thencon-
2

DataScienceandBusinessAnalyticsApproachestoFinancialWellbeing:ModelingConsumerHabitsandIdentifyingAt-RiskIndividualsinFinancialServices
˘HiddenMarkovModelsdetectspendingsequencepatterns
|                    | Œ   |     |     |     |                      | y   |     |                   | ¤   |     |     |
| ------------------ | --- | --- | --- | --- | -------------------- | --- | --- | ----------------- | --- | --- | --- |
| TransactionSources |     |     |     |     | FeatureExtraction    |     |     | PredictiveModels  |     |     |     |
| •Cardpurchases     |     |     |     |     | •Incomevolatility    |     |     | •Gradientboosting |     |     |     |
| •Billpayments      |     |     |     |     | •Discretionaryspend% |     |     | •Sequenceanalysis |     |     |     |
| •Paycheckdeposits  |     |     |     |     | •Liquiditytrends     |     |     | •Autoencoders     |     |     |     |
(cid:130)
|     |     | EconomicContext |     |     | RiskInsights |     |     |     |     |     |     |
| --- | --- | --------------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
•Defaultprobability
•Inflationrates
|     |     | •Employmenttrends |     |     | •Financialstresspaths |     |     |     |     |     |     |
| --- | --- | ----------------- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- |
•Cohortoutliers
•Regionalprices
(cid:181)Peergroupanalysisflagsbehavioraldeviations
Figure2.TransactionalDataModelingPipelineFromRawDatatoPrediction
sidersincludingpsychologicalandenvironmentalvariablesin markersoffinancialhealth: e.g.,highandsteadysavingsrate
financialprofiles,realizingthatfactorslikemoneyattitudes couldindicategoodfinancialdisciplineandtoughnesswhile
ofindividuals,stresslevels,andlifeexperiencescancreatean regularoverdraftchargesorpaydayloansusecouldsignify
additionaldepthofknowledgeregardingconsumerbehavior ongoingfinancialdifficulty.
andrisks. Section4turnstowardsbusinessanalyticsincon- Toportraysuchhabitsasquantitativemodels,analystsand
sumersegmentationanddeterminationoftheirvulnerabilities
|     |     |     |     |     |     | researchers | would typically | translate |     | raw transaction | histo- |
| --- | --- | --- | --- | --- | --- | ----------- | --------------- | --------- | --- | --------------- | ------ |
anddiscusseshowpopulationgroupscouldbesegmentedand riesintomeaningfulfeatures. Examplesoffeaturesinclude
howthefinancialwell-beingmetricscouldbeemployedto
themonthlyexpense-to-incomeratio,theannualincomevari-
identifyriskypersons. Section5focusesonexplainableAIand ance(volatility),discretionarycomparedtonecessaryexpenses
transparency,outliningapproachestomakingriskassessment asapercentageofspending,ortheaverageliquiditybalance
| modelsinterpretableandfair. |     |     | Section6discussestheethical |     |     |                            |     |     |                          |     |     |
| --------------------------- | --- | --- | --------------------------- | --- | --- | -------------------------- | --- | --- | ------------------------ | --- | --- |
|                             |     |     |                             |     |     | maintainedintheaccount[4]. |     |     | Machinelearningmodelscan |     |     |
andoperationalframeworksneededfortheeffectivedeploy- be trained on these features to classify or predict financial
mentofthesetechnologies,includingprivacy,biasreduction,
|     |     |     |     |     |     | outcomes. | Forexample,aclassificationmodelmightinform |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | ------------------------------------------ | --- | --- | --- | --- |
compliancewithregulation,andthetechnicalimplementation uswhichcustomersaremostlikelytobeunabletopaytheir
challengesinfinancialinstitutions. Section7presentsaglobal creditcardbillinthecomingmonthsbasedonrecenttrends
perspectiveandexaminesimplementationstrategies,compar-
|     |     |     |     |     |     | in their | spending and | balance | history. | A regression | model |
| --- | --- | --- | --- | --- | --- | -------- | ------------ | ------- | -------- | ------------ | ----- |
ingcontrastinglyhowthesestrategiesarebeingadoptedin mightattempttoforecastanintegerfinancialhealthscoreor
differentmarketsandinstitutionalsettings. Finally,Section theprobabilityofdefaultonaloan. Inordertoconstructsuch
8distillsmainfindingsandpresentsdirectionsforfuturere- models,complexalgorithmslikegradientboostingmachines
searchintoconsumer-drivenriskmanagementinfinancial orneuralnetworksmightspotnon-linearinteractionbetween
services.
variables,whereaslesstransparentmodelslikedecisiontrees
orlogisticregressionmightcallattentiontothespecifictrans-
|             |     |           |          |         |        | action patterns | most predictive |     | of risk | (e.g., an increase | in  |
| ----------- | --- | --------- | -------- | ------- | ------ | --------------- | --------------- | --- | ------- | ------------------ | --- |
| 2. Modeling |     | Financial | Behavior | through | Trans- |                 |                 |     |         |                    |     |
debt-to-incomeproportionorrisingutilizationofcreditlines
| action | Data | and | Digital Footprints |     |     |     |     |     |     |     |     |
| ------ | ---- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
tocoverminimalexpenses).
2.1. TransactionalDataandSpendingPatterns Sequenceanalysis,inwhichthetime-orderedsequenceof
Oneoftheprincipalsourcesofdataaboutconsumerfinancial paymentsisanalyzedasastudyobjectandnotmerelyasag-
behavioristhecompleterecordofpaymentsthatfinancialin- gregatenumbers,isanotheressentialanalyticalapproachto
stitutionsaccumulatewhentheydobusinesswithconsumers. modelingmoneybehavior. MethodssuchasHiddenMarkov
Everydebitcardorcreditcardpurchase,everypay-your-bill- Models or recurrent neural networks have been studied in
from-your-checking-accountpayment,andeverydepositof anattempttomodeltheincomeandexpendituresequence
apaycheckaddstoagrowingledgerofincomeandexpenses todeterminetransitionsfromoneleveloffinancialposition
for each consumer. By aligning and analyzing these trans- toanotherforaspecificindividual. Forinstance,anincome
actionhistories,datascientistscancreatearichprofileofa interruptionpatternfollowedbyariseincreditcardusageand
consumer’sspendinghabits.Ofinterestarepatternsofhowan subsequentlydelinquencycanberecognizedasapathtofi-
individualallocatesspendingbycategory(e.g.,housing,food, nancialcrisisbyasequencemodel. Byrecognizingsuchpaths
transportation,entertainment),incomefrequencyandsources, beforetheygettoofaralong,abankcaninterveneorassistat
billpaymenttiming,andfrequencyofincidencesuchasover- ajuncturewhenthecustomer’ssituationremainsreversible.
draftorlatefees. Fromthesehabits,itispossibletodeduce Evenmoresimplerule-basedsequenceanalysiscanbeeffec-
3

DataScienceandBusinessAnalyticsApproachestoFinancialWellbeing:ModelingConsumerHabitsandIdentifyingAt-RiskIndividualsinFinancialServices
FeatureType Examples DerivedMetrics BehavioralInsight UseCase
IncomeActivity Salarydeposits,gigpayments Volatility,frequency Stability,employmentregularity Riskprediction
SpendingPatterns Category-levelpurchases Essential/discretionaryratio Financialdiscipline Wellnesssegmentation
AccountEvents Overdrafts,fees Monthlycount Financialstrain Earlywarning
CreditBehavior Loanusage,repayments Utilizationtrends Relianceondebt Defaultmodeling
SavingsTrends Transferstosavings Consistency,growthrate Resilience Healthscoring
Table4.Commontransactionalfeaturesusedinbehavioralfinancialmodels.
ModelingApproach TemporalAwareness Interpretability IdealUseCase Complexity
LogisticRegression Low High Simpleclassification Low
DecisionTrees Low Medium Rule-basedflagging Low
GradientBoosting Medium Low Riskscoring,ranking High
RecurrentNeuralNets High VeryLow Sequenceprediction VeryHigh
Autoencoders Medium Low Anomalydetection High
Table5.Comparativeoverviewofmodelingtechniquesforfinancialbehavior.
DigitalFootprintType DataSource SignalType PotentialIndicator AppliedBy
MobileUsage Call/SMSlogs,airtime Regularity,top-ups Paymentdiscipline Fintechlenders
OnlineSubscriptions Streaming,SaaS Paymentcontinuity Budgetstrain Budgetingapps
E-commerceHistory Purchases Baskettrends Lifestyle,volatility Alt-creditscoring
UtilityPayments Electricity,water Timeliness Reliability Alt-creditmodels
Social/DigitalID Email,phonerecords Longevity,frequency Stability Identityverification
Table6.Typesofdigitalfootprintsandtheirfinancialmodelingrelevance.
tive:forexample,realizingthatanotherwiseregularpaycheck intheiraccountbeginstospendtheirbalancedowntonearly
hasnotarrivedonitsusualday,orthatapreviouslyregular zeroeverymonth, oriftheysuddenlymaxoutcreditcards
monthlyspendingpatternhasbeguntobecomeirregular,can wheretheyoncehadlowbalances,thesearechangesthatcan
giveimmediatewarningsigns. be quantitatively flagged by anomaly detection algorithms.
Unsupervisedlearningtechniques,suchasautoencodersand
clustering,canbeemployedtodeterminetheseoutlierswith-
Algorithm1:TransactionalDataFeatureExtraction
outthenecessityofpre-existingrisklabels;thesystemsimply
andModeling
learnswhat"normal"behaviorisforacohortorfortheindi-
Input: Rawtransactionrecords𝑇 ={𝑡 1 ,𝑡 2 ,…,𝑡 𝑛 } vidualandthencanalertwhenaprecipitousdeviationoccurs.
Output: Predictedfinancialriskscore𝑅
[5]
Step1: Preprocessing; Itisalsobeneficialtointroduceexternaleconomiccontext
Grouptransactionsbyuserandtimeperiod(e.g., intotransactiondatamodeling. Householdconsumptionand
monthly); savingpatternsarenotisolated; theyrespondtomacroeco-
Normalizeandcategorizetransactiontypes(income, nomicslikeinflation,interestratemovements,oremployment
bills,discretionary,etc.); trends. Forinstance,duringaperiodofrisinginflation,evena
Step2: FeatureExtraction; conservativehouseholdcanshowincreasingcreditconsump-
Computefeatures𝐹suchas:; tionordecreasingsavingsaslivingcostsrise. Astrongmodel
-Expense-to-incomeratio; offinancialbehaviormaybeabletocapturesuchcontextby
-Incomevolatility; adding local unemployment rates, regional price levels, or
-Discretionaryspendingpercentage; othereconomicmeasuresinadditiontoindividualtransaction
-Liquiditytrends; characteristics. Suchintegrationmayenhancetheaccuracy
ofthemodel inseparatingoutindividual-specificfinancial
Step3: ModelTrainingandPrediction; issuesfromthosemoregenerallydeterminedbythestateof
Loadpre-trainedmodelℳ(e.g.,gradientboosting,
theeconomy. Italsoplacestheanalysisonaworldwidelevel,
HMM);
recognizingthatconsumerfinancialhealthisanoutcomeof
Predictriskscore𝑅 =ℳ(𝐹);
individualinclinationsandoutsideinfluences.
return𝑅;
2.2. DigitalFootprintsandReal-TimeBehavioralAnalytics
Inadditiontopatternanalysisattheindividuallevel,trans- Together with the traditional bank operations, individuals
actionaldatacanbeprocessedinpeergrouporcohortenviron- leave behind innumerable traces in the digital world that
mentstodetectoutliers. Acustomerwhosespendingpattern would reflect their own financial practices or status. Elec-
abruptlydeviatesgreatlyfromhisownhistoryaverageorfrom tronicfootprintsrepresenttracesleftoverbypeople’sbehavior
typicalbehaviorofsimilarcustomersmightbeworthconsid- intheelectronicanddigitalworld,yettheyextendfarbeyond
ering. Forexample,ifacustomerwhousuallykeepsacushion officialeconomicrecords.Exampleincludese-businesshistory
4

DataScienceandBusinessAnalyticsApproachestoFinancialWellbeing:ModelingConsumerHabitsandIdentifyingAt-RiskIndividualsinFinancialServices
¯2/3offinancialappsnowuseopenbankingAPIs
|        | I        |        | ”       |      | (cid:212) |
| ------ | -------- | ------ | ------- | ---- | --------- |
| Mobile | Payments | Social | Signals | Open | Banking   |
•In-apppurchases •Employmentmentions •Multi-accountaggregation
|                |           | • Financial | hashtags  | • API  | streaming       |
| -------------- | --------- | ----------- | --------- | ------ | --------------- |
| • Peer-to-peer | transfers |             |           |        |                 |
| • Airtime      | usage     | • Network   | stability | • Cash | flow monitoring |
T
|     |     | Real-Time | Engine |     |     |
| --- | --- | --------- | ------ | --- | --- |
•Kafkastreams
|     |     | • Online | learning |     |     |
| --- | --- | -------- | -------- | --- | --- |
´<500mslatencyfortransactionprocessing
|     |     | • Anomaly | detection |     |     |
| --- | --- | --------- | --------- | --- | --- |
I
|     |     | Dynamic | Interventions |     |     |
| --- | --- | ------- | ------------- | --- | --- |
•Balancealerts
|     |     | • Budget   | adjustments |     |     |
| --- | --- | ---------- | ----------- | --- | --- |
|     |     | • Hardship | offers      |     |     |
Figure3.Real-TimeFinancialFootprintAnalysisSystemArchitecture
ofbehavior,mobiletelephonepayments,subscriptiononline, regularbehaviorwithmonetaryimplicationscanserveasthe
evensocialmediabehavior. Allpotentiallycanbeattached foundationforafinancialhealthmodel.
to financial standing or practice, theoretically. Alternative Astheopenbankingprogramsinvariouspartsoftheworld
datahavebeenutilizedinsomerecentfinancialservicesin
continuetoincrease,consumersarenowcapableofallowing
| anefforttoimproveriskmodels: | agoodoldexampleofthis |     |     |     |     |
| ---------------------------- | --------------------- | --- | --- | --- | --- |
third-partyfinancialappsdirectaccesstotheirbankaccount
isusingmobilephonedataandutilitybillrecordsinabidto details. This has opened up a new generation of real-time
measurecreditworthinessinindividualswhohavenoormini-
personalfinancialmanagementservicesandriskengines. A
malhistoryofformalcreditreporting. Aconsumer’srecord consumercanaggregatemultiplecreditcardsandbankac-
ofon-timepaymentofhisorherphonebillsorfrequencyof countsintoonedashboardapp,whichwillthenusestreaming
mobileairtimepurchases,say,mightbeemployedasaproxy
transactionupdatestotracktheirreal-timecashflow. Banks
for reliability and financial responsibility in the absence of themselvesincreasinglyareconstructingreal-timedatastream-
conventionalcreditdata.
ingintoriskinfrastructure.Insteadofwaitingforamonth-end
reporttoevaluateacustomer’sfinancialstatus,today’ssystems
Fintechsandalternativelenderswereattheforefrontofuti-
caningesttransactionsinrealtimeviaAPIsandupdatethe
lizingthesewebtracestocreatealternativecreditscoresorfi-
nancialwellnessmeasures[6]. Theymightstudyacustomer’s customer’sriskprofileinrealtime. Real-timeanalyticsplat-
forms(usuallybuiltonstreamingdatatechnologiesandevent-
purchasehistoryforonlineshoppingtoinfertheirconsump-
tionandcost-of-livingbehavior, orusesocialnetworkdata processingframeworks)cancomputerunningmetrics—such
ascurrentmonth-to-datespendvs. revenue,ordetectionofa
toverifyidentityandmakeestimatesofstability(e.g.,stable
significantunexpectedexpense—andimmediatelycompare
emailandphonenumberuseovertimemightindicatelower
defaultriskthanfrequentcontactinformationchanges). Even theseagainstthresholdsorpatternsofconcern.
somelendershaveexperimentedwithtappingpsychometric Theadvantageofreal-timebehavioralanalyticsisthepace
datacollectedthroughInternetquestionnaires—essentially atwhichissuescanbeidentifiedandaddressed. Forexam-
quantifyingsuchhabitsasconscientiousnessortendencies ple,ifanormallyregularsalarypaymentfailstoturnupon
to take risks—to predict payment of loans, utilizing the re- schedule,areal-timesystemcaninstantlyflagthisandpoten-
sponsesaspartoftheapplicant’sInternetrecord. Whilethese tiallysendanautomaticalerttothecustomerwithanoffer
innovationsstretchthedefinitionsoffinancialinformation, ofassistanceorasuggestionthattheychecktheirpayroll. If
theydrivehomeanexcellentpoint: intheory,anythingthatis there’sasuddenburstofhigh-valuepurchasesthatareoutof
5

DataScienceandBusinessAnalyticsApproachestoFinancialWellbeing:ModelingConsumerHabitsandIdentifyingAt-RiskIndividualsinFinancialServices
linewiththecustomer’susualpattern,thebankmaycallto metrictestsandquestionnaires.Somelenders,especiallyinde-
confirmthechargesaredeliberateandtorevisethebudgetpro- velopingeconomies,haveemployedstructuredquestionnaires
jectionforthatcustomer[7].Essentially,theperson’sfinancial toevaluatepersonalitycharacteristicslikeconscientiousness,
makeupisadynamicmodelthatisrepeatedlyrefiguredbased honesty,optimism,andcognitiveabilityaspartofthecredit
oneachnewpieceofinformation. Thisisacontrasttoearlier applicationprocess.Assumptionswouldbethatsuchtraitsare
paradigmsunderwhichriskassessmentwasaperiodicordis- somehowlinkedtomoneybehaviour;apersonwhoisverycon-
connectedexercise(e.g.,creditcheckonanapplicationfora scientiousmight,say,belikelytopaybackbillsontimeeven
loan)andwouldrapidlybecomestalebetweenexaminations. whenhard-up.Resultsfromthesetests–essentiallyquantative
Fromamodelingperspective,integratingreal-timestreams scoresthatreflectpsychologicalportraits–canbepluggedinto
ofinformationsuggestsalgorithmsthatincrementallyupdate. creditscoresorriskprofilesforthefinanciallyexcludedwho
Online learning platforms or frequent batch retraining are haveno’proper’creditrecords. Otherthanlending,thesame
usedsuchthatthemodelremainsup-to-dateasemergingpat- testscanalsogaugeacustomer’sfinancialconfidenceorstress.
ternsoccur. High-endeventprocessingsystemscanbeusedto Somebankshaveshortquizzesregardingcustomers’moods
combinesetsofdifferentdatasignals;theycan,forinstance, ortestingcustomers’interestrateknowledgeintheirmobile
linkafallinaccountbalancewithanewseventlikeanatural bankingapplications. Thesequizinformationcanshow,for
disasterinthelocalityofthecustomer,addingdepthofun- example, a customer is experiencing money stress or even
derstandingintowhetherthefinancialchangeistemporary overestimates his or her financial knowledge [8]. Merging
orreflectspersonalchallenges. Real-timemodelsalsomostly thesesignalswithtransaction-basedmodelscanbeusedto
utilize thresholds or rules that can trigger immediate reac- distinguishbetweentwocustomerswhoonpaperareequally
tions. Thesemightbesimplealerts(e.g.,ifaspecificcategory welloffbutpsychologicallyarequitedifferent–onecouldbe
ofexpenseexceedsaparticularthreshold),halfwaythrough relaxedandincommand,whereastheotherisstressedand
themonth)ormorecomplextriggerconditionsderivedfrom apttomakesecond-bestdecisionswhenunderpressure.
machinelearningmodeloutputs(e.g.,theleveloffinancial
stresspredictedbythemodelforacustomerexceedsacertain
probabilitycut-off).
Generallyspeaking,data-drivenmodelingoffinancialbe-
haviorexploitsboththerichnessoftransactionalrecordsand
the breadth of modern digital traces. By using advanced
analyticsonthesedata,financialinstitutionscancreatedy-
namic,real-timeportraitsofconsumerfinancialhealth. These
modelsformthefoundationforassessingrisk,enablingcus-
tomersegmentationbyfinancialhealth,andinformingany Contextualfactorsarealsoavitallevelofinformation.These
tailored interventions or products. The second step in the arepersonalcircumstancesandexternalconditionsthatsur-
analysisistoaddsuchdata-drivenmodelsmorehumancon- roundanindividual,whichprovidethecontextonwhichfi-
text—psychologicalandsituationalfactorsthatdatamightnot nancialconductwillbeassessed. Someofthemostcrucial
beabletoencompassfully—subjectofthefollowingsection. contextfactorsarelifeevents(i.e.,marrying,divorce,giving
birth to a child, losing an employer, or retirement), family
makeup(e.g.,thenumberofdependentsorone-incomever-
3. Incorporating Psychological and Contextual
sustwo-incomehousehold),communityorgeoeconomicsur-
Factors
roundings(localleveloflivingexpenses,conditionofthelo-
Whiledataontransactionsandbalancesprovidesaquantita- caleconomy,socialsafetynetavailable). Asuddenlifeevent
tivecontextofaconsumer’sfinanciallife,arealfullprofilere- canalterriskprofilesandfinancialneedsacutely: asudden
quiresfleshintheformofpsychologicalandcontextualfactors. healthcrisiscandrainreservesandincreaseshort-runcredit,
Psychologicalfactorsinvolveaperson’smoneymanagement orjoblosswilleasilyreduceincomeandcouldgeneratede-
attitudes,traits,andbehaviors,whichcanhaveasubstantial fault. Ifabankknowsaboutsuchevents–maybeinferred
impactonfinancialoutcomes. Forexample,personaltraits fromdatalikeinsuranceclaims,addressupdates,orevenac-
likeself-control,optimism,risktolerance,andfinancialliter- tualcommunicationwiththecustomer–itcanadjustitsper-
acyhavebeenknowntoimpactpeople’ssavingorspending ceptionofthecustomer’ssituation. Inpractice,banksdonot
behavior. Suchapersonwithhighself-controlandfutureori- alwayspossesscertaininformationaboutlifeevents,butincer-
entationmayalwayssaveandavoidunnecessarydebt,whereas taininstances,theycaninferthem. Aspikeinhealth-related
animpulsivedecisionmakermayhavefluctuatingspending transactionscouldimplyahealthemergency;aseriesofbaby
behaviorthatinducesfinancialstressirrespectiveofincome. purchaseswouldindicatethearrivalofachild;aseverance
Similarly,financialliteracy–awarenessoffinancialideasand packageorunemploymentclaimfilingwouldsuggestlossof
abilitytomanagefinances–isextremelyheterogenousamong employment. Sophisticated analytics are able to flag these
consumersandcanbreakormakewhetheraconsumerac- patterns, effectively setting a flag in the customer’s profile
quirespredatoryloansorpaysexcessivefees. Byquantifying thatextraordinaryconditionsprevail. Contextualinformation
suchpsychologicalfactors,eitherbysurvey,inferredaction, alsoextendtomacro-levelsituations. Ifsomeonewholives
orthird-partyinformation,financialinstitutionscansubstan- inaplacewitheconomichardship(e.g.,aplantshut-downin
tiallyenhancetheexplanatorypoweroftheirmodelsandthe asmalltown),theirotherwiseanomalous-lookingbehavior
salienceoftheirinterventions. (such as tapping into savings) could make sense and has a
Onewayofintegratingpsychologyisbyemployingpsycho- differentmeaningthanifone’sbroaderenvironmentisstable.
6

DataScienceandBusinessAnalyticsApproachestoFinancialWellbeing:ModelingConsumerHabitsandIdentifyingAt-RiskIndividualsinFinancialServices
Multidimensionaldatafusionthroughfederatedlearning
|     | j   |     |     | ¡   |     |     | (cid:130) |
| --- | --- | --- | --- | --- | --- | --- | --------- |
ContextualSignals
| PsychologicalDimensions |     |     | ConsumerProfile |     |     |     |     |
| ----------------------- | --- | --- | --------------- | --- | --- | --- | --- |
•Lifeeventdetection
| •Self-controlmetrics |     |     | TransactionHistory+ |     |     |     |     |
| -------------------- | --- | --- | ------------------- | --- | --- | --- | --- |
•Localeconomicindicators
| •Financialliteracyscores |     |     | PsychologicalTraits+ |             |     |                          |     |
| ------------------------ | --- | --- | -------------------- | ----------- | --- | ------------------------ | --- |
| •Risktolerancelevels     |     |     |                      | LifeContext |     | •Familystructureanalysis |     |
¤
EnhancedRiskModel
|     |     |     | •Psychometricweights |     | ˘XAItechniquesexplainpersonality-weightingfactors |     |     |
| --- | --- | --- | -------------------- | --- | ------------------------------------------------- | --- | --- |
•Context-adjustedscoring
•Dynamicinterventions
Ł
EthicalConsiderations
•Explicitconsentgates
•Privacy-preservingML
•Biasaudits
Figure4.FinancialProfilingwithIntegratingPsychologicalandContextualDimensions
¢ (cid:219)
|     |     | FinancialStatus | +Mutualinfluence |     | MentalWell-being |     |     |
| --- | --- | --------------- | ---------------- | --- | ---------------- | --- | --- |
”Anxietyfeedback
| ”Financialshocks |     | •Accountbalances   |     |     | •Stressbiomarkers |     |     |
| ---------------- | --- | ------------------ | --- | --- | ----------------- | --- | --- |
|                  |     | •Creditutilization |     |     | •Decisionfatigue  |     |     |
|                  |     | •Paymenthistory    |     |     | •Cognitiveload    |     |     |
6Differentialprivacyprotectssensitivepsychologicaldata
(cid:17) `
|     |     | AdaptiveInterventions |     |     | ContextCapture       |     |     |
| --- | --- | --------------------- | --- | --- | -------------------- | --- | --- |
|     |     | •Dynamicbudgeting     |     |     | •Psychometricsurveys |     |     |
|     |     | •Empathy-drivenalerts |     |     | •Transactionpatterns |     |     |
|     |     | •Counselingpathways   |     |     | •Lifeeventdetection  |     |     |
´72%fasterstressdetectionthroughreal-timepatternanalysis
Figure5.Financial-MentalHealthFeedbackSystemwithAdaptiveInterventions
Addinginpsychologicalandsituationalinformationinto
| Algorithm2: | FinancialRiskModelingwithPsycho- |     |     |     |     |     |     |
| ----------- | -------------------------------- | --- | --- | --- | --- | --- | --- |
logicalandContextualInputs financialportraitsmeansonecantailorandhavegreaterem-
|     |     |     |     | pathyforassessingrisk. | Ratherthanseeingacustomerasaset |     |     |
| --- | --- | --- | --- | ---------------------- | ------------------------------- | --- | --- |
Transactiondata𝑇,psychologicaltraits𝑃,
Input:
ofnumbers–income,expenditure,creditscore–theinstitu-
contextindicators𝐶
tioncomestoknowapersonwithsomefinancialperspective
| Output: | Personalizedriskscore𝑅 |     |     |             |                 |           |                     |
| ------- | ---------------------- | --- | --- | ----------- | --------------- | --------- | ------------------- |
|         |                        |     |     | and working | in some context | [9]. That | has a few benefits. |
TransactionalFeatureExtraction;
Step1: First,suchmodelspredictandexplainfinancialdistressmore
Computestandardfinancialfeatures𝐹 from𝑇; accurately. Forexample, incorporatingameasureoffinan-
𝑇
-Incomevolatility,creditusage,liquidityratio,etc.; cialliteracyorconfidencewouldmakeamodelmoreableto
PsychologicalProfiling; predictwhowillstruggletosticktoabudgetorwhowould
Step2:
|     |     |     |     | benefit | from proactive action. | Operationally, | knowing the |
| --- | --- | --- | --- | ------- | ---------------------- | -------------- | ----------- |
Quantifytraits𝑃(viasurveyorinferredbehavior):;
-Self-control,risktolerance,financialliteracy,stress contextcaninformhowtotacklethecustomer. Afinancially
levels;
| Normalizeandscoreintopsychometricvector𝐹 |     |     | ;   |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
𝑃
|     | ContextualSignalIntegration; |     |     | 7   |     |     |     |
| --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
Step3:
| Extractcontextfeatures𝐹 |     | from𝐶:; |     |     |     |     |     |
| ----------------------- | --- | ------- | --- | --- | --- | --- | --- |
𝐶
-Lifeevents,localeconomicdata,household
structure;
Applyweightsortriggersforrecentimpactfulevents;
ModelInference;
Step4:
| Fusefeatures: | 𝐹 =𝐹 ∪𝐹 | ∪𝐹 ; |     |     |     |     |     |
| ------------- | ------- | ---- | --- | --- | --- | --- | --- |
𝑇 𝑃 𝐶
Applymodelℳ(𝐹)trainedwithexplainabilityand
fairnessconstraints;
| Computeriskscore𝑅 | =ℳ(𝐹); |     |     |     |     |     |     |
| ----------------- | ------ | --- | --- | --- | --- | --- | --- |
return𝑅;

DataScienceandBusinessAnalyticsApproachestoFinancialWellbeing:ModelingConsumerHabitsandIdentifyingAt-RiskIndividualsinFinancialServices
PsychologicalTrait MeasurementMethod BehavioralCorrelate RiskIndicator ModelUsage
Self-control Survey,spendingregularity Budgetdiscipline Lowimpulsivedebt Classification
Optimism Psychometrictest Futureplanning Positivesavingsbehavior Engagementtargeting
RiskTolerance Questionnaire,investmentbehavior Willingnesstoborroworinvest Exposuretovolatiledebt Creditmodeling
FinancialLiteracy Quizscores Productselection Susceptibilitytofees Advicepersonalization
Stress/Anxiety Self-assessment,spendinganomalies Financialavoidance Missedpayments,debtcycles Supportflagging
Table7.Psychologicaltraitsrelevanttofinancialbehaviormodeling.
ContextualFactor ExampleSource InferredFrom FinancialImpact ModelingApproach
LifeEvents Claims,HRdata Purchasepatterns,deposits Expensespikes,incomechanges Event-basedflagging
HouseholdStructure Customerprofile Jointaccountusage,transferpatterns Budgetstrain,savingsrate Profilesegmentation
GeographicLocation Address,ZIPcode Regionalstats,appmetadata Cost-of-livingvariation Context-awaremodeling
EmploymentStatus Payrolldeposits Incomeregularity,benefits Volatility,defaultrisk Time-seriesanalysis
MacroeconomicConditions Externaldatabases Regionaleconomicindicators Broadfinancialstress Featureenrichment
Table8.Contextualfactorsandtheirintegrationintofinancialriskmodels.
illiteratecustomercanbeguidedtoagentler,moredidactic trulyatriskanddesigninterventionsthatresonateonahu-
approachwhensellingaproductorrecommendation,whereas manlevel. Thishuman-infusedaugmentationofdata-driven
asavvybuttime-constrainedcustomerwillbekeentoreceive modelsisasteppingstonetothenextlevelofanalysis: using
swift,high-levelresults. Shouldamodelknowthatacustomer theseaugmentedprofilestosystematicallysegmentconsumers
hasrecentlylosthisorherjob,anystrategyofcollectinglate andmeasurefinancialvulnerabilityinacustomerbase.
paymentscanbemadegentlerwithsympathyandaccommo-
dation(perhapsreschedulingthepayments)ratherthanan
4. Consumer Segmentation and Financial Vul-
automatedpenalty.
nerability Assessment
Therearefeedbackloopstobeconsideredaswell. Psycho-
logicalhealthandbehavioraroundmoneyaremutuallyinflu- Notallcustomersarefinanciallychallengedinthesamewayor
encing: becomingover-indebtedmaycausestressandanxiety, tothesameextent. Businessanalyticstechniquesallowfinan-
leadinginturntopoorerdecision-makingoravoidanceofdeal- cialinstitutionstomoveawayfromone-size-fits-allriskratings
ingwithmoney,makingtheissueworse. Thereissomeexper- tomorenuancedsegmentationoftheircustomerbasebyfi-
imentationamongfinancialinstitutionstoincludemeasures nancialhealthandrisk[11]. Thepurposeofthissegmentation
ofmentalwell-beingincustomercaremodels. Forinstance,if istofindcohortsofconsumerswhosharethesamefinancial
data(likeanunexpectedchangeinexpenditurepatternsora characteristicsandrisks,thusenablingeachtobeidentified
survey)showsthatacustomerisexperiencingextremefinan- and treated as such. For instance, one group of customers
cialdifficulties,thebankmayproactivelyreachouttothem might be consistently covering their costs with some spare
withsupportoptions,likecounselingservicesortailoredfinan- money (financially secure), one might be just about scrap-
cialplanningassistance. Inthepersonalfinanceappworld, ingbyeachmonth(financiallystretched),andanothergroup
someappsattempttogaugeusermood(throughchatbotsor mightbeoftenfallingshortandhavingtousecreditormiss
check-ins)tocustomizetheguidance–holdingbacklessifthe payments(financiallyvulnerable). Bydefiningsuchsegments,
userisstressed,orpushingmoreiftheuserisconfident. banksandotherinstitutionscangaugethesizeofeachseg-
Combiningcontextualandpsychologicalfactorswithgood ment,trackchangesovertime,andstructuretheirproductsor
old-fashioneddatahastobedonewithtactandethics. Mea- supportservicestosuittheneedsofeachsegment.
surementofsuchvariablescanentailelicitingtheinputfrom Agoodstartingpointindoingthisistoestablishasetof
thesubjects(e.g.,fillingoutaquestionnaire)orinferencefrom metrics or indices of financial vulnerability. Financial vul-
surrogates,whichcanbenoisyorintrusive[10]. Privacycon- nerabilityiscommonlyasynonymforthevulnerabilityofa
cernsareextremehere: consumerswillnotexpecttheirbank persontoextremefinancialhardship—likeinabilitytomeet
tomonitortheirsocialmediaorlifeeventsunlesstheyhave anunplannedexpense,ahighlikelihoodofdefaultonobliga-
explicitlygiventhatdata. Transparencyandconsentarethus tions,orpersistentinabilitytomaintainminimallivingstan-
criticalwhenextendingdatacollectionintothesedomains. dards. Beinginherentlymulti-dimensional,analystsusually
Technically,mergingtheseinputsmeansmergingqualitative buildacompositescoreorindexthatsumsupvariousindica-
dataandquantitativefinancialdata,whichposesmodeling torsintoonemeasureoffinancialwell-beingorvulnerability.
issues. Socialscienceandmachinelearningcanbeappliedto Thesemetricscouldincludemeasuresofliquidity(suchas
normalizeandquantifytheseinputs–e.g.,takingtheanswers liquidassetsovermonthlyexpenses),leverage(suchasdebt-
onasurveyandconvertingthemintostandardscoresthatcan to-incomeorcreditutilizationratio),stabilityofincome(in-
bemergedwithfinancialstatisticsinamodel. comevarianceinthelastyear),andpreviousfinancialdistress
Ingeneral,theinclusionofpsychologicalandcontextual indicators(numberofdelayedpayments,overdrafts,orloan
datagivesabetterunderstandingofthefinancialpositionof delinquencies). Eachoftheseitemscapturesadifferentaspect
each consumer. It acknowledges that two consumers with ofvulnerability: littlesavingscaptureslittleshockcushion,
similartransactionconductmayhaveextremelydifferentca- highdebt-to-incomeratiocapturessensitivitytoincomefall,
pacitiestowithstandfinancialshocksortoadjusttheirconduct. unstable earnings captures uncertainty, and history of past
Byaddingmindsetsandcircumstancestofinancialwell-being distresseventscapturesatroublerecord. Bybringingthese
models, financial institutions can better determine who is together—sometimesinweightedaveragesormorecomplex
8

DataScienceandBusinessAnalyticsApproachestoFinancialWellbeing:ModelingConsumerHabitsandIdentifyingAt-RiskIndividualsinFinancialServices
InputType Source ProcessingMethod OutputFormat IntegrationStrategy
SurveyResponses In-appquizzes Scoring,normalization Traitindex(0–1) Directmodelfeature
BehavioralProxies Spendingpatterns Rule-basedinference Binary/ordinaltags Modelflag
ExternalEvents NewsAPIs,macrodata Taggingbylocation/time Eventindicators Contextualfilter
UserFeedback Chatbot,check-ins Sentimentanalysis Emotionalstatescore Supportprioritization
LifeSignals Transactionsequences Patternmatching Flaggedeventtype Riskprofileadjustment
Table9.Methodsofincorporatingpsychologicalandcontextualsignalsintomodelingpipelines.
¤3distinctclustersidentifiedviasilhouetteanalysis
| ı                    |     | y                    |     |     |                        | ˘   |     |
| -------------------- | --- | -------------------- | --- | --- | ---------------------- | --- | --- |
| DataFoundation       |     | VulnerabilityMetrics |     |     | SegmentationEngine     |     |     |
| Transactionhistories |     | •Debt-to-incomeratio |     |     | •K-meansclustering     |     |     |
| Creditutilization    |     | •Liquidityindex      |     |     | •XGBoostclassification |     |     |
| Incomevolatility     |     | •Paymentdelinquency  |     |     | •SHAPexplanations      |     |     |
‡
RiskCohorts
SecureŁ
Stretched.
Vulnerable(cid:254)
TargetedActions
•Debtrestructuring
£68%reductionindefaultsthroughproactiveinterventions
•Financialcoaching
•Productrecommendations
Figure6.FinancialVulnerabilitySegmentationPipelineFromRawDatatoAction
(cid:215)Vulnerablesegmentincreasedduringdownturn avulnerablecluster—distinguishedfromanotherclusterof
customerswithstableincome,moderatesavings,andlowdebt,
| {   | £   |     | whoappeartobeingoodfinancialhealth[12]. |     |     | Clusteringcan |     |
| --- | --- | --- | --------------------------------------- | --- | --- | ------------- | --- |
TemporalAnalysis RiskDistribution identifynaturallyoccurringgroupswithoutgiventhresholds,
Monthlyrescoring •Secure:highshare whichisbeneficialinthecontextofsegmentdefinitioninan
Cohortmigration •Stretched:moderateshare
|                                       |     |     | exploratoryfashion. | Ontheotherhand,ifabankhassomecri- |     |     |     |
| ------------------------------------- | --- | --- | ------------------- | --------------------------------- | --- | --- | --- |
| Trenddetection •Vulnerable:lowershare |     |     |                     |                                   |     |     |     |
teriaordefinitionsofvulnerability,thenitcanuserule-based
|     |     |     | segmentationorsupervisedclassification. |     |     | Forinstance,the |     |
| --- | --- | --- | --------------------------------------- | --- | --- | --------------- | --- |
bankcandefinethatanyonewithadebt-to-incomeratioabove
| (cid:152)                         | 8   |     |                     |     |                |             |     |
| --------------------------------- | --- | --- | ------------------- | --- | -------------- | ----------- | --- |
|                                   |     |     | a certainpercentage | and | belowtwomonths | of expenses | in  |
| FeedbackMechanism GovernanceLayer |     |     |                     |     |                |             |     |
•Producteffectiveness •Fairnessaudits savingsisinthe"at-risk"segment. Inasupervisedlearning
| •Policyadjustments •ExplainableAI |     |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- |
environment,thebankcouldberequiredtousehistoricaldata
| •Modelretraining •Regulatoryreporting |     |     |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
labeledwithoutcomes(e.g.,whoultimatelydefaultedorap-
Figure7.DynamicFinancialHealthMonitoringSystemwith pliedforfinancialdifficultyrelief)inordertotrainamodel
whichclassifiesnewcustomersinto"at-risk"and"notat-risk"
EthicalGovernance
|     |     |     | bucketsbasedontheircurrentfinancialstatistics. |     |     | Themodel |     |
| --- | --- | --- | ---------------------------------------------- | --- | --- | -------- | --- |
canpossiblypickupsubtlepatternsoffeaturesthatareindica-
tiveoftroubleonthehorizon—maybepickinguponpatterns
statisticalscoringmodels—institutionscanassigneachcus-
tomerafinancialwellnessorvulnerabilityrating. Lowscore suchas"highincomebutextremelyerratic,alongwithrecent
mightmeanstrongfinancialhealth(lowrisk),whilehighscore spikeinborrowing"whicharule-basedsystemmaynotcatch.
signifiesthatthesubjectisatrisk. Onceriskclassesorsegmentsaredefined,theyareavery
Havingscoresorrawdataofthistypeonhand,segmenta- effectivetoolforbusinessstrategyandcustomerrelationship
tioncannextbeachievedthroughuseofseveraldata-driven management. Attheportfoliolevel,managementcanmonitor
methodologies. Clusteringanalysis,whichisanunsupervised whatproportionofcustomersareineachlevelofvulnerability
learningmethod,isoneofthepopularapproachesused,where andhowtheproportionsshiftwitheconomicconditionsoras
thecustomersarebeingsegmentedbasedonsimilarityamong aresultofinterventions. Forexample,duringarecession,a
financialattributesets. Forexample,aclusteringprocedure bankmightseethesizeofthevulnerablesegmentgrow;this
might identify one cluster of customers with little savings, cancauseittoinvestmoreincustomerassistanceprogramsor
volatileincomes,andheavycredituse—clearlyidentifiableas alteritslossprovisioning. Onthecontrary,oncethebankhas
9

DataScienceandBusinessAnalyticsApproachestoFinancialWellbeing:ModelingConsumerHabitsandIdentifyingAt-RiskIndividualsinFinancialServices
launchedabudgetingapporfinancialcoachingtool,thebank andcomplianceofficialsmustseetheattributesthatmakeup
mayexpectsomeofthoseinthevulnerablesegmenttomigrate eachsegment—"vulnerablecustomerswillhaveX,Y,andZ
toasafersegmentinthefuture,supportingtheeffectiveness characteristics"—sothatthesedefinitionsarelogicalanddon’t
ofthatproject. excludeorpenalizecertaingroupsinerror.
Onanindividualbasis,segmentationallowsforactionto Segmentationisn’taone-offactivitybutaniterativeexer-
bespecificallytargeted. Fiscallytroubledcustomerscanbead- cise. Customerscanmovebetweensegmentsastheirsituation
dressedwithpersonalizedsupport: e.g.,thebankcanactively changes;therefore,thedataandmodelsneedtoberefreshed
offerbudgetadvice,easydebtrestructurings,orwarningsand periodically. Ayoungprofessionalearlyintheircareermight
tools toavoid fees. These strategies notonly assistthe cus- firstbeinavulnerablesegmentduetolowsavingsandnew
tomer but also reduce the bank’s risk and increase loyalty. credit usage, but a few years later, after pay increases and
Meanwhile,customersinastablesegmentmightbeoffered somesavingshavebeenbuiltup,theymightmovetoamore
long-termsavingsorinvestmentproducts,andthoseinthe secure segment. Or, once good sound retiree becomes vul-
middlemightbeencouragedtoimprovesomeaspects(e.g., nerable after expensive medical care that consumed all his
establishinganemergencyfund)[13]. Thisalignswiththe money[14]. Businessanalyticsplatformstypicallyperform
ideaofconsumer-riskmanagement—usinganalyticsnotjust periodicrescoringandsegmentationrefreshes(e.g.,monthly
toprotecttheinstitutionfromrisk,buttohelpmanagethe orquarterly)tocapturesuchchanges. Trendanalysiscanthen
consumer’sownfinancialriskandimprovetheirwell-being. beappliedinsuchtransitions:ifmanycustomersaredropping
intoadvancedriskclasses,itmaysignalimpendingproblems
Algorithm3:ConsumerFinancialVulnerabilitySeg-
(macroeconomicorinstitutional)thathavetobetracked.
mentation
Theapplicationofbusinessanalyticstosegmentcustomers
Input: Consumerfinancialdata𝐷(e.g.,transactions,
basedonfinancialwell-beingandvulnerabilityallowsbanksto
credit,income)
betterunderstandtheheterogeneityoftheircustomerbase. By
Output: Assignedvulnerabilitysegment𝑆
movingbeyondthegenericcreditscoretoanelucidatingun-
Step1: FeatureConstruction; derstandingofthestateoffinancialwell-being,banksareable
Extractvulnerabilityfeatures𝐹suchas:; toidentifywhoandwhatsegmentsofpopulationaremostat
-Debt-to-incomeratio; riskandwhy.Thisopensthedoortotargetedriskmanagement
-Liquidityindex; interventionsandtailoredprogramsforfinancialwell-being.
-Incomevolatility; Theeffectivenessofsuchanalytics-drivenstrategies,however,
-Paymentdelinquencycount; alsohingesonthevalidityofthemodelsthemselvesandtheir
uptakebystakeholders—pointsaddressedbyhighlightingex-
Step2: ScoringorClustering;
plainabilityandethicaldeploymentinsubsequentparts.
if usingsupervisedmethodthen
Applytrainedclassifier𝒞(𝐹)toassignsegment𝑆;
else 5. Explainable AI for Transparent Risk Assess-
Applyunsupervisedclustering(e.g.,K-means)on𝐹
ment
tofindsegments;
Assign𝑆basedonclosestclustercentroid; Asbanksandotherfinancialinstitutionsusemoreadvanced
analyticsandmachinelearningmodelstoassessconsumer
Step3: ActionMapping; risk and well-being, transparency and explainability of the
Basedon𝑆,triggerbusinessactions:; modelsarecritical. ExplainableAI(XAI)referstotechniques
-If𝑆 =Vulnerable: Offerdebtrelief,coaching; andpracticesthatmakeanalgorithm’sdecision-makinginter-
-If𝑆 =Stretched: Suggestbudgetingtools; pretablebyhumans. Inconsumerfinancialriskassessment,
-If𝑆 =Secure: Recommendsavings/investment explainabilityservesseveralcriticalpurposes. Ithelpsfulfill
products; regulatorydemands(mostjurisdictionsrequirelenderstopro-
videreasonsforadversedecisionslikeloandenials),itallows
return𝑆;
modeldevelopersandriskmanagerstoverifythatthemodel
Financialvulnerabilitysegmentationalsohasaregulatory isusingappropriatefactors(andnot,e.g.,proxyingforpro-
and ethical dimension. In some countries, regulators have tectedcharacteristicsinadiscriminatoryway),andithelps
actuallyrequestedbankstoidentifyandsupportvulnerable buildconfidenceamongconsumersandotherstakeholdersby
customers. Forexample,guidelinescansuggestthatbanks explaininghowtheirdatagetstranslatedintoriskscoresor
shouldbeabletomarkcustomerswhomightbeatriskifin- segmentassignments.
terestratesriseorifgovernmentbenefitsarecut, andtreat Onepathtoexplainabilityistouseinherentlyinterpretable
themfairly. Segmentationmodelsandindexesprovideasta- models. Decisiontrees–essentiallyalistofweightedfactors
ble way to meet such needs by alerting for such customers orif-thenrulesthatresultinascore–andscorecardmodels
inadvance. Withthatsaid,cautionmustbeexercisedwith dominatedcreditriskfordecades. Thesemodelsarerelatively
howsuchsegmentsareutilized. Tobe"vulnerable"withinan easytointerpret;onecantellaloanofficeroracustomer,for
internalsystemshouldnotresultinnegativereactionslike instance,thatthescorewasloweredbecausecreditcardbal-
denialofservice,butrathertriggersomeformofsafeguardor anceswerehighorjobtenurewasshort,andthismakesintu-
assistancemechanism. Furthermore,thesegmentationcrite- itivesense[15]. Whilemachinelearninghasintroducedmore
riausedshouldbetransparenttothepointthattheycanbe complexmodels(e.g.,ensemblemethodsorneuralnetworks)
explainedandjustifiedtointernalstakeholdersandregulators. capableofcapturingpatternsthatmightnotbecapturedby
Thisiswhereexplainableanalyticscomesin: businessleaders traditionalmodels,mostorganizationssacrificeaccuracyfor
10

DataScienceandBusinessAnalyticsApproachestoFinancialWellbeing:ModelingConsumerHabitsandIdentifyingAt-RiskIndividualsinFinancialServices
SegmentLabel IncomePattern SpendingBehavior SavingsProfile DebtCharacteristics
FinanciallySecure Steady,predictable Controlled,balanced Regularcontributions Lowutilization
FinanciallyStretched Moderate,fluctuating Highessentialshare Irregularorminimal Risingtrend
FinanciallyVulnerable Unstable,volatile Unpredictable,reactive Noreserve Heavyrelianceoncredit
Table10.Consumersegmentsdefinedbykeyfinancialbehaviortraits.
IndicatorCategory ExampleMetric SignofVulnerability WeightinIndex Interpretation
Liquidity Liquidassetstomonthlyexpenses Lowratio High Poorshockabsorption
Leverage Debt-to-incomeratio Highratio High Creditburdenrisk
Stability Incomevariance Highvariability Medium Unpredictableearnings
DistressHistory Overdraftsordelinquencies Frequentevents High Signsofpaststruggle
SpendingPressure Discretionaryvs. essentialratio Lowdiscretionary Medium Budgetrigidity
Table11.Keydimensionsusedinfinancialvulnerabilityscoringmodels.
SegmentationMethod InputType Supervision UseCase Flexibility
Clustering(e.g.,K-Means) Normalizedfinancialfeatures Unsupervised Exploratorygrouping High
Rule-BasedSegmentation Threshold-definedmetrics Manual Regulatorycompliance Medium
SupervisedClassification Labeledriskoutcomes Supervised Predictiverisktagging High
Score-BasedBinning Compositeindexscore Semi-supervised Tieredwellnessassignment Medium
DynamicRescoring Time-evolvingprofile Periodicupdates Trendtracking High
Table12.Comparisonofsegmentationtechniquesforfinancialvulnerabilityassessment.
interpretabilitybyeitherkeepingsimplemodelsorbyrestrict- howchangingsomebehaviors(e.g., loweringdiscretionary
ingmodelcomplexity(e.g.,usingalimitednumberoffeatures) spendingorbuildingupsavings)wouldincreasetheirfinan-
topreservetransparency. Inconsumerriskmanagement,the cial health score. By opening the risk assessment process,
incrementalpredictivebenefitofanon-transparentmodelis bankscanreversetheimpressionfrom"thecomputergave
notworththepriceofatransparencyloss,especiallyforsensi- meabadscoreandIhavenoideawhy"to"Iunderstandmy
tivedecisionsaffectingpeople’slives. financialprofile,andIknowwhatIcandotoimproveit."[16]
Forthosesituationswheremorecomplexmodelsareused, Explainabilityisalsonecessaryforfairnessandethicalre-
post-hocexplainabilitytechniquescanclosethegap. Methods sponsibility. Ifmodelsareexplainable,theycanbemoreread-
likeLIMEandSHAP,forinstance,areverypopularforextract- ilyauditedfortestingforpotentialbiases. Forexample,ifan
ingexplanationsfromblack-boxmodels. Thesemethodscan explainabilityanalysisrevealsthatamodelheavilypenalizes
give,foranypredictionmade,anapproximateideaofwhat numeroustransactionsofsmalldollaramounts,onewould
inputfeaturesmostcontributedtotheresult. Areal-world wishtoinquirewhetherthatwoulddisproportionatelyhurt
exampleofanexplainableAIfinancialvulnerabilitysystem certainsegments(e.g.,thoselivingpaychecktopaycheckand
mightoutput: "Keycontributingfactorsforthisriskscore: 1) makingmultiplesmallpurchasesofnecessities,asopposedto
Veryhighcreditusage(using90%ofcreditlimits),2)Unsta- themorefinanciallywell-offwhospendinlargeramounts).By
bleincome(incomefluctuatingby±30%month-over-month), examiningfeatureimportanceanddecisionrules,analystscan
3)Lowsavingsbalance."Thiskindofexplanationdistillsthe determineifpatternsarelikelytobeassociatedwithsensitive
model’scomplexcalculationsintohuman-comprehensiblefac- attributes(likerace,gender,orage),evenifsuchattributesare
tors. Itenablesaloancandidatetounderstandwhytheyhave notexplicitlyused. ThisisresponsibleAIduediligence: mod-
beenclassedashighriskorallowsapersonalfinancialadvisor elsneedtonotonlybeaccurate,butalsofairandexplainable.
toseewhyaclienthadbeenflaggedasfinanciallyatrisk.Most Ifamodel’sreasoningcannotbeexplainedeasily,thenthereis
importantly,itprovidesareastoimprove–thecustomerin moreriskthatithasconcealedbiasesorwillmakedecisions
thesamplemayseektoreducecreditcardbalancesormake thatcannotbedefended.
incomeasstableaspossible,assoonastheyknowtheseare
Operationally, fielding explainable AI involves incorpo-
majordriversoftheirriskscore.
rating explanation generation into the model deployment
Transparencyofriskassessmentalsoincludestransparency pipeline. Forexample,ifabankemploysanautomatedsystem
regardingwhatinformationisbeingused. Consumerswill towarncustomerswhoareindangeroffinancialdifficulty,it
morereadilyacceptandtrustafinancialhealthscoreifthey couldaccompanyeachwarningwithaconciseexplanation:
knowthatitisbeingdrivenbylogicalinputsliketheirincome- "Wehaveseenyourmonthlyspendinghasoutstrippedincome
spending balance or repayment history, rather than undis- forthreeconsecutivemonthsandyourcredituseishigh–this
closed data points scraped from their social media. Part of canresultinfinancialhardship."Givingthiskindofcontext
explainableAIinthiscategoryissimplybeingopenwiththe notonlyenablesthecustomertotakeknowledgeableaction
customers:whatsortsofdatafeedintothemodelsandwhyare butalsominimizesconfusionorannoyancethatcouldresult
thosesignificant. Thatmaybedonethrougheducationalma- fromanalertthatmightotherwisebeperceivedasintrusiveor
terialsoreveninteractivetoolsallowingcustomerstomodel unexplained.Internally,riskmanagersviewingmodeloutputs
11

DataScienceandBusinessAnalyticsApproachestoFinancialWellbeing:ModelingConsumerHabitsandIdentifyingAt-RiskIndividualsinFinancialServices
+
|     |                  | Ł   |     |                         | 8           |     |     |
| --- | ---------------- | --- | --- | ----------------------- | ----------- | --- | --- |
|     | DataPrivacy      |     |     |                         | Fairness    |     |     |
|     | •GDPRcompliance  |     |     |                         | •Biasaudits |     |     |
|     | •Explicitconsent |     |     | •Disparateimpacttesting |             |     |     |
|     | •Righttoerasure  |     |     | •Fair-MLalgorithms      |             |     |     |
(cid:192)94%compliancewithAIethicsguidelinesthroughautomatedaudits
(cid:255)
EthicalGovernance
•Reviewboards
4
|     | ¡                        |     | •Impactassessments   |     |     |                     |     |
| --- | ------------------------ | --- | -------------------- | --- | --- | ------------------- | --- |
|     | Beneficence              |     | •Regulatoryalignment |     |     | Transparency        |     |
|     | •Win-winincentives       |     |                      |     |     | •SHAPexplanations   |     |
|     | •Vulnerabilitysafeguards |     |                      |     |     | •Humanappealprocess |     |
|     | •Anti-predatorycontrols  |     |                      |     |     | •Modeldocumentation |     |
+
Figure8.EthicalAIGovernanceFrameworkforConsumerRiskAnalytics
onadashboardwillwanttoreceiveaggregateexplanations– habits,andevenreligion(takenotethatcontributionstochar-
e.g.,"TopreasonsforNortheastregioncustomers’vulnerability ity,medicalexpenses,orchurchtithemightbeinferredfrom
scoresthisquarterweredropsinincomeduetounemployment spending). Itisimportantthatanysystemoperatingsuchdata
andincreasedgaspricesimpactingcostofliving"–thatcan doessowithexplicituserconsentandwithintheremitofdata
informstrategicdecisions. protectionacts. RegulationsliketheEUGeneralDataProtec-
Itisinterestingthatamodel’scomplexitycanbeatrade-off tionRegulation(GDPR)exerttightcontrolsontheprocessing
withthesimplicityofanexplanation. Anexplanationmight ofpersonaldata,imposingpurposeslimitation(datacollected
needtosimplifysomewhatsometimes(e.g.,aninteractionef- foronepurpose,e.g.,creditscoring,nottobere-purposedarbi-
fectmightbesimplifiedtoonefactorintheinterestsofbrevity). trarilyforanotherwithoutconsent)andextendingcontrolover
ExplainableAIefforts,therefore,trytofindthesweetspot,pro- individuals’data(e.g.,rightofaccess,correction,orerasureof
vidingenoughdetailtobeaccurateandusefulbutnotenough informationaboutthem). Financialinstitutionsmustensure
tooverwhelmtheaudiencewithtechnicalities. Workinthis thatcustomersareinformedincleartermsiftheirtransaction
directionisongoing,withresearchintomethodsthatmake dataordigitalfootprintsarebeingscrutinizedforwell-being
evendeeplearningmodelsmoreinterpretable,andintovisual- orriskscoring,andtheymustprovideopt-outsorsubstantial
izationtoolsthathelpnon-technicalstakeholderslearnabout alternativeswherepossible.
modelbehavior. [17] Fairnessandnon-discriminationarealsoparamount. Data-
Ingeneral,addingexplainabilitytofinancialbehaviormod-
|     |     |     |     | driven models | can unwittingly | perpetuate | or even worsen |
| --- | --- | --- | --- | ------------- | --------------- | ---------- | -------------- |
elsisnotatechnicalindulgencebutanecessarysteptodeploy- societalbiasesinpastdata[18]. Forexample, ifpreviously
| ingsuchmodelsinrealfinancialservices. |     | Openriskassess- |     |     |     |     |     |
| ------------------------------------- | --- | --------------- | --- | --- | --- | --- | --- |
somelow-incomegroupshadhadlimitedaccesstofinancial
mentsallowconsumerstohavefaithintheadviceordecisions
institutionsandthuslesscompletecredithistoriesormore
thatcomefromanAIsystem,regulatorstohaveconfidence erraticfinances,anuninformedmodelwouldlabelthemas
thatautomateddecisionsareaccountable,andfinancialinsti-
higherriskmerelyduetothosecircumstancesratherthandue
tutionsthemselvestoensurethattheirpursuitofdata-driven toanyinherentinabilitytomanagetheirfinancesresponsi-
insightsremainsrootedinprinciplesoffairnessandcustomer-
bly. Responsibledeploymentcallsformodelstobetestedfor
| centricservice. | Thenextpartshallcoverthebroaderethical |     |     |                  |                 |             |              |
| --------------- | -------------------------------------- | --- | --- | ---------------- | --------------- | ----------- | ------------ |
|                 |                                        |     |     | disparate impact | under different | demographic | strata. This |
andoperationalfoundationsthatmustbeestablishedinparal- mightinvolverunningsimulationsoraudits: arecustomers
lelwiththetechnicaldeploymentofsuchanalyticsinorder
ofacertainage,race,orgenderconsistentlyassignedlower
forexplainableandresponsibleAItobecomecommonplace riskscoresbythemodelevenwhentheirfinancialprofiles
inconsumerfinance.
|     |     |     |     | aresimilartoothers? | Ifyes, | themodelcanbeadjusted(or |     |
| --- | --- | --- | --- | ------------------- | ------ | ------------------------ | --- |
eventheinputdatarethought)inanefforttoavoidredlining
|            |                 |            |         | ordiscriminatorybehaviorundertheguiseofanalytics. |     |     | Some |
| ---------- | --------------- | ---------- | ------- | ------------------------------------------------- | --- | --- | ---- |
| 6. Ethical | and Operational | Frameworks | for Re- |                                                   |     |     |      |
organizationscreateanethicsreviewboardorincludebias
| sponsible | Deployment |     |     |                                               |                    |                   |            |
| --------- | ---------- | --- | --- | --------------------------------------------- | ------------------ | ----------------- | ---------- |
|           |            |     |     | auditorsinmodeldevelopmenttodetectsuchissues. |                    |                   | Tech-      |
|           |            |     |     | niques for                                    | enhancing fairness | involve stripping | or capping |
6.1. EthicalPrinciplesinConsumerRiskAnalytics
Applicationofdatasciencetopersonalmoneydataisfraught theinfluenceofproxyvariablesthataretoohighlycorrelated
withethicalconcerns,givenhowindividualmoneybecomes withprotectedattributes,orusingfairness-constrainedma-
in people’s lives. Privacy respect is likely the top principle. chinelearningalgorithmsthattradeoffaccuracyagainstfair
| Expenditurecanrevealmuchaboutanindividual’slifestyle, |     |     |     | treatment. |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | ---------- | --- | --- | --- |
12

DataScienceandBusinessAnalyticsApproachestoFinancialWellbeing:ModelingConsumerHabitsandIdentifyingAt-RiskIndividualsinFinancialServices
˘Biasmitigationviaadversarialretraining
|                     | —                    |                    | (cid:192)        |     |                      | (cid:181)            |     |     |     |
| ------------------- | -------------------- | ------------------ | ---------------- | --- | -------------------- | -------------------- | --- | --- | --- |
| 1stLine:Development |                      | 2ndLine:Validation |                  |     |                      | 3rdLine:Audit        |     |     |     |
|                     | •Modelbuilding       |                    | •Fairnesstesting |     |                      | •Compliancechecks    |     |     |     |
| •Initialvalidation  |                      | •Performanceaudits |                  |     |                      | •Processreviews      |     |     |     |
|                     | •Technicaldocs       | •Biasmitigation    |                  |     | •Regulatoryreporting |                      |     |     |     |
|                     | ı                    |                    |                  |     |                      | T                    |     |     |     |
| DataSafeguards      |                      |                    |                  |     | ProductionMonitoring |                      |     |     |     |
|                     | •Differentialprivacy |                    |                  |     |                      | •Modeldriftdetection |     |     |     |
|                     | •RBACpolicies        |                    |                  |     | •Real-timedashboards |                      |     |     |     |
|                     | •MPCprotocols        |                    |                  |     |                      | •Auto-retraining     |     |     |     |
(cid:215)Avgmonthlydrift:moderate(PSI)
Figure9.ThreeLinesofDefenseOperationalModelwithContinuousMonitoring
Anotherethicalprincipleisbeneficence–theprinciplethat release. Banksuseacommon"threelinesofdefense"model
theanalyticsshoulddomoregoodthanharmtoconsumers. riskmanagementframework. Inthisarchitecture,thedevel-
Unlikesomeolderriskmodels,whichareprimarilyforthe opmentordatascienceteam(firstline)buildstheanalytics
institution’s gain (e.g., to minimize loan losses), consumer- andisaccountableforinitialdocumentationofhowitworks
focusedanalyticsneedtobepositionedwiththeconsumer’s and meets regulatory needs and ethical practices. There is
welfareinmind. Thismeansusingtheinsightsnottoexploit thenasecondlinewherethereisadistinctindependentmodel
weaknessesbuttomitigatethem. Forinstance,theresearch validationorriskoversightfunctionwhoauditsthemodelby
revealsthataconsumerwilltendtobeinneedofcashahead challengingassumptionsmade,validatestheoutputstested,
ofpayday,andtheethicalthingtodowouldbetogiveadvice andindeedverifyingthatthemodelhasstandardsforfairness
oralow-costoption(likeacheapshort-termloanwithlowor andexplainability.Finally,internalauditorsomesimilarfunc-
nocharges)ratherthanencouragingahigh-costloanorallow- tion (third line) from time to time verifies that the process
inghigh-overdraftchargestoaccumulate. Inpractice,getting ofgovernanceitselfisingoodworkingconditionandmod-
theincentivesalignediskey: bankshavecometorealizethat elsinproductionremaincompliantandeffectiveinthelong
helpingcustomersimprovetheirfinancialwell-beingcanalso term. Thisformalprocess,whileoriginallydesignedfortradi-
benefitthebankinthelongtermthroughgreaterloyaltyand tionalcreditriskmodels,isincreasinglybeingusedwithAI
lowerdefaultrates,andawin-winsituationisachieved. But andmachinelearninginfinancetoverifywhethertheyare
thatalignmentmustbemaintainedconsciously,sothatwhat- trustworthy.
everisdoneautomaticallyasabyproductofthesemodelsmust Anothercriticaloperationalconcernisdatagovernance[20].
beinthecustomer’sbestinterest. Internalpolicymightfor-
Withadditionofnewsourcesofdata(likedetailedtransactions,
bidusingthevulnerabilityflagstoengageinaggressivecredit
socialdata,etc.),rigorouscontrolsondatasecurityandaccess
marketing,forexample.
|     |     |     | willneedtobeenforcedbyinstitutions. |     |     |     |     | Accesstosensitive |     |
| --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | ----------------- | --- |
Transparencyandchoicealsohaveamoralcomponent,in
informationshouldbepermittedonlytoindividualswhohave
termsofexplainabilitydiscussedearlier[19]. Onanethical aneedtoknow,andanalysiscanbedoneonde-identifieddata
level,customersshouldneverfeelpowerlessunderanalgo-
|     |     |     | quitefrequentlytoprotectindividualprivacy. |     |     |     |     | Techniqueslike |     |
| --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | -------------- | --- |
rithm’sjudgeandjury. Bankscanfostertrustbybeingopen differentialprivacyorsecuremulti-partycomputationcanbe
aboutwhytheyusesuchanalytics("weusethissystemtohelp
|     |     |     | employed | in situations | where | insights | need | to  | be obtained |
| --- | --- | --- | -------- | ------------- | ----- | -------- | ---- | --- | ----------- |
determinewhenyoumayneedassistance,sowecanprovide
|     |     |     | fromdatawithoutexposingrawpersonaldatatoanalysts. |     |     |     |     |     | Fur- |
| --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | ---- |
ittoyouproactively")andbyprovidingmeansforrecourse. If, thermore,whenworkingwithfintechsorthird-partyanalytics
say,acustomerisdeniedaspecificproductorissubjecttoan
providers,contractsandgovernancehavetoensurethatthese
alternativeprocedureduetoariskmodel,heorsheshouldbe partnerssticktothesamelevelofdataprotectionandethics.
abletoseekreviewbyahumanorhavetheabilitytoappeal.
|     |     |     | Deploying | models | in a | production | environment |     | also in- |
| --- | --- | --- | --------- | ------ | ---- | ---------- | ----------- | --- | -------- |
Variousjurisdictionsenactthisrighttohumanreviewinto
|     |     |     | volves pragmatic |     | approaches | to integration. |     | Systems | need |
| --- | --- | --- | ---------------- | --- | ---------- | --------------- | --- | ------- | ---- |
legislationforautomateddecisions. Evenaboveandbeyond
tobebuilttocollecttheresultsofanalytics(alerts,riskscores,
legalobligation,offeringanaccessibleprocessforcustomersto
segmentclassifications)andfeedthemintocustomerservice
askquestionsorchallengeanappraisalisarealpartofethical
|     |     |     | flowsordigitalbankingportalsseamlessly. |     |     |     |     | Forexample,ifthe |     |
| --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | ---------------- | --- |
customerservice.
modelmarksacustomerasbeingatriskinrealtime,therehas
|     |     |     | tobeaprocess: | perhapsanautomatednotificationapportext |     |     |     |     |     |
| --- | --- | --- | ------------- | --------------------------------------- | --- | --- | --- | --- | --- |
6.2. OperationalGovernanceandDeploymentStrategies messagewithanoffertotalktoafinancialplanner,orthecus-
Implementingethicalprinciplesinpracticereliesonstrong tomer’srecordwithinthecustomerrelationshipmanagement
operationalsystemswithinfinancialinstitutions. Oneofthese databaseismarkedsothatwhentheycallcustomersupport,
isgovernance: settingclearcontrolovermodelcreationand theagentisawaretohandlewithextracare. Customer-facing
13

DataScienceandBusinessAnalyticsApproachestoFinancialWellbeing:ModelingConsumerHabitsandIdentifyingAt-RiskIndividualsinFinancialServices
employeeshavetobetrainedtounderstandmodelresponses severalsourcestoprovideconsumersandlenderswitha360-
andrespondappropriately. Abankemployeemaybetaught degreepictureofsavingandspendinghabits. AGermanor
howtoinitiateadelicateconversationregardingbudgetsifthe French bank might partner with a fintech company to add
systemindicatesthatthecustomerisindistress. Theconver- real-timespendinganalysistoitscreditdecisioning,oraUK
sationhastobeconstructiveandnotinvasive. Thishuman- digitalbankmightgiveeverycustomerafinancialwellness
in-the-loopiscritical;regardlessofwhatanalyticsaredone, scoreontheirmonthlystatement,alongwithAI-poweredper-
thefrontlineexecutioncanbewhatturnsoutcomes. There- sonalizedrecommendations. Theemphasisinsuchmarkets
fore, changemanagementandstafftrainingarepartofthe istypicallyonimprovingaccuracyandpersonalization,butal-
operationalframeworkwhenimplementingthesedata-driven wayswithinhighlycontrolledenvironmentswhereconsumer
solutions. interests have to take priority. European regulators, for in-
Monitoringandmaintenanceofmodelsonanongoingbasis stance,desiretoregulatealgorithmicdecision-making,calling
isyetanotherpillarofethicaloperations[21].Trendsinspend- fortransparencyandequity(borneoutbysuchrulesanddi-
ingbehaviorandeconomicconditionsmayalsoevolveover rectivesasthoseissuedbytheEuropeanBankingAuthority).
time,andmodelscandegradeinfairnessoraccuracy—theso- TheapplicationofexplainableAIandbiastesting,thus,isnot
calledmodeldrift. Institutionsmusthaveinplacesystemsto merely best practice but increasingly compliance-driven in
tracktheperformanceoftheirmodelsoffinancialwell-being thesemarkets. [23]
(e.g.,comparingprojectedlevelsofriskovertimewithactual Emerging markets are distinct, however, and bring with
results,andobservingforcreepingbias). Whenforecastsfrom themanewsetofopportunitiesandchallenges. Inthema-
amodelstarttodivergefromrealityorshowundesirablebias, jorityofdevelopingnations,vastsegmentsofthepopulation
themodelmayrequireretrainingoradjustment. Mostorgani- are "thin-file" or "credit-invisible" consumers – people with
zationscreateascheduleofperiodicreviewsforeachmodel, minimalmainstreambankinghistory,perhapsbecausethey
andtheyidentifytriggersthatwouldcallforanoff-cyclereview arelargelyincashorhavenewlyenteredthefinancialsystem.
(e.g.,inthecaseofamajoreconomiceventlikeapandemic, Forthem, standardinformationavailabletouseforriskas-
whichcouldrenderassumptionsinthemodeloutdated). sessmentissparse, andalternativedataandnew-modeling
Regulatorycompliancechecksmustbeintegratedintothe takeover. InAfrica,Asia,andLatinAmerica,financialser-
processflowofoperations. Whenbringinginanovelanalytics vicescompanieshaveturnedtoalternativedatalikemobile
technique, it may be subject to regulatory sign-off or inter- phoneusage,utilitybillpayments,andsocialnetworkdata
nalcompliancesign-offatleast. Documentationiskeyhere: to gauge creditworthiness and stability. Kenya is an exam-
holdingtherightrecordsofhowthemodelwasbuilt,what ple,wherethewidespreaduseoftheM-Pesamobilepayment
dataitrunson,howitwasstress-testedforbiasanderrors, systemcreatedarichdatasetofonlineandpeer-to-peerpay-
and what controls are in place. This documentation is not ments. KenyanbankshavealreadyusedM-Pesatransaction
onlyaprotectionforauditorcustomercomplaintpurposes, histories as a proxy for assessing loan quality in unbanked
butitalsoforcestheinstitutiontohaveseriouslyweighedthe consumers,usingmobilewalletusageinthismanner. Other
deploymentfromallsides. suchpracticesexistinIndia,wherefintechlendershaveaccess
Operationalsystemsininternationalfinancialinstitutions toonlineshoppingtransactiondataoreveneducationalback-
needtobeadaptabletosuitthevariedregionalregulations groundandentranceexamscoresofaborrowerasinputstoits
and cultural desires. What is good practice in one country creditalgorithmsforyoungborrowerswiththinornocredit
can prove sensitive in another. For example, using certain data. Financialinclusionistheprimemoverinsuchmarkets:
informationliketelecommunicationsdataforcreditscoring datascienceisbeingusedtoreachouttohistoricallyexcluded
isbusiness-as-usualinsomeemergingmarketsbutwouldbe people. Centralbanksandgovernmentsliketofollowthese
controversialincountrieswithstrongerprivacynorms.Agood measuresbutarenotslowtoissueregulationssothattheuseof
deploymentframeworkusesthestrictestapplicablestandards non-traditionaldatadoesnotinterferewithprivacyorleadto
andoftenusesthemindiscriminatelytosimplifycompliance predatorylending. India’sReserveBankofIndia,forinstance,
andprotecttheinstitution’sreputation. [22] hasbeenconsideringhowtoregulatedigitallendingappsthat
tapsmartphonedata,strikingabalancebetweeninnovation
andconsumerprotection.
7. Global Perspectives and Implementation
Cultural and economic context determine what kinds of
Strategies
dataareseenasacceptableorpredictive. Chinesetechgiants,
Thepursuitofconsumerfinancialsuccessbydataanalysisis forinstance,havebuiltsocialcreditsystemsthatassemblean
aglobalphenomenon,butitsexecutiondifferswidelyamong incrediblevarietyofdatapoints–frominternetconsumption
regionsandmarkets. Indevelopedeconomieswithadvanced patternstosocialconnections–toassessindividuals. Thishas
financeinfrastructure,nearlyalladultconsumersleavedig- ledtoextremelypowerfulcredit-scoringsystemsthatcanfund
ital finance footprints – credit card usage, banking history, loanstomillionsofpeoplebasedonalternativecreditinfor-
onlinetransactions,etc. Banksintheseinstancespossessen- mation,butithasalsosparkeddebatethroughouttheglobe
richeddataandareincreasinglysupplementingtraditional regardingprivacyandstateinterference[24]. WithinWestern
creditscoringwithdetailedfinancialhealthmetrics. Forin- societies,thesamedegreeofmixingofpersonal,social,and
stance,withintheUKandtheEuropeanUnion,OpenBanking financialdatawouldmostprobablyfaceoppositionfromthe
regulationshavecompelledfinancialinstitutionstoprovide publicandauthorities. Indeed,thatwhichistechnologically
consumeraccountdata(withconsent)tothird-partyproviders. possibleisfrequentlyethicallydifferentacrossborders. Asa
Thishascreatedalucrativemarketforpersonalfinanceman- result,financialinstitutionsgloballyarecompelledtomodify
agementsoftwareandanalysistoolsthataggregatedatafrom data policies to accommodate local regulation and require-
14

DataScienceandBusinessAnalyticsApproachestoFinancialWellbeing:ModelingConsumerHabitsandIdentifyingAt-RiskIndividualsinFinancialServices
ments. Abankinsuchacasecanmakeuseofalternatedata "thisappaided5,000familiessavemoreandbecomedebt-free")
inanAsiandevelopingmarkettobuildcreditprofiles,while canhelpingainingacceptance.
intheUSitusesjustFICOscoresandaccountinformation Intheend,theshifttowardsconsumer-centricriskmanage-
frombanksbecauseofregulatoryandcustomeracceptance mentbasedondataisglobalbutdoesnotproceeduniformly.
reasons. Eachcountryorregioncreatesitsownequilibriumbetween
Asecondaspectofinternationalimplementationisinter- innovationandregulation,employingdataandprivacypro-
nationalorganizationsandcross-borderknowledgediffusion. tection,andinstitutiongainandconsumerwell-being. Sup-
InternationalorganizationsliketheWorldBank,International portively,theoveralldirectionistowardbehaviorsthathonor
FinanceCorporation(IFC),andtheOECDhavebeenactive openness,fairness,andgoodness,forconsumers. Whether
inresearchingandpromotingbestpracticesinfinancialwell- it’s an East African small farmer getting a loan via mobile
beingandinclusion. Theyholdpilotprograms–suchaspi- dataanalysisoranEUmiddle-classhouseholdusinganAI-
lotinganewfinancialhealthscoringsysteminadeveloping poweredbankapptomanagetheirfunds,thedenominatoris
countryinvolvinglocalbanksandfintechs–andthenexport- usingtechnologyanddatatoenhancefinancialsecurity[26].
ingthelessonslearnedfromthese. Taskforcesandconfer- Theglobalperspectiveemphasizesthatwhilefinancialbehav-
encesbringregulatorsandindustryleadersfromacrossthe iorandchallengeswilldifferindetailacrosstheworld,the
globetodiscusstopicslikeAIcredit,dataprivacy,andcon- fundamentalgoalsofriskmodeling–anticipatingtroubleand
sumerempowerment. Throughtheseintermediaries,some helpingthestricken–areuniversal. Smallandlargefinancial
sortofinternationalconsensusisgraduallyemergingaround institutionsarelearningfromoneanotherand,stepbystep,
keyprinciples: thatreal-timeinformationcanbeusedtoim- buildingamoreinclusiveandrobustfinancialcontextthrough
proveriskdetection,thatexplainabilityandfairnessmustbe theseadvancedanalytics.
baked into the algorithms, and that consumers themselves
ultimatelymustbenefitfromthedatathatisproducedabout
8. Conclusion
them.
Usingthesecutting-edgeanalyticsputsstrategyoutsideof Financialinstitutionsacrosstheglobeareexperiencingacross-
thealgorithms. Inmostcases,teamworkistheanswer. Banks roadswhereunprecedentedlevelsofgranularreal-timedata
maypartnerwithtelecomoperatorstogainaccesstomobile comeintocontactwithanintensifyingsocialobligationtoad-
billpaymenthistory(subjecttocustomerconsent)aspartof vancegenuineconsumerfinancialwell-being. Riskmanage-
creditevaluation–atrendinLatinAmericaandAfrica. Fin- mentfordecadeswasallbackstop: creditbureaus,scorecards,
techcompaniesliketobeinnovationlabs,experimentingwith and capital buffers were created to protect against balance
new scoring models based on machine learning that other sheetlossesonceborrowerdifficultyhadalreadytakenthe
banksormicrofinanceinstitutionscanlicenseorimplement formofdelinquency. Theparadigmsforanalysisdiscussed
[25]. Incountrieswithmaturingcreditbureaus,consortiaof here lay out a more ambitious task, namely, turning every
lenderscanpoolthemselvestogethertoprovideanonymized deposit,withdrawal,subscription,anddiscretionaryexpendi-
dataandbuildcommunity-wideindicesoffinancialdistress tureintopartofacontinuousearly-warninglatticethatpro-
tobenefittheentireindustry(indirectlyalsoconsumerswho tectsfamiliesfromgettingintotroubleinthefirstplace. To
derivebenefitsfromimprovedlendingdecisions). Agoodex- achieve this, re-imagination of data streams, paradigms of
ample of this cross-agency approach is in the UK with the modelling,andorganisationalincentivesneedtobealigned
FinancialVulnerabilityIndex,whichcollatesevidencefrom sothatthetoolsinitiallydesignedtobeusedbylendersare
differentsourcesinordertogeo-mapfinancialvulnerability; redirectedasinstrumentsofpreventivecare. Thepagesahead
andalthoughstillatanearlystage,whichshowsthepotential distillimportantinsightsandsketcharesearchandpractice
ofdatasharinginthesectortoflagupareasofcommunity agendawhoseconsequencesradiatefrommicro-interventions
vulnerabilityandpotentiallyinfluencepolicyortargetsupport. tomacro-financialstability.
Inpractice, fortheirroll-outglobally, flexibilitywillbea Centraltothenewvisionisaconceptualturnaboutintra-
requirement. Locallegislationcouldspecifywhatinforma- ditionalcreditanalytics. Thetraditionalmodelstreatrepay-
tioncanbeused–e.g.,applicationofgenderorpostalcode mentcapabilityasasnapshotintimeatorigin, entrapping
increditmodelscouldbedisallowedinsomejurisdictionsto riskinsideabinarizedmetricofdefaultornon-default. Mod-
preventdiscrimination. Technologyinfrastructurediffersas erndatasciencereimaginesriskasanevolvingprocesswhich
well;real-timestreaminganalyticsassumehigh-qualitydigital canbeguidedtowardsorawayfromtheedge. Transactional
connectivityandbankingsystemintegrationthatexistinsome cycles, cash flow volatility, saving periods, and behavioral
countriesbutnotothers. Implementationstrategiesusually micro-indications now provide temporal resolution, allow-
startwithpilotschemesinacontrolledsetting(incertainin- ing institutions to detect inflection points several months
stancesunderaregulatorysandboxagreementsupportedbya aheadofarrearsbecomingapparent. Theinclusionofsuch
centralbank)todemonstratetheworthandworkoutkinks. time-sensitive profiles within business-as-usual transforms
Successfulpilots–e.g.,aschemetoprovideautomatedfinan- riskmanagementfromaperiodicsnapshottoanongoingdia-
cialhealthguidancethroughSMSinanAsianmarket–can loguewithacustomer’sunfoldinglifecontext. Inherently,this
thenbeimplementednationallyorcopiedinothercountries reshapingflipstheepistemicinquiryfromaskingwhethera
withadjustments. Bankshavetoinvest,too,ineducatingcon- borrowerisgoodorbadcredittoaskinghowthingsstandtoday
sumersastheylaunchsuchproducts. Whenconsumersare andwhichhelpingactioncanflexthecurvetowardresilience.
notasfamiliarwiththeideaofacreditscoreoramoneywell- [27]
nessapp,thereisgoingtobelearningandskepticismthathas Technological maturity supports this ideological change.
toovercome;transparencyandshowingtangiblereturns(like Streamingingestionplatforms,event-drivenarchitectures,and
15

DataScienceandBusinessAnalyticsApproachestoFinancialWellbeing:ModelingConsumerHabitsandIdentifyingAt-RiskIndividualsinFinancialServices
elasticcloudinfrastructurenowupdateliquidityprojections, insteadofesotericcorrelationsorbiasedsurrogates.
affordability scores, and fraud indicators in real time with- Ethicalgovernmentintroducestransparencyintoprocess
out monthly statement cycles. On-device inferencing and ininstitutions. Three-linedefencedistinguishesbetweenthe
edgecryptographyencryptpaymentswhilestoringrawdata domainsofdevelopers,independentvalidators,andinternal
locallyontheconsumer’sdevice,thereforebalancinginsight auditors, locating fairness audits, privacy checks, and sce-
and privacy. Federated learning collaborations allow mod- nariostress-testingaspartofconstantdeployment,ratherthan
elstobetrainedbetweenbanks,fintechs,andtelcoswithout sign-offritual. Policyguardrailsmakeacceptabledatasources
centralizingsensitiveinformation,thereforeimprovingrep- formal,human-reviewtriggersforadverse-action,andlisted
resentativenesswithoutcompromisingsovereignty. Modern consumerrightsofexplanationandchallenge. Inclusivede-
MLOpspracticeacceleratestesting,versioning,androllback, signworkshopsinvolveconsumerchampionsandbehaviour
soiterativedevelopmentisacceleratedwithoutcompromising scientistsintoprototyperequirementphases,cuttingoffblind
governance. Aslatencyamongbehaviourandunderstanding spotsbeforetheybecomeentrenchedinsystemicinjustices.
dissolves,warningscanhitaconsumerpriortoenoughtime Wherestatuteissilent,cross-sectorchartersandvoluntaryin-
topreventoverdraftsorreorganisecommitments,transmogri- dustrycodesestablishde-factostandardsreassuringthepublic
fyingpassiverecord-keepingintostewardship. andpreventingtransformativeregulation. [29]
Numbersalone,though,cannotembracethemulti-layers Cross-jurisdictionalvariationmakesuniformdeployment
offactinpersonalfinance. Psychologicaltraitsandsituational harderbutdrivesinnovation. Inprivacy-conscious,data-rich
shocksinterveneastohowequalcashflowsrenderwell-being jurisdictions, open-bankings plans bring together safe data
effects. Surveysofconscientiousness,temporaldiscounting, transferanddemandexplainablealgorithms,compellingin-
andself-efficacyinfinance,whendistilledintoformalvari- cumbents toward high-precision transparency dashboards.
ables,bringnuancethatledgerslack. Eventdetectionalgo- Where thin-file conditions are the norm in lower-income
rithms alert to changes in employment, disease, or natural economies, alternative-data methods, drawing on mobile-
disastersthatconstraindisposableincomeorballoonmanda- money transaction history, prepaid airtime purchases, and
tory spending. By uniting these human factors with trans- utility-paymenttimeliness,wideninclusion. Regulatorysand-
actiondata,algorithmscandistinguishbetweendisciplined boxesinKenya,India,Brazil,andtheGulfallowfintechsto
thriftandcoercedparsimony,orleveragedopportunismand test new scoring models under overseers’ gaze, finding the
desperateborrowing. Modelsnolongerlabelbehaviouriniso- balancebetweenprotectionandspeed. Culturalnormsalso
lationbutconstructnarratives: increasingcredit-cardusage shapewhatisacceptablepractice: whathasbeeninherited
andindicatedreductionsinhoursworkedpointtoquestion- fromsocial-mediagraphsmaybeacceptableinSoutheastAsia
ablebalancing,butthesameincreasecombinedwithapay butnotWesternEurope. Theinstitutionsthatwillprosperwill
bonuspointstocelebratoryspendingwithlittlefuturerisk. betheonesthatembedflexibilityasanembeddedcompetence
Segmentationplacessuchsubtletyintoactiononamass ratherthanbolt-onconformity.
scale[28]. Advancedclusteringandsupervisedclassification Theanalytichorizonissettoexpandevenfurther. Smart-
carveportfoliosintostratadefinedbyliquiditycushions,lever- hometechnologywillmonitorenergyconsumptionpatterns
ageratios,incomepredictability,andpsychologicalreadiness. linked to discretionary spending and environmental expo-
Theresultingtaxonomysupportsdifferentiatedproductjour- sure. Connected vehicles will deliver high-granularity mo-
neys: customerswithexcesscapacityareencouragedtoward bilitypricesandassetvaluations. Voice-assistantrequestand
long-horizon investing; those at near insufficiency are pro- contact-centretranscriptnatural-languageprocessingwillun-
videdwithauto-sweeptools,fee-freebuffers,andstepped-up coversentimenttrajectoriesthatforecastcascadesofexpen-
repaymentplans;thoseinacutestressarestreamlinedtohu- ditureordepletionofsavings. Throughfullyinformedcon-
man advisors and hardship relief. Because boundaries be- sent,wearablebiosensorsmightyieldphysiologicalmarkersof
tweensegmentsaredefinedbyobservablemetrics,improve- stress,enablinginterventionsbeforeworryaboutmoneyleads
mentcanbemeasured: migrationsfromat-risktostableseg- tomaladaptivechoices. Everymodalityaddstopredictionbut
mentsarequantitativeevidencethatinterventionsarebuilding alsoaddsprivacycomplexity,needingcryptographicsafeguard
resilience. Conversely,anyfragilitytrendbetweencohortscan andgovernancestructuresthatevolveinparallel.
triggermacro-prudentialregulationlongbeforedefaultsstart System-levelimpactwillbecontingentuponcross-sector
toaccumulate. collaboration[30]. Bankspossessledgerdepth,telecomshave
Explainable artificial intelligence is the intervening key behavioural breadth, insurers trade life-cycle risk, and gov-
thatunitesmodellingsophisticationandpublicaccountability. ernmentsmanagemacro-indicatorsandsocialsafety-netpro-
Gradient-boostedensemblesanddeepneuralnetworksreveal grams. Federatedanalyticconsortiaareabletocomputecol-
nuancednonlinearities,buttheirvaliditywillbeundermined lectivevulnerabilityindicesthatnosingleorganizationcould
ifstakeholderscannotinterrogateunderlyingreasoning. Tech- assemble,whichcanbeutilizedformakingsubsidypayments
niquessuchasSHAPvalueattribution,conceptactivationmap- followingclimaticshocks,efficientworking-capitalcreditfor
ping,andhuman-interpretablesurrogatemodelstransform platformgigworkers,orblendededucationcampaignscom-
underlyinginteractionsintoclearstatements: higherdiscre- biningfiscalcounselwithdigitalskilltraining. Aligningin-
tionaryspendingcoupledwithreducedbuffershasdriventhe centivesiscrucial: lendersreducelosses,publicauthorities
projectedthirty-daycash-shortfallprobabilityaboveagiven minimizesocialexpenditures,privatepartnersbuildreputa-
threshold. Narrativetransparencyinthiswaycanempower tionalcapital,andfamiliesgaintangiblewelfareadvantages.
consumerstomakechanges,facilitatefrontlinestafftogivein- Prudententhusiasmrecognizeslimitsandfrontiersofre-
dividualsizedrecommendations,andcomfortregulatorsthat search. Predictivemodelsremainprobabilisticheuristicssus-
automaticchoicesaregroundedinsoundeconomicrationale ceptibletoregimechange,black-swanoccurrences,andfeed-
16

DataScienceandBusinessAnalyticsApproachestoFinancialWellbeing:ModelingConsumerHabitsandIdentifyingAt-RiskIndividualsinFinancialServices
| backmechanisms. |     | Pandemicsatthegloballevel,geopolitical |     |     |     |     |     |     |     |     |     |
| --------------- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
References
| shocks, | and climate | shocks | can rapidly | make | past | patterns |     |     |     |     |     |
| ------- | ----------- | ------ | ----------- | ---- | ---- | -------- | --- | --- | --- | --- | --- |
[1] F.Salignac,M.Hamilton,J.Noone,A.Marjolin,and
| irrelevant. | Datadesertspersistamongdisconnectedpopula- |     |     |     |     |     |     |     |     |     |     |
| ----------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
K.Muir,“Conceptualizingfinancialwellbeing:Aneco-
tionsandthosewhoeschewformalfinance,portendinganew
logicallife-courseapproach,”JournalofHappinessStud-
| exclusiondivide. |               | Psychologicaltagsofsurveyscanstrayas |                |       |     |            |      |          |                       |      |                |
| ---------------- | ------------- | ------------------------------------ | -------------- | ----- | --- | ---------- | ---- | -------- | --------------------- | ---- | -------------- |
|                  |               |                                      |                |       |     |            | ies, | vol. 21, | no. 5, pp. 1581–1602, | Jun. | 22, 2019. doi: |
| cultural         | norms evolve, |                                      | and contextual | hints | are | mostly im- |      |          |                       |      |                |
10.1007/s10902-019-00145-3.
precise. Furtherworkisneededontransferlearningacross
[2] M.Heiskanen,Problemgamblingandfinancialwellbe-
regimes,causalinferencetountangledriverfromcorrelation,
androbustnesstechniquesthatmaintainfairaccuracyunder ing:Theexperienceoflosing,consuming,andreceiving
money,Oct.6,2016.
datascarcity.
Operationally,consumer-centricanalyticsarealreadyrecon- [3] E.PorterandD.Bowman,Shocksandsafetynets?finan-
figuringinstitutionalmetricsandcustomerjourneys. Lead- cialwellbeingduringcovid-19,May25,2021.
| ing banks | combine | net | improvements |     | in client | financial |     |     |     |     |     |
| --------- | ------- | --- | ------------ | --- | --------- | --------- | --- | --- | --- | --- | --- |
[4] M.S.TahirandA.D.Ahmed,“Australians’financial
| well-being | with | executive | scorecards | alongside |     | traditional |     |     |     |     |     |
| ---------- | ---- | --------- | ---------- | --------- | --- | ----------- | --- | --- | --- | --- | --- |
wellbeingandhouseholddebt:Apanelanalysis,”Jour-
| measuresofprofitability. |     |     | Fintechappsdynamicallymodify |     |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
nalofRiskandFinancialManagement,vol.14,no.11,
| credit limits | or payment |     | dates based | on  | affordability | mod- |     |     |     |     |     |
| ------------- | ---------- | --- | ----------- | --- | ------------- | ---- | --- | --- | --- | --- | --- |
pp.513–,Oct.26,2021.doi:10.3390/jrfm14110513.
| els forecasting | strain | in  | advance, | not over-extending |     | by de- |     |     |     |     |     |
| --------------- | ------ | --- | -------- | ------------------ | --- | ------ | --- | --- | --- | --- | --- |
[5] C.HarterandJ.F.R.Harter,“Thelinkbetweenadverse
| signandnotcapturingpenaltyincomeexpost. |     |     |     |     |     | Regulators |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
pilotregulatory-technologydashboardsthatfeedanonymised childhoodexperiencesandfinancialsecurityinadult-
|     |     |     |     |     |     |     | hood,” | Journaloffamilyandeconomicissues, |     |     | vol. 43, |
| --- | --- | --- | --- | --- | --- | --- | ------ | --------------------------------- | --- | --- | -------- |
indicatorstoforecasthouseholdstressbeforearrearsspike,
no.4,pp.1–11,Sep.9,2021.doi:10.1007/s10834-021-
showingregulatorsthemselvesareshiftingawayfromautopsy
09796-y.
| towardsearlywarning. |     | [31] |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Behinditall,theunionofhigh-speeddataandprincipled [6] A.A.ZemtsovandT.Y..Osipova,“Financialwellbeing
analyticscontainsanemancipatorypromise: renderingthe asatypeofhumanwellbeing:Theoreticalreview,”in
financialspacefromareactiverealmofcollectionsintoapre- TheEuropeanProceedingsofSocialandBehaviouralSci-
ventivesystemofrespectfulassistance. Thisvisionisattained ences,Cognitive-crcs,Feb.20,2016,pp.385–392.doi:
10.15405/epsbs.2016.02.49.
| through      | less algorithmic                             |     | creativity | and more | synchronized |     |     |     |     |     |     |
| ------------ | -------------------------------------------- | --- | ---------- | -------- | ------------ | --- | --- | --- | --- | --- | --- |
| integration. | Dataengineering,governancecontrols,frontline |     |            |          |              |     |     |     |     |     |     |
[7] S.R.TanotoandE.Evelyn,“Financialknowledge,finan-
training,incentivestructures,andempatheticuserexperience
cialwellbeing,andonlineshoppingaddictionamong
mustblendlikepiecesinawell-oiledengine. Empathycannot youngindonesians,”JurnalManajemendanKewirausa-
betransplanted;itmustpermeatethequestionsanalystsask,
|     |     |     |     |     |     |     | haan, | vol. | 21, no. 1, pp. 32–40, | Apr. 5, | 2019. doi: 10. |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---- | --------------------- | ------- | -------------- |
theriskthresholdsriskofficersset,andthetonecopywriters
9744/jmk.21.1.32-40.
use.
[8] J.J.Xiao,“Consumerfinancialcapabilityandwellbe-
| The call | to action | is  | therefore | multiconstituent. |     | Studies |     |     |     |     |     |
| -------- | --------- | --- | --------- | ----------------- | --- | ------- | --- | --- | --- | --- | --- |
ing,”inSpringerInternationalPublishing,May31,2016,
shouldincludefairnessconstraintsinoptimisationobjectives,
pp.3–17.doi:10.1007/978-3-319-28887-1_1.
openupreproduciblecomparisonbypublishingopenbench-
marks,andpartnerwithsocialscientistsforin-the-fieldexperi- [9] K.Sehrawat,M.Vij,andG.Talan,“Understandingthe
ments.Practitionersshouldbuildrapidtest-and-learncultures pathtowardfinancialwell-being:Evidencefromindia.,”
thatprototypeinterventions,trackbehaviouraleffects,andit- Frontiers in psychology, vol. 12, pp. 638408–, Jul. 21,
2021.doi:10.3389/fpsyg.2021.638408.
| eratetransparentlywithaffectedcommunities. |     |     |     |     | Policymakers |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
caninducegoodexternalitiesbyofferinginnovationcredits,
|     |     |     |     |     |     |     | [10] D. N.S., | Protection | insurance | and financial | wellbeing, |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ---------- | --------- | ------------- | ---------- |
simplifyingapprovalsfortransparentlyinclusivegoods,and
May1,2009.
subsidizingpublic-datautilitiesthatreduceinformationasym-
[11] E.NazarenkoandN.Seegert,“Currentandfuturefi-
metry. Civil-societyorganizationsandeducatorsaddtothese
nancialwellbeingofoldagerussianpensioners,”Un-
initiativesbyplacingalgorithmicdatainculturallysituated
dergraduateResearchJournal,Aug.7,2015.
financial-educationcourses.
Consumerempowermentremainsthefoundation. Data- [12] nullnull,Iseoluwadata,Jan.1,2021.doi:10.6084/m9.
figshare.14381336.
portabilitymandatesandpersonalinformationwalletsgive
individualsdirectcontroloverhowtheirdigitaltracesareag-
[13] F.C.NavarroandJ.V.B.Murcia,“Dimensionsoffinan-
| gregatedandapplied. |     | Interactivedashboardsshowingpaths |     |     |     |     |      |            |                |           |              |
| ------------------- | --- | --------------------------------- | --- | --- | --- | --- | ---- | ---------- | -------------- | --------- | ------------ |
|                     |     |                                   |     |     |     |     | cial | wellbeing: | An alternative | scale for | microfinance |
ofexpenditure,liquiditybuffers,andtheoreticalconsequences borrowersindigoscity,philippines,”EuropeanJournal
makeback-endassessmentsintoself-diagnosticactionables.
ofEconomicandFinancialResearch,vol.6,no.1,Apr.5,
Whencitizenscantestouttestcasescenarios—tappinganac- 2022.doi:10.46827/ejefr.v6i1.1245.
cumulationofhigh-interestdebt,streamliningsubscriptions,
[14] D.A.Hayes,S.B.Collard,A.D.Finney,etal.,Financial
creatingalimitedemergencysavingsbucket—andseeenvi-
wellbeinginlaterlife:Evidenceandpolicy,Mar.1,2014.
| sioned | risk diminution |     | immediately, | analytics | moves | from |     |     |     |     |     |
| ------ | --------------- | --- | ------------ | --------- | ----- | ---- | --- | --- | --- | --- | --- |
distancemonitoringtohands-onplanning,fosteringagency [15] L.Appleyard,S.Dibb,andH.Aslam,Financialcapabil-
inplaceofreliance. [32] ity:Supportingmemberstowardsgreaterfinancialwell-
being,Mar.23,2020.
[16] J.Tatom,Financialwellbeingandsomeproblemsinas-
sessingitslinktofinancialeducation,Oct.1,2010.
17

DataScienceandBusinessAnalyticsApproachestoFinancialWellbeing:ModelingConsumerHabitsandIdentifyingAt-RiskIndividualsinFinancialServices
[17] S.Arber,K.Fenn,andR.Meadows,“Subjectivefinancial [30] N.F.JahanandU.Divya,Assessmentoffinancialwellbe-
well-being,incomeandhealthinequalitiesinmidand ingofslumdwellersinbangalore,Oct.6,2020.
laterlifeinbritain.,”Socialscience&medicine(1982),
[31] J.J.XiaoandN.Porto,“Financialcapabilityandwell-
vol. 100, pp. 12–20, Oct. 30, 2013. doi: 10.1016/j.
beingofvulnerableconsumers,”JournalofConsumer
socscimed.2013.10.016.
Affairs, vol. 56, no. 2, pp. 1–1018, Oct. 14, 2021. doi:
[18] J.M.NorvilitisandY.Mao,“Attitudestowardscredit 10.1111/joca.12418.
andfinancesamongcollegestudentsinchinaandthe
[32] M.K.Taft,Z.Z.Hosein,andS.M.T.Mehrizi,“Therela-
unitedstates.,”Internationaljournalofpsychology:Jour-
tionbetweenfinancialliteracy,financialwellbeingand
nalinternationaldepsychologie,vol.48,no.3,pp.389–
financialconcerns,”InternationalJournalofBusiness
398,Mar.8,2012.doi:10.1080/00207594.2011.645486.
andManagement,vol.8,no.11,pp.63–,May16,2013.
[19] C.RootmanandJ.Krüger,“Determiningconsumers’ doi:10.5539/ijbm.v8n11p63.
intentiontouseunittrusts,”JournalofEconomicand
FinancialSciences,vol.9,no.2,pp.436–454,Dec.18,
2017.doi:10.4102/jef.v9i2.51.
[20] L.FalahatiandM.F.Sabri,“Anexploratorystudyof
personalfinancialwellbeingdeterminants:Examining
themoderatingeffectofgender,”AsianSocialScience,
vol.11,no.4,pp.33–,Jan.14,2015.doi:10.5539/ass.
v11n4p33.
[21] F.Salignac,A.Marjolin,R.Reeve,andK.Muir,“Con-
ceptualizingandmeasuringfinancialresilience:Amul-
tidimensionalframework,”SocialIndicatorsResearch,
vol.145,no.1,pp.17–38,Mar.8,2019.doi:10.1007/
s11205-019-02100-4.
[22] F. Zantomio, Olderpeople’sparticipationindisability
benefits:Targeting,timingandfinancialwellbeing,Jul.6,
2010.
[23] W. B. Bajwa and M. S. L. Latif, “Cognitive and non-
cognitive factors as predictors of financial wellbeing
mediatedthroughfinancialmanagementbehaviorin
pakistan,”JournalofWorkplaceBehavior,vol.1,no.1,
pp.68–81,Dec.30,2020.doi:10.70580/jwb.01.01.025.
[24] B.C.Yin-Fah,J.Masud,T.A.Hamid,andL.Paim,“Fi-
nancial wellbeing of older peninsular malaysians: A
gendercomparison,”AsianSocialScience,vol.6,no.3,
pp.58–,Feb.8,2010.doi:10.5539/ass.v6n3p58.
[25] A.AkhterandM.-D.Sangmi,“Relationshipbetween
financialliteracyandpersonalfinancialwellbeing:An
empirical study,” Abhigyan, vol. 34, no. 3, pp. 37–46,
Dec.1,2016.doi:10.1177/0970238520160304.
[26] Z.C.Kirui,E.Simiyu,andD.Ngaba,“Personalfinancial
managementpracticesanddemographicfactorsonfi-
nancialwellbeingofmedicaldoctorsemployedinpublic
hospitalsnairobicounty,kenya,”InternationalJournal
ofCurrentAspectsinFinance,BankingandAccounting,
vol.3,no.2,pp.30–50,Oct.9,2021.doi:10.35942/ijcfa.
v3i2.193.
[27] K.Cherney,Emergingindebt:Understandingtheimpact
ofstudentdebtonthesubjectivefinancialwellbeingof
emergingadultsintheunitedstatesandcanada,Jul.13,
2021.
[28] D.Bowman,M.Banks,G.Fela,R.Russell,andA.de
Silva,Understandingfinancialwellbeingintimesofinse-
curity,Apr.30,2017.
[29] R.Rom,Theimpactofunsecuredlendingonthefinancial
wellbeingofconsumers.Jun.13,2014.
18