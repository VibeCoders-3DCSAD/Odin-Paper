Review
An Introduction to Machine Learning Methods for
Fraud Detection
AntonioAlessioCompagnino1,2,* ,YleniaMaruccia2,3 ,StefanoCavuoti2,3 ,GiuseppeRiccio2,3 ,
AntonioTutone1,2 ,RiccardoCrupi4 andAntonioPagliaro1,2,5,*
1 INAFIASFPalermo,ViaUgoLaMalfa153,I-90146Palermo,Italy;antonio.tutone@inaf.it
2 ICSC—CentroNazionalediRicercainHPC,BigDataeQuantumComputing,I-40121Bologna,Italy;
ylenia.maruccia@inaf.it(Y.M);stefano.cavuoti@gmail.com(S.C.);giuseppe.riccio@inaf.it(G.R.)
3 INAFOsservatorioAstronomicodiCapodimonte,I-80131Napoli,Italy
4 IntesaSanpaoloS.p.A,I-10138Torino,Italy;riccardo.crupi@intesasanpaolo.com
5 IstitutoNazionalediFisicaNucleareSezionediCatania,ViaSantaSofia,64,I-95123Catania,Italy
* Correspondence:antonio.compagnino@inaf.it(A.A.C.);antonio.pagliaro@inaf.it(A.P.)
Abstract
Financialfraudrepresentsacriticalglobalchallengewithsubstantialeconomicandsocial
consequences. Thiscomprehensivereviewsynthesizesthecurrentknowledgeonmachine
learning approaches for financial fraud detection, examining their effectiveness across
diverse fraud scenarios. We analyze various fraud types, including credit card fraud,
financialstatementfraud,insurancefraud,andmoneylaundering,alongwiththeirspecific
detectionchallenges. Thereviewoutlinessupervised,unsupervised,andhybridlearning
approaches, discussing their applications and performance in different fraud detection
contexts. Weexaminecommonlyuseddatasetsinfrauddetectionresearchandevaluate
performance metrics for assessing these systems. The review is further grounded by
twocasestudiesapplyingsupervisedmodelstoreal-worldbankingdata,illustratingthe
practicalchallengesofimplementingfrauddetectionsystemsinoperationalenvironments.
Throughouranalysisoftherecentliterature,weidentifypersistentchallenges,including
data imbalance, concept drift, and privacy concerns, while highlighting the emerging
trendsindeeplearningandensemblemethods. Thisreviewprovidesvaluableinsights
AcademicEditor:JoseMaríaAlvarez forresearchers,financialinstitutions,andpractitionersworkingtodevelopmoreeffective,
Rodríguez
adaptive,andinterpretablefrauddetectionsystemscapableofoperatingwithinreal-world
Received:25September2025 financialenvironments.
Revised:20October2025
Accepted:24October2025
Keywords: machinelearning;deeplearning;frauddetection;data-drivenfinance
Published:5November2025
Citation: Compagnino,A.A.;
Maruccia,Y.;Cavuoti,S.;Riccio,G.;
Tutone,A.;Crupi,R.;Pagliaro,A.An
1. Introduction
IntroductiontoMachineLearning
MethodsforFraudDetection.Appl. Financialfraudrepresentsoneofthemostpressingchallengesfacingmodernbusiness
Sci.2025,15,11787. https://doi.org/ sectors,withsevereimpactsextendingbeyondindividualorganizationstoaffecttheentire
10.3390/app152111787 globaleconomy. Recentcomprehensivesurveysrevealthat56%ofcompaniesworldwide
Copyright:©2025bytheauthors. haveexperiencedsomeformoffraud,withfinancialfraudbeingparticularlyprevalentand
LicenseeMDPI,Basel,Switzerland. economicallydamaging[1].Thesophisticationandscaleoffraudulentactivitiescontinueto
Thisarticleisanopenaccessarticle evolve,renderingtraditionaldetectionapproachesincreasinglyinadequateforaddressing
distributedunderthetermsand
contemporarythreats[2].
conditionsoftheCreativeCommons
Theemergenceofmachinelearning(ML)asapowerfulanalyticaltoolhasrevolution-
Attribution(CCBY)license
izedfrauddetectioncapabilities,enablingorganizationstoidentifycomplexpatternsand
(https://creativecommons.org/
licenses/by/4.0/).
Appl.Sci.2025,15,11787 https://doi.org/10.3390/app152111787

Appl.Sci.2025,15,11787 2of32
anomaliesinvastfinancialdatasetsthatmightindicatefraudulentactivities. Thestrate-
gicapplicationofappropriateMLtechniquesiscrucialforidentifyingemergingthreats
whilesimultaneouslyminimizingfalsefraudalarmsthatcandisruptlegitimatebusiness
operations[3].
Despite these technological advances, significant challenges persist in developing
robustfrauddetectionsystems. Thesechallengesarenotmerelytechnicalbutaredeeply
rooted in the nature of financial data and the adversarial dynamics of fraud. The key
obstacles include extreme class imbalance, where fraudulent transactions are needles
in a haystack (often less than 1% of the total), making it difficult for models to learn
theircharacteristics[4–6]. Furthermore,modelsfaceconstantconceptdriftasfraudsters
continuouslyevolvetheirtactics,renderingmodelstrainedonhistoricaldataobsolete[7].
Finally,theincreasingcomplexityofmodels,especiallydeeplearningapproaches,raises
criticalissuesofinterpretability, whichisoftenastrictrequirementinhighlyregulated
financialenvironments[8,9]. Thesemultifacetedchallengessignificantlycomplicatethe
accurateandtimelydetectionofevolvingfinancialfraudschemes.
ThiscomprehensivereviewaimstoprovideasystematicanalysisofMLtechniquesfor
financialfrauddetection,addressingthecurrentstateofresearchandpracticalapplications.
However,unlikemanysurveysthatremainatatheoreticallevel,thisworkaimstobridge
thegapbetweenacademicresearchandoperationalreality. Unlikeotherreviews,thiswork
bridgesthegapbetweentheoryandpracticethroughtwoin-depthcasestudiesonrealand
proprietarybankingdata,criticallyanalyzingtheoperationaltrade-offsandperformance
inrealisticscenarios. Weexaminedifferentcategoriesoffinancialfraud,analyzevarious
ML approaches, explore commonly used datasets, and evaluate performance metrics
thatarecriticalforassessingsystemeffectiveness. Bysynthesizingtherecentadvances
andidentifyingresearchgaps,thisreviewprovidesvaluableinsightsforresearchersand
practitionersseekingtodevelopmoreeffectiveandpracticalfrauddetectionsystems.
2. TypesofFinancialFraud
Financialfraudencompassesadiversearrayofdeceptiveactivitiesdesignedtoachieve
illegalfinancialgainthroughvariousmechanisms. Athoroughunderstandingofdifferent
fraudtypesandtheircharacteristicsisfundamentalfordevelopingtargetedandeffective
detection systems. Based on our comprehensive analysis of the literature, we present
a systematic classification of financial fraud into two primary categories: external and
internalfraud.
2.1. ExternalFraud
Externalfraudrepresentsdeceptiveactivitiesperpetratedbystakeholdersoperating
outside an organization’s direct control. Our literature analysis reveals that 54% of the
examinedarticlesfocusoninvestigatingvariousformsofexternalfraud.
2.1.1. CreditCardandPaymentFraud
Creditcardfraudemergesasthemostextensivelyresearchedtypeofexternalfraudin
theliterature[4,10,11]. Globally,lossesfromthistypeoffraudareprojectedtoexceedUSD
40billionannuallyby2027. Thiscategoryinvolvesunauthorizedtransactionsconducted
usingstolencardinformationorthroughsophisticateddeceptivemechanisms. Researchin
thisdomaintypicallyanalyzestransactionpatterns,purchasebehaviors,temporalaspects
ofcardusage,andgeographicanomaliestoidentifyindicatorsofpotentialfraud[12].
Thescopeofpaymentfraudhasexpandedsignificantlywithdigitaltransformation,
nowencompassingonlinepaymentfraud,digitalwallettransactions,contactlesspayments,
andpoint-of-salefraud. Theincreasingadoptionofdiversedigitalpaymentsystemshas

Appl.Sci.2025,15,11787 3of32
attractedsubstantialresearchattention,reflectingthegrowingcomplexityofpaymentfraud
schemes[13–15].
2.1.2. LoanFraud
Loanfraudinvolvessophisticateddeceptivepracticesthroughouttheloanlifecycle,
includingfraudulentloanapplications,identitytheftschemes,incomemisrepresentation,
andpropertyvalueinflation[16–18].MLmodelsdesignedforloanfrauddetectiontypically
analyzeapplicantdatapatterns,credithistoryinconsistencies,applicationtiminganomalies,
andcross-referencingpatternstoidentifypotentialfraudindicators.
2.1.3. InsuranceFraud
Insurance fraud represents a significant category encompassing various schemes
acrossdifferentinsurancesectors. TheFBIestimatesthatthetotalcostofinsurancefraud
(non-health insurance) is more than USD 40 billion per year in the United States alone.
Thisincludesfraudulentclaimsinhealthinsuranceprogramsinvolvingdocumentforgery,
fraudulentbillingpractices,andfalsemedicalprescriptions[19,20]. Additionally,automo-
bileinsurancefraudinvolvingsophisticatedcollusionnetworksbetweenpolicyholders
and repair shops presents unique detection challenges [21–23]. ML techniques in this
domainanalyzeclaimpatterns,policyholderbehavioralhistories,serviceprovidernetwork
relationships,andtemporalclaimsequencestodetectpotentialfraudulentactivities.
2.2. InternalFraud
Internalfraudconsistsofdeceptiveactivitiesperpetratedbyindividualswithautho-
rizedaccesswithinanorganization. Approximately46%oftheanalyzedstudiesfocuson
variousformsofinternalfraud.
2.2.1. FinancialStatementFraud
Financialstatementfraudinvolvessophisticatedmanipulationoffinancialreports
tomisrepresentanorganization’struefinancialperformanceandposition[24–26]. This
categoryistypicallystudiedusingcomprehensivedatafromfinancialregulatorybodies
suchastheSEC,majorstockexchanges,andauditingfirms[27]. MLtechniquesinthis
domainanalyzefinancialratios,reportingpatternanomalies,textualelementsoffinancial
statements,andcross-periodconsistencytoidentifypotentialfraudindicators.
2.2.2. MoneyLaundering
Money laundering fraud involves complex schemes designed to disguise the ori-
ginofillegallyobtainedfundsbyintegratingthemintolegitimatefinancialtransaction
flows [28,29]. According to the United Nations, the estimated amount of money laun-
deredgloballyinoneyearis2–5%oftheglobalGDP,orUSD800billion–USD2trillionin
currentUSdollars. MLmodelsformoneylaunderingdetectionanalyzesuspiciouspat-
ternsintransactionnetworks,customerbehavioralanomalies,accountactivitysequences,
andcross-institutionaltransactionflowsthatmayindicatelaunderingactivities[30].
2.2.3. TaxFraud
Taxfraudencompassesdeliberatemisrepresentationofinformationtotaxauthorities
withtheintenttoreducetaxliabilitythroughvariousschemes[31,32]. MLtechniquesin
thisdomainanalyzetaxreturndatainconsistencies,businessactivitypatterns,taxpayer
networkrelationships,andcross-referencingwithexternaldatasourcestoidentifypotential
evasionpatterns[33].

Appl.Sci.2025,15,11787 4of32
2.2.4. AssetMisappropriation
Thiscategoryincludesvariousformsofunauthorizedassetmanipulation,including
unauthorizedpaymentschemes[34,35],dormantaccountfraudexploitation,smurffraud
techniques,andbulkfraudoperations[36]. MLapproachesfordetectingassetmisappro-
priationanalyzetransactionpatterns,useraccesslogs,timinganomalies,andauthorization
sequencestodetectunusualactivitiesthatmayindicatemisappropriation.
Understandingthespecificcharacteristicsandindicatorsofeachfraudtypeisessential
fordevelopingtargetedMLapproachesthataddresstheuniquepatternsandchallenges
associatedwithdifferentfraudcategories. Thediversityoffraudtypesnecessitatesvaried
andsophisticatedapproachestodetectionasdifferentfraudschemesexhibitdistinctbehav-
ioralpatterns,temporalcharacteristics,andnetworkrelationshipsthatrequirespecialized
analyticaltechniques.
2.3. EmergingandComplexFraudTypologies
In addition to these well-established categories, recent developments have intro-
duced new and complex fraud typologies that warrant dedicated attention [37,38].
Theseincludethefollowing:
• MoneyMuling: Individualsarerecruited—knowinglyorunknowingly—totransfer
illicitfundsacrossaccounts,maskingtheircriminalorigin. Theseschemesoftenin-
volveSEPAtransfers,instantpayments,andprepaidcardtop-ups,andareassociated
withdeviceorSIMchangesandrecurringbeneficiarypatterns.
• Account Takeover (ATO): Unauthorized access to user accounts via stolen cre-
dentialsorsocialengineering,enablingfraudulenttransactionsundertheguiseof
legitimateusers.
• AuthorizedPushPayment(APP)Fraud:Victimsaredeceivedintoinitiatingpayments
tofraudsters,typicallythroughimpersonationorurgency-basedmanipulation.
• Synthetic Identity Fraud: Fraudsters construct fictitious identities by combining
real and fabricated personal data, allowing them to open accounts and obtain
creditundetected.
• Social Engineering and Impersonation: Psychological manipulation techniques
areusedtoextractsensitiveinformationorinducefinancialactions,oftentargeting
customersupportorvulnerableindividuals.
• BusinessEmailCompromise(BEC):Fraudstershijackorspoofcorporateemailaccounts
toredirectpaymentsorobtainconfidentialdatathroughdeceptivecommunications.
Theseemergingfraudtypesoftenblurtheboundariesbetweeninternalandexternal
threats and require adaptive detection strategies that incorporate behavioral analytics,
cross-channelmonitoring,andreal-timeanomalydetection.
3. ReviewMethodology
Thisreviewisbasedonasystematicliteraturesearchdesignedtoidentifyrelevant
andimpactfulresearchattheintersectionofmachinelearningandfinancialfrauddetection.
The process was guided by a defined protocol to ensure comprehensive coverage and
minimizebias. Ouranalysissynthesizesthefindingsfromover120peer-reviewedarticles,
conference proceedings, and technical reports published in the last decade, specifically
fromJanuary2014toDecember2023,tocapturethemostcurrenttrendsandchallengesin
thefield.
Theliteraturesearchwasconductedacrossseveralmajoracademicdatabases,includ-
ingScopus,IEEEXplore,ACMDigitalLibrary,andWebofScience. Searchquerieswere
formulatedbycombiningkeywordsfromthreecoreareas:

