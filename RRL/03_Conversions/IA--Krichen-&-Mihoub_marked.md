AI
Review
Long Short-Term Memory Networks: A Comprehensive Survey
MoezKrichen1,2,∗ andAlaeddineMihoub3,∗
1 DepartmentofSoftwareEngineering,FacultyofComputingandInformation,AlbahaUniversity,
P.O.Box7738,AlBaha65779,SaudiArabia
2 ReDCADResearchLaboratory,SfaxUniversity,Sfax3029,Tunisia
3 DepartmentofManagementInformationSystems,CollegeofBusinessandEconomics,QassimUniversity,
P.O.Box6666,Buraydah51452,SaudiArabia
* Correspondence:m.krichen@redcad.org(M.K.);a.mihoub@qu.edu.sa(A.M.)
Abstract
LongShort-TermMemory(LSTM)networkshaverevolutionizedthefieldofdeeplearning,
particularlyinapplicationsthatrequirethemodelingofsequentialdata. Originallyde-
signedtoovercomethelimitationsoftraditionalrecurrentneuralnetworks(RNNs),LSTMs
effectivelycapturelong-rangedependenciesinsequences,makingthemsuitableforawide
arrayoftasks. ThissurveyaimstoprovideacomprehensiveoverviewofLSTMarchitec-
tures,detailingtheiruniquecomponents,suchascellstatesandgatingmechanisms,which
facilitatetheretentionandmodulationofinformationovertime. Wedelveintothevarious
applicationsofLSTMsacrossmultipledomains,includingthefollowing: naturallanguage
processing(NLP),wheretheyareemployedforlanguagemodeling,machinetranslation,
andsentimentanalysis;timeseriesanalysis,wheretheyplayacriticalroleinforecasting
tasks;andspeechrecognition,significantlyenhancingtheaccuracyofautomatedsystems.
By examining these applications, we illustrate the versatility and robustness of LSTMs
inhandlingcomplexdatatypes. Additionally, weexploreseveralnotablevariantsand
improvementsofthestandardLSTMarchitecture,suchasBidirectionalLSTMs,whichen-
hancecontextunderstanding,andStackedLSTMs,whichincreasemodelcapacity. Wealso
discusstheintegrationofAttentionMechanismswithLSTMs,whichhavefurtheradvanced
theirperformanceinvarioustasks. Despitetheirstrengths,LSTMsfaceseveralchallenges,
includinghighComputationalComplexity,extensiveDataRequirements,anddifficulties
intraining,whichcanhindertheirpracticalimplementation. Thissurveyaddressesthese
limitationsandprovidesinsightsintoongoingresearchaimedatmitigatingtheseissues. In
AcademicEditor:SufiFahim
conclusion,wehighlightrecentadvancesinLSTMresearchandproposepotentialfuture
Received:25June2025 directionsthatcouldleadtoenhancedperformanceandbroaderapplicabilityofLSTM
Revised:31August2025
networks. Thissurveyservesasafoundationalresourceforresearchersandpractitioners
Accepted:1September2025
seekingtounderstandthecurrentlandscapeofLSTMtechnologyanditsfuturetrajectory.
Published:5September2025
Citation: Krichen,M.;Mihoub,A.
Keywords: LSTM;LongShort-TermMemory;deeplearning;sequencemodeling;natural
LongShort-TermMemoryNetworks:
languageprocessing;timeseriesforecasting;attentionmechanisms;applications
AComprehensiveSurvey.AI2025,6,
215. https://doi.org/10.3390/
ai6090215
Copyright:©2025bytheauthors.
1. Introduction
LicenseeMDPI,Basel,Switzerland.
Thisarticleisanopenaccessarticle The rapid evolution of deep learning has significantly impacted various domains,
distributedunderthetermsand particularly those involving sequential data [1–4]. From natural language processing
conditionsoftheCreativeCommons (NLP) to time series forecasting and speech recognition, the ability to model temporal
Attribution(CCBY)license
dependenciesiscrucialforachievinghighperformanceinthesetasks. TraditionalRNNs
(https://creativecommons.org/
havebeenwidelyusedforsequencemodeling[5,6]; however, theyarelimitedbytheir
licenses/by/4.0/).
AI2025,6,215 https://doi.org/10.3390/ai6090215

AI2025,6,215 2of21
inability to effectively capture long-range dependencies due to the vanishing gradient
problem. This problem arises during the training of RNNs, where gradients diminish
exponentiallythroughtime,makingitdifficultforthenetworktolearnfromlongsequences
ofdata.
Inresponsetothesechallenges, LongShort-TermMemory(LSTM)networkswere
introducedbyHochreiterandSchmidhuberin1997[7,8]. LSTMsareaspecializedkind
ofRNNdesignedtorememberinformationforlongperiods,makingthemparticularly
effectivefortasksthatrequiretheretentionofcontextualinformationovertime[9]. Their
architectureincorporatesmemorycellsandgatingmechanisms,whichregulatetheflow
ofinformation,allowingthenetworktolearnwhichdatatokeepordiscard. Thiscapabil-
ityhasmadeLSTMsapowerfultoolfornumerousapplications,resultinginsignificant
advancementsinvariousfields.
LSTMshavebeensuccessfullyappliedinnaturallanguageprocessing,wheretheyfacil-
itatetaskssuchaslanguagemodeling,machinetranslation,andsentimentanalysis[10,11].
Bymaintainingcontextualinformationacrosssentences,LSTMsimprovethequalityof
generatedtextandenhanceunderstandinginconversationalagents. Intimeseriesanalysis,
LSTMsexcelatforecastingfutureeventsbasedonhistoricaldata,provinginvaluablein
industrieslikefinance,healthcare,andmeteorology[12,13]. Moreover,inspeechrecogni-
tionsystems,LSTMshaveimprovedtheaccuracyofautomaticspeech-to-textconversion,
enablingmoreefficientcommunicationandinteractionwithtechnology [14,15].
Despitetheirstrengths,LSTMsarenotwithoutchallenges. TrainingLSTMnetworks
can be computationally intensive, requiring significant resources and large volumes of
labeleddata[16,17]. Additionally, issuessuchasoverfittingandmodelcomplexitycan
hinder their performance in real-world applications. Researchers continue to explore
variousenhancementsandadaptationsoftheLSTMarchitecture,includingBidirectional
LSTMs that provide context from both past and future inputs, and the integration of
AttentionMechanismsthatallowthemodeltofocusonrelevantpartsoftheinputsequence.
Itisworthnotingthatthissurveyfollowsanarrative(descriptive)reviewapproach,
withtheaimofsynthesisingandthematicallyorganizingthemostrelevantresearchon
LSTMarchitecturesandapplicationsratherthanconductingaprotocol-basedsystematic
review. Inlinewiththis,thereviewadoptsabroadperspectiveacrossmultipledomains
ratherthanfocusingonasingleuse-case(e.g.,financeorhealthcare). Theobjectiveisto
providereaderswithacomprehensiveoverviewthathighlightsthecommonalitiesand
differencesofLSTMusage,therebyservingasageneralentrypointintothefield. Hence,
thekeycontributionsofthispaperareasfollows:
1. Providing a clear and comprehensive explanation of the fundamental principles
andarchitectureofLSTMnetworks, therebyfacilitatinga solidunderstanding for
researchersandpractitionersnewtothetopic.
2. PresentingasystematicreviewofLSTMapplicationsandhighlightingdomainswhere
LSTMshavedemonstratedsignificanteffectiveness.
3. SummarizingandcomparingthedifferentenhancementsandvariantsoftheLSTM
architecturereportedintherecentliterature.
4. Identifyingandcriticallyanalyzingthechallengesandlimitationsthatarisewhen
LSTMsareusedinpracticalimplementations.
5. Highlighting recent research trends and outlining future research directions, thus
offeringguidanceforsubsequentworkinthefield.
Thestructureofthispaperisorganizedasfollows:Section2presentsthefundamentals
ofLSTMnetworks,detailingtheirarchitectureandmechanismsthatenabletheirunique
capabilities. Section3exploresthediverseapplicationsofLSTMsacrossdifferentdomains,
emphasizingtheirimpactandeffectiveness. InSection4,wediscussvariousenhancements

AI2025,6,215 3of21
andadaptationsoftheLSTMframework,includingBidirectionalLSTMsandAttention
Mechanisms. Section5addressesthechallengesandlimitationsassociatedwithLSTM
traininganddeployment,providinginsightsintoComputationalComplexityandData
Requirements. RecentadvancementsandtrendsinLSTMresearcharecoveredinSection6,
showcasingcutting-edgedevelopmentsandemergingresearchareas. Finally,Section7
summarizesthekeyfindingsandsuggestspotentialfutureresearchdirections,aimingto
inspirefurtherexplorationinthefieldofLSTMnetworks. Thestructureofthispaperis
showninFigure1.
Figure1.Structureofthispaper.
2. FundamentalsofLSTM
LSTMnetworksareaspecializedtypeofRNNsdesignedtoeffectivelylearnlong-term
dependenciesinsequentialdata[18]. TraditionalRNNsoftenstrugglewiththevanishing
gradientproblem,whichlimitstheirabilitytocaptureinformationfromdistantelements
inasequence. LSTMsaddressthischallengethroughtheiruniquearchitectureandgating
mechanisms.ThissectionprovidesacomprehensiveoverviewoftheLSTMarchitecture,the
mechanismsthatfacilitateitsfunctionality,andacomparisonwithtraditionalRNNs [19].
2.1. LSTMArchitectureandMechanism
TheLSTMarchitectureisasophisticatedstructuredesignedtomanageandpreserve
informationoverlongsequences. Itconsistsofseveralkeycomponentsthatfacilitateits
enhancedperformance:
• CellState(C ): ThecellstateservesasthememoryunitoftheLSTM,carryingrelevant
t
informationthroughoutthesequence. Itisupdatedateachtimestep,allowingthe
LSTMtoretaininformationoverlongperiods. Thecellstateiscrucialformaintaining
context, as it can store information from previous time steps without significant
degradation. ThisattributeenablesLSTMstorememberessentialdetailsoverlong
sequences,makingthemsuitableforapplicationslikelanguagemodelingandtime
seriesprediction.
• HiddenState(h ): ThehiddenstateistheoutputoftheLSTMattimesteptandis
t
usedformakingpredictions. Itencapsulatesinformationabouttheinputsequence
thusfarandispassedtosubsequentLSTMcells. Thehiddenstatecanbeinterpreted
asthefilteredversionofthecellstate,representingtherelevantinformationneeded
forthecurrentprediction. Thisdynamicnatureofthehiddenstateallowsthemodel
toadaptitsoutputsbasedontheevolvingcontextoftheinputsequence.
• Gates: LSTMs utilize three types of gates to control the flow of information, each
servingadistinctpurpose:

AI2025,6,215
4of21
– InputGate(i ): Thisgatedetermineshowmuchofthenewinformationfromthe
t
currentinputshouldbeaddedtothecellstate. Theinputgateusesasigmoid
activationfunctiontooutputvaluesbetween0and1,effectivelyactingasafilter.
Theformulafortheinputgateis
|     | i   | = σ(W ·[h | ,x  | ]+b ). | (1) |
| --- | --- | --------- | --- | ------ | --- |
|     | t   | i         | t−1 | t i    |     |
AvalueobtainedbyFormula(1)closetooneindicatesthattheinformationshould
befullyaddedtothecellstate,whereasavalueclosetozeroimpliesthatlittle
tonoinformationshouldbeadded. Here, i istheinputgateactivation,W is
|     |     |     |     | t   | i   |
| --- | --- | --- | --- | --- | --- |
theweightmatrix,h t−1 isthehiddenstatefromtheprevioustimestep,x t isthe
currentinput,andb i isthebiasterm.
– ForgetGate(f ): Theforgetgatedecideswhichinformationfromthecellstate
t
shouldbediscarded. Similartotheinputgate,itemploysasigmoidfunction:
|     | f   | = σ(W ·[h | ,x  | ]+b ). | (2) |
| --- | --- | --------- | --- | ------ | --- |
|     | t   | f         | t−1 | t f    |     |
TheforgetgateobtainedbyFormula(2)enablestheLSTMtoremoveirrelevant
information, helping to prevent the cell state from becoming cluttered. This
mechanismisessentialformaintainingthemodel’sabilitytofocusonrelevant
patternsovertime.Inthisformula, f t istheforgetgateactivation,W istheweight
f
matrix,b f isthebiasterm,andtheothervariablesareaspreviouslydefined.
– OutputGate(o t ): Thisgatecontrolswhatpartofthecellstatewillbeoutputas
thehiddenstate. ItdictatestheinformationpassedtothenextLSTMcell:
|     | o   | = σ(W ·[h | ,x  | ]+b ). | (3) |
| --- | --- | --------- | --- | ------ | --- |
|     | t   | o         | t−1 | t o    |     |
TheoutputgatecalculatedbyapplyingFormula(3)ensuresthatthehiddenstate
reflectsonlythemostpertinentinformationfromthecellstate,whichiscrucial
for making accurate predictions at each time step. Here, o is the output gate
t
activation,W istheweightmatrix,b isthebiasterm,andtheothervariablesare
| o   |     | o   |     |     |     |
| --- | --- | --- | --- | --- | --- |
asdefinedearlier.
Theupdatestothecellstateandhiddenstatearegovernedbythefollowingequations:
| C˜  | =tanh(W | ·[h   | ]+b  | ).  |     |
| --- | ------- | ----- | ---- | --- | --- |
| t   |         | C t−1 | ,x t | C   | (4) |
InFormula(4),C˜
t representsthecandidatevaluesforthecellstate,W C istheweight
matrix,andb isthebiasterm.
C
|     | C = | f ⊗C  | +i ⊗C˜ | .   | (5) |
| --- | --- | ----- | ------ | --- | --- |
|     | t   | t t−1 | t      | t   |     |
In Equation (5), C is the updated cell state, C is the previous cell state, and ⊗
| t   |     |     | t−1 |     |     |
| --- | --- | --- | --- | --- | --- |
denoteselement-wisemultiplication.
|     |     | = ⊗tanh(C | ).  |     |     |
| --- | --- | --------- | --- | --- | --- |
|     | h t | o t       | t   |     | (6) |
InEquation(6),
• h istheupdatedhiddenstate.
t
• σisthesigmoidactivationfunction,whichoutputsvaluesintherange(0,1).
• W f ,W,W i C ,W o areweightmatrices,andb f ,b,b i C ,b o arebiasvectors,whicharelearned
duringtraining.

AI2025,6,215 5of21
The architecture of the LSTM cell is visualized in Figure 2, which illustrates the
connectivitybetweenthegates,cellstate,andhiddenstate. Tocomplementthis,Figure3
presents a schematic of three successive LSTM cells across time steps (t−1, t, t+1),
highlighting how the input x, hidden state h, and cell state c are propagated through
thesequence.
ht
Cell
ct−1 × + ct
tanh
× ×
Hidden σ σ tanh σ
ht−1 ht
Input xt
Figure2.ThearchitectureoftheLSTMcell.
Figure3.GeneralschematicofanLSTMnetworkwiththreesuccessivecells(t−1,t,t+1),showing
inputx,hiddenstateh,andcellstatec.
Tofurtherclarifyhowlong-terminformationispreserved,weprovideamoredetailed
explanationoftheLSTMgatingmechanisms,aseachgateplaysacrucialroleincontrolling
theflowofinformation. Theforgetgateevaluatesthepreviouscellstateandthecurrent
inputtodecidewhatinformationtodiscard. Thisselectiveforgettingisessentialtoprevent
the cell state from becoming cluttered with irrelevant data, which helps maintain the
integrityofthelearningprocess. Theoutputoftheforgetgatecanbeinterpretedasamask
thatdetermineswhichpartsofthecellstateshouldbepreserved. Theinputgateassesses
thenewinputandtheprevioushiddenstatetodeterminehowmuchnewinformation
toaddtothecellstate. Thisgateallowsthemodeltodynamicallyincorporaterelevant
informationwhileignoringnoise,therebyimprovinglearningefficiency. Newcandidate
values are created using a hyperbolic tangent function, which helps in scaling the new
information and ensures that the LSTM can adapt to new information in a controlled
manner. Finally,theoutputgatefiltersthecellstatetogeneratethehiddenstate,whichis
usedforpredictionsandpassedtothenexttimestep. Thisensuresthatonlytherelevant
informationisexposedtotheoutput,allowingthemodeltoproducecontextuallyrelevant
outputsbasedontheentiresequence.

AI2025,6,215 6of21
2.2. ComparisonwithTraditionalRNNs
ToillustratetheadvantagesofLSTMsovertraditionalRNNs,wesummarizethekey
differencesinTable1.
Table1.ComparisonofRNNsandLSTMs.
Feature RNNs LSTMs
MemoryRetention Short-term Long-term
VanishingGradientProblem Severe Mitigated
Complexity Simpler MoreComplex
Gates None Three(Input,Forget,Output)
LearningCapability Limited Enhanced
ThetablehighlightsthatwhileLSTMsaremorecomplex,theyaresignificantlybetterat
retaininginformationoverlongersequencescomparedtotraditionalRNNs. Thiscapability
makesLSTMsparticularlysuitablefortaskssuchasnaturallanguageprocessing,where
contextandmeaningcanspanlongdistancesintext. Furthermore,theenhancedlearning
capability of LSTMs is attributed to their ability to adaptively learn which information
isrelevantovertime,whereastraditionalRNNsoftenstruggletomaintainthiscontext.
Inpracticalapplications,thistranslatestoimprovedperformanceintasksinvolvinglong
sequences, such as language translation and speech recognition. The architecture and
mechanismsofLSTMsenablethemtoeffectivelymanagelong-termdependencies,making
themarobustchoiceforavarietyofsequencemodelingtasks. Theuniquepropertiesof
LSTMshaveledtotheiradoptionacrossvariousfields,demonstratingtheirversatilityand
effectivenessinhandlingcomplexsequentialdata. AlthoughLSTMisarelativelymature
architecture,itisstillwidelyusedinbothappliedandcomparativestudiesduetoitsproven
effectivenessandtheavailabilityofwell-establishedimplementations, whichmakeita
strongandreliablebaselineforevaluatingmorerecentsequencemodelingtechniques.
2.3. FeatureSelectionandHyperparameterOptimization
Featureselection(FS)andhyperparameteroptimization(HPO)arecentraltoachieving
reliableLSTMperformance,thoughtheirrelativeimpactdependsondatacharacteristics
andtaskconstraints[20,21]. Filter-styleFS(e.g.,mutual-informationcriteria)helpsreduce
redundancy and noise in high-dimensional sequences and has been shown to improve
downstream modeling in time series settings [22,23]. Beyond filtering, representation-
learningapproachessuchasautoencoderscanprovidecompact,informativeinputsfor
sequencemodels,effectivelyactingasdata-drivenfeatureselectors[24]. AttentionMecha-
nismslikewisereweightinformativetemporalsignalsandhavedemonstratedbenefitsin
multivariatetimeseriesforecasting[25].
On the optimization side, modern HPO encompasses Bayesian methods and
evolutionary/population-basedsearch,withrecentstudiesdocumentingconsistentgains
over manual tuning and ad hoc heuristics [20,26]. Practical workflows often combine
surrogate-basedsearchwithresource-awareschedulingtoexplorearchitecturesandtrain-
ingsettingsefficiently(e.g.,depth/width,look-backwindow,learningrate,dropout,batch
size) [20]. Crucially, evaluation protocols must respect temporal order to avoid infor-
mationleakage;recentanalysesemphasizeblocked/rollingvalidationandwarnagainst
randomsplitsfortimeseries[27,28]. InappliedLSTMstudies,pairingprincipledFSwith
systematic HPO has yielded measurable accuracy and robustness gains in forecasting
tasks, underscoring the value of treating FS and HPO as first-class components of the
modelingpipeline[29].

