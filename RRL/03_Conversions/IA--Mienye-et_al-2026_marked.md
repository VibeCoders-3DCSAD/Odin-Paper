informatio n
Review
Deep Learning for Credit Risk Prediction: A Survey of Methods,
Applications, and Challenges
IbomoiyeDomorMienye ,EbenezerEsenogho* andCameronModisane
CentreforArtificialIntelligenceandMultidisciplinaryInnovations,DepartmentofAuditing,Collegeof
AccountingSciences,UniversityofSouthAfrica,Pretoria0002,SouthAfrica;emienyid@unisa.ac.za(I.D.M.);
modistc@unisa.ac.za(C.M.)
* Correspondence:esenoe@unisa.ac.za
Abstract
Creditriskpredictioniscentraltofinancialstabilityandregulatorycompliance,guiding
lendingdecisionsandportfolioriskmanagement. Whiletraditionalapproachessuchas
logisticregressionandtree-basedmodelshavelongbeentheindustrystandard, recent
advancesindeeplearning(DL)haveintroducedarchitecturescapableofcapturingcomplex
nonlinearities, temporaldynamics, andrelationaldependenciesinborrowerdata. This
studyprovidesacomprehensivereviewofDLmethodsappliedtocreditriskprediction,
coveringmulti-layerperceptron,recurrentandconvolutionalneuralnetworks,transformer,
andgraphneuralnetworks. Weexaminebenchmarkandlarge-scaledatasets,highlight
peer-reviewed applications across corporate, consumer, and peer-to-peer lending, and
evaluatethebenefitsofDLrelativetoclassicalmachinelearning. Inaddition,wecritically
assess key challenges and identify emerging opportunities. By synthesising methods,
applications,andopenchallenges,thispaperoffersaroadmapforadvancingtrustworthy
deeplearningincreditriskmodellingandbridgingthegapbetweenacademicresearch
andindustrydeployment.
Keywords: credit risk prediction; deep learning; convolutional neural networks;
transformers;machinelearning
1. Introduction
Credit risk prediction is a fundamental component of financial risk management,
enablinginstitutionstoevaluatethelikelihoodofborrowerdefaultandtomakeinformed
lending decisions [1–3]. Accurate modelling of credit risk supports financial stability,
reducesloanlosses,andcontributestoregulatorycompliance. Traditionally,logisticregres-
sion(LR)hasbeenthedominantmodelincreditscoringduetoitssimplicity,interpretability,
andeaseofdeploymentinregulatedenvironments[4]. However,asfinancialdatasetshave
AcademicEditors:Agnes
Vathy-FogarassyandJánosAbonyi growninsizeandcomplexity,conventionalLRmodelshavestruggledtocapturenonlinear
relationshipsandinteractionsamongfeatures. Thislimitationhasmotivatedtheadoption
Received:6December2025
Revised:25February2026 ofmoreadvancedmachinelearning(ML)methodssuchasrandomforests,supportvector
Accepted:27February2026 machines(SVMs),andgradientboosting,whichoftenachievehigherpredictiveaccuracy
Published:21April2026 butattheexpenseofinterpretability[5–7].
Copyright:©2026bytheauthors. Deeplearninghasbroadenedcreditriskmodellingbyenablingrepresentationlearning
LicenseeMDPI,Basel,Switzerland.
onborrowerdatathatisnonlinear,time-dependent,andsometimesnetworked. Recent
Thisarticleisanopenaccessarticle
work explores feed-forward tabular networks, sequence models, attention-based trans-
distributedunderthetermsand
formers, and graph neural networks to capture signals that are difficult to express in
conditionsofthe CreativeCommons
Attribution(CCBY)license. conventionalscorecards[8–10].
Information2026,17,395 https://doi.org/10.3390/info17040395

Information2026,17,395 2of28
Alongsidethesemethodologicaldevelopments,agrowingbodyofsurveyworkhas
reviewed credit risk models and related financial risk applications, as summarised in
Table1.EarlysystematicreviewsbyBhatoreetal.[11],Shietal.[12],Noriegaetal.[13],and
Montevechietal.[14]focusonML-basedcreditscoring,synthesisingalgorithms,datasets,
and evaluation metrics but treating deep neural networks largely as one model family
amongmany. Otherreviewsconcentrateonspecificperspectives: Kimetal.[15]andÇallı
andCos¸kun[16]examinecorporatedefaultpredictionandlong-rundefaultpredictors,
while Mhlanga [17] discusses ML- and AI-enabled credit assessment in the context of
financialinclusion. Deeplearning-centredsurveys,suchasHayashi[18],PengandYan[19],
Hoyosetal.[20],andDemmaetal.[21],identifyemergingDLtechniquesforcreditscoring
andbroaderfinancialrisk,butmainlyemphasisetabularmodelsanddonotsystematically
coversequential,transformer,andgraph-basedarchitecturesforborrower-levelcreditrisk.
Meanwhile,Mienyeetal.[22]providedabroadoverviewofDLinfinancialservices,yetits
treatmentofcreditriskwasatahigh-level. Inshort,muchofthereviewliteratureeither
prioritisesbroadMLcoverage,narrowsdeeplearningdiscussiontotabularscorecard-style
settings,ortreatsresponsibleAItopicswithoutamodel-family-levelsynthesistailoredto
borrower-levelcreditrisk.
This study addresses that gap by organising modern deep learning methods for
borrower-levelcreditriskprediction,cataloguingrecentpeer-reviewedapplications,and
synthesising deployment-relevant challenges and research opportunities. We focus on
borrower-,facility-,andfirm-levelsettingswheretheobjectiveistoestimatedefault-related
outcomesoveraspecifiedpredictionhorizonusingapplication,behavioural,bureau,trans-
actional,textual,orrelationaldata. Theprimarytargetisprobabilityofdefault(PD)and
closelyrelateddelinquencyoutcomes. Thereviewedevidencecoversconsumerlending,
SMElending,corporatecredit,andpeer-to-peerlendingusingbothpublicbenchmarks
andinstitution-scaledatasetsreportedinpeer-reviewedstudies. Weexcludeworkthat
focusesonmarketorliquidityrisk,portfoliooptimisationwithoutborrower-levellabelling,
orpurelymethodologicalcontributionsthatdonotevaluateonanempiricalcredit-risk
task. Themaincontributionsofthispaperareasfollows:
• Wepresentaunifiedoverviewofcreditriskpredictiontasksandbenchmarkdatasets,
andtracetheevolutionfromlogisticregressiontodeeparchitectures,includingMLPs,
CNNs, RNNs, transformers, and GNNs, highlighting how each class aligns with
differentcredit-riskobjectivesanddatamodalities.
• Weprovideamodality-awaresynthesisofrecentdeeplearningapplicationsincredit
risk,organisingstudiesbytabular,sequential,transformer-based,andgraph-based
models,andcollatingtheirdatasets,architectures,andreportedperformance.
• WecriticallyanalysemethodologicalandoperationalchallengesfordeployingDL-
basedcreditriskmodelsandderiveconcreteresearchdirectionsfordevelopingtrust-
worthy,regulation-readydeeplearningsolutions.
Theremainderofthispaperisorganisedasfollows. Section2presentsthereview
methodology. Section3providesanoverviewofcreditriskpredictiontasksandcommonly
used datasets. Section 4 traces the evolution from statistical to deep learning models,
detailing key architectures. Section 5 reviews peer-reviewed DL applications in credit
riskacrossdatamodalities. Section6presentsasynthesisofmajorchallengesandfuture
researchdirections. Section7concludesthepaper.
https://doi.org/10.3390/info17040395

Information2026,17,395 3of28
Table1.Summaryofrelatedreviewsoncreditriskmodellingandfinancialriskprediction.
Study Year Scope
BestpracticesforresponsibleMLincreditscoring,coveringfairness,explainability,
Valdrighietal.[23] 2025
andgovernance.
Pazetal.[24] 2025 SystematicreviewofMLandmetaheuristicsforindividualcreditriskassessment.
SystematicreviewofdefaultpredictionMLmodelsandtheirroleinstrengthening
Alvietal.[25] 2024
creditriskmanagement.
Montevechietal.[14] 2024 Comprehensivereviewofstate-of-the-artMLmodelsforcreditrisk.
DemmaWubeetal.[21] 2024 ReviewofMLandDLtechniquesforcreditscoring.
SystematicreviewofMLmethodsforcreditriskprediction,withemphasisonalgo-
Noriegaetal.[13] 2023
rithms,datasets,andperformancemetrics.
Comprehensivestudyofcreditriskevaluationmethods,includingstatisticalandML
Bhattacharyaetal.[26] 2023
models.
SystematicreviewofDL-basedcreditriskassessmentsystems,summarisingarchitec-
Hoyosetal.[20] 2023
tures,applicationsettings,andevaluationmeasures.
Review of emerging trends in DL for credit scoring, focusing on neural network
Hayashi[18] 2022
architectures,featurelearning,andinterpretability.
AsurveyofML-drivencreditrisk,organisingalgorithms,datasources,andevaluation
Shietal.[12] 2022
methods.
ÇallıandCos¸kun[16] 2021 Longitudinalsystematicreviewofcreditriskassessmentanddefaultpredictors.
Review of ML for credit risk assessment in the context of financial inclusion in
Mhlanga[17] 2021
emergingeconomies.
SurveyofDLforfinancialriskpredictionacrossmultipletasks,withcreditriskas
PengandYan[19] 2021
oneapplicationarea.
EmpiricalstudyonwhenDLisbeneficialforcreditscoring,practicaladoption,and
Gunnarssonetal.[27] 2021
comparisonwithtraditionalscoring.
SystematicreviewofMLtechniquesforcreditriskevaluation,coveringclassifiers,
Bhatoreetal.[11] 2020
featureselection,andbenchmarkdatasets.
Literaturereviewofcorporatedefaultpredictionmodels,summarisingstatisticaland
Kimetal.[15] 2020
MLapproaches.
2. ReviewMethodology
Weconductedastructuredliteraturesearchandscreeningexercisetoassemblerecent
peer-reviewedworkondeeplearningforborrower-levelcreditriskprediction. Thegoal
isacomprehensiveandtransparentnarrativesynthesisofthefieldratherthanaformal
systematicreviewormeta-analysis.
Tocoverbothcomputingandfinanceoutlets,wesearchedIEEEXplore,Scopus,ACM
Digital Library, ScienceDirect, SpringerLink, Web of Science, and Google Scholar. Web
ofSciencewasincludedtobroadencoverageoffinanceandoperationsresearchvenues
that are not always well represented in engineering-focused indexes. Queries paired
credit-riskterms(e.g.,creditscoring,defaultprediction,probabilityofdefault)withdeep
learningterms(e.g.,CNN,RNN,LSTM,GRU,Transformer,graphneuralnetwork). Where
supported,werestrictedsearchestotitle/abstract/keywordsandrefinedqueryvariants
iterativelyusinghighlycitedseedpaperstolimitirrelevantreturns. Wetargetedjournal
articles and full conference papers from 2015 to 2025, and added foundational earlier
studiesviabackward/forwardcitationtracking.
https://doi.org/10.3390/info17040395

Information2026,17,395 4of28
SearchStrategyandScreeningProtocol
Theinitialsearchidentifiedapproximately380recordsacrossalldatabasesaftermerg-
ingresults. Duplicaterecordswereremovedusingtitle,author,venue,andyearmatching.
Followingde-duplicationandremovalofclearlyout-of-scoperecords,208studieswere
retainedfortitleandabstractscreening,assummarisedinFigure1. Theremainingstudies
werescreenedintwostages: (i)titleandabstractscreening,followedby(ii)full-textassess-
ment. Duringtitleandabstractscreening,studieswereexcludediftheyfocusedexclusively
on market or liquidity risk, macroeconomic default modelling without borrower-level
prediction,ormethodologicaldeeplearningcontributionswithoutanempiricalcreditrisk
application. Full-textscreeningwasthenusedtoconfirmrelevance,extractmethodological
details,andverifythatthestudyaddressedborrower-,facility-,orentity-levelcreditrisk.
Figure1.PRISMAflowchartoftheliteraturesearchandscreeningprocessusedinthissurvey.The
diagramsummarisesdatabasequerying,de-duplication,titleandabstractscreening,andfull-text
eligibilityassessment.
Studieswereincludediftheysatisfiedatleastoneofthefollowingcriteria:(i)proposed
orempiricallyevaluatedadeeplearningarchitectureforcreditriskprediction;(ii)provided
asurveyorstructuredreview ofmachinelearningordeep learningmethodsforcredit
risk;or(iii)addressedinterpretability,fairness,robustness,orgovernanceexplicitlyina
creditriskcontext. Meanwhile,studieswereexcludediftheylackedquantitativeevalu-
ation,providedinsufficientmethodologicaldetailtoassessthelearningarchitecture,or
focusedsolelyonregulatoryorpolicydiscussionwithoutamodellingcomponent. Unlike
systematic reviews, no strict performance-improvement threshold was imposed; how-
ever,studieswererequiredtoreportatleastonestandardevaluationmetrictosupport
empiricalcomparison.
https://doi.org/10.3390/info17040395

