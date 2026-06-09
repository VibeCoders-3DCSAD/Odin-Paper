| HeadOffice:    | UniversityofPadova           |     |     |     |     |
| -------------- | ---------------------------- | --- | --- | --- | --- |
| Department:    | DepartmentofMathematics      |     |     |     |     |
| Ph.D.Coursein: | Brain,MindandComputerScience |     |     |     |     |
Curriculum: ComputerScienceandInnovationforSocietalChallenges
Series: XXXVI
| Integration | of Explainability |            | in Recommender   | Systems | to  |
| ----------- | ----------------- | ---------- | ---------------- | ------- | --- |
|             | Enhance           | Enterprise | Value Strategies |         |     |
ThesiswrittenwiththefinancialcontributionofEstilossrl
| Coordinator:   | Prof. AnnaSpagnolli |     |               |                |     |
| -------------- | ------------------- | --- | ------------- | -------------- | --- |
| Supervisor:    | Prof. FabioAiolli   |     |               |                |     |
| Co-Supervisor: | Prof. AnnaSpagnolli |     |               |                |     |
|                |                     |     | Ph.D.student: | AndreaMontagna |     |

ii

“Aleaiactaest”
—GaiusIuliusCaesar

iv

Abstract
Companiesareoftenlookingforstrategiestoachievebusinessgoalsinthemostefficientway.
Intheirjourney,theyrelyonsystemsandalgorithmstosupporttheirdecisions. Onefamilyof
algorithms,thathelpscompaniesinchoosingwhichactionstotake,isRecommenderSystems
(RSs). RSs are a family of algorithms that generate suggestions of the item-user type. They
are widely used in social networks, e-commerce, news and advertising, and online streaming
applications. However,oneareathathasnotyetbeenwidelyaddressedintheliteratureisre-
latedtothebusinesseffectsofrecommendations. Thebusinesseffectcanbeinterpretedasthe
generationofvalueforthecompany,whichcantakemanyshapesandinvolvemanyusers. For
example,thebusinessvaluemayconsistnotonlyofadirectmeasureofcompanymetrics,such
as revenue or profit, but also of changing the sales distribution, increasing Clicks-Through
Ratesforanadvertisement,orevenkeepingauser’sinterestinanitemhigh.
ThistopicintheliteratureiscalledValue-AwareRecommenderSystems(VARSs). VARSs
areaparticularclassofRSsthataimtomaximizeoneormorebusinessindicatorstoachieve
awell-establishedbusinessobjective. ThroughVARSs, acompanycanadoptstrategiestoin-
creaseefficiencyandanswerbusinessquestionsbydrivingthemarketdynamically. However,
end-usersmustunderstandarecommendationtogetthebesttradeoffbetweendemandandre-
sponse. Inthefirstpartofthisthesis,weexplorethestate-of-the-artofVARSs,collectingand
classifying all VARSs available in literature in a first-of-its-topic systematic review. Addition-
ally, we propose a more specific taxonomic categorization for the different models provided,
highlightingthemodeloutcomeandtheeconomicperspective.
Furthermore,inordertoimprovethecomprehensionofthesuggestionsprovidedbythese
algorithms,wefocusonExplainableArtificialIntelligence(XAI)thataimstopromotetrans-
parencyinRSsandthusincentivizeuseradoption. XAIfocusesondifferentperspectives,such
asindustrial,social,andend-user,givingexplanationsbasedonthecontext. Inthesecondpart
ofthethesis,wesuggestanovel,explainable,value-awarerecommendersystemthataimstobal-
anceXAIandVARSperspectives. ApplyingXAItoVARSsisstillexploratoryandhasseveral
potentialevolutionsandacademic-industrialinterests.
Scientificresearchhasshownthattherearemanyadvantagestocomplementingarecommen-
dationwithaconvincingexplanation. Forexample,suchexplanationsoftenleadtoimproved
usertrust,whichinturnimprovestheeffectivenessofrecommendationsandsystemadoption.
Inparticular,forthisreason,manyresearchworksarestudyingexplainablerecommendational-
gorithmsbasedongraphs,i.e.,exploitingKnowledgeGraph(KG)orGraphNeuralNetworks
(GNNs)methods. Theuseofgraphsisverypromisingsincealgorithmscan,inprinciple,com-
bine the benefits of personalization and graph reasoning, thus potentially improving the ef-
fectiveness of both recommendations and explanations. However, although graph-based al-
v

gorithmshavebeenrepeatedlyshowntobringimprovementsintermsofrankingquality,not
muchliteraturehasyetstudiedhowtoproperlyevaluatethequalityofthecorrespondingexpla-
nations. Inthefinalpartofthisthesis,wediscussaproblemthataffectsexplainabilityfeatures
appliedonKGandGNNmodels,examininghowtheyarecurrentlyassessedandsuggesting
thedirectionforafuturemorequantitativeandcomparableevaluation.
vi

Acknowledgments
I would like to express my gratitude to the many persons who have supported and inspired
methroughoutmydoctoraljourney. Thisachievementwouldnothavebeenpossiblewithout
theirunwaveringencouragement,guidance,andunderstanding.
Firstofall,IwouldliketosincerelythankEstilos,theorganizationthatallowedmetocon-
ductmyresearchduringthisimportantmomentinmycareer,andallmycolleagues. Inpartic-
ular,IthankSuleimaCitron,MarcoColusso,andPaoloTrevisanforhandlingprojectsinthe
best possible way so that I could concentrate on my Ph.D. program. Finally, I would like to
thankAndreaBergamo,CEOofEstilossrl,whohasbeenmyhuman,intellectual,andprofes-
sional mentor throughout this journey. Your commitment to innovation and excellence has
providedmewitharichandstimulatingenvironmenttoexplorethecomplexitiesofartificial
intelligencesystems. Iamtrulygratefulforyoursupport.
Ioweadebtofgratitudetomycolleagueandfriend, AlviseDeBiasio. Oursharedexperi-
ences,challenges,andtriumphshavemadethisjourneynotonlyintellectuallyrewardingbut
alsodeeplyandhumanlymeaningful. Thankyouforbeinganincrediblecompaniononthis
path.
AwarmgreetingtotheHCAIteaminMagdeburg,Germany,whowelcomedmeduringmy
abroad period. Your hospitality and competence have enriched my academic experience and
broadenedmyhorizons.
Tomyfamily,whohavestoodbymefromafar,offeringmetheirunwaveringsupportand
encouragement,especiallyduringthedifficulttimesofthepastyear,Iamdeeplygrateful. Your
trustinmehasbeenaconstantsourceofmotivation.
Last but certainly not least, I want to express my love and gratitude to my partner, Silvia
Balzan. Your boundless faith in my abilities and your constant support have been my rock.
Yourpresenceinmylifehasmadethisjourneyevenmoremeaningful. Youaremycompanion
onthisandfuturejourneys.
Toallmymentors,friends,andlovedoneswhohaveplayedaroleinmyacademicandper-
sonal growth, I extend my warmest thanks. Your contributions, whether big or small, have
shapedmypath.
Thankyou,oneandall,forbeinganintegralpartofthisincrediblejourney.
vii

viii

Contents
Abstract v
Acknowledgments vi
Listoffigures xi
Listoftables xiii
Listingofacronyms xv
1 Introduction 1
1.1 ResearchMotivationandContribution . . . . . . . . . . . . . . . . . . . . 3
1.2 Structureofthethesis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.3 Publications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.4 Workinprogress . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2 Value-AwareRecommenderSystem 7
2.1 BackgroundandConcepts . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.1.1 RecommendationAlgorithms . . . . . . . . . . . . . . . . . . . . 8
2.2 RelatedWork . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.2.1 Value-AwareRecommenderSystems . . . . . . . . . . . . . . . . . 10
2.2.2 OtherClassesofRecommenderSystemsandRelatedWorks . . . . . 13
2.3 ProposedApproach . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
2.3.1 ResearchQuestions . . . . . . . . . . . . . . . . . . . . . . . . . . 15
2.3.2 EligibilityCriteria . . . . . . . . . . . . . . . . . . . . . . . . . . 15
2.3.3 SearchStrategy . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
2.3.4 SelectionProcess . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
2.3.5 StudyLimitations . . . . . . . . . . . . . . . . . . . . . . . . . . 17
2.4 Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
2.4.1 Value-AwareRecommenderAlgorithmTaxonomy . . . . . . . . . . 17
2.4.2 Value-AwareRecommenderSystemsApplications . . . . . . . . . . 22
2.4.3 Datasets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
2.5 Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
2.5.1 BalancingAccuracyandProfitability . . . . . . . . . . . . . . . . . 35
2.5.2 OntheLong-TermPerspectiveofValueCreation . . . . . . . . . . 36
ix

2.5.3 DynamicPricingforValueOptimization . . . . . . . . . . . . . . . 36
2.5.4 Value-AwarePerformanceEvaluation . . . . . . . . . . . . . . . . . 37
2.5.5 TrustworthyValue-AwareRecommenderSystems . . . . . . . . . . 37
2.6 Contribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
3 ExplainableRecommenderSystemsandBusinessValue 39
3.1 BackgroundandConcepts . . . . . . . . . . . . . . . . . . . . . . . . . . 40
3.1.1 RecommendationEvaluationMetrics . . . . . . . . . . . . . . . . 40
3.1.2 ExplainabilityonRS . . . . . . . . . . . . . . . . . . . . . . . . . 44
3.1.3 ExplainabilityEvaluationProcess . . . . . . . . . . . . . . . . . . . 48
3.1.4 Humanaspectsontheimportanceofexplanations . . . . . . . . . . 49
3.2 RelatedWork . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
3.2.1 CriteriaforExplainableRSsevaluation . . . . . . . . . . . . . . . . 51
3.2.2 MethodsforExplainableRSsevaluation . . . . . . . . . . . . . . . 53
3.2.3 MetricsforExplainableRSsevaluation . . . . . . . . . . . . . . . . 54
3.3 ProposedApproach . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
3.4 ExperimentsandResults . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
3.4.1 Dataset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
3.4.2 ExperimentalSetup . . . . . . . . . . . . . . . . . . . . . . . . . . 60
3.4.3 Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
3.4.4 Comparisonwithothermethods . . . . . . . . . . . . . . . . . . . 64
3.5 Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
3.5.1 RealWorldutility . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
3.6 Contribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
4 ExplainabilityappliedonGraph-basedRecommendationSystems 69
4.1 Backgroundandconcepts . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
4.2 Evaluatingthegraph-basedexplainablerecommenders . . . . . . . . . . . . 72
4.2.1 Currentevaluationofexplanationsingraph-basedrecommendersys-
tems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
4.3 Towardsamorestandardizedevaluation . . . . . . . . . . . . . . . . . . . 75
4.4 Contributionandfuturedirection . . . . . . . . . . . . . . . . . . . . . . 76
5 Conclusionandfutureworks 79
5.1 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
5.2 Futureworks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
References 83
x

Listing of figures
2.1 PRISMAflowdiagramrepresentingthesystematicliteraturereviewprocess. . 14
2.2 Value-awarerecommenderalgorithmtaxonomy . . . . . . . . . . . . . . . . 16
3.1 PerformanceanalysisforYelpdataset: metricscalculationfortheindividual
variationofeachregularisationterm. . . . . . . . . . . . . . . . . . . . . . 62
3.2 Performance analysis for Yelp dataset: metrics calculation for simultaneous
variationofbothregularizationterms. . . . . . . . . . . . . . . . . . . . . . 63
3.3 PerformanceanalysisforAmazondataset: metricscalculationfortheindivid-
ualvariationofeachregularisationterm. . . . . . . . . . . . . . . . . . . . 63
3.4 PerformanceanalysisforAmazondataset: metricscalculationforsimultane-
ousvariationofbothregularizationterms. . . . . . . . . . . . . . . . . . . 64
xi

xii

Listing of tables
2.1 Applicationdomainsofvalue-awarerecommendersystems. . . . . . . . . . 20
2.2 Productvalue-awarerecommendersystems. . . . . . . . . . . . . . . . . . . 25
2.3 Advertisingvalue-awarerecommendersystems. . . . . . . . . . . . . . . . . 27
2.4 Newsvalue-awarerecommendersystems. . . . . . . . . . . . . . . . . . . . 29
2.5 Mediavalue-awarerecommendersystems. . . . . . . . . . . . . . . . . . . . 31
2.6 DatasetsusedinVARSliterature. . . . . . . . . . . . . . . . . . . . . . . . 34
3.1 MostusedevaluationmetricsforRecommenderSystems. . . . . . . . . . . 42
3.2 Listoftheexplanationstyles . . . . . . . . . . . . . . . . . . . . . . . . . . 46
3.3 Mostsignificantquantitativemetricstoevaluatethequalityofexplanations. . 54
3.4 Informationaboutdatasetsusedintheexperimentandfilterappliedtoavoid
coldstartissue. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
3.5 EvaluationmetricsMF,EMFandXVMFforYelpdataset. Thehighestvalue
perindexisindicatedinbold. . . . . . . . . . . . . . . . . . . . . . . . . . 65
3.6 EvaluationmetricsMF,EMFandXVMFforAmazondataset. Thehighest
valueperindexisindicatedinbold. . . . . . . . . . . . . . . . . . . . . . . 65
4.1 Graph-BasedExplainableRecommenderSystemssurveyedfromliterature,and
groupedbyalgorithmicmethodandexplainabilityevaluationapproach. . . . 71
xiii

xiv

Listing of acronyms
CLV ........... CustomerLifetimeValue
CTR .......... Click-throughrate
EMF ........... ExplainableMatrixFactorization
E-NDCG ...... ExplainableNormalizedDiscountedCumulativeGain
GNN .......... GraphNeuralNetwork
GNNxRS ...... GNN-basedExplainableRecommenderSystem
GRS ........... Graph-basedRecommenderSystem
GxRS .......... Graph-BasedExplainableRecommenderSystem
HR ............ HitRatio
KG ............ KnowledgeGraph
MDP .......... Markovdecisionprocess
MF ............ MatrixFactorization
NDCG ........ NormalizedDiscountedCumulativeGain
NDCV ........ NormalizedDiscountedCumulativeValue
RL ............ ReinforcementLearning
RLRS ......... ReinforcementLearningRecommenderSystems
RS ............ RecommenderSystem
VARS .......... Value-AwareRecommenderSystem
xRS ........... ExplainableRecommenderSystem
XAI ........... ExplainableArtificialIntelligence
xVARS ........ ExplainableValue-AwareRecommenderSystem
XVMF ......... ExplainableValue-awareMatrixFactorization
xv

xvi

1
Introduction
In the contemporary landscape of information abundance, the pivotal role of recommender
systemshasemergedasakeytosociety’sinteractionwithdigitalcontentandservices. These
systems,drivenbyadvancedalgorithmsandartificialintelligence,playacriticalroleinassisting
userstonavigatetheabundantvolumeofchoicesandenableefficientandtailoredaccesstorel-
evantinformation,products,andexperiences. Thisintroductorychapterrepresentsaprelude
to an in-depth exploration of recommender systems in the context of business applications,
delvingintothegrowinguserneedstocomprehendbetterthesuggestionofamodel.
Over the past decade, recommender systems have gained significant attention due to their
transformativeimpactonmodernuserexperiences. Thisincreasinginterestcanbeattributed
to the convergence of several factors, such as the proliferation of online platforms, the expo-
nentialgrowthofdataavailableandcollected,andtheadvancementofmachinelearningtech-
niques. As a concrete example of this paradigm shift, consider the rise of streaming services.
These platforms leverage recommender systems to propose personalized playlists, exploiting
userpreferencesandbehaviorstocreatetailoredmusic(ormovies)recommendations.Thisnot
onlyamplifiesuserengagementbutalsoexemplifiestheefficacyofthesesystemsindelivering
highlyrelevantcontent. Moreover,thebusinessworldhasdemonstratedanincreasingaware-
nessofthepotentialofrecommendersystemsandthistrendcanbeobserved,forinstance,in
thespreadingofthee-commercesector. E-commerceheavilyreliesonrecommendersystemsto
enhancecustomerengagementandaugmentrevenue. Enterpriseclients,inturn,increasingly
seektheintegrationofthesesystemsintotheirbusinessstrategies,recognizingtheirpotentialto
1

drivesales,customersatisfaction,andbrandloyalty. Thecomplexinteractionbetweencutting-
edgetechnologiesandreal-worldprofitabilitydemonstratestheneedtoimproveandadvance
therecommendationsystem.
Inanattempttoexploitthefullpotentialofrecommendersystems,theneedfortransparency
andcomprehensibilityintheirdecision-makingprocessesisakeychallenge. Asthesesystems
evolve in complexity and sophistication, the resulting recommendations can often appear as
black box results to end users and stakeholders. This opacity prevents the creation of trust
and limits the overall usefulness of the system, generating a demand for tools to clarify the
underlyingmechanismsofrecommendationsystemsandmaketheirresultsunderstandableto
bothusersandcompanies.
Thisthesisincludesanexaminationofthestateoftheartofrecommendersystemswiththe
aimofgeneratingbusinessvaluein enterpriseapplications. Theoverallobjectiveistwo-fold:
firstly,tosurveyandsummariseexistingadvancesinthefield,andsecondly,todevelopexplain-
abilitystrategiesthatimprovetheapplicabilityofthesesystemstoreal-worldbusinessscenarios.
Afocalpointofinvestigationconcernstheoptimizationofrecommendationmodelswithre-
spect to the delicate balance between their generated value and their explanatory capabilities.
Theaspirationistoproposeadirectioninthedebatedcontextbetweentheaccuracyofrecom-
mendations and their comprehensibility, ensuring that recommendations can be interpreted
withinabusinesscontextandthussupportactionsanddecisions.
Over the past few years, a variety of families of models have emerged in the recommenda-
tionsystemlandscape,eachwithuniquestrengthsandlimitations. Value-awarerecommender
systemsstandoutinthiscontextbecausetheytakeintoaccountnotonlyuserpreferencesbut
alsotheintrinsicvalueoftherecommendeditems,thusallowingformorepreciserecommen-
dations tailored to the enterprise context. One of the most widely used approaches in this
scenarioiscalledmatrixfactorizationtechniques. Thismethodologyexploitsthelatentstruc-
turesofuser-objectinteractionmatricestoreveallatentpatternsforaccuratepredictions. In
contrast, a novel approach is the use of graph networks that natively present capabilities to
exploitintricateuser-itemrelationships,infusingrecommendationswithrichcontextualinfor-
mation,evenifnotyetusedconcretelytogeneratebusinessvalueandoptimizedexplanations
tobusinessstakeholders.
Inthisthesis,thesefamiliesofmodelswillbemeticulouslyexploredandanalyzed,evaluating
mechanisms,limitations,andtrade-offs. Leveragingtheinsightsgainedfromthisanalysis,the
researchaspirestodevelopexplainablerecommendationstrategiesthatcontributetobusiness
users’understandingoftheresultsasaneffectivesupportfortheirdailywork.
2

1.1 Research Motivation and Contribution
Thisresearchwasinitiatedwiththedesiretoestablishacollaborationbetweenacademiaand
industryinordertobringthetwoworldsclosertogetherandcaptureaspectsthatarestilllittle
discussed. TheinitiativeispromotedbyanITconsultingcompany(Estilossrl)thathasbeen
workingforyearstounderstandtheneedsofitscustomersanddriveanAI-driventransition,
recognizingthevalueandunexpressedpotentialofcorporatedata. Thepursuitofthisresearch
alignsperfectlywiththeacademiccommitmenttoresearchandthecompany’sefforttowards
innovation,realizingthetheoreticaladvancesthatbelongtothecontextofrecommendersys-
tems. Thisthesisembarksonarigorousjourneythroughtherealmofrecommendersystems
andexplanationcapabilities,beginningwithanexplorationoftheireconomicsignificanceand
culminating in a search for more effective and interpretable business-oriented models. The
followingchaptersdelveintothecomplexitiesofthesesystems,assessingthemechanismsand
analyzingtheirimpactonthebusinesslandscape,providingdirectionsforfuturesolutionsand
challengesthatcharacterizethedomainofrecommendersystemsappliedtothecontemporary
enterprise. Fourdistinctinterrelatedcontributionshavebeendevelopedtorationalizeandad-
vancethestateoftheartinthisdomain:
1. Analysis and taxonomy of Value-Aware Recommender Systems: thefirstcontribu-
tionof thisthesis consistsof a comprehensiveanalysis ofthe state ofthe artof recom-
mendersystems,focusingexclusivelyontheidentificationandcategorizationofthefam-
ilyofsystemsdesignedtogeneratevalueforcompanies,knownasValue-AwareRecom-
mender Systems (VARSs). Through a systematic literature review based on PRISMA
constraints,thevariouscategoriesandtechnicalapproacheswithinthisfamilyaregrouped
intoanoveltaxonomytofacilitatetheadoptionandunderstandingofexistingstudies.
Furthermore, the research investigates real-life applications of VARSs proposed in the
literature, analyzing the availability of different datasets that embed business value in-
formation. Finally,byrigorouslyexaminingthestrengths,limitations,andimplications
ofthesesystems,thiscontributionaimstoprovideaholisticviewoftheirapplicability
inpracticalbusinessscenarios;
2. Exploring the connection of explainability and business significance: the second
contributionexploresthecriticalaspectofexplainabilityintherealmofrecommenda-
tionsystems, particularlyinabusinesscontext. Takingfromindustryexperiencesand
existingliterature,thiscontributionexplorestheimportanceofassessingexplainability
indecision-makingprocesses. Theindustrialperspectiveexposeshowalackofexplain-
abilitycanhindertheacceptanceandadoptionofrecommendersystemsinreal-world
businesscontexts. Combiningpracticalinsightsandtheoreticalperspectives, thiscon-
3

tributionemphasizestheneedforrecommendationsthatarenotonlyaccuratebutalso
understandableandtransparenttostakeholders;
3. Bridging business value and explainability: the third contribution of this research
aimstoestablishaconnectionbetweenthecommercialvaluegeneratedbyrecommen-
dationmodelsandthedemandforexplainability. Thesearchforabalancebetweenthe
accuracyofrecommendationsandtheabilitytointerpretresultsisacentralchallengein
thefieldofrecommendationsystems. Thiscontributionfocusesonthedevelopmentof
anovelmodelthataimstobalancebusinessvalueandrecommendationexplainability,
investigatinginnovativeapproachesthatreconciletheserequirements. Theobjectiveis
tofindabalancebetweenthequantitativebenefitsandqualitativeinsightsthatrecom-
mendersystemsbringtothebusinesslandscape;
4. Explainability features in graph networks, a novel challenge: the fourth contribu-
tion of this research concerns the emerging application of explainable graph networks
inrecommendationsystems. Graphnetworks,withtheirabilitytocapturecomplexre-
lationships between items and users, have been promised to improve the accuracy of
recommendations. Thiscontributiontakesthisastepfurtherbyfocusingontheevalua-
tionofexplainabilityintegratedintograph-basedrecommendations,aimingtoimprove
transparencyanduseracceptanceofgraphnetwork-basedrecommendations. Through
anempiricalinvestigation,thiscontributionstudiesthestate-of-the-artofhowGraph-
BasedExplainableRecommenderSystems(GxRSs)isproposedandhowtheyareevalu-
ated,providingadirectionandanimprovementofrecommendationoutcomesinbusi-
nesscontexts.
Inconclusion,thisresearchexploresthemultifacetedlandscapeofbusiness-appliedrecom-
mender systems, enhancing the comprehension, effectiveness, and transparency of these sys-
tems. Throughrigorousanalysis,empiricalinvestigation,andastrategicfusionoftheoretical
andpracticalperspectives,thisthesisaimstoguidethefieldofrecommendersystemstowarda
business-orienteddirection.
1.2 Structure of the thesis
Thisthesisisorganizedasfollows: Chapter2delvesintoasystematicliteraturereviewofValue
AwareRecommenderSystems(VARS),whichconstituteamainaspectoftheresearch’sorig-
inal contributions. It explores categories and technical methodologies within the business-
orientedrecommendersystem, culminatinginthegropingintoVARSfamily. Byexamining
their real-world applications and limitations, this chapter aims to provide a comprehensive
4

overviewofVARSwithinabusinesscontext, andanovelproposedtaxonomythatorganizes
thesesystemsforenhancingcomprehension.
Subsequently,Chapter3exploresthecomplexrelationshipbetweentheexplainabilityofrec-
ommendersystemsandtheirabilitytodeliverbusinessvalue. Basedonpracticalindustrialex-
perienceandtheoreticalframeworks,itemphasizesthecrucialneedtomakerecommendation
outputstransparentandunderstandable. Furthermore,itexaminesthedifficultyofbalancing
thevalue-drivengoalsofthesesystemswiththerequirementforclearandfeasibleexplanations.
Finally,inordertofacilitatethedevelopmentofmoreefficientandvaluableenterpriserecom-
mendationmodels,thisstudyseekstoestablishaclearlinkbetweentheimportanceofbusiness
andtheabilitytoprovideadequateexplanations,providinganovelmodelthataimstoevaluate
thetrade-offbetweentheexplainabilityfeatureandthevaluegenerated.
Then, in Chapter 4, we explore the fast-growing field of graph networks, which are capa-
ble of improving the comprehensibility of recommender outcomes. Recognizing the inher-
entchallenges, weexaminehowexplainabilityfeaturescanbeincorporatedintograph-based
recommendations. Furthermore,thischapterhighlightsasignificantgapintheresearch: the
lackofauniformevaluationmethodforcomparingexplainability-enhancedgraphnetworks.
Finally,weaimtohelpestablishafoundationfortheevaluationandbenchmarkingofgraph-
basedrecommendersystemsinthecontextofexplainabilitybyexaminingtheadvantagesand
disadvantagesofthesenewtechniques.
Finally,inChapter5,weconcludewithadiscussionofthecontributionsofthisthesisand
potentialavenuesforfutureresearchinbothacademicandindustrialsettings.
1.3 Publications
PartofthecontributionofthisthesisproducedasystematicreviewunderPRISMAconstraints
[1]publishedinthejournalExpertSystemswithApplications,andapositionpaperonthequal-
ityevaluationofgraph-basedexplainablerecommendationsystemspublishedintheconference
CHItaly’23andpresentedintheHCAI4U’23workshop.
• Asystematicreviewofvalue-awarerecommendersystems. [2]
AlviseDeBiasio,AndreaMontagna,FabioAiolli,andNicolòNavarin.
ExpertSystemswithApplications,September2023.
ISSN0957-4174
doi: 10.1016/j.eswa.2023.120131
5

• Graph-basedExplainableRecommendationSystems: AreWeRigorouslyEvaluat-
ingExplanations?. [3]
AndreaMontagna,AlviseDeBiasio,NicolòNavarin,andFabioAiolli.
Proceedingsofthe15thBiannualConferenceoftheItalianSIGCHIChapter.
CHItaly’23,September2023.
1.4 Work in progress
Theconcepts, approaches, andmodelproposedinChapter3aregoingtobeformalizedina
paperandsubmittedtoaconferenceorjournal.
• XVMF:arecommendersystemdesignedtobalancebusinessprofitandexplainabil-
ityfeatures.
AndreaMontagna,AlviseDeBiasio,NicolòNavarin,andFabioAiolli.
[Conferenceorjournalforsubmissiontobedefined.]
6

2
Value-Aware Recommender System
RecommenderSystems(RSs)helpusersmakedailydecisions[4]andtheyareusedinvarious
applications, including e-commerce systems [5], news [6] and online streaming [7] services,
andadvertisingplatforms[8]. Toalleviatetheproblemofinformationoverload[9], RSsrec-
ommenditemsofgreatestinterestforuserstofocustheirattentionon. Indeed,traditionalrec-
ommendationmodelsaredesignedtoprovidepersonalizedrecommendationsrelevanttothe
user[4]. Inordertomatchcustomerpreferences,anRStypicallyaddressesaspecificobjective
[10],namely,minimizingthepredictionerrorormaximizingtherankingquality.
However, although providing products and services to satisfy customers is a fundamental
requirement for the sustainability of any business, an organization often decides to adopt a
recommender to improve business performance [11, 12]. For these reasons, in the past few
years,therehasbeenincreasedinterestinValue-AwareRecommenderSystems(VARSs)[13].
Thesesystemsaredesignedtooptimizetheeconomicvalueofrecommendationsbybalancing
theinterestsofmultiplestakeholders[14],i.e.,consumers,providers,andorganizations. Some
examplesofVARSincluderecommendersdesignedtomaximizeprofits[15],increaseuseren-
gagement[16],andimprovecustomerlifetimevalue[17].
In this chapter, we present a systematicliterature review on value-awareRSs basedon the
PRISMAguidelines[1]. MostsurveysintheRSfieldhaveinvestigatedrelateddomains,such
as multi-objective RS [18], multi-stakeholder RS [19], multi-criteria RS [20], context-aware
RS [21], and attribute-aware RS [22]. However, to the best of the authors’ knowledge, no
survey or review has focused specifically on VARSs. Therefore, we aim to help academic re-
7

searchersandindustrystakeholdersunderstandhowVARScanbeusedtooptimizevalue,the
principalapplicationdomains,openchallengestobeaddressed,andfutureresearchdirections.
Finally,thischapterrepresentsanecessarystepintheresearchbecauseitprovidesanindustrial
perspectivethatisenhancedinthefollowingchapter3throughtheintegrationofexplainabil-
ity capabilities into recommender systems and the proposal of a model that aims to balance
explainabilityperformancewithbusinessvaluegeneration.
Themaincontributionsofthischaptercanbesummarisedasfollows:
• weprovidethefirstsystematicliteraturereviewfocusedonValue-AwareRecommender
System,basedonPRISMAguidelines,bydiscussingarticlescollectedfromdifferentre-
searchstreamsandindustrialperspectives;
• wedescribethemainvaluecategoriesthataretraditionallyoptimizedbyVARSandthe
technicalapproachesusedinthedesignofthesevalue-generationalgorithms;
• wediscussthevariousapplicationdomains,themostcommonlyuseddatasets,themain
challenges,andpossiblefutureresearchdirections.
2.1 Background and Concepts
Inthissection,weintroducethebasicfactsofRSstoprovidebackgroundelementsnecessary
forbetterunderstandingtherelatedworksectionthatreportsVARSsimilaritiesanddifferences
fromothergeneralrecommenderclasses.
2.1.1 RecommendationAlgorithms
RSs are algorithms designed to offer suggestions of items of interest for users [4]. Various
service providers have deployed RSs in different domains, including e-commerce [5], online
streaming[7]andnewsservices[6]. Usersinteractwiththesesystemsthroughvariousonline
siteswhenevertheyarelookingforaproducttopurchase,newstoread,oramovietowatch.
RSs help users evaluate a large number of alternatives [9] by suggesting items that might be
of the greatest interest. These suggestions are offered to the user in the form of a ranking of
items[4]. Therankingisgeneratedbyalgorithmsthatexploitinformationcollectedexplicitly
(e.g., item ratings) or implicitly (e.g., browsing behaviour, product reviews) from the user’s
interactionwiththeplatformhostingtheservice[4].
8

TheRecommendationProblem
Therecommendationproblemcanbeformulatedprimarilyintwoways,i.e.,determiningthe
degreeofuserinterestinaparticularitem(predictionproblem)oridentifyingasetofkitems
of interest to the user (top-k recommendationproblem)[10]. Formally, in both cases, given
a set U = { u ,...,u } of users and a set I = { i ,...,i } of items, a RS is designed to
1 m 1 n
predictamatrixofscoresR^ ∈ Rm×n fromamatrixR ∈ Rm×n ofground-truthpreferences
[4,23]. Althoughitisalwayspossibletoorderthepredictedratingstoobtainarankofkitems
fortheuser,algorithmsaredevelopedspecificallyforthepredictionproblem(e.g.,matrixfac-
torization [24]) or for the top-k recommendation problem (e.g., sparse linear method [25]).
Therearetwomainmodesbywhichrecommendersystemsareevaluated[11,12],i.e.,online
A/Btestsorofflineevaluation. Onlineevaluationbasedonconversionrates(e.g., measuring
howoftenauserchoosesarecommendeditem)isthemostdirectmethodforevaluatingthe
effectivenessofanRS[11,12]. However,thesetypesofstudiesareoftendifficultinpractice
becausetheyrequireaccesstoexistingsystemswithlargeusergroups,wherepotentiallyrisky
testing can be performed that could impact the economic performance of service providers.
Therefore,theevaluationofofflineperformancebasedonhistoricaldataisgenerallypreferred
toonlinetesting[11,12]. Forthepredictionproblem, wherethealgorithmtriestoinferthe
ratingforagivenuseranditem,performanceistraditionallyevaluatedbycalculatingthepredic-
tionerror(e.g.,meanabsoluteerrorandrootmeansquareerror)[26]. Ontheotherhand,for
thetop-krecommendationproblem,sincethealgorithmoutputsalistofkitemsfortheuser,
performanceistypicallyevaluatedusingrelevanceorrankingmetrics(e.g.,precision,recall,and
normalizeddiscountedcumulativegain)[26]. Therefore, offlineevaluationprovidesanindi-
rect performance measurement [11, 12], potentially correlated with online metrics, which is
usedasaproxyforthelatter.
MainClassesofRecommenderSystems
Tosuggestthemostrelevantitems,RSspersonalizerecommendations[4]. Differentusersre-
ceive different recommendations according to their interests. Based on the type of personal-
ization,recommendersystemsareoftendividedintodifferentclasses. Oneofthebest-known
taxonomies of recommender systems [4] divides algorithms into content-based filtering (CB)
[27], collaborative filtering (CF) [28] and hybrid systems (HS) [29]. CB systems [27] suggest
itemswithcharacteristicssimilartothosewithwhichtheuserinteractedinthepast. CFsystems
[28] recommend items that other users with similar tastes have engaged with in the past. By
9

contrast,HSsystems[29]relyonacombinationoftheprevioustechniques. Inaddition,fur-
therdistinctionscanbemadewithinthistaxonomy. CFsystemsaretraditionallydividedinto
neighborhood[23]andmodel-based[30]approaches. Theformer[23]recommendnewitems
usinguser/itemsimilaritycriteria(e.g.,user-basedneighborhood,item-basedneighborhood).
Thelatter[31,32,30]learnapredictivemodelfromhistoricalratingstomakenewrecommen-
dations(e.g.,rule-basedcollaborativefiltering,latentfactorsmodels).
TypicalChallengesinRecommenderSystems
There are various advantages and disadvantages depending on the type of algorithm chosen
[4]. For example, RSs may suffer to a greater or lesser degree from the cold-start problem
[33], which occurs whenever the amount of information available is insufficient to produce
recommendations that effectively reflect the interests of new users and recommendations of
newitemsthathavenotyetbeenengagedwithbyusers. Inparticular, [34]CBmethodsare
generallymorerobusttonewitemcold-startthanareCFmethods. However,CBsoftenpro-
ducerecommendationsofitemsthatarehighlysimilartothoseengagedthusfar, preventing
theuserfromdiscoveringsurprisinglyrelevantitems. Bycontrast,HSmethodscanworkwell
incold-startsettings; however,thecomputationalcostisoftenveryhigh,anditisdifficultto
produceanexplanationoftherationalebehindtherecommendations.
2.2 Related Work
2.2.1 Value-AwareRecommenderSystems
Inthissection,weintroducetheeconomicconceptofvalue. Wealsonotethetypicaltypesof
businessvaluegeneratedbyrecommendations. Next,weprovideachronologicaloverviewof
value-awarerecommendersystems. Thesealgorithmsaredesignedtodirectlyoptimizevarious
typesofbusinessvalueofrecommendationsfororganizations.
AnEconomicPerspectiveontheConceptofValue
Fromearlyacademicdefinitionsinthemid-1950s,thetermvaluehashadmultiplemeanings,
closelyrelatedtotheapplicationscenarioconsidered. Inearlystudies, Miles[35]definesthe
concept of value by distinguishing use value, estimated value, cost, and exchange value. As
reported in the author’s research, use value is the ability to perform a certain function, i.e.,
10

considering a mobile phone, its use value is the ability to make a phone call. On the other
hand,theestimatedvalueisrelatedtothesphereofattractivenessanddesirability,e.g.,amobile
phonewithacolordisplayismoredesirablethanonewithablack-and-whitedisplay.Costvalue
is related to the economic quantity used to produce an item, e.g., the cost to produce every
componentandassembleamobilephone. Finally,exchangevalueisrelatedtotheincreasein
valueovertime,i.e.,themobilephoneaftertenyears.
Onthebasisofthesetheoreticalconcepts,authorshaveproposedalternativedefinitionsthat
focus on different factors. In some work [36, 37], the concept of the value of a product or
serviceisrelatedtotheexpectedbenefitthatthebuyerreceivesasafunctionofthepricepaid.
Forexample, ifthepurchaseofaproductproducescertainsavings, thevalueliespreciselyin
thedeltabetweenthesavingsandthepricepaid. Ontheotherhand,otherworks[38,39,40]
definevalueaccordingtocustomerperception. Accordingtothisinterpretation,thevalueof
aproductorserviceishighlydependentonfactorsrelatedtotheemotionalandsensorysphere
of the customer. For two distinct customers, the same product might have a different value
dependingontheemotions/feelingsitgenerates.
Ascaneasilybeinferredfromtheaboveconsiderations,thedefinitionofvalueisnotunique
and may differ depending on the perspective considered. The value for the user/customer is
oftenrelatedtotheconceptsofqualityandpersonalization,experienceandtrust,features,and
benefits [41, 42]. Moreover, the value for the producer/business is often linked to the loy-
altyrelationshipestablishedwiththecustomerandtheeconomicresultsofsales[43,44,45].
Therefore,whenbusinessvalueisreferredtointheliterature,itrepresentstheimpactonthe
company’seconomicindicators(e.g.,revenues,costs,margins,profits,andlosses).
OntheBusinessValueofRecommendations
Asdiscussedintheprevioussection,theconceptofvaluehasmultipledefinitionsinthelitera-
tureandislargelycontextdependent. InthefieldofRSs,arecentstudybyJannachandZanker
[11,12]proposesaheterogeneoustaxonomybasedonfivedistinctdefinitionsofbusinessvalue
thatrecommendationsmaygenerate:
• Click-ThroughRate(CTR):accordingtowhichthebusinessvalueofrecommendations
isdefinedaccordingtothenumberofuserclicks;
• AdoptionandConversionRate: accordingtowhichthebusinessvaluedependsonthe
degreeofcustomeradoptionofthesystem;
11

