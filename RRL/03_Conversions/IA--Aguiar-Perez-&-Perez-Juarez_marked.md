sensors
Review
An Insight of Deep Learning Based Demand Forecasting in
Smart Grids
JavierManuelAguiar-Pérez* andMaríaÁngelesPérez-Juárez
DepartamentodeTeoríadelaSeñalyComunicacioneseIngenieríaTelemática,UniversidaddeValladolid,
ETSITelecomunicación,PaseodeBelén15,47011Valladolid,Spain
* Correspondence:javagu@tel.uva.es
Abstract:Smartgridsareabletoforecastcustomers’consumptionpatterns,i.e.,theirenergydemand,
andconsequentlyelectricitycanbetransmittedaftertakingintoaccounttheexpecteddemand.To
facetoday’sdemandforecastingchallenges,wherethedatageneratedbysmartgridsishuge,modern
data-driventechniquesneedtobeused.Inthisscenario,DeepLearningmodelsareagoodalternative
tolearnpatternsfromcustomerdataandthenforecastdemandfordifferentforecastinghorizons.
AmongthecommonlyusedArtificialNeuralNetworks,LongShort-TermMemorynetworks—based
onRecurrentNeuralNetworks—areplayingaprominentrole.Thispaperprovidesaninsightinto
theimportanceofthedemandforecastingissue,andotherrelatedfactors,inthecontextofsmart
grids,andcollectssomeexperiencesoftheuseofDeepLearningtechniques,fordemandforecasting
purposes. Tohaveanefficientpowersystem,abalancebetweensupplyanddemandisnecessary.
Therefore,industrystakeholdersandresearchersshouldmakeaspecialeffortinloadforecasting,
especiallyintheshortterm,whichiscriticalfordemandresponse.
Keywords:demandforecasting; loadforecasting; demandresponse; forecastinghorizon; smartgrid;
smartenvironment;DeepLearning;LongShort-TermMemorynetworks;ConvolutionalNeuralNetworks
1. Introduction
Citation:Aguiar-Pérez,J.M.; Electricitycannotbeeasilystoredforfuturesupply,unlikeothercommoditiessuchas
Pérez-Juárez,M.Á.AnInsightof oil. Thismeansthatelectricitymustbedistributedtotheconsumersimmediatelyafterits
DeepLearningBasedDemand production. Thedistributionofelectricitytofinalusershasbeendonewiththehelpofthe
ForecastinginSmartGrids.Sensors
traditionalelectricalgrid(seedefinitioninTable1)whichallowsthedeliveryofelectricity
2023,23,1467. https://doi.org/
fromproducerstoconsumers. Toachievethatgoal,itconnectstheelectricitygenerating
10.3390/s23031467
stationsandthetransmissionlinesthatdelivertheelectricitytothefinalusers. Traditional
AcademicEditors:Hossam electricalgridsvaryinsize. Whenthesegridsstartedtoexpand,controllingthembecamea
A.GabbarandFcoJavierRodríguez verycomplexanddifficulttask. Additionally,demandforecasting(seedefinitioninTable1)
hasnottraditionallybeenconsidered.
Received:27November2022
In this context, the concept of the smart grid (see definition in Table 1) arises and
Revised:9January2023
starts to play an important role. This concept has been exhaustively reviewed in the
Accepted:26January2023
literature(e.g.,[1–4]). Smartgridsprovideatwo-waycommunicationbetweenconsumers
Published:28January2023
andsuppliers. Smartgridsaddhardwareandsoftwaretothetraditionalelectricalgrid
toprovideitwithanautonomousresponsecapacitytodifferenteventsthatcanaffectthe
electricalgrid.Thefinalobjectiveistoachieveanoptimaldailyoperationalefficiencyforthe
Copyright: © 2023 by the authors. electricalpowerdelivery. In[4],theauthorsdefine“smartgrid”asanewformofelectricity
Licensee MDPI, Basel, Switzerland. networkthatoffersself-healing,power-flowcontrol,energysecurityandenergyreliability
This article is an open access article usingdigitaltechnology. In[2],theauthorshighlightthattheconceptofthesmartgridis
distributed under the terms and transformingthetraditionalelectricalgridbyusingdifferenttypesofadvancedtechnology.
conditionsoftheCreativeCommons Accordingtotheseauthors,thisconceptintegratesalltheelementsthatarenecessaryto
Attribution(CCBY)license(https:// generate, distribute, and consume energy efficiently and effectively. In [5], the authors
creativecommons.org/licenses/by/ emphasizethatthesmartgridconceptemergedtomakethetraditionalelectricalgridmore
4.0/).
Sensors2023,23,1467.https://doi.org/10.3390/s23031467 https://www.mdpi.com/journal/sensors

Sensors2023,23,1467 2of30
efficient,secure,reliable,andstable,andtobeabletoimplementdemandresponse(see
definitioninTable1).
Table1.Importantkeywordsforreadingthisarticle.
Keyword Definition
Theprocessofestimatingend-userdemandinrelationto
Demandforecasting
electricityconsumptionoveragivenperiod.
Achangeinend-users’electricityconsumptiontobetterbalance
Demandresponse powerdemandandsupply.
Alsoreferredtoasdemand-sideresponse.
Thetechniqueusedbypowercompaniestoforecasttheelectricity
Loadforecasting neededtomeetdemandtobetterbalancepowerdemand
andsupply.
Loadprofile Theelectricitydemandforecastmadeforthenext24h.
Anaggregationofloadsandmicrosourcesoperatingasasingle
system,i.e.,asmallelectricalgridofuserswithlocalcontroland
Microgrid
supplycapability.Itisnormallyconnectedtoacentralised
nationalelectricitygridbutcanoperateautonomously.
Agriddevelopedspecificallyforthetransmissionofelectrical
Traditionalelectricalgrid energyfrompointsofproductiontotheutilizationpoints.
Alsoreferredtoasconventional/existingelectrical/powergrid.
Abuildingthatusesawiderangeoftechnologiestoenable
Smartbuilding efficientuseofresources,includingelectricalenergy,while
providingacomfortableenvironmentforitsoccupants.
Anytypeofenvironment,suchasasmarthomeorasmart
building,thatusesawiderangeoftechnologiestoenableefficient
Smartenvironment
useofresources,includingelectricity,whilecreatinga
comfortableenvironmentforitsoccupants.
Anelectricalgridthatcanmonitorandprovidereal-time
informationonitsownactivitywiththehelpofdigital
Smartgrid
technologies.Itisconsideredadevelopedformofthetraditional
electricalgrid.
Ahomethatusesawiderangeoftechnologiestoenableefficient
Smarthome useofresources,includingelectricity,whilecreatinga
comfortableenvironmentforitsoccupants.
Thesmartgridparadigmallowsconsumerstofindouttheirenergyusagepatterns.
Consequently,consumerscancontroltheirconsumptionanduseenergymoreefficiently.
Intheimplementationofthesmartgridconcept,demandresponse—forbothhousehold
andindustrialpurposes—playsanimportantrole. Anotherusefultoolisloadforecasting
(seedefinitioninTable1). In[6]theauthorsmarktheimportanceofthisconceptinthe
contextofsmartgrids,asforecastingtheelectricityneededtomeetdemandallowspower
companiestobetterbalancedemandandsupply.Powercompaniesareespeciallyinterested
inachievingaccurateforecastsforthenext24h,whichiscalledloadprofile(seedefinition
inTable1).
Inaddition,inrecentyears,theincreaseddemandforelectricityatcertaintimesof
the day has created several problems. Load forecasting is especially important during
peak hours. Demand response encourages customers to offload non-essential energy
consumptionduringthesepeakhours.
Tofaceloadforecastingchallenges,itisnecessarytousemoderndata-driventech-
niques. Indeed,theincorporationofnewtechnologies,suchasBigData,MachineLearning,
DeepLearning,andtheInternetofThings(IoT),hasupgradedthesmartgridconceptto
anotherlevel,asthesetechnologiesallowforimproveddemandforecastingandautomated
demandresponse.

Sensors2023,23,1467 3of30
Thispaperprovidesaninsightintotheimportanceofdemandforecastingandim-
portant related factors in the context of smart grids, as well as the possibility of using
data-driven techniques for this purpose. More specifically, the authors focus on Deep
Learningtechniques,asithasemergedasagoodoptionfortheimplementationofdemand
forecasting in the context of smart grids. The paper collects some experiences of using
differentDeepLearningtechniquesintheenergydomainforforecastingpurposes. Aneffi-
cientpowersystemmusttakedemandresponseintoaccount. Additionally,accurateload
forecasting,especiallyintheshortterm,isessential,whichiswhyindustrystakeholders
andresearchersareputtingspecialeffortsintoit.
Table1definessomekeywordsrelatedtothetopicofthispaper.
Theremainderofthispaperisorganizedasfollows.Section2presentsthereasonswhy
demandforecastingisimportantinthecontextofsmartgrids. Section3describesthemost
importantfactorsinrelationtodemandforecasting.Section4presentsthedifferentpossible
classificationsofdemandforecastingtechniques. Section5providessomefundamentals
andconceptsusefultounderstandtheDeepLearningmodelscommonlyusedintheenergy
domain. Section6collectsdifferentexperiencesofusingthesemodelsinthecontextof
smartgridsforforecastingpurposes. Finally,Section7summarizesthemainconclusions
ofthiswork.
2. TheImportanceofDemandForecasting
In[7]theauthorssummarizethemainrequirementsofsmartgridsasfollows: flexible
enough to meet users’ needs, able to manage uncertain events, accessible for all users,
reliableenoughtoguaranteehigh-qualityenergydeliverytoconsumers,andinnovative
enoughtomanageenergyefficiently.
Withtheserequirementsinmind,smartgridsshouldaimtodeveloplow-cost,easy-
to-deploytechnicalsolutionswithdistributedintelligencetooperateefficientlyintoday’s
increasinglycomplexscenarios. Toupgradeatraditionalelectricalgridintoasmartgrid,
intelligentandsecurecommunicationinfrastructuresarenecessary[4].
Accordingtothestudypresentedin[8],forecastingcanbeappliedintwomainareas:
gridcontrolanddemandresponse. In[9],theauthorshighlightthatforecastingmodelsare
essentialtoprovideoptimalqualityoftheenergysupplyatthelowestcost. Inaddition,
real-timeinformationonusers’energyconsumptionpatternswillenablemoresophisticated
andefficientforecastingmodelstobeapplied. Forecastingmustalsoconsidertheneed
tomanageconstantlychanginginformation. In[10],theauthorshighlightthat,withthe
smartgrid,demandresponseprogramscanmakethegridmorecostefficientandresilient.
Theauthorsin[11]remarkthatthereareimportantchallengesindemandforecasting
due to the uncertainties in the generation profile of distributed and renewable energy
generationresources. Infact,increasingattentionisbeingpaidtoloadforecastingmodels,
especiallydealingwithrenewableenergysources(solarradiation,wind,etc.)[9].
Thedistributedgenerationparadigmfacilitatestheuseofrenewableenergysources
thatcanbeplacednearconsumptionpoints. Whenusingthisparadigm,smartgridshave
multiplesmallplantsthatsupplyenergytotheirsurroundings. Consequently,thedepen-
denceonthedistributionandtransmissiongridissmaller[9]. However,thisparadigm
makesgridcontrolevenmoreuncertain,especiallywhenthedistributedgenerationsources
arerenewableandconsequentlyhavearandomnature. Despitethisdifficulty,theshare
inenergyproductionofvariablerenewableenergysourcesisexpectedtoincreaseinthe
comingyears[12].
Anotherkeyelementaremicrogrids(seedefinitioninTable1)[13,14]. Basedonthis
concept,andtakingintoconsiderationtheintelligencedeployedinbuildings,newconcepts
haveemergedincludingsmarthomes(seedefinitioninTable1)andsmartbuildings(see
definitioninTable1). Buildingstodayarecomplexcombinationsofstructures,systems,
andtechnology. Technologyisagreatallyinoptimizingresourcesandimprovingsafety.
Advancesinbuildingtechnologiesarecombiningnetworkedsensorsanddatarecording
in innovative ways [15]. Modern facilities can adjust heating, cooling, and lighting to

Sensors2023,23,1467 4of30
maximize energy efficiency, providing alsodetailed reportsof energyconsumption. In
thesenewsmartenvironments(seedefinitioninTable1),sensorsandsmartdevicesare
deployed to obtain enough information about the users’ energy consumption patterns.
Onceagain,thisrequiresforecastingmodelsthatmustbeappliedtothespecificvariables
ofthescenariotobecontrolled.
Forecastingmodelswillallowtoconsidervariables(climatic,social,economic,habit-
related,etc.) thatcaninfluencetheaccuracyofforecasts[9]. Theseauthorsremarkthat
energydemandestimatesindisaggregatedscenarios,suchasresidentialusersinsmart
buildings, are more complex compared to energy demand estimates for an aggregated
scenario,suchasacountry. Disaggregatingthedemandalsofacilitatestheimplementation
of demand response, as different prices can be offered based on the criteria set by the
powercompany.
Thegradualintegrationofintelligenceatthetransmission,distributionandend-user
levels of the electricity system aims to optimize energy production and distribution to
adjustproducers’supplytoconsumers’demand. Moreover,smartgridsseektoimprove
fault detection algorithms [16]. Accurate demand forecasts are very useful for energy
suppliersandotherstakeholdersintheenergymarket[17]. Infact,loadforecastinghas
been one of the main problems faced by the power industry since the introduction of
electricpower[18].
3. ImportantFactorsinDemandForecasting
Electricitydemandisaffectedbydifferentvariablesordeterminants. Thesevariables
includeforecastinghorizons,thelevelofloadaggregation,weatherconditions(humidity,
temperature,windspeed,andcloudiness),socio-economicfactors(industrialdevelopment,
populationgrowth,costofelectricity,etc.),customertype(residential,commercial,and
industrial),andcustomerfactorsinrelationtoelectricityconsumption(characteristicsof
theconsumer’selectricalequipment)(e.g.,[19–23]).
Tofullyunderstanddemandforecastingtechniquesandobjectives,itisnecessarytoex-
aminethesedeterminants. Inthissection,theauthorswillfocuson(1)period,(2)economic
issues,(3)weatherconditions,and(4)customer-relatedfactors.
3.1. PeriodorForecastingHorizon
Theperiodcommonlyreferredasforecastinghorizonisprobablyoneofthefactors
thathasthegreatestimpact.
Accordingtodifferentauthors(e.g.,[17,24]),demandforecastingcanbeclassifiedinto
threecategorieswithrespecttotheforecastinghorizon:
• Short-term(typicallyonehourtooneweek).
• Medium-term(typicallyoneweektooneyear).
• Long-term(typicallymorethanoneyear).
Factors affecting short-term demand forecasting usually do not last long, such as
suddenchangesofweather[22]. Thequalityofshort-termdemandforecastingiscriticalfor
electricitymarketplayers[20]. Ontheotherhand,theinfluencingfactorsofmedium-term
demandforecastingoftenhaveacertaintimeduration,suchasseasonalweatherchanges.
Finally,thefactorsinfluencinglong-termdemandforecastinglastforalongtime,typically
several forecast periods, e.g., changes in Gross Domestic Product (GDP) [22]. Indeed,
economicfactorshaveanimportantimpactonlong-termdemandforecasting,butalsoon
mediumandshort-termforecasting[25].
The authors of [26] identify the following categories in relation to the forecasting
horizon:
• Veryshort-term(typicallysecondsorminutestoseveralhours).
• Short-term(typicallyhourstoweeks).
• Medium-termandlong-term(typicallymonthstoyears).

