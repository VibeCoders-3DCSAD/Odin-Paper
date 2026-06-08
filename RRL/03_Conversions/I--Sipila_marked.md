Master’s Programme in Computer, Communication and Information Sciences
| Proof   | of concept  | of centralized | personal |
| ------- | ----------- | -------------- | -------- |
| finance | application |                |          |
Milla Sipilä
Master’s Thesis
2025

MillaSipilä
Author
Proofofconceptofcentralizedpersonalfinanceapplication
Title
Computer,CommunicationandInformationSciences
Degree programme
Algorithms,Logic,andComputation
Major
ArtoHellas
Supervisor and advisor
29.6.2025 60 English
Date Number of pages Language
Abstract
This thesis presents the design and development of a centralized personal finance
management application using the Design Science Research Methodology (DSRM).
Theworkisbasedinpriorresearchonfinancialbehavior,planning,andmanagement
tools, explaining how motivation, structured planning, and digital solutions influence
financial well-being. The goal was to address real-world challenges faced by an
individualstakeholder,whoseexistingfinancialtrackingsystemreliedonfragmented
tools and manual processes. A proof-of-concept (PoC) application was developed
usingFlutter,.NET,andMongoDB,includingfunctionalitiessuchasassettracking,
categorized cash flow visualization, real-time data updates, and financial report
generation. Thesolutionwasiterativelydesignedbasedonstakeholder’sfeedbackand
evaluatedthroughtask-basedtesting,structuredquestionnaires,andcomparisontothe
baseline system. Results show significant improvements in automation, accuracy, and
usability. Whilesomefeatures,suchasauthenticationandfullbankingintegration,
were out of scope for this PoC, the system provides a strong foundation for further
developmentandwiderapplicabilityinthedomainofpersonalfinancemanagement.
Personalfinance,Financialplanning,DesignScienceResearch,Proofof
Keywords
Concept,Personalfinanceapplication,Financialtracking,User-centered
design

MillaSipilä
Tekijä
Keskitetynhenkilökohtaisenrahoitussovelluksenkonseptitodistus
Työn nimi
Tietotekniikka
Koulutusohjelma
Algoritmit,Logiikka,jaLaskenta
Pääaine
ArtoHellas
Työn valvoja ja ohjaaja
29.6.2025 60 englanti
Päivämäärä Sivumäärä Kieli
Tiivistelmä
Tämä diplomityö käsittelee keskitetyn henkilökohtaisen taloudenhallintasovelluk-
sensuunnitteluajakehittämistähyödyntäenDesignScienceResearchMethodology
(DSRM)-tutkimusmenetelmää.Työnteoreettinentaustapohjautuuaiempaankirjalli-
suuteentaloudellisestakäyttäytymisestä,suunnittelustajataloudenhallintatyökaluista,
joissa korostuvat motivaatio, suunnitelmallisuus ja digitaaliset ratkaisut taloudellisen
hyvinvoinnintukena.Työntavoitteenaoliparantaayksityisentoimijanolemassaolevaa
järjestelmää,joka koostuihajanaisista työkaluista ja manuaalisistaprosesseista. Kon-
septitodistuskehitettiinhyödyntäenteknologioitakutenFlutter,.NETjaMongoDB.
Sovellus sisältää toimintoja kuten varallisuuden seuranta, kategorisoitu kassavirta-
analyysi, reaaliaikainen datan päivitys sekä talousraporttien generointi. Ratkaisu
suunniteltiin iteratiivisesti toimijan palautteen perusteella ja arvioitiin tehtäväpoh-
jaisella testauksella,strukturoidulla kyselyllä ja vertailulla aiempaan järjestelmään.
Tuloksetosoittavatmerkittäviäparannuksiaautomaatiossa,luotettavuudessajakäytet-
tävyydessä.Vaikkakaikkiatoimintoja,kutentunnistautumistataipankki-integraatioita,
ei toteutettu konseptitodistuksessa, sovellus luo vahvan pohjan jatkokehitykselle ja
laajemmallekäytettävyydellehenkilökohtaisentaloudenhallinnanalueella.
Henkilökohtainentalous,Taloussuunnittelu,Kehittämistutkimus,
Avainsanat
Konseptitodistus,Henkilökohtaisentaloudensovellus,Talouden
seuranta,Käyttäjälähtöinensuunnittelu

Contents
Abstract 2
Abstract(inFinnish) 3
Contents 4
Symbolsandabbreviations 6
1 Introduction 7
1.1 Contextandmotivation . . . . . . . . . . . . . . . . . . . . . . . . 7
1.2 Objectivesandscope . . . . . . . . . . . . . . . . . . . . . . . . . 8
1.3 Useofartificialintelligencetools . . . . . . . . . . . . . . . . . . . 8
1.4 Thesisstructure . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2 Literaturereview 10
2.1 Financialliteracyandbehaviors . . . . . . . . . . . . . . . . . . . 10
2.2 Personalfinancialplanning . . . . . . . . . . . . . . . . . . . . . . 11
2.3 Personalfinancemanagementtools . . . . . . . . . . . . . . . . . . 13
2.4 Designscienceresearch . . . . . . . . . . . . . . . . . . . . . . . . 15
3 Researchmethodology 18
3.1 DSRMactions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.1.1 Problemidentificationandmotivation . . . . . . . . . . . . 18
3.1.2 Definetheobjectivesforthesolution . . . . . . . . . . . . . 19
3.1.3 Designanddevelopment . . . . . . . . . . . . . . . . . . . 19
3.1.4 Demonstration . . . . . . . . . . . . . . . . . . . . . . . . 20
3.1.5 Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3.1.6 Communication . . . . . . . . . . . . . . . . . . . . . . . . 22
3.2 MotivationforDSRM . . . . . . . . . . . . . . . . . . . . . . . . . 23
4 Problemidentificationandmotivation 24
4.1 Stakeholderinsightsfromquestionnaire . . . . . . . . . . . . . . . 24
4.1.1 Currentfinancialmanagementapproach . . . . . . . . . . . 24
4.1.2 Frequencyofuse . . . . . . . . . . . . . . . . . . . . . . . 24
4.1.3 Challengeswiththecurrentsystem . . . . . . . . . . . . . 24
4.1.4 Desiredfeaturesforanimprovedsolution . . . . . . . . . . 25
4.1.5 Stakeholderreflections . . . . . . . . . . . . . . . . . . . . 25
4.2 Problemdescription . . . . . . . . . . . . . . . . . . . . . . . . . . 25
4.3 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
5 Definingobjectivesforthesolution 28
5.1 Requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
5.2 Prioritizedobjectives . . . . . . . . . . . . . . . . . . . . . . . . . 30
4

6 Designanddevelopment 32
6.1 Architecturaldecisions . . . . . . . . . . . . . . . . . . . . . . . . 32
6.2 Systemarchitecture . . . . . . . . . . . . . . . . . . . . . . . . . . 34
6.3 Implementationdetails . . . . . . . . . . . . . . . . . . . . . . . . 35
6.3.1 Datamodelanddomainobjects . . . . . . . . . . . . . . . 35
6.3.2 Userinterfacestructureanddesignapproach . . . . . . . . 36
6.3.3 Developmenttoolsandprocess . . . . . . . . . . . . . . . . 37
7 Demonstration 38
7.1 Addressingcomplexityandhumanerror . . . . . . . . . . . . . . . 38
7.2 Solvingscalabilitylimitations . . . . . . . . . . . . . . . . . . . . 40
7.3 Automatingfinancialdataretrieval . . . . . . . . . . . . . . . . . . 41
7.4 Centralizedtrackingacrosscategories . . . . . . . . . . . . . . . . 43
7.5 Integratedandefficientreporting . . . . . . . . . . . . . . . . . . . 45
8 Evaluation 48
8.1 Task-basedusertesting . . . . . . . . . . . . . . . . . . . . . . . . 48
8.2 Stakeholderinsightsfromquestionnaire . . . . . . . . . . . . . . . 49
8.2.1 Generalimpressions . . . . . . . . . . . . . . . . . . . . . 49
8.2.2 Featuresatisfaction . . . . . . . . . . . . . . . . . . . . . . 49
8.2.3 Problem-solvingimpact . . . . . . . . . . . . . . . . . . . 50
8.2.4 Suggestionsandfutureimprovements . . . . . . . . . . . . 50
8.3 Comparisontobaseline . . . . . . . . . . . . . . . . . . . . . . . . 50
8.4 Evaluationagainstdesignobjectives . . . . . . . . . . . . . . . . . 51
9 Discussion 54
9.1 Summaryofresultsandimpact . . . . . . . . . . . . . . . . . . . . 54
9.2 Limitationsofthesolution . . . . . . . . . . . . . . . . . . . . . . 55
9.3 ReflectiononDSRM . . . . . . . . . . . . . . . . . . . . . . . . . 56
9.4 Opportunitiesforfuturedevelopment . . . . . . . . . . . . . . . . . 57
10 Conclusions 58
References 59
5

Symbols and abbreviations
Abbreviations
API ApplicationProgrammingInterface
DB Database
DS DesignScience
DSR DesignScienceResearch
DSRM DesignScienceResearchMethodology
FR FunctionalRequirement
PFM PersonalFinanceManagement
PoC Proof-of-concept
QA QualityAttribute
STD Self-DeterminationTheory
UI UserInterface
UX UserExperience
6

1 Introduction
1.1 Context and motivation
Peter Drucker said, "If you can’t measure it, you can’t manage it" highlighting the
importanceofdataindecision-making. Hamming’squote,"Yougetwhatyoumeasure"
representshowweguideourselveswithmeasuringthestepswetaketowardachieving
our goals. W. Edwards Deming presented the saying "In God we trust, all others
bring data" which is a reminder that we should base our decisions off data and not
assumptivebeliefs.
This holdstrue forPersonal Finance Management(PFM) whichrequires financial
literacy, motivation and structured planning to make informed financial decisions.
Studiessuggestthatpeoplewithhigherratesoffinancialliteracyaremorelikelyto
participateintypesofbehaviorsrelatedtosaving,investing,andavoidingunnecessary
financial mistakes (Lusardi and Mitchell 2014; Rajesh and Giridhar 2024). In
addition, globalsurveys suggestthat lowerratesof financialliteracy remainin many
demographics,particularlyyoungadults,women,andamonglowerincomeoreducation
levels(AtkinsonandMessy2012;LusardiandMitchell2014).
Financialknowledgealoneisnotenoughtocreatebehavioralchange. DiDomenico
et al. (2022) explains that autonomous motivation, driven by internal values and
interest,ismorestronglyassociatedwithsustainablefinancialhabitsandwell-being
thancontrolledmotivationwhichrelatestoexternalpressureorguilt. Furthermore,
Kaye et al. (2014) has shown that financial management behaviors are driven by
emotional,socialandexperientialmotivations,notjustrationalknowledge. Shafiee
et al. (2024) suggests that well-designed, personalized financial tools can increase
financial literacy and support decision-making, while still fulfilling an educational
andadvisoryrole.
While digital PFM tools aim to help users track expenses, manage budgets, and
visualizefinancialdata,theiradoptionremainslimited. Stefanovetal. (2024)found
thatonlyfew availabletools were ableto meetallconsumerneeds foreasierfinancial
management, especially in underrepresented regions. In addition, many tools only
offeroneservicetotheusers,suchasbudgeting,anddonotprovideeducationalcontent
whichwouldhelpraisetrusttofinancialservices(Tornoetal. 2021). Researchhas
shownthataddingpersonalization,gamifiedfeedback,andsimplifiedinteractionscan
improveuserengagementandfinancialself-efficacy(Bitriánetal. 2021; Cederberg
2013),yettheseelementsarestilluncommoninmainstreamapplications.
Thisthesisrespondstotheselimitationsbydesigningacentralizedpersonalfinance
application that consolidates financial data, supports user learning and motivation,
andofferstoolsforfinancialplanningandanalysis.

1.2 Objectives and scope
The goal of this study is to design and build a proof-of-concept of centralized
personalfinanceapplicationthathelpsindividualsmakeinformed,data-drivenfinancial
decisions. FollowingtheDesignScienceResearchMethodology(DSRM),thestudy
aims to identify user needs, create a customized solution, and evaluate its practical
relevanceandfunctionality. Theapplicationwasdevelopedforaprivatestakeholder
withreal-liferequirements.
Inparticular,theapplicationaimstoachieve:
• Consolidationoffinancialdataacrossassetclassesincludingcash,sharesand
realestatefrommultiplesourcesonasingleplatform
• Trackauser’snetworthdevelopmentovertimethroughvisualizeddata
• Provideclearvisualoverviewsoftransactionsandcashflowthroughtablesand
charts
• Improvetransparencyandaccessibilitybystructuringpersonalfinancialdatain
ascalable,easy-to-navigatesystem
• Provide breakdowns of the assets by categories and subcategories including
marketvalue,equity,countryattributionandmore
ThisworkcontributestothedevelopmentofpracticalPFMtoolsbyfocusingondata
integration,visualclarity,andactionableinsights. Italsodemonstratestheapplication
ofDSRM toguide artifactdevelopment anditerationbased onstakeholder’sfeedback
andevaluation.
1.3 Use of artificial intelligence tools
Artificialintelligencetools,includingChatGPT,wereusedtosupportthestructuring
and writing of this thesis. AI assistance was first used to help outline the overall
structureofthethesisanddecidingwhatcontentshouldbeincludedineachchapterand
section. Oncethestructurewasinplace,AIwasusedtohelpdraftsomeparagraphs
basedonpredefinedideas,bulletpoints,andnotes.
In the Literature review (Chapter 2), the process involved first highlighting and
collecting relevant information from selected academic sources. The material was
manuallyorganizedintoclearlydefinedsubsections. AItoolswerethenusedtohelp
compose coherent and logically structured paragraphs, ensuring that the collected
sourceswerepresentedundertheappropriatethemesandheadings.
Additionally, AI was used throughout the thesis to check that statements were
supportedbythecitedliteratureandtorefineclarity,grammar,andacademictone. All
AI-assistedcontentwasreviewed, edited,andfinalizedtoensureaccuracy, integrity,
8

andappropriatenessforacademicwork.
1.4 Thesis structure
This thesis consists of ten chapters. Chapter 1 introduces the research context,
motivation, andobjectives. Chapter2 reviews relevant literatureon financialliteracy,
personal finance planning, management tools, and DSRM. Chapter 3 presents the
research methodology. Chapters 4 to 8 follow the DSRM process: identifying the
problem,definingsolutionobjectives,designinganddevelopingtheproof-of-concept,
demonstratingitsuse,andevaluatingitseffectiveness. Chapter9discussesthebroader
impactoftheresultsandfuturedevelopmentopportunities. Chapter10concludesthe
thesisbysummarizingkeyfindingsandreflectingontheresearchoutcomes.
9

2 Literature review
Thischapterprovidesthetheoreticalbackgroundfortheresearchbyinvestigatingthe
threetopicsrelevanttothedevelopmentofacentralizedpersonalfinanceapplication.
First,itlooksintofinancialliteracyandbehavior,focusinghowknowledge,motivation,
and habits shape financial outcomes. Second, itlooks into personal financial planning
asastructuredprocessaimedatachievingfinancialgoalsthroughbudgeting,saving,
andinvesting. Third, itlooksintocurrentstateofpersonalfinancemanagementtools,
highlighting current capabilities, user needs, and design opportunities. Finally, the
chapterexplainsDesignScienceResearchMethodology(DSRM),tracingitsorigins,
artifacttypes,andstructuredresearchprocess,whichformsthemethodologicalbase
ofthisthesis.
2.1 Financial literacy and behaviors
Financialliteracyisessentialformanagingmoney,makinginformeddecisions,and
achieving long-term financial well-being. Rajesh and Giridhar (2024) argue that
low levels of financial literacy can lead to significant consequences related to the
accumulationofoverallwealth,suchasunsustainablelevelsofdebt,poorcredit,and
possibly even bankruptcy. Many people struggle with financial management, such
as, overspending, making poor investment decisions, borrowing too much money
unnecessarily, and failing to plan for retirement. They note that increased financial
literacyallowsindividualstohavebettersavingandspendingroutines,controltheirdebt
better,andachieveimprovedfinancialstrength. Likewise,LusardiandMitchell(2014)
confirm thatlow levelsof financialliteracyare presentinall populations,particularly
theelderlyandyouth. Theysaythatallpopulationsshowmajorgapsin certainareas,
such as, issues understanding interest rates, inflation, or risk diversification. They
statethathistorically,peoplereliedongovernment-managedpensionsandpaidlittle
attentiontofinancialplanningwhichdoesnotapplytodayanymore. Theauthorspoint
outtheconnectionbetweenfinancialilliteracyandriskierbehaviorssuchaslatebill
paymentsorexcessiveinterestcreditusage. Incontrast,financiallyliterateindividuals
reportmoreplanningforretirementandlong-termwealthaccumulation.
From the behavior side, Atkinson and Messy (2012) note that financial literacy
incorporates attitudes and habits that can lead to financial well-being. Their inter-
national survey concluded that people with better financial knowledge also display
better behaviors including budgeting, saving and timely bill payment. Individuals
exposedtowardlonger-termplanningarealsolikelyto adopthealthierbehaviorsin
theirfinancialpractices. Theresearchdemonstratednotabledemographicfindings:
womenscoredlowerthanmenonboththeknowledgeandbehaviorcomponent,and
middle-agedindividualsgenerallyoutperformedtheyoungerandolderagegroups.
Financialliteracyandeducationwerehighlycorrelated,butlow-incomeindividuals
sometimesshowedresistancetooutsideguidance.
Complementingthesefindings,Kayeetal. (2014)illustratesthatpersonalfinance
10

