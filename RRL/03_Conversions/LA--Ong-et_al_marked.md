Article
Purchasing Intentions Analysis of Hybrid Cars Using Random
Forest Classifier and Deep Learning
ArdvinKesterS.Ong1,2,* ,LaraNicoleZ.Cordova3,FranscineAltheaB.Longanilla3,NealloL.Caprecho3,
RockselAndryV.Javier3,RiañinaD.Borres1,4andJosephineD.German1
1 SchoolofIndustrialEngineeringandEngineeringManagement,MapúaUniversity,658MurallaSt.,
Intramuros,Manila1002,Philippines
2 E.T.YuchengcoSchoolofBusiness,MapuaUniversity,1191PabloOcampoSr.Ext,Makati1205,Philippines
3 YoungInnovatorsResearchCenter,MapúaUniversity,658MurallaSt.,Intramuros,Manila1002,Philippines
4 SchoolofGraduateStudies,MapúaUniversity,658MurallaSt.,Intramuros,Manila1002,Philippines
* Correspondence:aksong@mapua.edu.ph;Tel.:+63-(2)8247-5000(ext.6202)
Abstract: In developed or first-world countries, hybrid cars are widely utilized and essential in
technologicaldevelopmentandreducingcarbonemissions.Despitethat,developingorthird-world
countriessuchasthePhilippineshavenotyetfullyadoptedhybridcarsasameansoftransportation.
Hence,theSustainabilityTheoryofPlannedBehavior(STPB)wasdevelopedandintegratedwith
theUTAUT2frameworktopredictthefactorsaffectingthepurchasingintentionsofFilipinodrivers
toward hybrid cars. The study gathered 1048 valid responses using convenience and snowball
samplingtoholisticallymeasureuseracceptancethroughtwelvelatentvariables.MachineLearning
Algorithm(MLA)toolssuchastheDecisionTree(DT),RandomForestClassifier(RFC),andDeep
LearningNeuralNetwork(DLNN)wereutilizedtoanticipateconsumerbehavior.Thefinalresults
fromRFCshowedanaccuracyof94%andDLNNwithanaccuracyof96.60%, whichwereable
toprovethepredictionofsignificantlatentfactors. PerceivedEnvironmentalConcerns(PENCs),
Attitude(AT),PerceivedBehavioralControl(PBC),andPerformanceExpectancy(PE)wereobserved
tobethehighestfactors.ThisstudyisoneofthefirstextensivestudiesutilizingtheMLAapproach
topredictFilipinodrivers’tendencytoacquirehybridvehicles.Thestudy’sresultscanbeadapted
Citation:Ong,A.K.S.;Cordova,
byautomakersorcarcompaniesfordevisinginitiatives,tactics,andadvertisementstopromotethe
L.N.Z.;Longanilla,F.A.B.;Caprecho,
N.L.;Javier,R.A.V.;Borres,R.D.; viabilityandutilityofhybridvehiclesinthePhilippines.Sinceallthefactorswereprovensignificant,
German,J.D.PurchasingIntentions futureinvestigationscanassessnotonlythebehavioralcomponentbutalsothesustainabilityaspect
AnalysisofHybridCarsUsing ofanindividualusingtheSTPBframework.
RandomForestClassifierandDeep
Learning.WorldElectr.Veh.J.2023, Keywords:hybridcars;machinelearningalgorithm;purchasingintentions;sustainabilitytheoryof
14,227. https://doi.org/10.3390/ plannedbehavior;UTAUT2
wevj14080227
AcademicEditor:GenevieveCullen
Received:20July2023 1. Introduction
Revised:12August2023
Greenhousegasesemittedbyoil-poweredandfossil-fueledvehicleshaveincreased
Accepted:16August2023
over the years. According to Tiseo [1], the global transportation sector is a significant
Published:18August2023
polluter,producingapproximately7.3billiontonsofcarbondioxideemissionsin2020. In
thesameyear, passengercarswerethemostabundantsourceofemissions, accounting
for 41% of global transportation emissions. In Wasiak’s [2] study, internal combustion
Copyright: © 2023 by the authors. engineshavetwoprominentdrawbacks. Thefirstistherelativelylowefficiencyofturning
Licensee MDPI, Basel, Switzerland. theenergycontainedinthefuelintovaluablemechanicalenergyforpropulsion,andthe
This article is an open access article secondisthattheproductionofcarbondioxideandothercomponentsoftheexhaustgas
distributed under the terms and cancontributetoglobalwarming.
conditionsoftheCreativeCommons Hybrid cars are essential in technological development and in addressing carbon
Attribution(CCBY)license(https:// emissionreduction. Furthermore,hybridcarproductioncoversthreeoftheUnitedNations’
creativecommons.org/licenses/by/ globalSustainableDevelopmentGoals(SDGs):the7thSDGforaffordableandcleanenergy,
4.0/).
WorldElectr.Veh.J.2023,14,227.https://doi.org/10.3390/wevj14080227 https://www.mdpi.com/journal/wevj

WorldElectr.Veh.J.2023,14,227 2of26
the8thSDGfordecentworkandeconomicgrowth,andthe13thSDGforclimateaction.
SincetheintroductionofthevariousSDGs,theusageofhybridcarshasbeenpromoted[3].
Thepresentgenerationisseeinganincreaseinthemarketabilityofhybridvehicles,
buttheirutilityisnotwidelyacknowledged. Irawanetal.[4]estimatedthatroughly18.20%
ofautomobileownershavebeguntoconsiderswitchingfromaconventionalvehicleand
becomingpotentialhybridcarusers,while81.22%ofcarbuyerscontinuetorejectgettinga
hybridvehiclecompletely. Thus,consumerbehaviorshouldbeinvestigatedtounderstand
purchasingbehaviorforsustainabletransportationtobewidelyaccepted.
Onetheorywidelyusedtocomprehensivelyassessconsumers’behaviorintheaspect
ofpurchasingandmarketingistheTheoryofPlannedBehavior(TPB)[5]. Itisalsoproven
to extensively measure the intention to purchase. It is applied to examine customers’
behavioralaspectsofbuyingwhilesimultaneouslyprovingsomeofthedeterminantsof
purchaseintentions[6]. InlinewiththeTPBframework,severalstudieshavesupported
thatTPBiscommonlyusedinthefieldofpurchasingcarsduetoitsexplanatorycapacityto
predicttheadoptionorpurchasingintentionofcars,specificallyinHybridElectricVehicles
(HEVs) [7,8]. Similarly, a study by Javid et al. [9] stated that the determinants of TPB
couldalsobeappliedtoconsumers’purchasingintention,eveninElectricVehicles(EVs).
However, inthestudyofGermanetal.[10], TPBhaslimitedvariablesthatrestrainthe
modelforholisticmeasurements.
Anothertheorythatcanbeusedinassessingpeople’sacceptanceandbehavioralinten-
tionsistheUnifiedTheoryofAcceptanceandUseofTechnology2(UTAUT2). Venkatesh
et al. [11] explained how UTAUT2 comprehensively measures the behavioral aspect of
technologyusage. StudiessuchasthatofNordhoffetal.[12]employedtheUTAUT2model
toexplainthepublicacceptanceofconditionallyautomatedcarsinEuropeancountries.
According to their study’s analysis, the UTAUT2 model can be applied to conditional
automation,withhedonicmotivation,socialinfluence,andperformanceexpectancyin-
fluencingthebehavioralintentiontopurchaseandutilizeaconditionallyautomatedcar.
Similarly,PrasetyoandVallespin[13]usedtheUTAUT2modeltoidentifythefactorsinflu-
encingusers’utilityofmobiletechnologyapplicationsandservices. InMalaysia,Khazaei
andTareq[14]examinedconsumers’usageofbatteryelectricvehiclesusingtheUTAUT2
since this model incorporated a broader scope of factors to measure consumers’ usage
intention. However,alimitednumberofstudieshaveanalyzedthepurchasingintentions
ofhybridcars,especiallyinthePhilippines.OnlythatofOngetal.[15]wasseentoconsider
thepurchasingintentionsofhybridcarsinthePhilippines.
InthePhilippines,hybridcarsareavailableinthemarket.Withonlyleadingcarbrands
suchasCherry,Geely,Hyundai,Mitsubishi,Nissan,andToyotasellingtheproduct,limited
accessandpopularityareobserved. Therewere11,851,192registeredmotorvehiclesand
fossil-fueledcarsinthePhilippinesasofDecember2020[16]. Unlikeothercountries,the
hybridcarvehiclemarketinthePhilippinesonlycaterstotheextremeupperclass,which
accountsforonlylessthan0.1%ofthemarket—withabout7000hybridcarsregisteredin
2018[17]. ArecentreportbyCanivel[18]presentedhowKiaPhilippinesshowedasteady
increaseinthepurchaseofhybridcarsduetoincreaseinfuelcosts. Theonceaffordable
dieselfuelisnowrelativelynotthatcheapinthemarket. ItwasreportedthatKiawasable
toincreaseitssalesby14.6%in5months’timeofthesameyear. Kampialsoexpecteda
riseinsalesof17%in2021. AreportbyStatistaresearchdepartment[19]summarizedthe
hybrid/electriccarssoldfrom2020–2022. From378in2020to843in2021,asignificant
increasewasseenin2022with1013unitsbeingsold. Onereasonwhyhybridcarsarenot
highlypopularizedinthecountryistheirmaturityinthePhilippinecarmarket,leadingto
lowadoptionratesofhybridcars[20]. Asreportedbythenews[21],onlyrecently(2023)
hastherebeenanyplanstoputupchargingstations. Itwasreportedthat200charging
stationsareplannedtobeestablishedand500moreby2025. Therefore,theneedtoexplore
thepurchasingintentionsofconsumerswiththisrelativelynewtechnologyforthecountry
is needed. The slow progression of movement in purchase may be capitalized by the
governingunitssincetheestablishmentofchargingstationsandbusinessarestillonthe

WorldElectr.Veh.J.2023,14,227 3of26
rise. Thedeterminationofpurchasingintentionsurroundingthesehybridcarswouldbe
beneficialfortheliteratureandbusinessownersalike.
Thispaperaimedtodeterminewhatfactorsinfluencedrivers’preferencesforfuture
use and purchase intentions of hybrid vehicles (HVs) in the Philippines. Through the
integration of the extended pro-environmental theory of planned behavior (PEPB) of
Germanetal.[22]andtheextendedunifiedtheoryofacceptanceanduseoftechnology
(UTAUT2)onhybridcarpurchaseandusageintention,thisstudyisoneofthefirstfew
thatexaminedtheMLAapproachtobehavioralintention. Sincethecurrentstudyextended
the established purchasing intention of hybrid cars in the Philippines [15], this study
wantedtoaddtotheliteratureonclosingthegapbetweentheuseofmachinelearning
and analyzing human behavior. Structural equation modeling was considered by the
previousstudy[15], whichsuggestedtheuseofmachinelearningtobetteranalyzethe
nonlinearrelationshipamonglatentvariables. Inaccordance,theliterature,suchasthat
ofFanetal.[23],explainedthatsomelatentvariableswhenmediatingfactorsarepresent
maycauselittletonosignificance. Inaccordance,thestudyofWoody[24]alsopresented
similarfindingsandexplainedthatlargenonlinearrelationshipmodelsmaybeunreliable
whenSEMisusedasHeywoodcasesmightbepresentwhichmaycausewrongparameter
estimates[23,25]. Therefore,thisstudycontributestoamorethoroughevaluationofthe
Philippines’capabilitytosustainsmarttechnology—eventuallydevelopingintoasmart
andsustainablecity.
2. ConceptualFramework
2.1. TheoriesandRelatedStudies
Venkatesh et al. [11] extended the existing UTAUT by incorporating three latent
variables,namelyhedonicmotivation,pricevalue,andhabit,thusdevelopingtheUTAUT2
model.TheextensionsproposedintheUTAUT2producedasignificantimprovementinthe
varianceexplainedinbehavioralintentionandtechnologyusecomparedtoitspredecessor,
theUTAUT.AlthoughtheUTAUT2modelcomprehensivelyanalyzestheconstructsfor
theadoptionofnewtechnology, thescopeofthemodelonlyevaluatestheintentionto
usenewtechnologies,makingitinsufficientintermsofholisticallymeasuringthehuman
behaviorattributesandaspects[26]. LaRoseetal.[27]suggestedthattheUTAUT2model
employsgenericmeasuresofthelatentvariablessothatthesameoperationalstandards
canbeusedacrossdifferentstudies. Thisapproachimprovedthemodel’sgeneralizability
butcompromisedtheactionableinformationgathered. Inaddition,Ongetal.[26]stated
thattheUTAUT2modelwasnotabletoanalyzetheactualbehaviorofadoptingtechnology.
Theirstudyrecommendedincorporatingotherfactorsinordertoobtainamoreaccurate
depictionoftheviewpointofthegeneralpopulationinlightoftheseminorinformational
gapsintheresearch. Subsequently,theirstudyalsoshowedthatdemographicfactorsas
mediatingeffectsmightnotbeconsideredinananalysis.
SeveralstudieshaveintegratedtheUTAUT2modelwithothertheoriestoevaluate
innovative solutions and technology. Yuduang et al. [28] considered the integration of
ProtectionMotivationTheory(PMT)andUTAUT2toassesstheactualusageandintention
to use new technologies, specifically mobile applications. Their study stated that this
integrationcouldbeinterpretedasamodelthatcancomprehensivelyassesstheintention
andactualusageofamobileapplication. Hassanetal.[29]integratedthePrivacyCalculus
Model(PMC)andUTAUT2byaddingfourconstructs: privacyconcern,perceivedrisk,
trust,andperceivedcredibility. Theirstudyvalidatedthattheadditionoftheseconstructs
thoroughly measured the consumers’ perspectives in relation to the adoption of new
technologies. Changetal.[30]extendedtheUTAUT2model,whichassimilatestheexisting
constructsfromtheUTAUT2alongwithage,gender,andexperienceasmoderators. Their
study highlighted three findings: (1) age and experience reduce the impact of habit on
usagebehavior,(2)ageaffectstheinfluenceoffacilitatingconditionsonusagebehavior,and
(3)themoderatingeffectofexperiencereducedthedirectimpactofbehavioralintentionon
usagebehavior,makingitirrelevant.

