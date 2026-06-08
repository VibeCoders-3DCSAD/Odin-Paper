Received:7May2025|Revised:22July2025|Accepted:11August2025|Publishedonline:1September2025
FinTechandSustainableInnovation
| RESEARCH | ARTICLE |     |     |     |     |     |     | 2025,Vol.00(00)1–9 |     |
| -------- | ------- | --- | --- | --- | --- | --- | --- | ------------------ | --- |
DOI:10.47852/bonviewFSI52026108
| Credit       | Card | Fraud     | Detection |            | Through  | Deep |     |     |     |
| ------------ | ---- | --------- | --------- | ---------- | -------- | ---- | --- | --- | --- |
| Learning     | and  | Real-Time |           | Data       | Streams: |      |     |     |     |
| A Comparison |      | and       | New       | Directions |          |      |     |     |     |
EliasPolytarchos1,*
1DepartmentofManagementScience&Technology,AthensUniversityofEconomics&Business,Greece
Abstract:
Creditcardfrauddetectionhasbecomeacriticalconcernforfinancialinstitutionsasthevolumeofdigitaltransactionsgrows
rapidly.Thispaperpresentsacomparativestudyoftwoadvancedmethodologies–deeplearningandreal-timedatastreamanalysis–applied
tocreditcardfrauddetection.Deeplearningmodels,particularlyLongShort-TermMemorynetworks,demonstratedhighaccuracy(upto
92%)inpredictingcustomerbehaviorsandcontributingtothedetectionoffraudulenttransactions.However,theyrequirelargeamountsof
historicaldataandmaynotbeidealforreal-timedetection.Incontrast,real-timedatastreamanalysis,poweredbyinnovativetechniques
likethepatentedBEReTiCsystem,providesimmediatefrauddetectionbutwithlowerinitialaccuracy.Thispaperexploresthetrade-offs
betweentheseapproaches,highlightingthestrengthsofdeeplearninginpatternrecognitionandtheadaptabilityofreal-timedatamining
indynamicfinancialenvironments.Weevaluatebothtechniquesonreal-worlddata,measuringaccuracy,falsepositives,andadaptability
tonovelfraudpatterns.Resultsindicatethatwhiledeeplearningoffershighaccuracy,BEReTiCenablesfasterdetectionwithfewerfalse
alarms and enhanced responsiveness. The findings suggest that a hybrid model integrating both techniques may offer a more effective
solutionfortacklingthecomplexitiesofcreditcardfraudinrealtime,sinceitwouldcombinethepredictivepowerofdeepmodelswiththe
agilityofreal-timeanalytics,openingnewdirectionsinfraudpreventionforhigh-velocityfinancialenvironments.
Keywords: clusteringalgorithms,datastreams,patternrecognition,timeseriesanalysis,deeplearning,frauddetection
1.Introduction Despitetheemergenceofsuchtools,existingliteraturelacks
acomprehensive,empiricalcomparisonofreal-timeunsupervised
Inthemoderneraofdigitaltransactions,creditcardfraudhas stream-basedmethodswithdeeplearning-basedbatch-trainedmod-
| emerged | as a significant challenge | for | financial | institutions and |                   |                    |           |           |        |
| ------- | -------------------------- | --- | --------- | ---------------- | ----------------- | ------------------ | --------- | --------- | ------ |
|         |                            |     |           |                  | els, particularly | in fraud detection | scenarios | involving | highly |
consumers alike. As online payments and e-commerce activities imbalanced,high-volumefinancialdata.Thisgapiscritical:without
continue to rise, credit card fraud remains a persistent challenge suchcomparativeanalyses,systemdesignerscannotmakeinformed
due to the sophistication of evolving fraud tactics and the imbal- decisions about deploying timely and effective fraud prevention
| anceinherentintransactiondatasets.Thisgrowingthreatnotonly |                  |     |              |                | mechanisms. |     |     |     |     |
| ---------------------------------------------------------- | ---------------- | --- | ------------ | -------------- | ----------- | --- | --- | --- | --- |
| causes substantial                                         | financial losses | but | also affects | consumer trust |             |     |     |     |     |
Thispaperpresentsacomparativeevaluationofthesemethod-
andcompliancewithregulatoryobligations,makingeffectivedetec- ologies,exploringtheirperformanceonalarge,real-worlddataset
tionsystemsacriticaloperationalpriority.Consequently,thereisa of credit card transactions. The study focuses on addressing criti-
needformoreadvanced,scalablesolutionsthatcananalyzedatain cal gaps in speed, adaptability, and accuracy to propose a hybrid
realtime,ensuringquickerdetectionoffraudulenttransactions. solutionthatcombinesthestrengthsofbothapproaches.Inpartic-
Traditionalmethods,suchasrule-basedsystemsandmachine
ular,itaimstoevaluatetheeffectivenessofthepatentedBEReTiC
learningmodelstrainedonhistoricaldata,facelimitationsinreal- real-time data stream analysis methodology, which is capable of
time fraud detection, where immediate action is critical. While operating without prior data cleansing, against high-performing
deep learning techniques like Long Short-Term Memory (LSTM) deeplearningframeworkstrainedonhistoricaldata.Toourknowl-
networks excel in identifying intricate patterns within time series edge, this is among the first comparative evaluations of deep
| data, they | require extensive preprocessing |     | and retraining, | making |                     |                   |      |                   |     |
| ---------- | ------------------------------- | --- | --------------- | ------ | ------------------- | ----------------- | ---- | ----------------- | --- |
|            |                                 |     |                 |        | learning approaches | against real-time | data | stream frameworks | for |
themlesspracticalfordynamicenvironments.Conversely,real-time fraud detection. The deep learning methods are used only for
clusteringmethods,suchastheBEReTiCsystem,aredesignedto comparison; the research does not claim any contribution to
| detectanomaliesinstantlybyanalyzingdatastreamswithoutprior |     |     |     |     | these. |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
cleansing. The core research question explored in this paper is: Can
|     |     |     |     |     | real-time pattern | recognition without | any | a priori knowledge | be  |
| --- | --- | --- | --- | --- | ----------------- | ------------------- | --- | ------------------ | --- |
employedtodetectfraudondatastreamsoftransactions,andhow
| *Corresponding | author: Elias Polytarchos, |     | Department | of Management |     |     |     |     |     |
| -------------- | -------------------------- | --- | ---------- | ------------- | --- | --- | --- | --- | --- |
doesitfareagainstbatch-traineddeeplearning?
Science&Technology,AthensUniversityofEconomics&Business,Greece.
Email:ipoli@aueb.gr
© The Author(s) 2025. Published by BON VIEW PUBLISHING. This is an open access article under the CC BY License (https://creativecommons.org/licenses/
by/4.0/).
01
Pdf_Folio:1

