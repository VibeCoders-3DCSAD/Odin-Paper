| Using | Item | Personality-Based |     | Profiling | in Music | Recommender |
| ----- | ---- | ----------------- | --- | --------- | -------- | ----------- |
Systems
|                     | JoeldeGoma      |     | JanNielsenAnonuevo  |            |     | GianNicolePangan    |
| ------------------- | --------------- | --- | ------------------- | ---------- | --- | ------------------- |
| SCHOOLOFINFORMATION |                 |     | SCHOOLOFINFORMATION |            |     | SCHOOLOFINFORMATION |
|                     | TECHNOLOGY      |     |                     | TECHNOLOGY |     | TECHNOLOGY          |
|                     | MapuaUniversity |     | MapuaUniversity     |            |     | MapuaUniversity     |
Makati,MetroManila,Philippines Makati,MetroManila,Philippines Makati,MetroManila,Philippines
jcdegoma@mapua.edu.ph jndanonuevo@mymail.mapua.edu.ph gnlpangan@mymail.mapua.edu.ph
|     |     | JohnJovanielDeang             |     |                     | AlbertoVillaluz |     |
| --- | --- | ----------------------------- | --- | ------------------- | --------------- | --- |
|     |     | DepartmentofPhysicalEducation |     | SCHOOLOFINFORMATION |                 |     |
andAthletics TECHNOLOGY
|          |     | MapuaUniversity                |     |                                | MapuaUniversity |     |
| -------- | --- | ------------------------------ | --- | ------------------------------ | --------------- | --- |
|          |     | Makati,MetroManila,Philippines |     | Makati,MetroManila,Philippines |                 |     |
|          |     | jjcdeang@mapua.edu.ph          |     | acvillaluz@mapua.edu.ph        |                 |     |
| Abstract |     |                                |     | 1 Introduction                 |                 |     |
Musicrecommendersystemsplayanessentialroleingivingmusic Withtheincreasingadoptionofmusicsubscriptionserviceswithin
suggestionsinaccordancetoauser’sliking.However,therearetwo thecommunity,recommendersystemsplayacrucialroleinsuggest-
commonproblemswithregardstorecommendationalgorithms, ingsongsthatalignwiththeuser’sinterests. However,addressing
namelyuservariabilityandthecoldstartproblem. Withthis,the uservariabilityandovercomingthecold-startproblempresents
researchers aim to address the said problems by incorporating significantchallengesfortraditionalrecommendationalgorithms.
personality profiles to aid in giving music recommendations in Users’musicpreferencescanbediverseandmultifaceted,makingit
accordancetoauser’sinterests.ThestudymadeuseoftheLightFM difficultforthesealgorithmstoaccuratelycapturetheirpreferences
| Modeltoincorporatetheuser’stopfivefavoritegenresandbig |     |     |     | [1]. |     |     |
| ------------------------------------------------------ | --- | --- | --- | ---- | --- | --- |
fivepersonalityscores,henceusingahybridapproach.Thehybrid Theresearcherswillfocusontheeffectivenessofproportion-
modelisthencomparedwiththetraditionalcollaborativefiltering basedIPPstowardspersonality-basedmusicrecommendersystems.
modelwithcertainmetricstodetermineitsperformance.According ThecurrentstudybyAlharthifocusesontheuseoftherecom-
totheresults, thehybridmodeloutperformsthetraditionalCF mendersystemsingeneral,andwiththis,theresearchersintend
model,provingthatincorporatingpersonalityprofilescanimprove toapplythesaidapproachtomusicrecommendersystems[2].[3]
theaccuracyofthemodelingivingmusicsuggestionstoauser. suggeststhatitem-basedrecommendersystemsperformbetterin
termsofrating-basedCFrecommendersystems.Referencingthe
CCSConcepts saidstudy,theresearchersintendtoexploremoreonitem-based
recommendersystems.
•ComputingMethodologies;•Machinelearning;•Machine
Asthestudywillrevolvearoundtheuseofpersonality-based
learningapproaches;•Neuralnetworks;
musicrecommendationsystems,certaingapsareintendedtobe
addressed.Onlyafewstudieshaveexploredtheuseofpersonality-
Keywords
basedmusicrecommendersystemsasmostresearchwouldfocus
RecommenderSystems,CollaborativeFiltering,LightFM
|     |     |     |     | onmoodandemotion. |     | Lisuggeststhatpersonalityisoneofthe |
| --- | --- | --- | --- | ----------------- | --- | ----------------------------------- |
factorsthatdeterminesone’smusicalpreferences,besidesmood
ACMReferenceFormat:
andemotion[3].Withthis,theresearchersintendtoaddressthe
JoeldeGoma,JanNielsenAnonuevo,GianNicolePangan,JohnJovaniel
gapspresentedbythepersonality-basedrecommendersystemand
Deang,andAlbertoVillaluz.2025.UsingItemPersonality-BasedProfiling
inMusicRecommenderSystems. In2025The7thWorldSymposiumon thatisitsissueswithitsaccuracy. Researcherstendtoaddress
SoftwareEngineering(WSSE2025),October24–26,2025,Okayama,Japan. thisproblembyintegratingthesystemwithcurrentcollaborative
ACM,NewYork,NY,USA,7pages.https://doi.org/10.1145/3779657.3779698 filteringmethods. [1]foundthathavingaBigFivepersonality-
basedmusicrecommendationsystemhadcertainpersonalitybiases
thatmadetheresultsirrelevant.Withthis,theresearchersintendto
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor proposeanewapproachregardingpersonality-basedrecommender
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
systemsthatusetheBigFivemodel.AsAlharthi’sstudyproduces
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation
onthefirstpage.Copyrightsforthird-partycomponentsofthisworkmustbehonored. promisingresults,theresearchersbelievethatthesaidstudycan
Forallotheruses,contacttheowner/author(s). beincorporatedwithmusicrecommendersystemsusingtheBig
WSSE2025,Okayama,Japan
Fivepersonalitymodelwhichcouldlessenerrorsposedusingthe
©2025Copyrightheldbytheowner/author(s).
BigFivemodel.
ACMISBN979-8-4007-1577-8/2025/10
https://doi.org/10.1145/3779657.3779698
271