WorldElectr.Veh.J.2023,14,227 4of26
TheTheoryofPlannedBehavior(TPB)wasestablishedtoanticipatehumanbehavior.
AccordingtotheTPB,behavioralintentionisinfluencedbythreefactors: attitude(AT),
subjectivenorm(SN),andperceivedbehavioralcontrol(PEC)[31]. InthestudyofChau
andShiau[32],sixwell-knowntheoreticalmodelswereusedtohaveabetterunderstanding
oftermsofbehavioralintention,includingtheTPBandfiveothermodels,namelyService
Quality(SQ),Self-Efficacy(SE),MotivationalModel(MM),TechnologyAcceptanceModel
(TAM),andInnovationDiffusionTheory(IDT);thus,theunitedmodelgaveathorough
grasp of the aspects that have a significant impact on behavioral intention. With that,
theTPBistobeproveneffectivewhencombinedwithothermodels. Itprovidesamore
comprehensive review of a person’s behavioral intention concerning hybrid cars with
referencetothesaidstudy. InthepaperofSentosa[33],theTPB,alongwithTechnology
AcceptanceModeling(TAM),wasintegrated.Infulfillmentofthepaper,itwasimpliedthat
aperson’sconductisinfluencedbythedesiretoexecutetheactivity,whichisdetermined
byone’sattitudetowardthebehaviorandsubjectivenorm.
KimandHwang[34]usedaresearchmodelthatcombinedtheTPBandNormActiva-
tionModel(NAM)intoasingletheoreticalframeworktoanalyzeeco-friendlybehavioral
intentionstoemploydronefooddeliveryservices. Furthermore,themoderatinginfluence
ofproductknowledgewasinvestigatedinthisstudy,astheamountofproductknowledge
hasamajorimpactoncustomerbehaviors. PEPBandSERVQUALmodelswereintegrated
to further determine Filipino consumers’ behavioral intention in the paper of German
etal.[22],particularlyduringtheCOVID-19pandemic. Inrelianceonthesaidstudy,since
itwasmentionedthatthePEPBplacesemphasisonenvironmentalconcernsandauthority,
variables from the TPB play a role in determining an individual’s behavioral intention
towardsaparticularsituationoractivity. Additionally,thetwomodelsalsoindicateda
higher level of investigation. They can be used in developing countries like the Philip-
pinesbecausethesaidcountrystronglyencouragestheemergenceofmoresustainable
smarttechnology.
ThePEPBmodelwasdevelopedasanextensionofthetheoryofplannedbehavior
(TPB)sinceitcouldnotaddressallfactorsrelevanttothisstudy[22]. Perceivedauthor-
itysupport(PAS),perceivedenvironmentalconcern(PEC),perceivedbehavioralcontrol
(PBC),subjectivenorm(SN),attitude(AT),andbehaviorintention(BI)wereimportantin
determiningtheconsumer’sintentiontopurchaseproducts. Furthermore,othervariables
underthethreesustainabilitydomains,namelyeconomic,environmental,andsocial,are
coveredinthisstudy[35].
From the PEPB model [22], no economic aspects were covered. In line with the
objectiveofthisstudy,naturalresourcessuchasoilcannotbereplenishedrapidlyenough,
whichimpactstheeconomy[36]. Fossil-fueledcarsareknownforproducinglargeamounts
oftoxicairpollutantsintheatmosphere[37]. ThisincreaseinCO2intheatmospherewill
raisetheaveragetemperatureoftheearth’ssurface[38]. Inordertoreduceairpollution,
analternativemustbeused. Asimetal.[39]foundthathybridcarsarelessharmfulto
the environment because they use less gasoline. This shows that hybrid cars are much
cleanerandbetterfortheenvironment;nevertheless,aconsumer’sinterestdoesnotinclude
economicorenvironmentalconcerns[40]. Anindividual’schoiceofhybridcarsmayvary
dependingontheirsocialenvironmentperspective. Forinstance,aconsumer’sdecisionto
buyahybridcarmaypossiblybeinfluencedbytheirfamily,relatives,orfriends[41].
The researchers utilized the Unified Theory of Technology Acceptance and Use of
Technology2(UTAUT2),thePro-environmentalTheoryofPlannedBehavior(PEPB),and
sustainabilitydomainswhileincorporatinganadditionalfactorwhichisperceivedeco-
nomicconcerns(PECCs)tomeasurehumanbehaviorandtechnologyacceptance. Turon´
andKubik[42]studiedtheeconomicconsiderationsofadoptingautonomousvehiclescom-
paredtothetraditionalautomobilefleetacquiredbyindividualconsumersincar-sharing
systems. Inadifferentscope,Nisaetal.[43]revealedthatperceivedeconomicriskcon-
sistentlypredictedmitigationbehaviorandpolicysupport,andeconomicconsiderations
positivelypredictedalloutcomes. Hence,theaddedfactor,perceivedeconomicconcerns

World Electr. Veh. J. 2023, 14, x FOR PEER REVIEW 5 of 27
The researchers utilized the Unified Theory of Technology Acceptance and Use of
Technology 2 (UTAUT2), the Pro-environmental Theory of Planned Behavior (PEPB), and
sustainability domains while incorporating an additional factor which is perceived eco-
nomic concerns (PECCs) to measure human behavior and technology acceptance. Turoń
and Kubik [42] studied the economic considerations of adopting autonomous vehicles
compared to the traditional automobile fleet acquired by individual consumers in car-
sharing systems. In a different scope, Nisa et al. [43] revealed that perceived economic risk
consistently predicted mitigation behavior and policy support, and economic considera-
tions positively predicted all outcomes. Hence, the added factor, perceived economic con-
WorldElectr.Veh.J.2023,14,227 5of26
cerns (PECCs), relates to a sense of social responsibility, extensive societal and commercial
consideration, and voluntary company involvement.
(PECCs),relatestoasenseofsocialresponsibility,extensivesocietalandcommercialcon-
2.2. Conceptual Framework
sideration,andvoluntarycompanyinvolvement.
The Sustainability Theory of Planned Behavior (STPB) framework used in this study
(2F.2ig. Cuorne c1ep) teunalcoFrmampeawssoreks the combination of the TPB and the PEPB with the UTAUT2 and
the eTxhteenSsuiostna inoaf btihliet yeTcohneoormyiocf fPalcatnonre. dSeBveehraavli ovra(rSiTaPbBle)sf,r ainmceluwdoirnkgu hseadbiint (tHhiBs)s,t updryice value
((PFiVgu),r hee1d)oenncioc mmpoatsisveastitohen c(oHmMbi)n, apteiornfoorfmthaencTeP BexapnedctthanecPyE P(PBEw),i tehfftohret UexTpAeUcTta2nacnyd (EE), fa-
theextensionoftheeconomicfactor. Severalvariables,includinghabit(HB),pricevalue
cilitating conditions (FCs), perceived authority support (PAS), perceived environmental
(PV), hedonic motivation (HM), performance expectancy (PE), effort expectancy (EE),
concern (PENC), perceived behavioral control (PBC), perceived economic concern
facilitatingconditions(FCs),perceivedauthoritysupport(PAS),perceivedenvironmental
(PECC), subjective norm (SN), attitude (AT), and behavioral intention (BI) were taken into
concern(PENC),perceivedbehavioralcontrol(PBC),perceivedeconomicconcern(PECC),
account to comprehensively analyze the intention to use and actual purchase intention of
subjectivenorm(SN),attitude(AT),andbehavioralintention(BI)weretakenintoaccountto
ccoomnspurmeheernss’i vtoelwyaanrdal yhzyebtrhied incaternst. ioTnhitso fursaemanedwaocrtku awlpaus rachdaospetiendte fnrtoiomn othfceo sntsuudmye rosf’ Ong et
atol.w [a1r5d].h ybridcars. ThisframeworkwasadoptedfromthestudyofOngetal.[15].
FFiigguurree 11..S Suusstataininabaibliitlyittyh ethoreyoroyf polfa npnlaendnbeedh abveihoravfriaomr efwraomrkewwiotrhkU wTAithU TU2T.AUT2.
TheUTAUT2modelcanmeasuretheindividual’sintentiontousehybridcars. Inthis
study,anewframeworkwasestablishedinwhichthesocialinfluence(SI)wastransferred
tothePEPBmodelassubjectivenorm(SN).ThisisduetothePEPBhavingasubjective
norm(SN)variable,wheretheyofferedthesamebehavioralaspectbasedontheinfluence
ofotherpeople.

WorldElectr.Veh.J.2023,14,227 6of26
Habitisrepeatedlydescribedasaresultofearlierexperienceswithnumerousfactors,
whichbecomesabeneficialchoice[11]. Itisalsoconsideredapotentialfactorindecision
making[44]. Positivefeelingsassociatedwiththehabitualproductexperienceofdriving
acarstrengthensthehabitanddiscouragesconsumersfromembracinganewmeansof
transportation,suchashybridcars[45,46]. Additionally,theadoptionofanewcarmaybe
influencedbypreviousexperiencewithsimilarcars[47]. Thus,itwashypothesizedthat:
H1. Habithasasignificantdirecteffectonbehavioralintention.
Thetermpricevalue(PV)referstoconsumers’cognitivetrade-offbetweentheper-
ceived advantages of the applications and the financial expense of utilizing them [11].
Moreover,theadvantagesandassociatedexpensesofpurchasinghybridcarswereassessed
andcontrasted[48]. Irawanetal.[4]observedthatgaspriceandsupplyaffectedtheutility
ofhybridcarssignificantly;thissuggeststhatconsumersaremorelikelytoacquireahybrid
cardependingonthefuelcostandsupply. Thus,itwashypothesizedthat:
H2. Pricevaluehasasignificantdirecteffectonbehavioralintention.
Venkateshetal.[11]definedhedonicmotivationasthefunorpleasurederivedfrom
using technology. It also makes an individual feel better since it is a crucial factor in
consumerchoicetopurchasehybridcars[49–51]. Thus,itwashypothesizedthat:
H3. Hedonicmotivationhasasignificantdirecteffectonbehavioralintention.
According to Venkatesh et al. [11], performance expectancy (PE) is the degree of
personalbeliefthatemployingcollaborativetechnologywouldincreaseworkefficiency
andresultinoperationalsuccess.Additionally,ifcustomersfindasimplesystemtobeused,
itwillbemoreaccepted[52]. Thiscouldbeafactorinencouragingpeopletopurchase[53].
Thus,itwashypothesizedthat:
H4. Performanceexpectancyhasasignificantdirecteffectonbehavioralintention.
Effort Expectancy (EE) relates to the level of ease connected with the use of the
system. ThedefinitionofEEdiscussestheeffortrequiredtobecomeskillfulwhenutilizing
technology. ThismethodiscomparabletotheideaofDavis[54]ofperceivedeaseofuse,
whichaddressestheextenttowhichpeoplethinkutilizingtechnologydoesnotinvolve
much effort [55]. Ombach [56] concluded that developed technologies are efficiently
integratedwithseveralvehicles. Thus,itwashypothesizedthat:
H5. Effortexpectancyhasasignificantdirecteffectonbehavioralintention.
FacilitatingConditions(FCs)aresaidtobethedegreetowhichapersonfeelsthata
technologicalandorganizationalinfrastructureexiststoenabletheusageofthesystem[57].
FC affects people’s perception of infrastructures, technical support, and other facilities
whentheyutilizetechnology,products,andservices. InthepreviousUTAUTmodels,FC
wastheorizedasanoperatorofuserbehavior. Thismeansthatusersaremorelikelyto
usenewtechnologyifthereareavailableresources,expertise,andsupport[58]. Dueto
this,nationalpolicyactionsarerequiredtopromotethecommercializationoflow-carbon
technology (i.e., hybrid cars) in both advanced and especially developing nations like
thePhilippines[53]. Inaddition,FCispresumedtobeanessentialvariableinfluencing
behavioralintentionintheUTAUT2framework[11,59]. Thus,itwashypothesizedthat:
H6. Facilitatingconditionshasasignificantdirecteffectonbehavioralintention.
AstudybyWangetal.[8]revealedthatthetheoryofplannedbehavior(TPB),together
withitsprimaryconstructs,wasfoundtopredictbehavioralintentionsaccurately. Attitude
is characterized as the positive or negative evaluation of the adoption behavior. Social
influenceorsubjectivenormreferstotheperceivedsocialpressureanindividualfeelsfrom
others. Perceivedbehavioralcontrolwasdefinedasthelevelofperceivedeaseordifficulty
withregardtoengaginginthebehavior. Hybridelectricvehicleshavebeenregardedas
a potential solution to the pressure of lowering carbon emissions in the transportation

WorldElectr.Veh.J.2023,14,227 7of26
industry—affectingconsumers’behavioralintentionsonadoptinghybridcars. Tanwirand
Hamzah [7] integrated the theory of planned behavior with environmental knowledge
as the foundation of their research model to examine the factors influencing people’s
intention to buy a hybrid car. They found that people’s perceptions of their ability to
manageresourcesarethemostsignificantpredictorsoftheirintentiontopurchasehybrid
vehicles. Thus,itwashypothesizedthat:
H7. Subjectivenormhasasignificantdirecteffectonbehavioralintentions.
H8. Attitudehasasignificantdirecteffectonbehavioralintentions.
H9. Perceivedbehavioralcontrolhasasignificantdirecteffectonbehavioralintentions.
AccordingtoLinetal.[60],theperceivedenvironmentalconcerns(PENCs)latentvari-
ablefunctionsastheantecedentofthesubjectivenorm(SN),attitude(AT),andperceived
behavioralcontrol(PBC)variablesinthePEPBmodelofGermanetal.[22]. Caremissions
raisequantitiesofcarbondioxideandothergreenhousegaseswhiletrappingthesun’sheat
intheEarth’satmosphere,whichcausesglobalwarming. Intheyear2020,transportation
passengercarscontributetoaround41%ofworldwidecarbonemissions[1]. Thereisan
apparent need for alternatives or modifications that would better sustain the means of
transportationandautomotiveindustryproductionsnationwide,suchasdevelopingan
electriccar,butmoreopenandaccessibletothegeneralpublicandmoreethicallypriced,
particularlyhybridcars[61].Raczetal.[62]conductedastudyontheecologicalperspective
ofhybridcars. Theirresultsrevealedthatthemodernconceptofaneco-friendlycarisa
strongstartforahealthierenvironment,butatthesametime,batteryrecyclingrequires
greater focus because the advantages of electric batteries are generally acknowledged,
whilethedrawbacksofrecyclingarefrequentlyignored. Thus,itwashypothesizedthat:
H10. Perceivedenvironmentalconcernshaveasignificantdirecteffectonsubjectivenorm.
H11. Perceivedenvironmentalconcernhasasignificantdirecteffectonattitude.
H12.Perceivedenvironmentalconcernshaveasignificantdirecteffectonperceivedbehavioralcontrol.
Tothoroughlyexaminetheadoptionpotentialofhybridcars,theresearchersestab-
lishedtheSTPBmodelinaccordancewiththesustainabilitydomains. Thelatentvariable
perceived economic concerns (PECCs) was added. Barbosa Junior et al. [63] presented
theeconomicdimensionofthefinancialviabilityofprovidingproductioncontinuitywith
economicresourcesobtainedthroughsustainablepractices. Theirresearchidentifiedthree
barriers: low financial return, financial incentive, and financial viability. Social factors
arestronglyrelatedtosurveyrespondents’adoptionofsustainablepractices. Similarly,
economicconcernsorperceivedeconomicconcernsdirectlyimpactsubjectivenormand
attitude. Economic efficiency was used as an independent variable in a study by Saif
etal.[64]topredicttheintentiontoadoptdigital-onlytechnology. Itwasdefinedascus-
tomers’ perceptions of being able to save time, effort, and financial resources by using
theservices. Accordingtotheirfindings,perceivedconvenienceandperceivedeconomic
efficiencyhaveasignificantpositiveeffectontheusageintention,whichwouldsufficethe
significantdirecteffectPECChasonperceivedbehavioralcontrol. Thus, thefollowing
werehypothesized:
H13. Perceivedeconomicconcernshaveasignificantdirecteffectonsubjectivenorm.
H14. Perceivedeconomicconcernshaveasignificantdirecteffectonattitude.
H15. Perceivedeconomicconcernshaveasignificantdirecteffectonperceivedbehavioralcontrol.
InastudybyGermanetal.[22]utilizingthepro-environmentaltheoryofplanned
behavior(PEPB)model,perceivedauthoritysupport(PAS)referstoanindividual’sper-
ception of any resources, regulations, processes, or actions delivered by a government
orauthorityorganizationthatcanassistpeopleincarryingoutaparticularactivity. The
Philippines’policiesandprogramsareaimedatpreventingthedepletionofenvironmental