Appl.Sci.2025,15,11787 5of32
• FraudTypologies: “financialfraud",“creditcardfraud”,“insurancefraud”,“money
laundering”,“paymentfraud”,and“financialstatementfraud”.
• LearningParadigms: “machinelearning”,“deeplearning”,“supervisedlearning”,
“unsupervisedlearning”,“anomalydetection”,and“ensemblemethods”.
• SpecificAlgorithms: “RandomForest”,“SupportVectorMachine”,“neuralnetwork”,
“LSTM”,“autoencoder”,and“XGBoost”.
Ourinclusioncriteriarequiredarticlesto(i)applyoneormoreMLtechniquestoa
financialfrauddetectiontask,(ii)presentempiricalresultswithperformanceevaluation,
and(iii)bepublishedinEnglish. Weexcludedstudiesthatwerepurelytheoretical,lacked
sufficientmethodologicaldetailforreplication,orfocusedonnon-financialdomains(e.g.,
clickfraudandacademicplagiarism). Theselectioninvolvedaninitialscreeningoftitles
andabstracts,followedbyafull-textreviewtodeterminefinaleligibilityforinclusionin
thissynthesis.
4. MachineLearningApproachesforFraudDetection
Machinelearningapproachesforfrauddetectioncanbesystematicallycategorized
intothreeprimarymethodologies: supervised,unsupervised,andhybridmethods. Each
approachoffersdistinctadvantagesandlimitationsdependingonthespecificfrauddetec-
tionscenarioandavailabledatacharacteristics.
4.1. SupervisedLearning
Supervisedlearningrepresentsthepredominantapproachinfrauddetectionresearch,
accountingforapproximately57%ofthetechniquesemployedinthereviewedliterature.
Inthismethodology,modelsaretrainedoncarefullylabeleddatasetswheretransactions
areexplicitlyclassifiedaseitherfraudulentorlegitimate,enablingthealgorithmtolearn
discriminativepatterns.
4.1.1. ClassificationTechniques
RandomForest(RF)
RandomForestemergesasthemostwidelyadoptedsupervisedtechniqueforfraud
detection,appearingin34studieswithinourreview. Thisensemblemethodcombinesmul-
tipledecisiontreestoimproveclassificationaccuracywhileeffectivelyreducingoverfitting
tendencies[39,40]. RFmodelshavedemonstratedconsistentlyhighaccuracyratesincredit
card fraud detection and financial statement fraud identification, frequently achieving
accuracyratesexceeding95%[41].
RFovercomesthefundamentallimitationsofindividualdecisiontrees,wheresplits
occurconsideringtheentiredataset,makingDTalgorithmspronetooverfittingandhigh
variance. Instead,RFconsidersrandomsubsetsofdatatobuildmultipledecisiontrees,
and, for each tree, a random subset of features is selected from all available features.
Furthermore,itemploysoptimizationcriteriaforfindingthebestsplitforeachnodeusing
Giniindexorentropyforclassificationtasks,orRSSforregressionproblems.
ExtraTrees
ExtraTrees(ExtremelyRandomizedTrees)representacomputationallyefficientvari-
antofRandomForest[42,43]. Thisalgorithmisparticularlywell-suitedforapplications
withnoisydataoralargenumberoffeatures.
WhilesimilartoRandomForestinusinganensembleofdecisiontrees,ExtraTrees
introducesagreaterdegreeofrandomnessinhowsplitsarechosen. Specifically,foreach
node, a random subset of features is considered, and the split point for each feature
isselectedrandomlyratherthanbeingoptimizedbasedoncriterialikeGiniimpurityor

Appl.Sci.2025,15,11787 6of32
entropy.Thisrandomizedapproachreducesvarianceandcomputationalcost,oftenleading
torobustperformance,althoughitmaysometimesresultinaslightincreaseinbias.
LogisticRegression(LR)
LogisticRegressionappearsin32studiesandisparticularlyvaluedforitssimplicity
andinterpretabilitycharacteristics. Itmodelstheprobabilityofatransactionbeingfraudu-
lentbasedonitsfeaturecharacteristics[44,45]. LRdemonstratesparticulareffectiveness
forbinaryclassificationtaskscommoninfrauddetection,althoughitmaystrugglewith
highlycomplexandnon-linearfraudpatterns[46].
SupportVectorMachine(SVM)
SupportVectorMachineisutilizedin29studies,separatingdatapointsusingahyper-
planethatmaximizesthemarginbetweendifferentclasses[47,48]. SVMproveseffective
forbothlinearandnon-linearclassificationthroughvariouskernelfunctions,makingit
suitablefordiversefrauddetectionscenarioswithdifferentdatacharacteristics[49].
In practice, SVM is a linear model used in two primary scenarios: when data are
linearlyseparable(classesarewellseparated)andwhendataarenotlinearlyseparable
(nosharpseparationexistsintheoriginalspace). Inthefirstcase,wecanidentifyaline
(one-dimensionalproblem)orhyperplane(multi-dimensionalproblem)thateffectively
separatestheclasses. Thisseparatinghyperplaneiscalledthedecisionboundary.
While multiple separators may perfectly discriminate between classes, the choice
of separator significantly impacts how new data points are classified. We compute the
perpendiculardistancefromeachtrainingobservationtoagivenseparatinghyperplane;
thesmallestdistancefromobservationstothehyperplaneisknownasthemargin. Thede-
cisionboundaryshouldbepositionedasfaraspossiblefromdatapointsofbothclasses.
Trainingpointsthattouchthemarginaresupportvectors,which“support”themaximal
marginhyperplane.
For non-linearly separable data, SVM employs the kernel trick, transforming data
into higher-dimensional space where linear separation becomes possible. The kernel
functionimplicitlymapsdatatohigh-dimensionalspace,allowingfornon-lineardecision
boundariesintheoriginalspace.
DecisionTrees(DTs)
Decisiontreesareemployedin29studies,creatingmodelsthatpredicttargetvariable
classesbylearningdecisionrulesfromdatafeatures[50,51]. DTsareparticularlyvaluedfor
theirinterpretability,whichiscrucialinfrauddetection,whereexplainingwhyatransaction
wasflaggedasfraudulentmaybelegallyoroperationallynecessary[52].
Decision trees utilize tree-like structures to deliver consequences based on input
decisions. Theyareparticularlyimportantforanomalyandfrauddetectioninindustries
likefinanceandbanking,wherecompaniesdeploydecisiontreestofilteroutanomalous
orfraudulentloanapplicationsandidentifyfraudulentcustomers. Therecursivebinary
treestructureprovidesexcellentinterpretability,withthefeaturespacefullydescribedbya
singletree.
ThegoalistofindtreesthatminimizetheResidualSumofSquares(RSS),ageneral
characteristicofDTsexceptforExtraTrees. Unfortunately,findingthebestbinarypartition
intermsofminimumsumofsquaresisnotfeasibleinpracticebecauseitiscomputationally
infeasible to consider every possible partition of the feature space. For this reason, we
employatop-downgreedyapproachknownasrecursivebinarysplitting.

Appl.Sci.2025,15,11787 7of32
NaiveBayes(NB)
NaiveBayesappearsin19studies,applyingBayes’theoremwithanindependence
assumptionbetweenfeatures[53,54]. Whilethisindependenceassumptionrarelyholds
inreal-worldfinancialdata,NBoftenperformssurprisinglywellinfrauddetectiontasks,
particularlywhendealingwithlimitedtrainingdata[44].
Thisprobabilisticclassifierrepresentsoneofthefastest,mostaccurate,andreliable
supervisedlearningalgorithms. Itassumesfeaturesarenormallydistributedandindepen-
dentofeachother. ThealgorithmusespriorprobabilityP(H)ofhypothesisHbeingtrue
andposteriorprobabilityP(H|D)ofdataDgiventhathypothesisHistrue.
K-NearestNeighbor(KNN)
K-NearestNeighborisusedin14studies, representinganinstance-basedlearning
algorithmthatclassifiestransactionsbasedontheirproximitytoknownsamplesinthe
feature space [55,56]. KNN proves effective for detecting fraud patterns that cluster in
featurespacebutmaystrugglewithhigh-dimensionaldata[57].
KNNisanon-parametricsupervisedapproachusedforbothclassificationandregres-
sionproblems. Thealgorithmworksbyfindingthekmostsimilarobjectstoagivenobject
xbasedondistanceorsimilaritymeasuresbetweenxandallobjectsinthedataset. Itthen
assignsalabeltoxbasedonthemostfrequentlabelamongitskneighborsusingeither
majorityvotingorweightedvotingapproaches.
ArtificialNeuralNetworks(ANNs)
Artificialneuralnetworksareemployedin17studies,capableofmodelingcomplex
non-linear relationships between features and fraud likelihood [58,59]. While effective,
traditionalANNsmayrequiresignificantcomputationalresourcesandcarefulhyperpa-
rametertuning[60].
Neuralnetworksareinformationprocessingmodelsinspiredbybiologicalneuron
systems, composed of highly interconnected processing elements known as “neurons.”
Thesenetworksareadaptivesystemsthatcanchangetheirinternalstructurebyadjusting
input weights. Each input variable is multiplied by respective weights, then summed
togethertoformnetoutput,withbiasadded.
TheANNcreatesthreelayersintheneuralnetwork:inputlayer,hiddenlayer,andout-
putlayer. Thefirstlayerreceivesrawinput,processesit,andpassesprocessedinformation
tohiddenlayers,whichpassinformationtotheoutputlayerthatproducesthefinalout-
put. Theadvantageofneuralnetworksistheiradaptivenature,learningfromprovided
informationtooptimizeweightsforbetterpredictioninunknownoutcomesituations.
XGBoost
XGBoostappearsin13studies,representingagradientboostingframeworkknownfor
exceptionalperformanceandcomputationalspeed[61,62]. Itsequentiallybuildsdecision
trees, with each tree correcting errors made by previous trees, making it particularly
effectiveforimbalanceddatasetscommoninfrauddetection[63].
Boosting(XGBoost)isanensembletechniquecreatingacollectionofpredictorswhere
learnersarelearnedsequentially. Earlylearnersfitsimplemodelstodata,thenanalyze
dataforerrors. Thegoalistosolveerrorsfrompriortreesateverystep. Modelscanhave
differentimportanceorweights,anddatasetsareweightedsothatobservationsincorrectly
classifiedbypreviousclassifiersreceivegreaterimportanceinsubsequentmodeltraining.

Appl.Sci.2025,15,11787 8of32
4.2. UnsupervisedLearning
Unsupervisedlearningtechniquesareemployedinapproximately18%ofthereviewed
studies. Thesemethodsidentifypatternsandanomalieswithoutrequiringlabeledtraining
data,makingthemparticularlyvaluablefordetectingnovelfraudpatternsthatmaynotbe
representedinhistoricallabeleddatasets.
4.2.1. IsolationForest
IsolationForestappearsin19studies,isolatingobservationsbyrandomlyselecting
features and randomly selecting split values between maximum and minimum values
ofselectedfeatures[64,65]. Itprovesparticularlyeffectiveforidentifyingoutliers,which
frequentlyrepresentfraudulenttransactions[66].
4.2.2. Autoencoders
Autoencoders are used in 10 studies, representing neural networks that learn
to compress and reconstruct data, with reconstruction error serving as an anomaly
score[14,67]. Theyareparticularlyeffectivefordimensionalityreductionandcapturing
complexpatternsintransactiondata[68].
Autoencodersarelatentvariablemodelsthatdiscoverlatentvariables(variablesnot
directly observed but inferred from direct observations). They consist of an encoder that
learnsmappingfromdataXtolow-dimensionallatentspaceZandadecoderthatperforms
thereverseoperation,increasingdimensionsfromlatentspaceZbacktooriginaldimensions.
Theprocessrepresentsaformofcompression,keepingthecoreinformationindata.
The encoder learns mapping from data X to low-dimensional latent space Z, while the
decoderlearnstouselatentfeaturesZtoreconstructtheoriginaldata. Usingthedistance
between reconstructed data and real data, we can determine if a signal represents an
anomalyornormalbehavior.
4.2.3. K-MeansClustering
K-meansappearsin7studies,partitioningdataintokclusterswitheachobservation
belonging to the cluster with the nearest mean [69,70]. It can identify groups of simi-
lar transactions, with those falling outside established clusters potentially representing
fraudulentactivities[23].
TheK-meansalgorithmdividesNsamplesintoKdisjointclustersofequalvariances,
minimizingwithin-clustersum-of-squares(WSS)whilemaximizingbetween-clustersum
ofsquares(BSS).Eachclusterisrepresentedbythemeanofcontainedobservations.
4.2.4. HiddenMarkovModels(HMMs)
HMMs are employed in 7 studies, representing statistical models that assume the
systembeingmodeledfollowsaMarkovprocesswithunobservedstates[71,72]. HMMs
areparticularlyusefulformodelingsequentialdataliketransactionsequences,wherethey
canlearnnormalspendingbehaviorsandflagsignificantdeviations[73].
4.2.5. LocalOutlierFactor(LOF)
LOFappearsin13studies,comparingthelocaldensityofapointwithlocaldensities
ofitsneighbors,identifyingsampleswithsubstantiallylowerdensitythanneighborsas
potentialoutliers[65,74].
4.3. DeepLearningApproaches
Deeplearningapproachesconstitutearapidlygrowingsegmentoffrauddetection
research,withapproximately34studiesemployingthesesophisticatedtechniqueseither
independentlyorincombinationwithtraditionalMLmethods.

Appl.Sci.2025,15,11787 9of32
4.3.1. LongShort-TermMemory(LSTM)
LSTMnetworksareusedin8studies,representingspecializedrecurrentneuralnet-
worksdesignedtomodeltemporalsequencesandlong-rangedependencies[75,76]. They
proveparticularlyeffectiveforanalyzingsequentialtransactiondata,capturingtemporal
patternsthatmayindicatefraudulentbehavior[77].
LSTMsarespecialkindsofrecurrentneuralnetworkscapableoflearninglong-term
dependenciesindatathroughinternalmechanismscalledgatesthatregulateinformation
flow.Thesegatescanlearnwhichdatainasequenceisimportanttokeeporforget,allowing
LSTMmodelstostoreinformationforextendedperiods.
4.3.2. ConvolutionalNeuralNetworks(CNNs)
CNNsappearin7studies. Originallydesignedforimageprocessing,CNNscanbe
effectivelyappliedtostructureddataforfrauddetection[58,78]. Thecoreideaistotreat
structured financial data as a grid, similar to an image, and apply convolutional filters
(kernels) to it. They automatically learn hierarchical features from data, where initial
layerscapturesimplepatternsanddeeperlayerscombinethemtoidentifymorecomplex
relationships,whichisvaluableforidentifyingsophisticatedfraudpatterns[79].
Usingconv2dimplementation,themostpopularfunctionforbuildingconvolutional
layersrequiressettinginputchannels,outputchannels,kernelsize,stride,padding,anddi-
lationparameters. Thekernelisthefilterthatslidesoverthedata,thestridedefinesthe
stepsizeofthismovement,andpaddingaddsabordertocontroltheoutputdimensions.
Thegeneralformulatocalculatetheoutputsizeofaconvolutionis
(cid:22) InputSize+2×Padding−KernelSize (cid:23)
OutputSize= +1 (1)
Stride
where
• InputSize: Thedimensions(heightandwidth)oftheinputdata.
• KernelSize: Thedimensionsofthefilterusedtoscanthedata.
• Padding: A border of zeros added to the input, primarily to control the output’s
spatialdimensions.
• Stride: Thestepsize,orhowmanypixelsthefiltermovesatatimeacrosstheinput.
Inthisformula,theinputsizeisadjustedbyaddingtwicethepadding(toaccountfor
bothsides)andsubtractingthekernelsize.ThisresultisthendividedbytheStride(thestep
sizeofthefilter). Thefloorfunction⌊·⌋ensurestheoutputdimensionisaninteger,andone
is added to finalize the count of possible kernel positions. This determines the spatial
dimensionsofthefeaturemapproducedbythelayer. Thisprocessallowsthenetworkto
buildarichmulti-levelrepresentationoftheinputdatatoeffectivelyclassifytransactions.
4.3.3. RecurrentNeuralNetworks(RNNs)
RNNsareemployedin7studies, representingnetworksthatmaintainmemoryof
previousinputs,makingthemsuitableforsequentialdataanalysis[80,81]. Theycanmodel
temporaldependenciesintransactionsequences,helpingtoidentifyunusualpatterns[82].
RNNs are dynamic networks that account for temporal aspects, exhibiting cyclic
behavior that allows forward and backward processing to reconstruct temporal se-
quences. Theyareparticularlywell-suitedforsentimentanalysisandothersequentialdata
processingtasks.
4.3.4. GenerativeAdversarialNetworks(GANs)
GANsappearin7studies,consistingofgeneratoranddiscriminatornetworksthat
compete against each other [83,84]. In fraud detection, GANs can generate synthetic

