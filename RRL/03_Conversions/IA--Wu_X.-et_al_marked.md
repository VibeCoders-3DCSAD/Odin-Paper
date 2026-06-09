applied
sciences
Article
Optimizing Recurrent Neural Networks: A Study on Gradient
Normalization of Weights for Enhanced Training Efficiency
XinyiWu1,BingjieXiang1,HuaizhengLu2,ChaopengLi1,*,XingwangHuang2 andWeifangHuang1
1 SchoolofOceanInformationEngineering,JimeiUniversity,Xiamen361021,China;
202121306003@jmu.edu.cn(X.W.);jerryxiang@jmu.edu.cn(B.X.);202121306075@jmu.edu.cn(W.H.)
2 CollegeofComputerEngineering,JimeiUniversity,Xiamen361021,China;luhuaizheng@jmu.edu.cn(H.L.);
huangxw@jmu.edu.cn(X.H.)
* Correspondence:licp@jmu.edu.cn
Abstract:RecurrentNeuralNetworks(RNNs)areclassicalmodelsforprocessingsequentialdata,
demonstratingexcellentperformanceintaskssuchasnaturallanguageprocessingandtimeseries
prediction.However,duringthetrainingofRNNs,theissuesofvanishingandexplodinggradients
oftenarise,significantlyimpactingthemodel’sperformanceandefficiency. Inthispaper,wein-
vestigatewhyRNNsaremorepronetogradientproblemscomparedtoothercommonsequential
networks.Toaddressthisissueandenhancenetworkperformance,weproposeamethodforgradient
normalizationofnetworkweights. Thismethodsuppressestheoccurrenceofgradientproblems
byalteringthestatisticalpropertiesofRNNweights,therebyimprovingtrainingeffectiveness.Ad-
ditionally,weanalyzetheimpactofweightgradientnormalizationontheprobability-distribution
characteristicsofmodelweightsandvalidatethesensitivityofthismethodtohyperparameters
suchaslearningrate.Theexperimentalresultsdemonstratethatgradientnormalizationenhances
thestabilityofmodeltrainingandreducesthefrequencyofgradientissues.OnthePennTreebank
dataset,thismethodachievesaperplexitylevelof110.89,representingan11.48%improvementover
conventionalgradientdescentmethods.Forpredictionlengthsof24and96ontheETTm1dataset,
MeanAbsoluteError(MAE)valuesof0.778and0.592areattained,respectively,resultingin3.00%
Citation:Wu,X.;Xiang,B.;Lu,H.; and6.77%improvementoverconventionalgradientdescentmethods.Moreover,selectedsubsetsof
Li,C.;Huang,X.;Huang,W. theUCRdatasetshowanincreaseinaccuracyrangingfrom0.4%to6.0%.Thegradientnormalization
OptimizingRecurrentNeural methodenhancestheabilityofRNNstolearnfromsequentialandcausaldata, therebyholding
Networks:AStudyonGradient significantimplicationsforoptimizingthetrainingeffectivenessofRNN-basedmodels.
NormalizationofWeightsfor
EnhancedTrainingEfficiency.Appl. Keywords:recurrentneuralnetworks;vanishinggradients;explodinggradients;gradientnormalization;
Sci.2024,14,6578. https://doi.org/
probabilitydistributioncharacteristics
10.3390/app14156578
AcademicEditor:LuisJavier
GarciaVillalba
1. Introduction
Received:31May2024
RecurrentNeuralNetworks(RNNs)arecharacterizedbyperiodicmemorycapacity
Revised:23July2024
andthusareabletoretainpreviousinformationwhileprocessingsequentialdata,andthey
Accepted:24July2024
are widely used in the fields of natural language processing [1], speech recognition [2],
Published:27July2024
imagedescription[3],videoanalytics[4],andsoon.
DespitetheemergenceofvariousimprovedRNNmodelslikeLSTMandGRU,af-
ter years of research, their core structure remains recurrent. That is, at each time step,
Copyright: © 2024 by the authors. theyutilizethecurrentinputalongwiththehiddenstatefromtheprevioustimestepto
Licensee MDPI, Basel, Switzerland. computetheoutputandthehiddenstateforthenexttimestep.However,itisthisrecurrent
Thisarticleisanopenaccessarticle structurethatprimarilymakesRNNmodelsmoresusceptibletoissuessuchasvanishing
distributed under the terms and andexplodinggradientscomparedtofeedforwardmodels.
conditionsoftheCreativeCommons
Thecausesofgradientproblemscangenerallybedividedintotwocategories. Oneis
Attribution(CCBY)license(https://
the gradient cumulative product hypothesis [5], and the other is the neuron saturation
creativecommons.org/licenses/by/
hypothesis [6]. The former suggests that gradient disappearance and explosion mainly
4.0/).
Appl.Sci.2024,14,6578.https://doi.org/10.3390/app14156578 https://www.mdpi.com/journal/applsci

Appl.Sci.2024,14,6578 2of18
occurbecause,duringthebackwardpropagationprocessofmodeltraining,thegradientof
weightsiscalculatedprogressivelythroughthe“chainrule”. Asthedepthoftheneural
networkincreases,thegradientsofweightsclosertothebottomlayerbecomeincreasingly
smaller or larger. If the gradient is too small, it is referred to as a vanishing gradient;
ifitistoolarge, itiscalledanexplodinggradient. Thelattersuggeststhatthecauseof
gradientproblemsliesinthenonlinearityofneuronfunctionsandtheexistenceofactivation
andinhibitionzones. Thishypothesissuggeststhatcommonneuronfunctions,suchas
Sigmoid [7], Tanh [8], or ReLU [9], have gradients that are nonlinear. For instance, the
gradientsoftheSigmoidandTanhfunctionsaresmallwhentheabsolutevalueoftheinput
isgreaterthan1,leadingtonon-activation,whileReLUisnon-activatedinthenegative
domain. Alargenumberofneuronsenteringthenon-activationzoneintheneuralnetwork
willcausethemodeltoloseitslearningability,ultimatelyresultinginthefailureofmodel
trainingtoconverge.
The mechanism behind the gradient problems in RNN models is explored in this
article. Firstly,wefindthatduringthemodeltrainingprocess,rapidchangesinstatistical
variablesofweightgradientssuchasmeanandvarianceoftenleadtoalargenumberof
activationsofthemodel’sactivationfunctionsenteringtheinhibitionzone. Atthesame
time,therecurrentstructurecharacteristicofRNNmodelsimpliesthatthehiddenlayer
weightsarereusedacrossthetime-stepdimension,leadingtoresonanceinthevariation
ofstatisticalweightpropertiesacrossthetime-stepdimension. Duringtraining,almost
synchronousoccurrencesofgradientexplosionsanddisappearanceshappenatdifferent
timesteps(asshowninFigure1),andthereisasignificantsynchronouseffectbetween
thesuddenincreaseinweightgradientvariance,asuddenincreaseinlossvalue,anda
large number of neurons entering the inhibition zone. To suppress gradient problems,
weproposeaweightgradientnormalizationmethod(WGN)thatoptimizesthestatistical
parameters of weights such as mean, variance, etc., during the model training process,
avoidingabruptchangesinweightdistributioncharacteristics. Throughtheanalysisand
derivationofparameterssuchascovariancebetweenweightinitialvaluesandgradients,
covariancebetweenweightgradients,learningrate,etc.,wedemonstratethatthemethodis
effectiveinensuringthatthemeanoftheweightsandtherateofchangeofthevarianceare
stable. Inexperiments,weapplytheweightgradientnormalizationmethodtoLSTM[10]
and Simple-RNN models and validate its effectiveness on the MINIST [11], PTB [12],
ETTm1[13],andUCR[14]datasets. Finally,wediscusstheapplicabilityandscalabilityof
thismethod.
Figure1.Fromlefttorightaretheprobabilityactivationplotsofneuronsatdifferenttimestepsand
iterations,thegraphdepictingthephenomenonoflossexplosion,andthecorrespondingparameter
gradientplots.Byobservation,itcanbenotedthatthereisacorrespondingrelationshipbetweenthe
abruptchangesinthecurvesinthesethreeplots.
Theinnovationofthispaperisasfollows:
1. Fromtheperspectiveofthevarianceandcovarianceofweightgradients, thephe-
nomenonofgradientexplosionanddisappearanceinrecurrentneuralnetworksis
explored,tosomeextentexplainingthecausesofgradientproblems.

