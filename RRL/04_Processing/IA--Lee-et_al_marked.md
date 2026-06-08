Journal of Medical Economics
ISSN: 1369-6998 (Print) 1941-837X (Online) Journal homepage: www.tandfonline.com/journals/tfocoll
Comparing deep learning and classical regression
approaches for predicting healthcare expenditure
and spending: a systematic review
John Tayu Lee, Melody Hsiao-San Yeh, Vincent Cheng-Sheng Li, Hsiao-Hui
Chen, Yi-Hsuan Liu, Yu-Chun Chen & David Bin-Chia Wu
To cite this article: John Tayu Lee, Melody Hsiao-San Yeh, Vincent Cheng-Sheng Li, Hsiao-
Hui Chen, Yi-Hsuan Liu, Yu-Chun Chen & David Bin-Chia Wu (2023) Comparing deep
learning and classical regression approaches for predicting healthcare expenditure
and spending: a systematic review, Journal of Medical Economics, 29:1, 654-671, DOI:
10.1080/13696998.2026.2630598
To link to this article: https://doi.org/10.1080/13696998.2026.2630598
© 2026 The Author(s). Published by Informa
UK Limited, trading as Taylor & Francis
Group
View supplementary material
Published online: 04 Mar 2026.
Submit your article to this journal
Article views: 640
View related articles
View Crossmark data
Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=tfocoll

JOURNALOFMEDICALECONOMICS
2026,VOL.29,NO.1,654–671
https://doi.org/10.1080/13696998.2026.2630598
Article/2630598
ORIGINAL RESEARCH
Comparing deep learning and classical regression approaches for
predicting healthcare expenditure and spending: a systematic review
John Tayu Leea , Melody Hsiao-San Yeha , Vincent Cheng-Sheng Lia , Hsiao-Hui Chena ,
Yi-Hsuan Liub , Yu-Chun Chena and David Bin-Chia Wuc
aInstitute ofHealth PolicyandManagement,Collegeof PublicHealth, NationalTaiwan University, Taipei, Taiwan;bMaster
Program ofStatistics, NationalTaiwan University, Taipei, Taiwan;cSaw Swee HockSchool ofPublic Health, National
University ofSingapore, UniversityHall, Singapore
ABSTRACT ARTICLEHISTORY
Aims: This study compares deep learning architectureswith traditionalregression and Received11December2025
tree-based modelsforindividual-level healthcare cost prediction, with particularatten- Revised7February2026
tiontoperformancedifferencesacrossdatacontexts. Accepted9February2026
Methods: We conducted a preregistered systematic review (PROSPERO
KEYWORDS
CRD420251129440). Web of Science, PubMed, Embase, and Scopus were searched
Healthcareexpenditure;
through August 2025. Eligible studies used real-world individual-level data (claims,
healthspending;deep
electronic health records, or registries) to predict cost-related outcomes with at least learning;neuralnetwork;
one deep learning architecture and one classical regression comparator, and reported predictivemodeling;health
quantitative performance. Data were extracted on population, predictors, outcome economics
horizon, model type, validation strategy, performance metrics, calibration, and
JELCODES
interpretability.
Results: Eight studies met inclusion criteria, spanning the United States, Europe, and I13;I15;I28;H51
Asia. In longitudinal designs—such as multi-year claims prediction and medication or
hospitalization time-series forecasting—sequential deep learning models, particularly
LSTM and CNN–LSTM hybrids, consistently outperformed regression and tree-based
algorithms. Reported gains included approximately 10–20% reductions in RMSE/MAE,
R2 improvements of 0.01–0.15, and AUROC values up to 0.78 for high-risk classifica-
tion. Across studies, prior costs and utilization were consistently the strongest predic-
tors, while social determinants and free-text features were rarely incorporated. In
contrast, for low-dimensional, structured, cross-sectional medical data, generalized lin-
ear models and tree-based approaches remain robust baseline models due to their
interpretabilityandcalibrationstability.
Limitations: Evidence is based on a small and heterogeneous set of eight studies,
with limited external or temporal validation, short prediction horizons, and sparse
assessment of calibration, economic interpretability, and fairness, warranting cautious
interpretation.
Conclusions:Deeplearningofferscleargainsforlongitudinal,sequence-richcostfore-
casting, whereas tree-based methods remain highly competitive for cross-sectional
tabular prediction. Overall, these findings are consistent with the proposed
Complexity–Performance Hypothesis, which posits that the predictive advantages of
deep learning emerge primarily when model capacity is well matched to data
complexity.
Introduction
Healthcare expenditures continue to rise globally, imposing escalating burdens on payers, governments,
and patients alike1–3. Accurate forecasts of individual and population-level health costs are crucial—not
CONTACT John Tayu Lee johntayulee@ntu.edu.tw Institute of Health Policy and Management, College of Public Health, National
TaiwanUniversity,No.17,Xu-ZhouRoad,ZhongzhengDistrict,Taipei,100,Taiwan
Supplementaldataforthisarticleisavailableonlineathttps://doi.org/10.1080/13696998.2026.2630598.
(cid:1)2026TheAuthor(s).PublishedbyInformaUKLimited,tradingasTaylor&FrancisGroup
ThisisanOpenAccessarticledistributedunderthetermsoftheCreativeCommonsAttribution-NonCommercial-NoDerivativesLicense(http://creativecommons.
org/licenses/by-nc-nd/4.0/),whichpermitsnon-commercial re-use,distribution,andreproduction inany medium,providedthe originalworkis properlycited,
andisnotaltered,transformed,orbuiltuponinanyway.ThetermsonwhichthisarticlehasbeenpublishedallowthepostingoftheAcceptedManuscriptina
repositorybytheauthor(s)orwiththeirconsent.
www.tandfonline.com/ijme

JOURNALOFMEDICALECONOMICS 655
only for academic modeling but also for practical applications in insurance underwriting, risk adjustment,
budget planning, and value-based payment strategies4. Traditional statistical approaches (e.g. linear
models, generalized linear models, two-part models) frequently struggle to capture complex, nonlinear
interactions in health data and may underperform when faced with high-dimensional
inputs5–7.
In recent years, deep learning and neural network architectures have garnered considerable attention
for their promise in modeling high-dimensional, heterogeneous data8,9. For example, Drewe-Boss et al.
(2022) applied a deep neural network to claims data of German insurees and demonstrated superior per-
formance over ridge regression in predicting next-year total healthcare costs10. Such applications under-
score the potential of neural networks to learn latent feature interactions, temporal patterns, and
nonlinearities that conventional models often miss7,8.
However, despite such advances, important methodological questions remain. It is still unclear how
extant studies differ in their policy or operational context, population and data sources, neural network
architectures and training strategies, sensitivity analyses, software platforms, and modes of result presen-
tation and
interpretation11–13.
Moreover, many papers provide limited comparisons between neural net-
work models and benchmark regression or machine learning alternatives, making it hard to judge when
neural networks truly add value11.
Healthcare expenditures are influenced by multiple interrelated factors. Demographic composition,
particularly population aging, contributes to a growing demand for healthcare services14,15.
Epidemiological, lifestyle and environmental and socioeconomic factors also influence individual and
population health status, are also associated with healthcare spending14. Individual healthcare spending
is also shaped by utilization patterns, access to providers, and broader forces such as economic growth
and technological progress14,15. These determinants interact in nonlinear ways, producing highly skewed
and dynamic spending distributions. Capturing such complexity requires analytical frameworks capable
of modeling heterogeneity and temporal persistence in costs—motivating the application of neural net-
work approaches to health expenditure prediction.
This systematic review aims to map the evolving landscape of neural network-based healthcare cost
and expenditure prediction. Specifically, we systematically searched the literature to address the follow-
ing key questions: (1) What research objectives have been addressed (e.g. total cost, cost change, high-
cost classification)? (2) Which neural network methods—feedforward networks, convolutional nets, recur-
rent architectures (LSTM/GRU), hybrid models, or others—are used in health expenditure prediction?
(3) What evaluation frameworks and result presentation strategies (e.g. error metrics, calibration, classifi-
cation thresholds) are commonly employed? (4) How do neural network model performances compare
with classical regression or machine learning baselines across domains and settings?
Methods
This systematic review was conducted according to a pre-specified protocol and registered with the
International Prospective Register of Systematic Reviews (PROSPERO; registration number CRD420251129440).
A comprehensive search strategy was designed to identify relevant literature across multiple biblio-
graphic databases, including Web of Science, PubMed, EMBASE, and Scopus. The search covered all pub-
lications up to August 2025. Reference lists of included studies were additionally screened to capture
potentially eligible articles not retrieved through the database search.
Studies were considered eligible if they: (1) Applied deep learning or neural network algorithms (e.g.
feed-forward neural network, convolutional neural network, recurrent neural network, long short-term
memory [LSTM], DNN) for the prediction, estimation, or modeling of healthcare expenditure, cost, or
resource use; (2) Used real-world, individual-level health data such as insurance claims, electronic health
records (EHRs), administrative datasets, or registry data; (3) Reported model performance metrics (e.g.
RMSE, MAE, R2, AUC) or compared neural network models against classical or machine-learning base-
lines; and (4) Were published in English.
To ensure methodological comparability, only studies that directly implemented both a deep learning
(or neural network) model and at least one classical regression model (e.g. linear regression, GLM, ridge,
lasso) and quantitatively compared their predictive performance were included. Additionally, studies
were required to include an outcome variable explicitly representing healthcare expenditure, spending,

656 J.T.LEEETAL.
cost, or a closely related economic measure (e.g. medical cost, insurance charge, resource utilization
expressed in monetary units).
Studies were excluded if they: (i) focused exclusively on intervention cost-effectiveness or simulation
modeling without predictive application; used hypothetical, synthetic, or simulated data sources (e.g.
Kaggle or other artificially generated datasets) rather than real-world data; or (iii) applied machine-learn-
ing algorithms other than neural networks without neural network comparison. (iv) did not conduct a
direct comparative analysis between a classical regression model and a deep learning approach on cost-
or expenditure-related outcomes.
Three conceptual domains guided the search formulation: (1) Deep learning and neural network ter-
(cid:1)
minology (e.g. “deep learning,” “neural network ,” “CNN,” “RNN,” “LSTM,” “DNN,” “artificial intelligence,”
(cid:1) (cid:1) (cid:1)
“machine learning”); (2) Predictive modeling expressions (e.g. “predict ,” “forecast ,” “model ,”
(cid:1) (cid:1) (cid:1)
“estimate ,” “projection ”); and (3) Healthcare expenditure concepts (e.g. “healthcare cost ,” “medical
(cid:1) (cid:1) (cid:1)
cost ,” “health expenditure ,” “health spending,” “treatment cost ,” “resource use,” “resource utilization”).
Alternative databases such as ACM Digital Library were evaluated but subsequently excluded due to
limited coverage of health-economic literature.
During the initial screening stage, titles and abstracts were independently assessed by one trained
reviewer according to pre-specified eligibility criteria16. All records that were potentially eligible or for
which eligibility was unclear were retained for full-text review to avoid premature exclusion. Final inclu-
sion and exclusion decisions were jointly discussed by at least two team members; in cases of disagree-
ment, a third team member was consulted to resolve discrepancies and minimize the risk of systematic
selection bias.
Among excluded studies, the most common reason for exclusion was that the prediction target was
not healthcare cost or expenditure but alternative outcomes, such as disease incidence or hospitalisation
risk. Additional studies were excluded because they did not include a direct comparison between tradi-
tional regression or tree-based models and deep learning approaches. Studies relying on simulated or
synthetic data, or other non–real-world data sources, were also excluded. Based on these criteria, a total
of eight studies were ultimately included, all of which used real-world data, explicitly focused on health-
care cost prediction, and directly compared deep learning models with traditional regression or tree-
based approaches.
Data extraction was performed using a structured Excel framework. Extracted variables included bib-
liographic details, data source and setting, population characteristics, neural network architecture, input
variables, model evaluation metrics, comparator models, cost or outcome definitions, and key findings.
Findings were synthesized narratively and summarized in tabular form, categorizing studies by model
type, prediction task, dataset scale, and performance benchmark. Quantitative aggregation was limited
to descriptive reporting due to methodological heterogeneity among studies. The systematic review fol-
lowed the PRISMA 2020 reporting guidelines, and the completed checklist is provided in Supplementary
Table S1.
Results
The database search identified a total of 23,572 records: PubMed (n¼1,525), Embase (n¼9,532), Scopus
(n¼43), and Web of Science (n¼12,472). After removing 2,164 duplicate records, 21,408 unique records
were screened by title and abstract. Additionally, 11 records were identified through citation searching,
all of which were retrieved and assessed for eligibility, with 10 records excluded. Of these, 21,352 were
excluded as not relevant to the review objectives. 8 studies met the final inclusion criteria and were
included in this systematic review. The full study identification, screening, and inclusion process is illus-
trated in Figure 1 (PRISMA flow diagram).
Characteristics of identified studies
Table 1 showed the characteristics of the identified studies. A total of eight studies met the inclusion cri-
teria, conducted across the United States, predominantly private insurance system (n¼5)17,18,20,22,23;
Europe, including Germany, which has single-payer systems (n¼1)10, and France, which has universal

