electronics
Article
Single and Multiple Separate LSTM Neural Networks for
Multiple Output Feature Purchase Prediction
MilicaC´iric´ 1,* ,BratislavPredic´ 2 ,DraganStojanovic´ 2andIvanC´iric´ 3,*
1 FacultyofCivilEngineeringandArchitecture,UniversityofNiš,AleksandraMedvedeva14,18000Niš,Serbia
2 FacultyofElectronicEngineering,UniversityofNiš,AleksandraMedvedeva12,18000Niš,Serbia;
bratislav.predic@elfak.ni.ac.rs(B.P.);dragan.stojanovic@elfak.ni.ac.rs(D.S.)
3 FacultyofMechanicalEngineering,UniversityofNiš,AleksandraMedvedeva14,18000Niš,Serbia
* Correspondence:milica.ciric@gaf.ni.ac.rs(M.C´.);ivan.ciric@masfak.ni.ac.rs(I.C´.)
Abstract: Dataconcerningproductsalesareapopulartopicintimeseriesforecastingduetotheir
multidimensionality and wide presence in many businesses. This paper describes the research
inpredictingthetimingandproductcategoryofthenextpurchasebasedonhistoricalcustomer
transactiondata.Giventhatthedatasetwasacquiredfromavendorofmedicaldrugsanddevices,
thegenericproductidentifier(GPI)classificationsystemwasincorporatedinassigningproduct
categories. Themodelsbuiltarebasedonrecurrentneuralnetworks(RNN)andlongshort-term
memory(LSTM)neuralnetworkswithdifferentinputandoutputfeatures,andtrainingdatasets.
Experimentswithvariousdatasetswereconductedandoptimalnetworkstructuresandtypesfor
predictingbothproductcategoryandnextpurchasedaywereidentified.Thekeycontributionofthis
researchistheprocessofdatatransformationfromitsoriginalpurchasetransactionformatintoatime
seriesofinputfeaturesfornextpurchaseprediction.Withthisapproach,itispossibletoimplementa
dedicatedpersonalizedmarketingsystemforavendor.
Keywords:recurrentneuralnetworks;purchaseforecasting;timeseriesprediction
1. Introduction
Citation:C´iric´,M.;Predic´,B.;
Stojanovic´,D.;C´iric´,I.Singleand Thepredictionoffinancialdatahasbeenachallengingtopicforalongtimeandwas
MultipleSeparateLSTMNeural addressed by many researchers. Among other things, researchers have tried to predict
NetworksforMultipleOutput the following: the future values of stock prices [1–3], foreign exchange rates [4], sale
FeaturePurchasePrediction. volumesofoneormultipleproductcategories[5–7],andtheproductcategoryofthenext
Electronics2023,12,2616. https:// purchase[8,9]. Thepredictionofsalesdataisparticularlyinterestingasaresearchtopicdue
doi.org/10.3390/electronics12122616 tohowwidespreaditis. Additionally,ithasmanydimensionsthatcanbetargetedwhen
predictingafuturepurchase: timingofthepurchase,productcategory,quantity,orwill
AcademicEditor:JavidTaheri
thecustomerevenmakeanotherpurchase. Ifthepredictionshaveareasonablereliability,
Received:6May2023 thebusinessescanusetheminmakingdecisionsforinventoryorproductionplanning,
Revised:4June2023 personalizedmarketingordeterminingprices. Suchadditionalinformationcanbeusedto
Accepted:8June2023 preventbusinesscrisisorevenincreaseprofit[10].
Published:10June2023 Salesdatacanberepresentedasatimeserieswherepastvaluesareknownandthe
futurevaluesarewhatarebeingpredicted. Therearemanymethodsusedforthistask,
and each has its benefits and disadvantages while their performance varies based on
the application [11]. Recently, artificial neural networks have been used in time series
Copyright: © 2023 by the authors.
forecasting,oftenoutperformingmore“traditional”methods[12,13]. Forfinancialdata
Licensee MDPI, Basel, Switzerland.
specifically,statisticalmodelsarenotbestsuitedduetotheirnon-stationarynature. Atype
This article is an open access article
ofrecurrentneuralnetworks(RNNs),alongshort-termmemoryneuralnetwork(LSTM),
distributed under the terms and
hasanadvantagewhenworkingwithtimeseriesthathavelong-termdependencies. This
conditionsoftheCreativeCommons
Attribution(CCBY)license(https:// isduetothevanishinggradientproblemofRNNsthatissolvedinLSTMneuralnetworks.
creativecommons.org/licenses/by/ LSTMs were found to generally perform better than other methods with longer time
4.0/). ranges[14].
Electronics2023,12,2616.https://doi.org/10.3390/electronics12122616 https://www.mdpi.com/journal/electronics

Electronics2023,12,2616 2of14
Thisresearchwasstartedwiththegoalofpredictingacustomer’snextpurchasebased
ontheinformationofpreviouspurchases. Theprocesswasstartedbypredictingthenext
purchasedayforeachcustomer. Initialworkwasdonewithstatisticalmethods[15,16],
whichwerethencomparedtoneuralnetworks[17]andfinallyadditionalfeatureswere
addedtoneuralnetworkstoachievebetterresults[18]. Thenextlogicalquestionwasifit
ispossibletopredicttheproductcategoryforthenextpurchasewithadequatereliability.
Informationaboutthepredictedcontentsofthenextpurchasecouldbeusedinpersonalized
advertisingandincreatingcustomer-specificoffers. Theresearchpresentedinthispaper
focusesonpredictingproductcategoriesthatwillappearinthenextpurchaseofaspecific
customer. Additionally,thepredictionofproductcategoriesandnextpurchasedayoutput
featureswithdifferentneuralnetworksetupsarecompared. Themaintakeawayisthat
deciding what approach is best definitely depends on the output feature and it is best
totrydifferentapproachesbeforemakingafinaldecision. Theexperimentsperformed
with multiple setups and datasets showed that a dedicated neural network produced
significantly better results in predicting the product category, while for predicting the
timingofthenextpurchase,thesinglemultivariateneuralnetworkwassuperior. Themain
noveltyandresearchcontributionliesindatapreprocessingandtransformationappliedto
theoriginaldataformatinordertoformtheoptimalinputdatastructureforpresentedtime
seriesprediction. Specifically,ahierarchicalclassificationsystemwasusedfordefining
product categories and creating a new type of input feature vector. This original input
featurevectoraffectsbothproductcategorypredictionandnextpurchasedayprediction.
Anadditionaladvantageliesintheapplicabilityandusabilityofthenetworkoutputresults
in various vendor commercial purposes. The rest of the paper is structured as follows.
Section2isanoverviewoftheliteraturereviewinpredictioninsalesandotherfinancial
data. Section3providesthedescriptionoftheusedmethodology,includingthedataset.
Section4containstheresultsofconductedexperiments,whilethediscussionoftheresults
isinSection5. Finally,theconclusionsaregiveninSection6.
2. LiteratureReview
In [4], the authors use a combination of symbolic processing and recurrent neural
networksforforeignexchangerateprediction. Theyarguethatthemethodsusedarebetter
suitedforhighnoise,highlynon-stationaritytimeseriesprediction. Intheirexperiments,
theyachieveda47.1%errorrateinpredictingthedirectionofchangesandwereableto
lowerthatrateto40%byexcludingexamplesforwhichthesystemhadlowprediction
confidence.
The research presented in [5] focuses on comparing XGBoost-LSTM combination
forecastingmodelwithclassicaltimeseriespredictionmodelsforthepurposeofforecasting
sales volume. Results for the combination model were much better than the original
XGBoostsinglemodel.
LSTMwasthebestperformingmodelforcustomerproductpredictioninresearchtry-
ingtopredictwhichuserswillbuymobiledevicesorcamerasbasedontweetsmentioning
thesedevicescollectedfromtheTwitterAPI[19]. However,fordeterminingrelevanceto
customerpurchasingbehaviour,afeed-forwardneuralnetworkachievedbetterresults. In
thisresearch,predictingthepurchasewasaidedbythesequentialnatureofthetweets.
Accordingtotheauthorsof[20],iftherearecross-correlations,amultivariatetime
seriesmodelwillprobablygeneratemoreaccurateforecastswhencomparedtounivariate
models. However,iftherearenocorrelations,itisusuallytheotherwayaround. Inthis
research,thebestresultswereachievedwhenusingARIMA(comparedtounivariateand
multivariate state space models) and the authors’ explanations were that the case of a
touristflowfromdifferentEuropeancountriestoSeychellesshowsanabsenceofa‘rich’
cross-correlationstructure.
Esnafietal. in[6]describethecomparisonofmanydifferentmethodsforpredicting
furnituresalesasanexampleofseasonaltimeseries. Theauthorsconcludethatneural
networks in general performed better than classical forecasting methods with stacked