FinTechandSustainableInnovation Vol.00 Iss.00 2025
TheBEReTiCmethodology,theSCoDe2mechanism,andthe anomaly detection in sequence data [16] introduce symbolic rep-
CluNNalgorithmpresentedinthispaperaretheobjectofthepatent resentations and interpretable rule violations, offering valuable
PCT/GR2024/000039/02-12-2024(GR1010876)[1]. insights into time-dependent financial streams. Together, these
methodologies exemplify how unsupervised learning – grounded
2.Background in efficiency, accuracy, and explainability – can form the founda-
tionofadaptivefrauddetectionsystems,withstrongpotentialfor
Typically,frauddetectionincreditcardtransactionsandfinan- integrationintonear-real-timeanalyticspipelines.
cial risks in general is considered a data mining problem, where Beyond specialized fraud detection efforts, advancements in
clustering algorithms and other unsupervised machine learning real-timefinancialmodelingoffervaluableconceptualparallels.For
methods are employed to analyze datasets and detect suspicious example, Zhang et al. [17] introduced a cost-sensitive deep rein-
actions[2–6]. forcementlearningapproachforportfoliooptimization,addressing
An interesting approach, in the context of credit card fraud the challenges of non-stationary environments and asymmetric
detection,wherethenumberoffraudulenttransactionsissignificantly transactioncosts–bothofwhicharefundamentaltofraudanalytics.
lowerthannon-fraudulentones,leadingtoimbalanceddatasets,is Similarly,Lietal.[18]presentamultimodalLSTMarchitecturethat
Generative Adversarial Networks (GANs) [7]. Traditional binary integratestemporalandtextualsignalsforevent-drivenprediction
classification models may struggle with imbalanced data, as they infinancialmarkets.Whiletheaimofthepaperisstockforecast-
tendtobiasresultstowardthemajorityclass;whileoversampling ing,theunderlyingmechanisms(i.e.,sequencemodeling,concept
theminorityclassisacommontechniquetoaddressimbalance,it driftadaptation,andmultimodalfusion)resonatestronglywiththe
hasitslimitations.GANsaredeeplearningmodelsthataretrained objectivesofreal-time,data-drivenfrauddetectionsystems.
togeneratesyntheticexamplesoftheminorityclass,creatingamore Inthenextsections,wewillpresentthedatasetemployed,as
balancedtrainingset[8].Thegeneratedminorityclassexamplesare wellasanalyzetheemployedmethodologyandpresenttheresults.
combinedwiththeoriginaldataset,creatinganaugmentedtraining
set.Experimentsshowthatclassifierstrainedontheaugmentedset 3.Dataset
outperformthosetrainedontheoriginaldata.Notably,sensitivity,
whichiscrucialinfrauddetection,issignificantlyenhanced.The Twoseparatedatasetsthatcontainedhistoricaldataforasingle
combinedapproachofGANsandaugmentedtrainingsetsresultsin yearwereprovided:
amoreeffectivefrauddetectionmechanism[9]. IND dataset: 17514242 individual credit/debit card transac-
Infinancialapplications,akintonumerousreal-worldscenar- tionsand
ios,thedataposeschallengesthatarelessprevalentintraditional SUM dataset: 1207817 summaries for credit/debit card
academic datasets. Notable among these challenges are issues purchases
relatedtosize,noise,sparsity,anduncertainty.Moreover,themajor- Thedatawerelabeled,complete,andwellstructured.TheIND
ityoffinancialdatasetsexhibitapronouncedimbalance[10].Take dataset contained a non-negative time series, where each record,
credit card applications, for instance, where, as noted above, the besidesthetimestampofthepurchaseandthecustomerindex,also
numberofreliablecustomerssignificantlyoutweighsthatofprob- containedinformationregardingthespecifictransaction(merchant
lematic customers. Similarly, in fraud detection, the dataset is type, coarse location, month, season, and price range), as well as
predominantlycomposedofnormaltransactions,withonlyasparse demographic information (whether the customer has children or
representationoffraudulentones.Consequently,therearisesaneed not,gender,education,occupationcategory,agerange,totalfunds
forpredictiveanalyticstechniquesadeptathandlingtheintricacies range).TheSUMdatasetcontainedthetotalnumberofpurchases
of unbalanced financial datasets, facilitating the creation of accu- of every customer separated by category of expense (automotive
rate and interpretable financial models [11]. A wealth of research and maritime, gambling, energy, government and taxes, health,
existsregardingtheclassificationofunbalanceddatasets.Anexcel- home equipment, insurance, education, leisure activities, dining,
lentreview,whichdoesnotfocusonthereal-timefacetoftheissue, clothing,services,FMCG,electronics,travel)alongwiththeirtotal
canbefoundat[12].Ontheotherhand,itpresentsacomprehen- amount and demographic information (the demographic informa-
sive study on the application of machine learning techniques for tion included in the SUM dataset was the same as IND, with the
real-timefrauddetectioninfinancialtransactions[13].Itexplores additionofeducationlevel,maritalstatus,city,customertype).
bothsupervisedandunsupervisedmodels(e.g.,decisiontrees,Sup-
port Vector Machines, and neural networks) to identify patterns 4.Methodology
and anomalies indicative of fraud. The study highlights the inte-
grationofthesemodelsintoscalablesystemscapableofhandling Traditionalapproachestofrauddetectionprimarilyframethe
high-transactionvolumeswithlowlatencyandimprovedaccuracy. problemasadataminingchallenge,oftendealingwithunbalanced
Experimentalresultsdemonstratesignificantimprovementsinfraud datasetswherefraudulenttransactionsrepresentatinyfractionofthe
detectionratesandfalsepositivereduction. data.Whiletheseapproacheshavebeensomewhateffective,they
Anomaly detection is a cornerstone of financial fraud detec- comewithseveralinherentlimitationswhenappliedtoreal-world,
tion, where malicious behavior often appears as subtle devia- dynamicenvironments.Specifically,traditionalmethodsrelyon:
tions in high-volume, high-dimensional, or sequential transaction Machinelearningonunbalanceddata:Thesemodelsmust
data. The Empirical-Cumulative-distribution-based Outlier Detec- contendwiththeimbalanceoflegitimateversusfraudulenttransac-
tion(ECOD)methodologyprovidesalightweight,parameter-free, tions,requiringstrategiessuchasoversampling,undersampling,or
andinterpretableapproachbyidentifyingrareeventsthroughempir- syntheticdatageneration.However,thesetechniquescanfallshort
ical cumulative distributions, facilitating scalable and transparent inadaptingtoemergingfraudpatterns.
detection[14].Score-GuidedNetworks(SGN)[15]furtherenhance Vetted, pre-cleansed datasets: For accuracy, these models
performance by learning scoring patterns from existing detectors often depend on pre-processed, well-curated datasets, a step that
in a teacher-student setup, improving accuracy without domain- not only introduces delays in fraud detection but also limits the
specific tuning. Complementing these, rule-based approaches for adaptabilityofthemodelstoreal-timeenvironments.
02
Pdf_Folio:2