• SalesandRevenue:wherebusinessvalueisdefinedasafunctionoftotalsalesofproducts
andservices;
• Effects on Sales Distributions: according to which the value depends on the effects of
recommendationsonthedistributionofitemssold;
• User Engagement and Behaviour: according to which the value depends on the cus-
tomer’soverallengagementwiththeplatform.
Ascaneasilybeobserved, thebusinessvalueofrecommendationsdependsontheapplica-
tion context (e.g., product recommendation, news, ads) and the company’s business model
(e.g.,directsales,rental,subscription). Asaresult,thevalueofrecommendationscoulddiffer
dependingon,forexample,whetherthecompanysellsphysicalproductsthroughe-commerce
orsellsasubscriptionservicebystreamingvideocontent.
Somestudies[46,47,48,49,50]providequantitativeevidencebyrelatingrecommendations
tospecifictypesofvalue(e.g.,salesandrevenue,effectsonsalesanddistribution). Forexam-
ple,insomeresearch[46,47,49],theeffectofrecommendationsonthediversityofproducts
soldismeasured. Accordingtotheauthors,arecommendationsystemwouldindividuallylead
theusertoincreaseordecreasethediversityofitemspurchased. However,onaverage,recom-
mendations lead to an overall decrease in diversity in favour of the most popular items. On
theotherhand, withregardtotheeffectofrecommendationsontheoverallsalesvolume, in
theliterature[48],itisfoundthatdependingonthetypeofdesign(i.e.,collaborativefiltering,
content-based),onealgorithmcouldshowhigherperformancethananother. Furthermore,as
foundinmorerecentstudies[50],thesetwofactors,namely,diversityandsalesvolume,arecor-
related. Inparticular,greaterdiversitycorrelateswithhigherpurchaserates,averagepurchase
amounts,andcross-purchaserates.
IntroductiontoValue-AwareRecommenderSystems
PersonalizationhastraditionallyledRSstofocusontheuser[4]. Indeed,ifrecommendations
were not able to meet user needs, they would not be as successful. However, in real-world
circumstances, in addition to suggesting items of interest, the reasons a serviceprovider may
want to implement a recommendation system vary [11, 12]. As recently argued in research
onmultistakeholderrecommendersystems(MSRS)[14],RSsshouldconsidertheinterestsof
multipleparties, knownasstakeholders, togeneraterecommendations. e.g., consumerswho
receivetherecommendations,providerswhosupplyitemsbehindtherecommendations,and
organizationsthatmanagetherecommendationservice. Dependingontheperspectivefrom
12

whichtheMSRSisdesigned,recommendationswillbegeneratedtooptimizetheutilityofone
ormorestakeholders. Withinthemulti-stakeholdertaxonomy,aparticularclassofalgorithms
knownasValue-AwareRecommenderSystems(VARSs)canbedistinguished. VARSaresys-
tems that aim to directly maximize the economic value of recommendations. These include
systemsdesignedtoincreasesales,improvecustomerlifetimevalue,andoptimizeprofitability.
The strategic goal of optimizing the value of recommendations emerged with the growth
of e-business. The first studies in the VARS field [51] date to 2007. These works propose
severalmethodologiestogeneratemoreprofitablerecommendationstoincreasethebusiness
value of an organization. However, the first explicit reference to the term value-aware [52].
Intheirstudy,theauthorsintroduceVARSasafutureresearchdirectionforindustrialappli-
cations. ResearchonVARSwassubsequentlybroughttotheattentionoftheacademiccom-
munityinWorkshoponValue-AwareandMulti-StakeholderRecommendation(VAMS2017)
[13]. Theworkshopencouragedresearcherstoformulateacommonvisiononthisemerging
researchareabyinvitingthesubmissionofpapersonvarioustopics,includingvalue-awarerec-
ommendations and multi-stakeholder recommendations. After VAMS 2017, there has been
anincreaseinthenumberofspecialisedarticlesonVARS.Somestudieshaveinvestigatedhow
todesignVARSusingspecificmethodologiesincludingpost-processingapproaches[53]and
reinforcementlearningalgorithms[15]. Otherarticleshaveproposedmethodologiesthataim
tooptimiswvalueincertainapplicationcontexts,i.e.,e-commerce[15],advertising[54],news
[16] and others. Furthermore, other studies [55, 56, 53] have investigated the main benefits
andrisksofusingVARSinreal-worldcircumstances,consideringcustomerpricingpreferences,
the trade-off between profitability and accuracy, and the short- and long-term consequences
fororganizations.
2.2.2 OtherClassesofRecommenderSystemsandRelatedWorks
ResearchonVARSisanemergingtopic. However,otherRSshavebeenproposedintheliter-
aturetosolverelatedproblems. Thelatterincludethefollowing:
• Multi-ObjectiveRecommenderSystems [57]: inwhichthesystemaimstoproducerec-
ommendationsthatoptimizeseveralobjectives(e.g. accuracy,novelty,diversity)simul-
taneously;
• Multi-CriteriaRecommenderSystems[58]: inwhichthesystemexploitsauser’sprefer-
encesondifferentitemcriteria(e.g.,roomcleanliness,location,safety)toprovidebetter
suggestions;
13

Identification of studies via databases and registers Identification of studies via other methods
Rec I E A S o E r l C p d s E r M e s i E n v i g i d D X e e e p r i r g n l S o i L t t i c a r i f n e i o l e k p L d ( n u i ( b n f s r = r o a = ( m 2 r n y 2 2 : = 1 7 ( n 6 7 1 2 ) 4 = 5 5 7 ) 6 1 6 4 ) 6) Rec D N B or a u o d d p t s - l E i f r c o n e a r g m m te li o a s r v t h e t e i c n r d e o g c r b d r o e e s r f c d o ( o s r n e r d ( = n s s c 1 = ( r 6 n e 1 2 e = 8 7 n 0 3 6 in ) ) 8 g 0 : ) Rec C or i d ta s t i i o d n e n s t e if a ie rc d h f i r n o g m ( : n = 123)
Records screened (n = 28481) Records excluded (n = 28296)
Reports sought for retrieval (n = 185) Reports not retrieved (n = 0)
Reports assessed for eligibility (n = 185) Reports excluded (n = 94) Reports assessed for eligibility (n = 123) Reports excluded (n = 105)
Studies included in review (n = 109)
noitacifitnedI
gnineercS
dedulcnI
Reports sought for retrieval (n = 123) Reports not retrieved (n = 0)
Figure2.1:PRISMAflowdiagramrepresentingthesystematicliteraturereviewprocess.
• Multi-Stakeholder Recommender Systems [59]: in which the system considers the in-
terests of multiple stakeholders (e.g., consumers, suppliers, organizations) to generate
recommendations;
• Context-AwareRecommenderSystems [60]: inwhichthesystemusescontextualinfor-
mation(e.g.,location,time)toprovidepersonalizedrecommendationstotheuser;
• Attribute-Aware Recommender Systems [22]: in which the system exploits additional
user(e.g., gender), item (e.g., category), andrating (e.g., time)informationto provide
morepersonalizedrecommendations;
• Price-Aware Recommender Systems [61]: in which the system exploits the user’s price
preferencesandsensitivitytoincreasetheaccuracyofrecommendations.
There are various surveys and reviews on RSs since the research field has been studied in
thepastseveraldecades. Someoftheseworks[62]approachtheproblemfromageneralper-
spective. Othersspecialiseincertaintopics,suchasrecommendationsbasedondeeplearning
[63,64]orreinforcementlearning[65]. ManysurveysfocusondifferenttypesofRSs,suchas
multi-objectiveRS[18],multi-criteria[20],multi-stakeholder[19,59],context-aware[21,66],
attribute-aware[22]andfairness[67,68]. Asintroducedearlier,VARSdifferfromtheprevi-
ouslymentionedcategoriessincetheyaimtodirectlymaximizeeconomicvalue.Totheauthors’
14

knowledge, although there is growing interest in the literature [12, 11] on the topic of RSs’
value creation for business stakeholders, no surveys or reviews based on PRISMA guidelines
[1]focusedonVARShavebeenconducted.
2.3 Proposed Approach
Toselect studies forinclusion, we adopted the Preferred Reporting Items for Systematic Re-
viewsandMeta-Analyses(PRISMA)[1]guidelines. TherigorandcoverageofthePRISMA
selection process is recognised throughout the scientific community as an indication of high
reliabilityandquality. Below,wereporttheresearchquestionsbehindthestudy,theinforma-
tionsourcesqueried,thesearchstrategyusedtoidentifythearticles,theeligibilitycriteriaused
forselection,theoverallselectionprocess,andthelimitationsofthestudy.
2.3.1 ResearchQuestions
Thesystematicreviewaimstoanswerthefollowingresearchquestions(RQ):
• RQ1: What are the main value categories typically optimized in value-aware recom-
mendersystems?
• RQ2: Whatarethemaintechniquesusedtodesignvalue-awarerecommendersystems?
• RQ3: Whatarethemainapplicationsofvalue-awarerecommendersystems?
• RQ4: What are the main datasets used in the literature of value-aware recommender
systems?
• RQ5: Whatarethemainstate-of-the-artchallengesandfutureresearchdirections?
2.3.2 EligibilityCriteria
Onlyarticlesthatmetthefollowingeligibilitycriteria(EC)wereincluded:
• EC1: Articlesshouldfocusonvalue-awarerecommendersystems.
• EC2: ArticlesmustbeinEnglishandthefullcontentofthearticlemustbeaccessible
bytheauthors.
15

Value-AwareRecommender Algorithms
In-Processing Post-Processing
Value Objective Value Reinforcement Value Ranking Value Policy
Figure2.2:Value‐awarerecommenderalgorithmtaxonomy
.
• EC3: Articlesmustbeunique, andanyduplicatecopiesofthesamearticlearenotin-
cluded.
• EC4: Articlesmustbepeer-reviewedbyjournalsorconferences.
• EC5: Graduatethesesanddoctoraldissertationsarenotincluded.
2.3.3 SearchStrategy
Weidentifiedallarticlesinvariousonlinejournaldatabasesfrom2006to2022resultingfrom
thefollowingsearchquery(SQ):
• SQ:((”recommendersystem”OR”recommendationsystem”)AND(”value”OR”revenue”
OR ”sales” OR ”click” OR ”profit” OR ”price” OR ”customer” OR ”product” OR ”opti-
mization”OR”maximization”OR”aware”)).
To stay below the maximum number of items that could be extracted from the various
databases, it was necessary to implement operational arrangements, i.e., breaking the search
queryintodifferentsubqueries,eachexecutedinadistincttimerange.
2.3.4 SelectionProcess
As shown in the PRISMA flow diagram in Figure 2.1, a total of 2,277 articles from IEEE
Xplore, 14,566 articles from Elsevier Scopus, 7,146 articles from ACM Digital Library, and
16

21,625 articles from Springer Link were identified in this first research phase. We identified
16,273duplicaterecords,180non-Englisharticles,and680recordsthatexhibitedformatting
problems in the title and metadata that were removed. In the screening stage, the titles and
abstractsof28,481articleswereanalysed,and28,296recordswereexcludedbecausethetopics
coveredwerenotrelevanttoourstudy. Atotalof185articleswerefirstsoughtforretrievaland
thenassessedforeligibility. Atthisstage, 94articleswereexcludedafterreadingthefulltext.
Fromthissubsetofeligiblearticles,anadditional123articleswereidentifiedbysearchingfor
referencesintheirbibliography,thensoughtforretrievalandfinallyassessedforeligibility. In
thislaststage,105recordswereexcludedafterreadingthefulltext. Attheendofthisoverall
process,atotalof109studieswereincludedinthereview.
2.3.5 StudyLimitations
Themainlimitationsofthepresentstudyareasfollows:
• Articles were selected primarily from IEEE Xplore, Elsevier Scopus, ACM Digital Li-
brary, and Springer Link and from reference searches in the bibliographies of articles
thatpassedthescreeningstage.
• Unpublished articles, non-English articles, articles whose content was not accessible,
graduate theses, doctoral dissertations, commercial products, and demos were not in-
cluded.
2.4 Results
Inthissection, wepresenttheresultsofthesystematicreview. First, weclassifyanddescribe
VARSalgorithms. Then,wereviewsomeoftheworkthathasstudiedapplicationsofVARS
inthepastfewyears. Finally,wepresentthemostcommonlyuseddatasets.
2.4.1 Value-AwareRecommenderAlgorithmTaxonomy
Inthissection,weintroducethemainalgorithmsintheliteratureonVARS.Thesealgorithms
leveragedifferenttechnicalapproachesand,insomecases,dependonthenatureoftherecom-
mendedcontent. Althoughothertaxonomiesbased,forexample,onbusinessKPIsorvaluedi-
mensions,areavailableintheliterature(seeSection2.2.1),weprovideaclassificationofVARS
17

accordingtothetechnicalapproachesusedtohighlightthedifferentmechanismsunderlying
thevariousalgorithms. AsindicatedinFigure2.2,VARSalgorithmscanfirstbedividedinto
in-processingandpost-processingbasedonthetimeatwhichvalue-drivenoptimizationofrec-
ommendationsoccurs(althoughpre-processingmethodsmayalsoexist,nonehavebeenfound
intheliterature). Then, theapproachescanbefurtherdividedintovalueobjective, valuere-
inforcement,valueranking,andvaluepolicyaccordingtothespecifictechniqueused. Inthe
following,weintroduceeachoftheseapproaches.
Value-AwarePost-ProcessingAlgorithms
Post-processingalgorithmscanbeappliedtoanyrecommendationalgorithm(treatedasablack
box)tooptimizethevalueofrecommendations
Y∗
Intraditionalscenarios,arecommendersystemsuggeststouseruarank ofkitemsthat
u,k
maximizestheexpectedinterest:
∑
argmax ˆr
u,i (2.1)
Y
u,k i∈Y
u,k
bysortingthepredictedscoresˆr oftheunrateditemsindescendingorderandselectingthe
u,i
firstk. Post-processingmethodsrelyonpredictedscoresandothereconomicinformationto
reranktheoutputoftheoriginalalgorithm.
ValueRanking
ThisclassofmethodsextendstheapproachinEq.(2.1)byincorporatingeconomicvalueinfor-
mationintotheobjectivefunctiontoreranktheoutputoftheoriginalalgorithm.
∈ R
Givenavaluev associatedwithitemi(e.g.,productprofit),astrategycommonlyused
i
Y∗
bythesesystems[51,69,70,71,72,73,55,74,75,6,53]istorecommendtheset ofitems
u,k
thatmaximizetheweightedexpectedinterest:
∑
argmax ˆr · v
u,i i (2.2)
Y
u,k i∈Y
u,k
selectingthe first kitemswith the highestˆr · v. As notedin some studies [51, 69], in this
u,i i
way, it is possible to provide more profitable recommendations overall than those generated
by a traditional RS at the cost of some reduction in accuracy. However, as noted in various
works[55,75,53],theinterestsofcustomersandorganizationsmustbebalancedappropriately.
18

Clientsmayfeeldissatisfiedwithasystemthatrecommendsonlyhigh-profit,irrelevantitems,
andtheorganizationmayrisklosingloyalcustomers.
Tomitigatethisdrawback, severalstudies[72,74,6,53,76,77,78]haveproposedsimple
extensionsofEq.(2.2)toaccountfortheperspectivesofdifferentstakeholdersanddetermine
thebesttrade-offbetweeneconomicvaluefortheorganizationandcustomerinterests:
∑
argmax (1 − α)·ˆr +α · v
u,i i (2.3)
Y
u,k i∈Y
u,k
usingaregularizationparameterα ∈ [0,1]tocontroltheequation. Somevariants[70,71,75,
73]oftheapproachinEq.(2.3)havealsousedconstraintstomatchcertainconditionssuchas
theuserbudget.
ValuePolicy
Advancedpost-processingapproachesthataremorecomplexthansimplevaluerankinghave
alsobeenproposed. Werefertothesemethodsasvaluepoliciestoindicatethattheyarebased
onspecificpoliciesconsistingofmultiplestepstooptimizetheeconomicvaluederivedfrom
theentirerecommendationprocess.
Variousstudies[79,80,81]haveproposedmultiple-stepprocess-basedapproachestoopti-
mizeeconomicvalue. Forexample, onestudy[79]proposedanalgorithmthatrecommends
relevantitemstogaincustomertrustandthenrecommendsprofitableitemsoncetrustisgained
toincreasebusinessvalue. Moresophisticatedmodelshavealsobeenstudied[80]byincorpo-
ratingvariousfactorssuchasprice,profitability,productcompetition,andsaturationeffectsto
improveprofitabilityoverafinitetimehorizon. Recentwork[81]hasproposedaprobabilistic
approachtooptimizemultiplestrategicparameters(e.g.,click-throughrate,userengagement)
oneatatimeconsideringthatoptimizingoneparametercouldhavepositiveeffectsonother
valueindicatorsaswell.
Otherworks[5,82,7,83]haveproposedmethodologiesoptimizingthevalueofrecommen-
dations by integrating dynamic pricing algorithms. For example, some works [83] have pro-
posedtooptimizethediscountofrecommendeditemsbyexploitingmulti-armedbandits. By
contrast,amorerecentwork[7]hasproposedpersonalizingthepriceofrecommendedprod-
uctsbasedoncustomerwillingnesstopaytosimultaneouslyoptimizeserviceproviderprofit
andcustomersurplus.
19

| Application | Most Frequently       | Typically       | opti- Details |
| ----------- | --------------------- | --------------- | ------------- |
| Domain      | UsedTechnique         | mizedValue      |               |
| Product     | Recom- ValueObjective | SalesandRevenue | Table2.2      |
mendation
| Advertising | Value Reinforce- | SalesandRevenue | Table2.3 |
| ----------- | ---------------- | --------------- | -------- |
Recommendation ment
| News Recommen- | Value Reinforce-      | CTR,         | User Table2.4 |
| -------------- | --------------------- | ------------ | ------------- |
| dation         | ment                  | Engagement   |               |
| Media          | Recom- ValueObjective | Distribution | Table2.5      |
mendation
Table2.1:Applicationdomainsofvalue‐awarerecommendersystems.
Value-AwareIn-ProcessingAlgorithms
Whilethemethodspresentedaboveoptimizevalueafterthelearningprocess,in-processingal-
gorithmsaimtomodifyexistingortointroducenewalgorithmstogeneraterecommendations
thatoptimizevaluewithouttheneedtoperformsubsequentoperations.
ValueObjective
This class of methods contains algorithms that integrate the objective function of known or
domain-specificalgorithmstogeneratemorevaluablerecommendations.
Forexample,somework[84,85,86,87]hasproposedmodifyingthewell-knownneighbourhood
recommendersystem[23]. Theoriginalalgorithmcomputesthesimilaritybetweenusers(user-
basedapproach)oritems(item-basedapproach)belongingtoagivenneighborhoodtopredict
thescores. Aneighborhoodreferstoasetofuserswhosharesimilarinterestsorasetofitems
thathavebeenengagedwithbysimilarusers. Forexample,intheuser-basedapproach,thealgo-
| rithmcomputesthesimilaritysim(u,v)betweenauseru |     | ∈   | U   |
| ----------------------------------------------- | --- | --- | --- |
whodidnotexpressapreference
P(u,i)ofuserswhoexpressedpreferencessimilarto
foritemiandauservbelongingtoaset
uandratedi.
(2.4)
basedontheratingsoftheneighbours. Somevalueobjectivealgorithmshavebeenproposedby
partiallymodifyingthefunctioninEq. (2.4)tooptimizesometypesofeconomicvalue. For
example, some work [87] has proposed a neighbour selection algorithm to increase the over-
20

allprofitabilityofrecommendedproductswhilemaintainingaccuracyundershillingattacks,
i.e.,identifyingmalicioususerswhogeneratebiasedratingstoinfluencerecommendationsfor
their own interests. Moreover, other studies [86] have proposed increasing sales diversity by
recommendinguserstoitemsbyreversingtheoriginalneighbourcomputationalgorithm.
Furthermore,otherresearch[88,89,90,91,92]extendsthewell-knownmatrixfactorization
algorithm[24,30]byincorporatingvalueinformationintotheobjectivefunction. Inthetra-
ditionalmatrixfactorizationalgorithm,theuser-iteminteractionmatrixRisdecomposedinto
theproductoftworectangularlower-dimensionallatentspacematricesrepresentingusersand
items. Decompositionisoftenperformedusingadimensionalityreductionalgorithmknown
assingularvaluedecomposition[93].
⊺
ˆr = p q (2.5)
u,i u i
by computing the dot product between the l-dimensional latent feature vector p
∈ Rl
of
u
useruandq
∈ Rl
ofitemi. Somevalueobjectivealgorithmshavebeenproposedbyincor-
i
poratingotherfactorsintothecalculationofpredictedscoresinEq.(2.5)tooptimizecertain
typesofeconomicvalue. Forexample,someworks[88,90,91,92]haveusedpredictedscores
determinedviamatrixfactorizationandothereconomicinformationtoimprovetheutilityof
recommendedproductstotheuser.
ValueReinforcement
Recent studies have proposed value-aware recommendation algorithms by exploiting Rein-
forcementLearning(RL)[94]techniques,alearningapproachthataimstoautomaticallylearn
anoptimalpolicybasedonthesequentialinteractionsbetweenanagentandtheenvironment
throughtrialanderrortomaximizeareward. AnRLenvironmentcanbeformalisedthrough
a Markov decision process (MDP) in the tuple
(S,A,Ω,P,γ),
where
S
is a set of possible
A P
states, isasetofpossibleactions, Ωisarewardfunction, istheprobabilityoftransition
fromonestatetoanotherfollowinganactionandγ ∈ [0,1]isadiscountfactor. Typically,in
RLalgorithms,anagentinteractswiththeenvironmenttomaximizetheexpecteddiscounted
cumulativereward:
max
E[Ω(τ)]
∑τ
(2.6)
Ω(τ) = γt · ω(a,s)
t t
t=0
21

withω(a,s)astherewardfortakingactiona ∈ A instates ∈ S attimet. Theobjectiveof
t t
thealgorithmistodetermineanoptimalpolicyπ(a | s)thatinvolvestakinganactioninagiven
statetomaximizethereward.
GiventhesequentialnatureofuserinteractionwithanRS,ReinforcementLearningRecom-
menderSystems(RLRS)[65]haveemergedasalternativeapproachesbasedonRLtechniques
togeneraterecommendations.MuchoftheliteratureonVARS[95,96,16,97,17,15,98,54,8,
99,100]exploitsthismethodologytomaximizethelong-termvalueofrecommendations,im-
plementingtheagentrewardfunctionΩ(τ)inEq.(2.6)totakeintoaccountthevaluevofthe
recommendeditems. Forexample,inonestudy[95],analgorithmwasdesignedtomaximize
thecustomerlifetimevalue(CLV),i.e.,thetotalvaluegeneratedbythecustomerthroughout
his or her history. By contrast, in another study [15], the reward function was modified via
theconceptofclick-conversionrate(CVR)togeneraterecommendationsthatmaximizethe
economicvaluefromeachuseraction(e.g.,click,add-to-cart,pay).
2.4.2 Value-AwareRecommenderSystemsApplications
Recent years have witnessed growing interest in VARS. Since algorithms are often designed
basedondomain-dependentcharacteristics,inthissection,wereviewtheliteratureonVARS
invariousapplicationdomains. AsindicatedinTable2.1,theseincludetherecommendation
ofproducts,advertising,newsandmedia. Thisanalysisisproposedbecauseeachtypeofappli-
cationhasdistinctivecharacteristicsthatleadtoapreferenceforcertainmethodologiesandfor
optimizingcertaintypesofeconomicvalue. Thefollowingsectionsrefertothedetailedtables
linkedtothemaintableforamorein-depthdiscussionofindividualresearchworks.
ProductRecommendation
ManyVARShavebeendevelopedtooptimizeproductsales. Below,weprovideanoverviewof
themaintopicsaddressedintheliterature, includingtheaccuracy-profitabilitytrade-off, the
optimizationofmultipleobjectivessimultaneouslyfromamulti-stakeholderperspective,the
usefulness of recommendations for the customer, the long-term implications of value-aware
recommendations,theinfluenceofpriceonthewillingnesstopay,andreal-worldstudies.
Table2.2summarisestheliteratureonvalue-awareproductrecommendationsystems.
22