Appl.Sci.2025,15,11787 10of32
fraudsamplestoimproveclassifiertraining,particularlyvaluableforhighlyimbalanced
datasets[5].
Whilepromisingfordataaugmentation,GANsfacechallengessuchastrainingin-
stabilityand“modecollapse,”wherethegeneratorproducesalimitedvarietyofsamples.
Furthermore,evaluatingthequalityofsyntheticdataremainsanopenresearchquestion,
makingtheirpracticaldeploymentcomplex.
GANsutilizetwocompetingneuralnetworks: agenerator(G)thatcreatessamples
from random noise and a discriminator (D) that distinguishes between real and fake
samples. Thegeneratoristrainedindirectlythroughitsabilityto“fool”thediscriminator.
DeepConvolutionalGenerativeAdversarialNetworks(DCGANs)extendGANsusing
convolutionalarchitecturesforimprovedimagegenerationandfeatureextractioncapabilities.
4.4. HybridandEnsembleMethods
Many studies employ hybrid approaches that strategically combine multiple ML
techniquestoimproveoveralldetectionperformanceandrobustness.
4.4.1. Supervised-UnsupervisedHybrids
Approximately 15% of studies combine supervised and unsupervised techniques,
such as using unsupervised learning for feature extraction followed by supervised
classification[85,86].
4.4.2. EnsembleMethods
Techniquesincludingbagging(5studies),boosting(59studies),andstacking(4stud-
ies)combinemultiplemodelstoimprovepredictionaccuracy[87–89]. Theseapproaches
can effectively mitigate individual model weaknesses and improve overall detection
performance[52].
4.4.3. DeepLearningHybrids
SomestudiescombinetraditionalMLwithdeeplearningapproaches,suchasusing
deeplearningforfeatureextractionandtraditionalMLforfinalclassification[4,90].
Theprevalenceofsupervisedlearninginfrauddetectionresearchreflectstheavailabil-
ityoflabeledhistoricaldatainmanyfinancialinstitutions. However,thegrowinginterest
inunsupervisedanddeeplearningapproachesindicatesrecognitionoftheirpotentialto
identifynovelandevolvingfraudpatternsthatmaynotbewell-representedinhistorical
trainingdata.
Toprovideaclearcomparativeoverviewofthemostcommontechniquesdiscussedin
theliterature,Table1summarizestheirkeycharacteristics,advantages,anddisadvantages
in the context of financial fraud detection. This synthesis highlights the critical trade-
offsbetweenmodelperformance,complexity,andinterpretabilitythatpractitionersand
researchersmustnavigate.
Table1.Comparativeanalysisofmachinelearningapproachesinfrauddetection.
Handling Application
Algorithm Advantages Disadvantages Complexity Interpretability
Imbalance Examples
-Mostwidely
-Lessinterpretable
adoptedsupervised Canhandle
thanasingle
technique. Moderate-High: Low-Moderate: imbalanceddata
decisiontree. Creditcardfraud
-Reduces Requiresbuilding Notacomplete viaparameters
-CaseStudy2 andfinancial
RandomForest(RF) overfittingand andaggregating blackbox;feature likeclass_weight,
showsdifficulty statement
improvesaccuracy. multiple importancecan althoughwith
improving fraudidentification.
-Consistently decisiontrees. beextracted. varying
recallevenwith
highperformance effectiveness.
class_weight.
(>95%accuracy).

Appl.Sci.2025,15,11787
11of32
Table1.Cont.
|     |     |     |     |     | Handling | Application |
| --- | --- | --- | --- | --- | -------- | ----------- |
Algorithm Advantages Disadvantages Complexity Interpretability
|     |            |     |     |           | Imbalance     | Examples |
| --- | ---------- | --- | --- | --------- | ------------- | -------- |
|     | -Valuedfor |     |     | VeryHigh: | Oftenrequires |          |
simplicityandhigh -Maystrugglewith Coefficients preprocessing(e.g., Binaryclassification
| LogisticRegression |     |     | Low:Simplelinear |     |     |     |
| ------------------ | --- | --- | ---------------- | --- | --- | --- |
interpretability. complexnon-linear directlyindicate resampling)asitcan taskscommonin
(LR) -Effectiveforbinary fraudpatterns. model;fasttotrain. theinfluence bebiasedtowards frauddetection.
|     | classification.   |              |                | ofeachfeature. | themajorityclass.   |     |
| --- | ----------------- | ------------ | -------------- | -------------- | ------------------- | --- |
|     | -Knownforexcep-   |              |                | Low:Asan       |                     |     |
|     | tionalperformance | -Morecomplex |                |                |                     |     |
|     |                   |              | High:Agradient | ensembleof     |                     |     |
|     | andcomputa-       | totunethan   |                |                | Highlyeffectiveasit |     |
tionalspeed. simplermodels. boostingframework trees,itisdifficult sequentiallybuilds Frauddetectionin
| XGBoost |               |                    | withnumerous | tointerpret, |                | contextswithhighly |
| ------- | ------------- | ------------------ | ------------ | ------------ | -------------- | ------------------ |
|         | -Particularly | -Riskofoverfitting |              |              | treestocorrect |                    |
effectivewith ifnotcarefully hyperparameters althoughit errorsofpriorones. imbalanceddata.
|     |            |             | totune. | providesfeature |     |     |
| --- | ---------- | ----------- | ------- | --------------- | --- | --- |
|     | imbalanced | configured. |         |                 |     |     |
importancescores.
datasets.
-Unsupervised,
Nativelydesigned
|     | requiresno |     | Moderate:Based | Low:Provides |     |     |
| --- | ---------- | --- | -------------- | ------------ | --- | --- |
labeleddata. -Lesseffectiveif onanensemble ananomalyscore forthispurpose;
|                 |              | fraudpatternsare |               |              | itsgoalistoisolate | Anomalyand        |
| --------------- | ------------ | ---------------- | ------------- | ------------ | ------------------ | ----------------- |
| IsolationForest | -Effectiveat |                  | oftrees,often | butnotaclear |                    |                   |
|                 |              | complexandmimic  |               |              | raredatapoints,    | outlierdetection. |
isolatingoutliers, normalbehavior. computationally reasonwhya makingitidealfor
|     | whichoften |     | efficient. | pointwasisolated. |     |     |
| --- | ---------- | --- | ---------- | ----------------- | --- | --- |
imbalanceddata.
representfraud.
-Unsupervised;
|     | learncomplex |     |     | VeryLow:A | Nativelysuited: |     |
| --- | ------------ | --- | --- | --------- | --------------- | --- |
patterns -Designingthe High:Requires quintessential Learnsthe Anomalydetection
|              | andperform     |               |           | “black-box”model; | representationof  |                   |
| ------------ | -------------- | ------------- | --------- | ----------------- | ----------------- | ----------------- |
|              |                | neuralnetwork | designing |                   |                   | anddimensionality |
| Autoencoders | dimensionality |               |           | reconstruction    | “normal”(majority |                   |
reduction. architecturecan andtraininga errorindicates class)dataand reductionin
|     |               | becomplex. | neuralnetwork. |              |                    | transactionaldata. |
| --- | ------------- | ---------- | -------------- | ------------ | ------------------ | ------------------ |
|     | -Anomalyscore |            |                | ananomalybut | failstoreconstruct |                    |
|     | isbasedon     |            |                | notthecause. | anomalieswell.     |                    |
reconstructionerror.
|     | -Specialized |     |            |             | Canidentify    |            |
| --- | ------------ | --- | ---------- | ----------- | -------------- | ---------- |
|     | formodeling  |     |            | VeryLow:The | deviationsfrom |            |
|     |              |     | VeryHigh:A |             |                | Analysisof |
temporalsequences -Requiresdataina recurrentnature “normal”sequences,
|     |     |     | recurrentneural |     |     | sequential |
| --- | --- | --- | --------------- | --- | --- | ---------- |
LSTM andlong-range sequentialformat. networkwitha andtemporal butoftenrequires transactionaldatato
dependencies. -Computationally dependencies standardimbalance
|     |     |     | complexinternal |     |     | capturetemporal |
| --- | --- | --- | --------------- | --- | --- | --------------- |
-Idealforanalyzing expensivetotrain. makeitextremely techniques
sequencesof “gate”architecture. difficulttointerpret. inthefinal fraudpatterns.
|     | transactions. |     |     |     | classificationlayer. |     |
| --- | ------------- | --- | --- | --- | -------------------- | --- |
5. DatasetsforFraudDetectionResearch
Theperformanceandpracticalapplicabilityoffrauddetectionmodelsdependsig-
nificantlyonthequality,characteristics,andrepresentativenessofthedatasetsusedfor
trainingandevaluation. Ourcomprehensiveanalysisidentifiedseveralcommonlyused
datasetsinfrauddetectionresearch,eachwithdistinctcharacteristicsrelevanttodifferent
fraudtypesanddetectionscenarios.
5.1. CreditCardFraudDetectionDatasets
5.1.1. CreditCardFraudDetectionDataset
ThisdatasetfromtheMachineLearningGroupatUniversitéLibredeBruxellesrep-
resentsthemostwidelyusedresourceincreditcardfrauddetectionresearch,appearing
in15studies[10,91,92]. ItcontainsanonymizedcreditcardtransactionsfromEuropean
cardholdersinSeptember2013,withonly492fraudsoutof284,807transactions(0.172%
fraudrate). MostfeaturesunderwentPCAtransformationforconfidentialityprotection,
withonly’Time’and’Amount’retainedasoriginalfeatures[93].
5.1.2. GermanCreditData
CreatedbyProfessorHofmannfortheUCIMLrepository,thisdatasetfocusesoncredit
riskclassification[94]. Itcontains1000instanceswith20attributesdescribingindividual
characteristicsandcreditinformation. Ithasbeenutilizedinstudies[90,95,96].

Appl.Sci.2025,15,11787 12of32
5.1.3. AustralianCreditApproval
ThisUCIMLrepositorydatasetcontains690instancesand14attributesrelatedto
creditcardapplications[97]. Ithasbeenemployedinstudies[95,96,98].
5.1.4. DefaultofCreditCardClients
ThisdatasetfromtheUCIMLrepositoryfocusesondefaultedpaymentsofcreditcard
customersinTaiwan[99]. Itincludes30,000instanceswith24attributescoveringcredit
dataandpaymenthistoryfromApriltoSeptember2005. Ithasbeenusedby[90,96,98].
5.2. FinancialStatementFraudDatasets
5.2.1. ChinaStockMarketandAccountingResearch(CSMAR)
ThiscomprehensivedatasetprovidesinformationonChina’sstockmarketsandfinan-
cialstatementsoflistedcompaniesbetween1998and2016[100]. Itincludes35,574samples
with337annualfraudcases,usedinstudies[17,101,102].
5.2.2. Compustat
This database contains financial and economic information on US and Canadian
companies [103]. It includes data on 228 companies, with half showing fraud in their
financialinformation. Ithasbeenusedinstudies[25,104].
5.3. SyntheticDatasets
5.3.1. PaySimMobileMoneySimulator
This synthetic dataset was generated using aggregated data from a mobile money
service in an African country [105]. It contains 6,362,620 samples with 8213 fraudulent
transactions. Ithasbeenusedinstudies[106–108].
5.3.2. BankSimPaymentSimulator
BasedonasampleoftransactionaldatafromaSpanishbank,thissyntheticdataset
includes594,643transactions,withapproximately1.2%(7200)labeledasfraud[105]. Ithas
beenusedby[90,96,98].
5.4. OtherSpecializedDatasets
5.4.1. InsuranceCompanyBenchmark(COIL2000)
Thisdatasetcontainsinformationaboutcustomersofaninsurancecompany,including
productusageandsociodemographicdata[109]. Ithas9822instanceswith86attributes
andhasbeenusedininsurancefrauddetectionstudies[19,110].
5.4.2. BitcoinNetworkTransactionalMetadata
ThisdatasetcontainsBitcointransactionmetadatafrom2011to2013,with30,000in-
stancesand11attributesrelatedtoBitcointransactionsandflows[111]. Ithasbeenused
foranalyzinganomaliesincryptocurrencytransactions[112].
5.5. CharacteristicsofFraudDetectionDatasets
Ouranalysisrevealsseveralimportantcharacteristicsthatsignificantlyimpactfraud
detectionresearch.
5.5.1. ClassImbalance
Mostfrauddetectiondatasetsexhibitextremeclassimbalance,withfraudulenttrans-
actionstypicallyconstitutinglessthan1%ofalltransactions. Thisimbalanceaccurately
reflectsreal-worldfraudprevalencebutpresentssignificantchallengesformodeltraining
andevaluation[40,113].