FinTechandSustainableInnovation Vol.00 Iss.00 2025
Frequentretraining:Machinelearningmodelsrequireregular characteristics of the transaction (children, gender, education,
retrainingtorecognizenewtypesoffraud,whichincursasignificant occupation category, age range, and total funds range). We also
costintermsofbothtimeandresources.Thisretrainingcyclecan incorporated aggregated behavioral data from the SUM dataset,
hinderthedetectionofrapidlyevolvingfraudtacticsinrealtime. specificallythedistributionofpurchasecategoriespercustomer.
Theselimitationsmakeconventionalmethodologieslesssuit- Basedonthis,weperformedaninitialprocessingstepwhere
able for real-time fraud detection, where transactions must be we averaged the transactional features of each customer. Using
analyzedinstantlytopreventfraudulentactivitiesastheyoccur.In theseprofiles,wegenerated1000synthetictransactionsthataligned
thispaper,weproposeareal-timeclusteringapproachthatdirectly withtheaveragebehaviorofadifferentcustomerthantheonethey
addressestheseshortcomingsandrepresentsanovelmethodological wereassignedto–therebysimulatingfraudulentbehaviorbasedon
contributiontothefield. behavioralinconsistency.
Our key innovation lies in the development of a real-time The main contribution of this paper is the introduction of
clusteringmethodologydesignedtodetectanomaliesincreditcard a real-time fraud detection system based on dynamic clustering.
transactionsastheyhappen.Thisapproachdivergesfromtraditional This method offers several advantages over traditional and deep
methodsinseveralcrucialways: learning-basedapproaches,including:
Dynamicclusteringonlivedata:Insteadofrelyingonhistor- Speed:Instantaneousdetectionoffraudwithouttheneedfor
ical,pre-cleanseddatasets,oursystemoperatesonlivetransaction datacleansingorretraining.
streams.Transactionsareclustereddynamicallybasedontheirfea- Adaptability: The ability to identify novel fraud patterns in
tures,suchastransactionamount,location,time,andfrequency.By realtime,addressingtherapidlyevolvingnatureoffraudtactics.
continuouslyupdatingtheseclustersinrealtime,ourmodelisable Scalability: Efficient operation in high-transaction environ-
to identify transactions that deviate from established patterns and mentswithminimalcomputationaloverhead.
flagthemforfurtherinvestigation. Byaddressingthelimitationsofexistingfrauddetectionmeth-
Immediate detection of novel fraud patterns: Traditional ods,ourreal-timeclusteringapproachpresentsanovelsolutionthat
methods can struggle to detect new fraud tactics until they have isbothpracticalandeffectiveforhigh-velocitytransactionsystems.
occurred, and the models have been retrained. In contrast, our Toaddressthechallengesoffrauddetectioninhigh-velocity
real-time clustering approach is inherently adaptive, capable of financialenvironments,weimplementedandevaluatedtwodistinct
identifyingemergingpatternswithoutneedingretraining.Anysig- approaches:adeeplearning-basedpipelineandareal-timedatastream
nificantdeviationfromexistingclustersisimmediatelyflaggedas analysissystem.Thissectionoutlinesthemethodologyfollowedin
suspicious,allowingforfasterfraudintervention[19]. thiscomparativestudy,brokendownintotwomainbranches:
Scalability and adaptability: Unlike deep learning and tra- Deeplearningpipeline:Thisapproachinvolvedpreprocess-
ditionalmachinelearningmodels,whichcanberesource-intensive ing a large historical dataset, training multiple supervised models
andrequiresignificantcomputationalpowerforretraining,ourclus- (LSTMandMLP)toclassifykeydemographicandbehaviorallabels
tering method is lightweight and highly scalable. This makes it of the customer and computing the degree to which transactions
particularly well-suited for environments with large volumes of deviate from the expected profile. The deviation was quantified
transactions, such as those handled by financial institutions. Our using a composite metric (SST), which enabled the identification
systemcananalyzeandadapttopatternsinrealtime,evenasthe of potentially fraudulent transactions based on misclassification
volumeoftransactionsfluctuates. consensusamongtheensembles.
No need for data cleansing or preprocessing: One of the Real-time clustering and classification: In parallel, we
majorbottlenecksinfrauddetectionisthetimespentcleansingand deployed a real-time system (BEReTiC) capable of processing
vettingdatasetstoensuremodelsareaccurate.Ourreal-timeclus- streaming data without prior cleansing. This system dynamically
teringmethodologybypassesthisrequirement,asitworksdirectly clusterstransactionsandcustomerprofilesusingasemi-supervised
on raw transaction data, making it far more efficient in practical approach, detects behavioral deviations in real time, and flags
deployment.Thisallowsforquickerdetectionandresponsetofraud, anomalies through concept drift and similarity analysis (Gower
withouttheoverheadofpreparingdatasets. metric).
Toassesstheeffectivenessofourreal-timeclusteringmethod, Inbothapproaches,syntheticfraudulenttransactionsweregen-
wealsodevelopedadeeplearning-basedapproachasabenchmark erated and injected into the dataset to assess detection capability.
for comparison. Deep learning models, known for their ability to Thedeeplearningmodelsoperatedinabatchsetting,whilethereal-
identify complex patterns, were applied to the same dataset used time pipeline processed data incrementally, adapting to emerging
forreal-timeclustering.However,despitetheirpowerfulcapabili- patterns.Thesubsequentsectionsdescribethesemethodologiesin
ties,thedeeplearningmodelsrequiredextensivepreprocessingand detail,alongwiththeexperimentaldesignandevaluationcriteria.
retraining,makingthemlesssuitableforreal-timefrauddetection.
Thecomparisonhighlightsthecapabilityofreal-timeclusteringto 4.1.Deeplearning
deliveracceptableresultsinenvironmentswhereimmediatedetec-
tioniscrucialbutalsoexemplifiestheexcellentresultsthatcanbe Inspiredbytheparadigmofensembleclassifiersandthefact
achievedthroughfinelytuneddeeplearningmethodologies. thateachcreditcardtransactionisperformedbetweentwoknown
Toevaluatefrauddetectioncapabilities,weinjectedsynthetic bankentities(customerandbusiness),forwhomthebankhasample
fraudulenttransactionsintotheINDdataset,whichcontainsindivid- information,weusedtheapproachesdescribedbelow.
ualtransactionrecords.Thefirststepwastodefinewhatconstitutes Our initial approach focused on employing state-of-the-art
afraudulenttransaction.Atransactionconductedbysomeoneother machinelearningmethodologiestopredictthetotalfundscategory
thantherightfulpartyisclearlyfraudulent;however,detectingsuch ofthecustomerthatperformedthetransactions,basedontheIND
behaviorrequiresthepresenceofadditionalindicators.Theseinclude dataset.Thetotalfundscategorywasselectedduetoitscapability
deviationsfromthecustomer’stypicaltransactionprofile,asinferred tobeusedinfrauddetectionortargetedadvertisements.Thehigher
fromattributessuchasmerchanttype,generallocation,timeofyear possibilityofacustomerwhowillconsistentlybeclassifiedintoa
(month and season), price range, and the recorded demographic highertotalfundscategorycanindicatethatthey(a)areimplicated
03
Pdf_Folio:3