Accuracy-ProfitabilityTrade-Off
Business interest in leveraging recommender systems to increase revenue or other key perfor-
manceindicatorsofglobale-tailersexistedsincethe2000s. Inearlywork,Chenetal.[51,69]
proposedamethodologytoweighttherecommendationsofacollaborativefilteringalgorithm
withproductprofitabilityfactors(i.e.,revenuesminuscosts). Thisapproachallowsthesystem
tomeetthecustomer’sneedsandachievehigherprofitmarginsfortheorganization. However,
asobservedbytheauthors, focusingexcessivelyonprofitabilitycouldrapidlydegradetheac-
curacyofrecommendations. Whilesometechniquesbasedonconstrainedoptimization[70,
71,101,80,102]ormulti-objectivealgorithms[76,78,103,87,104,105,106,107,108,109]
havebeenproposed(seeSection2.4.1tobalancethepotentiallyconflictinginterestsofmultiple
stakeholders simultaneously, other studies [55, 53, 110, 108] have investigated the accuracy-
profitability trade-off through offline simulations. As argued by Jannach and Adomavicius
[55], theitemsthataremostimportantfortheusermaynotbethosethatproducethehigh-
estbusinessvaluefortheserviceprovider. Biasingalgorithmsinthedirectionofhigherprof-
itabilitycouldactuallyincreasemarginalitywhilemaintainingtherelevanceofrecommended
products. However,aboveacertainthreshold,theprobabilityofpurchasedropsdramatically,
andthebusinessvaluegeneratedasaresultisreduced. Takingthisreasoningtoitslogicalcon-
sequence, ZhouandZou[110]argueinatheoreticalstudythataprofit-basedrecommender
systemcouldinfluenceamarketplacebyleadingsellerstostrategicallyincreaseproductprices
tocompeteinrecommendations,leadingtoadecreaseinoverallprofitability.
OntheUsefulnessofCustomerRecommendations
Incontrasttopreviousstudies,adifferentresearchperspective[88,111,90,91,92]findsthat
theusefulnessofcustomerrecommendationsisdirectlyproportionaltothesalesperformance
oftherecommendationsystem. Infact,accordingtoleadingeconomictheories,arationalcus-
tomerwouldchooseproductsthatmaximizetheirutility. Basedonthisperspective,Wangand
Zhang [88] develop a recommendation algorithm that maximizes the net marginal utility of
recommendedproductsforthecustomerbyexploitingtheeconomicprincipleofdiminishing
marginalutility. Yangetal.[111]proposeanadaptiveassociationruleminingalgorithmtorec-
ommendthehighestutilityproducts. Bycontrast,Zhangetal.[90]designarecommendation
system that jointly optimizes the interests of customers and sellers in an online marketplace.
Thesystemoptimizescustomersurplus,definedastheamountofutilitythatacustomerob-
tainswithrespecttothepricethatheorshepays,andproducersurplus,definedastheamount
23

ofrevenuethataproducerobtainsaftercosts. Furtherdevelopingpreviousapproaches,Zhao
etal.[91]proposemaximizingtheusefulnessofrecommendationsbasedontheconceptofthe
marginalrateofsubstitution. Thealgorithmconsidersthecomplementarityandsubstitutabil-
ityoftheproductstoberecommendedtothecustomercomparedtothosealreadypurchased.
Finally,Geetal.[92]aimtooptimizetheutilityofrecommendedproductsbymaximizingthe
marginalutilityperdollar(MUD)undercustomerbudgetconstraints.
Long-TermImplicationsofValue-AwareRecommendations
Thusfar,thediscussedworkshavefocusedmostlyonoptimizingshort-termsalesperformance.
However, as argued by Jannach and Adomavicius [55] and Ghanem et al. [108], the perfor-
manceofanRSalsodependstoalargeextentonthelong-termeffectsofrecommendationson
customers. Purelyprofit-orientedstrategiesareoverlybiasedtowardstheorganization’sshort-
terminterestsandcanleadtolong-termcustomerchurn. Instead,strategiesthatbalanceprofit
withcustomerutility,andthusaremoreorientedtothecustomer’sperspective,wouldlikely
lead to sustained profitability in the long run due to more stable levels of customer satisfac-
tion. Hosanagar et al. [79] considered this factor by arguing that a recommendation system
shouldfirsttrytomaintainacertainleveloftrustbyproposingproductsthatarerelevantto
thecustomerbeforeoptimizingprofitability.AdditionalworkbyLiuandShih[120,121,119],
ShihandLiu[122]andTabaeiandFathian[123]proposedmethodologiesbasedoncustomer
lifetimevalue(CLV),apopularmetricinthemarketingandmanagementliteraturethatmea-
sures the overall value that a customer generates for the organization throughout his or her
history. However,previousstudiesfocusedontheuseofCLVtoimprovethequalityofrec-
ommendationsratherthantooptimizethelong-termvaluefortheorganization. Morerecent
works[114,96,15,115,100]haveproposeddirectlyoptimizingthelong-termperformanceof
recommendersystemsbyexploitingprobabilisticapproaches[114]orreinforcementlearning
[96, 15, 115, 100] algorithms (see Section 2.4.1). The latter have been used, for example, to
maximizethecumulativevalueobtainedviaalluseractions(i.e.,click,add-to-cart,pay)[15]or
tooptimizecustomerlifetimevalueincold-startscenarios[99].
Staticvs. DynamicPricing
ThemajorityofresearchonVARSisbasedonalgorithmsthatkeeppricesstatic. However,api-
oneeringalternativeapproachisrepresentedbysystemsthatintegraterecommendationswith
dynamicpricingalgorithms[83,112,5,82,106]. Accordingtothis philosophy, Kamishima
24

| Reference | TechniqueUsed  | optimizedValue  | Dataset        |        |
| --------- | -------------- | --------------- | -------------- | ------ |
| [51]      | ValueRanking   | SalesandRevenue | Foodmart       |        |
| [69]      | ValueRanking   | SalesandRevenue | Foodmart       |        |
| [79]      | ValuePolicy    | SalesandRevenue | N/A            |        |
| [70]      | ValueRanking   | SalesandRevenue | Self-collected |        |
| [71]      | ValueRanking   | SalesandRevenue | N/A            |        |
| [102]     | ValueObjective | SalesandRevenue | N/A            |        |
| [83]      | ValuePolicy    | SalesandRevenue | MovieLens      |        |
| [88]      | ValueObjective | UserEngagement  | Self-collected |        |
| [112]     | ValueObjective | SalesandRevenue | Self-collected |        |
| [106]     | ValueObjective | SalesandRevenue | Foodmart       |        |
| [101]     | ValueObjective | SalesandRevenue | Self-collected |        |
| [80]      | ValuePolicy    | SalesandRevenue | Self-collected |        |
| [5]       | ValuePolicy    | SalesandRevenue | Self-collected |        |
| [113]     | ValuePolicy    | SalesandRevenue | Self-collected |        |
| [82]      | ValuePolicy    | SalesandRevenue | Self-collected |        |
| [56]      | ValuePolicy    | SalesandRevenue | Self-collected |        |
| [90]      | ValueObjective | UserEngagement  | Self-collected |        |
| [91]      | ValueObjective | UserEngagement  | Self-collected |        |
| [55]      | ValueRanking   | SalesandRevenue | MovieLens      |        |
| [111]     | ValueObjective | UserEngagement  | Foodmart,      | Chain- |
|           |                |                 | Store,         | Amazon |
Review
| [96]  | ValueReinforcement | SalesandRevenue | Dunnhumby      |     |
| ----- | ------------------ | --------------- | -------------- | --- |
| [87]  | ValueObjective     | SalesandRevenue | Book-Crossing  |     |
| [114] | ValueObjective     | SalesandRevenue | MovieLens      |     |
| [104] | ValueObjective     | SalesandRevenue | Self-collected |     |
| [105] | ValueObjective     | SalesandRevenue | SPMF/Retail    |     |
| [92]  | ValueObjective     | UserEngagement  | AmazonReview   |     |
| [15]  | ValueReinforcement | SalesandRevenue | REC-RL         |     |
| [107] | ValueRanking       | SalesandRevenue | Self-collected |     |
| [78]  | ValueObjective     | UserEngagement  | EC-REC         |     |
| [103] | ValueObjective     | UserEngagement  | JD             |     |
| [115] | ValueReinforcement | SalesandRevenue | Self-collected |     |
| [53]  | ValueRanking       | SalesandRevenue | Self-collected |     |
| [116] | ValuePolicy        | SalesandRevenue | Self-collected |     |
| [100] | ValueReinforcement | SalesandRevenue | Self-collected |     |
| [99]  | ValueReinforcement | UserEngagement  | Self-collected |     |
| [109] | ValuePolicy        | SalesandRevenue | N/A            |     |
| [117] | ValueRanking       | CTR             | Self-Collected |     |
| [108] | ValueRanking       | SalesandRevenue | MovieLens      |     |
| [118] | ValueObjective     | SalesandRevenue | Self-Collected |     |
| [110] | ValuePolicy        | SalesandRevenue | N/A            |     |
Table2.2:Productvalue‐awarerecommendersystems.
25

andAkahoproposeasystemthatstrategicallyadjuststhepriceofitemsrecommendedtocus-
tomersthroughadiscountbasedonthetypeofcustomervisitingthesystem. Ifthecustomer
would purchase the product at a discounted price, the system would propose a favourable
price to obtain additional revenue. A different approach was proposed by Jiang et al. [113],
who designed a system that recommends products and simultaneously optimizes associated
promotionaldiscountstomaximizethetotalprofitgainforthecompany. Instead,Jiangand
Liu[112]optimizethediscountofpromotionalproductstoincreasetheoverallprofitability
ofnon-promotionalproducts. Theauthorsproposeexploitingintra/cross-categoryeffectsof
productspurchasedatadiscountedpricetostimulatecustomerstopurchasenon-discounted
products. Additionally,regardingpersonalizedpromotions,Zhaoetal.,[5]proposecustomiz-
ingthediscountofrecommendedproductsbasedoncustomerwillingnesstopaypredictions,
whileBeladevetal.[82]proposerecommendingproductbundlesbypricingthemtomaximize
theorganization’srevenue.
Real-WorldStudies
SomeresearchhasstudiedtheperformanceofVARSinreal-worldenvironments. Inparticu-
lar, themodeldesignedbyHosanagaretal.[79]hasbeenusedinmanyresearchworks. The
algorithm was designed according to the following assumptions: when a customer trusts an
RS, the system biases the recommendations to increase profitability; when customer trust is
belowacertainthreshold,thesystemrecommendsthemostrelevantproductstorestoretrust
attheexpenseofprofitability. Someonlinestudies[56,116]usedthisalgorithmtostudythe
sales performance of a profit-based recommender system. In particular, Panniello et al. [56],
inarandomisedfieldexperiment,showedthattheHosanagaretal.algorithmachievedhigher
revenuethanthatofacontent-basedalgorithmwithoutaffectingthecustomer’strustintheor-
ganization. Inanotherexperiment,Basu[116]foundthattherelevanceofrecommendations
andcustomertrustintheorganizationwerepositivelycorrelatedwiththerevenuegenerated
fromrecommendations.
SimilarresultswerereportedbyKompanetal.[53]inastudybasedonareal-worlde-commerce
dataset in the fashion domain. Integrating product profit factors and customer price prefer-
encesintothealgorithmscouldactuallyincreasetheprofitabilityand,insomecases,eventhe
accuracy of the recommendations. However, an excessive bias could lead to opposite effects.
Moreover,asarguedbyCavenaghietal.[117],thepriceandrankpositionofarecommended
productaretwokeyfactorsthatcaninfluenceCTRandotherbusinessvalueindicators.
26

| Reference | TechniqueUsed    | optimizedValue | Dataset        |
| --------- | ---------------- | -------------- | -------------- |
| [95]      | Value Reinforce- | UserEngagement | Self-collected |
ment
| [74]  | ValueRanking     | SalesandRevenue | Self-collected |
| ----- | ---------------- | --------------- | -------------- |
| [124] | ValuePolicy      | SalesandRevenue | Package,NBA    |
| [75]  | ValueRanking     | SalesandRevenue | Self-collected |
| [17]  | Value Reinforce- | SalesandRevenue | MovieLens      |
ment
| [54] | Value Reinforce- | UserEngagement | Self-collected |
| ---- | ---------------- | -------------- | -------------- |
ment
| [8] | Value Reinforce- | Adoption | Self-collected |
| --- | ---------------- | -------- | -------------- |
ment
| [81] | ValuePolicy | AllValues | AmazonReview |
| ---- | ----------- | --------- | ------------ |
Table2.3:Advertisingvalue‐awarerecommendersystems.
AdvertisingRecommendation
Several value-aware systems have been proposed to optimize the value of advertising. In the
following, we provide an overview of traditional systems in this field and recent perspectives
thataimtooptimizecustomerlifetimevalue.
Table2.3summarisestheliteratureonvalue-awareadvertisingrecommendationsystems.
TraditionalAdvertisingStrategies
Inadvertisingsystems,sponsoredspaceistraditionallysoldthroughauctions,wheredifferent
advertisers compete for customers’ attention. The systems often work as follows [125, 126,
8]: the advertiser first defines a subset of potential target customers based on certain demo-
graphicand/orpurchasingcharacteristics;subsequently,heorsheselectsanobjectivetoopti-
mizethroughsponsoredrecommendations(e.g., numberofclicks, add-to-cartsorgrossmer-
chandise volume); finally, the advertiser defines a bid price that he or she will pay when the
objectiveisreached. Therefore,acommonstrategyusedbyserviceproviderstomaximizesys-
tem revenues is to sort advertisers’ products into sponsored space by weighting the bid price
by click-through rate or click-conversion rate. As a result, much of the literature in the field
ofcomputationaladvertising[127,128,129,130,125,131,126,132]investigatesalgorithms
topredictthepreviousmetricsasaccuratelyaspossiblefromthecharacteristicsoftherecom-
27

mendeditems. Earlywork[127]byMicrosoftproposedaBayesianalgorithmbasedonapro-
bitregressionmodeltopredictCTRinaMicrosoftBingsponsoredsearch. Subsequentwork
describes the ad systems of Google [128], Facebook [130] and Yahoo [129], as well as the al-
gorithmsusedtoestimateCTR.MorerecentapproachesproposedbyEtsy[125]andAlibaba
[131,126,132]leverageensemblelearningmodelsandneuralnetworks,respectively,tomake
predictionsbyexploitingfeaturesassociatedwithitems(e.g., textandimages), andcustomer
purchasebehaviour.
ConsideringUserInteresttoGenerateHigherReturns
Althoughconventionaladvertisingstrategiesarewidelyadopted, alternativeapproacheshave
beenproposedtooptimizeotheraspectsofadvertising,particularlyconsideringusers’interests
[124,74,75]. Indiscriminatelypromotinghigh-profititemsthatdonotmatchusers’interests
couldpushusersawayfromthesystem.Thus,toconsiderboththeinterestsoftheorganization
andtheusers,Zhangetal.[74]proposedamethodologytobalancetherevenuegeneratedfrom
theadsofanappstoreandtheoverallqualityoftherecommendations. Thesystemoptimizes,
in the same objective function, the profit from downloading financially sponsored apps and
thenumberofdownloadsofnon-sponsoredappsrelevanttotheuser. Adoptingasimilarper-
spective: Longetal.[124]developedanalgorithmthatoptimizestheoverallprofitabilityofa
promotionalcampaignwhilemaintainingacertainnumberofsatisfiedcustomers;Malthouse
et al. [75] proposed a multi-stakeholder advertising system that jointly optimizes ad revenue
anduserutility. Consideringtheuser’sinterestsinrecommendationswouldincreasecustomer
lifetimevalueandimproveotherdriversofbusinessvalue. However,asnotedbyHeetal.[81],
maximizing multiple strategic parameters in the same objective function (e.g., click-through
rate,userengagement)couldleadtosuboptimalresultsinindividualindicators. Instead,con-
sideringthatmanyindicatorsareinterrelated,byadoptingaprobabilisticoptimizationmethod-
ology,optimizingoneparameteratatimecouldhavepositiveeffectsonotherbusinessvalues
aswell.
MaximizingCustomerLifetimeValueandAdvertiserRevenue
Aspreviouslyobserved,theinterestsofmultiplestakeholdersshouldbebalancedappropriately
to maximize customer lifetime value. Trying to increase short-term profitability with overly
biasedrecommendationscouldnegativelyimpactanorganization’sreputation. Ifthetrustre-
lationshipisbroken,somecustomersmaydecidetopurchasefromcompetitors,andthecom-
28

| Reference | TechniqueUsed    | optimizedValue | Dataset             |
| --------- | ---------------- | -------------- | ------------------- |
| [133]     | Value Reinforce- | CTR,           | User Self-collected |
|           | ment             | Engagement     |                     |
| [134]     | ValueRanking     | CTR,           | User Self-collected |
Engagement
| [16] | Value Reinforce- | UserEngagement | Self-collected |
| ---- | ---------------- | -------------- | -------------- |
ment
| [97] | Value Reinforce- | CTR | Self-collected |
| ---- | ---------------- | --- | -------------- |
ment
| [135] | ValueRanking     | UserEngagement | Self-Collected      |
| ----- | ---------------- | -------------- | ------------------- |
| [98]  | Value Reinforce- | CTR,           | User Self-collected |
|       | ment             | Engagement     |                     |
| [6]   | ValueRanking     | UserEngagement | Self-collected      |
| [136] | ValueRanking     | CTR,           | User Self-Collected |
Engagement
Table2.4:Newsvalue‐awarerecommendersystems.
panymaylosevaluablesourcesofrevenue. Toaddressthisproblem,someworks[95,17,54,8]
havestudiedhowtooptimizetheperformanceofalong-termadvertisingsystem.Insteadofrec-
ommendingtocustomersadsthathavethehighestprobabilityofbeingclicked,Theocharous
etal.[95]andHanetal.[17]proposedleveragingreinforcementlearningtechniquestoopti-
mizecustomerlifetimevalueand, moregenerally, cumulativerewardfortheplatform. Zhao
etal.[54]furtheradapteddtheapproachinthecaseofsequentialrecommendationsbypropos-
ing an approach that maximizes cumulative user engagement by balancing longer browsing
sessionsandtheclick-throughrate.
Moreover,fromamulti-stakeholderperspective,inadditiontotheinterestsofserviceproviders
andcustomers,thesystemshouldconsidertheinterestsofadvertisers. Accordingtothelatter
perspective,Guoetal.[8]proposedasystembasedonmulti-armedbanditstorecommendthe
bestadvertisingstrategytoadvertisers. Thesystemaimstoencouragetheadoptionoftheplat-
formbyhelpingadvertisersdefinecustomertargetsandbidpricestoimprovetheperformance
ofmarketingcampaignsbyreducingthecostoftrialanderror.
29

NewsRecommendation
Some value-aware recommenders have been proposed to optimize the value of news systems.
Below,weprovideanoverviewofconventionalnewsrecommendationstrategies,theexisting
relationship between click-through rate and user engagement, and the optimization of long-
termmetricstogenerategreaterreturnsfortheserviceprovider.
Table2.4summarisestheliteratureonvalue-awarenewsrecommendationsystems.
ConventionalNewsRecommendationStrategies
Thereputationofanewscompanyisdirectlyrelatedtotheimpactoftheinformationitpro-
vides on society (i.e., breaking news) [137]. The business model may be subscription-based,
advertising-based, or both. Conventionally the number of clicks or views a given news item
obtainsduringitsoveralllifespanisdirectlyrelatedtotheorganization’sreturns. Asaresult,
traditionally,companieswhosecorebusinessissharinginformationintheformofnewsmaybe
interestedingeneratinghigherprofitsbyoptimizinguserinteraction. Sincetheclick-through
rate(CTR)isdirectlyrelatedtoanorganization’srevenue,acommongoalistomaximizethe
numberofclicks. Therefore,traditionalnewsRSs[138,139]useCTRasaprimaryindicator
tofeedprobabilistictechniquestodeterminewhicharticlesmostcloselymatchthereader’sin-
terests. Thesystemsgeneratenewscandidateswiththehighestprobabilityofbeingclickedby
theusers.
OntheCTR-EngagementRelationship
Asforadvertising,althoughtheCTRmeasurestheprobabilityofclicksinthecurrentstep,it
doesnotcapturetheengagementthatmayoccurduetotheactionitself. Infact,evenifauser
clicks on an article simply for curiosity, he or she might not necessarily be interested in read-
ing it. Consequently, a growing body of work [134, 135, 6] has considered the relationship
between CTR and user engagement by proposing to optimize the latter. Besbes et al. [134]
formulatedaheuristicmethodologythatexaminestheprobabilityofclickingonanewsitem
and the engagement effect that it triggers. Specifically, they express the relationship between
clicks(thelikelihoodofclickingonanarticlewhenrecommended)andengagement(theprob-
abilityofclickingonanarticlewhenithostsarecommendation). Throughthisformulation,
thenewsisproposedalsoconsideringthefuturenavigationpathsofthecontents. Instead,Zi-
hayatetal.[135]proposedaprobabilisticmethodologythatsimultaneouslyconsidersanarti-
cle’srecentnessanduser-articleinteraction(i.e.,dwelltime)torecommendnewsbasedonuser
30

| Reference | TechniqueUsed  | optimizedValue  | Dataset        |       |
| --------- | -------------- | --------------- | -------------- | ----- |
| [140]     | ValueObjective | SalesandRevenue | Self-collected |       |
| [141]     | ValueObjective | SalesandRevenue | Self-collected |       |
| [84]      | ValueObjective | Distribution    | MovieLens      |       |
| [72]      | ValueRanking   | SalesandRevenue | Self-collected |       |
| [85]      | ValueObjective | Distribution    | MovieLens,     | Book- |
Crossing
| [89] | ValueObjective | Distribution | MovieLens      |      |
| ---- | -------------- | ------------ | -------------- | ---- |
| [86] | ValueObjective | Distribution | Netflix Prize, | Mil- |
lionSong
| [142] | ValueRanking | Distribution | MovieLens, | Net- |
| ----- | ------------ | ------------ | ---------- | ---- |
flixPrize,Jester
| [143] | ValueRanking | Distribution | MovieLens, |     |
| ----- | ------------ | ------------ | ---------- | --- |
NetflixPrize
| [144] | ValueRanking | Distribution | MovieLens, |     |
| ----- | ------------ | ------------ | ---------- | --- |
NetflixPrize
| [7]   | ValuePolicy | SalesandRevenue | Self-collected |     |
| ----- | ----------- | --------------- | -------------- | --- |
| [145] | ValuePolicy | SalesandRevenue | Self-collected |     |
Table2.5:Mediavalue‐awarerecommendersystems.
utilitycriteria. Moreover, asobservedbyLuetal.[6]andSpyridouetal.[136], newsrecom-
mendation differs from many traditional recommendation domains, such as e-commerce or
entertainment,inthatnewsorganizationshaveaclearresponsibilitytosocietytoprovidehigh-
qualityinformation.Algorithmsshouldfirstandforemostconsiderthecivicroleofjournalism
foraninformedcitizenryandoptimizetheeditorialvalueofnews(i.e.,amixofserendipity,dy-
namism,diversity,andcoverage)ratherthanlookingsolelyatCTR.
OptimizingLong-TermMetrics
Aswithothervalue-awaresystems,therelationshipbetweenvalueandtimeshouldnotbeun-
derestimated. In some cases optimizing exclusively for short-term CTR may prove counter-
productiveifthenewsprovidedisnotofinteresttotheuser. Takingthisintoconsideration,
several works [16, 133, 97, 98] have proposed methodologies to optimize long-term metrics.
Forexample,Wuetal.[16]proposeoptimizinglong-termuserengagementbymaximizingthe
totalnumberofclicksperperiodusingamulti-armedbanditsystem. Themodelalsoconsid-
ersthat, insomecases, theuser mayabandonthe systemdueto incorrectrecommendations,
31

A similar approach based on contextual bandits was originally proposed by Li et al. [133] to
maximizethetotalnumberofuserclicks. Moreadvancedapproachesbasedonreinforcement
learning have been proposed by Zheng et al. and Zou et al. [97, 98] to optimize both CTR
andlong-termuserengagementwhileconsideringtheuser’sreturnpatternontheplatformin
additiontoclickinformation.
MediaRecommendation
Somevalue-awarerecommendersystemshavebeendesignedtooptimizethevalueofmultime-
diaservices. Below,weprovideanoverviewofthemaintopicsintheliteratureconcerningthe
optimizationofuserengagement,theeffectsonthedistributionofitemswithwhichtheuser
interacts,andtheresultingincreaseinsales.
Table2.5summarisestheliteratureonvalue-awaremediarecommendationsystems.
OnTheEffectsofOptimizingUserEngagementonItemDistribution
Incontrasttoordinarygoods(e.g.,physicalproducts),movies,music,andotherdigitalgoods
arereferredtoasinformationgoodsbecausetheirproductionanddistributioncostsarenegli-
gibleandtheycanbecopied,shared,rentedorresoldeasily[7]. Aswithnewssystems,themain
businessmodelsofcompaniesprovidingmultimediaservicesarebasedoneithersubscriptions
oradvertising. Thus,especiallyforcompaniesintheentertainmentindustry,userengagement
isdirectlyrelatedtoprofits;asaresult,RSsaretraditionallydesignedwiththegoalofproviding
theuserwiththecontentofgreatestinterest[146].
However,giventheconsiderablylargeamountofcontentavailable,RSstendtorecommend
themostpopularitems,riskingboringtheuserswithpoorly-tailoredrecommendations[47,48,
49]. Tokeepusersengaged,oneofthemaintechniquesistooptimizethedistributionofrec-
ommendeditems(recalleffectsondistributionarepartofthevaluetaxonomyinSection2.2.1)
withthegoalofhelpingtheuserdiscoversurprisinglynewandrelevantitems.Thiscanbedone,
forexample,byincreasingthediversity[147]ofrecommendations[86,143,144]orpromoting
long-tailitems[84,85,89]thattendtobeproposedlessbyRSsbecauseofpopularitybias.
OptimizingSalesRevenueAccordingtotheBusinessModel
In addition to user engagement, research on media VARSs propose approaches to optimize
othervalueindicators. Someworks[72,140,141]haveproposeddomain-specificapproaches
torecommendfilmsthathavethehighestprobabilityofmaximizingsystemsalesrevenue.Azaria
32

etal.andIwataetal.proposedtwodifferentvariantsoftheirapproachdependingonwhether
thecustomerpaysasubscription(subscription-basedbusinessmodel)tohavetheopportunity
to watch several movies in a given time frame [140, 72] or a fixed price (on-demand business
model)forindividualmovies[141,72].
The importance of the value-aware approach on the overall revenues of a movie provider
based on an on-demand business model has also been studied in detail in two recent papers
[145,7].Inparticular,accordingtoZhangetal.[145],recommendationsystemsthataimsolely
atprofitoptimizationcouldproducenegativeeffectsoncustomersurplus(i.e.,thepricepaid
bythecustomerminuswillingnesstopay)andriskdrivingcustomersawayfromthecompany.
Instead, according to Najafabadi et al. [7], personalizing pricing would allow the offer to be
moretailoredto thecustomer’s willingness to payand simultaneouslycreatemore profit for
thesellersandsurplusforthecustomers.
2.4.3 Datasets
Inmanystudies,VARShavebeentrainedandevaluatedonpublicdatasets. Unliketraditional
datasets,themajorityofthelattercontaineconomicvalueinformation. Below,wepresentthe
maindatasetsusedintheliterature.
AsshowninTable2.6,mostdatasetsareusedtodesignproductormediavalue-awarerec-
ommendersystems. SomestudiesthatproposedproductVARS[51,69,111]haveexploited
theFoodMartdataset[148]. ThisisaMicrosoftSQLServer2000sampledatabaseofasuper-
market. Thedatasetcontains5,581customers,1,559products,and20,522purchasetransac-
tions. Inaddition,masterdataaboutcustomers(e.g.,country)andproducts(e.g.,brand)are
presented together with sales data (e.g., price, cost, profitability). Other studies on product
VARS [80, 87, 111, 81] have exploited different datasets crawled from Amazon [159, 149]
and Epinions [153]. These datasets are primarily based on product review data from vari-
ousproductcategoriesandcontaincustomerratings,textreviews,andproductmetadata(e.g.,
brand,category,price). Furthermore,otherworks[96,105,111]haveleveragedsupermarket
transaction datasets such as Dunnhumby [150], SPMF/Retail [151], and Chainstore [152],
whichcontaincustomer,product,andpurchasetransactioninformation. Finally,otherworks
[15,78,76,103,98]usede-commercedatasetssuchasEC-REC[78],REC-RL[15]andJD
[103]that,togetherwithcustomer,product,andpricinginformation,containuser-iteminter-
actiondata(e.g.,click,add-to-cart).
OtherstudiesthatinvestigatedmediaVARS[55,114,81,84,85,89,142,143,144,17]re-
33

| Dataset | Domain | Content |     | Availability |     |     |
| ------- | ------ | ------- | --- | ------------ | --- | --- |
FoodMart Product Contains transaction data, product https : / / github .
| [148] |     | metadata | and customer | demograph- com | / julianhyde | /   |
| ----- | --- | -------- | ------------ | -------------- | ------------ | --- |
icsofasupermarketchain foodmart-data-hsqldb
Amazon Product Contains product review data and https://nijianmo.github.
| Review[149] |     | metadata | crawled from | Amazon e- |     |     |
| ----------- | --- | -------- | ------------ | --------- | --- | --- |
io/amazon/index.html
commercesite
JD[103] Product Containsdatacollectedfromtherec- https : / / github . com /
ommendersystemslogsoftheJDChi- guyulongcs/CIKM2020_DMT
nesee-commercesite
| Dunnhumby | Product | Containstransactiondatafromasub- |     |                 |                     |     |
| --------- | ------- | -------------------------------- | --- | --------------- | ------------------- | --- |
|           |         |                                  |     | https :         | / / www . dunnhumby | .   |
| [150]     |         | setofhouseholdsthatmakefrequent  |     | com/sourcefiles |                     |     |
purchasesfromaretailer
SPMF/Retail Product Contains customer transaction data https : / / www .
| [151] |     | fromaBelgianretailstore |     | philippe-fournier-viger |     | .   |
| ----- | --- | ----------------------- | --- | ----------------------- | --- | --- |
com/spmf/index.php?link=
datasets.php
ChainStore Product Contains transaction data and prod- http : / / cucis . ece .
| [152] |     | uct metadata      | from a | supermarket northwestern | . edu             | /   |
| ----- | --- | ----------------- | ------ | ------------------------ | ----------------- | --- |
|       |     | chaininCalifornia |        | projects                 | / DMS / MineBench | .   |
html
EC-REC[78] Product Contains records of impressions, https : / / drive . google .
|     |     | clicks and | purchases | from a large- com/open?id=1rbidQksa_ |     |     |
| --- | --- | ---------- | --------- | ------------------------------------ | --- | --- |
scalee-commerceplatform mLQz-V1d2X43WuUQQVa7P8H
REC-RL[15] Product Contains user interaction data col- https : / / github . com /
lectedfromareal-worlde-commerce rec-agent/rec-rl
platform
Epinions[153] Product Containswho-trust-whomonlineso- https : / / snap . stanford .
|     |     | cial network | data from | the Epinions | soc-Epinions1 |     |
| --- | --- | ------------ | --------- | ------------ | ------------- | --- |
|     |     |              |           | edu / data   | /             | .   |
consumerreviewsite html
MovieLens Media Containsmovieratingscollectedover https://grouplens.org/
| [154] |     | varioustimeperiodsfromtheMovie- |     | datasets/movielens/ |     |     |
| ----- | --- | ------------------------------- | --- | ------------------- | --- | --- |
Lenswebsite
| Netflix Prize | Media | Contains | anonymous | movie ratings |     |     |
| ------------- | ----- | -------- | --------- | ------------- | --- | --- |
https://www.kaggle.com/
[155] fromsubscriberstotheNetflixonline datasets / netflix-inc /
movierentalservice netflix-prize-data
Book- Media Contains anonymised data of im- http://www2.informatik.
Crossing plicit/explicit book ratings from the uni-freiburg . de /
| [156] |     | Book-Crossingcommunity |     |     |     |     |
| ----- | --- | ---------------------- | --- | --- | --- | --- |
~cziegler/BX/
Million Song Media Containsaudiofeaturesandmetadata http://millionsongdataset.
| [157] |     | foroveramillioncontemporarypop- |     | com/ |     |     |
| ----- | --- | ------------------------------- | --- | ---- | --- | --- |
ularmusictracks
Jester[158] Media Containsanonymousratingsofjokes https : / / eigentaste .
|     |     | by users | of the Jester | Joke Recom- berkeley.edu/dataset/ |     |     |
| --- | --- | -------- | ------------- | --------------------------------- | --- | --- |
menderSystem
Table2.6:DatasetsusedinVARSliterature.
34

lied on the well-known MovieLens dataset [154]. This is a very popular dataset that is used
extensivelyinresearchonRSs. Thedatasetexistsinseveralversionsandcontainsmovierating
datafromthehomonymouswebsite. ThelargestversionisMovieLens25Mwhichcontains
162,000users,62,000movies,and25millionratings. Unlikethepreviousdatasets,MovieLens
doesnotexplicitlycontainproductpricingdata. Therefore,inseveralstudies[55,114,81,17],
some methodologies based on probability calculations have been proposed to add this infor-
mationtodesignVARS.Furthermore,otherstudies[84,85,89,142,143,144]haveusedthe
datasettodesignalgorithmscapableofoptimizingproductdistributionswithouttheneedto
addpricinginformation. DifferentresearchworksonmediaVARS[84,85,86,142,143,144]
haveadoptedasimilarphilosophyandarebasedonfamousdatasetsthatdonotcontainpricing
information,suchasNetflixPrize[155],Book-Crossing[156],MillionSong[157],andJester
[158].
2.5 Discussion
Value-aware recommendation systems offer many business benefits over traditional systems.
However, optimizing value brings new challenges. In this section, we discuss some of these
challengestoguidefutureresearchdirections.
2.5.1 BalancingAccuracyandProfitability
Earlystudiesintheliterature[51,69]focusedonoptimizingaparticularvaluedriverofinterest
(e.g.,CTR,sales,conversionrate). However,althoughbiasingrecommendationscaninmany
casesimprovesomekeybusinessindicators,asystemthatalwaysrecommendsirrelevanthigh-
profititemscouldhurtthecompany’sreputationbydrivingcustomersaway[55,53,110]. To
addressthisissue, manystudies[79,70,71,80,134,74,124,87,75,104,105,108]propose
algorithmstodeterminethebesttrade-offbetweenrecommendationaccuracyandvaluemaxi-
mization. Infact,toavoidlosingvaluablesourcesofrevenuefortheorganization,theRSmust
appropriatelybalancetheinterestsofallkeystakeholdergroups. Althoughseveralstudieshave
addressedthisissue,theproposedalgorithmsareoftenbasedonassumptionsaboutaparticular
typeofindustry(e.g.,retail,entertainment,insurance)[7,100]orbusinessmodel(e.g.,direct
sales, subscriptions)[140,141], andthemethodologiesarenotalwaysapplicableindifferent
contexts. Futureresearchshouldstudythisprobleminmoredetailbygeneralizingmethodolo-
gies to propose algorithms suitable for each application context. Furthermore, optimizing a
35

certaintypeofvalue(e.g.,click-throughrate)oftenaffectsotherrelatedindicators(e.g.,sales)
[81]. Studying more in-depth the correlations between the various indicators and their rela-
tionshipswithotherbusinessKPIssuchascashflowsorinventorylevels[73,160],tooptimize
other types of value for organizations as well (e.g., reducing logistics delays, cost-to-serve or
interestrates),couldbeanotherinterestingresearchdirectionforthefuture.
2.5.2 OntheLong-TermPerspectiveofValueCreation
Tobalancetheinterestsofdifferentparties,manyalgorithmshavebeenproposedbasedoncon-
strainedoptimizationtechniques. However, thesealgorithmsoftenperformpost-processing
operations to optimize short-term performancewithout consideringthe long-term effectsof
recommendations[79,55,108]. Althoughwidelyusedintheliterature,thisapproachisrisky
becauseifapotentialclientnoticesthattherecommendationsarebiased,theymaylosetrust
intheorganizationanddecidetopurchasefromcompetitors. Toaddressthisissue,reinforce-
mentlearningtechniqueshaverecentlybeenproposed[95,96,16,97,17,15,98,54,8,99,100].
In this way, the recommendation can be modeled as a sequential decision problem in which
an agent interacts with customers to maximize a cumulative reward for the organization. In
general,wethinkthattheuseofreinforcementlearningalgorithmstooptimizelong-termrec-
ommendationperformancewillbehighlyvaluedinthenextgenerationofVARS.
2.5.3 DynamicPricingforValueOptimization
Anotherimportantpointtoconsideristhevariabilityofcertaininformation(e.g.,price)that,
together with recommendations, helps influence a customer’s decision to purchase from an
onlineservice. Todate,theliteratureonVARShasprimarilystudiedhowtooptimizerecom-
mendationswhilekeepingpricesstable. Somespecializedworks[83,112,5,82,7,117]havein-
steadproposedfurtheroptimizingthesalesprocessbyintegratingdynamicpricingalgorithms
intorecommendations. Infact,thepriceofaproductisoneofthemostimportantpurchase
driversforacustomer[117,161]. Therefore,itispossibletoactonthisinformationaswellto
increaserevenueandoverallprofitabilityfortheorganization. Thestudyoftheintegrationof
dynamicpricingalgorithmsinvalue-awaresystemsiscurrentlystillinitsinfancybutcouldbe
avaluablefutureresearchdirection.
36

2.5.4 Value-AwarePerformanceEvaluation
ToevaluatetheperformanceofVARS[12,11,162],somestudies[56,116]haveperformedon-
lineA/Btests. Specifically,giventhenon-deterministicnatureofcustomerpurchasechoices,
randomisedcontrolledfieldtestsaretypicallyconsideredoneofthefewreliableperformance
evaluationmethods.However,performingthesetestsiscostlyintermsofbothtimeandmoney
onthepartoforganizations: often,anA/Btestcanlastseveralmonthsiflong-termaspectsare
to be evaluated and unexpected effects can sometimes occur, for example, due to particular
worldeventsthataffecttheresults,makingitnecessarytorerunthetest. Inaddition,apoorly
performing recommendation system could cause significant financial damage to the organi-
zationbymakingperformanceevaluationveryrisky. Thus, giventhecomplexityandcostof
conductingfieldteststoevaluateperformance,moststudiesonVARS[51,69,80,76,55,111,
131,87,114,78,105,15,81]exploitofflineapproachesbasedonpublicdatasets. However,the
mostpopularpublicdatasets[155,154]oftendonotcontainbusinessinformation(e.g.,prices,
profits),makingitdifficulttomeasurethepotentialvaluegeneratedbytherecommender. An-
otherimportantlimitationisthatitisoftenunclearunderwhatcircumstancesthedatawere
sampled. Theresultsobtainedbythealgorithmscouldthereforebeaffectedbybias,e.g.,dueto
aparticularpromotionorcertainpopulationcharacteristicsleadingtoerroneousconclusions.
Inaddition,theresultsofstudiesintheliteratureareoftennotcomparablebecausetheauthors
measureofflinevalueusingadhocmetricsorsimulationsystemsthatattempttoemulatethe
user’spurchasechoice. Asaresult, futureresearchshouldaddressthisissuetoprovidemore
reliableandsustainableperformanceevaluationmethods.
2.5.5 TrustworthyValue-AwareRecommenderSystems
Finally,likeotherAI-basedsystems,value-awarerecommendersshouldbedesignedtorespect
importantprinciplesofAItrustworthiness[163],includingalignmentwithhumanvalues,ro-
bustnessandsafety,privacypreservation,fairness[68],explainability[164]andtransparency,
reproducibility, and accountability. Studying each of these aspects in detail could be a prof-
itable research direction. Investigating how to explain VARS recommendations without de-
grading business value or studying the reproducibility of major algorithms in the literature
couldprovideinterestinghintsforfuturecontributions.
37

2.6 Contribution
ThischapterpresentedasystematicreviewofthelatestdevelopmentsinValue-AwareRecom-
menderSystems. Thesesystemshavebeenstrategicallydesignedforseamlessintegrationinto
commercial applications, aiming to enhance the economic value derived from recommenda-
tions. Value-Aware Recommender Systems find applications in diverse domains, including
e-commerceforprofitoptimization,advertisingplatformstoenhancecustomerlifetimevalue,
and online news services to maximize user engagement. The main algorithms within the lit-
eratureofvalue-awaresystemsarebasedonpost-processingtechniques,theincorporationof
objectivefunctionsfromestablishedrecommendationalgorithms,andtheapplicationofrein-
forcementlearningmethodologies.
However,ifontheonehand,thesesystemsprovidekeybenefitsforcompanies,ontheother
hand,theyintroducenewchallengessuchasappropriatelybalancingatthesametimethein-
terestsofconsumers, producers, andorganizationswhilemaintaininghighrecommendation
performanceintheshortandlongterm. Morein-depth,researchisrequiredtodesignhigher-
performingsystemsfollowingrecenttrustworthyAIprinciples,effectivelymanagepricingin-
formationtooptimizevalue,andimproveofflineandonlineperformanceevaluationmethod-
ologies.
However,whilethesesystemsoffersubstantialadvantagestoenterprises,theyalsointroduce
new challenges, such as appropriately balancing at the same time the interests of consumers,
producers, and organizations while maintaining high recommendation performance in the
short and long term. Furthermore, research is required to design higher-performing systems
followingrecenttrustworthyAIprinciples,effectivelymanagepricinginformationtooptimize
value,andimproveofflineandonlineperformanceevaluationmethodologies.
Finally,thesesystemscouldbeenhancedwiththeintegrationofexplainabilityfeaturesthat
provideusersinsightsintothesuggestionsofthemodelstomakebetterandinformeddecisions.
Inthenextchapter,wepresentexplainabilityconceptsandapplications,proposinganovelRS
model that aims to suggest items to business users, providing a balancing of value generated
andexplainabilityindices.
38

3
Explainable Recommender Systems and
Business Value
A Recommender System (RS) is a type of information filtering algorithm that provides sug-
gestionsforobjectsrelatedtoaparticularuser. However,notallrecommendationsystemsare
transparentabouthowtogeneratetheirrecommendations,whichcanaffectmultipleusercri-
teria,suchastrustandsatisfaction. Toaddressthisproblem,duringthelastdecaderesearchers
havedefinedanovelbranchofstudynamedExplainableArtificialIntelligence(XAI),inpar-
ticular,theyaimtoaddresstheproblemofusercomprehension. ExplanationsappliedtoRSs
aimtoaddressthisproblembyprovidingthereason,criteria,orevidencebehindthemodelre-
sults. Theseexplanationscanhelpusersunderstand,assess,andacceptrecommendationsand
improvedecision-makingprocesses.
Fromanindustrialperspective,thepotentialforexplanationisincreasinglyindemand,help-
ingcompaniesunderstandhowAImodelsprovideinformationandprovidingmoreinsightto
makedecisions. Theknowledgeofthesystemthatsuggestswhichactionsyoushouldtakeises-
sentialforthebuildupoftrustbetweenclients,employees,andregulators. Indeed,companies
thatadoptbestpracticestoallowexplanationcouldunderstandtheresultsandleadtheprofits,
anditcanalsoincreaseproductivitybyquicklyrevealingerrorsandareasforimprovement.
Although the potential impact of these complex systems is challenging for enterprises, it
has beenaffectedbysome limitations. One of the limitations that emerges from the current
state-of-the-art is that the more complex an AI system becomes, the harder it is to precisely
39

knowhowitobtainedaparticularinsight,especiallyifthemodelaimstoprovideexplanations
targeted to specific users. In particular, when different kinds of users (consumers, business
clients,modelers)interactwiththesemodels,theyexpecttosolveaspecificproblembasedon
multipleexplanationrequirements. Forexample,aconsumerrejectedbyabankforamortgage
wouldprobablywanttounderstandthereasonforthisdecision. Or,amarketinguserwantsto
beassistedbyanExplainableRecommenderSystemwhilepreparingamarketingcampaignfor
a specific business target, motivating why he makes these decisions (i.e., compose the proper
marketingproposalforacampaign). Duetothesignificantpotentialofthesemodels,thebal-
ancingbetweenbusinessvalueandexplainabilitywillleadtofutureindustrialresearch,helping
companiesfortheirtarget. Tothebestofourknowledge,nostudiestrytoapplyexplanations
toValue-AwareRecommenderSystem(VARS).
Inthischapter,weintroducetheconceptoftheExplainableRecommenderSystem(xRS),
review the main techniques for creating and evaluating explanations, and present literature
examplesofapplicationsforexplainingrecommendations(seesection3.1and3.2). Finally,we
propose a novel model called Explainable Value-aware Matrix Factorization (XVMF) that is,
tothebestofourknowledge,thefirsttentativetocreateamodeltargetedtodefineabalance
betweenexplainabilityperformanceandbusinessvaluegeneration,applyingXAIconceptsto
VARSs.
3.1 Background and Concepts
RecommenderSystemsrequiresaproperevaluationanalysistobecomparableandacceptable,
definingmetricstofacilitatetheselectionbystakeholders[165]. Toenhancethemotivations
providedduringthebest-modelselectionphase,explainabilitycanprovidesomeusefulinsights
andperspectives,simplifyingthecomprehensionoftheresultsandtheacceptancefromusers.
Inthissection,wereportthemainconceptsthatdescribeRSsevaluationmetricsand,inpar-
ticular,theexplainabilitymodelsstate-of-the-art,focusingontechniques,performanceindica-
tors,andhumanaspects. Thisinformationrepresentsthebasisforthecomprehensionofthe
approachproposedinthechapter,anditextendstheknowledgereportedinthechapter2.
3.1.1 RecommendationEvaluationMetrics
Recommender Systems operate in various contexts, ranging from e-commerce platforms to
contentrecommendationsinmediastreamingservices. Eachdomainintroducesdistinctchal-
40

lenges and requirements. The evaluation of recommender system models is a critical aspect
in assessing their effectiveness and suitability for diverse applications [166]. Due to the dif-
ferentnatureofrecommendationalgorithmsandtherequirementsofthespecificdomainof
applications,anexhaustiveevaluationprocessisessentialtoaccuratelydeterminethemodel’s
performanceandempowerstakeholderstomakeinformeddecisions,thusfavoringthecontin-
uous advancement of recommendation system techniques. Hence, the choice of evaluation
metricsbecomespivotalinreflectingthesystem’sperformancewithinitsspecificapplication.
An evaluation process tailored to the application domain ensures that the recommender sys-
tem aligns with user expectations, business goals, and the underlying data distribution. The
comprehensionofwhatmetricsevaluateiscrucialtounderstandbettertheneedforaproper
evaluationofthemodeldeveloped,distinguishingbetweenmeasuringbothrecommendation
resultsandexplainabilityperformance[167].
PropertiesofRecommendationSystem
AccordingtoHerlockeretal.[168]andGunawardanaandShani[169],severalpropertiescould
define a recommender system model. These important characteristics are crucial during the
selectionofasolutiontobeimplementedinanapplicationorinaproductivesystem. Inthe
last decade, most of the researchers’ effort has been on creating models that improve one or
more properties at the same time, trying to find the best trade-off and avoiding degradation
ofthesystemperformance. Variationsofapplication,experiments(onlineandoffline),dataset
improvement,anduserfeedback,aresomeofthesolutionsprovidedbyalotofscientificworks
to overcome numerous challenges. In every implementation, the developers use metrics to
compare the new models to the baseline. In table 3.1, wereport the most usedperformance
metricsamongrecommendationsystemmodels.
Accuracy Predictionaccuracyisafundamentalaspectofrecommendersystemsthathas
garneredsignificantattentionwithintherecommendationsystemliterature. Indeed,mostrec-
ommendersystemsrelyonapredictionengineresponsibleforforecastinguserpreferencesor
usageprobabilitiesoveritems. Theunderlyingassumptionisthatuserswillfavoursystemsthat
providemoreaccuratepredictions. Thispropertycomprisesthreeprimarycategories: theac-
curacyofratingpredictions,theaccuracyofusagepredictions,andtheaccuracyofrankingsof
items.
Evaluatingtheaccuracyofratingpredictionisthemainobjectiveinscenariosinterestedin
userratings(i.e.,movieratings). ThemainmetricsusedinthiscontextareRootMeanSquared
41

| Property | Focus |     | Metric |     |     | √Formula |     |     |
| -------- | ----- | --- | ------ | --- | --- | -------- | --- | --- |
∑
|     |        |     |           |      |           |     | m,n|ˆy | − |2  |
| --- | ------ | --- | --------- | ---- | --------- | --- | ------ | ----- |
|     |        |     | RMSE      | RMSE | =         | 1   |        | y     |
|     | Rating |     |           |      |           | N∑  | u,i    | ui ui |
|     |        |     |           |      | =         | 1   | m,n|ˆy | − |   |
|     |        |     | MAE       | MAE  |           |     |        | y     |
|     |        |     |           |      |           | N   | u,i ui | ui    |
|     |        |     |           |      |           |     | = TP   |       |
|     |        |     | Precision |      | Precision |     |        |       |
TP+FP
|          |       |     |           |            |        | =   | TP             |          |
| -------- | ----- | --- | --------- | ---------- | ------ | --- | -------------- | -------- |
|          | Usage |     | Recall    |            | Recall |     |                |          |
|          |       |     |           |            |        |     | T P + F        | N        |
| Accuracy |       |     |           |            |        |     | 2( Pr e cis io | n∗Recall |
|          |       |     | F-measure | F-measure= |        |     |                |          |
∑Precision+Recall
n 2reli−1
i=1 log2(i+1)
|     |     |     | NDCG |     | NDCG | = ∑ |     |     |
| --- | --- | --- | ---- | --- | ---- | --- | --- | --- |
nmax 2reli−1
i=∑1 log2(i+1)
|     | Ranking |                       |     |     |     | −   | 6 d2 |     |
| --- | ------- | --------------------- | --- | --- | --- | --- | ---- | --- |
|     |         | Spearman’sCorrelation |     |     | ρ   | = 1 |      | i   |
n(n2−1)
|     |     |     | NDPM |     | NDPM |     | = DP |     |
| --- | --- | --- | ---- | --- | ---- | --- | ---- | --- |
IDP
|     |     | PearsonCorrelation |     |     | ρ(x,y) | =   | E[x,y] |     |
| --- | --- | ------------------ | --- | --- | ------ | --- | ------ | --- |
∑
σxσy
|          |           |     |           |     | −   |          | n   | − i)· |
| -------- | --------- | --- | --------- | --- | --- | -------- | --- | ----- |
|          |           |     | GiniIndex | G = | 1   | 2        | (n  | R     |
| Coverage | Itemspace |     |           |     |     | n(n−∑ 1) | i=1 | i     |
−
|     |     |     | ShannonEntropy |     | H = | n   | p log | (p) |
| --- | --- | --- | -------------- | --- | --- | --- | ----- | --- |
|     |     |     |                |     |     | i=1 | i     | i   |
2
Table3.1:MostusedevaluationmetricsforRecommenderSystems.
Error(RMSE)andMeanAbsoluteError(MAE)[168].RMSEquantifiesthesquarerootofthe
averagesquareddifferencebetweenpredictedandactualratings,whileMAEcalculatestheav-
erageabsolutedifference. Additionally,twometricsnamedNormalizedRMSE(NRMSE)and
NormalizedMAE(NMAE) arethe normalizationversionof, respectively, RMSEand MAE
bytherangeofratings.
Onthecontrary,scenarioswhereisimportanttopredictusagebehavior(i.e.,itemselection
byuser)aresupportedbymetricslikePrecision, Recall, andF-measure[169]. Thesemetrics
helptheevaluationoftheaccuracyofpredictinginteractionsinrecommendersystems. Inpar-
ticular,precisionassessestheproportionofcorrectlypredictedselectionsamongallpredicted
ones,whileRecallmeasurestheproportionofcorrectlypredictedselectionsamongallactual
ones. Inordertosummarizetheperformanceofthetwomeasures,F-measurecanbeusedto
evaluatethebalancebetweenprecisionandrecallprovidingasinglescore.
Recommendation system output is commonly presented as a list of items in a ranked or-
derthatmustbeevaluatedbytheirpositiontoassesthefinalaccuracyofthemodel. Ranking
metricsincludemetricslikeNormalizedCumulativeDiscountedGain(NDCG),Normalized
Distance-basedPerformanceMeasure(NDPM),Spearman’scorrelation,andPearsonCorrela-
tion[169]. NDCGevaluatesrankingbyassessingthecumulativediscountedgainoftherec-
ommendeditemscomparedtoanidealranking. ItiscalculatedusingDiscountedCumulative
Gain(DCG)normalizedbytheidealDCG.Ontheotherhand,NDPMquantifiestheperfor-
42

manceofrankingitemsbyconsideringpairsofitemsandtheirrankingorders.
Coverage Coveragefocusesontheproportionoftheitemsthatthesystemcananalyzeand
producearecommendation, givingthestakeholdersinsightsintothediversityandcomplete-
ness of the results [4, 170]. A high coverage value indicates that the system can suggest the
majorityoftheitems,coversmultipleuserpreferences,andpreventstheriskofunderestimat-
ingtherealuserbehavioravoidinglimitationonthesubsetofitemsconsidered. Atthesame
time,keepingattentiontothecoveragelevelcouldintroduceuserstonovelandundiscovered
content.
Forevaluatingcoveragethetwomainmetrics,GiniIndexandShannonEntropy,offerdif-
ferentperspectivestoquantifythedistributionofrecommendationsacrossitems[169]. The
GiniIndex,commonlyemployedintheeconomicdomaintomeasurewealthdistribution,can
alsobeappliedtorecommendersystemstoquantifythedistributionofrecommendeditems. A
lowGiniIndexmeansamoreequallydistributedsetofrecommendations,anditcorresponds
toahighercoveragescore. Onthecontrary,ShannonEntropyisametricborrowedfrominfor-
mationtheoryanditassessesanuncertaintyorunpredictabilitydistributionintherecommen-
dationmodel,whereahighervalueofShannonEntropyindicatesamorediverserecommenda-
tion(bettercoverage). Bothmetricshelpassessthediversityanddistributionofrecommended
elements,ensuringthatawiderangeofoptionsispresentedtousers,andallowingevaluators
toevaluatethesystem’sabilitytointroduceuserstoawiderangeofoptions.
Finally, coverage evaluation guarantees not only to respect the diversity during the recom-
mendationprocessbutalsotoensurethediscoverycapabilitiesofthesystemwhichisessential
inreal-worldscenarios,especiallyinenterprisestrategies[101].
Others Properties In addition to the previous main properties of accuracy and cover-
age, theevaluationofrecommendersystemsisbasedonarangeofotherdimensionsthatare
equallyusefulinshapingtheuserexperienceandenhancingtheutilityoftherecommendations
provided. Thesepropertiesprovidevaluableperformanceinsightsacrossvariousperspectives,
enablingresearchersandstakeholderstomakeinformeddecisionsandimprovements. Inthe
followinglist,wereportthepropertiesthatcompletetheevaluationframeworkfordesigning
andoptimizingrecommendersystems[168]:
• Confidenceconcernsthesystem’sabilitytoquantifythecertaintyofpredictions,offering
insightintothereliabilityofitsrecommendations;
43

• Trust involves the user’s perspective in the recommendations, ensuring that users feel
secureandinformedintheirdecision-makingphase;
• Novelty and Serendipity emphasize the system’s capability to introduce users to unex-
plored and unexpected content, enriching their experience of discovering novel prod-
ucts;
• Diversitymeasuresthesystem’sabilitytosuggestadiverserangeofitems,respondingto
varioususerpreferencesandavoidingemphasizingthemostpopularitems;
• Utilityscorestherelevanceandvalueofrecommendationsaccordingtousers’needsand
preferences,enhancingusersatisfactionandengagement;
• Riskassessesthepotentialdrawbacksandconsequencesofrecommendations,ensuring
thatsystemsuggestionsdonotinadvertentlyexposeuserstoundesirableresults;
• Robustnessexaminesthesystem’sstabilityandperformanceundermultipleconditions,
maintainingitsreliabilityacrossdifferentscenarios;
• Privacyaimstoassessthesafeguardingofuserinformationwhileallowingforpersonal-
izedrecommendationsandwithoutcompromisinguserconfidentiality;
• Adaptivity focuses on the system’s capability to evolve and adjust recommendations,
basedonuserinteractionsandensuretherelevanceofsuggestionsovertime;
• Scalabilitytargetstothesystem’sefficiencyandcapabilitytohandlecomplexity(larger
datasetsanduserbases). ThispropertyisessentialinenterpriseadoptionofAIstrategies
wheretheamountofdataconstantlyincreases.
3.1.2 ExplainabilityonRS
Explainable Recommender Systems (xRSs) have become an important area of research in re-
centyearsduetotheirpotentialtoimproveusertrustandsatisfactionwithrecommendation
systems [171], facilitate system designers for better system debugging [166], and helps users
facilitate the accessto resourcesor relevantitems in an information-overloadedenvironment
[172]. Thereareseveralapproachestoimprovingexplainabilityinrecommendersystems. One
approachistousepost-hocexplainabilitymethodsthatprovideexplanationsafterarecommen-
dation has been made. Another approach is to use model-based explainability methods that
provide explanations based on the internal working methods of the recommendation model
[166].
44

xRSsattemptstodevelopmodelsthatgeneratehigh-qualityrecommendationsandintuitive
explanations. Theexplanationsmayeitherbepost-hocordirectlycomefromanexplainable
model(alsocalledinterpretableortransparentmodelinsomecontexts)[166]. Therearesev-
eraltypesofmodelsusedinexplainablerecommendations. Onemaintypeisrule-basedmodels,
which use a set of rules to make recommendations and provide explanations based on those
rules. Anothermost-usedfamilyismatrixfactorizationmodels,whichusetechniquestolearn
latentfactorsrepresentinguserpreferencesanditemattributes. Thesemodelscanprovideex-
planationsbasedonthelearnedfactors[173]. Anothertypeofmodelisthedecisiontree-based
model,whichusesdecisiontreestomakerecommendationsandprovideexplanationsbasedon
thedecisionpathstakenbythetree. Thesemodelscanbeusedforbothclassificationandre-
gressiontasks[174]. Finally,thereareneuralnetwork-basedmodels,whichuseneuralnetworks
tolearnrepresentationsofusersanditemsandcanprovideexplanationsbasedontheselearned
entities[175].
With the diffusion of the explainable model, it was fundamental to define a way to make
themcomparableandbasedonsimilarevaluationcriteria. Oneofthemostsignificantworks
aimedtosolvethisneedisfromTintarevandMasthoff[165],wheretheauthorsformalizethe
guidelinethateveryExplainableRecommenderSystemshouldbebasedon. Inthework,the
first guideline concerns the requirement of the target definition for the xRS, choosing from
transparency, scrutability, trust, effectiveness, persuasiveness, efficiency, or satisfaction. The
authors continuereminding developersand modelers not to confusethe evaluationmethods
of the explainability with those of RS, which are close but different (this is the focal point
ofthechapter4inthisthesis). Inaddition,presentationandinteractionwithexplanationsare
factorsthataffecttheachievementdegreeofthegoal.Finally,explanationstylesclassifyhowthe
explanationsaregeneratedandwhethertheyareusefulforachievingthemodelgoaldespitethe
presenceorabsenceofarecommendationmodelunderthehood.
Numerousotherworkshaverefinedtheseconceptsbyhighlightingperspectivesandappli-
cations: forinstance,Mohsenietal.[176],AdadiandBerrada[177]releasedsurveysthatcol-
lect evaluation methods for other algorithms family of intelligent systems, but not for RSs.
Moreover,ZhangandChen[166]collectsandsummarizesallstate-of-the-artapplicationsof
ExplainableRecommenderSystems. Finally,Vultureanu-AlbişiandBădică[178],Chenetal.
[172]providednovelandupdatedperspectivethroughtheirsurveysonxRS,specializingthe
primaryworkofTintarevandMasthoff[165].
45

Style Example
User CustomerswhoboughtitemAalsoboughtitemsB,C.
Item A is recommended because you highly rated or bought
Item
itemB,C.
Youmightbeinterestedinthisitembecauseyouarelookingfor
Feature
featureA(wordbased).
WesuggestitemsA,B,sincetheyareverypopularamongpeople
Popularity
similartoyou.
Social AandBalsoliketheitemC.
Pairwise personal- WeguessyouwouldlikeitemAmorethanBbecauseyoumay
ized preferCoverD.
Visual Explanationprovidedbyanimage
Table3.2:Listoftheexplanationstyles
Explanationstyles Oneoftheaspectsconcerningtheimplementationofanexplainable
model regards the presentation of the results. Explanations could be shown using different
styles to maximize the desired effect. In the literature, several styles are proposed in order to
define and enhance a specific perspective. Tintarev and Masthoff [165], for instance, collect
and define six types of style: case-based, collaborative-based [179], content-based [180], con-
versational[181],demographic-based,andknowledge-based[182].
Another perspective that aims to improve these style categories was provided by Papadim-
itriou et al. [183] and summarized by Zhang and Chen [166]. Different from the Tintarev
and Masthoff approach that distinguishes between styles and evaluation goals, the proposal
fromPapadimitriouetal.couldgiveasecondperspectiveonthestylesusedforanexplanation.
The authors create an entity-relation classification that suggests eight kinds of groups: user,
item,feature,popularity,social,pairwisepersonalized,sentence-level,andvisual(seetable3.2).
Theuser-basedmodelprovidesexplanationsbasedontheuser’spreferencesandinterests,and
it is useful for building personalized explanations that are tailored to the consumer’s needs.
Item-based approach, on the contrary, gives explanations based on the attributes of the rec-
ommended item, focusing on the item’s features and characteristics. The third main style is
feature-based,whichfocusesonhowthemodelinternallyworksandwhyitsuggestsanitemto
auser,exposinginternalfeaturesoftherecommendationmodel. Finally,hybridexplanations
aimtocombinetwoormorestylestoprovidemorecomprehensiveandinformativeexplana-
tions.
46

Presentation, Display Incorporating presentation consideration when an explanation
model provides insight to users is essential to enhance the reader experience and ensure the
effectiveness of the suggestions. Moreover, there are two approaches that model developers
could follow to influence user comprehension and acceptance: defining the appearance and
thepresentationstructure.
Firstly,consideringtheappearanceofexplanationsisessentialasitdirectlyimpactshowusers
perceivetheinformation. Itcouldbeperformedasnaturallanguagetext(arecentpromising
researchbranch),graphicalvisualization[179],orbasedonapresentationtemplate[184]such
asastructuredformtobefilledwiththeinformation.
Moreover,thedesignofthestructureisfollowedbycompanieswithprimaryinterestbecause
businessusersshouldinteractwiththeexplanationsduringtheproductivephase,leavingim-
portant feedback (implicit or explicit) in the system. It regards the design of a user interface
and user experience that aims for consistency and empowers users to seek clarification or ex-
plorealternativesbasedonpreferences. Theimplementationofauserinterfacerepresentsthe
solutiontointegratetheresultsoftheseAImodelsintotheselectionprocess,especiallyinthe
enterprisecontextwhereinsightsleadtobetterdecisionsforthebusiness.
Personalization Personalizationofexplanationsdefineswhoisthetargetuser. Whena
recommendationproposesanitemtoadifferentuser,itcouldbeexplainedindifferentways.
Herlockeretal.[179]affirmthatnon-personalizedratingsaremorepersuasivethanpersonal-
ized from users’ neighbors in preference space. On the contrary, Vig et al. [180] design tag-
basedexplanationstoimprovethepersonalizeduserexperiencebutimplyanegativeeffecton
differentdesigns. Inaddition,Guesmietal.[185]withhisworkdevelopedatransparentmodel
called Recommendation and Interest Modeling Application (RIMA) that aims to personalize
explanationswithdifferentdetaillevelstargetingtheresultsonspecifickindsofend-users. Fi-
nally,TintarevandMasthoff[184]assertthatthepositiveornegativeeffectsofanexplanation
dependonthedesignchosenforthemodel.
Explanationfocus Explanationscanalsobeclassifiedbasedonthepartoftherecommen-
dation process they are trying to explain: recommendation input, recommendation process,
recommendationoutput[186,187]. Explanationsappliedtotheinputpartoftherecommen-
dationsystemexposethesystem’shypothesisabouttheuser’sinterests,preferences,orneeds,
analyzingtheinputinformationtodriveawarenessofpersonaltastesordetectmisunderstand-
ings made by the system. Conversely, focusing on output explanations provides a justifica-
47

tionforaparticularrecommendationwithoutrevealinginternalelementsandlogic(black-box
mode). Finally,themostchallengingapproachistounderstandbetterwhatinternalprocesses
ensuretheproductionofaspecificsuggestionbytherecommendationmodel. Theexplainabil-
ityappliedtotheinternallogicprovidesthedecisionsthealgorithmmadetoproduceaspecific
itemlist. However,duetothecomplexityofthealgorithm,motivatingtheinternalprocessis
achallengingtask.
3.1.3 ExplainabilityEvaluationProcess
Evaluating the explanations produced by a model is one of the main challenges in the litera-
ture. Anexplanationmodelmustfirstaddressthetaskofevaluatingtheresultsobtained,not
only as recommendation items but also by assessing the intrinsic explanatory capacity of the
model[165]. Althoughsomestudiesaimatobjectivity, theevaluationmustrecognizethein-
trinsic relationship between articles and users, Measuring an explainability model, especially
an xRS model, numerically, requires time, assumptions, and applications. Evaluation of rec-
ommendationexplanationsisparticularlychallenging,accordingtoChenetal.[172]because
obtaining a ground truth is difficult, and it is complex to incorporate objective human emo-
tionsintoameasurementalgorithm.
The evaluation aims to define quantitative metrics that quantify the system performance
[188],suchasaccuracyorcoverage. Basically,itusesthesamemeasuresforevaluatingconven-
tionalRSadaptingthedefinitionoftherelativemetrictothenewcontext. Basedonthetypeof
experimentchosen,theevaluationcouldbegroupedintothreesets:userstudies,onlineevalua-
tions,andofflineevaluations. Userstudiesrequireexplicitfeedbackontheexplanationquality
but it is difficult to gather due to the large amount of users and their specific differences. In
this scenario, users are conscious of the study they are subjected to. On the contrary, online
evaluationhelpsthemodeltounderstandtheimplicitfeedbackthatusersgiveduringthegath-
eringphase. Realistically,itshouldbeimplementedinasystemwithalargenumberofusers
(registeredtothesystem). AnexampleofthiskindofevaluationcouldusetheClick-through
rate (CTR) to collect user feedback. Finally, the offline evaluation doesn’t require direct in-
teraction with the users and provides a score of the number of recommendations that could
beexplainedbythemodel(regardlessofthequalityoftherecommendation). Althoughthis
methodlacksdirectuserfeedback,ithastheadvantagethatthemodelcoulddirectlyevaluate
thequalityoftheoutcomeresults,dependingontheformatandtype,andcouldbecompared
toothermodels.
48

TheideabasedontheroleofhumansintheexplanationsevaluationisarguedbyEhsanand
Riedl [189] defining the concept of Human-Centered XAI, such as a mixture of human in-
teraction, cognitive psychology, and interpretable outcome, offered by the intelligent system.
Furthermore,thequalityoftheoutcomecanonlybeinterpretedbyusersinvolvingusability
studies on human subjects [188]. To perform a proper user evaluation and prepare the in-
teraction between humans and systems, some stakeholders should participate in the primary
definitionphaseofthemodelasend-users(humansthatareAIanddatanovices),andexperts
(humansthatareawareofdataandAI)[190]. Thefeedbackcollectedhasthesameimportance
valueastheratingforthetraditionalRS[191].
TheworkofMohsenietal.[176]expandstheHuman-Centeredevaluationperspective,ex-
ploringhowtheyareperceivedbyusersbycognition,interaction,satisfaction,andtrust. They
examinethecognitiveaspectsoftheexplainabilitymodel, describinghowuserscomprehend
thesystem’scapabilitiesandinteractwiththemodelresultsviaoutputandfailureprediction
ratings from a cognitive psychology perspective. Moreover, Tsai and Brusilovsky [192] con-
tributewithaworkabouttheextractionofthefeedbackfromthetextprovidedbyusersdur-
ing the approval of the recommendation. In addition, Dominguez et al. [193] consider the
RSinteractivitytobettersuitusers’needs. Furthermore,Purificatoetal.[194]combinediffer-
entexplainableinterfacestoprovideproperexplanationstousersduringtheinteractionphase,
aimingtoassesdifferentdisplayingresultsinthemostcomprehensiblestructure. Mostofthe
studiesfocusonusersatisfaction,extractingthelevelofunderstandability,fairness,usefulness,
andsufficiencyofdetailsthroughinterviews,self-reports,andquestionnaires[195,196,197].
Finally, trustisanattributethatinfluencesthesysteminapositiveornegativeway, anditre-
quirestimetobegainedbycontinuousinteractionwithusers. Itismeasuredbyaskingusers’
opinionsthroughinterviewsorquestionnaires,anditcouldobservedindirectlybyexamining
personalitytraits[198].
3.1.4 Humanaspectsontheimportanceofexplanations
The concept of explainability can be analyzed under different motivations, as proposed by
AdadiandBerrada[177]inarecentstudy. Intheirstudy,theauthorsexplorethemotivations
behindthestudyofExplainableArtificialIntelligencebydefiningfourdifferentneeds: tojus-
tify, tocontrol, toimprove, andtodiscover. Whenusersneedanexplanationofthemodel’s
resultstomakeaninformeddecision,thesystemshouldbecapableofjustifyinghowaparticu-
larresultwasachievedratherthanmerelydemonstratingthemethodsorreasoningstepstaken
49

to complete the process. Users of an explanation-capable recommendation system desire to
receiveajustificationofthesuggestedproposalwithregardtotheprocessthatledtoitsdevel-
opment. Providingexplanationsofthisnaturenotonlyenhancestheuser’sconfidenceinthe
systembutalsoimprovesthesystem’sreliability. Thisenablestheusertoacquireamorepro-
foundunderstandingofthesystem. Controlisparticularlyusefulfordevelopersbecausethey
caneasilyidentifyandsolveerrors,gainmorevisibilityintounknownvulnerabilitiesandprob-
lems,andlearnmoreaboutsystembehavior. RSsassistinmoreeffectiveinteractionbetween
users and systems by enabling better future action selection based on recommendations and
influencinguserbehaviorandsystemoutcomes. Theexplanationshaveboththeobjectiveof
orientingtheadministrationofsystembehavioraswellasinformingtheuser.Theimprovement
ofintelligentsystemsisconstantlysought, andtheneedtoconstantlyimproverecommenda-
tionsystemsisoneofthereasonswhy,inthisthesis,westudytheintegrationofexplainability.
Ifusersunderstandwhycertainrecommendationsweremade,theywillbeabletomakebetter
decisions. Evenifpeoplecannotexplaintheirdecisions,thesystemmustbeabletosupportthe
newinformationithasprovidedtothoseaffected. Accordingtothisunderstanding,explana-
tionbecomesausefultoolfordiscoveringnewelementsprovidedbyAI.
In addition, Miller [199] discusses the social significance of Explainable Artificial Intelli-
gence and identifies the sender and receiver as the two main profiles in the explanation inter-
action. Despite lacking agreement on the definitions and explanations in scientific research,
Miller presents three processes involved in explanation scenarios: cognitive, product, and so-
cial. Thefirstprocessaimstoidentifyapossiblecauseofaneventandsubsequentlyprovide
an explanation based on it. The last focuses on the human context required to interpret the
explanationintermsofexpectations,skills,andtasks,aimingtotransmittheleastamountof
informationfromtheexplainertotheexplained.
Furthermore, vanEngersanddeVries[200]proposeaframeworktoevaluatetheexplana-
tionproducedbyaXAImodelbasedonsixqualitycriteria: externalcoherence(theprobability
ofacceptanceofthedecisionincreaseswhenexplanationsarecompatiblewiththeuserknowl-
edgeofaparticularcontext),internalcoherence(sentencesmustbelogicallyconnectedtoim-
provetheexplanationandtheunderstanding), simplicity(fewandsimplecausesareeasierto
understandratherthancomplexsentences),articulation(qualityofexplanationsisinfluenced
bythelengthorwordsnumbercontainedinastatement), contrastiveness(apropertythatex-
pressestheclarityprovidedbytwoconsecutiveeventsorincertainconditions),andinteraction
(related to human-computer interaction concepts, it expresses how an explanation could be
customizedinteractivelybytheuser).
50

Moreover, Sovrano et al. [201] propose SAGE model as a discovery criteria to determine
a good path in the explanatory space. It is based on the principles of sourced (the references
thatleadtheexplanationaretheinputofthesystem),adaptation(theabilitytocreateanargu-
mentativeframeworkduringtheexploration),grounding (showingthesourceintheoriginal
format,usedforcounterfactuals),andexpansion(improvingtheexplanationwiththeproper
informationretrieved).
Finally,BarredoArrietaetal.[202]aimstoclarifytherelationshipbetweeninterpretability
(oriented to generate meaning for human beings) and explainability, in terms of an interface
between people and the decision-maker. Explanations are classified as global or local, where
globalofferscompletetransparentexplanationsandlocalexplainsaspectsofthereasoningpro-
cess[203,204].
3.2 Related Work
The idea of explaining a model is powerful, but it leads to a complexity that numerous re-
searcherssolvedbyprovidingdifferentapproachesandmodels. Inthissection,wereportthe
criteria,themethods,andthelimitationsregardingtheevaluationofExplainableRecommender
Systems. Sinceexplainabilityisimportantforthebusinessinordertogivethebestsolutionsas
ananswertoaspecificbusinessrequirement,werefertochapter2forbusinessvalueconcepts
appliedtoRSs.
3.2.1 CriteriaforExplainableRSsevaluation
Amongtheliterature,multipleapproachesareproposedtoevaluatetheexplainabilityofasys-
tem. Theevaluationelementscanbefoundunderdifferenttitlesasevaluationcharacteristics,
benefits, goals, metrics, orperspective[184,172]. However, accordingtotheguidelinespro-
posed by Tintarev and Masthoff [165], the evaluation could be properly defined as a set of
criteria and targeted one or more stakeholders (model designers, users, and providers). These
criteriaaimtostandardizethemethodbasedontheobjectiveofthealgorithms: transparency,
scrutability,trust,effectiveness,persuasiveness,efficiency,andsatisfaction.
• Transparency is one of the most significant goals for an Explainable Recommender
System,whichdirectlyaffectssomerelatedaspectsofusersatisfaction: accessibility,us-
ability,information,understanding,andauditability. Sincethelackofcomprehension
couldcauseamajormisunderstandingforusersregardingtheobjectivesofrecommender
51

systems[205], amodelshouldprovidetransparentexplanationstorevealthemainad-
vantages and disadvantages provided by the systems (embedding explanations) [206].
Model designers are the target stakeholders since explanations can reveal the internal
workingprinciplesoftherecommendermodels.
• Scrutabilityiscloselylinkedtotransparency. Althoughtransparencypaysmoreatten-
tiontodetailsinsidethemodelinordertorevealtheworkingmechanisms,ontheother
hand, scrutabilityismoreinterestedintherelationshipbetweenexplanationsandout-
puts,anditcanbeappliedproperlytoanagnosticmodel. Moreover,explanationsbased
on scrutability criteria can support both the user’s accurate argumentation and make
thesystemvalid. Indeed,inascrutablesystem(enabledbyexplanations),userscancom-
prehend the motivation on the basis of algorithmic results, and then they can control
thegeneratedrecommendationresultsbycorrectingthesystem’sassumptions. Finally,
thetargetofscrutabilitycriteriaismodeldesigners.
• Trustincreasestheuserconfidenceinthesystemandisrigidlyrelatedtotransparency.
If users understand why a particular recommendation was made, they will have more
confidenceintherecommendationsystem. Usersarethecriteriatarget.
• Effectivenesstargetstheusershelpingthemtomakequalitydecisions. Effectiveexpla-
nationswillallowtheuserto assessthequalityoftheproposeditemsmoreaccurately
onthebasisoftheirpreferences. TintarevandMasthoff[184]provideanoverviewof
evaluating the effectiveness and the metrics used in particular in the recommendation
domain.
• Persuasiveness aims to convince users to buy or try one or more items. In order to
persuadeuserstobuymoregoods(i.e.,toconvincethem),theexplanationscannotac-
curately reveal the operational mechanism of the model (i.e., transparency), but must
highlightthefeaturesthatcanpromotesales. Thefinalobjectiveistogainbenefitsfor
the system rather than for the user. Explanations may increase the user acceptance of
thesystem,aswellasoftheprovidedrecommendations. Thetargetofthiscriteriaisthe
providerofthesystemthatreceivesanimprovementfromtheapplicationofthemodel.
• Finally, there are two more criteria, both targeted to users. Efficiency helps the user
todecidefaster, givingthemthemostsuitablesuggestionsfortheitemrecommended.
Moreover, the explanation can improve user satisfaction and make the use of the rec-
ommendationsystemmorepleasant. Whenassessingthesatisfactionofexplanations,it
isimportanttodistinguishbetweenthesatisfactionoftherecommendationprocessand
thesatisfactionoftherecommendeditems.
52

3.2.2 MethodsforExplainableRSsevaluation
AfterthedefinitionofcriteriathatExplainableRecommenderSystemsshouldbetargetedto,
weneedtodefinehowtoevaluatethesystemandtheobjectivetomeasure. Theseevaluation
methods are grouped into four chunks: qualitative, quantitative, crowdsourcing, and online
experiments.
Qualitative evaluations consist of case studies designed by model designers and provide
comprehension of intuitive aspects. Although the objective is improving effectiveness and
transparencycriteria, theyareaffectedbybiasandbytheabsenceofnotcomparablefeatures
[172].Wediscussthislimitationdeeplyinchapter4,providingsymptomsofmostoftheactual
Graph-BasedExplainableRecommenderSystem,andpossiblesolutions.
Quantitativeevaluationsaimtoevaluateofflinemodelsthroughtheuseofspecificmetrics,
ensuringeffectivenessandscrutabilitycriteria[172]. Usingmetricsasasourceofevaluationof-
fersmodeldevelopersadvantagesduringthephaseofcomparingthedevelopedsolutionwith
thosebelongingtothestate-of-the-art. Atthesametime,theuseofobjectivemetricsfacilitates
theselectionphasebycorporatesuppliersinterestedinimplementingthesesolutionsinapro-
ductionenvironment. Theadvantagesofthesemethodsareefficiencyatthecomparisonstage
(i.e.,ensuringthatmodelperformanceisaboveathreshold),quantitativeaspects,andeaseof
benchmarking. Incontrast,measuringexplanationswithoutappropriatemetrics(i.e.,usingan
unsuitablemetricproposedtosolveanon-similarapplication)coulddeviatefromtheprimary
goalsoftheexplanationandproducelesseffectiveresultsduetoapproximation. Wecollectthe
numerousmetricsdefinedinthestate-of-the-artintable3.3(seesection3.2.3).
Differentfromqualitativeevaluationbasedontheusecases,crowdsourcingimpliestheac-
tivepresenceofaheterogeneousstudypopulationthatextractsrealhumanfeeling. Sincethis
methodwouldputtherightattentiontotheuserinteractionwiththesystem,studyingdeeply
causesandeffectsonhumans, itdemandsasignificantcostfortheexperimentationset. The
issueofcostissignificantinanindustrialenvironment,wherethedifferencebetweenaccepting
orrejectingaprojectliespreciselyinthetimeandcostinvolvedversusthereturnoninvestment
thatcanbeachieved. Thecriteriaaddressedareeffectivenessandscrutability(asinquantitative
evaluation),transparency(asinqualitativeevaluation),andpersuasiveness. Itcanalsobeper-
formedonpublicdatasets, constructeddatasetsorannotationinjectionsintopublicdatasets
[172].
Similarly to crowdsourcing, online experiments aim to collect user feedback in real-time,
producing a highly reliable result at a significant cost of the experiment, although the crite-
53

|                           |                      | Metrics |                                 | EvaluationObjective     | References |
| ------------------------- | -------------------- | ------- | ------------------------------- | ----------------------- | ---------- |
|                           |                      | BLEU    |                                 | userreviewwords         | [209]      |
|                           |                      | ROUGE   |                                 | userreviewwords         | [210]      |
| UniqueSentenceRatio(USR)  |                      |         |                                 | userreviewdiversity     | [211]      |
| FeatureCoverageRatio(FCR) |                      |         |                                 | userreviewdiversity     | [211]      |
|                           | FeatureDiversity(FD) |         |                                 | userreviewdiversity     | [211]      |
|                           |                      | PN,PS   | necessity,sufficiencyofafeature |                         | [208]      |
|                           | MEP,MER,EP           |         |                                 | user-itemexplainability | [173]      |
|                           | ModelFidelity        |         |                                 | user-itemexplainability | [212]      |
|                           |                      | E-NDCG  |                                 | user-itemexplainability | [213]      |
|                           |                      | NR2     |                                 | user-itemexplainability | [214]      |
LIR,LID,SEP,SED,PTD,PTC recency,diversity,popularity [215,216]
Table3.3:Mostsignificantquantitativemetricstoevaluatethequalityofexplanations.
ria aim to enhance effectiveness and persuasiveness. The explorations of the user acceptance
affected by the explanations (i.e., using A/B tests, evaluating the Click-through rate and the
conversionrate),areexploredbyZhangetal.[207].
3.2.3 MetricsforExplainableRSsevaluation
Inliterature,someworksproposedmetricstoevaluatedifferentquantitativeperspectivesofthe
model’sexplainabilitycapabilities. Onepointtoconsiderisdistinguishingbetweenassessing
themodel-generatedexplanationperformanceandtherecommendationoutcomes(seechap-
ter4). Regardingexplainableevaluation,authorsdefinedmetricstocountwords(i.e.,BLEU
and ROUGE index evaluate natural language explanations comparing the results with user
reviews), to evaluate diversity (i.e., Unique Sentence Ratio (USR), Feature Coverage Ratio
(FCR),FeatureDiversity(FD)),andtopredictfeatures(i.e.,Feature-levelPrecision(FP),Re-
call(FR),andF1score(FF)).Furthermore,Tanetal.[208]suggesttwoindexesnamedProb-
ability of Necessity (PN) and Probability of Sufficiency (PS), that estimate the necessity and
sufficiencyofafeatureiftheitemis,respectively,removedorstillinthesuggestionslist.
Explainable Matrix Factorization Researchers studied different recommendation
systemalgorithmclasses(i.e., Content-Based, CollaborativeFiltering, Knowledge-Based, Hy-
brid, andNeural), identifyingandstudyingadvantages, methods, andchallenges. Alongside
theclassicapproachesbuiltonthedecisiontree,rule-based,orBayesianalgorithms,MatrixFac-
torization(MF)isafamilyofmodel-basedmethodsappliedtocollaborativefilteringRSthat
54

primarilyhastheadvantageofproducinglatentfeaturesthatdiscerntheconnectionbetween
articleentitiesandusers.
Oneofthemostinterestingworksthataimstoembedexplainablecapabilitiesintoamatrix
factorization-basedrecommendersystemisproposedbyAbdollahiandNasraoui[173],where
theauthorsoptimizetheperformanceofthemodelsfromtwoperspectives:recommendations
system results and the explainable capabilities to the users. Indeed, Abdollahi and Nasraoui
propose to measure the performance of the explanations generated by the algorithm using a
quantitativeapproach,enhancingtheevaluationoftheRSmodelwithanewuser-centricper-
spective. Thetwoproposedindices,MeanExplainabilityPrecision(MEP)andMeanExplain-
ability Recall (MER), are based on the capability of the system to explain a suggestion using
theneighborhoodofauser(underspecificconstraints). Bothmeasuresarethemeanacrossall
testingusers,respectively,ofExplainabilityPrecision(EP)andExplainabilityRecall(ER).
TheprecisionEPiscalculatedastheratiobetweenthenumberofexplainableitemsinthe
top-nrecommendationlistandthetotalrecommendeditemsforeachuser:
| ∑     | |{ ∈       | }|  |       |
| ----- | ---------- | --- | ----- |
| 1     | i : i L ,E | > 0 |       |
| =     | u          | ui  |       |
| MEP   |            |     | (3.1) |
| | U | | N          |     |       |
u∈U
whereUisthesetofallusers,iisanitemoftherecommendationlistL (providedtouseru),
u
andNisthenumberofrecommendeditems.
Additionally,tocalculateER,ittakestheratiobetweenthenumberofexplainableitemsin
thetop-nrecommendationlistandthetotalnumberofexplainableitemsforgivenusers[173]:
∑
|       | |{ : ∈ ,E | > }| |       |
| ----- | --------- | ---- | ----- |
| 1     | i i L u   | ui 0 |       |
| MER = |           |      | (3.2) |
| |
| U   | W   |     |     |
| --- | --- | --- | --- |
u∈U
whereUisthesetofallusers,iisanitemoftherecommendationlistL (providedtouseru),
u
andWisthenumberofexplainableitems.
To implement this concept into the basic matrix factorization objective function, the au-
thorsaddanadditionalregularizationtermnamedExplainabilityPowerE ij asameasureofhow
manynearestneighborsforauser(withasimilarprofile)highlyratedanitem,constructinga
matrixEthatexposetheexplainabilitypowercalculatedwiththefollowingformula:
∑
|     | ×| NNk(u) | |   |       |
| --- | --------- | --- | ----- |
| E = | r         |     | (3.3) |
| u,i |           | i,r |       |
∀r∈R,r≥Pτ
55

whereiisanitemforaspecificuseru,ristheratinggivenbyuserutoitemi,andNNk(u)
i,r is
thekentitynearestneighboursofuseru[213].
Moreover, the standard matrix factorization objective function is enhanced with the new
regularizationterm,asformulatedin:
∑
β
|     |      |     | −      |     | (∥ ∥2 | +∥ ∥2)+λ |     | ∥ − ∥2E |       |
| --- | ---- | --- | ------ | --- | ----- | -------- | --- | ------- | ----- |
| G   | =    | (r  | a bT)2 | +   | a     | b        |     | a b     | (3.4) |
|     | expl |     | ui u   | i   | u     | i        |     | u i ui  |       |
2
u,i∈R
where i is the item rated by user u, R is the set of ratings r , a and b are the two terms to
|     |     |     |     |     |     |     | ui u | i   |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
regularizethecontributionofuseruanditemitotheobjectivefunction,andE containsthe
ij
informationofthenearestneighbors(withsimilarprofile)forauseru.
Then,tominimizetheobjectivefunctionG (seeEq.3.4),authorsusedthestochasticgra-
expl
dientdescentapproachappliedtothetwofollowingrules:
|     |     |     | (      |          |        |          |     | )     |       |
| --- | --- | --- | ------ | -------- | ------ | -------- | --- | ----- | ----- |
|     | a ′ | = a | +η 2(r | − a      | bT)b − | βa − λ(a | −   | b)E   | (3.5) |
|     |     | u   |        | ui u     | i      | u        | u   | i ui) |       |
|     | u   |     | (      |          | i      |          |     |       |       |
|     | b ′ | = b | +η 2(r | − a bT)a | −      | βb +λ(a  | −   | b)E   | (3.6) |
|     |     | i   |        | ui u     | u      | i        | u   | i ui  |       |
|     | i   |     |        |          | i      |          |     |       |       |
whereηisthelearningrateretrievedfromtheminimizationcomputationofthegradientde-
scendant,βcontrolsthemagnitudeofthelatentvectors(useranditem),andλaimstocontrol
theexplanationmatriximpact.
Finally,themodelproposedbyAbdollahiandNasraouiwasgeneralizedbyPeakeandWang
[212]proposingthemodelFidelityscore asthepercentageofexplainableitemsintherecom-
mendationlist.
Explainable-NDCG RelyingontheworkbyAbdollahiandNasraoui,Cobaetal.[213]
introduceanenhancedmodelnamedNovelEMF(NEMF)thataimstofindthetrade-offbe-
tweenthenoveltyofanitemandtheexplainabilitycapability. Inaddition, theynoticedthat
theMEPmetricassignsinaccuraterankingpositionsoftheexplainableandrecommendation
items,proposinganewmetricnamedExplainableNormalizedDiscountedCumulativeGain
(E-NDCG),basedonNDCGandabletopreciselyidentifyexplainableitems.
StartingfromtheNDCGformula3.7,theauthorsconsiderthepositionoftherecommended
itemL (seeEq. 3.1)duringtheevaluationoftheexplainabilitypowerforuseruanditemi.
u
IfNDCGisformalizedwith:
DCG
|     |     |     |     |      | =   | u   |     |     |       |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | ----- |
|     |     |     |     | NDCG |     |     |     |     | (3.7) |
IDCG
56

thenovelE-NDCGproposedbyCobaetal.isdefinedby:
E–DCG
E–NDCG = u (3.8)
E–IDCG
Thetwotermsoftheratioaredefinedbythefollowingequations:
∑N
E
E–DCG = E +
u,li
(3.9)
u u,l1 log (i)
i=1 2
∑N
E
E–IDCG = E + max (3.10)
max log (i)
i=1 2
wherelisanitemofthelistL ,andE istheexplainabilitypower,whileE istheexplain-
u u,l max
abilitypowerconsideringallrecommendeditemsinthelistL .
u
Consideringthetwodistinctobjectivefunctionsaimedtomaximizeexplanationandnovel:
∑
β
G = (r − a bT)2 + (∥ a ∥2 +∥ b ∥2)+λ ∥ a − b ∥ E (3.11)
expl ui u i 2 u i u i ui
u,i∈R
∑
β
G = (r − a bT)2 + (∥ a ∥2 +∥ b ∥2)+θ ∥ a − b ∥ N (3.12)
novel ui u i 2 u i u i ui
u,i∈R
Coba et al. formalized the objective function that describes the Novel Explainable Matrix
Factorization(NEMF)modelasfollows:
∑
β
G = (r − a bT)2 + (∥ a ∥2 +∥ b ∥2)+∥ a − b ∥(λE +θN ) (3.13)
expl&novel ui u i 2 u i u i ui ui
u,i∈R
where the final results depend on both explainable and novel elements traded off of the two
hyperparameters(λandθ),anda andb componentsareformulatedas:
u i
( )
a ′ = a +η 2(r − a bT)b − βa − sgn(a − b)(λE +θN ) (3.14)
u u ( ui u i i u u i ui ui)
b ′ = b +η 2(r − a bT)a − βb +sgn(a − b)(λE +θN ) (3.15)
i i ui u i u i u i ui ui
57

3.3 Proposed Approach
CompaniesincreasinglyrelyonAItoolstosupporttheirdecisionsandmaximisebusinessvalue
(see Chapter 2,). However, understanding by non-expert users is a limitation and a current
challengeinordertoenhancetheadoptionofthesesystems. Inparticular,withourwork,we
want to support this business phase through the creation of a model that, to the best of our
knowledge,isthefirsttosimultaneouslyconsiderbusinessvalueandmodelexplanationcapa-
bilities. ThissectionpresentsourmodelXVMFthataimstodefineaquantitative,evaluated,
explainable,andvalue-awarerecommendersystem.
In analogy with the approach of NEMF [213], we study how properly integrate a novel
valueregularizationtermtotheoriginalobjectfunctionofEMFproposedbyAbdollahiand
Nasraoui[173](seeEq. 3.4)tocontrolthebusinessvalueofthegeneratedrecommendations.
In particular, for the value-aware term, we define v as the business value of the item i. As
i
assertedinchapter2, thebusinessvalueofanitemismostconsideredequalforallusersand
itrepresentsthecontrolkeyfortheenterpriseusertoanswerbusinessquestionsandadoptan
AI-basedstrategyinthedecision-makingphase.
ThefollowingequationformalizestheobjectivefunctionofXVMF:
∑
β
L = (r − p · qT)2 + (∥ p ∥2 +∥ q ∥2)+ +∥ p − q ∥2(λW +δv) (3.16)
u,i u i 2 u i u i u,i i
(u,i)∈S
where,
L
• isthelossfunction;
• uisasingleuserfromtheset U = { 1,...,m } ofallmusers;
• iisasingleitemfromtheset I = { 1,...,n } ofallnitems
S
• isthesetofcombinations(user,item)
• r ∈ Ristheratingforitemibyuseruinvaluerange[1,5]
u,i
• p
∈ R1×fisthelatentfactorf-dimensionalofuseru(wherefistheembeddingdimen-
u
sion,hyper-parameterofthealgorithm)
• q
∈ Rf×1
isthelatentfactorf-dimensionalofitemi(wherefistheembeddingdimen-
i
sion,hyper-parameterofthealgorithm)
•
βrepresentsthelosshyper-parameterthatcontrolsthebias(∥
p
∥2 +∥
q
∥2)
u i
58

• λrepresentsthelosshyper-parameterthatcontrolstherecommendationexplainability
∈ Rm×nistheexplainabilitypowerweightedmatrix
• W
• δrepresentsthelosshyper-parameterthatcontrolsthebusinessvalue
• v isthebusinessvaluerelatedtoitemi
i
As can be shown by Eq. 3.16, we set a trade-off between the explainability and the value-
aware component, respectively, through the use of the two hyperparameters λ and δ on the
followingrules:
|     |     | (   |     |     |     |     | )   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
′
| p   | = p +η | 2(r | − p qT)q | − βp − sgn(p | − q)(λW |     | +δv) | (3.17) |
| --- | ------ | --- | -------- | ------------ | ------- | --- | ---- | ------ |
| u   | u      | ui  | u i      | i u          | u i     | ui  | i    |        |
|     |        | (   |          |              |         |     | )    |        |
′
| q   | = q +η | 2(r | − p qT)p | − βq +sgn(p | − q)(λW | +δv) |     | (3.18) |
| --- | ------ | --- | -------- | ----------- | ------- | ---- | --- | ------ |
|     | i      | ui  | u        | u i         | u i     | ui   | i   |        |
| i   |        |     | i        |             |         |      |     |        |
whereηisthelearningrate.
| 3.4 Experiments |     | and | Results |     |     |     |     |     |
| --------------- | --- | --- | ------- | --- | --- | --- | --- | --- |
Inthefollowingsection,weexperimentallycompareourapproachwithotherexplainablerec-
ommendationmodels.WecompareournovelmodelXVMFwithMatrixFactorization(MF)[217]
andExplainableMatrixFactorization(EMF)[173]. Sinceinourmodelweevaluatebothbusi-
ness value and explainability capabilities, the calculation of the explainability matrix is based
on the code by Coba et al., while the value is originally assigned to each item in the selected
datasets.
3.4.1 Dataset
Totestourapproach,theexperimentispreparedwithtwodifferentdatasetsYelp1
andAma-
zon Tools and Home Improvement2 [218] (see table 3.4 for numerical information about the
datasets). In both datasets, the rating dimension is scored in the range [1,5], where 1 is the
lowest user rate while 5 is the highest one. The item business value is native in the datasets
selected,user-independent,andshowstheenterprisereturngeneratedbypurchasingaspecific
item(profit).
1https://www.yelp.com/dataset/challenge/
2https://jmcauley.ucsd.edu/data/amazon_v2/index.html
59

| Property                  | Yelp    | Amazon  |
| ------------------------- | ------- | ------- |
| Usernumber                | 589379  | 4699605 |
| Itemnumber                | 15290   | 559628  |
| Interactionnumber         | 1191794 | 9437704 |
| Filteronuserinteraction   | 20      | 25      |
| Filteroniteminteraction   | 0       | 25      |
| Userfilterednumber        | 3876    | 5252    |
| Itemfilterednumber        | 11893   | 26927   |
| Interactionfilterednumber | 124999  | 134323  |
Table3.4:Informationaboutdatasetsusedintheexperimentandfilterappliedtoavoidcoldstartissue.
Since in the literature the number of available datasets that expose the business value for
anitemislimited,theselectionofthesedatasets(YelpandAmazon)isbasedontheinforma-
tiontheypresentintheformofuserratingsforanitem,andthecorrespondingbusinessvalue.
Althoughitispossibletogeneratesyntheticallythevalueforanitembyusingspecificmethod-
ologies, we discourage this approach that could be affected by bias and generates results that
donotrepresentbydefinitionthereal-worldbehaviors(wherevaluecouldbeassigneddueto
specificbusinessrequirements).
Fromtheoriginaldatasets,adatarefinementwasappliedtoavoidcoldstartproblems[154,
219,52,220]. Inparticular,fortheYelpdataset,weexperimentallyselectedthethresholdof20
astheminimumnumberofinteractionsperuser. Finally,tobecompliantwiththeoriginalin-
formationsource,weverifiedthatthecorrelationanddistributionofthedataweremaintained
afterthefilteringoperation. ThesameapproachwasappliedtotheAmazondatasetbutinthis
case, to avoid memory overflow on GPU, we applied a user interaction threshold of 25 and
in addition an item interaction threshold of 25, ensuring the compliance of correlation and
distributiontotheoriginaldataset.
3.4.2 ExperimentalSetup
Theexperimentconsistsofgeneratingitemrecommendationsforusersevaluatingtheperfor-
manceofexplainabilityandbusinessvaluecapabilitiesofthemodel. Allexperimentsareper-
formed with a train-validation-test split of 60%-20%-20%. We consider the first 20 elements
recommendedbythealgorithmsforeachuser.
Regardingtheassessmentphase,toevaluatetheaccuracyofthemodelweuseNDCGmetric.
60

Toevaluateexplainability,insteadofusingMEPmetric,suggestedbyAbdollahiandNasraoui,
weadoptE-NDCGcalculation,asarguedbyCobaetal.[213]. Finally,toevaluatethebusiness
impact, we define a novel evaluation metric named the Normalized Discounted Cumulative
Value(NDCV).NDCVisametricthatcombinesconsumerrelevanceandorganizationalvalue.
Theideaunderlyingthismetricistakenfromarecentpaperthatmeasuresperformanceusing
thePrice-BasedNDCG@k[104],i.e.,avariantofthepreviouslydefinedNDCG@kwherethe
gainisgivenbytheitem’sprice. Inourcontext,insteadofexplicitlyconsideringtheprice,we
consideragenericbusinessvalue(e.g.,short-termprofit)thatthecompanymayaimtooptimize
inaccordancewiththepurposesofvalue-awareRSs.
WesystematicallyassesstheperformanceMF,EMF,andXVMF.Ourevaluationmethod-
ology involves the manipulation of explainability and value regularization parameters while
holdingallothervariablesconstantatspecifiedvalues. FortheYelpdataset,thefixedparame-
tersincludealatentfactorcountof128,alearningrateηsetat0.001,andathresholdof20users
toprovideexplanationsforeachrecommendation. Moreover,referringtotheAmazondataset,
wemaintainparameteruniformitywith128latentfactors,anηvalueof0.001,andthesame
20-user threshold for explanation provision. In addition, all the experiments are conducted
withanupperboundof1000epochsoflearning,alsoimplementingacontrolthatearly-stops
thelearningwhenthevalidationerrorstartstoincreaseorstopsimproving.
Finally,theexperimentswereconductedonaUbuntu22.04machinewithAMDRyzenTM
52600Xprocessor,16GBDDR43000MHzram,NvidiaGeForceRTX2080Tigraphiccard.
3.4.3 Results
Inthissections,wediscusstheresultsofourproposedmodelwhenwesetvariationonthetwo
hyperparametersλandδ,respectivelytheexplainabilityandvalueregularizationterms.
We report the variation of the three considered evaluation metrics in two different charts,
repeatingtheprocedureforthetwodatasets. Inthecharts,weaimtoshowthetrendofcurves
whenwevarytheregularizationtermandcalculatetheNDCG,NDCV,andE-NDCGindexes.
PerformanceevidenceontheYelpdataset
Inchart3.1a,wereportthetrendofE-NDCGcomparedtotheNDCGvalue,increasingthe
explainabilitytermwhilefixingtheδat0.001. Thecurvesshowasimilartrendwithahigher
level of E-NDCG for λ less than or equal to 0.05, keeping the peak at 0.001. On the other
hand, 3.1b exposes the results for NDCG and NDCV calculation at λ = 0.001 while the
61

0.0040
0.0035
0.0030
0.0025
0.0020
0.0015
0.0010
0.0005
0.0 0.001 0.005 0.01 0.05 0.1 0.5 0.8
Explainability Regulation Term
GCDN
0.035
0.030
0.025
0.020
0.015
0.010
0.005
0.000
GCDN-E
0.0040
0.0035
0.0030
0.0025
0.0020
0.0015
0.0010
0.0005
0.0 0.0005 0.005 0.05 0.1 0.5
Value Regulation Term
(a)
GCDN
0.008
0.006
0.004
0.002
VCDN
(b)
Figure3.1:PerformanceanalysisforYelpdataset:metricscalculationfortheindividualvariationofeachregularisation
term.
modelvariesthevalueregularizationterm. Thetwocurvesdesignasimilarpaththatdegrades
atδ >= 0.005.
Considering,instead,thesimultaneousvariationofbothexplainabilityandvalueregulariza-
tionterm, wecannoticehowtheNDCG,NDCV,andE-NDCGchange. Werepresentthe
evaluationofthethreemetricsusingthreedifferentheatmaps(seeFigure3.2),whereeachcell
representsthemetricscorefortheconsideredcoupleofregularizationterms. Thehigherthe
valueofthemetricis,thedarkerbluethecelliscolored. Evaluatingtheobtainedcharts,they
showanexistingvalueintervalforbothoftheregularizationtermswherewecancalculatethe
maximumvalueforeachmetric. Theseintervalsoverlapapproximatelyforeachheatmap,and
eachmetricvaluedegradesquicklybyincreasingtheregularisersaboveacertainthreshold(0.01
forbothexplainabilityandvalueregularizationterm).
PerformanceevidenceontheAmazondataset
ConsideringtheAmazondataset,inthechart3.3awecouldhighlighttheE-NDCGcompared
to the NDCG, while increasing the explainability term and keeping the hyperparameter for
valueatδ = 0.01. Weobtainthebestexplainabilityresultforλ = 0.01andsimultaneously
a decrease of NDCG, while on other values the explainability performance degrades to the
benefitofNDCG.Ontheotherhand,3.3bexposesasimilartrendfortheNDCGandNDCV
curves,varyingthevalueregularizationtermandkeepingthebestλvalueat0.01.
InFigure3.4,weintegrateasimultaneousvariationintheweightofthetworegularization
termsandshowtherelativemetricvalueineachcell(darkerbluecolorforhighermetricscore,
62

NDCG NDCV
| 0.8                                |     | 0.0040 | 0.8                                |     |
| ---------------------------------- | --- | ------ | ---------------------------------- | --- |
| mreT noitaziralugeR ytilibanialpxE |     |        | mreT noitaziralugeR ytilibanialpxE |     |
0.0035 0.008
| 0.5 |     |     | 0.5 |     |
| --- | --- | --- | --- | --- |
0.0030
| 0.1 |     |     | 0.1 |     |
| --- | --- | --- | --- | --- |
0.006
| 0.05 |     | 0.0025 | 0.05 |     |
| ---- | --- | ------ | ---- | --- |
0.0020
| 0.01 |     |     | 0.01 | 0.004 |
| ---- | --- | --- | ---- | ----- |
0.0015
| 0.005 |     |        | 0.005 |       |
| ----- | --- | ------ | ----- | ----- |
| 0.001 |     | 0.0010 | 0.001 | 0.002 |
0.0005
| 0.0 |     |     | 0.0 |     |
| --- | --- | --- | --- | --- |
0.0 1000.0 5000.0 100.0 500.0 10.0 50.0 80.0 1.0 3.0 5.0 0.0 1000.0 5000.0 100.0 500.0 10.0 50.0 80.0 1.0 3.0 5.0
Value Regularization Term Value Regularization Term
| (a) |     |     | (b) |     |
| --- | --- | --- | --- | --- |
E-NDCG
0.035
mreT noitaziralugeR ytilibanialpxE 0.8
0.5 0.030
0.1
0.025
0.05 0.020
0.01
0.015
0.005
0.010
0.001
0.005
0.0
0.000
| 0.0 1000.0 5000.0 | 100.0 500.0 10.0 50.0 | 80.0 1.0 3.0 5.0 |     |     |
| ----------------- | --------------------- | ---------------- | --- | --- |
Value Regularization Term
(c)
Figure3.2:PerformanceanalysisforYelpdataset:metricscalculationforsimultaneousvariationofbothregularization
terms.
|     |     | 0.00175 | 0.0007 | 0.0016 |
| --- | --- | ------- | ------ | ------ |
0.00045
0.00150 0.0014
| 0.00040 |     |         | 0.0006 |        |
| ------- | --- | ------- | ------ | ------ |
| 0.00035 |     | 0.00125 |        | 0.0012 |
0.0005
| GCDN 0.00030 |     | 0.00100 GCDN-E | GCDN | 0.0010 VCDN |
| ------------ | --- | -------------- | ---- | ----------- |
0.0004
0.0008
0.00025 0.00075
0.0003
| 0.00020 |     |     |     | 0.0006 |
| ------- | --- | --- | --- | ------ |
0.00050
| 0.00015 |     |     | 0.0002 | 0.0004 |
| ------- | --- | --- | ------ | ------ |
0.00025
| 0.00010 |     |     | 0.0001 | 0.0002 |
| ------- | --- | --- | ------ | ------ |
0.00000
0.0 0.001 0.005 0.01 0.05 0.1 0.5 0.8 0.0 0.00010.0005 0.001 0.005 0.01 0.05 0.08
Explainability Regularization Term Value Regularization Term
| (a) |     |     | (b) |     |
| --- | --- | --- | --- | --- |
Figure3.3:PerformanceanalysisforAmazondataset:metricscalculationfortheindividualvariationofeachregularisation
term.
63

NDCG NDCV
| 0.8                                |     |     | 0.8                                | 0.0016 |
| ---------------------------------- | --- | --- | ---------------------------------- | ------ |
| mreT noitaziralugeR ytilibanialpxE |     |     | mreT noitaziralugeR ytilibanialpxE |        |
0.0007 0.0014
| 0.5 |     |     | 0.5 |     |
| --- | --- | --- | --- | --- |
0.0006
| 0.1  |     |        | 0.1  | 0.0012 |
| ---- | --- | ------ | ---- | ------ |
| 0.05 |     | 0.0005 | 0.05 | 0.0010 |
0.0004 0.0008
| 0.01 |     |     | 0.01 |     |
| ---- | --- | --- | ---- | --- |
0.0006
| 0.005 |     | 0.0003 | 0.005 |        |
| ----- | --- | ------ | ----- | ------ |
| 0.001 |     | 0.0002 | 0.001 | 0.0004 |
0.0002
| 0.0 |     | 0.0001 | 0.0 |     |
| --- | --- | ------ | --- | --- |
0.0 1000.0 5000.0 100.0 500.0 10.0 50.0 80.0 0.0 1000.0 5000.0 100.0 500.0 10.0 50.0 80.0
Value Regularization Term Value Regularization Term
| (a) |     |     | (b) |     |
| --- | --- | --- | --- | --- |
E-NDCG
mreT noitaziralugeR ytilibanialpxE 0.8 0.0040
0.5 0.0035
0.1 0.0030
0.05 0.0025
0.01 0.0020
0.005 0.0015
0.0010
0.001
0.0005
0.0
0.0000
| 0.0 1000.0 | 5000.0 100.0 500.0 | 10.0 50.0 80.0 |     |     |
| ---------- | ------------------ | -------------- | --- | --- |
Value Regularization Term
(c)
Figure3.4:PerformanceanalysisforAmazondataset:metricscalculationforsimultaneousvariationofbothregularization
terms.
lighter green color for lower one). We can point out that in 3.4a and 3.4b, the NDCG and
NDCV values follow a similar behavior with a good approximation, while the degradation
ofthemetricsispresentbutnotdefinedbyaprecisethreshold, presentingawiderareawith
low-levelscoreforhighervalueofexplainabilityandvalueterms. Conversely,thebehaviorofE-
NDCGmetricexposesatradeoffunderathresholdforboththeregularizationterm(λ = 0.05
= 0.005).
| andδ | Overthesevalues,theexplainabilitymetricdegrades. |     |     |     |
| ---- | ------------------------------------------------ | --- | --- | --- |
3.4.4 Comparisonwithothermethods
OurmodelXVMFismatrixfactorization-based,andforthecomparisonexperimentation,we
adopt MF as the baseline, and EMF [173] to compare the performance with an explainabile
model. Finally,InTable3.5and3.6arereportedtheresultsofthecomparisonanalysisbetween
the models selected, respectively for the outcome obtained with Yelp and Amazon datasets.
64

SincethebalanceobtainedwiththevariationofthehyperparametersinXVMFcouldshiftthe
performanceoftheresults,wereport:
• XVMF-easthebestsolutionforexplainabilityscoreconsideringthemaximumE-NDCG
obtained;
• XVMF-vasthebestsolutionforbusinessvalueconsideringthemaximumNDCVob-
tained;
• XVMF-evasthebestsolutionattheintersectionoftheprevioustwoandconsidering
bothofthepreviousindexessimultaneously.
ConsideringtheresultsoftheYelpdataset(seeTable3.5),ourmodelXVMFhasthehigh-
estscoreforallmetrics,andthesolutionthatmaximizestheexplainabilityandbusinessvalue
perspective,aloneorsimultaneously,isthesame. Conversely,consideringtheAmazondataset,
theXVMF-evisnotthetopmodelintermsofNDCVandE-NDCG,but,thesolutionsthat
considerindividualvalueandexplainabilitygetthehighestscore.
| Algorithm | NDCG    | NDCV    | E-NDCG  |
| --------- | ------- | ------- | ------- |
| MF        | 0.1281% | 0.2069% | 0.8799% |
| EMF       | 0.1003% | 0.2067% | 0.8101% |
| XVMF-e    | 0.2493% | 0.5042% | 1.9954% |
| XVMF-v    | 0.2493% | 0.5042% | 1.9954% |
| XVMF-ev   | 0.2493% | 0.5042% | 1.9954% |
Table3.5:EvaluationmetricsMF,EMFandXVMFforYelpdataset.Thehighestvalueperindexisindicatedinbold.
| Algorithm | NDCG    | NDCV    | E-NDCG  |
| --------- | ------- | ------- | ------- |
| MF        | 0.0525% | 0.0792% | 0.0836% |
| EMF       | 0.0121% | 0.0253% | 0.0000% |
| XVMF-e    | 0.0125% | 0.0275% | 0.1723% |
| XVMF-v    | 0.0514% | 0.1154% | 0.0123% |
| XVMF-ev   | 0.0365% | 0.1117% | 0.0184% |
Table3.6:EvaluationmetricsMF,EMFandXVMFforAmazondataset.Thehighestvalueperindexisindicatedinbold.
65

3.5 Discussion
Uponanalyzingtheprecedingsection’soutcomes,itisevidentthatdependingonthenatureof
theinteractionsavedintothedatabase,wecanfindslightlydifferentbehaviorsthatthemathe-
maticalmodeltriestolearn.Overall,basedonthemetricspresentedinTables3.5and3.6,itcan
benoticedthat,althoughthevaluesarelow,theyarepromisingsincetheygenerallyexceedthe
baselinesused,particularlyfortheYelpdataset. Moreover,theexperimentsshowthatthebal-
ancebetweenthetworegularizationtermsisachievedforlowvalue,andperformancedegrades
quickly after a certain threshold range that is dependent on the application context. The ex-
perimental model couldbe enhancedin the future byconsidering alternativeperspectives or
evaluation metrics, either previously existing in the literature or newly proposed. Adopting
qualitative measurement indicators, already present in the state-of-the-art, is desirable to en-
hancethisnewfieldofresearchwithmorecomparablemodels. Finally,weusedtheprofitas
businessvalue, butothercompaniescouldintegrateanotherkindofvalue(seechapter2)ac-
cordingtothebusinessstrategy. Differentkindsofvaluescouldrequirevariationonthemodel
toadaptthemathematicalinterpretationoftheproblemtotherealcontext.
Themodelisfocusedonthedefinitionofawaytobalancetheexplainabilitytermandthe
businessvalue. Wehadtodealwiththeclassicrecommendationproblems(i.e.,coldstart,long
tail)whilecreatingamodelthatintroducednewcomplexitytohandleandrespondtoaspecific
requirement of enterprises. Indeed, one of the problems that this model aims to solve is en-
ablingthecompanytounderstandbettertheirinternalprocessesenhancedbyAIinstruments.
Inparticular,integratingablack-boxAImodelintoadecisionprocesscanleadtounpleasantef-
fectsintheadoptionofsystemresults(i.e.,lackoftrustandunderstanding).Balancingbusiness
valueandenhancingtherecommendationswithaquantitativescoreofexplainabilitycouldre-
ducethedistancebetweentheuserandthemodel,enablingtheadoptionandleadingtheuse.
Infutureworks,theresearchonthistopiccouldbedirectedtoimproveXVMForcreatea
newmodel,consideringotherperspectivesorusingdifferentmetricsanddatasets. Industries
needtoleadandunderstandthecomplexitybeyondtheirprocess,yetwiththesupportofthese
kindsofsystems. Anotherfuturedirectionthatwecouldsuggestisthedevelopmentofanin-
teractiveuserinterfacetohandlethebalancebetweenthetwoperspectivesandcollectfeedback
fromtheusers,whichisessentialforempoweringthemodels.
66

3.5.1 RealWorldutility
Explainability and value awareness are two pivotal aspects in the implementation of recom-
mendersystemsforbusinessdecisions. Explainabilityaddressestheneedfortransparencyand
comprehensionintherecommendationsprovidedtousersandstakeholders. Inabusinesscon-
text, understanding the rationale behind recommendations is paramount, as it instills trust
andconfidenceinthesystem’ssuggestions. Explainablerecommendersystemsallowusersand
decision-makerstograspnotonlywhatisrecommended,butalsowhyitisrecommended,en-
ablingthemtomakeinformedchoicesalignedwiththeirpreferencesandneeds.
Ontheotherhand,value-awarenessaddsastrategicdimensiontorecommendersystemsby
focusingonthegenerationoftangiblebusinessvalue.Traditionalrecommendersystemsmight
solelyemphasizeuserpreferences,butinabusinesssetting,itiscrucialtoalignrecommenda-
tionswithorganizationalobjectives. Value-awarerecommendersystemstakeintoaccountnot
onlyuserpreferencesbutalsothepotentialimpactonkeybusinessmetrics,suchassales,cus-
tomer retention, or engagement. By optimizing recommendations to simultaneously satisfy
userpreferencesanddrivebusinessoutcomes,valueawarenessbecomesakeytoolforenhanc-
ingtheoverallefficiencyandeffectivenessofacompany’sdecision-makingprocesses.
Incorporating explainability and value-awareness into recommender systems can thus em-
powerbusinessestocreateaharmoniousbalancebetweenusersatisfactionandorganizational
success. Itnotonlyenhancesuserexperiencesbutalsopositionstheorganizationforimproved
competitivenessandgrowththroughrecommendationsthatarenotonlyaccuratebutalsoun-
derstandableandalignedwithstrategicgoals. Real-worlddatasetsdescribedifferentcontexts
ofapplicationandtheadaptationofthemodelproposedshouldbetakenintoaccount.Inaddi-
tion,byprovidinganinterfacetobusinessdecision-makers,itcouldcreateaninteractivewayto
accesstheinformationprovidedbythemodelproposed,guidingthesystemtoproducemore
refinedexplanationsormorevaluableoutputs,dependingonthepreferredlevelofbalanceand
businessgoals.
3.6 Contribution
Inthischapter, weprovidedthenovelrecommendationmodelXVMF,whichis, tothebest
ofourknowledge,thefirstmodeltobalanceexplainabilitycapabilitieswiththebusinessvalue
generated. Evaluating three different metrics, NDCG, NDCV, and E-NDCG, we aimed to
understand how the model affects the different perspective of explainability and value busi-
67

ness. Finally,changingthehyperparameterssimultaneously,wederivedthecross-dependence
performanceofthemodel.
Although the benefits of the system could be different for the companies, it appears chal-
lenging to create a general system that could be applied to multiple sources (i.e., datasets of
multiplecompanies)keepingahighandaccuratelevelofperformance. Theapplicationofthe
modelinareal-worldscenariomustrequirearefinementoftheparameterstrainedandadeep
understanding of the business decision process to encapsulate the right enterprise dynamics
withinthesystem. Measuringmodelperformanceintherightwayisessentialforenterprisesin
thedesignandevaluationphasebecauseitprovidesacomparablewaytoassessmultiplemodels,
selectingthebestone.
Moreover,wediscussedhowexplainabilityaffectstheRSsfield,focusingontheimportance
oftheevaluationphase. Amongtheevaluationmetricsreported,weselectedthemostusedand
promisingonestoevaluateourmodel.
In the next chapter of this thesis, we conclude our research journey with an analysis of a
promisingrecommendersystemsfamilybasedongraphs. Inparticular,wefocusonthereason
for the importance of defining common evaluation criteria for explainability, highlighting a
commonsymptomthataffectstheGraph-BasedExplainableRecommenderSystems,andsug-
gestingadirectionforfutureresearchworksinthisfieldtosupporttheenterprisemodeldesign
process.
68

4
Explainability applied on Graph-based
Recommendation Systems
Inrecentyears,wehaveregisteredanincreaseintheamountofpublishedresearchinthefieldof
ExplainableRecommenderSystems. Asreportedinthechapter3,thesesystemsaredesigned
tohelpusersfindtheitemsofthemostinterestbyprovidingnotonlysuggestionsbutalsothe
reasonsbehindthoserecommendations. Researchhasshownthattherearemanyadvantages
to complementing a recommendation with a convincing explanation. For example, such an
explanationcanoftenleadtoanincreaseinusertrust,whichinturncanimproverecommen-
dationeffectivenessandsystemadoption. Inparticular,manyresearchworksfocusonexplain-
ablerecommendationalgorithmsbasedongraphsduetothenaturalgraphstructurepresenta-
tioncapabilities(i.e., exploitingknowledgegraphsorgraphneuralnetworks-basedmethods).
The use of graphs is very promising since algorithms can, in principle, combine the benefits
of personalization and graph reasoning, thus potentially improving the effectiveness of both
recommendationsandexplanations. However,althoughgraph-basedalgorithmshavebeenre-
peatedlyshowntobringimprovementsintermsofrankingquality,notmuchliteraturehasyet
studiedhowtoproperlyevaluatethequalityofthecorrespondingexplanations. Asreported
inchapter2and3,fromanindustrialperspectiveisessentialforamodeltobecomparableand
quantitative evaluable, not only in the selection phase of the best performer but also during
projectsetup,establishingexpectationsandreturnoninvestment. Inthischapter,wefocuson
thisproblem,examiningindetailhowtheexplainablerecommendersystemsbasedongraphs
69

arecurrentlyevaluated,discussinghowtheycouldbeimproved,andsuggestingafuturedirec-
tioninamorequantitativeandcomparableway.
Asusershaveincreasinglydemandedexplanationsforrecommendationsinrecentyears, it
becomescrucialformodeldeveloperstoprovideinsightsintohowandwhythoserecommen-
dationsaremade. Unliketraditionalrecommendersystems,thiskindofapproachallowsany
recommendationtobegeneratedbysimultaneouslyintegratingitwithacorrespondingexpla-
nation. Theexplanationsprovidedcanbeverypersuasive[221,222,223]inthattheyoftenex-
ploitgraphreasoninglogicthatallowstheexplanationtoberepresentedasapathonthegraph.
Forexample, an explanationfora “Back to theFuture” recommendation, maybe intuitively
−w−a−tc−h→ed −d−ir−ec−ted−→by −th−at−al−so−d−ire−ct→ed
representedwiththepath“user ForrestGump RobertZemeckis
BacktotheFuture”[224].However,althoughgraph-basedmethodshaverepeatedlyshownre-
markableperformanceinmodelingcomplexuser-itemrelationaldependenciesandgenerating
relevantrecommendations,thetransparencyandinterpretabilityoftheunderlyingreasoning
processstillremainasignificantconcern. Inparticular,themainproblemliesinestablishinga
clearunderstandingofwhataGraph-BasedExplainableRecommenderSystem(GxRS)should
provideasanexplanation,howitcouldbeusefulforthefinalusers,andespeciallyhowaccurate
theoutcomeis.
Toclarifythechallengesmentionedabove,theremainderofthechapterisorganizedasfol-
lows. InSection4.1weofferageneralintroductiontorecentgraph-basedexplainablerecom-
mendation algorithms. Subsequently, in Section4.2 we focuson the current methodologies
usedintheliteraturetoevaluatethesealgorithms. Then,inSection4.3webringtothecom-
munity’sattentiontheimportanceoftheintegrationofquantitativeexplainableperformance
evaluation,whilealsodiscussingpotentialwaystousetheseguidelinesinfutureresearchworks.
4.1 Background and concepts
Graph-based algorithms have attracted the interest of many researchers because of the capa-
bilitiestheyoffertorepresenttheworldofinteractions,particularlythoserelatedtohumans.
They are a promising area because the learning process can be based directly on graphs that
notonlyrepresentuser-objectinteractionsbutcanalsoincludecontextualinformationsuch
as user demographics, product categories, and other attributes. In particular with the objec-
tive of capturing these connections and exploiting these potentials through user suggestions,
Knowledge Graphs (KGs) and Graph Neural Networks (GNNs) have gained significant at-
tentioninrecentyears,especiallyintheRecommenderSystems(RSs)fieldtoensurefairness
70

Table4.1:Graph‐BasedExplainableRecommenderSystemssurveyedfromliterature,andgroupedbyalgorithmicmethod
andexplainabilityevaluationapproach.
Qualitative Ex- Quantitative
Algorithmic No Explainability
plainability Explainability
Method Evaluation
Evaluation Evaluation
Embedding- [225,226,227,228,
[230,231,232]
based 229]
[233,234,235,236,
237, 238, 239, 224, [245, 246, 247, 214,
Path-based
240, 241, 242, 243, 248,249]
244]
[250], improvebusinessvalue[2], orgeneraterelevant, yetexplainable, recommendationsto
usersfromgraphs[251,194].
Analyzingthemostrecentsurveys[252,253,254,255,256,257]inthefieldofGNN-and
KG-basedrecommendersystems,from2018to2023(seeTable4.1),whatemergesisthatmany
existingstudieshavefocusedontheuseofgraphstoimprovetheperformanceofrecommender
systemsintermsofrecommendationquality,diversity,andotherconventionalmeasures,while
lessrigorouslyassessingthequalityofthecorrespondingexplanations. Studiesoftenofferonly
qualitative case-based examples where a particular explanation is represented graphically as a
pathonthegraph. However, whatisgenerallylackingisaquantitativeandcomparableeval-
uationofthequalityofexplanationsaccordingtothewidelyknownguidelinesofexplainable
recommendationsystems[165].Whilegraphicalexplanationsareusefulforgettinganintuitive
ideaoftheunderlyingreasoningprocess,theyalsoseverelylimitthecomparisonofalgorithms
and, more generally, the progress in this particular field. Instead, it may be beneficial for re-
search to focus more in the future on the evaluationaspects by designing metrics to provide
quantitativeinsightsintothecompletedecision-makingprocesstoensurethatthealgorithms’
explanationsareusefulinpracticefromahumanperspective.
Intheliterature,anumberofdifferentstudiesproposedtheuseofGNN-orKG-basedalgo-
rithmstogeneraterelevant,yetexplainablerecommendationsfromgraphs. Thesegraphsoften
provideadditionalinformationinadditiontothemostcommonlyuseduser-iteminteractions,
includingdemographiccharacteristicsoftheuser(e.g.,age,gender),variousattributesofthe
item (e.g., product category, price range), and contextual features (e.g., time, location) inter-
connectedinagraph. Agraphcanbeclassifiedintohomogeneous(iftheedgeconnectsonly
twonodesandthereisonlyonetypeofnodesandedges),heterogeneous(iftheedgeconnects
71

onlytwonodesandtherearemultipletypesofnodesandedges), orhypergraph(whereeach
edgejoinsmorethantwonodes). Whileedgesrepresentarelation(interactionorproperty)of
thenode,eachnoderepresentsanentityofthedatasetthatcouldhaveoneormoreassociated
propertiesandcouldinteractwithotherentities. Therearevarioustechniquesforusingsuch
graph-basedinformationforrecommendationsand/orexplanationpurposes.
Dependingonhowthegraphishandledinthelearningprocess,wecandistinguishdifferent
graph-basedexplainablerecommendationtechniquesintheliterature. Forexample,incertain
cases, neural networks can be exploited to decompose the graph in the form of embeddings
or paths (see Table 4.1). In particular, embedding-based methods typically aim to learn em-
bedding representations of users, items, and other entities from the graph that can be used
togeneraterecommendationsorexplanations. However,embedding-basedmethodsgenerally
lacktheabilitytodiscovermulti-hoprelationalpathsfromthegraphtogenerateexplanations.
Therefore,theexplanationsprovidedaregeneratedbyexploitingempiricalcriteriaofsimilarity
matchingamongthevariousembeddingsinthegraphtomotivatepost-hocagivenrecommen-
dation(weakexplainability). Instead,path-basedmethodsfirstidentifyconnectivitypathsbe-
tweenusersanditemsandthenfeedthosepathsintotherecommendationalgorithmstogen-
erate recommendations and explanations. However, although the explanations provided by
these models often appear quite convincing, as they are based on complex multi-hop reason-
ing, consideringallpossiblepathsbetweenagivenuser-itempairmayinvolveirrelevantones
thatcanleadtomismatcheswithrealuserpreferences(errorpropagation). Giventhecurrent
limitationsofpurepath-basedandembedding-basedalgorithms,otherhybrid[224,240,241]
algorithmshavealsobeenstudiedintheliterature. Thesemethodologiesshould,inprinciple,
improve recommendations and explanations by alleviating the weak explainability and error
propagationproblems. However,aswediscussinthenextsection,explanationsarenotalways
rigorouslyevaluated.
4.2 Evaluating the graph-based explainable recom-
menders
Inthissection,weexploretheevolutionoftheexplainabilityappliedonGraph-BasedExplain-
ableRecommenderSystems. Fordetailsontheexplainabilityevaluationprocess,metrics,cri-
teria,andlimitations(onRSsingeneral),seesections3.1and3.2.
In the above literature, a variety of methods and metrics are used for evaluation purposes.
72

In particular, all the surveyed studies employ well-known offline metrics (e.g., Precision, Re-
call, NDCG, AUC) from the RSs literature to evaluate the relevance of recommendations1.
ThesemetricsaretypicallyusedtoevaluatetheperformanceofaRSinrecommendingitems
ofmostinteresttousers. Proposedgraph-basedalgorithmsareoftenabletobeatbaselinesin
termsofrelevanceorotherwell-knownqualityfactorssuchasdiversityandcoveragebecause,
sincegraphsareoftenusedasadditionalcontextualinformationtotheuser-iteminteraction
matrix, they allow, in principle, more accurate recommendations to be generated. However,
especially for an Explainable Recommender Systems, while it is important to assess the rele-
vanceofrecommendations,itshouldalsobeequallyimportanttoassessthequalityofthecor-
respondingexplanations. Indeed,therecommendationalgorithmcould,inprinciple,produce
good-qualityrecommendationsbutweakexplanations.
Unfortunately,whenanalyzingtheaboveliteratureindetail,itemergesthatonlyafewworks
[245,246,247,214,248,249]haveevaluatedthequalityofexplanationsasrigorouslyasthey
haveassessedrecommendationsrelevance. Indeed,intermsofexplanationquality,almostall
studies (seeTable4.1) providesome qualitativecase-basedanalysis to intuitivelyevaluatethe
qualityofthealgorithmicreasoningprocess. Typically,aspecificrecommendationofacertain
itemisselectedforagivenuser,andagraphicalrepresentationoftheexplanationprovidedby
thealgorithmisproposed. Supplementingthegraphicalrepresentation,someempiricalobser-
vations are often provided to state that, at least intuitively, the considered explanation seems
realistic. However,whatisgenerallymissingisaquantitativeandcomparableassessmentofthe
qualityofthesystem’soverallexplanations, i.e., agoal-orientedevaluationbasedondifferent
factorsoftheexplanationsthatthesystemshouldprovideforeachrecommendationtoevery
user,asistypicallydoneinsteadwhenassessingrecommendationsrelevance.
4.2.1 Current evaluation of explanations in graph-based rec-
ommendersystems
Besides the typically employed qualitative case analyses, only a few articles, among the ones
listedinTable4.1,proposedtoevaluatetheexplanationsoftheproposedExplainableRecom-
mender Systems in a more quantitative way. For example, Lyu et al. [247] used ROUGE to
evaluateexplanationsoffline. Themetricistypicallyusedfortheevaluationoftextsummariza-
tiontasksandmeasuresthenumberofoverlappingwordsbetweenthegeneratedtextandthe
1Wereferreaderstosomerecentsurveys[170,258]forfurtherinsightsonwell-knownofflineevaluationmet-
ricsthatarewidelyusedintheRSsliteraturetoassesstherelevanceofrecommendations.
73

groundtruth. Sinceinthework,theexplanationsgeneratedbythealgorithmareexpressedin
naturallanguage,theauthorscanusethemetrictoassesshowclosetheseexplanationsareto
thegroundtruthuserreviews. However,themetriccanonlybeusedtoevaluatethenatural
language-basedexplanationstyle,whichisarecentareaofresearchintheliterature. Therefore,
theproposedevaluationisnotsuitableforevaluatingthemorewidelyadoptedpath-basedex-
planation style, i.e., where the logical reasoning of the algorithm is represented as a path on
thegraph. Toovercomethislimitation,asimilarmethodologyrecentlyemployedbyTaietal.
[248]andZhaoetal.[249]consistsofevaluatingtheabilityofanalgorithmtoprovideexpla-
nationpathsthatcontainentitiesalsopresentintheformofwordsinuserreviews,exploiting
well-knownrelevance-basedmetricssuchasNDCGandRecall. However,asintheprevious
case,ifuserreviewsarenotpresent,thiskindofevaluationmethodologyisnotapplicable. Ex-
ploiting a different methodology, Ma et al. [246] proposed to evaluate the quality of the ex-
planations(intermsofrelevanceanddiversity)fromahumanperspective. Inparticular, the
authorsrandomlyselected100user-itemrecommendationpairsandthecorrespondingpath-
basedexplanationsgeneratedbytherecommendersystem. Thentheyselected10humanraters
whohavemachinelearningexperiencetomanuallyevaluatethequalityofexplanations. How-
ever,asisalsoknowninotherareasinthefieldofrecommendersystems,thisparticularonline
evaluationmethodologycanbeveryexpensivetoperformonalargescaleandsubjecttouser
bias. Hence,theoverallvalidityofthefinalresultsmaybecompromisedifthehumanratersare
notcarefullyselected. AnothermethodologyhasbeenproposedrecentlybyWangetal.[245].
Inparticular,givenacertainexplanationforauserrecommendation,proposedtoevaluatethe
degreetowhichtheexplanationpathconformstotheparticularuserprofile. Specifically,fora
givenuser,theauthorsfirstconstructtheuserprofilecontaininghis/herinteractionswiththe
entitiesofthegraph. Thentheymeasuredthenumberofentitiesintheexplanationpaththat
arealsopresentintheuserprofile. Moreover,sinceanexplanationpathcanbebasedonmul-
tiplehopsbetweendifferentgraphentities,verylongreasoningpathswouldbeabletomatch
more user profile entities. Correspondingly, the authors’ proposed evaluation is based on a
hyper-parameter that considers only a certain number of entities in the explanation path for
evaluation purposes. However, as noted by the authors, this evaluation methodology is very
inefficient. Hence,theysampledonly100testsetusersandevaluatedtheexplanationsofthe
top20recommendationsforeachofthem. Finally,inanotherrecentworkbyGengetal.[214]
ithasbeenproposedtomeasurethroughtheNewReachRatio(NR2)metricinwhichterms
agraph-basedexplainablemodelisabletomitigatetherecallbias.
74

4.3 Towards a more standardized evaluation
Intheprevioussection, wehighlightedthatmostoftheworksintheGxRSliteratureuseda
qualitative case-based analysis rather than a quantitative approach to intuitively evaluate the
explanationsprovidedbythemodel. Unfortunately,thelackofadoptionofaquantitativeand
comparableframeworkforstyling,presenting,personalizing,andevaluatingsuchexplanations,
doesnotallowtocomparethedifferentmodelsintermsofexplainabilityresults. Theadoption
ofsharedguidelinesthatemployquantitativemetricswouldallowthisissuetobesolved.
In 2015 Tintarev and Masthoff [165], and more recently Chen et al. [172] and Mohseni
etal.[176]releasedwell-knownguidelinestocreateacommonevaluationframeworkforEx-
plainableRecommenderSystems(ofwhichGxRSarepart). Theguidelinesprovideaformal
processforassessingtheexplainabilityofamodel(seesection3.1). Followingthisprocess,the
developercandefinethegoalofthemodel,thetargetuser,andtheevaluationmetricstodeter-
minehowmuchthemodelperformsintermsofexplainability,consideringstyle,presentation,
personalization,andevaluationaspects. Forexample,intermsofpresentation,therecommen-
dationsprovidermaydesiretogiveexplanationsthatarestructuredinacertainway. Currently,
mostoftheexplanationsareprovidedtousersbyusingatemplate-basedstructure(e.g.,indicat-
inghowmanysimilarusershavethesametastesofthecurrentuser),agraphicalrepresentation
(e.g.,consideringapathonagraph)ornaturallanguage[259,260]. Instead,intermsofevalu-
ation,thequalityofexplanationsistypicallyassessedconsideringcertaingoals,astransparency,
scrutability, trust, effectiveness, persuasiveness, efficiency, and satisfaction. The ability of ex-
planations to achieve such goals can be evaluated by calculating certain metrics, considering
specificcasestudies(e.g.,foraqualitativeassessment),orthroughonlineexperiments(e.g.,user
studies,A/Btests)[172]. Eachofthesemethodshascertainadvantagesanddisadvantages. For
example,qualitativecase-basedanalysescanbeusedtointuitivelyassesswhetherexplanations
arerealisticornot. However,theevaluationmaybeaffectedbybias,andtheoutcomeofdiffer-
entmodelsisnotcomparable. Instead,analysesbasedonquantitativemetrics(e.g.,Probability
ofNecessity,MeanExplainabilityPrecision)[208,173]couldbelessintuitive,buttheyareeasy
tobenchmark,comparable,andmoreefficient.
Forexample,futureworksmayexploitexistingmetricsproposedintheliteraturetoevalu-
atetheexplanationsquality(e.g.,MeanExplainabilityPrecision[173],orExplainabilityPower
[213]). Arepresentativelistofexplainabilitymetricsfromtheliterature[172,256,166,261]is
presentedinTable3.3.Inparticular,researcherscouldfocusonbalancingmultipleperspectives
atthesametime, suchasfairnessandexplainabilitymeasuringthePathandDiversityScores
75

proposedbyFuetal.[262]. Moreover,inthefuture,itcouldbeworthtoinvestigatetherela-
tionbetweentherecommendationlistandtheexplanationpropertiesasproposedbyBalloccu
etal.. Inparticular,inrecentworks,e.g.,[215,216],Balloccuetal.proposesixnovelmetrics
to evaluate the quality of explanations, i.e., Linking Interaction Recency (LIR), Linking In-
teractionDiversity(LID),SharedEntityPopularity(SEP),SharedEntityDiversity(SED),Ex-
planationPathTypeDiversity(PTD),andExplanationPathTypeConcentration(PTC).The
useofsuchquantitativeevaluationmetricscanenhancetheinterpretabilityandtransparency
ofrecommendations,empoweringuserstomakeinformeddecisionsbasedoncomprehensible
explanations.Overalltheintegrationofsuchaquantitativeevaluationframeworkmaynotonly
provideconcreteevidenceofmodeleffectivenessbutitmayalsocontributetotheadvancement
andadoptionofexplainablerecommendersystemsinreal-worldapplications.
Besidesexploitingexistingmetrics,otherresearchdirectionsmayalsobeinterestingforthe
future. Inparticular,whileexistingmetricscanbeusedtomeasurecertainaspectsofexplana-
tions,futureresearchmaystudyotherquantitativeandcomparablemethodsthatcanbeused
to evaluate the quality of explanations in compliance with the explainability guidelines, e.g.,
assessing explanations in terms of style, personalization and presentation aspects. Moreover,
giventhelimitationsofavailabledatasetsinreflectingrealuserpreferencesintermsoftheex-
planationsprovidedbythemodels,furtherresearchmayfocusoncollectingdatasetsthathave
suchinformation. Furthermore,anotherimportantaspecttoconsiderforthefuturemaybe
theinclusionofhuman-centeredevaluationmethods. Indeed,evaluatingtheperformanceand
effectiveness of explainability from a human perspective is essential to gain valuable insights
intotheusabilityandimpactoftheexplanationsprovidedbyanalgorithm[188]. Finally,an-
other effective enhancement for evaluating explanations could be providing explanations to
users through an interface designed to facilitate access, increase comprehension, and collect
users’feedbackduringtheusageexperience. Throughthisinterface,providerscouldmeasure
theadoptionofasystemthatmayseektoachieveoneormoreobjectivesatthesametime,e.g.,
consideringeffectiveness[194],persuasiveness,scrutabilityaspects.
4.4 Contribution and future direction
Inthischapter,wediscussedhowtheexplanationsprovidedbygraph-basedexplainablerecom-
mendationsystemsarecurrentlyevaluated,pointingoutopenchallengesandfutureresearch
directionsinthisareaconcerningevaluationmethods. Whatemergesfromouranalysisisthat
mostpapersevaluatedthequalityofexplanationsthroughqualitativecase-basedanalysis,while
76

onlyafewarticlesproposedmetricsforamorequantitativeevaluation. Moreover,thecurrent
metricsarenotsufficienttocomprehensivelyevaluateallthedifferenttypesofexplanationsand
areonlypartiallycompliantwiththewell-knownexplainablerecommendersystemguidelines.
Futureresearchwillneedtoaddresscurrentlimitationsbyprovidingnewguidelines-compliant
evaluationmethodologies.Withthischapter,weencourageresearcherstoadoptamorequanti-
tativeandcomparableapproachwhenevaluatingthequalityoftheexplanations. Wehopethat
oureffortswillinspirefurtherresearchinthisfieldandleadtothecreationofmorecomprehen-
siveandguideline-compliantmethodsforassessingandcomparingthequalityofexplanations
ofgraph-basedexplainablerecommendationalgorithms.
77

78

5
Conclusion and future works
5.1 Conclusion
Approaching the research world with an enterprise perspective is the widest objective of the
industrial doctoral program at the basis of this thesis. Companies must operate under most
constraints,i.e.,regardingcost,time,manpower,andexpertise,andmostofthetimetheyfol-
lowonlyonepathinthemultitudeofsolutionsofferedbytheacademicworld. Whiletheyfind
aconcreteapplicationscenarioofthemodelavailableintheliterature,theresearchersshould
enhancetheproposedmodelwithexplanationsofwhattheblack-boxsystemgeneratesasout-
puttothenon-expertusers. Thistypeofapproachisdoublyeffective. While,ontheonehand,
businessusersunderstandtheAIsystemandincreaseitsadoption,ontheotherhand,academia
isforcedtoexpresstheresultsofthemodelnotonlyintermsofhowaccurateitisbutalsowhat
degreeofunderstandingprovidesthesystem.
Inthiscontext, wepreparedourjourneypathbycollectingnumerouscontributionsfrom
theliterature,developedourresearchbasedonindustrialexperience,andsummarizedthefind-
ingsonhowtheAImodels,inparticulartheRecommenderSystems,cansupportenterprise
strategiesofsellingaproductorproposinganitem. Firstly,weidentifiedthedifferentkindsof
businessvaluesdefinedintheliteratureandproposedataxonomythataimstosimplifycom-
prehensionandleadtoadoption. Secondly,weanalyzedhowexplainabilityapproachescanbe
implementedinrecommendersystemsfromanindustrialpointandweproposedamodelthat
79

aims to balance explainability and business value. Finally, we argued a symptom that affects
manyrecentworksintheliteratureofGraph-BasedExplainableRecommenderSystems,sug-
gestingtheimplementationofquantitativemetricsandtheadoptionofdefinitionguidelines
tocreatecomparablemodelsand,thus,facilitatingtheusebyenterprises.
Themaincontributionofthisthesisistheproposalofamodelthataimstosimultaneously
analyze both the explainability and the business value, mathematically finding a tradeoff be-
tween two perspectives that are studied separately in the literature. In designing the model
XVMF, we deal with some challenges. Primarily, we decided which family of algorithms we
shoulduse,andmatrixfactorizationoptimallysupportedourperspective. Then,wereviewed
theliteraturetochoosetheusedandpromisingmetricstoevaluatethemodelcreated. More-
over,wedecidedonthedatasetsfortheexperimentbasedonthefundamentalcharacteristics
wewantedtostudy,suchasthepresenceofadimensionrepresentingbusinessvalue. Finally,
wedefinedtheexperimentwiththemathematicalmodelconceptsandsetthehyperparameters
forthesimulationexecution.
On the other hand, we have also systematically investigated the state-of-the-art of Value-
Aware Recommender Systems to collect all the resources published regarding this topic, an-
alyzingthedifferentapproachesproposedandsuggestingapropertaxonomyanddatasetsfor
futuremodels. ThiscontributionbecamethefirstsystematicliteraturereviewonVARSs,cre-
atingabaselineforresearcherswhoareinterestedinthistopic.
Finally,duetotheincreasedcompanies’interestinGraph-BasedExplainableRecommender
Systems(GxRSs),wedecidedtopointouthowthesemodelscouldbebeneficialforenterprises
fromanexplainabilityperspective. Inparticular,sincetheyareabletosimplifythecomplexity
oftheinformationstoredinenterprisedatasets,wefocusedontheevaluationphasewhichis
essentialforacompany. Indeed,duringthedecisionphase,decision-makersstrategicallyman-
ageawidenumberofinformationatthesametimeandrequireasolutiontocomprehendthis
process. Moreover, after highlighting the absence of quantitative evaluation metrics for the
proposed explainable graph model, we suggested the adoption of a standard way to evaluate
theexplainabilitythroughtheadoptionofexistingquantitativemetricsandthedefinitionof
thepropertyofthemodelbasedonreleasedguidelinesthataimtoclassifythemodelinterms
ofstyle,personalization,presentation,andevaluation.
80

5.2 Future works
After examining the limitations and promising areas of expansion within this thesis, we can
highlightpotentialavenuesforfutureresearch:
• improveexplainablerecommendersystemswithenhancedexplainabilitycapabilitiesthrough
theintegrationofmodeldefinition,properevaluationmetrics,andadoptionofguide-
lines;
• focusonthedevelopmentofanexplainablemodeltargetedtobusiness,usingaproper
dataset and developing an effective approach to solving real-world problems, such as
profitorrevenuemaximizing;
• definenewmetricsthataredesignedtoexplaintheblack-boxmodeltonon-expertstake-
holderstoenhancethedecisionphase;
• designandintegratemoreHuman-Centeredinterfacesabletopresenttheinformation
properly(alreadyexistingapproachesareavailable;maybeitwouldbebeneficialtofocus
ontheindustrialuser),andthatareabletocollectuserfeedback,balancingtheexplain-
abilityenginetohumanbusinessquestions.
We hope that our work could add an additional element in a still unexplored area, due to
thedistancebetweentheacademicandenterpriseworld,butwithahighlevelofinterestand
potentialimprovement.
81

82

References
[1] MatthewJPage,JoanneEMcKenzie,PatrickMBossuyt,IsabelleBoutron,TammyC
Hoffmann,CynthiaDMulrow,LarissaShamseer,JenniferMTetzlaff,ElieAAkl,SueE
Brennan,etal. Theprisma2020statement: anupdatedguidelineforreportingsystem-
aticreviews. Systematicreviews,10(1):1–11,2021.
[2] Alvise De Biasio, Andrea Montagna, Fabio Aiolli, and Nicolò Navarin. A sys-
tematic review of value-aware recommender systems. Expert Systems with Applica-
tions, 226:120131, September 2023. ISSN 0957-4174. doi: 10.1016/j.eswa.2023.
120131. URL https://www.sciencedirect.com/science/article/pii/
S0957417423006334.
[3] Andrea Montagna, Alvise De Biasio, Nicolò Navarin, and Fabio Aiolli. Graph-based
explainablerecommendationsystems: Arewerigorouslyevaluatingexplanations? In
Proceedings of the 15th Biannual Conference of the Italian SIGCHI Chapter, CHItaly
’23,NewYork,NY,USA,2023.AssociationforComputingMachinery.
[4] FrancescoRicci,LiorRokach,andBrachaShapira.Recommendersystems:Techniques,
applications,andchallenges. RecommenderSystemsHandbook,pages1–35,2022.
[5] QiZhao,YiZhang,DanielFriedman,andFangfangTan. E-commerceRecommenda-
tionwithPersonalizedPromotion. InProceedingsofthe9thACMConferenceonRec-
ommender Systems, pages 219–226, Vienna Austria, September 2015. ACM. ISBN
978-1-4503-3692-5. doi: 10.1145/2792838.2800178. URLhttps://dl.acm.org/
doi/10.1145/2792838.2800178.
[6] FengLu,AncaDumitrache,andDavidGraus. BeyondOptimizingforClicks: Incor-
poratingEditorialValuesinNewsRecommendation. InProceedingsofthe28thACM
ConferenceonUserModeling,AdaptationandPersonalization,pages145–153,Genoa
Italy, July 2020. ACM. ISBN 978-1-4503-6861-2. doi: 10.1145/3340631.3394864.
URLhttps://dl.acm.org/doi/10.1145/3340631.3394864.
83

[7] Hekmat Adelnia Najafabadi, Ahmadreza Shekarchizadeh, Akbar Nabiollahi, Naser
Khani, and Hamid Rastgari. Dynamic pricing for information goods using revenue
managementandrecommendersystems. JournalofRevenueandPricingManagement,
2021. doi: 10.1057/S41272-020-00276-W.
[8] LiyiGuo,JunqiJin,HaoqiZhang,ZhenzheZheng,ZhiyeYang,ZhizhuangXing,Fei
Pan,LvyinNiu,FanWu,HaiyangXu,ChuanYu,YuningJiang,andXiaoqiangZhu.
We Know What You Want: An Advertising Strategy Recommender System for On-
line Advertising. In Proceedings of the 27th ACM SIGKDD Conference on Knowl-
edge Discovery & Data Mining, pages 2919–2927, Virtual Event Singapore, August
2021. ACM. ISBN 978-1-4503-8332-5. doi: 10.1145/3447548.3467175. URL
https://dl.acm.org/doi/10.1145/3447548.3467175.
[9] DirkBollen,BartP.Knijnenburg,MartijnC.Willemsen,andMarkGraus.Understand-
ing choice overload in recommender systems. In Proceedings of the fourth ACM con-
ference on Recommender systems - RecSys ’10, page 63, Barcelona, Spain, 2010. ACM
Press. ISBN 978-1-60558-906-0. doi: 10.1145/1864708.1864724. URL http:
//portal.acm.org/citation.cfm?doid=1864708.1864724.
[10] Mukund Deshpande and George Karypis. Item-based top-n recommendation algo-
rithms. ACMTransactionsonInformationSystems(TOIS),22(1):143–177,2004.
[11] Dietmar Jannach and Michael Jugovac. Measuring the Business Value of Recom-
mender Systems. ACM Transactions on Management Information Systems, 10(4):1–
23, December 2019. ISSN 2158-656X, 2158-6578. doi: 10.1145/3370082. URL
https://dl.acm.org/doi/10.1145/3370082.
[12] DietmarJannachandMarkusZanker. Valueandimpactofrecommendersystems. In
RecommenderSystemsHandbook,pages519–546.Springer,2022.
[13] Robin Burke, Gediminas Adomavicius, Ido Guy, Jan Krasnodebski, Luiz Pizzato,
Yi Zhang, and Himan Abdollahpouri. VAMS 2017: Workshop on Value-Aware and
Multistakeholder Recommendation. In Proceedings of the Eleventh ACM Conference
onRecommenderSystems,pages378–379,ComoItaly,August2017.ACM. ISBN978-
1-4503-4652-8. doi: 10.1145/3109859.3109957. URLhttps://dl.acm.org/doi/
10.1145/3109859.3109957.
84

[14] RobinBurke, HimanAbdollahpouri, EdwardC.Malthouse, KpThai, andYongfeng
Zhang.Recommendationinmultistakeholderenvironments.InProceedingsofthe13th
ACM Conference on Recommender Systems, pages 566–567, Copenhagen Denmark,
September 2019. ACM. ISBN 978-1-4503-6243-6. doi: 10.1145/3298689.3346973.
URLhttps://dl.acm.org/doi/10.1145/3298689.3346973.
[15] Changhua Pei, Xinru Yang, Qing Cui, Xiao Lin, Fei Sun, Peng Jiang, Wenwu Ou,
and Yongfeng Zhang. Value-aware Recommendation based on Reinforcement Profit
Maximization. In The World Wide Web Conference on - WWW ’19, pages 3123–
3129, San Francisco, CA, USA, 2019. ACM Press. ISBN 978-1-4503-6674-8. doi:
10.1145/3308558.3313404. URL http://dl.acm.org/citation.cfm?doid=
3308558.3313404. 17citations(SemanticScholar/DOI)[2022-02-04].
[16] QingyunWu, HongningWang, LiangjieHong, andYueShi. ReturningisBelieving:
Optimizing Long-term User Engagement in Recommender Systems. In Proceedings
of the 2017 ACM on Conference on Information and Knowledge Management, pages
1927–1936, Singapore Singapore, November 2017. ACM. ISBN 978-1-4503-4918-
5. doi: 10.1145/3132847.3133025. URL https://dl.acm.org/doi/10.1145/
3132847.3133025.
[17] Jianhua Han, Yong Yu, Feng Liu, Ruiming Tang, and Yuzhou Zhang. Optimizing
Ranking Algorithm in Recommender System via Deep Reinforcement Learning. In
2019InternationalConferenceonArtificialIntelligenceandAdvancedManufacturing
(AIAM),pages22–26,Dublin,Ireland,October2019.IEEE. ISBN978-1-72814-691-
1. doi: 10.1109/AIAM48774.2019.00011. URLhttps://ieeexplore.ieee.org/
document/8950897/.
[18] YongZhengandDavid(Xuejun)Wang. Asurveyofrecommendersystemswithmulti-
objective optimization. Neurocomputing, 474:141–153, February 2022. ISSN 0925-
2312. doi: 10.1016/j.neucom.2021.11.041. URL https://www.sciencedirect.
com/science/article/pii/S0925231221017185.
[19] Himan Abdollahpouri, Gediminas Adomavicius, Robin Burke, Ido Guy, Dietmar
Jannach, Toshihiro Kamishima, Jan Krasnodebski, and Luiz Pizzato. Multistake-
holder recommendation: Survey and research directions. User Modeling and User-
Adapted Interaction, 30(1):127–158, March 2020. ISSN 1573-1391. doi: 10.1007/
s11257-019-09256-1. URLhttps://doi.org/10.1007/s11257-019-09256-1.
85

[20] Diego Monti, Giuseppe Rizzo, and Maurizio Morisio. A systematic literature review
of multicriteria recommender systems. Artificial Intelligence Review, 54(1):427–468,
January2021. ISSN0269-2821,1573-7462. doi: 10.1007/s10462-020-09851-4. URL
https://link.springer.com/10.1007/s10462-020-09851-4.
[21] Shaina Raza and Chen Ding. Progress in context-aware recommender systems —
An overview. Computer Science Review, 31:84–97, February 2019. ISSN 15740137.
doi: 10.1016/j.cosrev.2019.01.001. URL https://linkinghub.elsevier.com/
retrieve/pii/S1574013718302120.
[22] Wen-Hao Chen, Chin-Chi Hsu, Yi-An Lai, Vincent Liu, Mi-Yen Yeh, and Shou-De
Lin. Attribute-AwareRecommenderSystemBasedonCollaborativeFiltering: Survey
andClassification. FrontiersinBigData,2:49,January2020. ISSN2624-909X. doi:
10.3389/fdata.2019.00049. URLhttps://www.frontiersin.org/article/10.
3389/fdata.2019.00049/full.
[23] Athanasios N Nikolakopoulos, Xia Ning, Christian Desrosiers, and George Karypis.
Trustyourneighbors: acomprehensivesurveyofneighborhood-basedmethodsforrec-
ommendersystems. RecommenderSystemsHandbook,pages39–89,2022.
[24] Yehuda Koren, Robert Bell, and Chris Volinsky. Matrix factorization techniques for
recommendersystems. Computer,42(8):30–37,2009.
[25] Xia Ning and George Karypis. Slim: Sparse linear methods for top-n recommender
systems. In2011IEEE11thinternationalconferenceondatamining, pages497–506.
IEEE,2011.
[26] GuyShaniandAselaGunawardana. Evaluatingrecommendationsystems. InRecom-
mendersystemshandbook,pages257–297.Springer,2011.
[27] Pasquale Lops, Marco de Gemmis, and Giovanni Semeraro. Content-based Recom-
menderSystems: StateoftheArtandTrends. InFrancescoRicci,LiorRokach,Bracha
Shapira, andPaulB.Kantor, editors, RecommenderSystemsHandbook, pages73–105.
Springer US, Boston, MA, 2011. ISBN 978-0-387-85819-7 978-0-387-85820-3. doi:
10.1007/978-0-387-85820-3_3. URL http://link.springer.com/10.1007/
978-0-387-85820-3_3.
86

[28] Xiaoyuan Su and Taghi M. Khoshgoftaar. A Survey of Collaborative Filtering Tech-
niques. Advances in Artificial Intelligence, 2009:1–19, October 2009. ISSN 1687-
7470,1687-7489. doi: 10.1155/2009/421425. URLhttps://www.hindawi.com/
journals/aai/2009/421425/.
[29] RobinBurke. Hybridrecommendersystems: Surveyandexperiments. Usermodeling
anduser-adaptedinteraction,12(4):331–370,2002.
[30] Yehuda Koren, Steffen Rendle, and Robert Bell. Advances in collaborative filtering.
Recommendersystemshandbook,pages91–142,2022.
[31] CharuCAggarwal.Model-basedcollaborativefiltering.InRecommendersystems,pages
71–138.Springer,2016.
[32] XavierAmatriain,NuriaOliver,JosepMPujol,etal. Dataminingmethodsforrecom-
mendersystems. InRecommendersystemshandbook,pages39–71.Springer,2011.
[33] BlerinaLika,KostasKolomvatsos,andStathesHadjiefthymiades. Facingthecoldstart
probleminrecommendersystems. ExpertSystemswithApplications,41(4):2065–2073,
2014.
[34] MarwaHussienMohamed,MohamedHelmyKhafagy,andMohamedHasanIbrahim.
Recommender systems challenges and solutions survey. In 2019 International Con-
ference on Innovative Trends in Computer Engineering (ITCE), pages 149–155. IEEE,
2019.
[35] LawrenceD.Miles.TechniquesofValueAnalysisandEngineering.NewYork:McGraw-
HillBookCompany.,1961.
[36] James C. Anderson and James A. Narus. Business marketing: understand what cus-
tomersvalue. Harvardbusinessreview,76:53–67,1998.
[37] James C. Anderson and James A. Narus. Understanding, Creating, and Delivering
Value.BusinessMarketManagement. NewJersey: PrenticeHall,UpperSaddleRiver,
1999.
[38] Valarie A Zeithaml. Consumer perceptions of price, quality, and value: a means-end
modelandsynthesisofevidence. Journalofmarketing,52(3):2–22,1988.
87

[39] HalilShevketNeapandTahirCelik. Valueofaproduct: Adefinition. International
JournalofValue-BasedManagement,12(2):181–191,1999.
[40] PhilipKotler.MarketingManagement:TheMillenniumEdition,volume10.Prentice
HallUpperSaddleRiver,NJ,2000.
[41] Adam Lindgreen and Finn Wynstra. Value in business markets: What do we know?
wherearewegoing? Industrialmarketingmanagement,34(7):732–748,2005.
[42] MiltonRokeach.TheNatureofHumanValues.Freepress,1973.ISBN0-02-926750-1.
[43] RogerJ.Best. Market-BasedManagement: StrategiesforGrowingCustomerValueand
Profitability. Pearson,2013. ISBN0-13-038775-4.
[44] FrancisButtle. CustomerRelationshipManagementConceptsandTools,EdisiPertama.
BayumediaPublishing,2007.
[45] PeterDoyle. Value-BasedMarketing: MarketingStrategiesforCorporateGrowthand
ShareholderValue. JohnWiley&Sons,2000. ISBN0471877271.
[46] DanielM.FlederandKartikHosanagar. Recommendersystemsandtheirimpacton
salesdiversity. InProceedingsofthe8thACMconferenceonElectroniccommerce-EC’07,
page 192, San Diego, California, USA, 2007. ACM Press. ISBN 978-1-59593-653-0.
doi: 10.1145/1250910.1250939. URLhttp://portal.acm.org/citation.cfm?
doid=1250910.1250939.
[47] Daniel Fleder and Kartik Hosanagar. Blockbuster Culture’s Next Rise or Fall: The
ImpactofRecommenderSystemsonSalesDiversity. ManagementScience,55(5):697–
712, May2009. ISSN0025-1909, 1526-5501. doi: 10.1287/mnsc.1080.0974. URL
http://pubsonline.informs.org/doi/abs/10.1287/mnsc.1080.0974.
[48] DokyunLeeandKartikHosanagar. Impactofrecommendersystemsonsalesvolume
anddiversity. ICIS2014,2014.
[49] DokyunLeeandKartikHosanagar.Howdorecommendersystemsaffectsalesdiversity?
a cross-category investigation via randomized field experiment. Information Systems
Research,30(1):239–259,2019.
88

[50] HyokminKwon,JaehoHan,andKyungsikHan. ART(AttractiveRecommendation
Tailor): HowtheDiversityofProductRecommendationsAffectsCustomerPurchase
PreferenceinFashionIndustry? InProceedingsofthe29thACMInternationalConfer-
enceonInformation&KnowledgeManagement, pages2573–2580, VirtualEventIre-
land,October2020.ACM. ISBN978-1-4503-6859-9. doi: 10.1145/3340531.3412687.
URLhttps://dl.acm.org/doi/10.1145/3340531.3412687.
[51] Mu-ChenChen,Long-ShengChen,Fei-HaoHsu,YuanjiaHsu,andHsiao-YingChou.
HPRS: A profitability based recommendersystem. In 2007 IEEE InternationalCon-
ferenceonIndustrialEngineeringandEngineeringManagement,pages219–223,Sin-
gapore, December 2007. IEEE. ISBN 978-1-4244-1528-1 978-1-4244-1529-8. doi:
10.1109/IEEM.2007.4419183. URLhttp://ieeexplore.ieee.org/document/
4419183/.
[52] Xavier Amatriain and Justin Basilico. Past, Present, and Future of Recommender
Systems: An Industry Perspective. In Proceedings of the 10th ACM Conference on
Recommender Systems, RecSys ’16, pages 211–214, New York, NY, USA, Septem-
ber 2016. Association for Computing Machinery. ISBN 978-1-4503-4035-9. doi:
10.1145/2959100.2959144. URLhttps://doi.org/10.1145/2959100.2959144.
[53] MichalKompan,PeterGaspar,JakubMacina,MatusCimerman,andMariaBielikova.
Exploring Customer Price Preference and Product Profit Role in Recommender Sys-
tems. IEEE Intelligent Systems, pages 1–1, 2021. ISSN 1541-1672, 1941-1294. doi:
10.1109/MIS.2021.3092768. URL https://ieeexplore.ieee.org/document/
9466459/.
[54] Yifei Zhao, Yu-Hang Zhou, Mingdong Ou, Huan Xu, and Nan Li. Maximizing Cu-
mulativeUserEngagementinSequentialRecommendation: AnOnlineOptimization
Perspective. In Proceedings of the 26th ACM SIGKDD International Conference on
KnowledgeDiscovery&DataMining,pages2784–2792,VirtualEventCAUSA,Au-
gust2020.ACM. ISBN978-1-4503-7998-4. doi: 10.1145/3394486.3403329. URL
https://dl.acm.org/doi/10.1145/3394486.3403329.
[55] DietmarJannachandGediminasAdomavicius. PriceandProfitAwarenessinRecom-
menderSystems. ProceedingsVAMSWorkshopatACMRecSys2017,July2017. URL
http://arxiv.org/abs/1707.08029. 25citations(SemanticScholar/arXiv)[2022-
02-04]arXiv: 1707.08029.
89

[56] UmbertoPanniello,ShawndraHill,andMicheleGorgoglione. Theimpactofprofitin-
centives on the relevance of online recommendations. Electronic Commerce Research
and Applications, 20:87–104, November 2016. ISSN 15674223. doi: 10.1016/j.
elerap.2016.10.003. URLhttps://linkinghub.elsevier.com/retrieve/pii/
S1567422316300588.
[57] MarioRodriguez,ChristianPosse,andEthanZhang. Multipleobjectiveoptimization
inrecommendersystems. InProceedingsofthesixthACMconferenceonRecommender
systems - RecSys ’12, page 11, Dublin, Ireland, 2012. ACM Press. ISBN 978-1-4503-
1270-7. doi: 10.1145/2365952.2365961. URL http://dl.acm.org/citation.
cfm?doid=2365952.2365961.
[58] GediminasAdomavicius, NikosManouselis, andYoungOkKwon. Multi-criteriarec-
ommendersystems.InRecommendersystemshandbook,pages769–803.Springer,2011.
[59] HimanAbdollahpouriandRobinBurke. Multistakeholderrecommendersystems. In
Recommendersystemshandbook,pages647–677.Springer,2022.
[60] Gediminas Adomavicius and Alexander Tuzhilin. Context-aware recommender sys-
tems. InRecommendersystemshandbook,pages217–253.Springer,2011.
[61] Yu Zheng, Chen Gao, Xiangnan He, Yong Li, and Depeng Jin. Price-aware Recom-
mendation with Graph Convolutional Networks. In 2020 IEEE 36th International
Conference on Data Engineering (ICDE), pages 133–144, April 2020. doi: 10.1109/
ICDE48307.2020.00019. 23 citations (Semantic Scholar/DOI) [2022-03-11] ISSN:
2375-026X.
[62] Hyeyoung Ko, Suyeon Lee, Yoonseo Park, and Anna Choi. A Survey of Recommen-
dationSystems: RecommendationModels,Techniques,andApplicationFields. Elec-
tronics,11(1):141,January2022. ISSN2079-9292. doi: 10.3390/electronics11010141.
URLhttps://www.mdpi.com/2079-9292/11/1/141.
[63] Aminu Da’u and Naomie Salim. Recommendation system based on deep learn-
ing methods: a systematic review and new directions. Artificial Intelligence Re-
view, 53(4):2709–2748, April 2020. ISSN 0269-2821, 1573-7462. doi: 10.
1007/s10462-019-09744-1. URL http://link.springer.com/10.1007/
s10462-019-09744-1.
90

[64] ShiwenWu,FeiSun,WentaoZhang,XuXie,andBinCui. Graphneuralnetworksin
recommendersystems: asurvey. ACMComputingSurveys,55(5):1–37,2022.
[65] MMehdiAfsar,TraffordCrump,andBehrouzFar. Reinforcementlearningbasedrec-
ommendersystems: Asurvey. ACMComputingSurveys(CSUR),2021.
[66] GediminasAdomavicius,KonstantinBauman,AlexanderTuzhilin,andMosheUnger.
Context-awarerecommendersystems: Fromfoundationsto recentdevelopments. In
RecommenderSystemsHandbook,pages211–250.Springer,2022.
[67] Evaggelia Pitoura, Kostas Stefanidis, and Georgia Koutrika. Fairness in rankings and
recommendations: anoverview. TheVLDBJournal,October2021. ISSN1066-8888,
0949-877X. doi: 10.1007/s00778-021-00697-y. URL https://link.springer.
com/10.1007/s00778-021-00697-y.
[68] YifanWang,WeizhiMa,MinZhang*,YiqunLiu,andShaopingMa. Asurveyonthe
fairnessofrecommendersystems. ACMJournaloftheACM(JACM),2022.
[69] L Chen, F Hsu, M Chen, and Y Hsu. Developing recommender systems with the
consideration of product profitability for sellers. Information Sciences, 178(4):1032–
1048, February 2008. ISSN 00200255. doi: 10.1016/j.ins.2007.09.027. URL
https://linkinghub.elsevier.com/retrieve/pii/S0020025507004641.
[70] Hsiao-Fan Wang and Cheng-Ting Wu. A mathematical model for product selection
strategiesinarecommendersystem.ExpertSystemswithApplications,36(3):7299–7308,
April 2009. ISSN 09574174. doi: 10.1016/j.eswa.2008.09.006. URL https://
linkinghub.elsevier.com/retrieve/pii/S0957417408006532.
[71] Aparna Das, Claire Mathieu, and Daniel Ricketts. Maximizing profit using recom-
mender systems. arXiv:0908.3633 [cs], August 2009. URL http://arxiv.org/
abs/0908.3633.
[72] Amos Azaria, Avinatan Hassidim, Sarit Kraus, Adi Eshkol, Ofer Weintraub, and Irit
Netanely.Movierecommendersystemforprofitmaximization.InProceedingsofthe7th
ACMconferenceonRecommendersystems,pages121–128,HongKongChina,October
2013.ACM. ISBN978-1-4503-2409-0. doi: 10.1145/2507157.2507162. URLhttps:
//dl.acm.org/doi/10.1145/2507157.2507162.
91

[73] Emre M. Demirezen and Subodha Kumar. Optimization of Recommender Systems
Based on Inventory. Production and Operations Management, 25(4):593–608, April
2016. ISSN10591478. doi: 10.1111/poms.12540. URLhttps://onlinelibrary.
wiley.com/doi/10.1111/poms.12540.
[74] ZhiweiZhang,NingChen,JunWang,andLuoSi.SMART:Sponsoredmobileapprec-
ommendationbybalancingappdownloadsandappstoreprofit. In2017IEEEInterna-
tionalConferenceonBigData(BigData), pages1600–1609, Boston, MA,December
2017.IEEE. ISBN 978-1-5386-2715-0. doi: 10.1109/BigData.2017.8258094. URL
http://ieeexplore.ieee.org/document/8258094/.
[75] EdwardCMalthouse,KhadijaAliVakeel,YasamanKamyabHessary,RobinBurke,and
Morana Fuduric. A multistakeholder recommender systems algorithm for allocating
sponsoredrecommendations. InRMSE@RecSys,2019.
[76] Phong Nguyen, John Dines, and Jan Krasnodebski. A Multi-Objective Learning
to re-Rank Approach to Optimize Online Marketplaces for Multiple Stakeholders.
arXiv:1708.00651[cs],August2017. URLhttp://arxiv.org/abs/1708.00651.
[77] LiangWu,DianeHu,LiangjieHong,andHuanLiu. TurningClicksintoPurchases:
RevenueOptimizationforProductSearchinE-Commerce. InThe41stInternational
ACMSIGIRConferenceonResearch&DevelopmentinInformationRetrieval,SIGIR
’18,pages365–374,NewYork,NY,USA,2018.AssociationforComputingMachinery.
ISBN978-1-4503-5657-2.doi:10.1145/3209978.3209993.URLhttps://doi.org/
10.1145/3209978.3209993.
[78] XiaoLin,HongjieChen,ChanghuaPei,FeiSun,XuanjiXiao,HanxiaoSun,Yongfeng
Zhang, Wenwu Ou, and Peng Jiang. A pareto-efficient algorithm for multiple objec-
tive optimization in e-commerce recommendation. In Proceedings of the 13th ACM
Conference on Recommender Systems, RecSys ’19, pages 20–28, New York, NY, USA,
2019.AssociationforComputingMachinery. ISBN978-1-4503-6243-6. doi: 10.1145/
3298689.3346998. URLhttps://doi.org/10.1145/3298689.3346998. 37cita-
tions(SemanticScholar/DOI)[2022-03-11].
[79] KartikHosanagar,RamayyaKrishnan,andLiyeMa.Recomendedforyou:Theimpact
ofprofitincentivesontherelevanceofonlinerecommendations.ICIS2008Proceedings,
page31,2008.
92

[80] Wei Lu Shanshan Chen Keqian Li and Laks VS Lakshmanan. Show me the money:
Dynamic recommendations for revenue maximization. Proceedings of the VLDB En-
dowment,7(14),2014.
[81] PengfeiHe,HaochenLiu,XiangyuZhao,HuiLiu,andJiliangTang. Propn: Personal-
izedprobabilisticstrategicparameteroptimizationinrecommendations.InProceedings
ofthe31stACMInternationalConferenceonInformation&KnowledgeManagement,
pages3152–3161,2022.
[82] Moran Beladev, Lior Rokach, and Bracha Shapira. Recommender systems for prod-
uctbundling. Knowledge-BasedSystems,111:193–206,November2016. ISSN0950-
7051. doi: 10.1016/j.knosys.2016.08.013. URL https://www.sciencedirect.
com/science/article/pii/S0950705116302751.
[83] ToshihiroKamishimaandShotaroAkaho. Personalizedpricingrecommendersystem:
multi-stageepsilon-greedyapproach. InProceedingsofthe2ndInternationalWorkshop
onInformationHeterogeneityandFusioninRecommenderSystems-HetRec’11,pages
57–64,Chicago,Illinois,2011.ACMPress. ISBN978-1-4503-1027-7. doi: 10.1145/
2039320.2039329. URL http://dl.acm.org/citation.cfm?doid=2039320.
2039329.
[84] Yoon-Joo Park and Alexander Tuzhilin. The long tail of recommender systems and
howtoleverageit. InProceedingsofthe2008ACMconferenceonRecommendersystems
- RecSys ’08, page 11, Lausanne, Switzerland, 2008. ACM Press. ISBN 978-1-60558-
093-7. doi: 10.1145/1454008.1454012. URLhttp://portal.acm.org/citation.
cfm?doid=1454008.1454012.
[85] Yoon-Joo Park. The Adaptive Clustering Method for the Long Tail Problem of Rec-
ommender Systems. IEEE Transactions on Knowledge and Data Engineering, 25(8):
1904–1915, August 2013. ISSN 1041-4347. doi: 10.1109/TKDE.2012.119. URL
http://ieeexplore.ieee.org/document/6226399/.
[86] Saúl Vargas and Pablo Castells. Improving sales diversity by recommending users to
items. InProceedingsofthe8thACMConferenceonRecommendersystems-RecSys’14,
pages145–152,FosterCity,SiliconValley,California,USA,2014.ACMPress. ISBN
978-1-4503-2668-1. doi: 10.1145/2645710.2645744. URL http://dl.acm.org/
citation.cfm?doid=2645710.2645744.
93

[87] YuanfengCaiandDanZhu.Trustworthyandprofit:Anewvalue-basedneighborselec-
tionmethodinrecommendersystemsundershillingattacks. DecisionSupportSystems,
124:113112,September2019. ISSN01679236. doi: 10.1016/j.dss.2019.113112. URL
https://linkinghub.elsevier.com/retrieve/pii/S0167923619301411.
[88] Jian Wang and Yi Zhang. Utilizing marginal net utility for recommendation in e-
commerce. In Proceedings of the 34th international ACM SIGIR conference on Re-
search and development in Information - SIGIR ’11, page 1003, Beijing, China, 2011.
ACM Press. ISBN 978-1-4503-0757-4. doi: 10.1145/2009916.2010050. URL
http://portal.acm.org/citation.cfm?doid=2009916.2010050.
[89] Yu-ChiehHo, Yi-TingChiang, andJaneYung-JenHsu. Wholikesitmore?: mining
worth-recommendingitemsfromlongtailsbymodelingrelativepreference. InProceed-
ings of the 7th ACM international conference on Web search and data mining, pages
253–262, NewYorkNewYorkUSA,February2014.ACM. ISBN978-1-4503-2351-
2. doi: 10.1145/2556195.2566589. URL https://dl.acm.org/doi/10.1145/
2556195.2566589.
[90] Yongfeng Zhang, Qi Zhao, Yi Zhang, Daniel Friedman, Min Zhang, Yiqun Liu, and
Shaoping Ma. Economic Recommendation with Surplus Maximization. In Proceed-
ings of the 25th International Conference on World Wide Web, pages 73–83, Mon-
tréal Québec Canada, April 2016. International World Wide Web Conferences Steer-
ing Committee. ISBN 978-1-4503-4143-1. doi: 10.1145/2872427.2882973. URL
https://dl.acm.org/doi/10.1145/2872427.2882973.
[91] QiZhao,YongfengZhang,YiZhang,andDanielFriedman.Multi-ProductUtilityMax-
imizationforEconomicRecommendation. InProceedingsoftheTenthACMInterna-
tionalConferenceonWebSearchandDataMining,pages435–443,CambridgeUnited
Kingdom, February 2017. ACM. ISBN 978-1-4503-4675-7. doi: 10.1145/3018661.
3018674. URLhttps://dl.acm.org/doi/10.1145/3018661.3018674.
[92] Yingqiang Ge, Shuyuan Xu, Shuchang Liu, Shijie Geng, Zuohui Fu, and Yongfeng
Zhang. MaximizingMarginalUtilityperDollarforEconomicRecommendation. In
The World Wide Web Conference on - WWW ’19, pages 2757–2763, San Francisco,
CA, USA, 2019. ACM Press. ISBN 978-1-4503-6674-8. doi: 10.1145/3308558.
3313725. URLhttp://dl.acm.org/citation.cfm?doid=3308558.3313725.
94

[93] Michael E Wall, Andreas Rechtsteiner, and Luis M Rocha. Singular value decompo-
sition and principal component analysis. In A practical approach to microarray data
analysis,pages91–109.Springer,2003.
[94] RichardSSuttonandAndrewGBarto.Reinforcementlearning:Anintroduction.MIT
press,2018.
[95] Georgios Theocharous, Philip S Thomas, and Mohammad Ghavamzadeh. Personal-
izedadrecommendationsystemsforlife-timevalueoptimizationwithguarantees. In
Twenty-FourthInternationalJointConferenceonArtificialIntelligence,2015.
[96] JoYongJu.ReinforcementLearningforProfitMaximizationofRecommenderSystems.
ReinforcementLearning,page9,2017.
[97] GuanjieZheng,FuzhengZhang,ZihanZheng,YangXiang,NicholasJingYuan,Xing
Xie, and Zhenhui Li. DRN: A Deep Reinforcement Learning Framework for News
Recommendation. InProceedingsofthe2018WorldWideWebConferenceonWorld
Wide Web - WWW ’18, pages 167–176, Lyon, France, 2018. ACM Press. ISBN
978-1-4503-5639-8. doi: 10.1145/3178876.3185994. URL http://dl.acm.org/
citation.cfm?doid=3178876.3185994.
[98] Lixin Zou, Long Xia, Zhuoye Ding, Jiaxing Song, Weidong Liu, and Dawei Yin. Re-
inforcementLearningtoOptimizeLong-termUserEngagementinRecommenderSys-
tems. In Proceedings of the 25th ACM SIGKDD International Conference on Knowl-
edge Discovery & Data Mining, pages 2810–2818, Anchorage AK USA, July 2019.
ACM. ISBN 978-1-4503-6201-6. doi: 10.1145/3292500.3330668. URL https:
//dl.acm.org/doi/10.1145/3292500.3330668.
[99] LuoJi, QiQin, BingqingHan, andHongxiaYang. ReinforcementLearningtoOpti-
mizeLifetimeValueinCold-StartRecommendation. InProceedingsofthe30thACM
InternationalConferenceonInformation&KnowledgeManagement,pages782–791,
Virtual Event Queensland Australia, October 2021. ACM. ISBN 978-1-4503-8446-
9. doi: 10.1145/3459637.3482292. URL https://dl.acm.org/doi/10.1145/
3459637.3482292.
[100] Yu Li, Yi Zhang, Lu Gan, Gengwei Hong, Zimu Zhou, and Qiang Li. RevMan:
Revenue-aware Multi-task Online Insurance Recommendation. Proceedings of the
95

AAAIConferenceonArtificialIntelligence,35(1):303–310,May2021.ISSN2374-3468.
URLhttps://ojs.aaai.org/index.php/AAAI/article/view/16105.
[101] Mikael Hammar, Robin Karlsson, and Bengt J. Nilsson. Using maximum coverage
to optimize recommendationsystemsin e-commerce. In Proceedingsof the7thACM
conferenceonRecommendersystems,pages265–272,HongKongChina,October2013.
ACM. ISBN978-1-4503-2409-0. doi: 10.1145/2507157.2507169. URLhttps://dl.
acm.org/doi/10.1145/2507157.2507169.
[102] Leman Akoglu and Christos Faloutsos. ValuePick: Towards a Value-Oriented Dual-
GoalRecommenderSystem. In2010IEEEInternationalConferenceonDataMining
Workshops, pages1151–1158, Sydney, TBD,Australia, December2010.IEEE. ISBN
978-1-4244-9244-2. doi: 10.1109/ICDMW.2010.68. URL http://ieeexplore.
ieee.org/document/5693424/.
[103] Yulong Gu, Zhuoye Ding, Shuaiqiang Wang, Lixin Zou, Yiding Liu, and Dawei
Yin. Deep Multifaceted Transformers for Multi-objective Ranking in Large-Scale E-
commerceRecommenderSystems. InProceedingsofthe29thACMInternationalCon-
ferenceonInformation&KnowledgeManagement,pages2493–2500,VirtualEventIre-
land,October2020.ACM. ISBN978-1-4503-6859-9. doi: 10.1145/3340531.3412697.
URLhttps://dl.acm.org/doi/10.1145/3340531.3412697.
[104] RaphaelLouca,MoumitaBhattacharya,DianeHu,andLiangjieHong.Jointoptimiza-
tionofprofitandrelevanceforrecommendationsystemsine-commerce. InRMSE@
RecSys,2019.
[105] Runyu Ma, Hantian Li, Jin Cen, and Amrinder Arora. Placement-and-Profit-
Aware Association Rules Mining:. In Proceedings of the 11th International Confer-
ence on Agents and Artificial Intelligence, pages 639–646, Prague, Czech Republic,
2019.SCITEPRESS-ScienceandTechnologyPublications. ISBN978-989-758-350-
6. doi: 10.5220/0007380606390646. URL http://www.scitepress.org/
DigitalLibrary/Link.aspx?doi=10.5220/0007380606390646.
[106] Cheng-Lung Huang, Mu-Chen Chen, Wen-Chen Huang, and Sheng-Huang Huang.
Incorporatingfrequency,recencyandprofitinsequentialpatternbasedrecommender
systems. IntelligentDataAnalysis,17(5):899–916,2013.
96

[107] Gaddiel Desirena, Armando Diaz, Jalil Desirena, Ismael Moreno, and Daniel Garcia.
Maximizing customer lifetime value using stacked neural networks: An insurance in-
dustryapplication. In201918thIEEEInternationalConferenceOnMachineLearning
AndApplications(ICMLA),pages541–544,2019. doi: 10.1109/ICMLA.2019.00101.
[108] NadaGhanem,StephanLeitner,andDietmarJannach. Balancingconsumerandbusi-
ness value of recommender systems: A simulation-based analysis. Electronic Com-
merce Research and Applications, 55:101195, 2022. ISSN 1567-4223. doi: https:
//doi.org/10.1016/j.elerap.2022.101195. URLhttps://www.sciencedirect.com/
science/article/pii/S1567422322000783.
[109] GuyAridorandDuarteGonçalves.Recommenders’originals:Thewelfareeffectsofthe
dualroleofplatformsasproducersandrecommendersystems. InternationalJournalof
IndustrialOrganization,83:102845,2022.
[110] Bo Zhou and Tianxin Zou. Competing for recommendations: The strategic impact
ofpersonalizedproductrecommendationsinonlinemarketplaces. MarketingScience,
2022.
[111] RuixinYang,MingyangXu,PaulJones,andNagizaSamatova. Realtimeutility-based
recommendation for revenue optimization via an adaptive online Top-K high utility
itemsets mining model. In 2017 13th International Conference on Natural Computa-
tion,FuzzySystemsandKnowledgeDiscovery(ICNC-FSKD),pages1859–1866,Guilin,
July2017.IEEE. ISBN978-1-5386-2165-3. doi: 10.1109/FSKD.2017.8393050. URL
https://ieeexplore.ieee.org/document/8393050/.
[112] Yuanchun Jiang and Yezheng Liu. Optimization of online promotion: a profit-
maximizingmodelintegratingpricediscountandproductrecommendation. Interna-
tionalJournalofInformationTechnology&DecisionMaking,11(05):961–982,Septem-
ber 2012. ISSN 0219-6220, 1793-6845. doi: 10.1142/S0219622012500289. URL
https://www.worldscientific.com/doi/abs/10.1142/S0219622012500289.
[113] YuanchunJiang, JenniferShang, YezhengLiu, andJerroldMay. Redesigningpromo-
tionstrategyfore-commercecompetitivenessthroughpricingandrecommendation.In-
ternationalJournalofProductionEconomics,167:257–270,2015.
[114] PatrickHosein,InzamamRahaman,KeanuNichols,andKiranMaharaj. Recommen-
dationsforlong-termprofitoptimization. InImpactRS@RecSys,2019.
97

[115] BjörnBrodén,MikaelHammar,BengtJ.Nilsson,andDimitrisParaschakis. ABandit-
BasedEnsembleFrameworkforExploration/ExploitationofDiverseRecommendation
Components: AnExperimentalStudywithinE-Commerce. ACMTransactionsonIn-
teractive Intelligent Systems, 10(1):1–32, January 2020. ISSN 2160-6455, 2160-6463.
doi: 10.1145/3237187. URLhttps://dl.acm.org/doi/10.1145/3237187.
[116] ShreyaBasu. Personalizedproductrecommendationsandfirmperformance. Electronic
Commerce Research and Applications, 48:101074, July 2021. ISSN 1567-4223. doi:
10.1016/j.elerap.2021.101074. URLhttps://www.sciencedirect.com/science/
article/pii/S1567422321000466.
[117] EmanueleCavenaghi,LorenzoCamaione,PaoloMinasi,GabrieleSottocornola,Fabio
Stella,andMarkusZanker.Anonlineexperimentofaprice-basedre-rankalgorithm.In
RecSysWorkshoponRecommendersinTourism(RecTour2022),2022.
[118] DongwonLee,KihwanNam,IngooHan,andKanghyunCho. Fromfreetofee: Mon-
etizingdigitalcontentthroughexpectedutility-basedrecommendersystems. Informa-
tion&Management,59(6):103681,2022.
[119] Duen-Ren Liu and Ya-Yueh Shih. Hybrid approaches to product recommenda-
tion based on customer lifetime value and purchase preferences. Journal of Systems
and Software, 77(2):181–191, August 2005. ISSN 01641212. doi: 10.1016/j.jss.
2004.08.031. URL https://linkinghub.elsevier.com/retrieve/pii/
S0164121204001426.
[120] Duen-RenLiuandYa-YuehShih. IntegratingAHPanddataminingforproductrec-
ommendationbasedoncustomerlifetimevalue. Information&Management,42(3):
387–400, March 2005. ISSN 03787206. doi: 10.1016/j.im.2004.01.008. URL
https://linkinghub.elsevier.com/retrieve/pii/S0378720604000394.
[121] Ya-YuehShihandDuen-RenLiu. HybridRecommendationApproaches: Collabora-
tiveFilteringviaValuableContentInformation.thHawaiiInternationalConferenceon
SystemSciences,page7,2005.
[122] Y Shih and D Liu. Product recommendation approaches: Collaborative filtering via
customer lifetime value and customer demands. Expert Systems with Applications, 35
(1-2):350–360,July2008. ISSN09574174. doi: 10.1016/j.eswa.2007.07.055. URL
https://linkinghub.elsevier.com/retrieve/pii/S0957417407002539.
98

[123] ZahraTabaeiandMohammadFathian. Usingcustomerlifetimevaluemodelforprod-
uct recommendation: An electronic retailing case study. International Journal of e-
Education,e-Business,e-Managementande-Learning,2(1):77,2012.
[124] Cheng Long, Raymond Chi-Wing Wong, and Victor Junqiu Wei. Profit Maximiza-
tionwithSufficientCustomerSatisfactions. ACMTransactionsonKnowledgeDiscov-
eryfromData, 12(2):1–34, April2018. ISSN1556-4681, 1556-472X. doi: 10.1145/
3110216. URLhttps://dl.acm.org/doi/10.1145/3110216.
[125] KameliaAryafar, DevinGuillory, and LiangjieHong. An Ensemble-basedApproach
toClick-ThroughRatePredictionforPromotedListingsatEtsy. InProceedingsofthe
ADKDD’17,pages1–6,HalifaxNSCanada,August2017.ACM. ISBN978-1-4503-
5194-2.doi: 10.1145/3124749.3124758.URLhttps://dl.acm.org/doi/10.1145/
3124749.3124758.
[126] Yufei Feng, Fuyu Lv, Weichen Shen, Menghan Wang, Fei Sun, Yu Zhu, and Keping
Yang. Deepsessioninterestnetworkforclick-throughrateprediction. InProceedings
of the 28th International Joint Conference on Artificial Intelligence, pages 2301–2307,
2019.
[127] Thore Graepel, Joaquin Quinonero Candela, Thomas Borchert, and Ralf Herbrich.
Web-scalebayesianclick-throughratepredictionforsponsoredsearchadvertisinginmi-
crosoft’sbingsearchengine. InProceedingsofthe27thInternationalConferenceonIn-
ternationalConferenceonMachineLearning.Omnipress,2010.
[128] H.BrendanMcMahan,GaryHolt,D.Sculley,MichaelYoung,DietmarEbner,Julian
Grady, Lan Nie, Todd Phillips, Eugene Davydov, Daniel Golovin, Sharat Chikkerur,
DanLiu,MartinWattenberg,ArnarMarHrafnkelsson,TomBoulos,andJeremyKu-
bica. Adclickprediction: aviewfromthetrenches. InProceedingsofthe19thACM
SIGKDD international conference on Knowledge discovery and data mining, pages
1222–1230,ChicagoIllinoisUSA,August2013.ACM.ISBN978-1-4503-2174-7.doi:
10.1145/2487575.2488200. URLhttps://dl.acm.org/doi/10.1145/2487575.
2488200.
[129] OlivierChapelle,ErenManavoglu,andRomerRosales. SimpleandScalableResponse
PredictionforDisplayAdvertising. ACMTransactionsonIntelligentSystemsandTech-
nology,5(4):34,2014.
99

[130] XinranHe,StuartBowers,JoaquinQuiñoneroCandela,JunfengPan,OuJin,Tianbing
Xu,BoLiu,TaoXu,YanxinShi,AntoineAtallah,andRalfHerbrich.PracticalLessons
from Predicting Clicks on Ads at Facebook. In Proceedings of 20th ACM SIGKDD
ConferenceonKnowledgeDiscoveryandDataMining-ADKDD’14,pages1–9,New
York,NY,USA,2014.ACMPress. ISBN978-1-4503-2999-6. doi: 10.1145/2648584.
2648589. URLhttp://dl.acm.org/citation.cfm?doid=2648584.2648589.
[131] GuoruiZhou, XiaoqiangZhu, ChenruSong, YingFan, HanZhu, XiaoMa, Yanghui
Yan,JunqiJin,HanLi,andKunGai. DeepInterestNetworkforClick-ThroughRate
Prediction. In Proceedings of the 24th ACM SIGKDD International Conference on
Knowledge Discovery & Data Mining, pages 1059–1068, London United Kingdom,
July 2018. ACM. ISBN 978-1-4503-5552-0. doi: 10.1145/3219819.3219823. URL
https://dl.acm.org/doi/10.1145/3219819.3219823.
[132] Wentao Ouyang, Xiuwu Zhang, Li Li, Heng Zou, Xin Xing, Zhaojie Liu, and Yan-
long Du. Deep Spatio-Temporal Neural Networks for Click-Through Rate Predic-
tion. In Proceedings of the 25th ACM SIGKDD International Conference on Knowl-
edge Discovery & Data Mining, pages 2078–2086, Anchorage AK USA, July 2019.
ACM. ISBN 978-1-4503-6201-6. doi: 10.1145/3292500.3330655. URL https:
//dl.acm.org/doi/10.1145/3292500.3330655.
[133] LihongLi,WeiChu,JohnLangford,andRobertE.Schapire. Acontextual-banditap-
proachtopersonalizednewsarticlerecommendation.InProceedingsofthe19thinterna-
tionalconferenceonWorldwideweb-WWW’10,page661,Raleigh,NorthCarolina,
USA, 2010. ACMPress. ISBN 978-1-60558-799-8. doi: 10.1145/1772690.1772758.
URLhttp://portal.acm.org/citation.cfm?doid=1772690.1772758.
[134] Omar Besbes, Yonatan Gur, and Assaf Zeevi. Optimization in online content recom-
mendationservices: Beyondclick-throughrates. Manufacturing&ServiceOperations
Management,18(1):15–33,2016.
[135] Morteza Zihayat, Anteneh Ayanso, Xing Zhao, Heidar Davoudi, and Aijun An. A
utility-based news recommendation system. Decision Support Systems, 117:14–27,
2019.
100

[136] PaschaliaSpyridou,ConstantinosDjouvas,andDimitraMilioni.Modelingandvalidat-
inganewsrecommenderalgorithminamainstreammedium-sizednewsorganization:
Anexperimentalapproach. FutureInternet,14(10):284,2022.
[137] YayuZhou,BobbyJCalder,EdwardCMalthouse,andYasamanKamyabHessary. Not
allclicksareequal: detectingengagementwithdigitalcontent. JournalofMediaBusi-
nessStudies,pages1–18,2021.
[138] Mozhgan Karimi, Dietmar Jannach, and Michael Jugovac. News recommender
systems–surveyandroadsahead. InformationProcessing&Management,54(6):1203–
1227,2018.
[139] Chong Feng, Muzammil Khan, Arif Ur Rahman, and Arshad Ahmad. News recom-
mendation systems-accomplishments, challenges & future directions. IEEE Access, 8:
16702–16725,2020.
[140] Tomoharu Iwata, Kazumi Saito, and Takeshi Yamada. Recommendation method for
extendingsubscriptionperiods.InProceedingsofthe12thACMSIGKDDinternational
conferenceonKnowledgediscoveryanddatamining-KDD’06,page574,Philadelphia,
PA,USA,2006.ACMPress.ISBN978-1-59593-339-3.doi:10.1145/1150402.1150470.
URLhttp://portal.acm.org/citation.cfm?doid=1150402.1150470.
[141] T.Iwata,K.Saito,andT.Yamada.RecommendationMethodforImprovingCustomer
LifetimeValue. IEEETransactionsonKnowledgeandDataEngineering,20(9):1254–
1263,September2008. ISSN1041-4347. doi: 10.1109/TKDE.2008.55. URLhttp:
//ieeexplore.ieee.org/document/4479464/.
[142] Shanfeng Wang, Maoguo Gong, Haoliang Li, and Junwei Yang. Multi-objective op-
timization for long tail recommendation. Knowledge-Based Systems, 104:145–155,
July 2016. ISSN 09507051. doi: 10.1016/j.knosys.2016.04.018. URL https:
//linkinghub.elsevier.com/retrieve/pii/S0950705116300600.
[143] Arda Antikacioglu and R. Ravi. Post Processing Recommender Systems for Diver-
sity. In Proceedings of the 23rd ACM SIGKDD International Conference on Knowl-
edge Discovery and Data Mining, pages 707–716, Halifax NS Canada, August 2017.
ACM. ISBN 978-1-4503-4887-4. doi: 10.1145/3097983.3098173. URL https:
//dl.acm.org/doi/10.1145/3097983.3098173.
101

[144] ElahehMalekzadehHamedaniandMarjanKaedi. Recommendingthelongtailitems
throughpersonalizeddiversification. Knowledge-BasedSystems,164:348–357,2019.
[145] Xiaochen Zhang, Pedro Ferreira, Miguel Godinho de Matos, and Rodrigo Belo.
WelfareProperties of Profit MaximizingRecommender Systems: Theoryand Results
from a Randomized Experiment. MIS Quarterly, 45(1):1–43, March 2021. ISSN
02767783,21629730.doi:10.25300/MISQ/2021/14971.URLhttps://misq.org/
welfare-properties-of-profit-maximizing-recommender-systems-theory-and-results-from-a-randomized-experiment.
html.
[146] CarlosAGomez-UribeandNeilHunt. Thenetflixrecommendersystem: Algorithms,
businessvalue, andinnovation. ACMTransactionsonManagementInformationSys-
tems(TMIS),6(4):1–19,2015.
[147] Matevž Kunaver and Tomaž Požrl. Diversity in recommender systems–a survey.
Knowledge-basedsystems,123:154–162,2017.
[148] MicrosoftCorporation. ExampleDatabaseFoodMartofMicrosoftAnalysisServices,
1998. URLhttps://github.com/julianhyde/foodmart-data-hsqldb.
[149] Jianmo Ni, Jiacheng Li, and Julian McAuley. Justifying Recommendations using
Distantly-LabeledReviewsandFine-GrainedAspects. InProceedingsofthe2019Con-
ferenceonEmpiricalMethodsinNaturalLanguageProcessingandthe9thInternational
JointConferenceonNaturalLanguageProcessing(EMNLP-IJCNLP),pages188–197,
HongKong,China,November2019.AssociationforComputationalLinguistics. doi:
10.18653/v1/D19-1018. URLhttps://aclanthology.org/D19-1018.
[150] Ventatesan. Dunnhumby - the complete journey, 2007. URL https://www.
dunnhumby.com/source-files/.
[151] Philippe Fournier-Viger, Jerry Chun-Wei Lin, Antonio Gomariz, Ted Gueniche,
AzadehSoltani,ZhihongDeng,andHoangThanhLam. Thespmfopen-sourcedata
mininglibraryversion2. InJointEuropeanconferenceonmachinelearningandknowl-
edgediscoveryindatabases,pages36–40.Springer,2016.
[152] Pisharath.NU-MineBenchversion2.0datasetandtechnicalreport.URI:http://cucis.ece.
northwestern.edu/projects/DMS/MineBench.html(lastaccesson2March2015),2005.
102

[153] Matthew Richardson and Pedro Domingos. Mining knowledge-sharing sites for vi-
ralmarketing. InProceedingsoftheeighthACMSIGKDDinternationalconferenceon
Knowledgediscoveryanddatamining,pages61–70,2002.
[154] F. Maxwell Harper and Joseph A. Konstan. The MovieLens Datasets: History and
Context.ACMTransactionsonInteractiveIntelligentSystems,5(4):1–19,January2016.
ISSN2160-6455,2160-6463. doi: 10.1145/2827872. URLhttps://dl.acm.org/
doi/10.1145/2827872.
[155] JamesBennett,StanLanning,etal. Thenetflixprize. InProceedingsofKDDcupand
workshop,volume2007,page35.Citeseer,2007.
[156] Cai-NicolasZiegler,SeanMMcNee,JosephAKonstan,andGeorgLausen.Improving
recommendationliststhroughtopicdiversification. InProceedingsofthe14thinterna-
tionalconferenceonWorldWideWeb,pages22–32,2005.
[157] BrianMcFee,ThierryBertin-Mahieux,DanielPWEllis,andGertRGLanckriet. The
million song dataset challenge. In Proceedings of the 21st International Conference on
WorldWideWeb,pages909–916,2012.
[158] KenGoldberg,TheresaRoeder,DhruvGupta,andChrisPerkins. Eigentaste: Acon-
stanttimecollaborativefilteringalgorithm. informationretrieval,4(2):133–151,2001.
[159] JulianMcAuley,RahulPandey,andJureLeskovec.InferringNetworksofSubstitutable
andComplementaryProducts.InProceedingsofthe21thACMSIGKDDInternational
Conference on Knowledge Discovery and Data Mining, pages 785–794, Sydney NSW
Australia, August 2015. ACM. ISBN 978-1-4503-3664-2. doi: 10.1145/2783258.
2783381. URLhttps://dl.acm.org/doi/10.1145/2783258.2783381.
[160] XingyueZhang,JamesADearden,andYuliangYao. Letthemstayorletthemgo? on-
lineretailerpricingstrategyformanagingstockouts. ProductionandOperationsMan-
agement,2022.
[161] Chi Zhou, Mingming Leng, Zhibing Liu, Xin Cui, and Jing Yu. The impact of rec-
ommendersystemsandpricingstrategiesonbrandcompetitionandconsumersearch.
ElectronicCommerceResearchandApplications,53:101144,2022.
103

[162] AselaGunawardana,GuyShani,andSivanYogev.Evaluatingrecommendersystems.In
Recommendersystemshandbook,pages547–601.Springer,2022.
[163] Davinder Kaur, Suleyman Uslu, Kaley J Rittichier, and Arjan Durresi. Trustworthy
artificialintelligence: areview. ACMComputingSurveys(CSUR),55(2):1–38,2022.
[164] AlexandraVultureanu-AlbişiandCostinBădică. Asurveyoneffectsofaddingexplana-
tionstorecommendersystems.ConcurrencyandComputation: PracticeandExperience,
pagee6834,2022.
[165] NavaTintarevandJudithMasthoff. ExplainingRecommendations: DesignandEval-
uation. In Francesco Ricci, Lior Rokach, and Bracha Shapira, editors, Recommender
SystemsHandbook,pages353–382.SpringerUS,Boston,MA,2015.ISBN978-1-4899-
7637-6. doi: 10.1007/978-1-4899-7637-6_10. URL https://doi.org/10.1007/
978-1-4899-7637-6_10.
[166] Yongfeng Zhang and Xu Chen. Explainable Recommendation: A Survey and New
Perspectives. FoundationsandTrends®inInformationRetrieval, 14(1):1–101, 2020.
ISSN1554-0669,1554-0677. doi: 10.1561/1500000066. URLhttp://arxiv.org/
abs/1804.11192. 297citations(SemanticScholar/arXiv)[2022-02-14]297citations
(SemanticScholar/DOI)[2022-02-14]arXiv: 1804.11192.
[167] Giacomo Balloccu, Ludovico Boratto, Gianni Fenu, and Mirko Marras. XRecSys:
A framework for path reasoning quality in explainable recommendation. Software
Impacts, 14:100404, December 2022. ISSN 26659638. doi: 10.1016/j.simpa.
2022.100404. URL https://linkinghub.elsevier.com/retrieve/pii/
S266596382200094X.
[168] JonathanL.Herlocker,JosephA.Konstan,LorenG.Terveen,andJohnT.Riedl. Eval-
uatingcollaborativefilteringrecommendersystems.ACMTransactionsonInformation
Systems,22(1):5–53,January2004.ISSN1046-8188,1558-2868.doi:10.1145/963770.
963772. URLhttps://dl.acm.org/doi/10.1145/963770.963772.
[169] Asela Gunawardana and Guy Shani. Evaluating Recommender Systems. In
Francesco Ricci, Lior Rokach, and Bracha Shapira, editors, Recommender Systems
Handbook,pages265–308.SpringerUS,Boston,MA,2015. ISBN978-1-4899-7637-
6. doi: 10.1007/978-1-4899-7637-6_8. URL https://doi.org/10.1007/
978-1-4899-7637-6_8.
104

[170] Thiago Silveira, Min Zhang, Xiao Lin, Yiqun Liu, and Shaoping Ma. How good
your recommender system is? A survey on evaluations in recommendation. Interna-
tionalJournalofMachineLearningandCybernetics,10(5):813–831,May2019. ISSN
1868-808X. doi: 10.1007/s13042-017-0762-9. URLhttps://doi.org/10.1007/
s13042-017-0762-9.
[171] Janneth Chicaiza and Priscila Valdiviezo-Diaz. Explainable Recommender Systems:
From Theory to Practice. In Atulya K. Nagar, Dharm Singh Jat, Durgesh Kumar
Mishra,andAmitJoshi,editors,IntelligentSustainableSystems,LectureNotesinNet-
worksandSystems,pages449–459,Singapore,2023.SpringerNature. ISBN978-981-
19766-3-6. doi: 10.1007/978-981-19-7663-6_42.
[172] Xu Chen, Yongfeng Zhang, and Ji-Rong Wen. Measuring ”Why” in Recommender
Systems: a Comprehensive Survey on the Evaluation of Explainable Recommenda-
tion, February 2022. URL http://arxiv.org/abs/2202.06466. Number:
arXiv:2202.06466arXiv:2202.06466[cs].
[173] Behnoush Abdollahi and Olfa Nasraoui. Explainable Matrix Factorization for Col-
laborative Filtering. In Proceedings of the 25th International Conference Companion
on World Wide Web, WWW ’16 Companion, pages 5–6, Republic and Canton of
Geneva,CHE,April2016.InternationalWorldWideWebConferencesSteeringCom-
mittee. ISBN 978-1-4503-4144-8. doi: 10.1145/2872518.2889405. URL https:
//doi.org/10.1145/2872518.2889405.
[174] XiangWang, XiangnanHe, FuliFeng, LiqiangNie, andTat-SengChua. TEM:Tree-
enhancedEmbeddingModelforExplainableRecommendation. InProceedingsofthe
2018WorldWideWebConference,WWW’18,pages1543–1552,RepublicandCan-
ton of Geneva, CHE, April 2018. International World Wide Web Conferences Steer-
ing Committee. ISBN 978-1-4503-5639-8. doi: 10.1145/3178876.3186066. URL
https://doi.org/10.1145/3178876.3186066.
[175] Yu-Yao Liu, Bo Yang, Hong-Bin Pei, and Jing Huang. Neural Explainable Recom-
mender Model Based on Attributes and Reviews. Journal of Computer Science and
Technology, 35(6):1446–1460, November 2020. ISSN 1860-4749. doi: 10.1007/
s11390-020-0152-8. URLhttps://doi.org/10.1007/s11390-020-0152-8.
105

[176] Sina Mohseni, Niloofar Zarei, and Eric D. Ragan. A Multidisciplinary Survey and
FrameworkforDesignandEvaluationofExplainableAISystems. ACMTransactions
on Interactive Intelligent Systems, 11(3-4):24:1–24:45, 2021. ISSN 2160-6455. doi:
10.1145/3387166. URLhttps://doi.org/10.1145/3387166.
[177] Amina Adadi and Mohammed Berrada. Peeking Inside the Black-Box: A Survey on
Explainable Artificial Intelligence (XAI). IEEE Access, 6:52138–52160, 2018. ISSN
2169-3536. doi: 10.1109/ACCESS.2018.2870052. ConferenceName: IEEEAccess.
[178] AlexandraVultureanu-AlbişiandCostin Bădică. Asurveyoneffectsof addingexpla-
nations to recommender systems. Concurrency and Computation: Practice and Ex-
perience, 34(20):e6834, 2022. ISSN 1532-0634. doi: 10.1002/cpe.6834. URL
https://onlinelibrary.wiley.com/doi/abs/10.1002/cpe.6834. _eprint:
https://onlinelibrary.wiley.com/doi/pdf/10.1002/cpe.6834.
[179] JonathanL.Herlocker, JosephA.Konstan, andJohnRiedl. Explainingcollaborative
filtering recommendations. In Proceedings of the 2000 ACM conference on Computer
supportedcooperativework,CSCW’00,pages241–250,NewYork,NY,USA,2000.As-
sociationforComputingMachinery. ISBN978-1-58113-222-9. doi: 10.1145/358916.
358995. URLhttps://doi.org/10.1145/358916.358995.
[180] Jesse Vig, Shilad Sen, and John Riedl. Tagsplanations: explaining recommendations
usingtags. InProceedingsofthe14thinternationalconferenceonIntelligentuserinter-
faces,IUI’09,pages47–56,NewYork,NY,USA,February2009.AssociationforCom-
putingMachinery. ISBN978-1-60558-168-2. doi: 10.1145/1502650.1502661. URL
https://doi.org/10.1145/1502650.1502661.
[181] Florian Pecune, Shruti Murali, Vivian Tsai, Yoichi Matsuyama, and Justine Cassell.
A Model of Social Explanations for a Conversational Movie Recommendation Sys-
tem. In Proceedings of the 7th International Conference on Human-Agent Interac-
tion, HAI ’19, pages 135–143, New York, NY, USA, 2019. Association for Comput-
ing Machinery. ISBN 978-1-4503-6922-0. doi: 10.1145/3349537.3351899. URL
https://doi.org/10.1145/3349537.3351899. 23 citations (Semantic Scholar/-
DOI)[2022-02-14].
[182] Weiquan Wang and Izak Benbasat. Recommendation Agents for Electronic Com-
merce: Effects of Explanation Facilities on Trusting Beliefs. Journal of Manage-
106