Appl.Sci.2025,15,11787 13of32
5.5.2. FeatureTransformation
Manydatasets,particularlythosecontainingsensitivefinancialinformation,undergo
featuretransformation(e.g.,PCA)toprotectprivacy. Whilenecessaryfordataprotection,
thistransformationcanobscuretheinterpretabilityofresultingmodelsandlimitdomain
knowledgeintegration[10].
5.5.3. TemporalAspects
Somedatasetspreservecrucialtemporalinformation,allowingforanalysisofhow
fraud patterns evolve over time. This temporal dimension is essential for developing
modelsthatcanadapttoemergingfraudstrategiesandconceptdrift.
5.5.4. Realvs. SyntheticData
While most studies (approximately 93%) utilize real-world data, there is growing
interest in synthetic datasets that can simulate diverse fraud scenarios without privacy
concerns. Thesesyntheticdatasetsproveparticularlyvaluablefortestingmodelrobustness
againstvariousfraudstrategiesandforscenarioswhererealfrauddataisscarce[105].
5.6. GuidelinesforFutureDatasetDevelopment
Basedontheidentifiedchallenges,weproposethefollowingguidelinestoadvance
researchinthisarea:
• EstablishmentofStandardizedBenchmarks: Thecommunitywouldbenefitgreatly
fromthecreationandmaintenanceofshared,large-scale,andcontemporarybench-
markdatasets. Thiswouldallowforamoredirectandfaircomparisonofdifferent
modelsandtechniques.
• Privacy-Preserving Data Sharing: Techniques like federated learning should be
furtherexploredtoenablecollaborativemodeltrainingacrossdifferentinstitutions
withoutcentralizingsensitivedata. Thiscouldleadtomorerobustmodelstrainedon
awidervarietyoffraudpatterns.
• AdvancedSyntheticDataGeneration: Whilesyntheticdatasetsexist,futurework
shouldfocusongeneratingdatathatmoreaccuratelycapturescomplexmulti-modal
fraud scenarios and temporal dynamics using advanced generative models like
WassersteinGANs(WGANs)orvariationalautoencoders(VAEs).
The choice of dataset significantly impacts both model performance and practical
applicabilityoffrauddetectionsystems. Datasetsthataccuratelyreflectthecomplexityand
evolvingnatureofreal-worldfraudareessentialfordevelopingeffectivedetectionsystems.
However,thelimitedavailabilityofrecent,comprehensive,andpubliclyaccessiblefraud
datasetsremainsasignificantchallengeforresearchersinthisfield.
6. PerformanceMetricsforFraudDetection
Evaluatingtheperformanceoffrauddetectionmodelsrequiresappropriatemetrics
thataddressthespecificchallengesofthedomain,particularlyclassimbalanceandasym-
metricmisclassificationcosts. Theselectionofevaluationmetricsmustcarefullyconsider
theoperationalcontextandbusinessrequirementsoffrauddetectionsystems.
6.1. SupervisedLearningMetrics
6.1.1. Accuracy
Accuracymeasurestheproportionofcorrectpredictions(bothfraudandnon-fraud)
tototalpredictions:
TP+TN
Accuracy= (2)
TP+TN+FP+FN

Appl.Sci.2025,15,11787 14of32
Whilecommonlyreported,accuracycanbemisleadinginhighlyimbalanceddatasets,
wheresimplyclassifyingalltransactionsasnon-fraudulentwouldyielddeceptivelyhigh
accuracy[114].
6.1.2. PrecisionandRecall
Thesetwometricsarecrucialforimbalancedclassification. Precisionmeasuresthe
proportionofcorrectlyidentifiedfraudulenttransactionsamongalltransactionsclassified
asfraudulent:
TP
Precision= (3)
TP+FP
Highprecisionindicatesalowfalsepositiverate(alsoknownasTypeIError),which
is critically important for minimizing unnecessary interventions in legitimate transac-
tions[115]. Conversely,recall(orsensitivity)measurestheproportionofactualfraudulent
transactionsthatwerecorrectlyidentified:
TP
Recall= (4)
TP+FN
Highrecallisessentialforminimizingfinanciallossesandensuringregulatorycom-
plianceasitdirectlyrelatestoalowfalsenegativerate(TypeIIError,whichisequalto
1−Recall)[115,116].
6.1.3. F1-Score
F1-scoreistheharmonicmeanofprecisionandrecall,providingabalancedmeasure
ofmodelperformance:
2×Precision×Recall
F1-Score= (5)
Precision+Recall
This metric is particularly valuable for fraud detection as it balances the need to
minimizebothfalsepositivesandfalsenegatives,makingitespeciallyusefulforimbalanced
datasets[117].
6.1.4. AreaUndertheROCCurve(AUC–ROC)
AUC–ROC represents the model’s ability to discriminate between fraudulent and
non-fraudulenttransactionsacrossdifferentthresholdsettings:
(cid:90) 1
AUC–ROC= TPR(FPR −1(t))dt (6)
0
HigherAUC–ROCvaluesindicatebettermodelperformance,withvaluescloserto1
representingnear-perfectdiscrimination[17].
6.2. UnsupervisedLearningMetrics
Evaluatingunsupervisedlearningmodelsforfrauddetectionpresentsuniquechal-
lengesasthesemodelsdonotrelyonlabeledtrainingdata. Severalspecializedmetrics
havebeendevelopedforthispurpose.
6.2.1. SilhouetteCoefficient
Thismetricmeasureshowwelldatapointsareclustered,withvaluesrangingfrom
−1to1:
y−x
s(j) = (7)
max(x,y)
wherexistheaveragedistancebetweenpointjandotherpointsinitscluster,andyisthe
minimumaveragedistancetopointsinanothercluster[118].

Appl.Sci.2025,15,11787 15of32
Theaveragesilhouettecoefficientmeasuresclusteringqualitybyassessinghowwell
eachdatapointfitswithinitsassignedcluster. Higheraveragesilhouettewidthindicates
betterclusteringperformance.
6.2.2. Davies–BouldinIndex
Thismetricevaluatesclusteringqualitybasedontheratioofwithin-clusterscatterto
between-clusterseparation:
(cid:32) (cid:33)
1 ∑ k α i +α j
DB= max (8)
K i=1 j̸=i d(c i ,c j )
where K is the number of clusters, c and c are cluster centroids, and α and α are the
i j i j
averagedistancesofallelementsinclustersiandjtotheirrespectivecentroids[118].
6.2.3. RandIndex
Thismeasuresthesimilaritybetweentwodataclusterings:
TP+TN
RI= ×100 (9)
TP+FP+TN+FN
Itisparticularlyusefulwhenexternallabelsareavailableforevaluationpurposes[118].
Havingclusteringalgorithmswithveryhighsilhouettecoefficientbutlowexternalmea-
suresindicatespoorperformancewhenobservationsareassignedtowrongclusters.
6.3. PracticalConsiderationsinMetricSelection
Theselectionofappropriateperformancemetricsshouldconsiderseveraldomain-
specificfactors:
6.3.1. ClassImbalance
Inhighlyimbalanceddatasets,metricslikeprecision,recall,F1-score,andAUC–ROC
providemoremeaningfulassessmentsthanaccuracyalone[117].
6.3.2. OperationalContext
Theoperationalcontextoffrauddetectionsystemsshouldinformmetricselection.
For example, in credit card fraud detection, minimizing false positives (high precision)
may be prioritized to avoid customer inconvenience, while, in money laundering de-
tection, minimizing false negatives (high recall) may be more critical due to regulatory
requirements[119].
6.3.3. CostSensitivity
Theasymmetriccostsoffalsepositivesandfalsenegativesshouldbecarefullyconsid-
ered. Cost-sensitivemetricsthatincorporatethefinancialimpactofmisclassificationscan
providemorepracticallyrelevantperformanceassessments[115].
6.3.4. TimeSensitivity
Forreal-timefrauddetectionsystems,metricsthatincorporatedetectionlatencyare
valuableasearlydetectioncansignificantlyreducefinanciallosses[75].
The comprehensive evaluation of fraud detection systems requires multiple com-
plementary metrics that collectively address the complex requirements of the domain.
Whilenosinglemetriccancaptureallrelevantaspectsofperformance,carefullyselected
metriccombinationscanprovidemeaningfulinsightsintoasystem’spracticalutilityand
operationaleffectiveness.

Appl.Sci.2025,15,11787 16of32
6.4. SoTAMicro-BenchmarkonStandardDataset(ULB2013)
In Table 2, we report AUPRC for five commonly used methods on the ULB 2013
credit-carddataset. Tree/boostingmethodsleadAUPRC;kNNlags; valuesprovidean
externalbaselineforourproprietarystudies[93,120–122].
Table2.SoTAmicro-benchmarkonULB2013(AUPRC).
Dataset Method AUPRC
ULB2013 LogisticRegression(L1) 0.724
ULB2013 RandomForest 0.871
ULB2013 XGBoost 0.867
ULB2013 AdaBoost 0.808
ULB2013 K-NearestNeighbor 0.585
7. CaseStudy1: ApplicationofSupervisedModelsonaReal-World
BankingDataset
Toprovidepracticalcontextforthereviewedmachinelearningtechniquesandperfor-
mancemetrics,thissectionpresentsacomprehensivecasestudybasedontheapplication
ofselectedsupervisedlearningmodelstoareal-worldfinancialdataset.
While this case study focuses on tree-based supervised models, it is worth noting
thatotherstudieshavedemonstratedthepotentialofdifferentapproaches. Forinstance,
deeplearningmodelslikeLSTMshaveshownpromiseincapturingsequentialpatternsin
transactiondata,whilehybridmodelscombiningunsupervisedanomalydetectionwith
supervisedclassifiershavebeeneffectiveinidentifyingnovelfraudtypologies.
7.1. DatasetandPreprocessing
Thedatasetforthisstudywasderivedfromactualtransactionaldataprovidedbya
financialinstitution,comprisingtwomainsources: banktransfers(“Bonifici”)andcardless
payments(“Cardless”). Therawdata,initiallyconsistingofover427,000recordsacross
multipleinterconnectedtables,underwentamulti-stagepreprocessingpipelinetoprepare
itformodeling.
First,adatacleaningstagewasperformedtoensuredataquality. Recordswithcritical
missingvalues(e.g.,transactionamountandtimestamp)wereexcluded,andduplicate
entrieswereremovedtopreventmodelbias. Followingthis,afeatureengineeringprocess
wasundertakentoextractrelevantvariables.
Fromthecleaneddataset,aspecificsubsetof48,559instanceswascarefullyselected.
This selection was not random but targeted a distinct operational period for which a
meticulously verified ground truth was available. Each transaction in this subset was
authoritativelylabeledaseitherlegitimateorfraudulentbydomainexperts. Thisprocess,
while reducing the dataset size, was critical to guarantee a high-quality dataset for a
controlledandreliableevaluationofmodelperformance.
The resulting features included a combination of numerical and categorical at-
tributes. Toensurecompatibilitywiththemachinelearningmodels,categoricalfeatures
were transformed using one-hot encoding. In line with best practices for tree-based
ensembles, numerical features were left unscaled as these models are not sensitive to
featuremagnitude.
Table3summarizesthekeycharacteristicsofthefinaldatasetusedfortheexperiments.
Asignificantandchallengingcharacteristicofthisdatasetisthesevereclassimbalance,
withafraudrateofapproximately1.43%.

Appl.Sci.2025,15,11787 17of32
Table3.Summaryofthebankingdatasetcharacteristics.
Characteristic Value
TotalInstances 48,559
FraudulentInstances 696
FraudRate ~1.43%
Initial“Bonifici”Records 242,792records,52features
Initial“Cardless”Records 184,729records,50features
num_impor, num_hour, num_day_of_month,
ExampleNumericalFeatures num_month, num_day_of_week, num_longi,
num_latit
ExampleCategoricalFeatures cat_CountryCodeBIC_f415b, cat_bank_code_4f875
7.2. ExperimentalSetupandModels
Threesupervisedlearningalgorithms,discussedcomprehensivelyin4,wereselected
forthiscomparativeanalysis:
• RandomForest(RF).
• ExtremeGradientBoosting(XGBoost).
• ExtraTrees(ETs).
Themodelsweretrainedontheprocesseddatasettoclassifytransactionsaseither
legitimate(class0)orfraudulent(class1). Theprimaryevaluationwasconductedusing
confusionmatricesandcomprehensiveclassificationreports,focusingonmetricsparticu-
larlyrelevanttoimbalanceddatasets,suchasprecision,recall,andF1-scorefortheminority
(fraud) class. Feature importance was also extracted from each model to identify key
indicatorscontributingtofraudclassification.
7.2.1. DataSplitsandValidation
Weadoptatemporalsplittopreventleakage: trainingontransactionsfromperiod
T 0 → T n−1 andtestingonT n . Withintraining,weuseastratifiedk-foldcross-validation
(k =5)toselecthyperparameters. Wefixaglobalrandomseed(e.g.,42)andrepeateach
experimentr =3times;wereportmean±standarddeviation.
7.2.2. PreprocessingandLeakagePrevention
Categorical features are one-hot encoded; numerical features are left unscaled for
treeensembles. Toavoidcustomer-levelleakage,alltransactionsbelongingtothesame
customer(oraccountidentifieravailable)areassignedtothesame split. Featurederivations
useonlypastinformationrelativetotransactiontime(nolook-ahead).
7.2.3. HyperparameterTuning
WeperformrandomizedsearchwithN =50configurationspermodel,selectingby
validationAUPRC.
• RF/ET:n_estimators∈ {200,400,800},max_depth∈ {None,8,12,16},max_features
∈ {sqrt,log2,0.5},min_samples_leaf∈ {1,2,5,10}.
• XGB: n_estimators ∈ {300,600,1000}, learning_rate ∈ [0.02,0.2], max_depth ∈
{4,6,8},subsample,colsample_bytree∈ [0.6,1.0],reg_alpha,reg_lambda∈ [0,10].
7.2.4. ProbabilityCalibrationandThresholding
Wecalibratescoreswithisotonicregressiononthevalidationfoldsandchoosethe
operatingthresholdtominimizeexpectedcost:
Cost=C ·FN+C ·FP,
FN FP

Appl.Sci.2025,15,11787
18of32
withC /C setbybusinessconstraints(e.g.,50:1). Wealsoreportthreshold-freemetrics
| FN FP |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- |
(AUPRCandAUROC).
7.2.5. EvaluationMetrics
Inadditiontoprecision/recall/F1andFPRalreadyreported,weadd(i)areaunder
theprecision–recallcurve(AUPRC),(ii)Precision@KandRecall@K(K=top0.1%and0.5%
scoredtransactions),(iii)calibration(Brierscore;reliabilityplot),and(iv)costcurvesfor
| severalC /C | ratios. |     |     |     |     |
| ----------- | ------- | --- | --- | --- | --- |
FN FP
7.3. ResultsandAnalysis
Testsplitandprevalence. Theheld-outtestsetcontainsN =5000transactionswith
afraudprevalenceof2.37%(119positives). WereportAUPRCandRecall@K(K=0.1%
and0.5%oftop-rankedtransactions),inadditiontostandardmetrics. AUPRCiscomputed
fromout-of-samplefraudprobabilities;Recall@Kistherecallachievedwhenscreeningthe
topK%transactionsrankedbythemodelscore(K=0.1%⇒5alerts;K=0.5%⇒25alerts).
(seeFigure1andTable4)
Table 4. Case Study 1—test set results (N = 5000; prevalence 2.37%). We report accuracy, F1
(weighted),AUPRC,andRecall@K.
| Model              | Accuracy | F1(w)  | AUPRC Recall@0.1% | Recall@0.5% |        |
| ------------------ | -------- | ------ | ----------------- | ----------- | ------ |
| RandomForest       | 0.9838   | 0.9801 | 0.6188            | 0.0336      | 0.2017 |
| GradientBoosting   | 0.9810   | 0.9756 | 0.5153            | 0.0336      | 0.1765 |
| KNN                | 0.9806   | 0.9755 | 0.4123            | 0.0336      | 0.1933 |
| LogisticRegression | 0.9768   | 0.9733 | 0.3263            | 0.0336      | 0.1261 |
| AdaBoost           | 0.9756   | 0.9675 | 0.1914            | 0.0336      | 0.1008 |
| SVC(probability)   | 0.9772   | 0.9672 | 0.4957            | 0.0336      | 0.1849 |
Bestmodelandconfusionmatrix.ThebestoverallmodelisRandomForest(F1(w) = 0.9801;
| AUPRC = 0.6188).Atthedefaultdecisionthreshold,itsconfusionmatrixis |                   |         |          |     |     |
| ------------------------------------------------------------------ | ----------------- | ------- | -------- | --- | --- |
|                                                                    | (cid:34)          |         | (cid:35) |     |     |
|                                                                    |                   | TN=4878 | FP=3     |     |     |
|                                                                    |                   | FN=78   | TP=41    |     |     |
|                                                                    | =                 | =       |          |     |     |
| (precision fraud                                                   | 0.93;recall fraud | 0.34).  |          |     |     |
Operationalscreening(Recall@K).Rankingbythefraudscore,RandomForestre-
trievesthefollowing: (i)Recall@0.1% = 0.0336 ⇒ amongthetop5alerts, itcatches ∼4
frauds(of119);(ii)Recall@0.5%=0.2017⇒amongthetop25alerts,itcatches∼24frauds.
Thesefiguresprovideanactionabletriageviewforlimitedhumancapacityandcomplement
threshold-basedmetrics.
Takeaways. (1)Rankingquality: Tree/boostingmethods(RFandGBDT)dominate
AUPRC,confirmingbetterorderingofrarepositivesunderheavyimbalance. (2)Capacity-
awarerecall: Withonly25top-rankedalerts,RFrecoversroughlyone-fifthofallfrauds—
usefulwhenmanualreviewbandwidthistight. (3)Thresholdvs. ranking: Highaccuracy
withlowfraudrecallatafixedthresholdsuggestscost-awarethresholdingortop-Kreview
aspreferredoperatingmodesinproduction.