Sensors2023,23,1467 5of30
Accordingtotheseauthors,veryshort-termdemandforecastingmodelsaregenerally
usedtocontroltheflow. Short-termdemandforecastingmodelsarecommonlyusedto
matchsupplyanddemand. And,finally,medium-termandlong-termdemandforecasting
modelsaretypicallyusedtoplanassetutilities.
Theauthorsin[27]showedthattheloadcurveofgridstationsisperiodic,notonly
inthedailyloadcurve,butalsointheweekly,monthly,seasonal,andannualloadcurves.
Thisperiodicitymakesitpossibletoforecasttheloadquiteeffectively.
Demandalsoreflectsthedailylifestyleoftheconsumer[28].Consumers’dailydemand
patterns are based on their daily activities, including work, leisure and sleep hours. In
addition, there are other demand variations patterns over time. For example, during
holidaysandweekends,demandinindustriesandofficesissignificantlylowerthanduring
weekdaysduetoadrasticdecreaseinactivity. Finally,powerdemandalsovariescyclically
dependingonthetimeoftheyear,dayoftheweek,andtimeofday[22].
3.2. Socio-EconomicFactors
Socio-economicfactors,includingindustrialdevelopment,GDP,andthecostofelec-
tricity, also significantly affect the evolution of demand. Indeed, as mentioned in the
previoussection,economicfactorsconsiderablyaffectlong-termdemandforecasts,and
alsohaveanimportantimpactonmedium-andshort-termforecasts.
Forexample,industrialdevelopmentwillundoubtedlyincreaseenergyconsumption.
Thesamewillbetrueforpopulationgrowth. Thismeansthatthereisapositivecorrelation
betweenindustrialdevelopment,orpopulationgrowth,andenergyconsumption.
GDP is an indicator that captures a country’s economic output. Countries with a
higherGDPgenerateagreaterquantityofgoodsandservicesandwillconsequentlyhave
ahigherstandardoflivingandlifestylehabits,whichwillstimulateenergydemand.
Another economic factor to consider is cost, as it also affects demand. For exam-
ple, when the price of electricity decreases, wasteful electricity consumption tends to
increase[22].
Thecostofelectricitydependsondifferentfactorsandisshapedindifferentways.
Forexample,insomecountriessuchasSpain,therearetwomarkets(regulatedandfree)
forelectricity. Inthefreemarket,thecostofelectricityisestablishedinthecontractsigned
by the consumer. In contrast, in the regulated market, the price of electricity depends
onsupplyanddemand. Thepriceisupdatedhourlyandfluctuates. Fromthedemand
side,themoreelectricityisdemanded,themoreexpensiveitis. Whenlesselectricityis
demanded,thecheaperitis. Normally,itischeaptouseelectricityatdawnandexpensive
todoitwheneveryoneelseisusingit(e.g.,atdinnertime).
But it is not only the demand that influences prices, but also the supply of energy.
Thereasonisthatvariationsinthepriceofelectricityontheregulatedmarketarecaused
by differences between demand and supply. Consequently, supply must consider the
differentwaysofgeneratingelectricity,whichhavedifferentcosts.Thecheapestiselectricity
generatedbyrenewableenergiessuchassolar,windandhydroelectric.Thepriceofnuclear
energyisalsolow;however,inmanycountries(e.g.,Spain),nuclearenergydoesnotcover
allenergyneeds. Thermal(coal),cogeneration,orcombinedcycle—whosemainfuelis
gas—tendstobemoreexpensive. Itisalsoimportanttorememberthatthemainsourcesof
renewableenergy,suchashydroelectricorwind,dependonuncontrollableexternalfactors.
Forexample,sufficientrainfallisessentialtoproducehydroelectricpower. However,there
isnowaytocontroltheweathertomakeitfavorableforproducingelectricalenergy. Given
the above, the price is determined by the price of a mix of different sources of power
generation,fromcheapesttomostexpensive,untiltheentireenergydemandismet.
3.3. WeatherCondition
Therearedifferentweathervariablesrelevantfordemandforecastingsuchastemper-
ature,humidity,andwindspeed.

Sensors2023,23,1467 6of30
Theinfluenceofweatherconditionsondemandforecastinghasattractedtheinterestof
manyresearchers. Asanexample,theauthorsin[29]proposeddifferentmodelstoforecast
nextday’saggregatedloadusingArtificialNeuralNetworks(ANNs),consideringthemost
relevantweathervariables—morespecifically,meantemperature,relativehumidity,and
aggregatesolarradiation—toanalyzetheinfluenceofweather.
Some authors have studied the relationship between temperature and electricity
consumptionandclaimthatthecorrelationbetweentemperatureandtheelectricityload
curveispositive,especiallyinsummer(e.g.,[25]).
Currently,heatwaveshavebecomemorecommonaroundtheworld,aswellasthe
possibilityofextremetemperatures.Inaddition,heatwavesarenotonlymorefrequent,but
alsomoreintenseandlongerlasting. Moreover,thenightsaregettingwarmer,whichisan
addedproblem. Themaineffectofaheatwaveisanincreaseinenergyconsumptionasthe
consumerturnsontheairconditioningmoreandforlongerperiodsoftime. Additionally,
coolingsystemsmustworkharderastheymustcopewithhighertemperatures.
Duringthesummer,heatwavesforcethegridtobeatmaximumcapacity. Infact,one
ofthewaysinwhichaheatwaveaffectsconsumptionisthroughtheincreasedsaturation
oftheelectricalgrid. Whilecoldwavesarecounteractedwithelectricity,gas,wood,etc.,
heatwavescanonlybefoughtwithelectricity. Inotherwords,thedevicesthatconsumers
useforcoolingaremainlypoweredbyelectricity. Forthisreason, heatwavesgenerate
morestressonpowerlines,aswellashigherconsumption.
Itshouldbenotedthat,incoldercountries,theincreaseinconsumptionduringaheat
waveisusuallylower. Thisisbecausetheinstallationofairconditioningsystemsisnotas
commonasinwarmercountries. However,thesecoldercountriesarefacingheatwaves
thatdidnotoccurinpreviousyears(beforeclimatechange)andthisiscausingthemall
typeofproblems,astheyarelessprepared. Thissituationisforcingthesecountriestomake
changessuchasincreasingtheuseofcoolingsystems.
Ontheotherside,experienceoftheharshnessoftemperatureincreaseswithhumidity,
especiallyduringtherainyseasonandsummer. Forthisreason,electricityconsumption
increasesduringhumidsummerdays. Itisalsoimportanttonotethatincoastalareas,such
astheMediterraneanareainSpain,electricityconsumptiontendstobehigher. Thisisboth
becausehousestendtohavemoreelectricalequipmentthaninotherareas,andbecauseof
thehighdegreeofhumidityduetotheproximityofthesea.
Windspeedalsoaffectselectricityconsumption. Whenitiswindy,thehumanbody
feels that the temperature is much lower and more heating is needed, which increases
electricityconsumption. However,itshouldalsobenotedthatwindenergyisoneofthe
main renewable energies. In other words, when there is wind, electricity consumption
increases, but at the same time its price decreases. This is because, as explained in the
previoussection,thepriceoftheelectricityisusuallydeterminedasamixofthedifferent
energysources,fromcheapestenergies(renewables,includingwind,andnuclear)tothe
mostexpensivegenerationsources(thermal,combinedcycle).
Temperature,humidity,andwindaffecttheuseofelectricity. Humidityandtempera-
turearealsothemainweathervariablesusedinelectricitydemandpredictionsystemsto
minimizeoperatingcosts. However,otherfactors,suchasclouds,alsoplayarole. Forex-
ample,duringtheday,whencloudsdisruptsunlightthereisusuallyadropintemperature
and,consequently,higherelectricityconsumption.
3.4. CustomerFactors
Thetypeofcustomer(residential,commercial,andindustrial),aswellasothercus-
tomerfactorsrelatedtoelectricityconsumption(characteristicsoftheconsumer’selectrical
equipment)can alsoaffect demand. This isimportant becausemost energycompanies
have different types of customers (residential, commercial, and industrial consumers),
who have equipment that varies in type and size. These different types of customers
havedifferentloadcurves,althoughtherearesomesimilaritiesbetweencommercialand
industrialcustomers.

Sensors2023,23,1467 7of30
Table2summarizesthemaindeterminantsaffectingelectricitydemanddescribedin
thissection.
Table2.Mainvariablesaffectingelectricitydemand.
Determinant Refersto...
Forecastinghorizon Thetimehorizonforwhichdemandforecastsareprepared.
Industrialdevelopment,populationgrowth,costofelectricity,
Socio-economicfactors andanyothersocio-economicfactorsthatmayinfluence
end-users’demand.
Temperature,humidity,windspeed,andanyotherweather
Weatherconditions
conditionsthatmayinfluenceend-users’demand.
Typeofcustomer(residential,commercial,andindustrial),
Customerfactors characteristicsoftheconsumer’sequipment,andanyother
customerfactorsthatmayaffecttheend-users’demand.
4. ClassificationofDemandForecastingTechniques
Thissectionclassifiesdemandforecastingmodelsaccordingtothreedifferentcriteria:
(1)period,(2)forecastingobjective,and(3)typeofmodelused.
The first classification focuses on the point of view of the period to be forecasted,
i.e.,theforecastinghorizon. Toselectthiscriterion,theelectricitydemanddeterminants
presentedintheprevioussectionhavebeenconsidered.Thesecondclassificationfocuseson
thepointofviewoftheforecastingobjective,differentiatingbetweenforecastingtechniques
that produce a single value and those that produce multiple values. Finally, the third
classificationfocusesonthepointofviewofthemodelused.
4.1. ClassificationofDemandForecastingTechniquesaccordingtotheForecastingHorizon
Asexplainedintheprevioussection,themainforecastinghorizonsthatcanbeidenti-
fiedarethefollowing:
• Veryshort-term: typicallyfromsecondsorminutestoseveralhours.
• Short-Term: typicallyfromhourstoweeks.
• Medium-Term: typicallyfromaweektoayear.
• Long-Term: typicallymorethanayear.
Themaindifferenceisthescopeofthevariablesusedineachcase. Veryshort-term
forecastingmodelsuserecentinputs(typicallyminutesorhours),short-termforecasting
modelsuseinputstypicallyintherangeofdays,andmediumandlong-termforecasting
modelsuseinputstypicallyintherangeofweeksorevenmonths.
Powercompaniesareparticularlyinterestedinproducingaccurateforecastsforthe
loadprofile(e.g.,[9,30,31]). Thisisbecauseitcandirectlyaffecttheoptimalscheduling
of power generation units. However, due to the non-linear and stochastic behavior of
consumers,theloadprofileiscomplex,andalthoughresearchhasbeendoneinthisarea,
accurateforecastingmodelsarestillneeded[32].
4.2. ClassificationofDemandForecastingTechniquesbyForecastingObjective
Forecasting models can be also classified according to the number of values to be
forecasted. Inthiscase,twomaincategoriescanbeconsidered.
Thefirstcategoryreferstoforecastingtechniquesthatproduceonlyonevalue(e.g.,
nextday’stotalload, nextday’speakload, nexthour’sload, etc.). Examplesarefound
in[33,34].
Thesecondcategoryreferstoforecastingtechniquesthatproducemultiplevalues,
e.g.,thenexthours’peakloadplusanotherparameter(e.g.,theaggregateload)ortheload
profile. Examplesarefoundin[35–37].

Sensors2023,23,1467 8of30
Generallyspeaking,one-valueforecastsareusefulforoptimizingtheperformance
of load flows. On the other hand, multiple-value forecasts are mainly used for energy
generationscheduling[9].
4.3. ClassificationofDemandForecastingTechniquesaccordingtotheModelUsed
Themodeltobeusedisusuallydecidedbythepractitioner. Intermsofmodels,the
maingroupsarelinearandnon-linearapproaches.
LinearmodelsincludeSpectralDecomposition(SD),PartialLeast-Square(PLS),Auto-
RegressiveIntegratedMovingAverage(ARIMA),Auto-RegressiveConditionalHeteroscedas-
ticity (ARCH), Auto-Regressive (AR), Auto-Regressive and Moving Average (ARMA),
MovingAverageModel(MAM),LinearRegression(LR),andState-Space(SS).
Linear techniques have progressively lost importance and interest in favor of non-
linear techniques based on ANNs. Deep Learning models use ANNs, inspired by the
human nervous system. These models can learn patterns from the data generated and
forecastpeakdemandinthecontextoftoday’scomplexsmartscenarios, wherealarge
amountofdataiscontinuouslygeneratedfromdifferentsources[7].
Table3summarizesthecriteriacommonlyusedtoclassifydemandforecastingmodels.
Table3.Maincriteriacommonlyusedtoclassifydemandforecastingmodels.
Criteria Refersto...
Thetimehorizonforwhichelectricitydemandforecastsare
prepared.Themainforecastinghorizonsare:
- veryshort-term:fromsecondsorminutestoseveralhours.
Forecastinghorizon
- short-term:fromhourstoweeks.
- medium-term:fromaweektooneyear.
- long-term:morethanoneyear.
Thenumberofvaluestobeforecasted,mainlyonevalue(e.g.,
Aimofprediction nextday’stotalload,nextday’speakload,nexthour’sload,etc.)
ormultiplevalues(e.g.,theloadprofile).
Mainlylinear(e.g.,SD,PLS,ARIMA,ARCH,AR,ARMA,MAM,
Typeofmodelused
LR,SS,etc.),andnon-linearANN-basedmodels.
5. FundamentalsandConceptsofMachineLearningandDeepLearningSystems
ArtificialIntelligenceisacomplexconceptthat, inanutshell, referstomachinein-
telligence[38]. Unlikehumans,ArtificialIntelligencecanidentifypatternswithinalarge
amount of data using a quite limited amount of time and resources. Furthermore, the
computationalcapacityofmachinesdoesnotdecreasewithtimeand/orfatigue[39].
ArtificialIntelligencesystemsusedifferenttypeoflearningmethods,suchasMachine
LearningandDeepLearning.
5.1. MachineLearning
MachineLearningalgorithmsarepre-trainedtoproduceanoutcomewhenconfronted
with a never-before-seen dataset or situation [40]. However, the computer needs more
examples to learn than humans do [41]. Machine Learning allows the introduction of
intelligentdecision-makinginmanyareasandapplicationswheredevelopingalgorithms
wouldbecomplexandexcellentresultsareneeded[42].
TherearedifferentcategoriesofMachineLearningalgorithmsincludingsupervised,
semisupervised,unsupervised,andreinforcementlearning. Thesedifferentcategoriesof
algorithmsarebrieflydescribedbelow.
5.1.1. SupervisedLearning
Afterbeingtrainedwithasetoflabelleddataexamples,thesealgorithmscanpredict
labelvalueswhentheinputhasunlabeleddata. Theproblemstypicallyassociatedwith
thistypeoflearningare(1)regressionand(2)classification[43].

Sensors2023,23,1467 9of30
Inregressionthealgorithmfocusesonunderstandingtherelationshipbetweendepen-
dentandindependentvariables. Inclassification,thealgorithmisusedtopredicttheclass
labelofthedata. Commonclassificationproblemsinclude(1)binaryclassification,between
twoclasslabels;(2)multi-classclassification,betweenmorethantwoclasslabels;and(3)
multi-labelclassificationwhereonepieceofdataisassociatedwithseveralclassesorlabels,
asopposedtotraditionalclassificationproblemswithmutuallyexclusiveclasslabels[44].
MethodsusedforsupervisedlearningincludeLinearDiscriminantAnalysis(LDA),
NaiveBayes(NB),K-nearestNeighbors(KNN),SupportVectorMachine(SVM),Decision
Tree(DT),RandomForest(RF),AdaptiveBoosting(AdaBoost),ExtremeGradientBoosting
(XGBoost),StochasticGradientDescent(SGD),Rule-basedClassification(forclassification);
andLR,Non-LinearRegression(NLR),andOrdinaryLeastSquaresRegression(OLS)(for
regression)[44,45]. Themostwidelycitedandimplementedsupervisedlearnersinthe
literatureareDT,NB,andSVMalgorithms[46].
Someinterestingpracticalapplicationsaretextclassification,predictingthesentiment
ofatext(suchasaTweetorothersocialmedia),assessingtheenvironmentalsustainability
ofclothingproducts[47],characterizing,predicting,andtreatingmentaldisorders[48],
andestimatingpeakenergydemand.
5.1.2. UnsupervisedLearning
This type of learning uses unlabeled data. In this case, the system explores the
unlabeleddatatofindhiddenstructures,ratherthanpredictingthecorrectoutput. This
typeoflearningisnotdirectlyapplicabletoregressionorclassificationproblems,asthe
possiblevaluesoftheoutputareunknown[49]. Instead,itisoftenusedfor(1)clustering,
(2)association,and(3)dimensionalityreduction[43].
Clusteringallowsunlabeleddatatobegroupedbasedontheirsimilaritiesordiffer-
ences[49,50]. Associationusesdifferentrulestoidentifynewandrelevantinsightsbetween
the objects of a set. Finally, dimension reduction allows a reduction of the number of
features(ordimensions)ofadatasettoeliminateirrelevantorlessimportantfeaturesand
thusreducethecomplexityofthemodel[44]. Thisreductioninthenumberoffeatures
canbedonebykeepingasubsetoftheoriginalfeatures(featureselection)orbycreating
completelynewfeatures(featureextraction).
ThemostpopularclusteringalgorithmisprobablyK-meansclustering,wherethek
valuerepresentsthesizeofthecluster[44,45,51]. AssociationalgorithmsincludeApriori,
EquivalenceClassTransformation(ECLAT),andFrequentPattern(F-P)Growthalgorithms.
Finally,dimensionalityreductiontypicallyusestheChi-squaredtest,AnalysisofVariance
(ANOVA)test,Pearson’scorrelationcoefficient,RecursiveFeatureElimination(RFE)for
featureselection,andPrincipalComponentsAnalysis(PCA)forfeatureextraction.
According to [46], the most commonly used unsupervised learners are K-means,
hierarchicalclustering,andPCA.
These unsupervised learners can have many practical applications, such as facial
recognition,customerclassification,patientclassification,detectingcyber-attacksorintru-
sions[52],anddataanalysisintheastronomicalfield[53].
5.1.3. SemisupervisedLearning
Conceptuallysituatedbetweensupervisedandunsupervisedlearning,thistypeof
learningallowsthetakingadvantageofthelargeunlabeleddatasetsthatareavailablein
somecasescombinedwith(usuallysmaller)amountsoflabelleddata[54,55]. Thisopens
upinterestingpossibilitiesaslabelleddataareoftenscarce,whileunlabeleddataaremore
frequent,andasemisupervisedlearnercanobtainbetterpredictionsthanthoseproduced
usingonlylabelleddata[44].
Candidateapplicationsarethosewherethereisonlyasmallsetoflabelledexamples,
andmanymoreunlabeledones,orwhenthelabellingeffortistoohigh. Anexampleis
medicalimaging,whereasmallamountoftrainingdatacanprovidealargeimprovement
inaccuracy[43,56].