FinTechandSustainableInnovation Vol.00 Iss.00 2025
infraud;(b)canexceedtheircreditlimit,increasingtheprobabil- todetectandanalyzepatternsinrealtime,amultitudeofnewpos-
ity of having to pay interest; and/or (c) are interested in specific sibilities could emerge, for example: (a) better and more efficient
categoriesofadvertisements.Astheallegationoffraudcannotbe protectionofabank’scustomersfromtheft,(b)real-timedetection
based on the misclassification of a model, however accurate this offraudulenttransactions,(c)abilitytosupportgamifiedchallenges
might be, the case of a fraudulent transaction should be based on for more playful customers (e.g., by automatically notifying cus-
firmergrounds.Inordertodothis,ourapproachwasaugmentedby tomersandprovidingrewardsfortransactionsperformedaccording
expanding the usual ensemble classifier scheme. Instead of using toanewlydetectedtrend)[26],(d)automaticdeductionofappro-
theensembletoclassifyanobjectintoaclass,weusedtheensem- priate advertisements for the customers, or (e) fast response to
bletoclassifyanobjectintomultipleclassesandthenverifythatthe unprecedentedevents.
predictedclasseswerecorrectlyselectedforthisobject. To tackle real-time pattern recognition, we employed our
Concisely,themodelslearnthepatternsofthevarioustrans- work in [1], where we defined a system that can analyze the
actionsbeingperformedbyeachcustomer,andthen,bycalculating datastreaminrealtimeusingasemi-supervisedmachinelearning
howprobableitisthatthecustomerwouldhavenormallyperformed methodology(BestEffortReal-TimeClusteringandClassification
the transaction, they are able to collectively flag a transaction as adapter – BEReTiC). This contains the modules described below.
suspicious.Below,wedefinethemethodthataccomplishesthat: TheirrelationsaredepictedinFigure1[1].
Eachcustomercanbeclassifiedusinganumberoflabels:
whetherthecustomerhaschildrenornot,gender,occupationcat-
egory,agerange,totalfundsrange,educationlevel,maritalstatus, Figure1
city,andcustomertype. RelationsoftheBEReTiCmodules
Eachtransactioncanalsobeclassifiedusingthefollowing
labels:merchanttype,coarselocation,andpricerange.
Each transaction is being performed by a debit or credit
card that belongs to a customer: As such, every transaction
inheritsthelabelsofthecustomer.
A number of classifiers are trained using the dataset: In
ordertobeabletoclassifyatransactionintoeachoftheselabels.
WedefinedtheScaleofSuspiciousTransaction(SST):The
percentage of the classifiers that did not correctly predict the rel-
evant labels of the customer that performed a transaction and the
Scale of Legitimate Transaction (SLT) as the complement of the
SST.
WedefinedtheConfidenceoftheSST(CSST):Theproduct
of the accuracy that had been achieved during the training of the
classifiersthatcomprisedtheSSTandtheConfidenceoftheSLT
(CSLT)astherelevantvaluefortheSLT.
Consequently:IftheSSTislargerthan0.5(i.e.,themajority
ofthemethodsintheensemblemisclassifiedthetransaction),and
theCSSTislargerthantheCSLT,thenthetransactionisconsidered
as a possible fraud with a confidence factor of CSST, and thus, a
largeamountoftransactionsflaggedaspossiblefraudwithinashort
periodoftimesignifiesahighprobabilityoffraud.
The method above aims to determine, through this “fuzzy”
classificationofatransactiontolabelsthatmatchthelabelsassigned Datareceptor:Thismoduleundertakesthereceptionandini-
tothecustomer,theprobabilitythatatransactioncouldhavebeen tialparsingofthedata,discardinganyitemsthatcannotbeproperly
performed by this customer under standard conditions. A mount- parsed.Itdoesnotperformanyfilteringorpreprocessingofthedata;
ing number of transactions of high SST and CSST values can itmapsthedatatoadatastructure.
indicatefraudulentmovements[20].Weemployedtwodeeplearn- Sample collector and deviation detector (SCoDe2): The
ing methods for the models using the TensorFlow infrastructure. SCoDe2 monitorsthestream,storesarepresentativesampleofthe
Specifically: received detections, measures the statistical properties (standard
WecreatedamodelthatusedanLSTMRecurrentNeuralNet- deviation),andcalculatesandkeepstrackofthemodeofdistances
work,sincethedatasetwasatimeseriesoftransactionsandLSTMs betweentheentities.
havebeenshowntoworkwellwithtimeseries[18,21–24]. Clustering module: The clustering module detects clusters
Wealsoperformedexperimentsusingsimpledeepsequential onthesamplecollectedbySCoDe2,usingthecalculatedmodeof
multilayerperceptronmodels(MLP)[25]. distances as an additional input. The clustering module processes
Aftertrainingthemodels,weemployedthemonadatasetthat the sample whenever input is available from the sample collec-
included only legitimate transactions (according to the bank) and tor,initiatinganewclusteringround.Aconceptdriftgetsdetected
afterwardonthesamedatasetenrichedwithsomethatwouldhave whenever the clusters differ from the clusters of the previous
tobeclassifiedaspossiblyfraudulent. round.
Classificationmodule:Everydatapoint,whetheritwasused
4.2.Realtime inthecontextofthepreviousmodulesornot,isalsoclassifiedby
theclassificationmoduleinoneofthedetectedclusters.
Creditcardtransactionscanbeconsideredasadatastream– Reportingmodule:Asthedesignedsystemisawebservice,
astochastictimeseries–thatcancontainpatterns.Bybeingable itdoesnotcontainauserinterface;thismodulehasbeendesigned
04
Pdf_Folio:4

| FinTechandSustainableInnovation                              |     |     |     |     | Vol.00 | Iss.00 | 2025      |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | ------ | ------ | --------- | --- | --- | --- | --- |
| inordertoprovideinformation,suchasthestatisticalpropertiesof |     |     |     |     |        |        | 5.Results |     |     |     |     |
thestream,theclustersdetected,andthenumberofconceptdrifts.
| ByconvertingtheINDdatasetintoadatastreamandfeeding |     |     |     |     |     |     | 5.1.Deeplearning |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- |
ittotheBEReTiC,wewereabletodetectthepatternsofthetrans-
Ourinitialapproach,whichwasdesignedtopredictthefield
actionsbeingperformedinrealtime.Theclusteringmoduleandthe
classificationmodulewereconfiguredtousetheCluNNalgorithm totalfundsrange,achieveda92%accuracy.
[1]andKNN[27],respectively. Theresultsoftheextendedclassifierschemewerepromising
Thedatastructureemployedbythesystemincluded,foreach andallowedustopredicteachoneofthelabelswithaccuraciesof
upto92%.Specifically,whenusingLSTMmodels,theaccuracies
customer:
were:
Theirdemographicinformation
Afingerprintoftheirtransactions(thecustomer’stransac-
• totalfundsrange:92%
tionprofile)
| Themodeoftheamountofthetotaltransactions |     |     |     |     |     |     | • agerange:86% |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- |
• children:82%
Thepercentageoftransactionspermerchanttype
• occupationcategory:79%
Themodeoftheamountoftransactionspermerchanttype
• customertype:79%
Thepercentageoftransactionsperlocation
• educationlevel:75%
Themodeofthenumberoftransactionsperlocation
| Thepercentageoftransactionspermonth |     |     |     |     |     |     | • gender:73% |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- |
• maritalstatus:72%
Themodeofthenumberoftransactionspermonth
• city:59%
| The | percentage | of transactions |     | per | merchant | type per |     |     |     |     |     |
| --- | ---------- | --------------- | --- | --- | -------- | -------- | --- | --- | --- | --- | --- |
location
WhenusingMLPmodels,theaccuracieswere:
Themodeoftheamountoftransactionspermerchanttype
perlocation
• totalfundsrange:78%
| The   | percentage | of transactions |     | per | merchant | type per | • agerange:81% |     |     |     |     |
| ----- | ---------- | --------------- | --- | --- | -------- | -------- | -------------- | --- | --- | --- | --- |
| month |            |                 |     |     |          |          | • children:64% |     |     |     |     |
Themodeoftheamountoftransactionspermerchanttype
• occupationcategory:71%
permonth
• customertype:64%
Thepercentageoftransactionsperlocationpermonth
• educationlevel:67%
| Themodeofthenumberoftransactionsperlocationper |     |              |       |          |           |        | • gender:72%        |     |     |     |     |
| ---------------------------------------------- | --- | ------------ | ----- | -------- | --------- | ------ | ------------------- | --- | --- | --- | --- |
| month                                          |     |              |       |          |           |        | • maritalstatus:64% |     |     |     |     |
| The similarity                                 |     | metric used, | which | compared | instances | of the |                     |     |     |     |     |
• city:47%
| data structure | described | above,     | was    | the             | Gower similarity | [28].        |                 |                |               |     |                      |
| -------------- | --------- | ---------- | ------ | --------------- | ---------------- | ------------ | --------------- | -------------- | ------------- | --- | -------------------- |
| This was       | selected  | because it | allows | the combination |                  | of categori- |                 |                |               |     |                      |
|                |           |            |        |                 |                  |              | After injecting | the fraudulent | transactions, |     | both in the training |
cal(demographicinformation)andnumerical(thefingerprintofthe datasetandthetestingdataset,788outofthe1000injectedfraudu-
transactions)data. lenttransactionswereabletobedetected,while1340falsealarms
Using the aforementioned metric, we were able to com- werealsoclassifiedaspossiblyfraudulent,thatis,transactionsthat
pare transactions, customers’ fingerprints, and clusters with other were contained in the original IND dataset, a less than 0.007%
transactions,customers’fingerprints,orclusters.
|     |     |     |     |     |     |     | misclassification | rate (assuming |     | that the provided | dataset did not |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | -------------- | --- | ----------------- | --------------- |
Thecomparisonsabovewereusedtocreateclustersoftrans- containadditionalillegaltransactions).
actions(i.e.,collectionsofsimilartransactions)andfingerprintsof
| customers(i.e.,collectionsoftransactionsperformedbythesame |          |              |     |              |     |              | 5.2.Realtime |     |     |     |     |
| ---------------------------------------------------------- | -------- | ------------ | --- | ------------ | --- | ------------ | ------------ | --- | --- | --- | --- |
| customer).                                                 | As such, | by employing |     | the BEReTiC, |     | we were able |              |     |     |     |     |
todynamicallycreateandupdatetheaforementionedclustersand
|               |     |     |     |     |     |     | When                          | using real-time | analysis, | the overall | accuracies, after |
| ------------- | --- | --- | --- | --- | --- | --- | ----------------------------- | --------------- | --------- | ----------- | ----------------- |
| fingerprints. |     |     |     |     |     |     | feedingtheentiredataset,were: |                 |           |             |                   |
Regardingtheexampleinsightsmentionedatthebeginningof
| thesection:                                                  |     |                |     |      |       |               | • totalfundsrange:66% |     |     |     |     |
| ------------------------------------------------------------ | --- | -------------- | --- | ---- | ----- | ------------- | --------------------- | --- | --- | --- | --- |
| Protection                                                   | of  | bank customers |     | from | theft | and real-time | • agerange:53%        |     |     |     |     |
| detectionoffraudulenttransactions.Abigdissimilarityofatrans- |     |                |     |      |       |               | • children:57%        |     |     |     |     |
action from the respective customer’s fingerprint can indicate a • occupationcategory:62%
| fraudulenttransaction.                                  |            |          |     |            |     |              | • customertype:51%   |     |     |     |     |
| ------------------------------------------------------- | ---------- | -------- | --- | ---------- | --- | ------------ | -------------------- | --- | --- | --- | --- |
| Ability                                                 | to support | gamified |     | challenges | for | more playful | • educationlevel:63% |     |     |     |     |
| customers(e.g.,byautomaticallynotifyingcustomersandpro- |            |          |     |            |     |              | • gender:44%         |     |     |     |     |
vidingrewardsfortransactionsperformedaccordingtoanewly • maritalstatus:48%
| detected | trend). | New trends | can | be considered | as  | new clusters | • city:51% |     |     |     |     |
| -------- | ------- | ---------- | --- | ------------- | --- | ------------ | ---------- | --- | --- | --- | --- |
oftransactions,andchallengescouldbeproposalstocustomersto
performtransactionsthatareclassifiedinthiscluster. After injecting the fraudulent transactions, 619 out of the
Automaticdeductionofappropriateadvertisementsforthe 1000 injected fraudulent transactions were able to be detected,
customers.Usingthemostcommonrecenttransactionsofthecus- while574falsealarmswerealsoclassifiedaspossiblyfraudulent,
achievinga0.003%misclassificationrate.
tomers,advertisementsforproductsorservicesthatexistinthesame
|     |     |     |     |     |     |     | The accuracy | of the | predictions | performed | by the real-time |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | ----------- | --------- | ---------------- |
clustercanbeproposed.
Fastresponsetounprecedentedevents.Anexampleofthisis approach was substantially lower than the relevant predictions of
thegamifiedchallengesmentionedabove,andthesecanbeenabled thedeeplearningmethods.Thiscanbeattributedtothefactthatthe
through new clusters of transactions and respective actions upon real-timeapproachwasnotawareofallthetransactionsthatthecus-
tomerhadhistoricallyperformed,atleastwhilethesystemhadnot
theirdetection.
05
Pdf_Folio:5