AI2025,6,215 7of21
3. ApplicationsofLSTM
LSTMnetworkshavegainedprominenceduetotheireffectivenessinhandlingse-
quencesandtime-dependentdata. ThissectionexploresvariousapplicationsofLSTMs
acrossdifferentdomains,highlightingtheirversatilityandimpact.
3.1. NaturalLanguageProcessing
LSTMsplayacrucialroleinNaturalLanguageProcessing(NLP),whereunderstanding
contextandmaintaininglong-termdependenciesareessential[30].Keyapplicationsinclude
thefollowing:
• MachineTranslation[31]: LSTMsareemployedintranslatingtextfromonelanguage
to another. For instance, Google Translate utilizes LSTMs to process sequences of
wordseffectively,improvingtranslationqualityacrossdiverselanguages. Themodel
captures contextual relationships, allowing it to handle idiomatic expressions and
complexgrammaticalstructures,leadingtotranslationsthatarenotonlyaccuratebut
alsocontextuallyrelevant.
• SentimentAnalysis[32–34]: LSTMsanalyzesentimentsintextdata,suchasproduct
reviews or social media posts, and are frequently evaluated on public benchmark
datasets,suchastheIMDBmoviereviewcorpus. Considerascenariowhereacom-
panyanalyzesTwitterdatatogaugecustomersentimentaboutanewproductlaunch.
By using an LSTM model, the company can accurately classify tweets as positive,
negative,orneutral,enablingittorespondpromptlytocustomerfeedbackandadjust
marketingstrategiesaccordingly.
• TextGeneration[35,36]: Inapplicationssuchascreativewritingandchatbots,LSTMs
are used to generate coherent and contextually relevant text. For example, early
textgenerationsystemsreliedonStackedLSTMarchitecturestomodellong-range
dependenciesinlanguage. Morerecentmodels,suchasOpenAI’sGPT-2,arebasedon
theTransformerarchitecturebutstillhighlighttheimportanceofsequencelearning
forgeneratinghuman-liketextfromagivenprompt. Businessescanleveragethese
capabilitiestocreateautomatedcustomersupportchatbotsthatprovideaccurateand
contextuallyappropriateresponsestouserinquiries.
• NamedEntityRecognition[37–40]: LSTMshelpidentifyandclassifyentitiesintext,
suchasnamesofpeople, organizations, andlocations. Forexample, inhealthcare,
extractingpatientinformationfromclinicalnotesiscrucial. AnLSTM-basedmodel
canaccuratelyidentifyandextractentitieslikedrugnames, dosages, andmedical
conditions,facilitatingbetterdatamanagementandresearch.
3.2. TimeSeriesAnalysis
LSTMsareparticularlyeffectiveinanalyzingtimeseriesdataduetotheirabilityto
capturetemporaldependencies[41]. Applicationsincludethefollowing:
• FinancialForecasting[42,43]: LSTMsarewidelyusedinpredictingstockpricesand
markettrendsbyanalyzinghistoricaldata. Forinstance,hedgefundsemployLSTM
modelstoforecaststockpricesbasedonhistoricaltradingdata,economicindicators,
andnewssentiment. Bylearningpatternsfrompastdata,LSTMshelptradersmake
informeddecisionsaboutbuyingorsellingstocksatoptimaltimes.
• WeatherForecasting[44–46]: MeteorologicalmodelsutilizeLSTMstopredictweather
conditions by analyzing historical weather data. An example is using LSTMs to
forecast temperature and precipitation based on past climatic data, enabling more
accuratepredictions.Thiscapabilityiscrucialforagriculture,wherefarmerscanbetter
planplantingandharvestingtimesbasedonexpectedweatherpatterns.

AI2025,6,215 8of21
• AnomalyDetection[47,48]: Infieldssuchasmanufacturingandfinance,LSTMscan
identifyanomaliesintimeseriesdata,suchasfraudulenttransactionsorequipment
failures. Forexample,abankmightuseLSTMstomonitortransactionpatternsand
detectunusualactivitiesthatcouldindicatefraud. Thesystemcanautomaticallyflag
thesetransactionsforfurtherinvestigation,enhancingsecurityandreducinglosses.
3.3. SpeechRecognition
LSTMs have significantly improved the accuracy of automatic speech recognition
(ASR)systems. Theirapplicationsincludethefollowing:
• Voice Assistants [49]: Technologies like Siri and Google Assistant use LSTMs to
understandandprocessspokencommands. Forinstance,whenauseraskstheirvoice
assistanttosetareminder,theLSTMmodelprocessesthespokeninput,maintaining
contextacrosstheconversationtoprovideaccurateresponses. Thisenhancesuser
experiencebyenablingmorenaturalinteractions.
• TranscriptionServices[50]: LSTMsfacilitatetheconversionofspokenlanguageinto
writtentext. CompanieslikeOtter.aiutilizeLSTMstoprovidereal-timetranscription
servicesformeetingsandlectures;inthisfield,LibriSpeechisoneofthemostcom-
monlyusedbenchmarkdatasetsfortrainingandevaluation. Themodelcanhandle
variousaccentsandspeechpatterns, ensuringthattranscriptionsareaccurateand
contextuallyrelevant,whichisinvaluableforprofessionalsneedingpreciserecords
ofdiscussions.
• EmotionRecognition[51,52]: Byanalyzingspeechpatternsandintonations,LSTMs
canidentifyemotionalstates,whichisusefulinapplicationssuchasmentalhealth
monitoring and customer service. Understanding emotions can lead to improved
userexperiencesandinteractions,ascustomerservicerepresentativescantailortheir
responsesbasedonthedetectedemotionaltone.
3.4. OtherEmergingApplications
Beyondtraditionalapplications,LSTMsarebeingexploredinvariousemergingfields:
• Healthcare [53–56]:LSTMsanalyzepatientdataovertime,predictinghealthoutcomes
andpersonalizingtreatmentplans. Forinstance,hospitalscanuseLSTMmodelsto
track vital signs of patients in real-time, predicting potential health deteriorations.
This enables timely interventions that can significantly improve patient outcomes,
suchasearlydetectionofsepsis.
• Robotics [57–59]: In robotics, LSTMs help in path planning and decision-making
bypredictingfuturestatesbasedonpastmovementsandsensoryinputs. Consider
autonomous vehicles, which use LSTMs to analyze traffic patterns and make real-
timenavigationdecisions. Thisenhancesthevehicle’sabilitytooperatesafelyand
efficientlyindynamicenvironments.
• VideoAnalysis[60–63]: LSTMsareusedinanalyzingvideosequencesforapplications
suchasactionrecognitionandeventprediction. Forexample,securitysystemscan
utilize LSTMs to detect unusual activities in surveillance footage. By analyzing
sequences of frames, the system can identify potential security threats, enhancing
safetyinpublicspaces.
Table 2 summarizes the various applications of LSTMs across different domains,
highlighting their key features and benefits. To sum up, LSTMs have shown strong
performanceinavarietyofapplicationdomains. Forexample,inspeechprocessingand
trafficprediction,theirabilitytocapturetemporaldependencieshasyieldedbetterresults
thantraditionalmachinelearningmodels. Infinancialforecasting,LSTMsdemonstrated
robustnesstonoisyandhighlydynamicsequentialdata. However,severallimitationshave

AI2025,6,215
9of21
alsobeenreportedintheliterature. InIoTscenarios,thehightrainingandinferencecosts
ofLSTMsoftenmakethemunsuitablefordeploymentonresource-constraineddevices.
In healthcare, long and irregular time series sequences frequently cause performance
degradation. Moreover,thelimitedinterpretabilityofLSTMmodelshasbeenidentifiedas
acriticalissueinsafety-criticaldomains,suchasmedicaldiagnosis. Theseobservations
suggestthatfurtherimprovementsarerequired,particularlytoenhancemodelefficiency,
increaserobustnesstolongandirregularsequences,andintegrateinterpretabilitymethods
orhybridarchitectures(e.g.,attention-basedextensions)intoLSTMmodels.
Table2.ApplicationsofLSTMnetworksacrossdifferentdomainsandtheirkeybenefits.
| ApplicationDomain | KeyTasks/Use-Cases | Benefits |
| ----------------- | ------------------ | -------- |
Captureslong-term
MachineTranslation,
dependenciesintextand
| NaturalLanguage | SentimentAnalysis,Text |     |
| --------------- | ---------------------- | --- |
improvescontextual
| Processing | Generation,Named |     |
| ---------- | ---------------- | --- |
understandingand
EntityRecognition
generationquality
Learnstemporalpatterns
FinancialForecasting,
forbetterforecastingand
| TimeSeriesAnalysis | WeatherForecasting, |     |
| ------------------ | ------------------- | --- |
detectsunusualbehaviour
AnomalyDetection
insequentialdata
|     | VoiceAssistants, | Maintainscontextacross |
| --- | ---------------- | ---------------------- |
|     | Speech-to-Text   | spokeninputandimproves |
SpeechProcessing
|     | Transcription,Speech | sequence-to-sequence |
| --- | -------------------- | -------------------- |
|     | EmotionRecognition   | predictionaccuracy   |
Enablesreal-time
|     | PatientMonitoring, | predictionfromevolving |
| --- | ------------------ | ---------------------- |
Healthcare
|     | OutcomePrediction | physiologicalsignalsand |
| --- | ----------------- | ----------------------- |
supportsearlyintervention
Predictsfuturestatesfrom
|     | PathPlanning,Navigation, | sensordataandimproves |
| --- | ------------------------ | --------------------- |
Robotics
|     | Decision-Making | autonomous |
| --- | --------------- | ---------- |
decision-making
Modelstemporaldynamics
ActionRecognition,
| VideoAnalysis |     | invisualsequencesto |
| ------------- | --- | ------------------- |
EventPrediction
recognisecomplexactivities
4. VariantsandImprovements
While LSTM networks have proven to be highly effective for sequence modeling,
severalvariantsandimprovementshaveemergedtoenhancetheirperformanceinvarious
applications. Thissectiondiscussesthreesignificantadvancements: BidirectionalLSTMs,
StackedLSTMs,andAttentionMechanisms. Itisworthnotingthat,unliketheapplication
sectionabove,thissectionprovidesasystematicoverviewofthreemainLSTMvariants
independentlyoftheirapplicationdomains,inordertoclearlydistinguisharchitectural
differencesfromuse-casespecificdeployments.
4.1. BidirectionalLSTMs
BidirectionalLSTMs(BiLSTMs)areanextensionofthestandardLSTMarchitecture
thatallowthenetworktolearnfrombothpastandfuturecontextsinasequence[64–67].
InatraditionalLSTM,informationflowsinonedirection, typicallyfrompasttofuture.
However,BiLSTMsprocesstheinputsequenceinbothforwardandbackwarddirections:

