| Test-Time |           | Adaptation |        | for | Non-stationary |     |              |     | Time Series: |
| --------- | --------- | ---------- | ------ | --- | -------------- | --- | ------------ | --- | ------------ |
| From      | Synthetic |            | Regime |     | Shifts         |     | to Financial |     | Markets      |
YuruiWu,QingyingDeng,WonouChung,MairuiLi
DepartmentofStatistics&OperationsResearch,UNCChapelHill
ChapelHill,NC,27599
6202 naJ 02  ]TS.nif-q[  1v37000.2062:viXra {yuruiwu,doradeng,wchung,mairuili}@email.unc.edu
Abstract
Timeseriesencounteredinpracticearerarelystationary.Whenthedatadistribution
|     | changes,aforecastingmodeltrainedonpastobservationscanloseaccuracy.  |                   |           |     |            |                             |           |     | We           |
| --- | ------------------------------------------------------------------- | ----------------- | --------- | --- | ---------- | --------------------------- | --------- | --- | ------------ |
|     | study                                                               | a small-footprint | test-time |     | adaptation | (TTA)                       | framework | for | causal time- |
|     | seriesforecastinganddirectionclassification.                        |                   |           |     |            | Thebackboneisfrozen,andonly |           |     |              |
|     | normalizationaffineparametersareupdatedusingrecentunlabeledwindows. |                   |           |     |            |                             |           |     | For          |
classificationweminimizeentropyandenforcetemporalconsistency;forregression
weminimizepredictionvarianceacrossweaktime-preservingaugmentationsand
optionallydistillfromanEMAteacher.Aquadraticdriftpenaltyandanuncertainty-
|     | triggeredfallbackkeepupdatesstable. |     |     |     | Weevaluatethisframeworkintwostages: |     |     |     |     |
| --- | ----------------------------------- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- |
syntheticregimeshiftsonETTbenchmarks,anddailyequityandFXseries(SPY,
|     | QQQ, | EUR/USD) | across | pandemic, | high-inflation, |     | and recovery |     | regimes. On |
| --- | ---- | -------- | ------ | --------- | --------------- | --- | ------------ | --- | ----------- |
syntheticgradualdrift,normalization-basedTTAimprovesforecastingerror,while
|     | in financial                                                       | markets  | a simple   | batch-normalization |     |            | statistics | update | is a robust |
| --- | ------------------------------------------------------------------ | -------- | ---------- | ------------------- | --- | ---------- | ---------- | ------ | ----------- |
|     | default                                                            | and more | aggressive | norm-only           |     | adaptation | can even   | hurt.  | Our results |
|     | providepracticalguidancefordeployingTTAonnon-stationarytimeseries. |          |            |                     |     |            |            |        | The         |
sourcecodeofthisstudyisavailableatthisGoogleDrive.
1 Introduction
Real-world time series, such as financial prices or electricity loads, evolve over time. Structural
breaks,policychanges,andmacroeconomicshockscanshiftboththelevelandthevolatilityofthe
process. DuringtheCOVID-19crisisandthesubsequenthigh-inflationperiod,marketdynamics
changedrapidly,andmodelstrainedonpre-crisisdatabecamemiscalibrated. Oncethedeployment
distributiondepartsfromthetrainingdistribution,minimizingtraininglossisnolongersufficientto
guaranteetestperformance.
Test-timeadaptation(TTA)addressesthisissuebyupdatingpartofthemodelusingunlabeledtest
inputs. Fortimeseries,apracticalTTAschememustbecausal(nofuturedata),parameterefficient,
androbusttonoisyupdates. Inthisworkwefreezethebackboneandadaptonlyasmallparameterset
atdeployment. Whendaytarrives,wecollectthemostrecentwindows,applyweaktime-preserving
augmentations, and take a few gradient steps on unsupervised objectives. For classification we
combineentropyminimizationwithtemporalconsistency;forregressionweminimizeaugmentation
varianceandoptionallydistillfromanexponential-moving-averageteacher. Wecontrolthesizeof
dailyparameterchangesandfallbacktoalightweightbatch-normalizationstatisticsupdatewhenan
uncertaintyproxyishigh.
Ourgoalisnottoproposeanewheavyarchitecture,buttounderstandwhensmall-footprintTTA
helpsorhurtsonnon-stationarysequences. Wemakethreecontributions. First,weunifyseveralTTA
choices—noadaptation,batch-normalizationstatisticsrefresh,andnorm-onlyadaptation—under
onecausalframework. Second,weevaluatethisframeworkintwostages: syntheticshiftsonETT
Preprint.Underreview.

benchmarks, and real markets (SPY, QQQ, EUR/USD) split into pandemic, high-inflation, and
recovery regimes. Third, we connect the results with econometric tools (Diebold–Mariano tests
and Newey–West adjustments) and summarize practical recommendations for deploying TTA in
streamingforecastingsystems.
2 LiteratureReview
2.1 Test-timeadaptationunderdistributionshift
TTA minimizes an unsupervised objective at inference using the current test inputs, while most
parametersarefrozen. Acentralresultisthattuningonlynormalizationaffineparameters(γ,β)by
entropyminimizationcanyieldlargegainsundercovariateshift[1].Thisworksbecausenormalization
re-centers and re-scales hidden activations to match the present input distribution, and the affine
degreesoffreedomareenoughtocorrectmanyfirst/second-momentchanges. Instreamingscenarios,
adaptationcanaccumulateerroriftheprocedureisaggressiveorifpseudo-targetsareunstable. Prior
work proposes stabilizers such as exponential-moving-average teachers and conservative update
schedules[2,3]. WefollowthislinebyusinganEMAteacherforself-distillationinregressionand
byaddingaquadraticdriftpenaltythatdiscourageslargeinter-dayparametermotion.
Refreshing batch-normalization statistics at test time (recomputing means and variances without
gradients)alreadyimprovesrobustnesstosmall-batchandcovariateshifts[4,5]. Thismotivates
our fallback: when an uncertainty proxy is high, we refresh statistics and skip gradient updates.
Recentanalysesaddexplanatorydepth;forexample,KimandLeeetal.[21]showthatTTAcan
increaselinearityinintermediatelayers,whichyieldsmorestableextrapolationonshiftedinputs. For
forecasting,test-timelearningcanbeformulatedwithvarianceandconsistencyobjectivesthatdonot
requirelabels[22]. Adaptationinnon-stationaryenvironmentscanalsobeframedasrepresentation
alignmentthatmaintainsproximitybetweencurrentandreferencefeatures[20]. Ourconsistencyand
varianceobjectives,togetherwithEMA-teacheranddriftcontrol,areconcreterealizationsofthese
ideasfortimeseries.
2.2 Normalizationandarchitecturesfornon-stationarysequences
Non-stationarityoftenmanifestsaslevel/scaledriftandtime-varyingseasonality,sonormalization
layersareaprimarytool. Reversibleinstancenormalization(RevIN)standardizeseachsequence
andthenreversesthetransformbeforeoutput;itreducestrain–testmismatchwhilepreservingthe
forecastingtarget[6]. Adaptivenormalizationlearnsgatesthatrespondtodistributionalchanges[7].
Frequency-awarenormalizationemphasizesmulti-scaleperiodicstructureandmodulatesfeatures
accordingly [8]. These methods act within the backbone. Our TTA instead acts on top of such
defenses,allowingsmallaffinecorrectionsthatfollowthedeploymentstream,sothetwoapproaches
arecomplementary. Onthearchitectureside,theNon-StationaryTransformerincorporatesevolving
statisticsdirectlyintoattentionandresidualpaths[9]. Forourhostsweadoptlightyetcompetitive
models—multi-scaleresidualTemporalConvolutionalNetworks(TCN)[10]andcompactTransform-
ers—aswellasPatchTSTandTimesNetasreferences[11,12]. Weselectsmallwidths(64–128)and
fewlayers(2–4)toensurethattest-timeupdatestouchonlythousandsofparameters,keepinglatency
negligiblewhilepreservingaccuracy.
2.3 Regime-wiseevaluationandeconometricsignificance
Statistical performance should be interpreted by regime. Markov-switching models explain how
coefficientsandvolatilitychangeacrossstates[14],andsurveyevidencesupportsregime-dependent
predictabilityinfinancialmarkets[15].Wethereforereportrollingcurvesandregime-wisesummaries.
TocompareforecastaccuracyweusetheDiebold–MarianotestwithHACvarianceestimation[16,17].
Whenweevaluatemanyvariants,standardmultiple-comparisoncorrectionsmaybeanti-conservative;
RealityCheckandSPAaddressdata-snoopingbybootstrappingthemaximumperformancestatistic
acrossmodels[18,19]. Oursignificancereportingisalignedwiththesetools.
2

3 ProblemSetup
Let{x }T ,x ∈Rdbeamultivariateseries. WeformaninputwindowX =[x ,...,x ]∈
| t t=1 | t   |     |     |     |     |     |     |     | t t−L+1 | t   |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
RL×dandstudytwotasks.
1. Classification: predictthedirectionfordayt+1;lety t+1 ∈{0,1}denotedownorup,and
[0,1]2
let pˆ(X t ) ∈ be the predicted probability. We track accuracy, F1, AUC, direction
accuracy,andexpectedcalibrationerror(ECE),anddrawreliabilitydiagrams.
2. Regression: predict next-day log-return r t+1 = logp t+1 −logp t or H-day cumulative
| log-returnr |     |         | = (cid:80)H | r       | ;wereportMAE,RMSE,andR2. |     |     |     |     |     |
| ----------- | --- | ------- | ----------- | ------- | ------------------------ | --- | --- | --- | --- | --- |
|             |     | t+1:t+H |             | h=1 t+h |                          |     |     |     |     |     |
Thedeploymentstream{P }isnon-stationaryrelativetotrainingP ,withshiftsincludinglocation-
|     |     | t   |     |     |     |     |     | train |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
scaledrift,noiseinflation,andstructuralchanges. SyntheticgeneratorsinAppendixBimplement
these. FordailyequityandFXseriesweuseaunifiedsplit: train2000–2016,validation2017–2019,
test2020–2025. Allscalersarefitontrainingonly,andweavoidexogenousvariablestoprevent
leakage. ETTbenchmarksfollowtheirstandardsplits.
4 Method
Wetrainabackbonef onthetrainingsplitwithsupervisedlosses. Attesttimeweadaptasmall
θ
parametersetonunlabeledwindowsfromthecurrentstream;thebackboneisfrozen.
4.1 Backbonesandupdateableunits
We consider a multi-scale residual TCN and a compact Transformer (2–4 layers, width 64–128).
| GRU/LSTMserveasreferences. |                                    |     |     | Attesttime,wecomparethefollowingoptions: |     |     |     |     |     |     |
| -------------------------- | ---------------------------------- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
| • no_tta:                  | notest-timeadaptation,frozenmodel. |     |     |                                          |     |     |     |     |     |     |
• bn_stats: refreshbatch-normalization(BN)meansandvariancesusingthecurrentbatch,no
gradients.
| • norm_only: |     | updateonlynormalizationaffineparameters(γ,β). |     |     |     |     |     |     |     |     |
| ------------ | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
4.2 Unsupervisedobjectives
LetBbethebatchofrecentunlabeledwindows. Forclassificationweuseentropyandconsistency:
|     |     |     |      | 1   | (cid:88) (cid:16) | (cid:88) |          |     | (cid:17) |     |
| --- | --- | --- | ---- | --- | ----------------- | -------- | -------- | --- | -------- | --- |
|     |     | L   | (θ)= |     | −                 | pˆ       | (X)logpˆ | (X) | ,        | (1) |
|     |     |     | ent  |     |                   |          | c        | c   |          |     |
|B|
|     |     |     |      |     | X∈B                            | c   |     |           |     |     |
| --- | --- | --- | ---- | --- | ------------------------------ | --- | --- | --------- | --- | --- |
|     |     |     |      | 1   | (cid:88) (cid:13)              |     |     | (cid:13)2 |     |     |
|     |     | L   | (θ)= |     | (cid:13)pˆ(X)−pˆ(T(X))(cid:13) |     |     | ,         |     | (2) |
cons
|     |     |     |     | |B| |     |     |     | 2   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
X∈B
whereT isaweaktime-preservingtransform(Section4.4). Forregressionweusevarianceminimiza-
tionandEMA-teacherself-distillation:
1
|     |     |      |     | (cid:88) | (cid:0) | (X))}K | (cid:1) |     |     |     |
| --- | --- | ---- | --- | -------- | ------- | ------ | ------- | --- | --- | --- |
|     | L   | (θ)= |     | Var      | {yˆ(T   |        | ,       |     |     | (3) |
|     | var |      | |B| |          | k       |        | k=1     |     |     |     |
X∈B
|     |     | (θ,θ˜)= | 1    | (cid:88) (cid:13)   |     | (cid:13) 2 | θ˜←ρθ˜+(1−ρ)θ. |     |     |     |
| --- | --- | ------- | ---- | ------------------- | --- | ---------- | -------------- | --- | --- | --- |
|     | L   |         |      | (cid:13)yˆ(X)−y˜(X) |     | (cid:13)   | ,              |     |     | (4) |
|     | sd  |         | |B | |                     |     | 2          |                |     |     |     |
X∈B
Driftcontrol: wepenalizeinter-daychangeinthesmallparameterset,
|     |     |     |       |                 |     | (cid:13) (cid:13)θ(t)−θ(t−1)(cid:13) |     | 2          |     |     |
| --- | --- | --- | ----- | --------------- | --- | ------------------------------------ | --- | ---------- | --- | --- |
|     |     |     | L     | (θ(t),θ(t−1))=γ |     |                                      |     | .          |     | (5) |
|     |     |     | drift |                 |     |                                      |     | (cid:13) 2 |     |     |
Totalobjective: forclassification,
|     |     |     | L(θ)=αL |     | +βL |      | +L    | ,   |     | (6) |
| --- | --- | --- | ------- | --- | --- | ---- | ----- | --- | --- | --- |
|     |     |     |         |     | ent | cons | drift |     |     |     |
andforregression,
|     |     |     | L(θ)=αL |     | var +βL | sd  | +L drift | .   |     | (7) |
| --- | --- | --- | ------- | --- | ------- | --- | -------- | --- | --- | --- |
AppendixAprovidesderivationsandgradientsfornorm-onlyparameters,includingproximalinter-
pretationsofthedriftpenaltyandthevariance-reductionroleoftheEMAteacher.
3

4.3 Uncertainty-triggeredfallback
We compute an uncertainty proxy on B. For classification, we use mean entropy
1 (cid:80)
u t = H(pˆ(X)). For regression, we use mean augmentation variance u t =
|     |     | |B| | X   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
1 (cid:80)
Var({yˆ(T k (X))} k ). We set τ as the 80th percentile of u t on validation; 70% and 90%
|B| X
|     | areablated. | Ifu | >τ,werefreshBNstatisticsandskipgradientupdates. |     |     |     |     |
| --- | ----------- | --- | ----------------------------------------------- | --- | --- | --- | --- |
t
4.4 Causality-preservingaugmentations
Weuseweaktransformsthatkeeptimeorderandavoidleakage:amplitudescaling(1±5%),Gaussian
jitterwithstandarddeviation0.01timesthetrainingstandarddeviation,timejitterby±1stepwithin
thewindow,andtimecutoutmaskingupto5steps.
4.5 Dailytest-timeadaptationalgorithm
DefaulthyperparametersareW=64,S=5,learningrate10−4,andα=β =10−3.
=1,γ
Algorithm1:CausalTest-TimeAdaptationforDayt
Input: Frozenbackbonef θ ;updatableparametersetϕ⊂θ(norm-onlyBNaffineparameters);
WindowlengthL;contextsizeW;stepsS;learningrateη;uncertaintythresholdτ;
|     | Losstype: | classification((6))orregression((7));transforms{T |     |     |     |     | }.  |
| --- | --------- | ------------------------------------------------- | --- | --- | --- | --- | --- |
k
|     | Output:              | Predictionyˆ |     | (orpˆ                            | )forthenextday. |     |     |
| --- | -------------------- | ------------ | --- | -------------------------------- | --------------- | --- | --- |
|     |                      |              | t+1 | t+1                              |                 |     |     |
|     | BuildunlabeledbatchB |              |     | ←{X                              | ,...,X          | }.  |     |
| 1   |                      |              |     | t−W+1                            |                 | t   |     |
| 2   | Computeuncertaintyu  |              | t   | (entropyoraugmentationvariance). |                 |     |     |
| 3   | ifu >τ               | then         |     |                                  |                 |     |     |
t
| 4   | RefreshBNrunningstatisticsonB;returnyˆ |     |     |     |     | ←f (X | ).  |
| --- | -------------------------------------- | --- | --- | --- | --- | ----- | --- |
|     |                                        |     |     |     |     | t+1 θ | t   |
| 5   | fors=1toS                              |     | do  |     |     |       |     |
ifclassificationthen
6
|     | SampleaweaktransformT;computeL |     |     |              |     | andL     | .   |
| --- | ------------------------------ | --- | --- | ------------ | --- | -------- | --- |
| 7   |                                |     |     |              |     | ent cons |     |
| 8   | L←αL                           |     | +βL | +γ∥ϕ−ϕprev∥2 |     | .        |     |
|     |                                |     | ent | cons         |     | 2        |     |
else
9
regression
10
| 11  | SampleK          | transforms{T |                   | k };computeL |     | var andoptionallyL | sd . |
| --- | ---------------- | ------------ | ----------------- | ------------ | --- | ------------------ | ---- |
|     | L←αL             |              | +βL               | +γ∥ϕ−ϕprev∥2 |     | .                  |      |
| 12  |                  | var          | sd                |              | 2   |                    |      |
|     | Updateonlyϕ←ϕ−η∇ |              |                   | L(SGD/Adam). |     |                    |      |
| 13  |                  |              |                   | ϕ            |     |                    |      |
|     | returnyˆ         | ←f           | (X )withupdatedϕ. |              |     |                    |      |
| 14  |                  | t+1          | θ t               |              |     |                    |      |
4.6 Ablationsandsensitivity
Only thousands of parameters are updated, so extra latency per test day is small on a single T4
GPU. For the hyperparameters, we sweep W ∈ {32,64,96}, S ∈ {1,3,5}, and learning rate
in {5 × 10−5,10−4,2 × 10−4}. We compare entropy-only vs. consistency-only vs. combined
for classification, and variance-only vs. variance plus EMA teacher for regression. We examine
|     | augmentationsets: |     | scalingonly;scalingplusjitter;scalingplusjitterandcutout. |     |     |     |     |
| --- | ----------------- | --- | --------------------------------------------------------- | --- | --- | --- | --- |
5 DataandShiftConstruction
StageI:ETTwithsyntheticshifts. WeuseETTh1/ETTh2(hourly)andETTm1/ETTm2(15-min).
Theseseriesincludepowertransformerloadsandtemperatureswithclearseasonality. Wegenerate
threesyntheticshifts: (i)gradualmean/variancedrift,(ii)localnoiseinflation,and(iii)structural
|     | switchesinperiodiccomponents. |     |     |     | FormaldefinitionsandgridsareinAppendixB. |     |     |
| --- | ----------------------------- | --- | --- | --- | ---------------------------------------- | --- | --- |
4

|     |     | Figure1: | RegimediagnosticsforSPYvolatilityandreturns. |     |     |     |
| --- | --- | -------- | -------------------------------------------- | --- | --- | --- |
Stage II: equity and FX markets. We use daily SPY and QQQ index ETFs, plus EUR/USD
exchangerates. FeaturesarebuiltfromOHLCVonlyandstandardizedusingtrainingstatistics:
|        | r =log(C | )−log(C | ),  |     |     |     |
| ------ | -------- | ------- | --- | --- | --- | --- |
|        | t        | t       | t−1 |     |     |     |
| MOM(N) | =log(C   | )−log(C | ),  |     |     |     |
|        | t        | t       | t−N |     |     |     |
N
(cid:88)
| REV(N) | =−  | r , |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- |
|        | t   | t−i |     |     |     |     |
i=1
|     |        | (cid:0) |                 |               | (cid:1)  |     |
| --- | ------ | ------- | --------------- | ------------- | -------- | --- |
| ATR | t =EMA | max{H   | t −L t ,|H t −C | t−1 |,|L t −C | t−1 |} , |     |
1
|     | σ2       |        | ))2, σ2 | 1(log(H | ))2−(2ln2−1)(log(C | ))2.   |
| --- | -------- | ------ | ------- | ------- | ------------------ | ------ |
|     | =        | (log(H | t /L t  | =       | t /L t             | t /O t |
|     | P,t 4ln2 |        | GK,t    | 2       |                    |        |
Wesplittestingintothreeregimes: (1)pandemic(2020),(2)high-inflation(2021–2023),(3)recovery
| (2024–2025). | Figure1showsbasicregimediagnosticsforSPY. |     |     |     |     |     |
| ------------ | ----------------------------------------- | --- | --- | --- | --- | --- |
6 ExperimentalProtocol
Weevaluateourtest-timeadaptationframeworkonthreefinancialdirectionclassificationtasks(SPY,
QQQ,andEUR/USD)andonelong-horizontime-seriesforecastingtask(ETTh1). Alldatasetsare
preprocessedintofixed-lengthslidingwindowswithinputlengthL=96,andETTh1isevaluated
withforecasthorizonH =96. Dataaresplitchronologicallyintotraining,validation,andtestsetsto
ensurestrictout-of-sampleevaluation. AllmodelsuseaTemporalConvolutionalNetwork(TCN)
withthreeresidualblocks,hiddendimension64,andkernelsize3,followedbyalinearheadfor
eitherclassificationorregression.
ModelsaretrainedusingAdamWwithlearningrate10−4,batchsize512,andearlystoppingbased
on validation AUC (classification) or validation MSE (regression). At deployment, three main
modesarecompared: noadaptation(no_tta),batch-normalizationstatisticsrefresh(bn_stats),and
norm-onlyparameteradaptation(norm_only). Test-timeadaptationistriggeredusinganuncertainty
thresholdτ estimatedasthe0.8quantileofvalidationuncertainty,computedviapredictionentropy
forclassificationandvarianceofstochasticaugmentationsforregression. Whentriggered,norm-only
parametersareupdatedusingasmallnumberofunsupervisedgradientstepswithentropy/consistency
lossforclassificationorvariance/distillationlossforregression. Evaluationisperformedstrictlyon
thetestsetusingaccuracy,F1,AUC,andECEforclassification;MAE,RMSE,andR2forregression;
alongwithrollingperformance,reliabilitydiagrams,Diebold–Marianostatisticaltests,andasimple
directionaltradingbacktestwithNewey–Westadjustedstatistics.
5

Table1: RepresentativeETTh1resultsundersyntheticregimeshifts. Eachentrycorrespondstoone
representativeconfigurationinthespecifiedregime.
Method Shift MAE RMSE R2
no_tta Gradual 0.22 0.28 -0.31
norm_only Noise 0.29 0.35 -0.02
bn_stats Structural 1.26 1.62 -20.80
Figure2: RollingforecastmetricsonETTh1undergradualdrift.
7 Results
7.1 StageI:syntheticshiftsonETT
WefirststudyhowdifferentTTAchoicesbehaveundercontrolledshiftsonETTh1. Table1reports
meanabsoluteerror(MAE),rootmeansquarederror(RMSE),andR2foronerepresentativeconfigu-
rationineachsyntheticregime: gradualdrift,localnoiseinflation,andstructuralswitches. Negative
R2 valuesindicatethatthemodelperformsworsethanasimpletraining-baselinebenchmarkunder
thecorrespondingshift.
Norm-onlyadaptationismosteffectiveundergradualmean/variancedrift,whereupdatingnormaliza-
tionaffineparameterscantrackslowchangesinscaleandlevel. Underlocalnoiseinflation,variance
minimizationacrossweakaugmentationsstabilizesregressionoutputsandreducestheimpactof
noisebursts. Structuralswitchesarethehardestcase: evenwithbn_stats,errorsremainlargeandR2
isstronglynegative.
Figure2showsrollingforecastmetricsonETTh1undergradualdrift. Comparedwiththefrozen
baseline,norm-onlyTTAreduceserrorsinthelaterpartofthehorizon,wherethesyntheticdrift
accumulates. Thissupportstheviewthatnormalization-basedupdatesarewellsuitedtosmooth
low-ordermomentshifts.
7.2 StageII:equityandFXmarkets
WenextevaluatedirectionclassificationonSPY,QQQ,andEUR/USDwiththesameTTArecipe.
Table2reportscross-marketdirectionaccuracyforallthreemethods. Thebaselineaccuracyisclose
to0.5onallseries,reflectingthedifficultyofdailydirectionprediction.
Thesenumberscomefromarunfocusedondirectionalaccuracy;absolutevaluesdifferfromother
experiments,butpatternsareconsistent. Thereisnosinglewinner: differentmarketsandregimes
preferdifferentTTAvariants. OnSPY,norm_onlyachievesthebestdirectionalaccuracy,slightly
aheadofno_ttaandbn_stats. OnQQQ,bn_statsprovidesthelargestgain,whilenorm_onlycanhurt
performance. OnEUR/USD,bothTTAmethodsareroughlyonparwithorslightlybetterthanthe
frozenbaseline.
Figure 3 plots rolling direction accuracy and RMSE for SPY, QQQ, and EUR/USD with regime
shading. ForSPY,improvementsfromTTAareconcentratedinthepandemicandearlyrecovery
periods, when distributional change is strong. For QQQ, batch-normalization statistics updates
6

Table2: Directionalaccuracyontestsets(2020–2025)forequityandFXmarkets.
| Method    | SPY QQQ     | EURUSD | Avg.rank |
| --------- | ----------- | ------ | -------- |
| no_tta    | 0.504 0.503 | 0.516  | 2.33     |
| bn_stats  | 0.498 0.525 | 0.520  | 1.66     |
| norm_only | 0.512 0.463 | 0.516  | 2.00     |
Figure3: RollingmetricsforSPY,QQQ,andEUR/USDwithregimeshading.
(bn_stats)areparticularlyeffective,whilenorm_onlycanoverfitlocalnoiseanddegradeaccuracy.
ForEUR/USD,bn_statsyieldsthemoststablegains,andnorm_onlybehavessimilarlytothefrozen
baseline.
7.3 Statisticaltestsandbacktests
Toassesswhetherobserveddifferencesarestatisticallymeaningful,werunDiebold–Marianotestson
dailyforecastlosses. Table3reportsDMstatisticsandp-valuesforpairwisecomparisonsbetween
bn_stats,norm_only,andno_tta. NegativeDMvaluesindicatethatthefirstmethodoutperformsthe
secondunderourlossconvention. OnSPYandQQQ,bn_statsissignificantlybetterthanno_ttaat
the5%level,whilenorm_onlyissignificantlyworsethanno_tta. OnEUR/USD,bn_statsisalso
significantlybetterthanno_tta,andnorm_onlyisindistinguishablefromthebaseline.
7

|            | Table3: | Diebold–Marianotestscomparingforecastlosses. |        |         |     |       |
| ---------- | ------- | -------------------------------------------- | ------ | ------- | --- | ----- |
| Comparison |         | Dataset                                      | DMStat | p-value |     | Notes |
bn_statsvsno_tta SPY -2.781 0.0054 bn_statssignificantlybetter
| norm_onlyvsno_tta |     | SPY | 6.810 | 0.0000 | no_ttasignificantlybetter |     |
| ----------------- | --- | --- | ----- | ------ | ------------------------- | --- |
bn_statsvsno_tta QQQ -2.290 0.0220 bn_statssignificantlybetter
| norm_onlyvsno_tta |     | QQQ | 8.936 | 0.0000 | no_ttasignificantlybetter |     |
| ----------------- | --- | --- | ----- | ------ | ------------------------- | --- |
bn_statsvsno_tta EURUSD 4.350 0.0000 bn_statssignificantlybetter
| norm_onlyvsno_tta |                                                         | EURUSD     | -0.112 | 0.9109         | nosignificantdifference |     |
| ----------------- | ------------------------------------------------------- | ---------- | ------ | -------------- | ----------------------- | --- |
|                   | Table4: SPYbacktestperformancewithNewey–Westadjustment. |            |        |                |                         |     |
|                   | Strategy                                                | Ann.return |        | Ann.volatility | Sharpe(NWt)             |     |
|                   | No-TTA                                                  | 3.321      |        | 4.621          | 1.746                   |     |
|                   | BN-Stats                                                | 7.933      |        | 9.582          | 1.930                   |     |
|                   | Norm-Only                                               | 2.029      |        | 3.460          | 1.544                   |     |
Finally, we connect predictive accuracy with simple economic metrics. Tables 4 and 5 report
annualized return, annualized volatility, and Sharpe ratio for a basic directional strategy on SPY
andQQQ,togetherwithNewey–Westadjustedt-statistics. Onbothassets, bn_statsachievesthe
highest Sharpe ratio, while norm_only underperforms the frozen baseline. These backtests are
purelyillustrative,buttheyshowthatthestatisticalgainsfrombn_statstranslateintomoreattractive
risk-adjustedreturns,whereasnaivenorm-onlyupdatescanbeharmful.
8 DiscussionandConclusion
Normalization-basedTTAismosteffectivewhenshiftsmainlychangelow-ordermoments. Inthe
syntheticETTh1experimentswithgradualdrift,updatingnormalizationaffineparameterstracks
thechangingscaleandreducesforecasterror. Localnoiseinflationispartlyhandledbyvariance-
basedobjectives,butstructuralswitchesinperiodiccomponentsstillleadtolargeerrorsevenafter
adaptation. Thissuggeststhatnorm-onlyupdatesarewellsuitedtosmoothcovariatedrift,butthey
donotfullysolvesharporregime-changingdynamics.
Incontrast,theequityandFXseries(SPY,QQQ,EUR/USD)arenoisy,heavy-tailed,andaffectedby
jumpsandmicrostructurenoise. Hereasimplerefreshofbatch-normalizationstatisticsisasafeand
effectivedefault: bn_statsachieveshigherdirectionaccuracyandSharperatiosonSPYandQQQ,
andtheDiebold–Marianotestsshowstatisticallysignificantimprovementsoverthefrozenbaseline.
Aggressivenorm-onlyadaptation,evenwithdriftcontrol,canoverfitshortwindows,performworse
thanno_tta,andreduceeconomicperformanceinthebacktests.
Our results also highlight the importance of uncertainty control. The fallback rule, which skips
gradient-basedadaptationondayswithhighentropyorlargeaugmentationvariance,mitigatesmany
failure cases of norm-only updates and limits the frequency of harmful steps. At the same time,
thechoiceofhyperparameters(W,S,η,τ)andthestabilityofthebackboneremainimportant,and
differentassetsmayfavordifferentadaptationregimes. Syntheticshiftgeneratorsarenecessarily
stylizedandcannotcoverallrealdynamics,somorerealisticbenchmarksandstresstestsareanatural
directionforfuturework.
Overall,thisstudyprovidesanempiricalpictureofwhensmall-footprintTTAhelpsandwhenithurts
onnon-stationarytimeseries. Forpractitioners,ourmainrecommendationistostartfrombn_statsas
adefault,addnorm-onlyupdatesonlywhenvalidationanduncertaintydiagnosticssupportthem,and
alwaysevaluatewithregime-wisemetricsandrobuststatisticaltests. Wehopethesefindingswill
helpbothpractitionersandresearchersdesignsaferandmoreeffectivetest-timeadaptationpipelines
forreal-worldtimeseries.
8

|     | Table5: QQQbacktestperformancewithNewey–Westadjustment. |            |                |             |
| --- | ------------------------------------------------------- | ---------- | -------------- | ----------- |
|     | Strategy                                                | Ann.return | Ann.volatility | Sharpe(NWt) |
|     | No-TTA                                                  | 10.884     | 7.689          | 3.205       |
|     | BN-Stats                                                | 20.293     | 11.974         | 4.080       |
|     | Norm-Only                                               | 3.136      | 5.204          | 1.349       |
References
[1] D.Wang,E.Shelhamer,S.Liu,B.Olshausen,andT.Darrell. Tent:Fullytest-timeadaptationbyentropy
| minimization.                  | InICLR,2021. |                                     |     |              |
| ------------------------------ | ------------ | ----------------------------------- | --- | ------------ |
| [2] J.Wang,Y.Liu,W.Zhang,etal. |              | Continualtest-timedomainadaptation. |     | InCVPR,2022. |
[3] L.Yuan,S.Wang,etal. Robusttest-timeadaptationindynamicscenarios. InCVPR,2023.
| [4] Z.Yang,Z.Li,etal. | Test-timebatchnormalization. |     | arXiv:2205.10210,2022. |     |
| --------------------- | ---------------------------- | --- | ---------------------- | --- |
[5] S.Schneider,A.Minderer,etal. Improvingrobustnessagainstcommoncorruptionsbycovariate-shift
| adaptationattesttime. | InNeurIPS,2020. |     |     |     |
| --------------------- | --------------- | --- | --- | --- |
[6] T. Kim, H. Oh, et al. Reversible instance normalization for accurate time-series forecasting against
| distributionshift. | InICLR,2022. |     |     |     |
| ------------------ | ------------ | --- | --- | --- |
[7] W.Liu,S.Zhang,etal. Adaptivenormalizationfornon-stationarytimeseriesforecasting. InNeurIPS,
2023.
[8] J.Ye,Z.Zhang,etal. Frequency-adaptivenormalizationfornon-stationarytimeseries. InNeurIPS,2024.
[9] M.Liu,X.Zhang,etal. Non-stationarytransformers:Exploringthestationarityintimeseriesforecasting.
InNeurIPS,2022.
[10] S.Bai,J.Z.Kolter,andV.Koltun.Anempiricalevaluationofgenericconvolutionalandrecurrentnetworks
| forsequencemodeling. | arXiv:1803.01271,2018. |     |     |     |
| -------------------- | ---------------------- | --- | --- | --- |
[11] Y.Nie,N.Liu,etal. Atimeseriesisworth64words:Long-termforecastingwithtransformers. InICLR,
2023.
[12] H.Wu,J.Xu,etal. TimesNet:Temporal2D-variationmodelingforgeneraltimeseriesanalysis. InICLR,
2023.
[13] H.Zhou,S.Zhang,etal. Informer:Beyondefficienttransformerforlongsequencetime-seriesforecasting.
InAAAI,2021.
[14] J.D.Hamilton. Anewapproachtotheeconomicanalysisofnonstationarytimeseriesandthebusiness
| cycle. | Econometrica,1989. |     |     |     |
| ------ | ------------------ | --- | --- | --- |
[15] A. Ang and A. Timmermann. Regime changes and financial markets. Annual Review of Financial
Economics,2011.
[16] F.X.DieboldandR.S.Mariano. Comparingpredictiveaccuracy. JournalofBusinessandEconomic
Statistics,1995.
[17] W.K.NeweyandK.D.West. Asimple,positivesemi-definite,heteroskedasticityandautocorrelation
| consistentcovariancematrix. |                               | Econometrica,1987. |                    |     |
| --------------------------- | ----------------------------- | ------------------ | ------------------ | --- |
| [18] H.White.               | Arealitycheckfordatasnooping. |                    | Econometrica,2000. |     |
[19] P.R.Hansen. Atestforsuperiorpredictiveability. JournalofBusinessandEconomicStatistics,2005.
[20] W.Zhang,X.Li,etal. Test-timeadaptationinnon-stationaryenvironmentsviaadaptiverepresentation
| alignment. | InNeurIPS,2024. |     |     |     |
| ---------- | --------------- | --- | --- | --- |
[21] D.Kim,Y.Lee,etal. Test-timeadaptationinducesstrongeraccuracyandlinearity. InNeurIPS,2024.
[22] V.Christou,etal. Testtimelearningfortimeseriesforecasting. arXiv:2409.14012,2024.
9

A NotationandDerivations
WeexpandtheobjectivesusedinSection4,givegradientsfornorm-onlybatch-normalization(BN)
affineparameters,andexplainwhyeachtermhelpsundertypicalregimeshifts. Symbolsfollowthe
maintext.
A.1 Norm-onlyupdatesasmomentmatching
ConsideraBN-normalizedhiddenchannel
u−µ
|     |     |     | h=BN(u)= |     | , y =γh+β, |     |     |
| --- | --- | --- | -------- | --- | ---------- | --- | --- |
σ
where(µ,σ)aretheBNstatisticsfromthecurrentstreamand(γ,β)arethetrainableaffineparameters.
Underacovariateshiftwithnewmoments(µ′,σ′),thepre-affinehiddenbecomes
|     |     |     |     | u−µ′ | µ−µ′ |     |     |
| --- | --- | --- | --- | ---- | ---- | --- | --- |
σ
|     |     |     | h′ = | =   | h+  | .   |     |
| --- | --- | --- | ---- | --- | --- | --- | --- |
|     |     |     |      | σ′  | σ′  | σ′  |     |
Choosing
|     |     |     |        | σ    |       | µ−µ′ |     |
| --- | --- | --- | ------ | ---- | ----- | ---- | --- |
|     |     |     | γ′ =γ· | , β′ | =β+γ· |      |     |
|     |     |     | σ′     |      |       | σ′   |     |
exactlyrestoresyforalluiftheshiftispurelyfirst/secondmoments. Thussmallchangesof(γ,β)
cancancellocation/scaledriftatthefeaturelevel.
ForascalarlossL,thegradientssatisfy
|     |     | ∂L  |          | ∂L  | ∂L  | ∂L       |     |
| --- | --- | --- | -------- | --- | --- | -------- | --- |
|     |     |     | (cid:88) |     |     | (cid:88) |     |
|     |     |     | =        | h , | =   |          | ,   |
|     |     | ∂γ  | ∂y       | i,c | ∂β  | ∂y       |     |
|     |     |     | c        | i,c | c   |          | i,c |
|     |     |     | i        |     |     | i        |     |
wherecindexeschannelsandiindexesbatchelements. Adapting(γ,β)thereforere-centersand
re-scales along directions where the loss is sensitive. This explains why norm-only is effective
whenregimeshiftsdominantlyalterlow-ordermoments,whichisexactlythecaseinoursynthetic
gradual-driftexperiments.
A.2 Entropyminimizationanddecisionmargin
Foratwo-classsoftmaxpˆ(X)=(p,1−p),theentropyis
H(pˆ)=−plogp−(1−p)log(1−p).
Thederivativeandsecondderivativewithrespecttopare
|     |     | dH  | 1−p  | d2H | 1   | 1   |     |
| --- | --- | --- | ---- | --- | --- | --- | --- |
|     |     |     | =log | ,   | =   | +   | >0, |
|     |     | dp  | p    | dp2 | p   | 1−p |     |
soH isstrictlyconvexinpwithminimaatp ∈ {0,1}. Afirst-orderTaylorexpansionaroundthe
pre-update p shows that a small gradient step with learning rate η reduces H by approximately
0
(cid:0)dH(cid:1)2
η ,pushingposteriorsawayfromindecision. Undertheusualclusterorlow-densityseparation
dp
assumptions,thiscoincideswithincreasingthemarginarounddecisionboundaries,whichisbeneficial
whenP(X)driftsbutclass-conditionalstructurepersists.
A.3 ConsistencyasJacobiancontrolalongcausaldirections
LetT beaweaktime-preservingtransformwithT equaltotheidentity. ByTaylorexpansion,
| ϵ   |     |     |                   |     | 0    |         |     |
| --- | --- | --- | ----------------- | --- | ---- | ------- | --- |
|     |     |     | pˆ(T (X))≈pˆ(X)+J |     | (X)∆ | +O(ϵ2), |     |
|     |     |     | ϵ                 |     | pˆ X |         |     |
(cid:12)
| where∆ | = d T (X)   | (cid:12) andJ | istheJacobianofpˆwithrespecttoX. |             |     |            | Then        |
| ------ | ----------- | ------------- | -------------------------------- | ----------- | --- | ---------- | ----------- |
| X      | d ϵ ϵ       | ϵ=0           | pˆ                               |             |     |            |             |
|        |             |               | (X))∥2                           |             | ∥2  | =∆⊤(cid:0) | J⊤J (cid:1) |
|        | ∥pˆ(X)−pˆ(T |               | ϵ                                | ≈∥J pˆ (X)∆ | X   |            | pˆ ∆ X .    |
|        |             |               |                                  | 2           | 2   | X          | pˆ          |
Minimizing the consistency loss therefore penalizes the directional Jacobian norm along small,
causality-preservingdeformations(re-timing±1,mildamplitudechanges). Thismakespredictions
insensitivetobenignlocalperturbationsthatoftenaccompanymeasurementnoiseormicrostructure
changesundernewregimes.
10

A.4 Augmentation-varianceminimizationandlocalriskcontrol
(cid:80)K
ForregressionwithKtransforms,defineyˆ =yˆ(T (X))andy¯= 1 yˆ . Thesamplevariance
|     |     | k   | k   |     | K k=1 | k   |
| --- | --- | --- | --- | --- | ----- | --- |
K
1 (cid:88)
|     | Var({yˆ | })= |     | (yˆ −y¯)2 |     |     |
| --- | ------- | --- | --- | --------- | --- | --- |
|     |         | k   | K−1 | k         |     |     |
k=1
upper-boundstheexpectedsquareddeviationunderalocalneighborhoodN(X)ofperturbations
HenceminimizingE
whenthetransformsetcoversprincipaldirections. [Var]reducesthelocal
X
Lipschitz constant of the predictor around each X, which is desirable when the test distribution
featurestransientnoiseinflation.
| Thegradientofthevariancetermwithrespecttoeachyˆ |     |         | m       | is    |     |     |
| ----------------------------------------------- | --- | ------- | ------- | ----- | --- | --- |
|                                                 |     | ∂       | 2       |       |     |     |
|                                                 |     | Var({yˆ | })= (yˆ | −y¯), |     |     |
|                                                 |     |         | k       | m     |     |     |
|                                                 |     | ∂yˆ m   | K       |       |     |     |
sothelosspullsdisagreeingoutputstowardtheirmeanandshrinksdispersion.
A.5 EMA-teacherself-distillationastemporalensembling
Letθ˜beanexponentialmovingaverageoftheadaptedparameters:
θ˜←ρθ˜+(1−ρ)θ,
withρ∈(0,1).Underalocallyquadraticlosswithunbiasedgradientnoise,Polyakaveragingimplies
thatθ˜haslowervariancethantheinstantaneousθ.
Distillation
1 (cid:88)
|     | L   | =   | ∥yˆ (X)−yˆ | (X)∥2 |     |     |
| --- | --- | --- | ---------- | ----- | --- | --- |
|     |     | sd  | θ          | θ˜    | 2   |     |
|B|
X∈B
regularizesthestudenttowardalow-passfilteredtarget, dampingoscillationsproducedbysmall
batchesandachangingB. Asimplescalarmodelwithi.i.d.zero-meangradientnoiseshowsthat
theteacher’svarianceisscaledby 1−ρ relativetothestudent’s,solargerρyieldsasteadiertarget.
1+ρ
Thisimprovesstabilitywithoutrequiringlabelsandcomplementsthevariancetermbyanchoringtoa
temporallysmoothedpredictor.
A.6 Driftpenaltyasproximalupdate
LetϕdenotealladaptedBNaffineparameters. Ondaytwesolve
|     | min | L     | (ϕ)+γ∥ϕ−ϕ(t−1)∥2, |     |     |     |
| --- | --- | ----- | ----------------- | --- | --- | --- |
|     |     | unsup |                   |     | 2   |     |
ϕ
whereL unsup istheentropy/consistencyloss(classification)orvariance/distillationloss(regression).
Asinglegradientstepwithstepsizeηgives
|                |     | (cid:16) |                            |     |     | (cid:17) |
| -------------- | --- | -------- | -------------------------- | --- | --- | -------- |
| ϕ(t) =ϕ(t−1)−η |     | ∇L       | (ϕ(t−1))+2γ(ϕ(t−1)−ϕ(t−2)) |     |     | ,        |
unsup
whichisequivalenttoSGDwithaquadraticproximaltermthatshrinksmotiontowardtheprevious
day.Inalocallyquadraticloss,theexactminimizerisaridge-regularizedsolutionwhosedisplacement
satisfies
(ϕ(t−1))∥
∥∇L unsup
|     | ∥ϕ(t)−ϕ(t−1)∥ |     | ≤   |     | ,   |     |
| --- | ------------- | --- | --- | --- | --- | --- |
2γ
explainingtheobservedresistancetooverreactionwhenregimesflipquickly.
A.7 BN-statisticsrefreshasshiftcorrectionwithoutgradients
Forbatchnormalizationwithrunningstatistics(µˆ,σˆ)fromtraining,thestandardBNtransformfora
channelis
u−µˆ
|     |     |     | h= . |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- |
σˆ
11

Refreshingstatisticsonthecurrentunlabeledbatchreplaces(µˆ,σˆ)by(µ ,σ ),sothetransform
B B
becomes
u−µ
B.
|     |     |     |     | h   | B = |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
σ
B
Whentheshiftisprimarilyfirst/second-order,this“zero-gradient”movecancelsmostofthecovariate
shiftatthehidden-layerlevel. Incontrasttonorm-only,whichupdates(γ,β)bygradientdescent,
bn_stats changes the normalizing statistics directly and is much harder to overfit in short, noisy
windows. Thisdifferencematchesourempiricalfindings:bn_statsisasafedefaultonfinancialseries,
whilenorm-onlycanbothhelp(smoothsyntheticdrift)andhurt(noisyrealmarkets).
A.8 Uncertaintyproxyandado-no-harmrule
Let∆Rbethechangeinexpectedlossafteradaptation. Whentheproxyu (entropyoraugmentation
t
variance) is large, empirical evidence indicates higher probability that ∆R > 0 due to unstable
pseudo-objectives. Usingaquantilethresholdτ estimatedonvalidationapproximatesthedecision
rule
|     |     |     |     | P(∆R>0|u |     | )>π |     |
| --- | --- | --- | --- | -------- | --- | --- | --- |
t
forachosentoleranceπ,andthefallbackpolicy“bn_statsinsteadofgradientupdates”controlsthe
frequencyofharmfulstepswithoutneedinglabelsattesttime.
A.9 Gradientsfornorm-onlyBNparameters
ForaBNlayerwithaffineparameters(γ ,β )onchannelcandoutputy forsamplei,thebackprop
|     |     |     |     | c c |     |     | i,c |
| --- | --- | --- | --- | --- | --- | --- | --- |
throughaffineparametersis
|               |     |      | ∂L                         |               |         | ∂L                    |          |
| ------------- | --- | ---- | -------------------------- | ------------- | ------- | --------------------- | -------- |
|               |     |      |                            | (cid:88)      |         |                       | (cid:88) |
|               |     |      | =                          | g i,c         | h i,c , | =                     | g i,c ,  |
|               |     |      | ∂γ                         |               |         | ∂β                    |          |
|               |     |      | c                          |               |         | c                     |          |
|               |     |      |                            | i             |         |                       | i        |
| whereg =∂L/∂y |     | andh | isthenormalizedactivation. |               |         | Thedriftpenaltyadds   |          |
| i,c           | i,c |      | i,c                        |               |         |                       |          |
|               |     |      | (cid:0)                    | −γprev(cid:1) |         | (cid:0) −βprev(cid:1) |          |
|               |     |      | 2γ γ                       |               | ,       | 2γ β                  |          |
|               |     |      |                            | c c           |         | c                     | c        |
toeachgradientterm,shrinkingdailymotioninaffineparameters. Thisisexactlywhatweimplement
inAlgorithm1.
A.10 Entropy/consistencyandcalibration
Minimizingentropyalonecanover-sharpen;pairingitwithconsistencypreventspathologicalcon-
fidencebyforcingagreementacrossbenigntransforms. Empiricallythisimprovescalibration: the
expectedcalibrationerror(ECE)afterTTAoftendecreasesrelativetothepre-adaptationmodelon
thesamestream,especiallyonSPYandQQQwherebn_statsplusconservativenorm-onlyupdates
reducebothlossandECE.
A.11 Multi-stephorizons
ForH-stepregressionyˆ= (cid:80)H rˆ ,thevariancetermstilldecomposesacrosstransforms:
|     |     |          | h=1 t+h  |          |        |          |               |
| --- | --- | -------- | -------- | -------- | ------ | -------- | ------------- |
|     |     | (cid:32) | (cid:33) |          |        |          |               |
|     |     | (cid:88) |          | (cid:88) |        | (cid:88) |               |
|     | Var |          | rˆ       | =        | Var(rˆ | )+2      | Cov(rˆ ,rˆ ), |
|     |     |          | h,k      |          | h,k    |          | h,k h′,k      |
|     |     | h        |          | h        |        | h<h′     |               |
sominimizingaugmentationvarianceindirectlycontrolscovariancebetweenstepwisepredictions,
reducingcompoundingerrortypicalundernoisyregimesandlonghorizons(asinourETTh1H =96
setting).
B SyntheticShiftGenerators
We briefly detail the synthetic shift generators used in Stage I. In all cases, shifts are applied to
the original ETT series channel-wise, and the same random seed is used across methods for fair
comparison.
12

Gradualmean/variancedrift. Letacleanseriesbes ∈Rd. Weaddadriftedversion
t
t t
x =a ⊙s +b , a =1+κ , b =µ +ν ,
t t t t t T t 0 T
whereT isthelengthofthetestsegment,⊙denoteselement-wisemultiplication,andκ,ν aresmall
drift coefficients. We grid κ,ν so that the final change in mean and standard deviation is within
0.2–0.4trainingstandarddeviationsperthousandsteps. Thisproducessmoothlocation-scaledrift
withoutchanginghigher-orderstructure.
Localnoiseinflation. Let
x =s +η , η ∼N(0,σ2I )
t t t t d
be the base noisy series, where σ2 is calibrated from the training set. We then select random
non-overlappingsegmentsoflengthℓ∈[96,192]andset
η ∼N(0,(kσ)2I ), k ∈{1.5,2.0}
t d
withinthosesegments. Thiscreatesburstsofnoiseinflationwhilekeepingtheoveralllevelofthe
processsimilar.
Structuralswitchesinperiodiccomponents. Writeaseasonalcomponentas
M
(cid:88)
c = A cos(2πmt/P +ϕ ),
t m m
m=1
whereP isthebaseperiodand(A ,ϕ )areamplitudesandphases. Atpredefinedchangepoints
m m
{t }J ,wedrawnew(A ,ϕ )whilekeepingtheunconditionalmeanunchanged,andset
j j=1 m m
x =c +ϵ , ϵ ∼N(0,σ2I ).
t t t t d
WeuseJ ∈{2,3}andmoderatechangesin(A ,ϕ )sothatseasonalitypatternsswitchvisiblybut
m m
remainrealistic. Thisisthehardestregimeinourexperiments: evenwithbn_stats,errorsremain
largeandR2isstronglynegative.
C StatisticalTests
Wesummarizethestatisticaltestsusedforforecastandbacktestcomparisons.
Diebold–Mariano(DM)test. Lete(A)ande(B)beforecasterrorsfrommethodsAandBonday
t t
t. Foraper-daylossℓ(·)(cross-entropyforclassification;MAEorMSEforregression),define
T
d =ℓ(e(A))−ℓ(e(B)), d¯= 1 (cid:88) d .
t t t T t
t=1
Underthenullofequalpredictiveaccuracy,E[d ]=0. TheDMstatisticis
t
d¯
DM= ,
(cid:113)
V(cid:100)ar(d¯)
whereV(cid:100)ar(d¯)isaheteroskedasticityandautocorrelationconsistent(HAC)estimatorofthelong-run
varianceof{d }usingNewey–Westweights:
t
(cid:32) q (cid:33)
V(cid:100)ar(d¯)=
T
1 γ
0
+2 (cid:88) w
h
γ
h
, w
h
=1−
q+
h
1
,
h=1
with γ the lag-h sample autocovariance of {d } and q = ⌊4(T/100)2/9⌋ [16, 17]. Under mild
h t
conditions,DMisasymptoticallystandardnormal,sowereporttwo-sidedp-values. Inourtables,
negativeDMvaluesmeanthatthefirstmethodhasloweraveragelossthanthesecond.
13

Newey–West(NW)forreturnsummaries. Givendailystrategyreturnsz ,thesamplemean
t
T
1 (cid:88)
µˆ = z
T t
t=1
hasvariance
(cid:32) q (cid:33)
1 (cid:88)
V(cid:100)ar(µˆ)=
T
γ
0
+2 w
h
γ
h
,
h=1
withthesameNewey–Westweightsw andlagqasabove,andγ thelag-hautocovarianceof{z }.
h h t
TheNWt-statisticfortestingE[z ]=0is
t
µˆ
t = ,
NW (cid:113)
V(cid:100)ar(µˆ)
whichwereporttogetherwithannualizedreturn, annualizedvolatility, andSharperatioforeach
strategyinTables4and5.
14