Appl.Sci.2025,15,11787 19of32
Figure1. CaseStudy1—precision–recallcurveforthebestmodel(RandomForest). Theaverage
precision(AUPRC)is0.619onthetestset.
7.4. PerformanceAnalysisandOperationalImplications
Thedetailedresultspresentedhighlightthepersistentchallengesinoperationalfraud
detection. While the overall accuracy is high, it remains a misleading metric in this
imbalancedcontext. Amoreinsightfulanalysisfocusesonthetrade-offbetweenranking
quality(AUPRC)andthemodel’sperformanceatafixeddecisionthreshold.
Thebest-performingmodel,RandomForest,achievesanAUPRCof0.619,indicating
a good ability to rank fraudulent transactions higher than legitimate ones. However,
thisrankingstrengthdoesnottranslatetosufficientperformanceatastandarddecision
threshold. Themodel’srecallforthefraudclassisonly0.34. Operationally,thisisthemost
criticalfinding: thesystem,evenatitsbest,failstodetectroughlytwo-thirds(66%)ofall
fraudulenttransactions,representinganunacceptablelevelofriskforafinancialinstitution.
Whilethemodel’shighprecision(0.93)ensuresthatthefewalertsitgeneratesare
highly reliable, this comes at the severe cost of a large number of missed frauds (false
negatives). This starkly illustrates that even a well-ranked model can be operationally
ineffectiveifdeployedwithasimplethreshold-basedstrategy.
Thepersistentlylowrecallsuggeststhatthechallengemaybeinherenttothedata
itself, where fraudulent patterns are too subtle or similar to legitimate behavior to be
distinguishedbystandardmodelsalone. Whilethisstudyfocusedontree-basedensembles,
the literature indicates that more advanced strategies could yield better results. These
includedata-levelapproacheslikesyntheticoversampling(e.g.,SMOTE)tocreateamore
balancedtrainingset[113,116],algorithm-levelapproachessuchascost-sensitivelearning
thatassignsahigherpenaltytomisclassifyingfrauds[12,115], andhybridmodelsthat
combineanomalydetectionwithsupervisedclassification[85,86].
Ultimately,thisanalysisconfirmsthatthesupervisedmethodstested,whenusedin
isolation,areinsufficientforrobuststandalonedeployment. Thefundamentalchallenge
ofbalancingadequatefrauddetection(highrecall)withanacceptablelevelofcustomer
friction (high precision) requires moving beyond standard models toward either more
sophisticatedarchitecturesordifferentoperationalparadigms,suchasthetop-Kscreening
exploredinourRecall@Kanalysis.

Appl.Sci.2025,15,11787 20of32
7.5. ImplicationsforFraudDetectionResearch
This case study underscores several persistent challenges outlined throughout
thisreview:
1. Class Imbalance Impact: The low prevalence of fraud (1.43% in this experiment)
makes it extremely difficult for models to learn distinctive fraud patterns without
specializedtechniquesandcarefulalgorithmselection.
2. Misclassification Cost Asymmetry: The relatively low recall for fraud detection
meansasignificantproportionoffraudswouldremainundetected. Conversely,even
alowFPRcantranslateintonumerousfalsealarms,emphasizingthecriticalneedfor
cost-sensitivelearningapproaches.
3. ModelSelectionandOptimization: Theperformancevariessignificantlybetween
models,withETshowingslightadvantagesinF1-scoreandrecallforfraudinthisspe-
cificinstance.Thishighlightsthenecessityforcarefulmodelselection,hyperparameter
optimization,andpotentiallyensembleapproaches.
4. NeedforAdvancedMethodologies:Theresultssuggestthatbasicsupervisedmodels,
evenwithfeatureengineering,maynotsufficeforrobustfrauddetection. Thispoints
towardtheimportanceofexploringhybridmethods,advancedensembletechniques,
deeplearningapproaches,orsophisticatedunsupervisedanomalydetectionsystems.
Thispracticalapplicationdemonstratesthat,whilemachinelearningofferspower-
fulanalyticaltools,achievingeffectiveandoperationallyviablefrauddetectionsystems
requires addressing inherent challenges through sophisticated methodologies, careful
evaluation protocols, and approaches specifically tailored to the financial context and
businessrequirements.
8. CaseStudy2: ApplicationofRandomForestonaReal-WorldBank
TransferDataset
8.1. Dataset
The initial dataset was extracted from the Intesa Sanpaolo (ISP) database, or-
ganized in a table containing 90,314 records of anonymous users’ bank transfers.
The dataset exhibits strong class imbalance, with only 3285 fraudulent transactions
among90,314totaltransactions(∼3.6%). Allthedatawereencryptedandanonymized
to ensure privacy and compliance with regulatory requirements. In particular, all the
categoricalandtextualvariableswerehashedusingtheSHA-256algorithm. Forcompu-
tationalpurposesandtoenabletherunningofmachinelearningalgorithms,thehashed
informationwasfurthertransformedintonumericalrepresentationsthroughappropriate
encodingstrategies.
Eachtransactionisdescribedbyasetofvariablesthatunderwentafeatureengineering
processtoderivetemporal,spatial,financial,technical,andcontextualfeatures. Temporal
informationincludesthehour,day,dayoftheweek,andaweekendindicator,whilespatial
datacapturethelatitudeandlongitudeofthetransactionorigin. Financialattributescom-
prisethetransactionamount,currencycode,divisibilityflags(by2,3,5,or10),anddecimal
patterns(e.g.,0.00,0.50,and0.99). ThedatasetalsoincludesmetadatasuchastheBank
IdentifierCode(BIC)countrycode,bankcodes,clienttype,andmobilecarrierinformation.
Securityandauthenticationindicatorsareavailabletocharacterizethetransactionenvi-
ronment,includingflagsforsecureappusage,fingerprintauthentication,instantpayment,
andadditionalelementssuchasfingerprintcertificate,securesessionID,anddigitalsigna-
ture. Furthermore,theIPaddressassociatedwitheachtransactionhasbeendecomposed
intoitsfouroctetsandencrypted,ensuringfullcompliancewithprivacystandards.

Appl.Sci.2025,15,11787 21of32
Finally,thedatasetcontainssemanticinformationderivedfromthetransactiondescrip-
tionfield(causalfield),representedasafixed-lengthWord2Vecembedding(10dimensions),
and a set of flags describing the access environment (e.g., access mode, device model,
operatingsystem,applicationnameandversion,useragent,andconnectiontype).
8.2. Experiments
Inclassificationproblems,itiscommontoencounterimbalanceddata,wherecertain
classesaresignificantlyunderrepresentedcomparedtoothers. Typicalexamplesinclude
fraud detection, where fraudulent transactions may represent less than 5% of the data,
ormedicaldiagnostics,whereadiseasemightonlyappearinasmallfractionofthepop-
ulation. Whentrainedonsuchdatawithoutanycorrectivemeasures, aclassifiertends
tobebiasedtowardthemajorityclass,oftenresultinginhighoverallaccuracybutpoor
performanceontheminorityclass. Thisimbalanceseverelylimitsthemodel’susefulnessin
real-worldscenarios,wherecorrectidentificationoftheminorityclassisoftentheprimary
objective. To address this issue, the Random Forest algorithm offers the class_weight
parameter,whichallowsassigningdifferentweightstoclasseswiththeaimofpenalizing
misclassificationsofminorityclassesmoreheavily. Byintroducingclass_weight,thede-
cisioncriteriausedtoconstructeachindividualtree(suchasGiniimpurityorentropy)
aremodifiedtoaccountfortherelativeimportanceofeachclass. Thisadjustmentleadsto
splitsthataremoresensitivetominoritysamples,therebyimprovingthemodel’sabilityto
identifythem. Forthesereasons,weperformedthreeclassificationexperimentsadopting
theRandomForestalgorithmwithdifferentsetupsoftheclass_weightparameter. Inpar-
ticular,inthefirstexperiment,itwassetto“None”(thedefault). Inthisway,alltheclasses
aretreatedequally,whichisgenerallyinappropriateinthepresenceofclassimbalance.
Inthesecondexperiment,itwassetto“balanced”. Thealgorithmautomaticallyadjusts
weightsinverselyproportionaltoclassfrequenciesintheentiretrainingset, effectively
compensatingforimbalanceandencouragingthemodeltopaymoreattentiontominority
classes. In the third experiment, setting it to “balanced_subsample” results in weights
beingcomputedinthesamewayas“balanced”,buttheseweightsarecalculatedindepen-
dentlyforeachbootstrapsampledrawntotrainanindividualtree. Thiscanleadtoslightly
differentweightingacrosstrees,potentiallyimprovingrobustnesswhenclassdistributions
varyacrossdifferentsubsetsofthedata.
8.3. ResultsandCriticalAnalysis
To evaluate the impact of different class_weight settings on model performance,
we applied the Random Forest models to a held-out test set. The test split contains
23,310 transactions, with a fraud prevalence of 3.39%. In addition to standard metrics,
wereportAUPRCandRecall@K,whichareparticularlyinformativeinimbalancedclas-
sificationscenarios. AUPRCiscomputedfromout-of-samplefraudprobabilities,while
Recall@K measures the fraction of fraud cases captured when screening the top K% of
transactions ranked by the model score (K = 0.1% corresponds to ∼23 alerts; K = 0.5%
correspondsto∼117alerts). Thesemetricsallowustoassesshowwelleachclass_weight
configurationimprovestheidentificationoftheminority(fraud)classinarealisticsetting.
Theresultsofthethreeexperiments, summarizedinTable5, arestrikinglysimilar
andprovideclearinsightintothelimitationsofsimplealgorithmicadjustmentsforclass
imbalance. Thisuniformityisthefirstandmostimportantfinding: simplealgorithmic
adjustmentslikeusingclass_weight(bothbalancedandbalanced_subsample)didnot
leadtoanysubstantialperformanceimprovements. Moreover,despitethehighoverall
accuracyandarelativelyhighweightedF1-score(botharound0.97),theseglobalmetrics

Appl.Sci.2025,15,11787
22of32
aremisleadinginthepresenceofextremeclassimbalanceandmaskthemodel’scritical
failuretoidentifytheminorityclass.
Table5. CaseStudy2—testsetresults(N=23,310;prevalence= 3.39%). Wereportaccuracy,F1
(weighted),AUPRC,andRecall@K.
ccclllaaassssss___wwweeeiiiggghhhttt
|                    | Accuracy | F1(w)  | AUPRC  | Recall@0.1% | Recall@0.5% |
| ------------------ | -------- | ------ | ------ | ----------- | ----------- |
| None(Default)      | 0.9769   | 0.9721 | 0.6969 | 0.0291      | 0.1403      |
| balanced           | 0.9753   | 0.9694 | 0.6787 | 0.0291      | 0.1365      |
| balanced_subsample | 0.9753   | 0.9694 | 0.6787 | 0.0291      | 0.1365      |
Among the three configurations, the model trained with class_weight = None
achievedthebestoverallbalancebetweenprecisionandrecall. Thecorrespondingconfu-
sionmatrixontheheld-outtestsetisreportedbelow:
|     | (cid:34)  |        |        | (cid:35) |     |
| --- | --------- | ------ | ------ | -------- | --- |
|     | TN=22,487 |        | FP=32  |          |     |
|     |           | FN=506 | TP=285 |          |     |
with precision = 0.90 and recall = 0.36. In Figure 2, the PR curve for
fraud fraud
| class_weight = Noneisshown. |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- |
Figure2. CaseStudy2—precision–recallcurveforclass_weight = None. Theaverageprecision
(AUPRC)is0.697onthetestset.
EventhoughtheAUPRCismoderatelyhigh,suggestingthatthemodelisabletodis-
tinguishbetweenclasses,therecallatlowdetectionratesiscriticallylow. Forexample,ata
thresholdof0.1%,themodelonlyidentifiesapproximately2.9%offraudulenttransactions.
Fromanoperationalperspective,thisisasignificantfinding: evenwhenthemodel
isexplicitlyinstructedtopenalizeerrorsontheminorityclassmoreheavily,itstillfails
to identify the vast majority of fraudulent transactions. This outcome highlights a key
limitationoftheclass_weightparameter. Whileitadjuststhecostfunction,itdoesnot
generate new information or alter the feature space. If the fraudulent transactions are
locatedindenseoverlappingregionswithlegitimatetransactions,simplyincreasingtheir
weightisofteninsufficienttoallowthealgorithmtofindacleangeneralizableseparation
boundary. Themodelremainsunabletolearnadistinctpatternfromthefewavailable
positivesamples.
Therefore,theseresultsstronglysuggestthatmoresophisticatedstrategiesarerequired.
Amorepromisingpathwouldbetoexploredata-leveltechniquesthatdirectlymodifythe

