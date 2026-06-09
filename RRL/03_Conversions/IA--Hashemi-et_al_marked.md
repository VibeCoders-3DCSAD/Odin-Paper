A User-Centric Exploration of Axiomatic Explainable AI
in Participatory Budgeting.
MaryamHashemi AliDarejeh FranciscoCruz∗
SchoolofComputerScienceand SchoolofComputerScienceand SchoolofComputerScienceand
Engineering Engineering Engineering
UniversityofNewSouthWales UniversityofNewSouthWales UniversityofNewSouthWales
Sydney,Australia Sydney,Australia Sydney,Australia
m.hashemi@unsw.edu.au ali.darejeh@unsw.edu.au f.cruz@unsw.edu.au
ABSTRACT Melbourne,VIC,Australia.ACM,NewYork,NY,USA,5pages.https://doi.
ExplainableArtificialIntelligence(XAI)hasbeenwidelyusedto org/10.1145/3675094.3677599
clarifytheopaquenatureofAIsystems.OneareawhereXAIhas
gainedsignificantattentionisParticipatoryBudgeting(PB).PB 1 INTRODUCTION
mechanismsaimtoachieveaproperallocationconcerningboth
The field of Explainable Artificial Intelligence (XAI) focuses on
the votes collected based on user’s preferences and the budget.
elucidatingthereasoningbehinddecisionsorpredictionsfromAr-
An essential criterion for evaluating these mechanisms is their
tificialIntelligence(AI)systems,therebymakingAImodelsmore
abilitytosatisfydesiredpropertiesknownasaxioms.However,
understandableandtransparent[14],[7].Variousmotivationsfor
eventhoughtherearecomplexvotingrulesthatmeetsomeax-
usingexplanationsinAIalgorithmsarecitedintheliterature[8],[6].
ioms,concernsregardingtransparencypersist.Inthisstudy,we
Thesereasonsinclude:1-Generatingtrust(trustworthyAI).2-Meet-
proposeanapproachtoprovideexplanationsinaPBsettingby
inglegalrequirements.3-Upholdingsocialresponsibility,fairness,
treatingaxiomsasconstraintsandseekingoutcomesthatadhere
andriskavoidance.4-Creatingaccountableandreliablemodels.5-
totheseconstraints.Thismethodenhancessystemtransparency
Minimizingbiases.6-Validatingmodels.Toenhancetransparency,
andexplainability.Eachpotentialallocationisacceptedorrejected
several approaches have been proposed, such as feature impor-
based on whether it satisfies the axioms, and the linear nature
tance,whichidentifiesthemostinfluentialfeaturesinthemodel’s
oftheaxiomsreducescomputationalcomplexity.Weevaluated
decision-makingprocess[10],[12],andcounterfactualexplanations,
ourapproachwithreal-worlduserstoassessitseffectivenessand
whichinvolvegeneratingalternativescenarioswherethemodel’s
helpfulness.Ourpilotstudyshowsthatusersgenerallyfindex-
outputwouldchange[15],[13].Anothersignificantapproachisthe
planationshelpfulforunderstandingthesystem’sdecisionsand
axiomaticapproach,whichusesaxioms(asetofdesiredproperties
perceivetheoutcomesasfairer.Additionally,usersprefergeneral
andagreedvalues)tojustifytheoutcomes[9].Ourworkfocuses
explanationsovercounterfactualones.
ontheaxiomaticapproach,developingexplainabilitybasedonthis
methodforAIalgorithmsaimedatsolvingParticipatoryBudgeting
CCSCONCEPTS
(PB)problems.
•Human-centeredcomputing→EmpiricalstudiesinHCI;• PBisademocraticapproachtodeterminingtheallocationof
Appliedcomputing→Sociology;•Computingmethodologies fundsforpublicprojects[2].Inthissetofchallenges,weencounter
→Cooperationandcoordination. variousprojectswithassociatedcostsandalimitedbudget,typically
insufficienttocoverallprojects.Thegoalistodecidewhichprojects
KEYWORDS tofundandwhichtodismissbasedonthevotesofparticipants.In
ExplainableArtificialIntelligence;Users;SocialChoice;Participa- citiesworldwide,suchasParis,Sydney,andNewYork,residents
toryBudgeting. engageinparticipatorybudgetingtocollectivelydeterminethe
allocationofpublicfunds.Residentscastvotesonproposalsranging
ACMReferenceFormat: fromconstructingaplayground,repavingaroad,andplantinga
MaryamHashemi,AliDarejeh,andFranciscoCruz.2024.AUser-Centric
communitygarden,toinstallingnewstreetlights.Theoutcomeis
ExplorationofAxiomaticExplainableAIinParticipatoryBudgeting..In
shapedbycollectivevoting,determiningtheprojectsthatsecure
Companionofthe2024ACMInternationalJointConferenceonPervasive
fundingandthosethatdonot.
andUbiquitousComputing(UbiCompCompanion’24),October5–9,2024,
SeveralintricatemethodsexisttodetermineaPBoutcome,con-
∗AlsowithUniversidadCentraldeChile. sideringboththebudgetconstraintsandthevotes.Eachofthese
methodsadherestoasetofaxioms.Generally,mechanismsthat
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor satisfyahighernumberofaxioms,representingdesiredproperties,
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed aredeemed“better”andmorejustifiable.Therefore,axiomsserve
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation
ascriteriaforguidingtheallocationprocessandjustifyingthefinal
onthefirstpage.Copyrightsforthird-partycomponentsofthisworkmustbehonored.
Forallotheruses,contacttheowner/author(s). outcome.Procaccia[11]notesthataxiomscapturewhatisdesir-
UbiCompCompanion’24,October5–9,2024,Melbourne,VIC,Australia ableandshouldbeappliedtoexplainthemechanism’soutcome
©2024Copyrightheldbytheowner/author(s).
tovoters.Caillouxetal.[4]developedalogic-basedlanguageto
ACMISBN979-8-4007-1058-2/24/10
https://doi.org/10.1145/3675094.3677599 describethestrengthsandweaknessesofdifferentsingle-winner
126