ment Information Systems, 23(4):217–246, 2007. ISSN 0742-1222. doi: 10.2753/
MIS0742-1222230410. URLhttps://doi.org/10.2753/MIS0742-1222230410.
[183] Alexis Papadimitriou, Panagiotis Symeonidis, and Yannis Manolopoulos. A general-
ized taxonomy of explanations styles for traditional and social recommender systems.
Data Mining and Knowledge Discovery, 24(3):555–583, May 2012. ISSN 1573-
756X. doi: 10.1007/s10618-011-0215-0. URL https://doi.org/10.1007/
s10618-011-0215-0.
[184] Nava Tintarev and Judith Masthoff. Evaluating the effectiveness of explanations for
recommendersystems. UserModelingandUser-AdaptedInteraction, 22(4):399–439,
October 2012. ISSN 1573-1391. doi: 10.1007/s11257-011-9117-5. URL https://
doi.org/10.1007/s11257-011-9117-5.
[185] MouadhGuesmi, MohamedAmine Chatti, Laura Vorgerd, Shoeb Joarder, Shadi Zu-
mor,YiqiSun,FangzhengJi,andArhamMuslim. On-demandPersonalizedExplana-
tionforTransparentRecommendation.InAdjunctProceedingsofthe29thACMConfer-
enceonUserModeling,AdaptationandPersonalization,pages246–252.Associationfor
ComputingMachinery,NewYork,NY,USA,2021. ISBN978-1-4503-8367-7. URL
https://doi.org/10.1145/3450614.3464479.
[186] Ruijing Zhao, Izak Benbasat, and Hasan Cavusoglu. Transparency in Advice-Giving
Systems:AFrameworkandaResearchModelforTransparencyProvision.volume2327
of CEUR Workshop Proceedings, 2019. URL https://ceur-ws.org/Vol-2327/
IUI19WS-IUIATEC-2.pdf. ISSN:1613-0073.
[187] Mouadh Guesmi, Mohamed Amine Chatti, Laura Vorgerd, Shoeb Joarder, Qurat Ul
Ain,ThaoNgo,ShadiZumor,YiqiSun,FangzhengJi,andArhamMuslim. Inputor
Output: EffectsofExplanationFocusonthePerceptionofExplainableRecommenda-
tion with Varying Level of Details. In Proceedings of the 8th Joint Workshop on Inter-
facesandHumanDecisionMakingforRecommenderSystems,volume2948ofCEUR
WorkshopProceedings,pages55–72,OnlineEvent,September,September2021.CEUR.
URLhttps://ceur-ws.org/Vol-2948/#paper4. ISSN:1613-0073.
[188] Giulia Vilone and Luca Longo. Notions of explainability and evaluation approaches
forexplainableartificialintelligence. InformationFusion,76(C):89–106,2021. ISSN
107

