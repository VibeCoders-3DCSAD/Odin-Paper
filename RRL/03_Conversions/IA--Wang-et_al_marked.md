Review
A Survey of Deep Anomaly Detection in Multivariate Time
Series: Taxonomy, Applications, and Directions
FenglingWang1,YiyueJiang1,RongjieZhang2,AiminWei3,JingmingXie4,*andXiongwenPang2,*
1 SchoolofArtificialIntelligence,SouthChinaNormalUniversity,Foshan528000,China;
wfl314159@163.com(F.W.);jiangyy@m.scnu.edu.cn(Y.J.)
2 SchoolofComputerScience,SouthChinaNormalUniversity,Guangzhou510555,China;zrj22127@gmail.com
3 SchoolofArchitecturalEngineering,GuangzhouPanyuPolytechnicCollege,Guangzhou511483,China;
weiam@gzpyp.edu.cn
4 DoctoralWorkstation,GuangdongSongshanPolytechnic,Shaoguan512126,China
* Correspondence:xiejm@gdsspt.edu.cn(J.X.);augepang@scnu.edu.cn(X.P.)
Abstract: Multivariate time series anomaly detection (MTSAD) can effectively identify
andanalyzeanomalousbehaviorincomplexsystems,whichisparticularlyimportantin
fieldssuchasfinancialmonitoring,industrialequipmentfaultdetection,andcybersecu-
rity. MTSADrequiressimultaneouslyanalyzetemporaldependenciesandinter-variable
relationshipshavepromptedresearcherstodevelopspecializeddeeplearningmodelsto
detectanomalouspatterns. Inthispaper,weconductedastructuredandcomprehensive
overviewofthelatesttechniquesindeeplearningformultivariatetimeseriesanomaly
detectionmethods. Firstly,weproposedataxonomyfortheanomalydetectionstrategies
fromtheperspectivesoflearningparadigmsanddeeplearningmodels,andthenprovidea
systematicreviewthatemphasizestheiradvantagesanddrawbacks. Wealsoorganizedthe
publicdatasetsfortimeseriesanomalydetectionalongwiththeirrespectiveapplication
domains. Finally,openissuesforfutureresearchonMTSADwereidentified.
Keywords: anomalydetection;deeplearningnetwork;multivariatetimeseries
AcademicEditors:JongmyonKim
1. Introduction
andGeorgeD.Magoulas
Time series anomaly detection is crucial in data analysis, focusing on identifying
Received:19November2024
unusualpatternsintimeseriesdatathatsignificantlydifferfromexpectedbehavior[1,2].
Revised:25December2024
Accepted:30December2024 ThistaskbecomesmoreintricateinMTSAD,whichitinvolvesmultiplechannelsorvariates
Published:1January2025 of data. The evolution of sensing technologies and enhancements in data storage have
Citation: Wang,F.;Jiang,Y.;Zhang, propelledtheadoptionofanomalydetectionacrossaspectrumofsectors. Forexample,In
R.;Wei,A.;Xie,J.;Pang,X.ASurvey thefinancialservicessector,itisusedinfinancialservicestoidentifyfraudulenttransactions
ofDeepAnomalyDetectionin andmarketfluctuations,protectingcustomerfunds[3]. Intheindustrialsector,itmonitors
MultivariateTimeSeries:Taxonomy,
equipmentstatustodetectfaultsearly,reducingdowntimeandmaintenancecosts[4].
Applications,andDirections.Sensors
Multivariatetimeseriesanomalydetectionhasbeenstudiedinavarietyofapplication
2025,25,190. https://doi.org/
domainsandhasexperiencedsignificantprogress. Thereexistvariousmethodsproposed
10.3390/s25010190
forMTSAD,includingstatisticalmethods,classicalmethods,distance-basedmethods[5],
Copyright:©2025bytheauthors.
distributional-basedmethods[6],anddensity-basedmethods[7],arestillaviablechoice
LicenseeMDPI,Basel,Switzerland.
ofalgorithm. Statisticaltechniquestypicallyinvolvemovingaverages(MA)andtheau-
Thisarticleisanopenaccessarticle
distributedunderthetermsand toregressiveintegratedmovingaverage(ARIMA)[8]. MAreducetheimpactofrandom
conditionsoftheCreativeCommons fluctuationsbycalculatingtheaveragevaluewithinaspecifictimewindow,therebyreveal-
Attribution(CCBY)license ingtrendsandpatternsinthedata. TheARIMAmodelisapopulartimeseriesforecasting
(https://creativecommons.org/
methodthatcombinesthreecomponents: AutoRegressive(AR),Integrated(I),andMA,
licenses/by/4.0/).
Sensors2025,25,190 https://doi.org/10.3390/s25010190

Sensors2025,25,190 2of27
whichareusedtomodelandpredicttimeseriesdata. Classicalmachinelearningmethods
includeOne-ClassSupportVectorMachine(OCSVM)[9]andSupportVectorDataDescrip-
tion(SVDD)[10]. SVDDissimilartoOCSVM,butinsteadoffindingjustaboundary,itcre-
atesahyperspherethatcontainsthenormaldata. Anydatapointsoutsidethishypersphere
areconsideredanomalies. Distance-basedtechniquesassessthedeviationofobservations
fromrepresentativedatapointsusingdistancemetrics,whiledistributionalmethodsfocus
onidentifyinganomaliesthroughpointswithlowlikelihood. Density-basedmethodsare
basedonthelocaldensityofdatapoints. Ifadatapointhassignificantlylowerlocaldensity
comparedtoitsneighboringarea,itmaybeflaggedasananomaly. However,astarget
systemsgrowinsizeandcomplexity, thesemethodsencounterchallenges, particularly
theirlimitationsinhandlingmultidimensionaldataandthelackoflabeledanomalies[11].
The challenge of MTSAD lies in the need to consider both the dynamic changes along
thetemporaldimensionandtheinterrelationshipsbetweenobservationssimultaneously.
Recently,deeplearning-basedtechniqueshaveadvancedthefieldofanomalydetection
withinmulti-dimensionaldatasets. Thesemethodsexploitpowerfuldeeplearningmodels
likeTransformers[12–14],GNN[15],VAEs[16],GANs[17],Diffusion[18]etc.,areadeptat
representingintricate,non-linearrelationshipsamongvarioussensorsandareproficientin
capturingtemporalcorrelationsandependencieseffectively[19]. Theseadvancedmodels
leverage the capabilities of deep learning to identify and learn subtle patterns in data,
enablingaccurateidentificationandearlywarningofanomalousbehaviorsacrossvarious
fieldssuchasfinancialtransactionmonitoring,cybersecuritythreatdetection,industrial
equipment maintenance forecasting, and healthcare monitoring. The progress of these
technologiesallowsustobetterunderstandandanalyzethecomplexdynamicswithin
multi-dimensionaldatasets,providingpowerfultoolsforreal-timeanomalydetectionand
decisionsupportsystems.
Inthispaper,weaimtoaddressthecurrentknowledgegapbyexploringfeaturesof
timeseries,typesofanomalies,andofferingathoroughoverviewofrecentadvancements
indeeplearningtechniquesforMTSAD.Itreviewsthelatestdeeplearningmethodsfor
this purpose from three perspectives and offers a comprehensive discussion about the
classification of deep learning models. Additionally, it compiles and organizes public
datasetsfortimeseriesanomalydetection,alongwiththeirrespectiveapplicationdomains.
Finally,thepaperwrapsupbyhighlightingpossibledirectionsforfutureresearchtofurther
developthefield.
Insummary,thecontributionsofthispaperinclude:
(1) The investigation and review of anomaly categories in multivariate time series
haveproposedanewclassification;
(2)Focusingonlearningparadigmsandneuralnetworkarchitectures,weconducted
a comprehensive review of the latest deep learning methods from three strategies and
proposedanewtaxonomyforMTSAD;
(3)AnexplorationoffutureresearchopportunitiesforMTSAD.
2. BackgroundandPreliminary
2.1. ProblemDefinition
MTSADreferstotheprocessofidentifyinganomalousbehaviororpatternsthatdevi-
atesignificantlyfromhistoricalpatternswithinthecontextofmultiplerelatedtimeseries.
Comparedtounivariatetimeseriesanomalydetection,multivariateanomalydetectionis
morecomplexasitrequiresconsiderationoftherelationshipsandtemporaldependencies
betweenmultiplevariablessimultaneously[20]. Anomalyscoreisanindicatorusedto
measurethedegreeofanomalyofatimepointortimewindows. Thehighertheanomaly
score,themorelikelythedatapointistobeanomalous.

Sensors2025,25,190
3of27
WeconsideracollectionofMTSdenotedasX. Hence,thedefinitioncanbeexpressed
asfollows:
|         |                                                | X = (x1,x2,...,xC) |             |                 | (1) |
| ------- | ---------------------------------------------- | ------------------ | ----------- | --------------- | --- |
|         |                                                | xc = (x            | ,x ,...,x ) |                 | (2) |
|         |                                                |                    | 1 2 T       |                 |     |
| wherexc | ∈ RT                                           |                    |             | ∈               |     |
|         | representsanT-dimensionalvector,eachdatapointx |                    |             | t Risacquiredat |     |
acertaintimestamptfromasensor. TrepresentsthelengthoflookbackwindowsandC
| representsthenumberofdimensionsorvariables(C |     |     | >1). |     |     |
| -------------------------------------------- | --- | --- | ---- | --- | --- |
GivenamultidimensionaltimeseriesdatasetX ∈ RTXC,thegoalistofindamethod
tocomputeanomalyscores:
|     |     | = (s | )               |     |     |
| --- | --- | ---- | --------------- | --- | --- |
|     |     | S    | 1 ,s 2 ,...,s T |     | (3) |
wheres t ∈ Rdenotestheanomalyscoreattimepointt.Thisallowsustoidentifyanomalous
datapointsthatdeviatefromnormalbehavior.
2.2. AnomalyTypesinMTS
MTSconsistsofasetofunivariatetimeseries(metric),eachofwhichdescribesdifferent
partsorattributesofacomplexentity. Therefore,itnotonlyhastemporaldependencies
within the metrics, manifested as periodic, trend, and other inherent patterns of each
metric, butalsointer-metricsdependencieswithintheentity, representingthelinearor
nonlinearrelationshipsbetweenallmetricsoftheentityateachtimepoint[2,21]. Thus,
anomaliesinMTScanbedividedintointra-metricanomalies(temporalanomalies)and
inter-metricanomalies. Theoverallclassificationframeworkforanomalytypesisshownin
Figure1. Temporalanomaliesoccurinmultivariate,affectingmultipleoralldimensions.
Temporalanomaliesprimarilyfocusonindividualdatapointsandsubsequences. Point-
wiseanomaliesrefertounexpectedeventsatasingletimepoint, wheretheanomalous
behaviorofatimepointcanbeaspikeorglitch. Pattern-wiseanomaliesareanomalous
subsequences, usually discordant or disharmonious. Here are the definitions of types
ofanomalies:
Figure1.Theoverallclassificationframeworkdiagramformultivariatetimeseriesanomalytypes.
2.2.1. Point-WiseAnomalies
Globalpointanomaly: Globalpointanomalyisananomalyinwhichasingledata
point is significantly different from other data. They are typically spikes in the entire
| sequence. | Consideringathresholdδ,itcanbedescribedas: |          |         |     |     |
| --------- | ------------------------------------------ | -------- | ------- | --- | --- |
|           |                                            | |x t −xˆ | t | > δ |     | (4) |

Sensors2025,25,190 4of27
wherex isexpectedvalueandxˆ istheoutputofthemodel,δ = λ∗G(x ),Grepresents
t t t
thevarianceofthecontextoverx ,andλisthethresholdadjustmentcoefficient.
t
LocalpointAnomaly: Localpointanomalyreferstoabnormalsituationsthatoccur
withinspecificenvironmentsorcontexts. Detectinglocalpointanomalytypicallyinvolves
analyzingboththepointanditsassociatedcontextualinformationtoidentifybehavior
thatdeviatesfromtheexpectednormswithinagivencontext. Thistypeofanomalycanbe
definedas:
δ ≈ λ∗L(x t−k : x t+k ) (5)
where x t−k : x t+k = (x t−k ,x t−k+1 ,...,x t+k ) referstothecontextofthedatapoint x t with
a window size k, L represents the variance of this local context. An example of point
anomaliesareshownonFigure2a,globalpointanomaliestypicallystandoutagainstthe
backdropoftheentiretimeseries,whilelocalpointanomaliescontrastmorewiththedata
pointsimmediatelyadjacenttothem.
Figure2.(a)Point-wiseanomalies,thereddotsindicateanomalies,and(b)Patten-wiseanomalies,
theredareasrepresentanomalies.
2.2.2. Pattern-WiseAnomalies
Shapeletanomaly: Shapeletanomaliesarecircumstancethatoccursinaparticular
environmentorcontext. Unlikeindividualdatapointanomalies,shapeletanomaliyindi-
catesthatthecollectivebehaviorofagroupofrelateddatasignificantlydeviatesfromthe
expectedornormalpattern,asshowninFigure2b.
diss (p,pˆ) > δ (6)
p
where pˆspecifiestheexpectedshapeofthesubsequence. dissisafunctionthatmeasures
thedifferencebetweentwosubsequences.
Trend anomaly: Trend anomalies focus on sudden changes or deviations from the
long-termtrendinthedata. Theseanomaliesmayresultfromsuddenevents,systemic
changes, or other factors leading to abrupt shifts or abnormal growth or decline in the
trenddirection.
diss (τ,τˆ) > δ (7)
τ
whereτˆ isthetrendofnormalsubsequences.
Cycle Anomaly: Cycle anomalies occur when there are abnormal changes in the
periodicpatternsoftimeseriesdata. Forexample,thereisanomalyinthefrequencyor
intensityofaseasonalevent.
diss (s,sˆ) > δ (8)
s

