| Exploring |                              | Machine        | Learning     | for Credit     | Card                            | Fraud Detection |     |
| --------- | ---------------------------- | -------------- | ------------ | -------------- | ------------------------------- | --------------- | --- |
|           |                              | from           | a Philippine | Perspective    |                                 |                 |     |
|           |                              | EricBlancaflor |              |                | KeziahDawnAsuncion              |                 |     |
|           | SchoolofIT,MapuaUniversity   |                |              |                | SchoolofIT,MapuaUniversity      |                 |     |
|           |                              | Philippines    |              |                | Philippines                     |                 |     |
|           | ebblancaflor@mapua.edu.ph    |                |              |                | kdrasuncion@mymail.mapua.edu.ph |                 |     |
|           | HailieJadeReyes              |                |              |                | MichaelaVerzosa                 |                 |     |
|           | SchoolofIT,MapuaUniversity   |                |              |                | SchoolofIT,MapuaUniversity      |                 |     |
|           |                              | Philippines    |              |                | Philippines                     |                 |     |
|           | hjsreyes@mymail.mapua.edu.ph |                |              |                | mpverzosa@mymail.mapua.edu.ph   |                 |     |
| Abstract  |                              |                |              | 1 Introduction |                                 |                 |     |
Thisstudyexamineshowmachinelearning(ML)techniquesare 1.1 BackgroundoftheStudy
appliedinthePhilippinesettingtoidentifycreditcardfraud.This
Paralleltothephenomenalgrowthofdigitaltransactionsandon-
researchaimstoprovideinsightsintotheeffectivenessofMLtech- linecommerce,creditcardfraudinthePhilippineshasrisento
niquesinfrauddetection,focusingoncustomizingMLalgorithms
|     |     |     |     | incredibleheights. | Togetherwithincreasinglysophisticatedforms |     |     |
| --- | --- | --- | --- | ------------------ | ------------------------------------------ | --- | --- |
tothedistinctpatternsanddynamicsofcreditcardfraudinthe
|     |     |     |     | of fraudulent | activities come | growing requirements | for equally |
| --- | --- | --- | --- | ------------- | --------------- | -------------------- | ----------- |
Philippines,consideringthenation’suniqueeconomic,technologi-
innovativesolutionsthatcancutthesecrimesdown.Inlinewith
cal,andsocialmilieu.Theresearchassessestheefficacyofdifferent
this,thisresearchwillinvestigatewhethermachinelearningcould
machinelearning(ML)modelsusingavailabledataoncreditcard beapowerfultoolinenhancingcreditcardfrauddetectionwithin
fraudoccurrencesandsuggestsimprovingfrauddetectionsystems
thePhilippinefinancialsector.Itisanartificialintelligencedomain
inPhilippinefinancialinstitutionsthroughMLintegration.Italso
thatimpartedcomputerswiththeabilitytolearnfromdatawith-
| examines | the opportunities | and difficulties | of using ML-driven |     |     |     |     |
| -------- | ----------------- | ---------------- | ------------------ | --- | --- | --- | --- |
outexplicitprogramming,henceagoodsolutionforidentifying
frauddetectiontechniquesinthePhilippinefinancialindustry.
fraudulentpatternsandanomaliesincreditcardtransactions.Fo-
cusingoncustomizingtheMLalgorithmsforthepeculiaritiesof
CCSConcepts
thePhilippinecontext—economic,technological,andsocial—this
•Securityandprivacy;•Humanandsocietalaspectsofsecu- paper,researchwilltrytoenhancetheeffectivenessoffraudde-
|     |     |     |     | tectionsystems. | Theliteraturereviewwillgointothebackground |     |     |
| --- | --- | --- | --- | --------------- | ------------------------------------------ | --- | --- |
rityandprivacy;•Privacyprotections;
ofcreditcardfraudinthismoderndigitalworld,thescopeand
purposeoftheresearch,themethodology,keyfindingsanddis-
Keywords
cussions,andfinally,implicationsandfutureresearchdirections.
CreditCard,FraudDetection,MachineLearning,Philippines,Sup- Creditcardfraudinstancesareincreasingatarapidrateinthe
portVectorMachines,ArtificialNeuralNetwork,Prevention,De- Philippines,whichgoesindirectrelationtotherapidgrowthof
tection itsdigitaleconomy[1]. Thisthreatincreaseswiththelimitedef-
fectivenessoftraditionalfrauddetection.Hereinliestherelevance
ACMReferenceFormat: ofthisreview. ByprovidingwaytothepossibilitiesofMLforthe
EricBlancaflor,KeziahDawnAsuncion,HailieJadeReyes,andMichaela Philippinesetting,thisstudyhopestoaddtotheexistingdiscussion
Verzosa.2024.ExploringMachineLearningforCreditCardFraudDetection regardingthestrengtheningoffinancialinstitutionsfromfraudin
fromaPhilippinePerspective.In2024The6thWorldSymposiumonSoftware developingeconomies. Furthermore,lessonslearnedintailingML
Engineering(WSSE)(WSSE2024),September13–15,2024,Kyoto,Japan.ACM, modelsforthedistinctlyPhilippineenvironmentwillalsoserve
NewYork,NY,USA,6pages.https://doi.org/10.1145/3698062.3698088 otherdevelopingcountriesthatfacesimilarchallenges.
|     |     |     |     | 1.2 ObjectiveoftheStudy |     |     |     |
| --- | --- | --- | --- | ----------------------- | --- | --- | --- |
Thispaperidentifiestheescalatingthreatofcreditcardfraudin
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
thePhilippinesandexploresitsparallelismwiththeproliferation
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation ofcomputer-basedtransactionsinthecountryandsimultaneously
onthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthanthe with the inadequacy of traditional fraud detection methods. It
author(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,or pointsoutthemainresearchquestionofwhetheritwouldbepos-
republish,topostonserversortoredistributetolists,requirespriorspecificpermission
and/orafee.Requestpermissionsfrompermissions@acm.org. sibletofine-tunemachinelearningalgorithmstothePhilippine
WSSE2024,September13–15,2024,Kyoto,Japan
contextformoreeffectivefrauddetection.Thissectionreviewsthe
©2024Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
backgroundofthestudyoncreditcardfraud,itsscopeandpurpose,
ACMISBN979-8-4007-1708-6/24/09
https://doi.org/10.1145/3698062.3698088 methodologyused,findings,anddiscussions. Thepaperseeksto
177

WSSE2024,September13–15,2024,Kyoto,Japan EricBlancafloretal.
prepareabettergroundforanall-roundedargumentaboutML’s [6].FormerRCBCbranchmanagerMaiaDeguitowasinJanuary
potentialinfightingcreditcardfraudinthePhilippinefinancial 2019convictedoneightcountsofmoneylaunderinginthe$81
sector. milliontheftfromtheCentralBankofBangladesh. Thebankwas
finedPHP1billion($19.17million)inAugust2016foritsfailureto
2 LITERATUREREVIEW preventtheflowofstolenfundsthroughit[6].
MariaNite,presidentofBankCapitalDevelopmentCorp.,was
Withthesuddensurgeofdigitalpaymentplatforms,fraudulent
behindanotoriousTreasurybillscaminwhichshebilkedbanks
creditcardtransactionsinthePhilippineshaverisenby21%since
andinvestorsbysellingtheTreasurybillsrepeatedlytotrickpeople
the outbreak of COVID-19. Many of the fraud prevention sys-
intobelievingtheywereallofthesameT-bill.Shemadeoffwith
temsdonotconsiderthesecurityofe-commercenetworksandthe
P2.5billion($200million)andwasarrestedbyFBIagentsin1997,
frauddetectionsystemsfaceissueslikeenormousquantitiesofdata,
andextraditedtothePhilippines[6]. TheFrancSwiss&Deutsch-
skeweddistribution,conceptdrift,andreal-timedetectionassis-
ersscambroughtlossesofPHP1billion,whilethatofthe12DP
tance.Althoughatthecostofexplainability,theaccuracyachieved
scamwas$500million.Legacyinsuranceandpensionscamcaused
byMachinelearningmodels, empoweredwithsuperiorpattern
lossesofPHP30billion, or$591million. AmanFuturesGroup
detectionandscalability,makethemthefutureofFrauddetection.
connedmorethan15,000investorsinMindanaoandVisayasintoa
Futureresearchshallinvestigatetheimpactsofadditionalsample
pyramidschemewhereaninvestmentreturnof80%injust20days
techniquesmeta-classifiersandmeta-learningmethodologiesto
waspromisedforcommoditiestrading.ConnectedtoLegalFunds
dealwithhighlyimbalancedcreditcardfrauddata.
TransferwasthecaseofAnnabellaC.Ylagan,convictedinApril
2018of55countsofmoneylaundering[6].
2.1 FraudIssuesonCreditCardUsage
Between2020and2021,cardfraudlossesgloballyincreasedby
AccordingtoPhilstar[2],MANILA,Philippines—Fraudulentcredit more than 10 percent. This is the highest rise since 2018. It is
cardoperationsinthePhilippinesthroughremoteandotherdigital estimatedthat30billiondollarswerelostbymerchantsandcard
paymentchannelsincreasedby21%sincethestartofthepandemic, acquirers;ofthose,lossesofabout12billionwerefrommerchants
accordingtotheCreditCardAssociationofthePhilippines.”The andcardacquirersintheUnitedStatesalone,asreported.Please
industryhassufferedfinanciallyduetoanincreaseinfraudcases notethatthefiguresshownhereincludebothcreditcardfraud
broughtonbytheincreasingacceptanceofdifferentdigitalpay- anddebitcardfraud. Theyarenotdistinguishedonthewebsite,
mentplatforms,”Ilaganstated.AccordingtoABS-CBNNews[3], andneitheristhereanystatisticontheUS,whichisyetanother
TheBangkoSentralngPilipinassaidonMondaythatonlinefraud countryknownforitsaddictiontocreditcards[7].
costconsumersmorethanP540millionin2021alone. Italsoap- From$28.4billionin2020and$27.9billionin2018,atotalof$33.5
pealedtolawmakerstopassabillthatprotectsfinancialcustomers. billionwasreportedlostduetocardtheftgloballyin2022.Inthe
BSPsaidtherewere42,456complaintsfromfraudvictimsofonline EU,cardtransactionsof€1.53billionwerereportedasfraudulent
monetarytransactionsbetween2020and2021involvingphishing, in2021,representinga7%declineinfraudulentcardtransactions
identitytheft,andmalwareattacks,amongotherformsofdeceit. overall. 93%offraudulentchargesin2024includedcreditcards
Mostofthesehavealreadybeenconsideredclosed. Inaddition, issuedintheUnitedStatesthatwerestillintheowners’possession.
Dioknoenlightenedthesenatorsthatalotofcomplaintshadreso- Card-not-presentisthefraudtypeaffecting$174millioninlost
lutionsthatdidnotbenefittheconsumer. Tothisextent,doubtless, revenuein2023. In2023,customersdidreport368,379casesof
theincreaseindigitaltransactionshasmadeconsumers’liveseasier fraudrelatedtoonlinepurchasingforacostof$392million.94%of
andfaster,butthistrendhasalsoopeneduproomfornewtypesof allcard-presenttransactionsgloballyweremadeusingcardswith
financialfraud.AccordingtotheCCAP,therehasbeenaphenome- EMVchipsasofthesecondquarterof2023,comparedto92%at
nalsurgeinfraud-relatedactivities,inparticularthroughdigital thesametimein2022[8].
andremotepaymentchannels[4].Apartfrombeingathreattothe Despitesuchefforts,theseareprimafaciereasonstobelievethat
consumers,theriseofthesefraudulentcasesiscostingthesector moreneedstobedonetoeducateandcreateawarenessamong
financially. customersconcerningthedangersassociatedwiththeuseofe-
Respondingtothisescalatingthreat,theBSPhasstartedtoad- financialservices.Severalresolvedcaseswithoutvictimsreceiving
dressalloftheseconcerns.WithdamagesestimatedatP540million adequatecompensationisapointertotheneedformoreeffective
lastyear,cybercrimehighlightsthenecessityofbetterpoliciesfor enforcementandconsumereducationcampaigns.Itputscustomers
securing clients [3]. The law was legislated in response to the onnoticetobevigilantandatalltimeskeepconstantcheckson
BSP’sappealtoCongresstopassthistypeoflaw[5].Itprovides theiraccountsandreportsuspiciousactivitiestotheirbanksor
fortherightsoffinancialconsumersforfairtreatmentandtimely appropriateauthorities.Tohavethecapacityforasafeandreliable
settlementoftheircomplaints. digitalecosystem,thecollaborationofallconcernedstakeholders—
ItiscurrentlyinvestigatingclaimsofcustomersofPhilippine fromfinancialinstitutionstoregulatorsandconsumers—shouldbe
bankBDOthattheylostmoneytointernetscammerswhoused assurance-basedoncedigitalfinancemakesitswaytothecountry.
accountsatUnionBankofthePhilippines.Itreportedhavingmon- Otherthanindividualcustomerprotection,acollaborativefight
itoredtheincreasedcomplaintsinthepastweekandsubsequently againstfraudwouldfurthercementtheintegrityofthePhilippine
frozen several accounts. The Philippines Anti-Money Launder- financialsystem.
ingCouncilannouncedthatthecountryhadsteppedupitsfight
againstmoneylaunderingandterrorfinancinginNovember2021
178

ExploringMachineLearningforCreditCardFraudDetectionfromaPhilippinePerspective WSSE2024,September13–15,2024,Kyoto,Japan
2.2 FraudDetectionStudiesonMachine machinelearning-drivenfocusshiftfrompre-transactiontopost-
Learning transactiondetectionportrayssuccessinthiswaragainstfraud
andcreatesamuchsaferdigitaltransactionenvironment[15]. In
Fraudstersfrequentlytargete-commercesystemsandusearange
thisexperiment,thethreemethodswillbeappliedtobothprepro-
ofunderhandedtacticstogetthrough. UsingFraudPrevention
cessedandrawdata.Theimplementationoftheworkwillbedone
Systemsaloneisnotsufficientforsecuringthenetwork.Twopos-
inPython. Theirperformancewillthenbeevaluatedusingthe
siblecombinationsofFPSsandFDSsaresharingtheircapacitiesin
approachesbasedontheiraccuracy,sensitivity,specificity,preci-
securinge-commercesystems.However,thefollowingfactorsusu-
sion,MatthewsCorrelationCoefficient,andbalancedclassification
allymakeFDSsweak.Someoftheseareconceptdrift,theneedfor
rate.Descriptivestatisticsofmodelsappliedforlogisticregression
real-timedetection,andimbalanceddistribution,coupledwithhan-
andk-nearestneighborclassifiershavetheirbestaccuracyrates
dlingvastvolumesofdata.Furthermore,threespecificlimitations
at54.86%and97.69%, respectively, whilethatofnaïveBayesis
preventFDSsfrombecominghighlyefficient: theproblemsasso-
at97.92%.ComparativeresultsshowthattheK-nearestneighbor
ciatedwiththemisclassificationcosts,noisydata,andoverlapped
outperformsthelogisticregressionandnaïveBayesmethods.The
classes.Theseconstraintsdrivethemodelsconstructedimproperly
researchgivestheeffectofhybridsamplingonthebinaryclassi-
andtobecometoocomplicateddetectionmodels-affectingthepre-
ficationofimbalanceddata. Expectedfutureareasofstudieson
dictedaccuracyadversely.Toaddresstheseproblems,thefollowing
meta-classifiersandmeta-learningstrategiesforthehandlingof
frauddetectiontoolsaremorecommonlyreliedon.Thesetoolsare
highlyimbalancedcreditcardfrauddataand,theeffectsofother
logisticregression,rule-inductiontechniques,decisiontrees,artifi-
re-samplingtechniquescouldalsobeexplored[16].
cialneuralnetworks,supportvectormachines,andmeta-heuristic
suchasevolutionaryalgorithms. AccordingtoAbdallahetal. in
2016,theinstrumentsareappliedtomostofthefrauddetection 2.3 FocusonFraudPreventionandDetection
industries[9].Techniquesprovideafeasiblemeanstoimprovethe
Concerningthemagnitudeoftheproblemofcreditcardfraudinthe
effectivenessoftheFDSsinsecuringe-commerceplatforms.
Philippines,thestrategicapproachhasbeenaboutstrengthening
• The matthews correlationcoefficient (mcc) is a metric to
fraudpreventionanddetectionsystems.Itisthroughacombination
assesshowwellbinaryclassificationsaredone. Itiswell
ofmultifactorauthentication,encryption,andreal-timemonitor-
recognizedasabalancedmeasurethatcanbeappliedeven
ingthatFPSsbecomebetterequippedtodetect,atanincredibly
incaseswheretheclasseshavedrasticallydifferentsizes
fastpace,anysuspiciousaction. Advancedanalytics,alongwith
because it accounts for both true and false positives and
machinelearningalgorithmslikeArtificialNeuralNetworks(ANN)
negatives1.Thisformulaisusedtocalculatethemcc:MCC
√ andSupportVectorMachines(SVM),strengthensfrauddetection
=(TP×TN)-(FP×FN)/ ((TP+FP)(TP+FN)(TN+FP)(TN
capabilitieswithinaFraudDetectionSystem(FDSs). Thesealgo-
+FN)):wheretpistruepositives,tnistruenegatives,fpis
rithms learn to recognize fraudulent patterns and anomalies in
falsepositives,andfnisfalsenegatives[10].
transactiondata. SupportVectorMachineisoneofthepopular
• Balancedclassificationrate(bcr): bcristheaverageofthe
methodsthatisusedtorecognizepatternsandclassifyproblems,
recallscoresforeachclass. Itissometimesreferredtoas
especiallywhenbinarycategorizationlikeclassifyingfraudulent
theaveragerecallorthebalancedaccuracy.Ithelpshandle
andnonfraudulentpatternsisinvolved.
datasetsthatareunbalanced3. Itcomesouttobe: BCR=
LikeallotherAItechniques,anSVMneedstobetrainedtoreturn
2Sensitivity+Specificity.Thegenuinepositiverateiscalled
amodelcapableofpredicting.Domainsofapplicationincludebut
sensitivity,andthetruenegativerateiscalledspecificity[11].
arenotlimitedtothefollowing:textcategorization,bioinformatics,
• Astatisticalmodelusedinmachinelearningforbinaryclas-
andfacedetection. SVMborrowsfromnon-parametricapplied
sification issues is called logistic regression. Logistic re-
statistics,neuralnetworks,andthebasicsofmachinelearning.Its
gressionforecastsanevent’sprobability,whichisanumber
decisionfunction,basedonthetheoryofStructuralRiskMinimiza-
between 0 and 1, as opposed to linear regression, which
tion,willdefineaboundarybetweenclassesinthecaseofbinary
predictsacontinuousoutcome[12].
classification. Thisfunctionalsoplaysaveryimportantrolein
• K-nearestneighbor: k-nnisasupervised,non-parametric
determiningtheseparationmarginbetweenclasses,whereinitis
learningclassifierthatclassifiesorpredictshowtocatego-
learnedbyparameterswandbduringthetrainingphasebymaxi-
rizeasingledatapointbasedonitsproximitytootherdata
mizingthemargin[17].HereisthesampleoftheSVMEquation:
points67.Whengivenatestobservationandapositiveinte- 𝑓(𝑥)=𝑠𝑞𝑛(𝑥.𝑤)+𝑏
gerk,k-nnfindstheknearestpointsandcanconcludethese
Toscalethesesystemsuptothenextlevel,thereisanurgent
closesttargets[13].
needtoperformperiodicupgradesofsecurityprotocolsandalgo-
• Usingthebayestheoremasitsfoundation,naïvebayesisa
rithmstostayaheadofthetacticsoffraudstersinvogueeachday
probabilisticmachinelearningtechniquethatmaybeused
[18].Bigdatatechnologycanprovidethecompetenceofthesesys-
forvariousclassificationtasks. Itisreferredtoas”naive”
temstoeffectivelydealwithvoluminousdataontransactions,thus
becauseitassumesthateachcharacteristicinthemodelis
identifyingfraudactivitieswithbetteraccuracyinreal-time. This
independentoftheothers[14].
isbecausegoodcollaborationwithinthebodiesofbanks,payment
Althoughthetradeoffbetweenexplainabilityandaccuracyexists, processors,andregulatoryauthoritiesisespeciallycrucialinshar-
withimprovedpatterndetectionandscalability,machinelearning ingvitalinformationandtrendsonfraud. Bydoingso,itbecomes
modelsremainthewayforwardforfrauddetection. Thiswaveof possibletofosteruniversallyacceptedstandardsandsolutionsthat
179

WSSE2024,September13–15,2024,Kyoto,Japan EricBlancafloretal.
thismaybeasimportantasexplainingtherationalebehindde-
cisionsasaccuracy. Therefore,inthecaseofcreditcardfraud,it
wouldbewisertorelymoreonmodelslikeANN-SMOTEtoen-
hancethepossibilitiesofdetection.However,includingLRmodels
isbeneficialinmeetingcomplianceandtransparencyrequirements.
Therefore,amiddlepathcanbeadoptedsothatthediscoverability
andpreventionoffraudaremorepotent,andatthesametime,the
developedprocessesremaincompliantwiththesetregulations.
2.5 UsingMachineLearningtoAvoidCredit
CardFraud
The case of credit card fraud detection in the Philippines stays
Figure1: ComparativePerformanceofMachineLearning timelyduetothesteepriseinfraudulenttransactionsby21%since
ModelsinCreditCardFraudDetection thepandemic[2].TraditionalFPSsdonotsufficetoprotectdigital
paymentnetworks;thus,thereisaneedformoderntechnologies
likeML.Thediscussionpointsouttheseriousnessoftheissueof
fraudandtheneedforproactiveactionsbasedoninsightsfrom
effectively mitigate any vulnerabilities across all the platforms.
reliablesources—theCreditCardAssociationofthePhilippinesand
Trainingemployeesinfinancialinstitutionsontheknowledgeof
theBangkoSentralngPilipinas.Verypromisingresultsinenhanc-
currentfrauddetectiontechnologiesandtechniqueshelpsmaintain
ingfrauddetectionskills,despiteinherentmodelexplainability–
aneffectivelevelofalertnessandcompetence.Equallyimportant
accuracytrade-offs,havebeenseenlatelywithmachinelearning
areconsumereducationprogramsthatcanboostknowledgeof
models,especiallysupportvectormachinesandartificialneural
securityproceduresandtheimportanceofprotectingpersonalin-
networks.Thediscussionneedsfurtherresearchinmorecreative
formation.Lastly,thedevelopmentofmachinelearningadaptive
methods such as meta-classifiers or meta-learning strategies to
modelsintoapplicationsableeasilytoacquireinformationonnew
solvetheproblemsarisingfromfraudulentcreditcarduseinthe
fraudulentactionsand,intheprocess,altertheiralgorithmwillin
Philippines.Italsocallsforstakeholderengagementinadvanced
thelongtermensureveryeffectivefrauddetectionsystems[19].
analyticstosetthefoundationforacollectivedefenseagainstfraud-
stersondigitalpaymentnetworks. Thediscussionisverymuch
2.4 ApproachtoAddressCreditCardFraud
inkeepingwiththeresearchaimstoinvestigatemachinelearning
Identificationofcomplexchallengesinmitigatingcreditcardfraud— increditcardfrauddetectioninthePhilippinesandprovidesvery
thatthisentailsfalsealertcasesandneedstobeinreal-time—is valuableinsightsandideasforfutureresearchinthisfield.
important.Toovercomesuchchallenges,developingandputtingin Inaddition,theimplementationofmachinelearningalgorithms
placerobustsolutionswillberelevant.Theseincludereal-timemon- intofrauddetectionsystemsincreasestheaccuracyoftheidenti-
itoringoptionsthatfacilitateimmediateidentificationofsuspicious ficationoffraudulentactions,providingreal-timedetectionwith
trendsandreactionstothesame.Furthermore,theimprovement thecapabilityofadaptivelearning[22]. Machinelearningmod-
ofrulesinfraudpreventionitselfincreasesaccuracyandmakes elsadapttonewlydevelopedfraudtechniquesbycontinuously
themeasuresmoreresponsive. Thesepreventivestepscanthen analysingtransactiondataandpatterns. Thisadaptiveabilityis
beimplementedtosafeguardthebusinessfromfraud,fortifythe quiteimportantinfightingmorecomplexfraudtechniques,given
protectionofitsfinancialassets,andupholdcustomertrust[20]. thefast-movingnatureofdigitaltransactions.Furthermore,fraud
Figure1comparestheperformanceoftwoMachineLearning preventionrequirescollaborationbetweendifferentstakeholders,
models:ArtificialNeuralNetwork(ANN)andLogisticRegression includingfinancialinstitutions,regulatoryauthorities,andtechnol-
(LR),withGeneticAlgorithm(GA)andtheSyntheticMinorityOver- ogyproviders. Onlythroughsharedinsights,bestpractices,and
samplingTechnique(SMOTE)-basedenhancementstoeachmodel collaborationcanstakeholdersbebetterplacedtoimprovefraud
[21]. Theseenhancementsareaddedtoeachmodeltomakethe preventionmeasureswithindigitalpaymentnetworksandreduce
modelmoreaccurateandrobusttoskewness—arelevantfactor vulnerabilities.Advancedanalyticsalsoshowcasesagreaterinter-
whendealingwithfrauddetection. Ithasthebestperformance estintheuseofdata-driventechniquestounearthquitehidden
comparedtoothermodelsonallaspectsofaccuracy, precision, trendsandanomaliesthatserveasleadingindicatorsoffraudu-
recall,andF1score.Thiswillmeanitcandetectfraudmoreimpres- lentactivities,andthereforesecureandpreservetheintegrityof
sivelyandwithfewmisclassifications. Thismeansthatprobably, financialtransactionsinthePhilippines.
ANN-SMOTEcouldprobablybehighlyefficient,forexample,in Theresearchershavetakenadetaileddrivethroughvariousma-
creditcardfrauddetection,whereillegaltransactionsareveryfew chinelearningmodelsinserviceforcreditcardfrauddetection.
as compared to legal ones. On the other hand, even if the LR Thissectionwillmainlyfocusonhowwellthesemodelsperform
models—bothLR-GAandLR-SMOTE—exhibitrelativelypoorper- intermsofaccuracy—oneofthemajorfactorsindetermininghow
formanceconsideringthesemetrics,theycanturnouttobeuseful efficienteachmodelisatthedetectionoffraudulenttransactions.
inapplicationsforwhichtheinterpretabilityofthedecisionsmade Further,somestrategicideasthatareaimedatenhancingthefore-
byamodelisparamount. Inparticular,inregulatorycompliance, castaccuracyandtotalefficiencyofsuchmodelsaresought. The
180

ExploringMachineLearningforCreditCardFraudDetectionfromaPhilippinePerspective WSSE2024,September13–15,2024,Kyoto,Japan
Table1:EvaluatingMachineLearningModelsforCreditCardFraudDetection:AccuracyandImprovementStrategies
Model DatasetDescription Method Accuracy WhattoImprove Reference
Logistic Creditcardtransactiondata Supervisedbinary 54.86% Explorehybridsamplingto [23]
Regression fromthePhilippines classification handleimbalanceddata
K-Nearest Datapointsclusteredbased Non-parametric, 97.69% Increasethediversityand [24]
Neighbors onproximitytodetectfraud nearestneighbor sizeofthedatasetforbetter
(k-NN) generalization
NaïveBayes Transactionpatternsfocusing Probabilistic 97.92% Adjustindependence [25]
onanomalydetection classification assumptionsinthemodel
SupportVector Featuresintendedto Kernel-based Variesupto Incorporatemeta-learning [26]
Machines(SVM) distinguishbetweenauthentic learningtechnique 80% forskeweddatahandling
andfraudulenttransactions
ArtificialNeural High-dimensionaldatasetsfor Deeplearning Variesupto Optimizeneuralnetwork [27]
Networks(ANN) patternrecognition algorithms 98.44% architectureforreal-time
detection
authorshaveclearlyshownthat,forinstance,someoftheirmodels detectionsystems.Resultsfromthisstudymayhelprelatedissues
addressimbalanceddatasetsorimprovingalgorithmparameters dealingwithotherdevelopingcountries.
asthecriticalareastoenhance, andthereforethisgivesaclear
avenueforfutureresearchonitspracticalapplicationinfraudde- References
tection. Thisthoroughassessmentimprovesourunderstandingof [1] KrisCrismundo.2021.DigitalfraudattemptsinPHriseamidpandemic|Philip-
thecurrentcapabilitiesandlimitationsofexistingmachinelearning pineNews.PhilippineNewsAgency.Retrievedfromhttps://www.pna.gov.ph/
articles/1134735
modelsandfurtherdrivesinnovationinmethodstosecurefinancial [2] LawrenceAgcaoili.2022.Creditcardissuersreport21%jumpinfraudcases|
securitysystemsagainstthethreatsoffraudulentactivities. Philstar.com.Philstar.Retrievedfromhttps://www.philstar.com/business/2022/
08/17/2203090/credit-card-issuers-report-21-jump-fraud-cases
[3] SherrieAnnTorres.2022.BSPsaysonlinefraudcostP540millionin2021|ABS-
3 CONCLUSION
CBNNews.Retrievedfromhttps://news.abs-cbn.com/business/01/17/22/bsp-says-
online-fraud-cost-p540-million-in-2021
Inconclusion,thedigitalpaymentsystemsthathavebeeninvented
[4] Doris Dumlao-Abadilla, D. 2021. Credit card fraud cases surge 29%. IN-
haveprovedtobeapotentialsourceofunintendedconsequences QUIRER.net.Retrievedfromhttps://business.inquirer.net/316906/credit-card-
forincreasedfraudulentactivities, especiallyinthePhilippines, fraud-cases-surge-29
[5] RepublicActNo.11765.2022.Lawphil.net.Retrievedfromhttps://lawphil.net/
which,sincetheepidemic,hasseenanincreaseincreditcardfraud
statutes/repacts/ra2022/ra_11765_2022.html
by21%.CurrentFPSSareprovingtobeutterlyinadequateintheir [6] JayHilton.2021.Philippines: Shortlistoftopfinancialscams,centralbank
securityfore-commercenetworks,whilevariouschallenges,such cracksthewhiponfraud,moneylaundering.gulfnews.com.Retrievedfromhttps:
//gulfnews.com/business/philippines-short-list-of-top-financial-scams-central-
asmanaginghugeamountsofdata,skeweddistribution,concept bank-cracks-the-whip-on-fraud-money-laundering-1.1639325591494?slide$=$1
drift,andthedemandforreal-timedetection,plagueFDSS.How- [7] RaynordeBest.2024.Cardfraudvalueworldwide.Statista.Retrievedfrom
https://www.statista.com/statistics/1394119/global-card-fraud-losses/.
ever,theintroductionofmachinelearningmodelsputsthefuture
[8] MariaWebb.2024.Creditcardfraudstatistics.Techopedia.Retrievedfromhttps:
offrauddetectiononthebrightside. Theapplicationofmodels //www.techopedia.com/credit-card-fraud-statistics.
thatcanlearnfromdatawithoutexplicitprogrammingforimprov- [9] AishaAbdallah,MohdAizainiMaarof,andAnazidaZainal.2016.Frauddetection
system:Asurvey|JournalofNetworkandComputerApplications,68,90–113.
ingsecurityine-commerceplatformsisincreasinglyused.Inthis
Retrievedfromhttps://doi.org/10.1016/j.jnca.2016.04.007
way,anadvancedwaragainstfraudformsasaferenvironmentfor [10] Li Sisters. 2024. Matthew’s correlation coefficient: When to use
digitaltransactionswithatransitionfrompre-transactiontopost- it and when to avoid it. Medium. Retrieved May 8, 2024, from
https://towardsdatascience.com/matthews-correlation-coefficient-when-
transactiondetection. Thisstudy,therefore,ismuchneededinthe to-use-it-and-when-to-avoid-it-310b3c923f7e.
Philippines,whichisclassifiedasoneofthecountrieswithalarge [11] ZachBobbitt.2021.Whatisbalancedaccuracy?(Definition&Example).Statology.
RetrievedMay8,2024,fromhttps://www.statology.org/balanced-accuracy.
volumeoffraudulentcreditcardtransactions.Inessence,whatthis
[12] IBM.Whatissupplychainmanagement?Retrievedfromhttps://www.ibm.com/
meansisthatthereshouldbeanenhancedFDSSwithadvanced topics/logistic-regression.
analytics,machinelearningalgorithms,andtechniquesforanomaly [13] IBM.Whatisthek-nearestneighborsalgorithm?Retrievedfromhttps://www.
ibm.com/topics/knn.
detectionwhilestrengtheningtheFPSSbymultifactorauthentica-
[14] Selva Prabhakaran. 2018. How naive bayes algorithm works? (with ex-
tion,encryptionprotocols,andreal-timemonitoring.Thiswould ample and full code). Machine Learning Plus. Retrieved May 8, 2024,
involvecollaborationconcerninginsight,bestpractices,andthreat fromhttps://www.machinelearningplus.com/predictive-modeling/how-naive-
bayes-algorithm-works-with-example-and-full-code.
informationsharingamongfinancialinstitutions,regulatorybod- [15] DorBank.2023.Thegame-changingroleofmachinelearningincreditcard
ies,andtechnologyproviders.Theresearchgoesfurthertooutline frauddetection|Justt.Retrievedfromhttps://justt.ai/blog/tech/machine-learning-
credit-card-fraud-detection
howmachinelearningwillbenefitfrauddetectioninthefinancial
[16] 6JohnO.Awoyemi,AdebayoO.Adetunmbi,andSamuelA.Oluwadare.2017.
sector. Tailoringmachinelearningalgorithmstotheintricaciesof Creditcardfrauddetectionusingmachinelearningtechniques:Acomparative
thePhilippinecontext—theuniqueeconomic,technological,and analysis.InProceedingsofthe2017InternationalConferenceonComputing
NetworkingandInformatics(ICCNI),1–9.Retrievedfromhttps://doi.org/10.1109/
socialaspects—iswhatcangreatlyincreasetheefficacyoffraud
iccni.2017.8123782.
181

WSSE2024,September13–15,2024,Kyoto,Japan EricBlancafloretal.
[17] V.DheepaandR.Dhanapal2012.Behaviorbasedcreditcardfrauddetection //orientreview.com/index.php/etmibd-journal/article/view/46/50
usingsupportvectormachines.ICTACTJournalonSoftComputing,2(4),391–397. [23] JohnO.Awoyemi,AdebayoO.Adetunmbi,andSamuelA.Oluwadare.2017.Credit
Retrievedfromhttps://doi.org/10.21917/ijsc.2012.0061. cardfrauddetectionusingmachinelearningtechniques:Acomparativeanaly-
[18] PhilipOlaseniShoetan,AdedoyinTolulopeOyewole,ChinweChinazoOkoye, sis.2017InternationalConferenceonComputingNetworkingandInformatics
andOnyekaChrisanctusOfodile.2024.Reviewingtheroleofbigdataanalyticsin (ICCNI),pp.1–9.Retrievedfromhttps://doi.org/10.1109/iccni.2017.8123782.
financialfrauddetection.Finance&AccountingResearchJournal,6(3),384–394. [24] KavitaArora,SonalPathak,andNguyenT.D.Linh.2023.Comparativeanalysis
Retrievedfromhttps://doi.org/10.51594/farj.v6i3.899 ofK-NN,NaïveBayes,andlogisticregressionforcreditcardfrauddetection.
[19] WaleedHilal,S.AndrewGadsden,JohnYawney.2021.Areviewofanomaly IngenieríaSolidaria,19(3),1–22.Retrievedfromhttps://doi.org/10.16925/2357-
detectiontechniquesandapplicationsinfinancialfraud.ExpertSystemswith 6014.2023.03.05.
Applications,193(1),116429.Retrievedfromhttps://doi.org/10.1016/j.eswa.2021. [25] T.Vairam,S.Sarathambekai,S.Bhavadharani,A.K.Dharshini,N.N.Sri,and
116429 TarikaSen.2022.Evaluationofnaïvebayesandvotingclassifieralgorithmfor
[20] KayodeAyorinde.2021.Amethodologyfordetectingcreditcardfraud.Cor- creditcardfrauddetection.20228thInternationalConferenceonAdvanced
nerstone: A Collection of Scholarly and Creative Works for Minnesota. ComputingandCommunicationSystems(ICACCS).Retrievedfromhttps://doi.
Retrievedfromhttps://cornerstone.lib.mnsu.edu/cgi/viewcontent.cgi?article$= org/10.1109/icaccs54159.2022.9784968.
$2167&context$=$etds. [26] NanaKwameGyamfiandJamal-DeenAbdulai.2018.Bankfrauddetectionusing
[21] ShailendraAswale,NikitaShirodkar,RohitShetMandrekar,RahulSakhalkar, supportvectormachine.Retrievedfromhttps://doi.org/10.1109/iemcon.2018.
andK.M.ChamanKumar.2020.Creditcardfrauddetectiontechniques.Retrieved 8614994.
May04,2024,fromhttps://www.researchgate.net/publication/351686482_Credit_ [27] F.Yeşilyurt,H.Temurtaş,andÇ.Bakır.2023.Detectionofcreditcardfraud
Card_Fraud_Detection_Techniques/citations withartificialneuralnetworks.ProceedingsoftheInternationalConferenceon
[22] AshishKSaxenaandAidarVafin.2019.Machinelearningandbigdataanalytics AdvancedTechnologies.Retrievedfromhttps://doi.org/10.58190/icat.2023.15.
forfrauddetectionsystemsintheUnitedStatesfintechindustry.Emerging .
TrendsinMachineIntelligenceandBigData,11(12),1–11.Retrievedfromhttps:
182