1566-2535. doi: 10.1016/j.inffus.2021.05.009. URLhttps://doi.org/10.1016/j.
inffus.2021.05.009.
[189] UpolEhsanandMarkO.Riedl. Human-CenteredExplainableAI:TowardsaReflec-
tiveSociotechnicalApproach. InConstantineStephanidis,MasaakiKurosu,Helmut
Degen, and Lauren Reinerman-Jones, editors, HCI International 2020 - Late Break-
ingPapers: MultimodalityandIntelligence,LectureNotesinComputerScience,pages
449–466, Cham, 2020. Springer International Publishing. ISBN 978-3-030-60117-1.
doi: 10.1007/978-3-030-60117-1_33.
[190] Lauren Shluzas, Joel A. Sadler, Rebecca Currano, Martin Steinert, Riitta Katila, and
TarynSanks.ComparingNoviceandExpertUserInputsinEarlyStageProductDesign,
December2012. URLhttps://papers.ssrn.com/abstract=2372677.
[191] Donghee Shin. How do users interact with algorithm recommender systems? The
interaction of users, algorithms, and performance. Computers in Human Behav-
ior, 109:106344, August 2020. ISSN 0747-5632. doi: 10.1016/j.chb.2020.
106344. URL https://www.sciencedirect.com/science/article/pii/
S0747563220300984.
[192] Chun-HuaTsaiandPeterBrusilovsky. ExplainingSocialRecommendationstoCasual
Users: DesignPrinciplesandOpportunities. InProceedingsofthe23rdInternational
Conference on Intelligent User Interfaces Companion, IUI ’18 Companion, pages 1–2,
NewYork,NY,USA,March2018.AssociationforComputingMachinery. ISBN978-
1-4503-5571-1. doi: 10.1145/3180308.3180368. URLhttps://doi.org/10.1145/
3180308.3180368.
[193] VicenteDominguez,PabloMessina,IvaniaDonoso-Guzmán,andDenisParra. Theef-
fectofexplanationsandalgorithmicaccuracyonvisualrecommendersystemsofartistic
images.InProceedingsofthe24thInternationalConferenceonIntelligentUserInterfaces,
IUI’19,pages408–416,NewYork,NY,USA,March2019.AssociationforComput-
ing Machinery. ISBN 978-1-4503-6272-6. doi: 10.1145/3301275.3302274. URL
https://doi.org/10.1145/3301275.3302274.
[194] Erasmo Purificato, Baalakrishnan Aiyer Manikandan, Prasanth Vaidya Karanam, Ma-
hanteshVishvanathPattadkal, andErnestoWilliamDeLuca. EvaluatingExplainable
InterfacesforaKnowledgeGraph-BasedRecommenderSystem. InPeterBrusilovsky,
108

