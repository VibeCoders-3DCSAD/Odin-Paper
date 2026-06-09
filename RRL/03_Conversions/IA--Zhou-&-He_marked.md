Rare Category Analysis for Complex Data: A Review
DAWEIZHOU,VirginiaTech
JINGRUIHE,UniversityofIllinoisatUrbana-Champaign
Thoughthesheervolumeofdatathatiscollectedisimmense,itistherarecategoriesthatareoftenthemost
importantinmanyhigh-impactdomains,rangingfromfinancialfrauddetectioninonlinetransactionnet-
workstoemergingtrenddetectioninsocialnetworks,fromspamimagedetectiononsocialmediaplatforms
torarediseasediagnosisinmedicaldecisionsupportsystems.Theuniquechallengesofrarecategoryanalysis
include(1)thehighlyskewedclassdistribution;(2)thenon-separablenatureoftherarecategoriesfromthe
majorityclasses;(3)dataandtaskheterogeneity;and(4)thetime-evolvingpropertyoftheinputdatasources.
Thissurveyreviewsstate-of-the-arttechniquesusedincomplexrarecategoryanalysis,wherethemajority
classeshaveasmoothdistributionwhiletheminorityclassesexhibitthecompactnesspropertyinthefeature
spaceorsubspace.Rarecategoryanalysisaimstoidentify,characterize,represent,andinterpretanomalies
thatnotonlyshowstatisticalsignificancebutalsoexhibitinterestingpatterns(e.g.,compactness,high-order
structures,showinginaburst).Weintroduceourstudy,definetheproblemsetting,anddescribetheunique
challengesofcomplexrarecategoryanalysis.Wethenpresentacomprehensivereviewofrecentadvances
thataredesignedforthisproblemsetting,fromrarecategoryexplorationwithoutanylabelinformationto
rarecategoryexpositionthatcharacterizesrareexampleswithacompactrepresentation,fromtherepresen-
tationofrarepatternsinasalientembeddingspacetotheinterpretationthepredictionresultsandproviding
relevantcluesfortheend-users’interpretation.Finallywediscusspotentialchallengesandshedlightonthe
futuredirectionsforcomplexrarecategoryanalysis.1
CCSConcepts:•Informationsystems→Datamining;
AdditionalKeyWordsandPhrases:Rarecategoryanalysis,imbalanceddatadistribution,anomalydetection
ACMReferenceformat:
DaweiZhouandJingruiHe.2023.RareCategoryAnalysisforComplexData:AReview.ACMComput.Surv.
56,5,Article123(November2023),35pages.
https://doi.org/10.1145/3626520
1Thisworkwasprimarilycompletedduringthefirstauthor’sPhDstudiesattheUniversityofIllinoisatUrbana-Champaign.
ThisworkissupportedbyNationalScienceFoundationunderAwardsNo.IIS-1947203,IIS-2002540,IIS-2137468,andIIS-
2117902.Theviewsandconclusionsarethoseoftheauthorsandshouldnotbeinterpretedasrepresentingtheofficial
policiesofthefundingagenciesorthegovernment.
Authors’ addresses: D. Zhou, Computer Science, Virginia Tech, 620 Drillfield Dr., Blacksburg, VA, 24060; e-mail:
zhoud@vt.edu;J.He,InformationScience,UniversityofIllinoisatUrbana-Champaign,501E.DanielSt,Champaign,IL,
61820-6211;e-mail:jingrui@illinois.edu.
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalorclassroomuseisgrantedwithoutfee
providedthatcopiesarenotmadeordistributedforprofitorcommercialadvantageandthatcopiesbearthisnoticeand
thefullcitationonthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthantheauthor(s)mustbe
honored.Abstractingwithcreditispermitted.Tocopyotherwise,orrepublish,topostonserversortoredistributetolists,
requirespriorspecificpermissionand/orafee.Requestpermissionsfrompermissions@acm.org.
©2023Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
0360-0300/2023/11-ART123$15.00
https://doi.org/10.1145/3626520
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.
123

