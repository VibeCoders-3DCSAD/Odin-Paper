| Clustering |         | and    | Similarity |     | Learning     |               | in Financial | Markets:    | A   |
| ---------- | ------- | ------ | ---------- | --- | ------------ | ------------- | ------------ | ----------- | --- |
|            |         |        | Tutorial   |     | for the      | Practitioners |              |             |     |
|            | Dhagash | Mehta, | John       | R.  | J. Thompson, |               | Hoyoung Lee, | Yongjae Lee |     |
|            |         |        |            |     | October      | 10,           | 2025         |             |     |
Dhagash Mehta is the Head of Applied Artificial Intelligence Research for Investment, BlackRock
| Inc., New | York, | NY, United | States | of America. |     |     |     |     |     |
| --------- | ----- | ---------- | ------ | ----------- | --- | --- | --- | --- | --- |
dhagash.mehta@blackrock.com
John R.J. ThompsonisanAssistantProfessorintheDepartmentofComputerScience,Mathemat-
ics, Physics and Statistics, The University of British Columbia, Kelowna, BC, Canada.
john.thompson@ubc.ca
Hoyoung Lee is a Master’s student in the Department of Industrial Engineering, Ulsan National
| Institute | of Science | and | Technology | (UNIST), | Ulsan, | Republic | of Korea. |     |     |
| --------- | ---------- | --- | ---------- | -------- | ------ | -------- | --------- | --- | --- |
hoyounglee@unist.ac.kr
Yongjae LeeisanAssociateProfessorintheDepartmentofIndustrialEngineeringandtheArtificial
Intelligence Graduate School, Ulsan National Institute of Science and Technology (UNIST), Ulsan,
| Republic | of Korea. |     |     |     |     |     |     |     |     |
| -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
yongjaelee@unist.ac.kr
1

Key Findings
1. Traditional peer-grouping methods, such as industry codes or static style boxes, are coarse and
rigid. Modern investment requires **adaptive, data-driven similarity systems** that quantify
closenessbasedonactualriskandthematicexposures,notpre-definedlabels. Advancesinmetric
learningandlargelanguagemodelsenabletheconstructionofflexible,operationalneighborhoods
for securities and funds.
2. Evaluation must shift from abstract academic metrics to operational validity. The core focus is
on substitution fidelity, neighborhood stability across regimes, and segment utility for decision-
making. This ensures that models are transparent, auditable, and withstand the scrutiny of
compliance and fiduciary accountability.
3. Effective similarity requires moving beyond single data types to fuse heterogeneous sources.
Models must integrate tabular fundamentals, time-series performance, textual disclosures, and
relational graph structures. This allows practitioners to achieve robust peer discovery and align
narratives with market dynamics, tackling the sparsity inherent in financial data.
2

Abstract
Clusteringandsimilaritylearningareincreasinglyindispensableforstructuringheterogeneous
financial data and supporting real-world decision making. Traditional heuristics such as indus-
try codes, static style boxes, or return correlations, offer only coarse and rigid notions of peer
groups. Recentadvancesinmetriclearning,graphmethods,andlargelanguagemodelsnowmake
it possible to build adaptive neighborhoods of securities, funds, companies, and investors that
align more closely with actual risk, liquidity, and thematic exposures. This tutorial synthesizes
these methodological developments and demonstrates their use across major asset classes. Case
studies show how supervised proximities improve bond substitution, how fund similarity systems
reconcilecategoryreproducibilitywithoutlierdetection,howmultimodalpipelinesrefinecompany
comparablesforvaluationandstrategy,andhowinvestorclusteringenhancespersonalizationand
Know-Your-Client (KYC) analytics. We emphasize modeling choices that make clustering and
similarity auditable and robust under regime shifts. We also outline their evaluation protocols
such as neighborhood stability, substitution fidelity, and segment utility, etc., which align with
investment, compliance, and fiduciary objectives. Overall, the central message for practitioners
is pragmatic: similarity systems have moved beyond experimental prototypes and now stand as
deployable techniques within real investment workflows.
Keywords: Clustering; Similarity Learning; Investment Management
3

Financial markets are built on comparisons. Every day, practitioners ask which bond can sub-
stitute for another, which fund belongs to which style, which company is closest to a competitor, or
which investor segment shares similar behaviors. Clustering and similarity learning formalize these
judgments, transforming them from ad hoc heuristics into systematic, data-driven frameworks. What
began as rule-based taxonomies and simple ratio screens has grown into a toolkit that can integrate
fundamentals, returns, text, graphs, and alternative data to uncover meaningful neighborhoods across
diverse asset classes.
The promise of these methods is straightforward: they help organize complexity. Vast universes of
securities, funds, or clients can be reduced to interpretable groups, and those groups can be aligned
withrealeconomicattributessuchascreditrisk, liquidity,orthematicexposure(Exhibit1). Peersets
becomethefoundationfortasksasvariedaspricing,hedging,allocation,surveillance,andcompliance.
Properlydesigned,clusteringandsimilaritytoolsprovidepractitionerswithatransparentwaytoalign
analytics with fiduciary and regulatory objectives.
Style Drift Detection Substitution Competitor Analysis
illiquid asset
liquid asset
Relative Valuation Scenario Reduction
Clustering
&
Similarity Learning
Growth
Personalization Outlier Detection Thematic Investing
Technology Finance
FinTech
Exhibit 1: Usecases of Clustering and Similarity Learning in Financial Markets.
Yet practical use requires care. Unlike supervised prediction, similarity has no universal ground
truth. The definition of “peer” depends on context, data modality, and market regime. Outputs can
shift with parameter choices, and advanced models often sacrifice interpretability just when oversight
is most needed. For this reason, governance frameworks such as SR 11-7 place strong emphasis on
documentation, reproducibility, and transparency.
This tutorial delivers a pragmatic perspective. It reviews the range of clustering and similarity
methods available today, shows how they operate across asset classes from bonds and funds to com-
4

modities and scenarios, and highlights evaluation practices that matter for production deployment.
The aim is to equip practitioners with a field guide to design robust, interpretable, and scalable sys-
tems that make similarity learning a dependable part of financial workflows.
Clustering and Similarity Learning Methodologies
Before discussing different techniques, we first clarify important nuances of clustering and similarity
learning. Atahighlevel,clustering discoversgroupsdirectlyfromdatawithoutlabels,whilesimilarity
learning focuses on constructing or learning a measure of closeness that can drive retrieval, ranking,
substitution, or downstream modeling.
What practitioners mean by clustering
Clusteringistheprocessofgroupingfinancialinstruments,funds,orinvestorsintosetswheremembers
share similar characteristics, such as risk profile or performance behavior, while being different from
those in other sets. Clustering is usually thought of as an unsupervised learning task, that is, the
grouping is learned without resorting to any target variable(s). In this setting, the notion of close-
ness is typically governed by a pre-specified similarity or distance function (for example, Euclidean
distance, correlation-based distance, or mixed-type dissimilarities), rather than being learned from
labeled supervision (common distance metrics are summarized in Exhibit 2). Thus, the effectiveness
of clustering hinges on how well this chosen metric captures the underlying economic structure of the
data.
Clustering methods across modalities Clustering provides a flexible family of techniques to par-
tition financial data into coherent groups, but the choice of algorithm depends on the modality, the
available similarity measure, and the structure of the data. Classical clustering methods have a long
tradition in finance (Marti et al., 2021), from peer group formation to portfolio construction, and
remain central to many modern applications. Below, we describe the main approaches (summarized
in Exhibit 3).
Partitioning methods suchask-meansandk-medoidsgroupsecuritiesbyminimizingwithin-cluster
distances(Jainetal.,1999). Theyarefastandeffectivefortabulardatainequitiesandbonds,though
they require a pre-set number of clusters; k-medoids is more robust to outliers.
Hierarchical clustering builds nested trees. Dendrograms enable drill-down views and align with
portfolio hierarchies. In practice, it supports Hierarchical Risk Parity (Lopez de Prado, 2016), which
delivers more stable allocations under estimation error (Raffinot, 2017).
5

Density-based clustering (DBSCAN, HDBSCAN) defines clusters as dense regions separated by
sparse areas. It avoids pre-specifying cluster counts and is well-suited to detecting niche cohorts or
| anomalies | such as fraud | and rare assets. |     |     |
| --------- | ------------- | ---------------- | --- | --- |
Model-basedclustering assumesdatacomefromamixtureofdistributions,oftenGaussian. Ityields
| soft memberships | and | provides natural | uncertainty | estimates. |
| ---------------- | --- | ---------------- | ----------- | ---------- |
Financeoftenfacesmixed-typetabulardata thatcombininenumeric,ordinal,categorical,andsparse
indicators. Measures such as Gower (Gower, 1971), k-prototypes, and generalized dissimilarities allow
| clustering | without forcing | all variables | into numeric | space. |
| ---------- | --------------- | ------------- | ------------ | ------ |
Time-series clustering extends these methods to sequential data. Distances include correlation,
ultrametrics from minimum spanning trees, dynamic time warping (DTW), Kullback–Leibler diver-
gence, Wasserstein distance, and others. Rolling windows reveal co-movement regimes while adapting
| to structural | breaks. |     |     |     |
| ------------- | ------- | --- | --- | --- |
Text clustering embeds documents via TF–IDF or transformer models, then applies partitioning
or hierarchical methods (Manning et al., 2008). Applications include grouping prospectuses, earnings
| calls, and | filings to integrate | qualitative | signals. |     |
| ---------- | -------------------- | ----------- | -------- | --- |
Graph clustering analyzes relational data, where nodes represent entities and edges represent eco-
nomic ties. Methods include community detection, modularity optimization, and embeddings such
as node2vec (Grover & Leskovec, 2016; Satone et al., 2021), widely used in systemic risk and peer
discovery.
Image and spatial clustering uses embeddings from convolutional or Siamese networks with par-
titioning or density-based grouping. In real estate, property and satellite images are clustered for
comparables, collateral risk, and geographic exposure (Poursaeed et al., 2017).
| What practitioners |     | mean | by similarity | learning |
| ------------------ | --- | ---- | ------------- | -------- |
Whereas typically clustering methods take a predefined notion of “closeness” in the form of a pre-
chosen similarity or distance metric, similarity learning formalizes the notion of closeness by learning
the distance metric using the given data: the goal here is to learn a distance or similarity function
that keeps “positives” close and “negatives” apart (contrastive and triplet paradigms), with extensive
surveys covering both classic vector data and structured objects (Kulis, 2013).
In practice, this takes several forms. Supervised similarity uses known equivalences—such as funds
in the same category or bonds with interchangeable features—to shape embeddings, with product
taxonomies or analyst coverage serving as weak labels. Semi-supervised and self-supervised similarity
leverage abundant unlabeled data, for example by forecasting in time series or masked modeling in
| text, reducing | dependence | on noisy | human labels. |     |
| -------------- | ---------- | -------- | ------------- | --- |
6

|           | Exhibit | 2: Common | Distance | Metrics    | for Clustering |       | by  | Data  | Type |     |
| --------- | ------- | --------- | -------- | ---------- | -------------- | ----- | --- | ----- | ---- | --- |
| Data Type |         | Distance  | /        | Similarity | Metrics        | Notes | /   | Usage |      |     |
Euclidean
|         |     |           |      |     |     | Standard     |     | metrics | for | tabular and |
| ------- | --- | --------- | ---- | --- | --- | ------------ | --- | ------- | --- | ----------- |
| Numeric |     | Manhattan | (L1) |     |     |              |     |         |     |             |
|         |     |           |      |     |     | multivariate |     | data;   |     |             |
(continuous)
|     |     | Minkowski |     |     |     | Mahalanobis |     | accounts |     | for correlations |
| --- | --- | --------- | --- | --- | --- | ----------- | --- | -------- | --- | ---------------- |
Mahalanobis
|             |     | Hamming | distance |             |     |            |         |        |                |     |
| ----------- | --- | ------- | -------- | ----------- | --- | ---------- | ------- | ------ | -------------- | --- |
|             |     |         |          |             |     | Works      | for     | binary | or categorical |     |
| Categorical |     | Simple  | matching | coefficient |     | variables; |         |        |                |     |
|             |     |         |          |             |     | Jaccard    | ignores |        | co-absences    |     |
Jaccard similarity
|     |     | Gower’s | similarity |     |     | Handles |     | heterogeneous |     | attributes |
| --- | --- | ------- | ---------- | --- | --- | ------- | --- | ------------- | --- | ---------- |
Mixed-type
|            |              | Huang             | distance |               |       | without  |     | coercing   | everything | to            |
| ---------- | ------------ | ----------------- | -------- | ------------- | ----- | -------- | --- | ---------- | ---------- | ------------- |
| (numeric + | categorical) |                   |          |               |       |          |     |            |            |               |
|            |              | Kernel            | metric   | dissimilarity |       | numeric  |     |            |            |               |
|            |              | Correlation-based |          | distance      |       |          |     |            |            |               |
|            |              | Dynamic           | Time     | Warping       | (DTW) | Captures |     | similarity | in         | trajectories, |
Time series
|     |     | Euclidean   | on         | lagged vectors |     | alignment, |     | and      | distributional | shifts  |
| --- | --- | ----------- | ---------- | -------------- | --- | ---------- | --- | -------- | -------------- | ------- |
|     |     | Wasserstein |            | distance       |     |            |     |          |                |         |
|     |     | Cosine      | similarity | on TF–IDF      |     |            |     |          |                |         |
|     |     |             |            |                |     | Measures   |     | semantic | similarity     | between |
Text
|                   |      | Word2Vec         | or            | BERT embeddings  |      |                |           |                 |       |               |
| ----------------- | ---- | ---------------- | ------------- | ---------------- | ---- | -------------- | --------- | --------------- | ----- | ------------- |
|                   |      |                  |               |                  |      | documents,     |           | disclosures,    |       | or strategies |
|                   |      | Jaccard          | similarity    | on token         | sets |                |           |                 |       |               |
|                   |      | Shortest-path    |               | distance         |      |                |           |                 |       |               |
|                   |      | Graph            | edit distance |                  |      | Used           | for       | issuer–security |       | networks,     |
| Graphs / Networks |      |                  |               |                  |      |                |           |                 |       |               |
|                   |      | Spectral         | distance      |                  |      | fund–holding   |           | bipartite       |       | graphs        |
|                   |      | Node2Vec         | /             | graph embeddings |      |                |           |                 |       |               |
|                   |      | Euclidean        | on            | feature vectors  |      |                |           |                 |       |               |
|                   |      |                  |               |                  |      | Property       |           | or satellite    | image | clustering;   |
| Images / Spatial  | data |                  |               |                  |      |                |           |                 |       |               |
|                   |      | Structural       | similarity    | (SSIM)           |      | spatial        | proximity |                 | also  | relevant      |
|                   |      | Siamese          | embedding     | distances        |      |                |           |                 |       |               |
|                   |      | Kullback–Leibler |               | divergence       |      |                |           |                 |       |               |
|                   |      |                  |               |                  |      | Comparing      |           | empirical       |       | return        |
| Distributional    |      | Jensen–Shannon   |               | divergence       |      | distributions, |           |                 |       |               |
|                   |      |                  |               |                  |      | volatility     |           | regimes,        | or    | scenarios     |
|                   |      | Wasserstein      |               | (Earth Mover’s)  | dis- |                |           |                 |       |               |
tance
Anotherdistinctionis betweenglobal metrics, whichapplyacross allentities, andlocal oradaptive
metrics, which adjust by region, class, or query. Finance often requires task-specific similarity (for
example, liquidity substitution versus credit risk), supported by multi-task learning that shares infor-
mation while tailoring metrics to objectives. Finally, feature-weighted similarity methods emphasize
the attributes most relevant to the task, ensuring neighborhoods and clusters reflect real operational
| needs (Ghashti | & Thompson, | 2025a,b). |     |     |     |     |     |     |     |     |
| -------------- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
In practice, this enables models to focus on the features most relevant to the financial task at
hand, whether prioritizing liquidity, credit, temporal dynamics, or textual content, thereby producing
| neighborhoods | and clusters | that better | reflect | operational | realities. |     |     |     |     |     |
| ------------- | ------------ | ----------- | ------- | ----------- | ---------- | --- | --- | --- | --- | --- |
7

