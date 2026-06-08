Article
RFM-Net: A Convolutional Neural Network for Customer
Segment Classification
KadriyeFilizBalbal1 andDeryaBirant2,*
1 DepartmentofComputerScience,DokuzEylulUniversity,Izmir35390,Turkey;
kadriyefiliz.balbal@deu.edu.tr
2 DepartmentofComputerEngineering,DokuzEylulUniversity,Izmir35390,Turkey
* Correspondence:derya@cs.deu.edu.tr
Abstract
CustomerSegmentClassificationisamachinelearningtaskinmarketinganalyticsthat
involvesassigningcustomerstopredefinedcategoriesusingfeaturesderivedfromhistorical
transactionaldata. However,conventionalapproaches,suchasstatisticalandclustering-
basedalgorithms, may face challengesinfully capturingthenonlinear relationshipsin
customerdata,whichcanleadtolimitedinsightsandsuboptimalsegmentationoutcomes.
ThispaperintroducesRFM-Net,anapproachthatintegratesDeepLearningwithRecency,
Frequency,andMonetary(RFM)analysisforcustomersegmentclassification.Byleveraging
RFMfeaturesasinputandlabeledcustomersegmentsasoutput,wedesignedaspecialized
Convolutional Neural Network (CNN) model tailored for classification tasks. In the
proposedmethod,labelsaregeneratedbyarule-basedlogicfromRFMscoresandthen
used as supervised ground truth. Accordingly, learning an expert-defined mapping is
employedtomodelcustomersegmentation,ratherthandiscoveringanewsegmentation
structure. Theproposedmethodenablesbusinessestoclassifycustomersintostrategically
meaningful segments such as Champions, Loyal Customers, At Risk, and Hibernating,
therebyfacilitatingeffectiveandtargetedmarketingstrategies. UnliketraditionalCNN
architectures,RFM-Netoffersamorecompact,lightweight,andcomputationallyefficient
modelwithfewerlayersandparameters,supportingimprovedinterpretabilityandreduced
riskofoverfitting. Experimentalresultsconductedonareal-worlddatasetdemonstrated
theeffectivenessofRFM-Netwithanaccuracyof94.33%. Theresultsofthisstudyshowed
arelativeaverageincreaseof13.17%comparedtotheresultsreportedinpreviousstudies
onthesamedataset. Thecorecontributionofthisresearchliesincombiningthepowerful
generalizationcapabilitiesofdeeplearningwiththeeffectivenessofRFManalysis,offering
arobustsolutionfordata-drivencustomerrelationshipmanagement.
Keywords: machinelearning;customersegmentation;classification;convolutionalneural
network;customerbehavioranalytics
AcademicEditors:JaeJoonAhnand
SukjunLee
Received:8January2026
Revised:20February2026
1. Introduction
Accepted:23February2026
Published:25February2026 CustomerSegmentationplaysasignificantroleinenablingpersonalizedmarketing
Copyright:©2026bytheauthors. strategies,boostingcustomersatisfaction,andenhancingoverallbusinessoutcomes. Re-
LicenseeMDPI,Basel,Switzerland. cency,Frequency,andMonetary(RFM)analysishasproventobeapowerfultechnique
Thisarticleisanopenaccessarticle forunderstandingcustomervalueandbehaviorinmarketinganalytics[1]. Itevaluates
distributedunderthetermsand
customerengagementacrossthreebehavioralmetrics: Recencyvalue(howrecentlythey
conditionsofthe CreativeCommons
boughtsomething), Frequencyvalue(howoftentheymakeapurchase), andMonetary
Attribution(CCBY)license.
Appl.Sci.2026,16,2223 https://doi.org/10.3390/app16052223

Appl.Sci.2026,16,2223 2of28
value(howmuchtheyspend). Thesemetricsenableorganizationstoclassifycustomers
basedontheirsimilarpurchasebehaviors.
Despiteitswidespreaduse,traditionalRFM-basedsegmentationreliesprimarilyon
rule-basedlogic,whichmaylimititsabilitytocapturecertainnonlinearpatternsinreal-
world datasets. In the contemporary business environment, customer behavior can be
multi-facetedandsophisticatedandinfluencedbyavarietyofdynamicfactors. Traditional
approaches,suchasstatisticalanalysisandclustering,maynotalwaysfullycapturethe
intricaterelationshipswithindata,sometimesleadingtosimplifiedcategorizations,limited
understanding, and incomplete interpretations. They sometimes offer static customer
groupingsthatlacktheadaptabilityrequiredindynamicmarketscenarios.Theseshortcom-
ingshavecreatedaneedforapotentiallymorerobust,intelligent,insightful,andadaptable
segmentationtechniqueusingDeepLearning.
Inthisstudy,weintroduceRFM-Net,acustomersegmentationapproachthatfuses
theeffectivenessofRFManalysiswiththestronglearningcapabilityofdeeplearning. By
designingaConvolutionalNeuralNetwork(CNN)trainedonRFMfeatures, RFM-Net
effectively categorizes customers into actionable groups, including Champions, Loyal
Customers,PotentialLoyalists,NeedAttention,AtRisk,AbouttoSleep,andHibernating.
The proposed approach leverages both domain knowledge and data-driven learning,
makingithighlyadaptabletodiversebusinesscontexts.
RFM-Netaddressesthechallengesbysynergizingdomain-drivenfeatures(RFM)with
a data-driven modeling approach (deep learning). This combination allows the model
notonlytopreservetheinterpretabilityoftraditionalRFManalysisbutalsotoenhanceit
throughautomatedlearningandfeatureextraction,enablingdeeperinsightintocustomer
dynamics. Asaresult,thisprovidesbusinesseswithasegmentationsolutionthatisboth
intuitivefordecision-makersandtechnicallyadvancedfordatascientistsandanalysts. A
primary aim of this research is to enable businesses to gain a more profound and data-
drivenunderstandingoftheircustomers,therebyfacilitatingcustomer-centricmarketing
strategiesthatarenotonlytargetedbutalsoefficientandscalable.
UnliketraditionalCNNarchitectureslikeAlexNet,GoogleNet,VGG,andResNet;the
architectureofRFM-Netisrelativelyshallow,consistingofonlyafewlayersandaminimal
number of parameters. Its lightweight structure is both computationally efficient and
highlyinterpretable,allowingforreal-timeapplicationsandeaseofdeployment. Unlike
deepermodels,RFM-Netisoptimizedforlow-dimensionalandtabularRFMdatasamples
toachieveeffectivegeneralizationwithoutoverfitting. ItspeciallyadaptstheCNNpower
to structured customer behavior metrics. Moreover, RFM-Net eliminates the need for
extensivefeatureengineeringormanualclustering.
Thecontributionsofthispaperarefourfold:
• RFM-Net: Generatinglabelsthroughrule-basedlogicderivedfromRFMscoresand
using them as supervised ground truth. Learning an expert-defined mapping to
representcustomersegmentationinsteadofdiscoveringanewsegmentationstructure
fromthedata.
• ValidationandComparison: ValidatedRFM-Netbyahighaccuracyof94.33%using
areal-worlddatasetanddemonstratedasignificantrelativeincreaseof13.17%over
previouslyreportedresultsintermsofclassificationaccuracy.
• Strategic Insights: Providing businesses with a reliable, advanced, and powerful
solutionforcustomersegmentationinmarketing.
• Benefits: UnliketraditionalCNNarchitectures,RFM-Netoffersamorecompactand
lightweightframeworkwithfewerlayersandparameters,enhancedinterpretability,
andoptimizationforcustomersegmentationusingstructuredRFMdata,withreduced
https://doi.org/10.3390/app16052223

Appl.Sci.2026,16,2223 3of28
risk of overfitting, enabling end-to-end learning without the need for a separate
clusteringalgorithm.
The rest of the paper is structured as follows: Section 2 provides an overview of
existingcustomersegmentationmethods. Section3detailstheresearchmethodologyand
introducestheproposedRFM-Netmodel. Section4reportstheexperimentalresultsand
comparative analysis, discussing the findings and their practical implications. Finally,
Section5wrapsupthestudyandhighlightsavenuesforfuturework.
2. RelatedWork
Thissectionprovidesasystematicreviewofcurrentstudiesincustomersegmentation.
Table1providesasummaryofpreviousstudies[2–10],includingthemethodsemployed,
theirapplicationpurposes,thetypesoftasksaddressed(classificationorclustering),the
performancemetricsused,andtheregionsinwhichthestudieswereconducted.
Table1. Summaryofpreviousstudies. C:Classification,K:Clustering,S:Silhouette,A:Accuracy,
P:Precision,R:Recall,F:F-Measure,CM:ConfusionMatrix,AUC:AreaUnderCurve. NA:Not
√
Available, :Available.
Ref. Year Region Methods Domain Description C K Period Metrics
K-means, √
[2] 2025 U.S. Retail Customersegmentation NA S
HierarchicalC.
√
[3] 2025 Portugal K-means,DBSCAN Bank Customersegmentation NA S,A,F
Postal √
[4] 2025 Slovakia Statisticalmethods Customersegmentation 2024 NA
Market
HierarchicalC.,GBM, √ √ A,P,R,
[6] 2024 Serbia E-Commerce Correspondenceanalysis 2022
DT,KNN,NB,RF,SVM F,AUC
√ √
[10] 2024 Iran SOM,CART HairCare IoT-CRM 2017–2018 A,P,R,F
√ √
[9] 2022 Brazil DBSCAN,XGBoost,LR E-Commerce Churnanalysis 2016–2018 AUC
√ √ A,P,R,
[5] 2022 China K-means,SVM E-Commerce Churnanalysis 2017
CM,AUC
√
[7] 2022 Malaysia K-means E-Commerce Customersegmentation 2019–2021 A,time
K-means, √
[8] 2021 China Bank Customersegmentation 2020 Density
HierarchicalC.
RFM,Deep Customersegment √
Proposed U.K. Retail 2010–2011 A,P,R,F,CM
Learning(CNN) classification
Some studies in the literature treat customer segmentation solely as a clustering
task[2–4,7,8],whereasothersaddressitwithinaclassificationframeworkaswell[5,6,9,10].
In[2],researchersclusteredcustomersintodifferentsegmentsashighspendersandsea-
sonalshoppers. In[3],customersweredividedintofourdifferentgroupsusingclustering
tasks, andtheimportanceofthisindeterminingmarketingstrategieswasemphasized.
In[4],whereathree-dimensionalsegmentationmodelwasapplied,asystem-basedcluster-
ingapproachwasadopted. Thestudywasimplementedunderreal-worldconditionswith
customersofacompanyinthepostalmarket. In[5],whereB2Ce-commercecustomers
weresegmentedbasedontheirshoppingbehavior,theproblemsituationwastreatedas
bothclusteringandclassificationtasks.In[6],machinelearning(ML)methodswereusedto
examinethepreferencesandbehaviorsofe-commercecustomers. Theresearchersdivided
customersintothreemaingroups(young,unemployed,andfemalee-customers;retirees
andtheelderly;andemployed,highlyeducated,andmiddle-agedmen). Afterthat,classi-
ficationwasperformedusingthelabeleddataobtainedinthestudy. Therearealsostudies
intheliteraturethatutilizeMLmethodstoseparatecustomersintodifferentcategories
https://doi.org/10.3390/app16052223

Appl.Sci.2026,16,2223 4of28
basedontheirsimilarbehaviors,withthegoalofrecommendingtherightproducttothe
rightcustomerforlong-termprofit[7,8].
Some studies have utilized traditional ML methods, such as Support Vector Ma-
chine(SVM)[5,6],NaiveBayes(NB)[6],DecisionTree(DT)[6,10],K-NearestNeighbors
(KNN)[6],andArtificialNeuralNetworks(ANN)[10]. SVMexhibitedbetterprediction
performancewithhigheraccuracythanothermodelsinB2Ce-commercecustomers’churn
predictionmodel[5]. Itwasalsoamongthemachinelearningclassifiersappliedtoidentify
e-customerprofiles(clusters)andwasoneofthealgorithmsshowingthehighestoverall
classificationperformance[6]. TheGaussianNaïveBayes(GNB)algorithmwasalsoused
toidentifythesamee-customerprofiles,butitshowedlowerperformanceinmulti-classac-
curacyandAreaUndertheCurve(AUC)metricsthanensemblemethods,suchasRandom
Forest[6]. TheClassificationandRegressionTree(CART)techniquewasappliedtodeter-
minetheimportanceof17keyfactorsaffectingcustomersatisfactionaftersegmentingIoT
customers[10]. TheKNNalgorithmwasamongthetestedalgorithmsine-customerprofile
classification,butitexhibitedlowerperformanceduetothevariabilityinthecategorical
dataset[6]. Finally,Self-OrganizingMap(SOM),amodelbasedonANN,wasappliedto
groupIoTcustomersaccordingtotheirdeviceusagepatterns[10].
Clusteringapproachesusedincustomersegmentationstudiesvary. Mostofthem
usedK-means[2,3,5,7,8],whileothersemployedhierarchicalclusteringalgorithms[2,6,8]
orDBSCAN[3]. K-means-basedapproachesgenerallyaimtosegmentcustomerbehavior
data [5,7] or retail customer value [8]. For example, in [5], K-means was shown to sig-
nificantly increase the performance of the churn prediction model by categorizing B2C
e-commercecustomersintothreegroupsaccordingtotheirshoppingbehavior. Ref.[7]
presentedanimprovedK-meansapproach,namelySAPK+K-means,toanalyzeMalaysian
e-commercecustomerpurchasingbehaviordataandidentifythemostprofitablecustomer
segments. In[3], K-meanswasemployedinthepreprocessingstageofthehybridKM-
DBSCANalgorithm,whichenablessegmentingbankcustomersintofourdistinctgroups
andcanhandlenoisydata. In[2],customersegmentswereidentifiedusingK-meansafter
dimensionalityreduction(FAMD)inmixeddatasetscontainingbothnumericalandcategor-
icalvariables. In[8],improvedalgorithmswereproposedtoaddresstheshortcomingsof
theK-meansalgorithm,includingtheinitialvalueofkandthetendencytofallintoalocal
optimalsolution,forretailcustomerclassificationandquantificationofcustomervalue
systems. In[6],theHierarchicalClusteringonPrincipalComponents(HCPC)methodwas
utilizedtomodelandlabele-customerprofilesbasedondemographicfactors. In[2],Ag-
glomerativeClusteringwasappliedincomparisonwithK-meanstovalidatesegmentation
resultsinmixeddatasets. Similarly,ahierarchicalclusteringalgorithmwasalsousedin[8]
toachievehigherefficiency.
Studiesinthefieldofcustomersegmentationandanalysishavefocusedonvarious
objectivesthatrespondtodifferentindustryneedsanddatatypes. Someofthesestudies
addressCustomerChurnPrediction[5,9,11]andCustomerLifeValue[4,7,8],whileothers
addressCustomerBehavior[2,6,10]. Instudies[5,9],theresearchersfocusedonpredicting
customerchurnine-commerceretail. In[11],theaimwastopredictcustomerretention
behaviorandpredictloyalty.In[9],thecriticalimpactofbehavioralfactorssuchasshipping
costs,productcategories,andcustomerinitialpurchasevalueonchurnisinvestigatedand
revealed. Thestudy[8]aimedatsegmentingretailcustomersintovalue-basedcategories;
customervaluewasquantified,andthenastructuresupportingCRMdecision-makingpro-
cesseswascreatedbyapplyingimprovedk-meansvariants. Studiesadoptingasustainable
developmentperspectivehavefocusedonidentifyingstrategicsegmentswithhighpoten-
tial,lowcost,andhighrelationshipvalue[4,7]. Studiesaimedatunderstandingcustomer
behavior have addressed demographic influences, online preferences, and interactions
https://doi.org/10.3390/app16052223

