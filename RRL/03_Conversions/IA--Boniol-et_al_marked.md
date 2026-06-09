DiveintoTime-SeriesAnomalyDetection:ADecadeReview
PAULBONIOL,Inria,DIENS,PSL,CNRS,France
QINGHUALIU,TheOhioStateUniversity,USA
MINGYIHUANG,TheOhioStateUniversity,USA
THEMISPALPANAS,UniversitéParisCité;IUF,France
JOHNPAPARRIZOS,TheOhioStateUniversity,USA
Recentadvancesindatacollectiontechnology,accompaniedbytheever-risingvolumeandvelocityofstreamingdata,underscorethe
vitalneedfortimeseriesanalytics.Inthisregard,time-seriesanomalydetectionhasbeenanimportantactivity,entailingvarious
applicationsinfieldssuchascybersecurity,financialmarkets,lawenforcement,andhealthcare.Whiletraditionalliteratureon
anomalydetectioniscenteredonstatisticalmeasures,theincreasingnumberofmachinelearningalgorithmsinrecentyearscallfora
structured,generalcharacterizationoftheresearchmethodsfortime-seriesanomalydetection.Thissurveygroupsandsummarizes
anomalydetectionexistingsolutionsunderaprocess-centrictaxonomyinthetimeseriescontext.Inadditiontogivinganoriginal
categorizationofanomalydetectionmethods,wealsoperformameta-analysisoftheliteratureandoutlinegeneraltrendsintime-series
anomalydetectionresearch.
ACMReferenceFormat:
PaulBoniol,QinghuaLiu,MingyiHuang,ThemisPalpanas,andJohnPaparrizos.2024.DiveintoTime-SeriesAnomalyDetection:A
DecadeReview.InProceedingsofMakesuretoenterthecorrectconferencetitlefromyourrightsconfirmationemai(Conferenceacronym
’XX).ACM,NewYork,NY,USA,51pages.https://doi.org/XXXXXXX.XXXXXXX
1 Introduction
Awiderangeofcost-effectivesensing,networking,storage,andprocessingsolutionsenablethecollectionofenormous
amountsofmeasurementsovertime[109–111,122,137,138,141,143,179,181,186].Recordingthesemeasurements
resultsinanorderedsequenceofreal-valueddatapointscommonlyreferredtoastimeseries.Moregenericterms,such
asdataseriesordatasequences,havealsobeenusedtorefertocaseswheretheorderingofdatareliesonadimension
otherthantime(e.g.,theangleindatafromastronomy,themassindatafromspectrometry,orthepositionindata
frombiology)[176].Analyticaltasksovertimeseriesdataarenecessaryvirtuallyineveryscientificdisciplineand
theircorrespondingindustries[14,61,62,78,161,182,190–192,201],includinginastronomy[4,102,245],biology
[11–13,64],economics[36,74,148,155,213,221,240],energysciences[6,9,158],engineering[112,162,203,243,248],
environmentalsciences[77,84,100,101,164,207,247],medicine[57,199,206],neuroscience[21,119],andsocial
sciences[36,160].Theanalysisoftimeserieshasbecomeincreasinglyprevalentforunderstandingamultitudeof
naturalorhuman-madeprocesses[187,188].Unfortunately,inherentcomplexitiesinthedatagenerationofthese
Authors’ContactInformation:PaulBoniol,Inria,DIENS,PSL,CNRS,Paris,France,paul.boniol@inria.fr;QinghuaLiu,TheOhioStateUniversity,
Columbus,USA,liu.11085@osu.edu;MingyiHuang,TheOhioStateUniversity,Columbus,USA,huang.5749@osu.edu;ThemisPalpanas,UniversitéParis
Cité;IUF,Paris,France,themis@mi.parisdescartes.fr;JohnPaparrizos,TheOhioStateUniversity,Columbus,USA,paparrizos.1@osu.edu.
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalorclassroomuseisgrantedwithoutfeeprovidedthatcopiesarenot
madeordistributedforprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitationonthefirstpage.Copyrightsforcomponents
ofthisworkownedbyothersthantheauthor(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,orrepublish,toposton
serversortoredistributetolists,requirespriorspecificpermissionand/orafee.Requestpermissionsfrompermissions@acm.org.
©2024Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
ManuscriptsubmittedtoACM
ManuscriptsubmittedtoACM 1
4202
ceD
92
]GL.sc[
1v21502.2142:viXra

2 Paparrizosetal.
processes,combinedwithimperfectionsinthemeasurementsystemsaswellasinteractionswithmaliciousactors,
oftenresultinabnormalphenomena.Suchabnormaleventsappearsubsequentlyinthecollecteddataasanomalies.
ConsideringthatthevolumeoftheproducedtimeserieswillcontinuetoriseduetotheexplosionofInternet-of-Things
(IoT)applications[75,105,151],anabundanceofanomaliesisexpectedintimeseriescollections.
Thedetectionofanomaliesintimeserieshasreceivedampleacademicandindustrialattentionforoversixdecades
[1,27–30,32,39,69,121,142,159,165,175,180,185,235,239].Withthetermanomalieswerefertodatapointsor
groupsofdatapointsthatdonotconformtosomenotionofnormalityoranexpectedbehaviorbasedonpreviously
observeddata[16,45,80,91,107].Intheliterature,alternativetermssuchasoutliers,novelties,exceptions,peculiarities,
aberrations,deviants,ordiscordsoftenappeartodescribetheoccurrencesofsuchrare,unusual,oftenhard-to-explain
anomalouspatterns[2,40,65].Dependingontheapplication,anomaliescanconstitute[2]:(i)noiseorerroneousdata,
whichhindersthedataanalysis;or(ii)actualdataofinterest.Intheformercase,theanomaliesareunwanteddatathat
areremovedorcorrected.Inthelattercase,theanomaliesmayidentifymeaningfulevents,suchasfailuresorchanges
inbehavior,whicharethebasisforsubsequentanalysis.
Regardlessofthepurposeofthetimeseriesandthesemanticmeaningofanomalies,anomalydetectiondescribesthe
processofanalyzingatimeseriesforidentifyingunusualpatterns,whichisachallengingtaskbecausemanytypesof
anomaliesexist.Theyappearindifferentsizesandshapes.AccordingtoFoorthuis[68],researchongeneral-purpose
anomalydetectiondatesbackto1777,whereBernoulli’sworkseemstobethefirstaddressingissuesofacceptingor
rejectingextremecasesofobservations[19].Robusttheoryinthatareawasdevelopedduringthe1800s(e.g.,methodof
leastsquaresin1805[225])[63,76,83,198,230]and1900s[60,85,106,197,212]butitwasnotuntilthe1950swhen
thefirstworksfocusedspecificallyintimeseriesdata[175].In1972,Foxconductedoneofthefirststudiestoexamine
anomalousbehaviorsacrosstimeanddefinedtwotypesofanomalies:(i)ananomalyaffectingasingleobservation;and
(ii)ananomalyaffectinganobservationandsubsequentobservations[69].In1988,Tsayextendedthesedefinitionsinto
fourtypesforunivariatetimeseries[239]andsubsequentlyformultivariatetimeseries[241].Inthesametimeframe,
thefirstfewapproachesappearfordetectinganomaliesintimeseries,withafocusonutilizingstatisticaltestssuchas
theLikelihood-ratiotest[48,242]
Sincethen,alargenumberofworkshaveappearedinthisarea,whichcontinuestoexpandatarapidpace.Additionally,
numeroussurveyshavebeenpublishedtoprovideanoverviewofthecurrentadvancementsinthisfield[22,33,43,46,
47,54,56,86,99].Unfortunately,themajorityofthesurveysfocusongeneral-purposeanomalydetectionmethodsand
onlyaportionofthembrieflyreviewmethodsfortime-seriesanomalydetection.Eventhoughtraditionalanomaly
detectionmethodsmaytreattimeseriesasanyotherhigh-dimensionalvectorandattempttodetectanomalies,ourfocus
isonapproachesthatarespecificallydesignedtoconsidercharacteristicsoftimeseries.Toillustratetheimportanceof
thispoint,inFigure1,wepresentthreeexamplesofanomaliesintimeseriesapplicationswherethetemporalordering
andthecollectiveconsiderationofpointsenablethedetectionofanomalies.Forexample,in1(a),consideringeach
pointinisolationcannotrevealtheunderlyinganomalyindata.
Therefore,time-orderingfeaturesareimportanttobeconsideredintheanomalydetectionpipeline.Dependingon
theresearchcommunity,multiplesolutionshavebeenproposedtotackletheabove-mentionedchallenge.Forexample,
agroupofmethodsproposedintheliteraturewillproposeatransformationstepthatconvertstimeinformationintoa
relevantvectorspaceandthenapplytraditionaloutlierdetectiontechniques.Inaddition,othergroupsofmethodswill
considerdistances(orsimilaritymeasuresdedicatedtotimeseries)toidentifyunusualtimeseriesorsubsequences.
Then,methodsproposedinthedeeplearningcommunitywillbenefitfromspecificarchitecturesthatembedtime
information(suchasrecurrentneuralnetworksorconvolutional-basedapproaches).
ManuscriptsubmittedtoACM

(a) Data series example: Snippet of an electrocardiogram (in (b) Data series example: Snippet of simulated engine disks data (c) Data series example: Snippet of spaceshuttlemarottavalve
blue:normal heartbeats, in red: premature heartbeat) (in blue:usual disk revolution, in red: failed disk revolution) (in blue:normal cycle, in red: anomalous cycle)
DiveintoTime-SeriesAnomalyDetection:ADecadeReview 3
(a) Data series example: Snippet of an electrocardiogram (in (b) Data series example: Snippet of simulated engine disks data (c) Data series example: Snippet of spaceshuttlemarottavalve
(a) Timb(elau )se eD:nraiotears mseearxli ehasem aerxptablmee:ap Stlesn,: iiSnpn priepedpt:e pot rofe fam anna t eeullreeecc thtreoraocractrbaderioadtgi)roagmr a(imn (in blu(ine(b :b) nl uDoear:tmua ssauealr lih edesi saekrx rtaebmveopalluett:s iS,o nnini,p iprnee rtde od:f:p sfraimeilmeudlaa dtteiusdkr eerenhvgoienlauert ditoibsnke)sa dt)a ta (c) D(aint ab slueeri:enso erxmamal pclyec:l eS,n iinp preedt :o af nsopmacaelosuhsu tctyleclem)arottavalve
blue:normal heartbeats, in red: premature heartbeat) (in blue:usual disk revolution, in red: failed disk revolution) (in blue:normal cycle, in red: anomalous cycle)
Premature Anomalous
heartbeat energizing
phase
Unusual disk
revolution
(a) Data series example: Snippet of an electrocardiogram (in (b) Data series example: Snippet of simulated engineT idmiseks idnadtea x (c) Data series example: Snippet of spaceshuttlemaroTttiamvea lvinedex
b(alu) e D:antoar smearile hse eaxratbmepaltes:, Sinn irpepde: tp oref mana teulerect hroecaartrbdeioagtr)am (in (b) T(imi(nb )eb l Duseaet:raui esseusraeile xdsa iesmkx arpmelvepo:lle uS:t nSioninpip,p pinee ttr eoodff :s faiam islueilmda tdueidslak e trneegvdioneleu ntdigoisinkn)se d adtias ks(in blu(ce) : Du(aisntau b asleulredie:isns koerxrmaemavlpo clleyuc: tlSeino, iinpnp, reientd o:r fea sndpo:amcfaeailsloehuudst ctdlyeicslmke)arreovttoaluvatlivoen)
blue:normal heartbeats, in red: premature heartbeat) (in blue:usual disk Prerevmoalututrieo n, in red: failed disk revolution) (in blue:normal cycle, in red: anomalous cycle) Anomalous
heartbeat energizing
Premature phAansoemalous
heartbeat energizing
phase
Unusual disk
revolution
Unusual disk
revolution
(a) Data series example: Snippet of an electrocardiogram (in (b) Data series example: Snippet of simulated engine disks data (c) Data series example: Snippet of spaceshuttlemaTroimttaev ianlvdeex Time index
blue:normal heartbeats, in red: premature heartbeat) (in blue:usual disk revolution, in red: failed disk revolution) (c) Tim(ine bsleueri:ensoremxaalm cypcllee,: iSnn reipdp: aentoomfa alo sups acycceles)huttlemarottavalve(in blue:normal cycle, in red:anomalouscycle)
Premature Anomalous
heartbeat energizing
P
h
r
e
e
a
m
rt
a
b
t
e
u
a
r
t
e phA ean nso eem
rg
a
iz
l
i
o
n
u
g
s
phase
Unusual disk
revolution
Unusual disk
revolution
Time index Time index
Premature AnomaloFuisg .1. Examplesofdifferenttimeseriesapplicationsandtypesofanomalies.
heartbeat energizing
phase
Unusual disk Unfortunately,theseareasremainmostlydisconnected,usingdifferentdatasets,baselines,andevaluationmeasures.
revolution
Newalgorithmsareevaluatedonlyagainstnon-representativesubsetsofapproachesanditisvirtuallyimpossible
tofindthebeststate-of-the-artapproachforaconcreteusecase.Toremedythisissue,thissurveypresentsanovel,
comprehensive,process-centrictaxonomyforthemultipledetectionmethodsineachcategory.Wecollectedacompre-
hensiverangeofalgorithmsintheliteratureandgroupedthemintofamiliesofalgorithmswithsimilarapproaches.In
addition,toidentifyresearchtrends,wealsoprovidestatisticsonthetypeandareaofproposedapproachesovertime.
Then,wealsolistexistingbenchmarksthatcanbeusedasacommongroundonwhichnewproposedmethods
(regardlessofthecommunity)shouldbeevaluated.Finally,weenumerateexistingevaluationmeasuresusuallyusedto
evaluateanomalydetectionmethodswhilediscussingtheirlimitationandbenefitswhenappliedtothespecificcaseof
timeseries.
2 Time-SeriesAnomalyDetectionOverview
Inthissection,wediscusstheproblemformulationfortime-seriesanomalydetectionalgorithmsandmotivateour
process-centrictaxonomy.
ManuscriptsubmittedtoACM

4 Paparrizosetal.
2.1 OntheDefinitionofAnomaliesinTimeSeries
Attestingtothechallengingnatureoftheproblemathand,weobservethattheredoesnotexistasingle,universal,
precisedefinitionofanomaliesoroutliers.Traditionally,anomaliesareobservationsthatdeviateconsiderablyfromthe
majorityofothersamplesinadistribution.Theanomalouspointsraisesuspicionsthatamechanismdifferentfrom
thoseoftheotherdatageneratedthespecificobservation.Suchamechanismusuallyrepresentseitheranerroneous
datameasurementprocedureoranunusualevent.
Incasesoferrorsinthedatameasurementprocedure,theanomalousobservationsaremarkedas“noise"–unwanted
datathatarenotattractivetotheanalystandshouldberemovedinthedatacleaningprocess.Manypiecesofliterature
havebeendedicatedtothistypeofproblem,particularlyinthesensorsetting,wherethemainobjectiveistoeliminate
transmissionerrorandrenderaccuratepredictions.Intime-seriesanomalydetection,however,recentliteraturebegins
tocenterondetectinganomalousevents,whichindicate“novelty"–unusualbutinterestingphenomenathatoriginate
fromaninherentvariabilityinthedomainofthedata.Anaturalexampleofthistypeofproblemisfrauddetectionfor
creditinformation,wheretheprincipalaimistodetectandanalyzethefrauditself.
Thedetectionofthesetwotypesofanomalies(anomaliesandoutlierscanbeusedinterchangeably)canbeachieved
viaexpertknowledge.Byknowingexactlyhowthesystemworks,theexpertscansettheparametertofitadistribution
ofvaluesthatrepresentthehealthyfunctioningstate.Anomaliesarethendetectedbymarkingpointsofmorethan
threestandarddeviationsawayfromthemeanofdatadistributionestimatedbytheexperts.Tovalidatethedetection
process,wealsoneedtoperformextensiveteststotestthedistribution(anditsparameters)againstthedataset.
Nevertheless,inseveralreal-worldproblems,wedonotknowpreciselythedatadistributionthathasgeneratedaset
ofpoints(andallthedifferentartifactsthatplayedarole).Besides,thedatadistributionsthatweencounterinpractice,
arealmostalwaysrathercomplexandveryhardtoidentifyorapproximateeffectively.Consequently,definingand
identifyinganomaliesusingtheirdistancefromameanvaluedefinedbyexpertsissometimeshardlypractical.
Despitethechallengeofestimatingdistributionparametersbyexperts,recentdevelopmentsincomputationalpower
haveliberatedusfromanalternativeapproachtoanalyzingdatadistributionfromthedataitself.Usingavarietyof
learningmethods,researchersmayapplycomputeralgorithmstoanalyzerawdata,estimateafairdistribution,and
detectanomalieswithoutexpertknowledge.Eventhoughbeingstronglydependentonthequalityandthecontextof
thedatasets,thesemethodsseemtoshowstrongresultsinachievingrelativelycomplextasks.Inthispaper,wefocus
onthistypeofmethod.
2.2 TypesofAnomaliesinTimeSeries
Thereisafurthercomplicationintime-seriesanomalydetection.Duetothetemporalityofthedata,anomaliescan
occurintheformofasinglevalueorcollectivelyintheformofsub-sequences.Inthespecificcontextofpoint,weare
interestedinfindingpointsthatarefarfromtheusualdistributionofvaluesthatcorrespondtohealthystates.Inthe
specificcontextofsequences,weareinterestedinidentifyinganomaloussub-sequences,whichareusuallynotoutliers
butexhibitrareand,hence,anomalouspatterns.Inreal-worldapplications,suchadistinctionbetweenpointsand
sub-sequencesbecomescrucialbecauseeventhoughindividualpointsmightseemnormalagainsttheirneighboring
points,theshapegeneratedbythesequenceofthesepointsmaybeanomalous.
Formally,wedefinethreetypesoftimeseriesanomalies:point,contextual,andcollectiveanomalies.Pointanomalies
refertodatapointsthatdeviateremarkablyfromtherestofthedata.Figure2(a)depictsasynthetictimeserieswitha
pointanomaly:thevalueoftheanomalyisoutsidetheexpectedrangeofnormalvalues.Contextualanomaliesreferto
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 5
𝑃𝑜𝑖𝑛𝑡-𝑏𝑎𝑠𝑒𝑑 𝑆𝑒𝑞𝑢𝑒𝑛𝑐𝑒-𝑏𝑎𝑠𝑒𝑑
𝑎.1 𝑇𝑖𝑚𝑒 𝑠𝑒𝑟𝑖𝑒𝑠 𝑏.1 𝑇𝑖𝑚𝑒 𝑠𝑒𝑟𝑖𝑒𝑠 𝑐.1 𝑇𝑖𝑚𝑒 𝑠𝑒𝑟𝑖𝑒𝑠
20 𝑃𝑜𝑖𝑛𝑡 𝐶𝑜𝑛𝑡𝑒𝑥𝑡𝑢𝑎𝑙 𝑎𝑛𝑜𝑚𝑎𝑙𝑦 𝐶𝑜𝑙𝑙𝑒𝑐𝑡𝑖𝑣𝑒
𝑎𝑛𝑜𝑚𝑎𝑙𝑦
𝑎𝑛𝑜𝑚𝑎𝑙𝑦
0
0 300 600 900 1200 0 300 600 900 1200 0 300 600 900 1200
𝑎.2 𝐷𝑖𝑠𝑡𝑟𝑖𝑏𝑢𝑡𝑖𝑜𝑛 𝑏.2 𝑏.3 𝑐.2 𝐷𝑖𝑠𝑡𝑟𝑖𝑏𝑢𝑡𝑖𝑜𝑛
0 5 10 15 20 0 5 10 15 20 0 5 10 15 20 0 5 10 15 20
𝑎 𝑃𝑜𝑖𝑛𝑡 𝑎𝑛𝑜𝑚𝑎𝑙𝑦 𝑜𝑢𝑡𝑠𝑖𝑑𝑒 𝑡ℎ𝑒 𝑏 𝐶𝑜𝑛𝑡𝑒𝑥𝑡𝑢𝑎𝑙 𝑎𝑛𝑜𝑚𝑎𝑙𝑦 𝑜𝑢𝑡𝑠𝑖𝑑𝑒 𝑡ℎ𝑒 𝑙𝑜𝑐𝑎𝑙 𝑐 𝐶𝑜𝑙𝑙𝑒𝑐𝑡𝑖𝑣𝑒 𝑎𝑛𝑜𝑚𝑎𝑙𝑦 𝑖𝑛𝑠𝑖𝑑𝑒 𝑡ℎ𝑒 ℎ𝑒𝑎𝑙𝑡ℎ𝑦
ℎ𝑒𝑎𝑙𝑡ℎ𝑦 𝑟𝑎𝑛𝑔𝑒 𝑜𝑓 𝑣𝑎𝑙𝑢𝑒𝑠 (𝑑𝑜𝑡𝑡𝑒𝑑 𝑏𝑙𝑎𝑐𝑘 𝑙𝑖𝑛𝑒) ℎ𝑒𝑎𝑙𝑡ℎ𝑦 𝑟𝑎𝑛𝑔𝑒 𝑜𝑓 𝑣𝑎𝑙𝑢𝑒𝑠 (𝑑𝑜𝑡𝑡𝑒𝑑 𝑏𝑙𝑎𝑐𝑘 𝑏𝑜𝑥) 𝑟𝑎𝑛𝑔𝑒 𝑜𝑓 𝑣𝑎𝑙𝑢𝑒𝑠 (𝑑𝑜𝑡𝑡𝑒𝑑 𝑏𝑙𝑎𝑐𝑘 𝑙𝑖𝑛𝑒)
𝑠𝑒𝑢𝑙𝑎𝑉
𝑦𝑐𝑛𝑒𝑢𝑞𝑒𝑟𝐹
Fig.2. Syntheticillustrationofthethreetimeseriesanomalytypes:(a)point;(b)contextual;and(c)collectiveanomalies.
datapointswithintheexpectedrangeofthedistribution(incontrasttopointanomalies)butdeviatefromtheexpected
datadistribution,givenaspecificcontext(e.g.,awindow).Figure2(b)illustratesatimeserieswithacontextualanomaly:
theanomalyiswithintheusualrangeofvalues(leftdistributionplotofFigure2(b))butoutsidethenormalrange
ofvaluesforalocalwindow(rightdistributionplotofFigure2(b)).Collectiveanomaliesrefertosequencesofpoints
thatdonotrepeatatypical(previouslyobserved)pattern.Figure2(c)depictsasyntheticcollectiveanomaly.Thefirst
twocategories,namely,pointandcontextualanomalies,arereferredtoaspoint-basedanomalies.whereas,collective
anomaliesarereferredtoassequence-basedanomalies.
Asanadditionalnote,thereisanothercaseofsub-sequenceanomalydetectionreferredtoaswhole-sequence
detection,relativetothepointdetection.Inthiscase,theperiodofthesub-sequenceisthatoftheentiretimeseries,
andtheentiretimeseriesisevaluatedforanomalydetectionasawhole.Thisistypicallythecaseinthesensorcleaning
environmentwhereresearchersareinterestedinfindinganabnormalsensoramongallthefunctioningsensors.
2.3 UnivariateversusMultivariate
Anothercharacteristicoftime-seriesanomalydetectionalgorithmscomesfromthedimensionalityofthedata.Univariate
timeseriesconsistsofanorderedsequenceofrealvaluesonasingledimension,andtheanomaliesaredetectedbased
ononesinglefeature.Inthiscase,asillustratedinFigure3(b.1),asubsequencecanberepresentedasavector.Onthe
otherhand,Multivariatetimeseriesiseitherasetoforderedsequencesofrealvalues(witheachorderedsequence
havingthesamelength)oranorderedsequenceofvectorscomposedofrealvalues.Inthisspecificcase,asillustrated
inFigure3(b.2),asubsequenceisamatrixinwhicheachlinecorrespondstoasubsequenceofonesingledimension.
Instancesofanomaliesaredetectedaccordingtomultiplefeatures,wherevaluesofonefeature,whensingledout,may
looknormaldespitetheabnormalityofthesequenceasawhole.
2.4 Unsupervised,Semi-supervisedversusSupervised
Thistaskcanbedividedintothreedistinctcases:(i)expertsdonothaveinformationonwhatanomaliestodetect;
(ii)expertsonlyhaveinformationontheexpectednormalbehaviors;(iii)expertshavepreciseexamplesofwhich
ManuscriptsubmittedtoACM

| 6   |     |     |     |     |     | Paparrizosetal. |
| --- | --- | --- | --- | --- | --- | --------------- |
𝑼𝒏𝒊𝒗𝒂𝒓𝒊𝒂𝒕𝒆	𝑎𝑛𝑑	𝑴𝒖𝒍𝒕𝒊𝒗𝒂𝒓𝒊𝒂𝒕𝒆	𝑝𝑜𝑖𝑛𝑡	𝑎𝑛𝑜𝑚𝑎𝑙𝑖𝑒𝑠 !"#$%&#%'()*+,-.'#$%&#%'(/01*2)*03)45 𝑼𝒏𝒊𝒗𝒂𝒓𝒊𝒂𝒕𝒆	𝑎𝑛𝑑	𝑴𝒖𝒍𝒕𝒊𝒗𝒂𝒓𝒊𝒂𝒕𝒆	𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒	𝑎𝑛𝑜𝑚𝑎𝑙𝑖𝑒𝑠 !"#$%&#%'()*+,-.'#$%&#%'(67897*:7)*03)45
𝑇(")
| ,(")       | 𝑇(") |              | ,(")       |        |     |              |
| ---------- | ---- | ------------ | ---------- | ------ | --- | ------------ |
| ,($)       | 𝑇($) |              | ,($)       |        |     |              |
| !"#$%&#%'( | 𝑇    | -*)'#$%&#%'( | !"#$%&#%'( | 𝑇 𝑇($) |     | -*)'#$%&#%'( |
$%)*(+*')#(& $%)*(+*')#(& /*6/(=*("7(+*')#(& /*6/(=*("7(+*')#(&
|       | …       |      |        | …    |     |      |
| ----- | ------- | ---- | ------ | ---- | --- | ---- |
| ,𝑇(%) | 𝑇(%)    |      | ,(%) 𝑇 | 𝑇(%) |     |      |
| 0 300 | 600 900 | 1200 | 0 300  | 600  | 900 | 1200 |
|       | 200     |      |        |      | 200 |      |
|       | 150     |      |        |      | 150 |      |
|       | 100     |      |        |      | 100 |      |
|       | 50      |      |        |      | 50  |      |
|       | 0       |      |        |      | 0   |      |
0 50 100 150 200 0 50 100 150 200 0 50 100 150 200 0 50 100 150 200
| %.1 !"#$%&#%'(7%/( | %.2 -*)'#$%&#%'(7%/( |     | 6.1 !"#$%&#%'(7%/( |     | 6.2 -*)'#$%&#%'(7%/( |     |
| ------------------ | -------------------- | --- | ------------------ | --- | -------------------- | --- |
6 >*6/(=*("7(+*')#(&#"/#0('ℎ(ℎ(%)'ℎ2&%"3(+4$%)*(/
% .+#"'+*')#(&+*'/#0('ℎ(ℎ(%)'ℎ2&%"3(+4$%)*(/
|     | (0+''(06)%78)#"() |     |     | (0+''(06)%78)#"() |     |     |
| --- | ----------------- | --- | --- | ----------------- | --- | --- |
Fig.3. Syntheticexamplecomparinganomaliesinunivariateandmultivariatetimeseriesfor(a)apointoutlierand(b)asequence
outlier.
anomaliestheyhavetodetect(andhaveacollectionofknownanomalies).Thisgivesrisetothedistinctionamong(i)
unsupervised,(ii)semi-supervised,and(iii)supervisedmethods.
Unsupervised:Incase(i),onecandecidetoadoptafullyunsupervisedmethod.Thesemethodshavethebenefitof
workingwithouttheneedforalargecollectionofknownanomaliesandcandetectunknownabnormalbehavior
automatically.Suchmethodscanbeusedeithertomonitorthehealthstateortominethehistoricaltimeseriesofa
system(tobuildacollectionofabnormalbehaviorsthatcanthenbeusedonasupervisedframework).
Semi-supervised:Incase(ii),methodscanlearntodetectanomaliesbasedonannotatedexamplesofnormalsequences
providedbytheexperts.Thisistheclassicalcaseformostoftheanomalydetectionmethodsintheliterature.One
shouldnotethatthiscategoryisoftendefinedasUnsupervised.However,weconsideritunfairtogroupsuchmethods
withthecategorymentionedabove,knowingthattheyrequiremuchmorepriorknowledgethanthepreviousone.
Supervised:Whileincase(i)and(ii)anomalieswereconsideredunknown,incase(iii),weconsiderthattheexperts
knowprecisely,whattypeofpattern(s)theywanttodetect,andthatacollectionoftimeserieswithlabeledanomalies
isavailable.Inthatcase,wehaveadatabaseofanomaliesatourdisposal.Inasupervisedsetting,onemaybeinterested
inpredictingtheabnormalsub-sequencebyitspriorsub-sequences.Suchsub-sequencescanbecalledprecursorsof
anomalies.
2.5 AnomalyDetectionPipelines
Uponsummarizingthevariousdifferentalgorithmsondifferentdomains,werealizedacommonpipelinefortime-series
anomalydetectionalgorithms.Thepipelineconsistsoffourparts:datapre-processing,detectionmethod,scoring,and
post-processing.Figure4illustratestheprocess.Thedecompositionofthegeneralanomalydetectionprocessintosmall
stepsofapipelineisbeneficialforcomparingdifferentalgorithmsonvariousdimensions.Understandingofalgorithms’
functioninthepre-processingstephelpsinterpretitstreatmentoftimeseriesdataspecifically.
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 7
Anomalies
Time Series
Pre-Processing
0 2000 4000
Anomaly Detection
Model Post-Processing
Scoring
Anomaly score
0 2000 4000 6000 8000
Fig.4. Timeseriesanomalydetectionpipeline.
Thedataprocessingsteprepresentshowtheanomalydetectionmethodprocessesthetimeseriesdataattheinitialstep.
Wehavenoticedalltheanomalydetectionmodelsaresomehowbasedonawindowedapproachinitially-converting
thetimeseriesdataintoamatrixwithrowsofslidingwindowslicesoftheoriginaltimeseries.Thepre-processing
stepconsistsoftheadditionalprocessingprocedurebesidesthewindowtransformation,whichvariesfromstatistical
featureextractiontofittingamachinelearningmodelandbuildinganeuralnetwork.
Afterthedataisprocessed,differentdetectionmethodsareimplementedonthedataset,whichmightbesimply
calculatingdistancesamongtheprocessedsub-sequences,fittingaclassificationhyper-plane,orusingtheprocessed
modeltogeneratenewsub-sequencesandcomparingthemwithoriginalsub-sequences.Thedetectionmethodsare
usuallytraditionaloutlierdetectionmethodsforvectordata.
Then,duringthescoringprocess,theresultsderivedinthedetectionmethodswillbeconvertedtoananomalyscore
thatassessestheabnormalityofindividualsub-sequencesbyarealvalue(suchasaprobabilityofbeingananomaly).
Thescoreswillbefurtherusedtoinferthescoreoftheindividualpoint.Theresultingscoreisatimeseriesofthesame
lengthastheinitialtimeseries.
Lastly,duringthepost-processingstep,theanomalyscoretimeseriesisprocessedtoextracttheanomalouspointsor
intervals.Usually,athresholdvaluewillbedetermined,wherethepointswithanomalyscoressurpassingthethreshold
willbemarkedastheanomaly.
Thiscategorizationoftime-seriesanomalydetectionpipelinesinspiresourprocess-centrictaxonomyofthedetection
methods,whichwillbediscussedthoroughlyinthenextsection.
3 AnomalyDetectionTaxonomy
Inthissection,wedescribeourproposedprocess-centrictaxonomyofthedetectionmethods.Wedividemethods
intothreecategories:(i)distance-based,(ii)density-based,and(iii)prediction-based.Thefirstfamilycontainsmethods
thatfocusontheanalysisofsub-sequencesforthepurposeofdetectinganomaliesintimeseries,mainlybyutilizing
distancestoagivenmodel.Second,insteadofmeasuringnearest-neighbordistances,density-basedmethodsfocuson
detectinggloballynormalorisolatedbehaviors.Third,prediction-basedmethodsaimtotrainamodel(onanomaly-free
timeseriesorwithveryfewanomalies)toreconstructthenormaldataorpredictthefutureexpectednormalpoints.
ManuscriptsubmittedtoACM

8 Paparrizosetal.
Time series anomaly detection methods
Distance-based Density-based Prediction-based
Proximity- Clustering- Discord- Distribution- Graph- Tree- Encoding- Forecasting- Reconstruction
based based based based based based based based -based
A BC A B C A D E A BC
ℬ A → BC
A → DE
…
Fig.5. Process-centricanomalydetectiontaxonomy.
Inthefollowingsections,webreakdowneachcategoryintoprocess-centricsubcategories.Figure5illustratesour
proposedprocess-centrictaxonomy.
Notethatthesecond-levelcategorizationisnotmutuallyexclusive.Amodelmightcompressthetimeseriesdata
whileadoptingadiscord-basedidentificationstrategy.Inthiscase,themodelfallswithintwodifferentsub-categories.
Inthetableofmethods,onlyoneofthesecond-levelwillbelistedtogiveaclearerrepresentation.
3.0.1 Distance-based. Asitsnamesuggests,thedistance-basedmethoddetectsanomaliespurelyfromtherawtime
seriesusingdistancemeasures.Giventwosequences(orunivariatetimeseries),𝐴∈Rℓ and𝐵 ∈Rℓ ,ofthesamelength,
ℓ,wedefinethedistancebetween𝐴and𝐵 as𝑑(𝐴,𝐵) ∈ R,suchas𝑑(𝐴,𝐵) = 0when𝐴and𝐵 arethesame.There
existdifferentdefinitionsof𝑑 intheliterature.TheclassicaldistancewidelyusedistheEuclideandistanceorthe
Z-normalizedEuclideandistance(Euclideandistancewithsequencesofmeanvaluesequalto0andstandarddeviations
equalto1).Then,DynamicTimeWarping(DTW)iscommonlyusedtocopewithmisalignmentissues.Overall,the
distance-basedalgorithmsmerelytreatthenumericalvalueoftimeseriesasitis,withoutfurthermodificationssuchas
removingseasonalityorintroducinganewstructurebuiltonthedata.Withinthedistance-basedmodels,therecome
threesecond-levelcategories:proximity-based,clustering-based,anddiscord-basedmodels.
(1) Theproximity-basedmodelmeasuresproximitybycalculatingthedistanceofagivensub-sequencetoits
closeneighborhood.Theisolationofasub-sequencewithregardstoitsclosestneighborsisthemaincriterionto
considerifthissub-sequenceisananomalyornot.Thisnotionofisolationwithregardtoagivenneighborhood
hasbeenproposedfornon-timeseriesdata.Thus,themethodscontainedinthiscategoryhavebeenintroduced
forthegeneralcaseofmulti-dimensionaloutlierdetection.Inourspecificcase,thesub-sequenceofatime
seriescanbeconsideredamulti-dimensionalpointwiththenumberofdimensionsequaltothelengthofthe
sub-sequence.
(2) Theclustering-basedmodelinfersanomaliesfromaclusterpartitionofthetimeseriessub-sequences.In
practice,theanomalyscoreiscalculatedbythenon-membershipofasub-sequenceofeachoftheclusterslearned
bythemodel.Otherconsiderations,suchasclusterdistanceandclustercapacity,canalsobeconsidered.The
clusteringissueisrelatedtotheanomalydetectionprobleminthatpointsmayeitherbelongtoaclusteror
bedeemedanomalies.Inpractice,thefactthatasub-sequencebelongsornottoaclusterisassessedbythe
computationofthedistancebetweenthissub-sequenceandtheclustercentroidormedoid.
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 9
(3) Thediscord-basedmodeltriestoidentifyefficientlyspecifictypesofsub-sequencesinthetimeseriesnamed
discord.Formally,asub-sequence𝐴(oragivenlengthℓ)isadiscord,ifthedistancebetweenitsnearestneighbor
isthelargestamongallthenearestneighbors’distancescomputedbetweensub-sequencesoflengthℓ inthe
timeseries.Overall,similarlytoproximity-basedmethods,Theisolationofasub-sequencewithregardsto
itsclosestneighborsisthemaincriteriontoconsiderifthissub-sequenceisananomalyornot.However,on
contrarytoproximity-basedmethods,discord-basedmethodshavebeenintroducedforthespecificcaseof
anomalydetectionintimeseries.Thus,assuchmethodsintroducedefficientprocessesfortimeseriesdistance
computationspecifically,wegroupthemintoonedifferentsub-category.
3.0.2 Density-based. Thedensity-baseddoesnottreatthetimeseriesassimplenumericalvaluesbutimbuesthem
withmorecomplexarchitecture.Thedensity-basedmethodprocessestimeseriesdataontopofarepresentationof
thetimeseriesthataimstomeasurethedensityofthepointsorsub-sequencespace.Suchrepresentationvariesfrom
graphs,trees,andhistogramstoagrammarinductionrule.Thedensity-basedmodelshavefoursecond-levelcategories:
distribution-based,graph-based,tree-based,andencoding-based.
(1) Thedistribution-basedanomalydetectionapproachisbuildingadistributionfromstatisticalfeaturesofthe
pointsorsub-sequencesofthetimeseries.Byexaminingthedistributionsoffeaturesofthenormalsub-sequences,
ittriestorecoverrelevantstatisticalmodelsandthenusesthemtoinfertheabnormalityofthedata.
(2) Agraph-basedmethodrepresentsthetimeseriesandthecorrespondingsub-sequencesasagraph.Thenodes
andedgesrepresentthedifferenttypesofsub-sequences(orrepresentativefeatures)andtheirevolutionintime.
Forinstance,thenodescanbesetsofsimilarsub-sequences(usingapredefineddistancemeasure),andtheedge
weightscanbethenumberoftimesasub-sequenceofagivennodehasbeenfollowedbyasub-sequenceof
anothernode.Thedetectionofanomaliesisthenachievedusingcharacteristicsofthegraph,suchasthenode
andedgeweights,butalsothedegreeofthenodes.
(3) Atree-basedapproachaimstodividethepointorsub-sequenceofatimeseriesusingtrees.Forinstance,such
treescanbeusedtosplitdifferentpointsorsub-sequencesbasedontheirsimilarity.Thedetectionofanomalies
isthenbasedonthestatisticsandcharacteristicsofthetree,suchasitsdepth.
(4) Aencoding-basedanomalydetectionmodelcompressesorrepresentsthetimeseriesintodifferentformsof
symbols.Theencoding-basedmodelsuggeststhatatimeseriescanbeinterpretedasasequenceofcontext-free,
discretesymbolsorstates.Forinstance,anomaliescanbedetectedbyusinggrammarruleswiththesymbols
extractedfromthetimeseries.Itshouldbenotedthatanencoding-basedmodelisnotexclusivetoitself;itmay
evenbebasedonagraph-basedortree-basedmodel.
3.0.3 Prediction-based. Prediction-based methods aim to detect anomalies by predicting the expected normal
behaviorsbasedonatrainingsetoftimeseriesorsub-sequences(containinganomaliesornot).Forinstance,some
methodswillbetrainedtopredictthenextvalueorsub-sequencebasedonthepreviousone.Thepredictionisthen
post-processedtodetectabnormalpointsorsub-sequences.Then,thepredictionerrorisusedasananomalyscore.
Theunderlyingassumptionofprediction-basedmethodsisthatnormaldataareeasiertopredict,whileanomalies
areunexpected,leadingtohigherpredictionerrors.Suchassumptionsarevalidwhenthetrainingsetcontainsnoor
fewtimeserieswithanomalies.Therefore,prediction-basedmethodsareusuallymoreoptimalundersemi-supervised
settings.
ManuscriptsubmittedtoACM

10 Paparrizosetal.
Time Series T ∈ ℝ! T T
!"#,ℓ !,ℓ
𝑇
Model &,ℓ
Predictor
Builder
Forecasting First Data First
𝑇%
&,ℓ Detection
Distance
Update model Model
𝑦
Raw Score 𝑌 ∈ ℝ!"ℓ$% & ℓ
Scoring
e.g. padding with 0
Final Score 𝑌 ∈ ℝ!
Fig.6. Thescoringprocess.
(1) Theforecasting-basedmethodisamodelthat,foragivenindexortimestamp,takesasinputpointsorsub-
sequencesbeforethisgiventimestampandpredictsitscorrespondingvalueorsub-sequence.Inotherwords,
suchmethodsusepastvaluesasinputtopredictthefollowingone.Theforecastingerror(thedifferencebetween
thepredictedandtherealvalue)isusedasananomalyscore.Indeed,suchforecastingerrorisrepresentativeof
theexpectationofthecurrentvaluebasedonthepreviouspointsorsub-sequences.Thelargertheerror,themore
unexpectedthevalue,andthus,potentiallyabnormal.Forecasting-basedapproachesassumethatthetraining
data(pastvaluesorsub-sequences)isalmostanomaly-free.Thus,suchmethodsaremostlysemi-supervised.
(2) Thereconstruction-basedmethodcorrespondstoamodelthatcompressestheinputtimeseries(orsub-
sequence)intoalatentspace(smallerthantheinputsize)andistrainedtoreconstructtheinputtimeseries
fromthelatentspace.Thedifferencebetweentheinputtimeseriesandthereconstructedone(namedthe
reconstructionerror)isusedasananomalyscore.Asforforecasting-basedmethods,thelargertheerror,the
moreunexpectedthevalue,andthus,potentiallyabnormal.Moreover,asthereconstructionerrorislikelytobe
smallforthetimeseriesusedtotrainthemodel,suchreconstructionmethodsareoptimalinsemi-supervised
settings.
3.1 ScoringProcess
Assummarizedinthepipeline,anomalydetectionalgorithmsdistinguishoutliersbyinferenceonthe“anomalyscores"
ofeachtemporaldatapoint.Theanomaliesaremarkedbypointswhosescoresexceedthethresholdvalue.Duetothe
specialfeaturesoftimeseriesdata,afurthergeneralcategorizationcanbeprovidedbasedonthealgorithm’sstrategy
ofscoringtheanomalies.Weincludethisgeneralizationasacomplementtoourtaxonomy.
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 11
*+,(803)
0 1250 2500 3750 5000
!= # − #( )
$,& $,&
0 1250 2500 3750 5000
Fig.7. Resultusing|Z|=16foraautoencoderEncoder(𝐶𝑜𝑛𝑣(64,3)-𝑅𝑒𝑙𝑢()-𝐷𝑒𝑛𝑠𝑒()-𝑇𝑎𝑛ℎ()),Decoder(𝐷𝑒𝐶𝑜𝑛𝑣(64,3)-𝑅𝑒𝑙𝑢()-
𝐷𝑒𝑛𝑠𝑒()-𝑇𝑎𝑛ℎ()).Topplot:Inputtimeseriessnippet.Bottomplot:𝑆(usingmeansquareerror)forallthesub-sequencesoflength80.
Aforecasting-firstapproachfirstinfersthevaluesofinterestedtimeseries,withoutknowingtheactualvaluesofthe
dataset,andthendeterminesifthecomingdatapointsareanomalies(basedontheirdistancetotheinferredvalues).
Thisgivespossibilitiesforstreamingdataanomalydetection.Adata-firstapproach,ontheotherhand,readsthedata
firsttoupdatethemodel.Then,theentiretrainingdatasampleswillbeusedtocomparewiththearrivingdataviathe
detectionmodel.Figure6givesanillustrationofthetwo.
Justlikeforecasting-firstalgorithms,data-firstalgorithmsmayalsobecapableofgeneratingnewsub-sequencesto
comparewithoriginalsequences.Figure7givessuchanexample,wheretheautoencoderreconstructsanestimated
sequence𝑇′ tocalculatetheerror𝑆ontheECGdata.Althoughitbehaveslikeaforecasting-firstmethodbytryingto
𝑖,𝑙
“forecast"theoriginalsub-sequences,itistechnicallydata-firstbecauseitrequiresthearrivalofnewdatatomakevalid
comparisons.
4 SurveyOrganization
Inthefollowingsections,wewillpresenttheState-Of-The-Art(SOTA)inthethreemajorcategoriesandelaborateon
thespecificvariantsoftheSOTAproposedinthepastliterature.Figure8illustratesourdetailedproposedtaxonomy
listingallthemethodsdiscussedinthispaper.Notethat,inFigure8,thenamesofthemethods(thefirstletter)are
positionedonthey-axisbasedontheirpublicationdate.Eventhoughsomeconceptsmightbeanteriortothedate
indicatedinFigure8(forinstancetheconceptofk-meanswasintroducedin1967),thedatescorrespondtothefirst
paperdiscussingtheconceptsappliedtoanomalydetection.Therestofthispaperisorganizedasfollows:
• Wefirstpresentdistance-basedmethodsthatperformanomalydetectionusingdistancecomputationand
comparisonsonpointsorsub-sequencesofthetimeseries.
• Nextweenumeratethedensity-basedmethods.Theseapproachesprocesstimeseriesdataontopofarepresen-
tationthataimstomeasurethedensityofthepointsorsub-sequenceswithinthetimeseriesspace.
• Wefurnishwithtwogroupsofprediction-basedmethodsthataimtopredicttheexpectednormalbehaviors
fromatrainingsetoftimeseries.Thesetwogroupsareforecasting-basedmethods(thatusetheforecastingerror
asanomalyscore)andreconstruction-basedmethods(thataretrainedtoreconstructaninputtimeseriesand
usethereconstructionerrorasanomalyscore).
• Wewillalsoincludeatableofallthemethodsineachsectiontorevealtheirothercharacteristics(suchasthe
requirementforsupervision,thecapabilityofhandlingstreamingdata,etc)ascomplementstoourtaxonomy.
ManuscriptsubmittedtoACM

12 Paparrizosetal.
Anomaly Detection Methods
Distance-based Density-based Prediction-based
Proximity- Clustering- Forecasting-
based based based
Distribution-
1980 based
1985
1990
Encoding-
based
1995 Discord-
based
Graph- Reconstruction-
2000 based based
2005 Tree- based
2010
2015
2020
2023
E HSFD DILO
LOF
KnorrSeq2 F F
SSA
CO ILO CI
KNN
LO CBLOF
DBSCAN
MCOD
DBStream
K-Means
Sequence
Miner
Hybrid-KMeans NormA NorM
TARZAN HOT SAX
MP
DAD
SCRI
Matrix Profile
SAND
PIAMD PSTAM STOM
P SCAM MERLIN MAD
+ MERLIN+ DAMP
MCD
Fast-MCD
MC-MCD TwoFinger
Series2Graph DADS
SurpriseEncode
IForest
Eros-SVMs Hybrid-IForest IF-LOF Extended-IForest
OCSVM
MS-SVDD
NetworkSVM
AOSVM
DeepSVM
HMAD
OC-KFD
S-SVM
MGDD MedianMethod SmartSifter
HBOS
H-ESD SH-ESD SH-ESD+ ConInd COPOD
GrammarViz
GeckoFSM
EM-HMM
PST
Lase E r D -D B B N N KDE-EDBN
NoveltySVR
Ensemble-GI
ES DES TES
ARIMA
PCA
deepPCA RobustPCA
ESN
emiT
Torsk HealthESN
MoteESN CoalESN
LSTM-AD PCI
OceanWNN MTAD-GAT AD-LTI
deepLSTM
Telemanon DeepAnT RePAD MultiHTM RADM
AE
DeepNAP
STORN Enc-Dec-AD
LSTM-VAE DONUT BAGEL OmniAnomaly MSCRED VELC CEA
GAN
NumentaHTM MAD-GAN VAR-GAN TAnoGAN LAMP DeepKMean
Fig.8. IllustrationofAnomalyDetectionTaxonomyforallmethods.
• Afterbrieflydescribingallthemethods,wewilldiscussameta-analysisofthetime-seriesanomalydetection
communitybyexaminingtheevolutionandthetrendsofeachcategory(distance-based,density-based,prediction-
based).Wewillalsohaveacloserlookattheevolutionintimeofproposedmethodsthataresemi-supervised,
unsupervised,andabletohandlemultivariatetimeseries.
• Wewillconcludethissurveywiththeevaluationofsuchmethods.Wewillfirstenumerateexistingbenchmarks
proposedintheliterature,aswellasdifferentevaluationmeasuresandtheirlimitationswhenappliedtotime-
seriesanomalydetection.
5 TimeSeriesNotations
Wenowintroducesomeformalnotationsrelatedtotimeseries.Wedefineatimeseries𝑇 ∈ R𝑛 asasequenceof
real-valuednumbers𝑇
𝑖
∈R[𝑇
0
,𝑇
2
,...,𝑇
𝑛−1
],where𝑛=|𝑇|isthelengthof𝑇,and𝑇
𝑖
isthe𝑖𝑡ℎ pointof𝑇.
Amultivariate,or𝐷-dimensionaltimeseriesT∈R(𝐷,𝑛) isasetof𝐷 univariatetimeseriesoflength𝑛.Wenote
T = [𝑇(0),...,𝑇(𝐷−1)] and for 𝑗 ∈ [0,𝐷 −1], we note the univariate time series𝑇(𝑗) = [𝑇(𝑗),𝑇(𝑗),...,𝑇(𝑗) ]. A
0 1 𝑛−1
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 13
subsequence𝑇 ( 𝑗) ∈Rℓ ofthedimension𝑇(𝑗)ofthemultivariatetimeseries𝑇 isasubsetofcontiguousvaluesfrom𝑇(𝑗)
𝑖 ,ℓ
oflengthℓ(usuallyℓ ≪𝑛)startingatposition𝑖;formally,𝑇 ( 𝑗) [𝑇 (𝑗),𝑇 ( 𝑗 ),...,𝑇 ( 𝑗 ) ].Themultivariatesubsequence
|     |     |     |     | 𝑖 ,ℓ = 𝑖 | 𝑖 + 𝑖 + ℓ −1 |     |
| --- | --- | --- | --- | -------- | ------------ | --- |
1
isdefinedas𝑇 [𝑇 ( 0),...,𝑇 ( 𝐷−1) ].Foragivenunivariatetimeseries𝑇,thesetofallsubsequencesin𝑇 oflengthℓis
|            | 𝑖,ℓ = 𝑖 ,ℓ | 𝑖 ,ℓ             |     |     |     |     |
| ---------- | ---------- | ---------------- | --- | --- | --- | --- |
| definedasT | ={𝑇 ,𝑇     | ,...,𝑇 |𝑇|−ℓ,ℓ}. |     |     |     |     |
ℓ 0,ℓ 1,ℓ
6 Distance-basedMethods
Inthissection,variousdistance-basedanomalydetectionmethodsareintroduced.Weenumeratethemethodsinthree
categoriesdescribedinthefollowingsection.WeenumerateallthementionedmethodsinTable1.
Table1. Summaryofthedistance-basedanomalydetectionmethods.
|     |         |     | SecondLevel     | Prototype       | Dim Method | Stream |
| --- | ------- | --- | --------------- | --------------- | ---------- | ------ |
|     | KNN[91] |     | Proximity-based | NearestNeighbor | M U        | ✗      |
✗
|     | KnorrSeq2[177] |     | Proximity-based | NearestNeighbor | M U |     |
| --- | -------------- | --- | --------------- | --------------- | --- | --- |
|     | LOF[34]        |     | Proximity-based | LOF             | M U | ✗   |
|     | COF[236]       |     | Proximity-based | LOF             | M U | ✗   |
✓
|     | LOCI[178] |     | Proximity-based | LOF | M U |     |
| --- | --------- | --- | --------------- | --- | --- | --- |
|     | ILOF[200] |     | Proximity-based | LOF | M U | ✓   |
✓
|     | DILOF[168]  |     | Proximity-based  | LOF     | M U |     |
| --- | ----------- | --- | ---------------- | ------- | --- | --- |
|     | HSDE[131]   |     | Proximity-based  | LOF     | I U | ✗   |
|     | k-means[91] |     | Clustering-based | k-means | M U | ✗   |
✗
|     | Hybrid-k-means[228] |     | Clustering-based | k-means | M U  |     |
| --- | ------------------- | --- | ---------------- | ------- | ---- | --- |
|     | DeepkMeans[163]     |     | Clustering-based | k-means | M Se | ✗   |
✗
|     | DBSCAN[215]  |     | Clustering-based | DBSCAN | M U |     |
| --- | ------------ | --- | ---------------- | ------ | --- | --- |
|     | DBStream[88] |     | Clustering-based | DBSCAN | M U | ✓   |
|     | MCOD[120]    |     | Clustering-based | -      | I U | ✗   |
✗
|     | CBLOF[93]         |     | Clustering-based | LOF | M U |     |
| --- | ----------------- | --- | ---------------- | --- | --- | --- |
|     | sequenceMiner[38] |     | Clustering-based | -   | I U | ✗   |
✗
|     | NorM(SAD)[23] |     | Clustering-based | NormA | I U |     |
| --- | ------------- | --- | ---------------- | ----- | --- | --- |
|     | NormA[25]     |     | Clustering-based | NormA | I U | ✗   |
|     | SAND[31]      |     | Clustering-based | NormA | I U | ✓   |
✗
|     | TARZAN[115] |     | Discord-based | -   | I S |     |
| --- | ----------- | --- | ------------- | --- | --- | --- |
|     | HOTSAX[114] |     | Discord-based | -   | I U | ✗   |
✗
|     | DAD[258]    |     | Discord-based | -             | I U |     |
| --- | ----------- | --- | ------------- | ------------- | --- | --- |
|     | AMD[257]    |     | Discord-based | -             | I U | ✗   |
|     | STAMPI[262] |     | Discord-based | MatrixProfile | M U | ✓   |
✗
|     | STOMP[269]  |     | Discord-based | MatrixProfile | M U |     |
| --- | ----------- | --- | ------------- | ------------- | --- | --- |
|     | MERLIN[169] |     | Discord-based | MatrixProfile | I U | ✗   |
✗
|     | MERLIN++[170] |     | Discord-based | MatrixProfile | I U |     |
| --- | ------------- | --- | ------------- | ------------- | --- | --- |
|     | SCRIMP[268]   |     | Discord-based | MatrixProfile | I U | ✗   |
|     | SCAMP[271]    |     | Discord-based | MatrixProfile | I U | ✗   |
✓
|     | VALMOD[135] |     | Discord-based | MatrixProfile | I U |     |
| --- | ----------- | --- | ------------- | ------------- | --- | --- |
|     | DAMP[146]   |     | Discord-based | MatrixProfile | I U | ✓   |
✓
|     | LAMP[272] |     | Discord-based | MatrixProfile | I Se |     |
| --- | --------- | --- | ------------- | ------------- | ---- | --- |
I:Univariate;M:Multivariate//S:Supervised;Se:Semi-SupervisedU:Unsupervised
6.1 Proximity-basedMethods
Proximity-basedmethodsusedistancetocloseneighborhoodsasthemainsteptodetectanomalies.Wedetailbelow
twomethodtypesofproximity-basedmethods.
6.1.1 KthNearestNeighbor. Oneofthefirstdistance-basedandproximity-basedmethodsintroducedintheliterature
foranomalydetectionisusingK-thNearestNeighbor(KNN)principle[91].KNN-typemethodsutilizeametricamong
neighboringsub-sequencestoinfertheabnormalityscoresofthetimeseries’sub-sequences.Adistancemeasure
𝑑(·,·)(alsocalleddissimilaritymeasure)isusedtofindthenearestneighborsforeachsubsequence.Commondistance
measuresareEuclidean,Manhatten,oringeneral,Minkowskidistances.Thek-anomalyscoreA𝑘 :{𝑇 𝑖,ℓ}𝑖∈I →Rfor
iscalculatedbasedoneachsub-sequences’𝑘𝑡ℎ
thesetoftimeseries’sub-sequences{𝑇 𝑖,ℓ}𝑖∈I nearestneighborsusinga
ManuscriptsubmittedtoACM

14 Paparrizosetal.
variableaggregationfunction𝑎𝑔𝑔:R𝑘 →R:
A𝑘(𝑇 𝑖,ℓ)= inf 𝑎𝑔𝑔 𝑗∈J 𝑑(𝑇 𝑖,ℓ ,𝑇 𝑗,ℓ) (1)
J⊂I,|J|=𝑘+1
Intheaboveequation,ℓisthefixedlengthoftheslidingwindow,and𝑘+1accountsfortrivialmatches.Followingthe
intuitionof[202]thattheanomalyscoreforasubsequence𝑇 𝑖,ℓ isthedistancetoits𝑘𝑡ℎ nearestneighbor,wecanuse
𝑎𝑔𝑔=(cid:205).AlternativeproposalsforA𝑘 mayutilizeotheraggregationmethods,suchasmedian,minimum,orother
functionsthatpoolthedistancesintoscalarscores.Withdifferentaggregationfunctionsanddistancemetricschoices,
onecanproposedifferentKNN-typemodelsthatareappropriateforvariousanomalydetectionproblems.
InadditiontothestandardKNNtechnique[202],wherethemaximumdistancetothe𝑘𝑡ℎ
nearestneighborisusedas
anomalyscore,othervariantsofKNNshavebeensuggestedbyresearchers.Forinstance,KnorrSeqandKnorrSeq2are
alsotwovariantsofKNNsproposedinthelitterature[177].ThefirstalgorithmKnorrSeqisbasedonatumblingwindow
anddiscoversonlyglobaloutliersbymarkingthosesub-sequencesforwhichatleast𝑝%oftheothersubsequence
arefurtherawaythanathreshold𝐷.TheirsecondalgorithmKnorrSeq2isanimplementationofKNNthatdetects
sub-sequencesasoutliersifatleast𝑝%ofthe𝑘 precedingor𝑘 succeedingsub-sequencesarefurtherawaythana
threshold𝐷.Theanomalyscoreiscalculatedusing(cid:205)astheaggregationfunction:
A𝑘(𝑇 𝑖,ℓ)= inf
∑︁ 1, if𝑑(𝑇 𝑖,ℓ ,𝑇 𝑗,ℓ) >𝐷
(2)
J⊂I,|J|=2𝑘+1,∀𝑗∈J,|𝑗−𝑖|≤𝑘 𝑗∈J0, otherwise

Theanomaloussub-sequencesareselectedusingathreshold𝜏 =𝑝𝑘ontheanomalyscores:A𝑘(𝑇 𝑖,ℓ) <=𝜏.
6.1.2 LocalOutlierFactor. Themostcommonlyusedproximity-basedapproachistheLocalOutlierFactor(LOF)[35],
whichmeasuresthedegreeofbeinganoutlierforeachinstance.Unlikethepreviousproximity-basedmodels,which
directlycomputethedistanceofsub-sequences,LOFdependsonhowtheinstanceisisolatedtothesurrounding
neighborhood.Thismethodaimstosolvetheoutlierdetectiontaskwhereanoutlierisconsideredas“anobservation
thatdeviatessomuchfromotherobservationsastoarousesuspicionthatitwasgeneratedbyadifferentmechanism"
(Hawkinsdefinition[91]).Thisdefinitioniscoherentwiththeanomalydetectiontaskintimeserieswherethedifferent
mechanismcanbeeitheranarrhythmiainanelectrocardiogramorafailureinthecomponentsofanindustrialmachine.
First,let’sconsider𝑇 𝑖,ℓ and𝑇 𝑗,ℓ twosub-sequencesofthesametimeseries.Inthefollowingparagraphs,wenotethese
twosub-sequences,AandB,respectively.Given𝑘-𝑑𝑖𝑠𝑡𝑎𝑛𝑐𝑒(𝐴)thedistancebetween𝐴andits𝑘𝑡ℎ
nearestneighbor
(𝑁 𝑘(𝐴)thesetofthese𝑘neighbors),LOFisbasedonthefollowingreachabilitydistancedefinition:
𝑟𝑑 𝑘(𝐴,𝐵)=𝑚𝑎𝑥(𝑘-𝑑𝑖𝑠𝑡𝑎𝑛𝑐𝑒(𝐵),𝑑(𝐴,𝐵)) (3)
AsillustratedinFigure9,themainconceptbehindthisdistancedefinitionistostressoutthehomogeneityof
distancesbetweeninstanceswithinthe𝑘-neighborhood(i.e.,the𝑘-neighborhoodwillhavethesamedistancebetween
eachother).Thusthelocalreachabilitycanbedefinedasfollow:
𝑙𝑟𝑑 𝑘(𝐴)=
(cid:205)
𝐵∈𝑁𝑘
|𝑁
(𝐴
𝑘
)
(
𝑟
𝐴
𝑑
)
𝑘
|
(𝐴,𝐵)
(4)
Givenaninstance,𝐴,𝑙𝑟𝑑 𝑘(𝐴)istheinverseoftheaveragereachabilityofAfromitsneighborhood,i.e.,theaverage
distanceatwhich𝐴canbereachedfromitsneighbors.Therefore,LOFisgivenby:
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 15
rd(A,B)
 B k
 B
rd(A,B)
|     |     | k   | A   |     |
| --- | --- | --- | --- | --- |
 C
A
rd(A,C) k
| rd (A,C) |     |  D  |     |     |
| -------- | --- | --- | --- | --- |
k
 C
| (a) Reachability distance  |     | (b)    Local reachability density  |     |     |
| -------------------------- | --- | ---------------------------------- | --- | --- |
Fig.9. (a)ReachabilitydistancebetweenAandB,AandCfor𝑘=4.(b)Differencebetween𝑟𝑑 𝑘(𝐴,𝑋),𝑋 ∈𝑁 𝑘(𝐴),whenAisan
anomalyandB,C,andDareregularinstances.
|           |                      | (cid:205) | 𝑙𝑟𝑑𝑘(𝐵) |     |
| --------- | -------------------- | --------- | ------- | --- |
|           | (cid:205) 𝑙𝑟𝑑𝑘(𝐵)    | 𝐵∈𝑁𝑘(𝐴)   |         |     |
|           | 𝐵∈𝑁 𝑘( 𝐴 ) 𝑙 𝑟 𝑑𝑘(𝐴) | 𝑁         | 𝐴       |     |
| 𝐿𝑂𝐹 𝑘(𝐴)= |                      | = |       | 𝑘 ( ) | |     |
|           | |𝑁 𝐴                 | 𝑙 𝑟       | 𝑑 𝐴     | (5) |
|           | 𝑘 ( ) |              |           | 𝑘 ( )   |     |
Intuitively,the𝐿𝑂𝐹 ofaninstanceistheaverageofthelocalreachabilitydensityoftheneighborsdividedbyits
𝑘
ownreachabilitydensity.Therefore,ifwesetsub-sequencesoflengthℓasthelengthofthesub-sequence,thisfactor
canbeusedasananomalyscore.
Inthepastdecade,researchersalsosuggestedmanyvariantsoftheLOFmethod[35].COF[236],forexample,is
aconnectivity-basedvariantofLOF.Itindicateshowfarawayapointshiftsfromapattern,adjustingthenotionof
isolationtonotdependonthedensityofdataclouds.LOCI[178]isanotherLOF-likealgorithmthatutilizesdifferent
statistics(correlationintegralandMDEF)toinferindividualpoints’isolation.OtherLOFvariantsaretheILOF[200]
andDILOF[168]method,whichadoptsafasteralgorithmanddetectsanomaliesincrementally.Finally,thehierarchy-
segmentation-baseddataextractionmethod(HSDE)[131]isinspiredbythestrategyofLOFtodetectabnormalpoints
intimeseries.
6.2 Discord-basedMethods
ApracticalmodificationtotheKNN-typemodelistousethediscord,whichevolvesfromcomparingdistancestothe
nearestneighbortocomparingdistancestothe𝑘𝑡ℎ neighbor.Suchadaptationsassistinedgeconditionswhereasmall
numberofanomaliesareclusteredalongwithlimiteddistances,andtheconventionalKNNapproachstrugglesto
recognizethem.Thefollowinggivesthespecificdefinitionsofdiscord:
Definition6.1(Top-k𝑚𝑡ℎ [25,37,70,116,144,147,219,261]Supposethewindowisoflengthℓ.Given
-discord).
acollectionofsub-sequences{𝑇 𝑗,ℓ}𝑗∈I,let𝑓 denote𝑚𝑡ℎ -discordfunctionmeasuringthedistanceto𝑚𝑡ℎ nearest
𝑚
| 𝑚   |     |     | isaTop-k𝑚𝑡ℎ |     |
| --- | --- | --- | ----------- | --- |
neighborhoodsothat𝑓 𝑚(𝑇 𝑗,𝑙) =min 𝑑(𝑇 𝑖,𝑙 ,𝑇 𝑗,𝑙).Asub-sequence𝑇 𝑖,ℓ -discordif𝑓 𝑚(𝑇 𝑖,ℓ)isthe
𝑗∈I\{𝑖}
𝑘𝑡ℎ
maximumamongtheset{𝑇 𝑗,ℓ}𝑗∈I.
Notethatthe𝑚𝑡ℎ -discordisthespecialcaseofTop-k𝑚𝑡ℎ
|     |     | -discordwhen𝑘 | =1,anddiscordisthespecialcaseof |     |
| --- | --- | ------------- | ------------------------------- | --- |
𝑚𝑡ℎ -discordwhen𝑚=1.
ManuscriptsubmittedtoACM

16 Paparrizosetal.
Top-1 1st-discord
1stNN
1stNN
2ndNN
Top-1 2nd-discord Top-2 1st-discord
Fig.10. Adatasetwith16sub-sequences(ofthesamelengthℓ)depictedaspointsin2-dimensionalspace;12sub-sequencesare
normal(hollowpoints),and4areanomalous(solid,redpoints).
Figure10illustratesthesenotionswithanexample,whereforeaseofexposition,werepresenteachsub-sequenceas
apointin2-dimensionalspace.Thefiguredepictstwo1 𝑠𝑡 -discords:thediscordinthetop-right(𝑇𝑜𝑝-1)hasits1-NN
atalargerdistancethanthediscordinthebottom-right(𝑇𝑜𝑝-2).Thefigurealsoshowsagroupoftwoanomalous
sub-sequences:oneofthemisthe𝑇𝑜𝑝-12 𝑛𝑑 -discord,andtheothersub-sequenceisits1-NN(alsoadiscord).
Thereexistseveralstudiesthathaveproposedfastandscalablediscorddiscoveryalgorithmsinvarioussettings[37,
70,116,144,147,219,259,261],includingsimpleand𝑚𝑡ℎ -discords1,in-memoryanddisk-awaretechniques,exactand
approximatealgorithms,usingeithertheirSymbolicAggregateApproximation(SAX)[116,219]orHaarwavelets
[37,70].Inthefollowingsections,wepresentthestate-of-the-artsolutionstothesub-sequenceanomalydetection
problem.Notethatinthisdiscussion,wefocusonthe𝑇𝑜𝑝-𝑘anomalies(usinginsteadathreshold𝜖todetectanomalies
wouldbeastraightforwardmodificationofthesolution).
DiskAwareDiscordDiscoverymethod(DAD)[259]isamethodthatproposesanewexactalgorithmtodiscover
discordrequiringonlytwolinearscansofthediskthoughtformanagingverylargedatasets.Thealgorithmusesthe
rawsequencesdirectly.First,itaddressesthesimplerproblemofdetectingrangediscord,thengeneralizestheproblem
todetectthe𝑇𝑜𝑝-𝑘discord.
OtherthanDAD,severalotherdiscord-likeanomalyidentificationapproacheshavealsobeenproposed.TARZAN[115]
isadiscordmethodviaSAXdiscretizationthroughtheslidingwindow.Theapproachprocessesdatabybuildinga
suffixtreeandcalculatingitsanomalyscorebyapplyinginferencesonthediscord.LikeTARZAN,HOTSAX[114]
alsoadoptsSAXdiscretizationthroughouttheprocessingstep;itthenmeasuresthedistancetothenearestnon-self
matchforsub-sequencestoidentifyabnormalities.AMD[257]furtherimprovesHOTSAX,whichperformsdynamic
segmentationtovarythewindowlength.
Asafinalnote,weobservethatinsituationswithmultiplesimilaranomalies,weshouldeitheruseamethodthat
supports𝑚𝑡ℎ
-discords,oruseasimplediscord(i.e.,1
𝑠𝑡
-discord)methodasfollows.Startingatthebeginningofthe
seriesandproceedingtotheright,weapplythediscordmethodbyonlyconsideringthepointstotheleftofthecurrent
position,andeverytimeananomalyisdetected,wesearchtheentireseriesforsimilaranomalies(thiswillrevealall
occurrencesofthemultiplesimilaranomalies).Asweproceedtotheright,thediscordmethodwilldetectonlythe
firstoccurrenceofeachsetofsimilaranomalies(therestbeingdetectedbythesimilaritysearchoperationmentioned
1Theauthorsofthesepapersdefinetheproblemas𝑘𝑡ℎ-discorddiscovery.
ManuscriptsubmittedtoACM

| DiveintoTime-SeriesAnomalyDetection:ADecadeReview |      |                                          |     |         |     |      |                                         |        |        |     | 17  |
| ------------------------------------------------- | ---- | ---------------------------------------- | --- | ------- | --- | ---- | --------------------------------------- | ------ | ------ | --- | --- |
|                                                   |      |                                          |     | Discord |     |      |                                         | Motifs |        |     |     |
|                                                   | (a1) |                                          |     |         |     | (b1) |                                         |        |        |     |     |
|                                                   | 0    | 100                                      | 200 | 300     | 400 | 0    | 100                                     | 200    | 300    | 400 |     |
|                                                   | (a2) |                                          |     |         |     | (b2) |                                         |        |        |     |     |
|                                                   | 0    | 100                                      | 200 | ! 300   | 400 | 0    | "′100                                   | 200    | "′′300 | 400 |     |
|                                                   |      | (a) Discord finding using matrix profile |     |         |     |      | (b) Motifs finding using matrix profile |        |        |     |     |
Fig.11. (a)Matrixprofile(𝑎 2)appliedontheSED(Nasadiskfailuredatasets)timeseriessnippet(𝑎 1).Thehighestvalueinthematrix
profile(𝑎 1)pointstothediscordoftheSEDtimeseries.(b)Matrixprofile(𝑏 2)appliedonasynthetictimeseries(𝑏 1).Thesmallest
| valuesinthematrixprofile(𝑎 |     | 1)pointtoamotifpairinthetimeseries. |     |     |     |     |     |     |     |     |     |
| -------------------------- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
above).Notethatthissolutionimpliesthatwehaveaccumulatedenoughdataatthebeginningoftheseriesforthefirst
executionofthediscordmethod.
6.2.1 MatrixProfile. MatrixProfile[261,270]isadiscord-basedmethodthatrepresentstimeseriesasamatrixof
closestneighbordistances.Comparedtoitspredecessor,MatrixProfileproposedanewmetadatatimeseriescomputed
effectively,capableofprovidingvariousvaluabledetailsabouttheexaminedtimeseries,suchasdiscords.Forsimplicity,
wecancallthismetadataseriesmatrixprofile,andwecandefineitasfollows:
|     |     |     | Amatrixprofile𝑀𝑃 |     | ofatimeseries𝑇 |     | oflength𝑛isatimeseriesoflength𝑛−ℓ−1 |     |     |     |     |
| --- | --- | --- | ---------------- | --- | -------------- | --- | ----------------------------------- | --- | --- | --- | --- |
Definition6.2(MatrixProfile).
wherethe𝑖𝑡ℎ elementof𝑀𝑃 containstheEuclideannormalizeddistanceofthesub-sequenceoflengthℓof𝑇 starting
at𝑖toitsnearestneighbor.
However,thelatterdefinitiondoesnottelluswherethatneighborislocated.Thisinformationisrecordedinthe
matrixprofileindex:
Definition6.3(MatrixProfileIndex). Amatrixprofileindex𝐼 isavectoroftheindexwhere𝐼 𝑀𝑃[𝑖] = 𝑗 and𝑗 isthe
𝑀𝑃
indexofthenearestneighborof𝑖.
TwogeneraldefinitionsofJoinmatrixcomputationcanbeinferred.Thefirst,calledSelf-Join,correspondsexactlyto
thematrixprofile.Thesecond,calledJoin,correspondstothesameoperationfortwodifferenttimeseries.Formallywe
havethefollowing:
Definition6.4(TimeSeriesSelf-Join). Givenatimeseries𝑇,theself-joinof𝑇 withsub-sequencelengthℓ,denotedby
𝑇⊲⊳ 𝑇,isametatimeseries,where:|𝑇⊲⊳ 𝑇|=|𝑇|−ℓ+1and∀𝑖.1≤𝑖 |𝑇⊲⊳ 𝑇|,(𝑇⊲⊳ 𝑇)𝑖,1 =𝑑𝑖𝑠𝑡(𝑇 𝑠𝑡𝑁𝑁 of𝑇
| ℓ   |     |     |     | ℓ   |     |     | ≤ ℓ |     | ℓ   | 𝑖,ℓ,1 | 𝑖,ℓ). |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- |
Definition6.5(TimeSeriesJoin). Giventwotimeseries𝐴and𝐵,andasub-sequencelengthℓ,the 𝐽𝑜𝑖𝑛between
| 𝐴 𝐵 |     | (𝐴⊲⊳ | 𝐵), |     |     | |𝐴⊲⊳ | 𝐵|  | |𝐵| −ℓ |     | ∀𝑖.1 𝑖 | |𝐴⊲⊳ 𝐵|, |
| --- | --- | ---- | --- | --- | --- | ---- | --- | ------ | --- | ------ | -------- |
and denoted by ℓ is a meta time series, where: ℓ = +1 and ≤ ≤ ℓ
| (𝐴⊲⊳ 𝐵)𝑖,1 | =𝑚𝑖𝑛(𝑑𝑖𝑠𝑡(𝐵 | ,𝐴  | 1,ℓ),...,𝑑𝑖𝑠𝑡(𝐵 | ,𝐴  | |𝐴|−ℓ+1,ℓ)). |     |     |     |     |     |     |
| ---------- | ----------- | --- | --------------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
| ℓ          |             | 𝑖,ℓ |                 | 𝑖,ℓ |              |     |     |     |     |     |     |
ThesemetadataarecomputedusingMueen’sultra-fastAlgorithmforSimilaritySearch(MASS)[166]thatrequires
just𝑂(𝑛∗𝑙𝑜𝑔(𝑛))timebyexploitingtheFastFourierTransform(FFT)tocalculatethedotproductsbetweenthequery
andallthesub-sequencesofthetimeseries.Oncethesemetadataaregenerated,retrievingthe𝑇𝑜𝑝-𝑘discordispossible
ManuscriptsubmittedtoACM

18 Paparrizosetal.
byconsideringthemaximumvalueoftheMatrixProfileandorderingit,excludingthetrivialmatches(overlapping
sub-sequences).Retrievingthesub-sequenceswiththeshortestdistancetotheirnearestneighbor(called𝑚𝑜𝑡𝑖𝑓𝑠)is
alsopossible.Thesesub-sequencescorrespondtoarecurrentmotifinthetimeseriesandcanbeusefulintheanomaly
search.
Figure11showsanexampleoftheMatrixProfilemetadata.Ontheonehand,Figure11(a)showsthattheidentified
discordcorrespondstoasub-sequencethatdeviatessignificantlyfromthenormalcycles.Ontheotherhand,Figure11
(b)showsthatthesingularshapesarewell-identifiedasmotifs.
AfamilyofMatrixProfileanomalydetectionmethodshasalsobeenproposedinthelastdecade.STAMP[262]
proposedanalgorithmthatcanprovideanaccurateansweratanytimeduringthefullcomputationwithtimecomplexity
of𝑂(𝑛2𝑙𝑜𝑔(𝑛)).STAMPI[262]notonlyperformsthestandardall-pairs-similarity-joinofsub-sequencesformatrix
profilemethodsbutalsoadaptsthemethodincrementallytoaccommodatestreamingpurposes.STOMP[269],basedon
STAMP,developedafasteralgorithmtakingadvantageofthesub-sequencesorderandachievingthecomputationwith
timecomplexityof𝑂(𝑛2).Moreover,aGPUimplementationofSTOMPhasbeenproposed.LikeSTOMP,SCAMP[271]
alsoadoptsGPUforthematrixprofileanomalydetectionprocess.TheSCRIMPmethod[268]combinestheSTAMP
algorithm(anytime)andSTOMP(ordered)tomakeahybridapproach.Moreover,theLAMPapproach[272]isableto
computeaconstanttimeapproximationoftheMPvaluegivenanewlyarrivingtimeseriessubsequence.Whileevery
aforementionedmethodcanextractdiscordsofapredefinedlength,VALMOD[134]andMAD[136]havebeenproposed
toextractdiscordsofvariablelengthwithinapredefinedlengthinterval.Moreover,MERLIN[169]andMERLIN++[170]
havebeenproposedtoidentifydiscordsofarbitrarylength.Finally,DAMP[146],adiscord-basedmethod,isableto
workononlinesettings,andscaletofast-arrivingstreams.
6.3 Clustering-basedMethods
Approachesbasedonclusteringstrategieshavebeenproposedfortheanomalydetectiontask.Themainideabehind
thesemethodsistopartitionthesub-sequencespaceandthenevaluatehowonesub-sequencefitsintothepartition.
6.3.1 K-meansMethod. Thek-meansclusteringalgorithmisawidelyusedunsupervisedlearningtechniqueindata
miningandmachinelearning.Itsmainobjectiveistopartitionagivendatasetinto𝑘distinctclusters,whereeachdata
pointbelongstotheclusterwiththeclosestmeanvalue.Thealgorithmoperatesiteratively,startingwithaninitial
randomassignmentof𝑘centroids.Forthespecificcaseoftimeseries,theEuclideanortheDTWdistanceiscommonly
used.K-meansalgorithmcanalsobeusedforanomalydetectionintimeseries[91].Thecomputationalstepsarethe
following:
• Allthesub-sequencesofagivenlengthℓ(providedbytheuser)areclusteredusingthek-meansalgorithm.The
Euclideandistanceisused,andthenumberofclustershastobeprovidedbytheuser.
• Oncethepartitionislearned.Wecomputetheanomalyscoresofeachsub-sequencebasedonthedistancetothe
centroidofitsassignedcluster.
• Thelargerthedistance,themoreabnormalthetimeserieswillbeconsidered.
Suchamethodisstraightforwardbuthasbeenshowntobeveryeffectiveforthespecificcaseofmultivariatetime
series[216].Moreover,extensionssuchasHybrid-k-means[228]canbeusedforanomalydetectionaswell.Finally,the
k-meansmethodcanbeusedontopofotherpre-processingandrepresentationsteps.Forinstance,DeepKMeans[163]
usesanAutoencodertolearnalatentrepresentationofthetimeseriesandappliesk-meansontopofthelatentspaceto
identifyanomalies.
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 19
6.3.2 DBSCAN. Anothercommonlyusedclustering-basedmethodistheDensity-BasedSpatialClusteringofAppli-
cationwithNoisealgorithm(DBSCAN)[215].Whenidentifyinganomalies,DBSCANmarksdatapointsintothree
categories:(i)corepoints,(ii)borderpoints,and(iii)anomalies.Toclassifythepoints,twonon-parametricparameters
areimportanttodetectthepotentialanomaliesusingDBSCAN:theradius𝜖ofneighborsoftheanalyzedpointandthe
minimumnumber𝜇ofpointsineachnormalcluster.Giventheseparameters,onecanidentifytheanomalousfollowing
thecategorizationofthesub-sequencesasfollows:
• A𝜖−neighborhoodof𝑇 𝑖,ℓ is𝐵 𝜙(𝑇 𝑖,ℓ ,𝜖)∩𝑇,where𝑇 isthetrainingdata{𝑇 𝑖,ℓ}𝑖∈𝐼.And𝐵 𝜙(𝑇 𝑖,ℓ ,𝜖)istheballof
radius𝜖centeredat𝑇
𝑖,ℓ
withrespecttothenorm𝜙(·,·).
• 𝑇 𝑖,ℓ isacorepointifthesizeofthe𝜖−neighborhoodof𝑇 𝑖,ℓ isgreaterthan𝜇.
• 𝑇 𝑖,ℓ isaborderpointif𝑇 𝑖,ℓ containsacorepointinits𝜖−neighborhood.
• 𝑇 𝑖,ℓ isidentifiedasananomaloussub-sequenceif𝑇 𝑖,ℓ isneitherabordernoracorepoint.
DBSCANhasbeenappliedforanomalydetectiononaunivariatetimeseriesthatcontainsobservationswithaverage
dailytemperatureover33years[41].Theprocessingstepistofirstconvertthedatasetintosub-sequencessetwitha
slidingwindow,whicharefurtherz-normalized.Aftertheprocessingstep,DBSCANisappliedtothesub-sequences,
andtheanomaliesaredetectedaccordingly,asthemethodaboveprescribes.Similarclusteringapproachessuchas
DBStream[88]canbeusedforanomalydetection.
6.3.3 OtherClustering-basedMethods. Anotherclustering-basedtime-seriesanomalydetectionmethodistheMCOD[120]
method.MCODmaintainsasetofmicro-clusterscontainingonlynormalobjects(inourcase:sub-sequences)toeffi-
cientlyandrobustlydetectoutliersintheeventstream.MCODdeterminesanobject𝑥 asanoutlierifthereareless
than𝑘clustersatadistanceof𝑅from𝑥.Wecanrepresentthisbinarydecisionusingthefollowingproductfunction:
A𝑘(𝑇 𝑖,ℓ)= inf
(cid:214) 1, if𝑑(𝑇 𝑖,ℓ ,𝑇 𝑗,ℓ) >𝑅
(6)
J⊂I,|J|=𝑘+1𝑗∈J0, otherwise

Thefunctionabovereturnsdiscretevalues1and0only.SoA𝑘 is1ifandonlyifall𝑘 nearestneighborsareat
least𝑅distanceapartfromtheconsideredsubsequence.Moreover,duetoitssimilaritywithKNN-basedmethods,itis
importanttonotethatMCODcanalsobeassociatedwithproximity-basedapproaches.
Anotherclustering-basedapproachisCBLOF[93],aLOF-basedclusteringalgorithm,whichfirstclustersthedata
andthenassignstheCBLOFfactortoeachentrytomeasureboththesizeandrelativeofandamongtheindividual
clusters.
Then,Sequenceminer[38]isanapproachproposedbyNASA.Itclustersthesequencesusingthelongestcommon
sub-sequence(LCS)metricandranksclustermembersbasedonLCS,andselectsthetop𝑝%asanomalies.Theanomalies
areidentifiedbythepartsofthesequencethatdifferthemostandcharacterizesanomalousedit.
Morerecently,NormA[23–25]isaclustering-basedalgorithmthatsummarizesthetimeserieswithaweightedset
ofsub-sequences.Thenormalset(weightedcollectionofsub-sequencestofeaturethetrainingdataset)resultsfroma
clusteringalgorithm(Hierarchical),andtheweightsarederivedfromclusterproperties(cardinality,extra-distance
clustering,timecoverage).AnextensionofNormA,calledSAND[31],hasbeenproposedforstreamingtimeseries.
ThemaindifferencebetweenNormAandSANDliesintheapproachusedtoupdatetheweightinastreamingmanner.
Additionally,theclusteringstepinSANDisperformedusingthek-Shapemethod[183,184,189],whereasNormA
employsahierarchicalclusteringmethod.
ManuscriptsubmittedtoACM

20 Paparrizosetal.
7 Density-basedMethods
Unlikedistance-basedapproaches,thedensity-basedapproachdoesnottreatthetimeseriesassimplenumericalvalues
butimbuesthemwithmorecomplexrepresentations.Thedensity-basedmethodprocessestimeseriesdataontop
ofarepresentationofthetimeseriesthataimstomeasurethedensityofthepointsorsub-sequencespace.Such
representationvariesfromgraphs,trees,andhistogramstoagrammarinductionrule.Thedensity-basedmodelshave
foursecond-levelcategories:distribution-based,graph-based,tree-based,andencoding-based.Weenumerateallthe
mentionedmethodsinTable2.
| Table2. Summaryofthedensity-basedanomalydetectionmethods. |                    |           |            |        |
| --------------------------------------------------------- | ------------------ | --------- | ---------- | ------ |
|                                                           | SecondLevel        | Prototype | Dim Method | Stream |
| FAST-MCD[210]                                             | Distribution-based | MCD       | M Se       | ✗      |
| MC-MCD[89]                                                | Distribution-based | MCD       | M Se       | ✗      |
✗
| OCSVM[150] | Distribution-based | SVM | M Se |     |
| ---------- | ------------------ | --- | ---- | --- |
| AOSVM[81]  | Distribution-based | SVM | M U  | ✓   |
✗
| Eros-SVMs[124] | Distribution-based | SVM | M Se |     |
| -------------- | ------------------ | --- | ---- | --- |
| S-SVM[20]      | Distribution-based | SVM | I Se | ✗   |
| MS-SVDD[253]   | Distribution-based | SVM | M Se | ✗   |
✗
| NetworkSVM[266] | Distribution-based | SVM | M Se |     |
| --------------- | ------------------ | --- | ---- | --- |
| HMAD[87]        | Distribution-based | SVM | I Se | ✗   |
✗
| DeepSVM[250] | Distribution-based | SVM | M U  |     |
| ------------ | ------------------ | --- | ---- | --- |
| HBOS[79]     | Distribution-based | -   | M U  | ✗   |
| COPOD[133]   | Distribution-based | -   | M U  | ✗   |
| ConInd[7]    | Distribution-based | -   | M Se | ✗   |
| MGDD[233]    | Distribution-based | -   | M U  | ✓   |
✗
| OC-KFD[208]      | Distribution-based | -   | M U |     |
| ---------------- | ------------------ | --- | --- | --- |
| SmartSifter[256] | Distribution-based | -   | M U | ✓   |
| MedianMethod[18] | Distribution-based | -   | I U | ✓   |
| S-ESD[97]        | Distribution-based | ESD | I U | ✗   |
| S-H-ESD[97]      | Distribution-based | ESD | I U | ✗   |
✗
| SH-ESD+[244]   | Distribution-based | ESD | I U  |     |
| -------------- | ------------------ | --- | ---- | --- |
| TwoFinger[156] | Graph-based        | -   | I Se | ✗   |
| GeckoFSM[214]  | Graph-based        | -   | M S  | ✗   |
✗
| Series2Graph[26] | Graph-based | Series2Graph | I U |     |
| ---------------- | ----------- | ------------ | --- | --- |
| DADS[217]        | Graph-based | Series2Graph | I U | ✗   |
✗
| IForest[139]        | Tree-based | IForest     | M U |     |
| ------------------- | ---------- | ----------- | --- | --- |
| IF-LOF[53]          | Tree-based | IForest/LOF | M U | ✗   |
| ExtendedIForest[90] | Tree-based | IForest     | M U | ✗   |
✗
| HybridIForest[157] | Tree-based     | IForest | M Se |     |
| ------------------ | -------------- | ------- | ---- | --- |
| SurpriseEncode[42] | Encoding-based | -       | M U  | ✗   |
✗
| GranmmarViz[220] | Encoding-based | -         | I U |     |
| ---------------- | -------------- | --------- | --- | --- |
| EnsembleGI[71]   | Encoding-based | -         | I U | ✗   |
| PST[234]         | Encoding-based | MarkovCh. | M U | ✗   |
✓
| EM-HMM[193]   | Encoding-based | MarkovCh.    | M Se |     |
| ------------- | -------------- | ------------ | ---- | --- |
| LaserDBN[173] | Encoding-based | BayseianNet. | M Se | ✗   |
✗
| EDBN[195]     | Encoding-based | BayseianNet. | M Se |     |
| ------------- | -------------- | ------------ | ---- | --- |
| KDE-EDBN[196] | Encoding-based | BayseianNet. | M Se | ✗   |
| PCA[223]      | Encoding-based | PCA          | M Se | ✗   |
✗
| RobustPCA[174] | Encoding-based | PCA | M U  |     |
| -------------- | -------------- | --- | ---- | --- |
| DeepPCA[44]    | Encoding-based | PCA | M Se | ✗   |
✗
| POLY[260] | Encoding-based | -   | I U |     |
| --------- | -------------- | --- | --- | --- |
| SSA[260]  | Encoding-based | -   | I U | ✗   |
I:Univariate;M:Multivariate//S:Supervised;Se:Semi-SupervisedU:Unsupervised
7.1 Distribution-basedMethods
Thefirstcategoryofdensity-basedapproachesisdistribution-basedanomalydetectionapproaches.Distribution-based
methodsinvolvebuildingadistributionfromstatisticalfeaturesofthepointsorsub-sequencesofthetimeseries.By
examiningthedistributionsoffeaturesofthenormalsub-sequences,thedistribution-basedapproachtriestorecover
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 21
relevantstatisticalmodels.Itusesthemtoinfertheabnormalityofthedata.Inthefollowingsections,wedescribe
importantanomalydetectionmethodsbelongingtothiscategory.
7.1.1 MinimumCovarianceDeterminant. TheMinimumCovarianceDeterminant(MCD)isacommondistribution-
basedstatisticinuse[209].Thealgorithmseekstofindasubset(ofagivensizeℎ)ofallthesequencestoestimate𝜇
(meanofthesubset)and𝑆(covariancematrixofthesubset)withminimaldeterminant.Inotherwords,theobjectiveis
tofindthesubsetthatistheleastlikelytoincludeanomalies.Oncetheestimationisdone,Mahalanobisdistanceis
utilizedtocalculatethedistancefromsub-sequencestothemean,whichisregardedastheanomalyscore.
FAST-MCD[210]isafasterversionoftheMCDalgorithm.Withinsmalldatasets,theresultoftheFAST-MCD
algorithmusuallyalignswiththatoftheexactMCD.Incontrast,fasterandmoreaccurateresultsarederivedthrough
theFAST-MCDratherthantheclassicalMCDforlargetimeseries.Finally,MC-MCD[89],anextensionofMCD,has
beenproposedforthemulti-clustersetting.
7.1.2 One-ClassSVM. One-ClassSupportVectorMachine(OCSVM)isatypicaldistribution-basedexample,which
aimstoseparatetheinstancesfromanoriginandmaximizethedistancefromthehyperplaneseparation[218]or
sphericalseparation[238].Theanomaliesareidentifiedwithpointsofhighdecisionscore,i.e.,farawayfromthe
separationhyper-plane.ThismethodisavariantoftheclassicalSupportVectorMachineforclassificationtasks[94].
Mathematically,givenℓ-dimensionaltrainingdatapoints𝑥 0 ,...𝑥 𝑛 ∈X,a.non-linearfunction𝜙 thatmapthefeature
spaceXtoadotproductspace𝐹,akernel𝑘(𝑥,𝑦)=(𝜙(𝑥),𝜙(𝑦))(usuallysettoaGaussiankernel𝑘(𝑥,𝑦)=𝑒−||𝑥−𝑦||2/𝑐
),
thequadraticprogramtosolveusingahyperplaneisthefollowing:
1 1 ∑︁
min ||𝑤||2+ 𝜉 𝑖 −𝜌
𝜔∈𝐹,𝜉∈R,𝜌∈R2 𝜈ℓ
𝑖
subjectto:(𝜔.𝜙(𝑥 𝑖)) ≥𝜌−𝜉 𝑖 ,
𝜉
𝑖
≥0.
Foragivennewinstance𝑥,byderivingthedualproblem,thedecisionfunctioncanbedefinedasfollow:
∑︁
𝑓(𝑥)=𝑠𝑔𝑛( 𝛼
𝑖
𝑘(𝑥
𝑖
,𝑥)−𝜌)
𝑖
Assumingthattheoptimizationproblemabovecanbesolved,wecanusesuchadecisionfunctionasananomaly
score.Tobeabletodoit,onehastoensuretotraintheOCSVMmodelonanormalsectionofthetimeseriesonly(those
havetobeannotatedbyaknowledgeexpertandthereforerequireextraworktobeused).Figure12illustratesthe
anomalydetectionprocess.ItisalsoimportanttonotethatOCSVMisverysimilartoSupportvectorDataDescription
(SVDD)thathasalsobeenusedforanomalydetection[253].
Inrecentdecades,anarrayofSVMvariantshavebeenappliedinthetimeseriessetting.AOSVM[81]isanefficient
streaminganomalydetectionalgorithmbasedonSVMthataccommodatesSVMtoanonlinedetection.Themodel
isalsoadaptive,i.e.,itforgetsolddata,featuringlowcomputationalandmemoryrequirements.Eros-SVMs[124]is
anothervariantoftheSVMalgorithm.Itadoptsasemi-supervisedapproachtotrainthemodelinthenormaldata.The
algorithmthenmeasurestimewindows’metricsasfeaturesfedintomultipleOCSVMs,whicharefurtherselected
basedontheEROSsimilaritymetric.Moreover,multipleothermethodsbasedonOCSVMhavebeenproposedinthe
literature.ThesemethodseitherproposeprocessingstepsbeforeapplyingOCSVM(suchasNetworkSVM[266]or
ManuscriptsubmittedtoACM

22 Paparrizosetal.
𝑁𝑜𝑟𝑚𝑎𝑙
𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒𝑠
𝜌
𝜉
!
𝜔 𝜉
"
𝑂𝑟𝑖𝑔𝑖𝑛𝑂 𝐴𝑏𝑛𝑜𝑟𝑚𝑎𝑙
𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒𝑠
Fig.12. OCSVMillustrationinwhichapointcorrespondstoasubsequenceandonlythegreenpointsareprovidedforthetraining
step.
S-SVM[20]thatproposedseasonalitydecompositionorStockwelltransformation)orcombineOCSVMwithother
methods(suchasHMAD[87]thatuseshiddenMarkovchaintorepresentthetimeseriesintoalatentspace,onwhich
OCSVMisapplied).Finally,DeepSVM[250]proposestouseanAutoencoderarchitecturetoextractmeaningfulfeatures
thatuseOCSVMontopofthelearnedlatentspacetodetectanomalies.
7.1.3 Histogram-basedOutlierScore. Histogram-basedOutlierScore(HBOS)[79]isanotherdistribution-basedal-
gorithmforanomalydetection.Foreverysingledimension(i.e.,timestampsofasub-sequenceforunivariatetime
seriesorvaluesacrossmultipledimensionsformultivariatetimeseries),aunivariatehistogramisconstructedwith
𝑘equalwidthbins.Eachhistogramisfurthernormalizedsothattheheightis1.Foragivenmultivariatepoint𝑝(or
univariatesub-sequence𝑇 𝑖,ℓ),wecountthebinthatcontains𝑝foreachdimensionandmultiplytogethertheinverseof
thefrequencyofbinswhere𝑝belongsforalldimensions.ThealgorithmassumesmutualIndependenceamongthe
timeseries’dimensions(orthetimestampsforunivariatesub-sequenceanomalydetection).Moreover,HBOSsuitsthe
particularcaseofhighlyunbalancedtimeseries(i.e.,veryfewanomalies)andunknowndistribution.
7.1.4 ExtremeStudentizedDeviate. Variousstatistics,suchasExtremeStudentizedDeviate(ESD),areusefulforinferring
timeseriesabnormality.Thelattercomputesthestatisticaltestfor𝑘extremevaluesby𝐶
𝑘
=max𝑘|𝑥
𝑘
−𝑥¯|/𝑠,where𝑥¯
and𝑠denotethemeanandthevariance.Thetestisthencomparedwithothercriticalvaluestodetermineifavalueis
abnormal.Ifso,thenthevalueisremoved,andthestatisticaltestisre-calculatediteratively.BuiltonESD,theS-ESD
andSH-ESD[97]methodsremovetheseasonalcomponentusingSeasonal-Trenddecomposition(STL)andsubtractthe
robustmedian.Thepure,normalizeddataisthenappliedwithESDtodetectanomalies.SH-ESD+[244],onafurther
stepthanSH-ESD,appliestheSTLdecompositionusingaLoessregressionandthengeneralizestheESDontheresidual
partofseasonaldecompositiontodetectanomalies.
7.1.5 Other Distribution-based Methods. Besides the distribution-based algorithms presented above, many other
methodsareproposedusingdifferentmodels.First,theMedianMethod[18]isasimpleanomalydetectionmethod
proposedinitiallytofilteroutliers.Themainideaistomeasurethedeviationfromthemedianofthepreviouspoints
andthemedianoftheirsuccessivedifferences.Moreover,SmartSifter[256]aimstobuildahistogramforcategorical
valuesandafinitemixturemodelforcontinuousdata.Theproposedmethodaimstoupdatethosehistograms/density
asnewpointsarriveinanunsupervisedmannerandthencomputeascorethatestimateshowthenewpointupdated
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 23
Fig.13. IllustrationoftheFiniteStateMachine(FSM).
haschangedthehistogram/density.Then,OC-KFD[208]utilizeslinearquantilemodels.Themodelisselectedviacross-
validatedlikelihood,fromwhichalinearquantilemodelisfitted,andoutliersaredetectedbyconsideringconfidence
intervals.Moreover,MGDD[233]utilizeskerneldensityestimationonslidingwindowsoftheoriginaltimeseries.The
estimateddistributionisthenusedtoidentifytheanomalies.Then,COPOD[133]isacopula-basedanomalydetection
methodandanidealchoiceformultivariatedata.Finally,unlikethepreviousmodels,ConInd[7]isanalgorithmbased
ondomainknowledge.Themodelcandetectonlytheknownanomalies,wheremultiplestatisticalanomalyindicators
(conditionindicators)areproposedbasedondifferentdistributionassumptions.
7.2 Graph-basedMethods
Then,graph-basedmethodsareanothercategoryofdensity-basedapproaches.Graph-basedmethodsrepresentthe
timeseriesandthecorrespondingsub-sequencesasagraph.Thenodesandedgesrepresentthedifferenttypesof
sub-sequences(orrepresentativefeatures)andtheirevolutionintime.Inthissection,wedescribethemostimportant
approachesinthiscategory.
7.2.1 FiniteStateMachine. Finally,FiniteStateMachine(FSM)isageneralcategorizationofmachinelearningalgorithms
thatcanbeonlyinexactlyoneofafinitenumberofstatesatanygiventime.Inreactiontoanyinputs,theFSMwill
shiftfromonestatetoanother;suchchangesbetweenstatesarecalledatransition.Inanomalydetection,inputtime
serieswill,uponcertainmachine-learnedrules,changethestateofthealgorithms.Ifthestateturnsintoananomaly,
theinputisidentifiedasanomalous.
Figure13givesanillustrationofsuchaprocess.Inmanyways,FSMissimilartoadynamicBayesiannetwork,which
alsousesDirectedAcyclicGraph(DAG).However,thetransitionrulebetweenFSMstatesisusuallyparametric,and
thustheentireprocessismachinelearningbased.However,FiniteStateMachineisageneralcategorizationwhere
particularmethodsmightbevastlydifferent,eachofwhichisuniquetoitsownspecificrulesofthelearningalgorithm.
TwoFingers[156],forexample,buildsadatabaseofnormalbehaviorbyconstructingasuffixtreeforvariable-length
N-gramsfromthetrainingdata.Thetreesaretransformedwithinthefinitestatemachineandarefurthercompacted
toaDAG.Finally,theFiniteStateMachine,endowedwiththearchitectureofDAG,matchesthenewseriestodetect
anomalies.GeckFSM[214],however,isvastlydifferentfromTwoFingers,despitealsofollowingafinite-statemachine
structure.Theproposedapproach,GeckoFSM,aimstoclusterthepoints(basedontheirslope)intheunivariatetime
seriesandthenextractsomenon-overlappingsub-sequences.Aslope-basedclustermergingoperationthenfindsan
optimalnumberofclusters,wheretransitionhuman-readablerulesofFSMforeachclusterarefurthercomputedusing
theRIPPERalgorithm[55].Anomaliesareidentifiedaspointsthatderivesignificantlyfromtheserules.
7.2.2 GraphRepresentationofSub-sequences. Asecondapproachistoconvertthetimeseriesintoadirectedgraphwith
nodesrepresentingtheusualtypesofsubsequencesandedgesrepresentingthefrequencyofthetransitionsbetween
ManuscriptsubmittedtoACM

24 Paparrizosetal.
Time series
0 1300 2600 3900 5200 6500
Pattern
following a
Pattern recurrent path
following an in the graph
unusual path
in the graph
(possible
anomaly)
Series2Graph representation of the Time series
Fig.14. ExampleofSeries2graphrepresentation.
typesofsubsequences.Series2Graph[26]isbuildingsuchkindsofgraphs.Moreover,anextensionofSeries2Graph
proposedintheliterature,namedDADS[217],proposesadistributedimplementationand,therefore,amuchmore
scalablemethodforlargetimeseries.
Foragivendataseries𝑇,theoverallprocessofSeries2Graphisdividedintothefollowingfourmainsteps.
(1) SubsequenceEmbedding:Projectallthesubsequences(ofagivenlengthℓ)of𝑇 inatwo-dimensionalspace,
whereshapesimilarityispreserved.
(2) NodeCreation:Createanodeforeachoneofthedensestpartsoftheabovetwo-dimensionalspace.These
nodescanbeseenasasummarizationofallthemajorpatternsoflengthℓthatoccurredin𝑇.
(3) EdgeCreation:Retrievealltransitionsbetweenpairsofsubsequencesrepresentedbytwodifferentnodes:each
transitioncorrespondstoapairofsubsequences,whereoneoccursimmediatelyaftertheotherintheinputdata
series𝑇.Werepresenttransitionswithanedgebetweenthecorrespondingnodes.Theweightsoftheedgesare
settothenumberoftimesthecorrespondingpairofsubsequenceswasobservedin𝑇.
(4) SubsequenceScoring:Computethenormality(oranomaly)scoreofasubsequenceoflengthℓ 𝑞 ≥ℓ(withinor
outsideof𝑇),basedonthepreviouslycomputededges/nodesandtheirweights/degrees.
Figure14depictstheresultinggraphreturnedbySeries2Graph.Theunusualpathinthegraph(withedgeswithlow
weightsandnodeswithlowdegrees)correspondstoanomaliesinthetimeseries.
7.3 Tree-basedMethods
Insteadofmodelingthetimeseriesintoagraph,thedifferentpointsorsub-sequencescanalsobeorganizedintreesto
highlightpotentialisolatedinstancesthatcouldcorrespondtoanomalies.IsolationForest(IForest)isdensity-basedand
themostfamoustree-basedapproachforanomalydetection.IForesttriestoisolatetheoutlierfromtherest[140].The
keyidearemainsonthefactthat,inanormaldistribution,anomaliesaremorelikelytobeisolated(i.e.,requiringfewer
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 25
ITree ITree ITree ITree
1 2 3 n
Instance A Instance A Instance A
...
Instance A
Instance N
Instance N Instance N
Instance N
Fig.15. Setofisolationtreesthatrandomlypartitionadataset.Onaverage,instanceNhasalongerpathtotherootthaninstanceA.
Thus,instanceA’sanomalyscorewillbehigher.
randompartitionstobeisolated)thannormalinstances.Ifweassumethelatterstatement,weonlyhavetoproducea
partitioningprocessthatindicateswelltheisolationdegree(i.e.,anomalousdegree)ofinstances.
LetfirstdefinetheconceptofIsolationTreeasstatedin[140].Letbe𝑇𝑟 abinarytreewhereeachnodehaszeroor
twochildrenandatestthatconsistsofanattribute𝑞andasplit𝑝 suchthat𝑝 <𝑞dividesdatapointsintothetwo
children.𝑇𝑟 isbuiltbydividingrecursivelythetrainingdataset𝑇 ={𝑇
𝑖,ℓ
,𝑇
𝑖+1,ℓ
,...,𝑇 |𝑇|−ℓ,ℓ}randomlyselecting𝑝and𝑞
until,themaximaldepthofthetreeisreached,orthenumberofdifferentinstancesisequalto1.Figure15depictsan
exampleofisolationtrees.
Usingthatkindofdatastructure,thepathlengthintothetree𝑇𝑟 toreachaninstance𝑇 𝑖,ℓ isdirectlycorrelatedto
theanomalydegreeofthatinstance.Therefore,wecandefinetheanomalyscoreasfollow:
𝑆(𝑥,𝑛)=2 𝑠𝑠 =
(cid:205)
𝑇𝑟∈T
ℎ(𝑥,𝑇𝑟)
,𝑐(𝑛)=𝐻(𝑛−1)−
2(𝑛−1)
(7)
|T|𝑐(𝑛) 𝑛
Withℎ(𝑥,𝑇𝑟)thelengthofthepathtoreach𝑥 inthetree𝑇𝑟,T asetofdifferentisolationtreesbuilt,𝑛thenumber
ofinstancesinthetrainingset,andHistheharmonicnumber.ItcanbesimplybutsurelyestimatedusingtheEuler
constant.
OtherIForest-basedalgorithmshavealsobeenproposedrecently.ExtendedIForest[90]isanextensionofthe
traditionalIsolationForestalgorithm,whichremovesthebranchingbiasusinghyperplaneswithrandomslopes.The
randomslopinghyperplanesenableanunbiasedselectionoffeaturesfreeofthebranchingstructurewithinthedataset.
HybridIForest[157]isanotherimprovementonIForest,enablingasupervisedsettingandeliminatingthedataset’s
potentialconfoundingduetounbalancedclusters.Finally,IF-LOF[53]combinesIForestandLOFbyapplyingIForest
andthenutilizesLOFtorefinetheresults,whichspeedsuptheprocess.
7.4 Encoding-basedMethods
Encoding-basedmethodsrepresentthesub-sequencesofatimeseriesintoalow-dimensionallatentspaceordata
structure.Theanomalyscoreisdirectlyfromthelatentspacerepresentations.Morespecifically,theanomalyscoresare
attributedtothepointsthatcorrespondtotheencodedsub-sequencesinthelatentspace.
7.4.1 PrincipalComponentAnalysis. Thefirstencoding-basedapproachistoencodeandrepresentthetimeserieswith
itsprincipalcomponents.PrincipalComponentsAnalysis(PCA)investigatesthemajorcomponentsofthetimeseries
thatcontributethemosttothecovariancestructure.Theanomalyscoreismeasuredbythesub-sequencesdistancefrom
0alongtheprincipalcomponentsweightedbytheireigenvalues.Astandardroutineistopick𝑞significantcomponents
ManuscriptsubmittedtoACM

26 Paparrizosetal.
thatcanexplain50%variationsofthetimeseriesand𝑟 minorcomponentsthatexplainlessthan20%variations.A
pointisananomalyifitsvaluesofmajorprinciplescomponents,𝑦
1
,𝑦
2
...,haveaweightedsumexceedingthethreshold
itsminoronehas.So𝑥 (orasub-sequence𝑇 𝑖,ℓ ofagiventimeseries)isananomalyif:
𝑞 𝑝
∑︁𝑦 𝑖 ∑︁ 𝑦 𝑖
𝜆 >𝑐 1or, 𝜆 >𝑐 2 (8)
𝑖 𝑖
1 𝑝−𝑟+1
Intheequationabove,𝑐 1and𝑐 2arepredefinedthresholdvalues,and𝜆saretheeigenvalues.RobustPCA[174]aims
torecovertheprincipalmatrix𝐿 0bydecomposingtheoriginalcovariancematrixinto𝑀 =𝐿 0 +𝑆 0tominimizetherank
of𝐿 0.Theresidualterm𝑆 0helpsseparatetheanomaloussubsetsandmakesthealgorithmapplicabletotimeseries
containingmanyanomalies.Finally,deepPCA[44]issimilartorobustPCAbutwithanautoencoderpreprocessingstep
first.Theautoencodermapsthetimeseriesintoalatentspace,andthenthePCA(describedabove)isusedtoidentify
anomalies.
7.4.2 GrammarandItemsetRepresentations. Anotherapproachistorepresentthetimeseriesintoasetofsymbols
associatedwithrules.GrammarViz[219]adoptsanapproachtofindanomaliesbasedontheconceptofKolmogorov
complexitywheretherandomnessinasequenceisafunctionofitsalgorithmicincompressibility.Themainideaisthat
itispossibletorepresentatimeseriesascontext-freegrammar(asetofsymbolsassociatedwithrules),andthesections
ofthetimeseriesthatmatchafewgrammarrulesareconsideredanomalies.Inaddition,Afeatureofthisalgorithmis
alsocenteredonitsabilitytofindanomaliesofdifferentlengths.
Moreprecisely,thealgorithmcanbedividedintodifferentphases.First,thewholetimeseriesissummarizedusing
SymbolicAggregateApproximation(SAX)tohavediscretevaluesandnotcontinuousones.Next,context-freegrammar
isbuiltusingSequitur,alinearspaceandtimealgorithmabletoderivecontext-freegrammarfromastringincrementally.
Finally,aruledensitycurveisbuilt,whichisthemetadatathatallowsthedetectionofanomalies.Itispossibletoobtain
aruledensitycurvebyiteratingoverallgrammarrulesandincrementingacounterforeachtimeseriesthatpointsto
therulespans.Oncetheruledensitycurveisobtained,itispossibletodiscoveranomaliesbypickingtheminimum
valuesofthecurve.Otherwise,itispossibletodiscovertheleastfrequentsub-sequences(andpossibleanomalies)by
applyingtheRareRuleAnomaly(RRA)algorithm.
Othergrammar-basedmethodshavebeenproposedintheliterature.First,EnsembleGI[71]isanextensionof
theGrammarVizalgorithm,whichfurtherimplementsgrammarinductiononanensembleapproachthatobtains
theanomalydetectionresultbasedontheensembledetectionofmodelswithdifferentparametervalues.Unlikethe
previoustwo,SupriseEncode[42]adoptsadistinctcompression-basedmethodrepresentingtherecordasanitemset.
Thecompressionratioofsegments(code-lengthencoding)derivedfromeachsub-sequenceiscomparedamongthe
trainingdatasettoderivetheanomalyscore.
7.4.3 HiddenMarkovModel. AnothertypeofEncoder-basedmethodisHiddenMarkovModel(HMM).Thelatter
assumestheexistenceofaMarkovprocess𝑋 suchthatthetimeseriesdataobservedisdependentonthat𝑋.Thegoal
istoderive𝑋 byobservingthedata.Theanomaliesaredetectedbymeasuringtheabilityoftheencodingtorepresent
thetimeseries.Forinstance,EM-HMM[193]isatime-seriesanomalydetectionmethodbasedonHMM.
Moreprecisely,PST[234]isanotherdetectionmethodbasedonHMM.Itproposesanefficientalgorithmforcomputing
theProbabilisticSuffixTree(PST),acompactvariable-orderMarkovchain.Inpractice,thealgorithmembedspossible
chainsofvalues(andtheirprobability)intothetreesandinferstheanomalyscorebycomputingtheprobabilitiesofthe
chainsofvalues.
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 27
7.4.4 BayesianNetworks. BayesianNetworkbuildsagraphdenotingtherelationshipbetweenrandomvariablesin
termsofDirectedAcyclicGraph(DAG).EachnodeintheDAGstandsforarandomvariable,andtheedgesrepresentthe
probabilisticrelationshipsamongthevariables.DynamicBayesianNetwork,ortemporalBayesianNetwork,generalizes
theBayesianNetworkgraphmodeltothetimeseriessetting.Themodeliscapableofmodelingthetemporalrelationship
fordifferentrandomvariableswithfirst-orderassumption.
Fig.16. IllustrationofDynamicBayesianNetwork(DBN).
AsdisplayedinFigure16,therandomvariablesatdifferenttimestampsareconnectedbyprobabilisticedges,which
arereferencedbythemodeltocharacterizethetemporalchangeoftherandomvariablesinthedataset.Thejoint
probabilitydistributionofagivenDBNvariable𝑋 𝑖 isgivenbythefollowingequation:
(cid:214)
𝑃(𝑋 𝑖:𝑡,1 ,𝑋 𝑖:𝑡,2 ,𝑋 𝑖:𝑡,𝑅−1 ...𝑋 𝑖:𝑡,𝑅)= 𝑃(𝑋 𝑖:𝑡,𝑟|𝑃𝑎𝑟(𝑋 𝑖:𝑡,𝑟)) (9)
𝑡≤𝑇,𝑟≤𝑅
𝑃𝑎𝑟(𝑋 𝑖:𝑡,𝑟)denotestheparentof𝑋 𝑖:𝑡,𝑟,whichareeitherinsidetheprevioustimestampsorjusttheparentinsidethe
sametimestamps,duetothefirstorderassumption.
Varioustime-seriesanomalydetectionmethodshaveimplementedDBNintheiralgorithms.LaserDBN[173]is
amethodproposedforimagetimeseries.Thedataisfirstpreprocessedbyk-meansclusteringtoperformfeature
selection,andthenDynamicBayesianNetworkisimplementedtocomputetheprobabilitiesofindividualsub-sequences.
EDBN[195]proposesanextensionofDBNtosuittheparticularcaseoftextualtime-seriesanomalydetection(specifically
forbusinessprocessesandlogs).Finally,KDE-EDBN[196]isanextensionofEDBNthatusesKernelDensityEstimation
(KDE)tohandlenumericalattributesinlogs.
7.4.5 OtherEncoding-basedMethods. Inadditiontoallthemethodsdescribedabove,severalmoreanomalydetection
methodscouldbegroupedintheencoding-basedcategory,suchaspolynomialapproximationmethodstodetect
anomalies,likePOLY[132]orSSA[260].Thelatteristrainingmultiplepolynomialapproximationmodelsforeachtime
series(orsub-sequenceinthetimeseries).Asimilaritymeasurebetweenthetrainedmodelsisusedtodetectanomalies.
8 Prediction-basedMethods
Prediction-basedmethodsaimtodetectanomaliesbypredictingtheexpectednormalbehaviorsbasedonatrainingsetof
timeseriesorsub-sequences(containinganomaliesornot).Forinstance,somemethodswillbetrainedtopredictthenext
valueorsub-sequencebasedonthepreviousone.Then,thepredictionerrorisusedasananomalyscore.Theunderlying
assumptionofprediction-basedmethodsisthatnormaldataareeasiertopredict,whileanomaliesareunexpected,
leadingtohigherpredictionerror.Suchassumptionsarevalidwhenthetrainingsetcontainsnoorfewtimeserieswith
anomalies.Therefore,prediction-basedmethodsareusuallymoreoptimalundersemi-supervisedsettings.Withinthe
ManuscriptsubmittedtoACM

28 Paparrizosetal.
prediction-basedmethods,therecometwosecond-levelcategories:forecasting-basedandreconstruction-based.We
enumerateallthementionedmethodsinTable3.
Table3. Summaryoftheprediction-basedanomalydetectionmethods.
|            |     | SecondLevel       |     | Prototype | Dim | Method Stream |     |
| ---------- | --- | ----------------- | --- | --------- | --- | ------------- | --- |
| ES[226]    |     | Forecasting-based |     | -         | I   | Se ✗          |     |
| DES[226]   |     | Forecasting-based |     | -         | I   | Se ✗          |     |
| TES[226]   |     | Forecasting-based |     | -         | I   | U ✗           |     |
| ARIMA[211] |     | Forecasting-based |     | ARIMA     | I   | U ✓           |     |
✓
| NoveltySVR[149] |     | Forecasting-based |     | SVM   | I   | U    |     |
| --------------- | --- | ----------------- | --- | ----- | --- | ---- | --- |
| PCI[263]        |     | Forecasting-based |     | ARIMA | I   | U ✓  |     |
| OceanWNN[246]   |     | Forecasting-based |     | -     | I   | Se ✗ |     |
| MTAD-GAT[267]   |     | Forecasting-based |     | GRU   | M   | Se ✓ |     |
| AD-LTI[252]     |     | Forecasting-based |     | GRU   | M   | Se ✓ |     |
✓
| CoalESN[172]  |     | Forecasting-based |     | ESN  | M   | Se   |     |
| ------------- | --- | ----------------- | --- | ---- | --- | ---- | --- |
| MoteESN[49]   |     | Forecasting-based |     | ESN  | I   | Se ✓ |     |
| HealthESN[51] |     | Forecasting-based |     | ESN  | I   | Se ✗ |     |
| Torsk[96]     |     | Forecasting-based |     | ESN  | M   | U ✓  |     |
| LSTM-AD[153]  |     | Forecasting-based |     | LSTM | M   | Se ✗ |     |
✗
| DeepLSTM[50]    |     | Forecasting-based |     | LSTM | I   | Se   |     |
| --------------- | --- | ----------------- | --- | ---- | --- | ---- | --- |
| DeepAnT[167]    |     | Forecasting-based |     | LSTM | M   | Se ✗ |     |
| Telemanom★[103] |     |                   |     |      |     | ✗    |     |
|                 |     | Forecasting-based |     | LSTM | M   | Se   |     |
| RePAD[127]      |     | Forecasting-based |     | LSTM | M   | U ✗  |     |
| NumentaHTM[3]   |     | Forecasting-based |     | HTM  | I   | U ✓  |     |
✓
| MultiHTM[249] |     | Forecasting-based    |     | HTM | M   | U    |     |
| ------------- | --- | -------------------- | --- | --- | --- | ---- | --- |
| RADM[59]      |     | Forecasting-based    |     | HTM | M   | Se ✓ |     |
| MAD-GAN[129]  |     | Reconstruction-based |     | GAN | M   | Se ✓ |     |
| VAE-GAN[171]  |     | Reconstruction-based |     | GAN | M   | Se ✗ |     |
| TAnoGAN[17]   |     | Reconstruction-based |     | GAN | M   | Se ✗ |     |
✗
| USAD[8]        |     | Reconstruction-based |     | GAN | M   | Se   |     |
| -------------- | --- | -------------------- | --- | --- | --- | ---- | --- |
| EncDec-AD[152] |     | Reconstruction-based |     | AE  | M   | Se ✗ |     |
✓
| LSTM-VAE[194] |     | Reconstruction-based |     | AE  | M   | Se   |     |
| ------------- | --- | -------------------- | --- | --- | --- | ---- | --- |
| DONUT[254]    |     | Reconstruction-based |     | AE  | I   | Se ✗ |     |
| BAGEL[130]    |     | Reconstruction-based |     | AE  | I   | Se ✗ |     |
✗
| OmniAnomaly[231] |     | Reconstruction-based |     | AE  | M   | Se  |     |
| ---------------- | --- | -------------------- | --- | --- | --- | --- | --- |
| MSCRED[265]      |     | Reconstruction-based |     | AE  | I   | U ✗ |     |
✗
| VELC[264]    |     | Reconstruction-based |     | AE  | I   | Se   |     |
| ------------ | --- | -------------------- | --- | --- | --- | ---- | --- |
| CAE[72,73]   |     | Reconstruction-based |     | AE  | I   | Se ✗ |     |
| DeepNAP[117] |     | Reconstruction-based |     | AE  | M   | Se ✓ |     |
✓
| STORN[227] |     | Reconstruction-based |     | AE  | M   | Se  |     |
| ---------- | --- | -------------------- | --- | --- | --- | --- | --- |
I:Univariate;M:Multivariate//S:Supervised;Se:Semi-SupervisedU:Unsupervised
8.1 Forecasting-basedMethods
Forecasting-basedmethodsuseamodeltrainedtoforecastseveraltimestepsbasedonpreviouspointsorsequences.
Theforecastingresultsarethusdirectlyconnectedtopreviousobservationsinthetimeseries.Theforecastedpointsor
sequencesarethencomparedtotheoriginalonestodeterminehowanomalousorunusualtheseoriginalpointsare.
8.1.1 ExponentialSmoothing. Oneofthefirstforecasting-basedapproachesproposedintheliteratureistheExponential
Smoothing[226].Thelatterisanon-linearsmoothingtechniquetopredictthetimeseriespointsbytakingtheprevious
timeseriesdataandassigningexponentialweightstothesepreviousindividualobservations.Theanomaliesarethen
detectedbycomparingthepredictedandactualresults.Formally,thepredictionofthecurrentvalue𝑇ˆ isdefinedas
𝑖
follows:
𝑁−1
∑︁
|     | 𝑇ˆ =(1−𝛼) | 𝑁−1𝑇 | +   | 𝛼(1−𝛼) | 𝑗−1𝑇 | 𝛼 ∈ [0,1] | (10) |
| --- | --------- | ---- | --- | ------ | ---- | --------- | ---- |
|     | 𝑖         |      | 𝑖−𝑁 |        | 𝑖−𝑗  |           |      |
𝑗=1
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 29
Thus,theestimatedsub-sequenceisalinearcombinationofthepreviousdatapoints,withtheweightsvarying
exponentially.Theparameter𝛼 standsfortherateofexponentialdecrease.Thesmallerthe𝛼 is,themoretheweightis
assignedtothedistantdatapoints.
Inaddition,severalapproachesbasedonexponentialsmoothinghavebeenproposed.Forexample,DoubleExponential
Smoothing(DES)andTripleExponentialSmoothing(TES)[226]arevariantsoftheexponentialsmoothingtechniques
fornon-stationarytimeseries.InDES,afurtherparameter𝛽isutilizedtosmooththetrendthatatimeseriescanhave.
Forthespecialcaseoftimeseriescontainingseasonality,TESenablesanotherparameter𝛾 tocontrolit.
8.1.2 ARIMA. Anotherearlycategoryofforecasting-basedapproachesproposedintheliteratureisARIMAmod-
els[211].Thelatterassumesalinearcorrelationamongthetimeseriesdata.ThealgorithmfitstheARIMAmodelon
thetimeseriesanddrawsanomaliesbycomparingthepredictionoftheARIMAmodelandrealdata.Formally,An
ARIMA(𝑝′,𝑞)modelisbuiltuponthefollowingiterativeequations:
|       | 𝑝′  |          | 𝑞           |      |
| ----- | --- | -------- | ----------- | ---- |
|       | ∑︁  |          | ∑︁ 𝑝        |      |
| 𝑇 𝑖 = | 𝛼 𝑘 | 𝑇 𝑡−𝑘 +𝜖 | 𝑖 + 𝜃 𝜖 𝑖−𝑗 | (11) |
𝑗
|     | 𝑘=1 |     | 𝑗=1 |     |
| --- | --- | --- | --- | --- |
Overall,usingARIMAmodels,weassumethateverynexttimeseriesvaluescorrespondtoalinearcombinationof
thepreviousvaluesandresiduals.Notethattheresidualsmustbeestimatedinaniteratedmanner.Moreover,Prediction
ConfidenceInterval(PCI)[263]isanextensionoftheARIMAmodel,whichfurthercombinesthenearestneighbor
method.Thepredictionconfidenceintervalallowsdynamicthresholding.Thethresholdcanbeestimatedonthe
historicalnearestneighbors.
8.1.3 LongShort-TermMemory. LongShort-TermMemory(LSTM)[98]networkhasbeendemonstratedtobepar-
ticularlyefficientinlearninginnerfeaturesforsub-sequencesclassificationortimeseriesforecasting.Suchamodel
canalsobeusedforanomalydetectionpurposes[67,154].Thetwolatterpapers’principleisasfollows:Astacked
LSTMmodelistrainedonnormalpartsofthedatathatwecall𝑁.Theobjectiveistopredictthepoint𝑁 𝑖 ∈𝑁 orthe
sub-sequence𝑁 usingthesub-sequence𝑁
𝑖,𝑙 𝑖−𝑙,𝑙.Consequently,themodelwillbetrainedtoforecastahealthystateof
1
thetimeseries,and,therefore,willfailtoforecastwhenitwillencounterananomaly.
LSTMnetworkisaspecialtypeofRecurrentNeuralNetwork(RNN),basedonLSTMunitsasmemorycellstoencode
hiddeninformation.Figure17depictsthecomponentsandinteractionswithinanLSTMcell.Thevariouscomponents
aregivenby:
| 𝑓 =𝜎 𝑔(𝑊    | 𝑥 +𝑈   | ℎ      | +𝑏 𝑓)        |     |
| ----------- | ------ | ------ | ------------ | --- |
| 𝑡           | 𝑓 𝑡    | 𝑓 𝑡−1  |              |     |
| 𝑖 =𝜎 𝑔(𝑊    | 𝑥 +𝑈   | ℎ +𝑏   |              |     |
| 𝑡           | 𝑖 𝑡    | 𝑖 𝑡−1  | 𝑖)           |     |
| 𝑜 𝑡 =𝜎 𝑔(𝑊  | 𝑥 𝑡 +𝑈 | ℎ 𝑡−1  | +𝑏 )         |     |
|             | 0      | 0      | 0            |     |
| 𝑐 =𝑓 ◦𝑐     | +𝑖     | ◦𝜎 𝑐(𝑊 | 𝑥 +𝑈 ℎ +𝑏 𝑐) |     |
| 𝑡 𝑡         | 𝑡−1    | 𝑡      | 𝑐 𝑡 𝑐 𝑡−1    |     |
| ℎ 𝑡 =𝑜 𝑡 ◦𝜎 | ℎ(𝑐 𝑡) |        |              |     |
Bycombiningalargenumberofcell(outlinedinFigure17)andstackingthem[154],onecanfittheweightsto
forecastthetimeseriesintwodifferentwaysdescribedasfollow:(i)Thefirstistotrainthenetworkusingafixedtime
windowlength𝑇 = [𝑇 ,...,𝑇 ]topredict𝑇 𝑡,(ii)orusingthesameinputtopredicttheincomingsequence
𝑡−ℓ−1,ℓ 𝑡−ℓ 𝑡−1
𝑇 𝑡,ℓ′ = [𝑇 𝑡 ,...,𝑇 𝑡+ℓ′].Forthespecificpurposeofanomalydetection,wewillassumethatsuchamodelcanbetrained
ManuscriptsubmittedtoACM

30 Paparrizosetal.
ℎ'
|     |     | *'() | x + |     | *'  |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- |
#$%ℎ
|     |     | ,'  | -' x | .'  |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- |
x
|     |     | !"   | !" #$%ℎ | !"  |     |     |     |
| --- | --- | ---- | ------- | --- | --- | --- | --- |
|     |     | ℎ'() |         |     | ℎ'  |     |     |
+'
|      |            | ℎ'()   |            | ℎ'   |            | ℎ'/) |      |
| ---- | ---------- | ------ | ---------- | ---- | ---------- | ---- | ---- |
| *'(0 | x          | +      | x +        |      | x +        |      | *'/) |
|      |            | x #$%ℎ |            | #$%ℎ |            | #$%ℎ |      |
|      |            |        | x          |      | x          |      |      |
|      |            | x      |            | x    |            | x    |      |
|      | !" !" #$%ℎ | !"     | !" !" #$%ℎ | !"   | !" !" #$%ℎ | !"   |      |
| ℎ'(0 |            |        |            |      |            |      | ℎ'/) |
|      | +'()       |        | +'         |      | +'/)       |      |      |
Fig.17. LSTMcellarchitecture.
toachievebothofthepreviouslyenumeratedtasks.Then,whathastobedoneistotrainthismodelonthenormal
sectionofthetimeseries(aprioriannotatedbytheknowledgeexpert)andusetheforecastingerrorasananomaly
score.Therefore,onecanexpecttoobtainabiggerforecastingerrorforasub-sequencethatthemodelhasneverseen
(likeananomaly),ratherthanausualsub-sequence.
ThereexistsalargevarietyofmethodsbasedonLSTMneuralnetworksproposedintheliterature.First,DeepLSTM[50]
isastandardimplementationofLSTMnetworks.ThegenerativemodelstackstheLSTMnetworktrainedfromnormal
sectionsofthetimeseries.Then,LSTM-AD[153]adoptsasimilarapproachtoDeepLSTM.Inadditiontotrainingthe
LSTMmodeltopredicttimeseries,LSTM-ADalsoestimatesthetrainingdataset’serrorswithmultivariatenormal
distributionandcalculatestheanomalyscorewiththeMahalanobisdistance.
Moreover,Telemanom[103]isanLSTM-basedapproachthatfocusesonchanneleddata(i.e.,multivariatetimeseries).
AnLSTMnetworkistrainedforeachchannel.Thepredictionerrorisfurthersmoothedovertime,andlowerrorsare
prunedretroactively.Then,RePad[127]isanotherLSTM-basedalgorithmthatconsidersshort-termhistoricaldata
pointstopredictfutureanomaliesinstreamingdata.ThedetectionisbasedontheAverageAbsoluteRelativeError
(AARE)ofLSTM,andRePadalsoimplementsadynamicthresholdadjustmenttovarythethresholdvalueatdifferent
timestamps.
8.1.4 GatedRecurrentUnit. InadditiontoLSTMcellsfrequentlyimplementedintimeseriessettings,otherneural
networkarchitectureshavealsobeeninuse.OneexampleistheGatedRecurrentUnit(GRU)whichisalsoanRNNbut
operatesinadifferentgatedunitthanLSTMtoforecasttimeseriesvalues.Wewillsummarizesomeoftheapproaches
usedinthesedifferentarchitectures.
MTAD-GAT[267]isthefirstexampleofanomalydetectionmethodsbasedonGRUunits.Thelatterusesboththe
predictionerrorandreconstructionerrorforthedetectionofanomalies(Thismethodcouldfitinbothforecasting
andreconstruction-basedcategories).Themodelutilizestwoparallelgraphattentionlayerstopreprocessthetime
seriesdatasetandthenimplementsaGRUnetworktoreconstructandpredictthenextvalues.AD-ITL[252]isanother
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 31
GRU-basedalgorithmwithseasonalandrawfeaturesasinput.Theinputtimeseriesisfirstusedtoextractseasonal
featuresandfurtherfedtotheGRUnetwork.TheGRUthenpredictseachvalueofthewindow,andLocalTrend
Inconsistency(LTI)isusedasameasureoftheerrortoassesstheabnormalitybetweenpredictedandactualvalues.
8.1.5 EchoStateNetworks. ResearchershavealsoproposedmultipleEchoStateNetworksfordetectinganomaliesin
timeseries.AnEchoStateNetwork(ESN)isavariantofRNN,whichhasasparselyconnectedrandomhiddenlayer.
Themodelrandomizestheweightsinhiddenandinputlayersandalsoconnectsneuronsrandomly.Onlythevaluesin
theoutputlayersarelearned,renderingthemethodalinearmodelthatiseasilytrained.Therandomhiddenlayersact
asadynamicreservoirthattransformstheinputintosequencesofnon-linear,complicatedprocesses.Thetrainable
outputlayerorganizestheencodingoftheinputsinthedynamicreservoir,enablingcomplexrepresentationofthedata
despiteitslinearity.Theinitialvaluesofinputandhiddenlayersarealsochosencarefully,usuallytunedwithmultiple
parameters.
First,CoalESN[172]isasimpleimplementationofEchoStatebypredictingtimeseriesvaluesandcomparingthe
estimatedresultswithrealonestodetermineabnormality.MoteESN[49]adoptsasimilarapproachtoCoalESNbutuses
theabsolutedifferencetomeasuretheanomalyscore.Themodelisoptimizedforasensordevice,wherethenetworkis
trainedofflinebeforedeploymentonthesensor.Torsk[96]isanotheradaptationofESN.Likeitsprecursors,Torskuses
thepreviouswindowastrainingdataandthenpredictsthefollowingones.Themodelfurtherimplementsautomatic
thresholding.Finally,HealthESN[51]isanEchoStateNetworkappliedtothemedicalandhealthdomain.Thealgorithm
utilizesthedefaultarchitecturewithtrainingandtestingsteps;afterasequenceofdatapreprocessing,intelligent
thresholdcomputationisusedtoestimatetheadaptivethresholdanddeclareanomaliesbytheESNpredictions.
8.1.6 HierarchicalTemporalMemory. AnotherrecurrentneuralnetworktypeofapproachisHierarchicalTemporal
Memory(HTM).Thelatteristhecorecomponentofmultipleanomalydetectionmethodsproposedintheliterature.
TheHTMmethodisbasedonthetheoryandideasproposedintheThousandBrainsTheoryofIntelligence[92].The
latterproposesthatmanymodelsarelearnedforeachobjectorconcept,ratherthanonlyonesinglemodelperobject,
asmostofthemethodsdescribedintheprevioussectionsusuallyhandle.
In particular, HTM focuses on three main tasks: sequence learning, continual learning, and sparse distributed
representations.EventhoughHTM-basedmethodscanbeseenasRNN-basedmethods(suchasLSTM,GRU,and
ESN-basedapproach),themaindifferenceisbetweentheneurondefinitionandthelearningprocess.ForHTM,the
unsupervisedHebbian-learningrule[95]isappliedtotrainthemodelratherthantheclassicalback-propagationisnot
applied.
Thefirsttime-seriesanomalydetectionmethodusingHTMproposedintheliteratureistheNumentaHTM[3]and
MultiHTM[249]approaches.Moreover,RADM[59]combinesHTMwithNaiveBayesianNetworkstodetectanomalies
inmultivariatetimeseries.
8.1.7 OtherForecasting-basedMethods. Finally,itisimportanttonotethatforecasting-basedapproachesareageneric
conceptthatrequirestohaveamodelthatcanpredicttheincomingvaluefromhistoricaldata.Therefore,anyregression
approachcanbeusedasaforecasting-basedapproach.Intheprevioussections,wedescribedonahigh-levelthemost
popularmethodsusedtoperformanomalydetectionusingforecasting-basedtechniques.Wecancomplementthelist
withmethodsusingmorespecificarchitectureonspecificapplicationssuchasOceanWNN[246]usingWavelet-Neural
Networks,ormoreclassicalregressiontechniquesusedasforecasting-basedcoreunitssuchasNoveltySVR[149]using
Support-Vector-Machine(SVM).
ManuscriptsubmittedtoACM

𝐸𝑥𝑖𝑠𝑡𝑖𝑛𝑔𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
𝑇(/)𝑇(/89) 𝑇(;)
-,ℓ -,ℓ -,ℓ
…
ℓ 𝐸𝑥𝑖𝑠𝑡𝑖𝑛𝑔
𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
𝐷(𝑇 ,𝜃 )
-ℓ /
𝐿𝑎𝑡𝑒𝑛𝑡𝑠𝑝𝑎𝑐𝑒𝑍 𝐺𝑒𝑛𝑒𝑟𝑎𝑡𝑒𝑑
𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
…
𝐺(𝑍,𝜃 )
4
ℓ
𝑇- 6 ,ℓ (/)𝑇 - 6 ,ℓ (/89)𝑇- 6 ,ℓ (;)
𝐺𝑒𝑛𝑒𝑟𝑎𝑡𝑒𝑑𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
32 Paparrizosetal.
𝐴𝑛𝑜𝑚𝑎𝑙𝑦𝑠𝑐𝑜𝑟𝑒
𝑂𝑟𝑖𝑔𝑖𝑛𝑎𝑙𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒 𝑆= ℒ(𝑇 -,@ ,𝑇′ -,@) 𝑅𝑒𝑐𝑜𝑛𝑠𝑡𝑟𝑢𝑐𝑡𝑒𝑑𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
𝑇 - ( ,ℓ /)𝑇 - ( ,ℓ /89) 𝑇 - ( ,ℓ ;) 𝑇- 6 ,ℓ (/)𝑇 - 6 ,ℓ (/89)𝑇- 6 ,ℓ (;)
𝐿𝑎𝑡𝑒𝑛𝑡𝑠𝑝𝑎𝑐𝑒
… …
E(𝑇,𝜃/) D(𝑍,𝜃/)
ℓ ℓ
𝑂𝑟𝑖𝑔𝑖𝑛𝑎𝑙𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
𝑅𝑒𝑐𝑜𝑛𝑠𝑡𝑟𝑢𝑐𝑡𝑒𝑑
𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
0 20 40 60 0 20 40 60
𝑁𝑜𝑟𝑚𝑎𝑙𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒 𝐴𝑛𝑜𝑚𝑎𝑙𝑜𝑢𝑠𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
Fig.18. Overviewofautoencodersmethodsfortime-seriesanomalydetection.
8.2 Reconstruction-basedMethods
Reconstruction-basedmethodsrepresentnormalbehaviorbyencodingsub-sequencesofanormaltrainingtimeseries
intoalow-dimensionalspace.Thesub-sequencesarethenreconstructedfromthelow-dimensionalspace,andthe
reconstructedsub-sequencesarethencomparedtotheoriginalsub-sequences.Thedifferencebetweenthereconstruction
andtheoriginalsequenceisusedtodetectanomalies.Ingeneral,theinputstothereconstructionprocessaretraining
sub-sequences.
8.2.1 Autoencoder. Autoencoderisatypeofartificialneuralnetworkusedtolearntoreconstructthedatasetgivenas
inputusingasmallerencodingsizetoavoididentityreconstruction.Asageneralidea,theautoencoderwilltrytolearn
thebestlatentrepresentation(alsocalledencoding)usingareconstructionloss.Therefore,itwilllearntocompressthe
datasetintoashortercodeandthenuncompressitintoadatasetthatcloselymatchestheoriginal.Figure18depictsan
overviewofautoencodersfortimeseries.Formally,giventwotransitionfunctions𝐸and𝐷,respectivelycalledencoder
anddecoder,thetaskofanautoencoderisthefollowingone:
𝜙 :T ℓ →Z (12)
𝜓 :Z→T ℓ (13)
𝜙,𝜓 =𝑎𝑟𝑔minL(𝑇 𝑖,ℓ ,𝜓(𝜙(𝑇 𝑖,ℓ))) (14)
𝜙,𝜓
Lisalossfunctionthatisusuallysettothemeansquareerroroftheinputanditsreconstruction,formallywritten
||𝑋 −𝜓(𝜙(𝑇 𝑖,ℓ))||2.Thislossfitsthetaskwellforthespecificcaseofsub-sequencesinatimeseriessinceitcoincides
withtheEuclidiandistance.
Thereconstructionerrorcanbeusedasananomalousscoreforthespecificanomalydetectiontask.Asthemodelis
trainedonthenon-anomaloussub-sequenceofthetimeseries,itisoptimizedtoreconstructthenormalsub-sequences.
Therefore,allthesub-sequencesfarfromthetrainingsetwillhaveabiggerreconstructionerror.
Asautoencoderhasbeenapopularmethodintherecentdecade,manyanomalydetectionalgorithmsarebasedon
autoencoderalgorithms’implementation.EncDec-AD[152]isthefirstmodelthatimplementsanencoder-decoder
byusingreconstructionerrortoscoreanomalies.LSTM-VAE[194]andMSCRED[265]useLSTMandConvolutional
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 33
𝐸𝑥𝑖𝑠𝑡𝑖𝑛𝑔𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
𝑇(/)𝑇(/89) 𝑇(;)
-,ℓ -,ℓ -,ℓ
…
ℓ 𝐸𝑥𝑖𝑠𝑡𝑖𝑛𝑔
𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
𝐷(𝑇 ,𝜃 )
-ℓ /
𝐿𝑎𝑡𝑒𝑛𝑡𝑠𝑝𝑎𝑐𝑒𝑍 𝐺𝑒𝑛𝑒𝑟𝑎𝑡𝑒𝑑
𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
…
𝐺(𝑍,𝜃 )
4
ℓ
𝑇- 6 ,ℓ (/)𝑇 - 6 ,ℓ (/89)𝑇- 6 ,ℓ (;)
𝐺𝑒𝑛𝑒𝑟𝑎𝑡𝑒𝑑𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
Fig.19. OverviewofGANmethodsfortime-seriesanomalydetection.
𝐴𝑛𝑜𝑚𝑎𝑙𝑦𝑠𝑐𝑜𝑟𝑒
𝑂𝑟𝑖𝑔𝑖𝑛𝑎𝑙𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒 𝑆= ℒ(𝑇 -,@ ,𝑇′ -,@) 𝑅𝑒𝑐𝑜𝑛𝑠𝑡𝑟𝑢𝑐𝑡𝑒𝑑𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
LSTMcellsintheautoencoder𝑇a
-
(
,ℓ
/rc)h𝑇
-
(i
,ℓ
/t8e9c)tu𝑇r
-
(
,
e
ℓ
;).Similarly,Omnianomaly[231]isanotherautoe𝑇n
-
6
,
c
ℓ
(o/d)𝑇e
-
6
,
r
ℓ
(/m89e)t𝑇h- 6 ,ℓo(;d)wherethe
autoencoderarchitectureusesGRUandplanarnormalizingfl𝐿𝑎o𝑡w𝑒𝑛.𝑡𝑠𝑝𝑎𝑐𝑒
Then, STORN [227] and DONUT [254] proposed a Varational Autoencoder (VAE) method to detect abnormal
… …
sub-sequences.ForDONUT,itfurtherpreproc E e ( s 𝑇 s , e 𝜃 s/t ) hetimeseriesusi D n ( g 𝑍, t 𝜃 h/e ) MCMC-basedmissingdataimputation
ℓ ℓ
technique[205].ImprovingfromDONUT,BAGEL[130]implementsconditionalVAEinsteadofVAE.VELC[264]sets
upadditionalconstraintstotheVAE.TheDecoderphaseisregularizedduetoanomaliesintrainingdata,whichhelps
𝑂𝑟𝑖𝑔𝑖𝑛𝑎𝑙𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
𝑟𝑒𝑐𝑜𝑛𝑠𝑡𝑟𝑢𝑐𝑡𝑒𝑑
fitnormaldataandpreventgeneralizationtomodelabnormalities.
𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
Moreover,CAE[72,73]usesaconvolutionalautoencodertoconverttimeseriessub-sequencestoimageencoding.
Thealgorithmalsospeedsupneste
0
d-loo
20
p-sea
4
r
0
chus60ingsub-sequ
0
ence
2
s
0
appr
4
o
0
xima
60
tionwithSAXwordembedding.
𝑁𝑜𝑟𝑚𝑎𝑙𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒 𝐴𝑛𝑜𝑚𝑎𝑙𝑜𝑢𝑠𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
Finally, DeepNAP [117] is a sequence-to-sequence AE-based model. However, unlike other AE-based models,
DeepNAPdetectsanomaliesbeforetheyoccur.
8.2.2 GenerativeAdversarialNetworks. GenerativeAdversarialNetwork(GAN)isinitiallyproposedforimagegener-
ationpurposes[82]butcanalsobeusedtogeneratetimeseries.GANhastwocomponents:(i)onetogeneratenew
timeseriesand(ii)onetodiscriminatetheexistingtimeseries.Bothofthecomponentsareusefulforthedetectionof
anomalies.Figure19depictstheoverviewofGANmethodsforanomalytimeseries.
Moreprecisely,aGANiscomposedoftwonetworks.Thefirstiscalledthegenerator𝐺(𝑧,𝜃 𝑔)with𝜃 𝑔itsparameters.
Thesecondoneiscalledthediscriminant𝐺(𝑥,𝜃 𝑑)with𝜃 𝑑itsparameters.Theoutputof𝐺isthesameshapeastheinput,
andtheoutputof𝐷isascalar𝐷(𝑥)thatrepresentstheprobabilitythat𝑥 camefromtheoriginaldataset.Therefore
1−𝐷(𝑥)istheprobabilitythat𝐺 hasgenerated𝑥.Formally,𝐺 and𝐷 havetobeoptimized,suchasthetwo-player
optimizationproblemwheretheaccuracyofthediscriminatorhastobemaximizedbutalsominimizedregardingthe
generator.Thevaluetobeminimized,denotedas𝑉(𝐺,𝐷),isdefinedinthefollowingmanner.
m
𝐺
inm
𝐷
ax𝑉(𝐺,𝐷)=E 𝑥∼𝑝𝑑𝑎𝑡𝑎(𝑥) [𝑙𝑜𝑔𝐷(𝑥)]+E 𝑧∼𝑝𝑧(𝑧) [𝑙𝑜𝑔(1−𝐷(𝐺(𝑧)))] (15)
ManuscriptsubmittedtoACM

34 Paparrizosetal.
ForT
ℓ
thesetofsub-sequencestotrainon,andZthecorrespondingsetofsub-sequencesfromthelatentspace
(noisesample),wehavethefollowingstochasticgradientdescend:
1 ∑︁
𝐷𝑖𝑠𝑐𝑟𝑖𝑚𝑖𝑛𝑎𝑛𝑡 :∇𝜃𝑑
|T|
[−𝑙𝑜𝑔𝐷(𝑇)−𝑙𝑜𝑔(1−𝐷(𝐺(𝑍)))] (16)
(𝑇,𝑍)∈(T,Z)
1 ∑︁
𝐺𝑒𝑛𝑒𝑟𝑎𝑡𝑜𝑟 :∇𝜃𝑔|Z| [1−𝑙𝑜𝑔(1−𝐷(𝐺(𝑍)))] (17)
𝑍∈Z
Thisarchitecturehasbeentriedforthespecificcaseoftime-seriesanomalydetection[128].Forthepurposeof
anomalydetection,thegeneratoristrainedtoproducesub-sequenceslabeledasnormal,andthediscriminatoris
trainedtodiscriminatetheanomalies.Thustrainingsuchamodelrequireshavingatrainingdatasetwithnormal
sub-sequences.Onecanusethediscriminatorandthegeneratorsimultaneouslytodetecttheanomaly.First,giventhat
thediscriminatorhasbeentrainedtoseparatereal(i.e.,normal)fromfake(i.e.,anomaly)sub-sequences,itcanbeused
asadirecttoolforanomalydetection.Nevertheless,thegeneratorcanalsobehelpful.Giventhatthegeneratorhas
beentrainedtoproducearealisticsub-sequence,itwillmostprobablyfailtoproducearealisticanomaly.Therefore,the
Euclidiandistancebetweenthesub-sequencetoevaluateandwhatwouldhavegeneratedthegeneratorwiththesame
latentinputcanhavesomesignificanceindiscriminatinganomaly.
SeveralanomalydetectionmethodsbasedonGANhavebeenproposedintheliterature,suchasMAD-GAN[129],
USAD[8]andTAnoGAN[17].TheseapproachestrainGANonthenormalsectionsofthetimeseries.Theanomaly
scoreisbasedonthecombinationofdiscriminatorandreconstructionloss.VAE-GAN[171]isanotherGAN-based
modelthatcombinesGANandVariationalAutoencoder.Morespecifically,thegeneratorisaVAE,whichfurther
competeswiththediscriminator.Theanomalyscoreiscomputedthesameastheprevioustwo.
9 EvolutionofMethodsoverTime:AMeta-Analysis
Atthispoint,wedescribedthemainmethodsproposedintheliteraturetodetectanomaliesintimeseries.Wegrouped
themintothreefirst-levelcategoriesand9second-levelcategories.However,thesefirstorsecond-levelcategoriesdo
notsharethesamedistributionintime.Figure20showsthenumberofmethodsproposedperintervalofyears(left)
andthecumulativenumberovertheyears(right).
Wefirstobservethatthenumberofmethodsproposedyearlywasconstantbetween1990and2016.Thenumberof
methodsproposedintheliteraturesignificantlyincreasedafter2016.Thisfirstconfirmsthegrowingacademicinterest
inthetopicoftime-seriesanomalydetection.
Wecanthendiveintothesecond-levelcategories,andweobservethatthesignificantincreaseinmethodsproposed
iscausedmainlybytheprediction-basedapproachand,morespecifically,byLSTMandautoencoder-basedapproaches.
Between2020and2023,suchmethodsrepresentalmost50%ofthenewlyintroducedanomalydetectionmethods.The
greatsuccessofdeeplearningforcomputervisioncausessuchgrowth.Moreover,thankstotheopen-sourcedeep
learninglibrarysuchasTensorFlowandPyTorch,genericdeeplearningmethodsareeasytoadapttotimeseries.
Wecantheninspecttheevolutionofthenumberofmethodsproposedintheliteraturethatcanhandleunivariateor
multivariatetimeseries.Figure21(right)showsthenumberofmethodsformultivariateandunivariatetimeseriesper
intervalofyearslistedonthex-axis.
Surprisingly,weobservethatmostofthemethodsproposedbetween1990and2016wereproposedformultivariate
timeseries,whereas,inthelastthreeyears,mostoftheproposedmethodsareforunivariatetimeseries.However,
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 35
Numberof methodsproposedper
Numberof methodsproposedper
Second-levelcategories(cumulative)
Second-levelcategories
Reconstruction Reconstruction
|            | noitciderP |          | noitciderP  |
| ---------- | ---------- | -------- | ----------- |
| Encoding   | desab      |          | desab       |
| Graph Tree |            | Encoding | Forecasting |
Forecasting
Graph
| Distribution |               |              | ytisneD    |
| ------------ | ------------- | ------------ | ---------- |
|              | ytisneD desab | Distribution | Tree desab |
Discord
Discord
Clustering
|     | ecnatsiD Clustering |     |          |
| --- | ------------------- | --- | -------- |
|     | desab               |     | ecnatsiD |
desab
Proximity
Proximity
Fig.20. Relativenumberofmethodsproposedovertimepercategory,atdifferenttimes-intervals(left),andcumulative(right).
Numberof methodsproposedthatare  Numberof methodsproposedthatcan
Unsupervisedor Semi-Supervised handleUnivariateor Multivariatetime series
desivrepus-imeS
etairavitluM
sdohtem
Multivariate
Semi-Supervised
|     | desivrepusnU |     | etairavinU |
| --- | ------------ | --- | ---------- |
sdohtem
| Unsupervised | Univariate |     |     |
| ------------ | ---------- | --- | --- |
Fig. 21. Number of methods proposed over time that are Unsupervised/Semi-supervised (left), and that can handle univari-
ate/multivariatetimeseries(right).
afteradeepinspection,mostofthemethodsproposedbefore2016weredesignedforpointanomalydetection(i.e.,
well-definedproblemsformultivariatetimeseries).Therecentinterestinsub-sequenceanomalydetection,joinedby
thefactthatthesubsequenceanomalydetectionproblemformultivariatetimeseriesishardertodefine,leadstoa
significantincreaseinmethodsforunivariatetimeseries.
Finally,wecanmeasuretheevolutionofthenumberofunsupervisedandsemi-supervisedmethodsovertheyears.
ThelatterisillustratedinFigure21(left).Weobservethat65%oftheanomalydetectionmethodsproposedinthe
literaturewereunsupervisedbetween1980and2000,whereas50%ofthemethodsproposedbetween2012and2018
wereunsupervised.
ManuscriptsubmittedtoACM

36 Paparrizosetal.
| Table4.       | Summaryofexistingbenchmarksfortime-seriesanomalydetection. |          |           |               |         |
| ------------- | ---------------------------------------------------------- | -------- | --------- | ------------- | ------- |
|               | #Time                                                      | Average  | Average#  | Average       | Anomaly |
| Benchmark     |                                                            |          |           |               | Dim     |
|               | Series                                                     | Length   | Anomalies | AnomalyLength | Type    |
| NAB[126]      | 58                                                         | 6301.7   | 2         | 287.8         | I P&S   |
| Yahoo[125]    | 367                                                        | 1561.2   | 5.9       | 1.8           | I P&S   |
| Exathlon[108] | 93                                                         | 25115.9  | 1         | 9537.6        | M S     |
| KDD21[113]    | 250                                                        | 77415.1  | 1         | 196.5         | I P&S   |
| TODS[123]     | 54                                                         | 13469.9  | 266.7     | 2.3           | I&M P&S |
| TimeEval[216] | 976                                                        | 30991    | 5.5       | 106.7         | I&M P&S |
| TSB-UAD[185]  | 14046                                                      | 34043.6  | 86.3      | 24.9          | I P&S   |
| TSB-AD[142]   | 1070(Curated)                                              | 105485.2 | 104.2     | 409.5         | I&M P&S |
I:Univariate;M:Multivariate//P:Point;S:Subsequence
Thestatisticsarebasedonthedatasetsdownloadedduringthewritingofthisarticle.
10 EvaluatingAnomalyDetection
Withthecontinuousadvancementoftime-seriesanomalydetectionmethods,itbecomesevidentthatdifferentmethods
possessdistinctpropertiesandmaybemoresuitableforspecificdomains.Moreover,themetricsusedtoevaluate
thesemethodsvarysignificantlyintermsoftheircharacteristics.Consequently,evaluatingandselectingthemost
appropriatemethodforagivenscenariohasemergedasamajorchallengeinthisfield.Inthissection,wewillbegin
bypresentingthebenchmarksthathavebeenproposedintheliteratureforevaluatingtime-seriesanomalydetection
methods.Then,wewilldiscussdifferentevaluationmeasurescommonlyusedinthefieldandexaminetheirlimitations
whenappliedtoanomalydetection.
10.1 ExistingBenchmarks
Inprevioussections,wenotedthatasubstantialnumberoftime-seriesanomalydetectionmethodshavebeendeveloped
overthepastseveraldecades.Multiplesurveysandexperimentalstudieshaveevaluatedtheperformanceofvarious
anomalydetectorsacrossdifferentdatasets[185,216,235].Theseinvestigationshaveconsistentlyhighlightedthe
absenceofaone-size-fits-allanomalydetector.Theemergingconsensusacknowledgesthatamodelperformingwellon
onedatasetisnotsufficienttodeclareananomalydetectionalgorithmuseful.Theeffectivenessofananomalydetector
shouldbedemonstratedacrossawiderangeofdatasetsratherthanseveralcherry-pickingdatasets.Consequently,
therehavebeeneffortsmadetoestablishbenchmarksincorporatingmultipledatasetsfromvariousdomainstoensure
thoroughandcomprehensiveevaluation.
Inthefollowing,wewilloverviewrecentbenchmarksfortime-seriesanomalydetection.Thesebenchmarksare
presentedchronologically,asillustratedinTable4,withbriefdescriptionstodemonstrateadvancementsinthisfield.
NAB[126]provides58labeledreal-worldandartificialtimeseries,primarilyfocusingonreal-timeanomalydetection
forstreamingdata.ItcomprisesdiversedomainssuchasAWSservermetrics,onlineadvertisementclickingrates,
real-timetrafficdata,andacollectionofTwittermentionsoflargepublicly-tradedcompanies.
Yahoo[125]comprisesacollectionofrealandsynthetictimeseriesdatasets,whicharederivedfromtherealproduction
traffictosomeoftheYahooproductionsystems.
Exathlon[108]isproposedforexplainableanomalydetectionoverhigh-dimensionaltimeseriesdata.Itisconstructed
basedonrealdatatracesfromrepeatedexecutionsoflarge-scalestreamprocessingjobsonanApacheSparkcluster.
KDD21(orUCRAnomalyArchive)[113]isacompositedatasetthatcoversvariousdomains,suchasmedicine,sports,
andspacescience.Itwasdesignedtoaddressthepitfallsofpreviousbenchmarks[251].
TODS[123]refinessyntheticcriterionandincludesfiveanomalyscenarioscategorizedbybehavior-driventaxonomy
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 37
aspoint-global,pattern-contextual,pattern-shapelet,pattern-seasonal,andpattern-trend.
TimeEval[216]comprisesacollectionofdatasets(bothrealandsynthetic)fromverydifferentdomains.Thisbenchmark
containsbothunivariateandmultivariatetimeseriesmixingbothpointandsequenceanomalies.Inaddition,this
benchmarkhasbeenfilteredsuchthatthereisnotimeseriesthathaveanormal/abnormalratioabove0.1,andthatat
leastonemethodperformsmorethan0.8AUC-ROCforeachtimeseries.
TSB-UAD[185]isacomprehensiveandunifiedbenchmarkdesignedforevaluatingunivariatetime-seriesanomaly
detectionmethods.Itincludespublicdatasetsthatcontainreal-worldanomalies,aswellassyntheticdatasetsthat
provideeleventransformationmethodstoemulatedifferentanomalytypes.Additionally,thebenchmarkincorporates
artificialdatasetsthataretransformedfromtime-seriesclassificationdatasetswithvaryinglevelsofsimilaritybetween
normalandabnormalsubsequences.ThiscomprehensivecoverageofdifferentanomalyscenariosmakesTSB-UADa
uniformplatformtocomparedifferentmethodsacrossdifferentrealisticscenarios.
Wenotethatthereareongoingdiscussionsregardingthelimitationsofcertaindatasetsusedinexistingbenchmarks.
Wuetal.[251]identifyfourcommonflaws:(i)triviality,(ii)unrealisticanomalydensity,(iii)mislabeledgroundtruth,and
(iv)run-to-failurebias.Suchissuesunderscorethesubstantialchallengesindesigningtrulyrepresentativebenchmarks.
Inresponse,Wuetal.developamanuallycurateddatasetconsistingprimarilyofunivariatetimeseriesfeaturinga
single,oftenartificiallyintroducedanomaly.However,thisdatasetmaynotaccuratelyreflectreal-worldscenarios
(giventhatmostpreviouslypublishedreal-worlddatasetscontainmultipleanomalies)andexcludesotherpotentially
anomalousregions,resultinginanewsetoflabelingambiguities.Toaddresstheseconcerns,TSB-AD[142]introduces
thefirstlarge-scale,heterogeneous,andmeticulouslycurateddataset,combininghumanperceptionwithmodel-driven
interpretationtoofferimprovedreliability.
TSB-AD[142]isthelargestbenchmarktodate,comprising1,000rigorouslycurated,high-qualitytimeseriesdatasets.
Thisbenchmarkincludebothunivariateandmultivariatecases,ensuringcoverageofawiderangeofreal-world
scenariosforanomalydetection.Itestablishesareliableframeworkforevaluatingmethodsandincludescomprehensive
benchmarkingof40anomalydetectionapproaches(continuouslyupdating2).Eachmethodundergoesathorough
hyperparameter tuning to ensure optimal performance. The benchmark also incorporates the latest advances in
foundationmodel-basedmethods,highlightingtheirpotentialfortimeseriesanomalydetection.
10.2 EvaluationMeasures
Inthissection,wepresentanoverviewofevaluationmetricsusedtoassesstheperformanceofanomalydetectors.
Therearevariouswaystocategorizetheevaluationmetrics.Itcanbeclassifiedbasedonwhetherathresholdneedsto
besetoriftheevaluationisconductedonindependenttimepointsorsequences.Inthefollowing,wewillcategorize
theevaluationbasedontherequirementofthresholdsetting.
10.2.1 Threshold-basedEvaluation. Threshold-basedevaluationrequiressettingathresholdtoclassifyeachpoint(time
step)asananomalyornotbasedontheanomalyscore𝑆 𝑇.Generally,ahigheranomalyscorevalueindicatesamore
abnormalpoint.Themoststraightforwardapproachistosetthethresholdto𝜇(𝑆 𝑇)+𝛼∗𝜎(𝑆 𝑇),with𝛼 setto3[15],
where𝜇(𝑆 𝑇)isthemeanand𝜎(𝑆 𝑇)isthestandarddeviationof𝑆 𝑇.However,thisapproachissensitivetoextreme
valuesintheanomalyscoreandcanresultinunfaircomparisonsbetweendifferentmethodsduetovariationsintheir
statisticalproperties.
2https://thedatumorg.github.io/TSB-AD
ManuscriptsubmittedtoACM

| 38  |     |     |     |     |     |     |     |     | Paparrizosetal. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- |
𝑠𝑒𝑡𝑜𝑓
| 1   |     | 1   |     |     |     | 1   | 𝑤𝑖𝑛𝑑𝑜𝑤ℓ | 1   | 𝑤𝑖𝑛𝑑𝑜𝑤ℓ |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------- | --- |
𝑃𝑜𝑖𝑛𝑡−𝑤𝑖𝑠𝑒𝑃𝑟𝑒𝑑𝑖𝑐𝑡𝑖𝑜𝑛
| 𝑙𝑒𝑏𝑎𝑙 |     | 𝑙𝑒𝑏𝑎𝑙 |     |     |     | ℓ𝑙𝑒𝑏𝑎𝑙 | 1/2 | ℓ𝑙𝑒𝑏𝑎𝑙 | 1/2 |     |
| ----- | --- | ----- | --- | --- | --- | ------ | --- | ------ | --- | --- |
𝑃𝑜𝑖𝑛𝑡−𝑎𝑑𝑗𝑢𝑠𝑡𝑒𝑑𝑃𝑟𝑒𝑑𝑖𝑐𝑡𝑖𝑜𝑛
| 0   | e   | 0   | s   |     |     | −ℓ/2+𝑠 0 | 𝑠 𝑒 𝑒+ℓ/2 | 0 −ℓ/2+𝑠 𝑠 | 𝑒 𝑒+ℓ/2 |     |
| --- | --- | --- | --- | --- | --- | -------- | --------- | ---------- | ------- | --- |
|     | s   |     | e   |     |     |          |           |            |         |     |
𝑒𝑟𝑜𝑐𝑠𝑦𝑙𝑎𝑚𝑜𝑛𝑎 𝑒𝑟𝑜𝑐𝑠𝑦𝑙𝑎𝑚𝑜𝑛𝑎 𝑆𝑒𝑡𝑜𝑓 𝑒𝑟𝑜𝑐𝑠𝑦𝑙𝑎𝑚𝑜𝑛𝑎 𝑆𝑒𝑡𝑜𝑓 𝑒𝑟𝑜𝑐𝑠𝑦𝑙𝑎𝑚𝑜𝑛𝑎 𝑆𝑒𝑡𝑜𝑓
|     |     |     |     | 𝑡ℎ𝑟𝑒𝑠ℎ𝑜𝑙𝑑𝑇 |     |     | 𝑡ℎ𝑟𝑒𝑠ℎ𝑜𝑙𝑑𝑇 |     | 𝑡ℎ𝑟𝑒𝑠ℎ𝑜𝑙𝑑𝑇 |     |
| --- | --- | --- | --- | ---------- | --- | --- | ---------- | --- | ---------- | --- |
𝑇ℎ𝑟𝑒𝑠ℎ𝑜𝑙𝑑𝑇
|     | 𝑡𝑖𝑚𝑒𝑖𝑛𝑑𝑒𝑥      |     | 𝑡𝑖𝑚𝑒𝑖𝑛𝑑𝑒𝑥 |     |     |     | 𝑡𝑖𝑚𝑒𝑖𝑛𝑑𝑒𝑥 | 𝑡𝑖𝑚𝑒𝑖𝑛𝑑𝑒𝑥 |     |     |
| --- | -------------- | --- | --------- | --- | --- | --- | --------- | --------- | --- | --- |
|     | 𝑃𝑜𝑖𝑛𝑡−𝑎𝑑𝑗𝑢𝑠𝑡𝑒𝑑 |     |           |     |     | 𝑅𝑃𝑇 |           |           |     |     |
| 𝑅𝑃𝑇 | 𝑃𝑜𝑖𝑛𝑡−𝑤𝑖𝑠𝑒     | 𝑅𝑃𝑇 |           |     |     |     |           |           |     | 𝑅𝑃𝑇 |
ℓ
|     | 𝐹𝑃𝑅                            |                                                                 |           | 𝐹𝑃𝑅 |     |                                      | 𝐹𝑃𝑅             | 𝐹𝑃𝑅                            |     |     |
| --- | ------------------------------ | --------------------------------------------------------------- | --------- | --- | --- | ------------------------------------ | --------------- | ------------------------------ | --- | --- |
|     |                                |                                                                 | (b.1) AUC |     |     |                                      | (b.2) Range-AUC | (b.3) Volume Under the Surface |     |     |
|     | (a) Threshold-based Evaluation |                                                                 |           |     |     | (b) Threshold-independent Evaluation |                 |                                |     |     |
|     | Fig.22.                        | Illustrationofevaluationmeasuresfortime-seriesanomalydetection. |           |     |     |                                      |                 |                                |     |     |
Toaddressthisissue,researchersinthefieldhavedevelopedalternativemethodsforthresholdselectionthatoperate
automatically,eliminatingtheneedforstatisticalassumptionsregardingerrors.Forinstance,[5]introducedanadaptive
thresholdingtechniquethatexploitstheconsistenttimecorrelationstructureobservedinanomalyscoresduring
benignactivityperiods.Thistechniquedynamicallyadjuststhethresholdbasedonpredictedfutureanomalyscores.
Non-parametricdynamicthresholding,proposedin[104],aimstofindathresholdsuchthatremovingallvaluesabove
itresultsinthegreatestpercentagedecreaseinthemeanandstandarddeviationoftheanomalyscores.Another
approach,knownasPeaks-Over-Threshold(POT)[224,232],involvesaninitialthresholdselection,identificationof
extremevaluesinthetailsofaprobabilitydistribution,fittingthetailportionwithageneralizedParetodistribution
withparameters,computinganomalyscoresbasedontheestimateddistribution,andapplyingasecondarythresholdto
identifyanomalies.
Aftersettingthethreshold,wecanclassifythepointsaseithernormalorabnormalbasedonwhethertheyexceed
the threshold. In the subsequent section, we will review common evaluation measures. We begin by presenting
thenecessarydefinitionsandformulationsforintroducingthesemeasures,followedbyabriefexplanationoftheir
∈{0,1}𝑛
distinctions.Formally,thebinarypredictions𝑝𝑟𝑒𝑑 areobtainedbycomparing𝑆 𝑇 withthreshold𝑇ℎas:
|     |     |     |     |     |     | 0, | if:𝑆 <𝑇ℎ |     |     |     |
| --- | --- | --- | --- | --- | --- | ------ | -------- | --- | --- | --- |
𝑇𝑖
|     |     |     | ∀𝑖 ∈ [1,|𝑆 | 𝑇|],𝑝𝑟𝑒𝑑 | 𝑖   | =    |             |     |     | (18) |
| --- | --- | --- | ---------- | -------- | --- | ---- | ----------- | --- | --- | ---- |
|     |     |     |            |          |     | 1, | if:𝑆 𝑇𝑖 ≥𝑇ℎ |     |     |      |

| Bycomparing𝑝𝑟𝑒𝑑tothetrue-labeledanomalies𝑙𝑎𝑏𝑒𝑙 |     |     |     |     |     | ∈{0,1}𝑛 |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
,thepointscanfallintooneofthefollowingfour
categories:
• TruePositive(TP):Numberofpointsthathavebeencorrectlyidentifiedasanomalies.
• TrueNegative(TN):Numberofpointsthathavebeencorrectlyidentifiedasnormal.
• FalsePositive(FP):Numberofpointsthathavebeenwronglyidentifiedasanomalies.
• FalseNegative(FN):Numberofpointsthathavebeenwronglyidentifiedasnormal.
Giventhesefourcategories,severalpoint-wiseevaluationmeasureshavebeenproposedtoassesstheaccuracyof
anomalydetectionmethods.
Precision(orpositivepredictivevalue)isthenumberofcorrectlyidentifiedanomaliesoverthetotalnumberofpoints
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 39
𝑇𝑃
detectedasanomaliesbythemethod:𝑇𝑃+𝐹𝑃.
𝑇𝑃
Recall(orTruePositiveRate,TPR)isthenumberofcorrectlyidentifiedanomaliesoverallanomalies:𝑇𝑃+𝐹𝑁.
FalsePositiveRate(orFPR)isthenumberofpointswronglyidentifiedasanomaliesoverthetotalnumberofnormal
𝐹𝑃
points: 𝐹𝑃+𝑇𝑁.ContrarytoRecall,theoptimalscoreisobtainedbypredictingallthepointsasnormal.
F-Scorecombinesprecisionandrecallintoasinglemetricbytakingtheirharmonicmean,withanon-negativereal
valueof𝛽:
(1+𝛽2)∗𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛∗𝑅𝑒𝑐𝑎𝑙𝑙
.Usually,𝛽issetto1,balancingtheimportancebetweenPrecisionandRecall.
𝛽2∗𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+𝑅𝑒𝑐𝑎𝑙𝑙
Precision@kistheprecisionofasubsetofanomaliescorrespondingto𝑘highestvalueintheanomalyscore𝑆 𝑇.
Whilemostcurrentmethods[222,232,255]calculatethesemetricsbytreatingtimepointsasindependentsamples,
theyoftenemploypointadjustmenttechniquestoaccountforconsecutiveanomalies.Thismeansthatdetectingany
pointwithinananomaloussegmentisconsideredasifallpointswithinthatsegmentweredetected,asisshownin
Figure22(a).However,theworkof[118]criticizestheuseofpoint-adjustedmetrics,demonstratingthattheyhaveahigh
likelihoodofoverestimatingdetectionperformanceandthatevenarandomanomalyscorecanyieldseeminglygood
results.Inlightofthiscritique,[118]proposePoint-adjustedmetricsat𝐾%,whereinapredeterminedproportion𝐾%
ofanomaliesmustbedetectedbeforetheapplicationofpointadjustment.Otherrefinedpoint-adjustedmetricsinclude
Delaythresholdedpoint-adjustedF-scorein[52,204].Thismetricconsidersananomalytobedetectedonlyifitis
predictedwithinthefirst𝑘timestepsofthetruth-labeledanomaly.
Furthermore, the above-mentioned metrics ignore the sequential nature of time series. A range-based quality
measure[237]wasrecentlyproposedtoaddresstheshortcomingsofpoint-basedmeasures.Thisdefinitionconsiders
severalfactors:(i)whetherasubsequenceisdetectedornot(ExistenceReward);(ii)howmanypointsinthesubsequence
aredetected(OverlapReward);(iii)whichpartofthesubsequenceisdetected(position-dependentweightfunction);
and(iv)howmanyfragmentedregionscorrespondtoonerealsubsequenceoutlier(CardinalityFactor).Inthisway,
point-basedPrecisionandRecallcanbeextendedtocalculatingRange-basedF-score.
OthermetricsincludeNABscore[126],whichpenalizesfalsepositivepointsbyassigninganegativevalueand
providespositivevaluerewardsforaccuratelydetectinganomaloussegments,withtherewardbeinghigherforearly
predictionofthefirstanomalouspoint.ItisnoteworthythattheutilizationoftheNABscoreitselfisnotwidespread;
however,thebenchmarkintroducedinthispaperiswidelyadoptedintheresearchcommunityforevaluationusing
othermetrics.
10.2.2 Threshold-independentEvaluation. Therequirementtoapplyathresholdtotheanomalyscoresignificantly
affectstheaccuracymeasures.Theycanvarysignificantlywhenthethresholdchanges.Accordingtoarecentwork[180],
threshold-basedmeasuresareparticularlysensitivetothenoisyanomalyscore,whichstemfromnoiseintheoriginaltime
series.Asthescorefluctuatesaroundthethreshold,theybecomelessrobusttonoise.Moreover,thenormal/abnormal
ratio,whichexhibitsconsiderablevariabilityacrossdifferenttasks,furtherinfluencesthethreshold.Notably,variations
inthisratiocanleadtovariationsinthethreshold,consequentlyimpactingthevaluesofthreshold-basedaccuracy
measures.Additionally,detectorsmayintroducealagintotheanomalyscore,andtheremaybeinherentlagresulting
from the approximation made during the labeling phase. Even small lags can have a significant impact on these
evaluationmeasures.Therefore,manyworksconsiderthresholdselectionasaproblemorthogonaltomodelevaluation
andusemetricsthatsummarizethemodelperformanceacrossallpossiblethresholds.Wewillintroduceseveral
threshold-independentevaluationmeasuresasfollows.
BestF-Score:MaximumF-Scoreoverallpossiblethresholds.
AUC:TheAreaUndertheReceiverOperatingCharacteristicscurve(AUC-ROC)[66]isawidelyusedevaluation
ManuscriptsubmittedtoACM

40 Paparrizosetal.
metricinanomalydetection,aswellasinbinaryclassificationingeneral.Itquantifiestheperformanceofamodel
bymeasuringtheareaunderthecurvethatrepresentsthetruepositiverate(TPR)onthey-axisagainstthefalse
positiverate(FPR)onthex-axis,asdepictedinFigure22(b.1).AUC-ROCrepresentstheprobabilitythatarandomly
chosenpositiveexamplewillberankedhigherthanarandomlychosennegativeexample.Itiscomputedusingthe
trapezoidalrule.Forthatpurpose,wedefineanorderedsetofthresholds,denotedas𝑇ℎ,rangingfrom0to1,where
𝑇ℎ= [𝑇ℎ
0
,𝑇ℎ
1
,...𝑇ℎ 𝑁]with0=𝑇ℎ
0
<𝑇ℎ
1
<...<𝑇ℎ
𝑁
=1.Therefore,𝐴𝑈𝐶-𝑅𝑂𝐶isdefinedasfollows:
𝑁
𝐴𝑈𝐶-𝑅𝑂𝐶 = 1∑︁ Δ
𝑇
𝑘
𝑃𝑅
∗Δ𝑘
𝐹𝑃𝑅
2
𝑘=1
(19)
 Δ𝑘 𝐹𝑃𝑅 =𝐹𝑃𝑅(𝑇ℎ 𝑘)−𝐹𝑃𝑅(𝑇ℎ 𝑘−1 )
with:
 Δ 𝑇 𝑘 𝑃𝑅 =𝑇𝑃𝑅(𝑇ℎ 𝑘−1 )+𝑇𝑃𝑅(𝑇ℎ 𝑘)

TheAreaUnderthePrecision-Recallcurve(AUC-PR)[58]issimilar,butwiththeRecall(TPR)onthex-axisand
Precisiononthey-axis.ThePrecisionandFPRexhibitdistinctresponsestochangesinfalsepositivesinthecontextof
anomalydetection.Inthisdomain,thenumberoftruenegativestendstobesubstantiallylargerthanthenumberof
falsepositives,resultinginlowFPRvaluesforvariousthresholdchoicesthatarerelevant.Consequently,onlyasmall
portionoftheROCcurveholdsrelevanceundersuchcircumstances.Onepotentialapproachtoaddressthisissueisto
focussolelyonspecificsegmentsofthecurve[10].Alternatively,theuseoftheAUC-PRhasbeenadvocatedasamore
informativealternativetoROCforimbalanceddatasets[145].
Range-AUC:AUC-ROCandAUC-PRareprimarilydesignedforpoint-basedanomalies,treatingeachpointinde-
pendentlyandassigningequalweighttothedetectionofeachpointincalculatingtheoverallAUC.However,these
metricsmaynotbeidealforassessingsubsequenceanomalies.Thereareseveralreasonsforthislimitation,including
theimportanceofdetectingevensmallsegmentswithinsubsequenceoutliers,theabsenceofconsistentlabelingcon-
ventionsacrossdatasets,especiallyforsubsequences,andthesensitivityoftheanomalyscorestotimelagsintroduced
bydetectors.Toaddresstheselimitations,anextensionoftheROCandPRcurvescalledRange-AUC[180]hasbeen
introducedspecificallyforsubsequences.Byaddingabufferregionattheoutliers’boundariesasshowninFigure
22(b.2),itaccountsforthefalsetoleranceoflabelinginthegroundtruthandassignshigheranomalyscoresnearthe
outlierboundaries.Itreplacesbinarylabelswithcontinuousvaluesintherange[0,1].Thisrefinementenablesthe
adaptationofpoint-basedTPR,FPR,andPrecisiontobettersuitsubsequenceanomalycases.
VolumeUndertheSurface(VUS)[180]:ThebufferlengthinRange-AUC,denotedas𝑙,needstobepredefined.Ifnot
properlyset,itcanstronglyinfluencerange-AUCmeasures.Toeliminatethisinfluence,VUScomputesRange-AUC
fordifferentbufferlengthsfrom0tothe𝑙,whichleadstothecreationofathree-dimensionalsurfaceintheROC-PR
spaceasshowninFigure22(b.3).TheVUSfamilyofmeasures,includingVUS-ROCandVUS-PR,areparameter-free
andthreshold-independent,applicableforevaluatingbothpoint-basedandrange-basedanomalies.
Differentevaluationmethodshavedifferentproperties,includingrobustnesstolagandnoise,theseparabilityto
differentiatebetweenaccurateandinaccuratemethods,andtheneedforparameters,etc.Therefore,theselectionof
evaluationmetricsshouldbeapproachedwithcaution,consideringthespecificrequirementsofthetask.Fordetailed
casestudieshighlightingthepropertiesofdifferentmetrics,werecommendreferringtothefollowingpapers[180,229].
Intermsofkeytakeaways,werecommendutilizingthreshold-independentevaluationmeasurestomitigatepotential
biasesintroducedbythresholdselection.AUC-basedmeasureshavebeenwidelyadoptedinthisregard.However,their
limitationslieinthelackofconsiderationfortheconsistencyoftimeseries.Toaddressthis,Range-AUChasrefined
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 41
theAUC-basedmeasures.Amongtherange-basedmeasures,VUS-ROCstandsoutforitsrobustness,separability,
andconsistencyinrankingtheaccuracyofdetectorsacrossdiversedatasets,makingitarecommendedchoiceasthe
evaluationmeasureofpreference.
11 Conclusions
Inthissurvey,weexaminedintotheanomalydetectionproblemintimeseries.Westartedbydefiningataxonomyof
timeseriestypes,anomalytypes,andanomalydetectionmethods.Wegroupedthemethodsintomultipleprocess-centric
categories.Wethendescribedthemostpopularanomalydetectionmethodsforeachcategoryindetail,andprovidedan
extensivelistofotherexistingmethods.Wefinallydiscussedtheproblemofbenchmarkingandevaluationofanomaly
detectionmethodsintimeseries.Weinitiatedthisdiscussionbylistingthetimeseriesdatasetandbenchmarkproposed
intheliterature.Wethenlistedthetraditionalevaluationmeasuresusedtoassessthedetectionquality,discussedtheir
limitations,andintroducedarecentefforttoadaptthesemeasurestothecontextoftimeseries.
Despitethedecades-longworthofresearchinthisarea,time-seriesanomalydetectionremainsachallengingproblem.
Several communities have tackled the problem separately, introducing methods that follow their corresponding
fundamentalconcepts.Sincethesemethodswerenotcomparedonthesamebasis(i.e.,usingthesameevaluation
measuresanddatasets),theprogressofanomalydetectionmethodshasbeenchallengingtoassess.However,therecent
effortsinproposingbenchmarks[113,185]hashelpedtoevaluatetheprogressandidentifyappropriatemethodsfor
specificproblems[185,216].
Nevertheless,multipleresearchdirectionsremainopen.First,thereisnoagreementyetonasinglebenchmark
thattheentirecommunityshoulduse.Eventhoughnumerousbenchmarkshavebeenproposed,theyhavetheirown
limitationsconcerningthediversityoftimeseries,anomalytypes,oruncertainlabels.Thereisaneedtoagreeasa
communityonacommonbasisforcomparingtheanomalydetectionmethods.
Second,encouragedbythecurrentmomentum,manynovelmethodsareproposedeveryyear.However,recent
evaluationssuggested[185,216]thatnosinglebestmethodexists(i.e.,achievingthebestperformanceoneverydataset).
Thisobservationopensanewdirectionofresearchtowardsensembling,modelselection,andAutoML.Arecent
experimentalevaluation[235]concludedthatsimpletimeseriesclassificationbaselinescanbeusedformodelselection
fortime-seriesanomalydetection,leadingtoaccuracyimprovementsbyafactorof2comparedtothebestperforming
individualanomalydetectionmethod.Thisstudysuggeststhatwecanbeoptimisticaboutfurtherimprovementsin
accuracy,bycontinuingtheresearchinthisdirection.
Finally,eventhoughalargenumberofunsupervisedmethodshavebeenproposedforunivariatetime-seriesanomaly
detection,notmuchattentionhasbeenpaidtomultivariatetimeseries,streamingtimeseries,serieswithmissing
values,serieswithnon-continuoustimestamps,heterogeneoustimeseries,oracombinationoftheabove.Suchtimes
seriesareoftenencounteredinpractice,thusweneedrobustandaccuratemethodsforthesecases,aswell.
References
[1] AliAbdul-Aziz,MarkWoike,NikunjOza,BryanMatthews,andGeorgeBaakilini.2010.Propulsionhealthmonitoringofaturbineenginedisk
usingspintestdata.InHealthMonitoringofStructuralandBiologicalSystems2010,TribikramKundu(Ed.),Vol.7650.InternationalSocietyfor
OpticsandPhotonics,SPIE,431–440. https://doi.org/10.1117/12.847574
[2] CharuCAggarwal.2017.Anintroductiontooutlieranalysis.InOutlieranalysis.Springer,1–34.
[3] SubutaiAhmad,AlexanderLavin,ScottPurdy,andZuhaAgha.2017.UnsupervisedReal-TimeAnomalyDetectionforStreamingData.262(2017),
134–147. https://doi.org/10.1016/j.neucom.2017.04.070
[4] ShadabAlam,FrancoDAlbareti,CarlosAllendePrieto,FriedrichAnders,ScottFAnderson,TimothyAnderton,BrettHAndrews,EricArmengaud,
ÉricAubourg,StephenBailey,etal.2015.TheeleventhandtwelfthdatareleasesoftheSloanDigitalSkySurvey:finaldatafromSDSS-III.The
ManuscriptsubmittedtoACM

42 Paparrizosetal.
AstrophysicalJournalSupplementSeries219,1(2015),12.
[5] MuhammadQasimAli,EhabAl-Shaer,HassanKhan,andSyedAliKhayam.2013.Automatedanomalydetectoradaptationusingadaptivethreshold
tuning.ACMTransactionsonInformationandSystemSecurity(TISSEC)15,4(2013),1–30.
[6] FranciscoMartinezAlvarez,AliciaTroncoso,JoseCRiquelme,andJesusSAguilarRuiz.2010.Energytimeseriesforecastingbasedonpattern
sequencesimilarity.IEEETransactionsonKnowledgeandDataEngineering23,8(2010),1230–1243.
[7] JérômeAntoniandPietroBorghesani.2019. AStatisticalMethodologyfortheDesignofConditionIndicators. 114(2019),290–327. https:
//doi.org/10.1016/j.ymssp.2018.05.012
[8] JulienAudibert,PietroMichiardi,FrédéricGuyard,SébastienMarti,andMariaAZuluaga.2020. Usad:Unsupervisedanomalydetectionon
multivariatetimeseries.InSIGKDD.3395–3404.
[9] MartinBach-Andersen,BoRømer-Odgaard,andOleWinther.2017.Flexiblenon-linearpredictivemodelsforlarge-scalewindturbinediagnostics.
WindEnergy20,5(2017),753–764.
[10] StuartGBakerandPaulFPinsky.2001.Aproposeddesignandanalysisforcomparingdigitalandanalogmammography:specialreceiveroperating
characteristicmethodsforcancerscreening.J.Amer.Statist.Assoc.96,454(2001),421–428.
[11] ZivBar-Joseph.2004.Analyzingtimeseriesgeneexpressiondata.Bioinformatics20,16(2004),2493–2503.
[12] ZivBar-Joseph,GeorgKGerber,DavidKGifford,TommiSJaakkola,andItamarSimon.2003.Continuousrepresentationsoftime-seriesgene
expressiondata.JournalofComputationalBiology10,3-4(2003),341–356.
[13] ZivBar-Joseph,AnthonyGitter,andItamarSimon.2012.Studyingandmodellingdynamicbiologicalprocessesusingtime-seriesgeneexpression
data.NatureReviewsGenetics13,8(2012),552.
[14] MohiniBariya,AlexandravonMeier,JohnPaparrizos,andMichaelJFranklin.2021.k-ShapeStream:ProbabilisticStreamingClusteringforElectric
GridEvents.In2021IEEEMadridPowerTech.IEEE,1–6.
[15] V.BarnetandT.Lewis.1994.OutliersinStatisticalData.JohnWileyandSons,Inc.
[16] VicBarnettandTobyLewis.1984. Outliersinstatisticaldata. WileySeriesinProbabilityandMathematicalStatistics.AppliedProbabilityand
Statistics(1984).
[17] MdAbulBasharandRichiNayak.2020.TAnoGAN:Timeseriesanomalydetectionwithgenerativeadversarialnetworks.InSSCI.IEEE,1778–1785.
[18] SabyasachiBasuandMartinMeckesheimer.2007. AutomaticOutlierDetectionforTimeSeries:AnApplicationtoSensorData. 11,2(2007),
137–154. https://doi.org/10.1007/s10115-006-0026-6
[19] DanielBernoulliandCGAllen.1961.Themostprobablechoicebetweenseveraldiscrepantobservationsandtheformationtherefromofthemost
likelyinduction.Biometrika48,1-2(1961),3–18.
[20] ArpitaBhargavaandASRaghuvanshi.2013.AnomalydetectioninwirelesssensornetworksusingS-TransformincombinationwithSVM.In2013
5thInternationalConferenceandComputationalIntelligenceandCommunicationNetworks.IEEE,111–116.
[21] BharatBBiswal,MaartenMennes,Xi-NianZuo,SurilGohel,ClareKelly,SteveMSmith,ChristianFBeckmann,JonathanSAdelstein,RandyL
Buckner,StanColcombe,etal.2010.Towarddiscoveryscienceofhumanbrainfunction.ProceedingsoftheNationalAcademyofSciences107,10
(2010),4734–4739.
[22] AneBlázquez-García,AngelConde,UsueMori,andJoseALozano.2021. Areviewonoutlier/anomalydetectionintimeseriesdata. ACM
ComputingSurveys(CSUR)54,3(2021),1–33.
[23] PaulBoniol,MicheleLinardi,FedericoRoncallo,andThemisPalpanas.2020.AutomatedAnomalyDetectioninLargeSequences.InProceedingsof
theInternationalConferenceonDataEngineering(ICDE).1834–1837. https://doi.org/10.1109/ICDE48307.2020.00182
[24] PaulBoniol,MicheleLinardi,FedericoRoncallo,andThemisPalpanas.2020.SAD:AnUnsupervisedSystemforSubsequenceAnomalyDetection.
InProceedingsoftheInternationalConferenceonDataEngineering(ICDE).1778–1781. https://doi.org/10.1109/ICDE48307.2020.00168
[25] PaulBoniol,MicheleLinardi,FedericoRoncallo,ThemisPalpanas,MohammedMeftah,andEmmanuelRemy.2021.Unsupervisedandscalable
subsequenceanomalydetectioninlargedataseries.TheVLDBJournal(March2021). https://doi.org/10.1007/s00778-021-00655-8
[26] PaulBoniolandThemisPalpanas.2020. Series2Graph:Graph-BasedSubsequenceAnomalyDetectionforTimeSeries. 13,11(2020),14.
https://doi.org/10.14778/3407790.3407792
[27] PaulBoniol,JohnPaparrizos,YuhaoKang,ThemisPalpanas,RueySTsay,AaronJElmore,andMichaelJFranklin.2022.Theseus:navigatingthe
labyrinthoftime-seriesanomalydetection.ProceedingsoftheVLDBEndowment15,12(2022),3702–3705.
[28] PaulBoniol,JohnPaparrizos,andThemisPalpanas.2023.NewTrendsinTimeSeriesAnomalyDetection..InEDBT.847–850.
[29] PaulBoniol,JohnPaparrizos,andThemisPalpanas.2024.AnInteractiveDiveintoTime-SeriesAnomalyDetection.In2024IEEE40thInternational
ConferenceonDataEngineering(ICDE).
[30] PaulBoniol,JohnPaparrizos,ThemisPalpanas,andMichaelJFranklin.2021.Sandinaction:subsequenceanomalydetectionforstreams.Proceedings
oftheVLDBEndowment14,12(2021),2867–2870.
[31] PaulBoniol,JohnPaparrizos,ThemisPalpanas,andMichaelJFranklin.2021.SAND:streamingsubsequenceanomalydetection.PVLDB14,10
(2021),1717–1729.
[32] PaulBoniol,EmmanouilSylligardos,JohnPaparrizos,PanosTrahanias,andThemisPalpanas.2024.ADecimo:ModelSelectionforTimeSeries
AnomalyDetection.In2024IEEE40thInternationalConferenceonDataEngineering(ICDE).
[33] MohammadBraeiandSebastianWagner.2020. Anomalydetectioninunivariatetime-series:Asurveyonthestate-of-the-art. arXivpreprint
arXiv:2004.00433(2020).
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 43
[34] MarkusMBreunig,Hans-PeterKriegel,RaymondTNg,andJörgSander.2000.LOF:identifyingdensity-basedlocaloutliers.InProceedingsofthe
2000ACMSIGMODinternationalconferenceonManagementofdata.93–104.
[35] MarkusM.Breunig,Hans-PeterKriegel,RaymondT.Ng,andJörgSander.2000.LOF:IdentifyingDensity-basedLocalOutliers.InSIGMOD.
[36] PeterJBrockwellandRichardADavis.2016.Introductiontotimeseriesandforecasting.springer.
[37] YingyiBu,OscarTat-WingLeung,AdaWai-CheeFu,EamonnJ.Keogh,JianPei,andSamMeshkin.2007.WAT:FindingTop-KDiscordsinTime
SeriesDatabase.InSIAM.
[38] SuratnaBudalakoti,AshokNSrivastava,andMatthewEricOtey.2008.Anomalydetectionanddiagnosisalgorithmsfordiscretesymbolsequences
withapplicationstoairlinesafety.IEEETransactionsonSystems,Man,andCybernetics,PartC(ApplicationsandReviews)39,1(2008),101–113.
[39] C.Bui,N.Pham,A.Vo,A.Tran,A.Nguyen,andT.Le.2018.TimeSeriesForecastingforHealthcareDiagnosisandPrognosticswiththeFocus
onCardiovascularDiseases.InInternationalConferenceontheDevelopmentofBiomedicalEngineeringinVietnam(BME6).SpringerSingapore,
Singapore,809–818.
[40] AnderCarreño,IñakiInza,andJoseALozano.2020.Analyzingrareevent,anomaly,noveltyandoutlierdetectiontermsunderthesupervised
classificationframework.ArtificialIntelligenceReview53,5(2020),3575–3594.
[41] MeteCelik,FilizDadaser-Celik,andAhmetSakirDokuz.2011.AnomalydetectionintemperaturedatausingDBSCANalgorithm.2011International
SymposiumonInnovationsinIntelligentSystemsandApplications(2011),91–95.
[42] SoumenChakrabarti,SunitaSarawagi,andByronDom.1998.MiningSurprisingPatternsUsingTemporalDescriptionLength.InProceedingsofthe
InternationalConferenceonVeryLargeDatabases(VLDB)(VLDB’98,Vol.24).MorganKaufmannPublishersInc.,606–617. https://dl.acm.org/doi/10.
5555/645924.671328
[43] RaghavendraChalapathyandSanjayChawla.2019.DeepLearningforAnomalyDetection:ASurvey.arXiv:1901.03407[cs,stat] http://arxiv.org/
abs/1901.03407
[44] RaghavendraChalapathy,AdityaKrishnaMenon,andSanjayChawla.2017.Robust,DeepandInductiveAnomalyDetection.InMachineLearning
andKnowledgeDiscoveryinDatabases,MichelangeloCeci,JaakkoHollmén,LjupčoTodorovski,CelineVens,andSašoDžeroski(Eds.).Springer
InternationalPublishing,Cham,36–51.
[45] VarunChandola,ArindamBanerjee,andVipinKumar.2009.Anomalydetection:Asurvey.ACMcomputingsurveys(CSUR)41,3(2009),1–58.
[46] VarunChandola,ArindamBanerjee,andVipinKumar.2009.AnomalyDetection:ASurvey.41,3(2009),1–58. https://doi.org/10.1145/1541880.
1541882
[47] V.Chandola,A.Banerjee,andV.Kumar.2012.AnomalyDetectionforDiscreteSequences:ASurvey.24,5(2012),823–839. https://doi.org/10.
1109/TKDE.2010.235
[48] IhChang,GeorgeCTiao,andChungChen.1988.Estimationoftimeseriesparametersinthepresenceofoutliers.Technometrics30,2(1988),
193–204.
[49] MarcusChang,AndreasTerzis,andPhilippeBonnet.2009.Mote-BasedOnlineAnomalyDetectionUsingEchoStateNetworks.InProceedingsofthe
InternationalConferenceonDistributedComputinginSensorSystems(DCOOS)(LectureNotesinComputerScience,Vol.5516),BhaskarKrishnamachari,
SubhashSuri,WendiHeinzelman,andUrbashiMitra(Eds.).SpringerBerlinHeidelberg,72–86. https://doi.org/10.1007/978-3-642-02085-8_6
[50] S.ChauhanandL.Vig.2015. AnomalyDetectioninECGTimeSignalsviaDeepLongShort-TermMemoryNetworks.InProceedingsofthe
InternationalConferenceonDataScienceandAdvancedAnalytics(DSAA).1–7. https://doi.org/10.1109/DSAA.2015.7344872
[51] QingChen,AnguoZhang,TingwenHuang,QianpingHe,andYongduanSong.2020.ImbalancedDataset-BasedEchoStateNetworksforAnomaly
Detection.32,8(2020),3685–3694. https://doi.org/10.1007/s00521-018-3747-z
[52] Run-QingChen,Guang-HuiShi,Wan-LeiZhao,andChang-HuiLiang.2021.AjointmodelforIToperationseriespredictionandanomalydetection.
Neurocomputing448(2021),130–139.
[53] ZhangyuCheng,ChengmingZou,andJianweiDong.2019.OutlierDetectionUsingIsolationForestandLocalOutlierFactor.InProceedingsofthe
ConferenceonResearchinAdaptiveandConvergentSystems(RACS).ACM,161–168. https://doi.org/10.1145/3338840.3355641
[54] DhruvChoudhary,ArunKejariwal,andFrancoisOrsini.2017.OntheRuntime-EfficacyTrade-offofAnomalyDetectionTechniquesforReal-Time
StreamingData.arXiv:1710.04735[cs,eess,stat] http://arxiv.org/abs/1710.04735
[55] WilliamW.Cohen.1995.FastEffectiveRuleInduction.InMachineLearningProceedings1995,ArmandPrieditisandStuartRussell(Eds.).Morgan
Kaufmann,SanFrancisco(CA),115–123. https://doi.org/10.1016/B978-1-55860-377-6.50023-2
[56] AndrewA.Cook,GokselMisirli,andZhongFan.2020. AnomalyDetectionforIoTTime-SeriesData:ASurvey. 7,7(2020),6481–6494.
https://doi.org/10.1109/JIOT.2019.2958185
[57] MadalenaCosta,AryLGoldberger,andC-KPeng.2002.Multiscaleentropyanalysisofcomplexphysiologictimeseries.Physicalreviewletters89,
6(2002),068102.
[58] JesseDavisandMarkGoadrich.2006.TherelationshipbetweenPrecision-RecallandROCcurves.InICML.233–240.
[59] NanDing,HuanboGao,HongyuBu,HaoxuanMa,andHuaiweiSi.2018.Multivariate-Time-Series-DrivenReal-TimeAnomalyDetectionBasedon
BayesianNetwork.18,10(2018),3367. https://doi.org/10.3390/s18103367
[60] WilfredJDixon.1950.Analysisofextremevalues.TheAnnalsofMathematicalStatistics21,4(1950),488–506.
[61] AdamDziedzic,JohnPaparrizos,SanjayKrishnan,AaronElmore,andMichaelFranklin.2019.Band-limitedtrainingandinferenceforconvolutional
neuralnetworks.InICML.PMLR,1745–1754.
ManuscriptsubmittedtoACM

44 Paparrizosetal.
[62] JensEd’Hondt,OdysseasPapapetrou,andJohnPaparrizos.2024.BeyondtheDimensions:AStructuredEvaluationofMultivariateTimeSeries
DistanceMeasures.In2024IEEE40thInternationalConferenceonDataEngineeringWorkshops(ICDEW).IEEE,107–112.
[63] FrancisYsidroEdgeworth.1887.Xli.ondiscordantobservations.Thelondon,edinburgh,anddublinphilosophicalmagazineandjournalofscience23,
143(1887),364–375.
[64] JasonErnstandZivBar-Joseph.2006.STEM:atoolfortheanalysisofshorttimeseriesgeneexpressiondata.BMCbioinformatics7,1(2006),191.
[65] PhilippeEslingandCarlosAgon.2012.Time-seriesdatamining.ACMComputingSurveys(CSUR)45,1(2012),12.
[66] TomFawcett.2006.AnintroductiontoROCanalysis.PatternRecognitionLetters27,8(2006),861–874. https://doi.org/10.1016/j.patrec.2005.10.010
ROCAnalysisinPatternRecognition.
[67] PavelFilonov,AndreyLavrentyev,andArtemVorontsov.2016.Multivariateindustrialtimeserieswithcyber-attacksimulation:Faultdetection
usinganlstm-basedpredictivedatamodel.arXivpreprintarXiv:1612.06676(2016).
[68] RalphFoorthuis.2020.OntheNatureandTypesofAnomalies:AReview.arXivpreprintarXiv:2007.15634(2020).
[69] AnthonyJFox.1972.Outliersintimeseries.JournaloftheRoyalStatisticalSociety:SeriesB(Methodological)34,3(1972),350–363.
[70] AdaWai-CheeFu,OscarTat-WingLeung,EamonnJ.Keogh,andJessicaLin.2006.FindingTimeSeriesDiscordsBasedonHaarTransform.In
ADMA.
[71] YifengGao,JessicaLin,andConstantinBrif.2020.EnsembleGrammarInductionForDetectingAnomaliesinTimeSeries.InProceedingsofthe
InternationalConferenceonExtendingDatabaseTechnology(EDBT). https://doi.org/10.5441/002/edbt.2020.09
[72] GabrielGarcia,GabrielMichau,MélanieDucoffe,JayantSenGupta,andOlgaFink.2020.TimeSeriestoImages:MonitoringtheConditionof
IndustrialAssetswithDeepLearningImageProcessingAlgorithms.(052020).
[73] GabrielRodriguezGarcia,GabrielMichau,MélanieDucoffe,JayantSenGupta,andOlgaFink.2020.TimeSeriestoImages:MonitoringtheCondition
ofIndustrialAssetswithDeepLearningImageProcessingAlgorithms.arXiv:2005.07031[cs,eess,stat] http://arxiv.org/abs/2005.07031
[74] MartinGavrilov,DragomirAnguelov,PiotrIndyk,andRajeevMotwani.2000.Miningthestockmarket:Whichmeasureisbest.InProc.ofthe6th
ACMSIGKDD.487–496.
[75] SamGeorge.2019.IoTSignalsreport:IoT’spromisewillbeunlockedbyaddressingskillsshortage,complexityandsecurity. https://blogs.microsoft.
com/blog/2019/07/30/.
[76] JWLGlaisher.1873.Ontherejectionofdiscordantobservations.MonthlyNoticesoftheRoyalAstronomicalSociety33(1873),391–402.
[77] SteveGoddard,SherriKHarms,StephenEReichenbach,TsegayeTadesse,andWilliamJWaltman.2003.Geospatialdecisionsupportfordrought
riskmanagement.Commun.ACM46,1(2003),35–37.
[78] RahulGoel,SandeepSoni,NamanGoyal,JohnPaparrizos,HannaWallach,FernandoDiaz,andJacobEisenstein.2016.Thesocialdynamicsof
languagechangeinonlinenetworks.InSocialInformatics:8thInternationalConference,SocInfo2016,Bellevue,WA,USA,November11-14,2016,
Proceedings,PartI8.Springer,41–57.
[79] MarkusGoldsteinandAndreasDengel.2013.Histogram-basedOutlierScore(HBOS):AfastUnsupervisedAnomalyDetectionAlgorithm.
[80] MarkusGoldsteinandSeiichiUchida.2016.Acomparativeevaluationofunsupervisedanomalydetectionalgorithmsformultivariatedata.PloS
one11,4(2016),e0152173.
[81] VanessaGómez-Verdejo,JerónimoArenas-García,MiguelLazaro-Gredilla,andÁngelNavia-Vazquez.2011.Adaptiveone-classsupportvector
machine.IEEETransactionsonSignalProcessing59,6(2011),2975–2981.
[82] IanGoodfellow,JeanPouget-Abadie,MehdiMirza,BingXu,DavidWarde-Farley,SherjilOzair,AaronCourville,andYoshuaBengio.2014.Generative
adversarialnets.NeurIPS27(2014).
[83] BAGould.1855.OnPeirce’sCriterionfortheRejectionofDoubtfulObservations,withtablesforfacilitatingitsapplication.TheAstronomical
Journal4(1855),81–87.
[84] AdityaGrover,AshishKapoor,andEricHorvitz.2015.Adeephybridmodelforweatherforecasting.InProceedingsofthe21thACMSIGKDD
InternationalConferenceonKnowledgeDiscoveryandDataMining.ACM,379–386.
[85] FrankEGrubbs.1950.Samplecriteriafortestingoutlyingobservations.TheAnnalsofMathematicalStatistics(1950),27–58.
[86] ManishGupta,JingGao,CharuC.Aggarwal,andJiaweiHan.2014. OutlierDetectionforTemporalData:ASurvey. 26,9(2014),2250–2267.
https://doi.org/10.1109/TKDE.2013.184
[87] NicoGörnitz,MikioBraun,andMariusKloft.2015.HiddenMarkovAnomalyDetection.InProceedingsoftheInternationalConferenceonMachine
Learning(ICML)(ICML’15).JMLR.org,1833–1842. https://dl.acm.org/doi/10.5555/3045118.3045313
[88] MichaelHahslerandMatthewBolaos.2016.ClusteringDataStreamsBasedonSharedDensitybetweenMicro-Clusters.IEEETrans.onKnowl.and
DataEng.28,6(jun2016),1449–1461. https://doi.org/10.1109/TKDE.2016.2522412
[89] JohannaHardinandDavidMRocke.2004.Outlierdetectioninthemultipleclustersettingusingtheminimumcovariancedeterminantestimator.
ComputationalStatistics&DataAnalysis44,4(2004),625–638. https://doi.org/10.1016/S0167-9473(02)00280-3
[90] SahandHariri,MatiasCarrascoKind,andRobertJ.Brunner.2019.ExtendedIsolationForest.(2019). https://doi.org/10.1109/TKDE.2019.2947676
arXiv:1811.02141
[91] D.MHawkins.1980.IdentificationofOutliers.SpringerNetherlands,Dordrecht. OCLC:945065134.
[92] JeffHawkinsandRichardDawkins.2021.Athousandbrains:anewtheoryofintelligence.(2021).
[93] ZengyouHe,XiaofeiXu,andShengchunDeng.2003.Discoveringcluster-basedlocaloutliers.Patternrecognitionletters24,9-10(2003),1641–1650.
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 45
[94] M.A.Hearst,S.T.Dumais,E.Osuna,J.Platt,andB.Scholkopf.1998.Supportvectormachines.IEEEIntelligentSystemsandtheirApplications13,4
(July1998),18–28. https://doi.org/10.1109/5254.708428
[95] DonaldO.Hebb.1949.Theorganizationofbehavior:Aneuropsychologicaltheory.Wiley,NewYork.
[96] NiklasHeimandJamesE.Avery.2019. AdaptiveAnomalyDetectioninChaoticTimeSerieswithaSpatiallyAwareEchoStateNetwork.
arXiv:1909.01709[cs,stat] http://arxiv.org/abs/1909.01709
[97] Jordan Hochenbaum, Owen S. Vallis, and Arun Kejariwal. 2017. Automatic Anomaly Detection in the Cloud Via Statistical Learning.
arXiv:1704.07706[cs] http://arxiv.org/abs/1704.07706
[98] SeppHochreiterandJürgenSchmidhuber.1997.LongShort-TermMemory.NeuralComput.9,8(Nov.1997),1735–1780. https://doi.org/10.1162/
neco.1997.9.8.1735
[99] VictoriaJ.HodgeandJimAustin.2004.ASurveyofOutlierDetectionMethodologies.22,2(2004),85–126. https://doi.org/10.1007/s10462-004-4304-y
[100] OveHoegh-Guldberg,PeterJMumby,AnthonyJHooten,RobertSSteneck,PaulGreenfield,EdgardoGomez,CDrewHarvell,PeterFSale,
AlasdairJEdwards,KenCaldeira,etal.2007.Coralreefsunderrapidclimatechangeandoceanacidification.science318,5857(2007),1737–1742.
[101] RieHonda,ShuaiWang,TokioKikuchi,andOsamuKonishi.2002.Miningofmovingobjectsfromtime-seriesimagesanditsapplicationtosatellite
weatherimagery.JournalofIntelligentInformationSystems19,1(2002),79–93.
[102] PabloHuijse,PabloAEstevez,PavlosProtopapas,JoseCPrincipe,andPabloZegers.2014.Computationalintelligencechallengesandapplications
onlarge-scaleastronomicaltimeseriesdatabases.IEEEComputationalIntelligenceMagazine9,3(2014),27–39.
[103] KyleHundman,ValentinoConstantinou,ChristopherLaporte,IanColwell,andTomSoderstrom.2018.DetectingSpacecraftAnomaliesUsing
LSTMsandNonparametricDynamicThresholding.InSIGKDD.ACM,387–395. https://doi.org/10.1145/3219819.3219845
[104] KyleHundman,ValentinoConstantinou,ChristopherLaporte,IanColwell,andTomSoderstrom.2018.Detectingspacecraftanomaliesusinglstms
andnonparametricdynamicthresholding.InSIGKDD.387–395.
[105] MarkHung.2017.Leadingtheiot,gartnerinsightsonhowtoleadinaconnectedworld.GartnerResearch(2017),1–29.
[106] JOIrwin.1925.Onacriterionfortherejectionofoutlyingobservations.Biometrika(1925),238–250.
[107] AlanJulianIzenman.2008.Modernmultivariatestatisticaltechniques.Regression,classificationandmanifoldlearning10(2008),978–0.
[108] VincentJacob,FeiSong,ArnaudStiegler,BijanRad,YanleiDiao,andNesimeTatbul.2021.Exathlon:abenchmarkforexplainableanomalydetection
overtimeseries.PVLDB14,11(2021),2613–2626.
[109] HoyoungJeung,SofianeSarni,IoannisPaparrizos,SaketSathe,KarlAberer,NicholasDawes,ThanasisGPapaioannou,andMichaelLehning.
2010.Effectivemetadatamanagementinfederatedsensornetworks.In2010IEEEInternationalConferenceonSensorNetworks,Ubiquitous,and
TrustworthyComputing.IEEE,107–114.
[110] HaoJiang,ChunweiLiu,QiJin,JohnPaparrizos,andAaronJElmore.2020.Pids:attributedecompositionforimprovedcompressionandquery
performanceincolumnarstorage.Proc.VLDBEndow13,6(2020),925–938.
[111] HaoJiang,ChunweiLiu,JohnPaparrizos,AndrewAChien,JihongMa,andAaronJElmore.2021.GoodtotheLastBit:Data-DrivenEncoding
withCodecDB.InSIGMOD.843–856.
[112] KunioKashino,GavinSmith,andHiroshiMurase.1999.Time-seriesactivesearchforquickretrievalofaudioandvideo.In1999IEEEInternational
ConferenceonAcoustics,Speech,andSignalProcessing.Proceedings.ICASSP99(Cat.No.99CH36258),Vol.6.IEEE,2993–2996.
[113] E.Keogh,T.DuttaRoy,U.Naik,andAAgrawal.2021.Multi-datasetTime-SeriesAnomalyDetectionCompetition2021,https://compete.hexagon-
ml.com/practice/competition/39/.
[114] EamonnKeogh,JessicaLin,andAdaFu.2005.Hotsax:Efficientlyfindingthemostunusualtimeseriessubsequence.InFifthIEEEInternational
ConferenceonDataMining(ICDM’05).Ieee,8–pp.
[115] EamonnKeogh,StefanoLonardi,andBill’Yuan-chi’Chiu.2002.Findingsurprisingpatternsinatimeseriesdatabaseinlineartimeandspace.In
ProceedingsoftheeighthACMSIGKDDinternationalconferenceonKnowledgediscoveryanddatamining.550–556.
[116] EamonnKeogh,StefanoLonardi,ChotiratAnnRatanamahatana,LiWei,Sang-HeeLee,andJohnHandley.2007.Compression-baseddatamining
ofsequentialdata.DataMiningandKnowledgeDiscovery(2007).
[117] ChunggyeomKim,JinhyukLee,RaehyunKim,YoungbinPark,andJaewooKang.2018. DeepNAP:DeepNeuralAnomalyPre-Detectionina
SemiconductorFab.457-458(2018),1–11. https://doi.org/10.1016/j.ins.2018.05.020
[118] SiwonKim,KukjinChoi,Hyun-SooChoi,ByunghanLee,andSungrohYoon.2022.Towardsarigorousevaluationoftime-seriesanomalydetection.
InProceedingsoftheAAAIConferenceonArtificialIntelligence,Vol.36.7194–7201.
[119] SKnieling,JNiediek,EKutter,JBostroem,CEElger,andFMormann.2017. Anonlineadaptivescreeningprocedureforselectiveneuronal
responses.Journalofneurosciencemethods291(2017),36–42.
[120] MariaKontaki,AnastasiosGounaris,ApostolosNPapadopoulos,KostasTsichlas,andYannisManolopoulos.2011.Continuousmonitoringof
distance-basedoutliersoverdatastreams.In2011IEEE27thInternationalConferenceonDataEngineering.IEEE,135–146.
[121] PeterKrenskyandJimHare.2018.HypeCycleforDataScienceandMachineLearning,2018.GartnerCompany(2018).
[122] SanjayKrishnan,AaronJElmore,MichaelFranklin,JohnPaparrizos,ZechaoShang,AdamDziedzic,andRuiLiu.2019.Artificialintelligencein
resource-constrainedandsharedenvironments.ACMSIGOPSOperatingSystemsReview53,1(2019),1–6.
[123] Kwei-HerngLai,DaochenZha,JunjieXu,YueZhao,GuanchuWang,andXiaHu.2021.RevisitingTimeSeriesOutlierDetection:Definitionsand
Benchmarks.InNeurIPS.
ManuscriptsubmittedtoACM

46 Paparrizosetal.
[124] BouchraLamrini,AugustinGjini,SimonDaudin,PascalPratmarty,FrançoisArmando,andLouiseTravé-Massuyès.2018.AnomalyDetection
usingSimilarity-basedOne-ClassSVMforNetworkTrafficCharacterization..InDX.
[125] N.Laptev,S.Amizadeh,andY.Billawala.2015.S5-ALabeledAnomalyDetectionDataset,version1.0(16M). https://webscope.sandbox.yahoo.com/
catalog.php?datatype=s&did=70
[126] AlexanderLavinandSubutaiAhmad.2015.Evaluatingreal-timeanomalydetectionalgorithms–theNumentaanomalybenchmark.InICMLA.
IEEE,38–44.
[127] Ming-ChangLee,Jia-ChunLin,andErnstGunnarGran.2020. RePAD:Real-TimeProactiveAnomalyDetectionforTimeSeries.InAINA,
LeonardBarolli,FloraAmato,FrancescoMoscato,TomoyaEnokido,andMakotoTakizawa(Eds.).SpringerInternationalPublishing,1291–1302.
https://doi.org/10.1007/978-3-030-44041-1_110
[128] DanLi,DachengChen,JonathanGoh,andSee-KiongNg.2018.AnomalyDetectionwithGenerativeAdversarialNetworksforMultivariateTime
Series.CoRRabs/1809.04758(2018).arXiv:1809.04758 http://arxiv.org/abs/1809.04758
[129] DanLi,DachengChen,BaihongJin,LeiShi,JonathanGoh,andSee-KiongNg.2019.MAD-GAN:Multivariateanomalydetectionfortimeseries
datawithgenerativeadversarialnetworks.InInternationalconferenceonartificialneuralnetworks.Springer,703–716.
[130] ZeyanLi,WenxiaoChen,andDanPei.2018.RobustandUnsupervisedKPIAnomalyDetectionBasedonConditionalVariationalAutoencoder.In
ProceedingsoftheInternationalPerformanceComputingandCommunicationsConference(IPCCC).IEEE,1–9. https://doi.org/10.1109/PCCC.2018.
8710885
[131] ZhihuaLi,ZiyuanLi,NingYu,StevenWen,etal.2017.Locality-basedvisualoutlierdetectionalgorithmfortimeseries.SecurityandCommunication
Networks2017(2017).
[132] ZhiLi,HongMa,andYongbingMei.2007.AUnifyingMethodforOutlierandChangeDetectionfromDataStreamsBasedonLocalPolynomial
Fitting.InAdvancesinKnowledgeDiscoveryandDataMining,Zhi-HuaZhou,HangLi,andQiangYang(Eds.).SpringerBerlinHeidelberg,Berlin,
Heidelberg,150–161.
[133] ZhengLi,YueZhao,NicolaBotta,CezarIonescu,andXiyangHu.2020.COPOD:Copula-BasedOutlierDetection.InIEEEInternationalConference
onDataMining(ICDM).IEEE.
[134] MicheleLinardi,YanZhu,ThemisPalpanas,andEamonnKeogh.2018. MatrixProfileX:VALMOD-ScalableDiscoveryofVariable-Length
MotifsinDataSeries.InProceedingsoftheInternationalConferenceonManagementofData(SIGMOD)(2018).ACMPress,1053–1066. https:
//doi.org/10.1145/3183713.3183744
[135] MicheleLinardi,YanZhu,ThemisPalpanas,andEamonnKeogh.2020.MatrixprofilegoesMAD:variable-lengthmotifanddiscorddiscoveryin
dataseries.DataMiningandKnowledgeDiscovery34(2020),1022–1071.
[136] MicheleLinardi,YanZhu,ThemisPalpanas,andEamonnJ.Keogh.2020.MatrixProfileGoesMAD:Variable-LengthMotifAndDiscordDiscovery
inDataSeries.InDAMI.
[137] ChunweiLiu,HaoJiang,JohnPaparrizos,andAaronJElmore.2021.Decomposedboundedfloatsforfastcompressionandqueries.Proc.VLDB
Endow14,11(2021),2586–2598.
[138] ChunweiLiu,JohnPaparrizos,andAaronJElmore.2024.Adaedge:Adynamiccompressionselectionframeworkforresourceconstraineddevices.
In2024IEEE40thInternationalConferenceonDataEngineering(ICDE).IEEE,1506–1519.
[139] FeiTonyLiu,KaiMingTing,andZhi-HuaZhou.2008.IsolationForest.InProceedingsoftheInternationalConferenceonDataMining(ICDM).IEEE,
413–422. https://doi.org/10.1109/ICDM.2008.17
[140] FeiTonyLiu,KaiMingTing,andZhi-HuaZhou.2008.Isolationforest.InICDM.IEEE,413–422.
[141] QinghuaLiu,PaulBoniol,ThemisPalpanas,andJohnPaparrizos.2024.Time-SeriesAnomalyDetection:OverviewandNewTrends.PVLDB17,12
(2024),4229–4232.
[142] QinghuaLiuandJohnPaparrizos.2024.TheElephantintheRoom:TowardsAReliableTime-SeriesAnomalyDetectionBenchmark.InNeurIPS
2024.
[143] ShinanLiu,TarunMangla,TedShaowang,JinjinZhao,JohnPaparrizos,SanjayKrishnan,andNickFeamster.2023.Amir:Activemultimodal
interactionrecognitionfromvideoandnetworktrafficinconnectedenvironments.ProceedingsoftheACMonInteractive,Mobile,Wearableand
UbiquitousTechnologies7,1(2023),1–26.
[144] YubaoLiu,XiuweiChen,andFeiWang.2009.EfficientDetectionofDiscordsforTimeSeriesStream.AdvancesinDataandWebManagement
(2009),629–634. http://www.springerlink.com/index/n546h380446p95r7.pdf
[145] JorgeMLobo,AlbertoJiménez-Valverde,andRaimundoReal.2008.AUC:amisleadingmeasureoftheperformanceofpredictivedistribution
models.GlobalecologyandBiogeography17,2(2008),145–151.
[146] YueLu,RenjieWu,AbdullahMueen,MariaAZuluaga,andEamonnKeogh.2022.MatrixprofileXXIV:scalingtimeseriesanomalydetectionto
trillionsofdatapointsandultra-fastarrivingdatastreams.InSIGKDD.1173–1182.
[147] WeiLuoandMarcusGallagher.2011.FasterandParameter-FreeDiscordSearchinQuasi-PeriodicTimeSeries.InAdvancesinKnowledgeDiscovery
andDataMining,JoshuaZhexueHuang,LongbingCao,andJaideepSrivastava(Eds.).
[148] HelmutLütkepohl,MarkusKrätzig,andPeterCBPhillips.2004.Appliedtimeserieseconometrics.Cambridgeuniversitypress.
[149] JunshuiMaandSimonPerkins.2003.OnlineNoveltyDetectiononTemporalSequences.InProceedingsoftheInternationalConferenceonKnowledge
DiscoveryandDataMining(SIGKDD).ACMPress,613. https://doi.org/10.1145/956750.956828
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 47
[150] JunshuiMaandSimonPerkins.2003.Time-seriesnoveltydetectionusingone-classsupportvectormachines.InProceedingsoftheInternational
JointConferenceonNeuralNetworks,2003.,Vol.3.IEEE,1741–1745.
[151] MohammadSaeidMahdavinejad,MohammadrezaRezvan,MohammadaminBarekatain,PeymanAdibi,PayamBarnaghi,andAmitPSheth.2017.
MachinelearningforInternetofThingsdataanalysis:Asurvey.DigitalCommunicationsandNetworks(2017).
[152] PankajMalhotra,AnushaRamakrishnan,GaurangiAnand,LovekeshVig,PuneetAgarwal,andGautamShroff.2016.LSTM-BasedEncoder-Decoder
forMulti-SensorAnomalyDetection.arXiv:1607.00148[cs,stat] http://arxiv.org/abs/1607.00148
[153] PankajMalhotra,LovekeshVig,GautamShroff,andPuneetAgarwal.2015.LongShortTermMemoryNetworksforAnomalyDetectioninTime
Series.InProceedingsoftheEuropeanSymposiumonArtificialNeuralNetworks,ComputationalIntelligenceandMachineLearning(ESANN),Vol.23.
http://www.elen.ucl.ac.be/Proceedings/esann/esannpdf/es2015-56.pdf
[154] PankajMalhotra,LovekeshVig,GautamShroff,PuneetAgarwal,etal.2015.LongShortTermMemoryNetworksforAnomalyDetectioninTime
Series..InEsann,Vol.2015.89.
[155] RosarioNMantegna.1999.Hierarchicalstructureinfinancialmarkets.TheEuropeanPhysicalJournalB-CondensedMatterandComplexSystems11,
1(1999),193–197.
[156] CarlaMarceau.2000.CharacterizingtheBehaviorofaProgramUsingMultiple-LengthN-Grams.InProceedingsoftheWorkshoponNewSecurity
Paradigms(NSPW).ACMPress,101–110. https://doi.org/10.1145/366173.366197
[157] Pierre-François Marteau, Saeid Soheily-Khah, and Nicolas Béchet. 2017. Hybrid Isolation Forest - Application to Intrusion Detection.
arXiv:1705.03800[cs] http://arxiv.org/abs/1705.03800
[158] FranciscoMartínez-Álvarez,AliciaTroncoso,GualbertoAsencio-Cortés,andJoséRiquelme.2015.Asurveyondataminingtechniquesappliedto
electricity-relatedtimeseriesforecasting.Energies8,11(2015),13162–13193.
[159] RobertLMasonandJohnCYoung.2002.Multivariatestatisticalprocesscontrolwithindustrialapplications.SIAM.
[160] RichardMcCleary,RichardAHay,ErrollEMeidinger,andDavidMcDowall.1980. Appliedtimeseriesanalysisforthesocialsciences. Sage
PublicationsBeverlyHills,CA.
[161] KathyMcKeown,HalDaumeIII,SnigdhaChaturvedi,JohnPaparrizos,KapilThadani,PabloBarrio,OrBiran,SuvarnaBothe,MichaelCollins,
KennethRFleischmann,etal.2016.Predictingtheimpactofscientificconceptsusingfull-textfeatures.JournaloftheAssociationforInformation
ScienceandTechnology67,11(2016),2684–2696.
[162] KatsiarynaMirylenka,VassilisChristophides,ThemisPalpanas,IoannisPefkianakis,andMartinMay.2016.Characterizinghomedeviceusage
fromwirelesstraffictimeseries.
[163] MaziarMoradiFard,ThibautThonet,andEricGaussier.2020.Deepk-Means:Jointlyclusteringwithk-Meansandlearningrepresentations.Pattern
RecognitionLetters138(2020),185–192. https://doi.org/10.1016/j.patrec.2020.07.028
[164] AMorales-Esteban,FranciscoMartínez-Álvarez,ATroncoso,JLJusto,andCristinaRubio-Escudero.2010.Patternrecognitiontoforecastseismic
timeseries.ExpertSystemswithApplications37,12(2010),8333–8342.
[165] CristinaMorariuandTheodorBorangiu.2018.Timeseriesforecastingfordynamicschedulingofmanufacturingprocesses.In2018IEEEInternational
ConferenceonAutomation,QualityandTesting,Robotics(AQTR).1–6. https://doi.org/10.1109/AQTR.2018.8402748
[166] AbdullahMueen,YanZhu,MichaelYeh,KavehKamgar,KrishnamurthyViswanathan,ChetanGupta,andEamonnKeogh.2017. TheFastest
SimilaritySearchAlgorithmforTimeSeriesSubsequencesunderEuclideanDistance.
[167] MohsinMunir,ShoaibAhmedSiddiqui,AndreasDengel,andSherazAhmed.2019. DeepAnT:ADeepLearningApproachforUnsupervised
AnomalyDetectioninTimeSeries.7(2019),1991–2005. https://doi.org/10.1109/ACCESS.2018.2886457
[168] GyoungSNa,DonghyunKim,andHwanjoYu.2018.Dilof:Effectiveandmemoryefficientlocaloutlierdetectionindatastreams.InSIGKDD.
1993–2002.
[169] TakaakiNakamura,MakotoImamura,RyanMercer,andEamonnJ.Keogh.2020.MERLIN:Parameter-FreeDiscoveryofArbitraryLengthAnomalies
inMassiveTimeSeriesArchives.InICDM,ClaudiaPlant,HaixunWang,AlfredoCuzzocrea,CarloZaniolo,andXindongWu(Eds.).IEEE,1190–1195.
https://doi.org/10.1109/ICDM50108.2020.00147
[170] TakaakiNakamura,RyanMercer,MakotoImamura,andEamonnKeogh.2023.MERLIN++:parameter-freediscoveryoftimeseriesanomalies.
DataMiningandKnowledgeDiscovery37,2(2023),670–709. https://doi.org/10.1007/s10618-022-00876-7
[171] ZijianNiu,KeYu,andXiaofeiWu.2020.LSTM-basedVAE-GANfortime-seriesanomalydetection.Sensors20,13(2020),3738.
[172] OliverObst,X.RosalindWang,andMikhailProkopenko.2008.UsingEchoStateNetworksforAnomalyDetectioninUndergroundCoalMines.In
ProceedingsoftheInternationalConferenceonInformationProcessinginSensorNetworks(IPSN).IEEE,219–229. https://doi.org/10.1109/IPSN.2008.35
[173] AlbertoOgbechie,JavierDíaz-Rozo,PedroLarrañaga,andConchaBielza.2017. DynamicBayesianNetwork-BasedAnomalyDetectionfor
In-ProcessVisualInspectionofLaserSurfaceHeatTreatment.InProceedingsoftheInternationalConferenceonMachineLearningforCyberPhysical
Systems(ML4CPS),JürgenBeyerer,OliverNiggemann,andChristianKühnert(Eds.).SpringerBerlinHeidelberg,17–24. https://doi.org/10.1007/978-
3-662-53806-7_3
[174] RandyPaffenroth,KathleenKay,andLesServi.2018. RobustPCAforAnomalyDetectioninCyberNetworks. arXiv:1801.01571[cs] http:
//arxiv.org/abs/1801.01571
[175] ESPage.1957.Onproblemsinwhichachangeinaparameteroccursatanunknownpoint.Biometrika44,1/2(1957),248–252.
[176] ThemisPalpanas.2015.DataSeriesManagement:TheRoadtoBigSequenceAnalytics.SIGMODRec.44,2(2015),47–52.
ManuscriptsubmittedtoACM

48 Paparrizosetal.
[177] GirishKeshavPalshikar.2005. Distance-basedoutliersinsequences.InDistributedComputingandInternetTechnology:SecondInternational
Conference,ICDCIT2005,Bhubaneswar,India,December22-24,2005.Proceedings2.Springer,547–552.
[178] SpirosPapadimitriou,HiroyukiKitagawa,PhillipBGibbons,andChristosFaloutsos.2003.Loci:Fastoutlierdetectionusingthelocalcorrelation
integral.InICDE.IEEE,315–326.
[179] IoannisPaparrizos.2018.Fast,Scalable,andAccurateAlgorithmsforTime-SeriesAnalysis.Ph.D.Dissertation.ColumbiaUniversity.
[180] JohnPaparrizos,PaulBoniol,ThemisPalpanas,RueySTsay,AaronElmore,andMichaelJFranklin.2022.Volumeunderthesurface:anewaccuracy
evaluationmeasurefortime-seriesanomalydetection.PVLDB15,11(2022),2774–2787.
[181] JohnPaparrizos,IkraduyaEdian,ChunweiLiu,AaronJElmore,andMichaelJFranklin.2022.Fastadaptivesimilaritysearchthroughvariance-aware
quantization.InICDE.IEEE,2969–2983.
[182] JohnPaparrizosandMichaelJFranklin.2019.GRAIL:efficienttime-seriesrepresentationlearning.ProceedingsoftheVLDBEndowment12,11
(2019),1762–1777.
[183] JohnPaparrizosandLuisGravano.2016.k-Shape:EfficientandAccurateClusteringofTimeSeries.SIGMOD45,1(June2016),69–76. https:
//doi.org/10.1145/2949741.2949758
[184] JohnPaparrizosandLuisGravano.2017.FastandAccurateTime-SeriesClustering.ACMTransactionsonDatabaseSystems(TODS)42,2(2017),8.
[185] JohnPaparrizos,YuhaoKang,PaulBoniol,RueySTsay,ThemisPalpanas,andMichaelJFranklin.2022.TSB-UAD:anend-to-endbenchmarksuite
forunivariatetime-seriesanomalydetection.PVLDB15,8(2022),1697–1711.
[186] JohnPaparrizos,ChunweiLiu,BrunoBarbarioli,JohnnyHwang,IkraduyaEdian,AaronJElmore,MichaelJFranklin,andSanjayKrishnan.2021.
VergeDB:ADatabaseforIoTAnalyticsonEdgeDevices..InCIDR.
[187] JohnPaparrizos,ChunweiLiu,AaronElmore,andMichaelJ.Franklin.2023.QueryingTime-SeriesData:AComprehensiveComparisonofDistance
Measures.IEEEDataEngineeringBulletin(DEB2023)47(2023),69–88.
[188] JohnPaparrizos,ChunweiLiu,AaronJElmore,andMichaelJFranklin.2020.Debunkingfourlong-standingmisconceptionsoftime-seriesdistance
measures.InSIGMOD.1887–1905.
[189] JohnPaparrizosandSaiPrasannaTejaReddy.2023.Odyssey:Anengineenablingthetime-seriesclusteringjourney.ProceedingsoftheVLDB
Endowment16,12(2023),4066–4069.
[190] JohnPaparrizos,RyenWWhite,andEricHorvitz.2016.Detectingdevastatingdiseasesinsearchlogs.InSIGKDD.559–568.
[191] JohnPaparrizos,RyenWWhite,andEricHorvitz.2016.Screeningforpancreaticadenocarcinomausingsignalsfromwebsearchlogs:Feasibility
studyandresults.Journalofoncologypractice12,8(2016),737–744.
[192] JohnPaparrizos,KaizeWu,AaronElmore,ChristosFaloutsos,andMichaelJFranklin.2023.Acceleratingsimilaritysearchforelasticmeasures:A
studyandnewgeneralizationoflowerboundingdistances.ProceedingsoftheVLDBEndowment16,8(2023),2019–2032.
[193] DaehyungPark,ZackoryErickson,TapomayukhBhattacharjee,andCharlesC.Kemp.2016. MultimodalExecutionMonitoringforAnomaly
DetectionduringRobotManipulation.InProceedingsoftheInternationalConferenceonRoboticsandAutomation(ICRA).IEEE,407–414. https:
//doi.org/10.1109/ICRA.2016.7487160
[194] DaehyungPark,YuunaHoshi,andCharlesC.Kemp.2018.AMultimodalAnomalyDetectorforRobot-AssistedFeedingUsinganLSTM-Based
VariationalAutoencoder.3,3(2018),1544–1551. https://doi.org/10.1109/LRA.2018.2801475
[195] StephenPauwelsandToonCalders.2019. AnAnomalyDetectionTechniqueforBusinessProcessesBasedonExtendedDynamicBayesian
Networks.InProceedingsoftheACM/SIGAPPSymposiumonAppliedComputing(SAC).ACM,494–501. https://doi.org/10.1145/3297280.3297326
[196] StephenPauwelsandToonCalders.2019.DetectingAnomaliesinHybridBusinessProcessLogs.19,2(2019),18–30. https://doi.org/10.1145/
3357385.3357387
[197] ERWINSPearsonandCChandraSekar.1936.Theefficiencyofstatisticaltoolsandacriterionfortherejectionofoutlyingobservations.Biometrika
28,3/4(1936),308–320.
[198] BenjaminPeirce.1852.Criterionfortherejectionofdoubtfulobservations.TheAstronomicalJournal2(1852),161–163.
[199] C-KPeng,ShlomoHavlin,HEugeneStanley,andAryLGoldberger.1995. Quantificationofscalingexponentsandcrossoverphenomenain
nonstationaryheartbeattimeseries.Chaos:AnInterdisciplinaryJournalofNonlinearScience5,1(1995),82–87.
[200] DragoljubPokrajac,AleksandarLazarevic,andLonginJanLatecki.2007. Incrementallocaloutlierdetectionfordatastreams.In2007IEEE
symposiumoncomputationalintelligenceanddatamining.IEEE,504–515.
[201] XiangfeiQiu,JilinHu,LekuiZhou,XingjianWu,JunyangDu,BuangZhang,ChenjuanGuo,AoyingZhou,ChristianS.Jensen,ZhenliSheng,
andBinYang.2024.TFB:TowardsComprehensiveandFairBenchmarkingofTimeSeriesForecastingMethods.Proc.VLDBEndow.17,9(2024),
2363–2377.
[202] SridharRamaswamy,RajeevRastogi,andKyuseokShim.2000.EfficientAlgorithmsforMiningOutliersfromLargeDataSets.SIGMODRec.29,2
(may2000),427–438. https://doi.org/10.1145/335191.335437
[203] UsmanRaza,AlessandroCamerra,AmyLMurphy,ThemisPalpanas,andGianPietroPicco.2015.Practicaldatapredictionforreal-worldwireless
sensornetworks.IEEETransactionsonKnowledgeandDataEngineering27,8(2015),2231–2244.
[204] HanshengRen,BixiongXu,YujingWang,ChaoYi,CongruiHuang,XiaoyuKou,TonyXing,MaoYang,JieTong,andQiZhang.2019.Time-series
anomalydetectionserviceatmicrosoft.InProceedingsofthe25thACMSIGKDDinternationalconferenceonknowledgediscovery&datamining.
3009–3017.
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 49
[205] DaniloJimenezRezende,ShakirMohamed,andDaanWierstra.2014.StochasticBackpropagationandApproximateInferenceinDeepGenerative
Models.InProceedingsofthe31stInternationalConferenceonICML-Volume32(Beijing,China)(ICML’14).JMLR.org,II–1278–II–1286.
[206] JoshuaSRichmanandJRandallMoorman.2000.Physiologicaltime-seriesanalysisusingapproximateentropyandsampleentropy.American
JournalofPhysiology-HeartandCirculatoryPhysiology278,6(2000),H2039–H2049.
[207] KexinRong,ClaraEYoon,KarianneJBergen,HashemElezabi,PeterBailis,PhilipLevis,andGregoryCBeroza.2018.Locality-sensitivehashing
forearthquakedetection:Acasestudyofscalingdata-drivenscience.ProceedingsoftheVLDBEndowment11,11(2018),1674–1687.
[208] VolkerRoth.2006.KernelFisherDiscriminantsforOutlierDetection.18,4(2006),942–960. https://doi.org/10.1162/neco.2006.18.4.942
[209] PeterRousseeuw.1984.LeastMedianofSquaresRegression.JournalofTheAmericanStatisticalAssociation-JAMERSTATISTASSN79(121984),
871–880. https://doi.org/10.1080/01621459.1984.10477105
[210] PeterJ.RousseeuwandKatrienVanDriessen.1999.AFastAlgorithmfortheMinimumCovarianceDeterminantEstimator.Technometrics41,3
(1999),212–223. https://doi.org/10.1080/00401706.1999.10485670arXiv:https://www.tandfonline.com/doi/pdf/10.1080/00401706.1999.10485670
[211] PeterJ.RousseeuwandAnnickM.Leroy.1987.Robustregressionandoutlierdetection.Wiley,NewYork.
[212] PeterJRousseeuwandAnnickMLeroy.2005.Robustregressionandoutlierdetection.Vol.589.Johnwiley&sons.
[213] EduardoJRuiz,VagelisHristidis,CarlosCastillo,AristidesGionis,andAlejandroJaimes.2012.Correlatingfinancialtimeserieswithmicro-blogging
activity.InProceedingsofthefifthACMinternationalconferenceonWebsearchanddatamining.ACM,513–522.
[214] StanSalvadorandPhilipChan.2005. LearningStatesandRulesforDetectingAnomaliesinTimeSeries. 23,3(2005),241–255. https:
//doi.org/10.1007/s10489-005-4610-3
[215] JörgSander,MartinEster,Hans-PeterKriegel,andXiaoweiXu.1998.Density-BasedClusteringinSpatialDatabases:TheAlgorithmGDBSCAN
andItsApplications.DataMiningandKnowledgeDiscovery2,2(01Jun1998),169–194. https://doi.org/10.1023/A:1009745219419
[216] SebastianSchmidl,PhillipWenig,andThorstenPapenbrock.2022.AnomalyDetectioninTimeSeries:AComprehensiveEvaluation.PVLDB15,9
(may2022),1779–1797. https://doi.org/10.14778/3538598.3538602
[217] JohannesSchneider,PhillipWenig,andThorstenPapenbrock.2021.DistributedDetectionofSequentialAnomaliesinUnivariateTimeSeries.The
VLDBJournal30,4(mar2021),579–602. https://doi.org/10.1007/s00778-021-00657-6
[218] BernhardSchölkopf,RobertCWilliamson,AlexSmola,JohnShawe-Taylor,andJohnPlatt.1999.Supportvectormethodfornoveltydetection.
NeurIPS12(1999).
[219] PavelSenin,JessicaLin,XingWang,TimOates,SunilGandhi,ArnoldP.Boedihardjo,CrystalChen,andSusanFrankenstein.2015.Timeseries
anomalydiscoverywithgrammar-basedcompression.InEDBT.
[220] PavelSenin,JessicaLin,XingWang,TimOates,SunilGandhi,ArnoldP.Boedihardjo,CrystalChen,andSusanFrankenstein.2015.TimeSeries
AnomalyDiscoverywithGrammar-BasedCompression.,481–492pages. https://doi.org/10.5441/002/edbt.2015.42
[221] DennisShasha.1999.Tuningtimeseriesqueriesinfinance:Casestudiesandrecommendations.IEEEDataEng.Bull.22,2(1999),40–46.
[222] LifengShen,ZhuocongLi,andJamesKwok.2020.Timeseriesanomalydetectionusingtemporalhierarchicalone-classnetwork.NeurIPS33(2020),
13016–13026.
[223] S-C.ChenK.SarinnapakornShyu,M-L.andLW.Chang.2003.ANovelAnomalyDetectionSchemeBasedonPrincipalComponentClassifier.
(2003).
[224] AlbanSiffer,Pierre-AlainFouque,AlexandreTermier,andChristineLargouet.2017.Anomalydetectioninstreamswithextremevaluetheory.In
Proceedingsofthe23rdACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining.1067–1075.
[225] DavidEugeneSmith.2012.Asourcebookinmathematics.CourierCorporation.
[226] RalphD.SnyderandStephenJ.Withers.1983.Exponentialsmoothingwithfinitesamplecorrection.Number1983,1inWorkingpaper.Department
ofEconometricsandOperationsResearch.MonashUniversity.Dept.,Univ,Clayton.
[227] MaximilianSoelch,JustinBayer,MarvinLudersdorfer,andPatrickvanderSmagt.2016.VariationalInferenceforOn-LineAnomalyDetectionin
High-DimensionalTimeSeries.arXiv:1602.07109[cs,stat] http://arxiv.org/abs/1602.07109
[228] HongchaoSong,ZhuqingJiang,AidongMen,andBoYang.2017.AHybridSemi-SupervisedAnomalyDetectionModelforHigh-Dimensional
Data.ComputationalIntelligenceandNeuroscience2017(15Nov2017),8501683. https://doi.org/10.1155/2017/8501683
[229] SondreSørbøandMassimilianoRuocco.2023.NavigatingtheMetricMaze:ATaxonomyofEvaluationMetricsforAnomalyDetectioninTime
Series.arXivpreprintarXiv:2303.01272(2023).
[230] EJStone.1873.Ontherejectionofdiscordantobservations.MonthlyNoticesoftheRoyalAstronomicalSociety34(1873),9.
[231] YaSu,YoujianZhao,ChenhaoNiu,RongLiu,WeiSun,andDanPei.2019. RobustAnomalyDetectionforMultivariateTimeSeriesthrough
StochasticRecurrentNeuralNetwork.InSIGKDD.ACM,2828–2837. https://doi.org/10.1145/3292500.3330672
[232] YaSu,YoujianZhao,ChenhaoNiu,RongLiu,WeiSun,andDanPei.2019.Robustanomalydetectionformultivariatetimeseriesthroughstochastic
recurrentneuralnetwork.InSIGKDD.2828–2837.
[233] S.Subramaniam,T.Palpanas,D.Papadopoulos,V.Kalogeraki,andD.Gunopulos.2006. OnlineOutlierDetectioninSensorDataUsingNon-
ParametricModels.InProceedingsoftheInternationalConferenceonVeryLargeDatabases(VLDB)(VLDB’06).VLDBEndowment,187–198.
https://dl.acm.org/doi/10.5555/1182635.1164145
[234] PeiSun,SanjayChawla,andBavaniArunasalam.2006.MiningforOutliersinSequentialDatabases.InProceedingsoftheInternationalConference
onDataMining(ICDM).SocietyforIndustrialandAppliedMathematics,94–105. https://doi.org/10.1137/1.9781611972764.9
ManuscriptsubmittedtoACM

50 Paparrizosetal.
[235] EmmanouilSylligardos,PaulBoniol,JohnPaparrizos,PanosE.Trahanias,andThemisPalpanas.2023.ChooseWisely:AnExtensiveEvaluationof
ModelSelectionforAnomalyDetectioninTimeSeries.Proc.VLDBEndow.16,11(2023),3418–3432. https://doi.org/10.14778/3611479.3611536
[236] JianTang,ZhixiangChen,AdaWai-CheeFu,andDavidWCheung.2002.Enhancingeffectivenessofoutlierdetectionsforlowdensitypatterns.In
PAKDD.535–548.
[237] NesimeTatbul,TaeJunLee,StanZdonik,MejbahAlam,andJustinGottschlich.2018.Precisionandrecallfortimeseries.InNeurIPS.1924–1934.
[238] DavidMJTaxandRobertPWDuin.2004.Supportvectordatadescription.Machinelearning54,1(2004),45–66.
[239] RueySTsay.1988.Outliers,levelshifts,andvariancechangesintimeseries.Journalofforecasting7,1(1988),1–20.
[240] RueySTsay.2014.FinancialTimeSeries.WileyStatsRef:StatisticsReferenceOnline(2014),1–23.
[241] RueySTsay,DanielPena,andAlanEPankratz.2000.Outliersinmultivariatetimeseries.Biometrika87,4(2000),789–804.
[242] JohnWTukeyetal.1977.Exploratorydataanalysis.Vol.2.Reading,Mass.
[243] KuniakiUeharaandMitsuomiShimada.2002.Extractionofprimitivemotionanddiscoveryofassociationrulesfromhumanmotiondata.In
ProgressinDiscoveryScience.Springer,338–348.
[244] RafaelG.Vieira,MarcosA.LeoneFilho,andRobinsonSemolini.2018.AnEnhancedSeasonal-HybridESDTechniqueforRobustAnomalyDetection
onTimeSeries.InSimpósioBrasileirodeRedesdeComputadores(SBRC),Vol.36.
[245] GabrielWachman,RoniKhardon,PavlosProtopapas,andCharlesRAlcock.2009.Kernelsforperiodictimeseriesarisinginastronomy.InJoint
EuropeanConferenceonMachineLearningandKnowledgeDiscoveryinDatabases.Springer,489–505.
[246] YiWang,LinshengHan,WeiLiu,ShujiaYang,andYanboGao.2019. StudyonWaveletNeuralNetworkBasedAnomalyDetectioninOcean
ObservingDataSeries.186(2019),106129. https://doi.org/10.1016/j.oceaneng.2019.106129
[247] PeterJWebster,GregJHolland,JudithACurry,andH-RChang.2005.Changesintropicalcyclonenumber,duration,andintensityinawarming
environment.Science309,5742(2005),1844–1846.
[248] BillyMWilliamsandLesterAHoel.2003.ModelingandforecastingvehiculartrafficflowasaseasonalARIMAprocess:Theoreticalbasisand
empiricalresults.Journaloftransportationengineering129,6(2003),664–672.
[249] JiaWu,WeiruZeng,andFeiYan.2018.HierarchicalTemporalMemoryMethodforTime-Series-BasedAnomalyDetection.273(2018),535–546.
https://doi.org/10.1016/j.neucom.2017.08.026
[250] P.Wu,J.Liu,andF.Shen.2020.ADeepOne-ClassNeuralNetworkforAnomalousEventDetectioninComplexScenes.IEEETransactionson
NeuralNetworksandLearningSystems31,7(2020),2609–2622. https://doi.org/10.1109/TNNLS.2019.2933554
[251] RenjieWuandEamonnJ.Keogh.2023.CurrentTimeSeriesAnomalyDetectionBenchmarksareFlawedandareCreatingtheIllusionofProgress.
IEEETrans.Knowl.DataEng.35,3(2023),2421–2429. https://doi.org/10.1109/TKDE.2021.3112126
[252] WentaiWu,LigangHe,WeiweiLin,YiSu,YuhuaCui,CarstenMaple,andStephenJarvis.2020.DevelopinganUnsupervisedReal-TimeAnomaly
DetectionSchemeforTimeSerieswithMulti-Seasonality.arXiv:1908.01146[cs,eess,stat] http://arxiv.org/abs/1908.01146
[253] YanshanXiao,BoLiu,LongbingCao,XindongWu,ChengqiZhang,ZhifengHao,FengzhaoYang,andJieCao.2009.Multi-spheresupportvector
datadescriptionforoutliersdetectiononmulti-distributiondata.In2009IEEEinternationalconferenceondataminingworkshops.IEEE,82–87.
[254] HaowenXu,WenxiaoChen,NengwenZhao,ZeyanLi,JiahaoBu,ZhihanLi,YingLiu,YoujianZhao,DanPei,YangFeng,etal.2018.Unsupervised
AnomalyDetectionviaVariationalAuto-EncoderforSeasonalKPIsinWebApplications.InProceedingsoftheInternationalConferenceonWorld
WideWeb(WWW).InternationalWorldWideWebConferencesSteeringCommittee,InternationalWorldWideWebConferencesSteering
Committee,187–196. https://doi.org/10.1145/3178876.3185996
[255] HaowenXu,WenxiaoChen,NengwenZhao,ZeyanLi,JiahaoBu,ZhihanLi,YingLiu,YoujianZhao,DanPei,YangFeng,etal.2018.Unsupervised
anomalydetectionviavariationalauto-encoderforseasonalkpisinwebapplications.InProceedingsofthe2018worldwidewebconference.187–196.
[256] KenjiYamanishi,Jun-ichiTakeuchi,GrahamWilliams,andPeterMilne.2004.On-LineUnsupervisedOutlierDetectionUsingFiniteMixtureswith
DiscountingLearningAlgorithms.8,3(2004),275–300. https://doi.org/10.1023/B:DAMI.0000023676.72185.7c
[257] Chao-LungYangandWei-JuLiao.2017.AdjacentMeanDifference(AMD)methodfordynamicsegmentationintimeseriesanomalydetection.In
2017IEEE/SICEInternationalSymposiumonSystemIntegration(SII).IEEE,241–246.
[258] DragomirYankov,EamonnKeogh,andUmaaRebbapragada.2008.Diskawarediscorddiscovery:Findingunusualtimeseriesinterabytesized
datasets.KnowledgeandInformationSystems17(2008),241–262.
[259] DragomirYankov,EamonnJ.Keogh,andUmaaRebbapragada.2007.DiskAwareDiscordDiscovery:FindingUnusualTimeSeriesinTerabyte
SizedDatasets.InICDM.
[260] YuanYao,AbhishekSharma,LeanaGolubchik,andRameshGovindan.2010.OnlineAnomalyDetectionforSensorSystems:ASimpleandEfficient
Approach.Perform.Eval.67,11(nov2010),1059–1075. https://doi.org/10.1016/j.peva.2010.08.018
[261] C.-C.M.Yeh,Y.Zhu,L.Ulanova,N.Begum,Y.Ding,H.A.Dau,D.F.Silva,A.Mueen,andE.J.Keogh.2016.MatrixProfileI:AllPairsSimilarityJoins
forTimeSeries:AUnifyingViewThatIncludesMotifs,DiscordsandShapelets.InICDM.
[262] Chin-ChiaMichaelYeh,YanZhu,LiudmilaUlanova,NurjahanBegum,YifeiDing,HoangAnhDau,DiegoFurtadoSilva,AbdullahMueen,and
EamonnKeogh.2016.MatrixProfileI:AllPairsSimilarityJoinsforTimeSeries:AUnifyingViewThatIncludesMotifs,DiscordsandShapelets.In
ProceedingsoftheInternationalConferenceonDataMining(ICDM).1317–1322. https://doi.org/10.1109/ICDM.2016.0179
[263] YufengYu,YuelongZhu,ShijinLi,andDingshengWan.2014.TimeSeriesOutlierDetectionBasedonSlidingWindowPrediction.2014(2014),
1–14. https://doi.org/10.1155/2014/879736
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 51
[264] ChunkaiZhang,ShaocongLi,HongyeZhang,andYingyangChen.2020.VELC:ANewVariationalAutoEncoderBasedModelforTimeSeries
AnomalyDetection.arXiv:1907.01702[cs,stat] http://arxiv.org/abs/1907.01702
[265] ChuxuZhang,DongjinSong,YuncongChen,XinyangFeng,CristianLumezanu,WeiCheng,JingchaoNi,BoZong,HaifengChen,andNiteshV.
Chawla.2019.ADeepNeuralNetworkforUnsupervisedAnomalyDetectionandDiagnosisinMultivariateTimeSeriesData.InAAAI,Vol.33.
1409–1416. https://doi.org/10.1609/aaai.v33i01.33011409
[266] RuiZhang,ShaoyanZhang,SethuramanMuthuraman,andJianminJiang.2007.OneClassSupportVectorMachineforAnomalyDetectioninthe
CommunicationNetworkPerformanceData.InProceedingsoftheConferenceonAppliedElectromagnetics,WirelessandOpticalCommunications
(ELECTROSCIENCE)(ELECTROSCIENCE’07).WorldScientificandEngineeringAcademyandSociety(WSEAS),31–37.
[267] HangZhao,YujingWang,JuanyongDuan,CongruiHuang,DefuCao,YunhaiTong,BixiongXu,JingBai,JieTong,andQiZhang.2020.Multivariate
time-seriesanomalydetectionviagraphattentionnetwork.InICDM.IEEE,841–850.
[268] YanZhu,Chin-ChiaMichaelYeh,ZacharyZimmerman,KavehKamgar,andEamonnKeogh.2018.MatrixprofileXI:SCRIMP++:timeseriesmotif
discoveryatinteractivespeeds.In2018IEEEInternationalConferenceonDataMining(ICDM).IEEE,837–846.
[269] YanZhu,ZacharyZimmerman,NaderShakibaySenobari,Chin-ChiaMichaelYeh,GarethFunning,AbdullahMueen,PhilipBrisk,andEamonn
Keogh.2016.Matrixprofileii:Exploitinganovelalgorithmandgpustobreaktheonehundredmillionbarrierfortimeseriesmotifsandjoins.In
2016IEEE16thinternationalconferenceondatamining(ICDM).IEEE,739–748.
[270] YanZhu,ZacharyZimmerman,NaderShakibaySenobari,Chin-ChiaMichaelYeh,GarethFunning,AbdullahMueen,PhilipBrisk,andEamonn
Keogh.2016.Matrixprofileii:Exploitinganovelalgorithmandgpustobreaktheonehundredmillionbarrierfortimeseriesmotifsandjoins.In
2016IEEE16thinternationalconferenceondatamining(ICDM).IEEE,739–748.
[271] ZacharyZimmerman,KavehKamgar,NaderShakibaySenobari,BrianCrites,GarethFunning,PhilipBrisk,andEamonnKeogh.2019.Matrix
profileXIV:scalingtimeseriesmotifdiscoverywithGPUstobreakaquintillionpairwisecomparisonsadayandbeyond.InProceedingsofthe
ACMSymposiumonCloudComputing.74–86.
[272] ZacharyZimmerman,NaderShakibaySenobari,GarethFunning,EvangelosPapalexakis,SametOymak,PhilipBrisk,andEamonnKeogh.2019.
MatrixprofileXVIII:timeseriesmininginthefaceoffastmovingstreamsusingalearnedapproximatematrixprofile.In2019IEEEInternational
ConferenceonDataMining(ICDM).IEEE,936–945.
ManuscriptsubmittedtoACM