|          | Exhibit | 3: Clustering | methods     | across data | modalities | in finance       |               |
| -------- | ------- | ------------- | ----------- | ----------- | ---------- | ---------------- | ------------- |
| Modality |         | Clustering    | Method      |             | Notes /    | Usage            |               |
|          |         |               |             |             | Partitions | data to minimize | intra-        |
|          |         | k-means       | / k-medoids |             | cluster    | variance; used   | for fundamen- |
Tabular data
|     |     |              |            |     | tals, factor | exposures.     |                  |
| --- | --- | ------------ | ---------- | --- | ------------ | -------------- | ---------------- |
|     |     |              |            |     | Creates      | a hierarchy of | clusters (den-   |
|     |     | Hierarchical | clustering |     | drogram);    | applied to     | equities, funds, |
macro data.
Findsdenseregions,goodforirregular
Density-based
| Tabular /  |     |          |          |     | shapes and     | noise; used | for transaction  |
| ---------- | --- | -------- | -------- | --- | -------------- | ----------- | ---------------- |
| mixed data |     | (DBSCAN, | HDBSCAN) |     | fraud, anomaly | detection.  |                  |
|            |     |          |          |     | Probabilistic  | approach    | for soft assign- |
Tabular / Model-based clustering ments;modelsheterogeneityinreturns
| distributions |     | (Gaussian   | mixtures)  |     |               |                       |     |
| ------------- | --- | ----------- | ---------- | --- | ------------- | --------------------- | --- |
|               |     |             |            |     | or volatility | regimes.              |     |
|               |     | Correlation | clustering |     |               |                       |     |
|               |     |             |            |     | Groups        | assets by co-movement | or  |
Time series Dynamic time warping trajectory similarity; for portfolio
|     |     |     |     |     | diversification, | regime | analysis. |
| --- | --- | --- | --- | --- | ---------------- | ------ | --------- |
Spectral clustering
Clustersdocumentsbasedonsemantic
| Text |     | Document             | embedding | +          |             |          |                  |
| ---- | --- | -------------------- | --------- | ---------- | ----------- | -------- | ---------------- |
|      |     |                      |           |            | embeddings; | thematic | analysis of fil- |
|      |     | k-means/hierarchical |           | clustering |             |          |                  |
ings, reports.
|        |     | Community | detection |     | Finds dense | subgraphs           | (communities); |
| ------ | --- | --------- | --------- | --- | ----------- | ------------------- | -------------- |
| Graphs |     |           |           |     | analyzes    | interbank networks, |                |
Spectral clustering
|     |     | Modularity | optimization |     | fund–holding | structures.      |             |
| --- | --- | ---------- | ------------ | --- | ------------ | ---------------- | ----------- |
|     |     |            |              |     | Clusters     | based on learned | visual fea- |
Images / spatial CNN / Siamese embeddings tures;usedforrealestatecomps,satel-
+ clustering
lite data analysis.
8

Similarity learning in finance goes beyond embedding vectors into latent spaces. It often requires
structured similarity, where relationships such as portfolio proximities, issuer–security hierarchies, or
temporallinksarepreserved. Graph-basedandmultimodalmethodscapturethesestructures,ensuring
that closeness respects domain constraints. Overall, similarity learning is not a single technique but a
flexible toolkit, adaptable to the context-specific definitions of “peer” that practitioners need.
Similarity learning methods Modern finance provides diverse modalities such as tabular, time
series, text, images, and graphs, and so on, and similarity methods must adapt accordingly. Below we
outline the main families of methods (summarized in Exhibit 4).
Metric learning (Kulis, 2013) transforms input space so that similar instances move closer and
dissimilar ones farther apart. Classical methods include Mahalanobis and LMNN, which learn linear
transformations to reshape geometry around task-specific closeness. Kernel metric learning extends
thistoheterogeneousdatabyoperatinginreproducingkernelHilbertspaces,handlingmixedvariables
and nonlinearities for applications such as segmentation and credit cohorts.
Random forest proximity measures how often two observations fall into the same leaf across an
ensemble, naturally handling nonlinearities and mixed data (Breiman, 2001). It has been applied to
bondsubstitution,fundpeergrouping,andinvestorsegmentation(Jeyapaulrajetal.,2022;Sahaetal.,
2024), where supervised proximities align similarity with predictive tasks.
Siamese networks map inputs into embedding spaces using paired examples with contrastive loss
(Bromley et al., 1993). They support real estate comparables, document matching, and collateral risk
assessment (Poursaeed et al., 2017; Das et al., 2021; Viana & Barbosa, 2021). Triplet loss embed-
dings extend this by enforcing anchor–positive–negative ordering, enabling fine-grained similarity for
thematic investing (Schroff et al., 2015; Lee et al., 2025).
Time-series similarity learning uses correlation, DTW, or Wasserstein distances, with recent en-
coders adapting to regime shifts (Dolphin et al., 2023).
Textual similarity relies on transformer embeddings such as BERT (Devlin et al., 2019), clustering
disclosures and reports to support thematic analysis and peer discovery (Vamvourellis et al., 2022;
Gabaix et al., 2024; Vamvourellis et al., 2024).
Graph neural networks (GNNs) learn node embeddings from neighborhood structure, useful for
issuer–security links, fund–holding networks, and supply chains. Methods like DeepWalk (Perozzi
et al., 2014) and node2vec (Satone et al., 2021) support systemic risk monitoring and peer retrieval.
Contrastive learning optimizes positive vs. negative pairs rather than triplets (Chen et al., 2020),
and is applied in time-series representation and volatility regime learning (Dolphin et al., 2024).
Multimodal similarity integrates fundamentals, returns, text, and graphs into joint embeddings,
9

using transformers and attention to align signals. Examples include theme grouping (Lee et al., 2025)
| and ripple-effect |     | prediction | via LLM–graph |     | integration |     | (Xu et | al., 2025). |     |     |
| ----------------- | --- | ---------- | ------------- | --- | ----------- | --- | ------ | ----------- | --- | --- |
Open-setsimilarity addsanomalydetection,flaggingobservationsoutsidelearnedgroupstoidentify
| new strategies, | anomalies, |               | or risk clusters |      | (Feng et    | al., 2024). |         |      |                   |                |
| --------------- | ---------- | ------------- | ---------------- | ---- | ----------- | ----------- | ------- | ---- | ----------------- | -------------- |
|                 | Exhibit    | 4: Similarity | Learning         |      | Methods     | (Supervised |         | and  | Semi-supervised)  |                |
| Method          |            |               | Learning         | Type | Data        | Type        | / Input |      | Applications      |                |
|                 |            |               |                  |      | Tabular     | features    |         | with | Bond substitution |                |
| Metric learning |            |               | Supervised       |      |             |             |         |      |                   |                |
|                 |            |               |                  |      | labels      | or expert   |         |      | Fund peer         | groups         |
|                 |            |               |                  |      | constraints |             |         |      | Investor          | risk profiling |
|                 |            |               |                  |      | Mixed-type  |             | tabular |      | Household         | finance        |
|                 |            |               | Supervised       | /    |             |             |         |      |                   |                |
| Kernel metric   | learning   |               |                  |      |             |             |         |      |                   |                |
|                 |            |               | Semi-supervised  |      | variables   | with        | side    |      | segmentation      |                |
|                 |            |               |                  |      | information |             |         |      | KYC similarity    |                |
|                 |            |               |                  |      | Images      | embeddings  |         |      | Real estate       | comparables    |
Supervised
| Siamese      | networks   |     |                   |      | Text             | embeddings |            |        | Document            | similarity      |
| ------------ | ---------- | --- | ----------------- | ---- | ---------------- | ---------- | ---------- | ------ | ------------------- | --------------- |
|              |            |     | (pairwise labels) |      |                  |            |            |        |                     |                 |
|              |            |     |                   |      | Tabular          | embeddings |            |        | Collateral          | risk            |
|              |            |     |                   |      | Networks         |            |            |        | Systemic            | risk monitoring |
| Graph neural | networks   |     |                   |      |                  |            |            |        |                     |                 |
|              |            |     |                   |      | (issuer–security |            |            |        | Fund embeddings     |                 |
|              |            |     |                   |      | fund–holding)    |            |            |        | Corporate           | peer sets       |
|              |            |     |                   |      |                  |            |            |        | Regime-aware        | asset           |
|              |            |     |                   |      | Time             | series     | embeddings |        |                     |                 |
|              |            |     |                   |      |                  |            |            |        | Thematic            | investing       |
| Contrastive  | learning   |     | Supervised        | /    | Text             | embeddings |            |        |                     |                 |
|              |            |     |                   |      |                  |            |            |        | Factor neighborhood |                 |
|              |            |     | Semi-supervised   |      | Multimodal       |            | inputs     |        |                     |                 |
|              |            |     |                   |      |                  |            |            |        | Fund classification |                 |
|              |            |     |                   |      |                  |            |            |        | Disclosure          | similarity      |
|              |            |     |                   |      | Integrated       |            | inputs     |        |                     |                 |
| Multimodal   | similarity |     |                   |      |                  |            |            |        | Company             | comparables     |
|              |            |     |                   |      | (tabular,        | text,      | image,     | graph) |                     |                 |
| learning     |            |     |                   |      |                  |            |            |        | Fund style          | innovation      |
|              |            |     |                   |      |                  |            |            |        | ESG alignment       |                 |
|              |            |     |                   |      |                  |            |            |        | Novel fund          | styles          |
| Open-set     | similarity |     | Supervised        | with | Tabular          | +          | text       |        |                     |                 |
|              |            |     |                   |      |                  |            |            |        | Outlier detection   |                 |
| learning     |            |     | anomaly detection |      | embeddings       |            |            |        |                     |                 |
|              |            |     |                   |      |                  |            |            |        | Market anomaly      |                 |
identification
Evaluation Methodologies in Clustering and Similarity Learning
Evaluating clustering and similarity is difficult because most methods are unsupervised. In finance,
thefocushasshiftedfromabstractmetricstooperational validity: whetherpeergroupsremainstable,
substitutes preserve liquidity and risk, outliers align with expert judgment, and outputs are explain-
able for compliance. Models are judged by their ability to support investment decisions, withstand
| regulatory | scrutiny, | and meet | fiduciary | duties. |     |     |     |     |     |     |
| ---------- | --------- | -------- | --------- | ------- | --- | --- | --- | --- | --- | --- |
Academic metrics. Classical indices such as Silhouette, Dunn, and Davies–Bouldin measure co-
hesion and separation, while external measures like ARI and NMI test alignment with known labels,
often in fund category reproducibility (Castellanos et al., 2024). Stability across bootstrap samples or
rolling windows is especially important in equities and ETFs (Polinesi & Recchioni, 2021).
10

Practitioner validation. Bonds are tested via K-nearest neighbor (KNN) peer sets that preserve
credit and liquidity (Jeyapaulraj et al., 2022). For funds, models must reproduce vendor categories
such as Morningstar (Mehta et al., 2020; Desai & Mehta, 2021; Feng et al., 2024). In equities, peer
groups should explain return co-movement better than GICS or SIC codes (Barberis et al., 2005;
Molinari et al., 2024). For investors, utility is judged by improved segmentation, personalized advice,
or behavioral monitoring (Thompson et al., 2021; Thompson & Davison, 2024).
Multimodal robustness. As data sources expand, evaluation extends to multimodal pipelines.
Text-based peers are validated by valuation accuracy gains (Dzuyo et al., 2025), graph embeddings
by improvements in risk and counterparty monitoring (Zhou et al., 2022; Cao et al., 2024), and LLM-
driven systems by ablation tests and governance checks such as bias audits (Papenkov et al., 2023).
| Exhibit | 5 provides | a brief       | summary        | of various | evaluation | metrics. |              |               |         |     |     |
| ------- | ---------- | ------------- | -------------- | ---------- | ---------- | -------- | ------------ | ------------- | ------- | --- | --- |
|         | Exhibit    | 5: Evaluation | methodologies: |            | academic   | vs.      | practitioner | perspectives. |         |     |     |
| Domain  |            |               | Academic       | metrics    |            |          | Practitioner |               | metrics |     |     |
General clustering Silhouette, Dunn, Davies–Bouldin, Stability in rolling windows; inter-
|     |     |     | ARI, NMI | (Hubert    | & Arabie,   | 1985;   | pretability |     | for compliance |     |     |
| --- | --- | --- | -------- | ---------- | ----------- | ------- | ----------- | --- | -------------- | --- | --- |
|     |     |     | Jain et  | al., 1999; | Castellanos | et al., |             |     |                |     |     |
2024)
Bonds Cluster cohesion vs. labels Substitution fidelity under liquidity
|     |     |     |     |     |     |     | and     | credit | constraints | (Jeyapaulraj |       |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ----------- | ------------ | ----- |
|     |     |     |     |     |     |     | et al., | 2022;  | Rosaler     | et al.,      | 2025) |
Funds ARI/NMI vs. vendor labels Categoryreproducibility,outlierde-
|     |     |     |     |     |     |     | tection, | open-set | anomalies |          | (Mehta |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --------- | -------- | ------ |
|     |     |     |     |     |     |     | et al.,  | 2020;    | Desai     | & Mehta, | 2021;  |
|     |     |     |     |     |     |     | Feng     | et al.,  | 2024)     |          |        |
Equities Return correlation alignment with Thematic co-movement, factor ex-
|     |     |     | GICS/SIC |     |     |     | posure | stability | (Barberis |       | et al., |
| --- | --- | --- | -------- | --- | --- | --- | ------ | --------- | --------- | ----- | ------- |
|     |     |     |          |     |     |     | 2005;  | Molinari  | et al.,   | 2024) |         |
Investors Clustering indices on transaction Segment utility for KYC, person-
|     |     |     | data |     |     |     | alization, |     | market     | crash | behavior,  |
| --- | --- | --- | ---- | --- | --- | --- | ---------- | --- | ---------- | ----- | ---------- |
|     |     |     |      |     |     |     | monitoring |     | (Thompson  | et    | al., 2021; |
|     |     |     |      |     |     |     | Thompson   |     | & Davison, | 2024) |            |
Multimodal Cross-modalembeddingconsistency Contribution of each modality, ab-
|              |     |       |            |     |     |            | lation | robustness, |               | governance | au- |
| ------------ | --- | ----- | ---------- | --- | --- | ---------- | ------ | ----------- | ------------- | ---------- | --- |
|              |     |       |            |     |     |            | dits   | (Dzuyo      | et al., 2025; | ?)         |     |
| Fixed-Income |     | Asset | Clustering |     | and | Similarity |        |             |               |            |     |
Fixedincomeposesuniquechallengesforclusteringandsimilarity(Fabozzi,2007). Bondsdifferwidely
in covenants, maturity, callability, and tax status, while trading is often sparse and noisy. Investor
needs center on substitution (finding liquid peers), relative value (benchmarking within a cohort),
and risk diagnostics (flagging outliers or monitoring). Therefore, effective pipelines combine tabular
11

descriptors such as ratings and fundamentals with time-series behavior, textual disclosures, and graph
structures like issuer linkages or co-holdings to create peer groups that are both stable and responsive
to market regimes.
Corporate Bonds
In corporate credit, the most valuable definition of “similar” is one for trades: a substitute must
preserve exposures such as sector, rating, maturity, and optionality, while also working under real
frictions like inventory, lot size, and liquidity. Because trading is intermittent and spreads embed
liquiditypremia,desksneedpeercohortstoprice,hedge,andsourcealternativeswhenatargetCUSIP
is unavailable.
Unsupervisedclusteringcanidentifypeersetsbasedondescriptivefeatures,butitsvaluedependson
business-centric validation such as substitution under desk constraints, turnover, and rolling stability,
i.e.,notonabstractindices. Wudemonstratesthisbygeneratingcorporatebondcohortsunderrating,
sector, and duration priors, then validating them against desk needs (Wu, 2023).
Supervised similarity provides a more direct path. Jeyapaulraj et al. show how Random Forest
proximitieslearnbond–bonddistancesalignedwithdeskusecasessuchasrelativevalue, substitution,
and surveillance, and propose evaluation criteria based on stability and substitution fidelity (Jeya-
paulraj et al., 2022). Rosaler et al. extend this idea with a quantum-cognition metric learner that
improves on tree models in high-yield markets, where noise and sparsity challenge heuristic similarity
(Rosaler et al., 2025).
Relational structure adds another layer. Bonds co-move not only through shared terms but also
throughissuers,capitalstructures,andcommonownership. Graphmethodscapturetheselinks. Zhou
et al. use a temporal bipartite fund–bond graph to show that graph neural networks improve price
and yield prediction relative to time-series models, with node embeddings naturally supporting peer
retrieval(Zhouetal.,2022). Similargraph-basedmodelsfordefaultriskconfirmthevalueofencoding
issuer and ownership networks (Li et al., 2023).
Portfolio trading further underscores the need for robust similarity. Nearly one-fifth of U.S.
investment-grade volume now trades in baskets. Traditional overlap metrics often fail to align baskets
with ETF benchmarks. STRAPSim addresses this by matching bonds at the constituent and weight
level,producingcloserreturn-basedalignmentandimprovingpricingandexecutioninportfoliotrades
(Li et al., 2025). For practitioners, basket similarity enhances transparency, liquidity sourcing, and
efficiency in less liquid credit markets.
12

