Generative Adversarial Networks in Time Series:
A Systematic Literature Review
EOINBROPHY,DublinCityUniversity
ZHENGWEIWANG,TrinityCollegeDublin
QISHE,ByteDanceAILab
TOMÁSWARD,DublinCityUniversity
Generativeadversarialnetwork(GAN)studieshavegrownexponentiallyinthepastfewyears.Theirimpact
hasbeenseenmainlyinthecomputervisionfieldwithrealisticimageandvideomanipulation,especially
generation,makingsignificantadvancements.Althoughthesecomputervisionadvanceshavegarneredmuch 199
attention,GANapplicationshavediversifiedacrossdisciplinessuchastimeseriesandsequencegeneration.
AsarelativelynewnicheforGANs,fieldworkisongoingtodevelophigh-quality,diverse,andprivatetime
seriesdata.Inthisarticle,wereviewGANvariantsdesignedfortimeseriesrelatedapplications.Weproposea
classificationofdiscrete-variantGANsandcontinuous-variantGANs,inwhichGANsdealwithdiscretetime
seriesandcontinuoustimeseriesdata.Hereweshowcasethelatestandmostpopularliteratureinthisfield—
theirarchitectures,results,andapplications.Wealsoprovidealistofthemostpopularevaluationmetrics
andtheirsuitabilityacrossapplications.AlsopresentedisadiscussionofprivacymeasuresfortheseGANs
andfurtherprotectionsanddirectionsfordealingwithsensitivedata.Weaimtoframeclearlyandconcisely
thelatestandstate-of-the-artresearchinthisareaandtheirapplicationstoreal-worldtechnologies.
CCSConcepts:•Computingmethodologies→Machinelearningapproaches;
Additional Key Words and Phrases: Generative adversarial networks, time series, discrete-variant GANs,
continuous-variantGANs
ACMReferenceformat:
Eoin Brophy, Zhengwei Wang, Qi She, and Tomás Ward. 2023. Generative Adversarial Networks in Time
Series:ASystematicLiteratureReview.ACMComput.Surv.55,10,Article199(February2023),31pages.
https://doi.org/10.1145/3559540
1 INTRODUCTION
Thisreviewarticleisdesignedforthoseinterestedingenerativeadversarialnetworks(GANs)
appliedtotimeseriesdatageneration.Weprovideareviewofcurrentstate-of-the-artandnovel
time series GANs and their solutions to real-world problems with time series data. GANs have
ThisworkwasfundedbyScienceFoundationIrelandundergrantnumbers17/RC-PhD/3482andSFI/12/RC/2289_P2.
Authors’addresses:E.Brophy(correspondingauthor),InfantResearchCentre&SchoolofComputing,DublinCityUni-
versity,Dublin,Ireland;email:eoin.brophy7@mail.dcu.ie;Z.Wang,V-SENSE,SchoolofComputerScienceandStatistics,
TrinityCollegeDublin,Dublin,Ireland;email:villa.wang.zhengwei@gmail.com;Q.She,ByteDanceAILab,China;email:
1477430657@qq.com;T.Ward,InsightSFIResearchCentreforDataAnalytics,DublinCityUniversity,Dublin,Ireland;
email:tomas.ward@dcu.ie.
This work is licensed under a Creative Commons Attribution International 4.0 License.
©2023Copyrightheldbytheowner/author(s).
0360-0300/2023/02-ART199
https://doi.org/10.1145/3559540
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

199:2 E.Brophyetal.
beengainingalotoftractionwithinthedeeplearningresearchcommunitysincetheirinception
in2014[38].Theirabilitytogenerateandmanipulatehigh-qualitydataacrossmultipledomains
hascontributedtotheirsuccess.ThemainfocusofGANstodatehasbeeninthecomputervision
domain;however,theyhavealsobeensuccessfullyappliedtoothers,suchasnaturallanguage
processing(NLP)andnowtimeseries.
AGANisagenerativemodelconsistingofageneratoranddiscriminator,typicallytwoneural
network (NN) models. In recent years GANs have demonstrated their ability to produce high-
quality image and video generation, style transfer, and image completion. They have also been
successfully used for audio generation, sequence forecasting, and imputation, with a movement
towardusingGANsfortimeseriesandsequentialdatagenerationandforecasting.
Wedefineatimeseriesasasequenceofvectorsdependentontime(t)andcanberepresented
asxt =x1,...,xnforcontinuous/realtimeanddiscretetime.Thetimeseries’valuescaneitherbe
definedascontinuousordiscreteand,dependingonthenumberofvaluesrecorded,areunivariate
ormultivariate.Inmostcases,thetimeserieswilltakeeitheranintegervalueorarealvalue.As
Dorffner[25]states,atimeseriescanbeviewed,fromapracticalperspective,asavaluesampledat
discretestepsintime.Thistimestepcanbeaslongasyearstoasshortasmilliseconds,forexample.
We define a continuous time series as a signal sampled from a continuous process—that is, the
function’sdomainisfromanuncountableset.Incontrast,adiscretetimeserieshasacountable
domain.
TheapplicabilityofGANstotimeseriesdatacansolvemanyissuesthatcurrentdatasetholders
facethatcannotorhavenotbeenaddressedbyothermachinelearningorregressivetechniques.
Data shortage is often an issue that many practitioners face, and GANs can augment smaller
datasets by generating new, previously unseen data. Data can be missing or corrupted in cases;
GANscanimputedata,suchasreplacetheartifactswithinformationrepresentativeofcleandata.
GANsarealsocapableofdenoisingsignalsinthecaseofcorrupteddata.Dataprotection,privacy,
and sharing have become heavily regulated with the introduction of data protection measures;
GANs can ensure an extra layer of data protection by generating differentially private datasets
containingnoriskoflinkagefromsourcetogenerateddatasets.
Timeseriesdatagenerationisnotanovelconceptinthatithaslongrootsseededinregression.
Furthermore,itinitiallybeganasforecastingoftimestepsratherthanwholesequencegeneration.
One of the most used time series forecasting methods was autoregressive (AR) models. Aside
fromforecastingdatapoints,ARmodelsfocusonpreservingthetemporaldynamicsofasequence.
However,theyareinherentlydeterministicinthatnorandomnessisinvolvedinthecalculationof
futurestatesofthesystem.ThismeansthatARmodelsarenotgenuinelygenerativeorprobabilis-
tic.ForanARmodel,thegoalistoproducethenexttimestep(x )inasequenceasafunctionof
t+1
thepreviousntimesteps,wherenistheorderofthemodel.TheformulaforaclassicARmodelis
giveninEquation(1).
x t+1 =c+θ 1 x t +θ 2 x t−1 +ϵ (1)
Here,x isthevalueofthesequenceattimet,θ isthemodelparameters,c isaconstant,andϵ is
t
theerrortermusuallychosenasnormallydistributednoise.
Autoregression was a step shy of time series synthesis. That ultimately came in the form of
directedgenerativenetworks.Whenusingthetermdirected,wemeanamodelwheretheedgesare
directedandthusindicateswhichvariable’sprobabilitydistributionisdefinedintermsofanother.
Inotherwords,thisisastructuredprobabilisticmodelwithconditionalprobabilitydistributions.
Thesedata-drivengenerativemodelsofferedresearcherstheoptionofgeneratingfull-lengthdata
sequencesversusforecastingsingularvaluesinthecaseoftheregressivemodels.Italsorequired
little domain knowledge of the time series signal morphology, which was often a necessity for
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

GenerativeAdversarialNetworksinTimeSeries:ASystematicLiteratureReview 199:3
Fig.1. AEmodel.
otherstatisticalmodelingtechniques.Thispropelledgenerativemodelingforwardinthemachine
learningcommunityfordatasynthesistechniques.
Several generative methods have been used in the past to generate synthetic data. One such
methodistheautoencoder(AE),whichisdesignedtoefficientlylearnaninformativerepresen-
tationofaninputinasmalldimensionalspaceandreconstructtheencodeddatabacksuchthat
thereconstructedinputissimilaraspossibletotheoriginalone.TheAEmodelismadeofanen-
coderanddecoderNN,asshowninFigure1.However,othergenerativemodelshaveemergedas
front-runnersduetothequalityofthegenerateddataandinherentprivacyprotectionmeasures.
Generativemodelscomeinmanyshapes,fromvariationalautoencoders(VAEs)andrecur-
rentneuralnetwork(RNN)variantstoGANs,allofwhichhavetheirprosandcons.Forexam-
ple,VAEsuselearnedapproximateinferencetoproducesyntheticsamplesefficiently.Aninference
problemissimplyusingthevalueofsomevariablesorprobabilitydistributionstopredictother
valuesorprobabilitydistributions.Approximateinferenceiswhenweseektoapproximateatrue
distribution,sayp(y|x),byseekinganapproximatedistributionq(y|x).However,thisnetworkap-
proximationconductedbyVAEsmeansthattheirgenerateddataqualitycanbedegradedcompared
to samples generated by GANs. However, for all of the benefits that come with GANs, they are
notwithouttheirowndownsides.Theyareaveryusefultechnologythatallowsustoreproduce
amazinglyinsightfulandpowerfuldatasets,butonlyifwecanaddresstheirfollowingchallenges.
OneofthesignificantchallengesofGANsliesintheirinherentinstability,whichmakesthem
difficulttotrain.GANmodelssufferfromissuessuchasnon-convergence,diminishing/vanishing
gradients,andmodecollapse.Anon-convergingmodeldoesnotstabilizeandcontinuouslyoscil-
lates,causingittodiverge.Diminishinggradientspreventthegeneratorfromlearninganything,
asthediscriminatorbecomestoosuccessful.Modecollapseiswhenthegeneratorcollapses,pro-
ducingonlyuniformsampleswithlittletonovariety.
The second challenge of GANs lies in its evaluation process. With image-based GANs, re-
searchers have reached a loose consensus [8] surrounding the evaluation of the generated dis-
tributionestimatedfromthetrainingdatadistribution.UnfortunatelyfortimeseriesGANs,due
tothecomparativelylownumbersofpaperspublished,therehasnotbeenanagreementreached
onthegenerateddata’sevaluationmetrics.Therehavebeendifferentapproachesputforward,but
noneestablishedasafront-runnerinthemetricsspaceasofyet.
In this review, we present the first complete review and categorization of time series GANs,
namelydiscreteandcontinuousvariants,theirapplications,architecture,lossfunctionsandhow
theyhaveimprovedontheirpredecessorsintermsofvarietyandqualityoftheirgenerateddata.
We also contribute by including experiments for the majority of time series GAN architectures
appliedtotimeseriessynthesis.
2 RELATEDWORK
Therehasbeenahandfulofhigh-qualityGANreviewpaperspublishedinthepastfewyears.For
example,Wangetal.[100]takeataxonomicapproachtoGANsincomputervision.Theauthors
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

199:4 E.Brophyetal.
split GANs into architecture variants and loss variants. Although they include applications of
GANsandmentiontheirapplicabilitytosequentialdatageneration,theworkisheavilyfocused
on media manipulation and generation. Gui et al. [40] break down GANs into their constituent
parts. They begin by discussing the algorithms and architecture of various GANs and their
evaluationmetrics,thenlisttheirsurroundingtheoryandproblemssuchasmodecollapse,among
others.Finally,theydiscusstheapplicationsofGANsandprovideaverybriefaccountofGANs
usedforsequentialdata.GonogandZhou[36]provideashortintroductiontoGANs,theirtheory,
and explore the variety of plausible models, again listing their applications in image and video
manipulationwithamentionofsequentialdata(NLP).Inanotherreview,Alqahtanietal.[3]give
an overview of GAN fundamentals, variants, and applications. Sequential data applications are
mentionedintheformofmusicandspeechsynthesis.
As with most review papers, Yinka-Banjo and Ugot [106] give an introduction and overview
ofGANs.However,theyalsoreviewGANsasadversarialdetectorsanddiscusstheirlimitations
applied to cybersecurity. Yi et al. [105] give a review of GANs and their applications in medical
imaging,andexplainhowtheycanbeusedinclinicalresearchandpotentiallydeployedtohelp
practicingclinicians.Thereisnomentionoftimeseriesdatausecases.
A recurring theme in these works focuseson GAN variants that have mostly been applied to
thecomputervisiondomain.Tothebestofourknowledge,noreviewpaperhasbeenconducted
withthemainfocusontimeseriesGANs.Althoughthesereviewshavementionedtheapplication
oftheseGANsingeneratingsequentialdata,theyhavescratchedthesurfaceofwhatisbecoming
agrowingbodyofresearch.
Wecontributetolesseningthisgapbypresentingourwork,whichseekstoprovidethelatest
up-to-dateresearcharoundtimeseriesGANs,theirarchitecture,lossfunctions,evaluationmetrics,
trade-offs,andapproachestoprivacypreservationoftheirdatasets.
3 GENERATIVEADVERSARIALNETWORKS
3.1 Background
The introduction of GANs facilitated a significant breakthrough in the generation of synthetic
data. These deep learning models typically consist of two NNs: a generator and a discriminator.
ThegeneratorGtakesinrandomnoisez ∈Rr andattemptsgeneratessyntheticdatathatissimilar
tothetrainingdatadistribution.ThediscriminatorDattemptstodetermineifthegenerateddata
isrealorfake.Thegeneratoraimstomaximizethefailurerateofthediscriminator,whereasthe
discriminatoraimstominimizeit.Figure2showsasimpleexampleoftheGANarchitectureand
thegamethattheNNmodelsplay.Thetwonetworksarelockedinatwo-playerminimaxgame
definedbythevaluefunctionV(G,D)(2),whereD(x)istheprobabilitythatx comesfromthereal
dataratherthanthegenerateddata[38].
m
G
inm
D
axV(G,D)=E x∼pdata(x) [loдD(x)]+E z∼pz(z) [loд(1−D(G(z)))] (2)
GANsbelongtothefamilyofgenerativemodelsandareanalternativemethodofgenerating
syntheticdatathatdonotrequiredomainexpertise.TheywereconceivedintheworkbyGood-
fellowetal.[38]in2014,whereamulti-layerperceptronwasusedforboththediscriminatorand
thegenerator.In2015,Radfordetal.[85]subsequentlydevelopedthedeepconvolutionalgen-
erative adversarial network (DCGAN) to generate synthetic images. Since then, researchers
havecontinuouslyimprovedontheearlyGANarchitectures,lossfunctions,andevaluationmet-
rics while innovating on their potential contributions to real-world applications. To appreciate
whytherehasbeensuchconcertedactivityinthefurtherdevelopmentofGANtechnologies,itis
importanttounderstandthelimitationsofearlyarchitecturesandthechallengesthesepresented.
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

