Modelling Concept Drift in Dynamic Data Streams for
Recommender Systems
LUCIANO CAROPRESE,UniversityGabrieled’AnnunzioofChietiandPescara,DepartmentofEngi-
neeringandGeosciences,Pescara,ItalyandICAR-CNR,Rende,Italy
FRANCESCOSERGIOPISANI,ICAR-CNR,Rende,Italy
BRUNOMIGUELVELOSO,UniversidadePortucalense,Porto,PortugalandINESCTEC,Porto,Portu-
gal
MATTHIASKONIG,LeidenUniversity,Leiden,Netherlands
GIUSEPPEMANCO,ICAR-CNR,Rende,Italy
HOLGER HOOS,LeidenUniversity,Leiden,NetherlandsandTheUniversityofBritishColumbia,Van-
couver,Canada
JOAOGAMA,UniversidadePortucalense,Porto,PortugalandINESCTEC,Porto,Portugal
Recommendationsystemsplayacrucialroleinmoderne-commerceandstreamingservices.However,the
limitedavailabilityofpublicdatasetshamperstherapiddevelopmentofmoreefficientandaccuraterecom-
mendationalgorithmswithintheresearchcommunity.Thisworkintroducesastream-baseddatagenerator
designedtogenerateuserpreferencesforasetofitemswhileaccommodatingprogressivechangesinuser
preferences.Theunderlyingprincipleinvolvesusinguser/itemembeddingstoderivepreferencesbyexplor-
ingtheproximityoftheseembeddings.Whetherrandomlygeneratedorlearnedfromarealfinitedatastream,
theseembeddingsserveasthebasisforgeneratingnewpreferences.Weinvestigatehowthisfundamental
modelcanadapttoshiftsinuserbehaviorovertime;inourframework,changescorrespondtoalterations
inthestructureofthetripartitegraph,reflectingmodificationsintheunderlyingembeddings.Throughan
analysisofreal-lifedatastreams,wedemonstratethattheproposedmodeliseffectiveincapturingactual
preferencesandthechangesthattheycanexhibitovertime.Thus,wecharacterizethesechangesandde-
velopageneralizedmethodcapableofsimulatingrealisticdata,therebygeneratingstreamswithsimilaryet
controllabledriftdynamics.
CCSConcepts:•Informationsystems→Retrievalmodelsandranking;
ThisworkwaspartiallysupportedbyProject“SERICS-SEcurityandRIghtsIntheCyberSpace”(PE00000014)andpartially
bytheEUH2020ICT48project“HumanE-AI-Net”undercontract#952026.
Authors’ContactInformation:LucianoCaroprese,UniversityGabrieled’AnnunzioofChietiandPescara,Department
ofEngineeringandGeosciences,Pescara,ItalyandICAR-CNR,Rende,Calabria,Italy;e-mail:luciano.caroprese@unich.it;
FrancescoSergioPisani,ICAR-CNR,Rende,Calabria,Italy;e-mail:francescosergio.pisani@icar.cnr.it;BrunoMiguelVeloso,
UniversidadePortucalense,Porto,PortugalandINESCTEC,Porto,Portugal;e-mail:bveloso@fep.up.pt;MatthiasKonig,
LeidenUniversity,Leiden,Netherlands;e-mail:h.m.t.konig@liacs.leidenuniv.nl;GiuseppeManco,ICAR-CNR,Rende,Cal-
abria,Italy;e-mail:giuseppe.manco@icar.cnr.it;HolgerHoos,LeidenUniversity,Leiden,NetherlandsandTheUniversity
ofBritishColumbia,Vancouver,BritishColumbia,Canada;e-mail:h.h.hoos@liacs.leidenuniv.nl;JoaoGama,Universidade
Portucalense,Porto,PortugalandINESCTEC,Porto,Portugal;e-mail:jgama@fep.up.pt.
This work is licensed under a Creative Commons Attribution International 4.0 License.
©2025Copyrightheldbytheowner/author(s).
ACM2770-6699/2025/03-ART24
https://doi.org/10.1145/3707693
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

24:2 L.Caropreseetal.
AdditionalKeyWordsandPhrases:Recommendersystems,collaborativefiltering,conceptdriftadaptation,
datageneration
ACMReferenceFormat:
LucianoCaroprese,FrancescoSergioPisani,BrunoMiguelVeloso,MatthiasKonig,GiuseppeManco,Holger
Hoos,andJoaoGama.2025.ModellingConceptDriftinDynamicDataStreamsforRecommenderSystems.
ACMTrans.Recomm.Syst.3,2,Article24(March2025),28pages.https://doi.org/10.1145/3707693
1 Introduction
Modernmachinelearningapplicationsandsystemsneedtodealwithlargeamountsofcontinuous
dataintheformofdatastreams.Mostreal-lifeapplicationscenariosrequiretheanalysisoflarge
volumes of data whose properties or distribution can change and evolve. Notable examples
are e-commerce and streaming platforms, which contain catalogs counting thousands or even
millions of products or items, where user preferences and purchasing/adoption behavior can
evolveovertimeaccordingtochangesinthecatalog.DataStreamMining[13,17,26]represents
thesetoftechniquesandmethodsthatenabledataanalysisfulfillingthefollowingcharacteristics:
(a)Highamountsofdatacominginaninfinitestream[26];(b)ConceptDrifting[15,42,47],i.e.,
datachangeorevolveovertime;(c)Highvolatility,thatpreventsthepossibilityofstoringthedata
andcallsforonlinemethodswheredataisanalyzedassoonasitreceivedanditisdiscardedor
summarised.
Besides traditional supervised [16] or unsupervised [25] learning problems on data streams,
recommendation can be considered an extremely significant landscape for data stream mining.
The massive amount of information available to users in the form of digital catalogs and online
services requires the capability to appropriately select relevant content and filter out irrelevant
data. Understanding and predicting users’ choices and preferences is thus a challenging task
and Recommender Systems (RS) play a crucial role in modeling complex situations, where
priorbeliefs,specifictendencies,andreciprocalinfluencesjointlycontributetodeterminingsuch
preferences[1,5,35].
Notably, although the field has been extensively studied and several techniques and methods
wereproposedintheliterature,thereisasignificantgapbetweenresearchalgorithmsandmodels,
and real-life industrial deployment of RS. In fact, the former are often based on the unrealistic
assumption that preferences are static and do not tend to change over time. As a consequence,
the studies essentially focus on static datasets collected over relatively long periods, and build
preference models that tend to be periodically updated. This perspective has obviously several
limitations,asitignoresthestreamingnatureofpreferencedataandconsequentlythecontinuous
evolutionoftheinteractions,dueeithertocatalogupdates,userchurnornewacquisitions,and
evolving tastes or preferences. This problem has been recently at the center of the attention of
current research [2] and some initial attempts were made to devise more sophisticated models
capableofcapturingthedynamicnatureofpreferences[11,29,30,43,45].
Inthisarticle,weaddresstheproblemoftheshortageofsufficientlylargepublicdatasetswith
realproperties,neededtotrainandevaluatemodernrecommendationsystems.Whenevaluating
recommendationsystemsinastreamingscenario[44],asignificantchallengearises:Howcanwe
effectivelyassesstherobustnessofadvancedmachinelearningsystemsandquantifytheirperfor-
manceinacontrolledexperimentalbenchmarkingenvironment,whereallthecharacteristicsof
thedatacanbeappropriatelytunedandthealgorithmicresponsecanbeevaluatedaccordingly?
Thisproblemischallengingforanumberofrelevantreasons.Themostimportantisthatobtaining
large-scale public repositories that represent interaction datasets is difficult, due to inherent
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

ModellingConceptDriftinDynamicDataStreamsforRecommenderSystems 24:3
privacy and technological concerns associated with their sharing. In fact, the available datasets
suchasAmazon[32],Netflix[7],orMovieLens[19]areordersofmagnitudesmallerthanpropri-
etary data and typically contain data collected in a limited period where preferences have been
collected.Syntheticdatageneratorscanhelpusalleviatethisproblembyprovidingad-hocdatasets
wherethedatacharacteristics(numberofusers/items,numberofinteractions,datadistributions)
can be manipulated and the algorithmic robustness compared according to such manipulations.
However,existingdatagenerationmethodsdonottakeintoaccountthedynamicnatureofthedata
distribution,whichislikelytooccurinastreamingscenarioandinthepresenceofevolvingprefer-
encesalongthetimedimension.Thissituationisfurtherexacerbatedbythelackofgeneralmodels
fordistributiondynamics,whichshouldinsteadbeaccuratelystudiedandcorrelatedtoalgorithmic
responses.
Inpractice,syntheticdatagenerationthataccountsfordriftsinacontinuousstreamingscenario
needstoaddressthefollowingchallenges:
(1) First, we need to hypothesize a preference model that can realistically characterize item
adoptionanduserpreferences.Thismodelshouldserveasthebasisforthedatageneration
processwithoutintroducinganybiasthatisnotactuallyobservableinrealdata.
(2) Second,weneedtoconsiderallpossiblechangesthatcancauseadriftwithinthepreferences.
Drifts can be abrupt or progressive, they can involve a percentage of users/items or the
whole population, and they can be caused by new emerging trends or by changes in the
characteristicsofusers/items.Alltheseaspectsneedtobemodeled,andthedatageneration
processneedstoembedthem.
Inordertodealwiththeaboveissues,weproposeageneralpreferencemodelthatcaneasily
adapttocoverpreferencedynamics.Wefocusmainlyonimplicitpreferences:Givenauser/item
pair,apreferenceisabinaryresponseexpressingthefactthattheuseradopted/didnotadoptthe
item.Thissimplerepresentationschemenaturallyinducesaper-userorderingamongitems,which
can,hence,berankedaccordingtotheadoptionlikelihood.Ourbasicassumptionisthatbothusers
anditemsmaptoanunderlyinglatentlow-dimensionalmanifold,andpreferencesessentiallyoc-
cur due to closeness within this latent space. Notably, this interaction can be made explicit by
uncoveringthelatentspaceandmodelingtheinteractionsasatripartitegraphconnectingusers,
latentspacedimensions,anditems.Asaconsequence,preferencedynamicscanbeeasilymadeex-
plicitbysuitablemodificationsofthelatentembeddings,whichinturnrepresentmodificationsof
theunderlyinggraph,asaddition/deletionofnodesorchangesintheconnectivity,thusproducing
realisticevolvingpreferencedatastreamswithcharacteristicsthatchangeovertime(conceptdrift).
Amajorchallengeisquantifyinghowrealisticapreferencemodeliswhendriftsarerepresented
aschangesintheunderlyingembeddings.Weapproachthisbyinvestigatingthebehaviorofthe
underlyingmodelonrealisticdatastreamsandstudyinghowitcaneffectivelyreplicatereal-data
distributions.Inpractice,inourevaluation,weadoptaschemewhere(i)driftscanbeidentifiedin
realdatabyobservingthemodel’sinabilitytocapturerealisticpreferences,and(ii)themodelauto-
maticallyadjustsbymakingminimalchangestothegraphstructuretoalignactualandgenerated
preferences.Inourscenario,theoptimaladjustmentsarethosethatcanaccuratelypredictactual
preferenceswithminimalerror,eveninthepresenceofconceptdrift.Notably,theanalysisofreal
dataalsoallowsustodeviseandcharacterizethechangesthattypicallycanoccur,thusdevising
afullygenerativemodelforsyntheticyetrealisticpreferencedatathatcanalsobecharacterized
bypreferencedynamics.
Tosummarize,themaincontributionsofthearticleare
—A preference model based on latent embeddings. According to such a model, concept
drifts can be modeled as major modifications of the embeddings, that can be deemed as
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