Municipal bonds
Municipal markets add another layer of complexity: issuers range from states to school districts,
tax treatments vary, and covenants are highly idiosyncratic. Trading is sparse, dealer-intermediated,
and costly, with intermittent price discovery (Harris & Piwowar, 2006; Green et al., 2007). In this
setting,supervisedsimilarityhasshownstrongvalue. ACatBoost-basedframeworklearnsmuni–muni
distancesfromlargeU.S.datasetsandassemblesnearest-neighborcohortsforpricingandsurveillance,
outperforming heuristic rules in backtests (Saha et al., 2024). This aligns with desk workflows such
as peer price checks conditioned on risk, tax status, and structure, monitoring category drift, and
identifying comparable trades.
Similarityinmunisgoesbeyondtabulartermslikecoupon,maturity,orratings. Textualdisclosures
inofficialstatementsaddinsightonpledgesandcovenants,andtheircomplexityisitselfpriced(Farrell
et al., 2023). Relational signals such as co-holdings, issuer hierarchies, and geography help stabilize
cohorts when trading is sparse. Evaluation emphasizes operational validity: stability over rolling
windows, substitutes under liquidity constraints, and agreement with expert judgment. Marketwide
municipal securities statistics1 provide baselines for coverage, turnover, and regime shifts.
Securitized credit: MBS, CMBS, ABS
In Mortgage-Backed Securities (MBS) and Asset-Backed Securities (ABS), substitution and risk are
contingent upon borrower behavior, particularly prepayments and defaults. Classical models segment
poolsbyloanandmacrocharacteristicssuchascoupon,seasoning,andgeography,andestimatecohort-
level termination hazards (Kang & Zenios, 1992). Bayesian approaches model prepayment at the pool
level with hierarchical mixtures, capturing path dependence and unobserved heterogeneity.
In commercial Mortgage-Baked Securities (CMBS), the key dimension of similarity is termination
risk, since prepayment and default drive pricing and surveillance. Early loan-level hazard models pro-
vided a natural basis for peer cohorts by segmenting mortgages with comparable termination propen-
sities (Ambrose & Sanders, 2003). Mixture survival methods sharpen these cohorts by distinguishing
long-term survivors from at-risk loans (Yildirim, 2008). Geography also matters: local economic con-
ditions such as property values, unemployment, and house price appreciation significantly improve
default modeling and should be built into similarity neighborhoods (An et al., 2013). Evidence from
special-serviced loans shows that workout strategies and default probabilities depend on market con-
ditions, supporting grouping stressed loans by resolution path (Chen & Deng, 2013). Pricing also
reflects information frictions: origination channel (conduit vs. portfolio) introduces systematic differ-
1https://www.msrb.org/
13

ences consistent with adverse selection, which means similarity models for pricing must account for
dataprovenance(Anetal.,2011). Takentogether, effectiveCMBSpeersetsrelyonhazard-consistent
features such as contract terms, collateral, geography, macro drivers, and origination channel, rather
than surface descriptors.
Housing and collateral markets (linkages to fixed income)
Housepriceandcollateralriskmodelsincreasinglyrelyonrepresentationlearningfromspatial,textual,
and visual data. Vision and multimodal embeddings that combine property photos with street and
satellitecontextimprovevaluationandcomparablessearchrelativetotraditionalmethods(Poursaeed
et al., 2017; Law et al., 2019; Nouriani & Lemke, 2022). At scale, Siamese networks learn “similar
home” embeddings that drive recommendations and peer retrieval, showing how task-aligned similar-
ity supports comparables in live marketplaces2. Graph and spatial embeddings extend this further
by incorporating neighborhood amenities and geographic context. For example, multipartite graphs
thatlinkhomestonearbypointsofinterestimprovepredictionaccuracy,whileattention-basedspatial
interpolation weights neighbors according to learned relevance. Both approaches strengthen compara-
bles and provide robust stress testing for collateralized products (Das et al., 2021; Viana & Barbosa,
2021).
Fund Clustering and Similarity
Peergroupingiscentraltofundanalysis. Allocators,suchasmulti-assetmanagersandconsultants,use
peergroupstoconstructbalancedportfolios,testwhetherexposuresareredundantorcomplementary,
and design allocations that deliver real diversification. Fund selectors on advisory platforms rely on
peer groups to find comparables and to spot outliers that drift from their stated style or category,
which can reveal opportunities or hidden risks. Sales and product teams apply similarity to identify
competitor funds that can be substituted with home-grown products on recommended lists, a process
that requires precise and auditable measures of substitutability. Regulators and oversight bodies also
usepeeranalysistocheckthatfundsaremarketedconsistentlywiththeirmandatesandthatholdings
and performance align with disclosures.
Across these use cases, the peer group is a critical tool. It guides allocation and diversification,
supports distribution and competitive positioning, diagnoses style drift or innovation, and enforces
compliance with disclosure standards.
2https://www.zillow.com/tech/embedding-similar-home-recommendation/
14

Categorizations, Clustering and Similarity for Funds
ETFs are often analyzed alongside mutual funds in peer-group pipelines. Early work relied on return-
based style analysis, with Sharpe’s method providing a disciplined way to decompose returns into
style exposures and guide category design (Sharpe, 1992). Marathe & Shawky (1999) documented
misclassifications in vendor taxonomies by applying return-based clustering, starting with K-means
and related methods. Similar findings emerged in studies of equity and mutual fund categories (Kim
et al., 2000).
Through the 2000s and 2010s, clustering was used to uncover structure beyond static labels. Non-
linearmethodssuchasself-organizingmapsrefinedorchallengedofficialcategories,asshowninSpanish
mutualfunds(Morenoetal.,2006). Double-stageclusteringcompressedperformanceandriskmeasures
beforegroupingthemintointerpretablecohorts(Menardi&Lisi,2015). Florietal.(2021)shiftedfrom
returns to holdings, capturing similarity through portfolio commonality. Network views of fund–asset
bipartite graphs revealed how popular versus niche holdings relate to performance and crowding risk.
Foryears,unsupervisedclusteringwasusedasabenchmarkagainstvendorlabelslikeMorningstar3
and Lipper4, with the assumption that disagreement implied flawed categories. Desai & Mehta (2021)
demonstrated that this was misleading, as clustering outcomes depend heavily on feature choice, dis-
tance metrics, and hyperparameters; thus, divergence often reflects algorithmic bias rather than label
failure. Castellanos et al. (2024) and Desai et al. (2023) reinforced this by stressing the role of evalua-
tiondesign. Toresolvetheissue,supervisedvalidationframeworkshavedemonstratedthatcategories,
such as those used by Morningstar, are reproducible with fund features, proving they are systematic
rather than arbitrary (Mehta et al., 2020). Later work applied metric learning and supervised sim-
ilarity to extend these taxonomies, aligning distance functions with declared categories and flagging
inliers and outliers in a manner that is transparent to practitioners and regulators (Desai & Mehta,
2021; Desai et al., 2023).
Recentworkexpandsfundsimilarityinthreedirections. DeMigueletal.(2023)showedthatsuper-
visedmodelsonfundcharacteristicscanidentifymanagerswithpersistentpositivealpha, highlighting
predictive modeling as a complement to similarity analysis. Mart´ın-Melero et al. (2025) compared
sector involvement with financial features for ESG scoring, finding that tree-ensemble methods per-
form robustly across modalities. Zou & You (2025) proposed an integrated framework that clusters
fundsbyperformancepatternsandthentestsgrouppersistence,outperformingstyle-boxbaselinesand
producing persistence-aware peer sets for monitoring.
Supervised similarity frameworks bring these elements together by quantifying how far a fund is
3https://advisor.morningstar.com/Enterprise/VTC/MorningstarCategoryClassificationforFunds_
October2024.pdf
4https://lipperalpha.refinitiv.com/lipper/fund-classifications/
15

from its declared category and flagging outliers with diagnostics that are transparent to selectors and
oversight teams (Desai et al., 2023). Recent work extends this approach with open-set recognition.
For example, Random Forests can be enhanced with distance-based rules that both classify funds into
known categories and detect when a fund lies outside all recognized clusters (Feng et al., 2024).
Similarity also strengthens explainability. Yampolsky et al. (2024) introduced case-based methods
for Random Forests that highlight prototypes, critics, counterfactuals, and semifactuals from training
data to clarify why a model produced a given outcome. Applied to funds, this means that similarity
tools can retrieve nearest peers, surface representative exemplars, and flag boundary cases, offering
interpretable diagnostics that help selectors and auditors trust and act on the results.
Clustering and Similarity of Funds Based on Returns
InfundsandETFs,returnhistoriesareapracticalbasisforpeerdiscoveryandstylechecks. Earlywork
clusteredreturnpathsintointerpretableexposures,creatingpeergroupsthatcouldbemaintainedwith
minimallabeling(Pattarinetal.,2004). Subsequentstudieslinkedfunduniqueness,measuredrelative
totime-seriesneighbors,toflows,fees,andalphapersistence(Vozlyublennaia&Wu,2016). ForETFs,
distance choice matters—Euclidean, DTW, and shape-preserving methods produce different clusters,
especially during shocks like COVID, and influence portfolio construction (Ito et al., 2021).
Noise-reductiontechniques,suchascorrelation-matrixfiltering,helprecoverETFgroupingsconsis-
tent with taxonomies (Polinesi & Recchioni, 2021). Returns-plus-risk approaches add volatility states
to the model, yielding peer sets that capture co-movement and regime-sensitive risk (Lisi & Otranto,
2008).
Clustering and Similarity based on other data modalities
Beyond flat labels, graph embeddings of fund–holding networks such as node2vec generate Fund2Vec
representations that capture relational structure, supporting peer search, recommender systems, and
competitor analysis (Satone et al., 2021). Related work adapts language models like Word2Vec and
BERTtocreateassetembeddingsfromportfoliostructures,whichimprovethepredictionofvaluations,
co-movement, and trading activity (Gabaix et al., 2024). Text-based methods also contribute: NLP
on prospectuses and strategy descriptions reproduces category systems and produces semantic fund
embeddings that align with practitioner views of peers (Vamvourellis et al., 2022).
Table 7 summarizes clustering and similarity methods and their applications for funds.
16

Company Clustering and Similarity
Identifying comparable companies supports valuation, risk management, strategy, and sales. Analysts
use peers for relative valuation by applying multiples, while risk teams and portfolio managers rely
on peer groups to diversify, hedge, and monitor exposures. Corporate strategy teams benchmark
competitors and map markets, Mergers & Acquisitions (M&A) professionals search for targets with
similarprofiles,andcommercialorunderwritingdesksusepeersforleadgenerationandriskassessment.
Robustsimilaritymeasures,therefore,strengthendecision-makingbyaligningcompanyneighborhoods
with the attributes that matter in each workflow.
Traditional taxonomies such as SIC (Guenther & Rosman, 1994) and GICS5 offer a baseline for
defining peers, but they are coarse and static. Firms sharing the same industry code can differ sub-
stantially in terms of products, customers, or technology, and such labels do not produce ranked peer
listsnecessaryforcomparablesandsurveillance. Theseshortcomingsmotivatedata-drivenapproaches
that integrate fundamentals, time-series signals, text, graphs, and alternative data into continuous
similarity scores and flexible clusters for both public and private firms.
Traditional approaches and their limits
Historically, practitioners supplemented industry codes with financial-ratio comparisons and simple
clustering. (Bhojraj & Lee, 2002) showed that selecting peers from fundamentals rather than labels
improved screening and explanatory power. Classification from financial statements alone can recover
sectors with reasonable accuracy using tree or boosting models (van der Heijden, 2022). Meanwhile,
networkheuristics,suchas“common-analyst”coverage,alsosignalrelatednessacrossfirms(Kaustia&
Rantala, 2021). These methods were useful but limited, as they ignore qualitative aspects of business
models and lack the multimodality and adaptivity now required for large-scale peer analysis.
Modern data-driven approaches by modality
Machine learning (ML) on fundamentals supports goal-specific peer sets and clustering. Correlation-
based methods have been used to form tradable portfolios for asset pricing (Ahn et al., 2009) and
to classify stocks into groups that maximize Sharpe ratios in mean-variance frameworks (Kim et al.,
2014). Other work applies K-medians or metric learning on financial ratios (Cai et al., 2016; Dzuba &
Krylov, 2021), and designs “financial clusters” from statement structures that sharpen explanations
beyond industry codes (Fodor et al., 2021). Supervised relative valuation methods use ML to express
5https://www.msci.com/our-solutions/indexes/gics
17

predicted multiples as peer-weighted averages, creating valuation kernels that are interpretable and
aligned with comparables (Geertsema & Lu, 2023).
On the time-series side, similarity is often judged by return co-movement. Equity2Vec links news
co-mentions, technical indicators, and sentiment to capture evolving cross-company relations, im-
proving prediction accuracy and trading profitability (Wu et al., 2021). SimStock tackles market
non-stationarity by treating time periods as separate domains and modeling parameter drift, blending
time-seriesfeatureswithfirmfundamentals(Hwangetal.,2023a). Otherapproachesdemonstratethat
sparse-autoencoder text embeddings improve correlation alignment compared to standard taxonomies
(Molinari et al., 2024), while evolving probabilistic industry mixtures outperform GICS in predicting
correlations (Papenkov, 2024).
Multimodalpipelinesarealsoemerging. CUBANcombinestextualdescriptionswithpeerfinancials
to forecast revenue and profitability, highlighting how comparables-informed features can enhance
predictive performance (Bae & Hyde, 2024).
Textual data (NLP-based similarity). Text offers a way to capture product–market proximity
and competitive positioning beyond numeric features. Early work showed that cosine similarity of
10-K descriptions reveals competitors, supports M&A analysis, and builds evolving industry networks
(Hoberg & Phillips, 2010). Modern LLM-based methods embed company descriptions to reproduce
GICS-likestructureswhileenablingcontinuouspeerrankingandperformancealignment(Vamvourellis
et al., 2024). Benchmarks across transformers and classifiers show strong sector classification from
text alone, with LLM-generated augmentation improving robustness (Rizinski et al., 2024). Hybrid
approaches that link narratives to accounting features boost both accuracy and interpretability in
sector prediction (Dzuyo et al., 2025).
Beyond filings, unstructured website text and images can be embedded for peer identification
and alternative industry segmentation, outperforming traditional NACE codes (Gerling, 2024). The
THEME framework aligns firm profiles with thematic descriptions and return dynamics, producing
adaptive embeddings for theme-based investing (Lee et al., 2025). Multi-task BERT fine-tuning on
annual reports has also been used to jointly learn sector classification, return similarity, and sector
naming (Ito et al., 2020).
Governance needs drive demand for interpretable similarity. Sparse autoencoders can disentangle
LLM embeddings into transparent factors linked to fundamentals and returns (Molinari et al., 2024).
Probabilistic multi-industry models further allow firms to load on several evolving topics, reflecting
conglomerationandindustrychange(Vamvourellisetal.,2024;Papenkovetal.,2023;Papenkov,2024).
Finally, text-driven retrieval powers interactive peer-search systems that combine LLM reading, API
18

queries, and ranking for live company lists (Patil et al., 2025).
Graph and network data. Relational data, such as supplier–customer ties, partnerships, shared
investors, and board interlocks, capture economic proximity that fundamentals or text may overlook.
CompanyKGbuildsalarge-scaleknowledgegraphwithheterogeneousrelationsandnodetextfeatures,
providingbenchmarktasksforsimilaritypredictionandcompetitorretrieval(Caoetal.,2024). Results
show the value of combining node, edge, and hybrid information to quantify peers. Graph methods
such as GNNs and link-prediction models learn embeddings that reflect multi-hop relationships and
complement NLP by re-ranking text-based candidates with relational evidence. Earlier heuristics like
common-analyst coverage also fit naturally as edges in this broader graph view (Kaustia & Rantala,
2021).
Other studies model the correlation matrix itself as a graph. Sarmah et al. show that learning
nodeembeddingsfromsuchgraphsmapscorrelatedstocksintoalow-dimensionalspace,enablingpeer
discovery, portfolio diversification, and systemic risk monitoring (Sarmah et al., 2024).
Images and alternative data. Visual cues (product imagery, brand style) and digital traces (web
and app usage) can provide orthogonal signals of market positioning, especially in consumer-facing
domains. Emerging work shows image embeddings can retrieve plausible peers and complement
text/graph views (Kaczmarek & Pukthuanthong, 2024). While not yet mainstream in academic liter-
ature, these features increasingly appear in proprietary pipelines and can refine neighborhoods when
combined with fundamentals, text, and graphs.
Private company similarities. Private company similarity is of growing importance for valuation,
underwriting, venture capital, and corporate strategy. Private-to-private similarity supports tasks
such as benchmarking financial performance among financial analysts, detecting high-growth firms,
screening for credit risk cohorts, and mapping competitive landscapes in opaque markets. Private-
to-public similarity enables anchoring startups to listed peers for relative valuation, benchmarking of
disclosure and ESG alignment, and constructing synthetic price or risk proxies where no market data
exist. Together, these workflows extend the reach of clustering and similarity learning from liquid,
information-rich public issuers into domains where traditional comparables are sparse but decision-
making still demands peer sets.
Afirstlineofresearchleveragesstructuredregistrydata suchasBureauvanDijk’sOrbis tobuildfi-
nancialpanelsofprivatefirms. Studiesshowthatfinancial-ratioclusteringcanrecoversectorstructures
and support benchmarking of profitability, leverage, and cash–flow patterns at scale (Kalemli-O¨zcan
et al., 2024). Time-series analyses of private firms’ employment or sales trajectories classify growth
19