FinTechandSustainableInnovation Vol.00 Iss.00 2025
calculated a representative fingerprint of the customer. We define trendsinrealtime:aclusterthatdidnotexistanhouragobutconsis-
therepresentativesampleofthecustomerastheonethatdoesnot tentlyappearsnowisastrongsignalofanemergingtrend.Notably,
differfromtheoneobtainedwhenalltheirtransactionshavebeen BEReTiCisdesignedtoworkonrawdatastreams(e.g.,transaction
processed.However,evenafterhavingcalculatedarepresentative logs)withoutofflinecleansing,enablinginstantdetectionofanoma-
fingerprintofthecustomer,theresultscouldnotreachtheaccuracy liesornovelties.Incontrast,traditionalmethodsmightonlycatch
ofthedeeplearningmethods. these shifts in a later batch analysis (if at all), by which time the
trendcouldbewellunderway.Bymaintainingup-to-dateclusters,
5.3.Newdirections thesystemeffectivelyproducesaconstantlyrevisedsegmentation
ofcustomersortransactions,mirroringthelatestpatternsinthedata
Despitethereal-timeapproach’smodestinitialperformance,it stream.
opensseveralpromisingavenuesforadvancingfrauddetectionsys-
tems.Buildingonthecomparativeinsightsofdeeplearningversus 5.4.Summaryanddiscussionofmetrics
streamingmethodspresentedabove,futureworkcanfocusonhar-
nessingreal-timecapabilitiestoenhancefraudmitigation,improve Toimproveclarity,Tables1,2,and3presentaconsolidated
financialserviceresponsiveness,andincreaseadaptabilitytoemerg- summary of the results for each methodology. While no publicly
ing threats. Key directions include technical innovations to blend availableimplementationofexistingsystemswascompatiblewith
andextendcurrentmodels,addressingregulatoryandethicalcon- theprovidedproprietarydatasetfordirectbenchmarking,thegoal
siderationsinlivedecision-makingandpioneeringapplication-level of this study was to explore the relative merits of two fundamen-
featuresthatengageandprotectusers.Below,weoutlinethesenew tallydifferentfrauddetectionparadigms,thatis,batch-traineddeep
directionsandtheirpotentialbenefits,challenges,andopportunities learning versus real-time clustering on streaming data. The pre-
forexploration. sented results are therefore meant to offer a baseline for future
comparative work and hybrid designs, rather than to claim direct
5.3.1.Technicalopportunities superiorityoverexistingsolutions.
HybridModelIntegration:Aclearpathforwardiscombining Existingliteraturesuggeststhatdeeplearningsystems,espe-
thehighaccuracyofdeeplearningwiththeimmediacyofstreaming ciallywhencombinedwithtechniqueslikeoversamplingorGAN-
analytics.Forexample,ahybridsystemmightuseanoffline-trained based augmentation, can achieve high sensitivity in imbalanced
LSTM to provide a strong baseline for fraud scoring, while an fraud detection contexts [7, 9, 30]. However, they often require
online clustering component (e.g., the BEReTiC system) adapts significant preprocessing and are unsuitable for real-time envi-
to live data drift. This combination can mitigate the weaknesses ronments. On the other hand, real-time, unsupervised clustering
of each approach, as deep learning models supply well-learned methods typically prioritize responsiveness and adaptability over
patterns, while real-time modules adjust to new fraud tactics on accuracy.Ourresultsconfirmthistrendandhighlightakeytrade-
the fly. Research into transfer learning or meta-learning for real- off:whiledeeplearningachieveshigheraccuracyinclassification,
timemodels(topre-seedstreamingdetectorswithknowledgefrom the BEReTiC-based real-time system demonstrates faster fraud
deepmodels)isonepromisingareatoaddresscold-startaccuracy responseandreducedfalsealarmrateswhenworkingwithrawdata
drops.Overall,hybridarchitecturescoulddrasticallyimprovefraud streams.
mitigation speed (catching fraud in-flight) without sacrificing the The implications of this study resonate beyond the immedi-
pattern-recognitionprowessofdeepnetworks. ate scope of fraud detection and intersect with broader advances
AdaptiveandSelf-LearningSystems:Astrengthofreal-time inreal-timefinancialanalytics.Forinstance,Manoharanetal.[13]
analytics is adaptability, that is, the ability to update the model directly address the challenges of machine learning-based fraud
as new data arrives, thus handling concept drifts in fraud pat- detectioninhigh-throughputtransactionalsystems,highlightingthe
terns[29].Futuresystemscouldleverageonlinelearningalgorithms practical feasibility of real-time deployments. Similarly, ECOD
and reinforcement learning to continuously adjust fraud decision [27] introduces a parameter-free and interpretable outlier detec-
policies.Forinstance,theBEReTiCcandetecttrendsasnewtrans- tiontechniquebasedonempiricalcumulativedistributions,offering
actionsstreamin,therebyreflectingcurrentcustomerbehavior.The scalability and transparency – two properties vital in financial
BEReTiCapproach,beingasemi-supervisedclusteringandclassifi- domains.TheSGNframework[15]enhancesdetectoraccuracyby
cationadapter,ispotentiallymoreinterpretable(clustersofbehavior learningscoringdistributionsandcouldcomplementfrauddetection
or “fingerprints” can be visualized) than a complex deep neural byrefininganomalydecisionboundaries.Furthermore,theanomaly
net,whichisabonusforexplainingfrauddecisions.Futurework rule detection approach by Gan et al. [16] provides a mechanism
can build on this by integrating explainable AI techniques (like foridentifyingsequentialirregularitiesinsymbolicform,aligning
ruleextractionorprototypeexamplesforclusters)directlyintothe with time-evolving fraud scenarios while ensuring human inter-
streamingpipeline. pretability.Beyondfraud-specificapplications,adjacentworkssuch
as[17]applyreal-timedeepreinforcementlearningandmultimodal
5.3.2.Application-levelinnovations LSTM architectures, respectively, for dynamic portfolio selection
Despite the fact that fraud detection through real-time data and stock prediction. These methods share key objectives with
stream processing cannot be relied on, as BEReTiC’s clustering fraud detection: timely decision-making, cost-sensitive optimiza-
module continuously groups streaming data points into evolving tion,andadaptationtonon-stationarydatastreams.Takentogether,
clusters,itiseffectivelyperformingdynamicsegmentationoffinan- thesecontributionsunderscorethegrowingconvergenceofanomaly
cialbehaviors(e.g.,spendingpatterns).Ifanewpatternofbehavior detection, real-time learning, and financial decision-making and
appears(e.g.,asurgeinapreviouslyraretransactiontypeorasud- suggestafertilelandscapeforfuturecross-domaininnovations.
denshiftinspendinghabits),thealgorithmwillformanewcluster The practical deployment of the proposed method in large-
torepresentit.Thesysteminherentlyflagssucheventsasconcept scalefinancialsystemsalsomeritsconsideration.Insuchenviron-
evolutions – essentially alerting that a new behavioral pattern or ments,transactionvolumescanreachthousandspersecond,neces-
trend has emerged. This mechanism allows BEReTiC to “sense” sitatingsolutionswithlowinferencelatencyandhighthroughput.
06
Pdf_Folio:6