Appl.Sci.2026,16,2223 5of28
withintheIoTecosystem[2,6,10]. AstudyexaminingSerbiane-commerceusersmodeled
therelationshipsbetweendemographicvariablesandonlinebehavior,showingthatthe
resultingthreebasicprofilescouldlaterbeusedaslabelsforclassificationmodels[6]. Stud-
iesexaminingthebehavioralpatternsofIoTusershaveanalyzedtheimportanceoffactors
affectingcustomersatisfaction[10]. Therearealsostudiesthatperformsegmentationon
mixeddatasetscontainingbothcategoricalandnumericalvariables;inthiscontext,distinct
groupssuchasseasonalbuyersandhigh-spendingcustomershavebeenidentified[2].
Performanceevaluationmetricsacrossstudiesdifferdependingonwhetherthetaskis
classificationorclustering. Sincethemajorityofthereviewedstudieswerefocusedonclas-
sification,theyprimarilyusemetricssuchasaccuracy[3,5,6,11–13],precision[3,5,6,11–13],
and recall [3,5,6,11–13]. These metrics are generally calculated using a confusion ma-
trix[5,12,13]. Furthermore,theF1-score[3,6,11–13]andAUROC[5,6,9,12,13],whichpro-
vide performance evaluations that are insensitive to the classification threshold, have
also been widely applied. In clustering problems [2,3], metrics such as Silhouette coef-
ficient, Calinski–Harabaszindex(CHI),andDavies–Bouldinindex(DBI)wereusedfor
qualityassessment.
Customersegmentationresearchconductedacrossdifferentgeographieshasyielded
importantfindingsabouthowthesemodelsinteractwithregionalmarketstructures,cul-
turalconsumptionhabits,andindustryconditions. StudiesintheEuropeancontext[3,4,6]
havefocusedprimarilyonregulatedservicesectorsande-commerce;inSlovakia,system-
basedsegmentationmodelshavebeenappliedtocorporatecustomers[4];inSerbia,the
impactofdemographicvariablesononlinebehaviorhasbeenexamined[6];andinPortugal,
bankingcustomershavebeenclassifiedusingadvancedclusteringtechniques[3]. Studies
inAsia[7,8,12]havefocusedontopicssuchascustomervaluemanagementandpurchasing
behavior;inChina,retailcustomervaluehasbeensegmentedusinganalyticalmethods[8],
andinMalaysia,“smartsegments”havebeencreatedbymodelinge-commercebehavior
with K-Means [7]. Among the studies conducted in South America, a comprehensive
segmentation and churn forecasting study for the Brazilian e-commerce market stands
out,combiningtransactionrecordsandsocio-demographicindicators[9]. Additionally,
retaildatasetsfromtheUnitedKingdom[12]andtheUnitedStates[2]wereusedasin-
ternationalreferenceswhenregionaldatawerelimited. Thisdiversitydemonstratesthat
customersegmentationmodelsaresensitivetoregionalcontextratherthanuniversaland
emphasizestheneedtocarefullyevaluatetheadaptabilityofthemethodsusedtodifferent
markets[2,4,6].
Customer segmentation has been studied for different regions such as China [8],
Brazil[9],Malaysia[7],Serbia[6],Iran[10],Slovakia[4],Portugal[3],theUnitedStates[2],
andtheUnitedKingdom[12]. Thesestudiesdemonstratehowcustomerbehaviorvaries
acrossdifferentgeographicandculturalcontexts. InEurope,segmentationmodelswere
developedforpostalandbankingservices[3,4],whileinAsia,retailcustomervalueand
e-commerce behavior were highlighted [7,8]. In South America, churn prediction was
addressedusingmulti-sourcedata[9],whiledatasetsfromtheUSandUKwereutilizedas
commonreferencepointsformethodcomparisons[2,12]. Thisdiversitydemonstratesthat
segmentationapproachesaresensitivetoregionaldynamicsandthatmodelsneedtobe
adaptedtodifferentmarketconditions[4].
Datausedincustomersegmentationstudiesgenerallyfallintobasiccategoriessuch
assalestransactions,behaviorallogs,demographicattributes,andgeo-socio-demographic
indicators. Manystudieshavemodeledcustomerpatternsusingtransactional/behavioral
datasuchaspurchasehistory,productviews,andbasketandfavoriteinteractions[2,5,7,12].
In addition, demographic data such as age, gender, education, income, and household
characteristicshavebeenwidelyusedinbothe-commerceuserprofiles[6]andIoTcustomer
https://doi.org/10.3390/app16052223

Appl.Sci.2026,16,2223 6of28
behavioranalysis[8,10].Geo-socio-demographicdata,includingindicatorssuchasregional
populationstructure,incomelevel,andurban/rurallocation,haveplayedasignificantrole,
especiallyinchurnforecastingstudies[9]. Insomesectors,structureddatasuchasbank
customerrecords[3]orESG-basedsustainabilitycriteria[4]havebeenintegratedintothe
modeltocreateanobjective-focusedsegmentation.
Inadditiontothestudiesdiscussedabove,therearealsostudiesthatcombineRFM
analysiswithmachinelearningtechniquesforcustomersegmentation[14–18]. In[16],re-
searchersexploredhybridanalyticalprocessesthatintegrateRFMfeatureswithsupervised
orquasi-supervisedlearningcomponents. Studies[14,17]incorporatedRFMvariablesinto
clustering-basedframeworkstosupportmanagerialdecision-makingprocesses. Similarly,
in[15,18],RFM-focusedsegmentationstrategieswereprimarilyusedwithincenter-based
clustering paradigms to divide customers into predefined behavioral layers (e.g., high-
value,medium-value,low-valuesegments). Themethodologiesofthesestudiesemphasize
segment-basedoptimizationandstatisticalgrouping,generallyrelyingondistancemea-
suresandtheintuitiveselectionofclusternumbers. Unlikestudiesthatprimarilyreliedon
cluster-focusedapproaches,weadoptedadeep-learning-basedsolution.
Consideringthecomparisonabove,conventionalstatisticalandclusteringapproaches
mayofferareasonablesolutionformanagingthecustomersegments. However,insce-
narioswherecustomerbehaviorexhibitspotentiallynonlinearorintricatepatterns,deep-
learningmodelsmightofferadditionaladvantages. Toexplorethispossibility,thisstudy
proposesRFM-Net—anapproachthatcombinesthepredictivecapabilitiesofdeeplearn-
ing with the strategic insights of RFM analysis, aiming to augment the capabilities of
existingmethodologies.
3. MaterialsandMethods
3.1. ProposedMethod(RFM-Net)
This study introduces RFM-Net, a customer segment classification approach that
fusesthevaluableinsightsofRFManalysiswiththepowerfullearningabilitiesofdeep
learning. RFM-Netincorporatesaspecializedconvolutionalneuralnetworkarchitecture
thatprocessesthehistoricalpurchasedataofthecustomers,transformingrawRFMinputs
intomeaningfulcustomersegments. Thismodelidentifiesintricatebehavioralpatterns,
allowingbusinessestocategorizecustomersintostrategicallyrelevantgroupssuchasLoyal
Customers,AbouttoSleep,NeedAttention,andAtRisk.
Figure1presentsthegeneralframeworkoftheproposedapproach. Themethodology
followsastructuredpipelinethatbeginswithrawdataacquisitionandproceedsthrough
preprocessingandfeatureengineeringtopreparethedatasetforanalysis. Afterthelabeled
dataareorganized,themodelissystematicallytrainedandevaluated. Thesubsequent
stages are then followed by generating predictions and ultimately transforming these
outputsintoactionabledecision-makingsupport.
Algorithm1outlinestheRFM-Netmethodologyinaformal,step-by-stepmanner.
Step 1—Data Acquisition: Historical raw customer data is acquired, focusing on
marketing transactions such as purchases and returns. This data can be stored in a
cloud-based platform to ensure scalability, availability, and efficient storage. Formally,
letD = {x ,x ,...,x }denotethedatasetconsistingofntransactions,whereeachtrans-
1 2 n
actionx containsfieldslikecustomerID,invoicenumber,transactiondate,quantity,and
i
unitprice. Foreachcustomerc,thealgorithmgathersalloftheirtransactions,asgiven
inEquation(1):
T = {x ∈ D|x.CustmerID= c} (1)
c
https://doi.org/10.3390/app16052223

Appl.Sci.2026,16,2223 7of28
Step2—DataPreprocessing: Therawdataundergoesseveralpre-processingstepsto
ensureitsquality,integrity,andusability.
- FeatureSelection: Inthisstep,onlythefieldsrelevanttoRFManalysisandcustomer
behaviormodelingareretained,suchastransactiondateandamount. Severalnon-
essentialcolumns,suchascountry,productnumber,andname,areexcludedfromthe
datasettoreducedimensionalityandcomputationalcomplexity.
- DataCleaning: Severalpreprocessingoperationsareappliedtoensuretheintegrity
and consistency of the dataset, including the removal of return transactions, the
handlingofmissingvalues,andtheexclusionofirrelevantentries.
- DataTransformation: Therawtransactionalrecordsareaggregatedforeachunique
customer to calculate Recency, Frequency, and Monetary (RFM) metrics, thereby
quantifyingtheirpurchasingbehavior.
Figure1.ThegeneraloverviewoftheproposedRFM-Netapproach.
Recency (R ) is calculated as the number of days since a customer’s most recent
c
purchase(dc )relativetothelatestdate(d )inthedataset,asgiveninEquation(2). This
last ref
metrichelpsdistinguishbetweenactiveanddormantcustomers.
(cid:16) (cid:17)
R = d −dc .days,
c ref last
whered =max(x.Date)forallx ∈ D (2)
ref
anddc =max(x.Date)forx ∈ T
last c
Frequency(F)reflectshowoftenacustomerhastransacted. Itiscalculatedbythe
c
total number of distinct purchase events (invoices) associated with the customer c, as
giveninEquation(3). Higherfrequencytypicallyindicatesstrongengagementwiththe
marketingplatform.
F = | {x.InvoiceNo |∀x ∈ T }| (3)
c c
Monetary(M )representsthetotalmonetaryvalueofallpurchasesmadebyaspecific
c
customer c over a particular time period. It is derived by summing the product of the
quantity and unit price of each transaction associated with the customer, as given in
Equation(4).Monetaryvaluequantifiesthecumulativefinancialcontributionofacustomer
to the business. This metric is particularly useful in identifying high-value customers
https://doi.org/10.3390/app16052223

