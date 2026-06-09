informatio n
Review
Recurrent Neural Networks: A Comprehensive Review of
Architectures, Variants, and Applications
IbomoiyeDomorMienye1,∗,† ,TheoG.Swart1,† andGeorgeObaido2,†
1 InstituteforIntelligentSystems,UniversityofJohannesburg,Johannesburg2006,SouthAfrica;
tgswart@uj.ac.za
2 CenterforHuman-CompatibleArtificialIntelligence(CHAI),BerkeleyInstituteforDataScience(BIDS),
UniversityofCalifornia,Berkeley,CA94720,USA;gobaido@berkeley.edu
* Correspondence:ibomoiyem@uj.ac.za
† Theseauthorscontributedequallytothiswork.
Abstract:Recurrentneuralnetworks(RNNs)havesignificantlyadvancedthefieldofmachinelearn-
ing(ML)byenablingtheeffectiveprocessingofsequentialdata.Thispaperprovidesacomprehensive
reviewofRNNsandtheirapplications,highlightingadvancementsinarchitectures,suchaslong
short-termmemory(LSTM)networks,gatedrecurrentunits(GRUs),bidirectionalLSTM(BiLSTM),
echostatenetworks(ESNs),peepholeLSTM,andstackedLSTM.Thestudyexaminestheapplication
ofRNNstodifferentdomains,includingnaturallanguageprocessing(NLP),speechrecognition,time
seriesforecasting,autonomousvehicles,andanomalydetection.Additionally,thestudydiscusses
recentinnovations,suchastheintegrationofattentionmechanismsandthedevelopmentofhybrid
modelsthatcombineRNNswithconvolutionalneuralnetworks(CNNs)andtransformerarchitec-
tures.ThisreviewaimstoprovideMLresearchersandpractitionerswithacomprehensiveoverview
ofthecurrentstateandfuturedirectionsofRNNresearch.
Keywords:deeplearning;GRU;LSTM;machinelearning;NLP;RNN
1. Introduction
Citation:Mienye,I.D.;Swart,T.G.;
Obaido,G.RecurrentNeural Deeplearning(DL)hasreshapedthefieldofartificialintelligence(AI),drivingad-
Networks:AComprehensiveReview vancementsinawidearrayofapplications,fromimagerecognitionandnaturallanguage
ofArchitectures,Variants,and processing(NLP)toautonomousdrivingandmedicaldiagnostics[1–5]. Thisrapidgrowth
Applications.Information2024,15,517. isfueledbytheincreasingavailabilityofbigdata,advancementsincomputingpower,and
https://doi.org/10.3390/info15090517 thedevelopmentofsophisticatedalgorithms[6–9]. AsDLmodelscontinuetoevolve,they
areincreasinglybeingdeployedincriticalsectors,demonstratingtheirabilitytooutperform
AcademicEditor:MaríaN.Moreno
traditionalmachinelearning(ML)techniquesinhandlingcomplextasks.
García
Recurrentneuralnetworks(RNNs)areaclassofdeeplearningmodelsthatarefunda-
Received:21July2024 mentallydesignedtohandlesequentialdata[10,11]. Unlikefeedforwardneuralnetworks,
Revised:22August2024 RNNspossesstheuniquefeatureofmaintainingamemoryofpreviousinputsbyusing
Accepted:23August2024 theirinternalstate(memory)toprocesssequencesofinputs[12]. Thismakesthemideally
Published:25August2024
suitedforapplicationssuchasnaturallanguageprocessing,speechrecognition,andtime
seriesforecasting,wherecontextandtheorderofdatapointsarecrucial.
TheinceptionofRNNsdatesbacktothe1970s,withfoundationalworkbyWerbos[13],
whichintroducedtheconceptofbackpropagationthroughtime(BPTT)thatlaidthefoun-
Copyright: © 2024 by the authors.
dationfortrainingrecurrentneuralnetworks. However,RNNsstruggledwithpractical
Licensee MDPI, Basel, Switzerland.
applicationsduetothevanishinggradientproblem,wheregradientseithergroworshrink
Thisarticleisanopenaccessarticle
exponentiallyduringbackpropagation[14]. Meanwhile,theintroductionofLongShort-
distributed under the terms and
TermMemory(LSTM)networksbyHochreiterandSchmidhuber[15]wasaturningpoint
conditionsoftheCreativeCommons
Attribution(CCBY)license(https:// for RNNs, allowing for the learning of dependencies over much longer periods. Addi-
creativecommons.org/licenses/by/ tionally,gatedrecurrentunits(GRUs),proposedbyChoetal. [16],offeredasimplified
4.0/). alternativetoLSTMwhilemaintainingcomparableperformance.
Information2024,15,517.https://doi.org/10.3390/info15090517 https://www.mdpi.com/journal/information

Information2024,15,517 2of34
Overtheyears,theseRNNarchitectureshavebeenappliedindifferentfields,achieving
excellentperformance[17–19]. Despitetheiradvancementsandadoptioninvariousfields,
RNNshavecontinuedtoevolve. Specifically,theincreasingcomplexityofdataandtasksin
recentyearshasdrivencontinuousinnovationsinRNNarchitecturesandvariants. These
developmentshaveexpandedtheapplicationofRNNsfromsimplesequencepredictionto
complextaskssuchasmultimodallearningandreal-timedecision-makingsystems.
Recent studies and reviews have highlighted the significant progress made in the
field of RNNs. For example, Lipton et al. [20] provided an overview of the theoretical
foundations and applications of RNNs, while Yu et al. [21] focused on the LSTM cell
anddifferentvariants. Additionally,Tarwanietal.[22]reviewedtheapplicationandrole
ofRNNsinnaturallanguageprocessing. However,manyofthesereviewsdonotfully
capturethelatestadvancementsandapplications,giventherapidpaceofinnovationin
thisfield. Additionally,thereremainsagapintheliteraturethatcomprehensivelycovers
thelatestadvancementsinRNNarchitecturesandtheirapplicationsacrossabroaderrange
offields. Therefore,thispaperaimstofillthatgapbyprovidingacomprehensivereviewof
RNNs,assessingtheirtheoreticaladvancementsandpracticalimplementations,aswellas
cutting-edgeapplications,thushelpingshapefutureresearchonneuralnetworks.
The rest of this paper is organized as follows: Section 2 reviews related works.
Section3coversthefundamentalsofRNNs,includingbasicarchitectureandcomponents.
Section4exploresadvancedRNNvariants,suchasLSTMandGRU.Section5highlights
innovationsinRNNarchitecturesandtrainingmethodologies. Section6presentssome
publiclyavailabledatasetsusedforRNNstudies. Section7discussesvariousapplications
ofRNNsintheliterature. Section8addresseschallengesandfutureresearchdirections.
Finally,Section9concludesthestudy.
2. RelatedWorks
RNNshavebeenappliedindifferentapplications,achievingstate-of-the-artperfor-
mance, especially in time-series applications. Early developments in RNNs, including
locallyrecurrent,globallyfeedforwardnetworks,asreviewedbyTsoiandBack[23],andthe
block-diagonalrecurrentneuralnetworksproposedbyMastorocostasandTheocharis[24],
laidimportantgroundworkforunderstandingcomplexsequencemodeling.
SeveralreviewshavebeenconductedonRNNsandtheirapplications,eachcontribut-
ing to the understanding and development of the field. For instance, Dutta et al. [25]
provided a comprehensive overview of the theoretical foundations of RNNs and their
applications in sequence learning. Their review highlighted the challenges associated
withtrainingRNNs,particularlythevanishinggradientproblem,anddiscussedthead-
vancements in LSTM and GRU architectures. However, the review primarily focused
on the theoretical aspects and applications of RNNs and did not extensively cover the
latestinnovationsandpracticalapplicationsinemergingfieldssuchasbioinformaticsand
autonomous systems. Quradaa et al. [26] presented a start-of-the-art review of RNNs,
coveringthecorearchitectureswithafocusonapplicationsincodeclones.
Similarly,thereviewbyTarwanietal.[22]providedanin-depthanalysisofRNNs
inthecontextofNLP.Whilethisreviewofferedvaluableinsightsintotheadvancements
inNLP,itlackedabroaderperspectiveonotherapplicationdomainsandrecentarchitec-
tural innovations. Another significant review by Goodfellow et al. [27] focused on the
fundamentalsofdeeplearning,includingRNNs,anddiscussedtheirapplicationsacross
variousdomains. Thisreviewprovidedasolidfoundationbutdidnotdelvedeeplyinto
thespecificadvancementsinRNNarchitecturesandtheirspecializedapplications.
Greff et al. [28] conducted an extensive study comparing various LSTM variants
todeterminetheireffectivenessindifferentapplications. Whilethisreviewprovideda
thorough comparison, it primarily focusedonLSTMarchitecturesand didnotaddress
otherRNNvariantsorthelatesthybridmodels. Insimilarresearch,Al-Selwietal.[29]
reviewedLSTMapplicationsintheliterature,coveringarticlesfromthe2018–2023time
period. Zarembaetal.[30]reviewedtheuseofRNNsinlanguagemodeling,highlighting

Information2024,15,517 3of34
significant achievements and the ongoing challenges in this field. Their work offered
valuableinsightsintotheapplicationofRNNsinNLPbutwaslimitedtolanguagemodeling
anddidnotexploreotherpotentialapplications. Baietal.[31]providedacriticalreviewof
RNNsandtheirvariants,comparingthemwithothersequencemodelingtechniqueslike
CNNsandattention-basedmodels. Cheetal.[32]focusedontheapplicationofRNNsin
healthcare,particularlyforelectronichealthrecords(EHRs)analysisanddiseaseprediction.
ThisreviewhighlightedthepotentialofRNNsinmedicalapplications.
Furthermore,morerecentstudieshaveexploredvariousnewaspectsandapplications
ofRNNs. Forexample,Chungetal.[33]exploredtheadvancementsinRNNarchitectures
over the past decade, focusing on improvements in training techniques, optimization
methods,andnewarchitecturalinnovations. Thisreviewprovidedanextensivesurveyof
recentdevelopmentsandtheirimplicationsforfutureresearch. Badawyetal.[34]provided
acomprehensiveoverviewoftheuseofRNNsinhealthcare,particularlyforpredictive
analyticsandpatientmonitoring. TheydiscussedtheintegrationofRNNswithotherML
techniquesandthechallengesindeployingthesemodelsinclinicalsettings.
Ismaeeletal.[35]examinedtheapplicationofRNNsinsmartcitytechnologies,includ-
ingtrafficprediction,energymanagement,andurbanplanning. Theirreviewdiscussedthe
potentialandlimitationsofRNNsintheseareasandsuggestedavenuesforfutureresearch.
Meanwhile,Mersetal.[36]reviewedtheapplicationsofRNNsinpavementperformance
forecastingandconductedacomprehensiveperformancecomparisonofthevariousRNN
models,includingsimpleRNNs,LSTM,GRU,andhybridLSTM–fullyconnectedneural
networks(LSTM-FCNNs).
Chenetal.[37]focusedontheuseofRNNsinenvironmentalmonitoringandclimate
modeling,discussingtheireffectivenessinpredictingenvironmentalchangesandmanaging
naturalresources.Theyalsohighlightedthechallengesinmodelingcomplexenvironmental
systems with RNNs. Linardos et al. [38] investigated the advancements in RNNs for
naturaldisasterpredictionandmanagement,highlightingthesuccessesandchallenges
in using RNNs for early warning systems, disaster response, and recovery planning.
Zhangetal.[39] discussed RNN applications in robotics, particularly focusing on path
planning,motioncontrol,andhuman–robotinteraction. Theydiscussedtheintegrationof
RNNswithotherDLtechniquesinrobotics. Thedifferentrelatedstudiesaretabulatedin
Table1,includingtheirmaincontributions.
Thisresearchaddressesthelimitationsintheexistingliteraturebyprovidingamore
comprehensivereviewthatincludesthelatestdevelopmentsinRNNarchitectures,suchas
hybridmodelsandneuralarchitecturesearch,aswellastheirapplicationsacrossawider
rangeofdomains. Additionally,thisreviewcontributestoamoreholisticunderstanding
ofthecurrentstateandfuturedirectionsofRNNresearchbyintegratingdiscussionson
scalability,robustness,andinteroperability.
Table1.SummaryofrelatedreviewsonRNNs.
Reference Year Description
Zarembaetal.[30] 2014 InsightsintoRNNsinlanguagemodeling
Chungetal.[33] 2014 SurveyofadvancementsinRNNtraining,optimiza-
tion,andarchitectures
Goodfellowetal.[27] 2016 Reviewondeeplearning,includingRNNs
Greffetal.[28] 2016 ExtensivecomparisonofLSTMvariants
Tarwanietal.[22] 2017 In-depthanalysisofRNNsinNLP
Chenetal.[37] 2018 EffectivenessofRNNsinenvironmentalmonitoring
andclimatemodeling
Baietal.[31] 2018 ComparisonofRNNswithothersequencemodeling
techniqueslikeCNNsandattentionmechanisms
Cheetal.[32] 2018 PotentialofRNNsinmedicalapplications

Information2024,15,517 4of34
Table1.Cont.
Reference Year Description
Zhangetal.[39] 2020 RNNapplicationsinrobotics,includingpathplan-
ning,motioncontrol,andhuman–robotinteraction
Duttaetal.[25] 2022 OverviewofRNNs,challengesintraining,andad-
vancementsinLSTMandGRUforsequencelearning
Linardosetal.[38] 2022 RNNsforearlywarningsystems,disasterresponse,
andrecoveryplanninginnaturaldisasterprediction
Badawyetal.[34] 2023 IntegrationofRNNswithotherMLtechniquesforpre-
dictiveanalyticsandpatientmonitoringinhealthcare
Ismaeeletal.[35] 2023 ApplicationofRNNsinsmartcitytechnologies,in-
cludingtrafficprediction,energymanagement,and
urbanplanning
Mersetal.[36] 2023 PerformancecomparisonofvariousRNNmodelsin
pavementperformanceforecasting
Quradaaetal.[26] 2024 Start-of-the-artreviewofRNNs,coveringcorearchi-
tectureswithafocusonapplicationsincodeclones
Al-Selwietal.[29] 2024 ReviewofLSTMapplicationsfrom2018to2023
3. FundamentalsofRNNs
3.1. BasicArchitectureandWorkingPrincipleofStandardRNNs
RNNs are designed to process sequential data by maintaining a hidden state that
capturesinformationaboutpreviousinputs[40]. Thebasicarchitectureconsistsofaninput
layer,ahiddenlayer,andanoutputlayer. Unlikefeedforwardneuralnetworks,RNNs
haverecurrentconnections,asshowninFigure1,allowinginformationtocyclewithinthe
networks. Ateachtimestep,t,theRNNtakesaninputvector,x ,andupdatesitshidden
t
state,h ,usingthefollowingequation:
t
h t = σ h (W xh x t +W hh h t−1 +b h ), (1)
whereW istheweightmatrixbetweentheinputandhiddenlayer, W istheweight
xh hh
matrixfortherecurrentconnection,b isthebiasvector,andσ istheactivationfunction,
h h
typically the hyperbolic tangent function (tanh) or the rectified linear unit [41,42]. The
outputateachtimestep,t,isgivenbythefollowing:
y = σ (W h +b ), (2)
t y hy t y
whereW istheweightmatrixbetweenthehiddenandoutputlayers,b isthebiasvector,
hy y
andσ istheactivationfunctionfortheoutputlayer.
y
Figure1.BasicRNNarchitecture.

Information2024,15,517
5of34
3.2. ActivationFunctions
ThecoreofRNNoperationsinvolvestherecurrentcomputationofthehiddenstate,
which integrates the current input with the previous hidden state [43]. This recurrent
computationallowsRNNstoexhibitdynamictemporalbehavior. Thechoiceofactivation
functionσ h playsacrucialroleinthebehaviorofthenetwork,introducingnon-linearity
thatenablesthenetworktolearnandrepresentcomplexpatternsinthedata[44,45]. One
commonlyusedactivationfunctioninRNNsisthehyperbolictangent(tanh). Thetanh
function squashes the input values to the range of [−1,1], making it zero-centered and
suitableformodelingsequenceswithbothpositiveandnegativevalues[46]. Thetanhis
representedmathematicallyasfollows:
ez−e−z
| σ (z) =tanh(z) | =      | (3) |
| -------------- | ------ | --- |
| h              | ez+e−z |     |
Anotherwidelyusedactivationfunctionistherectifiedlinearunit(ReLU).TheReLU
function outputs the input directly if it is positive; otherwise, it outputs zero [47]. This
simplicityhelpsmitigatethevanishinggradientproblemtosomeextentbyallowinggradients
toflowthroughthenetworkmoreeffectively.Furthermore,theLeakyReLUisavariantofthe
ReLUdesignedtoaddressthe“dyingReLU”problem,whereneuronscanbecomeinactive
andstoplearning[48]. TheleakyReLUallowsasmall,non-zerogradientwhentheinput
isnegative,thuskeepingtheneuronsactiveduringthetrainingprocess. Additionally,the
exponentiallinearunit(ELU)isanothervariantdesignedtobringthemeanactivationcloser
tozero,whichspeedsuplearningbyreducingbiasshifts[49]. TheELUtendstoimprove
learningcharacteristicsovertheReLUbyallowingtheactivationstotakeonnegativevalues
whentheinputisnegative.Theseactivationfunctionsarerepresentedasfollows:
| σ (z) =max(0,z) |     | (4) |
| --------------- | --- | --- |
h
(cid:40)
z ifz >0
| σ (z) = |           | (5) |
| ------- | --------- | --- |
| h αz    | otherwise |     |
(cid:40)
| z       | ifz >0 |     |
| ------- | ------ | --- |
| σ (z) = |        | (6) |
h
| α(ez−1) | otherwise |     |
| ------- | --------- | --- |
where α is a small constant, typically 0.01. Meanwhile, the sigmoid function squashes
the input values to the range [0,1]. It is similar to tanh but outputs values in a differ-
ent range, making it useful for problems where the output needs to be interpreted as
probabilities[50–52].Similarly,thesoftmaxfunctioniscommonlyusedintheoutputlayer
ofclassificationnetworkstoconvertrawscoresintoprobabilities[53]. Itisparticularly
usefulinmulti-classclassificationproblems. Thesigmoidandsoftmaxfunctionsarerepre-
sentedmathematicallyasfollows:
1
| σ (z) = |       | (7) |
| ------- | ----- | --- |
| h       | 1+e−z |     |
ezi
| σ (z ) | =     | (8) |
| ------ | ----- | --- |
| h i    | ∑ ezj |     |
j
wherez isthei-thelementoftheinputvectorz. Eachoftheseactivationfunctionshasits
i
advantagesandischosenbasedonthespecificrequirementsofthetaskathand.Meanwhile,
thehiddenstateupdateinRNNscanbeseenasafunction,h = f(x ,h ),whichcaptures
t t t−1
thedependenciesbetweentheinputsequenceandtherecurrentconnections. Thechoiceof
σ significantlyaffectshowwellthenetworklearnsthesedependenciesandgeneralizesto
h
newdata.