Sensors2023,23,1467 10of30
Table 4 compares Supervised and Unsupervised learning, focusing on the type of
inputdatausedineachcase(labeledversusunlabeleddata),andthemaintasksforwhich
bothtypesoflearningareused(classification,regressionversusclustering,association,and
dimensionalityreduction).
Table4.Supervisedvsunsupervisedlearning.
SupervisedLearning UnsupervisedLearning
Itrefersto:
Developingpredictivemodelsbasedoninput Groupingandinterpretingdatabasedon
andoutputdata inputdata
Usesasinput:
Labelleddata Unlabelleddata
Typicallyusedfor:
Clustering
Classification
Association
Regression
Dimensionalityreduction
5.1.4. ReinforcementLearning
Thislearningtechniquedependsontherelationshipbetweenanagentperformingan
activityanditsenvironment,whichprovidespositiveornegativefeedback[57,58]. The
agentmustchooseactionsthatmaximizetherewardinthatenvironment. Popularmethods
includeMonteCarlo,Q-learning,andDeepQ-learning[44].
Traditionallycommonapplicationsincludestrategygamessuchaschess,autonomous
driving,supplychainlogisticsandmanufacturing,geneticalgorithms[57],5Gmobility
management[59],andpersonalizedcaredelivery[60].
5.2. DeepLearning
MachineLearningcanbeclassifiedintoshallowanddeep,consideringthecomplexity
andstructureofthealgorithm[41]. DeepLearningusesmultiplelayersofneuronscom-
posedofcomplexstructurestomodelhigh-leveldataabstractions[61]. Thetypeofoutput
andthecharacteristicsofthedatadeterminethealgorithmtobeusedforaparticularuse
case[62].
DeepLearningusesANNsinspiredbythehumannervoussystem[63]. Thistypeof
networktypicallyhastwolayersofinputandoutputnodesrespectively,connectedtoeach
otherbyoneormorelayersofhiddennodes. PossibledeepANNarchitecturesinclude
MultilayerPerceptron(MLP),LongShort-TermMemoryRecurrentNeuralNetwork(LSTM-
RNN),GenerativeAdversarialNetwork(GAN),andConvolutionalNeuralNetwork(CNN
orConvNet).
Accordingtoourliteraturereview,themostwidelyusedmodelsintheenergydomain
areConvolutionalNeuralNetworks(CNNs),RecurrentNeuralNetworks(RNNs),Long
Short-TermMemory(LSTM),DeepQ-Networks(DQNs)andConditionalRestrictedBoltz-
mannMachine(CRBM)andavariationofanyofthem,acombinationoftwoormoreof
them,orthecombinationofanyofthemwithothertechniques. Thesemodelsarebriefly
describedbelow.
5.2.1. ConvolutionalNeuralNetworks
Thesenetworksarebiologicallyinspirednetworks,liketheordinaryneuralnetworks.
However,inthistypeofnetworktheinputsareassumedtohaveaspecificstructuresuch
asimages[64]. BeingoneofthemostwidelyusedandeffectivemodelsforDeepLearning,
thesenetworksusuallyincludetwotypesoflayers(i.e.,poolingandconvolutionlayers). A
typicalCNNarchitectureusuallyconsistsofaninputlayer,aconvolutionallayer,aMax
poolinglayer,andthefinalfullyconnectedlayer,asshowninFigure1[65].

Sensors 2022, 22, x FOR PEER REVIEW 2 of 37
According to our literature review, the most widely used models in the energy do-
main are Convolutional Neural Networks (CNNs), Recurrent Neural Networks (RNNs),
Long Short-Term Memory (LSTM), Deep Q-Networks (DQNs) and Conditional Restricted
Boltzmann Machine (CRBM) and a variation of any of them, a combination of two or more
of them, or the combination of any of them with other techniques. These models are briefly
described below.
5.2.1. Convolutional Neural Networks
These networks are biologically inspired networks, like the ordinary neural net-
works. However, in this type of network the inputs are assumed to have a specific struc-
ture such as images [64]. Being one of the most widely used and effective models for Deep
Learning, these networks usually include two types of layers (i.e., pooling and convolu-
Sensors2023,23,1467 tion layers). A typical CNN architecture usually consists of an input layer, a con11voofl3u0tional
layer, a Max pooling layer, and the final fully connected layer, as shown in Figure 1 [65].
FiFgiguurere 11. .SSttaannddaarrdd CCoonnvvoolulutitoionnalaNl NeueruarlaNl eNtwetowrkoArkr cAhirtcehctiutercet[u6r5e] .[65].
Thetotalinputtothejthfeaturemapoflayerlatposition(x,y)canbeexpressed[66]:
The total input to the jth feature map of layer l at position (x,y) can be expressed [66]:
v
(l)
(x,y) =
∑ l F(cid:3039)∑ −1(cid:3007)
k
(cid:2879)((cid:2869) l)
(u,v)·O
(l−1)
(x−u, y−v)+b
(l)
(1)
j𝑣((cid:3039))(𝑥,𝑦) =(cid:3533) (cid:3533)ji 𝑘((cid:3039))(𝑢,i𝑣)∙𝑂((cid:3039)(cid:2879)(cid:2869))(𝑥−𝑢,𝑦−j𝑣)+𝑏 ((cid:3039)) (1)
(cid:3037) i=1u,v=0 (cid:3037)(cid:3036) (cid:3036) (cid:3037)
(cid:3036)(cid:2880)(cid:2869)(cid:3048),(cid:3049)(cid:2880)(cid:2868)
Convolutionallayeroutput:
Convolutional layer output:
(cid:16) (cid:17)
O
i
(l−
𝑂
1) (((cid:3039)x(cid:2879),(cid:2869)y))
(𝑥
=
,𝑦
f
) =
v (
j
l
𝑓
) (
(cid:3435)
x
𝑣
,((cid:3039)y))
(𝑥,𝑦)(cid:3439)
(2)
(2)
(cid:3036) (cid:3037)
PPoooolliinngg llaayyeerr oouuttppuut:t:
O (l𝑂+(1(cid:3039))(cid:2878) ( (cid:2869) x ) ,(y𝑥),𝑦=) =mamx axO (l)𝑂(x ((cid:3039) · ) s(+𝑥∙u𝑠,+y·𝑢s +,𝑦v∙)𝑠+𝑣) (3) (3)
i (cid:3036) u,v=(cid:3048)0,,(cid:3049)..(cid:2880).,(cid:2868)G,−…,1(cid:3008)(cid:2879)i(cid:2869) (cid:3036)
w w he h r e e r e 𝑂 O(cid:3036) ((cid:3039) ( (cid:2879) l− (cid:2869)) 1 () ( 𝑖 i = = 1 1 , , … .. , . 𝑙 , ) l) r r e e p p r re e s s e e n n t t s s fe f a e t a u t r u e re m a m p a s p o s n o th n e t ( h l e + ( 1 l ) + l 1 a ) y e la r; y k e(r l ;) ( 𝑘 u(cid:3037), ( (cid:3036) (cid:3039) v ) ) (𝑢 d , e 𝑣 n ) o t d es enotes
trainable c
i
onvolution kernel;
𝑏((cid:3039))
indicates trainable bias; G is poolin
ji
g size; and S means
trainableconvolutionkernel;b (l) in (cid:3037) dicatestrainablebias;Gispoolingsize;andSmeansstride.
stride. j
Differentarchitecturaldesignsexploretheeffectofmultileveltransformationsonthe
Different architectural designs explore the effect of multilevel transformations on the
learningabilityofsuchnetworks. OneofthesepossiblearchitecturaldesignsisPyramid.
learning ability of such networks. One of these possible architectural designs is Pyramid.
The Pyramid Architecture of Convolutional Neural Network is commonly known as
TPhyer Pamyriadm-CiNd NAr[6c6h]i.tecture of Convolutional Neural Network is commonly known as Pyr-
amid-CNN [66].
5.2.2. RecurrentNeuralNetworks
Sensors 2022, 22, x FOR PEER REVIEW 2 of 37
5.2.2. IRnetchuisrrteynpte Nofenuertawl oNrke,twthoerckosn nectionsbetweennodesformadirectedorundirected
graphalongatimesequence. Figure2showsatypicalRNNstructure[65].
In this type of network, the connections between nodes form a directed or undirected
graph along a time sequence. Figure 2 shows a typical RNN structure [65].
F F ig ig u u r r e e 2 2 . . F F r r a a m m e e w w o or r k k o o f f a a R R e e cu cu rr r e r n e t n N t N eu e r u a r l a N l e N tw et o w rk o : rk In : p I u n t p l u a t y e la r y ( e X rt ) ( ; X o t u ); t p o u u t tp la u y t e r la ( y O etr ) ; ( h O id t) d ; e h n idden
la la y y e e r r ( ( S S t)t; ) ; p p a a r r a a m m e e t t e e r r m m a a t t r r i i c c e e s s a a n n d d v v ec e t c o t r o s rs (U (U ,V , , V W , ) W ;a ) c ; t a iv c a ti t v io a n tio fu n n f c u ti n o c n ti o o f n o o u f t p o u u t t l p a u y t e r la (σ yye ) r ; a (σ n y d ); and
activationfunctionofhiddenlayer(σ )[65].
activation function of hidden layer (hσh) [65].
This network can use a gating mechanism called Gated Recurrent Units (GRUs) and
introduced in 2014 by the authors in [67]. GRU are like LSTM networks but with a forget-
ting gate and fewer parameters as they lack an output gate.
Another variation of this type of network, proposed by Elman [68], is the Elman RNN
that includes modifiable feedforward connections and fixed recurrent connections. It uses
a set of context nodes to store internal states, which gives it certain unique dynamic char-
acteristics over static ones [69].
5.2.3. Long Short-Term Memory
These networks are a special kind of RNN. Unlike standard feedforward neural net-
works, these networks have feedback connections, and can even process entire sequences
of data (such as speech or video), in addition to individual data points (such as images).
This type of RNN contains an input layer, a recurrent hidden layer, and an output
layer, with a memory block structure as shown in Figure 3 [70].
Figure 3. LSTM memory block [70].
The LSTM memory block can be described according to the following equations [70]:
𝑖 (cid:3047) =𝜎(𝑊 (cid:3036) 𝑥 (cid:3047) +𝑈 (cid:3036) ℎ (cid:3047)(cid:2879)(cid:2869) +𝑏 (cid:3036) ) (4)

Sensors 2022, 22, x FOR PEER REVIEW  2 of 37

Figure 2. Framework of a Recurrent Neural Network: Input layer (Xt); output layer (Ot); hidden
layer (St); parameter matrices and vectors (U, V, W); activation function of output layer (σy); and
Sensors2023,23,1467 activation function of hidden layer (σh) [65].  12of30
This network can use a gating mechanism called Gated Recurrent Units (GRUs) and
introduced in 2014 by the authors in [67]. GRU are like LSTM networks but with a forget-
ThisnetworkcanuseagatingmechanismcalledGatedRecurrentUnits(GRUs)and
ting gate and fewer parameters as they lack an output gate.
introducedin2014bytheauthorsin[67].GRUarelikeLSTMnetworksbutwithaforgetting
Another variation of this type of network, proposed by Elman [68], is the Elman RNN
gateandfewerparametersastheylackanoutputgate.
that inAclnuodtehse mr voadriifaitaiobnle ofefetdhifsortwypaerdo fconnetnwecotriko,nps raonpdo sfeixdedby reEclumrarenn[t6 c8o],ninsetchteioEnlsm. Iatn uses
a sReNt Nof tchoanttinexcltu ndoedsemso tdoi fistaobrlee ifneetedrfnorawl satradtecos,n wnehcitciohn gsiavneds fiitx ceedrtraeicnu rurneniqtucoen dnyenctaiomnisc. cIthar-
acuteserissaticsse toovfecro snttaetxict noondeess [6to9]s.t oreinternalstates,whichgivesitcertainuniquedynamic
characteristicsoverstaticones[69].
5.2.3. Long Short-Term Memory
5.2.3. LongShort-TermMemory
These networks are a special kind of RNN. Unlike standard feedforward neural net-
These networks are a special kind of RNN. Unlike standard feedforward neural
works, these networks have feedback connections, and can even process entire sequences
networks,thesenetworkshavefeedbackconnections,andcanevenprocessentiresequences
of data (such as speech or video), in addition to individual data points (such as images).
ofdata(suchasspeechorvideo),inadditiontoindividualdatapoints(suchasimages).
This type of RNN contains an input layer, a recurrent hidden layer, and an output
ThistypeofRNNcontainsaninputlayer, arecurrenthiddenlayer, andanoutput
layer, with a memory block structure as shown in Figure 3 [70].  layer,withamemoryblockstructureasshowninFigure3[70].

Figure3.LSTMmemoryblock[70].
Figure 3. LSTM memory block [70].
TheLSTMmemoryblockcanbedescribedaccordingtothefollowingequations[70]:
The LSTM memory block can be described according to the following equations [70]:
|     |     |             | = σ(       | +                                | + )                             |            |     |
| --- | --- | ----------- | ---------- | -------------------------------- | ------------------------------- | ---------- | --- |
|     |     | i t         | W (i𝑊 x    | t U +i h 𝑈t−                     | ℎ1 b +i                         |            | (4) |
|     |     |             | 𝑖 = 𝜎      | 𝑥                                |                                 | 𝑏 )        | (4) |
|     |     |             | (cid:3047) | (cid:3036) (cid:3047) (cid:3036) | (cid:3047) (cid:2879)(cid:2869) | (cid:3036) |     |
|     |     |             | (cid:16)   |                                  | (cid:17)                        |            |     |
|     |     | f t         | = σ W x    | t +U h t−1                       | +b                              |            | (5) |
|     |     |             | f          | f                                | f                               |            |     |
|     | c = | f (cid:12)c | +i         | (cid:12)g(W x                    | +U h                            | +b )       | (6) |
|     | t   | t           | t−1 t      | c t                              | c t−1                           | c          |     |
|     |     | O t = σ(W   | x t +U     | h t−1 +V                         | c t +b                          | )          | (7) |
|     |     |             | O          | O                                | O                               | O          |     |
|     |     |             | =O         | (cid:12)h(c                      | )                               |            |     |
|     |     |             | h t        | t t                              |                                 |            | (8) |
  wherex isthemodelinputattimet;W,W,W ,W ,U,U,U ,U ,V areweightmatrices;
| t   |     |     | i   | f c 0 | i f | c 0 0 |     |
| --- | --- | --- | --- | ----- | --- | ----- | --- |
b,b,b ,b arebiasvectors;i ,f ,0 arerespectivelytheactivationsofthethreegatesattime
| i f c 0 |     | t t | t   |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- |
t;c isthestateofmemorycellattimet;h istheoutputofthememoryblockattimet;(cid:12)
| t   |     |     |     | t   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
representsthescalarproductoftwovectors;σ(x)isthegateactivationfunction;g(x)isthe
cellinputactivationfunction;h(x)isthecelloutputactivationfunction.
ApossibleextensionofthismodelistheBidirectionalLSTM(B-LSTM).Theaimofthis
typeofLSTMnetworkistoanalyzesequencesfrombothfront-to-backandback-to-front,
i.e.,thesequenceinformationflowsinbothdirectionsbackwardsandforwards,unlikeina
normalLSTM.

Sensors 2022, 22, x FOR PEER REVIEW  2 of 37