WorldElectr.Veh.J.2023,14,227 8of26
resources,whichinvolvesreducingenergyuse,chlorofluorocarbons,andcarbondioxide
emissions[65]. Thegovernment’sinitiativetosupervisethetransitionfromfossil-fueled
carstohybridcarsisexpectedtohaveanimpactonconsumers’purchaseintentiontoward
hybrid cars [66]. According to Lin et al. [60], support from the government has a posi-
tiveandsubstantialeffectonsubjectivenorm,attitude,andperceivedbehavioralcontrol,
demonstratingthatthegovernmenthasasignificantimpactonitspopulation. Thus,itwas
hypothesizedthat:
H16. Perceivedauthoritysupporthasasignificantdirecteffectonsubjectivenorm.
H17. Perceivedauthoritysupporthasasignificantdirecteffectonattitude.
H18. Perceivedauthoritysupporthasasignificantdirecteffectonperceivedbehavioralcontrol.
3. Methodology
3.1. Participants
TheresearchersconductedanonlinesurveytopredictFilipinos’purchasingintentions
forhybridcars. Non-probabilitysamplingmethodswereutilizedtogathertherespondents
forthestudy. AccordingtoGalloway[67],conveniencesamplingcanhelpgatheravariety
ofattitudesandopinionsaswellasidentifytentativeideas. Thatbeingso,theconvenience
samplingmethodwasused. Meanwhile,snowballsamplingwasalsoemployedtoreach
thetargetednumberofparticipantswiththehelpofeachone’ssocialnetwork[68]. The
researchersobtainedmorethan500respondents,generalizingthestudy’sresults[69]. Since
theself-administeredsurveywasopentothegeneralpublic,therespondentsanswered
attheirdiscretion. Atotalof 1149responseswereaccumulated(Table1), but1048was
the number of responses considered since 101 participants did not possess a driver’s
license—theinstrument’sprimaryqualification. Thisresultedina91.21%validresponse
ratewithnomissingdata—similartotheadopteddatafromOngetal.[15].
Table1.Respondents’descriptivecharacteristics(n=1048).
| Characteristics | Category | N   | %    |
| --------------- | -------- | --- | ---- |
|                 | Female   | 146 | 13.9 |
Gender
|     | Male  | 902 | 86.1  |
| --- | ----- | --- | ----- |
|     | 17–22 | 5   | 0.48  |
|     | 23–29 | 341 | 32.54 |
|     | 30–36 | 365 | 34.83 |
Age
|                      | 37–43             | 192  | 18.32 |
| -------------------- | ----------------- | ---- | ----- |
|                      | 44–50             | 97   | 9.26  |
|                      | 51–60             | 48   | 4.58  |
|                      | Lessthan20,000    | 42   | 4.01  |
|                      | 20,000–30,000     | 310  | 29.58 |
|                      | 30,000–40,000     | 495  | 47.23 |
| MonthlyIncome/Salary | 40,000–50,000     | 113  | 10.78 |
|                      | 50,000–60,000     | 52   | 4.96  |
|                      | Greaterthan60,000 | 34   | 3.24  |
|                      | Others            | 2    | 0.19  |
|                      | Employed          | 1035 | 98.76 |
|                      | Self-employed     | 8    | 0.76  |
| Occupation           | Unemployed        | 1    | 0.1   |
|                      | Retired           | 0    | 0.0   |
|                      | Student           | 4    | 0.38  |
|                      | Married           | 553  | 52.77 |
|                      | Single            | 487  | 46.47 |
MaritalStatus
|     | Widowed   | 4   | 0.38 |
| --- | --------- | --- | ---- |
|     | Separated | 4   | 0.38 |

WorldElectr.Veh.J.2023,14,227 9of26
Table1.Cont.
| Characteristics       |                              | Category    | N   | %     |
| --------------------- | ---------------------------- | ----------- | --- | ----- |
|                       | Elementarygraduate           |             | 2   | 0.19  |
|                       | Juniorhighschoolgraduate     |             | 1   | 0.1   |
|                       | Seniorhighschoolgraduate     |             | 4   | 0.38  |
| EducationalAttainment | Technical–VocationalGraduate |             | 2   | 0.19  |
|                       | CollegeGraduate              |             | 992 | 94.66 |
|                       | MasterGraduate               |             | 45  | 4.29  |
|                       |                              | PhDGraduate | 2   | 0.19  |
|                       |                              | Urban       | 866 | 82.63 |
Residence
|                       |                   | Rural  | 182 | 17.37 |
| --------------------- | ----------------- | ------ | --- | ----- |
|                       | Ownedhouseandlot  |        | 566 | 54.01 |
|                       | Ownedanapartment  |        | 25  | 2.39  |
| TypeofResidentialHome | Ownedacondominium |        | 10  | 0.95  |
|                       |                   | Rental | 395 | 37.69 |
|                       |                   | Others | 52  | 4.96  |
|                       |                   | Yes    | 636 | 60.69 |
Doyouhavecarinsurance?
|     |     | No  | 412 | 39.31 |
| --- | --- | --- | --- | ----- |
3.2. Questionnaire
Aquestionnairewith13distinctportionsandfouritemseachwasadaptedfromthe
relatedliterature[15]. Participantswereaskedtoratehowmuchtheyagreedordisagreed
withthegivenstatementona5-pointLikertscaletogatherinformationforthisstudy.
DatapreprocessingwasperformedpriortointegratetheMachineLearningAlgorithm
(MLA).SPSS25wasutilizedtoexaminethemissingdata. Forthedatacleaningprocess,
nonsignificantindicatorswithap-valuemoresignificantthan0.05wereremovedfromthe
datausingcorrelationanalysis. Similarly,fortheMLAoptimization,onlytheindicators
withavaluehigherthan0.20correlationcoefficientwereconsidered. Sincenoneofthe
indicationswereremoved,allproposedindicatorsweredeemedsignificant.
TorepresenttheinputfortheMLA,thevariousindicatorswereaveragedthroughdata
aggregation. Theimplicationsinthequestionnaireportraythelatentfactorsthatwereun-
observedvariablesandweretakenintoaccountinthisstudyfortheMLAutilizingPython
3.8, specifically Spyder 3—an integrated development environment. Other algorithms,
suchasthedecisiontree(DT),therandomforestclassifier(RFC),andthedeeplearning
neuralnetwork(DLNN)wereusedafterdatanormalizationtopredictthefactorsaffecting
theacceptanceofhybridcarsamongFilipinodrivers.
3.3. DecisionTree
A decision tree is a structure and classification approach with regression capacity
appliedasapredictionfactorinaclusterofindependentvariables[70]. Thisstructureis
labeledasaprimaryclassifierofdecisionnodesorganizedinatreepattern[71]. Theyare
easilyinterpretableandvisuallyportrayedashierarchicalstructures[72]. Additionally,
decision trees are often employed in model classification in data mining [73]. Milani
etal.[74]alsostatedthatDTiswidelyrecognizedasoneofthemosteffectivemethods
for dealing with nonlinear datasets. Since decision trees study a nonlinear dataset for
understanding human features and behavior [75], this approach can be applied to the
currentstudy.
BasedonthestudyofTopîrceanuandGrosseck[76],MLArecognizesdecisiontreesas
oneofitsclassificationtools.Itcategorizesrelevantlatentvariablesthatimpactadependent
factorbyevaluatingtherelationshipbetweenfactorsrepresentedbytreebranches. Their
studyalsostatedthatDTsareapredictivemodelforhumanbehaviorregardlessofthe
targetvariable’squantity. Furthermore,DTsareutilizedtodevelopapredictionmodel
formultipleclass(dependentfactor)labelsindomainssuchashealthcare,humanfactors,
manufacturing,andotherfields[77].

WorldElectr.Veh.J.2023,14,227 10of26
InconjunctionwithestablishingtheEntropyandGiniindexvaluesalongsidebestand
randomsplitters,varioustestingandtrainingratioswereappliedtotheDTclassification
process, such as the 40:60, 50:50, 60:40, 70:30, 80:20, and 90:10 training-to-testing ratios.
FollowingthestudyofChenetal.[78]thetreedepthwasevaluated,spanningfromfourto
seven. Theidealdecisiontreewasdeterminedbyrunningeachcombination100timesfora
totalof9600runs. Thesplitter(RandomorBest),trainingandtestingratios,treedepth,and
thecriterion(GiniorEntropy)werealldeterminedusingtheanalysisofvariance(ANOVA)
toevaluatetheidealdecisiontree.
3.4. RandomForestClassifier
Therandomforestclassifierisasupervisedclassificationalgorithmthatcategorizes
data by creating several classifiers to attain greater prediction accuracy [79]. The basic
decision tree generates a large number of branches; therefore, RFC classifies the most
satisfactory decision tree using several characteristics and creates the best branch split
amongthedecisiontrees[80]. TheprimarygoalofemployingtheRFCasMLAistolocate
the best tree with a high accuracy rate. The random forest classifier evaluates the best
tree for each iteration, whereas the standard DT generates a random tree for each run.
Chen et al. [81] supported the claim that the random forest classifier is the best among
other decision trees. According to the study of Rodriguez-Galano et al. [82], RFCs are
farmoreaccurateandresistanttonoisethansingleclassifiers(i.e.,basicdecisiontrees);
hence,ensemblelearningalgorithmslikerandomforest,bagging,andboostingaregaining
popularity. InthepaperofElhenawyetal.[83]andErmagunetal.[84],theRFCwasused
topredicthumanbehavior,specificallydrivingbehavior. Thus,thesameclassificationtool
wasappliedinthecurrentinvestigation. Similaroptimizationparameterswereutilizedin
thestudy,aspresentedintheDTsections.
3.5. DeepLearningNeuralNetwork
Comparedtoothermachinelearningandartificialintelligenceapplications,thedeep
learningneuralnetwork(DLNN)isrecognizedasthebestmodelforpredictingparameters
oridentifyingpatternsbecauseofitscapacitytoassessandcalculatemanyperceptions[26].
Cassini[85]statedthatthisalgorithmhassignificantadvantagesoverconventionalmachine
learning algorithms (MLAs) in extracting features at various levels of abstraction and
therebylearningmorecomplexpatterns. Furthermore,deeplearningneuralnetworksare
artificial neural networks with additional hidden layers between the input and output
layers, wherein Ong et al. [26] explained how these can assess nonlinear relationships
amongframeworksdeveloped. AccordingtoSturmanetal.[86],thevariationbetweenand
amonghumanannotatorsiseliminatedbythedeepneuralnetwork,whichoutperforms
commercialsystemsatalowercostandcontributestotheenhancementofbehavioraldata
quality and accuracy. Luceri et al. [87] affirmed that the deep learning neural network
effectivelyevaluatesthepsychologicalbehavior,behavioralintention,andpsychologyof
consumers. Inthisstudy,theresultsobtainedfromtherandomforestclassifierwouldbe
supportedbyuseofthedeeplearningneuralnetworksincethismethodcanpredictand
categorizethemostinfluentialfactorsaffectingthebehavioralintentionofconsumersin
purchasinghybridcars.
Similartothesetconditionswitharandomforestclassifier,thedeeplearningneural
network preprocessing incorporated correlation analysis for data cleaning. Following
datanormalization,variousactivationfunctionsforthehiddenlayer(sigmoid,tanh,and
swish),outputlayer(sigmoid),andoptimizer(Adam,SGD,RMSProp)weretakeninto
consideration[80]. Additionally,thenumberofnodesforthe80:20trainingandtesting
ratiowasalsoincludedusingafeed-forwardneuralnetworkprocess. Atotalof6480runs
wereconducted,setwith150epochsperiteration[88].

WorldElectr.Veh.J.2023,14,227 11of26
4. Results
4.1. DecisionTree
Iterationsofthedifferentcombinationsofparametersinthebasicdecisiontreewere
accomplishedtogeneratethebestoutput. PresentedinTable2arethesummarizedresults.
It could be posited that at depth 5, the most consistent tree output based on standard
deviationwasproducedwithGiniandbestassplitterandcriterion. Thoughentropyand
besthadhigheraccuracyrates,asignificantdifferencewasnotevident. Inaddition,the
accuracyratesunderGiniandbesthadhigheraccuracyrates.
Table2.DecisionTreeSummarizedResults.
| Category | 60:40 | 70:30 | 80:20 | 90:10 |
| -------- | ----- | ----- | ----- | ----- |
Random
| Gini              | 65.54 | 67.16 | 65.16 | 67.20 |
| ----------------- | ----- | ----- | ----- | ----- |
| StandardDeviation | 2.051 | 2.214 | 2.344 | 3.117 |
| Entropy           | 65.42 | 67.00 | 65.29 | 67.61 |
| StandardDeviation | 1.962 | 2.168 | 2.384 | 3.512 |
Best
| Gini              | 70.18 | 68.15 | 67.06 | 72.00 |
| ----------------- | ----- | ----- | ----- | ----- |
| StandardDeviation | 0.389 | 0.642 | 0.639 | 0.000 |
| Entropy           | 67.00 | 69.49 | 68.00 | 72.32 |
| StandardDeviation | 0.000 | 0.503 | 0.000 | 0.471 |
ThestudyofGermanetal.[22]presentedthattheselowaccuracyratesfromthebasic
decisiontreewereduetothefactthatitgeneratesrandomtreeseveryiteration. Itwas
proposedthatarandomforestclassifierbeused. Inthiscase,therandomforestclassifier
findsthebesttreeoutputeveryiteration,whichinturnconsidersahigheraccuracyrate.
StudiessuchasthatofOng[80]andChenetal.[81]presentedthesamediscussionand
justifiedhowtherandomforestclassifiercanpresenttheoptimumtreeoutput.
4.2. RandomForestClassifier
PresentedinTable3arethesummarizedresultsoftherandomforestclassifier. Fol-
lowingrelatedstudies[22,80,81],higheraccuracyrateswereevidentintherandomforest
classifier output compared to the basic decision tree. Similar to the basic decision tree,
depth5presentedthemostconsistentoutputwithGiniandbestastheparameters.
Table3.RandomForestClassifierSummarizedResults.
| Category | 60:40 | 70:30 | 80:20 | 90:10 |
| -------- | ----- | ----- | ----- | ----- |
Random
| Gini              | 81.82 | 80.69 | 83.22 | 85.38 |
| ----------------- | ----- | ----- | ----- | ----- |
| StandardDeviation | 4.896 | 3.668 | 5.904 | 4.582 |
| Entropy           | 82.85 | 80.36 | 84.43 | 83.69 |
| StandardDeviation | 3.300 | 3.976 | 5.028 | 6.238 |
Best
| Gini              | 88.74  | 84.06 | 92.55 | 94.00 |
| ----------------- | ------ | ----- | ----- | ----- |
| StandardDeviation | 0.7115 | 1.003 | 0.500 | 0.000 |
| Entropy           | 83.63  | 84.98 | 89.37 | 92.00 |
| StandardDeviation | 1.120  | 0.642 | 1.077 | 0.000 |

