Review
Foundations and Innovations in Data Fusion and Ensemble
Learning for Effective Consensus
Ke-LinDu1 ,RengongZhang2 ,BingchunJiang1,* ,JieZeng3 andJiabinLu4
1 SchoolofMechanicalandElectricalEngineering,GuangdongUniversityofScienceandTechnology,
Dongguan523668,China;kldu@gdust.edu.cn
2 ZhejiangYugongInformationTechnologyCo.,Ltd.,ChangheRoad475,Hangzhou310002,China;
zrg@ygwjg.com
3 ShenzhenFengXingTaiBaoTechnologyCo.,Ltd.,Shenzhen518063,China;zj@fxtb.cc
4 FacultyofElectromechanicalEngineering,GuangdongUniversityofTechnology,Guangzhou510006,China;
lujiabin@gdut.edu.cn
* Correspondence:jiangbingchun@gdust.edu.cn
Abstract: Ensemble learning and data fusion techniques play a crucial role in modern
machinelearning,enhancingpredictiveperformance,robustness,andgeneralization. This
paper provides a comprehensive survey of ensemble methods, covering foundational
techniques such as bagging, boosting, and random forests, as well as advanced topics
includingmulticlassclassification,multiviewlearning,multiplekernellearning,andthe
Dempster–Shafertheoryofevidence. Wepresentacomparativeanalysisofensemblelearn-
inganddeeplearning,highlightingtheirrespectivestrengths,limitations,andsynergies.
Additionally,weexaminethetheoreticalfoundationsofensemblemethods,includingbias–
variancetrade-offs,margintheory,andoptimization-basedframeworks,whileanalyzing
computationaltrade-offsrelatedtotrainingcomplexity,inferenceefficiency,andstorage
requirements. Toenhanceaccessibility, weprovideastructuredcomparativesummary
ofkeyensembletechniques. Furthermore,wediscussemergingresearchdirections,such
asadaptiveensemblemethods,hybriddeeplearningapproaches,andmultimodaldata
fusion,aswellaschallengesrelatedtointerpretability,modelselection,andhandlingnoisy
datainhigh-stakesapplications. Byintegratingtheoreticalinsightswithpracticalconsider-
ations,thissurveyservesasavaluableresourceforresearchersandpractitionersseekingto
AcademicEditors:FlorinLeon,
understandtheevolvinglandscapeofensemblelearninganditsfutureprospects.
MirceaHuleaandMariusGavrilescu
Received:1January2025 Keywords:ensemblelearning;bagging;boosting;randomforests;deeplearningintegration;
Revised:2February2025
multimodaldatafusion
Accepted:8February2025
Published:11February2025
MSC:68Q32;68T99
Citation: Du,K.-L.;Zhang,R.;Jiang,
B.;Zeng,J.;Lu,J.Foundationsand
InnovationsinDataFusionand
EnsembleLearningforEffective
1. Introduction
Consensus.Mathematics2025,13,587.
https://doi.org/10.3390/ The no-free-lunch theorem asserts that no single method universally outperforms
math13040587 othersacrossallproblemdomains. Inpractice,varioustechniquesareemployedtotackle
Copyright:©2025bytheauthors. specificchallenges,eachwithitsownstrengthsandweaknesses. Oneeffectiveapproachto
LicenseeMDPI,Basel,Switzerland. solvingcomplexproblemsisbrainstorming,wherediverseperspectivesareshared,and
Thisarticleisanopenaccessarticle decisionsaremadethroughconsensusorvoting.
distributedunderthetermsand
Learning algorithms differ in accuracy, and the no-free-lunch theorem states that
conditionsoftheCreativeCommons
no single algorithm excels in all domains. Combining algorithms can improve perfor-
Attribution(CCBY)license
mance,withaninfinitenumberofunbiasedclassifiersapproximatingtheoptimalBayes
(https://creativecommons.org/
licenses/by/4.0/). classifier[1]. Datafusioninvolvesintegratingmultiplerecordscorrespondingtothesame
Mathematics2025,13,587 https://doi.org/10.3390/math13040587

Mathematics2025,13,587 2of49
real-worldentityintoaunified,consistent,andaccuraterepresentation. Inmachinelearn-
ing,thefusionofdataplaysacrucialroleinboostingpredictionaccuracyandensuring
reliability,addressingasignificantchallengeinthefield.
Fusionstrategiescanbeappliedatvariouslevels,includingthesignalenhancement
and sensor (data) level, feature level, classifier level, decision level, and semantic level.
Evidencetheory[2]isaframeworkwithinthedomainofimpreciseprobabilities.
Inclassificationtasks,diverseclassifierscanbecreatedthroughdifferentinitializa-
tions,trainingonvarieddatasets,orutilizingdistinctfeaturesets. Ensemblemethods[3,4]
generatemultiplebaselearnersandcombinethemintoasinglecompositepredictorfor
classifyingnewdata. Thisapproachreliesontheconceptofdiversity[5],wheretwoclassi-
fiersareconsidereddiverseiftheyproducedifferentincorrectpredictionsonunseendata.
Diversityisacrucialfactorinensemblelearning,oftenreferredtoasacommitteemachine
oramixtureofexperts. Byleveragingdiversity,ensemblelearningenhancesclassification
accuracycomparedtoanyindividualclassifier,giventhesametrainingdata.
Inensemblelearning,theclassifierswithintheensemblecanbebuiltindependently,as
inbagging[3],orsequentially,asinboosting[4]. Theeffectivenessofensembletechniques
largely stems from the diversity among weak learners, which increases the variability
of predictions and enhances the ensemble’s generalization ability. This is achieved by
aggregatingpredictionsthroughstrategiessuchasmajorityvotingorweightedaveraging.
Fusingmultipleprobabilitydensityfunctions(pdfs)isaspecializedformofdataor
informationfusion[6]. Intheaxiomaticframework,fusionrulesaredefinedbyadheringto
specificproperties(axioms),whilethesupra-Bayesianmethodtreatsthepdfstobefusedas
randomobservationsinterpretedbythefusioncenter.
Variousstrategiesforgeneratingbaselearnersoperateatdifferentlevels. Atthedata
level,methodsincludesamplingtechniqueslikebagging[3]anddagging[7],orweighting
strategies like boosting [8], wagging [9], and multiboosting [10]. At the feature level,
methodssuchasrandomsubspace[11]areemployed. Techniquescombiningbothdata
andfeaturemanipulationsincluderandomforests[12]androtationforests[13]. Additional
approachesincludenegativecorrelationlearning[14]andneuralnetwork-basedmethods
utilizingrandominitialization[15].
Despite their effectiveness, ensemble learning and data fusion present challenges,
suchasincreasedcomputationalcomplexity,scalabilityconcerns,andtheneedforefficient
integrationwithdeeplearningmodels. Giventheincreasingprevalenceoflarge-scale,high-
dimensionaldatasets,understandingthetrade-offsbetweendifferentensemblestrategies
iscrucialforreal-worldapplications.
Theobjectiveofthispaperistoexplorehowensemblelearninganddatafusioncan
addresscriticalchallengesinmachinelearning. Byleveragingdiversityamongmodels
andintegratinginformationatvariouslevels,thisstudyhighlightshowtheseapproaches
improveclassificationaccuracy,robustness,andgeneralization.
Specifically,thispaperprovidesacomprehensiveexaminationofbothfundamental
and advanced topics, including multiclass classification, multiview learning, multiple
kernellearning,andtheDempster–Shafertheoryofevidence. Furthermore,itanalyzes
theinterplaybetweenensemblelearninganddeeplearning,offeringinsightsintotheir
respectiveadvantages. Bydoingso,thisarticleaimstoserveasaresourceforresearchers
andpractitionersseekingtounderstandandapplythesemethodologieseffectively.
Forreadersnewtoensemblelearning,werecommendstartingwithSection2,which
categorizesensemblelearningmethodsandprovidesanoverviewoffoundationalconcepts
beforeprogressingtoadvancedtopicssuchasmulticlassclassification(Section10)and
multiviewlearning(Section12). Additionally,Table1servesasaquickreferenceguide

Mathematics2025,13,587 3of49
tohelpreadersidentifythemostsuitabletechniquesbasedontheirneedsandfamiliarity
withthetopic.
Table1.Summaryofpopularensemblelearningmethods.
Method Strengths Weaknesses TypicalApplications
Reducesvariance,improves Lesseffectiveforbiased Imageclassification,tabular
Bagging
stability models data
Highaccuracy,adaptive Pronetooverfitting,sequential
Boosting Frauddetection,rankingtasks
learning training
Robust,featureselection, Requiresstorageformultiple Medicaldiagnosis,remote
Randomforests
scalable trees sensing
Efficient,handlesmissingdata, Highmemoryusage,tuning
XGBoost Timeseriesforecasting,NLP
fasttraining complexity
Thispaperpresentsacomprehensiveoverviewofensemblelearninganddatafusion.
Section2categorizesensemblelearningmethods,providingafoundationforthesubse-
quent discussions. Sections 3–8 examine key topics, including aggregation techniques,
majorityvoting,theoreticalanalyses,bagging,boosting,andrandomforests. Acompara-
tiveanalysisofpopularensemblemethodsisprovidedinSection9. Section10addresses
multiclassclassification,whileSection11discussestheDempster–Shafertheoryofevidence.
Section12exploresmultiviewlearning,followedbyanin-depthexaminationofmultiple
kernellearning(MKL)inSection13. NetworkensemblesarecoveredinSection14,with
theirtheoreticalfoundationsreviewedinSection15. Section16introducesincrementalen-
semblelearning,andSection17comparesensemblelearningwithdeeplearning. Empirical
validationsfromtheliteraturearepresentedinSection18.Finally,Section19outlinesfuture
researchdirections,andSection20concludesthispaperbysummarizingkeyinsightsand
openchallenges.
2. EnsembleLearningMethods
Popularensembletechniquessuchasrandomforests[12],bagging(bootstrapaggre-
gating)[3],andrandominitialization[16]promotediversitybyeitherrandomlyinitializing
modelsorresamplingthetrainingdataforeachmodel. Boosting[17]andsnapshoten-
sembles[18]alsofosterdiversitybytrainingmultiplemodelswhileensuringadegreeof
differencebetweenthenewlytrainedmodelsandtheirpredecessors.
Bagging[3]andboosting[4]aretwowidelyusedensemblemethodsthattrainmodels
ondifferentdistributionsofthedata.Bagginggeneratesmultipletrainingsets,or“bags”,by
randomlysamplingwithreplacement,whileboostingadaptivelyadjuststhetrainingset’s
distribution,focusingmoreondifficultexamplesbasedonpreviousclassifiers’performance.
Baggingreducesglobalvariancebytrainingmultiplemodelsondifferentdistributionsof
thedata,whileboostingiterativelytrainsweakmodelstominimizetheoverallmodelbias.
Bothbaggingandrandomforestsinvolveensembletreeswhereeachtreevotesforthe
predictedclass. Randomforestsandboostingsharesimilarmechanisms[19],withboth
typicallyoutperformingothermethodsinreducinggeneralizationerror,significantlysur-
passingbagging[12,19]. However,unlikerandomforests,boostingevolvesthecommittee
ofweaklearnersovertime,witheachlearnercastingaweightedvote.
Subspaceormultiviewlearninggeneratesmultipleclassifiersfromdistinctfeature
spaces,allowingeachclassifiertodefineitsdecisionboundariesfromadifferentperspective.
Byleveragingtheagreementbetweentheselearners,multiviewlearningaimstoimprove
classification performance. Notable methods in this area include the random subspace
method[11],randomforests[20],androtationforests[13].

Mathematics2025,13,587 4of49
Themixtureofexperts[21]isadivide-and-conquerapproachthatincludesagating
network for soft partitioning of the input space and expert networks that model each
partition. Theclassifiersandgatingmechanismarejointlytrainedonthedataset. This
techniquecanbeviewedasaradialbasisfunction(RBF)networkwherethesecond-layer
weightsw,knownasexperts,areoutputsoflinearmodelsthatprocesstheinput. TheVC
dimensionboundsformixturesofexpertsarediscussedin[22].
TheBayesiancommitteemachine[23]partitionsthedatasetintoMequalsubsets,with
Mmodelstrainedonthesesubsets. Predictionsarecombinedusingweightsbasedonthe
inversecovarianceofeachmodel’spredictionwithintheBayesianframeworkforGaussian
processregression. Thoughapplicabletovariousestimators,themethodprimarilytargets
Gaussianprocessregression,regularizationnetworks,andsmoothingsplines. Performance
improveswhenmultipletestpointsarequeriedsimultaneously,reachingoptimalitywhen
thenumberoftestpointsmatchesorexceedstheestimator’sdegreesoffreedom. Bayesian
modelaveraging[24]offersarelatedensembletechniquefromaBayesianperspective.
Stackgeneralization[25]improvesvotingbycombiningbaselearnersthroughacom-
biner trained on a separate dataset, addressing individual learner biases. Stacking [26]
refinespredictionsbytrainingastrongermodelonoutputsfrommultipleweakmodels,
usingcross-validationtoestimateweightsbasedonperformanceratherthanposteriorprob-
abilities. WhileBayesianmodelaveragingmatchesstackingwhenthetruedata-generating
modelisincluded[27],itismoresensitivetomodelapproximationerrors. Stacking,in
contrast,excelsundersignificantbiasorlimitedmodelrepresentationalcapacity,makingit
morerobustinmostpracticalscenarios[27].
Cascading is a multi-stage method where learner j is only applied if all preceding
learnersk(fork < j)arenotconfident. Eachlearnerhasanassociatedconfidenceweight
w ,whichindicateshowconfidentitisinitsoutput. Thelearnerjcanbeusedifw exceeds
j j
athreshold θ j , where1/K < θ j ≤ θ j+1 < 1incaseof K classes. Forclassificationtasks,
the confidence is defined by the highest posterior probability: w = max p , with p
j i ji ji
representingtheconfidenceoflearnerjforclassi.
Recentadvancementsinensemblelearningextendtraditionalapproachestoimprove
modelperformance,scalability,andinterpretability. Deepensembles[28]enhancerobust-
nessanduncertaintyestimationbyaggregatingmultipleindependentlytraineddeepneural
networks.Thesemethodsareparticularlyvaluableinapplicationsrequiringwell-calibrated
uncertaintyestimates,suchasmedicaldiagnosisandautonomoussystems.
Hybridensemblestrategiesintegratemultipleensembleparadigmstomaximizetheir
respectivestrengths. Forinstance,AdaBoostcanbecombinedwithdeepneuralnetworks
toenhancerobustness,whilebaggingandboostingcanbehybridizedtobalancevariance
reductionandbiascorrection[29]. Additionally,evolutionaryalgorithms[30,31]havebeen
appliedtodynamicallyoptimizeclassifierselectionandweighting,improvingadaptability
acrossdiverselearningtasks.
Advancedaggregationtechniques,suchasmeta-learning-basedensembles[32],dy-
namicallyadjusttheensemblecompositionbasedondatasetcharacteristics. Unlikestatic
combinationsofweaklearners,thesemethodsutilizereinforcementlearningoroptimiza-
tiontechniquestotailortheensemblestructuretospecificproblemdomains.
Attention-basedensemblemethodshaveemergedasaneffectiveapproachtoenhanc-
ing model performance by selectively focusing on different parts of the input data. By
leveragingmultipleattentionmasks[33],eachlearnercanemphasizedistinctregionsof
theinputspace. Thisstrategypromotesdiversityamonglearnersandhasdemonstrated
significantperformanceimprovementsindeepmetriclearningtasks.
Ensemble pruning seeks to enhance efficiency by selecting a subset of classifiers
thatmaintainpredictiveperformancewhilereducingcomputationalcomplexity. In[34],

Mathematics2025,13,587 5of49
ensemblepruningisapproachedasasubmodularfunctionmaximizationproblem. This
structuredmethodeffectivelybalancesclassifierqualityanddiversity,enablingefficient
optimizationwhilepreservingtheensemble’spredictivepower.
Neuralnetworks[35,36]andsupportvectormachines(SVMs)[37]canbeviewedas
ensemblemethods. Bayesianapproachestononparametricregressioncanalsobeinter-
pretedasensemblemethods,whereacollectionofcandidatemodelsisaveragedaccording
totheposteriordistributionoftheirparametervalues. Theerror-correctingoutputcode
(ECOC)methodformulticlassclassification[38]isanotherexampleofalearningensemble.
Similarly, dictionary methods like regression splines can be characterized as ensemble
methods, with the basis functions acting as weak learners. Neural trees [39] merge
neuralnetworksanddecisiontrees,whichoperateondistinctparadigms—connectionist
andsymbolic—offeringcomplementarystrengthsandlimitations,withneuralnetworks
learninghierarchicalrepresentationsanddecisiontreeslearninghierarchicalclusters.
3. Aggregation
Aggregationinvolvescombiningdatafrommultiplesourcesorthepredictionsfrom
variouscandidates[40].Itservesasafundamentalstepinensemblemethods.Infuzzylogic,
twocommonaggregationoperatorsaret-normandt-conorm[41]. Theorderedweighted
averaging (OWA) operator [42] is a widely used aggregation method in multicriteria
decision-making,offeringaparameterizedfamilyofoperatorsthatincludesthemaximum,
minimum,andaverageasspecialcases.
Thebasealgorithmsinanensemblecandifferbyalgorithmtype,parametersettings,
inputfeatures,ortrainingdatasubsets. Baselearnersmayalsousecascadedtrainingor
address subtasks of a primary task, as with ECOCs. Learner combination can occur in
parallelorthroughamultistageprocess.
Voting is a straightforward method for combining multiple classifiers by taking a
weightedsumoftheiroutputs. Thefinaloutputiscalculatedas
L
∑
y = w d , (1)
i j ji
j=1
wheretheweightssatisfythecondition
L
∑
w =1, w ≥0, ∀j, (2)
j j
j=1
andd representsthevoteoflearnerjforclassi,andw denotestheweightassociatedwith
ji j
eachvote.
When w = 1/L, this corresponds to simple voting. In classification tasks, this is
j
knownaspluralityvoting,wheretheclassreceivingthemostvotesischosenasthewinner.
Inthecaseoftwoclasses,itisreferredtoasmajorityvoting,wheretheclassthatsecures
morethanhalfofthevotesisselected. Votingmechanismscanbeinterpretedwithina
Bayesianframework,wheretheweightsrepresentpriormodelprobabilities,andthemodel
decisionscorrespondtomodel-conditionallikelihoods.
Aggregationtypicallycarriesalowerriskthanthebestindividualrule[43]. Incom-
parison,cross-validation,whichselectsonlyonecandidate,cannotexceedtheperformance
ofthebestrulewithinthefamily.
Theaggregatedhold-out(Agghoo)method[44]isanensemblemethodthatcombines
resamplingandaggregation,similartobagging. However,unlikeAgghoo,baggingapplies
to single estimators and does not address estimator selection. Thus, if there is a free
hyperparameter, bagging must be paired with an estimator selection method, such as

Mathematics2025,13,587 6of49
cross-validation. Bagging applied to hold-out was first proposed by [3] as a means to
combinepruningandbagginginclassificationandregressiontrees(CART).
Agghoo averages the learning rules chosen through hold-out, which is a form of
cross-validationwithasinglesplit. Whentheriskisconvex,Agghooperformsnoworse
thanthehold-outmethod,andthisholdsforclassificationwith0-1risk,withanadded
constant factor. The data are split multiple times, and for each split, one predictor is
selectedbythehold-out,withthefinalpredictorsaggregated. Agghooisalsoreferredtoas
cross-validation+averagingin[45,46].
Inclassification, theequivalentofAgghooistouseamajorityvote, knownasMa-
jhoo. AgghooandMajhoooutperformhold-outandsometimessurpasscross-validation,
provided their parameters are properly selected [44]. For k-nearest neighbors (k-NN),
Majhooperformsnotablybetterthancross-validationinselectingtheoptimalnumberof
neighbors[44].
IncontrasttoAgghoo,whichaveragesselectedpredictionrules,onecanalsoaverage
thechosenregularizationparameterinhigh-dimensionalregressionusingthemethodsof
K-foldaveragingcross-validation[47]andbaggedcross-validation[48].
Vote aggregation methods for combining the predictions of component classifiers
canbebroadlydividedintotwocategories: weightingmethodsandmetalearningmeth-
ods[49,50]. Weightingmethodsassignaweighttoeachclassifierandaggregatetheirvotes
accordingly (e.g., majority voting, performance weighting, and Bayesian combination).
Thesemethodsareeffectivewhentheclassifiersperformsimilartasksandhavecomparable
accuracy. Ontheotherhand,metalearningmethodsinvolvelearningfromboththeclassi-
fiersandtheirpredictionsontrainingdata(e.g.,stacking,arbitertrees,andgrading). These
methodsareparticularlyusefulwhencertainclassifierstendtoconsistentlymisclassifyor
correctlyclassifyspecificinstances[49].
4. MajorityVoting
Majorityvotingiseffectivewhenthereislimitedornoinformationaboutthelabeling
qualityofindividuallabelers,classdistributions,orinstancedifficulty,makingitpartic-
ularly attractive for crowdsourcing applications. It performs well when most labelers
havealabelingaccuracygreaterthan50%inbinarytasks,andtheirerrorsaredistributed
approximatelyuniformlyacrossallclasses.
Inweightedmajorityvoting,eachclassifierorvoterisassignedaspecificweight. The
PAC-Bayesiantheory[51]providesPACguaranteesforBayesian-likelearningalgorithms.
This approach bounds the risk of a weighted majority vote indirectly by analyzing the
associatedGibbsclassifier.ThePAC-Bayesiantheoremgivesariskboundforthe“true”risk
oftheGibbsclassifierbyconsideringitsempiricalriskandtheKullback–Leiblerdivergence
betweentheposteriorandpriordistributions. Theriskofthemajorityvoteclassifieris
knowntobeatmosttwicethatoftheGibbsclassifier[52,53].
TheC-bound[54]isamoreaccurateriskindicatorformajorityvoting. Byminimizing
theC-bound,thetrueriskoftheweightedmajorityvotecanbereduced,whichisformu-
lated as a quadratic optimization problem. Based on PAC-Bayesian theory, the MinCq
algorithm [55] optimizes the weights of a set of voters H by minimizing the C-bound,
whichinvolvesthefirsttwostatisticalmomentsofthemarginonthetrainingdata. MinCq
outputsaposteriordistributionQoverH,assigningeachvoteraweight.
Thebehaviorofmajorityvotesinbinaryclassificationisanalyzedin[56],showing
thattheC-boundcanoutperformtheGibbsclassifier’srisk,approachingzeroevenwhen
theGibbsriskisnear1/2. MinCqoutperformsAdaBoostandSVM,whileP-MinCq[57]
extendsMinCqbyintegratingpriorknowledgeasaweightdistributionconstraint,with
convergenceproofsfordata-dependentvotersinthesamplecompressionsetting. Applied

Mathematics2025,13,587 7of49
to k-NN voting, P-MinCq demonstrates strong resistance to overfitting, particularly in
high-dimensionalcontexts.
MajorityvotesarecentraltotheBayesianframework[58],wherethemajorityvote
istheBayesclassifier. Classifiersfromkernelmethods,suchasSVM,canalsobeseenas
majorityvotes. Specifically,theSVMclassifiercomputessgn
(cid:16) ∑|S|
α y k(x,x)
(cid:17)
,wherek(·)
i=1 i i i
isakernelfunction,andthepairs(x,y )aretrainingexamplesinthesetS. Eachy k(x,·)
i i i i
actsasavoterwithconfidence|k(x,x)|,andα istheweightofthevoter. Similarly,the
i i
neuronsinaneuralnetwork’sfinallayercanbeinterpretedasperformingmajorityvoting.
Whilemajorityvotingisoneofthesimplestandmostwidelyusedensemblemethods,
recentresearchhasexploredvariousenhancementstoimproveitseffectiveness. Onesuch
extension is weighted majority voting, where classifiers are assigned different voting
weights based on their predictive confidence or past performance [59]. This approach
ensuresthatmorereliableclassifiershaveastrongerinfluenceonthefinaldecision.
Another advancement is the use of probabilistic voting schemes, where classifiers
outputprobabilitydistributionsratherthandiscretelabels,andtheensembleaggregates
theseprobabilitiestomakeamoreinformeddecision[60]. Thismethodcanmitigatethe
impactofweakclassifiersandisparticularlyusefulinimbalancedlearningscenarios.
Fromatheoreticalstandpoint,recentstudieshaveanalyzederrorboundsformajority
voting,showingthatitseffectivenessdependsonclassifierdiversityandindividualaccu-
racies[61]. Thisalignswiththeconceptthatensemblediversityiscrucialforimproving
generalizationperformance. Ouranalysissuggeststhatwhilemajorityvotingisrobustin
manycases,itsperformancecanbefurtherenhancedbyincorporatingconfidence-aware
votingschemesandoptimizingensemblediversity.
5. TheoreticalAnalysisofEnsembleMethods
Ensemble learning methods operate by aggregating multiple models to improve
predictiveperformance,generalization,androbustness. Thetheoreticalfoundationofthese
methodsprimarilyrevolvesaroundthebias–variancedecomposition,margintheory,and
optimizationstrategies.
5.1. Bias–VarianceDecomposition
Afundamentalresultinstatisticallearningtheoryisbias–variancedecomposition,
whichstatesthattheexpectederrorofamodelcanbeexpressedasfollows:
(cid:20)(cid:16) (cid:17)2 (cid:21)
E y− fˆ(x) =Bias2+Variance+σ2, (3)
where fˆ(x) is the predicted output of the model given input x ∈ Rd, Bias2 represents
thesystematicerror duetoincorrectassumptionsinthe model, Variancequantifiesthe
sensitivitytofluctuationsinthetrainingdata,andσ2denotestheirreduciblenoise.Bagging
reducesvariancebyaveragingmultiplemodelstrainedondifferentbootstrapsamples,
whereasboostingaimstoreducebiasbyiterativelyrefiningweaklearners.
5.2. MarginTheoryinBoosting
Boostingmethodsaretheoreticallyjustifiedthroughmargintheory. Ithasbeenshown
thatboostingalgorithms,suchasAdaBoost,increasetheminimummarginofthetrainingdata,
whichcorrelateswithimprovedgeneralizationperformance[62].Moreformally,thegeneral-
izationerrorboundofaboostedclassifierH(x)dependsontheempiricalmargindistribution:
(cid:18) (cid:19)
1
P(H(x) (cid:54)= y) ≤ P(γ(x) < θ)+O √ , (4)
T