Appl.Sci.2026,16,2223
8of28
whogeneratesignificantrevenue. Ithelpsdifferentiatebetweenlow-spendingandhigh-
spendingcustomers,therebysupportingtargetedmarketingstrategies,resourceallocation,
andpersonalizedserviceofferings.
|     |     |     |     |     |     |     |     | = ∑ (x.Quantity×x.UnitPrice) |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | M c |                              |     |     |     |     |     |     | (4) |
x∈Tc
At the end of the first step, each customer is represented by a three-dimensional
featurevectorx = (R ,F,M ). Thesethreefeaturesformthecoreinputrepresentationfor
|     |     |     |     |     | c   | c   | c c |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
trainingthedeeplearningmodel.
Step3—RFMFeatureEngineering: Eachcustomerisassignedthreenumericalscores
(R, F, and M), which collectively capture their engagement level and transactional be-
havior. The continuous RFM metrics are discretized into categorical scores ranging
from 1 to 5 according to the user-defined threshold values, allowing the model to nor-
malize the dataset and better capture customer behavior patterns. This process sorts
the values, determines thresholds, and divides each metric into five segments. Let
Q = {RT ,RT ,RT ,RT } bethethresholdsofrecency, Q = {FT ,FT ,FT ,FT } for
|     |     |     |     | R 1 | 2   | 3   | 4   |     |     |     |     | F   | 1   | 2   | 3 4 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
frequency,andQ = {MT ,MT ,MT ,MT }formonetary,eachcustomer’sRFMvalue
|     |     |     |     |     |     | R   | 1   | 2   | 3 4 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is mapped to a discrete score between 1 and 5 using these thresholds. For example, a
customerwhospendsalargeamountoverallwouldreceiveatopmonetaryscore(e.g.,5),
reflectingstrongfinancialvalue,whereasonewithminimaltotalspendingwouldbeas-
signedalowerscore(e.g.,1),indicatinglimitedcontribution. Therecencyscoreisassigned
inversely—meaningthatalowerrecencyvalue(i.e.,morerecentpurchases)resultsina
higherscore—whilethefrequencyandmonetaryscoresareassigneddirectly,withhigher
valuesyieldinghigherscores,asgiveninEquation(5).
|     |       |       |      |     |     |       |     |      |     |     |       |      |     |     |     |
| --- | ------ | ----- | ---- | --- | --- | ------ | --- | ---- | --- | --- | ------ | ---- | --- | --- | --- |
|     |        | 5 ifR | ≤ RT |     |     | 1      | ifF | ≤ FT |     |     |        | 1 if | M ≤ | MT  |     |
|     |  | c     | 1    |     |     |  | c   | 1    |     |     |  |      | c   | 1   |     |
4 ifRT 1 < R ≤ RT 2 2 ifF T 1 < F ≤ FT 2 2 if M T 1 < M ≤ MT 2
|       |        |          | c     |      |       |        |         | c     |     |       |        |       |      | c   |        |
| ----- | ------ | -------- | ----- | ---- | ----- | ------ | ------- | ----- | --- | ----- | ------ | ----- | ---- | --- | ------ |
| R     | =      | ifRT     | < R ≤ | RT F | =     |        | ifFT    | < F ≤ | FT  | M     | =      |       | MT < | M ≤ | MT (5) |
| score |        | 3        | 2 c   | 3    | score | 3      |         | 2 c   | 3   | score |        | 3 if  | 2    | c   | 3      |
|       |  |          |       |      |       |  |         |       |     |       |  |       |      |     |        |
|       |        | 2 i f RT | < R ≤ | RT   |       | 4      | i f F T | < F ≤ | FT  |       |        | 4 i f | MT < | M ≤ | MT     |
|       |        |          | 3 c   | 4    |       |        |         | 3 c   | 4   |       |        |       | 3    | c   | 4      |
|       |        | 1 i f R  | > RT  |      |       | 5      | i f F   | > FT  |     |       |        | 5 i f | M >  | M T |        |
|       |        | c        | 4     |      |       |        | c       | 4     |     |       |        |       | c    | 4   |        |
Attheendofthisstep,eachcustomer’sRFMscores(R F ,M ,c)aresaved
|     |     |     |     |     |     |     |     |     |     |     |     | score | score | score |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | ----- | --- |
to be further used for assigning segment labels. These categorical scores normalize
customer activity, making it easier to compare and group customers based on similar
behavioralpatterns.
Step4—DataAnnotation: EachcustomerRFMscoretriplet(R,F,M)issubsequently
mappedtoapredefinedcustomersegmentusingrule-basedlogic. Segmentdefinitions
followestablishedmarketingtaxonomy,includinglabelssuchas“Champions”,“Loyal
Customers”,“PotentialLoyalists”,“AtRisk”,andothers,dependingoncombinationsof
highorlowRFMscores. Forexample,iftheRecency(R),Frequency(F),andMonetary(M)
scoresareeachgreaterthan4,thecustomerisclassifiedintothe“Champions”segment,
which comprises the most active and profitable customers. Similarly, customers with
Recency, Frequency, and Monetary scores of R < 2, F < 2, and M < 2 are classified into
the “Hibernating” segment, indicating they are low-value customers (likely to be lost).
Table2presentsRFMsegmentcriteria,characteristics,andtheircorrespondingstrategy
suggestions. Weidentifiedsevendistinctgroupsofcustomersbasedontheirtransaction
history,frequency,andspendinghabits,similartothestudy[19]. Thisrule-basedlabeling
offersaninterpretableandactionableapproachtocategorizingcustomersbasedontheir
behavior. ItcreatesasuperviseddatasetinwhichcontinuousRFMvaluesserveasfeatures
andcustomersegmentsasclasslabels.
https://doi.org/10.3390/app16052223

Appl.Sci.2026,16,2223
9of28
Table2.RFMsegmentrules,characteristics,andassociatedstrategyproposals.
|         | Rangeof             | RangeofM |                 |                     |
| ------- | ------------------- | -------- | --------------- | ------------------- |
| Segment |                     |          | Characteristics | StrategySuggestions |
|         | RValues andFAverage |          |                 |                     |
Offerpremiumcustomerservices,
Veryrecent,frequent,and
| Champions | 4–5 | 4–5 |     | personalizedgifts,andearlyaccessto |
| --------- | --- | --- | --- | ---------------------------------- |
high-spendingcustomers
newproducts
|                |     |     | Frequentandregular      | Motivatewithloyaltyrewardsand |
| -------------- | --- | --- | ----------------------- | ----------------------------- |
| LoyalCustomers | 2–5 | 3–5 |                         |                               |
|                |     |     | buyers—engagedcustomers | periodicappreciationmessages  |
Guidethemindiscoveringrelevant
|                    |     |     | Recent,notyetfrequent | products,providecustomized |
| ------------------ | --- | --- | --------------------- | -------------------------- |
| PotentialLoyalists | 3–5 | 1–3 |                       |                            |
|                    |     |     | butpromising          | communicationsandproduct   |
educationcontent
Mediumrecencyand
|               |     |     | frequency—mayneed          | Implementsurveystounderstandtheir |
| ------------- | --- | --- | -------------------------- | --------------------------------- |
| NeedAttention | 2–3 | 2–3 |                            |                                   |
|               |     |     | re-engagement—unsureifthey | needsandofferexclusiveexperiences |
willmakeanotherbuy
|              |     |     | Infrequentbuyers,havenot | Utilizere-engagementemails,tailored |
| ------------ | --- | --- | ------------------------ | ----------------------------------- |
| AbouttoSleep | 2–3 | 1–2 |                          |                                     |
|              |     |     | visitedinawhile          | discounts,orproductbundles          |
Longtimenopurchase,but
Re-engagewithrecoverycampaigns,big
| AtRisk | 1–2 | 2–5 | stillhavesomevalue |     |
| ------ | --- | --- | ------------------ | --- |
discounts,orurgentlimited-timeoffers
(frequency+spend)
Providelower-costmarketingstreams,
Leastengaged,low-value
| Hibernating | 1–2 | 1–2 |     | genericbulkoffers,orremindersto |
| ----------- | --- | --- | --- | ------------------------------- |
customerswhoarelikelylost
preventchurn
AsgiveninTable2,differentiatedmarketingstrategiescanbeimplementedforeach
customersegmentidentifiedbyRFM-Net. Forthe“Champions”,whoarethemosthigh-
valuecustomers,strategiessuchasVIPprograms,personalizedloyaltyrewards,andearly
access to new products can reinforce their satisfaction. “Loyal Customers” represent a
stablebaseandcanbemotivatedwithmembershipprogramsandperiodicappreciation
messages to maintain their engagement. The “Potential Loyalists”—recent but not yet
frequentbuyers—couldbecultivatedwithwelcomecampaigns,producteducationcontent,
customizedcommunications,andbehavior-basedproductrecommendations. Forthecus-
tomersinthe“NeedAttention”category,surveyscanbeimplementedtounderstandtheir
needs. “AbouttoSleep”customersmightbereactivatedwithre-engagementemails,tai-
loreddiscounts,orproductbundlesbasedonpastbehavior. The“AtRisk”grouprequires
strongerinterventionssuchastargetedwin-backstrategies,deeperdiscounts,orurgent
limited-time offers. Lastly, “Hibernating” customers, with the lowest engagement and
value,maybenefitfromlower-costmarketingstreams,genericbulkoffers,orreminders
to prevent churn. Designing special communication and promotions according to the
purchasing behavior of each group ensures a more efficient allocation of marketing re-
sources,strengthensoverallcustomerrelationshipmanagement,andmaximizescustomer
lifetimevalue.
Figure2illustratesthecustomersegmentationgridderivedfromRFManalysis,where
thex-axisrepresentsRecencyscores(howrecentlyacustomerboughtsomething),andthe
y-axiscombinesFrequencyandMonetaryscores(howoftenandhowmuchacustomer
spends). Eachdimensionisscoredonascalefrom1to5,with5representingthehighest
level of customer behavior (e.g., most recent, most frequent, or highest spending) and
1indicatingtheleastdesirablebehavior. Basedontheirscores,allcustomersareorganized
intosevenpredefinedgroupsonthegrid. Customerspositionedintheupper-rightquad-
rant,suchasChampionsandLoyalCustomers,arethemostvaluableones(highrecency,
highfrequency/monetary). Customerengagementdecreasesasonemovesleftwardand
https://doi.org/10.3390/app16052223

Appl.Sci.2026,16,2223 10of28
downward in the grid. Segments located in the lower-left quadrant (e.g., Hibernating)
representcustomerswhohaveminimalinteractionandexhibitlowspendingbehavior,
potentiallyindicatingthattheyarelostcustomers. Thegridprovidesaclear,quick,and
strategicoverviewofcustomerbehavior,enablingcompaniestodifferentiateandinterpret
customervalueandengagementlevelsataglance.
Figure2.CustomersegmentsinagridviewbasedonRFMscores.
Step5—DataSplitting: Theannotateddatasetispartitionedintothreedistinctparts:
a training set used to build the CNN model, a validation set to monitor training (i.e.,
earlystoppingforpreventingoverfitting),andatestsetforevaluatingthegeneralization
performanceofthemodelonunseendata.
Step6—ModelTraining: ACNNisthentrainedtolearnthecomplexrelationships
betweenRFMpatternsandcustomersegments. TheCNNarchitectureincludeslayerssuch
asconvolutionalkernelstocapturepatterns,poolinglayerstodecreasedatadimensionality,
and dense layers to carry out the classification task. The input to the model consists
ofthenumericalvaluesofrecency, frequency, andmonetarymetricsforeachcustomer.
The output of the model is a probability distribution over possible customer segments,
enablingittopredictthemostlikelyclassforeachnewcustomer. Modeltrainingcanbe
repeatedusingdifferenthyperparameterconfigurationsinordertoimproveperformance
andgeneralization.
Step7—ModelEvaluation: OncetheCNNarchitectureistrained,themodeliseval-
uated on the test set to predict segment labels for previously unseen customers using
standardperformanceindicatorssuchasaccuracy,recall,precision,f-measure,andconfu-
sionmatrix. Theseindicatorshelpevaluatetheabilityofthemodeltodistinguishbetween
customersegments. ThealgorithmoutputsYˆ,thepredictedcustomersegmentlabelsfor
thetestinstancesbasedontheirRFMvalues,asgiveninEquation(6).
Yˆ =Yˆ ∪yˆ, whereyˆ =Model(sample) and sample= (R,F,M) (6)
Step8—Prediction: TheCNNmodelisusedtoclassifyunseencustomersintooneof
thefollowingstrategicsegments,suchaschampions,atrisk,orhibernating. Thispredictive
capabilityenablesbusinessestogainactionableinsightsfortargetedmarketingstrategies.
Step9—Decision-MakingSupport: Thefinalpredictionsarepresentedtobusiness
decision-makersthroughaninterpretabledashboardorreportingsystem. Segment-based
visualizationsandanalyticsenablemarketingteamstomakeinformeddecisionsregarding
campaigndesign,customerretention,andresourceallocation.
Overall,theproposedmethodologyprovidesahybridsolution. Bycombiningthe
interpretability of RFM analysis with the predictive power of deep learning, RFM-Net
offersascalable,data-drivenapproachtocustomersegmentationthatiswell-suitedforreal-
worldapplicationsinmarketing,customerrelationshipmanagement,andpersonalized
recommendation systems. It enables organizations to understand customer behavior
https://doi.org/10.3390/app16052223