Information2026,17,395 5of28
Thefinalcorpuscomprises140deeplearningapplicationstudiesand18surveyor
guidelinepapers. Foreachincludedstudy,werecordedthedatamodality(tabular,sequen-
tial,textual,orrelational),modelarchitecture(MLP,CNN,RNN/LSTM/GRU,Transformer,
GNN,orhybrid),creditproductsegment(consumer,SME,corporate,interbank,ormixed),
predictiontarget,andreportedevaluationmetrics. Wedidnotapplyaformalrisk-of-bias
scoringprotocol(giventhenon-systematicscopeandheterogeneousstudydesigns),butwe
extractedreportingattributesrelevanttointerpretability,validationdesign(e.g.,out-of-time
vsrandomsplits),anddeploymentconsiderationswhereavailable. Theseattributesunder-
pinthetaxonomyusedinSections4and5,andtherelatedsurveyliteratureissummarised
inTable1.
3. OverviewofCreditRiskPredictionandDatasets
Creditriskreferstothepotentiallossthatalenderorinvestorfaceswhenaborrower
failstomeetcontractualfinancialobligations[17]. Accuratecreditriskpredictionisfunda-
mentaltofinancialstability,guidingcapitalallocation,pricing,andprovisioningdecisions
underregulatoryframeworkssuchasBaselIII.Traditionally,creditriskhasbeenassessed
throughstatisticalscorecardsandexpertjudgment;however,theriseofdata-drivenlending
and digital credit platforms has produced large-scale, high-dimensional borrower data
thatdemandmoreadvancedmodellingapproaches. Thissectionprovidesanoverviewof
thekeypredictivetasksincreditriskmanagementandsummarisesbenchmarkdatasets
commonlyemployedinempiricalstudies.
3.1. CreditRiskPredictionTasks
Credit risk prediction aims to estimate the likelihood and magnitude of potential
lossesassociatedwithlendingactivities. Inregulatoryandresearchpractice,threemain
quantitativetasksaretypicallyaddressed:
• ProbabilityofDefault: Thelikelihoodthataborrowerwillfailtomeetcontractual
repaymentobligationswithinaspecifiedhorizon. PDmodellingformsthefoundation
ofmostcreditscoringsystemsandrisk-basedpricingframeworks[28].
• LossGivenDefault(LGD):Theproportionoftheexposurethatisnotrecoveredinthe
eventofdefault,reflectingcollateralvalues,recoveryprocesses,andlegalcosts[29].
• ExposureatDefault(EAD):Thetotaloutstandingamountalenderisexposedtowhen
defaultoccurs,whichisparticularlyimportantforrevolvingfacilitiessuchascredit
cardsandoverdrafts[30].
Acrossthereviewedliterature,PD-styletargets(defaultorcloselyrelateddelinquency
outcomes)dominate,andtheyformtheprimarybasisforcomparingdeeplearningmodel
familiesinthissurvey. Predictionhorizonsandlabeldefinitionsvaryacrossstudiesand
products; where reported, we capture these details in the study summaries to support
consistent interpretation. LGD and EAD are discussed only in studies that explicitly
modelthemusingdeeparchitectures,reflectingtheircomparativelylimitedcoveragein
thedeeplearningcredit-riskliterature. ThesequantitiesdeterminetheExpectedLoss(EL),
acornerstoneofrisk-weightedasset(RWA)calculationinBaselframeworks,definedas:
EL = PD×LGD×EAD. (1)
ThoughELiscrucialincreditrisk,itisinconsistentlyreportedandisnotcomparable
across heterogeneous datasets and horizons in the surveyed studies. Accordingly, the
synthesis in Section 5 focuses on the evaluation metrics most commonly reported for
PD-styleprediction.
https://doi.org/10.3390/info17040395

Information2026,17,395 6of28
3.2. BenchmarkDatasets
Empiricalresearchoncreditriskfrequentlyreliesonbenchmarkdatasetstoevaluate
andcomparemodellingapproaches. Themostwidelyusedpublicdatasetsincludethe
GermanCredit,AustralianCredit,andTaiwanCreditCardDefaultdatasets,whichhave
becomestandardbaselinesforMLalgorithms. TheGermanCreditdataset,compiledby
theUCIMLRepository,contains1000loanapplicantswith20demographicandfinancial
attributeslabeledasgoodorbadcreditrisk[31]. TheAustralianCreditdatasetissmaller,
comprising690recordswithmixedcategoricalandnumericalfeaturesforbinarycredit-
worthinessclassification. TheTaiwanCreditCardDefaultdatasetissubstantiallylarger,
featuring30,000clientswithdetailedbilling,repayment,anddemographicinformation,
andiswidelyusedindeeplearningbenchmarks[32].
Whilethesedatasetsfacilitatereproducibilityandalgorithmiccomparison,theirlim-
itedsamplesizes,staticstructures,andlackoftemporalorbehaviouralfeaturesconstrain
generalisabilitytoreal-worldportfolios[33]. Smallbenchmarksalsocreatehigh-variance
evaluationregimesinwhichapparentperformancedifferencesareunstableandcanbe
driven by a few influential cases rather than a durable risk signal. For example, with
only1000observations,theGermanCreditdatasetcanyieldmateriallydifferentestimates
acrossrandomsplits,andhigh-capacitymodelsmayoverfitidiosyncraticcorrelationsthat
donottransfertonewborrowercohorts. Thiseffectiscompoundedbysample-selection
mechanismsthatareabsentorunobservedinpublicbenchmarks(e.g.,lenderacceptance
policiesandunderwritingrules),meaningtheobservedlabelsmayreflectafilteredsub-
populationratherthanthefullapplicantpool. Consequently,modelstrainedandreported
onsuchdatasetsoftenoverestimateout-of-sampleperformanceandunderstateuncertainty
incomparativeclaims.
Toaddresstheseshortcomings,contemporarystudiesincreasinglyadoptlargerand
more heterogeneous datasets. For example, the Home Credit Default Risk dataset [34]
includes over 300,000 loan applications enriched with demographic, behavioural, and
bureaurecords,representingacloserapproximationtoindustrialsettings. Similarly,the
LendingClubpeer-to-peerlendingdatasetcontainsmillionsoftransactionsandrepayment
records,enablinglarge-scaleevaluationsofensembleanddeeplearningmodels[35].
Despitetheseadvances,muchoftheacademicliteraturecontinuestorelyonsmall,
static benchmarks that fail to capture macroeconomic shifts and dynamic borrower be-
haviour. Bridgingthisgaprequireslongitudinal,multimodaldatasetswithexplicittime
structureandstablelabeldefinitions,sothatmodelscanbeevaluatedunderout-of-timeval-
idationandassessedfordrift,calibrationdecay,andsubgroupperformance. Suchdatasets
areessentialforbenchmarkingemergingdeeplearningarchitecturesunderrealisticand
regulatory-compliantconditions(Table2).
Table2.SummaryofBenchmarkDatasetsCommonlyUsedinCreditRiskPrediction.
Dataset SampleSize Features Description
Demographicandfinancialattributeswithbinary
GermanCredit 1000 20
good/badcreditlabels.
Mixedcategoricalandnumericalfeaturesfor
AustralianCredit 690 14
creditworthinessclassification.
TaiwanCreditCardDefault 30,000 24 Clientpaymenthistory,billingamounts,anddemographics.
Realisticindustrialdatasetcombiningbehaviouraland
HomeCreditDefaultRisk 300,000+ 122
bureauinformation.
Peer-to-peerlendingrecords,includingloan,borrower,and
LendingClub Millions 100+
repaymentdetails.
https://doi.org/10.3390/info17040395

Information2026,17,395 7of28
4. EvolutionofModelsforCreditRisk
Creditriskmodellinghasprogressedfrominterpretablelinearmethodstodeeparchi-
tecturesthatcapturenonlinearinteractions,sequentialbehaviour,andrelationaldependen-
ciesamongborrowers. Thissectionreviewsthemethodologicalevolutionacrossthemain
modelfamilies.
4.1. LogisticRegressionandClassicalMachineLearning
Logistic regression (LR) remains the cornerstone of credit scoring due to its trans-
parencyandregulatoryacceptance[36,37]. Giveninputfeaturesx ∈ Rd andparameters
(w,b),LRmodelstheprobabilityofdefaultas:
1
P(y =1| x) = σ(w ⊤ x+b) = , (2)
1+exp(−w⊤x−b)
whereσ(·)isthelogisticsigmoidandy ∈ {0,1}denotesdefaultstatus. Despiteitssim-
plicity,LRassumesalinearlog-oddsrelationship,limitingitsabilitytocapturenonlinear
featureeffectsandinteractionsinhigh-dimensionaldata. SubsequentclassicalMLmodels,
suchassupportvectormachines,randomforests,andgradientboosting,enhancedflexibil-
itybylearningnonlineardecisionboundaries. ThesemethodstypicallyoutperformLRin
accuracybutatthecostofinterpretability,motivatingsubsequentresearchintomodelsthat
balancebothproperties[5].
4.2. EarlyDeepLearningforTabularCreditRisk
Theintroductionofdeeplearningbroughtneuralarchitecturescapableoflearning
complex,nonlineartransformationsdirectlyfromtabularcreditdata. Unliketraditional
logistic regression (LR), which models linear relationships, deep neural networks can
capturehierarchicalfeatureinteractionsthroughmultiplehiddenlayers. Amulti-layer
perceptron (MLP), illustrated in Figure 2, extends LR by stacking hidden layers with
nonlinearactivationsthatenabletheautomaticextractionoflatentfeaturerepresentations.
Mathematically,theforwardpropagationinanMLPisgivenby:
h (l) = ϕ(W (l) h (l−1)+b (l)), (3)
whereϕ(·)denotesanonlinearactivationfunctionsuchasReLU.Thishierarchicalstructure
allows MLPs to approximate complex functions on large datasets, thereby uncovering
nonlinearrelationshipsbetweenborrowercharacteristicsanddefaultprobabilities[38].
Figure2.Basicstructureofafeed-forwardneuralnetworkusedfortabularcreditdata.Thenetwork
consistsofaninputlayer,oneormorehiddenlayerswithnonlinearactivations,andanoutputlayer
fordefaultprediction.
https://doi.org/10.3390/info17040395

Information2026,17,395
8of28
4.3. SequentialandTemporalBehaviourModelling
Creditworthinessevolvesovertimeasborrowersmakerepayments,accumulatebal-
ances,adjustspendingbehaviour,orexperienceincomefluctuations. Sequentialneural
networksexplicitlymodelthesebehaviouraltrajectoriesbycapturingtemporaldependen-
ciesthatstaticmodelscannot. Thesearchitecturesprocesscredit-relatedsequences—such
asmonthlyrepaymenthistories,rollingutilisationrates,ordelinquencytransitions—ina
step-wisemanner,enablingtheextractionoflong-rangebehaviouralpatterns. Recurrent
neuralnetworks(RNNs)formthefoundationforsequentialmodelling. Ateachtimestept,
anRNNupdatesitshiddenstateaccordingto
|     |     | h   | =tanh(W | h t−1 | +W x +b), |     |     | (4) |
| --- | --- | --- | ------- | ----- | --------- | --- | --- | --- |
|     |     | t   |         | h     | x t       |     |     |     |
wherex istheinputvectorattimet,h isthehiddenstate,W andW arelearnableweight
| t   |     |     |     | t   |     | h   | x   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
matrices,andbisabiasterm. AlthoughRNNscancaptureshort-termtemporalstructure,
theystrugglewithlong-rangedependenciesduetovanishinggradients[39].
4.3.1. LongShort-TermMemoryNetworks
ToaddressthelimitationsofstandardRNNs,longshort-termmemory(LSTM)net-
worksintroducegatingmechanismsthatregulateinformationflowandpreservelong-term
temporalpatterns. TheLSTMarchitecture(Figure3)usesthreegates—forget,input,and
| output—toupdateaninternalmemorycellC |     |     |     | :   |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
t
|     | f =        | σ(W [h   | ,x     | ]+b ),     |     |           |     | (5) |
| --- | ---------- | -------- | ------ | ---------- | --- | --------- | --- | --- |
|     | t          | f        | t−1    | t f        |     |           |     |     |
|     | i t =      | σ(W i [h | t−1 ,x | t ]+b i ), |     |           |     | (6) |
|     | C˜ =tanh(W |          | [h     | ,x ]+b ),  |     |           |     | (7) |
|     | t          |          | c t−1  | t c        |     |           |     |     |
|     | C =        | f ⊙C     | +i     | ⊙C˜        |     |           |     |     |
|     | t          | t        | t−1    | t t ,      |     |           |     | (8) |
|     | o =        | σ(W [h   | t−1 ,x | ]+b ),     | h = | o ⊙tanh(C | ),  | (9) |
|     | t          | o        |        | t o        | t   | t         | t   |     |
Here,thehiddenstateandcellstatearedenotedbyh andC ,respectively,andx isthe
|     |     |     |     |     | t   | t   |     | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
inputvectorattimestept. Thegates f t ,i t ,ando t controlforgetting,updating,andoutput,
| whileC˜ |     |     |     | σ(·)isthesigmoidactivationfunctionand⊙ |     |     |     |     |
| ------- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- |
t denotesthecandidatecellupdate.
denoteselementwisemultiplication[40].
Figure3. ArchitectureoftheLSTMnetworkshowinggatingmechanismsforinput, forget, and
outputregulation.
https://doi.org/10.3390/info17040395