WSSE2025,October24–26,2025,Okayama,Japan JoeldeGomaetal.
2 ReviewofRelatedLiterature accuracyscoresofstate-of-the-artrecommendationalgorithmsand
Manyrecentstudiesinsentimentanalysisgavesignificantriseto exploresuserbiasrelatedtopersonalitytraits.Themethodologyin-
MachineLearningalgorithms.Whiletherehasbeenmuchresearch volvesdatacleaning,personalityestimation,anddatasegmentation
onTraditionalMachineLearningmodelsspecificallyontheOnline fortrackandartistinformationextraction. SparseLinearMeth-
Learningdataset,onlyafewstudieshavetakenintoconsideration ods,EmbarrassinglyShallowAutoencoders(EASE),andVariational
DeepLearningmodels.Thishasbeenattributedtotheexceptional Autoencoders(Mult-VAE)areutilizedforanalysis. Thereported
accuracyoftraditionalmodels. recallvaluesatdifferentpositions(5,10,and15)provideinsights
Lu&Tintarev’sstudyfocusesonaddressingthecold-startprob- intoalgorithmperformancebasedonusers’personalitytraits.For
lemamongstrecommendersystems.Withthis,theirpaperfocuses instance,atRecall@5,EASEachieved0.0366,SLIMachieved0.0334,
ongivingbetterrecommendationsbyre-rankingthesuggestions andMult-VAEachieved0.0433. Theseratesindicatethepropor-
bytherecommenderandimprovingtheaccuracyofthemodelby tionofrelevantitemsretrievedbythealgorithmsatthespecified
integrationofpersonalitytraits. Theirresultssuggestedthatthe positions.Thestudyrecognizesitslimitations,suchasgeneraliz-
saidfocuspointsofthepaperhavebeenmet,whereinpersonalized abilityanddatacompletenessissues,andoutlinesfutureresearch
recommendationlistsarehigherindiversityandleadtoanincrease directionstobetterunderstandthecausesofbiasesandexplore
inusersatisfaction[4]. additionalaspectsofrecommendationqualitybeyondaccuracy.
Klecetal’sstudiedhowpersonalitytraitscanhaveaninfluence Delando&et.al.[7]iscenteredaroundtheMBTI,utilizingthe
onmusicrecommendationerror. Thestudycollectedresponses MARSYASDatasetalongwiththeExtendedandSDatasets,the
from279participantstogathertheirlisteningtraitsandtheirper- studyaimstopredictpersonalitytraits,specificallyextraversion
sonality profiles. With this data, the combination between the and introversion, based on individuals’ music preferences. The
personalitytraitsandtheaudiofeaturesfromthesongswerestud- methodologyinvolvesdatacollection,dimensionalityreduction,
iedtoarriveataconclusionwithregardstomusicrecommendation normalization,andsegmentationbasedon”PersonalityType.”Au-
error.Findingssuggestedthatsomepersonalityfacetshadyielded dioframesaresegmented,andfeaturesareextractedusingMIRtool-
thelowestrecommendationerrorforBFI-2,comparedtothehigher boxandavariationalautoencoder.SupportVectorMachine(SVM),
orderofthebigfivepersonalitytraits. Theresearchershadcon- RandomForest,K-NearestNeighbors(KNN),andNaiveBayesclas-
cludedthatthisdiscoverycanhelpotherresearcherstofilterthe sifiersareemployedforanalysis. TheSVMclassifierachievesa
personalityquestionnairedowntoonlytheessentialquestionsto performancerateof71%,showcasingitseffectivenessinpredicting
beusedingatheringthepersonalityprofilesoftheuserstopredict personalitytraitsbasedonmusicpreferences. Furthermore,the
theirlisteninghabits[1]. studyexploresthecorrelationbetweenmusicgenresandperson-
Garg&et. al. [5]focusesondevelopingamusicmood-based alitytypes,revealingascoringdistributionof53%forextraverts
recommendationsystemusingmachinelearninganddeeplearning and47%forintroverts,sheddinglightonthenuancedrelationship
techniques,withaparticularemphasisonaddressingthecommon betweenmusicpreferencesandpersonalitytraits.
strugglepeoplefaceinfindingmusicthatmatchestheirmoodor Dorochowicz[8]isfocusedonexploringemotionsandphysiolog-
emotions. TheresearchutilizestheFERPlusdatasetandSpotipy, icalsignals,utilizedtheDEAMandPMEmodatasetstoinvestigate
aPythonlibraryforSpotify,forwebscrapinganddatamanipula- theintricaterelationshipbetweenmusicandhumanemotions.The
tion.TheValence-Arousaltheoryisemployedtoclassifythesong researchaimedtoquantifythisconnectionanddevelopamachine
databaseintomoodquadrants,andK-Meansclusteringisusedfor learningmodelcapableofpredictingbothmusicmoodbasedon
furthercategorization.Featuressuchasvalence,energy,danceabil- audiosignalsandhumanemotionbasedonphysiologicalsignals.
ity,loudness,tempo,speechiness,instrumentalness,andpopularity Themethodologyinvolveddownscaling,formatconversion,reg-
areconsidered. ADeepConvolutionalNeuralNetwork(CNN)is ularization,andshrinkage,withfeatureextractionencompassing
employedforclassification,withvaryingaccuraciesreportedfor zero-crossingrate,energy,entropyofenergy,andvariousspectral
differentmodelsandemotions.Themodelaimstoproviderealtime features.Machinelearningmodels,suchasSVM,RandomForest,
playlistrecommendationsbasedonmood,contributingtomood DecisionTree,ExtraTree,k-NN,MLP,AdaBoost,ElasticNet,Ridge,
enhancementthroughAI-drivensongselection. Thestudysug- Lasso,andAdaptiveBoost,wereemployedforanalysis. ANOVA
geststhatthismethodsurpassesgenreclassificationinaccuracy, resultsindicatedsignificantvariancebetweenpeopleanditems,
withpotentialapplicationsinimprovingsocialnetworkingand emphasizingindividualizedemotionalresponsestomusic.TheRan-
customersatisfaction. Thereportedaccuracypercentagesinclude domForestmodeldemonstratednotableperformanceintermsof
below65%foraSimpleCNNwithsixemotions,above70%fora actioncallcountandtrainingtime.Thearousalandvalenceanaly-
SimpleCNNwithfouremotions,below72%foraDeepCNNwith sisrevealeddistinctemotionalresponsesassociatedwithdifferent
sixemotions,andabout80%foraDeepCNNwithfouremotions. musicmoods.Theresearchachievedanaccuracyrateof81%,un-
Losspercentages,basedon60%trainingdataand50%validation derscoringthepracticalpotentialofthedevelopedmodel,including
data,decreaseto30%orbelowasthenumberofepochsincreases personalizedplaylistgeneration.However,thestudyacknowledged
forbothtrainingandvalidationdata. theneedforfurtherresearchandrefinementtoenhanceaccuracy
Joy & et. al. [6] is rooted in the Big Five Model, leverages andbroadenthescopeofemotionrecognition.
dataobtainedfromTwitter,encompassing395,056listeningevents, Liu&et.al.[9]utilizesadatasetfromthemyPersonalityweb-
18,310userswithpersonalityvalues,and15,753uniquetracks.The site,aimedtodevelopanalgorithmtodetermineindividuals’music
researchinvestigateshowusers’personalitytraitsinfluencethe tastesbasedontheirpersonalitytraits.Theapproachinvolvedcon-
vertingFacebookstatusupdatesintovectorrepresentation.Various
272