Appl.Sci.2026,16,2223
11of28
in a structured way, while also leveraging machine learning to automate and scale the
segmentationprocessforreal-timeapplications.
Algorithm1:RFM-Net:Recency-Frequency-Monetary-basedNeuralNetwork
Inputs:
RT, FT, MT:thresholdvaluesforrecency,frequency,andmonetary,respectively
Outputs:
Yˆ:predictedcustomersegmentlabelsforthetestsamples
Begin:
D←{x ,x ,...,xn } wherex =(CustomerID,InvoiceNo,Date,Quantity,UnitPrice) //Step1:Dataacquisition
| 1 2 | i   |     |
| --- | --- | --- |
RFM_Values←∅
//Step2:Datapreprocessing
d ←max(x.Date)forallx∈D //Referencedate:Themostrecentdateinthedataset
ref
Customers←{x.CustomerID|∀x∈Dandx.CustomerID ̸=null}//Thesetofuniquecustomernumbers
foreachc ∈Customersdo //Calculaterecency,frequency,monetaryvalues
Tc ←{x∈D|x.CustomerID=c} //Alltransactionsbelongingtocustomerc
| dc ← max(x.Dat | e) (cid:12) (cid:12)∀x∈Tc |     |
| -------------- | ------------------------- | --- |
last
| (cid:16) | (cid:17) |     |
| -------- | -------- | --- |
Rc ← d −dc .days //Recency:Dayssincethecustomer’slastpurchase
| ref last |     |     |
| -------- | --- | --- |
Fc ←| {x.InvoiceNo |∀x ∈Tc }| //Frequency:Numberofuniqueinvoices
| Mc ←∑(x.Quantity×x.UnitPrice)forallx |     | ∈ Tc |
| ------------------------------------ | --- | ---- |
//Monetary:Totalspending
| RFM_Values← | RFM_Values∪{(Rc,Fc,Mc,c)} |     |
| ----------- | ------------------------- | --- |
endforeach
| RFM_Scores←∅ |     | //Step3:RFMfeatureengineering |
| ------------ | --- | ----------------------------- |
foreach (r,f,m,c) ∈RFM_Valuesdo //AssignRFMscores(1to5)basedonthresholds
forifrom1to5do
ifr≤RT[i]then
Rscore←6−i
break
endif
if f ≤FT[i]then
Fscore←i
break
endif
ifm≤ MT[i]then
Mscore←i
break
endif
endfor
RFM_Scores←RFM_Scores∪(Rscore,Fscore,Mscore,c)
endforeach
Data←∅ //Step4:Dataannotation
(R,F,M,c)∈RFM_Scoresdo
foreach //Rule-basedlabeling
| AvgFM = (F +     | M)/2         |                               |
| ---------------- | ------------ | ----------------------------- |
| if4≤R≤5and4≤     | AvgFM ≤5then | Segment← ”Champions”          |
| elseif2≤R≤5and3≤ | AvgFM ≤5then | Segment← ”LoyalCustomers”     |
| elseif3≤R≤5and1≤ | AvgFM ≤3then | Segment← ”PotentialLoyalists” |
| elseif2≤R≤3and2≤ | AvgFM ≤3then | Segment← ”NeedAttention”      |
| elseif2≤R≤3and1≤ | AvgFM ≤2then | Segment← ”AbouttoSleep”       |
| elseif1≤R≤2and2≤ | ≤5then       | Segment←                      |
AvgFM ”AtRisk”
| elseif1≤R≤2and1≤ | AvgFM ≤2then | Segment← ”Hibernating” |
| ---------------- | ------------ | ---------------------- |
Data←Data∪{(Recency,Frequency,Monetary,Segment)}
https://doi.org/10.3390/app16052223

Appl.Sci.2026,16,2223 12of28
Algorithm1:Cont.
endforeach
TrainSet,ValidationSet,TestSet←split(Data) //Step5:Datasplitting
BestParams←HyperparameterTuning(CNN,TrainSet,ValidationSet) //Performhyperparametertuning
Model←Train(CNN(BestParams),TrainSet) //Step6:TraintheCNNmodel
//inputs x← (R,F,Mvalues),output y← segmentlabel
Yˆ ←∅
foreachsampleinTestSet //Step7:Testmodel
yˆ←Model(sample)
Yˆ ←Yˆ ∪yˆ
endforeach
End
3.2. TheProposedCNNArchitecture
Inthisstudy,weproposeadeeplearningarchitecturecalledRFM-Net,designedtoen-
hancecustomersegmentationbyintegratingtheclassicalRecency,Frequency,andMonetary
frameworkwithacustom-builtConvolutionalNeuralNetwork. TheaimofRFM-Netisto
helpbusinessesunderstandcustomerbehaviorpatternseffectively,therebyenablingthem
todevelopprecise,customer-centricmarketingstrategies. ThearchitectureofRFM-Netis
composedofseveralkeylayers(inputlayer,convolutionallayer,max-poolinglayer,flatten
layer,denselayer,andoutputlayer),eachofwhichservesadistinctfunctiontosupport
data-drivencustomerclassification. EachcomponentoftheRFM-Netmodelisdescribed
below,highlightingitsspecificcontributiontothecustomersegmentationprocess.
InputLayer: Thislayerreceivesstructuredcustomerdata,typicallycomposedofRFM
features. Thedataisreshapedtoaformatcompatiblewithconvolutionaloperations. Each
inputsamplerepresentsasinglecustomerbehavioralprofile,formingthefoundationfor
deeperpatternextraction.
Convolutional Layers: These layers apply multiple filters to the features to detect
patterns within data. They enable the model to understand how certain RFM feature
combinations(e.g.,highfrequencybutlowmonetaryvalue)mightcorrelatewithspecific
customersegments. Therectifiedlinearunits(ReLU)activationfunctionintheselayers
introducesnon-linearity,whichhelpsinmodelingcomplexrelationships. Thisisparticu-
larlyusefulfordifferentiatingsubtlevariationsincustomerbehaviors,suchasidentifying
“PotentialLoyalists”or“Promising”customers. Anarrowkernelisusedtoensurelocal
featureextractionwithoutoverfitting.
Max-PoolingLayer: Thislayerdecreasesthespatialsizeofthefeaturemapswhile
preservingthemostinformativeones,therebyenhancinggeneralizabilityandreducing
noise. Itensuresminimizingtheimpactofsmallfluctuationsincustomerdata.
FlattenLayer: Themulti-dimensionaloutputsfromtheconvolutionallayersarecon-
vertedintoaone-dimensionalvectorthatissuitableforclassification. Thistransformation
bridges the convolutional layers and the dense classifier while preserving the learned
representationsofcustomerbehavior.
Dense Layer (Fully Connected): This layer processes the flattened vector to learn
higher-levelrelationshipsbetweenRFMpatterns. Itenablesthenetworktoformcompre-
hensiveviewsofcustomerprofiles,suchaswhethercustomersbelongtothe“Champion”
group,characterizedbyconsistentspending,orthe“Hibernating”group,characterizedby
minimalactivity.
OutputLayer: Thislayermapsthelearnedfeaturestomeaningfulcustomerclasses,
suchasChampions,LoyalCustomers,NeedAttention,andHibernating. Itusesasoftmax
activationtoassignprobabilitiesacrossthepredefinedcustomersegments. Thesegment
withthetopprobabilityvalueischosenasthefinalclassification. Thisoutputempowers
https://doi.org/10.3390/app16052223

Appl.Sci.2026,16,2223 13of28
organizationstodesigntheirmarketingstrategiesforeachcustomergroupseparatelywith
greaterprecisionandpersonalization.
Throughthisend-to-endlearningprocess,RFM-Netcanaccuratelycategorizeeach
customerintoarelevantsegment,enablingbusinessestodeveloptargeted,customer-centric
marketingstrategies.
Table3presentsthearchitectureoftheRFM-Netmodel,includingthetypesoflayers
used,theirrespectiveoutputshapes,andthenumberoftrainableparametersateachstage
ofthenetwork. Thearchitecturebeginswithaninputlayer,followedbyconvolutional
layersdesignedtoextractlow-levelfeaturepatternsfromRFMmetrics. Apoolinglayeris
thenappliedtoreducespatialcomplexity.Theprocesscontinueswithaflatteningoperation,
followedbyadenselayerthatinterpretstheextractedfeaturesandanoutputlayerthat
mapsthemtocustomersegmentpredictions.
Table3.TheproposedCNNarchitectureandparametersummary.
Layer OutputShape NumberofParameters
Conv2D (None,2,1,32) 96
MaxPooling2D (None,1,1,32) 0
Conv2D (None,1,1,64) 2112
Flatten (None,64) 0
Dense (None,64) 4160
Dense(SoftmaxOutput) (None,7) 455
TotalParameters 6823(≈26.65KB)
In the proposed CNN model, each customer is represented by three RFM features
(Recency,Frequency,Monetary),whicharereshapedintoasingle-channel2Dtensorofsize
(3, 1, 1)tocomplywiththeConv2Dinputformat. Thefirstconvolutionallayerapplies
32filterswithakernelsizeof(2,1)andReLUactivation,followedbyMaxPooling2Dwith
poolsize(2,1). Additionalconvolutionallayersuse64(orhigher)filterswithkernelsize
(1,1),enablingnonlinearfeaturetransformation. Afterconvolutionandpoolingoperations,
the feature maps are flattened and passed to a dense layer with 64 neurons and a final
softmaxoutputlayercorrespondingtothecustomersegments.
Despiteitsrelativelyshallowstructure,RFM-Netishighlyefficientandeffectivedueto
itscarefultask-specificdesign. Thetotalnumberoftrainableparametersremainsminimal,
ensuringcomputationalefficiencywhilepreservingmodelexpressiveness.Thislightweight
structuremakesRFM-Netidealforreal-worldapplicationswherecomputationalresources
maybeconstrained.
3.3. ComparativeAnalysisofRFM-NetwithExistingCNNArchitectures
Although conventional CNN architectures, such as ResNet, AlexNet, VGG, and
GoogleNet,havedemonstratedsuperiorperformanceincomputervisiontasks,theyare
nottypicallydesignedandoptimizedforlow-dimensionaltabulardatasuchasRFMinputs.
Thesemodelsareoftenoverparameterizedfortaskslikecustomersegmentclassification,
leadingtooverfitting,longertrainingtimes,andtheneedforextensivecomputationalre-
sources. ThekeyadvantagesofRFM-Netoverthesemodelscanbesummarizedasfollows:
LightweightandFast: ThearchitectureofRFM-Netisrelativelyshallow,consistingof
onlyafewlayersandaminimalnumberofparameters. Thislightweightdesignensures
highcomputationalefficiency,enablingthemodeltobeparticularlywell-suitedforreal-
timeinferenceanddeploymentinresource-constrainedenvironments.
https://doi.org/10.3390/app16052223

Appl.Sci.2026,16,2223 14of28
TailoredforTabularData: Unlikeimage-centricCNNs,RFM-Netisspecificallyde-
signed to work with structured data, preserving the semantic relationships between
RFMfeatures.
OverfittingPrevention:Deepermodels,suchasVGG-16orResNet-50,maybeproneto
overfittingwhenappliedtolow-dimensionaldata. RFM-Netaddressesthisissuethrough
itsarchitecturalsimplicityandpoolingmechanism.
Interpretability: ThecompactarchitectureofRFM-Netprovidesbetterinterpretability
than that of deeper and black-box models. This enables easier interpretation and de-
bugging,whichiscrucialincustomerbehavioranalysisforbusinessapplicationswhen
understandingmodeldecisions.
End-to-End Learning: By combining feature extraction and classification within a
unifiedframework,RFM-Neteliminatestheneedforseparateclusteringalgorithms. This
end-to-endframeworksimplifiesthesegmentationpipelineandimprovesscalability.
4. ExperimentalStudies
4.1. DatasetDescription
Inthisstudy,weutilizedthepubliclyavailable“OnlineRetail”dataset[20],whichwas
obtainedfromtheUCIMachineLearningRepository. Itisarichmultivariatetime-series
datasetcomprising541,909recordsand8variables,collectedfromaUK-basednon-store
onlineretailcompany. Thecompanyprimarilysellsuniqueall-occasiongifts,including
itemssuchasceramichomeware,scentedcandles,noveltymugs,children’scrafts,seasonal
decorations,andstationery. Theseproductsaretypicallylow-priced,decorativeandoften
purchasedinbulkbywholesalersforresaleingiftshopsorboutiquestores.Thetransactions
inthedatasetspanoveraone-yearperiod,from1December2010to9December2011. The
datasetcapturescustomerpurchasebehavioracross37differentcountries,includingthe
UnitedKingdom,Japan,theUnitedStates,Australia,theNetherlands,France,Italy,Spain,
Germany,Canada,andseveralothercountries. Duetoitssequentialnatureandtemporal
granularity,thedatasetiswell-suitedforcustomersegmentation,marketbasketanalysis,
anomalydetection,demandforecasting,andcustomerlifetimevalueestimation.
Table4presentsastructuraloverviewofthedataset,includingvariablenames,data
types, brief descriptions, and indications of missing values. Each record corresponds
to a line item in an invoice, meaning that a single invoice may have multiple rows cor-
responding to multiple products purchased in that transaction. Notably, the variables
Description,Country,andCustomerIDcontainmissingdata,whichmustbeaddressed
duringpreprocessingforanysegmentationandmodelingtasks.
Table4.Thecharacteristicsofthe“OnlineRetail”dataset.
Missing
VariableName Type Description
Value
CustomerID Categorical Afive-digitnumericalIDuniquelygiventoeachcustomer Yes
InvoiceNo Categorical Asix-digitintegernumberuniquelygiventoeachindividualtransaction No
InvoiceDate Date Thetimestampwhenthetransactionoccurred No
StockCode Categorical Afive-digitnumericidentifieruniquelygiventoeachuniqueproduct No
Description Categorical Thenamedescribingtheproduct Yes
Quantity Integer Thecountofunitsforanitemwithinasingletransaction No
UnitPrice Real Thepricechargedforoneunitoftheproductinsterling No
Country Categorical Thecountrywhereeachcustomerresides Yes
A sample of the dataset is shown in Table 5. Each row in the table represents an
individualproductitemwithinacustomerinvoice. Asseeninthetable,customersoften
purchase multiple items in a single order. For instance, invoice 536608 includes three
https://doi.org/10.3390/app16052223