JOURNALOFMEDICALECONOMICS 657
Figure 1. PRISMA flow diagram of study identification.
health insurance with multiple payers (n¼1)21; and Asia (China ¼ 1)19. Sample sizes ranged from
approximately 50,000 to over 1.4 million individuals, encompassing data sources such as commercial
insurance claims (n¼3)17,18,23, national health insurance databases (n¼3)10,20,21, and electronic medical
records (EMR) (n¼1)19, while one study used retail-level pharmacy transaction records (n¼1)22.
Six studies adopted longitudinal designs (multi-year or time-series forecasting)10,17,18,20,22,23, while two
were cross-sectional cost-regression studies19,21. Table 2 also shows the outcome variables primarily
included: (1) Total annual or per-member-per-month expenditure (n¼5)10,17,18,20,21, (2) Medication-spe-
cific or pharmacy expenditures (n¼3)18,22,23, (3) Preventable cost17, and (4) In-hospital costs (n¼1)19.
In the heart failure population study by Lewis et al. (2021), preventable costs were defined on the
basis of the follow-up period and operationalized using insurance claims data, in which hospitalizations
and emergency department visits classified as potentially avoidable—according to clinical quality indica-
tors and emergency care categorization algorithms—were aggregated into total reimbursed costs17.
Among the eight included studies, only this study explicitly focused on preventable costs as the primary
economic outcome, whereas the remaining studies primarily examined total medical expenditures or in-
hospital costs as the main economic indicators17.
Deep learning architectures varied across studies: feed-forward networks (DNN/MLP; n¼2)10,21,
sequence-based models (LSTM, stacked LSTM, CNN-LSTM, RNN; n¼4)17,18,20,23, hybrid or multi-view net-
works (n¼1)19, and variance-based generative adversarial network (V-GAN; n¼1)22. Comparators
included classical regression approaches—such as GLM, ridge, and LASSO regression
(n¼6)10,17,18,20,21,23—and tree-based machine-learning methods including Random Forest (RF), Gradient
Boosting Machine (GBM), or CatBoost
(n¼4)17,20–22.
Model performance was most commonly
evaluated using R2 or adjusted R2 (n¼5)10,18,20,21,23, MAE (n¼3)18,19,21, RMSE (n ¼ 5)18–20,22,23, and AUC
(n ¼ 2)10,17; several studies additionally reported precision@k, cost-capture, or correlation coefficients
for discrimination and calibration assessment (n¼3)10,17,19.
Clinical and policy contexts of prediction
Based on the comparative models in Table 2, this section shows the methodological frameworks and
model performance of each included study. One U.S. study focused on population health management,
predicting preventable hospitalizations, emergency visits, and expenditures among heart failure patients

