A Recommendation System for Participatory Budgeting
GilLeibiker NimrodTalmon
Ben-GurionUniversity,Israel
ABSTRACT Asub-fieldofComputationalsocialchoiceisParticipatoryBud-
Inparticipatorybudgeting,votersspecifytheirpreferencesovera geting(PB).PBisademocraticprocessinwhichcommunitymem-
setofprojectsofdifferentcostsandthegoalistoselectasubset bersdecidehowtospendaportionofapublicorprivatebudget.
oftheseprojectsthatsatisfysometotalcostupperboundwhile PBallowsmembersofacommunitytomaketheirvoicesheard
taking into account the preferences of the voters. To lower the regardingfundingdecisionsaffectingarangeoffieldssuchasedu-
cognitiveburdenonvoters,andtoincreasevoterparticipationin cation,healthandenvironment.Itgivesthemthepowertocompose
PBprocesses,weproposeanapproachbasedonamachinelearning projectproposalsandtoexpresstheirpreferencesoverthebudget
techniquesasrecommendationsystemandbinaryclassification allocation[1–3,7].Inourstudyweconcentrateonthemostpopular
thatqueriesvotersforpartialballotsandestimatestheircompletion. variantofPB,namelyapproval-basedcombinatorialPB.Thatis,
Wedevelopseveralconcretealgorithmsandevaluatethem–based givenasetofprojects–eachwithitscost–eachvoterexpressesits
onreal-worldinstances–wrt.theirabilitytocorrectlyapproximate preferencesovertheprojectsbyselectingasubsetoftheprojects
voterballotsaswellastheoveralloutcomeoftheprocess. thatshe“approvesof”,andtheresultoftheprocessofaggregating
suchvoterpreferencesisasubsetoftheprojectswhosetotalcost
KEYWORDS doesnotgooversomegivenbudgetupperbound[2,3].
InthisresearchweconsiderprocessesofPBandconcentrate
ComputationalSocialChoice,Attention-AwareSocialChoice,Par-
ontheinformationoverloadproblem,i.e.,thecognitiveburdenof
ticipatoryBudgeting,MachineLearning,RecommendationSystem
votersparticipatinginsuchprocesses.Essentially,theinformation
overloadproblemappearswhentoomuchinformationinterferes
ACMReferenceFormat:
withdecisionmaking[11,20].Tomitigatetheinformationoverload
GilLeibiker NimrodTalmon,Ben-GurionUniversity,Israel.2023.A
RecommendationSystemforParticipatoryBudgeting.InProc.ofthe22nd problemweproposeseveralsolutionsbasedontechniquesfrom
InternationalConferenceonAutonomousAgentsandMultiagentSystems machinelearningandrecommendationsystems.
(AAMAS2023),London,UnitedKingdom,May29–June2,2023,IFAAMAS, Recommendationsystems(RS)areapowerfultoolinmachine
11pages. learning,utilizingalgorithmstoprocesslargedatasetsandmake
personalizedpredictionsforusers[14,20].Bylearninguserprefer-
encesandusagepatterns,RScanprovideuserswithtailoredand
1 INTRODUCTION
relevantrecommendationsforproducts,services,orcontent[11,20].
SocialChoiceTheoryisabranchofeconomicsthatstudiescollec- Forexample,amovieRScouldsuggestfilmsbasedonpastuser
tivedecision-makingprocessesandthepreferencesofindividual ratings,genrepreferences,andevensocialconnections.Similarly,
agents.Itaimstodeterminehowamajoritycanmakedecisions arestaurantRScouldsuggesteateriesbasedonlocation,cuisine
basedonthepreferencesofagroup,whilestillrespectingeach type,andpricerange.Moreover,RSarebeingappliedinmanyother
individualinvolved.Thetheoryexploresvariousvotingsystems areassuchasmusic,books,andshopping,makingthemanimpor-
andwaystostructurevotingproceduresinordertomoreaccurately tantpartofmachinelearning.Theinformationoverloadproblem
representthewillofthemajority.SocialChoiceTheoryisanim- isdeeplyrelatedtotheresearchonRS[4,20,24].Itmayeffect
portantresearchareaasitseekstounderstandcollectivebehavior, the decision making of participants in such systems in various
andcanbeappliedtonumerousfieldssuchaspoliticaldecision- aspects,inparticularasusersmayfinditchallengingtochoose
making, economic welfare, and game theory. In essence, Social themostappropriatechoicesoutofthehugeamountandvariety
ChoiceTheoryprovidesaframeworktobetterunderstandinghow ofcontentthattheinternetoffers.ThegoalofaRSistosupport
ourdecisionsimpactothers,andhowwecanmakedecisionsthat usersinvariousdomainsofdecisionmakingprocesses,suchas
arebothequitableandefficient[5,13,17] whatitemstopurchase,whichmoviestowatch,orwhichbooks
Computationalsocialchoiceisafieldofresearchthatcombines toread[14,20,22].Inparticular,theresearchonRS,beingwell-
computerscience,gametheoryandsocialchoicetheorytodevelop establishedbynow,offersvaluabletoolsforonlineuserstocope
algorithmsforcollectivedecisionmaking.Itexamineshowgroups withinformationoverloadandhelptheminmakingbetterchoices.
ofpeoplecanusecomputerstomakedecisionsthatarefair,effi- Inthispaperwediscusstheproblemofinformationoverloadin
cientandbasedoninputsfromallinvolvedparties.Computational PBwherevotershavetoconsideralargenumberofprojects,leading
socialchoicecanbeusedinavarietyofreal-worldscenariossuch to a time-consuming and attention-demanding task [8, 27]. We
as voting systems, resource allocation, market design and even proposeasolutionthatinvolvesanapplicationthatusesmachine
communicationsnetworks[5]. learningandRStoestimateavoter’spreferencesfortheremaining
projectsbasedontheiropinionsaboutafewprojects.Thisapproach
couldsavevoterstimeandallowthemtoexpressbetterpreferences
Proc.ofthe22ndInternationalConferenceonAutonomousAgentsandMultiagentSys-
tems(AAMAS2023),A.Ricci,W.Yeoh,N.Agmon,B.An(eds.),May29–June2,2023, fortheproposalstheydoconsider.Thepaperhighlightsthebenefits
London,UnitedKingdom.©2023InternationalFoundationforAutonomousAgents
andMultiagentSystems(www.ifaamas.org).Allrightsreserved.