Appl.Sci.2026,16,2223 15of28
differentitemspurchasedbycustomer12855on2December2010. Repeatedpurchases
ofthesameproduct(e.g.,stockcode=16014)acrossdifferentinvoicesanddatesindicate
recurring demand for specific products in varying quantities. The sample also reflects
temporaldiversityintransactions,offeringinsightintocustomeractivityacrossvarious
pointsintimethroughouttheyear. Overall,theinclusionofbothcustomer-andproduct-
level details enables a wide range of analyses on customer behavior, sales trends, and
productperformance.
Table5.Asamplefromthe“OnlineRetail”dataset.
Invoice Stock Invoice Unit Customer
Description Quantity Country
No Code Date Price ID
536608 22863 Soapdishbrocante 6 12/2/201009:37 2.95 12855 UK
536608 22962 Jamjarwithpinklid 12 12/2/201009:37 0.85 12855 UK
536608 22963 Jamjarwithgreenlid 12 12/2/201009:37 0.85 12855 UK
537841 16014 SmallChinesestylescissor 1000 12/8/201015:10 0.32 13848 UK
543991 16014 SmallChinesestylescissor 1500 02/15/201110:17 0.32 13848 UK
543991 16015 MediumChinesestylescissor 100 02/15/201110:17 0.5 13848 UK
543991 16016 LargeChinesestylescissor 100 02/15/201110:17 0.85 13848 UK
566028 16014 SmallChinesestylescissor 1000 09/08/201112:58 0.32 13848 UK
549020 84879 Assortedcolourbirdornament 160 04/05/201115:36 1.45 13525 UK
549020 72801C 4rosepinkdinnercandles 48 04/05/201115:36 1.06 13525 UK
578785 84879 Assortedcolourbirdornament 160 11/25/201112:01 1.45 13525 UK
578785 22622 Boxofvintagealphabetblocks 2 11/25/201112:01 11.95 13525 UK
578785 23395 BelleJardinierecushioncover 12 11/25/201112:01 3.75 13525 UK
578785 23396 LeJardinbotaniquecushioncover 12 11/25/201112:01 3.75 13525 UK
Priortoanalysis,aseriesofdatapreprocessingstepswasperformedtoensureana-
lyticalrobustnessandrelevance. Theinitialphaseinvolvedselectingonlythevariables
essentialforRFManalysis. Supplementaryfieldssuchasproductcodesandnamesand
countrywereomitted,astheywerenotdirectlyrelevanttotheRFMframeworkandwould
contributetounnecessarycomplexity. Afterthat,recordslackingcustomeridentification
wereexcludedtoaddressdataincompleteness, astheycouldnotbelinkedtoanyuser
behavior.Anothercriticalstepinvolvesremovingreturntransactionsthatarenotassociated
withacorrespondingsalesrecord. Inotherwords,transactionswhoseinvoicenumbers
wereprefixedwiththeletter‘C’wereeliminatediftheydidnotcorrespondtoanoriginal
purchase. Additionally,contextuallyirrelevantentriessuchasbankcharges,postage,and
giftcardswereexcludedtomoreaccuratelyreflectactualcustomerpurchasebehavior.
Followingdatacleaning,customer-levelmetricswerecomputed: recencywascalcu-
lated as the number of days since the most recent purchase of the customer; frequency
capturedthetotalnumberofdistinctpurchases;andmonetaryvaluewasderivedbyaggre-
gatingtotalspendingacrossallinvoicesofthecustomer. Eachindividualcustomerwas
thenassigneddiscreteR,F,andMscoresbasedontheuser-definedthresholdvalues.Specif-
ically,recencywassegmentedusingthebins[10,30,50,150],whilemonetaryvalueswere
dividedaccordingtothebins[500,1500,2500,5000]. Giventhehighdensityofone-time
visitors,frequencyvalueswerescoredusingaspecializedbinningstrategyof[1,2,4,6].
Underthisscheme,thecustomerswithafrequencyscoreof1wereassignedtocategory1,
thosewithascoreof2wereplacedincategory2,thosewithscoresof3and4wereclassified
intocategory3, customersthathavethefrequencyvalues5and6weregroupedunder
category4,andthosewithafrequencyvaluehigherthan6wereincludedincategory5.
Thesethresholdsweredeterminedthroughanexploratoryanalysisanditerativeempirical
experimentation,consideringthedatadistributions,domainknowledge,andtheresulting
classificationaccuracyacrossmultipletrials. Finally, arule-basedclassificationscheme
https://doi.org/10.3390/app16052223

Appl.Sci.2026,16,2223 16of28
wasappliedtotheresultingRFMscorestoannotateeachcustomerwithacorresponding
behavioralsegmentlabel.
Table 6 illustrates a labeled dataset resulting from an RFM analysis, where each
customerhasbeenannotatedwithacorrespondingsegmentcategory(e.g.,‘Champions’,
‘Hibernating’)basedontheirpurchasingbehavior. Sincemultiplerowsmaycorrespondto
asingleinvoiceandeachcustomermayhavemultipleinvoicesovertime,therawdataare
aggregatedforcustomer-levelandinvoice-levelanalysis. Forinstance,asshowninTable5,
customer 13848 made three separate purchases at different times. These transactions
includedvaryingquantitiesandtypesofproducts,withatotalmonetaryvalueof£1255,a
frequencyof3purchases,andarecencyvalueof92daysfromthemostrecentpurchase
tothereferencedate. Basedonthisaggregateddata,RFMscoresareassignedaccording
to the user-defined thresholds. For CustomerID 13848, the resulting RFM score is 232,
indicatingrelativelylowrecency,moderatefrequency,andlowmonetaryvalue. According
topredefinedsegmentationrules,thiscustomerfallsintothe“NeedAttention”segment. In
short,theRFManalysistransformsrawsalesrecordsintointerpretablecustomersegments,
whichserveaslabelsfortheclassificationtask.
Table6.AsamplecustomersegmentsbasedonRFMmethodology.
CustomerID Recency Frequency Monetary R-Score F-Score M-Score RFM-Score CustomerSegment
13525 14 2 628.78 4 2 2 422 PotentialLoyalists
13848 92 3 1255 2 3 2 232 NeedAttention
12855 372 1 38.1 1 1 1 111 Hibernating
13089 2 118 57,385.88 5 5 5 555 Champions
17203 35 6 3563.85 3 4 4 344 LoyalCustomers
13194 135 1 60.7 2 1 1 211 AbouttoSleep
15332 366 4 1661.06 1 3 3 133 AtRisk
Figure3illustratesthedistributionofcustomersegments,showingtheproportion
of each group within the overall customer base. The largest portion of the customers
(23.70%)fallsunderthe“PotentialLoyalists”category,indicatingasignificantnumberof
recentbuyerswhohavethepotentialtobecomelong-termloyalusers. Thisisfollowedby
“LoyalCustomers”at18.28%,representingakeygroupofrepeatpurchasers. Meanwhile,
“Hibernating”customersaccountfor17.39%,reflectingasubstantialportionofinactiveand
low-engagementusers. Champions,themostvaluableandengagedcustomers,account
for 14.46%, while “About to Sleep” and “Need Attention” make up 11.30% and 8.51%,
respectively.Lastly,the“AtRisk”grouprepresents6.36%ofthecustomerbase,highlighting
asmallerbutstillimportantgroupwithdecliningactivity. Thisdistributionofferscritical
insightsintocustomerbehavior,enablingmoreeffectivetargetedefforts,fromsupporting
high-potentialsegmentstore-engagingthoseatriskofchurn.
Figure 4 illustrates the outcome of the permutation feature importance analysis, a
widelyusedtechniqueinmachinelearningforassessingtherelativecontributionofeach
inputfeaturetothepredictiveaccuracyofthemodel. Theprimaryobjectiveofthisanalysis
istodisrupttherelationshipbetweenthetargetvariableandagivenfeaturebyrandomly
permuting the feature’s values and then observing how the model’s performance dete-
riorates as a result. A greater drop in performance signifies a more important feature.
Accordingtotheresultspresented,Recencywasidentifiedasthemostimpactfulvariable,
withanimportancescoreof0.5358,indicatingthatthetimesinceacustomer’slastpurchase
playsasignificantroleinthedecision-makingprocess. Thishighvaluesuggeststhatthe
predictionishighlysensitivetotemporaldata,specificallyservingastheprimarysignal
fordistinguishingbetweenactiveandchurnedstates. Frequencywasrankedasthesecond
mostimportantvariable,withascoreof0.4217,suggestingthatthenumberofpurchasesis
https://doi.org/10.3390/app16052223

Appl.Sci.2026,16,2223 17of28
alsoastrongpredictor. Thisindicatesthatthemodelreliesontherepetitionofpurchase
behaviortoestablishpatternsofloyalty,implyingthat‘howoften’acustomerreturnsis
nearlyasvitalas‘when’theylastvisited. Monetarywasidentifiedastheleastimportant
amongthethreevariables,withascoreof0.2642,indicatingthatspendinglevelsarealso
relevantbutplayacomparativelysmallerroleinthepredictionprocess. Thehierarchical
importanceoftheRFMvariables(R>F>M)alignscloselywiththeChurnPrediction(CP)
inthecustomeranalyticsdomain,wherethe‘recency’ofanactionisoftenthestrongest
indicatoroffutureengagement. Furthermore,thisorderingalsoalignswiththeCustomer
LifetimeValue(CLV)framework,whererecencyandfrequencyaretypicallystrongerpre-
dictorsoffuturecashflowsthanmonetaryvaluealone,reflectingwell-establishedpatterns
observedindomainknowledge.
Figure3.Distributionofcustomersegments.
Figure4.Featureimportanceanalysis.
4.2. ExperimentalSetup
The proposed method was implemented in Python (version 3.12) using various li-
braries,includingTensorFlow(version2.20.0),NumPy(version2.0),Pandas(version2.0),
Scikit-Learn(version1.8.0),Seaborn(version0.13.0),andMatplotlib(version3.9.0). We
employeda10-foldcross-validationproceduretoassesstherobustnessandgeneralization
capabilityoftheproposedmodelwhileavoidingdataleakage. Inthisprocess,theentire
datasetwasrandomlydividedinto10equal-sizedandnon-overlappingsubsets(folds). In
eachround,onefold(10%oftheentiredata)washeldoutasanindependenttestset,while
theremainingninefoldsconstitutedthedevelopmentset. Thedevelopmentsetwasfurther
splitintotrainingandvalidationsubsetsusingan8:1ratio,correspondingto80%training
and10%validationdatawithrespecttothefulldataset. Thetrainingsubsetwasusedfor
modelfitting,whilethevalidationsubsetwasusedtomonitortraining(i.e.,earlystopping).
Thetestfoldwasusedsolelyforperformanceevaluation,neverinvolvedintrainingor
validation,ensuringthatnoinformationleakageoccurred. Thisprocedureisperformed
10times,witheachfoldactingasthetestdataexactlyonce. Thefinalperformanceisthen
https://doi.org/10.3390/app16052223

Appl.Sci.2026,16,2223
18of28
calculatedbyaveragingtheresultsacrossallfolds,providingacomprehensiveandreliable
evaluationofthemodel.
Hyperparameteranalysiswasconductedasaseparatesetofexperiments. Foreach
hyperparameterconfiguration(e.g.,numberofconvolutionallayers,learningrate,number
offilters, andnumberoffolds), theentire10-foldcross-validationproceduredescribed
abovewasexecutedindependently.Similarly,RFMthresholdingwascomputedbyrunning
thecompleteevaluationprocessforeachdifferentconfiguration. Thepreprocessingsteps
werefittedonthetrainingdataandthenappliedtothecorrespondingvalidationandtest
sets. Theapproachensuresthatpreprocessingandthresholdingarealwaysbasedsolelyon
thetrainingdata,preventinganydistributionleakage. Performancemetricswereaveraged
acrossfoldsforeachconfiguration,andcomparisonsweremadebetweenconfigurations
basedontheseaveragedresults.
Various assessment metrics were used to evaluate how well the model classifies
customersintothecorrectsegments. Thesemetricsincludeaccuracy—Equation(7)—which
measures the proportion of correct predictions, as well as precision, recall, and the F-
measure—Equations(8)–(10)—whichprovidemorenuancedinsightsintohowwellthe
model performs across different segment classes. The metrics were computed for the
multi-classclassificationtaskusingweightedaveraging. Specifically,class-wiseaccuracy,
precision(P),recall(R),andF-measurevalueswerefirstcalculated,andthefinalreported
i i
metricswereobtainedastheweightedaverageacrossclasses,whereweightscorrespond
to the number of samples in each class. This approach accounts for the possible class
imbalanceinsegmentcounts.
L
|     |          |              |     | 1∑  | TP   | +TN     |     |
| --- | -------- | ------------ | --- | --- | ---- | ------- | --- |
|     | Weighted | Accuracy(WA) | =   | n ∗ |      | i i     | (7) |
|     |          |              |     | i   | +TN  | +FP +FN |     |
|     |          |              |     | n   | TP i | i i i   |     |
i=1
|     |     |                       |     | 1∑  | L   | TP  |     |
| --- | --- | --------------------- | --- | --- | --- | --- | --- |
|     |     | WeightedPrecision(WP) |     | =   | ∗   | i   |     |
|     |     |                       |     |     | n i |     | (8) |
|     |     |                       |     | n   | TP  | +FP |     |
|     |     |                       |     |     | i=1 | i i |     |
L
|     |     |                      |      | 1∑  |      | TP i   |      |
| --- | --- | -------------------- | ---- | --- | ---- | ------ | ---- |
|     |     | WeightedRecall       | (WR) | =   | n ∗  |        | (9)  |
|     |     |                      |      | n   | i TP | +FN    |      |
|     |     |                      |      | i=1 |      | i i    |      |
|     |     |                      |      | 1∑  | L    | 2∗P ∗R |      |
|     |     | WeightedFmeasure(WF) |      | =   | n ∗  | i i    | (10) |
i +R
|     |     |     |     | n   |     | P i i |     |
| --- | --- | --- | --- | --- | --- | ----- | --- |
i=1
Here,Listhenumberofclasslabels,n isthenumberofinstancesinclassi,whilenis
i
thetotalnumberofinstancesacrossallclasses. Intheseformulations,TruePositives(TP)
i
andTrueNegatives(TN )arecorrectpredictionsofpositiveandnegativecasesforclassi,
i
| respectively,whileFalseNegatives(FN |     |     | i )andFalsePositives(FP)areincorrectpredictions |     |     | i   |     |
| ----------------------------------- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- |
wherethemodelmisclassifiesnegativecasesaspositiveandpositivecasesasnegative. A
confusionmatrixwasalsogeneratedtovisualizewhichsegmentsareoftenconfusedwith
others,offeringopportunitiesformodelimprovement.
4.3. Results
Table7presentstheperformanceoftheclassificationmodelobtainedfroma10-fold
cross-validation using four key evaluation metrics: Accuracy, Recall, Precision, and F-
Measure. Theresultsdemonstratedthatthemodeldeliveredrobustoutcomes,withaccu-
racyvaluesrangingfrom90.78%to97.23%. Onaverage,themodelachievedanaccuracy
of 94.33%. Precision and recall values closely follow this accuracy trend, reflecting the
stronggeneralizabilityofthemodel. Theseoutcomesindicatethattheclassifierisnotonly
accuratebutalsomaintainsastrongbalancebetweensensitivityandspecificity.
https://doi.org/10.3390/app16052223