UsingItemPersonality-BasedProfilinginMusicRecommenderSystems WSSE2025,October24–26,2025,Okayama,Japan
Figure1:ProposedModelWorkflow
recommendationmodels,includingNaiveBayesClassifierandcol- 3.1 DataCollection
laborativefilteringmethods,wereemployed.Therecommendation Thedatacollectionprocesswillbeconductedintheformofasurvey.
model’sperformancewasassessedusingRootMeanSquaredError Thesurveywillbeusedfortheexplicitgatheringoftheinformation
(RMSE),withMatrixFactorizationachievingthelowestRMSEat requiredforbuildingthethreematrices(user,item,interaction)that
0.88. F-MeasuresforBigFivePersonalityClasses,includingOpen- willbeusedfortheLightFMHybridModel.Thequestionnairewill
ness (0.2308), Conscientiousness (0.4865), Extraversion (0.6349), haveacombinedtotalof111questionsconsistingofthe10-item
Agreeableness(0.5000), andNeuroticism(0.6154), werealsocal- BFIQuestionnaire(LikertScaleof1–5),100-itemSongRating(1as
culated. Therecommendationmodeloutperformeduser-to-user like,0asdislike),andPreferredGenreChecklist(10genreoptions,
collaborativefilteringwitharatingmatrix,althoughmatrixfac- choosingamaximumof5).
torizationremainedsuperior. Thestudyprovidedinsightsintothe
relationshipbetweenpersonalitytraitsandmusicpreferences,em-
phasizingthepotentialofpersonalizedrecommendationsystems.
Lu & et. al. [10] utilizes the myPersonality dataset and the
3.2 DATAPRE-PROCESSING
PsychoFlickrdataset,focusedondevelopinganemotionalrecom-
mendersystemthatpredictsmusictastebasedonpersonalitytraits. 3.2.1 UserPersonalityProfile. Therespondents’answerstothe
Theuserrecognitionproblemswerecategorizedintofivebinary BigFiveInventory(BFI)willthenundergoamulti-stepprocess
classificationsandfurtherdividedintoclasses(low,medium,high). withonlytheresultingT-scorebeingstoredinthedataset. First,
ForwardFeaturesSelectionwith10-foldcross-validationwasem- rawscoresarecalculatedforeachofthefivecoredimensions(Ex-
ployed, and various classifiers, including Naive Bayes, Logistic traversion,Neuroticism,Agreeableness,Conscientiousness,and
Regression,SVM,RandomForest,andGBTwithdeepnetworks, Openness)bysumminganindividual’sresponsestotherelevant
wereused.TheaccuracyresultsforthemyPersonalitydatasetusing questionnaireitems. Theserawscoresarethentransformedinto
theproposedapproachwereO-0.71,C-0.72,E-0.75,A-0.73, thevariable“userBFdimensionmean”whichisusedtocontrol
N-0.71.Theself-assessedaccuracyresultsforthemyPersonality forpotentialdiscrepanciesinquestiondifficultyandestablishesa
datasetwerelower(O-0.54,C-0.55,E-0.54,A-0.54,N-0.54).For standardizedbaselineforcomparison.Thisiscomputedbydividing
thePsychoFlickrdataset,theproposedapproachachievedaccura- theitemscoresbythenumberofquestionsassociatedwitheach
ciesofO-0.61,C-0.59,E-0.56,A-0.60,N-0.61.Theself-assessed dimension.FollowingthecalculationofuserBFdimensionmeans,
accuracyresultswereagainO-0.54,C-0.55,E-0.54,A-0.54, theBFIemploysstandardizationprocedurestofacilitatemeaning-
N-0.54.Theexperimentsdemonstratedthesuccessofusinguser fulcomparisonsacrossindividualsandpopulations.Z-scoresare
personalityformoodrecognitioninpredictingmusictaste,urging derivedtorepresentthedeviationofanindividual’sscorefromthe
furtherexplorationinthisfield. averagepopulationscoreforaspecifictrait,expressedintermsof
standarddeviations.Finally,forenhancedinterpretability,Z-scores
areconvertedintoT-scoreswithameanof50andastandarddevi-
ationof10.Thiswillresultin5T-scores,whichwillbeconverted
intodegreestocategoricallyrepresenttheuser’spersonalityprofile.
ABFscoreisstoredas“high”ifitisgreaterthan55,“low”ifitis
3 Methodology
lowerthan45,oraverageotherwiseasdemonstratedinTable1.
Asshowninfigure1theprocedureindevelopingandevaluating ThiswillberepresentedintheappropriateformatshowninTable
themodel. 2tomakeitcompatibleasauser-featureembedding.
273