24:4 L.Caropreseetal.
rewiringchangesintheunderlyingtripartitegraph.Weshowthatthismodeliscapableof
characterizing real-data distributions and can hence be used as a basis for synthetic data
generation.
—A stream-based data generator that can produce preference data also characterized by
preference dynamics. We study a categorization of the possible drifts that can occur
withinpreferences.Tothebestofourknowledge,thisisthefirstattempttosystematically
approachtheproblemandproposeasolution.
The remaining sections of this article are organized as follows. Section 2 presents a systematic
literaturereviewonsyntheticdatageneratorsforRS.InSection3,weformulatetheproblemof
generating synthetic data and propose an algorithm for detecting drifts in preference data. Sec-
tion4providesdetailsonexperimentsconductedusingrealdataanddiscussestheapplicationof
learnedmodelsforemulatingadatagenerationprocess.Section5introducesageneraldatagener-
ationschemebasedontheinsightsobtainedfromtheexperiments.Finally,inSection6,wedraw
generalconclusionsandoutlinefutureresearchdirections.
2 RelatedWork
Generating synthetic data streams is not entirely novel and has been proposed in the past for
general machine learning tasks, such as classification and regression [8, 38]. However, previous
researchonsyntheticdatastreamsforrecommendationsystemsislimitedandhighlyfragmented,
tacklingdifferentdataissuessuchasuserprivacy[37],scalability,shortageofbenchmarks[6,9,
31,41],and,mostcloselyrelatedtothiswork,conceptchanges[21].
IntheworkbySlokometal.[37],theauthorspresentamethodtohidecertainpreference-related
user information from a set of user-item interactions, which otherwisecould be accessed. Their
approachemploystheCARTalgorithm[10],andtheoutputisasetofsynthesizedpreferencedata,
which preserves crucial statistical properties of the original data in order to be helpful for the
testingofrecommendationalgorithmsbuthidesspecificuserinformation,suchastheirfavorite
actor in the case of movie recommendation. However, their method is unable to generate new
ratingsforunseenitems,anditisuncleartowhatextenttheirapproachcangenerateincremental
dataorproducedatastreamswithdynamicallychangingcharacteristics.
ThesamelimitationholdsfortheworkbyBellettietal.[6].Theauthorsemployadatagenerator
toproducearealisticcopyoftheMovieLensdatasetbutwithaheavilyextendednumberofusers,
items, and ratings. While this approach successfully scales up the MovieLens dataset by several
orders of magnitude, therefore overcoming scalability, it does not address the issue of dynamic
changes in user preferences. In other words, there are no parameters in the generation process
that control drift in the data. In their study, Tso and Schmidt-Thieme [41] propose a synthetic
data generation methodology to examine the performance of attribute-aware algorithms. They
manipulatethelevelofinformativenessofattributesintheirartificialdatasetstostudytheirim-
pactonalgorithmbehavior.Inthedomainofcontext-awarerecommendationsystems,delCarmen
Rodríguez-Hernándezetal.[9]developedasystemspecificallydesignedforgeneratingpreference
datathatincorporatescontextualinformation.Theiraimwastoaddressthelackofsuitablebench-
marksinthisareaofresearch.Interestingly,theirgeneratorcanmixrealandsyntheticdataand,
thus, mimic properties from existing datasets. However, a change in the data, e.g., user taste, is
notconsideredinthegenerationprocess.ThesameholdsfortheworkofMontietal.[31],who
present a cluster-based data generation method that learns the rating behavior of specific user
communitiesandusesthisinformationtogeneratenewratings.
IntheworkofKoren[24],theauthorsproposedtocapturethetemporaldynamicsofuserpref-
erences.Morespecifically,theytriedtomodelgradualandsuddendriftsusinglinearandspline
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

ModellingConceptDriftinDynamicDataStreamsforRecommenderSystems 24:5
modelingofuserbiases.Theyalsoexploredtheimpactofdayeffectsonthebias.Theresultsshow
that the splines are more flexible in capturing user effects on gradual drifts, and the single-day
effectsareusefulforcapturingsuddendrifts.Similarly,theworkofBakir[4]describestheadop-
tionofamatrixfactorization(MF)modelusingSVD,andtomapthetemporaldynamics,the
authorsproposedtheapplicationofaconversionfunctionusedforthecalculationoftheageof
the ratings, giving more weight to more recent ratings and slowly forget old preferences. The
authorsassumedthatagradualtransitionexistsintheusers’preferences.Withtheincreaseofin-
terestindeeplearningmodels(embedding),researchersdevelopedsomesolutionsforasequential
recommendation.
Inparticular,[28]usedself-attentionmechanismstocaptureinteractionsbetweentwowatched
itemsinpredefinedtimeintervals.AnotherapproachproposedbyKangandMcAuley[22]assigns
weights to watched items to forget past interactions or give relevance to them. In both cases,
the authorsare trying to model the changes in user preferences. Our work not only models the
users’preferencesbutalsoiscapableofgeneratingartificialdriftsorproducingsyntheticdatawith
similardatadistributions.
ArecentworkproposedbyVelosoetal.[43]modelsuserpreferencesusingincrementallyup-
dated embeddings. The proposed model is equipped with a drift detector to capture changes in
users’ preferences and initiate a real-time optimization task. The main idea is that every time
during the learning process a drift is detected, the model needs to be adjusted by changing its
hyperparameters.
Regarding drift detectors, there are several solutions available in the literature. Drift Detec-
tionMethod(DDM)proposedbyGamaetal.[14]observesthelearnererrorrateandassumes
thatwith theincreaseof observedexamples, theerror ratewill decreasesince thedata distribu-
tionisstationary.Iftheerrorrateincreasesaboveaspecificthresholdcalculatedbasedontheerror
rate and standard deviation at one specific instant, it will trigger one alarm. Another variant of
thismethodcalledtheEarlyDriftDetectionMethod(EDDM),proposedbyBaena-Garcíaetal.
[3],wasdevelopedtoimprovedetectionperformanceundergradualconceptdrifts.Theauthors
proposedadoptingrunningaveragedistanceandrunningstandarddeviationsinsteadofcalculat-
ingthevaluesatspecificinstants.TheHoeffdingDriftDetectionMethod(HDDM)proposed
byFrías-Blancoetal.[12]workswithadifferentprinciple.ItusestheHoeffdingsinequalityanda
movingaveragetesttodetecttheconceptdrifts.ThePage–HinkleymethodproposedbySebastião
andFernandes[36]detectschangesusingtheCUSUMcontrolchartandcomputestheobserved
valuesandtheirmeanuntilthecurrentinstant.Ifthereisachange(increasingordecreasingthe
mean),itwillsignalanalarmbasedonapredefinedthreshold.Finally,theAdaptiveWindowing
(ADWIN) method proposed by Bifet and Gavalda [8] uses a dynamic-sized window that keeps
recent examples with the same data distribution. The window can be split into two parts and
comparedifthedatadistributionisthesameonbothsub-windows,signalinganalarmifthiscon-
ditionisinvalid.ThefocusofthisworkisnottodevelopnewDDMsbuttousethemtoidentify
thechangesinthedatadistributionsandbuildaportfolioofmodels.
Lex et al. [27] propose the adoption of Base-Level Learning (BLL) equations from the
cognitivearchitectureACT-Rtogetherwithrecency-basedmodelingofmusicgenrepreferences,
whichindicatesatendencyforindividualstolistentogenrestheyhaverecentlyencountered.The
significanceoftemporaldriftinmusicgenrepreferencesappearsinallusergroups.Consequently,
incorporatingrecencyinformationisexpectedtoenhancepredictionaccuracy.Similarly,Oyewole
[33]introducedamodelforusertemporalpreferencesdesignedtoascertaintherecencyweight
of an item, thereby capturing shifts in user preferences over time. The core principle of this
time-weightedalgorithmisthedeterminationofappropriateweightsforallitems,ensuringthat
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

24:6 L.Caropreseetal.
morerecentlypurchaseditemshaveamoresignificantinfluenceonsubsequentrecommendations.
Consequently, items purchased more recently are typically assigned higher weight values than
thosepurchasedearlier.
Hanetal.[18]proposeahypergraphwaveletlearningmethodologytocapturethesubtledrifts
in job preferences. To address the impact of noise in interactions, which is often a consequence
of frequent preference changes (drifts), they introduce an adaptive wavelet filtering technique
designedtoeliminatethesenoisyinteractions.
AccordingtoSunetal.[39],therecommendationforeachuserisconceptualizedasanindividual
learning task that aims at capturing region-independent personal preferences by utilizing their
check-indatawithoutconsideringspecificregions.Understandingusers’immediatedemandsand
modelingshort-termpreferencesarecrucialforthesubsequentrecommendation.Toachievethis,
theyemploysequentialmodelstorepresentusers’personalpreferences,therebyexploringtheir
behaviorpatternsthroughtheircompletecheck-insequencesusingLSTMmodels.
Thaipisutikul[40]integratescontextualinformationintothesubspacedecompositionofshort-
term and long-term memory units within the Long Short-Term Memory (LSTM) framework.
Specifically,theyintroduceamechanismtoattenuatetheinfluenceofthememorycellsuchthat
as time progresses or concept drift occurs, the impact of prior memory on the current output
diminishes.
Yang et al. [48] employ a recurrent neural network (RNN)-based model to generate short-
term user preferences, incorporating dual branches specifically designed for preference transfer
and drift. The transfer branch and the Point of Interest (POI) embedding vectors are shared
betweentouristsandresidentswithinthecurrentcity.Incontrast,thedriftbranchcapturesvaria-
tionsinpreferencesamongdifferentuserroles,includingatouristintheirhomecity,atouristin
thecurrentcity,andaresidentinthecurrentcity.
Wangwatcharakul and Wongthanavasu [46] propose a model that learns multi-transition
low-dimensionalfactorstoeffectivelycapturevariationsinuserinterestsacrossdifferentperiods.
The model emphasizes the importance of temporal influences, noting that a well-designed
algorithm should progressively diminish the impact of older data while maintaining accuracy
in predicting future user preferences. Initially, the model calculates the rating shift rate using
a time decay function that accounts for the forgotten information. Subsequently, it captures
the latent drift in user factors between successive time points to monitor the multi-transition
factors.
To our knowledge, the work of Jakomin et al. [21] is the only one that addresses incremen-
tal changes in the data. In this study, the authors present a method to generate multiple inter-
dependent data streams to evaluate recommendation or data fusion algorithms. The main idea
behindtheirgeneratoristosimulatescenarioswheregroupsofsimilarusersrategroupsofsim-
ilaritemsinthesamemanner.Inotherwords,differentprobabilitiesconnecttheresultingusers
anditemclusters.Theseprobabilitiesdeterminetheratingsthatusersofagivenuserclusterwould
giveanitemofagivenitemcluster.Theoutputisaratingmatrixwhereeachnon-zerocellrep-
resents the relation between a particular user and an item. Using arithmetic operations such as
multiplication or division to the ratings at a given time allows them to simulate concept drift.
However,thisrepresentsalimitation,asitdoesnotconsiderchangesinthelatentfeaturespace;
i.e.,theembeddingremainsatasimilarsize,andusersanditemsremainconnectedtothesame
featuresasthedataevolves.Ourworkdiffersfromtheliteratureinthefollowingaspects:(i)We
modeltheuser/itempreferencesandtheirevolutionovertimeasadynamictripartitegraph;(ii)
Welearnfromarealdatastreamasequenceoflatentmatricesthatmodelsthisgraph,and,lastly,
(iii)Weusethissequencetoproducesyntheticdatastreamswhosepropertiesaresimilartothose
oftheoriginalone.
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