| FinTechandSustainableInnovation |     | Vol.00 Iss.00 | 2025 |     |     |     |
| ------------------------------- | --- | ------------- | ---- | --- | --- | --- |
Table1
Classificationaccuracybylabel
Label Deeplearning(LSTM) Deeplearning(MLP) Real-timeclustering
|     | Totalfundsrange    | 92% |     | 78% |     | 66% |
| --- | ------------------ | --- | --- | --- | --- | --- |
|     | Agerange           | 86% |     | 81% |     | 53% |
|     | Children           | 82% |     | 64% |     | 57% |
|     | Occupationcategory | 79% |     | 71% |     | 62% |
|     | Customertype       | 79% |     | 64% |     | 51% |
|     | Educationlevel     | 75% |     | 67% |     | 63% |
|     | Gender             | 73% |     | 72% |     | 44% |
|     | Maritalstatus      | 72% |     | 64% |     | 48% |
|     | City               | 59% |     | 47% |     | 51% |
Table2
Frauddetectionperformance
|     | Metric                         |     | Deeplearning |     | Real-timeclustering |     |
| --- | ------------------------------ | --- | ------------ | --- | ------------------- | --- |
|     | Injectedfraudulenttransactions |     | 1000         |     | 1000                |     |
|     | Detectedfraudulenttransactions |     | 788          |     | 619                 |     |
|     | Falsepositives                 |     | 1340         |     | 574                 |     |
|     | Misclassificationrate          |     | 0.007%       |     | 0.003%              |     |
Table3
Methodologytrade-offs
|     | Feature               | Deeplearning          |     | Real-timeclustering   |     |     |
| --- | --------------------- | --------------------- | --- | --------------------- | --- | --- |
|     | Accuracy              | High                  |     | Moderate              |     |     |
|     | Latency               | High(batchprocessing) |     | Low(real-timecapable) |     |     |
|     | Preprocessingrequired | Yes                   |     | No                    |     |     |
Adaptabilitytonewpatterns Limited(requiresretraining) High(adaptiveclustering)
|     | Resourceintensity | High |     | Lowtomoderate |     |     |
| --- | ----------------- | ---- | --- | ------------- | --- | --- |
Themodularstructureofourreal-timeframeworkenablesdeploy- on customer behavior profiles allowed deep learning models to
ment alongside existing stream processing infrastructures (e.g., detectinjectedfraudulenttransactionswithanotablesuccessrate,
Apache Flink or Spark Streaming [31]), allowing scalable inges- achievingdetectionfor788outof1000fraudulentcases.However,
tion and scoring of transactions in near real time. Furthermore, it should be noted that this approach also yielded a certain num-
becausetheclusteringandclassificationcomponentsareonlineand ber of false positives, which reflects the challenges of accurately
adaptive,theycancontinuouslylearnfromnewdatawithoutcostly identifyingfraudinhighlyimbalanceddatasets.
retraining cycles, which is an important consideration in environ- In contrast, the real-time analysis approach, while offering
mentsaffectedbyconceptdrift.Overall,theproposedsystemaligns advantages in processing streaming data and detecting fraud as
well with the architectural constraints of modern financial insti- transactions occurred, displayed lower predictive accuracy com-
tutions, supporting timely fraud detection without compromising paredtodeeplearning.Thiswasprimarilyduetothecold-startissue,
performanceorinterpretability. wherethesystemlackedsufficienthistoricaldatatomakeaccurate
predictionsearlyinthetransactionlifecycle.Despitethis,theability
6.Conclusion todetectfraudinrealtimeandadjusttoevolvingtransactionpatterns
highlightsthepracticalityofthismethodindynamicenvironments,
Thispaperexploredtwoadvancedmethodologiesfordetect-
suchasonlinecreditcardtransactions.
ingcreditcardfraud:deeplearningneuralnetworksandreal-time Thecomparisonbetweenthesetwoapproachesrevealsimpor-
datastreamanalysisusingpatentedtechniques.Bothmethodswere tanttrade-offs.Deeplearningexcelsinhigh-accuracyclassification
applied to a large dataset of credit card transactions, and the whensufficienthistoricaldataisavailable,butitmaynotbesuitable
resultsprovideinsightsintotheeffectivenessofeachapproachin forreal-timeapplicationswhereimmediatefrauddetectioniscrit-
real-worldfrauddetection.
ical.Ontheotherhand,real-timeclusteringtechniquesarehighly
The deep learning models, particularly the LSTM networks, adaptableandallowforrapididentificationofsuspicioustransac-
demonstratedhighaccuracyacrossvariousclassifications,withthe tions, albeit at the cost of lower initial accuracy. Future research
mostnotableresultsbeingthepredictionofcustomer“totalfunds mightfocusonintegratingbothmethodologiestocombinethehigh
range”at92%accuracy.Thisconfirmsthestrengthofdeeplearning accuracyofdeeplearningwiththereal-timeadaptabilityofcluster-
inanalyzingtimeseriesdataandidentifyingsuspiciouspatternsin
ing,potentiallyleadingtoanoptimalsolutionforcreditcardfraud
| large,structureddatasets.Theabilitytoclassifytransactionsbased |     |     | detection. |     |     |     |
| -------------------------------------------------------------- | --- | --- | ---------- | --- | --- | --- |
07
Pdf_Folio:7