AI2025,6,215 10of21
• Architecture: ABiLSTMconsistsoftwoLSTMlayersforeachtimestep: oneprocesses
thesequencefromthebeginningtotheend(forward)andtheotherprocessesitfrom
theendtothebeginning(backward). Theoutputsofbothlayersareconcatenatedor
combined,providingaricherrepresentationthatcapturescontextfrombothsides.
Thisarchitectureisparticularlyusefulinscenarioswherethecontextsurroundinga
wordiscriticalforunderstandingitsmeaning.
• Example: Inasentencelike“Thebankoftheriver,”understandingtheword“bank”
requires context from both directions to determine whether it refers to a financial
institutionorthesideofariver. ABiLSTMusestheforwardlayertogathercontext
from preceding words and the backward layer to gather context from subsequent
words,enhancingitsabilitytodisambiguatemeaningeffectively.
• Applications: This approach is particularly useful in tasks such as named entity
recognition,wherethemodelneedstoidentifypropernounsincontext,andmachine
translation,wheresyntaxandsemanticsfrombothdirectionsarecriticalforaccurate
translations. Forinstance,BiLSTMshavebeenshowntoimprovetheperformanceof
systemslikeGoogleTranslate,whichneedtounderstandentirephrasesratherthan
isolatedwords.
• Benefits: Byleveraginginformationfrombothpastandfuturestates,BiLSTMsim-
provethemodel’sabilitytomakeaccuratepredictions. Thisdual-contextlearning
oftenresultsinbetterperformanceontasksthatrequireacomprehensiveunderstand-
ingofinputsequences,leadingtomorereliableoutputsinapplicationslikesentiment
analysisandtextgeneration.
Paper[64]presentsabidirectionalLongShort-TermMemory(BiDLSTM)-basedintru-
siondetectionsystemthatsignificantlyenhancesdetectionaccuracywhilereducingfalse
alarmratesforvariousnetworkattacks,particularlyUser-to-Root(U2R)andRemote-to-
Local(R2L)threats,whencomparedtoconventionalmodels. Thismodeleffectivelylearns
long-term visual–language interactions, achieving competitive performance in caption
generation and superior results in image–sentence retrieval through innovative hierar-
chical embeddings and data augmentation techniques. Moreover, article [65] develops
andevaluatesbothunidirectionalandBidirectionalLSTMmodelsforshort-termtraffic
prediction. ThefindingsrevealthattheBidirectionalLSTMoutperformsitsunidirectional
counterpart,achievingover90%accuracyinspeedpredictionsforupto60min,aswell
as high accuracy in traffic flow predictions across various horizons, thereby providing
reliableAItoolsforroadoperators. Inaddition,thestudybyHuangetal.[66]introducesa
novelprognosticmethodthatutilizesBidirectionalLSTMnetworkstoeffectivelyintegrate
sensorandoperationalconditiondataforpredictingtheremainingusefullife(RUL)of
engineeredsystems. Thisapproachdemonstratessuperiorperformanceinacasestudythat
focusedonaircraftturbofanenginescomparedtoexistingAI-basedmethods. Finally,the
articlebyMahadevaswamyetal.[67]summarizestheapplicationofaBidirectionalLSTM
network for sentiment analysis, successfully classifying Amazon product reviews into
positiveandnegativecategories. Thisachievementisattributedtothenetwork’scapability
tomanagelong-termdependencies,basedonacomprehensivedatasetof104,975reviews
ofmobileelectronics.
4.2. StackedLSTMs
StackedLSTMsrefertothearchitecturewheremultipleLSTMlayersarestackedon
topofeachother[68–71]. Thisdeeparchitectureallowsthemodeltolearnmorecomplex
representationsofthedata:
• Architecture: InaStackedLSTM,theoutputofoneLSTMlayerservesastheinput
tothenextlayer. Thishierarchicalstructureenablesthemodeltocapturehigh-level

AI2025,6,215 11of21
featuresatdeeperlayerswhileretainingthetemporaldynamicsinthelowerlayers.
Typically,thefirstfewlayersmightfocusoncapturingsimplepatterns,whiledeeper
layerscanlearnmorecomplexrelationshipsinthedata.
• Example: In speech recognition, lower layers of a Stacked LSTM might focus on
phoneticfeatures,suchasphonemesandintonation,whilehigherlayerscancapture
linguisticstructuresandcontext. Forinstance,amodelmightfirstlearntorecognize
thesoundsofwordsandthenunderstandtheminthecontextofsentences,leadingto
moreaccuratetranscriptions.
• Applications: StackedLSTMsareeffectiveintasksrequiringintricatefeatureextrac-
tion,suchasvideoanalysis,naturallanguageprocessing,andhandwritingrecognition.
For example, in video analysis, lower layers might extract motion patterns, while
higherlayerscouldrecognizeactionslikerunningorjumping. Thiscapabilityallows
for sophisticated applications, such as action recognition in sports or surveillance
footageanalysis.
• Benefits: TheincreasedcapacityofStackedLSTMsallowsthemtomodelmorecom-
plexrelationshipswithinthedata,leadingtoimprovedperformanceonchallenging
tasks. However,thiscomplexityrequirescarefultuningofhyperparameterstoavoid
overfitting,particularlywhenworkingwithsmallerdatasets.
ThestudybyMaetal.[68]developsaStackedLSTMneuralnetworkmodeldesigned
topredictdailyqualitycontrolrecordsforradiotherapymachineswithremarkableaccuracy.
This model not only outperforms the ARIMA model but also demonstrates robustness
inforecastingpotentialmachinefailures,therebyfacilitatingpreventivemaintenance. In
acomprehensivereview,Ghimireetal.[69]presentmodelingtechniquesandintroduce
a hybrid SAELSTM framework that combines deep learning with Manta Ray Foraging
Optimization. This innovative framework constructs accurate prediction intervals for
dailyGlobalSolarRadiation,showcasingsuperiorperformancecomparedtoconventional
machinelearningmodelsandsignificantlyenhancingsolarenergymonitoringsystems.
Wangetal.[70]introduceastackedresidualLSTMmodelaimedatpredictingsentiment
intensity. Byincorporatingresidualconnections,thismodeleffectivelyaddressesthechal-
lengesassociatedwithtrainingdeepernetworks,resultinginimprovedoptimizationand
predictionaccuracycomparedtotraditionallexicon-based,regression,andneuralnetwork
methods. Finally, Yuetal.[71]introduceanovelhierarchicalfaultdiagnosisalgorithm
basedonStackedLSTMnetworksforrollingbearings,achievinganimpressiveaccuracy
of over 99%. This algorithm automatically extracts features from raw temporal signals
withoutpreprocessing,surpassingtraditionalmethodsandstate-of-the-artintelligentfault
diagnosistechniques.
4.3. AttentionMechanisms
AttentionMechanismshaverevolutionizedthewaysequence-to-sequencemodelsop-
erate,particularlyinconjunctionwithLSTMs[72–77]. Thesemechanismsallowthemodel
tofocusonspecificpartsoftheinputsequencewhengeneratingeachpartoftheoutput
sequence. Thesevariantsandimprovements—BidirectionalLSTMs,StackedLSTMs,and
AttentionMechanisms—enhancethecapabilitiesoftraditionalLSTMnetworks,making
themmoreeffectiveforawiderrangeofapplications. Byleveragingtheseadvancements,
researchersandpractitionerscanachievebetterperformanceandmoreaccurateresultsin
complexsequencemodelingtasks:
• Concept: Insteadoftreatingallinputtokensequally,AttentionMechanismsweighthe
importanceofdifferenttokensforeachoutputtoken. Thisselectivefocusenablesthe
modeltocapturerelevantcontextmoreeffectively,whichisparticularlybeneficialin
longsequenceswherenotallpartsoftheinputareequallyimportantforeveryoutput.

AI2025,6,215 12of21
• Example: Inmachinetranslation,whentranslatingalongsentence,themodelcan
focus on the relevant words that contribute to the meaning of the current output
word. Forinstance,intranslating“Thecatsatonthemat,”themodelmightfocuson
“cat”whengeneratingtheword“it,”improvingthecoherenceofthetranslation. This
capabilityhelpsingeneratingmorefluentandaccuratetranslations,particularlyin
complexsentences.
• Applications: AttentionMechanismsarewidelyusedintaskssuchasmachinetransla-
tion,textsummarization,imagecaptioning,andevenvideoanalysis. Forexample,
intextsummarization, attentionhelpsthemodelidentifykeysentencesinadocu-
ment to create concise summaries that encapsulate the main ideas without losing
importantcontext.
• Benefits: TheintegrationofattentionwithLSTMsleadstosignificantimprovements
inperformance,particularlyforlongsequences. ItreducestheburdenontheLSTM
torememberallpreviousstates,allowingittoconcentrateonrelevantinformation
dynamically. ThishasledtothedevelopmentofmodelsliketheTransformer,which
reliesheavilyonAttentionMechanismstoachievestate-of-the-artresultsinvarious
NLPtasks.
The study by Sang et al. [72] introduces the Attention Mechanism Variant LSTM
(AMV-LSTM),whichsignificantlyimprovesstockpricepredictionaccuracy. Thismodel
enhancestraditionalLSTMframeworksbycouplingtheforgetandinputgates,addinga
simpleforgetgatetothelong-termstate,andincorporatinganAttentionMechanism. As
aresult,iteffectivelyaddressesstabilityandoverfittingchallengescommonlyassociated
withconventionalLSTMmodels. Inarelatedeffort, Linetal.[73]presentadual-stage
attention-based LSTM network tailored for short-term zonal electricity load probabilis-
tic forecasting. This innovative approach enhances feature selection through a feature
attentionencoderandcapturestemporaldependenciesviaadecoder,yieldingimproved
accuracyandgeneralizationoverexistingmodels,particularlyontheGEFCom2014dataset.
Moreover, Xiang et al. [74] propose a novel fault detection method for wind turbines
thatintegratesaconvolutionalneuralnetwork(CNN)withanattention-enhancedLong
Short-TermMemorynetwork(LSTM).ByutilizingSCADAdata,thismethodeffectively
extractsdynamicchanges,improveslearningaccuracy,andprovidesearlywarningsfor
anomalies,therebyenablingthepredictionofearlyfailuresinwindturbinecomponents.
Intherealmofenvironmentalmonitoring,Yangetal.[75]introduceawaterqualitypre-
dictionmodelknownasCNN-LSTMwithAttention(CLA).ThismodelforecastspHand
NH3-NlevelsintheBeilunEstuarybyemployinglinearinterpolationformissingdata
and wavelet techniques for denoising. The hybrid CNN-LSTM architecture effectively
addressesnonlineartimeseriesprediction,withtheAttentionMechanismenhancinglong-
termdependencies. ExperimentalfindingsdemonstratethatCLAoutperformsexisting
modelsandmaintainsstablepredictionsacrossvarioustimelags. Furthermore, Ranet
al.[76]proposeanLSTMmethodaugmentedwithanAttentionMechanismfortraveltime
prediction. ThismodeladdressesthelimitationsoftraditionalLSTMsbyincorporating
departuretimeandmodelinglong-termdependenciesthroughatreestructure. Utilizing
datasets from Highways England, the experimental results indicate that the proposed
modelachievessuperioraccuracycomparedtostandardLSTMandotherbaselinemeth-
ods,effectivelyleveragingtheAttentionMechanismtoenhancepredictions. Finally,Liu
et al. [77] introduce the attention-based bidirectional Long Short-Term Memory with a
convolutionlayer(AC-BiLSTM)architecture. Bycombiningaconvolutionallayerwith
BiLSTM and an Attention Mechanism, this model enhances text classification tasks in
naturallanguageprocessing. Itexcelsatextractinghigher-levelphraserepresentationsand
capturingbothlocalandglobalsemanticfeatures,demonstratingsuperiorclassification