WSSE2025,October24–26,2025,Okayama,Japan JoeldeGomaetal.
3.2.2 Item Features. The researchers will incorporate the whichofthetwolossfunctions(BPRandWARP)willperformbet-
proportion-basedIPPmethodusedin[2]wheretheitempersonal- teronofflineevaluationbeforefinalizingthemodeltobeevaluated
ityprofileisrepresentedinvectorform,consistingof15features. bynewusers. Thesetwolossfunctionswerechosenforevaluation
Eachdimensionisrepresentedbythreefeaturesthatcorrespond sincebothareparticularlyusefulincaseswhereonlypositiveinter-
to degrees (low, average, and high) The value of one feature is actions(likes)arerecordedbutwithdifferentoptimizations.WARP
theproportionofuserswholikeaniteminthedegreeofoneBF issuitedforoptimizingthetoprecommendationlist,whileBPRis
dimensionwhichiscalculatedbasedonthefollowingformula: moresuitedforoptimizingtheAUCscore.Formodelevaluation,
Proportion=(totalNumberofUserswholikedtheItemandhas thekvalueissetto10toevaluateitsperformancewhengenerating
thesameBFdegree)/(totalNumberofUserswhoLikedtheItem). thetop10recommendations.
SpotifyAPIwillbeusedtoextractcontent-basedfeaturestobe
usedalongsidetheitempersonalityprofileasitemfeatureweights. 3.4 ModelValidationandEvaluation
Insteadofthemusicalandthestandardfeatures(bpm,tempo,re-
Theresearcherswillusethebuilt-inevaluationmetricsprovided
leasedate,volume)thatarecommonlycoveredinexistingstudies,
bytheLightFMlibrary. Thesemetricscanbecollectivelyusedto
thestudywillfocusonextractingthefollowingsonicalcomponents
assessthemodel’sperformancebycomputingtheseforthetraining
orfeaturesthatquantitativelydescribeaspectsthatcontributeto
andtestsplitoftheinteraction’smatrix.Themetricstobeusedwill
theoverallsoundandmoodofthesong,whichareAcousticness,
betheROCAUCScore,Precision,Recall,andF1-score.ROCAUC
Danceability,Energy,Instrumentalness,Liveness,andValence.
Scorequantifiestheprobabilitythatarandomlyselectedpositive
examplewillhaveahigherscorethanarandomlychosennegative
3.2.3 Interaction Matrix. The interactions matrix will store
example. Itmeasuresthemodel’sabilitytorankpositiveexamples
recordedinteractionsforallusers.Thiswillcomprisethreecolumns,
higherthannegativeexamples.Aperfectscoreis1.0,indicatingop-
twoofwhichareforeignkeysthatlinktoboththeuserfeatures
timalperformanceindistinguishingbetweenpositiveandnegative
matrix(UserID)andsongfeaturesmatrix(songID).TheisLiked
examples. Precisionatkmeasuresthefractionofrelevantitems
columnisusedtorepresentinteractionsaseither1or0.Toaccount
amongthetopkitemsrecommendedbythesystem.Itevaluatesthe
forthedifferencesbetweenthewayinteractionsarestoredinthe
precisionoftherecommendationsbyconsideringhowmanyofthe
surveydatasetandtheMillionSongDataset(MDS),anadditional
toprecommendationsarerelevanttotheuser.Aperfectscoreis1.0,
column Weight will be used as an additional feature for model
indicatingthatalltopkrecommendationsarerelevanttotheuser’s
training,assigningdifferentlevelsofimportancedependingonthe
preferences. Recallatkevaluatesthesystem’sabilitytoretrieve
valueofaspecificinteraction. AllinteractionsfromtheMapuan
allrelevantitemsamongthetopkrecommendations. Itmeasures
studentswillautomaticallybeassignedthehighestvalue(5)since
theproportionofrelevantitemsthataresuccessfullyretrievedby
theserepresentexplicitlylikedsongsfromtheprovidedsonglist.
thesystemcomparedtoallrelevantitemsinthedataset.Aperfect
MDS user interactions on the other hand are in the form of
scoreis1.0,indicatingthatallrelevantitemsareretrievedamong
playcountsinsteadoflikeswhichrequireadifferentapproach.The
thetopkrecommendations.
researchersemployedamin-maxscalingtransformtonormalizethe
TheproposedhybridmodelasshowninProcedureCwillalsobe
databetweenarangeof0-1.Thescaledvaluesarethenmultiplied
evaluatedagainstapurecollaborativefiltering(CF)model(based
by4androundedtothenearestintegertomapto5weightlevels.
onlyoninteractionswithoutincorporatingpersonalityIPPand
Thiswillallowthemodeltoprioritizelearningthecorrelatedsong
UPPfeatures)thatistrainedonthesamecombineddatasetand
featuresinsongswithhigherplaycountswhenusedasweights
parameters.
duringmodeltraining.
3.5 OnlineEvaluation
3.3 ModelDevelopment
Inadditiontothesemetrics,researcherswillalsoemployonline
A hybrid recommender system will be developed utilizing the evaluationmethodstoconductmodelcomparisonsfromtheper-
LightFMlibrarywhichintegrateselementsofbothcollaborative spectiveofnewuserswhosepersonalityandpreferencecounts
filteringandcontent-basedfiltering.Inthismodel,usersandsongs weren’tincludedinmodeltraining.Thiswillbeconductedinthe
arerepresentedbylatentfactorsandbiases,derivedfromuserat- formofawebapp,whichwillrequire20newuserstotakethe
tributes,itemattributes,andhistoricalinteractions. Specifically, personalitytestandinputtheirtop5genrepreferences.Thiswillbe
usersaredescribedthroughfeaturessuchasgenrepreferencesand usedtotesttheefficacyofgeneratingreal-timerecommendations
userpersonalityprofiles(BigFive)whilesongsarecharacterized beforeacquiringalistoftheirliked/dislikedsongs. Theuserswill
bytheirsonicfeaturesandthecomputedItemPersonalityProfiles thenbepresentedwiththegeneratedtop10recommendationsfrom
(IPPs). Withthedescribedpreprocessingandfeatureextraction thetwotrainedmodelswhichtheywillevaluateintheformofa
steps,personalityfeaturesaremoredeeplyintegratedintoboththe post-feedbackquestionnairewhichisadaptedfromastudyevalu-
useranditemfeaturematrix,particularlyinsituationswithlimited atingtheirpersonality-basedrecommendersystem(Luet.al,2018).
explicituser-iteminteractions.Thiswillbecombinedwiththesubs Moreover,userswillalsobeabletoindividuallyrateeachsongin
Forallmodels,researcherswilluseLightFM’scross-validation thegeneratedlistaslike/dislike.Thesemeasureswillbeprecision
featuretorandomlysplittheinteractionsetintotwodisjointtrain- and recall (like the dataset evaluation), and user feedback. For
ingandtestsetswithan80-20split.Themodelwillthenbefitted userfeedback,thesystemisevaluatedqualitativelybyprompting
for30epochsanda0.02learningrate.Theresearcherswillalsotest userstoexpresstheiropinionsonalllistsbasedonthethreemain
274

