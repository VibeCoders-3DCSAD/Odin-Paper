|     | Proteus: | Shapeshifting |             |     |     | Desktop     |            | Visualizations |            |     |     | for Mobile |     | via |
| --- | -------- | ------------- | ----------- | --- | --- | ----------- | ---------- | -------------- | ---------- | --- | --- | ---------- | --- | --- |
|     |          |               | Multi-level |     |     | Intelligent |            |                | Adaptation |     |     |            |     |     |
|     |          | CanLiu        |             |     |     |             | SizheCheng |                |            |     |     | FengLiang  |     |     |
can.liu@ntu.edu.sg sizhe.cheng@ntu.edu.sg feng.liang@ntu.edu.sg
NanyangTechnologicalUniversity NanyangTechnologicalUniversity NanyangTechnologicalUniversity
|     |     | Singapore,Singapore |     |     |     | Singapore,Singapore |             |     |     |     |                    | Singapore,Singapore |     |     |
| --- | --- | ------------------- | --- | --- | --- | ------------------- | ----------- | --- | --- | --- | ------------------ | ------------------- | --- | --- |
|     |     | ZhibangJiang        |     |     |     |                     | LingruHuang |     |     |     | KavindaAthapaththu |                     |     |     |
zhibang.jiang@gmail.com huanglingru745@gmail.com kavinda.athapaththu@ntu.edu.sg
ProvidenceHealth&Services TheHongKongPolytechnic NanyangTechnologicalUniversity
6202 rpA 52  ]CH.sc[  1v99232.4062:viXra
|     | Renton,Washington,USA |     |     |     |     |     | University |     |     |     |     | Singapore,Singapore |     |     |
| --- | --------------------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | ------------------- | --- | --- |
HongKong,China
∗
YongWang
yong-wang@ntu.edu.sg
NanyangTechnologicalUniversity
Singapore,Singapore
| Abstract |     |     |     |     |     |     |     | Keywords |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
Withtheriseofmobile-firstconsumption,usersincreasinglyen- Mobile-friendly,visualization,multi-agent,largelanguagemodel,
| gagewithdatavisualizationsonmobiledevices.However,thevast |     |     |     |     |     |     |     | automaticdesign |     |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
majorityofexistingvisualizationsareoriginallyauthoredfordesk-
ACMReferenceFormat:
topenvironments.Duetosignificantdifferencesinviewportsize
CanLiu,SizheCheng,FengLiang,ZhibangJiang,LingruHuang,Kavinda
| and | interaction | paradigms, | directly | scaling | desktop | charts | often |     |     |     |     |     |     |     |
| --- | ----------- | ---------- | -------- | ------- | ------- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
Athapaththu,andYongWang.2026.Proteus:ShapeshiftingDesktopVisu-
resultsinillegibletext,informationloss,andinteractionfailures.
alizationsforMobileviaMulti-levelIntelligentAdaptation.InProceedings
Tobridgethisgap,weproposeanautomatedframeworktoadapt ofACMDesigningInteractiveSystemsConference(DIS’26).ACM,NewYork,
desktop-basedvisualizationsformobilescreens.Bysystematically NY,USA,18pages.https://doi.org/XXXXXXX.XXXXXXX
categorizingtheoperationsinvolvedintheadaptationprocess,we
establishamulti-leveldesignspace.Thisspacedefinesevolution
|     |     |     |     |     |     |     |     | 1   | Introduction |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
rulesspanningfromtheglobaltopologylevel,throughtherefer-
Theubiquityofmobilecomputinghasfundamentallyreshapedin-
| ence | frame | level, down to | the visual | elements | level. | Guided | by  |     |     |     |     |     |     |     |
| ---- | ----- | -------------- | ---------- | -------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
formationaccess.Withtheriseofmobile-firstconsumption,users
thistheoreticalframework,wedevelopedProteus,alargelanguage
increasinglyengagewithdatavisualizationsonhandhelddevices,
| model–driven |     | multi-agent | system | that automatically |     | parses | the |     |     |     |     |     |     |     |
| ------------ | --- | ----------- | ------ | ------------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
rangingfrommonitoringfinancialdashboardstotrackingpublic
| online | visualizations, | predicts | optimal | transformation |     | strategies |     |     |     |     |     |     |     |     |
| ------ | --------------- | -------- | ------- | -------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
healthstatistics.Despitethisshift,thevastmajorityofvisualiza-
withinthedesignspace,andgeneratesequivalent,highlyreadable
visualizationsformobiledevices.Casestudiesandanin-depthuser tionsarestillauthoredindesktopenvironments,implicitlydesigned
forlandscapeorientation,highpixelprecision,andmouse-hover
| study | with | 12 participants | demonstrate | the | effectiveness |     | and us- |     |     |     |     |     |     |     |
| ----- | ---- | --------------- | ----------- | --- | ------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
affordances.Thisdisparitycreatesacriticalauthoring–consumption
abilityofProteus.
gap.Whenvisualizationsdesignedforwidemonitorsareported
|     |     |     |     |     |     |     |     | to small | mobile | screens, | the | user experience | frequently | deterio- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | -------- | --- | --------------- | ---------- | -------- |
CCSConcepts
rates.Simplescalingoftenresultsinillegibletext,overlappingel-
•Human-centeredcomputing→Interactivesystemsandtools;
ements,andthelossofinteractiveprecision.Toaddressthis,the
Visualizationsystemsandtools;Interactiontechniques.
visualizationcommunityhasdevelopedtechniquesforresponsive
|     |     |     |     |     |     |     |     | visualization |     | (RV). Seminal | work | by Hoffswell | et al. | [17] estab- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------- | ---- | ------------ | ------ | ----------- |
∗Y.Wangisthecorrespondingauthor. lishedadesignspaceforflexiblevisualizations,categorizingtech-
|     |     |     |     |     |     |     |     | niques | into | layout adjustments, |     | scale modifications, |     | and encod- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---- | ------------------- | --- | -------------------- | --- | ---------- |
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
ingchanges.MorerecentsystemssuchasMobileVisFixer[53]fur-
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcita- therautomatepartsofthisprocessbyoperatingonrenderedSVG
tiononthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthan visualizationsthroughanintermediatestructuredrepresentation.
theauthor(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyother- However,suchsystemsremaintiedtoapredefinedrepresentation
wise,orrepublish,topostonserversortoredistributetolists,requirespriorspecific
permissionand/orafee.Requestpermissionsfrompermissions@acm.org. andtransformationpipeline,whichcanlimittherangeofadapta-
DIS’26,Singapore
|     |     |     |     |     |     |     |     | tions | they support | in  | practice. | Cicero [21] | further advances | this |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------------ | --- | --------- | ----------- | ---------------- | ---- |
©2026Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
lineofworkbyprovidingadeclarativegrammarforresponsivevi-
ACMISBN978-1-4503-XXXX-X/2018/06
https://doi.org/XXXXXXX.XXXXXXX sualizationtransformations,allowingdesign-agnosticadaptation

DIS’26,June13–17,2026,Singapore Trovatoetal.
rules to be reused across visualizations; nevertheless, like many • Proteus, an LLM-driven multi-agent framework that auto-
priorsystems,itsscoperemainscenteredonstructuredspecifica- matessemanticparsing,planning,codegeneration,andqual-
tionsratherthanthediverseimplementationstylesfoundinprac- ityevaluationformobilevisualizationadaptation.
tice. In practice, many web charts are implemented with hetero- • Casestudiesandacontrolleduserstudywith12participants
geneous tool-chains (such as D3, Plotly, or custom SVG/HTML), demonstratingthatoursemanticre-authoringapproachsig-
makingitdifficultforsuchspecification-boundapproachestogen- nificantlyoutperformsastrongLLM-basedbaselineacross
eralizeacrossplatformsandimplementationstyles.Moreover,ex- renderingsuccessandallfiveevaluationdimensionsonmo-
isting RV techniques predominantly rely on a flat taxonomy of biledevices.
geometricheuristics.Theytreatadaptationasalayoutpuzzle,re-
MoreexamplevisualizationsprocessedbyProteusformobilede-
arrangingboundingboxesorshrinkingelementstofittheview-
vicesareavailableathttps://vis2mobile.vercel.app.
port.Whileeffectiveforsimplecharts,thisgeometry-centricpar-
adigmfallsshortwhenhandlingcomplexdata.Itlackssemantic
2 RelatedWork
understanding,oftenresortingtohidinglabelsortruncatingtext
blindly,whichcompromisesinformationfidelity.Inaddition,most Wesituateourworkattheintersectionofresponsivevisualization
methodstreatoperationsinisolationanddonotaccountforhow techniques,automateddesignsystems,andtheemergingapplica-
ahigh-leveldecision(forexamplechangingacharttypeorreflow- tionofmulti-agentsystems.
ingagrid)structurallyconstrainslower-levelelements(forexam-
pleaxisticks,legends,andannotations). 2.1 ResponsiveVisualizationTechniques
To bridge this gap, we argue that effective mobile adaptation
Adaptingvisualizationsformobiledevicesinvolvesbalancingthe
requiresmorethanlayoutresponsiveness;itdemandsautomated
reduction of screen space with the preservation of information
semanticre-authoring.Inthispaper,wepresentProteus,anauto-
density and readability [17]. Early approaches relied on interac-
matedframeworkdrivenbyLargeLanguageModels(LLMs)that
tive exploration techniques, such as zooming, panning, and fish-
transformsdesktopchartsintomobile-optimizedvisualizations.Our
eyedistortions,tonavigatelargechartsonsmallscreens[4].Later,
approachisgroundedinanovelmulti-leveldesignspacethatorga-
researchers formalized specific adaptation actions, such as resiz-
nizesadaptationasahierarchyofdecisionsandrefinements,rather
ing, repositioning, and modifying encodings, leading to declara-
thanaflatlistofrules.Unlikepriorwork,ourframeworkoperates
tivelibrarieslikeRespVis[3]andCicero[21],whichallowauthors
acrossthreedistinctlayers:Level1:GlobalTopology,whichmakes
to manually define rules, and reusable transformation specifica-
macroscopicdecisions(forexampleaxistranspositionandgridre-
tions.Toreducethemanualeffortofdefiningrules,recentworks
flow)thatdefinetheoverallspatialstructureofthevisualization;
have shifted towards automated layout optimization. MobileVis-
Level 2: Reference Frame, which adjusts axes, legends, and scales
Fixer[54]employsareinforcementlearningframeworktrainedon
(forexampletickdecimationandscrollinjection)tobalancequanti-
humanpreferencestoautomaticallyre-scaleandrepositionSVG
tativeprecisionwithlegibility;andLevel3:VisualElements,which
elements.Similarly,Zengetal.[56]utilizedsimulatedannealing
performsmicro-levelrefinements(forexamplesemanticabbrevia-
topreservespatialrelationshipsindashboards,whileconstraint-
tionandlabelexternalization)onmarksandtexttooptimizethe
basedmethodstriggeradaptationsbasedonelementlegibilityrather
useofdatainkonsmallscreens.
thanstaticscreenwidths[40].
Guidedbythishierarchicalframework,Proteusemploysamulti-
Theseexistingframeworksprimarilyoperateataflatlevel.They
agentarchitecture.ByleveragingthesemanticreasoningofLLMs,
treat adaptation as a bounding-box rearrangement problem and
thesystemparsesthesourcevisualizationtopredictoptimaltrans-
cannotperformcontent-basedre-authoring,suchaslinguistically
formation strategies, and generates executable code. This allows
abbreviatinglabels,orswitchingcharttypestosuitthedata’smes-
Proteustoperformsophisticatedadaptations,suchasconvertinga
sageonasmallercanvas.Thislimitationoftenresultsindesigns
static small-multiple view into an interactive carousel or seman-
thataretechnicallyresponsivebutcognitivelycluttered.
tically shortening categorical labels. We present case studies to
showhowProteusworksfordifferenttypesofvisualizationsfrom
2.2 AutomatedVisualizationSystems
different.Also,weevaluateProteus inacomparativeuserstudy
with12participantsagainstamulti-agentLLM-basedbaselineon Automatedvisualizationdesignaimstorecommendorgenerateef-
adiversebenchmarkofreal-worldwebvisualizations.Theresults fectivecharts,givendataandtasks,reducingtheeffortofmanual
showthatourapproachachieveshigherrendersuccessratesand authoring—aneffortthatremainschallengingevenforexperts[38].
significantlybetterratingsacrossfivedimensions:executioncom- Over the years, prior work has evolved along three major direc-
pleteness,datafidelity,perceptualreadability,visualaesthetics,in- tions.First,rule-andconstraint-basedsystemsmakedesignknowl-
teractionreasonableness,accordingtoWilcoxonsigned-ranktests edgeexplicitandcomputable,fromfoundationssuchasAPT[30]
(𝑝 <0.05forfidelity/readabilityand𝑝 <0.001foraestheticsand tolaterrecommenderframeworks(e.g.,ShowMe[31],Voyager[51],
interaction). andDraco[34]),aswellasquery-drivenexploratoryapproaches[7,
Insummary,ourcontributionsareasfollows: 45]. Second, data-driven methods learn charting decisions from
largecorporaofdata-visualizationpairs[8,19,26,29,35].Third,
• Amulti-leveldesignspacethatadvancesbeyondflatrespon- visualizationreuseandrecoverytechniquesinferstructurefrom
sivetaxonomiesbymodelingthehierarchicalpropagation existingartifacts,e.g.,recoveringencodingsfromrenderedcharts
ofconstraintsfromglobalstructuretoindividualvisualmarks. orextractingreusabletemplatestoberepopulatedwithnewdata,

Proteus:ShapeshiftingDesktopVisualizationsforMobileviaMulti-levelIntelligentAdaptation DIS’26,June13–17,2026,Singapore
enablingauthoringbyreuseratherthanfromscratch[22,24,25, thefundamentalconflictbetweeninformationdensity(highondesk-
| 28,37,39,55,57]. |     |     |     |     |     |     | top)andperceptualbandwidth(lowonmobile). |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- |
Recently,LLMshaveencouragedagenticworkflowsthatdecom-
pose visualization generation into planning, coding, and valida- • R1.EnsurePerceptualScalability.Mobilescreenssuffer
tion,sometimeswithmultimodalfeedbacktoimprovecorrectness[13, from a scarcity of pixels. A direct reduction in size leads
36, 50]. However, most such systems focus on Text-to-Vis gen- toocclusionandillegibility.Thisrequiresaggressiveopera-
eration,whiletheVis-to-Visadaptationsettingremainsunderex- tions(suchasdecimationorre-layout)toensurethatallren-
plored: given a desktop visualization, the system must infer its deredelements(text,axes,marks)remainlegibleanddistin-
structureandinteractionintentandthenre-authoritformobile guishable,prioritizingthevisibilityofessentialsignalsover
constraints.Priormobile-orientedwork(e.g.,MobileVisFixer[53]) decorativefidelity.
primarily targets layoutrepairvia learning-based methods, leav- • R2.PreserveSemanticEquivalence.Simplyresizingavi-
ingadaptationofmulti-vieworganizationandinteractionredesign sualizationcanhideinformationthatisnecessaryforinter-
largelyopen. pretation.Forexample,hidingaxislabelsmaymakeachart
difficultorimpossibletounderstand.Therefore,adaptation
2.3 Multi-AgentSystemsforVisualization shouldgobeyondlayoutadjustmentandselectivelyrevise
|             |     |                  |     |            |           |          | visual | elements | while preserving | the          | original    | meaning of |
| ----------- | --- | ---------------- | --- | ---------- | --------- | -------- | ------ | -------- | ---------------- | ------------ | ----------- | ---------- |
| Multi-agent | and | mixed-initiative |     | ideas have | long been | explored |        |          |                  |              |             |            |
|             |     |                  |     |            |           |          | the    | data. To | do so, the       | system needs | to consider | the data   |
tomakecomplexinteractivetasksmoremanageable—systemsdis-
contextandtheroleofeachvisualcomponent.
| tribute reasoning |     | and responsibilities |     | across | cooperating | compo- |       |          |           |              |         |          |
| ----------------- | --- | -------------------- | --- | ------ | ----------- | ------ | ----- | -------- | --------- | ------------ | ------- | -------- |
|                   |     |                      |     |        |             |        | • R3. | Exchange | Space for | Time. Mobile | devices | lack the |
nentswhilekeepinghumansincontrolthroughdirectmanipula-
spatialwidthofdesktopsbutpossesssuperioraffordances
tionandincrementalrefinement[18,20].Invisualization,collab-
fortouchandscrollnavigation.Theframeworkcanleverage
orativeplatformsintroducedearlycoordinationmechanismssuch
|           |             |     |            |      |               |          | thisbyconvertingspatialdensity |     |     | intotemporalinteraction. |     |     |
| --------- | ----------- | --- | ---------- | ---- | ------------- | -------- | ------------------------------ | --- | --- | ------------------------ | --- | --- |
| as shared | annotations | and | versioning | [16, | 48]. Building | on clas- |                                |     |     |                          |     |     |
Static,crowdedelements(likesmallmultiplesordenseaxes)
| sic foundations | in  | distributed | problem | solving | and | collective in- |     |     |     |     |     |     |
| --------------- | --- | ----------- | ------- | ------- | --- | -------------- | --- | --- | --- | --- | --- | --- |
shouldbetransformedintodynamic,scrollable,orcollapsi-
| telligence | [5, 32, | 52], recent | advances | in  | large language | models |     |     |     |     |     |     |
| ---------- | ------- | ----------- | -------- | --- | -------------- | ------ | --- | --- | --- | --- | --- | --- |
blecomponents,allowinguserstoexplorehigh-resolution
| (LLMs) have | further | encouraged |     | multi-component |     | architectures |      |         |               |            |        |             |
| ----------- | ------- | ---------- | --- | --------------- | --- | ------------- | ---- | ------- | ------------- | ---------- | ------ | ----------- |
|             |         |            |     |                 |     |               | data | through | gesture-based | navigation | rather | than visual |
whererole-specializedagentsormodulescanplan,invoketools,
scanning.
reflect,andcoordinatemodel–toolpipelines[14,23,41,42,44,49].
• R4.RespectCross-LevelDependencies.Avisualization
However—asvisualizationdesignautomationremainschallenging—
isahierarchicalscenegraph.Achangeintheglobalchart
priorsystemsmostlyrelyonheuristicsorfixedtemplatesforchart
type(e.g.,transposingaxes)alterstheconstraintsforlower-
generationorscalingacrossdevicesratherthantrulyagent-based
levelelements(e.g.,labelorientation).Thedesignspaceshould
coordination[2,9,10,15].Athanor[27]insteadusesmultiplecol-
formallymodelthesedependencies.Ratherthanasetofiso-
laboratingagentstoenablemoreaccurateintentinterpretationfor
latedtweaks,adaptationshouldbemodeledasatop-down
addinginteractiontoanexistingvisualization.Ourworkadopts
propagationofconstraintswheretopologicaldecisionsdic-
MAS-inspiredprinciplestostructurecollaborativeLLMagentsfor
tatethevalidparameterspaceforatomicelements.
| Vis-to-Vis | adaptation, | enabling | semantic | reasoning |     | over desktop |     |     |     |     |     |     |
| ---------- | ----------- | -------- | -------- | --------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
visualizationsandcoordinateddecisionstoproducefaithfulyetop-
Therequirementsabovenecessitateaframeworkthathandles
timizedmobilecounterparts.
adaptationatdifferentlevelsofabstraction.However,aflatlistof
operatorsisinsufficientforthehierarchicalnatureofR4.Tostruc-
3 AMulti-levelDesignSpaceforMobile
turethisspacesystematically,wedecomposethevisualizationinto
VisualizationAdaptation threelevels.Weobservethatavisualizationisconstructedinthree
distinctlogicalstages:definingthespatialsubstrate,establishing
Thetransitionfromdesktoptomobilevisualizationisnotatrivial
|           |           |       |                        |     |         |          | the reference | context, | and populating | the | data content. | Accord- |
| --------- | --------- | ----- | ---------------------- | --- | ------- | -------- | ------------- | -------- | -------------- | --- | ------------- | ------- |
| graphical | rescaling | task; | it is a reconstruction |     | process | governed |               |          |                |     |               |         |
by competing constraints. Desktop environments are character- ingly,wepartitionourdesignspaceintothreelayersasillustrated
| izedbylandscapeorientation,highpixelprecision,mouse-hover |     |     |     |     |     |     | inFigure1: |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
affordances,andexpansivescreenrealestate.Incontrast,mobile
|              |        |        |          |     |             |              | • Level | 1: Global | Topology. | This level | dictates | the macro- |
| ------------ | ------ | ------ | -------- | --- | ----------- | ------------ | ------- | --------- | --------- | ---------- | -------- | ---------- |
| environments | impose | strict | physical | and | interaction | limitations: |         |           |           |            |          |            |
scopicarrangement,encompassingcontainerlayout,coor-
portraitorientation,fat-fingerinput,andnarrowhorizontalband-
width. To navigate this trade-off systematically, we first identify dinatesystems,andfacettopology.Itdefineswherecontent
thecoredesignrequirementsandthenmapthemtoahierarchical canexistanddeterminestheboundingboxesforalllower
|     |     |     |     |     |     |     | levels. | In mobile | adaptation, | this often | necessitates | struc- |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------- | ----------- | ---------- | ------------ | ------ |
designspace.
turalreconfiguration(addressingthedensityandhierar-
chyrequirementsinR1andR4),suchastransformingcom-
3.1 DesignRequirementsforMobile
|     |     |     |     |     |     |     | posite, | high-density | desktop | dashboards | into | decomposed |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | ------- | ---------- | ---- | ---------- |
VisualizationAdaptation
orserializedlayouts(e.g.,splittingamulti-viewdashboard
Tobridgethegapbetweendesktopauthoringandmobileconsump- intoseparatemobilepagesorreflowingagridofchartsinto
tion,weidentifyfourdesignrequirements.Thesearederivedfrom averticalstack).

DIS’26,June13–17,2026,Singapore Trovatoetal.
Figure1:Theproposedmulti-leveldesignspaceformobilevisualizationadaptation.Itorganizestransformationoperators
intothreelevels:(1)GlobalTopology,whichrestructurestheoverallspatiallayoutandcoordinatesystems;(2)ReferenceFrame,
whichadjustsaxes,ticks,legends,andviewports;and(3)VisualElements,whichrefinestherenderingofmarksandtextfor
mobilescreens.
• Level2:ReferenceFrame.Thislevelmanagesthevisual theaspectratio(typicallywidelandscapevs.narrowportrait).Co-
elements that help users interpret data values in the allo- ordinatetransformationoperatorsaddressthisbyremappingthe
cated space,including axes, legends, andscales. Itdefines spatialencodingchannels.
howtomeasureandinterpretthespaceallocatedbyLevel1.
Adaptationherefocusesoncontextualoptimization(inline • AxisTransposition.Mobiledevicestypicallyfavorapor-
withR1andR2):axesandlegendsmustberesizedorrepo- traitorientation(height>width),whichstandsinsharpcon-
sitioned to maximize space utilization, and in some cases trasttothelandscapelayoutscommonondesktopdisplays.
auxiliaryguidesorlegendsmustbeexplicitlyaddedtopre- To address this geometric inversion, transposing the axes
servesemanticinterpretabilityundermobileconstraints. becomesafundamentaladaptationstrategy.Forordinalor
• Level 3: Visual Elements. This level governs the visual nominaldata(e.g.,barcharts),limitedhorizontalbandwidth
marks(bars,points,lines)andthetextelements,thatis,the oftenconstrainsthenumberofcategoriesthatcanbedis-
actualcontentthatpopulatesthereferenceframe.Sincemo- played and can lead to overly dense labels along the hor-
bile screens often render desktop-sized elements spatially izontal axis. This operator swaps the horizontal and verti-
prohibitive (e.g., long labels causing overflow), this layer calaxes,mappingthecategoricaldimensionontothey‑axis.
handles granular adjustments (e.g., text wrapping, seman- Suchtranspositionleveragesthenativeverticalscrollingaf-
ticabbreviation,andmarkrescaling)toensureperceptual fordance of mobile interfaces, allowing more data points
scalabilityandsemanticfidelityasrequiredbyR1andR2, tobeshownwithoutcompression.Moreover,becausemost
whilealsopreparingelementstoparticipateininteraction text(e.g.,English)islaidouthorizontally,placingcategory
patternsthatrealizeR3. labelsalongtheverticalaxisalsohelpsavoidthecrowding
issuesthatwouldotherwisearisefromdenselypacked,ro-
3.2 Level1:GlobalTopology tatedlabels.
• LayoutSerialization.Ondesktopdisplays,amplepixelband-
Thehighestleveladdressesthemacroscopicstructureofthevisual-
widthoftenallowsmultipledatalayerstobeoverlaidwithin
ization.Adaptationhereinvolvesalteringthespatialarrangement
asinglesharedcoordinatespacefordirectcomparison.On
ofviews,definingthecontainerboundaries,andfundamentallyre-
mobilescreens,however,suchmultilayeroverlayscanbe-
orientingthecoordinatesystem.Sincethesedecisionsdetermine
comedifficulttoreadduetolimitedresolutionandscreen
theboundingboxesandspatiallogicofthereferenceframesand
size.Forlayersthatdonotstrictlyneedtobesuperimposed,
visualelements,theymustberesolvedfirst.
thisoperatorappliesdecomposition:itsplitsthecombined
3.2.1 CoordinateTransformation. Oneofthemostsalientdispari- viewintotwoormoreseparatechartsandserializesthem
tiesbetweendesktopandmobileenvironmentsistheinversionof inthelayout.Thisreducesvisualclutterwhilepreserving

Proteus:ShapeshiftingDesktopVisualizationsforMobileviaMulti-levelIntelligentAdaptation DIS’26,June13–17,2026,Singapore
theessentialcomparativecapabilitythroughsequentialin- operatorsfocusesonpreservingtheinterpretabilityofaxesunder
spectionratherthansimultaneousoverlay. compressionbyeitherreducingthenumberofvisibletickswhen
interpolationispossible,orreorientinglabelswheneverycategory
3.2.2 FacetManagement. Smallmultiples(facetedviews)present
mustremainexplicitlyshown.
a significant challenge. For example, a 3 × 2 grid effective on a
monitorbecomesillegibleonaphone. • TickDecimation:Forcontinuousattributes,suchasquan-
titativeortemporalscales,reducinglabeldensityrarelycom-
• GridReflowThisoperatoraddressesthelegibilitycollapse
promisesinformationretrievalduetotheuser’scapacityfor
ofspatiallydistributedsmallmultiplesonnarrowscreens.It
linearinterpolation.Forinstance,reducinga12-monthaxis
modifiesthelayouttopologybyreducingthegrid’scolumn
toquarterlyticks(“Jan”,“Apr”,“Jul”,“Oct”)allowsusersto
cardinality,effectivelyenforcingaserializationoftheview.
instinctivelyinferthepositionsofintermediatemonths(e.g.,
Forinstance,acompact3×2desktopgridisreflowedinto
“Feb”,“Mar”).Thisoperatorimproveslegibilitybyenforcing
averticalstack(𝑁 = 1),allowingeachindividualchartto
sparsitywhilerelyingonthepredictablenatureofthescale
expandtothefullwidthofthedeviceviewport.
topreservetheuser’smentalmodel.
3.2.3 EncodingTransformation. Incertainscenarios,thegeomet- • LabelRotation:Fornominaldataattributes(e.g.,specific
ricfootprintofadesktopchartisfundamentallyincompatiblewith categorynames),tickdecimationisofteninappropriatebe-
mobileconstraints,regardlessoflayoutadjustments.Thisnecessi- cause users cannot infer missing values via interpolation,
tatesatransformationofthevisualencodingitselftoreducehori- unlikewithcontinuousattributes.Whenpreservingthevis-
zontalspatialdemand. ibilityofeverycategoryismandatorybuthorizontalspaceis
• MarkTransmutation:Complexdiscretegeometries,such insufficient,thisoperatoractsasacriticaladaptationstrat-
asgroupedbarcharts,sufferfromseverecrowdingonnar-
egy.Byanglingtext(typically45∘ or90∘),itutilizesverti-
rowscreensduetothehighnumberofbarspertick.Thisop- calspacetopreventoverlap.Importantly,theeffectiveness
eratortransmutesthemarktypeintoamorecompactform. oflabelrotationislanguage-dependent:certainwritingsys-
Forinstance,convertinggroupedbarsintomulti-linecharts tems(e.g.,Mongolianscript)areinherentlydesignedforver-
maintainsthemulti-seriescomparisonwhilereducingthe ticallayout,whilesome(e.g.,Chinesecharacters)support
requiredpixelsperdatapoint. bothhorizontalandverticalorientationswithrelativelymi-
norlegibilityloss.
3.3 Level2:ReferenceFrame
3.3.3 Legend Adaptation. Legends often consume valuable hori-
Oncetheglobaltopologyisestablished,thedesignspacefocuses zontalspaceondesktopdisplays.Adjustingthepositionoflegends
onthereferenceframe.Theaxesandlegendsactasthebridgebe- usuallydoesnotincuranylossofinformation.
tweenrawdatavaluesandscreencoordinates.Mobileadaptation
• Repositioning: Changing the placement of legends typi-
hereprimarilyconcernsthetrade-offbetweenprecision(showing
callydoesnotleadtoinformationloss.Forexample,legends
allticks)andlegibility(showingreadableticks).
canbemovedfromaright-handsidebartothetoporbottom
3.3.1 DomainandRangeManipulation. Inmobileenvironments, ofthechart,orconvertedintoinlinelabelsthatareattached
wheretheavailable”pixelbudget”isseverelyrestricted,thedefault directlytothecorrespondingvisualelements(e.g.,linesin
mappingstrategiesusedondesktopsoftenresultincompressedor alinechart).Inaddition,legendscanoftenbeturnedinto
indistinguishablevisualpatterns.Adaptationatthislevelfocuses interactivebuttons,allowinguserstotapthemtocustomize
onoptimizingthisprojectiontomaximizediscernibility. whichdataseriesareshown.
• ViewportConstriction:Thisoperatoraddressesthelossof 3.3.4 InteractionInjection. Wherestaticspatialresolutionfails,tem-
resolutioncausedbyscalingdownalargedatasettoasmall poral interaction compensates. We introduce two operators that
screen.Ratherthanpreservingtheglobalextent(0-100%),it shifttheburdenfromvisualperceptiontomanualmanipulation,
semanticallycropsthevisibleaxisdomaintoaspecificre- adheringtotheprincipleofDetails-on-Demand[43].
gionofinterest.Forexample,achartmightzoominona
• ViewportDecoupling:Whendatadensityexceedsthephys-
denseclusterofvaluesordefaulttoshowingonlythemost
icalpixellimit,compressingtheentiredatasetrendersitil-
recenttimewindow,forcingtheviewertoscrollorinteract
legible.Thisoperatordecouplesthelogicalchartwidthfrom
toseethehistoricalcontext.Thiszoomingtradesglobalcon-
thephysicalviewportwidth.Itenablesnavigationthrough
textforlocalfidelity.Crucially,thisconstrictionistypically
diverse mechanisms: direct manipulation (panning the x-
pairedwithinteractiveaffordances,suchasarangeslider,a
axis or scrolling the virtual canvas) or proxy control (us-
mini-mapbrush,orpangestures,enablinguserstodynami-
inganauxiliarywidgetlikearangeslider).Thismaintains
callytraversethehiddendata.Thisapproachimplementsa
ahigh-resolutiondatarepresentation,allowinguserstoex-
”Focus+Context”strategy,tradingimmediateglobalvisibil-
plorethecontinuumsequentiallyratherthansimultaneously.
ityforlocalfidelitywhilepreservingnavigationalaccess.
• TooltipEnabling:Asaconsequenceofaggressivetickdec-
3.3.2 Axes Optimization Strategy. On small or horizontally con- imation(Level2)andmarkrescaling(Level3),theprecise
strained displays, axes are often the first component to become values of data points are often visually abstracted in the
problematic:asticklabelscompeteforlimitedwidth,theybegin static view. This operator injects an interactive layer, typ-
tooverlap,quicklyrenderingthescaleunreadable.Thisfamilyof ically triggered by touch or a long-press, to display exact

DIS’26,June13–17,2026,Singapore Trovatoetal.
valuesviaoverlays.Thiscompensatesforthelossofstatic renderingeverydatapointresultsinvisualnoiseandren-
fidelity, ensuring that quantitative precision is retrievable deringbottlenecks.Thisoperatorreducesvisualdensityby
despitethesimplifiedvisualpresentation. eitherselectingarepresentativesubset(sampling)orcom-
biningproximaldatapointsintosummarystatistics(i.e.,ag-
3.4 Level3:VisualElements gregationorbinning),ensuringthattheoverarchingtrend
remainsdiscernible.
Thedeepestlevelofthehierarchygovernsthe“atomic”constituents
ofthevisualization:thegeometricmarksrepresentingdatapoints
3.4.3 Visibility and Progressive Disclosure. Mobile interfaces ne-
andtheirassociatedtextualannotations.Whileupperlevelsdefine
cessitateastrategyofprogressivedisclosure,showingonlywhat
thecontainerandreferenceframe,thislevelmanagestheactual
isessentialandhidingsecondaryinformationuntilrequested.
dataink.Constraintsfromtheglobal-topologylevel(layout)and
reference-framelevel(range)propagatedownward,oftencreating • FilterEnabling:Forchartswithhigh-cardinalityelements,
extremespatialscarcityforthesefundamentalelements.Adapta- suchasgroupedbarcharts,displayingallseriessimultane-
tionherefocusesonmaintainingSemanticFidelity(R2)andIn- ouslyonanarrowscreenoftenresultsinoverlythin,hard-
teractionFeasibility(R3)atthegranularlevel. to-read bars. This operator mitigates overcrowding by in-
troducingexternalcontrols,suchassegmentedbuttonsor
3.4.1 Semantic Text Adaptation. Text is the most rigid element
filterchips.Insteadofpresentingadensevisualization,ital-
invisualizationdesign;unlikegeometry(bars,lines,orareas),it
lowsuserstomanuallytogglethevisibilityofspecificdata
cannot be linearly scaled down without losing legibility. Conse-
subsets.Forexample,agroupedbarchartshowingtrends
quently,textadaptationonmobiledevicesrequiresoperationsthat
acrossmultiplecategoriescanbetransformedintoacleaner,
prioritizemeaningoverform.
morelegibleviewwhereuserscanfocusononeseriesata
• SemanticAbbreviation:Thisoperatoraddressesthecon- timethroughabuttonstrip,tradingimmediatecross-series
flictbetweenlimitedhorizontalbandwidthandlongnomi- comparisonforenhancedvisualclarity.
nallabels.Insteadofnaivetruncation(whichdestroysmean- • Context Collapsing: Auxiliary context, such as lengthy
ing,e.g.,“South…”couldbe“SouthDakota”or“SouthCar- subtitlesorsecondarylegends,consumesvaluabledataink.
olina”),thisoperatoremploysdomain-specificlogictocom- Thisoperatorencapsulatessuchauxiliaryinformationinin-
pressstringlengthwhilepreservingsemanticdistinguisha- teractivetogglesthatuserscanexpandondemand.Inthis
bility.Forinstance,“UnitedStates”ismappedto“USA”,and way,staticdetailsarehiddenbydefaulttomaximizetheplot
“January2023”iscompressedto“23Jan”. area,yetremaineasilyaccessiblewhenneeded.Thispattern
• LabelExternalization:Whendatadensityprohibitsin-situ is also common on mobile devices, where limited screen
labeling(placinglabelsdirectlynexttomarks),textocclu- spaceencouragescollapsingsecondarydetailsbehindtap-
sionbecomesmoresevereinmobileenvironments.Thisop- pablecontrols.
eratordecouplesthelabelfromitsspatialpositionbyreplac-
ingtheon-charttextwithacompactindicator.Thefulltex-
3.5 ConstraintPropagationandInter-level
tualcontentisthenrelocatedtoanexternallistorlegend
Dynamics
belowthechart,resolvingtheclutterwithoutdiscardingin-
formation. Crucially, the three levels in our design space do not operate in
• Text Wrapping: Long titles or annotations often exceed isolation.Decisionsmadeathigherlevelsimposehardconstraints
theviewportwidthinportraitmode.Thisoperatorutilizes onwhatisfeasibleatlowerlevels,andlower-levelrequirements
verticalspacetocompensateforhorizontalscarcitybyintro- caninturntriggerstructuraladjustmentsupstream.
ducinglinebreaks.Ittransformsasingle-linestringintoa Changesattheglobaltopologylevelpropagatedownward.Op-
multi-lineblock,ensuringthefullcontextisvisiblewithout erations such as axis transposition, layout serialization, or grid
forcinghorizontalscrolling. reflow alter the aspect ratio and container boundaries, which in
turnconstrainhowlegendscanberepositionedandwhetherlabels
3.4.2 GeometryandDataReduction. Onsmallscreens,thephys- mustbeshortenedorexternalized(subsection3.3,subsection3.4).
icalsizeofvisualmarksmustbalancetwocompetingobjectives: Forexample,whenadensesmall-multiplegridisreflowedintoa
theymustbesmallenoughtopreventoverplotting,yetlargeenough verticalstack,legendsmayneedtomovetothetoporbeconverted
tobeaccuratelyperceivedandtouched. intoinlinelabels,andlongcategorynamesmayrequiresemantic
• ElementRescaling:Althoughthescreendimensionscon- abbreviationorlabelexternalizationtoremainreadable.Attheref-
tract, visual marks cannot undergo a simple linear down- erenceframelevel,reducingtickdensity(tickdecimation)isoften
scaling.Suchareductionwouldrenderelementstoominute pairedwithinteractivemechanismssuchastooltipsorfilters,so
foraccurateinteraction.Instead,thisoperatorenforcesarel- thatuserscanstillretrieveprecisevaluesondemanddespitefewer
ative enlargement of geometric primitives (e.g., points or visiblelabels(subsection3.3).Likewise,whenthevisiblerangeis
bars),ensuringthattheymaintainasufficientphysicalsize narrowedthroughviewportconstriction,itiscommonlycombined
toaccommodatecoarsetouchinputs,evenifthisdispropor- with viewport decoupling, allowing users to access the full data
tionatescalingnecessitatesareductionindatadensity. extentviapanningorrangeselection.Atthevisualelementslevel,
• DataSamplingandAggregation(sampleData):Whenthe operatorssuchaselementrescalingaredirectlydeterminedbycon-
cardinalityofthedatasetexceedstheavailablescreenpixels, straintsfromupperlevels:oncetheviewporthasbeenconstricted

Proteus:ShapeshiftingDesktopVisualizationsforMobileviaMulti-levelIntelligentAdaptation DIS’26,June13–17,2026,Singapore
andtheaxisrangefixed,marksizesmustbechosensothattheyre- ### Source Code
|     |     |     |     |     |     |     |     | Below is | the source | code | of the | original | SVG | or  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ---- | ------ | -------- | --- | --- |
mainbothperceptibleandtouchablewithintheavailablepixels.In
|     |     |     |     |     |     |     |     | HTML | file: | {source_code} |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----- | ------------- | --- | --- | --- | --- |
otherwords,fine-grainedchangestomarksandtextarenotarbi-
|     |     |     |     |     |     |     |     | ### Visual | Renderings |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | --- | --- | --- | --- |
trarytweaks,butmustrespectthelayoutandreference-framedeci-
|     |     |     |     |     |     |     |     | The first | image | is `desktop.png`. |     | The | second | image |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----- | ----------------- | --- | --- | ------ | ----- |
sionsalreadyinplace.Theseinter-leveldynamicshelpexplainwhy
is `desktop_on_mobile.png`.
simplerule-basedheuristicsthattreatoperationsindependentlyof- [IMAGE_PLACEHOLDER: desktop.png (tailored for
desktop)]
tenfailonmobile:improvingoneaspect(forexample,densityvia
|                 |     |         |              |              |     |            |     | [IMAGE_PLACEHOLDER: |     | desktop_on_mobile.png |        |         |     |     |
| --------------- | --- | ------- | ------------ | ------------ | --- | ---------- | --- | ------------------- | --- | --------------------- | ------ | ------- | --- | --- |
| tick reduction) |     | without | coordinating | compensating |     | mechanisms |     |                     |     |                       |        |         |     |     |
|                 |     |         |              |              |     |            |     | (rendered           |     | in mobile             | aspect | ratio)] |     |     |
(suchastooltips,scrolling,orcontextcollapsing)caneasilybreak
|     |     |     |     |     |     |     |     | ## Task | and Requirements |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------------- | --- | --- | --- | --- | --- |
readabilityorfidelity.
|           |     |     |     |     |     |     |     | 1. **Multimodal |        | Analysis       | & Correlation**: |              | Analyze |      |
| --------- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------ | -------------- | ---------------- | ------------ | ------- | ---- |
|           |     |     |     |     |     |     |     | the             | source | code alongside |                  | the provided |         |      |
| 4 Proteus |     |     |     |     |     |     |     | images.         | Bridge | the            | code-level       | semantics    |         | with |
|           |     |     |     |     |     |     |     | pixel-level     |        | spatial        | relationships.   |              |         |      |
GuidedbytheMulti-levelDesignSpacedefinedinsection3,we
|     |     |     |     |     |     |     |     | 2. **Visualization |     | Deconstruction**: |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ----------------- | --- | --- | --- | --- |
developed Proteus, a Large Language Model (LLM) driven multi- - Identify the global chart topology (e.g.,
agent system. Proteus automates the transformation of visualiza- Grouped Bar Chart, Line Chart, Scatter Plot,
etc.).
tions,movingfromadesktopvisualizationorsourcecodetoafully
|     |     |     |     |     |     |     |     | - Segment | and | list | all logical | components |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---- | ----------- | ---------- | --- | --- |
responsivemobilecomponent.
|     |     |     |     |     |     |     |     | (axes, | legends, | marks, | titles, |     | annotations, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ------ | ------- | --- | ------------ | --- |
|     |     |     |     |     |     |     |     | grid   | lines).  |        |         |     |              |     |
4.1 AgentRolesandResponsibilities
|     |     |     |     |     |     |     |     | 3. **Mobile | Rendering | Analysis**: |     | Analyze | the |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | ----------- | --- | ------- | --- | --- |
Toreplicatetheworkflowofahumanvisualizationexpert,Proteus `desktop_on_mobile.png` image. Explicitly
|     |     |     |     |     |     |     |     | document | the | visual | issues | and | constraints |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------ | ------ | --- | ----------- | --- |
isarchitectedasacollaborativeteamoffivespecializedagents(as when this desktop layout is forced into a
illustratedinFigure2):theSemanticParser,theDataExtractor,the mobile aspect ratio (e.g., overlapping text,
DesignPlanner,theFrontendEngineer,andtheVisualCritic.These squished marks, hidden elements).
agentsoperatewithinaclosed-loopiterativeenvironment,ensur- 4. **Codify Data (Crucial)**: Extract and
ingthatthefinaloutputnotonlycompilesbutalsostrictlyadheres structure the **real data** from the source
|     |     |     |     |     |     |     |     | SVG | (coordinates, |     | colors, | labels, | raw | data |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | ------- | --- | ---- |
tomobilereadabilityconstraints.
|     |     |     |     |     |     |     |     | values) | or  | HTML files. | **No | fake | data |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ----------- | ---- | ---- | ---- | --- |
• Semanticparseragent.Thepipelineinitiateswiththese- allowed.** Map the visual properties back to
manticparser.Uponingestingthedesktopsourcecode(HTM- the underlying data points.
|     |     |     |     |     |     |     |     | ## Output | Format |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ | --- | --- | --- | --- | --- |
L/SVG),thisagentfirstorchestratesarenderingprocessto
|     |           |               |        |          |       |              |     | Write your | output | in Markdown |     | format. | It must |     |
| --- | --------- | ------------- | ------ | -------- | ----- | ------------ | --- | ---------- | ------ | ----------- | --- | ------- | ------- | --- |
|     | capture a | high-fidelity | raster | snapshot | (PNG) | of the visu- |     | include:   |        |             |     |         |         |     |
alization.Crucially,itexecutesamultimodalanalysis,cor- 1. **Topology & Component Segmentation**: A
relatingtheexplicitvectorstructure (DOM/SVGhierarchy) detailed breakdown of the chart type and its
withtheperceptualbitmaplayout.Bybridgingcode-level logical components.
|     |     |     |     |     |     |     |     | 2. **Mobile | Constraints |     | Analysis**: |     | Identified |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | --- | ----------- | --- | ---------- | --- |
semanticswithpixel-levelspatialrelationships,itsprimary
|     |     |     |     |     |     |     |     | issues | in  | the mobile | aspect | ratio | render. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | ---------- | ------ | ----- | ------- | --- |
objectiveistoperformrobustVisualizationDeconstruction, 3. **Extracted Data**: A cleanly structured JSON
identifyingtheglobalcharttopology(e.g.,GroupedBarChart) or tabular format of the exact data extracted
andsegmentinglogicalcomponents(axes,legends,marks) from the code, ready to be used by the
beforepassingcontroltotheextractionlayer. downstream planner and engineering agents.
|     | You need                  | to act | as a **Semantic |                | Parser | Agent** in |     |                 |     |        |           |     |            |         |
| --- | ------------------------- | ------ | --------------- | -------------- | ------ | ---------- | --- | --------------- | --- | ------ | --------- | --- | ---------- | ------- |
|     |                           |        |                 |                |        |            | •   | Data extraction |     | agent. | Employing | a   | customized | reverse |
|     | a visualization-to-mobile |        |                 | transformation |        |            |     |                 |     |        |           |     |            |         |
engineeringapproach,thisagentutilizestheparsedvector
pipeline.
structuretorecovertheunderlyingdatasetandvisualspeci-
fications(e.g.,scaledomains,colormappings,andaxisranges).
|     | Your primary | objective | is  | to execute | a   | multimodal |     |     |     |     |     |     |     |     |
| --- | ------------ | --------- | --- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Unlikegenerictoolsorsimplepixel-basedresizing,itexe-
|     | analysis, | correlating |            | the explicit |      | vector |     |     |     |     |     |     |     |     |
| --- | --------- | ----------- | ---------- | ------------ | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
|     | structure | (DOM/SVG    | hierarchy) |              | with | the    |     |     |     |     |     |     |     |     |
cutescase-specificlogictoextractprecisegeometricattributes
|     | perceptual |     | bitmap layout. | You | will | perform |     |     |     |     |     |     |     |     |
| --- | ---------- | --- | -------------- | --- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
(e.g.,height,position,andcolor)fromthesourcecode.By
|     | robust  | Visualization |       | Deconstruction |     | and |     |             |       |             |      |                  |     |      |
| --- | ------- | ------------- | ----- | -------------- | --- | --- | --- | ----------- | ----- | ----------- | ---- | ---------------- | --- | ---- |
|     |         |               |       |                |     |     |     | integrating | these | visual cues | with | metadata-derived |     | map- |
|     | extract | real          | data. |                |     |     |     |             |       |             |      |                  |     |      |
pingrules,orbydirectlyparsingexplicittextlabelswhere
|     | ## Project | Structure | & Context |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---------- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
dataisvisible,theagentcomputestheexactnumericalcon-
- `original_visualization`:
|     | - `desktop.{{html, |        | svg}}`:       | the      | original | source |     |            |               |     |         |              |     |               |
| --- | ------------------ | ------ | ------------- | -------- | -------- | ------ | --- | ---------- | ------------- | --- | ------- | ------------ | --- | ------------- |
|     |                    |        |               |          |          |        |     | tent. This | reconstructed |     | data is | consolidated |     | into a struc- |
|     | code               | of the | visualization | tailored |          | for    |     |            |               |     |         |              |     |               |
turedJSONformat,ensuringthatsemanticfidelityisstrictly
desktop.
preservedduringthemigrationfromthedesktopsourceto
|     | - `desktop.png`: |     | the | rendered | original |     |     |     |     |     |     |     |     |     |
| --- | ---------------- | --- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
themobileimplementation.
|     | visualization              |     | tailored | for      | desktop. |          |     |     |     |     |     |     |     |     |
| --- | -------------------------- | --- | -------- | -------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | - `desktop_on_mobile.png`: |     |          | the      | original |          |     |     |     |     |     |     |     |     |
|     | visualization              |     | directly | rendered | in       | a mobile |     |     |     |     |     |     |     |     |
aspect ratio. You are a highly specialized Data Extraction Agent.

| DIS’26,June13–17,2026,Singapore |     |     |     |     |     |     |     |     |     | Trovatoetal. |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ |
Figure2:Themulti-agentframeworkofProteusfordesktop-to-mobilevisualizationadaptation.
Your task is to recover the underlying dataset and plan.Theagentadoptsahierarchicaldecision-makingpro-
visualization specifications from given cess:itfirstevaluatesthedisparitybetweendesktopandmo-
source code (e.g., SVG, Canvas, or bileformfactorstodeterminethenecessityofglobaltopol-
|     | chart-rendering | scripts), | and output | the |     |     |     |     |     |     |
| --- | --------------- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
ogychanges,suchasaxistranspositionorlayoutserializa-
|     | extracted | data in a structured | JSON | format. |     |     |     |     |     |     |
| --- | --------- | -------------------- | ---- | ------- | --- | --- | --- | --- | --- | --- |
### Capabilities tion.Oncethestructuralfoundationisset,itdecidesonad-
- You may write and execute Python or JavaScript justmentstothereferenceframe,includingmodificationsto
code to assist with parsing and extraction. axesandlegends,aswellastheintegrationofcomplemen-
- You are allowed to perform reverse engineering tary interactions. Finally, it specifies granular adaptations
|     | on the | source code to | recover data. |     |     |     |     |     |     |     |
| --- | ------ | -------------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
attheelementlevel.Thisprocessculminatesinahigh-level
### Instructions
1. Reverse Engineering blueprintthatexplicitlyinstructstheengineeringagenton
- Analyze the provided source code and parsed handlingspecificchallenges,suchasconvertinglegendsto
vector structure. inlinelabelsortransformingthex-axisintoascrollablecon-
- Identify visual elements such as shapes, tainer,effectivelymappingabstractconstraintstoconcrete
|     | paths, | bars, lines, and | text. |     |     |     |     |     |     |     |
| --- | ------ | ---------------- | ----- | --- | --- | --- | --- | --- | --- | --- |
implementationsteps.
|     | 2. Extract Visual | Specifications    |             |     |     |     |     |     |     |     |
| --- | ----------------- | ----------------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
|     | - Recover         | key visualization | parameters, |     |     |     |     |     |     |     |
including:
|     |              |                      |     |     | You need        | to act | as a **Design | Planner         | Agent**  | to      |
| --- | ------------ | -------------------- | --- | --- | --------------- | ------ | ------------- | --------------- | -------- | ------- |
|     | - Scale      | domains              |     |     | architect       | how    | to transform  |                 | a static | desktop |
|     | - Axis       | ranges               |     |     | visualization   |        | into          | an interactive, |          |         |
|     | - Color      | mappings             |     |     | mobile-friendly |        | component.    |                 |          |         |
|     | - Coordinate | systems              |     |     |                 |        |               |                 |          |         |
|     | 3. Geometric | Attribute Extraction |     |     |                 |        |               |                 |          |         |
## Global Objectives
|     | - Extract | precise geometric | attributes | such as: |                   |     |       |                            |     |     |
| --- | --------- | ----------------- | ---------- | -------- | ----------------- | --- | ----- | -------------------------- | --- | --- |
|     |           |                   |            |          | 1. **Mobile-First |     | UX**: | Ensure touch-friendliness, |     |     |
- Position (x, y) readable typography, and responsive layouts.
- Size (width, height, radius) 2. **Premium Aesthetics**: Use modern UI
|     | - Color  | values              |                |     | principles       |             | (glassmorphism, |           | vibrant palettes, |         |
| --- | -------- | ------------------- | -------------- | --- | ---------------- | ----------- | --------------- | --------- | ----------------- | ------- |
|     | - Do NOT | rely on pixel-level | heuristics;    |     |                  |             |                 |           |                   |         |
|     |          |                     |                |     | smooth           | animations) |                 | to create | a "wow"           | factor. |
|     | instead, | use structural      | and code-level |     |                  |             |                 |           |                   |         |
|     |          |                     |                |     | 3. **Information |             | Preservation**: |           | Preserve          | as much |
information.
|     |                        |                 |                |             | information      |              | and intention | presented    |     | in the |
| --- | ---------------------- | --------------- | -------------- | ----------- | ---------------- | ------------ | ------------- | ------------ | --- | ------ |
|     | 4. Data Reconstruction |                 |                |             | desktop          | version      | as            | possible.    |     |        |
|     | - Map geometric        | attributes      | back to        | data values |                  |              |               |              |     |        |
|     | using:                 |                 |                |             | ## Tech          | Stack Target |               |              |     |        |
|     | - Scale                | transformations |                |             |                  |              |               |              |     |        |
|     |                        |                 |                |             | - Framework:     | Next.js      | 14            | (App Router) |     |        |
|     | - Axis                 | mappings        |                |             |                  |              |               |              |     |        |
|     |                        |                 |                |             | - Styling:       | TailwindCSS  |               |              |     |        |
|     | - Metadata-derived     | rules           | (if available) |             |                  |              |               |              |     |        |
|     |                        |                 |                |             | - Visualization: |              | Recharts      |              |     |        |
|     | - If explicit          | text labels     | are present,   | directly    | - Icons:         | Lucide       | React         |              |     |        |
|     | parse and              | use them.       |                |             |                  |              |               |              |     |        |
## Inputs
|     |     |     |     |     | ### 1. Semantic |                   | Parser Output |               |           |        |
| --- | --- | --- | --- | --- | --------------- | ----------------- | ------------- | ------------- | --------- | ------ |
|     |     |     |     |     | Below is        | the deconstructed |               | chart         | topology, | mobile |
|     |     |     |     |     | constraint      |                   | analysis,     | and extracted | data      |        |
|     |     |     |     |     | provided        | by                | the Semantic  | Parser        | Agent:    |        |
{semantic_parser_output}
|     |     |     |     |     | ### 2. Vis2Mobile |              | Design    | Action | Space      |       |
| --- | --- | --- | --- | --- | ----------------- | ------------ | --------- | ------ | ---------- | ----- |
| •   |     |     |     |     | Below is          | the document | detailing |        | the design | space |
Designplanneragent.Armedwiththeextracteddataand
|     |     |     |     |     | of  | visualizations | and | the action | space | for |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ---------- | ----- | --- |
originalvisualizationstructure,theDesignPlanneractsas
|     |     |     |     |     | mobile | transformation: |     |     |     |     |
| --- | --- | --- | --- | --- | ------ | --------------- | --- | --- | --- | --- |
thesystem’sarchitect.Itreferencesthedesignspace(Sec- {vis2mobile_design_action_space}
tion3)togenerateacomprehensivetransformationaction ### 3. Visual References (Context)

Proteus:ShapeshiftingDesktopVisualizationsforMobileviaMulti-levelIntelligentAdaptation DIS’26,June13–17,2026,Singapore
[IMAGE_PLACEHOLDER: desktop.png (tailored for agent to precisely map the design planner’s abstract con-
desktop)]
straintsintoaconcrete,executablemobileimplementation.
| [IMAGE_PLACEHOLDER: |                  | desktop_on_mobile.png |        |          |        |     |     |     |     |     |     |
| ------------------- | ---------------- | --------------------- | ------ | -------- | ------ | --- | --- | --- | --- | --- | --- |
| (rendered           |                  | in mobile             | aspect | ratio)]  |        |     |     |     |     |     |     |
| ## Task             | and Requirements |                       |        |          |        |     |     |     |     |     |     |
| Armed with          | the              | extracted             | data,  | original | visual |     |     |     |     |     |     |
intent, and the Design Action Space, you must You should implement the mobile version of the
|                    |                |                      |                 |                |              | visualization                          |              | in the            |              |            |              |
| ------------------ | -------------- | -------------------- | --------------- | -------------- | ------------ | -------------------------------------- | ------------ | ----------------- | ------------ | ---------- | ------------ |
| generate           | a              | comprehensive        |                 | transformation |              |                                        |              |                   |              |            |              |
|                    |                |                      |                 |                |              | `src/components/Visualization.tsx`     |              |                   |              |            | file.        |
| action             | plan.          |                      |                 |                |              |                                        |              |                   |              |            |              |
| Adopt a            | **hierarchical |                      | decision-making |                | process**    |                                        |              |                   |              |            |              |
|                    |                |                      |                 |                |              | ## Tech                                | Stack Target |                   |              |            |              |
| in                 | your plan:     |                      |                 |                |              |                                        |              |                   |              |            |              |
|                    |                |                      |                 |                |              | - Framework:                           | Next.js      | 14                | (App Router) |            |              |
| 1. **Global        | Topology       | Adjustments**:       |                 |                | Evaluate the |                                        |              |                   |              |            |              |
| disparity          |                | between              | desktop         | and mobile     | form         | - Styling:                             | TailwindCSS  |                   |              |            |              |
|                    |                |                      |                 |                |              | - Visualization:                       |              | Recharts          |              |            |              |
| factors            | (referencing   |                      | the             | Semantic       | Parser's     |                                        |              |                   |              |            |              |
|                    |                |                      |                 |                |              | - Icons:                               | Lucide       | React             |              |            |              |
| constraint         |                | analysis).           | Determine       |                | if global    |                                        |              |                   |              |            |              |
| topology           | changes        |                      | are needed      | (e.g.,         | axis         |                                        |              |                   |              |            |              |
|                    |                |                      |                 |                |              | Carefully                              | read         | the following     | files        | for        |              |
| transposition,     |                | layout               | serialization,  |                | changing     |                                        |              |                   |              |            |              |
|                    |                |                      |                 |                |              | instructions                           |              | and more          | information: |            |              |
| chart              | types).        |                      |                 |                |              |                                        |              |                   |              |            |              |
| 2. **Reference     |                | Frame Adjustments**: |                 |                | Decide on    |                                        |              |                   |              |            |              |
|                    |                |                      |                 |                |              | - `transform-plan.md`:                 |              | the               | detailed     | plan       | for          |
| modifications      |                | to                   | axes and        | legends        | (e.g.,       |                                        |              |                   |              |            |              |
|                    |                |                      |                 |                |              | transforming                           |              | the visualization |              | to         | a mobile     |
| converting         |                | legends              | to inline       | labels,        | making       |                                        |              |                   |              |            |              |
|                    |                |                      |                 |                |              | version.                               | YOU          | SHOULD            | FOLLOW       | THIS PLAN. |              |
| the                | x-axis         | a scrollable         |                 | container).    | Plan the     |                                        |              |                   |              |            |              |
|                    |                |                      |                 |                |              | - `mobile-vis-design-action-space.md`: |              |                   |              |            | high-level   |
| integration        |                | of complementary     |                 | mobile         |              |                                        |              |                   |              |            |              |
|                    |                |                      |                 |                |              | description                            |              | of the            | space for    | the        | actions that |
| interactions       |                | (e.g.,               | touch           | tooltips,      | swipe        |                                        |              |                   |              |            |              |
| gestures).         |                |                      |                 |                |              | an                                     | agent can    | take to           | transform    | the        |              |
|                    |                |                      |                 |                |              | visualization                          |              | to a              | mobile       | version    |              |
| 3. **Element-Level |                | Adaptations**:       |                 | Specify        | granular     |                                        |              |                   |              |            |              |
- `original_visualization`:
| adaptations  |             | such | as mark       | sizing, | typography     |                         |                   |     |              |             |             |
| ------------ | ----------- | ---- | ------------- | ------- | -------------- | ----------------------- | ----------------- | --- | ------------ | ----------- | ----------- |
|              |             |      |               |         |                | - `desktop.{html|svg}`: |                   |     | the original |             | source code |
| adjustments, |             | and  | color palette |         | alignment with |                         |                   |     |              |             |             |
|              |             |      |               |         |                | of                      | the visualization |     | that         | is tailored | for         |
| premium      | aesthetics. |      |               |         |                |                         |                   |     |              |             |             |
desktop.
| ## Output   | Constraints |     |         |           |          | - `desktop.png`:           |     | the rendered |             | original |          |
| ----------- | ----------- | --- | ------- | --------- | -------- | -------------------------- | --- | ------------ | ----------- | -------- | -------- |
|             |             |     |         |           |          | visualization              |     | that         | is tailored | for      | desktop. |
| - Just give | a plan,     | no  | need to | implement | the code |                            |     |              |             |          |          |
|             |             |     |         |           |          | - `desktop_on_mobile.png`: |     |              | the         | original |          |
yet.
|            |            |            |            |         |             | visualization                         |        | that   | is directly | rendered | in       |
| ---------- | ---------- | ---------- | ---------- | ------- | ----------- | ------------------------------------- | ------ | ------ | ----------- | -------- | -------- |
| - You must | explicitly |            | list **the | actions | to take     |                                       |        |        |             |          |          |
|            |            |            |            |         |             | mobile                                | aspect | ratio. |             |          |          |
| that       | are in     | the Action | Space      | and     | justify why |                                       |        |        |             |          |          |
|            |            |            |            |         |             | - `src/components/Visualization.tsx`: |        |        |             |          | The main |
| you        | chose      | them**.    |            |         |             |                                       |        |        |             |          |          |
- If an action is not in the action space, state component that renders the transformed mobile
visualization.
| the | reason | and justify | why | existing | actions |     |     |     |     |     |     |
| --- | ------ | ----------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- |
are unsuitable.
| - If some | information |     | must be   | omitted      | or moved to |     |     |     |     |     |     |
| --------- | ----------- | --- | --------- | ------------ | ----------- | --- | --- | --- | --- | --- | --- |
| another   | view        | due | to mobile | constraints, |             |     |     |     |     |     |     |
• VisualCriticAgent.Ourframeworkincludesavisualcritic
| mention | it  | and write | your | justification. |     |     |     |     |     |     |     |
| ------- | --- | --------- | ---- | -------------- | --- | --- | --- | --- | --- | --- | --- |
- **Structure your response**: Start with a agent,whichperformsacomprehensivemulti-dimensional
High-Level Strategy, followed by Detailed evaluation.Oncethecodeisgenerated,thesystemrenders
Implementational Steps mapping abstract thecomponentandcapturesascreenshot(mimickingareal
| constraints |     | to concrete |     | engineering |     |     |     |     |     |     |     |
| ----------- | --- | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
mobiledeviceviewport).Utilizingvision-capableLLMs,the
instructions.
visualcriticagentassessesthevisualizationagainstfourcrit-
| - Write | your plan | in pure | Markdown | format. |     |     |     |     |     |     |     |
| ------- | --------- | ------- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
icalcriteria:
– DataFidelity.Verifyingthattherenderedvisualelements
|     |     |     |     |     |     | accurately | reflect | the extracted |     | numerical | data without |
| --- | --- | --- | --- | --- | --- | ---------- | ------- | ------------- | --- | --------- | ------------ |
• Frontend engineering agent. To translate the extracted distortionorloss.
dataandtheDesignPlanner’sstrategicschemeintoafunc- – PlanAdherence.Ensuringtheimplementationstrictly
tionalapplication,theFrontendEngineeringagentoperates followsthetopologicalandstructuraldirectivesissuedby
withinaspecifiedmobilesoftwareframework.Workingin theDesignPlanner.
aweb-basedenvironment(HTML,JavaScript,andCSS),the – TextReadability.Detectinglegibilitydegradationcaused
agentisprovidedwithapre-defined,emptymobileapplica- byspatialcompression.Ashighlightedinpriorresearch[53],
tionscaffoldandtaskedwithauthoringTypeScript[33]files maintainingtextreadabilityisoftenthemostsignificant
toimplementspecificvisualizationcomponentsandinterac- challenge when migrating visualizations to constrained
tionlogic.ThechoiceofTypeScriptisdeliberate;bymerging mobileenvironments.Theagentrigorouslyscansforsymp-
TypeScript’s robusttypesystem withJavaScript’sdeclara- tomsofpooradaptation,suchasaggressivefontdownsiz-
tive syntax [11], it enables the unified expression of data ingthatrenderstextindecipherable,labelocclusiondue
structures,interactionlogic,andinterfacelayoutswithina to horizontal crowding, or insufficient contrast against
singlecomponent.Thiscohesiveformatnotonlyenhances complex backgrounds, ensuring textual information re-
codereadabilityandmaintainabilitybutalsoempowersthe mainsaccessibledespitethereducedscreenrealestate.

| DIS’26,June13–17,2026,Singapore |     |     |     |     |     |     |     |     |     |     |     | Trovatoetal. |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |
– Aesthetics.Evaluatingtheoverallvisualappealbybal- sequenceofintermediateartifactsthatcanbeinspected,revised,
| ancingstylisticfidelitytothedesktopsourcewithmobile- |     |     |     |     |     | andvalidated. |     |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
native harmony. The agent assesses whether the adap- Inputs and runtime. The pipeline accepts desktop visualiza-
tation preserves the original visual identity (e.g., color tionassets,includingHTML/SVGsourcecodeandthecorrespond-
themes and stylistic tone) while ensuring the layout re- ingrenderedrastersnapshots.Allstepsruninasandboxedenvi-
mains spatially coherent, well-spaced, and aesthetically ronmentwithafixedprojectscaffoldandbuildtools,enablingthe
pleasingwithinthecompactmobileviewport. agentstoexecutecode,rendertheresultunderamobileviewport,
| Upondetectingdeficiencies,theagentdynamicallyroutes |     |     |     |     |     | anditeratesafely. |     |     |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
feedbackbasedontheseverityoftheissue.Implementation- Stage 1: Deconstruct and recover. Given the desktop input
level defects (e.g., styling inconsistencies or minor layout (Figure2a),theSemanticParserfirstrendersthevisualizationand
shifts)areaddressedtothefrontendengineeringagentfor alignstheDOM/SVGstructurewiththerenderedlayouttoidentify
immediatecoderefinement,whereasfundamentalstructural thecharttopologyanditscomponents(e.g.,axes,legends,marks,
flawsorstrategymismatchestriggeraregressiontothede- annotations) (Figure 2 c and d). Next, the Data Extractor recon-
signplanneragentforarchitecturalrevision. structs the underlying dataset and key visual specifications (e.g.,
scaledomainsandmappings)fromthesourcestructure(Figure2
b)andlabels(Figure2c),andoutputsastructuredJSONrepresen-
| You are a Visual | Critic | Agent | for | mobile visualization. |     |     |     |     |     |     |     |     |     |
| ---------------- | ------ | ----- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tationofdata(Figure2e).
| Your task | is  | to evaluate | the | quality | of a rendered |     |     |     |     |     |     |     |     |
| --------- | --- | ----------- | --- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
mobile visualization and provide actionable feedback. Stage2:Planthemobiletransformation.TheDesignPlan-
### Instructions nertakestherecovereddata/specs(Figure2f)andproducesanex-
| 1. Rendering | Inspection |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
plicittransformationplan(Figure2h).Guidedbythemulti-level
| - Run `uv | run python | screenshot.py` |     | to  | capture the |     |     |     |     |     |     |     |     |
| --------- | ---------- | -------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
designspace(Section3),theplanspecifies(i)view-levelreorgani-
| mobile | visualization |     | as `mobile-version.png`. |     |     |     |     |     |     |     |     |     |     |
| ------ | ------------- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
zation(e.g.,serializationofmultipleviews,axistransposition),(ii)
| - Inspect | the screenshot |     | to detect | rendering | issues or |     |     |     |     |     |     |     |     |
| --------- | -------------- | --- | --------- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
runtime errors. reference-frame and component changes (e.g., legend restructur-
- Optionally, use Playwright to interact with and ing,externalizingannotations/controls),and(iii)element-levelad-
| verify | the rendered |     | result. |     |     |     |     |     |     |     |     |     |     |
| ------ | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
justments(e.g.,labeldensity,marksizing),togetherwithconcrete
| 2. Evaluation | Criteria |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
implementationdirectives.
| Evaluate | the visualization |     | along | the following |     |       |              |     |             |     |          |          |     |
| -------- | ----------------- | --- | ----- | ------------- | --- | ----- | ------------ | --- | ----------- | --- | -------- | -------- | --- |
|          |                   |     |       |               |     | Stage | 3: Implement |     | and verify. | The | frontend | engineer | im- |
dimensions:
(a) Data Fidelity: Check whether visual elements plementstheplanwithintheprovidedmobilescaffoldwrittenin
accurately reflect the underlying data. Ensure no TypeScript,producinganexecutablecomponent(Figure2i).The
| distortion, | mismatch, |     | or missing | data. |     |     |     |     |     |     |     |     |     |
| ----------- | --------- | --- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
systemthenrendersthiscomponentandcapturesscreenshotsun-
| (b) Plan | Adherence: | Verify | that | the implementation |     |     |     |     |     |     |     |     |     |
| -------- | ---------- | ------ | ---- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
deraphone-sizedviewport.Thevisualcriticagentevaluatesthe
| follows | the design | plan | (layout, | structure, | chart |     |     |     |     |     |     |     |     |
| ------- | ---------- | ---- | -------- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
output(Figure2j)againstmobile-firstcriteria,includingdatafi-
type).
(c) Text Readability: Detect issues such as: Font delity,planadherence,textreadability,andoverallvisualquality,
sizes too small; Overlapping or occluded labels; and returns targeted feedback (Figure 2 k and l). Based on this
| Poor contrast; |     | Ensure | text | remains legible | in a |     |     |     |     |     |     |     |     |
| -------------- | --- | ------ | ---- | --------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
critique,theworkflowloops:code-levelissuesareroutedbackto
| mobile | viewport. |     |     |     |     |     |     |     |     |     |     |     |     |
| ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theEngineer,whilestrategy-levelmismatchestriggerreplanning.
| (d) Aesthetics: |     | Evaluate | visual | quality, | including: |     |     |     |     |     |     |     |     |
| --------------- | --- | -------- | ------ | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
TheiterationterminatesonlywhentheCriticcertifiestheresultas
| Layout | balance | and spacing, |     | consistency | with |     |     |     |     |     |     |     |     |
| ------ | ------- | ------------ | --- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
mobile-ready.
| original                | style        | (e.g., | colors), | and verall        | visual |                                      |                |             |               |     |     |        |     |
| ----------------------- | ------------ | ------ | -------- | ----------------- | ------ | ------------------------------------ | -------------- | ----------- | ------------- | --- | --- | ------ | --- |
| clarity                 | and harmony. |        |          |                   |        | Hereisanexampletransformplanexample: |                |             |               |     |     |        |     |
| 3. Issue Classification |              | &      | Routing  |                   |        |                                      |                |             |               |     |     |        |     |
|                         |              |        |          |                   |        | # Vis2Mobile                         | Transformation |             | Plan          |     |     |        |     |
| - If issues             | are          | minor  | (e.g.,   | styling, spacing, | small  |                                      |                |             |               |     |     |        |     |
|                         |              |        |          |                   |        | ## 1. Analysis                       |                | of Original | Visualization |     | &   | Mobile |     |
| layout                  | shifts):     |        |          |                   |        |                                      |                |             |               |     |     |        |     |
Challenges
| → Provide   | fixes | for        | the frontend | engineering | agent.      |            |      |             |               |     |           |     |     |
| ----------- | ----- | ---------- | ------------ | ----------- | ----------- | ---------- | ---- | ----------- | ------------- | --- | --------- | --- | --- |
|             |       |            |              |             |             | ### Visual | Spec | of Original | Visualization |     | (Desktop) |     |     |
| - If issues | are   | structural | (e.g.,       | wrong       | chart type, |            |      |             |               |     |           |     |     |
poor layout strategy): - **Type**: Scatter Plot with Overlayed Confidence
→ Escalate to the design planner for revision. Ellipses (Density Estimation).
|     |     |     |     |     |     | - **Data**: | "Penguins" |     | dataset. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | -------- | --- | --- | --- | --- |
4. Output
|                       |            |            |              |              |         | - **X-Axis**:      |             | Flipper     | Length    | (mm).       |                  |         |     |
| --------------------- | ---------- | ---------- | ------------ | ------------ | ------- | ------------------ | ----------- | ----------- | --------- | ----------- | ---------------- | ------- | --- |
| - List detected       |            | issues     | grouped      | by category. |         |                    |             |             |           |             |                  |         |     |
|                       |            |            |              |              |         | - **Y-Axis**:      |             | Body        | Mass (g). |             |                  |         |     |
| - Provide             | clear,     | actionable | suggestions. |              |         |                    |             |             |           |             |                  |         |     |
|                       |            |            |              |              |         | - **Color/Group**: |             |             | Species   | (Adelie,    | Chinstrap,       |         |     |
| - Indicate            | routing    | decision:  |              | [Frontend    | Fix] or |                    |             |             |           |             |                  |         |     |
| [Planner              | Revision]. |            |              |              |         | Gentoo).           |             |             |           |             |                  |         |     |
|                       |            |            |              |              |         | - **Narrative**:   |             | Comparing   | the       | correlation |                  | between |     |
|                       |            |            |              |              |         | flipper            | length      | and         | body      | mass across | three            | penguin |     |
|                       |            |            |              |              |         | species.           | The         | ellipses    | highlight |             | the distribution |         |     |
| 4.2 WorkflowExecution |            |            |              |              |         | range              | and         | correlation | strength. |             |                  |         |     |
|                       |            |            |              |              |         | - **Visual         | Encoding**: |             |           |             |                  |         |     |
Proteus executesvisualizationadaptationasaniterative,artifact-
|                 |         |     |        |               |                | - **Points**: |     | Individual    |     | data entries     | (Scatter). |        |     |
| --------------- | ------- | --- | ------ | ------------- | -------------- | ------------- | --- | ------------- | --- | ---------------- | ---------- | ------ | --- |
| driven workflow | (Figure | 2). | Rather | than treating | mobile adapta- |               |     |               |     |                  |            |        |     |
|                 |         |     |        |               |                | - **Polygons  |     | (Ellipses)**: |     | Semi-transparent |            | filled |     |
tionasaone-shot“resize”problem,thesystemprogressivelytrans- shapes representing statistical deviation.
latesadesktopvisualizationintoamobilecomponentthrougha - **Legend**: Located on the right side.

Proteus:ShapeshiftingDesktopVisualizationsforMobileviaMulti-levelIntelligentAdaptation DIS’26,June13–17,2026,Singapore
### Mobile Challenges (Desktop-on-Mobile Analysis) * *Plan*: Use the `Customized` component or SVG
1. **Aspect Ratio Distortion**: The wide aspect ratio `path` overlays within the Recharts container to
(approx 2:1) of the desktop version, when compressed render the ellipse data using the extracted
to mobile width, makes the chart extremely short. coordinates. This ensures the "Confidence/Deviation"
This squashes the Y-axis range, making vertical narrative is preserved.
separation between points difficult to distinguish. ### L5: Interaction & Feedback
2. **Legend Space**: The right-aligned legend consumes * **Action: Reposition (Fix Tooltip Position)**
approximately 20-25% of the horizontal screen real * *Reason*: Standard tooltips follow the cursor. On
estate. On mobile, this leaves very little room for mobile, the finger obscures the tooltip.
the actual data. * *Plan*: Implement a **"Selected State"**. When a
3. **Touch Targets**: The scatter points are relatively user taps a dot, display the specific data details
small. Hover interactions (standard on desktop) do (Sex, Island, exact mass) in a fixed card at the
not exist on mobile. bottom of the visualization or in a dedicated
4. **Label Readability**: Axis labels and titles may "Active Data" header space.
become too small to read if simply scaled down. * **Action: Disable Hover / Enable Tap**
5. **Data Density**: The ellipses overlap significantly. * *Reason*: Touch interface.
On a small screen, the transparency blending might ### Premium Aesthetics (UI Layer)
become muddy without proper color handling. * **Theme**: Glassmorphism.
* Background: Semi-transparent blurred cards for
## 2. Vis2Mobile Design Action Plan the legend and tooltip area.
* Colors: Vivid, accessible palette for the three
Based on the **Vis2Mobile Design Action Space**, I plan species (Blue, Orange, Red) ensuring high contrast
to apply the following actions to transform this against the background.
visualization. * Animation: Smooth transitions when filtering
### L0: Visualization Container species.
* **Action: Rescale (Aspect Ratio Adjustment)** ## 3. Data Extraction Strategy
* *Reason*: The original "wide" format fails on I will extract the data directly from the HTML source
vertical mobile screens. `spec` variable.
* *Plan*: Change the container aspect ratio to a 1. **Ellipse Data**: Located in
taller format (e.g., 1:1 square or 4:5 portrait). `spec.datasets["data-cb82d8ff5c0..."]`.
This utilizes the vertical scroll behavior of mobile * *Fields*: `order`, `Flipper Length (mm)`, `Body
usage and decompresses the Y-axis data. Mass (g)`, `Species`.
### L3: Legend Block * *Usage*: This will be converted into three
* **Action: Reposition & Transpose** separate arrays (one per species) to draw the SVG
* *Reasoning*: The side legend creates a "Distorted paths.
layout" on mobile. 2. **Scatter Data**: Located in
* *Plan*: Move the legend to the **top** of the `spec.datasets["data-300f0a3d0..."]`.
chart (below the main title). Transpose it from a * *Fields*: `Species`, `Island`, `Beak Length
vertical list to a horizontal row of "Chips" or (mm)`, `Beak Depth (mm)`, `Flipper Length (mm)`,
"Badges". `Body Mass (g)`, `Sex`.
* **Action: Interaction (Filter)** * *Usage*: Main data source for the scatter plot.
* *Plan*: Make the legend chips interactive. **Note on Data Processing**: The raw ellipse data is a
Tapping a species (e.g., "Adelie") acts as a filter set of points. To render this in Recharts/SVG, I
or focus mechanism, dimming the other species to will need to sort them by `order` and construct an
reduce "Overplotting" on the small screen. SVG path string (`M x1 y1 L x2 y2 ... Z`) for each
### L3/L4: Coordinate System (Axes) species.
* **Action: Decimate Ticks (Adjust Ticks)** ## 4. Implementation Plan (Step-by-Step)
* *Reason*: High density of tick labels on the ### Step 1: Data Preparation (`src/data/penguinData.ts`)
X-axis will lead to overlapping text on narrow * Create a TS file to export `scatterData` and
screens. `ellipseData`.
* *Plan*: Reduce `tickCount` for the X-axis (e.g., * Clean keys (remove spaces/units from keys for easier
max 5 ticks). coding, e.g., `Body Mass (g)` -> `bodyMass`).
* **Action: Simplify Label** * Group ellipse data by species and sort by `order` to
* *Reason*: "Flipper Length (mm)" is long. prepare for path generation.
* *Plan*: Keep the unit but ensure font size is ### Step 2: Component Architecture
readable (min 12px). If space is tight, move units (`src/components/Visualization.tsx`)
to the subtitle or a corner label. * **Layout Wrapper**: A standard container with
### L2: Data Marks (Scatter & Ellipses) padding, utilizing Tailwind for responsive width.
* **Action: Rescale (Mark Size)** * **Header**: Title ("Penguin Morphology") and Subtitle
* *Reason*: Small dots are hard to see and tap. ("Body Mass vs Flipper Length").
* *Plan*: Increase the base size of the scatter * **Controls**: A flex-row of toggle buttons for
circles. Species (Legend).
* **Action: Recompose (Handling Ellipses in Recharts)** * **Chart Container**: `ResponsiveContainer` wrapping a
* *Constraint*: Recharts standard `Scatter` doesn't `ComposedChart`.
support arbitrary filled polygons easily. ### Step 3: Visualization Implementation (Recharts)

| DIS’26,June13–17,2026,Singapore |     |     |     |     |     |     |     |     |     | Trovatoetal. |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |
* **X Axis**: `dataKey="flipperLength"`, type number, verticaldimensiononmobile.Insteadofspreadingthejusticeshor-
| domain | `['auto', | 'auto']` | (or | specific | range based |     |     |     |     |     |     |
| ------ | --------- | -------- | --- | -------- | ----------- | --- | --- | --- | --- | --- | --- |
izontally,westackthemvertically,whichmakesmoreefficientuse
| on data | to  | avoid whitespace). |     |     |     |     |     |     |     |     |     |
| ------- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
oftheverticalscreenspaceandreduceswastedwhitespace.This
| * **Y Axis**: |     | `dataKey="bodyMass"`, |     | type | number. |     |     |     |     |     |     |
| ------------- | --- | --------------------- | --- | ---- | ------- | --- | --- | --- | --- | --- | --- |
newlayoutpreservestheinformationconveyedbytheoriginalvi-
| * **Ellipses | Layer**: |     |     |     |     |     |     |     |     |     |     |
| ------------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sualizationwhilemakingthestructuremorecompactandreadable
| * Use | Recharts | `<Customized |     | />`. |     |     |     |     |     |     |     |
| ----- | -------- | ------------ | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
* Inside the custom component, iterate through the onmobile.Inaddition,wereorganizethetitleanddescriptivetext:
3 species.
theoriginalin-chartannotation(“percentageofvotesinthemajor-
| * Use | the | X and Y scales | provided | by  | Recharts to |     |     |     |     |     |     |
| ----- | --- | -------------- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
ity,overeachjustice’scareer”)ismovedintoasubtitle,whichre-
| transform | data | coordinates |     | to pixel coordinates. |     |     |     |     |     |     |     |
| --------- | ---- | ----------- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- |
ducestextclutterinsidetheplotareaandprovidesnecessarycon-
| * Render | `<path>` | elements |     | with `fillOpacity={0.2}`. |     |     |     |     |     |     |     |
| -------- | -------- | -------- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- |
textbeforetheuserreadsthechart.
| * **Scatter | Layer**: |     |     |     |     |     |     |     |     |     |     |
| ----------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
* Use `<Scatter />` component. Similarly,Figure3(c)isanearlysquarechoroplethmapofFrance2,
* Map data to the axes. showingwhichpresidentialcandidatereceivedthemostvotesin
| * Color | points | based | on species. |     |     |     |     |     |     |     |     |
| ------- | ------ | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
eachdépartement.Differentcolorsencodedifferentcandidates,and
| ### Step | 4: Mobile | Interaction | Logic |     |     |     |     |     |     |     |     |
| -------- | --------- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
theoriginaldesktopdesignusesseverallongtextualannotations
| * State: | `activeSpecies` |     | (for | filtering), |     |     |     |     |     |     |     |
| -------- | --------------- | --- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
placedaroundthemaptohighlightregionalpatterns(e.g.,where
| `selectedPoint` |     | (for | tooltip). |     |     |     |     |     |     |     |     |
| --------------- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
* Interaction: specificcandidatesperformedespeciallywellorpoorly).Onmo-
* Tap Scatter Point -> Set `selectedPoint`. bile,ourmethodpreservesthemapitselfbutadaptsthesurround-
| * Tap | Background | ->  | Clear | `selectedPoint`. |     |     |     |     |     |     |     |
| ----- | ---------- | --- | ----- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
inglayouttotheverticalscreen.Ifwesimplyscaledtheoriginal
* Feedback:
chartdown,thesquaremapwouldleavealargeunusedareabe-
| * Render | a   | **"Detail | Card"** | (Glassmorphism | style) |     |     |     |     |     |     |
| -------- | --- | --------- | ------- | -------------- | ------ | --- | --- | --- | --- | --- | --- |
lowit,andthedensein-mapannotationswouldquicklybecome
| floating | at  | the bottom | or fixed | below | the header |     |     |     |     |     |     |
| -------- | --- | ---------- | -------- | ----- | ---------- | --- | --- | --- | --- | --- | --- |
when a point is selected. unreadable.Instead,weexternalizethesetextualannotationsinto
### Step 5: Styling & Polish a“Keyinsights”panelplacedbelowthemap.Eachinsightispre-
| * Apply | Tailwind | classes | for typography | (Inter | font, |     |     |     |     |     |     |
| ------- | -------- | ------- | -------------- | ------ | ----- | --- | --- | --- | --- | --- | --- |
sentedasaseparate,scrollablecardthatsummarizesanimportant
| legible      | sizes).    |     |       |                 |     |                   |                     |     |               |            |     |
| ------------ | ---------- | --- | ----- | --------------- | --- | ----------------- | ------------------- | --- | ------------- | ---------- | --- |
|              |            |     |       |                 |     | regional pattern, | such as strongholds |     | of particular | candidates | or  |
| * Add subtle | animations |     | using | `framer-motion` |     |                   |                     |     |               |            |     |
notableshiftscomparedwithpreviouselections.Inaddition,the
| (optional) |     | or CSS transitions |     | for the | filter chips. |     |     |     |     |     |     |
| ---------- | --- | ------------------ | --- | ------- | ------------- | --- | --- | --- | --- | --- | --- |
* Ensure axis lines are minimal (`stroke-gray-200`) and mobilemapsupportscommoninteractionssuchaszooming,pan-
grid lines are dashed and subtle. ning,andtooltipsontap.Theseinteractionsallowuserstoexplore
| This plan       | moves | the visualization |      | from a static,     |     |                  |                   |             |        |               |     |
| --------------- | ----- | ----------------- | ---- | ------------------ | --- | ---------------- | ----------------- | ----------- | ------ | ------------- | --- |
|                 |       |                   |      |                    |     | specific regions | in detail despite | the limited | screen | size, comple- |     |
| desktop-centric |       | analysis          | tool | to an interactive, |     |                  |                   |             |        |               |     |
mentingthesummarizedinsightsandhelpingreadersinvestigate
| mobile-friendly |     | exploration |     | interface. |     |     |     |     |     |     |     |
| --------------- | --- | ----------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
areasofinterestondemand.
Externalcomponentscannotonlypresenttextualinformation
|     |     |     |     |     |     | (as in cases | (a) and (c)), but | also act | as interactive | controls | that |
| --- | --- | --- | --- | --- | --- | ------------ | ----------------- | -------- | -------------- | -------- | ---- |
5 CaseStudies
|     |     |     |     |     |     | adapt and | extend the original | interaction | for mobile | devices. | In  |
| --- | --- | --- | --- | --- | --- | --------- | ------------------- | ----------- | ---------- | -------- | --- |
AsshowninFigure3,wecollectedasetofonlinevisualizationex- case(b),theoriginaldesktopvisualization3
alreadysupportsset-
amplesfromthewebandusedthemascasestorunoursystem.
tingthestockindexdate.Itisimplementedthroughmousehover:
Theseexamplescovercommoncharttypes,includinglinecharts, whentheuserhoversoveraverticalreferencelineatagiventime
barcharts,maps,andscatterplots.Ineachcase,theleftsideshows point,thechartrecomputesreturnsrelativetothatindexdate.How-
theoriginaldesktopvisualization,andtherightsideshowsthemo- ever,thishover-basedinteractiondoesnottranslatewelltomobile.
bilevisualizationautomaticallygeneratedbyourmethod.
Ontheonehand,thelimited“hover”capabilityontouchdevices
isbetterreservedfortooltips,whicharecrucialforinspectingex-
5.1 Single-ViewVisualizations
actvalues.Ontheotherhand,draggingdirectlyonthechartwith
Theoriginalvisualization1inFigure3(a)shows,foreachU.S.Supreme a finger can occlude the lines and hinder readability. To resolve
|     |     |     |     |     |     | this conflict, | we externalize | the “set index | date” | interaction | into |
| --- | --- | --- | --- | --- | --- | -------------- | -------------- | -------------- | ----- | ----------- | ---- |
Courtjustice,thepercentageofvotesincloselydecidedcasesin
whichthejusticesidedwiththemajority.Thehorizontalaxisen- a separate control placed below the chart. In our mobile design,
codes “percentage of votes in the majority,” and each dot corre- usersadjusttheindexdateviaadedicated“SetIndexDate”slider,
spondstoajustice.ThechartparticularlyhighlightsKennedy,whose whilethelinechartaboveupdatestoshowreturnsrelativetothe
percentageis76%,toemphasizethathetendstoalignwiththema- selecteddate.Atthesametime,touchinteractionsonthechartare
dedicatedsolelytotriggeringtooltipsforprecisevalueinspection.
jorityinsuchclosedecisions.Theoriginalchartisaverywide1D
scatterplotdesignedfordesktopdisplays.Ourmethodkeepsthe In this way, the original index-setting functionality is preserved,
scatterplotasthemainvisualencodingonmobile,butredesigns butreimplementedinamannerthatbettermatchesmobileinter-
thelayouttobetterfitasmall,verticallyorientedscreen.Ifwedi- actionhabitsandavoidsoverloadingthehoversemantics.
rectlyscaletheoriginalchartdowntoaphone,thetextbecomes
| too small | and there | is a large | amount | of unused | vertical space, |     |     |     |     |     |     |
| --------- | --------- | ---------- | ------ | --------- | --------------- | --- | --- | --- | --- | --- | --- |
whichharmsreadability.Toaddressthis,Proteuspreservestheorig-
inalhorizontaldatamappingbutreorganizetheitemsalongthe
2https://see-mike-out.github.io/cicero-supplemental/
1https://see-mike-out.github.io/cicero-supplemental/ 3https://vega.github.io/vega/examples/stock-index-chart/

Proteus:ShapeshiftingDesktopVisualizationsforMobileviaMulti-levelIntelligentAdaptation DIS’26,June13–17,2026,Singapore
Figure3:CasestudiesofProteusonfivereal-worldwebvisualizations.Foreachcase,theleftshowstheoriginaldesktopdesign
andtherightshowsthecorrespondingmobilevisualizationgeneratedbyProteus.
5.2 Multi-ViewVisualizations highlightsthecorrespondingsubsetofmoviesintheratingsdis-
Whenavisualizationcomprisesmultiplecoordinatedcharts,amo- tribution, enabling users to compare the selected genre against
bile redesign must not only resize individual views but also re- the overall population shown in the background. Our mobile re-
organizethe overalllayoutto preservereadabilityand coordina- designpreservesthiscoordinationbutreimplementstheinterac-
tion.Moreover,theseviewsoftensupportcross-filteringorcross- tioninatouch-friendlyform.Userstapabarinthelowerchart
highlighting,whereselectionsinonechartaffecttheothers.Such toselectagenre,andtheupperdistributionviewimmediatelyup-
multi-viewcoordinationistypicallyalreadyencodedintheorig- datestohighlighttheselectedmovieswhilekeepingtheremaining
inaldesktopvisualization;otherwise,thewebpagewouldnotbe recordsascontextualbackground.Tobetterfitthenarrow,verti-
abletosupportcross-linkinginthefirstplace.Ourapproachex- calscreenandimprovetapprecision,wealsoreorientthegenre
tracts these inter-view relationships and reassembles them into barchartfromverticalcolumnstohorizontalbars,whichprovides
amobile-friendlystructurethatmaintainstheoriginalanalytical morespaceforcategorylabelsandcreateslarger,easier-to-target
workflow. touchareas.
AsshowninFigure3(d),ourmethodpreservestheoriginalfil-
teringwidgets4andkeepsslider-basedinteractionastheprimary
6 Evaluation
mechanism for refining the dataset. However, instead of placing
allcontrolsinadenseblock(asondesktop),werepositioneach TovalidatetheeffectivenessofProteus,weconductedacompara-
slidertositdirectlywithitscorrespondingview,creatingaone- tiveuserstudyfocusingonthequalityofthegeneratedmobilevi-
to-onemappingbetweencontrolandchart.Inaddition,weextend sualizations.Ourevaluationaimstoanswerthefollowingresearch
thesliderdesign:whilethedesktopversiononlysupportssetting question:DoestheintegrationofaMulti-levelDesignSpacesignifi-
anupperbound,ourmobileversionprovidesarangesliderthat cantlyimprovethereadability,aesthetics,anddatafidelityofmobile
allowsuserstospecifybothlowerandupperbounds.Thefiltered adaptationscomparedtogenericLLM-basedapproaches? Wenote
resultsareimmediatelyreflectedacrossallcoordinatedviews,and thatwedonotincludedirectsystem-levelcomparisonswithMo-
theinterfaceexplicitlyreportsthenumberofselecteditems,mak- bileVisFixer[53]orCicero[21].Thisisbecausethesepriorworks
ingthecross-vieweffectoffilteringvisibleandeasytoverify. arenotdirectlycomparabletoourtasksetting.MobileVisFixerfo-
InFigure3(e),theoriginaldesktopdesign5 consistsoftwoco- cusesonamorerestrictedclassofvisualizations,primarilysingle
ordinated views: a binned ratings distribution (2D grid with cir- Cartesianchartswithlinearordiscretescales,whereasProteustar-
cles) on top and a genre bar chart below. The desktop visualiza- getsabroaderrangeofvisualizationspecifications.Ciceroisavisu-
tionsupportscross-viewlinking:selectingagenreinthebarchart alizationgrammarratherthananend-to-endsystemforautomatic
mobiletransformation.Therefore,insteadofreportingpotentially
4https://vega.github.io/vega/examples/crossfilter-flights/ misleadingdirectcomparisons,wefocusourevaluationoncom-
5https://altair-viz.github.io/gallery/interactive_cross_highlight.html parisonswithgenericLLM-basedbaselines.

DIS’26,June13–17,2026,Singapore Trovatoetal.
6.1 BenchmarkDatasetConstruction • D3.InteractionReasonableness:Istheinformationeasy
Torigorously evaluate our framework, we constructed a diverse toconsumeonaphone?Istheinteractiondesignreasonable
benchmark dataset comprising 67 representative desktop visual- andpracticallyuseful?(1=Useless,7=VeryUseful).
izations.Weexcludeexamplesthatarenear-duplicatesinstructure • D3.VisualAesthetics:Isthelayoutbalancedandvisually
andstyle.Theseexampleswerecuratedfromofficialgalleries(e.g., pleasing?(1=Cluttered/Broken,7=Professional).
theVegaexamplesgallery[47],theVega-Liteexamplesgallery[46],
theAltairexamplegallery[1],andtheD3examples[6])toensure Weacknowledgethatthesemetricsarenotpurelyobjectiveand
variety.Thiscollectionspansabroadspectrumofdatadensityand inevitablyinvolvesubjectivejudgment.Tomitigatepotentialbias,
structuralcomplexity,fromsimplestatisticalcharts(e.g.,bar,line, weadoptedthefollowingrandomizationandblindingstrategies:
area,andscatterplots)toviewswithmanyvisualelementsorcom-
posite layouts. As a result, the dataset poses diverse challenges • Randomizedcaseorder.Foreachparticipant,thesequence
formobileadaptation,includingdenseencodings,implementation ofvisualizationswasrandomlyshuffled,reducingorderef-
methods,andmulti-viewcomposition. fectsandlearningeffectsacrosstasks.
• Randomized side assignment. For each case, the posi-
6.2 ComparativeBaselines
tionsofthetwomobileadaptations(leftvs.right)wereran-
AstraightforwardbaselineistodirectlypromptasingleLLMto domized, and participants were not informed which side
generate mobile visualization code in one shot. However, in our correspondedtoProteusorthebaseline.Thispreventssys-
preliminarytests,thisapproachexhibitedaverylowcorrectness tematicpreferenceduetosidebiasandensuresthatratings
rate:inmostcases,theproducedcodefailedtorender.Sincesuch reflectperceivedqualityratherthansystemidentity.
failurespreventmeaningfulcomparisononvisualquality,wecon-
siderthissettingtooweakandultimatelyunfairasabaseline.To
ensure a fair comparison with our agentic system, we therefore
implemented a stronger baseline using the same Multi-agent ar- 6.4 Results
chitecture(Planner+Engineer+Critic)butremovedtheknowl-
Weaggregatedtheuserratingsandperformedstatisticalanalysis
edgeoftheMulti-levelDesignSpace.Thisbaselinehasaccessto
usingtheWilcoxonsigned-ranktesttodeterminesignificance.
thesametoolchain,codingenvironment,andexecutionfeedback
Acrossallbenchmarkvisualizations,Proteussuccessfullycom-
asProteus,andcaniterativelyrevisecodethroughagentcollabo-
pleted the end-to-end adaptation pipeline on 91.8% of cases, as
ration.WeusethelatestGemini3.0ProPreview[12]APIasa
judgedbyparticipants’D0ratings,whilethebaselineachieveda
high-capacityLLMbackboneforallagentsinbothProteusandthis
lower render success rate of 87.8%. For each failed case, D0 was
baseline.Forasinglevisualization,theend-to-endadaptationpro-
markedasfailureandthecorrespondingD1–D4scoreswereset
cesstypicallycompleteswithin10minutes(about2–10minutesin
to0.WerevisitedtheoriginallyfailedD0caseandfoundthatthe
ourexperiments).
failuredidnotrecurinarepeatedrun,suggestingthatitmayhave
resultedfromtransientsysteminstabilityratherthanapersistent
6.3 MetricsandProcedure
renderingissue.Intotal,12participantseachevaluated67visual-
Werecruited12participants,allwithpriorexperienceindatavi- izationpairs,providingratingsonfivedimensions(D0–D4),which
sualization work, to evaluate the outputs. The study followed a resultedin804pairedcomparisonsperdimension.Weappliedthe
within-subjectsdesign.Foreachcaseinthedataset,participants Wilcoxon signed-rank test because the rating distributions devi-
wereshowntheoriginaldesktopchartandtwomobileadaptations: atedfromnormality.
onegeneratedbyProteusandonebythebaseline.Eachparticipant AssummarizedinFig.4,Proteussignificantlyoutperformsthe
completedallcasesinapproximately60–90minutes.Participants baselineacrossallevaluationdimensions.Intermsofdatafidelity
evaluatedtheadaptationsbasedonthefollowingfivedimensions. (D1)andtextreadability(D2),ourmethodachieveshigherratings
NotethatD0servesasabinaryprerequisite,whileD1–D4arerated withstatisticalsignificance(𝑝 <0.05).Forinteractionreasonable-
ona7-pointLikertscale: ness (D3) and visual aesthetics (D4), the improvementsare even
• D0.ExecutionCompleteness:Beforeratingquality,par- morepronounced,withProteusshowinghighlysignificantadvan-
ticipantsfirstjudgedwhetherthesystemsuccessfullygen- tages(𝑝<0.001).
eratedarenderablevisualization.Atrialwasmarkedasfail- Thesequantitativeresultsareconsistentwithparticipants’qual-
ureiftheoutputcontainedsyntaxerrors,producedablank itativejudgmentsonspecificcases.Forexample,inFigure5(a2)
screen,oronlyshowedanobviouslyincompleterendering. (our result) and Figure 5 (a3) (baseline), the overall trend in (a3)
Otherwise,thevisualizationwasdirectlyassignedascore may look roughly similar at first glance, but the actual encoded
of0onD1–D4withoutfurtherevaluation. valuesdeviatefromtheoriginaldata;consequently,(a3)receivesa
• D1.DataFidelity:Doesthemobilechartaccuratelyreflect muchlowerdatafidelityscore.Similarly,inFig.5(b2),ourmobile
thedataoftheoriginaldesktopchartwithouthallucinationor versionallowsuserstoswitchbetweennormalanduniformmodes
criticalloss?(1=SevereDistortion,7=PerfectFidelity). viaanexternaliconwithasmoothanimatedtransition.Compared
• D2.PerceptualReadability:Isthetextlegible?Arevisual with a version that provides little or no meaningful interaction,
marksclearlydistinguishablewithoutoverlapping? (1=Un- thismorereasonableinteractiondesignisjudgedasmoreuseful
readable,7=HighlyReadable). forrealmobileusage,leadingtohigherD3scores.

Proteus:ShapeshiftingDesktopVisualizationsforMobileviaMulti-levelIntelligentAdaptation DIS’26,June13–17,2026,Singapore
Figure4:ResultsoftheuserstudycomparingProteuswiththebaselineacrossfiveevaluationdimensions.Theleftmostchart
showsthesuccessrateofrendering(D0),whiletheremainingboxplotsreportparticipantratingsfordatafidelity(D1),per-
ceptualreadability(D2),interactionreasonableness(D3)andvisualaesthetics(D4).WeusetheWilcoxonsigned-ranktestto
assessstatisticalsignificance;thenumberofasterisksaboveeachpairdenotesthesignificancelevel(*𝑝<0.05,**𝑝<0.01,***
𝑝<0.001).Overall,Proteussignificantlyoutperformsthebaselineonalldimensions.
7 Discussion 7.2 TheParadigmofAutomatedConsumption
Inthiswork,wepresentedagenerativeframeworkforautomat- Unlike mixed-initiative tools for visualization authoring (for ex-
ingtheadaptationofvisualizationsfromdesktoptomobileenvi- ample,recommendationsystemsthatassistdesignersduringcre-
ronments.Ourresultsdemonstratetheefficacyofmappingdesign ation),ourframeworktargetstheconsumptionsideofthevisual-
requirementstoamulti-leveldesignspace,butseverallimitations izationpipeline.Inthescenariosweconsider,suchasreadingdata-
anddirectionsforfutureresearchremain. richarticlesonmobiledevices,usersprimarilyassumetheroleof
readersratherthaneditors.Theytypicallylackthetime,expertise,
7.1 ComplexityandtheLongTailofDesign orinteractionaffordancestoengageiniterativedesignrefinement
ortoexplicitlyapproveadaptationchoices.
Our evaluation on standard galleries, such as D3 and Vega-Lite
Thissettingimposesastrongerrequirementforzero-intervention
examples, suggests that the framework handles canonical chart
robustness:thesystemmustoperateasanautonomousdesignproxy,
typeswithhighfidelityandreasonableefficiency.Nonetheless,the
resolvingdesignambiguities(forexample,whethertotransposean
broader visualization ecosystem includes a long tail of bespoke,
axisorintroducescrolling)withouthumanconfirmation.Acritical
highlycustomized,andartisticdesignsthatdivergefromconven-
componentinachievingthisautonomyisthecriticagent,which
tionalgrammars.
evaluatesintermediatedesignsandguidestheiterativerefinement
Forsuchcomplexcases,twomainchallengesarise.First,infer-
process. In our workflow, most cases involve multiple rounds of
encelatencytendstoincreasewiththestructuralcomplexityofthe
refinement,andweobservethatwithoutthecritic,thesystemfre-
SVGorDOMrepresentation,sincelargerandmoreintricatescene
quentlyfailstoconvergeonfunctionalmobilevariants.Thisun-
graphs require the LLM to process more tokens. Second, many
derscoresthatthecriticisnotanecessarypartoftheadaptation
bespokevisualizationsrelyoncustomlayoutlogic,suchasforce-
pipeline.Althoughthiszero-interventionconstraintlimitsthede-
directedsimulations,hierarchicalpacking,ordomain-specificen-
greeoffine-grained,human-curatedoptimizationthatispossible,
codings,whichdonotdecomposecleanlyintoourpredefinedatomic
itenablesapervasivereading-orientedusagemodeforvisualiza-
operators. Although the system can often produce a functional
tionandlowersthebarriertoaccessingcomplexdataonhandheld
mobile variant, preserving subtle aesthetic and stylistic qualities
devices,wheremanualadjustmentwouldbeimpractical.
remains difficult. Addressing this long tail may require domain-
Futureworkcouldexplorelightweightpreferencemechanisms
specificmodeladaptationandricherhigh-leveloperatorlibraries
thatliebetweenfullautomationandfullauthoringcontrol,forex-
tailoredtoparticularvisualizationgenres.
amplebyallowinguserstospecifyhigh-leveldefaults,suchaspre-
In addition, our current evaluation primarily examines visual
ferringscrollingoverpaginationorfavoringreducedclutterover
fidelity and perceived comparability. It does not directly assess
maximal detail, without requiring them to manipulate visualiza-
whethertheadaptedvisualizationssupportthesameanalytictasks
tionparametersdirectly.Onedirectionistoexposestyle-preservation
orleaduserstothesameconclusionsastheoriginaldesigns.This
preferencesatahighlevel.Forexample,althoughourdefaultadap-
limitationmaybeespeciallyimportantforbespokevisualizations,
tationstrategymayrevisecolorchoicestoimprovereadabilityand
wheretheeffectofadaptationcanvaryacrosstasktypes.Atask-
visualclarityonsmallscreens,userscanoptionallyrequeststronger
orientedevaluationofanalyticequivalenceisanimportantdirec-
tionforfuturework.

DIS’26,June13–17,2026,Singapore Trovatoetal.
Figure5:ComparisonbetweenProteusandthebaselineontworepresentativecases.(a1)and(b1)showtheoriginaldesktop
visualizations.(a2)and(b2)presentthemobileadaptationsgeneratedbyProteus,while(a3)and(b3)showthecorresponding
mobileversionsproducedbythebaseline.In(a),ourmethodbetterpreservestheunderlyingdatadistribution,whereasthe
baseline produces incorrect values even though the overall trend appears similar. In (b), Proteus provides a more readable
layoutandamorereasonableinteraction(e.g.,switchingbetweenNormalandUniformjitter).
preservationoftheoriginalcolorscheme.Inarerunofonerepre- datatable.Althoughrecentmultimodallanguagemodelsshowen-
sentativeexample(asshowninFigure6)undersuchaconstraint, couragingprogressinchartunderstanding,accurate,fine-grained
wefoundthattheadaptedmobilevisualizationcouldstillachieve deconstructionofarbitrarychartsfrompixelsisstillanopenchal-
goodusabilitywhilemorecloselymatchingthesourcestyle. lenge.Futureworkcouldintegrateouradaptationenginewithchart-
to-codemodels,formingapipelinethatreconstructs,adapts,and
7.3 GeneralizabilitytoRasterGraphics re-rendersstaticbitmapvisualizationsasresponsivemobilecom-
ponents.
Our current implementation operates primarily on vector-based
specifications(e.g.,SVG),wheretheunderlyingdataandstructural
8 ConclusionandFutureWork
semanticsaredirectlyaccessible.Thisfocusalignswiththedomi-
nantparadigmofmodernweb-basedvisualization(e.g.,D3,Vega- Weaddressedthegapbetweendesktop-orientedvisualizationau-
Lite).However,asubstantialportionofexistingvisualizations,es- thoringandmobileconsumption,wheresimpleresizingoftenharms
peciallylegacycontent,remainsavailableonlyasstaticrasterim- readabilityandinteraction.Wearguedthateffectivemobileadap-
ages,wheredataandmarksareencodedpurelyatthepixellevel. tationrequiresmorethangeometricresizingandshouldinsteadre-
Extendingourframeworktorastergraphicswouldrequirean visethevisualizationcontentinameaning-preservingway.Tothis
additional upstream component for reverse engineering. Such a end,weproposedamulti-leveldesignspacethatorganizesadap-
componentwouldemploycomputervisionandOCRtechniquesto tationasahierarchyofdecisions,fromglobalstructure,through
reconstructascenegraphandrecoveranapproximateunderlying referenceelements,toindividualvisualelements.Guidedbythis

Proteus:ShapeshiftingDesktopVisualizationsforMobileviaMulti-levelIntelligentAdaptation DIS’26,June13–17,2026,Singapore
inComputingSystems,JosephA.Konstan,EdH.Chi,andKristinaHöök(Eds.).
ACM,473–482.doi:10.1145/2207676.2207741
[10] Will Epperson, Gagan Bansal, Victor C. Dibia, Adam Fourney, Jack Gerrits,
Erkang(Eric)Zhu,andSaleemaAmershi.2025.InteractiveDebuggingandSteer-
ingofMulti-AgentAISystems.InProceedingsofACMCHIConferenceonHu-
manFactorsinComputingSystems,NaomiYamashita,VanessaEvers,KojiYatani,
SharonXianghuaDing,BongshinLee,MarshiniChetty,andPhoebeO.Toups
Dugas(Eds.).ACM,156:1–156:15.doi:10.1145/3706598.3713581
[11] Facebook.2013. React:AJavaScriptlibraryforbuildinguserinterfaces. https:
//reactjs.org.
[12] Google.2025.Gemini3.0ProPreview. https://deepmind.google/models/gemini/
pro/Accessed:2025-01-10.
[13] KanikaGoswami,PuneetMathur,RyanRossi,andFranckDernoncourt.2025.
PlotGen:Multi-AgentLLM-basedScientificDataVisualizationviaMultimodal
Feedback.arXivpreprintarXiv:2502.00988(2025).
[14] TaichengGuo,XiuyingChen,YaqiWang,RuidiChang,ShichaoPei,NiteshV.
Figure 6: Style preservation during mobile adaptation. (a)
Chawla,OlafWiest,andXiangliangZhang.2024.LargeLanguageModelBased
Theoriginaldesktopvisualization.(b)Theadaptedmobilevi- Multi-agents:ASurveyofProgressandChallenges.InProceedingsoftheThirty-
sualizationgeneratedunderaconstraintthatpreservesthe ThirdInternationalJointConferenceonArtificialIntelligence,IJCAI2024,Jeju,
South Korea, August 3-9, 2024. ijcai.org, 8048–8057. https://www.ijcai.org/
originalcolorschememoreclosely. proceedings/2024/890
[15] JeffreyHeerandBenShneiderman.2012.Interactivedynamicsforvisualanaly-
sis.Commun.ACM55,4(2012),45–54.doi:10.1145/2133806.2133821
[16] JeffreyHeer,FernandaB.Viégas,andMartinWattenberg.2007. Voyagersand
framework,weintroducedProteus,anLLM-drivenmulti-agentsys- voyeurs:supportingasynchronouscollaborativeinformationvisualization.In
temthatparsesheterogeneouswebcharts,planssemantictransfor- ProceedingsofACMCHIConferenceonHumanFactorsinComputingSystems,
MaryBethRossonandDavidJ.Gilmore(Eds.).ACM,1029–1038. doi:10.1145/
mations,andgeneratesexecutablemobile-optimizedviews.Acon- 1240624.1240781
trolleduserstudyonreal-worldvisualizationsshowsthatProteus [17] JaneHoffswell,WilmotLi,andZhichengLiu.2020. Techniquesforflexiblere-
sponsivevisualizationdesign.IEEETransactionsonVisualizationandComputer
outperformsastrongmulti-agentLLMbaselineinrenderingsuc-
Graphics27,2(2020),1336–1346.
cessandfourqualitativedimensions,includingdatafidelity,read- [18] EricHorvitz.1999. PrinciplesofMixed-InitiativeUserInterfaces.InProceed-
ability,interactionquality,andvisualaesthetics.Inthefuture,we ingsofACMCHIConferenceonHumanFactorsinComputingSystems,MarianG.
WilliamsandMarkW.Altom(Eds.).ACM,159–166.doi:10.1145/302979.303030
plantoextendProteusbysupportingrapidend-usercustomization
[19] KevinZengHu,MichielA.Bakker,StephenLi,TimKraska,andCésarA.Hidalgo.
ofmobileadaptationsandbroadeninginputcoveragefromvector- 2019.VizML:AMachineLearningApproachtoVisualizationRecommendation.
basedwebchartstoraster-onlyvisualizations. InProceedingsofACMCHIConferenceonHumanFactorsinComputingSystems,
StephenA.Brewster,GeraldineFitzpatrick,AnnaL.Cox,andVassilisKostakos
(Eds.).ACM,128.doi:10.1145/3290605.3300358
Acknowledgments [20] NicholasR. Jennings,KatiaP.Sycara,and MichaelJ. Wooldridge.1998. A
RoadmapofAgentResearchandDevelopment.Auton.AgentsMultiAgentSyst.
ThisprojectissupportedbytheMinistryofEducation,Singapore, 1,1(1998),7–38.doi:10.1023/A:1010090405266
underitsAcademicResearchFundTier2(ProposalID:T2EP202220 [21] HyeokKim,RyanRossi,FanDu,EunyeeKoh,ShunanGuo,JessicaHullman,
andJaneHoffswell.2022.Cicero:ADeclarativeGrammarforResponsiveVisu-
049),andbytheStartUpGrantawardedtoYongWang.Anyopin-
alization.InProceedingsofACMCHIConferenceonHumanFactorsinComputing
ions,findingsandconclusions,orrecommendationsexpressedin Systems(NewOrleans,LA,USA)(CHI’22).AssociationforComputingMachin-
thismaterialarethoseoftheauthor(s)anddonotreflecttheviews ery,NewYork,NY,USA,Article600,15pages. doi:10.1145/3491102.3517455
[22] ChufanLai,ZhixianLin,RuikeJiang,YunHan,CanLiu,andXiaoruYuan.2020.
oftheMinistryofEducation,Singapore. AutomaticAnnotationSynchronizingwithTextualDescriptionforVisualiza-
tion.InProceedingsoftheACMCHIConferenceonHumanFactorsinComputing
References Systems(Honolulu,HI,USA)(CHI’20).AssociationforComputingMachinery,
NewYork,NY,USA,1–13. doi:10.1145/3313831.3376443
[1] AltairDevelopers.2026. AltairExampleGallery. https://altair-viz.github.io/ [23] Guohao Li, Hasan Hammoud, Hani Itani, Dmitrii Khizbullin, and Bernard
gallery/index.htmlAccessed:2026-01-20. Ghanem. 2023. CAMEL:Communicative Agents for ”Mind” Exploration of
[2] SaleemaAmershi,DanielS.Weld,MihaelaVorvoreanu,AdamFourney,Besmira Large Language Model Society. In Advances in Neural Information Process-
Nushi,PennyCollisson,JinaSuh,ShamsiT.Iqbal,PaulN.Bennett,KoriInkpen, ing Systems 36: Annual Conference on Neural Information Processing Sys-
JaimeTeevan,RuthKikin-Gil,andEricHorvitz.2019.GuidelinesforHuman-AI tems 2023, NeurIPS 2023, New Orleans, LA, USA, December 10 - 16, 2023,
Interaction.InProceedingsofACMCHIConferenceonHumanFactorsinCom- Alice Oh, Tristan Naumann, Amir Globerson, Kate Saenko, Moritz Hardt,
putingSystems,StephenA.Brewster,GeraldineFitzpatrick,AnnaL.Cox,and andSergeyLevine(Eds.). http://papers.nips.cc/paper_files/paper/2023/hash/
VassilisKostakos(Eds.).ACM,3.doi:10.1145/3290605.3300233 a3621ee907def47c1b952ade25c67698-Abstract-Conference.html
[3] KeithAndrews,DavidEgger,andPeterOberrauner.2023.RespVis:AD3Exten- [24] ShufanLi,CongxiLu,LinkaiLi,andHaoshuaiZhou.2022. Chart-RCNN:Ef-
sionforResponsiveSVGCharts.In202327thInternationalConferenceInforma- ficientLineChartDataExtractionfromCameraImages. CoRRabs/2211.14362
tionVisualisation(IV).IEEE,19–22. (2022).arXiv:2211.14362doi:10.48550/ARXIV.2211.14362
[4] BenjaminBBederson.2000.Fisheyemenus.Proceedingsofthe13thannualACM [25] CanLiu,ChunlinDa,XiaoxiaoLong,YuxiaoYang,YuZhang,andYongWang.
symposiumonUserinterfacesoftwareandtechnology(2000),217–225. 2025.SimVecVis:ADatasetforEnhancingMLLMsinVisualizationUnderstand-
[5] AlanH.BondandLesGasser(Eds.).1988.ReadingsinDistributedArtificialIntel- ing.In2025IEEEVisualizationandVisualAnalytics(VIS).26–30. doi:10.1109/
ligence.MorganKaufmann,SanMateo,CA. VIS60296.2025.00010
[6] D3.jsCommunity.2026.D3.jsGalleryandExamples. https://d3js.org/Accessed: [26] CanLiu,YunHan,RuikeJiang,andXiaoruYuan.2021. ADVISor:Automatic
2026-01-20. VisualizationAnswerforNatural-LanguageQuestiononTabularData.InPro-
[7] ÇagatayDemiralp,PeterJ.Haas,SrinivasanParthasarathy,andTejaswiniPeda- ceedingsofIEEEPacificVisualizationSymposium.6–15.
pati.2017.Foresight:RecommendingVisualInsights.Proc.VLDBEndow.10,12 [27] CanLiu,JaeukLee,TianheChen,ZhibangJiang,XiaolinWen,andYongWang.
(2017),1937–1940.doi:10.14778/3137765.3137813 2026.FromStatictoInteractive:AuthoringInteractiveVisualizationsviaNatural
[8] VictorDibiaandÇagatayDemiralp.2019. Data2Vis:AutomaticGenerationof Language.arXiv:2601.17736[cs.HC] https://arxiv.org/abs/2601.17736
DataVisualizationsUsingSequence-to-SequenceRecurrentNeuralNetworks. [28] CanLiu,LiwenhanXie,YunHan,XiaoruYuan,etal.2020. AutoCaption:An
IEEEComputerGraphicsandApplications39,5(2019),33–46.doi:10.1109/MCG. ApproachtoGenerateNaturalLanguageDescriptionFromVisualizationAuto-
2019.2924636 matically.InProceedingsofIEEEPacificVisualizationSymposium.191–195.
[9] AlexEndert,PatrickFiaux,andChrisNorth.2012. Semanticinteractionfor [29] YuyuLuo,NanTang,GuoliangLi,ChengliangChai,WenboLi,andXuediQin.
visualtextanalytics.InProceedingsofACMCHIConferenceonHumanFactors 2021. SynthesizingNaturalLanguagetoVisualization(NL2VIS)Benchmarks

DIS’26,June13–17,2026,Singapore Trovatoetal.
FromNL2SQLBenchmarks.InProceedingsoftheInternationalConferenceon [51] KanitWongsuphasawat,DominikMoritz,AnushkaAnand,JockD.Mackinlay,
ManagementofData.1235–1247. BillHowe,andJeffreyHeer.2016. Voyager:ExploratoryAnalysisviaFaceted
[30] JockMackinlay.1986. AutomatingtheDesignofGraphicalPresentationsof BrowsingofVisualizationRecommendations.IEEETransactionsonVisualization
RelationalInformation.ACMTransactionsonGraphics5,2(1986),110–141. andComputerGraphics22,1(2016),649–658.doi:10.1109/TVCG.2015.2467191
[31] JockD.Mackinlay,PatHanrahan,andChrisStolte.2007.ShowMe:Automatic [52] MichaelWooldridge.2009.AnIntroductiontoMultiAgentSystems(2nded.).John
| PresentationforVisualAnalysis. |     |     | IEEETransactionsonVisualizationandCom- |     |     | Wiley&Sons. |
| ------------------------------ | --- | --- | -------------------------------------- | --- | --- | ----------- |
puterGraphics13,6(2007),1137–1144.doi:10.1109/TVCG.2007.70594 [53] AoyuWu,WaiTong,TimDwyer,BongshinLee,PetraIsenberg,andHuamin
[32] ThomasW.MaloneandMichaelS.Bernstein(Eds.).2015.HandbookofCollective Qu.2020.MobileVisFixer:Tailoringwebvisualizationsformobilephoneslever-
Intelligence.TheMITPress,Cambridge,MA. aginganexplainablereinforcementlearningframework. IEEETransactionson
[33] Microsoft.2012. TypeScript:JavaScriptwithsyntaxfortypes. https://www. VisualizationandComputerGraphics27,2(2020),464–474.
typescriptlang.org. [54] AoyuWu,LiwenhanXie,BongshinLee,YunWang,WeiweiCui,andHuamin
[34] DominikMoritz,ChenglongWang,GregL.Nelson,HaldenLin,AdamM.Smith, Qu.2021.Learningtoautomatechartlayoutconfigurationsusingcrowdsourced
BillHowe,andJeffreyHeer.2019.FormalizingVisualizationDesignKnowledge pairedcomparison.InProceedingsofthe2021CHIConferenceonHumanFactors
asConstraints:ActionableandExtensibleModelsinDraco.IEEETransactionson inComputingSystems.1–13.
VisualizationandComputerGraphics25,1(2019),438–448. doi:10.1109/TVCG. [55] Liwenhan Xie, Yanna Lin, Can Liu, Huamin Qu, and Xinhuan Shu. 2025.
2018.2865240 DataWink:ReusingandAdaptingSVG-basedVisualizationExampleswithLarge
[35] ArpitNarechania,ArjunSrinivasan,andJohnT.Stasko.2021.NL4DV:AToolkit MultimodalModels.IEEETransactionsonVisualizationandComputerGraphics
| forGeneratingAnalyticSpecificationsforDataVisualizationfromNaturalLan- |     |     |     |     |     | (2025). |
| ---------------------------------------------------------------------- | --- | --- | --- | --- | --- | ------- |
guageQueries.IEEETransactionsonVisualizationandComputerGraphics27,2 [56] WeiZeng,XiChen,YihanHou,LingdanShao,ZheChu,andRemcoChang.2023.
(2021),369–379.doi:10.1109/TVCG.2020.3030378 Semi-AutomaticLayoutAdaptationforResponsiveMultiple-ViewVisualization
[36] GeliangOuyang,JingyaoChen,ZhiheNie,YiGui,YaoWan,HongyuZhang,and Design. IEEETransactionsonVisualizationandComputerGraphics30,7(2023),
| DongpingChen.2025.NVAGENT:AutomatedDataVisualizationfromNatural |     |     |     |     |     | 3798–3812. |
| --------------------------------------------------------------- | --- | --- | --- | --- | --- | ---------- |
LanguageviaCollaborativeAgentWorkflow. arXivpreprintarXiv:2502.05036 [57] YuZhang,BobCoecke,andMinChen.2021.MI3:Machine-initiatedIntelligent
(2025). InteractionforInteractiveClassificationandDataReconstruction. ACMTrans.
[37] JorgePocoandJeffreyHeer.2017.Reverse-EngineeringVisualizations:Recover- Interact.Intell.Syst.11,3-4(2021),18:1–18:34.doi:10.1145/3412848
ingVisualEncodingsfromChartImages.ComputerGraphicsForum36,3(2017),
353–363.doi:10.1111/CGF.13193 Received20February2007;revised12March2009;accepted5June2009
[38] XuediQin,YuyuLuo,NanTang,andGuoliangLi.2020.Makingdatavisualiza-
| tionmoreefficientandeffective:asurvey. |                                |     | TheVLDBJournal29,1(Jan.2020), |     |     |     |
| -------------------------------------- | ------------------------------ | --- | ----------------------------- | --- | --- | --- |
| 93–117.                                | doi:10.1007/s00778-019-00588-3 |     |                               |     |     |     |
[39] ManolisSavva,NicholasKong,ArtiChhajta,LiFei-Fei,ManeeshAgrawala,and
JeffreyHeer.2011.ReVision:automatedclassification,analysisandredesignof
chartimages.InProceedingsofACMSymposiumonUserInterfaceSoftwareand
Technology,JeffreyS.Pierce,ManeeshAgrawala,andScottR.Klemmer(Eds.).
ACM,393–402.doi:10.1145/2047196.2047247
[40] SarahSchöttler,JasonDykes,JoWood,UtaHinrichs,andBenjaminBach.2024.
Constraint-basedbreakpointsforresponsivevisualizationdesignanddevelop-
ment.IEEETransactionsonVisualizationandComputerGraphics(2024).
| [41] Yongliang         | Shen,       | Kaitao Song,                                       | Xu Tan, Dongsheng | Li, Weiming  | Lu, and          |     |
| ---------------------- | ----------- | -------------------------------------------------- | ----------------- | ------------ | ---------------- | --- |
| Yueting                | Zhuang.     | 2023. HuggingGPT:                                  | Solving           | AI Tasks     | with ChatGPT     |     |
| and its                | Friends in  | Hugging                                            | Face. In Advances | in Neural    | Information Pro- |     |
| cessing                | Systems 36: | Annual Conference                                  | on Neural         | Information  | Processing Sys-  |     |
| tems 2023,             | NeurIPS     | 2023, New                                          | Orleans, LA, USA, | December     | 10 - 16, 2023,   |     |
| Alice Oh,              | Tristan     | Naumann,                                           | Amir Globerson,   | Kate Saenko, | Moritz Hardt,    |     |
| andSergeyLevine(Eds.). |             | http://papers.nips.cc/paper_files/paper/2023/hash/ |                   |              |                  |     |
77c33e6a367922d003ff102ffb92b658-Abstract-Conference.html
| [42] Noah   | Shinn, Federico   | Cassano,                                           | Ashwin Gopinath,    | Karthik        | Narasimhan,     |     |
| ----------- | ----------------- | -------------------------------------------------- | ------------------- | -------------- | --------------- | --- |
| and Shunyu  | Yao.              | 2023.                                              | Reflexion: language | agents         | with verbal re- |     |
| inforcement | learning.         | In Advances                                        | in Neural           | Information    | Processing Sys- |     |
| tems 36:    | Annual Conference | on                                                 | Neural Information  | Processing     | Systems 2023,   |     |
| NeurIPS     | 2023, New         | Orleans,                                           | LA, USA, December   | 10 -           | 16, 2023, Alice |     |
| Oh, Tristan | Naumann,          | Amir                                               | Globerson, Kate     | Saenko, Moritz | Hardt, and      |     |
| Sergey      | Levine (Eds.).    | http://papers.nips.cc/paper_files/paper/2023/hash/ |                     |                |                 |     |
1b44b878bb782e6954cd888628510e90-Abstract-Conference.html
| [43] BenShneiderman.1996. |     | Theeyeshaveit:Ataskbydatatypetaxonomyfor |     |     |     |     |
| ------------------------- | --- | ---------------------------------------- | --- | --- | --- | --- |
informationvisualizations.InProceedingsofthe1996IEEESymposiumonVisual
Languages.IEEE,336–343.
| [44] SignificantGravitas.2023. |     | AutoGPT. | https://github.com/Significant-Gravitas/ |     |     |     |
| ------------------------------ | --- | -------- | ---------------------------------------- | --- | --- | --- |
AutoGPT
[45] ManasiVartak,SajjadurRahman,SamuelMadden,AdityaG.Parameswaran,and
NeoklisPolyzotis.2015.SEEDB:EfficientData-DrivenVisualizationRecommen-
dationstoSupportVisualAnalytics.Proc.VLDBEndow.8,13(2015),2182–2193.
doi:10.14778/2831360.2831371
| [46] Vega-LiteProject.2026.Vega-LiteExampleGallery. |     |     |     | https://vega.github.io/vega- |     |     |
| --------------------------------------------------- | --- | --- | --- | ---------------------------- | --- | --- |
lite/examples/Accessed:2026-01-20.
| [47] Vega Project. | 2026. | Vega Example | Gallery. | https://vega.github.io/vega/ |     |     |
| ------------------ | ----- | ------------ | -------- | ---------------------------- | --- | --- |
examples/Accessed:2026-01-20.
| [48] Fernanda | B. Viégas, | Martin | Wattenberg, Frank | van Ham, | Jesse Kriss, and |     |
| ------------- | ---------- | ------ | ----------------- | -------- | ---------------- | --- |
MatthewM.McKeon.2007.ManyEyes:aSiteforVisualizationatInternetScale.
IEEETransactionsonVisualizationandComputerGraphics13,6(2007),1121–
1128.doi:10.1109/TVCG.2007.70577
[49] GuanzhiWang,YuqiXie,YunfanJiang,AjayMandlekar,ChaoweiXiao,Yuke
| Zhu,LinxiFan,andAnimaAnandkumar.2024. |     |     | Voyager:AnOpen-EndedEm- |     |     |     |
| ------------------------------------- | --- | --- | ----------------------- | --- | --- | --- |
bodiedAgentwithLargeLanguageModels.Trans.Mach.Learn.Res.2024(2024).
https://openreview.net/forum?id=ehfRiF0R3a
| [50] Anton | Wolter, Georgios | Vidalakis, | Michael Yu, | Ankit Grover, | and Vaishali |     |
| ---------- | ---------------- | ---------- | ----------- | ------------- | ------------ | --- |
Dhanoa.2025.Multi-AgentDataVisualizationandNarrativeGeneration.arXiv
preprintarXiv:2509.00481(2025).