behavior isnot simply alogicalprocess. Rather, theemotional, culture, andrelational
contexts of how people manage money influences financial behaviors. Instead of
a complete, structured picture of their finances, individuals tend to piece together
financialinsightsthroughmoreinformalpractices,suchasonlyglancingthebalance
in their account or skimming last week’s transactions. This suggests a disconnect
betweenhowfinancialliteracyistypicallysupportedandhowpeopleactuallypreferto
engage with theirfinances. The findings show the importance of designingfinancial
tools that reflect real-life behaviors and habits, and also recognizing that financial
decision-making is deeply shaped by individual context and lived experience (Kaye
etal. 2014).
Motivation is another aspect to note. Di Domenico et al. (2022) apply Self-
Determination Theory framework to reflect on how autonomous, controlled, and
amotivatedmotivationrelatestofinancialknowledgeandoutcomes. Researchdemon-
stratedthatindividualswhoareautonomous,i.e. peoplewhoengagedinfinancialtasks
willingly, showed better financial knowledge, self-efficacy, and well-being. While,
amotivatedindividuals,i.e. peoplelackinginterestorfeeltheycannotmanagetheir
finances,weremorelikelytooverspendandreportedhavinglowerlevelsoffinancial
confidence. Whilebothautonomousandcontrolledmotivationwereshowtocorrelate
withsavingandinvesting,onlyautonomousmotivationhadaclearassociationwith
positivefinancialoutcomesfurthermitigatingtheimportanceofinternalmotivation
andsupportivefinancialbehaviors.
Finally, Lasmiatun (2024) examined how financial education shaped Generation
Z’sfinancialawarenessandhabits. Thestudyfoundthattheunderstandingandability
ofyoungadultstomanagemoney,strategicallyplan,andinvestwashigherforthose
who participatedin thefinancialeducation. Although, theunderstanding offinancial
competencyprimarilycamefrominformallearningonsocialmediaandthingslike
blogs,insteadofformalsources. Lasmiatun(2024)saidthatparticipantsvalueddigital
content that is presented in an interactive and visual format (infographic, videos,
interactive simulations)as they foundthe smallerchunks ofinformation andvisuals
easiertoengagewithandunderstand. Thissuggeststhatimprovingfinancialeducation
forGenerationZmayrequireintegratingmoreaccessible,digitalformatsthatalign
withtheirlearninghabitsandmediaconsumption(Lasmiatun2024).
2.2 Personal financial planning
Personal financial planning is a lifelong process designed to maximize the use of
income and assets, meet financial goals, and reduce uncertainty. Siegel and Yacht
(2009)describethisasanalogoustoplanninginotherareas: knowingwhereyouare,
knowingwhereyouwanttogo,andfiguringouthowtogetthere. Theygoontonote
thattherearemanyinterrelatedvariablesandtheuncertaintyoflifecancomplicatethe
planningprocess. Sincepersonalcircumstancesandtheeconomychangeovertime,
financialplanning has tobe sufficiently flexibleto dealwith change while pursuing
life-longgoals. Financialplanninginvolvescontinuallyreassessinggoals,considering
11

alternativesanddecidingifchangesneedtobemade(SiegelandYacht2009).
In building on this idea, Gitman et al. (2011) note that financial planning is
increasingly important given the context of a world in which we cannot expect
employer or government support to guarantee long-term security. They describe
financial planning as a systematic effort to organize a financial plan for personal
goals/values. Theirfinancialplanningmodelhassixbasicsteps: (1)identifyanddefine
financialgoals (2) develop financialstrategies(3) implementfinancial strategies (4)
createandmaintainbudgets(5)evaluateresultsusingfinancialstatements(6)revise
financialplansduetochangesinpersonalcircumstances,orunexpectedchallenges.
Whilesuccessisnotguaranteed,consistentandflexiblefinancialplanningcanimprove
thelikelihoodofsuccessinachievingfinancialsecurityandadaptingtotheunexpected
(Gitman et al. 2011). Huang (2016) states that financial planning is an important
skillintegratedinto dailylife, regardless ofhow muchfinancial considerationsaffect
peopleintheirdailydecisions, suchascostsbeingaffectedbyinterestrates,increases
inannualtuitionandothers. Thisisespeciallyimportantforyoungpeople,andcollege
graduates, experiencing independence in an expensive world with low income for
thefirsttime. Huang(2016)acknowledgedthatwhilesomepeoplefollowstructured
paths, and others adopt a more reactive method, financial planning is necessary for
eventual success. Similar to Gitman et al. (2011), she also divided the process to
six steps: (1) Identifying Smart Financial Goals, (2) Know Your Current Financial
Situations,(3)SpendingWiselywithaBudget,(4)ManagingtheCredit,(5)Saving
fortheFutureand(6)InvestingtheMoney.
IntheMalaysiancontext,LaiandTan(2009)investigatedhowindividualsengage
withdifferentareasoffinancialplanning. Theresultsindicatedthatwhilebudgeting
and investment planning is relatively well pursued, financial planning across other
areaslikeinsurance,retirement,andestateplanningareoftendisregarded. Specifically,
10%ofrespondentsremarkedthattheyplannedacrossallareasofpersonalfinance.
Despitethis,therearegenerallypositiveattitudestowardbudgetingandmoney,with
the conscious recognition of the importance of investment for long term financial
security. However, there were less positive attitudes towards retirement, as results
indicatedgreaterconsiderationonhealthandlifestylechanges. Inaddition,Laiand
Tan(2009)examinedjobstatusinfinancialplanning. Findingsindicatedthatemployed
andself-employedindividualsengagedinfinancialplanningmorethanthosewithout
stableincome,highlightingthatjobstatushasanimpactonplanningbehaviors.
ShahandBhatt(2014)studiedincomeallocation andinvestmentbehavioramong
residentsofthecityofAhmedabad,inthedistrictofGujarat. Findingsindicatedthat
individualstypicallyallocate45%ofincometoconsumption,saving25%,and15%
toinvestmentsandemergencyfunds,withsavingprioritiesoftheirchildren’sneeds,
housing, and to save taxes. In addition, respondents expressed that their preferred
investmentsarefixeddepositswithbanks,insuranceplans,andpublicprovidentfunds.
Regardinginvestmentbehaviors,malerespondentscertainlyfavoredinvestinginstock
markets,while female respondentstendedtoprefergold, bullion,andPPF investment
12

products respectively. The above trends may reflect a cautious and security based
financial planning behavior focused on meeting long term needs and awareness of
investmentrisk(ShahandBhatt2014).
2.3 Personal finance management tools
Personal finance management (PFM) applications have changed from being paper-
and-pencilorspreadsheet-basedsystems,tobeingadvancedwebormobiletools. As
Gafrikovaetal. (2015)demonstrate,althoughusingtraditionalpaper-and-pencil,or
spreadsheet,methodsoffersmaximizedfreedom,thedownsideisgreatertechnicalskill
andtimecommitment. Gafrikovaetal. (2015)tracedbackthatdedicatedPFMsoftware
started appearing in the 1980’s, and has since progressed into today’s specialized
web and mobile tools, many of which are now integrated into banking systems. A
keymilestonewasthelaunchofMint.comin2007,whichsetaglobalbenchmarkfor
onlinePFMtools. Despitethis,adoptionhasremainedlow. Citinga2012AiteGroup
surveytheyestimate58%ofU.S. consumershaveneverusedanddonotplantouse
PFMapplications, andonly13%of themwantedfinancialconsulting andplanning
from their financial institutions. In Poland, PFM tools embedded within banks are
relativelycommonbutoftenlimitedtointra-bankaccountmanagement,althoughwith
highersecuritystandards.
Stefanov etal. (2024)presented auser-centered designapproach fordevelopinga
mobilePFMappfocusingontheBulgariancontext,wherenoPFMsolutionscurrently
exist. In interviews and survey responses conducted by Stefanov et al. (2024), they
identified practices on how the users wanted to manage their finances: budgeting,
monitoredexpenses,investment planning,andstrategyplanning. Theysay thatmany
existingtoolsfallshortduetooverlycomplexinterfacesorlackofaccessibility. Based
on their analysis, they identified some desired functionalities: portable calculator,
currencyconverter, chartextraction,andbarcodescanning, allbundledontoa single
platform to enhance user experience and effective personal finance management.
The significance of design and usability is also verified by Cederberg (2013), who
researchedthePFMfeaturesyounguserspreferredwhenembeddedinbankingapps.
She conducted user interviews and prototype testing with their target market while
they used the PFM functionalities. Features that the respondents liked included
general income and spending diagrams, category-based pie charts, budget tracking
with monthly limits, alerts for nearing those limits, and visual planning of fixed
expenses. Users identified a desireforeasy-to-use applicationsand preferredminimal
manualinputwithautomatedcategorizationfeatures. Usersalsonotedaestheticswere
importantastheywantedapleasingandrecognizableuserinterface,astheybelieved
these types of tools would help them more effectively manage their finances due to
newinsight,control,andgoalsetting.
Looking atbroader range of tools, Torno et al. (2021) did a taxonomy and cluster
analysis on 170 PFM apps, finding ten separate archetypes. The clusters ranged
fromappsfocusedonfinancialnewsandassetmonitoring,toadvancedandmanual
13

budgetingtools,tofull-featuredmobilebankingplatforms. Mostappsrequiredinternet
accessand useraccountsandgenerally, offlinefunctionality waslimitedtoapps that
haveabasiccalculatorandmanualbudgetingpossibilities. Veryfewappsprovidean
advisoryoreducationalelement intheirservice. Withinthe clusters,examples such
as"InvestingwithAdvice"offerpredictiveanalysisandproductswhileothers(e.g.,
"TransactionAuthorisation")arenarrowerinscope. Despitethewidefunctionality
spectrum, Torno et al. (2021) highlight a lack of educational content across most
apps,suggestingamissedopportunityforfinancialserviceproviderstoimproveuser
engagementandtrustthroughbetterfinancialliteracytools.
Herralaetal. (2023)explorehowPFMsystemscanbothempowerandconstrain
young users, using empathy-based storytelling (MEBS) as a qualitative research
methodwith191universitystudents. Participantshadsignificantpositiveexperiences:
improvedbudgetingability,improvedsavingsandinvestingpractices,andbetteraccess
tolendinganddigitaltransactions,allfactorsthatcontributetopersonalagencyand
long-termplanning. Therewerealsosignificantnegativeexperiences: spontaneous
spending,difficultygraspingthevalueofdigitalmoney,andover-indebtednessdue
to ease of credit. Other concerns included stress regarding privacy, surveillance,
cybersecurity,overloadoninformation,andover-relianceontechnologyanddigital
competence. ThestudyconcludesthatwhilePFMtoolscanpromotefinancialwell-
being, they may also reinforce behavioral control and cognitive overload when not
appropriatelydesignedorsupported.
Gamification might offer a partial way around these problems. Bitrián et al.
(2021) investigate how gamified features promote user motivation by combining
self-determinationtheory(SDT)withthetechnologyacceptancemodel(TAM). They
evaluated 208 Mint app users and conclude that budgeting, alerts, credit score and
tracking opportunities are features that promote competence and autonomy. These
featuresetsencouragedusers’motivationtousetheappandresultedinstrongperceived
usefulness and ease-of-use. Bitrián et al. (2021) suggest independent goal setting,
visualdisplayofprogressandbudgets,realtimenotifications/alerts,andrewardsare
elementsthatappdesignerscanintroducetoimproveuserautonomyandcompetence.
Therecommendedaspectsforboththeappdesignerandusersuggestthepotentialfor
long-termengagementandasenseofempowermentfortheuser.
Incontinuingwithagenerationalperspective,Handayaniet al. (2024)described
fintechadoptionfrom amillennial perspective sincetheygrewupwith technology as
anormalwaytointeractwiththeworld. Theyexaminedmillennialsattitudestoward
technology-basedfinancialservicesanddistributedanonlinesurveyto120usersof
personal finance apps. The authors felt that personal finance apps helped provide
visibilitybyenablinguserstoseetheirincome,expenses,andbalancesinreal-time
thatsupportedtheirabilitytotracktheirspendingbehaviour,settheirgoals,andplan
theirfinances. Theypresentedkeyfeaturesthatwereseenasmotivatingfactorssuch
as automatic expence tracking, bill reminders, and personalized advice. Concerns
aboutdatasecurityandprivacyononlineplatformsdidstillexist. Fintechapplications
14

have become central to millennials’ financial behavior, and their growing usage is
pushingtraditionalfinancialinstitutionstoadaptandintegratesimilartechnologiesto
staycompetitive(Handayanietal. 2024).
Finally,Frenchetal. (2021)evaluatefourPFMappsdevelopedcollaborativelywith
creditunionsand testedvia arandomizedcontrolledtrialwith500membersofDerry
CreditUnioninNorthernIrelandwhere260wereinthetreatmentgroupand240in
thecontrolgroup. Thetreatmentgroupshowedsmall,significantincreasesinfinancial
literacy, ability to budget, confidence to budget, and ability to plan for unexpected
bills. The treatment group did not show significant increases to digital literacy or
behavioural change (i.e., saving money regularly). In terms of use, expectable,
descriptive analysis showed that 45% of users used the apps regularly (5 or more
times),32%usedtheappinfrequently,and23%didnotusetheapp. Forthenon-user
reasonsincludedforgetfulness,relevance,andrestrictiveness. Still,mostusersrated
theappspositively,indicatingstrongpotentialiffuturedesignscanaddressbarriersto
usageandengagement.
Insummary,theeffectivenessofPFMtoolsliesnotonlyintheirtechnicalcapabilities
butalsointheirabilitytosupportuserbehavior,motivation,andemotionalwell-being.
Integratedanduser-friendlytoolsthataddressprivacyconcerns,offerpersonalized
insights, and engage users in meaningful way are most likely to foster long-term
financialstabilityandinclusion.
2.4 Design science research
De Sordi (2021) describes Design Science Research Methodology (DSRM) as an
approachemergedintheearly2000sto provide amorestructured, scientificbasisfor
the development ofinformation systems. Essentially, DSRM aims to solve real-world
problems through designing artifacts in a systematic way. Vaishnavi and Kuechler
(2015) notes that design is more than simply describing and they define design as
purposeful creationofnew artifacts,where anartifactcan takemanyformsandtypes.
Theysaythata designisa routinein asituationwhen you haveenough knowledgeto
createwithouttheneedtodeveloporextendknowledge,versusadesignbeinglabeled
innovative when it manifests any form of new knowledge. They continue that the
subjectofDesignScience(DS)isfocusedontheconceptsandprocessesfollowedto
produceartifactswhichcompriseconstructs,models,methods,andinstantiations. This
thencomprisesthepracticalformsofknowledgeneededtosolveparticularfunctional
needs. Conversely,DesignScienceResearch(DSR)focusesonthescientificstudyof
thedesignprocessincludinganalysis,reflection,abstraction,andevaluation. Vaishnavi
andKuechler(2015)explainthatDSRcontributestoknowledgebyinvestigatingand
documentinghowartifactshaveevolvedthroughDSRIandhowartifactsachievetheir
intendedusefunctionwithincontexts.
De Sordi (2021) also describes the difference between natural science, which
develops knowledge to examine either physical or abstract phenomena that already
15