Information2026,17,395
9of28
4.3.2. GatedRecurrentUnitNetworks
Thegatedrecurrentunit(GRU),illustratedinFigure4,simplifiestheLSTMarchitec-
turebyusingasinglestatevariableandtwogates. GRUscomputetheirhiddenstateusing:
|     | z = | σ(W [h | ,x ]+b   | ),  |     | (10) |
| --- | --- | ------ | -------- | --- | --- | ---- |
|     | t   | z      | t−1 t    | z   |     |      |
|     | =   | σ(W [h | ]+b      | ),  |     |      |
|     | r t | r      | t−1 ,x t | r   |     | (11) |
h˜
|     | =tanh(W |      | [r ⊙h   | ,x ]+b | ),  | (12) |
| --- | ------- | ---- | ------- | ------ | --- | ---- |
|     | t       |      | h t t−1 | t      | h   |      |
|     | h =     | (1−z | )⊙h +z  | ⊙h˜    | ,   | (13) |
|     | t       |      | t t−1   | t      | t   |      |
wherex istheinputvectorattimesteptandh istheGRUhiddenstate. Thevectorsz and
| t   |     |     | t   |     |     | t   |
| --- | --- | --- | --- | --- | --- | --- |
r denotetheupdateandresetgates,respectively,andh˜ isthecandidatehiddenstate[39].
| t   |     |     |     |     | t   |     |
| --- | --- | --- | --- | --- | --- | --- |
Figure4. ArchitectureoftheGRUnetwork,highlightingtheupdateandresetgatesthatcontrol
informationflowacrosstimesteps.
4.3.3. TemporalConvolutionalNetworks
Temporalconvolutionalnetworks(TCNs)offeranalternativetorecurrentarchitectures
byapplyingone-dimensionaldilatedconvolutionstocapturelong-rangedependencies
withoutrecursion:
K−1
= ∑
|     |     | h t | W k x | t−d·k , |     | (14) |
| --- | --- | --- | ----- | ------- | --- | ---- |
k=0
whereddenotesthedilationfactorandKthekernelsize[41]. UnlikeRNNsandLSTMs,
TCNs process sequences in parallel, preserving causality through zero-padding while
enablingefficienttrainingonlongtemporalwindows[42,43]. ThispropertymakesTCNs
particularlyvaluableforhigh-frequencyrepaymentdataandreal-timetransactionstreams
whereparallelcomputationandlong-horizonforecastingareadvantageous.
4.4. ConvolutionalandHybridArchitectures
CNNs,thoughhistoricallyassociatedwithimageprocessing,havebecomeeffective
tools for modelling structured financial sequences [44]. In credit risk, one-dimensional
convolutionsslidelearnablefiltersoverborrowerhistories—capturinglocaltemporalpat-
ternssuchasconsecutivedelinquencies,abruptutilisationjumps,orirregularrepayment
intervals. Thesefiltersextractshort-rangebehaviouralmotifswhilesharingparameters
acrosstimesteps,yieldingmodelsthatarebothcomputationallyefficientandlessprone
https://doi.org/10.3390/info17040395

Information2026,17,395 10of28
to overfitting than dense architectures. Figure 5 illustrates this structure, where con-
volutional and pooling layers form hierarchical representations of borrower behaviour
beforeclassification.
Figure5.BasicCNNarchitectureadaptedforone-dimensionalfinancialsequences.Convolutional
andpoolinglayerscapturelocalrepaymentorutilisationpatterns,whicharethenpassedtodense
layersforclassification.
SeveralstudiesreportthatCNN-basedsequenceencodersarecompetitivewithre-
currentarchitecturesincredit-risksequencemodellingwhenlocalbehaviouralpatterns
dominatethesignal,whileofferingfastertrainingduetoparallelism[44,45]. Theirpar-
allelism offers significant speed advantages for large portfolios, and their stable train-
ingdynamicsmakethemwellsuitedforindustrialsettingswhererapidretrainingand
consistentconvergencearerequired. Thishasmotivatedhybridcredit-riskmodelsthat
integrate CNN modules with other deep architectures. Wide–deep networks combine
alinearbranch—reflectingscorecard-styleinterpretability—withnonlineardeepcompo-
nents that capture higher-order interactions. Other hybrids, such as CNN–LSTM and
CNN–Transformermodels,leverageconvolutionstoencodeshort-termbehaviourbefore
passingfeaturestorecurrentorattention-basedlayerstocapturelong-rangedependen-
cies. These designs offer a practical balance between interpretability, expressive capac-
ity, and computational scalability, making them increasingly relevant in modern credit
riskpipelines.
4.5. Transformer
Transformerarchitecturesintroduceafundamentallydifferentapproachtomodelling
sequenceandtabularcreditdatabyreplacingrecurrencewithself-attention,enablingthe
captureofglobaldependenciesinparallelratherthanstepwise[46]. Insteadofprocessing
borrowerhistorieschronologically,asRNNsdo,thetransformercomputespairwiseinter-
actionsacrossallfeaturedimensionsortimestepssimultaneously. Thecoreself-attention
mechanismisdefinedas:
(cid:32) (cid:33)
QK⊤
Attention(Q,K,V) =softmax √ V, (15)
d
k
https://doi.org/10.3390/info17040395

Information2026,17,395 11of28
whereQ,K,andVdenotethequery,key,andvaluematricesrepresentinglatentprojections
of input features or time steps, and d is a scaling constant to stabilise gradients. This
k
formulation enables the model to assign adaptive relevance weights across the entire
behaviouralsequence,allowingittocapturelong-rangedelinquencysignatures,cyclical
utilisationtrends,andcross-featureinteractionsthattraditionalrecurrentnetworksstruggle
toretain.
Recentadaptationsdemonstratehowtransformerscanberepurposedfromnatural
languageprocessingtostructuredfinanciallearning. TabTransformer[47]contextualises
categoricalembeddings,improvingdiscriminationontabularcreditdatasetswithhigh-
cardinalitysocio-economicattributes.
4.6. GraphNeuralNetworks
Borrowers often participate in interdependent financial ecosystems through co-
applicantties,sharedemployers,guarantorstructures,fund-flowrelationships,orsupply-
chain linkages. These relational patterns give rise to correlated credit exposures and
potential contagion pathways that cannot be represented in i.i.d. tabular data. Graph
neuralnetworks(GNNs)modelsuchrelationaldependenciesviaiterativemessagepassing,
whereeachnodeupdatesitsrepresentationbyaggregatingtransformedmessagesfrom
neighbouringnodes. Thegenericupdateruleforamessage-passinglayerisexpressedas
 
h (
v
l+1) = σ ∑ 1 W (l) h (
u
l) , (16)
c
u∈N(v) vu
whereh
(l)
istheembeddingofborrowervatlayerl,N(v)denotesneighbouringnodes(e.g.,
v
borrowers,firms,accounts,orcounterpartiesconnectedthroughownership,transactions,
orcontractualties),c isanormalisationcoefficient(e.g.,nodedegree),W(l) isalearnable
vu
weight transform, and σ(·) is a nonlinear activation. Figure 6 visualises this pipeline:
neighbours send learned messages, the messages are pooled, and the central borrower
embeddingisupdatedtoreflectrelationalcreditriskfactors.
Figure6.MessagepassingmechanisminaGNNforborrowernetworks.Neighbouringborrower
representationsarecollected,aggregated,andusedtoupdateeachnode,enablingpropagationof
financialinfluencesignals.
Table3summarisesthevariousDLarchitecturesforcreditriskmodelling.
https://doi.org/10.3390/info17040395

Information2026,17,395
12of28
Table3.Summaryofdeeplearningarchitecturesdiscussedforcreditriskmodelling.
ModelClass InputModality CoreMechanism Credit-RiskStrengths KeyLimitations
Learnscomplex
Notemporalorrelational
|     |                 | Feed-forwardnon-linear | interactionsbeyond        |                   |
| --- | --------------- | ---------------------- | ------------------------- | ----------------- |
| MLP | Tabularfeatures |                        |                           | reasoning;feature |
|     |                 | transformation         | linearscorecards;scalable |                   |
engineeringrequired
andeasytodeploy
Capturesonlylocal
Detectsrepaymentand
|     | Sequential/behavioural | Localshared-weight      |                             | temporalpatterns;       |
| --- | ---------------------- | ----------------------- | --------------------------- | ----------------------- |
| CNN |                        |                         | utilisationmotifs;efficient |                         |
|     | time-series            | convolutionswithpooling |                             | struggleswithlong-range |
trainingandparallelisable
dependencies
|     |     |     | Modelslong-term | Trainingcostincreases |
| --- | --- | --- | --------------- | --------------------- |
RecurrentModels(RNN, Temporalbehavioural Hiddenstatepropagation delinquency,repayment withlongsequences;
LSTM,GRU) sequences withgating evolution,and vanishinggradients;
|     |     |     | behaviouraldrift | limitedparallelism |
| --- | --- | --- | ---------------- | ------------------ |
Capturesglobal
|     |     | Globalmulti-head | temporal/feature | Requireslargerdata |
| --- | --- | ---------------- | ---------------- | ------------------ |
Transformers Tabularorsequentialdata self-attention,contextual interactions;scalable volumeandtuning;less
|     |     | embeddings | training;interpretability | effectiveontinydatasets |
| --- | --- | ---------- | ------------------------- | ----------------------- |
viaattention
|     |     | Iterativemessagepassing | Modelscontagioneffects, | Requiresgraph |
| --- | --- | ----------------------- | ----------------------- | ------------- |
Relationalborrower systemicdependencies, construction;sensitiveto
| GNNs |          | andneighbour |               |                 |
| ---- | -------- | ------------ | ------------- | --------------- |
|      | networks |              | andhiddenrisk | noiseandmissing |
aggregation
|     |     |     | propagation | relationships |
| --- | --- | --- | ----------- | ------------- |
Balancesinterpretability,
Heterogeneousdata Combinedfeature scalability,and Increasedcomplexity;
HybridArchitectures(e.g.,
(tabular,text,sequence, extractorsandfusion multimodallearning; hardertointerpretand
CNN–LSTM)
|     | network) | layers | strongestperformanceon | validateforregulation |
| --- | -------- | ------ | ---------------------- | --------------------- |
real-worlddata
5. NotableDLApplicationsinPeer-ReviewedCreditRiskStudies
Thissectionsynthesisespeer-reviewedapplicationsofdeeplearningtocreditrisk. We
mapempiricalstudiestothesamethreeaxes: modality,architecture,andobjective,and
reporttheevaluationmetricstheyusedandthequantitativeperformanceobtained.
5.1. TabularDeepNetworksforCreditRisk
Deep learning for tabular borrower data has evolved from simple multilayer per-
ceptrons(MLPs)tospecialisedarchitecturesthatleverageregularisation, attention, em-
beddings, and hybrid ensembling. This subsection reviews representative studies that
applydeeptabularmodelstocorporate,retail,andinstitutionallendingdata,highlighting
methodologicalcontributions,empiricalfindings,andcomparativeperformancerelativeto
conventionalMLmodels.
Yangetal.[48]proposedahigh-dimensionaldeepneuralnetwork(HDNN)forcorpo-
ratecreditriskusingsupply-chainaugmentedfinancialdata. Theirmodelincorporated
combined L1–L2 penalties to address feature sparsity and batch-normalisation effects,
achievinganaccuracyof80.12%,outperforminglogisticregression(areaunderthereceiver
operatingcharacteristiccurve(AUC)=0.717),supportvectormachines(AUC=0.738),and
astandardneuralnetworkbaseline(AUC=0.692). Linetal.[49]introducedapenalised
deepneuralnetwork(PDNN)basedonsurvivalmodelling,embeddingaone-to-onepe-
nalisationlayerthatsupportedvariableselectionalongsidetime-to-defaultestimationon
peer-to-peerlendingdata,consistentlyoutperformingnon-penaliseddeepvariants.
Recentstudieshavefurtherexaminedinterpretabilityandprofit-awareoptimisation
withindeeptabularlearning. Asenciosetal.[50]comparedMLP,XGBoost,andTabNet
on36,402Peruviancooperative-lendingapplicationsusingregression-basedprofitscor-
ing. XGBoost achieved the best results (R2 = 0.7906), although TabNet (R2 = 0.7465)
offeredmoretransparentfeature-levelinterpretabilitythroughattentiveembeddings. In
large-scalesettings,WangandZhang[51]proposedaTabNet-Stackingensemblethatinte-
https://doi.org/10.3390/info17040395

Information2026,17,395 13of28
gratedTabNet,XGBoost,LightGBM,CatBoost,SVM,andKNN,reachingaccuracy=0.979,
recall=0.856,F1=0.817,andAUC=0.941ontheTianchidataset(≈800,000cases),sub-
stantiallyoutperformingsingle-modelbaselines.
Beyondarchitecturedesign,explainabilityhasbecomecentraltotabulardeeplearning
deployment. Hjelkrem and de Lange [52] trained an MLP using open banking transac-
tiondataandcompareditwithabidirectionalencoderrepresentationsfromtransformers
(BERT)-basedmodel,reportingthattheMLPachievedsuperiorpredictiveperformance
whilemaintainingpracticalexplainabilityusingSHAPattributionvisualisations. Their
resultsshowedthatSHAPdetectedintuitivebehaviouralriskfactors,supportingsuitability
forregulatedfinancialsettings. Lietal.[53]introducedanincrementalDNN(I-DNN)for
borrowercreditscoringonagriculturalmicroloanrecords(22,475examples),demonstrat-
ingAUCimprovementsrangingbetween1.4%and7.8%comparedwithstandardDNN,
XGBoost,andrandomforestbaselinesunderconceptdriftscenarios.
Advancesindeeptabularmodellinghavealsoexploredensemble-drivengeneralisa-
tion. Popovetal.[54]introducedNeuralObliviousDecisionEnsembles(NODE),replacing
discrete tree splits with differentiable soft-gating, producing competitive performance
withgradientboostingwhileenhancingdifferentiabilityandcalibrationunderstochastic
optimisation. Buildingonensemblereasoning,ShanandGao[55]proposedanenhanced
TabNetstackingmodelforSMEsupply-chainfinancialriskpredictionusingmulti-stage
optimisation, achievingAUC=0.9616andAccuracy=0.9277, outperformingstandard
TabNet,LightGBM,andCatBoostbaselines.
TheseworksdemonstratethattabularDLhasadvancedfromsimplefeed-forwardnet-
workstowardarchitecturesthatintegrateregularization,attention,andensemblelearning.
Overall,thesestudiessuggestthatdeeptabularmodelsareoftencompetitivewithstrong
tree-based ensembles on larger datasets, particularly when the feature space includes
high-cardinality categorical variables, complex interactions, or multimodal extensions
that benefit from representation learning. On smaller benchmarks, reported gains are
frequently modest and can be sensitive to split design and tuning, meaning gradient
boostingremainsastrongandfrequentlyhard-to-beatbaseline. Deepnetworkstherefore
complementratherthanreplaceclassicalmethods,withtheirmainadvantagearisingwhen
datascale,heterogeneity,orunifiedmultimodalpipelinesjustifytheaddedmodellingand
operationalcomplexity.
5.2. SequentialModelsandEvent–TimeTargets
Sequentialdeeplearningapproachesmodeltheevolutionofborrowerorportfolio
behaviour over time, offering substantial advantages over static classifiers that ignore
risktrajectories. Thesemodelscapturetemporalpatternslinkedtorepaymentbehaviour,
behaviouraldrifts,cyclicalspending,macroeconomicshocks,andpost-originationdelin-
quency paths. Compared with conventional panel regression and tree-based models,
sequential architectures integrate information across ordered observations and enable
dynamicprobability-of-defaultestimationratherthanstatic,single-pointpredictions.
Liang and Cai [56] applied long short-term memory (LSTM) networks to forecast
monthlydefaultratesontheLendingClubpeer-to-peerplatform. TheLSTMconsistently
outperformedARIMA,SVM,andANNacrossmultiplecross-validationschemes,reducing
MAE from 0.095 to 0.072 and RMSE from 0.119 to 0.093. Further support for recurrent
credit modelling appears in Ala’raj et al. [57], who developed two behavioural LSTM
variants(MP–LSTMandPE–LSTM)forrealretailbankingcreditcardcustomers. Their
modelssurpassedSVM,RF,MLP,andLRbaselinesacrosspredictiveandcalibrationmetrics,
demonstratingthattemporalrepresentationlearningenhancesbehaviouraldefaultscoring
inoperationalsettings.
https://doi.org/10.3390/info17040395