AI2025,6,215 13of21
accuracyacrosssixsentimentclassificationdatasetsandaquestionclassificationdataset,
therebyoutperformingexistingstate-of-the-artmethods.
InTable3,thevariousvariantsandimprovementsofLSTMnetworksaresummarized,
highlightingtheirkeyfeatures,applications,andbenefits.
Table3.VariantsandimprovementsofLSTMnetworks.
Variant KeyFeatures Applications Benefits
Improvedcontext
Processessequencesin NamedEntityRecognition,
BidirectionalLSTMs understanding,better
bothdirections MachineTranslation
disambiguation
Enhancedfeatureextraction,
MultipleLSTMlayersfor SpeechRecognition,
StackedLSTMs abilitytomodel
deeperlearning VideoAnalysis
complexpatterns
Betterhandlingoflong
Focusesonspecificinput MachineTranslation,
AttentionMechanisms sequences,dynamic
partsforeachoutput TextSummarization
context focus
5. ChallengesandLimitations
Despite the effectiveness of LSTM networks in various applications, they are not
withouttheirchallengesandlimitations. Thissectiondiscussesthreemajorissues: Compu-
tationalComplexity,DataRequirements,andTrainingDifficulties.
5.1. ComputationalComplexity
LSTM networks are inherently complex due to their architecture, which includes
multiplegatesandmemorycells. Thiscomplexityleadstoseveralchallenges:
• High Resource Consumption: LSTMs require significant computational resources,
especially for large datasets and deep architectures. Training an LSTM model can
demandsubstantialCPUorGPUtime,makingitlessfeasibleforreal-timeapplications.
Forinstance,trainingastate-of-the-artLSTMfornaturallanguageprocessingtasks
mayrequirespecializedhardware,likeTPUs,whichcanbecostly.
• ScalabilityIssues: Asthesizeofthenetworkincreases,particularlywhenstacking
multiple LSTM layers, scalability becomes a concern. The time taken to train and
thememoryrequiredcangrowexponentially,limitingthemodel’sapplicabilityin
resource-constrained environments. This limitation can hinder the deployment of
LSTM-basedmodelsinmobileorembeddedsystemswherecomputationalpower
islimited.
• InferenceSpeed: ThecomplexityofLSTMscanalsoaffectinferencespeed,whichis
criticalinapplicationslikereal-timespeechrecognitionorchatbots. Slowerinference
can hinder user experience and system performance, leading to delays that may
frustrateusers. Forexample,inacustomersupportchatbot,anylaginresponsetime
candiminishtheperceivedqualityoftheservice.
5.2. DataRequirements
LSTMsrequiresubstantialamountsofhigh-qualitydataforeffectivetraining. This
necessityposesseveralchallenges:
• LargeDatasets: LSTMstypicallyperformwellwhentrainedonlargedatasets,which
maynotalwaysbeavailable.Indomainswithlimiteddata,suchasspecializedmedical
applicationsornichemarkets,LSTMscanoverfit,leadingtopoorgeneralizationon

AI2025,6,215 14of21
unseendata. Thisissuecanresultinmodelsthatperformwellontrainingdatabut
failtodeliveraccuratepredictionsinreal-worldscenarios.
• Data Quality: The quality of the training data significantly impacts model perfor-
mance.Noisy,unstructured,orbiaseddatacanresultinsuboptimallearningoutcomes.
Forexample,innaturallanguageprocessing,poorlyannotateddatasetscanleadto
models that misunderstand context or semantics, thereby generating irrelevant or
incorrectoutputs.
• Domain-SpecificData: TrainingLSTMsforspecializedtasksoftenrequiresdomain-
specific data, which can be difficult and time-consuming to collect. In fields like
healthcare,obtainingannotateddatasetscaninvolveextensivecollaborationwithex-
pertsandadherencetoregulatorystandards,complicatingthedatacollectionprocess
andextendingprojecttimelines.
Nevertheless,recentstudieshaveshownthatsyntheticdatacaneffectivelycompensate
forlimitedreal-worlddatasetsinLSTMapplications[78,79]. Forexample,GAN-generated
time series [80–82] have been used to augment LSTM training in condition monitoring
andpredictivemaintenance, andsyntheticspeechfeatureshavebeenemployedtopre-
trainLSTM-basedspeakerrecognitionmodels. Similarapproacheshavealsobeenapplied
in climate modeling by combining ConvLSTM [83,84] with synthetic sequence data to
improve prediction accuracy in data-sparse regions. These examples demonstrate that
LSTMscanstillbeappliedindata-scarcescenarioswhenappropriatedataaugmentation
techniquesareused.
5.3. TrainingDifficulties
TrainingLSTMnetworkspresentsseveralchallengesthatcanaffecttheireffectiveness:
• LongTrainingTimes: Duetotheircomplexity,LSTMscantakealongtimetotrain,
especiallywithlargedatasets. Thisextendedtrainingperiodcanbeabarriertorapid
prototypingandexperimentation. Researchersmayfinditdifficulttoiteratequickly
onmodeldesigns,slowingdowntheoveralldevelopmentprocessanddelayingthe
deploymentofsolutions.
• Hyperparameter Tuning: LSTMs have numerous hyperparameters (e.g., learning
rate, number of layers, hidden units) that need to be carefully tuned for optimal
performance. Findingtherightcombinationcanbechallengingandoftenrequires
extensiveexperimentation. Thistuningprocesscanberesource-intensive,requiring
multipletrainingrunsandpotentiallyconsumingsignificantcomputationalresources.
• VanishingandExplodingGradients: AlthoughLSTMsaredesignedtomitigatethe
vanishinggradientproblem,theyarestillsusceptibletoexplodinggradientsduring
training. Thisissuecanleadtounstablelearningandhindertheconvergenceofthe
model. Ifnotproperlymanaged,explodinggradientscancausethemodeltodiverge,
resulting in NaN values during training and necessitating the need for gradient
clippingorotherstabilizingtechniques.
Table 4 summarizes the various challenges and limitations associated with LSTM
networks,highlightingtheirimplicationsonperformanceandapplicability. WhileLSTM
networksoffersignificantadvantagesinsequencemodeling,theyalsofacesubstantialchal-
lengesthatcanlimittheireffectivenessandapplicability. Understandingtheselimitations
is crucial for researchers and practitioners aiming to implement LSTMs successfully in
variousdomains.

AI2025,6,215 15of21
Table4.ChallengesandlimitationsofLSTMnetworks.
Challenge Description Implications
Slowertrainingand
Highresource
inference,limited
ComputationalComplexity consumptionand
applicabilityin
scalabilityissues
real-timesystems
Riskofoverfitting,poor
Needforlarge,
DataRequirements generalization,andlimited
high-qualitydatasets
domainapplicability
Longtrainingtimes Increaseddevelopment
TrainingDifficulties andhyperparameter timeandpotential
tuningchallenges instabilityinlearning
6. RecentAdvancesandTrends
Asthefieldofmachinelearningcontinuestoevolve,recentadvancesandtrendsin
LSTMnetworksreflectongoinginnovationsinarchitectures,performanceevaluations,and
emergingresearchareas. Thissectionexploresthesedevelopmentsindetail.
6.1. InnovationsinLSTMArchitectures
InnovationsinLSTMarchitectureshavesignificantlyenhancedtheircapabilitiesand
performanceinvariousapplications. Researchershaveintroducedseveralmodificationsto
thetraditionalLSTMdesign,aimingtoaddressspecificlimitationsandimprovetraining
efficiency.Onenotableinnovationisthedevelopmentofpeepholeconnections,whichallow
LSTMstoaccessthecellstatedirectlyfromthegates.Thismodificationenablesthemodelto
makemoreinformeddecisionsbasedonthecurrentmemorycontent,leadingtoimproved
learning dynamics. Another advancement is the Grid LSTM, which extends the LSTM
architecturetohandlemulti-dimensionalsequences. Thisarchitectureisparticularlyuseful
in applications like video processing, where spatial and temporal information must be
capturedsimultaneously. ByorganizingtheLSTMcellsinagridstructure,theGridLSTM
caneffectivelylearncomplexrelationshipsinhigh-dimensionaldata. Additionally,layer
normalizationtechniqueshavebeenintegratedintoLSTMarchitecturestostabilizetraining
and improve convergence speed. This approach normalizes the inputs across features
ratherthanacrossthebatch,makingitparticularlybeneficialforrecurrentnetworkswhere
batchsizescanvary.
6.2. PerformanceComparisons
AsvariousLSTMarchitecturesandvariantshaveemerged,numerousstudieshave
conductedperformancecomparisonstoevaluatetheireffectivenessagainsttraditionalmod-
elsandothersequence-basedarchitectures[85–87].RecentbenchmarksindicatethatLSTMs
oftenoutperformstandardRNNsintasksinvolvinglong-rangedependencies[88–90].How-
ever,newerarchitectures,suchastheTransformer,haveshownsuperiorperformancein
manynaturallanguageprocessingtasks,promptingresearcherstoexplorehybridmodels
that combine the strengths of LSTMs and Attention Mechanisms [91–93]. For instance,
studies comparing LSTMs to Transformers in machine translation tasks have revealed
thatwhileLSTMscanhandlesequencedataeffectively,Transformersoftenachievebetter
performanceintermsofaccuracyandtrainingefficiency, mainlybecauseTransformers
processentiresequencessimultaneouslyratherthansequentially[94–96]. Nevertheless,
LSTMsremainvaluableinseveralscenarios: indata-scarceorresource-limitedsettings,
theyoftendemonstratebetterconvergenceandgeneralizationpropertiesduetotheirse-
quential inductive biasing, and in real-time or embedded applications (e.g., healthcare

AI2025,6,215 16of21
monitoringandindustrialIoT),LSTM-basedmodelshavebeenshowntooffercompetitive
performanceandlowercomputationaloverheadonwearablesensortasks [97–99]. More-
over,comparisonshavehighlightedthatintegratingAttentionMechanismswithLSTMs
can enhance their performance significantly, particularly in tasks requiring contextual
understandingoverlongsequences[100,101]. Thesehybridmodelsleveragethetemporal
strengthsofLSTMswhilebenefitingfromthecontextualawarenessprovidedbyAttention
Mechanisms[102,103].
6.3. EmergingResearchAreas
EmergingresearchareasrelatedtoLSTMsreflecttheongoingexplorationoftheircapa-
bilitiesinvariousfields. Onesignificantareaistransferlearning,wherepre-trainedLSTM
modelsareadaptedtonewtaskswithlimiteddata[104]. Thisapproachhasgainedtraction
asitallowsmodelstoleveragepriorknowledge,reducingtheneedforextensivetraining
ondatasets. AnotherpromisingareaistheapplicationofLSTMsinreinforcementlearning.
ResearchersareinvestigatinghowLSTMscanbeusedtomodelenvironmentswithtem-
poraldependencies,enablingagentstomakebetterdecisionsbasedonpastexperiences.
Thisintegrationhasthepotentialtoenhancetheperformanceofreinforcementlearning
algorithmsincomplexanddynamicenvironments. Recentstudiesdemonstratethispo-
tential: for instance, LSTM networks have been incorporated into a TD3 reinforcement
learning frameworkto improveroboticpath planning in dynamicenvironments [105],
whileGT-LSTMintegratesgeospatialandtemporaldependenciestoenhanceagent-based
modelinginmultimodalcontexts[106]. Additionally,theadaptationofLSTMsformulti-
modallearningisgainingattention[107]. ThisinvolvescombiningLSTMnetworkswith
other data types, such as images and audio, to create models that can process and un-
derstandinformationacrossdifferentmodalities. Applicationsinthisareaincludevideo
analysis,whereLSTMscanhelpanalyzebothvisualandauditorycomponentstointerpret
scenes more effectively. Finally, advancements in explainable AI (XAI) are prompting
researcherstofocusonmakingLSTMmodelsmoreinterpretable[108]. Understanding
howLSTMsmakedecisionsiscrucialfortheirdeploymentinsensitiveapplicationslike
healthcareandfinance,wheretransparencyisessential.
7. Conclusions
Inconclusion,LongShort-TermMemory(LSTM)networkshaveestablishedthem-
selvesasacornerstoneinthefieldofsequencemodeling,offeringpowerfulsolutionsfor
tasksinvolvingtemporaldependencies. Whilethemostsignificantchallengescurrently
limitingtheirbroaderadoptionremain(i)thehighcomputationalcostandlongtraining
times, (ii) the tendency to overfit on limited data, and (iii) the lack of interpretability
comparedtomorerecentarchitectures,LSTMsneverthelessremainhighlycompetitivein
specificscenarios. Theseincludeapplicationswherestricttemporalorderingisessential
(e.g.,real-timesensorstreamsandspeechprocessing),situationswheretrainingdatais
scarce,anddeploymentsthatrequirelightweightmodelsforedgedevices.
RecentinnovationsinLSTMarchitectures,suchaspeepholeconnectionsandGrid
LSTMs,haveenhancedtheircapabilitiesandbroadenedtheirapplicabilitytomorecomplex
data. Inparallel,performancecomparisonswithTransformer-basedmodelshighlightthe
evolvinglandscapeofdeeplearning,wherehybridapproachesthatcombinethestrengths
ofLSTMsandAttentionMechanismsaregainingtraction.
Intermsoffutureresearch,emergingareassuchastransferlearning,reinforcement
learning, and multimodal learning indicate promising directions and demonstrate the
adaptabilityofLSTMnetworksacrossvariousdomains—fromnaturallanguageprocessing
tovideoanalysis. Continuedeffortstoreducecomputationaloverhead,improvegeneral-