| World Electr. Veh. J. 2023, 14, x FOR PEER REVIEW  |     |     |     | 12 of 27  |
| -------------------------------------------------- | --- | --- | --- | --------- |

| Standard Deviation  | 0.389  | 0.642  | 0.639  | 0.000  |
| ------------------- | ------ | ------ | ------ | ------ |
| Entropy             | 67.00  | 69.49  | 68.00  | 72.32  |
| Standard Deviation  | 0.000  | 0.503  | 0.000  | 0.471  |
The study of German et al. [22] presented that these low accuracy rates from the basic
decision tree were due to the fact that it generates random trees every iteration. It was
proposed that a random forest classifier be used. In this case, the random forest classifier
finds the best tree output every iteration, which in turn considers a higher accuracy rate.
Studies such as that of Ong [80] and Chen et al. [81] presented the same discussion and
justified how the random forest classifier can present the optimum tree output.
4.2. Random Forest Classifier
Presented in Table 3 are the summarized results of the random forest classifier. Fol-
lowing related studies [22,80,81], higher accuracy rates were evident in the random forest
classifier output compared to the basic decision tree. Similar to the basic decision tree,
depth 5 presented the most consistent output with Gini and best as the parameters.
Table 3. Random Forest Classifier Summarized Results.
| Category  | 60:40  | 70:30  | 80:20  | 90:10  |
| --------- | ------ | ------ | ------ | ------ |
Random
| Gini                | 81.82  | 80.69  | 83.22  | 85.38  |
| ------------------- | ------ | ------ | ------ | ------ |
| Standard Deviation  | 4.896  | 3.668  | 5.904  | 4.582  |
| Entropy             | 82.85  | 80.36  | 84.43  | 83.69  |
| Standard Deviation  | 3.300  | 3.976  | 5.028  | 6.238  |
Best
| Gini                | 88.74   | 84.06  | 92.55  | 94.00  |
| ------------------- | ------- | ------ | ------ | ------ |
| Standard Deviation  | 0.7115  | 1.003  | 0.500  | 0.000  |
WorldElectr.Veh.EJ.n20t2r3o,p1y4, 227 83.63  84.98  89.37  92.00  12of26
| Standard Deviation  | 1.120  | 0.642  | 1.077  | 0.000  |
| ------------------- | ------ | ------ | ------ | ------ |
IItt ccoouuldldb bees eseenenf rformomth tehree sruesltuslttsh athtatht eth9e0 :1900:t1r0a itnrianingitnegs ttiensgtirnagti oraptiroo dpurocedducthede mthoes t
cmonossits ctoenntsitsrteeenwt tirtehe 9w4i%tha 9c4c%ur aacccyuarancdy aanstda na dstaarndddaervdi dateivoinatvioanlu veaolufe0 .o0f0 00..0T00h.u Tsh,uthsi, sthtries e
oturetep uotuwtpaust cwoanss icdoenrseiddethreedo tphteim oupmtimculamss icfilacsastiifoincamtioond eml.oFdieglu. rFeig2urreep 2re rseepnrtesstehnetso tphteim opu-m
ttriemeuwmit htreaer wanidtho am rafonrdeostmc lfaosrseisfite crl.assifier.

Figure2.OptimumTreewithRandomForestClassifier.
From the output, PENC (X ) dictated the behavioral intentions for acceptance of
1
hybrid cars. The tree will consider AT (X 0 ) for the first node. Then, it will consider X 0 ,
X (≤−0.412), and PBC (X ) with a value less than or equal to −0.909. Satisfying this
| 1   |     | 2   |     |     |
| --- | --- | --- | --- | --- |
(≤−0.412)condition
| condition,peoplewillhaveveryhighbehavioralintentions. |     |     | IftheX 1 |     |
| ----------------------------------------------------- | --- | --- | -------- | --- |
isnotsatisfied,onlyahighbehavioralintentionisseen. ThisindicatesthatPENCshould
behighlightedforpeopletohaveaveryhighorpositivebehavioralintention. Asimilar
outputisevidentifthefirstchildnodeconditionsarenotsatisfied.
If the parent node with a value less than or equal to 0.386 is not satisfied,
a 0.123condition for X first child node is considered. Satisfying this will consider X
0 1
and then PE (X 4 ) with a value less than or equal to −0.043, which will lead to a high
behavioralintention. ThispositsthatasPENCisinfluentialtothecontrolofanindividual
toaccepthybridcars,itsperformanceshouldalsobehighlightedasutilizationfortrans-
portation. Lastly,ifthechildnodeconditionsarenotsatisfied,itwillconsiderX ,thenX ,
2 1
andX ,whichwillleadtoveryhighbehavioralintentions.
0
Fromthefindings,itcouldbededucedthatPENCandATarethetopsignificantfactors
thataffectedpeople’sPBCandPEtohaveveryhighbehavioralintentionsforhybridcars.
ThisdictatesthatPBCandPEaresignificantfactorsaswellthatwouldinfluenceusers’
acceptanceofhybridcars. However,withvariedfactorsstillpresent,therandomforest
classifierneedsfurtherassistancefromotherMLAstoprovideadistinctclassificationof
latentvariablesaffectingbehavioralintentions. Chenetal.[81]consideredothertoolsin
supportofthefindingsoftherandomforestclassifiertodeducesignificantlatentvariables.
4.3. DeepLearningNeuralNetwork
Following the study of Ong et al. [75], deep learning neural network parameter
optimization was conducted to provide the optimum classification model. From the
differentparameterstested,tanh,astheactivationfunctionforthedifferenthiddenlayers,
presentedthebestoutput. Usingsigmoidastheactivationfunctionintheoutputlayerand
adamastheoptimizer,thesummarizedtrainingandtestingaverageresultsarepresented
inTable4.

WorldElectr.Veh.J.2023,14,227 13of26
Table4.Summarizedresultsfordeeplearningneuralnetwork.
Factor AverageTraining StandardDeviation AverageTesting StandardDeviation
| PENC | 91.41 | 1.630 |     | 93.14 |     | 1.681 |     |
| ---- | ----- | ----- | --- | ----- | --- | ----- | --- |
| AT   | 90.71 | 0.928 |     | 93.06 |     | 1.807 |     |
| PBC  | 80.95 | 1.663 |     | 89.84 |     | 2.631 |     |
| SN   | 80.70 | 0.143 |     | 87.29 |     | 2.997 |     |
| PE   | 81.12 | 1.071 |     | 83.14 |     | 2.285 |     |
| PAS  | 80.01 | 7.850 |     | 80.62 |     | 1.943 |     |
| FC   | 77.21 | 1.473 |     | 79.14 |     | 2.491 |     |
| HM   | 74.72 | 0.800 |     | 77.29 |     | 2.860 |     |
| EE   | 67.80 | 2.769 |     | 75.76 |     | 1.993 |     |
| PECC | 68.67 | 3.343 |     | 70.35 |     | 1.226 |     |
| PV   | 65.78 | 7.093 |     | 70.43 |     | 3.210 |     |
| HB   | 60.50 | 2.211 |     | 68.52 |     | 3.761 |     |
Tanhis anactivation functionthatis considered tobe anextensionof thesigmoid
function.Gudivada[89]explainedthatastretchedandshiftedsigmoidcalculationisseenin
thetanhactivationfunction. Thisisusuallyconsideredfornonlinearrelationshipmodels,
which can present high accuracy rates when used in the hidden layers. As explained
byWalraveetal.[90],tanhisanactivationfunctionwithstrongercomplexitytoupdate
weightsinneuralnetworkmodels,whichresultsinfasteroptimizationandhigheraccuracy
rates. TheequationoftanhispresentedinEquation(1)adoptedfromdeRycketal.[91].
2
|     |     | tanh(x) | =   | −1  |     |     | (1) |
| --- | --- | ------- | --- | --- | --- | --- | --- |
1+e−2x
Forsigmoid,Costarelli[92]explainedthatthisactivationfunctionismostlyutilized
in the output layer as it calculates nonlinear relationships with smaller ranges. Since
tanhwasconsideredwithseveralhiddenlayersinthisstudy,boundedvalueswouldbe
evidentaftertheprocess,whichcanbecomputedusingsigmoid[93]. Itisalsoarguedto
beefficientdespiteitssimplecalculation,whichiscommonlyutilizedwhenprobabilities
are considered. Equation (2) represents the sigmoid activation function adopted from
Narayan[94].
1
|     |     | sigmoid(x) | =   |     |     |     | (2) |
| --- | --- | ---------- | --- | --- | --- | --- | --- |
1+e−x
ThefinaldeeplearningneuralnetworkclassificationmodelispresentedinFigure3. A
totalofthreehiddenlayerswith50,50,and20nodes,respectively,providedtheoptimum
model.Witha96.60%accuracy,thescoreofimportanceusingSPSS25wasusedtoverifythe
outputofconsecutiverankingoffactorsaffectingtheacceptanceofhybridcars. Presented
inTable5isthenormalizedscoreoftheimportanceoftheresultingparameters.
Table5.Normalizedscoresofimportance.
|     | Factor |     | Importance |     | NormalizedImportance |        |     |
| --- | ------ | --- | ---------- | --- | -------------------- | ------ | --- |
|     | PENC   |     | 0.107      |     |                      | 100%   |     |
|     | AT     |     | 0.103      |     |                      | 96.32% |     |
|     | PBC    |     | 0.101      |     |                      | 94.50% |     |
|     | SN     |     | 0.099      |     |                      | 92.12% |     |
|     | PE     |     | 0.097      |     |                      | 90.20% |     |
|     | PAS    |     | 0.090      |     |                      | 84.50% |     |
|     | FC     |     | 0.087      |     |                      | 81.20% |     |
|     | HM     |     | 0.084      |     |                      | 79.00% |     |
|     | EE     |     | 0.083      |     |                      | 77.60% |     |
|     | PECC   |     | 0.082      |     |                      | 76.70% |     |
|     | PV     |     | 0.081      |     |                      | 76.20% |     |
|     | HB     |     | 0.076      |     |                      | 70.90% |     |

World Electr. Veh. J. 2023, 14, x FOR PEER REVIEW 14 of 27
to update weights in neural network models, which results in faster optimization and
higher accuracy rates. The equation of tanh is presented in Equation (1) adopted from de
Ryck et al. [91].
tanh(𝑥)= 2 −1 (1)
1+𝑒−2𝑥
For sigmoid, Costarelli [92] explained that this activation function is mostly utilized
in the output layer as it calculates nonlinear relationships with smaller ranges. Since tanh
was considered with several hidden layers in this study, bounded values would be
evident after the process, which can be computed using sigmoid [93]. It is also argued to
be efficient despite its simple calculation, which is commonly utilized when probabilities
are considered. Equation (2) represents the sigmoid activation function adopted from
Narayan [94].
𝑠𝑖𝑔𝑚𝑜𝑖𝑑 (𝑥)= 1 (2)
1+𝑒−𝑥
The final deep learning neural network classification model is presented in Figure 3.
A total of three hidden layers with 50, 50, and 20 nodes, respectively, provided the
optimum model. With a 96.60% accuracy, the score of importance using SPSS 25 was used
to verify the output of consecutive ranking of factors affecting the acceptance of hybrid
WorldElectr.Veh.J.2023,14,227 14of26
cars. Presented in Table 5 is the normalized score of the importance of the resulting
parameters.
FiFgiugruer 3e. 3D.eDepe eleparlneainrgn innegurnael unreatwlnoerktw moordkelm. odel.
4.4 . Validation
To validate the different MLA accuracy outputs, a Taylor Diagram was generated.
FollowingthestudyofGermanetal.[22]andOng[23],therootmeansquareerrorshould
bewithin20%andtheacceptedcorrelationvalueat90%forsignificantfactors. Settingthe
thresholdof1.00forthestandarddeviation,Figure4representstheTaylorDiagramforthis
study. ItcouldbeseenthattheoutputofdifferentMLAsusedinthisstudyisacceptable.
Moreover,thebasicdecisiontreecannotbeutilizedduetothelowoutputat0. Inaddition,
World Electr. Veh. J. 2023, 14, x FOR PEtEhR eREleVaIEsWt significantfactors,suchasHM,EE,PECC,PV,andHB,canst1il6l obf e27c onsideredbut
arelessinfluentiallatentvariables.
FFigiugruer 4e. T4.ayTlaoyr lDoiragDraiamg. ram.
5. Discussion
Hybrid cars promote sustainable transportation, which is essential for both techno-
logical advancement and reducing carbon emissions; therefore, it is crucial to study the
role of behavioral intention in determining how Filipino drivers adapt and transition to
eco-friendly vehicles. The study aimed to examine the factors influencing Filipinos’ ac-
ceptance or purchasing intentions toward hybrid cars using the Pro-environmental The-
ory of Planned Behavior (PEPB) and Sustainability Domains. These were combined into
the Sustainability Theory of Planned Behavior, along with the integrated the Unified The-
ory of Acceptance and the Use of Technology 2 (UTAUT2). From the results, both the
random forest classifier (RFC) and the deep learning neural network (DLNN) were uti-
lized to evaluate the different significant factors affecting purchasing intentions of hybrid
cars.
This study was able to justify the limitations of SEM as discussed by related studies
[23–25]. As seen, PENC was deemed to be the most important latent variable, followed by
AT, PBC, SN, and PE. Compared to the SEM result [15], it was seen that these were ranked
fifth, third, seventh, second, and fourth, respectively. Clear distinctions were seen within
the indirect effects among sustainability domains, which were mediated by the TPB do-
mains. From the current study, PENC was deemed highly significant, while PAS ranked
sixth, and PECC ranked tenth–compared to its SEM counterpart results being fifth, third,
and first, respectively. Since the presence of mediating factors are seen among the STPB
model, the justification of hindrance among mediating factors played a role [23–25].
In addition, the MLA results proved that the FC, EE, and HB were significant while
the SEM results deemed them insignificant. As explained by Li et al. [95] who compared
the SEM with the MLA, it was presented that the MLA has more predictive capabilities,
generated higher accuracy rates, and could better present the model output rather than
the final model SEM considers. It was added that the MLA can provide better explanation
of the model based on the mutual understanding of machines and humans. Hadiyat [96]
also provided the same justification. However, not all output may be different like that of
Ong et al. [75] when analyzing telemedicine acceptance in the Philippines where both the
SEM and the ANN provided the same output. Their explanation in the paper was that