GenerativeAdversarialNetworksinTimeSeries:ASystematicLiteratureReview 199:5
Fig.2. Generativeadversarialnetwork.
Wedescribethesenext,andinsodoing,wepreparethereaderfortheparticularmanifestationof
thesechallengesinthemorespecificcontextoftimeseries.
3.2 Challenges
TherearethreemainchallengesintheareaoftimeseriesGANs:trainingstability,evaluation,and
privacy risk associatedwith synthetic data created by GANs. We explain these three challenges
next.
Training stability. The original GAN work has already proved the global optimality and the
convergence of GANs during training [38]. However, it still highlights the instability problem
that can arise when training a GAN. Two problems are well studied in the literature: vanishing
gradients and mode collapse. The vanishing gradient is caused by directly optimizing the loss
presentedinEquation(2).WhenD reachestheoptimality,optimizingEquation(2)forG canbe
convertedtominimizingtheJensen-Shannon(JS)divergence(detailsofthederivationcanbefound
inSection5oftheworkofWangetal. [100])betweentherealdatadistribution(p )andthe
data
generator’sdistribution(p ):
д
L =2·JS(p (cid:5)p )−2·log2. (3)
G data д
L staysconstant(loд2=0.693)whenthereisnooverlapbetweenp andp ,whichindicates
G data д
thatthegradientforG usingthislossisnear0inthissituation.Anon-zerogradientforG only
existswhenp andp havesubstantialoverlap.Inpractice,thepossibilitythatp andp are
data д data д
not intersected or have negligible overlap is quite high [4]. To get rid of the vanishing gradient
problemforG,theoriginalGANwork[38]highlightstheminimizationof
L G =−E x∼pд log[D(x)] (4)
for updating G. This strategy is able to avoid the vanishing gradient problem but leads to the
modecollapseissue.OptimizingEquation(4)canbeconvertedtooptimizingthereverseKullback-
Leibler (KL) divergence—that is,KL(p ||p ) (details can be found in the work of Wang et al.
д data
[100]). When p contains multiple modes, p chooses to recover a single mode and ignores
data д
othermodeswhenoptimizingthereverseKLdivergence.Consideringthiscase,G trainedusing
Equation (4) might be only able to generate few modes from real data. These problems can be
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

199:6 E.Brophyetal.
amendedbychangingthearchitectureorthelossfunction,whicharereviewedbyWangetal.[100]
indetail.
Evaluation. Awiderangeofevaluationmetricshasbeenproposedtoevaluatetheperformance
ofGANs[9,10,98,99]. CurrentevaluationsofGANs incomputervisionarenormally designed
to consider two perspectives: quality and quantity of generated data. The most representative
qualitative metric is to use human annotation to determine the visual quality of the generated
images. Quantitative metrics compare statistical properties between generated and real images:
two-sampletestssuchasmaximummeandiscrepancy(MMD)[93],inceptionscore(IS)[88],and
Fréchetinceptiondistance(FID)[51].Contrarytoevaluatingimage-basedGANs,itisdifficultto
evaluatetimeseriesdatafromhumanpsycho-perceptualsensequalitatively.Intermsofqualita-
tivelyevaluatingtimeseriesbasedGANs,itnormallyconductst-SNE[95]andPCA[13]analyses
tovisualizehowwellthegenerateddistributionsresembletheoriginaldistributions[107].Quan-
titativeevaluationfortimeseriesbasedGANscanbedonebydeployingtwo-sampletestssimilar
toimage-basedGANs.
Privacyrisk. ApartfromevaluatingtheperformanceofGANs,awiderangeofmethodshave
been used to assess the privacy risk associated with synthetic data created by GANs. Choi et al.
[17]performedtestsforpresencedisclosureandattributedisclosure.Incontrast,othersutilizeda
three-sampletestonthetraining,test,andsyntheticdatatoidentifyifthesyntheticdatahasover-
fittedtothetrainingdata[17,31].Ithasbeenshownthatcommonmethodsofde-identifyingdata
donotpreventattackersfromre-identifyingindividualsusingadditionaldata[29,72].Sensitive
data is usually de-identified by removing personally identifiable information. However, work is
ongoingtocreateframeworkstolinkdifferentsourcesofpubliclyavailableinformationtogether
usingalternativeinformationtopersonallyidentifiableinformation.MalinandSweeney[72]de-
velopedasoftwareprogram,REID,toconnectindividualscontainedinpubliclyavailablehospital
discharge data with their unique DNA records. Culnane et al. [19] re-identified individuals in a
de-identified open dataset of Australian medical billing records using unencrypted parts of the
records and known information about individuals from other sources. Hejblum et al. [50] devel-
opedaprobabilisticmethodtolinkde-identifiedelectronichealthrecord(EHR)dataofpatients
with rheumatoid arthritis. The re-identification of individuals in publicly available datasets can
leadtotheexposureoftheirsensitivehealthinformation.Healthdatahasbeencategorizedasspe-
cialpersonaldatabyGeneralDataProtectionRegulation(GDPR)andissubjecttoahigherlevel
ofprotectionundertheDataProtectionActof2018(Section36(2))[32].Consequently,concerned
researchersmustfindalternativemethodsofprotectingsensitivehealthdatatominimizetherisk
ofre-identification.ThiswillbeaddressedinSection7.
3.3 PopularDatasets
Unlikeimage-baseddatasets(CIFAR,MNIST,ImageNet[22,61,64]),therearenostandardizedor
commonlyusedbenchmarkingdatasetsfortimeseriesgeneration.However,wehavecompileda
listofsomeofthemorepopulardatasetsimplementedinthereviewedworks,andtheyarelistedin
Table1alongwiththeiryearofrelease/update,datatype,andhowmanyinstancesandattributes
theycontain.Whatmakesthesedatasetsinteresting/applicabletotimeseriesGANsisthatthey
aresignalsmadeupofhighlycomplexwaveforms(physiologicalandaudio)andcontainimportant
temporaldynamicscrucialtopreservewhengeneratingnewsamples.Furthermore,thesesignals
aretheexactdatatypethatarehighlyregulatedandcanstandtobenefitfrombeingleveragedby
GANstogeneratefurthervolumesofthiskindofdata.
There exist two repositories; the UCR Time Series Classification/Clustering database [20]
and the UCI Machine Learning Repository [26] that make available several time series datasets.
Despitethis,thereremainsnoconsensusonastandardizeddatasetusedforbenchmarkingtime
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

GenerativeAdversarialNetworksinTimeSeries:ASystematicLiteratureReview 199:7
Table1. PopularDatasetsUsedintheReviewedWorks
| Name(Year) | DataType | Instances | Attributes |
| ---------- | -------- | --------- | ---------- |
Oxford-ManInstitute“realizedlibrary”(updated Realmultivariate >2,689,487 5
| daily) | timeseries |     |     |
| ------ | ---------- | --- | --- |
EEGMotorMovement/ImageryDataset(2004) Realmultivariate 1,500 64
timeseries
| ECG200(2001) | Realunivariatetime | 200 | 1   |
| ------------ | ------------------ | --- | --- |
series
EpilepticSeizureRecognitionDataset(2001) Realmultivariate 11,500 179
timeseries
| TwoLeadECG(2015) | Realmultivariate | 1,162 | 2   |
| ---------------- | ---------------- | ----- | --- |
timeseries
| MIMIC-III(2016) | Real,integer,and | –   | –   |
| --------------- | ---------------- | --- | --- |
categorical
multivariatetime
series
| EPILEPSIAEprojectdatabase(2012) | Realmultivariate | 30  | –   |
| ------------------------------- | ---------------- | --- | --- |
timeseries
| PhysioNet/CinC(2015) | Realmultivariate | 750 | 4   |
| -------------------- | ---------------- | --- | --- |
timeseries
| WristPPGDuringExercise(2017) | Realmultivariate | 19  | 14  |
| ---------------------------- | ---------------- | --- | --- |
timeseries
| MIT-BIHArrhythmiaDatabase(2001) | Realmultivariate | 201 | 2   |
| ------------------------------- | ---------------- | --- | --- |
timeseries
| PhysioNet/CinC(2012) | Real,integer,and | 12,000 | 43  |
| -------------------- | ---------------- | ------ | --- |
categorical
multivariatetime
series
| KDDCupDataset(2018) | Real,integer,and | 282 | 3   |
| ------------------- | ---------------- | --- | --- |
categorical
multivariatetime
series
| PeMSDatabase(updateddaily) | Integerand | –   | 8   |
| -------------------------- | ---------- | --- | --- |
categorical
multivariatetime
series
| NottinghamMusicDatabase(2003) | Specialtextformat | 1,000 | –   |
| ----------------------------- | ----------------- | ----- | --- |
timeseries
seriesGANs,whichmaybeduetothe“continuous”natureofthearchitecturedimensions.GANs
designedforcontinuoustimeseriesgenerationoftendifferinthelengthoftheirinputsequence
duetoeitherauthorpreferenceortheconstraintsplacedontheirarchitectureforthegenerated
data’sdownstreamtasks.
4 CLASSIFICATIONOFTIMESERIESBASEDGANS
WeproposeacategorizationofthefollowingtimeseriesbasedGANsbasedontwodistinctvari-
anttypes:discretevariants(discretetimeseries)andcontinuousvariants(continuoustimeseries).A
discretetimeseriesconsistsofdatapointsseparatedbytimeintervals.Thistypeofdatamighthave
adata-reportingintervalthatisinfrequent(e.g.,1pointperminute)orirregular(e.g.,whenevera
userlogsin),andgapswherevaluesaremissingduetoreportinginterruptions(e.g.,intermittent
serverornetworkdowntimeinanetworktrafficapplication).Discretetimeseriesgenerationin-
volves generating sequences that may have a temporal dependency but contain discrete tokens;
thesecanbecommonlyfoundinEHRs(InternationalClassificationofDiseases9codes)andtext
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

199:8 E.Brophyetal.
Fig.3. Exampleplotsofdiscrete(left)andcontinuoustimeseries(right).
generation. A continuous time series has a data value corresponding to every moment in time.
Continuousdatagenerationisconcernedwithgeneratingareal-valuedsignalxwithtemporalde-
pendencieswherex∈R.Figure3presentsexamplesofdiscreteandcontinuoustimeseriessignals.
Challengeswithdiscretetimeseriesgeneration.GANsstrugglewithdiscretedatagenerationdue
tothezerogradientnearlyeverywhere—thatis,thedistributionondiscreteobjectsarenotdifferen-
tiablewithrespecttotheirparameters[52,108].Thislimitationmakesthegeneratoruntrainable
using backpropagation alone. The generator starts with a random sampling and a deterministic
transform guided via the gradient of the loss from the discriminator with respect to the output
produced byG and the training dataset. This loss leads to a slight change inG’s output, push-
ing it closer to the desired output. Making slight changes to continuous numbers makes sense;
adding 0.001to a value of 10 in financial time seriesdata will bring it to 10.001.However, a dis-
cretetokensuchastheword“penguin”cannotsimplyundergotheadditionof0.001,asthesum
“penguin+0.001”makesnosense.Whatisimportanthereistheimpossibilityforthegeneratorto
jumpfromonediscretetokentothenextbecausethesmallchangegivesthetokenanewvalue
thatdoesnotcorrespondtoanyothertokenoverthatlimiteddiscretespace[37].Thisisbecause
thereexistszeroprobabilityinthespacebetweenthesetokens,unlikewithcontinuousdata.
Challenges with continuous time series generation. Modeling continuous time series data
presentsadifferentproblemforGANs,whichareinherentlydesignedtomodelcontinuousdata,
albeitmostcommonlyintheformofimages.Thetemporalnatureofcontinuousdataintimese-
riespresentsanextralayerofdifficulty.Complexcorrelationsexistbetweenthetemporalfeatures
andtheirattributes—forexample,ifusingmultichannelbiometric/physiologicaldata,theelectro-
cardiogram (ECG) characteristics will depend on the individual’s age and/or health. In addition,
long-termcorrelationsexistinthedata,whicharenotnecessarilyfixedindimensioncomparedto
image-baseddataunderafixeddimension.Transformingimagedimensionsmayleadtoadegra-
dationinimagequality,butitisarecognizedpractice.Thisoperationbecomesmoredifficultwith
continuoustimeseriesdata,asthereisnostandardizeddimensionusedacrosstimeseriesGAN
architectures,whichmeansthatbenchmarkingtheirperformancesbecomesdifficult.
Sincetheirinceptionin2014,GANshaveshowngreatsuccessingeneratinghigh-qualitysyn-
theticimagesindistinguishablefromrealimages[41,65,87].Althoughthefocustodatehasbeen
ondevelopingGANsforimprovedmediageneration,thereisagrowingconsensusthatGANscan
beusedformorethanimagegenerationandmanipulation,whichhasledtoamovementtoward
generatingtimeseriesdatawithGANs.
RNNs(Figure4,left),duetotheirloop-likestructure,areperfectforsequentialdataapplications
butbythemselveslacktheabilitytolearnlong-termdependenciesthatmightbecrucialinfore-
castingfuturevaluesbasedonthepast.Longshort-termmemory(LSTM)networks(Figure4,
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

GenerativeAdversarialNetworksinTimeSeries:ASystematicLiteratureReview 199:9
Fig.4. BlockdiagramofastandardRNN(left)andanLSTMcell(right).
right)areaspecifickindofRNNthathavetheabilitytorememberinformationforlongperiods
of time and, in turn, learn these long-term dependencies that the standard RNN is not capable
ofdoing.Inmostworkreviewedinthisarticle,themajorityoftheRNN-basedarchitecturesare
utilizingtheLSTMcell.
RNNscanmodelsequentialdatasuchasfinancialdata,medicaldata,text,andspeech,andthey
havebeenthefoundationalarchitecturefortimeseriesGANs.Arecurrentgenerativeadversar-
ialnetwork(RGAN)wasfirstproposedin2016.Thegeneratorcontainedarecurrentfeedback
loopthatusedboththeinputandhiddenstatesateachtimesteptogeneratethefinaloutput[54].
RGANs often utilize LSTM NNs in their generative models to avoid the vanishing gradient
problemassociatedwithmoretraditionalrecurrentnetworks[53].Inthesectionthatfollows,we
present time series GANs that have either contributed significantly to this space or have made
someofthemostrecentnoveladvancementsinaddressingthechallengesmentionedpreviously.
4.1 Discrete-VariantGANs
4.1.1 Sequence GAN (SeqGAN) (Sept. 2016). Yu et al. [108] proposed a sequential data gener-
ationframework[108]thatcouldaddresstheissueswithgeneratingdiscretedataasmentioned
previouslyinSection4.Thisapproachoutperformedpreviousmethodsforgenerativemodeling
onreal-worldtasks,includingamaximumlikelihoodestimation(MLE)-trainedLSTM,scheduled
sampling[6],andpolicygradientwithbilingualevaluationunderstudy(PG-BLEU)[79].SeqGAN’s
generative model comprises RNNs with LSTM cells, and its discriminative model is a convolu-
tionalneuralnetwork(CNN).Givenadatasetofstructuredsequences,theauthorstrainG to
produceasyntheticsequenceY = (y ...,y ...,y ),y ∈ Y whereY isdefinedasthevocab-
1:T 1 t T t
ulary of candidate tokens.G is updated by a policy gradient and Monte Carlo (MC) search on
the expected reward from D (Figure 5). The authors used two datasets for their experiments. A
Chinesepoemdataset[62]andaBarackObamaSpeechdataset[102]withAdamoptimizersand
abatchsizeof64.Theirexperimentsareavailableonline.1
Although the purpose of SeqGAN is to generate discrete sequential data, it opened the door
to other GANs in generating continuous sequential and time series data. The authors use a
synthetic dataset whose distribution is generated from a randomly initialized LSTM following
a normal distribution. They also compare the generated data to real-world examples of poems,
1SeqGANGitHub:https://github.com/LantaoYu/SeqGAN/.
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