UsingItemPersonality-BasedProfilinginMusicRecommenderSystems WSSE2025,October24–26,2025,Okayama,Japan
Table1:ModelMetricsComparison(Train)
Metrics CollaborativeFiltering(CF) HybridBPR HybridWARP
Precision 0.24 0.16 0.23
Recall 0.86 0.02 0.75
AUCScore 1.00 0.67 0.82
F1Score 0.38 0.04 0.35
Table2:ModelMetricsComparison(Validation)
Metrics CollaborativeFiltering(CF) HybridBPR HybridWARP
Precision 0.48 0.42 0.46
Recall 0.74 0.22 0.64
AUCScore 0.56 0.53 0.57
F1Score 0.58 0.29 0.54
aspectsbasedonPu,Chen,andHu’s(2011)ResQueUser-Centric researchers,thehybridmodelthatusesWARPhasthebestperfor-
EvaluationFramework.Thesequestionsareintheformofa5-point manceonallmetrics. TheimprovedperformanceofWARPover
Likertscale(1beingstronglydisagreeand5beingstronglyagree), BPRmaybeduetothelimitationofpairwiselossfunctionwhen
withonequestioneachforbothmodelsbeingevaluatedwhichwill usedonrelativelysparseandimbalanceddata,withthedatasethav-
assessRecommendationQuality,RecommendationDiversityand ingcompleteuserpersonalityinformationforlessthan20%ofthe
UserSatisfaction. Respondentswillalsobeaskedwhichmodel overalluserbase.Moreover,itisespeciallysuitableforimprovinga
ismoresuitedforthemintermsofrecommendationqualityand recommender’sabilitytorankitems,whichiswhyitwaschosen
diversity. asthefinalmodeltorepresenttheHybridPersonalityIPPModel
(ModelA)
4 ResultandDiscussion
Theresearcherscollecteddatafrom208studentsandusedsaiddata 4.2 OnlineEvaluation
tofeedinformationintothemodel,generatingrecommendations Theonlineevaluationmethodinvolvestheuseofasurveythattakes
tailoredaccordingtotheirpersonalityscoresandgenrepreferences theuserfeaturesofauserasinputsandthenthroughthoseinputs,
formodelA(hybridmodel),andpopularity-basedrecommenda- themodelgeneratesalistofsongrecommendations. Withthis,
tionsformodelB(pureCFmodel).Theprecision,recall,AUC,and usersaretaskedtocomparethesongrecommendationsformodel
F1scoresarethencomputedtoevaluatethemetricsofthemodels, A(Hybrid)andmodelB(PureCF)bymarkingthesongsinthelist
forbothofflineandonlineevaluationmethods.Atwo-tailedt-test thattheylike. Then,theyaretaskedtoanswerasecondsurvey
andchi-squaredtestwerealsoconductedforthesurveyresultsfrom relatedtotherecommendationquality(Q1),diversity(Q2),anduser
theonlineevaluationmethodtoverifyhowstatisticallysignificant satisfaction(Q3)ofthetwolists,andcomparewhichlisthasbetter
theresultsare,withp<0.05. recommendationsand/orismorediverse.Respondentswerealso
askedtolikesongsthatwererecommendedtothembythetwo
4.1 OfflineEvaluation
models.Afterthis,anothersurveywasconductedtodeterminethe
Asshownintable1andtable2,purecollaborativefilteringmodel qualityanddiversityoftherecommendationsofthetwomodels.In
has the overall best performance metrics when it comes to the responsetothis,at-testwasconductedtodeterminethesignificant
trainingsetparticularlyforrecallandAUC.Thehigherdiscrepancy differencebetweeneachquestion.TheresultisshowninTable3.
betweenrecallandprecisionscoreforthismodel(alsoreferredto ResultsshowthatModelAperformsbetterthanModelBinterms
asModelB)isindicativeofthelimitationsofthiskindofrecom- ofRecommendationQualityandUserSatisfaction.Incontrastto
mendersinceitprioritizesbreadth/diversityofrecommendations this,ModelBoutperformsModelAintermsofRecommendation
as opposed to actual relevance(precision) with an emphasis on diversity. Looking at the results, users think that model A has
prioritizingsongswithmoreinteractions.Thedrasticdropinper- betterrecommendationqualityandismoresatisfiedwithitsrec-
formancewhencomparingthetrainingandvalidation/testsetfor ommendations,whilsttheuserswouldprefermodelBintermsof
thismodelalsoindicatesthatmodel’sdesignhasissueswithover- diversity. Togetherwiththis,achi-testisconductedforthelast
fittingandislesscapableofadaptingtounseendatacomparedto twoquestions,whereintherespondentsareaskedwhichofthetwo
bothvariantsofthehybridmodel. Overall,thehybridmodelsare listshavebetterrecommendationquality,andwhichlistismore
observedtohavegoodmetricswithnolargediscrepancybetween diverse.ShownbelowisthetableforObservedandExpectedvalues.
validationandtrainingset,whichindicatesthatitcanidentifypat- Observedvaluesarethedatacollectedfromtherespondentswhilst
ternsandtailorrecommendationsaccordinglyevenondatawith Expectedvaluesarethecalculatedvalues.Theresultisshownin
norecordedinteractions.Betweenthetwolossfunctionstestedby table5.
275