WorldElectr.Veh.J.2023,14,227 15of26
5. Discussion
Hybridcarspromotesustainabletransportation,whichisessentialforbothtechno-
logicaladvancementandreducingcarbonemissions;therefore,itiscrucialtostudythe
roleofbehavioralintentionindetermininghowFilipinodriversadaptandtransitionto
eco-friendlyvehicles. ThestudyaimedtoexaminethefactorsinfluencingFilipinos’accep-
tanceorpurchasingintentionstowardhybridcarsusingthePro-environmentalTheory
ofPlannedBehavior(PEPB)andSustainabilityDomains. Thesewerecombinedintothe
SustainabilityTheoryofPlannedBehavior,alongwiththeintegratedtheUnifiedTheory
ofAcceptanceandtheUseofTechnology2(UTAUT2). Fromtheresults,boththerandom
forest classifier (RFC) and the deep learning neural network (DLNN) were utilized to
evaluatethedifferentsignificantfactorsaffectingpurchasingintentionsofhybridcars.
This study was able to justify the limitations of SEM as discussed by related
studies[23–25]. As seen, PENC was deemed to be the most important latent variable,
followedbyAT,PBC,SN,andPE.ComparedtotheSEMresult[15],itwasseenthatthese
wererankedfifth,third,seventh,second,andfourth,respectively. Cleardistinctionswere
seenwithintheindirecteffectsamongsustainabilitydomains,whichweremediatedbythe
TPBdomains. Fromthecurrentstudy,PENCwasdeemedhighlysignificant,whilePAS
rankedsixth,andPECCrankedtenth–comparedtoitsSEMcounterpartresultsbeingfifth,
third,andfirst,respectively. Sincethepresenceofmediatingfactorsareseenamongthe
STPBmodel,thejustificationofhindranceamongmediatingfactorsplayedarole[23–25].
Inaddition,theMLAresultsprovedthattheFC,EE,andHBweresignificantwhile
theSEMresultsdeemedtheminsignificant. AsexplainedbyLietal.[95]whocompared
theSEMwiththeMLA,itwaspresentedthattheMLAhasmorepredictivecapabilities,
generatedhigheraccuracyrates,andcouldbetterpresentthemodeloutputratherthan
thefinalmodelSEMconsiders. ItwasaddedthattheMLAcanprovidebetterexplanation
ofthemodelbasedonthemutualunderstandingofmachinesandhumans. Hadiyat[96]
alsoprovidedthesamejustification. However,notalloutputmaybedifferentlikethat
ofOngetal.[75]whenanalyzingtelemedicineacceptanceinthePhilippineswhereboth
theSEMandtheANNprovidedthesameoutput. Theirexplanationinthepaperwasthat
theirstudyonlyutilizedadirectrelationshipfromtheUTAUT2. Thus,thissmallmodel
compared to the current study has distinct differences. Summarized in Table 6 are the
differentrankedscoresofthelatentvariables. Thediscussionofthesucceedingsectionis
basedonthehighestsignificanteffectfromMLA.
Table6.MLAversusSEMResults.
| LatentVariable | MLA  | SEM           |
| -------------- | ---- | ------------- |
| PENC           | 1st  | 5th           |
| AT             | 2nd  | 3rd           |
| PBC            | 3rd  | 7th           |
| SN             | 4th  | 2nd           |
| PE             | 5th  | 4th           |
| PAS            | 6th  | 3rd           |
| FC             | 7th  | Insignificant |
| HM             | 8th  | 6th           |
| EE             | 9th  | Insignificant |
| PECC           | 10th | 1st           |
| PV             | 11th | 8th           |
| HB             | 12th | insignificant |

WorldElectr.Veh.J.2023,14,227 16of26
Fromthefindings,thehighestcontributingfactortoconsumeracceptancewasthe
perceivedenvironmentalconcern(PENC)(100%)latent,havingasignificantdirecteffecton
subjectivenorm(SN),attitude(AT),andperceivedbehavioralcontrol(PBC).Basedonthe
indicators,Filipinodriversorgeneralrespondentsrecognizedthathumankindisseverely
abusingandpollutingtheenvironment,causingthemtobeworriedaboutitsfuturestatus
andavoidingmoredisastrousconsequences. Theyfeltcompelledtoadoptmoreecologi-
callyfriendlyproducts,suchashybridcars,whicharebothhandyandbeneficialtothe
existingenvironmentalconditions. RossiandRivetti[97]mentionedthatyoungerpeople,
notablymillennialsandpost-millennials(ages23–29and30–36),aremoreconcernedwith
sustainability,haveacollectivepurchasingpower,andarebecominganincreasinglycrucial
consumerdemographic. Becausetheyaremoreinclinedtoenvironmentalactivismanden-
gagingthroughplatformswheretheseeco-labeleditemsandideologiesarepromoted—in
thisstudy,obtaininghybridcars—millennialsaremorelikelytoutilizeeco-friendlyman-
ufacturedproducts[98]. Thus,itcouldbededucedthathybridcarscouldbeviableasa
highlyefficientformoftransportationduetotheirpositiveenvironmentaleffects.
Attitude (AT) (96.32%) was also deemed to have a highly significant direct effect
on behavioral intention (BI). This shows that the positive or negative evaluation of the
adoptionbehaviorofhybridcarswillparticularlyinfluenceaperson’sintentiontopurchase
them. Respondentsweremorelikelytobelievethatpurchasingahybridcarisawiseand
pleasantdecision,andtheytrustedthenotionofpurchasingahybridcarsincelearning
to utilize it may be a fulfilling experience. In addition, this finding is substantiated by
thestudyofChenetal.[78],whichproveshowproductsthatmaymakecustomersfeel
joyful,thrilled,orcheerfulcanleadtomoreacceptanceandahigherloyaltyattitude. In
addition,thestudyofNadlifatinetal.[99]validatedthecorrelationbetweenATandBI
asthegreatestvalueamongallcorrelationresultsregardingtheuseofeco-labelproducts.
Therefore,thesecanbeobtainedthroughtheassociatedemotionalandknownsustainable
benefitsthatgreenproductsactivelyelicit. Inaccordance,PBCandPEwereprovedtohave
ahighlysignificantanddirecteffectonBI.
PBC (94.50%) and PE (90.20%) were shown to have a highly significant and direct
effectonBI.AlthoughlowerthanthatoftheATlatent,itsuggeststhatdriverscanstillsense
theeaseofoperationofahybridcarcomparedtoaconventionalvehicleandthatitcomes
withmoreexcellentresourcesandopportunitiesoranticipationthatitislessvulnerableto
impediments[100]. ThisfindingwassupportedbyCahigasetal.[101],whichfoundthat
PBCsignificantlyandpositivelyaffectedtheintentiontouseinthetransportationsetting.
Based on the two sets of indicators, it is up to the consumer’s discretion to confidently
selectahybridcarforhis/herfuturepurchasebydeterminingthatdrivingahybridcar
wouldbesafer,morecomfortable,andmoreproductive. Furthermore,PEhasbeenproven
byChongetal.[102]tohaveastrong, positiveassociationwithbehavioralintentionin
adoptingnewtechnology,similartothestudyconductedbyForoughietal.[103]inthearea
ofautonomoustransportation.Thesearevitalaspects,especiallywhenahighpercentageof
respondentswereworkingindividualswhorequireefficiencyintransportationandfewer
hindrancesinusingadifferenttypeofvehicle.
Concerningthesignificantfactors,SN(92.12%)latenthadasignificantdirecteffect
on BI. Filipinos believed that the people they trusted who influenced and had a good
impressiononthemwouldalsorecommendthattheypurchaseoruseahybridcar.Similarly,
itwasindicatedthathybridcarswouldcomeoffasmoreprestigiousthantraditionalfossil-
fueledvehicles. ThisresultalignedwithastudybyYang[104],whereinconsumers’buying
intentionswereimpactedbypeertrustandreciprocity. Theywereeagertotakeadviceand
suggestionsfromtrustworthypeers.Consequently,themoderateinfluenceSIhasonBImay
bebecauseonlytheexperienceofsocialinteractionsthathavecreatedcloserelationships
amongpeerswouldimpactcustomers’buyingintentionsmoresignificantly[10,101].
AlongwithSN,perceivedauthoritysupport(PAS)(84.50%)hadasignificantdirect
effectonSN,AT,andPBC.Theindicatorsrevealthatthegovernmentisactiveinsettingup
facilitiesforhybridcars,enactsregulationsthatallowFilipinostousethesevehicles,and

WorldElectr.Veh.J.2023,14,227 17of26
encouragesorendorsestheusageofthemthroughthesesameregulations. Althoughthe
PhilippineStatisticsAuthority[65]hasacknowledgedthattherearepoliciesandprograms
in place to enable the acquisition and handling of hybrid vehicles, they still need to be
promotedonparwithconventionalvehiclesinthemarket. AstudybyYazdanpanahand
HadjiHosseinlou[105]suggestedthatpolicymakersseektomodifyhabitsbyproviding
relevantinformationtoenhancetheintention-behaviorrelationship. Withthat, thereis
a need for eco-labeled cars in the country, which is gradually being addressed by the
authorities. EspeciallyinthePhilippines,thegovernmentistakingsmallsteps,suchas
settingupsomeplacesforchargingelectriccars. However,thepromotionoftheusageis
stillunderrepresentedinthecountry.
Facilitatingconditions(FCs)(81.20%)alsoprovedtobeasignificantfactoraffectingBI.
TheindicatorsdelineatedthatFilipinodrivershavethenecessaryresourcestooperatea
hybridcar,areknowledgeableindriving,andcanaskquestionsandfindsolutionsifany
problemsareidentified. ThisfindingissimilartothestudyofLallmahomedetal.[106],
whereintheypresentedhowFCsignificantlyaffectsusageintention. Yuduangetal.[28]
also mentioned how consumers prefer using applications that are beneficial and easily
accessible. Theresourcesthatareaccessibleforcontinuoususageofnewtechnologies,such
ashybridcars,areconsideredbythecurrentgeneration. Hedonicmotivation(HM)(79%)
wasalsoseentobeasignificantfactoraffectingBI.Basedontheindicators,usingahybrid
carismorefun,entertaining,enjoyable,andsatisfyingthandrivingafossil-fueledcar. It
has been demonstrated that hedonic motivation, defined as the enjoyment or pleasure
consumers derive from adopting new technology, is crucial in influencing technology
acceptanceanduse[107]. Theresultsoftheanalysisofthehedonicmotivationconstruct
wereinlinewiththeresultsofpreviousstudiesbyVenkateshetal.[11]andPalau-Saumell
etal.[108],asboththeirresultssubstantiatedthefactthathedonicmotivationisasignificant
predictorofintentiontouse.
Effortexpectancy(EE)(77.60%)alsoprovedtobeasignificantfactoraffectingBI.The
indicatorsthatledtotheimportancewerethathybridcarsprovideclearandunderstandable
interactionsthatareeasytooperate,adapt,andadept. Thisresultisquitesimilartothe
findingsofNordhoffetal.[12]: sinceEEisasubstantialpositivepredictorofbehavioral
intention, individuals who imply that using conditionally autonomous cars is simple
aremorelikelytowanttoutilizethem. Alignedwiththis,perceivedeconomicconcern
(PECC)(76.70%)wasalsoprovedtobeasignificantfactoraffectingBI,SN,AT,andPBC.
The study found that hybrid cars have good warranties and economic incentives, can
generatemoresavingswhichimproveanindividual’seconomicstandinginthelongrun,
drivemoreefficiently,andareeasilyacquirableinthemarket. Thisaddedlatent,which
completesthesustainabilitytheoryofplannedbehavior(STPB),isrelatedtoanindividual’s
voluntaryinvolvement,comprehensivesocietalandcommercialconsideration,andsense
ofsocialresponsibility.
ThisissupportedbythestudyofSaifetal.[64],whichprovedthatconsumers’inten-
tiontoadopthasapositiverelationshipwithperceivedeconomicefficiency. Accordingto
theirfindings,practitionersshouldprovideclientswithfinancialbenefits,suchascharge-
free,new,oruniqueservices,andcompetitiveprices,tofurtherpromoteuseracceptance.
It has been established by Lane and Potter [109] that economic instruments point to a
strategyofpromotingtheuseofcleanerfuelsandvehiclesthroughtheuseoffinancial
incentives,anapproachbasedontheconceptofecologicaltaxationreform. Thisindicates
substantialevidencethateconomicfactorscaneffectivelyencouragecleaneroptionssuch
ashybridcars.
Interestingly, despite the positive remarks of the latent price value (PV) (76.20%)
indicatorsthathybridcarsarereasonablypriced,goodvalueformoney,andavaluable
purchase,itwasstillconsideredthesecondleastsignificantfactoraffectingBI.Chaveesuk
etal.[110]explainedthatpricevalue,whichisdefinedasconsumers’cognitivetrade-offs
betweentheperceivedcostsandbenefitsofadoptingaspecificsystem,hasasignificant
direct effect on behavioral intention. Concerning the demographic factors, most of the

WorldElectr.Veh.J.2023,14,227 18of26
respondentshaveamonthlysalaryof20,000pesosto50,000pesoswhichmeansthatthey
belong to the lower middle class to the middle class as stated on the indicative range
ofmonthlyfamilyincomeinthestudyofAlbertetal.[111]. However, consumersmay
purchaseorarewillingtoinvestinhybridcarsinsteadoffossil-fueledcars,regardlessofthe
addedamount,sincetheyareconsideredcost-effective. Thisstudyfiguredthatconsumers
arewillingtopaytheextraamountfortheefficiency,environmental,andeconomicbenefits
thathybridcarsoffer.
The least significant out of all the latent affecting behavioral intention was Habit
(HB)(70.90%). Basedontheindicators,usingahybridcarbecameahabit,anaddiction
forwhichconsumersarewillingtopaymore,andservesasadailyutility. Theutilityof
hybridcarsremainsunrecognizedandunfamiliartomanysincethePhilippinemarket
forhybridcarsiscurrentlysparse,whichiswhyHBhasnotbeenestablishedandisthe
leastsignificantfactor. Similarly,Nordfjaernetal.[112]discoveredthatthecarhabitfactor
negativelypredictsintentionandisnotassignificantasotherbehavioralfactors. Itwas
found that to predict better user intention, user personality traits must be assessed in
line with TPB domains. As a result, consumers still need to develop the habit of using
thismodeoftransportation. Eventually,itisexpectedthathabitwillsoondevelopifthe
hybridcarmarketinthePhilippinesbecomessaturated,buildingstrongfamiliaritywith
Filipinodrivers.
To better provide insights among readers, Table 7 lists all the abbreviations used
throughoutthestudy.
Table7.Listofabbreviationsusedthroughoutthepaper.
Abbreviations Meaning
ANN ArtificialNeuralNetwork
AT Attitude
BI BehavioralIntentions
DLNN DeepLearningNeuralNetwork
DT DecisionTree
HB Habit
HM HedonicMotivation
HV HybridVehicle
IDT InnovationDiffusionTheory
MLA MachineLearningAlgorithm
MM MotivationalModel
NAM NormActivationModel
PE PerformanceExpectancy
PECC PerceivedEconomicConcern
PEPB Pro-EnvironmentalTheoryofPlannedBehavior
PENC PerceivedEnvironmentalConcern
PV PriceValue
RFC RandomForestClassifier
SE Self-Efficacy
SI SocialInfluence
SN SubjectiveNorm
SQ ServiceQuality
EE EffortExpectancy