ofthissystem,whichcouldleadtoamoreefficientandeffective
PBprocess.
1.1 PaperStructure
Afterprovidinganintroduction,inSection1,wegoontodiscuss
somepreliminaries(inSection2)regardingparticipatorybudgeting
Figure1:Ratingmatrixexample.Eachcellrepresentsthe
processes,machinelearningmethodsandouralgorithmictasks.
ratingthatausergivestoaparticularitem.
Then,wecontinue–inSection3.1–bydescribingthedifferent
problemvariantsweconsideranditscorrespondingalgorithms.In
sections4,5and6wedescribethedatasetsthatweexaminedour betweenanuserandanitem,meaningthepredictionoftherat-
experimentson,discussabouttheevaluationmethodsanddescribe ingoftheitemthatmaybegivenbytheuser(sucharatingcan
thevariousexperimentsweconducted.InSection7wepresent berepresentedinvariousranges[14,20,24]).RStechniquesare
anddiscussourexperimentalresults.WeconcludeinSection8,in extensivelyusedinthee-commerceindustry[4,20],wherethere
whichwediscusspossibleavenuesforfutureresearch. isabusinessaspectforhowgoodtherecommendationsare.
The information based on which such RS operate can be ac-
2 PRELIMINARIES
quiredexplicitlybycollectingusers’ratings.Sincetherisingofthe
Wediscussonthebinaryclassificationtechniqueandrecommen- popularityofsocialnetworksandotherplatforms,thereisahuge
dationsystems(Section2.1),thestandardmodelofcombinatorial corpusofavailabledatathatRStoolscanusefortheiranalysisand
participatorybudgeting(PB;Section2.2),themodelofPBwith operation[14,20,22].Anotherwayforgatheringuserinformation
partialballotsthatweusehere(Section2.3)andthealgorithmic isbyamoreimplicitway,i.e.,byanalyzinguserbehavioronaspects
taskwedealtwith(Section2.4). suchaswebsearchesandotherformsofusagehistory[4,14].In
ourresearchwefocusedonCollaborativefiltering(CF)andHybrid
2.1 BinaryClassificationandRecommendation RS.
Systems
CollaborativeFiltering. Thecollaborativefiltering(CF)approach
Wedividethissectiontotwoparts:BinaryClassificationandRec- playsanimportantroleinRStools.Itoperatesbyanalyzingrelation-
ommendationsystems. shipsbetweenusersanditemsinordertoidentifynewuser-item
interactions[15,20,21].CFreliesonanold,automaticactofpeople
2.1.1 Binaryclassification. Binaryclassificationisasupervised
sharingopinionbetweentheminordertomakebetterdecisions.
machinelearningtechniqueinwhichamodelistrainedtopredict
Forinstance,apersonmaydecidetogotoacertainrestaurantafter
oneoftwopossibleoutcomes,oftenrepresentedas"0"or"1"[18].
hearinggoodthingsaboutitfromseveralfriends.Corresponding,
Thistypeofclassificationiscommonlyusedinawiderangeof
hearingverybadreviewsregardinganewmoviefromcolleagues
applications.Theprimarygoalofbinaryclassificationistoidentify
mayresultindecidingtowatchanothermovieinstead.Essentially,
whichofthetwoclassesaninputsamplebelongsto,basedonaset
theCFtechniqueoperatesinasimilarfashion,howeveritallows
offeaturesorattributes[18].Theprocessoftrainingabinaryclas-
toconsidersuchopinionsonamuchlargerscale[20,21].
sifierinvolvesprovidingthemodelwithlabeledexamplesofeach
InaCFscenario,auser-itemmatrixisconstructed,whereeach
class,andthenadjustingthemodel’sparameterstominimizethe
cellinthematrixrepresentstheratingthatausergivestoaparticu-
classificationerroronthetrainingset.Oncethemodelistrained,it
laritem.Formally,aratingconsistsoftheassociationoftwothings
canthenbeusedtomakepredictionsonnew,unseensamples.One
–useranditem,onewaytovisualizeratingsisasamatrixwhere
popularalgorithmforbinaryclassificationisXGBoost(eXtreme
eachrowrepresentsauser,eachcolumnrepresentsanitem,and
GradientBoosting).Thisalgorithmisanensemblelearningtech-
thenumberattheintersectionofarowandacolumnrepresents
niquethathasbeenwidelyusedinbinaryclassificationtasks[9,26].
theuser’sratingvalueasshowninFigure1.Theabsenceofarating
Itisanimplementationofgradientboosting,apowerfulensemble
scoreatthisintersectionindicatesthatuserhasnotyetratedthe
methodthatcombinesthepredictionsofmultipleweaklearnersto
item[20,21].
produceamoreaccurateprediction[9,26].XGBoostisspecifically
OneprimaryfieldofCFislatentfactormodels[15,20,21].Latent
designedfordecisiontree-basedmodels,andithasbeenobservedto
factormodelsareapopulartechniqueinRSforcapturingtheun-
outperformotherpopularmachinelearningalgorithms[9].Overall,
derlyingpreferencesandattributesofusersanditems[15,21].The
XGBoostisapowerfulandwidely-usedtoolforbinaryclassification
ideabehindlatentfactormodelsisthattheobservedratingsaregen-
tasks,anditiswell-suitedfordatasetswithcomplex,non-linear
eratedbyalow-dimensionallatentspace,whereeachuseranditem
relationships[9,26]
isrepresentedbyasetoflatentfactors[15,21].Thelearnedlatent
2.1.2 RecommendationSystems. RSaretoolsthatarebasedonma- factorscanthenbeusedtomakepersonalizedrecommendations
chinelearningtechniques.Theirpurposeistogatherandanalyze tousers.Latentfactormodelscanhandlethesparsityproblemthat
informationregardingthepreferencesofuserswrt.asetofitems arisesinlargeuser-itemmatricesandcanmakerecommendations
inordertodeliverforeachuserasetofrecommendeditemsthat evenforuserswithlimitedratings.Onelatentfactormodelisthe
theuserhopefullywillfindinterestingtointeractwith[14,20,24]. MatrixFactorization(MF),MFcanthenbeusedtofactorizethis
RSareinformationfilteringsystemsthatprocessuser’sanditem’s largeuser-itemmatrixintotwosmallermatrices:ausermatrixand
informationtoprovidepersonalizedpredictionontheinteraction anitemmatrix[15].Theusermatrixcapturesthelatentpreferences
2