UbiCompCompanion’24,October5–9,2024,Melbourne,VIC,Australia MaryamHashemi,AliDarejeh,&FranciscoCruz
votingrulesforvoters.Boixeletal.[3]viewfindinganargument • Feasibility:Thisaxiomsaysthatanoutcome𝐶 isfeasible
|     |     |     |     | ifandonlyif:(cid:80) |     | 𝑐𝑜𝑠𝑡(𝑐 ≤ 𝐵.Inotherwords,itsays |     |     |
| --- | --- | --- | --- | -------------------- | --- | ------------------------------ | --- | --- |
foranoutcomeasaconstraint-solvingprobleminsingle-winner 𝑐𝑘∈𝐶 𝑘)
settings,whereatripleof(variables,domain,constraints)needs thatthesummationofourspendingmoneyshouldnotbe
| definition. |     |     |     | beyondourbudget. |     |     |     |     |
| ----------- | --- | --- | --- | ---------------- | --- | --- | --- | --- |
Inourwork,forthefirsttime,wedesignedatransparentmecha- • Exhaustiveness[2]:Thisaxiomsaysthatafeasibleallocation,
nismbasedonaxiomstocalculateandexplaintheoutcomeofaPB 𝐶,isexhaustiveifitisimpossibletofundanymoreprojects
setting,andevaluatedtheeffectivenessofaxiomaticexplanation withtheleftoverbudget[1].Consideringoursettingchar-
onreal-worldusers.Theproposedapproachconsidersaxiomsas acterization(approvalvotingandnon-divisibledegreeof
constraintstobefulfilledandsystematicallyenumeratesalloca- completion),wecanformulateitas:
tionsthatmeettheseconstraints.Throughthisaxiomaticapproach, (𝐵−(cid:80) 𝑐𝑘∈𝐶 𝑐𝑜𝑠𝑡(𝑐 𝑘))<𝑐𝑜𝑠𝑡(𝑐′),𝑐′ ∈𝑋\𝐶
wecanautomaticallyprovidereasoningandexplanationsforeach • Utilitarianwelfare_consistentAxiom:Anallocation𝐶 ∈2 𝑋
chosenorexcludedallocationbasedonthecriteriaofwhetherthey isutilitarianwelfareconsistentifthereexistsno𝐶′ ∈ 𝑋
2
|     |     |     |     |     | 𝑖 = 𝑛 𝑢 𝑖(𝐶′)>Σ | 𝑖 = 𝑛 𝑢 𝑖(𝐶)[5].Thisaxiomstatesthat |     |     |
| --- | --- | --- | --- | --- | --------------- | ----------------------------------- | --- | --- |
satisfyaxiomsornot.Inthefollowingsection,wewillbrieflydis- suchthatΣ 𝑖 𝑖
|     |     |     |     |     | = 1 | = 1 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
cussparticipatorybudgetingmodeling,theaxiomsemployed,and anallocationthatcausesabiggerutilityispreferredtoother
| formulateourapproach.            |     |     |     | allocations.  |     |     |     |     |
| -------------------------------- | --- | --- | --- | ------------- | --- | --- | --- | --- |
| 2 PARTICIPATORYBUDGETINGMODELING |     |     |     | 3 METHODOLOGY |     |     |     |     |
EveryPBsettingscanbemodeledbythefollowingvariables,[1]: Leveragingaxiomstodetermineoutcomesofferstheadvantageof
transparency.Weemployedaxioms,whichrepresentagreed-upon
• Thefirstvariableisagents(alsoknownasresidentsorvoters)
thatwillbeshownasN={1,...,𝑛}.
values,toadvocateforfundingcertainprojectswhileproviding
• Thesecondvariableisthebudget(orresources).Weshow reasoningfortherejectionofothers.
thebudgetasB,whichisthemoneylimitationwecanspend Theproposedmechanismoperatesbasedonaconstraint-solving
onprojectsingeneral. problemframework,whichinvolvesanobjectivefunctionaimed
• at maximizing the number of funded projects, along with a set
Thereisalsoasetofprojects(alsoknownascandidatesor
| alternatives)asX={𝑥 | ,...,𝑥 |     |     |                                                        |     |     |     |     |
| ------------------- | ------ | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- |
|                     | 1      | 𝑚}. |     | oflinearconstraints.Weformulatedeachmentionedaxiomasan |     |     |     |     |
• Thenextconsiderationisthedegreeofcompletion,which integerlinearformandusedanIntegerLinearProgramming(ILP)
canbedividedintotwogeneraltypes:divisibleandnon- solvertofindallpossibleoutcomesthatmeetourconstraints.
divisible.Divisibleprojectscanbecompletedtodifferent Inthissetting,wepresenttheoutcomeoffundingtheprojectsas
|                                                        |     |     |     | 𝑋.If𝑥 =1meansthattheproject𝑗 |     | hasbeenfundedandif𝑥 |     | =0  |
| ------------------------------------------------------ | --- | --- | --- | ---------------------------- | --- | ------------------- | --- | --- |
| degrees(continuous).Inoursetting,alltheprojectsarenon- |     |     |     | 𝑗                            |     |                     |     | 𝑗   |
divisible.Itmeanstheyonlycanbecompleted100%(shown meansthatthisprojecthasnotbeenfunded.Basedonthat,the
| by1)or0(shownby0). |                                     |     |     | problemcanbeformulatedinILPasfollows: |     |     |     |     |
| ------------------ | ----------------------------------- | --- | --- | ------------------------------------- | --- | --- | --- | --- |
| • Eachproject𝑥     | ∈𝑋 hasanassociatedcostfunctionshown |     |     |                                       |     |     |     |     |
𝑚
| as:𝑐𝑜𝑠𝑡 : | 𝑋 −→ R+,and𝑐𝑜𝑠𝑡(𝑥 | 𝑗)indicatesthecostofthe |     |     |     | ∑︁𝑥 |     |     |
| --------- | ----------------- | ----------------------- | --- | --- | --- | --- | --- | --- |
|           |                   |                         |     |     |     | 𝑗   |     | (2) |
𝑗-thproject.
𝑗=1
| • Agents’ votes | demonstrate | how agents can express | their | subjectto: |     |     |     |     |
| --------------- | ----------- | ---------------------- | ----- | ---------- | --- | --- | --- | --- |
selection. In our setting, we use approval voting, which 𝑥 ∈[0,1] 𝑗 =0,1,...,𝑚,
𝑗 forall
meanseachvotercanapproveordisapproveofaproject
(shownby1or0,respectively).Weconsiderthatvotersare WeappliedourILPprobleminPython,Gurobioptimizer1.Gurobi
indifferentbetweenapprovedordisapprovedprojects.All Optimizerisaprescriptiveanalyticsplatformandadecision-making
| theapprovedprojects(shownby1)arestrictlypreferredto |     |     |     | technology. |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | ----------- | --- | --- | --- | --- |
notapprovedones(shownby0).Weshowourvotelistas
={𝑣𝑜𝑡𝑒1,...,𝑣𝑜𝑡𝑒𝑛}.𝑣𝑜𝑡𝑒𝑛
| 𝑉𝑜𝑡𝑒      |                                      | shows𝑛thvoterballetthat |     | 4 EXPERIMENTALUSERSTUDY |     |     |     |     |
| --------- | ------------------------------------ | ----------------------- | --- | ----------------------- | --- | --- | --- | --- |
| contains𝑚 | membersof1or0indicatingapprovementor |                         |     |                         |     |     |     |     |
Asthenextstepofourwork,wetestedtheproposedaxiomatic
disapprovmentofaprojectrespectively.
approachonreal-worlduserstoseehowtheseexplanationsworkin
Basedonthepreviousnotations,wecandefineaPBvotingrule practice.Morespecifically,westudiedwhetherpresentingreason-
asfollows: ingtouserswillbringmoretransparencyfromtheuserperspective
andhelpthemtobettertrustthesystem(trustworthiness).
𝑋, ∑︁
𝐹 :⟨𝑉𝑜𝑡𝑒,𝐵,𝑐𝑜𝑠𝑡(𝑥)⟩−→{𝐶|𝐶 ⊆2 𝑐𝑜𝑠𝑡(𝑐 𝑘)≤𝐵} Forinstance,inasimplescenario,theproposedapproachmight
(1)
𝑐𝑘∈𝐶 provideanexplanationlikethis:“Althoughyousupportedproject
Weshowanallocationas𝐶containingfunded𝑥 𝑗s,and𝑐𝑜𝑠𝑡(𝑐 A,morevotersvotedforprojectB.Consequently,fundingprojectB
𝑘)
|                                       |     |                      | 𝑋   | wouldresultingreateroverallsatisfactionamongvoters.Addition- |     |     |     |     |
| ------------------------------------- | --- | -------------------- | --- | ------------------------------------------------------------ | --- | --- | --- | --- |
| isafunctionthatmapsselectedprojects(𝑐 |     | 𝑘s)totheircosts,and2 |     |                                                              |     |     |     |     |
ally,ourbudgetconstraintspreventusfromfundingbothprojects.”
isallthepossibleallocations.
|     |     |     |     | In this example, | the proposed | axiomatic approach | employs | the |
| --- | --- | --- | --- | ---------------- | ------------ | ------------------ | ------- | --- |
Axiomsareagreed-uponvaluesthatwecanuseasthefounda-
|     |     |     |     | utilitarian welfare-consistent |     | axiom (preferring | allocations | that |
| --- | --- | --- | --- | ------------------------------ | --- | ----------------- | ----------- | ---- |
tionalprinciplesforourvotingmechanismanddeploythemas
maximizevoterutility)andfeasibility(ensuringthetotalproject
explanationsforusers.Inthefollowing,weintroducedtheaxioms
thatweusedforthepurposeofprovidingexplanations: 1https://www.gurobi.com/
127

AUser-CentricExplorationofAxiomaticExplainableAI
inParticipatoryBudgeting. UbiCompCompanion’24,October5–9,2024,Melbourne,VIC,Australia
costsstaywithinbudget)toidentifythemostsuitableallocation Uponcompletionofthesurvey,weproceededtothephaseof
whilegeneratingreasoningforalternativescenarios. datavalidationandanalysis,culminatinginthepublicationofour
Ouruserstudyprimarilyfocusesonassessingwhetherexplana- results.
tionsgeneratedbasedonaxiomsenhanceusers’comprehension
oftheoutcomesinthePBsetting.Ourargumentsregardingthe 4.1 SurveyStructure:
outcomederivefromtheoreticalmathematicalproperties,andit Wedesignedaquestionnairetoevaluateourhypothesisesregarding
remainsuncertainwhetherusersperceivethemasunderstandable. explainablePBsetting.Thequestionnaireisstructuredtomaintain
Forinstance,whileitistheoreticallypreferabletomaximizethe anonymity,gatheringonlyessentialdemographicinformationsuch
utilityfunction,itisunclearfromtheuser’sperspectivewhether as gender, age, participants’ country, and their familiarity with
thisargumentisunderstandable.Thesecondaryobjectiveofthis computers.Thisdatacollectionservestoexplorepotentialcorre-
studyistoexaminehowourexplanationsandjustificationsassist lationsbetweengender,thestageofdevelopmentofthecountry,
participantsin: thelevelofcomputerscienceknowledge,andhowparticipants
• Betterunderstandingthedecision-makingprocessofthe assessexplanations.Ourstudyinvolvedtwodistinctparticipatory
system, budgetingcases,eachwithdifferentscenarios.Eachparticipant
• Developinggreatertrustinthealgorithmandthesystem’s randomlyassignedtoonecaseandbasedontheirvote,explana-
decisions, tionsregardingonescenariopresentedtothem.Weonlyshowed
• Perceivingthesystem’soutcomesasfairerafterreceiving oneparticipatoryproblemtousersinordertopreventpotential
theprovidedexplanations experimentalconfusionandbias.Thetwoparticipatorybudgeting
casesareindependentofeachother.Randomly,wepresentedone
Duringthisassessment,weexaminedwhetherusersleantoward
casetoeachuserinawaythateachcaseisshown50%ofthetime.
personalizedexplanationsorcounterfactualexplanations.Onthe
Inthefollowing,wepresentedeachcaseandpossibleoptions
onehand,apersonalizedexplanationinvolvesprovidingreasoning
fortheusertovote.
forwhyaparticularoutcomewaschosen,offeringinsightintowhy
certainprojectswerefundedornotbasedontheuser’svotes.On
4.2 PresentedParticipatoryBudgetingCases:
theotherhand,acounterfactualexplanationstepsintotherealm
of "what if," clarifying how the outcome would change if other • CASE1:
participants’votesshiftedtoalignwiththeuser’spreferences.It’s Considerthereisabudgetof$11,000allocatedtotheDepart-
importanttonotethatthesetwotypes ofexplanationsoperate mentofComputerScience,andthedeanaimstoallocate
independentlyofeachother. thesefundstotwopotentialprojects:
Ourhypothesisesregardingthementionedquestionsarelisted (1) Buyingnewbooksforthedepartmentlibrarywithatotal
below: costof$10,000.
(2) Upgradingthecomputerlabs,incurringacostof$9000.
(1) Wehypothesizethatasexplanationswillhelpuserstobetter
Giventheavailablebudget,thedeancanonlyfundoneoutof
understandthedecisionofthesystem.
thesetwoprojects.Tofacilitatethisdecision-makingprocess,
(2) Wehypothesizethatourexplanationswillpavethewayand
thedeanhasappointedthreerepresentativesforthedepart-
helpuserstobettertrustthesystem.
ment,andyourroleistoserveasthethirdrepresentative,
(3) Wehypothesizethatourexplanationswillhelpusersper-
providingyourvote.
ceivetheoutcomeofthesystemasfairercomparedtositu-
ationswherewedonotprovideanyexplanation. WeconsideredthatthefirstandsecondrepresentativesareAlice
(4) Weanticipatethatuserspreferpersonalizedexplanations andBob.AliceandBobbothapprovedonlyacquiringnewbooksfor
overcounterfactualexplanations. thelibrary.Weareemployingthegreedyruleasourvotingmethod.
Basedonthisrule,wecountthenumberofpeoplewhovotedfor
Ouruserstudybeganwiththeacquisitionofhumanethicsre-
eachproject,andtheprojectthatearnedthemostapprovalwill
searchapproval2,anessentialstepinourstudyprotocol.Following
befunded.Theoutcomewillbebuyingnewbooksforthelibrary
this,wedisseminatedinformationaboutourresearchthroughMe-
regardlessofthevoter’svoteinthiscase.
chanicalTurk.
• CASE2:
Duringthedatacollectionphase,weengagedparticipantsby
SydneyCityCouncilhasallocated$1.1milliontoenhance
providinganoverviewofthestudyandobtainingtheirconsent
thecity,consideringthreepotentialprojects:
toparticipate.Subsequently,participantswerepresentedwithour
(1) Creatinganewparkwithacostof$1million.
participatorybudgetingproblemandaskedtovotebasedontheir
(2) Establishinganartcenterwithacostof$0.9million.
personalinterests.Basedonthecollectedvotes,thealgorithm’s
(3) Constructinganewshoppingcenterwithacostof$1.1
decisionwasrevealedtothem.
million.
Wethengaugedparticipants’perceptionsofthealgorithm’sclar-
Withtheavailablebudget,thecitycanonlyfundoneoutof
ityandtrustworthinessthroughaseriesofquestions.Participants
thesethreeprojects.Tomakethisdecision,theCityCouncil
werealsoprovidedwithautomatedexplanationsandjustifications,
hasselectedthreerepresentatives,andyourroleistobethe
followedbyinquiriesregardingthetransparencyofthesystem
thirdrepresentative,providingyourvote.
post-explanation.
WeconsideredthefirstandsecondrepresentativesareAliceand
2HCreferencenumber:iRECS5941 Bob.Theyboththinkthecityneedsanewparkforchildren,sothey
128