Information2024,15,517
6of34
3.3. TheVanishingandExplodingGradientProblems
TrainingRNNspresentssignificantchallengesduetothevanishingandexploding
gradientproblems. Duringthetrainingprocess,theBPTTalgorithmisusedtocomputethe
gradientsofthelossfunctionwithrespecttotheweights[54]. Asthegradientsarepropa-
gatedbackwardsintime,theycaneitherdiminish(vanish)orgrowexponentially(explode),
makingitdifficultforthenetworktolearnlong-termdependenciesorcausinginstability
duringtraining. Mathematically,thehiddenstateattimesteptcanbeexpandedasfollows:
| =       | (W +W     | (W +W        | +b )+b     | ).  |     |
| ------- | --------- | ------------ | ---------- | --- | --- |
| h t σ h | xh x t hh | σ h xh x t−1 | hh h t−2 h | h   | (9) |
Whencalculatingthegradients,weencountertermsinvolvingtheproductofmany
Jacobianmatrices:
t −1
∂h t ∏
|     |     | = J | ,   |     | (10) |
| --- | --- | --- | --- | --- | ---- |
|     | ∂h  |     | k   |     |      |
t−n k=t−n
where J is the Jacobian matrix of the hidden state at time step k. If the eigenvalues of
k
J arelessthan1,theproductofthesematriceswilltendtozeroasnincreases,leading
k
tovanishinggradients[55,56]. Conversely,iftheeigenvaluesofJ aregreaterthan1,the
k
gradients can grow exponentially, leading to exploding gradients, which can cause the
modelparameterstobecomeunstableandresultinnumericaloverflowduringtraining.
Thevanishinggradientproblempreventsthenetworkfromeffectivelylearninglong-term
dependencies,asthegradientsignalbecomestooweaktoupdatetheweightsmeaningfully
forearlierlayers. Ontheotherhand,theexplodinggradientproblemcancausethemodel
toconvergetooquicklytoapoorlocalminimumormakethetrainingprocessfailentirely
duetoexcessivelylargeupdates.
To mitigate these problems, various RNN variants have been developed, such as
LSTMandGRUs. Thesearchitecturesintroducegatingmechanismsthatregulatetheflow
of information and gradients through the network, allowing for the better handling of
long-termdependencies. Additionally,gradientclippingisacommontechniqueusedto
prevent exploding gradients by capping the gradients at a maximum threshold during
backpropagation,ensuringthattheydonotgrowuncontrollably[57,58].
3.4. BidirectionalRNNs
BidirectionalRNNs(BiRNNs)enhancethearchitecturebyprocessingthesequencein
bothforwardandbackwarddirections. Thisallowsthenetworktohaveaccesstofuture
context,aswellaspastcontext,improvingitsperformanceintasksforwhichunderstanding
both the preceding and succeeding elements is crucial [43,59]. In BiRNNs, two hidden
|     |     | −→  |     |     | ←−  |
| --- | --- | --- | --- | --- | --- |
statesaremaintained: onefortheforwardpass(h )andoneforthebackwardpass(h ):
|     |          | t       |       |     | t    |
| --- | -------- | ------- | ----- | --- | ---- |
|     | −→       | −→      |       |     |      |
|     | h = σ (W | x +W h  | +b ), |     | (11) |
|     | t h      | xh t hh | t−1 h |     |      |
|     | ←−       | ←−      |       |     |      |
|     | h = σ (W | x +W h  | +b ). |     | (12) |
|     | t h      | xh t hh | t+1 h |     |      |
Theoutputy isthencomputedbyconcatenatingtheforwardandbackwardhiddenstates:
t
−→ ←−
|     | y = σ | (W [h ; h ]+b | ),  |     | (13) |
| --- | ----- | ------------- | --- | --- | ---- |
|     | t     | y hy t t      | y   |     |      |
where [;] denotes concatenation. Furthermore, BiRNNs are effective for tasks such as
namedentityrecognition,machinetranslation,andspeechrecognition,wherecontextfrom
bothdirectionsimprovesthemodel’sperformance[60,61]. Throughaccessinginformation
fromboththepastandfuture,BiRNNscanprovideamorecomprehensiveunderstanding
oftheinputsequence. Forinstance,inlanguagemodeling,understandingthesurrounding
words can significantly enhance the accuracy of predicting the next word [62,63]. In
machinetranslation,knowingtheentiresentenceallowsthenetworktotranslatewords
more accurately, considering the entire context. Additionally, BiRNNs are also used in

Information2024,15,517 7of34
varioustimeseriesapplications,suchasstockpricepredictionandmedicaldiagnosis,where
understandingthetemporaldependenciesinbothdirectionsisbeneficial[64]. However,
BiRNNsrequiremorecomputationalresourcesthanunidirectionalRNNsduetotheneed
toprocessthesequencetwice(forwardandbackwards)[59,65].
3.5. DeepRNNs
DeepRNNsextendthebasicarchitecturebystackingmultipleRNNlayersontopof
eachother,whichallowsthenetworktolearnmorecomplexrepresentations[66]. Each
layer’shiddenstateservesastheinputtothesubsequentlayer, enhancingthemodel’s
capacitytocapturehierarchicalfeatures. ForadeepRNNwithLlayers,thehiddenstates
atlayerlandtimesteptareupdatedasfollows:
h
(l)
= σ (W
(l)
h
(l−1)
+W
(l)
h
(l)
+b
(l)
), (14)
t h xh t hh t−1 h
whereh
(0)
= x representstheinputatthefirstlayer. Theoutputatthetopmostlayeris
t t
thencomputedusingthesameprocedureasinbasicRNNs:
y = σ (W h
(L)
+b ). (15)
t y hy t y
DeepRNNscanmodelmorecomplexsequencesandcapturelongerdependencies
thanshallowRNNs[67]. However, theyarealsomorepronetothevanishinggradient
problem,whichcanbemitigatedbyusingadvancedvariantslikeLSTMorGRUs. Deep
RNNs have been successfully applied in various domains, including natural language
processing,speechrecognition,andvideoanalysis. InNLP,deepRNNscanmodelcom-
plexlinguisticstructuresandcapturelong-rangedependencies,improvingtaskssuchas
machinetranslationandtextgeneration. However,trainingdeepRNNscanbechallenging
due to the increased complexity and the risk of overfitting [68,69]. Techniques such as
dropout,layernormalization,andresidualconnectionsareoftenemployedtoimprovethe
trainingprocessandgeneralizationofdeepRNNs[70–72]. Dropouthelpspreventoverfit-
tingbyrandomlysettingafractionoftheunitstozeroduringtraining,whichencourages
thenetworktolearnmorerobustfeatures,whilebatchnormalizationhelpsstabilizeand
accelerate training by normalizing the inputs to each layer [73]. Residual connections,
whichaddshortcutconnectionsthatbypassoneormorelayers,helpmitigatethevanishing
gradientprobleminverydeepnetworks[74].
4. AdvancedVariantsofRNNs
RNN architectures can vary significantly, with some featuring internal recurrence
withinneuronsandothershavingexternalrecurrencebetweenlayers. Thesevariations
impactthenetwork’sabilitytolearnandprocesssequences,influencingtheirapplication
tospecifictasks.
4.1. LongShort-TermMemoryNetworks
LSTMnetworkswereintroducedbyHochreiterandSchmidhuber[15]toaddressthe
vanishinggradientprobleminherenttobasicRNNs. ThekeyinnovationinLSTMistheuse
ofgatingmechanismstocontroltheflowofinformationthroughthenetwork. Thisallows
LSTM networks to maintain and update their internal state over long periods, making
themeffectivefortasksrequiringthemodelingoflong-termdependencies. EachLSTMcell
containsthreegates: theinputgate,forgetgate,andoutputgate,whichregulatethecell
statec andhiddenstateh [75]. Thesegatesdeterminehowmuchoftheinputtoconsider,
t t
howmuchofthepreviousstatetoforget,andhowmuchofthecellstatetooutput. The
LSTMupdateequationsareasfollows:
i t = σ(W xi x t +W hi h t−1 +b i ), (16)
f t = σ(W xf x t +W hf h t−1 +b f ), (17)

Information2024,15,517
8of34
|     |     | o = σ(W | x    | +W h    | t−1 +b ), |     | (18) |
| --- | --- | ------- | ---- | ------- | --------- | --- | ---- |
|     |     | t       | xo t | ho      | o         |     |      |
|     |     | =tanh(W |      | +W      | +b ),     |     |      |
|     | g t |         | xg x | t hg    | h t−1 g   |     | (19) |
|     |     | c =     | f ⊙c | +i      | ⊙g ,      |     | (20) |
|     |     | t       | t    | t−1     | t t       |     |      |
|     |     | h       | = o  | ⊙tanh(c | ),        |     | (21) |
|     |     |         | t t  |         | t         |     |      |
where i is the input gate, f is the forget gate, o is the output gate, g is the cell input,
| t   | t   |     |     | t   |     | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
| c h |     |     |     |     |     |     |     |
t is the cell state, t is the hidden state, σ represents the sigmoid function, tanh is the
hyperbolictangentfunction,and⊙denoteselement-wisemultiplication[75].
Figure2illustratestheinternalarchitectureofanLSTMcell,whicheffectivelymanages
long-termdependenciesinsequencedatabyemployingthreecrucialgatingmechanisms:
theinputgate(i t ),forgetgate(f t ),andoutputgate(o t ). Eachofthesegatesplaysadistinct
roleincontrollingtheflowofinformationthroughthecell. Theinputgatecontrolshow
muchofthenewinputx t iswrittentothecellstatec t . Theforgetgatedecideshowmuch
ofthepreviouscellstatec shouldberetained. Theoutputgatedetermineshowmuchof
t−1
thecellstatec t isusedtocomputethehiddenstateh t . Thecellinputg t isacandidatevalue
thatisaddedtothecellstateafterbeingmodulatedviatheinputgate. Theuseofthese
gatingmechanismsallowsLSTMnetworkstoselectivelyrememberorforgetinformation,
enablingthemtohandlelong-termdependenciesmoreeffectivelythantraditionalRNNs.
The internal recurrence within the LSTM cell is managed through the cell state c t ,
whichactsasaconveyorbelt,transferringrelevantinformationacrossdifferenttimesteps.
ThisrecurrencemechanismallowstheLSTMtomaintainandupdateitsmemoryoverlong
sequences,effectivelycapturinglong-termdependencies. Additionally,theelement-wise
multiplicationoperationsbetweenthegatesandtheirrespectiveinputsensurethatthe
interactions between different components of the LSTM are smooth and efficient. This
enablestheLSTMtoperformcomplextransformationsontheinputdatawhilemaintaining
thestabilityofthelearningprocess. Meanwhile,LSTMnetworksutilizeinternalrecurrence
withineachcelltomanagelong-termdependencies,withtherecurrencehappeningthrough
thecell stateas information ispassed fromone timestep tothenext [21]. OtherLSTM
variantsincludebidirectionalLSTM(BiLSTM)andstackedLSTM.
Figure2.ArchitectureoftheLSTMnetwork[41].
4.2. BidirectionalLSTM
BidirectionalLSTM,showninFigure3,extendsthestandardLSTMarchitectureby
processingthesequenceinbothforwardandbackwarddirections,similartoBiRNNs[76].
Thisapproachallowsthenetworktocapturecontextfromboththepastandthefuture,
enhancingitsabilitytounderstanddependenciesinthesequencemorecomprehensively.
In BiLSTM, two separate hidden states are maintained for each time step: one for the
| −→  |     |     |     |     | ←−  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
forwardpass(h t )andoneforthebackwardpass(h t ). Thesehiddenstatesarecomputed
asdescribedinEquations(11)and(12).BiLSTMfeaturesexternalrecurrencebetweenlayers
astheyprocesstheinputsequenceinbothforwardandbackwarddirections,maintaining
separatehiddenstatesforeachdirection.

Information2024,15,517
9of34
Figure3.ArchitectureofBiLSTMnetwork[41].
StackedLSTM
StackedLSTMinvolvesstackingmultipleLSTMlayers,inwhichtheoutputofone
LSTMlayerservesastheinputtothenext,asshowninFigure4. Thisdeeparchitecture
allowsthenetworktocapturemorecomplexpatternsanddependenciesinthedataby
learninghierarchicalrepresentationsatdifferentlevelsofabstraction. ForastackedLSTM
with Llayers, the hidden states at layer l and time step t are updated as described in
Equations(14)and(15). Stacked LSTM incorporates external recurrence by connecting
multipleLSTMlayers,inwhicheachlayerpassesitsoutputasinputtothenext,allowing
thenetworktocapturemorecomplextemporalpatterns.
Figure4.AstackedLSTM[41].
StackingLSTMlayersallowsthenetworktolearnincreasinglycomplexfeaturesand
representations. Thelowerlayerscancapturelocalpatternsandshort-termdependencies,
whilethehigherlayerscancapturemoreabstractfeaturesandlong-termdependencies[21].
Thishierarchicallearningisadvantageousfortaskssuchaslanguagemodeling,wheredifferent
levelsofsyntacticandsemanticinformationneedtobecaptured,orforvideoanalysis,where
temporaldependenciesatdifferenttimescalesmustbeunderstood.WhilestackedLSTMoffers
improvedmodelingcapabilities,theyalsocomewithincreasedcomputationalcomplexityand
ahigherriskofoverfitting.
4.3. GatedRecurrentUnits
Gatedrecurrentunitsareanothervariantdesignedtoaddressthevanishinggradient
problemwhilesimplifyingtheLSTMarchitecture. IntroducedbyChoetal.[16], GRUs
combinetheforgetandinputgatesintoasingleupdategateandmergethecellstateand
hiddenstate,reducingthenumberofgatesandparametersandthussimplifyingthemodel
andmakingitcomputationallymoreefficient. TheGRUarchitectureconsistsoftwogates:
theupdategate,z t ,andtheresetgate,r t [77]. Figure5showstheGRUarchitecture. The
gatescontroltheflowofinformationtoensurethatrelevantinformationisretainedand
irrelevantinformationisdiscarded. SimilartoLSTM,GRUsrelyoninternalrecurrence
withineachunitastheymaintainandupdatethehiddenstateacrosstimestepstocapture
temporaldependencies. TheupdatedequationsforGRUsareasfollows:
|     | z =     | σ(W x    | +W  | h t−1 +b | ),  | (22) |
| --- | ------- | -------- | --- | -------- | --- | ---- |
|     | t       | xz t     | hz  | z        |     |      |
|     | =       | σ(W      | +W  | +b       | ),  |      |
|     | r t     | xr x t   | hr  | h t−1 r  |     | (23) |
| h ′ | =tanh(W | x +r     | ⊙(W | h )+b    | ),  | (24) |
| t   |         | xh t     | t   | hh t−1   | h   |      |
|     | h =     | (1−z )⊙h |     | +z ⊙h    | ′ , | (25) |
|     | t       | t        | t−1 | t        | t   |      |

Information2024,15,517 10of34
wherez istheupdategate,r istheresetgate,andh′ isthecandidatehiddenstate. The
t t t
updategatez t determineshowmuchoftheprevioushiddenstateh t−1 shouldbecarried
forwardtothecurrenthiddenstateh ,whiletheresetgate,r ,controlshowmuchofthe
t t
previous hidden state to forget [75]. The candidate hidden state h′ represents the new
t
contenttobeaddedtothecurrenthiddenstate,modulatedviatheresetgate. Furthermore,
thesimplifiedarchitectureofGRUsallowsthemtobecomputationallymoreefficientthan
LSTMwhilestilladdressingthevanishinggradientproblem. ThisefficiencymakesGRUs
well-suitedfortaskswherecomputationalresourcesarelimitedorwhentrainingneedsto
befaster. GRUshavebeensuccessfullyappliedinvarioussequencemodelingtasks. Their
abilitytocapturelong-termdependencieswithfewerparametersmakesthemapopular
choice in many applications. Additionally, studies have shown that GRUs can achieve
performancecomparabletoLSTM[78–80],makingthemanattractivealternativeformany
usecases.
Figure5.ArchitectureoftheGRUnetwork.
ComparisonwithLSTM
GRUshavefewerparameterscomparedtoLSTMduetotheabsenceofaseparatecell
stateandcombinedgatingmechanisms[81]. Thisoftenleadstofastertrainingtimesand
comparableperformancetoLSTMinmanytasks. However,despitetheiradvantages,the
choicebetweenGRUsandLSTMoftendependsonthespecifictaskanddataset. Some
tasksmaybenefitmorefromtheadditionalcomplexityandgatingmechanismsofLSTM,
whileothersmayperformequallywellwiththesimplerGRUarchitecture.
4.4. OtherNotableVariants
WhileLSTMandGRUsarethemostwidelyusedRNNvariants,otherarchitectures
likepeepholeLSTM,echostatenetworks,andindependentlyrecurrentneuralnetworks
offeruniqueadvantagesforspecificapplications.
4.4.1. PeepholeLSTM
PeepholeLSTM,introducedbyGersandSchmidhuber[82],enhancesstandardLSTM
byallowingthegatestohaveaccesstothecellstatethroughpeepholeconnections. This
additionalconnectionenablestheLSTMtobetterregulatethegatingmechanismsbasedon
thecurrentcellstate,improvingtimingdecisionsinapplicationssuchasspeechrecognition
andfinancial timeseriesprediction [83]. Inthefollowingequations, theinput gate(i ),
t
forgetgate(f ),andoutputgate(o )areenhancedwithpeepholeconnections:
t t
i t = σ(W xi x t +W hi h t−1 +W ci c t−1 +b i ), (26)
wherei t istheinputgate,andW ci isthepeepholeweightconnectingthecellstatec t−1 to
theinputgate.
f t = σ(W xf x t +W hf h t−1 +W cf c t−1 +b f ), (27)

Information2024,15,517 11of34
wheref t istheforgetgate,andW cf isthepeepholeweightconnectingthecellstatec t−1 to
theforgetgate.
o t = σ(W xo x t +W ho h t−1 +W co c t +b o ), (28)
whereo istheoutputgate,andW isthepeepholeweightconnectingthecellstatec to
t co t
theoutputgate.
4.4.2. EchoStateNetworks
Echostatenetworks(ESNs), proposedbyJaeger[84], representaclassofRNNsin
which the hidden layer, also known as the reservoir, is fixed and randomly connected,
whileonlytheoutputlayeristrained. Thisarchitecturesignificantlysimplifiesthetraining
process, making ESNs particularly suitable for real-time signal processing, time series
prediction, andadaptivecontrolsystems. Thestateupdateandoutputcomputationin
ESNsareachievedthroughthefollowingequations:
h t =tanh(W in x t +W res h t−1 ), (29)
whereh isthehiddenstate,W istheinputweightmatrix,andW isthefixed,randomly
t in res
initializedreservoirweightmatrix. Whenitis assumed that W isthetrainedoutput
out
weightmatrix,theoutputofthenetworkcanberepresentedasfollows:
y = W h , (30)
t out t
ESNshavegainedsignificantattentionduetotheirabilitytohandlecomplextem-
poraldynamicswitharelativelysimpleandefficienttrainingprocess[85,86]. However,
traditionalESNsarelimitedduetothefixednatureofthereservoir,whichcanrestricttheir
adaptabilityandperformanceinmorecomplextasks. Toaddresstheselimitations,several
advancementshavebeenproposed:
• Deep Echo-State Networks: Recent research has extended the ESN architecture to
deepervariants,knownasdeepecho-statenetworks(DeepESNs).InDeepESNs,multi-
plereservoirlayersarestacked,allowingthenetworktocapturehierarchicaltemporal
featuresacrossdifferenttimescales[87]. EachlayerinaDeepESNprocessestheoutput
fromthepreviouslayer’sreservoir,enablingthemodeltolearnmoreabstractand
complexrepresentationsoftheinputdata. ThestateupdateforaDeepESNcanbe
generalizedasfollows:
hl =tanh(Wl hl−1+Wl hl ), (31)
t in t res t−1
where l denotes the layer number, hl is the hidden state at layer l, Wl is the in-
t in
putweightmatrixforlayer l, and
hl−1
isthehiddenstatefromthepreviouslayer.
t
DeepESNs have demonstrated improved performance in tasks requiring the mod-
eling of complex temporal patterns, such as speech recognition and financial time
seriesforecasting[88].
• EnsembleDeepESNs: InensembledeepESNs, multipleDeepESNsaretrainedin-
dependently,andtheiroutputsarecombinedtoformthefinalprediction[89]. This
ensembleapproachleveragesthediversityofthereservoirsandthedeeparchitecture
toimproverobustnessandaccuracy,particularlyintimeseriesforecastingapplica-
tions. Forinstance, Gaoetal.[90]demonstratedtheeffectivenessofDeepESNen-
semblesinpredictingsignificantwaveheights,wheretheensembleapproachhelped
mitigatetheimpactofreservoirinitializationvariabilityandimprovedthemodel’s
generalizationability.
• InputProcessingwithSignalDecomposition: Anothercriticalaspectofeffectively
utilizingRNNsandESNsisthepreprocessingofinputsignals. Giventhecomplex
andoftennoisynatureofreal-worldtimeseriesdata,signaldecompositiontechniques
suchastheempiricalwavelettransform(EWT)havebeenemployedtoenhancethe
inputtoESNs[91]. TheEWTdecomposestheinputsignalintodifferentfrequency