Information2026,17,395 14of28
Beyond standard LSTMs, hybrid deep temporal architectures have gained promi-
nence. Zhang [58] proposed a CNN–LSTM attention model for enterprise credit risk,
achieving AUC = 0.92 and F1 = 0.91, outperforming CNN- and LSTM-only baselines.
Lietal.[59]extendedthisapproachforlistedcorporateriskandreportedthatCNNlayers
effectivelyextractshort-termtemporalmotifs,whileLSTMcomponentsencodelongerbe-
haviouraltransitions,confirmingthathierarchicaltemporalmodellingimprovesenterprise
creditdiscrimination.
Survival-drivenarchitecturesfurthergeneralisetemporalcreditmodellingbyestimat-
inghazardratherthanstaticoutcomes. Wangetal.[60]implementedadeepdiscrete-time
survivalmodelthatdecomposescreditoutcomesintoage,period,andcohortdimensions,
generatinginterpretablehazardcurveswithasmoothertemporalstructurethanclassical
econometric approaches. Chen and Long [61] similarly advanced temporal modelling
throughaself-attention-basedend-to-endcorporatecreditratingframework, whichre-
movedtheneedformanualfeatureaggregationandimprovedratingclassificationstability
relativetotraditionalMLcompetitors.
More recent developments incorporate fusion and cross-feature interaction within
sequential networks. Han et al. [62] introduced a default-prediction framework com-
bining self-attention with a cross-network mechanism, demonstrating that modelling
interactivetemporaldependenciesyieldshigheraccuracy,precision,recall,andF1-score
relativetostandarddeeplearningarchitectures. Shietal.[63]alsobenchmarkedCNN,
RNN, and DNN models in financial-sector credit scoring and observed that recurrent
architecturesmaintainedsuperiortemporalsensitivity,whileCNNsprovidedparameter
efficiencybenefits.
Bidirectional and residual-enhanced architectures have been explored to stabilise
recurrenttrainingandpreservelong-rangegradients. Yangetal.[64]introducedaresidual-
enhancedbidirectionallongshort-termmemory(BiLSTM)frameworkincorporatingmulti-
headattention,achievingAUC=0.982andF1=0.958ontheFreddieMacSingle-Family
dataset,outperformingBiLSTM,GRU,CNN,andRNNbaselines. Complementaryresearch
explorescouplingsequentialencoderswithprobabilisticreasoning: Zhang[65]integrated
LSTMencoderswithBayesiancalibrationmodules,achievingAUC=0.981andreducing
uncertaintymiscalibrationrelativetoRFandLRbaselines.
Theseresultsindicatethatsequentialarchitecturesaremostvaluablewhenlenders
possessrichpost-originationhistoriesorportfolio-leveltimeseriesandcareabouthowrisk
evolves,notjustwhetheraborrowereventuallydefaults. LSTM-andGRU-likemodels
offer clear gains for dynamic behavioural scoring and vintage-level forecasting, while
CNN–LSTM hybrids and survival-based networks help bridge the gap between point
predictionsandtime-to-eventoutcomes. However,theempiricalliftoverstrongtabular
baselines tends to appear only when sequences are sufficiently long and informative;
on static benchmarks with limited behavioural content, sequential models mainly add
complexitywithoutdeliveringcommensuratepracticalbenefit.
5.3. Transformer-BasedModelsforCreditRisk
Transformersrepresentamajordeparturefromrecurrentarchitecturesbyreplacing
sequentialrecurrencewithself-attention,enablingparallelcomputationandglobaldepen-
dencymodellingacrossfeatures,timesteps,ormodalities[46]. Thekeymechanism,scaled
dot-productattention,allowseachelementinasequenceorfeaturevectortoconditionon
allothers,overcominglong-termdependencylimitationstypicalofLSTMsandGRUs. This
propertyisattractiveincreditmodelling,wherebehaviouralvariables,categoricalfeatures,
andtext-basedsignalsinteractincomplex,non-localpatterns.
https://doi.org/10.3390/info17040395

Information2026,17,395 15of28
Earlyadoptionhasfocusedonadaptingthetransformerencodertotabularandbe-
havioural credit data. Huang et al. [47] introduced the TabTransformer, demonstrating
performancegainsonhigh-cardinalitycategoricalfinancialdatasetsbyreplacingconven-
tionalone-hotencodingswithcontextualembeddings. Gorishniyetal.[66]laterimproved
architectural efficiency with the FT-Transformer, showing that attention-based tabular
modelscanbecompetitivewithstrongtree-ensemblebaselinessuchasCatBoostandXG-
Boost on several tabular tasks, particularly when feature interactions are complex and
heterogeneouslydistributed. WangandXiao[67]extendedthisparadigmbyembedding
behaviouralsequencesalongsidestaticfeatures,achievingAUC=0.72andKS=0.32onan
onlinelendingdataset,outperformingbothLSTMandXGBoostbaselines.
Recentworkhasstartedtospecialisetransformerarchitecturesfordifferentsegments
ofthecreditmarket. Korangietal.[68]framedmid-capcorporatedefaultpredictionas
amulti-labelpanelclassificationtask,usingatransformertolearnthetermstructureof
defaultprobabilitiesoverhorizonsfromafewmonthstothreeyears. Theirmulti-channel
designingestsaccounting,pricing,andmarketvariablesandappliesatask-specificlossfor
multi-horizondefaultprediction,yieldingsizeableAUCimprovementsovertraditional
statisticalandLSTM-basedbenchmarks. Lietal.[69]proposedHFTCRNet,ahierarchical
fusiontransformerforinterbankcreditratingandsystemicriskassessment. Themodel
combines a long-term temporal transformer for bank growth trajectories, a short-term
cross-graph transformer for dynamic interbank exposures, and an attentive contagion
module,trainedinasemi-supervisedfashionusingbothcreditratingsandSRISKlabels.
Onadatasetof4548bankswithquarterlybalancesheetsandnetworkdata,HFTCRNet
outperformeddeepandnon-deepbaselinesinratingaccuracywhilealsocapturingsystemic
riskpatternsintheinterbanknetwork.
In the retail and SME space, transformer-based models have been applied to both
tabularandsequentialcreditsignals. Kakadiyaetal.[70]investigatedtransformerarchi-
tectures for bank loan default prediction and reported performance gains over logistic
regressionandtree-basedmethods,arguingthatself-attentioncaptureshigher-orderde-
pendenciesamongfinancialvariablesthataremissedbyconventionalmodels. Zhangand
Liang[71]proposedaminimumweightedvalueerrorcombinationmodelthatintegratesa
BERT-basedtransformerfortemporalfeatureswithDNNandMLPcomponentsforstatic,
non-sequentialattributes. Featuresarefirstselectedusingchi-squaretestsandgradient
boostingdecisiontrees,andthefinalpredictionisobtainedbydynamicallyweightingthe
sequenceandnon-sequenceexpertsaccordingtoanimprovedminimumweightederror
criterion. Experimentsonpersonalcreditdatashowedthatthecombinedmodelachieves
higherclassificationaccuracythananyindividualtransformerorfeed-forwardbaseline.
Addressing class imbalance and transparency, Hartomo et al. [72] introduced a
weighted-lossTabTransformerwithintegratedexplainableAIforMSMEandconsumer
creditdatasets. Usingcost-sensitiveweighting,theirmodelimprovedaccuracyontheBI-
SAIDandGermanCreditdatasetsfrom86.35%to89.27%andfrom93%to95%,respectively,
whilealsoboostingminority-classAUCandprecision–recall. SHAP-basedexplanations
highlightedeconomicallymeaningfuldriverssuchasfinancingneedsandcreditamount,
illustrating how attention-based tabular models can be combined with explainable AI
(XAI)tosupportmoreaccountabledecision-making. Wu[73]developedaBiLSTM-fused
transformerforenterprisefinancialriskidentificationwithinablockchain-basedfinancial
sharingplatform. Themodeljointlyprocessestextualandvisualfinancialinformationto
classifyfirmsintofiverisklevelsand,inexperiments,achievedriskidentificationaccuracy
above94%withAUCexceeding0.95,outperformingbaselineRNNswhileoperatingon
securelysharedfinancialrecords.
https://doi.org/10.3390/info17040395

Information2026,17,395 16of28
Textualtransformershavealsogainedprominencewhereloanassessments, credit
memos,andSMEnarrativesremainhuman-authored. Stevensonetal.[74]showedthat
BERT-derivedembeddingsfromlender-writtendocumentsproducedcompetitivedefault
prediction results without structured data. Lu et al. [75] extended BERT embeddings
into a hybrid architecture with residual blocks to fuse textual and numeric signals for
corporatecredit. Thistrendalignswithregulatoryinterestinleveragingunstructuredand
semi-structureddisclosuresratherthanpurelytabularindicators.
A frontier research area involves transformer robustness, adversarial safety, and
regulatoryalignment. SchwabandKriebel[76]demonstratedthattransformerencoders
canbesensitivetoadversarialperturbationsandproposedgradient-basedregularisation
defenses. Giventhatfinancialsystemsarehighlysensitivetostabilityandfairness,future
deploymentsoftransformersmustincorporatecalibrationdiagnostics,imbalance-aware
lossfunctions,explainabilitytooling,andcontext-awareadversarialsafeguards.
Therecentcontributionsindicatethattransformersaremovingfromexperimental
architecturestopracticalcandidatesforlarge-scale,multimodal,andsystem-levelcreditrisk
models. Theirmainadvantageliesnotonlyinpredictiveliftbutalsointheirabilitytounify
behaviouralsequences,categoricalembeddings,textualnarratives,interbanknetworks,
andgraph-structuredrelationshipswithinasinglemodellinginterface,whileincreasingly
accommodatingclassimbalance,interpretability,andsystemicriskconsiderations.
The emerging evidence suggests that transformers are most promising in settings
where credit risk depends on high-dimensional, heterogeneous, or multimodal signals
thatinteractinnon-localways. Self-attentionisparticularlyeffectivewhenmodellingthe
jointinfluenceoflongrepaymenthistories,bureauortransactionaltext,andrichcategor-
icalattributes,anditenablesasinglearchitecturetooperateacrossthesemodalities. At
thesametime,transformerstypicallyrequirelargertrainingdatasets,moreparameters,
andlongertrainingtimesthanconventionalmodels,andthenumberoftrulylarge-scale,
production-gradecreditstudiesisstillsmall. Inpractice,theyshouldbeviewedascandi-
datesforportfolioswithabundantdataandcomplexinteractions,ratherthanasdrop-in
replacementsfortreeensemblesorrecurrentnetworksonsmalltabulardatasets.
5.4. GraphNeuralNetworksforRelationalCreditRisk
Graphneuralnetworks(GNNs)havegainedsignificanttractionforcreditriskpredic-
tionduetotheirabilitytoencoderelationaldependenciesthatconventionaltabularand
sequentialmodelsignore. Borrowersinteractwithinrichfinancialecosystemsinvolving
co-application, ownership links, shared directorship, supplier–customer contracts, and
transactionflows,makingrelationallearninganaturalextensiontodeepcreditscoring.
Unlikefeed-forwardorrecurrentarchitecturesthatassumeindependentrecords,GNNs
performiterativemessagepassing, enablingrepresentationlearningthatcapturesboth
directandindirectriskpropagationacrossfinancialnetworks.
Wangetal.[77]constructsmallandmediumenterprise(SME)relationalgraphsusing
shareddirectorandbusiness-interactioninformationandapplyarelationalgraphattention
network(RGAT)fordefaultprediction. Theirinductivetestingprotocolshowsthatgraph
baselinessuchasgraphconvolutionalnetwork(GCN),graphattentionnetwork(GAT),and
relationalGCN(RGCN)outperformnon-graphmodels,withRGATachievingAUC=0.797
andKS=0.457,whileamulti-headextensionreachesAUC=0.799andKS=0.528. The
resultsdemonstratethatrelationalsignalsremainpredictiveevenwithouttransactional
features. Similarly, Song et al. [78] proposed the multi-structure cascaded GNN (MS-
CGNN),integratingpairwisegraphswithheterogeneoushypergraphstructurestomodel
higher-orderinteractions. ThemethodachievedRecall=0.8863,Accuracy=0.9442,and
https://doi.org/10.3390/info17040395