exist, and artificial science, which develops knowledge based in context to develop
the creation of human artifacts that aim to solve problems for human populations.
AccordingtoDeSordi(2021),onedefiningcharacteristicofartificialscienceisafocus
on attempting to understand the context ofthe artifact, in terms ofthe environment
in which will be used or the individual human characteristics and needs that may
impact the use of the artifact. As referenced by De Sordi (2021, p. 9), “Design
involvesdesigningsomethingthatisasolutiontoaneed,whicharecalledartifacts.”
Artifacts developed using DSRM can take many forms. Vaishnavi and Kuechler
(2015)defineconstructs,astheconceptsandtermstodescribeproblemsandsolutions,
which may actually evolve in the research. Models are organized representation
of the relationships among constructs, which may be useful not perfectly accurate.
Methods are the procedures, algorithms, or techniques used to accomplish desired
ends. Instantiationsareartifactconstructs,models,ormethodsusedinpractice,which
mayoccurpriortotheorybeingformed(VaishnaviandKuechler2015).
Amongthevariousprocessmodelsproposedforconductingdesignscienceresearch,
the most widely adopted is from Peffers et al. (2007), presented in Figure 1. Their
modelwasdevelopedtoaddressthelackofstructureinearlyDSReffortsandhassince
becomeafoundationalframeworkin informationsystemsresearch. Ithasastructured
six-stepprocess: (1)problemidentificationandmotivation,(2)defineobjectivesfora
solution,(3)designanddevelopmentoftheartifact,(4)demonstrationoftheartifact
inuse,(5)evaluationoftheartifact’sperformance,and(6)communicationofresearch
results. This structuredprocesswill form themethodological basisofthis thesis,and
isfurtherexplainedinChapter3.
DesignScienceProcessModel(Peffersetal.,2007,p. 54)
Figure 1:
Inadditiontostructureandguidelines,DSRalsorequiresanunderstandingofwhat
a valid contribution means. According to Hevner et al. (2004), design science in
information systems requires the replication of artifacts that are not only novel and
effective, but also, that have been evaluated objectively in the context of use. The
authors provide a balance to the effective usability versus research methodological
16

rigor by claiming utility as the artifact’s valued contribution. In another words, the
artifact’sreasonablewaytoaddressausableproblem. Thebalancebetweentopical
relevance and rigor of method is one of the strengths of design science research,
andmakesDSRMparticularlyrelevantinappliedcontexts,suchaspersonalfinance
technology.
Inconclusion,DSRMprovideamethodtotheoreticallyshapeapracticalsolutionto
complexproblemsusingiterativeartifactdevelopment. DSRMencouragesincluding
feedbackfromusers,aswellascontextualconstraints,andformalevaluation. These
elementscontributetoappropriatenessofapplyingDSRMtodevelopamoreengaging
centralpersonalfinanceapplication,presentedinthisthesis.
17

| 3 Research | methodology |     |
| ---------- | ----------- | --- |
Thischapterdescribestheresearchmethodologyusedinthisthesis,whichfollowsthe
DesignScience ResearchMethodology(DSRM). Thechapterexplainshoweachof
thesixDSRMphaseshasbeenutilizedwithinthescopeofthisstudy,fromproblem
identification to communicating results. In addition, the last section provides the
justificationforwhyDSRMwasselectedasthemethodologyforthisthesis.
| 3.1 DSRM | actions |     |
| -------- | ------- | --- |
This thesis follows the DSRM proposed by Peffers et al. (2007), which consists of
six structured steps for developing and evaluating innovative artifacts. Each step is
describedindetailbelow.
| 3.1.1 Problem | identification | and motivation |
| ------------- | -------------- | -------------- |
ThefirststepofDSRM,ProblemIdentificationandMotivation,focusesondefininga
research-worthyproblemthatholdsbothacademicsignificanceandpracticalrelevance
(Peffersetal. 2007). AsDeSordi(2021)explains,thisrequiresdirectengagementwith
thefieldtoensurethattheidentifiedchallengereflectsrealuserneedsandcontextual
constraints.
Usability, lack of features, and low demand have all been identified as the most
significant limitations facing personal financial management (PFM). Torno et al.
(2021)discoverthatthemajorityofmobilePFMappsfocusonnarrowtasks,suchas
keepingabudgetorfacilitatingpayments,andrarelyincludeeducationalcontentor
considerincorporatingholisticfinancial planning. Herralaet al. (2023)illustrate that
whilePFM toolscanempowerusersandplacethem incontroloftheirfinanciallives,
theyalsoruntheriskofgeneratinguserstress,impulsivebehaviors,andcreateasense
ofsurveillance.
Tovalidatetheprobleminthisstudy,astructuredquestionnairewasconductedwith
the stakeholder (Table1), using open-endedquestionsto investigate challengesand
featuregaps. TheanalysisofthefinalproblemdefinitionispresentedinChapter4.
Problemidentificationquestionnaire
| Q1: Howdoyoucurrentlymanagepersonalfinances?                 |     |     |
| ------------------------------------------------------------ | --- | --- |
| Q2: Howoftendoyouusethecurrentsolution?                      |     |     |
| Q3: Whatdifferentpurposesdoyouuseitfor?                      |     |     |
| Q4: Whatisthemostchallengingaspectofusingthecurrentsolution? |     |     |
Q5: Arethereanymissingfeaturesorfunctionalitiesyouwishexisted?
| Q6: Howoftendoyouencountererrors,delays,orinconsistencies? |     |     |
| ---------------------------------------------------------- | --- | --- |
| Q7: Howwouldyouratetheuserexperience(UX)andeaseofuse?      |     |     |
Questionsusedintheproblemidentificationquestionnaire
| Table | 1:  |     |
| ----- | --- | --- |
18

3.1.2 Define the objectives for the solution
ThesecondstepofDSRM,DefineObjectivesfortheSolution,involvessettinggoals
that respond directly to the identifiedproblem, whileensuring theyare feasible and
relevant (Peffers etal. 2007). Objectives canbe bothquantitative, suchas measurable
improvements,andqualitative,suchasaddressinguserfrustrationsorunmetneeds. As
De Sordi(2021) notes, this stageincludes assessing the currentstate ofthe problem,
reviewingexistingtools,andidentifyinghowtheproposedartifactcanofferasuitable
solution.
Toformalizethesolutionscope,thesystemrequirementsweredividedintofunctional
andnon-functionalcategories. Functionalrequirementsdefinewhatthesystemshould
do, such as authentication, data processing, and reporting, while non-functional
requirementsspecifyhowthesystemshouldperform,includingitsreliability,security,
and responsiveness (Ironhack 2024). This structure helps ensure the artifact meets
bothusabilityexpectationsandtechnicalstandards.
Tofocusdevelopmentonthemostcriticalfeatures,aprioritizationoftherequire-
ments was conducted with the stakeholder. The MoSCoW method (Brush 2023), a
common approachin Agile development, was adapted to suitthe project context. The
customized scale, shown in Table 2, includes four levels: Must have, Should have,
Nicetohave,andOptional.
Prioritization Description
Musthave Mandatoryinthefinalproduct
Shouldhave Essentialbutnotabsolutelyvital
Nicetohave Usefuladditions,butnotnecessary
Optional Couldbeaddedlater
Customprioritizationscaleforthecontextcase
Table 2:
This customizedranking allowedthe stakeholderto distinguishcore featuresfrom
those better suited for future iterations. Requirements were labeled as functional
requirements(FR)orqualityattributes(QA),andnumberedbypriority,withlower
numbers indicating higher importance. The requirements are presented in detail in
Chapter5.
3.1.3 Design and development
The third step of DSRM, Design and Development, involves specifying the system
architecture and core functionality, followed by the implementation of the artifact
(Peffersetal. 2007). AccordingtoDeSordi(2021),thisphaseisiterativeandincludes
ongoingdevelopmentandevaluationtoensurethattheartifacteffectivelyaddressesthe
definedproblem. Continuousrefinementbasedonstakeholderfeedbackisencouraged
toenhancebothfunctionalityandrelevance.
19

Architecturaldecisionsweremadebased ontheprioritized requirements. Enstrom
(2018)definesArchitecturalDecisions(ADs) assignificant,documentedchoicesthat
influence the system’s structure, including software technologies, data integration,
andmaintainabilitystrategies. Thesedecisionsaredistinctfromroutinedesigndetails
andserve toalignthe system withlong-termgoalsand constraints(Enstrom 2018).
ThekeyADsforthisprojectarepresentedinChapter6.
After defining the architecture, the artifact was developed in iterative cycles.
Feedback from the stakeholder was used to refine features, user workflows, and
interfaceelements. ThisismotivatedfromthefindingsfromliteratureasbothStefanov
etal. (2024)andCederberg(2013)notedtheimportanceofusability,simplifiedand
invitinginterface,andcentralizedfunctionality.
3.1.4 Demonstration
ThefourthstepofDSRM,Demonstration,involvesshowingthatthedevelopedartifact
can solve at least one instance of the identified problem (Peffers et al. 2007). This
may involve experimentation, simulations, case studies, or other forms of proof.
As described by De Sordi (2021), this phase aims to validate whether the artifact’s
structure, procedures, and outputs address the problem in a meaningful way, even
if full performance optimization has not yet been achieved. De Sordi (2021) also
notesthatdemonstrationissometimesincorrectlyreportedasevaluationinacademic
studies,especiallywhentheartifactisstillindevelopment.
Inthisthesis,demonstrationwasusedtoshowhowtheartifactaddresseskeyissues
identified during stakeholder analysis. These included fragmented tools, repetitive
manual updates, and limited trust in the accuracy of financial data. These same
challenges were also noted in the literature. Gafrikova et al. (2015) mentions that
spreadsheet-basedsolutionsrequiretimeandtechnicalskills. Cederberg(2013)found
that usersmight stopusing the tool ifit requirestoo much manualinput, encouraging
automation. Additionally,Herralaetal. (2023)foundthatfinancialtoolsperceivedas
unreliable or difficult to use may increase user stress and undermine their sense of
control.
Thedemonstrationpresentsthefollowingcapabilitiesofthesystem:
• Addressingcomplexityandreducinghumanerror
• Solvingscalabilitylimitations
• Automatingfinancialdataretrieval
• Providingcentralizedtrackingacrossfinancialcategories
• Deliveringintegratedandefficientreporting
20

3.1.5 Evaluation
ThefifthstepofDSRM,Evaluation,assesseshowwelltheartifactsolvestheidentified
problem bycomparing itsintended objectives withthe actual outcomes (Peffers etal.
2007). Thisstepinvolvesanalyzingtheartifact’sperformance,usability,andfunctional
alignmentwithuserneeds. Evaluationisimportantfordeterminingwhethertheartifact
worksasintendedinreality. DeSordi(2021)explainthatthereareartificialevaluations
occurring under isolated or theoretical conditions, and naturalistic evaluations that
occur within real environments, with real users, and real problems. Naturalistic
evaluationsarealignedwiththefundamentalprinciplesofdesignscience,particularly
inapplieddomains.
Inthisstudy,theartifactwasevaluatedusingfourdifferentmethods. First,task-based
usertestingwasconductedtoassessusabilityandalignmentwithexpectedworkflows.
Thestakeholderperformedtypicalusagescenariosindependentlyontheirowndevice
while being observed. This allowed for direct feedback on task completion, design
effectiveness,andinterfaceclarity. ThescenariosarelistedinTable3.
Usertestingtasks
T1: Addanewtransactionforeveryassetcategoryandreviewupdated
networth
T2: Viewandinterpretassetdistributionusingpiechartsandassettables
T3: Add an expense and income and review the updated cash flow
visualization
T4: Generateafinancialreportforthepastthreemonths
Task-basedusertesting
Table 3:
Following the test session, the stakeholder completed a structured evaluation
questionnaire in similar format as in problem identification. The questions were
grouped into four categories: general impressions, feature satisfaction, problem-
solving,andsuggestionsforimprovement(Table4).
21

Evaluationquestionnaire
Generalimpressions
Howintuitivedidyoufindtheapplicationinterface?
Wasiteasytofindandusethekeyfeaturesyouneeded?
Featuresatisfaction
Howsatisfiedareyouwiththeassettrackingfunctionality?
Howsatisfiedareyouwiththecashflowtrackingfunctionality?
Doyoufeelthevisualizations(charts,tables)arehelpfulandinformative?
How useful is the PDF report generation compared to your previous
manualprocess?
Problemsolving
Towhatextenthasthissolutionreducedmanualworkcomparedtoyour
oldsystem?
Doyoufeelthissolutionhelpsyouavoiderrorsorinconsistencies?
Hasyourconfidenceinyourfinancialdataimproved?
Suggestionsandimprovements
Isthereanythingmissingyouwouldexpectinafullsolution?
Whatwouldyouimproveinfutureversions?
Questionsusedintheevaluationquestionnaire
Table 4:
Inadditiontocollectingqualitativefeedback,theevaluationincludedacomparison
with the stakeholder’s baseline system. This helped identify gains in automation,
usability, and reporting quality. Finally, an analytical review was performed by
checking how wellthe implementedsolution satisfiedthe original designobjectives
fromearlierDSRMstages. TheevaluationresultsarepresentedinChapter7.
3.1.6 Communication
ThesixthandfinalstepofDSRM,Communication,focusesonsharingtheresearch
outcomeswithbothacademicandprofessionalaudiences. AccordingtoPeffersetal.
(2007, p.92), “Communicate theproblemand itsimportance, the artifact, itsutility
and novelty, the rigor of its design, and its effectiveness to researchers and other
relevant audiences, such as practicing professionals, when appropriate.” De Sordi
(2021)highlightsthateffectivecommunicationinDSRmustbetailoredtoitsaudience.
Hesaysthatforpractitioners,theemphasisisontheartifact’spurposeandpractical
utility. Forresearchers,thefocusisonpresentingthedesignprocess,structure,and
evaluation outcomes to ensure methodological rigor and reproducibility (De Sordi
2021).
ThisthesisrepresentsthecommunicationphaseoftheDSRMprocess. Itdocuments
all stages of the research, beginning with problem identification and continuing
throughdesign,development,demonstration, andevaluation. Theaimis topresent
the motivation for the work, the rigor of its execution, and its contribution to both
22

researchandpractice. By clearlyarticulatingthemethodology andresults,this thesis
contributestoongoingdiscussionsaboutthedesignofpersonalfinancetoolsandthe
practicalapplicationofDSRMtoreal-worldchallenges.
3.2 Motivation for DSRM
DSRM is well suited for this thesis due to its structured and iterative process for
developingandevaluatingartifactsthataddressreal-worldproblems. Thisstudyaims
tocreate aproof-of-concept(PoC)of personalfinancemanagementapplication that
fulfills a stakeholder’s specific needs by using automation and data integration to
providebetterfinancialinsight. DSRMprovidesanorganizedandsystematicapproach
asan avenueto develop, validate andrefinesuchan artifactensuringits effectiveness
andrelevanceinpractice. ThiswasalsopointedbyTornoetal. (2021)whostatedthat
designscienceresearchisapromisingpracticetodevelopinnovativeITartifacts.
Themethodologyisspecificallyintendedforresearchwherethegoalistoconstruct
and evaluate artifacts that extend existing solutions or introduce new functionality
(Peffers et al. 2007). As Hevner et al. (2004) explains, design science research is
most effective when artifacts are developed in response to clearly defined business
needs and evaluated within real-world contexts. This aligns with the aims of this
thesis,whichaddresseslimitationsincurrentfinancialtrackingtoolssuchasmanual
spreadsheetsthatlackscalability,automation,andintegration. ThroughDSRM,these
limitationscan besystematically addressedusingan iterative development process.
Thesix-phasestructureprovidesatransparentdevelopmentroadmap,makingiteasier
totrackprogressandvalidatedesigndecisions.
DSRMdiffersfrompurelytheoreticalapproachesbyincludingdemonstrationand
practical evaluation. Because this project involves a real stakeholder with specific
financialtrackingneeds,themethodologysupportscontinuousengagementtoensure
thattheresultingsolutionmeetsactualuserexpectations. AsnotedbyDeSordi(2021),
practitioner involvement strengthens both academic rigor and real-world applicability.
Theevaluationphaseallowstheartifacttobeassessedagainstpredefinedobjectives
and revised if necessary. Since the goal of the thesis is to develop a PoC rather
than a production system, DSRM also allows for design flexibility and exploration of
feasibility without requiring full deployment. In particular, the Demonstration phase
enablestargetedtestingofcorefunctionalityinacontrolledsetting,helpingconfirm
thesolution’seffectivenessbeforefurtherdevelopment(Peffersetal. 2007;Hevner
etal. 2004).
23