Mathematics2025,13,587 8of49
whereH(x)istheensembleclassifier,γ(x)denotesthemargin(i.e.,confidenceoftheclassi-
fierinthecorrectlabel),θisamarginthreshold,andTisthenumberofboostingiterations.
Theimplicationisthatboostingcontinuestoimprovegeneralizationperformanceeven
afterthetrainingerrorreacheszero.
5.3. EnsemblePruning
Recentstudieshaveexploredoptimization-drivenensemblelearningtechniques. En-
semble pruning seeks to optimize the trade-off between accuracy and computational
complexity by selecting a subset of base classifiers [63]. The pruning problem can be
formulatedasfollows:
max ∑ w I(h(x) = y), (5)
h
S⊆H
h∈S
whereHisthesetofallbaseclassifiers,S ⊆ Histheselectedsubsetofclassifiers,w is
h
theweightassignedtoclassifierh,and
I(·)istheindicatorfunction,whichequals1ifthe
classifierpredictscorrectlyand0otherwise.
Approachessuchasgreedyoptimizationandconvexrelaxationmethodshavebeen
developedtosolvethisproblemefficiently.
Thesetheoreticalresultsprovidearigorousfoundationforunderstandingthemecha-
nismsbehindensemblemethods,offeringinsightsintotheirbias–variancetradeoff,margin
improvements,andoptimization-basedrefinements.
6. Bagging
Bagging[3]isanensemblemethoddesignedtoreducevarianceandimprovemodel
stabilitybytrainingmultiplebaselearnersondifferentsubsetsofthetrainingdata. Each
subsetisgeneratedthroughbootstrapsampling,whereinstancesarerandomlyselected
withreplacement.Thefinalpredictionisobtainedviamajorityvotingforclassificationtasks
oraveragingforregressiontasks. Thisapproachisparticularlyeffectiveforhigh-variance,
low-biasmodelslikedecisiontrees.
Akeyadvantageofbaggingisitsabilitytomitigateoverfittingbyreducingmodel
variance. Sinceindividualclassifiersaretrainedondifferentsampledsubsets,theirpredic-
tionvarianceisaveragedout,leadingtoimprovedgeneralization. Thiseffectisparticularly
beneficialformodelslikedecisiontrees,makingbaggingastrongchoiceforstabilizing
complexlearnerssuchasrandomforests[12].
Decisiontreesarewell-suitedforbaggingsincetheycanmodelcomplexdatainter-
actions. Because all trees in bagging are trained independently on different bootstrap
samples,averagingtheirpredictionsdoesnotchangebiascomparedtoindividualtrees.
Thisdiffersfromboosting,wheretreesaretrainedsequentiallytoreducebias[64]andare
notidenticallydistributed.
Recentadvancementsinbaggingincludestratifiedbagging,whichensuresamore
balanceddistributionofclasslabelsacrosssubsets,improvingperformanceinimbalanced
datasets[65]. Deepbaggingensembleshaveemerged,wheredeepneuralnetworksare
combinedusingbaggingtoimproverobustnessinhigh-dimensionaltasks,particularlyin
medicalimageanalysisandfinancialforecasting[66]. Researchershavealsoexploredhy-
bridbaggingapproachesthatintegratekernelmethodstoenhancefeaturerepresentations
beforetrainingensemblemodels[67].
Theperformanceboostfrombaggingcomesfromrepeatedlytrainingamodelonvari-
ousbootstrapsamplesandaveragingtheresultingpredictions. Itisparticularlyeffective
forunstablemodels,wheresmallchangesinthetrainingdatacanleadtosignificantdiffer-
encesinpredictions[3]. Unlikebagging,boostingassignsdifferentweightstopredictions
duringaveraging.

Mathematics2025,13,587 9of49
While both bagging and boosting are non-Bayesian, they share similarities with
MarkovChainMonteCarlo(MCMC)methodsinBayesianmodels. InaBayesiancontext,
parameters are adjusted based on a posterior distribution, while bagging perturbs the
trainingdataindependentlyandre-estimatesthemodelforeachperturbation. Thefinal
predictionisanaverageofallthesemodels. However,baggingsuffersfromrandomness,
asclassifiersaretrainedindependentlywithoutinteraction.
Mathematically,baggingcanbeexpressedasfollows:
L
fˆ(x ) = ∑ w E(y |x ,θˆ ), (6)
new l new new l
l=1
where θˆ represents a collection of model parameters. In the case of a Bayesian model,
l
w =1/L,andtheaverageservestoestimatetheposteriormeanbysamplingθ fromthe
l l
posteriordistribution. Forbagging,w =1/L,withθˆ correspondingtoparametersrefitted
l l
tobootstrapresamplesofthedata. Inboosting,w =1,whileθˆ ischosensequentiallyto
l l
iterativelyrefinethemodel’sfit.
Onlinebagging[68]appliesthebaggingprocedureinasequentialmanner,approx-
imatingtheoutcomesoftraditionalbatchbagging. Avariationofthismethodinvolves
replacingthestandardbootstrapwiththeBayesianbootstrap,wheretheonlineBayesian
versionofbagging[69]ismathematicallyequivalenttoitsbatchBayesiancounterpart. By
adoptingaBayesianapproach,thismethodoffersalosslessbaggingtechnique,improving
accuracyandreducingpredictionvariance,particularlyforsmalldatasets.
7. Boosting
Boosting, or ARCing (adaptive resampling and combining), was introduced in [4]
toenhanceweaklearningalgorithms,whichgenerateclassifiersonlyslightlybetterthan
random guessing. Schapire demonstrated that strong and weak PAC learnability are
equivalent[4],formingthetheoreticalfoundationforboosting. Boostingalgorithms,atype
ofvotingmethod,combineweakclassifierslinearly.
Boosting[4]isaniterativeensemblemethodthattrainsweaklearnerssequentially,
with each learner focusing more on misclassified instances from the previous iteration.
Unlikebagging,whichbuildsindependentmodels,boostingassignsadaptiveweightsto
trainingsamples,ensuringthatdifficultinstancesreceivegreaterattentioninsubsequent
trainingrounds.
Akeyadvantageofboostingisitsabilitytominimizebiasbyconvertingweaklearners
intostrongones. Eachiterationreweightsthedatatoprioritizemisclassifiedexamples,and
thefinalpredictionsareaggregatedusingaweightedmajorityvote. Themostwell-known
boostingvariant,AdaBoost[8],assignsweightstoclassifiersbasedontheirindividualper-
formance.
Recentresearchhasadvancedboostinginmultipledirections. Gradientboostingma-
chines(GBMs)[70]generalizeAdaBoostbyusinggradientdescentoptimizationoveraloss
function,yieldingstate-of-the-artperformanceinstructureddatatasks. Extremegradient
boosting(XGBoost)[71]furtherenhancescomputationalefficiencythroughparallelization
andregularizationtechniques,makingitwidelyusedinlarge-scaleapplicationssuchas
frauddetectionandrecommendationsystems.
Deepboostingmethods,suchasboostedconvolutionalneuralnetworks[17],integrate
boostingwithdeeplearningarchitecturestoimproverepresentationlearning. Additionally,
self-adaptiveboostingalgorithms[72]dynamicallyadjusthyperparametersduringtraining,
enhancingrobustnessagainstnoisydata. Theseadvancementshighlightthecontinuous
evolutionofboostingbeyondtraditionalensemblelearningparadigms.

Mathematics2025,13,587 10of49
Boosting operates by iteratively applying a weak learning algorithm to different
distributionsoftrainingexamplesandcombiningtheiroutputs. Fromagradientdescent
perspective,boostingisastagewisefittingprocedureforadditivemodels[64,70]. Ineach
iteration,gradientboostingperformsatwo-stepprocess: first,itidentifiesweaklearners
based on the steepest descent direction of the gradient, then it applies a line search to
determinethestepsize.
Theoriginalboostingmethod,calledboostingbyfiltering[4],reliesonPAClearning
theory and requires large amounts of training data. AdaBoost [8,73] was developed to
addressthislimitation. Boostingcanbedoneusingsubsampling,whereafixednumberof
trainingexamplesisdrawnandresampledbasedonaspecifiedprobabilitydistribution,or
usingreweighting,whereeachexampleisassignedaweightandallexamplesareusedto
traintheweaklearner,whichmusthandleweightedexamples.
Inbinaryclassification,theoutputofastrongclassifierH(x)isproducedbyaggregat-
ingtheweakhypothesesh (x)usingweightedcontributions:
t
(cid:32) (cid:33)
T
∑
H(x) =sign(f(x)) =sign α h (x) , (7)
t t
t=1
where T denotes the total number of iterations, and f(x) = ∑T α h (x) represents the
t=1 t t
strongclassifier. Toreducethelearningerror,thegoalistooptimizeh ateachboosting
t
iteration,whichinvolvesdeterminingtheappropriateconfidencelevelα .
t
Upperboundsontheriskforboostedclassifiersarederivedbynotingthatboosting
tendstomaximizethemarginfortrainingsamples[62]. Undercertainassumptionsabout
the underlying distribution, boosting can converge to the Bayes risk as the number of
iterationsincreasesindefinitely[74]. Whenusedwithaweaklearnerdefinedbyakernel,
boostingbecomesequivalenttoestimationusingaspecialboostingkernel[75].
Boostingdiffersfrombagginginthatitaddsmodelssequentially,focusingonmis-
classified instances, and it uses non-i.i.d. samples for training. Unlike bagging, where
thebaselearnersremainfixed,inboosting,thecommitteeofweaklearnersevolvesover
time,witheachlearnercastingaweightedvote. Inmanyscenarios,boostingoutperforms
baggingandisoftenpreferredasthemethodofchoice. Anexampleofaboostingvariant
isLearn++.NC[76]. However,boostingtendstoperformpoorlycomparedtobaggingin
noisyenvironments[77],asitfocusesnotonlyondifficultregionsbutalsoonoutliersand
noise[9].
Boostingtendstoperformwellandresistoverfitting[73,78],evenwhentheensemble
consistsofmanydeeptrees[12,19]. However,theriskofoverfittingincreaseswhenthe
number of classifiers becomes large [64]. By continuously adding weak classifiers, it
reducesthegeneralizationerrorevenafterthetrainingerrorreacheszero. Someresearch
has suggested that boosting can overfit, particularly in the case of noisy data [79,80].
Thoughboostingcaneventuallyoverfitwhenrunforanexcessivelylargenumberofsteps,
thisprocessisslow.
Whendecisiontreesserveasbaselearners,boostingcanautomaticallycapturecomplex
non-linearrelationships,discontinuities,andhigher-orderinteractions,makingitrobust
againstoutliers[81]. Tree-basedmodels,includingpopularalgorithmslikeXGBoost[71],
LightGBM [82], CatBoost [83], and random forests [20], often outperform deep neural
networksontabulardata[84,85].
AdaBoost
Theadaptiveboosting(AdaBoost)algorithm[8,73]isawidelyusedmethodinen-
semble learning. AdaBoost is theoretically capable of reducing the error of any weak
learner. Fromastatisticalperspective,AdaBoostcanbeseenasstagewiseoptimization

Mathematics2025,13,587 11of49
ofanexponentiallossfunction[64]. Fromacomputersciencestandpoint,generalization
errorboundsarederivedfromVCtheoryandtheconceptofmarginsinPAClearning[86].
AdaBoosthasbeenshowntooutperformotherclassifiers,suchasCART,neuralnetworks,
andlogisticregression,anditissignificantlysuperiortoensemblemethodscreatedvia
bootstrapsampling[3].
TheAdaBoostalgorithmtrainseachclassifierinsequence,usingtheentiredataset. It
adjuststhedistributionofthetrainingexamplesbasedonthedifficultyofclassification.
Ateachiteration,thealgorithmplacesgreateremphasisonmisclassifiedinstances,thus
focusingmoreonharder-to-classifyexamples. Theweightsofmisclassifiedsamplesare
increased,whilethoseofcorrectlyclassifiedsamplesarereduced. Additionally,classifiers
areweightedaccordingtotheirperformance,andtheseweightsareusedduringthetesting
phase. Whenanewinstanceisintroduced,eachclassifiercastsaweightedvote,andthe
finalpredictionismadebasedonthemajorityvote.
ConsideratrainingsetS = {(x,y ),i = 1,...,N} where y ∈ {−1,+1} represents
i i i
labelsdrawnfromi.i.d. samplesoftherandompair(x,y)followinganunknowndistribu-
tionP. AdaBoostaimstoconstructastrongclassifier f(x) = ∑T α h (x)thatminimizes
t=1 t t
aconvexlossfunction,specificallytheaverageofthenegativeexponentialofthemargin
y(x)f(x)overthetrainingsetS,givenasfollows:
J = 1 ∑ N e −yif(xi ) . (8)
N
i=1
TheAdaBoostalgorithmcancontinueaddingweaklearnersiterativelyuntilasufficiently
lowtrainingerrorisreached.
The AdaBoost algorithm is presented in Algorithm 1, where p denotes the data
t
distribution. Thegoalistoproduceaboostedclassifier H(x). Intheupdaterulefor p ,
t
−α y h (x) < 0 when y = h (x), and > 0 when y (cid:54)= h (x). This implies that after
t i t i i t i i t i
selectingthebestclassifier h forthedistribution p ,thecorrectlyclassifiedexamplesx
t t i
are given lower weights, while those incorrectly classified receive higher weights. In
thesubsequentround, theupdateddistribution p t+1 emphasizestheexamplesthatthe
previousclassifierfailedtoclassify,promptingtheselectionofanewclassifierthatfocuses
moreonthesedifficultinstances.
AdaBoostisaniterativecoordinatedescentalgorithmthatminimizesexponentialmar-
ginlossovertrainingdata[62,64,87],convergingasymptoticallytotheoptimalexponential
loss[88]andensuringstrongperformancewhenweakclassifiersareonlyslightlybetter
thanrandomguessing[8]. Thealgorithmguaranteesconsistencyifstoppedafter N1−(cid:101)
iterationsforsamplesizeNand(cid:101) ∈ (0,1),leadingtheerrorprobabilitytowardstheBayes
risk[89]. Itsconvergenceratetotheexponentiallossminimumisshownin[90],requiring
C/(cid:101) iterations to achieve exponential loss within (cid:101) of the optimal, with a lower bound
ofW(1/(cid:101))roundsfornear-optimalperformance. However,AdaBoostcanoverfitnoisy
datasetsduetoitspenaltyonmisclassifiedsampleswithlargemargins,makingitsensitive
tooutliers.
While AdaBoost identifies a linear separator with a large margin [62], it does not
alwaysconvergetothemaximalmarginsolution[91]. Withweaklearnability, thedata
becomelinearlyseparable[73],andwithshrinkage,AdaBoostasymptoticallyconvergesto
anL -margin-maximizingsolution[91]. AdaBoost∗ [91]convergestothemaximalmargin
1
solutioninO(log(N)/(cid:101)2)iterations,apropertysharedbyalgorithmsin[92]forlinearly
separabledata. ThesemethodshavebeendevelopedformaximizingL margins[92].
1

Mathematics2025,13,587 12of49
Algorithm1:TheAdaBoostalgorithmforboostingweakclassifiers.
1,fori
| 1. Initializethedistribution: | p (i) = | =1,...,N. |     |     |
| ----------------------------- | ------- | --------- | --- | --- |
1 N
=1toT:
2. fort
| (a) Selectaweaklearnerh    | basedonthecurrentdistribution |                | p :                 |     |
| -------------------------- | ----------------------------- | -------------- | ------------------- | --- |
|                            | t                             |                | t                   |     |
| • Computetheweightederror: |                               | (cid:101) = ∑N | p (i);              |     |
|                            |                               | t i=1,yi       | (cid:54)=ht (xi ) t |     |
=argmin
| • Findtheweakclassifierthatminimizestheerror: |        |     | h t | hj (cid:101) t . |
| --------------------------------------------- | ------ | --- | --- | ---------------- |
| (b) if(cid:101) ≥0.5,stopandsetT              | ← t−1; |     |     |                  |
t
(cid:16) (cid:17)
|                                      |     | 1ln   | 1−(cid:101)t |     |
| ------------------------------------ | --- | ----- | ------------ | --- |
| (c) Computetheweightoftheclassifier: |     | α t = | ;            |     |
|                                      |     | 2     | (cid:101)t   |     |
(d) Updatethedistributionforthenextround:
|     | (i) =   | (i)e −αtht (xi )yi, | =1,...,N; |     |
| --- | ------- | ------------------- | --------- | --- |
|     | p t+1 p | t                   | i         |     |
p ( i )
|     | (i) = | t+ 1 | =1,...,N. |     |
| --- | ----- | ---- | --------- | --- |
|     | p t+1 | ,    | i         |     |
∑N p (j)
j= 1 t + 1
3. Outputthefinalclassifier:
|     |     | (cid:32) | (cid:33) |     |
| --- | --- | -------- | -------- | --- |
T
|     | H(x) =sign | ∑     | (x) |     |
| --- | ---------- | ----- | --- | --- |
|     |            | α t h | t . |     |
t=1
FloatBoost[93]reduceserrorbybacktrackingaftereachAdaBoostiteration,targeting
errorminimizationratherthanexponentialmarginloss,requiringfewerclassifierswith
lowererrorratesbutlongertrainingtimes. MultBoost[94]allowsforparallelizationof
AdaBoostinbothspaceandtime. LogitBoost[64]optimizeslogisticregressionlossfor
classification tasks [95], and LogLoss Boost [88] minimizes logistic loss for inseparable
data. SmoothBoost [96] limits sample weight to avoid overfitting, with noise tolerance
comparabletotheonlineperceptronalgorithm.
AdaBoost.M1andAdaBoost.M2[8]extendAdaBoosttomulticlassclassification. Ad-
aBoost.M1 stops if the weak classifier error exceeds 50% [62], while AdaBoost.M2 uses
pseudolosstocontinueiftheclassifierisslightlybetterthanrandomguessing.AdaBoost.M2
alsointroducesamislabeldistributiontofocusondifficultormisclassifiedexamples.
For multilabel classification, AdaBoost.MH [87] and AdaBoost.LC [97] extend Ad-
aBoost,withAdaBoost.MHoptimizingHamminglossandAdaBoost.LCminimizingcov-
eringloss[97]. SAMME[98]isanothermulticlassextension,optimizingexponentialloss
forweightedclassification. SM-Boost[99]improvesrobustnesstonoiseusingstochastic
decisionrulesandgradientdescentinthefunctionspaceofbaselearners.
AdaBoostReg[79]andBrownBoost[100]preventoverfittingbylimitingfunctionclass
complexity. BrownBoostdampenstheinfluenceofhard-to-learnsampleswithanerror
functionasamargin-basedlossfunction,whileeta-boost[101]strengthensrobustnessto
mislabelsandoutliers. AdaBoost’sselectionofweaklearnersbasedontrainingerrormay
strugglewithsmalldatasets,buterror-degree-weightedtrainingerror[102]addressesthis
byconsideringsampledistancesfromtheseparatinghyperplane.
AdaBoost.R[8]adaptsAdaBoost.M2forregressiontasks,whileAdaBoost.RT[103]
filtersexampleswithhighestimationerrorsbeforeapplyingAdaBoost. Cascadeddetec-
tors[104]useAdaBoosttobalancedetectionrateandfalsepositivesinasequenceofstages
withprogressivelystrongerclassifiers. FCBoost[105]extendsAdaBoostbyminimizing
a Lagrangian risk for classification accuracy and speed, optimizing the cascade config-

Mathematics2025,13,587 13of49
urationautomatically. Itiscompatiblewithcost-sensitiveboosting[106],ensuringhigh
detectionrates.
L -Boosting[78]minimizes L lossinastepwisemanner,ensuringconsistency[89]
2 2
and resistance to overfitting [78], making it popular for regression [107]. However, its
convergencerateisslowduetolinearstepsizedetermination. Forsparsefunctions,itsrate
followsO(k−0.37),wherekrepresentsthenumberofiterations[108]. ε-Boosting[109],RS-
Boosting[110],andRTBoosting[111]offerimprovementsinstepsizeselection,improving
convergenceovertraditionalgradientboosting. RBoosting[112]acceleratesconvergence
andenhancesperformance,achievingnear-optimalconvergenceratesandsuperiorgener-
alizationcomparedtostandardboosting.
8. RandomForestsandDecisionForests
Decision trees are a fundamental approach for classification and regression tasks,
valuedfortheirsimplicityandinterpretability. Theyperformwellandoffercleardecision
rules in the form of if–then statements along paths from the root to the leaf. A notable
implementationisC4.5[113]. However,definingaglobalobjectiveforoptimallylearning
decisiontreesischallenging. TreescanbeconstructedusingcriterialikeGiniimpurity[114]
andinformationgain[113].
TheC4.5algorithmtakesasetofcasesrepresentedbyann-dimensionalfeaturevector,
where each case is preclassified into one of the target classes. It generates classifiers as
decisiontrees,whereeachnoderepresentsafeature,branchesconnectfeaturevalues,and
leavesdenotetheclass. Toclassifyaninstance,onetracesthepathfromtherootnodeto
theleaf. C4.5usesadivide-and-conquerstrategytobuildaninitialtreebasedonagiven
setSofinstances.
TheCARTmethod[114]usesabinaryrecursivepartitioningtechniqueforclassifyinga
dataset. CARToperatesgreedily,choosingthebestsplitateachnodetominimizeimpurity,
with the goal of producing a series of increasingly refined trees. The ideal tree size is
determinedbyevaluatingthepredictiveperformanceofallprunedtrees.
Aforestisagraphwithconnectedcomponentsthataretrees. Randomforest,anen-
sembletechnique,buildsupontheconceptofbaggingbygeneratingmultipledecisiontrees.
Thesetreesaretrainedusingrandomlyselectedsubsetsoffeatures[20]orinstances[12].
Decisionforests,includingrandomforestsandgradient-boosteddecisiontrees(GB-
DTs)[70],aretypicallycomposedofensemblesofaxis-aligneddecisiontreesthatpartition
thefeaturespacealongindividualdimensions.
8.1. RandomForests
Arandomforest[12]isanensembleofclassificationtrees,allofwhicharegrownusing
apartitioningruleandtrainedonbootstrapsamplesfromthedataset. Themethodaimsto
enhancevariancereductioncomparedtobaggingbyminimizingthecorrelationbetween
treeswithoutsignificantlyincreasingbias. Thisisachievedbyrandomlyselectinginput
variablesduringthetree-buildingprocess. Similartobagging,thebiasofarandomforest
equalsthebiasofindividualtrees. Predictionismadethroughamajorityvoteamongall
trees,meaningimprovementsinpredictionarepurelyduetovariancereduction. Beyonda
certainnumberoftrees,addingmoredoesnotenhanceperformance[12].
Numerousexperimentsshowthatincreasingthenumberoftreesstabilizespredictions,
while other tuning parameters impact model accuracy [115–117]. The accuracy of tree
ensembles is bounded by a function of the trees’ strength and diversity [12]. Random
forestsenhancetreediversitybyusingrandombootstrapsamplesforeachtreeandlimiting
the selection of the splitting dimension j to a random subset of the p total dimensions.
Asthenumberoftreesincreases,thegeneralizationerrorconverges,withanestablished

Mathematics2025,13,587 14of49
upperbound[12]. Eachbootstrapsampleformsaclassificationtreewithoutpruning,and
predictionsaremadeviamajorityvoteforclassificationoraveragingforregression.
Empiricalresultsshowthatrandomforestsconsistentlyoutperformmostmethods
inpredictiveaccuracy[118]. Moreover,randomforestsexhibitstrongresiliencetoboth
outliersandnoiseindatasets,makingthemareliablechoiceforvariousapplications[12,19].
Randomforestsoperateinbatchmode,andtheprocedureisdetailedinAlgorithm2.
Theconvergencepropertiesandratesofrandomforestshavebeenextensivelystud-
ied [119–121], along with methods for estimating prediction standard errors [122,123].
Consistencyisestablishedundertheassumptionthatthetrueregressionfunctionisad-
ditive[124],thoughtheoreticalstudiesontheirasymptoticbehavioroftenrelyonstrong
assumptionsandyieldsuboptimalrates[124–126]. Purelyrandomforests,basedondata-
independenthierarchicalpartitions,offerasimplerframeworkfortheoreticalanalysis[119].
Mondrianforestsachieveminimax-optimalratesbytuningtheircomplexityparameter
andutilizingrecursiveaxis-alignedpartitioning,efficientMarkovconstruction,andself-
consistency,makingthemsuitableforonlinelearning[127,128]. Minimaxoptimalityhas
alsobeenextendedtorandomforestswithgeneralsplitdirections[129].
Algorithm2:Outlineoftherandomforestalgorithm.
1. GenerateBdecisiontreesbydrawingnbootstrapsamplesfromtheoriginal
dataset.
2. Foreachbootstrapsample:
(a) Buildaclassificationorregressiontree.
(b) Ateachtreenode:
• Randomlyselectmpredictorvariablesfromthefullsetofpredictors.
• Identifythepredictorvariableamongtheselectedmthatresultsin
thebestsplitanduseittodividethedata.
• Repeatthisprocessatsubsequentnodes,withanewrandomselec-
tionofmvariablesateachstep.
3. Foranewdataset,classifyinstancesbytakingthemajorityvote(classification)
oraveragingpredictions(regression)acrossallBtrees.
RandomforestsarecompetitivewithSVMsinclassificationtasks,offeringanunbiased
internalestimateofgeneralizationerrorwhilehandlingmissingdataeffectively. Theyalso
estimatetherelativeimportanceofinputfeaturesandcanbeformulatedaskernelmethods,
enhancinginterpretabilityandenablinganalyticalevaluation[130]. Asbaselearnersfor
regressiontasks,theyimplicitlyconstructkernel-likeweightingfunctionsfortrainingdata.
Anextensionproposedin[131]generalizesrandomforeststomultivariateresponsesby
leveragingtheirjointconditionaldistribution,independentofthetargetdatamodel.
A unified framework for estimating prediction error in random forests introduces
an estimator for the conditional prediction error distribution function, with pointwise
uniformconsistencydemonstratedforanenhancedversion[132]. Misclassificationerrorin
randomforestsshowslowersensitivitytovariancethanmeansquarederror(MSE),and
overfittingtendstooccurslowlyornotatall,similartoboosting.Themethodfunctionsasa
robustadaptiveweightedversionofthek-NNclassifier,leveragingforest-inducedweights
rather than averaging individual tree estimates [133]. Variance estimation for bagged
predictorsandrandomforestsreliessolelyonthebootstrapsamplesusedforpredictions,
withmoderatecomputationalcost. Forbagging,convergencerequiresB =O(N)bootstrap
replicates,whereNisthetrainingsetsize[123].

