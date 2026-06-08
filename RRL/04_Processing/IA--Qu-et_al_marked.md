Budgeted Embedding Table For Recommender Systems
YunkeQu TongChen
TheUniversityofQueensland TheUniversityofQueensland
Brisbane,Australia Brisbane,Australia
yunke.qu@uq.net.au tong.chen@uq.edu.au
QuocVietHungNguyen HongzhiYin∗
GriffithUniversity TheUniversityofQueensland
GoldCoast,Australia Brisbane,Australia
henry.nguyen@griffith.edu.au h.yin1@uq.edu.au
ABSTRACT KEYWORDS
Attheheartofcontemporaryrecommendersystems(RSs)arelatent recommendersystems,neuralarchitecturesearch
factormodelsthatprovidequalityrecommendationexperienceto
ACMReferenceFormat:
users.Thesemodelsuseembeddingvectors,whicharetypicallyofa
YunkeQu,TongChen,QuocVietHungNguyen,andHongzhiYin.2024.
uniformandfixedsize,torepresentusersanditems.Asthenumber
BudgetedEmbeddingTableForRecommenderSystems.InProceedingsofthe
ofusersanditemscontinuestogrow,thisdesignbecomesineffi- 17thACMInternationalConferenceonWebSearchandDataMining(WSDM
cientandhardtoscale.Recentlightweightembeddingmethods ’24),March4–8,2024,Merida,Mexico.ACM,NewYork,NY,USA,10pages.
haveenableddifferentusersanditemstohavediverseembedding https://doi.org/10.1145/3616855.3635778
sizes,butarecommonlysubjecttotwomajordrawbacks.Firstly,
1 INTRODUCTION
theylimittheembeddingsizesearchtooptimizingaheuristicbal-
ancingtherecommendationqualityandthememorycomplexity, Recommender systems (RSs) predict a user’s preference for an
wherethetrade-offcoefficientneedstobemanuallytunedforev- item according to observed user-item interactions [51, 61] and
erymemorybudgetrequested.Theimplicitlyenforcedmemory havebeenindispensableacrossnumerousmodernplatformssuch
complexitytermcanevenfailtocaptheparameterusage,mak- ase-commerceandsocialmedia[23,27,64].Incontextswhere
ingtheresultantembeddingtablefailtomeetthememorybudget computationsonlocaldevicesareessential,suchasfederatedrec-
strictly.Secondly,mostsolutions,especiallyreinforcementlearn- ommendation[39]andInternetofThings(IoT)services[16],the
ingbasedonesderiveandoptimizetheembeddingsizeforeach needforRSswithsmallmemoryfootprintsbecomescriticaldueto
eachuser/itemonaninstance-by-instancebasis,whichimpedesthe highlyconstrainedcomputationalresources.Themainbottleneck
searchefficiency.Inthispaper,weproposeBudgetedEmbedding fordownsizingRSsisoftentheembeddingtable,whichrepresents
Table(BET),anovelmethodthatgeneratestable-levelactions(i.e., usersanditemswithdistinctembeddingvectorstofacilitatepair-
embeddingsizesforallusersanditems)thatisguaranteedtomeet wisesimilaritycomputation.Assuch,thesizeoftheembedding
pre-specifiedmemorybudgets.Furthermore,byleveragingaset- tablecanquicklyexhausttheavailablememory,posingasignificant
basedactionformulationandengagingsetrepresentationlearning, challengetoachievingscalableandresource-friendlyRSs.
wepresentaninnovativeactionsearchstrategypoweredbyan Suchmemorybottleneckisattributedtoconventionalembed-
actionfitnesspredictorthatefficientlyevaluateseachtable-level dingtables,whichtypicallyallocatefixedanduniformembedding
action.Experimentshaveshownstate-of-the-artperformanceon sizestoeachuseranditem[8,18].Suchadesignmayrequirean
tworeal-worlddatasetswhenBETispairedwiththreepopular excessivenumberofparametersinindustry-scaleapplications,e.g.,
recommendermodelsunderdifferentmemorybudgets. thebenchmarkrecommenderin[11]hasmorethan25billionpa-
rametersinitsembeddingtableandrequires100GBmemory.Inthis
CCSCONCEPTS regard,researchershavedevelopedmethodstoachievelightweight
embeddingswhilemaintainingitsexpressiveness.Onestreamof
•Informationsystems→Recommendersystems.
methodsaimtopruneredundantparametersoftheembeddingtable.
Forexample,[37]proposedOptEmbed,anovelembeddingsparsifi-
∗Correspondingauthor cationframeworkthatprunesredundantembeddingsbylearningan
importancescoreforeachfeature.Thesemethodsmostlyoptimize
alossfunctioncombiningarecommendationtermandasparsity
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
regularizer.Apartfromsparsification/pruningmethods,another
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation line of works featuring reinforcement learning (RL) techniques
onthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthanthe havealsoemerged.ThosemethodsadoptanRL-basedpolicynet-
author(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,or
worktosearchfortheoptimalembeddingsizesforeachuser/item,
republish,topostonserversortoredistributetolists,requirespriorspecificpermission
and/orafee.Requestpermissionsfrompermissions@acm.org. wheretheembeddingsizes(i.e.,actions)canbeselectedfroman
WSDM’24,March4–8,2024,Merida,Mexico action space consisting of either a predefined set of values [? ]
©2024Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
oracontinuousrange[41].Similartosparsificationmethods,the
ACMISBN979-8-4007-0371-3/24/03...$15.00
https://doi.org/10.1145/3616855.3635778 rewardfunctionsinRL-basedlightweightembeddingapproaches
557

WSDM’24,March4–8,2024,Merida,Mexico YunkeQu,TongChen,QuocVietHungNguyen,&HongzhiYin
alsobindtherecommendationqualitytermwithamemorycom-
plexitypenalty.Bytuningatrade-offcoefficientamongthetwo
terms,theycanadjusttheregularizationstrengthontheparameter
consumption,thusachievingthedesiredmemoryefficiency.
Despitethepossibilityofbalancingperformanceandembed-
ding parameter size, these two types of methods are still away
frompracticalusefortworeasons.Firstly,suchadesiredbalance
isachievedbyjointlyoptimizinganadditionalspacecomplexity
constraintontopoftherecommendationobjective.Forexample,
in[18],thisisformulatedasthedifferencebetweenthebudgeted
embeddingparametersizeandtheactualparameterconsumption
Figure1:OverviewofBET.
ofthecompressedembeddingtable.However,suchanimplicitloss
termmeansthattheresultantembeddingtablemaynotnecessarily aset-basedformulationofactions,andembedseachactionwith
meetthedesiredparameterbudgeteverytime[8].Moreover,the DeepSets[59],wherethelearnedhigh-qualityactionembeddings
optimizationqualityishighlysensitivetothetrade-offcoefficient, canefficientlyprovidereliableperformancefeedbackoneachtable-
whichneedstobeheuristicallytunedforeachmemorybudget. levelaction.Furthermore,theset-basedactionrepresentationscan
Thesecondreasonisthat,toachieveoptimalrecommendation beinductivelylearned,whichisessentialforouriterativesearch
performanceundereachmemorybudget,theembeddingsizeis algorithmthatconstantlygeneratesunseenactionsthatneedtobe
decidedonaninstance-by-instancebasisw.r.t.eachuser/item.Tak- evaluated.
ingarecentRL-basedmethodCIESS[41]asanexample,apolicy Tosummarize,ourworkpresentsthecontributionsbelow:
networkpredictstheoptimalactionforeverysingleuseranditem, • Weidentifythepracticalitybottlenecksofexistingembed-
basedonwhichthebackboneRSistrainedandevaluatedtocal-
dingsizesearchmethodsforlightweightRSs,namelythe
culatethereward,enablingtrainingthepolicynetwork.Onthe
implicitandnon-scalableparametersizeconstraintsformeet-
onehand,ideally,thepolicynetworkisexpectedtobeiteratively
ingdifferentmemorybudgets,andtheinefficientembedding
updatedw.r.t.eachinstance(i.e.,user/item),butthiscanbeprohib-
sizegenerationandevaluationforeveryinstance.
itivelyinefficientgiventhelargenumberofusersanditems.On • WeproposeBET,anoveltable-levelembeddingsizesearch
theotherhand,performingonlyoneupdateperbatch/epochleads
approachfeaturinganefficientactionsamplingstrategythat
toslowerconvergenceduetotheaggregatednatureofthereward
generatestable-levelactionsforallusersanditemsanda
function,andmaypotentiallyresultininferiorgeneralization[20].
DeepSets-basedfitnesspredictionnetworkthataccurately
Inresponsetobothchallenges,weproposeBudgetedEmbedding
predictstheirperformancetoreduceactionevaluationcosts.
Table(BET)forRSs,anautomatedinputembeddingsizesearch • Extensiveempiricalcomparisonshavebeencarriedouton
paradigmthatcanefficientlygeneratesizedecisionsandperform
tworeal-worlddatasetsbypairingstate-of-the-artembed-
optimizationattheembeddingtablelevel.AnoverviewofBETis
dingsizesearchalgorithmswithvariousbackboneRSs,which
providedinFigure1.Toaddressthefirstchallenge,weinnovatively
confirmtheadvantageousefficacyofBET.
propose a bounded sampler that draws embedding sizes for all
users/itemsfromacollectionofprobabilisticdistributions,withthe
2 PRELIMINARIES
guaranteethatthetotalparameterusageiscapped.Astheembed-
dingsizesforallinstancesintheembeddingtableareproducedall Toprovideadetailedresearchbackground,weherebydiscussrele-
atonce,wetermthisatable-levelaction.Thisstrategyfreesusfrom vantresearchtopics.
theneedformanuallydesigningandtuningtheimplicitparameter
2.1 DeepRecommenderSystems
constraintinthereward/lossfunction,andallowsustoenforcethe
memorybudgetwithanegligiblecost. Researchers have proposed numerous deep recommender mod-
Totacklethesecondchallenge,wefurtherpairthegenerated elstocapturetheuser-itemrelationships.Thefirstlineofdeep
table-levelactionswithafitnesspredictionnetworktoevaluatethe recommendersystemsarebasedonMLPs.Forinstance,Neural
qualityofthoseactions.Essentially,ineachsearchiteration,after CollaborativeFiltering(NCF)[15]integratesaMLPwithamatrix
samplingseveraltable-levelactions,weneedtoidentifytheones factorizationcomponenttolearnthetwo-wayinteractionsbetween
thatpromisehighrecommendationaccuracy.Astraightforward usersanditems.AutoRec[45]usesanautoencodertomodelthe
solutionistogreedilyevaluateeachcandidateactionbytraining user-iteminteractionsinalow-dimensionalhiddenspaceandper-
and evaluating a backbone RS from scratch with the suggested formcollaborativefiltering.Linetal.proposedanovelsequential
embeddingsizes[18,41,62?],whichapparentlyimpedesefficiency. recommender system, Dual Contrastive Network [31] that gen-
Onemaythinkofasurrogatefunction[3,8]that“predicts”the eratesself-supervisedsignalsbyconsideringbothuseranditem
fitnessofeachaction,insteadofexplicitlyevaluatingit.Accurately perspectivesandrefiningrepresentationlearningthroughdualrep-
predictingtheperformanceofthetable-levelactionsiscrucialyet resentationcontrastivelearning.InadditiontoMLP-basedmeth-
anothermajorchallengeinthisregard,aseitheroverestimatingor ods,graph-basedarchitectures[14,53,58]havealsobeenstudied.
underestimatinganaction’sperformancewilleventuallycausesub- Forexample,NeuralGraphCollaborativeFiltering(NGCF)[53]
optimalembeddingsizedecisions.Toalignwiththeevaluationof extendstraditionalneuralcollaborativefilteringbymodelinguser-
table-levelactionsinBET,ourfitnesspredictorinnovativelyutilizes iteminteractionswithgraphconvolutionnetworks.LightGCN[14]
558

BudgetedEmbeddingTableForRecommenderSystems WSDM’24,March4–8,2024,Merida,Mexico
takesinspirationfromNGCFandsimplifiesitbyremovingitsself- oritemIDstoareal-valuedembeddingvectore𝑛,where𝑛∈U∪V
indexeseitherauseroranitem.Notethatweonlyseparatelyuse𝑢
connection,featuretransformationandlinearactivationoperations.
and𝑣toindexusersanditemswhentheyneedtobedistinguished,
Anotherlineofrecommendersystemsarebasedonfactorization
machines.FactorizationMachines(FM)combinelinearregression e.g.,whenperformingpairwiseranking.Theverticalconcatena-
withmatrixfactorizationtechniquestohandlehigh-orderinterac- tionofallembeddingvectorsformstheembeddingtableEofsize
tions[42].[2]wasalsocreatedtominehigher-orderinteractions. (|U|+|V|)×𝑑 𝑚𝑎𝑥,where𝑑 isthemaximum/fullembedding
𝑚𝑎𝑥
|                   |        |             |                   | sizesupportedby𝐺 | Θ(·).Theembeddingsizesareadjustedviaabi- |     |     |     |
| ----------------- | ------ | ----------- | ----------------- | ---------------- | ---------------------------------------- | --- | --- | --- |
| Its deep variants | - QNFM | [7], DeepFM | [13] and xLightFM | [17]             |                                          |     |     |     |
narymaskM∈{0,1}(|U|+|V|)×𝑑𝑚𝑎𝑥,whichiscommonlyadopted
havebeenproposedtoo.Moreover,numerousmethodshavebeen
proposedtoleverageheterogeneousdataforrecommendation.For forembeddingsparsificationinlightweightrecommendersystems
instance,[6,12,25]havebeendevisedtoextractinformationfrom [35,37,41].Eachrowm𝑛inMisamaskvectorcorrespondingto
userreviewsorhashtags.[24,52]havebeenproposedtoexploit user/item𝑛.Givenasearchedembeddingsize𝑑 𝑛,wesetthefirst
videosandimagesforrecommendation.Locationinformationhas 𝑑 𝑛elementsofm𝑛toonestheremaining𝑑 −𝑑
𝑚𝑎𝑥 𝑛dimensionsto
alsobeenutilizedtoassistlocation-awarerecommendations[4]. zeros.Then,weperformelement-wisemultiplicationoftheembed-
dingtableEandthebinarymaskmatrixMtoadjusttheembedding
2.2 LightweightEmbeddingsFor sizesduringembeddinglook-up,i.e.,e𝑛 = (E⊙M)[𝑛]where[𝑛]
Recommenders retrievesthe𝑛-throwofamatrix.Misadaptivelyupdatedbased
Variousclassesofworkshaveinvestigatedlearningcompressed onthesampledactionsineveryiteration.Itisworthnotingthat,
inthedeploymentstage,onlytheheavilysparsifiedembedding
embeddingstoprovidealow-memoryalternativetotraditional
|                  |                |         |                     | tableE𝑠𝑝𝑎𝑟𝑠𝑒 | = E⊙Mwillbestored,wherethecostofstoring |     |     |     |
| ---------------- | -------------- | ------- | ------------------- | ------------ | --------------------------------------- | --- | --- | --- |
| embedding tables | in recommender | systems | [63]. For examples, |              |                                         |     |     |     |
zero-valuedentriescanbenegligiblewithsparsematrixstorage
featureselectionsearchmethods[32,36,54]aretrainedtolearn
techniques[44,49].Onceweobtainthesparseembeddingvectors,
importancescores,basedonwhichtheyfilterouttheunimportant
|     |     |     |     | therecommendermodel𝐺 |     | Φ(·) computesapreferencescore𝑦ˆ𝑢𝑣 |     |     |
| --- | --- | --- | --- | -------------------- | --- | --------------------------------- | --- | --- |
featurefields.Embeddingdimensionsearchapproaches[22,34,35,
representingpairwiseuser-itemsimilarity:
40,41,62]improvetraditionalrecommendersystemswithfixedand
|     |     |     |     |     | 𝑦ˆ𝑢𝑣 =𝐺 | ,e𝑣), 𝑢 | ∈U,𝑣 ∈V, |     |
| --- | --- | --- | --- | --- | ------- | ------- | -------- | --- |
uniformsizesbyintroducingmixeddimensionsforeachfeature. Θ(e𝑢 (1)
Quantization-basedmethods[5,9,10,19,21,26]reducesthepreci-
|     |     |     |     | where𝐺 | Θ(·)canbeanylatentfactor-basedrecommendermodel |     |     |     |
| --- | --- | --- | --- | ------ | ---------------------------------------------- | --- | --- | --- |
sionofnumericalvaluesandstoretheparameterswithlowerbits.
thatsupportspairwisescoring.
Featurehashingapproaches[1,11,28,30,33,46,47,57,60]utilize
Foroptimizingtherecommender,weadoptBayesianPersonal-
varioushashtrickstotransforminputvaluestoasmallerrange,
izedRanking(BPR)loss[43]:
thuscompressiontheembeddingtable.Knowledgedistillationtech-
∑︁
niquestrainasmallerstudentmodelfromalargerteachermodel L𝐵𝑃𝑅 = −ln𝜎(𝑦ˆ𝑢𝑣−𝑦ˆ𝑢𝑣′)+𝜂∥Θ∥2 , (2)
2
andhavebeenusedtolearnanembeddingtableofsmallersizes (𝑢,𝑣,𝑣′)∈D𝑡𝑟𝑎𝑖𝑛
fromlargerones[55,56].BETachievesdynamicembeddingsizes
|     |     |     |     | where | (𝑢,𝑣,𝑣′) ∈ D𝑡𝑟𝑎𝑖𝑛 | representsthetrainingsampleswhere |     |     |
| --- | --- | --- | --- | ----- | ----------------- | --------------------------------- | --- | --- |
andaimstofindtheoptimalembeddingsizeforeachfeature,soit
|     |     |     |     | user𝑢choosesitem𝑣overitem𝑣′,while𝑦ˆ𝑢𝑣 |     |     | and𝑦ˆ𝑢𝑣′ | respectively |
| --- | --- | --- | --- | ------------------------------------- | --- | --- | -------- | ------------ |
shouldbeclassifiedasaembeddingdimensionsearchapproach. representthepredictedpreferencesthatuser𝑢hasonitems𝑣and
𝑣′.𝜂∥Θ∥2
|                    |     |     |     |     | provides regularization | to  | prevent overfitting, | with a |
| ------------------ | --- | --- | --- | --- | ----------------------- | --- | -------------------- | ------ |
| 3 PROPOSEDAPPROACH |     |     |     |     | 2                       |     |                      |        |
scalingfactor𝜂.Ourgoalistosearchfortheoptimalembedding
Inanutshell,BEThasthreecomponents:(1)apre-trainedbackbone sizesforallusersanditemsunderstrictmemorybudgets,hence
recommenderwithafull-sizeembeddingtable𝐺 Θ(·)parameterized theoverallobjectiveisdefinedasfollows:
| byΘ;(2)anactionfitnesspredictionnetwork𝐹 |     |     | Φ(·)parameterized |     |     |     |        |     |
| ---------------------------------------- | --- | --- | ----------------- | --- | --- | --- | ------ | --- |
|                                          |     |     |                   |     |     | ∥   | M ∥ ,1 |     |
byΦ;and(3)anon-parametricactionsampler𝐻(·).Figure1pro- nL𝐵𝑃𝑅 s.t.1− 1 ≤𝑐,
|     |     |     |     |     | m i  |       | ×𝑑          | (3) |
| --- | --- | --- | --- | --- | ---- | ----- | ----------- | --- |
|     |     |     |     |     | Θ, Φ | (|U|+ | | V | ) 𝑚𝑎𝑥 |     |
videsanoverviewoftheworkflowofBET.Underpre-specified
memorybudgets,𝐻(·)samplesactionsfromasetofprobabilistic
|     |     |     |     | where∥M∥                        | 1,1countsthenumberofones,orequivalentlyretained |     |                        |     |
| --- | --- | --- | --- | ------------------------------- | ----------------------------------------------- | --- | ---------------------- | --- |
|     |     |     |     | parametersinthebinarymask,𝑐(0<𝑐 |                                                 |     | <1)isthetargetsparsity |     |
distributionsineachiteration.Eachactionspecifiestheembedding
sizesforallusersanditems.Afterwards,𝐹 Φ(·)estimatesthefitness rate,i.e.,theratiobetweenthenumbersofactiveparametersin
ofeachactionandselectsthebestactionpredicted.𝐺 Θ(·)isfurther sparsifiedandfullembeddingtables.
finetunedbyadoptingtheembeddingsizesinthechosenaction,
|     |     |     |     | 3.2 | Budget-AwareActionSampling |     |     |     |
| --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- |
andisthenisevaluatedonahold-outdatasettoobtaintheactual
fitnessscore(i.e.,recommendationquality)oftheaction.Thisfacil- Herebyweintroduceanoveltable-levelactionsamplingstrategy.In
| itatestheoptimizationof𝐹 |     | Φ(·)byminimizingitspredictionerror, |     |     |     |     |     |     |
| ------------------------ | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- |
eachsearchiteration,werandomlysampleasetofcandidateactions
| thusleadingustooptimalactionsundereachgivenmemorybudget |     |     |     | Q={𝑎 | ,...,𝑎 |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | ---- | ------ | --- | --- | --- |
1 𝑚}.Eachactionassignsacontinuousembeddingsize
| 𝑇   |     |     |     | 𝑑   | N + | 𝑛   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
a f t e r it e r a ti on s. In t h e r e mainderofthissection,weunfoldthe 𝑛 ∈ t o e v e r y u s e r or i t em ∈ U ∪ V .
≤ 𝑑𝑚 𝑎 𝑥
d e s i g no f e a c h co m po n e n t . A s w e ai m t o a v o i d o p t im iz i n gt he s ele cte d actiontowardsan
implicit,manuallytunedmemorycostterm,weproposetodirectly
3.1 RecommenderwithEmbeddingMasking
drawatable-levelactionthat:(1)makesallgeneratedembedding
LetUandVdenoteasetofusers𝑢anditems𝑣,respectively.The sizes conditioned on a certain distribution; and (2) ensures the
embeddingtableintherecommendermapseachinteger-valueduser totalparametersizeofallembeddingsiscappedatthebudgeted
559

WSDM’24,March4–8,2024,Merida,Mexico YunkeQu,TongChen,QuocVietHungNguyen,&HongzhiYin
parameterconsumption.Inshort,(1)essentiallynarrowstheaction
spacetomitigatethedifficultyofsearchingfromahugecollection
ofcompletelyrandomactions,while(2)guaranteesthatthetable-
levelactionstrictlymeetsthememorybudgetinthefirstplace.
Togenerateanaction𝑎,wefirstdeterminetwoprobabilitydistri-
| butions𝑃 | Uand𝑃 | Vrespectivelyforusersanditems.Meanwhile,to |     |     |     |     |     |     |
| -------- | ----- | ------------------------------------------ | --- | --- | --- | --- | --- | --- |
introduceinductivebiastotheactionsampler,insteadofresorting Figure2:Exampleofourset-basedactionformulation.Sup-
| toafixeddistributionthroughoutthesearchprocess,𝑃 |     |     |     |     |     | and𝑃 |                                         |             |
| ------------------------------------------------ | --- | --- | --- | --- | --- | ---- | --------------------------------------- | ----------- |
|                                                  |     |     |     |     | U   | V    | posewehavethreelegitimateembeddingsizes | {16,32,64}, |
arebothrandomlychosenfromasetofcandidatedistributions four users (red) and two items (green). Then, size 16 is a
withon-the-flyparameterization.Specifically,weutilizeapower setcontaininguser1,user2anditem4,whichmeanstheir
lawdistribution,atruncatedexponentialdistribution,atruncated
embeddingsizesare16.Similarly,theactionspecifiesthe
normaldistributionandalognormaldistribution.Forsimplicity,
embeddingsizesofuser3anditem5tobe32.Size64isnot
weletthetwoselecteddistributionsrespectivelybeparameterized usedbyanyusers/items.
by𝛽 Uand𝛽
V.Ineachiteration,theparametersarealldetermined
uniformlyatrandom:
|     |     | 𝛽 ,𝛽 | ∼Uniform(0,𝛽 | 𝑚𝑎𝑥), |     | (4) |     |     |
| --- | --- | ---- | ------------ | ----- | --- | --- | --- | --- |
U V
| where𝛽 | 𝑚𝑎𝑥 | isthemaximalvalueallowed.Notably,theembedding |     |     |     |     |     |     |
| ------ | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
sizesofeachfield(i.e.,usersanditems)arederivedbyindependently
| samplingfromtwodistributions𝑃 |     |     |     | and𝑃 V.Thisisbecauseeach |     |     |     |     |
| ----------------------------- | --- | --- | --- | ------------------------ | --- | --- | --- | --- |
U
fieldmayhavedistinctproperties[37]anddifferentdistributions
areneededtomodeltheembeddingsizesofusersanditems.
Afterthedistributionsaredetermined,wesample|U|and|V|
| probabilitiesrespectivelyfrom𝑃 |     |     | and𝑃 | V.Thesetofprobabilities |     |     |     |     |
| ------------------------------ | --- | --- | ---- | ----------------------- | --- | --- | --- | --- |
U
| arerespectivelydenotedas{𝑝 |     |        | | U |             | ∼𝑃 and{𝑝      | | V | ∼𝑃 |      |     |     |
| -------------------------- | --- | ------ | ----------------- | ------------- | -------- | ---- | --- | --- |
|                            |     |        | 𝑖} 𝑖              | U             | 𝑗} 𝑗     | V.We |     |     |
|                            |     |        | = 1               |               | =1       |      |     |     |
| thennormalizeall𝑝          |     | 𝑖 and𝑝 | 𝑗 asthefollowing: |               |          |      |     |     |
|                            |     |        | 𝑝 𝑖               | 𝑝 𝑗           |          |      |     |     |
|                            |     | 𝑝˜𝑖 =  | , 𝑝˜𝑗             | =             | ,        | (5)  |     |     |
|                            |     |        | (cid:205)|U|𝑝     | (cid:205)|V|𝑝 |          |      |     |     |
|                            |     |        | 𝑖                 |               | 𝑗        |      |     |     |
|                            |     |        | 𝑖                 | 𝑗             |          |      |     |     |
where𝑝˜𝑖/𝑝˜𝑗 Figure3:OverviewoftheDeepSets-basedfitnesspredictor.
indicatesthefractionofparameterseachuser/itemre-
ceivesamongallusers/items.Next,weobtaintheactualembedding
sizesbyapplyingthefractiononthememorybudget: convergenceandselecttheactionthatyieldsthebestfinalrecom-
mendationqualityonthevalidationset.However,thisapproach
|     | 𝑑 = | ⌊𝑝˜𝑖 ·𝑤·𝑑 | ·(|U|+|V|)⌋, | 𝑖   | =1,2,···,|U|, |     |     |     |
| --- | --- | --------- | ------------ | --- | ------------- | --- | --- | --- |
𝑖 𝑚𝑎𝑥 facesinevitablecomputationalburdensgiventhe𝑚trainingand
(6)
| 𝑑   | 𝑗 = ⌊𝑝˜𝑗 ·(1−𝑤)·𝑑 |     | 𝑚𝑎𝑥 ·(|U|+|V|)⌋, | 𝑗   | =1,2,···,|V|, |     |     |     |
| --- | ----------------- | --- | ---------------- | --- | ------------- | --- | --- | --- |
evaluationprocessesneededpersearchiteration.
where𝑤 InBET,weutilizeanactionfitnesspredictor,whichinductively
controlstheproportionofparametersallocatedtothe
learnsdistinctembeddingsofactionsandpredictsitsfitnessscore
| users.Inpractice,𝑤 |     | canbeempiricallydefined,suchasaneven |     |     |     |     |     |     |
| ------------------ | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- |
(i.e.,recommendationquality)basedontheactionembeddings.As
| split(i.e.,0.5).InBET,𝑤 |     |     | issampledfromauniformdistribution |     |     |     |     |     |
| ----------------------- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- |
discussedearlier,learningexpressiverepresentationsofdifferent
| eachtimeatable-levelactionisgenerated,i.e.,𝑤 |     |     |     |     | ∼Uniform(0,1), |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | -------------- | --- | --- | --- |
actionsisacrucialyetnon-trivialtaskforeffectivefitnesspredic-
soastoprobemoreembeddingsizeallocationstrategiesinthe
tion,especiallyconsideringtheneedforinductivelycomposing
iterativesearchprocess.
embeddingsforunseenactionsineverynewsearchiteration.
With|U|+|V|embeddingsizesderived,wenowallocatethem
Thus,weproposeanovelactionfitnesspredictionnetworkbased
toeachuseranditem.Previousstudies[37,48,62]haveshownthat
onthenotionofsetrepresentationlearning[50,59].Beforedelving
morefrequentusersanditemstendtobemoreinformativethan
long-tailones,hencegenerallybenefitfromalargerembedding intothefitnesspredictionnetwork,wefirstdetailtheset-based
formulationofeachaction.Eachactionisregardedasacollection
dimensionwhichallowsmoreinformationtobeencoded.Therefore, 𝑑
weranktheusersbytheirfrequencyandallocatethe𝑛-thlargest ofsets𝑎={S𝑑} 𝑚 𝑎𝑥,whereeachsetS𝑑 ={𝑛|∀𝑛∈U∪V,𝑑 𝑛 =𝑑}
𝑑 =1
|     |     |     |     |     |     |     | storestheusersanditemsthatusetheembeddingsize𝑑 | ∈ [1,𝑑 𝑚𝑎𝑥]. |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------- | ------------ |
userembeddingsizetothe𝑛-thfrequentuser.Similarly,weassign
∅ifthereisnouseroritemassignedtoembeddingsize𝑑.
| embeddingsizestoitemsbasedontheirfrequency.Assuch,weare |     |     |     |     |     |     | S𝑑 = |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | --- |
capableofsampling𝑚randomtable-levelactionsineachsearch Atoyexamplewithisgiveninfigure2.Assuch,thisallowsusto
buildourfitnesspredictoruponDeepSets[59]owingtoitsability
iterationtofacilitatethesubsequentsteps.
tolearnpermutation-variantrepresentationsofsets.
3.3 FitnessPredictionNetwork
Thefitnesspredictionnetworkconsistsoffourcomponents:a
Ineachiteration𝑡 wesampleasetof𝑚actions,denotedasQ𝑡.To userencoder𝜌 (·),anitemencoder𝜌
U V (·),anembeddingsize
selecttheoptimalactionfromQ𝑡,astraightforwardapproachisto encoder𝜇(·),andadecoder𝜋(·),allofwhichbearadistinctMLP.
paireachsampledactionwithafreshrecommender,trainituntil Encoders𝜌 (·)/𝜌 (·)takesomecontextualinformationabouta
U V
560

BudgetedEmbeddingTableForRecommenderSystems WSDM’24,March4–8,2024,Merida,Mexico
user/item,andproducetheircorrespondingrepresentations.Previ- Algorithm1EmbeddingSizeSearchwithBET
ousstudies[41,62]havedemonstratedthesuitabilityofusers’/items’ 1: InitializeΘandΦ,setA←∅;
popularityandcurrentembeddingsizesasthecontextinformation Train𝐺 Θ(·)tillconvergencew.r.t.Eq.2;
2:
forembeddingsizesearch.Weinheritthisdesignbyestablishinga for𝑡 =1,···,𝑇 do
3:
hierarchical,set-compatibleactionrepresentationlearningscheme.
4: Drawdistributionsandtheirparametersw.r.t.Eq.4;
Specifically,𝜌 (·)and𝜌 (·)respectivelytakestheuseranditem Draw𝑚actionsQ𝑡 ={𝑎 ,...,𝑎
|     | U   | V   |     |     |     |     | 5:  |     |     | 1 𝑚}withEq.5andEq.6; |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- |
frequenciestogeneratefrequency-weightedembeddings: 6: if0≤𝑡 mod5≤2then
|            |         |               | 𝑓      |          |           |      |     |         | 𝑎 𝑡 ←StrategyI;       |        |     |     |     |
| ---------- | ------- | ------------- | ------ | -------- | --------- | ---- | --- | ------- | --------------------- | ------ | --- | --- | --- |
|            |         | =𝜌            | 𝑢      | ), 𝑢 ∈U, |           |      | 7:  |         |                       |        |     |     |     |
|            | 𝒒𝑢      | U (           |        |          |           |      |     | elseif𝑡 | mod5=3then            |        |     |     |     |
|            |         | max𝑢′∈U       | 𝑓      | 𝑢′       |           |      | 8:  |         |                       |        |     |     |     |
|            |         |               |        |          |           | (7)  |     |         | 𝑎 ←StrategyII;        |        |     |     |     |
|            |         |               | 𝑓      |          |           |      | 9:  |         | 𝑡                     |        |     |     |     |
|            |         | =𝜌            | 𝑣      | ), 𝑣 ∈V, |           |      |     |         | 𝑡                     |        |     |     |     |
|            | 𝒒𝑣      | V (           |        |          |           |      | 1 0 | : else  | if m o d 5 = 4        | t h en |     |     |     |
|            |         | max𝑣′∈V       | 𝑓      | 𝑣′       |           |      |     |         |                       |        |     |     |     |
|            |         |               |        |          |           |      | 1 1 | :       | 𝑎 𝑡 ← S tr at eg y II | I ;    |     |     |     |
| where each | 𝑓 𝑢/𝑓 𝑣 | is normalized | by the | maximum  | user/item | fre- |     | endif   |                       |        |     |     |     |
12:
| quencyobserved. |     |     |     |     |     |     |     | FinetuneΘw.r.t.E⊙M𝑎𝑡 |     | andEq.2 |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ------- | --- | --- | --- |
13:
| Asmentionedabove,withinanaction𝑎,eachsetS𝑑 |     |     |     |     |     | contains |     | 𝑟   | ←Eq.13 |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | -------- | --- | --- | ------ | --- | --- | --- | --- |
|                                            |     |     |     |     |     |          | 14: | 𝑎𝑡  |        |     |     |     |     |
allusersanditemswithembeddingsize𝑑.Toobtainembedding𝒔𝑑 A←A∪(𝑎 ,𝑟
|     |     |     |     |     |     |     | 15: |     | 𝑡 𝑎𝑡 ); |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
ofsetS𝑑,wefirstlyfusetherepresentationsofallinvolvedusers 16: for𝑗 =1,···,𝑁 do
anditemsusingmeanaggregation,andthenappendtheexplicit 17: Randomlysample(𝑎 𝑗 ,𝑟 𝑎𝑗 )fromA;
| embeddingsizeinformation: |     |     |     |     |     |     |     |     | 𝑟ˆ𝑎𝑗 ←Eq.10; |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- |
18:
UpdateΦw.r.t.Eq.11;
|     |     | (cid:16)(cid:104) 1 | ∑︁   | 𝑑 (cid:105)(cid:17) |     |     | 19: |                                              |     |     |     |     |     |
| --- | --- | ------------------- | ---- | ------------------- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- |
|     |     | =𝜇                  |      |                     | ,   |     |     |                                              |     |     |     |     |     |
|     | 𝒔𝑑  |                     | 𝒒𝑛;  | 𝑑                   |     | (8) | 20: | endfor                                       |     |     |     |     |     |
|     |     | |S𝑑|                |      | 𝑚𝑎𝑥                 |     |     |     |                                              |     |     |     |     |     |
|     |     |                     | 𝑛∈S𝑑 |                     |     |     | 21: | endfor                                       |     |     |     |     |     |
|     |     |                     |      |                     |     |     | 22: | Performselectiveretrainingandobtain𝑎∗←Eq.14. |     |     |     |     |     |
where[;]representsconcatenation.Withtherepresentationsgen-
| eratedforall𝑑 | 𝑚𝑎𝑥 | sets,wederivetheembeddingfortheentire |     |     |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
action𝑎byfurthermergingallsetrepresentations:
|     |     |     |         |     |     |     | whereeval(·)evaluatestherecommendationquality,D𝑣𝑎𝑙 |     |                                        |     |     |     | isthe |
| --- | --- | --- | ------- | --- | --- | --- | -------------------------------------------------- | --- | -------------------------------------- | --- | --- | --- | ----- |
|     |     |     | 𝑑       |     |     |     |                                                    |     | isthebinarymaskcorrespondingtoaction𝑎, |     |     |     |       |
|     |     |     | 1 ∑︁𝑚𝑎𝑥 |     |     |     | validationset,M𝑎                                   |     |                                        |     |     |     |       |
|     |     | =   |         | ,   |     |     |                                                    |     |                                        |     |     |     |       |
𝒉𝑎 𝑑 𝒔𝑑 (9) andthedenominatoristherecommendationqualityofthepre-
𝑚𝑎𝑥
𝑑=1 trained backbone recommender𝐺 Θ(·) with the full embedding
|              |                                        |     |     |     |     |     | table.Hence,𝑟 |     | 𝑎 canbeinterpretedastheratiobetweenthetwo |     |     |     |     |
| ------------ | -------------------------------------- | --- | --- | --- | --- | --- | ------------- | --- | ----------------------------------------- | --- | --- | --- | --- |
| whereweuse𝒉𝑎 | todenoteanactionembedding.Anadditional |     |     |     |     |     |               |     |                                           |     |     |     |     |
recommendationaccuracyobtainedbythesparsifiedembeddings
benefitfromtheset-basedactionembeddingsisthat,wheneverthe
andthefullembeddings.Theimplementationofeval(·)canfollow
actionsamplerdrawsanyactionthatisnewtothefitnesspredictor
mostcommonlyusedrecommendationmetricslikeRecall@𝑘and
(whichiscommonlythecaseinembeddingsizesearch),itallows
NDCG@𝑘
forgeneratingtheactionembeddinginaninductivefashionwith [14,43],whereweadoptanensembleofbothmetrics
underdifferentvaluesof𝑘:
theavailablecontextinformationandtheupdatedsetformulation.
Witheachactionembedding𝒉𝑎,thedecoder𝜋(·)takes𝒉𝑎and ∑︁ (cid:205) 𝑘∈KRecall@𝑘 𝑢+NDCG@𝑘
|     |     |     |     |     |     |     | eval(E⊙M|D𝑣𝑎𝑙)= |     |     |     |     |     | 𝑢 , |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
(13)
| outputs𝑟ˆ𝑎,whichisthepredictedfitnessscoreofaction𝑎: |     |     |     |     |     |     |     |     |     |     | 2|K||U| |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- |
𝑢∈U
𝑟ˆ𝑎 =𝜋(𝒉𝑎). (10) wherewethechoicesof𝑘coverK ={5,10,20}inourpaper.
Thegroundtruthsamplescanbethusgeneratedbygathering
Wewilldetailhowtheentirefitnesspredictionnetwork𝐹
Φ(·)is
differentaction-fitnesspairs.Insteadofconstructingapoolofsuch
optimizedalongwiththesearchprocessinthenextsection. trainingsamplesandtrain𝐹
Φ(·)upfront,weincrementallyaddone
|     |     |     |     |     |     |     | trainingsampleineverysearchiteration𝑡 |     |     |     | tooptimize𝐹 |     | Φ(·) on |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | ----------- | --- | ------- |
3.4 FitnessPredictorTraining
thego.Thetrainingsampleisconstructedbyfirstlyidentifying
Thoughbearingarelativelysimplestructure,thefitnesspredictor apromisingactionfrom Q𝑡,denotedby𝑎 𝑡,andthenobtaining
still needs to be trained with some ground truth samples. The 𝑟 byevaluating𝑎 onthefinetuned𝐺 Θ(·).Comparedwithmost
|                           |     |     |                                |     |     |     | 𝑎𝑡  |     | 𝑡   |     |     |     |     |
| ------------------------- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fitnesspredictionnetwork𝐹 |     |     | Φ(·)isoptimizedbyminimizingthe |     |     |     |     |     |     |     |     |     |     |
RL-basedembeddingsizesearchmethods,therequirednumberof
meansquarederrorbetweenthepredictedfitnessscore𝑟ˆ𝑎andthe
fitnessevaluationwiththerecommendationmodelwillbereduced
actualone𝑟
𝑎withgradientdescent: from𝑚×𝑇 tomerely𝑇,where𝑇 isthetotalnumberofiterations
|          | ∑︁  |                       |     | ∑︁  |             |     | aswellasthegroundtruthsamplesforoptimizing𝐹 |     |     |     |     | Φ(·). |     |
| -------- | --- | --------------------- | --- | --- | ----------- | --- | ------------------------------------------- | --- | --- | --- | --- | ----- | --- |
| Φ=argmin |     | (𝑟 𝑎−𝐹 Φ′(𝑎))2=argmin |     |     | (𝑟 𝑎−𝑟ˆ𝑎)2. |     |                                             |     |     |     |     |       |     |
(11)
|     | Φ′  |     |     | Φ′  |     |     |     |                                       |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- |
|     | ∀𝑎  |     |     | ∀𝑎  |     |     | 3.5 | ActionSelectionandEmbeddingRetraining |     |     |     |     |     |
Theactualfitnessscore𝑟
𝑎,i.e.,recommendationqualityofthe ThepseudocodeforBETispresentedinAlgorithm1.Amongits𝑇
action,canbeevaluatedonthebackbonerecommender𝐺
Θ(·)after
searchiterations,weutilizethreedifferentstrategiestopickone
| beingfinetunedwithanaction𝑎w.r.t.Eq.2: |     |     |     |     |     |     | action𝑎 |     |                             |     |                      |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | --- | --------------------------- | --- | -------------------- | --- | --- |
|                                        |     |     |     |     |     |     |         | 𝑡   | fromthecandidateactionsetQ𝑡 |     | (lines4-12).Then,the |     |     |
eva l (E ⊙ M 𝑎 | D 𝑣𝑎𝑙) r ec o m m e n d e r 𝐺 Θ ( · ) is fi n e t u n ed b y a d o p t in g 𝑎 𝑡 an d e v a lu a t e d o n
|     |     | 𝑟 𝑎 = |     | ,   |     | (12) |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
e v al (E |D 𝑙) th e v al id a ti o n s et ( l i ne s 13 - 1 4 ) ,w h er e t h e p r od u c ed ( 𝑎 𝑡 , 𝑟 𝑎𝑡 ) s a m p l e
𝑣 𝑎
561

WSDM’24,March4–8,2024,Merida,Mexico YunkeQu,TongChen,QuocVietHungNguyen,&HongzhiYin
ispoppedintothepopulationsetAtofacilitatetrainingthefitness • PEP[35]:Itadaptivelyprunestheembeddingparameters
predictionnetwork𝐹 Φ(·)(lines16-20).Finally,aselectiveretraining basedonalearnedpruningthresholdlearnedalongwiththe
processisconductedwiththetop-rankedactionsinthepopulation model’sotherparametersduringthetrainingprocess.
inordertoidentifythebestembeddingsizedecisionforallusersand • ESAPN[?]:ItusesanRLagentwhichperformshardselec-
items.Weprovidefurtherdetailsaboutactionselectionstrategies tiononembeddingsizesforusersanditemsbasedonthe
andretrainingthesparsifiedembeddingsbelow. memorycomplexityandrecommendationperformance.
• OptEmbed[37]:Itprunesredundantembeddingsbasedon
3.5.1 DiversifyingtheActionSpace. Theiterativeinputembedding
learnablepruningthresholdsindicativeoffeatures’impor-
sizesearchcontains𝑇 iterations.Ineachiteration𝑡,theselected
tanceandderivestheoptimalembeddingsizeforeachfield
action𝑎 𝑡 isaddedtothepopulationsetAwithitsassociatedfitness
usingevolutionarysearch.
score. For efficiency consideration, in each iteration𝑡, we only
• CIESS[41]:ItisanRL-basedmethodthatchoosesembedding
computetheactualfitnessscoreforaction𝑎 𝑡,whichisselected
sizesfortheusersanditemsfromacontinuousdomain.
fromcandidateactionsQ𝑡withoneofthethreefollowingstrategies:
• SingleandUniform(SU):Allusersanditemsshareequal
I: Weuseourfitnesspredictionnetwork𝐹 Φ(·)topredictthe
andfixedembeddingsizes.
fitnessscoreofeachcandidateactions,andgreedilyselects • SingleandRandom(SR):Theembeddingsizesoftheusers
theactionpredictedtohavethehighestfitnessscore,i.e.,𝑎 𝑡 = anditemsaresampledfromauniformdistribution.
argmax𝑎∈Q𝑡 𝐹 Φ(𝑎).Inessence,𝐹 Φ(·)isasurrogatefunction
thatistrainedtoapproximateEq.12andissubstantiallymore
cost-effectivethanevaluatingall𝑚actionsviarecommender
finetuning. 4.2 EvaluationProtocols
II: WerandomlyselectoneactionfromtheQ𝑡 todiversifythe
Alltheaforementionedmethodsareevaluatedontworeal-world
trainingsamplesfor𝐹 Φ(·)bypreventingitfromoverfitting
datasets:Gowalla[29]andYelp2018[53].Thefirsthas1,027,370
somespecificactiondistributionsinthepopulationA.
interactionsbetween29,858usersand40,981itemswhilethelatter
III: Weidentifycurrentlythebestaction(withthehighest𝑟 𝑎)
has1,561,147interactionsbetween31,668usersand38,048items.
inA.AllactionsinQ𝑡 andthebestactionareinductively
Wetake50%,25%and25%ofthetwodatasetsfortraining,vali-
embeddedintovectorrepresentationsusingEq.9.Then,by
dation,andtest.Tomeasuretherecommendationperformanceof
calculatingthepairwiseEuclideandistance,weselectaction thebackbonerecommender,Recall@𝑘andNDCG@𝑘areusedas
𝑎 𝑡 ∈Q𝑡 bylocatingthebestaction’snearestneighborinthe evaluationmetrics,where𝑘issettoeither5or20.Totesttherecom-
embeddingspace.
mendationperformanceofCIESS,PEP,SUandSR,threedifferent
3.5.2 SelectiveRetrainingforSparsifiedEmbeddings. After𝑇search sparsityratios(𝑐)of80%,90%and95%areused.Foreachmethod,
iterations,fromthepopulationweidentifythetopfiveactionswith thecompressedembeddingtableisensuredtohavenomorethan
thehighest𝑟 𝑎 onthevalidationset,denotedasA′.Eachaction 𝑐·𝑑 𝑚𝑎𝑥 ·(|U|+|V|)usableparameterandthemaximalembed-
𝑎∈A′ispairedwithafreshbackbonerecommendermodel,which dingsizeis𝑑 𝑚𝑎𝑥 =128.However,sinceESAPNandOptEmbedare
istrainedfromscratchonthetrainingsetuntilconvergence.Next, notdesignedtopreciselycontroltheembeddingsparsityandfocus
weevaluatethetrainedrecommendersandselectthefinalaction moreontheperformance,thissectiononlyreportstheperformance
𝑎∗thatyieldsthebestvalidationperformance: associatedwiththeirfinalembeddingtablesafterpruning.
𝑎∗=argmax𝑟 𝑎 , (14)
𝑎∈A′
withwhichthesparsifiedembeddingE𝑠𝑝𝑎𝑟𝑠𝑒isobtainedandstored 4.3 ImplementationNotesforBET
forinference.
HerebywedetailtheimplementationofBET.Thenumberofsearch
4 EXPERIMENTS
iterations𝑇is10.Themaximalvaluesofthedistributionparameters
𝛽 𝑚𝑎𝑥 are set to 20 for power law distribution, 20 for truncated
ThissectiondetailstheexperimentalresultsofBET’sperformance.
normaldistribution,5fortruncatedexponentialdistributionand
0.5forlognormaldistribution.Themaximalembeddingsize𝑑
𝑚𝑎𝑥
4.1 BaseRecommendersandComparative
is128andtheminimalembeddingsize𝑑 𝑚𝑖𝑛is1.Ineachiteration,
Methods
thepre-trainedbackbonerecommenderisfinetunedfor10epochs
OnecancombineBETwithdifferentembedding-basedrepresenta- (i.e.,ℎ=10)whenthebackbonerecommenderisLightGCNorNCF.
tionlearningbackbonerecommendermodels.Wetestedtheeffec- WhenNGCFisused,thebackbonerecommenderisfinetunedfor
tivenessofourapproachwiththreecommonlyusedrecommender 15epochs(i.e.,ℎ =15).Forfinetuning,theinitiallearningrateis
modelsasthebackbonerecommender𝐹 Φ:NCF[15],NGCF[53] 0.03anddecaysevery200stepswithadecayratioof0.98.The
andLightGCN[14].Weusedthesamesettingsasreportedintheir numberoffitnesspredictionupdatesineachiteration,or𝑁,isset
originalworksandreplacedtheembeddingtablewithonewith to2.Theuseranditemencodershaveinputsize1,outputsize16,
adjustableembeddingsizestodemonstratetheversatilityandgen- andhiddensize16.Thesizeencoderhasinputsize17,outputsize
eralizabilityofourmethodacrossvariousbackbonerecommenders. 64,andhiddensize64.Thedecoderhasinputsize64,outputsize1,
WecompareBETwiththefollowingmodel-agnosticembedding andhiddensize64.AlltheMLP-basedencodersanddecodershave
sizesearchalgorithms: twolayerswiththeLeakyRelU[38]activationfunction.
562

BudgetedEmbeddingTableForRecommenderSystems WSDM’24,March4–8,2024,Merida,Mexico
LightGCN NGCF NCF
Method Sparsity R@5 N@5 R@20 N@20 Sparsity R@5 N@5 R@20 N@20 Sparsity R@5 N@5 R@20 N@20
ESAPN 75% 0.0741 0.1173 0.1579 0.1329 83% 0.0627 0.1060 0.1396 0.1193 74% 0.0498 0.0718 0.1280 0.0959
OptEmb 74% 0.0591 0.0983 0.1314 0.1115 75% 0.0510 0.0860 0.1227 0.1005 82% 0.0330 0.0492 0.0877 0.0653
PEP 0.0715 0.1189 0.1588 0.1347 0.0656 0.1049 0.1524 0.1245 0.0498 0.0704 0.1282 0.0957
SU 0.0756 0.1219 0.1674 0.1400 0.0619 0.0961 0.1466 0.1170 0.0481 0.0662 0.1235 0.0916
SR 80% 0.0708 0.1150 0.1583 0.1323 80% 0.0512 0.0815 0.1223 0.0982 80% 0.0478 0.0656 0.1243 0.0910
CIESS 0.0777 0.1263 0.1750 0.1461 0.0676 0.1084 0.1504 0.1251 0.0550 0.0744 0.1307 0.0997
BET 0.0797 0.1303 0.1753 0.1483 0.0643 0.1039 0.1454 0.1204 0.0511 0.0723 0.1294 0.0973
𝑝-value 0.0024 0.0001 0.0391 0.0012 0.7815 0.2179 0.0514 0.0924 0.1962 0.1337 0.2578 0.0414
PEP 0.0594 0.0992 0.1274 0.1102 0.0552 0.0914 0.1327 0.1081 0.0414 0.0631 0.1121 0.0839
SU 0.0646 0.1041 0.1477 0.1217 0.0589 0.0935 0.1380 0.1115 0.0413 0.0548 0.1112 0.0796
SR 90% 0.0617 0.1013 0.1403 0.1171 90% 0.0466 0.0764 0.1123 0.0911 90% 0.0399 0.0536 0.1069 0.0769
CIESS 0.0721 0.1193 0.1589 0.1353 0.0601 0.0980 0.1380 0.1140 0.0448 0.0613 0.1131 0.0841
BET 0.0736 0.1212 0.1620 0.1376 0.0623 0.1012 0.1426 0.1177 0.0434 0.0648 0.1122 0.0845
𝑝-value 0.0165 0.0481 0.0091 0.0226 0.0005 0.0205 0.0601 0.0232 0.1454 0.0554 0.6608 0.0655
PEP 0.0372 0.0666 0.0803 0.0712 0.0247 0.0471 0.0674 0.0554 0.0351 0.0591 0.0897 0.0712
SU 0.0446 0.0727 0.1085 0.0872 0.0527 0.0870 0.1213 0.1007 0.0336 0.0478 0.0952 0.0682
SR 95% 0.0500 0.0834 0.1178 0.0975 95% 0.0438 0.0739 0.1040 0.0859 95% 0.0329 0.0489 0.0918 0.0674
CIESS 0.0513 0.0853 0.1214 0.0997 0.0505 0.0856 0.1129 0.0964 0.0361 0.0567 0.0933 0.0717
BET 0.0627 0.1037 0.1374 0.1171 0.0528 0.0883 0.1172 0.9980 0.0388 0.0616 0.0963 0.0756
𝑝-value 0.0001 0.0002 0.0001 0.0001 0.1896 0.0638 0.7269 0.3608 0.0321 0.1107 0.1104 0.0010
(a)ResultsonGowalla
LightGCN NGCF NCF
Method Sparsity R@5 N@5 R@20 N@20 Sparsity R@5 N@5 R@20 N@20 Sparsity R@5 N@5 R@20 N@20
ESAPN 73% 0.0294 0.0696 0.0812 0.0773 71% 0.0214 0.0538 0.0632 0.0603 76% 0.0153 0.0342 0.0490 0.0430
OptEmb 80% 0.0183 0.0424 0.0534 0.0489 67% 0.0133 0.0301 0.0412 0.0369 77% 0.0076 0.0161 0.0238 0.0203
PEP 0.0253 0.0605 0.0723 0.0682 0.0086 0.0167 0.0275 0.0223 0.0130 0.0236 0.0406 0.0327
SU 0.0289 0.0665 0.0822 0.0758 0.0223 0.0517 0.0665 0.0603 0.0131 0.0226 0.0465 0.0351
80% 80% 80%
SR 0.0253 0.0588 0.0783 0.0698 0.0212 0.0499 0.0618 0.0573 0.0101 0.0183 0.0342 0.0268
CIESS 0.0292 0.0692 0.0839 0.0783 0.0233 0.0566 0.0701 0.0652 0.0175 0.0377 0.0533 0.0474
BET 0.0310 0.0726 0.0873 0.0816 0.0254 0.0601 0.0741 0.0685 0.0194 0.0451 0.0620 0.0554
𝑝-value 0.0008 0.0309 0.0004 0.0109 0.0412 0.0418 0.0082 0.0024 0.0387 0.0122 0.0483 0.0341
PEP 0.0224 0.0531 0.0657 0.0610 0.0080 0.0153 0.0276 0.0215 0.0139 0.0242 0.0427 0.0335
SU 0.0230 0.0544 0.0722 0.0648 0.0205 0.0528 0.0622 0.0592 0.0119 0.0201 0.0416 0.0309
SR 90% 0.0210 0.0476 0.0642 0.0573 90% 0.0195 0.0449 0.0573 0.0524 90% 0.0089 0.0170 0.0309 0.0242
CIESS 0.0263 0.0649 0.0730 0.0705 0.0232 0.0551 0.0669 0.0619 0.0153 0.0350 0.0500 0.0442
BET 0.0284 0.0674 0.0816 0.0762 0.0246 0.0586 0.0736 0.0676 0.0173 0.0400 0.0565 0.0499
𝑝-value 0.0045 0.0060 0.0051 0.0006 0.0012 0.0007 0.0102 0.0069 0.0234 0.0067 0.0426 0.0118
PEP 0.0199 0.0496 0.0600 0.0561 0.0075 0.0143 0.0259 0.0206 0.0125 0.0244 0.0399 0.0330
SU 0.0217 0.0494 0.0624 0.0571 0.0196 0.0496 0.0573 0.0545 0.0091 0.0174 0.0303 0.0238
SR 95% 0.0195 0.0465 0.0583 0.0540 95% 0.0175 0.0415 0.0528 0.0486 95% 0.0078 0.0145 0.0275 0.0216
CIESS 0.0230 0.0534 0.6570 0.0640 0.0222 0.0540 0.0662 0.0613 0.0157 0.0383 0.0483 0.0446
BET 0.0255 0.0596 0.0727 0.0676 0.0216 0.0505 0.0639 0.0588 0.0170 0.0404 0.0545 0.0491
𝑝-value 0.0403 0.0200 0.0305 0.0204 0.0327 0.0451 0.0064 0.0193 0.0399 0.0246 0.0094 0.0044
(b)ResultsonYelp
Table1:Performanceofallmethodson(a)Gowalla,and(b)Yelp2018withthesparsityratiosetto80%,90%,and95%.Thebest
resultsarehighlighted.Recall@𝑘andNDCG@𝑘aredenotedbyR@𝑘andN@𝑘forsimplicity.Each𝑝-valueiscalculatedviathe
paired𝑡-testbetweenBETandthebestbaseline.
Sparsity SelectionMethod Yelp2018 Gowalla recommendersandatnearlyallspecifiedsparsitylevels(80%,90%,
R@20 N@20 R@20 N@20
RandomSelection 0.0846 0.0788 0.1749 0.1473
and95%).Theassociated𝑝-valuesarebelow5%mostofthetime
80% Simplefitnessprediction 0.0835 0.0779 0.1739 0.1469 sowecanrejectthenullhypothesisthattheobservedperformance
DeepSetsfitnessprediction 0.0873 0.0816 0.1753 0.1483 changesoccurredbychanceinmostscenarios.
RandomSelection 0.0767 0.0717 0.1594 0.1357
Meanwhile,thesparsityratiosachievedbyESAPNandOptEm-
90% Simplefitnessprediction 0.0768 0.0717 0.1590 0.1355
DeepSetsfitnessprediction 0.0816 0.0762 0.1620 0.1376 bedrangefrom67%and83%,oftenfailingtomeettheminimum
RandomSelection 0.0637 0.0583 0.1335 0.1143 targetof80%.Despitekeepingarelativelyhighernumberofparam-
95% Simplefitnessprediction 0.0673 0.0629 0.1349 0.1152
eterscomparedtoothermethods,theirrecommendationperfor-
DeepSetsfitnessprediction 0.0727 0.0676 0.1374 0.1171
Table2:PerformanceofBETwhendifferentselectionmeth- manceisconsistentlyinferiortoBET.Forinstance,whenusedwith
odsareused. LightGCNontheGowalladataset,ESAPNrequiresmorememory
complexity (75% sparsity ratio) to achieve a comparable perfor-
4.4 OverallPerformanceComparison
mancecomparedtoBETunderan90%sparsitycondition.
Table1showstheRecall@𝑘andNDCG@𝑘scoresofvariouslight-
In summary, BET demonstrates superior performance while
weightembeddingmethodswhentheyarepairedwithdifferent
maintainingthesamememoryusage.Similarly,whencomparing
backbonerecommendermodels.Wealsoperformpairedstudent’s
performancelevels,BETprovestobemoreefficientinmemory
𝑡-testbetweenBETandthebestbaselinemethod.Comparedwith
utilization.Consequently,thesefindingshighlightthebenefitsof
thebaselineswithadjustablesparsityratios(i.e.,PEP,SU,SR,and
theongoingembeddingsizeexplorationinBET.
CIESS),BETachievesbetterperformanceacrossallthreebackbone
563

WSDM’24,March4–8,2024,Merida,Mexico YunkeQu,TongChen,QuocVietHungNguyen,&HongzhiYin
(a)Effectof𝑚onYelp (a)Effectof𝑇 onYelp
(b)Effectof𝑚onGowalla (b)Effectof𝑇 onGowalla
Figure 4: Sensitivity analysis of 𝑚 on Recall@20 and Figure 5: Sensitivity analysis of 𝑇 on Recall@20 and
NDCG@20withLightGCNasthebackbonerecommender. NDCG@20withLightGCNasthebackbonerecommender.
4.5 ModelComponentAnalysis
Selectingfromthesetofcandidateactionsineachiterationisavital
stepinBET,whereweproposedahybridselectionmethodthat
alternatelyusesthreeselectionstrategies.Tostudytheeffectiveness
oftheproposedselectionmethodandtheDeepSets-basedfitness
predictionnetwork,weconductaquantitativestudyonBETand
itstwovariants.Thefirstvariantusesrandomselectiononly.The
Figure 6: Sensitivity analysis of 𝑇 on the fitness predic-
secondvariantincorporatesasimplisticfitnesspredictionnetwork
tionlosswithLightGCNasthebackbonerecommenderon
thatonlyacceptstheembeddingsizesofeachuseranditem.Table
Yelp2018(left)andGowalla(right).
2illustratestheperformanceoftheoriginalversionofBETalong
withitstwovariantsintermsoftheirRecall@20andNDCG@20 population A𝑡 for each training iteration𝑡 ∈ [0,𝑇] and report
scores. Only the performance of the best-performing backbone thebestrecommendationperformanceintermsofRecall@20and
recommenderLightGCNisreportedduetospacelimit.Theresults NDCG@20.Wealsoreporttheaveragefitnesspredictionlossin
showthatBETwithaDeepSets-basedfitnesspredictionnetwork each iteration. Figure 6 shows that fitness predictor converges
hasbetterperformancethanthetwovariants,implyingthatour withinthefirst15iterations.Whilethetraininglossofthefitness
proposed selection method is effective and the DeepSets-based predictorisdiminishing,BETwitnessesasubstantialimprovement
architectureisabletolearnthelatentrepresentationofactions. initsperformanceinthefirst10-15iterations,asshowninFigure5.
Thenperformancecontinuestoclimbslowlyafterthe15thiteration
4.6 AnalysisofHyperparameter until it reaches its peak around the 40th iteration and remains
unchangedafterthat.Inconclusion,setting𝑇 =50shouldsuffice
Inthissection,weinspecttheinfluenceofthecorehyperparameters
forBETtofindtheoptimalactionforallsparsityratios.
inBETintermsofRecall@20andNDCG@20.LightGCNshows
thebestperformancesoitischosenasthebackbonerecommender
5 CONCLUSIONANDFUTUREWORKS
fordemonstration.
Latentfactorrecommenderstypicallyemployvectorizedembed-
4.6.1 NumberofSampledActions𝑚. Ineachiteration,wesam-
dingswithauniformandfixedsize,resultinginsuboptimalperfor-
ple𝑚candidateactionstochoosefrom.WetuneBETwith𝑚 ∈
manceandexcessivememorycomplexity.Toaddressthischallenge,
{20,40,60,80,100}forbothYelp2018andGowalla.Thenweshow
wehaveintroducedBET,amodel-agnosticalgorithmtoenablethe
howtheperformancechangeswithdifferentvaluesof𝑚w.r.t.Re-
selectionofcustomizedembeddingsizesatthe leveloftheem-
call@20andNDCG@20scores.AsshowninFigure4,although
beddingtableforeachuser/item.Thisapproachenhancesthethe
BETisrelativelyinsensitivetothevalueof𝑚,betterperformance
embeddingswhileminimizingmemorycosts.Next,wewilldevelop
isachievedwith𝑚=100onbothdatasets.
embeddingsizesearchalgorithmsforstreamingrecommendation.
4.6.2 NumberofIterations𝑇. BETiterativelysamples,selectsand
ACKNOWLEDGMENT
evaluatesactionsinsearchoftheoptimalone.Onenaturalquestion
thatarisesishowmanyiterationsitneedstofindtheactionthat ThisworkissupportedbytheAustralianResearchCouncilunder
leadstopeakrecommendationperformance.Thisquestioniscrucial the streams of Future Fellowship (No. FT210100624), Discovery
forunderstandingtheeffectivenessofBET.Therefore,weperform Project(No.DP190101985),andDiscoveryEarlyCareerResearch
selectiveretrainingasdescribedinSection3.5.2ontheresulting Award(No.DE200101465andNo.DE230101033).
564

BudgetedEmbeddingTableForRecommenderSystems WSDM’24,March4–8,2024,Merida,Mexico
REFERENCES
[25] PijiLi,ZihaoWang,ZhaochunRen,LidongBing,andWaiLam.2017. Neural
[1] AnshumaliShrivastavaAdityaDesai,LiChou.2022.RandomOffsetBlockEmbed- ratingregressionwithabstractivetipsgenerationforrecommendation.InProceed-
ding(ROBE)forcompressedembeddingtablesindeeplearningrecommendation ingsofthe40thInternationalACMSIGIRconferenceonResearchandDevelopment
systems.InProceedingsofMachineLearningandSystems.762–778. inInformationRetrieval.345–354.
[2] MathieuBlondel,AkinoriFujino,NaonoriUeda,andMasakazuIshihata.2016. [26] ShiweiLi,HuifengGuo,LuHou,WeiZhang,XingTang,RuimingTang,Rui
Higher-OrderFactorizationMachines.InProceedingsofthe30thInternational Zhang,andRuixuanLi.2023.AdaptiveLow-PrecisionTrainingforEmbeddings
ConferenceonNeuralInformationProcessingSystems.3359–3367. inClick-ThroughRatePrediction.ProceedingsoftheAAAIConferenceonArtificial
[3] HanCai,ChuangGan,TianzheWang,ZhekaiZhang,andSongHan.2020.Once- Intelligence37,4(2023),4435–4443.
for-all:Trainonenetworkandspecializeitforefficientdeployment.ICLR(2020). [27] SiyuanLiandElenaKarahanna.2015.OnlineRecommendationSystemsinaB2C
[4] ChengChen,XiangwuMeng,ZhenghuaXu,andThomasLukasiewicz.2017. E-CommerceContext:AReviewandFutureDirections.JournaloftheAssociation
Location-AwarePersonalizedNewsRecommendationWithDeepSemanticAnal- forInformationSystems16(2015),72–107.
ysis.IEEEAccess5(2017),1624–1638. [28] YangLi,TongChen,Peng-FeiZhang,andHongzhiYin.2021.Lightweightself-
[5] TingChen,LalaLi,andYizhouSun.2020.DifferentiableProductQuantization attentivesequentialrecommendation.InCIKM.967–977.
forEnd-to-EndEmbeddingCompression.InProceedingsofthe37thInternational [29] DawenLiang,LaurentCharlin,JamesMcInerney,andDavidM.Blei.2016.Mod-
ConferenceonMachineLearning.1617–1626. elingUserExposureinRecommendation.InWWW.951–961.
[6] TongChen,HongzhiYin,GuanhuaYe,ZiHuang,YangWang,andMengWang. [30] XurongLiang,TongChen,QuocVietHungNguyen,JianxinLi,andHongzhiYin.
2020.TryThisInstead:PersonalizedandInterpretableSubstituteRecommenda- 2023.LearningCompactCompositionalEmbeddingsviaRegularizedPruning
tion.InSIGIR.891–900. forRecommendation.InICDM.
[7] TongChen,HongzhiYin,XiangliangZhang,ZiHuang,YangWang,andMeng [31] GuanyuLin,ChenGao,YinfengLi,Y.Zheng,ZhihengLi,DepengJin,andYong
Wang.2021. QuaternionFactorizationMachines:ALightweightSolutionto Li.2022.DualContrastiveNetworkforSequentialRecommendationwithUser
IntricateFeatureInteractionModeling. IEEETransactionsonNeuralNetworks andItem-CentricPerspectives.ACMTransactionsonInformationSystems1,1
andLearningSystems34,8(2021),1–14. (2022).
[8] TongChen,HongzhiYin,YujiaZheng,ZiHuang,YangWang,andMengWang. [32] WeilinLin,XiangyuZhao,YejingWang,TongXu,andXianWu.2022.AdaFS:
2021.LearningElasticEmbeddingsforCustomizingOn-DeviceRecommenders. AdaptiveFeatureSelectioninDeepRecommenderSystem.InProceedingsof
InSIGKDD.138–147. the28thACMSIGKDDConferenceonKnowledgeDiscoveryandDataMining.
[9] YankaiChen,HuifengGuo,YingxueZhang,ChenMa,RuimingTang,JingjieLi, 3309–3317.
andIrwinKing.2022. LearningBinarizedGraphRepresentationswithMulti- [33] HanLiu,YinweiWei,JianhuaYin,andLiqiangNie.2023.HS-GCN:Hamming
FacetedQuantizationReinforcementforTop-KRecommendation.InSIGKDD. SpatialGraphConvolutionalNetworksforRecommendation.TKDE35,6(2023),
168–178. 5977–5990.
[10] YankaiChen,HuifengGuo,YingxueZhang,ChenMa,RuimingTang,Jingjie [34] HaochenLiu,XiangyuZhao,ChongWang,XiaobingLiu,andJiliangTang.2020.
Li,andIrwinKing.2022. LearningBinarizedGraphRepresentationswith Automatedembeddingsizesearchindeeprecommendersystems.InSIGIR.2307–
Multi-FacetedQuantizationReinforcementforTop-KRecommendation.InKDD. 2316.
168–178. [35] SiyiLiu,ChenGao,YihongChen,DepengJin,andYongLi.2021. Learnable
[11] AdityaDesaiandAnshumaliShrivastava.2022. Thetrade-offsofmodelsize EmbeddingsizesforRecommenderSystems.InICLR.
inlargerecommendationmodels:100GBto10MBCriteo-tbDLRMmodel.In [36] YuanfeiLuo,MengshuoWang,HaoZhou,QuanmingYao,Wei-WeiTu,Yuqiang
NeurIPS.33961–33972. Chen,WenyuanDai,andQiangYang.2019.Autocross:Automaticfeaturecrossing
[12] YuyunGongandQiZhang.2016.Hashtagrecommendationusingattention-based fortabulardatainreal-worldapplications.InSIGKDD.1936–1945.
convolutionalneuralnetwork..InIJCAI.2782–2788. [37] FuyuanLyu,XingTang,HongZhu,HuifengGuo,YingxueZhang,Ruiming
[13] HuifengGuo,RuimingTang,YunmingYe,ZhenguoLi,andXiuqiangHe.2017. Tang,andXueLiu.2022. OptEmbed:LearningOptimalEmbeddingTablefor
DeepFM:afactorization-machinebasedneuralnetworkforCTRprediction.IJCAI Click-throughRatePrediction.InCIKM.1399–1409.
(2017). [38] AndrewLMaas,AwniYHannun,AndrewYNg,etal.2013.Rectifiernonlineari-
[14] XiangnanHe,KuanDeng,XiangWang,YanLi,YongdongZhang,andMeng tiesimproveneuralnetworkacousticmodels.InICML.
Wang.2020.Lightgcn:Simplifyingandpoweringgraphconvolutionnetworkfor [39] KhalilMuhammad,QinqinWang,DiarmuidO’Reilly-Morgan,EliasTragos,Barry
recommendation.InSIGIR.639–648. Smyth,NeilHurley,JamesGeraci,andAonghusLawlor.2020. Fedfast:Going
[15] XiangnanHe,LiziLiao,HanwangZhang,LiqiangNie,XiaHu,andTat-Seng beyondaverageforfastertrainingoffederatedrecommendersystems.InSIGKDD.
Chua.2017.Neuralcollaborativefiltering.InWWW.173–182. 1234–1242.
[16] ZhenhuaHuang,XinXu,JuanNi,HonghaoZhu,andChengWang.2019.Multi- [40] LiangQu,YonghongYe,NingzhiTang,LixinZhang,YuhuiShi,andHongzhiYin.
modalrepresentationlearningforrecommendationinInternetofThings.IEEE 2022. Single-ShotEmbeddingDimensionSearchinRecommenderSystem.In
InternetofThingsJournal6,6(2019),10675–10685. SIGIR.513–522.
[17] GangweiJiang,HaoWang,JinChen,HaoyuWang,DefuLian,andEnhongChen. [41] YunkeQu,TongChen,XiangyuZhao,LizhenCui,KaiZheng,andHongzhiYin.
2021.XLightFM:ExtremelyMemory-EfficientFactorizationMachine.InSIGIR. 2023.ContinuousInputEmbeddingSizeSearchForRecommenderSystems.In
337–346. SIGIR.708–717.
[18] ManasRJoglekar,CongLi,MeiChen,TaibaiXu,XiaomingWang,JayKAdams, [42] SteffenRendle.2010.Factorizationmachines.In2010IEEEInternationalconference
PranavKhaitan,JiahuiLiu,andQuocVLe.2020.Neuralinputsearchforlarge ondatamining.995–1000.
scalerecommendationmodels.InSIGKDD.2387–2397. [43] SteffenRendle,ChristophFreudenthaler,ZenoGantner,andLarsSchmidt-Thieme.
[19] Wang-ChengKang,DerekZhiyuanCheng,TingChen,XinyangYi,DongLin, 2009.BPR:BayesianPersonalizedRankingfromImplicitFeedback.InProceedings
LichanHong,andEdH.Chi.2020.LearningMulti-GranularQuantizedEmbed- oftheTwenty-FifthConferenceonUncertaintyinArtificialIntelligence.452–461.
dingsforLarge-VocabCategoricalFeaturesinRecommenderSystems.InWWW. [44] NaserSedaghati,TeMu,Louis-NoelPouchet,SrinivasanParthasarathy,andP
562–566. Sadayappan.2015.AutomaticselectionofsparsematrixrepresentationonGPUs.
[20] NitishShirishKeskar,DheevatsaMudigere,JorgeNocedal,MikhailSmelyanskiy, InACMInternationalConferenceonSupercomputing.99–108.
andPingTakPeterTang.2016. OnLarge-BatchTrainingforDeepLearning: [45] SuvashSedhain,AdityaKrishnaMenon,ScottSanner,andLexingXie.2015.
GeneralizationGapandSharpMinima.InICLR. AutoRec:AutoencodersMeetCollaborativeFiltering.InWWW.111–112.
[21] YunyongKo,Jae-SeoYu,Hong-KyunBae,YongjunPark,DongwonLee,and [46] GeetSethi,BilgeAcun,NiketAgarwal,ChristosKozyrakis,CarolineTrippel,and
Sang-WookKim.2021.MASCOT:AQuantizationFrameworkforEfficientMatrix Carole-JeanWu.2022.RecShard:StatisticalFeature-BasedMemoryOptimization
FactorizationinRecommenderSystems.In2021IEEEInternationalConferenceon forIndustry-ScaleNeuralRecommendation.InProceedingsofthe27thACM
DataMining(ICDM).290–299. InternationalConferenceonArchitecturalSupportforProgrammingLanguagesand
[22] ShumingKong,WeiyuCheng,YanyanShen,andLinpengHuang.2023.AutoSrh: OperatingSystems.344–358.
AnEmbeddingDimensionalitySearchFrameworkforTabularDataPrediction. [47] Hao-JunMichaelShi,DheevatsaMudigere,MaximNaumov,andJiyanYang.2020.
TKDE35,7(2023),6673–6686. Compositionalembeddingsusingcomplementarypartitionsformemory-efficient
[23] SuMonKywe,Ee-PengLim,andFeidaZhu.2012. Asurveyofrecommender recommendationsystems.InSIGKDD.165–175.
systemsintwitter.InInternationalConferenceonSocialInformatics.420–433. [48] YangSun,FajieYuan,MinYang,GuoaoWei,ZhouZhao,andDuoLiu.2020.A
[24] JoonseokLee,SamiAbu-El-Haija,BalakrishnanVaradarajan,andApostolNatsev. GenericNetworkCompressionFrameworkforSequentialRecommenderSystems.
2018.Collaborativedeepmetriclearningforvideounderstanding.InProceedings InSIGIR’20.1299–1308.
ofthe24thACMSIGKDDInternationalconferenceonknowledgediscovery&data [49] PauliVirtanenetal.2020.SciPy1.0:fundamentalalgorithmsforscientificcom-
mining.481–490. putinginPython.NatureMethods17,3(2020),261–272.
[50] EdwardWagstaff,FabianBFuchs,MartinEngelcke,MichaelAOsborne,and
IngmarPosner.2022.Universalapproximationoffunctionsonsets.JMLR23,1
(2022),6762–6817.
565

WSDM’24,March4–8,2024,Merida,Mexico YunkeQu,TongChen,QuocVietHungNguyen,&HongzhiYin
[51] ShoujinWang,LongbingCao,YanWang,QuanZSheng,MehmetAOrgun, LearningforRecommendation.InSIGIR.1294–1303.
andDefuLian.2021.Asurveyonsession-basedrecommendersystems.ACM [59] ManzilZaheer,SatwikKottur,SiamakRavanbhakhsh,BarnabásPóczos,Ruslan
ComputingSurveys(CSUR)54,7(2021),1–38. Salakhutdinov,andAlexanderJSmola.2017.DeepSets.InNeurIPS.3394–3404.
[52] SuhangWang,YilinWang,JiliangTang,KaiShu,SuhasRanganath,andHuanLiu. [60] CaojinZhang,YicunLiu,YuanpuXie,SofiaIraKtena,AlykhanTejani,Akshay
2017.WhatYourImagesReveal:ExploitingVisualContentsforPoint-of-Interest Gupta,PranayKumarMyana,DeepakDilipkumar,SuvadipPaul,IkuhiroIhara,
Recommendation.InProceedingsofthe26thInternationalConferenceonWorld etal.2020. Modelsizereductionusingfrequencybaseddoublehashingfor
WideWeb.391–400. recommendersystems.InFourteenthACMConferenceonRecommenderSystems.
[53] XiangWang,XiangnanHe,MengWang,FuliFeng,andTat-SengChua.2019. 521–526.
Neuralgraphcollaborativefiltering.InSIGIR.165–174. [61] ShuaiZhang,LinaYao,AixinSun,andYiTay.2019.Deeplearningbasedrec-
[54] YejingWang,XiangyuZhao,TongXu,andXianWu.2022.Autofield:Automating ommendersystem:Asurveyandnewperspectives. ACMComputingSurveys
featureselectionindeeprecommendersystems.InWWW.1977–1986. (CSUR)52,1(2019),1–38.
[55] XinXia,HongzhiYin,JunliangYu,QinyongWang,GuandongXu,andQuoc [62] XiangyuZhao,HaochenLiu,WenqiFan,HuiLiu,JiliangTang,ChongWang,
VietHungNguyen.2022. On-DeviceNext-ItemRecommendationwithSelf- MingChen,XudongZheng,XiaobingLiu,andXiwangYang.2021. Autoemb:
SupervisedKnowledgeDistillation.InSIGIR.546–555. Automatedembeddingdimensionalitysearchinstreamingrecommendations.In
[56] XinXia,JunliangYu,QinyongWang,ChaoqunYang,NguyenQuocVietHung, 2021IEEEInternationalConferenceonDataMining(ICDM).896–905.
andHongzhiYin.2023. EfficientOn-DeviceSession-BasedRecommendation. [63] RuiqiZheng,LiangQu,BinCui,YuhuiShi,andHongzhiYin.2022. AutoML
ACMTransactionsInformationSystems41,4(2023). forDeepRecommenderSystems:ASurvey.ACMTransactionsonInformation
[57] BenchengYan,PengjieWang,JinquanLiu,WeiLin,Kuang-ChihLee,JianXu,and Systems101(2022),1–38.
BoZheng.2021.BinaryCodeBasedHashEmbeddingforWeb-ScaleApplications. [64] MeiziZhou,ZhuoyeDing,JiliangTang,andDaweiYin.2018.MicroBehaviors:
InCIKM.3563–3567. ANewPerspectiveinE-CommerceRecommenderSystems.InProceedingsofthe
[58] JunliangYu,HongzhiYin,XinXia,TongChen,LizhenCui,andQuocVietHung EleventhACMInternationalConferenceonWebSearchandDataMining.727–735.
Nguyen.2022.AreGraphAugmentationsNecessary?SimpleGraphContrastive
566