| 4 Problem |     | identification |     | and motivation |
| --------- | --- | -------------- | --- | -------------- |
This chapterpresents the problemdescription thatthe proof-of-conceptapplication
aims to address. It begins with insights gathered from a structured questionnaire
conducted with the stakeholder, followed by a detailed description of the current
financial management approach and its associated challenges. Finally, the chapter
explainsthemotivationfordevelopinga new solution,based onthelimitations and
problemsidentifiedintheexistingsystem.
| 4.1 Stakeholder |     | insights | from | questionnaire |
| --------------- | --- | -------- | ---- | ------------- |
To gain a deeper understanding of the problem, a structured questionnaire was
conducted with the stakeholder, as introduced in Chapter 3.1.1. Several challenges
werefoundfromthefinancialmanagementapproachbasedontheresponses.
| 4.1.1 Current | financial | management |     | approach |
| ------------- | --------- | ---------- | --- | -------- |
Thestakeholderusesmultiplefinancialtoolstotrackincome,expenses,andinvest-
ments. Theirprocessincludes:
• Tools used: A combination of Spendee (for expense tracking), multiple bank
accountsacrosstwocountries,GoogleSheets(forsharepriceandexchangerate
tracking),andseveralExcelspreadsheetsforrealestateandmortgagetracking.
• Manualdataentry: Financialdataisperiodicallyfetchedfromvarioussources
andconsolidatedintoa“master”Excelfile,inusesince2014.
• Financial reporting: Quarterly and yearly reports are generated manually by
analyzingdataandproducinggraphs.
| 4.1.2 Frequency |     | of use |     |     |
| --------------- | --- | ------ | --- | --- |
Thestakeholderengageswiththefinancialsystematvaryingintervals:
| • Daily:  | TrackingexpensesinSpendee.        |     |     |     |
| --------- | --------------------------------- | --- | --- | --- |
| • Weekly: | UpdatingandmaintainingExcelfiles. |     |     |     |
• Quarterly: Conductingafullfinancialreviewandgeneratingreports.
| 4.1.3 Challenges |     | with the current |     | system |
| ---------------- | --- | ---------------- | --- | ------ |
Thestakeholderidentifiedthefollowingmajorissues:
• Complexityandhumanerror: Thesystemhasbecomedifficulttomaintainand
pronetomistakes.
24

• Scalability limitations: Excel structures struggle to handle growing financial
dataneeds.
• Lack of automation: No integration with online sources and updates must be
donemanually.
• Reportinginefficiencies: Thequarterlyreportprocessistime-consumingand
fragmented.
4.1.4 Desired features for an improved solution
Thestakeholderexpressedtheneedfor:
• Moreautomation: Asystemthattrackskeymetricswithminimalmanualeffort.
• Better data integration: Automatic synchronization with sources like stock
prices,exchangerates,andbanks.
• Acentralizedplatform: Asinglesystemcombiningallfinancialaspects.
• Enhancedaccuracy: Reducedhumanerrorandmorereliabledata.
4.1.5 Stakeholder reflections
Thestakeholdersummarizedtheirconcernsasfollows: "Thewholeprocessisgetting
overly complex, resulting in a higher probability of human error impacting data
quality. Any changes made to the document might break something due to complex
dependenciesacrossdifferentdatatabs."
AlthoughtheyfindExcelsomewhatenjoyableandfamiliar,theyacknowledgethe
system is not user-friendly for others and is increasingly difficult to manage. As
they put it: "For me, it is somewhat of a relaxing experience, but it is starting to
feeloverwhelmingbecauseoftheinaccuraciesandgapsthathindermefromgetting
accuratedata."
4.2 Problem description
Thestakeholderhastrackedincome,expenses,andinvestmentsforoveradecadeusing
acombinationofspreadsheets,financialapplications,andmanualdatacollection. Over
time, this system evolved to support detailed financial analysis, including quarterly
and yearly reporting. However, asfinancial data hasgrown involumeand complexity,
maintainingthesystemhasbecomeincreasinglydifficult.
The current setup involves multiple tools: Spendee for expense tracking, bank
accounts across two countries, and Excel spreadsheets for managing real estate
investments, mortgages, and stock portfolios. These fragmented sources require
25

manualconsolidationintoa“master”Excelfile. Datamustbeperiodicallyfetched,
entered, and processed by hand, resulting in a time-consuming workflow that is
increasingly prone to error due to complex interdependencies across formulas and
sheets.
Themainchallengesoftheexistingsysteminclude:
• Scalabilitylimitations–Excelstrugglestoaccommodatetheincreasingvolume
andcomplexityoffinancialdata.
• High risk of error – Manual updates to stock prices, exchange rates, and
balancesintroduceinconsistenciesandinaccuracies.
• Lackofautomation–Nointegrationwithonlinefinancialdatasourcesrequires
frequentcopy-pasteoperationsandmanualdataentry.
• Inefficient reporting – Quarterly reporting involves multiple manual steps:
collectingdata,updatingformulas,generatingcharts,andcompilingsummaries.
The stakeholder is very sophisticated in their financial management, but as their
system complexity and fragmentation grow, inefficiencies and the risk of error has
increased. As many of the authors note, working with disparate tools or manual
processescreatesusability issues,detersengagement,and leadstoerrorsinfinancial
decision-making (Gafrikova et al. 2015; Torno et al. 2021; Stefanov et al. 2024).
Research also shows that even knowledgeable users cannot maintain their desired
financial behaviours (or make decisions) when the available tools do not simplify
their decision-making or provide timely feedback related to their current financial
goals(AtkinsonandMessy2012;Kayeetal. 2014;Cederberg2013). Thisbehaviour
supports the concepts of integrated ease of use, automation, real-time data, and
supportingfeedbackloopstowardtheestablishmentofhabits,allofwhichwerealso
requested by user participants in the most recent fintech and PFM adoption studies
(Bitriánetal. 2021;Handayanietal. 2024)
4.3 Motivation
Thestakeholder’sdifficultiesrepresentawiderdemandforpersonalfinancetoolsthat
combine automation, accuracy, and usability. Their current system allows them to
trackallaspectsoftheirfinancesingreatdetail,though,itisbecomingmoreandmore
difficultto sustain, as well asrequiring scaling. Thestakeholderhas notconsidered
commercial tools, because the stakeholder believe their needs to be really specific,
they would be unable to find an off-the-shelf product that fulfilled their needs. It is
notedbyStefanovetal. (2024),thattheabsenceoflocalizedtools(e.g. applications
inBulgarian)couldalsoleadtounmetexpectationsforusersincertainregions. Torno
etal. (2021)alsonotethatmostpersonalfinanceapplicationstendtofocusonasingle
function (budgeting versus payments) than being a solution for everything, and as
such,usersoftenneedtoresorttosomeothermethod,forexampleuseofspreadsheets.
26

Besidesmissingfeatures,manyexistingtoolsdonotofferacompletesolutionand
forceuserstomanagetheirfinancesacrossseveralseparateapps. Whileautomation
was recognized as a major priority, the stakeholder also indicated that accuracy
and completeness are critical aspects of their financial data. They said that without
these, they may not justify the expense of moving to another system in the future.
This viewpoint is aligned with Cederberg (2013), who found thatusers would often
abandontoolsthatrequiredexcessivemanualefforteveniftheyprovidedsomelevel
ofautomationortracking.
Animprovedsolutionshouldaddressthefollowingkeyneeds:
• Automatedfinancialdataretrievaltoeliminaterepetitivemanualupdates.
• Centralizedtrackingoffinancialdataacrossmultipleaccountsandinvestment
platforms.
• Integrated analytics and reporting to generate insights with minimal user inter-
vention.
• Enhancedaccuracyandreliabilitytoreducetheriskofcalculationerrors.
The motivation for this research is based on creating a scalable personal finance
systemthatcanimprovedatareliability,reducemanualeffort,andallowindividualsto
makeinformeddecisions. Theseprioritiesmatchtherecommendationsintheliterature
forcreatingtoolsthatnotonlyautomateanddofinancialtasks,butcanmotivateusers,
givefeedback,andsupportthefinancialgoalsoftheuser(Bitriánetal. 2021;Shafiee
et al. 2024). While some studies also mention potential stress or overreliance on
digitalsystems,theynotetheimportanceofuser-centeredandemotionallysupportive
design(Herralaetal. 2023).
27

| 5 Defining | objectives |     | for the | solution |     |     |
| ---------- | ---------- | --- | ------- | -------- | --- | --- |
This chapter defines the objectives of the proposed solution based on the problem
analysis and stakeholder needs presented in Chapter 4. It presents both functional
andnon-functionalrequirementsthatguidethedevelopmentoftheproof-of-concept
application. Theserequirementsarethenprioritizedtoensurethatthemostcritical
featuresareaddressed.
5.1 Requirements
Thefollowingrequirementsareintendedtoresolvethemajorproblemsandmotivations
explainedinChapter4. Theserequirementsreflectuserneedsandincorporatesomeof
bestpracticesinsoftwaredevelopmentandPFMdesign. Therequirementsarerelated
topracticesmentionedintheliteraturewherefragmentedandmanualsystemshave
beenshowntobeinefficientandcreatecognitiveburdenandlowusability(Gafrikova
et al. 2015; Herrala et al. 2023). In contrast, research also highlights that effective
personalfinancetoolsbuildlong-termengagementbyprovidingautomatedfeatures,
availability, ease of use, and tools to create engagement and maintain motivation
| (Bitriánetal. | 2021;Cederberg2013). |     |     |     |     |     |
| ------------- | -------------------- | --- | --- | --- | --- | --- |
The requirements are divided into two main categories: functional and non-
functional. Tables 5 and 6 present a summary of each, including descriptions, user
stories,andacceptancecriteriathatdefinewhentherequirementisconsideredfulfilled.
The functional requirements focus on features that support an understanding
of financial visibility, decision making, and operational efficiency. For example,
dashboards, tags, and reporting features. These features were requested by the
stakeholder, and research also suggests that clear goal-oriented feedback increases
| engagementandpersonaloversight(Shafieeetal. |          |           |     | 2024).     |     |     |
| ------------------------------------------- | -------- | --------- | --- | ---------- | --- | --- |
| Functional                                  | require- | Userstory |     | Acceptance |     |     |
ment
Presentreal-timecap- "As a user, I want to see the Thesystemfetchesup-to-date
italinformation real-time value of all my as- stock prices and displays the
|     |     | sets." |     | real-time | value of all | tracked |
| --- | --- | ------ | --- | --------- | ------------ | ------- |
assets.
User interface(Desk- "Asauser,Iwanttobeableto Theapplicationprovidesare-
topandmobile) add/update/viewmy financial sponsive user interface that
|     |     | data from | mobile and | desk- works    | on both desktop | and |
| --- | --- | --------- | ---------- | -------------- | --------------- | --- |
|     |     | top."     |            | mobiledevices. |                 |     |
Datavisualizationof "Asauser,Iwanttoseehow Theapplicationdisplaysinter-
capitalandstatistics myassetsaregrowinginaway active visualizations, such as
|     |     | that supports        | me in | making charts              | and tables, represent- |     |
| --- | --- | -------------------- | ----- | -------------------------- | ---------------------- | --- |
|     |     | financialdecisions." |       | ingassetgrowthandfinancial |                        |     |
trends.
28

| Functional | require- | Userstory |     | Acceptance |     |     |
| ---------- | -------- | --------- | --- | ---------- | --- | --- |
ment
Manualfinancialdata "As a user, I want to be able Userscanmanuallyinputand
| input |     | toadd/modify/deleteincome, |     | managefinancialrecordsand |     |     |
| ----- | --- | -------------------------- | --- | ------------------------- | --- | --- |
expenses,anddifferentassets importdataviasupportedfile
|     |     | throughthe | application | orim- formats. |     |     |
| --- | --- | ---------- | ----------- | -------------- | --- | --- |
portthemfromafile."
Automaticdatafetch- "Asauser,Iwantmyincome, Thesystemintegrateswithex-
| ing |     | expenses,     | transactions, | and ternalAPIs                        | orservicesto | au- |
| --- | --- | ------------- | ------------- | ------------------------------------- | ------------ | --- |
|     |     | different     | assets to be  | fetched tomaticallyretrieveuserfinan- |              |     |
|     |     | automatically | from          | the bank cialdata.                    |              |     |
andbrokersthatIuse."
| Tagging |     | "Asauser,Iwanttobeableto    |     | Users can   | assign, edit, | and |
| ------- | --- | --------------------------- | --- | ----------- | ------------- | --- |
|         |     | dividemyassetsintodifferent |     | view custom | categories    | and |
categoriesandsubcategories." subcategoriesforeachasset.
Financialreportgen- "As a user, I want to receive Users can generate and view
eration on-demand financial reports downloadablereportssumma-
|     |     | (weekly/monthly) | summariz-         | rizing key                  | financial | metrics |
| --- | --- | ---------------- | ----------------- | --------------------------- | --------- | ------- |
|     |     | ing my           | income, expenses, | and overaselectedtimerange. |           |         |
assetgrowth."
Customizable dash- "Asauser,Iwanttocustomize Users can add, remove, and
| boards |     | thewidgetsonmydashboard |     | rearrange | dashboard elements |     |
| ------ | --- | ----------------------- | --- | --------- | ------------------ | --- |
tosuitmyfinancialgoals" suchascharts,summaries,and
alerts.
Choosecurrency "Asauser,Iwanttobeableto Users can select a preferred
choosethecurrencyIwantto displaycurrency,andthesys-
|     |     | usefordatavisualizationand |     | tem automatically | converts         |     |
| --- | --- | -------------------------- | --- | ----------------- | ---------------- | --- |
|     |     | analytics."                |     | values using      | current exchange |     |
rates.
Functionalrequirements
Table 5:
The non-functional requirements address factors such as trust, reliability, and
responsivenesswhichareimportantfactorsforuseradoptionandcontinuedengagement.
Herralaetal. (2023)notedthattechnicalissues,usererrorsandconcernsaboutdata
security resulted in increased stress and lowerrates of userengagement. Handayani et
al. (2024)identifiedprivacyandinformationsecurityasmajorconcernsformillennial
users.
29

| Category | Non-Functional | Userstory |     | Acceptance |     |
| -------- | -------------- | --------- | --- | ---------- | --- |
requirement
Dataprotection Preventunau- “Asauser, Iwant Alluserdataisiso-
andsecurity thorizedparties mypersonaldata latedandaccessible
|     | from accessing | tobesafeandnot  |             | onlytotheauthenti-  |          |
| --- | -------------- | --------------- | ----------- | ------------------- | -------- |
|     | data.          | getintothewrong |             | cateduser.          | External |
|     |                | hands.”         |             | accessisrestricted  |          |
|     |                | “Asan           | application | viasecureauthenti-  |          |
|     |                | owner,          | Iwantto     | cationandauthoriza- |          |
|     |                | protectcustomer |             | tionmechanisms.     |          |
andbusinessdata
from unauthorized
access.”
Reliability Thestatistics “Asauser, Ineedto Thesystem produces
|     | providedbythe  | trustthecalculation |     | correctfinancial |     |
| --- | -------------- | ------------------- | --- | ---------------- | --- |
|     | systemshouldbe | andanalyticsgiven   |     | analyticswithan  |     |
|     | correct.       | bythesystem.”       |     | accuracyrateofat |     |
least99.99%when
validatedagainst
sampledata.
| Performance | Goodresponse | “Asauser,         | Iwant  | 95%ofuserrequests  |     |
| ----------- | ------------ | ----------------- | ------ | ------------------ | --- |
|             | time         | thesystem         | topro- | areprocessedwithin |     |
|             |              | cessmyactions,    |        | 1secondundernor-   |     |
|             |              | suchasupdating    |        | maloperatingcondi- |     |
|             |              | assetsandfetching |        | tions.             |     |
reports,quickly.”
Non-Functionalrequirements
Table 6:
5.2 Prioritized objectives
Aftertherequirementsfortheproof-of-conceptapplicationweredefined,theywere
prioritizedtogetherwiththestakeholder,asdescribedinSection3.1.2. Theprioritized
listis presentedin Table 7, includinga short description, associatedgoal, andpriority
levelforeachrequirement.
| Label | Description | Goal |     |     | Priority |
| ----- | ----------- | ---- | --- | --- | -------- |
FR-01 Userinterface(Desktop Ensuretheapplication hasa Musthave
|     | andmobile) | responsiveandintuitiveinter- |     |     |     |
| --- | ---------- | ---------------------------- | --- | --- | --- |
faceusableacrossdevices.
FR-02 Datavisualization of Provideinteractiveandclear Musthave
|     | capitalandstatistics | visualizationstohelpusers |     |     |     |
| --- | -------------------- | ------------------------- | --- | --- | --- |
analyzefinancialperfor-
mance.
30