WorldElectr.Veh.J.2023,14,227 19of26
Table7.Cont.
Abbreviations Meaning
FC FacilitatingConditions
PAS PerceivedAuthoritySupport
STPB SustainabilityTheoryofPlannedBehavior
TAM TechnologyAcceptanceModel
TPB TheoryofPlannedBehavior
UTAUT2 UnifiedTheoryofAcceptanceandUseofTechnology
5.1. TheoreticalContributions
AccordingtothestudybyAgatonetal.[113],airpollutionandgreenhousegasemis-
sionsfromthecombustionoffossilfuelsareoneofthemaindriversofwhygovernments
andregionsseekmoresustainablemeansoftransportation. Withthat,PEPBwasusedto
analyzetheenvironmentalimpactonconsumers’behavioralintentionandsupportsthe
otherlatentvariablesofthesustainabilitydomains[22]. AlongsidethePEPBframework,
thesustainabilitydomains,suchassocial,environmental,andeconomic,wereconsidered,
whiletheUTAUT2addressedthetechnologicalaspect. InthestudyofYurievetal.[114],
theTPB,orthetheoryofplannedbehavior,isthemostextensivelyusedmodelinstudying
individuals’ behavior and is stated to encompass all environmental behavior variables.
However,itlacksthenecessarysustainabilitylatentconstruct[102,115].
Inmeasuringtheacceptanceentirelyorholistically,theframeworksmentionedabove
werecombinedwithintegratingtheeconomicaspectintotheproposedsustainabilitytheory
ofplannedbehavior(STPB).Itcanbeappliedwhenevaluatingthecurrentgeneration’s
behavioralintentionandacceptanceofnewlyemergingorcurrentsmarttechnologiessuch
as the hybrid car. According to the study of Zadjafar and Gholamian [116], consumers
nowadaysaremoreconsciousofobtainingandpurchasingsustainableproducts. Inthis
case,itwassuggestedthatmanufacturersandindustriesfocusmoreondevelopingand
selling products that attest to the demand of green consumers. Since all the factors in
the study were proven significant, the developed framework could be used by future
researcherstomeasurenotonlythebehavioralaspectbutalsothesustainabilityaspectof
anindividualutilizingtheSTPB.
5.2. PracticalandManagerialImplications
Thefindingsofthisstudyhavedemonstratedtheimportanceofpredictingconsumers’
acceptanceofhybridcarsinthePhilippines. Filipinodriverstendtoconsiderhybridcars
whenawareoftheenvironmentalandeconomicbenefits. Theresultofthestudyproved
thatitisessentialfortheyoungergenerationtoadapttoamoresustainablelifestyle,with
thehighdemandforgreenertransportation. Giventhatthereiscurrentlyalimitedmarket
forhybridcarsinthePhilippines,consumersarestillunawareoftheutilityofthesevehicles.
Fortunately,thisconditionmightimprovewithincreasedgovernmentreinforcementby
adopting incentives to promote their utility. Hybrid cars cost more than fossil-fueled
cars, which makes the marketing aspect challenging. In line with this, car companies
andmanufacturerscanalsousetheresultofthisstudyasaframeworkfordesigningand
implementingprograms,strategies,andadvertisementstopropagatethemarketabilityand
utilityofhybridcars. Itissuggestedthatcarcompaniesshouldconsidermillennialsasthe
primarytargetforeco-friendlymanufacturedproductssuchashybridcars,asprojectedin
thestudy’sdemographicresults. Theadvertisementandstrategiesmayrevolvearound
sustainability,targetgeneration,andthedevelopmentandusageofhybridcarstoengage
purchasingintentions. Lastly,consideringthetechnologicalaspect,companiescanalso
disseminate information about the ecological and economic advantages of hybrid cars
throughsocialmediaplatformsandin-appadvertisementssuchasFacebookandYouTube
adsthatcanbecapitalizedbymarketingfirms.

WorldElectr.Veh.J.2023,14,227 20of26
5.3. Limitations
Althoughtherearepositivefindingsinthisstudy,therearealsoseverallimitations
tobenoted. First,duetotheadaptedquestionnaire,therewerelimitedconstructs. The
instrumentwasaself-administeredonlinesurvey, whichpresentsaconstraintinterms
ofthemodalityofthedisseminationandfollowsthesecondpoint,theconsiderationof
therespondents. Havingmoreconstructsanditemsofmeasuremaydevelopresponse
efficiency. Inaddition,consideringinterviewersmayidentifydriversforpurchasinghybrid
carsamongresidentsinthePhilippinesthatotherstudiesmayconsider.
Second, the primary criteria of a driver’s license and the modality narrowed the
respondentstothosedriverswhowereactiveonsocialmedia. Itisrecommendedthat
thedatacollectionbemorediversifiedandnotbeinclinedtoonlyaparticulargeneration,
specificallythemillennials. Abalanceofeachvariationwouldemergeifthestudycould
expoundonothergenerations, suchasGenerationZorbabyboomers, andwouldalso
makestudyingtheacceptanceofeachgenerationtowardhybridcarspossible. Itwould
bemoreprofoundtogathermorerespondentsoutsidethecurrentstudy’ssample,suchas
publicutilityvehiclesorpublicutilityjeepneydrivers,separatelytoreassessthedifferent
perspectives,behavior,andexperiencesofdriverstowardhybridcars.
Third, it is suggested that the study conduct interviews with these individuals to
provideaqualitativeandquantitativeanalysisofthosewhointendtopurchasehybrid
cars. Allowingthestudytohaveaqualitativeaspectwouldprovidemoreflexibility. The
insightsfromtheinterviewresultsmaybeconsideredforadditionallatentvariablesand
itemsofmeasure,evenpresentingaqualitative-quantitativestudy.
Fourth,thisstudyonlyconsideredtwomachinelearningalgorithms:therandomforest
classifierandthedeeplearningneuralnetwork. Tomaximizetheutilityofrelatedanalysis
techniques, other machine learning algorithm tools such as the Naïve Bayes classifier,
K-Nearestneighbor,vectormachine,orevenC-Meansclusteringmaybeincorporatedto
capturedifferentareasoftheresultandidentifyfactorsbasedonprobabilityandsimilarities
asidefromtheindividualfindingsfoundinthisstudy. Lastly,othertoolssuchasK-Means
clusteringcouldbeutilizedaftergatheringrespondentsfromdifferentgenerationstoassess
thedemographiccharacteristicsofdriverswhointendtopurchasehybridcarsfromthe
lowesttothehighestvaluedcustomers,whichwouldallowtheresearcherstoformulate
strategieswiththemarkettosupporttheeconomicaspectfurther. Simultaneousanalysis
ofthevariousfactorsmaybereanalyzedusingmultivariateanalysistoolstojustifythe
study’sfindingssincetheindirecteffectfoundoneachlatentmayprovideasignificant
relationshipamongthefactorsconsideredwhenitcomestothebehavioral,sustainable,
andtechnologicalaspectsofconsumers’purchasingintentionstowardhybridcars.
6. Conclusions
There are not enough studies on the purchasing intentions regarding hybrid cars
in developing countries like the Philippines. This necessitated the formulation of the
SustainabilityTheoryofPlannedBehavior(STPB).Theframeworkwasconstructedusing
thePro-environmentalTheoryofPlannedBehavior(PEPB)andsustainabilitydomains,as
wellasintegrationoftheUnifiedTheoryofAcceptanceandUseofTechnology2(UTAUT2)
to predict the adoption of hybrid cars in the country. It was utilized to fully assess the
acceptanceofsmartandgreentechnology,emphasizingsustainability—avitalaspectwhen
addressingclimatechange. Atotalof1048participantscompletedtheself-administered
survey,disseminatedusingnon-probabilitysamplingmethods,includingconvenienceand
snowballsampling.
This study utilized a Machine Learning Algorithm (MLA) ensemble comprising a
DecisionTree(DT),RandomForestClassifier(RFC),andDeepLearningNeuralNetwork
(DLNN),whichprovedthatPENC,AT,PBC,andPEwerethemostinfluentialfactorsthat
significantlyaffectuseracceptanceofhybridcarsinthePhilippines. ThisimpliesthatMLA
isadvantageousinanalyzingtheantecedentsofhumanbehavior,particularlysustainability
behavior. ComparingtheresultsofbothSEMandMLA,thisstudyidentifiedthatMLA

WorldElectr.Veh.J.2023,14,227 21of26
providedbetterandmoreaccurateresultssincethisstudywasabletoconsideranexpanded
andlargeframeworkforanalysis. However,basedonotherstudies,asmallermodelmay
providesimilaroutput. Therefore,thisstudyconcludesthatusingMLAmaybeapplicable
andbettersuitedforanalyzingnonlinearrelationshipsamonglargeandextendedmodels.
Moreover,itshouldbenotedthatthisstudywasnotabletoguaranteethatitrepresentsan
unbiasedcrosssectionofthetargetaudiencesinceaconveniencesamplingapproachwas
usedduetothelimitationsdiscussed. Inaddition,thisstudyonlyfocusedonthosewho
arecapableandhavedrivers’licenses. Thismeansthattheoutputmaybebiasedinthe
aspectofcapablepurchasers.
Fromthisstudyoutput,perceivedenvironmentalconcernshavethehighestsignificant
directeffectonbehavioralintention,suggestingthattheenvironmentalbenefitsthatcome
with utilizing green technology increase Filipino drivers’ tendency to purchase hybrid
cars. Itisrecommendedthatcarcompaniesconsiderthestudy’sresultsanddemographics
in propagating the marketability of hybrid cars. Other researchers could use the STPB
frameworkestablishedbythestudy’sconstructsandmodeltocontextualizeandemphasize
technologicalsustainability,whichfurthervalidatestheobjectivesoftheUnitedNations’
Sustainable Development Goals (SDGs) to expedite the decarbonization of the overall
marketandtheentireeconomy.
AuthorContributions:Conceptualization,R.D.B.,A.K.S.O.,L.N.Z.C.,F.A.B.L.,N.L.C.,R.A.V.J.and
J.D.G.; methodology, R.D.B., A.K.S.O., L.N.Z.C., F.A.B.L., N.L.C. and R.A.V.J.; software, R.D.B.,
A.K.S.O., L.N.Z.C., F.A.B.L., N.L.C.andR.A.V.J.; validation, R.D.B., A.K.S.O.and J.D.G.; formal
analysis, R.D.B., A.K.S.O., L.N.Z.C., F.A.B.L., N.L.C., R.A.V.J. and J.D.G.; investigation, R.D.B.,
A.K.S.O.,L.N.Z.C.,F.A.B.L.,N.L.C.andR.A.V.J.;resources,R.D.B.,A.K.S.O.,L.N.Z.C.,F.A.B.L.,N.L.C.
andR.A.V.J.;datacuration,A.K.S.O.,L.N.Z.C.,F.A.B.L.,N.L.C.andR.A.V.J.;writing—originaldraft
preparation,R.D.B.,A.K.S.O.,L.N.Z.C.,F.A.B.L.,N.L.C.andR.A.V.J.;writing—reviewandediting,
R.D.B.,A.K.S.O.,L.N.Z.C.,F.A.B.L.,N.L.C.,R.A.V.J.andJ.D.G.;visualization,R.D.B.,A.K.S.O.and
J.D.G.;supervision,R.D.B.,A.K.S.O.andJ.D.G.;projectadministration,R.D.B.,A.K.S.O.andJ.D.G.;
fundingacquisition,R.D.B.,A.K.S.O.andJ.D.G.Allauthorshavereadandagreedtothepublished
versionofthemanuscript.
Funding: ThisresearchwasfundedbyMapuaUniversityDirectedResearchforInnovationand
ValueEnhancement(DRIVE).
InstitutionalReviewBoardStatement: ThisstudywasapprovedbyMapuaUniversityResearch
EthicsCommittees(FM-RC-23-01-13).
InformedConsentStatement: Informedconsentwasobtainedfromallsubjectsinvolvedinthis
study(FM-RC-23-02-13).
DataAvailabilityStatement: Thedatapresentedinthisstudyareavailableonrequestfromthe
correspondingauthor.
Acknowledgments:Theauthorswouldliketothankalltherespondentswhoansweredouronline
questionnaire.Wewouldalsoliketothankourfriendsfortheircontributionstothedistributionof
thequestionnaire.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.
References
1. Tiseo, I. Global Transport CO Emissions Breakdown; Statista: Singapore, 2021; Available online: https://www.statista.com/
2
statistics/1185535/transport-carbon-dioxide-emissions-breakdown/(accessedon31May2023).
2. Wasiak,A.L.ModelingtheEffectsofImplementationofAlternativeWaysofVehiclePowering.Fuels2021,2,487–500.[CrossRef]
3. UnitedNations. The17Goals|SustainableDevelopment. 2015. Availableonline: https://sdgs.un.org/goals(accessedon
2January2023).
4. Irawan,M.Z.;Belgiawan,P.F.;Widyaparaga,A.;Deendarlianto;Budiman,A.;Muthohar,I.;Sopha,B.M.Amarketshareanalysis
forhybridcarsinIndonesia.CaseStud.Transp.Policy2018,6,336–341.[CrossRef]
5. Ong,A.K.S.;Cleofas,M.A.;Prasetyo,Y.T.;Chuenyindee,T.;Young,M.N.;Diaz,J.F.T.;Nadlifatin,R.;Redi,A.A.N.P.Consumer
behaviorinclothingindustryanditsrelationshipwithopeninnovationdynamicsduringtheCOVID-19pandemic.J.OpenInnov.
Technol.Mark.Complex.2021,7,211.[CrossRef]