AI2025,6,215 17of21
izationinlow-dataenvironments,andincreasemodelinterpretabilitywillbecentralfor
advancingLSTMtechnologyandmaximizingitspracticalimpact.
AuthorContributions:Conceptualization,M.K.;formalanalysis,M.K.;methodology,M.K.;valida-
tion,A.M.;writing—originaldraft,M.K.;writing—reviewandediting,M.K.andA.M.Allauthors
havereadandagreedtothepublishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
DataAvailabilityStatement:Notapplicable.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.
References
1. Janiesch,C.;Zschech,P.;Heinrich,K. Machinelearninganddeeplearning. Electron.Mark.2021,31,685–695.[CrossRef]
2. Taye,M.M. Understandingofmachinelearningwithdeeplearning:Architectures,workflow,applicationsandfuturedirections.
Computers2023,12,91.[CrossRef]
3. Gasmi,K.;BenLtaifa,I.;EltoumAbdalrahman,A.;Hamid,O.;OthmanAltaieb,M.;Ali,S.;BenAmmar,L.;Mrabet,M. Hybrid
FeatureandOptimizedDeepLearningModelFusionforDetectingHatefulArabicContent. IEEEAccess2025,13,131411–131431.
[CrossRef]
4. Gasmi,K.;Hrizi,O.;BenAoun,N.;Alrashdi,I.;Alqazzaz,A.;Hamid,O.;OthmanAltaieb,M.;Abdalrahman,A.E.M.;BenAmmar,
L.;Mrabet,M.;etal. EnhancedMultimodalPhysiologicalSignalAnalysisforPainAssessmentUsingOptimizedEnsembleDeep
Learning. Comput.Model.Eng.Sci.2025,143,2459–2489.[CrossRef]
5. Mienye, I.D.; Swart, T.G.; Obaido, G. Recurrent neural networks: A comprehensive review of architectures, variants, and
applications. Information2024,15,517.[CrossRef]
6. Ullah, I.; Mahmoud, Q.H. Design and development of RNN anomaly detection model for IoT networks. IEEE Access
2022,10,62722–62750.[CrossRef]
7. VanHoudt,G.;Mosquera,C.;Nápoles,G. Areviewonthelongshort-termmemorymodel. Artif.Intell.Rev.2020,53,5929–5955.
[CrossRef]
8. Sherstinsky,A. Fundamentalsofrecurrentneuralnetwork(RNN)andlongshort-termmemory(LSTM)network. Phys. D
NonlinearPhenom.2020,404,132306.[CrossRef]
9. Halbouni, A.; Gunawan, T.S.; Habaebi, M.H.; Halbouni, M.; Kartiwi, M.; Ahmad, R. Machinelearninganddeeplearning
approachesforcybersecurity:Areview. IEEEAccess2022,10,19572–19585.[CrossRef]
10. Behera,R.K.;Jena,M.;Rath,S.K.;Misra,S. Co-LSTM:ConvolutionalLSTMmodelforsentimentanalysisinsocialbigdata.
Inf.Process.Manag.2021,58,102435.[CrossRef]
11. Edara,D.C.;Vanukuri,L.P.;Sistla,V.;Kolli,V.K.K. Sentimentanalysisandtextcategorizationofcancermedicalrecordswith
LSTM. J.Ambient.Intell.Humaniz.Comput.2023,14,5309–5325.[CrossRef]
12. Lindemann,B.;Maschler,B.;Sahlab,N.;Weyrich,M. AsurveyonanomalydetectionfortechnicalsystemsusingLSTMnetworks.
Comput.Ind.2021,131,103498.[CrossRef]
13. Hua,Y.;Zhao,Z.;Li,R.;Chen,X.;Liu,Z.;Zhang,H. Deeplearningwithlongshort-termmemoryfortimeseriesprediction.
IEEECommun.Mag.2019,57,114–119.[CrossRef]
14. Oruh,J.;Viriri,S.;Adegun,A. Longshort-termmemoryrecurrentneuralnetworkforautomaticspeechrecognition. IEEEAccess
2022,10,30069–30079.[CrossRef]
15. Agarwal,P.;Kumar,S. Electroencephalography-basedimaginedspeechrecognitionusingdeeplongshort-termmemorynetwork.
ETRIJ.2022,44,672–685.[CrossRef]
16. Fang,K.;Kifer,D.;Lawson,K.;Shen,C. Evaluatingthepotentialandchallengesofanuncertaintyquantificationmethodforlong
short-termmemorymodelsforsoilmoisturepredictions. WaterResour.Res.2020,56,e2020WR028095.[CrossRef]
17. Zhang, J.; Wang, P.; Yan, R.; Gao, R.X. Long short-term memory for machine remaining life prediction. J. Manuf. Syst.
2018,48,78–86.[CrossRef]
18. Fernando,T.;Denman,S.;McFadyen,A.;Sridharan,S.;Fookes,C. Treememorynetworksformodellinglong-termtemporal
dependencies. Neurocomputing2018,304,64–81.[CrossRef]
19. Muhuri,P.S.;Chatterjee,P.;Yuan,X.;Roy,K.;Esterline,A.Usingalongshort-termmemoryrecurrentneuralnetwork(LSTM-RNN)
toclassifynetworkattacks. Information2020,11,243.[CrossRef]
20. Bischl, B.; Binder, M.; Lang, M.; Pielok, T.; Richter, J.; Coors, S.; Thomas, J.; Ullmann, T.; Becker, M.; Boulesteix, A.L.; etal.
Hyperparameteroptimization:Foundations,algorithms,bestpractices,andopenchallenges. WIREsDataMin.Knowl.Discov.
2023,13,e1484.[CrossRef]

