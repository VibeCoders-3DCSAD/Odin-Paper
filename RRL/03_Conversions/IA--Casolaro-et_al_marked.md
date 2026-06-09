informatio n
Review
Deep Learning for Time Series Forecasting: Advances
and Open Problems
AngeloCasolaro† ,VincenzoCapone† ,GennaroIannuzzo† andFrancescoCamastra*,†
DepartmentofScienceandTechnology,ParthenopeUniversityofNaples,CentroDirezionaleIsolaC4,
80143Naples,Italy;angelo.casolaro001@studenti.uniparthenope.it(A.C.);
vincenzo.capone002@studenti.uniparthenope.it(V.C.);gennaro.iannuzzo001@studenti.uniparthenope.it(G.I.)
* Correspondence:francesco.camastra@uniparthenope.it
† Theseauthorscontributedequallytothiswork.
Abstract:Atimeseriesisasequenceoftime-ordereddata,anditisgenerallyusedtodescribehow
aphenomenonevolvesovertime. Timeseriesforecasting,estimatingfuturevaluesoftimeseries,
allowstheimplementationofdecision-makingstrategies.Deeplearning,thecurrentlyleadingfield
ofmachinelearning,appliedtotimeseriesforecastingcancopewithcomplexandhigh-dimensional
timeseriesthatcannotbeusuallyhandledbyothermachinelearningtechniques. Theaimofthe
workistoprovideareviewofstate-of-the-artdeeplearningarchitecturesfortimeseriesforecasting,
underline recent advances and open problems, and also pay attention to benchmark data sets.
Moreover,theworkpresentsacleardistinctionbetweendeeplearningarchitecturesthataresuitable
forshort-termandlong-termforecasting. Withrespecttoexistingliterature,themajoradvantage
oftheworkconsistsindescribingthemostrecentarchitecturesfortimeseriesforecasting,suchas
GraphNeuralNetworks,DeepGaussianProcesses,GenerativeAdversarialNetworks,Diffusion
Models,andTransformers.
Keywords: short-term forecasting; long-term forecasting; recurrent neural networks; temporal
convolutionalneuralnetworks;graphneuralnetworks;deepgaussianprocesses;transformers;time
seriesbenchmarking;generativeadversarialnetworks;diffusionmodels
Citation:Casolaro,A.;Capone,V.;
Iannuzzo,G.;Camastra,F.Deep
1. Introduction
LearningforTimeSeriesForecasting:
Atimeseriesisasequenceofdataenumeratedintimeorder. Timeseriesareused
AdvancesandOpenProblems.
Information2023,14,598. https:// tostudyhowcertainmeasures,e.g.,airpollutiondata[1],ozoneconcentration[2],plant
doi.org/10.3390/info14110598 growth[3],sunspots[4],DowJonesandNasdaqindices[5],andelectricityconsumption[6],
evolveovertime. Timeseriesforecastingestimatesvaluesthatatimeseriestakesinthe
AcademicEditor:NikosE.
future,allowingtheimplementationofdecision-makingstrategies,e.g.,abandonmentof
Mastorakis
fossilfuelstoreducethesurfacetemperatureoftheEarth. Specifically, timeseriesfore-
Received:26September2023 castingisveryrelevantfortheenergydomain(e.g.,electricityloaddemand[7,8],solarand
Revised:18October2023 windpowerestimation[9,10]),meteorology(e.g.,predictionofwindspeed[11],tempera-
Accepted:2November2023 ture[12,13],humidity[12],precipitation[13,14]),airpollutionmonitoring(e.g.,prediction
Published:4November2023 of PM , PM , NO , O , SO , and CO concentrations [12,15,16]), the finance domain
2.5 10 2 3 2 2
(e.g.,stockmarketindexandsharesprediction[17,18],thestockprice[19,20],exchange
rate[21,22]),health(e.g.,predictionofinfectivediseasesdiffusion[23],diabetesmellitus[24],
bloodglucoseconcentration[25],andcancergrowth[26]),traffic(e.g.,trafficspeedandflow
Copyright: © 2023 by the authors.
prediction[27–30]),andindustrialproduction(e.g.,petroleumproduction[31],remaininglife
Licensee MDPI, Basel, Switzerland.
prediction[23,32,33],industrialprocesses[34],fuelcellsdurability[35],enginefaults[36]).
This article is an open access article
Deeplearningalgorithmsarecurrentlytheleadingmethodsinmachinelearningdueto
distributed under the terms and
theirsuccessfulapplicationtomanycomputersciencedomains(e.g.,computervision,natural
conditionsoftheCreativeCommons
Attribution(CCBY)license(https:// languageprocessing,speechrecognition). Inrecentyears,therehasbeenagrowthofinterestin
creativecommons.org/licenses/by/ theapplicationofdeeplearningtotimeseriesforecasting,duetodeeplearning’scapability
4.0/). tograspthenonlinearrelationsamonginputdata(i.e.,timeseriessamples). Tothebest
Information2023,14,598.https://doi.org/10.3390/info14110598 https://www.mdpi.com/journal/information

Information2023,14,598 2of35
ofourknowledge,thereareseveralreviewsondeeplearningfortimeseriesforecasting
(e.g.,[37–43]),buttheyhavethefollowingmajorshortcomings: theylackadescriptionof
Transformeranditsvariants; theydonotprovideacleardistinctionbetweenmodelsfor
short-termandlong-termforecasting,therearenosectionsonshort-termandlong-term
forecasting benchmarks; they do not cover the most recent deep learning strategies for
short-term forecasting (e.g., Graph Neural Networks, Deep Gaussian Processes, Generative
AdversarialNetworks,andDiffusionModels). Theaimofthisworkistoprovideacomprehen-
sivesurveyofrecentdeeplearningapproachesfortimeseriesforecasting,underliningthe
advancesandtheopenproblemsforeachrevieweddeeplearningarchitecture. Specifically,
thesurveyfocusesonworksaboutmachinelearningappliedtotimeseriesforecastingthat
arenotolderthan2016, forthesakeoflength. Thepaperisorganisedinthefollowing
sections: inSection2,thefoundationsofdeterministictimeseriesareintroduced;Section3
describesdeeplearningarchitecturesforshort-termforecasting,i.e.,ConvolutionalNeural
Networks,TemporalConvolutionalNetworks,RecurrentNeuralNetworks(RNNs),GraphNeural
Networks, Deep Gaussian Processes, Generative Adversarial Networks, and Diffusion Models;
Section4discusseslong-termforecastingarchitectures, i.e., theTransformerarchitecture
anditstimeseries-basedvariants;Section5reviewsotherheterogeneousarchitecturesfor
bothshort-termandlong-termforecasting;benchmarkingforshort-termandlong-term
timeseriesforecastingispresentedinSection6;inSection7,someconclusionsaredrawn
andfuturepossibledevelopmentsarediscussed;finally,intheappendixarereportedthe
main mathematical notation used in the work and a description of the main diffusion
modelfoundations.
2. DeterministicTimeSeries
Atimeseriesiscalledaunivariatetimeseriesifallitssamplesarescalar;otherwise,ifall
samplesarevectors,itiscalledamultivariatetimeseries. Atimeseriesisdefinedasstationary
whenthedynamicalprocessthatgenerateditdoesnotchangeovertime,otherwise,itis
non-stationary. Adeterministicstationarytimeseriesx ,witht =1,...,L,canbedescribedby
t
anautoregressivemodelasfollows:
x t+p = f(x t−1 ,...,x t−q )+(cid:101) t+p ∀p ∈ [0,P] (1)
where f(·) and q are called skeleton and model order of time series, i.e., how many past
samplesarerequiredtomodelthetimeseriesadequately,respectively,and(cid:101) t+p represents
anindeterminablepartoriginatedeitherfromunmodeleddynamicsoftheprocessorfrom
realnoise. Pdefinesthepredictionlength,i.e.,howmanyfuturesamplesshouldbepredicted.
Figure1givesagraphicalrepresentationofanautoregressivemodel.
X ... X X X
0 t-2 t-1 t
+ ε
f
X ... X X X X
0 t-2 t-1 t t+1
Figure1.Anexampleofanautoregressivemodelforforecastingbasedondeterministicstationary
timeseries. Inthefigure,themodelorderisq = 2andthepredictionlengthisP = 0(i.e.,itisa
one-stepaheadforecastingproblem).

Information2023,14,598 3of35
IfP =0,theautoregressivemodeldefinestheso-calledone-stepaheadforecasting,other-
wise,apredictionlengthP >0specifiesamulti-stepaheadforecastingproblem. Moreover,
multi-stepaheadforecastingcanbefurtherdividedintoshort-termandlong-termforecasting.
Intheliterature,thetypicalthresholdvalueofpredictionlengthPbetweenshort-termand
long-termforecastingrangesbetween2and48[44]. Finally,forthesakeofclarity,inthis
work,one-stepaheadforecastingisincludedinshort-termforecasting.
3. DeepLearningModelsforShort-TermForecasting
In short-term forecasting, the skeleton of time series can be approximated by the
followingdeeplearningmodels,whicharedescribedbelow. Thesectionisorganisedas
follows. Firstly, Convolutional Neural Networks (Section 3.1), and Temporal Convolutional
Networks(Section3.1.2)areintroduced. Furthermore,RecurrentNeuralNetworks(Section3.2)
aredescribed,includingElmanRNNs(Section3.2.1),EchoStateNetworks(Section3.2.3),Long
Short-TermMemory(Section3.2.4),andGatedRecurrentUnits(Section3.2.5). Successively,
hybridsandvariants(Section3.3)oftheaforementionedarchitecturesarebrieflyreviewed.
Moreover,GraphNeuralNetworks(Section3.4),DeepGaussianProcesses(Section3.5),and
generative models (Section 3.6), i.e., Generative Adversarial Networks (Section 3.6.1) and
DiffusionModels(Section3.6.3),arediscussed. Finally,foreachreviewedmodel,drawbacks
andlimitationsarediscussedinpropersections.
3.1. ConvolutionalNeuralNetworks
ConvolutionalNeuralNetworks(CNNs)[45],asshowninFigure2,haveadeeparchi-
tecture generally formed by convolution, pooling, and fully connected layers. CNNs have
threemainpeculiarities: localconnectivity,sharedweightsandtranslationequivariance. Local
connectivityresidesineachCNNneuronbeingconnectedonlytoitsexclusiveinputregion,
theso-calledreceptivefield. Besides,theneuronsofagivenlayersharethesameweight
matrix. TranslationequivarianceistheabilityofCNNstodetectcertainpatterns,regardless
of the position they have in the input image. 1D convolution (see Figure 3) of an input
sequenceX = [x ,...,x ]withagivenkernelwwithsizeqisdefinedas:
1 L
q/2
∑
y(t) = (w∗X)(t) = w(a)X(t−a) ∀t ∈ [1,...,L] (2)
a=−q/2
Itisworthwhiletoremarkthatintheautoregressiveapproach,thekernelsizeqcorresponds
tothemodelorder,generallyfixedusingmodelselectiontechniques(e.g.,cross-validation)[46].
Moreover,CNNcanstackdifferentconvolutionallayersinordertotransformtheinput
data(i.e.,thepasttimeseriesvalues)intoamoresuitablehigher-levelrepresentationfor
theforecastingtask. CNNtimeseriesforecastingapplicationsaredescribedinTable1.
Figure2.AnexampleofConvolutionalNeuralNetworkappliedtotimeseriesforecasting.Thered,
theblueandthegreenboxesrepresentCNN’sconvolutionallayers.

Information2023,14,598 4of35
Output Length
|     | . . . yt yt+1 | . . . |     | Output Sequence |     |     |     |
| --- | ------------- | ----- | --- | --------------- | --- | --- | --- |
Kernel (size=3)
| . . . | xt-1 xt xt+1xt+2 | . . . |     |     |     |     |     |
| ----- | ---------------- | ----- | --- | --- | --- | --- | --- |
Input Sequence
Input Length
Figure3.Exampleof1Dconvolutionusingakernelwithsizek=3.Thescalarproductisdenotedby
•.Theyellowboxesdenotethelearnedkernel.
Table1.RecentapplicationsontimeseriesforecastingusingConvolutionalNeuralNetworks.
| Ref. |     |     | Year |     |                                    | Application                  |     |
| ---- | --- | --- | ---- | --- | ---------------------------------- | ---------------------------- | --- |
| [47] |     |     | 2017 |     |                                    | ETFsprices                   |     |
| [48] |     |     | 2018 |     |                                    | Electricityconsumption       |     |
| [10] |     |     | 2018 |     |                                    | Solarpowerandelectricityload |     |
| [6]  |     |     | 2018 |     |                                    | Electricityconsumption       |     |
| [7]  |     |     | 2018 |     |                                    | Electricityprice             |     |
| [49] |     |     | 2019 |     | Electricitypriceandloadforecasting |                              |     |
| [50] |     |     | 2019 |     |                                    | Building-levelload           |     |
| [12] |     |     | 2023 |     |                                    | CO 2 /Temperature/Humidity   |     |
3.1.1. ShortcomingsofConvolutionalNeuralNetworks
ThemajordrawbackofCNNsfortimeseriesforecastingistheuseofEuclideanker-
nels[51],sinceonlyacontinuousandcommonlyshorttimeseriessubsequenceisconsidered
atatimebyanEuclideankernel. However,intimeseriesforecastingtasksitmaybeuse-
fultoextractrepresentativefeaturesbyanalysingnon-contiguousandfarthertimeseries
samplesinthepast. ThislimitationisovercomebyTemporalConvolutionalNetworks(see
Section3.1.2),withtheuseofcausalanddilatedconvolutions,andbyGraphNeuralNetworks
(seeSection3.4),withaproperlydesignedadjacencymatrix.
3.1.2. TemporalConvolutionalNetworks
Temporal Convolutional Networks (TCNs) were proposed for action segmentation and
detectionbyLeaetal.[52]. Inanutshell,aTCNiscomposedofcascaded1Dconvolutional
layersthatallowmappingarbitrarilylonginputsontooutputsequencesofthesamelength.
IncontrasttotraditionalCNNs,TCNsperformcausalanddilatedconvolutions. Unlike1D
convolution(seeEquation(2)),incausal1Dconvolution(seeFigure4)theoutputelement
at time t is yielded by the convolution between the kernel and past input elements only,
namely[x ,x ,...,x ],whereqisthekernelsizethatcorrespondstothemodelorder
| t−1 | t−2 t−q |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- |
inanautoregressiveapproach(seeSection3.1). Indetail,causal1Dconvolutionisdefined
asfollows:
q
∑
|     | y(t) = (w∗X)(t) |     | =   | w(a)X(t−a) |     | ∀t ∈ [1,...,L] | (3) |
| --- | --------------- | --- | --- | ---------- | --- | -------------- | --- |
a=1
A dilated 1D convolution (see Figure 5) differs from a 1D convolution due to the in-
troduction of a dilation factor d. The dilation, applied to convolution, is equivalent to
consideringafixedstepbetweentwoadjacentkernelelements. Inparticular,dilatedcausal
1Dconvolutioncanbedefinedas:
q
∑
|     | y(t) = (w∗X)(t) |     | =   | w(a)X(t−d·a) |     | ∀t ∈ [1,...,L] | (4) |
| --- | --------------- | --- | --- | ------------ | --- | -------------- | --- |
a=1

Information2023,14,598 5of35
Whend =1,adilated1Dconvolutionisreducedtoa1Dconvolution.
Dilatedconvolutions
allowthenetworkstohavealargereceptivefield,i.e.,tocaptureinformationintothefar
past,byalogarithmicgrowthofthenumbergofconvolutionallayers,asstatedin:
|     |     |     | (cid:24) | (cid:18)(n−1)(b−1) |       |     | (cid:19)(cid:25) |     |
| --- | --- | --- | -------- | ------------------ | ----- | --- | ---------------- | --- |
|     |     |     | g = log  |                    |       | +1  |                  | (5) |
|     |     |     |          | b                  | (q−1) |     |                  |     |
wherebisthelogarithmicbaseofthedilationfactord forthei-thconvolutionallayer(namely,
i
d = bi). TCNtimeseriesforecastingapplicationsarereportedinTable2.
i
|              |     | y y          | . . .         | y       | Output Sequence |     |     |     |
| ------------ | --- | ------------ | ------------- | ------- | --------------- | --- | --- | --- |
|              |     | 1 2          |               | L       |                 |     |     |     |
| 0            | 0   | x 1 x 2      | . . . x L-2 x | L-1 x L | Input Sequence  |     |     |     |
| Zero Padding |     | Input Length |               |         |                 |     |     |     |
Figure4.Causal1Dconvolutionwithakernelofsizeq=3.Zeropaddingelementsareaddedatthe
beginningoftheinputsequenceinordertohaveanoutputsequencewiththesamelengthasthe
inputsequence.
Output Sequence
ConvLayer2
(d2=22=4)
0
| Zero |     |     |     |     | ConvLayer1 |     |     |     |
| ---- | --- | --- | --- | --- | ---------- | --- | --- | --- |
Padding
(d1=21=2)
ConvLayer0
(d0=20=1)
Input Sequence
Figure5.Exampleofadilatedcausal1Dconvolutionwiththreelayersusingadilationbaseb=2
andakernelsizeq=3.Zeropaddingisusedtopreservetheinputsequencelength.
Table2.TimeseriesforecastingapplicationsusingTemporalConvolutionalNetworks.
|     | Ref. |     | Year |     |     |     | Application |     |
| --- | ---- | --- | ---- | --- | --- | --- | ----------- | --- |
|     | [53] |     | 2018 |     |     |     | Stockmarket |     |
|     | [15] |     | 2019 |     |     |     | BeijingPM   |     |
2.5
|     | [30] |     | 2019 |     |                                      |                     | Traffic   |     |
| --- | ---- | --- | ---- | --- | ------------------------------------ | ------------------- | --------- | --- |
|     | [54] |     | 2020 |     | Nationalelectricdemandandpowerdemand |                     |           |     |
|     | [9]  |     | 2020 |     |                                      | Windpowergeneration |           |     |
|     | [55] |     | 2020 |     |                                      |                     | Weather   |     |
|     | [11] |     | 2022 |     |                                      |                     | Windspeed |     |
TCNssharewithCNNsmostshortcomings(seeSection3.1.1),withtheonlyexception
oftheEuclideankernel.

Information2023,14,598 6of35
3.2. RecurrentNeuralNetworks
RecurrentNeuralNetworks(RNNs)[45]aimtoexploretherelationsbetweenthecurrent
timeseriessamplesandthepastones. AnRNNprocessesonetimeseriessampleatatime
f(·)
to approximate the skeleton and determine the model order q implicitly. While in
Equation(1)themodelorderqisassumedtobeconstant,RNNsexhibitadynamictemporal
behaviour,astheydonotrequireafixedmodelorderqandtheyauto-determinehowfar
back to look in the past. An RNN is composed of recurrent layers, which process one
inputsampleatatime. TheearliestRNNapplicationsfortimeseriesforecasting[56,57]are
replacedbymorespecificandsophisticatedrecurrentarchitectures,thatis,ElmanRecurrent
NeuralNetworks[58],EchoStateNetworks[59],LongShort-TermMemoryNetworks[60],and
GatedRecurrentUnits[61].
3.2.1. ElmanRecurrentNeuralNetworks
Elman[58],Williams-Zipser[62],andJordan[63]RNNsaretheearliestRecurrentNeural
Networksproperlydesignedtohandletemporalpatternsintimeseries.Inparticular,Elman
(cid:126)
RNN(ERNN)usesarecurrentlayer,whichyieldsanoutputh thatdependsonthecurrent
t
(cid:126)
sample(cid:126)x t andthepreviousoutput h t−1 byafunctiong(·)andagenericsetoftime-shared
parametersω,asdescribed:
|     |     | (cid:126) | (cid:126)         |     |     |
| --- | --- | --------- | ----------------- | --- | --- |
|     |     | h =       | g ((cid:126)x , h | )   | (6) |
|     |     | t         | ω t t−1           |     |     |
(cid:126)
whereh isproducedbythesamerecurrentlayer,i.e.,:
t−1
|     |     | (cid:126) |                     | (cid:126) |     |
| --- | --- | --------- | ------------------- | --------- | --- |
|     |     | h t−1 =   | g ω ((cid:126)x t−1 | , h t−2 ) | (7) |
andsoon. Thebasicrecurrentlayer,oftencalledavanillacell,workslikeafullyconnected
layer with a fixed number of units, jointly applied to the current input(cid:126)x and the last
t
(cid:126)
outputh t−1 :
|     |     | (cid:16)  |                    | (cid:17)   |     |
| --- | --- | --------- | ------------------ | ---------- | --- |
|     |     | (cid:126) | (cid:126)          | +(cid:126) |     |
|     |     | h t = g   | V(cid:126)x t +W h | t−1 b      | (8) |
In this case, the set of parameters of a recurrent layer is ω = {V,W, (cid:126) b}, where V is the
(cid:126)
input-recurrentweightmatrix,W istherecurrent-recurrentweightmatrix,andbisthebias
InEquation(8),g(·)isanonlinearactivationfunction,usuallyahyperbolictangent.
vector.
ERNNtimeseriesforecastingapplicationsaresummarisedinTable3.
Table3.ElmanRNNapplicationsfortimeseriesforecasting.
| Ref. | Year |     |     | Application          |     |
| ---- | ---- | --- | --- | -------------------- | --- |
| [64] | 2017 |     |     | Electricityload      |     |
| [65] | 2018 |     |     | Electricityload      |     |
| [66] | 2018 |     |     | Energyconsumption    |     |
| [14] | 2019 |     |     | Monthlyprecipitation |     |
| [16] | 2021 |     |     | AirQualityIndex      |     |
3.2.2. ShortcomingsofRecurrentNeuralNetworks
Recurrent neural networks based on the vanilla cell suffer from unstable training,
which prevents the network from grasping long-term dependencies. Recurrent networks,
like most neural networks, are trained by gradient descent [67], and backpropagation [67]
(Backpropagation is denoted Backpropagation Through Time (BPTT), when applied to re-
currentneuralnetworks)isusedtocomputethegradientofthelossfunctionw.r.t. the
network’sweights. Whenback-propagationisappliedtodeepnetworks,theproblemsof
vanishingorexplodinggradients[45]mayarise. Astheerrorgradientisback-propagated,
someofitscomponentsmighteithergetverysmall, givinganegligiblecontributionto
thecorrespondingweightupdate,orverylarge,leading,inthisway,tounstabletraining.
Overtheyears,severalapproacheshavebeenproposedtocopewithunstablegradients.

Information2023,14,598 7of35
Amongthemostsuccessfulapproachesarereservoircomputingmethods,e.g.,EchoStateNet-
works[59](seeSection3.2.3),andgatedcells,e.g.,LongShort-TermMemory(LSTM)cells[60]
andGatedRecurrentUnits(GRU)[61]. Agatedcellcontrolshowmuchinputinformation
flowsthroughthelayerandpreventsderivativesfromvanishingorgettinglarge.
3.2.3. EchoStateNetworks
EchoStateNetworks(ESNs)weresuggestedbyH.Jaeger[59]in2001asavariantof
ERNNs. ESNsarereallyeffectiveindealingwithchaoticmultivariatetimeseries[68]. Inaddi-
tion,thesenetworksmitigatetheunstablegradientproblemandaremorecomputationally
efficientduetotheuseoffixed,randomweightmatricesfortherecurrentlayers. Basedon
thevanillacellofERNNs(seeEquation(8)),ESNsavoidbackpropagationontherecurrent
layerbysettingV andW asfixed(i.e.,non-trainable)randommatrices. Furthermore,a
givensparsitylevelisconsideredinmatrixW. Althoughrandommatricesareanadvantage
ofENSstomitigatetheunstablegradientproblem,they,atthesametime,representamajor
ESNsshortcomingsincetheymakeparticularlydifficulttheapplicationofcommoninter-
pretabilityapproaches,e.g.,gradient-basedapproaches[69,70]. ESNtimeseriesforecasting
applicationsaredescribedinTable4.
Table4.ESNapplicationsontimeseriesforecasting.
| Ref. | Year |                                       | Application                   |     |
| ---- | ---- | ------------------------------------- | ----------------------------- | --- |
| [71] | 2017 |                                       | Fuelcellvoltageageing         |     |
| [32] | 2017 |                                       | Healthofautomotivebatteries   |     |
| [72] | 2017 |                                       | Sluggingflowphenomenon        |     |
| [13] | 2017 |                                       | Temperature/Rainfall          |     |
| [73] | 2018 |                                       | Lorenz/Rossler/Sunspot-Runoff |     |
| [34] | 2019 |                                       | Industrialprocesses           |     |
| [35] | 2019 |                                       | Fuelcelldurability            |     |
| [74] | 2019 |                                       | Photovoltaicvoltage           |     |
| [75] | 2020 |                                       | Electricityload               |     |
| [76] | 2020 |                                       | Electricityload               |     |
| [77] | 2020 | Energyconsumption/Windpowergeneration |                               |     |
| [78] | 2020 |                                       | Temperatureofexhaustgas       |     |
| [36] | 2020 |                                       | Faultsinairplaneengines       |     |
| [79] | 2020 |                                       | Multipletimeseries            |     |
| [25] | 2020 |                                       | Bloodglucoseconcentration     |     |
| [80] | 2021 |                                       | Multipletimeseries            |     |
| [81] | 2021 |                                       | Electricalload                |     |
| [16] | 2021 |                                       | AirQualityIndex               |     |
| [82] | 2022 |                                       | Chaotictimeseries             |     |
3.2.4. LongShort-TermMemory
LongShort-TermMemory(LSTM)Networks[60]wereoriginallyproposedfornatural
languagemodelling. TheLSTMcell(seeFigure6)usesthreegatingmechanisms: input,forget
andoutputgates. Firstly,theinputofLSTMlayers,whichiscomposedofthecurrentinput
| (cid:126)x (cid:126) |     |     |     |     |
| -------------------- | --- | --- | --- | --- |
t andtheoutput h t−1 fromthelasttimestepareiscombinedintothecurrentinputvector
(cid:126)
i asfollows:
t
|     | (cid:126) = | γ(W (cid:126)x +U | (cid:126) +(cid:126) ) |     |
| --- | ----------- | ----------------- | ---------------------- | --- |
|     | i t         | i t               | i h t−1 b i            | (9) |
where γ(·) can be any sigmoidal function (e.g., logistic or hyperbolic tangent ones) and
(cid:126)
{W,U, b}isasetofparameters. Furthermore,thethreegatesarecomputedas:
i i i
|     |              |                   | (cid:126) +(cid:126) |      |
| --- | ------------ | ----------------- | -------------------- | ---- |
|     | (cid:126)g = | σ(W (cid:126)x +U | h b )                | (10) |
|     | t            | g t               | g t−1 g              |      |
|     | (cid:126)    |                   | (cid:126) +(cid:126) |      |
|     | f =          | σ(W (cid:126)x +U | h b )                | (11) |
|     | t            | f t               | f t−1 f              |      |

Information2023,14,598 8of35
(cid:126) +(cid:126)
|     |     | (cid:126)o = | σ(W (cid:126)x +U | h     | b ) | (12) |
| --- | --- | ------------ | ----------------- | ----- | --- | ---- |
|     |     | t            | o t               | o t−1 | o   |      |
(cid:126)
whereσ(·)isthelogisticfunction,(cid:126)g t , f t ,(cid:126)o t aretheinput,forget,andoutputgates,respec-
| {W (cid:126) | }, {W | (cid:126) | }, {W (cid:126) | }   |     |     |
| ------------ | ----- | --------- | --------------- | --- | --- | --- |
tively, and g ,U g , b g f ,U f , b f o ,U o , b o are the respective sets of parameters.
|     | inner | state(cid:126)c |     |     | (cid:126) i |     |
| --- | ----- | --------------- | --- | --- | ----------- | --- |
Furthermore, the LSTM’s t is updated by a linear combination of t and the
| previousinnerstate(cid:126)c | :   |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | --- | --- |
t−1
|                                        |     |              | (cid:12)(cid:126)                              | (cid:126)                  |                              |      |
| -------------------------------------- | --- | ------------ | ---------------------------------------------- | -------------------------- | ---------------------------- | ---- |
|                                        |     | (cid:126)c t | =(cid:126)g t i t +                            | f t (cid:12)(cid:126)c t−1 |                              | (13) |
| where(cid:12)istheelement-wiseproduct. |     |              |                                                |                            | (cid:126)                    |      |
|                                        |     |              | Finally,theoutput                              |                            | h t ofaLSTMlayerisdefinedas: |      |
|                                        |     |              | (cid:126) =(cid:126)o (cid:12) tanh((cid:126)c | )                          |                              |      |
|                                        |     |              | h t t                                          | t                          |                              | (14) |
| x t                                    | i t |              |                                                |                            |                              |      |
Input
| h t-1 |     |     | c t |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- |
tanh
| x          | g   |     |       |     |     |     |
| ---------- | --- | --- | ----- | --- | --- | --- |
| t          | t   |     |       |     |     |     |
| Input Gate |     |     | c t-1 |     |     |     |
h
t-1
h t
| x   | f   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| t   | t   |     |     |     |     |     |
Forget Gate
h
t-1
| x   | o   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| t   | t   |     |     |     |     |     |
Output Gate
h
t-1
Figure6.Long-ShortTermMemorycellarchitecture.
LSTMtimeseriesforecastingapplicationsaredescribedinTable5.
Table5.LSTMapplicationsontimeseriesforecasting.
| Ref.    |     | Year |     |                              | Application               |     |
| ------- | --- | ---- | --- | ---------------------------- | ------------------------- | --- |
| [17]    |     | 2016 |     |                              | Stockmarket               |     |
| [83]    |     | 2016 |     |                              | Electricityload           |     |
| [84]    |     | 2016 |     |                              | Trafficflow               |     |
| [19]    |     | 2017 |     |                              | Stockprices               |     |
| [85,86] |     | 2017 |     |                              | Stockmarket               |     |
| [87]    |     | 2017 |     |                              | Electricityload           |     |
| [88]    |     | 2017 |     |                              | Airquality                |     |
| [26]    |     | 2018 |     |                              | ForecastingCancerGrowth   |     |
| [89,90] |     | 2018 |     |                              | Stockmarket               |     |
| [20]    |     | 2018 |     |                              | Stockprices               |     |
| [7]     |     | 2018 |     |                              | Electricityprice          |     |
| [24]    |     | 2018 |     |                              | Diabetesmellitus          |     |
| [91]    |     | 2018 |     |                              | Rainfall-runoffmodelling  |     |
| [92]    |     | 2018 |     |                              | Predictingwatertabledepth |     |
| [93,94] |     | 2018 |     |                              | Electricityload           |     |
| [33]    |     | 2018 |     |                              | Lifepredictionofbatteries |     |
| [10]    |     | 2018 |     | Solarpowerandelectricityload |                           |     |
| [95]    |     | 2018 |     |                              | Solarintensity            |     |
| [96]    |     | 2018 |     |                              | Airquality                |     |
| [97]    |     | 2019 |     |                              | UCIdatasets               |     |
| [98]    |     | 2019 |     |                              | Buildingload              |     |
| [31]    |     | 2019 |     |                              | Petroleumproduction       |     |
| [14]    |     | 2019 |     |                              | Monthlyprecipitation      |     |
| [99]    |     | 2019 |     |                              | Weatherforecasting        |     |

Information2023,14,598 9of35
Table5.Cont.
|     | Ref.  |     | Year |     |                                 | Application           |     |     |
| --- | ----- | --- | ---- | --- | ------------------------------- | --------------------- | --- | --- |
|     | [18]  |     | 2020 |     |                                 | Stockmarket           |     |     |
|     | [100] |     | 2020 |     |                                 | COVID-19              |     |     |
|     | [79]  |     | 2020 |     |                                 | Multipletimeseries    |     |     |
|     | [101] |     | 2021 |     | Weather/AirQuality/Clinicaldata |                       |     |     |
|     | [16]  |     | 2021 |     |                                 | AirQualityIndex       |     |     |
|     | [102] |     | 2022 |     |                                 | Financialmarkets      |     |     |
|     | [12]  |     | 2023 |     | CO                              | /Temperature/Humidity |     |     |
2
3.2.5. GatedRecurrentUnits
RNNs based on Gated Recurrent Units (GRUs) [61] were introduced for Statistical
Machine Translation. A GRU layer, as shown in Figure 7, uses two gating mechanisms:
an update and a reset gate. Both the reset and the update gate depend on(cid:126)x and (cid:126) h .
t t−1
AnalogouslytoLSTM,theresetgate(cid:126)r andtheupdategate(cid:126)u arecomputedas:
|     |     |     |                | t               |                        | t        |     |      |
| --- | --- | --- | -------------- | --------------- | ---------------------- | -------- | --- | ---- |
|     |     |     |                | (cid:16)        | (cid:126) +(cid:126)   | (cid:17) |     |      |
|     |     |     | (cid:126)r = σ | W (cid:126)x +U | h                      | b        |     | (15) |
|     |     |     | t              | r t             | r t−1                  | r        |     |      |
|     |     |     | (cid:16)       |                 |                        | (cid:17) |     |      |
|     |     |     | (cid:126)u = σ | W (cid:126)x +U | (cid:126) h +(cid:126) | b        |     | (16) |
|     |     |     | t              | u t             | u t−1                  | u        |     |      |
whereσ(·)isthelogisticfunctionandtherestoftheparametershavethesamemeaningas
theLSTM(seeSection3.2.4). Furthermore,anintermediateoutput (cid:126) h(cid:48) isgivenby:
t
|     |     |     | (cid:16)                   |                           |                     | (cid:17)      |     |      |
| --- | --- | --- | -------------------------- | ------------------------- | ------------------- | ------------- | --- | ---- |
|     |     |     | (cid:126) h (cid:48) =tanh | W(cid:126)x +U((cid:126)r | (cid:12)(cid:126) h | )+(cid:126) b |     | (17) |
|     |     |     | t                          | t                         | t t−1               |               |     |      |
(cid:126)
where {W,V, b} is an additional set of parameters and (cid:12) is the element-wise product.
|     |     | (cid:126) |     |     |     |     | (cid:126) h(cid:48) (cid:126) |     |
| --- | --- | --------- | --- | --- | --- | --- | ----------------------------- | --- |
Finally, the output h t of the GRU layer is given by the sum of and h t−1 , weighted
t
element-wisebytheupdategate:
|     |     |     | (cid:126)     | (cid:12)(cid:126)         | )(cid:12)(cid:126) | (cid:48) |     |      |
| --- | --- | --- | ------------- | ------------------------- | ------------------ | -------- | --- | ---- |
|     |     |     | h =(cid:126)u | h +((cid:126)e−(cid:126)u |                    | h        |     | (18) |
|     |     |     | t t           | t−1                       | t                  | t        |     |      |
where(cid:126)eisacolumnvectorwhoseelementsareallequalto1.
GRUtimeseriesforecasting
applicationsaredescribedinTable6.
h
t-1
u
t
Update Gate
| x   |     | u   |     |     |     |     | h   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t   |     | t   |     |     |     |     | t   |     |
e-u
|       | e   |     | t   |     |      |     |     |     |
| ----- | --- | --- | --- | --- | ---- | --- | --- | --- |
| h t-1 |     |     |     |     | h' t |     |     |     |
r
t
|     |     | Reset Gate |     | tanh |     |     |     |     |
| --- | --- | ---------- | --- | ---- | --- | --- | --- | --- |
h
t-1
x
t
Figure7.ArchitectureofaGRUcell.Thecolumnvector(cid:126)eiscomposedofelementsthatareallequalto1.

Information2023,14,598 10of35
Table6.ApplicationsontimeseriesforecastingusingGRU-basedRecurrentNeuralNetworks.
Ref. Year Application
[84] 2016 Trafficflow
[8] 2017 Electricityload
[103] 2018 Photovoltaicforecasting
[7] 2018 Electricityprice
[24] 2018 Diabetesmellitus
[97] 2019 UCIdatasets
[79] 2020 Multipletimeseries
[104] 2021 Airquality/Stockprices/Householdelectricpower
3.2.6. ShortcomingsofLSTMsandGRUs
It has to be remarked that, even if training is stable, it can be hard for recurrent
networkstolearndependenciesbetweendistantsequencesamples.Forinstance,arecurrent
networkthatgeneratesanoutputsequencestartingfromaninputsequenceisshownin
Figure8.
y19 y20 y21 y59 y60 y61
OUT Layer OUT Layer OUT Layer OUT Layer OUT Layer OUT Layer
h19 h20 h21 h59 h60 h61
Recurrent Recurrent Recurrent Recurrent Recurrent Recurrent
Layer Layer Layer Layer Layer Layer
. . . . . . . . .
x19 x20 x21 x59 x60 x61
Figure8. Theredpathintherecurrentmodeldenotestheflowthatinformationaboutaninput
sample(x )mustfollowbeforereachinganoutputlayer(y )thatmightrequireit.
20 60
Supposingthattheoutputelementatpositiont =60hasastrongdependencyonthe
inputatpositiont = 20,informationabouttheinputsample x isusefultopredictthe
20
outputsampley . Theoutputsampley ispredictedstartingfromh ,alossysummary
60 t t
ofthepastinputsyieldedbytherecurrentlayer;hence,theonlywayfortheoutputlayer
to know about x is through h . The recurrent layer first captures information about
20 60
x throughh ,whichhastopassbymanystepsandthenaggregateinformationabout
20 20
manyotherinputelements,beforeachievingh . Thereisnoguaranteethataftersomany
60
recurrentsteps,adequateinformationaboutx ispreservedintoh . Infact,h mayjust
20 60 60
containinformationaboutthemostrecentsamplesandhavenoinformationaboutx atall.
20
Theshort-termmemoryofrecurrentnetworksisoneoftheirmajordrawbacksandoneof
themainreasonswhyattentionmechanismsandTransformerswereoriginallyintroduced
indeeplearning(seeSection4.1).
3.3. HybridsandVariantsofDeepNeuralNetworks
Inrecentyears,specificdeepneuralnetworkshavebeenproposedashybridsorvariants
oftheaforementionedarchitectures.Hybridmodelscombinemultiplestatisticalormachine
learningmethodstoimprovetherobustnessandaccuracyofforecasting. Towardsthesame
goalaretheworksthatproposevariantsofdeepneuralarchitecturesproperlyadapted
fortimeseriesforecastingtasks. Hybridsandvariantsofdeepneuralnetworkssharethe
same limitations as the models they are based on. The most successful approaches are
summarisedinTable7.

Information2023,14,598 11of35
Table7.Applicationsintimeseriesforecastingusingvariantsandhybridsofcommondeepneural
networks.Thesymbol‘+’denotesacombinationofmultiplemodelsormethodologies.GARCHand
ANNacronymstandforGeneralizedAutoRegressiveConditionalHeteroskedasticity[105]andArtificial
NeuralNetworks,respectively.
| Ref. Year  |     | Architecture     |     |     |     | Application       |     |
| ---------- | --- | ---------------- | --- | --- | --- | ----------------- | --- |
| [106] 2016 |     | Autoencoder+LSTM |     |     |     | Solarpower        |     |
| [107] 2017 |     | Autoencoder+LSTM |     |     |     | Stockprices       |     |
| [108] 2017 |     | CNN+LSTM         |     |     |     | Stockprices       |     |
| [109] 2018 |     | CNN+LSTM         |     |     |     | Electricityprices |     |
| [110] 2018 |     | CNN+LSTM         |     |     |     | Electricityload   |     |
| [111] 2018 |     | CNN+LSTM         |     |     |     | Windspeed         |     |
LSTM+Attentionmechanism
| [112] 2018 |     |     |     |     |     | Stockmarket |     |
| ---------- | --- | --- | --- | --- | --- | ----------- | --- |
(seeSection4.1.1)
| [113] 2018 |     | LSTM+GRU     |     |     |     | Stockprices          |     |
| ---------- | --- | ------------ | --- | --- | --- | -------------------- | --- |
| [114] 2018 |     | GARCH+LSTM   |     |     |     | Stockprices          |     |
| [115] 2018 |     | GRUvariant   |     |     |     | Trafficforecasting   |     |
| [116] 2018 |     | CNN+LSTM     |     |     |     | PM 2.5 concentration |     |
| [117] 2018 |     | ANN+LSTM+CNN |     |     |     | PM concentration     |     |
2.5
LSTM+Attentionmechanism
| [118] 2019 |     |     |     |     | OnlineSales/Electricityprices |     |     |
| ---------- | --- | --- | --- | --- | ----------------------------- | --- | --- |
(seeSection4.1.1)
LSTM+Attentionmechanism
| [119] 2019 |     |     |     |     |     | Solargeneration |     |
| ---------- | --- | --- | --- | --- | --- | --------------- | --- |
(seeSection4.1.1)
LSTM+Attentionmechanism
| [120] 2019 |     |     |     |     |     | Electricityload |     |
| ---------- | --- | --- | --- | --- | --- | --------------- | --- |
(seeSection4.1.1)
CNN+Attentionmechanism
| [27] 2019 |     |     |     |     |     | Traffic/Stockmarket |     |
| --------- | --- | --- | --- | --- | --- | ------------------- | --- |
(seeSection4.1.1)
| [121] 2020 |     | CNN+LSTM        |     |     |     | Stockmarket/Temperature |     |
| ---------- | --- | --------------- | --- | --- | --- | ----------------------- | --- |
| [122] 2020 |     | LSTM+FuzzyLogic |     |     |     | COVID-19                |     |
| [23] 2020  |     | TCN+Attention   |     |     |     | RemainingUsefulLife     |     |
| [123] 2023 |     | TCN+LSTM/GRU    |     |     |     | ChaoticTimeSeries/ECG   |     |
3.4. GraphNeuralNetworks
Arecentpromisingresearchdirectioninmultivariatetimeseriesforecastingisthe
applicationofGraphNeuralNetworks(GNNs)[124,125]. TheoriginaldomainofGNNsis
thehandlingofspatialdependenciesamongentitiesinagraph-modelledproblem. Indetail,
GNNscanbeusedtogeneraterepresentationsofsuchentitiesthatdependonthestructure
ofthegraphandonanyadditionalinformation. AgraphG(cid:48) isformallydefinedasatuple
| G(cid:48) = [V,E], | V   |     |     | E   |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- | --- |
where denotes the set of nodes and is the set of edges, the connections
betweenthenodesofthegraph,represented,inthiscase,withanadjacencymatrix. The
definition of this matrix is based on a metric function that can be either a priori fixed or
learned during the training process [125]. The basic idea of a GNN can be summarised
bytheuseofthreemainoperators: aggregate,combine,andreadout. Thek-thGNNlayer
performstheaggregateandcombinesoperators. Theformerconsistsofagglomerating,
foreachgraphnodev ∈ V,informationfromitsneighbourhood N(v)asdefinedbythe
adjacencymatrix:
|     | (cid:126) | aggregate((cid:126) hk−1 |     |         |     |     |      |
| --- | --------- | ------------------------ | --- | ------- | --- | --- | ---- |
|     |           | hk =                     | : u | ∈ N(v)) | ∀k  | >1  | (19) |
|     |           | N(v)                     | u   |         |     |     |      |
where (cid:126) hk−1isthefeaturevectoroftheu-thneighbouringnodeofv,yieldedbytheprevi-
u
(cid:126)
ousGNNlayer k−1, and hk istheaggregatedinformation. Thelattercombinesthe
N(v)
|                       |     | (cid:126) hk         |     | (cid:126) hk−1ofthecurrentnodev: |     |     |     |
| --------------------- | --- | -------------------- | --- | -------------------------------- | --- | --- | --- |
| aggregatedinformation |     | withthefeaturevector |     |                                  | v   |     |     |
N(v)
|     |     | (cid:126) combine((cid:126) hk−1, | (cid:126) |     |        |     |      |
| --- | --- | --------------------------------- | --------- | --- | ------ | --- | ---- |
|     |     | hk =                              | hk        | )   | ∀k >1. |     | (20) |
|     |     | v                                 | v N(v)    |     |        |     |      |

Information2023,14,598 12of35
Whenk =1theaggregateoperatorisnotdefined,whereasthecombineoperatorreducesto:
|     | (cid:126) h1 | =(cid:126)x |     |      |
| --- | ------------ | ----------- | --- | ---- |
|     |              | v v ,       |     | (21) |
where(cid:126)x representstheinputfeaturevectorassociatedtothev-thnode. Furthermore,the
v
readoutoperatorisappliedontheoutputofthelastGNNlayerKinordertoobtainafinal
| (cid:126) representingthewholegraphG(cid:48) |     | = [V,E]: |     |     |
| -------------------------------------------- | --- | -------- | --- | --- |
vector h G
|     | (cid:126) h =readout((cid:126) | h K : v ∈ | V)  | (22) |
| --- | ------------------------------ | --------- | --- | ---- |
|     | G                              | v         |     |      |
Inthecaseofmultivariatetimeseriesforecasting,GNNshavebeensuccessfullyappliedas
featureselectionmechanisms. ItisimportanttoremarkthatGNNscouldalsobeappliedto
spatio-temporaltimeseriesforecastingwhichisnottheobjectofthesurvey. GNNtimeseries
forecastingapplicationsaredescribedinTable8.
Table8.GNNapplicationsontimeseriesforecasting.
| Ref. Year  |                                                  | Application            |     |     |
| ---------- | ------------------------------------------------ | ---------------------- | --- | --- |
| [28] 2020  | Traffic/Electricityload/Exchangerate             |                        |     |     |
| [29] 2021  | Solarenergy/Traffic/Electricityload/Exchangerate |                        |     |     |
| [126] 2022 |                                                  | Stockmarket            |     |     |
| [127] 2022 | PM                                               | 2.5 /Traffic/Windspeed |     |     |
| [128] 2022 |                                                  | Stockmarket            |     |     |
| [129] 2022 | Electricityload/Solarenergy/Traffic              |                        |     |     |
[21] 2022 Solarenergy/Windpowergeneration/Electricityload/Exchangerate
| [130] 2022 | Solarenergy/Traffic/Electricityload/Exchangerate |     |     |     |
| ---------- | ------------------------------------------------ | --- | --- | --- |
| [22] 2023  | Solarenergy/Traffic/Electricityload/Exchangerate |     |     |     |
3.5. DeepGaussianProcesses
Let D = (x(cid:126) ,x(cid:126) ,...,x(cid:126) ) be a data set and Y = (y(cid:126) ,y(cid:126) ,...,y(cid:126) ) the target output, a
| 1 2 | n   |     | 1 2 n |     |
| --- | --- | --- | ----- | --- |
GaussianProcess[131]isaBayesianmodelcomposedofacollectionofrandomvariables,
any finite number of which have a joint Gaussian distribution, and it is fully defined
by a mean function m((cid:126)x ) and covariance function k((cid:126)x,(cid:126)x ), which is usually a Mercer
| i   |     |     | i j |     |
| --- | --- | --- | --- | --- |
kernel[131,132]. TheanalyticalsolutionofaGaussianProcessentailscomputingtheinverse
ofthecovariancematrixofobservations,whichhasacomputationalcomplexityofO(n3).
A common approach for coping with this computational drawback is the use of Sparse
GaussianProcess[133]. Thismethodconsistsofconsideringareducedsetof m (m (cid:28) n)
trainingsamples,theso-calledinducingvariables,reducing,inthisway,thecomplexityto
O(nm2). AsequenceofGaussianProcessesdefinesaBayesianmodelcalledDeepGaussian
Process (DGP) [134]. As shown in Figure 9, in DGPs the output of the single Gaussian
ProcesslocatedatthepreviouslayerisfedasaninputtotheGaussianProcesslocatedat
thenextlayer. Unliketherestofthedeeplearningtechniques,DeepGaussianProcesses
canestimatenotonlythevalueoffuturetimeseriessamplesbutalsoprovideaconfidence
intervalofthepredictivetimeseriesvaluerepresenting,inthisway,theuncertaintyofthe
model. DGPtimeseriesforecastingapplicationsaredescribedindetailinTable9.
Table9.DGPapplicationsontimeseriesforecasting.
| Ref.  | Year |     | Application                   |     |
| ----- | ---- | --- | ----------------------------- | --- |
| [135] | 2017 |     | CropYieldforecasting          |     |
| [136] | 2020 |     | CropYieldforecasting          |     |
| [137] | 2022 |     | Electricityload               |     |
| [138] | 2023 |     | Car-hailingdemand             |     |
| [139] | 2023 |     | Ozoneconcentrationforecasting |     |

Information2023,14,598 13of35
Figure9.DeepGaussianProcesses.InthefigureX,Y representthedatasetandthedesiredoutput,
respectively, f(i)isthelatentfunctiontobeestimatedandm,k representthemeanandcovariance
i i
functionofi-thlayer.
3.6. GenerativeModels
Amongthelatesttrendsindeeplearningresearch,therearetheso-calledgenerative
models, specifically Generative Adversarial Networks (GANs) and Diffusion Models (DMs).
Both families are popular for their groundbreaking capabilities in generating synthetic
images. ThesesuccessesencouragedresearcherstoapplyGANsandDMstosequential
dataaswell,includingtimeseries. Asgenerativemodels,bothmethodologieshavebeen
usedfortimeseriesgenerationtasks. However,itcanadaptthemforothertimeseries-related
tasksaswell,specificallytimeseriesforecasting. Sections3.6.1and3.6.2provideanoverview
ofGANsandtheirusagefortimeseriesforecasting,respectively;Sections3.6.3and3.6.4
discussdiffusionmodelsandtheirapplicationstotimeseriesforecasting,respectively.
3.6.1. GenerativeAdversarialNetworks
A GAN [140] is composed of two separate artificial neural networks: a generator
networkGthatgeneratessyntheticdata,withthesamedistributionoftheinputones,and
adiscriminatornetworkDthatclassifiesinputdataaseitherrealorsynthetic. GandDare
trainedwithanadversarialtrainingapproach. G takesrandomnoiseasinputandithas
totransformthenoiseintoasyntheticdatasamplefollowingthesamedistributionofthe
realdata. Dreceivesbothrealandgeneratedsamplesanditestimatestheprobabilitythat
anygivendatasamplecomesfromtherealdataratherthanfromthegenerator. Thetwo
networksaretrainedjointlywithaminimaxtwo-playergame[140],i.e.,thediscriminator
istrainedtomaximisethecorrectclassificationratioforbothrealandgeneratedsamples.
Whereas,thegeneratorhasthegoaltotrickthediscriminatorintomisclassifyinggenerated
samplesbyminimisingthecorrectclassificationratio. Thistrainingprocedureisexpressed
bytheobjectivefunction:
minmaxV(D,G) =E [logD((cid:126)x)]+E [log(1−D(G((cid:126)z)))]. (23)
G D
(cid:126)x∼px ((cid:126)x) (cid:126)z∼pz ((cid:126)z)
where,(cid:126)x isarealdatapoint, sampledfromtherealdatadistribution p ((cid:126)x);(cid:126)z isanoise
x
vector,sampledfromadistribution p ((cid:126)z),apriorifixed;D((cid:126)x)istheprobabilitydistribution
z
estimatedbythediscriminator;G((cid:126)z)isthesampleproducedbythegenerator,startingfrom
thenoise(cid:126)z. GANscanbeimplementedbyanyneuralarchitectureforthegeneratorand
thediscriminator. Forinstance,GandDcanbeimplementedbyMLPs[67],asoriginally
proposedin[140],CNNs(seeSection3.1),withsomearchitecturalconstraintstostabilise
thetrainingprocedure[141],orLSTM(seeSection3.2.4)networks[142].

Information2023,14,598 14of35
3.6.2. GenerativeAdversarialNetworksinTimeSeriesForecasting
Inliterature,therearetwomainapproachesforusingGANsintimeseriesforecast-
ing: asdataaugmentationorasanend-to-endforecastingmodel. Intheformercase,GANs
generate synthetic time series in a given domain (e.g., financial or health-related time
series) in order to augment the original small data set. The augmented data set, with
bothrealandgeneratedtimeseries,isthenusedtotrainatraditionalforecastingmodel,
e.g., a model based on an LSTM network. In the latter case, the forecasting model is a
GANitself,anditgeneratesfuturesamplesstartingfrompreviousonesand,eventually,
otherexogenousinputs(Intimeseriesforecasting,avariableissaidtobeexogenousifit
is not a time series sample, but it can still affect the time series samples. For instance,
temperature may be an exogenous variable in rainfall time series forecasting) [143]. For
example,in[144]aGANisfirstlyusedtoaugmentabuildingenergyconsumptiondataset
andthen,anensembleoffivetraditionalpredictivemodelsistrainedonsuchaugmented
data set. In particular, to augment the data set, Conditional GANs (CGANs) [145] and
InformationMaximisingGANs(InfoGANs)[146]arecomparedwitheachother. Similarly,
in[147]COVID-19epidemicdataisgeneratedbyacustomGANwithanLSTMgenerator
andanMLPdiscriminator.Furthermore,aTransformerisusedtomakeaforecastingmodel
trainedontheGAN-augmenteddataset. Moreover,someGAN-basedmodelshavebeen
specificallydevelopedfortimeseriesgeneration,e.g.,QuantGAN[148],forfinancialtime
series with long-term time dependencies, SynSigGAN [149], for continuous biomedical
signals,RecurrentConditionalGANs(RCGANs)[150],formedicaldata,TimeGAN[151],a
frameworkfordomain-agnostictimeseriesgeneration,ConditionalSig-WassersteinGAN
(Sig-WCGAN) [152], and TTS-GAN [153], entirely based on Transformers. Some of the
aforementionedGANs,e.g.,RCGAN,TimeGAN,Sig-WCGAN,areconditionalGANs[145],
i.e,timeseriesarenotgeneratedfromonlyrandomnoisebutalsoconditionedonthereal
timeseriesand/orrelatedinformation,e.g.,exogenousinputs,forimprovinggenerated
timeseriesquality. TheuseofconditionalGANsispopularforend-to-endforecasting,
wherethegeneratedtimeserieswindow,typicallyintheshort-termfuture,isoftencon-
ditioned on previous samples and on other exogenous inputs (see [154–158]). Table 10
collectssomeworksonGANapplicationsfortimeseriesforecasting.
Table10.GANapplicationsontimeseriesforecasting.
| Ref.  | Year |                                             | Application         |
| ----- | ---- | ------------------------------------------- | ------------------- |
| [159] | 2018 |                                             | Stockmarket         |
| [160] | 2019 |                                             | Trafficforecasting  |
| [154] | 2019 | Lorenz/Mackey-Glass/InternetTrafficdata     |                     |
| [161] | 2019 |                                             | Medicineexpenditure |
| [162] | 2019 |                                             | Electricityload     |
| [163] | 2020 |                                             | Stockprice          |
| [164] | 2020 | Long-termbenchmarkdatasets(seeSection6.2)   |                     |
| [165] | 2020 |                                             | Soiltemperature     |
| [166] | 2021 | Stockmarket/Energyproduction/EEG/Airquality |                     |
| [156] | 2021 |                                             | InternetTrafficdata |
[167] 2021 StoreItemDemand/InternetTraffic/Meteorologicaldata
| [168]     | 2021 |     | Windpower/Solarpower    |
| --------- | ---- | --- | ----------------------- |
| [144]     | 2021 |     | Energyconsumption       |
| [169]     | 2021 |     | Electricityload         |
| [170]     | 2022 |     | Trajectoriesforecasting |
| [147,155] | 2022 |     | COVID-19                |
| [157,158] | 2022 |     | Photovoltaicpower       |
| [171]     | 2022 |     | Buildingpowerdemand     |
| [172]     | 2023 |     | Financialtimeseries     |

Information2023,14,598 15of35
3.6.3. DiffusionModels
A new family of generative architectures are the diffusion models. They have been
showingcutting-edgeperformanceingeneratingsamplesthatreflecttheobserveddata
indifferentdomains,e.g.,imagegeneration,videogeneration,andtextsynthesis. Three
key formulations are used to develop diffusion-based approaches for short-term time
series applications: denoising diffusion probabilistic models (DDPMs) [173,174], score-
basedgenerativemodels(SGMs)[175],andstochasticdifferentialequations(SDEs)[176].
DiffusionmodelsaimtoapproximateagenerativeprocessG thatgeneratesnewsamples
drawn from an underlying distribution q(x), given some observed data x from the same
distribution. ToapproximateG,intheforwardprocess,aprogressiveinjectionofGaussian
noisesontheobserveddataisperformedbythemajorityofdiffusionmodels. Furthermore,
areverseprocessisapplied,byalearnabletransitionkernel,toreconstructtheoriginal
data. Mostdiffusionmodelsassumethat,afterafinitenumberofnoiseinjectionsteps,q(x)
distributionoftheobserveddatawillbecomeaGaussiandistribution. Therefore,thegoal
ofdiffusionmodelsistofindtheprobabilisticprocessP thatapproximatesq(x)distribution
oforiginaldatafromtheGaussiandistribution. Inthismanner,anysampleofGaussian
distributioncanbetransformedbyP intoanewsampleofq(x)distributionofobserved
datax. Theprincipleofdiffusionmodelsistoprogressivelyperturbtheobserveddatax
witharandomnoisebyaforwarddiffusionprocess F beforerecoveringtheoriginaldata
usingabackwardreversediffusionprocessB. AdeepneuralnetworkisusedintheBprocess
toapproximatetheamountofnoisethatmustberemovedinthedenoisingstepstorecover
theoriginaldata. Forthesakeofreadability,thetheoreticalfoundationsofdiffusionmodels
andtheirmainarchitecturesareomittedinthesectionandmovedinAppendixB,whereas
thediffusionmodelsforshort-termtimeseriesforecastingaredescribedinthefollowing
subsection.
3.6.4. DiffusionModelsinShort-TermTimeSeriesForecasting
Inrecentyears,severaldiffusion-basedapproachesfortimeseriesforecastinghave
been proposed. They are based on the three predominant methods of diffusion model
describedinAppendixB.Thefirstprominentdiffusionmodelarchitecturefortimeseries
forecastingisTimeGrad[177],whichisaDDPMvariant. TheforwardprocessofTimeGrad
injectsnoisesintodataateachpredictivesample,andthendenoisesgraduallythroughthe
backwardprocessconditionedonprevioustimeseriessamples. Forencodingtheprevious
timeseriessamples,TimeGradusesanRNNarchitecture,e.g.,LSTM(seeSection3.2.4)or
GRU(seeSection3.2.5),TheobjectivefunctionofTimeGradisrepresentedbyanegative
log-likelihood,denotedas:
T
∑ −logp θ (x t 0|h t−1 ), (24)
t=t0
where[t ,T]isthepredictionlength. TheEquation(24)canbereformulatedconsideringthe
0
lowerbound:
E k,x0,(cid:101) [δ(k)||(cid:101) − (cid:101) θ ( (cid:112) a˜ k x t 0 + (cid:112) 1−a˜ k (cid:101),h t−1 ,k)||2]. (25)
t
Theparametersθareestimatedduringthetraining,minimisingthenegativelog-likelihood
objectivefunctionwithastochasticsampling. Furthermore,futuretimeseriessamplesare
generatedwithastep-by-stepprocedure. Theobservationforthenextsamplesattime
T+1ispredictedinasimilarwayasDDPM(seeAppendixB).Similarly,theScoreGrad
model [178], based on the same target distribution of TimeGrad, defines a continuous
diffusionprocessusingSDEs(seeAppendixB).ScoreGradconsistsoftwomodules: the
former is a feature extraction module (e.g., an RNN) almost identical to TimeGrad, or an
attention-basednetwork,e.g.,Transformer(seeSection4.1),forcomputingthehiddenstate

Information2023,14,598 16of35
h
t ofprevioustimesamples,thelatterisaconditionalSDE-basedscore-matchingmodule.
TheobjectivefunctionofScoreGradiscomputedasfollows:
T
∑
|     |     |     |     |     | L (θ), |     |     |     | (26) |
| --- | --- | --- | --- | --- | ------ | --- | --- | --- | ---- |
t
t=t0
withL t (θ)being:
|     | E       | [δ(k)||s | (xk,h | ,k) | − ∇ | logq  | (x |x0)||2]. |     | (27) |
| --- | ------- | -------- | ----- | --- | --- | ----- | ------------ | --- | ---- |
|     | k,x0,xk |          | θ     | t t |     | xk ok | t t          |     |      |
|     |         | t t      |       |     |     | t     |              |     |      |
Itisworthwhiletoremarkthat,inEquation(27),thegeneralformulationofSDEshasbeen
usedforthesakeofsimplicity. Recently,timeseriesresearchhaspaidattentiontoavoiding
model overfitting phenomena in the forecasting of short time series. D3VAE [179], tries to
addresstheproblemofshorttimeseries,applyingacoupleddiffusionprocessfortimeseries
dataaugmentation,andthenitperformsabidirectionalautoencoder(BVAE),asascoremodel.
Moreover,D3VAEtakesintoaccountthedecouplingoflatentvariablesbyreducingtotal
correlationtoimprovepredictioninterpretabilityandstability. Furthermore,theobjective
functionofD3VAEincludesthemeansquareerror(MSE),whichhighlightstherequirement
ofsupervision,amongtheforecastandcurrentsamplesinthepredictionwindow. Unlike
TimeGrad,D3VAEinjectsnoisesseparatelyintotheprevioussamples(context)x0 and
1:t0 −1
thepredictionwindowx0
bythecoupleddiffusionprocess:
t0:T
|     |     |      |      | (cid:112)     |         | (cid:112)    |              |     |      |
| --- | --- | ---- | ---- | ------------- | ------- | ------------ | ------------ | --- | ---- |
|     |     | xk   | =    | a˜ x0         | +       | 1−a˜         | (cid:101),   |     | (28) |
|     |     | 1:t0 | −1   | k             | 1:t0 −1 |              | k            |     |      |
|     |     |      |      | (cid:113)     |         | (cid:113)    |              |     |      |
|     |     | xk   | =    | a˜(cid:48) x0 | +       | 1−a˜(cid:48) |              |     |      |
|     |     |      | t0:T | k             | t0:T    |              | k (cid:101), |     | (29) |
where(cid:101)indicatesthestandardGaussiannoise. Shorttimeseriesforecastingbenefitsthe
simultaneousimprovementofthecontextandpredictionwindowprovidedbythediffusion
process. TheB processismadeupoftwosteps. Theformerforecastsxk withaBVAE
t0:T
model,consideringthecontextxk . Thelatterdenoisestheoutputx˜k ofBVAEwitha
|     |     |     | 1:t0 −1 |     |     |     |     | t0:T |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | ---- | --- |
denoisingscorematchingmodule,asfollows:
|     |     | xk   | ← x˜k | −σ2∇ |     | E(x˜k | ;e), |     | (30) |
| --- | --- | ---- | ----- | ---- | --- | ----- | ---- | --- | ---- |
|     |     | t0:T |       | t0:T | 0 k | t0:T  |      |     |      |
x˜ t 0:T
whereE(x˜k ;e)istheenergyfunction. TheobjectivefunctionofD3VAEiscomposedof
t0:T
fourlosses,thatcanbewrittenasfollows:
|     | λ D (q(xk |      | ||p (x˜k | ))   | + λ L | +   | λ L + | L , | (31) |
| --- | --------- | ---- | -------- | ---- | ----- | --- | ----- | --- | ---- |
|     | 1 KL      | t0:T | θ        | t0:T | 2 DSM |     | 3 TC  | MSE |      |
whereλ ,λ ,λ aretheregularisationparametersofdivergencebetweentargetdistributionand
1 2 3
distributionofpredictionwindow,denoisingscorematchingobjective,andtotalcorrelationamong
latentvariables,respectively. Diffusionmodelsfortimeseriesforecastingaresummarisedin
Table11.
Table11.Recentdiffusionmodelsfortimeseriesforecasting.
| Ref.  |     |     |     |     | Year |     |     | Model     |     |
| ----- | --- | --- | --- | --- | ---- | --- | --- | --------- | --- |
| [177] |     |     |     |     | 2021 |     |     | TimeGrad  |     |
| [178] |     |     |     |     | 2021 |     |     | ScoreGrad |     |
| [180] |     |     |     |     | 2022 |     |     | DSPD      |     |
D3VAE
| [179] |     |     |     |     | 2022 |     |     |     |     |
| ----- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
4. DeepLearningModelsforLong-TermForecasting
Inlong-termforecasting,theskeletonofatimeseriescanbeapproximatedbyusing
theTransfomerarchitecture. Firstly,theoriginalTransformerarchitecture(Section4.1)is

Information2023,14,598 17of35
describedandattentionmechanismsarepresented(Sections4.1.1and4.1.2). Furthermore,
themainlimitationsofTransformersarediscussed(Section4.1.3)andvariantsofTransformer,
properly designed to cope with long-term time series forecasting tasks, e.g., Informer,
Autoformer,FEDFormerandCrossformer,arepresented(Section4.1.4).
4.1. Transformers
TheTransformer[181]isadeep-learningarchitectureborrowedfromNaturalLan-
guageProcessing.Itcanbedescribedas:“amodelarchitectureeschewingrecurrenceandrelying
entirelyonattentionmechanismstodrawglobaldependenciesbetweeninputandoutput”[181].
TheTransformerarchitecturewasproposedtoovercomethemaindrawbacksofrecurrent
models(seeSections3.2.2and3.2.6)withsequencemodellingtasks:
1. Theoutputstateh t ofarecurrentlayerattimetdependsonthestateh t−1 ,produced
attheprevioustimestep. Thisinherentsequentialnatureprohibitstheintra-sequence
parallelismofrecurrentnetworks.
2. Recurrentnetworkscannotgenerallylearnrelationshipsbetweensequencesofdistant
samples,sinceinformationmustfirstpassthroughalldatasamplesinbetween(see
Figure8).
ThestandardTransformerfollowsageneralencoder-decoderarchitectureforsequence-
to-sequencetransduction,asshowninFigure10.
Intimeseriesforecasting,theTransformer’sinputisatime-orderedsequenceofpast
samplesX = [(cid:126)x ,(cid:126)x ,...,(cid:126)x ]whereListhesequencelengthand(cid:126)x ∈Rdisthei-thsampleofa
1 2 L i
d-dimensionalmultivariatetimeseries.Duetotheuseofattentionmechanisms,Transformers
makenoassumptiononanyintrinsictemporalorspatialorderingofinputelements,namely
inputsareseenasasetofsamplesratherthanorderedsequencesofsamples. Ifthereisa
relevantinputorderingforthemodellingtask,e.g.,timeseriesforecasting,theordering
shouldbeencodedintheinputembedding. InTransformers,thisiscommonlyachievedby
summingapositionalembeddingE tothemainsampleembeddingF(X)[181]:
pos
input = F(X)+E (32)
pos
wherethematrix(Differentlyfromwhatappearsinsomemachinelearningpapers,the
moreprecisetensorproductnotationisusedinthewholeworkforrepresentingmatrices)
F(X) ∈RL⊗RD representsaprojectionoftheinputsequenceinahigherD-dimensional
space (D > d). In time series forecasting, a 1D convolutional layer is commonly used
with D learnedkernels, asdescribedinSection3.1, inordertoextracta D-dimensional
representationforeachsampleinX [181–184]. E caneitherbealearnedembeddingor
pos
afixedembedding. Anaivesolution,yeteffective,consistsofusingasinusoidalposition
encoding[181]. However,intimeseriesforecasting,otherpositionalembeddingscanbe
usedaswell,e.g.,temporal-basedembeddings[182–184]. Theencoderandthedecodercan
havetwodifferentseparatedembeddings,ortheycansharethesameembeddingifinput
andoutputsamplesbelongtothesameset. Intimeseriesforecasting,theencoderinputis
thecompletesequenceofpastsamplesX,whilethedecoderinputiscommonlycomposed
ofthemostrecentpartof X (e.g., thesecondhalfof X, i.e., [(cid:126)x L/2 ,(cid:126)x L/2+1 ,...,(cid:126)x L ])anda
zero-vector whose length is equal to prediction length P, see Equation (1). The encoder
anddecoderarecomposedofN andN stackedlayers,respectively(seeFigure10). The
e d
outputofalayeristheinputforthenextlayer. Eachencoderlayerhastwosublayers: a
self-attentionlayer,thatrelateseachinputsamplewiththerestofthesamples,andashallow
feed-forwarddenselayer,sharedalongthesequenceaxis,thatworksasanonlinearprojection
layer.Tofostergradientpropagationandtraining,eachsublayer’sinputisaddedtoitsown
outputwitharesidualconnection[185],andlayernormalization[186]isusedtonormalise
thesamplesoftheresultingsequenceintoanormaldistributionwithalearnedmeanand
standard deviation. Each decoder layer follows the same overall structure of a generic
encoderlayer,butithasoneadditionalsublayer. Thefirstsublayerimplementsaparticular
kindofself-attentionmechanism,theso-calledcausal(ormasked)self-attention[181]. Itworks

Information2023,14,598 18of35
similarlytotheencoderlayer’sself-attention,aseachinputsampleisrelatedtotheothers
inthedecoder’sinputsequence,butitalsousesmaskingtopreventfuturesamplesfrom
being considered when the processing of the current sample occurs. Furthermore, the
outputofthecausalself-attentionsublayerisrelatedtotheencoder’shiddenrepresentation
(thatis,theoutputofthefinalencoderlayer)byacross-attentionlayer. Asinencoderlayers,
aMulti-LayerPerceptron[67]withonehiddenlayerisusedforprojectingnonlinearlythe
outputofcross-attention. Moreover,eachsublayeriswrappedbyaresidualconnection
followedbylayernormalization. Finally,theoutputofthelastdecoderlayerisfedtoafinal
predictionlayer.
Output Probabilities
softmax
Dense Layer
Add & Norm
Feed-Forward
|     | Add & Norm |     | Add & Norm |     |     |     |
| --- | ---------- | --- | ---------- | --- | --- | --- |
N d
Decoder
|     | Feed-Forward |     | Cross-Attention | Layers |     |     |
| --- | ------------ | --- | --------------- | ------ | --- | --- |
N e
K V Q
Encoder
Layers
|     | Add & Norm     |     | Add & Norm |     |     |     |
| --- | -------------- | --- | ---------- | --- | --- | --- |
|     | Self-Attention |     | Causal     |     |     |     |
Self-Attention
|                      | K V              | Q            | K V              | Q                |     |     |
| -------------------- | ---------------- | ------------ | ---------------- | ---------------- | --- | --- |
| Positional           |                  | + Positional | +                |                  |     |     |
| Encoding             |                  | Encoding     |                  |                  |     |     |
|                      | D-dimensional    |              | D-dimensional    |                  |     |     |
|                      | Embedding Module |              | Embedding Module |                  |     |     |
| En c o d e r  In put |                  |              |                  | De c o d e r  In | put |     |
|                      | xi,1 xi,2        | xi,3 xi,L1   | xi,1 xi,2 xi,3   | xi,L2            |     |     |
| S e q u e n ce       |                  |              |                  | S e q u e n      | ce  |     |
Figure 10. Transformer architecture. On the left side, the encoder processes an input sequence,
producingahiddenrepresentation.Ontherightside,thedecoderusestheencoder’soutputtogenerate
theoutputsequence.Thedecoderworksinanautoregressiveway,consumingpastgeneratedsamples
asadditionalinputstogeneratethenextoutputsample.
4.1.1. AttentionMechanisms
ThemostimportantcomputationalblocksofaTransformerareattentionmechanisms,
that allow the model to focus its attention on specific parts of the input, depending on
theinformationbeingprocessed. Amongvariousdefinitionsofattention,Transformers
adopt the so-called scaled dot-product attention, which is very similar to multiplicative at-
tention [187]. Attention mechanisms operate on the following elements: a set of queries
∈RM⊗RDk
Q thatrepresentstheinformationbeingprocessedbythemodel,andsetsof
keysK ∈RN⊗RDk andvaluesV ∈RN⊗RDv,whereDk andDv denotethedimensionof
spacewherequeries,keysandvaluesareprojected. Moreover,Ndenotesthecardinalityof
bothkeysandvalues,while Misthecardinalityoftheinputqueries. TheoutputYforall
queriesiscomputedasfollows:
(cid:32) (cid:33)
QK(cid:62)
|     |     | Y =Attention(K,V,Q) |     | =softmax | √ V | (33) |
| --- | --- | ------------------- | --- | -------- | --- | ---- |
D k
∈RM⊗RDv
TheattentionoutputY isamatrixwhosei-throwcontainstheoutputvector
forthei-thquery. NotethatthesoftmaxinEquation(33)isappliedrow-wisetoitsinput
matrix.Wheredothesequeries,keysandvaluescomefrom?Firstofall,keysandvaluesareoften
thesamevectors,i.e.,avaluevectorcoincideswithitskey. Furthermore,asdescribedin
Section4.1,theTransformerperformsattentionintwoways,self-attentionandcross-attention.

Information2023,14,598 19of35
Inself-attention,queriesandvaluesarethesamevectors;incross-attentionqueriescome
fromthepreviousdecodersublayer,whilekeyandvaluevectorsaregivenbytheencoder’s
hiddenrepresentation.
4.1.2. Multi-HeadAttention
Multi-HeadAttention(MHA)isamoreadvancedversionoftheaforementionedscaled
dot-productattention. Asdiscussedin[181],thescaleddot-productattentionpermitsa
networktoattendoverasequence. However,oftentherearemultipledifferentaspectsa
sequenceelementwantstoattendto,andasingleweightedaverageisnotanadequate
optionforit. Thismotivatestheextensionofthescaleddot-productattentiontoMHA,
whichallowsthemodeltojointlyattendtoinformationfromdiverserepresentationsub-
spaces,asshowninFigure11.
|     |                                  | Y      |     |     |               | Y       |           |     |
| --- | -------------------------------- | ------ | --- | --- | ------------- | ------- | --------- | --- |
|     |                                  | MatMul |     |     |               | Project |           |     |
|     | Softmax                          |        |     |     | Concatenation |         |           |     |
|     | Masking                          |        |     |     |               |         | H         |     |
|     | (only for causal self-attention) |        |     |     |               |         | Attention |     |
Scaled Dot-Product Attention
Heads
Scaling
|     |     |     |     |     | Project | Project Project |     |     |
| --- | --- | --- | --- | --- | ------- | --------------- | --- | --- |
MatMul
|     | Q   | K   | V   |     | Q   | K   | V   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
(a)Scaleddot-productattention. (b)Multi-HeadAttentionwithHheads.
Figure11.Comparisonofasinglescaleddot-productattention(a)andmulti-headattentionwithH
attentionheads(b).
InMHA,keys,valuesandqueriesarelinearlyprojected H separatetimes,bythree
learnedprojectionmatrices,ontospacesofdimensions D k , D v and D k respectively. Fur-
thermore, ascaleddot-productattentionisappliedtoeachoftheseprojectionsandthe
results are concatenated together and re-projected onto the previous layer space. Each
projection-attention pair defines a so-called attention head h. For the sake of simplicity,
i
keys,valuesandqueriesareassumedtohavethesamedimensionD. Eachattentionhead
|         |               |           | K   | ∈ RD⊗RDk, | V   | ∈ RD⊗RDv | Q ∈ RD⊗RDk, |     |
| ------- | ------------- | --------- | --- | --------- | --- | -------- | ----------- | --- |
| h i has | three learned | matrices: | W   |           | W   |          | andW        |     |
|         |               |           | i   |           | i   |          | i           |     |
usedtoprojectkeys,valuesandqueries,respectively. Eachattentionheadappliesascaled
dot-productattention(seeEquation(33))totheprojectedkeys, valuesandqueries(see
Section4.1.1):
|     |     |     | =Attention(KWK,VWV,QW |     |     | Q) ∀i ∈ [1,H] |     |      |
| --- | --- | --- | --------------------- | --- | --- | ------------- | --- | ---- |
|     |     | h   | i                     |     |     |               |     | (34) |
|     |     |     |                       | i   | i   | i             |     |      |
Finally,theattentionoutputYisgivenby:
)Wo
|     |     | Y =MHA(K,V,Q) |     | =Concatenate(h |     | ,h ,...,h |     | (35) |
| --- | --- | ------------- | --- | -------------- | --- | --------- | --- | ---- |
|     |     |               |     |                |     | 1 2       | H   |      |
RM⊗RHDv
wheretheoutputsh i fromallattentionheadsareconcatenatedintoasingle
matrixandthenre-projectedlinearlytotheoriginalD-dimensionalspaceviaanadditional
| projectionmatrixWo |     | ∈RHDv | ⊗RD. |     |     |     |     |     |
| ------------------ | --- | ----- | ---- | --- | --- | --- | --- | --- |
4.1.3. ShortcomingsofTransformers
TherearethreemainshortcomingsofTransformers. Firstly,Transformersarelocally-
agnostic,thatis,thescaleddot-productoftheattentionmechanism(seeEquation(33))is
insensitive to the local context, which can make the model prone to anomalies in time

Information2023,14,598 20of35
seriesforecasting[188]. Furthermore,Transformerssufferofmemorybottleneck,i.e.,Trans-
formers’spacecomplexityisO(L2)withsequencelengthL[188]. Similarly,Transformers
alsohavethesametimecomplexity,limitingtheirapplicationtothelong-termforecast-
ing. TheseshortcomingsarefacedbysomeoftheTransformervariantsdescribedinthe
followingsection.
4.1.4. TransformerVariantsforTimeSeriesForecasting
Inrecentyears,manyvariantsofthenaiveTransformer[181],specificfortimeseries
forecasting,havebeenproposed. Keyinnovationsthatthesevariantssuggestconcernthe
embeddinglayer,attentionmechanismsandeventheencoder-decoderstructure. Most
oftheliteraturefocusedonthedesignofalternativeattentionmechanismsthataremore
suitablefortimeseriesforecastingtasks. OneofthefirstsuchworksistheLogTrans[188],
whichhandlestwolimitationsofthetraditionalTransformer: locally-agnosticandmemory
bottleneck(seeSection4.1.3). Theformerlimitationistackledusingcausalconvolutions
(see Section 3.1.2) to generate keys and queries in the self-attention module. For the
latter,alog-sparsemaskisconsideredinordertoreducethecomputationalcomplexity(see
Section4.1.3)ofmulti-headattention. InspiredbytheideaofLogTrans,anothervariant,the
Informer[182],definesanewsparsemeasuretocharacteriseasubsetofthemostinformative
queriesbeforeapplyingattention. Inaddition,thisstrategyalsoallowsforthereductionof
thecomputationalcomplexityofattentionmechanisms. UnlikeLogTransandInformer,the
Autoformer[183]replacesthestandardscaleddot-productattentionwithanautocorrelation
mechanism. Additionally,adecompositionmoduleisemployedtobreakdownthetimeseries
intotrendandseasonalcomponents,assumingimplicitlythattheyexistandareadditive.
Theautocorrelationmechanismmeasuresthetime-delaysimilaritybetweeninputsignals
andaggregatesthetop-ksimilarsub-seriestoproducetheoutput. TheFEDformer[184],
basedontheworkofLinformer[189],appliesattentiontoalow-rankapproximationofthe
inputbasedontheRestrictedIsometryProperty(RIP)matrixtheory[190]. First,itrepresents
the input signal into a frequency domain (either Fourier or Wavelet). Furthermore, it
achievesalinearcomplexitybyapplyingsimplifiedattentionmechanismsonarandomly
selectedsubsetoffrequencieswithafixedsizem. Recently,researcheffortshavemoved
fromattentionmechanismstoinputrepresentation, specificallyconcerninghowtorelate
thedimensionsofamultivariatetimeseriesandhowtoprojecttheinputsequenceintoa
latentrepresentation. ThepatchTST[191]assumeschannelindependence,i.e.,independence
amongthe dimensionofthe inputmultivariatetime series, processingeachdimension
as a univariate time series. PatchTST segments each input sequence into shorter, local
sub-sequences that are fed as input samples to a naive Transformer encoder [181]. All
time series dimensions are implicitly related via the sharing of the encoder weights. A
similarconsiderationisadoptedbytheCrossformer[192],whichsegmentseachdimension
of the input time series into non-overlapping shorter sub-sequences. Unlike patchTST,
however,theCrossformerexplicitlydefinestherelationsamongalldimensionsusinga
Two-StageAttention(TSA)mechanism. Furthermore, CrossformerfollowsaHierarchical
Encoder-Decoderarchitecture,inwhichmultiplelayersofTSAareusedtocapturerelations
atmultipletimescales. AnotherrelevantworkisthePyraformer[193],whichproposesa
PyramidalAttentionModule(PAM)tocapturelong-termdependencieswhileachievinga
complexitythatislinearinthesequencelength. Essentially,PAMconsistsofapplyingthe
classicscaleddot-productattentioninasparsefashionaccordingtoapyramidalgraph,
built using a cascade of strided convolutions, that defines a multi-scale representation
of the input sequence. According to PAM, each node of the graph is a query and it
can attend only those nodes (keys) that are its direct neighbours in the graph. In this
way, Pyraformer is able to capture both short-term and long-term dependencies while
still achieving a linear complexity. Similarly to Pyraformer, Scaleformer [194] addresses
the importance of multi-scale dependencies in time series forecasting. The approach is
orthogonaltomanytimeseriesTransformersand,assuch,ithasbeenempiricallyevaluated
withsomeoftheaforementionedmodelsliketheAutoformer[183]andtheFEDformer[184].

Information2023,14,598 21of35
Givenaninputpastsequenceandthecorrespondingtargetsequence,themainideaisto
applyoneoftheabove-mentionedTransformermodels,multipletimesatmultipletime
scales. Atagivenscales,theinputtotheencoderistheoriginallook-backwindowbut i
downsampledbyafactors usingaveragepooling;theinputtothedecoderisgivenbythe
i
modelforecastatthepreviousscales i−1 ,butupsampledbyafixedfactorsthroughlinear
interpolation. Tomitigateerrorpropagationanddistributionshiftsthatareduetorepeated
upsamplingoperations,theencoderanddecoder’sinputsarefirstnormalisedusingCross-
ScaleNormalization. Finally,alossfunction,basedonanadaptiveloss,isappliedateach
timescalebetweenthemodelforecastandthetargetsequence,whichisalsodownsampled
byafactors viaaveragepooling. TheTriformer[195]proposesaparticulararchitecturethat
i
integratesattentionmechanismsandrecurrentunitstoensurehighefficiencyandaccuracy.
Theformerisachievedbyapatchattentionmechanismwithlinearcomplexity;thelatteris
obtainedbyusingvariable-specificparameters.Thepatchattentionmechanismsplitstheinput
sequenceinPpatchesoflengthSandassignsalearnablepseudo-timestampT toeachpatch.
p
Whenpatchattentionisapplied,eachpseudo-timestampT p isconsideredasaqueryQforits
patchonly. Moreover,variable-specificparametersareintroducedbyfactorisingtheprojection
| matrices(i.e,WK | andWV)intothreematrices: |                             |     | ∈ RD⊗Ra, |
| --------------- | ------------------------ | --------------------------- | --- | -------- |
|                 |                          | leftvariable-agnosticmatrix |     | L        |
middlevariable-specificmatrixB ∈Ra⊗Ra andrightvariable-agnosticmatrixR ∈Ra⊗RD,
(cid:28)
where a D. Finally, to cope with the limited temporal receptive field that is due to
thepatchmechanism,recurrentunitsareusedtoaggregateandcontroltheinformation
forallpseudo-timestampsofeachlayerbeforethefinalprediction. Allabove-mentioned
variantsofTransformersharetheover-stationarizationproblemthatconsistsintheinability
togeneratedistinguishableattentionscoreswhentrainedonstationarizedseries[196]. The
Non-stationaryTransformer[196]proposesagenericframeworktoovercometheproblemof
over-stationarization. Thisframeworkiscomposedoftwointerdependentmodules: Series
StationarizationandDe-stationaryAttention. Theformerattenuatesthenon-stationarityof
thetimeseriesconsidered,usingtwosequentialoperations: Normalizationmodule,which
computesthemeanandthevarianceforeachinputtimeseriesinordertotransformit
into a stationary time series, and a De-normalization module, which transforms the model
outputsbackintoanon-stationarytimeseries,usingthemeanandvariancecomputedin
thepreviousmodule. Thelatterisanovelattentionmechanism,whichcanapproximate
theattentionscoresthatareobtainedwithoutstationarizationanddiscovertheparticular
temporaldependenciesfromoriginalnon-stationarydata. Transformervariantsfortime
seriesforecastingaredescribedindetailinTable12. FurtherdetailsoneachTransformer
variant,canbefoundintheoriginalpaperthatpresentsthearchitecture.
Table12.RecentvariantsofTransformerarchitecturefortimeseriesforecasting.
|     | Ref.  | Year | Model                     |     |
| --- | ----- | ---- | ------------------------- | --- |
|     | [188] | 2019 | LogTrans                  |     |
|     | [182] | 2021 | Informer                  |     |
|     | [183] | 2021 | Autoformer                |     |
|     | [184] | 2022 | FEDFormer                 |     |
|     | [193] | 2022 | Pyraformer                |     |
|     | [195] | 2022 | Triformer                 |     |
|     | [196] | 2022 | Non-stationaryTransfomers |     |
|     | [191] | 2023 | PatchTST                  |     |
|     | [192] | 2023 | Crossformer               |     |
|     | [194] | 2023 | Scaleformer               |     |
Table 13 reports an extensive comparison among all aforementioned Transformer
variants. Ithastobenotedthat,thereportedresultswerecollectedfromtheoriginalpapers
thattestedagivenmodelonagivendataset(thereadercanrefertotheGitHubpages
linkedintheoriginalpapersofeacharchitectureforreproducingtheexperiments,using
theoriginalexperimentalsetups).

Information2023,14,598 22of35
Table13.Multivariatelong-termforecastingbenchmarksamongvariantofTransformerarchitectureswithdifferentpredictionlengthsP∈[96,192,336,720].The
inputlengthconsideredforILIdatasetis36and96fortheothers. AlowerMSEorMAEindicatesabetterprediction. Thebestresults,foreachdatasets,are
highlightedinbold.
Models Crossformer PatchTST Non-Stationary Pyraformer FEDFormer Autoformer Informer LogTrans LSTM TCN
Metric MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE
rehtaeW
96 - - 0.149 0.198 0.173 0.223 0.354 0.392 0.217 0.296 0.266 0.336 0.300 0.384 0.458 0.490 0.369 0.406 0.615 0.589
192 - - 0.194 0.241 0.245 0.285 0.673 0.597 0.276 0.336 0.307 0.367 0.598 0.544 0.658 0.589 0.416 0.435 0.629 0.600
336 0.495 0.515 0.245 0.282 0.321 0.338 0.634 0.592 0.339 0.380 0.359 0.395 0.578 0.523 0.797 0.652 0.455 0.454 0.639 0.608
720 0.526 0.542 0.314 0.334 0.414 0.410 0.942 0.723 0.403 0.482 0.419 0.428 1.059 0.741 0.869 0.675 0.535 0.520 0.639 0.610
cfifarT
96 - - 0.360 0.249 0.612 0.338 0.684 0.393 0.562 0.349 0.613 0.388 0.719 0.391 0.684 0.384 0.843 0.453 1.438 0.784
192 - - 0.379 0.256 0.613 0.340 0.692 0.394 0.562 0.346 0.616 0.382 0.696 0.379 0.685 0.390 0.847 0.453 1.463 0.794
336 0.530 0.300 0.392 0.264 0.618 0.328 0.699 0.396 0.570 0.323 0.622 0.337 0.777 0.420 0.733 0.408 0.853 0.455 1.479 0.799
720 0.573 0.313 0.432 0.286 0.653 0.355 0.712 0.404 0.596 0.368 0.660 0.408 0.864 0.472 0.717 0.396 0.500 0.805 1.499 0.804
yticirtcelE 96 - - 0.129 0.222 0.169 0.273 0.498 0.299 0.183 0.297 0.201 0.317 0.274 0.368 0.258 0.357 0.375 0.437 0.985 0.813
192 - - 0.147 0.240 0.182 0.286 0.828 0.312 0.195 0.308 0.222 0.334 0.296 0.386 0.266 0.368 0.442 0.473 0.996 0.821
336 0.323 0.369 0.163 0.159 0.200 0.304 1.476 0.326 0.212 0.313 0.231 0.338 0.300 0.394 0.280 0.380 0.439 0.473 1.000 0.824
720 0.404 0.423 0.197 0.290 0.222 0.321 4.090 0.372 0.231 0.343 0.254 0.361 0.373 0.439 0.283 0.376 0.980 0.814 1.438 0.784
ILI
24 3.041 1.186 1.319 0.754 2.294 0.945 5.800 1.693 2.203 0.963 3.483 1.287 5.764 1.677 4.480 1.444 5.914 1.734 6.624 1.830
36 3.406 1.232 1.579 0.870 1.825 0.848 6.043 1.733 2.272 0.976 3.103 1.148 4.755 1.467 4.799 1.467 6.631 1.845 6.858 1.879
48 3.459 1.221 1.553 0.815 2.010 0.900 6.213 1.763 2.209 0.981 2.669 1.085 4.763 1.469 4.800 1.468 6.736 1.857 6.968 1.892
60 3.640 1.305 1.470 0.788 2.178 0.963 6.531 1.814 2.545 1.061 2.770 1.125 5.264 1.564 5.278 1.560 6.870 1.879 7.127 1.918
2mTTE
96 - - 0.166 0.256 0.192 0.274 0.409 0.488 0.203 0.287 0.255 0.339 0.365 0.453 0.768 0.642 2.041 1.073 3.041 1.330
192 - - 0.223 0.296 0.280 0.339 0.673 0.641 0.269 0.328 0.281 0.340 0.533 0.563 0.989 0.757 2.249 1.112 3.072 1.339
336 - - 0.274 0.329 0.334 0.361 1.210 0.846 0.325 0.366 0.339 0.372 1.363 0.887 1.334 0.872 2.568 1.238 3.105 1.348
720 - - 0.362 0.385 0.417 0.413 4.044 1.526 0.421 0.415 0.422 0.419 3.379 1.388 3.048 1.328 2.720 1.287 3.153 1.354

Information2023,14,598 23of35
5. OtherRelevantDeepLearningModels
This section is reserved for those works that propose interesting architectures for
short-termandlong-termtimeseriesforecastingwhichdonotfitthepreviouslydefined
categories. Eventhoughthesemodelsmightsharethesamebuildingblocksofwell-known
architectures(e.g., CNN,TCN,RNN,Transformer), duetotheirpeculiarityandhetero-
geneityithasbeendecidedtocollectthemunderapropersection. In[197]aContinuous
RecurrentUnit(CRU)basedonstochasticdifferentialequations(SDEs)andKalmanfilters,
thatcanhandleirregularlysampledtimeseries,isproposed. TheFiLM(Frequency-improved
LegendreMemory)model[198]generatesarepresentationofpasttimeseriessamplesby
Legendreprojections. ItusesanoisereductionmodulebasedonFourieranalysistopreserve
onlyrelevantinformationfromprevioustimesamples,reducingtheeffectthatnoisysignals
canhaveontimeseriesforecasting. In[199],itshowshowatimeseriesforecastingmodel
fullybasedonMLPcancomparecompetitivelywithstate-of-the-artTransformermodels
(e.g.,PatchTST[191]),reducing,inthisway,theforecastingcomputationalcost. Indetail,it
proposesanadaption(TSMixer)ofMLP-Mixer,originallyproposedforthevisiondomain,
fortimeseriesforecasting. Aconvolution-basedarchitecture,MICN(Multi-scaleIsometric
ConvolutionNetwork)[200],candiscoverlocalpatternsandglobalcorrelationsintimeseries
byusingamulti-branchstructureandrelyingondownsampled1Dconvolutionstoextractlocal
featuresandisometricconvolutions,aparticularcaseofcausalconvolution(seeSection3.1.2),
todiscoverglobalcorrelations. Table14summarisestheaforementionedmodels.
Table14.Recentapplicationsontimeseriesforecastingusingotherdeeplearningarchitectures.
| Ref.      | Year |                                           | Application |     |
| --------- | ---- | ----------------------------------------- | ----------- | --- |
| [197]     | 2022 | Climatedata/ElectronicHealthRecords       |             |     |
| [198]     | 2022 | Long-termbenchmarkdatasets(seeSection6.2) |             |     |
| [199,200] | 2023 | Long-termbenchmarkdatasets(seeSection6.2) |             |     |
6. BenchmarksforTimeSeriesForecasting
Recently,agroupoftimeserieshaveemergedasbenchmarksforassessingtheperfor-
manceofmachinelearningmodelsintimeseriesforecastingtasks. Thissectiondescribes
themostrelevantbenchmarksforbothshortandlong-termforecasting.
6.1. BenchmarksforShort-TermForecasting
Amongseveraldifferentdatasetsusedforshort-termforecasting,themostpopular
onesaredescribedinTable15. ItisworthquotingtheM4dataset[44],proposedin2020for
thehomonymousM4competitionasacommonbenchmarkforevaluatingtheperformance
ofshort-termforecastingmodels. TheM4datasetcontains100.000timeseriessubdivided
accordingtotheirdatafrequencyintosixgroups: M4-Yearly,M4-Quarterly,M4-Monthly,
M4-Weekly,M4-DailyandM4-Hourly. Furthermore,timeseriesarealsocategorisedintosix
domains,namely,Demographic,Finance,Industry,Macro,MicroandOther. Someinsightson
howtimeseriesaredistributedintothesecategoriesaregiveninFigure12.
Table15.Short-termforecastingdatasets.ThecolumnDimreferstothedimensionalityoftimeseries.
| Dataset          |     | Dim | DataType(Real/Synthetic) |      |
| ---------------- | --- | --- | ------------------------ | ---- |
| M4-Yearly[44]    |     | 1   |                          | Real |
| M4-Quarterly[44] |     | 1   |                          | Real |
| M4-Monthly[44]   |     | 1   |                          | Real |
1
| M4-Weekly[44]     |     |     |     | Real      |
| ----------------- | --- | --- | --- | --------- |
| M4-Daily[44]      |     | 1   |     | Real      |
| M4-Hourly[44]     |     | 1   |     | Real      |
| Mackey-Glass[201] |     | 1   |     | Synthetic |
| DatasetA[202]     |     | 1   |     | Real      |
| DSVC1[203]        |     | 1   |     | Real      |
| Paris-14E[204]    |     | 1   |     | Real      |
| DatasetD[205]     |     | 1   |     | Synthetic |

Information2023,14,598 24of35
|     | M4-Monthly	data	set                         |     |     |     | M4-Yearly	data	set |                          |
| --- | ------------------------------------------- | --- | --- | --- | ------------------ | ------------------------ |
|     | Other:	277	-	0.6% Demographic:	5728	-	11.9% |     |     |     | Other:	1236	-	5.4% | Demographic:	1088	-	4.7% |
Micro:	10975	-	22.9%
Finance:	6519	-	28.3%
Micro:	6538	-	28.4%
Finance:	10987	-	22.9%
Macro:	10016	-	20.9%
|     | Industry:	10017	-	20.9% |     |     | Macro:	3903	-	17.0% |     | Industry:	3716	-	16.2% |
| --- | ----------------------- | --- | --- | ------------------- | --- | ---------------------- |
Demographic Finance Industry Macro Micro Other Demographic Finance Industry Macro Micro Other
|     |     | meta-chart.com |     |     |     | meta-chart.com |
| --- | --- | -------------- | --- | --- | --- | -------------- |
(a)M4-Monthlydatasetcomposition. (b)M4-Yearlydatasetcomposition.
Total	M4	competition	data	sets
M4-Hourly:	414	-	0.4%
M4-Daily:	4227	-	4.2%
|     |     | M4-Weekly:	359	-	0.4% | M4-Yearly:	23000	-	23.0% |     |     |     |
| --- | --- | --------------------- | ------------------------ | --- | --- | --- |
M4-Monthly:	48000	-	48.0%
M4-Quarterly:	24000	-	24.0%
|     |     | M4-Yearly | M4-Quarterly M4-Monthly M4-Weekly | M4-Daily |     |     |
| --- | --- | --------- | --------------------------------- | -------- | --- | --- |
M4-Hourly
meta-chart.com
(c)M4-Competitiondatasetcomposition.
Figure12.CompositionoftheM4dataset.(a,b)show,respectively,thedistributionofM4-Monthly
andM4-YearlytimeseriesintothesixM4categories.(c)showsthenumberoftimeseriesineachof
theM4datasets.
6.2. BenchmarksforLong-TermForecasting
Nowadays,agroupofspecificdatasetshasbecomethede-factobenchmark[183]to
assesslong-termforecastingaccuracyofallTransformervariantspresentedinSection4.1.4.
Indetail,thisbenchmarkiscomposedofninemultivariatetimeseriesdatasetsconcerning
the following domains: electricity, transportation, weather, exchange rate and illness (see
Table16). Timeresolutioncanvaryfrom10minupto7days.
Table 16. Long-term forecasting benchmark data sets. The data set size (·,·,·) refers to the car-
dinality of training, validation and test set, respectively. The columns dim, pred len and time res
refer to the dimensionality of time series, the number of predicted future samples and the time
resolution,respectively.
| Dataset | Dim PredLen |     | DatasetSize |     | TimeRes | Domain |
| ------- | ----------- | --- | ----------- | --- | ------- | ------ |
ETTm1 7 [96,192,336,720] (34,465,11,521,11,521) 15mins Electricity
ETTm2 7 [96,192,336,720] (34,465,11,521,11,521) 15mins Electricity
| ETTh1 | 7 [96,192,336,720] |     | (8545,2881,2881) |     | 15mins | Electricity |
| ----- | ------------------ | --- | ---------------- | --- | ------ | ----------- |
| ETTh2 | 7 [96,192,336,720] |     | (8545,2881,2881) |     | 15mins | Electricity |
Electricity 321 [96,192,336,720] (18,317,2633,5261) 1h Electricity
| Traffic | 862 [96,192,336,720] |     | (12,185,1757,3509) |     | 1h  | Transport |
| ------- | -------------------- | --- | ------------------ | --- | --- | --------- |
Weather 21 [96,192,336,720] (36,792,5271,10,540) 10mins Weather
| Exchange | 8 [96,192,336,720] |     | (5120,665,1422) |     | 1day  | Finance |
| -------- | ------------------ | --- | --------------- | --- | ----- | ------- |
| ILI      | 7 [24,36,48,60]    |     | (617,74,170)    |     | 1week | Illness |
7. Conclusions
Thepaperhasrevieweddeeplearningarchitecturesfortimeseriesforecasting,un-
derliningtheiradvances. Nevertheless,fourmajorproblemsremainopen. Thefirstone
residesintheinabilityofmostdeeplearningmethods,withtheexceptionofDeepGaussian
Processes,toestimateaconfidenceintervalforthetimeseriesprediction. Inprinciple,all
deeplearningarchitecturesquotedinthesurveycanbeproperlymodifiedusingBayesian
trainingstrategies[206]inordertoprovidetheuncertaintyofthemodelprediction,but,to
thebestofourknowledge,ithasnotbeenperformedyet. Thesecondproblemresidesin

Information2023,14,598 25of35
thedevelopmentofmoreandmorecomplexdeeplearningarchitectures. Thismakesthem
subjecttooverfitting,aproblemthatcanhardlybefacedbydeeplearningarchitectures.
Therefore,thedevelopmentofdeeplearningarchitecturesfortimeseriesforecastingthat
arerobustw.r.t.overfittingisbecomingmoreandmorerelevant.Thethirdproblemconsists
intheneedforadequatelylongtimeseries. Inparticular,somedeeplearningarchitectures,
e.g.,Transformers,requiretheestimationofmillionsofparameters,implying,inthisway,
thenecessityofadequatelylongtimeseriesforestimatingthem. Theproblemseemsto
be partially addressed by data augmentation but the proposed solutions are not fully
adequate, yet. Finally, thelastproblememergesinmostoftherevieweddeeplearning
models. Theyassumethedynamicalstationarityoftimeseries,implyingthatthedynamic
systemgeneratingtimeseriesisstationaryovertime. Whentheaforementionedassump-
tionisviolated,aconceptdriftphenomenon[207]intimeseriesisobserved,consequently
leadingtoadramaticdecreaseinthepredictionaccuracyofdeeplearningmodelsfortime
seriesforecasting.
AuthorContributions:Conceptualization,A.C.,V.C.andF.C.;methodology,A.C.andV.C.;valida-
tion,A.C.,V.C.andF.C.;formalanalysis,F.C.;investigation,A.C.,V.C.andG.I.;resources,A.C.,V.C.,
G.I.andF.C.;writing—originaldraftpreparation,A.C.,V.C.andF.C.;writing—reviewandediting,
A.C.,V.C.andF.C.;visualization,A.C.,V.C.andF.C.;supervision,F.C.;projectadministration,F.C.
Allauthorshavereadandagreedtothepublishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
DataAvailabilityStatement:Nonewdatawerecreatedoranalyzedinthisstudy.Datasharingis
notapplicabletothisarticle.
Acknowledgments:Wewouldliketothanktheanonymousreviewersfortheusefulcomments.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.
AppendixA.TableofMathematicalExpressions
InAppendixA,thetableofthemostfrequentmathematicalexpressionsandoperations
isprovided. TableA1providesadescriptionforeachmathematicaloperation.
TableA1.Tableofthemostcommonlyusedmathematicaloperationswiththeirrespectivedescription.
Symbol Definition
Y =w∗X ConvolutionbetweenakernelwandasequenceX.TheresultisanewsequenceY.
Element-wiseproductbetweentwovectors(cid:126)uand(cid:126)v.Theresultisavector(cid:126)ysuch
(cid:126)y=(cid:126)u(cid:12)(cid:126)v
thaty =uv.
i i i
V⊗W TensorproductbetweentwovectorsVandW,theresultisamatrix.
I TheIdentitymatrix.
AppendixB.DiffusionModels
Inthissection,themostrelevantdiffusionmodels,i.e.,DDPMs(AppendixB.1),SGMs
(AppendixB.2)andSDEs(AppendixB.3),andfoundations,aredescribed.
AppendixB.1. DenoisingDiffusionProbabilisticModels
DenoisingDiffusionProbabilisticModels,originallyproposedin[173]andlaterextended
in[174],considertwoMarkovchainsforforwardandbackwardprocess,respectively,to
approximatethegenerativeprocessofobserveddata.Indetail,lettheoriginalnoiselessdata
bex0. TheforwardMarkovchainprojectsx0intoasequenceofnoiseddatax1,x2,...,xK
withadiffusiontransitionkernel:
√
q(xk|xk−1) = N( a xk−1,(1−a )I), (A1)
k k

Information2023,14,598 26of35
whereKisthefinitenumberofnoiselevelofforwardprocess,a ∈ (0,1)fork =1,2,...,K
k
arehyperparametersindicatingthevarianceofthenoiselevelateachstep,N(·,·)isthe
Gaussiandistribution,and I istheidentitymatrix. TheGaussiantransitionkernelq(·|·)
hasafundamentalpropertythatallowsobtainingxk directlyfromoriginalsamplex0:
(cid:112)
|     |     |     | q(xk|x0) |     | = N( | a˜ x0,(1−a˜)I), |     |     |     |     | (A2) |
| --- | --- | --- | -------- | --- | ---- | --------------- | --- | --- | --- | --- | ---- |
|     |     |     |          |     |      | k               | k   |     |     |     |      |
∏k
where a˜ = a. In DDPM, the reverse transition kernel p (·|·) is designed by a deep
|     | k i=1 | i   |     |     |     |     |     | θ   |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
neuralnetwork:
|     |     |     | (xk−1|xk) |     |       | (xk,k),Σ | (xk,k)), |     |     |     |      |
| --- | --- | --- | --------- | --- | ----- | -------- | -------- | --- | --- | --- | ---- |
|     |     |     | p         |     | = N(µ |          |          |     |     |     | (A3) |
|     |     |     | θ         |     |       | θ        | θ        |     |     |     |      |
whereθindicateslearnableparametersofdeepneuralnetworks. Inordertocomputethe
parametersθsuchthatsamplesestimatedby p (x0)arealmostidenticaltoobserveddata
θ
x0,amaximumlikelihoodestimationmethodisperformed,minimisingthevariationallower
| boundoftheestimatednegativelog-likelihood |     |     |     |     |     | E[−logp |     | (x0)]: |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | ------- | --- | ------ | --- | --- | --- |
θ
|     |         |     |          |         | (cid:34)  |     |     |             |     | (cid:35) |      |
| --- | ------- | --- | -------- | ------- | --------- | --- | --- | ----------- | --- | -------- | ---- |
|     |         |     |          |         |           |     | K   | p (xk−1|xk) |     |          |      |
|     | E[−logp |     | (x0)] =E |         | −logp(xK) |     | − ∑ | θ           |     |          |      |
|     |         | θ   |          | q(x0:K) |           |     |     | log         |     | ,        | (A4) |
q(xk|xk−1)
k=1
where x0:K indicates the sequence x0,...,xK. A simpler objective function [174] can be
provided,asfollows:
|     |     |     |                  |     | (cid:112)      |      | (cid:112) |                   |     |     |      |
| --- | --- | --- | ---------------- | --- | -------------- | ---- | --------- | ----------------- | --- | --- | ---- |
|     |     | E   | [δ(k)||(cid:101) | −   | (cid:101) ( a˜ | x0 + | 1−a˜      | (cid:101),k)||2], |     |     | (A5) |
|     |     |     | k,x0,(cid:101)   |     | θ              | k    |           | k                 |     |     |      |
σ2I
assumingthecovariancematrixequaltoΣ (xk,k) = ,whereσ2controlsthenoiselevel
|     |     |     |     |     | θ   |     | k   | k   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
)2
| andmayvaryatdifferentreversesteps,andδ(k) |     |     |     |     |     | =   | (1−ak | .   |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
2ak
|     |     |     |     |     |     |     | 2σ (1−a˜k | )   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
k
| AppendixB.2. | Score-BasedGenerativeModels |     |     |     |     |     |     |     |     |     |     |
| ------------ | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Score-basedgenerativemodels(SGMs)[175],aremadeupoftwomodules. Theformeris
thescorematchingmodule[208],forestimatingtheunknowntargetdistributionq(x)withthe
Steinscoreapproximation,∇ logq(x),bymeansofascore-matchingnetwork(e.g.,denoising
x
scorematching[209],slidedscorematching[210]). ThelatteristheannealedLangevindynamics
(ALD),thatisasamplingalgorithmgeneratingsampleswithaniterativeLangevinMonte
Carloprocessateachupdatestep. Thefundamentalideabehinddenoisingscorematchingis
toprocesstheobserveddatax0withtheforwardtransitionkernelq(xk|x0) = N(x0,σ2I),and
k
toestimatejointlytheSteinscoresforthenoisedensitydistributionsq (x),q (x),...,q (x).
|                                                  |     |     |     |     |     |     |        |      | σ1   | σ2            | σk  |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | ------ | ---- | ---- | ------------- | --- |
| Inthiscase,theSteinscorefornoisedensityfunctionq |     |     |     |     |     |     | (x)is∇ | logq | (x). |               |     |
|                                                  |     |     |     |     |     |     | σk     | x    | σk   | Hence,aneural |     |
networks (x,σ ),withlearnableparametersθ,canapproximatetheSteinscore. Theinitial
θ x
objectivefunctionisthereforegivenby:
|     |     |     | E [δ(k)||s |     | (xk,k) | − ∇klogq |     | (xk)||2]. |     |     | (A6) |
| --- | --- | --- | ---------- | --- | ------ | -------- | --- | --------- | --- | --- | ---- |
|     |     |     | k,x0,xk    |     | θ      | x        | σk  |           |     |     |      |
Subsequently, the ALD algorithm is used for the sampling phase. The algorithm is
initialised with a sequence of increasing noise levels σ ,...,σ and a starting sample
|        |              |     |                           |     |                                      |           | 1   | K         |     |     |      |
| ------ | ------------ | --- | ------------------------- | --- | ------------------------------------ | --------- | --- | --------- | --- | --- | ---- |
| xK,0   | I).          |     | K,K−1,...,0,xk            |     |                                      |           |     |           |     |     |      |
| ∼ N(0, | Fork         | =   |                           |     | isupdatedwithNiterationsthatcompute: |           |     |           |     |     |      |
|        |              |     |                           |     | z ← N(0,                             | I)        |     |           |     |     | (A7) |
|        |              |     | xk,n xk,n−1               |     | 1                                    | (xk,n−1,σ |     | (cid:112) |     |     |      |
|        |              |     | ←                         | +   | ψ s                                  |           | )   | + ψ z,    |     |     | (A8) |
|        |              |     |                           |     | 2 k                                  | θ         | k   | k         |     |     |      |
| wheren | =1,...,Nandψ |     | representthestepofupdate. |     |                                      |           |     |           |     |     |      |
k

Information2023,14,598 27of35
AppendixB.3. StochasticDifferentialEquations
As described in Appendices B.1 and B.2, both DDPMs and SGMs models define a
discrete forward process, considering N iterations of diffusion steps. In order to define a
continuousdiffusionprocess,asolutionbasedonstochasticdifferentialequations(SDEs)[176]
hasbeenproposed. SincebothDDPMsandSGMsarediscreteformsofSDEs,theSDEs
formulation can be considered as an extension of the aforementioned two definitions.
Therefore,thebackwardprocessismodelledasatime-reverseSDE(seeEquation(A10)),and
thesamplescanbegeneratedbysolvingtime-reverseSDE.AgeneralexpressionofSDEis
definedasfollows:
dx = f(x,k)dk + g(k)dw, (A9)
andthetime-reverseSDE[211]is:
dx = [f(x,k) − g(k)2∇ logq (x)]dk + g(k)dw˜, (A10)
x k
wherewandw˜ arestandardWienerprocesses[212]. Itcanbeproved[176]thatthesampling
fromtheprobabilityflowordinarydifferentialequations(ODE)yieldsthesamedistributionof
thetime-reverseSDE:
1
dx = [f(x,k) − g(x)∇ logq (x)]dk, (A11)
x k
2
where f(x,k)and g(k)arethedriftanddiffusioncoefficientsforthediffusionprocess,re-
spectively,and∇ logq (x)istheSteinscorethatcanbelearnedwithsimilarmethodsas
x k
inSGMs(seeAppendixB.2). Atthispoint,itcanobservedthattheDDPMscanberefor-
mulatedintermsofSDEs,thatgenerallyknownasvariancepreserving(VP)SDE[176]. The
samereformulationcanbedonefortheforwardprocessofSGMs,wherethecorresponding
SDEisknownasvarianceexploding(VE)SDE[176]. Afterhavinglearnedthescoremodel
s (x,k),thesamplesaregeneratedbysolvingthetime-reverseSDEortheprobabilityflow
θ
ODEwithALDtechniques.
References
1. Chianese,E.;Camastra,F.;Ciaramella,A.;Landi,T.C.;Staiano,A.;Riccio,A. Spatio-temporallearninginpredictingambient
particulatematterconcentrationbymulti-layerperceptron. Ecol.Inform.2019,49,54–61.[CrossRef]
2. Feng, Y.; Zhang, W.; Sun, D.; Zhang, L. Ozoneconcentrationforecastmethodbasedongeneticalgorithmoptimizedback
propagationneuralnetworksandsupportvectormachinedataclassification. Atmos.Environ.2011,45,1979–1985.[CrossRef]
3. Paine,C.T.;Marthews,T.R.;Vogt,D.R.;Purves,D.;Rees,M.;Hector,A.;Turnbull,L.A. Howtofitnonlinearplantgrowthmodels
andcalculategrowthrates:Anupdateforecologists. MethodsEcol.Evol.2012,3,245–256.[CrossRef]
4. Pala,Z.;Atici,R. Forecastingsunspottimeseriesusingdeeplearningmethods. Sol.Phys.2019,294,50.[CrossRef]
5. Duarte,F.B.;TenreiroMachado,J.;MonteiroDuarte,G. DynamicsoftheDowJonesandtheNASDAQstockindexes. Nonlinear
Dyn.2010,61,691–705.[CrossRef]
6. Binkowski,M.;Marti,G.;Donnat,P. Autoregressiveconvolutionalneuralnetworksforasynchronoustimeseries. InProceedings
oftheInternationalConferenceonMachineLearning,Stockholm,Sweden,10–15July2018;pp.580–589.
7. Ugurlu,U.;Oksuz,I.;Tas,O. Electricitypriceforecastingusingrecurrentneuralnetworks. Energies2018,11,1255.[CrossRef]
8. Kuan, L.; Yan, Z.; Xin, W.; Yan, C.; Xiangkun, P.; Wenxue, S.; Zhe, J.; Yong, Z.; Nan, X.; Xin, Z. Short-termelectricityload
forecastingmethodbasedonmultilayeredself-normalisingGRUnetwork. InProceedingsofthe2017IEEEConferenceonEnergy
InternetandEnergySystemIntegration(EI2),Beijing,China,26–28November2017;pp.1–5.
9. Zhu,R.;Liao,W.;Wang,Y. Short-termpredictionforwindpowerbasedontemporalconvolutionalnetwork. EnergyRep.2020,
6,424–429.[CrossRef]
10. Koprinska,I.;Wu,D.;Wang,Z. Convolutionalneuralnetworksforenergytimeseriesforecasting. InProceedingsofthe2018
InternationalJointConferenceonNeuralNetworks(IJCNN),RiodeJaneiro,Brazil,8–13July2018;pp.1–8.
11. Li,D.;Jiang,F.;Chen,M.;Qian,T. Multi-step-aheadwindspeedforecastingbasedonahybriddecompositionmethodand
temporalconvolutionalnetworks. Energy2022,238,121981.[CrossRef]
12. Narigina,M.;Kempleis,A.;Romanovs,A. MachineLearning-basedForecastingofSensorDataforEnhancedEnvironmental
Sensing. WseasTrans.Syst.2013,22,543–555.[CrossRef]
13. Han,M.;Xu,M. Laplacianechostatenetworkformultivariatetimeseriesprediction. IEEETrans.NeuralNetw.Learn.Syst.2017,
29,238–244.[CrossRef]

Information2023,14,598 28of35
14. Kumar,D.;Singh,A.;Samui,P.;Jha,R.K. Forecastingmonthlyprecipitationusingsequentialmodelling. Hydrol. Sci. J.2019,
64,690–700.[CrossRef]
15. Wan,R.;Mei,S.;Wang,J.;Liu,M.;Yang,F. Multivariatetemporalconvolutionalnetwork:Adeepneuralnetworksapproachfor
multivariatetimeseriesforecasting. Electronics2019,8,876.[CrossRef]
16. Liu,H.;Zhang,X. AQItimeseriespredictionbasedonahybriddatadecompositionandechostatenetworks. Environ.Sci.Pollut.
Res.2021,28,51160–51182.[CrossRef][PubMed]
17. Akita,R.;Yoshihara,A.;Matsubara,T.;Uehara,K. Deeplearningforstockpredictionusingnumericalandtextualinformation.
InProceedingsofthe2016IEEE/ACIS15thInternationalConferenceonComputerandInformationScience(ICIS),Okayama,
Japan,26–29June2016;pp.1–6.
18. Pang, X.; Zhou, Y.; Wang, P.; Lin, W.; Chang, V. An innovative neural network approach for stock market prediction. J.
Supercomput.2020,76,2098–2118.[CrossRef]
19. Zhang,L.;Aggarwal,C.;Qi,G.J. Stockpricepredictionviadiscoveringmulti-frequencytradingpatterns. InProceedingsofthe
23rdACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining,Halifax,NS,Canada,13–17August
2017;pp.2141–2149.
20. McNally,S.;Roche,J.;Caton,S. Predictingthepriceofbitcoinusingmachinelearning. InProceedingsofthe201826thEuromicro
InternationalConferenceonParallel,DistributedandNetwork-BasedProcessing(PDP),Cambridge,UK,21–23March2018;
pp.339–343.
21. Ye,J.;Liu,Z.;Du,B.;Sun,L.;Li,W.;Fu,Y.;Xiong,H. Learningtheevolutionaryandmulti-scalegraphstructureformultivariate
timeseriesforecasting. InProceedingsofthe28thACMSIGKDDConferenceonKnowledgeDiscoveryandDataMining,
Washington,DC,USA,14–18August2022;pp.2296–2306.
22. Chen,L.;Chen,D.;Shang,Z.;Wu,B.;Zheng,C.;Wen,B.;Zhang,W.Multi-ScaleAdaptiveGraphNeuralNetworkforMultivariate
TimeSeriesForecasting. IEEETrans.Knowl.DataEng.2023,35,10748–10761.[CrossRef]
23. Song,Y.;Gao,S.;Li,Y.;Jia,L.;Li,Q.;Pang,F. Distributedattention-basedtemporalconvolutionalnetworkforremaininguseful
lifeprediction. IEEEInternetThingsJ.2020,8,9594–9602.[CrossRef]
24. Alhassan,Z.;McGough,A.S.;Alshammari,R.;Daghstani,T.;Budgen,D.;AlMoubayed,N. Type-2diabetesmellitusdiagnosis
fromtimeseriesclinicaldatausingdeeplearningmodels. InProceedingsoftheArtificialNeuralNetworksandMachineLearning–
ICANN2018:27thInternationalConferenceonArtificialNeuralNetworks,Rhodes,Greece,4–7October2018;Proceedings,Part
III27;Springer:Berlin/Heidelberg,Germany,2018;pp.468–478.
25. Kim,T.;King,B.R.Timeseriespredictionusingdeepechostatenetworks. NeuralComput.Appl.2020,32,17769–17787.[CrossRef]
26. Lim,B. Forecastingtreatmentresponsesovertimeusingrecurrentmarginalstructuralnetworks. Adv.NeuralInf.Process.Syst.
2018,31.
27. Huang,S.;Wang,D.;Wu,X.;Tang,A.Dsanet:Dualself-attentionnetworkformultivariatetimeseriesforecasting. InProceedings
ofthe28thACMInternationalConferenceonInformationandKnowledgeManagement,Beijing,China,3–7November2019;
pp.2129–2132.
28. Wu,Z.;Pan,S.;Long,G.;Jiang,J.;Chang,X.;Zhang,C. Connectingthedots:Multivariatetimeseriesforecastingwithgraph
neuralnetworks. InProceedingsofthe26thACMSIGKDDInternationalConferenceonKnowledgeDiscovery&DataMining,
Virtual,6–10July2020;pp.753–763.
29. Cui, Y.; Zheng, K.; Cui, D.; Xie, J.; Deng, L.; Huang, F.; Zhou, X. METRO:Agenericgraphneuralnetworkframeworkfor
multivariatetimeseriesforecasting. Proc.VldbEndow.2021,15,224–236.[CrossRef]
30. Zhao,W.;Gao,Y.;Ji,T.;Wan,X.;Ye,F.;Bai,G. Deeptemporalconvolutionalnetworksforshort-termtrafficflowforecasting.
IEEEAccess2019,7,114496–114507.[CrossRef]
31. Sagheer,A.;Kotb,M. TimeseriesforecastingofpetroleumproductionusingdeepLSTMrecurrentnetworks. Neurocomputing
2019,323,203–213.[CrossRef]
32. Sánchez,L.;Anseán,D.;Otero,J.;Couso,I. AssessingthehealthofLiFePO4tractionbatteriesthroughmonotonicechostate
networks. Sensors2017,18,9.[CrossRef][PubMed]
33. Zhang,Y.;Xiong,R.;He,H.;Pecht,M.G. Longshort-termmemoryrecurrentneuralnetworkforremainingusefullifeprediction
oflithium-ionbatteries. IEEETrans.Veh.Technol.2018,67,5695–5705.[CrossRef]
34. Colla,V.;Matino,I.;Dettori,S.;Cateni,S.;Matino,R.Reservoircomputingapproachesappliedtoenergymanagementinindustry.
InProceedingsoftheEngineeringApplicationsofNeuralNetworks:20thInternationalConference,EANN2019,Xersonisos,
Crete,Greece,24–26May2019;Proceedings20;Springer:Berlin/Heidelberg,Germany,2019;pp.66–79.
35. Li,Z.;Zheng,Z.;Outbib,R. Adaptiveprognosticoffuelcellsbyimplementingensembleechostatenetworksintime-varying
modelspace. IEEETrans.Ind.Electron.2019,67,379–389.[CrossRef]
36. Bala,A.;Ismail,I.;Ibrahim,R.;Sait,S.M.;Oliva,D. Animprovedgrasshopperoptimizationalgorithmbasedechostatenetwork
forpredictingfaultsinairplaneengines. IEEEAccess2020,8,159773–159789.[CrossRef]
37. Mahmoud,A.;Mohammed,A. Asurveyondeeplearningfortimeseriesforecasting. InMachineLearningandBigDataAnalytics
Paradigms:Analysis,ApplicationsandChallenges;Springer:Cham,Switzerland,2021;pp.365–392.
38. Lim,B.;Zohren,S. Time-seriesforecastingwithdeeplearning:Asurvey. Philos.Trans.R.Soc. 2021,379,20200209.[CrossRef]
[PubMed]

Information2023,14,598 29of35
39. Sezer,O.B.;Gudelek,M.U.;Ozbayoglu,A.M. Financialtimeseriesforecastingwithdeeplearning:Asystematicliteraturereview:
2005–2019. Appl.SoftComput.2020,90,106181.[CrossRef]
40. Zeroual,A.;Harrou,F.;Dairi,A.;Sun,Y. DeeplearningmethodsforforecastingCOVID-19time-Seriesdata:AComparative
study. ChaosSolitonsFractals2020,140,110121.[CrossRef]
41. Lara-Benítez,P.;Carranza-García,M.;Riquelme,J.C. Anexperimentalreviewondeeplearningarchitecturesfortimeseries
forecasting. Int.J.NeuralSyst.2021,31,2130001.[CrossRef]
42. Barrera-Animas,A.Y.;Oyedele,L.O.;Bilal,M.;Akinosho,T.D.;Delgado,J.M.D.;Akanbi,L.A. Rainfallprediction:Acomparative
analysisofmodernmachinelearningalgorithmsfortimeseriesforecasting. Mach.Learn.Appl.2022,7,100204.[CrossRef]
43. Lakshmanna,K.;Kaluri,R.;Gundluru,N.;Alzamil,Z.S.;Rajput,D.S.;Khan,A.A.;Haq,M.A.;Alhussen,A. Areviewondeep
learningtechniquesforIoTdata. Electronics2022,11,1604.[CrossRef]
44. Makridakis,S.;Spiliotis,E.;Assimakopoulos,V. TheM4Competition:100,000timeseriesand61forecastingmethods. Int. J.
Forecast.2020,36,54–74.[CrossRef]
45. Goodfellow,I.;Bengio,Y.;Courville,A. DeepLearning;MITPress:Cambridge,MA,USA,2016.
46. Hastie,T.;Tibshirani,R.;Friedman,J.H.;Friedman,J.H. TheElementsofStatisticalLearning:DataMining,Inference,andPrediction;
Springer:Berlin/Heidelberg,Germany,2009;Volume2.
47. Gudelek,M.U.;Boluk,S.A.;Ozbayoglu,A.M. Adeeplearningbasedstocktradingmodelwith2-DCNNtrenddetection. In
Proceedingsofthe2017IEEESymposiumSeriesonComputationalIntelligence(SSCI),Honolulu,HI,USA,27November–1
December2017;pp.1–8.
48. Kuo,P.H.;Huang,C.J. Ahighprecisionartificialneuralnetworksmodelforshort-termenergyloadforecasting. Energies2018,
11,213.[CrossRef]
49. Zahid,M.;Ahmed,F.;Javaid,N.;Abbasi,R.A.;ZainabKazmi,H.S.;Javaid,A.;Bilal,M.;Akbar,M.;Ilahi,M. Electricitypriceand
loadforecastingusingenhancedconvolutionalneuralnetworkandenhancedsupportvectorregressioninsmartgrids. Electronics
2019,8,122.[CrossRef]
50. Cai,M.;Pipattanasomporn,M.;Rahman,S. Day-aheadbuilding-levelloadforecastsusingdeeplearningvs. traditionaltime
seriestechniques. Appl.Energy2019,236,1078–1088.[CrossRef]
51. Bronstein,M.M.;Bruna,J.;LeCun,Y.;Szlam,A.;Vandergheynst,P. Geometricdeeplearning:Goingbeyondeuclideandata. IEEE
SignalProcess.Mag.2017,34,18–42.[CrossRef]
52. Lea,C.;Flynn,M.D.;Vidal,R.;Reiter,A.;Hager,G.D. Temporalconvolutionalnetworksforactionsegmentationanddetection.
InProceedingsoftheIEEEConferenceonComputerVisionandPatternRecognition,Virtual,6–10July2017;pp.156–165.
53. Borovykh,A.;Bohte,S.;Oosterlee,C.W. Dilatedconvolutionalneuralnetworksfortimeseriesforecasting. J.Comput.Financ.
Forthcom.2018.[CrossRef]
54. Lara-Benítez,P.;Carranza-García,M.;Luna-Romera,J.M.;Riquelme,J.C. Temporalconvolutionalnetworksappliedtoenergy-
relatedtimeseriesforecasting. Appl.Sci.2020,10,2322.[CrossRef]
55. Hewage,P.;Behera,A.;Trovati,M.;Pereira,E.;Ghahremani,M.;Palmieri,F.;Liu,Y.Temporalconvolutionalneural(TCN)network
foraneffectiveweatherforecastingusingtimeseriesdatafromthelocalweatherstation. SoftComput. 2020,24,16453–16482.
[CrossRef]
56. Sfetsos,A.;Coonick,A. Univariateandmultivariateforecastingofhourlysolarradiationwithartificialintelligencetechniques.
Sol.Energy2000,68,169–178.[CrossRef]
57. Hsieh,T.J.; Hsiao,H.F.; Yeh,W.C. Forecastingstockmarketsusingwavelettransformsandrecurrentneuralnetworks: An
integratedsystembasedonartificialbeecolonyalgorithm. Appl.SoftComput.2011,11,2510–2525.[CrossRef]
58. Elman,J.L. Findingstructureintime. Cogn.Sci.1990,14,179–211.[CrossRef]
59. Jaeger,H. The“echostate”approachtoanalysingandtrainingrecurrentneuralnetworks-withanerratumnote. BonnGer.Ger.
Natl.Res.Cent.Inf.Technol.GmdTech.Rep.2001,148,13.
60. Hochreiter,S.;Schmidhuber,J. Longshort-termmemory. NeuralComput.1997,9,1735–1780.[CrossRef]
61. Cho,K.;vanMerrienboer,B.;Gulcehre,C.;Bahdanau,D.;Bougares,F.;Schwenk,H.;Bengio,Y. LearningPhraseRepresentations
usingRNNEncoder–DecoderforStatisticalMachineTranslation. InProceedingsofthe2014ConferenceonEmpiricalMethodsin
NaturalLanguageProcessing(EMNLP),Doha,Qatar,25–29October2014;AssociationforComputationalLinguistics:Cedarville,
OH,USA,2014;p.1724.
62. Williams,R.J.;Zipser,D. Alearningalgorithmforcontinuallyrunningfullyrecurrentneuralnetworks. NeuralComput.1989,
1,270–280.[CrossRef]
63. Jordan,M.I. Serialorder: Aparalleldistributedprocessingapproach. InAdvancesinPsychology;Elsevier: Amsterdam,The
Netherlands,1997;Volume121,pp.471–495.
64. Shi,H.;Xu,M.;Ma,Q.;Zhang,C.;Li,R.;Li,F. Awholesystemassessmentofnoveldeeplearningapproachonshort-termload
forecasting. EnergyProcedia2017,142,2791–2796.[CrossRef]
65. Mohammadi,M.;Talebpour,F.;Safaee,E.;Ghadimi,N.;Abedinia,O. Small-scalebuildingloadforecastbasedonhybridforecast
engine. NeuralProcess.Lett.2018,48,329–351.[CrossRef]
66. Ruiz,L.G.B.;Rueda,R.;Cuéllar,M.P.;Pegalajar,M. EnergyconsumptionforecastingbasedonElmanneuralnetworkswith
evolutiveoptimization. ExpertSyst.Appl.2018,92,380–389.[CrossRef]
67. Bishop,C.M. NeuralNetworksforPatternRecognition;OxfordUniversityPress:Oxford,UK,1995.

Information2023,14,598 30of35
68. Kantz,H.;Schreiber,T. NonlinearTimeSeriesAnalysis;CambridgeUniversityPress:Cambridge,UK,2004;Volume7.
69. Simonyan,K.;Vedaldi,A.;Zisserman,A. Deepinsideconvolutionalnetworks: Visualisingimageclassificationmodelsand
saliencymaps. arXiv2013,arXiv:1312.6034.
70. Selvaraju,R.R.;Cogswell,M.;Das,A.;Vedantam,R.;Parikh,D.;Batra,D. Grad-cam:Visualexplanationsfromdeepnetworks
viagradient-basedlocalization. InProceedingsoftheIEEEInternationalConferenceonComputerVision,Venice,Italy,22–29
October2017;pp.618–626.
71. Morando,S.;Jemei,S.;Hissel,D.;Gouriveau,R.;Zerhouni,N. ANOVAmethodappliedtoprotonexchangemembranefuelcell
ageingforecastingusinganechostatenetwork. Math.Comput.Simul.2017,131,283–294.[CrossRef]
72. Antonelo,E.A.;Camponogara,E.;Foss,B. Echostatenetworksfordata-drivendownholepressureestimationingas-liftoilwells.
NeuralNetw.2017,85,106–117.[CrossRef][PubMed]
73. Shen,L.;Chen,J.;Zeng,Z.;Yang,J.;Jin,J. Anovelechostatenetworkformultivariateandnonlineartimeseriesprediction. Appl.
SoftComput.2018,62,524–535.[CrossRef]
74. Jing,Z.;Yuxi,L.;Yan,C.;Bao,Y.;Jiakui,Z.;Di,L. PhotovoltaicOutputPredictionModelBasedonEchoStateNetworkswith
WeatherTypeIndex. InProceedingsofthe20193rdInternationalConferenceonInnovationinArtificialIntelligence,Suzhou,
China,15–18March2019;pp.91–95.
75. Hu,H.;Wang,L.;Peng,L.;Zeng,Y.R. Effectiveenergyconsumptionforecastingusingenhancedbaggedechostatenetwork.
Energy2020,193,116778.[CrossRef]
76. Mansoor, M.; Grimaccia, F.; Mussetta, M. Echo State Network Performance in Electrical and Industrial Applications. In
Proceedingsofthe2020InternationalJointConferenceonNeuralNetworks(IJCNN),Glasgow,UK,19–24July2020;pp.1–7.
77. Hu,H.;Wang,L.;Lv,S.X. Forecastingenergyconsumptionandwindpowergenerationusingdeepechostatenetwork. Renew.
Energy2020,154,598–613.[CrossRef]
78. Yang,Y.;Zhao,X.;Liu,X. Anovelechostatenetworkanditsapplicationintemperaturepredictionofexhaustgasfromhotblast
stove. IEEETrans.Instrum.Meas.2020,69,9465–9476.[CrossRef]
79. Li,N.;Tuo,J.;Wang,Y.;Wang,M. Predictionofbloodglucoseconcentrationfortype1diabetesbasedonechostatenetworks
embeddedwithincrementallearning. Neurocomputing2020,378,248–259.[CrossRef]
80. Gao,R.;Du,L.;Duru,O.;Yuen,K.F. Timeseriesforecastingbasedonechostatenetworkandempiricalwavelettransformation.
Appl.SoftComput.2021,102,107111.[CrossRef]
81. Mansoor,M.;Grimaccia,F.;Leva,S.;Mussetta,M. Comparisonofechostatenetworkandfeed-forwardneuralnetworksin
electricalloadforecastingfordemandresponseprograms. Math.Comput.Simul.2021,184,282–293.[CrossRef]
82. Sui,Y.;Gao,H. Modifiedechostatenetworkforpredictionofnonlinearchaotictimeseries. NonlinearDyn.2022,110,3581–3603.
[CrossRef]
83. Marino, D.L.; Amarasinghe, K.; Manic, M. Building energy load forecasting using deep neural networks. In Proceed-
ingsoftheIECON2016—42ndAnnualConferenceoftheIEEEIndustrialElectronicsSociety, Florence, Italy, 23-26October
2016;pp.7046–7051.
84. Fu,R.;Zhang,Z.;Li,L. UsingLSTMandGRUneuralnetworkmethodsfortrafficflowprediction. InProceedingsofthe2016
31stYouthAcademicAnnualConferenceofChineseAssociationofAutomation(YAC),Wuhan,China,11–13November2016;
pp.324–328.
85. Li,Z.;Tam,V. Combiningthereal-timewaveletdenoisingandlong-short-term-memoryneuralnetworkforpredictingstock
indexes. InProceedingsofthe2017IEEESymposiumSeriesonComputationalIntelligence(SSCI),Honolulu,HI,USA,27
November–1December2017;pp.1–8.
86. dosSantosPinheiro,L.;Dras,M. Stockmarketpredictionwithdeeplearning: Acharacter-basedneurallanguagemodelfor
event-basedtrading. InProceedingsoftheAustralasianLanguageTechnologyAssociationWorkshop2017,Brisbane,Australia,
6–8December2017;pp.6–15.
87. Shi,H.;Xu,M.;Li,R. Deeplearningforhouseholdloadforecasting—AnovelpoolingdeepRNN. IEEETrans.SmartGrid2017,
9,5271–5280.[CrossRef]
88. Li,X.;Peng,L.;Yao,X.;Cui,S.;Hu,Y.;You,C.;Chi,T. Longshort-termmemoryneuralnetworkforairpollutantconcentration
predictions:Methoddevelopmentandevaluation. Environ.Pollut.2017,231,997–1004.[CrossRef][PubMed]
89. Baek,Y.;Kim,H.Y. ModAugNet: Anewforecastingframeworkforstockmarketindexvaluewithanoverfittingprevention
LSTMmoduleandapredictionLSTMmodule. ExpertSyst.Appl.2018,113,457–480.[CrossRef]
90. Fischer,T.;Krauss,C. Deeplearningwithlongshort-termmemorynetworksforfinancialmarketpredictions. Eur.J.Oper.Res.
2018,270,654–669.[CrossRef]
91. Kratzert,F.;Klotz,D.;Brenner,C.;Schulz,K.;Herrnegger,M. Rainfall–runoffmodellingusingLongShort-TermMemory(LSTM)
networks. Hydrol.EarthSyst.Sci.2018,22,6005–6022.[CrossRef]
92. Zhang,J.;Zhu,Y.;Zhang,X.;Ye,M.;Yang,J. DevelopingaLongShort-TermMemory(LSTM)basedmodelforpredictingwater
tabledepthinagriculturalareas. J.Hydrol.2018,561,918–929.[CrossRef]
93. Bouktif,S.;Fiaz,A.;Ouni,A.;Serhani,M.A.Optimaldeeplearninglstmmodelforelectricloadforecastingusingfeatureselection
andgeneticalgorithm:Comparisonwithmachinelearningapproaches. Energies2018,11,1636.[CrossRef]
94. Xu,L.;Li,C.;Xie,X.;Zhang,G. Long-short-termmemorynetworkbasedhybridmodelforshort-termelectricalloadforecasting.
Information2018,9,165.[CrossRef]

Information2023,14,598 31of35
95. Wang, Y.; Shen, Y.; Mao, S.; Chen, X.; Zou, H. LASSOandLSTMintegratedtemporalmodelforshort-termsolarintensity
forecasting. IEEEInternetThingsJ.2018,6,2933–2944.[CrossRef]
96. Freeman,B.S.;Taylor,G.;Gharabaghi,B.;Thé,J. Forecastingairqualitytimeseriesusingdeeplearning. J.AirWasteManag.Assoc.
(1995)2018,68,866–886.[CrossRef]
97. Wang,Y.;Smola,A.;Maddix,D.;Gasthaus,J.;Foster,D.;Januschowski,T. Deepfactorsforforecasting. InProceedingsofthe
InternationalConferenceonMachineLearning,LongBeach,CA,USA,9–15June2019;pp.6607–6617.
98. Nichiforov,C.;Stamatescu,G.;Stamatescu,I.;Fa˘ga˘ra˘s¸an,I.Evaluationofsequence-learningmodelsforlarge-commercial-building
loadforecasting. Information2019,10,189.[CrossRef]
99. Zou,M.;Fang,D.;Harrison,G.;Djokic,S. Weatherbasedday-aheadandweek-aheadloadforecastingusingdeeprecurrent
neuralnetwork. InProceedingsofthe2019IEEE5thInternationalforumonResearchandTechnologyforSocietyandIndustry
(RTSI),Florence,Italy,9–12September2019;pp.341–346.
100. Chimmula,V.K.R.;Zhang,L. TimeseriesforecastingofCOVID-19transmissioninCanadausingLSTMnetworks. ChaosSolitons
Fractals2020,135,109864.[CrossRef][PubMed]
101. Wu,Y.;Ni,J.;Cheng,W.;Zong,B.;Song,D.;Chen,Z.;Liu,Y.;Zhang,X.;Chen,H.;Davidson,S.B. Dynamicgaussianmixture
baseddeepgenerativemodelforrobustforecastingonsparsemultivariatetimeseries. InProceedingsoftheAAAIConference
onArtificialIntelligence,Virtual,2–9February2021;Volume35,pp.651–659.
102. Dastgerdi,A.K.;Mercorelli,P. InvestigatingtheeffectofnoiseeliminationonLSTMmodelsforfinancialmarketsprediction
usingKalmanFilterandWaveletTransform. WSEASTrans.Bus.Econ.2022,19,432–441.[CrossRef]
103. Wang,Y.;Liao,W.;Chang,Y. Gatedrecurrentunitnetwork-basedshort-termphotovoltaicforecasting. Energies2018,11,2163.
[CrossRef]
104. Du,Y.; Wang,J.; Feng,W.; Pan,S.; Qin,T.; Xu,R.; Wang,C. Adarnn: Adaptivelearningandforecastingoftimeseries. In
Proceedingsofthe30thACMInternationalConferenceonInformation&KnowledgeManagement,GoldCoast,QLD,Australia,
1–5November2021;pp.402–411.
105. Bollerslev,T. Generalizedautoregressiveconditionalheteroskedasticity. J.Econom.1986,31,307–327.[CrossRef]
106. Gensler,A.;Henze,J.;Sick,B.;Raabe,N. DeepLearningforsolarpowerforecasting—AnapproachusingAutoEncoderand
LSTMNeuralNetworks. InProceedingsofthe2016IEEEInternationalConferenceonSystems,Man,andCybernetics(SMC),
Budapest,Hungary,9–12October2016;pp.2858–2865.
107. Bao,W.;Yue,J.;Rao,Y. Adeeplearningframeworkforfinancialtimeseriesusingstackedautoencodersandlong-shortterm
memory. PLoSONE2017,12,e0180944.[CrossRef][PubMed]
108. Lee,C.Y.;Soo,V.W. Predictstockpricewithfinancialnewsbasedonrecurrentconvolutionalneuralnetworks. InProceedings
ofthe2017ConferenceonTechnologiesandApplicationsofArtificialIntelligence(TAAI),Taipei,Taiwan,1–3December2017;
pp.160–165.
109. Kuo,P.H.;Huang,C.J. Anelectricitypriceforecastingmodelbyhybridstructureddeepneuralnetworks. Sustainability2018,
10,1280.[CrossRef]
110. Tian,C.;Ma,J.;Zhang,C.;Zhan,P. Adeepneuralnetworkmodelforshort-termloadforecastbasedonlongshort-termmemory
networkandconvolutionalneuralnetwork. Energies2018,11,3493.[CrossRef]
111. Liu,H.;Mi,X.;Li,Y.Smartdeeplearningbasedwindspeedpredictionmodelusingwaveletpacketdecomposition,convolutional
neuralnetworkandconvolutionallongshorttermmemorynetwork. EnergyConvers.Manag.2018,166,120–131.[CrossRef]
112. Chen,Y.;Wu,J.;Bu,H. Stockmarketembeddingandprediction: Adeeplearningmethod. InProceedingsofthe201815th
InternationalConferenceonServiceSystemsandServiceManagement(ICSSSM),Hangzhou,China,21–22July2018;pp.1–6.
113. Hossain,M.A.;Karim,R.;Thulasiram,R.;Bruce,N.D.;Wang,Y. Hybriddeeplearningmodelforstockpriceprediction. In
Proceedingsofthe2018IEEESymposiumSeriesonComputationalIntelligence(SSCI),Bangalore,India,18–21November2018;
pp.1837–1844.
114. Kim,H.Y.;Won,C.H.Forecastingthevolatilityofstockpriceindex:AhybridmodelintegratingLSTMwithmultipleGARCH-type
models. ExpertSyst.Appl.2018,103,25–37.[CrossRef]
115. Li,Y.; Yu,R.; Shahabi,C.; Liu,Y. DiffusionConvolutionalRecurrentNeuralNetwork: Data-DrivenTrafficForecasting. In
ProceedingsoftheInternationalConferenceonLearningRepresentations,Vancouver,BC,Canada,30April–3May2018.
116. Huang,C.J.;Kuo,P.H.AdeepCNN-LSTMmodelforparticulatematter(PM2.5)forecastinginsmartcities. Sensors2018,18,2220.
[CrossRef]
117. Soh, P.W.; Chang, J.W.; Huang, J.W. Adaptive deep learning-based air quality prediction model using the most relevant
spatial-temporalrelations. IEEEAccess2018,6,38186–38199.[CrossRef]
118. Fan,C.;Zhang,Y.;Pan,Y.;Li,X.;Zhang,C.;Yuan,R.;Wu,D.;Wang,W.;Pei,J.;Huang,H. Multi-horizontimeseriesforecasting
withtemporalattentionlearning. InProceedingsofthe25thACMSIGKDDInternationalConferenceonKnowledgeDiscovery&
DataMining,Anchorage,AK,USA,4–8August2019;pp.2527–2535.
119. Pan,C.;Tan,J.;Feng,D.;Li,Y. Veryshort-termsolargenerationforecastingbasedonLSTMwithtemporalattentionmechanism.
InProceedingsofthe2019IEEE5thInternationalConferenceonComputerandCommunications(ICCC),Chengdu,China,6–9
December2019;pp.267–271.
120. Wang,S.;Wang,X.;Wang,S.;Wang,D. Bi-directionallongshort-termmemorymethodbasedonattentionmechanismandrolling
updateforshort-termloadforecasting. Int.J.Electr.PowerEnergySyst.2019,109,470–479.[CrossRef]

Information2023,14,598 32of35
121. Shen,Z.;Zhang,Y.;Lu,J.;Xu,J.;Xiao,G. Anoveltimeseriesforecastingmodelwithdeeplearning. Neurocomputing2020,
396,302–313.[CrossRef]
122. Pal,R.;Sekh,A.A.;Kar,S.;Prasad,D.K. NeuralnetworkbasedcountrywiseriskpredictionofCOVID-19. Appl. Sci. 2020,
10,6448.[CrossRef]
123. Dudukcu,H.V.;Taskiran,M.;Taskiran,Z.G.C.;Yildirim,T. TemporalConvolutionalNetworkswithRNNapproachforchaotic
timeseriesprediction. Appl.SoftComput.2023,133,109945.[CrossRef]
124. Scarselli,F.;Gori,M.;Tsoi,A.C.;Hagenbuchner,M.;Monfardini,G. Thegraphneuralnetworkmodel. IEEETrans.NeuralNetw.
2008,20,61–80.[CrossRef]
125. Hamilton,W.L. GraphRepresentationLearning;Morgan&ClaypoolPublishers:SanRafael,CA,USA,2020.
126. Cheng,D.;Yang,F.;Xiang,S.;Liu,J. Financialtimeseriesforecastingwithmulti-modalitygraphneuralnetwork. PatternRecognit.
2022,121,108218.[CrossRef]
127. Geng,X.;He,X.;Xu,L.;Yu,J. Graphcorrelatedattentionrecurrentneuralnetworkformultivariatetimeseriesforecasting. Inf.
Sci.2022,606,126–142.[CrossRef]
128. Xiang,S.;Cheng,D.;Shang,C.;Zhang,Y.;Liang,Y. TemporalandHeterogeneousGraphNeuralNetworkforFinancialTime
SeriesPrediction. InProceedingsofthe31stACMInternationalConferenceonInformation&KnowledgeManagement,Atlanta,
GA,USA,17–21October2022;pp.3584–3593.
129. Jin,M.;Zheng,Y.;Li,Y.F.;Chen,S.;Yang,B.;Pan,S. Multivariatetimeseriesforecastingwithdynamicgraphneuralodes. IEEE
Trans.Knowl.DataEng.2022,35,9168–9180.[CrossRef]
130. Liu,Y.;Liu,Q.;Zhang,J.W.;Feng,H.;Wang,Z.;Zhou,Z.;Chen,W.Multivariatetimeseriesforecastingwithtemporalpolynomial
graphneuralnetworks. Adv.NeuralInf.Process.Syst.2022,35,19414–19426.
131. Williams,C.K.;Rasmussen,C.E. GaussianProcessesforMachineLearning;MITPress:Cambridge,MA,USA,2006;Volume2.
132. Berg,C.;Christensen,J.P.R.;Ressel,P. HarmonicAnalysisonSemigroups:TheoryofPositiveDefiniteandRelatedFunctions;Springer:
Berlin/Heidelberg,Germany,1984;Volume100.
133. Hensman,J.;Fusi,N.;Lawrence,N.D. Gaussianprocessesforbigdata. arXiv2013,arXiv:1309.6835.
134. Damianou,A.;Lawrence,N.D. Deepgaussianprocesses. InProceedingsoftheArtificialIntelligenceandStatistics,Scottsdale,
AZ,USA,29April–1May2013;pp.207–215.
135. You,J.;Li,X.;Low,M.;Lobell,D.;Ermon,S. Deepgaussianprocessforcropyieldpredictionbasedonremotesensingdata. In
ProceedingsoftheAAAIConferenceonArtificialIntelligence,SanFrancisco,CA,USA,4–9February2017;Volume31.
136. Mahdi, M.D.; Mrittika, N.J.; Shams, M.; Chowdhury, L.; Siddique, S. ADeepGaussianProcessforForecastingCropYield
andTimeSeriesAnalysisofPrecipitationBasedinMunshiganj,Bangladesh. InProceedingsoftheIGARSS2020—2020IEEE
InternationalGeoscienceandRemoteSensingSymposium,Waikoloa,HI,USA,26September–2October2020;pp.1331–1334.
137. Jiang,Y.;Fan,J.;Liu,Y.;Zhang,X. DeepgraphGaussianprocessesforshort-termtrafficflowforecastingfromspatiotemporal
data. IEEETrans.Intell.Transp.Syst.2022,23,20177–20186.[CrossRef]
138. Chang,W.;Li,R.;Fu,Y.;Xiao,Y.;Zhou,S. Amultistepforecastingmethodforonlinecar-hailingdemandbasedonwavelet
decompositionanddeepGaussianprocessregression. J.Supercomput.2023,79,3412–3436.[CrossRef]
139. Camastra,F.;Casolaro,A.;Iannuzzo,G. TimeSeriespredictionwithmissingdatabyanIteratedDeepGaussianProcess. In
Proceedingsofthe31stEditionofWIRN2023,VietrisulMare,Salerno,Italy,22–26May2023.
140. Goodfellow,I.;Pouget-Abadie,J.;Mirza,M.;Xu,B.;Warde-Farley,D.;Ozair,S.;Courville,A.;Bengio,Y. GenerativeAdversarial
Nets. InProceedingsoftheAdvancesinNeuralInformationProcessingSystems,Montreal,QC,Canada,8–13December2014;
Volume27.
141. Radford,A.;Metz,L.;Chintala,S.Unsupervisedrepresentationlearningwithdeepconvolutionalgenerativeadversarialnetworks.
arXiv2015,arXiv:1511.06434.
142. Mogren,O. C-RNN-GAN:Continuousrecurrentneuralnetworkswithadversarialtraining. arXiv2016,arXiv:1611.09904.
143. Box,G.E.;Jenkins,G.M.;Reinsel,G.C.;Ljung,G.M. TimeSeriesAnalysis:ForecastingandControl;JohnWiley&Sons:Hoboken,NJ,
USA,2015.
144. Wu,D.;Hur,K.;Xiao,Z.AGAN-EnhancedEnsembleModelforEnergyConsumptionForecastinginLargeCommercialBuildings.
IEEEAccess2021,9,158820–158830.[CrossRef]
145. Mirza,M.;Osindero,S. Conditionalgenerativeadversarialnets. arXiv2014,arXiv:1411.1784.
146. Chen,X.;Duan,Y.;Houthooft,R.;Schulman,J.;Sutskever,I.;Abbeel,P. InfoGAN:InterpretableRepresentationLearningby
InformationMaximisingGenerativeAdversarialNets. Adv.NeuralInf.Process.Syst.2016,29.
147. Wang, H.; Tao, G.; Ma, J.; Jia, S.; Chi, L.; Yang, H.; Zhao, Z.; Tao, J. Predicting the epidemics trend of COVID-19 using
epidemiological-basedgenerativeadversarialnetworks. IEEEJ.Sel.Top.SignalProcess.2022,16,276–288.[CrossRef]
148. Wiese,M.;Knobloch,R.;Korn,R.;Kretschmer,P. QuantGANs:Deepgenerationoffinancialtimeseries. Quant.Financ.2020,
20,1419–1440.[CrossRef]
149. Hazra,D.;Byun,Y.C. SynSigGAN:Generativeadversarialnetworksforsyntheticbiomedicalsignalgeneration. Biology2020,
9,441.[CrossRef][PubMed]
150. Esteban,C.;Hyland,S.L.;Rätsch,G. Real-valued(medical)timeseriesgenerationwithrecurrentconditionalgans. arXiv2017,
arXiv:1706.02633.
151. Yoon,J.;Jarrett,D.;VanderSchaar,M. Time-seriesgenerativeadversarialnetworks. Adv.NeuralInf.Process.Syst.2019,32.

Information2023,14,598 33of35
152. Ni, H.; Szpruch, L.; Wiese, M.; Liao, S.; Xiao, B. Conditional sig-wasserstein gans for time series generation. arXiv 2020,
arXiv:2006.05421.
153. Li, X.; Metsis, V.; Wang, H.; Ngu, A.H.H. Tts-gan: A transformer-based time series generative adversarial network. In
ProceedingsoftheInternationalConferenceonArtificialIntelligenceinMedicine,Halifax,NS,Canada,14–17June2022;Springer:
Berlin/Heidelberg,Germany,2022;pp.133–143.
154. Koochali,A.;Schichtel,P.;Dengel,A.;Ahmed,S. Probabilisticforecastingofsensorydatawithgenerativeadversarialnetworks–
ForGAN. IEEEAccess2019,7,63868–63880.[CrossRef]
155. Bej, A.; Maulik, U.; Sarkar, A. Time-Series prediction for the epidemic trends of COVID-19 using Conditional Generative
adversarialNetworksRegressiononcountry-wisecasestudies. SNComput.Sci.2022,3,352.[CrossRef]
156. Zúñiga,G.;Acuña,G. Probabilisticmultisteptimeseriesforecastingusingconditionalgenerativeadversarialnetworks. In
Proceedingsofthe2021IEEELatinAmericanConferenceonComputationalIntelligence(LA-CCI),Temuco,Chile,2–4November
2021;pp.1–6.
157. Huang,X.;Li,Q.;Tai,Y.;Chen,Z.;Liu,J.;Shi,J.;Liu,W. Timeseriesforecastingforhourlyphotovoltaicpowerusingconditional
generativeadversarialnetworkandBi-LSTM. Energy2022,246,123403.[CrossRef]
158. Li,F.;Zheng,H.;Li,X. Anovelhybridmodelformulti-stepaheadphotovoltaicpowerpredictionbasedonconditionaltime
seriesgenerativeadversarialnetworks. Renew.Energy2022,199,560–586.[CrossRef]
159. Zhou,X.;Pan,Z.;Hu,G.;Tang,S.;Zhao,C. Stockmarketpredictiononhigh-frequencydatausinggenerativeadversarialnets.
Math.Probl.Eng.2018,2018,4907423.[CrossRef]
160. Zhang,Y.;Wang,S.;Chen,B.;Cao,J.;Huang,Z. Trafficgan:Network-scaledeeptrafficpredictionwithgenerativeadversarial
nets. IEEETrans.Intell.Transp.Syst.2019,22,219–230.[CrossRef]
161. Kaushik,S.;Choudhury,A.;Natarajan,S.;Pickett,L.A.;Dutt,V. Medicineexpenditurepredictionviaavariance-basedgenerative
adversarialnetwork. IEEEAccess2020,8,110947–110958.[CrossRef]
162. Gu,Y.;Chen,Q.;Liu,K.;Xie,L.;Kang,C. GAN-basedModelforResidentialLoadGenerationConsideringTypicalConsumption
Patterns. InProceedingsofthe2019IEEEPower&EnergySocietyInnovativeSmartGridTechnologiesConference(ISGT),
Washington,DC,USA,18–21February2019;pp.1–5.
163. He,B.;Kita,E. Stockpricepredictionbyusinghybridsequentialgenerativeadversarialnetworks. InProceedingsofthe2020
InternationalConferenceonDataMiningWorkshops(ICDMW),Sorrento,Italy,17–20November2020;pp.341–347.
164. Wu,S.;Xiao,X.;Ding,Q.;Zhao,P.;Wei,Y.;Huang,J. Adversarialsparsetransformerfortimeseriesforecasting. Adv.NeuralInf.
Process.Syst.2020,33,17105–17115.
165. Li, Q.; Hao, H.; Zhao, Y.; Geng, Q.; Liu, G.; Zhang, Y.; Yu, F. GANs-LSTM model for soil temperature estimation from
meteorological:Anewapproach. IEEEAccess2020,8,59427–59443.[CrossRef]
166. Yin,X.;Han,Y.;Sun,H.;Xu,Z.;Yu,H.;Duan,X. Multi-attentiongenerativeadversarialnetworkformultivariatetimeseries
prediction. IEEEAccess2021,9,57351–57363.[CrossRef]
167. Wu,W.;Huang,F.;Kao,Y.;Chen,Z.;Wu,Q. Predictionmethodofmultiplerelatedtimeseriesbasedongenerativeadversarial
networks. Information2021,12,55.[CrossRef]
168. Jiang,C.;Mao,Y.;Chai,Y.;Yu,M. Day-aheadrenewablescenarioforecastsbasedongenerativeadversarialnetworks. Int. J.
EnergyRes.2021,45,7572–7587.[CrossRef]
169. Bendaoud,N.M.M.;Farah,N.;BenAhmed,S. ComparingGenerativeAdversarialNetworksarchitecturesforelectricitydemand
forecasting. EnergyBuild.2021,247,111152.[CrossRef]
170. Wu,X.;Yang,H.;Chen,H.;Hu,Q.;Hu,H. Long-term4Dtrajectorypredictionusinggenerativeadversarialnetworks. Transp.
Res.PartEmerg.Technol.2022,136,103554.[CrossRef]
171. Ye,Y.;Strong,M.;Lou,Y.;Faulkner,C.A.;Zuo,W.;Upadhyaya,S. Evaluatingperformanceofdifferentgenerativeadversarial
networksforlarge-scalebuildingpowerdemandprediction. EnergyBuild.2022,269,112247.[CrossRef]
172. Vuletic´,M.;Prenzel,F.;Cucuringu,M. Fin-Gan:ForecastingandClassifyingFinancialTimeSeriesviaGenerativeAdversarial
Networks.2023. Availableonline:https://ssrn.com/abstract=4328302(accessedon25September2023).
173. Sohl-Dickstein,J.;Weiss,E.;Maheswaranathan,N.;Ganguli,S. Deepunsupervisedlearningusingnonequilibriumthermodynam-
ics. InProceedingsoftheInternationalConferenceonMachineLearning,Lille,France,7–9July2015;pp.2256–2265.
174. Ho,J.;Jain,A.;Abbeel,P. Denoisingdiffusionprobabilisticmodels. Adv.NeuralInf.Process.Syst.2020,33,6840–6851.
175. Song,Y.;Ermon,S. Generativemodelingbyestimatinggradientsofthedatadistribution. Adv.NeuralInf.Process.Syst.2019,32.
176. Song,Y.;Sohl-Dickstein,J.;Kingma,D.P.;Kumar,A.;Ermon,S.;Poole,B. Score-BasedGenerativeModelingthroughStochastic
DifferentialEquations. InProceedingsoftheInternationalConferenceonLearningRepresentations,AddisAbaba,Ethiopia,
26–32April2020.
177. Rasul,K.;Seward,C.;Schuster,I.;Vollgraf,R. Autoregressivedenoisingdiffusionmodelsformultivariateprobabilistictime
seriesforecasting. InProceedingsoftheInternationalConferenceonMachineLearning,Virtual,18–24July2021;pp.8857–8868.
178. Yan,T.;Zhang,H.;Zhou,T.;Zhan,Y.;Xia,Y. ScoreGrad: Multivariateprobabilistictimeseriesforecastingwithcontinuous
energy-basedgenerativemodels. arXiv2021,arXiv:2106.10121.
179. Li,Y.;Lu,X.;Wang,Y.;Dou,D. Generativetimeseriesforecastingwithdiffusion,denoise,anddisentanglement. Adv.NeuralInf.
Process.Syst.2022,35,23009–23022.

Information2023,14,598 34of35
180. Biloš,M.;Rasul,K.;Schneider,A.;Nevmyvaka,Y.;Günnemann,S. Modelingtemporaldataascontinuousfunctionswithprocess
diffusion. arXiv2022,arXiv:2211.02590.
181. Vaswani,A.;Shazeer,N.;Parmar,N.;Uszkoreit,J.;Jones,L.;Gomez,A.N.;Kaiser,Ł.;Polosukhin,I. Attentionisallyouneed.
Adv.NeuralInf.Process.Syst.2017,30.
182. Zhou,H.;Zhang,S.;Peng,J.;Zhang,S.;Li,J.;Xiong,H.;Zhang,W. Informer:Beyondefficienttransformerforlongsequence
timeseriesforecasting. InProceedingsoftheAAAIConferenceonArtificialIntelligence,Virtual,2–9February2021;Volume35,
pp.11106–11115.
183. Wu,H.;Xu,J.;Wang,J.;Long,M. Autoformer:Decompositiontransformerswithauto-correlationforlong-termseriesforecasting.
Adv.NeuralInf.Process.Syst.2021,34,22419–22430.
184. Zhou,T.;Ma,Z.;Wen,Q.;Wang,X.;Sun,L.;Jin,R. Fedformer: Frequencyenhanceddecomposedtransformerforlong-term
seriesforecasting. InProceedingsoftheInternationalConferenceonMachineLearning,Baltimore,MD,USA,17–23July2022;
pp.27268–27286.
185. He,K.;Zhang,X.;Ren,S.;Sun,J. Deepresiduallearningforimagerecognition. InProceedingsoftheIEEEConferenceon
ComputerVisionandPatternRecognition,LasVegas,NV,USA,26June–1July2016;pp.770–778.
186. Ba,J.L.;Kiros,J.R.;Hinton,G.E. Layernormalization. arXiv2016,arXiv:1607.06450.
187. Luong,T.;Pham,H.;Manning,C.D. EffectiveApproachestoAttention-basedNeuralMachineTranslation. InProceedingsofthe
2015ConferenceonEmpiricalMethodsinNaturalLanguageProcessing,Lisbon,Portugal,17–21September2015;Associationfor
ComputationalLinguistics:Cedarville,OH,USA,2015;pp.1412–1421.
188. Li,S.;Jin,X.;Xuan,Y.;Zhou,X.;Chen,W.;Wang,Y.X.;Yan,X. Enhancingthelocalityandbreakingthememorybottleneckof
transformerontimeseriesforecasting. Adv.NeuralInf.Process.Syst.2019,32.
189. Wang,S.;Li,B.Z.;Khabsa,M.;Fang,H.;Ma,H. Linformer:Self-attentionwithlinearcomplexity. arXiv2020,arXiv:2006.04768.
190. Donoho,D.L. Compressedsensing. IEEETrans.Inf.Theory2006,52,1289–1306.[CrossRef]
191. Nie,Y.; Nguyen,N.H.;Sinthong,P.;Kalagnanam,J. ATimeSeriesisWorth64Words:Long-termForecastingwithTransformers.
InProceedingsoftheInternationalConferenceonLearningRepresentations,Kigali,Rwanda,1–5May2023.
192. Zhang,Y.;Yan,J. Crossformer:Transformerutilisingcross-dimensiondependencyformultivariatetimeseriesforecasting. In
ProceedingsoftheEleventhInternationalConferenceonLearningRepresentations,Kigali,Rwanda,1–5May2022.
193. Liu,S.;Yu,H.;Liao,C.;Li,J.;Lin,W.;Liu,A.X.;Dustdar,S. Pyraformer:Low-ComplexityPyramidalAttentionforLong-Range
TimeSeriesModelingandForecasting. InProceedingsoftheInternationalConferenceonLearningRepresentations,Virtual,
25–29April2022.
194. Shabani, M.A.; Abdi, A.H.; Meng, L.; Sylvain, T. Scaleformer: Iterative Multi-scale Refining Transformers for Time Series
Forecasting. InProceedingsoftheTheEleventhInternationalConferenceonLearningRepresentations,Kigali,Rwanda,1–5
May2023.
195. Cirstea,R.G.;Guo,C.;Yang,B.;Kieu,T.;Dong,X.;Pan,S. Triformer:Triangular,Variable-SpecificAttentionsforLongSequence
MultivariateTimeSeriesForecasting–FullVersion. arXiv2022,arXiv:2204.13767.
196. Liu,Y.;Wu,H.;Wang,J.;Long,M. Non-stationarytransformers:Exploringthestationarityintimeseriesforecasting. Adv.Neural
Inf.Process.Syst.2022,35,9881–9893.
197. Schirmer, M.; Eltayeb, M.; Lessmann, S.; Rudolph, M. Modelingirregulartimeserieswithcontinuousrecurrentunits. In
ProceedingsoftheInternationalConferenceonMachineLearning,Baltimore,MD,USA,17–23July2022;pp.19388–19405.
198. Zhou,T.;Ma,Z.;Wen,Q.;Sun,L.;Yao,T.;Yin,W.;Jin,R. Film:Frequencyimprovedlegendrememorymodelforlong-termtime
seriesforecasting. Adv.NeuralInf.Process.Syst.2022,35,12677–12690.
199. Ekambaram,V.;Jati,A.;Nguyen,N.;Sinthong,P.;Kalagnanam,J. TSMixer:LightweightMLP-MixerModelforMultivariateTime
SeriesForecasting. InProceedingsofthe29thACMSIGKDDConferenceonKnowledgeDiscoveryandDataMining,LongBeach,
CA,USA,6–10August2023;pp.459–469.
200. Wang,H.;Peng,J.;Huang,F.;Wang,J.;Chen,J.;Xiao,Y. MICN:Multi-scaleLocalandGlobalContextModelingforLong-term
SeriesForecasting. InProceedingsoftheEleventhInternationalConferenceonLearningRepresentations,Kigali,Rwanda,1–5
May2023.
201. Mackey,M.C.;Glass,L. Oscillationandchaosinphysiologicalcontrolsystems. Science1977,197,287–289.[CrossRef][PubMed]
202. Weiss,C.O.;Hübner,U.;Abraham,N.B.;Tang,D. Lorenz-likechaosinNH3-FIRlasers. InfraredPhys.Technol.1995,36,489–512.
[CrossRef]
203. Aguirre,L.A.;Rodrigues,G.G.;Mendes,E.M. Nonlinearidentificationandclusteranalysisofchaoticattractorsfromareal
implementationofChua’scircuit. Int.J.Bifurc.Chaos1997,7,1411–1423.[CrossRef]
204. Wijngaard,J.;KleinTank,A.;Können,G. Homogeneityof20thcenturyEuropeandailytemperatureandprecipitationseries. Int.
J.Climatol.J.R.Meteorol.Soc.2003,23,679–692.[CrossRef]
205. Weigend,A.S.;Gershenfeld,N.A.TimeSeriesPrediction:ForecastingtheFutureandUnderstandingthePast;SantaFeInstituteStudies
intheSciencesofComplexity:SantaFe,NM,USA,1994.
206. Jospin,L.V.;Laga,H.;Boussaid,F.;Buntine,W.;Bennamoun,M. Hands-onBayesianneuralnetworks—Atutorialfordeep
learningusers. IEEEComput.Intell.Mag.2022,17,29–48.[CrossRef]
207. Lu,J.;Liu,A.;Dong,F.;Gu,F.;Gama,J.;Zhang,G. Learningunderconceptdrift:Areview. IEEETrans.Knowl.DataEng.2018,
31,2346–2363.[CrossRef]

Information2023,14,598 35of35
208. Hyvärinen,A.;Dayan,P. Estimationofnon-normalizedstatisticalmodelsbyscorematching. J.Mach.Learn.Res.2005,6.
209. Vincent,P. Aconnectionbetweenscorematchinganddenoisingautoencoders. NeuralComput.2011,23,1661–1674.[CrossRef]
[PubMed]
210. Song,Y.;Garg,S.;Shi,J.;Ermon,S. Slicedscorematching:Ascalableapproachtodensityandscoreestimation. InProceedingsof
theUncertaintyinArtificialIntelligence,Virtual,3–6August2020;pp.574–584.
211. Anderson,B.D. Reverse-timediffusionequationmodels. Stoch.Process.TheirAppl.1982,12,313–326.[CrossRef]
212. Papoulis,A.;UnnikrishnaPillai,S. Probability,RandomVariablesandStochasticProcesses;McGraw-Hill:NewYork,NY,USA,2002.
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.