MarcodeGemmis,AlexanderFelfernig,ElisabethLex,PasqualeLops,GiovanniSemer-
aro,andMartijnC.Willemsen,editors,Proceedingsofthe8thJointWorkshoponInter-
facesandHumanDecisionMakingforRecommenderSystems,volume2948ofCEUR
WorkshopProceedings,pages73–88,OnlineEvent,September,September2021.CEUR.
URLhttps://ceur-ws.org/Vol-2948/#paper5. ISSN:1613-0073.
[195] Brian Y. Lim, Anind K. Dey, and Daniel Avrahami. Why and why not explanations
improve the intelligibility of context-aware intelligent systems. In Proceedings of the
SIGCHI Conference on Human Factors in Computing Systems, CHI ’09, pages 2119–
2128,NewYork,NY,USA,April2009.AssociationforComputingMachinery. ISBN
978-1-60558-246-7. doi: 10.1145/1518701.1519023. URL https://doi.org/10.
1145/1518701.1519023.
[196] Yongfeng Zhang, Min Zhang, Yi Zhang, Yiqun Liu, and Shaoping Ma. Understand-
ingtheSparsity: AugmentedMatrixFactorizationwithSampledConstraintsonUnob-
servables. InProceedingsofthe23rdACMInternationalConferenceonConferenceon
Information and Knowledge Management, CIKM ’14, pages 1189–1198, New York,
NY,USA,November2014.AssociationforComputingMachinery. ISBN978-1-4503-
2598-1.doi:10.1145/2661829.2661976.URLhttps://doi.org/10.1145/2661829.
2661976.
[197] Pigi Kouki, James Schaffer, Jay Pujara, John O’Donovan, and Lise Getoor. Gen-
erating and Understanding Personalized Explanations in Hybrid Recommender Sys-
tems. ACMTransactionsonInteractiveIntelligentSystems,10(4):31:1–31:40,Novem-
ber 2020. ISSN 2160-6455. doi: 10.1145/3365843. URL https://doi.org/10.
1145/3365843.
[198] ShlomoBerkovsky,RonnieTaib,andDanConway. HowtoRecommend? UserTrust
FactorsinMovieRecommenderSystems. InProceedingsofthe22ndInternationalCon-
ference on Intelligent User Interfaces, IUI ’17, pages 287–300, New York, NY, USA,
March2017.AssociationforComputingMachinery. ISBN978-1-4503-4348-0. doi:
10.1145/3025171.3025209. URLhttps://doi.org/10.1145/3025171.3025209.
[199] Tim Miller. Explanation in Artificial Intelligence: Insights from the Social Sciences.
arXiv:1706.07269[cs], August2018. URLhttp://arxiv.org/abs/1706.07269.
arXiv: 1706.07269.
109