Appl.Sci.2025,15,11787 23of32
dataset,suchasoversampling(e.g.,SMOTE)toincreasethenumberofminoritysamplesor
undersamplingtoreducethemajorityclass.Anotherpowerfulalternative,supportedbythe
literature,liesinusingadvancedensemblemethodsspecificallydesignedforimbalanced
dataorhybridapproachesthatcanisolateanomalouspatternsbeforeafinalclassification
occurs[12,85].
Inconclusion,thiscasestudyservesasapracticaldemonstrationthattacklingsevere
classimbalancerequiresmorethanasingleparametertweak.Itunderscoresthenecessityof
employingmultifacetedstrategiesthateitherreshapethedataorusealgorithmsinherently
designedtohandlesuchchallengingconditions.
9. ChallengesandFutureDirections
DespitesignificantadvancesinML-basedfrauddetection,severalpersistentchallenges
continuetolimitsystemeffectiveness,whilenewopportunitiesareemerginginthisrapidly
evolvingfield.
9.1. CurrentChallenges
9.1.1. DataImbalanceandFeatureEngineering
Theextremeclassimbalanceinfrauddatasetsremainsafundamentalandpersistent
challenge. Fraudulent transactions typically constitute less than 1% of all transactions,
makingitexceptionallydifficultformodelstolearndiscriminativefeaturesfortheminority
classwithoutspecializedtechniques[4,5]. Compoundingthisissueisthecomplexityof
featureengineering,whichiscrucialforsuccessbutrequiressubstantialdomainexpertise
andisoftenlabor-intensive[123].
Furthermore,drawinginspirationfromadvancesincomputervision,suchasmeth-
ods for learning robust feature representations in complex scenes for accurate human
parsing [124], could offer valuable pathways to improve feature extraction and model
generalizationintheintricatedomainoffinancialtransactions.
9.1.2. ConceptDriftandReal-TimeRequirements
Fraudpatternsevolvecontinuously, leadingtoconceptdrift, whereamodel’sper-
formance degrades as the relationship between features and fraud likelihood changes.
Developingmodelsthatcanadapttotheseevolvingpatternswithoutrequiringfrequentre-
trainingremainsasignificantchallenge[7]. Thisisfurthercomplicatedbymodernfinancial
systemsthatrequirereal-timedetection,imposingstrictconstraintsonmodelcomplexity
andcomputationallatency.
Moreover,theadversarialnatureoffrauddetectionsharessimilaritieswithchallenges
ininformationsecurity. Techniquesdevelopedforrobustwatermarkingagainstgeometric
attacks[125],whichfocusonresistingcomplexinterference,mayprovideusefulinsights
forbuildingfrauddetectionsystemsresilienttodynamicenvironmentsandsophisticated
adversarialattempts.
9.1.3. The“Black-Box”ProblemandtheNeedforExplainableAI(XAI)
As fraud detection models become increasingly complex, their interpretability de-
creases,creatinga“blackbox”thatisproblematicinregulatoryenvironments. Financial
regulations,suchastheGDPR’s“righttoexplanation,”demandthatinstitutionsbeableto
justifyautomateddecisions. Thismakesexplainabilitynotjustadesirablefeaturebuta
criticalcompliancerequirement[8,9].
ExplainableAI(XAI)providesapathwaytoaddressthischallenge. Techniqueslike
SHAPs(SHapleyAdditiveexPlanations)andLIMEs(LocalInterpretableModel-Agnostic
Explanations)aregainingsignificanttractionforprovidingtransparency[7].Forthemodels

Appl.Sci.2025,15,11787 24of32
inourcasestudies,thesemethodscouldbeappliedtoprovidecrucialinsights.Forinstance,
foratransactionflaggedbyourRandomForestmodel,SHAPvaluescouldrevealprecisely
whichfeatures—suchasanunusuallyhightransactionamount(num_impor),anatypical
time of day (num_hour), or a high-risk country code—were the primary drivers behind
thefraudclassification. Thistransformsanopaquealertintoanactionableandauditable
insightforfraudanalysts.
9.1.4. DataPrivacy,Security,andthePromiseofFederatedLearning
Fraud detection systems require access to vast amounts of sensitive financial data,
raisingsignificantprivacyandregulatoryconcerns[20]. Centralizingcustomerdatafrom
multiplesourcescreatesahigh-valuetargetforcyberattacksandcomplicatescompliance
withdataprotectionlaws. Federatedlearningemergesasapowerfulprivacy-preserving
paradigmtoovercomethisobstacle[126].
Insteadofpoolingrawdata, federatedlearningallowsmultipleinstitutionstocol-
laboratively train a shared model without ever exposing their confidential data. Each
institutiontrainsthemodellocallyonitsowndataset,andonlytheresultingmodelup-
dates(anonymousparametersorgradients)aresenttoacentralserverforaggregation.
Thisapproachallowsaglobalmodeltolearnfromamuchwiderandmorediverseset
offraudpatterns—improvingitsaccuracyandrobustness—whileensuringthatsensitive
customerinformationneverleavesthesecureperimeterofeachparticipatinginstitution.
9.1.5. AlgorithmicBiasandEthicalImplications
Asignificant,andoftenoverlooked,challengeistheriskofembeddingsocietalbiases
intoautomatedfrauddetectionsystems. Ifhistoricaldatausedfortrainingcontainsbiases,
anMLmodelwilllearnandamplifythem. Forexample,amodelmightunfairlyassociatea
higherriskoffraudwithtransactionsoriginatingfromlow-incomeneighborhoodsorwith
specificdemographicgroupssimplybecauseofhistoricaldataimbalancesorprejudiced
policingpracticesreflectedinthedata. Thiscanleadtodiscriminatoryoutcomes,where
certaingroupsoflegitimatecustomersaresubjectedtohigherratesofdeclinedtransactions
oraccountblockages.
Theethicalimplicationsofsuchbiasesareprofound,posingsignificantreputational
andlegalriskstofinancialinstitutions[9]. Addressingthisrequiresadedicatedfocuson
fairnessthroughoutthemodellifecycle. Thisincludesconductingbiasauditsondatasets,
employingfairness-awaremachinelearningalgorithms,andregularlymonitoringmodel
predictions to ensure equitable treatment across different user groups. The pursuit of
accuracymustbebalancedwithacommitmenttofairnessandethicalresponsibility.
9.2. EmergingTrendsandOpportunities
9.2.1. DeepLearningAdvances
Deeplearningapproaches,particularlythosedesignedforsequentialdataanalysis
(e.g.,LSTMandGRU),showconsiderablepromiseforcapturingcomplextemporalpatterns
intransactionsequencesandbehavioraldata[76,90].
9.2.2. Graph-BasedMethods
Graph-based approaches that model complex relationships between entities (cus-
tomers,merchants,transactions,andaccounts)areemergingaseffectivetoolsfordetect-
ing sophisticated fraud schemes involving multiple participants and complex network
structures[127].
Thesemethodsexcelatuncoveringcoordinatedfraudulentactivities,suchasmoney
launderingringsorcollusionnetworks,thataredifficulttodetectwithtransaction-level

Appl.Sci.2025,15,11787 25of32
models. However,theircomputationalcomplexityandtheneedforgraph-specificdata
structurescanbebarrierstoimplementation.
9.2.3. FederatedLearning
Federatedlearningapproachesallowmodelstobetrainedacrossmultipleinstitutions
withoutsharingrawsensitivedata,addressingprivacyconcernswhileleveragingbroader
datasourcesandcollectiveintelligence[126].
9.2.4. ExplainableAIIntegration
Techniquesforexplainingmodeldecisionsarebecomingincreasinglyimportantin
frauddetectionapplications,withmethodslikeSHAPs(SHapleyAdditiveexPlanations)
andLIMEs(LocalInterpretableModel-AgnosticExplanations)gainingsignificanttraction
forregulatorycomplianceandoperationaltransparency[7].
Grad-CAMrepresentsavaluableapproachformodeldebugging,usinggradientsas
importancemeasuresinfeaturespace. ItdoesnotrequirespecificCNNarchitecturesand
canbeappliedtoanygradient-basedneuralnetworkmodel. SHAPvalues,derivedfrom
cooperative game theory, assess feature contributions by analyzing prediction changes
whenfeaturesareremovedfromfeaturesets.
9.2.5. SyntheticDataGeneration
Advancedtechniquesforgeneratingrealisticsyntheticfrauddata,suchasGANsand
variationalautoencoders,arebeingexploredtoaddressdatascarcityandprivacyconcerns
whileprovidingdiversetrainingscenarios[84,107].
9.2.6. HybridandEnsembleApproaches
SophisticatedcombinationsofmultipleMLtechniques,leveragingthecomplemen-
tarystrengthsofdifferentapproaches,showsignificantpromiseforimprovingdetection
performanceacrossdiversefraudscenariosandoperationalcontexts[81,128].
9.2.7. TransferLearningApplications
Transfer learning approaches that can leverage knowledge gained from one fraud
detectiontasktoimproveperformanceonrelatedtaskswithlimiteddataareemergingas
valuabletechniquesforaddressingdatascarcityinspecificdomains[6].
9.3. FutureResearchDirections
Basedon ourcomprehensive analysis, severalpromising directionsfor future
researchemerge.
9.3.1. AdvancedUnsupervisedTechniques
Furtherexplorationofsophisticatedunsupervisedandsemi-supervisedtechniquesis
needed,particularlyfordetectingnovelfraudpatternsnotrepresentedinhistoricallabeled
dataandforaddressingthechallengeoflimitedlabeledfraudexamples[35,108].
9.3.2. Real-TimeAdaptiveSystems
Developmentoffrauddetectionsystemsthatcanadapttoevolvingfraudpatternsin
realtime,withoutrequiringperiodicretrainingormanualintervention,wouldeffectively
addressthepersistentchallengeofconceptdrift[7].
9.3.3. ComprehensiveEvaluationFrameworks
Standardizedframeworksforevaluatingfrauddetectionsystemsthatconsidermul-
tipleperformancedimensions(accuracy,interpretability,computationalefficiency,adapt-

Appl.Sci.2025,15,11787 26of32
ability, and regulatory compliance) would facilitate meaningful comparisons between
approachesandaccelerateresearchprogress[117].
9.3.4. Domain-SpecificApproaches
Tailoredapproachesforspecificfraudtypes(e.g.,moneylaundering,insurancefraud,
and tax evasion) that incorporate domain-specific knowledge, regulatory constraints,
andoperationalrequirementscouldsignificantlyimprovedetectioneffectiveness[28,32].
9.3.5. Cross-OrganizationalCollaboration
Frameworksforcollaborativefrauddetectionacrossorganizationsthatpreservedata
privacywhileleveragingbroaderpatternrecognitioncapabilitiescouldenhancedetection
ofsophisticatedfraudschemesthatspanmultipleinstitutions[112].
9.3.6. BehavioralAnalysisIntegration
Integrationofadvancedbehavioralanalyticsthatmodelnormaluserbehaviorpatterns
anddetectsubtledeviationscouldimprovefrauddetectionaccuracywhilereducingfalse
positivesandenhancinguserexperience[36].
9.3.7. EthicalConsiderations
Researchontheethicalimplicationsofautomatedfrauddetection,includingfairness,
biasmitigation,transparency,andaccountability,isincreasinglyimportantasthesesystems
becomemorewidespreadandinfluential[9].
10. Conclusions
This comprehensive review has presented a systematic analysis of machine learn-
ingtechniquesforfinancialfrauddetection,examiningthecurrentstateoftheresearch,
practicalapplications,andemergingtrends. Ouranalysisconfirmsthedominanceofsuper-
visedlearningmethodsintheliterature,butitalsohighlightsthepersistentfundamental
challengesthatlimittheireffectivenessinreal-worldoperationalenvironments.
Theuniquecontributionofthispaperliesinbridgingtheoreticalknowledgewitha
criticalassessmentofpracticalapplication. Weachievethisthroughtwocasestudieson
proprietaryreal-worldbankingdata,whichmovethediscussionfromabstractperformance
toconcreteoperationaltrade-offs. Crucially,ourexperimentsrevealapersistentandcritical
limitation: evenwithhyperparametertuningandclassweightadjustments,themodels
struggletoachieveadequaterecallfortheminority(fraud)class. Thisfindingisnotmerely
atechnicalresult;itisastrategicinsightdemonstratingthatstandardsupervisedmodels,
when used in isolation, are often insufficient to overcome the extreme class imbalance
inherentinfinancialfrauddata.
Thisidentifiedgapdirectlyinformsamorestrategicvisionforfutureresearch.Thelow
recallobtainedhighlightstheneedtoexplorehybridarchitectureswithresamplingorcost-
sensitivemodels. Futureworkshouldfocusonhybridmodelsthatcombineunsupervised
anomaly detection for identifying novel threats with supervised classifiers trained on
enricheddatasetsusingadvancedresampling(e.g.,SMOTEvariations)orgenerative(e.g.,
GANs) techniques. Furthermore, to meet the regulatory and operational demands for
transparency,theintegrationofExplainableAI(XAI)isnolongeroptional. Techniqueslike
SHAPsandLIMEsmustbeembeddedintothedevelopmentlifecycletotransitionfrom
“black-box”predictorstodecision-supportsystemsthatprovideclearactionablerationales
forfraudalerts.
Asfinancialsystemsbecomeincreasinglyinterconnected,thepathforwardrequiresa
shifttowardsmoreadaptive,interpretable,andcollaborativesystems. Researchshouldpri-
oritizereal-timeadaptivemodelsthatarecapableofcounteringconceptdrift,andprivacy-