oftheusers,whiletheitemmatrixcapturesthelatentattributesof 2.2.3 PopularityandConsensus. Givenaset𝑉 ofvoterswiththeir
approvalballotsoveraset𝑃
theitems[15,16].Thesefactorizedmatricescanthenbeusedto ofprojects,itisusefultoconsiderthe
makepersonalizedrecommendationstousersbyfindingtheitems approvalscoreofeachprojectaswellastheconsensusdegreeofeach
| thataremostsimilartotheitemstheyhaveratedhighlyinthe |     |     |     | project. |     |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
past.ByusingMF,CFcanhandlethesparsityproblemthatarises
|                                                         |     |     |     | Definition2.1(Approvalscores). |     |     |     | 𝑠𝑐𝑜𝑟𝑒(𝑝)=|{𝑣 |     | ∈𝑉  | :𝑝 ∈𝑣 𝑖}|. |
| ------------------------------------------------------- | --- | --- | --- | ------------------------------ | --- | --- | --- | ------------ | --- | --- | ---------- |
| inlargeuser-itemmatrices,wheremanycellsareempty,andmake |     |     |     |                                |     |     |     |              |     | 𝑖   |            |
ofaproject𝑝,denotedby𝑠𝑐𝑜𝑟𝑒(𝑝),isthe
recommendationsevenforuserswithlimitedratings[15,16,20]. Theapprovalscore
numberofvotersthatapproveit.Wefurthermoredefine𝜎
tobe
Hybridapproach-FactorizationMachines. HybridRScombine theset𝑃 ofprojects,sortedindecreasingorderoftheirscores;in
twoormorerecommendationtechniquestothatallowaRStomake particular,𝜎 1istheprojectthathasthemostvoteswhile𝜎 𝑚 isthe
accurateandreliablerecommendationswithfewerofthedrawbacks leastpopularproject.
ofanyindividualone[6].Thehybridapproachcombinesthebest 𝜎 popularity,𝛾,
|     |     |     |     | While |     | orders | the projects | according |     | to their |     |
| --- | --- | --- | --- | ----- | --- | ------ | ------------ | --------- | --- | -------- | --- |
ofbothmethodstoprovideamoreholisticapproachthatcanbetter
definednext,orderstheprojectsaccordingtohowmuchthevoters
identifyuserpreferenceandpersonalizetherecommendationsto
areinconsensusregardingthem.
eachindividualuser[6,20].Ithelpstoovercomethelimitationsof Theconsensuslevelofaproject𝑝,denotedby𝑐𝑜𝑛𝑠𝑒𝑛𝑠𝑢𝑠(𝑝),is
eachmethodsuchascoldstart,scalabilityandsparsitybycombin- theabsolutedifferencebetweenthenumberofvotersapproving𝑝
ingthestrengthsofbothandproducingbetterrecommendations andthenumberofvotersdisapproving𝑝;
thananyindividualmethodcouldprovide[16,20].
FactorizationMachines(FM)isahybridapproachthatincreas- Definition2.2(Consensuslevels). 𝑐𝑜𝑛𝑠𝑒𝑛𝑠𝑢𝑠(𝑝) =𝑎𝑏𝑠(|{𝑣 𝑖 ∈𝑉 :
|     |     |     |     | 𝑝 ∈𝑣 | 𝑖|,|{𝑣 | 𝑖 ∈𝑉 :𝑝 | ∉𝑣 𝑖}|). |     |     |     |     |
| --- | --- | --- | --- | ---- | ------ | ------- | -------- | --- | --- | --- | --- |
inglygainingtractionduetotheirabilitytogeneratehighqual-
ityandpersonalizedrecommendations[19].FMarelearningal-
Notethat,inparticular,bothaprojectthatisapprovedbyall
gorithmswhichcombinethestrengthsoflinearmodelsandMF
votersaswellasaprojectthatisdisapprovedbyallvotershave
methodstolearnfromsparsedatasets[19].Thisenablesthemto
|     |     |     |     | consensuslevel𝑛.Correspondingly,wedefine𝛾 |     |     |     |     |     | tobetheset𝑃 | of  |
| --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | ----------- | --- |
captureintricateuser-iteminteractionsandtheassociatedlatent
projects,sortedindecreasingorderoftheirconsensuslevels;in
factors, resulting in improved accuracy and personalization for particular,𝛾 isthe“mostcontroversial”project.
𝑚
| recommending | products, | movies, and other | items to individual |     |     |     |     |     |     |     |     |
| ------------ | --------- | ----------------- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
users. 2.2.4 Budgetupperlimitandoutcome. Thebudgetlimitisdenoted
by𝐵.Theoutcome(alsoreferredtoasthewinningbundle)ofaPB
FMmodelspossessseveraladvantagesoverexistingrecommen-
|     |     |     |     | processisasetofprojects𝑝★⊆𝑃 |     |     |     | where(cid:205) |     |     |     |
| --- | --- | --- | --- | --------------------------- | --- | --- | --- | -------------- | --- | --- | --- |
dationalgorithms,mainlyduetotheiruniquestructure[19].Unlike 𝑝∈𝑝★ 𝐶 𝑝 ≤𝐵(i.e.,that
respectsthebudgetlimit).
othermodels,whichrelyonfixedfeaturerepresentationsthatare
oftentailoredtoonetypeofdataset,FMmodelsarecapableof
|     |     |     |     | 2.2.5 | Votingrulesandgreedyapproval. |     |     |     | Avotingruleisafunction |     |     |
| --- | --- | --- | --- | ----- | ----------------------------- | --- | --- | --- | ---------------------- | --- | --- |
automaticallylearningcomplexfeaturerepresentationsderived
takinganinstanceofPBandreturningawinningbundle.Themost
frominteractionsbetweenusersanditems[19,20].Thisessentially
popularvotingruleforPBcanbedescribedasagreedyapproval[25];
allowsthemtocapturetheunderlyingfeaturesthatinfluenceusers’
intuitively,itconsiderstheprojectsaccordingtotheirapproval
preferencesinaneffectivemanner[19].Inaddition,FMmodels scores,decreasingly,andkeepsfundingprojectsuntilthebudgetis
arehighlyefficientintermsofcomputationalcost,astheyrequire
exhausted.
minimalpre-processingandrequireonlyasmalldatasettoproduce
Formally,greedyapprovalproceedsiniterationsandmaintains
accurateresults[19,20]. atemporarybudget𝐵′andatemporarywinningbundle𝑆′.Initially,
|     |     |     |     | 𝐵′  | := 𝐵and𝑆′ | =   | ∅.Inthe𝑖thiteration,𝑖 |     | ∈   | [𝑛],theproject𝜎 | 𝑖 is |
| --- | --- | --- | --- | --- | --------- | --- | --------------------- | --- | --- | --------------- | ---- |
2.2 ParticipatoryBudgeting considered.If𝐶 ≤ 𝐵′,thentheamount𝐶 isdecreasedfrom
|     |     |     |     |     |     | 𝜎𝑖  |     |     |     | 𝜎𝑖  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝐵′ and𝜎 isaddedto𝑆′.Afterthe𝑛thiteration,𝑆′
InourresearchwefocusoncombinatorialPB,asitisthemoststud- 𝑖 containsthe
| iedandappliedmodelofPB[2].Belowwedescribetheingredients |     |     |     | winningbundle. |     |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
ofaninstanceofcombinatorialPB.NotethatcombinatorialPBisa
|                                                |     |     |     | Example |     | 2.3. Consider |                    | a toy example | with | 𝑃 =     | {𝑝 ,𝑝 ,𝑝 }, |
| ---------------------------------------------- | --- | --- | --- | ------- | --- | ------------- | ------------------ | ------------- | ---- | ------- | ----------- |
| formalgeneralizationofmultiwinnerelections[1]. |     |     |     |         |     |               |                    |               |      |         | 1 2 3       |
|                                                |     |     |     | where𝐶  |     | =𝐶 =1,𝐶       | =2,and𝐵=3;andwith𝑉 |               |      |         | ={𝑣 ,𝑣 ,𝑣 } |
|                                                |     |     |     |         | 𝑝 1 | 𝑝 2           | 𝑝 3                |               |      |         | 1 2 3       |
|                                                |     |     |     |         | 𝑣   | = { 𝑝         | , 𝑝 }, 𝑣 =         | { 𝑝 , 𝑝 },    | 𝑣    | = { 𝑝 } |             |
2 . 2 .1 P r o j e c ts. T he s et o f p r o j ec ts i s d e n o t e d b y 𝑃 = { 𝑝 , . . . ,𝑝 } . suc h t h a t 1 1 2 2 1 3 an d 3 2 .
|     |       |     | 1 𝑚 |     |             | t𝑠 𝑐𝑜 𝑟 𝑒 | 𝑝 𝑠𝑐 𝑜𝑟 | 𝑒 𝑝     | 𝑠𝑐     | 𝑜𝑟 𝑒 𝑝          |     |
| --- | ----- | --- | --- | --- | ----------- | --------- | ------- | ------- | ------ | --------------- | --- |
|     | 𝑝 ∈ 𝑃 | 𝐶   |     | N   | o t e t h a |           | ( 1 ) = | ( 2 ) = | 2 a nd | ( 3 )=1.Thus,in |     |
E a c hpr o j e c t ha s it s c o s t 𝑝 (u s u a l ly , t h e re s ou rc e t a k i n g in t o thefirstandseconditerationsofgreedyapproval,𝑝 1and𝑝
2will
accountforcostismoney[2]).Notethatmodelisindivisible,and,
bealreadyselectedtobeincludedinthewinningbundle;and,so,
inparticular,eachprojectcanbeeitherfullyimplemented(atits
|     |     |     |     | inthethirditerationofgreedyapproval,inwhich𝑝 |     |     |     |     |     | 3isconsidered, |     |
| --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | -------------- | --- |
givencost)ornotimplementedatall.IncombinatorialPBprojects
thereisnotenoughbudgetlefttofundit,soitwillbeskipped.The
areeitherfullyimplementedornotimplementedatall.
|               |            |                       |                 | winningbundleisthus{𝑝 |     |     | ,𝑝  |      |     |     |     |
| ------------- | ---------- | --------------------- | --------------- | --------------------- | --- | --- | --- | ---- | --- | --- | --- |
|               |            |                       |                 |                       |     |     | 1   | 2 }. |     |     |     |
| 2.2.2 Voters. | The set of | voters is denoted by𝑉 | = {𝑣 ,...,𝑣 𝑛}, |                       |     |     |     |      |     |     |     |
1
2.3 ParticipatoryBudgetingwithPartialBallots
whereeachvotersubmitsherpreferencesonthepotentialprojects.
Weconsiderapproval-basedprocesses,inwhichtheballotofavoter Recallthatweareinterestedinsituationsinwhichnotallvoters
correspondstoasubsetofthesetofprojects(i.e.,voter𝑣 𝑖 submits providecompleteballots.Inaballotwith𝑚candidatesapartial
anapprovalballot,alsodenotedby𝑣 𝑖,suchthat𝑣 𝑖 ⊆𝑃). voteiscasewherevotergivespreferencesonlyover𝑗 candidates,
3

where1≤ 𝑗 <𝑚[12].Ourgoalistocreateandstudyalgorithms Offlinesetup-Analgorithmfortheofflinesetupoperatesasfol-
|     |     |     |     |     |     | lows:first,foreachvoter𝑣 | ∈𝑇𝑉,thealgorithmchooses𝑘projects |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------ | -------------------------------- | --- | --- |
that,whengivenapartialballotasaninput,willproduceoutput
asallvotershavingcompletelyfilledouttheirballots.Specifically, ofitschoice(possiblybytakingintoconsiderationtheballotsof
weassumethateachvoterisassociatedwithasetofapproved 𝐿𝑉,intuitivelyassumingsomesimilaritybetweenvotersin𝐿𝑉 and
candidates,asetofdisapprovedcandidates,andasetofcandidates 𝑇𝑉 in𝐼)andmovestheminto𝐸,inawaythat𝐼1agreeswith𝐼.
wherethevoter’sstandisunknown.Formally,voter𝑣 ∈{𝑣 ,...,𝑣 𝑛} Then,thealgorithmhastopredicttherestoftheballots-𝐻 for
1
| hasanapprovalset𝐴 |     | ⊂𝑃,adisapprovalset𝐷 |     | ⊂𝑃            |            | eachvoter𝑣 | ∈𝑇𝑉. |     |     |
| ----------------- | --- | ------------------- | --- | ------------- | ---------- | ---------- | ---- | --- | --- |
|                   |     | 𝑣                   |     | 𝑣             | andahidden |            |      |     |     |
| setdenotedby𝐻     |     | 𝑃.Notethat𝐴         | +𝐷  | +𝐻 𝑃.Wedenote |            |            |      |     |     |
𝑣 ⊂ 𝑣 𝑣 𝑣 = Onlinesetup-Analgorithmfortheonlinesetupoperatesas
|     |     |     |     |     |     | follows:first,foreachvoter𝑣 |     | ∈𝑇𝑉,thealgorithmproceedsin𝑘it- |     |
| --- | --- | --- | --- | --- | --- | --------------------------- | --- | ------------------------------ | --- |
thatthemergeofapprovedanddisapprovedcandidatessetsisan
exposedset𝐴 𝑣∪𝐷 𝑣 =𝐸 𝑣 ,𝐸 𝑣 ∈𝑃. erations,whereineachiterationthealgorithmcanchoose1project
ofitschoice(possiblybytakingintoconsiderationtheballotsof𝐿𝑉
Example2.4. ConsideraninstanceofPBwithpartialballotswith aswellastheresultsofthepreviousiterations,intuitivelyassum-
3projects:𝑝 1,𝑝 2,and𝑝 3;andwith2voters:𝑣 1and𝑣 2.Letitbethat ingsomesimilaritybetweenvotersin𝑇𝑉 and𝐿𝑉 in𝐼
andusing
𝑣 1providesafullballotinwhichsheapprovesallprojects,while𝑣
|                                           |     |     |     |                | 2   | therevealedpreferencesofthepreviousiterations)andmovesit |     |     |     |
| ----------------------------------------- | --- | --- | --- | -------------- | --- | -------------------------------------------------------- | --- | --- | --- |
| providesapartialballotinwhichsheapproves𝑝 |     |     |     | 1,disapproved𝑝 |     |                                                          |     |     |     |
|                                           |     |     |     |                | 2   | into𝐸,inawaythat𝐼1agreeswith𝐼.Then,thealgorithmhas       |     |     |     |
anddoesnotprovideherpreferenceregarding𝑝
|     |     |     |     | 3.Wedenotesuch |     | to predict | the rest of the ballots | -𝐻 for each voter𝑣 | ∈ 𝑇𝑉. A |
| --- | --- | --- | --- | -------------- | --- | ---------- | ----------------------- | ------------------ | ------- |
asettingasfollows:𝑃 ={𝑝 ,𝑝 ,𝑝 },𝑉 ={𝑣 ,𝑣 },𝐸 ={𝑝 ,𝑝 ,𝑝 }, moreintuitiveexpositionofthesealgorithmstaskscouldbethe
|     |     | 1 2 3 |     | 1 2 1 | 1 2 3 |     |     |     |     |
| --- | --- | ----- | --- | ----- | ----- | --- | --- | --- | --- |
𝐴 = {𝑝 ,𝑝 ,𝑝 }, 𝐷 = ∅, 𝐻 = ∅, 𝐸 = {𝑝 ,𝑝 }, 𝐴 = {𝑝 }, following:imagine𝑛votersprovidingtheirapprovalballotswhere,
| 1   | 1 2 3 1 | 1   | 2   | 1 2 | 2 1 |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
𝐷 ={𝑝 },𝐻 ={𝑝 }. pictorially,eachvoterhas𝑚cards,onecardforeachproject,on
| 2 2 | 2 3 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
whichthevoterwritestheirapproval/disapprovalpreference.Then,
2.4 AlgorithmicTasks somevoters(thosein𝐿𝑉)showalltheircards;whileothers(those
in𝑇𝑉)initiallydonotshowtheircardsatall.Intherandomsetting,
Weconsiderthreeslightlydifferentalgorithmictasks,correspond-
eachsuchvotershows𝑘cardsatrandomtothealgorithm;inthe
ingtodifferentwaysinwhichvotersmayinteractwithourenvi-
sionedapplication,ortodifferentassumptionsregardingthepartial offlinesetting,thealgorithmcanchoose,foreachsuchvoter,aset
of𝑘cardsthatthealgorithmwantstosee;andintheonlinesetting,
ballots.Inallthreevariants,weassumesomeidealinstanceofPB
containing𝑛voters,allofwhichprovidefullballots;denotethis thealgorithmcaniterativelyasksforafirstcard,asecondcard,
untila𝑘thcard,toseefromeachsuchvoter.Finally,thealgorithm
instanceby𝑖𝑑𝑒𝑎𝑙.Intuitively,inthealgorithmictasksweconsider,
ourgoalistoestimate𝑖𝑑𝑒𝑎𝑙,howeverthealgorithmswedesign shallpredictallofthehiddencards.Illustrationsofthedifferent
donothaveaccessto𝑖𝑑𝑒𝑎𝑙 butonlytoaPBinstancewithpartial settingscanbeseeninFigure2.
with𝑖𝑑𝑒𝑎𝑙
| ballotsthatagrees |     | (aPBinstancewithpartialballots |     |     |     |     |     |     |     |
| ----------------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- |
issaidtoagreewithsomePBinstancewithfullballotsifallthe
3 SOLUTIONARCHITECTURE
providedpreferencesagree;intuitively,ifitispossibletocomplete
thepartialinstancetobeequaltotheidealinstance). Inthissectionwediscussthearchitectureofoursolution,which
consistsofthreemodules:samplingmodule,predictionmodule
Example 2.5. Consider an ideal instance 𝐼 with projects 𝑃 = andvotingruleimplementation.Agraphicalrepresentationofour
{𝑝 ,𝑝 ,𝑝 ,𝑝 }andonevoter𝑣 1whereherexposedset𝐸 ={𝑝 ,𝑝 }. solutionarchitectureisgiveninFigure3.
| 1 2 3 | 4   |     |     |     | 1 2 4 |     |     |     |     |
| ----- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
ConsideraPBinstancewithpartialballots,denotedby𝐼1,with Asmentioned,weproposeacomputationalsolutionforPBwith
| onevoter𝑣 | ′ thatprovidesapartialballot,andlet𝐴 |     |     |     | {𝑝       |                                                         |     |     |     |
| --------- | ------------------------------------ | --- | --- | --- | -------- | ------------------------------------------------------- | --- | --- | --- |
|           |                                      |     |     | 1   | = 2 }and | partialballots,wheresomevotersdonotcompleteballots.Aswe |     |     |     |
1
𝐷 =𝑝 1.Then,𝐼1agreeswith𝐼. wanttocontroltheamountofinformationtogatherfromvoters,
1
wedefinealevelofpartialityashowsparseisourPBandhowwe
Todescribeouralgorithmictasks,considersomeidealinstance dividethelevelofpartialityto𝐿𝑉 and𝑇𝑉.
| 𝐼 withaset𝑉 | of𝑛voters.Then,consideraninstanceofPBwith |     |     |     |     |     |     |     |     |
| ----------- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
partialballots𝐼1thatisconstructedbyfirstpartitioningtwogroups
ofvotersLearningVoters-𝐿𝑉 andTargetVoters-𝑇𝑉.Intuitively,𝐿𝑉 3.0.1 Partialitylevel,SamplingDegreeandLVDegree. ThePartial-
arevotersthatalreadyprovidedtheirfullballotsand𝑇𝑉 itylevelofaPBdenotedbysampledegreeasthepercentageofdata
arevoters
collectingfromthevotersparticipateinPB.WedenoteLVDegree
| that provides | partial | ballots. Consider | the | voters in𝑇𝑉 | and set |     |     |     |     |
| ------------- | ------- | ----------------- | --- | ----------- | ------- | --- | --- | --- | --- |
asthelevelofcollecteddatathatassociatedwith𝐿𝑉.Asthelevel
theminitiallysothat𝐸=∅;i.e.,suchthattheydonotprovideany
ofsamplingDegreeincreases,votersarerequestedtoprovidemore
preference.Theoverarchinggoalofouralgorithmsistoestimate𝐼
dataandasthelevelofLVDegreeincreasesthe|𝐿𝑉|isincreases.
from𝐼1.Eachofthethreealgorithmictasksweconsiderdifferentiate
bytheallowedoperationsthatthealgorithmcanperformon𝐼1to
reachthisgoal,asdescribednext: Example3.1. WhereSamplingDegreeis1itmeansthatthePB
Randomsetup-Analgorithmfortherandomsetupoperates iscomplete,allvotersfilledtheirballots.WhenSamplingDegreeis
asfollows:first,foreachvoter𝑣 ∈𝑇𝑉,thealgorithmchooses𝑘 0.5andLVDegreeis1itmeansthat50%ofvotesareknownandall
projectsuniformlyatrandomandmovestheminto𝐸,inawaythat
ofthemarepartoffullindividualballots.WhenSamplingDegreeis
| 𝐼1agreeswith𝐼 | (possiblydifferent𝐸foreachvoter𝑣 |     |     |     | ∈𝑇𝑉).Then, |     |     |     |     |
| ------------- | -------------------------------- | --- | --- | --- | ---------- | --- | --- | --- | --- |
0.5andLVDegreeis0.1itmeansthat50%ofvotesareknownand
thealgorithmhastopredicttheresttheballot-𝐻 foreachvoter 10%ofthemarepartoffullindividualballotsand90%areequally
| 𝑣 ∈𝑇𝑉. |     |     |     |     |     | dividedbetween𝑇𝑉. |     |     |     |
| ------ | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- |
4

| (a) The random   | setting -  | the algorithm |     |     |     |     |
| ---------------- | ---------- | ------------- | --- | --- | --- | --- |
| chooses randomly | 𝑘 projects | from each     |     |     |     |     |
votertoexposed.
(b)OfflineSetting-thealgorithmchoosesasetof𝑘projectsthat
itasksforeachvotertoexpose.
Figure3:Architecture:startingwithsamplingalgorithm-
asthewaywecollectpreferencesfromvoters-gainpartial
ballot;thenfillingthemissingvotesbyapplyingprediction
module;implyingvotingruletooutputthepredictedwin-
ningbundle.
|     |     |     | 3.1.1 AlgorithmsfortheRandomSetup. |     | Recallthatanalgorithm |     |
| --- | --- | --- | ---------------------------------- | --- | --------------------- | --- |
forthissetupcannotchoosethe𝑘projectsforwhichthevotersin
𝑇𝑉 providepreferencesfor;thus,theonlyoperationthatsuchan
algorithmdoesistopredicttheremainingpreferencesofthevoters
|     |     |     | in𝑇𝑉,basedonthepreferencesofvotersin𝐿𝑉 |                                                |     | andthepreferences |
| --- | --- | --- | -------------------------------------- | ---------------------------------------------- | --- | ----------------- |
|     |     |     | in𝐸 =(𝐸                                | ,...,𝐸 𝑛)bypredictionmethodsdiscussedinSection |     |                   |
|     |     |     | 𝑇𝑉                                     | 1                                              |     |                   |
2.1.
|     |     |     | 3.1.2 AlgorithmsfortheOfflineSetup. |     | Recallthatanalgorithmfor |     |
| --- | --- | --- | ----------------------------------- | --- | ------------------------ | --- |
(c)OnlineSetting-thealgorithmchoosesiteratively𝑘projects
|                                 |     |     | thissetupfirsthastochoose,foreach𝑣 |     | ∈𝑇𝑉,aset𝑘 |            |
| ------------------------------- | --- | --- | ---------------------------------- | --- | --------- | ---------- |
| thatitasksforeachvotertoexpose. |     |     |                                    |     |           | ofprojects |
to“reveal”(tosetas𝐸);and,onlythen,topredicttheremaining
preferencesofthevotersin𝑇𝑉,basedonthepreferencesofvoters
Figure2:AlgorithmicTasks.
|     |     |     | in𝐿𝑉 and | the preferences | in 𝐸 𝑇𝑉 = (𝐸 ,...,𝐸 | 𝑛) by prediction |
| --- | --- | --- | -------- | --------------- | ------------------- | ---------------- |
1
methodsdiscussedinSection2.1.
• Revealingbypopularity
3.1 AlgorithmicSolutions Herethealgorithmchoosesthetop𝑘popularprojectsofthe
|     |     |     | votersin𝐿𝑉 | andsetthe𝐸ofeachvoter𝑣 |     | ∈𝑇𝑉 |
| --- | --- | --- | ---------- | ---------------------- | --- | --- |
Wedescribeseveralalgorithmicsolutionsforeachofthesetupswe toinclude
consider,namelyfortherandomsetup,theofflinesetup,andthe exactlythose.(I.e.,itsets𝐸={𝜎 1 ,...,𝜎 𝑘}foreach𝑣 ∈𝑇𝑉.)
onlinesetup. • Revealingbyconsensus
5

Herethealgorithmchoosesthe𝑘projectsmostinconsensus around10%ofprojectproposalswereapprovedineveryPB,the
| amongthevotersin𝐿𝑉 | andsetthe𝐸ofeachvoter𝑣 | ∈𝑇𝑉 |     |     |     |     |
| ------------------ | ---------------------- | --- | --- | --- | --- | --- |
exactpercentageisdetailedinTable1.
| toincludeexactlythose.(I.e.,itsets𝐸={𝛾 |     | ,...,𝛾 |     |     |     |     |
| -------------------------------------- | --- | ------ | --- | --- | --- | --- |
1 𝑘}foreach
| 𝑣 ∈𝑇𝑉.) |     |     | Table1:Descriptionofusedreal-worlddatasets. |     |     |     |
| ------- | --- | --- | ------------------------------------------- | --- | --- | --- |
• Revealingbycontroversiality
Herethealgorithmchoosesthe𝑘projectsleastinconsensus
|                                        |                        |           | PB          | Voters Projects | Budget Approvedproposals[%] |      |
| -------------------------------------- | ---------------------- | --------- | ----------- | --------------- | --------------------------- | ---- |
| amongthevotersin𝐿𝑉                     | andsetthe𝐸ofeachvoter𝑣 | ∈𝑇𝑉       |             |                 |                             |      |
|                                        |                        |           | Wola2022    | 9256 94         | 524020                      | 9.5  |
| toincludeexactlythose.(I.e.,itsets𝐸={𝛾 |                        | ,...,𝛾    |             |                 |                             |      |
|                                        |                        | 𝑚−𝑘 𝑚}for | Ursynow2022 | 6672 107        | 5614506                     | 10.7 |
each𝑣 ∈𝑇𝑉.)
|     |     |     | Wola2021         | 8647 107 | 465432  | 9.8  |
| --- | --- | --- | ---------------- | -------- | ------- | ---- |
|     |     |     | Praga-Polnoc2022 | 2614 90  | 2432952 | 12.5 |
Theintuitionforthisprocedureisthattheprojectsleastin
|     |     |     | Praga-Poludnie2022 | 10424 96 | 6643832 | 10.6 |
| --- | --- | --- | ------------------ | -------- | ------- | ---- |
consensuscorrespondtothoseprojectsthatarethehardest
|     |     |     | Wawer2021 | 4662 100 | 2493341 | 9.1 |
| --- | --- | --- | --------- | -------- | ------- | --- |
topredict.
|     |     |     | Bielany2020 | 8003 108 | 4321791 | 7.7 |
| --- | --- | --- | ----------- | -------- | ------- | --- |
|     |     |     | Wawer2022   | 5045 111 | 2807253 | 7.8 |
3.1.3 AlgorithmsfortheOnlineSetup. Recallthatanalgorithmfor Wola2023 6760 67 5663326 15.3
thissetupfirsthastochoose,foreach𝑣 ∈𝑇𝑉,aset𝑘 Targowe2022 4940 87 4585180 10.7
ofprojects
to“reveal”(tosetas𝐸);and,onlythen,topredicttheremaining
preferencesofthevotersin𝑇𝑉,basedonthepreferencesofvot-
Table2:Voter’sandproject’sattributesspace.
ersin𝐿𝑉 andthepreferencesin𝐸.But,incontrasttotheoffline
setting,thealgorithmcanchoosethese𝑘projectsadaptively.We
consideronewayofchoosingthe𝑘projectstoreveal,adaptively,
|     |     |     | Voter’sAttributes |     | Project’sAttributes |     |
| --- | --- | --- | ----------------- | --- | ------------------- | --- |
namely:adaptivecontroversial.Thealgorithmproceedsin𝑘itera-
|     |     |     |     | Age | Cost |     |
| --- | --- | --- | --- | --- | ---- | --- |
tions,whereineachiterationitcomputesthemostcontroversial
|     |     |     |     | Gender | Category |     |
| --- | --- | --- | --- | ------ | -------- | --- |
project.(Notethat,indeed,thisprocedureissimilartotherevealing
|     |     |     | VotingMethod |     | Populationsegments |     |
| --- | --- | --- | ------------ | --- | ------------------ | --- |
bycontroversialityprocedureoftheofflinesetting,howeverhere
itisdoneiterativelyandadaptively.)Afterusingtheadaptivecon-
troversialprocedure,wepredicttheremaininghiddenpreferences,
5 EVALUATION
usingpredictionmethodsdiscussedinSection2.1.
Inordertoevaluateourpredictionsmethodswedividedourdataset
3.1.4 VotingRule. Afterweperformthepredictingmodulewe into3sets:Train-set,Validation-setandTestset.
holdafullballot,wenowchosegreedyapprovalasavotingrule.
Inourresearchcontext,thetrain-setisthedatathatwecollected
AsdescribedinSection2.2.5forthisvotingsystem,eachvoteris
fromvotersregardingtheirvotes.Thevalidationsetispredefined
abletovoteforasmanycandidatesastheychoose,butcannot
setofvotesfromclosedsetofvoters,thesevotesareusedtotune
voteforthesamecandidatetwice.Thealgorithmthenbeginswith
thehyperparametersofamodel.Wedenotedthatthevalidation
thecandidatewhohasthemostnumberofvotesandselectsthem. setsize is15% ofeach data set. Thetest-set isthecollection of
Eachsubsequentcandidateischosenuntilthetotalnumberofvotes votesthatweusetoevaluateourmodel,thesevotesarethevotes
reachesthedesiredthreshold.Theaimofthissystemistomaximize
thatwedidnotcollectedfromthevoters.AsmentionedinTable4,
theamountof“approval”giventothechosencandidatesbythe
thePBdatasetsareimbalanced,thiscanleadtobiasedresultsand
voters[25].Hence,weoutputthepredictedwinningbundlewith
suboptimalperformanceofourpredictingmodels,asthemodelis
respecttoagivenbudget. morelikelytopredictthemajorityclass.Weaddressthisissueby
modifyingthemodellossfunctiontogivemoreweighttominority
4 DATASETS
classsamples.
Wehaveusedareal-worlddatasetscomingforapublicrepository, Wedivideourevaluationmethodsintotwosections:theclassifi-
namelyPabulib[10],apublicrepositoryfordataregardingreal- cationaccuracymetricsinwhichanalyzethefullpredictedballots
andBundleevaluationmetricsthatanalyzethefinalpredictedbun-
worldinstancesofparticipatorybudgeting,mainlyfromseveral
dle.
Europeancities.Inparticular,wehaveusedthedataconcerning
thePBprocessindifferentdistrictsfromWarsaw,Poland.Outof
5.1 ClassificationAccuracyMetrics
thisopenlibrarywecollectedtenPBthattookplacefrom2020to
2023.Table1detailstheamountofvoters,amountofprojectsand Toanalyzeouralgorithms,weconsideredavarietyofclassification
budgetforeachPB.Table2detailstheattributesofPB’svotersand accuracymetrics,namely:precision,recallandf1[20,23].They
projects.EachPBinstanceconsistvotersandprojects(theprojects measuretheamountofcorrectandincorrectclassificationandare
correspondtodifferentproposalstoimprovethedevelopmentof derivedfromconfusionmatrix.Theconfusionmatrixholdsthefol-
Warsawinseveraldomainssuchas,e.g.,education,environment lowingmeasures:TheacronymTP,FN,FP,andTNoftheconfusion
protection,publictransportation,etc.).Theproposalsarealsoaimed matrix cellsreferstothefollowing:TP=truepositive,thenum-
fordifferentsegmentsofthecitypopulation,e.g.children,adults, berofpositivecasesthatarecorrectlyidentifiedaspositive,FN
seniors,andpeoplewithdisabilities.Notethatacertainproposal =falsenegative,thenumberofpositivecasesthataremisclassi-
canconsistmultipletopicsandpopulationsegments.InallPBsthe fiedasnegativecases,FP=falsepositive,thenumberofnegative
percentageofvoter’sapprovedprojectproposalsisnaturallysmall, casesthatareincorrectlyidentifiedaspositivecases,TN=true
6

negative,thenumberofnegativecasesthatarecorrectlyidentified
asnegativecases[20,23].Precision,definedas𝑇𝑃/(𝑇𝑃 +𝐹𝑃),in
RScontextistheratioofthenumberofrelevantrecommended
itemstothetotalnumberofrecommendeditems[20,23].Recall,
definedas𝑇𝑃/(𝑇𝑃 +𝐹𝑁),istheratioofrelevantrecommended
itemstothenumberofrelevantitems.Thesetwometrics,sharean
inverserelationshipbetweenthem.Precisionandrecallarenotsen-
Figure4:TreatmentMatrix-pleaseseeSection6.
sitivetochangesindatadistributions.Aperfectmodelwillcapture
allpositiveexamples(Recall=1),andscoreasonlytheexamples
thatareinfact(Precision=1),fromananalyticalpointofview
itisdesirabletoincreaserecallwithoutsacrificingaccuracy.𝐹
1
datasetasdetailedinFigure4for50times.Weassumethatthemore
datawecollected,highersampledegreeinourcontext,thecloser
measurecombinesrecallandprecisionasharmonicmeanofthem,
𝐹 1 = (2∗𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛∗𝑟𝑒𝑐𝑎𝑙𝑙)/(𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+𝑟𝑒𝑐𝑎𝑙𝑙) andissuitable wewillbetothetruerealballotresults.Inparticular,weassume
thattheFAscorewouldincreaseasthesampledegreeincrease
measureforanimbalanceddata[23].
andtheSDwoulddecreasethesampledegreeincreaseforeach
5.2 Bundleevaluationmetrics setupforeveryPB.Hence,weconductedasanitytesttocheckthis
assumption.
Eventually,wehaveinterestincomputingthebundleofwinning
Everyalgorithmicsetupholdsdifferentlevelofinterventionin
projectsthatwasdecidedbythevoters,i.e,thelistofprojectsthat
selectingtheprojectproposalstocollect;inthe’Random’setupthe
’won’andwouldbeimplemented.Asanevaluationmethodwe
algorithmhasnopoweratallinchoosingwhichprojectproposals
compared the bundle from the ’real’ votes to the bundle of the
preferences to collect, in the offline setups it has the power to
’predicted’votes.ThiscomparisonhasdonebycomputingtheSym-
choose𝐾 projectproposalsbasedongroupofvotersthatprovided
metricDistancebetweenthetherealbundle(rb)andthepredicted
fullballots(LVgroup)andfortheonlinesetupithasthepowerto
bundle(pb).
chooseprojectproposalsbasedonallvoterspreferencesitteratively.
5.2.1 SymmetricDistance. Symmetricdistance(SD)isadistance Weassumethatthemore’power’thealgorithmicsolutionholdthe
measurethatsatisfiesthepropertyofsymmetry,whichstatesthat betteritwouldperformbetter(higherFAscoreandlowerSD).
thedistancebetweentwopointsisthesameinbothdirections. Hence,foreveryPBwecomparedallsetupsandalgorithmic
Formally,giventwopointsxandy,aSDfunctionfsatisfiesthe solutionspersampledegree.Additionally,weimplementedaper-
equation f(x,y) = f(y,x). Consider several toy examples: The SD formancetestinwhichwecomparedoursolutionswithanaive
between𝑟𝑏 = {1,2,3} and𝑝𝑏 = {2,1,3} is 0. The SD between samplingprocedure.Thissamplingprocedureisthecasewhere
𝑟𝑏 ={1,2,3}and𝑝𝑏 ={1,3,4}is1.TheSDbetween𝑟𝑏 ={1,2,3} LVdegreeisequalto1foracertainsampledegree.Notethatin
and𝑝𝑏 ={1,4,5}is4. samplingprocedureonlypartofcommunity(sampledegreetobe
exact)sharetheirpreferences,incontrasttoourproposedsolutions
5.2.2 FractionalAllocationscore. Anothermetricweusetoeval-
whereeveryvoterhasatleast𝐾 projectproposalstoshareher
uatethebundleis’FractionalAllocation’(FA)Score;Wedenote
opinionon.Inordertogenerateitwerandomlysampledvotersfor
FAscoreasthesumcostsofprojectsthatwerepredictedproperly
eachPBforeachsampledegreefor50timesandcalculateitsFA
dividedbythecostlimit-budget.
andSD.
Definition5.1(FractionalAllocation(FA)Score). Wedefinethe
fractionalallocationscoretobe:𝐹𝐴=
𝐵
𝜆,𝜆=(cid:205)
𝑝∈𝑝𝑏∩𝑟𝑏
𝑐𝑜𝑠𝑡(𝑝) 7 RESULTS
Inthissectionwedescribeanddiscussourresultsfortheprediction
6 EXPERIMENTS
module, for the sampling module, and for the architecture as a
Inthissectionwedescribetheexperimentsweconductedonthe whole.
real-worlddata-setspresentedinTable1.Webeganwithdefining FirstweperformedasanitychecktotesthowthesampleandLV
thepartialitylevelsoftheexperiment,wedefinedmultiplelevelsin degreeseffectonFAscoresandSD.WecalculatedtheaverageFA
ordertoconductseveralexperimentswithdifferentSampledegree scoresandSDforallPB’sforeachcombinationofsampledegree
andLVdegreeasmentionedinSection3.0.1.Therangeofsample and LV degree as described in Figure 4. The sanity test results,
degreesis0.1,0.15,0.3,0.5,0.7and0.9andtherangeofLVdegrees showninFigures5and6,showedthatinmostLVdegrees,asthe
is0.1,0.2,0.3,0.5,0.7,0.9and1.WhenLVdegreeisequalto1itrep- sampledegreeincreasestheFAscoreincreasesaswellandtheSD
resentthecaseofsamplesizeofthespecificSampleDegree.After isdecreases,asassumed.
weestablishedtheframeoftheamountsofinformationwewould Furthermore,itcanbeobservedthatastheLVdegreeincreases
collectfromthevoters,weusedeachofoursamplemodules(Ran- theFAscore/SDincreases/decreasesaswell,bymeansthepredic-
dom,Offline-popularity,Offline-controversial,Offline-consensus tionmodulesperformbetterwhenalargergroupofvotersprovide
andOnline)togatherthepreferencesfromvoters.Weperformed theirfullballots.
eachsamplemoduleonallsampledegree-LVdegreecombination InFigures7-12wecanseetheFAscoresperformanceofevery
for20times.ThisprocedurewasexecutedonallPBdatasets. setupasfunctionofLVdegreeandsampledegreeincludingacom-
Thenweperformedeachpredictionmoduleontheeachoffamily parisontosamplingmethod(LVdegreeequalsto1).Itseemsthatin
ofsampledegreeandLVdegree.Wedidthisprocedureonevery somesettingssomeofoursolutionssucceedbetterthanasampling
7

scores,Classification-onlineandClassification-offline-popularity
setupsperformbestforallsampledegrees.
8 CONCLUSIONSANDOUTLOOK
Wehaveproposedtheuseoftechniquesfrommachinelearning
andrecommendationsystemstotackletheinformationoverload
probleminparticipatorybudgeting.Technically,wehavedeveloped
amoreofPBwithpartialballotsthatisusefulforourcontext,de-
signedseveralalgorithmicsolutionsfordifferentspecificprediction
settings,andreportedontheresultsofcomputer-basedsimula-
tionsshowingthehighqualityofpredictionwithrespecttovoter
Figure5:Sanitytest-heatmapofFAscoresasfunctionof ballotsandthewinningbundlesthatthealgorithmsachievefora
SampledegreeandLVdegree. real-worlddata.Weconductedourexperimentson10real-world
PBandeliminatedsomepreferencestosimulatePBwithpartial
ballots.Thiseliminationofpreferenceswereconductedundercon-
trolledandstructuredmanner,definedassamplingmodule.After
wecreatedthesepartialballotsweimplementedpredictionmodule
topredictthemissingpreferences.Thenwecalculatedthewinning
bundleusinggreedyapprovalvotingrule.Weevaluateoursampling
andpredictionmodulesbycomparingthewinningbundlestothe
realones.Thecomparisonweredefinedbysymmetricdistanceand
FractionalAllocationscore,asameasureofhowgoodthebudget
wasallocatedinthepredictedwinningballot.Exceptfromcom-
paringourownsolutionsbetweenthemselves,wecomparedthem
toanaivesamplingmethod.Wefoundthatsomeofoursolutions
performbetterfromsamplingmethod.Hence,althoughtakinga
Figure6:Sanitytest-heatmapofSDasfunctionofSample sampleofPBcommunityandextractwinningbundleoutofit’s
degreeandLVdegree. preferencesisquiteeasyandperformsrelativelygood,wepropose
solutionthattakeintoaccountallofPB’svotersandperformsbet-
terthansamplingmethods.So,oursolutionspermitallpotential
method.Specifically,forsampledegreeequalsto0.1(Figure7)all
votersinaPBtoexpresstheiropinionsregardingprojectproposals
solutionsexceptMF-online,MF-offline-popularityandFM-online
andprovideasolutiontotheinformationoverloadproblem.
producehigherFAscoresthansamplingmethod.Specificallythe
Someavenuesforfutureresearcharethefollowing:
Classification-onlineandClassification-off-popularitysetupsfor
sample deg equals to 0.1 perform better than sampling method • Adifferent,somewhatstrongersettingmaycorrespondto
forsampledegreeequalsto0.3.InFigure8itseemsthatourso- algorithmsthatinitiallygetaninstanceofPBwithpartial
lutionsperformnotasgoodasthesamplingmethod,exceptfrom ballotswhereallvoterpreferencesarehidden(i.e.,where
Classification-onlineandClassification-off-popularity.InFigure9 𝑇𝑉 =𝑉 and𝐸=∅forall𝑣 ∈𝑇𝑉).Designingandanalyzing
wecanseethatmoreofoursolutionsperformbetterorgoodas algorithms for this setting is of practical importance, as,
goodasthesamplingmethod,exceptfromClassification-onlineand inherently,aPBprocessstartswithonlycompletelyempty
Classification-off-popularity.InFigure10weseethattherandom ballots.Fromatechnicalpointofview,thiswouldnaturally
setups,forallpredictionmodules,outperformsandachievedrela- allow the algorithm consider more complex correlations
tivelyhighFAscores.Additionally,theClassification-off-popularity acrosstheelectorate.
gainedthemaximalFAscore,weachieveditforcollectinghalfof • Amoreinteractivesettingthatisworthconsideringmay
thevotes.Asforsampledegreeequalsto0.7and0.9itisnotsurpris- bethefollowing:first,thevoterrevealssomeofherpref-
ingthatoursolutionsgainedhighFAscores.Throughallsample erence,afterwhichthealgorithmestimatestherestofthe
degreesthesetupsthatperformbest,producethehigherFAscores, ballot(or,alternatively,onlythepreferencesofthevoter
aretheClassification-onlineandClassification-offline-popularity regardingsomefurtherprojectsnotyetrevealed).Then,the
setups,especiallyinthe0.1,0.15and0.3sampledegrees.Forhigher voterhasthepossibilitytoexaminethepredictionsdone
samplingdegreesallofoursolutionsperformbetterorgoodas bythealgorithmandto“correct”someofthem,inwhich
samplingmethods.Asweassumed,therandomsamplingmodule casethealgorithmcanfurtherupdateitsestimatesregarding
performworsethantheofflineandonlinesamplingmodules.Asfor theremainingprojects.Suchaninteractivecommunication
thepredictionmodules,itisshownthattheclassificationtechnique betweenavoterandtheenvisionapplicationmayleadto
performsbetterthantheRStechniques. resultsofhigherquality.
InFigures13-18representtheSDofeverysetupasfunctionof • WhileherewehaveconsideredthequitestandardPBsetting
LVdegreeandsampledegreeincludingacomparisontosampling ofapproval-basedcombinatorialPB,analyzingasimilarRS-
method. We see quite the same trend as we saw for for the FA orientedapproachfordifferentsettingsofPB(inparticular,
8

thoseinthesurveyofAzizandShah[2])isanaturalavenue APPENDIX
forfutureresearch. Weprovidesomefurtherplotsintheappendix.Figures7-12de-
• Whileweproposedcertainapproachestoaddressthepredic- scribetheFAscoresthatwereproducedforeverycombination
tionmodule,itwouldbeinterestingtoimplyothermachine of the algorithmic solutions, prediction module, LV degree and
learningtechniquestopredictvoter’sballot. sampledegreeasdescribeinFigure4.Theseheatmapsenableus
tocomparetheFAscoresbetweenthealgorithmicsolutions(ran-
REFERENCES
dom,offline-popularity,offline-consensus,offlinecontroversyand
[1] HarisAziz,BartonLee,andNimrodTalmon.2017.Proportionallyrepresentative online)andbetweenthepredictionmodule(MF,FMandbinary
participatorybudgeting:Axiomsandalgorithms.arXivpreprintarXiv:1711.08226
(2017). classification).Furthermore,wecomparebetweenoursolutions
[2] HarisAzizandNisargShah.2021. Participatorybudgeting:Modelsandap- acrossallLVdegreelevelstosamplingsolution,whereonlypartof
proaches.InPathwaysBetweenSocialScienceandComputationalSocialScience.
thevoterstakenintoaccount,itisthecasewhereLVdegreeequals
Springer,215–236.
[3] GerdusBenade,SwapravaNath,ArielDProcaccia,andNisargShah.2021.Pref- to1,whereeachfigurereferstodifferentsampledegree.
erenceelicitationforparticipatorybudgeting.ManagementScience67,5(2021), Figures13-18describethesamecomparisonsshownabovebut
2813–2827.
forSymmetricdistances(SD).
[4] JesúsBobadilla,FernandoOrtega,AntonioHernando,andAbrahamGutiérrez.
2013.Recommendersystemssurvey.Knowledge-basedsystems46(2013),109–
132.
[5] FelixBrandt,VincentConitzer,andUlleEndriss.2012. Computationalsocial
choice.Multiagentsystems2(2012),213–284.
[6] RobinBurke.2002.Hybridrecommendersystems:Surveyandexperiments.User
modelinganduser-adaptedinteraction12,4(2002),331–370.
[7] YvesCabannes.2004. Participatorybudgeting:asignificantcontributionto
participatorydemocracy.Environmentandurbanization16,1(2004),27–46.
[8] IvánCantador,MaríaECortés-Cediel,MiriamFernández,andHarithAlani.2018.
What’sgoingoninmycity?recommendersystemsandelectronicparticipatory
budgeting.InProceedingsofthe12thACMConferenceonRecommenderSystems.
219–223.
[9] TianqiChenandCarlosGuestrin.2016.Xgboost:Ascalabletreeboostingsystem.
InProceedingsofthe22ndacmsigkddinternationalconferenceonknowledge
discoveryanddatamining.785–794.
[10] NimrodTalmonDariuszStolicki,StanisławSzufa.2020.pabulibanopenPArtici-
patoryBUdgetingLIBrary.http://http://pabulib.org.
[11] AngelaEdmundsandAnneMorris.2000.Theproblemofinformationoverload
inbusinessorganisations:areviewoftheliterature. Internationaljournalof
informationmanagement20,1(2000),17–28.
[12] PeterEmerson.2013.TheoriginalBordacountandpartialvoting.SocialChoice
andWelfare40,2(2013),353–358.
[13] WulfGaertner.2009. Aprimerinsocialchoicetheory:Revisededition. Oxford
UniversityPress.
[14] DietmarJannach,MarkusZanker,AlexanderFelfernig,andGerhardFriedrich.
2010.Recommendersystems:anintroduction.CambridgeUniversityPress.
[15] YehudaKoren,RobertBell,andChrisVolinsky.2009.Matrixfactorizationtech-
niquesforrecommendersystems.Computer42,8(2009),30–37.
[16] BlerinaLika,KostasKolomvatsos,andStathesHadjiefthymiades.2014.Facing
thecoldstartprobleminrecommendersystems.ExpertSystemswithApplications
41,4(2014),2065–2073.
[17] IanMDLittle.1952. Socialchoiceandindividualvalues. JournalofPolitical
Economy60,5(1952),422–432.
[18] TomMMitchellandTomMMitchell.1997.Machinelearning.Vol.1.McGraw-hill
NewYork.
[19] SteffenRendle.2010.Factorizationmachines.In2010IEEEInternationalconference
ondatamining.IEEE,995–1000.
[20] FrancescoRicci,LiorRokach,andBrachaShapira.2011. Introductiontorec-
ommendersystemshandbook. InRecommendersystemshandbook.Springer,
1–35.
[21] JBenSchafer,DanFrankowski,JonHerlocker,andShiladSen.2007.Collaborative
filteringrecommendersystems.InTheadaptiveweb.Springer,291–324.
[22] JBenSchafer,JosephKonstan,andJohnRiedl.1999.Recommendersystemsin
e-commerce.InProceedingsofthe1stACMconferenceonElectroniccommerce.
158–166.
[23] GunnarSchröder,MaikThiele,andWolfgangLehner.2011.Settinggoalsand
choosingmetricsforrecommendersystemevaluations.InUCERSTI2workshopat
the5thACMconferenceonrecommendersystems,Chicago,USA,Vol.23.53.
[24] GuyShaniandAselaGunawardana.2011.Evaluatingrecommendationsystems.
InRecommendersystemshandbook.Springer,257–297.
[25] NimrodTalmonandPiotrFaliszewski.2019.Aframeworkforapproval-based
budgetingmethods.InProceedingsofAAAI’19,Vol.33.2181–2188.
[26] ChenWang,ChengyuanDeng,andSuzhenWang.2020.Imbalance-XGBoost:
leveragingweightedandfocallossesforbinarylabel-imbalancedclassification
withXGBoost.PatternRecognitionLetters136(2020),190–197.
[27] Yueping Zheng and Hindy Lauer Schachter. 2017. Explaining citizens’ E-
participationuse:Theroleofperceivedadvantages.PublicOrganizationReview
17,3(2017),409–428.
9

Figure11:HeatmapofFAforSampledegree=0.7. Figure7:HeatmapofFAforSampledegree=0.1.
Figure12:HeatmapofFAforSampledegree=0.9. Figure8:HeatmapofFAforSampledegree=0.15.
Figure13:HeatmapofSDforSampledegree=0.1.
Figure9:HeatmapofFAforSampledegree=0.3.
Figure14:HeatmapofSDforSampledegree=0.15.
Figure10:HeatmapofFAforSampledegree=0.5.
10

Figure15:HeatmapofSDforSampledegree=0.3. Figure17:HeatmapofSDforSampledegree=0.7.
Figure16:HeatmapofSDforSampledegree=0.5. Figure18:HeatmapofSDforSampledegree=0.9.
11