[200] TomM.vanEngersandDennisM.deVries. GovernmentalTransparencyintheEraof
ArtificialIntelligence. LegalKnowledgeandInformationSystems, pages33–42, 2019.
doi: 10.3233/FAIA190304. URLhttps://ebooks.iospress.nl/doi/10.3233/
FAIA190304. Publisher: IOSPress.
[201] FrancescoSovrano,FabioVitali,andMonicaPalmirani. ModellingGDPR-Compliant
Explanations for Trustworthy AI. In Andrea Kő, Enrico Francesconi, Gabriele Kot-
sis, A Min Tjoa, and Ismail Khalil, editors, Electronic Government and the Informa-
tion Systems Perspective, Lecture Notes in Computer Science, pages 219–233, Cham,
2020. Springer International Publishing. ISBN 978-3-030-58957-8. doi: 10.1007/
978-3-030-58957-8_16.
[202] Alejandro Barredo Arrieta, Natalia Díaz-Rodríguez, Javier Del Ser, Adrien Bennetot,
Siham Tabik, Alberto Barbado, Salvador Garcia, Sergio Gil-Lopez, Daniel Molina,
RichardBenjamins,RajaChatila,andFranciscoHerrera. ExplainableArtificialIntelli-
gence(XAI):Concepts, taxonomies, opportunitiesandchallengestowardresponsible
AI.InformationFusion,58:82–115,June2020.ISSN1566-2535.doi:10.1016/j.inffus.
2019.12.012. URLhttps://www.sciencedirect.com/science/article/pii/
S1566253519308103.
[203] Alexandra Vultureanu-Albişi and Costin Bădică. Improving Students’ Performance
byInterpretableExplanationsusingEnsembleTree-BasedApproaches. In2021IEEE
15thInternationalSymposiumonAppliedComputationalIntelligenceandInformatics
(SACI),pages215–220,May2021. doi: 10.1109/SACI51354.2021.9465558.
[204] MarcoTulioRibeiro,SameerSingh,andCarlosGuestrin. ”WhyShouldITrustYou?”:
ExplainingthePredictionsofAnyClassifier.InProceedingsofthe22ndACMSIGKDD
InternationalConferenceonKnowledgeDiscoveryandDataMining, KDD’16, pages
1135–1144,NewYork,NY,USA,2016.AssociationforComputingMachinery. ISBN
978-1-4503-4232-2. doi: 10.1145/2939672.2939778. URLhttps://doi.org/10.
1145/2939672.2939778.
[205] Nasim Sonboli, Jessie J. Smith, Florencia Cabral Berenfus, Robin Burke, and Casey
Fiesler. Fairness and Transparency in Recommendation: The Users’ Perspective. In
Proceedings of the 29th ACM Conference on User Modeling, Adaptation and Personal-
ization,UMAP’21,pages274–279,NewYork,NY,USA,2021.AssociationforCom-
110