Electronics2023,12,2616 3of14
LSTMbeingthebest. Intotal,Prophet,LSTM,stackedLSTMandCNNweretheclosestin
predictionperformance.
Aninterestingapproachispresentedin[21]. Theauthorsdevelopedagraph-multi-
scalepyramidnetworks(GMP)frameworkwiththeintentofincludingmulti-scaletemporal
dynamics and arbitrary inter-dependencies that exist between product categories. The
partoftheGMPisaconvolutionalneuralnetworkwhosetaskistoencodethecategorical
temporalpatternatallscales(daily,weekly,bi-weekly,monthly). Theirexperimentsshow
thatthismethodperformsbetterthanthestate-of-the-artbaselines.
In purchase prediction, one of the main challenges in the non-contractual setting
is how to differentiate customers that are currently in between transactions and those
thatwillnotreturn[22]. Aproposedsolutionhasbeendevelopedasamachinelearning
frameworkforforecastingfuturepurchasesbasedonthecustomertransactiondatabase.
Inthisresearch,customercharacteristicsweredeterminedonamonthlylevel. Someof
thecustomercharacteristicsincludedthefollowing: thenumberoftotalpurchases, the
meantimebetweenpurchases,themeanvaluesofpurchases,andthetimeframevariation.
Intheirexperiments,theyusedlogisticlassoregression,extremelearningmachineand
gradient tree boosting on transactional data of a central European manufacturer, with
gradienttreeboostingoutperformingtheothertwo.
However,accordingto[23],despiteexperimentingwithdifferentnetworksetupsand
featurecombinations,therewasnotasinglesetup/combinationthatcouldachievesuperior
resultsinallthreeoftheposedtasks. TheauthorsusedanLSTMneuralnetworktoforecast
dayoftheweek,timeofdayandproductcategoryforanonlineshoppingstoreandhad
themostdifficultyinpredictingtheproductcategory.
Both [24,25] suggest that there is a difference in the purchasing process, as well as
featureinteraction,whenacustomeractuallymakesapurchaseandwhentheyaresimply
browsingand/orgiveuponthepurchase.
Additionally,thepurposeofapurchasecanbeafactorinpurchasedecisionmaking.
Theauthorsof[26]arguethatpersonalpurchasesarecharacterizedasimpulsive,while
businesspurchasesfollowamorerigid,formalizedprocesswherethereisa“need”,nota
“want”.
The topic of [27] is to predict purchase behaviour in large product assortments by
usingpurchasehistorydataandpotentiallycustomercharacteristics. Theyconsiderlatent
DirichletallocationandmixturesofDirichlet-multinomials,andconcludethattheformer
performssimilartothelatterwhilebeingfarmorescalable.
Consumer behaviour was also analysed in [28] in order to build a model for fore-
castingthenextpurchasedateandthepurchaseamount. Inputdatawascollectedfrom
confirmationemailssenttocustomersafterpurchase. Inthisresearch,thebestperforming
modelwasBayesiannetworkclassification.
In[29],asalesforecastingmodelbasedonLSTMwasdevelopedwhereoneoftheinput
variables,“numberoftheactivebookersperday”,wasestimated. Theuseofapredicted
variableasaninputvariabletoanothermodelincreasesthechanceofuncertaintyentering
thesystem,whilethesalespredictionsresultsdependonvariousuncertaintiesornoise
duetotheestimatedinputvariableanddifferentnoisedistributionssuchasnormalized,
uniform,andlogisticdistributions.
Luoet. al. proposedtheextremedeepfactorizationmachine(xDeepFM)modelto
explorethecorrelationsbetweenthesales-influencingfeaturesasmuchaspossible,and
then modelled the sales prediction using LSTM in [30] to improve the accuracy of the
predictionmodel. Thehybridforecastingmodelhasahigheroptimizationratecompared
toothermodelsandprovidesascientificbasisforapparelcompanies’demandplans.
Seasonal long short-term memory (SLSTM) was presented in [31] as a method for
predictingthesalesofagriculturalproductstostabilizesupplyanddemand. TheSLSTM
modelistrainedusingtheseasonalityattributesofweek,month,andquarterasadditional
inputstohistoricaltime-seriesdata. TheforecastingresultsoftheproposedSLSTMmodel

Electronics 2023, 12, x FOR PEER REVIEW 4 of 16
Electronics2023,12,2616 4of14
model is trained using the seasonality attributes of week, month, and quarter as additional
inputs to historical time-series data. The forecasting results of the proposed SLSTM model
were compared to auto ARIMA, Prophet, and a standard LSTM and SLSTM outperforms
werecomparedtoautoARIMA,Prophet,andastandardLSTMandSLSTMoutperforms
the other presented models regarding the metrics proposed in their research.
theotherpresentedmodelsregardingthemetricsproposedintheirresearch.
Based on the analysed research, it can be concluded that the main advantage of LSTM
Based on the analysed research, it can be concluded that the main advantage of
neural networks is their ability to capture both short-term and long-term sequence pat-
LSTMneuralnetworksistheirabilitytocapturebothshort-termandlong-termsequence
terns. Their complexity, however, increases training times, which can be a problem if time
patterns. Theircomplexity,however,increasestrainingtimes,whichcanbeaproblemif
constraints exist.
timeconstraintsexist.
33.. MMeetthhooddss
TThhee wwhhoollee ppuurrcchhaassee pprreeddiiccttiioonn pprroocceessss ffrroomm ccoolllleeccttiinngg ddaattaa ttoo eevvaalluuaattiinngg rreessuullttss iiss
sshhoowwnn iinn FFiigguurree1 1..T Thheed daatatai sisc coollleleccteteddf rforommt htheed dataatbaabsaesec ocnotnatianiinnignga lallpl uprucrhcahsaester atrnasnasc--
taioctnios,ncsu, sctuosmtoemr,earn, danpdro pdruocdtuinctf oinrmfoartmioant.ioNne. xNt,esxetv, eseravledraalt adatrtaan tsrfaonrsmfoartmioantiporno cpersosceessasrees
aaprep laiepdpltioeda dtoa patddaaptta dfoatrat hfoerr ethger ersesgiorenssmioond eml.oTdheils. Tishfios llios wfoeldlowweitdh wthietht rtahien itnrgaionfinmgu olf-
tmipuleltiLpSlTe MLSnTeMu rnaelunreatlw noertwksowrkisth wditihff edrieffnetriennpt uintpaundt aonudt pouuttpfeuatt fueraetsu.rFeisn. aFlilnya,lplyre, dpircetdioicn-
rteiosunl rtsesaurletse vaarelu eavtaeldu.ated.
FFiigguurree 11.. TThhee ppuurrcchhaassee pprreeddiiccttiioonn pprroocceessss..
TThhee nnoovveellttyy,, ccoommppaarreedd ttoo rreellaatteedd wwoorrkk,, iiss uussiinngg tthhee ggeenneerriicc pprroodduucctt iiddeennttiififieerrss ffoorr
ddeefifinniinngg pprroodduucctt ccaatteeggoorriieess.. AAddddiittiioonnaallllyy,,a an neeww ttyyppee ooff iinnppuutt ffeeaattuurree iiss ccoonnssttrruucctteedd bbaasseedd
oonn ggeenneerriicc pprroodduucctt iiddeennttiififieerr ((GGPPII)) vvaalluueess ffoorr pprroodduuccttss iinn tthhee ppuurrcchhaassee.. TThhiiss ffeeaattuurree iiss aa
mmuullttii--hhoott eennccooddeedd vveeccttoorr nnaammeedd tthhee GGPPII ddrruuggg grroouupp//ccaatteeggoorryy vveeccttoorr.. OOnnee bbeenneefifitt ooff tthhee
pprrooppoosseedd aapppprrooaacchh iiss tthhee ppoossssiibbiilliittyy ooff aappppllyyiinngg iitt ttoo aa ddiiffffeerreenntt ddoommaaiinn wwiitthh aa ddeefifinneedd
ccllaassssiifificcaattiioonn ssyysstteemm ssiimmiillaarr ttoo GGPPII..
IInnddiivviidduuaall ppaarrttss ooff tthhee ppuurrcchhaassee pprreeddiiccttiioonn pprroocceessss aarree ddeessccrriibbeedd iinn tthhee ffoolllloowwiinngg
ssuubbsseeccttiioonnss..
3.1. DataCollection
3.1. Data Collection
This research was performed with data acquired from a medical device and drug
This research was performed with data acquired from a medical device and drug
company. Thedatawascollectedfromthedatabasecontainingallpurchasetransactions,
company. The data was collected from the database containing all purchase transactions,
customer, and product information. Collected data consist of purchasing transactions
customer, and product information. Collected data consist of purchasing transactions for
foragreatnumberofcustomersduringafour-and-a-half-yearperiod. Allthepersonal
identifiableinformationwasanonymizedbeforeanyotherdatatransformationprocess.