AI2025,6,215 18of21
21. Kazemi,F.;Asgarkhani,N.;Shafighfard,T.;Jankowski,R.;Yoo,D.Y. Machine-LearningMethodsforEstimatingPerformance
ofStructuralConcreteMembersReinforcedwithFiber-ReinforcedPolymers. Arch. Comput. MethodsEng. 2025,32,571–603.
[CrossRef]
22. Huang, L.; Zhou, X.; Shi, L.; Gong, L. Time Series Feature Selection Method Based on Mutual Information. Appl. Sci.
2024,14,1960.[CrossRef]
23. Alalhareth,M.;Hong,S.C. AnImprovedMutualInformationFeatureSelectionTechniqueforIntrusionDetectionSystemsinthe
InternetofMedicalThings. Sensors2023,23,4971.[CrossRef]
24. Berahmand,K.;Daneshfar,F.;Salehi,E.S.;Li,Y.;Xu,Y. Autoencodersandtheirapplicationsinmachinelearning: Asurvey.
Artif.Intell.Rev.2024,57,28.[CrossRef]
25. Sakib,S.;Mahadi,M.K.;Abir,S.R.;Moon,A.M.;Shafiullah,A.;Ali,S.;Faisal,F.;Nishat,M.M. Attention-BasedModelsfor
MultivariateTimeSeriesForecasting:Multi-stepSolarIrradiationPrediction. Heliyon2024,10,e27795.[CrossRef]
26. Vincent, A.M.; Jidesh, P. An improved hyperparameter optimization framework for AutoML systems using evolutionary
algorithms. Sci.Rep.2023,13,4737.[CrossRef][PubMed]
27. Yang,X.;Li,J.;Jiang,X. Researchoninformationleakageintimeseriespredictionbasedonempiricalmodedecomposition.
Sci.Rep.2024,14,28362.[CrossRef][PubMed]
28. Liu,S.;Zhou,D.J. Usingcross-validationmethodstoselecttimeseriesmodels:Promisesandpitfalls. Br.J.Math.Stat.Psychol.
2024,77,337–355.[CrossRef]
29. Dhake, H.; Kashyap, Y.; Kosmopoulos, P. Algorithms for Hyperparameter Tuning of LSTMs for Time Series Forecasting.
RemoteSens.2023,15,2076.[CrossRef]
30. Purba,M.R.;Akter,M.;Ferdows,R.;Ahmed,F. Ahybridconvolutionallongshort-termmemory(CNN-LSTM)basednatural
languageprocessing(NLP)modelforsentimentanalysisofcustomerproductreviewsinBangla. J.Discret.Math.Sci.Cryptogr.
2022,25,2111–2120.[CrossRef]
31. Su,C.;Huang,H.;Shi,S.;Jian,P.;Shi,X. NeuralmachinetranslationwithGumbelTree-LSTMbasedencoder. J.Vis.Commun.
ImageRepresent.2020,71,102811.[CrossRef]
32. Gondhi,N.K.;Chaahat.;Sharma,E.;Alharbi,A.H.;Verma,R.;Shah,M.A. EfficientLongShort-TermMemory-BasedSentiment
AnalysisofE-CommerceReviews. Comput.Intell.Neurosci.2022,2022,3464524.[CrossRef][PubMed]
33. Al-Smadi,M.;Talafha,B.;Al-Ayyoub,M.;Jararweh,Y. Usinglongshort-termmemorydeepneuralnetworksforaspect-based
sentimentanalysisofArabicreviews. Int.J.Mach.Learn.Cybern.2019,10,2163–2175.[CrossRef]
34. Gandhi,U.D.;MalarvizhiKumar,P.;ChandraBabu,G.;Karthick,G. Sentimentanalysisontwitterdatabyusingconvolutional
neuralnetwork(CNN)andlongshorttermmemory(LSTM). Wirel.Pers.Commun.2021,1–10.[CrossRef]
35. Perez-Castro,A.;Martínez-Torres,M.d.R.;Toral,S. Efficiencyofautomatictextgeneratorsforonlinereviewcontentgeneration.
Technol.Forecast.Soc.Change2023,189,122380.[CrossRef]
36. Hajipoor,O.;Nickabadi,A.;Homayounpour,M.M.GPTGAN:UtilizingtheGPTlanguagemodelandGANtoenhanceadversarial
textgeneration. Neurocomputing2025,617,128865.[CrossRef]
37. Ma,P.;Jiang,B.;Lu,Z.;Li,N.;Jiang,Z. Cybersecuritynamedentityrecognitionusingbidirectionallongshort-termmemorywith
conditionalrandomfields. TsinghuaSci.Technol.2020,26,259–265.[CrossRef]
38. Khalifa,M.;Shaalan,K. CharacterconvolutionsforArabicnamedentityrecognitionwithlongshort-termmemorynetworks.
Comput.SpeechLang.2019,58,335–346.[CrossRef]
39. Santoso,J.;Setiawan,E.I.;Purwanto,C.N.;Yuniarno,E.M.;Hariadi,M.;Purnomo,M.H. Namedentityrecognitionforextracting
conceptinontologybuildingonIndonesianlanguageusingend-to-endbidirectionallongshorttermmemory. ExpertSyst.Appl.
2021,176,114856.[CrossRef]
40. Lyu,C.;Chen,B.;Ren,Y.;Ji,D. Longshort-termmemoryRNNforbiomedicalnamedentityrecognition. BMCBioinform.2017,
18,1–11.[CrossRef]
41. Cheng, Q.; Chen, Y.; Xiao, Y.; Yin, H.; Liu, W. Adual-stageattention-basedBi-LSTMnetworkformultivariatetimeseries
prediction. J.Supercomput.2022,78,16214–16235.[CrossRef]
42. Bukhari,A.H.;Raja,M.A.Z.;Sulaiman,M.;Islam,S.;Shoaib,M.;Kumam,P. Fractionalneuro-sequentialARFIMA-LSTMfor
financialmarketforecasting. IEEEAccess2020,8,71326–71338.[CrossRef]
43. Cao,J.;Li,Z.;Li,J. FinancialtimeseriesforecastingmodelbasedonCEEMDANandLSTM. Phys.AStat.Mech.ItsAppl.2019,
519,127–139.[CrossRef]
44. Qing,X.;Niu,Y. Hourlyday-aheadsolarirradiancepredictionusingweatherforecastsbyLSTM. Energy2018,148,461–468.
[CrossRef]
45. Tukymbekov,D.;Saymbetov,A.;Nurgaliyev,M.;Kuttybay,N.;Dosymbetova,G.;Svanbayev,Y. Intelligentautonomousstreet
lightingsystembasedonweatherforecastusingLSTM. Energy2021,231,120902.[CrossRef]
46. Hossain,M.S.;Mahmood,H. Short-termphotovoltaicpowerforecastingusinganLSTMneuralnetworkandsyntheticweather
forecast. IEEEAccess2020,8,172524–172533.[CrossRef]

AI2025,6,215 19of21
47. Nguyen,H.D.;Tran,K.P.;Thomassey,S.;Hamad,M. ForecastingandAnomalyDetectionapproachesusingLSTMandLSTM
Autoencodertechniqueswiththeapplicationsinsupplychainmanagement. Int.J.Inf.Manag.2021,57,102282.[CrossRef]
48. Ergen,T.;Kozat,S.S. UnsupervisedanomalydetectionwithLSTMneuralnetworks. IEEETrans.NeuralNetw.Learn.Syst.2019,
31,3127–3141.[CrossRef]
49. Wubet,Y.A.;Lian,K.Y.VoiceconversionbasedaugmentationandahybridCNN-LSTMmodelforimprovingspeaker-independent
keywordrecognitiononlimiteddatasets. IEEEAccess2022,10,89170–89180.[CrossRef]
50. Orosoo,M.;Raash,N.;Treve,M.;Lahza,H.F.M.;Alshammry,N.;Ramesh,J.V.N.;Rengarajan,M. TransformingEnglishlanguage
learning:AdvancedspeechrecognitionwithMLP-LSTMforpersonalizededucation. Alex.Eng.J.2025,111,21–32.[CrossRef]
51. Zhao,J.;Mao,X.;Chen,L. Speechemotionrecognitionusingdeep1D&2DCNNLSTMnetworks. Biomed.SignalProcess.Control
2019,47,312–323.
52. Du, X.; Ma, C.; Zhang, G.; Li, J.; Lai, Y.K.; Zhao, G.; Deng, X.; Liu, Y.J.; Wang, H. AnefficientLSTMnetworkforemotion
recognitionfrommultichannelEEGsignals. IEEETrans.Affect.Comput.2020,13,1528–1540.[CrossRef]
53. Guo,A.; Beheshti,R.; Khan,Y.M.; Langabeer,J.R.; Foraker,R.E. Predictingcardiovascularhealthtrajectoriesintime-series
electronichealthrecordswithLSTMmodels. BMCMed.Inform.Decis.Mak.2021,21,5.[CrossRef][PubMed]
54. Yin,J.;Han,J.;Xie,R.;Wang,C.;Duan,X.;Rong,Y.;Zeng,X.;Tao,J. MC-LSTM:Real-time3Dhumanactiondetectionsystemfor
intelligenthealthcareapplications. IEEETrans.Biomed.CircuitsSyst.2021,15,259–269.[CrossRef]
55. Srivastava,S.;Sharma,S.;Tanwar,P.;Dubey,G.;Memoria,M. ImprovingHealthCareAnalytics:LSTMNetworksforEnhanced
RiskAssessment. ProcediaComput.Sci.2025,259,11–22.[CrossRef]
56. Rashid,T.A.;Hassan,M.K.;Mohammadi,M.;Fraser,K. ImprovementofvariantadaptableLSTMtrainedwithmetaheuristic
algorithmsforhealthcareanalysis.InResearchAnthologyonArtificialIntelligenceApplicationsinSecurity;IGIGlobal:Hershey,PA,
USA,2021;pp.1031–1051.
57. Aslan,S.N.;Özalp,R.;Uçar,A.;Güzelis¸,C. NewCNNandhybridCNN-LSTMmodelsforlearningobjectmanipulationof
humanoidrobotsfromdemonstration. Clust.Comput.2022,25,1575–1590.[CrossRef]
58. Molina-Leal,A.;Gómez-Espinosa,A.;EscobedoCabello,J.A.;Cuan-Urquizo,E.;Cruz-Ramírez,S.R. Trajectoryplanningfora
mobilerobotinadynamicenvironmentusinganLSTMneuralnetwork. Appl.Sci.2021,11,10689.[CrossRef]
59. Park,D.;Hoshi,Y.;Kemp,C.C. Amultimodalanomalydetectorforrobot-assistedfeedingusinganlstm-basedvariational
autoencoder. IEEERobot.Autom.Lett.2018,3,1544–1551.[CrossRef]
60. Bin,Y.;Yang,Y.;Shen,F.;Xie,N.;Shen,H.T.;Li,X. Describingvideowithattention-basedbidirectionalLSTM. IEEETrans.Cybern.
2018,49,2631–2641.[CrossRef]
61. Ge, H.; Yan, Z.; Yu, W.; Sun, L. AnattentionmechanismbasedconvolutionalLSTMnetworkforvideoactionrecognition.
Multimed.ToolsAppl.2019,78,20533–20556.[CrossRef]
62. Hussain,T.;Muhammad,K.;Ullah,A.;Cao,Z.;Baik,S.W.;DeAlbuquerque,V.H.C. Cloud-assistedmultiviewvideosummariza-
tionusingCNNandbidirectionalLSTM. IEEETrans.Ind.Inform.2019,16,77–86.[CrossRef]
63. Ullah,A.;Ahmad,J.;Muhammad,K.;Sajjad,M.;Baik,S.W. Actionrecognitioninvideosequencesusingdeepbi-directional
LSTMwithCNNfeatures. IEEEAccess2017,6,1155–1166.[CrossRef]
64. Imrana,Y.;Xiang,Y.;Ali,L.;Abdul-Rauf,Z. AbidirectionalLSTMdeeplearningapproachforintrusiondetection. ExpertSyst.
Appl.2021,185,115524.[CrossRef]
65. Abduljabbar,R.L.;Dia,H.;Tsai,P.W. UnidirectionalandbidirectionalLSTMmodelsforshort-termtrafficprediction. J.Adv.
Transp.2021,2021,5589075.[CrossRef]
66. Huang,C.G.;Huang,H.Z.;Li,Y.F. AbidirectionalLSTMprognosticsmethodundermultipleoperationalconditions. IEEETrans.
Ind.Electron.2019,66,8792–8802.[CrossRef]
67. Mahadevaswamy,U.;Swathi,P. SentimentanalysisusingbidirectionalLSTMnetwork. ProcediaComput.Sci.2023,218,45–56.
[CrossRef]
68. Ma,M.;Liu,C.;Wei,R.;Liang,B.;Dai,J. Predictingmachine’sperformancerecordusingthestackedlongshort-termmemory
(LSTM)neuralnetworks. J.Appl.Clin.Med.Phys.2022,23,e13558.[CrossRef]
69. Ghimire,S.;Deo,R.C.;Wang,H.;Al-Musaylh,M.S.;Casillas-Pérez,D.;Salcedo-Sanz,S. StackedLSTMsequence-to-sequence
autoencoder with feature selection for daily solar radiation prediction: A review and new modeling results. Energies
2022,15,1061.[CrossRef]
70. Wang, J.; Peng, B.; Zhang, X. Using a stacked residual LSTM model for sentiment intensity prediction. Neurocomputing
2018,322,93–101.[CrossRef]
71. Yu,L.;Qu,J.;Gao,F.;Tian,Y. AnovelhierarchicalalgorithmforbearingfaultdiagnosisbasedonstackedLSTM. ShockVib.
2019,2019,2756284.[CrossRef]
72. Sang,S.;Li,L. AnovelvariantofLSTMstockpredictionmethodincorporatingattentionmechanism. Mathematics2024,12,945.
[CrossRef]

