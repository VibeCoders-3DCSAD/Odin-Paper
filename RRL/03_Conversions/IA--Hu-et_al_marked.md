A User Profile System for the Finance Platform of Commerce
ZhonghuangHu YuboQiu SongnanHu
ChinaCommunicationsTrading& ChinaCommunicationsInformation CCCC(Xiamen)E-commerceCo.,
SupplyCo.,Ltd. TechnologyGroupCo. Ltd.
Beijing,China Beijing,China Xiamen,China
huzhonghuang@126.com qiuyubo@ccccltd.cn husongnan@ccccltd.cn
ZijieCheng ShuaiQiu
CCCC(Xiamen)E-commerceCo., CCCC(Xiamen)E-commerceCo.,
Ltd. Ltd.
Xiamen,China Xiamen,China
chengzijie@ccccltd.cn qiushuai@ccccltd.cn
Abstract 1 INTRODUCTION
Withtherapidadvancementofbigdatatechnology,userprofiling Theinformationonthewebisalwaystoogeneraltosolveindividual
hasemergedasacriticaltoolforenterprisestorefineoperationsand user’sneed.Anaccuraterepresentationofauser’sinterestisstored
enhanceprecisionmarketing.Thispaperexplorestheapplication inauserportrait.Researchersareinterestedinhowtoidentifythe
ofuserprofilingwithinthefinancialplatformofcommerce,focus- interestoftheuserandbuildanaccurateprofile.
ingontheintegrationofinternalandexternaldataresources,data Intheyearof2015,theStateCouncilofChinaproposedthe“Ac-
miningtechniques,andtheconstructionofauserprofilemodeland tionPlanforPromotingtheDevelopmentofBigData”[4]pointed
system.Theproposedsystemaimstoachieveprecisemarketing, that“thedatahasbecomeabasicstrategicresourceforthecoun-
riskcontrol,andinformeddecision-makingbyprovidingcompre- try,andbigdataisincreasinglybecominganewdrivingforcefor
hensiveinsightsintouserbehaviorandpreferences.Thesystem economictransformationanddevelopment.”In2016,inresponse
encompassesmodulesforindividualandgroupuserprofiles,be- tothedevelopmentandapplicationofbigdata,theChinaBank-
haviortrendanalysis,andtagmanagement,facilitatingdetailed ingandInsuranceRegulatoryCommissionemphasizedtheneed
usersegmentationandtargetedmarketingstrategies.Asample toproactivelyformulateabigdatastrategy,activelyestablisha
K-meansclusteringalgorithmisalsopresentedtodemonstrateuser bigdataservicesystem,strengthendatasharing,deepenbigdata
groupingbasedonsharedcharacteristics.Thefindingshighlight applications,andunleashthevalueofdata.Inviewofthehuge
thepotentialofuserprofilingtoimprovecustomersatisfactionand datasystemandmassivedata,developingvaluableinformation
overallcompetitivenessinthefinancialindustry,whilepromoting throughdatamininghasbecomeanimportantchallenge.Asthe
cross-industrydataintegrationandthecontinuousevolutionof Internetgraduallyenterstheeraofbigdata,itwillinevitablybring
userprofilemodels. aseriesofchangesandreshapestoenterprisesanduserbehaviors;
thebiggestchangeisthatalluserbehaviorsare"visualized"infront
CCSConcepts ofenterprises.Withthein-depthresearchandapplicationofbig
•Informationsystems→Enterpriseinformationsystems. datatechnology,enterprisesareincreasinglyfocusingonhowto
usebigdatatoserverefinedoperationsandprecisionmarketing,
Keywords andthenfurtherexplorepotentialbusinessvalue.Therefore,the
conceptofuserprofilingcameintobeing.Userprotraitcanmake
UserProfileSystem,BehaviorAnalysis,DataProcessing,DataInte-
theserviceobjectsofproductsmorefocusedandmorefocused.To
gration
increaseclient’ssatisfactionandincreasethecompetition,financial
ACMReferenceFormat: institutions,especiallybankinginstitutions,needtorapidlyinno-
ZhonghuangHu,YuboQiu,SongnanHu,ZijieCheng,andShuaiQiu.2024. vatetheirproducts.Tomakegooduseofexistingdataassetsto
AUserProfileSystemfortheFinancePlatformofCommerce.In2024the makedatavaluable.Toachievethisgoal,theuseofuserprofileas
12thInternationalConferenceonInformationTechnology(ICIT)(ICIT2024), atoolhasbecomeabreakthroughinsolvingindustrypainpoints.
December13–15,2024,KualaLumpur,Malaysia.ACM,NewYork,NY,USA,
Userprofilescaneffectivelypresentusercharacteristicsandpro-
6pages.https://doi.org/10.1145/3718391.3718436
videsupportforproductinnovation.Traditionalfinancialindustry
reliesoncommunicationbetweenaccountmanagersandcustomers
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed tounderstandcustomers.Theuserprofilesystemcaneffectively
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation breaktheresourcebindingrelationshipbetweenaccountmanagers
onthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthanthe
andcustomerresources.Anyonecanunderstandcustomerscom-
author(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,or
republish,topostonserversortoredistributetolists,requirespriorspecificpermission prehensivelyandthree-dimensionallythroughthesystem.
and/orafee.Requestpermissionsfrompermissions@acm.org. As industry competition continues to intensify, product and
ICIT2024,KualaLumpur,Malaysia
servicehomogeneityandcustomerloyaltydecrease,thestickiness
©2024Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
ACMISBN979-8-4007-1737-6/24/12 betweenusersandproductsgraduallydecreases,andtheuserchurn
https://doi.org/10.1145/3718391.3718436
267

ICIT2024,December13–15,2024,KualaLumpur,Malaysia Trovatoetal.
ratebecomesmoreserious.Therefore,itisparticularlyimportantto two-stagestructureusingamonthofdatawithdemographiclabels
usemultipledatasourcesandapplybigdatatechnologytoachieve asthetrainingdata.Thefirststageofthestructureisbasedon
moreaccurateuserprofiles,therebypromotingproductoptimiza- traditionalmachinelearningmodelsandneuralnetworkmodels,
tion,iterativeupgradesofbusiness,customizedservicesandmore whereasthesecondoneisacombinationofthemodelsfromthe
accuratemarketing. firststage.Paper[7]minismobileuserbehaviorpatternsandcon-
Therestofthispaperisorganizedasfollows:InSection2we structsagroupuserprofilebyanalyzingaccessdatacollectedfrom
presentrelatedwork.PreliminariesaregiveninSection3.InSection theWeChatMiniProgram.Theyextracttheattributesofmobile
4,wepresentouruserprofilemodelandthesystemofuserprofile usersconsideringtheiragegroup,geographicinformation,andon-
isintroducedinsection5.Weconcludetheworkofthispaperin lineduration.UsingZ-scorestandardizedprocessingandK-means
Section6. clusteringalgorithm,theymodeltheuserprofilesthroughthree
dimensionsincludinginteractionintensity,dailyaverageduration,
andaccessfrequency.Zhangetal.constructedapoweruserbehav-
2 RELATEDWORK
iorassessmentmodelbasedonahugenumberofuserprofiles[11].
TheInternetindustrywasthefirsttoproposeandapplyuserprofile Aftertextconversion,datacleaningandvariableattributeanalysis
technology.TheconceptoriginatedfromthePersonaconceptpro- thehugenumberofgridcustomerservicephonedata,alotofuser
posedbyAlanCooper,thefatherofinteractivedesign.AlanCooper profilesareestablished.Thelogisticregressionmodeliscombined
explainedthatPersonaisavirtualusercorrespondingtoarealuser, withthedecisiontreealgorithmtocompletetheconstructionof
andisatargetcustomermodelbasedonaseriesofrealdata.Based theelectricpoweruserbehaviorevaluationmodel.
onthistechnology,theuserprofilesystemwasdeveloped.Initially, Thee-commerceindustryutilizesthepersonalprofilefunction
theUniversityofCaliforniagraduallylearnedbydisplayingand ofsocialplatformsformarketingandpromotion,therebyenriching
collectingusers’satisfactionwiththecurrentpagetoestablisha thedatadimensionsofuserconsumptionhabits,consumptionabil-
userinterestmodel.Later,theCaliforniaUniversityofManagement ity,consumptionpreferences,etc.accumulatedbythee-commerce
developedtheuserprofilesystemWebWatcher[2],whichchanged industryitself,andefficientlyconductingmarketingandpromo-
fromindividualuserstogroupusers,usingdatacollectorstorecord tion[10].Withtherapiddevelopmentofbigdataanalysistechnol-
users’behavior,preferences,andbasicinformationontheInter- ogyandtherapidaccumulationofdatainvariousindustries,user
net,andusingthisstatisticalinformationtoderivethebrowsing profilesaregraduallyutilizingmassiveamountsofdatabetween
behaviorofusergroups,therebybuildingauserinterestmodel. industriestopromoteactiveunderstandingofusersandprovide
Currently,theneedforsoftwaresystemstoautomaticallyadapt userswithbetterexperiences[8].Theenrichmentofdatadimen-
totheirusershasbeenrecognizedandtheresearchonuserpro- sionsandthebreakingofbarrierstoinformationexchangebetween
file[9].Ausermodelisinitializedeitherwithdefaultvaluesor industrieshavedriventhedevelopmentofdataanalysisandthe
byqueryingandgroupingtheuserin“stereotypes”[1].Userpro- improvementofuserprofilemodels,thusformingavirtuouscycle
filehasbeenwidelyappliedinthefinancialindustry,e-commerce mechanism.Methodsandapplications.
industry,powerindustry,andtelecomindustry.Especiallyinthe
financialindustry,withthepopularizationofbigdatatechnology 3 PRELIHMINARY
andtheemphasisondatainthefinancialindustry,userprofilehas
3.1 DataAcquisitionandDataProcessing
graduallybecomeanimportantmeansforfinancialinstitutions
toenhancetheircompetitiveness.Recently,financialinstitutions Dataacquisitionisbasedonvaryinguserparticipationmethods,
integrateinternalandexternaldataresources,utilizedatamining thecollectionofrawuserprofiledatacanbecategorizedintotwo
andbigdataanalysistechniques,constructuserprofilemodels, approaches:explicitandimplicitacquisition.Explicitacquisitionin-
andachievecomprehensiveunderstandingandaccurateprediction volvesusersmanuallyinputtingtheirbasicinformation,behavioral
ofcustomerbehavior.Thisnotonlyhelpsfinancialinstitutions preferences,andrelateddata.Thisstraightforwardmethodoffers
achieveprecisemarketingandriskcontrol,butalsoimprovescus- high-qualitydatabutnecessitatesactiveuserengagementandtypi-
tomersatisfactionandloyalty. callylimitsthescopeofaccessibleinformation.Conversely,implicit
Francaetal.didresearchinthefieldofpsychologyhighlighted acquisitionistransparenttousersandencompassestwomaintech-
thevalueofidentifyingusers’personalitytraits,whichhelpsbuild niques:logginguserinformationduringinteractionsandanalyzing
adaptiveandpersonalizedsystemsandimproveuserexperiences[5]. userbehaviorpatternstodeducecharacteristics.Thericherdata
Gu et al. proposed a psychological modeling method based on obtained through implicit methods results in more comprehen-
computational linguistic features to profile personality traits of siveuserprofiles.Inpractice,bothmethodsareoftencombinedby
usersonSinaWeiboandtheircorrelationswithuser’ssocialbe- industryandacademiatoleveragethediversedatatrailsleftby
haviors[6].Thisresearchinvestigatesthepotentialrelationship users.
betweenpersonalitytraitsofusers,profileinformation,andsocial- Dataprocessingreferstothepurificationofrawdatatoeliminate
networkbehaviorsonSinaWeibo.Thisapproachunderstanded impurities,yieldingstandardizeddatasuitableforconstructinguser
demographicandpsychologicalprofilesofusersonsocialmedia profiles.Keydataprocessingtechniquesincludewordsegmenta-
withoutcustomerdisruption.Chenetal.usedclassificationalgo- tion,datafiltering,anddatanormalization.Wordsegmentationis
rithmsinmachinelearningtopredictusers’demographicattributes crucialforunstructuredtextdataprocessing;datafilteringensures
basedonamonthofdatacollectedwiththeSogousearchengine thereliabilityofbasicdatabyriddingitofimpurities;anddata
inordertogenerateusers’profiles[3].Theproposedmodelisa normalizationmaintainsconsistencyacrossinputmodeldata.
268

AUserProfileSystemfortheFinancePlatformofCommerce ICIT2024,December13–15,2024,KualaLumpur,Malaysia
3.2 TagSelectionandTagWeight mergedasasuper-documenttotraintheclassifierforeachconcept.
Tagssymbolizespecificusercharacteristicsandserveasahighly Asuper-documentgoesthroughanindexingtocalculateavector.
correlatedcontentorganizationmethod,enablingswiftidentifica- Theweightofeachvocabularyterm(vector)isstoredtheinthat
tionofsuitablecontentandclassifications.Fromacomputational concept.Thus,eachconceptistreatedasn-dimensionalvectorsin
hierarchyperspective,tagscanbecategorizedintofacttagsand whichnrepresentsthenumberofuniquetermsinthevocabulary.
modeltags.Facttagsarederivedfromstatisticalanalysesofraw Eachtermweightiscalculatedas𝑡𝑓 ×𝑖𝑑𝑓 andnormalizedbytheir
data,forinstance,userpurchasefrequency,whichreflectsastatis- length.Inmoredetail,𝑢𝑤 𝑖𝑗 representstheunnormalizedweightof
ticaloverviewofauser’sactualpurchasebehavioroveraspecified
term𝑖inconcept𝑗,iscalculatedasequation(1)and(2)
duration.Conversely,modeltagsareformulatedbasedonfacttags 𝑢𝑤 𝑖𝑗 =𝑡𝑓 𝑖𝑗 ×𝑖𝑑𝑓 𝑖 (1)
byestablishingassociationswithbusinesschallenges,therebyyield- #𝑜𝑓𝑑𝑜𝑐𝑢𝑚𝑒𝑛𝑚𝑡𝑠𝑖𝑛𝑡ℎ𝑒𝑐𝑜𝑙𝑙𝑒𝑐𝑡𝑖𝑜𝑛
ingtagstailoredforuserprofileselectionmodels. 𝑖𝑑𝑓 𝑖 =𝑙𝑜𝑔 (2)
#𝑜𝑓𝑑𝑜𝑐𝑢𝑚𝑒𝑛𝑡𝑠𝑖𝑛𝑡ℎ𝑒𝑐𝑜𝑙𝑙𝑒𝑐𝑡𝑖𝑜𝑛𝑡ℎ𝑎𝑡𝑐𝑜𝑛𝑡𝑎𝑖𝑛𝑡
𝑖
Tags primarily address the issue of description. However, in
where𝑡𝑓 𝑖𝑗 is the number of occurrences of𝑡 𝑖 in𝑠𝑑 𝑗,𝑖𝑑𝑓 𝑖‘is the
practicalapplications,resolvingtheproblemofdatacorrelationis
super-documentusedfortrainingconcept𝑗.
equallyimportant.Hence,tagsareoftendesignedasacomprehen-
(2)Collectinguserdata.Thedocumentsarestoredinalogfile
sivesystemencompassingmultipletags.Eachtagholdsvarying
byaproxyserver.Thedocumentsareextractedforeachuserand
degreesofsignificanceinportrayingspecificdimensionsofauser
filteredtoremovedocumentsthatareconsideredasnotsuitable
profile.Consequently,assigningweightstothesetagsbasedon
[10].
theirimportanceincharacterizinguserprofilesisimperative.The
(3)classifyingthedocuments.Documentsandconceptsarelisted
prevalentweightingmethodologiescanbebroadlyclassifiedinto
inthevectormodelandthesimilarityiscalculatedinthevector.
subjectiveandobjectiveweightingmethods.Objectiveweighting
methodsencompasstheentropyweightmethod,correlationco- Thesimilaritybetweenconcept𝑐 𝑗 anddocument𝑑 𝑘 iscalculated
asequation(3).
efficientmethod,andstandarddeviationmethod,amongothers.
𝑛
Subjectiveweightingmethodsincludethesubjectiveexperience ∑︁
method,expertsurveyweightingmethod,Delphimethod,andana- 𝑠𝑖𝑚𝑖𝑙𝑎𝑟𝑖𝑡𝑦(𝑐 𝑗 ,𝑑 𝑘)=𝑐 𝑗 ◦𝑑 𝑘 = 𝑤 𝑖𝑗 ×𝑑 𝑗𝑘 (3)
𝑖=1
lytichierarchyprocess.
where𝑛representsthenumberoftermsinthevocabulary,𝑤 𝑖 𝑗 is
thenormalizedweightorterm𝑖inconcept𝑗.
3.3 UserProfileModelselection
After the similarity is calculated, the results are sorted, the
Userprofilingtechnologyisamultidisciplinarycombinationthat weightsfromdocumentswhichmatchthesameconceptareaccu-
requiresknowledgefusioninareassuchasknowledgegraphs,nat- mulated.Auserfileconsistsallconceptswithweightsarecreated
urallanguageprocessing,machinelearning,anddatamining.The asaresult.
commonlyuseduserprofilemodelsaremainlydividedintothree AsshowninFigure1,theprofilemodelcontainsfourlayers:
categories:textminingtechniques,classificationalgorithms,clus-
teringalgorithms,etc.Textminingmainlyfocusesonthemining
andprocessingofunstructureddata,includingTF-IDF,vectorspace
models,topicmodels,etc;Classificationalgorithmsaresuitablefor
supervisedlearninguserclassification,includingartificialneural
networks(ANN),proximityalgorithms(KNN),supportvectorsup-
portmachines(SVM),etc;Clusteringalgorithmsaresuitablefor
unsupervisedlearninguserclustering,includingk-meansclustering
algorithm,k-centroidalgorithm,densitybasedclusteringalgorithm
DBSCAN,hierarchicalagglomerativeclusteringalgorithmHAC,
etc.
Theapplicationscopeofuserprofilingisverybroad,mainly
includingthreeaspects:firstly,byanalyzingpotentialusersand
targetingspecificusergroupsforadvertisingplacement,unneces-
sarycostinvestmentcanbereduced;Secondly,byanalyzingthe
correlationofuserdata,apersonalizedrecommendationsystem
foruserscanbeconstructedtoachievecustomizeddeploymentof
servicesorproductsforthousandsofpeople;Thirdly,evaluatethe
operationaleffectivenessoftheenterprise,improveproductopera-
tions,enhanceservicequalityanduserexperience,andpromote
thehealthydevelopmentoftheenterprise. Figure1:TheUserProfileModel
4 THEUSERPROFILEMODEL
DataCollectionLayer:Thisfoundationallayerservesasthe
Tobuildauserprofilemodel,usuallyitrequiresthreesteps:(1) cornerstoneandindispensableprerequisiteforbuildinguserpro-
Trainingtheclassifier.Thetrainingdataforaparticularconceptare files.Itinvolvesthesystematicgatheringofamyriadofdatapoints
269

ICIT2024,December13–15,2024,KualaLumpur,Malaysia Trovatoetal.
fromavarietyofsources.Thesesourcesincludebutarenotlim- UserProfileModuleincludesthreemainfunctionalities.List
ited to user interactions on digital platforms, user information, ofUserProfilescontainsacollectionofalluserprofilescreated
transactionalhistories,browsingbehaviors,businessactivities,and withinthesystem,allowingforeasyaccessandoverview.Indi-
more.Thedatacollectedisbothstructured(e.g.,numericaldatain vidualUserProfiledetailsprofileofindividualuser,including
databases)andunstructured(e.g.,textdatafromsocialmediaposts). userbasicinformation,userfinancialinformation,userworking
Thequality,completeness,andtimelinessofthedatacollectedare information,usercompanyinformation,userpreferences,purchase
crucialfactorsthatdirectlyinfluencetheaccuracyandreliability history,andanyotherrelevantdatapoints.Thisprovidesaholistic
oftheuserprofilesgenerated. viewofeachuser.UserBehaviorTrendsprovideanalysisandvi-
DataStorageLayer:Thislayerisresponsibleforsecurelystor- sualizationofuserbehaviorovertime,identifyingpatterns,trends,
ingandmanagingthevastamountsofdatacollectedfromthedata andchangesinuserpreferencesorinteractions.Thiscanhelppre-
collectionlayer.Itemploysadvanceddatabasemanagementsystems dictfuturebehaviorsandoptimizeuserengagementstrategies.
andstoragesolutionstoensurethedataisorganized,accessible, UserGroupProfileModuleincludefivemajorfunctionalities.List
andscalable.Thedatastoragelayeralsosupportsdatabackupand ofUserGroupsProfilescontainsacollectionofallusergroup
recoverytoensurethatdatacanberestoredquicklyandefficiently profiles,enablingquicknavigationandcomparisonbetweendiffer-
intheeventofafailure.Integritychecks,suchasdatavalidationand entusergroups.IndividualUserGroupProfilecontainsin-depth
consistencyenforcement,areperformedtomaintaindataaccuracy profilesofaspecificusergroup,detailingsharedcharacteristics,
andreliability.Effectivemanagementofthedatastoredinthislayer interests,andbehaviors.Thishelpstailormarketingandproduct
enablesseamlessaccessandretrievalforsubsequentprocessing developmenteffortstobettermeettheneedsofthesegroups.User
andanalysisintheMiddleLayer. GroupAnalysisdetailsexaminationofusergroupdata,including
TheMiddleLayer:Positionedbetweenthedatastoragelayer demographics,preferences,andbehaviors,togaininsightsintothe
andthedatavisualizationlayer,thislayerisamultifacetedentity uniquequalitiesandchallengesofeachgroup.UserGroupTrends
thatcanbebothabstractandtangible.Itservesasthebrainofthe providetrackingandanalyzingtrendswithinusergroups,such
profilesystem,interactingwithboththedatastoragelayerand aschangesinpreferencesoremergingbehaviors,tostayahead
thedatavisualizationlayertoimplementtheintricatebusiness ofmarketshiftsanduserneeds.UserGroupCompanyAnaly-
logicofuserprofiles.Themiddlelayeristaskedwithprocessing, sisevaluateshowusergroupsinteractwithspecificcompanies,
integrating,andanalyzingthedatastoredinthebottomlayer.This identifyingareasforimprovement,andopportunitiesfordeeper
includesdatacleaningtoremoveinconsistenciesanderrors,data engagementorloyaltybuilding.
normalizationtoensureuniformity,anddataenrichmenttoadd TagInformationModulecontainsthreekeyfunctionalities.List
contextandvalue.Additionally,themiddlelayeremploysadvanced ofUserTagsincludesalistofalltagsassignedtoindividualusers,
algorithmsandmachinelearningmodelstoextractmeaningful helpingtocategorizeandgroupusersbasedonsharedattributesand
insightsandpatternsfromthedata.Theseinsightsarethenusedto behaviors.ListofUserGroupTagsissimilartousertags,butfor
createdetailedandnuanceduserprofilesthatencapsulatevarious usergroups,allowingforthecategorizationandanalysisofgroups
aspects of user behavior, preferences, demographics, and more. basedoncommoncharacteristicsandtrends.TagManagement
Throughsophisticateddatavisualizationtoolsandsystems,the providestoolsforcreating,editing,anddeletingtags,aswellas
dataresultsandmodelsimplementedinthemiddlelayercanbe assigningthemtousersorusergroups.Thisfeatureensuresthat
transformedintovisuallycompellingandeasilyunderstandable thetaggingsystemremainsup-to-dateandrelevant,supporting
formats.Thisenablesbusinessusersandanalyststogaininsights accurateandefficientusersegmentationandanalysis.
intouserbehavior,identifytrends,andmakeinformeddecisions
basedondata-driveninsights. 5.1 SampleCharacteristicsofUserProfile
DataVisualizationLayer:Thisisthepinnacleoftheprofile
TheTable1describealistofsamplecharacteristicsofuser’sbasic
system,oftenreferredtoasthenarrowuserprofile.Itrepresents
informationusedinprofile.
thefinaloutput,presentingtheinsightsandpatternsderivedfrom
themiddlelayerinavisuallyappealingandintuitivemanner.The 5.2 ASampleK-meansUserGrouping
datavisualizationlayeremploysavarietyofcharts,graphs,dash-
Algorithm
boards,andothervisualelementstodisplayuserprofiles,trends,
andpatterns.Thesevisualizationsenablebusinessuserstoquickly TheK-meansalgorithmisanunsupervisedlearningalgorithmused
andeasilyunderstandcomplexdatasets,identifykeytrendsand todivideadatasetintoKclusters(groups),whereeachclusteris
insights,andmakedata-drivendecisions.Byprovidingaclearand representedbyitscentroid(centerpoint)[8].Thealgorithmcontin-
concise view of user behavior and preferences, the data visual- uouslyupdatesthecentroidandgroupingthroughiterationuntil
ization layer supports strategic planning, product development, theconvergenceconditionisreached.Inusergroupingapplications,
marketingcampaigns,andmore. userswithsimilarcharacteristicsorbehaviorscanbegroupedto-
gether to facilitate subsequent recommendations, analysis, and
otherapplications.
5 AUSERPROFILESYSTEM AsampleK-meansalgorithmforgroupingusersisprovidedas
Theuserprofilesystemisdevelopedtoprovideprecisemarketing, follows.
riskpreventionandcontrol,decision-making.Themainfunctional- (1) Initializecentroids:RandomlyselectKusersfromtheuser
itiescurrentlycontainthreeparts,asshowninFigure2: datasetastheinitialcentroids.
270

AUserProfileSystemfortheFinancePlatformofCommerce ICIT2024,December13–15,2024,KualaLumpur,Malaysia
Figure2:FunctionalitiesoftheUserProfileSystem
UserInfo UserFinancialInfo UserWorkingInfo UserTransactionInfo
|     | Name | Contribution  |     | Company         | TransactionofParties |
| --- | ---- | ------------- | --- | --------------- | -------------------- |
|     | Age  | LevelofCredit |     | PositionandRank | TransactionItems     |
|     | ID   | Income        |     | WorkExperience  | TimeandLocation      |
Education Expenditure YearofworkingintheCompany TransactionStatus
|     | Gender    | RowAsset | IndustryBackground |     | PriceandPaymentMethod |
| --- | --------- | -------- | ------------------ | --- | --------------------- |
|     | Email     | Debt     |                    |     | RelevantInformation   |
|     | CellPhone |          |                    |     | TransactionHistory    |
Table1:UserCharacteristics
(2) Iterationprocess:Startiteratinguntilthemaximumnum- Algorithm1K-meansAlgorithmforGroupingUsers
berofiterationsMax_iterationisreachedorthechangein
Input: User_Dataset,K,Max_Iteration,Threshold
centroidislessthanthethresholdThreshold.
|     |     |     |     | Output: User_Groups,Centroids |     |
| --- | --- | --- | --- | ----------------------------- | --- |
(a) Grouping:Foreachuser,calculatetheirdistancetoallcen- 1: foriterationinrange(MaxIteration)do
| troidsandassignthemtothegroupwiththecentroidwith |     |     |     | User_Groups=[] |     |
| ------------------------------------------------ | --- | --- | --- | -------------- | --- |
2:
thesmallestdistance.Duringinitialization,setamaximum foruserinUser_Dataset:do
3:
valueastheminimumdistance,traverseallcentroids,find
|     |     |     |     | 4: min_distance=maximumvalue |     |
| --- | --- | --- | --- | ---------------------------- | --- |
thecentroidwiththesmallestdistance,andrecordthe
|                                                   |                  |                     |           | 5: forcentroidinCentroids:do                     |     |
| ------------------------------------------------- | ---------------- | ------------------- | --------- | ------------------------------------------------ | --- |
| index                                             | of that centroid | as the user’s group | ID. After | as-                                              |     |
|                                                   |                  |                     |           | 6: distance=calculatingthedistancebetweenuserand |     |
| signingeachusertothecorrespondinggroup,thecurrent |                  |                     |           | centroid                                         |     |
groupingresultUser_Groupsisobtained. ifdistance<min_distance:then
7:
(b) Updatecentroid:Foreachgroup,calculatethecentroid
|     |     |     |     | 8: min_distance=distance |     |
| --- | --- | --- | --- | ------------------------ | --- |
ofalluserswithinthegroup(i.e.,thenewcentroid).This
|     |     |     |     | 9: group_id=currentcentroid’sindex |     |
| --- | --- | --- | --- | ---------------------------------- | --- |
isusuallyachievedbycalculatingtheaverageofalluser
|     |     |     |     | 10: endif |     |
| --- | --- | --- | --- | --------- | --- |
informationwithinthegroup.Storeallnewcentroidsin 11: User_Groups.append(groupid)
| thenew_centroidslist. |     |     |     | endfor |     |
| --------------------- | --- | --- | --- | ------ | --- |
12:
(3) Checkconvergence:Ifthechangebetweenthenewandold
13: endfor
| centroids | is less than the | given threshold | Threshold, the |     |     |
| --------- | ---------------- | --------------- | -------------- | --- | --- |
14: new_centroids=[]
algorithmisconsideredtohaveconvergedandtheiteration
15: foriinrangeK:do
isstopped.Otherwise,assignthenewcentroidtotheoriginal 16: Group_Users=selectallusersinUser_Datasetingroupi
centroidandcontinuewiththenextiteration. new_centroid=calculatingGroup_Users’scenter
17:
(4) Returnresult:Whentheiterationends,returnthefinalgroup-
|     |     |     |     | 18: new_centroids.append(new_centroid) |     |
| --- | --- | --- | --- | -------------------------------------- | --- |
ingresultUser_GroupsandcentroidCentroids.
19: endfor
20: ifthechangeofgroupcenterislessthanThresholdthen
| 6 CONCLUSION |     |     |     | 21: Break |     |
| ------------ | --- | --- | --- | --------- | --- |
endif
| Userprofilingprovidescomprehensiveuserinsightsforfinancial |     |     |     | 22: |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- |
Centroids=new_centroids
| institutionsthroughin-depthanalysisofuserbehaviorandpref-   |     |     |     | 23:                                |     |
| ----------------------------------------------------------- | --- | --- | --- | ---------------------------------- | --- |
| erences.Thisnotonlyhelpsfinancialinstitutionsachieveprecise |     |     |     | 24: endfor                         |     |
|                                                             |     |     |     | 25: return User_GroupsandCentroids |     |
marketingandriskcontrol,butalsosignificantlyimprovescus-
tomersatisfactionandloyalty.Inthefinancialsupplychain,user
profilinghasbecomeakeymeansforfinancialinstitutionstoen-
hancetheircompetitiveness.Withtheincreaseofdatadimensions
271

ICIT2024,December13–15,2024,KualaLumpur,Malaysia Trovatoetal.
andthebreakingofinformationexchangebarriersbetweenindus- content/2015-09/05/content_10137.htm
tries,theconstructionofuserprofileswillpaymoreattentionto [5] FO.Franca,DHGoya,andCL.C.Penteado.2018.UserprofilingoftheTwitter
SocialNetworkduringtheimpeachmentofBrazilianPresident.SocialNetwork
theintegrationandsharingofcross-industrydata.Thisnotonly
Analysis&Mining8,1(2018),1–5.
enrichesthecontentofuserprofiles,improvestheiraccuracyand [6] H.Gu,J.Wang,Z.Wang,B.Zhuang,andF.Su.2018.ModelingofUserPortrait
comprehensiveness,butalsopromotesthedevelopmentofdata ThroughSocialMedia.In2018IEEEInternationalConferenceonMultimediaand
Expo.1–6.
analysistechnologyandtheimprovementofuserprofilemodels, [7] T.Hovorushchenko,D.Medzatyi,D.Kvanitskyi,andS.Kravchuk.2022.Character-
formingavirtuouscyclemechanism. isticsandMethodofFormingtheUserInformationPortrait.In12thInternational
ConferenceonDependableSystems,ServicesandTechnologies.1–6.
[8] P.KeikhosrokianiandG.M.Fye.2024.Ahybridrecommendersystemforhealth
References
supplemente-commercebasedoncustomerdataimplicitratings.Multimedia
[1] P.A.Akiki,A.K.Bandara,andY.Yu.2016.Engineeringadaptivemodel-driven Tools&Applications83,15(2024),45315–45344.
userinterfaces.IEEETransactionsonSoftwareEngineering42,12(2016),1118– [9] AlfredKobsa.1993.UserModelling:Recentwork,prospectsandhazards.Adaptive
1147. UserInterfaces:PrinciplesandPractices10(1993),1–14.
[2] R.Armstrong,D.Freitag,andT.Joachims.1995.Webwatcher:Alearningappren- [10] X.Wang,B.Cai,andK.Salleh.2024.Researchontheapplicationofclusteranalysis
ticefortheworldwideweb.InAAAISpringsymposiumonInformationgathering incross-bordere-commercecustomersegmentationandmarketstrategy.Applied
fromHeterogeneous,distributedenvironments.93–107. MathematicsandNonlinearSciences9,1(2024),2024–2568.
[3] Y.Chen,J.He,W.Wei,N.Zhu,andC.Yu.2021.AMulti-ModelApproachfor [11] M.Zhang,Z.Deng,C.Song,H.Liu,andM.Ding.2022. Poweruserbehavior
UserPortrait.FutureInternet13,6(2021),142–147. evaluationmodelbasedon95598userportrait.InInternationalConferenceon
[4] ChinaStateCouncil.2015.TheStateCouncilissuesadocumenttopromotethe Algorithms,MicrochipsandNetworkApplications.SPIE.454–459.
developmentofbigdataNoticeofActionPlan. https://www.gov.cn/zhengce/
272