Electronics 2023, 12, x FOR PEER REVIEW 5 of 16
a great number of customers during a four-and-a-half-year period. All the personal iden-
Electronics2023,12,2616 5of14
tifiable information was anonymized before any other data transformation process.
The original format of the data contained around 7.5 million transactions including
data such as the identifier of the customer, the identifier of the product, the quantity of
Theoriginalformatofthedatacontainedaround7.5milliontransactionsincluding
the product, and the date and time of the transaction. Each transaction was for a single
datasuchastheidentifierofthecustomer,theidentifieroftheproduct,thequantityof
product even though a customer had (usually) ordered multiple products, because each
theproduct,andthedateandtimeofthetransaction. Eachtransactionwasforasingle
was recorded separately. After aggregating transactions from the same order and remov-
producteventhoughacustomerhad(usually)orderedmultipleproducts,becauseeach
ing customers with less than four orders, just under one million orders remained. Those
wasrecordedseparately. Afteraggregatingtransactionsfromthesameorderandremoving
orders were made by around 10,100 customers. Figure 2 shows the histogram of the num-
customerswithlessthanfourorders,justunderonemillionordersremained. Thoseorders
ber of orders per customer. It is noticeable that the majority of customers made 200 or less
weremadebyaround10,100customers. Figure2showsthehistogramofthenumberof
orders.
orderspercustomer. Itisnoticeablethatthemajorityofcustomersmade200orlessorders.
FFigiguurree2 2..H Hisisttooggrraammo offt thheen nuummbbeerro offo orrddeerrssp peerrc cuusstotommeer.r.
3.2. DataPreprocessing
3.2. Data Preprocessing
Datapre-processingandbuildingtrainingdatasetswasperformedinPython,utilizing
Data pre-processing and building training datasets was performed in Python, utiliz-
thePandaslibrary[32].
ing the Pandas library [32].
Thefirststepindatatransformationwasanonymizingallpersonalidentifiableinfor-
The first step in data transformation was anonymizing all personal identifiable infor-
mation. Next,GPIorpartialGPIwasdeterminedonanindividualbasisandthosedata
mation. Next, GPI or partial GPI was determined on an individual basis and those data
wereaddedtoproductinformation.
were added to product information.
Originaldataproductinformationcontainedpropertiessuchasproductidentifiers
Original data product information contained properties such as product identifiers
(internalID,notrelevantoutsidethesystem),productnamesandGPIs. TheGPI(generic
(internal ID, not relevant outside the system), product names and GPIs. The GPI (generic
product identifier) is a 14-character therapeutic classification system. It contains seven
product identifier) is a 14-character therapeutic classification system. It contains seven 2-
2-characterhierarchicalgroupswhereeachtiercontainsdifferentinformationaboutadrug
character hierarchical groups where each tier contains different information about a drug
product: druggroup,drugclass,drugsubclass,drugbasename,drugname,doseform
product: drug group, drug class, drug subclass, drug base name, drug name, dose form
anddosestrength. Thislevelofgranularityenablesstoringverygeneralorveryspecific
and dose strength. This level of granularity enables storing very general or very specific
informationaboutadrugproduct[33].
information about a drug product [33].
GPIsareuniversalandcanbeusedfordrugproductsfromallvendors. However,the
GPIs are universal and can be used for drug products from all vendors. However, the
fullGPIwasnotavailableinthesystemforallproducts. Abouthalfoftheproductshad
afufulll lGGPPI wIsatso rneodt ,awvahiillaebtleh einr ethste hsyadstenmo vfoarl uaells p. rTohdeuGctPs.I Acobnoutati hnasl7f otife trhseo pfriondfourcmtsa htiaodn a,
bfuutll nGoPtIa slltowreedre, wnehcilees stharey refostr heaadch noo fvtahlueeast.t eTmhep GtePdI pcorendtaicintiso n7 st.ieSrisn ocfe inthfoer2m-cahtiaorna,c tbeurt
gnrootu aplsl wareereh ineercaerscshaircya lf,oirt ewaachs poof sthsieb alettteomfipltleidn pthreedfiicrtsiton4st.o S8incche atrhaec 2te-rcshaforarcatelmr gorsotuaplls
parroed huicetrsaurcshinicgaal,v iat iwlaabsle pporsosdibulect tion ffiol,l liena tvhine gfiorsntl y4 2to.5 8% cohfatrhaectperrso dfourc taslmwoitsht oaullt panroydGuPctIs
inufsoinrmg aatvioainla.ble product info, leaving only 2.5% of the products without any GPI infor-
matiTohne. first 2-characters represent the drug group. There are 99 possible values, i.e.,
99druTgheg rfiorustp 2s-,cwhahriacchtecrasn rbepergersoeuntp tehde idnr1u5g cgartoeugpor. iTehseorfes aimrei l9a9r pdorsusgibgler ovuapluse.sI,n i.be.o, t9h9
cdarsuesg, garnoaudpds,i twiohniaclhU cannk nboew grnovuapleude iwn a1s5 ccoantesgidoerrieesd o,rf espimreisleanr tdinruggp groroduupcsts. Imn ibsositnhg caGsPesI,
daant aa.dAdibtaiorncahla Urtnrekpnroewsenn tvinalguteh ewnaus mcobnesriodfepreudr,c hreapsersesceonnttianign ipnrgoedaucchtso fmthises1in0g0 GGPPII ddrautga.
groupsisgiveninFigure3. Evidently,notalldruggroupsareequallyrepresented—some
areorderedmuchmorefrequentlythanothers.

Electronics 2023, 12, x FOR PEER REVIEW 6 of 16
A bar chart representing the number of purchases containing each of the 100 GPI drug
Electronics2023,12,2616 6of14
groups is given in Figure 3. Evidently, not all drug groups are equally represented—some
are ordered much more frequently than others.
Figure3.Numberofordersperdruggroup.
Figure 3. Number of orders per drug group.
Collected transaction data contained information about the date and time of the
Collected transaction data contained information about the date and time of the pur-
purchase. In the following step, input data were adapted for the regression model by
chase. In the following step, input data were adapted for the regression model by trans-
transforming the date/time information into a value that signifies the number of days
forming the date/time information into a value that signifies the number of days that have
thathavepassedbetweenthepreviousrelevantpurchaseandthecurrentpurchase. This
passed between the previous relevant purchase and the current purchase. This way, the
way,thetimeseriesdescribingthepurchasehistorycontainedaseriesofnumbers,each
time series describing the purchase history contained a series of numbers, each represent-
representingthenumberofdaysthatpassedbetweentwoconsecutivepurchases. Tobe
ing the number of days that passed between two consecutive purchases. To be able to
abletocreateatimeseries,aminimumoftworelevantpurchasesareneeded,butagreater
create a time series, a minimum of two relevant purchases are needed, but a greater num-
number(atleastfivepurchases)ispreferableforbetterresults.
ber (at least five purchases) is preferable for better results.
Sincetheresearchaimwastopredictdruggroupsthatwillbecontainedinthenext
Since the research aim was to predict drug groups that will be contained in the next
purchaseofacustomer,thetransactionswerethenaggregatedbydate/timetoincludeall
purchase of a customer, the transactions were then aggregated by date/time to include all
productsfromthesamepurchase. Theresultwasalistofallproductsinthepurchaseand
products from the same purchase. The result was a list of all products in the purchase and
theGPI(orapartialGPI),includingthedruggroupofeachproduct.
the GPI (or a partial GPI), including the drug group of each product.
Next,theGPIgroupandcategoryvectorswerederivedforthewholepurchase. The
Next, the GPI group and category vectors were derived for the whole purchase. The
resultingfeature,usedforprediction,wasamulti-hotencodedvectorwitheachelement
resulting feature, used for prediction, was a multi-hot encoded vector with each element
representingthepresenceofaspecificdruggroup/categoryinthepurchase. Thefinalstep
representing the presence of a specific drug group/category in the purchase. The final step
wastotransformallthisinformationintotimeseriesfortrainingandtestingLSTMneural
was to transform all this information into time series for training and testing LSTM neural
networks.
networks.
Therearethreedatasetsusedfortheexperiments. Eachdatasetcontainstransactions
There are three datasets used for the experiments. Each dataset contains transactions
forthesameperiod,butonlyforcustomersthathavemadeatleastaspecifiednumber
for the same period, but only for customers that have made at least a specified number of
of purchases during that period. The data set of 100+ purchases contains transactions
purchases during that period. The data set of 100+ purchases contains transactions from
fromcustomersthathavemadeatleast100purchasesduringthedefinedperiod. Analo-
customers that have made at least 100 purchases during the defined period. Analogously,
gously,the20+purchasesdatasetandthe5+purchasesdatasetcontainstransactionsfrom
the 20+ purchases dataset and the 5+ purchases dataset contains transactions from cus-
customersthathaveatleast20or5purchases,respectively,duringthedefinedperiod.
tomers that have at least 20 or 5 purchases, respectively, during the defined period.
3.3. TrainingNeuralNetworks
3.3. Training Neural Networks
Thetrainingprocesswasdoneseparatelyforseveraldifferenttypesofneuralnetwork
structTuhrees taranidniinngp uptr/oocuetsps uwtafesa dtuornees .sEepxparearitmelyen ftosrw seerveercaoln ddiuffcetreednwt tiythpense uorfa nlenuetrwalo nrkets-
iwmoprlke msternutcetudriens Payntdh oinnpuusti/noguttphuetK feeartausrleibs.r aErxyp[e3r4im]reunntns iwngeroen cotonpduocftTeedn wsoirthFl noweu[r3a5l ]n.et-
workSse vimerpallesmetesnotfedex ipne Priymtheonnts uwsienrge ptheer fKoremraesd liwbriathryd [i3ff4e]r erunntnseintugp osn. Etoacph osfe TteisnsdoerfiFnloewd
b[3y5a].f ewcharacteristics:
• TSheeveursaal gseetosf odf reuxgpegrriomuepnst(s1 w00erger opueprfso)romreddr uwgitcha tdeigffoerrieenst( 1se6tcuaptse.g Eoarciehs )s;et is defined
•by a Pferewd cichtainragctthereisntiecxst: purchase day and drug group/category together with a single
neuralnetworkorwithtwoseparateneuralnetworks;and
• Thedatasetused,wheredatasetsaredefinedbyaminimalnumberofrelevantpur-
chasesbyasinglecustomer.