| Label | Description |     | Goal                    | Priority |
| ----- | ----------- | --- | ----------------------- | -------- |
| FR-03 | Tagging     |     | Allowuserstoorganizefi- | Musthave |
nancialdatausingcustom
categoriesandtags.
| QA-01 | Thestatisticsprovided |        | Ensurethatallsystem-    | Musthave |
| ----- | --------------------- | ------ | ----------------------- | -------- |
|       | bythesystem           | mustbe | generatedstatisticsand  |          |
|       | correct               |        | analyticsareaccurateand |          |
reliable.
FR-04 Presentreal-timecapital Displayup-to-datevaluesof Shouldhave
|     | information |     | alluserassetsusingreal-time |     |
| --- | ----------- | --- | --------------------------- | --- |
datasources.
FR-05 Financialreportgenera- Generatereportsthatsum- Shouldhave
|     | tion |     | marizefinancialmetricsfor |     |
| --- | ---- | --- | ------------------------- | --- |
selectedperiods.
QA-02 Preventunauthorized Securealluserdataandpre- Shouldhave
|     | partiesfrom | accessing | ventunauthorizedaccess |     |
| --- | ----------- | --------- | ---------------------- | --- |
|     | data        |           | throughauthentication  | and |
encryption.
FR-06 Automaticdatafetching IntegratewithfinancialAPIs Nicetohave
|     |     |     | toimporttransaction | and |
| --- | --- | --- | ------------------- | --- |
assetdataautomatically.
| FR-07 | Choosecurrency |     | Allowuserstochoosetheir | Nicetohave |
| ----- | -------------- | --- | ----------------------- | ---------- |
preferreddisplaycurrency
andapplyreal-timeconver-
sion.
| FR-08 | Customizabledash- |     | Letuserstailortheirdash- | Nicetohave |
| ----- | ----------------- | --- | ------------------------ | ---------- |
|       | boards            |     | boardswithwidgetsforper- |            |
sonalizedfinancialtracking.
| FR-09 | Manualfinancialdata |     | Supportmanualentryfor     | Optional |
| ----- | ------------------- | --- | ------------------------- | -------- |
|       | input               |     | transactionsandassetswhen |          |
automationisunavailable.
| QA-03 | Goodresponsetime |     | Ensurefastandresponsive | Optional |
| ----- | ---------------- | --- | ----------------------- | -------- |
interactionforcommonuser
actions.
|     |     | Table 7: Prioritizedrequirements |     |     |
| --- | --- | -------------------------------- | --- | --- |
31

| 6 Design | and development |     |     |
| -------- | --------------- | --- | --- |
The chapter provides the technical basis for the proof-of-concept application. The
chapter presents the major design decisions, system architecture, and implementa-
tion details that were used to meet the functional and non-functional requirements
described in the previous chapter. The focus was on designing a modular, scalable
and maintainable system that met stakeholder requirements while facilitating rapid
developmentunderthescopeofaPoC.
6.1 Architectural decisions
Based on the prioritized functional requirements (FR) and quality attributes (QA)
presented in Chapter 5, key architectural decisions were made to support the most
criticalgoalsforthesystem. Thefocuswasplacedonaddressingthe“Musthave”and
“Shouldhave”requirements. Sincethisisaproof-of-concept(PoC)application,the
architectureisintentionallysimplifiedtofocusfeasibility,corefunctionality,andrapid
developmentwhileminimizingunnecessarycomplexity. Thearchitecturaldecisions
arepresentedinTable8,alongwiththeirjustificationsandcorrespondingrequirement
links.
Thetechnicaldesignreflectsbothstakeholderneedsandrecommendationsfromthe
literature onPFM tools. Previous studiesindicated the importance of centralization
andmodularityforfacilitatingsustainedusageandcontinuedengagement(Gafrikova
et al. 2015; Torno et al. 2021). Similarly, usability and reliability were important
factors. Cederberg(2013)notedtheneedforanintuitiveuserinterfaceandautomated
categorization to minimize user effort, while Herrala et al. (2023) recognized that
technical complexity and user error may lead to stress and lower user trust. The
decision to create a cross platform UI, and modular back end is meant to promote
flexibilityandscalability. Additionally,featureslikevisualanalyticsandautomation
werechosenbasedonfindingsthattheyenhanceusermotivationandpromoteclearer
| financialunderstanding(Shafieeetal. | 2024;Cederberg2013). |               |             |
| ----------------------------------- | -------------------- | ------------- | ----------- |
| Short                               | Decision             | Justification | Requirement |
description
| User      | -UseFlutterfora     | -FlutterallowsquickUI   | FR-01 |
| --------- | ------------------- | ----------------------- | ----- |
| interface | cross-platformUI    | iterationwithasingle    |       |
|           | (mobileanddesktop). | codebase.               |       |
|           | -Implementabasic    | -ResponsiveUIensures    |       |
|           | responsiveUI.       | usabilityacrossdevices. |       |
32