Appl.Sci.2025,15,11787 27of32
preservingframeworkslikefederatedlearningtoenablecross-institutionalcollaboration
withoutcentralizingsensitivedata. Byfocusingonthesestrategicdirections—inspired
directlybythepracticallimitationsobserved—theresearchcommunitycandevelopmore
robustandeffectivedefensesagainstthepersistentandevolvingthreatoffinancialfraud.
Successinthisendeavorwillrequireclosecollaborationbetweenresearchers,practi-
tioners,financialinstitutions,andregulatorybodiestoensurethattechnologicaladvances
translateintopractical,transparent,andethicallysoundsolutionsthatprotecttheintegrity
oftheglobalfinancialecosystem.
AuthorContributions: Conceptualization, A.P., A.A.C., Y.M., S.C., G.R.andR.C.; methodology,
A.P.,A.A.C.,Y.M.,S.C.,G.R.andR.C.;software,A.P.,A.A.C.,Y.M.,S.C.,G.R.andR.C.;validation,
A.P., A.A.C., Y.M., S.C., G.R. and R.C.; formal analysis, A.P., A.A.C., Y.M., S.C., G.R. and R.C.;
investigation,A.P.,A.A.C.,Y.M.,S.C.,G.R.andR.C.;datacuration,A.P.,A.A.C.,Y.M.,S.C.,G.R.and
R.C.;writing—originaldraftpreparation,A.P.,A.A.C.,Y.M.,S.C.,G.R.andR.C.;writing—reviewand
editing,A.P.,A.A.C.,andA.T.;visualization,A.P.andA.A.C.;supervision,A.P.Allauthorshaveread
andagreedtothepublishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
InstitutionalReviewBoardStatement:Allanalyseswereconductedonanonymizedrecordsunder
institutionalagreementswithstrictaccesscontrolsandaudittrails.Onlyfeaturesnecessaryforfraud
detectionwereprocessed(dataminimization),andresultswerereportedataggregatelevelwithout
anyattemptatre-identification.
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement:ThedatausedinCaseStudy1andCaseStudy2consistofproprietary
banktransactions.Thedatapresentedinthisstudyareavailableonrequestfromthecorresponding
author.Thedataarenotpubliclyavailableduetolegalandcontractualrestrictions.
Acknowledgments:TheauthorsacknowledgesupercomputingresourcesandsupportfromICSC—
CentroNazionalediRicercainHighPerformanceComputing,BigDataandQuantumComputing—
andhostingentity,fundedbyEuropeanUnion—NextGenerationEU.Theviewsandopinionsex-
pressed are those of the authors and do not necessarily reflect the views of Intesa Sanpaolo, its
affiliates,oritsemployees.
ConflictsofInterest:AuthorRiccardoCrupiwasemployedbythecompanyIntesaSanpaoloS.p.A.
Theremainingauthorsdeclarethattheresearchwasconductedintheabsenceofanycommercialor
financialrelationshipsthatcouldbeconstruedasapotentialconflictofinterest.
References
1. PricewaterhouseCoopers.EncuestaGlobaldeCrimenyFraudeEconómicodePwCColombia2022–2023;PricewaterhouseCoopers:
London,UK,2022.
2. Reurink,A.Financialfraud:Aliteraturereview.J.Econ.Surv.2018,32,1292–1325.[CrossRef]
3. Ahmed,M.;Mahmood,A.N.;Islam,M.R.Asurveyofanomalydetectiontechniquesinfinancialdomain.FutureGener.Comput.
Syst.2016,55,278–288.[CrossRef]
4. Femila,Roseline,J.F.;Naidu,G.;SamuthiraPandi,V.;AlamelualiasRajasree,S.;Mageswari,D.N.Autonomouscreditcardfraud
detectionusingmachinelearningapproach.Comput.Electr.Eng.2022,102,108132.[CrossRef]
5. Tingfei,H.;Guangquan,C.;Kuihua,H.Usingvariationalautoencodingincreditcardfrauddetection. IEEEAccess2020,8,
149841–149853.[CrossRef]
6. Dantas,R.M.;Firdaus,R.;Jaleel,F.;NevesMata,P.;Mata,M.N.;Li,G.Systemicacquiredcritiqueofcreditcarddeceptionexposure
throughmachinelearning.J.OpenInnov.Technol.Mark.Complex.2022,8,192.[CrossRef]
7. DalPozzolo,A.;Caelen,O.;LeBorgne,Y.A.;Waterschoot,S.;Bontempi,G.Learnedlessonsincreditcardfrauddetectionfroma
practitionerperspective.ExpertSyst.Appl.2022,41,4915–4928.[CrossRef]
8. Makki,S.;Assaghir,Z.;Taher,Y.;Haque,R.;Hacid,M.S.;Zeineddine,H.Anexperimentalstudywithimbalancedclassification
approachesforcreditcardfrauddetection.IEEEAccess2019,7,93010–93022.[CrossRef]

Appl.Sci.2025,15,11787 28of32
9. Rakowski,R.;Polak,P.;Kowalikova,P.EthicalaspectsoftheimpactofAI:Thestatusofhumansintheeraofartificialintelligence.
Society2021,58,196–203.[CrossRef]
10. Alarfaj,F.K.;Malik,I.;Khan,H.U.;Almusallam,N.;Ramzan,M.;Ahmed,M.Creditcardfrauddetectionusingstate-of-the-art
machinelearninganddeeplearningalgorithms.IEEEAccess2022,10,39700–39715.[CrossRef]
11. Madhurya, M.J.; Gururaj, H.L.; Soundarya, B.C.; Vidyashree, K.P.; Rajendra, A.B.Exploratoryanalysisofcreditcardfraud
detectionusingmachinelearningtechniques.Glob.TransitionsProc.2022,3,31–37.[CrossRef]
12. Sahin,Y.;Bulkan,S.;Duman,E.Acost-sensitivedecisiontreeapproachforfrauddetection.ExpertSyst.Appl.2013,40,5916–5923.
[CrossRef]
13. Vanini,P.;Rossi,S.;Zvizdic,E.;Domenig,T.Onlinepaymentfraud:Fromanomalydetectiontoriskmanagement.Financ.Innov.
2023,9,66.
14. Srokosz,M.;Bobyk,A.;Ksiezopolski,B.;Wydra,M.Machine-learning-basedscoringsystemforantifraudCISIRTsinbanking
environment.Electronics2023,12,251.[CrossRef]
15. Zhou,H.;Chai,H.;Qiu,M.Frauddetectionwithinbankcardenrollmentonmobiledevicebasedpaymentusingmachinelearning.
Front.Inf.Technol.Electron.Eng.2018,19,1537–1545.[CrossRef]
16. Xiong,T.;Ma,Z.;Li,Z.;Dai,J.Theanalysisofinfluencemechanismforinternetfinancialfraudidentificationanduserbehavior
basedonmachinelearningapproaches.Int.J.Syst.Assur.Eng.Manag.2022,13,996–1007.[CrossRef]
17. Chen,Y.;Wu,Z.FinancialfrauddetectionoflistedcompaniesinChina:Amachinelearningapproach.Sustainability2022,15,105.
[CrossRef]
18. Kumar,S.;Ahmed,R.;Bharany,S.;Shuaib,M.;Ahmad,T.;TagEldin,E.;Rehman,A.U.;Shafiq,M.Exploitationofmachine
learningalgorithmsfordetectingfinancialcrimesbasedoncustomers’behavior.Sustainability2022,14,13875.
19. Sathya,M.;Balakumar,B.Insurancefrauddetectionusingnovelmachinelearningtechnique.Int.J.Intell.Syst.Appl.Eng.2022,
10,374–381.
20. VanCapelleveen,G.;Poel,M.;Mueller,R.M.;Thornton,D.;VanHillegersberg,J.Outlierdetectioninhealthcarefraud:Acase
studyintheMedicaiddentaldomain.Int.J.Account.Inf.Syst.2016,21,18–31.[CrossRef]
21. Aslam,F.; Hunjra,A.; Ftiti,Z.; Louhichi,W.; Shams,T.Insurancefrauddetection: Evidencefromartificialintelligenceand
machinelearning.Res.Int.Bus.Financ.2022,62,101744.
22. Nian, K.; Zhang, H.; Tayal, A.; Coleman, T.; Li, Y.Autoinsurancefrauddetectionusingunsupervisedspectralrankingfor
anomaly.J.Financ.DataSci.2016,2,58–75.[CrossRef]
23. Subudhi,S.;Panigrahi,S.UseofoptimizedfuzzyC-Meansclusteringandsupervisedclassifiersforautomobileinsurancefraud
detection.J.KingSaudUniv.-Comput.Inf.Sci.2020,32,568–575.[CrossRef]
24. Chen,S.Detectionoffraudulentfinancialstatementsusingthehybriddataminingapproach.SpringerPlus2016,5,89.[CrossRef]
[PubMed]
25. Dutta,I.; Dutta,S.; Raahemi,B.Detectingfinancialrestatementsusingdataminingtechniques. ExpertSyst. Appl. 2017,90,
374–393.[CrossRef]
26. Hajek,P.;Henriques,R.Miningcorporateannualreportsforintelligentdetectionoffinancialstatementfraud—Acomprehensive
surveyofmachinelearningmethods.Knowl.-BasedSyst.2017,128,139–152.[CrossRef]
27. Lokanan,M.; Tran,V.; Vuong,N.H.Detectinganomaliesinfinancialstatementsusingmachinelearningalgorithm. AsianJ.
Account.Res.2019,4,181–201.[CrossRef]
28. Alsuwailem,A.A.S.;Salem,E.;Saudagar,A.K.J.Performanceofdifferentmachinelearningalgorithmsindetectingfinancialfraud.
Comput.Econ.2022,62,1631–1667.[CrossRef]
29. Lokanan,M.E.Predictingmoneylaunderingusingmachinelearningandartificialneuralnetworksalgorithmsinbanks.J.Appl.
Secur.Res.2022,19,20–24.[CrossRef]
30. Rocha-Salazar,J.J.;Segovia-Vargas,M.J.;Camacho-Miñano,M.M.Moneylaunderingandterrorismfinancingdetectionusing
neuralnetworksandanabnormalityindicator.ExpertSyst.Appl.2021,169,114470.[CrossRef]
31. Baghdasaryan,V.;Davtyan,H.;Sarikyan,A.;Navasardyan,Z.Improvingtaxauditefficiencyusingmachinelearning:Theroleof
taxpayer’snetworkdatainfrauddetection.Appl.Artif.Intell.2022,36,2012002.[CrossRef]
32. Savic´,M.;Atanasijevic´,J.;Jakovetic´,D.;Krejic´,N.Taxevasionriskmanagementusingahybridunsupervisedoutlierdetection
method.ExpertSyst.Appl.2022,193,116409.[CrossRef]
33. Vanhoeyveld,J.;Martens,D.;Peeters,B.Value-addedtaxfrauddetectionwithscalableanomalydetectiontechniques.Appl.Soft
Comput.2020,86,105895.[CrossRef]
34. Arévalo,F.;Barucca,P.;Téllez-León,I.E.;Rodríguez,W.;Gage,G.;Morales,R.Identifyingclustersofanomalouspaymentsinthe
salvadorianpaymentsystem.Lat.Am.J.Cent.Bank.2022,3,100050.[CrossRef]
35. Rubio,J.;Barucca,P.;Gage,G.;Arroyo,J.;Morales-Resendiz,R.Classifyingpaymentpatternswithartificialneuralnetworks:An
autoencoderapproach.Lat.Am.J.Cent.Bank.2020,1,100013.[CrossRef]

Appl.Sci.2025,15,11787 29of32
36. Hamza,C.;Lylia,A.;Nadine,C.;Nicolas,C.Semi-supervisedmethodtodetectfraudulenttransactionsandidentifyfraudtypes
whileminimizingmountingcosts.Int.J.Adv.Comput.Sci.Appl.2023,14,861–870.[CrossRef]
37. UK Finance. Fraud-The Facts 2021, The Definitive Overview of Payment Industry Fraud. 2021. Available online: https:
//www.ukfinance.org.uk(accessedon20October2025).
38. Langan,T.InternetCrimeReport2023;Tech.rep.;FederalBureauofInvestigation:Washington,DC,USA,2023.
39. Amusan,E.;Alade,O.;Fenwa,O.D.;Emuoyibofarhe,J.O.Creditcardfrauddetectiononskeweddatausingmachinelearning
techniques.LAUTECHJ.Comput.Inform.2021,2,49–56.
40. Ahirwar,A.;Sharma,N.;Bano,A.EnhancedSMOTE&fastrandomforesttechniquesforcreditcardfrauddetection.SolidState
Technol.2020,63,4721–4733.
41. Jonnalagadda,V.;Gupta,P.;Sen,E.Creditcardfrauddetectionusingrandomforestalgorithm.Int.J.Adv.Res.IdeasInnov.Technol.
2019,5,1–5.
42. Geurts,P.;Ernst,D.;Wehenkel,L.Extremelyrandomizedtrees.Mach.Learn.2006,63,3–42.[CrossRef]
43. Pagliaro,A.ForecastingSignificantStockMarketPriceChangesUsingMachineLearning:ExtraTreesClassifierLeads.Electronics
2023,12,4551.[CrossRef]
44. Itoo,F.;Singh,S.Comparisonandanalysisoflogisticregression,NaïveBayesandKNNmachinelearningalgorithmsforcredit
cardfrauddetection.Int.J.Inf.Technol.2021,13,1503–1511.[CrossRef]
45. Adityasundar,N.;SaiAbhigna,T.;Lakshman,B.;Phaneendra,D.;MohanKumar,N.Creditcardfrauddetectionusingmachine
learningclassificationalgorithmsoverhighlyimbalanceddata.J.Sci.Technol.2020,5,138–146.[CrossRef]
46. Soh,W.W.;Yusuf,R.M.Predictingcreditcardfraudonaimbalanceddata.Int.J.DataSci.Adv.Anal.2019,1,12–17.[CrossRef]
47. Li,C.;Ding,N.;Zhai,Y.;Dong,H.Comparativestudyoncreditcardfrauddetectionbasedondifferentsupportvectormachines.
Intell.DataAnal.2021,25,105–119.[CrossRef]
48. Zhang,D.;Bhandari,B.;Black,D.Creditcardfrauddetectionusingweightedsupportvectormachine. Appl. Math. 2020,11,
1275–1291.[CrossRef]
49. Pavithra,T.;Thangadurai,K.TheimprovingperditionofcreditcardfrauddetectiononPSOoptimizedSVM.Int.J.Anal.Exp.
ModalAnal.2019,XI,478–485.
50. Bandyopadhyay,S.;Thakkar,V.;Mukherjee,U.;Dutta,S.Emergingapproachfordetectionoffinancialfraudsusingmachine
learning.Preprints2021.https//doi.org/10.20944/preprints202108.0028.v1.
51. Hammed,M.;Soyemi,J.Animplementationofdecisiontreealgorithmaugmentedwithregressionanalysisforfrauddetectionin
creditcard.Int.J.Comput.Sci.Inf.Secur.2020,18,79–88.
52. Barahim,A.;Alhajri,A.;Alasaibia,N.;Altamimi,N.;Aslam,N.;Khan,I.U.Enhancingthecreditcardfrauddetectionthrough
ensembletechniques.J.Comput.Theor.Nanosci.2019,16,4461–4468.[CrossRef]
53. Borse,D.D.;Patil,S.H.;Dhotre,S.CreditcardfrauddetectionusingnaiveBayesandrobustscalingtechniques.Int.J.2021,10,
1–5.
54. Gupta,A.;Lohani,M.C.;Manchanda,M.FinancialfrauddetectionusingnaiveBayesalgorithminhighlyimbalancedataset.J.
Discret.Math.Sci.Cryptogr.2021,24,1559–1572.[CrossRef]
55. Chowdari,G.B.Supervisedmachinelearningalgorithmsfordetectingcreditcardfraud.EpraInt.J.Res.Dev. 2021,6,131–134..
[CrossRef]
56. Kumar,R.;Student,P.G.;Budihul,R.Anefficientapproachforcreditcardfrauddetection.Int.J.Innov.Sci.Res.Technol.2020,5,
1057–1073.
57. Manlangit,S.;Azam,S.;Shanmugam,B.Novelmachinelearningapproachforanalyzinganonymouscreditcardfraudpatterns.
Int.J.Electron.Commer.Stud.2019,10,175–202.[CrossRef]
58. Agarwal,V.Identitytheftdetectionusingmachinelearning.Int.J.Res.Appl.Sci.Eng.Technol.2021,9,1943–1946.[CrossRef]
59. Asha,R.B.;KR,S.K.Creditcardfrauddetectionusingartificialneuralnetwork.Glob.TransitionsProc.2021,2,35–41.
60. Oumar,A.W.;Augustin,P.CreditcardfrauddetectionusingANN.Int.J.Comput.Sci.Mob.Comput.2019,8,257–260.
61. Niu, X.; Wang, L.; Yang, X. A comparison study of credit card fraud detection: Supervised versus unsupervised. arXiv
2019,arXiv:1904.10604.[CrossRef]
62. Faraj,A.A.;Mahmud,D.A.;Rashid,B.N.Comparisonofdifferentensemblemethodsincreditcarddefaultprediction.UHDJ.Sci.
Technol.2021,5,20–25.[CrossRef]
63. Dalal, S.; Seth, B.; Radulescu, M.; Secara, C.; Tolea, C. Predicting fraud in financial payment services through optimized
hyper-parameter-tunedXGBoostmodel.Mathematics2022,10,4679.[CrossRef]
64. Meenu;Gupta,S.;Patel,S.;Kumar,S.;Chauhan,G.Anomalydetectionincreditcardtransactionsusingmachinelearning.Int.J.
Innov.Res.Comput.Sci.Technol.2020,8,2347–5552.
65. Vijayakumar,V.;Divya,N.S.;Sarojini,P.;Sonika,K.Isolationforestandlocaloutlierfactorforcreditcardfrauddetectionsystem.
Int.J.Eng.Adv.Technol.2020,9,261–265.[CrossRef]