123:2 D.ZhouandJ.He
1 INTRODUCTION
The so-called era of big data is defined in part by the sheer volume of multimodel data that are
beingcollectedfromvariousplatforms(e.g.,graphs,images,text).Yet,itistherareoccurrences—
those data points that are significantly different from other observations in the data—that often
areofgreatestimportanceinmanyhigh-impactdomains:fromfinancialfrauddetectioninonline
transactionnetworkstoemergingtrenddetectioninsocialnetworks,fromspamimagedetection
onsocialmediaplatformstorarediseasediagnosisinmedicaldecisionsupportsystems.Anomaly
detection refers to the process by which these rare occurrences are identified. Many techniques
havebeenproposedtocharacterizeanomaliesindomainssuchasfinancialfrauddetection[102],
insiderthreatprediction[66],noveltydetection[92],genediseasediscovery[17],emergingtrend
tracking[28],networkintrusiondetection[58],astronomy[133],spamimagedetection[93],and
rarediseasediagnosis[117].
1.1 Anomaliesvs.RareCategoryExamples
Thebranchofdataminingconcernedwithidentifyinganomaliesoroutliers2hasalengthyhistory.
In1980,DouglasM.Hawkinsproposedthedefinitionofoutliers[47]thatisshowninDefinition1.1.
Sincethistime,theproblemofanomalydetectionoroutlierdetectionhasbeengeneralizedand
studied in various contexts, such as those of high-dimensional numerical data [173], sequential
data [27], time-series data [45], graph data [7], and financial data [36, 113]. This wide-ranging
explorationhasyieldedmanydomain-specifictermsforoutliers,includingnoveltiesevents,sur-
prisingchanges,fraudsoutbreak.
Definition1.1. Hawkins’sDefinitionofOutliers[47]
Anoutlierisanobservationthatdifferssomuchfromotherobservationsastoarousesus-
picionthatitwasgeneratedbyadifferentmechanism.
Thoughresearchershavehadtremendoussuccessapplyinganomalydetectionmethodsinvar-
iousdomains,notallanomaliesdetectedarenecessarilyusefulorrelevanttotheactualeventsof
interest.Infact,mostanomaliesareuninterestingdatapointsthateitheraredrawnfromaknown
distributionofnoiseorcorrespondtocombinationsoffeaturesthatareirrelevanttodownstream
applications[109].Forinstance,inFigure1,wepresentasetofskyimagescapturedbyground-
based telescopes as part of the Sloan Digital Sky Survey (program).3 According to the Sloan
Digital Sky Survey 99.9% of its captured sky images (e.g., the top row of Figure 1) can be well
explained based on known phenomena of the universe (e.g., discovered stars, comets, nebulae);
only 0.1% of the images (e.g., the bottom row of Figure 1) are anomalies. Moreover, among the
anomalies,99%oftheimages(e.g.,bottomleftimageinFigure1)areofnointeresttoastronomers
andarecausedbydiffractionspikesofsatellitetrailsorartifactsofthetelescope.Only1%ofthe
instances(aminuscule0.001%oftheSloanDigitalSkySurveydatabase)areusefulandmaylead
tonewscientificdiscoveries(e.g.,thebottomrightimageinFigure1).Here,werefertoanomalies
that are not only statistically significant but also interesting as rare category examples and the
problem of studying rare category examples as rare category analysis. Figure 2 illustrates the
relationshipamonganomalies,uninterestinganomalies,andusefulanomalies(i.e.,rarecategory
examples),whererarecategoryexamplesareasubsetofanomaliesthatarenotonlystatistically
significantbutalsocompactinthefeaturespace.
Weprovidethefollowinggeneraldefinitionofrarecategoryanalysis:Givenadataset D ofn
(cid:2) →−
examplesthatcomefromCdistinctclasses,withoutlossofgenerality,weassumethat n x = 0
i=1 i
2Inthisarticle,weuse“anomalies”and“outliers”interchangeably.
3http://www.sdss.org/iotw/archive.html
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:3
Fig.1. AnomaliesinSloandata[109].Toprow:knownobjects.Bottomrow:anomalies,99%ofwhichare
uninteresting patterns, such as diffraction spikes (bottom left) and only 1% of which are interesting pat-
terns that are worthy of future research and may lead to the discovery of extraordinary objects (bottom
right).
Fig.2. Relationshipbetweenanomalies/outliersandrarecategoryexamples.
(cid:2)
and 1 n (xj)2 =1,wherexj denotesthejthfeatureofx .Forthesakeofsimplicity,weassume
n i=1 i i i
theclasslabelfor theith node,y = 0, correspondsto themajority class(i.e.,normalexamples)
i
andy ∈ {1,...,C −1} corresponds to the rare categories (i.e., suspicious examples). Note that
i
rarecategoryanalysisistheproblemofstudyingpatternsintheminorityclasses.4 Inparticular,
forcasesinwhichmorethanonemajorityclassisobserved,wetreatallthemajorityclassesasa
singleclassoncetheunderlyingdistributionofeachmajorityclassissufficientlysmooth[49].In
generalrarecategoryanalysis,wemakethefollowingassumptionsregardingthesupportregion
ofthemajorityclassandminorityclasses:
Assumption 1. Smoothness Assumption for Majority Class. Given a highly imbalanced
dataset,thedistributionofthesupportregionofeachmajorityclassissufficientlysmooth.
Assumption2. CompactnessAssumptionforMinorityClass.Givenahighlyskeweddataset,
theminorityclassexamplescanberepresentedasacompactclusterinthefeaturespace.
Theseassumptionsaremadetoensurethattherarecategoriesareidentifiableandmeaningful.
To better capture this, let us look first at the example in Figure 3(a), where the majority class
(shown in blue) has a Gaussian distribution with large variance on the left, while the minority
4Inthisarticle,weuse“rarecategory”and“minorityclass”interchangeably.
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:4 D.ZhouandJ.He
Fig.3. Thesupportregionsofamajorityclassandaminorityclassinaone-dimensionalsyntheticdataset.
class (shown in orange) corresponds to a peak with small variance on the right. If the minority
classisnotcompactandviolatesAssumption2(e.g.,theminorityclassinFigure3(b)isuniformly
distributedinthefeaturespace),thennoalgorithmcanperformbetterthanrandomsampling.If
thedistributionofthemajorityclassisnotsmoothandviolatesAssumption1(e.g.,themajority
classinFigure3(c)consistsofmultiplenarrowandsharppeaksjustliketheminorityclass),then
theminorityclasscannotbeidentifiedwithaclearclue.Basedontheassumptionsrelatedtorare
categoryexamples,weproposethefollowingdefinitionofcomplexrarecategoryanalysis:
Definition1.2. ComplexRareCategoryAnalysis
Complex rare category analysis refers to the problem of detecting, characterizing, repre-
senting,andinterpretingrareexamplesfromunderrepresentedminorityclassesinahighly
imbalanceddataset.
1.2 ChallengesofRareCategoryAnalysis
Wefirstdiscussthekeychallengesassociatedwithrarecategoryanalysis.Unliketheconventional
anomalies,rarecategoryexampleshavethefollowinguniquecharacteristics:
• C1.Rarity.Itisoftenthecasethatthepatternsofinterestaresporadicinthecollecteddata.
Forexample,infinancialfrauddetection,thevastmajorityoffinancialtransactionsarele-
gitimate;onlyasmallnumbermayberelatedtomoneylaundering,andtheyoftenexhibit
similartraits.Anotherexampleisnetworkintrusiondetection.Newmaliciousnetworkac-
tivitiesarehiddenamonghugevolumesofroutinenetworktraffic,andnetworkintrusions
ofthesametypeareoftensimilartooneanother.
• C2.LabelScarcity.Giventhehighskewnessandnon-separablenatureofrarecategories,
labelingrarecategoryexamplesisextremelyexpensive.Invariousrealapplications,suchas
moneylaunderingdetection,syntheticidentity(ID)detection,andnetworkintrusiondetec-
tion,weareusuallyrequiredtolearnfromahandfuloflabeledexamples.
• C3.Non-separability.Rarecategoriesareoftennon-separablefromthemajorityclassesin
thefeaturespace.Forexample,fromthealarmofgridhacking(e.g.,NotPetya)totheswift
growthincyber-criminals(e.g.,coin-miningattacks),thepastseveralyearshaveservedas
astarkreminderofanemergingtypeofterroristattack(i.e.,adversarialattacks).Suchmali-
ciousattacksaredesignedtobypasscurrentdetectionsystemsbycamouflagingthemselves
asnormalinstances,i.e.,thesupportregionsofnormalinstances,andmaliciousattacksare
non-separableinthegivenfeaturespace.
• C4.DataHeterogeneity.Toidentifytherarecategories,weoftenneedtocollectrawdata
fromdifferentsources,atdifferenttimestampsusingdifferenttechniques.Eachdatasource
mighthavedifferenttypesofusersandattributes.Ofsuchhighlyheterogeneousrawdata,
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:5
Fig.4. Overviewofcomplexrarecategoryanalysis.
onlyasubset(e.g.,datasources,attributes)mayberelevanttotheidentificationoftherare
categoryexamples(e.g.,securitythreats).
• C5. Dynamics. The raw input data continuously change over time; thus, extracting and
modeling useful information from such dynamic systems plays an important role in rare
categoryanalysis.
1.3 AnOverviewofComplexRareCategoryAnalysis
Complex rare category analysis can be divided into four tasks: detecting, characterizing, repre-
senting,andinterpretingrarecategoryexamples.Figure4presentsanoverviewofrarecategory
analysis,fromtheexplorationstepwithoutanygroundtruthtotheexpositionstepthataimsto
characterize rare examples with a compact representation, from representing rare patterns in a
salientspacetoprovidinginsightfulinterpretationoverthepredictionresults.
• T1:RareCategoryExploration. Inthistask,westartfromde-novoanddonothaveany
label information for the data. The goal is to identify at least one example from each rare
categorywithminimalhelpfromlabelingoracles.Webeginwithacomprehensivereview
ofsomerelevanttopics,includinganomalydetection[7,26],outlierdetection[57],andpre-
dictivemodelingonimbalanceddomains[20];thenweelaborateonpopularapproachesto
rarecategoryexplorationinbothstaticanddynamicenvironments.
• T2: Rare Category Exploitation. In this task, we use one/a few labeled examples from
eachclassthatmayhavebeenobtainedfromtheexploratorystepdiscussedinT1.Thepri-
marygoalistocaptureacompactrepresentationoftherarecategoriesinvariousdatafor-
mats by learning from a few-shot annotated data points. Depending on the availability of
amultimodalrepresentationofexamples,rarecategorydetectioncanbecategorizedasho-
mogeneous rare category exploration or heterogeneous rare category exploration. In the
formersetting[52,109],alltheexamplesarehomogeneous,astheyarecollectedfromthe
samedatasourceorhaveidenticaltraits;inthelatterone[41,79,160,163],weaimtoidentify
rarecategoriesinthepresenceofdataheterogeneity.
• T3:UnderstandingRareCategories: Thistask,whichmayentailrepresentingrareexam-
plesinasalientembeddingspace,visualizingthedatadistribution,orinterpretingtheunder-
lyingpredictionprocessintheprevioussteps(T1andT2),servesasaninvestigationstepfor
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:6 D.ZhouandJ.He
end-users. We systematically discuss recent advances in representation learning [60, 166],
interpretation[30,84,89],andvisualanalyticsystems[81,105]forrarecategoryanalysis.
1.4 PreviousWorkandOurContributionstotheLiterature
Extensiveliteraturesurveysonthetopicsofimbalancedclassification,anomaly/outlierdetection,
andfrauddetectionhavebeenpublishedinthepastdecade.Inthecontextofimbalancedclassifi-
cation,HeandGarcia[48]coverthedevelopmentofresearchonlearningfromimbalanceddata.
Inthecontextofanomaly/outlierdetection,HodgeandAustin[57]introducesaliteraturereview
ofcontemporarytechniquesforoutlierdetection,andChandolaetal.[26]presentsacomprehen-
siveoverviewoftheresearchonanomalydetection.Aseriesofsurveysandspecial-issuejournal
articlesthattargetmorespecificproblemsandapplicationsinthecontextofanomaly/outlierdetec-
tionhavealsobeenpublished.Inparticular,Zimeketal.[173]studiestheproblemofunsupervised
outlierdetectioninhigh-dimensionalnumericaldata,Chandolaetal.[27]considersanomaliesin
discretesequences,Guptaetal.[45]focusonoutlierdetectionfortemporaldata,Akogluetal.[7]
attends to graph-based anomaly detection algorithms, Chalapathy and Chawla [25] provide an
overviewofdeep-learning-basedanomalydetectiontechniques,and,EdgeandFalconeSampaio
[36]andPhuaetal.[113]surveymethodologiesoffrauddetection.
However,veryfewworkspresentacomprehensiveoverviewofcomplexrarecategoryanalysis.
He[49]isoneofthefirsttopresentanend-to-endinvestigationofrarecategories,buttheintro-
ducedmethodologiesarelargelyrestrictedtothetabulardatainthestaticsetting.Respondingto
the gap in the literature, here we provide a comprehensive and structured overview of complex
rarecategoryanalysisfromseveralperspectives:
• DataPerspective.Unliketheprevioussurveysonoutlierdetection,anomalydetection,and
rarecategoryanalysis,ourstudyreviewsstate-of-the-arttechniquesforhandlingrichdata
types,suchastext/blogs,electronichealthrecords,weblinkgraphs,andstreamingdata.
• TaskPerspective.Weprovideacomprehensiveoverviewofend-to-endcomplexrarecategory
analysis,fromrarecategoryexplorationwithoutanylabelinformation,torarecategoryex-
positioncharacterizingrareexampleswithcompactrepresentation,fromrepresentingrare
patterns in a salient embedding space to interpreting the prediction results and providing
relevantcluesforend-users’investigation.
1.5 SurveyRoadmap
We present our survey in five parts sections. In Section 2, we focus on the de novo step of rare
categoryanalysis,i.e.,rarecategoryexploration,whichaimstofindtheinitialexamplefromeach
minorityclassintheunsupervisedsetting.InSection3,wediscussthefollowingstep,rarecategory
exploitation, which relies on the output of rare category exploration (i.e., initially labeled exam-
ples)tocharacterizetherarecategories.InSection4,westresstheimportanceofinterpretationin
rarecategoryanalysisinvarioushighlyregulatedindustries,suchasfinanceandhealthcare.We
systematicallydiscusshowtounderstandrarecategoryanalysisfromthefollowingtwoaspects:
(1) data diagnosis (i.e., How are the data distributed? Which piece of information is most valuable
foragiventask?);and(2)modeldiagnosis(i.e.,Whydoesthemodelmakeacertainpredictionona
particularpieceofinformation?).Section5enumeratesthepopularbenchmarkdatasetsandrepre-
sentativebaselinemodels.InSection6,weconcludeourstudyandshareourthoughtsregarding
futureresearchdirections,suchashowtoensureperformanceinthepresenceofnoise,missing
data, and adversarial examples and how to generate task-specific rare category examples (e.g.,
moneylaunderingactivity)givenaspecificdomain(e.g.,transactionnetworks).Ageneraloutline
follows:
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:7
• Section2:RareCategoryExploration
– 2.1Rarecategoryexplorationforstaticdata
∗ 2.1.1Tabulardata
∗ 2.1.2Graph-structureddata
– 2.2Rarecategoryexplorationfordynamicdata
∗ 2.2.1Time-seriesdata
∗ 2.2.2Temporalgraphs
• Section3:RareCategoryExploitation
– 3.1Homogeneousrarecategoryexploitation
∗ 3.1.1Globalapproaches
∗ 3.1.2Localapproaches
– 3.2Heterogeneousrarecategoryexploitation
∗ 3.2.1Dataheterogeneity
∗ 3.2.2Taskheterogeneity
• Section4:UnderstandingRareCategories
– 4.1Rarecategoryrepresentation
– 4.2Rarecategoryinterpretation
• Section5:DatasetsandRepresentativeMethods
– 5.1Datasets
– 5.2Representativemethods
• Section6:ConclusionandFutureDirections
2 RARECATEGORYEXPLORATION
Consideredthedenovostepinrarecategoryanalysis,rarecategoryexploration,a.k.a.rarecate-
gorydetection,aimstoproposeinitialrarecategoryexamplestothelabelingoracleinthegiven
dataset.Givenanunlabeled,imbalanceddataset,themostnaturalmethodofrarecategoryexplo-
rationisrandomsampling.Inthismethodwerandomlydrawexampleswithoutreplacementto
be labeled by the oracle until at least one example from each minority class has been identified.
However,duetotherarityofrarecategories(e.g.,theproportionofararecategoryis0.01%),an
extensivenumber(i.e.,10,000)oflabelingrequestsisrequiredtospottherareexample.Itisthus
worthwhiletodevelopmoreeffectiveandefficientsamplingstrategiestoaddressthisrarecategory
explorationproblem.Inthissection,weformallydefinetheproblemofrarecategoryexploration.
Weprimarilyaimtoaddress(C1)rarity,(C4)dataheterogeneity,and(C5)dynamicsinrarecategory
analysis.
Problem1. RareCategoryExploration.
Given:(i)anunlabeleddatasetD,(ii)asmallbudgetBforqueryingdomainexperts.
Find:thesetofinitialexamplesQ fromeachrarecategory.
Inreal-worldapplicationsofrarecategoryexploration,researchershavecustomizedProblem1
fordifferentdataformats,includingtabulardata,time-seriesdata,andgraph-structureddata.In
the following three subsections, we review the existing literature on rare category exploration
fromadataperspective(e.g.,staticdatavs.dynamicdata,tabulardatavs.graph-structureddata).
2.1 RareCategoryExplorationforStaticPatterns
Thetechniquescurrentlyusedinthestaticsettinghavebeenprimarilydesignedinactive-learning-
based schemes. The general procedure of this paradigm is presented in Figure 5. The key idea
behindthesample-selection-basedmethodsistolearnadetectorthatcangraduallysearchforthe
potentialrareexamplesbylearningfromtheexampleslabeledbytheoracle.Weoftenassumethat
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:8 D.ZhouandJ.He
Fig.5. Aconceptualframeworkforrarecategoryexploration[109].
the labels obtained from the oracles are under a fixed budget B. Thus, the goal is to maximally
improvethepredictionaccuracywiththeminimumnumberoflabelingrequeststotheoracle.As
showninFigure5,rarecategoryexplorationproceedsiteratively.Ineachiteration,theprogram
starts with the oracle annotating a few samples. Then the sample-selection-based methods are
updated based on the newly labeled examples and further predict a small number of potential
rarecategoryexamplesinthesensethatobtaininglabelsforthemfurtherimprovestheprediction
accuracy. The program terminates once all the target rare categories have been captured. Next,
weelaborateontheexistingrarecategoryexplorationalgorithmsdesignedfortabularandgraph-
structureddata.
2.1.1 TabularData. GivenanunlabeleddatasetwithnsamplesD = {x ,...,x },whereeach
1 n
samplex ,i =1,...,ncomeswithd-dimensionalfeaturesx = {x1,...,xd},ourgoalistoidentify
i i i i
atleastoneexamplefromeachclassy =1,...,mwiththeminimumnumberofqueries.Thework
of Peleg and Moore [109] is one of the first attempts at rare category exploration. The authors
developamixturemodeltofitthedataanddesignafamilyofhintselectionmethodstoselectthe
rareexampleswiththehelpofahumanexpert.Experimentalresultsusingdifferenthintselection
methodsshowtheefficacyoftheproposedrarecategorydetectionframework.HeandCarbonell
[52] study the rare category exploration problem when the minority classes are non-separable
fromthemajorityclasses.Specifically,theauthorsdevelopanearest-neighbor-basedrarecategory
detectionalgorithmnamedNNDM,whichgraduallyselectsexampleswiththemaximumchanges
inthelocaldensityonacertainscaleandasksforlabelingfromtheoracle.Thealgorithmworks
asfollows:Giventhepriorp ofeachrarecategoryC,thealgorithmfirstestimatesthenumberof
examplesK =n×pinC.Then,thealgorithmrepresentseachexamplex intermsofavectorthat
i
iscomposedofthedistancesfromitsK-nearestneighbors.Byobtainingtheminimumdistancer
amongallsamples,thealgorithmconstructsahyper-ballwithradiusr foreachexample(ascenter)
andcomputesthelocaldensityasthenumberofenclosedexampleswithinthehyper-ball:
Hyberball(x ,r) = {x|x∈ D,(cid:5)x−x (cid:5) ≤r} (1)
i i
LocalDensity(x ) = |Hyberball(x ,r)| (2)
i i
Tomeasurethedegreeoflocaldensitychangesaroundeachsample(i.e.,hyper-ball),theauthors
proposeusingthedifferenceinthelocaldensitybetweenx anditsneighbors:
i
DensityChange(x )
i
= ⎧⎪ ⎨ ⎪ max xk ∈Hyberball(xi,r) [LocalDensity(x i )−LocalDensity(x k )] x i islabeled (3)
⎩ −∞ Otherwise
Inparticular,thefunctionDensityChangeassignseachlabeledexample’sscoreswith−∞toavoid
duplicated labeling requests. Finally, the algorithm returns the examples with the largest local
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:9
densitychangestotheoracleforlabeling:
Query=argmax xi ∈D DensityChange(x i ) (4)
Theoretical analysis shows that the methods effectively select examples on both the boundary
andintheinterioroftherarecategories.Inparticular,whentherarecategoriesarecompact,the
majorityclassdistributionislocallysmooth,andthesamplespaceissufficientlylarge,NNDMis
guaranteedtoidentifyatleastoneexamplecomingfromeachminorityclasswithprobability1−δ
after (cid:8)2α(cid:9) iterations,whereδ ∈ (0,1),α,andr areallpositiveparameters.
r2 2
Despite the promising results of NNDM with theoretical guarantees, the algorithm’s perfor-
mancelargelyreliesonpriorinformation(e.g.,numberofclasses,proportionofminorityclasses).
To alleviate the restriction on prior knowledge, He and Carbonell [50] propose a prior-free rare
categorydetectionalgorithmnamedSEDER.Theintuitionofthisalgorithmliesintheobservation
thataregionwithanabruptlocaldensitychangehasahigherprobabilityofobservingtherare
classes.UnlikeHeandCarbonell[52]andHeetal.[53],SEDERpicksthepotentialrareexamples
withlargeneighborhooddensitychangesforlabelingbyperformingsemi-parametricdensityes-
timation.SEDERintroducesaprior-freeDensityChangefunction,whichisdefinedasthenormof
thegradientofthelocaldensityfunction:
(cid:6)(cid:3)(cid:4)
(cid:2)
(cid:5)d ( n DensityEstimation(x )(xl −blxl))2
DensityChange(x ) = k=1 i i k (5)
i
((σl)2bl)2
l=1
where xl denotes the lth feature of x , σl denotes the bandwidth of the lth feature,
i i
DensityEstimationisakerneldensityestimationfunctionwithGaussiankernel[37],andbl is
apositiveparameter.Inthepresenceofnoisydataandirrelevantfeatures,HeandCarbonell[51]
formulate the rare category exploration problem via a co-selection scheme, which recovers the
relevantfeaturesandrepresentativeexamplesfromtherarecategories.Toobtaintheoptimalsets
ofrelevantfeaturesandrareexamples,HeandCarbonellproposeaneffectivesearchingprocedure
(i.e.,PALM)basedonanaugmentedLagrangianfunctiontosolvetheoptimizationproblem.Inpar-
ticular,PALM isdesignedinanalternativefashionsothattherelevantfeaturesandtheminority
classexamplescanbefound.
Recently,aparadigmshifthasbeenobservedinthedataminingcommunity:fromhowtoac-
curatelydetectrarecategoriestohowtoensuretrustworthinessinrarecategoryexploration.For
instance,AhmadianandLindsten[4],Kauretal.[67],andLiuetal.[83]studyhowtoensurerobust-
nessindetectingrareevents,especiallyintheout-of-distributionsetting.Shekharetal.[120]point
outthatalgorithmicfairnessandrarecategoryexplorationaredualproblemswhenencountering
thedataimbalanceissue.Theauthorsproposeafairness-awaremethodthatjointlyoptimizespre-
dictionaccuracyandstatisticalparity.Dengetal.[32]studythehardnessbiasintheautoencoder-
basedrarecategorydetectionmethodsandproposeaplug-and-playerrorcalibrationmethodto
mitigatethehardnessbiasissue.
2.1.2 Graph-StructuredData. Inmanyfields,graphsofferaunifyingdatastructureformodel-
ing relational data. As a result, extensive research related to rare category exploration has been
conductedtospottherarecategoryentitiesingraph-structureddata.Formallyspeaking,givenan
unlabeledgraphD = G(V,E),whereV andE denotethesetsofnodesandedgesinG,respec-
tively,ourtargetistoidentifyinitialnodesandedgesfromeachoftherarecategories.Heetal.[53]
extendstheideaofHeandCarbonell[52]tograph-structureddatabyproposingagraph-basedrare
categorydetectionalgorithmnamedGRADE.Thealgorithmstartscomputingaglobalsimilarity
matrixSmotivatedbymanifoldranking[169],whichisusedtoobtainacompactrepresentation
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:10 D.ZhouandJ.He
oftheexamplesfromtheminorityclasses:
S= (I−αD −1 2AD − 2 1 ) −1 (6)
whereIdenotestheidentifymatrix,Ddenotesthediagonalmatrix,andAdenotestheadjacency
matrix of G. A prior-guided k-nearest-neighbor matrix is then computed to capture the sharp
localdensitychangesneartheboundaryofminorityclassesandthusmakeiteasiertocapturethe
rarepatterns.InadditiontodevelopingGRADE,theauthorsdevelopavariationnamedGRADE-LI,
whichrequiresonlyanupperboundontheproportionofeachrarecategory.GRADE-LI canwork
with the data when a detailed class-membership distribution of the data is not available to the
users.
Exceptfortheplaingraphs,dataoftenexhibitnode-levelandedge-levelheterogeneityforvar-
ious critical tasks in security, finance, and medicine, among other fields. Each node or edge is
associated with a specific type in such data (referred to as a heterogeneous graph). To accommo-
dateheterogeneousgraphs,researchershavestudiedhowtodetectanomaliesandrareeventsin
the unsupervised setting. For example, Sun et al. [127] propose the notion of neighborhood for-
mationforabipartitegraph,whichcomputestherelevancescoresofallnodestoaquerynodev
anddefinetheneighborhoodofv asthesetofnodeswithhigherrelevancescores.Basedonthe
neighborhoodformation,theauthorsdevelopananomalydetectionalgorithmtospottheabnor-
mal nodes with low “normality” scores. Based on similar intuition, Tong and Lin [132] propose
a non-negative residual matrix factorization framework named NrMF, which aims to detect the
maliciousgroupofentitiesaswellasprovideinterpretationofpredictionresultsfordataanalysts.
NrMF isbuiltupontheconventionalmatrixfactorizationmechanism,
A=FG+R (7)
whereFandGarelow-rankfactorizedmatrices,andR istheresidualmatrixthatindicatesrare
examplesonthebipartitegraphs.TointerpretthepredictionsviaNrMF,TongandLinimposea
non-negativeconstraintontheresidualmatrixR,suchthatallentriesinRarelargerthan0.Intu-
itively,highervalueoftheentryinRindicatesahigherprobabilityofexistingrareandabnormal
examples.Tosolvetheoptimizationproblemofnon-negativeresidualmatrixfactorization,theau-
thorsdevelopafastoptimizationalgorithmtoincrementallycomputetheresidualmatrixviathe
rank-1approximation,whichrunsinlinearw.r.t.thesizeofthegraph.
Morerecently,extensiveattemptshavebeenmadetopredictrarecategoryeventsbydeveloping
customizedgraphneuralnetworks(GNNs)todepictthestructureofagraphandlearnrepre-
sentations of various graph signals (e.g., nodes, edges, subgraphs). GNNs-based approaches are
generallydesignedbasedonthemessage-passingscheme,whichisgivenasfollows:
h(l+1) =UPDATE(l)(h(l),AGGREGATE(l)(h(l),∀u ∈N(v))) (8)
v v u
=UPDATE(l)(h(l),m(l) ) (9)
v N(v)
where h(l+1) denotes the embedding of node v ∈ V at the (l + 1)th-layer, UPDATE(l) and
v
AGGREGATE(l) arebothdifferentiablefunctionsforthelth-layer,andm(l) istheaggregated“mes-
N(v)
sage” from nodev’sneighborhoodN(v). Deng et al. [34] proposea graph convolutional net-
work(GCN)-basedframeworkforpredictingemergingeventsthatrequirescapturingcontextual
information from the raw data. The proposed framework first extracts graph representations of
theevents;itthendocumentsandlearnstopredicttheoccurrenceoffutureeventsandtoidentify
theeventsofinterest(i.e.,rarecategories).Zhongetal.[162]studiestheproblemofrarecategory
detectioninvideos,whereeachvideoisdecomposedintonsnippets(i.e.,nodesintheconstructed
videograph),theedgesbetweeneachpairofsnippetsaredefinedbasedonfeaturesimilarity,and
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:11
Fig.6. Anillustrationofthebi-levelrarecategories(i.e.,raresequencesandraretimesegments)inatime-
seriesdatabase[164].
the rare events are represented as abnormal actions. To solve this problem, a GCN is built to si-
multaneously clean noisy signals in the constructed video graph and predict abnormal actions.
Goodge et al. [42] investigate the relationship between the local outlier methods [69] and the
message-passingframework,whichmotivatesthemtodevelopaGNN-basedmethodtoidentify
localrareexamples.
2.2 RareCategoryExplorationforDynamicPatterns
Theexistingliteratureondetectingrarepatternsintemporaldataisveryrich,withnouniversal
abstractcategorizationcapableofcapturingallthedevelopedtechniquesinthisdirection.Accord-
ingly,weherefocusonrarecategoryexplorationfortime-seriesdataandtemporalgraphs.
2.2.1 Time-SeriesData. Inthesettingoftime-seriesdata,therarecategoriescanbeobserved
atboththesequencelevelandthesegmentlevel,asshowninFigure6.Forexample,mostelectro-
cardiogram(ECG)signalsarenormal(i.e.,collectedfromhealthypeople);onlyasmallportionof
themisabnormal(i.e.,collectedfrompatientswithheartdisease).Moreover,withintheabnormal
ECGsignals,onlyafewsegmentsareabnormal(e.g.,heartarrhythmia);therestarenormal.Early
studiesofrarecategoryexplorationfortime-seriesdata[18,21,22,65,80,97,100,108,118,150]
arecloselyrelatedtotheoutlierdetectionanddisorderdetectionmethods.Theyrelylargelyon
distanced-basedmechanisms[97,101,116,119]thatdefinevarioussimilaritymeasurements[45]of
temporalsequencesandsegmentsandthenidentifyrarepatternsdeviatingfromthenormalones.
Forinstance,Caoetal.[22]proposeascalabledistance-baseddetectionalgorithmforhigh-volume
data streams. This algorithm has been found to be optimal in terms of CPU costs. Begum and
Keogh[18]studytheproblemofdiscoveringraretime-seriesmotifs(i.e.,repeatedsubsequences)
from unbounded streams. To address the rarity issue of the time-series motif in a never-ending
stream,BegumandKeoghdevelopa“stickycash”algorithmthatadoptsaBloomfiltertoremem-
bereveryincomingsubsequenceandefficientlydetectsraremotifsintheunboundedreal-valued
timeseries.Tofacilitatetheuseofdistance-basedmethods,Yehetal.[150]introduceafastcompu-
tationalalgorithmfortime-series/subsequenceall-pairs-similarity-searchthathasstrongimplica-
tionsforandpromisingresultsforthetaskoftime-seriesdiscorddiscovery.Finally,Goodgeetal.
[43]introducearobustrandom-cutdatastructuretoproduceasketchorsynopsisoftime-series
data.Usingthisstructure,theauthorsproposeascalableanomalydetectionalgorithmbygradually
updatingthetime-seriessketchinacontinuousdatastream.
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:12 D.ZhouandJ.He
A key motivation of the aforementioned methods is that the distributions of rare categories
(minorities) deviate from the normal distribution (majorities). However, there are some obvious
limitationstothisideainpractice.Theidentifiedexamplesareoftennotthetargetsofresearchers’
interest,whicharedrawnfromnoiseorcombinationsofirrelevantfeatures.Zhouetal.[164]as-
sumethatthetargetsofourinterestarerareanddrawnfromacompactdistribution.Underthis
assumption,Zhouetal.proposeabi-levelgenerativemodelthataimstojointlycharacterizethe
raretemporalpatternatthetime-seriesandsubsequencelevels.Recentadvancesindeeplearning
architectureshave led to a surge in research interest related to developing deep models to char-
acterizeanddetectraretemporalpatternsinhigh-impactapplications.Tuoretal.[134]presenta
deepunsupervisedframeworkfordetectinginsiderthreatinonlinedatastreams.Thisframework
outputsarankedlistofanomalyscoresofindividualuserbehaviors;Lietal.[77]developagen-
erative adversarial network (GAN) for unsupervised multivariate anomaly detection. Unlike
conventional distance-based methods and supervised methods, the proposed framework detects
rare temporal patterns by using the GAN-trained generator and discriminator to compute the
discriminationandreconstructionanomalyscore(DR-Score);Shenetal.[121]proposeare-
currentnetworkensemblecalledtherecurrentautoencoder,whichisdesignedtocharacterizeand
capture the abnormal time-series segments at multiple resolutions; finally, Deng and Hooi [33]
andZhangetal.[159]proposemodelingthebetween-sensordependencerelationshiptoidentify
abnormaltimesegmentsinmultivariatetimeseries.
2.2.2 TemporalGraphs. Manyreal-worldsystems,includingsocialnetworks,communication
networks, and gene interaction networks, are intrinsically dynamic and can be represented as
temporal graphs. In the past few years, researchers have proposed several rare category explo-
ration models for temporal graphs [3, 13, 34, 59, 76, 89, 90, 115, 125, 140, 149, 153, 167, 168].
The existing work can be categorized as discrete temporal graphs [154] or continuous temporal
graphs [85, 103, 171] based on the method of data collection used in the particular application
domain.
The discrete temporal graphs are often referred to as a time-evolving graphsn wherein the
data D is presented as a sequence of snapshots G˜ = {G(1),G(2),...,G(T)}. Each snapshot
G(t) = (V(t),E(t)),t = 1,2,...,T is composed of a collection of nodes V(t) and edges E(t) at
timestamp t. To identify rare examples on G˜, the static methods are extended to the dynamic
setting.Forexample,Sunetal.[126]proposeaparameter-freemodelthatcanmonitorgrouped
outliersandtheirchangesinastreamofgraphs.Thealgorithmisdesignedbasedonminimum
descriptionlength(MDL),whichallowsuserstodiscoverthechangesincommunitiesaswell
asinpointsintime.Araujoetal.[14]developafastincrementaltensoranalysisapproachthatcan
discoverbothtransientandperiodic/repeatingcommunitiesindynamicgraphs.SricharanandDas
[125] define a commute-time distance that captures node relationship changes and allows tradi-
tionaldistance-basedmethodstobeusedwithdiscretetemporalgraphs.Leeetal.[76]proposea
discrete-timeexponential-familyrandomgraphmodeltoidentifyclustersintime-evolvinggraphs.
Manzooretal.[90]studytheproblemofanomalydetectioninstreamingheterogeneousgraphsby
proposingaclustering-basedanomalydetectionapproachthatcansimultaneouslyaddressthehet-
erogeneityandstreamingnatureoftheinputdata.Inparticular,Manzooretal.introduceanovel
embeddingmechanismthatcanencodetheheterogeneousstreaminggraphintoavectorrepresen-
tationthatisthenusedtoperformclusteringandidentifyanomalouspatterns.Appeletal.[13]
proposesafactorizationframeworkthatcanjointlymodelthedistributionofdynamicconnections
andattributesandtracktheevolutionofevolvingcommunities.Despitetheirsuccess,thedetec-
tionalgorithmsoftensufferfromhighcomputationalcosts,especiallywhenextensivesnapshots
are given or when the algorithms are applied in the online setting. To address this issue, Zhou
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:13
etal.[167,168]proposeanincrementalrarecategoryexplorationschemethataimstogradually
updatethestaticrarecategoryexplorationmodelsbasedonthelocalchangesonanewsnapshot
withoutlearningfromscratch.Inparticular,Zhouetal.proposeaclosed-formsolutiontoupdate
theglobalsimilaritymatrixS(definedinEquation(6))inthedynamicsetting:
S(t) =S(t−1) +α
S(t−1)uvTS(t−1)
(10)
I+vTS(t−1)u
where u and v are one-hot vectors indicating the source nodes and target nodes of the updated
edges,respectively;Idenotestheidentitymatrix;andS(t)andS(t−1)aretheglobalsimilaritymatri-
cesatthetimestampstand(t−1),respectively.Moreover,toefficientlyandeffectivelycomputethe
densitychanges,DensityChange(x ),atheoreticalcondition,isprovidedtodeterminewhetherthe
i
hyper-ballHyberball(x ,r)isrequiredtoupdatefromtheprevioustimestamp.YasamiandSafaei
i
[149]studytheproblemofanomalydetectionindynamicsocialnetworks,whereinbothnetwork
structureandnodeattributesareobservedovertime.Theproposedframeworkjointlymodelstwo
processes,i.e.,(1)thenormalmodelingcomponentand(2)theanomalydetectioncomponent,to
track the abnormal relationship between nodes’ features and link generation in dynamic social
networks.Agarwaletal.[3]introduceanovelcommunityscoringmetriccalledpermanenceand
proposesanincrementalalgorithmtotracktheevolutionofnetworkcommunitiesinthedynamic
setting. The theoretical analysis shows that the updating procedure of the proposed algorithms
leadstopermanencemaximizationinthedynamicnetworks.Furthermore,toguaranteemodeleffi-
ciencyandalgorithmicfairness,Fuetal.[39]introduceafairness-awareclique-preservingspectral
clusteringalgorithmthatgeneralizesthestaticcliqueclusteringmethodstothedynamicsetting
viafairness-awareedgefilteringandincrementaleigenpairupdating.
Continuoustemporalgraphsarealsocalledfine-grainedtemporalgraphsortemporalinteraction
graphs,wherethetemporalgraphispresentedasasequenceoftimestampededges.Itisintractable
to directly generalize the static rare category exploration approaches used in discrete temporal
graphstocontinuoustemporalgraphs.Forthisreason,Manzooretal.[90]proposetorepresent
continuoustemporalgraphswithavectorrepresentation,whichiseasytocomputeandpreserves
thecontextualinformationofthecontinuoustemporalgraphs.Withthelearnedcontinuoustem-
poral graph representation, Manzoor et al. develop a fast and memory-efficient detection algo-
rithmtoprocessanyincomingnodesandedgesandidentifyanomaliesinrealtime.Hollocouetal.
[59] subsequently studies the problem of identifying grouped anomalies in the edge streaming
setting. In particular, the data are presented as a sequence of streaming edges. The authors pro-
poseastreamingalgorithmwiththetheoreticaljustificationthatperformsgraphclusteringwith
onlythreeintegerspernodeanddoesnotkeepanyedgeinmemory.AmjadiandTulabandhula
[10] propose a block-structured time-series model for detecting communities on time-evolving
graphs. This approach can capture both the link persistence and community persistence over
time.
3 RARECATEGORYEXPLOITATION
Intheprevioussection,weintroducedthecurrentliteratureonrarecategoryexploration,aprob-
lemthataimstoidentifyatleastoneexamplefromeachminorityclass.Afollow-uptorarecat-
egoryexploration,rarecategoryexploitationaimstolearnfromtheidentifiedexamplesandcap-
turealltherareexamplesinagivendataset.InFigure7,wepresentanexampleofrarecategory
exploitation on a synthetic dataset with one majority class and four minority classes. The key
observations are as follows: (1) the distribution of the majority class is smooth and (2) the sup-
port regions of the four minority classes are compact. That is, instances in each minority class
are self-similar and form a compact representation. In the past decades, the question of how to
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:14 D.ZhouandJ.He
Fig.7. Anexampleofrarecategoryexploitationwithonemajorityclassandfourminorityclasses[54].The
labeledminorityclassexamplesareshowningreen,thelabeledmajorityclassexamplesareshowninred,
andtheunlabeledexamplesareshowninblack.
explorethecompactnessofrarecategorieshasattractedconsiderableinterestfromthedatamining
and machine learning communities. In this section, we delve into the problem of rare category
exploitation under two scenarios: (1) homogeneous data and (2) heterogeneous data. Whereas
in the former setting, data are collected from the same source and represented in the same for-
mat in the latter setting, we aim to capture rare examples in the presence of data and task
heterogeneity.
3.1 HomogeneousRareCategoryExploitation
Formally,weletX andY denotethesamplespaceandlabelspace,respectively.Wearegivena
dataset D = {D ,D }, where D = {(x )}Nl consists of N obtained annotated samples, D =
l u l i i=1 l u
{(x )}Nu denotesN unlabeledexamples,andx ,x ∈ X,y ∈ Y.Itisoftenthecasethat,dueto
j j=1 u i j i
the (C1) rarity and label (C2) scarcity challenges, annotated data N are scarce. In rare category
l
exploitation, our goal is to produce a prediction function f(·) : X → Y by learning from D
l
and to accurately characterize unknown rare category examples in D . Given this, we present
u
thefollowingdefinitionofrarecategoryexploitationinthehomogeneoussetting.Inthisproblem
setting,wemainlystudy(C1)rarity,(C2)labelscarcity,(C3)non-separability,and(C5)dynamics
inRCA.
Problem2. HomogeneousRareCategoryExploitation.
Given:adatasetD = {D ,D }withscarcelabeledexamplesD = {(x )}Nl andextensiveunla-
l u l i i=1
beledexamplesD = {(x )}Nu.
u j j=1
Find:(i)apredictionfunction f(·) tocharacterizerarecategoryexamples,(ii)asetofunlabeled
examplesthatarelikelycomingfromtherarecategories.
We categorize the current approaches to homogeneous rare category exploitation as either
global or local. Thefirstcategoryaims to capturetheglobal datadistributionforcharacterizing
rarecategories,whereasthesecondcategoryfocusesonexploringrarecategorieswithinasingle
orafewlocalregions(e.g.,theneighborhoodoftheidentifiedrarecategoryexamples).
3.1.1 GlobalApproaches. Thiscategoryofapproachesexploitsboththelabeledandunlabeled
examples to learn the class-membership distribution. Essentially, these methods transform the
rarecategoryexploitationproblemintoaclassificationproblemwithhighlyskeweddatadistribu-
tion. However, unlike the well-studied imbalanced classification problem that aims to maximize
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:15
theoverallclassificationaccuracy(majorityclassesandminorityclasses),rarecategoryexploita-
tionemphasizeslearningandcharacterizingtheminorityclasses.Earlyrarecategoryexploitation
workaddressesthe(C1)rarityand(C3)non-separabilitychallenges.Onerepresentativeapproach
ishyper-ball-basedrarecategoryexploitation[54,55].Thekeyideabehindapproachesistofor-
mulate rare category exploitation as an optimization problem: minimizing the radius R of the
hyper-ball that well encloses the rare categories. The general objective function for the binary
case(i.e.,onemajorityclassandoneminorityclass)canbewrittenasfollows.
min R2 (11)
R,c
s.t.,(cid:5)x −c(cid:5)2 ≤R2,x ∈ Dmaj
i i l
(cid:5)x −c(cid:5)2 ≥R2,x ∈ Dmin
j j l
(cid:5)x −c(cid:5)2 ≥R2,x ∈ D
k j u
whereRdenotestheradiusofthehyper-ball,c
denotesthecenterofthehyper-ball,Dmaj
denotes
l
the set of labeled majority class examples, and Dmin denotes the set of labeled minority class
l
examples. Moreover, to ensure the compactness of the hyper-ball, the authors introduce three
constraintsontheoptimizationproblem:(1)thelabeledexamplesfromthemajorityclassesshould
beoutsideofthehyper-ball;(2)thelabeledexamplesfromtheminorityclassshouldbeinsideof
thehyper-ball;and(3)thehyper-ballshouldencloseasmanyunlabeledexamplesaspossible.To
tacklethenon-separabilitychallenges,RACH[54]providesarelaxedsolutionofEquation(11)by
introducingslackvariablestoallowthemiss-classifiedinstancesandthenconvertingtheproblem
intoaconvexoptimizationproblem.Therelaxedproblemcanbeeasilysolvedinitsdualformvia
theprojectedsubgradientmethod.FollowingHeetal.[54],Heetal.[55]introducesakernelized
rarecategoryexploitationalgorithmthat,generalizesRACHtomodelcomplexshapesofthetarget
rarecategories’supportregionsbyprojectingtothehigh-dimensionalfeaturespaceinducedby
kernels.Thekernelmethodprovidesmoreflexibilitywhencharacterizingcomplexrarecategories
inreal-worldapplications.
Severalmorerecentstudiesconsidertheproblemofrarecategoryexploitationinthepresence
of(C2)scarceandnoisylabels.Haqueetal.[46],studytheproblemofnovelclassclassificationon
datastreams.Insteadofrelyingonredundanthuman-annotatedlabelsorpriorknowledge,they
propose a semi-supervised framework to track the confidence changes of classifiers in order to
detectthenovelconceptdriftsandthusidentifythenovelclasses.Zhouetal.[166]proposeabi-
levellearningmechanism(showninFigure8)inwhich,ateachermodel(i.e.,curriculumlearning
scheme)graduallyaugmentsthetrainingsetwithpseudolabels,andthestudentmodel(i.e.,rare
categorycharacterization)returnsthepredictionresultstogetherwiththepredictionconfidence
totheteachermodel.Ingeneral,theteachermodelandthestudentmodelaretrainedinamutu-
ally beneficial way, enabling the model to achieve better prediction accuracy in both rarity and
label scarcity. Any real-world applications (e.g., video classification [162]), in addition featuring
labelscarcity,comewithcomplexdataandnoisylabels,whichrequiremachinelearningmodels
to be trained with only weak supervision [172]. Zhong et al. [162] propose a GCN to clean the
noisylabels.TheGCN-basedlabelnoisecleanerisdesignedtoprovidesupervisorysignalsfrom
high-confidencesnippetstolow-confidencesnippets,suchthattheclassifiercanbetrainedwith
“clean”supervision. Xietal.[144]studytheproblemofonlinetransactionfrauddetection.Tohan-
dlethenoisyandcomplexuserbehaviorinformation,theydevelopthedualimportance-aware
factorizationmachine(DIFM)thatcapturesfieldvaluevariationsandfieldinteractionssimulta-
neouslytosupportonlinetransactionfrauddetection.Linetal.[82]proposeamulti-resolutionrare
categoryexploitationapproachtoidentifyinstancesofonlinecreditpaymentfraudsatdifferent
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:16 D.ZhouandJ.He
Fig.8. Aconceptualframeworkofbi-levellearningforrarecategoryexploitation[166]thatiscomposedof
astudentlearningmodelandateacherlearningmodel.Thedashedarrowsindicatethelearningprocessof
theteachermodelthataimstogeneratepseudolabels;thesolidarrowsindicatethelearningprocessofthe
studentmodelthatisdesignedtopredictrarecategoryexamples.
granularities.Wuetal.[143]studyrarecategoryexploitationundervariousdatacontamination,
by proposing an information-theoretic bound of performance degradation in terms of the data
contaminationratio.
3.1.2 Local Approaches. The local algorithms are also referred to as seeded or targeted algo-
rithms[56,112,151,170].Thiscategoryofapproachesessentiallytacklesrarecategoryexploita-
tionasalocalclusteringproblem.Thekeyideaistotreatthelabeledexamplesasseedsandreturna
compactclusterneartheseedexampleswithoutexploringthewholedataset.Azmandianetal.[16]
present a local kernel density ratio feature selection framework that seeks a salient feature sub-
space in which the normal data points form a high-density region and the rare examples form
a low-density region. In the learned subspace,therare examples stand out and are easily distin-
guishedbydetectionalgorithms.SpielmanandTeng[124],presentadesignofalocalclustering
algorithm for massive graphs. The local algorithm is able to find a compact local cluster near a
seedexampleandtherunningtimeisnear-linearwithrespecttothesizeofthereturnedcluster.
Andersenetal.[11],deriveamixingresultforPageRankandproposeafastapproximationmethod
to compute PageRank vectors. Using this method, the authors develop an improved local graph
partitioningalgorithmthatenablespolylogarithmictimecomplexitywithrespecttothenumber
of edges in the given graph. Pang et al. [107] propose a local and interactive rare event detec-
tionalgorithm,thatleveragesthefeedbackfromananomaly-biasedsimulationenvironmentand
continuouslyupdatesthelearnedabnormalitytonovelrarecategories.
Although the conventional local clustering algorithms are primarily designed for low-order
connectivity patterns (e.g., edge in Table 1), many applications exhibit high-order connectivity
patterns(e.g.,starinTable1).Forexample,theloop-shapedstructureplaysasignificantroleinde-
tectingcommunitiesinuser-itemnetworks[170];aclusterofstar-shapedstructuresoftenserves
a red flag indicating potential instances of synthetic ID fraud in the personal identifiable in-
formation (PII) networks [102]. To account for the crucial high-order connectivity patterns in
real-worldsystems,Zhouetal.[170]andYinetal.[152]offerinnovativestudiesoftheproblemof
localhigh-ordergraphclustering.Inparticular,theauthorsintroducethenotionofhigh-ordercon-
ductanceandthehigh-orderdiffusionkernelwiththehigh-orderMarkovchainastheunderlying
model, which allows end-users to model various types of high-order structures. Moreover, they
generalizethewell-knownlocalclusteringalgorithms[11,124]tothehigh-ordersettingandpro-
vide a theoretical analysis of the effectiveness and scalability of the proposed algorithms. Many
recent studies study the high-order connectivity patterns in more complicated scenarios, such
as modeling evolving high-order structures on fine-grained temporal networks [165], capturing
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:17
Table1. IllustrativeExamplesofHigh-OrderConnectivityPatternsandLocalClusteringAlgorithms
ConnectivityPatternN Illustration OrderofN ClusteringAlgorithms Applications
Vertex 1st-order N/A N/A
Edge 2nd-order 1st-order Rarecategorydetection[53]
3-nodeLine
3rd-order 2nd-order Socialcommunitydetection[71]
Triangle
k-nodeStar kth-order (k−1)th-order Syntheticidentitydetection[102]
higher-orderclustersinheterogeneousnetworks[23],andtrackinghigh-orderstructuresontime-
evolvinggraphs[38].
3.2 HeterogeneousRareCategoryExploitation
Intheeraofbigdata,manyapplicationdomainsexhibitmultipletypesofheterogeneity,including
dataheterogeneitythatoriginatesfrommultipleinformationsourcesandtaskheterogeneitythat
originatesfrommultipleapplicationdomains.Inthissubsection,weorganizetheexistingworkin
thecontextofdataheterogeneityandtaskheterogeneity.
3.2.1 Dataheterogeneity. Learningfromdataheterogeneityisoftenreferredtoasmulti-view
learning, as the data are collected from different sources, enabling multiple views. In the data
heterogeneitysetting,rarecategoryexploitationbecomesevenmorechallengingthaninthedata
homogeneitysettingduetotheexistenceofmultipleviews.Itiscrucialtoleveragemultipleviews
and identify the relevant features for distinguishing between the majority and minority classes.
With the aim of addressing (C1) rarity, (C2) label scarcity, and (C4) data heterogeneity in rare
categoryanalysis,weformallydefinetheproblemasfollows:
Problem3. Multi-ViewRareCategoryExploitation.
Given:(i)adatasetD collectedfromV views;(ii)asmallsetoflabeledexamplesD = {(x )}Nl .
l i i=1
Find:(i)apredictionfunction f(·) tocharacterizerarecategoryexamples,(ii)asetofunlabeled
examplesthatarelikelycomingfromtherarecategories.
ApivotalstepinaddressingProblem5istoleverageviewconsistencyandlearnaunifiedrep-
resentation to improve the performance of rare category exploitation. In the past decades, re-
searchers have proposed extensive multi-view learning frameworks [9, 40, 63, 64, 78, 79, 79, 91,
122,157,160]foranomalydetectionthatcouldpotentiallysolveProblem5.However,thesemeth-
odsaremostlyunsupervisedand/orbasedonsomeheuristicfunctions,whichmeansthemethods
mightnotwellcapturethecharacteristicsofrarecategories.MUVIR[163]isoneoftheprincipled
effortsthathasbeenproposedtoaddressProblem5.MUVIRprovidesagenericrarecategoryde-
tectionsolutionthatisabletointegratetheexistingsingle-viewrarecategoryexploitationmodels
inordertocomputetheoverallposteriorprobabilityofeachexample.Thekeyideaistoexploitthe
relationshipamongmultipleviewsandestimatetheoverallposteriorprobabilityofexamplescom-
ingfromrarecategoriesgivendatafrommultipleviews.Inparticular,givendatawithmulti-view
features, one can trainV distinct rare category exploitation models uponV views and compute
view-specific posterior probability P(y = rarecategory|xv) with respect to thevth view. The
authorsproposethefollowingtheoremtoeffectivelyintegrateview-specificposteriorprobability
P(y =rarecategory|xv)inamodel-agnosticway:
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