UbiCompCompanion’24,October5–9,2024,Melbourne,VIC,Australia MaryamHashemi,AliDarejeh,&FranciscoCruz
approvedthefirstprojectanddisapprovedothers.Weareusingthe
greedyruleasamethodofvoting.Basedonthisrule,wecountthe
numberofpeoplewhovotedforeachproject,andtheprojectthat
earnedthemostapprovalwillbefunded.So,inthisscenario,the
parkwillbefundedregardlessofthecollecteduser’svote.
Weexplainedtoourparticipantsthattheyhavetheoptionto
eitherapproveordisapproveofprojectsbasedontheirindividual
interests.Thereisnorestrictiononthenumberofprojectsthatcan
beapproved,butparticipantsmustapproveatleastoneproject.We
(a)Userunderstandingofthesys- (b)Userunderstandingofthesys-
thenexplainedthatwehadalreadycollectedvotesfromotherpar-
temdecision,case1. temdecision,case2.
ticipantsandaskedthemtoindicatetheirapprovalordisapproval.
Itwasmentionedthatallrepresentativevoteshadbeenprocessed
bythealgorithm.Followingtheirresponses,thesystem’sdecision
willbeprovided,alongwithexplanationsregardingthisdecision.
Subsequently,aseriesofquestionswillbepresentedtoassessthe
impactoftheseexplanations.
Aftertheusers’voteswerecollectedandtheoutcomeofthe
algorithmwasshowntothem,weaskedsomequestionsregarding
thetransparencyoftheoutcomeandtheleveloftheusers’trust
inthesystem.Inthenextstage,wepresentedexplanationsand
(c)Usertrusttothesystemdeci- (d)Usertrusttothesystemdeci-
reasoningbasedonaxiomstojustifytheoutcomeofthealgorithm.
sion,case1 sion,case2.
Followingthepresentationoftheseexplanations,weaskedfurther
questionstoassesstheeffectandperformanceoftheexplanations
ontheusers’understandingofthesystem.
5 RESULTS
Weconductedourpilotstudywith26users(male=16,female=10).
(e)Towhatextentusersfindthe (f)Towhatextentusersfindthe
62%participantsagedbetween25-34and23%agedbetween35-44. systemdecisionfair,case1. systemdecisionfair,case2.
Oftheparticipants,50%werefromIndia,42.3%fromtheUnited
States,andtherestfromvariouscountriessuchasItalyandSri
Figure1:Comparisonofuser’sreportregardingthetrans-
Lanka.Overall,42%participantsdescribedtheircomputerscience
parencyofthesystem’sdecision(firstrow),theirtrustto
literacyasadvancedand31%expert.
thesystem(thesecondrow),andthefairness(thethirdrow)
Mostoftheparticipants(72.4%)foundtheexplanationseither
beforeandafterreceivingexplanations.
extremelyhelpfulorveryhelpfulinunderstandingthesystem’s
decision.Additionally,63.3%oftheparticipantspreferredgeneral
explanationsovercounterfactualones.About30%ofparticipants
reportedthattheexplanationshadapositiveimpactontheirper-
6 CONCLUSIONANDFUTUREWORKS
ceptionofthesystem’sfairness.Noneoftheparticipantsreported
anegativeimpactfromtheexplanationsinthatmatter.However, Inthisstudy,wefocusedonprovidingexplanationsforAIalgorithm
wecouldnottdrawanymeaningfulconclusionsabouthowtheex- outcomesinPBsettings.Byusingaxioms(desiredproperties)aslin-
planationsaffectedusers’trustinthesystem.Insomecases(20%), earconstraints,weidentifiedallpossibleoutcomesthatmeetthese
providingtheexplanationsdecreasedthelevelofthetrustinusers. criteria,rulingoutanythatdonot.Wethentestedourapproach
27%ofparticipantsreportedanincreaseintheirleveloftrustin withreal-worlduserstoseeiftheexplanationswouldenhancetrans-
thesystemafterreceivinganexplanation,23%reportedadecrease parency,increaseusertrust,andimproveperceivedfairness.Our
intheirleveloftrust,and50%expressedthattheirleveloftrust resultsshowthatusersgenerallyfoundtheexplanationshelpfulfor
didnotchange.InFig.1,wepresenthowsystemdecisiontrans- understandingthesystem,improvingtransparencyandfairness.
parency,fairness,andusertrustinsystemdecisionschangebefore However,wecouldnotdrawadefinitivelinkbetweentrustinthe
andafterreceivingexplanationsforbothpresentedPBscenarios system’sdecisionsandtheexplanations.
inoursurvey,shownascase1andcase2.Weprovidedusersfive Next,wewillconductanextensiveuserstudywithasubstantial
optionstochoosefromforeachcriterionoftransparency,trust, numberofparticipantstoverifyourfindingsandgaindeeperin-
andfairness.Asshown,userunderstandingofthesystem(system sightsintotheexplainablePBsetting.Additionally,wewillexplore
transparency)andperceivedfairnessimprovedinbothcasesafter thereasonsbehindinstanceswhereprovidingexplanationsreduced
receivingexplanations. trustandhowtomitigatethisissue.
129