Mathematics2025,13,587 15of49
Thecomputationalefficiencyofrandomforestsheavilydependsonthecomplexityof
thesplittingstep. Toimproveruntime,approximationsofthesplittingcriterionareused,
includingdensityestimationthataggregatesCARTcriteriaforvariousresponsetransfor-
mations[134]andtheaggregationofstandardunivariateCARTsplittingcriteria[135,136].
Randomforestsinherentlyexhibitbias, withtheoreticalboundsestablishedunder
assumptionsaboutthetree-growingprocessanddatadistribution[125]. Buildingonthis,
GhosalandHooker[137]exploreabiascorrectionmethodfirstsuggestedby[138],concep-
tuallyakintogradientboosting[70],andfurtheranalyzedin[139]. Anotherapproachto
mitigatingbias[140]adaptstraditionalbootstrapbiasestimationforgreatercomputational
efficiency.
Extensions of random forests to quantile regression include quantile regression
forests[141],whichenableconsistentconditionalpredictionintervals. Generalizedrandom
forests[142]furthersupportquantileregression,emphasizingheterogeneityinthetarget
metric. Predictionintervalscanalsobecomputedusingempiricalquantilesofout-of-bag
predictionerrors[143]. Moregenerally,conformalinferenceprovidesaflexibleframework
forestimatingpredictionintervals,applicabletonearlyanyregressionestimator,including
randomforests[144,145].
Conventionalrandomforestsassignequalweightstoalltrees. Alternativeweighting
strategiesincludetreeweightingbasedonout-of-bagaccuracy[146]ortree-levelprediction
errors[147]. Forregression,optimalweightingalgorithms[148]asymptoticallymatchthe
squaredlossandriskofthebest-weightedrandomforestsundercertainregularityconditions.
8.2. RecentAdvancesinRandomForests
WildWood[149]enhancesrandomforestsbyaggregatingpredictionsfromallsubtrees
usingexponentialweightsviathecontexttreeweightingalgorithm. Thismethod,com-
binedwithhistogram-basedfeaturebinningsimilartoXGBoost[71],LightGBM[82],and
CatBoost[83],significantlyimprovescomputationalefficiency,makingitcompetitivewith
extremegradientboostingalgorithms. Inspiredbysubtreeaggregationwithexponential
weights[150],WildWoodleveragesout-of-bagsamplesforweightcomputation,naturally
mitigatingoverfittingwithoutrelyingonheuristicpruningmethods[113]. Forcategorical
features,itappliesexponentialweightaggregationinsteadofCatBoost’stargetencoding
topreventoverfitting. Additionally,byadoptingbootstrap-basedsamplesplittingfrom
honestforests[125],WildWoodensuresrobustpredictions. Withfewhyperparametersto
tune,itintegrateshistogram-basedaccelerationandadaptssubtreeaggregationforbatch
learning,achievingstrongperformanceacrossvarioustasks.
FrechettreesandFrechetrandomforests[151]extendrandomforeststoheterogeneous
datatypes,includingcurves,images,andshapes,whereinputandoutputvariableslie
in general metric spaces. These methods introduce a novel node-splitting technique,
generalize prediction procedures, and adapt out-of-bag error estimation and variable
importancescoring. AconsistencytheoremfortheFrchetregressogrampredictorusing
data-drivenpartitionsisalsoestablishedandappliedtopurelyrandomtrees.
Markowitzrandomforest[152]introducesatree-weightingmethodthatconsiders
bothperformanceanddiversitythroughatreecovariancematrixforriskregularization.
Inspiredbyfinancialoptimization,thisapproachappliestobinaryandmulti-classclassifi-
cationaswellasregressiontasks. Experimentson15benchmarkdatasetsdemonstratethat
theMarkowitzrandomforestsignificantlyoutperformsprevioustree-weightingmethods
andotherlearningapproaches.

Mathematics2025,13,587 16of49
8.3. DecisionForests
Fordecisionforests,thesplitsofaxis-aligneddecisiontreesparalleltothecoordinate
axes limit the ability to capture feature dependencies, often necessitating deeper trees
withcomplex, step-likedecisionboundaries. Thiscanincreasevarianceandtheriskof
overfitting,particularlywhendataclassesarenotseparablealongsingledimensions.
Toaddresstheselimitations,methodssuchasforest-RC(randomizedcombination),
whichemployssplitsbasedonlinearcombinationsoffeatures[12],andoblique-splitting
randomforests[153–155],havebeenintroducedtoimproveempiricalperformance. Addi-
tionally,sparseprojectionshavebeendevelopedtoreducethecomputationalcostassociated
withobliquesplits[156].
The random subspace method [11] selects random feature subsets for training, as
seen in random forests and bootstrap-based techniques [157]. It can also be viewed as
an axis-aligned random projection approach [158]. Extensions include boosting [159]
andsparseclassificationensembles,whereweaklearnersaretrainedinoptimallychosen
subspaces[160].
Severalextensionstodecisionforestsintroduceaxis-obliquesplits,suchasrandom
rotation random forests [154] and canonical correlation forests [155]. These oblique ap-
proaches,oftenreferredtoasobliquedecisionforests,allowforsplitsbasedoncombinations
offeaturedimensions,enhancingflexibility. However,theymaysacrificesomeofthead-
vantageouspropertiesofaxis-alignedforests,suchasinterpretabilityandcomputational
simplicity. Treesthatuseobliquesplitsarealsoknownasbinaryspacepartitioningtrees.
Therandomrotationrandomforestmethod[154]appliesuniformrandomrotations
tothefeaturespacebeforetrainingeachtree. Thisadjustmentenablesobliquedecision
boundaries,increasingtheensemble’sflexibility. Followingrotation,standardaxis-aligned
procedures are used to train the trees. A regularized variant of the random rotation
method [161] encourages simpler base models. Canonical correlation forests [155] use
canonicalcorrelationanalysis(CCA)ateachsplittodeterminedirectionsthatmaximize
correlationwithclasslabels. Randomprojectionmethods[158,162,163]trainbaseclassifiers
inlow-dimensionalsubspacesderivedfromrandomprojections. Forexample,random
projectionforests[164]utilizerandomprojectionstocompressimagefilterresponses,while
forest-RC [12] uses univariate projections and often outperforms random forests [165].
Rotationforests[13]utilizeK-axisrotationstogeneratenewfeaturesfortrainingmultiple
classifiers,enhancingsplitsthroughtheapplicationofprincipalcomponentanalysis(PCA).
Sparse projection oblique randomer forests (SPORF) [156] improve on both axis-
aligned and oblique decision forests through very sparse random projections, offering
betterperformanceandscalabilitywhilepreservinginterpretability. Thesparseprojection
frameworkcanalsobeextendedtoGBDTsforsimilargains.
8.4. Gradient-BoostedDecisionTrees
Gradientboosting[64,70]commonlyemploysdecisiontreesasbaselearners,forming
arobustmodelbysequentiallyaggregatingthem. Acceleratedgradientboosting[166],in-
spiredbyNesterov’saccelerateddescent[70],enhancesperformancebyreducingsensitivity
totheshrinkageparameterandproducingsparsermodelswithfewertrees.
GBDTs[70]buildadditivemodelsbyiterativelycombiningsmall,shallowdecision
trees,knownasweaklearners. Eachiterationtrainsanewtreetoapproximatetheresiduals
between the true labels and the current predictions, addressing errors from previous
iterations. Thisstage-wiseprocessoptimizesacostfunctionusinggradientdescent[70,167].
GBDTsareawidelyusedensemblelearningmethodforregressionandclassification.
ThepopularityofGBDTsstemsfromtheirstrongpredictiveperformance,computational
efficiency,andinterpretability. Theiradoptionhasbeenfurtheracceleratedbyfast,scal-

Mathematics2025,13,587 17of49
able, open-source tools like XGBoost [71], LightGBM [82], and CatBoost [83]. XGBoost
improvesaccuracybyutilizingsecond-ordergradientinformationtorefinetheboosting
process. LightGBMsignificantlyenhancestrainingspeedthroughhistogram-basedgra-
dientaggregation. CatBoostintroducesaspecializedtechniqueforhandlingcategorical
featuresefficiently.
Forbothtrainingandinference,GBDTimplementationssuchasXGBoostandLight-
GBMoperatewithlineartimecomplexityconcerningthenumberofbins,inputfeatures,
outputdimensions,andboostingiterations.
GBDTs are highly effective, often surpassing deep learning models and other tra-
ditionalalgorithmsontabulardata[83,168],includingneuralobliviousdecisionensem-
bles[168]. Representerpointmethods[169]providemoreefficientmodelinterpretation,
representingitasthesumofcontributionsfromalltrainingpoints,groundedinrepresen-
tertheorems.
TracIn [170] focuses on estimating the influence of training examples throughout
the learning process rather than just analyzing the final model’s properties. Influence
estimationhasbeenextendedfromdeeplearningmodelswithcontinuousparametersto
GBDTs[171]. TREX[171],basedonrepresenter-pointmethods[169],andBoostIn[171],an
efficientinfluence-estimationmethodforGBDTsinspiredbyTracIn[170],offersignificant
performance improvements. BoostIn is notably four orders of magnitude faster while
maintainingorexceedingtheaccuracyofexistingmethods[171].
GBDT models have been extended for multi-output learning [172–174], with tree
leaves predicting all or subsets of outputs to optimize aggregate objective gains [174].
Privilegedinformationhasalsobeenintegratedtoiterativelyrefinepredictions,guiding
updatesviaauxiliaryfunctionsthatadjustresiduals[175].
8.5. Adaboost,GBDTsVersusRandomForests
AdaBoost’sbehaviorpuzzledstatisticiansduetotwonotableproperties: interpola-
tionisachievedwithinrelativelyfewiterations,yetthegeneralizationerrorcontinuesto
improvebeyondthispoint. Fromastatisticalperspective,AdaBoostperformsstagewise
optimizationofanexponentialloss,necessitatingregularizationoftreesizeandcontrol
overiterationcount. Conventionalwisdomsuggestsusingearlystoppingorlimitingitto
low-complexitylearners.
Randomforests, bycontrast, growtreesindependentlyandoptimizelocalcriteria,
suchastheGiniindex, withoutagloballossfunction. Asanensembleofinterpolating
classifiers,randomforestsperformwellwithlargetreesandextensiveiterations. Inmany
cases,randomforestsperformsimilarlytoboostingbutareeasiertotrainandtune,making
themawidelyusedmethodinvariousapplications.
GBDTsfundamentallydifferfromAdaBoost,addressinganinfinite-dimensionalop-
timizationproblemthatdrivestheirstrongperformance. Unlikerandomforests,which
growtreesindependentlyandcombinetheminparallel,GBDTsconstructtreessequentially,
progressivelyenhancingpredictionaccuracy. Despitethesemethodologicaldifferences,
both GBDTs and random forests achieve success through weighted ensembles of inter-
polating classifiers that adapt to local decision boundaries, often yielding comparable
performance[19].
BreimanspeculatedthatAdaBoost, initslaterstages, mimicsarandomforest[12].
AdaBoosthasbeencharacterizedasaweightedensembleofclassifiersthatinterpolatesthe
trainingdata[19]. Initslateriterations,thealgorithmexhibitsanaveragingeffect,leading
tobehavior thatclosely resemblesthat ofa randomforest [19]. Ithas beenarguedthat
boostingmethods,likerandomforests,aremosteffectivewhenemployinglargedecision
trees and avoiding both regularization and early stopping [19]. In this interpretation,

Mathematics2025,13,587 18of49
AdaBoostcanbeseenasa“randomized”forestofforests,wheretheindividualtreesin
randomforestsandtheensemblesinAdaBoostbothachieveerror-freeinterpolationofthe
trainingdata[19].
Thisinterpolationintroducesrobustnesstonoise: whenclassifiersfitdataverylocally,
noiseinoneregionhasminimalinfluenceonpredictionsinneighboringareas. Training
models with deep trees and averaging their outputs inherently prevents overfitting by
maintaininglocalinterpolationproperties[19].BothrandomforestsandAdaBoostleverage
thismechanism,reducingoverfittingasthenumberofiterationsincreaseswhilepreserving
predictiveaccuracy.
WildWood [149] bridges the gap between traditional random forests and modern
boostingtechniques,offeringablendofefficiency,robustness,andinterpretability. This
method might pave the way for new innovations in ensemble learning and machine
learningalgorithms.
9. ComparisonofEnsembleMethods: ComputationalTrade-Offs
Randomforest[12]isanensemblelearningmethodthatconstructsmultipledecision
treesusingbootstrappedsamplesoftrainingdataandrandomlyselectedsubsetsoffeatures.
Thefinalpredictionisobtainedthroughmajorityvoting(classification)oraveraging(regres-
sion). Theadvantageofrandomforestliesinitsrobustnesstooverfittinganditsabilityto
handlehigh-dimensionaldata.Recentadvancementsincludeadaptationssuchasextremely
randomizedtrees(extra-trees)[176]andweightedfeatureselectiontechniques[120].
Bagging[3]isamethodthattrainsmultiplebaselearnersindependentlyondifferent
bootstrappedsubsetsofthedatasetandaggregatestheirpredictions. Iteffectivelyreduces
varianceandimprovesstability,particularlyforhigh-variancemodelslikedecisiontrees.
Bagging-based techniques such as random forests have been widely used due to their
improvedgeneralizationcapabilities. Computationally,baggingisparallelizable,makingit
efficientforlarge-scalelearning[60].
Boosting[4,8]isaniterativeensembleapproachthatsequentiallytrainsweaklearners,
witheachlearnerfocusingonmisclassifiedinstancesfromthepreviousiteration.Prominent
algorithmsincludeAdaBoost[8],gradientboosting[70],andtheirmodernextensionslike
XGBoost[71]andLightGBM[82]. Boostingachieveshighaccuracybutiscomputationally
moreexpensivethanbaggingduetoitssequentialnature.
Table1providesanoverviewofkeyensembletechniques,theirstrengths,weaknesses,
andcommonapplications.
Understanding the computational and storage complexities of ensemble methods
is crucial for selecting an appropriate approach based on resource availability. Table 2
summarizesthetrade-offsamongkeyensembletechniques.
Table2.Computationalandstoragecomplexityofpopularensemblelearningmethods.
Method TrainingComplexity InferenceComplexity StorageRequirement
Bagging O(BTdlogd) O(Bd) O(BTd)
Boosting O(Tdlogd) O(Td) O(Td)
RandomForests O(BTdlogd) O(Bd) O(BTd)
XGBoost O(Tdlogd) O(Td) O(Td)
Notation:Brepresentsthenumberofbaselearners(treesforbaggingandrandomforests),Tdenotesthenumber
ofboostingrounds(forboostingandXGBoost)orthenumberofdecisionnodespertree(forbaggingandrandom
forests),anddistheinputfeaturedimensionality.
Baggingmethodssuchasrandomforestsbenefitfromparallelization,makingthem
morescalableforlargedatasets[12]. Theytrainbasemodelsindependently,makingthem
highly parallelizable, but they require large storage for all base learners [12]. They are

Mathematics2025,13,587 19of49
effectiveinreducingvarianceandarerobusttooverfitting,buttheyrequiresubstantial
storageandtrainingtime[12].
Incontrast,boostingmethodssuchasAdaBoostandXGBoostexhibithighercomputa-
tionalcostsduetotheirsequentialtrainingnaturebutoftenachievesuperioraccuracy[71].
Boostingissequentialandcanbemorecomputationallyexpensive,butitoftenachieves
higheraccuracywithfewerbaselearners[8]. Boostingmethodsexcelinreducingbiasbut
aresensitivetonoisydataandrequirecarefultuning[4].
Forlarge-scaleapplications,baggingispreferredduetoitsparallelizablenature,while
boostingcanbeprohibitiveinreal-timeenvironments[60]. Randomforestsscalewellto
largedatasets,whereasboostingcanbecomputationallyintensiveasthenumberofweak
learnersgrows[70].
Stackingaddsanotherlayerofcomplexitybyrequiringanadditionalmeta-learner,
makingbothtrainingandinferenceslowerthansimplerensembles[25]. Stackingisuse-
fulwhendiversemodelscontributecomplementarystrengths,butitiscomputationally
expensiveandpronetooverfittingwithoutsufficientregularization[7].
10. SolvingMulticlassClassification
Atypicalapproachtohandlingmulticlassclassificationtasksinvolvesconstructing
multiplebinaryclassifiersandintegratingtheiroutputs. ECOCsprovideaversatileframe-
workforcombiningthesebinaryclassifierstosolvemulticlassproblemseffectively[38].
10.1. One-Against-AllStrategy
Theone-against-allapproachisoneofthesimplestandmostcommonlyusedstrategies
formulticlassclassificationwithK classes(K > 2). Inthismethod,eachclassistrained
againstthecombinedsetofallotherclasses. Fortheithbinaryclassifier,theoriginalK-class
trainingdataarelabeledaseitherbelongingtoornotbelongingtoclassiandareusedfor
training. Asaresult,Kbinaryclassifiersarecreated,eachrequiringtrainingontheentire
dataset. However,thismethodmaystrugglewithdistinguishingbetweenclassesandcan
leadtoimbalanceddataissues.
Inthisframework,wedefineKdirectdecisionfunctions,eachofwhichseparatesa
singleclassfromtherest. LetD(x)bethedecisionfunctionforclassi,whichmaximizes
i
themarginseparatingitfromtheotherclasses. Onthedecisionboundary,D(x) =0. To
i
avoidunclassifiableregions,asdepictedinFigure1,adatasamplexisassignedtotheclass
correspondingtothemaximumvalueofD i (x),i.e.,i =argmax i=1,...,K D i (x).
D(x ) = 0
1
x
2 Class 1
Class 2
D(x ) = 0
3
Class 3
D(x ) = 0
2
x
1
Figure1.Regionsthatcannotbeclassifiedbytheone-against-allapproach.
10.2. One-Against-OneStrategy
The one-against-one (pairwise voting) approach helps mitigate the unclassifiable
regionsthatariseintheone-against-allmethod,althoughsomeunclassifiableregionsstill
persist. Intheone-against-onestrategy,decisionfunctionsaredeterminedforallpossible
class pair combinations. For each class pair, the training data are restricted to the two

Mathematics2025,13,587 20of49
classesinvolved,reducingtheamountofdatausedineachtrainingsessioncomparedto
theone-against-allmethod,whichutilizestheentiredataset. Theone-against-onestrategy
requirestrainingK(K−1)/2binaryclassifiers,whiletheone-against-allstrategyonlyneeds
K. Tomakeafinaldecision,theoutputsofallK(K−1)/2classifiersmustbecombined
using majority voting. This results in significant computational complexity, especially
whenKislarge.
LetD (x)representthedecisionfunctionforclassiagainstclassj,withthemaximum
ij
margin. ItholdsthatD (x) = −D (x). Theregions
ij ji
R = {x| D (x) >0,j =1,...,K,j (cid:54)=i}, i =1,...,K (9)
i ij
do not overlap. If x ∈ R, it is classified as belonging to class i. However, there is a
i
possibilitythatxdoesnotbelongtoanyoftheregionsR. Insuchcases,weclassifyxby
i
employingavotingmechanism. Thisisdonebycalculating
K
∑
D(x) = sign(D (x)), (10)
i ij
j=1,j(cid:54)=i
andassigningxtotheclassk =argmax i=1,...,K D i (x).
Ifx∈ R,thenD(x) = K−1andD < K−1forallj (cid:54)=i,meaningthatxiscorrectly
i i j
classified. However,ifanyD(x) (cid:54)= K−1,thenmultipleclassesmaybepossible,makingx
i
unclassifiable. InFigure2,theshadedarearepresentstheunclassifiableregion,whichis
significantlysmallercomparedtotheone-against-allapproach.
D (x ) = 0
12
x
2 Class 1
Class 2
D (x ) = 0
13
Class 3
D (x ) = 0
23
x
1
Figure2.Regionswhereclassificationisambiguousintheone-against-oneapproach.
Toaddressunclassifiableregionswhilemaintainingthesameclassificationoutcomes
astheconventionalone-against-onemethodinclassifiableregions,themembershipfunc-
tionisintroduced,similartotheone-against-allapproach. Theall-and-onemethod[177]
combinesone-against-allandone-against-onestrategies,partiallymitigatingtheirrespec-
tiveweaknesses.
Avariationoftheone-against-onestrategyisfoundindirectedacyclicgraphSVM
(DAGSVM) [178]. While the training process is identical to that of the one-against-one
method,thetestingphaseutilizesarootedbinarydirectedacyclicgraphwithK(K−1)/2
internalnodesandKleaves,requiringtheevaluationofonlyK−1binaryclassifiers.
ThemulticlasssmoothSVM[179]implementsaone-versus-one-versus-restscheme,
breakingtheproblemintoK(K−1)/2ternaryclassificationsubproblemsbasedonternary
votinggames. Thisapproachoutperformsboththeone-against-oneandone-against-rest
methodsacrossalldatasets.
10.3. Error-CorrectingOutputCodes
In the ECOC framework, the process begins with the creation of binary problems
bypartitioningclasses,whicharethenlearnedbyabaseclassifier. Thesepartitionsare

Mathematics2025,13,587 21of49
encodedintothecolumnsofacodingmatrixQ,whereeachrowrepresentsacodewordthat
encodesaspecificclass. Duringthedecodingphase,anewtestsampleisprocessed,and
acorrespondingcodewordisgeneratedbasedontheresultsofthebinaryproblems. The
codewordthatmostcloselyresemblesthetestsampleisidentifiedusingadistancemetric
suchasHammingorEuclideandistance. IftheminimumHammingdistancebetweenany
pairofcodewordsist,thenupto(cid:98)(t−1)/2(cid:99)single-biterrorsinQcanbecorrected,where
(cid:98)a(cid:99)denotesthelargestintegerlessthanorequaltoa.
Incontrasttosimplevotingprocedures,theECOCmethodsharesinformationamong
classestomakeamoreaccurateclassificationdecision,whichhelpsmitigateerrorsstem-
mingfromvarianceandbiasintheindividuallearners[180].
InabinaryECOCsetup,eachentryinthecodingmatrixQtakesvaluesfromtheset
{+1,−1}. Thismeansthateachdichotomizertreatsclassesaspartofoneoftwopossi-
blepartitions. Commonbinarycodingschemesincludetheone-against-allstrategyand
the dense random strategy [38], which require N and 10log N dichotomizers, respec-
2
tively[181].
IntheECOCframework,theclassificationtaskisdividedintosubtaskshandledby
binaryclassifiers. Eachclassifier’soutputiscombinedusingacodingmatrixQ= [q ]of
ij
sizeK×L,whereK isthenumberofclassesand Listhenumberofbaselearners(with
outputsd ,j =1,...,L). Thefinalclassificationisdeterminedbythehighestvote,
j
L
∑
y = q d , (11)
i ij j
j=1
wherey istheaccumulatedvoteforclassi.
i
In ternary ECOCs [181], the coding matrix Q uses symbols +1, −1, and 0, where
0indicatesthataclassisexcludedfromthelearningprocessofaparticularclassifier. This
ternaryframeworkintroducesabroadersetofbinaryclassificationtasks,promptingthede-
velopmentofproblem-specificdesignsanddecodingstrategies[182–184].Commonternary
ECOCdesignsincludeone-against-one[185],one-versus-all,andsparserandomstrate-
gies[181]. Theone-against-onestrategyinvolvesallclasspairs,resultinginK(K−1)/2
binary classifiers. The sparse random design introduces the 0 symbol with a different
probability,yieldingacodeoflength15log K[181]. Additionally,thediscriminantECOC
2
approach[184]uses N−1classifiers,where N−1binarytreenodesareencodedasdi-
chotomizersinaternaryproblem-dependentECOCscheme.
IntheECOCframework,theone-against-onecodingdesigntypicallyoutperforms
othercodingschemesinreal-worldmulticlassproblems[182]. Anotablefeatureofthis
approachisthehighsparsityofthecodingmatrix,withmanypositionsbeingfilledwith
zeros. Thisintroducestwotypesofbias,whichnecessitateadjustmentstothedecoding
procedure[182]. Toaddressthesebiases,anewdecodingmeasureandtwostrategiesare
proposed. Thesestrategiesensurethatallcodewordsoperatewithinthesamedynamic
range,leadingtosignificantimprovementsinECOCperformance[182]. TheECOCframe-
workhasbeenextendedtoonlinelearningscenarios[186],wherethefinalclassifieradapts
totheintroductionofnewclasseswithoutrequiringchangestothebaseclassifier. Online
ECOCmethodsconvergetotheresultsofbatchapproacheswhileprovidingarobustand
scalablesolutionforincorporatingnewclasses.
IntheECOCapproach,error-correctingcodewordsareutilizedtoenhanceclassifi-
cationaccuracy. Whilethesecodewordsexhibitstrongerror-correctingproperties,some
of the generated subproblems can be challenging to solve [181]. Simpler methods like
one-against-allandone-against-oneoftenyieldcomparableorevenbetterresultsinvarious

Mathematics2025,13,587 22of49
applications than the more complex ECOC approach. Additionally, the ECOC method
requiresatleastKtimesthenumberoftests.
Typically, the ECOC strategy combines the outputs of multiple binary classifiers
using a straightforward nearest-neighbor rule, selecting the class closest to the binary
classifiers’outputs. Fornearest-neighborECOCs,theerrorrateofthemulticlassclassifier
isimprovedbasedontheaveragebinarydistance[187]. Thisdemonstrateswhymethods
suchaseliminationandHammingdecodingoftenleadtosimilaraccuracylevels. Beyond
improvinggeneralization,ECOCscanalsobeappliedtohandleunclassifiableregions.
IntheECOCframework,letg representthetargetvalueforthejthdecisionfunction
ij
D (x)correspondingtoclassi,definedasfollows:
ij

1, ifD (x) >0
g = ij , i =1,...,K. (12)
ij
−1, otherwise
Thetargetvectorforthejthdecisionfunctionisthecolumnvectorg =
(cid:0)
g ,...,g
(cid:1)T
.
j 1j Kj
If all elements of a column vector are either 1 or −1, the decision function does not
contribute to classification. Additionally, if two column vectors satisfy g = −g , they
i j
representthesamedecisionfunction. Therefore,themaximumnumberofdistinctdecision
functionsis2K−1−1.
The ithrowvector (g ,...,g ) representsacodewordforclass i, where k denotes
i1 ik
thenumberofdecisionfunctions. Forathree-classproblem, therecanbeatmostthree
 
1 −1 −1
decisionfunctions,representedby (cid:2) g (cid:3) =  −1 1 −1 ,whichcorrespondstothe
ij  
−1 −1 1
one-against-allformulationandlackserror-correctingcapability. Byintroducingadon’t-
careoutputsymbol0,theone-against-all,one-against-one,andECOCschemesareuni-
fied[181]. Theone-against-oneclassificationforthreeclassescanberepresentedasfollows:
 
1 0 −1
(cid:2) g (cid:3) =  −1 1 0 .
ij  
0 −1 1
11. Dempster–ShaferTheoryofEvidence
TheDempster–Shafertheoryofevidence,introducedbyDempster[188]andexpanded
byShafer[2],buildsupontheconceptsofupperandlowerprobabilities. Itgeneralizes
the Bayesian approach to probability by facilitating the combination of multiple pieces
ofevidenceinordertomakeprobabilityjudgments. Thisframeworkiscommonlyused
for fusing information from diverse sources to assess the truth of a hypothesis. Within
Dempster–Shafer theory, two key concepts are employed: belief, which quantifies the
supportforahypothesisbasedontheevidence,andplausibility,whichmeasurestheextent
towhichtheevidencedoesnotcontradictthehypothesis. Theseconceptsareanalogousto
necessityandpossibilityinfuzzylogic. TheDempster–Shaferapproachutilizesintervalsto
representuncertainprobabilities,similartointerval-valuedfuzzysets. Asamethodfor
reasoningunderuncertainty,Dempster–Shafertheoryhasfoundextensiveapplicationin
fieldssuchasexpertsystems,informationfusion,anddecisionanalysis.
Definition 1 (Frame of Discernment). A frame of discernment, denoted by Θ, is a finite set
consistingofNmutuallyexclusivesingletonhypotheses,representingthescopeofknowledgefora
givensource. Thiscanbeexpressedasfollows:
Θ = {A ,A ,...,A }. (13)
1 2 N