| FinTechandSustainableInnovation |     |     |     | Vol.00 | Iss.00 | 2025 |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | ------ | ------ | ---- | --- | --- | --- | --- | --- | --- |
The hybrid nature of the proposed future work of integra- [6] Guggilam, S., Chandola, V., & Patra, A. (2022). Tracking
tion (i.e., the juxtaposition of deep learning-based detection with clusters and anomalies in evolving data streams. Statistical
real-timedatastreammodels)offersavaluablesynthesisofpredic- Analysis and Data Mining: The ASA Data Science Journal,
tivepowerandoperationalfeasibility.Whiledeepneuralnetworks 15(2),156–178.https://doi.org/10.1002/sam.11552
excelatcapturingcomplexpatternsintransactionalbehavior,their [7] Mehri,H.,Hawkin,J.,Nickerson,K.L.,Bihlo,A.,&Shoeleh,
computational cost and need for retraining limit their applica- F.(2024).BankGAN:Agenerativemodelforsyntheticfinan-
bility in real-time, high-volume environments. Conversely, the cialtransactions.InThe37thCanadianConferenceonArtificial
| real-time | stream-based | framework | emphasizes | adaptability, | low |     |     |     |     |     |     |     |
| --------- | ------------ | --------- | ---------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Intelligence,1–12.
latency,andcontinuouslearningfromunlabeleddata.Byleverag- [8] Goodfellow,I.,Pouget-Abadie,J.,Mirza,M.,Xu,B.,Warde-
ing the strengths of both paradigms, this hybrid strategy enables Farley, D., Ozair, S., ..., & Bengio, Y. (2020). Generative
comprehensiveevaluationunderpracticalconstraints:deeplearning adversarial networks. Communications of the ACM, 63(11),
modelsserveashigh-accuracyofflinebenchmarks,whilereal-time
139–144.https://doi.org/10.1145/3422622
| stream learners |     | are suited | for production | deployment. | This dual |            |                |            |     |          |                 |     |
| --------------- | --- | ---------- | -------------- | ----------- | --------- | ---------- | -------------- | ---------- | --- | -------- | --------------- | --- |
|                 |     |            |                |             |           | [9] Fiore, | U., De Santis, | A., Perla, | F., | Zanetti, | P., & Palmieri, | F.  |
approachensuresthatperformanceisnotpursuedattheexpenseof (2019). Using generative adversarial networks for improving
responsivenessorscalability,anditopensthedoortolayeredsys- classificationeffectivenessincreditcardfrauddetection.Infor-
tems where batch-trained models periodically inform or calibrate mation Sciences, 479,
448–455. https://doi.org/10.1016/j.ins.
onlinemodelsinacontinuallearningloop.
2017.12.030
[10] Sundarkumar,G.G.,&Ravi,V.(2015).Anovelhybridunder-
EthicalStatement samplingmethodforminingunbalanceddatasetsinbankingand
|     |     |     |     |     |     |     | Engineering | Applications |     | of Artificial | Intelligence, |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | --- | ------------- | ------------- | --- |
insurance.
Thisstudydoesnotcontainanystudieswithhumanoranimal
37,368–377.https://doi.org/10.1016/j.engappai.2014.09.019
subjectsperformedbytheauthor.
|     |     |     |     |     |     | [11] Antonelli, | M., Bernardo,  |              | D., Hagras, | H.,          | & Marcelloni, | F.        |
| --- | --- | --- | --- | --- | --- | --------------- | -------------- | ------------ | ----------- | ------------ | ------------- | --------- |
|     |     |     |     |     |     | (2016).         | Multiobjective | evolutionary |             | optimization |               | of type-2 |
ConflictsofInterest fuzzyrule-basedsystemsforfinancialdataclassification.IEEE
TransactionsonFuzzySystems,25(2),249–264.https://doi.org/
Theauthordeclaresthathehasnoconflictsofinteresttothis
10.1109/TFUZZ.2016.2578341
work.
[12] Pei,W.,Xue,B.,Zhang,M.,Shang,L.,Yao,X.,&Zhang,Q.
(2023).Asurveyonunbalancedclassification:Howcanevolu-
DataAvailabilityStatement
tionarycomputationhelp?IEEETransactionsonEvolutionary
|      |         |          |              |                    |        | Computation, | 28(2), | 353–373. | https://doi.org/10.1109/TEVC. |     |     |     |
| ---- | ------- | -------- | ------------ | ------------------ | ------ | ------------ | ------ | -------- | ----------------------------- | --- | --- | --- |
| Data | are not | publicly | available as | they were provided | to the |              |        |          |                               |     |     |     |
2023.3257230
| author under | a   | non-disclosure | agreement | for the purposes | of this |                 |                |     |     |         |               |     |
| ------------ | --- | -------------- | --------- | ---------------- | ------- | --------------- | -------------- | --- | --- | ------- | ------------- | --- |
|              |     |                |           |                  |         | [13] Manoharan, | G., Dharmaraj, |     | A., | Sheela, | S. C., Naidu, | K., |
study.
|     |     |     |     |     |     | Chavva, | M., & Chaudhary, |     | J. K. | (2024). | Machine | learning- |
| --- | --- | --- | --- | --- | --- | ------- | ---------------- | --- | ----- | ------- | ------- | --------- |
basedreal-timefrauddetectioninfinancialtransactions.In2024
AuthorContributionStatement
InternationalConferenceonAdvancesinComputing,Commu-
nicationandAppliedInformatics,1–6.https://doi.org/10.1109/
| Elias | Polytarchos: |     | Conceptualization, | Methodology, | Soft- |     |     |     |     |     |     |     |
| ----- | ------------ | --- | ------------------ | ------------ | ----- | --- | --- | --- | --- | --- | --- | --- |
ware, Validation, Formal analysis, Investigation, Resources, Data ACCAI61061.2024.10602350
curation, Writing – original draft, Writing – review & editing, [14] Li, Z., Zhao, Y., Hu, X., Botta, N., Ionescu, C., & Chen,
|     |     |     |     |     |     | G. H. | (2022). Ecod: | Unsupervised |     | outlier | detection | using |
| --- | --- | --- | --- | --- | --- | ----- | ------------- | ------------ | --- | ------- | --------- | ----- |
Visualization,Supervision,Projectadministration.
empiricalcumulativedistributionfunctions.IEEETransactions
|            |     |     |     |     |     | on Knowledge | and | Data Engineering, |     | 35(12), |              |     |
| ---------- | --- | --- | --- | --- | --- | ------------ | --- | ----------------- | --- | ------- | ------------ | --- |
| References |     |     |     |     |     |              |     |                   |     |         | 12181–12193. |     |
https://doi.org/10.1109/TKDE.2022.3159580
[1] Polytarchos,E.,Bardaki,C.,&Pramatari,K.(2024).Errorpre- [15] Huang, Z., Zhang, B., Hu, G., Li, L., Xu, Y., & Jin, Y.
dictionandpredictivememorymaintenancethroughrealtime (2023).Enhancingunsupervisedanomalydetectionwithscore-
|                                                         |     |     |     |     |     |        | IEEE     | Transactions |     | on Neural | Networks | and |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | ------ | -------- | ------------ | --- | --------- | -------- | --- |
| machinelearningmethods.Retrievedfrom:https://worldwide. |     |     |     |     |     | guided | network. |              |     |           |          |     |
espacenet.com/patent/search?q=pn%3DGR1010876B Learning Systems, 35(10), 14754–14769. https://doi.org/10.
[2] Kou,G.,Peng,Y.,&Wang,G.(2014).Evaluationofclustering 1109/TNNLS.2023.3281501
algorithms for financial risk analysis using MCDM methods. [16] Gan,W.,Chen,L.,Wan,S.,Chen,J.,&Chen,C.M.(2021).
|             |     |           |                                           |     |     | Anomaly | rule detection | in  | sequence | data. | IEEE Transactions |     |
| ----------- | --- | --------- | ----------------------------------------- | --- | --- | ------- | -------------- | --- | -------- | ----- | ----------------- | --- |
| Information |     | Sciences, | 275, 1–12. https://doi.org/10.1016/j.ins. |     |     |         |                |     |          |       |                   |     |
2014.02.137 on Knowledge and Data Engineering, 35(12), 12095–12108.
[3] Phua,C.,Lee,V.,Smith,K.,&Gayler,R.(2010).Acompre- https://doi.org/10.1109/TKDE.2021.3139086
hensivesurveyofdatamining-basedfrauddetectionresearch. [17] Zhang,Y.,Zhao,P.,Wu,Q.,Li,B.,Huang,J.,&Tan,M.(2020).
arXivPreprint:1009.6119. Cost-sensitiveportfolioselectionviadeepreinforcementlearn-
[4] Williams, G. J., & Huang, Z. (1997). Mining the knowl- ing.IEEETransactionsonKnowledgeandDataEngineering,
edge mine: The hot spots methodology for mining large 34(1),236–248.https://doi.org/10.1109/TKDE.2020.2979700
real world databases. Australian Joint Conference on Arti- [18] Li, Q., Tan, J., Wang, J., & Chen, H. (2020). A multi-
ficial Intelligence, 1342, 340–348. https://doi.org/10.1007/ modal event-driven LSTM model for stock prediction using
|                  |     |     |     |     |     |        | IEEE  | Transactions |     | on Knowledge |     | and Data |
| ---------------- | --- | --- | --- | --- | --- | ------ | ----- | ------------ | --- | ------------ | --- | -------- |
| 3-540-63797-4_87 |     |     |     |     |     | online | news. |              |     |              |     |          |
[5] Adhikari, P., Hamal, P., & Jnr, F. B. (2024). Artificial Intel- Engineering, 33(10), 3323–3337. https://doi.org/10.1109/TK
| ligence | in fraud | detection: | Revolutionizing | financial | security. | DE.2020.2968894 |     |     |     |     |     |     |
| ------- | -------- | ---------- | --------------- | --------- | --------- | --------------- | --- | --- | --- | --- | --- | --- |
InternationalJournalofScienceandResearchArchive,13(01), [19] Kim,H.,Kim,S.,Min,S.,&Lee,B.(2023).Contrastivetime-
seriesanomalydetection.IEEETransactionsonKnowledgeand
1457–1472.https://doi.org/10.30574/ijsra.2024.13.1.1860
08
Pdf_Folio:8