Information2026,17,395 17of28
F1-score=0.9300,outperformingseveralGNNbaselinesandconfirmingthatmulti-level
topologystrengthensriskrepresentation.
Temporalandbehaviouraldynamicshavealsobeenincorporatedintographmod-
elling. Yuanetal.[79]introduceDGNN-SR,whichfusesstaticfund-transfergraphswith
dynamicuser–merchantpaymentgraphsusingmulti-viewtimeencoders. Experimentson
Tencentdatasetscontainingmorethan2.8Mnodesand200MedgesshowAUCimprove-
ments between 0.85% and 2.5% over the best continuous-time GNN baselines. From a
supply-chainfinancingperspective,Mojdehietal.[80]combinetopologicaldataanalysis
withGNNs(BM–GNN),attainingmaximumaccuracyof93.56%acrossmultiplescenarios
whileconsistentlyoutperformingclassicalMLmodelsinstabilityandrobustness,despite
similarpoint-estimateaccuracyonsomesubsets.
Recentworkhasemphasisedhigher-ordergraphstructures, regulatoryalignment,
and training stability. Wang et al. [81] proposed a motif-preserving GNN with curricu-
lumlearningtocapturesubgraphpatternsfrequentlyobservedinenterprisenetworks,
demonstratingimprovedperformanceacrossonepublicandtwoindustrialdatasets. The
curriculumdesignhelpedmitigateconvergenceinstabilityarisingfromnoisyrelational
substructures.Inanotherdirection,Liuetal.[82]constructedenterprisecreditgraphsusing
amaximumspanningtreederivedfrom29financialindicatorsandappliedGraphSAGE
tomulti-levelcreditgrading. TheirresultsconfirmedhigherROCvaluesthantree-based
and neural baselines, despite using a sparse graph, highlighting the value of relational
inductivebiaseveninlimited-connectivitysettings.
Scalabilityhasbecomeacoreevaluationcriterionforreal-worlddeployment. Zhang
et al. [83] developed a large-scale industrial GNN pipeline comprising 23.4M nodes
for supply-chain mining and 8.6M nodes for default prediction. Their model achieved
AUC=0.995 on supply-chain tie mining and 0.701 on loan-default prediction, outper-
formingstaticgraph-learningcompetitorsanddemonstratingthatGNNscanoperateat
web-scalefornationalcreditinfrastructure. Furthermore,ChengandLuo[84]proposea
metapath-drivenriskcontagionGNN(RCGNN)usingheterogeneouspaths(investment,
geography, and industry), reporting superior performance to homogeneous GNNs for
enterprisecreditclassification,althoughdetailedmetricswerenotpublished.
Overall,GNN-basedcreditmodelsaremostcompellingwhenrelationalstructureis
intrinsictotheriskproblem,suchasSMEsupplychains,interbankexposures,enterprise
ownershipnetworks,orfund-transfergraphs. Intheseenvironments,messagepassing
capturescontagionandcorrelatedriskthattabularorsequentialmodelsarestructurally
unable to represent, and the empirical studies show consistent gains in discrimination
and stability under sparse or noisy features. The trade-off is engineering complexity:
constructing,maintaining,andgoverninglarge-scalefinancialgraphsisnon-trivial,and
themarginalbenefitofGNNsislimitedwhenrelationalinformationisweakorunavailable.
Consequently, GNNs are best viewed as targeted tools for systemically interconnected
portfoliosratherthanasuniversalreplacementsforborrower-levelscorecards.
Table4consolidatesthepeer-revieweddeeplearningapplicationsdiscussedinthis
section, grouped by model family for readability and direct linkage to the preceding
subsections. Reportedmetricsandvaluesarereproducedasstatedinthesourcestudies
andarenotstandardisedacrossdatasets,targets,horizons,orlabeldefinitions,whichlimits
directcross-papercomparability.
https://doi.org/10.3390/info17040395

Information2026,17,395
18of28
Table4.Summaryofdeeplearningapplicationsincreditriskprediction.
| ModellingFocus | Reference | Year MethodsandApplication |
| -------------- | --------- | -------------------------- |
NODEdifferentiabletreeensembles;matchgradient
TabularDLModels Popovetal.[54] 2019 boostingoncredit-styletabulartaskswhileremaining
fullydifferentiable.
PenalisedDNNsurvivalmodelforP2Ptime-to-default;
Linetal.[49] 2022 embeddedpenaltiessupportfeatureselectionandimprove
PDestimation.
HDNNwithL1–L2regularisationforcorporatecredit;
|     | Yangetal.[48] | 2023 |
| --- | ------------- | ---- |
Acc=80.12%andoutperformsLR,SVM,andbaselineDNN.
MLP,XGBoost,andTabNetforprofitscoring;XGBoostbest
|     | Asenciosetal.[50] | 2023 |
| --- | ----------------- | ---- |
R2 =0.7906,TabNetslightlylowerbutmoreinterpretable.
Hjelkremand MLPonopen-bankingtransactionswithSHAP;outperforms
2023
Lange[52] aBERTmodelandyieldsintuitivebehaviouralriskdrivers.
IncrementalDNNforagriculturalmicroloansunderconcept
|     | Lietal.[53] | 2023 |
| --- | ----------- | ---- |
drift;1.4–7.8ppAUCgainsoverDNN,XGBoost,andRF.
Wangand TabNet–stackingensembleonlarge-scalecredit;Acc=0.979,
2024
|     | Zhang[51] | AUC=0.941onTianchi. |
| --- | --------- | ------------------- |
StackedTabNetwithmulti-stageoptimisationforSME
ShanandGao[55] 2025 supply-chainrisk;AUC=0.9616,Acc=0.9277,above
TabNet,LightGBM,andCatBoost.
LSTMforLendingClubmonthlydefault-rateforecasts;MAE
| SequentialModels | LiangandCai[56] | 2020 |
| ---------------- | --------------- | ---- |
0.072andRMSE0.093,betterthanARIMA,SVM,andANN.
Self-attentionend-to-endcorporaterating;removesmanual
|     | ChenandLong[61] | 2020 |
| --- | --------------- | ---- |
aggregationandstabilisesratingsvsclassicalML.
BehaviouralLSTMvariantsforcreditcards;exceedSVM,RF,
|     | Ala’rajetal.[57] | 2022 |
| --- | ---------------- | ---- |
MLP,andLRinPDpredictionandcalibration.
CNN–LSTM–attentionforenterprisecredit;AUC=0.92and
|     | Zhang[58] | 2022 |
| --- | --------- | ---- |
F1=0.91,outperformingCNN-onlyandLSTM-onlymodels.
CNN–LSTMforlistedcorporates;CNNcapturesshort-term
|     | Lietal.[59] | 2023 motifs,LSTMlong-termbehaviour,improving |
| --- | ----------- | -------------------------------------------- |
discrimination.
Deepdiscrete-timesurvivalwithage–period–cohort
Wangetal.[60] 2024 decomposition;yieldssmoothcredithazardcurvesand
macro/maturitystructure.
Self-attentionpluscross-networkfordefaultprediction;
Hanetal.[62] 2024 improvesaccuracy,precision,recall,andF1over
baselineDL.
BenchmarkofCNN,RNN,andDNNforfinancialcredit
|     | Shietal.[63] | 2025 scoring;RNNbesttemporalsensitivity,CNNmost |
| --- | ------------ | ----------------------------------------------- |
parameter-efficient.
Residual-enhancedBiLSTMwithmulti-headattentionon
Yangetal.[64] 2025 FreddieMacdata;AUC=0.982,F1=0.958,beatingBiLSTM,
GRU,CNN,andRNN.
LSTMencoderswithBayesiancalibrationforcorporaterisk;
|     | Zhang[65] | 2025 Acc=0.972,AUC=0.981andreduceduncertainty |
| --- | --------- | --------------------------------------------- |
miscalibrationvsRFandLR.
TabTransformerwithcontextualembeddingsfor
Transformer-Based
Huangetal.[47] 2020 high-cardinalitycategoricalfeatures;improvesoverMLP
Models
andtreebaselines.
FT-Transformerfortabulardata;attentionblocksmatchor
|     | Gorishniyetal.[66] | 2021 |
| --- | ------------------ | ---- |
surpassCatBoost/XGBoostonnonlinearfinancialtasks.
BERTembeddingsfromSMEloantexts;textalonegives
|     | Stevensonetal.[74] | 2021 |
| --- | ------------------ | ---- |
competitivedefaultpredictionwithoutstructuredvariables.
https://doi.org/10.3390/info17040395

Information2026,17,395 19of28
Table4.Cont.
ModellingFocus Reference Year MethodsandApplication
Feature-embeddedtransformerfusingbehavioural
Transformer-Based
WangandXiao[67] 2022 sequencesandstaticfeaturesforonlinelending;AUC=0.72,
Models
KS=0.32,betterthanLR,XGBoost,andLSTM.
Transformerformid-capcorporatemulti-horizondefault;
Korangietal.[68] 2023 multi-channelpaneldesignyieldshigherAUCthan
statisticalandLSTMbaselines.
HFTCRNethierarchicalfusiontransformerforinterbank
ratingsandsystemicrisk;temporal+graphtransformers
Lietal.[69] 2024
andcontagionmoduleoutperformothermodelson
4548banks.
Transformermodelsforbankloandefault;self-attention
Kakadiyaetal.[70] 2024 captureshigher-orderinteractionsandbeatsLRand
treeensembles.
BiLSTM-Transformeronablockchainfinancialsharing
Wu[73] 2024 platform;multimodaltext/visualenterpriserisk
identificationwithAcc>94%andAUC>0.95.
Weighted-lossTabTransformerwithSHAP-basedXAIfor
Hartomoetal.[72] 2025 imbalancedMSMEandconsumercredit;increasesaccuracy
andminority-classAUC/PR(e.g.,86.35%→89.27%).
MinimumweightedvalueerrorcombinationofBERT-based
Zhangand temporalencoderandDNN/MLPexperts;dynamic
2025
Liang[71] weightingimprovespersonalcreditclassificationvssingle
models.
BERTplusresidualblockstofusetextualandnumeric
Luetal.[75] 2025 signalsforcorporatecredit;improvesclassificationvs.
single-modalityandnon-residualbaselines.
Analysisoftransformerrobustnessinfinancialtasks;shows
Schwaband
2025 adversarialsensitivityandproposes
Kriebel[76]
gradient-regulariseddefences.
Motif-preservingGNNwithcurriculumlearningfor
GNN-basedModels Wangetal.[81] 2023 enterprisenetworks;improvesaccuracyandconvergence
stabilityacrosspublicandindustrialdatasets.
RGATonSMEgraphsfromshareddirectorsand
Wangetal.[77] 2024 interactions;multi-headRGATachievesAUC=0.799and
KS=0.528,abovenon-graphbaselines.
MS-CGNNcombiningpairwisegraphsandhypergraphs;
Songetal.[78] 2024 Recall=0.8863,Acc=0.9442,F1=0.93,outperforming
severalGNNvariants.
GraphSAGEonmaximum-spanning-treeenterprisecredit
Liuetal.[82] 2024 graphs;higherROCthantreeandneuralbaselinesdespite
sparseconnectivity.
DGNN-SRfusingstaticfund-transferanddynamicpayment
Yuanetal.[79] 2025 graphswithmulti-viewtimeencoders;gains0.85–2.5pp
AUCovercontinuous-timeGNNs.
BM–GNNusingtopologicaldataanalysisandGNNsfor
Mojdehietal.[80] 2025 supply-chainfinance;maxAcc=93.56%withrobust
performancevsclassicalML.
Large-scaleindustrialGNNpipeline(23.4Mand8.6M
Zhangetal.[83] 2025 nodes)forsupply-chainmininganddefault;AUC=0.995
(links)and0.701(default).
Metapath-drivenRCGNNusingheterogeneouspaths
ChengandLuo[84] 2025 (investment,geography,industry);improvesmulti-class
enterprisecreditclassificationvs. homogeneousGNNs.
https://doi.org/10.3390/info17040395