Mathematics2025,13,587 23of49
EachhypothesisA,knownasasingleton,representsthesimplestandmostgranular
i
levelofdistinguishableinformation.
Definition2(BasicProbabilityAssignmentFunction). Thebasicprobabilityassignment(BPA)
function,denotedasm(A),assignsaprobabilitytoeachevent(orproposition)Awithintheframeof
discernmentΘ.Themappingm :2 Θ → [0,1]mustsatisfythefollowingconditions: m(∅) =0and
∑ m(A) =1. (14)
A⊆Θ
Theset2 Θ representsthepowersetofΘ,whichincludesallpossiblesubsetsofΘ. For
example,ifΘ = {A ,A ,A },then2 Θ consistsofthefollowingsubsets:{∅,A ,A ,A ,A ∪
1 2 3 1 2 3 1
A ,A ∪A ,A ∪A ,Θ}.
2 1 3 2 3
InthecontextofaframeofdiscernmentΘ,aneventAisconsideredafocalelement
oftheBPAmifm(A) >0. Whenmhasonlyonefocalelement,denotedasA,theBPAis
referredtoascategoricalandiswrittenasmA. Ifeveryfocalelementofmcorrespondstoa
singletonevent,thenmisconsideredBayesian.
ThevaluesassignedbyaBPAfunctionarereferredtoasbeliefmasses. ABPAfunction
isconsiderednormalifm(∅) =0.
Definition3(BeliefFunction). ForanyhypothesisA⊆ Θ,itsbelieffunction,denotedasBel(A),
isamappingfrom2 Θ to[0,1]andisdefinedasthesumofthebasicprobabilitiesofallsubsetsofA,
Bel(A) = ∑ m(B), ∀A⊆ Θ. (15)
B⊆A
Thebelieffunction,alsoreferredtoasthelowerlimitfunction,quantifiestheminimum
supportforahypothesisA. Itcanbeinterpretedasaglobalindicatorofthedegreeofbelief
thatAistrue. Basedonitsdefinition,wehaveBel(∅) =0andBel(Θ) =1. Itisimportant
tonotethatthereisaone-to-onecorrespondencebetweentheBPAandthebelieffunctions.
Definition4(PlausibilityFunction). TheplausibilityfunctionofahypothesisA,denotedPl(A) :
2 Θ → [0,1],measuresthebeliefthatisnotassignedtothenegationofA. Itisdefinedasfollows:
Pl(A) =1−Bel(A¯) = ∑ m(B), ∀A⊆ Θ. (16)
B∩A(cid:54)=∅
The plausibility function, also known as the upper limit function, represents the
maximumpossiblebeliefassignedtoA. Whiletheplausibilityfunctionservesasameasure
ofpossibility,thebelieffunctionisitsdualcounterpart,representingnecessity. Itcanbe
demonstratedthat[2]
Pl(A) ≥ Bel(A), ∀A⊆ Θ. (17)
InthecasewheremisBayesian,boththebeliefandplausibilityfunctionscoincide,effec-
tivelyactingasaprobabilitymeasure.
Definition5(UncertaintyFunction). TheuncertaintyassociatedwithAisgivenbythedifference
betweentheplausibilityandbelieffunctions:
U(A) = Pl(A)−Bel(A). (18)

Mathematics2025,13,587 24of49
Definition6(CommonalityFunction). ThecommonalityfunctionquantifiestheamountofBPA
thatisallocatedtoAandallsetsthatcontainAasasubset:
|     |     |     | Com(A) | = ∑ | m(B). |     |     |     |
| --- | --- | --- | ------ | --- | ----- | --- | --- | --- |
(19)
B⊇A
Belief functions are extensively utilized to represent and handle uncertainty. In
Dempster–Shafer theory, Dempster’s combination rule is employed to merge different
belief sources. Under certain probabilistic assumptions, the outcomes of this rule are
bothprobabilisticallysoundandinterpretable. Knownastheorthogonalsummingrule,
Dempster’srulesynthesizestheBPAsfrommultiplesourcestoproduceanewbeliefor
probability,expressedasaBPA.Ifm andm aretheBPAsfromtwodistinctsourceswithin
|     |     |     | 1   | 2   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
thesameframeofdiscernment,thecombinationisgivenby[2]
1
| m(∅) |     | m(A) |     |          | ∑   | (B)m | (C), |      |
| ---- | --- | ---- | --- | -------- | --- | ---- | ---- | ---- |
|      | =0, |      | = m | 1 ⊕m 2 = |     | m 1  | 2    | (20) |
1−K
B∩C=A
where
|     |     |     | ∑   | (B)m | (C) |     |     |      |
| --- | --- | --- | --- | ---- | --- | --- | --- | ---- |
|     |     |     | K = | m    | >0  |     |     | (21) |
1 2
B∩C=∅
representstheconflictbetweentheevidencesources. IfK =1,thetwopiecesofevidence
aredeemedlogicallyinconsistentandcannotbecombined. ToapplyDempster’srulein
casesofhighconflict,anyconflictingbeliefmassescanbeassignedtoanemptyevent,in
linewiththeopen-worldassumption. Thisassumptionpositsthatsomepotentialevent
mayhavebeenoverlookedandthusisnotrepresentedintheframeofdiscernment[189].
In general, the combined result of n BPA values, m , m , ..., m , within the same
|     |     |     |     |     |     | 1 2 | n   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
frameofdiscernmentΘ,iscomputedasfollows:
|      |     |      |        |       |     | (cid:32) | (cid:33) |      |
| ---- | --- | ---- | ------ | ----- | --- | -------- | -------- | ---- |
|      |     |      |        |       | 1 ∑ | ∏ n      |          |      |
| m(A) | =   | m ⊕m | ⊕···⊕m | =     |     |          | m(A) ,   | (22) |
|      |     | 1    | 2      | n 1−K |     |          | i        |      |
∩A =A
i i=1
where
|     |     |     |     | (cid:32) | (cid:33) |     |     |     |
| --- | --- | --- | --- | -------- | -------- | --- | --- | --- |
n
|     |     |     |     | ∑ ∏    | m(A) |     |     |      |
| --- | --- | --- | --- | ------ | ---- | --- | --- | ---- |
|     |     |     | K = |        | i .  |     |     | (23) |
|     |     |     | ∩A  | =∅ i=1 |      |     |     |      |
i
InthecontextofDempster–Shafertheory,thefusionprocessinvolvingDempster’srule
ofcombinationisknowntobeNP-complete,whichlimitsthenumberofbelieffunctionsand
focalsetsthatcanbecombined. Toovercomethischallenge,MonteCarloalgorithms[190]
useimportancesamplingandlow-discrepancysequencestoapproximatetheresultsof
Dempster’srule.
OnekeyadvantageoftheDempster–ShafermethodovertheBayesianapproachis
that it does not require prior probability distributions, instead directly combining the
availableevidence. However,theDempster–Shafermethodfailsinfuzzysystemsdueto
itsassumptionthathypothesesaremutuallyexclusive.
Dempster’srulepresumestheindependenceofclassifiers. Forcombiningdependent
classifiers,alternativessuchasthecautiousruleandt-norm-basedrules,whichprovide
arangeofbehaviorsfromDempster’sruletothecautiousrule,canbeutilized[191]. An
optimalcombinationstrategycanbederivedfromaparameterizedfamilyoft-norms.
AnotherlimitationofDempster’sruleisthatittreatsallsourcesofevidenceasequally
reliable. Incertaincases,particularlywhenthereissubstantialconflictamongevidence
sources,counterintuitiveresultsmayarise[192]. Ameasureoffalsity,derivedfromthe
conflictcoefficientusingDempster’srule,hasbeenproposedtoaddressthisissue[193].

Mathematics2025,13,587 25of49
Basedonthismeasure,discountingfactorscanbeintroducedtoadjusttheevidencecombi-
nationprocess.
Dempster–Shafertheorystruggleswithhighlyconflictinginformation.Asanextension
and alternative, Dezert–Smarandache theory [194] introduces flexible fusion rules that
effectivelymanageparadoxicalandconflictingdata. Itoffersageneralcombinationrule
applicable to any model without normalization, making it advantageous in fields like
defenseandroboticswherecontradictoryevidenceiscommon.
WhenapplyingDempster–Shafertheoryfordecisionfusion,itisnecessarytoestablish
thecorrespondingBPAs. Logisticregressionandmultilayerfeedforwardnetworkscan
beviewedastechniquesthatconvertinputfeaturesorhigher-levelrepresentationsinto
massfunctions,whicharethenaggregatedusingDempster’sruleofcombination[195].
Theprobabilisticoutputsoftheseclassifierscorrespondtothenormalizedplausibilities
thatmakeupthecombinedmassfunction.
The granule fusion density-based clustering with evidential reasoning (GFDC)
method [196] introduces an approach based on Dempster–Shafer theory for assigning
border samples and detecting outliers. Additionally, a belief function theory-based re-
samplingtechnique[197]addressesclassimbalanceinmulti-classscenarios,integrating
ensemblelearningforimprovedperformance.
12. MultipleKernelLearning
MKL focuses on combining multiple kernels to build robust models, particularly
suitablefortasksinvolvingheterogeneousdatasources[198,199]. Byleveragingcomple-
mentaryinformationfromdifferentperspectives,MKLconstructsbasekernelsforeach
view, enabling the simultaneous optimization of feature combinations and their associ-
atedpredictors.
MKL,initiallyformulatedasasemidefiniteprogramming(SDP)problem[198],com-
bineskernelsk(·) = ∑ α k (·)intoaconvexquadraticallyconstrainedquadraticprogram
i i i
(QCQP) [198] and later adapts to large-scale applications as a semi-infinite linear pro-
gram [200]. In regularized kernel discriminant analysis, the kernel matrix is a linear
combinationofpredefinedkernels,transformingkernellearningintoaconvexSDP[201].
Sparse MKL, such as multiple kernel linear discriminant analysis (LDA) [202], applies
L -norm regularization to kernel weights, solving it as a convex optimization problem.
1
ThesemethodsutilizeSDP,QCQP,andlinearprogramming(LP)techniquesforscalable
kernellearning[198,200–202].
Sparse MKL [203] imposes L -norm simplex constraints, while generalized mod-
1
els[204]balancesparsityandflexibilitywithelastic-net-likeconstraints. SimpleMKL[205]
usesreducedgradientdescent,whileHessianMKL[206]employsNewtonupdates. L -
p
normMKLoffersadvantageswhensparsityislesscritical[207,208],andanalyticalsolvers
outperformL -normmethods[200],particularlywithcutting-planeoptimization[207].
1
SpicyMKL[209]iterativelysolvessmoothminimizationproblemsforgeneralconvex
lossfunctions,achievingsuper-linearconvergence.Kernelslackvariables[210]extendMKL
tovariouslossfunctions,withSMO-MKL[211]usingsequentialminimaloptimizationfor
L -normMKL.BayesianMKL[212]integrateskernelsinaconjugateBayesianframework,
p
andahierarchicalmodelincorporatesdata-dependentpriors[213].
Multiple kernel fuzzy C-means (FCM) [214] improves clustering by integrating
MKL, while clustering methods [215–220] select kernels to refine clustering. The MPS
method [221] further improves clustering by using multi-dimensional representations.
MultipleC-meansclustering[218]optimizeskernelcombinationsusingalternatingmini-
mization,andamin–maxframework[222]createsunifiedkernels.

Mathematics2025,13,587 26of49
ScalabilitychallengesinMKLareaddressedbySVRG-MKL[223],whichavoidsGram
matrix computations for linear complexity. The multi-kernel RBF network [224] uses a
linearconvexmodelwithorthogonalleastsquaresoptimization. DOMKL[225]integrates
kernelsusingonlinealternatingdirectionmethodofmultipliers(ADMM)andadistributed
hedge algorithm, achieving sublinear regret. Raker and AdaRaker [226] dynamically
generatenonlinearlearningfunctions,withAdaRakerexcellingindynamicenvironments.
MetaheuristicapproachesarealsoappliedinMKLfordiverseoptimizationtasks[30].
13. MultiviewLearning
Multiviewlearning,acommonensemblelearningstrategy,representsreal-worlddata
usingmultipledistinctfeaturesets,orviews. Eachviewofferscomplementaryinformation
thatimproveslearningperformance[227].
Supervisedmultiviewlearningmethodsarecategorizedintolatentspaceandcoregu-
larizationapproaches. Latentspacemethodsidentifyasharedlatentsubspaceforunified
embeddings,enablingsingle-viewlearningtechniques. Multiviewrepresentationlearning
(MVRL) consolidates information across views, enhancing performance by integrating
hierarchicalstructures[228–232]. Techniqueslikematrixfactorization[233,234],graphical
models[235,236],andsparsecoding[237]addressMVRLchallenges,suchascross-view
translationandmultiviewalignment.
MVRLfocusesonlearningunifiedrepresentationsacrossmultiviewdatatoensure
consistent latent space features [227,238]. Methods are divided into coordinated and
jointapproaches. Coordinatedlearningalignsseparateviewrepresentations,withCCA
maximizing their correlation. Joint learning seeks a shared latent representation using
techniqueslikelow-rankdecompositionandmatrixfactorization[239–242],maintaining
consistency,whileothermethods[243,244]capturecomplementaryinformationbylearning
bothcommonandview-specificrepresentations.
Recent deep MVRL methods include using deep Boltzmann machines for textual–
visualfusion[235],deepautoencodersforsharedrepresentationsintwo-viewdata[245],
andneuralnetworksforgeneralrelationships[246]. Deepmatrixfactorization[247,248]
enhancestraditionalmethodsandaidsinunsupervisedanalysis[249,250].
Fordomainadaptation,amulti-sourcecontributionlearningmethod[251]improves
featuretransferabilitybyreducingmisclassificationwithmulti-leveldistributionmatching.
13.1. Subspace-BasedApproach
CCA[36]isakeymethodformultiviewsubspacelearning,identifyinglineartrans-
formationsthatmapviewsintoasharedspaceformaximallinearcorrelation. Ithasbeen
extendedtohandlemultipleviews[252–255]andincorporatenonlinearprojectionsusing
kernelmethods[256]ordeeplearning[257,258]. CCAhasalsobeenadaptedtofuzzy[259],
probabilistic [260], and Bayesian [261] frameworks and has been applied in supervised
learning[262].
Multiset CCA [252,253] extends pairwise correlation, and generalized CCA [263]
alignsallviewsviaasharedrepresentation,commonlyformulatedwithleastsquares[264].
Deep CCA [258] uses deep networks for nonlinear view correlation, while multiview
deepnetworks[265]learnview-invariantrepresentationsforcross-viewclassification. An
ensembleofmultiviewclassifiers[266]employslightweightCNNs,withmeta-learning
usedforeffectiverepresentationselection. DeepmultisetCCA[267]extendsmultisetCCA
withdeeplearning.
Other linear models for two-view data include partial least squares (PLS) [268]
andorthogonalpartialleastsquares(OPLS)[269],withnonlinearextensionslikekernel
OPLS [270]. The multiview uncorrelated locality-preserving projection (MULPP) [271]

Mathematics2025,13,587 27of49
improves consistency by maximizing correlations while preserving local structures
acrossviews.
Bayesianmethods[272]recovermultiviewcorrespondences,withadversarialCCA[272]
enhancinglatentconsistency. CCAalignswithLDAinsupervisedclassificationformulti-
classtasks[273],sharingleast-squaresproperties,withLDAextensionsforbinaryclassifica-
tionacrosstwoviews[274],andmultiviewdiscriminantanalysis[265]formultipleviews.
CombiningCCAandLDAenablesgeneralizedmultiviewanalysis[262,265,275–277].
13.2. CoregularizationApproach
Coregularizationmethodsdirectlyaddresssupervisedtasks,assumingoutputsfrom
differentviewsshouldalign. Modelsaretrainedtoensureconsistentoutputs,enhancing
robustnessandmitigatingoverfitting. Disagreementbetweenviews,measuredbyclassifi-
cationmargins,servesasacoregularizationterm[278]. Forexample,SVM-2k[279]aligns
margins,whilemultiviewmaximumentropydiscriminationanditsextensions[280–282]
enforceviewagreementthroughposteriormarginconstraints.
Gaussianprocesseshavebeenextendedtomultiviewsettingswithmodelslikethe
multimodalsimilarityGaussianprocesslatentvariablemodel[283]andmanifoldrelevance
determination [284], building on Gaussian process latent variable models [285]. These
approaches use Gaussian processes to model data embeddings across views. Bayesian
cotraining[261]introducesaprobabilisticgraphicalmodelthatcoupleslatentfunctions
fromdifferentviewsviaaconsensusfunction. ThemultiviewregularizedGaussianprocess
model[286]furtherintegratesviewsbyregularizingGaussianprocessmarginallikelihoods,
aligningposteriordistributionsviapairwisesymmetricKullback–Leiblerdivergence.
MultiviewOPLS[287]trainsclassifiersinasharedlatentspace,reinforcedbyregular-
izerstargetingmodelparameters,decisionvalues,andlatentprojections,accommodating
reformulationsandintroducingnovelmodelswithdiverseprior-basedregularizers.
13.3. MultiviewClustering
Multimodaldatafusionmergesdatafromvarioussourcesintoaunifiedspace,repre-
sentingbothintermodalityandcross-modalityconsistently[288]. Severalmethods,suchas
multimodalindependentcomponentanalysis[289],combineindependentvariablesfrom
eachmodalityusingaBayesianframework.
Multiviewclusteringuncoverssharedstructuresbyleveragingcomplementaryinfor-
mation. Traditionalmethodsoftenoverlookpartitionsfromsingle-viewclustering[290].
M2VEC [291] addresses this by combining individual view partitions into a consensus,
using low-rank and sparse decomposition, spectral consensus graph partitioning, and
multilayerextensionsfornonlinearrepresentations.
Multiview fusion clustering with attentive contrastive learning (MFC-ACL) [292]
utilizes an attention mechanism. The Att-AE module enhances the autoencoder (AE)
toextractglobalviewfeatures,whilethetransformerfeaturefusioncontrastivemodule
(TFFC)learnsconsistentlow-dimensionalfeatures. Thesehigh-levelfeatureswithshared
consistencyinformationarethenclusteredforoptimizedresults.
Ensemble clustering [293–295] combines basic partitions into a consensus result,
harnessing complementary information [296]. Multiview clustering methods include
cotraining-basedmethods[215,297],commonsubspace-basedmethods[298–300],andlate
fusion-basedmethods. Cotrainingenhancesmutualconsistencybetweenviews,whilecom-
monsubspacemethodsfocusonlearningsharedsubspacesforclustering[290]. Thesecan
bedividedintoCCA-based[298],nonnegativematrixfactorization(NMF)-based[242,299],
andlow-ranksubspace-basedmethods[300,301].

Mathematics2025,13,587 28of49
Ensemble clustering can be based on utility functions [295] or coassociation matri-
ces[294],withexamplessuchashierarchicalconsensusclustering[294]andspectralensem-
bleclustering[302]. OtherapproachesincludeNMF-basedframeworks[303],linked-based
methods[304],andwisdom-of-crowdsapproaches[305]. Performancecanbeenhanced
bylearningrobustrepresentations,enforcingalow-rankconstraintonthecoassociation
matrix[306],andusingstackedmarginalizeddenoisingautoencoders(mDAs)[307].
Comparedtomultiviewclustering,ensembleclusteringoffershigher-levelinsights.
However, it often treats each basic partition equally, neglecting the complementary in-
formation across views. A more effective approach learns a consensus representation
sharedacrosscoassociationmatrices,addressingchallengessuchasoutliersandinconsis-
tencies[306].
14. EnsembleNeuralNetworks
Networkensembles[15]enhanceperformancebycombiningoutputsfrommultiple
weakmodels,usingstrategieslikevaryingnetworkinitializationsorpartitioningdata. In
deeplearning,ensemblemethods,suchasVGGNetandAlexNetensembles,retrainmodels
withdifferentinitializationsandaveragepredictionstoimproveaccuracy.
BoostingcombinesmultipleSVMs,eachtrainedonsubsetsofdata,toenhanceperfor-
mance[308]. ParallelSVMmethods,liketheparallelmixtureofSVMs[309],distributedata
acrossprocessors,trainingSVMsandcombiningoutputsviagatingmechanisms,reducing
complexitytoO(N)andimprovinggeneralization.
Bias–variance decomposition [310] for SVMs with various kernels shows that en-
semblemethodsreducevarianceandenhancerobustness,extendingSVMbias–variance
characteristicstobaggedandrandomensembles.
The mixture model of linear SVMs [311] partitions feature space into linearly sep-
arablesubregions,usingtheexpectation-maximization(EM)algorithmforsparsityand
modelselection.
Ensemble clustering combines multiple solutions into a unified result, improving
consistencyacrosstheensemble[312]. Clusterensembles[313]andtechniqueslikebagging
andAdaBoost[314]improveperformanceandreducelearningtimecomparedtotraditional
methods. Exactbaggingwithk-NNextendsbootstrapsampling[315].
Thereal-timerecurrentlearning(RTRL)algorithmandtheextendedKalmanfilter
(EKF)havecomplexitiesofO(n4)andO(n2)fornneuronsinonlinerecurrentnetworks,
respectively. TheensembleKalmanfilter(EnKF)[316]reducescomplexityandoutperforms
gradientdescentandEKF.
Theinverseadversarialdiversitylearningapproach[317]enforcesdiversitybytreating
weaknetworksasgeneratorswithadiscriminatortoassessfeaturedisparity.
Themixture-of-expertsmodel[318]anddiverseensembleevolution[319]promote
diversitythroughvaryinglearningrates,trainingsamples,andmodelarchitectures. Snap-
shotensembles[18]andadaptivediversity-promotingregularizers[320]exploreensemble
robustness,whilediversity-regularizedpruning[321]investigatesdiversity’simpacton
generalizationinprobablyapproximatelycorrect(PAC)learning.
15. TheoreticalResults
15.1. EnsembleSize
Thenumberofclassifiersselectedforanensembleplaysacrucialroleinitsoverall
predictiveperformance[322]. Determiningtheoptimalensemblesizeisakeychallenge,
asitinfluencesboththecomputationalefficiency(intermsoftimeandmemory)andthe
ensemble’spredictiveaccuracy[323,324],especiallyinonlinelearningenvironmentswhere
efficiencyisparamount.

Mathematics2025,13,587 29of49
Thediversityamongindividualclassifierswithintheensembleisacriticalfactorthat
contributes to its success [49,325]. Studies such as [326] have empirically explored the
relationshipbetweenensemblesizeanddiversity. Greaterdiversitywithinthecomponent
classifiersleadstouncorrelateddecisions,which,inturn,enhancestheensemble’soverall
performance[327].
A geometric framework [328] explores how diversity impacts ensemble classifier
accuracyandhelpspre-determineoptimalensemblesizeforbatchandonlinesettings. For
majorityvoting,itshowsthataddingstrongcomponentsimprovesaccuracy. Forweighted
majorityvoting,theoptimalsizematchesthenumberofclasslabelsifthecomponentsare
strongandindependent. Theframeworkalsoexplainshowdiversityimprovesensemble
predictionaccuracy.
Thesizeofanensemblecanbepredetermined,asinbaggingmethods,oradjusted
dynamicallybyassessingtheimpactofaddingnewcomponents[49]. Studiesshowthata
well-chosensubsetofalargerensemblecanmatchtheperformanceofthefullensemble
in accuracy and diversity [326]. Incremental batch-mode ensemble construction based
oncriterialikeaccuracy,diversity,andcorrelationhasalsobeenexplored[329]. Another
approachistoallowensemblestogrowindefinitely,thenprunethemforimprovedeffec-
tiveness[49,330].
Inonlinelearning,ensemblesizecanadjustautomatically,asshownby[331],where
aprobabilisticframeworkaddscomponentsbasedonconfidencelevels. However, this
approachdoesnotaccountforthediversityofcomponentclassifiers,andthereisariskof
continuouslyaddingcomponentswithoutachievingthedesiredconfidencelevel. Increas-
ingensemblesizealonedoesnotindefinitelyreduceerrors[1].
For batch-mode ensembles, a practical method [332] involves limiting the number
of classifiers based on the McNemar test of significance. Other studies [9,333] recom-
mend using 10–20 base classifiers for bagging, depending on the dataset and the base
classifier used. The misclassification rate of linear combiners is influenced by both the
performanceofindividualclassifiersandthecorrelationbetweentheiroutputs[334]. Using
aweightedaverage,ratherthanasimpleaverage,canimproveperformance.Thisapproach
isextendedin[333]toanalyzebagging-generatedensemblesandtoprovideamodelfor
misclassificationprobabilityasafunctionofensemblesize.
Furtherresearchinvestigatesconvergence,determiningthenumberoftreesneeded
forstabilization[335,336].
15.2. DiversityVersusEnsembleAccuracy
Existing ensemble methods often generate unnecessarily large ensembles, leading
to inefficiencies. Ensemble pruning addresses this by identifying a subset of classifiers
that approximates the performance of the full ensemble. A common strategy involves
rankingclassifiersbytheirperformanceonaheld-outtestsetandselectingthetopper-
formers. However, this approach is not always optimal. For instance, an ensemble of
threeidenticalclassifierswith90%accuracymayunderperformcomparedtoanensemble
ofthreeclassifierswith70%accuracybutlowererrorcorrelation.
Ensemblepruningcanbeframedasadiscreteoptimizationproblem,aimingtobalance
accuracyanddiversity.Thischallengeisoftenmodeledasaquadraticintegerprogramming
problem,wheretechniquessuchasSDPoffereffectiveapproximatesolutions[337].
Itisgenerallyacceptedthatgreaterdiversityamongclassifiersleadstoimprovedper-
formanceinanensemble.ThemostwidelyusedmeasureofdiversityistheQ-statistic[338].
Whentwoclassifiersarestatisticallyindependent,theirQ-statisticvaluewillbezero. The
valueofQrangesfrom−1to1,withlowervaluesindicatinggreaterdiversity. Classifiers