Information2024,15,517
12of34
components,allowingtheESNtoprocesseachcomponentseparatelyandimprove
the model’s ability to capture underlying patterns. The combination of the EWT
withESNshasshownpromisingresultsinvariousapplications,includingtimeseries
forecasting,whereithelpsreducenoiseandenhancethepredictiveperformanceof
themodel.
4.4.3. IndependentlyRecurrentNeuralNetwork
Most recently, independently recurrent neural networks (IndRNNs), proposed
byLietal.[92], have used independent recurrent units to address the gradient vanish-
ingandexplodingproblems,makingiteasiertotrainverydeepRNNs. Thisarchitectureis
usefulforlongsequencetaskssuchasvideosequenceanalysisandlongtextgeneration.
Whenitisassumedthath t isthehiddenstate,W xh istheinputweightmatrix,anduisa
vectorofrecurrentweights. ThestateupdateequationforIndRNNisasfollows:
|     |     |     | = σ(W | +u⊙h | ),  |     |     |      |
| --- | --- | --- | ----- | ---- | --- | --- | --- | ---- |
|     |     | h t | xh x  | t    | t−1 |     |     | (32) |
ThevariousRNNarchitecturesaresummarizedinTable2.
Table2.ComparativeoverviewofRNNarchitectures.
| RNNType | KeyFeatures |     | GradientStability |     |     | TypicalApplications |     |     |
| ------- | ----------- | --- | ----------------- | --- | --- | ------------------- | --- | --- |
Simple structure with Highriskofvanishing Simplesequencetaskslike
BasicRNN
|      | short-termmemory     |        | gradients             |     |     | textgeneration    |              |     |
| ---- | -------------------- | ------ | --------------------- | --- | --- | ----------------- | ------------ | --- |
|      | Long-term            | memory |                       |     |     |                   |              |     |
|      |                      |        | Stable,handlesvanish- |     |     | Language          | translation, |     |
| LSTM | withinput,forget,and |        |                       |     |     |                   |              |     |
|      |                      |        | inggradientswell      |     |     | speechrecognition |              |     |
outputgates
|     |                    |     | Stable, | handles   | van-   |                  |     |        |
| --- | ------------------ | --- | ------- | --------- | ------ | ---------------- | --- | ------ |
|     | SimplifiedLSTMwith |     |         |           |        | Tasks requiring  |     | faster |
| GRU |                    |     | ishing  | gradients | effec- |                  |     |        |
|     | fewergates         |     |         |           |        | trainingthanLSTM |     |        |
tively
Processesdatainboth
Bidirectionalforwardandbackward Medium stability, de- Speech recognition and
| RNN | directions | for better | pendsondepth |     |     | sentimentanalysis |     |     |
| --- | ---------- | ---------- | ------------ | --- | --- | ----------------- | --- | --- |
contextunderstanding
|     | Multiple | RNN layers | Variable, | and | the risk |     |     |     |
| --- | -------- | ---------- | --------- | --- | -------- | --- | --- | --- |
Complexsequencemodel-
| DeepRNN | arestackedtolearnhi- |     | ofvanishinggradients |     |     |     |     |     |
| ------- | -------------------- | --- | -------------------- | --- | --- | --- | --- | --- |
inglikevideoprocessing
|     | erarchicalfeatures |              | increaseswithdepth    |     |     |     |     |     |
| --- | ------------------ | ------------ | --------------------- | --- | --- | --- | --- | --- |
|     | Fixed              | hidden layer | Notapplicableastrain- |     |     |     |     |     |
Timeseriespredictionand
| ESN | weights, | trained only | ing bypasses |     | typical |     |     |     |
| --- | -------- | ------------ | ------------ | --- | ------- | --- | --- | --- |
systemcontrol
|          | attheoutput         |     | gradientissues |             |     |             |            |     |
| -------- | ------------------- | --- | -------------- | ----------- | --- | ----------- | ---------- | --- |
|          |                     |     |                |             |     | Recognition | of complex |     |
| Peephole | Addspeepholeconnec- |     | Stable         | and similar |     | to          |            |     |
temporalpatternslikemu-
| LSTM | tionstoLSTMgates |     | LSTM |     |     |     |     |     |
| ---- | ---------------- | --- | ---- | --- | --- | --- | --- | --- |
sicalnotation
|     | Allows | training | of  |     |     |     |     |     |
| --- | ------ | -------- | --- | --- | --- | --- | --- | --- |
deeper networks by Reducesriskofvanish- Verylongsequences,such
IndRNN maintaining indepen- ingandexplodinggra- as in video processing or
|     | dence | between time | dients |     |     | longtextgeneration |     |     |
| --- | ----- | ------------ | ------ | --- | --- | ------------------ | --- | --- |
steps
5. InnovationsinRNNArchitecturesandTrainingMethodologies
Inrecentyears,therehavebeensignificantinnovationsinRNNarchitecturesandtrain-
ingmethodologiesaimedatenhancingperformanceandaddressingexistinglimitations.