Appl.Sci.2024,14,6578 3of18
2. Basedonstatistics,aweightgradientnormalizationmethodisproposed,whichcan
effectivelyacceleratethetrainingspeedwhilesuppressinggradientexplosionand
disappearanceduringthetrainingprocess.
3. Aquantificationmethodforthedegreeofgradientanomalyisproposed,providinga
basisforevaluatingtheeffectivenessofgradientproblemsuppressionmethods.
2. RelatedWork
Asmentionedabove,thecausesofthegradientvanishingandexplodingphenomenon
indeeplearningareexplainedbytwocategories: gradientcumulativemultiplicationand
neuron inhibition. Specifically, in the case of recurrent neural network (RNN) models,
duetotheiruniquearchitectureandweightreuse,themodelismorepronetoencountering
gradientissuesduringthetrainingprocess.
Asearlyasthe1990s,YoshuaBengioandothersarguedthattrainingneuralnetwork
modelsoverlongtimeperiodswasdifficultduetothephenomenonofgradientvanishing
in models like RNNs [15]. Bengio used a model structure with only a single recurrent
neuronasanexampletoillustratethat,asthemodelwastrained,thepartialderivativesof
themodel’sobjectivefunctionwithrespecttothemodel’srecurrentlayerweightswould
decrease and even vanish as the model’s time period increased. Later, in 2012, Razvan
Pascanuandothersdiscoveredthatunderdifferentweightinitializationconditions,model
trainingcouldalsoleadtosituationswherethepartialderivativesoftheobjectivefunction
withrespecttotheweightsincreasedandapproachedinfinityasthetimeperiodprogressed,
aphenomenontermedgradientexplosion[16]. Withtheriseofdeeplearning,numerous
researchersfoundthatgradientvanishingorexplosionphenomenacouldalsooccurwhen
training deep feedforward neural networks [17]. Compared to RNN-like models, the
structureoffeedforwardneuralnetworkmodelsisrelativelysimpler, andbyadjusting
hyperparametersreasonably,gradientproblemscanbeeasilysuppressedandresolved.
There are multiple existing solutions to gradient problems, broadly classified into
threecategories: modeltransformation,gradientclipping,andnormalization.
Modeltransformationmethodsincludealteringneuronfunctions,convertingneuron
functionstogatestructures,andemployingresidualstructuressuchasResNet. Chang-
ingneuronfunctionsinvolvesreplacingtraditionalSigmoid[7]orTanh[8]functionsof
Simple-RNNrecurrentlayerswithnovelfunctionslikeReLU[9],SeLU[18],orELU[19].
Thesenovelneuronfunctionseffectivelyexpandtheactivationrangeofneuronfunctions
comparedtotraditionalsigmoidandtanhfunctions,preventingindividualneuronsfrom
fallingintoinhibitionzonesandlosinglearningcapability. Additionally,replacingneuron
functionsofrecurrentlayerswithgatestructurescansignificantlyenhancethememory
capacityofRNNmodels. CommonlyoptimizedRNNmodelswithgatestructuresinclude
LSTM[20]andGRU[21]. Theseapproachesaddressthegradientproblembytransforming
theneuronfunctionintoathresholdfunction. Theyarecommonlyemployedintheprocess-
ingoftime-seriessignalsandcausaldataduetotheircapacitytomitigatetheoccurrenceof
gradientvanishingorexplodingduringmodeltrainingtoacertainextent. Nevertheless,
thenecessitytomaintainandupdatemultiplethresholdstructuresinLSTMmodelsrenders
themmorecomputationallyexpensiveanddifficulttoparallelizeeffectively. Consequently,
models with very long sequences remain susceptible to the gradient problem. Related
studies[22]indicatethatcomparedtogradientexplosion,modelslikeLSTMarebetterat
suppressinggradientvanishing. Thesemethodsareempiricaltechniquesthatdonotfunda-
mentallysolvegradientproblemsmechanistically,andeffectivemathematicalexplanations
forgradientproblemsinRNNmodelsarestilllacking.
Gradientclipping[23]iscurrentlyacommontechniqueusedintrainingneuralnet-
works,thecoreideaofwhichistolimitthegradientvaluebeforethegradientisupdated.
In the event that the magnitude of the gradient exceeds a pre-established threshold, it
isscaledtofallwithinthespecifiedrange. Twoprincipalmethodsofgradientclipping
exist: gradientparadigmclipping, whichpreservesthedirectionofthegradientvector
whilereducingitslength,andgradientvalueclipping,whichmayalterthedirectionof

Appl.Sci.2024,14,6578 4of18
thegradientvectorbutensuresthattheabsolutevalueofthegradientremainswithina
reasonablerange. Althoughgradientclippingplaysanimportantroleinpreventinggradi-
entexplosion,ithastwomainlimitations. Firstly,gradientclippingcanonlybeusedto
preventgradientexplosion,andforanothercommonproblem,gradientvanishing,where
thegradientvaluesaretoosmallforthemodeltoeffectivelylearn,gradientclippingdoes
notprovideadirectsolution. Secondly,gradientclippingrequiresrepeatedexperiments
andmanualadjustmentofthresholdstoachievesatisfactoryresults. Thisisbecausethe
appropriateclippingthresholdoftendependsonthespecificmodelstructureanddataset
withoutauniversalstandard,requiringresearchersorengineerstodeterminetheoptimal
clippinglevelthroughcontinuousexperimentation.
Normalizationmethods, representedbybatchnormalization(BN),areonetypeof
these approaches. BN normalizes the values within a batch for the inputs of neuron
functions,ensuringthatthemodelcancontinuelearningwithlessinternalcovariateshifting
andinputdistributionduringtraining,therebyacceleratingtheprocess. Inaddition,the
batchnormalizationmethodcanstabilizetheactivationvaluesofthenetworkthroughout
thetrainingprocess,therebyreducingthegradientproblemthatarisesduetochangesin
datadistribution. However,thebatch-normalizationmethodissusceptibletoalterationsin
thebatchsizesetting. Ininstanceswherethebatchsizeisrelativelysmall,theestimationof
themeanandvarianceofthesampleswithinthebatchmaynotbesufficientlyaccurate.
Furthermore, the forced scaling of the input data may result in the destruction of the
featuredistributionoftheoriginaldata. BNhasshowngoodperformanceinconventional
deepneuralnetworks,butthereisrelativelylessresearchonitsapplicationinRNN-type
networks,andsomeconclusionsarecontradictory: CésarLaurentfoundintheirstudy[24]
thathorizontalBNhadadetrimentaleffect,whileverticalBNcouldaccelerateparameter
convergence. DarioAmodei’sresearchalsoreachedtheconclusionthatthehorizontalBN
hasadetrimentaleffectandadditionallyfoundthatifthedepthoftheverticaldirection
networkisnotdeepenough,verticalBNwouldalsohaveadetrimentaleffect[25].However,
TimCooijmansoverturnedtheaforementionedconclusion[26],provingthathorizontal
BNcansimultaneouslyacceleratetrainingconvergenceandimprovemodelgeneralization.
HebelievedthatthereasonwhyBNdoesnotperformwellinthehorizontaldirectionin
thefirsttwoworksislikelyduetotheimpropersettingofthescaleparameteroftheBN.
Subsequently,TahminaZebinintroducedBNintoLSTMmodels[27],achievinghuman
activityrecognitiononsmartphones, thusvalidatingthefeasibilityofBNinRNN-type
models. Thesenormalizationmethodsarewidelyusedinfeedforwardneuralnetwork
models,showinggoodperformanceinhandlingimagedata,butthereisalackofresearch
ontheireffectivenessinRNNmodels.
Inconclusion, whilethesethreecategoriesofmethodsareeffectivetosomeextent
in mitigating the gradient explosion and vanishing issues in RNN-type models, there
stillexistlimitationssuchasslowconvergencespeed,complexhyperparametertuning,
andalackofeffectivemathematicalexplanations. Therefore,thispaperproposesanovel
weight-gradientnormalizationmethodtailoredforRNNmodels.
3. WGNforRNNs
3.1. ExperimentalModel
In this paper, the analysis primarily focuses on time-series models such as RNNs
and LSTMs. RNNs (as shown in Figure 2) are a type of recurrent neural network with
astructurethatincorporatestemporalfeedback,enablingthemodelingofsequentialdata.
Denotingtimesteptandgivenaninputvector(x1,x2,...,xt),thegenerationofahidden
statevector(h1,h2,...,ht)isdefinedasEquation(1):
ht = ∅(W ×ht−1+W ×xt) (1)
hh ih
whereW denotestheweightsbetweenneuronsatdifferenttimesteps,W denotesthe
hh ih
weightsbetweeninputsandneurons,andthe∅functionistheactivationfunction.