Appl.Sci.2026,16,2223
19of28
Table7.PerformanceresultsoftheproposedRFM-Netmethodacrossallfolds.
| Fold | Accuracy(%) | Precision | Recall | F-Measure |
| ---- | ----------- | --------- | ------ | --------- |
| 1    | 93.55       | 0.9379    | 0.9355 | 0.9354    |
| 2    | 95.85       | 0.9599    | 0.9585 | 0.9585    |
| 3    | 93.32       | 0.9381    | 0.9332 | 0.9334    |
| 4    | 95.16       | 0.9533    | 0.9516 | 0.9517    |
| 5    | 93.78       | 0.9446    | 0.9378 | 0.9383    |
| 6    | 90.78       | 0.9154    | 0.9078 | 0.9065    |
| 7    | 93.55       | 0.9396    | 0.9355 | 0.9341    |
| 8    | 97.00       | 0.9706    | 0.9700 | 0.9701    |
| 9    | 97.23       | 0.9728    | 0.9723 | 0.9723    |
| 10   | 93.07       | 0.9335    | 0.9307 | 0.9288    |
| Avg. | 94.33       | 0.9466    | 0.9433 | 0.9429    |
Figure5presentstheconfusionmatrix,whichshowstheperformanceoftheclassifica-
tionmodelacrossdifferentclasses. Themodeldemonstratednotablyhighclassification
accuracies in customer categories. For instance, the “Champions” group was correctly
classifiedatarateof94.3%,withonly5.7%ofinstancesmisclassified. Similarly,the“Need
Attention” category showed strong performance with 90.5% accuracy. The model per-
formedparticularlywellinidentifying“PotentialLoyalists”(96.9%)and“AbouttoSleep”
customers (93.7%), with minor misclassifications distributed across adjacent segments.
Overall, the matrix indicates that the classification model is effective in distinguishing
betweencustomersegments.
Figure5.Confusionmatrix.
Figure6illustratesthetrainingandvalidationlossvaluesover20epochs,indicatinga
consistentimprovementinmodelperformance. Bothofthemdecreasesubstantially,with
thetraininglossdroppingfrom0.6024to0.1549andthevalidationlossdecreasingfrom
0.3792to0.1502. Thistrendreflectseffectivelearningandgeneralization. Notably,from
epoch15onward,thelossesbecomecloselyaligned,meaningthatthemodelhasreacheda
stablelearningphase. Thedecreasinggapbetweentrainingandvalidationlosstowardthe
finalepochsfurthersupportsthemodel’srobustnessanditsabilitytogeneralizewellon
unseendata.
https://doi.org/10.3390/app16052223

Appl.Sci.2026,16,2223 20of28
Figure6.Training—validationloss.
4.4. SensitivityAnalysis
Table8presentstheresultsofthesensitivityanalysisconductedtoevaluatetheimpact
of key hyperparameters on the proposed model performance. This analysis involved
systematictestingofmultiplevaluesforeachparameter. Forthenumberofconvolutional
layers,thesensitivityanalysisexploredvaluesrangingfrom2to7.Thehighestperformance
wasobservedwithtwolayers,yieldinganaccuracyof94.33%. Asthenumberoflayers
increased,performanceconsistentlydeclined,likelyduetooverfittingorredundantfeature
extraction. Thelearningratewasalsotestedacrossarangeofvalues: 0.04,0.03,0.02,and
0.01. Amongthese,alearningrateof0.01achievedpeakperformanceinallmetrics. Higher
learning rates negatively impacted model performance, possibly due to overshooting
duringtheoptimizationprocess. FortheK-FoldCrossValidation,using10foldsproduced
bettergeneralizationcomparedto5folds,demonstratingtheadvantagesofamorethorough
validationapproach.Furthermore,afiltersizeof32wasfoundtobeoptimal,offeringhigher
accuracycomparedto16filters. Itdemonstratesthatthemodelissensitivetofiltersize,
suggestingthatahighernumberoffilterscanenhancefeatureextractionwithoutoverfitting.
Finally,ananalysiswasconductedtoexaminetheimpactofdifferentuser-definedRFM
thresholdvaluesonmodelperformance. Toprovideacomprehensiveevaluation,various
distinctthresholdconfigurations,rangingfromtightertobroaderintervals,weretestedto
determinetheoptimaldiscretizationstrategy. TheprogressiveadjustmentofR,F,andM
rangesenabledadetailedexaminationofhowthresholdgranularityinfluencesclassification
stability. AsshowninTable8,broaderthresholdintervalsresultedinhigheraccuracyand
amorebalancedclassdistribution, betterreflectingunderlyingdifferencesincustomer
purchasingbehavior. Overall,alltheseresultsguidedtheselectionofhyperparameters
forthefinalmodelconfiguration: twoconvolutionallayers,alearningrateof0.01,10-fold
cross-validation,and32filters.
4.5. Discussion
Inthissection,theperformanceoftheproposedRFM-Netmethodisevaluatedcom-
parativelywiththeresultsreportedinpriorstudies[16,21–34]onthesamedataset. As
presentedinTable9,thecomparisonwasmadeusingcommonperformancemetrics,in-
cluding accuracy, recall, precision, and F-measure. According to the results, RFM-Net
providedaconsistentandsignificantperformanceadvantageoverallcomparedmethods
in terms of all evaluation criteria. On average, RFM-Net demonstrated a performance
increaseofapproximately13.17%inaccuracycomparedtotheresultsreportedinstate-
of-the-artstudies. Forinstance,theproposedmethodyieldedasuperiorresult(94.33%)
comparedtoadvancedmodels,suchasPARM(90.00%)[22]andRet-DNN(90.00%)[25]. In
https://doi.org/10.3390/app16052223

Appl.Sci.2026,16,2223
21of28
addition,RFM-NethasalsosurpassedensemblelearningmethodssuchasRandomForest
(87.60%) [16], Gradient Boosting (85.00%) [28], and AdaBoost (73.30%) [21]. Compared
tothesestudies,theRFM-Netmethodachievedthehighestresultsnotonlyintermsof
accuracybutalsoinallperformancemetrics,withaprecisionof0.9466,arecallof0.9433,
andanF-measureof0.9429. TheseresultsclearlydemonstratedRFM-Net’ssuperiorityin
processingonlineretaildata. AsshowninTable9,standardclassificationalgorithms,such
asKNN,DT,andSVM,aremorelimitedincapturingcomplexandnonlinearrelationships
intransactionaldatacomparedtoourdeeplearning-basedapproach. Insummary,RFM-
Net’sstrongperformancecomparedtootherstate-of-the-artstudiesvalidatedthemodel’s
abilitytodistinguishcriticalclasses.
Table8.SensitivityanalysisforRFM-Net(OnlineRetailIdataset).
|     | Accuracy(%) | Precision | Recall | F-Measure |
| --- | ----------- | --------- | ------ | --------- |
TheNumberofConvolutionLayers
| 2   | 94.33 | 0.9466 | 0.9433 | 0.9429 |
| --- | ----- | ------ | ------ | ------ |
| 3   | 93.47 | 0.9385 | 0.9347 | 0.9339 |
| 4   | 92.95 | 0.9349 | 0.9295 | 0.9283 |
| 5   | 92.51 | 0.9293 | 0.9251 | 0.9233 |
| 6   | 90.96 | 0.9161 | 0.9096 | 0.9075 |
| 7   | 90.85 | 0.9135 | 0.9085 | 0.9083 |
LearningRate
| 0.04 | 90.06 | 0.9080 | 0.9006 | 0.8986 |
| ---- | ----- | ------ | ------ | ------ |
| 0.03 | 92.05 | 0.9273 | 0.9205 | 0.9208 |
| 0.02 | 92.16 | 0.9274 | 0.9216 | 0.9209 |
| 0.01 | 94.33 | 0.9466 | 0.9433 | 0.9429 |
K-FoldCrossValidation
| 5   | 92.28 | 0.9306 | 0.9228 | 0.9219 |
| --- | ----- | ------ | ------ | ------ |
| 10  | 94.33 | 0.9466 | 0.9433 | 0.9429 |
Filter
| 16  | 93.75 | 0.9412 | 0.9375 | 0.9371 |
| --- | ----- | ------ | ------ | ------ |
| 32  | 94.33 | 0.9466 | 0.9433 | 0.9429 |
ThresholdValues
R[5,15,25,75]
| F[1,2,3,4] | 93.38 | 0.9382 | 0.9338 | 0.9338 |
| ---------- | ----- | ------ | ------ | ------ |
M[250,750,1250,2500]
R[6,18,30,90]
| F[1,2,3,6] | 93.38 | 0.9379 | 0.9338 | 0.9335 |
| ---------- | ----- | ------ | ------ | ------ |
M[300,900,1500,3000]
R[7,21,35,105]
| F[1,2,3,4] | 93.52 | 0.9396 | 0.9352 | 0.9343 |
| ---------- | ----- | ------ | ------ | ------ |
M[350,1050,1750,3500]
R[8,24,40,120]
| F[1,2,4,5] | 93.75 | 0.9415 | 0.9375 | 0.9368 |
| ---------- | ----- | ------ | ------ | ------ |
M[400,1200,2000,4000]
R[9,27,45,135]
| F[1,2,4,6] | 94.21 | 0.9442 | 0.9421 | 0.9417 |
| ---------- | ----- | ------ | ------ | ------ |
M[450,1350,2250,4500]
R[10,30,50,150]
| F[1,2,4,6] | 94.33 | 0.9466 | 0.9433 | 0.9429 |
| ---------- | ----- | ------ | ------ | ------ |
M[500,1500,2500,5000]
https://doi.org/10.3390/app16052223

Appl.Sci.2026,16,2223
22of28
Table9.ComparativeresultsofRFM-Netandpreviouslyreportedmethodsonthesamedataset.
| Ref. | Authors           | Year Method          |     | Accuracy | Precision | Recall | F-Measure |
| ---- | ----------------- | -------------------- | --- | -------- | --------- | ------ | --------- |
|      |                   | XGBoost              |     | 92.10    | 0.9170    | 0.8990 | 0.9080    |
| [11] | Devietal.         | 2025                 |     |          |           |        |           |
|      |                   | RF                   |     | 87.60    | 0.8620    | 0.8350 | 0.8480    |
|      |                   | LR                   |     | 70.40    | 0.7000    | 0.6950 | 0.7000    |
|      |                   | KNN                  |     | 72.10    | 0.7300    | 0.7100 | 0.7100    |
|      |                   | SVM                  |     | 73.20    | 0.7450    | 0.7200 | 0.7200    |
| [21] |                   | 2025                 |     |          |           |        |           |
|      | Vermaetal.        | DT                   |     | 74.20    | 0.7400    | 0.7350 | 0.7400    |
|      |                   | RF                   |     | 72.80    | 0.7400    | 0.7150 | 0.7150    |
|      |                   | AdaBoost             |     | 73.30    | 0.7450    | 0.7200 | 0.7200    |
|      |                   | XGBoost              |     | 73.90    | 0.7450    | 0.7500 | 0.7200    |
| [22] | Mohantyetal.      | 2025 PARM            |     | 90.00    | 0.8480    | 0.8000 | 0.8230    |
|      |                   | OptimizedBP          |     | 87.30    | 0.8860    | -      | -         |
| [23] | Lv                | 2025 SVM             |     | 78.90    | 0.8010    | -      | -         |
|      |                   | RF                   |     | 84.50    | 0.8580    | -      | -         |
| [24] | HussainJafrietal. | 2025 ESReLUAF        |     | 76.00    | -         | -      | -         |
| [25] | Rudroetal.        | 2025 Ret-DNN         |     | 90.00    | -         | -      | -         |
|      |                   | Tuned_XGB_ADASYN     |     | -        | -         | -      | 0.8000    |
| [34] | Imanietal.        | 2025                 |     |          |           |        |           |
|      |                   | Tuned_XGB_SMOTE      |     | -        | -         | -      | 0.9200    |
| [13] | Mirzaeeetal.      | 2024 LSTM-RNN        |     | 92.55    | 0.9285    | 0.9002 | 0.9111    |
|      |                   | BaselineModel        |     | -        | 0.8500    | 0.8500 | 0.8500    |
|      |                   | (SDG)DiffusionModels |     | -        | 0.9000    | 0.9000 | 0.9000    |
Pushkarenkoand
| [26] |     | 2024 SMOTE |     | -   | 0.8800 | 0.8800 | 0.8800 |
| ---- | --- | ---------- | --- | --- | ------ | ------ | ------ |
Zaslavskyi
|      |              | ADASYN                  |     | -     | 0.8900 | 0.8900 | 0.8900 |
| ---- | ------------ | ----------------------- | --- | ----- | ------ | ------ | ------ |
|      |              | Borderline-SMOTE        |     | -     | 0.8700 | 0.8700 | 0.8700 |
|      |              | LR                      |     | 93.42 | -      | -      | -      |
| [27] | Lalithaetal. | 2024 RF(Estimators=150) |     | 86.57 | -      | -      | -      |
|      |              | KNNRegression(k=3)      |     | 78.82 | -      | -      | -      |
| [28] | Asfietal.    | 2024 GBM                |     | 85.00 | 0.7800 | 0.8000 | -      |
| [29] | XuandHu      | 2023 DAPT→TAPT          |     | 74.20 | 0.7450 | 0.7280 | 0.7390 |
|      |              | SVM                     |     | -     | 0.6292 | -      | -      |
|      |              | LR                      |     | -     | 0.7268 | -      | -      |
|      |              | KNN                     |     | -     | 0.6778 | -      | -      |
| [30] | Mustafaetal. | 2023 DT                 |     | -     | 0.7327 | -      | -      |
|      |              | RF                      |     | -     | 0.7593 | -      | -      |
|      |              | AdaBoost                |     | -     | 0.7021 | -      | -      |
|      |              | GradientBoosting        |     | -     | 0.7605 | -      | -      |
|      |              | CollaborativeFiltering  |     | -     | 0.8500 | 0.7500 | 0.7900 |
[31] Loukilietal. 2023 Content-BasedFiltering - 0.7800 0.6600 0.7100
|          |                  | HybridFiltering |         | -     | 0.8200 | 0.7200 | 0.7600 |
| -------- | ---------------- | --------------- | ------- | ----- | ------ | ------ | ------ |
|          |                  | DT              |         | 77.00 | 0.7700 | 0.7700 | 0.7700 |
| [32]     | AlrawiandAjlouni | 2022            |         |       |        |        |        |
|          |                  | RF              |         | 80.00 | 0.7900 | 0.8000 | 0.7900 |
| [33]     | Jana             | 2020 LR         |         | 84.00 | 0.8600 | 0.7800 | 0.8200 |
|          |                  |                 | Average | 81.16 | 0.7947 | 0.7866 | 0.8002 |
| Proposed |                  | RFM-Net         |         | 94.33 | 0.9466 | 0.9433 | 0.9429 |
Table10presentstheperformancecomparisonbetweentheproposedRFM-Netand
severalbaselinemodels,includinglogisticregression(LR),naiveBayes,multi-layerpercep-
tron(MLP),k-nearestneighbors,AdaBoost,decisiontree(DT),andatree-basedensemble
https://doi.org/10.3390/app16052223