Electronics 2023, 12, x FOR PEER REVIEW  7 of 16

•  The usage of drug groups (100 groups) or drug categories (16 categories);
Electronics2023,12,2616 7of14
•
Predicting the next purchase day and drug group/category together with a single
neural network or with two separate neural networks; and
•  The dataset used, where datasets are defined by a minimal number of relevant pur-
The first expericmhaesnets bseyt au psinfgolceu csuesdtomonern. eural networks, with both the GPI drug
group/category andThthe efinrsetx etxppuerricmheanset sdeatuypa sfoocuustepdu tonfe anteuurreasl .nFetowlloorwksi,n wgipthr ebvoitohu sthree -GPI drug
search[15–18],ingrnoeuxpt/cpautergchorays eadnday t’hsep rneedxitc ptiuornc,htahsee idnaityi aalse xopuetpriumt efenattsuuresse.d Fmolulolwtivinagr iaptreevious re-
timeseriescontasienainrcght [h1e5–n1u8m], ibne nreoxft dpauyrcshbaestew deaeyn’sc pornesdeiccutiotinv,e thpeu irncihtiaasl eesxpanerdimtheentms uuslteid-h moutltivariate
encoded vectortoimfe1 0s0eridersu cgongtraoinuinpgs tphree nseunmtbaesr ionf pduaytsa bnedtwweaens pcoenrsfoecrumtievde pounrcLhSaTseMs aanndd the multi-
SimpleRNN neuhroat lennceotdweodr vkesc,toi.re o.,f t1h0e0i rdriumgp glreomupesn ptarteisoennst aisn inKpeurta asn[d3 4w]a.sS poelrvfoinrmgeodf otnh eLSTM and
problemofthevSaimnipslheiRnNgNg rnaeduieranlt nisettwheorpkrsi, nic.ei.p, atlheaidr viamnptlaegmeeonftatthioenLs SiTnM Ke[r3a6s, 3[73]4,]w. Shoilcvhing of the
resultsintheabiplirtoybtloemst oofr ethloe nvga-ntiesrhmingd agtraaddieepnet nisd tehnec piersin[c3i8p,a3l9 a]d. vAacnctoargdei nofg tthoe tLhSisT,ML S[3T6M,37], which
betterrerseuslutsl tisn tihnee avbeilriyty mtoe sttroirce, laonndg-tSeirmmp dlaetRa NdeNpewndaesnecileims [i3n8a,3t9e]d. Afrcocomrdfiungrt thoe trhis, LSTM
produced
produced better results in every metric, and SimpleRNN was eliminated from further ex-
experiments.
periments.
ThesecondsetupwasdirectedatpredictingonlytheGPIdruggroup/categoryusing
The second setup was directed at predicting only the GPI drug group/category using
anLSTMneuralnetwork,whilethethirdsetupfocusedonpredictingonlythenextpurchase
an LSTM neural network, while the third setup focused on predicting only the next pur-
daywithaseparateLSTMneuralnetwork.
chase day with a separate LSTM neural network.
ThestructureoftheLSTMcellusedintheexperimentsisshowninFigure4. Eachcell
The structure of the LSTM cell used in the experiments is shown in Figure 4. Each
isessentiallyamemoryblockwiththreemultiplicativegates: theinputgate,theforgetgate
cell is essentially a memory block with three multiplicative gates: the input gate, the forget
andtheoutputgate. Thegatescontrolwhatpartofinput,cellstateoroutputwillbeused
gate and the output gate. The gates control what part of input, cell state or output will be
infurthercalculations,respectively,andwhatpartwillbediscarded. used in further calculations, respectively, and what part will be discarded.