Mathematics2025,13,587 30of49
thatmakesimilarcorrectpredictionswillhaveapositive Qvalue,whileclassifiersthat
makeerrorsondifferentinstanceswillyieldanegativeQ.
Empiricalstudiesrevealthattherelationshipbetweendiversitymeasuresandensem-
bleaccuracyiscomplexandoftenambiguous[325]. Theoretically,diversitymeasuresare
notalwayseffective[339];althoughtheycanproduceensembleswithhighdiversity,this
doesnotguaranteeachievingmaximumdiversity[339].
Theperformanceofanensembledependssignificantlyonboththediversityamong
itsclassifiersandtheirindividualaccuracies. Tocapturethetrade-offbetweenthesefactors,
aninformation-theoreticscorehasbeenproposed[338],whichdirectlyaidsinselecting
anoptimalsubsetfromapoolofclassifiers. Inscenariosinvolvingoverproductionand
selection,ensembleschosenusingthisscoreconsistentlyoutperformthoseselectedsolely
basedondiversitymeasures.
Boththediversityamongclassifiersandtheirindividualaccuraciesplayasignificant
role in the overall performance of an ensemble. An information-theoretic score [338]
expressesthetrade-offbetweenaccuracyanddiversity. Thisscorecanbeuseddirectlyto
selectanoptimalsubsetfromapoolofclassifiers. Incasesofoverproductionandselection,
ensemblesselectedusingthisinformation-theoreticscoretendtooutperformthoseselected
basedpurelyondiversitymeasures.
15.3. BiasVersusVariance
The superior generalization performance of ensemble methods can be explained
throughvarioustheoreticalframeworks,includinglargemarginclassifiers[181],stochastic
discrimination theory [340], and bias–variance analysis [341,342]. Ensembles enhance
generalization by expanding decision margins, thereby boosting the robustness of the
underlyingmodels[62,181]. Theyareeffectiveinreducingvariance[341]and, insome
cases,bias[180].
Theeffectivenessofensemblemethods,suchasrandomforests,dependsonboththe
accuracyofindividualbaselearnersandthedependenciesbetweenthem. Bias–variance
decompositionistraditionallydefinedusingsquaredlossastheobjectivefunction. How-
ever, in classification tasks where the 0/1 loss is prevalent, alternative decompositions
havebeenintroduced[341,343,344]. Aunifiedframeworkforbias–variancedecomposition
underthe0/1lossfunctionisintroducedin[344],extendingtheseconceptstomoregeneral
lossfunctions. Buildingonthistheory,quantitativemethodsforassessingbias–variance
decomposition in ensemble learning are proposed in [345], while the decomposition is
examinedspecificallyforECOCensemblesin[180].
Decision trees, such as those in CART [114], can overfit without careful pruning.
Bagging helps by reducing variance through training on bootstrap samples. Random
forestsfurtherenhancethisbyintroducingextrarandomness,reducingtreedependence
butincreasingindividualtreevariance.
Randomforestscanbeunderstoodintermsofthebias–variancetradeoff[12],wherea
smallreductioninbaselearneraccuracy(introducedbyadditionalrandomness)results
inalargerdecreaseinthecorrelationbetweentrees. Thisreductionincorrelationhelps
lower variance, as highlighted by [346], and often explains the observed performance
improvements.
Theconceptofmargins,centralto[62],iscloselylinkedtobiasandvariance,which
areinterrelatedratherthanstrictlyadditive[344]. Insomecases,highbiascanbeoffset
bylowvariance,improvingclassificationaccuracy[343]. Thisphenomenonisparticularly
evident in simple models like naive Bayes classifiers, where combining models, such
as through bagging, reduces high bias. This interplay explains why simpler methods

Mathematics2025,13,587 31of49
cansometimesoutperformmorecomplexmodelsandwhyaggregatingclassifiersoften
enhancesperformance[343].
15.4. Regularization
Theinherentrandomnessinindividualdecisiontreesservesasanimplicitregular-
ization,makingrandomforestsparticularlyeffectiveinscenarioswithlowsignal-to-noise
ratios(SNRs)[347]. Insomecases,randomforestsexhibitbehaviorakintoridgeregres-
sion[346]. Specifically,themtryparameterinrandomforestsfunctionssimilarlytothe
shrinkagepenaltyinregularizedregressionmethodslikeLASSOandridgeregression. A
randomizedforwardselectionprocedureforlinearmodels[347]mirrorsthestructureof
tree-basedrandomforests. Thisworkintroducestworandomizedforwardselectionstrate-
giesforlinearmodelsthatparallelclassicalbaggingandrandomforests,demonstrating
similarregularizationeffects.
Tree-based ensembles are also related to kernel methods [130,348] and neural net-
works [349,350]. In [19], it is hypothesized that the success of random forests and Ad-
aBoost[73]isattributedtotheirbehaviorasself-averaginginterpolators,enablingperfect
datafittingwhilesmoothingpredictionsthroughaveraging[19].
In terms of statistical properties, methods like subsampling offer consistency and
asymptoticnormality. In[351],theintroducedpermutation-basedhypothesistestforfea-
turesignificance,analogoustotheF-test,iscomputationallyefficientandrobust,requiring
farfewercalculationswhilemaintaininghighpower.
EnsembledeeplearningmethodslikeSnapshot[18],fastgeometricensembling[352]
andstochasticweightaveraging[353,354]haveprovenhighlyeffectiveatimprovingmodel
generalization.
16. IncrementalEnsembleLearningforStreamingData
Random forests are leading tree-based ensemble methods in batch learning, with
adaptationsfordatastreamlearning[150,355,356]. Theadaptiverandomforestintegrates
learningbufferswiththetraditionalrandomforeststructure[356],extendedtoregression
tasks[357],andusedinincrementaldeepforests[358,359].
Streamingrandompatches[360,361]isanotherincrementalensemblemethod,offering
flexibility by supporting diverse base learners and using a data perturbation strategy
to generate models. Unlike adaptive random forests, which sample feature subsets at
eachnode,streamingrandompatchesselectsasinglefeaturesubsetforconstructingthe
basemodel.
Theonlineextratrees(OXT)algorithm[362],inspiredbyextratrees,usessubbagging,
randomsplits,andmodeltreestoimprovepredictionaccuracywhilereducingcomputa-
tionalcost,beingfasterandmorememory-efficientthanadaptiverandomforests.
Learn++ is a chunk-based ensemble for stationary data streams [363], combining
predictionsviamajorityvoting,thoughinefficiencyariseswhenretainingallclassifiers.
Bagging++[364]addressesthisbycreatingmodelsfromnewdatachunks. Onlinebagging
andboostingmethods[68]enhanceflexibilityfordynamiclearning.
Fornonstationaryenvironments,chunk-basedensemblesadapttoconceptdriftbytrain-
ingnewclassifiersonincomingchunks[365]. Learn++isextendedtoLearn++.NSE[366],
weightingexamplesbasedonensembleperformanceandmakingpredictionsviaweighted
majorityvoting. Onlineensemblesfornonstationarystreamsaremorememory-efficient
andfasterthanchunk-basedmethods.

Mathematics2025,13,587 32of49
17. EnsembleLearningVersusDeepLearning
Ensemblelearninganddeeplearningoffertwodistinctapproachestoaddressingthe
samereliabilitychallenge. Ensemblelearningreliesontheconceptofparallelprocessing,
whiledeeplearningfollowsaserialprocessingframework. Together,theycomplement
eachother.
The representational capacities of random forests, binary decision diagrams, and
neuralnetworksarecomparedbasedonthenumberofnodes[367]. Whenaxis-aligned
functions are assigned to edges in random forests and binary decision diagrams, and
neuralnetworksutilizecommonactivationfunctionslikesigmoidorrectifiedlinearunits
(ReLUs),itisdemonstratedthatanyrandomforestcanberepresentedbyanequivalent
depth-3neuralnetworkwithalinearnumberofnodes[367]. Similarly,anybinarydecision
diagram with balanced width can be represented by a shallow neural network with a
polynomialnumberofnodes[367]. Thesefindingshighlightthatshallowneuralnetworks
oftenpossessequalorgreaterrepresentationalpowercomparedtodeeprandomforestsor
decisiondiagrams. Additionally,certainfunctionsthatcanbeexpressedcompactlybya
smallerrandomforestmayrequireanexponentiallylargernumberofnodesinadifferent
randomforestrepresentation[367].
Anotherareaoffocusinensemblelearninginvolvesimprovingdecisionreliability
whilereducingcomputationalcosts. Forinstance,considerthescenariowhereeachmis-
sileinterceptorhasa70%chanceofsuccess. Launchingthreeinterceptorsindependently
increases the probability of success to 1−0.3×0.3×0.3 = 97.3%, assuming ideal con-
ditions. If each interceptor has an 80% success rate, the success rate increases to 99.2%.
Whiledesigningacontrollerwith70%accuracyismuchlesscostlythanonewith97.3%,
thecombinationofmultipleclassifiersusingamajorityvotingstrategycansignificantly
improveoverallreliabilityatalowcost[368].
Deepneuralnetworksareoftenmoreexpressivethanshallowonesofcomparablesize.
NetworkswithReLUscanefficientlyapproximatesmoothfunctions,makingthemmore
powerfulthanshallownetworks[369]. However,shallow,widernetworkscansometimes
outperformdeepmodels,thoughdeepnetworksaregenerallyfavoredinrecentresearch.
Shallownetworkscancomputeawidervarietyoffunctionsthandeepnetworks,butthe
functionstheycomputetendtobelessregular[370].
Residual networks (ResNets) are a popular deep model, with their success being
interpreted as an ensemble of many shallow networks. This is because the paths in a
ResNetarenotheavilydependentoneachother,eventhoughtheyaretrainedjointly[371].
SkipconnectionsinResNethelpmitigatethegradientvanishingissuecommonlyfoundin
deepnetworks[372].
InastudycomparingdeepandshallowneuralnetworksontheMNISTdatasetfor
digitrecognition,itwasfoundthatasimpleshallownetworklikeamultilayerperceptron
often achieves performance similar to deeper models [368,373]. This supports the idea
thatsimplermodelscanbejustaseffective,aligningwiththeno-free-lunchtheoremand
Occam’srazor[30,36].
Datafusionservesasacentralconceptinmachinelearning,leadingtotwodistinct
approaches—ensemblelearninganddeeplearning—bothaimedatenhancingclassification
accuracy. Whileensemblelearningimprovesperformancebycombiningmultiplemod-
els,deeplearningachievesthisbylearninghierarchicalfeaturerepresentations. Table3
summarizesthekeydifferencesbetweenthesetwoapproaches.

Mathematics2025,13,587 33of49
Table3.Comparisonbetweenensemblelearninganddeeplearning
Aspect EnsembleLearning DeepLearning
Combinesmultiplemodelpredictionsto Learnshierarchicalrepresentationsfrom
Definition
improveaccuracyandrobustness. rawdatathroughmultiplelayers.
Effectivewithsmalltomedium-sized Typicallyrequireslargelabeleddatasets
DataRequirements
datasets. foroptimalperformance.
Generallylessdemanding,dependingon Computationallyintensive,often
ComputationalComplexity
thebasemodelsused. requiringGPUsorTPUs.
Moreinterpretable,asindividualmodel Lessinterpretableduetocomplexfeature
Interpretability
contributionscanbeanalyzed. transformations.
Aggregatespredictionsviamajority
Integratesfeaturesacrossmultiplelayers
FusionMethod voting,averaging,orweighted
forfinalpredictions.
combinations.
Reducesbias,variance,orbothby Excelsatfeatureextractionandhandling
Strengths
leveragingmodeldiversity. high-dimensionaldata.
Performancedependsonthequalityand Pronetooverfittingandrequirescareful
Weaknesses
diversityofbaselearners. tuningandregularization.
Suitableforclassification,regression,and Idealforimagerecognition,NLP,and
Applications
anomalydetection. speechanalysis.
18. EmpiricalValidationfromtheLiterature
Thispaperprovidesatheoreticalandmethodologicalanalysisofensemblelearning
techniquesratherthananempiricalcomparison. Whileexperimentalvalidationisvaluable,
numerousstudieshavealreadyconductedextensivebenchmarkingofensemblemethods
(e.g.,[70,71,149,152]). Instead,ourfocusisonsystematicallyanalyzingthetheoreticalfoun-
dations,algorithmicproperties,andcomputationaltrade-offsofthesemethods,offering
insightsthatcomplementexistingempiricalstudies. Thisapproachallowsforabroader,
model-agnosticdiscussionapplicabletodiverseproblemdomains.
Empiricalstudieshavedemonstratedtheeffectivenessofensemblemethodsacross
variousdomains. Bagginghasbeenextensivelyvalidatedforitsabilitytoreducevariance,
particularlyforhigh-variancemodelslikedecisiontrees[3]. Randomforests,awidelyused
bagging-basedmethod,consistentlyoutperformindividualdecisiontreesinstructured
dataapplicationsduetotheirrobustnessandgeneralizationability[12].
Boostingalgorithms,suchasAdaBoostandgradientboosting,focusonreducingbias
toachievesuperiorpredictiveperformance. Experimentalstudiesindicatethatboosting
oftenoutperformsbaggingwhenappliedtostructureddatasets[8,70]. XGBoost,amodern
implementation of gradient boosting, has gained widespread adoption in data science
competitionsduetoitscomputationalefficiencyandhighaccuracy[71].
Comparativestudieshaveexploredthestrengthsandweaknessesofensemblemeth-
odsunderdifferentconditions. Researchsuggeststhatboostingtendstoexcelinlow-noise
scenarios,whereasbaggingismorerobustinhigh-noiseenvironments[9,77]. However,
recent advancements in random forests, such as WildWood [149] and other improved
variants[152],indicatethatthesemethodsmayoutperformgradientboostingincertainap-
plications. Foracomprehensiveempiricalcomparisonofstate-of-the-artgradientboosting
methodsandrandomforests,see[149,152].
These empirical findings validate the theoretical principles discussed earlier and
highlightthepracticaladvantagesofensemblemethodsinvariousreal-worldapplications.

Mathematics2025,13,587 34of49
PracticalApplicationsofEnsembleMethods
Beyond theoretical insights, ensemble methods have been successfully applied in
variousreal-worlddomains:
• Finance: Random forests and gradient boosting models are widely used in fraud
detection, whereensemblelearninghelpsidentifyanomaloustransactionpatterns
withhighaccuracy[374].
• Healthcare: Inmedicaldiagnosis,ensemblemethodsimprovediseasepredictionmod-
elsbyaggregatingmultipleclassifierstrainedonpatientrecords[375]. Forexample,
boosting-basedmodelshavebeenemployedforearlycancerdetection[376].
• Cybersecurity: Intrusion detection systems (IDS) benefit from ensemble learning
bycombiningmultipleweakanomalydetectors, leadingtoenhancedthreatdetec-
tion[377].
• Autonomoussystems: Inself-drivingcars,ensemblesofdeeplearningmodelshelp
improveobjectdetectionandsceneunderstanding,increasingsafetyinreal-world
deployment[378].
Thesuccessfulapplicationofensemblemethodsinthesediversefieldsdemonstrates
theirpracticalrelevanceandeffectiveness,reinforcingtheirimportancebeyondtheoretical
considerations.
19. FutureResearchDirections
Despitethesignificantadvancementsinensemblelearning,severalopenchallenges
andpromisingdirectionsremain. Onekeyareaisthedevelopmentofadaptiveensemble
methods that dynamically adjust model selection and weighting based on data charac-
teristicsandevolvingdistributions. Researchonself-adaptiveboosting[72]hasshown
initialpromise,butfurtherexplorationisneededtoimproverobustnessinnon-stationary
environments.
19.1. TheoreticalAnalysisofEnsembleLearning
Currently,theoreticalanalysesofvariousensemblelearningmethodsprimarilyrelyon
gradientdescentorBayesianframeworks. Developingageneralanalyticalframeworkthat
appliestoallensemblelearningmodelsremainsasignificantchallenge. Todate,analyses
havelargelyconcentratedonempiricallysuccessfulmethodssuchasAdaBoostandrandom
forests. However,newermodels,suchasGBDTs,demandfurthertheoreticalinvestigation.
Adeeperexplorationofgeneralizationboundsforensemblemethodsisalsoneces-
sary. Whilemargin-basedanalysis[62]providesafoundation, morerefinedtheoretical
guarantees,particularlyformodernboostingandbaggingvariants,remainanopenchal-
lenge. Investigatingthetrade-offsbetweenmodelcomplexity, computationalcost, and
generalizationcouldfurtherenhanceensemblemethodologies.
Asboostingmethodscontinuetoadvancethefrontiersofpredictivemodeling,sig-
nificantopportunitiesariseforfurtherinnovation. TheremarkablesuccessofXGBoost
underscores the critical role of computational efficiency and algorithmic refinement in
machinelearning. Futureresearchcoulddelvedeeperintotheseareas,exploringnovel
algorithms and optimizations that build upon existing boosting frameworks. Such en-
deavorsmayuncovernewapproachesthatsignificantlyenhancepredictiveperformance
acrossdiverseapplications. Investigatingthesynergybetweenboostingmethodsandother
emergingtechniques,likedeeplearningorautomatedmachinelearning(AutoML),might
alsoopennewpathwaysforinnovationinpredictiveanalytics.

Mathematics2025,13,587 35of49
19.2. IntegrationofEnsembleLearningandDeepLearning
Deep learning has undoubtedly become a defining feature of modern AI research.
Manystudieshaveexploredintegratingensemblelearningwithdeeplearning[379,380].
While much effort has been directed toward developing highly powerful deep neural
networksthatoutperformexistingmethods,thisisnotuniversallynecessary. Deepmodels
mayexcelonspecificdatasetsbutdonotconsistentlyoutperformotherapproachesacross
alldatasets,inlinewiththeno-free-lunchtheorem. Thistheoremunderscoresthelimita-
tionsofdeepnetworks,particularlyregardingtheirtrainingcomplexityanddependency
onextensivedatasets.
Ensemblelearning,beingalow-costapproachtoachievinghighreliability,offersa
valuablecomplementtodeeplearning. Integratingthetwomethodscanenhancedecision-
makingreliabilityatamoderatecomputationalcost,makingitapromisingdirectionfor
futureresearch. Futureresearchshouldinvestigatehowtobestoptimizehybridmodelsby
balancinginterpretability,computationalefficiency,andgeneralizationability.
19.3. MultimodalDataFusion
Anotherimportantresearchdirectionisthedevelopmentofadvancedframeworks
formultimodaldatafusion. Leveragingmoderncomputingarchitecturesandparameter
compressiontechniquesindeeplearningcouldsignificantlyimprovetheefficiencyand
scalability of multimodal frameworks. While considerable progress has been made in
compressingparametersforsingle-modalityfeaturelearning,thesetechniquescouldalso
beadaptedformultimodalmodelstoenhancetheirperformanceandefficiency.
Multimodaldatacontainnotonlyinformationwithineachmodalitybutarealsorich
cross-modalrelationships. Tofullyexploittheserelationships,itisessentialtotransform
rawmodality-specificdataintohigh-levelabstractionswithinaunifiedglobalspace. These
globalrepresentationscanbeconstructedusingstrategiessuchasmultiviewfusion,transfer
learning,andprobabilisticdependencyfusion. Combiningdeeplearningtechniqueswith
semantic fusion strategies offers a promising approach to overcoming the challenges
inherentinmultimodaldataexploration.
19.4. ProcessingLow-QualityMultimodalData
Multimodal data are often collected in dynamic and unpredictable environments,
leadingtothepresenceofnoisyorlow-qualitydata. Thereisanurgentneedforrobust
deep learning models capable of effectively handling such data. Developing models
thatcanprocesslow-qualitymultimodalinputswithoutsignificantlossofperformance
represents a critical challenge for future research. New regularization techniques and
uncertainty-awarelearningframeworksshouldbeexploredtomitigatetheimpactofnoise
andmissinginformationinmultimodallearningsystems.
Byaddressingthesechallengesandexploringtheoutlineddirections,futureresearch
cansignificantlyadvancethecapabilitiesandapplicationsofensemblelearningandits
integrationwithdeeplearning.
20. Conclusions
Several review articles focus on traditional ensemble learning methods [381,382],
ensemblelearningfordatastreamclassification[383],ensembledeeplearningapproaches
inbioinformatics[380],andsurveysthatdiscussbothtraditionalensembletechniquesand
ensembledeeplearning[379].Additionally,deeplearningapplicationsformultimodaldata
fusionareexploredin[384]. However,thesearticlesoftenconcentrateonnarrowtopics
or provide limited references. In contrast, our survey offers a far more comprehensive
overview,coveringtopicsrangingfromconventionalensemblelearningmethodsandtheir

Mathematics2025,13,587 36of49
theoreticalfoundationstotheirrelationshipwithdeeplearning,aswellasrelatedareassuch
asmultiviewlearningandmultiplekernellearning. Furthermore,ourworkisdesignedto
serveasatutorialonensemblelearning,makingitaccessibletoabroadaudience.
Inthissurvey,wehavesummarizedfundamentalconcepts,theoreticalinsights,and
practicaladvancementsinensemblelearning. Wehavealsohighlightedkeymethodologies,
suchasboosting,bagging,andstacking,alongsidetheirintegrationwithdeeplearning
techniques. Byanalyzingboththeoreticalandempiricalevidence,weprovideastructured
understandingofensemblemethodsthatcanbenefitbothresearchersandpractitioners.
Futureresearchshouldfocusonaddressingtheoreticalgaps,improvingtheefficiency
ofensembletechniques,andexploringnovelapplicationsindeeplearningandmultimodal
datafusion. Continuedadvancementsintheseareaswillfurtherenhancetherobustness,
interpretability,andeffectivenessofensemblelearningmethodsinreal-worldapplications.
AuthorContributions:Theauthorscollaboratedcloselyandcontributedsignificantlytoallaspects
ofthework.Allauthorshavereadandagreedtothepublishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
DataAvailabilityStatement:Nonewdatawerecreatedoranalyzedinthisstudy.
ConflictsofInterest: AuthorRengongZhangisemployedatZhejiangYugongInformationTechnol-
ogyCo.LtdandauthorJieZengisemployedatShenzhenFengXingTaiBaoTechnologyCo.Ltd.
Theauthorsdeclarethattheyhavenoknowncompetingfinancialinterestsorpersonalrelationships
thatcouldhaveappearedtoinfluencetheworkreportedinthispaper.
Abbreviations
AdaBoost adaptiveboosting
ADMM alternatingdirectionmethodofmultipliers
AE autoencoder
Agghoo aggregatedhold-out
ARCing adaptiveresamplingandcombining
bagging bootstrapaggregating
BPA basicprobabilityassignment
CART classificationandregressiontrees
CCA canonicalcorrelationanalysis
DAGSVM directedacyclicgraphSVM
ECOC error-correctingoutputcodes
EKF extendedKalmanfilter
EM expectation-maximization
EnKF ensembleKalmanfilter
FCM fuzzyC-means
GBDT gradient-boosteddecisiontree
GBM gradientboostingmachines
GFDC granulefusiondensity-basedclusteringwithevidentialreasoning
k-NN k-nearestneighbors
LDA lineardiscriminantanalysis
LP linearprogramming
MCMC MarkovChainMonteCarlo
mDA marginalizeddenoisingautoencoder
MFC-ACL multiviewfusionclusteringwithattentivecontrastivelearning
MKL multiplekernellearning
MSE meansquarederror
MVRL multiviewrepresentationlearning
NMF nonnegativematrixfactorization

Mathematics2025,13,587 37of49
MULPP multiviewuncorrelatedlocality-preservingprojection
OPLS orthogonalpartialleastsquares
OWA orderedweightedaveraging
OXT onlineextratrees
PAC probablyapproximatelycorrect
PCA principalcomponentanalysis
pdf probabilitydensityfunction
PLS partialleastsquares
QCQP quadraticallyconstrainedquadraticprogram
RBF radialbasisfunction
RC randomizedcombination
ReLU rectifiedlinearunit
ResNet residualnetwork
RTRL real-timerecurrentlearning
SDP semidefiniteprogramming
SNR signal-to-noiseratio
SPORF sparseprojectionobliquerandomerforests
SVM supportvectormachine
TFFC transformerfeaturefusioncontrastivemodule
XGBoost extremegradientboosting
References
1. Tumer,K.;Ghosh,J.Analysisofdecisionboundariesinlinearlycombinedneuralclassifiers.PatternRecognit.1996,29,341–348.
[CrossRef]
2. Shafer,G.AMathematicalTheoryofEvidence;PrincetonUniversityPress:Princeton,NJ,USA,1976.
3. Breiman,L.Baggingpredictors.Mach.Learn.1996,24,123–140.[CrossRef]
4. Schapire,R.E.Thestrengthofweaklearnability.Mach.Learn.1990,5,197–227.[CrossRef]
5. Du,K.-L.;Swamy,M.N.S.WirelessCommunicationSystems;CambridgeUniversityPress:Cambridge,UK,2010.
6. Koliander,G.;El-Laham,Y.;Djuric,P.M.;Hlawatsch,F.Fusionofprobabilitydensityfunctions.Proc.IEEE2022,110,404–453.
[CrossRef]
7. Ting, K.M.; Witten, I.H. Stackingbaggedand daggedmodels. InProceedings ofthe International Conferenceon Machine
Learning(ICML),Nashville,TN,USA,8–12July1997.
8. Freund,Y.;Schapire,R.E.Adecision-theoreticgeneralizationofon-linelearningandanapplicationtoboosting.J.Comput.Syst.
Sci.1997,55,119–139.[CrossRef]
9. Bauer,E.;Kohavi,R.Anempiricalcomparisonofvotingclassificationalgorithms:Bagging,boosting,andvariants.Mach.Learn.
1999,36,105–139.[CrossRef]
10. Webb,G.I.MultiBoosting:Atechniqueforcombiningboostingandwagging.MachLearn.2000,40,159–196.[CrossRef]
11. Ho,T.K.Therandomsubspacemethodforconstructingdecisionforests.IEEETrans.Pat.Anal.Mach.Intell.1998,20,832–844.
12. Breiman,L.Randomforests.Mach.Learn.2001,45,5–32.[CrossRef]
13. Rodriguez,J.J.;Kuncheva,L.I.;Alonso,C.J.Rotationforest:Anewclassifierensemblemethod.IEEETrans.Pat.Anal.Mach.Intell.
2006,28,1619–1630.[CrossRef][PubMed]
14. Liu,Y.;Yao,X.Ensemblelearningvianegativecorrelation.NeuralNetw.1999,12,1399–1404.[CrossRef]
15. Hansen,L.K.;Salamon,P.Neuralnetworkensembles.IEEETransPat.Anal.Mach.Intell.1990,12,993–1001.[CrossRef]
16. Szegedy,C.;Liu,W.;Jia,Y.;Sermanet,P.;Reed,S.;Anguelov,D.;Erhan,D.;Vanhoucke,V.;Rabinovich,A.Goingdeeperwith
convolutions.InProceedingsoftheIEEEConferenceonComputerVisionandPatternRecognition(CVPR),Boston,MA,USA,
7–12June2015;pp.1–9.
17. Moghimi, M.; Belongie, S. J.; Saberian, M.; Yang, J.; Vasconcelos, N.; Li, L.-J. Boosted convolutional neural networks. In
ProceedingsoftheBritishMachineVisionConference(BMVC),Dundee,UK,19–22September2016;pp.1–13.
18. Huang,G.;Li,Y.;Pleiss,G.;Liu,Z.;Hopcroft,J.E.;Weinberger,K.Q.Snapshotensembles:Train1,getMforfree.InProceedings
oftheInternationalConferenceonLearningRepresentations(ICLR),Toulon,France,24–26April2017;pp.1–9.
19. Wyner,A.J.;Olson,M.;Bleich,J.;Mease,D.ExplainingthesuccessofAdaBoostandrandomforestsasinterpolatingclassifiers.
J.Mach.Learn.Res.2017,18,1–33.
20. Ho,T.K.Randomdecisionforests.InProceedingsofthe3rdInternationalConferenceonDocumentAnalysisandRecognition
(ICDAR),Montreal,QC,Canada,14–16August1995;Volume1,pp.278–282.