WorldElectr.Veh.J.2023,14,227 22of26
6. Vabø,M.;Hansen,H.PurchaseintentionsforDomesticFood: Amoderatedtpb-explanation. Br. FoodJ.2016,118,2372–2387.
[CrossRef]
7. Tanwir,N.S.;Hamzah,M.I.Predictingpurchaseintentionofhybridelectricvehicles:Evidencefromanemergingeconomy.World
Electr.Veh.J.2020,11,35.[CrossRef]
8. Wang,S.;Fan,J.;Zhao,D.;Yang,S.;Fu,Y.Predictingconsumers’intentiontoadopthybridelectricvehicles:Usinganextended
versionofthetheoryofplannedbehaviormodel.Transportation2016,43,123–143.[CrossRef]
9. Javid,M.A.;Abdullah,M.;Ali,N.;Shah,S.A.H.;Joyklad,P.;Hussain,Q.;Chaiyasarn,K.Extractingtravelers’preferencestoward
electricvehiclesusingthetheoryofplannedbehaviorinLahore,Pakistan.Sustainability2022,14,1909.[CrossRef]
10. German,J.D.;Ong,A.K.S.;PerwiraRedi,A.A.N.;Robas,K.P.E.Predictingfactorsaffectingtheintentiontousea3PLduringthe
COVID-19pandemic:Amachinelearningensembleapproach.Heliyon2022,8,e11382.[CrossRef]
11. Venkatesh,V.;Thong,J.Y.L.;Xu,X.Consumeracceptanceanduseofinformationtechnology:Extendingtheunifiedtheoryof
acceptanceanduseofTechnology.MISQ.2012,36,157.[CrossRef]
12. Nordhoff,S.;Louw,T.;Innamaa,S.;Lehtonen,E.;Beuster,A.;Torrao,G.;Bjorvatn,A.;Kessel,T.;Malin,F.;Happee,R.;etal.Using
theUTAUT2modeltoexplainpublicacceptanceofconditionallyautomated(L3)cars:Aquestionnairestudyamong9118car
driversfromeightEuropeancountries.Transp.Res.PartFTrafficPsychol.Behav.2020,74,280–297.[CrossRef]
13. Prasetyo,Y.T.;Vallespin,B.E.P.DeterminingfactorsaffectingtheacceptanceofgrabapplicationinthePhilippinesusingUTAUT2
approach.InProceedingsofthe2021IEEE8thInternationalConferenceonIndustrialEngineeringandApplications(ICIEA),
Chengdu,China,23–26April2021.[CrossRef]
14. Khazaei,H.;Tareq,M.A.Moderatingeffectsofpersonalinnovativenessanddrivingexperienceonfactorsinfluencingadoptionof
BEVsinMalaysia:Anintegratedsem–BSEMapproach.Heliyon2021,7,e08072.[CrossRef]
15. Ong,A.K.S.;German,J.D.;Redi,A.A.N.P.;Cordova,L.N.Z.;Longanilla,F.A.B.;Caprecho,N.L.;Javier,R.A.V.Antecedentsof
behavioralintentionsforpurchasinghybridcarsusingsustainabilitytheoryofplannedbehaviorintegratedwithUTAUT2.
Sustainability2023,15,7657.[CrossRef]
16. LandTransportationOffice.AnnualReport2020;LandTransportationOffice—DepartmentofTransportation:Philippines,2021;
Availableonline: https://eb-production-media.s3.amazonaws.com/clients/research_paper_reports/EB-Report-BE-Manila-
Electric-Vehicles-2021-2.pdf(accessedon27January2023).
17. InternationalTradeAdministration. PhilippinesElectricVehiclesMarket. 2020. Availableonline: https://www.trade.gov/
market-intelligence/philippines-electric-vehicles-market(accessedon27January2023).
18. Canivel,R.S.C.FilipinoBuyersShifttoSmallerCars,HevsasFuelPricesSoar.Availableonline:https://business.inquirer.net/35
1026/filipino-buyers-shift-to-smaller-cars-hevs-as-fuel-prices-soar(accessedon29April2023).
19. StatistaResearchDepartmentPhilippines.ElectricVehiclesSold.2022.Availableonline:https://www.statista.com/statistics/12
50975/philippines-electric-vehicles-sold/(accessedon29June2023).
20. Visconti,K.HybridCarsNotCatchingoninPhilippines.Availableonline:https://www.rappler.com/business/10854-hybrids-
not-catching-on-in-the-philippines/#:~:text=Hybrids%20haven\T1\textquoterightt%20caught%20on,in%20terms%20of%20
hybrid%20technology%E2%80%A6(accessedon26February2023).
21. ManilaBulletinThinkaboutDrivinganElectricorHybridVehicle.Availableonline:https://mb.com.ph/2023/01/29/think-
about-driving-an-electric-or-hybrid-vehicle/(accessedon29April2023).
22. German, J.D.; Redi, A.A.N.P.; Prasetyo, Y.T.; Persada, S.F.; Ong, A.K.S.; Young, M.N.; Nadlifatin, R. Choosing a package
carrierduringCOVID-19pandemic:Anintegrationofpro-environmentalplannedbehavior(PEPB)theoryandServiceQuality
(SERVQUAL).J.Clean.Prod.2022,346,131123.[CrossRef][PubMed]
23. Fan, Y.; Chen, J.; Shirkey, G.; John, R.; Wu, S.R.; Park, H.; Shao, C.Applicationsofstructuralequationmodeling(SEM)in
EcologicalStudies:Anupdatedreview.Ecol.Process.2016,5,19.[CrossRef]
24. Woody,E.AnSEMperspectiveonevaluatingmediation:Whateveryclinicalresearcherneedstoknow.J.Exp.Psychopathol.2011,
2,210–251.[CrossRef]
25. Al-Emran,M.;Arpaci,I.;Salloum,S.A.AnempiricalexaminationofcontinuousintentiontouseM-learning: Anintegrated
model.Educ.Inf.Technol.2020,25,2899–2918.[CrossRef]
26. Ong,A.K.S.;Chuenyindee,T.;Prasetyo,Y.T.;Nadlifatin,R.;Persada,S.F.;Gumasing,M.J.J.;German,J.D.;Robas,K.P.E.;Young,
M.N.; Sittiwatethanasiri, T. Utilization of random forest and deep learning neural network for predicting factors affecting
perceivedusabilityofaCOVID-19contacttracingmobileapplicationinThailand“Thaichana”.Int.J.Environ.Res.PublicHealth
2022,19,6111.[CrossRef][PubMed]
27. Larose,R.;DeMaagd,K.;Chew,H.E.;Tsai,H.-Y.S.;Steinfield,C.;Wildman,S.S.;Bauer,J.M.Broadbandadoption|measuring
sustainablebroadbandadoption:Aninnovativeapproachtounderstandingbroadbandadoptionanduse.Int.J.Commun.2012,
6,25.[CrossRef]
28. Yuduang,N.;Ong,A.K.S.;Prasetyo,Y.T.;Chuenyindee,T.;Kusonwattana,P.;Limpasart,W.;Sittiwatethanasiri,T.;Gumasing,
M.J.J.;German,J.D.;Nadlifatin,R.Factorsinfluencingtheperceivedeffectivenessofcovid-19riskassessmentmobileapplication
“Morchana”inThailand:Utaut2approach.Int.J.Environ.Res.PublicHealth2022,19,5643.[CrossRef]
29. Hassan,I.B.;Murad,M.A.A.;El-Shekeil,I.;Liu,J.ExtendingtheUTAUT2modelwithaprivacycalculusmodeltoenhancethe
adoptionofahealthinformationapplicationinMalaysia.Informatics2022,9,31.[CrossRef]

WorldElectr.Veh.J.2023,14,227 23of26
30. Chang,C.-M.;Liu,L.-W.;Huang,H.-C.;Hsieh,H.-H.Factorsinfluencingonlinehotelbooking:ExtendingUTAUT2withage,
gender,andexperienceasmoderators.Information2019,10,281.[CrossRef]
31. Ajzen,I.Thetheoryofplannedbehavior.Organ.Behav.Hum.Decis.Process.1991,50,179–211.[CrossRef]
32. Shiau,W.-L.;Chau,P.Y.K.Understandingbehavioralintentiontouseacloudcomputingclassroom:Amultiplemodelcomparison
approach.Inf.Manag.2016,53,355–365.[CrossRef]
33. Sentosa,I.Theintegrationoftheoryofplannedbehavior(TPB)andtechnologyacceptancemodelininternetpurchasing: A
structuralequationmodeling(SEM)approach.InProceedingsoftheAppliedInternationalBusinessConference,KualaLumpur,
Malaysia,30June–2July2008.
34. Kim,J.J.;Hwang,J.Mergingthenormactivationmodelandthetheoryofplannedbehaviorinthecontextofdronefooddelivery
services:Doesthelevelofproductknowledgereallymatter?J.Hosp.Tour.Manag.2020,42,1–11.[CrossRef]
35. Elkington,J.;Rowland,I.H.Cannibalswithforks:Thetriplebottomlineof21st-centurybusiness.Altern.J.1999,25,42–43.
36. Friedman,L.;Cobb,E.C.ImpactofHybridCars;WorcesterPolytechnicInstitute:Worcester,MA,USA,2010.
37. Su,C.-W.;Yuan,X.;Tao,R.;Umar,M.Cannewenergyvehicleshelptoachievecarbonneutralitytargets?J.Environ.Manag.2021,
297,113348.[CrossRef][PubMed]
38. Korchinski,W.FuelingAmerica: Howhydrogencarsaffecttheenvironment. ReasonFound. PolicyStudy2004,322. Available
online:https://www.policyarchive.org/handle/10207/5741(accessedon18July2023).
39. Asim,N.;Bimani,A.A.;Saqri,A.A.;Matriano,M.Thesocialandenvironmentalimpactofhybridcars.Int.J.Res.Entrep.Bus.
Stud.2020,1,36–47.[CrossRef]
40. James, P.; Magee, L. Domains of sustainability. Glob. Encycl. Public Adm. Public Policy Gov. 2016, 1–17. Available online:
https://link.springer.com/referenceworkentry/10.1007/978-3-319-31816-5_2760-1(accessedon18July2023).
41. He,L.;Wang,M.;Chen,W.;Conzelmann,G.IncorporatingsocialimpactonnewproductadoptioninChoicemodeling:Acase
studyingreenvehicles.Transp.Res.PartDTransp.Environ.2014,32,421–434.[CrossRef]
42. Turon´,K.;Kubik,A.Economicaspectsofdrivingvarioustypesofvehiclesinintelligenturbantransportsystems,including
CAR-sharingservicesandAutonomousVehicles.Appl.Sci.2020,10,5580.[CrossRef]
43. Nisa,C.F.;Bélanger,J.J.;Faller,D.G.;Buttrick,N.R.;Mierau,J.O.;Austin,M.M.K.;Schumpe,B.M.;Sasin,E.M.;Agostini,M.;
Gützkow,B.;etal. Livesversuslivelihoods? perceivedeconomicriskhasastrongerassociationwithsupportforCOVID-19
preventivemeasuresthanperceivedhealthrisk.Sci.Rep.2021,11,9669.[CrossRef][PubMed]
44. Klöckner,C.A.;Matthies,E.Howhabitsinterferewithnorm-directedbehaviour:Anormativedecision-makingmodelfortravel
modechoice.J.Environ.Psychol.2004,24,319–327.[CrossRef]
45. Sandqvist,K.TheAppealofAutomobiles:HumanDesiresandtheProliferationofCars.Availableonline:https://trid.trb.org/
view/567975(accessedon8May2023).
46. Tengstrom,R.TheUseoftheAutomobile: ItsImplicationsforMan,Society,andtheEnvironment. Availableonline: https:
//trid.trb.org/view/386217(accessedon8May2023).
47. Crabbe,M.;Standing,C.;Standing,S.;Karjaluoto,H.AnadoptionmodelformobilebankinginGhana. Int. J.Mob. Commun.
2009,7,515.[CrossRef]
48. Zeithaml,V.A.Consumerperceptionsofprice,quality,andvalue:Ameans-endmodelandsynthesisofevidence.J.Mark.1988,
52,2.[CrossRef]
49. Onwezen,M.C.;Antonides,G.;Bartels,J.Thenormactivationmodel:Anexplorationofthefunctionsofanticipatedprideand
guiltinpro-environmentalbehaviour.J.Econ.Psychol.2013,39,141–153.[CrossRef]
50. Rezvani,Z.;Jansson,J.;Bodin,J.Advancesinconsumerelectricvehicleadoptionresearch:Areviewandresearchagenda.Transp.
Res.PartDTransp.Environ.2015,34,122–136.[CrossRef]
51. Schuitema,G.;Anable,J.;Skippon,S.;Kinnear,N.Theroleofinstrumental,hedonicandsymbolicattributesintheintentionto
adoptelectricvehicles.Transp.Res.PartAPolicyPract.2013,48,39–49.[CrossRef]
52. Pikkarainen, T.; Pikkarainen, K.; Karjaluoto, H.; Pahnila, S. Consumer acceptance of online banking: An extension of the
TechnologyAcceptanceModel.InternetRes.2004,14,224–235.[CrossRef]
53. Manutworakit,P.;Choocharukul,K.FactorsinfluencingbatteryelectricvehicleadoptioninThailand—Expandingtheunified
theoryofacceptanceanduseoftechnology’svariables.Sustainability2022,14,8482.[CrossRef]
54. Davis,F.D.;Bagozzi,R.P.;Warshaw,P.R.Useracceptanceofcomputertechnology: Acomparisonoftwotheoreticalmodels.
Manag.Sci.1989,35,982–1003.[CrossRef]
55. Gunawan,I.;Redi,A.A.N.P.;Santosa,A.A.;Maghfiroh,M.F.N.;Pandyaswargo,A.H.;Kurniawan,A.C.Determinantsofcustomer
intentionstouseelectricvehicleinIndonesia:Anintegratedmodelanalysis.Sustainability2022,14,1972.[CrossRef]
56. Ombach,G.DesignconsiderationsforWirelessChargingSystemforelectricandplug-inhybridvehicles.InProceedingsofthe
HybridandElectricVehiclesConference2013(HEVC2013),London,UK,6–7November2013.
57. Alalwan,A.A.;Dwivedi,Y.K.;Rana,N.P.;Algharabat,R.ExaminingfactorsinfluencingJordaniancustomers’intentionsand
adoptionofinternetbanking:ExtendingUTAUT2withrisk.J.Retail.Consum.Serv.2018,40,125–138.[CrossRef]
58. Venkatesh,V.;Morris,M.G.;Davis,G.B.;Davis,F.D.Useracceptanceofinformationtechnology:Towardaunifiedview.MISQ.
2003,27,425.[CrossRef]
59. Morosan,C.;DeFranco,A.It’sAbouttime:Revisitingutaut2toexamineconsumers’intentionstouseNFCmobilepaymentsin
hotels.Int.J.Hosp.Manag.2016,53,17–29.[CrossRef]