paths (for example, rapid-growth “gazelles” versus stable incumbents) via trajectory-aware cluster-
ing (Delmar et al., 2003; Coad, 2009). These approaches ground peer discovery in accounting and
real-economy signals where coverage is sufficient.
When structured financials are missing, textual data become the dominant modality. Company
descriptions, website blurbs, and profile summaries are encoded into embeddings to align startups
with both private and public peers. For example, Company2Vec produces text-based embeddings
of German companies for competitor retrieval (Gerling, 2024), while topic models and transformer
embeddings map global startup ecosystems (Savin et al., 2023). These text-driven methods enable
semantic comparables where numeric data are sparse.
Graph and alternative data extend coverage further. Large-scale heterogeneous knowledge graphs,
such as CompanyKG (Cao et al., 2024), integrate millions of public and private firms with relational
edgesthatspaninvestors,boardmembers,partnerships,andco-mentions. Graphneuralnetworksand
link-prediction models learn embeddings that more accurately recover competitors and partners than
textalone. Complementarysignalsfromimageryanddigitaltracesalsoemerge: productphotos,brand
cues, andappusagedatacanpositionconsumer-facingfirmssemantically, enrichingprivate-to-private
comparables (Kaczmarek & Pukthuanthong, 2024). Together, these strands show that multimodal
similaritysystemscanextendvaluation,strategy,andrisktoolsintotheopaqueworldofprivatefirms,
supporting both intra-private benchmarking and mappings onto public market anchors.
Investors Clustering and Similarity
Worldwide,financialinstitutionsaretaskedwithunderstandingtheirclientbase. Basedonthisunder-
standing,theseinstitutionsrecommendseveralassetsandmonitortheperformanceofclientportfolios.
Theyareoftenrequiredtoupdatetheirunderstandingofclientsastheirdecision-makingchangesover
time,asinvestmentneeds,includingfinancialobjectivesandrisktolerancechangeasclientsageandlife
situations change. This understanding can be gained by measuring investor risk tolerance (Thompson
et al., 2022) and risk aversion (Grable et al., 2024) relative to portfolios through statistical quantities.
Similarity learning offers an alternative approach to measuring clients’ risk by understanding clients
as different investor types and their relation to an institution’s overall portfolio.
Investor decision-making and risk assessment frameworks
Before discussing similarity learning for assessing investor risk and suitability, we first clarify how
clients make investment decisions and how these decisions can be mapped to regulatory and practical
frameworks. Investor profiling seeks to directly elicit preferences, risk tolerance, and time horizons
20

from clients, while revealed behavioral analysis focuses on comparing these elicited preferences with
actual investment choices (Faff et al., 2004).
How individuals make investment decisions, and particularly how they understand, tolerate, and
manage financial risk, has been a central concern in regulatory practice. At a high level, regula-
tors, such as the Financial Industry Regulatory Authority6 (FINRA) of the USA and the Canadian
InvestmentRegulatoryOrganization7 (CIRO)ofCanada,developsuitabilityregulationsforsecurities-
related commerce to protect investors. They require collecting client information, including identity,
investment needs, financial objectives, and circumstances, as well as risk tolerance, to ensure that
recommended products and behaviors align with client financial goals. In practice, firms implement
suitability largely through onboarding processes, such as questionnaires and demographic screenings.
Classical risk assessment approaches have been used in financial institutions for decades. Suitability
assessmentsoftenusequestionnaire-basedmethods,riskassessmenttools,andassetcalculators,among
others,whichcanthenbeusedtorecommendsuitableassetsforportfoliosBaloyi&Lotter(2024)and
informrisktolerancescalesThompsonetal.(2022),therebygroupingclientsintobroadriskcategories.
A central question in academic research surrounding suitability is whether current investor risk
assessments meaningfully reflect behavioral realities: does this investment decision align with this
client’sfinancialgoals? Recentworkshowsthatelicitedattributesoftendivergefromobservedactions,
whichraisesconcernsaboutwhetherexistingstandardsreliablyguideinvestorstowardsuitablechoices
or leave gaps in protection due to behavioral mismatches or inconsistent implementation.
Methodological applications
Clustering and similarity learning have been applied in a variety of contexts; however, an important
and sometimes difficult question is choosing a clustering method that is best suited for a specific
financial dataset. These evaluations include cluster cohesion and separation, similarity choice, and
computational cost, where no single method dominates in all respects (Kou et al., 2014).
The choice of method can substantially affect insights, as illustrated in two recent studies using
a financial wellness survey. One study focused on using the K-means approach to clustering (Phelps
& Metzler, 2024), whereas a follow-up study extended this analysis using seven different distance
metrics (Ghashti & Thompson, 2023). The first, using knowledge- and skill-based measures, identifies
four clusters and emphasizes gaps between self-assessed and actual financial knowledge, which reveal
risks of overconfidence and misperceived literacy. The second approach, using dissimilarity learning
on mixed-type data, yields two clusters that differ primarily in terms of housing affordability, debt,
budgeting, and retirement strategies. Although each method utilizes different similarities, they both
6https://www.finra.org/rules-guidance/rulebooks/finra-rules/2111
7https://www.ciro.ca/newsroom/publications/guidance-know-your-client-and-suitability-determination
21

demonstratethatfinancialwellnessencompassesbothcognitivemisalignmentsandcontextualstressors.
Asthereareno“true”clusters,differentsimilarityandclusteringapproachesofferuniqueinsightsinto
the same data that must be analyzed by finance-domain experts.
Behavioral finance, similarity learning and household finance
Identifying meaningful similarities between client trade and transaction behaviors help to group them
into distinct investor types. Evidence from household finance shows that individuals with similar
profiles on traditional financial data (such as income, education level, and self-assessed risk tolerance)
often diverge in their actual saving, borrowing, and investment behaviors. Recent applications of
clusteringandsimilarityforinvestorclassification(Thompsonetal.,2021)addressthisgapbyrevealing
misalignments between elicited investor profiles and observed decision-making.
Deep clustering has been used to identify heterogeneity in household financial behaviors that con-
ventional demographics overlook (Hwang et al., 2023b). K-means clustering was used on literacy
measures to reveal gaps between self-assessed knowledge and decision-making (Phelps & Metzler,
2024; Hwang et al., 2024). De Luca & Mehta (2023) studied investments in ESG among 5.5 million
households using K-Modes clustering to identify five distinct investor types.
Determining similarity between clients allows financial institutions to better understand how their
clients react to market stimuli and give better advice that aligns clients with their financial goals.
Adaptive similarity learning methods for local information of financial information relevant to cluster-
ing allow methods to adapt to each unique financial dataset. Kernel metric learning has been used for
clustering trade and transaction data of clients to determine trading behaviors under the guidance of
financial advisors and during financial market crashes (Ghashti & Thompson, 2023, 2025a,b).
Pagliaro et al. (2021) analyzed over 1.5 million handwritten and drop-down notes written by fi-
nancial advisors using a Customer Relationship Management system. They used the natural language
processing method of Word2Vec to summarize textual information and achieve semantic similarity
amongst a corpus of text, and then used logistic regression, decision trees, and gradient boosting to
classify whether an investor would decide to move all assets to cash. Shiao et al. (2022) further used
advisor notes, trade and transaction data, digital activity (such as log-ins, emails, and calls), and the
VIX index with gradient boosting trees to predict whether investors would make similar impulsive
trading decisions.
Kim et al. (2023) extended the healthcare analogy of “diagnosis and prescription” to the financial
domain by introducing a healthcare diagnostic framework, Risk Information-adjusted Hierarchical
Autoencoder (RI-HAE), that generates household financial risk scores. Health-state clustering groups
households by similarity and stratifies them into risk-based clusters. In the context of future health
22

costs, Tan & Mehta (2022) applied K-modes clustering to a health and retirement study and found
that their categorizations yielded more accurate cost estimates for personalized retirement planning.
Clustering and Similarity for Other Asset Classes
This section reviews how clustering and similarity are applied beyond the core domains of equities,
fixed income, funds, companies, and investors. We highlight use cases in commodities, currencies and
foreign exchange, derivatives, and real estate (REITs). For each market, we start with practitioner
applications and then summarize traditional and modern methods, organized by data type.
Commodities
Peergroupsincommoditiessupportdiversificationandhedgingacrossenergy,metals,andagriculture,
help identify substitutes such as edible oils or battery metals, and interpret futures curves in terms of
contango or backwardation relative to inventory and convenience yields (Gorton et al., 2013).
Traditional approaches. Early studies showed that commodities often move together despite dif-
fering fundamentals (Pindyck & Rotemberg, 1990). Clustering methods such as correlation networks
and minimum spanning trees group assets into intuitive clusters like energy, precious metals, and
agriculture, and track how these groups evolve over time (Lucey et al., 2011). Volatility-spillover
similarityaddsdirectionality, distinguishingcommoditiesthattransmitshocksfromthosethatabsorb
them (Diebold & Yilmaz, 2012). Clustering can also be applied to futures curves: common contango
or backwardation patterns reflect shared storage and carry dynamics, offering a basis for grouping
commodities by market structure (Gorton et al., 2013).
Modern approaches (dynamic networks and multi-factor curves). Recentstudies(Maetal.,
2021;Ouyangetal.,2022;Dahletal.,2020;Szender´ak,2018)combinedynamiccorrelationwithMSTs
or connectedness indices to track evolving clusters and risk transmission. For specific complexes (such
as oil), multi-factor models of the entire futures curve provide a compact representation of curve
similarity across time and maturities (Cortazar & Naranjo, 2006). Results consistently show energy
and precious metals form tight clusters, with agriculture being more diverse.
A complementary perspective is offered by Chen et al. (2021), who apply unsupervised learning to
both the cross-section of commodities and the time dimension of trading days. Using k-means and
hierarchical clustering on logarithmic returns (with manifold learning via Multi-dimensional Scaling
and t-SNE for visualization), they recover economically interpretable peer groups across fuels, metals,
and agriculturals. Crucially, they also cluster the transpose of the panel, grouping trading days by
conditional volatility (GARCH-based), which reveals market regimes without imposing ad hoc crisis
23

dates. For practitioners, this two-way clustering links instrument similarity (what trades together)
with regime similarity (when markets behave alike), enabling regime-aware hedging and monitoring.
Currencies (Foreign Exchange)
Similarityinforeignexchange(FX)mattersdirectlyforriskmanagementandtrading. Itguideshedge
programdesignbygroupingcurrenciesintonaturalblocks,whichrevealshowshocksandinterventions
propagateacrosstheFXnetwork, andidentifiessafe-havenclusterssuchastheUSdollar, Swissfranc,
or Japanese yen that play a central role in risk parity and drawdown control.
Traditional approaches. Earlystudiesshowthatexchangeratesoftentransactatroundnumbers,
with the strength of price clustering varying across currencies and trading platforms (Sopranzetti &
Datar, 2002). Hierarchical clustering applied to return correlations or cointegration has long been
used to identify regional blocks and key hub currencies (Kwapien et al., 2009; Wu & Zheng, 2013).
(Scarlat et al., 2007) examined transitional economies and highlighted self-similar scaling properties
in currency dynamics, suggesting deeper structural clustering even beyond correlation. (Wang et al.,
2012) extended this work using DTW to measure similarity between entire return paths, producing
minimum spanning trees that provide intuitive maps of the FX market structure.
Modern approaches. Recent work emphasizes the use of more complex similarity metrics and
dynamic community detection. Mizuno et al. (2006) and Fenn et al. (2012) showed that correlation
networksandcommunitydetectionmethodsuncovercurrencygroupsthatevolveovertimeinresponse
to crises and interventions. Chakraborty et al. (2020) proposed similarity metrics based on the dis-
tribution of return fluctuations, recovering a hierarchical structure of the global FX market that goes
beyond correlations. Fernandes et al. (2023) employed hierarchical clustering to compare West Texas
Intermediate (WTI) oil, fiat currencies, and foreign exchange rates, identifying coherent clusters that
spanned across asset classes, thereby highlighting the integration of energy and foreign exchange mar-
kets. Kremer et al. (2019) demonstrated that political and economic events alter clustering dynamics,
changing the role of safe-haven currencies.
Derivatives
Similarity in derivatives helps in three main ways. It allows contracts to be grouped by their key risk
exposures,suchasdelta,gamma,orvega(theoptionsGreeks),reducesthecomplexityoflargetrading
books by creating representative hedging clusters, and makes it possible to compare volatility surfaces
and curve shapes across different underlyings to spot risks and relative-value opportunities.
24

Traditional Approaches. Option prices across strikes and maturities can be summarized by the
implied volatility surface. This surface provides a natural way to measure similarity: contracts or
markets with similar surface shapes behave alike. Empirical studies show that only a few factors
explain most of the surface variation, so options can be clustered by their factor loadings or by the
overall shape of their volatility surface (Derman & Kani, 1994).
Modern Approaches. In practice, traders already group options by sensitivities such as delta,
gamma, and vega. Recent learning-based hedging frameworks formalize this by clustering contracts
with similar exposure profiles, simplifying execution and valuation adjustments (Buehler et al., 2019).
In rates and commodities, contracts are naturally organized by the shape of their term structures.
Classic studies showed that government bond yields can be explained by a few factors—level, slope,
and curvature that capture most variation in returns (Litterman, 1991). This factor view underpins
modern practice: bonds or swaps with similar loadings are treated as substitutes, and clustering by
factor exposures is standard in fixed-income risk management. In commodities, futures curves are
summarized in a similar way. Cortazar and Naranjo (Cortazar & Naranjo, 2006) show that two or
three Gaussian factors describe oil futures, with peer contracts defined by comparable responses to
contango or backwardation shifts.
Acrossassetclasses,clusteringinstrumentsbyfactorloadingsprovidesacompactandeconomically
interpretable method for managing large derivative books.
Real Estate/REITs
InlistedrealestateandREITs,clusteringbygeographyorpropertytypehelpsdefinepeersandmanage
riskacrossregionsandsectors. Forinsurance-linkedsecurities,similaritycomesfromcontractfeatures
such as peril, trigger design, and expected loss, allowing contracts with comparable structures to be
grouped for pricing, benchmarking, and portfolio construction.
Earlystudies(Gyourko&Keim,1992;Ling&Naranjo,1997;Goetzmann&Wachter,1995)showed
that real estate securities co-move with economic and financial factors and are closely tied to equities.
This creates a natural basis for clustering: securities with similar factor exposures or geographic and
sector footprints form peer groups that support benchmarking and risk analysis.
Economic Scenario Clustering and Similarity
Banks,insurers,andassetmanagersmaintainlargescenariolibrariesforregulatorystresstestssuchas
ComprehensiveCapitalAnalysisandReview(CCAR)andEuropeanBankingAuthority(EBA),aswell
as for internal capital, Asset–Liability Management (ALM), and top-down risk exercises. Clustering
25

andsimilaritymakethesesetsusablebycuratingdiversebutnon-redundantscenarios,reducingMonte
Carlo paths to tractable representatives, and assessing severity, novelty, and alignment with portfolio
sensitivities such as credit, rates, housing, and labor. They also improve governance by ensuring
scenario selection is auditable and reproducible Borio et al. (2014).
Data modalities. Scenario data appear in four forms: (i) paths (multivariate trajectories of GDP,
unemployment, inflation, and so on); (ii) trees (multistage Monte Carlo or ESG outputs); (iii) pan-
els (mixed-frequency macro indicators); and (iv) narratives (qualitative supervisory texts linked to
quantitative paths).
Classical foundations Scenario reduction addressestheproblemthatMonteCarloenginesproduce
thousands of macro paths while regulators and managers need only a few. Forward and backward
selection prune paths using probability distances such as Kantorovich or Wasserstein, preserving tail
risks while cutting redundancy (Dupaˇcov´a et al., 2003; Heitsch & R¨omisch, 2003). In clustering
terms,reductiongroupssimilarpathsandselectsprototypes,creatingcompressedyetdecision-relevant
libraries for ALM, energy, and solvency analysis.
Macro regime identification clusterstheeconomyacrosstime. Hamilton’sMarkov-switchingmodel
introduced latent states such as expansions and recessions (Hamilton, 1989), later extended with
dynamicfactormodelstocapturemultipleindicatorsjointly(Camachoetal.,2018). Theseframeworks
group periods with similar co-movements in GDP, unemployment, inflation, and financial variables,
providing practitioners with structured, regime-based similarity for forecasting and stress testing.
Actuarialeconomicscenariogeneratorssimulateinflation,rates,equities,andrealestateforinsurers
and pensions. Wilkie-style models capture long-run correlations, while Solvency II stresses calibration
and transparency Moudiki & Planchet (2016); Ahlgrim et al. (2005). Clustering and similarity prune
redundant scenarios to keep libraries of scenarios tractable, but regime coverage must be checked to
avoid losing rare stress states. Once the reduction is applied, quite a few governance and compliance
concerns can be resolved.
Modern methods Vanguard Research (2023) applied machine-learning clustering to classify capital
marketscenariosintofivestates(recession,recovery,expansion,slowdown,andhighinflation),showing
how unsupervised methods can build objective taxonomies for scenario analysis and portfolio design.
Trajectory similarity methods align cycles that differ in timing or intensity. Franses & Wiemann
(2020) used DTW to recover comparable phases even when shifted in time. Augustyn´ski & Lasko´s-
Grabowski (2018) applied DTW-based clustering to macro series, finding it more effective than corre-
lationwhenrecessiontimingvariesacrosseconomies. Raihan(2017)showedthatDTWimprovesU.S.
26