putingMachinery. ISBN978-1-4503-8366-0. doi: 10.1145/3450613.3456835. URL
https://doi.org/10.1145/3450613.3456835.
[206] LarissaChazetteandKurtSchneider. Explainabilityasanon-functionalrequirement:
challengesandrecommendations. RequirementsEngineering,25(4):493–514,Decem-
ber 2020. ISSN 1432-010X. doi: 10.1007/s00766-020-00333-1. URL https:
//doi.org/10.1007/s00766-020-00333-1.
[207] Yongfeng Zhang, Guokun Lai, Min Zhang, Yi Zhang, Yiqun Liu, and Shaoping Ma.
Explicitfactormodelsforexplainablerecommendationbasedonphrase-levelsentiment
analysis. In Proceedings of the 37th international ACM SIGIR conference on Research
&developmentininformationretrieval,SIGIR’14,pages83–92,NewYork,NY,USA,
2014.AssociationforComputingMachinery. ISBN978-1-4503-2257-7. doi: 10.1145/
2600428.2609579. URLhttps://doi.org/10.1145/2600428.2609579.
[208] Juntao Tan, Shuyuan Xu, Yingqiang Ge, Yunqi Li, Xu Chen, and Yongfeng Zhang.
Counterfactual Explainable Recommendation. In Proceedings of the 30th ACM In-
ternationalConferenceon Information& Knowledge Management, CIKM ’21, pages
1784–1793,NewYork,NY,USA,2021.AssociationforComputingMachinery. ISBN
978-1-4503-8446-9. doi: 10.1145/3459637.3482420. URLhttps://doi.org/10.
1145/3459637.3482420.
[209] Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu. BLEU: a method
for automatic evaluation of machine translation. In Proceedings of the 40th Annual
Meeting on Association for Computational Linguistics - ACL ’02, page 311, Philadel-
phia, Pennsylvania, 2001. Association for Computational Linguistics. doi: 10.3115/
1073083.1073135. URL http://portal.acm.org/citation.cfm?doid=
1073083.1073135.
[210] Chin-YewLin. ROUGE:APackageforAutomaticEvaluationofSummaries. InText
Summarization Branches Out, pages 74–81, Barcelona, Spain, July 2004. Association
forComputationalLinguistics. URLhttps://aclanthology.org/W04-1013.
[211] Lei Li, Yongfeng Zhang, and Li Chen. Generate Neural Template Explanations for
Recommendation. In Proceedings of the 29th ACM International Conference on In-
formation & Knowledge Management, CIKM ’20, pages 755–764, New York, NY,
USA, 2020. Association for Computing Machinery. ISBN 978-1-4503-6859-9. doi:
111

10.1145/3340531.3411992. URL https://doi.org/10.1145/3340531.3411992.
26citations(SemanticScholar/DOI)[2022-02-14].
[212] GeorginaPeakeandJunWang. ExplanationMining: PostHocInterpretabilityofLa-
tent Factor Models for Recommendation Systems. In Proceedings of the 24th ACM
SIGKDD International Conference on Knowledge Discovery & Data Mining, KDD
’18, pages 2060–2069, New York, NY, USA, 2018. Association for Computing Ma-
chinery. ISBN 978-1-4503-5552-0. doi: 10.1145/3219819.3220072. URL https:
//doi.org/10.1145/3219819.3220072.
[213] Ludovik Coba, Panagiotis Symeonidis, and Markus Zanker. Personalised novel and
explainablematrixfactorisation. Data&KnowledgeEngineering, 122:142–158, July
2019. ISSN 0169-023X. doi: 10.1016/j.datak.2019.06.003. URL https://www.
sciencedirect.com/science/article/pii/S0169023X1830332X.
[214] Shijie Geng, Zuohui Fu, Juntao Tan, Yingqiang Ge, Gerard de Melo, and Yongfeng
Zhang. PathLanguageModelingoverKnowledgeGraphsforExplainableRecommen-
dation. InProceedingsoftheACMWebConference2022,WWW’22,pages946–955,
NewYork,NY,USA,April2022.AssociationforComputingMachinery. ISBN978-
1-4503-9096-5. doi: 10.1145/3485447.3511937. URLhttps://dl.acm.org/doi/
10.1145/3485447.3511937.
[215] GiacomoBalloccu,LudovicoBoratto,GianniFenu,andMirkoMarras.PostProcessing
RecommenderSystemswithKnowledgeGraphsforRecency,Popularity,andDiversity
of Explanations. In Proceedings of the 45th International ACM SIGIR Conference on
ResearchandDevelopmentinInformationRetrieval,SIGIR’22,pages646–656,New
York,NY,USA,2022.AssociationforComputingMachinery.ISBN978-1-4503-8732-
3. doi: 10.1145/3477495.3532041. URL https://dl.acm.org/doi/10.1145/
3477495.3532041.
[216] Giacomo Balloccu, Ludovico Boratto, Gianni Fenu, and Mirko Marras. Reinforce-
mentrecommendationreasoningthroughknowledgegraphsforexplanationpathqual-
ity. Knowledge-BasedSystems, 260:110098, January2023. ISSN0950-7051. doi: 10.
1016/j.knosys.2022.110098. URLhttps://www.sciencedirect.com/science/
article/pii/S0950705122011947.
112

[217] Yehuda Koren, Robert Bell, and Chris Volinsky. Matrix factorization techniques for
recommendersystems. Computer,42(8):30–37,2009. doi: 10.1109/MC.2009.263.
[218] YuZheng,ChenGao,XiangnanHe,DepengJin,andYongLi.IncorporatingPriceinto
RecommendationWithGraphConvolutionalNetworks.IEEETransactionsonKnowl-
edgeandDataEngineering,35(2):1609–1623,February2023. ISSN1558-2191. doi:
10.1109/TKDE.2021.3091160. ConferenceName: IEEETransactionsonKnowledge
andDataEngineering.
[219] NadaGhanem,StephanLeitner,andDietmarJannach. Balancingconsumerandbusi-
ness value of recommender systems: A simulation-based analysis. Electronic Com-
merceResearchandApplications,55:101195,September2022. ISSN1567-4223. doi:
10.1016/j.elerap.2022.101195. URLhttps://www.sciencedirect.com/science/
article/pii/S1567422322000783.
[220] Robert Garfinkel, Ram Gopal, Bhavik Pathak, Rajkumar Venkatesan, and Fang Yin.
Empirical Analysis of the Business Value of Recommender Systems. doi: 10.2139/
SSRN.958770.
[221] Sofia Gkika and George Lekakos. The Persuasive Role of Explanations in Recom-
menderSystems. InAnssiÖörni,SaskiaKelders,LisettevanGemert-Pijnen,andHarri
Oinas-Kukkonen, editors, ProceedingsoftheSecondInternationalWorkshoponBehav-
iorChangeSupportSystems,volume1153ofCEURWorkshopProceedings,pages59–68,
Padua,Italy,May2014.CEUR.URLhttps://ceur-ws.org/Vol-1153/#Paper_6.
ISSN:1613-0073.
[222] PaoloCremonesi,FrancaGarzotto,andRobertoTurrin. InvestigatingthePersuasion
Potential of Recommender Systems from a Quality Perspective: An Empirical Study.
ACM Transactions on Interactive Intelligent Systems, 2(2):11:1–11:41, 2012. ISSN
2160-6455. doi: 10.1145/2209310.2209314. URL https://doi.org/10.1145/
2209310.2209314.
[223] AlviseDeBiasio,MerylinMonaro,LucaOneto,LambertoBallan,andNicolòNavarin.
On the problem of recommendation for sensitive users and influential items: Simul-
taneously maintaining interest and diversity. Knowledge-Based Systems, 275:110699,
September2023. ISSN0950-7051. doi: 10.1016/j.knosys.2023.110699. URLhttps:
//www.sciencedirect.com/science/article/pii/S0950705123004495.
113

[224] Hongwei Wang, Fuzheng Zhang, Jialin Wang, Miao Zhao, Wenjie Li, Xing Xie, and
Minyi Guo. RippleNet: Propagating User Preferences on the Knowledge Graph for
RecommenderSystems. InProceedingsofthe27thACMInternationalConferenceon
InformationandKnowledgeManagement,CIKM’18,pages417–426,NewYork,NY,
USA, 2018. Association for Computing Machinery. ISBN 978-1-4503-6014-2. doi:
10.1145/3269206.3271739. URL https://dl.acm.org/doi/10.1145/3269206.
3271739.
[225] QianyuLi,XiaoliTang,TengyunWang,HaizhiYang,andHengjieSong.UnifyingTask-
OrientedKnowledgeGraphLearningandRecommendation. IEEEAccess,7:115816–
115828,2019. ISSN2169-3536. doi: 10.1109/ACCESS.2019.2932466. Conference
Name: IEEEAccess.
[226] XiaoSha,ZhuSun,andJieZhang. Hierarchicalattentiveknowledgegraphembedding
forpersonalizedrecommendation. ElectronicCommerceResearchandApplications,48:
101071,July2021. ISSN1567-4223. doi: 10.1016/j.elerap.2021.101071. URLhttps:
//www.sciencedirect.com/science/article/pii/S1567422321000430.
[227] Chuan Shi, Binbin Hu, Wayne Xin Zhao, and Philip S. Yu. Heterogeneous Infor-
mation Network Embedding for Recommendation. IEEE Transactions on Knowl-
edge and Data Engineering, 31(2):357–370, February 2019. ISSN 1558-2191. doi:
10.1109/TKDE.2018.2833443. ConferenceName: IEEETransactionsonKnowledge
andDataEngineering.
[228] ZhuSun,JieYang,JieZhang,AlessandroBozzon,Long-KaiHuang,andChiXu. Re-
currentknowledgegraphembeddingforeffectiverecommendation. InProceedingsof
the12thACMConferenceonRecommenderSystems,RecSys’18,pages297–305,New
York,NY,USA,2018.AssociationforComputingMachinery.ISBN978-1-4503-5901-
6. doi: 10.1145/3240323.3240361. URL https://dl.acm.org/doi/10.1145/
3240323.3240361.
[229] Xiaoli Tang, Tengyun Wang, Haizhi Yang, and Hengjie Song. AKUPM: Attention-
EnhancedKnowledge-AwareUserPreferenceModelforRecommendation. InProceed-
ings of the 25th ACM SIGKDD International Conference on Knowledge Discovery &
Data Mining, KDD ’19, pages 1891–1899, New York, NY, USA, 2019. Association
forComputingMachinery.ISBN978-1-4503-6201-6.doi:10.1145/3292500.3330705.
URLhttps://dl.acm.org/doi/10.1145/3292500.3330705.
114

[230] Qingyao Ai, Vahid Azizi, Xu Chen, and Yongfeng Zhang. Learning Heterogeneous
Knowledge Base Embeddings for Explainable Recommendation. Algorithms, 11(9):
137,September2018. ISSN1999-4893. doi: 10.3390/a11090137. URLhttp://www.
mdpi.com/1999-4893/11/9/137.
[231] Yixin Cao, Xiang Wang, Xiangnan He, Zikun Hu, and Tat-Seng Chua. Unifying
KnowledgeGraphLearningandRecommendation: TowardsaBetterUnderstanding
ofUserPreferences. InTheWorldWideWebConference,WWW’19,pages151–161,
NewYork,NY,USA,2019.AssociationforComputingMachinery. ISBN978-1-4503-
6674-8.doi:10.1145/3308558.3313705.URLhttps://dl.acm.org/doi/10.1145/
3308558.3313705.
[232] JinHuang,WayneXinZhao,HongjianDou,Ji-RongWen,andEdwardY.Chang. Im-
provingSequentialRecommendationwithKnowledge-EnhancedMemoryNetworks.
InThe41stInternationalACMSIGIRConferenceonResearch&DevelopmentinInfor-
mationRetrieval,SIGIR’18,pages505–514,NewYork,NY,USA,2018.Association
forComputingMachinery. ISBN978-1-4503-5657-2. doi: 10.1145/3209978.3210017.
URLhttps://dl.acm.org/doi/10.1145/3209978.3210017.
[233] Zuoxi Yang and Shoubin Dong. HAGERec: Hierarchical Attention Graph Con-
volutional Network Incorporating Knowledge Graph for Explainable Recommenda-
tion. Knowledge-Based Systems, 204:106194, September 2020. ISSN 0950-7051.
doi: 10.1016/j.knosys.2020.106194. URL https://www.sciencedirect.com/
science/article/pii/S0950705120304196.
[234] WeizhiMa,MinZhang,YueCao,WoojeongJin,ChenyangWang,YiqunLiu,Shaop-
ingMa,andXiangRen.JointlyLearningExplainableRulesforRecommendationwith
KnowledgeGraph. InTheWorldWideWebConference,pages1210–1221,SanFran-
ciscoCAUSA,May2019.ACM. ISBN978-1-4503-6674-8. doi: 10.1145/3308558.
3313607. URLhttps://dl.acm.org/doi/10.1145/3308558.3313607.
[235] XitingWang,KunpengLiu,DongjieWang,LeWu,YanjieFu,andXingXie.Multi-level
Recommendation Reasoning over Knowledge Graphs with Reinforcement Learning.
InProceedingsoftheACMWebConference2022,WWW’22,pages2098–2108,New
York,NY,USA,April2022.AssociationforComputingMachinery.ISBN978-1-4503-
9096-5.doi:10.1145/3485447.3512083.URLhttps://dl.acm.org/doi/10.1145/
3485447.3512083.
115

[236] Xiang Wang, Dingxian Wang, Canran Xu, Xiangnan He, Yixin Cao, and Tat-Seng
Chua. Explainable Reasoning over Knowledge Graphs for Recommendation. Pro-
ceedingsoftheAAAIConferenceonArtificialIntelligence,33(01):5329–5336,July2019.
ISSN 2374-3468. doi: 10.1609/aaai.v33i01.33015329. URL https://ojs.aaai.
org/index.php/AAAI/article/view/4470. Number: 01.
[237] Xiaowen Huang, Quan Fang, Shengsheng Qian, Jitao Sang, Yan Li, and Changsheng
Xu. ExplainableInteraction-drivenUserModelingoverKnowledgeGraphforSequen-
tial Recommendation. In Proceedings of the 27th ACM International Conference on
Multimedia, MM ’19, pages 548–556, New York, NY, USA, 2019. Association for
Computing Machinery. ISBN 978-1-4503-6889-6. doi: 10.1145/3343031.3350893.
URLhttps://doi.org/10.1145/3343031.3350893.
[238] YikunXian,ZuohuiFu,S.Muthukrishnan,GerarddeMelo,andYongfengZhang. Re-
inforcementKnowledgeGraphReasoningforExplainableRecommendation. InPro-
ceedings of the 42nd International ACM SIGIR Conference on Research and Develop-
mentinInformationRetrieval,SIGIR’19,pages285–294,NewYork,NY,USA,2019.
Association for Computing Machinery. ISBN 978-1-4503-6172-9. doi: 10.1145/
3331184.3331203. URLhttps://doi.org/10.1145/3331184.3331203.
[239] Yikun Xian, Zuohui Fu, Handong Zhao, Yingqiang Ge, Xu Chen, Qiaoying Huang,
Shijie Geng, Zhou Qin, Gerard de Melo, S. Muthukrishnan, and Yongfeng Zhang.
CAFE:Coarse-to-FineNeuralSymbolicReasoningforExplainableRecommendation.
Proceedings of the 29th ACM International Conference on Information & Knowledge
Management,pages1645–1654,October2020.doi: 10.1145/3340531.3412038.URL
http://arxiv.org/abs/2010.15620. 28citations(SemanticScholar/arXiv)[2022-
02-14]28citations(SemanticScholar/DOI)[2022-02-14]arXiv: 2010.15620.
[240] XiangWang,XiangnanHe,YixinCao,MengLiu,andTat-SengChua. KGAT:Knowl-
edgeGraphAttentionNetworkforRecommendation. InProceedingsofthe25thACM
SIGKDD International Conference on Knowledge Discovery & Data Mining, KDD
’19, pages950–958, NewYork, NY,USA,2019.AssociationforComputingMachin-
ery. ISBN 978-1-4503-6201-6. doi: 10.1145/3292500.3330989. URL https:
//dl.acm.org/doi/10.1145/3292500.3330989.
[241] HongxuChen,YicongLi,XiangguoSun,GuandongXu,andHongzhiYin. Temporal
Meta-pathGuidedExplainableRecommendation. InProceedingsofthe14thACMIn-
116

ternationalConferenceonWebSearchandDataMining,WSDM’21,pages1056–1064,
NewYork,NY,USA,March2021.AssociationforComputingMachinery. ISBN978-
1-4503-8297-7. doi: 10.1145/3437963.3441762. URLhttps://dl.acm.org/doi/
10.1145/3437963.3441762.
[242] WeipingSong,ZhijianDuan,ZiqingYang,HaoZhu,MingZhang,andJianTang.Ekar:
An Explainable Method for Knowledge Aware Recommendation. arXiv:1906.09506
[cs],January2022. URLhttp://arxiv.org/abs/1906.09506. arXiv: 1906.09506.
[243] Xin Xin, Xiangnan He, Yongfeng Zhang, Yongdong Zhang, and Joemon Jose. Rela-
tional Collaborative Filtering: Modeling Multiple Item Relations for Recommenda-
tion. In Proceedings of the 42nd International ACM SIGIR Conference on Research
and Development in Information Retrieval, pages 125–134, Paris France, July 2019.
ACM. ISBN 978-1-4503-6172-9. doi: 10.1145/3331184.3331188. URL https:
//dl.acm.org/doi/10.1145/3331184.3331188.
[244] BinbinHu,ChuanShi,WayneXinZhao,andPhilipS.Yu.LeveragingMeta-pathbased
Context for Top- N Recommendation with A Neural Co-Attention Model. In Pro-
ceedingsofthe24thACMSIGKDDInternationalConferenceonKnowledgeDiscovery
&DataMining,KDD’18,pages1531–1540,NewYork,NY,USA,2018.Association
forComputingMachinery. ISBN978-1-4503-5552-0. doi: 10.1145/3219819.3219965.
URLhttps://dl.acm.org/doi/10.1145/3219819.3219965.
[245] Qinqin Wang, Elias Tragos, Neil Hurley, Barry Smyth, Aonghus Lawlor, and Ruihai
Dong. Entity-EnhancedGraphConvolutionalNetworkforAccurateandExplainable
Recommendation.InProceedingsofthe30thACMConferenceonUserModeling,Adap-
tationandPersonalization,UMAP’22,pages79–88,NewYork,NY,USA,2022.Asso-
ciationforComputingMachinery. ISBN978-1-4503-9207-5. doi: 10.1145/3503252.
3531316. URLhttps://dl.acm.org/doi/10.1145/3503252.3531316.
[246] Ting Ma, Longtao Huang, Qianqian Lu, and Songlin Hu. KR-GCN: Knowledge-
Aware Reasoning with Graph Convolution Network for Explainable Recommenda-
tion. ACM Transactions on Information Systems, 41(1):4:1–4:27, 2023. ISSN 1046-
8188. doi: 10.1145/3511019. URLhttps://dl.acm.org/doi/10.1145/3511019.
[247] ZiyuLyu,YueWu,JunjieLai,MinYang,ChengmingLi,andWeiZhou.KnowledgeEn-
hancedGraphNeuralNetworksforExplainableRecommendation. IEEETransactions
117

onKnowledgeandDataEngineering,35(5):4954–4968,May2023. ISSN1558-2191.
doi: 10.1109/TKDE.2022.3142260. ConferenceName: IEEETransactionsonKnowl-
edgeandDataEngineering.
[248] Chang-You Tai, Liang-Ying Huang, Chien-Kun Huang, and Lun-Wei Ku. User-
CentricPathReasoningtowardsExplainableRecommendation. InProceedingsofthe
44thInternationalACMSIGIRConferenceonResearchandDevelopmentinInforma-
tionRetrieval,SIGIR’21,pages879–889,NewYork,NY,USA,2021.Associationfor
Computing Machinery. ISBN 978-1-4503-8037-9. doi: 10.1145/3404835.3462847.
URLhttps://dl.acm.org/doi/10.1145/3404835.3462847.
[249] Yuyue Zhao, Xiang Wang, Jiawei Chen, Yashen Wang, Wei Tang, Xiangnan He, and
HaiyongXie.Time-awarePathReasoningonKnowledgeGraphforRecommendation.
ACMTransactionsonInformationSystems,41(2):26:1–26:26,2022. ISSN1046-8188.
doi: 10.1145/3531267. URLhttps://dl.acm.org/doi/10.1145/3531267.
[250] ErasmoPurificato,LudovicoBoratto,andErnestoWilliamDeLuca.DoGraphNeural
Networks Build Fair User Models? Assessing Disparate Impact and Mistreatment in
Behavioural User Profiling. In Proceedings of the 31st ACM International Conference
onInformation&KnowledgeManagement,CIKM’22,pages4399–4403,NewYork,
NY,USA,2022.AssociationforComputingMachinery.ISBN978-1-4503-9236-5.doi:
10.1145/3511808.3557584. URLhttps://doi.org/10.1145/3511808.3557584.
[251] ChristianScheel,AngelCastellanos,ThebinLee,andErnestoWilliamDeLuca. The
ReasonWhy: ASurveyofExplanationsforRecommenderSystems. InAndreasNürn-
berger,SebastianStober,BirgerLarsen,andMarcinDetyniecki,editors,AdaptiveMul-
timedia Retrieval: Semantics, Context, and Adaptation, Lecture Notes in Computer
Science, pages 67–84, Cham, 2014. Springer International Publishing. ISBN 978-3-
319-12093-5. doi: 10.1007/978-3-319-12093-5_3.
[252] YunfeiChu,JiangchaoYao,ChangZhou,andHongxiaYang. GraphNeuralNetworks
in Modern Recommender Systems. In Lingfei Wu, Peng Cui, Jian Pei, and Liang
Zhao,editors,GraphNeuralNetworks: Foundations,Frontiers,andApplications,pages
423–445. Springer Nature, Singapore, 2022. ISBN 9789811660542. doi: 10.1007/
978-981-16-6054-2_19. URL https://doi.org/10.1007/978-981-16-6054-2_
19.
118

[253] ShiwenWu,FeiSun,WentaoZhang,XuXie,andBinCui. GraphNeuralNetworksin
RecommenderSystems: ASurvey. ACMComputingSurveys,55(5):97:1–97:37,2022.
ISSN0360-0300.doi: 10.1145/3535101.URLhttps://dl.acm.org/doi/10.1145/
3535101.
[254] ChenGao,YuZheng,NianLi,YinfengLi,YingrongQin,JinghuaPiao,YuhanQuan,
JianxinChang,DepengJin,XiangnanHe,andYongLi.ASurveyofGraphNeuralNet-
worksforRecommenderSystems: Challenges,Methods,andDirections. ACMTrans-
actionsonRecommenderSystems,1(1):3:1–3:51,March2023. doi: 10.1145/3568022.
URLhttps://dl.acm.org/doi/10.1145/3568022.
[255] HaoYuan,HaiyangYu,ShuruiGui,andShuiwangJi. ExplainabilityinGraphNeural
Networks: ATaxonomicSurvey. IEEETransactionsonPatternAnalysisandMachine
Intelligence, 45(5):5782–5799, May 2023. ISSN 1939-3539. doi: 10.1109/TPAMI.
2022.3204236. Conference Name: IEEE Transactions on Pattern Analysis and Ma-
chineIntelligence.
[256] QingyuGuo,FuzhenZhuang,ChuanQin,HengshuZhu,XingXie,HuiXiong,and
QingHe. ASurveyonKnowledgeGraph-BasedRecommenderSystems. IEEETrans-
actions on Knowledge and Data Engineering, 34(8):3549–3568, August 2022. ISSN
1558-2191. doi: 10.1109/TKDE.2020.3028705. Conference Name: IEEE Transac-
tionsonKnowledgeandDataEngineering.
[257] Giacomo Balloccu, Ludovico Boratto, Christian Cancedda, Gianni Fenu, and Mirko
Marras. KnowledgeisPower,UnderstandingisImpact: Utilityand BeyondGoals,Ex-
planationQuality,and Fairnessin PathReasoningRecommendation. InJaapKamps,
Lorraine Goeuriot, Fabio Crestani, Maria Maistro, Hideo Joho, Brian Davis, Cathal
Gurrin,UdoKruschwitz,andAnnalinaCaputo,editors,AdvancesinInformationRe-
trieval,LectureNotesinComputerScience,pages3–19,Cham,2023.SpringerNature
Switzerland. ISBN978-3-031-28241-6. doi: 10.1007/978-3-031-28241-6_1.
[258] SandeepK.RaghuwanshiandR.K.Pateriya. RecommendationSystems: Techniques,
Challenges,Application,andEvaluation.InJagdishChandBansal,KedarNathDas,At-
ulyaNagar,KusumDeep,andAkshayKumarOjha,editors,SoftComputingforProb-
lem Solving, Advances in Intelligent Systems and Computing, pages 151–164, Singa-
pore,2019.Springer. ISBN9789811315954. doi: 10.1007/978-981-13-1595-4_12.
119

[259] Shuo Chang, F. Maxwell Harper, and Loren Gilbert Terveen. Crowd-based person-
alizednaturallanguageexplanationsforrecommendations. InProceedingsofthe10th
ACMConferenceonRecommenderSystems,RecSys’16,pages175–182,NewYork,NY,
USA, 2016. Association for Computing Machinery. ISBN 978-1-4503-4035-9. doi:
10.1145/2959100.2959153. URL https://doi.org/10.1145/2959100.2959153.
77 citations (Semantic Scholar/DOI) [2022-10-07] 44 citations (Crossref) [2022-10-
07].
[260] FelipeCosta,SixunOuyang,PeterDolog,andAonghusLawlor.AutomaticGeneration
ofNaturalLanguageExplanations. InProceedingsofthe23rdInternationalConference
on Intelligent User Interfaces Companion, IUI ’18 Companion, pages 1–2, New York,
NY, USA, March 2018. Association for Computing Machinery. ISBN 978-1-4503-
5571-1.doi: 10.1145/3180308.3180366.URLhttps://doi.org/10.1145/3180308.
3180366.
[261] Marta Caro-Martínez, Guillermo Jiménez-Díaz, and Juan A. Recio-García. Concep-
tual Modeling of Explainable Recommender Systems: An Ontological Formalization
to Guide Their Design and Development. Journal of Artificial Intelligence Research,
71:557–589, July 2021. ISSN 1076-9757. doi: 10.1613/jair.1.12789. URL https:
//jair.org/index.php/jair/article/view/12789.
[262] Zuohui Fu, Yikun Xian, Ruoyuan Gao, Jieyu Zhao, Qiaoying Huang, Yingqiang Ge,
ShuyuanXu,ShijieGeng,ChiragShah,YongfengZhang,andGerarddeMelo.Fairness-
Aware Explainable Recommendation over Knowledge Graphs. In Proceedings of the
43rdInternationalACMSIGIRConferenceonResearchandDevelopmentinInforma-
tion Retrieval, SIGIR ’20, pages 69–78, New York, NY, USA, 2020. Association for
Computing Machinery. ISBN 978-1-4503-8016-4. doi: 10.1145/3397271.3401051.
URLhttps://doi.org/10.1145/3397271.3401051.
120