ModellingConceptDriftinDynamicDataStreamsforRecommenderSystems 24:7
3 DataStreamModelling
Theproposeddatageneratorcanproducesyntheticstreamsofpreferencedatabasedonagraph
learned from real data. The generation process and the drift operations will be explained in the
followingsections.
3.1 BasicFramework
We start by introducing the notation to be used throughout the remainder of this article. In the
following,u ∈U = {1,...,N} indexesauser,andi ∈ I = {1,...,M} indexesanitemforwhich
ausercanexpressapreference.Letr ∈ {r ,...,r }denotesthepreference(rating)ofuser
u,i min max
u for itemi. The range {r ,...,r } represents a preference rank: Whenr = r , useru
min max u,i min
maximally dislikes item i, while r = r denotes maximal preference for the item. Typical
u,i max
ranges are {0,1} (implicit preference) or {1,...,5}. In the following, we shall focus on implicit
preferences.
The set of all preferences can be represented as a rating matrix R, or alternatively, as a set
of triplets R = {(u ,i ,r ),...,(u ,i ,r )}, where each triplet (u ,i ,r ) represents an inter-
1 1 1 n n n j j j
action between any user u and any item i , with r = r being the corresponding rating.
j j j uj,ij
When N and M are large, R only represents a partial and extremely small view of all possible
ratings.
WeadoptanMFframeworkforpredictingthescorethatauseru assignstoeachitemi.Each
useruanditemiadmitarepresentationinaK-dimensionalspace.Wedenotesuchrepresentations
byembeddingvectorsp ,q
∈RK,whichrepresenttherowsoftheembeddingmatricesP∈RN×K
u i
andQ∈RM×K.
Given useru and item i, the corresponding score r can be modeled as a random variable
u,i
withafixeddistributionwhoseparametersrelyontheembeddingsp andq .Thismodelcanbe
u i
represented with a weighted and undirected tripartite graph. It has three types of nodes: Nodes
representingusers(usernodes),thoserepresentingitems(itemnodes),andthoserepresentingfea-
tures(featurenodes).Edgescanonlyconnectuserstofeaturesoritemstofeatures.Theweightof
auser/featureedge(resp.item/featureedge)isameasureofhowstronglythatfeatureispresent
intheuser(resp.item);seeFigure1.
The preference matrixR induces a natural ordering among items, wherei (cid:4) j means thatu
u
prefersi to j, i.e.,r > r . The additional assumption that we make in this work is that the
u,i u,j
partialviewRcanbecontinuouslyupdated.Thatis,eithernewunknownentriescanbedisclosed
(forexample,someuserscanexpresspreferencesforpreviouslyunseenitems)orformerprefer-
enceschange(forexample,duetochangeoftastesbytheuser,orduetoamoreaccurateevalu-
ation). Thus, weassume thatthehistoryofpreferencesproducesacontinuousstreamof shards
R
(1)
,R
(2)
,...,R
(t)
,whereR
(t)
representstheviewofRattimet.
Asalreadymentioned,snapshotscanoverlap,i.e.,itcanhappenthatbothr
(n)
andr
(m)
existfor
(cid:2) u,i u,i
m (cid:2) n, and r u (n ,i ) (cid:2) r u (m ,i ) . We then defin (cid:2) e n≤t R (n) as a merge among R (1) ,R (2) ,...,R (t) that
preserves recency. That is, by denoting n≤t R (n) as V (t) , we define V u ( , t i ) = r u (t , ∗ i ) , where t ∗ =
max{t |(u,i,r )∈R (t)}.Ifnosucht ∗ exists,thenV (t) isundefined.
u,i u,i
Over time, the distribution of data can change, more or less abruptly. When this occurs, we
are facing a concept drift. The situation is illustrated in Figure 2. Typically, we can consider a
streamasthecooperationofmultipleregimesthatinteracttoproduceobservabledata.Aregime
i ischaracterizedbyanunderlyingmodel,describedbyfactorizationmatrices P
(i)
andQ
(i)
.The
appearance of a new regime as a result of a shift in data distribution reflects changes in user
preferencesortheentryofnewfeatures.Asshowninthefigure,thechangesareessentiallydue
tochangesintheunderlyinggraphwhichreflectondifferentsamplesinthedatasamplingprocess.
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

24:8 L.Caropreseetal.
Fig.1. User/Feature/Itemgraph.
Fig.2. Regimesinadatastream.
Thechallengeofmanagingnewusersoritemscanbeaddressedbyaddingnewnodesinitialized
withaheuristicfunctionthatconsidersthecharacteristicsofthegraphintheithregime.However,
thisapproachintroducesanadditionallayerofcomplexity.Afeasiblesimplificationistoavoidim-
posingspecificassumptionsandinsteadinitializethenodesrandomly,thenevaluatethevariation
inmodelperformanceacrossdifferentregimes.Thatistheactualimplementation.
Inpractice,theproblemwewanttofaceis howtodeviseadata generationprocessbasedon
factorizationmatricesPandQ,capableofreflectingsuchchanges.Aninitialattemptinthisdirec-
tionwasmadein[43].Moreimportantly,thequestionswewanttoanswerhereare:Whatarethe
typicalchangesthatcharacterizeareal(orrealistic)datastream,andhowcanwemodelthemby
controllable(model-based)adaptationsoftheunderlyingsamplingprocess?
Weapproachthisproblemintwodifferentsteps.Inthefirststep,westudyhowapopularfac-
torizationmodel[34]canbeusedtotrackanddescribechangesinareal-lifedatastream.Forthis,
weproposeaninferencealgorithmthat,givenadatastream,iscapableoftrackingviablechanges
andadaptationsoftheunderlyingmodeltoreflecttheactualstream.Thestudyandcharacteriza-
tionofsuchchangeswillthenallowustodeviseafullycontrollableprocedureforgeneratingdata
streamsexhibitingconceptdrifts.
3.2 LearningConceptDrifts
TheformulationweconsiderisinspiredbytheBayesianPersonalizedRanking(BPR)model
introducedin[34].TheBPRmodelisapopularimplementationforMF-basedmodel,ensuringscal-
ability,trainableonimplicitfeedback(noratingsarerequired).Thetrainingphaseisquiteeffective,
asitisperformedbycomparingpairsofitemsthatauserhasinteractedwithandoptimizingthe
rankingoftheseitems.Thismodelallowsustoprocessdatasetswiththousandsofitemsandusers.
Beinghighlypopularinliterature,itrepresentstheprimarychoicemadebynumerousauthorsin
the field of RS. Moreover, the BPR model is chosen because of its robustness and suitability for
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

ModellingConceptDriftinDynamicDataStreamsforRecommenderSystems 24:9
handlingimplicitpreferences.However,thekeyaspectoftheapproachisnotjustthemodelitself
butitsabilitytotrackchangesovertimethroughadjustmentsinthelatentfactormatrices.Inprin-
ciple,anyMFmodelthatsupportsaprobabilisticinterpretationofuser/itemadoptionintermsof
latentfactorscouldbeused.
Theideaunderlyingthismodelisthatapreferencei (cid:4) jcanbedirectlyexplainedascloseness
u
inalatentspacewherebothitemsanduserscanbemapped.Mathematically,thiscanbedevised
bycomputingafactorizationrankpTq foreachpair(u,i),andmodelingprecedencesbymeans
u i
ofaBernoulliprocess:
(cid:3) (cid:4)
i (cid:4) j ∼Bernoulli(p), p =σ pT(q −q ) ,
u u i j
whereσ(a) = (1+e −a)−1 isthelogisticfunction.TheoptimalembeddingsM = (P,Q)canhence
beobtainedbyoptimizingtheloss:
(cid:5)(cid:5) (cid:3) (cid:4)
(cid:2)bpr(M|V)= logσ pT(q −q ) , (1)
u i j
u i,j
i(cid:4) uj
wherei (cid:4) j meansV >V .
u u,i u,j
We can exploit the above learning(cid:6) scheme(cid:7) to devise a sequence(cid:2)of embeddings
M (t1 ) ,...,M (th ) ,... where each M (t) = P (t) ,Q (t) is trained on V (t) (i.e., n≤t R (n) ) as ex-
plained below. In particular, each model of this sequence represents a different regime and
characterizesitsdatadistribution.
Typically, RS are optimized by exploiting historical interactions as training data, to produce
a model that can predict users’ future interactions in the testing data. This scheme inherently
assumesthatthetrainingandtestingdataaredrawnfromthesamedistribution.However,distribu-
tionshiftscanoccurwhenchangesinthepreferences(expressedasmodificationsintheunderlying
graphdiscussedintheprevioussection)occur.Inpractice,amodeltrainedoncurrentdataislikely
todeteriorateitsperformanceonfuturedatawhenasubstantialdriftinthepreferencesoccurs.
TheseobservationsinspireaspecificprotocolfortrainingtheembeddingsM
(t1 )
,...,M
(th )
,...
characterizingthedrift.Thetimestampt
i
hererepresentsthedrift:modelM
(ti−1 )
underperforms
onR
(ti )
and,asaconsequence,weneedtoretrainthemodel.Theideaistodeviseacontinuous
learningframeworkthroughtheshards:ateachstept themodelisoptimizedonV
(t)
.Ifthemodel
substantiallyunderperformsonR
(t)
,thenanadaptationisrequired.Formally,wedefinetheloss
(cid:5)
Lc(M;R)= (cid:2)bpr(M|R)+λ(||P||
∞
+||Q||
∞
)
u∈S
thatincludestheregularizationterm.
ByminimizingtheinfinitynormofPandQ,weenforceanupperboundonthematrixweights
duringthetrainingprocess.Thisensuresthattheweightsbelongtoalimitedrange.
Then, given a current model M, we check whether a drift has occurred by checking the loss
Lc(M;R (t)).
Ifnodriftisdetected,theprocessproceedsintwosteps:
—First,asyntheticinteractiondatasetS isgeneratedfromM.
—Next,MisupdatedbyoptimizingthelossLc(M;S (cid:9)R (t)).
The second step resembles a continual learning strategy [13]. In principle, the model should
be updated from the entireV
(t)
. However, in a streaming scenario, it is impractical to maintain
thewholesetofpastinteractions.ExploitingthecurrentmodeltogenerateasampleS,withthe
same size of R
(t)
, has the advantage of compacting the representation of past interactions and
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