recession prediction, highlighting its early-warning value.
Stress-testingaftertheglobalfinancialcrisisemphasizedscenariosthatarebothsevereandplausi-
ble. Glassermanetal.(2015)proposedempiricallikelihoodmethodstogenerateextremebutconsistent
scenarios under supervisory limits. Aikman et al. (2024) introduced multi-scenario frameworks that
cluster adverse mixes, demonstrating that multiple grouped scenarios capture vulnerabilities better
than a single baseline.
Authorities now publish standardized paths. The Federal Reserve specifies GDP, unemployment,
housing,andfinancialvariables,enablingsimilaritychecksagainstpastvintagesfornoveltyandredun-
dancy8 . The EBA provides EU-wide templates that can be clustered with earlier designs to ensure
continuity while adapting to new risks9.
Recent work explores generative and multimodal methods. Gustafsson & Jonsson (2023) applies
WassersteinGANstogeneratesyntheticstress-testscenarios,showingadversarialtrainingcanreplicate
and diversify macroeconomic paths. These advances mark a shift toward pipelines where clustering
and similarity support reduction, evaluation, creation, and governance of scenarios.
Practical Tips for Practitioners
Clusteringandsimilarityarepowerfultools, buttheirvaluedependsondesignandgovernance. Afew
practical guidelines for financial modelers are below.
1. Defineevaluationmetricsbeforemodeling. Evenunsupervisedprojectsneedclearobjectives,
forexample, forbonds, testsubstitutionfidelity; forfunds, categoryreproducibility; forinvestors, seg-
ment stability. Choosing Metrics right at the beginning anchors the pipeline in practitioner relevance.
2. Start with simple, interpretable methods. Use transparent baselines like correlation clus-
tering, k-means, or hierarchical methods to set expectations. Only add advanced methods when
incremental gains are clear.
3. Match distance metrics to data. Choose metrics suited to modality: Gower for mixed tabular
data, DTW or correlation for time series, and so on. Avoid one-size-fits-all Euclidean distance.
4. Normalize and pre-process carefully. Scale and distribution differences distort similarity.
Apply z-scores, log transforms, and so on to ensure results reflect the financial structure rather than
units.
5. Use domain knowledge. Credit and liquidity matter for bonds, factors for funds, and risk toler-
ance for investors. Embed expert input through feature selection or must-link/cannot-link constraints
to ensure operational relevance.
8https://www.federalreserve.gov/publications/files/2024-stress-test-scenarios-20240215.pdf
9https://www.eba.europa.eu/risk-and-data-analysis/risk-analysis/eu-wide-stress-testing
27

6. Apply supervised similarity when labels exist. Ratings, fund categories, or client segments
allow supervised methods such as random forest proximities or Siamese networks. These produce
task-specific similarity and richer interpretability.
7. Check stability across time. Marketsshiftwithvolatilityandregimes. Userollingwindows,for
example,andtrackstabilitymetricssopractitionersknowwhenpeersetsarerobustorregime-specific.
8. Document assumptions and design choices. Under SR11-7, all features, preprocessingsteps,
metrics,andparametersmustberecorded. Cleardocumentationensuresreproducibility,transparency,
and regulatory acceptance.
9. Prioritize interpretability. Trust on the end results of clustering and similarity depends on
explanations. Feature importances, SHAP values, or case-based reasoning (Yampolsky et al., 2024;
Rosaler et al., 2024) show why entities are peers, which is critical in regulated contexts.
10. Plan for scale and production. Methods must scale to large universes. Use approximate
nearest neighbors, distributed computing, and retraining pipelines to meet production needs.
Taken together, these principles make clustering and similarity systems interpretable, stable, and
aligned with decision-making and governance.
Summary
Clustering and similarity learning have evolved from heuristic peer-grouping methods to become in-
dispensable tools across asset classes. Traditional approaches relied on static classifications such as
industry codes or style boxes, which offered only coarse approximations of economic relationships. In
contrast,moderntechniquesenableadaptive,data-drivenneighborhoodsthatbetterreflectactualrisk,
liquidity, and thematic exposures. By integrating clustering and similarity methods, practitioners can
build flexible frameworks that structure complex financial data in economically meaningful and oper-
ationally useful ways, positioning these methods as core components of investment analytics, portfolio
construction, and risk management systems. (Exhibits 6 to 12 summarize clustering and similarity
methods applied in different asset classes and data modalities.)
Acentrallessonofthetutorialisthatmodelingchoicesmustbecloselyalignedwiththecharacter-
istics of the data and the intended use cases. Different modalities (tabular fundamentals, time-series
returns, textual disclosures, and graphs) require distinct similarity techniques. Moreover, evaluation
must move beyond abstract academic metrics to focus on task-specific criteria such as substitution
fidelity, neighborhood stability, reproducibility, and utility in decision-making. These considerations
ensure that similarity systems are transparent, auditable, and robust across market regimes, making
them suitable for production deployment in regulated environments. Their applications are already
28

broad,spanningbonds,funds,companies,andinvestors,andarerapidlyextendingintonewerdomains
such as commodities, currencies, derivatives, and scenario generation.
Despitetheirpromise,clusteringandsimilaritymethodsfaceimportantpracticalchallenges. Their
outputsareoftensensitivetoinitialconditionsandhyperparameterchoices,makingresultsfragileand
potentially unstable. Interpretability is another major hurdle: many high-performing models, espe-
cially deep learning approaches, operate as “black boxes,” complicating accountability to clients and
regulators. Additionally, similarity is inherently subjective and context-dependent, varying according
to the analytical task, data modality, and market regime. These factors underscore that no single
notion of similarity applies universally across all financial contexts.
The tutorial ultimately delivers a pragmatic message: clustering and similarity learning are no
longer experimental techniques but essential, embedded components of modern financial workflows.
Toresponsiblyharnesstheirfullpotential,practitionersmustdesignrobust,interpretable,andaligned
models that align with fiduciary objectives. This requires thoughtful model selection, careful evalua-
tion, and transparent governance. By addressing these issues directly, clustering and similarity frame-
workscanprovidepowerfultoolsforstructuringfinancialinformation,enhancingdecision-making,and
meeting regulatory expectations.
Several domains remain under-explored but highly promising for clustering and similarity: com-
modities, derivatives, private markets, and ESG. In particular, similarities across private equity, pri-
vate credit, private-to-public transactions, and so on are expected to become major focus areas for
researchersinthenearfuture. Advancesinmultimodallearning,regime-awaresimilarity,andopen-set
recognition will shape the next wave of applications.
Acknowledgments The views expressed here are those of the authors and not of BlackRock, Inc.
DM thanks all his collaborators on this topic over the years: Victor Allen, Nathalia Castellanos,
Rishab Chauhan, Peter Chu, Thomas de Luca, Dhruv Desai, Ashmita Dhiman, Guanchao Feng,
Eduardo Fontes, Sebastian Frank, Harrison Garber, Joshua Harvey, Riya Jain, Jerinsh Jeyapaulraj,
Sweet Kaur, Andrew Leba, Jay Klein, Mingshu Li, Jingrao Lyu, Nayana Nair, Deran Onay, Cyn-
thia Pagliaro, Stefano Pasquali, Jithin Pradeep, Joshua Rosaler, Preetha Saha, Anusha Sai Meesala,
Bhaskarjit Sarmah, Deepika Sharma, Tushar Sharma, Han-tai Shiao, Philip Sommer, Michael Stern-
berg, Fu Tan, Jeff Tang, Dimitrios Vamvourellis, Vipul Satone, Shaofei Wang, Luwei Xiong, Bill Xu,
TinaZhao. DMespeciallythanksDhruvDesaiforwonderfulcollaborationsandstimulatingdiscussions
on these topics over the years.
29

References
Kevin C Ahlgrim, Stephen P D’Arcy, and Richard W Gorvett. Modeling financial scenarios: A
framework for the actuarial profession. Proceedings of the Casualty Actuarial Society, 92(177):177–
238, 2005.
Dong-Hyun Ahn, Jennifer Conrad, and Robert F Dittmar. Basis assets. The Review of Financial
| Studies, | 22(12):5133–5174, | 2009. |     |     |     |     |     |
| -------- | ----------------- | ----- | --- | --- | --- | --- | --- |
David Aikman, Romain Angotti, and Katarzyna Budnik. Stress testing with multiple scenarios: A
tale on tails and reverse stress scenarios. Technical Report 2941, European Central Bank, 2024.
Brent W. Ambrose and Anthony B. Sanders. Commercial mortgage-backed securities: Prepayment
and default. The Journal of Real Estate Finance and Economics, 26(2-3):179–196, 2003.
Xudong An, Yongheng Deng, and Stuart A. Gabriel. Asymmetric information, adverse selection, and
| the pricing | of cmbs. Journal | of Financial | Economics, |     | 100(2):304–325, |     | 2011. |
| ----------- | ---------------- | ------------ | ---------- | --- | --------------- | --- | ----- |
XudongAn,YonghengDeng,JosephB.Nichols,andAnthonyB.Sanders. Localtraitsandsecuritized
commercial mortgage default. The Journal of Real Estate Finance and Economics, 47(4):787–813,
2013.
Iwo Augustyn´ski and Pawel(cid:32) Lasko´s-Grabowski. Clustering macroeconomic time series. Econometrics.
| Ekonometria. | Advances | in Applied Data | Analytics, |     | 22(2):74–88, | 2018. |     |
| ------------ | -------- | --------------- | ---------- | --- | ------------ | ----- | --- |
SiwooBaeandDavidHyde.Cuban: Leveragingsemanticcomparablestopredictfinancialmetricsusing
textual descriptions of companies. In 2024 IEEE International Conference on Big Data (BigData),
| pp. 4819–4827. | IEEE, | 2024. |     |     |     |     |     |
| -------------- | ----- | ----- | --- | --- | --- | --- | --- |
Solani Baloyi and Melany Lotter. Suitability of risk assessment tools used during the portfolio recom-
mendation process. Journal of Economic and Financial Sciences, 17(1):896, 2024.
NicholasBarberis,AndreiShleifer,andJeffreyWurgler. Comovement. Journal of financial economics,
| 75(2):283–317, | 2005. |     |     |     |     |     |     |
| -------------- | ----- | --- | --- | --- | --- | --- | --- |
Sanjeev BhojrajandCharles M. C.Lee. Whois mypeer? a valuation-basedapproachto theselection
| of comparable | firms. Journal | of Accounting |     | Research, | 40(2):407–439, |     | 2002. |
| ------------- | -------------- | ------------- | --- | --------- | -------------- | --- | ----- |
Claudio Borio, Mathias Drehmann, and Kostas Tsatsaronis. Stress-testing macro stress testing: does
| it live up   | to expectations? | Journal of | Financial | Stability,  | 12:3–15, |       | 2014. |
| ------------ | ---------------- | ---------- | --------- | ----------- | -------- | ----- | ----- |
| Leo Breiman. | Random forests.  | Machine    | learning, | 45(1):5–32, |          | 2001. |       |
30

Jane Bromley, Isabelle Guyon, Yann LeCun, Eduard S¨ackinger, and Roopak Shah. Signature verifi-
cation using a “siamese” time delay neural network. In Advances in Neural Information Processing
| Systems, | volume 6, pp. | 737–744, 1993. |     |     |     |
| -------- | ------------- | -------------- | --- | --- | --- |
Hans Buehler, Lukas Gonon, Josef Teichmann, and Ben Wood. Deep hedging. Quantitative Finance,
| 19(8):1271–1291, | 2019. |     |     |     |     |
| ---------------- | ----- | --- | --- | --- | --- |
Fan Cai, Nhien-An Le-Khac, and Tahar Kechadi. Clustering approaches for financial data analysis: a
| survey. | arXiv preprint | arXiv:1609.08520, | 2016. |     |     |
| ------- | -------------- | ----------------- | ----- | --- | --- |
MaximoCamacho,GabrielPerez-Quiros,andPilarPoncela. Markov-switchingdynamicfactormodels
| in real | time. International | Journal of | Forecasting, | 34(4):598–611, | 2018. |
| ------- | ------------------- | ---------- | ------------ | -------------- | ----- |
Lele Cao, Vilhelm von Ehrenheim, Mark Granroth-Wilding, Richard Anselmo Stahl, Andrew McCor-
nack,ArminCatovic,andDhianaDevaCavalcantiRocha. Companykg: Alarge-scaleheterogeneous
graph for company similarity quantification. In Proceedings of the 30th ACM SIGKDD Conference
| on Knowledge | Discovery | and Data Mining, | pp. | 4816–4827, | 2024. |
| ------------ | --------- | ---------------- | --- | ---------- | ----- |
N.M.Castellanos,S.Frank,D.Desai,S.Pasquali,andD.Mehta. Cananunsupervisedclusteringalgo-
rithm reproduce a categorization system? In Proceedings of the 5th ACM International Conference
| on AI in | Finance, pp. | 213–221. ACM, | 2024. |     |     |
| -------- | ------------ | ------------- | ----- | --- | --- |
Abhijit Chakraborty, Soumya Easwaran, and Sitabhra Sinha. Uncovering the hierarchical structure
of the international forex market by using similarity metric between the fluctuation distributions of
| currencies. | arXiv preprint | arXiv:2005.02482, | 2020. |     |     |
| ----------- | -------------- | ----------------- | ----- | --- | --- |
James Ming Chen, Mobeen Ur Rehman, and Xuan Vinh Vo. Clustering commodity markets in space
andtime: Clarifyingreturns,volatility,andtradingregimesthroughunsupervisedmachinelearning.
| Resources | Policy, 73:102162, | 2021. |     |     |     |
| --------- | ------------------ | ----- | --- | --- | --- |
Jun Chen and Yongheng Deng. Commercial mortgage workout strategy and conditional default prob-
ability: Evidence from special serviced cmbs loans. The Journal of Real Estate Finance and Eco-
| nomics, | 46(4):609–632, | 2013. |     |     |     |
| ------- | -------------- | ----- | --- | --- | --- |
Ting Chen, Simon Kornblith, Mohammad Norouzi, and Geoffrey Hinton. A simple framework for
contrastive learning of visual representations. In International Conference on Machine Learning,
| pp. 1597–1607. | PMLR, | 2020. |     |     |     |
| -------------- | ----- | ----- | --- | --- | --- |
Alex Coad. The Growth of Firms: A Survey of Theories and Empirical Evidence. Edward Elgar
| Publishing, | 2009. |     |     |     |     |
| ----------- | ----- | --- | --- | --- | --- |
31

Gonzalo Cortazar and Lorenzo Naranjo. An n-factor gaussian model of oil futures prices. Journal of
futures markets: futures, options, and other derivative products, 26(3):243–268, 2006.
Roy Endr´e Dahl, Atle Oglend, and Muhammad Yahya. Dynamics of volatility spillover in commodity
markets: Linking crude oil to agriculture. Journal of Commodity Markets, 20:100111, 2020.
Sarkar Snigdha Sarathi Das, Mohammed Eunus Ali, Yuan-Fang Li, Yong-Bin Kang, and Timos Sellis.
Boostinghousepricepredictionsusinggeo-spatialnetworkembedding. Data Mining and Knowledge
Discovery, 35(6):2221–2250, 2021.
Thomas J De Luca and Dhagash Mehta. Esg fund usage among individual investor households: A
machine learning–based behavioral study. Journal of Impact & ESG Investing, 3(3), 2023.
Fr´ed´eric Delmar, Per Davidsson, and William B Gartner. Arriving at the high-growth firm. Journal
of Business Venturing, 18(2):189–216, 2003.
VictorDeMiguel,JavierGil-Bazo,FranciscoJ.Nogales,andAndr´eA.P.Santos. Machinelearningand
fundcharacteristicshelptoselectmutualfundswithpositivealpha. JournalofFinancialEconomics,
150(3):103737, 2023.
Emanuel Derman and Iraj Kani. The volatility smile and its implied tree. RISK, 7(2):139–145, 1994.
Dhruv Desai and Dhagash Mehta. On robustness of mutual funds categorization and distance metric
learning. The Journal of Financial Data Science, 3(4):130–150, 2021.
Dhruv Desai, Ashmita Dhiman, Tushar Sharma, Deepika Sharma, Dhagash Mehta, and Stefano
Pasquali. Quantifying outlierness of funds from their categories using supervised similarity. In
Proceedings of the 4th ACM International Conference on AI in Finance (ICAIF), pp. 655–663,
2023.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert: Pre-training of deep
bidirectional transformers for language understanding. NAACL-HLT, pp. 4171–4186, 2019.
Francis X Diebold and Kamil Yilmaz. Better to give than to receive: Predictive directional measure-
ment of volatility spillovers. International Journal of forecasting, 28(1):57–66, 2012.
RianDolphin,BarrySmyth,andRuihaiDong.Stockembeddings: Learningdistributedrepresentations
for financial assets. Engineering Proceedings, 39:30, 2023.
RianDolphin,BarrySmyth,andRuihaiDong. Contrastivelearningofassetembeddingsfromfinancial
timeseries. InProceedings of the 5th ACM International Conference on AI in Finance,pp.379–387,
2024.
32