| FinTechandSustainableInnovation |     |     | Vol.00 | Iss.00 | 2025 |     |     |     |     |     |
| ------------------------------- | --- | --- | ------ | ------ | ---- | --- | --- | --- | --- | --- |
DataEngineering,36(10),5053–5065.https://doi.org/10.1109/ [26] Chauhan,S.,Akhtar,A.,&Gupta,A.(2021).Gamificationin
TKDE.2023.3335317 banking:Areview,synthesisandsettingresearchagenda.Young
[20] Large,J.,Lines,J.,&Bagnall,A.(2019).Aprobabilisticclassi- Consumers:InsightandIdeasforResponsibleMarketers,22(3),
fierensembleweightingschemebasedoncross-validatedaccu- 456–479.https://doi.org/10.1108/YC-10-2020-1229
racyestimates.DataMiningandKnowledgeDiscovery,33(6), [27] Fix, E., & Hodges, J. L. (1989). Discriminatory analysis,
1674–1709.https://doi.org/10.1007/s10618-019-00638-y
|               |               |             |                        |     | nonparametric | discrimination: |     | Consistency | properties. | Inter- |
| ------------- | ------------- | ----------- | ---------------------- | --- | ------------- | --------------- | --- | ----------- | ----------- | ------ |
| [21] Bandara, | K., Bergmeir, | C., & Smyl, | S. (2020). Forecasting |     |               |                 |     |             |             |        |
nationalStatisticalReview,57(3),238–247.https://doi.org/10.
| acrosstimeseriesdatabasesusingrecurrentneuralnetworkson |     |     |     |     | 2307/1403797 |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
groupsofsimilarseries:Aclusteringapproach.ExpertSystems
|     |     |     |     |     | [28] Gower, | J. C. (1971). | A general | coefficient | of similarity | and |
| --- | --- | --- | --- | --- | ----------- | ------------- | --------- | ----------- | ------------- | --- |
withApplications,140,112896.https://doi.org/10.1016/j.eswa.
someofitsproperties.Biometrics,27(4),857–871.https://doi.
2019.112896
org/10.2307/2528823
[22] Connor,J.T.,Martin,R.D.,&Atlas,L.E.(1994).Recurrent
|     |     |     |     |     | [29] Pelosi,D.,Cacciagrano,D.,&Piangerelli,M.(2025).Explain- |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- |
neuralnetworksandrobusttimeseriesprediction.IEEETrans-
|     |     |     |     |     | ability | and interpretability | in  | concept and | data drift: | A sys- |
| --- | --- | --- | --- | --- | ------- | -------------------- | --- | ----------- | ----------- | ------ |
actionsonNeuralNetworks,5(2),240–254.https://doi.org/10.
tematicliteraturereview.Algorithms,18(7).https://doi.org/10.
1109/72.279188
[23] Hewamalage,H.,Bergmeir,C.,&Bandara,K.(2021).Recur- 3390/a18070443
|      |                 |          |                     |         | [30] You, | D., Xiao, J., | Wang, Y.,      | Yan,     | H., Wu, | D., Chen,  |
| ---- | --------------- | -------- | ------------------- | ------- | --------- | ------------- | -------------- | -------- | ------- | ---------- |
| rent | neural networks | for time | series forecasting: | Current |           |               |                |          |         |            |
|      |                 |          |                     |         | Z., ...,  | & Wu, X.      | (2023). Online | learning | from    | incomplete |
statusandfuturedirections.InternationalJournalofForecast-
andimbalanceddatastreams.IEEETransactionsonKnowledge
| ing, | 37(1), 388–427. | https://doi.org/10.1016/j.ijforecast.2020. |     |     |     |     |     |     |     |     |
| ---- | --------------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
06.008 and Data Engineering, 35(10), 10650–10665. https://doi.org/
[24] Liu,Y.,Gong,C.,Yang,L.,&Chen,Y.(2020).DSTP-RNN: 10.1109/TKDE.2023.3250472
|              |           |                 |                  |      | [31] Carbone,P.,Katsifodimos,A.,Ewen,S.,Markl,V.,Haridi,S., |     |     |     |     |     |
| ------------ | --------- | --------------- | ---------------- | ---- | ----------------------------------------------------------- | --- | --- | --- | --- | --- |
| A dual-stage | two-phase | attention-based | recurrent neural | net- |                                                             |     |     |     |     |     |
work for long-term and multivariate time series prediction. &Tzoumas,K.(2015).Apacheflink:Streamandbatchprocess-
ExpertSystemswithApplications,143,113082.https://doi.org/ inginasingleengine.BulletinoftheIEEEComputerSociety
10.1016/j.eswa.2019.113082 TechnicalCommitteeonDataEngineering,36(4),28–38.
| [25] Zhao, | Q., Wang, F., | Wang, W., Zhang, | T., Wu, H., | & Ning, |     |     |     |     |     |     |
| ---------- | ------------- | ---------------- | ----------- | ------- | --- | --- | --- | --- | --- | --- |
W. (2025). Research on intrusion detection model based on HowtoCite:Polytarchos,E.(2025).CreditCardFraudDetectionThroughDeep
improved MLP algorithm. Scientific Reports, 15(1), 5159. LearningandReal-TimeDataStreams:AComparisonandNewDirections.Fin-
TechandSustainableInnovation.https://doi.org/10.47852/bonviewFSI52026108
https://doi.org/10.1038/s41598-025-89798-0
09
Pdf_Folio:9