|     |     |     |     |     |     |              |                | 𝑓 =                               | 𝜎(𝑊 𝑥                 | +𝑈                                        | ℎ                                         | +𝑏 )                  |                                                 |     | (5) |
| --- | --- | --- | --- | --- | --- | ------------ | -------------- | --------------------------------- | --------------------- | ----------------------------------------- | ----------------------------------------- | --------------------- | ----------------------------------------------- | --- | --- |
|     |     |     |     |     |     |              |                | (cid:3047)                        | (cid:3033)            | (cid:3047)                                | (cid:3033) (cid:3047)(cid:2879)(cid:2869) | (cid:3033)            |                                                 |     |     |
|     |     |     |     |     |     | 𝑐 (cid:3047) | = 𝑓 (cid:3047) | ⊙𝑐 (cid:3047)(cid:2879)(cid:2869) | +𝑖 (cid:3047) ⊙𝑔(𝑊𝑥   |                                           | (cid:3030) (cid:3047) +𝑈                  | (cid:3030) ℎ          | (cid:3047)(cid:2879)(cid:2869) +𝑏 (cid:3030) )  |     | (6) |
|     |     |     |     |     |     |              | 𝑂              | = 𝜎(𝑊                             | 𝑥 +𝑈                  | ℎ                                         | +𝑉                                        | 𝑐 +𝑏                  | )                                               |     | (7) |
|     |     |     |     |     |     |              | (cid:3047)     |                                   | (cid:3016) (cid:3047) | (cid:3016) (cid:3047)(cid:2879)(cid:2869) |                                           | (cid:3016) (cid:3047) | (cid:3016)                                      |     |     |
|     |     |     |     |     |     |              |                |                                   | ℎ =                   | 𝑂 ⊙ℎ(𝑐                                    | )                                         |                       |                                                 |     |     |
|     |     |     |     |     |     |              |                |                                   | (cid:3047)            | (cid:3047)                                | (cid:3047)                                |                       |                                                 |     | (8) |
where x is the model input at time t; W, W, W, W , U, U, U, U , V  are weight matrices;
|     |     |     | t   |     |     |     |     |     | i   | f c | 0   | i f | c 0 0 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
b, b, b, b  are bias vectors; i, f, 0 are respectively the activations of the three gates at time
|     |     | i f | c 0 |     |     |     | t t | t   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t; c is the state of memory cell at time t; h is the output of the memory block at time t; ⊙
|     |     | t   |     |     |     |     |     |     | t   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
represents the scalar product of two vectors; 𝜎(𝑥) is the gate activation function; g(x) is
the cell input activation function; h(x) is the cell output activation function.
A possible extension of this model is the Bidirectional LSTM (B-LSTM). The aim of
this type of LSTM network is to analyze sequences from both front-to-back and back-to-
front, i.e., the sequence information flows in both directions backwards and forwards, un-
like in a normal LSTM.
Sensors2023,23,1467 13of30
5.2.4. Deep Q Network and Dueling Deep-Q Network
Deep Q Network (DQN) and Dueling Deep-Q Network (DDQN) are a type of ANN
|     |     | 5.2.4. | DeepQNetworkandDuelingDeep-QNetwork |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------ | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
using the Deep Q learning algorithm, which is popular in reinforcement learning. In a
DeepQNetwork(DQN)andDuelingDeep-QNetwork(DDQN)areatypeofANN
duuseinligntgh enDeteweporQk ltehaernrein agrael gtowrioth smtr,ewamhicsh tois speoppaurlaatreilny reeisntfimorcaetme ethnte lesatarntein-vga.lIunea as well as
tdhue ealidnvgannettawgoersk ftohre reeaacrhe tawctoiosntr.e aTmhse tmosaeipna orabtjeelcyteivstei moaf tDeteheeps-tQat eN-veatlwueoarks wise ltloa schoose the
btehset aadcvtaionnta gine saf ocreretaacihna scttaioten.. CThoenmsidaienrionbgje cπti vise tohfeD peoepli-cQy Nfoeltlwoworekdis btyo cahno oasgeetnhte in a given
|     |     | environment, the function Q bestactioninacertainstate. |     |     |     |     | Consideringπisthepolicyfollowedbyanagentinagiven can be defined as follows [71]:  |     |     |     |     |     |     |     |     |
| --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
π
|     |     | environment,thefunctionQ |     |     |     |     | canbedefinedasfollows[71]: |     |     |     |     |     |     |     |     |
| --- | --- | ------------------------ | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
π
|     |     |     |     |     |     | 𝑄          | (𝑠,𝑎) | = 𝐸(cid:4670)𝑟 | +𝛾𝑟        | +⋯|𝑆       | =          | 𝑠,𝐴        | = 𝑎,𝜋(cid:4671)#  |     | (9) |
| --- | --- | --- | --- | --- | --- | ---------- | ----- | -------------- | ---------- | ---------- | ---------- | ---------- | ----------------- | --- | --- |
|     |     |     |     |     |     | (cid:3095) |       |                | (cid:2869) | (cid:2870) | (cid:2868) | (cid:2868) |                   |     |     |
|     |     |     |     |     | Q   | π (s, a)   | = E[r | +γr            | 2 +...|S   | 0 =        | s,A 0 =    | a,π]#      |                   | (9) |     |
1
where s is a state; a is an action; r is the potential reward; 𝛾 i ∈ (cid:4670)0,1(cid:4671) is a discount factor for
wheresisastate; aisanaction; r isthepotentialreward; γ ∈ [0,1] isadiscountfactor
i
making the immediate reward more important than the futures ones. Therefore, the ob-
formakingtheimmediaterewardmoreimportantthanthefuturesones. Therefore,the
je o c b t je iv ct e iv  o e f o   f Q Q -l - e le a a r r n n i in n g g  is is t   o to m   a m xi a m x i i z m e i t z h e e   o t p h t e im  o i p ze t d im v i a z lu e e d f   u v n a c l t u io e n  f Q u*n (s c , t a i ) o = n m  Q ax *(s, Q a)=m (s, a a x ).   π Q  π (s,a).
π π
FFiigguurree 44 sshhoowwssth tehsec shcehmeemoef aotfy ap itcyaplDicQalN DaQrcNhi taecrtcuhriete[7c1tu].re [71].

FFiigguurree 44.. DDeeeeppQ Q-N-Netewtowrkorakrc ahritcehcittuercet[u7r1e]. [71].
|     |     | 5.2.5. | ConditionalRestrictedBoltzmannMachine |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------ | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
5.2.5. Conditional Restricted Boltzmann Machine
ARestrictedBoltzmannMachine(RBM)isastochasticRNNwithtwolayers,onewith
visibAle uRneitsstarnicdteodn eBwoiltthzbminaanrny hMidadcehniunnei t(sR. TBhMis)t yips eao fsntoectwhaorskticca nRNleaNrn wapitrho btawbioli tlyayers, one
wdiitshtr ivbuistiibonleo uvenritists asnetdo foinnep uwtsi.thR BbMinsaarrye ahvidadrieannt uofnBitosl.t zTmhaisn ntyMpaec hoifn ense(tBwMo)rkan cdan learn a
canbeinsupervisedorunsupervisedmode,dependingonthetasktobeperformed.
probability distribution over its set of inputs. RBMs are a variant of Boltzmann Machines
WhenBMsarerestricted,apairofnodesfromeachofthetwogroupsofunits(visible
andhidden)canhaveasymmetricconnectionbetweenthem,buttherearenoconnections
betweennodesinthesamegroup,allowingformoreefficienttraining. Ontheotherhand,
unrestrictedBMscanhaveconnectionsbetweenhiddenunits.
RBMconsistsofmvisibleunitsV=(v ,... ,v )representingobservabledataandn
|     |     |     |     |     |     |     |     |     | 1   | m   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
hiddenunitsH=(h ,... ,h )capturingdependenciesbetweenobservablevariables,with
|     |     |                              |     |     | 1   | n   |      |                                |     |     |     |     |     |     |     |
| --- | --- | ---------------------------- | --- | --- | --- | --- | ---- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|     |     | theconditionallayerunitsF=(f |     |     |     |     | ,... | ,f ),asitisshowninFigure5[72]. |     |     |     |     |     |     |     |
|     |     |                              |     |     |     |     | 1    | p                              |     |     |     |     |     |     |     |
TheenergyfunctionofCRBMis[73]:
|         |        | ∑m  | ∑K  |       | ∑m  | ∑H  | ∑k  |       | ∑H   |     | ∑H  | ∑F  |          |      |     |
| ------- | ------ | --- | --- | ----- | --- | --- | --- | ----- | ---- | --- | --- | --- | -------- | ---- | --- |
| E(V, H, | F) = − |     |     | vkbk− |     |     |     | vkWkh | −    | h   | b − |     | f D      | (10) |     |
|         |        | i=1 | k=1 | i i   | i=1 | j=1 | k=1 | i     | ij j | j=1 | j j | j=1 | q=1 q qj |      |     |
wheremrepresentsthenumberofitemstheuserrated;Histhenumberofhiddenlayers;
F is the number of conditional layers; K is the highly rating; vk is the binary value of
i
visiblelayerunitiandratingk;h isthebinaryvalueofhiddenunitj;f isthebinaryvalue
|     |     |     |     |     |     |     | j   |     |     |     |     |     | q   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
bk
of conditional layer F; is the bias of rating k with visible layer unit i; b is the bias of
|     |     |     |     |     |     | i   |     |     |     |     |     |     | j   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
featurej;Wk
istheconnectedweightbetweenhiddenlayerHandvisiblelayerV;Disthe
ij
connectedweightbetweenhiddenlayerHandconditionallayerF;D istheconnected
qj
weightbetweenhiddenfeaturejandconditionallayerunitq.

Sensors 2022, 22, x FOR PEER REVIEW 2 of 37
(BM) and can be in supervised or unsupervised mode, depending on the task to be per-
formed.
When BMs are restricted, a pair of nodes from each of the two groups of units (visible
and hidden) can have a symmetric connection between them, but there are no connections
between nodes in the same group, allowing for more efficient training. On the other hand,
unrestricted BMs can have connections between hidden units.
RBM consists of m visible units V=(v ,…, v ) representing observable data and n hid-
1 m
Sensors2023,23,1467 den units H=(h 1 ,…, h n ) capturing dependencies between observable variabl1e4s,o fw30ith the
conditional layer units F=(f ,…, f ), as it is shown in Figure 5 [72].
1 p
FFiigguurree 55.. RReessttrriicctteeddB Booltlztmzmanannnm machacinhein[7e3 []7.3].
In[73],theauthorsintroducedtheFactoredConditionedRestrictedBoltzmannMa-
chines (FCRTBhMes e)nbeyrgayd dfuinngcttihoenc oofn CceRpBtMof ifsa c[7to3r]e:𝐸d,(𝑉m,u𝐻l,ti𝐹p)lic=at−iv∑e,(cid:3040)an∑d(cid:3012)trid𝑣ir(cid:3038)e𝑏c(cid:3038)tio−nal
(cid:3036)(cid:2880)(cid:2869) (cid:3038)(cid:2880)(cid:2869) (cid:3036) (cid:3036)
(10)
interactionstopredict∑m(cid:3040)ult∑ip(cid:3009)leh∑u(cid:3038)ma𝑣n(cid:3038)m𝑊ov(cid:3038)ℎem−en∑t(cid:3009)stylℎes.𝑏 −∑(cid:3009) ∑(cid:3007) 𝑓 𝐷
Finally,DeepBelie (cid:3036) f (cid:2880) N (cid:2869) et (cid:3037) w (cid:2880) o (cid:2869) rk (cid:3038) s (cid:2880) ( (cid:2869) DB (cid:3036) Ns) (cid:3036)(cid:3037) ar (cid:3037) eform (cid:3037)(cid:2880) e (cid:2869) db (cid:3037) y (cid:3037) sever (cid:3037) a (cid:2880) l (cid:2869) RB (cid:3044) M (cid:2880)(cid:2869) ss (cid:3044) tac (cid:3044) k(cid:3285)edontopof
wthheeorteh mer r[e74p]r.esents the number of items the user rated; H is the number of hidden layers;
F is the number of conditional layers; K is the highly rating; 𝑣(cid:3038) is the binary value of
(cid:3036)
6. DeepLearningModelsandDemandForecastingintheContextofSmartGrids
visible layer unit i and rating k; h is the binary value of hidden unit j; f is the binary value
j q
of con
R
d
es
it
e
i
a
o
r
n
ch
al
e r
l
s
ay
h
e
a
r
v e
F;
p r
𝑏
o(cid:3038)p o
is
s e
t
d
he
f o
b
r
i
e
a
c
s
a s
o
ti
f
n
r
g
at
m
in
o
g
d e
k
l s
w
in
ith
th
v
e
i
t
s
w
ib
o
le
m
la
a
y
in
er
a r
u
e
n
as
it
w
i;
h
b
er e
is
D
th
ee
e
p
bias of
(cid:3036) j
Learningtechniquescanbeapplied[8]: (1)demandmanagement(e.g.,[75,76])and(2)grid
feature j; 𝑊(cid:3038) is the connected weight between hidden layer H and visible layer V; D is
control(e.g.,(cid:3036)(cid:3037)[77–79]).
the connected weight between hidden layer H and conditional layer F; D is the connected
Duetothegrowingdemandforenergyfromdifferentsectors,supplyaqnjddemand
weight between hidden feature j and conditional layer unit q.
mustbebalancedintheelectricalgrid. Inthisscenario,smartgridscanplayanimportant
rolebIny [p7r3o]v, itdhineg aautbhidoirrse cintitornoadluflcoewd otfheen Feargcytobreetdw Ceeonncdointisounmeder sRaenstdriucttielidti eBso.lUtznmlikaenn Ma-
cthraindeitsi o(nFaClRelBeMctrsi)c ablyg ariddds,insmg athrteg croidnschepavt eofs ofpachtiostriecdat,e mduseltnispilnigcadtievveic, easntdh attrigdeinreecratitoenal in-
tderaatactfiroonms wtoh picrhedenicetr gmyupltaitptelern hsucmanabne mdeorviveemde.nTth setsyelepsa.t ternsareextremelyusefulfor
loadFfoinreaclalyst,i Dnge,eppe aBkelsiheaf vNinegtw,aonrdkds e(mDaBnNdsr)e aspreo nfosermmeadn abgye mseevnetr.al RBMs stacked on top of
Astheamountofdatageneratedbyasmartgridishugeandconstantlyincreasing,
the other [74].
DeepLearningbasedmodelsareagoodoptiontounderstandconsumptionpatternsand
makeforecasts. ResearchershavestudiedthepossibilitiesofusingDeepLearningmodels,
6. Deep Learning Models and Demand Forecasting in the Context of Smart Grids
withLSTMnetworksplayingaleadingrole(e.g.,[32,57,80]).
RTaebsleea5rcshuemrsm haraivzees pdrioffperoesnetdw foorrkescwashteinregp mraoctditeiolsn einrs thhaev etwsuoc cmesasifnu llayreuasse dwDheeerpe Deep
LLeeaarrnniinngg tteecchhnniiqquueessf ocranfo breec aasptipnlgiepdu [r8p]o: s(e1s). dTehmesaenedx pmerainenacgeesmheanvte (bee.gen., i[d7e5n,7t6ifi])e dand (2)
garfitder caonsytrsotelm (ea.tgic., r[e7v7i–e7w9]o)f. thepublishedliterature. Thesearchforreferenceshasbeen
carriDeduoeu ttoi nthdei fgferroewntinscgie dnetimficandadt afboar seense(erg.gy., fSrcoiemn cdeDiffierercetn,tS psericntogersL,i nsuk,pIpElEyE axnpdlo rdee,mand
metuc.s)t. bPea pbearlsanfrcoemd ivna rthioeu eslreecltervicaanlt gsrciiden. tIinfi cthjoisu srcneanlsasruioc,h smasaErnt egrrgidysI ncfaonr mplaatyic sa,nI EimEEportant
TransactionsonSmartGrid,EnergiesandAppliedEnergyhavealsobeenreviewed. The
role by providing a bidirectional flow of energy between consumers and utilities. Unlike
keywordsusedinclude:
traditional electrical grids, smart grids have sophisticated sensing devices that generate
- termslikeDeepLearning,ANN,neuralnetworks,andthenamesofdifferentDeep
data from which energy patterns can be derived. These patterns are extremely useful for
Learningmodels,bothfullandacronyms(e.g.,LongShort-TermMemorynetworks
load forecasting, peak shaving, and demand response management.
andLSTM),
combined(AND)with:
- terms related to the energy field, more specifically, “energy demand forecasting”,
“electricitydemandforecasting”,“loadforecasting”,“demandresponse”,“demand-
sideresponse”andvariationsoftheseexpressions.