Appl.Sci.2024,14,6578 5of18
Figure2.TheRNNmodeldiagramshowsthestructureoftheRNNmodelafterunfoldingaccording
tothetimestep.
LSTMisanimprovednetworkstructurebasedonRNNs,whicheffectivelyaddresses
theissueoflong-termdependencies. ThecoreofLSTMisthememorycell,whichcanstore
informationandretrieveitwhenneeded.Informationwithinthememorycellcanbeadded,
deleted,orupdatedthroughgatecontrol,therebyachievingtheeffectoflong-termmemory.
ThestructureofLSTMincludesinputgates,forgetgates,andoutputgates,corresponding
tocontrollingtheflowofinputinformation,controllingtheflowofforgetinformation,and
controllingtheflowofoutputinformation,respectively. Thesegatescanbeadjustedin
theiropenorclosedstatesthroughlearning.
 f˜
t
  o i ˜ ˜ t t    =W h ×h t−1 +W x ×x t +b (2)
g˜
t
c t = σ(f˜ t )⊙c t−1 +σ(i˜ t )⊙tanh(g˜ t ) (3)
h = σ(o˜)⊙tanh(c ) (4)
t t t
where f˜ denotestheforgetgate,i˜ representstheinputgate,o˜ signifiestheoutputgate,g˜
t t t t
standsforthenewmemorygate,c denotesthecellstate,h representsthehiddenlayer
t t
outputattimestept,W representstheweightmatrixofneuronconnections,W istheinput
h x
weightmatrix,x standsfortheinput,andbrepresentsthebiasesoftherespectivegates.
t
3.2. ProposedWeightGradientNormalization
Whenusingrecurrentneuralnetworks,differencesinthegradientmagnitudesacross
differenttimestepsandbatchescanleadtoinstabilityinparameterupdatesifthegradient
valuesatcertaintimestepsaretoolarge,causingmodeloscillationorfailuretoconverge.
Conversely,ifgradientvaluesaretoosmall,parameterupdatesmaybenegligible,resulting
insloworstagnantconvergenceandthusaffectingthemodel’sconvergencespeedand
performance. Inconventionaltrainingprocesses,modelscontinuouslyupdateparameters
tominimizethelossfunctionbycomputinggradientsofthelossfunctionwithrespectto
modelparametersusinggradientdescentalgorithms. Thispaperproposesanovelweight
updatemethod,weightgradientnormalization(WGN),whosespecificimplementation
formulaisshowninEquation(5):

Appl.Sci.2024,14,6578 6of18
params.grad−params.grad_mean
params = params−η× (5)
params.grad_std+δ
whereparamsdenotestheparameterweights, params.gradrepresentstheweightgradients,
params.grad_meanstandsforthemeanoftheweightgradients, params.grad_stdsignifies
thevarianceoftheweightgradients,δdenotesthebiascorrectionvalue,andηrepresents
thescalingfactor.
In our formula, we normalize the gradients of each weight, standardize the mean
andvarianceofgradientsforeachtrainingiteration,andutilizeparameterstocontrolthe
contributionofthisnormalization,makingWGNapplicabletomostdatasets. Duringex-
perimentation,differentvaluesaresetforvariousdatasets,andtherangeoflossvariations
canbeeffectivelyandstablycontrolledbyadjustingthehyperparameterstospeedupthe
convergenceprocessofthemodel. Experimentationindicatesthattherangeofηbetween
0.005and0.0001ismosteffective. Theparameterisusedtomaintainasteadychangeinthe
varianceoftheweights,whichisalinearchangeaboutt.
Traditionalgradientupdatemethodssuchasstochasticgradientdescent(SGD)and
momentumgradientdescent(Adam)donotaccountforthegradientcorrelationbetween
consecutive time steps and overall information. By employing the gradient update ap-
proachofweightgradientnormalization(WGN),boththefirst-andsecond-momentesti-
matesofthegradientsarecombined,enablingthegradientsofindividualdimensionsof
aparametertoshareinformationwitheachother. Thisadjustmentinthemagnitudeof
gradientsensuresthatthemeanofgradientsapproacheszeroandthevarianceapproaches
one. Withintheparameterspace,theWGNmethodnotonlyconsidersinformationfrom
individualpointsbutalsoaggregatesinformationfromneighboringpoints,facilitatinga
morerobustsearchinacomplexstructuredparameterspace. Asgradientsflowthroughthe
forwardupdatesandbackwardpropagation,theWGNmethodcontinuouslynormalizes
thegradients,ensuringsmoothchangesingradientsthroughoutthetrainingprocessand
consequentlysteadyincrementsinweights.
Comparedtotheoriginalstochasticgradientdescent,theWGNalgorithmachievesa
refinedimprovementingradientupdatingbyperforminganadditionalmeanandstandard
deviation calculation step on the gradient. Although WGN significantly improves the
stability of the weight updating process, it also inevitably brings about an increase in
the time complexity, which is O(N×train_num×epoch_num), where N is the size of
theweights,train_numisthetotalnumberofsamplesfortraining,andepoch_numisthe
total number of training rounds. After quantitative analysis, we can find that the time
complexityofWGNbelongstothesameorderofmagnitudeasthatofSGD,butthetime
complexityofWGNisincreasedbyaboutseventoeighttimesmorecomplexitythanSGD.
ConsideringthatWGNdoesnotchangethemainorderofmagnitudeofthealgorithmand
itsimprovementintheoverallperformanceofthemodel,weconsiderthisincrementtobe
withinacceptablelimits.
3.3. MathematicalExplanationoftheWGN
Inthissection,takingthesimpleRNNasanexample,weanalyzetheWGNmethod
mathematically. Accordingtothemodeltrainingprocess,afternormalization,thesparsity
oftheweightgradientmatrixdecreases,andthevarianceapproaches1. Thedistributionof
theweightgradientmatrixbeforeandafternormalizationisshowninFigure3.
TheformulaforweightupdateisshowninEquation(6):
iter
witer = witer−1−∆witer = w0− ∑ η∆wi,iter =0,1,...,n (6)
i=1
∆wi−E (cid:0)∆wi(cid:1)
∆wi = (cid:113) (7)
Var
(cid:0)∆wi (cid:1)
+δ

Appl.Sci.2024,14,6578 7of18
wherewdenotestheweightofthemodel,witerrepresentstheweightsattheiter-thiteration
oftraining,w0denotesthemodel’sinitializedweights,ηstandsforthelearningrate,and
∆widenotesthenormalizedgradient. TakingthemeanonbothsidesofEquation(6)and
considering E(η∆wi) = 0,weobtainEquation(8). Afternormalization,themeanofthe
weightsremainsinagoodinitialstate.
(cid:16) (cid:17) (cid:16) (cid:17)
E witer = E w0 (8)
Figure3. Thetoptwoplotsdepictthedistributionandheatmapoftheunnormalizedgradients,
whilethebottomtwoplotsdepictthedistributionandheatmapofthenormalizedgradients,where
thereddashedlineindicatesthemeanandthegreendashedlineindicatespositiveornegative
standarddeviation,respectively.Byobservingthedistributionandheatmapofthenormalizedand
unnormalizedgradients,itcanbeobservedthatthemeanofthegradientsafternormalizationiscloser
to0,andtheirvarianceiscloserto1.Thesparsityofthegradientmatrixdecreasesafternormalization.
SolvingforthevarianceofbothsidesoftheEquation(6)yieldsEquation(9):
(cid:32) (cid:33) (cid:32) (cid:33)
(cid:16) (cid:17) (cid:16) (cid:17) iter iter
Var witer =Var w0 +η2Var ∑∆wi −2cov w0,η ∑∆wi (9)
i=1 i=1
Expandingη2Var(∑iter ∆wi)yieldsEquation(10):
i=1
(cid:32) (cid:33) (cid:32) (cid:32) (cid:33) (cid:32) (cid:33)(cid:33)
iter (cid:16) (cid:17) iter iter
η2Var ∑∆wi = η2 Var ∆w1 +Var ∑∆wi +2cov ∆w1, ∑∆wi (10)
i=1 i=2 i=2
SinceVar(∆wi)isconstantat1afternormalization,andsoon,thesimplificationleads
toEquation(11).
(cid:32) (cid:33) (cid:32) (cid:33)
iter (cid:16) (cid:17) i iter (cid:16) (cid:17)
η2Var ∑ Var ∆wi = η2 iter+2 ∑ ∑ cov ∆wi,∆wj (11)
i=1 i=1j=i+1