Mathematics2025,13,587 38of49
21. Jacobs,R.A.;Jordan,M.I.;Nowlan,S.J.;Hinton,G.E.Adaptivemixturesoflocalexperts.NeuralComput.1991,3,79–87.[CrossRef]
22. Jiang,W.TheVCdimensionformixturesofbinaryclassifiers.NeuralComput.2000,12,1293–1301.[CrossRef][PubMed]
23. Tresp,V.ABayesiancommitteemachine.NeuralComput.2000,12,2719–2741.[CrossRef][PubMed]
24. Domingos,P.Bayesianaveragingofclassifiersandtheoverfittingproblem.InProceedingsofthe17thInternationalConference
onMachineLearning,Stanford,CA,USA,29June–2July2000;MorganKaufmann:SanMateo,CA,USA,2020;pp.223–230.
25. Wolpert,D.H.Stackedgeneralization.NeuralNetw.1992,5,241–259.[CrossRef]
26. Wolpert,D.;Macready,W.G.CombiningStackingwithBaggingtoImproveaLearningAlgorithm;TechnicalReport;SantaFeInst.:
SantaFe,NM,USA,1996;p.30.
27. Clarke,B.ComparingBayesmodelaveragingandstackingwhenmodelapproximationerrorcannotbeignored.J.Mach.Learn.
Res.2003,4,683–712.
28. Lakshminarayanan,B.;Pritzel,A.;Blundell,C.Simpleandscalablepredictiveuncertaintyestimationusingdeepensembles.In
ProceedingsoftheAdvancesinNeuralInformationProcessingSystems(NeurIPS),LongBeach,CA,USA,4–9December2017;
pp.3140–3148.
29. Zhou,Z.-H.EnsembleMethods:FoundationsandAlgorithms,2nded.;ChapmanandHall/CRC:BocaRaton,FL,USA,2021.
30. Du, K.-L.; Swamy, M.N.S. Search and Optimization by Metaheuristics: Techniques and Algorithms Inspired by Nature; Springer:
NewYork,NY,USA,2016.
31. Zhang,B.;Wu,Y.;Lu,J.;Du,K.-L.EvolutionaryComputationandItsApplicationsinNeuralandFuzzySystems.Appl.Comput.
Intell.SoftComput.2011,2011,938240.[CrossRef]
32. Vanschoren,J.Meta-learning:ASurvey.arXiv2018,arXiv:1810.03548.
33. Kim,W.;Goyal,B.;Chawla,K.;Lee,J.;Kwon,K.Attention-basedensemblefordeepmetriclearning. InProceedingsofthe
EuropeanConferenceonComputerVision(ECCV),Munich,Germany,8–14September2018;pp.736–751.
34. Sha,C.;Wang,K.;Wang,X.;Zhou,A.Ensemblepruning:Asubmodularfunctionmaximizationperspective.InDatabaseSystems
forAdvancedApplications;LNCS;Springer:Cham,Switzerland,2014;Volume8422,pp.1–15.
35. Du,K.-L.;Zhang,R.;Jiang,B.;Zeng,J.;Lu,J.Understandingmachinelearningprinciples:Learning,inference,generalization,
andcomputationallearningtheory.Mathematics2025,13,451.[CrossRef]
36. Du,K.-L.;Swamy,M.N.S.NeuralNetworksandStatisticalLearning,2nded.;Springer:London,UK,2019.
37. Du,K.-L.;Jiang,B.;Lu,J.;Hua,J.;Swamy,M.N.S.Exploringkernelmachinesandsupportvectormachines:Principles,techniques,
andfuturedirections.Mathematics2024,12,3935.[CrossRef]
38. Dietterich,T.G.;Bakiri,G.Solvingmulticlasslearningproblemsviaerror-correctingoutputcodes. J.Artif. Intell. Res. 1995,2,
263–286.[CrossRef]
39. Li,H.;Song,J.;Xue,M.;Zhang,H.;Song,M.Asurveyofneuraltrees:Co-evolvingneuralnetworksanddecisiontrees.IEEE
Trans.NeuralNetw.Learn.Syste.2025.[CrossRef]
40. Tsybakov,A.B.Optimalaggregationofclassifiersinstatisticallearning.Ann.Stat.2004,32,135–166.[CrossRef]
41. Du,K.-L.;Swamy,M.N.S.NeuralNetworksinaSoftcomputingFramework;Springer:London,UK,2006.
42. Yager,R.R.Onorderedweightedaveragingaggregationoperatorsinmulticriteriadecision-making.IEEETrans.Syst.ManCybern.
1988,18,183–190.[CrossRef]
43. Salmon,J.;Dalalyan,A.S.Optimalaggregationofaffineestimators.InProceedingsofthe24thAnnualConferenceonLearning
Theory(COLT),Budapest,Hungary,9–11June2011;pp.635–660.
44. Maillard,G.;Arlot,S.;Lerasle,M.Aggregatedhold-out.J.Mach.Learn.Res.2021,22,1–55.
45. Hoyos-Idrobo, A.; Schwartz, Y.; Varoquaux, G.; Thirion, B. Improving sparse recovery on structured images with bagged
clustering.InProceedingsoftheIEEE2015InternationalWorkshoponPatternRecognitioninNeuroImaging(PRNI),Stanford,
CA,USA,10–12June2015;pp.73–76.
46. Varoquaux,G.;Raamana,P.R.;Engemann,D.A.;Hoyos-Idrobo,A.;Schwartz,Y.;Thirion,B.Assessingandtuningbraindecoders:
Crossvalidation,caveats,andguidelines.NeuroImage2017,145,166–179.[CrossRef]
47. Jung,Y.;Hu,J.AK-foldaveragingcross-validationprocedure.J.Nonparam.Statist.2015,27,167–179.[CrossRef][PubMed]
48. Hall,P.;Robinson,A.P.Reducingvariabilityofcrossvalidationforsmoothing-parameterchoice. Biometrika2009,96,175–186.
[CrossRef]
49. Rokach,L.Ensemble-basedclassifiers.Artif.Intell.Rev.2010,33,1–39.[CrossRef]
50. Chan,L.-W.Weightedleastsquareensemblenetworks. InProceedingsoftheIEEEInternationalJointConferenceonNeural
Networks(IJCNN),Washington,DC,USA,10–16July1999;Volume2,pp.1393–1396.
51. McAllester,D.A.PAC-Bayesianmodelaveraging.InProceedingsofthe12thACMAnnualConferenceComputationalLearning
Theory(COLT),SantaCruz,CA,USA,6–9July1999;pp.164–170.
52. Langford,J.;Shawe-Taylor,J.PAC-Bayes&margins.InProceedingsoftheAdvancesinNeuralInformationProcessingSystems,
Vancouver,BC,Canada,9–14December2002;Volume15,pp.423–430.

Mathematics2025,13,587 39of49
53. McAllester,D.SimplifiedPAC-Bayesianmarginbounds.InComputationalLearningTheoryandKernelMachines;LNCS;Springer:
NewYork,NY,USA,2003;Volume2777,pp.203–215.
54. Lacasse,A.;Laviolette,F.;Marchand,M.;Germain,P.;Usunier,N.PAC-Bayesboundsfortheriskofthemajorityvoteandthe
varianceoftheGibbsclassifier. InAdvancesinNeuralInformationProcessingSystems;MITPress: Cambridge,MA,USA,2006;
Volume19,pp.769–776.
55. Laviolette,F.;Marchand,M.;Roy,J.-F.FromPAC-Bayesboundstoquadraticprogramsformajorityvotes.InProceedingsofthe
28thInternationalConferenceonMachineLearning(ICML),Bellevue,WA,USA,28June–2July2011;pp.649–656.
56. Germain,P.;Lacasse,A.;Laviolette,F.;Marchand,M.;Roy,J.-F.Riskboundsforthemajorityvote:FromaPAC-Bayesiananalysis
toalearningalgorithm.J.Mach.Learn.Res.2015,16,787–860.
57. Bellet,A.;Habrard,A.;Morvant,E.;Sebban,M.Learningaprioriconstrainedweightedmajorityvotes.Mach.Learn.2014,97,
129–154.[CrossRef]
58. Gelman,A.;Carlin,J.B.;Stern,H.S.;Rubin,D.B.BayesianDataAnalysis;Chapman&Hall/CRC:London,UK,2004.
59. Kuncheva,L.I.CombiningPatternClassifiers:MethodsandAlgorithms,2nded.;Wiley:Hoboken,NJ,USA,2014.
60. Opitz,D.;Maclin,R.Popularensemblemethods:Anempiricalstudy.J.Artif.Intell.Res.1999,11,169–198.[CrossRef]
61. Ueda,N.;Nakano,R.GeneralizationErrorofEnsembleEstimators.IEEETrans.Pat.Anal.Mach.Intell.1996,20,871–885.
62. Schapire,R.E.;Freund,Y.;Bartlett,P.L.;Lee,W.S.Boostingthemargin:Anewexplanationfortheeffectivenessofvotingmethods.
Ann.Stat.1998,26,1651–1686.
63. Bastos,M.A.M.;deOliveira,H.B.C.;Valle,C.A.Anoptimalpruningalgorithmofclassifierensembles:Dynamicprogramming
approach.NeuralComput.Appl.2020,32,6345–6358.
64. Friedman,J.;Hastie,T.;Tibshirani,R.Additivelogisticregression:Astatisticalviewofboosting.Ann.Stat.2000,28,337–407.
[CrossRef]
65. Lemense,G.;Liu,H.Stratifiedbaggingforimbalancedclassification.Pat.Recogn.2022,130,108801.
66. Ganaie,M.A.;Hu,M.;Tanveer,M.;Chen,Y.Ensembledeeplearning:Areview.Artif.Intell.Rev.2022,55,4431–4486.[CrossRef]
67. Li,Y.;Zhao,X.Kernel-enhancedbaggingforhigh-dimensionaldataclassification.IEEETrans.NeuralNetw.Learn.Syst.2023,34,
5891–5904.
68. Oza,N.C.;Russell,S.Onlinebaggingandboosting.InProceedingsofthe18thInternationalWorkshopArtificialIntelligenceand
Statistics(AISTATS),KeyWest,FL,USA,1–3April2001;MorganKaufmann:SanMateo,CA,USA,2001;pp.105–112.
69. Lee,H.K.H.;Clyde,M.A.LosslessonlineBayesianbagging.J.Mach.Learn.Res.2004,5,143–151.
70. Friedman,J.H.Greedyfunctionapproximation:Agradientboostingmachine.Ann.Stat.2001,29,1189–1232.[CrossRef]
71. Chen, T.; Guestrin, C. XGBoost: A scalable tree boosting system. In Proceedings of the 22nd ACM SIGKDD International
ConferenceonKnowledgeDiscoveryandDataMining(KDD),SanFrancisco,CA,USA,13–17August2016;pp.785–794.
72. Zhou,Z.-H.Self-AdaptiveBoostingforNoisyData.IEEETrans.PatternAnal.Mach.Intell.2021,43,712–728.
73. Freund,Y.;Schapire,R.E.Experimentswithanewboostingalgorithm.InProceedingsofthe13thInternationalConferenceon
MachineLearning,Bari,Italy,3–6July1996;MorganKaufmann:SanMateo,CA,USA,1996;pp.148–156.
74. Breiman,L.Populationtheoryforpredictorensembles.Ann.Stat.2004,32,1–11.[CrossRef]
75. Aravkin,A.Y.;Bottegal,G.;Pillonetto,G.Boostingasakernel-basedmethod.Mach.Learn.2019,108,1951–1974.[CrossRef]
76. Muhlbaier,M.D.;Topalis,A.;Polikar,R.Learn++.NC:Combiningensembleofclassifierswithdynamicallyweightedconsult-and-
voteforefficientincrementallearningofnewclasses.IEEETrans.NeuralNetw.2009,20,152–168.[CrossRef][PubMed]
77. Dietterich,T.G.Anexperimentalcomparisonofthreemethodsforconstructingensemblesofdecisiontrees:Bagging,boosting,
andrandomization.Mach.Learn.2000,40,139–158.[CrossRef]
78. Buhlmann,P.;Yu,B.BoostingwiththeL loss:Regressionandclassification.J.Amer.Stat.Assoc.2003,98,324–339.[CrossRef]
2
79. Ratsch,G.;Onoda,T.;Muller,K.-R.SoftmarginsforAdaBoost.Mach.Learn.2001,43,287–320.[CrossRef]
80. Mease,D.;Wyner,A.Evidencecontrarytothestatisticalviewofboosting.J.Mach.Learn.Res.2008,9,131–156.
81. Johnson,R.;Zhang,T.Learningnonlinearfunctionsusingregularizedgreedyforest.IEEETrans.Pat.Anal.Mach.Intell.2013,36,
942–954.[CrossRef][PubMed]
82. Ke,G.;Meng,Q.;Finley,T.;Wang,T.;Chen,W.;Ma,W.;Ye,Q.;Liu,T.-Y.LightGBM:Ahighlyefficientgradientboostingdecision
tree.InAdvancesinNeuralInformationProcessingSystems;CurranAssociates,Inc.:RedHook,NY,USA,2017;pp.3146–3154.
83. Prokhorenkova,L.;Gusev,G.;Vorobev,A.;Dorogush,A.V.;Gulin,A.CatBoost:Unbiasedboostingwithcategoricalfeatures.In
ProceedingsoftheAdvancesinNeuralInformationProcessingSystems(NeurIPS),Montreal,QC,Canada,3–8December2018;
pp.6638–6648.
84. Grinsztajn,L.;Oyallon,E.;Varoquaux,G.Whydotree-basedmodelsstilloutperformdeeplearningontypicaltabulardata?
InProceedingsofthe36thConferenceonNeuralInformationProcessingSystems(NeurIPS)DatasetsBenchmarksTrack,New
Orleans,LA,USA,28November–9December2022;pp.1–14.
85. Shwartz-Ziv,R.;Armon,A.Tabulardata:Deeplearningisnotallyouneed.Inf.Fusion2022,81,84–90.[CrossRef]

Mathematics2025,13,587 40of49
86. Guestrin,C.PAC-Learning,VCDimensionandMargin-BasedBounds;LectureNotesfor10-701/15-781:MachineLearning;Carnegie
MellonUniversity:Pittsburgh,PA,USA,2006.Availableonline:https://www.cs.cmu.edu/~guestrin/Class/10701-S07/Slides/
learning-theory2-big-picture.pdf(accessedon1February2025).)
87. Schapire,R.E.;Singer,Y.Improvedboostingalgorithmsusingconfidence-ratedpredictions. Mach. Learn. 1999,37,297–336.
[CrossRef]
88. Collins,M.;Schapire,R.E.;Singer,Y.Logisticregression,AdaBoostandBregmandistances. Mach. Learn. 2002,47,253–285.
[CrossRef]
89. Bartlett,P.L.;Traskin,M.AdaBoostisconsistent.J.Mach.Learn.Res.2007,8,2347–2368.
90. Mukherjee,I.;Rudin,C.;Schapire,R.E.TherateofconvergenceofAdaBoost.J.Mach.Learn.Res.2013,14,2315–2347.
91. Ratsch,G.;Warmuth,M.K.Efficientmarginmaximizingwithboosting.J.Mach.Learn.Res.2005,6,2153–2175.
92. Shalev-Shwartz,S.;Singer,Y.Ontheequivalenceofweaklearnabilityandlinearseparability: Newrelaxationsandefficient
boostingalgorithms.Mach.Learn.2010,80,141–163.[CrossRef]
93. Li,S.Z.;Zhang,Z.FloatBoostlearningandstatisticalfacedetection. IEEETrans. Pat. Anal. Mach. Intell. 2004,26,1112–1123.
[CrossRef]
94. Gambs,S.;Kegl,B.;Aimeur,E.Privacy-preservingboosting.DataMin.Knowl.Discov.2007,14,131–170.[CrossRef]
95. Buhlmann,P.;Hothorn,T.Boostingalgorithms:Regularization,predictionandmodelfitting.Statist.Sci.2007,22,477–505.
96. Servedio,R.A.Smoothboostingandlearningwithmaliciousnoise.J.Mach.Learn.Res.2003,4,633–648.
97. Amit,Y.;Dekel,O.;Singer,Y.Aboostingalgorithmforlabelcoveringinmultilabelproblems.InProceedingsoftheInternational
ConferenceonArtificialIntelligenceandStatistics,FortLauderdale,FL,USA,20–22April2007;pp.27–34.
98. Zhu,J.;Zou,H.;Rosset,S.;Hastie,T.Multi-classadaBoost.Stat.Interface2009,2,249–360.
99. Geist,M.Soft-maxboosting.Mach.Learn.2015,100,305–332.[CrossRef]
100. Freund,Y.Anadaptiveversionoftheboostbymajorityalgorithm.Mach.Learn.2001,43,293–318.[CrossRef]
101. Kanamori,T.;Takenouchi,T.;Eguchi,S.;Murata,N.Robustlossfunctionsforboosting. NeuralComput. 2007,19,2183–2244.
[CrossRef][PubMed]
102. Gao,C.;Sang,N.;Tang,Q.OnselectionandcombinationofweaklearnersinAdaBoost. Pat. Recogn. Lett. 2010,31,991–1001.
[CrossRef]
103. Shrestha,D.L.;Solomatine,D.P.ExperimentswithAdaBoost.RT,animprovedboostingschemeforregression.NeuralComput.
2006,18,1678–1710.[CrossRef][PubMed]
104. Viola,P.;Jones,M.Robustreal-timeobjectdetection.Int.J.Comput.Vis.2001,57,137–154.[CrossRef]
105. Saberian,M.;Vasconcelos,N.Boostingalgorithmsfordetectorcascadelearning.J.Mach.Learn.Res.2014,15,2569–2605.
106. Viola,P.; Jones,M.FastandrobustclassificationusingasymmetricAdaBoostandadetectorcascade. InAdvancesinNeural
InformationProcessingSystems;MITPress:Cambridge,MA,USA,2002;Volume14,pp.1311–1318.
107. Duffy,N.;Helmbold,D.Boostingmethodsforregression.Mach.Learn.2002,47,153–200.[CrossRef]
108. Livshits,E.Lowerboundsfortherateofconvergenceofgreedyalgorithms.Izv.Math.2009,73,1197–1215.[CrossRef]
109. Hastie,T.;Taylor,J.;Tibshirani,R.;Walther,G.Forwardstagewiseregressionandthemonotonelasso.Electron.J.Stat.2007,1,
1–29.[CrossRef]
110. Ehrlinger,J.;Ishwaran,H.CharacterizingL Boosting.Ann.Stat.2012,40,1074–1101.[CrossRef]
2
111. Zhang,T.;Yu,B.Boostingwithearlystopping:Convergenceandconsistency.Ann.Stat.2005,33,1538–1579.[CrossRef]
112. Wang,Y.;Liao,X.;Lin,S.Rescaledboostinginclassification.IEEETrans.NeuralNetw.Learn.Syst.2019,30,2598–2610.[CrossRef]
113. Quinlan,J.R.Inductionofdecisiontrees.Mach.Learn.1986,1,81–106.[CrossRef]
114. Breiman,L.;Friedman,J.H.;Olshen,R.A.;Stone,C.J.ClassificationandRegressionTrees;Chapman&Hall/CRC:London,UK,1984.
115. Genuer,R.;Poggi,J.-M.;Tuleau,C.Randomforests:Somemethodologicalinsights.arXiv2008,arXiv:0811.3619.
116. Bernard,S.;Heutte,L.;Adam,S.Influenceofhyperparametersonrandomforestaccuracy.InInternationalWorkshoponMultiple
ClassifierSystems;Springer:Berlin/Heidelberg,Germany,2009;pp.171–180.
117. Probst,P.;Boulesteix,A.-L.Totuneornottotunethenumberoftreesinrandomforest.J.Mach.Learn.Res.2017,18,1–18.
118. Fernandez-Delgado,M.;Cernadas,E.;Barro,S.;Amorim,D.Doweneedhundredsofclassifierstosolverealworldclassification
problems?J.Mach.Learn.Res.2014,15,3133–3181.
119. Biau,G.;Devroye,L.;Lugosi,G.Consistencyofrandomforestsandotheraveragingclassifiers. J.Mach. Learn. Res. 2008,9,
2015–2033.
120. Biau,G.Analysisofarandomforestsmodel.J.Mach.Learn.Res.2012,13,1063–1095.
121. Klusowski,J.M.Sharpanalysisofasimplemodelforrandomforests.InProceedingsofthe24thInternationalConferenceon
ArtificialIntelligenceandStatistics(AISTATS),Virtual,13–15April2021;pp.757–765.
122. Sexton,J.;Laake,P.Standarderrorsforbaggedandrandomforestestimators. Computat. Stat. DataAnal. 2009,53,801–811.
[CrossRef]