AUser-CentricExplorationofAxiomaticExplainableAI
inParticipatoryBudgeting. UbiCompCompanion’24,October5–9,2024,Melbourne,VIC,Australia
REFERENCES
[8] JulieGerlings,ArisaShollo,andIoannaConstantiou.2020.Reviewingtheneed
[1] HarisAzizandAdityaGanguly.2021.ParticipatoryFundingCoordination:Model, forexplainableartificialintelligence(xAI).arXivpreprintarXiv:2012.01007(2020).
AxiomsandRules.InInternationalConferenceonAlgorithmicDecisionTheory. [9] MaryamHashemi,AliDarejeh,andFranciscoCruz.2024.UnderstandingUser
Springer,409–423. PreferencesinExplainableArtificialIntelligence:ASurveyandaMappingFunc-
[2] HarisAzizandNisargShah.2021. Participatorybudgeting:Modelsandap- tionProposal. arXiv:2302.03180[cs.AI] https://arxiv.org/abs/2302.03180
proaches.InPathwaysBetweenSocialScienceandComputationalSocialScience. [10] ScottMLundbergandSu-InLee.2017.Aunifiedapproachtointerpretingmodel
Springer,215–236. predictions.Advancesinneuralinformationprocessingsystems30(2017).
[3] ArthurBoixelandUlleEndriss.2020. Automatedjustificationofcollective [11] ArielDProcaccia.2019. Axiomsshouldexplainsolutions. InTheFutureof
decisionsviaconstraintsolving.(2020). EconomicDesign.Springer,195–199.
[4] OlivierCaillouxandUlleEndriss.2016.Arguingaboutvotingrules.(2016). [12] MarcoTulioRibeiro,SameerSingh,andCarlosGuestrin.2016."Whyshouldi
[5] IoannisCaragiannis,DavidKurokawa,HervéMoulin,ArielDProcaccia,Nisarg trustyou?"Explainingthepredictionsofanyclassifier.InProceedingsofthe22nd
Shah,andJunxingWang.2019.TheunreasonablefairnessofmaximumNash ACMSIGKDDinternationalconferenceonknowledgediscoveryanddatamining.
welfare. ACMTransactionsonEconomicsandComputation(TEAC)7,3(2019), 1135–1144.
1–32. [13] SahilVerma,JohnDickerson,andKeeganHines.2020.Counterfactualexplana-
[6] FranciscoCruz,CharlotteYoung,RichardDazeley,andPeterVamplew.2022. tionsformachinelearning:Areview.arXivpreprintarXiv:2010.10596(2020).
Evaluatinghuman-likeexplanationsforrobotactionsinreinforcementlearning [14] GiuliaViloneandLucaLongo.2021.Notionsofexplainabilityandevaluation
scenarios.In2022IEEE/RSJInternationalConferenceonIntelligentRobotsand approachesforexplainableartificialintelligence.InformationFusion76(2021),
Systems(IROS).IEEE,894–901. 89–106.
[7] RichardDazeley,PeterVamplew,CameronFoale,CharlotteYoung,SunilAryal, [15] SandraWachter,BrentMittelstadt,andChrisRussell.2017. Counterfactual
andFranciscoCruz.2021.Levelsofexplainableartificialintelligenceforhuman- explanationswithoutopeningtheblackbox:AutomateddecisionsandtheGDPR.
alignedconversationalexplanations.ArtificialIntelligence299(2021),103525. Harv.JL&Tech.31(2017),841.
130