Appl.Sci.2026,16,2223
23of28
method(Bagging(DT)).Allmodelswereevaluatedunderthesameexperimentalproto-
col (identical preprocessing, RFM thresholds, and segment definitions) to ensure a fair
comparison. TheresultsdemonstratedthatRFM-Netoutperformedallbaselinemodels
acrossallevaluatedmetrics. Forinstance,whiletheMLPobtainedanaccuracyof85.50%,
RFM-Net reached a substantially higher accuracy of 94.33%. Similarly, LR yielded an
accuracyof90.32%,whichremainslowerthantheaccuracyobtainedbyRFM-Net. The
tree-basedensembleapproach,Bagging(DT),deliveredanaccuracyof90.68%,confirming
thestrengthofensemble-basedmodeling, yetremainingbelowtheresultsachievedby
RFM-Net. Specifically,RFM-Netimprovedaccuracyby6.31percentagepointscomparedto
theaveragebaselineperformance(88.02%). Theseresultsdemonstratetheeffectiveness
oftheproposedCNN-basedarchitectureinmodelingtheRFMfeatureinteractionsand
improvingclassificationperformance.
Table10.PerformancecomparisonofRFM-Netagainstbaselinemachinelearningmodels.
| Method                |         | Accuracy(%) | Precision | Recall | F-Measure |
| --------------------- | ------- | ----------- | --------- | ------ | --------- |
| LogisticRegression    |         | 90.32       | 0.9030    | 0.9030 | 0.9030    |
| NaiveBayes            |         | 76.46       | 0.7850    | 0.7650 | 0.7530    |
| Multi-LayerPerceptron |         | 85.50       | 0.8560    | 0.8550 | 0.8520    |
| K-NearestNeighbors    |         | 92.39       | 0.9240    | 0.9240 | 0.9230    |
| AdaBoost              |         | 91.72       | 0.9170    | 0.9170 | 0.9170    |
| DecisionTree(DT)      |         | 89.07       | 0.8950    | 0.8910 | 0.8900    |
| Bagging(DT)           |         | 90.68       | 0.9120    | 0.9070 | 0.9060    |
|                       | Average | 88.02       | 0.8846    | 0.8803 | 0.8777    |
| RFM-Net(proposed)     |         | 94.33       | 0.9466    | 0.9433 | 0.9429    |
Althoughtheinputconsistsofonlythreestructuredfeatures(R,F,andM),thecon-
volutionalarchitecturecanprovideadvantagesinlearninglocalizedinteractionpatterns
betweenthesefeatures. InsteadoftreatingR,F,andMasfullyindependentvariables,the
convolutionalfiltersactasfeatureinteractionextractors,capturinglocaldependencystruc-
turesandnonlinearcombinationsmoreeffectivelythansolelyglobalweightupdatesina
standardMLP.Furthermore,thepoolingmechanismenhancesrobustnessbyemphasizing
dominantinteractionpatternswhilereducingsensitivitytonoise. Comparedtotraditional
models such as Regression, which usually assume linearity in their feature space, and
tree-basedmethodsthatrelyonhierarchicalsplits,theshared-filtermechanismoftheCNN
actsasanimplicitregularizer,whichimprovesgeneralizationperformance.
To further strengthen the validity and generalizability of the proposed RFM-Net
approach,anadditionaldatasetwasincorporatedintotheexperimentalevaluation. The
publiclyavailableOnlineRetailII[35]dataset,containing1,067,371real-worldtransactional
recordsfromaUK-basednon-storeonlineretailerspanningtwoyears(2009–2011),was
utilized. Thesamepreprocessingmethodologyandevaluationmetricswereemployed
to ensure consistency with the primary dataset. In the sensitivity analysis, the same
hyperparameterconfigurationsweresystematicallyexamined,exceptforthresholdvalues,
whichweredoubledbecausethedatasetsizewasalsotwicethatofthemaindataset. The
resultsarepresentedinTable11. Consistentwiththefindingsfromtheprimarydataset,
thebestperformancewasachievedusingashallowconvolutionalarchitecture(2layers)
andalowerlearningrate(0.01),whereasdeeperconfigurationsresultedinperformance
degradation. Similarly,ahigherfiltercapacity(32)andbroaderRFMthresholdintervals
ledtoimprovedclassification,achievinganaccuracyof95.41%. Thesefindingsconfirmed
that the proposed RFM-Net model maintained strong performance on large-scale, real-
https://doi.org/10.3390/app16052223

Appl.Sci.2026,16,2223
24of28
worldtransactionaldata. Theconsistencyofresultsacrossdatasetsfurthersupportsthe
robustnessandgeneralizabilityoftheproposedsegmentationapproach.
Table11.SensitivityanalysisforRFM-Net(OnlineRetailIIdataset).
|     | Accuracy(%) | Precision | Recall | F-Measure |
| --- | ----------- | --------- | ------ | --------- |
TheNumberofConvolutionLayers
| 2   | 95.41 | 0.9563 | 0.9541 | 0.9541 |
| --- | ----- | ------ | ------ | ------ |
| 3   | 95.33 | 0.9552 | 0.9533 | 0.9532 |
| 4   | 93.71 | 0.9446 | 0.9371 | 0.9327 |
| 5   | 92.16 | 0.9191 | 0.9216 | 0.9163 |
| 6   | 91.90 | 0.9258 | 0.9190 | 0.9177 |
| 7   | 85.51 | 0.8698 | 0.8551 | 0.8500 |
LearningRate
| 0.04 | 92.34 | 0.9314 | 0.9234 | 0.9235 |
| ---- | ----- | ------ | ------ | ------ |
| 0.03 | 93.88 | 0.9440 | 0.9388 | 0.9388 |
| 0.02 | 94.20 | 0.9464 | 0.9420 | 0.9420 |
| 0.01 | 95.41 | 0.9563 | 0.9541 | 0.9541 |
K-FoldCrossValidation
| 5   | 94.80 | 0.9508 | 0.9480 | 0.9478 |
| --- | ----- | ------ | ------ | ------ |
| 10  | 95.41 | 0.9563 | 0.9541 | 0.9541 |
Filter
| 16  | 94.95 | 0.9522 | 0.9495 | 0.9493 |
| --- | ----- | ------ | ------ | ------ |
| 32  | 95.41 | 0.9563 | 0.9541 | 0.9541 |
ThresholdValues
R[10,30,50,150]
| F[1,2,4,6] | 93.44 | 0.9378 | 0.9344 | 0.9334 |
| ---------- | ----- | ------ | ------ | ------ |
M[500,1500,2500,5000]
R[12,36,60,180]
| F[1,2,4,6] | 93.83 | 0.9432 | 0.9383 | 0.9377 |
| ---------- | ----- | ------ | ------ | ------ |
M[600,1800,3000,6000]
R[14,42,70,210]
| F[1,2,4,6] | 94.00 | 0.9438 | 0.9400 | 0.9399 |
| ---------- | ----- | ------ | ------ | ------ |
M[700,2100,3500,7000]
R[16,48,80,240]
| F[1,2,4,6] | 94.46 | 0.9479 | 0.9446 | 0.9439 |
| ---------- | ----- | ------ | ------ | ------ |
M[800,2400,4000,8000]
R[18,54,90,270]
| F[1,2,4,6] | 95.23 | 0.9559 | 0.9523 | 0.9525 |
| ---------- | ----- | ------ | ------ | ------ |
M[900,2700,4500,9000]
R[20,60,100,300]
| F[1,2,4,6] | 95.41 | 0.9563 | 0.9541 | 0.9541 |
| ---------- | ----- | ------ | ------ | ------ |
M[1000,3000,5000,10000]
Onelimitationofthisstudyisthatcustomersegmentlabelsaregeneratedfromprede-
finedRFMrulesandsubsequentlyusedasgroundtruthfortrainingtheCNN,introducing
adegreeofcircularity. However,althoughcustomersegments(labels)arederivedfrom
discreteRFMscores(1–5scale), theCNNmodelistrainedonrawdiscreteRFMvalues
topreservetheoriginalbehavioralmeasures. Theprimaryobjectiveofemployingadeep
learningarchitectureinthiscontextistocreateascalableframeworkcapableofsegmenting
customersaccurately. Whilesegmentationisconceptuallygroundedinrule-basedlogic
usingRFMscores,modeltrainingisperformedusingactualRFMvalues.
https://doi.org/10.3390/app16052223

Appl.Sci.2026,16,2223 25of28
5. ConclusionsandFutureWork
Thisstudypresentsadeep-learning-basedsupervisedcustomersegmentationframe-
worknamedRFM-Net. Intheproposedmethod,labelsaregeneratedthroughrule-based
logicderivedfromRFMscores. Themodel,therefore,learnsanexpert-definedmappingto
representcustomersegmentation. Thisapproachenablesorganizationstonotonlyunder-
standcustomerbehaviorbutalsomakedata-drivendecisionsforpersonalizedmarketing
andretentionstrategies. Unlikeconventionalclusteringorstatisticaltechniques,RFM-Net
effectively captures the complex and nonlinear patterns inherent in customer behavior,
providinganaccurateandactionableclassification.TheRFM-Netarchitectureisspecifically
designedtobelightweightandoptimizedforstructured,low-dimensionalinputs,allowing
forefficienttraining,stronggeneralization,andreducedoverfitting. Anexperimentaleval-
uationonareal-worlddatasetshowedthattheproposedmethodattainedaclassification
accuracy of 94.33%. Furthermore, RFM-Net demonstrated an average relative increase
of13.17%comparedtopreviouslyreportedresultsonthesamedataset. Thesefindings
underscoretheeffectivenessofcombiningRFMandCNNtechniquesindrivingintelligent
customersegmentclassificationsolutions.
Futureworkmayincludebuildingaweb/mobileinterfacefordeployingRFM-Net,
therebyenhancingitsusabilityinreal-worldbusinessscenarios. Suchaninterfacewould
enablebusinessanalyststouploadtransactionaldata,performanautomatedsegmentation
process,andvisualizetheresultsdynamicallyinadashboardwithoutrequiringtechnical
expertise. Implementingthisapplicationinacloud-basedplatformcouldenhanceitsac-
cessibility,scalability,andreal-timeinsights. Furthermore,extendingtheapplicationwith
featuressuchasreportgeneration,segmenttrackingovertime,notification-basedalerts,
and personalized campaign recommendations could significantly enhance its practical
valueinreal-worldenvironments. Inaddition,futureresearchmayfocusonimprovingthe
interpretabilityofRFM-NetbyintegratingposthocexplanationmethodssuchasSHAP[36]
andLIME[37],whichprovidefeature-levelandlocallyfaithfulexplanationsforindividual
segmentpredictions. Sincetheseapproachesprimarilyofferassociationalinsights,incorpo-
ratingcausalexplainableAIframeworks,particularlyFuzzyCognitiveMaps(FCMs)with
totalcausaleffectanalysis[38],couldfurtherenabletheidentificationofcausalrelationships
amongRFMvariablesandsupportmoreinformedstrategicdecision-making.
AuthorContributions:Conceptualization,K.F.B.andD.B.;methodology,K.F.B.andD.B.;software,
D.B.;validation,K.F.B.;formalanalysis,K.F.B.;investigation,K.F.B.;resources,K.F.B.;datacuration,
K.F.B.;writing—originaldraftpreparation,K.F.B.andD.B.;writing—reviewandediting,K.F.B.and
D.B.;visualization,D.B.;supervision,D.B.;projectadministration,D.B.;fundingacquisition,K.F.B.
Allauthorshavereadandagreedtothepublishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
InstitutionalReviewBoardStatement:Notapplicable.
InformedConsentStatement:Notapplicable.
Data Availability Statement: The “Online Retail” dataset [20] is publicly available in the UCI
(UniversityofCaliforniaIrvine)machinelearningrepository(https://archive.ics.uci.edu/dataset/
352/online+retail,accessedon1September2025). The“OnlineRetailII”dataset[35]ispublicly
availableintheUCI(UniversityofCaliforniaIrvine)machinelearningrepository(https://archive.
ics.uci.edu/dataset/502/online+retail+ii,accessedon6February2026).
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.
https://doi.org/10.3390/app16052223