Information2026,17,395 20of28
6. Challenges,Limitations,andFutureResearchDirections
Deeplearningcanimproveriskdiscrimination, butdeployingsuchmodelsinreg-
ulatedcreditenvironmentsintroducesconstraintsthatgobeyondaccuracy. Thissection
summarisesthemainchallengesandthendistilsresearchdirectionsaimedattrustworthy,
regulation-readycreditriskmodelling.
6.1. ChallengesandLimitations
6.1.1. EvaluationIntegrity
Creditriskevolvesovertimeinresponsetobehavioural,policy,andmacroeconomic
shifts,makingrandomk-foldcross-validationpronetotemporalleakage. Whenobserva-
tionsfromlaterperiodsappearinbothtrainingandtestfolds,performanceestimatescan
implicitlyrelyonfutureinformationthatwouldnotbeavailableatdecisiontime. Time-
orderedevaluationschemes,includingout-of-timesplitsandrolling-originvalidationin
whichthetrainingwindowstrictlyprecedestheevaluationwindow,provideamorefaith-
fulestimateofdeploymentperformanceunderregimechangeandstressconditions[85].
However, a non-trivial portion of deep credit risk studies still relies on random splits,
weakeningexternalvalidityandcomplicatingcomparisonsacrossmodelfamilies.
A second source of fragility is over-reliance on threshold-agnostic summary met-
rics such as AUC, which aggregate performance across all score cut-offs and can mask
behaviourintheoperatingregionwherelendingdecisionsareactuallymade. Inhighlyim-
balancedportfolios,complementarymeasuressuchastheareaundertheprecision–recall
curve(AUPRC)andcost-sensitivemetricsbetterreflectminority-classperformanceand
theeconomicconsequencesofmisclassification[33]. Equallyimportant,probabilitycal-
ibration is rarely assessed, despite being central to decisioning and risk quantification:
poorlycalibratedscorescanleadtounstableapprovalrates,mis-pricedcredit,andbiased
downstreamestimatesofportfoliorisk,evenwhenrankingperformance(AUC)improves.
Calibration-sensitivereportingusingtheBrierscoreandexpectedcalibrationerror,together
withreliabilitydiagrams,providesdirectevidenceofwhetherpredictedprobabilitiesmatch
observeddefaultfrequencies[86]. Whenmiscalibrationisdetected,posthocmethodssuch
asPlattscaling,isotonicregression,andtemperaturescalingcanimprovealignmentbe-
tweenpredictedandempiricaldefaultrates[87],butthesestepsareseldomdocumentedin
deepcreditriskpapers.
Finally, decision-facing evaluation should make explicit how metrics map to lend-
ingoutcomes. ForPD-stylemodels,thisincludesreportingperformanceatoperationally
relevantthresholdsand,whereinputsareavailable,quantifyingutilityusingsimplecost
proxies(false-approvallossversusfalse-rejectionopportunitycost)orbypropagatingcali-
bratedPDintodownstreamlossconstructs(e.g.,EL-styleestimates),whileacknowledging
thatELisnotcomparableacrossheterogeneousdatasetsandrecoverydefinitions. These
considerationsjointlyformadefactoevaluationchecklistfordeployment-alignedcredit
riskmodelling.
6.1.2. ImbalancedLearningandRejectInference
Defaultdatasetsareheavilyimbalanced,andnaïveresamplingcandistorttemporal
andbehaviouralstructure. Over-samplingtechniquessuchasSMOTEareoftenapplied
indiscriminatelywithouttemporalsafeguards,whilecost-sensitivelearningbetterreflects
economicriskbutisinfrequentlyemployed[88,89]. Afurthercomplicationisrejectinfer-
ence: declinedapplicantslackobservedoutcomes,leadingtostructurallybiasedtraining
dataandunreliablegeneralisation[28,90,91]. Observedoutcomesareconditionalonaccep-
tancepolicies,leadingtosample-selectionbiasthatinflatesapparentmodelperformance
https://doi.org/10.3390/info17040395

Information2026,17,395 21of28
when applied to rejected populations. Existing proxy-based inference methods remain
heuristicandarenotalignedwithregulatorytransparencyexpectations.
6.1.3. InterpretabilityandFairness
Although deep models improve predictive power, their opacity conflicts with reg-
ulatory explainability requirements. Post hoc explanation tools, including SHAP and
integratedgradients,maynotprovidestable,counterfactual-faithfulexplanations[92]. In
practice,theappropriateexplanationtooldependsonthemodelfamilyandthedecision
artefactbeingjustified: forMLP-styletabularnetworks,featureattributionmethodsand
monotonicorsparseconstraintscansupportreasonedfactornarratives;fortree-likebase-
lines and tree–neural hybrids, TreeSHAP-style decompositions often provide the most
auditablefeature-levelbreakdown;fortransformer-basedcreditmodels,attributionover
token/feature embeddings (with attention used as a supportive diagnostic rather than
a standalone explanation) is typically more reliable than raw attention maps; and for
GNN-basedcreditmodels,subgraph-ormessage-passingexplanationscanlocalisewhich
relationsdriveariskscore.
FairnessisalsoinconsistentlyoperationalisedintheDLcredit-riskliterature. Metrics
suchasequalisedodds[93]arerarelyintegratedintotrainingobjectives,despiteevidence
thatautomatedlendingcanamplifyexistingsocio-economicinequalities. Fairnesstargets
arecontextdependent: demographicparitymaybeinappropriatewhenbaseratesdiffer
for legitimate reasons, whereas error-rate constraints such as equalised odds may be
moresuitablewhentheaimistocontroldifferentialmisclassificationharms. Accordingly,
the selected fairness definition should be justified relative to the lending decision, the
attributes available for monitoring, and the governing legal regime, and it should be
assessedalongsidemodelcalibrationandoperating-thresholdbehaviour. Counterfactual
explanationapproachesremainpromising,butdeploymentatscaleisoftenhinderedby
feasibilityconstraintsandbytheneedtoensureplausibilityunderrealcreditpolicyand
data-generatingprocesses[94].
Amongthesurveyeddeeplearningstudies,onlyasmallsubsetexplicitlyincorporates
posthocexplainabilitytoolsorfairnessmetrics,andevenfeweroptimisefairness-aware
objectivesduringtraining,whichshowsthegapbetweenregulatoryaspirationsandcur-
rentpractice.
6.1.4. RobustnessandPrivacy
Deeplearningmodelsaresensitivetoconceptdriftcausedbymacroeconomicshocks,
behaviouralchanges,andportfoliorebalancing,leadingtocalibrationdecayovertime[95].
Existingstudiesseldomincorporatedrift-awareretrainingorautomatedchangedetection.
Fordeployment-alignedrobustness,studiesshoulddistinguish(i)temporaldrift(vintage
andmacroshifts),(ii)populationdrift(portfoliomixchanges),and(iii)label/definition
drift(policyorcollections-rulechanges),andthenevaluatemitigationusingtime-ordered
backtestsratherthanrandomre-sampling. Operationally,thistranslatestomonitoringboth
discriminationandcalibrationovertime(e.g.,AUC/AUPRCalongsideBrier/ECE),trig-
geringreviewwhencalibrationdeviatesmateriallyevenifrankingmetricsappearstable.
Atthesametime,sharinggranulardataacrossinstitutionsintroducesprivacyand
confidentialityconstraints. Differentiallyprivatetrainingandsyntheticdatageneration
partiallyaddresstheselimitationsbutintroduceaccuracytrade-offs. Wherecollaboration
isrequired,privacy-preservinglearningshouldbeframedasanend-to-enddesignchoice
(e.g., federatedtrainingwithsecureaggregation, differentialprivacywithdocumented
privacy budgets, or controlled synthetic-data release), accompanied by utility and bias
testingtoshowwhatdecisionqualityislostorretainedunderprivacyconstraints.
https://doi.org/10.3390/info17040395

Information2026,17,395 22of28
6.1.5. OperationalDeploymentandGovernance
Operational success requires structured machine learning operations (MLOps)
pipelineswithversioning,lineagetracking,monitoring,andchallenger-championtesting.
Withoutthese, systemsaccumulatetechnicaldebtthatweakenscomplianceandunder-
minesmodellifecyclemanagement[96]. Inregulatedcreditsettings,deploymentdiscipline
istypicallyenforcedthroughamodelriskmanagementworkflowthatmakeseachstageau-
ditable: reproduciblefeaturepipelines,immutabletrainingandevaluationdatasets,signed
modelartefacts,andtraceabledecisionrecordsthatlinkeveryproductionscoretoaspecific
modelversionanddatasnapshot. Acommonrolloutpatternisstagedrelease,inwhich
acandidatemodelfirstpassesofflinebacktesting,thenrunsinshadowscoring(producing
scoreswithoutaffectingapprovals), andonlythenprogressestolimitedexposurewith
pre-definedpromotiongatesbasedoncalibration,drift,andstabilitychecks. Thesegates
reducefailuresthatfrequentlyoccurinpractice,suchassilentcalibrationdecayafterpolicy
orcollections-rulechanges,performancedropsundermacroeconomicregimeshifts,and
inconsistentfeaturecomputationbetweentrainingandserving.
Moreover,existinggovernanceartefacts,includingdatasheetsandmodelcards,are
rarelyintegratedwithregulatoryprocessessuchasBaselIII,SR11-7, ortheEUAIAct,
reducingorganisationalreadinessforexternalaudit. Tomakeinterpretabilityandfairness
operationalratherthanadhoc,explanationandbias-assessmentoutputsshouldbegener-
atedautomaticallypermodelversionwithintheCI/CDworkflowandstoredaspartof
themodelevidencepack. Concretely,thismeanslogging(i)globalandlocalexplanation
artefactsalignedwiththedeployedmodelfamily,(ii)fairnessreportscomputedonthe
productiondecisionpopulation(and,wherefeasible,onapproved-outcomepopulations),
and(iii)monitoringdashboardsthattrackbothdiscriminationandcalibrationovertime.
Whenexceptionsoccur(e.g.,manualoverrides,policy-drivenrulechanges,ortemporary
riskcontrols),thegovernancelayershouldrecordtheoverriderationaleanditsimpact
onobservedoutcomessothatfutureretrainingdoesnotunknowinglyencodeshort-term
interventionsaspredictivesignals.
6.2. FutureResearchDirections
Future research should adopt evaluation frameworks that reflect realistic data-
generating processes, including temporally constrained train-test splits, multi-horizon
performancetracking,andcalibration-awarereporting. Thisincludesbenchmarkingon
large-scale,longitudinaldatasetswithexplicittemporalstructureandeconomicannota-
tions,enablingfaircomparisonacrossmodelfamiliesandreducingover-optimismasso-
ciatedwithsmallpublicdatasets. Moreover,futureworkshouldprioritisecost-aligned
performancereporting,wheremodelutilityisquantifiedintermsofexpectedlossreduc-
tion,capitalefficiency,defaulttiming,andresilienceacrossmacroeconomicstressregimes
(Table5).
Anotherdirectionisthedevelopmentoflearningobjectivesthatintegratefairness,in-
terpretability,andeconomiccostattrainingtimeratherthanrelyingonposthocadjustment.
Interpretable-by-designarchitectures,monotonicneuralnetworks,sparseattentionmecha-
nisms,andhybridsymbolic-neuralmodelscanprovidegreaterregulatorycompatibility
whileretainingfeatureinteractioncapacity. Causalfairness,adversarialdebiasing,and
counterfactualtrainingpipelinesrepresentpromisingframeworksformitigatingdisparate
impactwithoutsuppressingpredictivepower.
https://doi.org/10.3390/info17040395

Information2026,17,395 23of28
Table5.Challengesindeeplearningcreditriskmodellingandalignedresearchdirections.
Challenge Description EmergingResearchDirections
Out-of-timeandrollingvalidation;
Temporalleakageandweakcalibration
EvaluationIntegrity calibration-awarereporting;cost-sensitive
undermineexternalvalidity[18,23,58,87].
andutility-alignedscoring.
Causalestimation,selectiveabstention,
Raredefaultsandmissingcounterfactual
ImbalanceandRejectInference semi-supervisedrejectinference,and
labelsdistortlearningsignals[88–90].
cost-sensitiveobjectives.
Interpretable-by-designarchitectures,
Deepmodelsviolateexplainabilityand
InterpretabilityandFairness causalfairnessconstraints,certified
anti-biascompliance[92,97].
explanationmechanisms.
Drift-robustadaptivetraining,federated
Driftandprivacyconstraintslimit
RobustnessandPrivacy learning,syntheticfinancialdigitaltwins,
long-termreliability[95,98].
DP-SGDoptimisation.
Automatedmonitoringframeworks,
Insufficientdeploymentdiscipline
OperationalDeploymentandGovernance model-cardpipelines,Basel-aligned
increasesregulatoryrisk[96,99].
documentationstandards.
Researchshouldalsofocusondesigningmodelsthatadaptunderuncertaintywhile
maintaining stability guarantees. Drift-aware architectures, online continual learning
mechanisms,uncertainty-calibratedpredictions,andstress-testingundermacroeconomic
scenariosimulationmayimprovelong-termreliability. Privacy-preservingcollaborative
learning,throughfederatedoptimisation,securemultipartycomputation,andhigh-fidelity
syntheticdigitaltwins,wouldenablecross-institutionallearningwhilerespectingconfiden-
tialityandregulation. Thisagendaalsorequiresgovernanceandregulatoryalignmentfor
cross-institutionaldatasharing,includingclearaccountabilityforconsent,accesscontrol,
retention,andauditability. Similarly,syntheticdatashouldbegovernedwithdocumented
generationprotocols,privacy-risktesting,anddownstream-userestrictionstoavoidleakage
andunwarrantedrelianceinregulateddecision-making.
Finally, there is a need for deployment-aligned governance frameworks that stan-
dardise model documentation, monitoring, and auditability. Integrated pipelines that
combineMLOpswithregulatoryartefacts,suchasmodelcardslinkedtovalidationlogs
andchallenger-championperformancetrails,couldaccelerateinstitutionaltrustandre-
ducecompliancecosts. Long-termprogresswillrequiresystemsthatarenotonlymore
accurate,butalsocertifiablyfair,transparent,androbust—makingdeeplearningsuitable
forproduction-gradefinancialriskmanagement.
7. Conclusions
Thissurveyrevieweddeeplearningmethodsforcreditriskpredictionacrosstabu-
lar,sequential,transformer-based,andgraph-structuredsettings. Byorganisingexisting
research through a unified taxonomy that links model families to data structures and
credit-riskobjectives,thesurveyprovidesconceptualclarityonwhenandwhyspecific
architecturesareappropriate. Acrossthepeer-reviewedevidence,deepmodelstendto
outperformtraditionalscorecardandensemblemethodswhentrainedonsufficientlylarge,
temporallyrepresentativedatasetswithrichbehaviouralandrelationalinformation.
However,theliteraturealsorevealsgapsthatconstrainreliablereal-worldadoption.
Reporting standards are inconsistent, with limited use of temporally valid evaluation,
calibrationmetrics,andcost-alignedperformancereporting. Interpretabilityandfairness
areoftentreatedasadd-onsratherthanrequirements,androbustnessunderconceptdrift,
data-sharingconstraints,andoperationalgovernanceremainsweaklyaddressed,shifting
successcriteriatowardpredictiveaccuracyratherthanlifecyclereliabilityandauditability.
https://doi.org/10.3390/info17040395