Figure4.Structureofthelongshort-termmemorycell[40].
Figure 4. Structure of the long short-term memory cell [40].
FortheLSTMceFlolrs thhoew LnSTiMnF ciegllu srheo4w,nth ien fFoilgluorwe i4n,g theeq fuoalltoiowninsga peqpulyat[io4n0]s: apply [40]:
|             | i          | =  ( W     | x + W h       | + W c +b ),       |     |      |
| ----------- | ---------- | ----------- | ------------- | ----------------- | --- | ---- |
| i = σ(W     | x +W       | h +xiW      | c +t−1b       | )                 |     | (1)  |
| t           | xi t th    | i t− 1      | tc i t−h1i    | i ci t−1 i        | (1) |      |
| = σ(W       | +W f       | =  (W +    | x + W h       | + + W c +b ,      |     | (2)  |
| f t         | xf x t th  | f h t− 1 xf | Wt cf c t−hf1 | t −1b f cf t−1 f  | (2) |      |
|             | tacn h=(Wf | c ++i       | Wta n hh( W   | +x b+ )W h +b ),  |     |      |
| c = f c t−1 | +i         | x           | −1xc          |                   | (3) | (3)  |
| t t         | t t        | t xtc− 1t   | t h c t       | t c hc t−1 c      |     |      |
| o = σ(W     | x +W       | h           | +W c +b       | )                 | (4) |      |
| t           | xo t       | ho t−1      | co t          | o                 |     |      |
|             | h = o      | tanh(c      | )             |                   | (5) |      |
|             | t          | t           | t             |                   |     |      |

Intheequationsstatedabove,i,f,o,candxrepresenttheactivationvectorsforthe
inputgate,forgetgate,outputgate,andcellandcellinput,whereσisthesigmoidfunction,
histhehiddenvector, bthebiasesandW representstheweightmatrices. Eachweight
matrixitismarkedinsubscript,indicatingtowhichconnectionitapplies.

Electronics2023,12,2616 8of14
3.4. Evaluation
Theneuralnetworksfromthefirstsetupwereevaluatedseparatelysincetheycon-
tainedalloutputfeatures,whilethesecondandthethirdwereevaluatedtogetherbecause
eachofthemoutputsapartoftherequiredfeatures.
Inallsetups,theproblemwasposedasaregression,i.e.,basedonpreviousvaluesina
timeseries,theneuralnetworkpredictsthefollowingvalues. However,fortheevaluation
oftheseexperimentalresults,itwasnotpossibletoadequatelymeasuretheperformance
withregressionmetrics.Theoutputoftheneuralnetworkscontained,similarlyastheinput,
thenumberofdaysuntilthenextpurchaseandtheGPIdruggroup/categoryvectorfor
thenextpurchase. Forthenumberofdaysuntilthenextpurchase,itwaspossibletoapply
regressionmetricsorconverttoaclassificationproblem—istheregoingtobeapurchase
inthefollowing7days? FortheGPIdruggroup/categoryvector,eachelementhasthe
valueof0or1where0signifiesthatthisdruggroup/categorywillnotappearinthenext
purchase,while1signifiesthatitwill. Fortheevaluationofthesepredictions,itisbetter
tofocusonhowmanyofthedruggroup/categorypresentinthepurchasewerecorrectly
predicted. Sincethereare100druggroups(99plusanUnknownvalue)and16categories
(15 plus an unknown value) there are usually much more drug groups/categories that
will not be present in a purchase than those that will. Therefore, simply looking at the
numberofcorrectlypredictedvectorelementswillnotadequatelyrepresentthesituation
anditisnecessarytolookatpresentandmissingdruggroups/categoriesseparately. This
isequivalenttotransformingthisproblemtoaclassificationone—accuracy,precisionand
recallcanbemeasuredfortwoclasses: thedruggroup/categorythatwillappearinthe
followingpurchase(thecorrespondingvectorelementis1)andthedruggroup/category
thatwillnotappearinthefollowingpurchase(thecorrespondingvectorelementis0). This
approachissimilartotheoneproposedinpreviousresearchpredictingthenextpurchase
day [17,18]. The output of the neural network was the predicted number of days until
thenextrelevantpurchase,butpredictionsweredividedintwoclasses: “Apurchasewill
happeninthefollowing7days”and“Therewillbenopurchaseinthefollowing7days”.
Thisallowedfortheviewingoftheproblemintwowaysandapplyingbothtypesofmetrics
(i.e.,regressionandclassificationmetrics).
4. Results
Resultsforallexperimentsareshownusingaccuracy,precisionandrecall[41]. Ac-
curacypresentsaquotientofthesumofcorrectlyclassifiedinstancesofanyclassandthe
totalnumberofinstancesofallclasses. Precisionforacertainclassisthequotientofthe
numberofcorrectlyclassifiedinstancesofthatclassandallinstancesthatwereclassifiedas
thatclass. Recall,ontheotherhand,isthequotientofthenumberofcorrectlyclassified
instancesofaclassandthenumberofallinstancesthatbelongtothatclass.
Asmentionedintheprevioussection, theinitialsetofexperimentsperformedthe
predictionof100druggroupvectorandthenextpurchasedaywithamultivariateLSTM
neuralnetworkandamultivariateSimpleRNNneuralnetworkusingtheKeraslibrary
inPython. LSTMneuralnetworksproducedbetterresultsinallmeasuredmetricswith
themostobviousdifferencesinprecisionandrecallforthe“Realizedpurchases”category
in predicting the GPI drug group. For this reason, SimpleRNN neural networks were
eliminated from the following experiments. In order to demonstrate the differences in
resultswiththesetwotypesofneuralnetworks,Table1showstheresultsforthe100+pur-
chasesdataset.
ResultsofthefollowingexperimentsareshowninFigures5–7. Eachfigureshows
the results for one of the datasets and consists of two charts: one represents the metric
valuesforthepredictionofdruggroups/categoriesandtheothershowstheresultsforthe
predictionofthenextpurchaseday. Thevaluesformetricsarecalculatedseparatelyforthe
predictionofdruggroups/categoriesandthepredictionofthenextpurchaseday. Different
neural networks are represented with different colours and denoted with abbreviated
namesasfollows. AsinglemultivariateLSTMneuralnetworkforsimultaneousprediction

Electronics 2023, 12, x FOR PEER REVIEW 9 of 16
eliminated from the following experiments. In order to demonstrate the differences in re-
sults with these two types of neural networks, Table 1 shows the results for the 100+ pur-
chases dataset.
Table 1. The 100+ purchases dataset—prediction of the GPI drug groups/categories and the next
purchase day with multivariate LSTM and multivariate SimpleRNN neural networks. Better perfor-
mance is marked with bold lettering for each metric.
Electronics2023,12,2616 9of14
GPI Drug Groups Next Day
Realized Unrealized Realized Unrealized
Accuracy Purchases Purchases Accuracy Purchases Purchases
of the druPgreccaistieogno rRyecvaellc toPrre(c1is6iodnr uRgeccaaltle gories) andPrneecixstiopnu rRcehcaaslle Pdraeycisiisond enRoetceadll as
Multivariate LSTM S9M7.L27S%T M1962..3T4h%e co62m.3b3i%n ati9o7n.50o%f am99u.l6t5i%va ria9t5e.1L6S%T M9n9e.8u6r%al n9e3t.w02o%r kf8o7r.0t0h%e pr9e9d.7ic1t%io n
Multivariate SimpleRNN o9f6t.h03e%d rug8c4a.4t7e%go ry46v.0e2c%to r9(61.644d%r ug9c9a.4te3g%o rie9s4).4a2n%d ap9s9e.2u8d%o -m92u.4l8ti%v ari8a6t.0e0L%S TM98n.5e0u%r al
network for prediction of the next purchase day is denoted as MLSTM + PMLSTM 16.
AsingRleesmulutsl toifv tahreia ftoellLoSwTiMng nexeuperarilmneentwtso arrke fsohrotwhne isnim Fiuglutarense 5o–u7s. pEraecdhi fictgiounreo sfhtohwesd trhueg
grreosuupltsv feocrt oorne(1 o0f0 thder udgatgarsoeutsp asn)da ncodntshisetsn oefx ttwpou rcchhaarstse: donaye riespdreenseonttesd thaes mSMetLriScT vMalu1e0s0 .
Ffionra tlhlye, tphreedcoicmtiobnin oaft idornuogf garomuuplst/icvaatreigaoteriLesS TanMd ntheue roatlhneer tswhoorwksf othret hreespurletsd fioctri othneo pfrteh-e
ddriucgtiognr oouf pthvee ncteoxrt (p1u0r0chdarsueg dgaryo. uTphse) vaanldueas pfosre umdeot-rmicsu altriev acrailactuelaLteSdT Msepnaeruarteallyn feotrw tohrek
foprretdhiectpiorend oicf tdiorungo gfrtohuepnse/cxattpeguorcriheass aendda tyheis pdreendoictteidona sofM thLeS nTeMxt +puPrMchLaSsTe Mda1y0. 0D.iIffnera-ll
thenetc nheaurrtas,l tnheetwcloarskss “aRree arelipzreedsePnutercdh wasitehs ”diiffselarebnetl lceodloausrRs aPn,dw dheilneottheed cwlaitshs a“bUbnrerevaialitzeedd
pnuarmcheass aess ”foilslolawbse.l Ale dsinagslUe Pm.ultivariate LSTM neural network for simultaneous prediction
of the drug category vector (16 drug categories) and next purchase day is denoted as
TSaMbleLS1.TTMhe 1160.0 T+hpeu crcohmasbeisndaatitoasne to—f par meduiclttiiovnaroifatthee LGSPTIMdr ungeugrroaul pnse/tcwatoergko rfioers athned pthreedneicxttiopunr -
cohaf stehdea dyrwuigth cmatuegltoivrayr ivateecLtoSrT M(16a nddrumgu cltaivteagrioatreieSsi)m apnledR aN pNsneueudroa-lmneutwltiovrakrsi.aBteet tLeSrTpeMrf onremuarnacle
isnmetawrkoerdk wfoirth pbroelddicletitotenri nogf tfhore enaecxhtm peutrrcich.ase day is denoted as MLSTM + PMLSTM 16. A
single multivariate LSTM neural network for the simultaneous prediction of the drug
group veGctPoIrD (ru1g0G0 rdourpusg groups) and the next purchase day isN edxteDnaoyted as SMLSTM 100.
Finally, tRheea lcizoemd bination ofU anr emaluizletdivariate LSTM neural neRtewaloizrekd for the predUicntreioalniz eodf the
Accuracydrug gro P u u p rc h v a e se c s tor (100 drug Pu g rc r h o as u e p s s) and aA pccsueruacdyo-multiv P a u r r i c a h t a e se L s STM neural P n u e rc t h w as o e r s k for
Precision Recall Precision Recall Precision Recall Precision Recall
the prediction of the next purchase day is denoted as MLSTM + PMLSTM 100. In all the
MultivariateLSTM 97.27% 92.34% 62.33% 97.50% 99.65% 95.16% 99.86% 93.02% 87.00% 99.71%
charts, the class “Realized Purchases” is labelled as RP, while the class “Unrealized pur-
MultivariateSimpleRNN 96.03% 84.47% 46.02% 96.44% 99.43% 94.42% 99.28% 92.48% 86.00% 98.50%
chases” is labelled as UP.
(a) (b)
Electronics 2023, 12, x FOR PEER REVFIEiWgu re 5. Prediction results for the 100+ purchases dataset: (a) results for the prediction 1o0f odfr u16g
Figure5. Predictionresultsforthe100+purchasesdataset: (a)resultsforthepredictionofdrug
groups/categories; and (b) results for the prediction of the next purchase day.
groups/categories;and(b)resultsforthepredictionofthenextpurchaseday.
(a) (b)
Figure 6. Prediction results for the 20+ purchases dataset: (a) results for the prediction of drug
Figure 6. Prediction results for the 20+ purchases dataset: (a) results for the prediction of drug
groups/categories; and (b) results for the prediction of the next purchase day.
groups/categories;and(b)resultsforthepredictionofthenextpurchaseday.

Electronics 2023, 12, x FOR PEER REVIEW 11 of 16
Electronics2023,12,2616 10of14
(a) (b)
Figure 7. Prediction results for the 5+ purchases dataset: (a) results for the prediction of drug
Figure 7. Prediction results for the 5+ purchases dataset: (a) results for the prediction of drug
groups/categories; and (b) results for the prediction of the next purchase day.
groups/categories;and(b)resultsforthepredictionofthenextpurchaseday.
It is clear at first sight that the drug group/category vector prediction for the follow-
Itisclearatfirstsightthatthedruggroup/categoryvectorpredictionforthefollowing
ing purchase produces significantly better results when using a dedicated neural network
purchase produces significantly better results when using a dedicated neural network
for all datasets and using both drug groups and drug categories. The most noticeable im-
for all datasets and using both drug groups and drug categories. The most noticeable
provement can be seen for the recall in the “Realized purchases” class, which increased
improvementcanbeseenfortherecallinthe“Realizedpurchases”class,whichincreased
by 15–50%. In this case, recall is the quotient of the number of drug groups/categories that
by15–50%. Inthiscase, recallisthequotientofthenumberofdruggroups/categories
wthearte wceorrereccotlryre pctrleydpicrteeddi cttoe datpopaeparp einar tihnet hneexnte xptuprcuhrachsea saenadn dthteh enunmumbebre roof faalll lddrruugg
ggrroouuppss//ccaateteggoorrieiess ththaat taappppeeaarreedd inin ththee nneexxt tppuurrcchhaassee((ss)). .AAdddditiitoionnaalllyly,, tthhee iinnccrreeaassee ffoorr tthhee
““RReeaalliizzeedd ppuurrcchhaasseess”” ccllaassss’’ss rreeccaallll iiss aallwwaayyss ggrreeaatteerr wwhheenn uussiinngg aallll 110000 ddrruugg ggrroouuppss..
FFoorr tthhee pprreeddiiccttiioonn ooff tthheen neexxttp puurcrhchaasesed daya,yt,h tehsei tsuitautiaotnioins eisx aecxtalycttlhy ethoep poopspitoes.itEex. cEexp-t
cseopmt esommineo mrvinaorira vtiaorniastiinonths ein1 0t0h+e p10u0r+ch pausercshdaasteass edta,taalmseot,s atlamllomste tarlilc mssehtoriwcs bsehtotewr rbeesttueltrs
rweshuelntsa wsihnegnl ean seinugralel nneetuwroalr kneptewrfoorrkm psesrifmorumltsa nsiemouusltpanreedoiucsti opnreodficthtieonp uorfc thhaes epudracyhaansed
dthaey GanPdI dthrue gGgPrIo durpu/gc gatreoguopr/yc.ategory.
IIff oonnllyy tthhee ddrruugg ggrroouuppss//ccaateteggoorireiess ththaat taarree pprreesseenntt iinn tthhee ffoolllloowwiinngg ppuurrcchhaasseess aarree
ttaakkeenn iinnttoo aaccccoouunntt,, tthhee nnuummbbeerr ooff ccoorrrreeccttllyy oorr iinnccoorrrreeccttllyy pprreeddiicctteedd ppuurrcchhaasseedd ddrruugg
ggrroouuppss//cactaetgegoroireise scacna nbeb aenaalnyasleyds.e Tdh.eT rheseurletss uarltes raelraetirveelalyti sviemlyilasri mfoirl aerxpfoerriemxepnetrsi museinntgs
tuhsei ndgruthge gdrrouugpgsr oaunpds eaxnpdeerixmpeernitms eunstisnugs idnrgudgr ucagtecgatoergieosr.i eFso.rF othreth seaskaek eofo fclceleaarerer rvviissuuaall
rreepprreesseennttaattiioonn,, tthhee ddaattaa pplolotttteeddi sisf rforomme xepxepreirmimenetnstws withithd rdurgucga tceagtoegrioersiebse cbaeucsaeutshee trheearree
aornel yon1l6y o1f6t hofe mth,ecmo,m cpoamrepdarteod1 t0o0 1d0r0u dgrgurgo ugprosu.ps.
FFiigguurree 88 sshhoowwss tthhee mmiinniimmuummn nuummbbeerro offc ocorrrercetcltylyp prerdeidcitcetdedp uprucrhcahsaesdeddr durgucga tceagteogrioe-s
rbieysp beyr cpeenrtcaegnetafogre tfhoer 1t0h0e+ 1p00u+r cphuarscehsadsaetsa dseattaasnedt adnedd icdaetdeidcaLtSedT MLSnTeMur nalenueratwl noertkw. Torhkis.
Tmheisa nmsetahnast tthhaet etxhpe eerximpeernimtsewntesr ewceoren dcouncdteudctuesdi nugsianng LaSnT LMSTnMeu nreaulrnaelt nweotwrkotrrka itnraeidneodn
othne th10e 01+00p+u rpcuhracsheassdesa tdaasetatsweth werheetrhee tohnel yonoluyt opuuttpiustt hise tdhreu dgrcuagte cgaotreigeosrvieesc tvoer.ctAofrt. eArfpteerr -
pfoerrmfoirnmginthge tehxep eexripmeerinmtse,nthtse, nthuem nbuemrobfecro orfr eccotlryrepcrtelyd ipctreeddidctreudg dcartuegg ocraiteesgworaisesc awlcausl actaeld-
cfuolraeteadch focru esatocmh ecursttaokminegr itnaktoinagc cinotuon atcocnoluyntth oonsley tthhaotsaec tthuaatl layctaupaplleya rapinpetahre ifno ltlhoew fionlg-
lpouwricnhga speu.rItchwaasse.t hIte nwpaso stshiebnle ptoosdseibteler mtoi ndeettheermpienrcee tnhtea gpeerocfetnottaaglecu osft otomtaelr scufosrtowmheicrsh ftohre
wfohlliochw tihneg fooclclouwrriendg: oactcluearrsetdo:n aet pleuarscth oansee dpucarctehgaosreyd wcaatsegcoorryre wctalys cporrerdeiccttleyd p,raetdleicatsetdt,w aot
lceaatsetg towrioe scawteegroercioesrr wecetrlye cporrerdeiccttleyd p,reetcd.icFtoerd9, 5e.t7c%. Foofr c9u5s.7to%m oefr csu,asttolmeaesrtso, naet lceaatsetg oonrye cthata-t
ewgaosryp uthracht awsaesd pinurtchheafsoeldlo iwn itnhge pfoulrlochwaisnegw pausrcchorarseec wtlyasp croedrriecctetldy. pArtedleiacstetdtw. Aotc laetaesgt otrwieos
werecorrectlypredictedfor82.91%ofcustomers,atleastthreefor67.18%ofcustomersand
categories were correctly predicted for 82.91% of customers, at least three for 67.18% of
for51.19%ofcustomersatleastfourcategorieswerecorrectlypredicted.
customers and for 51.19% of customers at least four categories were correctly predicted.
The other way of looking at the experimental results is by viewing the number of
incorrectlypredictedcategories,againonlyconsideringcategoriesthatarepresentinthe
nextpurchase. Byusingananalogousprocessasdescribedabove,thepercentageoftotal
customerswasdeterminedforwhichthefollowingoccurred: nomorethanonecategory
wasincorrectlypredicted,nomorethantwocategorieswereincorrectlypredicted,etc.After
examiningthenumbers,itwasevidentthattherewerenevermorethanfiveincorrectly
predictedcategoriesoutofthosethatwerepresentinthefollowingpurchases. Thechart
showing the maximum number of incorrectly predicted purchased drug categories by

Electronics2023,12,2616 11of14
percentageforthe100+purchasesdatasetanddedicatedLSTMneuralnetworkisshownin
Figure9. Nomorethanonecategorywasincorrectlypredictedfor81.17%ofcustomers,no
Electronics 2023, 12, x FOR PEER REVIEW 12 of 16
morethantwofor93.6%ofcustomers,nomorethanthreefor98.26%ofcustomersandno
morethanfourfor99.63%ofcustomers.
Electronics 2023, 12, x FOR PEER REVIEW 13 of 16
FFiigguurree 88.. MMiinniimmuumm nnuummbbeerr ooff ccoorrrreeccttllyy pprreeddiicctteedd ppuurrcchhaasseedd ddrruugg ccaatteeggoorriieess bbyy ppeerrcceennttaaggee ffoorr tthhee
110000++ ddaattaasseett aanndd ddeeddiiccaatteedd LLSSTTMM nneeuurraall nneettwwoorrkk..
The other way of looking at the experimental results is by viewing the number of
incorrectly predicted categories, again only considering categories that are present in the
next purchase. By using an analogous process as described above, the percentage of total
customers was determined for which the following occurred: no more than one category
was incorrectly predicted, no more than two categories were incorrectly predicted, etc.
After examining the numbers, it was evident that there were never more than five incor-
rectly predicted categories out of those that were present in the following purchases. The
chart showing the maximum number of incorrectly predicted purchased drug categories
by percentage for the 100+ purchases dataset and dedicated LSTM neural network is
shown in Figure 9. No more than one category was incorrectly predicted for 81.17% of
customers, no more than two for 93.6% of customers, no more than three for 98.26% of
customers and no more than four for 99.63%. of customers.
FigurFei g9u. Mrea9x.iMmuaxmim nuummbneur mofb ienrcoofrriencctolyrr pecrteldyicptreedd picutercdhpauserdch darsuegd cdartueggocraiteesg boyr ipeserbcyenpteargcee nfotra gefor
the 10th0e+ 1p0u0r+chpausrecsh daasetassdeta taansdet daenddicdaeteddic LatSeTdML SnTeMuranle nuertawlnoerktw. ork.
For iFllourstirllautisotrna ptiuonrppouserps,o tshees ,sttrhuecstturruec otuf rae noefuaranle nuertawlnoerktw porrekdipcrteiodnic itsi ogniviesng biveelonwb.e low.
The Tphreedpicrteidonic trieopnreresepnretesden hteedre hies raeni seaxnamexpalem opfl eano foauntpouut tfpruotmf rao msinagslein mglueltmivualrtiiavtaer iate
LSTMLS TneMurnaelu nraeltwneotrwk ofrokr ftohret hseimsiumltualntaenoeuosu psrperdeidcitciotino noof fththee ddrruugg ccaatteeggoorryy vveeccttoorr (1(166d rug
drugc acateteggoorireies)s)a annddn nexexttp puurcrhchasaesed dayay::
1 0 10 01 01 11 10 10 01 00 10 00 01 00 11 01 13.1453 .45
The first 16 values represent a multi-hot drug category vector in which 0 denotes that
Thefirst16valuesrepresentamulti-hotdrugcategoryvectorinwhich0denotesthat
the appropriate drug category is not expected in the following purchase, while 1 denotes
theappropriatedrugcategoryisnotexpectedinthefollowingpurchase,while1denotes
that the drug category is expected in the next purchase. The final value represents the
estimated number of days until the following purchase by the specified customer.
5. Discussion
In all experiments with the prediction of the drug groups/categories that will appear
in the following purchase, the metrics were higher when using drug groups instead of
drug categories. This leads to the conclusion that transforming the data to generate the
vector of drug categories is unnecessary since it is an additional step that does not produce
better results. The reason for this is probably the fact that original data contain more de-
tails (more specific groups versus more general categories) allowing for more precise pre-
dictions.
In the case of next purchase day prediction, the added information about the content
of the purchase helped produce more accurate predictions than relying solely on the num-
ber of days between consecutive purchases. As for using the drug group or drug category
vector, there was a slight difference in favour of using all 100 drug groups. This difference
was not very significant, but since the drug categories were derived from the drug groups,
it was only logical to use the original form of the data in prediction.
If the results for different experiment setups are compared across datasets, there were
no significant variations in accuracy, i.e., very good results can be achieved even with a
small number of purchases per customer. The biggest difference can be noticed in recall
for the “Realized purchases” category in both the drug group/category and next purchase
day prediction, which significantly increased in datasets with a greater number of pur-
chases per customer. The conclusion that can be derived is that when there is more histor-
ical information (a greater number of purchases), a greater percent of the actual future
purchases will be correctly predicted.

Electronics2023,12,2616 12of14
that the drug category is expected in the next purchase. The final value represents the
estimatednumberofdaysuntilthefollowingpurchasebythespecifiedcustomer.
5. Discussion
Inallexperimentswiththepredictionofthedruggroups/categoriesthatwillappear
inthefollowingpurchase,themetricswerehigherwhenusingdruggroupsinsteadofdrug
categories. Thisleadstotheconclusionthattransformingthedatatogeneratethevectorof
drugcategoriesisunnecessarysinceitisanadditionalstepthatdoesnotproducebetter
results. Thereasonforthisisprobablythefactthatoriginaldatacontainmoredetails(more
specificgroupsversusmoregeneralcategories)allowingformoreprecisepredictions.
Inthecaseofnextpurchasedayprediction,theaddedinformationaboutthecontentof
thepurchasehelpedproducemoreaccuratepredictionsthanrelyingsolelyonthenumber
of days between consecutive purchases. As for using the drug group or drug category
vector,therewasaslightdifferenceinfavourofusingall100druggroups. Thisdifference
wasnotverysignificant,butsincethedrugcategorieswerederivedfromthedruggroups,
itwasonlylogicaltousetheoriginalformofthedatainprediction.
If the results for different experiment setups are compared across datasets, there
were no significant variations in accuracy, i.e., very good results can be achieved even
withasmallnumberofpurchasespercustomer. Thebiggestdifferencecanbenoticedin
recallforthe“Realizedpurchases”categoryinboththedruggroup/categoryandnext
purchasedayprediction,whichsignificantlyincreasedindatasetswithagreaternumber
ofpurchasespercustomer. Theconclusionthatcanbederivedisthatwhenthereismore
historicalinformation(agreaternumberofpurchases),agreaterpercentoftheactualfuture
purchaseswillbecorrectlypredicted.
6. Conclusions
Inthispaper,researchinthefieldofpurchasepredictionbasedonhistoricalcustomer
transactionsispresented. Theoriginaldatafromthemedicalsupplycompanywaspre-
processedandtransformedtocreateatimeseriesappropriateasinputforaneuralnetwork.
Due to the medical nature of the data, part of the GPI was used to determine product
categoryinformationinitsoriginalformandashortenedversiondevisedbygrouping
similarcategories. Multipleneuralnetworksforthepredictionofthenextpurchaseday,
GPIdruggroups/categoriesandallfeaturestogetherweretrained. Thetrainednetworks
were evaluated with multiple datasets, differing on the minimal number of purchases
per customer. The results show that the drug groups/categories for the next purchase
canbepredictedwithahigheraccuracywhenusinganLSTMneuralnetworkdedicated
solelytopredictingthisoutputfeature. However,forpredictingthenextpurchaseday,itis
preferabletouseasingleLSTMneuralnetworkthatpredictsalloutputfeatures. Itcanbe
concludedthatacombinedapproachshouldgivethebestresultsifthegoalistoachieve
superioraccuracyforalloutputfeatures.
OnepracticallimitationoftheproposedapproachistheusageoftheGPIfordefining
productcategories. Sincethistherapeuticclassificationsystemisusedforidentifyingdrug
products,itlimitstheapplicationofthisapproachtothefieldofmedicaldrugs. However,
this novel approach can be applied to any domain which uses a classification system,
whetherhierarchicalornon-hierarchical.
Infurtherresearch, itwouldbeinterestingtouseagreaternumberofhierarchical
groups of the GPI which would enable focusing on more specific classification of the
productinquestion.
AuthorContributions: Conceptualization, B.P.andM.C´.; methodology, M.C´.andB.P.; software,
M.C´.;validation,B.P.,D.S.andI.C´.;datacuration,B.P.;writing—originaldraftpreparation,M.C´.;
writing—reviewandediting,B.P.,D.S.andI.C´.Allfiguresandtablesaretheauthors’contributions,
except those explicitly cited. All authors have read and agreed to the published version of the
manuscript.

Electronics2023,12,2616 13of14
Funding:Thisresearchreceivednoexternalfunding.
DataAvailabilityStatement:Restrictionsapplytotheavailabilityofthesedata.Datawereobtained
fromamedicaldeviceanddrugcompanyand,duetoconfidentialityissues,arenotpubliclyavailable.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.
References
1. Zhang,X.;Liang,X.;Zhiyuli,A.;Zhang,S.;Xu,R.;Wu,B.AT-LSTM:AnAttention-basedLSTMModelforFinancialTimeSeries
Prediction.IOPConf.Ser.Mater.Sci.Eng.2019,569,052037.[CrossRef]
2. Althelaya,K.A.;El-Alfy,E.-S.M.;Mohammed,S.EvaluationofbidirectionalLSTMforshort-andlong-termstockmarketprediction.
InProceedingsofthe20189thInternationalConferenceonInformationandCommunicationSystems(ICICS),Irbid,Jordan,
3–5April2018;pp.151–156.[CrossRef]
3. Kim,S.;Kang,M.FinancialseriespredictionusingAttentionLSTM.arXiv2019,arXiv:1902.10877.
4. Giles,C.L.;Lawrence,S.;Tsoi,A.C.NoisyTimeSeriesPredictionusingRecurrentNeuralNetworksandGrammaticalInference.
Mach.Learn.2001,44,161–183.[CrossRef]
5. Wei,H.;Zeng,Q.ResearchonsalesForecastbasedonXGBoost-LSTMalgorithmModel.J.Phys.Conf.Ser.2021,1754,012191.
[CrossRef]
6. Esnafi,Y.;Amin,S.H.;Zhang,G.;Shah,B.Time-seriesforecastingofseasonalitemsusingmachinelearning—Acomparative
analysis.Int.J.Inf.Manag.DataInsights2022,2,100058.
7. Pavlyshenko,B.M.Machine-LearningModelsforSalesTimeSeriesForecasting.Data2019,4,15.[CrossRef]
8. Wang,P.;Zhang,Y.;Niu,S.;Guo,J.ModelingTemporalDynamicsofUsers’PurchaseBehaviorsforNextBasketPrediction.
J.Comput.Sci.Technol.2019,34,1230–1240.[CrossRef]
9. Stanimirovic´, A.; C´iric´, M.; Džonic´, B.; Stoimenov, L.; Petrovic´, N. Sistem za davanje preporuka baziran na tehnologijama
semanticˇkogweb-a(Recommendersystembasedonsemanticwebtechnologies).Proc.YUINFO2012,2012,147–152.
10. Gruenen,J.;Bode,C.;Hoehle,H.PredictiveProcurementInsights:B2BBusinessNetworkContributiontoPredictiveInsightsinthe
ProcurementProcessFollowingaDesignScienceResearchApproach.InProceedingsoftheDesigningtheDigitalTransformation:
12thInternationalConference,DESRIST2017,Karlsruhe,Germany,30May–1June2017;Volume10243,pp.267–281.[CrossRef]
11. DeGooijer,J.G.;Hyndman,R.J.25yearsoftimeseriesforecasting.Int.J.Forecast.2006,22,443–473.[CrossRef]
12. Fu,R.;Zhang,Z.;Li,L.UsingLSTMandGRUneuralnetworkmethodsfortrafficflowprediction.InProceedingsofthe31st
YouthAcademicAnnualConferenceofChineseAssociationofAutomation(YAC2016),Wuhan,China,11–13November2016;
Volume7804912,pp.324–328.[CrossRef]
13. Verma,A.ConsumerBehaviourinRetail:NextLogicalPurchaseusingDeepNeuralNetwork.arXiv2010,arXiv:2010.06952.
14. McNally,S.;Roche,J.;Caton,S.PredictingthePriceofBitcoinUsingMachineLearning.InProceedingsofthe201826thEuromicro
InternationalConferenceonParallel,DistributedandNetwork-BasedProcessing(PDP),Cambridge,UK,21–23March2018;
pp.339–343.
15. Stojcˇic´,A.;Radosavljevic´,N.;Predic´,B.;Kovacˇevic´,M.;Roganovic´,M.Analizavremenskihserija:Metodepredvid¯anjabuduc´e
potražnjeuveleprodaji(TimeSeriesAnalysis: MethodsforFutureDemandForecastinginB2BSales). InProceedingsofthe
ZbornikRadova—63.KonferencijazaElektroniku,Telekomunikacije,Racˇunarstvo,AutomatikuiNuklearnuTehniku,Srebrno
jezero,Serbia,3–6June2019;pp.923–928.
16. Predic´,B.;Radosavljevic´,N.;Stojcˇic´,A.Timeseriesanalysis: Forecastingsalesperiodsinwholesalesystems. FactaUniv. Ser.
Autom.Control.Robot.2020,18,177–188.[CrossRef]
17. C´iric´,M.;Predic´,B.PredictingPurchaseDayinB2B:FromStatisticalMethodstowardsLSTMNeuralNetworks.InProceedings
ofthe10thInternationalConferenceonInformationSocietyandTechnology,Kopaonik,Serbia,8–11March2020;pp.193–197,
ISBN978-86-85525-24-7.
18. C´iric´,M.;Predic´,B.Pseudo-multivariatelstmneuralnetworkapproachforpurchasedaypredictioninb2b.FactaUniv.Ser.Autom.
Control.Robot.2021,19,151–162.[CrossRef]
19. Korpusik,M.;Sakaki,S.;Chen,F.;Chen,Y.Y.RecurrentNeuralNetworksforCustomerPurchasePredictiononTwitter.CBREcsys@
recsys2016,1673,47–50.
20. duPreez,J.;Witt,S.F.Univariateversusmultivariatetimeseriesforecasting:Anapplicationtointernationaltourismdemand.Int.
J.Forecast.2003,19,435–451.[CrossRef]
21. Huang,C.;Wu,X.;Zhang,X.;Zhang,C.;Zhao,J.;Yin,D.;Chawla,N.V.OnlinePurchasePredictionviaMulti-ScaleModelingof
BehaviorDynamics.InProceedingsofthe25thACMSIGKDDinternationalconferenceonknowledgediscovery&datamining,
Anchorage,AK,USA,4–8August2019.[CrossRef]
22. Martínez,A.;Schmuck,C.;Pereverzyev,S.;Pirker,C.;Haltmeier,M.Amachinelearningframeworkforcustomerpurchase
predictioninthenon-contractualsetting.Eur.J.Oper.Res.2018,281,588–596.[CrossRef]
23. Cirqueira,D.; Helfert,M.; Bezbradica,M.TowardsPreprocessingGuidelinesforNeuralNetworkEmbeddingofCustomer
BehaviorinDigitalRetail.InProceedingsofthe20193rdInternationalSymposiumonComputerScienceandIntelligentControl,
Amsterdam,TheNetherlands,25–27September2019.[CrossRef]

Electronics2023,12,2616 14of14
24. Stubseid,S.;Arandjelovic,O.MachineLearningBasedPredictionofConsumerPurchasingDecisions: TheEvidenceandIts
Significance.InProceedingsoftheAIandMarketingScienceworkshopatAAAI-2018,NewOrleans,LA,USA,2February2018;
pp.100–106,ISBN978-1-57735-801-5.
25. Suchacka,G.;Stemplewski,S.ApplicationofNeuralNetworktoPredictPurchasesinOnlineStore.InProceedingsofthe37th
InternationalConferenceonInformationSystemsArchitectureandTechnology–ISAT2016–PartIV,Karpacz, Poland, 18–20
September2016;SpringerInternationalPublishing:Cham,Switzerland,2017;Volume524,pp.221–231,ISBN978-3-319-46583-8.
26. Chai,Y.;Liu,G.;Chen,Z.;Li,F.;Li,Y.;Effah,E.A.ATemporalCollaborativeFilteringAlgorithmBasedonPurchaseCycle.In
ProceedingsoftheCloudComputingandSecurity:4thInternationalConference,ICCCS2018,Haikou,China,8–10June2018;
RevisedSelectedPapers,PartII.SpringerInternationalPublishing:Cham,Switzerland,2018;pp.191–201.[CrossRef]
27. Jacobs, B.J.; Donkers, B.; Fok, D. Model-Based Purchase Predictions for Large Assortments. Mark. Sci. 2016, 35, 389–404.
[CrossRef]
28. Kooti,F.;Lerman,K.;Aiello,L.M.;Grbovic,M.;Djuric,N.;Radosavljevic,V.PortraitofanOnlineShopper:Understandingand
predictingconsumerbehavior.InProceedingsoftheNinthACMInternationalConferenceonWebSearchandDataMining,San
Francisco,CA,USA,22–25February2016.[CrossRef]
29. Goel,S.;Bajpai,R.ImpactofUncertaintyintheInputVariablesandModelParametersonPredictionsofaLongShortTerm
Memory(LSTM)BasedSalesForecastingModel.Mach.Learn.Knowl.Extr.2020,2,256–270.[CrossRef]
30. Luo,T.;Chang,D.;Xu,Z.ResearchonApparelRetailSalesForecastingBasedonxDeepFM-LSTMCombinedForecastingModel.
Information2022,13,497.[CrossRef]
31. Yoo,T.-W.;Oh,I.-S.TimeSeriesForecastingofAgriculturalProducts’SalesVolumesBasedonSeasonalLongShort-TermMemory.
Appl.Sci.2020,10,8169.[CrossRef]
32. McKinney,W.Datastructuresforstatisticalcomputinginpython.InProceedingsofthe9thPythoninScienceConference,Austin,
TX,USA,28June–3July2010;Volume445,pp.51–56.
33. Availableonline:http://wolterskluwer.com/en/solutions/medi-span/about/gpi(accessedon6August2022).
34. Keras.Availableonline:https://keras.io(accessedon8January2020).
35. Abadi,M.;Barham,P.;Chen,J.;Chen,Z.;Davis,A.;Dean,J.;Devin,M.;Ghemawat,S.;Irving,G.;Isard,M.;etal.Tensorflow:
Asystemforlarge-scalemachinelearning.InProceedingsofthe12thUSENIXSymposiumonOperatingSystemsDesignand
Implementation(OSDI’16),Savannah,GA,USA,2–4November2016;pp.265–283.
36. Gers, F.A.; Schmidhuber, J.; Cummins, F. Learning to forget: Continual prediction with LSTM. In Proceedings of the 9th
InternationalConferenceonArtificialNeuralNetworks:ICANN’99;InstitutionofEngineeringandTechnology(IET),Edinburgh,
UK,7–10September1999;pp.850–855.
37. Gers,F.LongShort-TermMemoryinRecurrentNeuralNetworks. Ph.D.Thesis,EcolePolytechniqueFederaledeLausanne,
Lausanne,Switzerland,2001.
38. Hochreiter,S.TheVanishingGradientProblemDuringLearningRecurrentNeuralNetsandProblemSolutions.Int.J.Uncertain.
FuzzinessKnowl.BasedSyst.1998,6,107–116.[CrossRef]
39. Hochreiter,S.;Schmidhuber,J.Longshort-termmemory.NeuralComput.1997,9,1735–1780.[CrossRef][PubMed]
40. Graves,A.GeneratingSequencesWithRecurrentNeuralNetworks.arXiv2014,arXiv:1308.0850.
41. Lever,J.;Krzywinski,M.;Altman,N.ClassificationEvaluation.Nat.Methods2016,13,541–542.[CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.