Appl.Sci.2026,16,2223 26of28
Abbreviations
Thefollowingabbreviationsareusedinthismanuscript:
ADASYN Adaptivesyntheticsamplingapproach
AdaBoost Adaptiveboosting
AF Activationfunction
CART Classificationandregressiontrees
CNN Convolutionalneuralnetwork
DAPT Domainadaptivepretraining
DBSCAN Density-basedspatialclusteringofapplicationswithnoise
DT Decisiontree
ELUAF Exponentiallinearunitactivationfunction
ESReLUAF ExtendedsigmoidReLUactivationfunction
GBM Gradientboostingmachines
GNN Graphneuralnetwork
GNUS Gaussiannoiseupsampling
GRU Gatedrecurrentunits
KNN K-nearestneighbors
LeakyReLUAF Leakyrectifiedlinearunitactivationfunction
LR Logisticregression
LSTM Longshort-termmemory
MLP Multi-LayerPerceptron
NB NaiveBayes
OptimizedBP Optimizedbackpropagation
PARM Para-associationrulemining
RELUAF Rectifiedlinearunitactivationfunction
Ret-DNN Retail-deepneuralnetwork
RF Randomforest
RFM Recency,frequency,andmonetary
RFM-Net Recency-frequency-monetary-basedneuralnetwork
RNN Recurrentneuralnetworks
SMOTE Syntheticminorityover-samplingtechnique
SDG Syntheticdatageneration
SVM Supportvectormachine
SOM Self-organizingmap
Standingforspatial,temporal,payment,andproductcategoryintheprobability
STPC-PGM
graphicmodel
TAPT Taskadaptivepretraining
TARM Traditionalassociationrulemining
XGB Extremegradientboosting
References
1. Christy,A.J.;Umamakeswari,A.;Priyatharsini,L.;Neyaa,A.RFMranking—Aneffectiveapproachtocustomersegmentation.
J.KingSaud.Univ.Comput.Inf.Sci.2021,33,1251–1257.[CrossRef]
2. Ufeli,C.P.;Sattar,M.U.;Hasan,R.;Mahmood,S.EnhancingCustomerSegmentationThroughFactorAnalysisofMixedData
(FAMD)-BasedApproachUsingK-MeansandHierarchicalClusteringAlgorithms.Information2025,16,441.[CrossRef]
3. Yan,X.;Li,Y.;Nie,F.;Li,R.BankCustomerSegmentationandMarketingStrategiesBasedonImprovedDBSCANAlgorithm.
Appl.Sci.2025,15,3138.[CrossRef]
4. Madlenak,R.;Drozdziel,P.;Zysinska,M.;Madlenakova,L.ASystemsPerspectiveonCustomerSegmentationasaStrategicTool
forSustainableDevelopmentWithinSlovakia’sPostalMarket.Systems2025,13,701.[CrossRef]
5. Xiahou,X.;Harada,Y.B2CE-CommerceCustomerChurnPredictionBasedonK-MeansandSVM.J.Theor.Appl.Electron.Commer.
Res.2022,17,458–475.[CrossRef]
https://doi.org/10.3390/app16052223

Appl.Sci.2026,16,2223 27of28
6. Vrhovac,V.;Orošnjak,M.;Ristic´,K.;Sremcˇev,N.;Jocanovic´,M.;Spajic´,J.;Brkljacˇ,N.UnsupervisedModellingofE-Customers’
Profiles: Multiple Correspondence Analysis with Hierarchical Clustering of Principal Components and Machine Learning
Classifiers.Mathematics2024,12,3794.[CrossRef]
7. Tabianan,K.;Velu,S.;Ravi,V.K-MeansClusteringApproachforIntelligentCustomerSegmentationUsingCustomerPurchase
BehaviorData.Sustainability2022,14,7243.[CrossRef]
8. Fang,C.;Liu,H.ResearchandApplicationofImprovedClusteringAlgorithminRetailCustomerClassification.Symmetry2021,
13,1789.[CrossRef]
9. Matuszelan´ski,K.;Kopczewska,K.CustomerChurninRetailE-CommerceBusiness:SpatialandMachineLearningApproach.
J.Theor.Appl.Electron.Commer.Res.2022,17,165–198.[CrossRef]
10. Eslami,E.;Razi,N.;Lonbani,M.;Rezazadeh,J.UnveilingIoTCustomerBehaviour:SegmentationandInsightsforEnhanced
IoT-CRMStrategies:ARealCaseStudy.Sensors2024,24,1050.[CrossRef]
11. Devi,N.M.;Asha,V.;Dev,P.;Kumar,P.CustomerLoyaltyandRetentionAnalysisUsingHybridStrategy.InProceedingsofthe
IEEE3rdInternationalConferenceonInventiveComputingandInformatics(ICICI),Bangalore,India,4–6June2025;pp.472–477.
[CrossRef]
12. Khiloun,I.R.;Belmabrouk,K.;Dekhici,L.;Bergmeir,C.HeterogeneousGraphNeuralNetworksforProductRecommendationon
TransactionalRetailData.Commun.Sci.Technol.2025,23,23–35.
13. Mirzaee,A.;Zeynali,M.;Ghorbanzadeh,A.;Ghorbanzadeh,P.PersonalRecommenderModelandPredictingConsumerBehavior
inDigitalMarketingBasedonDeepLearning.Trans.Mach.Intell.2024,7,179–193.[CrossRef]
14. Lewaaelhamd,I.CustomerSegmentationUsingMachineLearningModel:AnApplicationofRFMAnalysis.J.DataSci.Intell.
Syst.2024,2,29–36.[CrossRef]
15. Liao, J.; Jantan, A.; Ruan, Y.; Zhou, C.Multi-behaviorRFMmodelbasedonimprovedSOMneuralnetworkalgorithmfor
customersegmentation.IEEEAccess2022,10,122501–122512.[CrossRef]
16. Talaat,F.M.;Aljadani,A.;Alharthi,B.;Farsi,M.A.;Badawy,M.;Elhosseini,M.AMathematicalModelforCustomerSegmentation
LeveragingDeepLearning,ExplainableAI,andRFMAnalysisinTargetedMarketing.Mathematics2023,11,3930.[CrossRef]
17. Cheng,C.-H.;Chen,Y.-S.ClassifyingthesegmentationofcustomervalueviaRFMmodelandRStheory.Expert.Syst.Appl.2009,
36,4176–4184.[CrossRef]
18. Akande,O.N.;Akande,H.B.;Asani,E.O.;Dautare,B.T.CustomerSegmentationthroughRFMAnalysisandK-meansClustering:
LeveragingData-DrivenInsightsforEffectiveMarketingStrategy.InProceedingsoftheIEEEInternationalConferenceonScience,
EngineeringandBusinessforDrivingSustainableDevelopmentGoals(SEB4SDG),Omu-Aran,Nigeria,2–4April2024;pp.1–8.
[CrossRef]
19. Jauhar, S.K.; Chakma, B.R.; Kamble, S.S.; Belhadi, A.Digitaltransformationtechnologiestoanalyzeproductreturnsinthe
e-commerceindustry.J.Enterp.Inf.Manag.2024,37,456–487.[CrossRef]
20. Chen,D.;Sain,S.L.;Guo,K.Dataminingfortheonlineretailindustry:AcasestudyofRFMmodel-basedcustomersegmentation
usingdatamining.J.DatabaseMark.Cust.Strateg.Manag.2012,19,197–208.[CrossRef]
21. Verma,R.;Rathor,D.;Kumar,S.;Mishra,M.;Baranwal,M.EnhancingCustomerRepurchasePrediction:IntegratingClassification
AlgorithmswithRFMAnalysisforPrecisionandActionableInsights.IIMBManag.Rev.2025,37,100574.[CrossRef]
22. Mohanty,B.;Champati,S.L.;Barisal,S.K.X.EnhancingRetailStrategiesthroughAnomalyDetectioninAssociationRuleMining.
IEEEAccess2025,13,92376.[CrossRef]
23. Lv,Q.ApplicationandoptimizationofBPpredictionmodeldrivenbyinternetofthingsintourismeducation.Sci.Rep.2025,
15,14698.[CrossRef]
24. HussainJafri,S.I.;AlSaedi,A.K.Z.;Elsafi,A.;Abdelguiom,G.A.;Ghazali,R.;Javid,I.ESReLU:ADynamicActivationFunction
forEnhancingDeepLearningPerformanceinRecommendations.Int.J.Intell.Eng.Syst.2025,18,166.[CrossRef]
25. Rudro,R.A.M.;Uddin,M.H.;Aurnob,M.J.A.;Razzaque,R.;Nur,K.Ret-DNN:PredictiveAnalyticsinRetail-AnEnhancedDeep
LearningModelforCustomerBehaviorAnalysis.Int.J.Comput.2025,18,1–14.[CrossRef]
26. Pushkarenko, Y.; Zaslavskyi, V. Synthetic Data Generation for Fraud Detection Using Diffusion Models. Inf. Secur. 2024,
55,185–198.[CrossRef]
27. Lalitha,S.;Gupta,T.S.;Thelu,A.;Reddy,V.K.;Reddy,V.C.PredictiveModelingforReal-TimeCustomerLifetimeValue. In
ProceedingsoftheIEEE15thInternationalConferenceonComputingCommunicationandNetworkingTechnologies(ICCCNT),
Kamand,India,24–28June2024;pp.1–6.[CrossRef]
28. Asfi,M.;Warsito,B.;Wibowo,A.EnhancingExplainableAI:LeveragingSHAPforTransparentDecision-MakinginMachine
Learning.InProceedingsoftheIEEENinthInternationalConferenceonInformaticsandComputing(ICIC),Medan,Indonesia,
24–25October2024;pp.1–6.[CrossRef]
29. Xu,N.;Hu,C.EnhancingE-CommerceRecommendationusingPre-TrainedLanguageModelandFine-Tuning. arXiv2023,
arXiv:2302.04443.[CrossRef]
https://doi.org/10.3390/app16052223

Appl.Sci.2026,16,2223 28of28
30. Mustafa,S.M.N.;Akhtar,A.;Noronha,J.T.P.;Salman,M.;Baig,M.A.Customersegmentationusingmachinelearningtechniques.
InProceedingsoftheIEEEInternationalMulti-disciplinaryConferenceinEmergingResearchTrends(IMCERT),Karachi,Pakistan,
4–5January2023;pp.1–7.[CrossRef]
31. Loukili, M.; Messaoudi, F.; El Ghazi, M. Personalizing product recommendations using collaborative filtering in online
retail:Amachinelearningapproach. InProceedingsoftheIEEEInternationalConferenceonInformationTechnology(ICIT),
Amman,Jordan,9–10August2023;pp.19–24.[CrossRef]
32. Alrawi,A.H.;Ajlouni,N.IntelligentMachineLearningCustomerSegmentationsAlgorithm.Manch.J.Artif.Intell.Appl.Sci.2022,
3,1–11.
33. Jana,A.K.AMachineLearningFrameworkforPredictiveAnalyticsinPersonalizedMarketing.J.Artif.Intell.Mach.Learn.Data
Sci.2020,1,560–564.[CrossRef][PubMed]
34. Imani,M.;Beikmohammadi,A.;Arabnia,H.R.ComprehensiveAnalysisofRandomForestandXGBoostPerformancewith
SMOTE,ADASYN,andGNUSUnderVaryingImbalanceLevels.Technologies2025,13,88.[CrossRef]
35. Chen,D.UCIMachineLearningRepository.OnlineRetailIIDataset.Availableonline:https://archive.ics.uci.edu/dataset/502/
online+retail+ii(accessedon6February2026).
36. Lundberg, S.M.; Lee, S.I.Aunifiedapproachtointerpretingmodelpredictions. InProceedingsoftheAdvancesinNeural
InformationProcessingSystems,LongBeach,CA,USA,4–9December2017;pp.1–10.
37. Ribeiro,M.T.;Singh,S.;Guestrin,C.WhyshouldItrustyou?Explainingthepredictionsofanyclassifier.InProceedingsofthe
22ndACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining,SanFrancisco,CA,USA,13–17August
2016;pp.1135–1144.[CrossRef]
38. Tyrovolas,M.;Kallimanis,N.D.;Stylios,C.AdvancingexplainableAIwithcausalanalysisinlarge-scalefuzzycognitivemaps.
arXiv2024,arXiv:2405.09190.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.
https://doi.org/10.3390/app16052223