| WSSE2025,October24–26,2025,Okayama,Japan |     |     |     |     |     |     |     | JoeldeGomaetal. |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------------- |
Table3:ModelMetricsComparison(Train)
RecommendationQuality RecommendationDiversity UserSatisfaction
|                 | AQ1         |     | BQ1 | AQ2  |     | BQ2  | AQ3         | BQ3  |
| --------------- | ----------- | --- | --- | ---- | --- | ---- | ----------- | ---- |
| Mean            | 3.7         |     | 3.4 | 3.75 |     | 3.95 | 4.15        | 3.55 |
| P(T<=t)two-tail | 0.428290293 |     |     |      |     |      | 0.518979715 |      |
Table4:Chi-TestResult(Observed)
|       |     | A   |     | B   |     | HardtoTell | TOTAL |     |
| ----- | --- | --- | --- | --- | --- | ---------- | ----- | --- |
| LCQ1  |     | 14  |     | 4   |     | 2          | 20    |     |
| LCQ2  |     | 3   |     | 12  |     | 5          | 20    |     |
| TOTAL |     | 17  |     | 16  |     | 7          | 40    |     |
4.3 PrecisionandRecall recommendationqualityisconsistentwiththeactualqualityofthe
Bothmodelsinitiallyproducedrecommendationswithnovaria- recommenderwhichisbasedontheuser’sexplicitlikes.
tionduetothelimitedsongdataset,thisalsohasthebenefitof
5 ConclusionandRecommendation
makingiteasiertoidentifyhowtheincorporationofpersonality
andothergenrefeaturesinfluencethequalityanddiversityofthe Overall,theresearchersaccomplishedtheprimaryobjectiveofthis
| recommendations. | PurecollaborativesystemssuchasModelB, |     |     |     |     |     |     |     |
| ---------------- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
studywhichistodevelopapersonality-basedIPPrecommender
whichsolelyreliesoninteractioncounts,generatedthesameset
systemaswellaseffectivelydemonstrateitspotentialcomparedto
| of recommendations | based | on its overall | popularity | among the |     |     |     |     |
| ------------------ | ----- | -------------- | ---------- | --------- | --- | --- | --- | --- |
traditionallypurecollaborativefilteringrecommendersevenwith
usersincludedinthedataset. Therecommendationlististherefore thelimitationsofdatasetskewnessandsparsity. Inbothoffline
showntofavoroldertracksduetoinherentpopularitybiasand andonlineevaluation,hybridmodelsoutperformpureCFmodels
doesnotadjustbasedontheprovidedinformationsuchasgenre
inbothcomputedmetrics(Precision,Recall,AUC,andF1Score)
andsonicfeatures.Incontrast,ModelAhaspersonality-basedIPPs
aswellasuser-promptedfeedback(forRecommendationQuality
alongsidesonicmetadataandgenrepreferences,whichenablesit
andDiversity).Theoutputrecommendationsalsosuggestthatthe
totailorrecommendationsevenwiththelimiteddataset.Despite
|     |     |     |     |     | hybrid | model achieved a | better balance between | relevance and |
| --- | --- | --- | --- | --- | ------ | ---------------- | ---------------------- | ------------- |
thenumberofusersincreasing(DatasetAvsDatasetB),Model diversitybyleveragingpersonalityalongsidegenreandsonicfea-
Awasstillnotabletocreatemorevariations.Thismaybedueto
turestofindemergentpatternswhencombininguser,song,and
thelimitednumberofsongsthattheusermustchoosefrom(100
|                                  |     |     |                        |     | interactionfeatures. | Toexploretheideamoreeffectively,there- |     |     |
| -------------------------------- | --- | --- | ---------------------- | --- | -------------------- | -------------------------------------- | --- | --- |
| songs)inthecreationofthedataset. |     |     | Forinstance,newersongs |     |                      |                                        |     |     |
searchersrecommendacquiringevenmoresamplesforthemodel
likeVampire(absentfromthe2011MSDdatasetduetozeroprior
tolearnfromandfixtheissuesthatarisefromoverfitting,specif-
interactions)appearedintheTop10byleveragingfeaturesimilari- icallymoresongsfortheusertoevaluateincreatingthedataset
tiestoothertracksalreadypopularamongMapuanstudents.This andincreasingthenumberofrespondentsforthedataset.Feature
hasanunintendedeffectofmakingitappearless”diverse”tousers
engineeringcouldalsobeamendedtoachieveamorereasonable
sincetherecommendedsongsarelikelytobemorespecificand
balancebetweenpopularanddiverseitemswiththeincorpora-
likeeachotheraswhichexplainsthediscrepancybetweenopinion
|     |     |     |     |     | tionofpersonality-basedIPPs. |     | Futureresearchcanalsoexplore |     |
| --- | --- | --- | --- | --- | ---------------------------- | --- | ---------------------------- | --- |
andmetrics-baseddiversity. alternativemethodsforincorporatingpersonalitydata,suchasus-
Basedontheindividualsongsfeedbackforthemodels’recom- ingotherrecommenderlibrariessuchasscikitinsteadofLightFM
mendations,thecomputedprecisionandrecallvaluesalsoindicate
whichwouldhaveadifferentmethodforhandlingtheuser-itemin-
thatModelAoutperformsModelBintermsofrecommendation
formationmatrixandcouldpotentiallyleadtobetterperformance.
qualityanddiversitywhichisevenmoreapparentwhenthereis
moreinformationavailableinthedataset.ModelAhasanaverage
References
precisionvaluethatis0.13higherthanModelB,whichindicates
[1] M.Kleć,A.Wieczorkowska,K.Szklanny,andW.Strus.2023.BeyondtheBigFive
thatevenwithnovariation,ithasgreateraccuracyinadjusting
personalitytraitsformusicrecommendationsystems.EURASIPJournalonAudio,
therankingtoprioritizeitemsuserslikedbasedontheprovided Speech,andMusicProcessing2023,1(2023).DOI:https://doi.org/10.1186/s13636-
| IPPfeatures.Whileinthesurveyitself,thenewrespondentsseem |     |     |     |     |     | 022-00269-0. |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | ------------ | --- | --- |
[2] H.Alharthi.2015.TheUseofItemsPersonalityProfilesinRecommenderSys-
toperceiveModelBasmorediverseandhavemorequality,the tems.RetrievedFebruary2,2024fromhttps://ruor.uottawa.ca/server/api/core/
computedaveragerecallmetricssuggestthatModelAalsoper- bitstreams/59170a9c-2a13-4ad6-baa5-.
[3] H.Li.2023.Musicdepthrecommendationalgorithmbasedonuserdatamining.
formsbetteringeneratingliststhatrepresentawidercoverageto
InProceedingsofthe2023InternationalConferenceonElectronicsandDevices,
| representvariationsinuserpreferences. |     |     | Asaresult,ModelAis |     |     |     |     |     |
| ------------------------------------- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
ComputationalScience(ICEDCS)(Marseille,France),630–634.DOI:https://doi.
alsoconsistentlyshowntohavehigherF1scores,especiallywithan org/10.1109/ICEDCS60513.2023.00121.
increaseindatasetsize,whichisagoodindicatorthattheperceived [4] F.LuandN.Tintarev.2018.ADiversityAdjustingStrategywithPersonalityfor
MusicRecommendation,7–14.
276