199:10 E.Brophyetal.
Fig.5. SeqGAN:Distrainedoverrealandgenerateddata(left),whereasGistrainedbypolicygradient
wherethefinalrewardsignalisprovidedbyDandispassedbacktotheintermediateactionvalueviaMC
search(right).
Fig.6. Dilatedcausalconvolutionallayer.
speech-language, and music. SeqGAN showed competitive performance in generating the
sequencesandcontributedheavilytowardthefurtherdevelopmentofthecontinuoussequential
GANs.
4.1.2 Quant GAN (July 2019). Quant GAN is a data-driven model that aims to capture long-
range dependencies in financial time series data such as volatility clusters. Both the generator
anddiscriminatorusetemporalconvolutionalnetworks(TCNs)withskipconnections[101],
which are essentially dilated causal convolutional networks. They have the advantage of being
suitedtomodellong-rangedependenciesincontinuoussequentialdata.Thegeneratorfunctionis
anovelstochasticvolatilityneuralnetworkthatconsistsofavolatilityanddriftTCN.Temporal
blocks are the modules used in the TCN that consist of two dilated causal convolutions layers
(Figure6)andtwoparametricrectifiedlinearunits(PReLU)asactivationfunctions.Datagenerated
byGispassedtoDtoproduceoutputs,whichcanthenbeaveragedtogiveanMCestimateofD’s
lossfunction.TheauthorsusedadatasetofdailyspotpricesoftheS&P500fromMay2009until
December2018.
The authors aim to capture long-range dependencies in financial time series; however, mod-
eling the series in continuous time over these long time frames would blow up the models’
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

GenerativeAdversarialNetworksinTimeSeries:ASystematicLiteratureReview 199:11
Fig.7. StructureofC-RNN-GAN’sgeneratoranddiscriminator.
computational complexity. Therefore, this method models the time series in discrete time. The
authors report that this approach is capable of outperforming more conventional models from
mathematical finance (constrained stochastic volatility NN and generalized AR conditional
heteroskedasticity (GARCH) [7]) but state that there remain issues that need to be resolved for
thisapproachtobecomewidelyadopted.Onesuchissueconcernstheneedforaunifiedmetric
forquantifyingtheperformanceoftheseGANs,whichisapointwediscussfurtherinSection6.
4.2 Continuous-VariantGANs
TrainingStabilityDevelopments
4.2.1 ContinuousRNN-GAN(C-RNN-GAN)(Nov.2016). Inpreviousworks,RNNshavebeenap-
pliedtomodelingmusicbuthavegenerallyusedasymbolicrepresentationtomodelthistypeof
sequentialdata.Mogren[74]proposedtheC-RNN-GAN(Figure7),oneofthefirstexamplesofus-
ingGANstogeneratecontinuoussequentialdata.ThegeneratorisanRNN,andthediscriminatora
bidirectionalRNN,whichallowsthediscriminatortotakethesequencecontextinbothdirections.
TheRNNsusedinthisworkweretwostackedLSTMlayers,witheachcellcontaining350hidden
units.ThelossfunctionscanbeseeninEquations(5)and(6),wherez(i) isasequenceofuniform
randomvectorsin[0,1]k,andx(i) isasequencefromthetrainingdata.k isthedimensionalityof
thedataintherandomsequence.
(cid:2)m
1
L = loд(1−D(G(z(i)))) (5)
G
m
i=1
(cid:2)m
1
L = [−loдD(x(i))−loд(1−D(G(z(i))))] (6)
D
m
i=1
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

199:12 E.Brophyetal.
TheC-RNN-GANistrainedwithbackpropagationthroughtime(BPTT)andmini-batchstochas-
ticgradientdescentwithL2regularizationontheweightsofbothG andD.Freezingwasapplied
to bothG and D when one network becomes too strong relative to the other. The dataset used
was3,697midifilesfrom160differentcomposersofclassicalmusicwithabatchsizeof20.Adam
andgradientdescentoptimizerswereusedduringtraining;fullimplementationdetailsareavail-
ableonline.2 Overall,theC-RNN-GANwascapableoflearningthecharacteristicsofcontinuous
sequentialdataand,inturn,generatemusic.However,theauthorstatedthattheirapproachstill
needswork,particularlyinrigorousevaluationofthegenerateddataquality.
4.2.2 NoiseReductionGAN(NR-GAN)(Oct.2019). NR-GANisdesignedfornoisereductionin
continuous time series signals but more specifically has been implemented for noise reduction
inmiceelectroencephalogram(EEG)signals[90].ThisdatasetwasprovidedbytheInternational
InstituteforIntegrativeSleepMedicine(IIIS).EEGisthemeasureofthebrain’selectricalactivity,
and it commonly contains significant noise artifact. NR-GAN’s core idea is to reduce or remove
thenoisepresentinthefrequencydomainrepresentationofanEEGsignal.ThearchitectureofG
isatwo-layer1DCNNwithafullyconnectedlayerattheoutput.Dcontainsalmostthesametwo-
layer1DCNNstructurewiththefullyconnectedlayerreplacedbyasoftmaxlayertocalculatethe
probabilitythattheinputbelongstothetrainingset.ThelossfunctionsaredefinedinEquations(7)
and(8)as (cid:2)
G = [loд(1−D(G(x)))+α(cid:5)x −G(x)(cid:5)2], (7)
loss
(cid:2)x∈Sns
(cid:2)
D = [loд(D(G(x)))]+ [loд(1−D(y))], (8)
loss
x∈Sns y∈Scs
whereS andS are the noisy and clear EEG signals, respectively.α is a hyperparameter that
ns cs
essentiallycontrolstheaggressivenessofnoisereduction;theauthorschoseavalueofα =0.0001.
Forthiswork,thegeneratordoesnotsamplefromalatentspace;rather,itattemptstogenerate
theclearsignalfromthenoisyEEGsignalinput(Figure8).TheauthorsfoundthattheNR-GAN
iscompetitivewithclassicalfrequencyfiltersintermsofnoisereduction.Theyalsostatethatthe
experimentalconditionsmayfavortheNR-GANandlistsomelimitationsintermsoftheamount
of noise NR-GAN can handle and the influence ofα. However, this is a novel method for noise
reductionincontinuoussequentialdatausingGANs.
4.2.3 TimeGAN (Dec. 2019). TimeGAN provides a framework that utilizes both the conven-
tional unsupervised GAN training method and the more controllable supervised learning ap-
proach [107]. By combining an unsupervised GAN network with a supervised AR model, the
networkaimstogeneratetimeserieswithpreservedtemporaldynamics.Thearchitectureofthe
TimeGANframeworkisillustratedinFigure9.Theinputtotheframeworkisconsideredtoconsist
oftwoelements:astaticfeatureandatemporalfeature.srepresentsavectorofstaticfeaturesand
xoftemporalfeaturesattheinputtotheencoder.Thegeneratortakesatupleofstaticandtempo-
ralrandomfeaturevectorsdrawnfromaknowndistribution.Therealandsyntheticlatentcodesh
andhˆ areusedtocalculatethesupervisedlosselementofthisnetwork.Thediscriminatorreceives
thetupleofrealandsyntheticlatentcodesandclassifiesthemaseitherreal(y)orsynthetic(yˆ),
andthe˜operatordenotesthesampleaseitherrealorfake.
ThethreelossesusedinTimeGANarecalculatedasfollows.
⎡ ⎢ (cid:2) ⎤ ⎥
L reconstruction =E s,x1:T ∼p ⎢ ⎢ ⎢ (cid:5)s−s˜(cid:5) 2 + (cid:5)x t −x˜ t (cid:5) 2 ⎥ ⎥ ⎥ (9)
⎣ ⎦
t
2C-RNN-GANGitHub:https://github.com/olofmogren/c-rnn-gan/.
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