Information2024,15,517
13of34
5.1. HybridArchitectures
CombiningRNNswithotherneuralnetworkarchitectureshasledtohybridmodels
thatleveragethestrengthsofeachcomponent. Forexample,integratingCNNswithRNNs
hasproveneffectiveinvideoanalysis,whereCNNshandlespatialfeatureswhileRNNs
capturetemporaldynamics[93,93]. Thisapproachallowsthemodeltoprocessbothspatial
andtemporalinformation,enhancingitsabilitytorecognizepatternsandmakepredictions.
Furthermore, incorporating attention mechanisms into RNNs has also improved their
abilitytomodellong-rangedependencies. Attentionmechanismsenablethenetworkto
focusonrelevantpartsoftheinputsequence, whichisusefulintaskssuchasmachine
translationandtextsummarization. Theattentionmechanismcanbedescribedasfollows:
|     | =softmax(u |     | ),  |     |      |
| --- | ---------- | --- | --- | --- | ---- |
|     | a t        |     | t   |     | (33) |
T
∑
|     | c   | = a | h,    |     | (34) |
| --- | --- | --- | ----- | --- | ---- |
|     |     | t   | t,i i |     |      |
i=1
wherea istheattentionweight,u isthescorefunction,andc isthecontextvector.
| t   | t   |     |     | t   |     |
| --- | --- | --- | --- | --- | --- |
5.2. NeuralArchitectureSearch
Neural architecture search (NAS) has automated the design of RNN architectures,
enablingthediscoveryofmoreefficientandpowerfulmodels[94,95].NAStechniques,such
asthosepioneeredbyZophandLe[96],explorevariouscombinationsoflayers,activation
functions,andhyperparameterstofindoptimalconfigurationsthatoutperformmanually
designedarchitectures. TheNASprocesscanbeformulatedasanoptimizationproblem:
|     | A∗ =argmaxAccuracy(A), |     |     |     | (35) |
| --- | ---------------------- | --- | --- | --- | ---- |
A∈S
isthesearchspace,andA∗istheoptimalarchitecture.
whereArepresentsanarchitecture,S
5.3. AdvancedOptimizationTechniques
Advanced optimization techniques have been developed to improve the training
efficiency and stability of RNNs. Gradient clipping is a technique used to prevent the
gradientsfrombecomingtoolarge,whichcandestabilizetraining[58,97].
g
←
|     | g   |     | ,   |     | (36) |
| --- | --- | --- | --- | --- | ---- |
max(1, ∥g∥ )
τ
where g is the gradient, and τ is the threshold value. Furthermore, adaptive learning
rates,suchasthoseusedintheAdamoptimizer,adjustthelearningrateduringtrainingto
accelerateconvergenceandimproveperformance[98]. TheAdamoptimizerupdatesthe
parametersusingthefollowing:
|     | m = β | m +(1−β | )g  | ,   | (37) |
| --- | ----- | ------- | --- | --- | ---- |
|     | t 1   | t−1     | 1 t |     |      |
)g2
|     | v t = β | v t−1 +(1−β | ,      |     | (38) |
| --- | ------- | ----------- | ------ | --- | ---- |
|     | 2       |             | 2 t    |     |      |
|     | m       | t           | v t    |     |      |
|     | mˆ =    | , vˆ        | =      | ,   | (39) |
|     | t 1−βt  |             | t 1−βt |     |      |
|     |         | 1           | 2      |     |      |
mˆ
|     | θ = θ | −α√ | t , |     | (40) |
| --- | ----- | --- | --- | --- | ---- |
t t−1
vˆ +ϵ
t
wherem andv arethefirst-andsecond-momentestimates,β andβ arethedecayrates,α
| t t |     |     |     | 1 2 |     |
| --- | --- | --- | --- | --- | --- |
isthelearningrate,andϵisasmallconstant[98].Also,second-orderoptimizationmethods,
suchastheHessian-freeoptimizer,havealsobeenexploredtoimprovetheconvergence
speedandstabilityoftrainingdeepnetworks.

Information2024,15,517 14of34
5.4. RNNswithAttentionMechanisms
Integrating attention mechanisms into RNNs allows these networks to selectively
focusonimportantpartsoftheinputsequence,addressingthelimitationsoftraditional
RNNsinmodelinglong-termdependencies[99–101]. Thishybridapproachcombinesthe
strengthsofRNNsandattentionmechanisms,enhancingtheircapabilitytohandlecomplex
sequencetasks. Attention-enhancedRNNshaveshownsignificantimprovementsintasks
suchasspeechrecognitionandtextsummarization. Forexample, Bahdanauetal.[102]
demonstratedtheuseofattentionmechanismsinneuralmachinetranslation,whichal-
lowed RNNs to focus on relevant words in the source sentence, improving translation
accuracy. Similarly, Luongetal.[103]proposedglobalandlocalattentionmechanisms,
furtherenhancingtheperformanceofRNNsinvarioussequence-to-sequencetasks.
5.5. RNNsIntegratedwithTransformerModels
Transformers,introducedbyVaswanietal.[104]in2017,employself-attentionmecha-
nismsandhaveproventobehighlyeffectiveincapturinglong-rangedependencies. Unlike
RNNs,transformersprocesssequencesinparallel,whichcanleadtobetterperformanceon
longsequences. Theself-attentionmechanismisdefinedasfollows:
(cid:32) (cid:33)
QKT
Attention(Q,K,V) =softmax √ V, (41)
d
k
where Q, K, and V are the query, key, and value matrices, respectively, and d is the
k
dimension of the keys. Considering that both transformer and RNN architecture have
limitations, studies have integrated both methods to obtain robust models, as shown
in the recent literature [104]. Therefore, researchers can develop more powerful and
efficientmodelsforawiderangeofapplicationsbyleveragingthesequentialprocessing
capabilitiesofRNNsandtheparallel,attention-basedmechanismsoftransformers. This
integratedapproachaddressesthelimitationsofeacharchitectureandenhancestheoverall
performanceinsequencemodelingtasks.
6. PublicDatasetsforRNNResearch
Thissectionprovidesanoverviewofpubliclyavailabledatasetsthatarecommonly
usedinthestudyandevaluationofRNNs. Thesedatasetscoveravarietyofapplications,
rangingfromnaturallanguageprocessingtotimeseriesforecasting,reflectingthediverse
capabilities of RNNs. Each of these datasets provides a unique challenge for RNNs,
allowingresearcherstoexplorethestrengthsandlimitationsofdifferentRNNarchitectures
across various real-world tasks. Table 3 summarizes the publicly available datasets for
RNNresearch.
Table3.PublicdatasetsforstudyingRNNs.
DatasetName Application Description
A corpus of English sentences annotated for
Penn Natural part-of-speechtagging,parsing,andnameden-
Treebank[105] languageprocessing tityrecognition;widelyusedforlanguagemod-
elingwithRNNs
Adatasetofmoviereviewsusedforbinarysen-
IMDB timentclassification; suitableforstudyingthe
Sentimentanalysis
Reviews[106] effectivenessofRNNsintextsentimentclassifi-
cationtasks
A version of the MNIST dataset formatted as
MNIST
Imagerecognition sequences for studying sequence-to-sequence
Sequential[107]
learningwithRNNs

Information2024,15,517 15of34
Table3.Cont.
DatasetName Application Description
TIMIT Speech An annotated speech database used for auto-
Speechrecognition
Corpus[108] maticspeechrecognitionsystems
Reuters-21578
Acollectionofnewswirearticlesthatisacom-
Text
Textcategorization monbenchmarkfortextcategorizationandNLP
Categorization
taskswithRNNs
Collection[109]
UCIMLReposi- Containsvarioustimeseriesdatasets,including
tory:TimeSeries Timeseriesanalysis stockpricesandweatherdata,idealforforecast-
Data[110] ingwithRNNs.
Used for continuous object recognition, ideal
CORe50 for RNN models dealing with video input se-
ObjectRecognition
Dataset[111] quenceswhereobjectpersistenceandtemporal
contextareimportant
7. ApplicationsofRNNsinPeer-ReviewedLiterature
RNNsandtheirvariantshavebeenextensivelystudiedandappliedacrossvarious
domainsinthepeer-reviewedliterature. Thissectionprovidesacomprehensivereviewof
theseapplications.
7.1. NaturalLanguageProcessing
RNNshavetransformedthefieldofNLPbyenablingmoresophisticatedandcontext-
awaremodels. SeveralstudieshavedemonstratedtheeffectivenessofRNNsinvarious
NLPtasks.
7.1.1. TextGeneration
RNNshavebeenusedextensivelyfortext-generationtasks. Sourietal.[112]demon-
stratedtheuseofRNNstogeneratecoherentandcontextuallyrelevantArabictext. Their
modelwastrainedonalargecorpusoftextdata,allowingittolearntheprobabilitydistribu-
tionofwordsequences,whichprovedeffectiveingeneratinghuman-liketext. Meanwhile,
several researchers have proposed novel approaches to enhancing the performance of
RNNs in text generation. For instance, Islam [113] introduced a sequence-to-sequence
frameworkthatimprovedthegenerationqualityusingLSTM.Thismethodallowedthe
networktohandlelongersequencesandmaintaincoherenceoverextendedtext.
Gajendranetal.[114]demonstratedtheeffectivenessofRNNsingeneratingcharacter-
leveltext. TheirworkshowedthatBiLSTMcouldcaptureawiderangeofpatterns,from
character-leveldependenciestohigher-levelsyntacticstructures,makingthemversatile
fordifferenttextgenerationtasks,includingthegenerationofcode,literature,andpoetry.
Morerecently,advancementsinRNN-basedtextgenerationhavefocusedonimprovingthe
diversityandcoherenceofgeneratedtext. Huetal.[115]proposedtheuseofvariational
autoencoders(VAEs)combinedwithRNNstoenhancethecreativityoftextgeneration.
Their approach enabled the generation of diverse and contextually rich sentences by
learningalatentspacerepresentationofthetext.
Meanwhile,Holtzmanetal.[116]introducedtheconceptof“controlledtextgeneration”
usingRNNs,whichalloweduserstoinfluencethestyleandcontentofthegeneratedtext.
Thismethodprovidedmoreflexibilityandcontroloverthetextgenerationprocess,making
it useful for applications such as creative writing and personalized content generation.
Additionally,withtheadventofmoresophisticatedmodelsliketransformers,RNN-based
textgenerationhasevolvedtoincorporateattentionmechanisms.
Yinetal.[117]proposedanapproachcombiningRNNwithanattentionmechanism,
whichallowsthemodeltofocusonrelevantpartsoftheinputsequenceduringthegenera-

Information2024,15,517 16of34
tionprocess. Thissignificantlyimprovedthequalityandcoherenceofthegeneratedtextby
dynamicallyadjustingthefocusofthemodelbasedonthecontext.HusseinandSavas[118]
employedLSTMfortextgeneration.Similarly,Baskaranetal.[119]employedLSTMfortext
generation,achievingexcellentperformance. ThesestudiesshowedthatLSTMnetworks
arecapableofgeneratingtextsthatarecontextuallyrelevantandlinguisticallyaccurate.
Furthermore,studieshavecontinuedtoexploreandenhancethecapabilitiesofRNNs
intextgeneration. Keskaretal.[120]introducedalarge-scalelanguagemodelknownas
ConditionalTransformerLanguage(CTRL),whichcanbeconditionedonspecificcontrol
codestogeneratetextinvariousstylesanddomains. Thisworkhighlightsthegrowing
trend of combining RNNs with transformer architectures to leverage their strengths in
sequence modeling and text generation. Additionally, Guo [121] explored the integra-
tion of reinforcement learning with RNNs for text generation. The approach aimed to
optimizethegenerationprocessbyrewardingthemodelforproducinghigh-quality,con-
textually appropriate text, thereby improving both the coherence and relevance of the
generatedcontent.
In text generation tasks, the LSTM networks have proven to be the most effective
amongRNNarchitectures. TheLSTM’sabilitytomanagelong-termdependenciesthrough
itsgatingmechanismsmakesitwell-suitedforgeneratingcoherentandcontextuallyrel-
evant text over extended sequences. Studies such as those by Souri et al. [112] and
Gajendranetal. [114]highlighttheversatilityofLSTMinhandlingbothword-leveland
character-level text generation tasks, respectively. While more recent models, such as
thoseincorporatingtransformers,havegainedpopularity,LSTM-basedmodelscontinue
to be preferred for scenarios requiring robust sequence modeling with fewer computa-
tionalresources,especiallywhendealingwithsmallerdatasetswherethecomplexityof
transformersmightnotbenecessary.
7.1.2. SentimentAnalysis
In sentiment analysis, RNNs have been shown to outperform traditional models
by capturing the context and details of sentiment expressed in text. Yadav et al. [122]
used LSTM-based models to analyze customer reviews and social media posts, achiev-
ing notable improvements in accuracy over conventional methods. Building on this,
Abimbolaetal. [123]proposedahybridLSTM-CNNmodelfordocument-levelsentiment
classification,whichfirstcapturesthesentimentofindividualsentencesandthenaggre-
gatesthemtodeterminetheoverallsentimentofthedocument. Thishierarchicalapproach
allowsforamoredetailedunderstandingofsentiment,especiallyinlongandcomplextexts.
Zulqarnainetal.[124]utilizedtheconceptofattentionmechanismsandGRUtoenhance
sentimentanalysis. Byallowingthemodeltofocusonspecificpartsoftheinputtextthat
aremostindicativeofsentiment,attentionmechanismssignificantlyimprovedtheinter-
pretabilityandperformanceofsentimentanalysismodels. Thisadvancementenabledthe
modelstohighlightwhichwordsorphrasescontributethemosttosentimentprediction.
Additionally,severalstudieshaveexploredtheintegrationofRNNswithCNNsto
leveragethestrengthsofbotharchitectures.Forinstance,Pujarietal.[125]combinedCNNs
andRNNstocapturebothlocalfeaturesandlong-rangedependenciesintext,resulting
inahybridmodelthatachievedstate-of-the-artperformanceinsentimentclassification
tasks. Meanwhile, Wankhade et al. [126] employed the fusion of CNN and BiLSTM
withanattentionmechanism,leadingtoenhancedsentimentclassification. Furthermore,
SangeethaandKumaran[127]utilizedBiLSTMtoenhancethesentimentanalysiscapability
byprocessingtextinbothforwardandbackwarddirections. Thisapproachcapturesthe
contextfrombothpastandfuturewords,providingamorecomprehensiveunderstanding
ofthesentimentexpressedinthetext.
Inadditiontothesearchitecturalinnovations,therehasbeenafocusonimprovingthe
robustnessofRNN-basedsentimentanalysismodels. Forexample,HeandMcAuley[128]
developedanadversarialtrainingframeworkthatenhancesthemodel’sabilitytohandle
noisyandadversarialtextinputs,therebyimprovingitsgeneralizationtoreal-worlddata.

Information2024,15,517 17of34
Also,theuseoftransferlearningandpre-trainedlanguagemodels,suchasBERTandGPT,
hasbeenincreasinglypopularinsentimentanalysis[129–131].Thesemodels,fine-tunedfor
sentimentclassificationtasks,havedemonstratedexceptionalperformancebyleveraging
large-scalepre-trainingondiversetextcorporaandthenadaptingtospecificsentiment
analysisdatasets.
Furthermore,BiLSTMcanbeconsideredthemosteffectivevariantofRNNsinsenti-
mentanalysisduetotheirabilitytoprocesstextinbothforwardandbackwarddirections.
Thisbidirectionalprocessingallowsthemodeltocapturethefullcontextofasentence,
making it effective in understanding intrinsic sentiment expressed in text. Studies by
SangeethaandKumaran[127]demonstratethesuperiorityofBiLSTMinachievinghigher
accuracyinsentimentclassificationtasks. TheabilityofBiLSTMtointegratewithattention
mechanisms,asshowninworkbyWankhadeetal.[126],furtherenhancestheirperfor-
mancebyallowingthemodeltofocusonthemostrelevantpartsofthetext,thusimproving
interpretabilityandclassificationaccuracy.
7.1.3. MachineTranslation
Toaddressthechallengeoftranslatinglongsentences,Wuetal.[132]introducedthe
conceptofdeepRNNswithmultiplelayersinboththeencoderanddecoder. Theirmodel,
knownasGoogleNeuralMachineTranslation(GNMT),improvedtranslationaccuracy
andfluencybycapturingmorecomplexpatternsanddependencieswithinthetext. GNMT
becameamajorachievementinneuralmachinetranslation,settinganewbenchmarkfor
translationsystems. Sennrichetal.[133]presentedamethodforincorporatingsubword
unitsintoRNN-basedtranslationmodels. Thisapproach,knownasByte-PairEncoding
(BPE),enabledthetranslationmodelstohandlerareandout-of-vocabularywordsmore
effectively by splitting them into smaller, more frequent subword units. This method
improvedtherobustnessandgeneralizationofthetranslationmodels.
Withtheadventoftransformermodels,Vaswanietal.[104]revolutionizedthefield
ofmachinetranslationbyintroducingafullyattention-basedarchitecturethateliminated
the need for recurrence entirely. Transformers demonstrated superior performance in
translationtasksbyallowingforparallelprocessingofsequencesandcapturinglong-range
dependenciesmoreefficiently. Despitethisshift,RNN-basedmodelswithattentionmecha-
nismscontinuedtoberelevant,particularlyinscenarioswherecomputationalresources
werelimitedorsequentialprocessingwaspreferred. Forexample,Kangetal.[134]com-
binedRNNwithanattentionmechanismtoobtainabilingualattention-basedmachine
translation model. While Zulqarnain et al. [124] utilized GRU in a multi-stage feature
attentionmechanismmodel.
Several studies have also combined RNNs with transformer models to utilize the
strengthsofbotharchitectures. Forinstance,Yangetal.[135]proposedahybridmodelthat
integratesRNNsintothetransformerarchitecturetoenhanceitsabilitytocapturesequential
dependencieswhilemaintainingtheefficiencyofparallelprocessing. Thishybridapproach
achieved state-of-the-art performance in several translation benchmarks. Meanwhile,
more recent studies have explored the integration of pre-trained language models like
BERT and GPT into machine translation systems. Song et al. [136] demonstrated that
incorporatingBERTintotheencoderofatranslationmodelenhanceditsunderstandingof
thesourcelanguage,leadingtomoreaccurateandfluenttranslations. Table4summarizes
thediscussedapplicationsofRNNsinnaturallanguageprocessing.
HybridmodelsthatcombinethestrengthsofRNNs,particularlyLSTM,withtrans-
former architectures are considered the best approach to machine translation. While
transformershavesetnewbenchmarksintranslationaccuracyduetotheirparallelpro-
cessingcapabilitiesandefficienthandlingoflong-rangedependencies,integratingRNNs
withattentionmechanisms,asseeninstudiesbyYangetal. [135]andSongetal. [136],
hasshownthatthesehybridmodelscanoutperformpurelytransformer-basedapproaches
incertainscenarios. Thisisespeciallytrueinresource-constrainedenvironmentswhere

Information2024,15,517
18of34
thesequentialprocessingofRNNs,enhancedbyattentionmechanisms,canleadtomore
accurateandcomputationallyefficienttranslations.
Table4.SummaryofapplicationsofRNNsinnaturallanguageprocessing.
| ApplicationDomain | Reference       | Year | MethodsandApplication |                |          |     |                  |     |          |
| ----------------- | --------------- | ---- | --------------------- | -------------- | -------- | --- | ---------------- | --- | -------- |
|                   |                 |      | RNNs                  | for generating | coherent |     | and contextually |     | relevant |
| Textgeneration    | Sourietal.[112] | 2018 |                       |                |          |     |                  |     |          |
Arabictext
|     |                    |      | Controlled | text | generation | using | RNNs | for | style and |
| --- | ------------------ | ---- | ---------- | ---- | ---------- | ----- | ---- | --- | --------- |
|     | Holtzmanetal.[116] | 2019 |            |      |            |       |      |     |           |
contentcontrol
|     |              |      | VAEs | combined | with RNNs |     | to enhance | creativity | in  |
| --- | ------------ | ---- | ---- | -------- | --------- | --- | ---------- | ---------- | --- |
|     | Huetal.[115] | 2020 |      |          |           |     |            |            |     |
textgeneration
Gajendranetal.[114] 2020 Character-leveltextgenerationusingBiLSTMforvarioustasks
|     | HusseinandSavas[118] | 2024 | LSTMfortextgeneration |     |     |     |     |     |     |
| --- | -------------------- | ---- | --------------------- | --- | --- | --- | --- | --- | --- |
Baskaranetal.[119] 2024 LSTMfortextgeneration,achievingexcellentperformance
Sequence-to-sequenceframeworkusingLSTMforimprovedtext
|     | Islam[113] | 2019 |     |     |     |     |     |     |     |
| --- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- |
generationquality
AttentionmechanismswithRNNsforimprovedtextgeneration
|     | Yinetal.[117] | 2018 |     |     |     |     |     |     |     |
| --- | ------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
quality
|     |          |      | Integration | of  | reinforcement |     | learning | with | RNNs for |
| --- | -------- | ---- | ----------- | --- | ------------- | --- | -------- | ---- | -------- |
|     | Guo[121] | 2015 |             |     |               |     |          |      |          |
textgeneration
ConditionalTransformerLanguage(CTRL)forgeneratingtextin
|     | Keskaretal.[120] | 2019 |     |     |     |     |     |     |     |
| --- | ---------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
variousstyles
|                   |                   |      | Adversarial | training | framework |     | for robustness |     | in sentiment |
| ----------------- | ----------------- | ---- | ----------- | -------- | --------- | --- | -------------- | --- | ------------ |
| Sentimentanalysis | HeandMcAuley[128] | 2016 |             |          |           |     |                |     |              |
analysis
Pujarietal.[125] 2024 HybridCNN-RNNmodelforsentimentclassification
FusionofCNNandBiLSTMwithattentionmechanismforsenti-
|     | Wankhadeetal. [126] | 2024 |     |     |     |     |     |     |     |
| --- | ------------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
mentclassification
|     |                          |      | BiLSTM | for | sentiment | analysis | by processing |     | text in |
| --- | ------------------------ | ---- | ------ | --- | --------- | -------- | ------------- | --- | ------- |
|     | SangeethaandKumaran[127] | 2023 |        |     |           |          |               |     |         |
bothdirections
LSTM-basedmodelsforsentimentanalysisincustomerreviews
|     | Yadavetal.[122] | 2023 |     |     |     |     |     |     |     |
| --- | --------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
andsocialmediaposts
Zulqarnainetal.[124] 2024 AttentionmechanismsandGRUforenhancedsentimentanalysis
Samiretal.[129] 2021 Useofpre-trainedmodelslikeBERTforsentimentanalysis
Prottashaetal.[130] 2022 TransferlearningwithBERTandGPTforsentimentanalysis
|     |                    |      | Hybrid | LSTM-CNN | model | for | document-level |     | sentiment |
| --- | ------------------ | ---- | ------ | -------- | ----- | --- | -------------- | --- | --------- |
|     | Abimbolaetal.[123] | 2024 |        |          |       |     |                |     |           |
classification
|     |                   |      | Analyzing | sentiment | with | pre-trained | models | fine-tuned | for |
| --- | ----------------- | ---- | --------- | --------- | ---- | ----------- | ------ | ---------- | --- |
|     | Mujahidetal.[131] | 2023 |           |           |      |             |        |            |     |
specifictasks
MachineTranslation Sennrichetal.[133] 2015 Byte-PairEncodingforhandlingrarewordsintranslationmodels
|     |              |      | Google | Neural | Machine Translation |     | with | deep RNNs | for im- |
| --- | ------------ | ---- | ------ | ------ | ------------------- | --- | ---- | --------- | ------- |
|     | Wuetal.[132] | 2016 |        |        |                     |     |      |           |         |
provedaccuracy
Fullyattention-basedtransformermodelsforsuperiortranslation
|     | Vaswanietal.[104] | 2017 |     |     |     |     |     |     |     |
| --- | ----------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
performance
Yangetal.[135] 2017 HybridmodelintegratingRNNsintothetransformerarchitecture
IncorporatingBERTintotranslationmodelsforenhancedunder-
|     | Songetal.[136] | 2019 |     |     |     |     |     |     |     |
| --- | -------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
standingandfluency
Bilingualattention-basedmachinetranslationmodelcombining
|     | Kangetal.[134] | 2023 |     |     |     |     |     |     |     |
| --- | -------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
RNNwithattention
Zulqarnainetal.[124] 2024 Multi-stagefeatureattentionmechanismmodelusingGRU
7.2. SpeechRecognition
RNNs have also made significant contributions to the field of speech recognition,
leadingtomoreaccurateandefficientsystems. Hintonetal.[137]exploredtheuseofdeep
neuralnetworks,includingRNNs,forspeech-to-textsystems. Theirresearchshowedthat
RNNscouldcapturethetemporaldependenciesinspeechsignals,leadingtosignificant
improvementsintranscriptionaccuracycomparedtopreviousmethods.

Information2024,15,517 19of34
Hannun et al. [138] introduced DeepSpeech, a state-of-the-art speech recognition
systembasedonRNNs. DeepSpeechemployedadeepLSTMnetworktrainedonavast
amountoflabeledspeechdata,therebyimprovingtranscriptionaccuracy. Thissystemwas
designedtohandlenoisyenvironmentsanddiverseaccents,makingitrobustforvarious
real-world applications. Similarly, Amodei et al. [139] presented DeepSpeech2, which
extendedthecapabilitiesoftheoriginalDeepSpeechmodelbyincorporatingbidirectional
RNNsandamoreextensivedataset. DeepSpeech2achievednotableperformanceimprove-
ments,demonstratingthatRNNscouldeffectivelyhandlevariationsinspeechpatterns
andaccents.
Meanwhile,Chiuetal.[140]proposedtheuseofRNN-transducer(RNN-T)modelsfor
end-to-endspeechrecognition.RNN-Tmodelsintegratebothacousticandlanguagemodels
intoasingleRNNframework,allowingformoreefficientandaccuratetranscription. This
integrationreducedthecomplexityandlatencyofreal-timespeechrecognitionsystems,
making them more practical for deployment in real-world applications. Furthermore,
Zhangetal.[141]proposedtheuseofconvolutionalrecurrentneuralnetworks(CRNNs)
for speech recognition. CRNNs combine the strengths of CNNs for feature extraction
andRNNsforsequencemodeling,resultinginahybridarchitecturethatisrobustinboth
accuracyandcomputationalefficiency. Specifically,thismodelwaseffectiveinhandling
longaudiosequencesandvaryingspeechrates.
Recently, Dong et al. [142] introduced the Speech-Transformer, a model that lever-
agestheself-attentionmechanismtoprocessaudiosequencesinparallel,improvingboth
speedandaccuracy. Thismodeldemonstratedthattransformer-basedarchitecturescould
effectivelyhandlethesequentialnatureofspeechdata,providingacompetitivealterna-
tivetotraditionalRNN-basedmodels. BhaskarandThasleema[143]developedaspeech
recognitionmodelusingLSTM.Themodelachievedvisualspeechrecognitionusingfa-
cialexpressions. OtherstudiesthatexploredtheuseofdifferentRNNvariantsinspeech
recognitioninclude[144–147].
Inthefieldofspeechrecognition,LSTMnetworkshavebeenconsistentlyrecognized
asthemosteffectiveRNNvariantduetotheirabilitytocapturelong-rangedependencies
insequentialdata. LSTM,asutilizedinsystemslikeDeepSpeechbyHannunetal.[138],
hasdemonstratedsuperiorperformanceinhandlingthetemporaldependenciesinherent
inspeechsignals. Thiscapabilityisparticularlycrucialformaintainingcontextoverlong
audio sequences, which directly translates to improved transcription accuracy. While
newermodelsliketheSpeech-Transformer[142]leverageattentionmechanismsforfaster
processing,LSTMnetworksremainacornerstoneinspeechrecognitionduetotheirproven
robustnessandabilitytohandlecomplexvariationsinspeechpatterns. Thismakesthem
thepreferredchoiceinscenarioswheremaintainingsequentialorderandcontextiscritical,
despitethegrowingpopularityoftransformer-basedarchitectures.
7.3. TimeSeriesForecasting
RNNshavebeenextensivelyusedintimeseriespredictionduetotheirabilitytomodel
temporaldependenciesandtrendsinsequentialdata. Infinancialforecasting,Fischerand
Krauss[148]conductedacomprehensivestudyusingdeepRNNstopredictstockreturns.
TheirresultsindicatedthatRNNscouldoutperformtraditionalMLmodels,suchassupport
vectormachinesandrandomforests,infinancialforecastingtasks. Thestudydemonstrated
thatdeepRNNscouldlearnintricatepatternsinstockpricemovements,contributingto
betterforecastingaccuracy.
Withtheadvancementofdeeplearningtechniques, Nelsonetal.[149]proposeda
model combining CNNs and RNNs for stock price prediction. The CNN component
extractedlocalfeaturesfromhistoricalpricedata,whiletheRNNcomponentcapturedthe
temporaldependencies. Thishybridmodelshowedsignificantimprovementsinprediction
performance, suggesting that integrating different neural network architectures could
enhancefinancialforecasting. Also,attentionmechanismshavebeenintegratedintoRNNs
toimprovefinancialforecasting.

Information2024,15,517 20of34
Luoetal.[150]usedanattention-basedCNN-BiLSTMmodelthatfocusedonrelevant
time steps in the input sequence, enhancing the model’s ability to capture important
patternsinfinancialdata. Thisapproachallowedformoreaccuratepredictionsofstock
pricesandmarkettrendsbydynamicallyweightingthesignificanceofpastobservations.
Furthermore,Baoetal.[151]employedanoveldeeplearningframeworkcombiningLSTM
withstackedautoencodersforfinancialtimeseriesforecasting.Theirmodelutilizedstacked
autoencoderstoreducethedimensionalityofinputdataandLSTMtomodeltemporal
dependencies. Thismethodimprovedthemodel’sabilitytopredictfuturestockpricesby
effectivelycapturingbothfeaturerepresentationsandsequentialpatterns.
Fengetal.[152]exploredtheuseoftransferlearningforfinancialforecasting. They
proposedamodelthatpre-trainedanRNNonalargecorpusoffinancialdataandfine-
tuneditonspecificstockdatasets. Thisapproachemployedtheknowledgegainedfrom
broader market data to improve predictions on individual stocks, which demonstrates
the potential of transfer learning in financial forecasting. Meanwhile, the application
of reinforcement learning in conjunction with RNNs has gained attention in financial
forecasting. Rundo [153] combined RL with LSTM to develop a trading strategy that
maximizesreturns. Theirmodellearnedoptimaltradingactionsthroughinteractionswith
themarketenvironment,resultinginarobustandadaptivefinancialforecastingsystem.
Beyond financial applications, RNNs have shown effectiveness in other domains,
suchasweatherforecastingandrenewableenergypredictions,wheremodelingtemporal
dependencies is critical for accurate forecasts. In weather forecasting, Devi et al. [154]
developedanRNN-basedmodelspecificallyforweatherprediction,whichdemonstrated
superiorperformanceinbothshort-termandlong-termforecastingcomparedtotraditional
statisticalmethods. Thismodeleffectivelycapturesthesequentialdependenciesinmeteo-
rologicaldata,suchastemperature,humidity,andatmosphericpressure,enablingmore
accurateandreliableforecasts. Additionally, Anshukaetal.[155]showedtheeffective-
nessofusingLSTMnetworksinpredictingextremeweathereventsbylearningcomplex
temporal patterns in historical weather data. Furthermore, Lin et al. [100] proposed a
modelthatintegratestheattentionmechanismwithLSTM,whichfurtherimprovedthe
abilityofRNNs,especiallyastheattentionmechanismensuresthemodelfocusesoncritical
featureswithinthelargedataset,therebyenhancingtheaccuracyofpredictionsincomplex
weatherscenarios.
Inthefieldofrenewableenergy,RNNshavebeenextensivelyappliedtoforecastenergy
generationfromrenewablesourcessuchaswindandsolarpower. Marulandaetal.[156]
utilizedanLSTM-basedmodelforshort-termwindpowerforecasting,whichshowedsignifi-
cantimprovementsinpredictionaccuracybycapturingthenon-linearandtime-dependent
characteristicsofwindspeeddata. Similarly,Chenetal.[157]developedanadvancedDL
approachcombiningabidirectionalGRUwithtemporalconvolutionalnetworks(TCNs)for
energytimeseriesforecasting.Thishybridmodelwasparticularlyeffectiveincapturingboth
short-termfluctuationsandlong-termtrends,leadingtomorereliablepredictions.Moreover,
RNNshavealsobeenusedtoforecastenergydemandinsmartgrids, wheretheirability
tomodeltemporaldependencieshelpsinoptimizingtheintegrationofrenewableenergy
sourcesintothegridandimprovingoverallenergymanagement[158,159].
Furthermore,RNNshavebeenappliedtopredictconsumerdemandpatternsforgoods
andservices,allowingbusinessestooptimizetheirsupplychainmanagementandreduce
costs. Forinstance,Yildizetal.[160]proposedahybridRNNmodelthatcombinesLSTM
with CNN to accurately predict electricity demand in urban areas, showing significant
improvementsovertraditionalforecastingtechniques.
Meanwhile, ESNshavealsoshownpromiseinweatherforecastingandrenewable
energypredictionsduetotheirabilitytohandlenon-linearandchaotictimeseriesdata.
For instance, Anshuka et al. [155] applied ESNs to model and predict extreme weather
events,demonstratingthenetwork’sabilitytocapturecomplextemporalpatternsfrom
historicalweatherdata. Similarly,Marulandaetal.[156]usedanESN-basedapproachfor
short-termwindpowerforecasting,whicheffectivelycapturedthenon-lineardynamicsof

Information2024,15,517
21of34
windspeedandimprovedpredictionaccuracycomparedtoconventionalmethods. These
studieshighlighttheversatilityandrobustnessofESNsinhandlingdiversetimeseries
forecastingtasksacrossdifferentdomains.
Additionally, Gao et al. [90] proposed a dynamic ensemble deep ESN specifically
designedforwaveheightforecasting. Thismodeladjustsreservoirweightsdynamically,
allowingittomodelthecomplexandnon-linearpatternsoftenfoundintimeseriesmore
effectively than traditional methods. Additionally, Bhambuet al. [161] introduced a re-
currentensembledeeprandomvectorfunctionallinkneuralnetworkforfinancialtime
series forecasting. This model integrates the strengths of both ESNs and recurrent net-
works,providingsuperiorperformanceinpredictingfinancialmarketvolatilityandtrends.
Table5providesasummaryoftheRNNapplicationsinbothspeechrecognitionandtime
seriesforecasting.
AmongthevariousRNNarchitectures,LSTMnetworksstandoutasthemosteffectivefor
timeseriesforecasting,especiallyinfinancialapplications[162].LSTM’sgatingmechanisms
allow it to maintain and utilize long-term dependencies, which are crucial for accurately
predictingfuturetrendsbasedonhistoricaldata. TheabilityofLSTMtocapturecomplex
temporalpatternsmakesitparticularlywell-suitedforfinancialmarkets,wherelong-range
dependenciesandintricatepatternsindataarecommon.Meanwhile,whenLSTMiscombined
with other techniques, such as CNNs for feature extraction or attention mechanisms for
focusingoncriticaltimesteps,themodels’forecastingperformanceimprovesevenfurther.
This combination of adaptability, robustness, and precision demonstrates why LSTM is
frequentlyconsideredthebestRNNvariantfortimeseries-forecastingtasks.
Table5.SummaryofRNNsinspeechrecognitionandtimeseriesforecasting.
| ApplicationDomain  | Reference        | Year MethodsandApplication |                     |       |                    |
| ------------------ | ---------------- | -------------------------- | ------------------- | ----- | ------------------ |
|                    |                  | Deep neural                | networks, including | RNNs, | for speech-to-text |
| Speech recognition | Hintonetal.[137] | 2012                       |                     |       |                    |
systems
Hannunetal.[138] 2014 DeepSpeech:LSTM-basedspeechrecognitionsystem
DeepSpeech2:EnhancedLSTM-basedspeechrecognitionwith
|     | Amodeietal.[139] | 2016 |     |     |     |
| --- | ---------------- | ---- | --- | --- | --- |
bidirectionalRNNs
Zhangetal.[141] 2017 ConvolutionalRNNforrobustspeechrecognition
Chiuetal.[140] 2018 RNN-transducermodelsforend-to-endspeechrecognition
|     |                | Speech-Transformer: | Leveragingself-attentionforbetterpro- |     |     |
| --- | -------------- | ------------------- | ------------------------------------- | --- | --- |
|     | Dongetal.[142] | 2018                |                                       |     |     |
cessingofaudiosequences
BhaskarandThasleema[143] 2023 LSTMforvisualspeechrecognitionusingfacialexpressions
Daouadetal.[144] 2023 VariousRNNvariantsforautomaticspeechrecognition
|     | Nasretal.[146] | 2023 End-to-endspeechrecognitionusingRNNs |     |     |     |
| --- | -------------- | ----------------------------------------- | --- | --- | --- |
Kumaretal.[147] 2023 PerformanceevaluationofRNNsinspeechrecognitiontasks
ComprehensivestudyofdifferentRNNmodelsforspeechrecog-
|     | Dhanjaletal.[145] | 2024 |     |     |     |
| --- | ----------------- | ---- | --- | --- | --- |
nition
Timeseriesforecasting Nelsonetal.[149] 2017 HybridCNN-RNNmodelforstockpriceprediction
CombiningLSTMwithstackedautoencodersforfinancialtime
|     | Baoetal.[151] | 2017 |     |     |     |
| --- | ------------- | ---- | --- | --- | --- |
seriesforecasting
DeepRNNsforpredictingstockreturns,outperformingtradi-
|     | FischerandKrauss[148] | 2018 |     |     |     |
| --- | --------------------- | ---- | --- | --- | --- |
tionalMLmodels
|     | Fengetal.[152] | 2019 TransferlearningwithRNNsforstockprediction |     |     |     |
| --- | -------------- | ----------------------------------------------- | --- | --- | --- |
CombiningreinforcementlearningwithLSTMfortradingstrat-
|     | Rundo[153] | 2019 |     |     |     |
| --- | ---------- | ---- | --- | --- | --- |
egydevelopment
|     |                | RNN-based | model for weather | prediction | and capturing se- |
| --- | -------------- | --------- | ----------------- | ---------- | ----------------- |
|     | Devietal.[154] | 2024      |                   |            |                   |
quentialdependenciesinmeteorologicaldata
LSTMnetworksforpredictingextremeweathereventsbylearn-
|     | Anshukaetal.[155] | 2022 |     |     |     |
| --- | ----------------- | ---- | --- | --- | --- |
ingcomplextemporalpatterns

Information2024,15,517 22of34
Table5.Cont.
ApplicationDomain Reference Year MethodsandApplication
IntegratingattentionmechanismswithLSTMforenhancedweatherfore-
Linetal.[100] 2022
castingaccuracy
LSTMmodelforshort-termwindpowerforecastingandimprovingpre-
Marulandaetal.[156] 2023
dictionaccuracy
Chenetal.[157] 2024 BidirectionalGRUwithTCNsforenergytimeseriesforecasting
RNNs for forecasting energy demand in smart grids and optimizing
Hasanatetal.[158] 2024
renewableenergyintegration
Asirietal.[159] 2024 Short-termrenewableenergypredictionsusingRNN-basedmodels
HybridmodelofLSTMwithCNNforaccurateelectricitydemandpredic-
Yildizetal.[160] 2024
tion
Luoetal.[150] 2024 Attention-basedCNN-BiLSTMmodelforimprovedfinancialforecasting
Gaoetal.[90] 2023 DynamicensembledeepESNforwaveheightforecasting
Recurrentensembledeeprandomvectorfunctionallinkneuralnetwork
Bhambuetal.[161] 2024
forfinancialtimeseriesforecasting
7.4. SignalProcessing
RNNs,particularlyESNs,haveseensignificantapplicationsinvarioussignal-processing
tasksduetotheirefficienttrainingandrobustperformanceinhandlingtime-dependent
data. Onekeyareaofapplicationisphysiologicalsignalprocessing. Mastoietal.[163]de-
veloped an ESN-based approach for the real-time monitoring and prediction of heart
rate variability. Their approach outperformed traditional methods in terms of accu-
racy and computational efficiency, demonstrating ESNs’ potential in real-time health
monitoringsystems.
ESNshavealsobeenextensivelyusedinspeech-processingtasks. Valinetal.[164]
proposedanESNarchitecturespecificallydesignedforspeechsignalenhancement. This
model demonstrated improved noise reduction and speech intelligibility in noisy envi-
ronments,whichiscriticalforapplicationssuchashearingaidsandspeechrecognition
systems. Themodel’sabilitytohandletemporaldependenciesinspeechsignalsmadeit
particularlyeffectiveinenhancingaudioqualityunderchallengingconditions.
Additionally, ESNs have been applied in the preprocessing and analysis of non-
stationary and noisy time series data. Gao et al. [91] integrated the empirical wavelet
transform(EWT)withESNstoenhanceperformanceintimeseriesforecasting. Thishybrid
approachdemonstratedthatcombiningtheEWT’sabilitytodecomposecomplexsignals
withtherobustmodelingcapabilitiesofESNsleadstosuperiorperformance,particularly
in scenarios where data is noisy or exhibits non-stationary behavior. This integration
demonstrates the adaptability of ESNs to a wide range of signal processing challenges,
reinforcingtheirutilityindomainsrequiringaccurateandefficienttimeseriesanalysis.
7.5. Bioinformatics
In bioinformatics, RNNs have been used to analyze biological sequences such as
DNA,RNA,andproteins. Lietal.[165]employedRNNsforgenepredictionandprotein
structureprediction,demonstratingtheabilityofRNNstocapturedependencieswithin
biologicalsequencesandprovidinginsightsintogeneticinformationandbiologicalpro-
cesses. Zhang et al. [166] used bidirectional LSTM in predicting DNA-binding protein
sequences. Theirmodel,calledDeepSite,leveragedthesequentialnatureofbiologicaldata,
achievinghigheraccuracyinidentifyingbindingsitescomparedtotraditionalmethods.
ThisapplicationdemonstratedthepotentialofRNNstoenhanceourunderstandingof
protein-DNAinteractions.
Inthefieldofproteomics,RNNshavebeenusedforproteinstructurepredictionand
functionannotation. Xuetal.[167]developedanRNN-basedmodeltopredictprotein
secondarystructures,showingthatRNNscouldeffectivelycapturesthesequentialdepen-

Information2024,15,517 23of34
denciesinaminoacidsequences. Thisapplicationprovidedsignificantadvancementsin
proteinstructureprediction,whichisessentialfordrugdiscoveryanddiseaseresearch.
Morerecently,researchershaveexploredtheintegrationofRNNswithotherneural
network architectures for bioinformatics applications. For example, Yadav et al. [168]
combinedBiLSTMwithCNNstoanalyzeproteinsequences. Theirmodelextractedlocal
featuresandcapturedlong-rangedependencieswithBiLSTM,resultinginimprovedper-
formanceinproteinclassificationtasks. Additionally,theuseofensembledeeplearning
hasenhancedtheperformanceofRNNsinbioinformatics. Aybeyetal. [169]introducedan
ensemblemodelforpredictingprotein–proteininteractionsusingRNNs,GRUs,andCNNs.
Themodelimprovestheaccuracyofinteractionpredictions. Thisapproachhighlighted
thepotentialofensembledeeplearningtoenhancetheinterpretabilityandperformanceof
RNNsinbioinformatics.
Inbioinformatics,RNNs,specificallyLSTMnetworksandGRUs,haveestablished
themselvesasthebestmodelsforanalyzingbiologicalsequencesduetotheirabilityto
processlongsequencesandmaintaininformationoverlongdistances,crucialforunder-
standingcomplexbiologicalstructuresandfunctions. BidirectionalLSTM,usedbyZhang
et al. [166] in predicting DNA-binding protein sequences, is particularly effective, as it
processessequencesinbothforwardandbackwarddirections,providingabettercontext
and significantly improving prediction accuracy over unidirectional approaches. This
capabilitymakesitpreferablefortaskswhereunderstandingthefullcontextofasequence
isessential, suchasgeneprediction, proteinfolding, andothercomplexbioinformatics
applicationsinvolvingsequentialdata.
7.6. AutonomousVehicles
RNNsplayanimportantroleinautonomousvehiclesbyprocessingsequentialdata
fromsensorstomakedrivingdecisions. Lietal.[170]usedRNNsforpathplanning,object
detection,andtrajectoryprediction,enablingautonomousvehiclestonavigatecomplex
environmentsandmakereal-timedecisions. Followingthisfoundationalwork,researchers
have continued to explore and enhance the use of RNNs in autonomous driving. For
instance,Leeetal.[171]developedadeeplearningframeworkthatintegratesLSTMwith
CNNforend-to-enddriving. TheirmodelutilizedCNNtoextractspatialfeaturesfrom
cameraimagesandLSTMtocapturetemporaldependencies,whichimprovedtheaccuracy
androbustnessofdrivingdecisionsindynamicenvironments.
Codevillaetal.[172]introducedaconditionalimitationlearningapproachthatcom-
binedRNNswithimitationlearningforautonomousdriving. Themodellearnedfrom
humandrivingdemonstrationsandusedRNNstopredictfutureactionsbasedonpast
observations. Thisapproachallowedthevehicletoadapttovariousdrivingconditionsand
makesaferdecisionsincomplexscenarios. Additionally,researchershaveexploredtheuse
ofLSTMfortrajectorypredictioninautonomousvehicles. AltchéanddeLaFortelle[173]
proposedanLSTM-basedmodelthatpredictsthefuturetrajectoriesofsurroundingvehi-
cles. Thismodelleveragesthesequentialnatureoftrafficdatatoanticipatethemovements
ofotherroadusers,enablingmoreaccurateandproactivepathplanningforautonomous
vehicles. Meanwhile, attention mechanisms have been integrated into RNN models to
enhance their performance in autonomous driving tasks. Li et al. [174] introduced an
attention-based LSTM model that focuses on relevant parts of the data, improving the
detectionandtrackingofvideoobjects.
ResearchershavealsoexploredtheuseofRNNsforbehaviorpredictioninautonomous
driving. Lietal.[175]proposedamodelthatcombinesRNNswithCNNtopredictthe
intentionsofotherdrivers. Theirapproachusedsequentialdatatolearnthebehavioral
patternsofsurroundingvehicles,enablingtheautonomousvehicletoanticipatepotential
hazardsandrespondaccordingly. Inaddition, researchershaveinvestigatedtheuseof
RNNsfordecision-makinginautonomousvehicles. LiuandDiao[176]introducedadeep
reinforcementlearningframeworkthatincorporatesGRUfordecision-makingincomplex

Information2024,15,517 24of34
trafficscenarios. TheirmodelusedRNNstoprocesssequentialobservationsandmake
real-timedecisions,achievingstate-of-the-artperformanceinvariousdrivingtasks.
Furthermore,theintegrationofLSTMwithCNNsseemstorepresentthebestapproach
inautonomousvehicleapplications,asdemonstratedbyLeeetal.[171]. Thiscombination
leveragesLSTM’sabilitytounderstandtemporaldynamicsandCNNs’strengthinspatial
feature extraction, making it robust for real-time applications like driving, where both
spatialandtemporalunderstandingsarecrucialfordecision-making. Thehybridnatureof
thesemodelsallowsforabetterunderstandingandprocessingofthevastamountsofdata
fromvarioussensors,ensuringbetterperformanceinnavigationandreal-timedecision
makingindynamicenvironments.
7.7. AnomalyDetection
RNNs are used in anomaly detection across different fields, such as cybersecurity,
industrialmonitoring,andhealthcare. Altindaletal.[177]demonstratedtheuseofLSTM
networksforanomalydetectionintimeseriesdata,showingthatRNNscouldeffectively
model normal behavior patterns and identify deviations indicative of anomalies. Sim-
ilarly, Matar et al. [178] proposed a model for anomaly detection in multivariate time
series. TheirmodelutilizedBiLSTMtolearntemporaldependenciesandtodetectdevia-
tionsfromnormalpatterns. Thisapproachwaseffectiveinindustrialapplicationswhere
monitoring the health of machinery and predicting failures is critical. In cybersecurity,
Kumaresanetal.[179]appliedRNNstodetectanomaliesinnetworktraffic. Theirmodel
analyzedsequentialdatatoidentifyunusualpatternsthatcouldindicatesecuritybreaches
ormaliciousactivities. TheuseofRNNsallowedforreal-timedetectionandresponseto
potentialthreats,enhancingthesecurityofnetworksystems.
Furthermore,Lietal.[180]exploredtheapplicationofRNNsforanomalydetectionin
manufacturingprocesses. TheydevelopedamodelcombiningRNNswithtransferlearning
tocapturebothtemporaldependenciesandfeaturerepresentations. Thismethodimproved
thedetectionofanomaliesincomplexindustrialprocesses,contributingtotheoptimization
of production efficiency and quality control. In healthcare, researchers have utilized
RNNs for detecting anomalies in physiological signals. For instance, Mini et al. [181]
employedRNNstodetectabnormalpatternsinelectrocardiogram(ECG)signals. Their
modelaccuratelyidentifieddeviationsindicativeofcardiacarrhythmias,demonstrating
thepotentialofRNNstoassistintheearlydiagnosisandmonitoringofheartconditions.
Moreover,advancesinunsupervisedlearninghavefurtherenhancedthecapabilities
ofRNNsinanomalydetection. ZhouandPaffenroth[182]introducedarobustdeepau-
toencodermodelthatleveragesRNNsforunsupervisedanomalydetection. Thisapproach
effectivelycapturedtheunderlyingstructureofthedata,identifyinganomalieswithout
requiringlabeledtrainingdata. Renetal.[183]proposedanattention-basedRNNmodel
thatfocusesonrelevanttimestepsinthedata,improvingtheaccuracyandinterpretabil-
ity of anomaly detection. This approach allowed for the more precise identification of
anomaliesbydynamicallyweightingtheimportanceofdifferentpartsofthesequence. Ad-
ditionally,hybridmodelscombiningRNNswithotherneuralnetworkarchitectureshave
alsobeenemployedinanomalydetection. Muniretal.[184]developedahybridmodel
thatintegratesCNNsandRNNstodetectanomaliesinmultivariatetimeseriesdata. The
CNNcomponentextractedlocalfeatures,whiletheRNNcomponentcapturedtemporal
dependencies,resultinginimprovedperformanceinvariousanomalydetectiontasks.
The BiLSTM model stands out as the best RNN architecture in anomaly detection,
especiallyinmultivariatetimeseriesdata,whereunderstandingtheinfluenceofpastand
futureinputcontextsiscrucial. Mataretal.[178]demonstratedthatBiLSTMeffectively
capturetemporaldependenciesinbothdirections,whichiscriticalinanomalydetection
scenarios where anomalies may be contextually linked to events in both the past and
the future. This bidirectional processing capability allows for more robust detection of
anomaliesacrossvariousapplications,fromindustrialmonitoringtocybersecurity,making
itthemostsuitableRNNmodelforthesetasks.

Information2024,15,517
25of34
AsummaryofRNNapplicationsinbioinformatics,autonomousvehicles,andanomaly
detectionisshowninTable6.
Table6.SummaryofRNNsinsignalprocessing,bioinformatics,autonomousvehicles,andanomaly
detection.
| ApplicationDomain | Reference | Year MethodsandApplication |     |     |     |     |
| ----------------- | --------- | -------------------------- | --- | --- | --- | --- |
Signalprocessing Mastoietal.[163] 2019 ESNsforreal-timeheartratevariabilitymonitoring
Valinetal.[164] 2021 ESNsforspeechsignalenhancementinnoisyenvironments
Gaoetal.[91] 2021 EWTintegratedwithESNsforenhancedtimeseriesforecasting
Bioinformatics Lietal.[165] 2019 RNNsforgenepredictionandprotein-structureprediction
|     |                 | Bidirectional | LSTM | for predicting | DNA-binding | protein |
| --- | --------------- | ------------- | ---- | -------------- | ----------- | ------- |
|     | Zhangetal.[166] | 2020          |      |                |             |         |
sequences
Xuetal.[167] 2021 RNN-basedmodelforpredictingproteinsecondarystructures
Yadavetal.[168] 2019 CombiningBiLSTMwithCNNsforproteinsequenceanalysis
Aybeyetal.[169] 2023 Ensemblemodelforpredictingprotein–proteininteractions
Autonomousvehicles AltchéanddeLaFortelle[173] 2017 LSTMforpredictingthefuturetrajectoriesofvehicles
Codevillaetal.[172] 2018 RNNswithimitationlearningforautonomousdriving
|     | Lietal.[170]  | 2020 RNNsforpathplanningandobjectdetection |           |         |            |            |
| --- | ------------- | ------------------------------------------ | --------- | ------- | ---------- | ---------- |
|     |               | Integrating                                | LSTM with | CNN for | end-to-end | autonomous |
|     | Leeetal.[171] | 2020                                       |           |         |            |            |
driving
|     | Lietal.[174] | 2024 Attention-basedLSTMforvideoobjecttracking |     |     |     |     |
| --- | ------------ | ---------------------------------------------- | --- | --- | --- | --- |
LiuandDiao[176] 2024 GRUwithdeepreinforcementlearningfordecision-making
|                  |                        | RNNs | in unsupervised | anomaly | detection | with deep |
| ---------------- | ---------------------- | ---- | --------------- | ------- | --------- | --------- |
| Anomalydetection | ZhouandPaffenroth[182] | 2017 |                 |         |           |           |
autoencoders
Muniretal.[184] 2018 HybridCNN-RNNmodelforanomalydetectionintimeseries
Renetal.[183] 2019 Attention-basedRNNmodelforanomalydetection
|     |              | RNNs | with Transfer | learning | for anomaly | detection in |
| --- | ------------ | ---- | ------------- | -------- | ----------- | ------------ |
|     | Lietal.[180] | 2023 |               |          |             |              |
manufacturing
|     | Minietal.[181] | 2023 RNNsfordetectinganomaliesinECGsignals |     |     |     |     |
| --- | -------------- | ------------------------------------------ | --- | --- | --- | --- |
Mataretal.[178] 2023 BiLSTMforanomalydetectioninmultivariatetimeseries
Kumaresanetal.[179] 2024 RNNsfordetectingnetworktrafficanomalies
Altindaletal.[177] 2024 LSTMforanomalydetectionintimeseriesdata
8. ChallengesandFutureResearchDirections
Despitesignificantadvancements,severalunresolvedproblemsareencounteredwhen
applyingRNNs. Addressingtheseissuesiscrucialforfurtherimprovingtheperformance
andusageofRNNs.
8.1. ScalabilityandEfficiency
TrainingRNNsonlargedatasetswithlongsequencesremainscomputationallyinten-
siveandtime-consuming[185–187]. Althoughtechniqueslikegradientcheckpointingand
hardwareacceleratorshaveprovidedimprovements,thesequentialnatureofRNNscontin-
uestolimittheirscalabilitycomparedtoparallelizablearchitecturesliketransformers[188].
Futureresearchcouldfocusondevelopingmoreefficienttrainingalgorithmsandexploring
asynchronousandparalleltrainingmethodstodistributethecomputationalloadmore
effectively. Additionally,hybridarchitecturesthatcombineRNNswithothermodels,such
asintegratingRNNswithattentionmechanismsorconvolutionallayers,couldprovidenew
solutions. Thesehybridmodelshavethepotentialtoreducetrainingtimesandimprove
scalabilitywhilemaintainingtheperformanceadvantagesofRNNs[104].
8.2. InterpretabilityandExplainability
RNNsareoftenperceivedas“black-box”modelsduetotheircomplexinternaldy-
namics,makingitchallengingtointerprettheirdecisions[189,190]. Althoughattention
mechanismsandposthocexplanationtechniqueslikeLocalInterpretableModel-Agnostic
Explanations(LIMEs)andShapleyAddictiveExplanations(SHAPs)havebeenproposed

Information2024,15,517 26of34
toimproveinterpretability,thesemethodscanstillbeimprovedtofurtherprovidemore
comprehensiveexplanations[191]. Therefore,futureresearchshouldaimtodevelopinher-
entlyinterpretableRNNarchitecturesandhierarchicalmodelsthatofferstructuredinsights
intothemodel’sdecision-makingprocess. Additionally,integratingdomainknowledge
intoRNNmodelscanhelpaligntheirbehaviorwithhumanreasoning,enhancingboth
interpretabilityandperformanceinspecializedapplications.
8.3. BiasandFairness
RNNscaninadvertentlylearnandpropagatebiasespresentinthetrainingdata,lead-
ingtounfairpredictions. Whilevariousbiasdetectionandmitigationtechniqueshavebeen
developed,suchasfairness-awarealgorithmsandadversarialtraining,thesemethodsneed
furtherrefinementtoensurefairnessacrossdiverseapplicationsanddatasets[192–194].
Research should continue to focus on developing robust bias detection techniques and
fairtrainingalgorithmsthatexplicitlyincorporatefairnessconstraints. Additionally,trans-
parencyandaccountabilityframeworks,includingexternalauditsandimpactassessments,
areessentialforensuringthatRNNsaredevelopedanddeployedresponsibly.
8.4. DataDependencyandQuality
RNNs require large amounts of high-quality, labeled sequential data for effective
training[195]. Inmanyreal-worldscenarios,suchdatamaybescarce,noisy,orincomplete.
Althoughdataaugmentation,transferlearning,andsemi-supervisedlearningtechniques
have been explored, these methods require further refinement to handle diverse data
challengesmoreeffectively. Futureresearchshouldfocusonenhancingthesetechniquesto
improvetherobustnessofRNNswhentrainedonlimitedorimperfectdata. Additionally,
developing new methods for utilizing unlabeled data and integrating domain-specific
knowledgecanfurtherimprovetheperformanceofRNNsindata-scarceenvironments.
8.5. OverfittingandGeneralization
RNNs,particularlydeeparchitectures,arepronetooverfitting,especiallywhentrained
onsmalldatasets[196]. EnsuringthatRNNmodelsgeneralizewelltounseendatawithout
overfittingremainsasignificantchallenge. Whileregularizationtechniqueslikedropout
andL2regularizationarecommonlyused,morerobustmethodsforimprovinggeneral-
izationareneeded. Futureresearchcanexploreadvancedregularizationtechniques,such
asadversarialtrainingandensemblemethods,toenhancethegeneralizationcapabilities
ofRNNs. Additionally,applyingdataaugmentationandtransferlearningcanhelpRNN
modelslearnmorerobustfeatures,improvingtheirabilitytogeneralizetonewdata.
9. Conclusions
RNNshavedemonstratedaremarkableabilitytomodelsequentialdata,makingthem
indispensableinnumerousMLapplicationssuchasnaturallanguageprocessing,speech
recognition,timeseriesprediction,bioinformatics,andautonomoussystems. Thispaper
providedacomprehensiveoverviewofRNNsandtheirvariants,coveringfundamental
architectureslikebasicRNNs,LSTMnetworks,andGRUs,aswellasadvancedvariants,
including bidirectional RNNs, peephole LSTM, ESNs, and IndRNNs. This study has
provided a detailed and comprehensive review of RNNs, as well as their architectures,
applications,andchallenges. Thepaperwillbeavaluableresourceforresearchersand
practitionersinthefieldofmachinelearning,helpingtoguidefuturedevelopmentsand
applicationsofRNNs.
AuthorContributions:Conceptualization,I.D.M.,T.G.S.andG.O.;methodology,I.D.M.;validation,
I.D.M.,T.G.S.andG.O.;investigation,I.D.M.,T.G.S.andG.O.;resources,T.G.S.;writing—original
draftpreparation,I.D.M.andG.O.;writing—reviewandediting,I.D.M.,T.G.S.andG.O.;visual-
ization,I.D.M.;supervision,T.G.S.Allauthorshavereadandagreedtothepublishedversionof
themanuscript.

Information2024,15,517 27of34
Funding:Thisresearchreceivednoexternalfunding.
InstitutionalReviewBoardStatement:Notapplicable.
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement:Notapplicable.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.
Abbreviations
Thefollowingabbreviationsareusedinthismanuscript:
AI Artificialintelligence
ANN Artificialneuralnetwork
BiLSTM Bidirectionallongshort-termmemory
CNN Convolutionalneuralnetwork
DL Deeplearning
GRU Gatedrecurrentunit
LSTM Longshort-termmemory
ML Machinelearning
NAS Neuralarchitecturesearch
NLP Naturallanguageprocessing
RNN Recurrentneuralnetwork
RL Reinforcementlearning
SHAPs ShapleyAdditiveExplanations
TPU Tensorprocessingunit
VAE Variationalautoencoder
References
1. O’Halloran,T.;Obaido,G.;Otegbade,B.;Mienye,I.D. AdeeplearningapproachforMaizeLethalNecrosisandMaizeStreak
Virusdiseasedetection. Mach.Learn.Appl.2024,16,100556.[CrossRef]
2. Peng,Y.;He,L.;Hu,D.;Liu,Y.;Yang,L.;Shang,S. DecouplingDeepLearningforEnhancedImageRecognitionInterpretability.
ACMTrans.Multimed.Comput.Commun.Appl.2024.[CrossRef]
3. Khan,W.;Daud,A.;Khan,K.;Muhammad,S.;Haq,R. Exploringthefrontiersofdeeplearningandnaturallanguageprocessing:
Acomprehensiveoverviewofkeychallengesandemergingtrends. Nat.Lang.Process.J.2023,4,100026.[CrossRef]
4. Obaido,G.;Achilonu,O.;Ogbuokiri,B.;Amadi,C.S.;Habeebullahi,L.;Ohalloran,T.;Chukwu,C.W.;Mienye,E.;Aliyu,M.;
Fasawe,O.;etal. AnImprovedFrameworkforDetectingThyroidDiseaseUsingFilter-BasedFeatureSelectionandStacking
Ensemble. IEEEAccess2024,12,89098–89112.[CrossRef]
5. Mienye,I.D.;Obaido,G.;Aruleba,K.;Dada,O.A. EnhancedPredictionofChronicKidneyDiseaseusingFeatureSelectionand
BoostedClassifiers. InProceedingsoftheInternationalConferenceonIntelligentSystemsDesignandApplications,Virtual,
13–15December2021;pp.527–537.
6. Al-Jumaili,A.H.A.;Muniyandi,R.C.;Hasan,M.K.;Paw,J.K.S.;Singh,M.J. Bigdataanalyticsusingcloudcomputingbased
frameworksforpowermanagementsystems:Status,constraints,andfuturerecommendations. Sensors2023,23,2952.[CrossRef]
7. Gill,S.S.;Wu,H.;Patros,P.;Ottaviani,C.;Arora,P.;Pujol,V.C.;Haunschild,D.;Parlikad,A.K.;Cetinkaya,O.;Lutfiyya,H.;etal.
Moderncomputing:Visionandchallenges. Telemat.Inform.Rep.2024,13,100116.[CrossRef]
8. Mienye,I.D.;Jere,N. ASurveyofDecisionTrees:Concepts,Algorithms,andApplications. IEEEAccess2024,12,86716–86727.
[CrossRef]
9. Aruleba,R.T.;Adekiya,T.A.;Ayawei,N.;Obaido,G.;Aruleba,K.;Mienye,I.D.;Aruleba,I.;Ogbuokiri,B. COVID-19diagnosis:A
reviewofrapidantigen,RT-PCRandartificialintelligencemethods. Bioengineering2022,9,153.[CrossRef]
10. Alhajeri,M.S.;Ren,Y.M.;Ou,F.;Abdullah,F.;Christofides,P.D. Modelpredictivecontrolofnonlinearprocessesusingtransfer
learning-basedrecurrentneuralnetworks. Chem.Eng.Res.Des.2024,205,1–12.[CrossRef]
11. Shahinzadeh,H.;Mahmoudi,A.;Asilian,A.;Sadrarhami,H.;Hemmati,M.;Saberi,Y. DeepLearning:AOverviewofTheoryand
Architectures. InProceedingsofthe202420thCSIInternationalSymposiumonArtificialIntelligenceandSignalProcessing
(AISP),Babol,Iran,21–22February2024;pp.1–11.
12. Baruah,R.D.;Organero,M.M. ExplicitContextIntegratedRecurrentNeuralNetworkforapplicationsinsmartenvironments.
ExpertSyst.Appl.2024,255,124752.[CrossRef]
13. Werbos,P. Backpropagationthroughtime:Whatitdoesandhowtodoit. Proc.IEEE1990,78,1550–1560. [CrossRef]
14. Lalapura,V.S.;Amudha,J.;Satheesh,H.S. Recurrentneuralnetworksforedgeintelligence:Asurvey. ACMComput.Surv.(CSUR)
2021,54,1–38.[CrossRef]

Information2024,15,517 28of34
15. Hochreiter,S.;Schmidhuber,J. Longshort-termmemory. NeuralComput.1997,9,1735–1780.[CrossRef][PubMed]
16. Cho,K.;VanMerriënboer,B.;Gulcehre,C.;Bahdanau,D.;Bougares,F.;Schwenk,H.;Bengio,Y. Learningphraserepresentations
usingRNNencoder-decoderforstatisticalmachinetranslation. arXiv2014,arXiv:1406.1078.
17. Liu,F.;Li,J.;Wang,L. PI-LSTM:Physics-informedlongshort-termmemorynetworkforstructuralresponsemodeling. Eng.
Struct.2023,292,116500.[CrossRef]
18. Ni,Q.;Ji,J.;Feng,K.;Zhang,Y.;Lin,D.;Zheng,J.Data-drivenbearinghealthmanagementusinganovelmulti-scalefusedfeature
andgatedrecurrentunit. Reliab.Eng.Syst.Saf.2024,242,109753.[CrossRef]
19. Niu,Z.;Zhong,G.;Yue,G.;Wang,L.N.;Yu,H.;Ling,X.;Dong,J. Recurrentattentionunit: Anewgatedrecurrentunitfor
long-termmemoryofimportantpartsinsequentialdata. Neurocomputing2023,517,1–9.[CrossRef]
20. Lipton, Z.C.; Berkowitz, J.; Elkan, C. A critical review of recurrent neural networks for sequence learning. arXiv 2015,
arXiv:1506.00019.
21. Yu,Y.;Si,X.;Hu,C.;Zhang,J. Areviewofrecurrentneuralnetworks:LSTMcellsandnetworkarchitectures. NeuralComput.
2019,31,1235–1270.[CrossRef]
22. Tarwani,K.M.;Edem,S. Surveyonrecurrentneuralnetworkinnaturallanguageprocessing. Int.J.Eng.TrendsTechnol.2017,
48,301–304.[CrossRef]
23. Tsoi,A.C.;Back,A.D. Locallyrecurrentgloballyfeedforwardnetworks:Acriticalreviewofarchitectures. IEEETrans.Neural
Netw.1994,5,229–239.[CrossRef][PubMed]
24. Mastorocostas,P.A.;Theocharis,J.B. Astablelearningalgorithmforblock-diagonalrecurrentneuralnetworks:Applicationtothe
analysisoflungsounds. IEEETrans.Syst.Man.Cybern.PartB(Cybern.)2006,36,242–254.[CrossRef][PubMed]
25. Dutta,K.K.;Poornima,S.;Sharma,R.;Nair,D.;Ploeger,P.G. ApplicationsofRecurrentNeuralNetwork:OverviewandCase
Studies.InRecurrentNeuralNetworks;CRCPress:BocaRaton,FL,USA,2022;pp.23–41.
26. Quradaa,F.H.;Shahzad,S.;Almoqbily,R.S. Asystematicliteraturereviewontheapplicationsofrecurrentneuralnetworksin
codecloneresearch. PLoSONE2024,19,e0296858.[CrossRef]
27. Goodfellow,I.;Bengio,Y.;Courville,A. DeepLearning;MITPress:Cambridge,MA,USA,2016.
28. Greff,K.;Srivastava,R.K.;Koutník,J.;Steunebrink,B.R.;Schmidhuber,J. LSTM:Asearchspaceodyssey. IEEETrans.NeuralNetw.
Learn.Syst.2016,28,2222–2232.[CrossRef][PubMed]
29. Al-Selwi, S.M.; Hassan, M.F.; Abdulkadir, S.J.; Muneer, A.; Sumiea, E.H.; Alqushaibi, A.; Ragab, M.G. RNN-LSTM: From
applicationstomodelingtechniquesandbeyond—Systematicreview. J.KingSaud-Univ.-Comput. Inf. Sci. 2024,36,102068.
[CrossRef]
30. Zaremba,W.;Sutskever,I.;Vinyals,O. Recurrentneuralnetworkregularization. arXiv2014,arXiv:1409.2329.
31. Bai,S.;Kolter,J.Z.;Koltun,V. Anempiricalevaluationofgenericconvolutionalandrecurrentnetworksforsequencemodeling.
arXiv2018,arXiv:1803.01271.
32. Che,Z.;Purushotham,S.;Cho,K.;Sontag,D.;Liu,Y. Recurrentneuralnetworksformultivariatetimeserieswithmissingvalues.
Sci.Rep.2018,8,6085.[CrossRef]
33. Chung,J.;Gulcehre,C.;Cho,K.;Bengio,Y. Empiricalevaluationofgatedrecurrentneuralnetworksonsequencemodeling. arXiv
2014,arXiv:1412.3555.
34. Badawy,M.;Ramadan,N.;Hefny,H.A. Healthcarepredictiveanalyticsusingmachinelearninganddeeplearningtechniques:A
survey. J.Electr.Syst.Inf.Technol.2023,10,40.[CrossRef]
35. Ismaeel,A.G.;Janardhanan,K.;Sankar,M.;Natarajan,Y.;Mahmood,S.N.;Alani,S.;Shather,A.H. Trafficpatternclassificationin
smartcitiesusingdeeprecurrentneuralnetwork. Sustainability2023,15,14522.[CrossRef]
36. Mers,M.;Yang,Z.;Hsieh,Y.A.;Tsai,Y. Recurrentneuralnetworksforpavementperformanceforecasting:Reviewandmodel
performancecomparison. Transp.Res.Rec.2023,2677,610–624.[CrossRef]
37. Chen,Y.;Cheng,Q.;Cheng,Y.;Yang,H.;Yu,H. Applicationsofrecurrentneuralnetworksinenvironmentalfactorforecasting:A
review. NeuralComput.2018,30,2855–2881.[CrossRef][PubMed]
38. Linardos,V.;Drakaki,M.;Tzionas,P.;Karnavas,Y.L.Machinelearningindisastermanagement:Recentdevelopmentsinmethods
andapplications. Mach.Learn.Knowl.Extr.2022,4,446–473.[CrossRef]
39. Zhang,J.;Liu,H.;Chang,Q.;Wang,L.;Gao,R.X. Recurrentneuralnetworkformotiontrajectorypredictioninhuman-robot
collaborativeassembly. CIRPAnn.2020,69,9–12.[CrossRef]
40. Tsantekidis,A.;Passalis,N.;Tefas,A. RecurrentNeuralNetworks.InDeepLearningforRobotPerceptionandCognition;Elsevier:
Amsterdam,TheNetherlands,2022;pp.101–115.
41. Mienye,I.D.;Jere,N. DeepLearningforCreditCardFraudDetection:AReviewofAlgorithms,Challenges,andSolutions. IEEE
Access2024,12,96893–96910. [CrossRef]
42. Mienye,I.D.;Sun,Y. Amachinelearningmethodwithhybridfeatureselectionforimprovedcreditcardfrauddetection. Appl.
Sci.2023,13,7254.[CrossRef]
43. Rezk,N.M.;Purnaprajna,M.;Nordström,T.;Ul-Abdin,Z. Recurrentneuralnetworks:Anembeddedcomputingperspective.
IEEEAccess2020,8,57967–57996.[CrossRef]
44. Yu,Y.;Adu,K.;Tashi,N.;Anokye,P.;Wang,X.;Ayidzoe,M.A. Rmaf:Relu-memristor-likeactivationfunctionfordeeplearning.
IEEEAccess2020,8,72727–72741.[CrossRef]

Information2024,15,517 29of34
45. Mienye, I.D.; Ainah, P.K.; Emmanuel, I.D.; Esenogho, E. SparseNoiseMinimizationinImageClassificationusingGenetic
AlgorithmandDenseNet. InProceedingsofthe2021ConferenceonInformationCommunicationsTechnologyandSociety
(ICTAS),Durban,SouthAfrica,10–11March2021;pp.103–108.
46. Ciaburro,G.;Venkateswaran,B. NeuralNetworkswithR:SMARTModelsUsingCNN,RNN,DeepLearning,andArtificialIntelligence
Principles;PacktPublishingLtd.:Birmingham,UK,2017.
47. Nwankpa,C.;Ijomah,W.;Gachagan,A.;Marshall,S. Activationfunctions:Comparisonoftrendsinpracticeandresearchfor
deeplearning. arXiv2018,arXiv:1811.03378.
48. Szandała,T. Reviewandcomparisonofcommonlyusedactivationfunctionsfordeepneuralnetworks. Bio-InspiredNeurocomp.
2021,203–224.
49. Clevert,D.A.;Unterthiner,T.;Hochreiter,S. Fastandaccuratedeepnetworklearningbyexponentiallinearunits(elus). arXiv
2015,arXiv:1511.07289.
50. Dubey, S.R.; Singh, S.K.; Chaudhuri, B.B. Activationfunctionsindeeplearning: Acomprehensivesurveyandbenchmark.
Neurocomputing2022,503,92–108.[CrossRef]
51. Obaido,G.;Mienye,I.D.;Egbelowo,O.F.;Emmanuel,I.D.;Ogunleye,A.;Ogbuokiri,B.;Mienye,P.;Aruleba,K. Supervised
machinelearningindrugdiscoveryanddevelopment:Algorithms,applications,challenges,andprospects. Mach.Learn.Appl.
2024,17,100576.[CrossRef]
52. Mienye,I.D.;Sun,Y. EffectiveFeatureSelectionforImprovedPredictionofHeartDisease. InProceedingsofthePan-African
ArtificialIntelligenceandSmartSystemsConference,Durban,SouthAfrica,4–6December2021;pp.94–107.
53. Martins, A.; Astudillo, R. From Softmax to Sparsemax: A Sparse Model of Attention and Multi-Label Classification. In
ProceedingsoftheInternationalConferenceonMachineLearning,NewYork,NY,USA,20–22June2016;pp.1614–1623.
54. Bianchi,F.M.;Maiorino,E.;Kampffmeyer,M.C.;Rizzi,A.;Jenssen,R.;Bianchi,F.M.;Maiorino,E.;Kampffmeyer,M.C.;Rizzi,A.;
Jenssen,R. PropertiesandTraininginRecurrentNeuralNetworks. InRecurrentNeuralNetworksforShort-TermLoadForecasting:
AnOverviewandComparativeAnalysis;Springer:Berlin/Heidelberg,Germany,2017;pp.9–21.
55. Mohajerin,N.;Waslander,S.L. StateInitializationforRecurrentNeuralNetworkModelingofTime-SeriesData. InProceedings
ofthe2017InternationalJointConferenceonNeuralNetworks(IJCNN),Anchorage,AK,USA,14–19May2017;pp.2330–2337.
56. Forgione,M.;Muni,A.;Piga,D.;Gallieri,M.Ontheadaptationofrecurrentneuralnetworksforsystemidentification. Automatica
2023,155,111092.[CrossRef]
57. Zhang,J.;He,T.;Sra,S.;Jadbabaie,A. Whygradientclippingacceleratestraining:Atheoreticaljustificationforadaptivity. arXiv
2019,arXiv:1905.11881.
58. Qian,J.;Wu,Y.;Zhuang,B.;Wang,S.;Xiao,J.UnderstandingGradientClippinginIncrementalGradientMethods. InProceedings
oftheInternationalConferenceonArtificialIntelligenceandStatistics,Virtual,13–15April2021;pp.1504–1512.
59. Fei,H.;Tan,F. Bidirectionalgridlongshort-termmemory(bigridlstm):Amethodtoaddresscontext-sensitivityandvanishing
gradient. Algorithms2018,11,172.[CrossRef]
60. Dong,X.;Chowdhury,S.;Qian,L.;Li,X.;Guan,Y.;Yang,J.;Yu,Q. DeeplearningfornamedentityrecognitiononChinese
electronic medical records: Combining deep transfer learning with multitask bi-directional LSTM RNN. PLoS ONE 2019,
14,e0216046.[CrossRef][PubMed]
61. Chorowski,J.K.;Bahdanau,D.;Serdyuk,D.;Cho,K.;Bengio,Y. Attention-basedmodelsforspeechrecognition. Adv.NeuralInf.
Process.Syst.2015,28.
62. Zhou,M.;Duan,N.;Liu,S.;Shum,H.Y. ProgressinneuralNLP:Modeling,learning,andreasoning. Engineering2020,6,275–290.
[CrossRef]
63. Naseem,U.; Razzak,I.; Khan,S.K.; Prasad,M. Acomprehensivesurveyonwordrepresentationmodels: Fromclassicalto
state-of-the-artwordrepresentationlanguagemodels. Trans.AsianLow-Resour.Lang.Inf.Process.2021,20,1–35.[CrossRef]
64. Adil,M.;Wu,J.Z.;Chakrabortty,R.K.;Alahmadi,A.;Ansari,M.F.;Ryan,M.J. Attention-basedSTL-BiLSTMnetworktoforecast
touristarrival. Processes2021,9,1759.[CrossRef]
65. Min,S.;Park,S.;Kim,S.;Choi,H.S.;Lee,B.;Yoon,S. Pre-trainingofdeepbidirectionalproteinsequencerepresentationswith
structuralinformation. IEEEAccess2021,9,123912–123926.[CrossRef]
66. Jain,A.;Zamir,A.R.;Savarese,S.;Saxena,A. Structural-rnn:DeepLearningonSpatio-TemporalGraphs. InProceedingsofthe
IEEEConferenceonComputerVisionandPatternRecognition,LasVegas,NV,USA,27–30June2016;pp.5308–5317.
67. Pascanu,R.;Gulcehre,C.;Cho,K.;Bengio,Y. Howtoconstructdeeprecurrentneuralnetworks. arXiv2013,arXiv:1312.6026.
68. Shi,H.;Xu,M.;Li,R. Deeplearningforhouseholdloadforecasting—AnovelpoolingdeepRNN. IEEETrans.SmartGrid2017,
9,5271–5280.[CrossRef]
69. Gal,Y.;Ghahramani,Z. Atheoreticallygroundedapplicationofdropoutinrecurrentneuralnetworks. Adv.NeuralInf.Process.
Syst.2016,29.
70. Moradi,R.;Berangi,R.;Minaei,B. Asurveyofregularizationstrategiesfordeepmodels. Artif.Intell.Rev.2020,53,3947–3986.
[CrossRef]
71. Salehin,I.;Kang,D.K. Areviewondropoutregularizationapproachesfordeepneuralnetworkswithinthescholarlydomain.
Electronics2023,12,3106.[CrossRef]
72. Cai,S.;Shu,Y.;Chen,G.;Ooi,B.C.;Wang,W.;Zhang,M. Effectiveandefficientdropoutfordeepconvolutionalneuralnetworks.
arXiv2019,arXiv:1904.03392.

Information2024,15,517 30of34
73. Garbin,C.;Zhu,X.;Marques,O. Dropoutvs.batchnormalization:Anempiricalstudyoftheirimpacttodeeplearning. Multimed.
ToolsAppl.2020,79,12777–12815.[CrossRef]
74. Borawar,L.;Kaur,R. ResNet: SolvingVanishingGradientinDeepNetworks. InProceedingsoftheInternationalConferenceon
RecentTrendsinComputing:ICRTC2022,Delhi,India,3–4June2022;Springer:Berlin/Heidelberg,Germany,2023;pp.235–247.
75. Mienye, I.D.; Sun, Y. A deep learning ensemble with data resampling for credit card fraud detection. IEEE Access 2023,
11,30628–30638.[CrossRef]
76. Kiperwasser,E.;Goldberg,Y. SimpleandaccuratedependencyparsingusingbidirectionalLSTMfeaturerepresentations. Trans.
Assoc.Comput.Linguist.2016,4,313–327.[CrossRef]
77. Zhang,W.;Li,H.;Tang,L.;Gu,X.;Wang,L.;Wang,L. DisplacementpredictionofJiuxianpinglandslideusinggatedrecurrent
unit(GRU)networks. ActaGeotech.2022,17,1367–1382.[CrossRef]
78. Cahuantzi,R.;Chen,X.;Güttel,S.AComparisonofLSTMandGRUNetworksforLearningSymbolicSequences. InProceedingsof
theScienceandInformationConference,Nanchang,China,2–4June2023;Springer:Berlin/Heidelberg,Germany,2023;pp.771–785.
79. Shewalkar,A.;Nyavanandi,D.;Ludwig,S.A. Performanceevaluationofdeepneuralnetworksappliedtospeechrecognition:
RNN,LSTMandGRU. J.Artif.Intell.SoftComput.Res.2019,9,235–245.[CrossRef]
80. Vatanchi,S.M.;Etemadfard,H.;Maghrebi,M.F.;Shad,R. Acomparativestudyonforecastingoflong-termdailystreamflow
usingANN,ANFIS,BiLSTMandCNN-GRU-LSTM. WaterResour.Manag.2023,37,4769–4785.[CrossRef]
81. Mateus,B.C.;Mendes,M.;Farinha,J.T.;Assis,R.;Cardoso,A.M. ComparingLSTMandGRUmodelstopredicttheconditionofa
pulppaperpress. Energies2021,14,6958.[CrossRef]
82. Gers,F.A.;Schmidhuber,J. RecurrentNetsThatTimeandCount. InProceedingsoftheIEEE-INNS-ENNSInternationalJoint
ConferenceonNeuralNetworks,IJCNN2000,NeuralComputing:NewChallengesandPerspectivesfortheNewMillennium,
Como,Italy,24–27July2000;Volume3,pp.189–194.
83. Gers,F.A.;Schraudolph,N.N.;Schmidhuber,J. LearningprecisetimingwithLSTMrecurrentnetworks. J.Mach.Learn.Res.2002,
3,115–143.
84. Jaeger,H. Adaptivenonlinearsystemidentificationwithechostatenetworks. Adv.NeuralInf.Process.Syst.2002,15,593–600.
85. Ishaq, M.; Kwon, S. A CNN-Assisted deep echo state network using multiple Time-Scale dynamic learning reservoirs for
generatingShort-Termsolarenergyforecasting. Sustain.EnergyTechnol.Assessments2022,52,102275.
86. Sun,C.;Song,M.;Cai,D.;Zhang,B.;Hong,S.;Li,H. Asystematicreviewofechostatenetworksfromdesigntoapplication.
IEEETrans.Artif.Intell.2022,5,23–37.[CrossRef]
87. Gallicchio,C.;Micheli,A. Deepechostatenetwork(deepesn):Abriefsurvey. arXiv2017,arXiv:1712.04323.
88. Gallicchio,C.;Micheli,A. RichnessofDeepEchoStateNetworkDynamics. InProceedingsoftheAdvancesinComputational
Intelligence:15thInternationalWork-ConferenceonArtificialNeuralNetworks,IWANN2019,GranCanaria,Spain,12–14June2019,
Proceedings,PartI15;Springer:Berlin/Heidelberg,Germany,2019;pp.480–491.
89. Hu,R.;Tang,Z.R.;Song,X.;Luo,J.;Wu,E.Q.;Chang,S. Ensembleechonetworkwithdeeparchitecturefortime-seriesmodeling.
NeuralComput.Appl.2021,33,4997–5010.[CrossRef]
90. Gao,R.;Li,R.;Hu,M.;Suganthan,P.N.;Yuen,K.F. Dynamicensembledeepechostatenetworkforsignificantwaveheight
forecasting. Appl.Energy2023,329,120261.[CrossRef]
91. Gao,R.;Du,L.;Duru,O.;Yuen,K.F. Timeseriesforecastingbasedonechostatenetworkandempiricalwavelettransformation.
Appl.SoftComput.2021,102,107111.[CrossRef]
92. Li,S.;Li,W.;Cook,C.;Zhu,C.;Gao,Y. IndependentlyRecurrentNeuralNetwork(indrnn):BuildingaLongerandDeeperrnn.
InProceedingsoftheIEEEConferenceonComputerVisionandPatternRecognition,SaltLakeCity,UT,USA,18–23June2018;
pp.5457–5466.
93. Yang,J.;Qu,J.;Mi,Q.;Li,Q.ACNN-LSTMmodelfortailingsdamriskprediction. IEEEAccess2020,8,206491–206502.[CrossRef]
94. Ren, P.; Xiao, Y.; Chang, X.; Huang, P.Y.; Li, Z.; Chen, X.; Wang, X. Acomprehensivesurveyofneuralarchitecturesearch:
Challengesandsolutions. ACMComput.Surv.(CSUR)2021,54,1–34.[CrossRef]
95. Mellor,J.;Turner,J.;Storkey,A.;Crowley,E.J. NeuralArchitectureSearchwithoutTraining. InProceedingsoftheInternational
ConferenceonMachineLearning,Virtual,18–24July2021;pp.7588–7598.
96. Zoph,B.;Le,Q.V. Neuralarchitecturesearchwithreinforcementlearning. arXiv2016,arXiv:1611.01578.
97. Chen,X.;Wu,S.Z.;Hong,M. Understandinggradientclippinginprivatesgd:Ageometricperspective. Adv.NeuralInf.Process.
Syst.2020,33,13773–13782.
98. Zhang,Z. ImprovedAdamOptimizerforDeepNeuralNetworks. InProceedingsofthe2018IEEE/ACM26thInternational
SymposiumonQualityofService(IWQoS),Banff,AB,Canada,4–6June2018;pp.1–2.
99. DeSantanaCorreia,A.;Colombini,E.L. Attention,please!Asurveyofneuralattentionmodelsindeeplearning. Artif.Intell.Rev.
2022,55,6037–6124.[CrossRef]
100. Lin,J.;Ma,J.;Zhu,J.;Cui,Y. Short-termloadforecastingbasedonLSTMnetworksconsideringattentionmechanism. Int.J.Electr.
PowerEnergySyst.2022,137,107818.[CrossRef]
101. Chaudhari,S.;Mithal,V.;Polatkan,G.;Ramanath,R. Anattentivesurveyofattentionmodels. ACMTrans.Intell.Syst.Technol.
(TIST)2021,12,1–32.[CrossRef]
102. Bahdanau,D.;Cho,K.;Bengio,Y.Neuralmachinetranslationbyjointlylearningtoalignandtranslate. arXiv2014,arXiv:1409.0473.

Information2024,15,517 31of34
103. Luong, M.T.; Pham, H.; Manning, C.D. Effective approaches to attention-based neural machine translation. arXiv 2015,
arXiv:1508.04025.
104. Vaswani,A.;Shazeer,N.;Parmar,N.;Uszkoreit,J.;Jones,L.;Gomez,A.N.;Kaiser,Ł.;Polosukhin,I. Attentionisallyouneed.
Adv.NeuralInf.Process.Syst.2017,30.
105. Marcus,M.P.;Marcinkiewicz,M.A.;Santorini,B. BuildingalargeannotatedcorpusofEnglish: ThePennTreebank. Comput.
Linguist.1993,19,313–330.
106. Maas,A.L.;Daly,R.E.;Pham,P.T.;Huang,D.;Ng,A.Y.;Potts,C. LearningWordVectorsforSentimentAnalysis. InProceedings
ofthe49thAnnualMeetingoftheAssociationforComputationalLinguistics:HumanLanguageTechnologies,Portland,OR,
USA,19–24June2011;pp.142–150.
107. LeCun, Y.; Bottou, L.; Bengio, Y.; Haffner, P. Gradient-based learning applied to document recognition. Proc. IEEE 1998,
86,2278–2324.[CrossRef]
108. Garofolo,J.S.;Lamel,L.F.;Fisher,W.M.;Fiscus,J.G.;Pallett,D.S. TIMITacoustic-phoneticcontinuousspeechcorpus. Linguist.
DataConsort.1993,93,27403.
109. Lewis,D. Reuters-21578TextCategorizationTestCollection; Distribution1.0;AT&TLabs-Research:Atlanta,GA,USA,1997.
110. Dua,D.;Graff,C. UCIMachineLearningRepository;SchoolofInformationandComputerScience,UniversityofCalifornia:Irvine,
CA,USA,2017.
111. Lomonaco,V.;Maltoni,D. Core50:ANewDatasetandBenchmarkforContinuousObjectRecognition. InProceedingsofthe
ConferenceonRobotLearning.PMLR,MountainView,CA,USA,13–15November2017;pp.17–26.
112. Souri, A.; ElMaazouzi, Z.; AlAchhab, M.; ElMohajir, B.E. ArabicTextGenerationusingRecurrentNeuralNetworks. In
ProceedingsoftheBigData,CloudandApplications: ThirdInternationalConference,BDCA2018,Kenitra,Morocco,4–5April2018;
RevisedSelectedPapers3;Springer:Berlin/Heidelberg,Germany,2018;pp.523–533.
113. Islam,M.S.;Mousumi,S.S.S.;Abujar,S.;Hossain,S.A. Sequence-to-sequenceBanglasentencegenerationwithLSTMrecurrent
neuralnetworks. ProcediaComput.Sci.2019,152,51–58.[CrossRef]
114. Gajendran, S.; Manjula, D.; Sugumaran, V. Character level and word level embedding with bidirectional LSTM–Dynamic
recurrentneuralnetworkforbiomedicalnamedentityrecognitionfromliterature. J.Biomed.Inform.2020,112,103609.[CrossRef]
115. Hu,H.;Liao,M.;Mao,W.;Liu,W.;Zhang,C.;Jing,Y. VariationalAuto-EncoderforTextGeneration. InProceedingsofthe
2020IEEE5thInformationTechnologyandMechatronicsEngineeringConference(ITOEC),Chongqing,China,12–14June2020;
pp.595–598.
116. Holtzman,A.;Buys,J.;Du,L.;Forbes,M.;Choi,Y. Thecuriouscaseofneuraltextdegeneration. arXiv2019,arXiv:1904.09751.
117. Yin,W.;Schütze,H. Attentiveconvolution:Equippingcnnswithrnn-styleattentionmechanisms. Trans.Assoc.Comput.Linguist.
2018,6,687–702.[CrossRef]
118. Hussein,M.A.H.;Savas¸,S. LSTM-BasedTextGeneration:AStudyonHistoricalDatasets. arXiv2024,arXiv:2403.07087.
119. Baskaran,S.;Alagarsamy,S.;S,S.;Shivam,S. TextGenerationusingLongShort-TermMemory. InProceedingsofthe2024Third
InternationalConferenceonIntelligentTechniquesinControl,OptimizationandSignalProcessing(INCOS),Krishnankoil,India,
14–16March2024;pp.1–6. [CrossRef]
120. Keskar,N.S.;McCann,B.;Varshney,L.R.;Xiong,C.;Socher,R. Ctrl:Aconditionaltransformerlanguagemodelforcontrollable
generation. arXiv2019,arXiv:1909.05858.
121. Guo,H. Generatingtextwithdeepreinforcementlearning. arXiv2015,arXiv:1510.09202.
122. Yadav,V.;Verma,P.;Katiyar,V. Longshorttermmemory(LSTM)modelforsentimentanalysisinsocialdatafore-commerce
productsreviewsinHindilanguages. Int.J.Inf.Technol.2023,15,759–772.[CrossRef]
123. Abimbola, B.; deLaCalMarin, E.; Tan, Q. EnhancingLegalSentimentAnalysis: AConvolutionalNeuralNetwork–Long
Short-TermMemoryDocument-LevelModel. Mach.Learn.Knowl.Extr.2024,6,877–897.[CrossRef]
124. Zulqarnain,M.;Ghazali,R.;Aamir,M.;Hassim,Y.M.M. Anefficienttwo-stateGRUbasedonfeatureattentionmechanismfor
sentimentanalysis. Multimed.ToolsAppl.2024,83,3085–3110.[CrossRef]
125. Pujari, P.; Padalia, A.; Shah, T.; Devadkar, K. HybridCNNandRNNforTwitterSentimentAnalysis. InProceedingsofthe
InternationalConferenceonSmartComputingandCommunication;Springer:Berlin/Heidelberg,Germany,2024;pp.297–310.
126. Wankhade,M.;Annavarapu,C.S.R.;Abraham,A. CBMAFM:CNN-BiLSTMmulti-attentionfusionmechanismforsentiment
classification. Multimed.ToolsAppl.2024,83,51755–51786.[CrossRef]
127. Sangeetha,J.;Kumaran,U. AhybridoptimizationalgorithmusingBiLSTMstructureforsentimentanalysis. Meas.Sensors2023,
25,100619.[CrossRef]
128. He,R.;McAuley,J. UpsandDowns:ModelingtheVisualEvolutionofFashionTrendswithOne-ClassCollaborativeFiltering. In
Proceedingsofthe25thInternationalConferenceonWorldWideWeb,Montreal,QC,Canada,11–15April2016;pp.507–517.
129. Samir,A.;Elkaffas,S.M.;Madbouly,M.M. TwitterSentimentAnalysisusingBERT. InProceedingsofthe202131stInternational
ConferenceonComputerTheoryandApplications(ICCTA),Kochi,Kerala,India,17–19August2021;pp.182–186.
130. Prottasha,N.J.;Sami,A.A.;Kowsher,M.;Murad,S.A.;Bairagi,A.K.;Masud,M.;Baz,M. Transferlearningforsentimentanalysis
usingBERTbasedsupervisedfine-tuning. Sensors2022,22,4157.[CrossRef]
131. Mujahid,M.;Rustam,F.;Shafique,R.;Chunduri,V.;Villar,M.G.;Ballester,J.B.;Diez,I.d.l.T.;Ashraf,I. Analyzingsentiments
regardingChatGPTusingnovelBERT:Amachinelearningapproach. Information2023,14,474.[CrossRef]

Information2024,15,517 32of34
132. Wu,Y.;Schuster,M.;Chen,Z.;Le,Q.V.;Norouzi,M.;Macherey,W.;Krikun,M.;Cao,Y.;Gao,Q.;Macherey,K.;etal. Google’s
neuralmachinetranslationsystem:Bridgingthegapbetweenhumanandmachinetranslation. arXiv2016,arXiv:1609.08144.
133. Sennrich,R.;Haddow,B.;Birch,A. Neuralmachinetranslationofrarewordswithsubwordunits. arXiv2015,arXiv:1508.07909.
134. Kang,L.;He,S.;Wang,M.;Long,F.;Su,J. Bilingualattentionbasedneuralmachinetranslation. Appl.Intell.2023,53,4302–4315.
[CrossRef]
135. Yang,Z.;Dai,Z.;Salakhutdinov,R.;Cohen,W.W. Breakingthesoftmaxbottleneck:Ahigh-rankRNNlanguagemodel. arXiv
2017,arXiv:1711.03953.
136. Song,K.;Tan,X.;Qin,T.;Lu,J.;Liu,T.Y. Mass:Maskedsequencetosequencepre-trainingforlanguagegeneration. arXiv2019,
arXiv:1905.02450.
137. Hinton,G.;Deng,L.;Yu,D.;Dahl,G.E.;Mohamed,A.r.;Jaitly,N.;Senior,A.;Vanhoucke,V.;Nguyen,P.;Sainath,T.N.;etal. Deep
neuralnetworksforacousticmodelinginspeechrecognition:Thesharedviewsoffourresearchgroups. IEEESignalProcess.Mag.
2012,29,82–97.[CrossRef]
138. Hannun,A.;Case,C.;Casper,J.;Catanzaro,B.;Diamos,G.;Elsen,E.;Prenger,R.;Satheesh,S.;Sengupta,S.;Coates,A.;etal.
Deepspeech:Scalingupend-to-endspeechrecognition. arXiv2014,arXiv:1412.5567.
139. Amodei,D.;Ananthanarayanan,S.;Anubhai,R.;Bai,J.;Battenberg,E.;Case,C.;Casper,J.;Catanzaro,B.;Cheng,Q.;Chen,G.;
etal. DeepSpeech2:End-to-EndSpeechRecognitioninEnglishandMandarin. InProceedingsoftheInternationalConference
onMachineLearning,NewYork,NY,USA,20–22June2016;pp.173–182.
140. Chiu,C.C.;Sainath,T.N.;Wu,Y.;Prabhavalkar,R.;Nguyen,P.;Chen,Z.;Kannan,A.;Weiss,R.J.;Rao,K.;Gonina,E.;etal. State-
of-the-ArtSpeechRecognitionwithSequence-to-SequenceModels. InProceedingsofthe2018IEEEInternationalConferenceon
Acoustics,SpeechandSignalProcessing(ICASSP),Calgary,Canada,15–20April2018;pp.4774–4778.
141. Zhang,Y.;Chan,W.;Jaitly,N. VeryDeepConvolutionalNetworksforEnd-to-EndSpeechRecognition. InProceedingsofthe
2017IEEEInternationalConferenceonAcoustics,SpeechandSignalProcessing(ICASSP),NewOrleans,LA,USA,5–9March
2017;pp.4845–4849.
142. Dong, L.; Xu, S.; Xu, B. Speech-Transformer: A No-Recurrence Sequence-to-Sequence Model for Speech Recognition. In
Proceedingsofthe2018IEEEInternationalConferenceonAcoustics, SpeechandSignalProcessing(ICASSP),Calgary, AB,
Canada,15–20April2018;pp.5884–5888.
143. Bhaskar,S.;Thasleema,T. LSTMmodelforvisualspeechrecognitionthroughfacialexpressions. Multimed. ToolsAppl. 2023,
82,5455–5472.[CrossRef]
144. Daouad, M.; Allah, F.A.; Dadi, E.W. An automatic speech recognition system for isolated Amazigh word using 1D & 2D
CNN-LSTMarchitecture. Int.J.SpeechTechnol.2023,26,775–787.
145. Dhanjal,A.S.;Singh,W. Acomprehensivesurveyonautomaticspeechrecognitionusingneuralnetworks. Multimed.ToolsAppl.
2024,83,23367–23412.[CrossRef]
146. Nasr,S.;Duwairi,R.;Quwaider,M. End-to-endspeechrecognitionforarabicdialects. Arab.J.Sci.Eng.2023,48,10617–10633.
[CrossRef]
147. Kumar,D.;Aziz,S. PerformanceEvaluationofRecurrentNeuralNetworks-LSTMandGRUforAutomaticSpeechRecognition.
InProceedingsofthe2023InternationalConferenceonComputer,Electronics&ElectricalEngineering&TheirApplications
(IC2E3),SrinagarGarhwal,India,8–9June2023;pp.1–6.
148. Fischer,T.;Krauss,C. Deeplearningwithlongshort-termmemorynetworksforfinancialmarketpredictions. Eur.J.Oper.Res.
2018,270,654–669.[CrossRef]
149. Nelson,D.M.;Pereira,A.C.;DeOliveira,R.A. StockMarket’sPriceMovementPredictionwithLSTMNeuralNetworks. In
Proceedingsofthe2017InternationalJointConferenceonNeuralNetworks(IJCNN),Anchorage,AK,USA,14–19May2017;
pp.1419–1426.
150. Luo,A.;Zhong,L.;Wang,J.;Wang,Y.;Li,S.;Tai,W. Short-termstockcorrelationforecastingbasedonCNN-BiLSTMenhancedby
attentionmechanism. IEEEAccess2024,12,29617–29632.[CrossRef]
151. Bao,W.;Yue,J.;Rao,Y. Adeeplearningframeworkforfinancialtimeseriesusingstackedautoencodersandlong-shortterm
memory. PLoSONE2017,12,e0180944.[CrossRef][PubMed]
152. Feng,F.;Chen,H.;He,X.;Ding,J.;Sun,M.;Chua,T.S. EnhancingStockMovementPredictionwithAdversarialTraining. In
ProceedingsoftheTwenty-EighthInternationalJointConferenceonArtificialIntelligence(IJCAI-19),Macao,China,10–16August
2019;Volume19,pp.5843–5849.
153. Rundo,F. DeepLSTMwithreinforcementlearninglayerforfinancialtrendpredictioninFXhighfrequencytradingsystems.
Appl.Sci.2019,9,4460.[CrossRef]
154. Devi,T.;Deepa,N.;Gayathri,N.;RakeshKumar,S. AI-BasedWeatherForecastingSystemforSmartAgricultureSystemUsinga
RecurrentNeuralNetworks(RNN)Algorithm. Sustain.Manag.Electron.Waste2024,97–112.
155. Anshuka,A.;Chandra,R.;Buzacott,A.J.;Sanderson,D.;vanOgtrop,F.F. Spatiotemporalhydrologicalextremeforecasting
frameworkusingLSTMdeeplearningmodel. Stoch.Environ.Res.RiskAssess.2022,36,3467–3485.[CrossRef]
156. Marulanda,G.;Cifuentes,J.;Bello,A.;Reneses,J. AhybridmodelbasedonLSTMneuralnetworkswithattentionmechanismfor
short-termwindpowerforecasting. Wind.Eng.2023,0309524X231191163.[CrossRef]
157. Chen,W.;An,N.;Jiang,M.;Jia,L. Animproveddeeptemporalconvolutionalnetworkfornewenergystockindexprediction. Inf.
Sci.2024,682,121244.[CrossRef]

Information2024,15,517 33of34
158. Hasanat, S.M.; Younis, R.; Alahmari, S.; Ejaz, M.T.; Haris, M.; Yousaf, H.; Watara, S.; Ullah, K.; Ullah, Z. EnhancingLoad
ForecastingAccuracyinSmartGrids:ANovelParallelMultichannelNetworkApproachUsing1DCNNandBi-LSTMModels.
Int.J.EnergyRes.2024,2024,2403847.[CrossRef]
159. Asiri,M.M.;Aldehim,G.;Alotaibi,F.;Alnfiai,M.M.;Assiri,M.;Mahmud,A. Short-termloadforecastinginsmartgridsusing
hybriddeeplearning. IEEEAccess2024,12,23504–23513.[CrossRef]
160. YıldızDog˘an,G.;Aksoy,A.;Öztürk,N. AHybridDeepLearningModeltoEstimatetheFutureElectricityDemandofSustainable
Cities. Sustainability2024,16,6503.[CrossRef]
161. Bhambu,A.;Gao,R.;Suganthan,P.N. Recurrentensemblerandomvectorfunctionallinkneuralnetworkforfinancialtimeseries
forecasting. Appl.SoftComput.2024,161,111759.[CrossRef]
162. Mienye,E.;Jere,N.;Obaido,G.;Mienye,I.D.;Aruleba,K. DeepLearninginFinance:ASurveyofApplicationsandTechniques.
Preprints2024. [CrossRef]
163. Mastoi,Q.U.A.;Wah,T.Y.;GopalRaj,R. Reservoircomputingbasedechostatenetworksforventricularheartbeatclassification.
Appl.Sci.2019,9,702.[CrossRef]
164. Valin,J.M.;Tenneti,S.;Helwani,K.;Isik,U.;Krishnaswamy,A. Low-Complexity,Real-TimeJointNeuralEchoControland
SpeechEnhancementBasedonPercepnet. InProceedingsoftheICASSP2021-2021IEEEInternationalConferenceonAcoustics,
SpeechandSignalProcessing(ICASSP),Toronto,ON,Canada,6–11June2021;pp.7133–7137.
165. Li,Y.;Huang,C.;Ding,L.;Li,Z.;Pan,Y.;Gao,X. Deeplearninginbioinformatics:Introduction,application,andperspectivein
thebigdataera. Methods2019,166,4–21.[CrossRef]
166. Zhang,Y.;Qiao,S.;Ji,S.;Li,Y. DeepSite:BidirectionalLSTMandCNNmodelsforpredictingDNA–proteinbinding. Int.J.Mach.
Learn.Cybern.2020,11,841–851.[CrossRef]
167. Xu,J.;Mcpartlon,M.;Li,J. Improvedproteinstructurepredictionbydeeplearningirrespectiveofco-evolutioninformation. Nat.
Mach.Intell.2021,3,601–609.[CrossRef]
168. Yadav,S.;Ekbal,A.;Saha,S.;Kumar,A.;Bhattacharyya,P. Featureassistedstackedattentiveshortestdependencypathbased
Bi-LSTMmodelforprotein–proteininteraction. Knowl.-BasedSyst.2019,166,18–29.[CrossRef]
169. Aybey,E.;Gümüs¸,Ö. SENSDeep:Anensembledeeplearningmethodforprotein–proteininteractionsitesprediction. Interdiscip.
Sci.Comput.LifeSci.2023,15,55–87.[CrossRef][PubMed]
170. Li,Z.;Du,X.;Cao,Y. DAT-RNN:TrajectoryPredictionwithDiverseAttention. InProceedingsofthe202019thIEEEInternational
ConferenceonMachineLearningandApplications(ICMLA),Miami,FL,USA,14–17December2020;pp.1512–1518.
171. Lee,M.j.;Ha,Y.g. AutonomousDrivingControlUsingEnd-to-EndDeepLearning. InProceedingsofthe2020IEEEInternational
Conference on Big Data and Smart Computing (BigComp), Busan, Republic of Korea, 19–22 February 2020; pp. 470–473.
[CrossRef]
172. Codevilla,F.;Müller,M.;López,A.;Koltun,V.;Dosovitskiy,A. End-to-EndDrivingviaConditionalImitationLearning. In
Proceedingsofthe2018IEEEInternationalConferenceonRoboticsandAutomation(ICRA),Brisbane,Australia,21–25May2018;
pp.4693–4700.
173. Altché,F.; deLaFortelle,A. AnLSTMNetworkforHighwayTrajectoryPrediction. InProceedingsofthe2017IEEE20th
InternationalConferenceonIntelligentTransportationSystems(ITSC),AbuDhabi,UnitedArabEmirates,25–28October2017;
pp.353–359.
174. Li,P.;Zhang,Y.;Yuan,L.;Xiao,H.;Lin,B.;Xu,X. Efficientlong-shorttemporalattentionnetworkforunsupervisedvideoobject
segmentation. PatternRecognit.2024,146,110078.[CrossRef]
175. Li,R.;Shu,X.;Li,C. DrivingBehaviorPredictionBasedonCombinedNeuralNetworkModel. IEEETrans.Comput.Soc.Syst.
2024,11,4488–4496. [CrossRef]
176. Liu,Y.;Diao,S. Anautomaticdrivingtrajectoryplanningapproachincomplextrafficscenariosbasedonintegrateddriverstyle
inferenceanddeepreinforcementlearning. PLoSONE2024,19,e0297192.[CrossRef]
177. Altindal,M.C.;Nivlet,P.;Tabib,M.;Rasheed,A.;Kristiansen,T.G.;Khosravanian,R. Anomalydetectioninmultivariatetime
seriesofdrillingdata. GeoenergySci.Eng.2024,237,212778.[CrossRef]
178. Matar, M.; Xia, T.; Huguenard, K.; Huston, D.; Wshah, S. Multi-Head Attention Based bi-lstm for Anomaly Detection in
MultivariateTime-Seriesofwsn. InProceedingsofthe2023IEEE5thInternationalConferenceonArtificialIntelligenceCircuits
andSystems(AICAS),Hangzhou,China,11–13June2023;pp.1–5.
179. Kumaresan,S.J.;Senthilkumar,C.;Kongkham,D.;Beenarani,B.;Nirmala,P. InvestigatingtheEffectivenessofRecurrentNeural
NetworksforNetworkAnomalyDetection. InProceedingsofthe2024InternationalConferenceonIntelligentandInnovative
TechnologiesinComputing,ElectricalandElectronics(IITCEE),Bangalore,India,24–25January2024;pp.1–5.
180. Li,E.;Bedi,S.;Melek,W. Anomalydetectioninthree-axisCNCmachinesusingLSTMnetworksandtransferlearning. Int.J.Adv.
Manuf.Technol.2023,127,5185–5198.[CrossRef]
181. Minic,A.;Jovanovic,L.;Bacanin,N.;Stoean,C.;Zivkovic,M.;Spalevic,P.;Petrovic,A.;Dobrojevic,M.;Stoean,R. Applying
recurrentneuralnetworksforanomalydetectioninelectrocardiogramsensordata. Sensors2023,23,9878.[CrossRef]
182. Zhou,C.;Paffenroth,R.C. AnomalyDetectionwithRobustDeepAutoencoders. InProceedingsofthe23rdACMSIGKDD
InternationalConferenceonKnowledgeDiscoveryandDataMining,Halifax,NS,Canada,13–17August2017;pp.665–674.

Information2024,15,517 34of34
183. Ren,H.;Xu,B.;Wang,Y.;Yi,C.;Huang,C.;Kou,X.;Xing,T.;Yang,M.;Tong,J.;Zhang,Q.Time-SeriesAnomalyDetectionService
atMicrosoft. InProceedingsofthe25thACMSIGKDDInternationalConferenceonKnowledgeDiscovery&DataMining,
Anchorage,AK,USA,4–8August2019;pp.3009–3017.
184. Munir,M.;Siddiqui,S.A.;Dengel,A.;Ahmed,S. DeepAnT:Adeeplearningapproachforunsupervisedanomalydetectionin
timeseries. IEEEAccess2018,7,1991–2005.[CrossRef]
185. Hewamalage,H.;Bergmeir,C.;Bandara,K. Recurrentneuralnetworksfortimeseriesforecasting: Currentstatusandfuture
directions. Int.J.Forecast.2021,37,388–427.[CrossRef]
186. Ahmed,S.F.;Alam,M.S.B.;Hassan,M.;Rozbu,M.R.;Ishtiak,T.;Rafa,N.;Mofijur,M.;ShawkatAli,A.;Gandomi,A.H. Deep
learningmodellingtechniques:Currentprogress,applications,advantages,andchallenges. Artif.Intell.Rev.2023,56,13521–13617.
[CrossRef]
187. Li,X.;Qin,T.;Yang,J.;Liu,T.Y. LightRNN:Memoryandcomputation-efficientrecurrentneuralnetworks. Adv. NeuralInf.
Process.Syst.2016,29.
188. Katharopoulos, A.; Vyas, A.; Pappas, N.; Fleuret, F. TransformersArernns: FastAutoregressiveTransformerswithLinear
Attention. InProceedingsoftheInternationalConferenceonMachineLearning,Virtual,12–18July2020;pp.5156–5165.
189. Shao,W.;Li,B.;Yu,W.;Xu,J.;Wang,H. WhenIsItLikelytoFail? PerformanceMonitorforBlack-BoxTrajectoryPrediction
Model. IEEETrans.Autom.Sci.Eng.2024,4,765–772.[CrossRef]
190. Jacobs,W.R.;Kadirkamanathan,V.;Anderson,S.R.Interpretabledeeplearningfornonlinearsystemidentificationusingfrequency
responsefunctionswithensembleuncertaintyquantification. IEEEAccess2024,12,11052–11065.[CrossRef]
191. Mamalakis,M.;Mamalakis,A.;Agartz,I.;Mørch-Johnsen,L.E.;Murray,G.;Suckling,J.;Lio,P. Solvingtheenigma:Deriving
optimalexplanationsofdeepnetworks. arXiv2024,arXiv:2405.10008.
192. Shah,M.;Sureja,N. AComprehensiveReviewofBiasinDeepLearningModels:Methods,Impacts,andFutureDirections. Arch.
Comput.MethodsEng.2024,1–13.[CrossRef]
193. Goethals,S.;Calders,T.;Martens,D.BeyondAccuracy-Fairness:Stopevaluatingbiasmitigationmethodssolelyonbetween-group
metrics. arXiv2024,arXiv:2401.13391.
194. Weerts,H.;Pfisterer,F.;Feurer,M.;Eggensperger,K.;Bergman,E.;Awad,N.;Vanschoren,J.;Pechenizkiy,M.;Bischl,B.;Hutter,
F. Canfairnessbeautomated?Guidelinesandopportunitiesforfairness-awareAutoML. J.Artif.Intell.Res.2024,79,639–677.
[CrossRef]
195. Bai,Y.;Geng,X.;Mangalam,K.;Bar,A.;Yuille,A.L.;Darrell,T.;Malik,J.;Efros,A.A. SequentialModelingEnablesScalable
LearningforLargeVisionModels. InProceedingsoftheIEEE/CVFConferenceonComputerVisionandPatternRecognition,
SeattleWA,USA,17–21June2024;pp.22861–22872.
196. Taye,M.M. Understandingofmachinelearningwithdeeplearning:Architectures,workflow,applicationsandfuturedirections.
Computers2023,12,91.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.