Appl.Sci.2025,15,11787 30of32
66. Palekar,V.;Kharade,S.;Zade,H.;Ali,S.;Kamble,K.;Ambatkar,S.Creditcardfrauddetectionusingisolationforest.Int.Res.J.
Eng.Technol.2020,7,1–6.
67. Misra,S.;Thakur,S.;Ghosh,M.;Saha,S.K.Anautoencoderbasedmodelfordetectingfraudulentcreditcardtransaction.Procedia
Comput.Sci.2020,167,254–262.[CrossRef]
68. Wu,E.;Cui,H.;Welsch,R.E.Dualautoencodersgenerativeadversarialnetworkforimbalancedclassificationproblem. IEEE
Access2020,8,91265–91275.[CrossRef]
69. Abdulsalami,B.A.; Kolawole,A.A.; Ogunrinde,M.A.; Lawal,M.; Azeez,R.A.; Afolabi,A.Z.Comparativeanalysisofback-
propagationneuralnetworkandK-meansclusteringalgorithminfrauddetectioninonlinecreditcardtransactions.FountainJ.
Nat.Appl.Sci.2019,8,315.[CrossRef]
70. Deb,K.;Ghosal,S.;Bose,D.Acomparativestudyoncreditcardfrauddetection.EngrXiv2021.[CrossRef]
71. Singh,P.andSinghUmrao,L.Creditcardfrauddetectionsystemusingdatamining.OpenNanoRes.J.2024,20,4.[CrossRef]
72. Singh,M.;Kumar,S.;Kumar,S.;Garg,T.CreditcardfrauddetectionusinghiddenMarkovmodel.Int.J.Eng.Comput.Sci.2019,8,
24878–24882.[CrossRef]
73. Danaa,A.A.A.;Daabo,M.I.;Abdul-Barik,A.DetectingelectronicbankingfraudonhighlyimbalanceddatausinghiddenMarkov
models.EarthlineJ.Math.Sci.2021,7,315–332.[CrossRef]
74. Sugidamayatno,S.;Lelono,D.Outlierdetectioncreditcardtransactionsusinglocaloutlierfactoralgorithm(LOF).Indones. J.
Comput.Cybern.Syst.2019,13,409–420.[CrossRef]
75. Alghofaili,Y.;Albattah,A.;Rassam,M.A.AfinancialfrauddetectionmodelbasedonLSTMdeeplearningtechnique.J.Appl.
Secur.Res.2020,15,498–516.[CrossRef]
76. Benchaji,I.;Douzi,S.;ElOuahidi,B.CreditcardfrauddetectionmodelbasedonLSTMrecurrentneuralnetworks.J.Adv.Inf.
Technol.2021,12,113–118.[CrossRef]
77. Cheon,M.J.;Lee,D.H.;Joo,H.S.;Lee,O.Deeplearningbasedhybridapproachofdetectingfraudulenttransactions.J.Theor.Appl.
Inf.Technol.2021,99,4044–4054.
78. Aswathy,M.;Samuel,L.Creditcardfrauddetectionusinghybridmodels.Int.Res.J.Eng.Technol.2019,6,2019.
79. Chen,J.I.Z.;Lai,K.L.Deepconvolutionneuralnetworkmodelforcredit-cardfrauddetectionandalert.J.Artif.Intell.2021,3,
101–112.
80. Bandyopadhyay,S.;Dutta,S.DetectionoffraudtransactionsusingrecurrentneuralnetworkduringCOVID-19:Fraudtransaction
duringCOVID-19.J.Adv.Res.Med.Sci.Technol.2020,7,16–21.[CrossRef]
81. Forough,J.;Momtazi,S.Ensembleofdeepsequentialmodelsforcreditcardfrauddetection.Appl.SoftComput.2021,99,106883.
[CrossRef]
82. Sadgali,I.;Sael,N.;Benabbou,F.Bidirectionalgatedrecurrentunitforimprovingclassificationincreditcardfrauddetection.
Indones.J.Electr.Eng.Comput.Sci.2021,21,1704–1712.[CrossRef]
83. Ba, H. Improving detection of credit card fraudulent transactions using generative adversarial networks. arXiv
2019,arXiv:1907.03355.[CrossRef]
84. Fiore,U.;DeSantis,A.;Perla,F.;Zanetti,P.;Palmieri,F.Usinggenerativeadversarialnetworksforimprovingclassification
effectivenessincreditcardfrauddetection.Inf.Sci.2019,479,448–455.[CrossRef]
85. Dzakiyullah,N.R.;Pramuntadi,A.;Fauziyyah,A.K.Semi-supervisedclassificationoncreditcardfrauddetectionusingautoen-
coders.J.Appl.DataSci.2021,2,1–7.[CrossRef]
86. Pratap,B.G.;Vijayaraghavulu,P.Ahybridmethodforcreditcardfrauddetectionusingmachinelearningalgorithm. Int. J.
Comput.Electr.Adv.Commun.Eng.2021,10,46–50.
87. Husejinovic,A.CreditcardfrauddetectionusingnaiveBayesianandc4.5decisiontreeclassifiers.Period.Eng.Nat.Sci.2020,4,
1–5.[CrossRef]
88. Lin,T.H.;Jiang,J.R.Creditcardfrauddetectionwithautoencoderandprobabilisticrandomforest. Mathematics2021,9,2683.
[CrossRef]
89. Karthik,R.;Navinkumar,R.;Rammkumar,U.;Mothilal,K.C.Supervisedmachinelearningalgorithmsforcreditcardfraudulent
transactiondetection.Int.J.Sci.Res.Comput.Sci.Eng.Inf.Technol.2019,2019,2456–3307.
90. Esenogho, E.; Mienye, I.D.; Swart, T.G.; Aruleba, K.; Obaido, G. A neural network ensemble with feature engineering for
improvedcreditcardfrauddetection.IEEEAccess2022,10,16400–16407.[CrossRef]
91. Baker,M.R.;Mahmood,Z.N.;Shaker,E.H.Ensemblelearningwithsupervisedmachinelearningmodelstopredictcreditcard
fraudtransactions.Rev.Intell.Artif.2022,36,509–518.[CrossRef]
92. Fanai,H.;Abbasimehr,H.Anovelcombinedapproachbasedondeepautoencoderanddeepclassifiersforcreditcardfraud
detection.ExpertSyst.Appl.2023,217,119562.[CrossRef]
93. MachineLearningGroup—ULB.CreditCardFraudDetection(Dataset);Kaggle:SanFrancisco,CA,USA, 2013.
94. Hofmann,H.Statlog(GermanCreditData);UCIMachineLearningRepository:Berkeley,CA,USA,1994.

Appl.Sci.2025,15,11787 31of32
95. Lee,H.;Choi,E.;Kim,I.;Choi,D.;Go,W.;Lee,K.;Yim,H.;Lee,T.Featureselectionpracticeforunsupervisedlearningofcredit
cardfrauddetection.J.Theor.Appl.Inf.Technol.2018,96,408–417.
96. Pumsirirat,A.;Yan,L.Creditcardfrauddetectionusingdeeplearningbasedonauto-encoderandrestrictedBoltzmannmachine.
Int.J.Adv.Comput.Sci.Appl.2018,9,18–25.[CrossRef]
97. Quinlan,R.Statlog(AustralianCreditApproval);UCIMachineLearningRepository:Berkeley,CA,USA,1997.
98. Seera,M.;Lim,C.P.;Kumar,A.;Dhamotharan,L.;Tan,K.H.Anintelligentpaymentcardfrauddetectionsystem.Ann.Oper.Res.
2021,334,445–467.[CrossRef]
99. Yeh,I.C.DefaultofCreditCardClients;UCIMachineLearningRepository:Berkeley,CA,USA,2016.
100. ChinaStockMarket&AccountingResearch(CSMAR);WhartonUniversityofPennsylvania:Philadelphia,PA,USA,2022.
101. Achakzai,M.A.K.;Juan,P.Usingmachinelearningmeta-classifierstodetectfinancialfrauds.Financ.Res.Lett.2022,48,102915.
[CrossRef]
102. Shou,M.;Bao,X.;Yu,J.Anoptimalweightedmachinelearningmodelfordetectingfinancialfraud.Appl.Econ.Lett.2023,30,
410–415.[CrossRef]
103. Compustat.S&PGlobalMarketIntelligence;Compustat:Centennial,CO,USA,2022.
104. Whiting,D.G.;Hansen,J.V.;McDonald,J.B.;Albrecht,C.;Albrecht,W.S.Machinelearningmethodsfordetectingpatternsof
managementfraud.Comput.Intell.2012,28,505–527.[CrossRef]
105. López-Rojas,E.SyntheticFinancialDatasetsforFraudDetection;Kaggle:SanFrancisco,CA,USA,2017.
106. Alwadain,A.;Ali,R.F.;Muneer,A.Estimatingfinancialfraudthroughtransaction-levelfeaturesandmachinelearning.Mathemat-
ics2023,11,1184.[CrossRef]
107. Hwang,J.;Kim,K.Anefficientdomain-adaptationmethodusingGANforfrauddetection.Int.J.Adv.Comput.Sci.Appl.2020,
11,94–103.[CrossRef]
108. Moreira,M.Â.L.;deSouzaRochaJunior,C.;deLimaSilva,D.F.;deCastroJunior,M.A.P.;deAraújoCosta,I.P.;Gomes,C.F.S.;
dosSantos,M.Exploratoryanalysisandimplementationofmachinelearningtechniquesforpredictiveassessmentoffraudin
bankingsystems.ProcediaComput.Sci.2022,214,117–124.[CrossRef]
109. Putten,P.InsuranceCompanyBenchmark(COIL2000);UCIMachineLearningRepository:Berkeley,CA,USA,2000.
110. Huang,D.;Mu,D.;Yang,L.;Cai,X.CoDetect:Financialfrauddetectionwithanomalyfeaturedetection. IEEEAccess2018,6,
19161–19174.[CrossRef]
111. Omershafiq.BitcoinNetworkTransactionalMetadata;Kaggle:SanFrancisco,CA,USA,2019.
112. Ashfaq,T.;Khalid,R.;Yahaya,A.;Aslam,S.;Alsafari,S.;Hameed,I.Amachinelearningandblockchainbasesefficientfraud
detectionmechanism.Sensors2022,22,7162.[CrossRef]
113. Almhaithawi,D.;Jafar,A.;Aljnidi,M.Example-dependentcost-sensitivecreditcardsfrauddetectionusingSMOTEandBayes
minimumrisk.SNAppl.Sci.2020,2,1–12.
114. Ramírez-Alpízar,A.;Jenkins,M.;Martínez,A.;Quesada-López,C.Useofdataminingandmachinelearningtechniquesforfraud
detectioninfinancialstatements:Asystematicmappingstudy.Rev.Iber.Sist.Tecnol.Inform.2020,2020,97–109.
115. Bakumenko,A.;Elragal,A.Detectinganomaliesinfinancialdatausingmachinelearningalgorithms. Systems2022,10,130.
[CrossRef]
116. Zhao,Z.;Bai,T.FinancialfrauddetectionandpredictioninlistedcompaniesusingSMOTEandmachinelearningalgorithms.
Entropy2022,24,1157.[CrossRef][PubMed]
117. Shahana,T.;Lavanya,V.;Bhat,A.R.Stateoftheartinfinancialstatementfrauddetection:Asystematicreview.Technol.Forecast.
Soc.Change2023,192,122527.[CrossRef]
118. Viera,J.;Aguilar,J.;Rodríguez-Moreno,M.;Quintero-Gull,C.Analysisofthebehaviorpatternofenergyconsumptionthrough
onlineclusteringtechniques.Energies2023,16,1649.[CrossRef]
119. Nicholls,J.;Kuppa,A.;Le-Khac,N.A.Financialcybercrime:Acomprehensivesurveyofdeeplearningapproachestotacklethe
evolvingfinancialcrimelandscape.IEEEAccess2021,9,163965–163986.[CrossRef]
120. Andrade-Arenas,L.;Yactayo-Arias,C.Comparativeanalysisofmachinelearningmodelsforcreditcardfrauddetectionusing
SMOTEforclassimbalance.Int.J.Saf.Secur.Eng.2025,15,893–901.[CrossRef]
121. Saito,T.;Rehmsmeier,M.Theprecision–recallplotismoreinformativethantheROCplotwhenevaluatingbinaryclassifierson
imbalanceddatasets.PLoSONE2015,10,e0118432.[CrossRef]
122. DalPozzolo,A.;Caelen,O.;Johnson,R.A.;Bontempi,G.Calibratingprobabilitywithundersamplingforunbalancedclassification.
In Proceedings of the 2015 IEEE Symposium Series on Computational Intelligence (SSCI), Cape Town, South Africa, 7–10
December2015.
123. Lucas,Y.;Portier,P.E.;Laporte,L.;He-Guelton,L.;Caelen,O.;Granitzer,M.;Calabretto,S.Towardsautomatedfeatureengineering
forcreditcardfrauddetectionusingmulti-perspectiveHMMs.FutureGener.Comput.Syst. 2020,102,393–402.[CrossRef]

Appl.Sci.2025,15,11787 32of32
124. Li,W.;Zhao,R.;Wang,X.Fromsimpletocomplexscenes:Learningrobustfeaturerepresentationsforaccuratehumanparsing.
InProceedingsoftheIEEEConferenceonComputerVisionandPatternRecognition2015,Boston,MA,USA,7–12June2015;
pp.26–34.
125. Wang,C.;Zhang,J.;Gao,Z.;Wang,Z.;Liu,N.Light-fieldimagemultiplereversiblerobustwatermarkingagainstgeometric
attacks.IEEEAccess2018,6,41193–41207.[CrossRef]
126. Salam, M.A.; Fouad, K.M.; Elbably, D.L.; Elsayed, S.M.Federatedlearningmodelforcreditcardfrauddetectionwithdata
balancingtechniques.NeuralComput.Appl.2024,36,6231–6256.[CrossRef]
127. Cheng,D.;Wang,X.;Zhang,Y.;Zhang,L.Graphneuralnetworkforfrauddetectionviaspatial-temporalattention.IEEETrans.
Knowl.DataEng.2020,34,3800–3813.[CrossRef]
128. Chullamonthon,P.;Tangamchit,P.Ensembleofsupervisedandunsuperviseddeepneuralnetworksforstockpricemanipulation
detection.ExpertSyst.Appl.2023,220,119698.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.