GenerativeAdversarialNetworksinTimeSeries:ASystematicLiteratureReview 199:13
Fig.8. NR-GANarchitecturewithnoisyEEGinputSns andcleaninputdataScs.
Fig.9. TimeGANarchitecture.
|     | ⎡   |     | (cid:2) | ⎤    | ⎡          |     | (cid:2)  | ⎤   |
| --- | --- | --- | ------- | ---- | ---------- | --- | -------- | --- |
|     | ⎢   |     |         | ⎥    | ⎢          |     |          | ⎥   |
| =E  | ⎢   |     |         | ⎥ +E | ⎢ loд(1−yˆ |     | loд(1−yˆ | ⎥   |
L unsupervised s,x1:T ∼p ⎢ loд(y S )+ loд(y t ) ⎥ s,x1:T ∼pˆ ⎢ S )+ t ) ⎥ (10)
|     | ⎢   |     |     | ⎥          | ⎢   |     |     | ⎥   |
| --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
|     | ⎣   |     | t   | ⎦          | ⎣   |     | t   | ⎦   |
|     |     |     |     | ⎡ ⎢(cid:2) |     |     | ⎤   |     |
⎥
|     |            | =E  |        | ⎢ (cid:5)h | −д        | )(cid:5) | ⎥   |      |
| --- | ---------- | --- | ------ | ---------- | --------- | -------- | --- | ---- |
|     | L          |     | ∼p     | ⎢          | (h ,h t−1 | ,z       | ⎥   | (11) |
|     | supervised |     | s,x1:T | ⎢ t        | X S       | t        | 2 ⎥ |      |
|     |            |     |        | ⎣          |           |          | ⎦   |      |
t
ThecreatorsofTimeGANconductedexperimentsongeneratingsinewaves,stocks(dailyhistor-
icalGooglestocksdatafrom2004to2019),energy(UCIAppliancesenergypredictiondataset)[26],
andevent(privatelungcancerpathwaysdataset)datasets.Abatchsizeof128andAdamoptimizer
wereusedfortraining,andimplementationdetailsareavailableonline.3Theauthorsdemonstrated
3TimeGANGitHub:https://github.com/jsyoon0823/TimeGAN.
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

199:14 E.Brophyetal.
improvements over other state-of-the-art time series GANs such as RCGAN, C-RNN-GAN, and
WaveGAN.
4.2.4 ConditionalSig-WassersteinGAN(SigCWGAN)(June2020). AproblemaddressedbyNi
etal.[76]isthatlongtimeseriesdatastreamscangreatlyincreasethedimensionalityrequirements
ofgenerativemodeling,whichmayrendersuchapproachesinfeasible.Tocounterthisproblem,the
authorsdevelopametricnamedSignatureWasserstein-1(Sig-W )thatcapturestimeseriesmodels’
1
temporaldependencyandusesitasadiscriminatorinatimeseriesGAN.Itprovidesanabstract
anduniversaldescriptionofcomplexdatastreamsanddoesnotrequirecostlycomputationlikethe
Wasserstein metric. A novel generator is also presented that is named conditional autoregressive
feed-forwardneuralnetwork(AR-FNN),whichcapturestheARnatureofthetimeseries.Thegen-
eratoriscapableofmappingpastseriesandnoiseintofutureseries.Forarigorousmathematical
descriptionoftheirmethod,theinterestedreadershouldconsulttheworkofNietal.[76].
FortheAR-FNNgenerator,theideaistoobtainthestep-qestimatorXˆ(t) .Thelossfunction
t+1:t+q
forD isdefinedas
(cid:2) (cid:9) (cid:10) (cid:9) (cid:10)
(cid:8) (cid:8)
L(θ)= (cid:8) (cid:8) E μ S M (X t+1:t+q )|X t−p+1:t −E v S M (Xˆ t (t + ) 1:t+q )|X t−p+1:t (cid:8) (cid:8), (12)
t
wherev andμ aretheconditionaldistributionsinducedbytherealdataandsyntheticgenerator,
respectively.X t−p+1:t isthetruepastpath,Xˆ t (t + ) 1:t+q istheforecastednextpath,andX t+1:t+q isthe
trueforecastvalue.S isthetruncatedsignatureofpathX ofdegreeM.FurtherdetailsoftheNi’s
M
algorithm can be found in the appendix of their original paper [76]. SigCWGAN eliminates the
problemofapproximatingacostlyDandsimplifiestraining.Itisreportedtoachievestate-of-the-
art results on synthetic and empirical datasets compared to TimeGAN, RCGAN, and generative
momentmatchingnetworks(GMMNs)[68].TheempiricaldatasetconsistsoftheS&P500index
(SPX)andDowJonesindex(DJI)andtheirrealizedvolatility,whichisretrievedfromtheOxford-
ManInstitute’s“realizedlibrary”[55].Abatchsizeof200withtheAdamoptimizerwasusedfor
training.4
4.2.5 Decision-AwareTimeSeriesConditionalGAN(DAT-CGAN)(Sept.2020). Thisframework
isdesignedtoprovidesupportforendusers’decisionprocesses,specificallyinfinancialportfolio
choices. It uses a multi-Wasserstein loss on structured decision-related quantities [91]. The dis-
criminatorlossandgeneratorlossaredefinedinEquations(13)and(14),respectively.Forfurther
detailsonthelossfunctions,seeSection3oftheoriginalpaper[91]andEquations(15)through(18).
(cid:2)K (cid:3) (cid:4) (cid:2)K (cid:2)J (cid:3) (cid:4)
inf sup ω Er −EGη + λ Ef,R −Ef,Gη (13)
k k k j,k j,k j,k
η γk,θj,k k=1 k=1 j=1
(cid:2) (cid:2)
inf − ω EGη − λ Ef,Gη (14)
k k j,k j,k
η
k k,j
Er k =E rt+k ∼P(rt+k |xt) [D γk (r t+k ,x t )] (15)
EG k η =E zt,k ∼P(zt,k) [D γk (r t (cid:6) ,k ,x t )] (16)
Ef j, , k R =E Rt,k ∼P(Rt,k |xt) [D θj,k (f j,k (R t,k ,x t ),x t )] (17)
Ef j, , k Gη =E Zt,k ∼P(Zt,k) [D θj,k (f j,k (R t (cid:6) ,k ,x t ),x t )] (18)
4SigCWGANGitHub:https://github.com/SigCGANs/Conditional-Sig-Wasserstein-GANs/.
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

GenerativeAdversarialNetworksinTimeSeries:ASystematicLiteratureReview 199:15
WeofferafulldescriptionofalltermsusedinEquations(13)and(14).D isthediscriminatorfor
γk
thedataatlookaheadperiodk withrespecttoparametersγ.G isthegeneratorwithparameters
η
η.Asthisistheconditionalcase,x istheconditioningvariablecontainingrelevantinformation
t
(cid:6)
up to timet.r = G (z ,x ) is defined as the synthetic data at look ahead pointk where the
t,k η t,k t
noiseisz .Thediscriminatorfordecision-relatedquantityj atlookaheadperiodk withrespect
t,k
to parameters θ is defined as D . These decision-related quantities may include mean and
j,k θj,k
covariance,forexample. f (R ,x )representsthedecision-relatedquantity.Finally,ω andλ
j,k t,k t k j,k
are weights andinf andsup are the infimum and supremum or greatest lower bound and least
upperboundofanon-emptysubset,respectively.
The generator is a two-layer feed-forward NN for each input—assets in this case.G outputs
assetreturnsthatareusedtocomputedecision-relatedquantities.ThesequantitiesarefedintoD,
whichisalsoatwo-layerfeed-forwardNN.Furtherdetailsaboutthearchitecturecanbefoundin
theappendixoftheworkofSunetal.[91].Thedatasetusedisdailypricedataforeachoffour
U.S.Exchange-tradedfunds(ETFs):Material(XLB),Energy(XLE),Financial(XLF),andIndustrial
(XLI)ETFs,from1999to2016.Theauthorsfoundthismodelcapableofhigh-fidelitytimeseries
generationthatsupportsdecisionprocessesbyendusersduetoincorporatingadecision-aware
loss function. However, this approach’s limitation is that the computational complexity of this
modelisvastandrequires1monthoftrainingtimeforasinglegenerativemodel.
PrivacyDevelopments
4.2.6 RecurrentConditionalGAN(RCGAN)(2017). RCGANforcontinuousdatageneration[31]
differsarchitecturallyfromtheC-RNN-GAN.AlthoughtheRNNLSTMisused,thediscriminator
isunidirectional,andtheoutputsofGarenotfedbackasinputsatthenexttimestep.Thereisalso
additional information that the model is conditioned on, which makes for a conditional RGAN;
seethelayoutofthemodelinFigure10.ThepurposeoftheRCGANandRGANinthisworkis
togeneratecontinuoustimeserieswithafocusonmedicaldataintendedforuseindownstream
tasks,andthiswasoneofthefirstworksinthisarea.ThelossfunctionscanbeseeninEquations
(19)and(20),whereCEistheaveragecross-entropybetweentwosequences.X aresamplesdrawn
n
fromthetrainingdataset.y istheadversarialgroundtruth;forrealsequences,itisavectorof1s,
n
andconversely,forgeneratedorsyntheticsequences,itisavectorof0s.Z isasequenceofpoints
n
sampledfromthelatentspace,andthevalidadversarialgroundtruthiswrittenhereas1.
D (X ,y )=−CE(D(X ),y ) (19)
loss n n n n
G (Z )=D (G(Z ),1)=−CE(D(G(Z )),1) (20)
loss n loss n n
Intheconditionalcase,theinputstoDandG areconcatenatedwithsomeconditionalinforma-
tionc .ThisvariantofanRNN-GANfacilitatesthegenerationofasyntheticcontinuoustimese-
n
riesdatasetwithassociatedlabels.Experimentswerecarriedoutongeneratedsinewaves,smooth
functionssampledfromaGaussianprocesswithazero-valuedmeanfunction,theMNISTdataset
asasequence,andthePhilipseICUdatabase[83].Abatchsizeof28withAdamandgradientde-
scentoptimizerswasusedfortraining.Theauthorsproposeanovelmethodforevaluatingtheir
model,whichisdiscussedfurtherinSection6.Fullexperimentaldetailscanbefoundonline.5
4.2.7 Sequentially Coupled GAN (SC-GAN) (April 2019). SC-GAN aims to generate patient-
centricmedicaldatatoinformofapatient’scurrentstateandgeneratearecommendedmedication
dosagebasedonthestate[97].Itconsistsoftwocoupledgeneratorstaskedwithproducingtwo
5RCGANGitHub:https://github.com/ratschlab/RGAN/.
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

| 199:16 |     |     |     | E.Brophyetal. |     |
| ------ | --- | --- | --- | ------------- | --- |
Fig.10. RCGANarchitecturewithconditionalinputc,inputdatax,andlatentvariablez.
|     | Fig.11. | SC-GANarchitecture. |     |     |     |
| --- | ------- | ------------------- | --- | --- | --- |
outcomes:oneforthecurrentstateofanindividualandtheotherforarecommendedmedication
dosagebasedontheindividual’sstate.Thediscriminatorisatwo-layerbidirectionalLSTM,and
thecoupledgeneratorsarebothtwo-layerunidirectionalLSTMs.Figure11presentsfurtherdetails
ofthearchitecture.
G generatestherecommendedmedicationdosagedata(a ,a ,...,a )withacombinedinput
| 1   |     |     | 1 2 T |     |     |
| --- | --- | --- | ----- | --- | --- |
of the sequential continuous patient state data (s ,s ,...,s T−1 ) and a random noise sequence
|     |     | 0 1 |     |     |     |
| --- | --- | --- | --- | --- | --- |
(zˆa ,zˆa ,...,zˆ a ) sampled from a uniform distribution. At each timestept, the input z a ofG is
| 0 1 T −1 |     |     |     | t   | 1   |
| -------- | --- | --- | --- | --- | --- |
andzˆa.
| theconcatenationofs t | t   |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- |
Conversely,G istaskedwithgeneratingthepatientstatedatas andateachtimesteptheinput
2 t
zs istheconcatenationofs ,a andzˆs .ThismeansthattheoutputsfromG andG arethe
| t   | t−1 t−1 | t   |     | 1 2 |     |
| --- | ------- | --- | --- | --- | --- |
inputstooneanother.Combiningthegeneratorstogetherleadstothefollowinglossfunction:
(cid:2)N (cid:2)T
|     | 1    | 1           |      |     |      |
| --- | ---- | ----------- | ---- | --- | ---- |
|     | L =  | loд(1−D(G(z | ))), |     | (21) |
|     | G NT |             | i,t  |     |      |
i=1 t=1
|     |     | (cid:9)      | (cid:10) |     |      |
| --- | --- | ------------ | -------- | --- | ---- |
|     | G(z | )= G (za );G | (zs ) ,  |     | (22) |
|     |     | i,t 1 i,t 2  | i,t      |     |      |
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

GenerativeAdversarialNetworksinTimeSeries:ASystematicLiteratureReview 199:17
whereN isthenumberofpatientsandT isthetimelengthofthepatientrecord.TheSC-GANhas
a supervised pre-training step for the generators to avoid an excessively strongD that uses the
least-squaresloss.
The discriminator is tasked with classifying the sequential patient-centric records as real or
synthetic,andthelossfunctionisdefinedas
(cid:2)N (cid:2)T
1 1
L =− (loдD(x )+loд(1−D(G(z )))), (23)
D i,t i,t
NT
i=1 t=1
where x = [s ;a ]. This model contains novel coupled generators that coordinate to generate
i,t t t
patientstateandmedicationdosagedata.Ithasperformanceclosetorealdataforthetreatment
recommendationtask.ThedatasetusedinthisexperimentisMIMIC-III[56].Theauthorsbench-
mark their SC-GAN against variants of SeqGAN, C-RNN-GAN, and RCGAN and observe their
modeltobethebestperformingforthisspecificusecase.
4.2.8 Synthetic Biomedical Signals GAN (SynSigGAN) (Dec. 2020). SynSigGAN is designed to
generate different kinds of continuous physiological/biomedical signal data [49]. It is capable of
generatingECG,EEG,electromyography(EMG),andphotoplethysmography(PPG)fromtheMIT-
BIHArrhythmiadatabase[75],SienaScalpEEGdatabase[23],andBIDMCPPGandRespiration
dataset[82].AnovelGANarchitectureisproposedherethatusesabidirectionalgridlongshort-
termmemory(BiGridLSTM)forthegenerator(Figure12)andaCNNforthediscriminator.The
BiGridLSTM is a combination of a double GridLSTM (a version of LSTM that can represent the
LSTMsinamultidimensionalgrid)withtwodirectionsthatcancombatthegradientphenomenon
fromtwodimensionsandarefoundtoworkwellintimesequenceproblems.Theauthorsusedthe
valuefunctiondefinedpreviouslyinEquation(2).
SynSigGAN is capable of capturing the different physiological characteristics associated with
eachofthesesignaltypesandhasdemonstratedanabilitytogeneratebiomedicaltimeseriesdata
withamaxsequencelengthof191datapoints.Theauthorsalsopresentapreprocessingstageto
clean and refine the biomedical signals in this work. They compare theirarchitectureto several
variants (BiLSTM-GRU, BiLSTM-CNN GAN, RNN-AE GAN, Bi-RNN, LSTM-AE, BiLSTM-MLP,
LSTM-VAEGAN,andRNN-VAEGAN)andfoundtheBiGrid-LSTMasthebest-performingmodel.
EvaluationDevelopments
As evaluating GANs has been identified as one of their major challenges, we discuss standard
evaluationmetricsandnoveldevelopmentsformallyinSection6.
5 APPLICATIONS
WehavediscussedthetwoclassesoftimeseriesGANsandtheircontributiontosolvingthechal-
lengespresentedinSection3.2.Nowwewilllistthewide-rangingapplicationsoftimeseriesGANs
andthebenefitsofsuchtobothresearchandindustry.
5.1 DataAugmentation
It is common knowledge in the deep learning community that GANs are among the methods
of choice when discussing data augmentation. Reasons for augmenting datasets range from in-
creasingthesize/varietyofsmallandimbalanceddatasets[2,44,59,77]toreproducingrestricted
datasetsfordissemination.
Awell-definedsolutiontothedatashortageproblemistransferlearning,anditworkswellin
domainadaptation,whichhasledtoadvancementsinclassificationandrecognitionproblems[78].
However,ithasbeenfoundthataugmentingdatasetswithGANscanleadtofurtherimprovements
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

199:18 E.Brophyetal.
(cid:6)
Fig. 12. Architecture of BiGridLSTM with LSTM blocks for the time and depth dimension. The prime ( )
symbolindicatesreverseinthefigureasintheworkofFeiandTan[34].
in certain classification and recognition tasks [110]. Data synthesized by a GAN can adhere to
stricterprivacymeasuresdiscussedinSection7.Thisfurtherdemonstratestheadvantagesofaug-
mentingyourtrainingdatasetwithGANsoverimplementingtransferlearningwithapre-trained
modelfromadifferentdomainonasmallerdataset.
Many researchers find that accessing datasets for their deep learning research and models to
be time-consuming, laborious work, particularly when the research is concerned with personal
sensitive data. Often medical and clinical data are presented as continuous sequential data that
can only be accessed by a small contingent of researchers who are not at liberty to disseminate
their research openly. This, in turn, may lead to stagnation in the research progress in these
domains.
Fortunately,wearebeginningtoseetheuptakeofGANsappliedtotimeserieswiththesetypes
ofmedicalandphysiologicaldata[12,21,31,49,111].Brophy[11]showsthatdependentmultivari-
atecontinuoushigh-fidelityphysiologicalsignalgenerationiscapableviaGANs,demonstrating
theimpressivecapabilityofthesenetworks.Figure13presentsanexampleoftherealinputand
syntheticgenerateddata.
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

GenerativeAdversarialNetworksinTimeSeries:ASystematicLiteratureReview 199:19
Fig. 13. An example of dependent multichannel ECG data (left) and generated ECG from a multivariate
GAN(right)[11].NSRindicatesthetrainingdataset,whichisthenormalsinusrhythm.Thegenerateddata
isproducedbyaGANnamedbytheauthorsasLSGAN-DTW.
Ofcourse,thisisnotcomprehensivecoverageoftheresearchusingtimeseriesGANsfordata
synthesis and augmentation. GANs have been applied to time series data for a plethora of use
cases.
Audio generation (both music and speech) and text-to-speech (TTS) [57] have been popular
areasforresearcherstoexplorewithGANs.TheC-RNN-GANdescribedinSection4.2.1wasone
oftheseminalworkstoapplyGANstogeneratingcontinuoussequentialdataintheformofmusic.
Inthefinancialsector,GANshavebeenimplementedtogeneratedataandpredict/forecastval-
ues.Wieseetal.[101]implementedaGANtoapproximatefinancialtimeseriesindiscretetime.
Nietal.[76]designedadecision-awareGANthatgeneratessyntheticdataandsupportsdecision
processestofinancialportfolioselectionofendusers.
Other time seriesgeneration/predictionmethodsrange from estimating soil temperature[67]
topredictingmedicineexpenditurebasedonthecurrentstateofpatients[58].
5.2 Imputation
Inreal-worlddatasets,missingorcorruptdataisanalltoocommonproblemthatleadstodown-
stream problems. These issues manifest themselves in further analytics of the dataset and can
inducebiasesinthedata.Commonmethodsofdealingwithmissingorcorrupteddatainthepast
have been the deletion of data streams containing the missing segments, statistical modeling of
thedata,ormachinelearningimputationapproaches.Lookingatthelatter,wereviewtheworkin
imputingthesedatausingGANs.Guoetal.[42]designedaGAN-basedapproachformultivariate
timeseriesimputation.Figure14presentsanexampleofimputeddatafromatoyexperiment[12].
5.3 Denoising
Artifacts induced in time series data often manifest themselves as noise in the signals. This has
become an ever-present challenge in further processing and analytical applications. Corrupted
datacancausebiasesinthedatasetsorleadtodegradationintheperformanceofcriticalsystems
such as those used for health applications. Common methods for dealing with noise include
the use of adaptive linear filtering. Another approach recently explored in the work of Sumiya
etal.[90]usedGANsasanoise-reductiontechniqueinEEGdata.Theirexperimentsshowedthat
theirproposedNR-GAN(Section4.2.2)wascapableofcompetitivenoisereductionperformance
comparedtomoretraditionalfrequencyfilters.
5.4 AnomalyDetection
Detectingoutliersoranomaliesintimeseriesdataisanimportantpartofmanyreal-worldsystems
andsectors.Whetheritisdetectingunusualpatternsinphysiologicaldatathatmaybeaprecursor
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

199:20 E.Brophyetal.
Fig.14. Anexampleoftheincompletecorruptedtimeseries(top)andimputedsignal(bottom).
tosomemoremaliciousconditionordetectingirregulartradingpatternsonthestockexchange,
anomalydetectingcanbevitaltokeepingusinformedonimportantinformation.Statisticalmea-
suresofnon-stationarytimeseriessignalsmayachievegoodperformanceonthesurface,butthey
might also miss some important outliers present in deeper features. They may also struggle in
exploitinglargeunlabeleddatasets;thisiswheretheunsuperviseddeeplearningapproachescan
outperform the conventional methods. Zhu et al. designed a GAN algorithm for anomaly detec-
tionintimeseriesdata(ECGandtaxidataset)withLSTMsandGANs,whichachievedsuperior
performancecomparedtoconventional,moreshallowapproaches[112].Similarapproacheshave
beenappliedtodetectcardiovasculardiseases[69],incyber-physicalsystemstodetectnefarious
players[66],andevenirregularbehaviorssuchasstockmanipulationonthestockmarkets[63].
5.5 OtherApplications
Someworkshaveutilizedimage-basedGANsfortimeseriesandsequentialdatagenerationbyfirst
convertingtheirsequencestoimagesviasometransformationfunctionandtrainingtheGANon
theseimages.OncetheGANconverges,similarimagescanbegenerated;then,asequencecanbe
retrievedusingtheinverseoftheoriginaltransformationfunction.Forexample,thisapproachhas
beenimplementedinaudiogenerationwithwaveforms[16,24,60],anomalydetection[18],and
physiologicaltimeseriesgeneration[12].
6 EVALUATIONMETRICS
AsmentionedinSection3,GANscanbedifficulttoevaluate,andresearchersareyettoagreeon
what metrics reflect GAN performance best. There have been plenty of metrics proposed in the
literature[8],withmostofthemsuitedtothecomputervisiondomain.Workisstillongoingto
suitably evaluate time series GANs. We can break down evaluation metrics into two categories:
qualitativeandquantitative.Qualitativeevaluationisanothertermforhumanvisualassessment
via the inspection of generated samples from the GAN. However, this cannot be deemed a full
evaluationofGANperformanceduetothelackofasuitableobjectiveevaluationmetric.Thequan-
titativeevaluation includes the use of metrics associatedwith statisticalmeasuresused for time
series analytics and similarity measures such as the Pearson correlation coefficient (PCC), per-
centrootmeansquaredifference(PRD),rootmeansquarederror(RMSE)andmeansquarederror
(MSE),meanrelativeerror(MRE),andmeanabsoluteerror(MAE).Thesemetricsareamongthe
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

GenerativeAdversarialNetworksinTimeSeries:ASystematicLiteratureReview 199:21
mostcommonlyusedfortimeseriesevaluationand,assuch,areusedasasuitableGANperfor-
mancemetric,astheycanreflectthestabilitybetweenthetrainingdataandsyntheticgenerated
data,andweshowsomeofthesecommonformulasinEquations(24)through(27).
(cid:5)
|     |     |     |       | N (x    | −x˜)(y  | −y˜)       |     |     |     |      |
| --- | --- | --- | ----- | ------- | ------- | ---------- | --- | --- | --- | ---- |
|     |     |     |       | i=1     | i       | i          |     |     |     |      |
|     |     |     | PCC = | (cid:6) |         |            |     |     |     | (24) |
|     |     |     |       | (cid:5) | (cid:5) |            |     |     |     |      |
|     |     |     |       | N (x    | −x˜)2   | N (y −y˜)2 |     |     |     |      |
|     |     |     |       | i=1 i   | i=1     | i          |     |     |     |      |
(cid:7)
(cid:5)
|     |     |     |     |     | N (x −y      | )2  |     |     |     |      |
| --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | ---- |
|     |     |     |     |     | i(cid:5)=1 i | i   |     |     |     |      |
|     |     |     | PRD | =   |              |     |     |     |     | (25) |
|     |     |     |     |     | N            | )2  |     |     |     |      |
|     |     |     |     |     | i=1 (x i     |     |     |     |     |      |
(cid:11)(cid:8)(cid:9)
(cid:2)N
1
−y )2
|     |     |     | RMSE | =   | (x i | i   |     |     |     | (26) |
| --- | --- | --- | ---- | --- | ---- | --- | --- | --- | --- | ---- |
N
i=1
(cid:2)N
(cid:8) (cid:8)x −y (cid:8) (cid:8)
|     |     |     |      | 1   | (cid:8) i | i(cid:8)    |     |     |     |      |
| --- | --- | --- | ---- | --- | --------- | ----------- | --- | --- | --- | ---- |
|     |     |     | MRAE | =   | (cid:8)   | (cid:8)     |     |     |     | (27) |
|     |     |     |      | N   | (cid:8)x  | − f (cid:8) |     |     |     |      |
i i
i=1
Acrosstheseformulas,x i istheactualvalueofthetimeseriesx attime/samplei,andy i isthe
generated value of the time seriesy at time/samplei. x˜ andy˜ represents the mean values of x
andy,respectively. f isusedintheMRAEcalculationfortheforecastvalueattimei ofachosen
i
benchmarkmodel.Ingeneral, f i canbechosentobey i−1 fornon-seasonaltimeseriesandy i−M
| forseasonaltimeseries,whereM |     |     | istheseasonalperiodofx. |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- |
Several metrics have become well-established choices in evaluating image-based GANs, and
some of these have permeated through to the sequential and time series GANs such as IS [88],
Fréchet distance, and FID [51]. The structural similarity index (SSIM) is a measure of similarity
between two images. However, Parthasarathy et al. [80] use this with time series data, as SSIM
doesnotexcludeitselffromcomparingalignedsequencesoffixedlength.
Ofcourse,someofthesemetricsaremeasuresofsimilarities/dissimilaritiesbetweentwoprob-
abilitydistributions,suitableformanytypesofdata,particularlyMMD[39].Intherealworld,we
do not have access to the underlying distributions of data, and therefore we show an empirical
estimateofMMDinEquation(28),whichisaquitesuitablemetricforthistaskacrossdomains:
|     |             | ⎡   |          |        |            |        |      |          | ⎤1     |      |
| --- | ----------- | --- | -------- | ------ | ---------- | ------ | ---- | -------- | ------ | ---- |
|     |             | ⎢   | (cid:2)m |        | m(cid:2),n |        |      | (cid:2)n | ⎥      |      |
|     |             | ⎢   |          |        |            |        |      |          | ⎥ 2    |      |
|     | MMD[F,X,Y]= | ⎢   | 1        | )−     | 2          |        | 1    |          | )⎥     |      |
|     |             | ⎢   |          | k(x ,x |            | k(x ,y | )+   | k(y      | ,y ⎥ , | (28) |
|     |             | ⎢m2 |          | i j    | mn         | i      | i n2 |          | i j ⎥  |      |
|     |             | ⎣   | i,j=1    |        | i,j=1      |        |      | i,j=1    | ⎦      |      |
whereF isaclassFofsmoothfunctions f : X → R.TwoobservationsX := {x ,x ,...,x }and
|               |                                     |     |     |     |     |                              |     |     | 1 2 | n   |
| ------------- | ----------------------------------- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- |
| {y            | }aredrawnfromtwodistributionsp      |     |     |     |     |                              |     |     |     |     |
| Y :=          | 1 ,y 2 ,...,y n                     |     |     |     |     | andq withmpointssampledfromp |     |     |     | and |
| nfromq.Last,k | isthekernelfunctionchosenbytheuser. |     |     |     |     |                              |     |     |     |     |
Another metric that generalizes well to the sequential data case is the Wasserstein distance.
TheWassterstein-1,orEarthMoverdistance,showninEquation(29),describesthecostittakesto
moveonecumulativedistributionfunctiontoanotherwhilepreservingtheshapeofthefunctions,
whichisdonebyoptimizingthetransportplan:
|     |     |     |     | (cid:10) (cid:11) |     |     | (cid:12) |     |     |     |
| --- | --- | --- | --- | ----------------- | --- | --- | -------- | --- | --- | --- |
1
|     |     |          |     |          | dp(x,y)dγ(x,y) |     | p   |     |     |      |
| --- | --- | -------- | --- | -------- | -------------- | --- | --- | --- | --- | ---- |
|     |     | W (μ,ν)= |     | inf      |                |     |     | ,   |     | (29) |
|     |     | p        |     | γ∈`(μ,ν) |                |     |     |     |     |      |
XxY
where`(μ,ν)isthesetofalltransportplans,dp(x,y)isthedistancefunction,anddγ(x,y)isthe
amountof“mass”tobemoved.
The data generated from GANs have been used in downstream classification tasks. Using
the generated data together with the training data has led to the Train on Synthetic, Test on
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

199:22 E.Brophyetal.
Real (TSTR) and Train on Real, Test on Synthetic (TRTS) evaluation methods, first proposed
by Esteban et al. [31]. In scoring downstream classification applications that use both real
and generated data, studies have adopted the precision, recall, and F1 scores to determine the
classifier’s quality and, in turn, the quality of the generated data. Other accuracy measures of
classifierperformanceincludetheweightedaccuracy(WA)andunweightedaveragerecall(UAR).
OftenuseddistanceandsimilaritymeasuresintimeseriesdataaretheEuclideandistance(ED)
anddynamictimewarping(DTW)algorithms.Multivariate(in)dependentdynamictimewarp-
ing(MVDTW),implementedintheworkofBrophy[11],candeterminesimilaritymeasuresacross
bothdependentandindependentmultichanneltimeseriessignals.TheideabehindDTWistofind
theminimumcost,oroptimalalignmentofthewarpingpathviathecumulativedistancefunction.
TheMVDTWcumulativedistancefunctionisgiveninEquation(30),whichisusedtofindthepath
thatminimizesthewarpingcostofmultivariatetimeseriessignals.
(cid:2)M
D(i,j)= (q −c )2+min{D(i−1,j−1),D(i−1,j),D(i,j−1)} (30)
i,m j,m
m=1
Othermetricsusedacrossdifferentapplicationsinclude:
• Financialsector:Autocorrelationfunction(ACF)scoreandDYmetric.
• Temperatureestimation:Nash-Sutcliffemodelefficiencycoefficient(NS),Willmottindexof
agreement(WI),andtheLegatesandMcCabeindex(LMI).
• Audiogeneration:Normalizedsource-to-distortionratio(NSDR),source-tointerferenceratio
(SIR),source-to-artifactratio(SAR),andt-SNE[95].
ForafulllistofGANarchitecturesreviewedinthiswork,theirapplications,evaluationmetrics,
anddatasetsusedintheirrespectiveexperiments,seeTable2.ResultsforthesinewaveandECG
generationusingvariantsofGANarchitecturescanbefoundinTables3and4,respectively.
7 PRIVACY
Aswellasevaluatingthequalityofthedata,awiderangeofmethodshavebeenusedtoevaluate
andmitigatetheprivacyriskassociatedwithsyntheticdatacreatedbyGANs.
7.1 DifferentialPrivacy
Thegoalofdifferentialprivacyistopreservetheunderlyingprivacyofadatabase.Analgorithmor,
morespecifically,aGANachievesdifferentialprivacyif,bylookingatthegeneratedsamples,we
cannotidentifywhetherthesampleswereincludedinthetrainingset.AsGANsattempttomodel
the training dataset, the problem of privacy lies in capturing and generating useful information
aboutthetrainingsetpopulationwithoutthepossibilityoflinkagefromgeneratedsampletoan
individual’sdata[27].
Aswehaveaddressedpreviously,oneofthemaingoalsofGANsistoaugmentexistingunder-
resourced datasets for use in further downstream applications such as upskilling of clinicians
wherehealthcaredataisinvolved.Thesepersonalsensitivedatamustcontainprivacyguarantees,
andtherigorousmathematicaldefinitionofdifferentialprivacy[28]offersthisassurance.
Work is ongoing to develop machine learning methods with privacy-preserving mechanisms
suchasdifferentialprivacy.Abadietal.[1]demonstratedtheabilitytotraindeepNNswithdiffer-
entialprivacyandimplementedamechanismfortrackingprivacyloss.Xieetal.Xie2018proposed
adifferentiallyprivateGAN(DPGAN)thatachievedDPbyaddingnoisegradientstotheoptimizer
duringthetrainingphase[103].
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

GenerativeAdversarialNetworksinTimeSeries:ASystematicLiteratureReview 199:23
Table2. ListofGANArchitectures,TheirApplications,andDatasetsUsedinTheirExperimentsand
EvaluationMetricsUsedtoJudgetheQualityoftheRespectiveGANs
| Application | GANArchitecture(s) |     | Dataset(s) | EvaluationMetrics |
| ----------- | ------------------ | --- | ---------- | ----------------- |
Medical/physiological LSTM-LSTM [2, 31, 44, 45, EEG,ECG,EHRs, TSTR,MMD,
| generation | 77,97]             |     | PPG,EMG,speech, | reconstructionerror, |
| ---------- | ------------------ | --- | --------------- | -------------------- |
|            | LSTM-CNN[11,21]    |     | NAF,MNIST,      | DTW,PCC,IS,FID,      |
|            | BiLSTM-CNN[111]    |     | syntheticsets   | ED,S-WD,RMSE,        |
|            | BiGridLSTM-CNN[49] |     |                 | MAE,FD,PRD,          |
|            | CNN-CNN[33,47]     |     |                 | averagingsamples,    |
|            | AE-CNN[81]         |     |                 | WA,UAR,MV-DTW        |
FCNN[104]
| Financialtimeseries | TimeGAN[107] |     | S&P500index(SPX), | Marginal |
| ------------------- | ------------ | --- | ----------------- | -------- |
generation/prediction SigCWGAN[76] DowJonesindex distributions,
|     | DAT-GAN[91]   |     | (DJI),ETFs | dependencies,TSTR,   |
| --- | ------------- | --- | ---------- | -------------------- |
|     | QuantGAN[101] |     |            | Wassersteindistance, |
EMdistance,DY
metric,ACFscore,
leverageeffectscore,
discriminativescore,
predictivescore
| Timeseries            | LSTM-NN[67]  |     | Meteorologicaldata, | RMSE,MAE,NS,WI, |
| --------------------- | ------------ | --- | ------------------- | --------------- |
| estimation/prediction | LSTM-CNN[58] |     | TruvenMarketScan    | LMI             |
|                       | LSTM-MLP[58] |     | dataset             |                 |
Audiogeneration C-RNN-GAN[74] Nottinghamdataset, Humanperception,
|     | TGAN(variant)[16]  |     | midimusicfiles,    | polyphony,scale   |
| --- | ------------------ | --- | ------------------ | ----------------- |
|     | RNN-FCN[109]       |     | MIR-1K,TheSession, | consistency,tone  |
|     | DCGAN(variant)[60] |     | speech             | span,repetitions, |
|     | CNN-CNN[57]        |     |                    | NSDR,SIR,SAR,FD,  |
t-SNE,distributionof
notes
| Timeseries | MTS-GAN[42] |     | TEP,pointmachine, | Visually,MMD,MAE, |
| ---------- | ----------- | --- | ----------------- | ----------------- |
imputation/repairing CNN-CNN[84] windturbinedata, MSE,RMSE,MRE,
|     | DCGAN(variant)[43] |     | PeMS,PhysioNet    | spatialsimilarity, |
| --- | ------------------ | --- | ----------------- | ------------------ |
|     | AE-GRUI[71]        |     | Challenge2012,KDD | AUCscore           |
|     | RGAN[92]           |     | CUP2018,parking   |                    |
|     | FCN-FCN[15]        |     | lotdata,          |                    |
GRUI-GRUI[70]
Anomalydetection LSTM-LSTM[63] SET50,NYCtaxidata, Manipulateddata
|                 | LSTM-(LSTM&CNN)[112] |           | ECG,SWaT,WADI     | usedasatestset,     |
| --------------- | -------------------- | --------- | ----------------- | ------------------- |
|                 | LSTM-LSTM            | (MAD-GAN) |                   | ROCcurve,precision, |
|                 | [66]                 |           |                   | recall,F1,accuracy  |
| Othertimeseries | VAE-CNN[80]          |           | Fixedlengthtime   | DTW,SSIM            |
| generation      |                      |           | series“vehicleand |                     |
enginespeed”
Fornovelapproaches,theGANnameisgivenastheyhavebeencoveredalreadyinSection4.
7.2 Decentralized/FederatedLearning
Distributed or decentralized learning is another method for limiting the privacy risk associated
withpersonalandpersonalsensitivedatainmachinelearning.Standardapproachestomachine
learningrequirethatalltrainingdatabekeptononeserver.Decentralized/distributedapproaches
to GAN algorithms require large communication bandwidth to ensure convergence [5, 46] and
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

199:24 E.Brophyetal.
Table3. ExperimentalResultsComparingthePerformanceofTimeSeries
GANsforSinewaveGeneration
ToySineDataset
Architecture LossFunction
|     | MMD DTW        | MSE    |
| --- | -------------- | ------ |
| BCE | 0.9527 91.1071 | 0.2308 |
LSTM-LSTM
| MSE | 0.0078 54.1644  | 0.1480 |
| --- | --------------- | ------ |
| BCE | 0.1215 428.4310 | 3.0700 |
BiLSTM-LSTM
| MSE | 0.9515 79.5607 | 0.2362 |
| --- | -------------- | ------ |
| BCE | 0.006 55.3620  | 0.3154 |
LSTM-CNN
| MSE | 0.5757 86.7357     | 0.5643 |
| --- | ------------------ | ------ |
| BCE | 1.129E-05 129.9257 | 0.9193 |
BiLSTM-CNN
| MSE | 0.4891 43.2694 | 0.1869 |
| --- | -------------- | ------ |
| BCE | 0.0244 37.1630 | 0.2303 |
GRU-CNN
| MSE | 0.3727 42.7348 | 0.22823 |
| --- | -------------- | ------- |
| BCE | 0.0039 58.3565 | 0.3048  |
FC-CNN
| MSE | 0.0117 43.3611 | 0.2972 |
| --- | -------------- | ------ |
Table4. ExperimentalResultsComparingthePerformanceofTimeSeries
GANsforECGGenerationontheMIT-BIHDataset
MIT-BIHArrhythmiaDataset
Architecture LossFunction
|     | MMD DTW        | MSE    |
| --- | -------------- | ------ |
| BCE | 0.9931 30.1816 | 0.0867 |
LSTM-LSTM
| MSE | 0.8842 44.4553 | 0.1389 |
| --- | -------------- | ------ |
| BCE | 0.9916 22.8634 | 0.0699 |
BiLSTM-LSTM
| MSE | 0.9737 23.5533 | 0.0806 |
| --- | -------------- | ------ |
| BCE | 0.5519 13.0158 | 0.0151 |
LSTM-CNN
| MSE | 0.0005 24.7306  | 0.0457 |
| --- | --------------- | ------ |
| BCE | 0.9246 117.3994 | 0.2272 |
BiLSTM-CNN
| MSE | 0.0687 22.6740 | 0.0586 |
| --- | -------------- | ------ |
| BCE | 0.0055 20.4845 | 0.0335 |
GRU-CNN
| MSE | 0.7704 108.4124 | 0.1948 |
| --- | --------------- | ------ |
| BCE | 0.2068 23.9910  | 0.0309 |
FC-CNN
| MSE | 0.3082 18.2340 | 0.0212 |
| --- | -------------- | ------ |
arealsosubjecttostrictprivacyconstraints.Anewmethodthatenablescommunicationefficient
collaborative learning on a shared model while keeping all of the training data decentralized
is known as federated learning [73]. Rasouli et al. [86] applied a federated learning algorithm
to a GAN for communication-efficient distributed learning and proved the convergence of
their federated learning GAN (FedGAN) [86]. However, it should be noted that they did not
experiment with differential privacy in this study but note that it as an avenue of future
work.
Combiningtheprecedingtechniquesoffederatedlearninganddifferentialprivacyindeveloping
newGANalgorithmswouldleadtoafullydecentralizedprivateGANcapableofgeneratingdata
withoutleakageofprivateinformationtothesourcedata.Thisisclearlyanopenresearchavenue
forthecommunity.
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

GenerativeAdversarialNetworksinTimeSeries:ASystematicLiteratureReview 199:25
7.3 AssessmentofPrivacyPreservation
Wecanalsoassesshowwellthegenerativemodelwasabletoprotectourprivacythroughtests
knownasattributeandpresencedisclosure[17].Thelattertestismorecommonlyknowninthe
machinelearningspaceasamembershipinferenceattack.Thishasbecomeaquantitativeassess-
mentofhowmachinelearningmodelsleakinformationabouttheindividualdatarecordsonwhich
theyweretrained[89].Membershipinferenceattacksattempttodetectthedatathatwasusedto
train a target model without the attacker having access to the model’s parameters. A nefarious
actorcreatesrandomrecordsforatargetmachinelearningmodel.Theattackerthenfeedseach
record into the model. The model will return a confidence score, and based on this score, the
recordswillbefinetuneduntilahigherconfidencescoreisreturned.Thisprocesswillcontinue
untilthemodelreturnsaveryhighscore,andatthisstagetherecordwillbenearlyidenticalto
oneoftheexamplesusedinthetrainingdataset.Thesestepswillberepeateduntilenoughdataset
examples are generated. The fake records will then be used to train an ensemble of models to
predictwhetheradatarecordwasusedinthetrainingsetofthetargetmodel.
Hayesetal.[48]carriedoutmembershipinferenceattacksonsyntheticimagesandconcluded
that for acceptable levels of privacy in the GAN, the quality of the data generated is sacrificed.
Conversely,othershavefollowedthisapproachandfoundthatdifferentialprivacynetworkscan
successfully generate data that adheres to differential privacy and resists membership inference
attackswithouttoomuchdegradationinthequalityofthegenerateddata[11,21,31].
8 DISCUSSION
WehavepresentedasurveyoftimeseriesGANvariantsthathavemadesignificantprogressinad-
dressingtheprimarychallengesidentifiedinSection3.2.TheseGANsintroducedtheideaofboth
discrete and continuous sequential data generation and have made incremental improvements
overoneanotherviaanarchitecturevariantoramodifiedobjectivefunctioncapableofcapturing
thespatio-temporaldependenciespresentinthesedatatypes.Thelossfunctionsimplementedin
theseworksforsomearchitectureswillnotnecessarilygeneralizetoothers;hence,theybecome
architecturespecific.ThearchitecturechoicesofthetimeseriesGANsaffectboththequalityand
diversityofthedata.However,thereremainopenproblemsintermsofthepracticalimplementa-
tionofthegenerateddataandGANsinreal-worldapplications,particularlyinhealthapplications
wheretheperformanceofthesemodelscandirectlyaffectpatients’qualityofcare/treatment.
The “best” GAN architecture and objective function is yet to be determined. This is because
humanshavemanuallydesignedmostarchitectures.Asaresult,thereisgrowinginterestinau-
tomated neural architecture search (NAS) methods [30], whereby automating the architecture
engineering aspect of machine learning. It is a growing branch of automatic machine learning
(AutoML)andautomaticdeeplearning(AutoDL)thatseekstooptimizetheprocessesaroundma-
chinelearning.Workhasbeendoneintheimagedomainspacewithneuralarchitecturesearchand
GANs [35]. This method, named AutoGAN, achieved highly competitive performance compared
tostate-of-the-arthuman-engineeredGANs.ThisisapromisingareafortimeseriesGANs;tothe
authors’knowledge,itisyetunexplored.
Asitstands,GANstendtobeapplicationspecific;theyperformwellfortheirintendedpurpose
butdonotgeneralizewellbeyondtheiroriginaldomain.Furthermore,amajorlimitationoftime
seriesGANsistherestrictionsplacedonthelengthofthesequencespecifiedthatthearchitecture
canmanage;documentedexperimentsvalidatinghowwellatimeseriesGANcanadapttovarying
data lengths are notably absent at the time of writing. However, glimpses of work in the NLP
literatureintheformofTransformers[96]havedemonstratedsomeapplicabilitytodealingwith
varyingsequencelengthsthatmayprovebeneficialinaddressingthisissueandmightemergein
timeseriesgenerationgiventime.
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

199:26 E.Brophyetal.
OtheraspectsnotinthescopeofthissurveyarticlebutimportanttonoteishowGANscandeal
with issues such as scalability and real-time data. Given its importance, we present some draft
ideasanddirecttheinterestedreadertofurtherresourcesforfull-stackmachinelearningingen-
eral.Thankfully,theemergingpracticeofmachinelearningoperations(MLOps)addressesmost
concernssurroundingretrainingmodelsoncereal-timedatabeginstodivergefromtheoriginal
dataset it was trained on [14, 94]. This can be applied to GANs, whereby the datasets encoun-
teredinproductioncanbedriventhroughametricprocesstoassessdivergencefromtheoriginal
dataandsubsequentdataforretraining,allowingforreliablemachinelearningsolutionsthatscale.
Foraparallelcomputingapproach,wewouldconsiderfederatedlearning,asreferencedpreviously,
whereyoucantraintheGANonsubsetsofthedataandcancombinethemodelsfollowingtraining.
9 CONCLUSION
This article reviews a niche but growing use of GANs for time series data based mainly around
architectural evolution and loss function variants. We see that each GAN provides application-
specificperformanceanddoesnotnecessarilygeneralisewelltootherapplications—forexample,
aGANforgeneratinghigh-qualityphysiologicaltimeseriesmaynotproducehigh-fidelityaudio
duetosomelimitationimposedbythearchitectureorlossfunction.Adetailedreviewoftheappli-
cationsoftimeseriesGANstoreal-worldproblemshasbeenprovided,alongwiththeirdatasets
andtheevaluationmetricsusedforeachdomain.AsstatedintheworkofWangetal.[100],GAN-
related research for time series lags that of computer vision both in terms of performance and
definedrulesforgeneralizationofmodels.Thisreviewhashighlightedtheopenchallengesinthis
areaandoffersdirectionsforfutureworkandtechnologicalinnovation,particularlyforthoseGAN
aspectsrelatedtoevaluation,privacy,anddecentralizedlearning.
REFERENCES
[1] MartínAbadi,H.BrendanMcMahan,AndyChu,IlyaMironov,LiZhang,IanGoodfellow,andKunalTalwar.2016.
Deeplearningwithdifferentialprivacy.InProceedingsoftheACMConferenceonComputerandCommunications
Security(CCS’16).308–318.https://doi.org/10.1145/2976749.2978318
[2] SherifM.Abdelfattah,GhodaiM.Abdelrahman,andMinWang.2018.AugmentingthesizeofEEGdatasetsusinggen-
erativeadversarialnetworks.InProceedingsofthe2018InternationalJointConferenceonNeuralNetworks(IJCNN’18).
IEEE,LosAlamitos,CA,1–6.https://doi.org/10.1109/IJCNN.2018.8489727
[3] HamedAlqahtani,ManolyaKavakli-Thorne,andGulshanKumar.2019.Applicationsofgenerativeadversarialnet-
works (GANs): An updated review. Archives of Computational Methods in Engineering 28 (Dec. 2019), 525–552.
https://doi.org/10.1007/s11831-019-09388-y
[4] MartinArjovsky,SoumithChintala,andLéonBottou.2017.WassersteinGAN.arXivpreprintarXiv:1701.07875.
[5] SeanAugenstein,H.BrendanMcMahan,DanielRamage,SwaroopRamaswamy,PeterKairouz,MingqingChen,Rajiv
Mathews,andBlaiseAguerayArcas.2020.GenerativemodelsforeffectiveMLonprivate,decentralizeddatasets.
arXiv:1911.06679[cs.LG].
[6] SamyBengio,OriolVinyals,NavdeepJaitly,andNoamShazeer.2015.Scheduledsamplingforsequenceprediction
withrecurrentneuralnetworks.arXiv:1506.03099[cs.LG].
[7] TimBollerslev.1986.Generalizedautoregressiveconditionalheteroskedasticity.JournalofEconometrics31,3(1986),
307–327.https://EconPapers.repec.org/RePEc:eee:econom:v:31:y:1986:i:3:p:307-327.
[8] AliBorji.2018.ProsandconsofGANevaluationmeasures.arXiv:1802.03446[cs.CV].
[9] AliBorji.2019.ProsandconsofGANevaluationmeasures.ComputerVisionandImageUnderstanding179(2019),
41–65.https://doi.org/10.1016/j.cviu.2018.10.009
[10] AliBorji.2021.ProsandconsofGANevaluationmeasures:Newdevelopments.arXiv:2103.09396[cs.LG].
[11] EoinBrophy.2020.SynthesisofdependentmultichannelECGusinggenerativeadversarialnetworks.InProceedings
ofthe29thACMInternationalConferenceonInformationandKnowledgeManagement(CIKM’20).ACM,NewYork,
NY,3229–3232.https://doi.org/10.1145/3340531.3418509
[12] EoinBrophy,ZhengweiWang,andTomasE.Ward.2019.Quickandeasytimeseriesgenerationwithestablished
image-basedGANs.arXiv:1902.05624[cs.LG].
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

GenerativeAdversarialNetworksinTimeSeries:ASystematicLiteratureReview 199:27
[13] FredB.BryantandPaulR.Yarnold.1995.Principal-componentsanalysisandexploratoryandconfirmatoryfactor
analysis.InReadingandUnderstandingMultivariateStatistics.AmericanPsychologicalAssociation,Washington,DC,
99–136.
[14] AndriyBurkov.2020.MachineLearningEngineering.TruePositiveInc.
[15] YuanyuanChen,YishengLv,andFei-YueWang.2020.Trafficflowimputationusingparalleldataandgenerative
adversarialnetworks.IEEETransactionsonIntelligentTransportationSystems21,4(April2020),1624–1630.https:
//doi.org/10.1109/TITS.2019.2910295
[16] Ping-SungCheng,Chieh-YingLai,Chun-ChiehChang,Shu-FenChiou,andYu-ChiehYang.2020.Avariantmodel
ofTGANformusicgeneration.InProceedingsofthe2020AsiaServiceSciencesandSoftwareEngineeringConference.
ACM,NewYork,NY,40–45.https://doi.org/10.1145/3399871.3399888
[17] EdwardChoi,SiddharthBiswal,BradleyMalin,JonDuke,WalterF.Stewart,andJimengSun.2017.Generatingmulti-
labeldiscretepatientrecordsusinggenerativeadversarialnetworks.arXiv:1703.06490.
[18] YejiChoi,HyunkiLim,HeeseungChoi,andIg-JaeKim.2020.GAN-basedanomalydetectionandlocalizationof
multivariatetimeseriesdataforpowerplant.InProceedingsofthe2020IEEEInternationalConferenceonBigDataand
SmartComputing(BigComp’20).IEEE,LosAlamitos,CA,71–74.https://doi.org/10.1109/BigComp48618.2020.00-97
[19] ChrisCulnane,BenjaminI.P.Rubinstein,andVanessaTeague.2017.Healthdatainanopenworld.arXiv:1712.05627.
[20] Hoang Anh Dau, Eamonn Keogh, Kaveh Kamgar, Chin-Chia Michael Yeh, Yan Zhu, Shaghayegh Gharghabi,
ChotiratAnnRatanamahatana,etal.2018.UCRTimeSeriesClassificationArchive.RetrievedSeptember7,2022
fromhttps://www.cs.ucr.edu/~eamonn/time_series_data_2018/.
[21] AnneMarieDelaney,EoinBrophy,andTomásE.Ward.2019.SynthesisofrealisticECGusinggenerativeadversarial
networks.arXiv:1909.09150.
[22] JiaDeng,WeiDong,RichardSocher,Li-JiaLi,KaiLi,andLiFei-Fei.2009.ImageNet:Alarge-scalehierarchicalimage
database.InProceedingsofthe2009IEEEConferenceonComputerVisionandPatternRecognition.IEEE,LosAlamitos,
CA,248–255.https://doi.org/10.1109/CVPR.2009.5206848
[23] PaoloDetti,GiampaoloVatti,andGaraziZabaloManriquedeLara.2020.EEGsynchronizationanalysisforseizure
prediction:Astudyondataofnoninvasiverecordings.Processes8,7(2020),846.https://doi.org/10.3390/pr8070846
[24] ChrisDonahue,JulianMcAuley,andMillerPuckette.2019.Adversarialaudiosynthesis.arXiv:1802.04208[cs.SD].
[25] GeorgDorffner.1996.Neuralnetworksfortimeseriesprocessing.NeuralNetworkWorld6(1996),447–468.
[26] DheeruDuaandCaseyGraff.2017.UCIMachineLearningRepository.RetreivedSeptember7,2022fromhttp://
archive.ics.uci.edu/ml.
[27] CynthiaDwork.2006.Differentialprivacy.InProceedingsofthe33rdInternationalConferenceonAutomata,Languages,
andProgramming—VolumePartII(ICALP’06).1–12.https://doi.org/10.1007/11787006_1
[28] CynthiaDworkandAaronRoth.2014.Thealgorithmicfoundationsofdifferentialprivacy.FoundationsandTrends
inTheoreticalComputerScience9,3–4(Aug.2014),211–407.https://doi.org/10.1561/0400000042
[29] KhaledElEmam,ElizabethJonker,LukArbuckle,andBradleyMalin.2011.Asystematicreviewofre-identification
attacksonhealthdata.PLoSOne6(2011),e28071.https://doi.org/10.1371/journal.pone.0028071
[30] ThomasElsken,JanHendrikMetzen,andFrankHutter.2019.Neuralarchitecturesearch:Asurvey.JournalofMa-
chineLearningResearch20,1(2019),1997–2017.
[31] CristóbalEsteban,StephanieL.Hyland,andGunnarRätsch.2017.Real-valued(medical)timeseriesgenerationwith
recurrentconditionalGANs.arXiv:1706.02633.
[32] European Union. 2018. Data Protection Act 2018 (Section36(2)). Retrieved September 7, 2022 from http://www.
irishstatutebook.ie/eli/2018/si/314/made/en/pdf.
[33] FatemehFahimi,ZhuoZhang,WooiBoonGoh,KaiKengAng,andCuntaiGuan.2019.TowardsEEGgeneration
usingGANsforBCIapplications.InProceedingsofthe2019IEEEEMBSInternationalConferenceonBiomedicaland
HealthInformatics(BHI’19).IEEE,LosAlamitos,CA,1–4.https://doi.org/10.1109/BHI.2019.8834503
[34] HongxiaoFeiandFengyunTan.2018.Bidirectionalgridlongshort-termmemory(BiGridLSTM):Amethodtoaddress
context-sensitivityandvanishinggradient.Algorithms11,11(2018),172.https://doi.org/10.3390/a11110172
[35] XinyuGong,ShiyuChang,YifanJiang,andZhangyangWang.2019.AutoGAN:Neuralarchitecturesearchforgen-
erativeadversarialnetworks.arXiv:1908.03835.
[36] LiangGonogandYiminZhou.2019.Areview:Generativeadversarialnetworks.InProceedingsofthe201914thIEEE
ConferenceonIndustrialElectronicsandApplications(ICIEA’19).IEEE,LosAlamitos,CA,505–510.https://doi.org/10.
1109/ICIEA.2019.8833686
[37] IanGoodfellow.2016.GenerativeAdversarialNetworksforText.RetrievedSeptember7,2022fromhttps://www.
reddit.com/r/MachineLearning/comments/40ldq6/generative_adversarial_networks_for_text/.
[38] IanGoodfellow,JeanPouget-Abadie,MehdiMirza,BingXu,DavidWarde-Farley,SherjilOzair,AaronCourville,and
YoshuaBengio.2014.Generativeadversarialnets.InAdvancesinNeuralInformationProcessingSystems,Z.Ghahra-
mani,M.Welling,C.Cortes,N.Lawrence,andK.Q.Weinberger(Eds.),Vol.27.CurranAssociates,Montréal,Canada.
https://proceedings.neurips.cc/paper/2014/file/5ca3e9b122f61f8f06494c97b1afccf3-Paper.pdf.
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

199:28 E.Brophyetal.
[39] ArthurGretton,KarstenM.Borgwardt,MalteJ.Rasch,BernhardSchölkopf,andAlexanderSmola.2012.Akernel
two-sampletest.JournalofMachineLearningResearch13(March2012),723–773.
[40] JieGui,ZhenanSun,YonggangWen,DachengTao,andJiepingYe.2020.Areviewongenerativeadversarialnetworks:
Algorithms,theory,andapplications.arXiv:2001.06937[cs.LG].
[41] JohnT.Guibas,TejpalS.Virdi,andPeterS.Li.2017.Syntheticmedicalimagesfromdualgenerativeadversarial
networks.arXiv:1709.01872.
[42] ZijianGuo,YimingWan,andHaoYe.2019.Adataimputationmethodformultivariatetimeseriesbasedongenerative
adversarialnetwork.Neurocomputing360(Sept.2019),185–197.https://doi.org/10.1016/j.neucom.2019.06.007
[43] LingyiHan,KanZheng,LongZhao,XianbinWang,andHuiminWen.2020.Content-awaretrafficdatacompletionin
ITSbasedongenerativeadversarialnets.IEEETransactionsonVehicularTechnology69,10(Oct.2020),11950–11962.
https://doi.org/10.1109/TVT.2020.3007025
[44] ShotaHarada,HideakiHayashi,andSeiichiUchida.2018.Biosignaldataaugmentationbasedongenerativeadver-
sarialnetworks.InProceedingsofthe201840thAnnualInternationalConferenceoftheIEEEEngineeringinMedicine
andBiologySociety(EMBC’18).IEEE,LosAlamitos,CA,368–371.https://doi.org/10.1109/EMBC.2018.8512396
[45] ShotaHarada,HideakiHayashi,andSeiichiUchida.2019.Biosignalgenerationandlatentvariableanalysiswith
recurrentgenerativeadversarialnetworks.IEEEAccess 7(2019),144292–144302.https://doi.org/10.1109/ACCESS.
2019.2934928
[46] CorentinHardy,ErwanLeMerrer,andBrunoSericola.2019.MD-GAN:Multi-discriminatorgenerativeadversarial
networksfordistributeddatasets.arXiv:1811.03850[cs.LG].
[47] KayGregorHartmann,RobinTiborSchirrmeister,andTonioBall.2018.EEG-GAN:Generativeadversarialnetworks
forelectroencephalograhic(EEG)brainsignals.arXiv:1806.01875.
[48] JamieHayes,LucaMelis,GeorgeDanezis,andEmilianoDeCristofaro.2019.LOGAN:Membershipinferenceattacks
againstgenerativemodels.ProceedingsonPrivacyEnhancingTechnologies2019,1(2019),133–152.https://doi.org/10.
2478/popets-2019-0008
[49] DebapriyaHazraandYung-CheolByun.2020.SynSigGAN:Generativeadversarialnetworksforsyntheticbiomedical
signalgeneration.Biology9,12(Dec.2020),441.https://doi.org/10.3390/biology9120441
[50] BorisP.Hejblum,GriffinM.Weber,KatherineP.Liao,NathanP.Palmer,SusanneChurchill,NancyA.Shadick,Peter
Szolovits,ShawnN.Murphy,IsaacS.Kohane,andTianxiCai.2019.Probabilisticrecordlinkageofde-identified
researchdatasetswithdiscrepanciesusingdiagnosiscodes.ScientificData6(2019),Article180298,11pages.https:
//doi.org/10.1038/sdata.2018.298
[51] MartinHeusel,HubertRamsauer,ThomasUnterthiner,BernhardNessler,andSeppHochreiter.2018.GANstrained
byatwotime-scaleupdateruleconvergetoalocalNashequilibrium.arXiv:1706.08500[cs.LG].
[52] R.DevonHjelm,AthulPaulJacob,TongChe,AdamTrischler,KyunghyunCho,andYoshuaBengio.2018.Boundary-
seekinggenerativeadversarialnetworks.arXiv:1702.08431[stat.ML].
[53] SeppHochreiterandJurgenSchmidhuber.1997.Longshort-termmemory.NeuralComputation9,8(1997),1735–1780.
https://doi.org/10.1162/neco.1997.9.8.1735
[54] DanielJiwoongIm,ChrisDongjooKim,HuiJiang,andRolandMemisevic.2016.Generatingimageswithrecurrent
adversarialnetworks.arXiv:1602.05110.
[55] Oxford-ManInstitute.2021.Oxford-ManInstituteofQuantitativeFinance:RealizedLibrary.RetrievedApril30,2021
fromhttps://realized.oxford-man.ox.ac.uk.
[56] AlistairE.W.Johnson,TomJ.Pollard,LuShen,LiWeiH.Lehman,MenglingFeng,MohammadGhassemi,Benjamin
Moody,PeterSzolovits,LeoAnthonyCeli,andRogerG.Mark.2016.MIMIC-III,afreelyaccessiblecriticalcare
database.ScientificData3(2016),160035.
[57] LauriJuvela,BajibabuBollepalli,JunichiYamagishi,andPaavoAlku.2019.Waveformgenerationfortext-to-speech
synthesisusingpitch-synchronousmulti-scalegenerativeadversarialnetworks.InProceedingsofthe2019IEEEIn-
ternationalConferenceonAcoustics,Speech,andSignalProcessing(ICASSP’19).IEEE,LosAlamitos,CA,6915–6919.
https://doi.org/10.1109/ICASSP.2019.8683271
[58] ShrutiKaushik,AbhinavChoudhury,SayeeNatarajan,LarryA.Pickett,andVarunDutt.2020.Medicineexpenditure
predictionviaavariance-basedgenerativeadversarialnetwork.IEEEAccess8(2020),110947–110958.https://doi.org/
10.1109/ACCESS.2020.3002346
[59] DaniKiyasseh,GirmawAbebeTadesse,LeNguyenThanhNhan,LeVanTan,LouiseThwaites,TingtingZhu,and
DavidClifton.2020.PlethAugment:GAN-basedPPGaugmentationformedicaldiagnosisinlow-resourcesettings.
IEEEJournalofBiomedicalandHealthInformatics24,11(Nov.2020),3226–3235.https://doi.org/10.1109/JBHI.2020.
2979608
[60] AntoninaKolokolova,MitchellBillard,RobertBishop,MoustafaElsisy,ZacharyNorthcott,LauraGraves,Vineel
Nagisetty,andHeatherPatey.2020.GANs&reels:CreatingIrishmusicusingagenerativeadversarialnetwork.
arXiv:2010.15772[cs.SD].
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

GenerativeAdversarialNetworksinTimeSeries:ASystematicLiteratureReview 199:29
[61] AlexKrizhevskyandGeoffreyHinton.2009.LearningMultipleLayersofFeaturesfromTinyImages.TechnicalReport.
UniversityofToronto,Toronto,Ontario.
[62] MirellaLapata.2015.EMNLP14.RetrievedApril30,2021fromhttp://homepages.inf.ed.ac.uk/mlap/Data/EMNLP14/.
[63] TeemaLeangarun,PojTangamchit,andSuttipongThajchayapong.2018.Stockpricemanipulationdetectionusing
generativeadversarialnetworks.InProceedingsofthe2018IEEESymposiumSeriesonComputationalIntelligence
(SSCI’18).IEEE,LosAlamitos,CA,2104–2111.https://doi.org/10.1109/SSCI.2018.8628777
[64] Y.LeCun,L.Bottou,Y.Bengio,andP.Haffner.Gradient-basedlearningappliedtodocumentrecognition.Proceedings
oftheIEEE86,11(1998),2278–2324.
[65] Christian Ledig, Lucas Theis, Ferenc Huszár, Jose Caballero, Andrew Cunningham, Alejandro Acosta, Andrew
Aitken,etal.2017.Photo-realisticsingleimagesuper-resolutionusingagenerativeadversarialnetwork.InPro-
ceedingsofthe30thIEEEConferenceonComputerVisionandPatternRecognition(CVPR’17).105–114.https://doi.org/
10.1109/CVPR.2017.19
[66] DanLi,DachengChen,BaihongJin,LeiShi,JonathanGoh,andSee-KiongNg.2019.MAD-GAN:Multivariateanom-
alydetectionfortimeseriesdatawithgenerativeadversarialnetworks.InArtificialNeuralNetworksandMachine
Learning—ICANN 2019: Text and Time Series. Lecture Notes in Computer Science, Vol. 11730.Springer, 703–716.
https://doi.org/10.1007/978-3-030-30490-4_56
[67] QingliangLi,HuibowenHao,YangZhao,QingtianGeng,GuangjieLiu,YuZhang,andFanhuaYu.2020.GANs-LSTM
modelforsoiltemperatureestimationfrommeteorological:Anewapproach.IEEEAccess8(2020),59427–59443.
https://doi.org/10.1109/ACCESS.2020.2982996
[68] YujiaLi,KevinSwersky,andRichardZemel.2015.Generativemomentmatchingnetworks.arXiv:1502.02761[cs.LG].
[69] FieteLuer,DominikMautz,andChristianBohm.2019.Anomalydetectionintimeseriesusinggenerativeadversarial
networks.InProceedingsofthe2019InternationalConferenceonDataMiningWorkshops(ICDMW’19).IEEE,Los
Alamitos,CA,1047–1048.https://doi.org/10.1109/ICDMW.2019.00152
[70] Yonghong Luo, Xiangrui Cai, Ying Zhang, Jun Xu, and Yuan Xiaojie. 2018. Multivariate time series imputation
withgenerativeadversarialnetworks.InAdvancesinNeuralInformationProcessingSystems,S.Bengio,H.Wallach,
H.Larochelle,K.Grauman,N.Cesa-Bianchi,andR.Garnett(Eds.),Vol.31.CurranAssociates,Montréal,Canada,
1596–1607.https://proceedings.neurips.cc/paper/2018/file/96b9bff013acedfb1d140579e2fbeb63-Paper.pdf.
[71] YonghongLuo,YingZhang,XiangruiCai,andXiaojieYuan.2019.E2GAN:End-to-endgenerativeadversarialnet-
workformultivariatetimeseriesimputation.InProceedingsofthe28thInternationalJointConferenceonArtificial
Intelligence.3094–3100.https://doi.org/10.24963/ijcai.2019/429
[72] B.MalinandL.Sweeney.2001.Re-identificationofDNAthroughanautomatedlinkageprocess.InProceedingsof
theAMIASymposium.423–427.https://pubmed.ncbi.nlm.nih.gov/11825223.
[73] H. Brendan McMahan, Eider Moore, Daniel Ramage, Seth Hampson, and Blaise Agüera y Arcas. 2017.
Communication-efficientlearningofdeepnetworksfromdecentralizeddata.arXiv:1602.05629[cs.LG].
[74] Olof Mogren. 2016. C-RNN-GAN: Continuous recurrent neural networks with adversarial training.
arXiv:1611.09904[cs.AI].
[75] G.B.MoodyandR.G.Mark.2001.TheimpactoftheMIT-BIHarrhythmiadatabase.IEEEEngineeringinMedicine
andBiologyMagazine20,3(2001),45–50.https://doi.org/10.1109/51.932724
[76] HaoNi,LukaszSzpruch,MagnusWiese,ShujianLiao,andBaorenXiao.2020.ConditionalSig-WassersteinGANs
fortimeseriesgeneration.arXiv:2006.05421[cs.LG].
[77] KonstantinosNikolaidis,SteinKristiansen,VeraGoebel,ThomasPlagemann,KnutLiestøl,andMohanKankanhalli.
2019.Augmentingphysiologicaltimeseriesdata:Acasestudyforsleepapneadetection.arXiv:1905.09068[cs.LG].
[78] S.J.PanandQ.Yang.2010.Asurveyontransferlearning.IEEETransactionsonKnowledgeandDataEngineering22,
10(2010),1345–1359.https://doi.org/10.1109/TKDE.2009.191
[79] KishorePapineni,SalimRoukos,ToddWard,andWei-JingZhu.2002.Bleu:Amethodforautomaticevaluationof
machinetranslation.InProceedingsofthe40thAnnualMeetingoftheAssociationforComputationalLinguistics.311–
318.https://doi.org/10.3115/1073083.1073135
[80] DhasarathyParthasarathy,KarlBäckström,JensHenriksson,andSólrúnEinarsdóttir.2020.Controlledtimeseries
generationforautomotivesoftware-in-the-looptestingusingGANs.arXiv:2002.06611[cs.LG].
[81] DamianPascual,AlirezaAmirshahi,AmirAminifar,DavidAtienza,PhilippeRyvlin,andRogerWattenhofer.2020.
EpilepsyGAN:Syntheticepilepticbrainactivitieswithprivacypreservation.IEEETransactionsonBiomedicalEngi-
neering67(2020),1.https://doi.org/10.1109/TBME.2020.3042574
[82] Marco A. F. Pimentel, Alistair E. W. Johnson, Peter H. Charlton, Drew Birrenkott, Peter J. Watkinson, Lionel
Tarassenko,andDavidA.Clifton.2017.Towardarobustestimationofrespiratoryratefrompulseoximeters.IEEE
TransactionsonBiomedicalEngineering64,8(2017),1914–1923.https://doi.org/10.1109/TBME.2016.2613124
[83] TomJ.Pollard,AlistairE.W.Johnson,JesseD.Raffa,LeoA.Celi,RogerG.Mark,andOmarBadawi.2018.TheeICU
CollaborativeResearchDatabase,afreelyavailablemulti-centerdatabaseforcriticalcareresearch.ScientificData5,
1(Sept.2018),180178.https://doi.org/10.1038/sdata.2018.178
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

199:30 E.Brophyetal.
[84] FumingQu,JinhaiLiu,YanjuanMa,DongZang,andMingruiFu.2020.Anovelwindturbinedataimputationmethod
withmultipleoptimizationsbasedonGANs.MechanicalSystemsandSignalProcessing139(May2020),106610.https:
//doi.org/10.1016/j.ymssp.2019.106610
[85] AlecRadford,LukeMetz,andSoumithChintala.2015.Unsupervisedrepresentationlearningwithdeepconvolutional
generativeadversarialnetworks.arXiv:1511.06434.
[86] MohammadRasouli,TaoSun,andRamRajagopal.2020.FedGAN:Federatedgenerativeadversarialnetworksfor
distributeddata.arXiv:2006.07228[cs.LG].
[87] ScottReed,ZeynepAkata,XinchenYan,LajanugenLogeswaran,BerntSchiele,andHonglakLee.2016.Generative
adversarialtexttoimagesynthesis.InProceedingsofthe33rdInternationalConferenceonMachineLearning,M.F.
BalcanandK.Q.Weinberger(Eds.).PMLR,NewYork,NY,1681–1690.
[88] TimSalimans,IanGoodfellow,WojciechZaremba,VickiCheung,AlecRadford,XiChen,andXiChen.2016.Im-
provedtechniquesfortrainingGANs.InAdvancesinNeuralInformationProcessingSystems,D.Lee,M.Sugiyama,
U. Luxburg, I. Guyon, and R. Garnett (Eds.), Vol. 29. Curran Associates, Barcelona, Spain, 2234–2242. https://
proceedings.neurips.cc/paper/2016/file/8a3363abe792db2d8761d6403605aeb7-Paper.pdf.
[89] RezaShokri,MarcoStronati,CongzhengSong,andVitalyShmatikov.2017.Membershipinferenceattacksagainst
machinelearningmodels.arXiv:1610.05820[cs.CR].
[90] YukiSumiya,KazumasaHorie,HiroakiShiokawa,andHiroyukiKitagawa.2019.NR-GAN:NoisereductionGANfor
miceelectroencephalogramsignals.InProceedingsofthe20194thInternationalConferenceonBiomedicalImaging,
SignalProcessing.ACM,NewYork,NY,94–101.https://doi.org/10.1145/3366174.3366186
[91] HeSun,ZhunDeng,HuiChen,andDavidC.Parkes.2020.Decision-awareconditionalGANsfortimeseriesdata.
arXiv:2009.12682[cs.LG].
[92] YuqiangSun,LeiPeng,HuiyunLi,andMinSun.2018.Explorationonspatiotemporaldatarepairingofparkinglots
basedonrecurrentGANs.InProceedingsofthe201821stInternationalConferenceonIntelligentTransportationSystems
(ITSC’18).IEEE,LosAlamitos,CA,467–472.https://doi.org/10.1109/ITSC.2018.8569319
[93] DougalJ.Sutherland,Hsiao-YuTung,HeikoStrathmann,SoumyajitDe,AadityaRamdas,AlexSmola,andArthur
Gretton.2016.Generativemodelsandmodelcriticismviaoptimizedmaximummeandiscrepancy.arXiv:1611.04488.
[94] MarkTreveilandDataikuTeam.2020.IntroducingMLOps.O’Reilly.
[95] LaurensvanderMaatenandGeoffreyHinton.2008.Visualizingdatausingt-SNE. JournalofMachineLearning
Research9,86(2008),2579–2605.http://jmlr.org/papers/v9/vandermaaten08a.html.
[96] AshishVaswani,NoamShazeer,NikiParmar,JakobUszkoreit,LlionJones,AidanN.Gomez,ŁukaszKaiser,andIllia
Polosukhin.2017.Attentionisallyouneed.InProceedingsofthe31stInternationalConferenceonNeuralInformation
ProcessingSystems(NIPS’17).CurranAssociatesInc.,RedHook,NY,USA,6000–6010.
[97] Lu Wang, Wei Zhang, and Xiaofeng He. 2019. Continuous patient-centric sequence generation via sequentially
coupledadversariallearning.InDatabaseSystemsforAdvancedApplications,GuoliangLi,JunYang,JoaoGama,
JuggapongNatwichai,andYongxinTong(Eds.).SpringerInternational,Cham,Switzerland,36–52.
[98] ZhengweiWang,GrahamHealy,AlanF.Smeaton,andTomasE.Ward.2020.Useofneuralsignalstoevaluatethe
qualityofgenerativeadversarialnetworkperformanceinfacialimagegeneration.CognitiveComputation12,1(2020),
13–24.
[99] ZhengweiWang,QiShe,AlanF.Smeaton,TomasE.Ward,andGrahamHealy.2020.Synthetic-neuroscore:Usinga
neuro-AIinterfaceforevaluatinggenerativeadversarialnetworks.Neurocomputing405(2020),26–36.
[100] ZhengweiWang,QiShe,andTomásE.Ward.2021.Generativeadversarialnetworksincomputervision:Asurvey
andtaxonomy.ACMComputingSurveys54,2(2021),1–38.
[101] MagnusWiese,RobertKnobloch,RalfKorn,andPeterKretschmer.2020.QuantGANs:Deepgenerationoffinancial
timeseries.QuantitativeFinance20,9(Sept.2020),1419–1440.https://doi.org/10.1080/14697688.2020.1730426arXiv:
1907.06673
[102] SamimWiniger.2015.ObamaPoliticalSpeechGenerator—RecurrentNeuralNetwork.RetrievedApril30,2021from
https://github.com/samim23/obama-rnn.
[103] LiyangXie,KaixiangLin,ShuWang,FeiWang,andJiayuZhou.2018.Differentiallyprivategenerativeadversarial
network.arXiv:1802.06739.
[104] L.YiandM.Mak.2019.Adversarialdataaugmentationnetworkforspeechemotionrecognition.InProceedingsof
the2019Asia-PacificSignalandInformationProcessingAssociationAnnualSummitandConference(APSIPAASC’19).
IEEE,LosAlamitos,CA,529–534.https://doi.org/10.1109/APSIPAASC47483.2019.9023347
[105] XinYi,EktaWalia,andPaulBabyn.2019.Generativeadversarialnetworkinmedicalimaging:Areview.Medical
ImageAnalysis58(2019),101552.https://doi.org/10.1016/j.media.2019.101552
[106] ChikaYinka-BanjoandOgban-AsuquoUgot.2020.Areviewofgenerativeadversarialnetworksanditsapplication
in cybersecurity. Artificial Intelligence Review 53, 3 (March 2020), 1721–1736. https://doi.org/10.1007/s10462-019-
09717-4
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.

GenerativeAdversarialNetworksinTimeSeries:ASystematicLiteratureReview 199:31
[107] JinsungYoon,DanielJarrett,andMihaelavanderSchaar.2019.Time-seriesgenerativeadversarialnetworks.In
AdvancesinNeuralInformationProcessingSystems,H.Wallach,H.Larochelle,A.Beygelzimer,F.d’Alché-Buc,E.Fox,
andR.Garnett(Eds.),Vol.32.CurranAssociates,Vancouver,Canada,5508–5518.https://proceedings.neurips.cc/
paper/2019/file/c9efe5f26cd17ba6216bbe2a7d26d490-Paper.pdf.
[108] LantaoYu,WeinanZhang,JunWang,andYongYu.2017.SeqGAN:Sequencegenerativeadversarialnetswithpolicy
gradient.InProceedingsofthe31stAAAIConferenceonArtificialIntelligence(AAAI’17).2852–2858.
[109] HuiZhang,NiannaoXiao,PeishunLiu,ZhichengWang,andRuichunTang.2020.G-RNN-GANforsingingvoice
separation.InProceedingsofthe20205thInternationalConferenceonMultimediaSystemsandSignalProcessing.ACM,
NewYork,NY,69–73.https://doi.org/10.1145/3404716.3404718
[110] ZixingZhang,JingHan,KunQian,ChristophJanott,YananGuo,andBjoernSchuller.2019.Snore-GANs:Improving
automaticsnoresoundclassificationwithsynthesizeddata.arXiv:1903.12422[cs.LG].
[111] FeiZhu,FeiYe,YuchenFu,QuanLiu,andBairongShen.2019.Electrocardiogramgenerationwithabidirectional
LSTM-CNNgenerativeadversarialnetwork.ScientificReports9,1(2019),Article6734,11pages.https://doi.org/10.
1038/s41598-019-42516-z
[112] Guangxuan Zhu, Hongbo Zhao, Haoqiang Liu, and Hua Sun. 2019. A novel LSTM-GAN algorithm for time se-
riesanomalydetection.InProceedings ofthe2019PrognosticsandSystemHealthManagementConference(PHM-
Qingdao’19).IEEE,LosAlamitos,CA,1–6.
Received18June2021;revised12August2022;accepted21August2022
ACMComputingSurveys,Vol.55,No.10,Article199.Publicationdate:February2023.