Sensors2023,23,1467 15of30
Table5.ExamplesofapplicationofDeepLearningtechniquesintheenergydomain,focusingondemand/loadforecasting.
Reference Year Models ForecastingHorizon Dataset Outcome
Rodríguezetal. 2022 FeedforwardSpatiotemporal Minutes Solarirradiationdatabaseofthemeteorologicalstationsof Solarirradiationforecastersatisfyingtherequired
[81] NeuralNetwork+t-Student Vitoria-Gasteiz,Spain,providedbytheMeteorologicalAgencyof conditionPredictionIntervalCoveragePercentage
PDF(ProbabilityDistribution theBasqueGovernment:Euskalmet (PICP)0.05>0.95on85.22%ofthedaysin2017.
Function) (http://www.euskalmet.euskadi.eus/)(accessedon26November
2022).
Talebetal. 2022 CNN+LSTM+MLP Half-hourly DatafromEDM(ÉlectricitédeMayotte)OpenData DemandforecastingwithMeanAbsolutePercentage
[82] 1-day (https://opendata.electricitedemayotte.com/)(accessedon26 Error(MAPE)of1.71%for30-minpredictions,3.5%
1-week November2022). for1-daypredictions,and5.1%for1-weekpredictions.
Xuetal. 2022 RBM 1-day Historicalloaddataonsimilardaysfrompastyears.Datafrom DemandforecastingwithmeanofMAPEoflessthan
[83] 1-year March2010toMarch2018wereusedfortrainingandfromMarch 5%foralldaysin1-dayforecastsandMAPElessthan
2019toMarch2020forvalidation. 5%for1-yearforecasts.
YemSouheetal. 2022 SupportVectorRegression Years Smartmeterconsumptiondataovera24-yearperiod(1994to2017) DemandforecastingwithRootMeanSquareError
[84] (SVR)+FireflyAlgorithm inCameroon,obtainedfromtheElectricityDistributionAgency, (RMSE)of0.1524,MeanAbsoluteError(MAE)of
(FA)+Adaptive theElectricitySectorRegulatoryAgencyofCameroon,andthe 21.023,andMAPEof0.4124%showedthatthe
Neuro-FuzzyInference WorldBank. proposedmethodoutperformedothermodelssuchas
System(ANFIS) LSTMandRF.
Aurangzebetal. 2021 Pyramid-CNN Half-hourly Datafromindividualcustomerswhohaveahotwatersystem Demandforecastingforrandomlyselectedcustomers
[85] installed,fromtheAustralianGovernment’sSmartGridSmart fromlowandhighconsumptioncustomergroups
City(SGSC)projectdatabase,launchedin2010,whichcontains withanimprovementofMAPEupto10%compared
dataonthousandsofindividualhouseholdenergycustomers. toLSTM.
Jahangiretal. 2021 B-LSTM Hourly DatasetfortheprovinceofOntario(Canada).Hourlyelectricity Improvedforecastingresultsforwindspeed,load,
[86] price,loaddemand,andwindspeeddatafor3years(from1 andelectricityprice,especiallyatpeakpoints,based
January2016,to30December2018,with1-htimeintervals). onRMSE,MAE,andMAPE,comparedtoother
modelssuchasLSTMandCNN.
Mubasharetal. 2021 LSTM 1-month Datafrom12housesoveraperiodof3consecutivemonths. ComparisonofLSTMresidentialloaddemand
[87] forecastingwithARIMAandExponentialSmoothing,
forindividualandaggregateresidentialloaddemand,
usingMAE.
Rosatoetal. 2021 CNN+LSTM 1-day DatafromtheNWTCphotovoltaicpowerproductionplant, Experimentalresultsforoutputpowerforecasting,
[88] 3-days geographicallyidentifiedbycoordinates:3954038.200N, basedonRMSE,showedthattheproposed2D-CNN
7-days 10514004.900W,elevation1855m,locatedinDenver,Colorado, modeloutperformedamultivariateimplementation
UnitedStates.Irradiancedata,alongwithothermeteorological ofLSTM.
factors,wereretrievedthroughtheMeasurementand
InstrumentationDataCentre(MIDC)database.Alltimeseries
werecollectedinthesameplant,sampledhourly(i.e.,24samplesa
day)andreferredtotheyears2017and2018.

Sensors2023,23,1467 16of30
Table5.Cont.
Reference Year Models ForecastingHorizon Dataset Outcome
Zhangetal. 2021 DQN 3-h Smartthermostats’datacollectedduring1monthfroma Automatedbuildingdemandresponsecontrol
[89] realbuilding. frameworkthatenablescost-effectivelarge-scale
deployments.Costanalysisofacommercialbuilding
showedthattheannualcostofoptimalpolicytraining
wasonly2.25%ofthedemandresponseincentive
received.
Aurangzeb& 2020 Pyramid-CNN Short-term(severaltime AustralianGovernmentSGSCprojectdatabase,initiatedin2010, Accurateshort-termdemandforecastingofindividual
Alhussein horizons) containingdatafromthousandsofindividualhousehold householdcustomerswithirregularenergy
[90] energycustomers. consumptionpatterns.Theresultsindicatedthat
demandforecastingofindividualhouseholdsis
highlyunpredictable:morethan57%ofthecustomers
hadmorethan20outliersinthedailyenergy
consumption,yetthemodelfairlyreasonablytracked
theunpredictableenergyconsumption.
Bedietal.[75] 2020 ElmanRNN 1-day ClemsonUniversity’s Developmentofasmartbuildingcasestudypowered
Real-TimePowerandIntelligentSystems(RTPIS)Laboratory, bytheInternetofThings.
SouthCarolina,UnitedStates.
Escobaretal. 2020 LSTM,CNN,GRU,and 3-days 4yearsofhourlydatafromMadrid,includingenergy Comparativeanalysisofenergydemand,andsolar
[91] hybridmodels:CNN-LSTM consumption,energygeneration,pricingdata,andmeteorological andonshorewindgenerationforecasting,forLSTM,
andCNN-GRU information:temperature(K),humidity(waterpercentageinthe CNN,GRU,andhybridmodelsmergingCNNwith
air),winddirectioninsexagesimaldegrees,windspeedinmiles LSTMandGRU,basedonMAE,MAPEandRMSE.
persecond(m/s),onshorewindandsolarenergy,andtotalload, ThecombinationofthebestCNNandGRUmodels
theselastinMW. obtainedbetterpredictionresults.
Hafeezetal.[32] 2020 FCRBM Hourly PJMelectricitymarket.FE,Dayton,andEKPCpowergrids, Modelcomparedtootherforecastingmethodssuchas
UnitedStates. LSTM.
Hafeezetal. 2020 FCRBM 1-month PJMelectricitymarket,years2014–2017,FEpowergrid, Hybridelectricityconsumptionforecastingmodelto
[92] UnitedStates. provideefficientandaccurateforecastingwithan
affordableconvergencerate.
Hongetal. 2020 IterativeResblocksBased 1-week REDD(ReferenceEnergyDisaggregationDataset),apublicly IRBDNNmodelcomparedtoexistingmethodssuch
[21] DeepNeuralNetwork availabledatasetthatrecordshouseholdapplianceconsumption asDNN,ARMAandELM,basedonMAPE,RMSE
(IRBDNN) dataforresidentialusersfromMarch2011toJuly2011. andMAE,forresidentialbuildings.
Nguyenetal. 2020 LSTM 1-day Electricityloadconsumptionfrom2012to2017includingabout DemandforecastingresultsevaluatedusingRMSE.
[93] 2200valuesinkWh,fromTienGiang,Vietnam.

Sensors2023,23,1467 17of30
Table5.Cont.
Reference Year Models ForecastingHorizon Dataset Outcome
Rosatoetal. 2020 CNN+LSTM 3-days PhotovoltaicpowerproductionplantatOakRidgeNational Experimentalresultsofloadforecasting,basedon
[94] LaboratorylocatedinOakRidge,Tennessee,UnitedStates,with RMSE,showedthatthecombinationofCNNand
geographiccoordinates:3592099:600N,8430095:200W,elevation LSTMoutperformedtheisolateduseofLSTM.
245m.IrradiancedatawereretrievedthroughtheMIDCdatabase
Qietal. 2020 CNN+LSTM 1-day Datafromtheintegratedenergysystemofanindustrialareain ExperimentalresultsshowedthattheCNN-LSTM
[95] China,whichisacombinedelectric,cooling,andheatingsystem. compositeforecastingmodelforshort-termdemand
ofindividualhouseholdcustomershasahigher
predictionaccuracythantheCNNandLSTMmodels.
Wangetal. 2020 DeepReinforcement Hourly DatafromIEEE33-nodeextensionsystem(selectedasatypical DDQNimprovesthenoiseandinstabilityin
[96] Learning(DRL)+DDQN modelofmediumvoltagedistributionsystemmodel). traditionalDQN,andreducesoperationcostsand
peakloaddemandwhileregulatingvoltagetothesafe
limit.
Wenetal. 2020 DeepRecurrentNeural Hourly Dataport,PecanStreetInc.Residentialbuildings,Austin,Texas, Deeplearningmodeltoforecastandfillinmissing
[80] Network(DRNN)+GRU+ UnitedStates. dataonresidentialbuildingsenergydemand.
LSTM
Wenetal. 2020 ModifiedRNN Hourly Dataport,PecanStreetInc.Residentialbuildings,Europe. Experimentalresultsonresidentialbuildingsdemand
[97] showedthatpeakdemandcanbereducedby17%.
Yangetal. 2020 MultitaskBayesianNeural Hourly TwopublicdatasetsonsmartmetersprovidedbytheIrish Experimentalresults,basedonMAEandRMSE,
[98] Network(MT-BNN) CommissionforEnergyRegulation(CER)andtheAustralian showedthattheproposedloadforecastingframework
Government’sSGSCproject,respectively.TheCERdatasetwas forresidentialdemandresponseprovidedhigher
collectedbetweenJuly2009andDecember2010withthe accuracyofindividualelectricityconsumptionthan
participationofmorethan4225residentialcustomersand2210 othermethodssuchasSVR,GradientBoosted
SmallandMediumEnterprises(SMEs)participating.TheSGSC RegressionTrees(GBRT),RF,andPooling-basedLong
datasetwascollectedforabout10,000customersbetween2010and Short-TermMemory(PLSTM).
2014inNewSouthWales.Electricityconsumption(kWh)was
recordedeveryhalfhourateachmeterinbothdatasets.
Aminetal. 2019 LSTM Severaltimehorizons Smartmeterdatacollectedover2yearsfrom114apartments, Comparisonofthreedemandforecastingmethods:a
[99] alongwithweatherinformationforthesameperiod. piecewiseLRmodel,theunivariateseasonalARIMA
model,andamultivariateLSTMmodel.Theresults
showedthatwhiletheLRmodelcouldbeusedfor
long-termplanning,theLSTMmodelsignificantly
improvedtheaccuracyofshort-term(1-day)demand
forecastingcomparedtotheARIMAandLRmodels.

Sensors2023,23,1467 18of30
Table5.Cont.
| Reference | Year | Models | ForecastingHorizon |     | Dataset | Outcome |
| --------- | ---- | ------ | ------------------ | --- | ------- | ------- |
Atef&Eltawil 2019 LSTM Hourly RealtimeelectricitypricesfromDenmarkfrom17January2013to ComparativestudyofLSTMandSVRforelectricity
[100] 30September2018. priceforecastinginsmartgrids.Resultsshowedthat
bothmodelsareeffective.However,LSTM
outperformedSVR,withameanRMSEvalueof1.1165
and0.416respectively.
Chanetal.[101] 2019 CNN Short-term Multivariateseriescomposedof9variablesand2,075,259 Experimentalresults,basedonMAEandRMSE,
|     |     |     |     | observationsprovidedbytheDataScienceandInteraction    | showedthattheproposedCNN-basedmethod        |                            |
| --- | --- | --- | --- | ----------------------------------------------------- | ------------------------------------------- | -------------------------- |
|     |     |     |     | ScientificTeam,RegiondeParis,France.Datacollectedfrom | achieveshigherperformancethantheSVMmodelin  |                            |
|     |     |     |     | December2006toNovember2010withasamplingfrequencyof1   | demandforecastingwith0.514%MAEversus14.32%, |                            |
|     |     |     |     |                                                       | min.                                        | and0.698%RMSEversus19.23%. |
Hafeezetal. 2019 ModifiedMutual 1-day PJMelectricitymarket Experimentalresultsshowedthattheproposedfast
[102] Information(MMI)technique andaccuratemodeloutperformedexistingmodels
+FCRBM+GeneticWind suchasMultipleInstanceArtificialNeuralNetwork
DrivenOptimization (MI-ANN)andAccurateFastConvergingShort-Term
|     | (GWDO)algorithm |     |     |     | Loadforecast(AFC-STLF),intermsofdemand |     |
| --- | --------------- | --- | --- | --- | -------------------------------------- | --- |
forecastingaccuracyandconvergencerate.The
forecastingaccuracywasimprovedusingtheMMI
techniqueandtheFCRBMmodel,andthe
convergenceratewasenhancedwiththeGWDO
algorithm.
Kauretal. 2019 RNN+LSTM Hourly SmartmeterdataofenergyconsumptioninkWhfrom112 Experimentalresults,basedonMAPEandRMSE,
[103] householdsfor500dayswithasamplingfrequencyofhalfanhour. showedthattheproposedmethodgivesbetterresults
forsmarthomesdemandforecastingthanRNNand
ARIMA.
Khafafetal. 2019 LSTM Hourly Historicalenergyconsumption.For3-dayforecasts,thedata Experimentalresults,basedonMAPEandRMSE,
[104] 3-days correspondstodailyconsumptionforeachmonth.For15-day showedagoodperformanceoftheproposedLSTM
|     |     |     | 15-days | forecasts,thedatacorrespondstodailyconsumptionforthe |     | modelfordemandforecasting. |
| --- | --- | --- | ------- | ---------------------------------------------------- | --- | -------------------------- |
wholeyear.
Khanetal. 2019 CombineFeatureSelection Halfhourly MarketdatafromtheISONewEnglandControlArea(ISO Experimentalresults,basedonMAEandMSE,
[105] ConvolutionalNeural 1-day NE-CA)from showedbetterefficiencyandaccuracyoftheproposed
Network(CFSCNN) 1-week January2017toDecember2017withhalf-hourly modelfordemandforecastingcomparedtoDB-SVM
1-month samplingfrequency. (DensityBasedSupportVectorMachine).