| 123:18 |     |     |     |     |     | D.ZhouandJ.He |     |
| ------ | --- | --- | --- | --- | --- | ------------- | --- |
Theorem 3.1 ([163]). If the features from m(cid:6)ultiple views have weak dependence given the class
|          | [1],i.e.,P(x|y =rarecategory) | ≥α  | V P(xv|y | =rarecategory),α |     |         |     |
| -------- | ----------------------------- | --- | -------- | ---------------- | --- | ------- | --- |
| labely i |                               |     | v=1      |                  |     | >0,then |     |
(cid:6)
|     |                      | (cid:7)V |                       |     |                 | V P(xv)(cid:9) |      |
| --- | -------------------- | -------- | --------------------- | --- | --------------- | -------------- | ---- |
|     |                      | (cid:7)  |                       |     | (cid:9)×(cid:7) | v=1            |      |
|     | P(y =rarecategory|x) | ≥C       | P(y =rarecategory|xv) |     |                 |                | (12) |
P(x)
|        |                  | (cid:8) v=1 |     |     | (cid:10) (cid:8) | (cid:10) |     |
| ------ | ---------------- | ----------- | --- | --- | ---------------- | -------- | --- |
| whereC | = α isaconstant. |             |     |     |                  |          |     |
(p2)V−1
= rarecategory|x)
UsingTheorem3.1,theoverallposteriorprobabilityP(y canbeapproxi-
matedasfollows:
(cid:6)
|     |     | (cid:7)V |     |     | V   | d   |     |
| --- | --- | -------- | --- | --- | --- | --- | --- |
(cid:7) v=1 P(xv)(cid:9)
|     | P(y =rarecategory|x) | =   | P(y =rarecategory|xv) |     |              |          | (13) |
| --- | -------------------- | --- | --------------------- | --- | ------------ | -------- | ---- |
|     |                      |     |                       |     | (cid:8) P(x) | (cid:10) |      |
v=1
wherethemarginalprobabilitiesP(x)andP(xv)canbeestimatedviakerneldensity,anddisanon-
negativeparameterthatbalancestheimportanceofthetermrelatedtothemarginalprobabilities.
AmodifiedversionofMUVIRhasbeenproposedforhandlingproblemswhentheexactpriorsofmi-
norityclassesareunknown.Inthepastfewyears,researchershaveexploredmanyhigh-impactap-
plicationsofrarecategoryexploitationthatcanbeformulatedasmulti-viewrarecategoryexploita-
tionproblems.Amongthem,Leeetal.[75]proposeanattention-basedvisualquestion-answering
network to jointly model the input images and corpora and identify system errors or abnormal
events;Chenetal.[29]studytheproblemofmulti-modalvideoanomalydetection,proposinga
bi-directional predictive network to regularize the prediction task from pixel-wise, cross-modal,
and temporal-sequence levels; and Shen et al. [123] propose an anomaly segmentation network
forlocalizingdefectiveareasinlarge-scaleindustrialmanufacturingenvironments.
Another group of approaches to multi-view rare category exploitation consist of the semi-
supervised classification models. For example, Nie et al. [104] propose a multi-view framework
withadaptiveneighborhoodlearning.Theframeworkintegratesmulti-viewclusteringandsemi-
supervised classification, which allows learning attention for each view automatically. Zhang
etal.[156]developamulti-viewrarecategoryexploitationframeworkforAlzheimer’sdiseasedi-
agnosis.Theyproposeamulti-layermulti-viewframeworkthatautomaticallyconstructsashared
latentrepresentationacrossmultipleviewsandlearnsthemappingfunctionsfromthemulti-view
featurestothepredictionlabels.WangandLan[138]assumethemultipleviewsofthemajority
class examples are drawn from a unique distribution with different projection functions. Given
thisassumption,theauthorsproposeahierarchicalBayesianmodelthatcomputestheoutlierness
ofunlabeledsamplesandthusidentifiesrareexamples.
3.2.2 Task heterogeneity. This subsection provides an overview of the rare category exploita-
tionalgorithmsthathavebeenproposedinthecontextoftaskheterogeneity.Formallyspeaking,in
thepresenceofmultipletasks,wearegivenadatasetD={D1∪...∪DS}thatcomesfromSapplica-
tionsdomains,andasmallsetoflabeledexamplesfromeachtaskDs={(xs)}N s
|     |     |     |     |     |         | l ,whereNs | denotes |
| --- | --- | --- | --- | --- | ------- | ---------- | ------- |
|     |     |     |     |     | l i i=1 | l          |         |
thenumberoflabeledexamplesinDs.Ourgoalistocapturethemultimodalitiesfromdifferent
tasksanddomainsandlearnapredictionmodeltoaccuratelycharacterizetherarecategoriesfrom
different tasks and domains. The problem, which aims to address (C1) rarity, (C2) label scarcity,
(C3)non-separability,and(C5)dynamicsinrarecategoryanalysis,iscommonlydefinedasfollows:
| Problem4. | Multi-taskRareCategoryExploitation. |     |     |     |     |     |     |
| --------- | ----------------------------------- | --- | --- | --- | --- | --- | --- |
Given:(i)adatasetD = {D1∪...∪DS},whereDs isthedatasetforthesthtask,s = 1,...,S;
|                                              |     |     |     | {(xs)}N s |     |     |     |
| -------------------------------------------- | --- | --- | --- | --------- | --- | --- | --- |
| (ii)asmallsetoflabeledexamplesfromeachtaskDs |     |     |     | = l       | .   |     |     |
i i=1
|     |     | f(·) tocharacterizerarecategoryexamplesineachtaskDs,(ii)a | l   |     |     |     |     |
| --- | --- | --------------------------------------------------------- | --- | --- | --- | --- | --- |
Find:(i)apredictionfunction
setofunlabeledexamplesthatarelikelycomingfromtherarecategoriesineachtaskDs.
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:19
The past decades have produced much literature studying Problem 4. This literature can be
categorizedinoneoftwowaysbasedonitsobjectives.Thefirstcategoryaimstolearnamixture
ofpredictionfunctionsthatmaximizetheoverallaccuracyacrossalltasks.Forexample,Yangetal.
[146]studytheproblemofrarecategoryexploitationinthepresenceofmultipletasksandmultiple
viewsbyproposingajointoptimizationframeworkcalledM2LID.Theauthorsstartfromametric
calledborderdegreethatisusedtocapturethesharpchangesindensityneartheboundaryofrare
categoriesinthefeaturespace:
BorderDegree(x) =Hub(x)−Authority(x) (14)
where Hub(x) and Authority(x) indicate the hub value and authority value [70] of example x,
correspondingly.Intuitively,thelargertheborderdegreeis,thehighertheprobabilitythatxbe-
longstotherarecategory.Tomodeltaskrelatednessandviewconsistency,theythenformulate
the problem by requiring (1) task-specific learners to behave similarly on the features, (2) view-
based learners to behave similarly on the examples, and (3) the border-degree to be negatively
correlated with the prediction confidence score. Finally, to solve the optimization problem, they
develop a block-coordinate-descent-based method to iteratively update the boundary character-
istics of rare categories and multiple classification functions for different tasks. [62] propose a
multimodel learning algorithm that is based on a mixture of sparse Gaussian graphical models.
[161] aims to tackle the Problem 4 in the presence of data scarcity and adversarial attacks. The
authorsproposeafederatedlearningframeworkthatperformsmultipletaskssimultaneously.
The second category is also referred to as transferable rare category exploitation. Instead of
learning an optimal predictor for all tasks, transferable rare category exploitation heavily em-
phasizes the target tasks. Some typical works includes [8], [12], [72], [129], and [136]. In Appel
etal.[12],theauthorssystematicallyevaluatetheperformanceofanomalydetectionframeworks
using two types of transfer representation learning paradigms: (1) transfer learning from pre-
trained networks, and (2) transfer learning from auxiliary tasks. Kumagai et al. [72] develop an
autoencoderframeworkthatlearnsthedomain-specificlatentvectorsandthusimprovestheper-
formanceindetectingrareexamples.Unlikemosttransferlearningmodelsthataimtolearnthe
transferablerepresentationfor thetarget domain, the work of Vercruyssenet al. [136] proposes
to select a subset of labeled and relevant examples from the source domain to augment the tar-
gettasks. Theaforementionedmethodsallassumethetargetdomainsarerelatedtothesource
domains.However,thereisamorechallengingscenario:theso-calledout-of-distributionrarecat-
egory exploitation, wherein the test data are unseen or from shifted distributions. To handle the
out-of-distributionscenarios,MortezaandLi[98]proposeananalyticalframeworkwithprovable
guarantees to characterize and understand out-of-distribution detection in open-world applica-
tions.SunandWang[128]proposeanadaptivein-out-awarelearningframeworktojointlymodel
themixedin-distributionandout-of-distributiondatasamples.Acharyaetal.[2]proposeagraph
contextreasoningnetworkforout-of-distributionobjectdetectionbyconstructingarepresenta-
tiongraphandacontextgraphfromtheinputimage.
4 UNDERSTANDINGRARECATEGORIES
Although they have been tremendously successful in exploring and exploiting rare category ex-
amples,manyadvancedmethods,especiallydeeplearningmodels,oftenremainblack-boxinna-
ture. This poses a challenge to their application in industries that have to follow highly regu-
lated processes. In these industries, prediction models must be interpretable and the output re-
sultsarerequiredtomeetcompliancestandards.Therefore,anaturalresearchquestionishowto
make existing models transparent to the end-user by identifying the right context (e.g., key fac-
tors,representativeentities,criticaltimestamps).Inthissection,wesystematicallydiscusshowto
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:20 D.ZhouandJ.He
Fig.9. Rare-category-orientednetworkrepresentation:themajorityandminorityclassesarenotseparable
intheoriginalfeaturespace,butbecomewellseparatedintheembeddingspace[166].
understandrarecategorypatternsfromthefollowingtwodirections:(1)rarecategoryrepresen-
tationand(2)rarecategoryinterpretation.Thefirstdirectionaimstodiagnosefromthedataper-
spective(i.e.,How isthedata distributed?Whichpieceof informationismostvaluable fora given
task?),whiletheseconddirectionaimstodiagnosefromthemodelperspective(i.e.,Whydoesthe
modelmakeacertainpredictiononaparticularpieceofinformation?).
4.1 RareCategoryRepresentation
In this task, we aim to learn a rare-category-oriented embedding representation such that the
rare examples (e.g., security threats) are well separated from the majority classes (e.g., normal
activities).Figure 9 presentsa typicalexample of rarecategoryrepresentationlearning wherein
themajorityclassandtheminorityclassareoverlappedtogetherintheoriginalfeaturesspacebut
becomeseparatedinthelearnedembeddingspace.Formallyspeaking,theproblemcanbedefined
asfollows:
Problem5. RareCategoryRepresentation.
Given:(i)adatasetDthatconsistsofnsamples;(ii)asmallsetoflabeledexamplesD = {(x )}Nl ;
l i i=1
(iii)theuser-definedembeddingdimensiond.
Find:(i)ararecategoryrepresentationmodelд(·);(ii)ad-dimensionalembeddingrepresentation
E∈Rn×d
thatwellpreservestheunderlyingdistributionofrarecategories.
Inthepastdecade,extensiveworkhasbeendonetodeveloprepresentationlearningmethodsto
learntheunderlyingdistributionoftherarecategorypatterns.Thekeyideabehindthesemethods
istotrackthe“footprints”ofrarecategoriesviaexternalinformation(e.g.,supervisionfromora-
cles)orpriorknowledge(e.g.,featuresindicatinglocaldensitychanges[52,147])andthenleverage
thisinformationtoregularizetherepresentationlearningmodelstoextractlow-dimensionaland
salient embedding for rare category analysis. For instance, Akoglu and Falioutsos [5] propose a
set of egonet features (e.g., weighted and unweighted in- and out-degree, number of neighbors,
numberoftriangles)fromeachsnapshotofthegraphsequencetomodelthe“behavior”ofeach
node.Thesefeaturesareeffectiveinspottingrarecategoryexamples.Manzooretal.[90]aimto
spotanomalouspatternsinastreamofheterogeneousgraphscontainingdifferenttypesofnodes
andedgesbyproposingaclustering-basedanomalydetectionapproachthatcansimultaneously
addresstheheterogeneityandstreamingnatureoftheinputdata.Inparticular,Manzooretal.in-
troduceanovelembeddingmechanismthatcanencodetheheterogeneousstreaminggraphinto
avectorrepresentationthatisthenusedtoperformclusteringandidentifyanomalouspatterns.
Huangetal.[60]studytheproblemofimageclassificationwhendatainthevisiondomainexhibit
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:21
Fig.10. Preliminaryresultscomparingnetworkembeddingusingvariousalgorithms[166].
a highly skewed class distribution by learning a deep representation such that rare categories
are easily separable from the majority class by contemporary classification methods. In particu-
lar, this article first proposes to learn the data representation by maintaining both inter-cluster
andinter-classmarginsthatreducetheclassimbalanceinherentinthelocaldataneighborhood.
TheproposedframeworkisbuiltbasedonaConvolutionalneuralnetwork(CNN)framework
throughaquintupletsamplingschemeandtheassociatedtriple-headerhingeloss.
Morerecently,duetothenotablesuccessofnetwork-embeddingapproaches,variousnetwork-
embedding-based approaches have been proposed for rare category analysis. For example,
SPARC [166] is one of the first rare-category-oriented network embedding frameworks. SPARC
aimstolearnasalientrepresentationtocharacterizerarecategoryexamples.Inspiredbythefamily
ofcurriculumlearningthatsimulatesthecognitivemechanismsofhumanbeings,SPARC gradu-
allyselectsthekeynetworkcontextualinformationandlearnstherare-category-orientednetwork
representationbyshiftingfromthe“easy”concepttothe“difficult”concept.Theresultsshowthat
(1)SPARC enablesuserstovisualizethenetworklayoutinasalientembeddingspace,wherethe
majority classes and minority classes are well separated; and (2) SPARC is able to identify valu-
ablecontextualinformationthatprovidesinterpretationandguidanceinthetaskofrarecategory
characterization. Here we compare SPARC with three state-of-the-art network embedding algo-
rithms,includingtwounsupervisedmethods,i.e.,DeepWalk[111]andLINE[130],andonesemi-
supervisedmethod,i.e.,PLANETOID[148].Wefirstmapthegivennetworktoa129-dimensional
spacewithdifferentembeddingmethods.Then,weemploythenonlineardimensionalityreduction
method,i.e.,t-SNE[88],toencodeexamplesinatwo-dimensionalspaceforbettervisualization,
asshowninFigure10.Weobservethattherareexamplesarebetterclusteredusingtheproposed
methodthananyofthebaselinemethods.
FollowingSPARC,Wuetal.[142]proposeabiasedrandomwalkmodelnamedVDRW forlearn-
ing imbalanced network representation.VDRW is designed to dynamically adjust the transition
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:22 D.ZhouandJ.He
Fig.11. UserinterfaceofRCLens,whichiscomposedofthreekeymodules:thedataexplorermodule(shown
insubfigurea),thefeatureexplorermodule(showninsubfigureb),andthecategoryexplorermodule(shown
insubfigurec).
probabilitymatrixeachtimeanodeisvisitedbytherandomparticle.ViaVDRW,Wuetal.propose
apairofsamplingstrategies,i.e.,contextsamplingandbalanced-bathsampling,tolearnnetwork
representationusingskip-grammodel[94].NetWalk[155]isdevelopedforrareeventdetectionby
learningthenetworkrepresentations,whichcanbeupdateddynamicallyasthenetworkevolves.
NetWalkfirstextractsthedynamicnetworkcontextandencodestheverticesofthedynamicnet-
worktoalow-dimensionalrepresentation.Then,aclustering-basedschemeisemployedtoincre-
mentallyanddynamicallytrackthemaliciouspatternsinthedynamicnetworks.Dengetal.[34]
proposeaGCN-basedframeworkforpredictingfutureeventsbycapturingcontextualinformation
fromtherawdata.Theproposedframeworkfirstextractsgraphrepresentationsoftheeventsdoc-
umentsand,thenlearnstopredicttheoccurrenceoffutureeventsandidentifyeventsofinterest
(e.g.,anomalypatterns).
4.2 RareCategoryInterpretation
Interpretabilityinmachinelearningmodelsplaysacrucialroleinmanyhigh-impactdomainsand
rare category analysis. In this task, we aim to characterize the rare categories with a predictive
modelandinterprettheoutputfromthismodelbyprovidingrelevantclues,suchasconnectivity
patterns, data sources, features, and timestamps from time-series data. We define the problem
settingasfollows:
Problem6. RareCategoryInterpretation.
Given:(i)adatasetD thatconsistsofnsamples,(ii)ararecategoryanalysismodel f(·).
Find:interpretationovertheoutputfrom f(·)onD.
Despitetherichliteratureinthecontextof explainableartificialintelligence(XAI)[15,31,
44,61,95,96,131],interpretingrarecategoryanalysismodelsremainschallengingforthefollow-
ing reasons: (1) rare category analysis models are naturally “biased” (i.e., focusing on minority
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:23
Fig. 12. User interface of RCAnalyzer, which is composed of (a) the timeline view; (b) the matrices view;
(c) the instance view; (d) the sub-network view; (e) the label result view; (f) the parameter panel; (g) the
encodingpanel;and(h)theinformationpanel.
patterns instead of the overall data distribution), (2) rare category analysis model f(·) is
often trained with scarcity labels, and (3) the learning process of rare category analysis
model f(·) may frequently involve oracles and operate in a human-in-the-loop fashion (see
Figure 5 for rare category exploration). Simply replacing f(·) with a conventional interpretable
machine learning models may deteriorate the prediction performance by providing misleading
characterizationsorinjectingadditionalbias[74].
There have been a few attempts in the visualization domain to address Problem 6 given the
aforementionedchallenges.Forexample,RCLens[81]isaninteractivevisualanalyticsystemthatis
designedtoexploreandidentifyrarecategoryexampleswiththeguidanceofend-users.Figure11
presentstheuserinterfaceofRCLens,whichactivelyvisualizesandinterpretsthethreelearning
phases of rare category analysis models to end-users. In the data exploration phase (shown in
subfigurea),thesystemconductsapersonalizedvisualizationofthedataviaadataqueryingand
filtering mechanism; in the feature selection phase (shown in subfigure a), the system provides
relevantcluesandstatistics(e.g.,correlationsoffeatures)forend-userstoinvestigatethefeature
dimensions;andintherarecategoryanalysismodel(showninsubfigurec),thesystemvisualizes
theidentifiedrarecategoriestoend-usersandthenrefinesthepredictionsbyleveragingtheusers’
feedback.
Pan et al. [105] proposes a visual analytic system named RCAnalyzer for studying rare cate-
gorypatternsindynamicsystems.TheuserinterfaceofRCAnalyzer isshowninFigure12,which
includes (a) the timeline view showing an overview of the given dynamic networks; (b) the ma-
tricesviewshowingtheneighborhoodcontextualinformationofeachnode;(c)theexampleview
showingthefeaturedistributionofrarepatterns;and(d)thelabelresultviewshowingthehistory
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:24 D.ZhouandJ.He
Table2. PubliclyAccessibleReal-WorldDatasetsforRareCategoryAnalysis
| DataType    | Dataset         | DescriptionofRareCategories |
| ----------- | --------------- | --------------------------- |
| TabularData | 20NewsGroup[68] | Raretopicsofnewspapers      |
TabularData Donors[106] OutstandingprojectsproposedbyK-12teachers
TabularData Census[35] High-incomepeopleinU.S.censusbureaudatabase
| TabularData | Fraud[114]    | Fraudulentcreditcardtransaction |
| ----------- | ------------- | ------------------------------- |
| TabularData | UNSW-NB15[99] | Networkintrusion                |
| TabularData | URL[86]       | MaliciousURLs                   |
TabularData Campaigndata[35] Rarelysuccessfulcampaigningrecords
| TabularData     | Thyroid[35] | Raredisease                 |
| --------------- | ----------- | --------------------------- |
| Time-seriesData | Vandal[73]  | Wikipediavandalwarning      |
| Time-seriesData | Spam[139]   | Webspams                    |
| Time-seriesData | HDFS[145]   | Systemerrors                |
| GraphData       | Tox21[87]   | Toxicenvironmentalchemicals |
| GraphData       | ENZYMES[19] | Abnormalproteins            |
| GraphData       | NCI1[137]   | Abnormalchemicalcompounds   |
predictionresultsaswell as themodel diagnosis. To ensuretheinterpretabilityof rarecategory
analysismodels,thesystemisabletoactivelyvisualizeeachidentifiedrareexampleincontext(e.g.,
neighborhoodstructuresintheadjacenttimestamps)tohelporaclesunderstandandexaminethe
predictionresults.
5 DATASETSANDREPRESENTATIVEMETHODS
Thissectionsummarizesthepopularevaluationdatasetsandrepresentativealgorithmsacrossdif-
ferentdatatypesanddownstreamtasks.
5.1 Datasets
Although rare categories are prevalent across various domains (e.g., finance), collecting and an-
notatingrareexamplesisextremelytime-consumingandlabor-intensive(e.g.,annotatingmoney
launderingactivities).Earlystudies(e.g.,[48,50,52,53,109])evaluatetheirmodelsonsynthetic
or semi-synthetic datasets that are either generated from a pre-defined data distribution or ma-
nipulatedfrompublicbenchmarkdatasets.However,evaluationsperformedonsyntheticorsemi-
syntheticdatasetsmaynotreflecttheperformanceofrarecategoryanalysismodelsinreal-world
applications.Topromotethefurtherdevelopmentofrarecategoryanalysis,Table2summarizes
some public benchmark datasets, whose data range from tabular data to graph-structured data,
fromstaticdatatodynamicdata.
5.2 RepresentativeMethods
Comparison evaluation with representative algorithms serves a pivotal role in the development
ofmachinelearningalgorithms.InTable3,weenumerateandsummarize25representativerare
category analysis algorithms w.r.t. data type (i.e., tabular data, time-series data, graph data) and
downstreamtask(i.e.,exploration,exploitation,representation,andvisualization).Sincethemeth-
ods in Table 3 have been developed for diverse tasks and datasets, we are unable to provide
a meta-analysis of their performance in a unified setting. Instead, to provide insight and an
in-depth understanding of the methods, we summarize our major observations as follows: (i)
most methods are designed in an unsupervised or semi-supervised setting, (ii) sampling-based
methods [135, 163] and anomaly-detection-based methods [132, 158] are still the mainstream
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:25
Table3. RepresentativeAlgorithmsinDataPerspective
| DataType        | Algorithm          | Task                      |
| --------------- | ------------------ | ------------------------- |
| TabularData     | NNDB[52]           | RareCategoryExploration   |
| TabularData     | ACT [141]          | RareCategoryExploration   |
| TabularData     | SEDER[50]          | RareCategoryExploration   |
| TabularData     | HMS[135]           | RareCategoryExploration   |
| TabularData     | MUVIR[163]         | RareCategoryExploitation  |
| TabularData     | RACH [54]          | RareCategoryExploitation  |
| TabularData     | MLAN [104]         | RareCategoryExploitation  |
| TabularData     | RCLens[81]         | RareCategoryVisualization |
| Time-seriesData | SUITS[80]          | RareCategoryExploration   |
| Time-seriesData | CDLC [18]          | RareCategoryExploration   |
| Time-seriesData | MatrixProfile[150] | RareCategoryExploration   |
Time-seriesData BIRAD[164] RareCategoryExploration&Exploitation
| Time-seriesData | RRCF [43]     | RareCategoryExploration      |
| --------------- | ------------- | ---------------------------- |
| Time-seriesData | Sand [46]     | RareCategoryExploitation     |
| GraphData       | Oddball[6]    | RareCategoryExploration      |
| GraphData       | NrMF [132]    | RareCategoryExploration      |
| GraphData       | HiDDen[158]   | RareCategoryExploration      |
| GraphData       | FocusCO[110]  | RareCategoryExploration      |
| GraphData       | BIRD[168]     | RareCategoryExploration      |
| GraphData       | StreamSpot    | [90] RareCategoryExploration |
| GraphData       | AnomRank[153] | RareCategoryExploration      |
GraphData SPARC [166] RareCategoryExploitation&Representation
| GraphData | HOSPLOC    | [170] RareCategoryExploitation  |
| --------- | ---------- | ------------------------------- |
| GraphData | L-MEGA[38] | RareCategoryExploitation        |
| GraphData | RCAnalyzer | [105] RareCategoryVisualization |
solutionsinrarecategoryexploration,and(iii)rarecategoryvisualizationandinterpretationare
underexplored.
6 CONCLUSIONANDFUTUREDIRECTIONS
Departingfromtheprevioussurveys,thisarticlepresentedacomprehensivepipelineofrecentad-
vancesinrarecategoryanalysis.Westartedfromthede-novostepwithoutanylabelinformation
and surveyed rare category exploration techniques in the setting of homogeneous data and het-
erogeneousdata.Then,wereviewedrarecategoryexploitationmethodsthataimtocharacterize
acompactrepresentationoftheminorityclassesinordertodiscoveralltherareexampleswith
highaccuracy.Finally,wediscussedtheproblemofrarecategoryexplanation,andinparticular,
how to learn a salient representation of rare categories and interpret the prediction results. De-
spitethesignificantdevelopmentsinrarecategoryanalysis,thereremainsomeexcitingresearch
opportunities
•
RareCategoryGeneration.Tomeetthedramaticallyincreasingdemandformachinelearning
systemsasserviceproviders(e.g.,socialnetworking,onlineadvertising,datasecurity),amas-
siveamountofdatahasbeengeneratedandcollectedfromavarietyofdomains.However,
thecollectedraredataareoftennoisy,sparse,few-shotannotated,andevolvingovertime.
Directly training machine learning models from the raw data would introduce inevitable
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:26 D.ZhouandJ.He
model bias and largely degrade the model performance in downstream applications (e.g.,
rare category characterization, rare category explanation). Moreover, the ever-increasing
sizeofdata,togetherwiththedifficultyofreleasingandsharingthem,hasmadedatagener-
ationafundamentalproblemthatiskeyformanyhigh-impactapplications,includingfraud
detection,recommendation,anddatasecurity,amongothers.Hence,itiscriticaltodevelop
deepgenerativemodelsthatenablescalablemodelingofrealdatatoextractkeycontextual
information,distillknowledge,andgenerateplausiblepatternsfordataaugmentationinrare
categoryanalysis.
• Long-TailCategoryAnalysis.Inthepastdecade,deeplearninghasachievedremarkablesuc-
cessinvariouslearningtasks(e.g.,imageclassification,speechrecognition,linkprediction)
throughthetrainingof“bigmodels”on“bigdata.”However,unlikethesewell-studiedtasks
(e.g.,imageclassificationoverdomesticcatsandwildcats)withrichtrainingdata,thevast
majority of real-world entities and patterns (e.g., identification of honest employees and
maliciousinsidersinalargeinstitution)areunderexploredandlacktheobservationaland
annotated data that often correspond to the “long-tail” categories. Unlike existing works
onrarecategoryanalysisthatfocusononeorafewrarecategories,herewefaceamassive
numberofunderrepresentedcategoriesfroma“long-tail”distribution.Moreover,thecurrent
machine learning systems are mostly tailored to specific learning scenarios, prevent them
fromdeliveringontheirpromisesindetectingthetargetsofinterestinthepresenceofdistri-
butionchanges(e.g.,dynamicsystems).Twofundamentalresearchquestionsthusemerge:
(Q1)Howcanwecomprehendsuchmassive“long-tail”categoriesgiventheinherentpaucityof
observationalandannotateddata? (Q2)Howcanwecapturethetargetsofinterest(e.g.,rare
categoryexamples)givenanoveldatadistribution?
• Robust Rare Category Analysis. Robust rare category analysis is another fundamental yet
quiteopenresearchproblemthatisattractingasurgeofattentionfrommanyhigh-impact
domains(e.g.,spamdetection,financialfraud,systemdiagnosis).Forexample,infinancial
frauddetection:Howcanwemeasureentitysensitivity,algorithmicrobustness,taskhardness,
andmodelgeneralization,givenapredictionmodel? Howcanweachieveoperationalrobust-
ness and adversarial robustness in the presence of the external disturbances (e.g., noise, miss-
ingvalues,outliers,adversarialattacks)? Despitetheextensiveworkonadversarialmachine
learning,thevastmajorityofthepreviousstudiesassumeabalanceddatadistributionwhile
neglectingrealisticcasesinwhichthedataarehighlyskewed,andthetargetsofinterestare
underrepresented.Comparedtoconventionalmachinelearningtools,rarecategoryanalysis
modelsaremoresensitiveandvulnerableinthepresenceofadversarialattacksduetothe
rarity,non-separability,andlabelscarcityofrarecategoryexamples.
• Human–AICollaborativeRareCategoryAnalysis.Manyindustriesfollowhighlyregulated
processesthatrequirerarecategoryanalysismodelstobeinterpretableandhumanexperts
tobeinvolvedinthepredictionloop.Thehuman-in-the-loopfashion[24,52]enablesrare
categoryanalysismodelstoleveragehumanintelligencetoalleviatethelabelscarcityissue
andimprovethepredictionperformanceinhigh-stakeapplications,suchasfailurepredic-
tion in safety-critical systems and rare disease diagnosis in health care. However, as hu-
man intelligence is naturally a black box to AI models, a fundamental research question
remains nascent: How can we gain a deeper understanding of the underlying mechanism of
humanintelligence,thusenablingunimpededknowledgetransferbetweenhumanintelligence
andAI? Apromisingbutchallengingresearchdirectionliesinhowtobuildanintegrated
andinteractivesystemforaccurateandtrustworthyhuman–AIcollaborativerarecategory
analysis.
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:27
REFERENCES
[1] StevenP.Abney.2002.Bootstrapping.In40thAnnualMeetingoftheAssociationforComputationalLinguistics(ACL),
pages360–367.
[2] ManojAcharya,AnirbanRoy,KaushikKoneripalli,SusmitJha,ChristopherKanan,andAjayDivakaran.2022.De-
tecting out-of-context objects using graph contextual reasoning network. In 31st International Joint Conference
on Artificial Intelligence (IJCAI 2022) (Vienna, Austria, 23–29 July 2022), Luc De Raedt (Ed.). ijcai.org, 629–635.
https://doi.org/10.24963/ijcai.2022/89
[3] PrernaAgarwal,RichaVerma,AyushAgarwal,andTanmoyChakraborty.2018.DyPerm:Maximizingpermanence
fordynamiccommunitydetection.InPacific-AsiaConferenceonKnowledgeDiscoveryandDataMining.Springer,
437–449.
[4] AmirhosseinAhmadianandFredrikLindsten.2021.Likelihood-freeout-of-distributiondetectionwithinvertiblegen-
erativemodels.In30thInternationalJointConferenceonArtificialIntelligence(IJCAI2021),(VirtualEvent/Montreal,
Canada,19–27August2021),Zhi-HuaZhou(Ed.).ijcai.org,2119–2125.https://doi.org/10.24963/ijcai.2021/292
[5] LemanAkogluandChristosFaloutsos.2010.Eventdetectionintimeseriesofmobilecommunicationgraphs.In
ArmyScienceConference,Vol.1.
[6] LemanAkoglu,MaryMcGlohon,andChristosFaloutsos.2010.Oddball:Spottinganomaliesinweightedgraphs.In
Pacific-AsiaConferenceonKnowledgeDiscoveryandDataMining.Springer,410–421.
[7] LemanAkoglu,HanghangTong,andDanaiKoutra.2015.Graphbasedanomalydetectionanddescription:Asurvey.
DataMiningandKnowledgeDiscovery29,3(2015),626–688.
[8] SamirAl-StouhiandChandanK.Reddy.2016.Transferlearningforclassimbalanceproblemswithinadequatedata.
Knowl.Inf.Syst.48,1(2016),201–228.https://doi.org/10.1007/s10115-015-0870-3
[9] AlejandroMarcosAlvarez,MakotoYamada,AkisatoKimura,andTomoharuIwata.2013.Clustering-basedanomaly
detectioninmulti-viewdata.In22ndACMInternationalConferenceonInformationandKnowledgeManagement
(CIKM’13)(SanFrancisco,CA,October27–November1,2013),QiHe,ArunIyengar,WolfgangNejdl,JianPei,and
RajeevRastogi(Eds.).ACM,1545–1548.https://doi.org/10.1145/2505515.2507840
[10] MehrnazAmjadiandThejaTulabandhula.2018.Block-structurebasedtime-seriesmodelsforgraphsequences.arXiv
preprintarXiv:1804.08796(2018).
[11] ReidAndersen,FanR.K.Chung,andKevinJ.Lang.2006.Localgraphpartitioningusingpagerankvectors.In47th
AnnualIEEESymposiumonFoundationsofComputerScience(FOCS2006)(21–24October2006,Berkeley,California).
IEEEComputerSociety,475–486.https://doi.org/10.1109/FOCS.2006.44
[12] JeroneAndrews,ThomasTanay,EdwardJ.Morton,andLewisD.Griffin.2016.Transferrepresentation-learningfor
anomalydetection.JournalofMachineLearningResearch.
[13] AnaPaulaAppel,RenatoL.F.Cunha,CharuC.Aggarwal,andMarcelaMegumiTerakado.2018.Temporallyevolving
communitydetectionandpredictionincontent-centricnetworks.InJointEuropeanConferenceonMachineLearning
andKnowledgeDiscoveryinDatabases.Springer,3–18.
[14] MiguelAraujo,SpirosPapadimitriou,StephanGünnemann,ChristosFaloutsos,PrithwishBasu,AnanthramSwami,
EvangelosEPapalexakis,andDanaiKoutra.2014.Com2:Fastautomaticdiscoveryoftemporal(‘comet’)communities.
InPacific-AsiaConferenceonKnowledgeDiscoveryandDataMining.Springer,271–283.
[15] AlejandroBarredoArrieta,NataliaDíaz-Rodríguez,JavierDelSer,AdrienBennetot,SihamTabik,AlbertoBarbado,
SalvadorGarcía,SergioGil-López,DanielMolina,RichardBenjamins,RajaChatila,andFranciscoHerrera.2020.
Explainableartificialintelligence(XAI):Concepts,taxonomies,opportunitiesandchallengestowardresponsibleAI.
InformationFusion58(2020),82–115.
[16] FatemehAzmandian,AyseYilmazer,JenniferG.Dy,JavedA.Aslam,andDavidR.Kaeli.2012.GPU-accelerated
featureselectionforoutlier detectionusingthelocalkerneldensityratio.In12thIEEEInternationalConference
on Data Mining (ICDM2012) (Brussels, Belgium, December10–13, 2012), Mohammed Javeed Zaki, Arno Siebes,
Jeffrey Xu Yu, Bart Goethals, Geoffrey I. Webb, and Xindong Wu (Eds.). IEEE Computer Society, 51–60. https:
//doi.org/10.1109/ICDM.2012.51
[17] MichaelJ.Bamshad,SarahB.Ng,AbigailW.Bigham,HollyK.Tabor,MaryJ.Emond,DeborahA.Nickerson,and
JayShendure.2011.ExomesequencingasatoolforMendeliandiseasegenediscovery.NatureReviewsGenetics12,
11(2011),745.
[18] NurjahanBegumandEamonnKeogh.2014.Raretimeseriesmotifdiscoveryfromunboundedstreams.Proceedings
oftheVLDBEndowment8,2(2014),149–160.
[19] KarstenM.Borgwardt,ChengSoonOng,StefanSchönauer,S.V.N.Vishwanathan,AlexanderJ.Smola,andHans-
PeterKriegel.2005.Proteinfunctionpredictionviagraphkernels.In13thInternationalConferenceonIntelligentSys-
temsforMolecularBiology2005(Detroit,MI,25–29June2005).47–56.https://doi.org/10.1093/bioinformatics/bti1007
[20] PaulaBranco,LuísTorgo,andRitaP.Ribeiro.2016.Asurveyofpredictivemodelingonimbalanceddomains.ACM
ComputingSurveys(CSUR)49,2(2016),31.
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:28 D.ZhouandJ.He
[21] SuratnaBudalakoti,AshokN.Srivastava,RamAkella,andEugeneTurkov.2006.Anomalydetectioninlargesetsof
high-dimensionalsymbolsequences.TechnicalReportNASATM-2006-214553,NASAAmesResearchCenter,2006.
[22] LeiCao,DiYang,QingyangWang,YanweiYu,JiayuanWang,andElkeA.Rundensteiner.2014.Scalabledistance-
basedoutlierdetectionoverhigh-volumedatastreams.In2014IEEE30thInternationalConferenceonDataEngineering.
IEEE,76–87.
[23] AldoG.Carranza,RyanA.Rossi,AnupRao,andEunyeeKoh.2020.Higher-orderclusteringincomplexheteroge-
neousnetworks.InThe26thACMSIGKDDConferenceonKnowledgeDiscoveryandDataMining(KDD’20)(Virtual
Event,CA,August23–27,2020),RajeshGupta,YanLiu,JiliangTang,andB.AdityaPrakash(Eds.).ACM,25–35.
https://doi.org/10.1145/3394486.3403045
[24] ChengliangChai,LeiCao,GuoliangLi,JianLi,YuyuLuo,andSamuelMadden.2020.Human-in-the-loopoutlier
detection.In2020InternationalConferenceonManagementofData(SIGMODConference2020),(OnlineConference
[Portland,OR],June14–19,2020),DavidMaier,RachelPottinger,AnHaiDoan,Wang-ChiewTan,AbdussalamAlaw-
ini,andHungQ.Ngo(Eds.).ACM,19–33.https://doi.org/10.1145/3318464.3389772
[25] RaghavendraChalapathyandSanjayChawla.2019.Deeplearningforanomalydetection:Asurvey.arXivpreprint
arXiv:1901.03407(2019).
[26] VarunChandola,ArindamBanerjee,andVipinKumar.2009.Anomalydetection:Asurvey.ACMComputingSurveys
(CSUR)41,3(2009),15.
[27] VarunChandola,ArindamBanerjee,andVipinKumar.2010.Anomalydetectionfordiscretesequences:Asurvey.
IEEETransactionsonKnowledgeandDataEngineering24,5(2010),823–839.
[28] ChaomeiChen.2006.CiteSpaceII:Detectingandvisualizingemergingtrendsandtransientpatternsinscientific
literature.JournaloftheAmericanSocietyforInformationScienceandTechnology57,3(2006),359–377.
[29] ChengweiChen,YuanXie,ShaohuiLin,AngelaYao,GuannanJiang,WeiZhang,YanyunQu,RuizhiQiao,BoRen,and
LizhuangMa.2022.Comprehensiveregularizationinabi-directionalpredictivenetworkforvideoanomalydetection.
In36thAAAIConferenceonArtificialIntelligence(AAAI2022),34thConferenceonInnovativeApplicationsofArtificial
Intelligence(IAAI2022),12thSymposiumonEducationalAdvancesinArtificialIntelligence(EAAI2022)(VirtualEvent,
February22–March1,2022).AAAIPress,230–238.https://ojs.aaai.org/index.php/AAAI/article/view/19898
[30] XuanHongDang,BarboraMicenková,IraAssent,andRaymondT.Ng.2013.Localoutlierdetectionwithinterpre-
tation.InJointEuropeanConferenceonMachineLearningandKnowledgeDiscoveryinDatabases.Springer,304–320.
[31] ArunDasandPaulRad.2020.Opportunitiesandchallengesinexplainableartificialintelligence(XAI):Asurvey.
arXivpreprintarXiv:2006.11371(2020).
[32] AilinDeng,AdamGoodge,LangYiAng,andBryanHooi.2022.CADET:Calibratedanomalydetectionformitigating
hardnessbias.In31stInternationalJointConferenceonArtificialIntelligence(IJCAI2022),(Vienna,Austria,23–29July
2022),LucDeRaedt(Ed.).ijcai.org,2002–2008.https://doi.org/10.24963/ijcai.2022/278
[33] AilinDengandBryanHooi.2021.Graphneuralnetwork-basedanomalydetectioninmultivariatetimeseries.In
35thAAAIConferenceonArtificialIntelligence(AAAI2021),33rdConferenceonInnovativeApplicationsofArtificial
Intelligence(IAAI2021),11thSymposiumonEducationalAdvancesinArtificialIntelligence(EAAI2021),(VirtualEvent,
February2–9,2021).AAAIPress,4027–4035.https://ojs.aaai.org/index.php/AAAI/article/view/16523
[34] SonggaojunDeng,HuzefaRangwala,andYueNing.2019.Learningdynamiccontextgraphsforpredictingsocial
events.In25thACMSIGKDDInternationalConferenceonKnowledgeDiscovery&DataMining.ACM,1007–1016.
[35] DheeruDuaandCaseyGraff.2017.UCIMachineLearningRepository.http://archive.ics.uci.edu/ml
[36] MichaelEdwardEdgeandPedroR.FalconeSampaio.2009.Asurveyofsignaturebasedmethodsforfinancialfraud
detection.Computers&Security28,6(2009),381–394.
[37] BradleyEfronandRobertTibshirani.1996.Usingspeciallydesignedexponentialfamiliesfordensityestimation.The
AnnalsofStatistics24,6(1996),2431–2461.
[38] DongqiFu,DaweiZhou,andJingruiHe.2020.Localmotifclusteringontime-evolvinggraphs.In26thACMSIGKDD
ConferenceonKnowledgeDiscoveryandDataMining(KDD’20),(VirtualEvent,CA,August23–27,2020),RajeshGupta,
YanLiu,JiliangTang,andB.AdityaPrakash(Eds.).ACM,390–400.https://doi.org/10.1145/3394486.3403081
[39] DongqiFu,DaweiZhou,RossMaciejewski,ArieCroitoru,MarcusBoyd,andJingruiHe.2023.Fairness-awareclique-
preservingspectralclusteringoftemporalgraphs.InACMWebConference2023(WWW2023),(Austin,TX,30April
2023–4May2023).,YingDing,JieTang,JuanF.Sequeda,LoraAroyo,CarlosCastillo,andGeert-JanHouben(Eds.).
ACM,3755–3765.https://doi.org/10.1145/3543507.3583423
[40] JingGao,WeiFan,DeepakTuraga,SrinivasanParthasarathy,andJiaweiHan.2011.Aspectralframeworkfordetect-
inginconsistencyacrossmulti-sourceobjectrelationships.In2011IEEE11thInternationalConferenceonDataMining
(ICDM).IEEE,1050–1055.
[41] YuanGao,XiangWang,XiangnanHe,ZhenguangLiu,HuaminFeng,andYongdongZhang.2023.Addressinghet-
erophilyingraphanomalydetection:Aperspectiveofgraphspectrum.InACMWebConference2023,WWW2023,
Austin,TX,USA,30April2023–4May2023,YingDing,JieTang,JuanF.Sequeda,LoraAroyo,CarlosCastillo,and
Geert-JanHouben(Eds.).ACM,1528–1538.https://doi.org/10.1145/3543507.3583268
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:29
[42] Adam Goodge, Bryan Hooi, See-Kiong Ng, and Wee Siong Ng. 2022. LUNAR: Unifying local outlier detection
methods via graph neural networks. In 36th AAAI Conference on Artificial Intelligence (AAAI 2022), 34th Con-
ference on Innovative Applications of Artificial Intelligence (IAAI 2022), 12th Symposium on Educational Advances
in Artificial Intelligence (EAAI 2022) (Virtual Event, February 22–March 1, 2022). AAAI Press, 6737–6745. https:
//ojs.aaai.org/index.php/AAAI/article/view/20629
[43] SudiptoGuha,NinaMishra,GouravRoy,andOkkeSchrijvers.2016.Robustrandomcutforestbasedanomalydetec-
tiononstreams.InInternationalConferenceonMachineLearning.2712–2721.
[44] David Gunning, Mark Stefik, Jaesik Choi, Timothy Miller, Simone Stumpf, and Guang-Zhong Yang. 2019. XAI-
explainableartificialintelligence.ScienceRobotics4,37(2019),eaay7120.
[45] ManishGupta,JingGao,CharuC.Aggarwal,andJiaweiHan.2013.Outlierdetectionfortemporaldata:Asurvey.
IEEETransactionsonKnowledgeandDataEngineering26,9(2013),2250–2267.
[46] AhsanulHaque,LatifurKhan,andMichaelBaron.2016.SAND:Semi-supervisedadaptivenovelclassdetectionand
classificationoverdatastream.InAAAIConferenceonArtificialIntelligence.
[47] D.M.Hawkins.1980.IdentificationofOutliers.Springer.https://doi.org/10.1007/978-94-015-3994-4
[48] HaiboHeandEdwardoA.Garcia.2009.Learningfromimbalanceddata.IEEETransactionsonKnowledgeandData
Engineering21,9(2009),1263–1284.
[49] JingruiHe.2010.RareCategoryAnalysis.Ph.D.Dissertation.CarnegieMellonUniversity,Pittsburgh,PA.
[50] JingruiHeandJaimeCarbonell.2009.Prior-freerarecategorydetection.In2009SIAMInternationalConferenceon
DataMining.SIAM,155–163.
[51] JingruiHeandJaimeCarbonell.2010.Coselectionoffeaturesandinstancesforunsupervisedrarecategoryanalysis.
StatisticalAnalysisandDataMining:TheASADataScienceJournal3,6(2010),417–430.
[52] JingruiHeandJaimeG.Carbonell.2008.Nearest-neighbor-basedactivelearningforrarecategorydetection.In
AdvancesinNeuralInformationProcessingSystems.633–640.
[53] JingruiHe,YanLiu,andRichardLawrence.2008.Graph-basedrarecategorydetection.In8thIEEEInternational
ConferenceonDataMining,2008(ICDM’08).IEEE,833–838.
[54] JingruiHe,HanghangTong,andJaimeCarbonell.2010.Rarecategorycharacterization.In10thIEEEInternational
ConferenceonDataMining(ICDM).IEEE,226–235.
[55] JingruiHe,HanghangTong,andJaimeCarbonell.2012.Aneffectiveframeworkforcharacterizingrarecategories.
FrontiersofComputerScience6,2(2012),154–165.
[56] ZengyouHe,XiaofeiXu,andShengchunDeng.2003.Discoveringcluster-basedlocaloutliers.PatternRecognit.Lett.
24,9-10(2003),1641–1650.https://doi.org/10.1016/S0167-8655(03)00003-5
[57] VictoriaHodgeandJimAustin.2004.Asurveyofoutlierdetectionmethodologies.ArtificialIntelligenceReview22,
2(2004),85–126.
[58] StevenA.Hofmeyr,StephanieForrest,andAnilSomayaji.1998.Intrusiondetectionusingsequencesofsystemcalls.
JournalofComputerSecurity6,3(1998),151–180.
[59] AlexandreHollocou,JulienMaudet,ThomasBonald,andMarcLelarge.2017.Astreamingalgorithmforgraphclus-
tering.CoRRabs/1712.04337(2017).arXiv:1712.04337http://arxiv.org/abs/1712.04337
[60] ChenHuang,YiningLi,ChenChangeLoy,andXiaoouTang.2016.Learningdeeprepresentationforimbalanced
classification.InIEEEConferenceonComputerVisionandPatternRecognition.5375–5384.
[61] TsuyoshiIdé,AmitDhurandhar,JiríNavrátil,MoninderSingh,andNaokiAbe.2021.Anomalyattributionwith
likelihoodcompensation.In35thAAAIConferenceonArtificialIntelligence(AAAI2021),33rdConferenceonInnovative
ApplicationsofArtificialIntelligence(IAAI2021),11thSymposiumonEducationalAdvancesinArtificialIntelligence
(EAAI2021),(VirtualEvent,February2–9,2021).AAAIPress,4131–4138.https://ojs.aaai.org/index.php/AAAI/article/
view/16535
[62] TsuyoshiIdé,DzungT.Phan,andJayantKalagnanam.2017.Multi-taskmulti-modalmodelsforcollectiveanomaly
detection.In2017IEEEInternationalConferenceonDataMining(ICDM2017)(NewOrleans,LA,November18–21,
2017),VijayRaghavan,SrinivasAluru,GeorgeKarypis,LucioMiele,andXindongWu(Eds.).IEEEComputerSociety,
177–186.https://doi.org/10.1109/ICDM.2017.27
[63] TomoharuIwataandMakotoYamada.2016.Multi-viewanomalydetectionviarobustprobabilisticlatentvariable
models.InAdvancesInNeuralInformationProcessingSystems.1136–1144.
[64] Tomoharu Iwata and Makoto Yamada. 2016. Multi-view anomaly detection via robust probabilistic latent vari-
ablemodels. In Advances in Neural Information Processing Systems 29: AnnualConference onNeural Information
ProcessingSystems2016,(December5–10,2016,Barcelona,Spain),DanielD.Lee,MasashiSugiyama,Ulrikevon
Luxburg, Isabelle Guyon, and Roman Garnett (Eds.). 1136–1144. https://proceedings.neurips.cc/paper/2016/hash/
0f96613235062963ccde717b18f97592-Abstract.html
[65] H.V.Jagadish,NickKoudas,andS.Muthukrishnan.1999.Miningdeviantsinatimeseriesdatabase.InVLDB,Vol.99.
7–10.
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:30 D.ZhouandJ.He
[66] MiltiadisKandias,AlexiosMylonas,NikosVirvilis,MarianthiTheoharidou,andDimitrisGritzalis.2010.Aninsider
threatpredictionmodel.InInternationalConferenceonTrust,PrivacyandSecurityinDigitalBusiness.Springer,26–37.
[67] Ramneet Kaur, Susmit Jha, Anirban Roy, Sangdon Park, Edgar Dobriban, Oleg Sokolsky, and Insup Lee. 2022.
iDECODe:In-distributionequivarianceforconformalout-of-distributiondetection.In36thAAAIConferenceonAr-
tificialIntelligence(AAAI2022),34thConferenceonInnovativeApplicationsofArtificialIntelligence(IAAI2022),12th
SymposiumonEducationalAdvancesinArtificialIntelligence(EAAI2022)(VirtualEvent,February22–March1,2022).
AAAIPress,7104–7114.https://ojs.aaai.org/index.php/AAAI/article/view/20670
[68] FabianKeller,EmmanuelMüller,andKlemensBöhm.2012.HiCS:Highcontrastsubspacesfordensity-basedoutlier
ranking.InIEEE28thInternationalConferenceonDataEngineering(ICDE2012)(Washington,DC, [Arlington,Vir-
ginia],1–5April,2012),AnastasiosKementsietsidisandMarcosAntonioVazSalles(Eds.).IEEEComputerSociety,
1037–1048.https://doi.org/10.1109/ICDE.2012.88
[69] KamranKhan,SaifUrRehman,KamranAziz,SimonFong,andSababadySarasvady.2014.DBSCAN:Past,present
andfuture.In5thInternationalConferenceontheApplicationsofDigitalInformationandWebTechnologies(ICADIWT
2014).IEEE,232–238.
[70] JonM.Kleinberg.1998.Authoritativesourcesinahyperlinkedenvironment.In9thAnnualACM-SIAMSymposium
onDiscreteAlgorithms(25–27January1998,SanFrancisco,California), HowardJ.Karloff(Ed.).ACM/SIAM,668–677.
http://dl.acm.org/citation.cfm?id=314613.315045
[71] ChristineKlymko,DavidGleich,andTamaraG.Kolda.2014.Usingtrianglestoimprovecommunitydetectionin
directednetworks.arXivpreprintarXiv:1404.5874(2014).
[72] AtsutoshiKumagai,TomoharuIwata,andYasuhiroFujiwara.2019.Transferanomalydetectionbyinferringlatent
domainrepresentations.InAdvancesinNeuralInformationProcessingSystems32:AnnualConferenceonNeuralIn-
formationProcessingSystems2019(NeurIPS2019),(December8–14,2019,Vancouver,BC,Canada),HannaM.Wallach,
HugoLarochelle,AlinaBeygelzimer,Florenced’Alché-Buc,EmilyB.Fox,andRomanGarnett(Eds.).2467–2477.
https://proceedings.neurips.cc/paper/2019/hash/7895fc13088ee37f511913bac71fa66f-Abstract.html
[73] SrijanKumar,FrancescaSpezzano,andV.S.Subrahmanian.2015.VEWS:AWikipediavandalearlywarningsystem.
In21thACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining(Sydney,NSW,Australia,
August10–13,2015),LongbingCao,ChengqiZhang,ThorstenJoachims,GeoffreyI.Webb,DragosD.Margineantu,
andGrahamWilliams(Eds.).ACM,607–616.https://doi.org/10.1145/2783258.2783367
[74] HimabinduLakkarajuandOsbertBastani.2020.“HowdoIfoolyou?”Manipulatingusertrustviamisleadingblack
boxexplanations.InAAAI/ACMConferenceonAI,Ethics,andSociety.79–85.
[75] DoyupLee,YeongjaeCheon,andWook-ShinHan.2021.Regularizingattentionnetworksforanomalydetection
invisualquestionanswering.In35thAAAIConferenceonArtificialIntelligence(AAAI2021),33rdConferenceon
InnovativeApplicationsofArtificialIntelligence(IAAI2021),11thSymposiumonEducationalAdvancesinArtificial
Intelligence(EAAI2021),(VirtualEvent,February2–9,2021).AAAIPress,1845–1853.https://ojs.aaai.org/index.php/
AAAI/article/view/16279
[76] KevinH.Lee,LingzhouXue,andDavidR.Hunter.2017.Model-basedclusteringoftime-evolvingnetworksthrough
temporalexponential-familyrandomgraphmodels.arXivpreprintarXiv:1712.07325(2017).
[77] DanLi,DachengChen,LeiShi,BaihongJin,JonathanGoh,andSee-KiongNg.2019.MAD-GAN:Multivariateanom-
alydetectionfortimeseriesdatawithgenerativeadversarialnetworks.arXivpreprintarXiv:1901.04997(2019).
[78] KaiLi,ShengLi,ZhengmingDing,WeidongZhang,andYunFu.2018.Latentdiscriminantsubspacerepresentations
formulti-viewoutlierdetection.In32ndAAAIConferenceonArtificialIntelligence,(AAAI-18),30thInnovativeAppli-
cationsofArtificialIntelligence(IAAI-18),and8thAAAISymposiumonEducationalAdvancesinArtificialIntelligence
(EAAI-18)(NewOrleans,LA,February2–7,2018),SheilaA.McIlraithandKilianQ.Weinberger(Eds.).AAAIPress,
3522–3529.https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/17401
[79] ShengLi,MingShao,andYunFu.2015.Multi-viewlow-rankanalysisforoutlierdetection.In2015SIAMInternational
ConferenceonDataMining(Vancouver,BC,Canada,April30–May2,2015),SureshVenkatasubramanianandJieping
Ye(Eds.).SIAM,748–756.https://doi.org/10.1137/1.9781611974010.84
[80] XiaoleiLiandJiaweiHan.2007.Miningapproximatetop-ksubspaceanomaliesinmulti-dimensionaltime-series
data.InProceedingsofthe33rdInternationalConferenceonVeryLargeDataBases.VLDBEndowment,447–458.
[81] HanfeiLin,SiyuanGao,DavidGotz,FanDu,JingruiHe,andNanCao.2018.Rclens:Interactiverarecategoryexplo-
rationandidentification.IEEETransactionsonVisualizationandComputerGraphics24,7(2018),2223–2237.
[82] WangliLin,LiSun,QiweiZhong,CanLiu,JinghuaFeng,XiangAo,andHaoYang.2021.Onlinecreditpayment
frauddetectionviastructure-awarehierarchicalrecurrentneuralnetwork.In30thInternationalJointConferenceon
ArtificialIntelligence(IJCAI2021)(VirtualEvent/Montreal,Canada,19–27August2021),Zhi-HuaZhou(Ed.).ijcai.org,
3670–3676.https://doi.org/10.24963/ijcai.2021/505
[83] BoyangLiu,Pang-NingTan,andJiayuZhou.2022.Unsupervisedanomalydetectionbyrobustdensityestimation.
In36thAAAIConferenceonArtificialIntelligence(AAAI2022),34thConferenceonInnovativeApplicationsofArtificial
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:31
Intelligence(IAAI2022),T12thSymposiumonEducationalAdvancesinArtificialIntelligence(EAAI2022)(VirtualEvent,
February22–March1,2022).AAAIPress,4101–4108.https://ojs.aaai.org/index.php/AAAI/article/view/20328
[84] NinghaoLiu,DonghwaShin,andXiaHu.2017.Contextualoutlierinterpretation.arXivpreprintarXiv:1711.10589
(2017).
[85] Zhining Liu, Dawei Zhou, Yada Zhu, Jinjie Gu, and Jingrui He. 2020. Towards fine-grained temporal network
representation via time-reinforced random walk. In 34th AAAI Conference on Artificial Intelligence (AAAI 2020),
32ndInnovativeApplicationsofArtificialIntelligenceConference(IAAI2020),10thAAAISymposiumonEducational
Advances in Artificial Intelligence (EAAI 2020) (New York, February 7–12, 2020). AAAI Press, 4973–4980. https:
//aaai.org/ojs/index.php/AAAI/article/view/5936
[86] JustinMa,LawrenceK.Saul,StefanSavage,andGeoffreyM.Voelker.2009.IdentifyingsuspiciousURLs:Anapplica-
tionoflarge-scaleonlinelearning.In26thAnnualInternationalConferenceonMachineLearning(ICML2009)(Mon-
treal,Quebec,Canada,June14–18,2009)(ACMInternationalConferenceProceedingSeries),AndreaPohoreckyjDany-
luk,LéonBottou,andMichaelL.Littman(Eds.),Vol.382.ACM,681–688.https://doi.org/10.1145/1553374.1553462
[87] RongrongMa,GuansongPang,LingChen,andAntonvandenHengel.2021.Deepgraph-levelanomalydetection
byglocalknowledgedistillation.CoRRabs/2112.10063(2021).arXiv:2112.10063https://arxiv.org/abs/2112.10063
[88] LaurensvanderMaatenandGeoffreyHinton.2008.Visualizingdatausingt-SNE. JournalofMachineLearning
Research9(Nov.2008),2579–2605.
[89] MeghanathMachaandLemanAkoglu.2018.Explaininganomaliesingroupswithcharacterizingsubspacerules.
DataMiningandKnowledgeDiscovery32,5(2018),1444–1480.
[90] EmaadManzoor,SadeghM.Milajerdi,andLemanAkoglu.2016.Fastmemory-efficientanomalydetectioninstream-
ingheterogeneousgraphs.In22ndACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining.
ACM,1035–1044.
[91] AlejandroMarcosAlvarez,MakotoYamada,AkisatoKimura,andTomoharuIwata.2013.Clustering-basedanom-
alydetectioninmulti-viewdata.In22ndACMInternationalConferenceonConferenceonInformation&Knowledge
Management.ACM,1545–1548.
[92] MarkosMarkouandSameerSingh.2003.Noveltydetection:Areview-Part1:Statisticalapproaches.SignalProcessing
83,12(2003),2481–2497.
[93] BhaskarMehta,SaurabhNangia,ManishGupta,andWolfgangNejdl.2008.Detectingimagespamusingvisualfea-
turesandnearduplicatedetection.In17thInternationalConferenceonWorldWideWeb.ACM,497–506.
[94] TomasMikolov,IlyaSutskever,KaiChen,GregS.Corrado,andJeffDean.2013.Distributedrepresentationsofwords
andphrasesandtheircompositionality.InAdvancesinNeuralInformationProcessingSystems.3111–3119.
[95] YifeiMing,HangYin,andYixuanLi.2022.Ontheimpactofspuriouscorrelationforout-of-distributiondetection.
In36thAAAIConferenceonArtificialIntelligence(AAAI2022),34thConferenceonInnovativeApplicationsofArtificial
Intelligence(IAAI2022),12thSymposiumonEducationalAdvancesinArtificialIntelligence(EAAI2022)(VirtualEvent,
February22–March1,2022).AAAIPress,10051–10059.https://ojs.aaai.org/index.php/AAAI/article/view/21244
[96] ChristophMolnar.2020.InterpretableMachineLearning.Lulu.com.
[97] HosseinMoradiKoupaie,SuhaimiIbrahim,andJavadHosseinkhani.2014.Outlierdetectioninstreamdatabyclus-
teringmethod.InternationalJournalofAdvancedComputerScienceandInformationTechnology(IJACSIT) 2(2014),
25–34.
[98] PeymanMortezaandYixuanLi.2022.Provableguaranteesforunderstandingout-of-distributiondetection.In36th
AAAIConferenceonArtificialIntelligence(AAAI2022),34thConferenceonInnovativeApplicationsofArtificialIntel-
ligence(IAAI2022),12thSymposiumonEducationalAdvancesinArtificialIntelligence(EAAI2022)(VirtualEvent,
February22–March1,2022).AAAIPress,7831–7840.https://ojs.aaai.org/index.php/AAAI/article/view/20752
[99] NourMoustafaandJillSlay.2015.UNSW-NB15:Acomprehensivedatasetfornetworkintrusiondetectionsystems
(UNSW-NB15networkdataset).In2015MilitaryCommunicationsandInformationSystemsConference(MilCIS2015)
(Canberra,Australia,November10–12,2015).IEEE,1–6.https://doi.org/10.1109/MilCIS.2015.7348942
[100] ShanMuthukrishnan,RahulShah,andJeffreyScottVitter.2004.Miningdeviantsintimeseriesdatastreams.In16th
InternationalConferenceonScientificandStatisticalDatabaseManagement,2004.IEEE,41–50.
[101] AlexandreNairac,NeilTownsend,RoyCarr,SteveKing,PeterCowley,andLionelTarassenko.1999.Asystemfor
theanalysisofjetenginevibrationdata.IntegratedComputer-AidedEngineering6,1(1999),53–66.
[102] EricW.T.Ngai,YongHu,YiuHingWong,YijunChen,andXinSun.2011.Theapplicationofdataminingtechniques
infinancialfrauddetection:Aclassificationframeworkandanacademicreviewofliterature.DecisionSupportSys-
tems50,3(2011),559–569.
[103] GiangHoangNguyen,JohnBoazLee,RyanA.Rossi,NesreenK.Ahmed,EunyeeKoh,andSungchulKim.2018.
Continuous-time dynamic network embeddings. In Companion of the Web Conference 2018 (WWW 2018) (Lyon,
France,April23–27,2018),Pierre-AntoineChampin,FabienGandon,MouniaLalmas,andPanagiotisG.Ipeirotis
(Eds.).ACM,969–976.https://doi.org/10.1145/3184558.3191526
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:32 D.ZhouandJ.He
[104] FeipingNie,GuohaoCai,andXuelongLi.2017.Multi-viewclusteringandsemi-supervisedclassificationwithadap-
tiveneighbours.In31stAAAIConferenceonArtificialIntelligence(February4–9,2017,SanFrancisco,California),
SatinderP.SinghandShaulMarkovitch(Eds.).AAAIPress,2408–2414.http://aaai.org/ocs/index.php/AAAI/AAAI17/
paper/view/14833
[105] JiachengPan,DongmingHan,FangzhouGuo,DaweiZhou,NanCao,JingruiHe,MingliangXu,andWeiChen.2020.
RCAnalyzer:Visualanalyticsofrarecategoriesindynamicnetworks.FrontiersInf.Technol.Electron.Eng.21,4(2020),
491–506.https://doi.org/10.1631/FITEE.1900310
[106] GuansongPang,ChunhuaShen,andAntonvandenHengel.2019.Deepanomalydetectionwithdeviationnetworks.
In25thACMSIGKDDInternationalConferenceonKnowledgeDiscovery&DataMining.353–362.
[107] GuansongPang,AntonvandenHengel,ChunhuaShen,andLongbingCao.2021.Towarddeepsupervisedanomaly
detection:Reinforcementlearningfrompartiallylabeledanomalydata.In27thACMSIGKDDConferenceonKnowl-
edgeDiscoveryandDataMining(KDD’21)(VirtualEvent,Singapore,August14–18,2021),FeidaZhu,BengChin
Ooi,andChunyanMiao(Eds.).ACM,1298–1308.https://doi.org/10.1145/3447548.3467417
[108] DhavalPatel.2023.Timeseriesanomalydetectiontool:Handsoflab.InAAAIConferenceonArtificialIntelligence.
[109] DanPellegandAndrewW.Moore.2005.Activelearningforanomalyandrare-categorydetection.InAdvancesin
NeuralInformationProcessingSystems.1073–1080.
[110] BryanPerozzi,LemanAkoglu,PatriciaIglesiasSánchez,andEmmanuelMüller.2014.Focusedclusteringandoutlier
detectioninlargeattributedgraphs.In20thACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandData
Mining.ACM,1346–1355.
[111] BryanPerozzi,RamiAl-Rfou,andStevenSkiena.2014.Deepwalk:Onlinelearningofsocialrepresentations.In20th
ACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining(August24-27,2014,NewYork,NY)
ACM,701–710.
[112] GeoPertea,XiaoqiuHuang,FengLiang,ValentinAntonescu,RazvanSultana,SvetlanaKaramycheva,YuandanLee,
JosephWhite,FooCheung,BabakParvizi,JenniferTsai,andJohnQuackenbush.2003.TIGRgeneindicesclustering
tools(TGICL):AsoftwaresystemforfastclusteringoflargeESTdatasets.Bioinform.19,5(2003),651–652.https:
//doi.org/10.1093/bioinformatics/btg034
[113] CliftonPhua,VincentLee,KateSmith,andRossGayler.2010.Acomprehensivesurveyofdatamining-basedfraud
detectionresearch.arXivpreprintarXiv:1009.6119(2010).
[114] AndreaDalPozzolo,OlivierCaelen,ReidA.Johnson,andGianlucaBontempi.2015.Calibratingprobabilitywith
undersamplingforunbalancedclassification.InIEEESymposiumSeriesonComputationalIntelligence(SSCI2015)
(CapeTown,SouthAfrica,December7–10,2015).IEEE,159–166.https://doi.org/10.1109/SSCI.2015.33
[115] StephenRanshous,ShitianShen,DanaiKoutra,SteveHarenberg,ChristosFaloutsos,andNagizaF.Samatova.2015.
Anomaly detection in dynamic networks: A survey. Wiley Interdisciplinary Reviews: Computational Statistics 7,
3(2015),223–247.
[116] UmaaRebbapragada,PavlosProtopapas,CarlaE.Brodley,andCharlesAlcock.2009.Findinganomalousperiodic
timeseries.MachineLearning74,3(2009),281–313.
[117] MaurizioScarpa,ZsuzsannaAlmássy,MichaelBeck,OlafBodamer,IainA.Bruce,LindaDeMeirleir,NathalieGuf-
fon,EncarnaGuillén-Navarro,PaulineHensman,SimonJones,etal.2011.MucopolysaccharidosistypeII:European
recommendationsforthediagnosisandmultidisciplinarymanagementofararedisease.OrphanetJournalofRare
Diseases6,1(2011),72.
[118] FrançoisSchnitzler,ThomasLiebig,ShieMannor,GustavoSouto,SebastianBothe,andHendrikStange.2014.Het-
erogeneousstreamprocessingfordisasterdetectionandalarming.InIEEEInternationalConferenceonBigData.IEEE
Press,914–923.
[119] Karlton Sequeira and Mohammed Zaki. 2002. ADMIT: Anomaly-based data mining for intrusions. In 8th ACM
SIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining.ACM,386–395.
[120] ShubhranshuShekhar,NeilShah,andLemanAkoglu.2021.FairOD:Fairness-awareoutlierdetection.InAAAI/ACM
ConferenceonAI,Ethics,andSociety(AIES’21)(VirtualEvent,May19–21,2021)MarionFourcade,BenjaminKuipers,
SethLazar,andDeirdreK.Mulligan(Eds.).ACM,210–220.https://doi.org/10.1145/3461702.3462517
[121] LifengShen,ZhongzhongYu,QianliMa,andJamesT.Kwok.2021.Timeseriesanomalydetectionwithmultiresolu-
tionensembledecoding.In35thAAAIConferenceonArtificialIntelligence(AAAI2021),33rdConferenceonInnovative
ApplicationsofArtificialIntelligence(IAAI2021),11thSymposiumonEducationalAdvancesinArtificialIntelligence
(EAAI2021)(VirtualEvent,February2–9,2021).AAAIPress,9567–9575.https://ojs.aaai.org/index.php/AAAI/article/
view/17152
[122] Xiang-RongSheng,De-ChuanZhan,SuLu,andYuanJiang.2019.Multi-viewanomalydetection:Neighborhood
inlocalitymatters.In33rdAAAIConferenceonArtificialIntelligence(AAAI2019),31stInnovativeApplicationsof
ArtificialIntelligenceConference(IAAI2019),9thAAAISymposiumonEducationalAdvancesinArtificialIntelligence
(EAAI2019),(Honolulu,Hawaii,January27–February1,2019).AAAIPress,4894–4901.https://doi.org/10.1609/aaai.
v33i01.33014894
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:33
[123] JouWonSong,KyeongboKong,YeInPark,SeongGyunKim,andSuk-JuKang.2021.AnoSeg:Anomalysegmen-
tationnetworkusingself-supervisedlearning.CoRRabs/2110.03396(2021).arXiv:2110.03396https://arxiv.org/abs/
2110.03396
[124] DanielA.SpielmanandShang-HuaTeng.2013.Alocalclusteringalgorithmformassivegraphsanditsapplication
tonearlylineartimegraphpartitioning.SIAMJ.Comput.42,1(2013),1–26.https://doi.org/10.1137/080744888
[125] KumarSricharanandKamalikaDas.2014.Localizinganomalouschangesintime-evolvinggraphs.In2014ACM
SIGMODInternationalConferenceonManagementofData.ACM,1347–1358.
[126] JimengSun,ChristosFaloutsos,SpirosPapadimitriou,andPhilipS.Yu.2007.Graphscope:Parameter-freeminingof
largetime-evolvinggraphs.In13thACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining.
ACM,687–696.
[127] JimengSun,HuimingQu,DeepayanChakrabarti,andChristosFaloutsos.2005.Neighborhoodformationandanom-
alydetectioninbipartitegraphs.In5thIEEEInternationalConferenceonDataMining.IEEE,418–425.
[128] Yi-XuanSunandWeiWang.2022.Exploitingmixedunlabeleddatafordetectingsamplesofseenandunseenout-
of-distributionclasses.In36thAAAIConferenceonArtificialIntelligence(AAAI2022),34thConferenceonInnova-
tiveApplicationsofArtificialIntelligence(IAAI2022),12thSymposiumonEducationalAdvancesinArtificialIntelli-
gence(EAAI2022)(VirtualEvent,February22–March1,2022).AAAIPress,8386–8394.https://ojs.aaai.org/index.
php/AAAI/article/view/20814
[129] YingSun,WenjunWang,NannanWu,WeiYu,andXueChen.2020.Anomalysubgraphdetectionwithfeature
transfer.In29thACMInternationalConferenceonInformationandKnowledgeManagement(CIKM’20)(VirtualEvent,
Ireland,October19–23,2020),Mathieud’Aquin,StefanDietze,ClaudiaHauff,EdwardCurry,andPhilippeCudré-
Mauroux(Eds.).ACM,1415–1424.https://doi.org/10.1145/3340531.3411968
[130] JianTang,MengQu,MingzheWang,MingZhang,JunYan,andQiaozhuMei.2015.LINE:Large-scaleinformation
networkembedding.In24thInternationalConferenceonWorldWideWeb(WWW2015)(Florence,Italy,May18–22,
2015).1067–1077.
[131] EricoTjoaandCuntaiGuan.2020.Asurveyonexplainableartificialintelligence(XAI):TowardmedicalXAI.IEEE
TransactionsonNeuralNetworksandLearningSystems32,11(2020),4793–4813.
[132] HanghangTongandChing-YungLin.2011.Non-negativeresidualmatrixfactorizationwithapplicationtograph
anomalydetection.In2011SIAMInternationalConferenceonDataMining.SIAM,143–153.
[133] JasonTumlinson.2011.Astronomy:Anewspinonthefirststars.Nature472,7344(2011),426.
[134] AaronTuor,SamuelKaplan,BrianHutchinson,NicoleNichols,andSeanRobinson.2017.Deeplearningforunsuper-
visedinsiderthreatdetectioninstructuredcybersecuritydatastreams.InWorkshopsatthe31stAAAIConferenceon
ArtificialIntelligence.
[135] PavanVatturiandWeng-KeenWong.2009.Categorydetectionusinghierarchicalmeanshift.In15thACMSIGKDD
InternationalConferenceonKnowledgeDiscoveryandDataMining.ACM,847–856.
[136] VincentVercruyssen,WannesMeert,andJesseDavis.2020.Transferlearningforanomalydetectionthroughlocal-
izedandunsupervisedinstanceselection.In34thConferenceonArtificialIntelligence(AAAI2020),32ndInnovative
ApplicationsofArtificialIntelligenceConference(IAAI2020),10thAAAISymposiumonEducationalAdvancesinArtifi-
cialIntelligence(EAAI2020)(NewYorkFebruary7–12,2020).AAAIPress,6054–6061.https://aaai.org/ojs/index.php/
AAAI/article/view/6068
[137] NikilWale,IanA.Watson,andGeorgeKarypis.2008.Comparisonofdescriptorspacesforchemicalcompound
retrievalandclassification.Knowl.Inf.Syst.14,3(2008),347–375.https://doi.org/10.1007/s10115-007-0103-5
[138] ZhenWangandChaoLan.2020.TowardsahierarchicalBayesianmodelofmulti-viewanomalydetection.In29th
InternationalJointConferenceonArtificialIntelligence(IJCAI2020),ChristianBessiere(Ed.).ijcai.org,2420–2426.
https://doi.org/10.24963/ijcai.2020/335
[139] SteveWebb,JamesCaverlee,andCaltonPu.2006.IntroducingtheWebbspamcorpus:Usingemailspamtoidentify
webspamautomatically.In3rdConferenceonEmailandAnti-Spam(CEAS2006)(July27–28,2006,MountainView,
California).http://www.ceas.cc/2006/listabs.html#6.pdf
[140] JamesD.Wilson,NathanielT.Stevens,andWilliamH.Woodall.2016.Modelingandestimatingchangeintemporal
networksviaadynamicdegreecorrectedstochasticblockmodel.arXivpreprintarXiv:1605.04049(2016).
[141] GangWuandEdwardY.Chang.2003.Adaptivefeature-spaceconformaltransformationforimbalanced-datalearn-
ing.In20thInternationalConferenceonMachineLearning(ICML-03).816–823.
[142] JunWu,JingruiHe,andYongmingLiu.2018.ImVerde:Vertex-diminishedrandomwalkforlearningimbalanced
networkrepresentation.In2018IEEEInternationalConferenceonBigData(BigData).IEEE,871–880.
[143] ShuangWu,JingyuZhao,andGuangjianTian.2022.Understandingandmitigatingdatacontaminationindeep
anomalydetection:Akernel-basedapproach.In31stInternationalJointConferenceonArtificialIntelligence(IJCAI
2022)(Vienna,Austria,23–29July2022)LucDeRaedt(Ed.).ijcai.org,2319–2325.https://doi.org/10.24963/ijcai.2022/
322
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

123:34 D.ZhouandJ.He
[144] DongboXi,BowenSong,FuzhenZhuang,YongchunZhu,ShuaiChen,TianyiZhang,YuanQi,andQingHe.2021.
Modelingthefieldvaluevariationsandfieldinteractionssimultaneouslyforfrauddetection.In35thAAAIConference
onArtificialIntelligence(AAAI2021),33rdConferenceonInnovativeApplicationsofArtificialIntelligence(IAAI2021),
11thSymposiumonEducationalAdvancesinArtificialIntelligence(EAAI2021)(VirtualEvent,February2–9,2021).
AAAIPress,14957–14965.https://ojs.aaai.org/index.php/AAAI/article/view/17755
[145] WeiXu,LingHuang,ArmandoFox,DavidA.Patterson,andMichaelI.Jordan.2009.Onlinesystemproblemdetection
byminingpatternsofconsolelogs.In9thIEEEInternationalConferenceonDataMining(ICDM2009)(Miami,Florida,
6-9December2009)WeiWang,HillolKargupta,SanjayRanka,PhilipS.Yu,andXindongWu(Eds.).IEEEComputer
Society,588–597.https://doi.org/10.1109/ICDM.2009.19
[146] PeiYang,JingruiHe,andJia-YuPan.2015.Learningcomplexrarecategorieswithdualheterogeneity.In2015SIAM
InternationalConferenceonDataMining.SIAM,523–531.
[147] PeiYang,HongxiaYang,HaodaFu,DaweiZhou,JiepingYe,TheodorosLappas,andJingruiHe.2015.Jointlymodeling
labelandfeatureheterogeneityinmedicalinformatics.ACMTransactionsonKnowledgeDiscoveryfromData(TKDD-
2015)(2015).
[148] ZhilinYang,WilliamW.Cohen,andRuslanSalakhutdinov.2016.Revisitingsemi-supervisedlearningwithgraph
embeddings.In33ndInternationalConferenceonMachineLearning(ICML2016)(NewYorkCity,NY,June19–24,
2016).40–48.
[149] YasserYasamiandFarshadSafaei.2017.Astatisticalinfinitefeaturecascade-basedapproachtoanomalydetection
fordynamicsocialnetworks.ComputerCommunications100(2017),52–64.
[150] Chin-ChiaMichaelYeh,YanZhu,LiudmilaUlanova,NurjahanBegum,YifeiDing,HoangAnhDau,DiegoFurtado
Silva,AbdullahMueen,andEamonnKeogh.2016.MatrixprofileI:Allpairssimilarityjoinsfortimeseries:Aunifying
viewthatincludesmotifs,discordsandshapelets.In2016IEEE16thInternationalConferenceonDataMining(ICDM).
IEEE,1317–1322.
[151] HaoYin,AustinR.Benson,JureLeskovec,andDavidF.Gleich.2017.Localhigher-ordergraphclustering.InProceed-
ingsofthe23rdACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining.ACM,555–564.
[152] HaoYin,AustinR.Benson,JureLeskovec,andDavidF.Gleich.2017.Localhigher-ordergraphclustering.In23rd
ACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining(Halifax,NS,Canada,August13–17,
2017).ACM,555–564.https://doi.org/10.1145/3097983.3098069
[153] MinjiYoon,BryanHooi,KijungShin,andChristosFaloutsos.2019.Fastandaccurateanomalydetectionindynamic
graphswithatwo-prongedapproach.In25thACMSIGKDDInternationalConferenceonKnowledgeDiscovery&Data
Mining.ACM,647–657.
[154] BingYu,HaotengYin,andZhanxingZhu.2018.Spatio-temporalgraphconvolutionalnetworks:Adeeplearning
frameworkfortrafficforecasting.In27thInternationalJointConferenceonArtificialIntelligence(IJCAI2018)(July
13–19,2018,Stockholm,Sweden),JérômeLang(Ed.).ijcai.org,3634–3640.https://doi.org/10.24963/ijcai.2018/505
[155] WenchaoYu,WeiCheng,CharuC.Aggarwal,KaiZhang,HaifengChen,andWeiWang.2018.Netwalk:Aflexible
deepembeddingapproachforanomalydetectionindynamicnetworks.In24thACMSIGKDDInternationalConfer-
enceonKnowledgeDiscovery&DataMining.ACM,2672–2681.
[156] ChangqingZhang,EhsanAdeli,TaoZhou,XiaoboChen,andDinggangShen.2018.Multi-layermulti-viewclassifi-
cationforAlzheimer’sdiseasediagnosis.In32ndAAAIConferenceonArtificialIntelligence(AAAI-18),30thInnovative
ApplicationsofArtificialIntelligence(IAAI-18),and8thAAAISymposiumonEducationalAdvancesinArtificialIntel-
ligence(EAAI-18)(NewOrleans,Louisiana,February2–7,2018)SheilaA.McIlraithandKilianQ.Weinberger(Eds.).
AAAIPress,4406–4413.https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/16864
[157] GuoxiZhang,TomoharuIwata,andHisashiKashima.2017.Robustmulti-viewtopicmodelingbyincorporatingde-
tectinganomalies.InJointEuropeanConferenceonMachineLearningandKnowledgeDiscoveryinDatabases.Springer,
238–250.
[158] SiZhang,DaweiZhou,MehmetYigitYildirim,ScottAlcorn,JingruiHe,HasanDavulcu,andHanghangTong.2017.
HiDDen:Hierarchicaldensesubgraphdetectionwithapplicationtofinancialfrauddetection.In2017SIAMInterna-
tionalConferenceonDataMining.SocietyforIndustrialandAppliedMathematics,570–578.
[159] WeiqiZhang,ChenZhang,andFugeeTsung.2022.GRELEN:Multivariatetimeseriesanomalydetectionfromthe
perspectiveofgraphrelationallearning.In31stInternationalJointConferenceonArtificialIntelligence(IJCAI2022)
(Vienna,Austria,23–29July2022),LucDeRaedt(Ed.).ijcai.org,2390–2397.https://doi.org/10.24963/ijcai.2022/332
[160] HandongZhaoandYunFu.2015.Dual-regularizedmulti-viewoutlierdetection..In24thInternationalJointConfer-
enceonArtificialIntelligence(IJCAI2015).4077–4083.
[161] YingZhao,JunjunChen,DiWu,JianTeng,andShuiYu.2019.Multi-tasknetworkanomalydetectionusingfeder-
atedlearning.In10thInternationalSymposiumonInformationandCommunicationTechnology(Hanoi,HaLongBay,
Vietnam,December4–6,2019).ACM,273–279.https://doi.org/10.1145/3368926.3369705
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.

RareCategoryAnalysisforComplexData:AReview 123:35
[162] Jia-XingZhong,NannanLi,WeijieKong,ShanLiu,ThomasH.Li,andGeLi.2019.Graphconvolutionallabelnoise
cleaner:Trainaplug-and-playactionclassifierforanomalydetection.InIEEEConferenceonComputerVisionand
PatternRecognition.1237–1246.
[163] DaweiZhou,JingruiHe,K.SelukCandan,andHasanDavulcu.2015.MUVIR:Multi-viewrarecategorydetection.In
24thInternationalJointConferenceonArtificialIntelligence(IJCAI-15).
[164] DaweiZhou,JingruiHe,YuCao,andJae-sunSeo.2016.Bi-levelraretemporalpatterndetection.InIEEEInternational
ConferenceonDataMiningSeries(ICDM2016).
[165] DaweiZhou,JingruiHe,HasanDavulcu,andRossMaciejewski.2018.Motif-preservingdynamiclocalgraphcut.In
IEEEInternationalConferenceonBigData(BigData2018)(Seattle,Washington,December10–13,2018),NaokiAbe,
HuanLiu,CaltonPu,XiaohuaHu,NesreenK.Ahmed,MuQiao,YangSong,DonaldKossmann,BingLiu,KisungLee,
JiliangTang,JingruiHe,andJeffreyS.Saltz(Eds.).IEEE,1156–1161.https://doi.org/10.1109/BigData.2018.8622263
[166] DaweiZhou,JingruiHe,HongxiaYang,andWeiFan.2018.SPARC:Self-pacednetworkrepresentationforfew-shot
rarecategorycharacterization.In24thACMSIGKDDInternationalConferenceonKnowledgeDiscovery&DataMining.
ACM,2807–2816.
[167] DaweiZhou,ArunKarthikeyan,KangyangWang,NanCao,andJingruiHe.2017.Discoveringrarecategoriesfrom
graphstreams.DataMiningandKnowledgeDiscovery31,2(2017),400–423.
[168] DaweiZhou,KangyangWang,NanCao,andJingruiHe.2015.Rarecategorydetectionontime-evolvinggraphs.In
IEEEInternationalConferenceonDataMining(ICDM2015).IEEE.
[169] DengyongZhou,JasonWeston,ArthurGretton,OlivierBousquet,andBernhardSchölkopf.2004.Rankingondata
manifolds.InAdvancesinNeuralInformationProcessingSystems.169–176.
[170] DaweiZhou,SiZhang,MehmetYigitYildirim,ScottAlcorn,HanghangTong,HasanDavulcu,andJingruiHe.2017.
Alocalalgorithmforstructure-preservinggraphcut.In23rdACMSIGKDDInternationalConferenceonKnowledge
DiscoveryandDataMining.ACM,655–664.
[171] DaweiZhou,LechengZheng,JiaweiHan,andJingruiHe.2020.Adata-drivengraphgenerativemodelfortemporal
interactionnetworks.In26thACMSIGKDDConferenceonKnowledgeDiscoveryandDataMining(KDD’20)(Virtual
Event,CA,August23–27,2020)RajeshGupta,YanLiu,JiliangTang,andB.AdityaPrakash(Eds.).ACM,401–411.
https://doi.org/10.1145/3394486.3403082
[172] Zhi-HuaZhou.2018.Abriefintroductiontoweaklysupervisedlearning.NationalScienceReview5,1(2018),44–53.
[173] ArthurZimek,ErichSchubert,andHans-PeterKriegel.2012.Asurveyonunsupervisedoutlierdetectioninhigh-
dimensionalnumericaldata.StatisticalAnalysisandDataMining:TheASADataScienceJournal5,5(2012),363–387.
Received15March2022;revised23May2023;accepted18September2023
ACMComputingSurveys,Vol.56,No.5,Article123.Publicationdate:November2023.