JitkaDupaˇcov´a,NicoleGr¨owe-Kuska,andWernerR¨omisch. Scenarioreductioninstochasticprogram-
| ming. Mathematical |     | programming, |     | 95(3):493–511, |     | 2003. |     |     |
| ------------------ | --- | ------------ | --- | -------------- | --- | ----- | --- | --- |
Sergey Dzuba and Denis Krylov. Cluster analysis of financial strategies of companies. Mathematics, 9
| (24):3192, | 2021. |     |     |     |     |     |     |     |
| ---------- | ----- | --- | --- | --- | --- | --- | --- | --- |
Guy Stephane Waffo Dzuyo, Ga¨el Guibon, Christophe Cerisara, and Luis Belmar-Letelier. Linking
industrysectorsandfinancialstatements: Ahybridapproachforcompanyclassification. Proceedings
| of the AAAI | Conference |     | on Artificial |     | Intelligence, | 39(16):16444–16452, |     | 2025. |
| ----------- | ---------- | --- | ------------- | --- | ------------- | ------------------- | --- | ----- |
Frank J Fabozzi. Fixed income analysis, volume 6. John Wiley & Sons, 2007.
Robert W Faff, Terrance Hallahan, and Michael D McKenzie. An empirical investigation of personal
| financial | risk tolerance. | Financial |     | Services | Review, | 13(1):57–79, | 2004. |     |
| --------- | --------------- | --------- | --- | -------- | ------- | ------------ | ----- | --- |
Michael Farrell, Dermot Murphy, Marcus Painter, and Guangli Zhang. Disclosure complexity, regula-
tory burden, and the cost of capital. George J. Stigler Center for the Study of the Economy & the
| State Working | Paper, | (338), | 2023. |     |     |     |     |     |
| ------------- | ------ | ------ | ----- | --- | --- | --- | --- | --- |
GuanchaoFeng,DhruvDesai,StefanoPasquali,andDhagashMehta. Opensetrecognitionforrandom
| forest. pp. | 45–53, | 2024. |     |     |     |     |     |     |
| ----------- | ------ | ----- | --- | --- | --- | --- | --- | --- |
Daniel J. Fenn, Mason A. Porter, Peter J. Mucha, Mark McDonald, Stacy Williams, Neil F. Johnson,
andNickS.Jones. Dynamicalclusteringofexchangerates. Quantitative Finance,12(10):1493–1520,
2012.
LeonardoHSFernandes,JoseWLSilva,DerickDQuintino,AndreLPSantos,TiagoAEFerreira,and
Fernando HA de Araujo. Comparing the efficiency and similarity between wti, fiat currencies and
| foreign exchange |     | rates. Fluctuation |     | and | Noise | Letters, 22(04):2340003, |     | 2023. |
| ---------------- | --- | ------------------ | --- | --- | ----- | ------------------------ | --- | ----- |
Andrea Flori, Fabrizio Lillo, Fabio Pammolli, and Alessandro Spelta. Better to stay apart: asset
commonality,bipartitenetworkcentrality,andinvestmentstrategies.AnnalsofOperationsResearch,
| 299(1):177–213, |     | 2021. |     |     |     |     |     |     |
| --------------- | --- | ----- | --- | --- | --- | --- | --- | --- |
Andy Fodor, Randy D Jorgensen, and John D Stowe. Financial clusters, industry groups, and stock
| return correlations. |     | Journal | of  | Financial | Research, | 44(1):121–144, |     | 2021. |
| -------------------- | --- | ------- | --- | --------- | --------- | -------------- | --- | ----- |
Philip Hans Franses and Thomas Wiemann. Intertemporal similarity of economic time series: An
application of dynamic time warping. Computational Economics, 56(1):59–75, 2020.
XavierGabaix,RalphSJKoijen,RobertRichmond,andMotohiroYogo. Assetembeddings. Available
| at SSRN | 4507511, | 2024. |     |     |     |     |     |     |
| ------- | -------- | ----- | --- | --- | --- | --- | --- | --- |
33

Paul Geertsema and Helen Lu. Relative valuation with machine learning. Journal of Accounting
| Research, | 61(1):329–376, |     | 2023. |     |     |     |     |
| --------- | -------------- | --- | ----- | --- | --- | --- | --- |
Christopher Gerling. Company2vec—german company embeddings based on corporate websites. In-
ternational Journal of Information Technology & Decision Making, 23(06):2209–2243, 2024.
Jesse S. Ghashti and John R. J. Thompson. The complexity of financial wellness: Examining survey
patterns via kernel metric learning and clustering of mixed-type data. In Proceedings of the Fourth
ACM International Conference on AI in Finance (ICAIF ’23), pp. 314–322. ACM, 2023.
JesseS.GhashtiandJohnR.J.Thompson. Mixed-typedistanceshrinkageandselectionforclustering
| via kernel | metric | learning. | Journal | of Classification, | 42:311–334, |     | 2025a. |
| ---------- | ------ | --------- | ------- | ------------------ | ----------- | --- | ------ |
Jesse S. Ghashti and John R. J. Thompson. Mixed-type kernel-based quantification of similarity for
| clustering. | Advances | in  | Data Analysis | and | Classification, | pp. | 1–37, 2025b. |
| ----------- | -------- | --- | ------------- | --- | --------------- | --- | ------------ |
Paul Glasserman, Chulmin Kang, and Wanmo Kang. Stress scenario selection by empirical likelihood.
| Quantitative | Finance, | 15(1):25–41, |     | 2015. |     |     |     |
| ------------ | -------- | ------------ | --- | ----- | --- | --- | --- |
William N Goetzmann and Susan M Wachter. Clustering methods for real estate portfolios. Real
| Estate Economics, |     | 23(3):271–310, |     | 1995. |     |     |     |
| ----------------- | --- | -------------- | --- | ----- | --- | --- | --- |
Gary B Gorton, Fumio Hayashi, and K Geert Rouwenhorst. The fundamentals of commodity futures
| returns. | Review of | Finance, | 17(1):35–105, |     | 2013. |     |     |
| -------- | --------- | -------- | ------------- | --- | ----- | --- | --- |
John C. Gower. A general coefficient of similarity and some of its properties. Biometrics, 27(4):
| 857–871, | 1971. |     |     |     |     |     |     |
| -------- | ----- | --- | --- | --- | --- | --- | --- |
John Grable, Abed Rabbani, and Wookjae Heo. The complementary nature of financial risk aversion
| and financial | risk | tolerance. | Risks, | 12(7):109, | 2024. |     |     |
| ------------- | ---- | ---------- | ------ | ---------- | ----- | --- | --- |
RichardC.Green,BurtonHollifield,andNormanSchu¨rhoff. Dealerintermediationandpricebehavior
in the aftermarket for new bond issues. The Journal of Financial Economics, 86(3):643–682, 2007.
Aditya Grover and Jure Leskovec. node2vec: Scalable feature learning for networks. In Proceedings of
the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pp.
| 855–864, | 2016. |     |     |     |     |     |     |
| -------- | ----- | --- | --- | --- | --- | --- | --- |
David A. Guenther and Andrew J. Rosman. Differences between compustat and crsp sic codes and
related effects on research. Journal of Accounting and Economics, 18(1):115–128, 1994.
34

Jonas Gustafsson and Conrad Jonsson. Scenario generation for stress testing using generative ad-
versarial networks: Deep learning approach to generate extreme but plausible scenarios. Master’s
| thesis, Ume˚a | University, | 2023. |     |     |
| ------------- | ----------- | ----- | --- | --- |
Joseph Gyourko and Donald B. Keim. What does the stock market tell us about real estate returns?
Journal of the American Real Estate and Urban Economics Association, 20(3):457–485, 1992.
James D Hamilton. A new approach to the economic analysis of nonstationary time series and the
business cycle. Econometrica: Journal of the econometric society, pp. 357–384, 1989.
Lawrence E. Harris and Michael S. Piwowar. Secondary trading costs in the municipal bond market.
| The Journal | of Finance, | 61(3):1361–1397, | 2006. |     |
| ----------- | ----------- | ---------------- | ----- | --- |
HolgerHeitschandWernerR¨omisch. Scenarioreductionalgorithmsinstochasticprogramming. Com-
| putational | optimization | and applications, | 24(2):187–206, | 2003. |
| ---------- | ------------ | ----------------- | -------------- | ----- |
Gerard Hoberg and Gordon Phillips. Product market synergies and competition in mergers and ac-
quisitions: A text-based analysis. Review of Financial Studies, 23(10):3773–3811, 2010.
Lawrence Hubert and Phipps Arabie. Comparing partitions. Journal of Classification, 2(1):193–218,
1985.
YoontaeHwang,JunhyeongLee,DahamKim,SeunghwanNoh,JoohwanHong,andYongjaeLee. Sim-
stock: Representation model for stock similarities. In Proceedings of the Fourth ACM International
| Conference | on AI in | Finance, pp. | 533–540. ACM, 2023a. |     |
| ---------- | -------- | ------------ | -------------------- | --- |
Yoontae Hwang, Yongjae Lee, and Frank J. Fabozzi. Identifying household finance heterogeneity via
| deep clustering. | Annals | of Operations | Research, 325(2):1255–1289, | 2023b. |
| ---------------- | ------ | ------------- | --------------------------- | ------ |
Yoontae Hwang, Junpyo Park, Jang Ho Kim, Yongjae Lee, and Frank J. Fabozzi. Heterogeneous
tradingbehaviorsofindividualinvestors: Adeepclusteringapproach. Finance Research Letters,65:
105481, 2024.
Hidetoshi Ito, Akane Murakami, Nixon Dutta, Yukari Shirota, and Basabi Chakraborty. Clustering of
etf data for portfolio selection during early period of corona virus outbreak. Gakushuin Economic
| Review, | 58(1), 2021. |     |     |     |
| ------- | ------------ | --- | --- | --- |
Tomoki Ito, Jose Camacho Collados, Hiroki Sakaji, and Steven Schockaert. Learning company em-
beddings from annual reports for fine-grained industry characterization. In Proceedings of The 2nd
Workshop on Financial Technology and Natural Language Processing (FinNLP), 2020.
35

AnilK.Jain,M.NarasimhaMurty,andPatrickJ.Flynn. Dataclustering: Areview. ACM Computing
| Surveys, | 31(3):264–323, | 1999. |     |     |
| -------- | -------------- | ----- | --- | --- |
Jerinsh Jeyapaulraj, Dhruv Desai, Peter Chu, Dhagash Mehta, Stefano Pasquali, and Philip Sommer.
Supervised similarity learning for corporate bonds using random forest proximities. In Proceedings
of the 3rd ACM International Conference on AI in Finance (ICAIF ’22), pp. 411–419. ACM, 2022.
Tomasz Kaczmarek and Krit Pukthuanthong. Visual embeddings for consumer brand and product
| similarity | in finance. | Journal of | Financial Data Science, | 2024. |
| ---------- | ----------- | ---------- | ----------------------- | ----- |
S¸ebnem Kalemli-O¨zcan, Bent E Sørensen, Carolina Villegas-Sanchez, Vadym Volosovych, and Sevcan
Ye¸silta¸s. How to construct nationally representative firm-level data from the orbis global database:
New facts on smes and aggregate implications for industry concentration. American Economic
| Journal: | Macroeconomics, | 16(2):353–374, | 2024. |     |
| -------- | --------------- | -------------- | ----- | --- |
Pan Kang and Stavros A Zenios. Complete prepayment models for mortgage-backed securities. Man-
| agement | Science, 38(11):1665–1685, |     | 1992. |     |
| ------- | -------------------------- | --- | ----- | --- |
Markku Kaustia and Ville Rantala. Common analysts: Method for defining peer firms. Journal of
| Financial | and Quantitative | Analysis, | 56(5):1505–1536, | 2021. |
| --------- | ---------------- | --------- | ---------------- | ----- |
Kyeongbin Kim, Yoontae Hwang, Dongcheol Lim, Suhyeon Kim, Junghye Lee, and Yongjae Lee.
Householdfinancialhealth: amachinelearningapproachfordata-drivendiagnosisandprescription.
| Quantitative | Finance, | 23(11):1565–1595, | 2023. |     |
| ------------ | -------- | ----------------- | ----- | --- |
Moon Kim, Ravi Shukla, and Michael Tomas. Mutual fund objective misclassification. Journal of
| Economics | and Business, | 52(4):309–323, | 2000. |     |
| --------- | ------------- | -------------- | ----- | --- |
Woo Chang Kim, Yongjae Lee, and Yoon Hak Lee. Cost of asset allocation in equity market: How
much do investors lose due to bad asset class design? The Journal of Portfolio Management, 41(1):
34–44, 2014.
Gang Kou, Yi Peng, and Guoxun Wang. Evaluation of clustering algorithms for financial risk analysis
| using mcdm | methods. | Information | Sciences, 275:1–12, | 2014. |
| ---------- | -------- | ----------- | ------------------- | ----- |
Marcel Kremer, Alexander P Becker, Irena Vodenska, H Eugene Stanley, and Rudi Sch¨afer. Economic
and political effects on currency clustering dynamics. Quantitative Finance, 19(5):705–716, 2019.
Brian Kulis. Metric learning: A survey. Foundations and Trends in Machine Learning, 5(4):287–364,
2013.
36

Jaroslaw Kwapien, Stanislaw Gworek, Stanislaw Drozdz, and Andrzej Gorski. Analysis of a network
structure of the foreign currency exchange market. Journal of Economic Interaction and Coordina-
| tion, 4:51–70, | 2009. |     |     |     |     |     |     |     |
| -------------- | ----- | --- | --- | --- | --- | --- | --- | --- |
Stephen Law, Brooks Paige, and Chris Russell. Take a look around: using street view and satellite
images to estimate house prices. ACM Transactions on Intelligent Systems and Technology (TIST),
| 10(5):1–19, | 2019. |     |     |     |     |     |     |     |
| ----------- | ----- | --- | --- | --- | --- | --- | --- | --- |
Hoyoung Lee, Wonbin Ahn, Suhwan Park, Jaehoon Lee, Minjae Kim, Sungdong Yoo, Taeyoon Lim,
Woohyung Lim, and Yongjae Lee. Theme: Enhancing thematic investing with semantic stock
representations and temporal dynamics. arXiv preprint arXiv:2508.16936, 2025.
Mingshu Li, Dhruv Desai, Jerinsh Jeyapaulraj, Philip Sommer, Riya Jain, Peter Chu, and Dhagash
Mehta. Strapsim: Aportfoliosimilaritymetricforetfalignmentandportfoliotrades. arXiv preprint
| arXiv:2509.24151, |     | 2025. |     |     |     |     |     |     |
| ----------------- | --- | ----- | --- | --- | --- | --- | --- | --- |
YuyongLi,ZhaoruiWang,andFanMeng. Bonddefaultpredictionwithtemporalgraphconvolutional
neural network and weakly supervised learning. Procedia Computer Science, 221:1376–1385, 2023.
David C. Ling and Andy Naranjo. Economic risk factors and commercial real estate returns. The
| Journal | of Real | Estate | Finance | and | Economics, | 14(3):283–307, |     | 1997. |
| ------- | ------- | ------ | ------- | --- | ---------- | -------------- | --- | ----- |
FrancescoLisiandEdoardoOtranto. Clusteringmutualfundsbyreturnandrisklevels. InProceedings
of the International Conference MAF 2008 – Mathematical and Statistical Methods for Actuarial
| Sciences | and Finance, |     | pp. 183–191. |     | Springer, | 2008. |     |     |
| -------- | ------------ | --- | ------------ | --- | --------- | ----- | --- | --- |
Robert Litterman. Common factors affecting bond returns. Journal of fixed income, pp. 54–61, 1991.
Marcos Lopez de Prado. Building diversified portfolios that outperform out of sample. The Journal
| of Portfolio | Management, |     | 42(4):59–69, |     | 2016. |     |     |     |
| ------------ | ----------- | --- | ------------ | --- | ----- | --- | --- | --- |
Brian M Lucey, Claire G Gilmore, and Marian Boscia. Comovements in commodity markets: A
| minimum | spanning | tree | analysis, | 2011. |     |     |     |     |
| ------- | -------- | ---- | --------- | ----- | --- | --- | --- | --- |
Yan-Ran Ma, Qiang Ji, Fei Wu, and Jiaofeng Pan. Financialization, idiosyncratic information and
| commodity | co-movements. |     | Energy | Economics, |     | 94:105083, | 2021. |     |
| --------- | ------------- | --- | ------ | ---------- | --- | ---------- | ----- | --- |
Christopher D. Manning, Prabhakar Raghavan, and Hinrich Schu¨tze. Introduction to Information
| Retrieval. | Cambridge |     | University | Press, | 2008. |     |     |     |
| ---------- | --------- | --- | ---------- | ------ | ----- | --- | --- | --- |
Achla Marathe and Hany A Shawky. Categorizing mutual funds using clusters. Advances in Quanti-
| tative analysis | of  | Finance | and | Accounting, |     | 7(1):199–204, | 1999. |     |
| --------------- | --- | ------- | --- | ----------- | --- | ------------- | ----- | --- |
37