Sensors2025,25,190 5of27
wheresˆisthecyclicityofexpectedsubsequences.
2.2.3. Inter-MetricAnomalies
Globalintermetricanomaly: CertainmetricsinMTSexperiencesignificantchanges,
withalengthmatchingtheentiresequence. Thistypeofanomalytypicallyoccurswhen
initialparametersorsystemstatesdeviatefromthenormalrange. Whenthechangeina
keymetrictriggersaseriesofabnormalfluctuationsinrelatedmetrics,theentiresequence
reflectsthisanomaly. AnexampleofanentiresequenceanomalyisshowninFigure3a,as
itsbehaviorsignificantlydeviatesfromthatofothermetrics.
diss (corr(xi,xj)) > δ (9)
corr
where xi, and xj are different metrics, and corr represents the degree of correlation be-
tweenthem.
Figure3. (a)Globalintermetricanomalies. (b)Thered-highlightedareaontheleftindicateslocal
intermetricanomalies,whilethered-highlightedareaontherightindicatestemporal-localintermet-
ricanomalies.
Local intermetric anomaly: There is correlation between metrics within the entity,
whichcanbelinearornonlinear,suchastherelationshipbetweentemperatureandelectric-
ityconsumption. Ifthesecorrelationsaredisrupted,MTSwillexhibitanomalousbehavior.
Duringacertaintimeperiod,therelationshipsbetweenmetricssignificantlydeviatefrom
historicalpatterns,suggestingachangeintheinterdependenciesamongthemetrics. For
example,inFigure3b,thereisinitiallyapositivecorrelationbetweentwometrics,butthe
highlightedredareaontheleftclearlybreaksthisrelationship,leadingtoanomalies.
diss (corr(xi,xj),corr(xi ,x j ) > δ (10)
corr t:t+k t:t+k
wherekisthetimewindow. Ifthecorrelationisdisruptedfromttot+k,itindicatesthat
thecorrelationcoefficienthasexceededthethresholdcomparedtothenormalvalue.
Temporal-localintermetricanomaly: Theanomaliesviolatethedependenciesbetween
metricsandtemporalrelationships,focusingonhowaspecificmetricbreaksitscorrelation
and deviates from its historical trend within a certain time period, as indicated by the
highlightedredareaontherightsideofFigure3b.
2.3. Time/FrequencyDomainAnalysis
Timeseriesfrequencydomainanalysisinvolvestransformingatimedomainsignal,
which is a signal that varies over time, into a frequency-domain representation. This
conversionallowsforabetterunderstandingofthesignal’sfrequencycomponentsand
periodicity. Frequencydomainanalysisrevealsthedifferentfrequencycomponentswithin

Sensors2025,25,190 6of27
atimeseries,whichhelpsinidentifyingcyclicpatterns,trends,andanomalies. Themost
commonlyusedformulaistheDiscreteFourierTransform(DFT):
T−1
X = ∑ x e −i2πkt/T, k =0,...,T−1 (11)
k t
t=0
whereX isthediscretecomplexamplitudeatfrequencyk,x isthetimeseriessignal,and
k t
iistheimaginaryunit.
The Fast Fourier Transform (FFT) typically uses Formula (11) to convert the time
domainintothefrequencydomain. FFTisanefficientcomputationalalgorithmfortheDFT,
itcanconverttheoriginaltimeseriesintoaspectrumandsortitbycoefficients,obtaining
theseasonalcyclebyreversingthehighestfrequency. Mostprogramminglanguagesand
mathematicallibrariesprovidebuilt-inFFTfunctionsthatcanbedirectlyusedtocompute
theDFT.
3. TaxonomyofMTSADMethods
Tosummarizetheexistingdeepmultivariatetimeseriesanomalydetectionmethods,
weproposedataxonomyfortheanomalydetectionstrategiesfromtheperspectivesof
learning paradigms and deep learning models. We present a general pipeline as illus-
tratedinFigure4. Wecategorizeanomalydetectionmethodsintoforecasting,reconstruc-
tionandcontrastivetypes. Aforecasting-basedmodelusesnexttimestamppredictions,
whereasareconstruction-basedmodeluseslatentrepresentationsofthewholetimeseries.
Contrastive-basedmethodsrelyoncalculatingthesimilarityordissimilaritybetweendata
points to conduct analysis and prediction. Table 1 offers a more detailed overview of
thesemethods.
3.1. Temporal/Spatial
Temporalanalysisfocusesonhowvariableschangeovertime,whilespatialanalysis
examineshowthesevariablesvaryacrossdifferentlocationsorspatialunits. Temporaland
spatialperspectivesofferamorethoroughunderstandingoftheunderlyingrelationships
andpatternsinMTS.
Figure4. ThegeneralpipelineforMTSADusingdeeplearningmodels. Givenasourcedata,we
firstprocessthesourcedatausingadataprocessingmodulethatperformsbasicdatacleaningand
normalizationtasks.Subsequently,weutilizetheanomalydetectionstrategiesfromtheperspectives
oflearningparadigmsanddeeplearningmodelstoobtainrepresentationsforexecutinganomaly
detectiontasksacrossdifferentapplicationdomains.

Sensors2025,25,190
7of27
Table1.MultivariateDeepAnomalyDetectionModelsinTimeSeries.T/S:Temporal/Spatial|Values:
[S: Spatial, T: Temporal, ST: Spatio-Temporal], T/F: Time/Frequency domain|Values: [T: Time,
F: Frequency], LP: Learn Paradigms|Values: [Su: Supervised, Un: Unsupervised, Semi: Semi-
supervised,Self:Self-supervised],Input:ModelInput|Values:[P:Point,W:Window].
| Model | Venue | Bonkbone | LP S/T | T/F Input | Code Language |
| ----- | ----- | -------- | ------ | --------- | ------------- |
Forecasting
✓
| DeepAnt[22] | IEEE’2018 | CNN | Un T   | T W | Pytorch |
| ----------- | --------- | --- | ------ | --- | ------- |
| TCN-ms[23]  | IOP’2019  | CNN | Semi T | T W | – –     |
✓
| TimesNet[24] | ICLR’2023     | CNN | Un T   | F W | Pytorch      |
| ------------ | ------------- | --- | ------ | --- | ------------ |
| LSTM-NDT[25] | KDD’2018      | RNN | Un T   | T W | ✓ Tensorflow |
| LGMAD[26]    | Elsevier’2019 | RNN | Semi T | T P | – –          |
| THOC[27]     | NeurIPS’2020  | RNN | Self T | T W | – –          |
| AD-LTI[28]   | TKDE’2020     | RNN | Un T   | F P | – –          |
✓
| MTAD-GAT[29]    | ICDM’2020  | GNN         | Self ST | T W | Tensorflow |
| --------------- | ---------- | ----------- | ------- | --- | ---------- |
| GDN[30]         | AAAI’2021  | GNN         | Un S    | T W | ✓ Pytorch  |
| FuSAGNet[31]    | KDD’2022   | GNN         | Un ST   | T W | – –        |
| DVGCRN[32]      | ICML’2022  | GNN         | Un ST   | T W | – –        |
| DyGraphAD[33]   | ACM’2024   | GNN         | Un ST   | T W | – –        |
| MAD[34]         | IJCNN’2022 | Transformer | Self T  | T W | – –        |
| CLFormer[35]    | EAAI’2023  | Transformer | Un ST   | T W | – –        |
| AnomalyBERT[36] | ICLR’2023  | Transformer | Self T  | T W | ✓ Pytorch  |
Reconstruction
✓
| DAGMM[37] | ICLR’2018 | AE  | Un T | T P | Pytorch |
| --------- | --------- | --- | ---- | --- | ------- |
✓
| MSCRED[38]   | AAAI’2019    | AE      | Semi T | T W | Tensorflow   |
| ------------ | ------------ | ------- | ------ | --- | ------------ |
| USAD[39]     | KDD’2020     | AE,GAN  | Un T   | T W | ✓ Pytorch    |
| NPSR[40]     | NeurIPS’2024 | AE      | Un T   | T W | ✓ Pytorch    |
| LSTM-VAE[41] | IEEE’2018    | VAE,RNN | Semi T | T P | ✓ Tensorflow |
✓
| OmniAnomaly[42] | KDD’2019 | VAE,GRU | Semi T | T W | Tensorflow |
| --------------- | -------- | ------- | ------ | --- | ---------- |
✓
| InterFusion[43] | KDD’2021 | VAE | Un T | T W | Tensorflow |
| --------------- | -------- | --- | ---- | --- | ---------- |
✓
| SLA-VAE[44] | WWW’2022   | VAE | Semi T | T W | Pytorch      |
| ----------- | ---------- | --- | ------ | --- | ------------ |
| LARA[16]    | WWW’2024   | VAE | Un T   | T W | ✓ Pytorch    |
| MAD-GAN[45] | ICANN’2019 | GAN | Un ST  | T W | ✓ Tensorflow |
✓
| TadGAN[46] | IEEE’2020 | GAN,LSTM | Un T | T W | Pytorch |
| ---------- | --------- | -------- | ---- | --- | ------- |
✓
| MIM-GAN[47] | IEEE’2023 | GAN,LSTM | Un T | T W | Tensorflow |
| ----------- | --------- | -------- | ---- | --- | ---------- |
✓
| DAEMON[48]      | WSDM’2023    | GAN,AE       | Un T  | T W | Pytorch   |
| --------------- | ------------ | ------------ | ----- | --- | --------- |
| DCGAN[17]       | AAAI’2024    | GAN,CNN      | Un T  | T W | ✓ Pytorch |
| DiffusionAE[49] | ICDMW’2023   | Diffusion,AE | Un T  | T W | ✓ Pytorch |
| D3R[18]         |              |              |       |     | ✓         |
|                 | NeurIPS’2024 | Diffusion    | Un ST | F W | Pytorch   |
✓
| TransAnomaly[50] | CCDC’2021 | Transformer,VAE | Un T | T W | Pytorch |
| ---------------- | --------- | --------------- | ---- | --- | ------- |
✓
AnomalyTransformer[51] ICLR’2022 Transformer Un T T W Pytorch
| TranAD[52] | VLDB’2022    | Transformer | Un T | T W | ✓ Pytorch |
| ---------- | ------------ | ----------- | ---- | --- | --------- |
| MEMTO[53]  | NeurIPS’2023 | Transformer | Un T | T W | ✓ Pytorch |
✓
| Dual-TF[54] | WWW’2024 | Transformer | Un T | TF W | Pytorch |
| ----------- | -------- | ----------- | ---- | ---- | ------- |
✓
| CATCH[55] | arXiv’2024 | Transformer | Un T | TF W | Pytorch |
| --------- | ---------- | ----------- | ---- | ---- | ------- |
Contrastive
| AnomalyLLM[56] | arXiv’2024 | LLMs | Un ST  | T W | ✓ Pytorch |
| -------------- | ---------- | ---- | ------ | --- | --------- |
| aLLM4TS[57]    | ICML’2024  | LLMs | Self T | T W | ✓ Pytorch |
| AnomalyLLM[58] | IJCAI’2024 | LLMs | Self T | T W | – –       |
✓
| PatchAD[59]    | arXiv’2024    | MLP-Mixer   | Un T   | T W | Pytorch   |
| -------------- | ------------- | ----------- | ------ | --- | --------- |
| TRL-CPC[60]    | Elsevier’2022 | Transformer | Un T   | T W | – –       |
| RESIST[61]     | Springer’2022 | Transformer | Un T   | T W | – –       |
| Dcdetector[13] | KDD’2023      | Transformer | Self T | T W | ✓ Pytorch |
✓
| SimAD[62] | arXiv’2024 | Transformer | Un T | T W | Pytorch |
| --------- | ---------- | ----------- | ---- | --- | ------- |
✓
| RESTAD[63] | arXiv’2024 | Transformer | Un T | T W | Pytorch |
| ---------- | ---------- | ----------- | ---- | --- | ------- |
3.2. RelatedLearningParadigms
Unsupervised,semi-supervisedandself-supervisedmethodsarecommonlearning
paradigmsinMTSAD,andtheycanbedistinguishedaccordingtothelabelinformationof
thedataandthedegreeofsupervision:

Sensors2025,25,190 8of27
UnsupervisedLearning:Unsupervisedanomalydetectiondoesnotrelyonanylabeled
anomalous data for training. It attempts to discover anomalous patterns by analyzing
thefeaturesofthetimeseries,whichmeansitneedstouseonlynormaldataduringthe
trainingphase.
Semi-unsupervisedLearning: Insemi-supervisedlearning,onlypartofthetraining
datahaslabelinformation,whiletheotherpartofthesamplehasnolabelinformation,
the model uses the sample with label information to learn during the training process,
andtriestoimprovetheperformancethroughtheunlabeledsample. Inthemultivariate
timeseriesanomalydetection,thesemi-supervisedlearningmethodcanusethelabeled
anomaly sample the original and unlabeled normal samples are trained to distinguish
betweennormalandabnormaltimeseriespatterns.
Self-supervised Learning: Self-supervised methods utilize unlabeled data to train
models by creating supervisory signals from the data itself. These methods typically
involvepredictingmissingpartsorpropertiesoftheinputbasedontheobserveddata,
allowingthemodeltolearnusefulrepresentationswithoutrequiringexplicitlabels,which
canthenbeappliedtovariousdownstreamtasks.
3.3. ModelInput
Themodelinputofmultivariatetimeseriesanomalydetectioncanbetimestepsor
windows(slidingwindows).Timestepsrefertoindividualpointsintimewhereobserva-
tionsarerecordedforeachvariableinthemultivariatetimeseries. Eachtimestepincludes
measurementsforallvariablesatthatspecificmoment. Windowissubsetsofconsecutive
timestepswithafixedsize.Thesewindowsareusedtoaggregatedataovertime,capturing
temporalpatternsandrelationshipsamongvariableswithineachwindow. Inrealworld,
thereareoftencomplexstructuressuchasnoise,seasonality,trends,etc.,andanomalies
usuallydonotappearatasinglepointintime,butpersistorpresentapatternoveraperiod
oftime. Therefore,themostrecentMTSADmodeltakesawindowinsteadofasinglepoint
asthemodelinput.
4. ForecastingMethods
Forecasting-based methods use historical data of time series to train a predictive
model that can forecast future data points. This method assesses the anomaly level by
comparing predicted values with actual values, considering anomalies as a significant
increaseinpredictionerror,asillustratedinFigure5a. Thissectionwillexplorepredictive
anomalydetectionmethods,focusingprimarilyonfourtypes: CNN-based,RNN-based,
GNN-based,andTransformer-basedmodels.
Figure5.Theexamplesofeachtypeofanomalycriteria:(a)aforecastingloss;(b)areconstruction
loss;and(c)acontrastiveloss.

Sensors2025,25,190 9of27
4.1. CNN-BasedModels
DeepAnt[22]proposesanunsupervisedanomalydetectionmethodbasedonCNN,
whichdoesnotrequirelabeledtrainingdata. ThismethodusesCNNtoautomaticallylearn
therepresentationoftimeseriesdataandidentifiesanomaliesusingreconstructionerror.
ComparedtotraditionalCNNs,TemporalConvolutionalNetworks(TCN)canbetterhandle
thetemporalcharacteristicsoftimeseries,TCN-ms[23]usesTCNforanomalydetection,
emphasizingtheimportanceoftemporalinformation. Byintroducingcausalconvolution
anddilatedconvolutionintheconvolutionoperationtoprocesstimeseriesdata,ithelpsto
capturelongdistancedependencies. However,theaforementionedmethodsonlyconsider
theone-dimensionalchangesofthetimeseries. Toenhancethemodel’sunderstandingof
thestructureoftimeseries,TimesNet[24]extendstheanalysisoftemporalchangesto2D
spacebyinnovativelyincorporatesFastFourierTransform,makingiteasytomodel2D
changeswith2Dkernels,andprovidinganewperspectiveformorecomplextimeseries
analysis. Itnotonlyimprovestheaccuracyofanomalydetectionbutalsoenhancesthe
model’sgeneralizationabilityofthemodelfortimeseriesdata.
4.2. RNN-BasedModels
LSTM-NAT[25]representsaninnovativeapplicationofRNNsforspacecrafttelemetry
analysis, emphasizingtheuseofLSTM[64]toidentifyanomalieswithincomplexdata.
Unliketraditionalmethods,LSTM-NATemploysanon-parametricdynamicthresholding
method,utilizinganunsupervisedapproachtoassessresidualsanddeterminewhether
predictionerrorsindicatespacecraftanomalies. However,itsrelianceonone-dimensional
outputslimitsitsabilitytohandlehigh-dimensionaldatainmultivariatescenarios. Build-
inguponthisfoundation,LGMAD[26]integratesLSTMwiththeGaussianMixtureModel
(GMM)[65],providingacomprehensivesolutionforlow-dimensionalsystemcharacteris-
tics. Thismethodnotonlyenhancestheefficiencyofanomalydetectionthroughthehealth
factorbutalsoexpandsitsapplicationtotheprocessingofMTSbyleveragingthestrengths
ofbothLSTMandGMMincapturingtemporaldynamicsandanalyzingfeaturecorrela-
tions. AnothernotableadvancementincapturingtemporaldynamicsistheTHOC[27].
ByintroducingtheTemporalHierarchicalOne-Classnetwork,whichusesadilatedRNN
with skip connections [66], the limitations of LSTM in capturing multi-scale temporal
dynamicsareaddressed. ThehierarchicalclusteringprocessofTHOCandtheintroduction
ofaself-supervisiontaskinthetemporaldomainsignificantlyenhancethemodel’sability
todetectanomaliesinreal-worldtimeseriesdata. However,theseschemesmayrequire
adjustmentsforspecifictypesofmulti-seasonaltimeseriesdatatoensuretheiraccuracy
andefficiency. Wuetal. [28]proposedanunsupervisedschemewithmulti-seasonality.
AD-LTIintroducedanewmetric—LocalTrendInconsistency(LTI),whichcanbecomputed
efficientlyandrobustlyscorestheprobabilityofanomaliesforeachdatapoint.Itovercomes
thechallengesofrequiringlabeleddataandthecomputationalintensityofprocessinglarge
volumesofdata,makingitsuitableforavarietyofevent-sensitivescenarios.
4.3. GNN-BasedModels
InthefieldofMTSAD,capturingthecomplexrelationshipsanddynamicchanges
inMTSiscrucial. TheMTAD-GAT[29]modellearnscomplexdependenciesonboththe
featureandtemporaldimensionsviaagraphattentionnetwork[67]andachieveshigh
performanceinMTSADthroughajointoptimizationstrategy. However,itmayencounter
issueswithefficiencyandscalabilitywhendealingwithlarge-scaledatasets. GDN[30]
leveragesgraphneuralnetworkstolearnadependencygraphamongsensorsandenhances
theinterpretabilityofanomalydetectionthroughattentionweights. However,itfailsto
fullycapturethespatialandtemporalcorrelationsbetweensensorswhenprocessingsensor

Sensors2025,25,190 10of27
data. To address these issues, Chen et al. [31] proposed DVGCRN, effectively models
thespatialandtemporalcorrelationsoftimeseriesbycombininganEmbedding-Guided
ProbabilisticGenerativeNetwork(DEPN)withanadaptivevariationalgraphconvolutional
recurrent network(GCRN), demonstrating superior performance in anomaly detection.
FuSAGNet[32]integratesfeatureselectionwithGNNstoeffectivelyidentifyandmodel
the relationships between different time series features. The model constructs an inter-
seriesadjacencymatrixbasedonthelatentfeaturerepresentationsgeneratedbyasparse
auto-encoder,enhancingitsabilitytodetectanomalies. TheDyGraphAD[33]framework
strengthens the capture of short-term and long-term dependency relationships in time
seriesthroughdynamicgraphforecasting,therebyimprovingdetectionaccuracy.
4.4. Transformer-BasedModels
Transformer-based models, with their self-attention mechanisms, have become a
cornerstoneinavarietyofsequencemodelingtasks[12],includingtimeseriesanalysis.
These models are particularly adept at capturing the inherent temporal dynamics and
complexpatternsintimeseriesdata.
AnomalyBERT[36]utilizesaself-supervisedmethod,whichdoesnotrequirelabeled
data,acommonscenarioinreal-worldsituations. Itsinnovativedatadegradationscheme
introduces synthetic outliers, enhancing the model’s ability to detect various types of
anomalieswhileeffectivelycapturingtemporaldependenciesandcontextualinformation
usingtheTransformerarchitecture. However,themodelmayfacechallengesintraining
duetothecomplexityoftheTransformerarchitectureandtheneedtobalancethedata
degradationscheme. MAD[34]alsoadoptsaself-supervisedlearningapproach,eliminat-
ingtheneedforlabeleddata. However,MADfocusesonmaskedmodeling,simplifying
thetrainingprocessbylearningrepresentationsofnormality,whichreducesthecomplexity
introducedbytheintegrationofsyntheticoutliers. MADimprovesuponthetraditional
NextStepPrediction(NSP)taskbyusingmaskedinputs,allowingthemodeltolearnfrom
bidirectionalcontexts. Nevertheless,comparedtoNSPmodels,MADisslowerduringthe
inferenceprocess,especiallywhenmaskingallstepssequentially. Toenhanceinference
speed while maintaining accuracy, CLformer [35] proposes a lightweight Transformer,
enhancinglocalfeatureextractionthroughmulti-scalecausalconvolutionandreducing
erroraccumulation. Additionally,theblockrecurrentpredictionstrategydecreasestime
andspacecomplexity,leadingtofasterinference.
4.5. ProsandCons
Thissectionexplorestheadvantagesanddisadvantagesofprediction-basedtimeseries
anomalydetectionmethods.CNNsexcelasfeatureextractorsforcapturinglocalfeaturesin
timeseriesdata;however,theirkernelsizeandoperationalmechanismslimittheirability
tocaptureglobaldependencies,whichrestrictstheirperformanceasabackbonefortime
seriesdata. RNN-basedmodelsperformwellincapturinglong-termdependencies,but
facescalabilitychallengeswhenprocessinglongsequencesduetotheirsequentialnature
andmemorylimitations. GNN-basedmodelsprovidedeepinsightsintospatio-temporal
dynamics,buttheirincreasedcomputationalcomplexityposesadditionalchallengeswhen
handlinglarge-scaleorhigh-dimensionaldata,andtheymaynotbesuitablefornon-graph
orfuzzygraphstructures. Incontrast,Transformer-basedModelstypicallyoutperform
othersinanomalydetectiontasks,astheyarebetterathandlinglong-rangedependencies
andachievingparallelprocessing. However,thesemodelsmayrequirefurtheradjustments
toensurethatimportantcontextualinformationisnotoverlooked.

Sensors2025,25,190 11of27
5. ReconstructionMethods
Reconstruction-basedmethodsuseanormaldatasettotrainamodelthatattempts
to encode the data into a latent space and then reconstruct the original data from this
representation. Reconstructionlossiscalculatedbycomparingthedifferencesbetweenthe
reconstructeddataandtheoriginaldata,asillustratedinFigure5b. Thissectiondelvesinto
reconstructionanomalydetectionmethods,focusingonfourtypes: AE-based,VAE-based,
GAN-based,Transformer-based,andDiffusion-basedmodels.
5.1. AE-BasedModels
Asaninnovativeapplicationinthefieldofunsupervisedlearning,modelsbasedon
autoencoders(AE)[68]havemadesignificantprogressintheareaofAD.DAGMM[37]
isthepioneeringmodelthatintegratesdeepAEwithGMM[65]forunsupervisedanomaly
detection. Unlike traditional techniques that perform density estimation after dimen-
sionality reduction, DAGMM optimizes both processes simultaneously, ensuring that
keyinformationforanomalydetectionispreserved. However,DAGMMreliesondeep
autoencoders,whichfacechallengesinescapinglocaloptimaandrequiresubstantialcom-
putationalresources. Toaddressthisissue,USAD[39]wasproposed,utilizingadversarial
trainingtoenhancethestabilityandspeedofautoencoder-basedanomalydetection. The
architecture of USAD enables it to train quickly and isolate anomalies effectively, mak-
ingitsuitableforlarge-scaleapplications. However,USADmaystrugglewithdetecting
subtleanomaliesbecauseitfocusesonreconstructionerror. Inresponsetothischallenge,
Zhang et al. [38] introduced MSCRED, which incorporates a multi-scale convolutional
recurrentencoder-decoderframeworktocapturetemporaldependenciesandinter-sensor
correlationswithinmultivariatetimeseriesdata. Itsapproachusingsignaturematrices
andanattentionmechanismallowsthemodeltorobustlydiagnoseanomaliesofvarying
severitylevels. However,thecomplexityofthemodelmayposechallengeswhendeal-
ing with extremely high-dimensional data or real-time applications. The next method
NPSR,proposedbyLaietal. [40],alsofacesthechallengeofhandlingthecomplexityof
high-dimensionaldata. NPSRmodulatestheanomalydetectionprocessbyintroducinga
NominalityScore,balancingthedetectionofpointandcontextualanomalies. TheNPSR
framework includes both point-based and sequence-based reconstruction models, and
itsperformancesurpassesexistingtechniques,offeringatheoreticallygroundedmethod
for anomaly detection. Further optimization is still needed for its application in high-
dimensionalsettingstoensurecomputationalefficiency.
5.2. VAE-BasedModels
VariationalAutoencoders(VAEs)[69]useanencodertomapinputdataintoaspace
oflatentrandomvariables,andthenreconstructthedatafromthisspacewithadecoder.
LSTM-VAE[41],theformernetworkisreplacedbyLSTMinVAE.However,LSTM-VAE
ignoresthetemporaldependencebetweenstochasticvariates. Hence,OmniAnomaly[42]
wasproposed,themodelisthefirstMTSADalgorithmcapableofhandlingexplicittem-
poraldependenciesamongrandomvariables. Itprovidesanovelmethodforentity-level
anomaly explanation through stochastic recurrent neural networks, the objective is to
learnthenormalpatternsofdataandutilizereconstructionprobabilityforanomalyde-
tection. Additionally,InterFusion[43]isanunsupervisedmethodthatmodelsboththe
inter-dependencyandtemporaldependencyofMTSsimultaneously. Itscoreideainvolves
modeling the normal patterns within data using a hierarchical VAE with two stochas-
ticlatentvariables,eachlearninglow-dimensionalembeddingsofeitherinter-metricor
temporalaspects. UnsupervisedVAEisvulnerabletotheinfluenceofanomalousinputs.
SLA-VAE[44]addressesthechallengeofobtaininglabeleddatainInterFusionthrough

Sensors2025,25,190 12of27
semi-supervisedlearning,utilizingactivelearningtoleverageasmallnumberofhighly
uncertain samples for learning and updating online system anomaly detection models.
LARA[16]solvestheneedforonlinesystemstoquicklyadapttonewdistributionswitha
lightweightretrainingapproach. LARAdesignstheretrainingprocessasaconvexproblem
topreventoverfittingandensurerapidconvergence. Italsohasthecapabilitytoutilize
historicaldatawithouttheneedforstorage.
5.3. GAN-BasedModels
TheprincipleofGAN[70]isbasedonaframeworkknownasadversarialtraining,
whichconsistsoftwocomponents: ageneratordesignedtomimicthedistributionofreal
data,andadiscriminatortaskedwithdistinguishingbetweengeneratedandauthenticdata.
MAD-GAN[45]employsLSTM-RNNsasboththegeneratoranddiscriminatorwithin
aGANframeworktoseizethetemporalrelationshipsbetweentimeseriesdistributions,
whilealsotakingintoaccountthecompletedatasettouncovertheunderlyinginteractions
amongthem. MAD-GANusingstandardadversariallosssuffersfromgradientexplosion
andmodecollapse. Hence,TadGAN[46]combineswassersteinloss[71]andcycleconsis-
tencyloss[72]toformthefinalminmaxobjective,theformeraimstomatchthedistribution
ofgeneratedtimeserieswiththedatadistributionofthetargetdomain,whilethelatter
preventsconflictingoutputsbetweenthetwogenerators. Additionally,MIM-GAN[47]
introducesanexponentialinformationmetricintothelossfunctionofGANstoavoidlocal
optimalsolutionandmodelcollapse. Itconsidersadiscriminativereconstructionscore
composedofdiscriminativeandreconstructionloss. MIM-GANemploysLSTM-basedgen-
eratorsanddiscriminatorstocapturetemporalrelationshipswithinthedata.Soft-DTW[73]
isusedasadifferentiablealternativeforthereconstructionloss,andthecombinationof
reconstructionlossandthepriorprobabilitydistributionofthelatentspaceservesasthe
anomalyscore. DCGANs[17]canadjustthegeneratortoproducesamplesclosertoreal
databyminimizingtheSoft-DTWloss. DCGANsutilizeCNNsinboththegeneratorand
discriminatornetworks,whileperformingparallelcomputationforthereconstructionof
multiplepoints,effectivelyalleviatingperformancebottlenecks(i.e.,ModeCollapse). In
complexsystems,thedatageneratedbydevicesexhibitcomplexpatternsandascarcityof
labeleddata,makinganomalydetectionasignificantchallenge. DAEMON[48]employs
twodiscriminatorstoadversariallytrainanautoencodertolearnthenormalpatternsof
timeseries, usingreconstructionerrorstoidentifyanomalies. Itsrobustnessisensured
throughregularizationofhiddenvariablesandreconstructeddata.
5.4. Transformer-BasedModels
Duetothecomplextemporalcharacteristics(i.e.,temporaldependency,inter-variable
correlations,andnoise)inmultivariatetimeseries,manydifferenthybridschemeshave
beenproposed. TransAnomaly[50]isthefirstmodelcombiningTransformerandVAEfor
timeseriesdata. TransAnomalyenablesmoreparallelizationandreduceslearningcosts.
TranAD[52]proposestheuseofattention-basedsequenceencodersforrapidinference,
combinedwithadaptiveconditioningandadversarialtrainingtoenhancethestabilityof
themodel. However,theproblemofover-generalizationpersists. MEMTO[53]introduces
a novel memory module that can learn how each memory item should be updated in
responsetoinputdata,adaptingtodiversenormalpatterns. Duetotherarityofanomalies
intimeseriesdataandthedifficultyofestablishingnon-trivialassociationsfromanomalies
totheentireseries,AnomalyTransformer[51]calculatesassociationdiscrepancythrougha
newAnomaly-Attentionmechanismandenhancesthedistinguishabilitybetweennormal
andabnormalpointswithaminimaxstrategy,demonstratingthepotentialofTransformers
incapturingassociationsofanomalypointsintimeseries.

Sensors2025,25,190 13of27
Theaforementionedmethodsareallinthetimedomainanddonotutilizefrequency
domaininformation. Recentstudieshaveattemptedtoimprovetheaccuracyofanomaly
detection by combining information from both the time and frequency domains. Dual-
TF [54] proposes a Nested-Sliding Windows (NS-window) technique, where anomaly
scoresinthetimedomainarecalculatedwithintheouterwindow, andanomalyscores
inthefrequencydomainarecalculatedwithintheinnerwindow,achievingalignmentof
anomalyscoresatthegranularityofindividualdatapoints. CATCH[55]performspatching
operationsinthefrequencydomaintocapturefine-grainedfrequencycharacteristicsand
usesaChannelFusionModule(CFM)toperceivecorrelationsbetweenchannels. Ituses
Frequency-EnhancedPoint-GranularityScoringtechnology[54]tocalculatetheanomaly
scoreforeachtimepoint, whichinvolvespatchscanningandfrequencyreconstruction
withintheinputwindow.
5.5. Diffusion-BasedModels
DiffusionmodelsperturbtheobserveddatabygraduallyaddingGaussiannoise[74]
andthenutilizealearnabletransformationtorecovertheoriginaldata.
DiffusionAE [49] conditions the diffusion process on autoencoder reconstructions
ratherthantheoriginaldata. DiffusionAEachievesgreaterrobustnesstovaryingtraining
anomaly ratios and better handling of multiple anomaly types (i.e., point anomaly) in
the dataset. The diffusion process smooths out abnormal fragment, resulting in higher
reconstructionerrors,whichinturnimprovesperformance. However,thetrainingcostto
adjusttheinformationbottleneckinthereconstructionprocessishigh. D3R[18]introduces
amethodcallednoisediffusiontoexternallymanagetheinformationbottleneck. Diffu-
sionreframesthebottleneckbytreatingnoiseasthelimitingfactoranduncontaminated
informationasacondition. Asthebottleneckisnolongerinherenttothemodel,itcanbe
adjustedinsizewithoutrequiringretraining.
5.6. ProsandCons
Thissectiondescribestheadvantagesandlimitationsoftheaforementionedanomaly
detectionmodelsfortimeseriesdata.AE-basedmethodsautomaticallyextractdatafeatures
but cannot capture all the complexities of the data and have difficulty interpreting the
meaningofreconstructionerrors. VAEisadeptatexplicitlymodelingprobabilitiesand
provideatheoreticalfoundationforunderstandingdatadistributions.However,themodels
relyontheassumptionofGaussiandistributions,whichmaylimittheexpressivepowerof
thesemodels. GAN-basedmodelslearncomplexdatadistributionsthroughadversarial
training,maintaininganimpressivefidelitytotheoriginaldatadistributions. Nevertheless,
theyareverychallengingtotrainduetoissueslikevanishinggradients[75],whichcan
hindermodelstabilityandconvergence. Diffusionmodelsperformwellwhenfacingnoise
andmissingdata,astheycaninfermissingpartsduringthegenerationprocess,allowing
them to better understand the distribution of normal data when detecting anomalies.
However,whenhandlingtheboundarybetweenmissingandobservedparts,themodel
mayexhibitinconsistencies[49]. Additionally,capturingthedynamiccharacteristicsof
timeseriesmayrequirefurtheradjustmentsandimprovements.
6. ContrastiveMethods
Contrastivemethodsoperatewithintheframeworkofcontrastivelearning, which
typicallyinvolvesadual-towermodel. Timeseriesdataisinputintotwodistinctrepresen-
tationlearningnetworkstogeneratetworepresentationvectors. Duringtherepresentation
learningphase,representationsofthetimeseriesareextractedfromdifferentperspectives,
itisnecessarytouseacontrastivefusionmodule(suchasupsampling)toaligntherep-

Sensors2025,25,190 14of27
resentationstoeachtimestep. Subsequently, acontrastivelossisemployedtocalculate
thesimilaritybetweendifferentrepresentations. AsillustratedinFigure5c. Themethod
iscommonlyusedinunsupervisedorself-supervisedlearningtasks. Thissectiondelves
intocontrastiveanomalydetectionmethods,focusingonthreetypes: Transformer-based,
MLP-basedmodels,LLMs-bsed.
6.1. LLMs-BasedModels
Recently,LLMshavegainedpopularityintimeseriesAnalysis[76,77]. Refs. [56,58]
paperssharethesamemodelname,AnomalyLLM,buttheyadoptdifferentstrategiesto
addressanomalydetectionissuesintheirrespectivefields. TheformerAnomalyLLM[56]
involvespre-trainingadynamic-awareencodertogeneraterepresentationsofedgesin
dynamicgraphs. Thisincludesconstructingstructural-temporalsubgraphsandoptimizing
with contrastive loss to capture the structural and temporal information of the edges.
Byselectingwordembeddingsrelatedtodynamicgraphsandclusteringthemintotext
prototypes,thesetextprototypesarethenusedtoreprogramedgeembeddingstoalignthe
semanticsbetweendynamicgraphsandLLMs. Aprompttemplateisdesignedtoencode
theinformationofafewlabeledsamplesintotheLLM,enablingthemodeltoadaptto
varioustypesofanomalieswithoutupdatingmodelparameters. Thelatter,proposedby
Liuetal. [58],introducesaknowledgedistillation-basedmethodwhereastudentnetwork
is trained to mimic the output of a teacher network that is pre-trained on a large-scale
dataset. During the testing phase, anomalies are detected when there is a significant
discrepancy between the outputs of the student and teacher networks. To consolidate
normalfeatureextraction,prototypicalsignalsareincorporatedintothestudentnetwork,
makingitmorefocusedonhistoricalnormalpatterns. Syntheticanomaliesaregenerated
throughdataaugmentationtechniquestoexpandtherepresentationgapbetweenthetwo
networks. Additionally,acontrastivelossisusedtobringtherepresentationsoforiginal
andaugmentedsamplesintheteachernetworkclosertogether,servingasaregularization
termtoencouragetheteachernetworktocapturemoregeneralpatterns.
aLLM4TS[57]adaptsLLMsfortimeseriesthroughatwo-stagetrainingstrategy. Ini-
tially,itundergoescausalcontinuouspre-trainingonvarioustimeseriesdatasets,followed
by fine-tuning for multi-patch prediction in specific time series contexts. A distinctive
featureofthisframeworkisthepatch-wisedecodinglayer,whichconvertsindividualdata
patches(segments)directlyintotimeseries,therebysignificantlyenhancingthemodel’s
abilitytomastertimeseriesrepresentationsbasedontemporalpatches.
6.2. MLPMixer-BasedModels
Recently,analysesoftimeseriespredictionhaveshownthattheMLP-Mixercaneffec-
tivelyhandlesequentialdata[78–80]. PatchAD[59]representsadeparturefromtraditional
reconstruction-basedapproaches. ThemodelconsistsoffourdistinctMLPMixers,specifi-
callydesignedtoachieveefficiencyandlight-weightusingtheMLParchitecture. PatchAD
innovativelyintroducesadual-projectionconstraintmoduletoalleviatepotentialmodel
degradation. For practitioners and researchers seeking the latest and potentially more
effectivemethodsforMTSAD,thispapermaybevaluablereadingmaterial.
6.3. Transformer-BasedModels
Existingreconstruction-methodsfrequentlyfailtohandlesufficienttemporalcontext
andinadequaterepresentationofnormalpatterns,hinderingtheireffectivenessinidentify-
ingabnormalbehaviors. TheTRL-CPC[60]explorestheintegrationofcontrastivelearning
intotimeseriesanalysis. InTRL-CPC,thecontextvectorsrepresentobservationwindows
inMTS.Thelatentrepresentationsofsubsequenttimestepsareobtainedthroughnonlinear
transformationsofthesecontextvectorsarecontrastedwiththelatentrepresentationsof

Sensors2025,25,190 15of27
theencoderformultivariatetimeseriestomaximizepositivedensity. RESIST[61]relies
onarobustlossfunctionbasedoncontrastivelearningtotrainaTransformerthatmodels
theexpectedbehaviorofnetworkactivity,withouttheneedforananomaly-freetraining
subset. Itautomaticallymitigatestheimpactofatypicalcorruptedtrainingdatatoreduce
theirinfluenceontrainingoptimization. DCdetector[13]employsacontrastivelearning
frameworktolearnrepresentationsoftimeseriesdata. Byutilizingadual-attentionmecha-
nism,itobtainsrepresentationsoftheinputtimeseriesfromtwobranches(thein-patch
branchandthepatch-wisebranch). Thecontrastivelossfunctionisdefinedbymeasuring
the similarity of representations from these two different perspectives, thus acquiring
permutation-invariantrepresentationswithsuperiordiscriminativecapabilities.
Recentresearchhasbeguntocombinereconstructionandcontrastivelearningtocreate
a comprehensive integrated anomaly score that can capture deviations from expected
patternsandeffectivelyidentifysubtleanomalies. SimAD[62]combinesasophisticated
featureextractoradeptathandlingextendedtimewindows,integratesnormalbehavior
patternscomprehensivelyusingtheEmbedPatchencoder,andintroducesaninnovative
ContrastFusion module aimed at highlighting distribution differences between normal
andabnormaldatatoenhancetherobustnessofAD.RESTAD[63]implementsaRadial
BasisFunction(RBF)neuronlayerintheTransformermodeltorepresentanon-parametric
densityinthelatentspace. AhighoutputfromtheRBFindicatessimilaritywithnormal
training data. Additionally, RESTAD merges RBF similarity scores with reconstruction
errorstoenhanceanomalydetectionsensitivity.
6.4. ProsandCons
Thissectiondescribestheadvantagesandlimitationsoftheaforementionedanomaly
detectionmodelsfortimeseriesdata. MLPMixer-basedmethodsfeatureasimplestructure
thatiseasytoimplementandcanbeadaptedtovariousdatacomplexitiesbyadjusting
thenumberoflayersandneurons[78]. AlthoughMLPcancapturenonlinearrelationships,
theymaynoteffectivelyhandleextremelycomplexdatadistributions. LLMs-basedmodels
havelearnedawealthofsemanticknowledgethroughpre-trainingonlargetextdatasets,
possessingstrongrepresentationalcapabilities. Theyareadaptabletoavarietyofdown-
streamtasksandcanalsoperformwellinfew-shotlearningscenarios,butdirectlyapplying
LLMsforTSADisnoteffective. Itrequiresthedesignofpromptingstrategiesandproper
fine-tuningtoenhancetheirabilitytodetectandinterpretanomalies[76]. Moreover,LLMs
maystrugglewithmorecomplex,context-relatedanomaliesandmayhallucinatewhen
indexingandexplaininganomalypoints.
7. Datasets
Thissectioncompilesandsummarizesavarietyofdatasetsandevaluationbenchmarks
forMTSAD,aimingtoprovidecomprehensiveresearchresourcesforresearchersinthis
field. Thesedatasetsincludebothgeneralandspecializedtimeseriesdatasetsthatcanbe
usedfortheevaluationofanomalydetectiontasks,withthelatterbeingapplicableunder
certainassumptionsorspecificcustomizations. Eachdatasetorbenchmarkisdescribed
indetailthroughmultipledimensionsandtheirinherentcharacteristics. InTable2,we
havecollectedandanalyzeddatasetsthatarewellknownorfrequentlycitedinthefieldof
MTSAD,whichhavebeentestedbyaseriesofdeeplearningmodels.
Applicationstypicallyproducedataviaasequenceofdatagenerationprocessesthat
mirrorsystemoperationsorofferinsightsintothebehaviorofvariousentities. Anomalies
frequentlyemergeasaconsequenceofirregularitiesinthesedatagenerationprocesses,
highlightingunusualaspectsofthesystemsandentitiesinvolved. Identifyingsuchatypical

Sensors2025,25,190
16of27
traitscanyieldvaluableinsightsacrossdiverseapplications. Thedeeplearningmodels
outlinedbelowarecategorizedbasedontheirrespectiveapplicationdomains.
Table2.Publicdataset/benchmarkusedmostlyforMTSAD.R/S:Thesourceofthedata,whether
itisrealworlddataorsyntheticdata. Samples: Individualdatapointsorobservationswithina
dataset. Entities: Independentobservationunitorobject,suchassensors,machines,devices,etc.
Dims:Thenumberoffeaturesorvariablesinthedata.Rate:Theproportionofanomaloussamples
withinthedataset.
| Datasets/Benchmark       | R/S Samples    | Entities Dims | Rate Domain                    |
| ------------------------ | -------------- | ------------- | ------------------------------ |
| MSL[25]                  | Real 132,046   | 27 55         | 10.48 Aerospace                |
| NASAShuttleValveData[81] | Real 49,097    | 1 9           | 7.0 Aerospace                  |
| IOnsphere[82]            | Real 351       | 33            | 36.0 Astronomy                 |
| SWAN-SF[83]              | Real 355,330   | 5 51          | 23.8 Astronomy                 |
| SMAP[25]                 | Real 562,800   | 55 25         | 12.83 Environmentalscience     |
| OPPORTUNITY[82]          | Real 36,224    | 24 133        | 3.4 Environmentalscience       |
| GECCO[84]                | Real 138,521   | 1 9           | 1.25 Internetofthings(IoT)     |
| CICIDS[85]               | Real 170,231   | 72            | 1.28 Internetofthings(IoT)     |
| Kitsune[82]              | Real 3,018,973 | 9 115         | 17.0 Cybersecurity             |
| Http(KDDCUP99)[86]       | Real 567,479   | 3             | 0.4 Cybersecurity              |
| Smtp(KDDCUP99)[86]       | Real 95,156    | 3             | 0.03 Cybersecurity             |
| NAB-realAdExchange[87]   | Real 9616      | 3 2           | Businessandfinance             |
| Creditcard[88]           | Real 284,807   | 1 29          | 0.17 Businessandfinance        |
| Genesis[89]              | Real 16,220    | 1 18          | 0.3 Industrialcontrolsystems   |
| GHL[90]                  | Synth 200,001  | 48 22         | 0.4 Industrialcontrolsystems   |
| SWaT[91,92]              | Real 946,719   | 1 51          | 11.98 Industrialcontrolsystems |
| WADI[93]                 | Real 957,372   | 1 123         | 5.99 Industrialcontrolsystems  |
| trimSyn[38]              | Synth 17,680   | 1 35          | 2.34 Industrialcontrolsystems  |
| MSDS[94]                 | Real 292,860   | 1 10          | 5.37 Industrialcontrolsystems  |
| Arrhythmia[95]           | Real 452       | 1 274         | 15.0 Healthcare                |
| MBA[96]                  | Real 200,000   | 8 2           | 0.14 Healthcare                |
| Thyroid[97]              | Real 3772      | 6             | 2.5 Healthcare                 |
| SVDB[98]                 | Real 230,400   | 78 2          | 13.6 Healthcare                |
| Daphnet[82,99]           | Real 32,594    | 35 3          | 13.2 Healthcare                |
| Callt2[82,100]           | Real 10,080    | 2 2           | 4.1 Infrastructure             |
| Metro[82]                | Real 48,204    | 1 5           | 0.1 Infrastructure             |
| NYC[101]                 | Real 17,520    | 3             | 0.57 Infrastructure            |
| Occupancy[82]            | Real 6208      | 2 8           | 28.7 Infrastructure            |
| Exathlon[102]            | Real 47,530    | 39 45         | 18.3 Servermonitoring          |
| MBD[103]                 | Real 8640      | 5 26          | Servermonitoring               |
| MMS[103]                 | Real 4370      | 50 7          | Servermonitoring               |
| PSM[104]                 | Real 132,480   | 1 25          | 27.76 Servermonitoring         |
| SMD[105]                 | Real 1,416,825 | 28 38         | 4.16 Servermonitoring          |
7.1. Astronomy
Inthefieldofastronomy,datasetstypicallyincludevariousobservationalandsim-
ulationdata,mainlyusedtostudyphenomenasuchastheuniverse,galaxies,stars,and
planets [106,107]. The Ionosphere dataset [82] comes from the UCI Machine Learning
Repositoryandisusedforabinaryclassificationtask,withthegoalofdeterminingwhether
thereareelectronspresentintheionospherebasedonreceivedsignals.Thedatasetincludes
individualfeatureinformationaswellasionospherethresholds.Itcontains351samplesand
33features,whereeachsamplerepresentsameasurementofaradarechosignal. Various
classificationalgorithmscanbeusedformodeltrainingandvalidationwhenworkingwith
theIonospheredataset. Thedatasethasahighfeaturedimension,whichmayleadtothe
“curseofdimensionality”duringmodeltraining. Additionally,handlingnoiseandoutliers
inthedatasetisanotherimportantchallenge. TheAERO[14]modelcandistinguishnormal
temporalpatternsfrompotentialanomaliesinastronomicalobservations,effectivelydiffer-
entiateconcurrentnoise,andreducethenumberoffalsealarms. SWAN-SF(SpaceWeather

Sensors2025,25,190 17of27
AnalyticsforSolarFlares)[83]isamultivariatetimeseriesbenchmarkdatasetdesigned
forthefieldofsolarphysics. Thedatasetcontains4075solaractiveregions,spanningthe
9-yearoperationalperiodoftheSolarDynamicsObservatory(SDO).Accuratepredictionof
solarflaresiscrucialforastronauts,spaceequipment,andsatellitecommunicationsystems.
7.2. Aerospace
Intheaerospacefield,MTSADdatasetsaretypicallyusedtomonitortheperformance
parametersandtelemetrydataofaircraft,satellites,spacecraft,andotherrelatedequipment.
Aerospace datasets are crucial for predicting equipment failures and ensuring mission
success. By conducting in-depth analysis of this time series data, anomaly detection
algorithms can be developed and tested to enhance the reliability and performance of
aerospace systems [108,109]. For instance, the NASA Shuttle Valve Data [81] includes
telemetrydatafromshuttlevalves,whichisusedtoanalyzethehealthconditionofthe
valvesandpredictpotentialmalfunctions. TheMSL(MarsScienceLaboratory)dataset[25],
collectedbyNASA,containstime-seriesdatafrom27channels,eachwith55dimensions.
Thedataisanonymized,standardizedtoarangeof0–1,andrecordedeveryminute. Except
for the telemetry values, which are continuous, most variables are binary (indicating
whethercommandsweresent). AnLSTM-basedmodelcanbeusedforanomalydetection
inthisdataset. Hundmanetal. [25]proposedtheLSTM-NDT,anunsupervisedmethod
forunivariatetimeseriesanomalydetection,whichservesasanon-parametricanomaly
thresholdmethodforNASAdatasets.
7.3. EnvironmentalScience
Datasetsinthefieldofenvironmentalscienceareprimarilyusedformonitoringand
managingnaturalresources,environmentalquality,andthehealthofecosystems[110,111].
For instance, the SMAP [25] provides measurements of soil moisture and temperature,
which are crucial for understanding the water cycle, crop health, and climate change.
By conducting in-depth analysis of this time series data, we can better understand the
dynamicsofenvironmentalsystemsandprovidedatasupportforsustainabledevelopment.
The OPPORTUNITY dataset [82] contains data from 23 body-worn sensors, 12 object-
placementsensors,and21environmentalsensors,usedtomeasurethedailyactivitiesof
foursubjects. TheOPPORTUNITYdatasetiswidelyusedinresearchinthefieldsofdeep
learningandartificialintelligence,particularlyinactivityrecognition,andhasbecomean
importantbenchmarkdataset. ItisoftenutilizedwithCNNsandLSTMscombinedwith
spatio-temporalfeatureextractiontocapturecomplexactivitypatterns.
7.4. InternetofThings(IoT)
In the field of IoT, time series anomaly detection datasets are primarily used for
monitoringandanalyzingdatastreamsgeneratedbyavastarrayofinterconnecteddevices
andsensors. Thisallowsforthetimelydetectionofequipmentfailures,networkanomalies,
orunexpectedbehaviors[112]. TheGECCOIoT[84]dataset,forinstance,containssensor
data from smart home or industrial IoT devices, which is utilized for detecting device
anomaliesandsystemmalfunctions. TheCICIDSdataset[85]containssamplesofvarious
networkattacksandnormaltraffic. Itincludesdatafromnormalactivitiesandsimulated
maliciousattackscollectedoverfivedays.ThedatawasgeneratedusingtheCICFlowMeter
toolandprovidesrichlabeleddata. DeeplearningbasedmodelsontheCICIDSdataset
havesignificantlyimprovedtheaccuracyofintrusiondetection. Researchershaveexplored
deeplearningmethods,suchasmultilayerperceptronsandconvolutionalneuralnetworks,
toenhancedetectionaccuracyandefficiency.
IntheIoT,millionsofconnecteddevicesandsmartsensorsgeneratehighlydynamic,
large-scale,heterogeneous,andtimestampeddata. Thistimestampeddataisatthecoreof

Sensors2025,25,190 18of27
IoTautomationandhasthepotentialtosignificantlyimpactindustrialprocesses. Effec-
tivelydetectinganomaliesintime-seriesdataandprovidingreal-timeactionableinsightsto
driveimprovementsinindustrialprocessespresentssignificantchallenges. Liuetal.[113]
proposedtheAMCNN-LSTMmodel,whichemphasizescommunicationefficiencyand
federatedlearning(FL)methodsondevices,enablingdistributededgedevicestocollabora-
tivelytrainananomalydetectionmodel. Toachievereal-timeanomalydetection,Nizam
etal.[114]proposedahybridend-to-enddeepanomalydetectionframeworkthatleverages
CNNandLSTMnetworkstodevelopanadvancedanomalydetectionsystem. Thesystem
architectureconsistsofthreelayers: sensorsandmachinesintheindustrialsetting,anedge
layerforreal-timedataprocessing,andacloudlayerforoffloadingprocessingtasks. The
frameworkisdesignedtoaccuratelydetectanomaliesandextremelyrareeventsinIoT
streamingdata.
7.5. BusinessandFinance
Inthebusinessandfinancesector,timeseriesdatasetsarecrucialforidentifyingand
preventingfraud,marketanomalies,creditrisks,andotherfinancialissues[3]. TheNAB-
realAdExchange dataset [87] is part of the Numenta Anomaly Benchmark (NAB). This
datasetrecordsonlineadvertisementclick-throughrates,withthemetricbeingcostper
click(CPC).Itcontainsonefilewithnoanomaliesandanotherfilewithanomalies,designed
toevaluatetheperformanceofanomalydetectionalgorithmsonreal-timestreamingdata.
TheCreditCarddataset[88]containsrecordsofcreditcardtransactions,primarilyusedfor
identifyinganddetectinganomaloustransactions,thatis,potentialfraudulentactivities.
Whendealingwithfinancialtimeseriesinvolvingvariousmarketriskfactors,amajor
issueisthepresenceofanomalies. Theseanomaliescanleadtocalibrationerrorsinmod-
elsusedforquantifyingandmanagingrisk,resultinginpotentialmisestimationsofrisk.
Crépeyetal. [115]proposedananomalydetectionmethodforfinancialtimeseriesthat
combinesPrincipalComponentAnalysis(PCA)andneuralnetworks. Byreducingdimen-
sionalitywithPCA,thisapproacheffectivelyextractskeyfeaturesfromhigh-dimensional
financialtimeseriesdata,simplifyingthesubsequentanomalydetectionprocess. Neural
networksarethenappliedtoidentifynonlinearrelationshipsandcomplexpatterns. To
detectanomaliesinmorepracticalbusinessscenariosintherealworld,contextualinfor-
mationisneededforaccurateprediction. Time-CAD[116]isacontext-awaredeeptime
seriesdecompositionframeworkthatusesdeeplearningtechniquestodecomposetime
seriesdataandincorporatescontextualinformationtoimprovetheaccuracyofanomaly
detection. Thismethodiscapableofeffectivelydetectinganomaliesinbusinessprocesses.
7.6. Cybersecurity
Inthefieldofcybersecurity,timeseriesanomalydetectiondatasetsareprimarilyused
formonitoringandanalyzingnetworktraffic,userbehavior,andsystemlogstopromptly
identifysecuritythreats,intrusionattempts,andabnormalactivities. TheKDDCUP99[86]
isaclassiccybersecuritydatasetwidelyusedforresearchinnetworkanomalydetection. It
containsvarioustypesofcyberattacks,suchasDoS(DenialofService),Probe,R2L(Remote
toLocal),U2R(UsertoRoot),aswellastrafficdatafromnormalbehavior. TheKitsune
dataset [82] is a dataset used for network intrusion detection, containing both normal
andanomalousnetworktrafficdata. Thisdatasetisusedtotrainandtestdeeplearning
models to differentiate between normal and malicious traffic. KitNET [117] is a deep
learningmodelthatusesasetofautoencodersforonlinenetworkintrusiondetection. This
unsupervisedmethodcanlearntodistinguishthecharacteristicsofnormalandanomalous
networktrafficwithouttheneedforexpert-labeledtrafficdata.

Sensors2025,25,190 19of27
7.7. IndustrialControlSystems
InthefieldofIndustrialControlSystems(ICS),timeseriesdatasetsarecommonlyused
formonitoringandanalyzingtheoperationalstatusofindustrialequipment.Thisfacilitates
thetimelydetectionofequipmentfailures,predictionofmaintenanceneeds,optimization
ofproductionprocesses,andensuringproductionsafety. TheWADI(WaterDistribution)
dataset[93],collectedandopen-sourcedbytheiTrustinstituteoftheSingaporeUniversity
ofTechnologyandDesign(SUTD),isusedtosimulatewatertreatmentanddistribution
networks.Thisdatasetincludessensordataandnetworkdata,coveringmultiplestages
ofthewatertreatmentprocess,suchasrawwaterintake,chemicaltreatment,filtration,
dechlorination, and reverse osmosis. The SWaT (Secure Water Treatment) [91] is also
providedbytheiTrustinstituteofSUTDandservesasatestplatformforresearchinthe
fieldofISCforwatertreatmentprocesses. TheSWaTdatasetcontainssensordatafrom
variousstagesofthewatertreatmentprocess.
IndustrialControlSystems(ICS)arewidelyusedandarecrucialtobothindustryand
society. Failuresinthesesystemscanhavesevereimpactsontheeconomyandhumanlife.
Asaresult,thesesystemshavebecomeattractivetargetsforbothphysicalandcyberattacks.
Kravchiketal. [118]proposedanefficientmethodfordetectingnetworkattacksinICS,
whichcombineslightweightneuralnetworkswithPrincipalComponentAnalysis(PCA).
This approach aims to reduce computational resource consumption while maintaining
highdetectionaccuracy,whichisparticularlyimportantinresource-constrainedICSen-
vironments. Anomaly detection is critical for preventing cybersecurity intrusions and
system attacks. Many AI-based anomaly detection methods have been proposed with
high detection performance, but they remain a “black box” that is difficult to interpret.
Hoangetal. [119]usedexplainableartificialintelligence(XAI)toenhancetheperspective
andreliabilityofanLSTM-basedAutoencoder-OCSVMlearningmodelforanomalyde-
tection in ICS. This model is capable of providing detailed information about detected
anomalies,helpingsecurityteamsmakeinformeddecisions.
7.8. Healthcare
Inthehealthcaredomain,timeseriesanomalydetectiondatasetsareprimarilyuti-
lizedformonitoringandanalyzinganindividual’sphysiologicalparameters. Thisallows
for the timely detection of health issues, abnormalities in diseases, or malfunctions in
medicalequipment. Forinstance,theMIT-BIHArrhythmiaDatabase(ECG)[95]contains
avastcollectionofelectrocardiogram(ECG)recordsthatareusedforthedetectionand
analysis of cardiac arrhythmias. The SVDB [98] offers a range of standard and variant
electrocardiogramrecordings,whichareemployedinresearchoncardiachealthandthe
detectionofarrhythmias. Thesedatasetsareinstrumentalinadvancingourunderstanding
ofheartconditionsandindevelopingmoreeffectivediagnosticandmonitoringtoolsfor
healthcareprofessionals.
Electrocardiogram (ECG) signals are commonly used to assess heart health. The
heart,beingacomplexorgan,canexhibitmanydifferenttypesofarrhythmias. Therefore,
applying anomaly detection methods to analyze ECG signals can be highly beneficial.
ANNet [120] utilizes LSTM networks and MLP to process ECG signals, and improves
theaccuracyofanomalydetectionbycombiningfeaturevectors. Thestudyalsoincludes
preprocessingstepsforECGsignals,suchasdenoisingwithDiscreteWaveletTransform
(DWT)andusinga60Hznotchfiltertoremovepowerlineinterference(PLI).Similarly,
Alamretal. [121]proposedanunsupervisedtransformer-basedanomalydetectionmethod.
Themodelarchitectureconsistsoftwoparts: atransformermodelforfeatureextraction
andaclassifierforanomalyscoring, whichisusedtoevaluateanddetectanomaliesin
ECGsignals.

Sensors2025,25,190 20of27
7.9. ServerMonitoring
Timeseriesanomalydetectiondatasetswithinthedomainofservermonitoringare
primarilyusedtomonitortheperformancemetricsofserversystemstopromptlyidentify
performancebottlenecks,systemfailures,orsecurityissues.Forinstance,SMDdataset[105]
gathersavarietyofserverperformanceindicators,suchasCPUusage,memoryconsump-
tion,diskI/O,etc.,foranomalydetectionandperformanceanalysis. Exathlondataset[102]
may collect performance data of servers under high load conditions to detect perfor-
manceanomalies.
Largecompaniesneedtomonitorvariousmetrics(suchaspageviewsandrevenue)of
theirapplicationsandservicesinrealtime. AtMicrosoft,atime-seriesanomalydetection
servicehasbeendevelopedtohelpcustomerscontinuouslymonitortime-seriesdataand
promptlyalertpotentialincidents. Denetal. [122]proposedanovelalgorithmbasedon
SpectralResidualandCNN,whichisthefirstattempttoapplytheSRmodel,originally
fromthevisualsaliencydetectiondomain,totime-seriesanomalydetection. Theapproach
aimstoprovideanaccurate,efficient,andgeneralsolution. Netzeretal. [123]proposeda
segment-basedtimeseriesanomalydetectionmethodformonitoringmachiningprocesses.
Thisapproachdetectsanomaliesbyusingsubprocess-specificthresholds,enablingmore
preciseidentificationandlocalizationofabnormalbehaviorsinthemachiningprocess.
7.10. Infrastructure
Securityisthefoundationofsustainableurbandevelopment.Theprocessofurbancon-
structionandoperationinvolvesalargeamountofmultidimensionaltime-seriesdata. By
detectinganomaliesinMTS,decisionsupportforurbanconstructionandoperationalrisk
warningcanbeprovided. Giventhecomplexityofurbaninfrastructure,thereisanurgent
needforfastandaccurateanomalydetection. Wuetal. [124]proposedareal-timeanomaly
detection algorithm based on an improved distance measure, called RADIM. RADIM
preservestherelationshipsbetweendimensionsinthemultidimensionalsubsequences
andusesanextendedFrobeniusnormwithlocalweightsandEuclideandistancebasedon
multidimensionaldatatomeasurethesimilarityofMTS.Inaddition,athresholdupdate
mechanismbasedonthefirst-ordermeandifference(TMFD)isdesignedtodetectreal-time
anomaliesbyassessingdeviations. Thismethodhasbeenappliedintunnelconstruction.
Atthesametime,mostcurrentmodelsstillfacechallengesinperceivinghigh-frequency
data,andthemostchallengingtaskisprocessinglargevolumesofdatainanextremely
short time. Liu et al. [125] proposed an anomaly detection method for high-frequency
sensordataintrafficinfrastructuremonitoringsystemsbasedonafine-tunedmodel. The
researchersdemonstratedthatconvertingdataintoimagescanimproveanomalydetection
speed,buttrainingdeeplearningmodelsisstilltime-consuming. Therefore,theydesigned
afour-stagemodelandcomparedtheproposedCNNwithfourwidelyusedfine-tuned
CNNsusingconfusionmatricestorapidlydetectanomaliesinhigh-frequencydata.
8. ConclusionsandFutureDirection
Thisarticleprovidesacomprehensivesurveyandreviewofmultivariatetimeseries
anomalydetection,exploringtypesofanomaliesanddeeparchitecturesforanomalydetec-
tion. Itanalyzesandorganizesdeeplearningmodelarchitecturesforanomalydetection
fromthreeperspectives,proposesanewclassificationofanomalydetectionstrategies,and
discusses46deeplearningmodelsindepth. Inaddition,itcompilespublicdatasetsfor
multivariatetimeseriesanomalydetection,alongwiththeirrespectiveapplicationdomains.
Toadvancethefield,thearticleconcludeswithadiscussionofpotentialdirectionsforfuture
researchexploration.

Sensors2025,25,190 21of27
Discrepancy: The contrastive learning has attracted considerable attention across
various domains, as it is capable of training models by contrasting positive pairs with
negativepairs. Recentresearchhasbeenfocusingonhighlightingdiscrepancies[59,62],
andfurtherexplorationinthisdirectionisexpected.
Integrationofdomainknowledge: Integratingexistingknowledgefromthestatistical
domain with deep learning can further enhance the model’s capability for time series
anomalydetection. FCVAE[126]selectsthemostusefulinformationfromthefrequency
domain to achieve better short-term trend construction. Future work could leverage
insightsfromthefrequencydomain,combinedwithdomainknowledge,tostrengthenthe
analysisoftimeseriesdata.
Benchmarking and evaluation metrics: The development and use of diverse pub-
lic datasets that simulate real-world anomaly situations, with clear subset divisions
for training and testing. At the same time, the design of intuitive, interpretable, and
parameter-adjustment-free evaluation metrics to adapt to different types of time series
anomalydetection.
LeveragingtechniquesfromLLMs: Recently,LLMshavegainedpopularityintime
seriesanalysis[127]. LLMsexhibitexceptionalgeneralizationcapabilities,demonstrating
robustpredictiveperformanceevenwithscarcedatasets. Thischaracteristicisparticularly
valuableinthecontextofMTSAD.Byleveragingmultimodalknowledge,suchasincorpo-
ratingadditionaltextualinformationtogeneratemultimodalembeddings,LLMseffectively
bridgethegapbetweennormalandanomalousdatainanomalydetection. Thismodeling
approach enriches the anomaly detection process by providing a more comprehensive
data representation, enabling the inclusion of diverse data sources and fostering more
detailedandcontext-awareanomalydetection. ExploringLLMsinMTSADisapromising
avenuethatcouldsignificantlyenhancetheaccuracyandefficiencyofdetectinganomalies
inmultivariatetimeseriesdata.
AuthorContributions: Writing—–originaldraftpreparation,F.W.;writing–—reviewandediting,
F.W.,Y.J.,R.Z.,A.W.andJ.X.;supervision,X.P.;ProjectAdministration,A.W.;FundingAcquisition,
J.X.Allauthorshavereadandagreedtothepublishedversionofthemanuscript.
Funding: Thisresearchwasfundedbythe2021KeyResearchPlatformsandProjectsofCollegesand
UniversitiesbytheDepartmentofEducationofGuangdongProvince:ResearchontheConstruction
ofKnowledgeGraphModelsforVocationalCollegeArchitecturalEducationSupportedbyArtificial
Intelligence(ProjectNo.:2021ZDZX1112).
InstitutionalReviewBoardStatement:Notapplicable.
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement:Thedatapresentedinthisstudyareavailableonthesourcementioned
inthetext.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.
References
1. Belay,M.A.;Blakseth,S.S.;Rasheed,A.;SalvoRossi,P.UnsupervisedAnomalyDetectionforIoT–BasedMultivariateTimeSeries:
ExistingSolutions,PerformanceAnalysisandFutureDirections.Sensors2023,23,2844.[CrossRef]
2. Correia,L.;Goos,J.C.;Klein,P.;Bäck,T.;Kononova,A.V.Onlinemodel–basedanomalydetectioninmultivariatetimeseries:
Taxonomy,survey,researchchallengesandfuturedirections.Eng.Appl.Artif.Intell.2024,138,109323.[CrossRef]
3. Hilal,W.;Gadsden,S.A.;Yawney,J.Financialfraud:Areviewofanomalydetectiontechniquesandrecentadvances.ExpertSyst.
Appl. 2022,193,116429.[CrossRef]
4. Cook,A.A.;Misirli,G.;Fan,Z.AnomalyDetectionforIoTTime–SeriesData:ASurvey.IEEEInternetThingsJ.2020,7,6481–6494.
[CrossRef]

Sensors2025,25,190 22of27
5. Angiulli,F.;Pizzuti,C.Fastoutlierdetectioninhighdimensionalspaces. InProceedingsofthe6thEuropeanConferenceon
PrinciplesofDataMiningandKnowledgeDiscovery,Berlin/Heidelberg,Germany,19–23August2002;pp.15–27.
6. Schölkopf,B.;Platt,J.C.;Shawe–Taylor,J.Estimatingthesupportofahigh–dimensionaldistribution.NeuralComput.2001,13,
1443–1471.[CrossRef][PubMed]
7. Breunig,M.M.;Kriegel,H.P.;Ng,R.T.;Sander,J.LOF:Identifyingdensity–basedlocaloutliers.InProceedingsofthe2000ACM
SIGMODInternationalConferenceonManagementofData,Dallas,TX,USA,15–18May2000;pp.93–104.
8. Nelson,B.K.Timeseriesanalysisusingautoregressiveintegratedmovingaverage(ARIMA)models.Acad.Emerg.Med.1998,5,
739–744.[CrossRef][PubMed]
9. Ma,J.;Perkins,S.Time–seriesnoveltydetectionusingone–classsupportvectormachines.InProceedingsoftheInternational
JointConferenceonNeuralNetworks,Portland,OR,USA,20–24July2003;Volume3,pp.1741–1745.
10. Tax,D.M.J.;Duin,R.P.W.Supportvectordatadescription.Mach.Learn.2004,54,45–66.[CrossRef]
11. Munir, M.; Chattha, M.A.; Dengel, A.; Ahmed, S.Acomparativeanalysisoftraditionalanddeeplearning–basedanomaly
detectionmethodsforstreamingdata. InProceedingsofthe18thIEEEInternationalConferenceonMachineLearningand
Applications(ICMLA),BocaRaton,FL,USA,16–19December2019;pp.561–566.
12. Vaswani,A.Attentionisallyouneed.InProceedingsofthe31stInternationalConferenceonNeuralInformationProcessing
Systems,LongBeach,CA,USA,4–9December2017.
13. Yang,Y.;Zhang,C.;Zhou,T.;Wen,Q.;Sun,L.Dcdetector: Dualattentioncontrastiverepresentationlearningfortimeseries
anomalydetection.InProceedingsofthe29thACMSIGKDDConferenceonKnowledgeDiscoveryandDataMining,LongBeach,
CA,USA,6–10August2023;pp.3033–3045.
14. Hao, X.; Chen, Y.; Yang, C.; Du, Z.; Ma, C.; Wu, C.; Meng, X. From Chaos to Clarity: Time Series Anomaly Detection in
AstronomicalObservations.arXiv2024,arXiv:2403.10220.
15. Huang,X.;Chen,N.;Deng,Z.;Huang,S.Multivariatetimeseriesanomalydetectionviadynamicgraphattentionnetworkand
Informer.Appl.Intell.2024,54,7636–7658.[CrossRef]
16. Chen,F.;Qin,Z.;Zhou,M.;Zhang,Y.;Deng,S.;Fan,L.;Wen,Q.LARA:ALightandAnti–overfittingRetrainingApproachfor
UnsupervisedTimeSeriesAnomalyDetection.InProceedingsoftheACMonWebConference2024,Singapore,13–17May2024;
pp.4138–4149.
17. Prabhu,H.;Valadi,J.;Arjunan,P.GenerativeAdversarialNetworkwithSoft–DynamicTimeWarpingandParallelReconstruction
forEnergyTimeSeriesAnomalyDetection.arXiv2024,arXiv:2402.14384.
18. Wang,C.;Zhuang,Z.;Qi,Q.;Wang,J.;Wang,X.;Sun,H.;Liao,J.Driftdoesn’tmatter:Dynamicdecompositionwithdiffusion
reconstructionforunstablemultivariatetimeseriesanomalydetection.InProceedingsofthe37thInternationalConferenceon
NeuralInformationProcessingSystems,NewOrleans,LA,USA,10–16December2023;pp.10758–10774.
19. Pang,G.;Shen,C.;Cao,L.;Hengel,A.V.D.Deeplearningforanomalydetection:Areview.ACMComput.Surv. 2021,54,1–38.
[CrossRef]
20. Ma, S.; Guan, S.; He, Z.; Nie, J.; Gao, M. TPAD: Temporal pattern based neural network model for anomaly detection in
multivariatetimeseries.IEEESens.J.2023,23,30668–30682.[CrossRef]
21. ZamanzadehDarban,Z.;Webb,G.I.;Pan,S.;Aggarwal,C.;Salehi,M.Deeplearningfortimeseriesanomalydetection:Asurvey.
ACMComput.Surv. 2024,57,1–42.[CrossRef]
22. Munir,M.;Siddiqui,S.A.;Dengel,A.;Ahmed,S.DeepAnT:Adeeplearningapproachforunsupervisedanomalydetectionin
timeseries.IEEEAccess2018,7,1991–2005.[CrossRef]
23. He,Y.;Zhao,J.Temporalconvolutionalnetworksforanomalydetectionintimeseries. J.Phys. Conf. Ser. 2019,1213,042050.
[CrossRef]
24. Wu,H.;Hu,T.;Liu,Y.;Zhou,H.;Wang,J.;Long,M.Timesnet:Temporal2d–variationmodelingforgeneraltimeseriesanalysis.
InProceedingsoftheEleventhInternationalConferenceonLearningRepresentations,Kigali,Rwanda,1–5May2023.
25. Hundman, K.; Constantinou, V.; Laporte, C.; Colwell, I.; Soderstrom, T. Detecting spacecraft anomalies using lstms and
nonparametric dynamic thresholding. In Proceedings of the 24th ACM SIGKDD International Conference on Knowledge
DiscoveryandDataMining,KDD’18,London,UK,19–23August2018;pp.387–395.
26. Ding,N.;Ma,H.;Gao,H.;Ma,Y.;Tan,G.Real–timeanomalydetectionbasedonlongshort–TermmemoryandGaussianMixture
Model.Comput.Electr.Eng.2019,79,106458.[CrossRef]
27. Shen,L.;Li,Z.;Kwok,J.Timeseriesanomalydetectionusingtemporalhierarchicalone–classnetwork.InProceedingsofthe34th
InternationalConferenceonNeuralInformationProcessingSystems,Vancouver,BC,Canada,6–12December2020;Volume33,
pp.13016–13026.
28. Wu,W.;He,L.;Lin,W.;Su,Y.;Cui,Y.;Maple,C.;Jarvis,S.Developinganunsupervisedreal–timeanomalydetectionschemefor
timeserieswithmulti–seasonality.IEEETrans.Knowl.DataEng.2020,34,4147–4160.[CrossRef]

Sensors2025,25,190 23of27
29. Zhao,H.;Wang,Y.;Duan,J.;Huang,C.;Cao,D.;Tong,Y.;Xu,B.;Bai,J.;Tong,J.;Zhang,Q.Multivariatetime–seriesanomaly
detectionviagraphattentionnetwork.InProceedingsoftheIEEEInternationalConferenceonDataMining,ICDM,Sorrento,
Italy,17–20November2020;pp.841–850.
30. Deng,A.;Hooi,B.GraphNeuralNetwork–BasedAnomalyDetectioninMultivariateTimeSeries.Proc.AAAIConf.Artif.Intell.
2021,35,4027–4035.[CrossRef]
31. Chen,W.;Tian,L.;Chen,B.;Dai,L.;Duan,Z.;Zhou,M.Deepvariationalgraphconvolutionalrecurrentnetworkformultivariate
timeseriesanomalydetection.InProceedingsofthe39thInternationalConferenceonMachineLearning,Baltimore,MD,USA,
17–23July2022;pp.3621–3633.
32. Han,S.;Woo,S.S.Learningsparselatentgraphrepresentationsforanomalydetectioninmultivariatetimeseries.InProceedings
ofthe28thACMSIGKDDConferenceonKnowledgeDiscoveryandDataMining,Washington,DC,USA,14–18August2022;
pp.2977–2986.
33. Chen, K.; Feng, M.; Wirjanto, T.S. Multivariate time series anomaly detection via dynamic graph forecasting. arXiv 2023,
arXiv:2302.02051.
34. Fu, Y.; Xue, F. Mad: Self–supervised masked anomaly detection task for multivariate time series. In Proceedings of the
InternationalJointConferenceonNeuralNetworks,IJCNN,Padua,Italy,18–23July2022;pp.1–8.
35. Wu,Y.;Dong,Y.;Zhu,W.;Zhang,J.;Liu,S.;Lu,D.;Li,Y.CLformer:Constraint–basedLocalityenhancedTransformerforanomaly
detectionofancientbuildingstructures.Eng.Appl.Artif.Intell.2023,126,107072.[CrossRef]
36. Jeong,Y.;Yang,E.;Ryu,J.H.;Park,I.;Kang,M.Anomalybert: Self–supervisedtransformerfortimeseriesanomalydetection
usingdatadegradationscheme.arXiv2023,arXiv:2305.04468.
37. Zong,B.;Song,Q.;RenqiangMin,M.;Cheng,W.;Lumezanu,C.;Cho,D.;Chen,H.Deepautoencodinggaussianmixturemodel
forunsupervisedanomalydetection.InProceedingsoftheInternationalConferenceonLearningRepresentations,Vancouver,
BC,Canada,30April–3May2018.
38. Zhang,C.;Song,D.;Chen,Y.;Feng,X.;Lumezanu,C.;Cheng,W.;Chawla,N.V.Adeepneuralnetworkforunsupervisedanomaly
detectionanddiagnosisinmultivariatetimeseriesdata. InProceedingsoftheAAAIConferenceonArtificialIntelligence,
Honolulu,HI,USA,27January–1February2019;Volume33,pp.1409–1416.
39. Audibert,J.;Michiardi,P.;Guyard,F.;Marti,S.;Zuluaga,M.A.Usad: Unsupervisedanomalydetectiononmultivariatetime
series.InProceedingsofthe26thACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining,Virtual
Event,CA,USA,23–27August2020;pp.3395–3404.
40. Lai, C.Y.A.; Sun, F.K.; Gao, Z.; Lang, J.H.; Boning, D. Nominality score conditioned time series anomaly detection by
point/sequentialreconstruction.InProceedingsofthe37thConferenceonNeuralInformationProcessingSystems,NewOrleans,
LA,USA,10–16December2023;pp.76637–76655.
41. Park,D.;Hoshi,Y.;Kemp,C.C.Amultimodalanomalydetectorforrobot–assistedfeedingusinganlstm–basedvariational
autoencoder.IEEERobot.Autom.Lett.2018,3,1544–1551.[CrossRef]
42. Su, Y.; Zhao, Y.; Niu, C.; Liu, R.; Sun, W.; Pei, D.Robustanomalydetectionformultivariatetimeseriesthroughstochastic
recurrentneuralnetwork.InProceedingsofthe25thACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandData
Mining,Anchorage,AK,USA,4–8August2019;pp.2828–2837.
43. Li,Z.;Zhao,Y.;Han,J.;Su,Y.;Jiao,R.;Wen,X.;Pei,D.Multivariatetimeseriesanomalydetectionandinterpretationusing
hierarchicalinter–metricandtemporalembedding.InProceedingsoftheACMSIGKDDInternationalConferenceonKnowledge
DiscoveryandDataMining,VirtualEvent,Singapore,14–18August2021;pp.3220–3230.
44. Huang,T.;Chen,P.;Li,R.Asemi–supervisedvaebasedactiveanomalydetectionframeworkinmultivariatetimeseriesforonline
systems.InProceedingsoftheACMWebConference,WWW’22,VirtualEvent,Lyon,France,25–29April2022;pp.1797–1806.
45. Li,D.;Chen,D.;Jin,B.;Shi,L.;Goh,J.;Ng,S.K.MAD–GAN:Multivariateanomalydetectionfortimeseriesdatawithgenerative
adversarialnetworks.Int.Conf.Artif.NeuralNetw.2019,11730,703–716.
46. Geiger,A.;Liu,D.;Alnegheimish,S.;Cuesta–Infante,A.;Veeramachaneni,K.Tadgan: Timeseriesanomalydetectionusing
generativeadversarialnetworks. InProceedingsoftheIEEEInternationalConferenceonDataMining, Atlanta, GA,USA,
10–13December2020;pp.33–43.
47. Lu, S.; Dong, Z.; Cai, D.; Fang, F.; Zhao, D. MIM–GAN–based Anomaly Detection for Multivariate Time Series Data. In
ProceedingsoftheIEEEVehicularTechnologyConference(VTC2023–Fall),HongKong,China,10–13October2023;pp.1–7.
48. Chen,X.;Deng,L.;Zhao,Y.;Zheng,K.Adversarialautoencoderforunsupervisedtimeseriesanomalydetectionandinterpretation.
InProceedingsofthe16thACMInternationalConferenceonWebSearchandDataMining,Singapore,27February–3March2023;
pp.267–275.
49. Pintilie,I.;Manolache,A.;Brad,F.Timeseriesanomalydetectionusingdiffusion–basedmodels. InProceedingsoftheIEEE
InternationalConferenceonDataMining,Shanghai,China,1–4December2023;pp.570–578.

Sensors2025,25,190 24of27
50. Zhang,H.; Xia,Y.; Yan,T.; Liu,G.Unsupervisedanomalydetectioninmultivariatetimeseriesthroughtransformer–based
variational autoencoder. In Proceedings of the 33rd Chinese Control and Decision Conference (CCDC), Kunming, China,
22–24May2021;pp.281–286.
51. Xu,J.Anomalytransformer:Timeseriesanomalydetectionwithassociationdiscrepancy.InProceedingsoftheInternational
ConferenceonLearningRepresentations,VirtualEvent,25–29April2022.
52. Tuli,S.;Casale,G.;Jennings,N.R.Tranad:Deeptransformernetworksforanomalydetectioninmultivariatetimeseriesdata.
Proc.VLDBEndow.2022,15,1201–1214.[CrossRef]
53. Song, J.; Kim, K.; Oh, J.; Cho, S. Memto: Memory–guided transformer for multivariate time series anomaly detection.
In Proceedings of the 37th International Conference on Neural Information Processing Systems, New Orleans, LA, USA,
10–16December2023;Volume36,pp.57947–57963.
54. Nam,Y.; Yoon,S.; Shin,Y.; Bae,M.; Song,H.; Lee,J.G.; Lee,B.S.BreakingtheTime–FrequencyGranularityDiscrepancyin
Time–SeriesAnomalyDetection.InProceedingsoftheACMonWebConference2024,WWW’24,Singapore,13–17May2024;
pp.4204–4215.
55. Wu,X.;Qiu,X.;Li,Z.;Wang,Y.;Hu,J.;Guo,C.;Yang,B.CATCH:Channel–AwareMultivariateTimeSeriesAnomalyDetection
viaFrequencyPatching.arXiv2024,arXiv:2410.12261.
56. Liu,S.;Yao,D.;Fang,L.;Li,Z.;Li,W.;Feng,K.;Bi,J.AnomalyLLM:Few–ShotAnomalyEdgeDetectionforDynamicGraphs
usingLargeLanguageModels.arXiv2024,arXiv:2405.07626.
57. Bian,Y.;Ju,X.;Li,J.;Xu,Z.;Cheng,D.;Xu,Q.Multi–patchprediction: Adaptingllmsfortimeseriesrepresentationlearning.
In Proceedings of the 41st International Conference on Machine Learning, Vienna, Austria, 21–27 July 2024; Volume 235,
pp.3889–3912.
58. Liu,C.;He,S.;Zhou,Q.;Li,S.;Meng,W.Largelanguagemodelguidedknowledgedistillationfortimeseriesanomalydetection.
InProceedingsoftheThirty–ThirdInternationalJointConferenceonArtificialIntelligence(IJCAI–24),Jeju,RepublicofKorea,
3–9August2024;pp.2162–2170.
59. Zhong,Z.;Yu,Z.;Yang,Y.;Wang,W.;Yang,K.PatchAD:Patch–BasedMLP–MixerforTimeSeriesAnomalyDetection.arXiv
2024,arXiv:2401.09793.
60. Pranavan,T.;Sim,T.;Ambikapathi,A.;Ramasamy,S.Contrastivepredictivecodingforanomalydetectioninmulti–variatetime
seriesdata.arXiv2022,arXiv:2202.03639.
61. Najari,N.;Berlemont,S.;Lefebvre,G.;Duffner,S.;Garcia,C.RESIST:Robusttransformerforunsupervisedtimeseriesanomaly
detection.InProceedingsoftheAdvancedAnalyticsandLearningonTemporalData:7thECMLPKDDWorkshop,Grenoble,
France,19–23September2022;pp.66–82.
62. Zhong,Z.;Yu,Z.;Xi,X.;Xu,Y.;Chen,J.;Yang,K.SimAD:ASimpleDissimilarity–BasedApproachforTimeSeriesAnomaly
Detection.arXiv2024,arXiv:2405.11238.
63. Ghorbani,R.;Reinders,M.J.;Tax,D.M.RESTAD:REconstructionandSimilaritybasedTransformerfortimeseriesAnomaly
Detection.arXiv2024,arXiv:2405.07509.
64. Hochreiter,S.;Schmidhuber,J.LongShort–TermMemory.NeuralComput.1997,9,1735–1780.[CrossRef][PubMed]
65. Reynolds,D.A.Gaussianmixturemodels.Encycl.Biom. 2009,741,659–663.
66. Orhan,A.E.;Pitkow,X.Skipconnectionseliminatesingularities.arXiv2017,arXiv:1701.09175.
67. Velickovic,P.;Cucurull,G.;Casanova,A.;Romero,A.;Lio,P.;Bengio,Y.Graphattentionnetworks.arXiv2017, arXiv:1710.10903.
68. Bank,D.;Koenigstein,N.;Giryes,R.Autoencoders.InMachineLearningforDataScienceHandbook:DataMiningandKnowledge
DiscoveryHandbook;Springer:Cham,Switzerland,2023;pp.353–374.
69. Doersch,C.Tutorialonvariationalautoencoders.arXiv2016,arXiv:1606.05908.
70. Goodfellow,I.;Pouget–Abadie,J.;Mirza,M.;Xu,B.;Warde–Farley,D.;Ozair,S.;Bengio,Y.Generativeadversarialnetworks.
Commun.ACM2020,63,139–144.[CrossRef]
71. Frogner, C.; Zhang, C.; Mobahi, H.; Araya, M.; Poggio, T.A. Learning with a Wasserstein loss. In Proceedings of the 28th
InternationalConferenceonNeuralInformationProcessingSystems,Montreal,QC,Canada,7–12December2015;Volume2,
pp.2053–2061.
72. Dwibedi,D.;Aytar,Y.;Tompson,J.;Sermanet,P.;Zisserman,A.Temporalcycle–consistencylearning. InProceedingsofthe
IEEE/CVFConferenceonConferenceonComputerVisionandPatternRecognition(CVPR),LongBeach,CA,USA,15–20June
2019;pp.1801–1810.
73. Cuturi, M.; Blondel, M. Soft–dtw: A differentiable loss function for time–series. In Proceedings of the 34th International
ConferenceonMachineLearning,Sydney,Australia,6–11August2017;pp.894–903.
74. MacKay,D.J.IntroductiontoGaussianprocesses.NATOASISer.FComput.Syst.Sci. 1998,168,133–166.

Sensors2025,25,190 25of27
75. Yoon,J.;Zame,W.R.;vanderSchaar,M.Estimatingmissingdataintemporaldatastreamsusingmulti–directionalrecurrent
neuralnetworks.IEEETrans.Biomed.Eng.2018,66,1477–1490.[CrossRef]
76. Dong,M.;Huang,H.;Cao,L.CanLLMsServeAsTimeSeriesAnomalyDetectors?arXiv2024,arXiv:2408.03475.
77. Alnegheimish,S.;Nguyen,L.;Berti–Equille,L.;Veeramachaneni,K.Largelanguagemodelscanbezero–shotanomalydetectors
fortimeseries?arXiv2024,arXiv:2405.14755.
78. Zhong,S.;Song,S.;Zhuo,W.;Li,G.;Liu,Y.;Chan,S.H.G.Amulti–scaledecompositionmlp–mixerfortimeseriesanalysis.arXiv
2023,arXiv:2310.11959.[CrossRef]
79. Gong, Z.; Tang, Y.; Liang, J. Patchmixer: A patch–mixing architecture for long–term time series forecasting. arXiv 2023,
arXiv:2310.00655.
80. Ekambaram,V.;Jati,A.;Nguyen,N.;Sinthong,P.;Kalagnanam,J.Tsmixer:Lightweightmlp–mixermodelformultivariatetime
seriesforecasting.InProceedingsofthe29thACMSIGKDDConferenceonKnowledgeDiscoveryandDataMining,LongBeach,
CA,USA,6–10August2023;pp.459–469.
81. Ferrell,B.;Santuro,S.NASAShuttleValveData;FloridaTech:Melbourne,FL,USA,2005.
82. Asuncion,A.;Newman,D.UCIMachineLearningRepository.2007.Availableonline:https://ergodicity.net/2013/07/(accessed
on8November2024).
83. Angryk,R.A.;Martens,P.C.;Aydin,B.;Kempton,D.;Mahajan,S.S.;Basodi,S.;Georgoulis,M.K.Multivariatetimeseriesdataset
forspaceweatherdataanalytics.Sci.Data2020,7,227.[CrossRef]
84. Moritz,S.;Rehbach,F.;Chandrasekaran,S.;Rebolledo,M.;Bartz–Beielstein,T.GECCOIndustrialChallenge2018Dataset:Awater
qualitydatasetforthe‘InternetofThings:OnlineAnomalyDetectionforDrinkingWaterQuality’Competition.InProceedingsof
theGeneticandEvolutionaryComputationConference,Kyoto,Japan,15–19July2018.
85. Poorebrahimi,A.CICIDS2017.J.Adv.SignalProcess.2021,5,105–115.
86. KDDCup.TheThirdInternationalKnowledgeDiscoveryandDataMiningToolsCompetitionDatasetKDDCup1999Data.1999.
Availableonline:https://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html(accessedon24December2024).
87. Ahmad,S.;Lavin,A.;Purdy,S.;Agha,Z.Unsupervisedreal–timeanomalydetectionforstreamingdata.Neurocomputing2017,
262,134–147.[CrossRef]
88. DalPozzolo,A.;Caelen,O.;Johnson,R.A.;Bontempi,G.Calibratingprobabilitywithundersamplingforunbalancedclassification.
InProceedingsoftheIEEESymposiumSeriesonComputationalIntelligence,CapeTown,SouthAfrica,7–10December2015;
pp.159–166.
89. vonBirgelen,A.;Niggemann,O.Anomalydetectionandlocalizationforcyber–physicalproductionsystemswithself–organizing
maps.Improve2018,8,55–71.
90. Filonov,P.;Lavrentyev,A.;Vorontsov,A.Multivariateindustrialtimeserieswithcyber–attacksimulation:Faultdetectionusing
anlstm–basedpredictivedatamodel.arXiv2016, arXiv:1612.06676.
91. Aditya,P.M.;Nils,O.T.SWaT:AwatertreatmenttestbedforresearchandtrainingonICSsecurity.InProceedingsofthe2016
InternationalWorkshoponCyber–PhysicalSystemsforSmartWaterNetworks(CySWater),Vienna,Austria,11April2016;
pp.31–36.
92. Goh,J.;Adepu,S.;Junejo,K.N.;Mathur,A.Adatasettosupportresearchinthedesignofsecurewatertreatmentsystems.Crit.
Inf.Infrastruct.Secur.2017,10242,88–99.
93. Ahmed,C.M.;Palleti,V.R.;Mathur,A.P.WADI:Awaterdistributiontestbedforresearchinthedesignofsecurecyberphysical
systems.InProceedingsofthe3rdInternationalWorkshoponCyber–PhysicalSystemsforSmartWaterNetworks,Pittsburgh,
PA,USA,21April2017;pp.25–28.
94. Nedelkoski, S.; Bogatinovski, J.; Mandapati, A.K.; Becker, S.; Cardoso, J.; Kao, O.Multi–sourcedistributedsystemdatafor
ai–poweredanalytics.InProceedingsoftheService–OrientedandCloudComputing:8thIFIPWG2.14EuropeanConference,
ESOCC2020,Heraklion,Greece,28–30September2020;pp.161–176.
95. Moody,G.B.;Mark,R.G.TheimpactoftheMIT–BIHarrhythmiadatabase.IEEEEng.Med.Biol.Mag.2001,20,45–50.[CrossRef]
96. Goldberger,A.L.;Amaral,L.A.N.;Glass,L.;Hausdorff,J.M.;Ivanov,P.C.;Mark,R.G.;PhysioBank,P.PhysioNet:Componentsof
aNewResearchResourceforComplexPhysiologicSignals.Circulation2000,101,215–220.[CrossRef]
97. Vanderpump,M.P.Theepidemiologyofthyroiddisease.Br.Med.Bull.2011,99,39–51.[CrossRef]
98. Greenwald,S.D.;Patil,R.S.;Mark,R.G.Improveddetectionandclassificationofarrhythmiasinnoise–corruptedelectrocardiograms
usingcontextualinformation.InProceedingsoftheComputersinCardiology,Chicago,IL,USA,23–26September1990;pp.461–464.
99. Bachlin,M.;Plotnik,M.;Roggen,D.;Maidan,I.;Hausdorff,J.M.;Giladi,N.;Troster,G.WearableassistantforParkinson’sdisease
patientswiththefreezingofgaitsymptom.IEEETrans.Inf.Technol.Biomed.2009,14,436–446.[CrossRef]
100. Ihler,A.;Hutchins,J.;Smyth,P.Adaptiveeventdetectionwithtime–varyingpoissonprocesses. InProceedingsofthe12thACM
SIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining,Philadelphia,PA,USA,20–23August2006;pp.207–216.