Sensors2023,23,1467 19of30
Table5.Cont.
Reference Year Models ForecastingHorizon Dataset Outcome
Kim&Cho 2019 CNN+LSTM Minutely IndividualhouseholdelectricityconsumptionintheUCIMachine Experimentalresultsforsmarthomedemand
[106] Hourly LearningrepositoryoftheUniversityofCalifornia,Irvine,which forecasting,basedonMSE,RMSE,MAE,andMAPE
Daily providesadatasetofelectricityconsumptionwith2,075,259 showedthattheproposedmodeloutperformedother
Weekly time-seriesand12variables techniquessuchasLSTM,GRU,B-LSTM,
(https://archive.ics.uci.edu/mL/datasets/)(accessedon26 Attention-basedLSTM,LR,FCRBM,andCRBM.
November2022).Thedatasetcollectedelectricityconsumption
over4years(from16December2006to26November2010)ina
householdinFrance.
Kim&Cho 2019 ParticleSwarmOptimization Minutely IndividualhouseholdelectricityconsumptionintheUCIMachine Experimentalresultsforsmarthomedemand
[107] (PSO)based Hourly LearningrepositoryoftheUniversityofCalifornia,Irvine,which forecasting,basedonMAEandMAPE,showeda
CNN+LSTM Daily providesadatasetofelectricityconsumptionwith2,075,259time betterperformanceoftheproposedmodel,which
Weekly seriesand12variables(https://archive.ics.uci.edu/mL/datasets/) outperformedothertechniquessuchasLR,RF,
(accessedon26November2022).Thedatasetcollectedelectricity Regression,MLP,andCNN+LSTM(withoutPSO).
consumptionover4years(from16December2006to26
November2010)inahouseholdinFrance.
Lu&Hong 2019 ReinforcementLearning(RL) Hourly PJMelectricitymarket.Datafrom1January2017to21February Experimentalresultsfordemandforecastingand
[108] +DeepNeuralNetwork 2018wereusedtotrainthemodel. electricityprices,basedonMAEandMAPE,showed
(DNN) goodperformanceoftheproposedmodelforservice
providersinpurchasingenergyfromitsvarious
customerstoimprovegridreliabilityandbalance
energyfluctuations.
Pramonoetal. 2019 CNN+LSTM Hourly Twodifferentdatasets:ENTSO-E(EuropeanNetworkof Experimentalresultsfordemandforecasting,basedon
[109] TransmissionSystemOperatorsforElectricity)dataset,and MAE,MAPE,andRMSE,showedbetterperformance
ISO-NE(IndependentSystemOperatorNewEngland)dataset. oftheproposedmodelcomparedtoothertechniques.
Rahmanetal. 2019 RNN+LSTM Daily Datasetcontaininghouseholdelectricityconsumptiondataata ComparisonofARIMAandRNNwithLSTM,
[110] Monthly samplingfrequencyof1minfrom2006to2010.Theelectricity UnivariateLR,andMultivariateLR.Experimental
Yearly consumptionvalueswere resultsfordemandforecastinginsmarthomes
collectedfordifferentelectricalappliancesinthehousehold. showedthatallmodelscouldcapturethegeneral
trendofthedata,butexhibiteddifferentpredictive
capabilities.Bestforecastingresultswereobtained
withajointmethodbasedonMahalanobisdistance.

Sensors2023,23,1467 20of30
Table5.Cont.
Reference Year Models ForecastingHorizon Dataset Outcome
Syedetal. 2019 RecurrentNeuralNetwork 1-day Datasetcontainingenergyconsumptionrecordsfor5567 Experimentalresultsfordemandforecastingversus
[111] (RNN)+LSTM householdsfromtheUKPowerNetwork’sLowCarbonLondon temperature,humidity,dewpoint,windspeedand
projectfromNovember2011toFebruary2014. UVIndex,basedonRMSE,showedbetter
performanceoftheproposedAveragingRegression
EnsemblesmodelbasedontheLRandLSTMRNN
ensemblecomparedtoothertechniquessuchasLR
ModelandElaborationLikelihoodModel(ELM).
Ustundagetal. 2019 LSTM Hourly PJMDataMiner2,1–11March2019(hourlyload)NewJersey, Theworkshowedthatdataprivacyassurancecanbe
[112] UnitedStates. obtainedtovaryingdegreeswithtolerable
degradationinloadforecastingresults.
Vesaetal. 2019 MLP+LSTM 1-day UKDomesticAppliance-LevelElectricity(UKDALE)open-access Experimentalresultsforindividualandaggregated
[113] intraday(4h) datasetcontaininghistoricalelectricityconsumptionreadingsfrom loadforecastinginresidentialbuildings,obtaining
5housesover655daystakenatasamplingrateof6s. MAE—5.60kWh,MAPE—1.59%,andRMSE—6.19
kWh,showedhighaccuracyoftheproposed
combinedmodelforresidentialbuildingenergy
demandforecasting.Thecombinedmodel
outperformedMLPandLSTMmodels.
Yangetal. 2019 GRU Hourly Real-worldsmartmeterdatasetprovidedbytheIrishCER.The Experimentalresultsforloadforecasting,basedon
[114] studyuseddatafrom800residentsand400SMEswithasampling twotypicalprobabilisticscoringmethods(pinballloss
frequencyofhalfanhourfrom1August2010to31October2010. score,andwinklerscore),showedbetterperformance
oftheproposedmodelcomparedtoothertechniques
suchasQuantileRegressionForest(QRF),Quantile
RegressionGradientBoosting(QRGB),andQuantile
LongShort-TermMemory(QLSTM)NeuralNetwork.
Zahidetal. 2019 CNN Hourly ISO-NEdatasetwith2018loaddata. Improvedclassifierswereusedtoforecastloadand
[115] electricityprices.
Ouyangetal. 2019 DBN Hourly OneyeargridloaddatacollectedinanurbanizedareainTexas, Predictionaccuracyoftheproposedmodelwas
[116] UnitedStates. evaluatedwithMAPE,RMSE,andHitRate(HR).
Experimentalresultsforloadforecasting,examinedin
fourseasonsindependently,showedahigher
predictionaccuracyoftheproposed
Gumbel-HouggardCopula-DBNmodel,comparedto
othertechniquessuchasSVRandDBN.

Sensors2023,23,1467 21of30
Table5.Cont.
Reference Year Models ForecastingHorizon Dataset Outcome
Hafeezetal. 2018 FCRBM+CRBM 1-weekwithhourly PubliclyavailableKagglerepositoryfromthe2012globalenergy Experimentalresultsforloadforecasting,basedon
[117] resolution,inthemiddle forecastingcompetition.Thedatasetconsistedofhourlyload(kW) MAPE,NRMSEandcorrelationcoefficient,showed
ofeachseason from20UnitedStatesutilityzonesandtemperaturefrom11 thattheproposedmodelswereaccurateandrobust
stationsfrom1January2004to30June2008. comparedtoANNandCNN.Theadoptedstacked
FCRBMachieved99.62%accuracywithaffordable
runtimeandcomplexity.
Koprinskaetal. 2018 CNN+LSTM 1-day ElectricityloaddatasetsfromAustralia,Portugal,andSpainfor ComparisonoftheperformanceofCNNwithMLP
[118] twoyears,2010and2011(from1January2010to31December andLSTMRNNforphotovoltaicsolarpowerand
2011),withhourlysampleddata.TheAustraliandatawasfrom loadforecasting.Experimentalresultsshowedthat
NewSouthWales,providedbytheAustralianEnergyMarket CNNandMLPhadsimilaraccuracyandtraining
Operator.ThePortugueseandSpanishdatawereprovidedbythe time,andoutperformedtheothermodels.
SpanishEnergyMarketOperator.
Kuo&Huang 2018 CNN+LSTM Next3days UnitedStatesDistrictpublicconsumptionandelectricloaddataset Theloadforecastingperformanceoftheproposed
[119] from2016providedbytheElectricReliabilityCouncilofTexas. CNN-basedmethodiscomparedwithother
techniquessuchasSVM,RF,DT,MLPandLSTM.
Experimentalresults,basedonMAPEand
CumulativeVariationofRootMeanSquareError
(CV-RMSE),showedveryhighforecastingaccuracy
fortheproposedmodel.
Shietal. 2018 Pooling-basedDRNN Hourly DatafromtheSmartMeteringElectricityCustomerBehaviour Experimentalresultsforsmarthomeloadforecasting,
[120] Trials(CBTs)initiatedbytheIrishCER,from1July2009to31 basedonRMSE,showedthattheproposedmodel
December2010,involvingover5000IrishresidentialandSME outperformedothertechniquessuchasARIMAby
consumers.Samplesofhalf-hourlyelectricityconsumption(kWh) 19.5%,SVRby13.1%,andclassicaldeepRNNby6.5%.
wereavailableforeachparticipant,aswellascustomertype
andtariff.
Ghaderietal. 2017 RNN Hourly HourlywindspeeddatafromMeteorologicalTerminalAviation Experimentalresultsforwindspeedforecasting,
[121] Routine(METAR)weatherreportsfrom57stationsontheEast basedonMAE,RMSEandNRMSE,showedthatthe
CoastoftheUnitedStatesincludingstationsinNewYork, proposedmodeloutperformedothertechniquessuch
Massachusetts,NewHampshire,andConnecticut.Atimeperiod asPersistenceForecasting,ARoforder1,ARoforder
from6January2014to20February2014,withthemostunstable 3andWaveletTransform-ArtificialNeuralNetwork
windconditionsoftheentireyear,wasconsideredastestset. (WT-ANN).

Sensors2023,23,1467 22of30
Table5.Cont.
Reference Year Models ForecastingHorizon Dataset Outcome
Jarábeketal. 2017 LSTM DatasetonelectricityconsumptionofSlovakcompanies,collected ResearchontheneedforclusteringwhenusingLSTM
[122] intheframeworkoftheprojectInternationalCentreofExcellence withSequencetoSequence(S2S)architectureforgrid
forResearchofIntelligentandSecureInformation-Communication levelloadforecastingonrealworlddata.Amethod
TechnologiesandSystems,from1July2013to16February2015 withoutclustering(simpleaggregationofthe
withasamplingfrequencyof15min.Consumptiondatafrom consumers)wascomparedwithamethodusing
11,281enterpriseswereaggregatedinto1152timeseries k-shapeclustering.Experimentalresultsfor
consideringtheenterprise’spostcode. aggregatedloadforecastingshowedthatmore
accuratepredictionswereobtainedusing
k-shapeclustering.
Lietal. 2017 CNN Minutes Electricityload,fromJanuary2014toJune2016inalargecity Proposedmethodconsideringallexternalfactorsthat
[123] inChina. influenceloadforecastingsuchashumidity,
temperature,windspeed,etc.

Sensors2023,23,1467 23of30
The search was limited to the last 6 years. The decision as to which articles were
finallyincludedinTable5wasmadebytheauthorsafterreviewingthesearchresultsand
ensuringthattheworkinvolvedtheuseofaDeepLearningmodelfordemandorload
forecastingpurposes.
7. Conclusions
Increasingenergydemandputspressureonthepowergridtobalancesupplyand
demand. Smartgridscanplayanimportantrole. Inthesesystems,datarelatedtoenergy
useareregularlycollectedandanalyzedtoobtainenergyconsumption. Theusagepatterns
obtained can be useful for demand and load forecasting. This is a challenging task in
thecontextofsmartenvironments,whichiswhyresearchersareputtingspecialefforts
intothis.
To meet today’s demand forecasting challenges, where smart grids generate large
amountsofdata, itisnecessarytousemoderndata-driventechniques. DeepLearning
basedmodelsareagoodalternative. Traditionally, researchhasfocusedonforecasting
customers’ energy consumption using the small historical data sets available on their
behavior. However,currentresearchapplyingDeepLearningmethodshasdemonstrated
better performance than conventional forecasting methods. The use of Deep Learning
models involves using large amounts of data, such as those provided by the different
datasets used by practitioners in the works collected in Table 5. It is a fact that smart
gridsgeneratelargeamountsofdata,soBigDataisalsoakeytechnologytoovercomethe
challengesofrenewableenergyintegration,loadfluctuationandsustainabledevelopment.
Withtheintroductionofrenewablesintothesmartgrid,anincreasingnumberofvariables
are brought into the system and more data need to be processed. This situation is also
aggravatedwiththegradualintroductionofelectricvehicles,sotheseBigDatatechnologies
arealsobecomingincreasinglynecessary[124].
ThestudyconductedhasrevealedthatthemostwidelyusedDeepLearningmodels
in the energy domain for demand forecasting purposes are CNNs, RNNs, LSTM, DQNs,
andCRBMandavariationofanyofthem,acombinationoftwoormoreofthem,orthe
combination of any of them with other techniques. Notable are CNN and its variations
suchasPyramid-CNN[82,85,88,90,91,94,95,101,106,107,109,115,118,119,123], LSTMandits
variationssuchasB-LSTM[80,82,86–88,91,93–95,99,100,103,104,106,107,109–113,118,119,122],
and a combination of both [82,88,91,94,95,106,107,109,118,119]. Real testbeds with high-
quality data are not common, but are necessary to determine the performance of Deep
Leaningmodels. ItisimportanttocontinuetestingfutureDeepLearningmodels,including
potentialvariationsand/orcombinationsoftwoormoremodels,forforecastingpurposes
inthecontextofsmartgrids. Itisalsoimportantthatthesetestsarecarriedoutfordifferent
scenarios. DeepLearningmodelscapableofautomaticallyforecastingloadfordifferent
typesofcustomers,premises/buildings,anddifferentweatherconditionsarestillneeded.
It is important to test the performance of Deep Learning, but also to determine which
modelisbestforeachscenario.
Intermsofdatasets,practitionersuseddifferentoptions,highlightingPJMelectric-
ity market [32,92,102,108,112], SGSC [85,90,98], CER [98,114,120], ISO-NE [105,109,115],
Pecan Street Inc. [80,97], UCI [106,107], UKDALE [113] and REDD [21]. Many reviews
on demand/load forecasting in the context of smart grids focus on the Deep Learning
modelsusedbutforgetaboutthedata. However,foraDeepLearningimplementationto
besuccessful,thealgorithmsareasvaluableasthedata. Infact,itwouldbedesirablefor
researcherstoincorporatemoreinformationaboutthedatausedintheirworks,addressing
forexamplethetraining/validation/testingdatasplit,thesamplingintervalofthedata,
themethodfordatacleaning,etc. OneofthelimitationsofusingDeepLearningmodels
isthelackofhigh-qualityreal-worlddatasets. Afuturetrendwouldprobablybetoshift
theemphasisfromthemodeltothedata. Furthermore,theauthorsforeseeanintegration
ofIoTintoDeepLearningmodelsusedfordemand/loadforecasting. IoTisenablingthe
democratization of sensing. This opens exciting opportunities in terms of high-quality

Sensors2023,23,1467 24of30
datacollection,whichiscriticalinthecontextofdemand/loadforecasting. Relatedtothis,
another future trend would be the development of integrated systems that include the
necessarydataacquisitionandpre-processing.
Finally, it is also remarkable that in most cases researchers focused on short-term
forecasting.
Load forecasting is a challenging task in the context of smart environments. Con-
sequently,researchersareputtingspecialeffortsintoit. Realtestbedswithhigh-quality
dataarenotcommonbutnecessarytodeterminetheperformanceoftheDeepLeaning
models. DeepLearningmodelscapableofautomaticallyforecastingloadfordifferenttypes
ofcustomers,premises/buildings,anddifferentweatherconditionsarestillneeded.
AuthorContributions:Conceptualization,methodology,writing—originaldraftpreparation,writing—
reviewandediting,andsupervision,J.M.A.-P.andM.Á.P.-J.Allauthorshavereadandagreedtothe
publishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
InstitutionalReviewBoardStatement:Notapplicable.
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement:Notapplicable.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.
Abbreviations
Thefollowingabbreviationsareusedinthismanuscript:
AdaBoost AdaptiveBoosting
AFC-STLF AccurateFastConvergingShort-TermLoadforecast
ANFIS AdaptiveNeuro-FuzzyInferenceSystem
ANN ArtificialNeuralNetwork
ANOVA AnalysisofVariance
AR Auto-Regressive
ARCH Auto-RegressiveConditionalHeteroscedasticity
ARIMA Auto-RegressiveIntegratedMovingAverage
ARMA Auto-RegressiveandMovingAverage
B-LSTM BidirectionalLongShort-TermMemory
BM BoltzmannMachines
CBT CustomerBehaviorTrial
CER CommissionforEnergyRegulation
CFSCNN CombineFeatureSelectionConvolutionalNeuralNetwork
CNN ConvolutionalNeuralNetwork
CRBM ConditionalRestrictedBoltzmannMachine
CV-RMSE CumulativeVariationofRootMeanSquareError
DB-SVM DensityBasedSupportVectorMachine
DBN DeepBeliefNetwork
DDQN DuelingDeep-QNetwork
DNN DeepNeuralNetwork
DQN DeepQ-Network
DRL DeepReinforcementLearning
DRNN DeepRecurrentNeuralNetwork
DT DecisionTree
ECLAT EquivalenceClassTransformation
EDM ÉlectricitédeMayotte
ELM ElaborationLikelihoodModel
ElmanRNN ElmanRecurrentNeuralNetwork
ENTSO-E EuropeanNetworkofTransmissionSystemOperatorsforElectricity
FA FireflyAlgorithm

Sensors2023,23,1467 25of30
FCRBM FactoredConditionedRestrictedBoltzmannMachine
F-P FrequentPattern
GAN GenerativeAdversarialNetwork
GBRT GradientBoostedRegressionTrees
GDP GrossDomesticProduct
GRU GatedRecurrentUnits
GWDO GeneticWindDrivenOptimization
HR HitRate
IoT InternetofThings
IRBDNN IterativeResblocksBasedDeepNeuralNetwork
ISO-NE IndependentSystemOperatorNewEngland
ISONECA ISONewEnglandControlArea
KNN K-nearestNeighbors
LDA LinearDiscriminantAnalysis
LR LinearRegression
LSTM LongShort-TermMemory
LSTM-RNN LongShort-TermMemoryRecurrentNeuralNetwork
MAE MeanAbsoluteError
MAM MovingAverageModel
MAPE MeanAbsolutePercentageError
METAR MeteorologicalTerminalAviationRoutine
MI-ANN MultipleInstanceArtificialNeuralNetwork
MIDC MeasurementandInstrumentationDataCentre
MLP MultilayerPerceptron
MMI ModifiedMutualInformation
MT-BNN MultitaskBayesianNeuralNetwork
NB NaiveBayes
NLR Non-LinearRegression
NRMSE NormalizedRootMeanSquaredError
OLS OrdinaryLeastSquaresRegression
PCA PrincipalComponentsAnalysis
PDF ProbabilityDistributionFunction
PICP PredictionIntervalCoveragePercentage
PLS PartialLeast-Square
PLSTM Pooling-basedLongShort-TermMemory
PSO ParticleSwarmOptimization
Pyramid-CNN PyramidConvolutionalNeuralNetwork
QLSTM QuantileLongShort-TermMemory
QRF QuantileRegressionForest
QRGB QuantileRegressionGradientBoosting
RBM RestrictedBoltzmannMachine
REDD ReferenceEnergyDisaggregationDataSet
RF RandomForest
RFE RecursiveFeatureElimination
RL ReinforcementLearning
RMSE RootMeanSquaredError
RNN RecurrentNeuralNetwork
RTPIS Real-TimePowerandIntelligentSystems
S2S SequencetoSequence
SD SpectralDecomposition
SGD StochasticGradientDescent
SGSC SmartGridSmartCity
SME SmallandMediumEnterprise
SS State-Space
SVM SupportVectorMachine
SVR SupportVectorRegression
UKDALE UKDomesticAppliance-LevelElectricity
WT-ANN WaveletTransform-ArtificialNeuralNetwork
XGBoost ExtremeGradientBoosting

Sensors2023,23,1467 26of30
References
1. Butt,O.M.;Zulqarnain,M.;Butt,T.M.Recentadvancementinsmartgridtechnology:Futureprospectsintheelectricalpower
network.AinShamsEng.J.2021,12,687–695.[CrossRef]
2. Cecati,C.;Mokryani,G.;Piccolo,A.;Siano,P.AnOverviewontheSmartGridConcept.InProceedingsoftheIECON2010—36th
AnnualConferenceonIEEEIndustrialElectronicsSociety,Glendale,CA,USA,7–10November2010;pp.3322–3327.
3. Vakulenko,I.;Saher,L.;Lyulyov,O.;Pimonenko,T.ASystematicLiteratureReviewofSmartGrids.InProceedingsofthe1st
ConferenceonTraditionalandRenewableEnergySources: PerspectivesandParadigmsforthe21stCentury(TRESP2021),
Prague,CzechRepublic,22–23January2021;Volume250.[CrossRef]
4. Yan,Y.;Qian,Y.;Sharif,H.;Tipper,D.Asurveyoncybersecurityforsmartgridcommunications. IEEECommun. Surv. Tutor.
2012,14,998–1010.[CrossRef]
5. ShawkatAli,A.B.M.;Azad,S.A.Demandforecastinginsmartgrid.GreenEnergyTechnol.2013,132,135–150.[CrossRef]
6. Prabadevi,B.;Pham,Q.-V.;Liyanage,M.;Deepa,N.;Vvss,M.;Reddy,S.;Madikunta,P.K.R.;Khare,N.;Gadekallu,T.R.;Hwang,
W.H.Deeplearningforintelligentdemandresponseandsmartgrids:Acomprehensivesurvey.arXiv2021.[CrossRef]
7. Ferreira, H.C.; Lampe, L.; Newbury, J.; Swart, T.G. Power Line Communications. Theory and Applications for Narrowband and
BroadbandCommunicationsOverPowerLines;JohnWileyandSons:Chichester,UK,2010.
8. Vanting,N.B.;Ma,Z.;Jørgensen,B.N.Ascopingreviewofdeepneuralnetworksforelectricloadforecasting.EnergyInform.2021,
4,49.[CrossRef]
9. Hernández,L.;Baladrón,C.;Aguiar,J.M.;Carro,B.;Sánchez-Esguevillas,A.J.;Lloret,J.;Massana,J.Asurveyonelectricpower
demandforecasting:Futuretrendsinsmartgrids,microgridsandsmartbuildings.IEEECommun.Surv.Tutor.2014,16,1460–1495.
[CrossRef]
10. Javed,F.;Arshad,N.;Wallin,F.;Vassileva,I.;Dahlquist,E.Forecastingfordemandresponseinsmartgrids:Ananalysisonuseof
anthropologicandstructuraldataandshort-termmultipleloadsforecasting.Appl.Energy2012,96,150–160.[CrossRef]
11. Khodayar,M.E.;Wu,H.Demandforecastinginthesmartgridparadigm: Featuresandchallenges. Electr. J.2015,28,51–62.
[CrossRef]
12. Boza,P.;Evgeniou,T.Artificialintelligencetosupporttheintegrationofvariablerenewableenergysourcestothepowersystem.
Appl.Energy2021,290,116754.[CrossRef]
13. Lasseter,R.;Akhil,A.;Mamy,C.;Stephens,J.;Dagle,J.;Guttromson,R.;Meliopoulous,A.S.;Yinger,R.;Eto,J.Integrationof
DistributedEnergyResources. TheCERTSMicrogridConcept. WhitePaper. 2003. Availableonline: https://certs.lbl.gov/
publications/integration-distributed-energy(accessedon20November2022).
14. Anduaga, J.; Boyra, M.; Cobelo, I.; García, E.; Gil, A.; Jimeno, J.; Laresgoiti, I.; Oyarzabal, J.M.; Rodríguez, R.; Sánchez, E.;
etal.LaMicrorred,UnaAlternativadeFuturoParaunSuministroEnergéticoIntegral;TECNALIA,CorporaciónTecnológica:Derio,
Spain,2008.
15. Hoy,M.B.Smartbuildings:Anintroductiontothelibraryofthefuture.Med.Ref.Serv.Q.2016,35,326–331.[CrossRef][PubMed]
16. Fang,X.;Misra,S.;Xue,G.;Yang,D.Smartgrid—Thenewandimprovedpowergrid:ASurvey.IEEECommun.Surv.Tutor.2012,
14,944–980.[CrossRef]
17. Singh,A.;Nasiruddin,I.;Khatoon,S.;Muazzam,M.;Chaturvedi,D.K.LoadForecastingTechniquesandMethodologies: A
Review.InProceedingsofthe2ndInternationalConferenceonPower,ControlandEmbeddedSystems(ICPCES),Allahabad,
India,17–19December2012.[CrossRef]
18. Nti,I.K.;Teimeh,M.;Nyarko-Boateng,O.;Adekoya,A.F.Electricityloadforecasting: Asystematicreview. J.Electr. Syst. Inf.
Technol.2020,7,13.[CrossRef]
19. AhmedMir,A.;AlghassabKafait,M.;Ullah,K.;AliKhan,Z.;Lu,Y.;Imran,M.Areviewofelectricitydemandforecastinginlow
andmiddleincomecountries:Thedemanddeterminantsandhorizons.Sustainability2020,12,5931.[CrossRef]
20. Clements,A.E.;Hurn,A.S.;Li,Z.Forecastingday-aheadelectricityloadusingamultipleequationtimeseriesapproach.Eur.J.
Oper.Res.2016,251,522–530.[CrossRef]
21. Hong,Y.;Zhou,Y.;Li,Q.;Xu,W.;Zheng,X.Adeeplearningmethodforshort-termresidentialloadforecastinginsmartgrid.
IEEEAccess2020,8,55785–55797.[CrossRef]
22. Phuangpornpitak,N.;Prommee,W.Astudyofloaddemandforecastingmodelsinelectricpowersystemoperationandplanning.
GMSARNInt.J.2016,10,19–24.
23. Xiao,L.;Shao,W.;Liang,T.;Wang,C.Acombinedmodelbasedonmultipleseasonalpatternsandmodifiedfireflyalgorithmfor
electricalloadforecasting.Appl.Energy2016,167,135–153.[CrossRef]
24. Xue,B.;Geng,J.DynamicTransverseCorrectionMethodofMiddleandLong-termEnergyForecastingbasedonStatisticof
ForecastingErrors.InProceedingsofthe10thConferenceonPowerandEnergy(IPEC),HoChiMinh,Vietnam,12–14December
2012;pp.253–256.[CrossRef]
25. Khatoon, S.; Nasiruddin, I.; Singh, A.; Gupta, P. Effects of Various Factors on Electric Load Forecasting: An Overview. In
ProceedingsoftheIEEEPowerIndiaInternationalConference(PIICON),Delhi,India,5–7December2014;pp.1–5.
26. Hippert,H.S.;Pedreira,C.E.;Souza,R.C.Neuralnetworksforshort-termloadforecasting:Areviewandevaluation.IEEETrans.
PowerSyst.2001,16,44–55.[CrossRef]
27. Fahad,M.U.;Arbab,N.Factoraffectingshorttermloadforecasting.J.CleanEnergyTechnol.2014,2,305–309.[CrossRef]

Sensors2023,23,1467 27of30
28. Novianto,D.;Gao,W.;Kuroki,S.Reviewonpeople’slifestyleandenergyconsumptionofAsiancommunities:Casestudyof
Indonesia,Thailand,andChina.EnergyPowerEng.2015,7,465.[CrossRef]
29. Hernández,L.;Baladrón,C.;Aguiar,J.M.; Calavia,L.;Carro,B.;Sánchez-Esguevillas,A.;García,P.; Lloret,J.Experimental
analysisoftheinputvariables’relevancetoforecastnextday’saggregatedelectricdemandusingneuralnetworks.Energies2013,
6,2927–2948.[CrossRef]
30. Issi, F.; Kaplan, O.Thedeterminationofloadprofilesandpowerconsumptionsofhomeappliances. Energies2018, 11, 607.
[CrossRef]
31. Shi,Y.;Yu,T.;Liu,Q.;Zhu,H.;Li,F.;Wu,Y.Anapproachofelectricalloadprofileanalysisbasedontimeseriesdatamining.IEEE
Access2020,8,209915–209925.[CrossRef]
32. Hafeez,G.;Alimgeer,K.S.;Khan,I.Electricloadforecastingbasedondeeplearningandoptimizedbyheuristicalgorithmin
smartgrid.Appl.Energy2020,269,114915.[CrossRef]
33. Gillies,D.K.A.;Bernholtz,B.;Sandiford,P.J.Anewapproachtoforecastingdailypeakloads.Trans.Am.Inst.Electr.Eng.PartIII
PowerAppar.Syst.1956,75,382–387.[CrossRef]
34. Park,D.C.;El-Sharkawi,M.A.;MarksII,R.J.;Atlas,L.E.;Damborg,M.J.Electricloadforecastingusinganartificialneuralnetwork.
IEEETrans.PowerSyst.1991,6,442–449.[CrossRef]
35. Bakirtzis,A.G.;Petridis,V.;Kiartzis,S.J.;Alexiadis,M.C.;Maissis,A.H.Aneuralnetworkshorttermloadforecastingmodelfor
theGreekpowersystem.IEEETrans.PowerSyst.1995,11,858–863.[CrossRef]
36. Lu,C.-N.;Wu,H.-T.;Vemuri,S.Neuralnetworkbasedshorttermloadforecasting. IEEETrans. PowerSyst. 1993,8,336–342.
[CrossRef]
37. Papalexopoulos,A.D.;Hao,S.;Peng,T.-M.AnimplementationofaneuralnetworkbasedloadforecastingmodelsfortheEMS.
IEEETrans.PowerSyst.1994,9,1956–1962.[CrossRef]
38. Wang,P.Ondefiningartificialintelligence.J.Artif.Gen.Intell.2019,10,1–37.[CrossRef]
39. Ongsulee,P.ArtificialIntelligence,MachineLearningandDeepLearning.InProceedingsofthe15thInternationalConferenceon
ICTandKnowledgeEngineering(ICT&KE),Bangkok,Thailand,22–24November2017;pp.1–6.[CrossRef]
40. Raz, A.R.; Llinas, J.; Mittu, R.; Lawless, W.F.Engineeringforemergenceininformationfusionsystems: Areviewofsome
challenges.InHuman-MachineSharedContexts;Lawless,W.F.,Mittu,R.,Sofge,D.A.,Eds.;AcademicPress:Cambridge,MA,USA,
2020;pp.241–255,ISBN9780128205433.[CrossRef]
41. Cohen,S.Thebasicsofmachinelearning: Strategiesandtechniques. InArtificialIntelligenceandDeepLearninginPathology;
Cohen,S.,Ed.;Elsevier:Amsterdam,TheNetherlands,2021;pp.13–40,ISBN9780323675383.[CrossRef]
42. Bonetto,R.;Latzko,V.Machinelearning.InComputinginCommunicationNetworks,FromTheorytoPractice;Fitzek,F.H.P.,Granelli,
F.,Seeling,P.,Eds.;AcademicPress:Cambridge,MA,USA,2020;pp.135–167,ISBN9780128204887.[CrossRef]
43. Delua,J.Supervisedvs.UnsupervisedLearning:What’stheDifference?2021.Availableonline:https://www.ibm.com/cloud/
blog/supervised-vs-unsupervised-learning(accessedon15November2022).
44. Sarker, I.H. Machine learning: Algorithms, real-world applications and research directions. SN Comput. Sci. 2021, 2, 160.
[CrossRef][PubMed]
45. Choi,R.Y.;Coyner,A.S.;Kalpathy-Cramer,J.;Chiang,M.F.;Campbell,J.P.Introductiontomachinelearning,neuralnetworks,
anddeeplearning.Transl.Vis.Sci.Technol.2020,9,14.[CrossRef]
46. Alloghani,M.; Al-Jumeily,D.; Mustafina,J.; Hussain,A.; Aljaaf,A.J.Asystematicreviewonsupervisedandunsupervised
machinelearningalgorithmsfordatascience.InSupervisedandUnsupervisedLearningforDataScience;Berry,M.,Mohamed,A.,
Yap,B.,Eds.;Springer:Cham,Switzerland,2020;pp.3–21.[CrossRef]
47. Satinet,C.;Fouss,F.Asupervisedmachinelearningclassificationframeworkforclothingproducts’sustainability.Sustainability
2022,14,1334.[CrossRef]
48. Jiang,T.;Gradus,J.L.;Rosellini,A.J.Supervisedmachinelearning: Abriefprimer. Behav. Ther. 2020,51,675–687. [CrossRef]
[PubMed]
49. ElBouchefry,K.; deSouza,R.S.Learninginbigdata: Introductiontomachinelearning. InKnowledgeDiscoveryinBigData
fromAstronomyandEarthObservation; Škoda,P.,Adam,F.,Eds.; Elsevier: Amsterdam,TheNetherlands,2020; pp. 225–249,
ISBN9780128191545.[CrossRef]
50. Uddamari,N.;Ubbana,J.Astudyonunsupervisedlearningalgorithmsanalysisinmachinelearning.Turk.J.Comput.Math.Educ.
2021,12,6774–6782.
51. Khanum, M.; Mahboob, T.; Imtiaz, W.; Ghafoor, H.; Sehar, R. A survey on unsupervised machine learning algorithms for
automation,classificationandmaintenance.Int.J.Comput.Appl.2015,119,34–39.[CrossRef]
52. Avinash,K.;William,G.;Ryan,B.NetworkAttackDetectionUsinganUnsupervisedMachineLearningAlgorithm.InProceedings
oftheHawaiiInternationalConferenceonSystemSciences(HICSS),Maui,HI,USA,7–10January2020.[CrossRef]
53. Chen,Y.;Kong,R.;Kong,L.Applicationsofartificialintelligenceinastronomicalbigdata.InBigDatainAstronomy;Kong,L.,
Huang,T.,Zhu,Y.,Yu,S.,Eds.;Elsevier:Amsterdam,TheNetherlands,2020;pp.347–375,ISBN9780128190845.[CrossRef]
54. VanEngelen,J.E.;Hoos,H.H.Asurveyonsemi-supervisedlearning.Mach.Learn.2020,109,373–440.[CrossRef]
55. ZhongKaizhu,G.;Huang,H.SemisupervisedLearning:Background,ApplicationsandFutureDirections;NovaSciencePublishers:
NewYork,NY,USA,2018.

Sensors2023,23,1467 28of30
56. Huynh,T.;Nibali,A.;He,Z.Semisupervisedlearningformedicalimageclassificationusingimbalancedtrainingdata.Comput.
MethodsProgramsBiomed.2022,216,106628.[CrossRef]
57. Kaur,A.;Gourav,K.Astudyofreinforcementlearningapplications&itsalgorithms.Int.J.Sci.Technol.Res.2020,9,4223–4228.
58. Mohammed,M.;Khan,M.B.;BashierMohammed,B.E.MachineLearning:AlgorithmsandApplications;CRCPress:BocaRaton,FL,
USA,2016.
59. Tanveer,J.;Haider,A.;Ali,R.;Kim,A.Anoverviewofreinforcementlearningalgorithmsforhandovermanagementin5G
ultra-densesmallcellnetworks.Appl.Sci.2022,12,426.[CrossRef]
60. Liu,S.;See,K.C.;Ngiam,K.Y.;Celi,L.A.;Sun,X.;Feng,M.Reinforcementlearningforclinicaldecisionsupportincriticalcare:
Comprehensivereview.J.Med.InternetRes.2020,22,e18477.[CrossRef][PubMed]
61. Hao,X.;Zhang,G.;Ma,S.Deeplearning.Int.J.Semant.Comput.2016,10,417–439.[CrossRef]
62. Nichols,J.A.;HerbertChan,H.W.;Baker,M.Machinelearning:Applicationsofartificialintelligencetoimaginganddiagnosis.
Biophys.Rev.2019,11,111–118.[CrossRef]
63. Sadiq,R.; Rodríguez,M.J.; Mian,H.R.EmpiricalmodelstopredictDisinfectionBy-Products(DBPs)indrinkingwater: An
updatedreview.InEncyclopediaofEnvironmentalHealth,2nded.;Nriagu,J.,Ed.;Elsevier:Amsterdam,TheNetherlands,2019;pp.
324–338,ISBN978-0-444-63952-3.
64. Teuwen,J.;Moriakov,N.Convolutionalneuralnetworks.InHandbookofMedicalImageComputingandComputerAssistedInterven-
tion;Zhou,S.K.,Rueckert,D.,Fichtinger,G.,Eds.;Elsevier:Amsterdam,TheNetherlands,2020;pp.481–501,ISBN9780128161760.
[CrossRef]
65. He,Z.DeepLearninginImageClassification:ASurveyReport.InProceedingsofthe2ndInternationalConferenceonInformation
TechnologyandComputerApplication(ITCA),Guangzhou,China,18–20December2020;pp.174–177.[CrossRef]
66. Khan,A.;Sohail,A.;Zahoora,U.;Qureshi,A.S.Asurveyoftherecentarchitecturesofdeepconvolutionalneuralnetworks.Artif.
Intell.Rev.2020,53,5455–5516.[CrossRef]
67. Cho,K.;vanMerrienboer,B.;Bahdanau,D.;Bengio,Y.OnthePropertiesofNeuralMachineTranslation: Encoder-Decoder
Approaches.arXiv2014,arXiv:1409.1259.
68. Elman,J.Findingstructureintime.Cogn.Sci.1990,14,179–211.[CrossRef]
69. Toha,S.F.;Tokhi,M.O.MLPandElmanRecurrentNeuralNetworkModellingfortheTRMS.InProceedingsofthe7thIEEE
InternationalConferenceonCyberneticIntelligentSystems,London,UK,9–10September2008;pp.1–6.[CrossRef]
70. Liu,Y.;Guo,J.;Cai,C.;Wang,Y.;Jia,L.Short-TermForecastingofRailTransitPassengerFlowBasedonLongShort-TermMemory
NeuralNetwork.InProceedingsoftheInternationalConferenceonIntelligentRailTransportation(ICIRT),Singapore,12–14
December2018;pp.1–5.[CrossRef]
71. Zhao,Z.;Liang,Y.;Jin,X.HandlingLarge-ScaleActionSpaceinDeepQNetwork.InProceedingsoftheInternationalConference
onArtificialIntelligenceandBigData(ICAIBD),Chengdu,China,26–28May2018;pp.93–96.[CrossRef]
72. Xie, W.; Ouyang, Y.; Ouyang, J.; Rong, W.; Xiong, Z. User Occupation Aware Conditional Restricted Boltzmann Machine
BasedRecommendation.InProceedingsoftheIEEEInternationalConferenceonInternetofThings(iThings)andIEEEGreen
ComputingandCommunications(GreenCom)andIEEECyber,PhysicalandSocialComputing(CPSCom)andIEEESmartData
(SmartData),Chengdu,China,15–18December2016;pp.454–461.[CrossRef]
73. Taylor,G.W.;Hinton,G.E.;Roweis,S.T.Twodistributed-statemodelsforgeneratinghigh-dimensionaltimeseries.J.Mach.Learn.
Res.2011,12,1025–1068.
74. Hinton,G.E.;Osindero,S.;Teh,Y.W.Afastlearningalgorithmfordeepbeliefnets.NeuralComput.2006,18,1527–1554.[CrossRef]
75. Bedi,G.;Venayagamoorthy,G.K.;Singh,R.DevelopmentofanIoT-drivenbuildingenvironmentforpredictionofelectricenergy
consumption.IEEEInternetThingsJ.2020,7,4912–4921.[CrossRef]
76. Timur,O.;Zor,K.;Çelik,Ö.;Teke,A.;I˙brikçi,T.Applicationofstatisticalandartificialintelligencetechniquesformedium-term
electricalenergyforecasting:Acasestudyforaregionalhospital.J.Sustain.Dev.EnergyWaterEnviron.Syst.2020,8,520–536.
[CrossRef]
77. Selvi,M.V.;Mishra,S.InvestigationofWeatherInfluenceinDay-AheadHourlyElectricLoadPowerForecastingwithNew
ArchitectureRealizedinMultivariateLinearRegressionArtificialNeuralNetworkTechniques.InProceedingsofthe8thIEEE
IndiaInternationalConferenceonPowerElectronics(IICPE),Jaipur,India,13–15December2018.
78. Selvi, M.V.; Mishra, S.Investigationofperformanceofelectricloadpowerforecastinginmultipletimehorizonswithnew
architecturerealizedinmultivariatelinearregressionandfeed-forwardneuralnetworktechniques.IEEETrans.Ind.Appl.2020,
56,5603–5612.[CrossRef]
79. Eseye,A.T.;Lehtonen,M.;Tukia,T.;Uimonen,S.;Millar,R.J.Machinelearningbasedintegratedfeatureselectionapproachfor
improvedelectricitydemandforecastingindecentralizedenergysystems.IEEEAccess2019,7,91463–91475.[CrossRef]
80. Wen,L.;Zhou,K.;Yang,S.Loaddemandforecastingofresidentialbuildingsusingadeeplearningmodel.Electr.PowerSyst.Res.
2020,179,106073.[CrossRef]
81. Rodríguez,F.;Galarza,A.;Vasquez,J.C.;Guerrero,J.M.Usingdeeplearningandmeteorologicalparameterstoforecastthe
photovoltaicgeneratorsintra-houroutputpowerintervalforsmartgridcontrol.Energy2022,239,122116.[CrossRef]
82. Taleb,I.;Guerard,G.;Fauberteau,F.;Nguyen,N.A.Flexibledeeplearningmethodforenergyforecasting.Energies2022,15,3926.
[CrossRef]

Sensors2023,23,1467 29of30
83. Xu,A.;Tian,M.-W.;Firouzi,B.;Alattas,K.A.;Mohammadzadeh,A.;Ghaderpour,E.AnewdeeplearningRestrictedBoltzmann
Machineforenergyconsumptionforecasting.Sustainability2022,14,10081.[CrossRef]
84. YemSouhe,F.G.;FranklinMbey,C.;TeplairaBoum,A.;Ele,P.;FobaKakeu,V.J.Ahybridmodelforforecastingtheconsumption
ofelectricalenergyinasmartgrid.J.Eng.2022,6,629–643.[CrossRef]
85. Aurangzeb,K.;Alhussein,M.;Javed,K.;Haider,S.I.APyramid-CNNbaseddeeplearningmodelforpowerloadforecastingof
similar-profileenergycustomersbasedonclustering.IEEEAccess2021,9,14992–15003.[CrossRef]
86. Jahangir,H.;Tayarani,H.;Gougheri,S.S.;Golkar,M.A.;Ahmadian,A.;Elkamel,A.Deeplearning-basedforecastingapproachin
smartgridswithmicroclusteringandbidirectionalLSTMnetwork.IEEETrans.Ind.Electron.2021,68,8298–8309.[CrossRef]
87. Mubashar,R.;Awan,M.J.;Ahsan,M.;Yasin,A.;Singh,V.P.Efficientresidentialloadforecastingusingdeeplearningapproach.
Int.J.Comput.Appl.Technol.2022,68,205–214.[CrossRef]
88. Rosato,A.;Araneo,R.;Andreotti,A.;Panella,M.2-DConvolutionalDeepNeuralNetworkforMultivariateEnergyTimeSeries
Prediction.InProceedingsofthe2019IEEEInternationalConferenceonEnvironmentandElectricalEngineeringand2019IEEE
IndustrialandCommercialPowerSystemsEurope(EEEIC/I&CPSEurope),Genova,Italy,11–14June2019.
89. Zhang,X.;Biagioni,D.;Cai,M.;Graf,P.;Rahman,S.Anedge-cloudintegratedsolutionforbuildingsdemandresponseusing
reinforcementlearning.IEEETrans.SmartGrid2020,12,420–431.[CrossRef]
90. Aurangzeb,K.;Alhussein,M.DeepLearningFrameworkforShort-termPowerLoadForecasting,aCaseStudyofIndividual
HouseholdEnergyCustomer.InProceedingsofthe2019InternationalConferenceonAdvancesintheEmergingComputing
Technologies(AECT),AlMadinahAlMunawwarah,SaudiArabia,10February2020.
91. Escobar, E.; Rodríguez Licea, M.A.; Rostro-Gonzalez, H.; Espinoza Calderon, A.; Barranco Gutiérrez, A.I.; Pérez-Pinal, F.J.
ComparativeAnalysisofMultivariableDeepLearningModelsforForecastinginSmartGrids.InProceedingsofthe2020IEEE
InternationalAutumnMeetingonPower,ElectronicsandComputing(ROPEC),Ixtapa,Mexico,4–6November2020.[CrossRef]
92. Hafeez,G.;Alimgeer,K.S.;Wadud,Z.;Shafiq,Z.;AliKhan,M.U.;Khan,I.;Khan,F.A.;Derhab,A.Anovelaccurateandfast
convergingdeeplearning-basedmodelforelectricalenergyconsumptionforecastinginasmartgrid. Energies2020,13,2244.
[CrossRef]
93. Nguyen,V.-B.;Duong,M.-T.;Le,M.-H.ElectricityDemandForecastingforSmartGridbasedonDeepLearningApproach.In
Proceedingsofthe20205thInternationalConferenceonGreenTechnologyandSustainableDevelopment(GTSD),HoChiMinh
City,Vietnam,27–28November2020;pp.353–357.[CrossRef]
94. Rosato,A.;Succetti,F.;Araneo,R.;Andreotti,A.;Mitolo,M.;Panella,M.ACombinedDeepLearningApproachforTimeSeries
PredictioninEnergyEnvironments. InProceedingsofthe2020IEEE/IAS56thIndustrialandCommercialPowerSystems
TechnicalConference(I&CPS),LasVegas,NV,USA,29June–28July2020.
95. Qi,X.;Zheng,X.;Chen,Q.AShort-termLoadForecastingofIntegratedEnergySystembasedonCNN-LSTM.InProceedingsof
the2020InternationalConferenceonEnergy,EnvironmentandBioengineering(ICEEB2020),Xi’an,China,7–9August2020;
Volume185,p.01032.[CrossRef]
96. Wang,B.;Li,Y.;Ming,W.;Wang,S.Deepreinforcementlearningmethodfordemandresponsemanagementofinterruptibleload.
IEEETrans.SmartGrid2020,11,3146–3155.[CrossRef]
97. Wen,L.;Zhou,K.;Li,J.;Wang,S.Modifieddeeplearningandreinforcementlearningforanincentive-baseddemandresponse
model.Energy2020,205,118019.[CrossRef]
98. Yang,Y.;Li,W.;Gulliver,T.A.;Li,S.Bayesiandeeplearning-basedprobabilisticloadforecastinginsmartgrids.IEEETransInd.
Inf.2020,16,4703–4713.[CrossRef]
99. Amin,P.;Cherkasova,L.;Aitken,R.;Kache,V.AutomatingEnergyDemandModelingandForecastingUsingSmartMeterData.
InProceedingsofthe2019IEEEInternationalCongressonInternetofThings(ICIOT),Milan,Italy,8–13July2019.
100. Atef,S.;Eltawil,A.B.AComparativeStudyUsingDeepLearningandSupportVectorRegressionforElectricityPriceForecasting
inSmartGrids.InProceedingsoftheIEEE6thInternationalConferenceonIndustrialEngineeringandApplications(ICIEA),
Tokyo,Japan,12–15April2019;pp.603–607.[CrossRef]
101. Chan, S.; Oktavianti, I.; Puspita, V. A Deep Learning CNN and AI-Tuned SVM for Electricity Consumption Forecasting:
MultivariateTimeSeriesData. InProceedingsofthe2019IEEE10thannualinformationtechnology,ElectronicsandMobile
CommunicationConference(IEMCON),Vancouver,BC,Canada,17–19October2019.
102. Hafeez,G.;Javaid,N.;Riaz,M.;Ali,A.;Umar,K.;Iqbal,Q.Z.DayAheadElectricLoadForecastingbyanIntelligentHybrid
ModelbasedonDeepLearningforSmartGrid.InProceedingsofthe14thInternationalConferenceonComplex,Intelligentand
SoftwareIntensiveSystems(CISIS-2020),Lodz,Poland,1–3July2020.
103. Kaur, D.; Kumar, R.; Kumar, N.; Guizani, M.SmartGridEnergyManagementusingRNN-LSTM:ADeepLearning-Based
Approach.InProceedingsoftheIEEEGlobalCommunicationsConference(GLOBECOM),BigIsland,HI,USA,9–13December
2019;pp.1–6.[CrossRef]
104. AlKhafaf,N.;Jalili,M.;Sokolowski,P.Applicationofdeeplearninglongshort-termmemoryinenergydemandforecasting.
Commun.Comput.Inf.Sci.2019,1000,31–42.
105. Khan,A.B.M.;Khan,S.;Aimal,S.;Khan,M.;Ruqia,B.;Javaid,N.Halfhourlyelectricityloadforecastingusingconvolutional
neuralnetwork.InInnovativeMobileandInternetServicesinUbiquitousComputing;Barolli,L.,Xhafa,F.,Hussain,O.,Eds.;Springer:
Cham,Switzerland;Volume994.[CrossRef]

Sensors2023,23,1467 30of30
106. Kim,T.Y.;Cho,S.B.PredictingresidentialenergyconsumptionusingCNN-LSTMneuralnetworks. Energy2019,182,72–81.
[CrossRef]
107. Kim,T.;Cho,S.ParticleSwarmOptimization-basedCNN-LSTMNetworksforForecastingEnergyConsumption.InProceedings
ofthe2019IEEECongressonEvolutionaryComputation(CEC),Wellington,NewZealand,10–13June2019.
108. Lu,R.;Hong,S.H.Incentive-baseddemandresponseforsmartgridwithreinforcementlearninganddeepneuralnetwork.Appl.
Energy2019,236,937–949.[CrossRef]
109. Pramono,S.H.;Rohmatillah,M.;Maulana,E.;Hasanah,R.N.;Hario,F.Deeplearning-basedshort-termloadforecastingfor
supportingdemandresponseprograminhybridenergysystem.Energies2019,12,3359.[CrossRef]
110. Rahman,S.;Alam,M.G.R.;Rahman,M.M.DeepLearningbasedEnsembleMethodforHouseholdEnergyDemandForecasting
ofSmartHome.InProceedingsofthe201922ndInternationalConferenceonComputerandInformationTechnology(ICCIT),
Dhaka,Bangladesh,18–20December2019.
111. Syed,D.;Refaat,S.S.;Abu-Rub,H.;Bouhali,O.;Zainab,A.;Xie,L.AveragingEnsemblesModelforForecastingofShort-Term
LoadinSmartGrids.InProceedingsoftheIEEEInternationalConferenceonBigData(BigData),LosAngeles,CA,USA,9–12
December2019;pp.2931–2938.[CrossRef]
112. UstundagSoykan,E.;Bilgin,Z.;Ersoy,M.A.;Tomur,E.DifferentiallyPrivateDeepLearningforLoadForecastingonSmart
Grid.InProceedingsofthe2019IEEEGlobecomWorkshops(GCWkshps),Waikoloa,HI,USA,9–13December2019;pp.1–6.
[CrossRef]
113. Vesa, A.V.; Ghitescu, N.; Pop, C.; Antal, M.; Cioara, T.; Anghel, I.A.; Salomie, I. Stacking Ulti-Learning Ensemble Model
for Predicting Near Real Time Energy Consumption Demand of Residential Buildings. In Proceedings of the 2019 IEEE
15thInternationalConferenceonIntelligentComputerCommunicationandProcessing(ICCP),Cluj-Napoca,Romania,5–7
September2019.
114. Yang,Y.;Hong,W.;Li,S.Deepensemblelearningbasedprobabilisticloadforecastinginsmartgrids.Energy2019,189,116324.
[CrossRef]
115. Zahid,M.;Ahmed,F.;Javaid,N.;Abbasi,R.A.;ZainabKazmi,H.S.;Javaid,A.;Bilal,M.;Akbar,M.;Ilahi,M.Electricitypriceand
loadforecastingusingenhancedconvolutionalneuralnetworkenhancedsupportvectorregressioninsmartgrids.Electronics
2019,8,122.[CrossRef]
116. Ouyang,T.;He,Y.;Li,H.;Sun,Z.;Baek,S.Modelingandforecastingshort-termpowerloadwithcopulamodelanddeepbelief
network.IEEETrans.Emerg.Top.Comput.Intell.2019,3,127–136.[CrossRef]
117. Hafeez,G.;Javaid,N.;Ullah,S.;Iqbal,Q.Z.;Khan,M.;Rehman,A.U.;Ullah,Z.Short-TermLoadForecastingbasedonDeep
LearningforSmartGridApplications.InProceedingsofthe12thInternationalConferenceonInnovativeMobileandInternet
ServicesinUbiquitousComputing(IMIS-2018),Matsue,Japan,4–6July2018.[CrossRef]
118. Koprinska,I.;Wu,D.;Wang,Z.ConvolutionalNeuralNetworksforEnergyTimeSeriesForecasting.InProceedingsofthe2018
InternationalJointConferenceonNeuralNetworks(IJCNN),RiodeJaneiro,Brazil,8–13July2018.
119. Kuo,P.H.;Huang,C.J.Ahighprecisionartificialneuralnetworksmodelforshort-Termenergyloadforecasting.Energies2018,11,
213.[CrossRef]
120. Shi,H.;Xu,M.;Li,R.Deeplearningofhouseholdloadforecasting—AnovelpoolingdeepRNN.IEEETransSmartGrid2018,9,
5271–5280.[CrossRef]
121. Ghaderi,A.;Sanandaji,B.M.;Ghaderi,F.Deepforecast:Deeplearning-basedspatio-temporalforecasting.arXiv2017.[CrossRef]
122. Jarábek,T.;Laurinec,P.;Lucká,M.EnergyLoadForecastusingS2SDeepNeuralNetworkswithk-ShapeClustering.InProceed-
ingsofthe2017IEEE14thInternationalScientificConferenceonInformatics2017,Poprad,Slovakia,14–16November2017.
123. Li,L.;Ota,K.;Dong,M.EverythingisImage:CNN-BasedShort-TermElectricalLoadForecastingforSmartGrid.InProceedingsof
the201714thInternationalSymposiumonPervasiveSystems,AlgorithmsandNetworks&201711thInternationalConferenceon
FrontierofComputerScienceandTechnology&2017ThirdInternationalSymposiumofCreativeComputing(ISPAN-FCST-ISCC),
Exeter,UK,21–23June2017;pp.344–351.[CrossRef]
124. Zhan,J.;Huang,J.;Niu,L.;Peng,X.;Deng,D.;Cheng,S.StudyoftheKeyTechnologiesofElectricPowerBigDataandIts
ApplicationProspectsinSmartGrid.InProceedingsoftheIEEEPESAsia-PacificPowerandEnergyEngineeringConference
(APPEEC),HongKong,China,7–10December2014;pp.1–4.[CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.