658 J.T.LEEETAL.
)deunitnoc(
)yats-nihtiw(lanoitces-ssorC
|     |     |     | )raey-itlum(lanidutignoL |     | )5102–1102(lanidutignoL |     |     |     |     | )raey-itlum(lanidutignoL |     |     |
| --- | --- | --- | ------------------------ | --- | ----------------------- | --- | --- | --- | --- | ------------------------ | --- | --- |
ngisedlaropmeT
)sraey21(lanidutignoL
stneitap;atadsmialclaicremmoc -tneitapfosraeyevifgnisuyduts -niart01/02/07;atadsmialclevel krowemarf)noitciderPnoitazilitU smialcevitartsinimdagnisuyduts doirep-txentciderpotdesuerew
|     | gniledomcitsongorpevitcepsorteR | ,noitadilav,gniniartotnidedivid |     | ;doirepnoitavresbo5102–0102( |     |     |     |     | sweivatadelpitlumgnitargetni |     |     |     |
| --- | ------------------------------- | ------------------------------- | --- | ---------------------------- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- |
fo)7102–6002(sraey21gnisu .)doirepnoitaulave7102–6102 ydutslanoitavresboevitcepsorteR ydutsehT.gninraeldesivrepus ecruoseR(PURehtdecudortni )txetnoitarepo,txetsisongaid trohoclanidutignolevitcepsorteR lacirotsihs’tneitaphcaE.atad
|     |     |                        | desab-noitalupopevitcepsorteR |                           |                              | gnitsacerof-tsoclanidutignol |     |                        |                          |     |                         | snoitacidemdna,serudecorp |
| --- | --- | ---------------------- | ----------------------------- | ------------------------- | ---------------------------- | ---------------------------- | --- | ---------------------- | ------------------------ | --- | ----------------------- | ------------------------- |
|     |     |                        |                               | sdrocersmialclanidutignol |                              |                              |     | rofatadRMEderutcurtsnu |                          |     |                         |                           |
|     |     |                        |                               | dnatnempoleved-ledom      | ,lanoitavresbo,evitcepsorteR |                              |     |                        |                          |     |                         | .serutidnepxe)htnom-21(   |
|     |     | .)1:2:7(stesgnitsetdna |                               | gnisuydutsnosirapmoc      |                              |                              |     |                        | ,serutaefderutcurts.g.e( |     | ,sesongaid,serutidnepxe |                           |
ngisedydutS
|     |     |     |     |     |     |     | dnaderutcurtsgnisu |     |     | .ledomdeifinuaotni |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | ------------------ | --- | --- |
.tilpstset-noitadilav
-nondnalaitneuqes(sehcaorppa stneitap)FH(eruliaftraehgnoma stsocerac-htlaeherutufraey-eno ecnamrofrepstierapmocotdna latothtobrofsledomkramhcneb serutidnepxenoitacidemtneitap gnitamitseyllacificeps,noitazilitu gninraelenihcamfoecnamrofrep laropmetyfitnauqotdemiayduts
gnitciderprofnoissergercitsigol gnidnepserachtlaehdna,stisiv rehtodnanoissergeregdirhtiw egnahc-tsocdnanoitciderptsoc gnitsacerofrof)skrowtenlaruen ,serutidnepxeerachtlaeherutuf dnagniyfitnedinosucofahtiw deen-hgihtsoc-hgihgniganam .sehcaorppanoissergerlacissalc
peedaetaulavednapolevedoT gnitciderprofkrowtenlaruen ,atadsmialclanidutignolmorf ylhtnomdnaylkeewtsacerofoT gninrael-peeddecnavdagnisu gnitsaceroflanoitidarttsniaga fohtgneldnastsoclatipsoh-ni ehT.stneitapdiacideM)NHCH( tsniagasledomgninraelpeed
.noitciderp ,snoitazilatipsohelbatneverp )DE(tnemtrapedycnegreme otdna,sdohtemseires-emit –NNCdedaeh-itlumerapmoc serutcetihcraelbmesneMTSL ecruoserlatipsoh-nitciderpoT kramhcnebotdnagnidneps
|     |                       | lanoitidarthtiw)laitneuqes |     |     |     |     |     | cinortcelegnisu)SOL(yats peedaaivsdrocerlacidem |     |                         | tnerrucergnidulcni(sledom |                         |
| --- | --------------------- | -------------------------- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | ----------------------- | ------------------------- | ----------------------- |
|     | sevitcejbodnamiA      |                            |     |     |     |     |     |                                                 |     |                         |                           | erachtlaehniecnetsisrep |
|     | gninraelpeederapmocoT |                            |     |     |     |     |     |                                                 |     | evitciderpehtetaulaveoT |                           |                         |
.hcaorppagninrael
erutidnepxe
.noitacifitnedi
.sledom
erachtlaeh
eziselpmasdnanoitalupopydutS .S.Uegralani)7102–6102(sraey etatsdna,xes,egaybnoitalupop ,saxeTnistneitapdellorne-diacideM elpmaS.atadsmialclanidutignol fosnoillimdeniatnoctesatadeht
esabatadecnarusnilaicremmoc morfslaudividniderusni643,304,1 sdrocertneitapdegrahcsid000,057 esabatad)RME(sdrocerlacidem -hgihtsoc-hgihdnanoitalupop fosraeylarevesgnisudezylana tub,detroperylticilpxetonezis
|              | owtrofdellorneylsuounitnoc   |     |     | namreGehtfoevitatneserper                    |                        |                                                  | nward,slatipsohesenihCmorf |                            |                           |     |                      |                         |
| ------------ | ---------------------------- | --- | --- | -------------------------------------------- | ---------------------- | ------------------------------------------------ | -------------------------- | -------------------------- | ------------------------- | --- | -------------------- | ----------------------- |
| rof          | eruliaftraehhtiwstluda062,39 |     |     |                                              |                        | 5102lirpAdna1102yraunaJ nacStekraMnevurTehtmorf  |                            | cinortceleelacs-egralamorf | tneitapdna,sedocnoitarepo |     |                      |                         |
|              |                              |     |     |                                              |                        | neewtebsmialcnoitacidem ).S.U(esabatadsretnuocnE |                            |                            |                           |     |                      | fosraeyelpitlumgnirevoc |
|              |                              |     |     | 06>(esabatadfeGnIeht                         |                        |                                                  |                            | ,stxetsisongaidgnidulcni   |                           |     | ,spuorgbus)NHCH(deen | sdrocerrebmemylhtnom    |
| snoitacilppa |                              |     |     | htlaehyrotutatsnamreG ,)7102–0102,secnarusni | htiwstneitap000,05revO | niapdesab-noitpircserp dnasmialClaicremmoC       |                            |                            |                           |     |                      |                         |
lareneghtobgnidulcni
.yrotsiherutidnepxe
.scihpargomed
.ecnediserfo
gninrael
peed
|     | setatSdetinU |     |     |     | setatSdetinU |     |     |     |     | setatSdetinU |     |     |
| --- | ------------ | --- | --- | --- | ------------ | --- | --- | --- | --- | ------------ | --- | --- |
no yrtnuoC
ynamreG
seiduts
anihC
dedulcni
|     | stropeRcifitneicS |     |            |             |                |                      | desaB-egdelwonK |     |     |           |        |     |
| --- | ----------------- | --- | ---------- | ----------- | -------------- | -------------------- | --------------- | --- | --- | --------- | ------ | --- |
|     |                   |     |            | noisiceDdna | fosnoitacilppA |                      |                 |     |     |           |        |     |
|     |                   |     |            | scitamrofnI |                | –gninraeL :41retpahC |                 |     |     |           |        |     |
|     | lanruoJ           |     | lacideMCMB |             |                |                      |                 |     |     | gnEdeMoiB |        |     |
|     |                   |     |            |             |                | enihcaM              | smetsyS         |     |     |           |        |     |
| fo  |                   |     |            | gnikaM      |                |                      |                 |     |     |           | eniLnO |     |
scitsiretcarahC
|     |     |     | .latessoB-ewerD |     |     |     | 91)1202(.lateuY |     |     |     |     |     |
| --- | --- | --- | --------------- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- |
.latekihsuaK
|     | .latesiweL 71)1202( |     |     | 01)2202( |     | 81)0202( |     |     |     | .lategnaY | 02)8102( |     |
| --- | ------------------- | --- | --- | -------- | --- | -------- | --- | --- | --- | --------- | -------- | --- |
.1 elbaT ydutS

JOURNALOFMEDICALECONOMICS 659
|                | raeyelgnis(lanoitces-ssorC                                   |     |                          | gnisuledomgnitsacerof emitelpitlumrevoatad | shtnom84tsrif—ngised          | shtnom21lanif,gniniart .gnitsetrofdesu)5102( |
| -------------- | ------------------------------------------------------------ | --- | ------------------------ | ------------------------------------------ | ----------------------------- | -------------------------------------------- |
|                |                                                              |     | seires-emit,lanidutignoL | erutidnepxelaitneuqes                      |                               | rofdesu)4102–1102(                           |
| ngisedlaropmeT |                                                              |     |                          |                                            | seires-emitlanidutignoL       |                                              |
|                | )6102                                                        |     |                          | .stniop                                    |                               |                                              |
|                | evitartsinimdadetcellocylenituor etarapeS.SDNSmorfatadsmialc |     |                          |                                            | smialcecnarusniyradnocesgnisu |                                              |
-hgihrofdnanoitalupoperitne
|     | gnisuydutsdesab-noitalupop |     |     | -emiterutidnepxenoitpircserp | ydutslanoitavresboevitcepsorteR |     |
| --- | -------------------------- | --- | --- | ---------------------------- | ------------------------------- | --- |
ehtrofdeniarterewsledom
,lanoitces-ssorc,evitcepsorteR
lanoitatupmocevitcepsorteR
| ngisedydutS |     |     |     | gnisuydutsgniledom |     |     |
| ----------- | --- | --- | --- | ------------------ | --- | --- |
.spuorgbustsoc
.atadseires
.atad
ediwnoitangnisustsocerachtlaeh
|     | gninraelenihcamfoecnamrofrep lacissalcahtiwsledom)krowteN | otthguosydutsehT.atadsmialc sniaglufgninaemsreffogninrael |     |     |     |                            |
| --- | --------------------------------------------------------- | --------------------------------------------------------- | --- | --- | --- | -------------------------- |
|     | )MLG(ledoMraeniLdezilareneG                               |                                                           |     |     |     | atsniagaecnamrofreperapmoc |
-noitpircserpanoerutidnepxe
|                  |                                                | enihcamrehtehwenimreted | ninoissergerlanoitidartrevo -ecnairavatsetdnapolevedoT | lairasrevdaevitarenegdesab tahtledom)NAG-V(krowten dnaledomneewtebecnairav | tneitap-repylhtnomtsacerofoT | gnisunoitacidemniapdesab otdna)MTSL(gninraelpeed |
| ---------------- | ---------------------------------------------- | ----------------------- | ------------------------------------------------------ | -------------------------------------------------------------------------- | ---------------------------- | ------------------------------------------------ |
|                  | larueNdnatseroFmodnaR(                         |                         |                                                        | niecnereffidehtseziminim                                                   |                              | ledomlacitsitatslanoitidart                      |
| sevitcejbodnamiA |                                                |                         |                                                        | gnitciderprofatadlautca                                                    |                              |                                                  |
|                  | evitciderpehterapmocoT laudividnignitsacerofni |                         |                                                        |                                                                            |                              |                                                  |
|                  |                                                |                         | .gniledomtsochtlaeh                                    |                                                                            | serutidnepxeenicidem         |                                                  |
.)AMIRA(
| eziselpmasdnanoitalupopydutS | gnisu,)SDNS(metsySnoitamrofnI                             |     |                                 | eziselpmastcaxeeht;noitacidem                             | -noitpircserpagnisahcrupsetatS | detcartxe,noitacidemniapdesab |
| ---------------------------- | --------------------------------------------------------- | --- | ------------------------------- | --------------------------------------------------------- | ------------------------------ | ----------------------------- |
|                              | ehtybderevocnoitalupoplareneG esabatadlanoitanehtfoelpmas |     | niapcificepsagnisahcrupstneitaP |                                                           |                                | –1102(tesatadsmialcecnarusni  |
|                              | modnarevitatneserper79/1a                                 |     |                                 | morfdeviredtubdeificepston sdrocernoitcasnartlevel-liater |                                |                               |
|                              | ataDhtlaeHlanoitaNhcnerF                                  |     |                                 |                                                           | detinUehtnistneitap000,05>     | nacStekraMnevurTehtmorf       |
|                              | .6102raeyehtrof                                           |     |                                 | .)atadseires-emit(                                        |                                |                               |
)5102
|     |     |     | setatSdetinU |     | setatSdetinU |     |
| --- | --- | --- | ------------ | --- | ------------ | --- |
yrtnuoC
ecnarF
|     | lanruoJnaeporuE |     |     |     |     | noecnerefnoC                          |
| --- | --------------- | --- | --- | --- | --- | ------------------------------------- |
|     |                 |     |     |     |     | lanoitanretnI dnagninraeL ecneicSataD |
fosgnideecorP
lanruoJ htlaeHfo scimonocE
|     |     |     | sseccAEEEI |     | EEEIeht | enihcaM |
| --- | --- | --- | ---------- | --- | ------- | ------- |
)SDLM(
.deunitnoC
|     |     |     | .latekihsuaK |     | .latekihsuaK |     |
| --- | --- | --- | ------------ | --- | ------------ | --- |
.latetnomiV
|     | 12)2202( |     |     | 22)0202( | 32)7102( |     |
| --- | -------- | --- | --- | -------- | -------- | --- |
.1 elbaT ydutS

660 J.T.LEEETAL.
|     |     |                           |     |                             |                           | gnisuetipseddetimilniamer edistuonoitadilavlanretxeoN– |                              |                                                  |                       |                                |                                                | )deunitnoc(                                     |
| --- | --- | ------------------------- | --- | --------------------------- | ------------------------- | ------------------------------------------------------ | ---------------------------- | ------------------------------------------------ | --------------------- | ------------------------------ | ---------------------------------------------- | ----------------------------------------------- |
|     |     | desabsemoctuoelbatneverP– |     | oteudycneiciffenilaitnetoP– |                           |                                                        | laicosfonoisulcniticilpxeoN– |                                                  | dnasdaehelpitlumoteud | ;detimilytilibaterpretniledoM– | -htlaehlarenegon(tesatad                       |                                                 |
|     |     |                           |     |                             | dnaytilibaterpretniledoM– | ybdetceffaebyamledoM–                                  |                              | nodedeenhcraeserrehtruF– dnaserutcetihcralamitpo |                       |                                | nevurTmorfserutidnepxe .stnanimretedlaroivaheb | )PAHS.g.e(IAelbanialpxe niseirogetacerutidnepxe |
segnellahcdeifitnedI lanretnimodnardnoyeb dnaycnerapsnartdetimiL– rehtootnoitazilareneg evisnetniyllanoitatupmoC– rolaicosfonoisulcnioN– redaorbnognitsetdna
|     | ,cimonoceoicosfokcaL– | smhtiroglagnitsixeno |     | .wodniwatadraey-11 | peedfoytilibanialpxe noitamitseytniatrecnu | .stneidargdetargetni | gnidocrosnoitaluger | .srotcaflatnemnorivne |     |     | otdetcirtsernoitadilaV– |     |
| --- | --------------------- | -------------------- | --- | ------------------ | ------------------------------------------ | -------------------- | ------------------- | --------------------- | --- | --- | ----------------------- | --- |
RHEdna,yrotarobal dnaytilibaterpretni noitadilavlanretxeoN– .erutcurtselbmesne gnitargetnidetsegguS–
|     |     |                  | yam)IQP,sgnilliB( .stneveyfissalcsim |     |                 | .tesatadfeGnIeht | gnillibnisegnahc |                |             | erutaefraelcskcal | detaler-noitacidem |             |
| --- | --- | ---------------- | ------------------------------------ | --- | --------------- | ---------------- | ---------------- | -------------- | ----------- | ----------------- | ------------------ | ----------- |
|     |     | detimilselbairav |                                      |     | .sledomgninrael |                  |                  | rostnanimreted |             |                   |                    |             |
|     |     | .ssenetelpmoc    |                                      |     |                 |                  |                  |                |             |                   | .)stsocmetsys      |             |
|     |     |                  |                                      |     |                 |                  |                  |                | .sepytonehp |                   |                    | .krowerutuf |
|     |     |                  |                                      |     |                 |                  | .secitcarp       |                |             | .noitubirtta      |                    |             |
.tilps
|     | )NNCdnaMTSLylralucitrap( |                                                                                           |                                                                           | nisnoitnevretnidetegratrof                        | yllaitnatsbuskrowtenpeedehT | egnahc-tsocdnanoitciderp                            | gninraelpeedtahtdelaever | -DCI(sisongaidlufgninaem |                            |                                                    |                                                  |     |
| --- | ------------------------ | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------- | --------------------------- | --------------------------------------------------- | ------------------------ | ------------------------ | -------------------------- | -------------------------------------------------- | ------------------------------------------------ | --- |
|     |                          |                                                                                           | noitazilituroirP.gnidneps DE,SOL,snoitazilatipsoh( erew)yteixna,DKC,DPOC( | detartsnomeD.srevirdyek noitacifitartsksirecnahne |                             | lanoitidartdnanoisserger ecnamrofreP.noitacifitnedi |                          | sedoc)CTA(gurddna)01     | yltnacifingisserutcetihcra | gnitsacerofnissentsubor .serutidnepxelevel-tneitap | mret-trohshtobderutpac gnitsaceroftsocerachtlaeh |     |
|     |                          | citsigolllademrofreptuo dnasenilesabnoisserger rofksirhgihtastneitap dnastneveelbatneverp | seitidibromocdna)stisiv                                                   |                                                   |                             | tsocllarevorofsenilesab                             | regnoldnaatadgniniart    | yllacinilcnoeromdeiler   | .ytilibaterpretnilacidem   | dnaycaruccadevorpmi                                | mret-gnoldnalaropmet                             |     |
gnitanimircsidniMBG nacgninraelpeedtaht regralhtiwdevorpmi .swodniwnoitavresbo decnahnegnitseggus MTSL-NNCdirbyhehT roflaitnetopgniwohs .gninnalpecruoserdna
|     |                    |     |     |     | .eracFHdesab-eulav egdirdemrofreptuo |     | stneidargdetargetnI |                   | elbmesnededaeh-itluM |     | ylevitceffeelbmesne ,seicnednepeddnert |     |
| --- | ------------------ | --- | --- | --- | ------------------------------------ | --- | ------------------- | ----------------- | -------------------- | --- | -------------------------------------- | --- |
|     | sledomgninraelpeeD |     |     |     |                                      |     |                     | ,sedocgnillibnaht |                      |     |                                        |     |
sgnidniF
|     |                                               |                                                |     |     |                          | dna)6212e¼EPAM,062.0                                                  | sv(80.0¼CRPUA:stneitap stsocgnisaerced;)egdir40.0 |     |                     |                                       | senilesablacissalcrodedaeh |     |
| --- | --------------------------------------------- | ---------------------------------------------- | --- | --- | ------------------------ | --------------------------------------------------------------------- | ------------------------------------------------- | --- | ------------------- | ------------------------------------- | -------------------------- | --- |
|     | scirtemecnamrofrepledoM :CORUAtsehgihdeveihca | %34–93:%1pottanoisicerP                        |     |     | EPAM,236.0¼q,725.0¼r     | MPC,662.0¼2R,4002e¼ gnimrofreptuo–623.0¼ roF.)62.0(cid:3)2R(ASR-ibroM | gnisaercni-tsocgniyfitnedi                        |     |                     | –3(cid:3)EPAM,201(cid:4)5.3(cid:3)EAM |                            |     |
|     |                                               | ,)snoitazilatipsoh(877.0 citsigolrof%51–21.sv( |     |     | :)elbmesne(krowtenlarueN |                                                                       |                                                   |     |                     |                                       |                            |     |
|     | gninraeLpeeDlaitneuqeS                        | 727.0,)stisivDE(186.0                          |     |     |                          | ¼2R(noissergeregdir                                                   | 12.0sv(42.0¼CRPUA                                 |     | MTSL-NNCelbmesneehT | -elgnisllademrofreptuotI              |                            |     |
|     |                                               |                                                |     |     |                          |                                                                       |                                                   |     |                     | .39.0–19.0(cid:3)2R,%4                | .)NNC,MTSL,AMIRA(          |     |
tsebehtdeveihca
:ecnamrofrep
.)noisserger
|     |                          | .)stsoc(                                    |                                               |     |                        |                                           |                     | .)egdir |                         |                                      |     |     |
| --- | ------------------------ | ------------------------------------------- | --------------------------------------------- | --- | ---------------------- | ----------------------------------------- | ------------------- | ------- | ----------------------- | ------------------------------------ | --- | --- |
|     | gnitaulaverofdesuscirteM | .)stsoc(727.0,)stisivDE( ehtrednUaerA(CORUA | noisicerP,)citsiretcarahC erutpaCtsoCdna,)%01 |     |                        |                                           |                     |         | ,)EAM(rorrEetulosbAnaeM |                                      |     |     |
|     | gninraeLpeeDlaitneuqeS   | 186.0,)snoitazilatipsoh(                    |                                               |     |                        | noitciderPs’gnimmuC llaceR–noisicerPrednu | egnahc-tsocrofCORUA |         |                         |                                      |     |     |
|     | ecnamrofrepledom         |                                             | –1(%kpotta)eulaV                              |     | naeM,)q(namraepS       | aerA,)MPC(erusaeM                         |                     |         | derauqSnaeMtooR         | egatnecrePetulosbA 2Rdna,)EPAM(rorrE |     |     |
|     |                          | gnitarepOrevieceR                           | evitciderPevitisoP(                           |     | ,)r(noitalerrocnosraeP | noitciderPetulosbA ,2R,)e,EPAM(rorrE      | dna)CRPUA(evruc     |         |                         | naeM,)ESMR(rorrE                     |     |     |
tsehgihdeveihca
|             |                             |                                                    |                          |          |                           |                          |                                                                  |     |                          | fotneiciffeoC(             | .)noitanimreteD |     |
| ----------- | --------------------------- | -------------------------------------------------- | ------------------------ | -------- | ------------------------- | ------------------------ | ---------------------------------------------------------------- | --- | ------------------------ | -------------------------- | --------------- | --- |
|             |                             | 877.0:CORUA                                        |                          |          |                           |                          | .noitacifissalc                                                  |     |                          |                            |                 |     |
| .noitciderp |                             |                                                    |                          | .%kpotta |                           |                          |                                                                  |     |                          |                            |                 |     |
| erutidnepxe | ledomehtnidedulcniserutaeF  | -ataddna)sdnertnoitazilitu ceV2droWgnisusmialcmorf |                          |          | repsmialcfonoitatneserper | gurdCTA,sesongaidMG-01   | erutaeflanoisnemid-420,333                                       |     |                          |                            |                 |     |
|             | serutaefnevird-egdelwonk939 | ,serudecorp,seitidibromoc                          |                          |          |                           | -DCI:)sretrauq42(retrauq |                                                                  |     |                          | noitazilitugurd,srotacidni |                 |     |
|             |                             | detarenegserutaefnevird                            | laitneuqeshtob,seirotsih |          |                           | ytlaicepsnaicisyhp,sedoc |                                                                  |     | ,redneg,ega(scihpargomeD | ytidibromoc,snoitpircserp  |                 |     |
|             |                             |                                                    |                          |          |                           | gnillibPOG,serudecorp    | dna,ega,xes,)GF(syek !stsoccificeps-rotces retfatneitapreprotcev |     |                          |                            |                 |     |
raey-11(sgniddebme .)laitneuqes-nondna
|     |     | ,stsoc,snoitacidem |     |     |     |     |     | .gniretlifycneuqerf | forebmun,)noiger | suoiverpdna,setar .sdnerterutidnepxe |     |     |
| --- | --- | ------------------ | --- | --- | --- | --- | --- | ------------------- | ---------------- | ------------------------------------ | --- | --- |
SPO,GRD,sedoc
,scihpargomed(
lanoisnemid-hgiH
erachtlaeh
| rof | derapmocledomrehtO stnairavowt(noisserger | .)MBG(ledoMgnitsooB |     |     |     |     |     |     | detargetnIevissergeRotuA |     |     |     |
| --- | ----------------------------------------- | ------------------- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- |
;)serutaefdetimilhtiw
tneidarG;)serutaef
| sledom |                     | citsigoldecnahnE |     |     |     |     |     |     |               |     |     |     |
| ------ | ------------------- | ---------------- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- |
|        | citsigollanoitidarT | 939(noisserger   |     |     |     |     |     |     | egarevAgnivoM |     |     |     |
noissergeregdiR
)AMIRA(
lacissalc
tuopord,noitavitcaULeR
|          | epytledomgninraelpeeD :gninraeLpeeDlaitneuqeS |                                                                            | drawroF-deeF:gninraeL |     | reyalitlumdetcennoc-ylluF | ,hcaesnoruen05,sreyal                 |     |     | dedaeH-itluM/)MTSLHM( |                                    |     |     |
| -------- | --------------------------------------------- | -------------------------------------------------------------------------- | --------------------- | --- | ------------------------- | ------------------------------------- | --- | --- | --------------------- | ---------------------------------- | --- | --- |
| dna      |                                               | htiw)MTSL(yromeM ;msinahcemnoitnetta larueNlanoitulovnoC -noN.)NNC(krowteN | .)NNF(krowteNlarueN   |     | neddih4(nortpecrep        | ,rezimitpoMADA,52.0 .)snur5foelbmesne |     |     |                       | dirbyH/)NNCHM(NNC elbmesneMTSL-NNC |     |     |
|          | mreT-trohSgnoL                                |                                                                            |                       |     |                           |                                       |     |     |                       | ledomMTSLdekcatS                   |     |     |
| gninrael |                                               | peeDlaitneuqes                                                             |                       |     |                           |                                       |     |     | MTSLdedaeH-itluM      |                                    |     |     |
peed
| fo       | snoitazilatipsohelbatneverP | -6(stisivDEelbatneverP                                  |     |     |                                              |                     |     |     |                      |                     |     |     |
| -------- | --------------------------- | ------------------------------------------------------- | --- | --- | -------------------------------------------- | ------------------- | --- | --- | -------------------- | ------------------- | --- | --- |
|          | .g.e(elbairavemoctuO        |                                                         |     |     | erac-htlaehraey-enolatoT tsocdna)soruE(stsoc | esaercedroesaercni( |     |     |                      | emitrepserutidnepxe |     |     |
| sgnidnif |                             | )2(;)nozirohhtnom )3(;)nozirohhtnom -1(stsocelbatneverP |     |     |                                              | neewtebdlof-001>    |     |     |                      |                     |     |     |
|          | )elbairavtegrat             | -6(snoitazilatipsoh                                     |     |     |                                              | seirogetacegnahc    |     |     | level-tneitapegarevA |                     |     |     |
|          | elbatneverP)1(              |                                                         |     |     |                                              |                     |     |     |                      | /ylkeew(doirep      |     |     |
ro(erachtlaeh
|     |     |     | )nozirohraey |     |     |     |     |     |     | )noitacidem |     |     |
| --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | ----------- | --- | --- |
.)ylhtnom
.)sdoirep
evitarapmoC
71)1202(.latesiweL
.latessoB-ewerD
.latekihsuaK
.2 01)2202( 81)0202(
elbaT
ydutS

|     |     |     |     |     |     |     |     | JOURNALOFMEDICALECONOMICS |     |     | 661 |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- |
)deunitnoc(
-itlumfotsoclanoitatupmoC– otnithgisnidetimilsedivorp tceffaserutaeflautxetwoh gnissimoteudsaiblaitnetoP– sisylanaytiuqerossenriafoN– eudFRnignittifrevoelbissoP– detimilniamerycnerapsnart otezilarenegtonyamstluseR– rosmetsyserachtlaehrehto
|     |     | peedksat-itlumdnaweiv PUR:ytilibanialpxedetimiL– | slatipsohssorcanoitadilav | RMEssorcaseicnetsisnocni | xob-kcalb(stuptuoledom cimonoceoicosfoecnesbA– |     |     |     | elpmasllamsotdetubirtta .noitazimitpodetimildna | .)ylnoatadlanoitces-ssorc( |     |
| --- | --- | ------------------------------------------------ | ------------------------- | ------------------------ | ---------------------------------------------- | --- | --- | --- | ----------------------------------------------- | -------------------------- | --- |
segnellahcdeifitnedI dnaycnerapsnartfokcaL– -smialcdnoyebselbairav evisnetniyllanoitatupmoC– .gninutretemaraprepyh serutaeflaropmetfokcaL– dnaytilibanialpxeledoM–
|     | ytilibazilarenegdetimiL– RMEesenihCdnoyeb |                   |                    |     | NNRniytilibaterpretni | ytilibazilarenegdetimiL– diacideMehtedistuo |                    |     |                  |                                      |     |
| --- | ----------------------------------------- | ----------------- | ------------------ | --- | --------------------- | ------------------------------------------- | ------------------ | --- | ---------------- | ------------------------------------ | --- |
|     |                                           |                   |                    |     |                       |                                             | detimildnagniniart |     |                  | .teselbairavegralot .sehcaorppaLMrof |     |
|     |                                           | .gniniartgninrael | lanretxefoecnesbA– |     |                       |                                             |                    |     | ecnamrofreprednu |                                      |     |
.serutaefdesab
|     |     |     |              | gnidocroatad |     |     |                          |     | krowtenlarueN– |     | .serutcurtstsoc |
| --- | --- | --- | ------------ | ------------ | --- | --- | ------------------------ | --- | -------------- | --- | --------------- |
|     |     |     | .snoitciderp | .seirtnuocro |     |     | .noitalupop fonoissucsid |     |                |     |                 |
.)noitatimil
|     | .smetsys                  |                                                 |                                                     |     | .smetsys                                 |                                                                     | .dedulcni                                          |                                                    |                                                              |                       |     |
| --- | ------------------------- | ----------------------------------------------- | --------------------------------------------------- | --- | ---------------------------------------- | ------------------------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------ | --------------------- | --- |
|     |                           | ytilibapacstignitartsnomed                      | sawnoisufdesab-noitnetta                            |     | deen-hgihtsoc-hgihgnoma                  |                                                                     | gnithgilhgih,)MBG(sledom oslatI.noitciderpgnidneps | erew)seirotcejartgnidneps citatsnahtevitciderperom |                                                              | :krowteNlarueN–;.%85¼ |     |
|     | gninraelpeedweiv-itlumehT | desab-eertdnanoisserger ,scirtemllassorcasledom | .ylevitceffeatadderutcurts /sisongaidfonoisulcniehT |     | ylralucitrap,serutidnepxe                | ledomNNRehT.stneitap raeniL,OSSAL(noisserger elbmesnedna)noissergeR | laropmettahtdezisahpme                             |                                                    | RiH,833,1e¼EAM,574.0 ¼2R-jda:MLG–;.%76¼ RiH,536,1e¼EAM,743.0 |                       |     |
|     | lanoitidartdemrofreptuo   | dnalautxetetargetniot                           | ecnamrofreproflacitirc                              |     | niecnetsisreplaropmet                    |                                                                     |                                                    | roscihpargomedtneitap                              | ¼2R-jda:tseroFmodnaR–                                        | ¼EAM,613.0¼2R-jda     |     |
|     |                           |                                                 |                                                     |     |                                          | lacissalcdemrofreptuo                                               | rofgninraellaitneuqes                              |                                                    |                                                              |                       |     |
|     |                           |                                                 | dnastxetnoitarepo                                   |     | gnortsdnuofydutsehT erachtlaehlaudividni |                                                                     | erachtlaehcimanyd tnecer.g.e(serutaef              |                                                    |                                                              | .%55¼RiH,066,1e       |     |
fosegatnavdaeht
sgnidniF )PUR(hcaorppa
.sesongaid
.sniag
|     |     |     | eht,FRdnaMBGotderapmoC |     |     |     |     |     | ,574.0fo2R-jdanadeveihcaFR fo2R-jdanadahMLG;%76 | krowtenlaruen;%85foRiH EAM,613.0fo2R-jdanadah |     |
| --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | ----------------------------------------------- | --------------------------------------------- | --- |
scirtemecnamrofrepledoM ledomgninraelpeedPURehT llanahtrewolyltnacifingis seulavderauqs-R.ycarucca NHCHrofrorrenoitciderp ehtotderapmocstneitap gniwohs,sdoireptsocroirp -emiterutpacotytilibasti foRiHdna,8331efoEAM dna,5361efoEAM,743.0 %55foRiHdna,0661efo
|     |     |                      |                 |     | dnaMBGdemrofreptuoNNR | NNR.noitalupoplareneg 4–3gnitaroprocninehw | .snrettaptsoctnedneped |     |     |     |     |
| --- | --- | -------------------- | --------------- | --- | --------------------- | ------------------------------------------ | ---------------------- | --- | --- | --- | --- |
|     |     | dnatsocrof58.0>:CCP– |                 |     | rewol;7.0nahtretaerg  | devorpmiecnamrofrep                        |                        |     |     |     |     |
|     |     | .)100.0<p(senilesab  | decuderledomPUR |     | noitciderpniOSSAL     |                                            |                        |     |     |     |     |
ybrorrenoitciderp
,)tsoc(396.0:ESMR–
.SOLrof08.0>
|     |     | .154.0:EAM– | .%51–21(cid:5) |     |     |     |     |     |     |     |     |
| --- | --- | ----------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
:deveihca
| gnitaulaverofdesuscirteM |     |     |     |     |     |     |     |     | ,)2R-jda(derauqs-RdetsujdA |     |     |
| ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- |
rorrEderauqSnaeMtooR etulosbAnaeM,)ESMR( naeMtooR,)2R(derauqs-R ,)ESMR(rorrEderauqS egatnecrepeht—)RiH( nislaudividnitsoc-hgih lautcafoelicedpoteht
ecnamrofrepledom nosraeP,)EAM(rorrE rorrEetulosbAnaeM oitaRtiHdna,)EAM( deifitnediyltcerrocfo
|     |     |     |     |     | fonosirapmocdna ssorcasnoitubirtsid |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- |
.)CCP(tneiciffeoC
rorrenoitciderp
.erutidnepxe
noitalerroC
.sledom
ledomehtnidedulcniserutaeF ,snrettapnoitazilitudnatsoc )shtnom4–1fosgal(sdoirep ,)gnigami,snoitacidem,syats
|     |                         | ,sutatsegrahcsid,srotacidni                      |                                                                     | ,srotacidnilevel-tnemtraped .sedocpuorgecruoserdna | sisongaid(serutaeflacinilc lacirotsih,)esunoitacidem | .srotacidniytidibromocdna | etaulaveotdedulcnierew |     |                                               |                         |     |
| --- | ----------------------- | ------------------------------------------------ | ------------------------------------------------------------------- | -------------------------------------------------- | ---------------------------------------------------- | ------------------------- | ---------------------- | --- | --------------------------------------------- | ----------------------- | --- |
|     | noitarepo,epytnoissimda | sisongaidnoissimdadna sisongaiD:atadderutcurtsnU | morfstxetnoitarepodna drowaivdedocnesRME detagerggA:serutaefdevireD |                                                    | scitsiretcarahccihpargomeD ,sedocerudecorp,sedoc     | elpitlumrevostsocroirP    |                        |     |                                               |                         |     |
|     | ,xes,egA:atadderutcurtS |                                                  |                                                                     |                                                    |                                                      |                           |                        |     |                                               | latipsoh,snoitatlusnoc( |     |
|     | ,tnemtrapedlatipsoh     |                                                  |                                                                     |                                                    | ,)noiger,redneg,ega(                                 |                           | .ecnetsisreplaropmet   |     | gnitsixe-erp,redneg,egA noitazilituerachtlaeh |                         |     |
|     |                         |                                                  |                                                                     |                                                    |                                                      |                           |                        |     | noslrahC,snoitidnoc ,xedniytidibromoc         | latotraey-roirpdna      |     |
|     |                         |                                                  | ,stnuocnoitarepo                                                    |                                                    |                                                      |                           |                        |     |                                               | .stsocerachtlaeh        |     |
.sgniddebme
.edoc
)MBG(enihcaMgnitsooB
|                    |                       | 5M,)TD(eerTnoisiceD                  |     |     | dna,noissergeROSSAL                    |                     |     |     |                                            |     |     |
| ------------------ | --------------------- | ------------------------------------ | --- | --- | -------------------------------------- | ------------------- | --- | --- | ------------------------------------------ | --- | --- |
| derapmocledomrehtO |                       | modnaR,eerTledoM tneidarG,)FR(tseroF |     |     | tsniagadekramhcneb                     | atadlacitnedirofNNR |     |     | ledoMraeniLdezilareneG golhtiwnoitubirtsid |     |     |
|                    | ,)RL(noissergeRraeniL |                                      |     |     | ,)RL(noissergeRraeniL lla–)MBG(enihcaM |                     |     |     |                                            |     |     |
|                    | ,)RVS(noissergeR      |                                      |     |     | gnitsooBtneidarG                       |                     |     |     | modnaRdna)knil                             |     |     |
|                    | rotceVtroppuS         |                                      |     |     |                                        |                     |     |     | ammag()MLG(                                |     |     |
.)FR(tseroF
.stilps
roirpfoshtnomelpitlum .atadnoitazilitudnatsoc
epytledomgninraelpeeD asenibmoc–)krowten noitnettaþgniddebme suoenegoreteherutpac weivhcaE.secruosatad saw)txetnoitarepo,txet dnayletarapesdedocne .noisufdesab-noitnetta raenilnonhtiwkrowteN level-tneitapnodeniart
|     |                      | gnisu(redocnedrocer otrotciderpecruoser | sisongaid,derutcurts( |                   | krowteNlarueNtnerruceR ycnednepedlaropmet |     |     |     |                      |     |     |
| --- | -------------------- | --------------------------------------- | --------------------- | ----------------- | ----------------------------------------- | --- | --- | --- | -------------------- | --- | --- |
|     | ,weiv-itlum(ledomPUR | adna)smsinahcem                         |                       | hguorhtdetargetni |                                           |     |     |     | ,snoitcnufnoitavitca |     |     |
|     |                      |                                         |                       |                   | ssorcanoitamrofni                         |     |     |     | larueNdrawrof-deeF   |     |     |
|     | laruenksat-itlum     |                                         |                       |                   | gnirutpac,)NNR(                           |     |     |     |                      |     |     |
ecneuqesdna
.setairavoc
|                      | -ni:stegratsuounitnocowT dna)YNC(stsoclatipsoh | ksat-itlumaivdetciderp |     |     | erutuflatotgnitneserper              |     |     |     |                       |     |     |
| -------------------- | ---------------------------------------------- | ---------------------- | --- | --- | ------------------------------------ | --- | --- | --- | --------------------- | --- | --- |
| .g.e(elbairavemoctuO | .)syad(yatsfohtgnel                            |                        |     |     |                                      |     |     |     | erutidnepxeerachtlaeh |     |     |
|                      |                                                |                        |     |     | htnoMrePrebmeMreP elbairavsuounitnoc |     |     |     | suounitnoc(6102ni     |     |     |
|                      | )elbairavtegrat                                | yltniojerewhtoB        |     |     | erachtlaeh)MPMP(                     |     |     |     | .)sorueni,elbairav    |     |     |
.tneitapreptsoc
|     |     |     |     |     | —erutidnepxe |     |     |     | laudividnilaunnA |     |     |
| --- | --- | --- | --- | --- | ------------ | --- | --- | --- | ---------------- | --- | --- |
.gninrael
.deunitnoC
02)8102(.lategnaY
91)1202(.lateuY
.2 .latetnomiV 12)2202(
elbaT
ydutS

.deunitnoC
.2 elbaT
segnellahcdeifitnedI
sgnidniF
scirtemecnamrofrepledoM
gnitaulaverofdesuscirteM
ledomehtnidedulcniserutaeF
derapmocledomrehtO
epytledomgninraelpeeD
.g.e(elbairavemoctuO
ydutS
ecnamrofrepledom
)elbairavtegrat
lanretxefoecnesbA–
krowemarfNAG-VehT
tsewolehtdeveihcaNAG-VehT
rorrEerauqSnaeMtooR
dnascihpargomedtneitaP
,)RL(noissergeRraeniL
evitareneGdesaB-ecnairaV
erutidnepxeegarevayliaD
.latekihsuaK
raelcnudnanoitadilav
decuderyllufsseccus
llaotderapmocESMR
)ESMR(
/esahcruplacirotsih
gnitsooBtneidarG
-V(krowteNlairasrevdA
niapcificepsano
22)0202(
ehtfossenevitatneserper
seicnapercsidecnairav
,sledomkramhcneb
seires-emiterutidnepxe
)RBG(noissergeR
nagnitargetni)NAG
.noitacidem
–tesatadnoitacidem
detarenegdnalaerneewteb
roirepusgnitartsnomed
lacinilcfonoitnemon;atad
rotarenegdesab-MTSL
elgnisaotdetimil
,snoitubirtsiderutidnepxe
tcaxE(.ycaruccaevitciderp
setairavoccimonoceoicosro
desab-NNCadna
tsocdnaaeracituepareht
lanoitidartgnimrofreptuo
yllaciremuntonESMR
reyalitluM.rotanimircsid
fokcal–epyt
peeddnanoisserger
tubtxetnidetroper
dna,)PLM(nortpecreP
lacinilcdnacimonoceoicos
,MTSL(senilesabgninrael
laminimehtsadetacidni
-trohSgnoLdradnats
stcirtserserutaef
devorpledomehT.)PLM
).srotarapmocgnoma
)MTSL(yromeMmreT
redaorbotytilibazilareneg
rofevitceffeylralucitrap
krowten
–gnidnepserachtlaeh
yranoitats-nongniledom
tonytilibaterpretniledom
erutidnepxeerachtlaeh
.dessucsid
.seires
etairavinuotdetimilledoM–
sledomMTSLhtoB
¼2R,558.61¼ESMR:AMIRA
rorrEerauqSnaeMtooR
foatadseires-emitetairavinU
evissergeRotuA(AMIRA
MTSL)allinav(dradnatS)1(
tneitapylhtnomegarevA
.latekihsuaK
on(gnitsacerof
.AMIRAdemrofreptuo
5408.0
)ESMR(
noitacidemylhtnom
gnivoMdetargetnI
reyalneddihenohtiw
anoerutidnepxe
32)7102(
rocihpargomed
ehtdeveihcaMTSLdekcatS
yromem7(MTSLdradnatS
fotneiciffeoC(2R
cihpargomed;serutidnepxe
)kramhcneb,egarevA
)2(dna)sllecyromem7(
noitacidemniapcificeps
.)setairavoccimonoceoicos
.ecnamrofrepevitciderptseb
¼2R,716.41¼ESMR:)sllec
)noitanimreteD
,redneg,ega(selbairav
owthtiwMTSLdekcatS
,gnidnepstekcop-fo-tuo(
noitadilavlanretxefokcaL–
,tsuboreromerewsMTSL
8408.0
erew)raeyhtrib,noiger
yromem4(sreyalMTSL
diap-rerusnignidulcxe
rosepytnoitacidemssorca
rettebdna,cirtemarapnon
yromem4þ4(MTSLdekcatS
nidesutontubelbaliava
.)hcaesllec
.)tnuoma
desabstluseR–.snoitalupop
laropmetgnirutpacta
¼2R,396.31¼ESMR:)sllec
rofdesoporp(sledomniam
yrogetacgurdelgnisano
:noitacilpmI.seicnedneped
9518.0
.)krowetairavitlumerutuf
gnitimil,)noitacidemniap(
troppusdluocsMTSL
,ega(elbaliavascihpargomeD
.ytilibazilareneg
nisksatgnitsacerof
,)raeyhtrib,noiger,redneg
desoporpkrowerutuF–
dnaerutidnepxeerachtlaeh
niamnidesutontub
etairavitlumgnipoleved
.gnikamycilop
krowerutuf(sledom
gnitaroprocnisledomMTSL
etairavitlumdesoporp
dnascihpargomed
)sledom
elpitlumotgnidnapxe
rofseirogetacnoitacidem
tsocerachtlaehredaorb
.gnitsacerof
662 J.T.LEEETAL.

JOURNALOFMEDICALECONOMICS 663
using LSTM and CNN models to support risk stratification and care coordination under value-based care
frameworks17. Two studies from Germany and France examined risk adjustment and insurance premium
prediction, using large national claims datasets to forecast annual healthcare costs and assess whether
deep or tree-based models improved fairness and predictive accuracy in reimbursement and capitation
formulas10,22. Both were conducted within statutory health insurance systems, emphasizing model trans-
parency and calibration for regulatory use10,21. A U.S. Medicaid study analyzed high-need, high-cost
(HCHN) populations, applying recurrent neural networks to predict per-member-per-month expendi-
tures20. A Chinese study using electronic medical records focused on hospital resource utilization, pre-
dicting in-hospital costs and length of stay with a multi-view DNN that combined structured and
unstructured clinical data19. This work supports hospital efficiency improvement and DRG-based pay-
ment reform, linking predictive analytics to provider-level financial management19. Finally, three U.S.
studies addressed pharmaceutical expenditure forecasting, using claims or retail transaction data to pre-
dict weekly, monthly, or daily medication spending18,22,23.
Neural network architectures in the included studies
Neural network architectures were applied according to input type and temporal structure. Feedforward
deep neural networks handled static or high-dimensional features, capturing nonlinear relationships in
cross-sectional data. Recurrent networks (RNNs/LSTMs) modeled temporal dependencies in longitudinal
or multi-wave sequences. More complex architectures—including hybrid CNN-LSTM models, multi-head
ensembles, and generative frameworks (V-GANs)—were used for heterogeneous or non-stationary data,
integrating structured and unstructured inputs.
Across the studies, neural network design generally reflected data characteristics (see Table 3).
Feedforward DNN models were applied to static features21, while Vimont et al., 202221 included a simple
neural network alongside statistical models for comparison. Recurrent architectures captured temporal
dependencies when explicitly implemented, with convolutional neural networks (CNNs) and fully con-
nected networks (FCNs) used to process spatial and static features, respectively (e.g. Lewis et al. 202117)
Hybrid or generative models addressed complex temporal or heterogeneous inputs (Kaushik et al.
201723; 202022; Yu et al. 202119) However, some studies (e.g. Yang et al. 201820) primarily relied on tradi-
tional machine learning approaches.
Evaluation frameworks and performance metrics
All eight studies evaluated model performance using quantitative metrics aligned with their clinical or
policy objectives10,17–23. Six studies employed internal multi-split validation (train–validation–test or
cross-validation)17–19,21–23, while two—Drewe-Boss et al. (2022) and Yang et al. (2018)—used temporal
holdout samples to assess generalizability10,20. None performed full external validation across independ-
ent datasets.
Longitudinal prediction studies (n¼6)—Drewe-Boss et al. (2022), two studies from Kaushik et al.
(2020), Kaushik et al. (2017), Yang et al. (2018), and Lewis et al. (2021)—focused on forecasting accuracy
and discrimination10,17,18,20,22,23. Most reported RMSE (n¼4)18–20,22,23 and some reported MAE
(n¼2)10,18 and R2 or correlation coefficients (r, q) to quantify fit. Lewis et al. (2021) also included
AUROC, precision@k, and cost-capture to evaluate high-risk identification17, while Drewe-Boss et al.
Table 3. Neural network architectures applied in the included studies.
Neuralnetworkarchitecture Datatype Models Studies
Feedforward/DNN Staticorhigh-dimensionaldata Standarddeepneuralnetwork Drewe-Bossetal.202210
Simpleneuralnetwork Staticorhigh-dimensionaldata Simpleneuralnetwork Vimontetal.,202221
(comparisonwithstatistical
models)
Recurrent Longitudinalortime-dependent RNN,LSTM(auxiliary:CNN,FCN) Lewisetal.202117
data
Hybrid/generative Complextemporalpatterns, Hybridorgenerativemodels Kaushiketal.201723;202018;
heterogeneousdata (e.g.V-GAN) 202022;Yuetal.202119

664 J.T.LEEETAL.
(2022) and Kaushik et al. (2020) added AUPRC and Mean Absolute Percentage Error (MAPE), respectively,
for trend and cost-change detection10,18. Sequential models such as LSTM and CNN-LSTM were assessed
primarily on temporal forecasting stability and error reduction18,23.
Cross-sectional studies (n¼2)—Vimont et al. (2022) and Yu et al. (2021)—emphasized model fit and
numerical error for static cost prediction19,21. Vimont et al. (2022) used adjusted R2, MAE, and Hit Ratio
to compare neural networks with GLM and Random Forest for national reimbursement modeling21. Yu
et al. (2021) evaluated RMSE, MAE, and Pearson correlation coefficient for in-hospital cost and length-of-
stay prediction19.
Across all papers, R2/adjusted R2 (n¼5), MAE (n¼4), RMSE (n¼5), and AUC or related discrimination
metrics (n¼2) were most frequently reported10,17–23. Only one study addressed calibration to a limited
extent19, and none included decision-curve, net-benefit, or fairness analyses.
Explainability frameworks such as Integrated Gradients was carried out in Drewe-Boss et al. (2022)10.
Comparative performance of neural networks versus classical models
Across studies comparing neural architectures with classical regression and ensemble methods, neural
models generally performed best when applied to longitudinal or temporally rich healthcare
data10,17–23.
Recurrent and hybrid architectures captured temporal persistence and nonlinear dynamics that tradi-
tional approaches often missed. In a U.S. Medicaid study, Yang et al. (2018) showed that, for predicting
raw Per Member Per Month (PMPM) dollar amount expenditures, a recurrent neural network increased
test R2 from about 0.14–0.17 (for linear regression and GBM) to 0.30 and reduced RMSE by roughly one-
third, with similar improvements in RMSE among the top 10% highest-cost patients; on log- and per-
centile-transformed outcomes, R2 differences across models were smaller, but the RNN still achieved
lower overall and high-cost error.20 Kaushik et al. (2017) likewise found that stacked LSTMs improved
RMSE by nearly 19% over ARIMA forecasts for a medication-spending time series23, while a later multi-
headed CNN–LSTM, Convolutional LSTM, and CNN-LSTM ensemble achieved even stronger performance
with R2 values around 0.8–0.9 in patient-level forecasting18. Lewis et al. (2021) also reported that sequen-
tial deep models outperformed gradient boosting and logistic regression in predicting preventable hos-
pitalizations and costs, attaining AUROCs up to approximately 0.78.17
The picture was more mixed in cross-sectional cost prediction. In a French nationwide claims study,
Vimont et al. (2022) found that a relatively shallow two-hidden-layer MLP performed similarly to a gener-
alized linear model but was clearly outperformed by a random forest (adj-R2 0.475 vs.0.347 and 0.316
for GLM and neural network; MAE e1,338 vs. e1,635 and e1,660), suggesting limited benefit of shallow
neural architectures on tabular cost data21. By contrast, in China, Yu et al. (2021) demonstrated that
when rich structured and textual EMR inputs were available, a multi-view deep learning model integrat-
ing diagnosis and operation text with structured features clearly surpassed all regression and tree-based
baselines, reducing prediction error by roughly 12–15%.19
Figure 2 illustrates roughly how predictive performance evolves as data become richer and more com-
plex. The x-axis moves from simple cross-sectional claims to increasingly heterogeneous, longitudinal, and
multimodal data; the y-axis represents relative model performance. Classical regression performs well for
simple, low-dimensional tabular inputs but tends to plateau as complexity increases. Tree-based machine-
learning models (e.g. random forests, gradient boosting) extend performance by capturing nonlinearities,
typically outperforming regression across most settings. It is important to note that Figure 2 is a concep-
tual framework developed to synthesize the evidence reviewed in this study and to illustrate the proposed
Complexity–Performance Hypothesis24. The figure is intended to visualize the overall performance trends
of different model families as data complexity increases and does not represent empirical estimates
derived directly from any individual study.
Shallow feed-forward neural networks (green) show the weakest performance in the cross-sectional
regime—consistent with Vimont et al. (2022), where a two-layer MLP achieved an adjusted R2 of only
0.316, below both RF (0.475) and GLM (0.347)21. Without sequential structure or rich feature representa-
tions, shallow networks offer limited advantage over traditional methods. However, deep neural architec-
tures (red) behave differently. Even in cross-sectional settings, when richer input modalities are
available—as in the multi-view RUP model using structured and textual EMR features (Yu et al. 2021)—

JOURNALOFMEDICALECONOMICS 665
Figure 2. Model performance by data complexity.
deep learning can clearly outperform both regression and tree-based baselines.19 As data become
increasingly high-dimensional, sequential, or multimodal, deep networks benefit from their higher cap-
acity and representation learning capabilities. This produces the strongest gains in the longitudinal/
multimodal regime, where studies such as Lewis et al. (2021), Yang et al. (2018), Kaushik et al. (2017/
2020), and Kaushik et al. (2020V-GAN) show that recurrent, convolutional, and hybrid deep models out-
perform classical and ensemble methods by substantial margins17,18,20,22,23.
Building on these findings, we formulate what we term the Complexity–Performance Hypothesis,
which posits that model accuracy is maximized when the capacity of the modeling approach is matched
to the complexity of the data. When data are simple and homogeneous, classical regression performs
competitively, reflecting its efficiency in low-dimensional settings. As data gain nonlinear structure or
moderate dimensionality, tree-based machine-learning methods begin to offer clear advantages by cap-
turing interactions and flexible decision boundaries. With further increases in data richness—such as
large-scale, temporal, or multimodal inputs—DNN models provide the greatest performance gains, often
surpassing alternative approaches by a wide margin.
Discussion
Primary findings
Across the eight included studies, deep learning models demonstrated consistent performance gains
over classical regression, though the magnitude and nature of improvement varied by study design and
data type. The strongest advantages were observed in longitudinal analyses, while cross-sectional appli-
cations yielded smaller or mixed results. These results provide empirical support for the Complexity–
Performance Hypothesis, which proposes that predictive accuracy depends on how well a model’s archi-
tecture is matched to the underlying structure and complexity of the data.
In longitudinal or time-series prediction tasks, such as forecasting healthcare expenditures, hospitaliza-
tions, or medication costs, neural networks with sequential structures—particularly LSTM and CNN-
LSTM—achieved notable accuracy improvements, typically showing roughly 10–20% lower prediction
error (RMSE or MAE) and absolute R2 improvements of about 1–15 percentage points compared with
classical regression or autoregressive models. These architectures effectively captured temporal persist-
ence, nonlinear cost dynamics, and patterns of high-cost episodes that static models failed to represent.
In contrast, cross-sectional models predicting single-year or aggregated costs showed more limited
improvements. Shallow feed-forward neural networks performed similarly to or worse than classical
regressions—while tree-based methods such as random forests and gradient boosting often matched or
exceeded neural performance in overall fit and calibration. However, when unstructured or multimodal
inputs such as EMR text were incorporated, deep learning achieved clearer advantages, yielding larger

666 J.T.LEEETAL.
error reductions and demonstrating greater flexibility in modeling heterogeneous clinical information.
Taken together, these findings suggest that deep learning delivers its greatest advantages in settings
with temporal depth or multimodal complexity, whereas classical and ensemble methods can remain
competitive—or superior—when the task is cross-sectional and inputs are purely tabular or the neural
architecture is relatively shallow.
Across studies, feature importance patterns were highly consistent. Prior costs and utilization emerged
as the dominant predictors, followed by comorbidities, procedures, and medication use. Very few models
incorporated social determinants, behavioral data, or text-based clinical variables, limiting interpretability
and potential policy translation.
When compared across methodological families, deep learning outperformed classical regression in nearly
all contexts, but tree-based models remained highly competitive in cross-sectional settings that emphasize
transparency and calibration. Overall, the evidence suggests that deep learning excels when data are longitu-
dinal, high-dimensional, or sequential, while classical and tree-based methods continue to provide stable,
interpretable baselines for policy-oriented modeling such as risk adjustment and premium setting.
Although most included studies involved large sample sizes, often ranging from tens of thousands to sev-
eral million observations, these studies generally possessed sufficient statistical power to detect meaningful
performance improvements, such as significant reductions in RMSE or MAE. Nevertheless, the overall conclu-
sions remain influenced by contextual factors, including the concentration of studies within specific countries
or insurance systems and the reliance on single-database observational designs. Importantly, these limitations
do not overturn the overarching conclusion that deep learning offers advantages over traditional regression
in longitudinal time-series cost prediction. However, effect size estimates—particularly across specific popula-
tions, subgroups, or neural network architectures—should be interpreted with caution.
Through the integration of theoretical considerations and empirical evidence, this review articulates
the Complexity–Performance Hypothesis as a unifying framework to explain these findings. In data sce-
narios characterized by relatively low dimensionality or limited complexity, traditional regression models
are often sufficient to achieve effective prediction. As data complexity increases—through greater nonli-
nearity or interaction effects—tree-based machine learning models begin to demonstrate advantages in
flexibility and fit. When data are both high-dimensional and longitudinal or multimodal, DNN models
with hierarchical feature-learning capabilities exhibit the greatest potential to improve overall prediction
error and identify high-cost tails. Importantly, this hypothesis is derived inductively from the eight
included empirical studies and is presented as a conceptual framework to guide model selection across
data structures and application scenarios, rather than as a precise estimate of a single causal effect.
Implications for health economics and policy
From a health economics and healthcare finance perspective, these findings translate into operational
guidance regarding when deep learning is most appropriate for real-world application. Specifically, deep
learning models are most relevant for healthcare cost prediction tasks that integrate longitudinal data or
multiple data modalities25. Under such conditions, neural networks tend to achieve lower overall predic-
tion error and demonstrate superior ability to identify high-cost populations, compared with traditional
regression and some tree-based models. In practice, this improved discrimination can support earlier
identification of high-risk individuals and inform budget planning and resource allocation decisions26.
When sufficient data infrastructure, computational resources, and institutional support are available,
deploying high-complexity deep learning models can be cost-effective and analytically justified. By con-
trast, in cross-sectional risk-adjustment or insurance estimation settings—where available predictors are
limited to standard claims data or a small number of structured covariates—the empirical evidence indi-
cates that shallow neural architectures yield only marginal improvements in explanatory power or cali-
bration. In such scenarios, tree-based machine learning models often achieve comparable or superior
performance, while offering greater interpretability.
Moreover, under regulatory and governance constraints, tree-based models typically impose lower com-
munication and transparency costs when engaging with policymakers and supervisory agencies27.
Accordingly, GLM-based two-part models and selected tree-based approaches remain appropriate baseline
choices for many applied health economics analyses. Adoption of deep learning in these contexts should be

JOURNALOFMEDICALECONOMICS 667
contingent upon direct head-to-head comparisons conducted on identical datasets and data partitions, dem-
onstrating reproducible and policy-relevant improvements in cost capture, budget accuracy, and high-cost
| population | monitoring. |     |     |     |     |     |
| ---------- | ----------- | --- | --- | --- | --- | --- |
Finally, practical deployment of deep learning models requires careful consideration of downstream
resource requirements, including computational infrastructure, MLOps maturity, and the capacity to
explain model behavior to decision-makers and regulators28. Within health economics, the Complexity–
Performance Hypothesis therefore implies not only a statistical matching between model capacity and
data structure, but also a balanced assessment of predictive gains, transparency, and institutional feasi-
bility. Given that most routine analytic workflows in insurance and public health agencies continue to
rely on GLM and tree-based models, the limited availability of readily deployable deep learning plat-
| forms remains     | a non-trivial | barrier     | to widespread | adoption29. |     |     |
| ----------------- | ------------- | ----------- | ------------- | ----------- | --- | --- |
| Future directions | and           | fundamental | challenges    |             |     |     |
To guide future research, this review delineates five fundamental challenges in applying deep learning
to healthcare expenditure prediction, outlines actionable strategies for their resolution, and identifies pri-
orities for collaboration between machine learning scientists and health economists (see Table 4).
| Challenge | 1: limited economic | interpretability |     |     |     |     |
| --------- | ------------------- | ---------------- | --- | --- | --- | --- |
Despite the high predictive accuracy of deep learning architectures, their opaque internal representa-
tions constrain economic interpretation and policy translation34. The “black-box” nature of neural net-
works obscures causal pathways and cost-driver interactions, limiting their relevance for accountability
and decision-making in health financing27. To align model outputs with economic reasoning, deep learn-
ing models should integrate explainable-AI (XAI) approaches—such as SHAP, Integrated Gradients, or
Propagation—and
Layer-wise Relevance report marginal effects comparable to those derived from gen-
eralized linear or two-part models. Developing hybrid “interpretable-deep” frameworks that embed
econometric constraints within neural architectures may reconcile predictive precision with transparency,
analyses35.
| facilitating | their integration | into budget-impact |     | and resource-allocation |     |     |
| ------------ | ----------------- | ------------------ | --- | ----------------------- | --- | --- |
Table 4. Challenges of deep learning in predicting healthcare spending and expenditure, and how they may be over-
| come with  | future development. |     |               |     |     |            |
| ---------- | ------------------- | --- | ------------- | --- | --- | ---------- |
| Challenges |                     |     | Currentstatus |     |     | Strategies |
Limitedeconomic Deeplearningmodelsachievehigh (cid:6) IncorporateexplainableAI(XAI)frameworkssuchas
interpretability predictiveaccuracybutprovidelimited SHAPorIntegratedGradients.
|     |     | transparencyforeconomicreasoning,    |     |     | (cid:6) Reportmarginaleffectsandsensitivityanalyses |     |
| --- | --- | ------------------------------------ | --- | --- | --------------------------------------------------- | --- |
|     |     | policytranslation,orcausalinference. |     |     | comparabletotraditionalregressionoutputs.           |     |
(cid:6) Develophybridinterpretable-deepmodelstailored
forcostdriversandbudgetimpactinterpretation.
Insufficientbenchmarking Manystudieslackdirect,standardized (cid:6) Requireside-by-sidebenchmarkingusingidentical
againstclassical comparisonsbetweendeeplearning datasetsandperformancemetrics.
(cid:6)
regression modelsandestablishedregression Emphasizecalibration,fairness,andwelfare
|     |     | frameworks(GLM,two-part,orhurdle |     |     | implicationsbeyondaccuracy.                      |     |
| --- | --- | -------------------------------- | --- | --- | ------------------------------------------------ | --- |
|     |     | models)30.                       |     |     | (cid:6) Promotetransparentreportingofincremental |     |
predictiveandeconomicgains.
Shorttemporalprediction Mostmodelspredictone-yearcosts, (cid:6) Extendmodelinghorizonstomulti-yearpredictions.
| horizons31 |     |                                  |     |     | (cid:6)                                   |     |
| ---------- | --- | -------------------------------- | --- | --- | ----------------------------------------- | --- |
|            |     | overlookinglong-termexpenditure  |     |     | Incorporatelongitudinalclaimsdataandtime- |     |
|            |     | dynamicsorpersistenceofhigh-cost |     |     | dependentsurvivalorsequencemodels.        |     |
status. (cid:6) Evaluatetemporalgeneralizationviarolling-window
validation.
Limiteddatadiversityand Currentstudiesrelyheavilyonsingle- (cid:6) Promotemulti-country,multi-payerbenchmarking
| generalizability |     | countryorproprietarydatasets,restricting |     |     | datasets.                                              |     |
| ---------------- | --- | ---------------------------------------- | --- | --- | ------------------------------------------------------ | --- |
|                  |     | generalizationacrosssystemsand           |     |     | (cid:6) Integrateopen,de-identifiedEHRoradministrative |     |
|                  |     | populations32.                           |     |     | datawithharmonizedcoding.                              |     |
(cid:6) Implementdomainadaptationandfederated
learningforprivacy-preservingcollaboration.
(cid:6)
Underuseofsocialand Modelspredominantlyusedemographicand Linkcostdatawithareadeprivation,socioeconomic,
behavioraldeterminants clinicalvariables,neglectingsocial orbehavioralriskindices.
|     |     | determinantsofhealth(SDOH)and |     |     | (cid:6) QuantifyincrementalexplanatorypowerofSDOH |     |
| --- | --- | ----------------------------- | --- | --- | ------------------------------------------------- | --- |
|     |     | behavioralpredictors33.       |     |     | variablesonexpenditureprediction.                 |     |
(cid:6) IntegrateSDOHembeddingsinmultimodal
architectures.

668 J.T.LEEETAL.
Challenge 2: insufficient benchmarking against classical regression
The absence of standardized benchmarking between deep learning models and traditional regression frame-
works remains a major methodological gap36. Many studies neglect formal comparisons with generalized lin-
ear, hurdle, or two-part models, or apply inconsistent data partitions and performance metrics, precluding
rigorous assessment of incremental value. Future research should direct, head-to-head benchmarking using
identical datasets, covariates, and validation procedures36. Evaluation must extend beyond statistical accuracy
to encompass calibration, discrimination, and welfare-relevant metrics such as cost-capture or decision-curve
analysis37. Transparent reporting of incremental explanatory power relative to GLM baselines will clarify
when the additional complexity of deep learning models is justified38.
All eight studies included in this review met the pre-specified minimum comparison criteria by incor-
porating at least one traditional or tree-based
comparator10,17–23.
However, only Drewe-Boss et al. (2022)
and Vimont et al. (2022) partially satisfied more stringent benchmarking requirements, including consist-
ent sample splits direct comparison with GLM two-part models10,21. The remaining studies reported
results under heterogeneous subgroup definitions or outcome specifications, limiting their suitability as
complete benchmarking
cases17–20,22,23.
Drawing on principles articulated in DECIDE-AI, we emphasize the importance of clearly defining
application scenarios, target populations, comparator models, and evaluation structures a priori36.
Although not specific to economic evaluation, these principles provide a useful framework for structur-
ing systematic and transparent benchmarking between neural networks and classical cost-prediction
models.
Challenge 3: short temporal prediction horizons
Most existing models focus on one-year prediction horizons, reflecting budget-cycle pragmatism but
neglecting the persistence and temporal dependencies of high-cost conditions31. Extending prediction
windows to multi-year horizons using longitudinal claims and EHR data would better capture dynamic
health-state transitions39. Sequence-based architectures (e.g. LSTM, GRU, transformer models), combined
with rolling-window validation, should be used to assess temporal stability39.
Across the included studies, training windows often exceeded the prediction horizon. For example,
Drewe-Boss et al. (2022) used data from 2010–2015 to predict costs in 2016–201710, while Lewis et al.
(2021) analyzed commercial claims data spanning 2006–2017.17 Kaushik et al. (2017, 2020a, 2020b) typic-
ally employed four to five years of training data with the final year reserved for testing18,22,23, whereas
Vimont et al. (2022) and Yu et al. (2021) relied primarily on cross-sectional designs19,21. However, details
regarding training and observation periods were often confined to tables and not fully discussed in the
main text. Future studies should provide explicit disclosure of calendar years and observation windows
to strengthen assessment of longitudinal performance and cross-context generalizability.
Challenge 4: limited data diversity and generalizability
Most studies rely on single-country, single-payer, or proprietary datasets, limiting external validity and
constraining cross-system generalization40. Differences in coding standards, benefit structures, and reim-
bursement schemes further impede model transferability. Addressing this challenge requires the estab-
lishment of multi-country, multi-payer benchmark datasets with harmonized variable definitions and cost
metrics41. Privacy-preserving and federated learning architectures can facilitate cross-institutional collab-
oration without compromising confidentiality41. Domain-adaptation techniques should be developed to
recalibrate models for heterogeneous populations and health systems. Publicly accessible, de-identified
datasets adhering to FAIR (Findable, Accessible, Interoperable, Reusable) data principles are essential for
reproducibility and methodological transparency42.
Challenge 5: underuse of social and behavioral determinants
Current deep learning cost-prediction models overwhelmingly depend on demographic and clinical variables,
with limited incorporation of social determinants of health (SDOH) or behavioral risk factors. Yet socioeco-
nomic conditions, education, and lifestyle behaviors exert substantial influence on utilization patterns and
cost trajectories43. Integrating SDOH requires linking administrative and clinical data with census, deprivation,

JOURNALOFMEDICALECONOMICS 669
or behavioral datasets, and representing these inputs through multimodal embeddings that capture latent
social context44. Quantifying the incremental explanatory and policy value of SDOH variables will help iden-
tify structural cost drivers and guide equitable allocation of healthcare resources.
Study limitations
This systematic review included only eight studies, and substantial heterogeneity was observed in
research design, data sources, healthcare systems, outcome definitions, and performance metrics. As a
result, quantitative meta-analysis was not feasible, and findings were synthesized narratively by identify-
ing consistent directional patterns. Most studies relied on single-country, single-database designs and
lacked external validation across time periods or healthcare systems. Additionally, the predominance of
one-year prediction horizons limits assessment of long-term robustness and generalizability.
Consequently, the Complexity–Performance Hypothesis should be viewed as a working hypothesis,
requiring further systematic validation rather than a definitively established causal mechanism.
Conclusion
Although the studies reviewed offer preliminary support for the Complexity–Performance Hypothesis,
rigorous empirical validation is still in its early stages. Future research should conduct head-to-head
benchmarking of modeling approaches on the same datasets, systematically varying dimensionality and
temporal depth to determine the threshold at which adopting deep neural networks becomes justified
over classical regression or ensemble methods. Deep learning offers clear gains for longitudinal,
sequence-rich cost forecasting, whereas tree-based methods remain highly competitive for cross-sec-
tional tabular prediction. Overall, these findings are consistent with the proposed Complexity–
Performance Hypothesis, which posits that the predictive advantages of deep learning emerge primarily
when model capacity is well matched to data complexity.
Transparency
Declaration of funding
This research was supported by the National Health Research Institutes (NHRI) Integrated Research Grant for
Biomedical and Health-Related Sciences Innovative Research Grant (IRG) (NHRI-EX114-11421PI) and the Mount Jade
ProjectYushan Fellow Program oftheMinistryof Education(MOE),Taiwan (MOE-112-YSFMN-0003-002-P1).
Declaration of financial/other interests
D.B.-C. W. is employed by Johnson & Johnson; this position is independent of and unrelated to the research pre-
sented in this manuscript. All other authors declare that they have no conflicts of interest relevant to the content of
this article.Peerreviewerson thismanuscript havenorelevant financialor other relationshipsto disclose.
Author contributions
J.T.L.conceivedanddesignedthestudy,conductedtheanalysis,andledthemanuscriptwriting.M.H.-S.Y.performed
the literature search and screening. All authors contributed to drafting and refining the of the manuscript. All
authorsread andapproved thefinalmanuscript.
Acknowledgements
JTL is partly funded by the Ministry of Education, Taiwan, through the Mount Jade Fellowship and the Mount Jade
Project Yushan Fellow Program (MOE-112-YSFMN-0003-002-P1) as well as by the National Health Research Institutes
(NHRI) Integrated Research Grant for Biomedical and Health-Related Sciences Innovative Research Grant (IRG) (NHRI-
EX114-11421PI)

670 J.T.LEEETAL.
| Use of generative | AI  |     |
| ----------------- | --- | --- |
The authors used ChatGPT (OpenAI, GPT-4o, 2025) to assist with language polishing and grammar/word checking
only.
| Data availability | statement |     |
| ----------------- | --------- | --- |
This systematic review is based solely on data extracted from published articles. No new datasets were created.
Extracteddatatablesandthe PRISMAchecklist canbe providedupon reasonable request.
ORCID
| JohnTayu Lee http://orcid.org/0000-0002-1551-4923   |                                         |     |
| --------------------------------------------------- | --------------------------------------- | --- |
| Melody Hsiao-San Yeh                                | http://orcid.org/0009-0009-4116-0637    |     |
| VincentCheng-Sheng                                  | Li http://orcid.org/0009-0006-8719-1699 |     |
| Hsiao-Hui Chen http://orcid.org/0000-0001-7897-3118 |                                         |     |
Yi-HsuanLiu http://orcid.org/0009-0007-5727-8328
| DavidBin-Chia Wu | http://orcid.org/0000-0002-0313-5758 |     |
| ---------------- | ------------------------------------ | --- |
References
[1] Dieleman JL, Campbell M, Chapin A, et al. Future and potential spending on health 2015–40: development
assistance for health, and government, prepaid private, and out-of-pocket health spending in 184 countries.
Lancet.2017;389(10083):2005–2030.
| The |     | doi: 10.1016/S0140-6736(17)30873-5. |
| --- | --- | ----------------------------------- |
[2] Rao KD, et al. Future health expenditures and its determinants in Latin America and the Caribbean: a multi-
| country projection | study. TheLancet | Regional Health–Americas;2025. |
| ------------------ | ---------------- | ------------------------------ |
[3] American Medical Association. Trends in health care spending. Chicago, IL: American Medical Association;
2023.
[4] Holster T, Ji SX, Marttinen P.Risk adjustment forregional healthcarefunding allocations with ensemble meth-
2024;25(7):1117–1131.
ods: an empirical study and interpretation. Eur J Health Econ. doi: 10.1007/s10198-023-
01656-w.
[5] Henley SS, Golden RM, Kashner TM. Statistical modeling methods: challenges and strategies. Biostat
2020;4(1):105–139.doi:
| Epidemiol. |     | 10.1080/24709360.2019.1618653. |
| ---------- | --- | ------------------------------ |
Rahnenfu€hrer
[6] J, De Bin R, Benner A, et al. Statistical analysis of high-dimensional biomedical data: a gentle
introduction to analytical goals, common approaches and challenges. BMC Med. 2023;21(1):182. doi: 10.1186/
s12916-023-02858-y.
2019;25(1):24–
[7] Esteva A, Robicquet A, Ramsundar B, et al. A guide to deep learning in healthcare. Nat Med.
29. doi:10.1038/s41591-018-0316-z.
[8] Miotto R, Wang F, Wang S, et al. Deep learning for healthcare: review, opportunities and challenges. Briefings
Bioinformat.2018;19(6):1236–1246.
doi: 10.1093/bib/bbx044.
[9] LeCunY, BengioY, Hinton G.Deeplearning.Nature.2015;521(7553):436–444.doi: 10.1038/nature14539.
[10] Drewe-Boss P, Enders D, Walker J, et al. Deep learning for prediction of population health costs. BMC Med
| Inform DecisMak. | 2022;22(1):32.doi: | 10.1186/s12911-021-01743-z. |
| ---------------- | ------------------ | --------------------------- |
[11] Topol EJ. High-performance medicine: the convergence of human and artificial intelligence. Nat Med. 2019;
| 25(1):44–56.doi: | 10.1038/s41591-018-0300-7. |     |
| ---------------- | -------------------------- | --- |
[12] Liu X, Faes L, Kale AU, et al. A comparison of deep learning performance against health-care professionals in
detecting diseases from medical imaging: a systematic review and meta-analysis. Lancet Digit Health. 2019;
| 1(6):e271–e297. | doi: 10.1016/S2589-7500(19)30123-2. |     |
| --------------- | ----------------------------------- | --- |
[13] He J, Baxter SL, Xu J, et al. The practical implementation of artificial intelligence technologies in medicine.
Med.2019;25(1):30–36.
| Nat | doi: 10.1038/s41591-018-0307-0. |     |
| --- | ------------------------------- | --- |
[14] Amiri MM, et al. Systematic review of factors determining health care expenditures. Health Policy Technol.
2021;10(2):100498.
[15] Ke X, Saksena P, Holly A. The determinants of health expenditure: a country-level panel data analysis.
| Geneva: WorldHealthOrganization; |     | 2011. p.1–28. |
| -------------------------------- | --- | ------------- |
[16] Page MJ, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ.
2021;372:n71.
[17] Lewis M, Elad G, Beladev M, et al. Comparison of deep learning with traditional models to predict prevent-
able acutecare use andspendingamong heartfailure patients.Sci Rep.2021;11(1):1164.doi: 10.1038/s41598-
020-80856-3.

JOURNALOFMEDICALECONOMICS 671
[18] Kaushik S, et al. Ensemble of multi-headed machine learning architectures for time-series forecasting of
healthcare expenditures. In: Applications of machine learning. Singapore: Springer; 2020. p. 199–216. doi: 10.
1007/978-981-15-3357-0_14.
[19] Yu K, Yang Z, Wu C, et al. In-hospital resource utilization prediction from electronic medical records with
deep learning.Knowl BasedSyst.2021;223:107052. doi:10.1016/j.knosys.2021.107052.
[20] Yang C, Delcher C, Shenkman E, et al. Machine learningapproachesfor predictinghighcosthighneed patient
expendituresinhealthcare.BiomedEngOnline.2018;17(Suppl1):131.doi:10.1186/s12938-018-0568-3.
[21] Vimont A, Leleu H, Durand-Zaleski I. Machine learning versus regression modelling in predicting individual
healthcare costs from a representative sample of the nationwide claims database in France. Eur J Health
Econ.2022;23(2):211–223.doi: 10.1007/s10198-021-01363-4.
[22] Kaushik S, Choudhury A, Natarajan S, et al. Medicine expenditure prediction via a variance-based generative
adversarialnetwork. IEEEAccess.2020;8:110947–110958. doi:10.1109/access.2020.3002346.
[23] Kaushik S, et al. Using LSTMs for predicting patient’s expenditure on medications. In: 2017 International
Conferenceon MachineLearning andDataScience (MLDS).IEEE;2017. doi:10.1109/MLDS.2017.9.
[24] Laqtib S, Yassini KE, Hasnaoui ML. A deep learning methods for intrusion detection systems based machine
learning inMANET.Proceedings ofthe4thInternational ConferenceonSmart CityApplications; 2019.
[25] Teles AS, de Moura IR, Silva F, et al. EHR-based prediction modelling meets multimodal deep learning: a sys-
tematic review of structured and textual data fusion methods. Information Fusion. 2025;118:102981. doi: 10.
1016/j.inffus.2025.102981.
[26] Smith J. Predictive analytics in healthcare: powering proactive patient care in the era of value-based care;
2025.
[27] Hassija V, Chamola V, Mahapatra A, et al. Interpreting black-box models: a review on explainable artificial
intelligence.Cogn Comput. 2024;16(1):45–74. doi: 10.1007/s12559-023-10179-8.
[28] Sendak MP, et al. A path for translation of machine learning products into healthcare delivery. EMJ Innov.
2020;10:19–00172.
[29] Obermeyer Z, Emanuel EJ. Predicting the future—big data, machine learning, and clinical medicine. N Engl J
Med. 2016;375(13):1216–1219.doi: 10.1056/NEJMp1606181.
[30] Bodha S. A comparative study of machine learning and deep learning models for predicting medical insur-
ancecosts withexplainable AI; 2025.
[31] Sohn JH, Chen Y, Lituiev D, et al. Prediction of future healthcare expenses of patients from chest radiographs
usingdeep learning: apilotstudy. Sci Rep.2022;12(1):8344.doi: 10.1038/s41598-022-12551-4.
[32] Futoma J, Simons M, Panch T, et al. The myth of generalisability in clinical research and machine learning in
healthcare. Lancet DigitHealth. 2020;2(9):e489–e492. doi:10.1016/S2589-7500(20)30186-2.
[33] Tan M, Hatef E, Taghipour D, et al. Including social and behavioral determinants in predictive models: trends,
challenges,andopportunities. JMIR Med Inform.2020;8(9):e18084. doi: 10.2196/18084.
[34] Yoon CH, Torrance R, Scheinerman N. Machine learning in medicine: should the pursuit of enhanced inter-
pretabilitybe abandoned? JMed Ethics. 2022;48(9):581–585.doi: 10.1136/medethics-2020-107102.
[35] De Bock KW, Coussement K, Caigny AD, et al. Explainable AI for operational research: a defining framework,
methods, applications, and a research agenda. Eur J Oper Res. 2024;317(2):249–272. doi: 10.1016/j.ejor.2023.
09.026.
[36] Vasey B, Nagendran M, Campbell B, et al. Reporting guideline for the early stage clinical evaluation of deci-
sion support systems driven by artificial intelligence: DECIDE-AI. BMJ. 2022;377:e070904. doi: 10.1136/bmj-
2022-070904.
[37] Collins GS, Reitsma JB, Altman DG, et al. Transparent reporting of a multivariable prediction model for indi-
vidual prognosis or diagnosis (TRIPOD): the TRIPOD statement. Br J Surg. 2015;102(3):148–158. doi: 10.1002/
bjs.9736.
[38] Steyerberg EW, Vickers AJ, Cook NR, et al. Assessing the performance of prediction models: a framework for
traditional andnovelmeasures. Epidemiology.2010;21(1):128–138.doi: 10.1097/EDE.0b013e3181c30fb2.
[39] Choi E, et al. Doctor AI: predicting clinical events via recurrent neural networks. In: Machine Learning for
Healthcare Conference.PMLR;2016.
[40] RasmyL,WuY,WangN,etal.Astudyofgeneralizabilityofrecurrentneuralnetwork-basedpredictivemodels
for heart failure onset risk using a large and heterogeneous EHR data set. J Biomed Inform. 2018;84:11–16.
doi: 10.1016/j.jbi.2018.06.011.
[41] Kaissis GA, Makowski MR, Ru€ckert D, et al. Secure, privacy-preserving andfederated machine learning inmed-
icalimaging. NatMach Intell.2020;2(6):305–311.doi:10.1038/s42256-020-0186-1.
[42] Wilkinson MD, Dumontier M, Aalbersberg IJ, et al. The FAIR guiding principles for scientific data management
andstewardship. Sci Data.2016;3(1):1–9.doi: 10.1038/sdata.2016.18.
[43] Lee NS, Whitman N, Vakharia N, et al. High-cost patients: hot-spotters don’t explain the half of it. J Gen
InternMed. 2017;32(1):28–34. doi:10.1007/s11606-016-3790-3.
[44] Rajkomar A, Hardt M, Howell MD, et al. Ensuring fairness in machine learning to advance health equity. Ann
InternMed. 2018;169(12):866–872.doi: 10.7326/M18-1990.