| Short       | Decision             | Justification           | Requirement |
| ----------- | -------------------- | ----------------------- | ----------- |
| description |                      |                         | Link        |
| Backend     | -UseASP.NETCore      | -ASP.NETCoreis          | FR-01,      |
| services    | WebAPIforbackend     | performant,scalable,and | QA-02       |
|             | logic(C#).           | alignswithdeveloper     |             |
|             | -ImplementRESTful    | expertise.              |             |
|             | APIfordataflow.      | -UsingMongoDB.Driver    |             |
|             | -UseMongoDB.Driver   | ensurescompatibilityand |             |
|             | fordataaccess.       | flexibilitywith         |             |
|             | -Separatefrontendand | MongoDBdatamodels.      |             |
|             | backendintomodular   | -Modulararchitecture    |             |
|             | components.          | supportsmaintainability |             |
andfuturescaling.
| Database | -UseMongoDBfor        | -Flexibleschemaallows | FR-03, |
| -------- | --------------------- | --------------------- | ------ |
|          | storingfinancialdata, | adaptingtoevolving    | FR-06, |
|          | tags,andtransactions. | financialdata.        | QA-01  |
-Definecollectionsfor
structureddatastorage.
| Datavisual- | -Usechartlibrariesand  | -Chartsandtableshelp  | FR-02 |
| ----------- | ---------------------- | --------------------- | ----- |
| ization     | builtintablesinFlutter | usersanalyzefinancial |       |
|             | forfinancialdata       | trendseffectively.    |       |
visualization.
| Automatic    | -UseGoogleSheetAPI  | -GoogleSheet        | FR-04, |
| ------------ | ------------------- | ------------------- | ------ |
| datafetching | tofetchshareprices. | integrationensures  | FR-06  |
|              | -Implementscheduled | real-timefinancial  |        |
|              | jobstofetchandstore | updateswithnocosts. |        |
|              | data.               | -Scheduledjobs      |        |
automatedataretrieval.
| Multi-   | -Storeallfinancialdata | -Storingdatainabase      | FR-07 |
| -------- | ---------------------- | ------------------------ | ----- |
| currency | inabasecurrency(e.g.,  | currencyavoids           |       |
| support  | USD/EUR).              | unnecessaryconversions.  |       |
|          | -Fetchexchangerates    | -Dynamicconversion       |       |
|          | fromHexaRateAPI.       | providesuserflexibility. |       |
Customizable -Storedashboardlayouts -JSONstorageenables FR-08
| dashboards | inMongoDBasJSON | flexibleUIcustomization. |     |
| ---------- | --------------- | ------------------------ | --- |
|            | documents.      | -Drag-and-DropUI         |     |
|            | -UseFlutter’s   | enhancesusability.       |     |
Drag-and-DropWidgets.
| Manual    | -Usedifferentformsto  | -Enableseasydatainput | FR-09 |
| --------- | --------------------- | --------------------- | ----- |
| financial | inputdifferent        | whenintegrationsmight |       |
| datainput | transactionsmanually. | notbeavailable.       |       |
|           | -Maketableseditable.  | -CSVimportreduces     |       |
|           | -SupportCSVimports.   | manualworkloadforbulk |       |
dataentry.
33

| Short       | Decision               | Justification           | Requirement |
| ----------- | ---------------------- | ----------------------- | ----------- |
| description |                        |                         | Link        |
| Performance | -OptimizeAPIandDB      | -Reducesresponsetimes   | QA-03       |
| optimiza-   | querieswithindexingand | andimprovesscalability. |             |
| tion        | caching.               |                         |             |
-UseprovidersinUIand
onlycallAPIwhen
somethingisupdated.
Architecturaldecisionsandtheirlinkagetorequirements
| Table      | 8:           |     |     |
| ---------- | ------------ | --- | --- |
| 6.2 System | architecture |     |     |
Thehigh-levelsystemarchitectureisshowninFigure2. Thesystemconsistsofthree
core components aligned with the architectural decisions discussed in the previous
section: theuserinterface,thebackendAPI,andthedatastoragelayer. Additionally
thetwointegrationsarepresentedinthepicture: stockpricesandexchangerates.
The user interface is developed using Flutter and Dart to support cross-platform
deployment across mobile and web platforms. It handles user interactions, such as
addingoreditingtransactions,andvisualizesfinancialdatathroughinteractivecharts
andtables. WhileWinUIwasinitiallyconsideredforthefrontend,itwaseventually
letgoduetoitslimitedvisualizationcapabilitiesanditsrestrictiontotheWindows
desktopenvironment.
Figure 2: High-levelsystemarchitecturediagram
The backend API is implemented in C# using the .NET framework. It contains
the core business logic of the application, including transaction handling (shares,
34

cash,andrealestate),statisticalcomputations,andcommunicationwithexternaldata
sources. TheAPIisalsoresponsibleforallinteractionswiththedatabase,including
datastorage,updates, andretrieval. Whilethisdesign doesnotscalefarinproduction
environment where there is more traffic, the code is structured in a way that would
allowseparationtomicroserviceslateron.
MongoDBisusedastheNoSQLdatabaseduetoitsflexibilityinmanagingdiverse
financialdata. Itstoresallthedatamodels,includingtransactions,assetdetails(shares,
realestate,andcash),cashflow(incomeandexpenses),anddailynetworthsnapshots.
To enrich the application with current market data, two external integrations are
included. Forstockprices,thesystemusesaGoogleSheetsintegrationpoweredby
GoogleFinance. Real-time prices areretrieved viatheGoogle SheetsAPIbased on
tickersymbols,withdatarefreshedeachtimetheapplicationisopenedormodified.
Althoughthissolutionrequiressomemanualsetupbyusers,itwasselectedduetothe
highcostandlimitedavailabilityofcommercialstockAPIs.
CurrencyexchangeratesarefetchedfromtheHexaRateAPI. Toimproveefficiency,
exchangeratesareretrievedonceperdayandcachedinthedatabaseforreuse,ensuring
up-to-dateconversiondatawithminimalexternalrequests.
6.3 Implementation details
6.3.1 Data model and domain objects
Theapplication’sdatamodelisdesignedtoreflectthefinancialdomainandsupport
corefunctionalitiessuchasassettracking,incomeandexpensemonitoring,andnet
worthcalculation. ANoSQL,document-basedapproachisused,witheachdomain
objectstoredinaseparateMongoDBcollection. Themaincollectionsandtheirroles
aredescribedbelow:
• ShareTransaction, CashTransaction, RealEstateTransaction: These collec-
tionsstorerawtransactiondataenteredbyusers. Eachrecordincludesmetadata
such as transaction date, amount, and relevant domain-specific fields such as
purchasepriceorloanamountforrealestate. Thesetransactionsformthebase
forcalculatingassetvalues.
• Share,Cash, RealEstate:Thesecollections representtheuser’s current asset
state. Theyarecomputeddynamicallyfromtransactionhistory. Forexample,
the collection aggregates holdings per ticker symbol, calculating total
Share
quantityandcurrentmarketvalue.
• CashFlowTransaction: This collection tracks income and expense activity.
Eachentryincludesthetransactiontype(incomeorexpense),category,amount,
currency,andoptionalnotes. Thisenablesbudgettracking,categorybreakdowns,
andmonthlyexpensesummaries.
35

• NetWorthSnapShot:Thiscollectionstoresdailysnapshotsoftheuser’stotal
networth. Wheneverassetsaremodified,forexample,throughaneworupdated
transaction,thesystemeithercreatesorupdatesthesnapshotforthatdate. These
recordssupporthistoricalnetworthtrackingandtrendvisualization.
• ExchangeRate: Thiscollectionstoresdailycurrencyexchangeratesretrieved
fromtheHexaRateAPI. Ratesarefetchedonceperdayandcachedtoreduce
external requests. All financial data are normalized to a base currency (e.g.,
EURorUSD)usingthesestoredrates.
Thismodulardatamodelsupportsaflexibleandextensiblearchitecture,enabling
newfeaturestobeaddedwithminimaldisruptiontoexistingcomponents. Thebackend
API follows a structured design pattern in which each domain feature is managed
through a dedicated – pair, promoting a clear separation between
Controller Logic
requesthandlingandbusinesslogic. Thispatternalsoenablespossiblelaterseparation
totheirownmicroservicestoincreasescalability.
6.3.2 User interface structure and design approach
TheuserinterfaceisimplementedinFlutterusingamodular,screen-basedarchitecture.
Each primary functionality, such as the dashboard, asset management, transaction
input, and cash flow tracking, is encapsulated in a dedicated screen. These screens
are composed of reusable UI components, including editable tables, input forms,
pie charts, and bar graphs. All components are located in the folder and
widgets/
accessapplicationdatathroughstatemanagementprovidedbythe package.
provider
Theinterfaceupdatesreactivelyinresponsetochangesintheunderlyingdatalayer,
ensuringsynchronizationbetweenthedatamodelandtherenderedviews.
Financial visualizations are built using the fl_chart library, supporting different
diagramssuchasline,bar,andpiecharts. Theseprovideuserswithimmediatevisual
feedbackonfinancialdistributionsandtrends. AsnotedbyBitriánetal. (2021),visual
progress indicators and dashboards can improve user motivation and purposefulness.
To support responsive layouts, Flutter’s layout tools, such as , ,
Expanded Flexible
and , are used alongside maximum width constraints to optimize the
LayoutBuilder
interface for large screens. While the current design primarily targets desktop and
webresolutions,theuseofFlutterenablesfuturemobilesupportwithminimalcode
changes.
TheUI designfocuses clarityandease ofdataentry. Structuredformsareprovided
for each transaction type, and editable tables enable efficient bulk modifications.
Usabilityand dataintegrityarefurtherimproved throughfeatures suchas real-time
form validation, dropdown menus, and multi-select checkboxes. This emphasis on
visual feedback and structured input aligns with design recommendations for PFM
tools,whichstressthatreducingmanualeffortandsimplifyinginteractionsencourages
continuedengagementandreducesuserstress. Cederberg(2013)highlightsthatyoung
36

usersvaluetoolsthathaveinvitinginterface,automatedcategorization,andminimized
inputcomplexity,whileHerralaetal. (2023)cautionthatsystemsperceivedasdifficult
orunreliablecanincreasecognitiveloadandunderminetrust.
6.3.3 Development tools and process
ArangeofmoderntoolswereutilizedduringthePoCdevelopment. Backendservices
weredevelopedusingMicrosoftVisualStudioCommunity2022,whiletheFlutter-
basedfrontendwasimplementedinVisualStudioCode. MongoDBCompasswasused
to inspect and manage database documents during development. Version control was
handledusingGit,enablingstructuredbranching,changetracking,andsafeiteration.
GenerativeAItoolswereusedtosupportthedevelopmentprocessbyassistingwith
code scaffolding, debugging suggestions, and exploration of architectural patterns.
These tools were particularly helpful in accelerating UI layout design in Flutter,
formulatingMongoDBqueries,andstructuringbackendlogicin.NET. However,their
rolewasstrictlysupportive: allcodewasmanuallyreviewed,adapted,andintegrated
tomeettheproject’sspecificrequirements.
An iterative development approach was followed, including regular feedback from
thestakeholder. Thefunctionalitywasimplementedinmodularunits. Forexample,
share management and its related transactions were treated as a single feature set.
Each feature typically followed a consistent workflow: beginning with UI design,
followedbydatacontractdefinition,backendlogicandAPIendpointcreation,database
integration, and finally frontend-backend connection. After each feature reached a
workingstate,timewasallocatedforrefactoringandfine-tuningbeforeproceedingto
thenextsetoffeatures. Thisincrementalapproachsupportedrapidprototypingwhile
allowing flexibilityto respondto evolving requirementsthroughout thedevelopment
phase. Iterative developmentwith stakeholderfeedback is also recommendedin DSR
literature. Hevner et al. (2004) stated that iteration and implementation are central
piecestothisresearchasitincreasesthequalityoftheendproductandhelpsaddress
problemsalongtheway.
37

7 Demonstration
This chapterdescribes apractical demonstration ofthe proof-of-conceptapplication.
The goal is to demonstrate how the implemented system solves the main problems
inthestakeholder’sfinancialmanagementprocess. Thedemonstrationwillfollowa
structureofthemostimportantissuesandhowtheproposedsolutionaddressesthese.
7.1 Addressing complexity and human error
A major challenge with the stakeholder’s current system is its complexity and vul-
nerability to human error, caused by the use of multiple spreadsheets and manual
calculations across various financial sources. The PoC application mitigates these
issuesbyconsolidatingallfinancialdataintoasingle,structuredbackendsupported
bywell-definedlogicandcalculations.
Eachfinancialdomain(shares,cash,andrealestate)ishandledbyadedicatedlogic
class in the backend, following a consistent – design pattern. This
Controller Logic
separationensuresthateachlogicclassisresponsiblefordomain-specificoperations
suchasassetaggregation,transactionhandling,andprofitcalculation. Forexample,
the class compiles a user’s holdings based on transaction history and
ShareLogic
computeskeymetrics,including:
• Totalinvestedamount
• Currentmarketvalue(basedonthelatestprices)
• Profitorlossinabsoluteterms
• Profitorlossasapercentage
Thesecalculationsareperformedautomaticallyontheserverside,usingtheuser’s
basecurrencyandup-to-dateexchangeratesandshareprices. Theresultsarereturned
tothefrontendaspartoftheassetmodel,eliminatingtheneedforspreadsheet-based
formulas or manual input. Similar logic applies to cash and real estate assets, with
realestatecomputationstakingintoaccountthepurchasepriceandloanamount.
By encapsulatingbusiness logic in code, the system delivers consistentand reliable
results,significantlyreducingtheriskoferrorscausedbyuserinput,brokenformulas,
or accidental modifications. Centralized logic also simplifies future updates as any
changetocalculationrules,suchasprofitformulasorexchangeratehandling,canbe
appliedsystem-widefromasinglesource.
The frontend presents these results visually and interactively. On the
Dashboard
page, shares are displayed in a doughnut chart (Figure 3), while the
Assets and
pageshowsdetailedassetdataineditabletables(Figure4).
Transactions
38

User’ssharespresentedinaninteractivedoughnutchart
Figure 3:
User’sassetspresentedineditabletableswithsummarystatistics
Figure 4:
39

Automatingcomplexcalculationsandreducingmanualworkflowsincreasesease
ofuse. This isconsistentwithresearchthatsuggests usersaremorelikelytoengage
withsystemswithloweffortandclearfeedback. Cederberg(2013)foundthatyoung
users preferred financial tools that required less manual input, included automated
categorization,andimprovedvisualclaritywhichfurtherempoweredthemtomanage
theirfinancesbetterandencouragedcontinueduse. Likewise,Herralaetal. (2023)
identified that by makingfinancial tasks easier to complete, user stress was reduced,
andsenseofcontrolincreased.
7.2 Solving scalability limitations
The stakeholder’s previous system, based on Excel spreadsheets, had scalability
limitations as the financial data volume increased. Over time, the growing number
of transactions, investment types, and calculated fields made the system fragile
and difficult to scale. Complex dependencies between formulas and worksheets
created a risk where even minor changes could disrupt the entire setup. The PoC
applicationaddressesthesechallengesthroughaservice-orientedarchitectureanda
document-baseddatabasemodel.
FinancialdataisstoredinMongoDBcollections,whichareconvenientforevolving
data structures. This enables thesystem to handleincreasing volumes oftransactions
andassetswithoutrequiringstrictschemasormanualreconfiguration. Thebackend
is implemented as a stateless ASP.NET Core Web API, which supports horizontal
scalability. WhilethisPoCis notintendedforproductiondeployment,the underlying
architectureallowsforfuturecontainerizationandcloud-basedscaling.
ThePoC hasremovedthe traditionallimitationsofExcel,suchasworksheetsize,
formuladepth,and fragilecross-sheetdependenciesgivinga basisforscalabilityover
time, data reliability, and consistent performance, as the financial data grows. In
additiontogreaterdatavolumes,theapplicationsupportsmorecomplexdatamodels
that are more structured, more object-oriented than traditional spreadsheets. This
could include things like real estate records that could have fields for loan amount,
terms of mortgage payments, and all of the payment history, or share transactions
that could track dividends, market pricing, and country attribution. It is difficult to
modelthelevelofdetailinExcelandtomaintainitsreliability. Thislimitationisalso
observedinstudiesofPFMtools,wheretraditionalsystemsrelyingonmanualentry
andstaticformatsoftenstruggletosupportgrowingdataneedsandcomplexfinancial
contexts(Gafrikovaetal. 2015).
Oneexampleofimprovedscalabilityistheautomatednetworthtrackingfeature.
Previously, thestakeholder manuallygathered assetvalues fromvarious sourcesand
combined them to update a dataset for visualization. In contrast, the PoC system
calculatesnetworthautomaticallywheneveranyassetismodifiedandcanalsogenerate
historicalvaluesretrospectively(seeFigure5).
40

User’snetworthovertime
Figure 5:
7.3 Automating financial data retrieval
One of the key goals identified during the problem definition phase was to reduce
the manualeffortrequired toupdate financialdata, especiallystock prices, exchange
rates,andaccountbalances. Whilefullautomationremainsachallengeduetolimited
access to bank and broker APIs, the current solution introduces partial automation
thatmeaningfullyreducestheuser’sworkload.
StockpricesareautomaticallyretrievedthroughaGoogleSheetsintegration,where
thesheetispoweredbythe function(SeeFigure6). Theapplication
GOOGLEFINANCE
connects to this sheet through the Google Sheets API and fetches up-to-date prices
foralltickerslistedbytheuser. Althoughusersmuststillmaintainthistickerlistand
entersharetransactionsmanually,thesolutionremovestheneedtorepeatedlycopy
databetweenExcelfiles.
41

GoogleSheetwiththeuser’sstocktickerspoweredbythe
Figure 6: GOOGLEFINANCE
function
ExchangeratesareretrieveddailyusingtheHexaRateAPIandstoredinthedatabase
forreuse. Thisensuresthatallfinancialdataregardlessoforiginalcurrencyisconverted
consistentlywithoutrequiringtheusertolookuporinputratesmanually.
Whileincomeandexpensedataarestillenteredmanuallythroughtheapplication’s
user interface, the system centralizes this information for easier tracking. In the
stakeholder’spreviousworkflow,expenseandincomedatawereenteredintoSpendee,
exported,andthenincorporatedintoafinancialreportandmasterExcelfile. Incontrast,
thenewsystemdecreasesredundancyandimprovesconsistencybymaintainingall
datainacentralizedplatform. Thisremovestheneedtoupdateratesandpricesacross
multipletabsandformulas.
Future iterations may include integration with Open Banking APIs or broker-
42

specificservices,if reliableandcost-effectiveoptionsbecomeavailable. Thecurrent
solutionoffersapracticalbalancebetweenautomation,dataaccuracy,andusercontrol.
Achievingevenpartialautomationhashelpedreducefrictionforusersandcreatea
levelofconsistency. ThisalignswithfindingsbyCederberg(2013),whonotedthat
usersweremorelikelytoadoptPFMtoolswhenfeaturessuchastransactiontracking
andvisualsummarieswereautomated,reducingmanualinputandcognitiveeffort.
However,aspointedbyKayeetal. (2014),someusersmaybecomefrustratedwith
toomuchautomation,suchasinflexibleorinaccurateexpensecategorization,which
can hinder trust or usability. This supports the rationale for retaining user control
alongside automation, ensuring the system remains both efficient and adaptable to
individualpreferences.
7.4 Centralized tracking across categories
Theapplication providesstructuredand centralizedtrackingoffinancial dataacross
assetandcashflowcategories. Assets,includingshares,cash,andrealestate,arestored
indedicatedcollectionsandgroupedusingrelevantidentifierstosupportorganized
analysis.
Shares are enriched with metadata such as category (e.g., dividend, growth),
subcategory(e.g.,REIT,BDC),andcountryoforigin. Theseadditionalfieldsenable
detailedbreakdownsandarevisualizedthroughmulti-layeredpiecharts,asshownin
Figure7.
Sharedistributionvisualizedbycategory,country,andsubcategory
Figure 7:
Cash assets are grouped by account name (e.g., savings or investment account),
whilerealestateholdingsarecategorizedbypropertyname. Thishelpsuserstrack
thevalueandperformanceofeachassetindividually,withoutmixingdifferenttypes
offinancestogether(SeeFigure8).
43

Otherassetdistributionvisualizedbycategory,country,andsubcategory
Figure 8:
Additionally, the application tracks income and expenses under the cash flow
module. Transactionsaretaggedwithlabelssuchasfood,salary,orshopping,enabling
categorized insights. As shown in Figure 9, cash flow data is presented through
categorizedpiecharts,achronologicaltransactiontimeline,andabarchartcomparing
monthlyincomeandexpenses.
44

Cash flow tracking: categorized income and expenses with monthly
Figure 9:
comparison
Thesystemprovidestheuserwithinsightsthatwerepreviouslyfragmentedthrough-
out different tools and spreadsheets by standardizing categorization for both assets
andtransactionsandconsolidatingallofthedatawithinasingleinterface. Thishelps
centralizing the user’s financial management, and ultimately helps their decision-
makingprocess. Moreorganizedandcategorizedfinancialdatacanaidmoreinformed
insightsanddecision-making. ThissupportsfindingsfromGafrikovaetal. (2015),
who described how PFM tools provide users with categorized expense tracking,
groupedspendingbytype(e.g.,rent,food,transportation),andaggregatedfinancial
informationfromvarioussources,whichimprovesvisibilityintopersonalfinancial
flows. Handayani etal. (2024)similarly notedthatautomatic expensetrackers, cate-
gorizationfeatures,andintegrationacrossfinancialsourcesallowuserstorecognize
theirspendingpatternsandmakebetterfinancialdecisions.
7.5 Integrated and efficient reporting
One of the most labor-intensive tasks in the stakeholder’s previous workflow was
the creation of quarterly financial reports. This process involved manually copying
charts,aggregatingfiguresfromvariousspreadsheets,andcompilingthemintoaWord
document. ThePoCapplicationreplacesthiswithafullyintegratedreportingfeature
thatgeneratesacomprehensivesummaryforaselectedtimeperiod.
ThereportconsolidatesdatafrommultiplepartsofthesystemintoasinglePDF
45

fileandincludesthefollowingelements:
• Monthlyincome,expenses,andsurplusvisualizedinagroupedbarchart
• Savingspercentagepermonth
• Expensesvs. incomedisplayedasalinechart
• Adetailedlistofcategorizedcashflowtransactions
• Networthdevelopmentovertimeandbreakdownbyassetcategory
• Sharedistributionbytype,country,andsubcategory
Alldataisautomaticallyretrievedfromthebackendandvisualizedthroughcharts
and tables based on the selected time frame. The compiled report is exported as
a downloadable PDF document, allowing users to archive or review their financial
summarieswithoutmanualintervention.
This feature saves time and effort when generating reports on a recurring basis
by replacing a multi-step manual process with one integrated functionality. As
Cederberg (2013) says, automating repetitive financial tasks along with providing
visual summaries for clarity can reduce the burden on users and ease adoption.
Likewise,Shafieeetal. (2024)pointoutthatreportingprovidescoherentandvisual
outputsto helpestablishunderstanding andinformdecisions. It alsosatisfies theidea
foranoverviewoffinancesbyKayeetal. (2014),consolidatinganumberoftoolsand
processesintoasingularreportingprocess.
46

User-generatedfinancialreportforaselectedtimeperiod
Figure 10:
By automating the generation of structured and visually rich reports, the system
supports more efficient and consistent financial review cycles while preserving the
stakeholder’spreferencefordetaileddocumentationandanalysis.
47

8 Evaluation
Thischapterpresentstheresultsoftheevaluationphase. Thegoalofthisphaseisto
assess how effectively the implemented artifact addresses the original problem and
fulfillsthedefinedsolutionobjectives. Fourevaluationmethodswereused: task-based
usertesting, astakeholderfeedbackquestionnaire,comparisontothebaselinesystem,
andanalyticalassessmentagainstthedesignobjectives.
8.1 Task-based user testing
Task-basedusertestingwasconducted toobservethestakeholderinteractingwiththe
systemina realisticusagescenario. Thepurpose was toevaluatetheusability, core
functionality,andoveralluserexperience. Thestakeholderperformedapredefinedset
oftasksontheirownmachinewhilebeingobserved. Eachtaskwasassessedbasedon
successfulcompletion, workflow intuitiveness, and any usabilityissues orfeedback
thatarose. ThetaskswereoriginallydefinedinChapter3.1.5.
All tasks were completed successfully. The stakeholder navigated the system
confidentlyandrequirednoexternalguidancetolocateoruseanyofthekeyfeatures.
Taskdurationsrangedfromtwotofiveminutes,dependingondataentryrequirements.
Forexample:
• Task 1: The stakeholder imported share transactions using a CSV file and
manuallyaddedtwocashandtworealestatetransactions.
• Task2:Theuserexploredpiechartsonthedashboardbycategoryandreviewed
datatableson the"AssetsandTransactions"page,includingtestingthesorting
andeditingfunctionalities.
• Task 3: Multiple income and expense transactions were added across a four-
monthperiod,followedbyareviewoftheupdatedcashflowvisualizations.
• Task4:Thestakeholdergeneratedafinancialreportfortheperiod1.1.2025–30.4.2025
andexaminedthecontentsofthegeneratedPDFfile.
Feedback during testing primarily concerned user interface clarity and usability
improvements. Notablesuggestionsincluded:
• Enhancingtooltipsinpiechartstoshowadditionaldetails(e.g.,EURvalue)
• Improvinglabelclarityintherealestatetable
• Adjustingthetransactionorderinginthecashflowlistforbetterintuitiveness
Despite these observations, all tasks were completed without errors or external
assistance which indicates that the system provides a generally intuitive and user-
48

friendly experience. These findings are consistent with literature showing that
structured, intuitive interfaces and visual feedback mechanisms play a big role in
improvinguserengagementandconfidenceinpersonalfinancetools. Thisissupported
by Cederberg (2013), who found that simplified interfaces with visual summaries
reduce user effort and promote adoption. Similarly, Shafiee et al. (2024) note that
user-friendlyandpersonalizedinterfacesimproveusers’understandingandconfidence
infinancialdecision-making.
8.2 Stakeholder insights from questionnaire
Followingthetask-basedtestingsession,astructuredquestionnairewasadministered
to gather deeper feedback from the stakeholder. The questions were organized into
four areas: general impressions, feature satisfaction, problem-solving impact, and
suggestions for future development. This section summarizes the stakeholder’s
responsesineacharea.
8.2.1 General impressions
The stakeholder found the interface intuitive and user-friendly. Although some
functionalitieswerenotimmediatelyvisible,theywereeasilydiscoveredthroughbrief
exploration. Overall,the structureandnavigation ofthe application wereconsidered
effectiveandalignedwithtypicaluserexpectations.
8.2.2 Feature satisfaction
Thesharetrackingfunctionalitywaspraisedforitsscalabilityandeaseofusecompared
tothestakeholder’spreviousExcelsystem. Theautomationofdataaggregationand
valuecomputationwasseenasamajorimprovement.
The stakeholder found the cash flow feature useful and realistic but suggested
clarifyingitspurposewhetheritismeantfordetailedbudgetinglikeinappssuchas
Spendee,orformoregeneralexpensetracking. Thiswouldhelpdeterminewhether
thefeatureshouldbesimplifiedoroffermorecustomization.
Visualizationsweredescribedasclearandinformative. Thestakeholderhighlighted
the pie charts and trend graphs as particularly valuable for gaining quick insights.
Minorrefinementsweresuggested,particularlyforthelong-termcapitaldevelopment
graphtoimproveclarity.
The PDF report generation feature was considered a strong improvement. It
streamlinedapreviouslymanualandtime-consumingreportingprocess,offeringclear
valuethroughautomationandintegration.
49

8.2.3 Problem-solving impact
The stakeholder reported a reduction in manual work, especially with processes that
wentbackandforthbetweenexcelandgooglesheets. Theabilitytoseeallthefinancial
informationinoneinterfacewasseenasamajorimprovement. Thissupportsfindings
byKayeetal. (2014)thatuserspreferredsimplifiedsnapshotsratherthanacomplete
representation. Inasimilarmanner,Cederberg(2013)notedthatPFMsystemsoffering
centralized and easy-to-access financial data increase user motivation and ongoing
engagement.
Systemstabilityanddatareliabilitywerealsonoteworthy. Incontrasttotheprevious
Excelworkflowthatwassusceptibletobrokenformulasandinconsistencies,thePoC
was praised as secure and dependable. Automatic integration of transactions and
chronological organization contributed to a higher level of trust in the data. This
finding supports the consideration of epistemic stability in personal finance tools,
articulatedbyHerralaetal. (2023). Theyarguedthatusersmustbeabletotrustthe
logic andoutputof the applicationin orderto experience thesense ofempowerment
andfeelingofcontrolovertheirfinances. Whentoolsareperceivedasunpredictable
or"blackbox",users’trustinthedataandthesystemasawholecandecrease.
8.2.4 Suggestions and future improvements
Suggestions focused primarily on improving user experience and refining existing
features. Theseincluded:
• Enhancingtooltipandgraphclarity
• Addingtheabilitytomodifytransactionsdirectlyfromthetransactionlist
• Clarifyingtheintendeduseofthecashflowfunctionality
Overall,thestakeholderexpressedstrongconfidenceintheapplication’spotential.
Theyindicatedthatwithfurtherrefinementanditeration,thesystemcouldevolveinto
afullydeployableproductthatmeetsbroaderpersonalfinancemanagementneeds.
8.3 Comparison to baseline
In order to assess the practical advantages of the implemented solution, a simple
comparisonwasmadebetweenthestakeholder’sexistingfinancialtrackingmethod
tothe PoCapplication. Theoriginalmethodconsisted ofnumerousapproaches and
tools,suchasExcelspreadsheets,GoogleSheets, andtheSpendeeapplication,where
consolidatingalloftheinformationwaslaboriousandmanual.
Table9summarizeskeydifferencesbetweenthebaselinesetupandthePoCsystem.
50

| Aspect        | Oldsystem(Baseline)  |        | Newsystem(PoC)           |
| ------------- | -------------------- | ------ | ------------------------ |
| Tool          | Multipletools:       | Excel, | Centralized,web-based    |
| fragmentation | Spendee,GoogleSheets |        | application              |
| Shareprice    | Manualcopy-pastefrom |        | AutomatedviaGoogleSheets |
| updates       | GoogleFinance        |        | APIintegration           |
Exchangerate Manuallycheckedandentered Automaticallyfetcheddaily
| updates        |                    |     | fromHexaRateAPI            |
| -------------- | ------------------ | --- | -------------------------- |
| Income/expense | RecordedinSpendee, |     | Enteredandvisualizedwithin |
| tracking       | analyzedinExcel    |     | theapplication             |
Datavisualization Static,manuallycreatedExcel Interactive,real-time
|           | charts                 |     | visualizationsandtables  |
| --------- | ---------------------- | --- | ------------------------ |
| Financial | Manualreportassemblyin |     | AutomatedPDFreportswith  |
| reporting | WordwithExcelcharts    |     | integrateddataandvisuals |
Stabilityand Highriskofformulaerrors Backend-calculatedvalues
| accuracy                                                   | andbrokenreferences        |     | withrobustlogic       |
| ---------------------------------------------------------- | -------------------------- | --- | --------------------- |
| Timespent                                                  | Significantmanualeffortand |     | Streamlinedupdatesvia |
| updating                                                   | toolswitching              |     | integrateddataflow    |
| Table 9: ComparisonofthebaselinesystemandthePoCapplication |                            |     |                       |
Asseen inTable9, thePoC solutionmeetsthe mostimportantissuesfoundfrom
theprevious system,by offeringcentralizeddata, anautomated updates,andbuilt-in
analyticcapabilities. Inshort,itminimizesusermanualworkloadanderrorrateswhile
increasing data transparency. The stakeholder was in agreement that the usability,
automation,andtrustintheaccuracyofthedatahadimproved. Tornoetal. (2021)
found that most personal finance solutions tend to focus on very few features or
services,sothisPoCfocusesbridgingthesegaps.
| 8.4 Evaluation | against | design objectives |     |
| -------------- | ------- | ----------------- | --- |
ThissectionassesseshoweffectivelytheimplementedPoCmeetsthefunctionaland
quality objectives defined in Chapter 5. Each requirement is reviewed basedon the
actual system implementation, stakeholderfeedback, andoutcomes observed during
theevaluationphase.
FR-01: Userinterface(Desktopandmobile)
ThesystemwasimplementedusingFlutter,supportingdeploymentacrossdesktop,
web,andmobileplatforms. Thestakeholderconfirmedtheinterfacewasintuitiveand
easytouseduringdesktoptesting. However,thecurrentimplementationisprimarily
optimized fordesktop and web, withmobile-specific layoutadjustments stillpending.
Status: Partiallyachieved
FR-02: Datavisualizationofcapitalandstatistics
Interactivechartsandgraphswereimplementedtovisualizenetworthtrends,asset
51

categories,andcashflowsummaries. Thestakeholderhighlightedthesefeaturesas
clearandsignificantlymoreeffectivethantheirpreviousmanualvisualizations. Status:
Achieved
FR-03: Tagging
Thedatamodelsupportsassetclassificationbycategories,subcategories,andcountry
oforigin. Taggingisappliedconsistentlyacrossshares,cashaccounts,realestate,and
cashflowtransactions. Status: Achieved
QA-01: Correctnessofstatistics
Keycalculations,includingnetworth,profit/loss,andsavingsrate,areperformedby
centralizedbackendlogic,reducingriskofusererror. Thestakeholderconfirmedthe
accuracyandreliabilityoftheresults. Status: Achieved
FR-04: Presentreal-timecapitalinformation
Real-timemarketdataandexchangeratesarefetchedautomatically,ensuringup-to-
date capital values. This functionality was identified by the stakeholder as a major
improvementoverthemanualupdateprocess. Status: Achieved
FR-05: Financialreportgeneration
ThesystemprovidesdownloadablePDFreportssummarizingkeyfinancialmetrics
overaselectedtimeframe. Thisreplacedthestakeholder’smanualreportingprocess
andwasviewedasamajorefficiencyimprovement. Status: Achieved
QA-02: Dataaccesscontrol
Although the data model is designed to support user-level data segregation, no
authenticationorauthorizationmechanismswereimplemented. Thislimitationwas
acknowledged and deferred due to time constraints and PoC scope. Status: Not
achieved
FR-06: Automaticdatafetching
The system integrates with external sources to retrieve exchange rates and share
prices. However,fullautomationofbankorbrokertransactionswasnotimplemented.
Despitethis,thecurrentsolutionmeaningfullyreducesmanualeffort. Status: Partially
achieved
FR-07: Choosecurrency
All financialdata is normalized to a base currency, with exchange rates fetcheddaily.
Thisensuresconsistencyacrosscalculationsandsupportsuser-definedcurrencyviews.
Status: Achieved
FR-08: Customizabledashboards
Customizable dashboards were not implemented. All visualizations are static and
predefined. Thisfeature wasdeprioritizeddue to limitedtime and PoCfocus. Status:
Notachieved
52

FR-09: Manualfinancialdatainput
StructuredformsandCSVimportfeatureswereimplementedforallmajortransaction
types,enablingeffectivemanualdataentryandcorrections. Status: Achieved
QA-03: Goodresponsetime
Performance during testing was consistently fast. Efficient data fetching, use of
caching, and statemanagement contributed toa responsive userexperience. However
no performance testing was conducted and some refinements would be needed for
productionversion. Status: Achieved
Insummary,allcore"Musthave"requirementsweresuccessfullyimplementedor
partially fulfilled, ensuring that the fundamental goals of the PoC were met. Most
"Shouldhave"featureswereincluded,whilelower-priorityitemssuchasauthentication
anddashboardcustomizationweredeferredforfuturedevelopmentiterations.
53

9 Discussion
Thischapterlooksbackon theprojectandreflectsonwhat was achieved. Itstartsby
reviewinghowwellthefinalsolutionaddressedtheoriginalproblemandwhatkind
of feedback the stakeholder gave. It also considers how useful the Design Science
ResearchMethodology(DSRM)wasthroughoutthe process. Inaddition, thechapter
highlightssome ofthechallenges facedduringdevelopmentandpoints outpossible
waysthe solutioncould beimprovedorexpanded inthe future. Altogether, itgivesa
clearpictureofwhattheprojectaccomplishedandwhereitcouldgonext.
9.1 Summary of results and impact
ThefindingsfromthisresearchprojectshowthatthePoCapplicationaccomplishesthe
identifiedgoalsdefinedearlierinthethesis. Thecorefunctionalitieswereimplemented
andtestedwiththeactualenduserinarealisticenvironment. Userfeedbackconfirmed
that theapplication solved theprimary stakeholder concerns: it reducedmanual effort
and mitigated human errors. This finding corresponds with Herrala et al. (2023)’s
observationthatcomplexinanerror-pronetoolscanreducefinancialconfidenceand
raiseunnecessaryanxiety,especiallyforyoungerusers. Byreducingcomplexityand
centralizingfinancialdata,thePoCsystemimprovesbothusabilityandreliability.
Unlike many existing PFM tools which focus on limited functionality, such as
budgetingortrackingspendingpatterns(e.g.,Mint,YNAB,Spendee),thePoCwas
designedtoprovideamoreglobalandintegratedapproachacrossallaspectsofPFM.
The PoC provided a functionality for tracking investments, monitoring net worth,
analyzing cash flow, and producing financial reports, in a more centralized way.
ThePoC’sdesigndirectlyaddressedthefragmentedfocusofPFMasrecognizedby
Torno et al. (2021). The study noted that most PFM apps focus on single service
and rarely combine planning, tracking, and education in one app. While Kaye et
al. (2014) noted that some tools provide discomfort due to perceived complexity,
reliability, and fragmented view of PFM thus risking long-term engagement. The
existingstakeholdersystemalsolackedautomationwhichwasnotedintheliterature.
According to Cederberg (2013), automating tasks and reducing manual user input
werebigmotivatorsforadoptingmobilefinancialtools,astheysimplifiedworkflows
andreduced friction. ThePoC applicationimproveson thisbyproviding automated
retrieval of exchange rates, stock price updates, and aggregation of asset data in
real-time.
One of the major strengths was the PoC being adaptable under the European
context. Many of the popular PFM tools, such as Mint, Quicken, etc. are largely
basedonU.S. users,customarilylinkedtoregionally-identifiedfinancialAPIs. This
alsocomplementsthefindingsofStefanovetal. (2024),whostatedthatusersfrom
underrepresentedmarkets,forexamplefromEasternEurope,facelocalizationissues
relatingtoglobalPFMtools. Thestakeholderwasalsoabletobenefitfromfeatures
that include multi-currency and share price updates for both Finnish and Swedish
54

stocks,whichiscommonlynotavailableinmainstreamfinancialapplications.
Anotheridentifiedcoreimprovementwasthetransitiononreportingfromquarterly
to real-time financial reporting. Previously, the stakeholder was only engaging in
quarterly reviews dueto time consuming process. The stakeholder cannowanalyze
real-timedashboardsinonequickviewandinitiatereportsintopdf. Thisfunctionality
supports the findings of Cederberg (2013), which implied that financial tools with
lessmanualinputsandofferedsimplifiedworkflowsmadeitlikelythatusersfurther
engage with personal finance technologies. Similarly, Shafiee et al. (2024) noted
that real-time, personalized outputs enhance users’ understanding and support more
responsivefinancialdecision-making.
Finally,bydeliveringreal-timeinsightsandvisualfeedbackthroughpiecharts,bar
graphs, and trend visualizations, the application promotes awareness and decision
confidence. Bitrián etal. (2021)foundthatvisualandgamifiedelementscanincrease
users’ perceivedcompetenceandengagement. Similarly, Shafieeetal. (2024)showed
that personalized and real-time financial guidance helps users better understand
complexfinancialfactorsandmakemoreinformeddecisions.
9.2 Limitations of the solution
WhilethePoCsuccessfullyaddressedcorerequirements,severallimitationsremain.
Mostunimplementedfeatureswerecategorizedas“nicetohave”oroptionalandwere
intentionallyexcludedduetothelimitedscopeandtimeframeoftheproject. However,
onecriticalweaknessistheabsenceofuserauthenticationandauthorization. Security
isafundamentalconcerninfinancialtechnology,especiallywheresensitivepersonal
data is involved. Kaye et al. (2014) explains that users are often reluctant to adopt
digitalfinancetoolsduetofearsarounddataaccessandprivacy. Similarly,Handayani
et al. (2024)identify securityand dataprotection as centralfactors influencing user
trustinfintechsolutions. Herralaetal. (2023)furtherarguethatwhenusersfeelalack
ofcontrolovertheirfinancialinformation,itcancontributetostressanddisengagement,
highlightingtheimportanceoftransparentandsecuresystemdesign. Thesefindings
underscoretheimportanceofimplementingbasicaccesscontrolmechanismsinfuture
iterationstostrengthensystemcredibilityandpromotelong-termuse.
Fromadevelopmentperspective,themostsignificantlimitationistheincomplete
automationoffinancialdataretrieval. Althoughthestakeholderexpressedsatisfaction
withthecurrentlevelofautomation,thesystemlacksthescalabilityneededtosupport
broaderuserbase. Ideally, userswould beabletoconnect theirbankandbrokerage
accountsdirectlytotheapplication,allowingautomaticsynchronizationoftransactions
and balances. However, this level of integration remains difficult to implement due
to different factors. Several stock price API’s were investigated such as Finnhub,
stockdata.org,eoddata,andAlphavintage,butwereeventuallydiscardedduetolimited
support for European stocks or were too expensive. Investment brokers also do not
have API’s or they are limited, for example Nordnet offers API only in Sweden.
55

Additionally,fromopen-bankingperspective,someoptionswereinvestigatedsuchas
Yapily, Polygon, andGoCardless. Thesewere notsuitable forthe contextcase asthey
wereeithertargetedforenterprisesorrequiredalotofdevelopmentwork. Another
issuewiththeopen-bankingintegrationsistheautomatedcategorizationwhichwas
pointedoutalsobyKayeetal. (2014).
Asapracticalworkaround,thePoCapplicationintegrateswithGoogleSheetsusing
the functiontoretrievestockprices. Thissolution,whilemanualtoset
GOOGLEFINANCE
up, aligned with the stakeholder’s workflow and allowed real-time pricing without
additional financial costs. Still, the absence of seamless, API-based integration for
broader asset classes and account types remains a major limitation. These findings
supportwhatCederberg(2013)observed: manualdataentryandscatteredtoolsmake
itdifficultforpeopletocontinueusingpersonalfinancesystemsinthelongrun.
Anotherthingtonoteisthestakeholdersgoodfinancialliteracyandthereforehigher
expectationsfromthesystem. Astheyhavetrackedtheirfinancesmorethanadecade,
theyhaveaccumulatedalotofknowledgeandexperienceinthisdomain. However,
some usability improvements and educational content would be beneficial to add
in the current application for more novice users. This need is also reflected in the
literature. Torno et al. (2021) point out that few personal finance applications offer
built-in financial education, despite its potential to increase trust and engagement.
Similarly,Lasmiatun(2024)foundthatyoungerusersoftenturntodigitalplatforms
forfinancialguidanceandpreferinteractiveandvisualformatsforlearning. Kayeetal.
(2014) also noted that many users do not engage with existing all-in-one financial
systems,suggestinganopportunitytodesignmoreaccessibleanduser-tailoredfinancial
experiences.
9.3 Reflection on DSRM
Design Science Research Methodology (DSRM) provided an effective structure
for development of this project. The structured iterative process created a logical
progressionstartingwithaproblemdefinitionstepandendingwithanartifactevaluation
stepwhich was extremely usefulin a solodevelopmentenvironment. DSRM consists
ofsetofstepsas describedbyPeffersetal. (2007)thatenableresearcherstodevelop
solutionstoreal-worldproblemsbythedesignandevaluationofartifacts.
EachphaseoftheDSRM directlyinformedthenext. In DesignandDevelopment
phase,thearchitecturaldecisionswerederivedfromthefunctionalandnon-functional
requirements. The requirements on the other hand were formatted based on the
stakeholderneedsfoundintheProblemidentificationphase. Evaluationphasebenefited
fromtheestablishedobjectivesbutalsoprovidedsubstancetotheirevaluation. This
correspondswiththeguidanceofHevneretal. (2004)thatutility,quality,andefficacy
arenecessarycriteriaofevaluatingdesignartifactsininformationsystemsresearch
context.
56

Having a real stakeholder involved made a big difference in the project. Their
ongoingfeedbackgavepracticalinsightsthatwouldhavebeenhardtodiscoverthrough
theory alone. By taking part in the demonstration and evaluation, they ensured the
solution met real needs and worked in practice. As De Sordi (2021) points out,
involvingpractitionersinDesignScienceResearchmakestheresultsmorerelevant
andstrengthensthecredibilityoftheresearch.
Overall, Design Science Research Methodology gave a clear but flexible way to
work through the project. It made it easier to build a useful and practical solution
whilestillfollowinga solidresearchprocess. Thismade itagoodchoice foraproject
likethisthatcombinesreal-worldneedswithacademicwork.
9.4 Opportunities for future development
TheevaluationphaserevealedseveralkeyopportunitiestoenhancethePoCapplication
and move toward a production-ready solution. The most critical area for future
development is the integration of automated data fetching from banks and brokers.
Implementing such features wouldsignificantlyreduce manual input, enhance user
convenience,andimprovethesystem’sscalabilityforawideraudience. Thisaddresses
alimitationalsoobservedbyTornoetal. (2021)andStefanovetal. (2024),whofound
thatmostPFMtoolslackcomprehensiveintegrationacrossfinancialinstitutions,with
Stefanovetal. (2024)furthernotingthatmanysolutionsofferonlylimitedlocalized
services,reducingtheireffectivenessincertainmarkets.
Usability improvements also emerged as a priority. The stakeholder identified a
range of refinements that would improve the user experience, including the ability
to edit transactions directly, more informative tooltips, and clearer differentiation
betweendetailedbudgetingandhigh-levelcashflowtracking. Thisalignswithfindings
by Cederberg (2013), who described that users value intuitive, visually appealing
interfacesthatreducemanualeffortandsupportfinancialself-awareness. Similarly,
Bitrián et al. (2021) found that clear feedback mechanisms and well-designed user
experiencesfosterperceivedcompetenceandautonomywhicharetwokeydriversof
sustaineduseinpersonalfinanceapplications.
Theadditionofuserauthenticationandauthorizationisessentialforensuringdata
privacy and security, especially if the system is to be deployed beyond the original
stakeholder. On the technical side, the introduction of unit and integration testing,
alongwith comprehensivedocumentation, wouldsupportlong-termmaintainability
andfacilitatecollaborationinlargerdevelopmentteams. Also,splittingthearchitecture
into severalmicroservices wouldincrease scalabilityandincrease performancefora
productionenvironmentwheremoretrafficistobeexpected.
57

10 Conclusions
This thesis covered the design and development of a centralized personal finance
managementapplicationthataddressedtheproblemsfacedbyanindividualstakeholder.
The main issues involved the complexity, fragmentation, and manual workload
that were found in the stakeholder’s existing financial tracking setup. The system
relied on a combination of Excel spreadsheets, third-party apps, and manual data
consolidation. The objective was to create a customized solution that improves
automation, visualization, and reporting while supporting personalized financial
analysis.
The projectfollowedthe DesignScience ResearchMethodology (DSRM),which
providedastructuredanditerativeframeworkwithsixsteps: problemidentification,
objective definition, design and development, demonstration, evaluation, and com-
munication. This methodologysupportedboththe technicalexecutionandacademic
rigoroftheresearchprocess. Eachphaseproducedoutcomesthatcouldbeusedonthe
nextstages,eventuallyresultinginafunctioningproof-of-concept(PoC)application.
The final artifact includes asset tracking such as shares, cash, and real-estates,
categorizedcashflowmonitoring,andfinancialPDFreportgeneration. Inadditionto
constantfeedbackduringthedevelopmentphase,thesefeatureswerevalidatedthrough
task-basedusertestingandstructuredstakeholderfeedback. Comparedtothebaseline
system, the PoC significantly reduced manual effort, improved data reliability, and
offered a centralized view of the user’s financial status. These outcomes align with
findingsintheliterature,whichstressedthatsimplification,visualfeedback,andtrust
areimportantforeffectivepersonalfinancetools.
However, the PoC did not implement several planned features, including user
authentication,customizabledashboards,orfulldataautomationthroughbankingand
broker integrations. These limitations stemmed from external API constraints and
thelimitedscopeofasolodevelopmentprojectandwouldbemainfocusareaifthis
applicationwouldbedeployedtobroaderuse.
Oneofthechallengesfacedduringthisthesiswasfindinggoodliteraturethatreally
looked at how people manage their finances in everyday life. A lot of the existing
researchfocusesonfinancialliteracy,behavior,orplanningtheory,buttherewasnot
muchdetailaboutwhattoolspeopleactuallyuse. Itwashardtofindstatisticsorstudies
aboutwhichappspeoplerelyon,whatworksforthem,andwhatproblemstheyrun
into. Thatisoneofthemainreasonsthisthesiscametolife. Mostappsonthemarket
arebuiltjustforbudgetingortrackingexpenses. WithsimpleGooglesearch“personal
financeapps,”almostallofthemfallintothatcategory. Butmanagingyourfinances
is more than just budgeting. People also want to track investments, assets, and see
theirfullfinancial pictureinone place. Moreresearchis neededthatlooks intohow
peopleactuallymanagetheirfinancesandhowtoolscouldbebuilttosupportthat.
58

References
| Atkinson, | Adele      | and | Flore-Anne |                 | Messy | (2012). |           |                     |           |           |      |
| --------- | ---------- | --- | ---------- | --------------- | ----- | ------- | --------- | ------------------- | --------- | --------- | ---- |
|           |            |     |            |                 |       |         | Measuring |                     | Financial | Literacy: |      |
|           |            |     |            | INFEPilotStudy. |       | Tech.   | rep.      | 15. OECDPublishing. |           |           | doi: |
| Results   | oftheOECD/ |     |            |                 |       |         |           |                     |           |           |      |
|           |            |     |            | .               | url:  |         |           |                     |           |           |      |
10.1787/5k9csfs90fr4-en https://www.oecd.org/content/dam/oecd/
en/publications/reports/2012/03/measuring-financial-literacy_g17a210b/
.
5k9csfs90fr4-en.pdf
Bitrián,Paulaetal. (2021). “Makingfinancefun: thegamificationofpersonalfinancial
managementapps”. In: InternationalJournalofBankMarketing39.7,pp.1310–
| 1332. | doi: |                           |     |     |     | . url: |                               |     |     |     |     |
| ----- | ---- | ------------------------- | --- | --- | --- | ------ | ----------------------------- | --- | --- | --- | --- |
|       |      | 10.1108/IJBM-02-2021-0074 |     |     |     |        | https://doi.org/10.1108/IJBM- |     |     |     |     |
.
02-2021-0074
| Brush, | Kate (2023). |     |        |     | method. TechTarget |     | definitions. |     | url:         |     |     |
| ------ | ------------ | --- | ------ | --- | ------------------ | --- | ------------ | --- | ------------ | --- | --- |
|        |              |     | MoSCoW |     |                    |     |              |     | https://www. |     |     |
.
techtarget.com/searchsoftwarequality/definition/MoSCoW-method
Cederberg,Jessica(2013). “ChangingFinancialBehaviorsUsingMobilePFMTools
| (Dissertation)”. |     |     | In: Södertörn |     | University, | Sweden. |     | url: |     |     |     |
| ---------------- | --- | --- | ------------- | --- | ----------- | ------- | --- | ---- | --- | --- | --- |
https://urn.kb.se/
.
resolve?urn=urn:nbn:se:sh:diva-19735
De Sordi, José Osvaldo (2021). Design Science Research Methodology: Theory
Development from Artifacts. 1st. Palgrave Macmillan Cham. doi:
https:
.
//doi.org/10.1007/978-3-030-82156-2
DiDomenico,StefanoI. etal. (2022). “Motivationsforpersonalfinancialmanagement:
ASelf-DeterminationTheoryperspective”. In: FrontiersinPsychologyVolume13
| -2022. | issn: | 1664-1078. |     | doi: |                           |     |     |     | . url:       |     |     |
| ------ | ----- | ---------- | --- | ---- | ------------------------- | --- | --- | --- | ------------ | --- | --- |
|        |       |            |     |      | 10.3389/fpsyg.2022.977818 |     |     |     | https://www. |     |     |
.
frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.977818
| Enstrom, | D.  | W. (2018). |            |     |               |     | Decision. |     |                      |     |     |
| -------- | --- | ---------- | ---------- | --- | ------------- | --- | --------- | --- | -------------------- | --- | --- |
|          |     |            | Guideline: |     | Architectural |     |           |     | https://www.unified- |     |     |
am.com/UAM/UAM/guidances/guidelines/uam_architectural_decision_BAE7AFA2.
|     | . UnifiedArchitectureMethod(UAM). |     |     |     |     |     |     |     |     |     |     |
| --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
html
French,Declanetal. (2021). “Personalfinanceappsandlow-incomehouseholds”. In:
| StrategicChange30,pp.367–375. |     |     |     |     | doi: |     |     |     | .   |     |     |
| ----------------------------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
10.1002/jsc.2430
Gafrikova,V. etal. (2015). “Onlinepersonalfinancemanagementapplications”. In:
In-
| formationSystemsinManagement4.1,pp.39–52. |     |     |     |     |     |     | url: |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
https://bibliotekanauki.
.
pl/articles/94727
Gitman,L.J. etal. (2011). Personalfinancialplanning. 12th. South-WesternCengage
| Learning. |     | isbn: | 978-1-4390-4447-6. |     |     |     |     |     |     |     |     |
| --------- | --- | ----- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Handayani, Tika et al. (2024). “Fintech Analysis of Personal Finance App Usage
among Millennials”. In: Journal of Economic Education and Entrepreneurship
| Studies5,pp.150–162. |     |     |     | doi: |     |     |     | .   |     |     |     |
| -------------------- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
10.62794/je3s.v5i2.2299
Herrala, Juha-Matti et al. (2023). “How Personal Finance Management Systems
Emancipate and Oppress Young People”. In: Proceedings of the 56th Hawaii
International Conference on System Sciences, pp. 5542–5550. doi:
10.24251/
.
HICSS.2023.675
Hevner,AlanR. etal. (2004). “DesignScienceinInformationSystemsResearch”.
| In: MISQuarterly28.1,pp.75–105. |     |     |     |     | doi: |     |     |     |     |     | .   |
| ------------------------------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
https://doi.org/10.2307/25148625
Huang, Lisha (2016). “Personal Financial Planning for College Graduates”. In:
| Technology |     | and | Investment | 7,  | pp. 123–134. |     | doi: |     |     |     | . url: |
| ---------- | --- | --- | ---------- | --- | ------------ | --- | ---- | --- | --- | --- | ------ |
10.4236/ti.2016.73014
.
https://doi.org/10.4236/ti.2016.73014
59

Ironhack (2024). Functional vs Non-Functional Requirements: Understanding the
| Core Differences |     | and | Examples. | Ironhack | blogs. | url: |     |     |
| ---------------- | --- | --- | --------- | -------- | ------ | ---- | --- | --- |
https://www.ironhack.
com/gb/blog/functional-vs-non-functional-requirements-understanding-
.
the-core-differences-and
Kaye, Joseph Jofish et al. (2014). “Money talks: tracking personal finances”. In:
ProceedingsoftheSIGCHIConferenceonHumanFactorsinComputingSystems.
AssociationforComputingMachinery,pp.521–530. isbn: 9781450324731. doi:
|     |     |     | . url: |     |     |     |     | .   |
| --- | --- | --- | ------ | --- | --- | --- | --- | --- |
10.1145/2556288.2556975 https://doi.org/10.1145/2556288.2556975
Lai, Ming-Ming and Wei-Khong Tan (2009). “An Empirical Analysis of Personal
FinancialPlanninginanEmergingEconomy”. In: EuropeanJournalofEconomics,
| FinanceandAdministrativeSciences. |     |     |     | issn: | 1450-2275. |     |     |     |
| --------------------------------- | --- | --- | --- | ----- | ---------- | --- | --- | --- |
Lasmiatun, KMT (2024). “The Role of Financial Education in Improving Personal
FinancialPlanning: AQualitativeStudyonGeneration Z”. In: Nomico1, pp.149–
| 158. doi: |     |     |     | .   |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- |
10.62872/8n585q36
Lusardi, Annamaria and Olivia S. Mitchell (2014). “The Economic Importance of
| Financial     | Literacy: | Theory | and | Evidence”. |     | In:     |             |            |
| ------------- | --------- | ------ | --- | ---------- | --- | ------- | ----------- | ---------- |
|               |           |        |     |            |     | Journal | of Economic | Literature |
| 52.1,pp.5–44. |           | doi:   |     |            |     |         | .           |            |
https://doi.org/10.1257/jel.52.1.5
Peffers,Kenetal. (2007). “Adesignscienceresearchmethodologyforinformation
systems research”. In: Journal ofManagementInformation Systems 24, pp. 45–77.
| doi: |     |     |     | .   |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- |
10.2753/MIS0742-1222240302
Rajesh, R.J. and K.V. Giridhar (2024). “Financial literacy and personal financial
management: Smart movestowardspersonalfinance”. In: ShanlaxInternational
| Journal | of Arts, | Science | and | Humanities | 12.S1, | pp. 62–67. | doi: |     |
| ------- | -------- | ------- | --- | ---------- | ------ | ---------- | ---- | --- |
https://doi.
. url:
org/10.34293/sijash.v12iS1-Oct.8285 https://shanlaxjournals.in/
.
journals/index.php/sijash/article/view/8285
Shafiee,Saraetal. (2024). “ImprovingFinancialLiteracyandSupportingFinancial
| Decisions: | DevelopingaPersonalizedConfigurator”. |     |     |     |     | In: |     |     |
| ---------- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
JournaloftheKnowledge
| Economy | 15, | pp. 14256–14285. |     | doi: |     |     |     |     |
| ------- | --- | ---------------- | --- | ---- | --- | --- | --- | --- |
https://doi.org/10.1007/s13132-023-
.
01651-9
Shah,SweetyandAmolaBhatt(2014). “UnderstandingPracticesofPersonalFinancial
Planning (PFP)”. In: Internationalconferenceon “Roleof FinancialIndustryin
AcceleratingEconomicGrowth”organisedbyGujaratTechnologicalUniversity
(GTU)-CentreforFinancialServices,Ahmedabad.
Siegel, R. and C. Yacht (2009). Finance. Saylor Foundation. isbn:
Personal
| 9780982361863. |     | url: |     |     |     |     |     | .   |
| -------------- | --- | ---- | --- | --- | --- | --- | --- | --- |
https://open.umn.edu/opentextbooks/textbooks/31
Stefanov, Tihomir et al. (2024). “Personal Finance Management Application”. In:
| TEMJournal |     | 13,pp.2066–2075. |     | doi: |     |     | .   |     |
| ---------- | --- | ---------------- | --- | ---- | --- | --- | --- | --- |
10.18421/TEM133-34
Torno, Albert et al. (2021). “More than Mobile Banking – A Taxonomy-based
AnalysisofMobilePersonalFinance Applications”. In: PACIS 2021Proceedings.
| 179. url: |     |     |     |     |     | .   |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- |
https://aisel.aisnet.org/pacis2021/179
Vaishnavi, V.K. and W. Kuechler (2015). Design Science Research Methods and
|           |            |     |             |     |               |     | Technology. | 2nd. CRC |
| --------- | ---------- | --- | ----------- | --- | ------------- | --- | ----------- | -------- |
| Patterns: | Innovating |     | Information | and | Communication |     |             |          |
| Press.    | doi:       |     |             |     |               | .   |             |          |
https://doi.org/10.1201/b18448
60