WorldElectr.Veh.J.2023,14,227 24of26
60. Lin,S.-C.;Nadlifatin,R.;Amna,A.R.;Persada,S.F.;Razif,M.Investigatingcitizenbehaviorintentiononmandatoryandvoluntary
Pro-Environmentalprogramsthroughapro-environmentalplannedbehaviormodel.Sustainability2017,9,1289.[CrossRef]
61. Pearson.DOEPushesforFasterelectricVehicleRolloutinthePhilippines.Availableonline:https://www.philstar.com/nation/
2023/06/05/2271616/doe-pushes-faster-electric-vehicle-rollout-philippines(accessedon8May2023).
62. Racz,A.A.;Muntean,I.;Stan,S.-D.Alookintoelectric/hybridcarsfromanecologicalperspective. ProcediaTechnol. 2015,19,
438–443.[CrossRef]
63. BarbosaJunior,M.;Pinheiro,E.;Sokulski,C.C.;RamosHuarachi,D.A.;deFrancisco,A.C.Howtoidentifybarrierstotheadoption
ofsustainableagriculture?astudybasedonamulti-criteriamodel.Sustainability2022,14,13277.[CrossRef]
64. Saif,M.A.M.;Hussin,N.;Husin,M.M.;Alwadain,A.;Chakraborty,A.Determinantsoftheintentiontoadoptdigital-onlybanks
inMalaysia:Theextensionofenvironmentalconcern.Sustainability2022,14,11043.[CrossRef]
65. PhilippineStatisticsAuthority.Goal7.EnsureEnvironmentalSustainability.2021.Availableonline:https://psa.gov.ph/sdg/
about#:~:text=The%20Sustainable%20Development%20Goals%20(SDGs,targets%20and%20232%20unique%20indicators(ac-
cessedon12February2023).
66. Mufidah,I.;Jiang,B.C.;Lin,S.-C.;Chin,J.;Rachmaniati,Y.P.;Persada,S.F.Understandingtheconsumers’behaviorintentionin
usinggreenecolabelproductthroughPro-Environmentalplannedbehaviormodelindevelopinganddevelopedregions:Lessons
learnedfromTaiwanandIndonesia.Sustainability2018,10,1423.[CrossRef]
67. Galloway,A.Non-probabilitysampling. InEncyclopediaofSocialMeasurement;Elsevier: Amsterdam,TheNetherlands,2005;
pp.859–864.
68. Kirchherr,J.;Charles,K.EnhancingthesamplediversityofSnowballSamples:Recommendationsfromaresearchprojecton
anti-dammovementsinSoutheastAsia.PLoSONE2018,13,e0201710.[CrossRef]
69. Hair,J.F.MultivariateDataAnalysis:AGlobalPerspective;PearsonPrenticeHall:UpperSaddleRiver,NJ,USA,2010.
70. Yang,W.;Zhou,S.Usingdecisiontreeanalysistoidentifythedeterminantsofresidents’CO2emissionsfromdifferenttypesof
trips:AcasestudyofGuangzhou,China.J.Clean.Prod.2020,277,124071.[CrossRef]
71. Wu,D.J.;Feng,T.;Naehrig,M.;Lauter,K.Privatelyevaluatingdecisiontreesandrandomforests. Cryptol. ePrintArch. 2015.
Availableonline:https://math.berkeley.edu/~fengt/decision_tree.pdf(accessedon18July2023).[CrossRef]
72. Bordarie,J.Predictingintentionstocomplywithspeedlimitsusinga‘decisiontree’appliedtoanextendedversionofthetheory
ofplannedbehaviour.Transp.Res.PartFTrafficPsychol.Behav.2019,63,174–185.[CrossRef]
73. Charbuty,B.;Abdulazeez,A.ClassificationBasedonDecisionTreeAlgorithmforMachineLearning.J.Appl.Sci.Technol.Trends
2021,2,20–28.[CrossRef]
74. Milani,L.;Grumi,S.;Camisasca,E.;Miragoli,S.;Traficante,D.;DiBlasio,P.FamilialriskandprotectivefactorsaffectingCPS
Professionals’ChildRemovalDecision:Adecisiontreeanalysisstudy.Child.YouthServ.Rev.2020,109,104687.[CrossRef]
75. Ong,A.K.S.;Kurata,Y.B.;Castro,S.A.D.G.;DeLeon,J.P.B.;DelaRosa,H.V.;Tomines,A.P.J.Factorsinfluencingtheacceptanceof
telemedicineinthePhilippines.Technol.Soc.2022,70,102040.[CrossRef]
76. Topîrceanu,A.;Grosseck,G.Decisiontreelearningusedfortheclassificationofstudentarchetypesinonlinecourses.Procedia
Comput.Sci.2017,112,51–60.[CrossRef]
77. Harwati;Sudiya,A.Applicationofdecisiontreeapproachtostudentselectionmodel—Acasestudy.IOPConf.Series:Mater.Sci.
Eng.2016,105,012014.[CrossRef]
78. Chen,J.;Li,Q.;Wang,H.;Deng,M.AmachinelearningensembleapproachbasedonRandomForestandradialbasisfunction
neuralnetworkforriskevaluationofRegionalFloodDisaster:Acasestudyoftheyangtzeriverdelta,China.Int.J.Environ.Res.
PublicHealth2019,17,49.[CrossRef][PubMed]
79. Schnebly,J.; Sengupta,S.Randomforesttwitterbotclassifier. InProceedingsofthe2019IEEE9thAnnualComputingand
CommunicationWorkshopandConference(CCWC),LasVegas,NV,USA,7–9January2019.
80. Ong,A.K.S.;Prasetyo,Y.T.;Velasco,K.E.C.;Abad,E.D.R.;Buencille,A.L.B.;Estorninos,E.M.;Cahigas,M.M.L.;Chuenyindee,T.;
Persada,S.F.;Nadlifatin,R.;etal.Utilizationofrandomforestclassifierandartificialneuralnetworkforpredictingtheacceptance
ofreopeningdecommissionednuclearpowerplant.Ann.Nucl.Energy2022,175,109188.[CrossRef]
81. Chen,Y.-S.;Chang,T.-W.;Li,H.-X.;Chen,Y.-R.TheinfluenceofGreenbrandaffectonGreenPurchaseIntentions:Themediation
effectsofgreenbrandassociationsandGreenbrandattitude.Int.J.Environ.Res.PublicHealth2020,17,4089.[CrossRef]
82. Rodriguez-Galiano,V.F.;Ghimire,B.;Rogan,J.;Chica-Olmo,M.;Rigol-Sanchez,J.P.Anassessmentoftheeffectivenessofa
randomforestclassifierforland-coverclassification.ISPRSJ.Photogramm.RemoteSens.2012,67,93–104.[CrossRef]
83. Elhenawy,M.;Rakha,H.A.;El-Shawarby,I.Enhancedmodelingofdriverstop-or-runactionsatayellowindication.Transp.Res.
Rec.J.Transp.Res.Board2014,2423,24–34.[CrossRef]
84. Ermagun,A.;Rashidi,T.H.;Lari,Z.A.Modechoiceforschooltrips. Transp. Res. Rec. J.Transp. Res. Board2015,2513,97–105.
[CrossRef]
85. Casini,M.BuildingAutomationSystems.Constr.4.02022,525–581.[CrossRef]
86. Sturman,O.;vonZiegler,L.;Schläppi,C.;Akyol,F.;Privitera,M.;Slominski,D.;Grimm,C.;Thieren,L.;Zerbi,V.;Grewe,B.;etal.
Deep learning-based behavioral analysis reaches human accuracy and is capable of outperforming commercial solutions.
Neuropsychopharmacology2020,45,1942–1952.[CrossRef]
87. Luceri,L.;Braun,T.;Giordano,S.Analyzingandinferringhumanreal-lifebehaviorthroughonlinesocialnetworkswithsocial
influenceDeepLearning.Appl.Netw.Sci.2019,4,34.[CrossRef]

WorldElectr.Veh.J.2023,14,227 25of26
88. Pradhan,B.;Lee,S.LandslidesusceptibilityassessmentandFactorEffectAnalysis:Backpropagationartificialneuralnetworks
andtheircomparisonwithFrequencyRatioandbivariatelogisticregressionmodelling.Environ.Model.Softw.2010,25,747–759.
[CrossRef]
89. Gudivada,V.N.Naturallanguagecoretasksandapplications.InHandbookofStatistics;Elsevier:Amsterdam,TheNetherlands,
2018;pp.403–428.[CrossRef]
90. Walrave,M.;Waeterloos,C.;Ponnet,K.Readyornotforcontacttracing? investigatingtheadoptionintentionofCOVID-19
contact-tracingtechnologyusinganextendedunifiedtheoryofacceptanceanduseofTechnologyModel.Cyberpsychol.Behav.Soc.
Netw.2021,24,377–383.[CrossRef]
91. DeRyck,T.;Lanthaler,S.;Mishra,S.OntheapproximationoffunctionsbyTanhneuralnetworks.NeuralNetw.2021,143,732–750.
[CrossRef][PubMed]
92. Costarelli,D.NeuralNetworkOperators: Constructiveinterpolationofmultivariatefunctions. NeuralNetw. 2015,67,28–36.
[CrossRef]
93. Liébana-Cabanillas,F.;Marinkovic´,V.;Kalinic´,Z.ASEM-neuralnetworkapproachforpredictingantecedentsofM-Commerce
Acceptance.Int.J.Inf.Manag.2017,37,14–24.[CrossRef]
94. Narayan,S.Thegeneralizedsigmoidactivationfunction:Competitivesupervisedlearning.Inf.Sci.1997,99,69–82.[CrossRef]
95. Li,J.;Sawaragi,T.;Horiguchi,Y.Introducestructuralequationmodellingtomachinelearningproblemsforbuildinganexplainable
andpersuasivemodel.SICEJ.Control.Meas.Syst.Integr.2021,14,67–79.[CrossRef]
96. Hadiyat,M.A.Combinedstructuralequationmodelling—Artificialneuralnetworksmodelforpredictingcustomerloyalty.IOP
Conf.Ser.Mater.Sci.Eng.2019,703,012024.[CrossRef]
97. Rossi,C.;Rivetti,F.Assessingyoungconsumers’responsestosustainablelabels:InsightsfromafactorialexperimentinItaly.
Sustainability2020,12,10115.[CrossRef]
98. Bedard,S.A.N.;Tolmie,C.R.Millennials’greenconsumptionbehaviour:ExploringtheroleofSocialMedia.Corp.Soc.Responsib.
Environ.Manag.2018,25,1388–1396.[CrossRef]
99. Nadlifatin,R.;Lin,S.-C.;Rachmaniati,Y.P.;Persada,S.F.;Razif,M.Apro-environmentalreasonedactionmodelformeasuring
citizens’intentionsregardingecolabelproductusage.Sustainability2016,8,1165.[CrossRef]
100. Ajzen,I.Perceivedbehavioralcontrol,self-efficacy,locusofcontrol,andthetheoryofplannedbehavior1.J.Appl.Soc.Psychol.
2002,32,665–683.[CrossRef]
101. Cahigas,M.M.;Prasetyo,Y.T.;Persada,S.F.;Ong,A.K.S.;Nadlifatin,R.Understandingtheperceivedbehaviorofpublicutility
buspassengersduringtheeraofCOVID-19pandemicinthePhilippines:Applicationofsocialexchangetheoryandtheoryof
plannedbehavior.Res.Transp.Bus.Manag.2022,45,100840.[CrossRef]
102. Chong, Y.T.; Teo, K.M.; Tang, L.C. A lifecycle-based sustainability indicator framework for waste-to-energy systems and a
proposedmetricofsustainability.Renew.Sustain.EnergyRev.2016,56,797–809.[CrossRef]
103. Foroughi,B.;Nhan,P.V.;Iranmanesh,M.;Ghobakhloo,M.;Nilashi,M.;Yadegaridehkordi,E.Determinantsofintentiontouse
AutonomousVehicles:FindingsfromPLS-semandANFIS.J.Retail.Consum.Serv.2023,70,103158.[CrossRef]
104. Yang,X.Understandingconsumers’purchaseintentionsinsocialcommercethroughsocialcapital: Evidencefromsemand
fsQCA.J.Theor.Appl.Electron.Commer.Res.2021,16,1557–1570.[CrossRef]
105. Yazdanpanah, M.; Hadji Hosseinlou, M. The role of personality traits through habit and intention on determining future
preferencesofpublictransportuse.Behav.Sci.2017,7,8.[CrossRef]
106. Lallmahomed, M.Z.; Lallmahomed, N.; Lallmahomed, G.M. Factors influencing the adoption of e-government services in
Mauritius.Telemat.Inform.2017,34,57–72.[CrossRef]
107. Brown,S.A.;Venkatesh,V.Modelofadoptionoftechnologyinhouseholds:Abaselinemodeltestandextensionincorporating
householdlifecycle.MISQ.2005,29,399.[CrossRef]
108. Palau-Saumell,R.;Forgas-Coll,S.;Sánchez-García,J.;Robres,E.Useracceptanceofmobileappsforrestaurants:Anexpanded
andextendedutaut-2.Sustainability2019,11,1210.[CrossRef]
109. Lane,B.;Potter,S.TheadoptionofcleanervehiclesintheUK:Exploringtheconsumerattitude–actiongap.J.Clean.Prod.2007,
15,1085–1092.[CrossRef]
110. Chaveesuk,S.;Khalid,B.;Bsoul-Kopowska,M.;Rostan´ska,E.;Chaiyasoonthorn,W.Comparativeanalysisofvariablesthat
influencebehavioralintentiontousemoocs.PLoSONE2022,17,e0262037.[CrossRef][PubMed]
111. Albert,J.R.G.;Santos,A.G.F.;Vizmanos,J.F.V.ProfileandDeterminantsoftheMiddle-IncomeClassinthePhilippines;Philippine
InstituteforDevelopmentStudies:LegaspiVillage,Philippines,2018.
112. Nordfjærn, T.; S¸ims¸ekog˘lu, Ö.; Rundmo, T. The role of deliberate planning, car habit and resistance to change in public
transportationmodeuse.Transp.Res.PartFTrafficPsychol.Behav.2014,27,90–98.[CrossRef]
113. Agaton, C.B.; Collera, A.A.; Guno, C.S. Socio-economic and environmental analyses of sustainable public transport in the
Philippines.Sustainability2020,12,4720.[CrossRef]
114. Yuriev,A.; Dahmen,M.; Paillé,P.; Boiral,O.; Guillaumie,L.Pro-environmentalbehaviorsthroughthelensofthetheoryof
plannedbehavior:Ascopingreview.Resour.Conserv.Recycl.2020,155,104660.[CrossRef]

WorldElectr.Veh.J.2023,14,227 26of26
115. Wang,Z.;Dong,X.;Yin,J.Antecedentsofurbanresidents’separatecollectionintentionsforhouseholdsolidwasteandtheir
willingnesstopay:EvidencefromChina.J.Clean.Prod.2018,173,256–264.[CrossRef]
116. Zadjafar,M.A.;Gholamian,M.R.AsustainableinventorymodelbyconsideringEnvironmentalErgonomicsandenvironmental
pollution,casestudy:PulpandPapermills.J.Clean.Prod.2018,199,444–458.[CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.