Mathematics2025,13,587 41of49
123. Wager,S.;Hastie,T.;Efron,B.Confidenceintervalsforrandomforests:TheJackknifeandtheinfinitesimalJackknife.J.Mach.
Learn.Res.2014,15,1625–1651.[PubMed]
124. Scornet,E.;Biau,G.;Vert,J.-P.Consistencyofrandomforests.Ann.Stat.2015,43,1716–1741.[CrossRef]
125. Wager,S.;Athey.S.Estimationandinferenceofheterogeneoustreatmenteffectsusingrandomforests.J.Amer.Stat.Assoc.2018,
113,1228–1242.[CrossRef]
126. Mentch,L.;Hooker,G.Quantifyinguncertaintyinrandomforestsviaconfidenceintervalsandhypothesistests.J.Mach.Learn.
Res.2016,17,841–881.
127. Mourtada,J.; Gaiffas,S.; Scornet,E.MinimaxoptimalratesforMondriantreesandforests. Ann. Stat. 2020,28,2253–2276.
[CrossRef]
128. Lakshminarayanan,B.;Roy,D.M.;Teh,Y.W.Mondrianforests:Efficientonlinerandomforests.InProceedingsoftheAdvancesin
NeuralInformationProcessingSystems((NeurIPS),Montreal,QC,Canada,8–13December2014;pp.3140–3148.
129. O’Reilly,E.;Tran,N.M.Minimaxratesforhigh-dimensionalrandomtessellationforests.J.Mach.Learn.Res.2024,25,1–32.
130. Scornet,E.Randomforestsandkernelmethods.IEEETrans.Inf.Theo.2016,62,1485–1500.[CrossRef]
131. Cevid,D.;Michel,L.;Naf,J.;Buhlmann,P.;Meinshausen,N.Distributionalrandomforests: Heterogeneityadjustmentand
multivariatedistributionalregression.J.Mach.Learn.Res.2022,23,1–79.
132. Lu,B.;Hardin,J.Aunifiedframeworkforrandomforestpredictionerrorestimation.J.Mach.Learn.Res.2021,22,1–41.
133. Lin,Y.;Jeon,Y.Randomforestsandadaptivenearestneighbors.J.Amer.Stat.Assoc.2006,101,578–590.[CrossRef]
134. Pospisil,T.;Lee,A.B.RFCDE:Randomforestsforconditionaldensityestimation.arXiv2018,arXiv:1804.05753.
135. Kocev,D.;Vens,C.;Struyf,J.;Dzeroski,S.Ensemblesofmulti-objectivedecisiontrees.In ProceedingsoftheEuropeanConference
onMachineLearning(ECML),Berlin,Germany,3–5September2007;pp.624–631.
136. Segal,M.;Xiao,Y.Multivariaterandomforests.WileyInterdiscip.Rev.DataMin.Knowl.Discov.2011,1,80–87.[CrossRef]
137. Ghosal,I.;Hooker,G.Boostingrandomforeststoreducebias;One-stepboostedforestanditsvarianceestimate.InProceedings
ofthe24thInternationalConferenceonArtificialIntelligenceandStatistics(AISTATS),Virtual,13–15April2021;PMLR:San
Diego,CA,USA,2021;pp.757–765.
138. Breiman,L.UsingAdaptiveBaggingtoDebiasRegressions;Technicalreport;UniversityofCalifornia,Berkeley,Departmentof
Statistics,Berkeley,CA,USA,1999.
139. Zhang,G.;Lu,Y.Bias-correctedrandomforestsinregression.J.Appl.Stat.2012,39,151–160.[CrossRef]
140. Hooker,G.;Mentch,L.Bootstrapbiascorrectionsforensemblemethods.Stat.Comput.2018,28,77–86.[CrossRef]
141. Meinshausen,N.Quantileregressionforests.J.Mach.Learn.Res.2006,7,983–999.
142. Athey,S.;Tibshirani,J.;Wager,S.Generalizedrandomforests.Ann.Stat.2019,47,1148–1178.[CrossRef]
143. Zhang,H.; Zimmerman,J.; Nettleton,D.; Nordman,D.J.Randomforestpredictionintervals. Amer. Stat. 2019,74,392-406.
[CrossRef]
144. Lei,J.; Wasserman,L.Distribution-freepredictionbandsfornon-parametricregression. J.Roy. Stat. Soc. B2014,76,71–96.
[CrossRef]
145. Johansson,U.;Bostrom,H.;Lofstrom,T.;Linusson,H.Regressionconformalpredictionwithrandomforests.Mach.Learn.2014,
97,155–176.[CrossRef]
146. Li,H.;Wang,W.;Ding,H.;Dong,J.Treesweightingrandomforestmethodforclassifyinghigh-dimensionalnoisydata. In
Proceedingsofthe2010IEEE7thInternationalConferenceonE-BusinessEngineering,Shanghai,China,10–12November2010;
pp.160–163.
147. Winham,S.J.;Freimuth,R.R.;Biernacka,J.M.Aweightedrandomforestsapproachtoimprovepredictiveperformance.Stat.Anal.
DataMin.2013,6,496–505.[CrossRef]
148. Chen,X.;Yu,D.;Zhang,X.Optimalweightedrandomforests.J.Mach.Learn.Res.2024,25,1–81.
149. Gaiffas,S.;Merad,I.;Yu,Y.WildWood:Anewrandomforestalgorithm.IEEETrans.Inf.Theory2023,69,6586–6604.[CrossRef]
150. Mourtada,J.;Gaiffas,S.;Scornet,E.AMF:AggregatedMondrianforestsforonlinelearning.J.Roy.Stat.Soc.B2021,83,505–533.
[CrossRef]
151. Capitaine,L.;Bigot,J.;Thiebaut,R.;Genuer,R.FrechetrandomforestsformetricspacevaluedregressionwithnonEuclidean
predictors.J.Mach.Learn.Res.2024,25,1–41.
152. Kouloumpris,E.;Vlahavas,I.Markowitzrandomforest:Weightingclassificationandregressiontreeswithmodernportfolio
theory.Neurocomputing2025,620,129191.[CrossRef]
153. Menze,B.H.;Kelm,B.M.;Splitthoff,D.N.;Koethe,U.;Hamprecht,F.A.Onobliquerandomforests. InMachineLearningand
KnowledgeDiscoveryinDatabases;Springer:Berlin/Heidelberg,Germany,2011;pp.453–469.
154. Blaser,R.;Fryzlewicz,P.Randomrotationensembles.J.Mach.Learn.Res.2016,17,126–151.
155. Rainforth,T.;Wood,F.Canonicalcorrelationforests.arXiv2015,arXiv:1507.05444.
156. Tomita,T.M.;Browne,J.;Shen,C.;Chung,J.;Patsolic,J.L.;Falk,B.;Priebe,C.E.;Yim,J.;Burns,R.;Maggioni,M.;etal.Sparse
projectionobliquerandomerforests.J.Mach.Learn.Res.2020,21,1–39.

Mathematics2025,13,587 42of49
157. Boot,T.;Nibbering,D.Subspacemethods.InMacroeconomicForecastingintheEraofBigData;Springer:Cham,Switzerland,2020;
pp.267–291.
158. Cannings,T.I.;Samworth,R.J.Random-projectionensembleclassication.J.R.Stat.Soc.B2017,79,959–1035.[CrossRef]
159. Garca-Pedrajas,N.;Ortiz-Boyer,D.Boostingrandomsubspacemethod.NeuralNetw.2008,21,1344–1362.[CrossRef][PubMed]
160. Tian,Y.;Feng,Y.RaSE:Randomsubspaceensembleclassification.J.Mach.Learn.Res.2021,22,1–93.
161. Blaser,R.;Fryzlewicz,P.Regularizingaxis-alignedensemblesviadatarotationsthatfavorsimplerlearners.Stat.Comput.2021,
31,15.[CrossRef]
162. Durrant, R.J.; Kaban, A.Randomprojectionsasregularizers: Learningalineardiscriminantfromfewerobservationsthan
dimensions.Mach.Learn.2015,99,257–286.[CrossRef]
163. Mukhopadhyay,M.;Dunson,D.B.Targetedrandomprojectionforpredictionfromhigh-dimensionalfeatures.J.Amer.Stat.Assoc.
2020,115,1998–2010.[CrossRef]
164. Lee,D.;Yang,M.-H.;Oh.S.Fastandaccurateheadposeestimationviarandomprojectionforests.InProceedingsoftheIEEE
InternationalConferenceonComputerVision(ICCV),Santiago,Chile,7–13December2015;pp.1958–1966.
165. Tomita,T.M.;Maggioni,M.;Vogelstein,J.T.Romao:Robustobliqueforestswithlinearmatrixoperations.InProceedingsofthe
SIAMInternationalConferenceonDataMining(SDM),Houston,TX,USA,27–29April2017;pp.498–506.
166. Biau,G.;Cadre,B.;Rouviere,L.Acceleratedgradientboosting.Mach.Learn.2019,108,971–992.[CrossRef]
167. Breiman,L.Arcingclassifiers.Ann.Stat.1998,26,801–849.
168. Popov,S.;Morozov,S.;Babenko,A.Neuralobliviousdecisionensemblesfordeeplearningontabulardata.InProceedingsofthe
7thInternationalConferenceonLearningRepresentations(ICLR),NewOrleans,LA,USA,6–9May2019;pp.1–9.
169. Yeh,C.-K.;Kim,J.S.;Yen,I.E.H.;Ravikumar,P.Representerpointselectionforexplainingdeepneuralnetworks.InProceedings
oftheAdvancesinNeuralInformationProcessingSystems(NeurIPS),Montral,QC,Canada,2–8December2018;pp.9311–9321.
170. Pruthi,G.;Liu,F.;Kale,S.;Sundararajan,M.Estimatingtrainingdatainfluencebytracinggradientdescent.InProceedingsofthe
34thInternationalConferenceonNeuralInformationProcessingSystems,Virtual,6–12December2020;Volume33,pp.9311–9321.
171. Brophy,J.;Hammoudeh,Z.;Lowd,D.Adaptingandevaluatinginfluence-estimationmethodsforgradient-boosteddecisiontrees.
J.Mach.Learn.Res.2023,24,1–48.
172. Geurts,P.;Wehenkel,L.;d’Alche-Buc,F.Gradientboostingforkernelizedoutputspaces.InProceedingsofthe24thInternational
ConferenceonMachineLearning(ICML),Corvallis,OR,USA,20–24June2007;pp.289–296.
173. Si,S.;Zhang,H.;Keerthi,S.S.;Mahajan,D.;Dhillon,I.S.;Hsieh,C.Gradientboosteddecisiontreesforhighdimensionalsparse
output. InProceedingsoftheInternationalConferenceonMachineLearning(ICML),Sydney,Australia,6–11August2017;
pp.3182–3190.
174. Zhang,Z.;Jung,C.GBDT-MO:Gradient-boosteddecisiontreesformultipleoutputs.IEEETrans.NeuralNetw.Learn.Syst.2021,
32,3156–3167.[CrossRef]
175. Li,X.;Du,B.;Zhang,Y.;Xu,C.;Tao,D.Iterativeprivilegedlearning.IEEETrans.NeuralNetw.Learn.Syst.2020,31,2805–2817.
[CrossRef]
176. Geurts,P.;Ernst,D.;Wehenkel,L.Extremelyrandomizedtrees.Mach.Learn.2006,63,3–42.[CrossRef]
177. Pedrajas,N.G.;Boyer,D.O.Improvingmulticlasspatternrecognitionbythecombinationoftwostrategies.IEEETrans.Pat.Anal.
Mach.Intell.2006,28,1001–1006.[CrossRef]
178. Platt,J.C.;Christiani,N.;Shawe-Taylor,J.LargemarginDAGsformulticlassclassification. InAdvancesinNeuralInformation
ProcessingSystems;MITPress:Cambridge,MA,USA,1999;Volume12,pp.547–553.
179. Chang,C.-C.;Chien,L.-J.;Lee,Y.-J.Anovelframeworkformulti-classclassificationviaternarysmoothsupportvectormachine.
Pat.Recogn.2011,44,1235–1244.[CrossRef]
180. Kong,E.;Dietterich,T.G.Error-correctingoutputcodingcorrectbiasandvariance. InProceedingsofthe12thInternational
ConferenceonMachineLearning(ICML),TahoeCity,CA,USA,9–12July1995;MorganKauffmanm:SanFrancisco,CA,USA,
1995;pp.313–321.
181. Allwein,E.L.;Schapire,R.E.;Singer,Y.Reducingmulticlasstobinary:Aunifyingapproachformarginclassifiers.J.Mach.Learn.
Res.2000,1,113–141.
182. Escalera,S.;Pujol,O.;Radeva,P.Onthedecodingprocessinternaryerror-correctingoutputcodes.IEEETrans.Pat.Anal.Mach.
Intell.2010,32,120–134.[CrossRef]
183. Escalera,S.;Tax,D.;Pujol,O.;Radeva,P.;Duin,R.Subclassproblemdependentdesignoferror-correctingoutputcodes.IEEE
Trans.Pat.Anal.Mach.Intell.2008,30,1041–1054.[CrossRef][PubMed]
184. Pujol,O.;Radeva,P.;Vitria,J.DiscriminantECOC:Aheuristicmethodforapplicationdependentdesignoferrorcorrecting
outputcodes.IEEETrans.Pat.Anal.Mach.Intell.2006,28,1001–1007.[CrossRef]
185. Hastie,T.;Tibshirani,R.Classificationbypairwisegrouping. InAdvancesinNeuralInformationProcessingSystems;MITPress:
Cambridge,MA,USA,1998;Volume11,pp.451–471.

Mathematics2025,13,587 43of49
186. Escalera,S.;Masip,D.;Puertas,E.;Radeva,P.;Pujol,O.Onlineerrorcorrectingoutputcodes.Pat.Recogn.Lett.2011,32,458–467.
[CrossRef]
187. Klautau,A.;Jevtic,N.;Orlitsky,A.Onnearest-neighborerror-correctingoutputcodeswithapplicationtoall-pairsmulticlass
supportvectormachines.J.Mach.Learn.Res.2003,4,1–15.
188. Dempster,A.P.Upperandlowerprobabilitiesinducedbymultivaluedmappings.Ann.Math.Stat.1967,38,325–339.[CrossRef]
189. Smets,P.Thecombinationofevidenceinthetransferablebeliefmodel. IEEETrans. Pat. Anal. Mach. Intell. 1990,12,447–458.
[CrossRef]
190. Salehy,N.;Okten,G.MonteCarloandquasi-MonteCarlomethodsforDempster’sruleofcombination.Int.J.Appr.Reason.2022,
145,163–186.[CrossRef]
191. Quost, B.; Masson, M.-H.; Denoeux, T. Classifier fusion in the Dempster-Shafer framework using optimized t-norm based
combinationrules.Int.J.Approx.Reason.2011,52,353–374.[CrossRef]
192. Zadeh,L.A.AsimpleviewoftheDempster-Shafertheoryofevidenceanditsimplicationfortheruleofcombination.AIMag.
1986,2,85–90.
193. Schubert,J.ConflictmanagementinDempster-Shafertheoryusingthedegreeoffalsity.Int.J.Approx.Reason.2011,52,449–460.
[CrossRef]
194. Dezert,J.;Smarandache,F.AnintroductiontoDSmT.arXiv2009,arXiv:0903.0279.
195. Denoeux,T.Logisticregression,neuralnetworksandDempster-Shafertheory:Anewperspective.Knowl.-BasedSyst.2019,176,
54–67.[CrossRef]
196. Cai,M.;Wu,Z.;Li,Q.;Xu,F.;Zhou,J.GFDC:Agranulefusiondensity-basedclusteringwithevidentialreasoning.Int.J.Approx.
Reason.2024,164,109075.[CrossRef]
197. Grina,F.;Elouedi,Z.;Lefevre,E.Re-samplingofmulti-classimbalanceddatausingbelieffunctiontheoryandensemblelearning.
Int.J.Approx.Reason.2023,156,1–15.[CrossRef]
198. Lanckriet,G.R.G.;Cristianini,N.;Bartlett,P.;Ghaoui,L.E.;Jordan,M.I.Learningthekernelmatrixwithsemidefiniteprogramming.
J.Mach.Learn.Res.2004,5,27–72.
199. Ong,C.S.;Smola,A.J.;Williamson,R.C.Learningthekernelwithhyperkernels.J.Mach.Learn.Res.2005,6,1043–1071.
200. Sonnenburg,S.;Ratsch,G.;Schafer,C.;Scholkopf,B.Largescalemultiplekernellearning.J.Mach.Learn.Res.2006,7,1531–1565.
201. Ye,J.;Ji,S.;Chen,J.Multi-classdiscriminantkernellearningviaconvexprogramming.J.Mach.Learn.Res.2008,9,719–758.
202. Kim,S.-J.;Magnani,A.;Boyd,S.OptimalkernelselectioninkernelFisherdiscriminantanalysis.InProceedingsoftheInternational
ConferenceonMachineLearning(ICML),Helsinki,Finland,28June–1July2006;pp.465–472.
203. Subrahmanya,N.;Shin,Y.C.Sparsemultiplekernellearningforsignalprocessingapplications.IEEETrans.Pat.Anal.Mach.Intell.
2010,32,788–798.[CrossRef]
204. Yang,H.;Xu,Z.;Ye,J.;King,I.;Lyu,M.R.Efficientsparsegeneralizedmultiplekernellearning.IEEETrans.NeuralNetw.2011,22,
433–446.[CrossRef]
205. Rakotomamonjy,A.;Bach,F.;Canu,S.;Grandvalet,Y.SimpleMKL.J.Mach.Learn.Res.2008,9,2491–2521.
206. Chapelle,O.;Rakotomamonjy,A.Secondorderoptimizationofkernelparameters.InNIPSWorkshoponKernelLearning:Automatic
SelectionofOptimalKernels,ProceedingsoftheMachineLearningResearch(PMLR),Whistler,BC,Canada,8–13December2008;PMLR:
Cambridge,MA,USA,2008;pp.465–472.
207. Kloft,M.;Brefeld,U.;Sonnenburg,S.;Zien,A.lp-normmultiplekernellearning.J.Mach.Learn.Res.2011,12,953–997.
208. Aflalo,J.;Ben-Tal,A.;Bhattacharyya,C.;Nath,J.S.;Raman,S.Variablesparsitykernellearning. J.Mach. Learn. Res. 2011,12,
565–592.
209. Suzuki,T.;Tomioka,R.SpicyMKL:Afastalgorithmformultiplekernellearningwiththousandsofkernels.Mach.Learn.2011,85,
77–108.[CrossRef]
210. Xu,X.;Tsang,I.W.;Xu,D.Softmarginmultiplekernellearning.IEEETrans.NeuralNetw.Learn.Syst.2013,24,749–761.
211. Vishwanathan,S.V.N.;Sun,Z.;Ampornpunt,N.;Varma,M.MultiplekernellearningandtheSMOalgorithm. InAdvancesin
NeuralInformationProcessingSystems;MITPress:Cambridge,MA,USA,2010;Volume23,pp.465–472.
212. Gonen,M.Bayesianefficientmultiplekernellearning.InProceedingsofthe29thInternationalConferenceonMachineLearning
(ICML),Edinburgh,UK,18–21June2012;Volume1,pp.1–8.
213. Mao,Q.;Tsang,I.W.;Gao,S.;Wang,L.Generalizedmultiplekernellearningwithdata-dependentpriors.IEEETrans.NeuralNetw.
Learn.Syst.2015,26,1134–1148.[CrossRef][PubMed]
214. Huang,H.-C.;Chuang,Y.-Y.;Chen,C.-S.Multiplekernelfuzzyclustering.IEEETrans.FuzzySyst.2012,20,120–134.[CrossRef]
215. Bickel,S.;Scheffer,T.Multi-viewclustering.InProceedingsofthe4thIEEEInternationalConferenceonDataMining(ICDM),
Brighton,UK,1–4November2004;pp.19–26.
216. Liu,X.;Dou,Y.;Yin,J.;Wang,L.;Zhu,E.Multiplekernelk-meansclusteringwithmatrix-inducedregularization.InProceedings
oftheAAAIonferenceonArtificialIntelligence,Phoenix,AZ,USA,12–17February2016;Volume30,pp.1–7.

Mathematics2025,13,587 44of49
217. Zhou,S.;Ou,Q.;Liu,X.;Wang,S.;Liu,L.;Wang,S.;Zhu,E.;Yin,J.;Xu,X.Multiplekernelclusteringwithcompressedsubspace
alignment.IEEETrans.NeuralNetw.Learn.Syst.2023,34,252–263.[CrossRef][PubMed]
218. Yao,Y.;Li,Y.;Jiang,B.;Chen,H.Multiplekernelk-meansclusteringbyselectingrepresentativekernels.IEEETrans.NeuralNetw.
Learn.Syst.2021,32,4983–4996.[CrossRef][PubMed]
219. Han,Y.;Yang,K.;Yang,Y.;Ma,Y.Localizedmultiplekernellearningwithdynamicalclusteringandmatrixregularization.IEEE
Trans.NeuralNetw.Learn.Syst.2018,29,486–499.[CrossRef]
220. Wang,C.;Chen,M.;Huang,L.;Lai,J.;Yu,P.S.Smoothnessregularizedmultiviewsubspaceclusteringwithkernellearning.IEEE
Trans.NeuralNetw.Learn.Syst.2021,32,5047–5060.[CrossRef][PubMed]
221. Wang,J.;Li,Z.;Tang,C.;Liu,S.;Wan,X.;Liu,X.Multiplekernelclusteringwithadaptivemulti-scalepartitionselection.IEEE
Trans.Know.DataEng.2024,36,6641–6652.[CrossRef]
222. Li,M.;Zhang,Y.;Ma,C.;Liu,S.;Liu,Z.;Yin,J.;Liu,X.;Liao,Q.Regularizedsimplemultiplekernelk-meanswithkernelaverage
alignment.IEEETrans.NeuralNetw.Learn.Syst.2024,35,15910–15919.[CrossRef]
223. Alioscha-Perez,M.;Oveneke,M.C.;Sahli,H.SVRG-MKL:Afastandscalablemultiplekernellearningsolutionforfeatures
combinationinmulti-classclassificationproblems.IEEETrans.NeuralNetw.Learn.Syst.2020,31,1710–1723.[CrossRef][PubMed]
224. Fu,L.;Zhang,M.;Li,H.SparseRBFnetworkswithmulti-kernels.NeuralProcess.Lett.2010,32,235–247.[CrossRef]
225. Hong,S.;Chae,J.Distributedonlinelearningwithmultiplekernels.IEEETrans.NeuralNetw.Learn.Syst.2023,34,1263–1277.
[CrossRef][PubMed]
226. Shen,Y.;Chen,T.;Giannakis,G.B.Randomfeature-basedonlinemulti-kernellearninginenvironmentswithunknowndynamics.
J.Mach.Learn.Res.2019,20,1–36.
227. Li,Y.;Yang,M.;Zhang,Z.Asurveyofmulti-viewrepresentationlearning. IEEETrans. Knowl. DataEng. 2018,31,1863–1883.
[CrossRef]
228. Zhu,J.-Y.;Park,T.;Isola,P.;Efros,A.A.Unpairedimage-to-imagetranslationusingcycle-consistentadversarialnetworks. In
ProceedingsoftheIEEEInternationalConferenceonComputerVision(ICCV),Venice,Italy,22–29October2017;pp.2223–2232.
229. Zhu,Y.;Kiros,R.;Zemel,R.;Salakhutdinov,R.;Urtasun,R.;Torralba,A.Aligningbooksandmovies:Towardsstory-likevisual
explanationsbywatchingmoviesandreadingbooks.InProceedingsoftheIEEEInternationalConferenceonComputerVision
(ICCV),Santiago,Chile,7–13December2015;pp.19–27.
230. Karpathy,A.;Fei-Fei,L.Deepvisual-semanticalignmentsforgeneratingimagedescriptions.IEEETrans.Pat.Anal.Mach.Intell.
2017,39,664–676.[CrossRef]
231. Niu,L.;Li,W.;Xu,D.;Cai,J.Anexemplar-basedmulti-viewdomaingeneralizationframeworkforvisualrecognition.IEEETrans.
NeuralNetw.Learn.Syst.2018,29,259–272.[CrossRef][PubMed]
232. Ding,Z.;Shao,M.;Fu,Y.Incompletemultisourcetransferlearning. IEEETrans. NeuralNetw. Learn. Syst. 2018,29,310–323.
[CrossRef]
233. Guan,Z.;Zhang,L.;Peng,J.;Fan,J.Multi-viewconceptlearningfordatarepresentation.IEEETrans.Knowl.DataEng.2015,27,
3016–3028.[CrossRef]
234. Deng,C.;Lv,Z.;Liu,W.;Huang,J.;Tao,D.;Gao,X.Multiviewmatrixdecomposition:Anewschemeforexploringdiscriminative
information. InProceedingsoftheInternationalJointConferenceonArtificialIntelligence(IJCAI),BuenosAires,Argentina,
25–31July2015;pp.3438–3444.
235. Srivastava,N.;Salakhutdinov,R.R.MultimodallearningwithdeepBoltzmannmachines.InProceedingsoftheNeuralInformation
ProcessingSystems(NIPS)Conference,LakeTahoe,NV,USA,3–8December2012;pp.2222–2230.
236. Hu,D.;Li,X.;Lu,X.Temporalmultimodallearninginaudiovisualspeechrecognition.InProceedingsofthe2016IEEEConference
onComputerVisionandPatternRecognition(CVPR),LasVegas,NV,USA,27–30June2016;pp.3574–3582.
237. Li,B.;Yuan,C.;Xiong,W.;Hu,W.;Peng,H.;Ding,X.Multi-viewmulti-instancelearningbasedonjointsparserepresentationand
Multi-viewdictionarylearning.IEEETrans.Pat.Anal.Mach.Intell.2017,39,2554–2560.[CrossRef]
238. Baltrusaitis,T.;Ahuja,C.;Morency,L.-P.Multimodalmachinelearning:Asurveyandtaxonomy.IEEETrans.Pat.Anal.Mach.
Intell.2019,41,423–443.[CrossRef][PubMed]
239. Zong, L.; Zhang, X.; Zhao, L.; Yu, H.; Zhao, Q. Multi-view clustering via multi-manifold regularized non-negative matrix
factorization.NeuralNetw.2017,88,74–89.[CrossRef][PubMed]
240. Yang,W.;Shi,Y.;Gao,Y.;Wang,L.;Yang,M.Incomplete-dataorientedmultiviewdimensionreductionviasparselow-rank
representation.IEEETrans.NeuralNetw.Learn.Syst.2018,29,6276–6291.[CrossRef][PubMed]
241. Peng,J.;Luo,P.;Guan,Z.;Fan,J.Graph-regularizedmulti-viewsemanticsubspacelearning.Int.J.Mach.Learn.Cybern.2019,10,
879–895.[CrossRef]
242. Du,K.-L.;Swamy,M.N.S.;Wang,Z.-Q.;Mow,W.H.Matrixfactorizationtechniquesinmachinelearning,signalprocessingand
statistics.Mathematics2023,11,2674.[CrossRef]
243. Liu,J.;Jiang,Y.;Li,Z.;Zhou,Z.-H.;Lu,H.Partiallysharedlatentfactorlearningwithmultiviewdata.IEEETrans.NeuralNetw.
Learn.Syst.2015,26,1233–1246.

Mathematics2025,13,587 45of49
244. Kim, H.; Choo, J.; Kim, J.; Reddy, C.K.; Park, H. Simultaneous discovery of common and discriminative topics via joint
nonnegativematrixfactorization.InProceedingsofthe21thACMSIGKDDInternationalConferenceonKnowledgeDiscovery
andDataMining(KDD),Sydney,Australia,10–13August2015;pp.567–576.
245. Ngiam, J.; Khosla, A.; Kim, M.; Nam, J.; Lee, H.; Ng, A.Y. Multimodal deep learning. In Proceedings of the International
ConferenceonMachineLearning(ICML),Bellevue,WA,USA,28June–2July2011;pp.689–696.
246. Zhang,C.;Fu,H.;Hu,Q.;Cao,X.;Xie,Y.;Tao,D.Generalizedlatentmulti-viewsubspaceclustering.IEEETrans.Pat.Anal.Mach.
Intell.2020,42,86–99.[CrossRef]
247. Trigeorgis,G.;Bousmalis,K.;Zafeiriou,S.;Schuller,B.W.Adeepmatrixfactorizationmethodforlearningattributerepresentations.
IEEETrans.Pat.Anal.Mach.Intell.2017,39,417–429.[CrossRef][PubMed]
248. Sharma,P.;Abrol,V.;Sao,A.K.Deep-sparse-representation-basedfeaturesforspeechrecognition.IEEE/ACMTrans.AudioSpeech
Lang.Process.2017,25,2162–2175.[CrossRef]
249. Zhao,H.;Ding,Z.;Fu,Y.Multi-viewclusteringviadeepmatrixfactorization.InProceedingsoftheAAAIConferenceonArtificial
Intelligence,SanFrancisco,CA,USA,4–9February2017;pp.2921–2927.
250. Huang,S.;Kang,Z.;Xu,Z.Auto-weightedmulti-viewclusteringviadeepmatrixdecomposition.Pat.Recogn.2020,97,107015.
[CrossRef]
251. Li,K.;Lu,J.;Zuo,H.;Zhang,G.Multi-sourcecontributionlearningfordomainadaptation.IEEETrans.NeuralNetw.Learn.Syst.
2022,33,5293–5307.[CrossRef]
252. Kettenring,J.R.Canonicalanalysisofseveralsetsofvariables.Biometrika1971,58,433–451.[CrossRef]
253. Nielsen,A.A.Multisetcanonicalcorrelationsanalysisandmultispectral,trulymultitemporalremotesensingdata.IEEETrans.
ImageProcess.2002,11,293–305.[CrossRef][PubMed]
254. Horst,P.Relationsamongmsetsofmeasures.Psychometrika1961,26,129–149.[CrossRef]
255. Luo,Y.;Tao,D.;Ramamohanarao,K.;Xu,C.;Wen,Y.Tensorcanonicalcorrelationanalysisformulti-viewdimensionreduction.
IEEETrans.Knowl.DataEng.2015,27,3111–3124.[CrossRef]
256. Lai,P.L.;Fyfe,C.Kernelandnonlinearcanonicalcorrelationanalysis.Int.J.NeuralSyst.2000,10,365–377.[CrossRef][PubMed]
257. Hsieh,W.W.Nonlinearcanonicalcorrelationanalysisbyneuralnetworks.NeuralNetw.2000,13,1095–1105.[CrossRef]
258. Andrew,G.;Arora,R.;Bilmes,J.A.;Livescu,K.Deepcanonicalcorrelationanalysis. InProceedingsofthe30thInternational
ConferenceonMachineLearning(ICML),Atlanta,GA,USA,16–21June2013;pp.1247–1255.
259. Wang,Y.;Chen,L.Multi-viewfuzzyclusteringwithminimaxoptimizationforeffectiveclusteringofdatafrommultiplesources.
ExpertSyst.Appl.2017,72,457–466.[CrossRef]
260. Bach,F.R.;Jordan,M.I.AProbabilisticInterpretationofCanonicalCorrelationAnalysis;TechnicalReport688;DepartmentofStatistics;
UniversityofCalifornia,Berkeley:Berkeley,CA,USA,2005;pp.1–11.
261. Yu,B.;Krishnapuram,S.;Rosales,R.;Rao,R.B.Bayesiancotraining.J.Mach.Learn.Res.2011,12,2649–2680.
262. Sharma,A.;Kumar,A.;Daume,H.;Jacobs,D.W.Generalizedmultiviewanalysis:Adiscriminativelatentspace.InProceedingsof
theIEEEConferenceonComputerVisionandPatternRecognition(CVPR),Providence,RI,USA,16–21June2012;pp.2160–2167.
263. Horst,P.Generalizedcanonicalcorrelationsandtheirapplicationstoexperimentaldata. J.Clin. Psychol. 1961,17,331–347.
[CrossRef][PubMed]
264. Va,J.;Santamara,I.;Perez,J.Alearningalgorithmforadaptivecanonicalcorrelationanalysisofseveraldatasets.NeuralNetw.
2007,20,139–152.[CrossRef]
265. Kan,M.;Shan,S.;Zhang,H.;Lao,S.;Chen,X.Multi-viewdiscriminantanalysis. IEEETrans. Pat. Anal. Mach. Intell. 2016,38,
188–194.[CrossRef]
266. Kuehlkamp,A.;Pinto,A.;Rocha,A.;Bowyer,K.W.;Czajka,A.Ensembleofmulti-viewlearningclassifiersforcross-domainiris
presentationattackdetection.IEEETrans.Inf.ForensicsSecur.2019,14,1419–1431.[CrossRef]
267. Somandepalli,K.;Kumar,N.;Travadi,R.;Narayanan,S.Multimodalrepresentationlearningusingdeepmultisetcanonical
correlation.arXiv2019,arXiv:1904.01775.
268. Li,D.;Dimitrova,N.;Li,M.;Sethi,I.K.Multimediacontentprocessingthroughcross-modalassociation.InProceedingsofthe
11thACMInternationalConferenceMultimedia(MULTIMEDIA),Berkeley,CA,USA,2–8November2003;pp.604–611.
269. Sun,L.;Ji,S.;Yu,S.;Ye,J.Ontheequivalencebetweencanonicalcorrelationanalysisandorthonormalizedpartialleastsquares.
InProceedingsofthe21stInternationalJointConferenceonArtificialIntelligence(IJCAI),Pasadena,CA,USA,11–17July2009;
pp.1230–1235.
270. Arenas-Garcia,J.;Camps-Valls,G.EfficientkernelorthonormalizedPLSforremotesensingapplications. IEEETrans. Geosci.
RemoteSens.2008,46,2872–2881.[CrossRef]
271. Yin,J.;Sun,S.MultiviewUncorrelatedLocalityPreservingProjection.IEEETrans.NeuralNetw.Learn.Syst.2020,31,3442–3455.
[CrossRef]
272. Shi,Y.;Pan,Y.;Xu,D.;Tsang,I.W.MultiviewalignmentandgenerationinCCAviaconsistentlatentencoding.NeuralComput.
2020,32,1936–1979.[CrossRef]

Mathematics2025,13,587 46of49
273. Hastie,T.;Buja,A.;Tibshirani,R.Penalizeddiscriminantanalysis.Ann.Stat.1995,23,73–102.[CrossRef]
274. Diethe, T.; Hardoon, D.R.; Shawe-Taylor, J.MultiviewFisherdiscriminantanalysis. InProceedingsoftheNIPSWorkshop
LearningMultipleSources,Whistler,BC,Canada,12–13December2008.
275. Sun,S.;Xie,X.;Yang,M.Multiviewuncorrelateddiscriminantanalysis.IEEETrans.Cybern.2015,46,3272–3284.[CrossRef]
276. Kan,M.;Shan,S.;Chen,X.Multi-viewdeepnetworkforcrossviewclassification. InProceedingsoftheIEEEConferenceon
ComputerVisionandPatternRecognition(CVPR),LasVegas,NV,USA,26–30June2016;pp.4847–4855.
277. Cao,G.;Iosifidis,A.;Chen,K.;Gabbouj,M.Generalizedmultiviewembeddingforvisualrecognitionandcross-modalretrieval.
IEEETrans.Cybern.2017,48,2542–2555.[CrossRef]
278. Sindhwani,V.;Rosenberg,D.S.AnRKHSformulti-viewlearningandmanifoldco-regularization.InProceedingsofthe25th
InternationalConferenceonMachineLearning(ICML),Helsinki,Finland,5–9July2008;pp.976–983.
279. Farquhar,J.D.R.;Hardoon,D.R.;Meng,H.;Shawe-Taylor,J.;Szedmak,S.Twoviewlearning:SVM-2K,theoryandpractice.In
ProceedingsoftheAdvancesinNeuralInformationProcessingSystems(NIPS),Vancouver,BC,Canada,5–8December2005;
pp.355–362.
280. Sun,S.;Chao,G.Multi-viewmaximumentropydiscrimination.InProceedingsofthe23rdInternationalJointConferenceon
ArtificialIntelligence(IJCAI),Beijing,China,3–9August2013;pp.1706–1712.
281. Chao, G.; Sun, S.Alternativemultiviewmaximumentropydiscrimination. IEEETrans. NeuralNetw. Learn. Syst. 2016, 27,
1445–1456.[CrossRef]
282. Mao,L.;Sun,S.Softmarginconsistencybasedscalablemulti-viewmaximumentropydiscrimination.InProceedingsofthe25th
InternationalJointConferenceonArtificialIntelligence(IJCAI),NewYork,NY,USA,9–15July2016;pp.1839–1845.
283. Song,G.;Wang,S.;Huang,Q.;Tian,Q.MultimodalsimilarityGaussianprocesslatentvariablemodel.IEEETrans.ImageProcess.
2017,26,4168–4181.[CrossRef][PubMed]
284. Damianou, A.C.; Ek, C.H.; Titsias, M.K.; Lawrence, N.D. Manifold relevance determination. In Proceedings of the 29th
InternationalConferenceMachineLearning(ICML),Edinburgh,UK,26June–1July2012;pp.531–538.
285. Lawrence, N.D.Gaussianprocesslatentvariablemodelsforvisualisationofhighdimensionaldata. InProceedingsofthe
Advances in Neural Information Processing Systems (NIPS), Vancouver and Whistler, BC, Canada, 8–13 December 2003;
pp.329–336.
286. Liu,Q.;Sun,S.Multi-viewregularizedGaussianprocesses.InProceedingsofthe21thPacific–AsiaConferenceonKnowledge
DiscoveryandDataMining(PAKDD),Jeju,RepublicofKorea,23–26May2017;pp.655–667.
287. Wang,L.;Li,R.-C.;Lin,W.-W.;Multivieworthonormalizedpartialleastsquares:Regularizationsanddeepextensions.IEEE
Trans.NeuralNetw.Learn.Syst.2023,34,4371–4385.[CrossRef][PubMed]
288. Bramon, R.; Boada, I.; Bardera, A.; Rodriguez, J.; Feixas, M.; Puig, J.; Sbert, M. Multimodal data fusion based on mutual
information.IEEETrans.Vis.Comput.Graph.2012,18,1574–1587.[CrossRef][PubMed]
289. Groves,A.R.;Beckmann,C.F.;Smith,S.M.;Woolrich,M.W.Linkedindependentcomponentanalysisformultimodaldatafusion.
NeuroImage2011,54,2198–2217.[CrossRef]
290. Du,K.-L.Clustering:Aneuralnetworkapproach.NeuralNetw.2010,23,89–107.[CrossRef][PubMed]
291. Tao,Z.;Liu,H.;Li,S.;Ding,Z.;Fu,Y.Marginalizedmultiviewensembleclustering.IEEETrans.NeuralNetw.Learn.Syst.2020,31,
600–611.[CrossRef][PubMed]
292. Huang,X.; Zhang,R.; Li,Y.; Yang,F.; Zhu,Z.; Zhou,Z.MFC-ACL:Multi-viewfusionclusteringwithattentivecontrastive
learning.NeuralNetw.2025,184,107055.[CrossRef][PubMed]
293. Strehl,A.;Ghosh,J.Clusterensembles—Aknowledgereuseframeworkforcombiningmultiplepartitions.J.Mach.Learn.Res.
2003,3,583–617.
294. Fred,A.L.N.;Jain,A.K.Combiningmultipleclusteringsusingevidenceaccumulation.IEEETrans.Pat.Anal.Mach.Intell.2005,
27,835–850.[CrossRef][PubMed]
295. Topchy,A.;Jain,A.K.;Punch,W.Clusteringensembles:Modelsofconsensusandweakpartitions.IEEETrans.Pat.Anal.Mach.
Intell.2005,27,1866–1881.[CrossRef]
296. Wu,J.;Liu,H.;Xiong,H.;Cao,J.;Chen,J.K-means-basedconsensusclustering:Aunifiedview.IEEETrans.Knowl.DataEng.
2015,27,155–169.[CrossRef]
297. Kumar,A.;Daume,H.,III.Aco-trainingapproachformulti-viewspectralclustering.InProceedingsofthe28thInternational
ConferenceMachineLearning(ICML),2011,Bellevue,WA,USA,28June–2July2011;pp.393–400.
298. Blaschko,M.B.;Lampert,C.H.Correlationalspectralclustering.InProceedingsoftheIEEEConferenceonComputerVisionand
PatternRecognition(CVPR),Anchorage,AL,USA,23–28June2008;pp.1–8.
299. Singh, A.P.; Gordon, G.J. Relational learning via collective matrix factorization. In Proceedings of the 14th ACM SIGKDD
InternationalConferenceKnowledgeDiscoveryDataMining(KDD),LasVegas,NV,USA,24–27August2008;pp.650–658.
300. Xia,R.;Pan,Y.;Du,L.;Yin,J.Robustmulti-viewspectralclusteringvialow-rankandsparsedecomposition.InProceedingsofthe
28thAAAIConferenceonArtificialIntelligence,QuebecCity,QC,Canada,27–31July2014;pp.2149–2155.

Mathematics2025,13,587 47of49
301. Cao,X.;Zhang,C.;Fu,H.;Liu,S.;Zhang,H.Diversity-inducedmulti-viewsubspaceclustering. InProceedingsoftheIEEE
ConferenceonComputerVisionandPatternRecognition(CVPR),Boston,MA,USA,7–12June2015;pp.586–594.
302. Liu,H.;Liu,T.;Wu,J.;Tao,D.;Fu,Y.Spectralensembleclustering. InProceedingsofthe21thACMSIGKDDInternational
ConferenceonKnowledgeDiscoveryandDataMining(KDD),Sydney,Australia,10–13August2015;pp.715–724.
303. Li,T.;Ding,C.;Jordan,M.Solvingconsensusandsemi-supervisedclusteringproblemsusingnonnegativematrixfactorization.In
Proceedingsofthe7thIEEEInternationalConferenceDataMining(ICDM),Omaha,NE,USA,28–31October2007;pp.577–582.
304. Iam-On,N.;Boongoen,T.;Garrett,S.M.;Price,C.J.Alink-basedapproachtotheclusterensembleproblem.IEEETrans.Pat.Anal.
Mach.Intell.2011,33,2396–2409.[CrossRef]
305. Yousefnezhad,M.;Huang,S.-J.;Zhang,D.WoCE:Aframeworkforclusteringensemblebyexploitingthewisdomofcrowds
theory.IEEETrans.Cybern.2018,48,486–499.[CrossRef][PubMed]
306. Tao,Z.;Liu,H.;Li,S.;Fu,Y.Robustspectralensembleclustering. InProceedingsofthe25thACMInternationalConference
InformationandKnowledgeManagement(CIKM),Indianapolis,IN,USA,24–28October2016;pp.367–376.
307. Liu,H.;Shao,M.;Li,S.;Fu,Y.Infiniteensembleforimageclustering.InProceedingsofthe22ndACMSIGKDDInternational
ConferenceKnowledgeDiscoveryandDataMining(KDD),SanFrancisco,CA,USA,13–17August2016;pp.1745–1754.
308. Pavlov,D.;Mao,J.;Dom,B.Scaling-upsupportvectormachinesusingboostingalgorithm.InProceedingsofthe15thInternational
ConferenceonPatternRecognition(ICPR)Barcelona,Spain,3–7September2000;pp.2219–2222.
309. Collobert,R.;Bengio,S.;Bengio,Y.AparallelmixtureofSVMsforverylargescaleproblems.NeuralComput.2002,14,1105–1114.
[CrossRef]
310. Valentini,G.;Dietterich,T.G.Bias-varianceanalysisofsupportvectormachinesforthedevelopmentofSVM-basedensemble
methods.J.Mach.Learn.Res.2004,5,725–775.
311. Fu,Z.;Robles-Kelly,A.;Zhou,J.MixinglinearSVMsfornonlinearclassification.IEEETrans.NeuralNetw.2010,21,1963–1975.
312. Singh,V.;Mukherjee,L.;Peng,J.;Xu,J.Ensembleclusteringusingsemidefiniteprogrammingwithapplications.Mach.Learn.
2010,79,177–200.[CrossRef]
313. Kuncheva,L.I.;Vetrov,D.P.Evaluationofstabilityofk-meansclusterensembleswithrespecttorandominitialization.IEEETrans.
Pat.Anal.Mach.Intell.2006,28,1798–1808.[CrossRef]
314. Shigei,N.;Miyajima,H.;Maeda,M.;Ma,L.BaggingandAdaBoostalgorithmsforvectorquantization.Neurocomputing2009,73,
106–114.[CrossRef]
315. Steele,B.M.Exactbootstrapk-nearestneighborlearners.Mach.Learn.2009,74,235–255.[CrossRef]
316. Mirikitani,D.T.;Nikolaev,N.EfficientonlinerecurrentconnectionistlearningwiththeensembleKalmanfilter.Neurocomputing
2010,73,1024–1030.[CrossRef]
317. Zhou,S.;Wang,J.;Wang,L.;Wan,X.;Hui,S.;Zheng,N.Inverseadversarialdiversitylearningfornetworkensemble.IEEETrans.
NeuralNetw.Learn.Syst.2024,35,7923–7935.[CrossRef]
318. Shazeer,N.;Mirhoseini,A.;Maziarz,K.;Davis,A.;Le,Q.V.;Hinton,G.E.;Dean,J.Outrageouslylargeneuralnetworks: The
sparsely-gatedmixture-of-expertslayer. InProceedingsoftheInternationalConferenceonLearningRepresentations(ICLR),
Toulon,France,24–26April2017.
319. Zhou,T.;Wang,S.;Bilmes,J.A.Diverseensembleevolution:Curriculumdata-modelmarriage.InProceedingsoftheAdvancesin
NeuralInformationProcessingSystems(NeurIPS),Montreal,QC,Canada,2–8December2018;pp.5905–5916.
320. Pang,T.;Xu,K.;Du,C.;Chen,N.;Zhu,J.Improvingadversarialrobustnessviapromotingensemblediversity.InProceedingsof
theInternationalConferenceMachineLearning(ICML),LongBeach,CA,USA,9–15June2019;pp.4970–4979.
321. Li, N.; Yu, Y.; Zhou, Z.-H. Diversity regularized ensemble pruning. In Proceedings of the Joint European Conference on
MachineLearningandKnowledgeDiscoveryinDatabases(ECMLPKDD),Bristol,UK,24–28September2012;Springer:Cham,
Switzerland,2012;pp.330–345.
322. Oshiro,T.M.;Perez,P.S.;Baranauskas,J.A.Howmanytreesinarandomforest?InProceedingsoftheMachineLearningand
DataMininginPatternRecognition(MLDM),Berlin,Germany,13–20July2012;pp.154–168.
323. Tsoumakas,G.;Partalas,I.;Vlahavas,I.Ataxonomyandshortreviewofensembleselection.InProceedingsoftheWorkshop
SupervisedandUnsupervisedEnsembleMethodsandtheirApplications(SUEMA),Patras,Greece,21–22July2008;pp.41–46.
324. Gomes,J.B.;Gaber,M.M.;Sousa,P.A.C.;Menasalvas,E.Miningrecurringconceptsinadynamicfeaturespace.IEEETrans.Neural
Netw.Learn.Syst.2014,25,95–110.[CrossRef][PubMed]
325. Kuncheva,L.I.;Whitaker,C.J.Measuresofdiversityinclassifierensemblesandtheirrelationshipwiththeensembleaccuracy.
Mach.Learn.2003,51,181–207.[CrossRef]
326. Liu, H.; Mandvikar, A.; Mody, J. An empirical study of building compact ensembles. In Advances in Web-Age Information
Management;Springer:Berlin,Germany,2004;pp.622–627.
327. Hu,X.Usingroughsetstheoryanddatabaseoperationstoconstructagoodensembleofclassifiersfordataminingapplications.
InProceedingsoftheIEEEInternationalConferenceDataMining(ICDM),SanJose,CA,USA,29November–2December2001;
pp.233–240.

Mathematics2025,13,587 48of49
328. Bonab,H.;Can,F.LessIsmore:Acomprehensiveframeworkforthenumberofcomponentsofensembleclassifiers.IEEETrans.
NeuralNetw.Learn.Syst.2019,30,2735–2745.[CrossRef][PubMed]
329. Ulas,A.;Semerci,M.;Yildiz,O.T.;Alpaydin,E.Incrementalconstructionofclassifieranddiscriminantensembles.Inf.Sci.2009,
179,1298–1318.[CrossRef]
330. Windeatt,T.; Zor,C.Ensemblepruningusingspectralcoefficients. IEEETrans. NeuralNetw. Learn. Syst. 2013,24,673–678.
[CrossRef]
331. Pietruczuk,L.;Rutkowski,L.;Jaworski,M.;Duda,P.Howtoadjustanensemblesizeinstreamdatamining?Inf.Sci.2017,381,
46–54.[CrossRef]
332. Latinne,P.;Debeir,O.;Decaestecker,C.Limitingthenumberoftreesinrandomforests.InMultipleClassifierSystems;Springer:
Berlin,Germany,2001;pp.178–187.
333. Fumera,G.;Roli,F.;Serrau,A.Atheoreticalanalysisofbaggingasalinearcombinationofclassifiers.IEEETrans.Pat.Anal.Mach.
Intell.2008,30,1293–1299.[CrossRef][PubMed]
334. Fumera,G.;Roli,F.Atheoreticalandexperimentalanalysisoflinearcombinersformultipleclassifiersystems.IEEETrans.Pat.
Anal.Mach.Intell.2005,27,942–956.[CrossRef]
335. Lopes,M.E.;Wu,S.;Lee,T.C.M.Measuringthealgorithmicconvergenceofrandomizedensembles:Theregressionsetting.SIAM
J.Math.DataSci2020,2,921–943.[CrossRef]
336. Lopes,M.E.Estimatingthealgorithmicvarianceofrandomizedensemblesviathebootstrap. Ann. Stat. 2019,47,1088–1112.
[CrossRef]
337. Zhang,Y.;Burer,S.;Street,W.N.Ensemblepruningviasemi-definiteprogramming.J.Mach.Learn.Res.2006,7,1315–1338.
338. Meynet,J.;Thiran,J.-P.Informationtheoreticcombinationofpatternclassifiers.PatternRecogn.2010,43,3412–3421.[CrossRef]
339. Tang,E.K.;Suganthan,P.N.;Yao,X.Ananalysisofdiversitymeasures.Mach.Learn.2006,65,247–271.[CrossRef]
340. Kleinberg,E.Onthealgorithmicimplementationofstochasticdiscrimination. IEEETrans. Pat. Anal. Mach. Intell. 2000,22,
473–490.[CrossRef]
341. Breiman,L.BiasVarianceandArcingClassifiers;TechnicalReportTR460;StatisticsDepartment,UniversityofCalifornia:Berkeley,
CA,USA,1996.
342. Friedman,J.;Hall,P.OnBaggingandNonlinearEstimation;TechnicalReport;StatisticsDepartment,StanfordUniversity:Stanford,
CA,USA,2000.
343. Friedman,J.H.Onbias,variance,0/1–loss,andthecurse-of-dimensionality.DataMin.Knowl.Discov.1997,1,55–77.[CrossRef]
344. Domingos, P. A unified bias-variance decomposition for zero-one and squared loss. In Proceedings of the 17th National
ConferenceonArtificialIntelligence,Austin,TX,USA,30July–3August2000;pp.564–569.
345. Valentini,G.Anexperimentalbias-varianceanalysisofSVMensemblesbasedonresamplingtechniques.IEEETrans.Syst.Man
Cybern.B2005,35,1252–1271.[CrossRef]
346. Hastie,T.;Tibshirani,R.;Friedman,J.TheElementsofStatisticalLearning:DataMining,Inference,andPrediction,2nded.;Springer:
NewYork,NY,USA,2009.
347. Mentch,L.;Zhou,S.Randomizationasregularization: Adegreesoffreedomexplanationforrandomforestsuccess. J.Mach.
Learn.Res.2020,21,1–36.
348. Olson,M.A.;Wyner,A.J.Makingsenseofrandomforestprobabilities:Akernelperspective.arXiv2018,arXiv:1812.05792.
349. Welbl,J.Castingrandomforestsasartificialneuralnetworks(andprofitingfromit).InProceedingsoftheGermanConferenceon
PatternRecognition(GCPR),Munster,Germany,3–5September2014;pp.765–771.
350. Biau,G.;Scornet,E.;Welbl,J.Neuralrandomforests.SankhyaA2016,78,140–158.[CrossRef]
351. Coleman,T.;Peng,W.;Mentch,L.Scalableandefficienthypothesistestingwithrandomforests.J.Mach.Learn.Res.2022,23,1–35.
352. Garipov,T.;Izmailov,P.;Podoprikhin,D.;Vetrov,D.;Wilson,A.G.Losssurfaces,modeconnectivity,andfastensemblingofDNNs.
InProceedingsoftheAdvancesinNeuralInformationProcessingSystems(NeurIPS),Montreal,QC,Canada,2–8December2018;
pp.876–885.
353. Izmailov, P.; Podoprikhin, D.; Garipov, T.; Vetrov, D.; Wilson, A.G. Averaging weights leads to wider optima and better
generalization.InProceedingsofthe34thConferenceonUncertaintyinArtificialIntelligence2018(UAI),Corvallis,OR,USA,
1–4August2018;pp.1–9.
354. Maddox,W.;Garipov,T.;Izmailov,P.;Vetrov,D.;Wilson,A.G.ASimplebaselineforBayesianuncertaintyindeeplearning.In
ProceedingsoftheAdvancesinNeuralInformationProcessingSystems(NeurIPS),Montreal,QC,Canada,8–14December2019;
pp.102–111.
355. Wang,A.;Wan,G.;Cheng,Z.;Li,S.Anincrementalextremelyrandomforestclassifierforonlinelearningandtracking. In
Proceedingsofthe16thIEEEInternationalConferenceImageProcessing(ICIP),Cairo,Egypt,7–11November2009;pp.1449–1452.
356. Gomes,H.M.;Bifet,A.;Read,J.;Barddal,J.P.;Enembreck,F.;Pfharinger,B.;Holmes,G.;Abdessalem,T.Adaptiverandomforests
forevolvingdatastreamclassification.Mach.Learn.2017,106,1469–1495.[CrossRef]

Mathematics2025,13,587 49of49
357. Gomes,H.M.;Barddal,J.P.;Ferreira,L.E.B.;Bifet,A.Adaptiverandomforestsfordatastreamregression.InProceedingsofthe
EuropeanSymposiumonArtificialNeuralNetworks,ComputationalIntelligenceandMachineLearning(ESANN),Bruges,
Belgium,25–27April2018;pp.267–272.
358. Luong, A.V.; Nguyen, T.T.; Liew, A.W.-C. Streaming active deep forest for evolving data stream classification. arXiv 2020,
arXiv:2002.11816.
359. Korycki,L.;Krawczyk,B.Adaptivedeepforestforonlinelearningfromdriftingdatastreams.arXiv2020,arXiv:2010.07340.
360. Gomes,H.M.;Read,J.;Bifet,A.;Durrant,R.J.Learningfromevolvingdatastreamsthroughensemblesofrandompatches.Knowl.
Inf.Syst.2021,63,1–29.[CrossRef]
361. Gomes, H.M.; Montiel, J.; Mastelini, S.M.; Pfahringer, B.; Bifet, A. On ensemble techniques for data stream regression. In
ProceedingsoftheInternationalJointConferenceonNeuralNetworks(IJCNN),Glasgow,UK,19–24July2020;pp.1–8.
362. Mastelini,S.M.;Nakano,F.K.;Vens,C.;deCarvalho,A.C.P.d.L.F.Onlineextratreesregressor.IEEETrans.NeuralNetw.Learn.Syst.
2023,34,6755–6767.[CrossRef][PubMed]
363. Polikar,R.;Upda,L.;Upda,S.S.;Honavar,V.Learn++:Anincrementallearningalgorithmforsupervisedneuralnetworks.IEEE
Trans.Syst.ManCybern.C2001,31,497–508.[CrossRef]
364. Zhao,Q.;Jiang,Y.;Xu,M.Incrementallearningbyheterogeneousbaggingensemble. InProceedingsofthe6thInternational
ConferenceonAdvancedDataMiningandApplications(ADMA),Chongqing,China,19–21November2010;Volume2,pp.1–12.
365. Zliobaite,I.AdaptiveTrainingSetFormation.Ph.D.Thesis,VilniusUniversity,Vilnius,Lithuania,2010.
366. Elwell,R.;Polikar,R.Incrementallearningofconceptdriftinnonstationaryenvironments.IEEETrans.NeuralNetw.2011,22,
1517–1531.[CrossRef][PubMed]
367. Kumano,S.;Akutsu,T.Comparisonoftherepresentationalpowerofrandomforests,binarydecisiondiagrams,andneural
networks.NeuralComput.2022,34,1019–1044.[CrossRef]
368. Du,K.-L.Severalmisconceptionsandmisusesofdeepneuralnetworksanddeeplearning.InProceedingsofthe2023International
CongressonCommunications,Networking,andInformationSystems(CNIS2023),Guilin,China,25–27March2023;pp.155–171.
369. Yarotsky,D.ErrorboundsforapproximationswithdeepReLUnetworks.NeuralNetw.2017,94,103–114.[CrossRef][PubMed]
370. Baldi,P.;Vershynin,R.Thecapacityoffeedforwardneuralnetworks.NeuralNetw.2019,116,288–311.[CrossRef]
371. Veit,A.;Wilber,M.;Belongie,S.Residualnetworksbehavelikeensemblesofrelativelyshallownetworks.InAdvancesinNeural
InformationProcessingSystems;CurranAssociates,Inc.:RedHook,NY,USA,2016;Volume29,pp.550–558.
372. He,F.;Liu,T.;Tao,D.WhyResNetworks? Residualsgeneralize. IEEETrans. NeuralNetw. Learn. Syst. 2020,31,5349–5362.
[CrossRef][PubMed]
373. Du,K.-L.;Leung,C.-S.;Mow,W.H.;Swamy,M.N.S.Perceptron:Learning,generalization,modelselection,faulttolerance,and
roleinthedeeplearningera.Mathematics2022,10,4730.[CrossRef]
374. Bhattacharyya,S.;Jha,S.;Tharakunnel,K.;Westland,J.C.Dataminingforcreditcardfraud:Acomparativestudy.Decis.Support
Syst.2011,50,602–613.[CrossRef]
375. Santos,M.S.;Soares,J.P.;Abreu,P.H.;Arajo,H.;Santos,J.Cross-validationforimbalanceddatasets:Avoidingoveroptimisticand
overfittingapproaches.IEEEComput.Intell.Mag.2018,13,59–76.[CrossRef]
376. Cruz,J.A.;Wishart,D.S.Applicationsofmachinelearningincancerpredictionandprognosis. CancerInform. 2006,2,59–77.
[CrossRef]
377. Zhang,J.;Zulkernine,M.;Haque,A.Random-forests-basednetworkintrusiondetectionsystems.IEEETrans.Syst.ManCybern.
PartAppl.Rev.2008,38,649–659.[CrossRef]
378. Janai, J.; Guney, F.; Behl, A.; Geiger, A. Computer vision for autonomous vehicles: Problems, datasets and state of the art.
Foundationsandtrends?Comput.Graph.Vis.2020,12,1–308.
379. Yang,Y.;Lv,H.;Chen,N.ASurveyonensemblelearningundertheeraofdeeplearning.Artif.Intell.Rev.2023,56,5545–5589.
[CrossRef]
380. Cao, Y.; Geddes, T.A.; Yang, J.Y.H.; Yang, P.Ensembledeeplearninginbioinformatics. Nat. Mach. Intell. 2020, 2, 500–508.
[CrossRef]
381. Sagi,O.;Rokach,L.Ensemblelearning:Asurvey.WileyInterdiscip.Rev.DataMin.Knowl.Discov.2018,8,e1249.[CrossRef]
382. Dong,X.;Yu,Z.;Cao,W.;Shi,Y.;Ma,Q.Asurveyonensemblelearning.Front.Comput.Sci.2020,14,241–258.[CrossRef]
383. Gomes,H.M.;Barddal,J.P.;Enembreck,F.;Bifet,A.Asurveyonensemblelearningfordatastreamclassification.ACMComput.
Surv.2017,50,23:1–23:36.[CrossRef]
384. Gao,J.;Li,P.;Chen,Z.;Zhang,J.Asurveyondeeplearningformultimodaldatafusion. NeuralComput. 2020,32,829–864.
[CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.