Appl.Sci.2024,14,6578
8of18
|     | Expandingcov(w0,η∑iter |     |     |     | ∆wi)yieldsEquation(12). |     |     |     |     |     |     |
| --- | ---------------------- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |
i=1
|     | (cid:32)                | iter | (cid:33) | (cid:32)                                      |          |          | (cid:32)(cid:32) | iter | (cid:33) (cid:32) | iter (cid:33)(cid:33)(cid:33) |      |
| --- | ----------------------- | ---- | -------- | --------------------------------------------- | -------- | -------- | ---------------- | ---- | ----------------- | ----------------------------- | ---- |
|     |                         | ∑∆wi |          |                                               | (cid:16) | (cid:16) | (cid:17)(cid:17) | ∑    |                   | ∑                             |      |
|     | cov w0,η                |      |          | = E                                           | w0−E     | w0       | ·                | η∆wi | −E                | η∆wi                          | (12) |
|     |                         | i=1  |          |                                               |          |          |                  | i=1  |                   | i=1                           |      |
|     |                         |      |          | η∆wi)andE(η∆wi)are0,thefurtherexpansionofE(w0 |          |          |                  |      |                   |                               | ∆wi) |
|     | SincethevaluesofE(∑iter |      |          |                                               |          |          |                  |      |                   |                               | ·    |
i=1
leadstoEquation(13).
|     |     |     |     | (cid:32) |      | (cid:33) |      |          |          |     |      |
| --- | --- | --- | --- | -------- | ---- | -------- | ---- | -------- | -------- | --- | ---- |
|     |     |     |     |          | iter |          | iter | (cid:16) | (cid:17) |     |      |
|     |     |     |     | w0,      | ∑∆wi |          | ∑    | w0·∆wi   |          |     |      |
|     |     |     |     | cov      |      |          | = η  | cov      |          |     | (13) |
|     |     |     |     |          | i=1  |          | i=1  |          |          |     |      |
Thus,Equation(9)canbesummarizedasEquation(14).
(cid:16) (cid:17) (cid:16) (cid:17) iter iter (cid:16) (cid:17) iter (cid:16) (cid:17)
| witer =Var | w0 +η2·iter+2η2· |     |     | ∑        | ∑   | ∆wi,∆wj |     | −2η ∑ | w0·∆wj |     |      |
| ---------- | ---------------- | --- | --- | -------- | --- | ------- | --- | ----- | ------ | --- | ---- |
| Var        |                  |     |     |          | cov |         |     | cov   |        |     | (14) |
|            |                  |     |     | i=1j=i+1 |     |         |     | i=1   |        |     |      |
BysummingupthelasttwotermsofEquation(14),thesumisfoundtobecloseto
0 when choosing a suitable value of η. There are two cases: one is that η is 0, which is
obviouslyimpossible,andtheotheristhatηsatisfiesthecaseasinEquation(15),andthere
(cid:0) witer(cid:1)
still exists a residual term about iter, and Var can be made roughly linear with
iteration,asshownspecificallyinFigure4.
|     |     |     |     |    |         | 2η∑i ter             | cov(w0·∆wi) |             |     |     |      |
| --- | --- | --- | --- | --- | ------- | -------------------- | ----------- | ----------- | --- | --- | ---- |
|     |     |     |     |    |         | i=                   |             |             |     |     |      |
|     |     |     |     |     | η =     | 1                    |             |             |     |     |      |
|     |     |     |     |     | ∑i      | t e r ∑ i t er       | c o v ( ∆w  | i,∆ wj )    |     |     | (15) |
|     |     |     |     |     | (cid:0) | i = 1 (cid:1) j = i+ | 1 (cid:0)   | (cid:1)     |     |     |      |
|     |     |     |     |    | Var w   | i t e r =            | V a r w     | 0 + η 2iter |     |     |      |
Equation(16)wasusedtoexpressthecycliclayerstructureoftheSimpleRNNmodel.
|     |     |     |     | nI   |       | nH  |              |     |                   |     |      |
| --- | --- | --- | --- | ---- | ----- | --- | ------------ | --- | ----------------- | --- | ---- |
|     |     |     |     | ∑    |       | ∑   |              |     | (cid:0) at(cid:1) |     |      |
|     |     |     |     | at = | w xt+ |     | w ht−1,∀t,ht | =   | θ                 |     | (16) |
|     |     |     |     |      | ih    |     | hh           |     |                   |     |      |
|     |     |     |     | i=1  |       | h   |              |     |                   |     |      |
whereat denotestheinputofaneuron,ht−1
denotestheoutputofthepreviousneuron,
andw andw aretheparameterweights. Solvingforthevarianceonbothsidesofthe
|     | ih  | hh  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Equation(16)yieldsEquation(17).
|     |     |     |     |                   |      | (cid:32) |     |        | (cid:33) |     |      |
| --- | --- | --- | --- | ----------------- | ---- | -------- | --- | ------ | -------- | --- | ---- |
|     |     |     |     |                   |      | nI       |     | nH     |          |     |      |
|     |     |     |     | (cid:0) at(cid:1) |      | ∑        | xt+ | ∑ ht−1 |          |     |      |
|     |     |     |     | Var               | =Var |          | w   | w      |          |     | (17) |
|     |     |     |     |                   |      |          | ih  | hh     |          |     |      |
|     |     |     |     |                   |      | i=1      |     | h      |          |     |      |
ExpandingonEquation(17)ismorecomplicated,andweexperimentallyverifiedthat
theneuronoutputsofthemodelunderourgradientnormalizationapproachshowamore
stableupwardtrendcomparedtotheunnormalizedapproach,afewcasesofwhichare
showninFigure4.
Duringthetheoreticalderivation,wecalculatethecovarianceofthemodelweights
and their weight gradients, which can be obtained with a small order of magnitude.
By comparing the normalized and unnormalized weight variance, it can be found that
theparametervarianceunderthenormalizedapproachchangessteadily,whichwillmake
theneuron’soutputalsochangesteadily,andthustheneuron’sactivationprobabilitywill
notchangedrastically. Inthiscase, themodelcanlearntherelevantinformationfaster
andmoresteadily. Sincetheneuronoutputcanstablydiscardsomeuselessinformation
whenpassingthroughtheactivationfunction,thisleadstoamodelthatislesspronetothe
gradientexplosionandgradientvanishingproblems.

Appl.Sci.2024,14,6578 9of18
Figure4. Comparisonofnormalizedandnon-normalizedweightvarianceandneuronaloutput
variance;fromlefttoright,thevariancechangesareplottedatlearningratesof0.005,0.001,and
0.0005,respectively. Observationofitschangesshowsthatitsweight(WihandWhh)andneuron
output(at)variancechangesshowasteadyupwardtrend, whiletheweightandneuronoutput
varianceunderunnormalizedconditionsarenon-smoothupwardcurves.WGNissensitivetothe
learningrate,anddifferentlearningrateshavedifferentimprovementeffects.
4. Dataset
Weutilizedfourdatasets,namelytheMINISTdataset[11],thePTBdataset[12],the
ETTm1dataset[13],andtheUCRdataset[14]. TheMINISTdatasetcomprises60,000sam-
ples,with50,000inthetrainingsetand10,000inthetestset. Itisaclassichandwritten
digitalimagedatasetcommonlyemployedinimageclassificationtasksinmachinelearning.
The PTB dataset, short for the Penn Treebank dataset, is a classic language model
datasetcollectedandcuratedbythelinguisticsdepartmentattheUniversityofPennsyl-
vaniaaspartofthePennTreebankproject. Widelyusedinlanguagemodeling,natural
language processing, and other related fields of research, the PTB dataset consists of
threetextfilesservingastraining,validation,andtestsets,containing929k,73k,and82k
words,respectively.
TheETT(ElectricityTransformerTemperature)datasetcollectstransformerdatafrom
two independent counties in China over two years. We selected the ETTm1 dataset at
a 15-min granularity, totaling 69,680 data points, each comprising the target variable
“oiltemperature”andsixpowerloadfeatures. Throughslidingwindows(whichtransform
timeseriesdataintosupervisedlearningdatasets),wepartitioneditinto48,627training,
10,303validation,and10,303testinstances,trainingforatotalof20epochs.
TheUCR(UnivariateTimeSeriesClassificationArchive)servesasanopenresource
forstoringandsharingtimeseriesclassificationdatasets. Encompassingvariousdomains
andapplicationssuchasmedicine,finance,andengineering,eachdatasetcontainsasetof
labeledunivariatetimeseriessamples,whicharecategorizedbasedontheirtimeseries
shapesandfeatures. WeselectedthreedatasetsfromtheUCRdataset,coffee,computer,
andECG500,fortrainingevaluation.

Appl.Sci.2024,14,6578 10of18
5. Experiment
Inthesubsequentexperiments,wecontrastedsingle-layerandtwo-layerRNNand
LSTMmodels,withandwithoutweightgradientnormalization(WGN),usingfourdifferent
datasets. To emphasize the contribution of WGN, and assuming the program operates
normally,weaimedtomaintaintheoriginalrecurrentnetworkmodelsintheirsimplest
configurationspossible. Throughcomparativeexperiments,specificallycontrastingwith
mini-batch stochastic gradient descent, our objective was to elucidate the performance
advantagesoftheWGNmethodovertraditionalapproaches. Thesedatasetsspanmultiple
domains,enablingacomprehensiveevaluationofmodelperformancevariationsacross
differentdatacontexts.
5.1. AblationExperiment
AblationexperimentswereconductedusingtheWGNmethodontheMINISTdataset,
with the parameters η set to 0.001 and δ set to 1 × 10−5. As illustrated in Table 1, the
RNNmodelisoptimallyimplementedbyemployingtheWGNmethodonboththeW
ih
and W . Conversely, the LSTM model is most effectively normalized by applying the
hh
WGN method to all weights. Experiments have shown that in some cases, combining
gradientnormalizationforspecificweightsismoreeffectivethanusingtheWGNmethod
foraparticularweightalone. ThecombinationofWGN(W )andWGN(W ),aswellas
hh fc
thecombinationofWGN(W )andWGN(W ),hasbeenobservedtoresultinanotable
ih hh
enhancementinmodelperformancewhencomparedtotheirindividualnormalizations.
However,thecombinationofWGN(W )andWGN(W ),whencomparedtotheirindi-
ih fc
vidualnormalizations,hasbeenobservedtoresultinadeclineinmodelperformance. It
can thus be proposed that a single WGN strategy may not be applicable to all weighty
optimizationrequirementsandshouldbeadaptedtothespecificmodelstructureandtask
requirements.
Table1.ComparisonofaccuracyinWGNablationexperiments.
Method RNN(1Layer) LSTM(1Layers)
WGN(W ) 98.05 98.44
ih
WGN(W ) 97.66 98.59
hh
WGN(W ) 97.01 98.16
fc
WGN(W )+WGN(W ) 98.07 98.56
ih hh
WGN(W )+WGN(W ) 97.84 98.60
hh fc
WGN(W )+WGN(W ) 98.01 98.12
ih fc
WGN(W )+WGN(W )+WGN(W ) 98.04 98.80
ih hh fc
5.2. HyperparametricSensitivityAnalysis
Tooptimizethemodelanddeterminetheeffectivehyperparametersettingsforthe
WGNmethodinneuralnetworks,asensitivityanalysisofWGNforsingle-layerneural
networks on the MINIST dataset was performed. As illustrated in Table 2, the WGN
methodyieldsnotableoutcomesforRNNneuralnetworkswhenthevalueoftheparameter
ηiswithintherangeof0.0001to0.001. InthecaseofLSTMneuralnetworks,theeffective
rangeisobservedtoextendfrom0.0001to0.005. Furthermore,withintheaforementioned
effectiveranges,anincreaseintheparameterηtypicallyresultsinenhancedaccuracy. In
particular,theRNNmodelattainsthehighestlevelofaccuracywhenthevalueofηis0.001
andδis1×10−5,whereastheLSTMmodeldemonstratesoptimalperformancewhenηis
0.005andδis1×10−4.
Theresultsofourexperimentsdemonstratethattheparameterηexertsamorepro-
nouncedinfluenceontheWGNmethodthantheparameterδ. Consequently,theselection
ofsuitablehyperparametervaluescanmarkedlyenhancetheoptimizationoftheWGN
method,whereastheinappropriatechoiceofhyperparametersmayresultinadeclinein
performance.

Appl.Sci.2024,14,6578
11of18
Table2.ComparisonoftheaccuracyofWGNwithdifferentcombinationsofhyperparameters.
| δ   | 1×10−7 |      | 1×10−6 |      | 1×10−5 |      | 1×10−4 |      |
| --- | ------ | ---- | ------ | ---- | ------ | ---- | ------ | ---- |
|     | RNN    | LSTM | RNN    | LSTM | RNN    | LSTM | RNN    | LSTM |
η
| 0.0001 | 95.09 | 96.75 | 95.35 | 97.29 | 94.81 | 97.18 | 95.45 | 96.86 |
| ------ | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0.0005 | 97.83 | 98.28 | 97.8  | 98.36 | 97.74 | 98.48 | 97.93 | 97.98 |
| 0.001  | 97.96 | 98.60 | 98.02 | 98.60 | 98.04 | 98.64 | 97.94 | 98.63 |
| 0.005  | 58.44 | 98.88 | 66.85 | 98.76 | 64.75 | 98.81 | 48.38 | 98.91 |
| 0.01   | 11.35 | 78.29 | 28.91 | 97.03 | 31.06 | 97.64 | 10.28 | 98.90 |
| 0.05   | 9.74  | 31.95 | 10.32 | 28.87 | 9.82  | 49.42 | 10.1  | 51.06 |
5.3. MINISTClassification
Inthispaper,weevaluatedourmodelsusingtheMINISTimageclassificationtask.
FortheRNNmodel,weemployedoneormorerecurrentunitswiththehyperbolictangent
(tanh) function as the activation function. In the output layer, we extracted the hidden
stateofthelasttimestepinthesequenceandmappedittotheoutputcategorydimension
throughalineartransformation. TheLSTMmodelwassimilartotheRNNmodel,andwe
usedthecross-entropylossfunctiontocomputethelossbetweenthemodeloutputandthe
originallabels.
Duringtraining,wecomparedstochasticgradientdescentwithourownWGNgradi-
entupdatemethod,asshowninFigure5,andthefinalaccuracycomparisonisshownin
Table3. Ourmodelfeaturedarecurrentnetworkwith28timesteps,capableofhandling
informationwithlong-termtemporaldependencies. Thedimensionoftheinputfeature
Every28×28picturewasviewedasasequenceinwhichtheorder
wassimilarlysetto28.
ofscanlineswasfollowedtoprocesseachrow,whichrepresentedarowofpixelvaluesin
theimage. Usingabatchsizeof1000,alearningrateof0.05intheclassicgradientdescent
approach,and200trainingepochs,weselected128recurrenthiddenunits. IntheWGN
algorithm,weusedascalingfactorof0.001,abiascorrectionfactorof1×10−5,andthe
otherparametersremainedconsistent.
Figure5. ThetrainingeffectplotoftheMINISTdatasetwithandwithoutnormalizationunder
different models. As observed in the figure, under identical parameter conditions, the gradient
descentmethodemployingWGNeffectivelyreducesthefrequencyofexplosionsandaccelerates
convergencetime,resultinginasmootherlearningcurve.ItisevidentthatourWGNapproachbetter
mitigatestheissueoflong-termdependencies.

Appl.Sci.2024,14,6578 12of18
5.4. LanguageModel
WeassessedthemodelsusingthePTBdatasetatthewordlevel. Ourbaselinemodels
areLSTMorRNNmodelswith200hiddenunitsineachlayer.Tanhservedastheactivation
function,andallweightmatriceswereinitializedusingauniformdistribution. Weuseda
variablelearningratetechniquefortheunnormalizedmethod: thelearningrate(lr)was
dividedby4.0,startingat20ifthecurrentvalidationlossdidnotexceedthebestvalidation
loss. There are 55 epochs of training in total. The large vocabulary of the PTB dataset
maycauseseriousgradientproblemsintheRNNnetwork,whichcouldresultinprogram
failure. Asaresult,gradientclippingwitha0.25clippingcoefficientwasappliedpriorto
gradientupdates. Thenormalizationapproachemployedafixedlearningrateof0.0001,
whileallotherparametersstayedthesame. AsseeninFigure6,wefoundthatutilizing
WGNimprovedthemodel’sconvergencetimeevenifgradientexplosionhappenedless
frequentlyinLSTM.ThefinalaccuracycomparisonisshowninTable4.
Figure6.ThePTBdatasettrainingeffectsundervariousmodels,withandwithoutnormalization.
When normalization techniques are used in the RNN model, confusion is significantly reduced;
infact, itisreducedbyseveralordersofmagnitudewhencomparedtothenon-normalizedsce-
nario.Furthermore,thenormalizationoftheperplexitycurveresultsinasmoothercurvedevoidof
noticeablespikes.
5.5. TimeSeriesPredictionTask
Inthetimeseriesforecastingtask,weusetheslidingwindowtechniquetodividethe
ETTm1datasetwithanobservationwindowwithalengthof126toobtainadatasetof
thenewsize. Weusethemeansquarederrorasalossfunctiontomeasurethedifference
between the predictions and the true values. The task is the multivariate prediction of
multivariate,andthemodeloutputssevendimensionsafterinputtingsevendimensions.
Intherecurrentneuralnetworkmodelwith128hiddenunitsperlayer, ReLUwas
usedastheactivationfunctiontointroducenon-linearrelationships. Twopredictionswere
made,onetopredictthedataforthenext24timestepsandtheothertopredictthedatafor
thenext96timesteps.
Duringthetrainingprocess,thesamerandomseedof1029wasset,andwedivided
the data into batches, each of which had a size of 64. We chose the stochastic gradient
descentmethodfortheoriginalmodelwithoutWGN,withthelearningratesetto0.05to
controlthemagnitudeofthemodel’supdateoftheweightsineachtrainingstep,whilethe
learningrateofthenormalizationmethodwas0.0001. Whenwecomparethelossvariation
inFigure7totheoriginalbaseline,wecanseethattheWGNsignificantlyimprovesthe
RNNmodelandprovidesadecenttrainingcurvefortheLSTMmodel. Thefinalaccuracy
comparisonisshowninTable5suggeststhatWGNhasagoodpotentialtoimprovethe
performanceandefficiencyofmodelsintimeseriespredictiontasks.

Appl.Sci.2024,14,6578 13of18
Figure7.TrainingeffectplotoftheETTm1datasetwithandwithoutnormalizationunderdifferent
models;themodeltrainingprocessismorerobustundertheRNNmodelwiththeWGNmethod,
whiletheLSTMmodelwiththeWGNmethodreachesconvergencefaster.
5.6. TimeSeriesClassificationTask
Inourtimeseriesclassificationtask,weselectedthreedatasetsfromtheUCRdataset.
Withthesamestochasticseed,thesethreedatasetshaveasmallersamplesize,alearning
rate of 0.05 for stochastic gradient descent, and a learning rate of 0.0001 for the WGN
method. For the Coffee and ECG5000 datasets, we trained a total of 500 epochs, while
fortheComputersdataset,wetrainedonly20epochs. WefoundthatontheComputers
dataset,themodelachievedbetterperformancewithfewertrainingrounds.
Notably, ontheCoffeedataset, theRNNmodelusingtheWGNmethodexhibited
a smoother learning process, while the LSTM model demonstrated faster convergence.
AlthoughtheWGNmethoddidnoteffectivelysolvethegradientproblemintheComputers
dataset, it still accelerated the convergence of the models. In the ECG5000 dataset, the
WGNmethodwasnotaseffectivebutstillimprovedthebestaccuracybyabout0.4percent.
As shown in Figures 8–10 and Table 6, our experimental results indicate that different
datasetsmayrequiredifferentoptimaltrainingstrategies.TheWGNmethodexhibitsa
smoothlearningprocessandfasterconvergenceinmostcases,showingthepotentialto
improvetheperformanceoftimeseriesclassification.
Figure8. PlotsoftheCoffeedatasetinUCRwithandwithoutnormalizedtrainingeffectsunder
differentmodels.

Appl.Sci.2024,14,6578 14of18
Figure9.PlotsoftheComputersdatasetinUCRwithandwithoutnormalizedtrainingeffectsunder
differentmodels.
Figure10.PlotsoftheECG5000datasetinUCRwithandwithoutnormalizedtrainingeffectsunder
differentmodels.
6. Metric
WedesignedametricLOEtomeasurethegradientproblem,whereloss denotesthe
t
lossvalueatmomentt,epochdenotesthecurrenttraininground,andtotal_epochdenotes
thetotalnumberoftrainingrounds.
(cid:12) (cid:12)
LOE= (cid:12) (cid:12) loss t −loss t−1(cid:12) (cid:12)·eto ρ ta ·e l_ p e o p c o h ch (18)
(cid:12) loss t−1 +α (cid:12)
Astrainingproceeded,wenoticedthatthenegativeimpactofthegradientproblem
onmodeltraininggraduallyincreasedinthelaterstagesoftraining. Inordertoquantify
this,wedesignedacorrectionmechanismcontaininganexponentialtermforcorrectingthe
severityofthegradientproblem.Intheindexwedesigned,theparameterLOErepresents
thedegreeofimpactofthegradientproblemontraining, withlargervaluesindicating
amoresignificantimpactofgradientexplosion. Specifically,wefirstcalculatedthepro-
portionoftheincreaseinlossateachtimenoderelativetotheprevioustimenode;this
proportion requires an absolute value operation because both gradient vanishing and
gradient explosion can occur. We then multiplied this proportion by an e-exponential
correction term, where the value of the exponent is related to the number of training
roundsandmodelparameters. Byintroducingsuchacorrectionmechanism,wecanmore
accuratelyvisualizetheextenttowhichthemodelisexperiencinggradientproblemsand
caneffectivelyimprovethemodelbasedontheseindicators. Theperformancecomparison
of the models using WGN and without WGN method is shown in Tables 3–6 and the
performancecomparisonofusingtheWGNmethodwithgradientclippingandtheGRU
modelisshowninTablesA1andA2. Theirexperimentalconfigurationsareallthesameas
thosedescribedinthepreviousexperimentalsection.

Appl.Sci.2024,14,6578
15of18
Table 3. Best metric on the training and development sets on MINIST. Bolded values are for
bestperformance.
|     |     | RNN |     | RNN-WGN |     |     | LSTM |     | LSTM-WGN |     |
| --- | --- | --- | --- | ------- | --- | --- | ---- | --- | -------- | --- |
Metric
|          | 1Layer    | 2Layers |     | 1Layer | 2Layers | 1Layer |     | 2Layers | 1Layer | 2Layers |
| -------- | --------- | ------- | --- | ------ | ------- | ------ | --- | ------- | ------ | ------- |
| Accuracy | 98.07     | 98.21   |     | 97.91  | 98.04   | 97.94  |     | 98.42   | 98.80  | 99.11   |
|          | LOE 57.63 | 132.49  |     | 9.39   | 16.42   | 27.62  |     | 17.22   | 55.15  | 25.90   |
Table4. BestmetricontraininganddevelopmentsetsonPeenTreebank. Boldedvaluesarefor
bestperformance.
|     |     | RNN |     | RNN-WGN |     |     | LSTM |     | LSTM-WGN |     |
| --- | --- | --- | --- | ------- | --- | --- | ---- | --- | -------- | --- |
Metric
|     | 1Layer     | 2Layers |     | 1Layer | 2Layers | 1Layer |     | 2Layers | 1Layer | 2Layers |
| --- | ---------- | ------- | --- | ------ | ------- | ------ | --- | ------- | ------ | ------- |
|     | PPL 383.20 | 972.38  |     | 144.97 | 141.02  | 125.27 |     | 293.15  | 118.58 | 110.89  |
|     | LOE 37.77  | 104.59  |     | 58.05  | 54.52   | 53.14  |     | 55.62   | 55.15  | 54.78   |
Table 5. Best metric on training and development sets on ETTm1. Bolded values are for
bestperformance.
|     |     | RNN |     |     | RNN-WGN |     | LSTM |     | LSTM-WGN |     |
| --- | --- | --- | --- | --- | ------- | --- | ---- | --- | -------- | --- |
Metric
|     |     | 1Layer | 2Layers | 1Layer | 2Layers | 1Layer |       | 2Layers | 1Layer | 2Layers |
| --- | --- | ------ | ------- | ------ | ------- | ------ | ----- | ------- | ------ | ------- |
|     | MAE | 0.806  | 0.943   |        | 0.978   | 0.886  | 0.802 | 0.866   | 0.778  | 0.902   |
len=24
|     | LOE | 34.62 | 81.15 |     | 8.28  | 13.85 | 23.78 | 32.58 | 15.29 | 24.00 |
| --- | --- | ----- | ----- | --- | ----- | ----- | ----- | ----- | ----- | ----- |
|     | MAE | 0.635 | 0.733 |     | 0.592 | 0.678 | 0.681 | 0.685 | 0.704 | 0.790 |
len=96
|     | LOE | 9.94 | 17.58 |     | 6.38 | 11.83 | 20.03 | 27.33 | 14.63 | 21.95 |
| --- | --- | ---- | ----- | --- | ---- | ----- | ----- | ----- | ----- | ----- |
Table 6. Best metric on training and development sets on UCR. Bolded values are for
bestperformance.
|     |     | RNN |     |     | RNN-WGN |     | LSTM |     | LSTM-WGN |     |
| --- | --- | --- | --- | --- | ------- | --- | ---- | --- | -------- | --- |
Metric
|     |          | 1Layer | 2Layers | 1Layer | 2Layers | 1Layer |       | 2Layers | 1Layer | 2Layers |
| --- | -------- | ------ | ------- | ------ | ------- | ------ | ----- | ------- | ------ | ------- |
|     | Accuracy | 0.935  | 0.932   |        | 0.939   | 0.939  | 0.935 | 0.933   | 0.930  | 0.925   |
ECG5000 LOE 192.791 2446.467 29.486 52.538 56.822 86.378 25.096 63.990
|     | Accuracy | 0.964 | 0.964 |     | 0.964 | 0.964 | 1.000 | 1.000 | 1.000 | 1.000 |
| --- | -------- | ----- | ----- | --- | ----- | ----- | ----- | ----- | ----- | ----- |
Coffee LOE 35.237 68.573 67.513 27.677 35.013 64.383 86.321 25.374
|     | Accuracy | 0.600 | 0.524 |     | 0.556 | 0.572 | 0.652 | 0.600 | 0.624 | 0.660 |
| --- | -------- | ----- | ----- | --- | ----- | ----- | ----- | ----- | ----- | ----- |
Computers
|     | LOE | 18.627 | 27.378 | 27.817 | 23.865 |     | 3.876 | 0.543 | 20.221 | 26.314 |
| --- | --- | ------ | ------ | ------ | ------ | --- | ----- | ----- | ------ | ------ |
Inthelanguagemodels,theperplexityofthemodelsutilizingWGNistypicallylower
thanthatofthemodelsnotemployingWGN.Moreover,boththeperplexityandtheLOE
ofthemodelsutilizingWGNdemonstratedadeclineasthenumberoflayersincreased.
Theperplexityreachedaminimuminthetwo-layerLSTMmodelwithWGN,andtheLOE
was found to be average. In the context of the image dataset classification, the highest
accuracywasobservedwhentheWGNmethodwasemployedwithanetworkcomprising
twolayers,utilizingeithertheRNNortheLSTMmodel. Furthermore,theincorporation
oftheWGNmethodintotheRNNmodelresultedinasignificantreductionintheLOE.
Incontrast,theintroductionofWGNintotheLSTMmodelledtoanotableenhancementin
accuracy,althoughthiswasaccompaniedbyanincreaseinLOE.Forthepredictiontask
oftheETTm1dataset,weobservedthattheperformanceofrecurrentneuralnetworksor
LSTMmodelswithdifferentnumbersoflayerscombinedwiththeWGNmethodvaried
underdifferentpredictionlengthconditions. Firstly,atapredictionlengthof96,thetwo-
layerRNN-WGNmodelexhibitedthelowestmeanabsoluteerror,whilethesingle-layer
RNN-WGNmodeldemonstratedthelowestLOE.Conversely, atapredictionlengthof
24,theone-layerLSTM-WGNmodelexhibitsthemostfavorableoutcomes,whiletheone-
layerRNN-WGNmodeldemonstratesthelowestLOE.Thisindicatesthattheutilization

Appl.Sci.2024,14,6578 16of18
of the WGN approach is an effective method for optimizing model performance and
achievingoptimalvaluesindifferentsettings. ItcanbeobservedthatthemodelwithWGN
exhibitsmarkedlyelevatedaccuracyandmarkedlyreducedLOEintheECG5000dataset.
IntheCoffeedataset,thetwo-layerLSTM-WGNmodeldemonstratestheoptimalLOE,
althoughtheaccuracyisnotsignificantlyenhanced. IntheComputerdataset,thetwo-layer
LSTM-WGNmodelattainsthehighestaccuracy.
7. Conclusions
Thispaperpresentsananalysisofthecausesofthegradientproblemfromtheperspec-
tivesofgradientvarianceandcovariance.Italsoproposesanewgradientupdatingmethod
andanevaluationmetrictoquantifythegradientproblembasedonstatisticaltheory.Theef-
ficacyoftheWGNmethodinalleviatingthegradientproblemindeepneuralnetworks,
particularlyrecurrentneuralnetworksandnetworkswithlongtime-dependentcharac-
teristics, has been demonstrated through experimentation on multiple public datasets.
Inadditiontosuppressingthegradientproblem, theWGNmethodhasbeenshownto
acceleratemodelconvergenceandimproveaccuracy. Furthermore,itisourcontentionthat
theWGNalgorithmrequiresfurtherexaminationinthefollowinginstances:
(1)OurfindingsindicatethattheimplementationoftheWGNmethodinasingle-
layerRNNneuralnetworkdoesnotresultinanotableenhancementintheaccuracyrate.
However,theLOEindexofthemodelexhibitsaconsiderableimprovement. Thisisdueto
themonotonousstructureofthesingle-layerSimple-RNN,whichproducesapermutation
effectontheLOEmetricsandaccuracy.
(2)Insomecases,theuseofthegradientnormalizationmethodhasbeenobservedto
occasionallyresultinadecreaseinaccuracyoranincreaseinLOEmetricswhenappliedto
smallerdatasets. Thisisprimarilyattributabletothefactthatthebatchsizeisconstrained
whenthedatasetislimitedinsize.Thisresultsinanincompleterepresentationoftheoverall
sampleprobabilitywithinthesamplespacecorrespondingtoeachbatch,whichinturn
givesrisetoanincreaseinthediscrepancybetweenthebatchesandaffectstherobustnessof
thetrainingprocess. Insmall-scaledatasetswherethevariabilityofsamplesisstronger,the
useofgradientnormalizationmayresultinanover-adjustmentofthegradient,whichin
turnaffectstheoverallperformanceofthemodel. Incontrast,inlarge-scalecorpusdatasets,
theWGNmethodismorelikelytocapturetheoverallcharacteristicsofthegradientsand
effectivelybalancethegradientdifferencesbetweendifferentsamples.
(3) The necessity for the additional computation of the mean and variance of the
gradientforeachbatchinherenttothegradientnormalizationmethodalsoresultsinan
increaseintimecomplexity.Itisthereforenotrecommendedthatthegradientnormalization
methodbeemployedinscenarioswherethereisahighrequirementforreal-timeprocessing
andalowrequirementforaccuracy.
Ingeneral,themodelsincorporatingWGNappeartoyieldthemostfavorableout-
comesacrossarangeoftasks.ThissuggeststhattheWGNapproachhasbroadapplicability
andcanprovideeffectivesupportforthetrainingofdiversetypesofmodels. Infuture
research, wewillcontinuetoinvestigatetheefficacyofWGNandapplyittoabroader
rangeofmodels,includingGRUandTransformer.
AuthorContributions:Conceptualisation,X.W.;methodology,B.X.andC.L.;software,W.H.;valida-
tion,H.L.andX.H.;formalanalysis,X.W.;investigation,H.L.;resources,B.X.;datacuration,W.H.;
writing—originaldraftpreparation,X.H.;writing—reviewandediting,X.W.;visualization,X.H.;
supervision,C.L.;projectadministration,B.X.;fundingacquisition,C.L.Allauthorshavereadand
agreedtothepublishedversionofthemanuscript.
Funding: This work was supported by National Natural Science Foundation of China (Grant
No.62106083),theNaturalScienceFoundationofXiamenMunicipality(GrantNo.3502Z202373035),
and the Youth Program of the Natural Science Foundation of Fujian Province of China (Grant
No.2022J05162).
InstitutionalReviewBoardStatement:Notapplicable.

Appl.Sci.2024,14,6578 17of18
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement:Therawdatasupportingtheconclusionsofthisarticlewillbemade
availablebytheauthorsonrequest.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.
AppendixA
TableA1. ComparisonoftheWGNmethodwithgradientclippingandtheGRUmethodonthe
MINISTdataset.Boldedvaluesareforbestperformance.
RNN-CLIP LSTM-CLIP GRU LSTM-WGN
Metric
1Layer 2Layers 1Layer 2Layers 1Layer 2Layers 1Layer 2Layers
Accuracy 98.09 98.30 98.07 98.42 98.35 98.71 98.80 99.11
LOE 68.05 97.27 46.44 40.50 66.36 49.62 55.15 25.90
TableA2.ComparisonoftheWGNmethodwithgradientclippingandtheGRUmethodonthePTB
dataset.Boldedvaluesareforbestperformance.
LSTM-CLIP GRU-CLIP LSTM-WGN
Metric
1Layer 2Layers 1Layer 2Layers 1Layer 2Layers
PPL 110.76 109.49 119.30 127.72 118.58 110.89
LOE 55.12 55.59 54.88 56.05 55.15 54.78
References
1. Tarwani,K.M.;Edem,S.Surveyonrecurrentneuralnetworkinnaturallanguageprocessing.Int.J.Eng.TrendsTechnol.2017,48,
301–304.[CrossRef]
2. Miao,Y.;Gowayyed,M.;Metze,F.EESEN:End-to-endspeechrecognitionusingdeepRNNmodelsandWFST-baseddecoding.
InProceedingsofthe2015IEEEWorkshoponAutomaticSpeechRecognitionandUnderstanding(ASRU),Scottsdale,AZ,USA,
13–17December2015;IEEE: Piscataway,NJ,USA,2015;pp.167–174.
3. Khamparia,A.;Pandey,B.;Tiwari,S.;Gupta,D.;Khanna,A.;Rodrigues,J.J.P.C.AnintegratedhybridCNN–RNNmodelfor
visualdescriptionandgenerationofcaptions.CircuitsSyst.SignalProcess.2020,39,776–788.[CrossRef]
4. Olatunji,I.E.;Cheng,C.H.Videoanalyticsforvisualsurveillanceandapplications:Anoverviewandsurvey.InMachineLearning
ParadigmsApplicationsofLearningandAnalyticsinIntelligentSystems;Springer:Berlin/Heidelberg,Germany,2019;pp.475–515.
5. Schaefer,A.M.;Udluft,S.;Zimmermann,H.G.Learninglong-termdependencieswithrecurrentneuralnetworks.Neurocomputing
2008,71,2481–2488.[CrossRef]
6. Kolbusz,J.;Rozycki,P.;Wilamowski,B.M.ThestudyofarchitectureMLPwithlinearneuronsinordertoeliminatethe“vanishing
gradient”problem. InProceedingsoftheInternationalConferenceonArtificialIntelligenceandSoftComputing,Zakopane,
Poland,11–15June2017;Springer:Cham,Switzerland,2017;pp.97–106.
7. Wanto,A.;Windarto,A.P.;Hartama,D.;Parlina,I.Useofbinarysigmoidfunctionandlinearidentityinartificialneuralnetworks
forforecastingpopulationdensity.IJISTECHInt.J.Inf.Syst.Technol.2017,1,43–54.[CrossRef]
8. Chung,H.;Lee,S.J.;Park,J.G.Deepneuralnetworkusingtrainableactivationfunctions.InProceedingsofthe2016International
JointConferenceonNeuralNetworks(IJCNN),Vancouver, BC,Canada, 24–29July2016; IEEE:Piscataway, NJ,USA,2016;
pp.348–352.
9. Hara,K.;Saito,D.;Shouno,H.Analysisoffunctionofrectifiedlinearunitusedindeeplearning. InProceedingsofthe2015
InternationalJointConferenceonNeuralNetworks(IJCNN),Killarney,Ireland,12–17July2015;IEEE: Piscataway,NJ,USA,
2015;pp.1–8.
10. Yu,Y.;Si,X.;Hu,C.;Zhang,J.Areviewofrecurrentneuralnetworks: LSTMcellsandnetworkarchitectures. NeuralComput.
2019,31,1235–1270.[CrossRef]
11. LeCun,Y.;Bottou,L.;Bengio,Y.;Haffner,H.Gradient-basedlearningappliedtodocumentrecognition. Proc. IEEE1998,86,
2278–2324.[CrossRef]
12. Marcus, M.; Santorini, B.; Marcinkiewicz, M.A. Building a Large Annotated Corpus of English: The Penn Treebank; MIT Press:
Cambridge,MA,USA,1993.
13. Zhou,H.;Zhang,S.;Peng,J.;Zhang,S.;Li,J.;Xiong,H.;Zhang,W.Informer:Beyondefficienttransformerforlongsequence
time-seriesforecasting.InProceedingsoftheAAAIConferenceonArtificialIntelligence,virtually,2–9February2021;Volume35,
pp.11106–11115.

Appl.Sci.2024,14,6578 18of18
14. Dau,H.A.;Keogh,E.;Kamgar,K.;Yeh,C.M.;Zhu,Y.;Gharghabi,S.;Ratanamahatana,C.A.;Chen,Y.;Hu,B.;Begum,N.;etal.
TheUCRTimeSeriesClassificationArchive.2019.Availableonline:https://www.cs.ucr.edu/~eamonn/time_series_data_2018/
(accessedon8February2024).
15. Bengio,Y.;Simard,P.;Frasconi,P.Learninglong-termdependencieswithgradientdescentisdifficult.IEEETrans.NeuralNetw.
1994,5,157–166.[CrossRef][PubMed]
16. Pascanu,R.;Mikolov,T.;Bengio,Y.Understandingtheexplodinggradientproblem.Comput.Sci.Math.2012,2,1.
17. Glorot,X.;Bengio,Y.Understandingthedifficultyoftrainingdeepfeedforwardneuralnetworks.InProceedingsoftheThirteenth
InternationalConferenceonArtificialIntelligenceandStatistics,Sardinia,Italy,13–15May2010;pp.249–256.
18. Klambauer,G.;Unterthiner,T.;Mayr,A.;Hochreiter,S.Self-normalizingneuralnetworks.Adv.NeuralInf.Process.Syst.2017,30,
972–981.
19. Clevert,D.A.;Unterthiner,T.;Hochreiter,S.Fastandaccuratedeepnetworklearningbyexponentiallinearunits(elus).arXiv
2015,arXiv:1511.07289.
20. Gers,F.A.;Schmidhuber,J.;Cummins,F.Learningtoforget:ContinualpredictionwithLSTM.NeuralComput.2000,1,2451–2471.
[CrossRef][PubMed]
21. Cho,K.;VanMerriënboer,B.;Gulcehre,C.;Bahdanau,D.;Bougares,F.;Schwenk,H.;Bengio,Y.Learningphraserepresentations
usingRNNencoder-decoderforstatisticalmachinetranslation.arXiv2014,arXiv:1406.1078..
22. Greff,K.;Srivastava,R.K.;Koutník,J.;Steunebrink,B.R.;Schmidhuber,J.LSTM:Asearchspaceodyssey.IEEETrans.NeuralNetw.
Learn.Syst.2016,28,2222–2232.[CrossRef][PubMed]
23. Pascanu,R.;Mikolov,T.;Bengio,Y.Onthedifficultyoftrainingrecurrentneuralnetworks.InProceedingsofthe30thInternational
ConferenceonInternationalConferenceonMachineLearning,Atlanta,GA,USA,16–21June2013;pp.1310–1318.
24. Laurent,C.;Pereyra,G.;Brakel,P.;Zhang,Y.;Bengio,Y.Batchnormalizedrecurrentneuralnetworks. InProceedingsofthe
2016IEEEInternationalConferenceonAcoustics,SpeechandSignalProcessing(ICASSP),Shanghai,China,20–25March2016;
IEEE:Piscataway,NJ,USA,2016;pp.2657–2661.
25. Amodei,D.;Ananthanarayanan,S.;Anubhai,R.;Bai,J.;Battenberg,E.;Case,C.;Casper,J.;Catanzaro,B.;Cheng,Q.;Chen,G.;
etal.Deepspeech2:End-to-endspeechrecognitioninenglishandmandarin.InProceedingsoftheInternationalConferenceon
MachineLearning,NewYork,NY,USA,20–22June2016;PMLR;pp.173–182.
26. Cooijmans,T.;Ballas,N.;Laurent,C.;Gülçehre,Ç.;Courville,A.Recurrentbatchnormalization.arXiv2016,arXiv:1603.09025.
27. Zebin,T.;Balaban,E.;Ozanyan,K.B.;Casson,A.J.;Peek,N.ImplementationofabatchnormalizeddeepLSTMrecurrentnetwork
onasmartphoneforhumanactivityrecognition.InProceedingsofthe2019IEEEEMBSInternationalConferenceonBiomedical
&HealthInformatics(BHI),Chicago,IL,USA,19–22May2019;IEEE: Piscataway,NJ,USA,2019;pp.1–4.
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.