Information2026,17,395 24of28
Futureworkshouldthereforeprioritisedeployment-alignedresearch: interpretable-
by-designmodelling,temporallyrealisticbenchmarks,fairnessstrategiesgroundedinthe
decision and legal context, privacy-preserving collaborative learning, and governance-
readymonitoringanddocumentationpipelines. Thissurveyislimitedtopeer-reviewed
English-language studies indexed in major databases and does not cover proprietary
implementationsorregulatorygreyliterature;futuresynthesescouldextendtheevidence
base using secure-access supervisory data or meta-analyses where study designs and
outcomesaresufficientlycomparable.
AuthorContributions: Conceptualisation,I.D.M.,E.E.andC.M.; methodology,I.D.M.,E.E.and
C.M.;validation,I.D.M.,E.E.andC.M.;investigation,I.D.M.,E.E.andC.M.;writing—originaldraft
preparation,I.D.M.;writing—reviewandediting,I.D.M.,E.E.andC.M.;visualisation,I.D.M.,E.E.
andC.M.;supervision,E.E.andC.M.Allauthorshavereadandagreedtothepublishedversionof
themanuscript.
Funding:Thisresearchreceivednoexternalfunding.
InstitutionalReviewBoardStatement:Notapplicable.
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement:Nonewdatawerecreatedoranalysedinthisstudy.Datasharingis
notapplicabletothisarticle.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.
Abbreviations
Thefollowingabbreviationsareusedinthismanuscript:
AI Artificialintelligence
AUC Areaunderthereceiveroperatingcharacteristiccurve
AUPRC Areaundertheprecision–recallcurve
CNNs Convolutionalneuralnetworks
DL Deeplearning
EAD Exposureatdefault
EL Expectedloss
GNNs Graphneuralnetworks
GRU Gatedrecurrentunit
HDNN High-dimensionaldeepneuralnetwork
I-DNN IncrementalDNN
LGD Lossgivendefault
LR Logisticregression
LSTM Longshort-termmemory
ML Machinelearning
MLOps Machinelearningoperations
MLP Multi-layerperceptron
MS-CGNN Multi-structurecascadedGNN
NODE NeuralObliviousDecisionEnsembles
PD Probabilityofdefault
PDNN Penaliseddeepneuralnetwork
RNNs Recurrentneuralnetworks
RWA Risk-weightedasset
SME Smallandmediumenterprise
SVMs Supportvectormachines
TCNs Temporalconvolutionalnetworks
XAI ExplainableAI
https://doi.org/10.3390/info17040395

Information2026,17,395 25of28
References
1. Zhu,Y.;Wu,D. P2PcreditriskmanagementwithKG-GNN:Aknowledgegraphandgraphneuralnetwork-basedapproach.
J.Oper.Res.Soc.2025,76,866–880.[CrossRef]
2. Alagic,A.;Zivic,N.;Kadusic,E.;Hamzic,D.;Hadzajlic,N.;Dizdarevic,M.;Selmanovic,E. Machinelearningforanenhanced
creditriskanalysis:Acomparativestudyofloanapprovalpredictionmodelsintegratingmentalhealthdata. Mach.Learn.Knowl.
Extr.2024,6,53–77.[CrossRef]
3. Karami,A.;Igbokwe,C. Theimpactofbigdatacharacteristicsoncreditriskassessment. Int.J.DataSci.Anal.2025,20,4239–4259.
[CrossRef]
4. Talaat,F.M.;Aljadani,A.;Badawy,M.;Elhosseini,M. Towardinterpretablecreditscoring: Integratingexplainableartificial
intelligencewithdeeplearningforcreditcarddefaultprediction. NeuralComput.Appl.2024,36,4847–4865.[CrossRef]
5. Aruleba,I.;Sun,Y. Effectivecreditriskpredictionusingensembleclassifierswithmodelexplanation. IEEEAccess2024,12,
115015–115025.[CrossRef]
6. Machado,M.R.;Chen,D.T.;Osterrieder,J.R. Ananalyticalapproachtocreditriskassessmentusingmachinelearningmodels.
Decis.Anal.J.2025,16,100605.[CrossRef]
7. Tian,Z.;Xiao,J.;Feng,H.;Wei,Y. Creditriskassessmentbasedongradientboostingdecisiontree. ProcediaComput.Sci.2020,
174,150–160.[CrossRef]
8. Aruleba,I.;Sun,Y. EnhancedcreditriskpredictionusingdeeplearningandSMOTE-ENNresampling. Mach.Learn.Appl.2025,
21,100692.[CrossRef]
9. Sun,P.;Jia,Y.;Shi,Y.;Ren,J.;Li,Z.;Li,X. ArtificialIntelligenceCreditRiskAssessmentModelBasedonMLP-HybridClustering.
Complexity2025,2025,3308222.[CrossRef]
10. Mienye,I.D.;Esenogho,E.;Modisane,C. DeepReinforcementLearningintheEraofFoundationModels:ASurvey. Computers
2026,15,40.[CrossRef]
11. Bhatore,S.;Mohan,L.;Reddy,Y.R. Machinelearningtechniquesforcreditriskevaluation:Asystematicliteraturereview. J.Bank.
Financ.Technol.2020,4,111–138.[CrossRef]
12. Shi,S.;Tse,R.;Luo,W.;D’Addona,S.;Pau,G. Machinelearning-drivencreditrisk:Asystemicreview. NeuralComput.Appl.2022,
34,14327–14339.[CrossRef]
13. Noriega,J.P.;Rivera,L.A.;Herrera,J.A. Machinelearningforcreditriskprediction:Asystematicliteraturereview. Data2023,
8,169.[CrossRef]
14. Montevechi,A.A.;deCarvalhoMiranda,R.;Medeiros,A.L.;Montevechi,J.A.B. AdvancingcreditriskmodellingwithMachine
Learning:Acomprehensivereviewofthestate-of-the-art. Eng.Appl.Artif.Intell.2024,137,109082.[CrossRef]
15. Kim,H.;Cho,H.;Ryu,D. Corporatedefaultpredictionsusingmachinelearning:Literaturereview. Sustainability2020,12,6325.
[CrossRef]
16. Çallı,B.A.;Cos¸kun,E. Alongitudinalsystematicreviewofcreditriskassessmentandcreditdefaultpredictors. SageOpen2021,
11,21582440211061333.[CrossRef]
17. Mhlanga,D. Financialinclusioninemergingeconomies:Theapplicationofmachinelearningandartificialintelligenceincredit
riskassessment. Int.J.Financ.Stud.2021,9,39.[CrossRef]
18. Hayashi,Y. Emergingtrendsindeeplearningforcreditscoring:Areview. Electronics2022,11,3181.[CrossRef]
19. Peng,K.;Yan,G. Asurveyondeeplearningforfinancialriskprediction. Quant.Financ.Econ.2021,5,716–737.[CrossRef]
20. HoyosGutiérrez,S.P.;SantosLópez,F.M. CreditRiskAssessmentSystemBasedonDeepLearning: ASystematicLiterature
Review. InProceedingsoftheInternationalConferenceonComputerScience,ElectronicsandIndustrialEngineering(CSEI);Springer:
Berlin/Heidelberg,Germany,2023;pp.395–413.
21. DemmaWube,H.;ZekariasEsubalew,S.;FayisoWeldesellasie,F.;GirmaDebelee,T. Deeplearningandmachinelearningtech-
niquesforcreditscoring:Areview. InProceedingsofthePanAfricanConferenceonArtificialIntelligence;Springer:Berlin/Heidelberg,
Germany,2024;pp.30–61.
22. Mienye,E.;Jere,N.;Obaido,G.;Mienye,I.D.;Aruleba,K. DeepLearninginFinance:ASurveyofApplicationsandTechniques.
AI2024,5,2066–2091.[CrossRef]
23. Valdrighi, G.; MRibeiro, A.; SBPereira, J.; Guardieiro, V.; Hendricks, A.; MirandaFilho, D.; NietoGarcia, J.D.; FBocca, F.;
BVeronese,T.;Wanner,L.;etal. Bestpracticesforresponsiblemachinelearningincreditscoring. NeuralComput.Appl.2025,37,
20781–20821.[CrossRef]
24. Paz,Á.;Crawford,B.;Monfroy,E.;Barrera-García,J.;PeñaFritz,Á.;Soto,R.;Cisternas-Caneo,F.;Yáñez,A. MachineLearning
andMetaheuristicsApproachforIndividualCreditRiskAssessment:ASystematicLiteratureReview. Biomimetics2025,10,326.
[CrossRef]
25. Alvi,J.;Arif,I.;Nizam,K. Advancingfinancialresilience:Asystematicreviewofdefaultpredictionmodelsandfuturedirections
increditriskmanagement. Heliyon2024,10,e39770.[CrossRef]
https://doi.org/10.3390/info17040395

Information2026,17,395 26of28
26. Bhattacharya, A.; Biswas, S.K.; Mandal, A. Credit risk evaluation: A comprehensive study. Multimed. Tools Appl. 2023,
82,18217–18267.[CrossRef]
27. Gunnarsson,B.R.;VandenBroucke,S.;Baesens,B.;Óskarsdóttir,M.;Lemahieu,W. Deeplearningforcreditscoring:Doordon’t?
Eur.J.Oper.Res.2021,295,292–305.[CrossRef]
28. Thomas,L.;Crook,J.;Edelman,D. CreditScoringandItsApplications;SIAM:Philadelphia,PA,USA,2017.
29. Bandyopadhyay,A. Loanlevellossgivendefault(LGD)studyofIndianbanks. IIMBManag.Rev.2022,34,168–177.[CrossRef]
30. Wattanawongwan,S.;Mues,C.;Okhrati,R.;Choudhry,T.;So,M.C. Modellingcreditcardexposureatdefaultusingvinecopula
quantileregression. Eur.J.Oper.Res.2023,311,387–399.[CrossRef]
31. Hofmann,H.Statlog(GermanCreditData). UCIMachineLearningRepository.1994.Availableonline:https://archive.ics.uci.
edu/dataset/144/statlog+german+credit+data(accessedon1October2025).
32. Yeh,I.C.;Lien,C.H. Thecomparisonsofdataminingtechniquesforthepredictiveaccuracyofprobabilityofdefaultofcredit
cardclients. ExpertSyst.Appl.2009,36,2473–2480.[CrossRef]
33. Lessmann,S.;Baesens,B.;Seow,H.V.;Thomas,L.C. Benchmarkingstate-of-the-artclassificationalgorithmsforcreditscoring:An
updateofresearch. Eur.J.Oper.Res.2015,247,124–136.[CrossRef]
34. Montoya,A.;Inversion;KirillOdintsov;Kotek,M. HomeCreditDefaultRisk.Kaggle.2018. Availableonline:https://kaggle.
com/competitions/home-credit-default-risk(accessedon5December2025).
35. Malekipirbazari,M.;Aksakalli,V. Riskassessmentinsociallendingviarandomforests. ExpertSyst.Appl.2015,42,4621–4631.
[CrossRef]
36. Nwafor,C.N.;Nwafor,O.;Brahma,S. Enhancingtransparencyandfairnessinautomatedcreditdecisions:Anexplainablenovel
hybridmachinelearningapproach. Sci.Rep.2024,14,25174.[CrossRef]
37. deOliveira,N.A.;Basso,L.F.C. AdvancingCreditRatingPrediction:TheRoleofMachineLearninginCorporateCreditRating
Assessment. Risks2025,13,116.[CrossRef]
38. LeCun,Y.;Bengio,Y.;Hinton,G. Deeplearning. Nature2015,521,436–444.[CrossRef]
39. Mienye, I.D.; Swart, T.G.; Obaido, G. Recurrent neural networks: A comprehensive review of architectures, variants, and
applications. Information2024,15,517.[CrossRef]
40. Mienye,I.D.;Esenogho,E.;Modisane,C. DetectingImbalancedCreditCardFraudviaHybridGraphAttentionandVariational
AutoencoderEnsembles. AppliedMath2025,5,131.[CrossRef]
41. Bai,S.;Kolter,J.Z.;Koltun,V. Anempiricalevaluationofgenericconvolutionalandrecurrentnetworksforsequencemodeling.
arXiv2018,arXiv:1803.01271.[CrossRef]
42. Liu,M.;Xia,C.;Xia,Y.;Deng,S.;Wang,Y. TDCN:Anoveltemporaldepthwiseconvolutionalnetworkforshort-termload
forecasting. Int.J.Electr.PowerEnergySyst.2025,165,110512.[CrossRef]
43. Dong,A.;Starr,A.;Zhao,Y. AninterpretabletemporalconvolutionalframeworkforGrangercausalityanalysis. IEEE/CAAJ.
Autom.Sin.2025,13,1–15.[CrossRef]
44. Vashishth,T.K.;Sharma,V.;Sharma,K.K.;Ahamad,S.;Kaushik,V. FinancialForecastingwithConvolutionalNeuralNetworks
(CNNs):TrendsandChallenges. InShapingCutting-EdgeTechnologiesandApplicationsforDigitalBankingandFinancialServices;
Taylor&Francis:Abingdon,UK,2025;pp.62–81.
45. Mienye,I.D.;Swart,T.G. Acomprehensivereviewofdeeplearning:Architectures,recentadvances,andapplications. Information
2024,15,755.[CrossRef]
46. Vaswani,A.;Shazeer,N.;Parmar,N.;Uszkoreit,J.;Jones,L.;Gomez,A.N.;Kaiser,Ł.;Polosukhin,I. Attentionisallyouneed.
Adv.NeuralInf.Process.Syst.2017,30,6000–6010.
47. Huang,X.;Khetan,A.;Cvitkovic,M.;Karnin,Z. Tabtransformer:Tabulardatamodelingusingcontextualembeddings. arXiv
2020,arXiv:2012.06678.[CrossRef]
48. Yang,M.;Lim,M.K.;Qu,Y.;Li,X.;Ni,D. DeepneuralnetworkswithL1andL2regularizationforhighdimensionalcorporate
creditriskprediction. ExpertSyst.Appl.2023,213,118873.[CrossRef]
49. Lin,C.;Qiao,N.;Zhang,W.;Li,Y.;Ma,S. Defaultriskpredictionandfeatureextractionusingapenalizeddeepneuralnetwork.
Stat.Comput.2022,32,76.[CrossRef]
50. Asencios,R.;Asencios,C.;Ramos,E. Profitscoringforcreditunionsusingthemultilayerperceptron,XGBoostandTabNet
algorithms:EvidencefromPeru. ExpertSyst.Appl.2023,213,119201.[CrossRef]
51. Wang,S.;Zhang,X. ResearchoncreditdefaultpredictionmodelbasedonTabNet-stacking. Entropy2024,26,861.[CrossRef]
52. Hjelkrem,L.O.;Lange,P.E.d. ExplainingdeeplearningmodelsforcreditscoringwithSHAP:AcasestudyusingOpenBanking
Data. J.RiskFinanc.Manag.2023,16,221.[CrossRef]
53. Li,G.;Zhu,F.;Zhang,Y.;Li,M. AData-DrivenIncrementalDeepNeuralNetworkforBorrowerCreditScoring. SSRN2023.
[CrossRef]
54. Popov, S.; Morozov, S.; Babenko, A. Neural oblivious decision ensembles for deep learning on tabular data. arXiv 2019,
arXiv:1909.06312.[CrossRef]
https://doi.org/10.3390/info17040395