AI2025,6,215 20of21
73. Lin,J.;Ma,J.;Zhu,J.;Cui,Y. Short-termloadforecastingbasedonLSTMnetworksconsideringattentionmechanism. Int.J.Electr.
PowerEnergySyst.2022,137,107818.[CrossRef]
74. Xiang,L.;Wang,P.;Yang,X.;Hu,A.;Su,H. FaultdetectionofwindturbinebasedonSCADAdataanalysisusingCNNand
LSTMwithattentionmechanism. Measurement2021,175,109094.[CrossRef]
75. Yang,Y.;Xiong,Q.;Wu,C.;Zou,Q.;Yu,Y.;Yi,H.;Gao,M. AstudyonwaterqualitypredictionbyahybridCNN-LSTMmodel
withattentionmechanism. Environ.Sci.Pollut.Res.2021,28,55129–55139.[CrossRef][PubMed]
76. Ran, X.; Shan, Z.; Fang, Y.; Lin, C. AnLSTM-basedmethodwithattentionmechanismfortraveltimeprediction. Sensors
2019,19,861.[CrossRef][PubMed]
77. Liu,G.;Guo,J. BidirectionalLSTMwithattentionmechanismandconvolutionallayerfortextclassification. Neurocomputing
2019,337,325–338.[CrossRef]
78. Wei,L.;Chen,S.;Lin,J.;Shi,L. EnhancingreturnforecastingusingLSTMwithagent-basedsyntheticdata. Decis.SupportSyst.
2025,193,114452.[CrossRef]
79. Azkue,M.;Miguel,E.;Martinez-Laserna,E.;Oca,L.;Iraola,U. CreatingaRobustSoCEstimationAlgorithmBasedonLSTM
UnitsandTrainedwithSyntheticData. WorldElectr.Veh.J.2023,14,197. [CrossRef]
80. Brophy, E.; Wang, Z.; She, Q.; Ward, T. GenerativeAdversarialNetworksinTimeSeries: ASystematicLiteratureReview.
ACMComput.Surv.2023,55,1–31. [CrossRef]
81. Takahashi,S.;Chen,Y.;Tanaka-Ishii,K. Modelingfinancialtime-serieswithgenerativeadversarialnetworks. Phys.AStat.Mech.
ItsAppl.2019,527,121261.[CrossRef]
82. Chatterjee,S.;Hazra,D.;Byun,Y.C. GAN-basedsynthetictime-seriesdatagenerationforimprovingpredictionofdemandfor
electricvehicles. ExpertSyst.Appl.2025,264,125838.[CrossRef]
83. Deng,F.;Chen,Z.;Liu,Y.;Yang,S.;Hao,R.;Lyu,L. ANovelCombinationNeuralNetworkBasedonConvLSTM-Transformerfor
BearingRemainingUsefulLifePrediction. Machines2022,10,1226. [CrossRef]
84. Bounoua,I.; Saidi,Y.; Yaagoubi,R.; Bouziani,M. DeepLearningApproachesforWaterStressForecastinginArboriculture
UsingTimeSeriesofRemoteSensingImages:ComparativeStudybetweenConvLSTMandCNN-LSTMModels. Technologies
2024,12,77. [CrossRef]
85. daSilva,D.G.;Geller,M.T.B.;dosSantosMoura,M.S.;deMouraMeneses,A.A.PerformanceevaluationofLSTMneuralnetworksfor
consumptionprediction. e-PrimeAdv.Electr.Eng.Electron.Energy2022,2,100030.[CrossRef]
86. Haque, S.T.; Debnath, M.; Yasmin, A.; Mahmud, T.; Ngu, A.H.H. Experimental Study of Long Short-Term Memory and
TransformerModelsforFallDetectiononSmartwatches. Sensors2024,24,6235.[CrossRef][PubMed]
87. Trujillo-Guerrero,M.F.;Román-Niemes,S.;Jaén-Vargas,M.;Cadiz,A.;Fonseca,R.;Serrano-Olmedo,J.J. AccuracyComparisonof
CNN,LSTM,andTransformerforActivityRecognitionUsingIMUandVisualMarkers. IEEEAccess2023,11,106650–106669.
[CrossRef]
88. Curreri,F.;Patanè,L.;Xibilia,M.G. RNN-andLSTM-BasedSoftSensorsTransferabilityforanIndustrialProcess. Sensors2021,
21,823. [CrossRef]
89. Yunita,A.;Pratama,M.I.;Almuzakki,M.Z.;Ramadhan,H.;Akhir,E.A.P.;FirdausiahMansur,A.B.;Basori,A.H. Performance
analysisofneuralnetworkarchitecturesfortimeseriesforecasting: AcomparativestudyofRNN,LSTM,GRU,andhybrid
models. MethodsX2025,15,103462.[CrossRef]
90. CrisóstomodeCastroFilho,H.;AbíliodeCarvalhoJúnior,O.;FerreiradeCarvalho,O.L.;PozzobondeBem,P.;dosSantosde
Moura,R.;OlinodeAlbuquerque,A.;RosaSilva,C.;GuimarãesFerreira,P.H.;FontesGuimarães,R.;TrancosoGomes,R.A. Rice
CropDetectionUsingLSTM,Bi-LSTM,andMachineLearningModelsfromSentinel-1TimeSeries. RemoteSens.2020,12,2655.
[CrossRef]
91. Jiang,J.;Wan,X.;Zhu,F.;Xiang,D.;Hu,Z.;Mu,S. AdeeplearningframeworkintegratingTransformerandLSTMarchitectures
forpipelinecorrosionrateforecasting. Comput.Chem.Eng.2025,109365. [CrossRef]
92. Gao,S.;Chen,M.;Yang,W.;Zhu,H. TFF-TL:TransformerbasedontemporalfeaturefusionandLSTMfordynamicsoftsensor
modelingofindustrialprocesses. J.TaiwanInst.Chem.Eng.2025,176,106328.[CrossRef]
93. Pantopoulou,S.;Cilliers,A.;Tsoukalas,L.H.;Heifetz,A. TransformersandLongShort-TermMemoryTransferLearningfor
GenIVReactorTemperatureTimeSeriesForecasting. Energies2025,18,2286. [CrossRef]
94. Casola,S.;Lauriola,I.;Lavelli,A. Pre-trainedtransformers: Anempiricalcomparison. Mach. Learn. Appl. 2022,9,100334.
[CrossRef]
95. Papa,L.;Russo,P.;Amerini,I.;Zhou,L. ASurveyonEfficientVisionTransformers:Algorithms,Techniques,andPerformance
Benchmarking. IEEETrans.PatternAnal.Mach.Intell.2024,46,7682–7700.[CrossRef][PubMed]
96. Wang,R.;Ma,L.;He,G.;Johnson,B.A.;Yan,Z.;Chang,M.;Liang,Y. TransformersforRemoteSensing:ASystematicReviewand
Analysis. Sensors2024,24,3495. [CrossRef][PubMed]
97. Zhang,N.;Song,Y.;Fang,D.;Gao,Z.;Yan,Y. AnImprovedDeepConvolutionalLSTMforHumanActivityRecognitionUsing
WearableSensors. IEEESens.J.2024,24,1717–1729.[CrossRef]

AI2025,6,215 21of21
98. Khatun,M.A.;Yousuf,M.A.;Ahmed,S.;Uddin,M.Z.;Alyami,S.A.;Al-Ashhab,S.;Akhdar,H.F.;Khan,A.;Azad,A.;Moni,M.A.
DeepCNN-LSTMWithSelf-AttentionModelforHumanActivityRecognitionUsingWearableSensor. IEEEJ.Transl.Eng.Health
Med.2022,10,1–16.[CrossRef]
99. Zhao,Y.;Yang,R.;Chevalier,G.;Xu,X.;Zhang,Z. DeepResidualBidir-LSTMforHumanActivityRecognitionUsingWearable
Sensors. Math.Probl.Eng.2018,2018,7316954.[CrossRef]
100. Wu,Z.;Hu,P.;Liu,S.;Pang,T. AttentionMechanismandLSTMNetworkforFingerprint-BasedIndoorLocationSystem. Sensors
2024,24,1398. [CrossRef]
101. Cao,M.; Yao,R.; Xia,J.; Jia,K.; Wang,H. LSTMAttentionNeural-Network-BasedSignalDetectionforHybridModulated
Faster-Than-NyquistOpticalWirelessCommunications. Sensors2022,22,8992. [CrossRef]
102. Chen,H.;Yang,J.;Fu,X.;Zheng,Q.;Song,X.;Fu,Z.;Wang,J.;Liang,Y.;Yin,H.;Liu,Z.;etal. WaterQualityPredictionBasedon
LSTMandAttentionMechanism:ACaseStudyoftheBurnettRiver,Australia. Sustainability2022,14,13231. [CrossRef]
103. Xie,T.;Ding,W.;Zhang,J.;Wan,X.;Wang,J. Bi-LS-AttM:ABidirectionalLSTMandAttentionMechanismModelforImproving
ImageCaptioning. Appl.Sci.2023,13,7916. [CrossRef]
104. Hassan,N.;Miah,A.;Shin,J. ADeepBidirectionalLSTMModelEnhancedbyTransfer-Learning-BasedFeatureExtractionfor
DynamicHumanActivityRecognition. Appl.Sci.2024,14,603. [CrossRef]
105. Lin,Y.;Zhang,Z.;Tan,Y.;Fu,H.;Min,H. EfficientTD3-basedpathplanningofmobilerobotindynamicenvironmentsusing
prioritizedexperiencereplayandLSTM. Sci.Rep.2025,15,18331.[CrossRef]
106. S.K.B.,S.;Mathivanan,S.K.;Rajadurai,H.;Cho,J.;Easwaramoorthy,S.V. Amulti-modalgeospatial–temporalLSTMbaseddeep
learningframeworkforpredictivemodelingofurbanmobilitypatterns. Sci.Rep.2024,14,31579.[CrossRef]
107. Zhou, H.; Zhao, Y.; Liu, Y.; Lu, S.; An, X.; Liu, Q. Multi-Sensor Data Fusion and CNN-LSTM Model for Human Activity
RecognitionSystem. Sensors2023,23,4750.[CrossRef]
108. Guidotti,R.;Monreale,A.;Ruggieri,S.;Turini,F.;Giannotti,F.;Pedreschi,D. ASurveyofMethodsforExplainingBlackBox
Models. ACMComput.Surv.2018,51,1–42.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.