24:10 L.Caropreseetal.
additionally, it provides better control on past preference shifts since the model will disregard
obsoleteinteractions.
If a drift is detected, M is obsolete and requires a substantial update. In our framework, this
means that the graph topology can change, with new users/items and/or features. We adopt a
conservativeapproachtotacklingthisproblem.Foragivenuser/featureprobabilityvectorp ∈
u
RK,itispossibletodeviseaninfinite-dimensionalextensionp (cid:10) ∈ R∞ initializedsuchthatp (cid:10) =
u u,k
p if1 ≤ k ≤ K,andp (cid:10) = 0fork > K,andthesamepropertyholdsforitem/featurevector
u,k u,k
(cid:10)
q .Thus,givenM,wedenotebyM itsinfinite-dimensionalcounterpart.Thelearningobjective
i
(cid:10)
onthenewregimecanhencebestatedascomputinganewversionM withminimaldifferences
w.r.t.M.Formally,wedevisetheloss
(cid:8)
(cid:5)(cid:5)K (cid:5)(cid:5)K
Ld(M (cid:10) ;M,R (t))=Lc(M (cid:10) ;R (t))+δ |p (cid:10) −p |+ |q (cid:10) −q |
u,k u,k i,k i,k
u k=1 i k=1 (cid:9)
(cid:5)(cid:5) (cid:5)(cid:5)
+ |p (cid:10) |+ |q (cid:10) |
u,k i,k
u k>K i k>K
thesecondterminthelossrepresentsthedivergencebetweenunderlyingfeaturevectors.Thera-
tionalehereisthattheupdatedmodelshouldpenalizeunnecessarydiscrepancieswiththeprevious
modelonthecurrentfeatures,whileatthesametimelettingthemodelintroducenewfeaturesin
ordertoadapttothecurrentchanges.Inpractice,thetrainingstartsbyaddingΔ newcolumns
K
(initially set to 0) to both P and Q and then optimizing the extended model through Ld on the
new shard R
(t)
. Algorithm 1 provides an overview of the learning procedure. In this procedure,
weutilizethedriftDetectionfunctiontodetectanydriftsinthelosses.Theeffectivenessofdrift
detection heavily relies on the chosen signal, which in our case is primarily the loss values. By
monitoringthelossfunction’svalue,wecanidentifysignificantdeviationsinthemodel’sperfor-
mance,indicatingthepresenceofdrifts.However,itisworthnotingthatthechoiceofthesignal
fordriftdetectioncanvarydependingonthespecificapplicationandproblemdomain,whichcan
leadtodifferentperformancefordetectionalgorithms.WeemploytheHDDM algorithm[12],a
W
well-knownDDMbasedonHoeffding’sboundswithamovingweightedaveragetest.HDDM uti-
W
lizestheExponentiallyWeightedMovingAverage(EWMA)statisticasanestimator.Givena
streamofvalues(inourcase,lossvalues)asinput,itdeterminestheestimatedstatusofthestream:
Stable,Warning,orDrift.1
Therefore,themodelisupdatedusingtwotrainingmodalities:
(cid:10)
—whenadriftoccurs,wetrainthemodelM withthedataofthecurrentshardandpenalize
(cid:10)
thedistancebetweenM andthemodellearnedinthepreviousregimeM;
—otherwise, the current model M is refined on data of the current regime and a sample of
historicaldatageneratedfromthemodelMofthecurrentregime.Thisguaranteesthatthe
modelisawareofbothasummaryofthepreviousdataandthenewdataavailable.
Finally, the generateSamples function leverages the matrix M to generate n new samples.
S
This procedure involves sampling items for each user based on their score, with the probability
of selection proportional to the score. The item frequency for each user (or user frequency
for each item) can be estimated using a Zipf distribution or provided as input to preserve the
originalproperties.Thesefrequencieshelpdeterminethenumberofitemstosampleandbiasthe
probabilityofselectinglow-popularityitems.
1NoticethattheadoptionofHDDMW requiresboundedsignals,whichcanbeguaranteedbyboundingthedifferencein
Equation(1).
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

ModellingConceptDriftinDynamicDataStreamsforRecommenderSystems 24:11
Thesampleiscombinedwiththeshard’sdatatotrainthecurrentmodel.Thisapproachaims
atretaininghistoricalinformationwithoutrequiringthestorageofalldatainthecurrentregime,
inthiswaywebalancetheweightofnewpreferencesandthepastones.However,whenadrift
occurs, we switch to a different strategy aimed at minimizing the deviation from the previous
model;therebyreducingtheimpactofthelimitedcurrentdata,i.e.,thepreferencesofthecurrent
shard,onupdatingthenewmodelandpreservingasofttransitionbetweenregimes.Thevalueof
parametern hasbeensetequaltothesizeoftheBtrain setofthecurrentshard,weightingequal
S
tothenumberofpreferencesobservedinthecurrentshardandinthecurrentregime.
4 Experiments
WeconductedanempiricalevaluationofAlgorithm1withtwomainobjectives.Firstly,weaimed
to monitor actual drift in realistic scenarios. Secondly, we aimed to devise a data generator that
captures the properties of realistic data streams and effectively models concept drift similar to
whatisobservedinrealdata.
Weprocessedthreerealdatastreamsusingourproposedapproach.Duringthetrainingphase,
weidentifiedasequenceofregimesforeachdataset,eachcharacterizedbyitsdatadistribution.We
associatedanMFmodelwitheachregime.Usingthissequenceofmodels,wegeneratedasynthetic
datastreamthatcloselyresembledtheoriginalstream.Thiswasachievedbyimposingthesame
regimesinthesameorder,withanequalnumberofsamplesforeachregime.Bycomparingthe
originalandsyntheticstreams,weassessedthefidelityofthegeneratorinsamplingnewdata.
Ourapproachyieldedsatisfactoryresultswhenthenumberofitempreferenceswassufficiently
hightotrainamodelcapableofreplicatingarealstream.Thiswasespeciallyevidentindatasets
where there were numerous items with few preferences and a core set of highly popular items.
Thebehaviorcanbeexplainedbythemodel’sinabilitytoaccuratelyestimatethedistributionof
underrepresented items. To achieve good generation performance, it was crucial to have a suffi-
cientnumberofpreferencesforeachitem.Thisconditionwasnaturallymetwhenthenumberof
userssignificantlyexceededthenumberofitems.Infact,thefirstandthirddatasetssatisfiedthis
condition,asthedistributionofthesyntheticdatacloselyresembledthatoftheoriginaldata.
Wealsochoseaseconddatasetthatdidnotexhibitthisbehavioralpattern,wherethenumberof
userswasmuchsmallerthanthenumberofitems.Inthiscase,thedistributionofthesyntheticdata
generatedbythegeneratordeviatedsignificantlyfromtheoriginaldata. Tofurthersupportour
hypothesis,wereversedtherolesofusersanditemsandrepeatedtheexperiment,demonstrating
the importance of having an adequate number of preferences to derive an effective model. The
resultsweresatisfactoryinthiscase.
Additionally,weselectedathirddatasettoanalyzechangesindistributionsduringadrift.We
drewinsightsfromastudybyYangetal.[49],wheretheytackledthechallengeofdevelopinga
recommendersystemthatcanadapttothedynamicnatureofuserpreferencesanditempopularity.
Tofosterreproducibility,wehavepubliclyreleasedallthedataandcoderequiredtoreproduceour
experiments.2
4.1 Datasets
Our analysis is conducted on the following popular benchmark datasets, each from a different
domainandhavingspecificcharacteristics:
—MicrosoftNews(MIND):ThisdatasetconsistsofnewsarticlespublishedontheMicrosoft
Newswebsiteandthefeedbacklogsgeneratedby1millionusersoveraspanof6days.We
2https://github.com/fsp22/mcd_dds4rs
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