Information2026,17,395 27of28
55. Shan,W.;Gao,B. StackedEnsembleModelwithEnhancedTabNetforSMESupplyChainFinancialRiskPrediction. Systems2025,
13,892.[CrossRef]
56. Liang,L.;Cai,X. Forecastingpeer-to-peerplatformdefaultratewithLSTMneuralnetwork. Electron.Commer.Res.Appl.2020,
43,100997.[CrossRef]
57. Ala’raj,M.;Abbod,M.F.;Majdalawieh,M.;Jum’a,L. Adeeplearningmodelforbehaviouralcreditscoringinbanks. Neural
Comput.Appl.2022,34,5839–5866.[CrossRef]
58. Zhang,L. TheEvaluationontheCreditRiskofEnterpriseswiththeCNN-LSTM-ATTModel. Comput. Intell. Neurosci. 2022,
2022,6826573.[CrossRef][PubMed]
59. Li,J.;Xu,C.;Feng,B.;Zhao,H. CreditriskpredictionmodelforlistedcompaniesbasedonCNN-LSTMandattentionmechanism.
Electronics2023,12,1643.[CrossRef]
60. Wang,H.;Bellotti,A.;Qu,R.;Bai,R. Discrete-TimeSurvivalModelswithNeuralNetworksforAge–Period–CohortAnalysisof
CreditRisk. Risks2024,12,31.
61. Chen,B.;Long,S. Anovelend-to-endcorporatecreditratingmodelbasedonself-attentionmechanism. IEEEAccess2020,
8,203876–203889.[CrossRef]
62. Han,D.;Guo,W.;Chen,Y.;Wang,B.;Li,W. Personalcreditdefaultpredictionfusionframeworkbasedonself-attentionand
cross-networkalgorithms. Eng.Appl.Artif.Intell.2024,133,107977.[CrossRef]
63. Shi,X.;Tang,D.;Yu,Y. CreditScoringPredictionUsingDeepLearningModelsintheFinancialSector. IEEEAccess2025,13,
130731–130746.[CrossRef]
64. Yang,Y.;Lin,Y.;Zhang,Y.;Su,Z.;Goh,C.C.;Fang,T.;Bellotti,A.G.;Lee,B.G. TransformingCreditRiskAnalysis:ATime-Series-
DrivenResE-BiLSTMFrameworkforPost-LoanDefaultDetection. arXiv2025,arXiv:2508.00415.[CrossRef]
65. Zhang, Y. AI-Driven Framework for Financial Risk Management: Enhancing Decision-Making with LSTM Networks and
ProbabilisticModels. InProceedingsofthe20252ndInternationalConferenceonIntelligentComputingandRobotics(ICICR);IEEE:
Piscataway,NJ,USA,2025;pp.176–181.
66. Gorishniy,Y.;Rubachev,I.;Khrulkov,V.;Babenko,A. Revisitingdeeplearningmodelsfortabulardata. Adv.NeuralInf.Process.
Syst.2021,34,18932–18943.
67. Wang,C.;Xiao,Z. Adeeplearningapproachforcreditscoringusingfeatureembeddedtransformer. Appl.Sci.2022,12,10995.
[CrossRef]
68. Korangi,K.;Mues,C.;Bravo,C. Atransformer-basedmodelfordefaultpredictioninmid-capcorporatemarkets. Eur.J.Oper.
Res.2023,308,306–320.[CrossRef]
69. Li,J.;Zhou,Z.;Zhang,J.;Cheng,D.;Jiang,C. HFTCRNet:Hierarchicalfusiontransformerforinterbankcreditratingandrisk
assessment. IEEETrans.NeuralNetw.Learn.Syst.2024,36,13006–13020.[CrossRef]
70. Kakadiya,R.;Khan,T.;Diwan,A.;Mahadeva,R. TransformerModelsforPredictingBankLoanDefaultsaNext-GenerationRisk
Management. InProceedingsofthe2024IEEE6thInternationalConferenceonCybernetics,CognitionandMachineLearningApplications
(ICCCMLA);IEEE:Piscataway,NJ,USA,2024;pp.26–31.
71. Zhang,Y.;Liang,X. PersonalCreditRiskPredictionBasedonMinimumWeightValueErrorCombinationModel. InProceedings
ofthe20258thInternationalConferenceonAdvancedAlgorithmsandControlEngineering(ICAACE);IEEE:Piscataway,NJ,USA,2025;
pp.307–313.
72. Hartomo,K.D.;Arthur,C.;Nataliani,Y. Anovelweightedlosstabtransformerintegratingexplainableaiforimbalancedcredit
riskdatasets. IEEEAccess2025,13,31045–31056.[CrossRef]
73. Wu,Y. Enterprisefinancialsharingandriskidentificationmodelcombiningrecurrentneuralnetworkswithtransformermodel
supportedbyblockchain. Heliyon2024,10,e32639.[CrossRef]
74. Stevenson,M.;Mues,C.;Bravo,C. Thevalueoftextforsmallbusinessdefaultprediction:Adeeplearningapproach. Eur.J.Oper.
Res.2021,295,758–771.[CrossRef]
75. Lu,S.;Zhang,X.;Su,Y.;Liu,X.;Yu,L. Efficientmultimodallearningforcorporatecreditriskpredictionwithanextendeddeep
beliefnetwork. InAnnalsofOperationsResearch;Springer:Berlin/Heidelberg,Germany, 2025;pp.1–38.
76. Schwab,B.;Kriebel,J. Mitigatingadversarialattacksontransformermodelsincreditscoring. Eur.J.Oper.Res.2025,328,309–323.
[CrossRef]
77. Wang,J.;Liu,G.;Xu,X.;Xing,X. Creditriskpredictionforsmallandmediumenterprisesutilizingadjacententerprisedataanda
relationalgraphattentionnetwork. J.Manag.Sci.Eng.2024,9,177–192.[CrossRef]
78. Song, L.; Li, H.; Tan, Y.; Li, Z.; Shang, X. Enhancing enterprise credit risk assessment with cascaded multi-level graph
representationlearning. NeuralNetw.2024,169,475–484.[CrossRef][PubMed]
79. Yuan,Q.;Liu,Y.;Tang,Y.;Chen,X.;Zheng,X.;He,Q.;Ao,X. DynamicGraphLearningwithStaticRelationsforCreditRisk
Assessment. InProceedingsoftheAAAIConferenceonArtificialIntelligence,Philadelphia,PA,USA,25February–4March2025;
Volume39,pp.13133–13141.
https://doi.org/10.3390/info17040395

Information2026,17,395 28of28
80. Mojdehi,K.F.;Amiri,B.;Haddadi,A. ANovelHybridModelforCreditRiskAssessmentofSupplyChainFinanceBasedon
TopologicalDataAnalysisandGraphNeuralNetwork. IEEEAccess2025,13,13101–13127.[CrossRef]
81. Wang,D.;Zhang,Z.;Zhao,Y.;Huang,K.;Kang,Y.;Zhou,J. Financialdefaultpredictionviamotif-preservinggraphneural
networkwithcurriculumlearning. InProceedingsofthe29thACMSIGKDDConferenceonKnowledgeDiscoveryandData
Mining,LongBeach,CA,USA,6–10August2023;pp.2233–2242.
82. Liu,B.; Li,I.; Yao,J.; Chen,Y.; Huang,G.; Wang,J. UnveilingthePotentialofGraphNeuralNetworksinSMECreditRisk
Assessment. InProceedingsofthe20245thInternationalConferenceonIntelligentComputingandHuman-ComputerInteraction(ICHCI);
IEEE:Piscataway,NJ,USA,2024;pp.562–566.
83. Zhang,Z.;Shen,Q.;Hu,Z.;Liu,Q.;Shen,H. CreditriskanalysisforSMEsusinggraphneuralnetworksinsupplychain. In
Proceedingsofthe2025InternationalConferenceonBigData,ArtificialIntelligenceandDigitalEconomy,Kunming,China,
18–20July2025;pp.81–85.
84. Cheng,C.;Luo,C. EnterpriseCreditRatingFrameworkBasedonRiskContagionGraphNeuralNetwork. InProceedingsofthe
InternationalConferenceonMachineLearningandSoftComputing;Springer:Berlin/Heidelberg,Germany,2025;pp.243–254.
85. Bergmeir,C.; Benítez,J.M. Ontheuseofcross-validationfortimeseriespredictorevaluation. Inf. Sci. 2012,191,192–213.
[CrossRef]
86. Fonseca, P.G.; Lopes, H.D. Calibration of machine learning classifiers for probability of default modelling. arXiv 2017,
arXiv:1710.08901.[CrossRef]
87. Guo,C.;Pleiss,G.;Sun,Y.;Weinberger,K.Q. Oncalibrationofmodernneuralnetworks. InProceedingsoftheInternational
ConferenceonMachineLearning,Sydney,Australia,6–11August2017;pp.1321–1330.
88. Idwan, S.; Etaiwi, W.; Rafayia, H.; Matar, I. A comprehensive review of statistical variants and enhancements of SMOTE
oversamplingmethod. Int.J.DataSci.Anal.2025,20,6887–6904.[CrossRef]
89. Hu,X.;Chen,H.;Zhang,J.;Chen,H.;Liu,S.;Li,X.;Wang,Y.;Xue,X. GAT-COBO:Cost-sensitivegraphneuralnetworkfor
telecomfrauddetection. IEEETrans.BigData2024,10,528–542.[CrossRef]
90. Andrae,S. Fairnessandbiasinmachinelearningmodelsforcreditdecisions. InMachineLearningandModelingTechniquesin
FinancialDataScience;IGIGlobalScientificPublishing:Hershey,PA,USA,2025;pp.1–24.
91. Liao,J.;Wang,W.;Xue,J.;Lei,A.;Han,X.;Lu,K. Combatingsamplingbias:Aself-trainingmethodincreditriskmodels. In
ProceedingsoftheAAAIConferenceonArtificialIntelligence,Online,22February–1March2022;Volume36,pp.12566–12572.
92. Rudin,C. Stopexplainingblackboxmachinelearningmodelsforhighstakesdecisionsanduseinterpretablemodelsinstead.
Nat.Mach.Intell.2019,1,206–215.[CrossRef]
93. Hardt,M.;Price,E.;Srebro,N. Equalityofopportunityinsupervisedlearning. Adv.NeuralInf.Process.Syst.2016,29,3323–3331.
94. Wachter,S.;Mittelstadt,B.;Russell,C. Counterfactualexplanationswithoutopeningtheblackbox:Automateddecisionsandthe
GDPR. Harv.JLTech.2017,31,841.[CrossRef]
95. Greco,S.;Vacchetti,B.;Apiletti,D.;Cerquitelli,T. Unsupervisedconceptdriftdetectionfromdeeplearningrepresentationsin
real-time. IEEETrans.Knowl.DataEng.2025,37,6232–6245.[CrossRef]
96. Ximenes,R.;Alves,A.P.S.;Escovedo,T.;Spinola,R.;Kalinowski,M. InvestigatingIssuesthatLeadtoCodeTechnicalDebtin
MachineLearningSystems. InProceedingsofthe2025IEEE/ACM4thInternationalConferenceonAIEngineering–SoftwareEngineering
forAI(CAIN);IEEE:Piscataway,NJ,USA,2025;pp.173–183.
97. Bartlett,R.;Morse,A.;Stanton,R.;Wallace,N. Consumer-lendingdiscriminationintheFinTechEra. J.Financ. Econ. 2022,
143,30–56.[CrossRef]
98. Pradhan,R.;Alazzam,M.B.;Keswani,S.;Bhasin,N.K.;Jaff,N.A.;Muthuperumal,S. AHybridGRU-TransformerModelfor
FinancialForecastingandRiskManagement. InProceedingsofthe20253rdInternationalConferenceonIntegratedCircuitsand
CommunicationSystems(ICICACS);IEEE:Piscataway,NJ,USA,2025;pp.1–5.
99. Amershi,S.;Begel,A.;Bird,C.;DeLine,R.;Gall,H.;Kamar,E.;Nagappan,N.;Nushi,B.;Zimmermann,T. Softwareengineering
formachinelearning: Acasestudy. InProceedingsofthe2019IEEE/ACM41stInternationalConferenceonSoftwareEngineering:
SoftwareEngineeringinPractice(ICSE-SEIP);IEEE:Piscataway,NJ,USA,2019;pp.291–300.
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.
https://doi.org/10.3390/info17040395

Reproduced with permission of copyright owner. Further reproduction
prohibited without permission.