Sensors2025,25,190 26of27
101. Daus,M.W.Taxis.InTheRoutledgeHandbookofPublicTransport;Routledge:London,UK,2021;pp.252–269.
102. Jacob,V.;Song,F.;Stiegler,A.;Rad,B.;Diao,Y.;Tatbul,N.Exathlon:Abenchmarkforexplainableanomalydetectionovertime
series.arXiv2020,arXiv:2010.05073.[CrossRef]
103. He,Z.;Chen,P.;Li,X.;Wang,Y.;Yu,G.;Chen,C.;Zheng,Z.Aspatiotemporaldeeplearningapproachforunsupervisedanomaly
detectionincloudsystems.IEEETrans.NeuralNetw.Learn.Syst.2020,34,1705–1719.[CrossRef]
104. Abdulaal, A.; Liu, Z.; Lancewicki, T. Practical approach to asynchronous multivariate time series anomaly detection and
localization.InProceedingsofthe27thACMSIGKDDConferenceonKnowledgeDiscoveryandDataMining,VirtualEvent,
Singapore,14–18August2021;pp.2485–2494.
105. Li,Z.;Chen,W.;Pei,D.RobustandunsupervisedKPIanomalydetectionbasedonconditionalvariationalautoencoder. In
Proceedingsofthe2018IEEE37thInternationalPerformanceComputingandCommunicationsConference(IPCCC),Orlando,
FL,USA,17–19November2018;pp.1–9.
106. Muthukrishna,D.;Gupta,R.AClassifier–BasedApproachtoMulti–ClassAnomalyDetectionAppliedtoAstronomicalTime–
Series.arXiv2024,arXiv:2408.08888.
107. Scargle,J.D.Studiesinastronomicaltimeseriesanalysis.Astrophys.J.1982,263,835–853.[CrossRef]
108. Baireddy, S.; Desai, S.R.; Mathieson, J.L.; Foster, R.H.; Chan, M.W.; Comer, M.L.; Delp, E.J.Spacecrafttime–seriesanomaly
detectionusingtransferlearning. InProceedingsoftheIEEE/CVFConferenceonComputerVisionandPatternRecognition
(CVPR),Nashville,TN,USA,20–25June2021;pp.1951–1960.
109. El–Shafeiy,E.;Alsabaan,M.;Ibrahem,M.I.;Elwahsh,H.Real–timeanomalydetectionforwaterqualitysensormonitoringbased
onmultivariatedeeplearningtechnique.Sensors2023,23,8613.[CrossRef][PubMed]
110. Chevrot, A.; Vernotte, A.; Legeard, B.CAE:Contextualauto–encoderformultivariatetime–seriesanomalydetectioninair
transportation.Comput.Secur. 2022,116,102652.[CrossRef]
111. Rollo, F.; Bachechi, C.; Po, L.Anomalydetectionandrepairingforimprovingairqualitymonitoring. Sensors2023, 23, 640.
[CrossRef]
112. Sgueglia, A.; DiSorbo, A.; Visaggio, C.A.; Canfora, G.AsystematicliteraturereviewofIoTtimeseriesanomalydetection
solutions.FutureGener.Comput.Syst.2022,134,170–186.[CrossRef]
113. Liu,Y.;Garg,S.;Nie,J.;Zhang,Y.;Xiong,Z.;Kang,J.;Hossain,M.S.Deepanomalydetectionfortime–seriesdatainindustrialIoT:
Acommunication–efficienton–devicefederatedlearningapproach.IEEEInternetThingsJ.2020,8,6348–6358.[CrossRef]
114. Nizam,H.;Zafar,S.;Lv,Z.;Wang,F.;Hu,X.Real–timedeepanomalydetectionframeworkformultivariatetime–seriesdatain
industrialiot.IEEESens.J.2022,22,22836–22849.[CrossRef]
115. Crépey,S.;Lehdili,N.;Madhar,N.;Thomas,M.Anomalydetectioninfinancialtimeseriesbyprincipalcomponentanalysisand
neuralnetworks.Algorithms2022,15,385.[CrossRef]
116. Nam,Y.;Trirat,P.;Kim,T.;Lee,Y.;Lee,J.G.Context–awaredeeptime–seriesdecompositionforanomalydetectioninbusinesses.
InProceedingsoftheJointEuropeanConferenceonMachineLearningandKnowledgeDiscoveryinDatabases,Turin,Italy,
18–22September2023;pp.330–345.
117. Zelichenok,I.;Kotenko,I.KitsuneDatasetAnalysisviaBigDataandDeepLearningTechniques.InProceedingsofthe2024IEEE
Ural–SiberianConferenceonBiomedicalEngineering,RadioelectronicsandInformationTechnology(USBEREIT),Yekaterinburg,
Russia,13–15May2024;pp.152–155.
118. Kravchik,M.;Shabtai,A.Efficientcyberattackdetectioninindustrialcontrolsystemsusinglightweightneuralnetworksandpca.
IEEETrans.DependableSecur.Comput.2021,19,2179–2197.[CrossRef]
119. Hoang, N.X.; Hoang, N.V.; Du, N.H.; Huong, T.T.; Tran, K.P. Explainable anomaly detection for industrial control system
cybersecurity.IFAC–PapersOnLine2022,55,1183–1188.
120. Sivapalan,G.;Nundy,K.K.;Dev,S.;Cardiff,B.;John,D.ANNet:AlightweightneuralnetworkforECGanomalydetectioninIoT
edgesensors.IEEETrans.Biomed.CircuitsSyst.2022,16,24–35.[CrossRef]
121. Alamr,A.;Artoli,A.Unsupervisedtransformer–basedanomalydetectioninECGsignals.Algorithms2023,16,152.[CrossRef]
122. Ren, H.; Xu, B.; Wang, Y.; Yi, C.; Huang, C.; Kou, X.; Zhang, Q. Time–series anomaly detection service at microsoft. In
Proceedingsofthe25thACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining,Anchorage,AK,
USA,4–8August2019;pp.3009–3017.
123. Netzer, M.; Palenga, Y.; Fleischer, J. Machine tool process monitoring by segmented timeseries anomaly detection using
subprocess–specificthresholds.Prod.Eng. 2022,16,597–606.[CrossRef]
124. Wu,B.;Zhang,F.;Wang,Y.;Hu,M.;Bai,X.AnomalyDetectionAlgorithmforUrbanInfrastructureConstructionEquipment
BasedonMultidimensionalTimeSeries.Sustainability2024,16,3335.[CrossRef]
125. Liu,H.;Li,L.Anomalydetectionofhigh–frequencysensingdataintransportationinfrastructuremonitoringsystembasedon
fine–tunedmodel.IEEESens.J.2023,23,8630–8638.[CrossRef]

Sensors2025,25,190 27of27
126. Wang,Z.;Pei,C.;Ma,M.;Wang,X.;Li,Z.;Pei,D.;Xie,G.RevisitingVAEforUnsupervisedTimeSeriesAnomalyDetection:A
FrequencyPerspective.InProceedingsoftheACMonWebConference2024,Singapore,13–17May2024;pp.3096–3105.
127. Gao,S.;Koker,T.;Queen,O.;Hartvigsen,T.;Tsiligkaridis,T.;Zitnik,M.Units:Buildingaunifiedtimeseriesmodel.arXiv2024,
arXiv:2403.00131.
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.