24:12 L.Caropreseetal.
ALGORITHM1:LearningLatentMatrices
|     | StreamR=R | (1) (n) |     |
| --- | --------- | ------- | --- |
Input: ,...,R ,...ofpreferencesorderedinshards;numberofsamplesnS to
generatefortrainingthemodelwithinthei-thshard,inconjunctionwiththeshard’sdata.
|         | (0)    | (h)                           |     |
| ------- | ------ | ----------------------------- | --- |
| Output: | AlistM | ,...,M ,...ofpreferencemodels |     |
t =0;(cid:2)=∅
1
| q=∅;r | =∅  |     |     |
| ----- | --- | --- | --- |
2
| initializeM | (t) |     |     |
| ----------- | --- | --- | --- |
3
(i) Rdo
| 4 foreachR | in                    | (cid:3) | (cid:4) |
| ---------- | --------------------- | ------- | ------- |
|            | Btrain,Btest =splitDa | ta (i)  |         |
| 5          |                       | R       |         |
|            | (cid:3)               | (cid:4) |         |
(t)
| 6   | (cid:2)drift =Lc M                          | ;Btest |     |
| --- | ------------------------------------------- | ------ | --- |
| 7   | drift =driftDetection((cid:2)drift,(cid:2)) |        |     |
ifdriftthen
8
|     | (t+1) :=extendModel(M |              | (t) )                 |
| --- | --------------------- | ------------ | --------------------- |
| 9   | M                     |              | ,ΔK                   |
|     | optimizeM             | (t+1) onLd(M | (t+1) ;M (t) ,Btrain) |
10
| 11  | t+=1 |     |     |
| --- | ---- | --- | --- |
end
12
else
13
|     | =generateSam | ples(M  | (t) ,q,(cid:4)r) |
| --- | ------------ | ------- | ---------------- |
| 14  | S,q,r        | (cid:3) | ,nS              |
(t) onLc (t) ;S(cid:9)Btrain
| 15  | optimizeM | M   |     |
| --- | --------- | --- | --- |
16 end
(t)
|     | (cid:2)eval =Lc(M | ;Btest) |     |
| --- | ----------------- | ------- | --- |
17
(cid:2)=(cid:2)∪{(cid:2)eval}
18
(i)
|     | Updateuseranditempopularitiesq,r |     | basedonR |
| --- | -------------------------------- | --- | -------- |
19
20 end (cid:10)
(t)}
| return | {M  |     |     |
| ------ | --- | --- | --- |
| 21     | t   |     |     |
FunctiongenerateSamples(M,nS,q=∅,r =∅,α =1.8,β =1.9,c =1,d =5):
22
23 Functionnormalize(μ):
|     | p˜=σ(c·μ −d) |     |     |
| --- | ------------ | --- | --- |
24
(cid:11)
|     | returnp˜/( | p˜ ) |     |
| --- | ---------- | ---- | --- |
| 25  |            | i i  |     |
ifq=∅then
26
∈U =Zipf(α,1,M/c)
| 27  | foreachu | do qu |     |
| --- | -------- | ----- | --- |
end
28
=∅then
29 ifr
|     | ∈I       | =Zipf(β,1,N/d) |     |
| --- | -------- | -------------- | --- |
| 30  | foreachi | do ri          |     |
end
31
∈U
| 32  | foreachu       | do(cid:11)   |     |
| --- | -------------- | ------------ | --- |
|     | = (cid:13)nSqu | /( )(cid:14) |     |
| 33  | qu             | qu           |     |
u
|     | p˜ =normalize       | (pu ·Q)    |     |
| --- | ------------------- | ---------- | --- |
| 34  | u                   | (cid:11)   |     |
|     | =(p˜ (cid:15)r)/(   | )          |     |
| 35  | pu u                | i p˜ u,iri |     |
| 36  | nu =min(qu,|{i|pu,i | >0}|)      |     |
Samplewithreplacementnu itemsIu fromI withprobabilityproportionaltopu
37
|     | =generateTriplets(u,Iu |     | )   |
| --- | ---------------------- | --- | --- |
| 38  | S                      |     |     |
end
39
40 returnS,q,r
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

ModellingConceptDriftinDynamicDataStreamsforRecommenderSystems 24:13
utilizetheclickinformationofeachnewsarticlebyuserstoconstructadataset.Theread
newsarticlesserveasuserpreferences,andweconsideronlyuserswhohaveatleastone
preference(newsread).Thefinaldatasetcomprises19,206itemsand3,958,500preferences
from750,434users.Thedatasetcanbeaccessedathttps://msnews.github.io/.
—Amazon Video Games: This dataset contains ratings provided by users for video games.
The ratings range from 1 to 5. As our approach focuses on implicit feedback, we binarize
thedatabyassigningavalueof1touser-itempairswheretheratingisstrictlygreaterthan
3,and0otherwise.ToaddressGPUmemorylimitations,weprocessasubsetofthedataset,
consideringthelast824,752preferencesfrom26,038usersregisteredoveraspanof10years,
withrespectto567,865items.Thedatasetcanbeaccessedathttp://snap.stanford.edu/data/
amazon/productGraph/categoryFiles/ratings_Video_Games.csv.
—Yoochoose:ThisdatasetwaspublishedfortheRecSysChallenge2015.Itcomprisesacol-
lectionofsessionsfromaretailer,specificallyfocusingonthepurchaseeventsofusers.To
streamlinethedataset,weselecteditemsthatwereinteractedwithmorethan4timesand
removed users with fewer than 3 purchased items. After the cleaning process, the dataset
consistsof143,481users,9,975items,and642,237interactions.Thedatasetcanbeaccessed
athttps://www.kaggle.com/datasets/chadgostopp/recsys-challenge-2015.
These datasets were chosen due to their popularity and diverse characteristics, enabling us to
conductcomprehensiveanalysesanddrawmeaningfulconclusions.
4.2 ModelingDataStreams
FollowingtheprotocolpresentedinSection3,wetestourmodelonthedatasetsreportedinSec-
tion4.1.Foreachuseru andeachitemi whichispositiveforu (i.e.,(u,i,1) ∈ R (t) ),fournegative
itemsjaresampled(i.e.,(u,j,1)(cid:3)R (t) ).Inourframework,weconsiderasnegativeanyitemthatis
notexplicitlypositiveforauser.Thisincludesbothitemsthattheuserhasneverinteractedwith
anditemsthattheuserexplicitlydislikes.Thus,inthiscase,(u,j,1)mustnotbelongtoR (t) which
isdifferentfromsayingthatu dislikesj,i.e.,(u,j,0)mustbelongtoR (t) .
ThisapproachiscommoninRS,particularlywhendealingwithlargeitemcatalogs.Theratio-
nalebehindthismethodliesinthetypicalcharacteristicsofrecommendationscenarios.Inmost
cases,thenumberofitemsauserlikesissignificantlysmallerthanthetotalnumberofavailable
items.Forinstance,inacatalogofmillionsofproducts,ausermightonlybeinterestedinafew
hundred.Thiscreatesaverysparsepreferencematrix.Giventhissparsity,randomlysamplingan
itemhasahighprobabilityofselectingonethattheuserwouldnotlikeorhasnotinteractedwith,
makingitareasonableproxyfornegativefeedback.Thisassumptionsimplifiesthemodelingpro-
cessandisespeciallyusefulwhendetailedinteractiondata(likeviewedbutnotpurchaseditems)
isnotavailable.
Thetriplets(u,i,j)areprocessedinchronologicalordergroupingtheminbatchesof2000tuples.
WespliteachbatchBintwosets:(i)atrainingsetBtrain (70%),and(ii)atestsetBtest (30%).
To train the model, we use 20 epochs; the optimizer is the ADAM algorithm with a learning
rateof0.001,andthelossfunctionsarepresentedinSection3.2.Aftereachbatch,weevaluatethe
model on the test set, and we report some performance metrics. We consider(cid:2)bpr(M|Btest) and
theHit-Ratescore.Letusrecallthedefinitionofthislastmetric:GivenauseruoccurringinBtest,
weconsiderthesetP ofitspositiveitems(i.e.,P = {i | (u,i,j) ∈ Btest})andsampleasetN of
u u u
negativeitems(|N | = 100,inourcase).Thenforagivencutoffk (weusek = 10andk = 5)we
u
considerthek −1negativeitemsinN forwhichMreturnsthehighestscore.Amongthem,we
u
considertheitemj withthelowestscore.Thereisahitwithcutoffk,fortheuseru andtheitem
i ∈P ,ifM(u,i) ≥ M(u,j).Inthefollowing,wereportbothHR@5andHR@10.
u
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

24:14 L.Caropreseetal.
Fig.3. LossontestsetpartofeachbatchoftheMicrosoftNewsdataset.
Fig.4. ResultsfortheMicrosoftNewsdataset.
4.3 ExperimentonMIND
Figure3showsthelosscomputedonthetestpartofthecurrentbatch(i.e.,Lbpr(M,Btest))aver-
agedonamovingwindowof20batches.Themovingaveragehighlightstheincreasing/decreasing
trend, disregarding a local minimum/maximum. The orange vertical lines indicate the batches
wherethedriftalgorithmhasdetectedawarningbeforeapotentialdrift;meanwhile,theredlines
indicateadrift.
Thelossisrelativelystablewithminimalincrease/decreaseduetothenatureofthedataset.The
numberofitemsislessthanthenumberofusers,whilethenewsareequallyscatteredacrossthe
dataset that covers only six days. For this reason, each batch contains a few new items, and the
preferencesonhotnewsregisteredinafewhoursshouldmotivatethehighnumberofwarning
and drift alerts and the value differences between consecutive batches. We highlight that each
batchcontainsthenewsreadinafewminutes.
ThegoodperformanceinthelosschartcanbealsoseenintheHitRatecharts.JustafterBatch
500,inFigure4(a),wecanseealowHRvalue(HR@5≈0.6).Thisbehaviorcouldbeexplainedby
adriftfollowing multiplewarningsintheregionclosetotheminimum. Probably,thisindicates
asignificantchange.ComparingtheHR@5valueswiththeHR@10values,thesecondonesare
betterforthesamebatches,indicatingthatthemodelworsensthepredictionsonlyonsomeitems
whilemaintaininggoodoverallperformance.Thenumberofwarningsisduetothefluctuations
recordedintheloss.
ThevisualrepresentationinFigure5providesinsightsintothedistinctionsbetweensegments
oftherealdatacorrespondingtodifferentregimesandtheirsyntheticcounterparts.Thesynthetic
dataineachregimeisgeneratedbysamplingfromthemodeltrainedonthecorrespondingreal
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

ModellingConceptDriftinDynamicDataStreamsforRecommenderSystems 24:15
Fig.5. ComparisonofrealandsyntheticstreamfortheMicrosoftNewsdataset:ThechartshowstheP(f >
k)wheretheithfrequencyisdenotedask(log-scaleonbothaxes).
data.Toensureafairandmeaningfulcomparisonbetweenthesyntheticandoriginaldatastreams,
wemeticulouslystructuredthesyntheticdatatomirrortheoriginaldata.Thisinvolvedmaintain-
ingthesameregimesinthesameorderandensuringanequalnumberofsamplesforeachregime.
Inthecharts,thehorizontalaxisrepresentstheithfrequencydenotedask,whilethevertical
axisindicatesthecumulativecountofitems(i.e.,P(f >k)),normalizedbythesumofvalues.Upon
analyzingthedistributions,weobservethatthefrequenciesexhibitcomparablepatterns,thereby
confirmingtheeffectivenessoftrainingthedifferentmodels.Thesimilarityisalsoconfirmedbya
positiveoutcomeoftheKolmogorov–Smirnovtest[20]oneachregime.
Theobservedsimilaritybetweenthedistributionsinthechartsservesasstrongvalidationfor
theeffectivenessandfidelityofourapproachingeneratingsyntheticdatathataccuratelyrepro-
ducesthecharacteristicsoftheoriginalstream.
It’scrucialtonotethatourcomparisonfocusesonfrequencydistributionsratherthanprefer-
encedistributionsinthecharts.Thisdeliberatechoiceismotivatedbytherecognitionthatcom-
paringpreferencedistributionscanbeproblematicduetotheinfluenceofpopularitybiasonpre-
dictivemodelsforpreferencedata[23].Popularitybiastendstooverlookcontributionsfromcold
startusersandlow-popularityitems,especiallyinpreferencedatawithvastitemcatalogs.Com-
paringdistributionsbasedonpreferenceswouldconsequentlyfail,duetoinaccurateassociations
involving cold-start users and/or low-popularity items. By contrast, it is important to highlight
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

24:16 L.Caropreseetal.
Fig.6. LossontestsetpartofeachbatchoftheAmazonVideoGamesdataset.
Fig.7. ResultsfortheAmazonVideoGamesdataset.
thatsuchinaccuraciesdonotsignificantlyimpacttheglobalmodelingcapabilitiesofthelearned
embeddingmatrices,whichisthemainfocushere.
4.4 ExperimentonAmazonVideoGames
Weconductedsimilarexperimentsfortheothertwodatasets.Firstly,fortheAmazonVideoGames
dataset,weanalyzedthelossvalues(Figure6)andHitRate(Figure7)onthetestset.Inthesecharts,
weobservethepresenceof 7 regimes, indicating 6 detecteddriftsby thealgorithm. We observe
similarpatternsasseenintheMINDdataset,wheretheperformancedeteriorateswhenmultiple
driftsoccurincloseproximity.
Tocomparetheitemdistributionofthesyntheticstreamwiththerealstream,weexaminedthe
distributionsshowninFigure8.IncontrasttotheMINDdataset,thedistributionsinthiscaseare
significantlyworse.Thisindicatesthatthenumberofpreferencesforeachitemisinsufficientto
acquirethenecessaryknowledgerequiredtoaccuratelyreplicatethestream.
Tofurthersupportthisobservation,weinvertedtherolesofusersanditemsinthedataset.By
doing so, the number of items became smaller than the number of users, resembling the MIND
dataset. Analyzing the loss performance (Figure 9) computed on each batch (i.e., M,Btest) after
the training phase, we notice a rapid increase in loss value when a drift appears in the stream.
Subsequently, the loss value decreases as the model adjusts to the new data. Although the drift
detectionalgorithmtriggersafalsewarning,ithasminimalimpactonthelossvalue.Wedonot
observeanysignificantchangesintheHitRatevalues.
We computed HR@5 and HR@10 (Figure 10) and observed similar behavior in both settings.
The model performs poorly in the vicinity of a drift due to significant changes in the data
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

ModellingConceptDriftinDynamicDataStreamsforRecommenderSystems 24:17
Fig.8. ComparisonofrealandsyntheticstreamfortheAmazonVideoGamesdataset:Thechartshowsthe
P(f >k)wheretheithfrequencyisdenotedask(log-scaleonbothaxes).
Fig.9. LossontestsetpartofeachbatchoftheInvertedAmazonVideoGamesdataset.
distribution,evenwithnewuser/itempreferencesorpreviouslyunseenitems.However,afterthe
drift,thenewmodelistrainedontheupdateddata,andwithinafewbatches,itregainsoptimal
performance.
Incontrasttothepreviouscase,thedistributionsofthegenerateddataarenoticeablyimproved
inthisscenario.AsdepictedinFigure8,thecurvesrepresentingthedistributionsareveryclose
toeachother.Thisobservationalignswithourintuitionregardingthesignificanceofhavingan
adequatenumberofitempreferencestotrainagenerativemodeleffectively.Theclosesimilarity
betweenthecurvesconfirmstheimportanceofhavingasufficientnumberofpreferencesforeach
iteminordertoaccuratelyreplicatethedata.
4.5 ExperimentonYoochoose
TheresultsfromtheYoochoosedatasetexhibitabehaviorsimilartothepreviousdataset.Figure11
illustratesthelossonthetestset,highlightingasingledriftwherethereisanoticeableincrease
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

24:18 L.Caropreseetal.
Fig.10. ResultsfortheInvertedAmazonVideoGamesdataset.
Fig.11. LossontestsetpartofeachbatchoftheYoochoosedataset.
in the loss value. However, the changes in the data distribution have only partially affected the
qualitymeasures,asdepictedintheHitRatechartsinFigure12.
This observation suggests that while the model’s performance is impacted by the drift, it is
able to adapt and adjust to the new data to some extent. The changes in the data distribution
haveresultedinadecreaseintheHitRate,indicatingthatthemodel’srecommendationsareless
accurate during the drift period. However, it is worth noting that the model gradually recovers
andimprovesitsperformanceafterthedrift.
Overall, theresultsfrom theYoochoosedatasetconfirmthepresenceof driftand themodel’s
abilitytoadapt,albeitwithsomeimpactonthequalityofrecommendationsduringthetransition
period.
4.6 ComparisonwithaBaselineAlgorithm
Inthissection,acomparisonwasmadebetweentheBPRalgorithmandamodelthatcouldbemore
easilyadaptabletomanagingnewusers/items.Wehavechosenavariationalautoencoder,inwhich
thenumberofitemsthesystemcanhandleisfixedapriori.Themodelreceivesasinputtheitems
thatauserhasalreadyseenand,basedonthisinformation,assignsascoretotheentirecatalogto
generatearankingandthusbuildarecommendationlist.Havingthewholecatalogavailablefrom
theoutsetgivesthemodelacompetitiveadvantageovertheBPRmodel,whichinsteadadaptsby
updating thelatent space whensignificant changesare detectedin the system, both in terms of
newusers/itemsand/ornewpreferencepatternsforexistingusers/items.Naturally,theimpacton
performance will be more noticeable with many items distributed over a broad temporal range.
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

ModellingConceptDriftinDynamicDataStreamsforRecommenderSystems 24:19
Fig.12. ResultsfortheYoochoosedataset.
Fig.13. ComparisonofrealandsyntheticstreamfortheInvertedAmazonVideoGamesdataset:Thechart
showstheP(f >k)wheretheithfrequencyisdenotedask(log-scaleonbothaxes).
Fig.14. ComparisonofrealandsyntheticstreamfortheYoochoosedataset:ThechartshowstheP(f >k)
wheretheithfrequencyisdenotedask(log-scaleonbothaxes).
Conversely, in the presence of lower variability, i.e., when the model can learn patterns in the
initialmomentsthatarevalidfortheentireobservationperiod,amodelliketheVAEwillhavea
competitiveadvantageoveranadaptivemodel.
Performance was measured for three datasets: MIND, Amazon Video Games with reversed
roles, and Yoochoose. The experiment could not be executed for the original Amazon Video
Games dataset because the model required excessive memory due to the high number of items
(567,865).ConsideringtheHitrate@5values(theHitrate@10metricshowssimilartrendsandis
not reported for brevity), for the MIND dataset (Figure 15), we can observe that the VAE model
reaches a peak value in the middle of the stream and maintains constant performance for the
restoftheobservationperiod.Conversely,theBPRmodelexhibitsmorefluctuatingperformance
following the detection of drifts. The nature of the data can explain this: the dataset consists
of news produced over 6 days. In many cases, these are news items covering the same event,
resultinginreducedvariabilityinidentifieduserpreferencepatterns.Thesystemcanlearnhighly
generalizablerecommendationmodels.Forinstance,itiscommontoobservemanyuserssharing
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

24:20 L.Caropreseetal.
Fig.15. ComparingBPRandVAEontheMINDdataset(HitRate@5).
Fig.16. ComparingBPRandVAEontheInvertedAmazonVideoGamesdataset(HitRate@5).
similar patternsbecausetheyread multiple news items on thesame topic. In thiscase, the VAE
ismoreeffectiveindetectinglatentspacesimilaritiesthantheBPR.
FortheAmazonVideoGamesdatasetwithreversedroles(Figure16),i.e.,whereusersanditems
wereswappedtohaveacatalogof25kitems,weobservedworseperformancefortheVAE.Asthe
numberofnewitemsgrows,themodel’sperformancedegrades.Additionally,therecommendation
listcontainsitemsforwhichnopreferencesareobserved.AnadaptivesystemlikeBPRmanages
thesechangesbetter,ensuringsuperiorperformance.
WecanseeasimilartrendfortheYoochoosedatasetinFigure17.Themaindifferenceliesinthe
oscillatingpatternseeninthecharts.Thesystemadaptsmorequicklytochangesinpreferences,
but the limited temporal range prevents the model from converging to mid-high levels. In this
context, BPR adapts faster to changes, while the VAE system tends to be more stable around a
lower median value than BPR. Moreover, a descending trend is evident in the last shards of the
stream:arelativelyhighnumberofnewitemsappearswithalimitednumberofpreferences,and
bothsystemsstruggletoidentifynewpatternseffectively.
4.7 AblationStudy
Our approach aims at identifying a method that allows generating realistic data, replicating the
trendspresentinarealstream.Tocapturepossiblechangesinpreferences,regimeshomogeneous
inexpressedpreferencesareidentified,andtheircorrespondingmodelsarestoredtogeneratedata
derivedfromthosebehavioralmodels.Twoanalyseswereconductedtoevaluatethisprotocol:
—try ignoring the regime identification, so we train the model only on the first regime and
thentesttheperformanceondataofthenextregimes;
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

ModellingConceptDriftinDynamicDataStreamsforRecommenderSystems 24:21
Fig.17. ComparingBPRandVAEontheYoochoosedataset(HitRate@5).
Fig.18. Testperformanceofthefirstmodel,i.e.,trainedonlyonfirstregime,ontheentirestream.
—comparetheperformanceignoringthestreamnatureofthedata.Wesamplea‘small’train-
ingsetwithdataofallregimes,thentestonthefulldatasetw.r.tregimes.
Inthefirstexperiment,wetrainedasinglemodelonlyondatabelongingtothefirstregime.As
soonasadriftisdetected,themodelisfrozenandtestedontherestofthestream.Itisevident
thatthemodelachievesgoodperformanceonlyonthedatabelongingtotheregimeitwastrained
on and performs poorly on the remaining regimes (Figure 18). This result is not surprising but
confirmstheneedtoimplementamechanismofcontinuoustrainingthatcreatesandtrainsanew
modelwhenthecharacteristicsofthestreamdatachange,andtheirpropertiescannolongerbe
capturedbythepreviousone.
Inthesecondexperiment,wecreatedatrainingsetbyrandomlyextracting30%ofthesamples
from the original dataset. We trained a single model using this training set and verified that its
performanceissimilartothatachievedbythesystemweareproposing(Figure19),whichcreates
andtrainsanewmodelwhenanewdriftoccurs.However,thissimplemodelisnotrealisticand
cannotbeappliedinreal-worldcontextsbecauseithastheadvantageofimmediatelyanalyzing
datasamplesfromtheentirehistoryofthestream.Itisnotrealisticbecausenomodelcan‘look’
into the future. The objective is only to test whether the detected changes are present in the
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

24:22 L.Caropreseetal.
Fig.19. Testperformanceonthedatasetwithamodeltrainedonasampleofdata.
originaldatasetorareonlyasideeffectofthemodeltraining.Breakingthechronologicalorderof
preferencescouldheavilyimpactdatasetevaluation:ForYoochooseandAmazonVideoGames,it
meanschangingtheorderwhenitems‘appear’inthesystem.FortheMINDdataset,thesideeffect
isbreakingthecorrelationbetweennews:asequenceofnewsonthesameeventlosesmeaning,
influencingtheperformanceevaluation.However,thisbehaviorcanbeacceptedconsideringthe
scope of this experiment. The architecture we propose, however, remains competitive with this
‘ideal’modelandmatchesitsperformance.
Inafurthersetofexperiments,weevaluatewhethertheapproacheffectivelysupportsactual
shifts in data distribution. In our approach, we only increase dimensionality when a drift is de-
tected. This means that if no increase in loss is detected, we do not modify the structure of the
current model. Conversely, any increase in the loss is identified as a structural inability of the
modeltoproperlycaptureuserpreferences,promptingustotrainanewmodelwithupdateddi-
mensionality.
Figure20(b)illustratesthetestlosstrendfortheYoochoosedatasetaftershufflingthedata.In
thiscase,thedatasetnolongerdemonstratesfeaturesthatdegrademodelperformance.Essentially,
themodelfailstoadapttonewitemsorpreferences.AsimilartrendisobservedwiththeAmazon
dataset.
Figure 20(a), where the focus is on the MIND dataset, presents a contrasting behavior: the
model’s performance worsens upon encountering new items. In this dataset, items typically fol-
lowaninherentperiodicityduetoevolvingtopicsovertime.Userstendtoreadnewsonthesame
topicwithinashorttimeframebeforemovingontothenextone.Shufflingexacerbatesthissce-
nario,leadingtheframeworktoadjustbyidentifyingagreaternumberofregimes.
5 EnablingFullGeneration
The rationale of the above analysis is that, by tracking a realistic data stream, it is possible to
devise a sequence of models that can be used to generate a synthetic data stream similar to an
originalone.Thecomparisonbetweentheoriginalstreamandthesyntheticstreamintheprevious
section allowed us to evaluate the fidelity level of the generator in sampling new data. Clearly,
thisframeworkallowstogeneratestreamswithanarbitrarynumberofregimes,inanarbitrary
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

ModellingConceptDriftinDynamicDataStreamsforRecommenderSystems 24:23
Fig.20. Testperformanceonthedatasetwithamodeltrainedonasampleofdata.
Fig.21. Summarystatisticsonchangesintheregimesdetected.ThefirstcolumnreferstotheMicrosoft
Newsdataset.Theothertwocolumnsreferto(originalandinverted)AmazonVideoGames.Thelastcolumn
referstotheYoochoosedataset.
order, and with an arbitrary number of samples. However, this generation can only rely on the
modelsextractedfromtheoriginaldatastream.Thisisclearlyalimitationsincewewouldliketo
generate new regimes that can also deviate from the extracted models. Better, we would like to
deviseageneralschemewherewecansynthesizethematricesassociatedwitheachregime,and
evenenablechangesofthesematricesalongtheshards.
InFigure21,wepresentstatisticalinsightsintothechangesobservedinthedatafromtheprevi-
ousexperiments.Thefirstrowprovidesinformationabouttheappearance/disappearanceofusers
and items across different regimes. It illustrates the dynamic nature of the dataset, where users
anditemscanappearorvanishovertime.
Thesecondrowfocusesonthefeaturevectorsassociatedwithusersanditemsandhowthey
evolve across the regimes. While a significant number of components remain stable, indicating
consistentuseranditemcharacteristics,certainusersundergosubstantialchangesintheirfeature
vectors.Thissuggestsshiftsintheirpreferencesorcharacteristicsovertime.
Additionally, Figures 5, 8, 13, and 14 display other noteworthy changes in the distributions.
Thesefiguresprovidevisualrepresentationsofthevariationsobservedinthegenerateddata,re-
flectingshiftsinuserpreferences,trends,orothersignificantmodifications.Thenumberofusers
isreportedinlog-scaleontheX-axis, whilethenumberofitemsisreportedinlog-scale onthe
Y-axis.
Ingeneral,thefollowingdriftdirectionscanbeidentified:
—Userscanundergochangesintheirtastes,leadingtoshiftsintheirpreferences.Thiscanbe
visualizedasarewiringofcertainusernodesinthefeaturegraphdiscussedinSection3.1.
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

24:24 L.Caropreseetal.
—Newtrendsmayemerge,influencinguserpreferences.Thisisdirectlylinkedtothestructure
ofthefeaturegraphandhownodes(representingusersanditems)areconnectedwithinit.
—Newuserscanjointhesystem,expressingtheirpreferencesandimpactingtheunderlying
preference distributions. Similarly, new items can be introduced, further altering the
distributionofavailableitems.
—Conversely, some users may leave the system or become inactive, and certain items may
becomeobsolete.Thesechangesresultinmodificationstotheunderlyingitemdistribution.
Byunderstandingandaddressingthesedriftdirections,wecaneffectivelycapturethedynamics
ofuserpreferences,trends,andtheevolutionoftheitemspace.
In Algorithm 1, we observed that the generation of new samples (using the generateSamples
procedure) depends on the P and Q matrices, as well as the user/item frequency distributions
q and r. Consequently, if we want to capture the described drifts in the generated preferences,
we need to modify these parameters accordingly. We can develop a versatile stream generator
inspiredbytheconceptofgeometricclosenessintheBPRmodel,whichcaneffortlesslyintegrate
theaforementioneddriftmodels.
Tobegin,wedefineasetofnearlyorthogonalgeneratingvectorsinK-dimensionalspace,de-
noted as g ,...,g (i.e., designed such that g · g ≈ 0, for i (cid:2) j). Conceptually, these vectors
1 h i j
represent clusters of users and items. In practice, we can generate feature vectors p for users
u
u (and q for itemsi) aligned with a specific generating vector g . These user and item feature
i s
vectorsarecreatedbyintroducingrandomvariationsalongtheK dimensionsbasedong .Togen-
s
eratepreferences,weutilizethegenerateSamplesfunction,whichincorporatesrandomuser/item
frequenciesqandr accordingly.
Consequently, the aforementioned drifts can be effectively modeled by making appropriate
adjustmentstothesefeaturevectors,asdescribedbelow.
Drifting users: To capture changes in user preferences, we can model the shift in tastes for
a user u with a feature vector p associated with the generating vector g . This shift can be
u s
represented as a movement towards a different generating vector g . Consequently, a new ver-
t
sion of the user’s feature vector p can be obtained by combining g and g through a linear
u s t
combination.
New trends: To incorporate new trends, we introduce changes in the latent dimension K.
(cid:10)
Each generating vector g is extended with additional dimensions, denoted as k . User and
s
item feature vectors are extended accordingly, and this extension affects their geometric
proximity.
Distributiondrifts: Toaccountforchangesinuseranditemdistributions,wecanintroducenew
usersanditemsbyassociatingthemwithageneratorvectorandgeneratingtheirrespectivefeature
vectors.Theoreticalfrequenciesinqcanbeassignedtothesenewusers/items.Alternatively,new
generating vectors g can be created, allowing for the association of new items/users and the
s
drift of existing items. User churns and item obsolescence can be modeled by annihilating their
respectivefrequenciesinqandr.
InAlgorithm 2,wepresentasamplegenerationschemethatsummarizestheaforementioned
conceptsusingasetofpoliciesforpreferencegeneration.Weidentifysixmainpolicies,andprovide
example implementations for some of these policies. They essentially introduce adjustments to
generatingvectors,featurematrices,orfrequencydistributions.Byutilizingthemodifiedfeature
matricesand/orfrequencydistributions,wecangeneratepreferencesfortheshardassociatedwith
eachpolicy.
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

ModellingConceptDriftinDynamicDataStreamsforRecommenderSystems 24:25
ALGORITHM2:StreamGenerator
Input: Numberhofclustergeneratingvectors;ClusterusersizeNsanditemsizeMs,for1≤s ≤h;Numbernofinitial
preferencestogenerate;AlistofT−1policiesspecifictodriftingregimesandpreferencestogenaratent
Output: PreferencemodelsM(1),...,M(T)andassociatedpreferencesR(1),...,R(T).
1
M(1),G=generateFeatureMatrices({N1,...,Nh },{M1,...,Mh })
2
R(1),q,r =generateSamples(M,n)
3 foreacht ∈{2,...,T}do
4
M(t)=M(t−1)
5 ifthet-thregimecontains’userdrift’withpercentageαthen
6
M(t),G=coalesceDrift(α,G,M(t))
7 end
8 ifthet-thregimecontains’newtrends’withdimensionkthen
9
M(t),G=directionDrift(α,G,M(t))
10 end
11 ifthet-thregimecontains’newusers’withdimensionkthen
12
M(t),q=updateP(a,G,M(t))
13 end
14 ifthet-thregimecontains’newitems’withdimensionkthen
15
M(t),r =updateQ(a,G,M(t))
16 end
17 ifthet-thregimecontains’userschurn’withpercentageαthen
18
q=churnDrift(α,q)
19 end
20 ifthet-thregimecontains’itemsexpire’withpercentageαthen
21 r =obsolescenceDrift(α,r)
22 end
23
R(t),q,r =generateSamples(M,nt,q,r)
24 end
25
FunctiongenerateFeatureMatrices({N1,...,Nh },{M1,...,Mh }):
26 SampleK >h
27 Generatehorthogonalvectorsg1,...,gh ∈RK
28 foreachs ∈{1,...,h}do
29 foreachu ∈{1,...,Ns }andi ∈{1,...,Ms }do Generatetworandomperturbationsofgsaspuandqi
30 end
31
returnM,{g1,...,gh }
32 FunctioncoalesceDrift(α,G,M):
33 Sampleα%usersfromU intoU(cid:10)
34 foreachu ∈U(cid:10)do
35 Letgsbethegeneratingvectorassociatedwithu.
36
Randomlysamplegtwitht(cid:2)sfromGandβ ∈[0,1]
37 gh+1 =βgs +(1−β)gt;Addgh+1toG
38 Generatearandomperturbationsofgtasp u (cid:10) andupdatepuasβps +(1−β)p u (cid:10)
39 end
40 returnM,G
41 FunctiondirectionDrift(k,G,M):
42 foreachs ∈{1,...,h}do
43 extendgswithknewrandomdimensions
44 foreachu ∈{1,...,Ns }andi ∈{1,...,Ms }do extendpuandqibyusingtherandomperturbationsfromthe
generatingvectors
45 end
46 returnM,G
47 FunctionupdateP(k,G,M):
48
SamplekgeneratingvectorswithreplacementfromGintoG(cid:10)
49
foreachg∈G(cid:10)do
50 Generatearandomperturbationofgaspuwhereuisanewuserassociatedwithg
51 SamplearandomZipffrequencyqu
52 end
53 returnM,q
54 FunctionobsolescenceDrift(α,r):
55 Sampleα%usersfromU intoU(cid:10)
56 foreachu ∈U(cid:10)do updaterubymultiplyingitwitharandomdecayw
57 returnM,q
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

24:26 L.Caropreseetal.
6 Conclusions
Inthisstudy,weintroducedatechniqueformodelinguser/itempreferencesandtheirevolution
overtimeusingadynamictripartitegraphrepresentation.Thisgraphisconstructedasasequence
ofMFmodelstrainedonthesourcedatastream,witheachmodelcapturingthepropertiesanddata
distributionofaspecificregime.Thetransitionfromonemodeltoanotheroccurswhenaconcept
driftisdetected.
We explored this concept in two main directions. Firstly, we utilized the learned sequence of
modelstogeneratesyntheticdatastreamsthatexhibitsimilarpropertiestotheoriginaldata.This
approachenablesthegenerationofrealisticsyntheticdatastreams,facilitatingthedevelopmentof
moreefficientandaccuraterecommendationsystems.Theexperimentalevaluationdemonstrated
theeffectivenessofourapproachingeneratingdatastreamsthataccuratelyreflectthedynamics
oftheunderlyingdatadistribution.
Buildingupontheinsightsfromthepreliminarystudy,wedevelopedamoregeneralapproach
capable of mapping specific drifting operations to changes in the underlying tripartite graphs.
These changes can be parameterized, allowing for controlled data generation strategies where
variousdriftingstrategiescanbeimplementedbymanipulatingthetripartitegraph.
Itisworthnotingthatourproposedapproachisbasedonaspecificpreferencemodelthatas-
sumesgeometricclosenessofusersanditemsinthelatentembeddingspaceasameasureofinter-
action.Asadirectionforfutureresearch,itwouldbeinterestingtoadapttheproposedschemeto
otherpreferencemodelingstrategiesthatdonotrelyongeometriccloseness.Forinstance,explor-
inghowthemodelcanbetunedtoworkwithMarkovianmodelswherepreferencesarecorrelated,
andpreviousinteractionscaninfluenceauser’sfuturepreferences.
Anotherfascinatingtopicisthestudyofstrategiesformanagingnewusersand/oritems.For
instance,anewtypeofnodecouldbeaddedtothegraph(Figure1)toaccountfornewentriesand
applytargetedstrategiestomodelthebehaviorofnewuserseffectively.Similarly,foritems,one
couldconsiderincorporatingbusinesslogic,suchasprioritizingnew,moreprofitableitems.Also,
thesestrategiescouldbeconsideredaviablesolutiontothecold-startproblemoftherecommender
system.
References
[1] CharuC.Aggarwal.2016.RecommenderSystems.Springer.
[2] MarieAl-Ghossein,TalelAbdessalem,andAnthonyBarré.2021.Asurveyonstream-basedrecommendersystems.
ACMComputingSurveys54,5,Article104(2021),1–36.
[3] ManuelBaena-García,JosédelCampo-Ávila,RaulFidalgo,AlbertBifet,RicardGavalda,andRafaelMorales-Bueno.
2006.Earlydriftdetectionmethod.InProceedingsofthe4thInternationalWorkshoponKnowledgeDiscoveryfromData
Streams.Citeseer,77–86.
[4] CigdemBakir.2018.Collaborativefilteringwithtemporaldynamicswithusingsingularvaluedecomposition.Tehnički
Vjesnik25,1(2018),130–135.
[5] NicolaBarbieri,GiuseppeManco,andEttoreRitacco.2014.ProbabilisticApproachestoRecommendations.Morganand
ClaypoolPublishers.
[6] FrancoisBelletti,KarthikLakshmanan,WalidKrichene,Yi-FanChen,andJohnAnderson.2019.Scalablerealisticrec-
ommendationdatasetsthroughfractalexpansions.arXiv:1901.08910.Retrievedfromhttps://arxiv.org/abs/1901.08910
[7] JamesBennett,CharlesElkan,BingLiu,PadhraicSmyth,andDomonkosTikk.2007.KDDcupandworkshop2007.
ACMSIGKDDExplorationsNewsletter9,2(2007),51–52.
[8] AlbertBifetandRicardGavalda.2007.Learningfromtime-changingdatawithadaptivewindowing.InProceedingsof
the2007SIAMInternationalConferenceonDataMining.SIAM,443–448.
[9] MaríadelCarmenRodríguez-Hernández,SergioIlarri,RamónHermoso,andRaquelTrillo-Lado.2017.DataGenCARS:
Ageneratorofsyntheticdatafortheevaluationofcontext-awarerecommendationsystems.PervasiveandMobile
Computing38(2017),516–541.
[10] JörgDrechslerandJeromeP.Reiter.2011.Anempiricalevaluationofeasilyimplemented,nonparametricmethodsfor
generatingsyntheticdatasets.ComputationalStatisticsandDataAnalysis55,12(2011),3232–3243.
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

ModellingConceptDriftinDynamicDataStreamsforRecommenderSystems 24:27
[11] EduardoFerreiraJosé,FabricioEnembreck,andJeanPaulBarddal.2020.ADADRIFT:Anadaptivelearningtechnique
forlong-historystream-basedrecommendersystems.InProceedingsofthe2020IEEEInternationalConferenceonSys-
tems,Man,andCybernetics(SMC’20).2593–2600.
[12] IsvaniFrías-Blanco,JosédelCampo-Ávila,GonzaloRamos-Jiménez,RafaelMorales-Bueno,AgustínOrtiz-Díaz,and
YailéCaballero-Mota.2015.Onlineandnon-parametricdriftdetectionmethodsbasedonhoeffding’sbounds.IEEE
TransactionsonKnowledgeandDataEngineering 27,3(2015),810–823.DOI: https://doi.org/10.1109/TKDE.2014.
2345382
[13] JoaoGama.2010.KnowledgeDiscoveryfromDataStreams.ChapmanandHall/CRC.
[14] JoaoGama,PedroMedas,GladysCastillo,andPedroRodrigues.2004.Learningwithdriftdetection.InProceedingsof
theBrazilianSymposiumonArtificialIntelligence.Springer,286–295.
[15] JoãoGama,IndreŽliobaite,AlbertBifet,MykolaPechenizkiy,andAbdelhamidBouchachia.2014.Asurveyonconcept
driftadaptation. ACMComputingSurveys46,4(2014),1–37.
[16] HeitorM.Gomes,AlbertBifet,JesseRead,JeanPaulBarddal,FabrícioEnembreck,BernhardPfharinger,GeoffHolmes,
andTalelAbdessalem.2017.Adaptiverandomforestsforevolvingdatastreamclassification.MachineLearning106,
9(2017),1469–1495.
[17] HeitorMuriloGomes,JesseRead,AlbertBifet,JeanPaulBarddal,andJoãoGama.2019.Machinelearningforstreaming
data:State-of-the-art,challenges,andopportunities.ACMSIGKDDExplorationsNewsletter21,2(2019),6–22.
[18] X.Han,C.Zhu,X.Hu,C.Qin,X.Zhao,andH.Zhu.2024.Adaptingjobrecommendationstouserpreferencedrift
withbehavioral-semanticfusionlearning.InProceedingsofthe30thACMSIGKDDConferenceonKnowledgeDiscovery
andDataMining.1004–1015.
[19] F.MaxwellHarperandJosephA.Konstan.2015.TheMovieLensdatasets:Historyandcontext.ACMTransactionson
InteractiveIntelligentSystems5,4(2015),1–19.
[20] MylesHollander,DouglasA.Wolfe,andEricChicken.2014.NonparametricStatisticalMethods.JohnWileyandSons.
[21] MartinJakomin,TomažCurk,andZoranBosnić.2018.Generatinginter-dependentdatastreamsforrecommender
systems.SimulationModellingPracticeandTheory88(2018),1–16.
[22] Wang-ChengKangandJulianMcAuley.2018.Self-attentivesequentialrecommendation.InProceedingsoftheIEEE
InternationalConferenceonDataMining.IEEE,197–206.
[23] AnastasiiaKlimashevskaia,DietmarJannach,MehdiElahi,andChristophTrattner.2024.Asurveyonpopularity
biasinrecommendersystems.UserModelUser-AdapInter 34(2024),1777–1834.https://doi.org/10.1007/s11257-024-
09406-0
[24] YehudaKoren.2009.Collaborativefilteringwithtemporaldynamics.InProceedingsofthe15thACMSIGKDDInterna-
tionalConferenceonKnowledgeDiscoveryandDataMining.447–456.
[25] LukaszKoryckiandBartoszKrawczyk.2019.Unsuperviseddriftdetectorensemblesfordatastreammining.InPro-
ceedingsofthe2019IEEEInternationalConferenceonDataScienceandAdvancedAnalytics(DSAA’19).317–325.
[26] JureLeskovec,AnandRajaraman,andJeffreyUllman.2020.MiningMassiveData.CambridgeUniversityPress.
[27] ElisabethLex,DominikKowald,andMarkusSchedl.2020.Modelingpopularityandtemporaldriftofmusicgenre
preferences.TransactionsoftheInternationalSocietyforMusicInformationRetrieval3,1(2020),17–30.
[28] JiachengLi,YujieWang,andJulianMcAuley.2020.Timeintervalawareself-attentionforsequentialrecommendation.
InProceedingsofthe13thInternationalConferenceonWebSearchandDataMining.322–330.
[29] PawelMatuszykandMyraSpiliopoulou.2017.Stream-basedsemi-supervisedlearningforrecommendersystems.
MachineLearning106,6(2017),771–798.
[30] PawelMatuszyk,JoãoVinagre,MyraSpiliopoulou,AlípioMárioJorge,andJoãoGama.2018.Forgettingtechniquesfor
stream-basedmatrixfactorizationinrecommendersystems.KnowledgeandInformationSystems55,2(2018),275–304.
[31] DiegoMonti,GiuseppeRizzo,andMaurizioMorisio.2019.Allyouneedisratings:Aclusteringapproachtosynthetic
ratingdatasetsgeneration.InProceedingsoftheREVEALWorkshopatACMRecSysConference.
[32] JianmoNi,JiachengLi,andJulianMcAuley.2019.Justifyingrecommendationsusingdistantly-labeledreviewsand
fine-grainedaspects.InProceedingsofthe2019ConferenceonEmpiricalMethodsinNaturalLanguageProcessingand
the9thInternationalJointConferenceonNaturalLanguageProcessing(EMNLP-IJCNLP’19).188–197.
[33] StanleyAdeOyewole.2021.ImageContent-basedUserPreferenceElicitationforPersonalisedMobileRecommendationof
ShoppingItems.Ph.D.Dissertation.DepartmentofInformationTechnology,FacultyofAccountingandInformatics,
DurbanUniversityofTechnologyDurban,SouthAfrica.
[34] S.Rendle,C.Freudenthaler,Z.Gantner,andL.Schmidt-Thieme.2009.BPR:Bayesianpersonalizedrankingfromim-
plicitfeedback.InProceedingsoftheConferenceonUncertaintyinArtificialIntelligence(UAI’09).452–461.
[35] FrancescoRicci,LiorRokach,andBrachaShapira(Eds.).2015.RecommenderSystemsHandbook(2nded.).Springer
PublishingCompany,Incorporated.
[36] RaquelSebastiãoandJoséMariaFernandes.2017.SupportingthePage-Hinkleytestwithempiricalmodedecompo-
sitionforchangedetection.InProceedingsoftheInternationalSymposiumonMethodologiesforIntelligentSystems.
Springer,492–498.
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.

24:28 L.Caropreseetal.
[37] ManelSlokom,MarthaLarson,andAlanHanjalic.2020.Partiallysyntheticdataforrecommendersystems:Prediction
performanceandpreferencehiding.arXiv:2008.03797.Retrievedfromhttps://arxiv.org/abs/2008.03797
[38] RicardoSousaandJoaoGama.2016.Firstprinciplemodelsbaseddatasetgenerationformulti-targetregressionand
multi-labelclassificationevaluation.InProceedingsoftheSTREAMEVOLV@ECML-PKDD.
[39] HuiminSun,JiajieXu,KaiZheng,PengpengZhao,PingfuChao,andXiaofangZhou.2021.MFNP:Ameta-optimized
modelforfew-shotnextPOIrecommendation.InProceedingsoftheIJCAI.3017–3023.
[40] TipajinThaipisutikul.2022.Anadaptivetemporal-conceptdriftmodelforsequentialrecommendation.ECTITransac-
tionsonComputerandInformationTechnology16,2(2022),222–236.
[41] KarenH.L.TsoandLarsSchmidt-Thieme.2006.Empiricalanalysisofattribute-awarerecommendersystemalgo-
rithmsusingsyntheticdata.J.Comput.1,4(2006),18–29.
[42] AlexeyTsymbal.2004.Theproblemofconceptdrift:Definitionsandrelatedwork.ComputerScienceDepartment,
TrinityCollegeDublin106,2(2004),58.
[43] BrunoVeloso,LucianoCaroprese,MatthiasKönig,SóniaTeixeira,GiuseppeManco,HolgerH.Hoos,andJoãoGama.
2021.Hyper-parameteroptimizationforlatentspaces.InProceedingsoftheECML/PKDD2021EuropeanConferenceon
MachineLearningandKnowledgeDiscoveryinDatabases(LectureNotesinComputerScience,Vol.12977).249–264.
[44] JoãoVinagre,AlípioMárioJorge,ConceiçãoRocha,andJoaoGama.2021.Statisticallyrobustevaluationofstream-
basedrecommendersystems.IEEETransactionsonKnowledgeandDataEngineering33,7(2021),2971–2982.
[45] JoãoVinagre,AlípioMárioJorge,andJoãoGama.2018.Onlinegradientboostingforincrementalrecommendersys-
tems.InProceedingsoftheDiscoveryScience.209–223.
[46] CharinyaWangwatcharakulandSartraWongthanavasu.2021.Anoveltemporalrecommendersystembasedonmulti-
pletransitionsinuserpreferencedriftandtopicreviewevolution.ExpertSystemswithApplications185(2021),115626.
[47] Geoffrey I. Webb, Loong Kuan Lee, François Petitjean, and Bart Goethals. 2017. Understanding concept drift.
arXiv:1704.00362.Retrievedfromhttps://arxiv.org/abs/1704.00362
[48] TaoruYang,YongGao,ZhouHuang,andYuLiu.2023.UPTDNet:Auserpreferencetransferanddriftnetworkfor
cross-citynextPOIrecommendation.InternationalJournalofIntelligentSystems2023,1(2023),9091570.
[49] ZhengyiYang,XiangnanHe,JizhiZhang,JiancanWu,XinXin,JiaweiChen,andXiangWang.2023.Agenericlearning
frameworkforsequentialrecommendationwithdistributionshifts.InProceedingsofthe46thInternationalACMSIGIR
ConferenceonResearchandDevelopmentinInformationRetrieval.
Received15December2022;revised30July2024;accepted17September2024
ACMTrans.Recomm.Syst.,Vol.3,No.2,Article24.Publicationdate:March2025.