Gautier Marti, Frank Nielsen, Mikol(cid:32)aj Bin´kowski, and Philippe Donnat. A review of two decades
of correlations, hierarchies, networks and clustering in financial markets. Progress in information
| geometry: | Theory | and applications, |     | pp. | 245–274, | 2021. |     |     |
| --------- | ------ | ----------------- | --- | --- | -------- | ----- | --- | --- |
In˜igo Mart´ın-Melero, Rau´l G´omez-Mart´ınez, Mar´ıa Luisa Medrano-Garc´ıa, and Felipe Hern´andez-
Perlines. Comparison of sectorial and financial data for esg scoring of mutual funds with machine
| learning. | Financial | Innovation, |     | 11:84, | 2025. |     |     |     |
| --------- | --------- | ----------- | --- | ------ | ----- | --- | --- | --- |
Dhagash Mehta, Dhruv Desai, and Jithin Pradeep. Machine learning fund categorizations. In Pro-
ceedings of the First ACM International Conference on AI in Finance, pp. 1–8. ACM, 2020.
Giovanna Menardi and Francesco Lisi. Double clustering for rating mutual funds. Electronic Journal
| of Applied | Statistical | Analysis, | 8(1):44–56, |     | 2015. |     |     |     |
| ---------- | ----------- | --------- | ----------- | --- | ----- | --- | --- | --- |
Takayuki Mizuno, Hideki Takayasu, and Misako Takayasu. Correlation networks among currencies.
| Physica | A: Statistical | Mechanics |     | and its | Applications, |     | 364:336–342, | 2006. |
| ------- | -------------- | --------- | --- | ------- | ------------- | --- | ------------ | ----- |
Marco Molinari, Victor Shao, Luca Imeneo, Mateusz Mikolajczak, Vladimir Tregubiak, Abhimanyu
Pandey, and Sebastian Kuznetsov Ryder Torres Pereira. Interpretable company similarity with
| sparse autoencoders, |     | 2024. |     |     |     |     |     |     |
| -------------------- | --- | ----- | --- | --- | --- | --- | --- | --- |
David Moreno, Paulina Marco, and Ignacio Olmeda. Self-organizing maps could improve the clas-
sification of spanish mutual funds. European Journal of Operational Research, 174(2):1039–1054,
2006.
Thierry Moudiki and Fr´ed´eric Planchet. Economic scenario generators. Springer, 2016.
AliNourianiandLanceLemke.Vision-basedhousingpriceestimationusinginterior,exterior&satellite
| images. | Intelligent | Systems | with | Applications, |     | 14:200081, | 2022. |     |
| ------- | ----------- | ------- | ---- | ------------- | --- | ---------- | ----- | --- |
Ruolan Ouyang, Chengkai Zhuang, Tingting Wang, and Xuan Zhang. Network analysis of risk trans-
mission among energy futures: An industrial chain perspective. Energy Economics, 107:105798,
2022.
CynthiaPagliaro, DhagashMehta, Han-TaiShiao, ShaofeiWang, andLuweiXiong. Investorbehavior
modelingbyanalyzingfinancialadvisornotes: amachinelearningperspective. InProceedings of the
| Second | ACM International |     | Conference |     | on AI | in Finance, | pp. 1–8, | 2021. |
| ------ | ----------------- | --- | ---------- | --- | ----- | ----------- | -------- | ----- |
Maksim Papenkov. Multi-industry simplex 2.0: Temporally-evolving probabilistic industry classifica-
tion, 2024.
38

MaksimPapenkov,ChrisMeredith,ClaireNoel,JaiPadalkar,TempleHendrickson,DanielNitiutomo,
and Thomas Farrell. Multi-industry simplex: A probabilistic extension of gics, 2023.
Sharathchandra Patil, S Mahalakshmi, NR Vikas, VN Srajan, and M Srinandan. Llm-driven peer
competitor and stock analysis. In 2025 International Conference on Computing for Sustainability
| and Intelligent | Future | (COMP-SIF), | pp. | 1–6. IEEE, 2025. |
| --------------- | ------ | ----------- | --- | ---------------- |
Francesco Pattarin, Sandra Paterlini, and Tommaso Minerva. Clustering financial time series: an
application to mutual funds style analysis. Computational Statistics & Data Analysis, 47(2):353–
372, 2004.
BryanPerozzi,RamiAl-Rfou,andStevenSkiena. Deepwalk: Onlinelearningofsocialrepresentations.
In Proceedings of the 20th ACM SIGKDD International Conference on Knowledge Discovery and
| Data Mining, | pp. 701–710, | 2014. |     |     |
| ------------ | ------------ | ----- | --- | --- |
Nathan Phelps and Adam Metzler. An exploratory clustering analysis of the 2016 national financial
| well-being | survey. PloS | One, 19(9):e0309260, |     | 2024. |
| ---------- | ------------ | -------------------- | --- | ----- |
RobertSPindyckandJulioJRotemberg.Theexcessco-movementofcommodityprices.TheEconomic
| Journal, | 100(403):1173–1189, | 1990. |     |     |
| -------- | ------------------- | ----- | --- | --- |
Gloria Polinesi and Maria Cristina Recchioni. Filtered clustering for exchange traded fund. Rivista
Italiana di Economia Demografia e Statistica, LXXV(1), 2021. Applies random-matrix filtering and
| hierarchical | clustering | to ETF return | correlations. |     |
| ------------ | ---------- | ------------- | ------------- | --- |
Omid Poursaeed, Tomas Matera, and Serge Belongie. Vision-based real estate price estimation. arXiv
preprint arXiv:1707.05489, 2017. URL https://arxiv.org/abs/1707.05489.
ThomasRaffinot.Hierarchicalclustering-basedassetallocation.TheJournalofPortfolioManagement,
| 43(1):9–24, | 2017. |     |     |     |
| ----------- | ----- | --- | --- | --- |
Tasneem Raihan. Predicting us recessions: A dynamic time warping exercise in economics. Available
| at SSRN | 3047649, 2017. |     |     |     |
| ------- | -------------- | --- | --- | --- |
Maryan Rizinski, Andrej Jankov, Vignesh Sankaradas, Eugene Pinsky, Igor Mishkovski, and Dimitar
Trajanov. Comparativeanalysisofnlp-basedmodelsforcompanyclassification. Information, 15(2):
77, 2024.
Joshua Rosaler, Dhruv Desai, Bhaskarjit Sarmah, Dimitrios Vamvourellis, Deran Onay, Stefano
Pasquali, and Dhagash Mehta. Enhanced local explainability and trust scores with random for-
est proximities. In Proceedings of the 5th ACM International Conference on AI in Finance, pp.
| 521–529, | 2024. |     |     |     |
| -------- | ----- | --- | --- | --- |
39

Joshua Rosaler, Luca Candelori, Vahagn Kirakosyan, Kharen Musaelian, Ryan Samson, Martin T.
Wells, Dhagash Mehta, and Stefano Pasquali. Supervised similarity for high-yield corporate bonds
with quantum cognition machine learning. arXiv preprint arXiv:2502.01495, 2025. URL https:
//arxiv.org/abs/2502.01495.
Preetha Saha, Jasmine Lyu, Dhruv Desai, Rishab Chauhan, Jerinsh Jeyapaulraj, Peter Chu, Philip
Sommer, and Dhagash Mehta. Machine learning-based relative valuation of municipal bonds. In
Proceedings of the 5th ACM International Conference on AI in Finance, pp. 634–642, 2024.
Bhaskarjit Sarmah, Nayana Nair, Riya Jain, Dhagash Mehta, and Stefano Pasquali. Learning em-
bedded representation of the stock correlation matrix using graph machine learning. In 2024 IEEE
Symposium on Computational Intelligence for Financial Engineering and Economics (CIFEr), pp.
1–9. IEEE, 2024.
Vipul Satone, Dhruv Desai, and Dhagash Mehta. Fund2vec: Mutual funds similarity using graph
learning. In Proceedings of the Second ACM International Conference on AI in Finance, pp. 1–8.
ACM, 2021.
Ivan Savin, Kristina Chukavina, and Andrey Pushkarev. Topic-based classification and identification
of global trends for startup companies. Small Business Economics, 60(2):659–689, 2023.
E.I. Scarlat, Cristina Stan, and C.P. Cristescu. Self-similar characteristics of the currency exchange
rate in an economy in transition. Physica A: Statistical Mechanics and its Applications, 379(1):
188–198, 2007. ISSN 0378-4371.
FlorianSchroff,DmitryKalenichenko,andJamesPhilbin.Facenet: Aunifiedembeddingforfacerecog-
nition and clustering. In IEEE Conference on Computer Vision and Pattern Recognition (CVPR),
pp. 815–823, 2015.
William F. Sharpe. Asset allocation: Management style and performance measurement. The Journal
of Portfolio Management, 18(2):7–19, 1992.
Han-Tai Shiao, Cynthia Pagliaro, and Dhagash Mehta. Using machine learning to model advised-
investor behavior. Journal of Financial Data Science, 4(4), 2022.
B. Joseph Sopranzetti and Vinay Datar. Price clustering in foreign exchange spot markets. Journal
of Financial Markets, 5(4):411–417, 2002.
J´anos Szender´ak. Correlation clustering: Analysis of major agricultural commodity markets. Interna-
tional Journal of Engineering and Management Sciences, 3(3):288–302, 2018.
40

FuTanandDhagashMehta. Healthstateriskcategorization: Amachinelearningclusteringapproach
using health and retirement study data. Journal of Financial Data Science, 4(2), 2022.
John R. J. Thompson and Matt Davison. Functional mixed-type clustering of investors’ daily returns
during a market shock change-point and recovery. In Proceedings of the 5th ACM International
Conference on AI in Finance (ICAIF ’24), pp. 186–194. ACM, 2024.
John R. J. Thompson, Longlong Feng, R. Mark Reesor, and Chuck Grace. Know your clients’ be-
haviours: A cluster analysis of financial transactions. Journal of Risk and Financial Management,
14(2):50, 2021.
John R. J. Thompson, Longlong Feng, R. Mark Reesor, Chuck Grace, and Adam Metzler. Measuring
the gap between elicited and revealed risk for investors: An empirical study. Financial Planning
Review, 5(3):e1151, 2022.
Dimitrios Vamvourellis, M´at´e T´oth, Dhruv Desai, Dhagash Mehta, and Stefano Pasquali. Learning
mutual fund categorization using natural language processing. In Proceedings of the Third ACM
International Conference on AI in Finance, pp. 87–95. ACM, 2022.
Dimitrios Vamvourellis, M´at´e T´oth, Snigdha Bhagat, Dhruv Desai, Dhagash Mehta, and Stefano
Pasquali. Company similarity using large language models. In 2024 IEEE Symposium on Compu-
tational Intelligence for Financial Engineering and Economics (CIFEr), pp. 1–9. IEEE, 2024.
HansvanderHeijden.Predictingindustrysectorsfromfinancialstatements: Anillustrationofmachine
learning in accounting research. The British Accounting Review, 54(5):101084, 2022.
Vanguard Research. Market and economic environments. Technical report, Vanguard, 2023. Avail-
able at: https://www.vanguardmexico.com/content/dam/intl/americas/documents/mexico/
en/market-and-economic-environments.pdf.
DarnitonVianaandLucianoBarbosa. Attention-basedspatialinterpolationforhousepriceprediction.
InProceedings of the 29th ACM SIGSPATIAL International Conference on Advances in Geographic
Information Systems, pp. 545–548. ACM, 2021.
Nadia Vozlyublennaia and Youchang Wu. Mutual funds apart from the crowd. Dera working paper,
U.S. Securities and Exchange Commission, Division of Economic and Risk Analysis, 2016. URL
https://www.sec.gov/files/dera_wp_vozlyublennaia_mutualfundsapart.pdf.
Guo-Jin Wang, Chi Xie, Feng Han, and Bo Sun. Similarity measure and topology evolution of foreign
exchange markets using dynamic time warping method: Evidence from minimal spanning tree.
Physica A: Statistical Mechanics and its Applications, 391(16):4136–4146, 2012.
41

BoyuWu. Similarcorporatebondsselectionbyclusteringalgorithmstoincreaseinvestmentefficiency.
Technical Report SSRN 4572112, SSRN, 2023. URL https://ssrn.com/abstract=4572112.
Qiong Wu, Christopher G Brinton, Zheng Zhang, Andrea Pizzoferrato, Zhenming Liu, and Mihai
Cucuringu. Equity2vec: End-to-end deep learning framework for cross-sectional asset pricing. In
Proceedings of the Second ACM International Conference on AI in Finance, pp. 1–9, 2021.
Xin-Ye Wu and Zhi-Gang Zheng. Hierarchical cluster-tendency analysis of the group structure in the
| foreign exchange | market. | Frontiers | of Physics, | 8(4):451–460, | 2013. |
| ---------------- | ------- | --------- | ----------- | ------------- | ----- |
Yuanjian Xu, Jianing Hao, Kunsheng Tang, Jingnan Chen, Anxian Liu, Peng Liu, and Guang Zhang.
Finripple: Aligning large language models with financial market for event ripple effect awareness.
| arXiv preprint | arXiv:2505.23826, |     | 2025. |     |     |
| -------------- | ----------------- | --- | ----- | --- | --- |
GregoryYampolsky, DhruvDesai, MingshuLi, StefanoPasquali, andDhagashMehta. Case-basedex-
plainabilityforrandomforest: Prototypes,critics,counter-factualsandsemi-factuals. arXivpreprint
| arXiv:2408.06679, | 2024. |     |     |     |     |
| ----------------- | ----- | --- | --- | --- | --- |
Yildiray Yildirim. Estimating default probabilities of cmbs loans with clustering and heavy censoring.
| The Journal | of Real Estate | Finance | and Economics, | 37(2):93–111, | 2008. |
| ----------- | -------------- | ------- | -------------- | ------------- | ----- |
Dan Zhou, Ajim Uddin, Xinyuan Tao, Zuofeng Shang, and Dantong Yu. Temporal bipartite graph
neural networks for bond prediction. In Proceedings of the Third ACM International Conference on
| AI in Finance, | pp. 308–316, | 2022. |     |     |     |
| -------------- | ------------ | ----- | --- | --- | --- |
Meng Zou and Quan You. Fgpa: An integrated framework for mutual fund grouping and group
persistence assessment. In Advances in Knowledge Discovery and Data Mining (PAKDD 2025),
volume 15870 of Lecture Notes in Computer Science, pp. 149–161, Singapore, 2025. Springer.
42

| Appendix | Online | Tables |     |     |     |     |     |     |     |
| -------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
Exhibit 6: Clustering and similarity applications in fixed income across asset classes and data modal-
ities
| Asset Class | Data Modality |     | Method  |     |     | Applications |     |           |     |
| ----------- | ------------- | --- | ------- | --- | --- | ------------ | --- | --------- | --- |
|             | Tabular       |     | K-means |     |     | Peer groups  | for | valuation |     |
Hierarchical
|     | (ratings,     | spreads, |                 |                  |     | Illiquid | bond substitutes |     |     |
| --- | ------------- | -------- | --------------- | ---------------- | --- | -------- | ---------------- | --- | --- |
|     |               |          | Random          | Forest Proximity |     |          |                  |     |     |
|     | fundamentals) |          |                 |                  |     | Relative | value screening  |     |     |
|     |               |          | Metric Learning |                  |     |          |                  |     |     |
Time series
|     |     |     | Correlation | Clustering |     | Volatility | regime | detection |     |
| --- | --- | --- | ----------- | ---------- | --- | ---------- | ------ | --------- | --- |
Corporate
|     | (returns, | spreads) | Dynamic | Time Warping |     | Monitoring | structural | breaks |     |
| --- | --------- | -------- | ------- | ------------ | --- | ---------- | ---------- | ------ | --- |
Bonds
|     |     |     | Rolling-Winodw | Clustering |     | Grouping | by market | behavior |     |
| --- | --- | --- | -------------- | ---------- | --- | -------- | --------- | -------- | --- |
Graphs Graph Embeddings (node2vec)Systemic risk & contagion analysis
(ownership, Graph Neural Networks Finding substitutes via investor overlap
issuer links)
|     | Tabular     |             | Mixed-type      | Distances | (Gower)   | Peer cohorts   | for          | surveillance |     |
| --- | ----------- | ----------- | --------------- | --------- | --------- | -------------- | ------------ | ------------ | --- |
|     | (covenants, |             | k-prototypes,   | GB        | Proximity | Price check    | set          | construction |     |
|     | ratings)    |             |                 |           |           | Credit quality | benchmarking |              |     |
|     | Text        |             |                 |           |           | Disclosure     | outlier      | detection    |     |
|     | (official   | statements, | Text Embeddings |           |           | ESG-relevant   | cohort       | analysis     |     |
Municipal
|     | filings) |     | + Clustering |     |     | Monitoring | communication |     | consistency |
| --- | -------- | --- | ------------ | --- | --- | ---------- | ------------- | --- | ----------- |
Bonds
Graphs
|     |            |              |           |            |     | Mapping     | regional | exposure |            |
| --- | ---------- | ------------ | --------- | ---------- | --- | ----------- | -------- | -------- | ---------- |
|     | (issuer    | hierarchies, | Community | Detection, |     |             |          |          |            |
|     |            |              |           |            |     | Monitoring  | systemic | fiscal   | risks      |
|     | geo-links) |              | Spectral  | Clustering |     |             |          |          |            |
|     |            |              |           |            |     | Identifying | clusters | for      | comparison |
Tabular
|     |             |           | Gaussian | Mixtures |     | Prepayment/default |     | risk | cohorts |
| --- | ----------- | --------- | -------- | -------- | --- | ------------------ | --- | ---- | ------- |
|     | (loan-level | features) |          |          |     |                    |     |      |         |
Securitized Deep Metric Learning Borrower credit segmentation
Credit
| (MBS/ABS) | Time series |     |     |     |     | Aligning | stress test | scenarios |     |
| --------- | ----------- | --- | --- | --- | --- | -------- | ----------- | --------- | --- |
DTW
|            | (delinquency | paths)     |                |           |     | Benchmarking | cohort    | performance  |              |
| ---------- | ------------ | ---------- | -------------- | --------- | --- | ------------ | --------- | ------------ | ------------ |
|            |              |            | Wasserstein    | Distances |     |              |           |              |              |
|            |              |            |                |           |     | Monitoring   | credit    | risk regimes |              |
|            | Images       | & Spatial  |                |           |     | Automated    | property  | comparables  |              |
| Housing /  |              |            | Siamese        | Networks  |     |              |           |              |              |
|            | (photos,     | satellite) |                |           |     | Collateral   | valuation | &            | underwriting |
| Collateral |              |            | CNN Embeddings |           |     |              |           |              |              |
|            |              |            |                |           |     | Regional     | stress    | testing      |              |
43