UsingItemPersonality-BasedProfilinginMusicRecommenderSystems WSSE2025,October24–26,2025,Okayama,Japan
Table5:MatrixComparison
|        | Precision | Recall | F1Score |
| ------ | --------- | ------ | ------- |
| ModelA | 0.57      | 0.62   | 0.58    |
| ModelB | 0.41      | 0.46   | 0.40    |
[5] A.Garg,V.Chaturvedi,A.B.Dhindsa,V.Varshney,andA.Parashar.2022.Ma- February3,2024fromhttps://sol.sbc.org.br/index.php/sbcm/article/download/
| chinelearningmodelformappingofmusicmoodandhumanemotionbasedon |     | 19433/19261/. |     |
| ------------------------------------------------------------- | --- | ------------- | --- |
physiologicalsignals.MultimediaToolsandApplications81.Advanceonline [8] A.Dorochowicz,A.Kurowski,andB.Kostek.2020.Employingsubjectivetests
publication.DOI:https://doi.org/10.1007/s11042-021-11650-0. anddeeplearningfordiscoveringtherelationshipbetweenpersonalitytypes
[6] R.P.Joy,M.R.Thanka,J.P.M.Dhas,andE.B.Edwin.2023.MusicMoodBased andpreferredmusicgenres.Electronics9,12(2020),Article2016.
RecognitionSystemBasedonMachineLearningandDeepLearning.International [9] R.LiuandX.Hu.2020.AMultimodalMusicRecommendationSystemwith
JournalofIntelligentSystemsandApplicationsinEngineering11,2(2023), Listeners’PersonalityandPhysiologicalSignals.DOI:https://doi.org/10.1145/
| 904–911. |     | 3383583.3398623. |     |
| -------- | --- | ---------------- | --- |
[7] L.Delando,S.MoreiraJúnior,G.Ribeiro,E.Cabral,andG.Ribeiro.n.d.Correlating [10] F.LuandN.Tintarev.2018.ADiversityAdjustingStrategywithPersonalityfor
BigFivePrimaryPersonalityDimensionswithMusicalPreferences.Retrieved MusicRecommendation,7–14.
277