Exhibit 7: Clustering and similarity applications for mutual funds and ETFs across data modalities
| Data Modality         |            | Method             |                   | Applications    |                           |                 |
| --------------------- | ---------- | ------------------ | ----------------- | --------------- | ------------------------- | --------------- |
|                       |            | Correlation        | Clustering        |                 |                           |                 |
|                       |            |                    |                   | Detecting       | investment                | styles          |
| Time series           |            | K-shape            |                   |                 |                           |                 |
|                       |            |                    |                   | Monitoring      | style drift               |                 |
| (returns, volatility, | flows)     | DTW                |                   |                 |                           |                 |
|                       |            |                    |                   | Forming         | regime-aware              | peer groups     |
|                       |            | Contrastive        | Embeddings        | Checking        | category reproducibility  |                 |
|                       |            | Regime-switching   | Models            |                 |                           |                 |
|                       |            | Cosine/Jaccard     | Similarity        |                 |                           |                 |
|                       |            |                    |                   | Identifying     | peer groups               | by holdings     |
| Tabular               |            | K-means            |                   |                 |                           |                 |
|                       |            |                    |                   | Detecting       | crowding &                | overlap risk    |
| (holdings,            | fees, AUM) | Hierarchical       | Clustering        |                 |                           |                 |
|                       |            |                    |                   | Refining        | categories for            | due diligence   |
|                       |            | Gower/k-prototypes |                   | Surveillance    | based on                  | fund attributes |
|                       |            | Kernel             | Metric Learning   |                 |                           |                 |
|                       |            |                    |                   | Strategy        | & thematic classification |                 |
| Text                  |            | TF-IDF             |                   |                 |                           |                 |
|                       |            |                    |                   | ESG consistency | analysis                  |                 |
| (prospectuses,        | reports)   | Transformer        | Embeddings        |                 |                           |                 |
|                       |            |                    |                   | Verifying       | disclosure alignment      |                 |
|                       |            | Supervised         | Similarity Models |                 |                           |                 |
|                       |            |                    |                   | Narrative       | anomaly detection         |                 |
|                       |            |                    |                   | Mapping         | systemic exposures        |                 |
|                       |            | Community          | Detection         |                 |                           |                 |
| Graphs                |            |                    |                   | Finding         | clusters of overlapping   | strategies      |
Node Embeddings
| (fund–asset | networks) |            |                 | Peer retrieval | via network    | structure |
| ----------- | --------- | ---------- | --------------- | -------------- | -------------- | --------- |
|             |           | (DeepWalk, | node2vec)       |                |                |           |
|             |           | Graph      | Neural Networks |                |                |           |
|             |           |            |                 | Robust         | peer discovery |           |
Multimodal
|            |                  | Late/Early  | Fusion       |             |                   |                  |
| ---------- | ---------------- | ----------- | ------------ | ----------- | ----------------- | ---------------- |
|            |                  |             |              | Identifying | innovative/hybrid | strategies       |
| (returns + | holdings + text) | Cross-modal | Transformers |             |                   |                  |
|            |                  |             |              | Allocation  | support with      | multiple sources |
Joint Embeddings
Exhibit 8: Clustering and Similarity Applications for Companies by Data Modality
| Data Modality |     | Method |     | Applications |     |     |
| ------------- | --- | ------ | --- | ------------ | --- | --- |
K-means
| Tabular |     |     |     | Peer identification | for | valuation |
| ------- | --- | --- | --- | ------------------- | --- | --------- |
Hierarchical
|                |         |                 |                    | M&A target   | screening   |     |
| -------------- | ------- | --------------- | ------------------ | ------------ | ----------- | --- |
| (fundamentals, | ratios) |                 |                    |              |             |     |
|                |         | Metric Learning |                    | Benchmarking | competitors |     |
|                |         | Random          | Forest Proximities |              |             |     |
|                |         | Correlation     | Clustering         |              |             |     |
| Time series    |         |                 |                    | Thematic     | investing   |     |
DTW
| (returns, volatility) |     |     |     | Market | regime discovery |     |
| --------------------- | --- | --- | --- | ------ | ---------------- | --- |
Spectral Clustering
|     |     |     |     | Systemic | risk diagnostics |     |
| --- | --- | --- | --- | -------- | ---------------- | --- |
Sequence Encoders
| Text            |          | TF-IDF      | + Clustering | Thematic   | grouping of        | firms             |
| --------------- | -------- | ----------- | ------------ | ---------- | ------------------ | ----------------- |
|                 |          | Transformer | Embeddings   | Aligning   | strategy with      | disclosures       |
| (filings, news, | patents) |             |              |            |                    |                   |
|                 |          | LLM-based   | Similarity   | Mapping    | product/technology | overlaps          |
|                 |          | Community   | Detection    | Competitor | mapping            | via relationships |
Graphs
(supply chain, ownership) Node Embeddings (node2vec) Tracing systemic risk channels
|     |     | Graph Neural | Networks | Benchmarking | governance/ownership |     |
| --- | --- | ------------ | -------- | ------------ | -------------------- | --- |
Correlation matrices Graph Embeddings Peer discovery for portfolios
| (stock correlation | networks) |             |                       |                 |                      |     |
| ------------------ | --------- | ----------- | --------------------- | --------------- | -------------------- | --- |
|                    |           | GNNs        |                       | Diversification | analysis             |     |
|                    |           | Graph ML    | on Correlation Graphs | Systemic        | contagion monitoring |     |
|                    |           | Cross-modal | Embeddings            | Comprehensive   | peer discovery       |     |
Multimodal
|            |                | Multimodal           | Transformers | Mapping    | private to public | comps   |
| ---------- | -------------- | -------------------- | ------------ | ---------- | ----------------- | ------- |
| (tabular + | text + graphs) |                      |              |            |                   |         |
|            |                | Joint Representation | Learning     | Robustness | across data       | sources |
44

|         | Exhibit | 9:           | Clustering | and Similarity | Applications | for         | Private       | Companies |     |
| ------- | ------- | ------------ | ---------- | -------------- | ------------ | ----------- | ------------- | --------- | --- |
| Setting |         | Data         | Modality   |                | Applications |             |               |           |     |
|         |         | Tabular      |            |                | Benchmarking |             | profitability |           |     |
|         |         | (financials, | registry   | data)          | Forming      | credit      | risk cohorts  |           |     |
|         |         |              |            |                | Identifying  | high-growth |               | firms     |     |
|         |         |              |            |                | Startup      | ecosystem   | mapping       |           |     |
Text
|     |     |            |               |     | Competitor | identification |     |     |     |
| --- | --- | ---------- | ------------- | --- | ---------- | -------------- | --- | --- | --- |
|     |     | (websites, | descriptions) |     |            |                |     |     |     |
Private-to-Private
|     |     |              |                |         | Thematic            | grouping      | of          | SMEs        |                    |
| --- | --- | ------------ | -------------- | ------- | ------------------- | ------------- | ----------- | ----------- | ------------------ |
|     |     | Graphs       |                |         | Investor            | syndicate     | analysis    |             |                    |
|     |     | (investors,  | partnerships)  |         | Partnership         | discovery     |             |             |                    |
|     |     |              |                |         | Competitive         | landscape     |             | mapping     |                    |
|     |     |              |                |         | Product             | & brand       | comparables |             |                    |
|     |     | Images       | / Alternative  | Data    |                     |               |             |             |                    |
|     |     |              |                |         | Collateral          | & property    |             | valuation   |                    |
|     |     | (products,   | web            | traces) |                     |               |             |             |                    |
|     |     |              |                |         | Digital             | footprint     | analysis    |             |                    |
|     |     | Tabular      | + Fundamentals |         | Relative            | valuation     | vs.         | public      | peers              |
|     |     |              |                |         | Sector benchmarking |               |             |             |                    |
|     |     | (hybrid      | models)        |         |                     |               |             |             |                    |
|     |     |              |                |         | Building            | interpretable |             | comparables |                    |
|     |     | Text         | + Financials   |         | Aligning            | private       | firms       | with        | public disclosures |
|     |     | (multimodal) |                |         | Refining            | hybrid        | comparables |             |                    |
Private-to-Public
|     |     | Graphs     |            |                | Ecosystem      | mapping   |                   | with public | firms   |
| --- | --- | ---------- | ---------- | -------------- | -------------- | --------- | ----------------- | ----------- | ------- |
|     |     | (shared    | investors, | supply chains) | M&A target     | discovery |                   |             |         |
|     |     |            |            |                | Tracing        | systemic  | interdependencies |             |         |
|     |     | Time       | series     |                | Benchmarking   |           | volatility        | with        | proxies |
|     |     | (synthetic | proxies)   |                | Stress testing |           | & scenario        | analysis    |         |
Exhibit 10: Clustering and similarity applications for investors across data modalities
| Data Modality |     |     | Method |     |     | Simplified |              | Applications |                    |
| ------------- | --- | --- | ------ | --- | --- | ---------- | ------------ | ------------ | ------------------ |
|               |     |     |        |     |     | Client     | segmentation |              | for product design |
K-means
Tabular
|     |     |     |     |     |     | Suitability |     | checks |     |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ------ | --- |
Hierarchical
| (demographics, |     | portfolio) |       |          |     | Targeted |     | advisory | services |
| -------------- | --- | ---------- | ----- | -------- | --- | -------- | --- | -------- | -------- |
|                |     |            | Gower | Distance |     |          |     |          |          |
K-prototypes
|             |           |     | DTW         |            |     | Detecting  |     | herding   | behavior |
| ----------- | --------- | --- | ----------- | ---------- | --- | ---------- | --- | --------- | -------- |
| Transaction | Histories |     |             |            |     |            |     |           |          |
|             |           |     | Correlation | Clustering |     | Monitoring |     | liquidity | risk     |
(trades, flows)
|     |     |     | Contrastive | Embeddings |     | Tailoring |     | engagement | strategies |
| --- | --- | --- | ----------- | ---------- | --- | --------- | --- | ---------- | ---------- |
Risk & Behavioral Signals Latent Class Analysis Risk tolerance profiling
(questionnaires, sentiment) Mixture Models Suitability & compliance monitoring
|           |         |        | Supervised  | Similarity | Learning | Personalized |     | allocation   | strategies   |
| --------- | ------- | ------ | ----------- | ---------- | -------- | ------------ | --- | ------------ | ------------ |
| Text      |         |        | Topic       | Modeling,  |          | Thematic     |     | segmentation | (goals, ESG) |
|           |         |        |             |            |          | Advisor      |     | support      | tools        |
| (surveys, | advisor | notes) | Transformer | Embeddings |          |              |     |              |              |
Product recommendation
|     |     |     | Community | Detection |     | Detecting |     | peer influence |     |
| --- | --- | --- | --------- | --------- | --- | --------- | --- | -------------- | --- |
Graphs
(social, referral networks) Spectral Clustering Identifying contagion pathways
|     |     |     | GNNs |     |     | Mapping |     | behavioral | communities |
| --- | --- | --- | ---- | --- | --- | ------- | --- | ---------- | ----------- |
Multimodal
|             |         |         | Cross-modal | Embeddings   |     | Comprehensive |     |                 | client segmentation |
| ----------- | ------- | ------- | ----------- | ------------ | --- | ------------- | --- | --------------- | ------------------- |
| (portfolios | + flows | + text) |             |              |     |               |     |                 |                     |
|             |         |         | Multimodal  | Transformers |     | Robo-advisor  |     | personalization |                     |
|             |         |         |             |              |     | Stress-test   |     | propagation     | analysis            |
45

|             | Exhibit | 11: Clustering         | and Similarity Applications | in Other        | Asset Classes      |            |
| ----------- | ------- | ---------------------- | --------------------------- | --------------- | ------------------ | ---------- |
| Asset Class |         | Method / Modality      |                             | Simplified      | Applications       |            |
|             |         |                        |                             | Diversification | & hedging          | strategies |
|             |         | Time-series Clustering |                             |                 |                    |            |
| Commodities |         |                        |                             | Identifying     | contagion channels |            |
|             |         | (correlations,         | DTW, regimes)               |                 |                    |            |
|             |         |                        |                             | Analyzing       | co-movements       |            |
|             |         | Correlation-based      | Clustering                  | Identifying     | currency blocs     |            |
FX (Currencies)
|     |     |              |            | Designing           | carry trade baskets |           |
| --- | --- | ------------ | ---------- | ------------------- | ------------------- | --------- |
|     |     | Hierarchical | Clustering |                     |                     |           |
|     |     |              |            | Managing            | FX exposure         |           |
|     |     |              |            | Market surveillance | & anomaly           | detection |
Manifold Learning
| Derivatives |      |                    |            | Relative    | pricing of options   |            |
| ----------- | ---- | ------------------ | ---------- | ----------- | -------------------- | ---------- |
|             |      | Volatility Surface | Similarity |             |                      |            |
| (Options,   | CDS) |                    |            | Systemic    | risk & counterparty  | monitoring |
|             |      | Clustering CDS     | Spreads    |             |                      |            |
|             |      |                    |            | Identifying | stable coin families |            |
Network Clustering,
|                  |     |                         |                  | Monitoring | contagion channels      |                |
| ---------------- | --- | ----------------------- | ---------------- | ---------- | ----------------------- | -------------- |
| Cryptocurrencies |     | Time-series Correlation | Clustering,      |            |                         |                |
|                  |     |                         |                  | Assessing  | systemic risk in        | digital assets |
|                  |     | Transaction             | Graph Embeddings |            |                         |                |
|                  |     |                         |                  | Collateral | valuation & comparables |                |
Real Assets / Image & Spatial Embeddings, Geographic concentration analysis
Alternatives Feature-based Clustering Peer benchmarking & risk monitoring)
Exhibit 12: Summary of data modalities, methods, and applications for economic scenario clustering
and similarity
| Data Modality |     | Method  |                     | Applications |                |     |
| ------------- | --- | ------- | ------------------- | ------------ | -------------- | --- |
|               |     | Dynamic | Time Warping (DTW), | Macro regime | classification |     |
Paths
|     |     | Trajectory | Clustering, | Cross-country | cycle alignment |     |
| --- | --- | ---------- | ----------- | ------------- | --------------- | --- |
(macro trajectories)
|     |     | Correlation-based | Clustering | Early warning | systems for | recessions |
| --- | --- | ----------------- | ---------- | ------------- | ----------- | ---------- |
Scenario Trees Wasserstein / Nested Distance, Scenario reduction for ALM
(multistage Monte Carlo) Entropic Regularization Risk management optimization
|     |     |     |     | Preserving | key decision features |     |
| --- | --- | --- | --- | ---------- | --------------------- | --- |
Panels
|                  |             | Factor-based     | Clustering, | Probabilistic | regime identification |                    |
| ---------------- | ----------- | ---------------- | ----------- | ------------- | --------------------- | ------------------ |
| (mixed-frequency | indicators) |                  |             |               |                       |                    |
|                  |             | Regime-switching | Models      | Macroeconomic | forecasting           |                    |
|                  |             | (e.g., Markov    | Switching)  | Stress-test   | design                |                    |
|                  |             |                  |             | Aligning      | narratives with       | quantitative paths |
| Narratives       |             | Topic Modeling,  |             |               |                       |                    |
|                  |             |                  |             | Plausibility  | checks & governance   |                    |
|                  |             | Text Embeddings, |             |               |                       |                    |
| (supervisory     | texts)      |                  |             | Supervisory   | scenario analysis     |                    |
|                  |             | Bayesian         | Networks    |               |                       |                    |
|                  |             |                  |             | Systematic    | supervisory scenario  | design             |
Stress Scenarios Clustering of Severity Metrics, Plausibility benchmarking
(macro-financial variables) Empirical Likelihood Methods Ensuring diversity of adverse cases
|     |     |     |     | Generating | diverse & plausible | scenarios |
| --- | --- | --- | --- | ---------- | ------------------- | --------- |
Multimodal Cross-modal Embeddings, Aligning designs with historical data
|     |     | Multimodal | Transformers, |     |     |     |
| --- | --- | ---------- | ------------- | --- | --- | --- |
(quantitative + qualitative) Predicting systemic vulnerabilities
|     |     | GANs | for scenario generation |     |     |     |
| --- | --- | ---- | ----------------------- | --- | --- | --- |
46