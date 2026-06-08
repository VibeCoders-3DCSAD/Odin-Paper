International Journal of Computational Intelligence Systems          (2024) 17:310
https://doi.org/10.1007/s44196-024-00719-x

RESEARCH ARTICLE

Study of an Adaptive Financial Recommendation Algorithm Using Big
Data Analysis and User Interest Pattern with Fuzzy K‑Means Algorithm

Jinyong Yang1

Received: 14 August 2024 / Accepted: 2 December 2024
© The Author(s) 2024

Abstract
In an ever-changing financial market, big data is set to revolutionize user interest management by sparking innovation and
reshaping recommendations for the future. Conventional financial services face significant challenges like accessibility,
personalization, limited reachability, and incomplete information about user interest patterns. Thus, it results in suboptimal
financial recommendations that do not fully capture the individual user interests and adapt to changing market conditions.
Hence, the research developed an adaptive algorithm that uses fuzzy logic, neural networks, and big data to deliver accurate
financial recommendations based on user patterns using the Fuzzy Neural Financial Recommendation (FNFinRec) Algo-
rithm. Implemented on a Hadoop platform with a MapReduce framework, the FNFinRec ensures efficient processing of
large datasets. Fuzzy K-means clustering is applied, in which fuzzy logic helps to handle uncertainties in financial data and
clusters users with similar patterns. An adaptive user profile is developed based on real-time user data input. The Neutral
Collaborative Filtering (NCF) recommendation approach aims to predict user interests in financial products/services by learn-
ing from user interaction data. The neural networks provide personalized financial recommendations, adapting to changes
in user patterns over time for improved accuracy. The metrics such as silhouette coefficient, Davies–Bouldin Index, mean
square error (MSE), Precision@k, and Recall@k are used to assess the algorithm’s performance with existing algorithms.
The results show that the proposed FNFinRec algorithm outperforms existing methods regarding clustering quality and
recommendation accuracy. The competitive processing times that FNFinRec achieves are also crucial for making real-time
financial decisions.

Keywords  Financial recommendation · Big data analysis · Fuzzy K-means algorithm · User interest pattern

1  Introduction

The rise of big data has brought forward an evolutionary
change in the constantly evolving financial sector, requiring
a comprehensive understanding of market conditions and
user recommendations [1]. The user experience and opera-
tional effectiveness in financial services will be significant.
Incorporating big data to handle large-volume transaction
platforms with existing systems can create new business
opportunities [2]. One of the most successful recommenda-
tion systems uses collaborative filtering (CF), which pre-
dicts user interest by collecting data from former users with

 *  Jinyong Yang

jinyong_yang@hotmail.com

1  Economics and Trade Management Department,

Tianjin Sino-German University of Applied Sciences,
Tianjin 300350, China

identical perceptions [3]. The adoption of AI in extensive
data analysis emphasized the need for robust monitoring and
adaptation to the evolving changes in the financial sector
and technological landscape [4]. Machine learning and vast
amounts of data have accelerated the development of invest-
ment recommendation systems and demonstrated how these
innovations can improve users’ stock fund management and
financial literacy [5].

Big data analysis enables financial service providers to
provide personalized services by analyzing user interests
and spending patterns. However, several challenges must
be focused on to fully adapt the use of big data analysis and
ML in financial services [6]. Financial sectors share massive
amounts of data daily, with big data analysis impacting the
productivity of services [7]. User-friendly experience-based
financial services adopt AI techniques and big data analysis
to reshape user disparities and financial growth opportunities
[8]. Earlier K-means clustering algorithm poses challenges

Vol.:(0123456789)
  310

Page 2 of 14

International Journal of Computational Intelligence Systems          (2024) 17:310

with large-scale data and noise due to its preset user-related
values and sensitivity to initial centroids. It also discussed
improvement using mean shift technique to focus on big data
analysis [9]. With this clustering issue, the user groups are
clustered using adaptive learning-based improved k-means
clustering with an additional optimization algorithm for
cluster centres [10]. The study demonstrates its progressive
nature in the test of real financial data, reaching a clustering
accuracy of over 70% significant recommendation for sub-
sequent financial analysis and user data management [11].
Finance recommendation system identifies user interests’
patterns and supplements for decision making of a financial
stock trader but still needs improvement towards accurate-
ness of user pattern analysis [12]. However, the recom-
mendation algorithm that solely considers recommendation
diversity and accuracy is insufficient given the significance
of the growing amount of user activity data and individual
user interests [13].

With  the  use  of  real-time  relevant  feedback  and  user
activity data, the recommendation systems may automati-
cally create profiles that can identify users’ actual interests
and make recommendations about their preferred patterns
[14]. The study applies fuzzy k-means clustering for seg-
menting the users based on their interests in frequency, time
and location adaptability for achieving financial goals [15].
For obtaining more accurate results, user pattern in cluster-
ing formation is analyzed with the optimal cluster numbers
and initial values of its centers [16]. The study proposes an
automatic recommender system for investment types using
adaptive fuzzy k means algorithm with neural architecture
based on user feedback and improves decisions [17].

Novel contributions:

(1)  To process and analyze large volumes of financial data
and facilitate distinct user investment patterns, employs
MapReduce framework on Hadoop platform.

(2)  To handle uncertainty in user preferences by cluster-
ing users based on their interest pattern using fuzzy
k-means algorithm.

(3)  To analyze the user interest patterns thereby provid-
ing precise predictions and adaptive financial recom-
mendations using neural collaborative filtering (NCF)
approach.

Manuscript order: A summary of reviewed literature work
of existing recommendation techniques related to financial
data based on user interest is discussed in Sect. 2. Section 3
deliberates the data collection from financial sources. Sec-
tion 4 discusses Fuzzy Neural Financial Recommendation
(FNFinRec) Algorithm for adapting to the changing user
interest pattern. Section 5 delves deeper into the implemen-
tation of comparison analysis of clustering and big data
analysis, while Sect. 6 concludes the research work.

2   Overview of Existing Studies

2.1   Traditional Recommendation Algorithms

Luo [18] presented an optimized incremental clustering
approach assisted using kernels for providing investment
recommendation  for  financial  users.  The  experimental
dataset for the study is based on stock from the Shanghai
Stock Exchange. The results show that the suggested algo-
rithm helps stabilize markets and decreases risks associ-
ated with financial investments. However, the possibility
of scaling issues with bigger datasets and the requirement
for  additional  processing  to  account  for  ever-changing
market conditions are needed.

Asem et al. [19] applied users’ feedback, fuzzy logic,
and neural network inference to improve investment rec-
ommendations  in  the  adaptive  neural  fuzzy  inference
system (ANFIS) model. The study makes uses of demo-
graphic profile and financial types to give adaptive recom-
mendations by applying data-driven algorithms. A web-
based collection of potential investors’ demographic and
investment data is used by the program to process seven
main parameters. The JMP and MATLAB system groups
investors and makes customized investment suggestions.
The model’s dependence on precise initial gathering of
data  and  potential  scaling  concerns  with  larger,  more
diversified datasets are drawbacks.

Sengupta et al. [20] presented a portfolio recommender
system  (PRS)  for  financial  service  optimization  using
Markowitz’s Modern Portfolio Theory (MPT), a greedy
algorithm, and integer programming. For FY 2021–22,
the dataset includes NSE closing prices for the day and
transaction data for 297 Indian equities. K-means clus-
tering finds dissimilar equities and optimizes portfolios,
with greedy algorithm surpassing integer programming in
financial resource management. The model relies on past
data, which may not accurately predict market trends or
investor behavior.

2.2   Big Data Analysis and Its Applications

in Finance Based on User Interest Patterns

Li et al. [21] suggested smart investing platform evalu-
ation,  with  a  particular  emphasis  on  China  Merchants
Bank’s Financial Capricorn Intelligence, for their invest-
ment efficiency using the K-means clustering algorithm.
This  platform’s  investment  preferences  of  users  data
forms the basis of the dataset. According to the findings,
Capricorn  Intelligence’s  investing  approach  is  timing-
oriented, and its business shows signs of unpredictabil-
ity in choosing funds and a tendency to lower returns to

International Journal of Computational Intelligence Systems          (2024) 17:310

Page 3 of 14

  310

control risk. The study constraints include limited data
mining depth and possible algorithmic model discrepan-
cies that could lead to an inaccurate assessment of invest-
ment effectiveness.

Dandugala and Vani [22] The Improved Fuzzy C-Means
Multiview technique (IFCM) clustering technique uses the
MobileNet V2 model and a Three-Layered Stacked Bidirec-
tional LSTM (3L-BiLSTM) to speed up huge market data anal-
ysis. MapReduce is used to implement the method on Hadoop
to improve efficiency and reduce time complexities. Research
on three typical data sets showed greater performance in dif-
ferent parameters compared to previous techniques. The study
may be constrained by the computing capabilities needed for
large-scale processing of data and the assessment datasets,
which may not apply to other big data.

You [23] introduced a state-of-the-art models in marketing
changes with E-commerce recommendation method that sur-
passes the shortcomings of earlier systems by combining large
data analysis with fuzzy clustering gene analysis. Integrating
genetic fuzzy analysis to improve recommendation accuracy
is the main contribution. As a result of its well-configured
algorithm, the mean absolute error (MAE) is minimal. The
complexity of dealing with large-scale data and the necessity
for additional optimization in real-time processing, however,
limit its performance.

Chiou-Wei and Lee [24] applied a financial recommenda-
tion model called K-medoids clustering using Kullback–Lei-
bler-K-Medoids (K-L-KM) divergence for fund recommen-
dations, algorithm. User-item rating matrix was employed to
identify same funds based on their similarity measured using
an enhanced KL distance cluster. KL similarity is 0.85 accu-
rate on average and RMSE ranges from 0.93 to 0.94. Data
complexity can be reduced while important patterns are pre-
served using principal component analysis (PCA). Possible
sensitivity to clustering variables and limitations on dataset
size are its limitations.

Concerns with data quality, scalability, and flexibility in
real time are among the obstacles encountered by current
research on financial recommendation systems. It might be
difficult for traditional methods to deal with massive datasets
and adjust rapidly to changes in the market. To tackle these
issues, the FNFinRec technique uses a MapReduce framework
on Hadoop for scalable processing, fuzzy K-means clustering
for data uncertainty management, and neural collaborative
filtering for real-time accuracy and adaptability. By boosting
suggestion accuracy and system efficiency, this integrated
strategy improves efficiency in dynamic financial environ-
ments, overcoming limits of conventional methods.

3   Research Analysis

Research  in  financial  management  and  clustering  has
recently made great strides, with an emphasis on improv-
ing clustering performance and quantifying financial data
indicators. The current research aims to provide intelligent
financial recommendation model based on user interest
pattern. Fuzzy K-means clustering can accurately aggre-
gate vast volumes of user profile into clusters depending
on financial investment preferences and behaviors depicted
in Fig. (a and b). NCF may then exploit these clusters to
deliver adaptive recommendations, despite the setting of
massive financial data sets. The utilization of algorithms
that use deep learning such as NCF and the integration
of different features show that the data can manage the
complicated and varied nature of big data analysis. A dis-
tinct form of data sources from various big data analysis
is validated using silhouette coefficient.

Table 1 indicates key user attributes for the financial
recommendation system are summarized from the source
[25]. Gender breakdown, age range, investment charac-
teristics, and projected returns are all part of it. The table
gives a thorough picture of user profiles and habits by
including graphical representations of investment length
and monitoring frequency.

3.1   Data Preprocessing and Feature Selection

The initial data inspection selects the relevant features that
influences the financial decisions and user interest pat-
terns. The set of users can be represented in the form of
mathematical evaluation given in Eq. (1).
U = {ur1, ur2, .., urm}

(1)

Followed by defining the set of items called financial

products/services offered to the users can be defined as:

I = {i1, i2, .., in}

The interaction matrix R is defined using Eq. (3).

Rm×n =

r11 ⋯ r1n
⋮ ⋱ ⋮
rm1 ⋯ rmn ⎤
⎥
⎥
⎦

⎡
⎢
⎢
⎣

ruri indicates the interaction between user ur and item i . For
analyzing the user interest pattern, the financial risk score
Ψ is calculated based on the investment preferences Pi and
expected returns Ei , a simple weighted sum can be used.
The other attribute investment diversity namely an invest-
ment diversity score D can be calculated using the entropy

(2)

(3)

  310

Page 4 of 14

International Journal of Computational Intelligence Systems          (2024) 17:310

Table 1   Financial profile overview

Attributes

Gender distribution
Age category
Features used

Investment duration

Distributions

Female 43.1%, Male 56.1%
21–35
Mutual funds, equity market, debentures, government

bonds, fixed deposits, PPF, gold

Investment monitoring frequency

Fig (a) Investment duration analysis

Expected return

Fig (b) Investment monitoring frequency analysis
10–20%, 20–30%, 30–40%

of the distribution of preferences across different investment
avenues analyzed in Eq. (4).

n

D = −

pilog(pi)

i=1
∑

(4)

where  pi is the proportion of investment in the ith
 option
that may include stocks, bonds, real estate, mutual funds,
and gold. A more diverse investment, with a greater entropy
value, is crucial for adaptive financial recommendations that
aim to balance risk and return based on user expectations
and observed patterns. Feature selection involves the process
of identifying the importance of evaluated features using
random forest concept where the importance of feature  j in
a random forest can be calculated using Eq. (5)

Ij =

1
T

I(t)
j

T

t=1
∑

(5)

where I(t)
j  is the importance of feature  j in tree t , and T is the
total number of trees in the forest. This step helps in identify
the most influential factors in predicting user investment
preferences. The suggested FNFinRec algorithm’s whole
process flow is illustrated in this Fig. 1. Starting with the
intake of data and progressing via preprocessing, grouping,
and NCF, it culminates in the output of recommendations.

3.2   Big Data Analysis

Processing and analyzing massive amounts of financial data
are much improved when the MapReduce framework is used
on  the  Hadoop  platform.  Distributing  processing  duties
across numerous machines provides scalable data handling
with MapReduce. The analysis is essential for managing
massive datasets. The framework’s “Map” and “Reduce”
stages divide data processing, enabling parallel computa-
tion and result aggregation to speed up the recommendation
system and clustering model training in a qualified manner.

International Journal of Computational Intelligence Systems          (2024) 17:310

Page 5 of 14

  310

Fig. 1   Overall working flow of fuzzy neural financial recommendation (FNFinRec) algorithm

Hadoop guarantees quick data processing by effectively
managing resources and organizing activities. The research
analysis is crucial for real-time updates and synthesizing
feedback from users. Because it is more adept at dealing
with complicated data, this method makes data preprocess-
ing more efficient and makes financial recommendations
more accurate.

3.3   Fuzzy K‑Means Clustering

Fuzzy K-Means is helpful as it organizes financial resources
according to factors like risk levels and expected returns,
allowing it to identify patterns in the relationship between
the two. The users with conservative tolerance for risk can
be suggested low-risk, stable-return investments that work
based on personalized financial plans that match user pref-
erences. Applying fuzzy logic to handle uncertainty in user
preferences and data, providing adaptable recommendations
by clustering users with similar financial patterns. The fuzzy
k-means clustering minimizes Within-cluster variance with
the following objective function

Jm =

K

m

k=1
�

i=1
�

ur

m
ik ∙

xk − ck

2

(6)

In Eq. (6), the variable m indicates the fuzziness param-
eter typically m > 1 , urik is the degree of membership of

‖

‖

the datapoint xi to cluster k and ck indicates the centroid of
cluster k

Step  1:  define  appropriate  membership  functions  for

fuzzy sets based on user attributes.

Due to the subjective character of users’ ur financial deci-
sions, membership values will show the extent to which
each user is an integral component of specific clusters. The
degree to which clusters overlap is controlled by the fuzzi-
ness parameter m . There is more overlap when m is larger,
which means that users can be members of more than one
cluster. Each data point xi represents an individual user’s
financial profile. This profile could include features like
age, gender, preferences for various investment avenues that
involve mutual funds, equity market, debentures, and other
factors such as investment objectives, expected returns, and
investment duration. The membership value uij indicates how
much the ith
 data point called the user profile belongs to the
jth

 cluster it is calculated using an Eq. (7).

urij =

1

xi−cj
xi−ck

2
m−1

K
k=1

(7)

∑

� ‖
‖

‖
�
xi − cj
‖

The parameter

 indicates the Euclidean distance
between the data point xi and the centroid cj of cluster  j with
considered features like investment preferences. From this, the
hypothesis may provide if user i heavily invests in mutual
funds and centroid j represents a high-risk investment cluster,

‖

‖

  310

Page 6 of 14

International Journal of Computational Intelligence Systems          (2024) 17:310

xi−cj
xi−ck

the distance might be large, reflecting that the user is far from

‖

� ‖
‖

 compares
the profile typical of that cluster. The ratio
the distance of the datapoint xi to the centroid of cluster j with
�
its distance to the centroid of another cluster k . The considered
hypothesis is if user i is closer to the centroid of a low-risk
cluster cj compared to a high-risk cluster ck , this ratio will be
smaller, indicating a higher membership value for the low-risk
m−1 where m > 1 , which con-
cluster. The exponent parameter
trols the degree of fuzziness, is used to adjust the influence of
the  distance  ratio  based  on  the  m .  The  method  takes

‖

2

Fig. 2   Flowchart of fuzzy k-means clustering algorithm

Fig. 3   Cluster centroid update

uncertainty with  m > 1 into consideration and permits users
to have varied degrees of membership in multiple clusters,
mirroring the complexity of financial actions in the real world.
The sum in the denominator ensures that the membership val-
ues across all clusters for a given data point sum to 1, reflecting
the probability-like interpretation of these values.
Step 2: initialize cluster centroids randomly.
Initialization  of  centroids  starts  with  the  random  or
informed representing investment profiles with a different
focus on users preferring mutual funds and other favorites on
the equity market. Adjusting the clustering to represent user
financial preferences for various financial services is the goal
of the clustering criterion. For instance, if a user has a strong
preference for equities investments, their interests may be
grouped. However, some overlap may exist if they demonstrate
interest in other investment types. More effective convergence
and meaningful clusters can result from initial centroids influ-
enced by known user preferences.

Step 3: calculate the fuzzy membership of each data point
to all clusters, and the Fuzzy K-means clustering technique is
broken down into its parts in this flowchart in Fig. 2.

Step  4:  update  cluster  centroids  based  on  fuzzy

memberships.

The centroid cj of cluster, j is updated based on each user’s
investment pattern with a degree of membership to different
clusters. The membership value urij indicates how strongly a
user i belongs to cluster  j using this Eq. (8) to reflect their
investment behavior.

cj =

n
i=1ur
n
i=1ur

m
ij xi
m
ij

∑

∑

(8)

International Journal of Computational Intelligence Systems          (2024) 17:310

Page 7 of 14

  310

where urij in Eq. (8), is the membership value of the data
point xi to cluster  j , m as a fuzzy parameter determines how
clusters overlap and how membership values are calculated
and n as number of data points is shown in Fig. 3.

Step 5: repeat steps 3 and 4 until convergence that indicates
a change in centroids between iterations is minimal and below
a threshold.

Δcj =

c(new)
j

− c(old)
j

(9)

where Δcj in Eq. (9) should be below the predefined thresh-
old to indicate convergence.

‖

‖

Step 6: analyze resulting clusters to identify distinct user
groups based on financial interest. The time complexity of
fuzzy k-means is generally O(T × K × n × d) where T indi-
cates the number of iterations, K represents the number of
clusters, n as the number of data points, and d is the dimen-
sionality of the data. The cluster quality is analyzed using sil-
houette score and David Bouldin Index (DBI) to measure the
average similarity ratio of each cluster with its most similar
cluster. The FNFinRec algorithm generates synthetic data,
applies fuzzy K-means clustering, and calculates the silhouette
score to evaluate clustering outcomes, essential for segmenting
customers by financial preferences.

DBI =

1
k

K

i=1
∑

max
⏟⏟⏟
j≠i

d

(

Si + Sj
centi + centj

Si =

1
Ci

d

x, centi

x∈Ci
∑

(

(

)

)

)

(10)

(11)

|
|

|
|

where K in Eq. (10) indicates the number of clusters and
computes the ratio of the sum of scatter within clusters i
and  j to the distance between their centroids for each pair of
clusters with the index as the average of maximum ratios.
The term Ci indicates the number of data points in cluster
i , x represents a data point and d
 in Eq. (11) is the
distance between x and the cluster centre Ci . For each pair
of clusters, Mij with i and  j , calculate the distance between
the centroids d(centi + centj) in Eq. (12).
Mij =

centi − centj

x, centi

(

)

(12)

For various cluster numbers with a minimum of two clus-
ters, this FNFinRec algorithm computes the DBI , which
optimizes financial data clustering. Analyzing the Si + Sj
data helps segment and assist with risk management, per-
sonalized  recommendations  for  financial  services,  and
adaptability of financial products and services to different
types of users. By incorporating the proposed clustering
algorithm and Davies–Bouldin Index analysis into the big
analysis platform with financial dataset, the algorithm can
classify investors into different categories, enabling it to pro-
vide highly personalized financial recommendations based
 . As the number of clusters increases,
on

x, centi

d

x∈Ci

1
Ci

�

�

�

�

∑

the trend line decreases in the Davies–Bouldin Index (DBI),
suggesting that the clustering using the Fuzzy k means algo-
rithm is becoming more successful. Improving the model’s
capacity to group similar financial data points, a lower DBI
signifies better-defined cluster groups based on user interest
patterns. This means that as the number of clusters grows,
the clusters get more distinctive to provide investment rec-
ommendations based on the dynamically changing behavior
of user interests.

3.4   Neural Collaborative Filtering for Adaptive

Financial Recommendations

The recommendations will remain relevant since the model
can adjust to user interests that change over time through
continuous learning from new data. To provide users with
adaptive recommendations for investments that are appro-
priate for their risk-return profile, the NCF algorithm learns
through user data.

Step 1: user-item interaction matrix from  transaction

history.

Construct a matrix where rows represent users and col-
umns represent investment avenues like mutual funds, equity
markets, etc. Entries are binary, indicating whether a user is
interested in an investment type (1) or (0) otherwise. This
matrix is given as input to the NCF model, and the data
collected from interactions enables the model to understand
user interest patterns and estimate their subsequent invest-
ment patterns.

‖

‖

Table 2   User-item interaction
matrix

User

Fixed depos-
its

Mutual funds

Equity

Bonds

Real estate

Crypto

1
2
3
4
5

1
1
0
1
0

0
1
1
1
0

1
0
1
0
1

0
1
0
0
1

0
0
1
0
0

0
0
0
1
0

  310

Page 8 of 14

International Journal of Computational Intelligence Systems          (2024) 17:310

For each user, mapping user interest patterns as given in
Table 2 helps to analyze the risk levels of the investment
avenues that interacted with 1 in the interaction matrix and
are mapped to the appropriate risk category. Suppose a user
has interacted with multiple investment avenues within the
same risk level. In that case, one is selected based on prede-
fined rules, such as the frequency of interaction and prefer-
ence for specific avenues. If a user has expressed interest in
certain investments, the interaction matrix will represent that
interest as binary data. The level of risk associated with each
investment is classified as low for fixed deposits and bonds,
medium for real estate and mutual funds and high for equity
and cryptocurrency. To maintain fair representation even in
cases where some data are absent, the generated table shows
which investment paths each user prefers within each risk
category. The proposed NCF approach relies on this classifi-
cation to provide adaptive financial recommendations based
on users’ risk-return decisions.

Users’ chosen investment alternatives are displayed in
Table 3 according to their low, medium, or high-risk levels.
NCF analysis of user interaction data is the basis for the pref-
erences. Each user’s investing options are classified accord-
ingly based on their comfort level with risk. Investors’ risk
tolerance is defined in this table as either low, medium, or
high. It shows how the algorithm sorts investment opportuni-
ties according to risk profiles and how user preferences are
mapped to these groups. This categorization helps make sug-
gestions to consumers that are suitable for their level of risk.
Step 2: general matrix factorization and multi-layer per-

ceptron for training.

They are implementing a feedback mechanism to collect
user responses to recommendations, periodically update the
clusters based on new user data, and adjust recommenda-
tions based on real-time market conditions and user feed-
back. The NCF model typically consists of an embedding
layer followed by multiple dense layers where the embed-
ding layer maps each user and item to a lower-dimensional
space.
i)  User embedding matrix

These embeddings aim to map users and items to a low-
dimensional space where similar users and items are closer

Table 3   User investment preferences analyzed by risk level

User

Investment avenue (Low)

1
2
3
4
5

Fixed deposits
Bonds
Fixed deposits
Fixed deposits
Bonds

Investment ave-
nue (Medium)

Investment
avenue
(High)

Mutual funds
Mutual funds
Bonds
Mutual funds
Fixed deposits Mutual funds

Equity
Equity
Mutual funds
Crypto

together. This user embedding matrix can be represented in
the form of P ∈ ℝm×d
 where each row pur is a d-dimensional
embedding for the user ur.
ii)  Item embedding matrix

The matrix represents each financial service or investment
item in the same latent space. Similarly, Q ∈ ℝn×d
 indicates
a financial service embedding matrix where each row qi
is a d-dimensional embedding for item i . The embedding
size controls the dimensionality of the space, affecting the
model’s ability to capture complex patterns in user behavior.
Interaction prediction: The interaction prediction for the
user ur and financial item i is given by embeddings from the
matrices P and Q . The interaction prediction ̂ruri is given in
Eq. (13),

̂ruri = f (pur

, qi)

(13)

where  f (pur
For instance, using a multi-layer perceptron (MLP)

, qi) in Eq. (14) can be modeled in various ways.

f

pur

, qi

= MLP(f (pur

⊕ qi))

(14)

(

)

Here, an operator ⊕ indicates the concatenation, and MLP
is a fully connected neural network that takes the concat-
enated user and financial item embeddings as input and out-
puts and the prediction interaction score ̂ruri.

Training with loss function: The model is trained using a
loss function such as binary cross entropy for implicit feed-
back or MSE for explicit feedback. This loss function L
Yuri
is used to train the model to predict user interest patterns
(
)
based on implicit feedback. The goal is to minimize the loss
so that the model’s predictions ̂ruri closely match the actual
user interest ruri . For implicit feedback the binary values are
considered indicating whether a user has shown interest or
invested in certain investment avenues can be integrated as
given in Eq. (15).

1ifuserurhasinvestedinitemi
0otherwise

Yuri =

{

(15)

L

Yuri

=

rurilog

̂ruri

+

1 − ruri

log(1 − ̂ruri)

(ur, i)∈R
∑

[

(

)

(

)

(

)

]
(16)
The representation of R indicates the set of all user and
financial service item pairs provided with feedback. The
term ruri indicates the actual feedback given by the ur for
financial service item i followed by ̂ruri predicted feedback
for ur for financial service item i . The term log
 and
log(1 − ̂ruri) in Eq. (16) represent the logarithmic loss for
correct and incorrect predictions; this loss function penal-
izes the model more when the projections are confident but
incorrect. The hidden layers learn the interactions between
user and item embeddings. Additionally, the output layer

̂ruri

(

)

International Journal of Computational Intelligence Systems          (2024) 17:310

Page 9 of 14

  310

produces a score representing the predicted interest in an
investment type. The explicit feedback reflects user interest
level, which can be observed from Eq. (17).

L =

1
R

rur,i − ̂rur,i

2

)

(ur,i)∈R
∑

(

|

|

(17)

3.5   Adaptive Recommendation System

The adaptive financial recommendation system guides users
to make informed investment decisions using data-driven
insights  from  fuzzy  K-means  clustering  and  NCF.  The
measures of the system’s performance, such as recall and
precision at the top N recommendation, show how well the
recommendations are employed for each user, contributing
credence to data-driven decision-making.

Top-N recommendation: For each user ur , generate the
top-N recommendations by sorting items based on the pre-
dicted ratings ̂rur . Precision and recall for a user ur at rank,
N can be calculated using Eq. (18).

4.2   Performance Assessment

For comparison, the existing algorithms such as ANFIS [19],
PRS-MPT [20], IFCM [22], and K-L-KM [24] are consid-
ered for performance comparison. The metrics used for anal-
ysis are clustering quality evaluation using silhouette coef-
ficient Davis Bouldin Index, followed by recommendation
accuracy using mean square error, precision@k, recall@k,
and processing time analysis.

4.2.1   Clustering Quality

One of the most important metrics for assessing clustering
quality, the Silhouette coefficient and Davis Bouldin Index
(DBI), is utilized to analyze financial data for adaptive rec-
ommendations. This will be useful in evaluating the clusters’
quality, essential for grouping financial users based on their
preferences.

A.  Silhouette coefficient

Top − N

ur

= argsorti

̂rur

[∶ N]

(

)

pre@N =

recitems

{

|
|
|

}

(

)
∩ {relitems}
N

|
|
|

Recall@N =

recitems

∩ {relitems}

{
|
|
|

relitems
}

|
|

|
|

|
|
|

4   Experimental Environment

4.1   Training Parameters

Critical parameters are used in the study to optimize the
adaptive recommendation algorithm. The level of fuzzi-
ness in cluster assignments is determined by the fuzziness
parameter ( m ), an essential component of the fuzzy k-means
method. To accurately capture the relationships between
users and financial goods, the NCF model is set up with
three layers. The NCF uses an embedding size of 64 to bal-
ance computational economy and model performance. Users
will obtain the most relevant financial alternatives according
to their interests and investment habits because the system
is designed to deliver the top five recommendations. The
training-test split and the ability to provide top-N recom-
mendations show that the system can scale and adapt to a
growing dataset without losing accuracy or relevance.

(18)

(19)

(20)

The silhouette coefficient is an evaluation tool for user
interest pattern grouping, and it is helpful in more extensive
data on intelligent investment strategies. This coefficient
measures cluster coherence, and a higher value suggests that
the user behavior clusters are more distinct and well-defined.
This statistic verifies that users are appropriately grouped
according to their financial routines and preferences; it can
take values between -1 and 1, with close to + 1 signifying a
high separation across clusters.

s(i) =

b(i) − a(i)
max(a(i), b(i))

(21)

where a(i) in Eq. (21) is the average distance between the
point i and all other points in the same cluster, and b(i) is the
minimum average distance from point i to points in a differ-
ent cluster. Improved and adaptive financial recommendation
is the final result of the research’s usage of the Silhouette
coefficient to verify that fuzzy K-means clustering are good
at capturing complex user patterns.

The dotted lines show in Fig. 4 shows that the average
silhouette score plotted with cluster label and impact val-
ues. This evaluation provides significant and well-separated
clusters, resulting in more accurate and adaptable financial
recommendations. The silhouette score validates clustering
methods, which are essential to adapting financial advice
to particular user profiles in this research. Cluster 2 has the
highest average silhouette score of 0.690, making it the most
coherent and well-separated adaptive financial recommen-
dation system user group. This suggests that users in this
cluster share identical financial interest patterns, improving

  310

Page 10 of 14

International Journal of Computational Intelligence Systems          (2024) 17:310

Fig. 4   Clustering quality using silhouette coefficient

Fig. 5   Clustering quality using Davies–Bouldin index scores for dif-
ferent clusters

recommendation accuracy and relevance. An elevated aver-
age  silhouette  score  throughout  clusters  indicates  well-
defined and distinctive user profiles, allowing the computer
to make more personalized and successful financial sugges-
tions based on data patterns.

performance  evaluation.  Low  DBI  result  shows  well-
formed clusters and distinct user segments, suggesting that
the FNFinRec system can target them. High DBI indicate
that user segments are not diverse enough, requiring clus-
tering redesign to analyze the user interest patterns based
on the changing financial trends and services among users
with more features.

The results of the Davies–Bouldin Index (DBI) shown
in Fig. 5 demonstrated different FNFinRec cluster topolo-
gies  shown  in  this  picture.  The  DBI  measures  cluster
separation and compactness. Lower values indicate that
the clusters are better defined and more distinct. As the
number of clusters increases, the graph probably shows
that DBI scores decrease, which means that the cluster-
ing quality is improving. The ideal number of clusters to
utilize for user-specific financial behavior and preference
segmentation can be found with the help of this visualiza-
tion. If the recommendation system is to adapt financial
recommendations to different user segments successfully,
then it is essential to analyze DBI scores.

4.2.2   Recommendation Accuracy

A.  Mean square error

B.  Davies–Bouldin Index

The Davies–Bouldin Index measures cluster separa-
tion and compactness, making it valuable for clustering

For each model rur,i , provides the actual feedback and
̂rur,i indicates the predicted feedback for each user-financial
service pair in Eq. (22) is given below:

International Journal of Computational Intelligence Systems          (2024) 17:310

Page 11 of 14

  310

Compared to previous algorithms, FNFinRec shows bet-
ter precision across a range of k values shown in Fig. 7, sug-
gesting that a larger percentage of the top-k suggestions are
relevant to users. As k increases, the system’s accuracy may
decrease, showing that there is trade-off between the quan-
tity and quality of recommendations. This graph highlights
the success of FNFinRec’s neural collaborative filtering and
fuzzy k-means clustering combination, which leads to more
accurate and user-satisfying recommendations for financial
products.

C. Recall@k

FNFinRec consistently obtains better recall, demonstrat-
ing that it can include a more substantial number of relevant
financial goods in its top-k recommendations, regardless
of the value of k . This suggests that more relevant items
are caught as the suggestion list extends, since memory
improves as k increases. The strength of FNFinRec is in its
comprehensive financial advice, which ensures that users
don’t miss out on helpful products or services. Algorithms
may differ in their recall growth rates, which could be a
sign of how well they can find relevant items outside of the
top few recommendations as given in Fig. 8. If users have
frequently changing interest pattern, they are less likely to
pass up useful financial services and products.

MSE =

1
R

rur,i − ̂rur,i

(

2

)

(ur,i)∈R
∑

(22)

|

|

Improved performance is shown by lower MSE values.
To learn how model improvements result in better sugges-
tions, it is helpful to monitor changes in MSE over itera-
tions and across various models. When dealing with finan-
cial applications, this statistic comes in handy because
bigger forecast errors might result in significant losses. It
is necessary to refine the model if the MSE is large since
it shows that the predictions made by the model ̂rur,i are
considerably lower than the actual values. On the other
hand, if the MSE is low, it means the model better pre-
dicts financial recommendations based on user interests.
To ensure the proposed system gives accurate financial
recommendations, it provides a quantitative way to assess
and contrast how various models perform.

The suggested FNFinRec is one of several recommen-
dation algorithms compared here with their MSE metric
shown in Fig. 6. This proves that FNFinRec is more accu-
rate than competing algorithms when it comes to making
financial recommendations.

B.  Precision@k

Fig. 6   Recommendation accuracy using mean average precision

  310

Page 12 of 14

International Journal of Computational Intelligence Systems          (2024) 17:310

Fig. 7   Recommendation accuracy using Precision@k

4.2.3   Processing Time Analysis

5   Conclusion

The ability to update user interest patterns in real time
and provide timely and appropriate recommendations is
made possible by quicker processing speeds in financial
data analysis. Because of its adaptability, the system can
swiftly adjust to shifting user interests and market cir-
cumstances, resulting in better, more personalized invest-
ment recommendations. In financial data research, pro-
cessing time analysis includes comparing the execution
times of various algorithms and systems for preprocess-
ing data, MapReduce operations, and clustering, among
other tasks. The research found that processing times can
vary greatly across FNFinRec, ANFIS, PRS-MPT, IFCM,
and K-L-KM. If ANFIS requires 60 min to process data,
while IFCM only takes 40 min, then IFCM must be more
efficient as shown in Fig. 9. Decisions on the performance
and scalability of the system can be guided by an analysis
of these periods, which helps determine the algorithms
that are most efficient for managing massive amounts of
financial data. In earlier similarity calculation methods,
2) and from this pro-
the user similarity calculated is o(
posed approach mitigates the complexity to linear form.

u

|

|

The adaptive financial recommendation system processes
user data in real-time to provide individualized sugges-
tions, driven by Fuzzy K-means clustering and NCF. The
rapid  progression  of  user  preferences  and  marketplace
dynamics makes this an especially pertinent considera-
tion in the world of finance. An adaptive financial rec-
ommendation system that offers real-time individualized
investment  advice  utilizing  Fuzzy  K-means  clustering
and neural collaborative filtering (NCF) is presented in
the research work. In the dynamic financial sector, where
user interests and financial conditions are always shifting,
this proposed FNFinRec algorithm excels. The solution
outperforms conventional approaches by incorporating
sophisticated  algorithms,  which  improve  the  precision
and customization of financial suggestions. Dealing with
the immense amount and complexity of financial big data,
keeping computing efficient, and adjusting with evolving
s are all major challenges resolved using this algorithm.
Incorporating more sophisticated deep learning methods,
improving real-time flexibility, and fixing the issue for

International Journal of Computational Intelligence Systems          (2024) 17:310

Page 13 of 14

  310

Fig. 8   Recommendation accuracy using Recall@k

Fig. 9   Processing time analysis

adaptive behavior for new users are all potential areas are
focused with the user and financial service matrix and
clustering quality analysis. Regardless of these issues, the
system is a huge step forward in financial innovation and

shows promise in providing more personalized and precise
financial recommendation.

Further research might look into making AI systems that
are easier to understand and interact with more external data

  310

Page 14 of 14

International Journal of Computational Intelligence Systems          (2024) 17:310

sources that are updated in real-time, such as social media
and news. It might also broaden the system’s coverage to
include more financial services and goods.

Author contributions  Jinyong Yang wrote the main manuscript text
and prepared figures, tables and equations. Jinyong Yang reviewed the
manuscript.

Funding  No funding was received.

Data availability  The datasets used and/or analyzed during the cur-
rent study are available from the corresponding author on reasonable
request. No datasets were generated or analysed during the current
study.

Declarations

Conflict of interest  It is declared by the authors that this article is free
of conflict of interest.

Open Access    This  article  is  licensed  under  a  Creative  Commons
Attribution-NonCommercial-NoDerivatives 4.0 International License,
which permits any non-commercial use, sharing, distribution and repro-
duction in any medium or format, as long as you give appropriate credit
to the original author(s) and the source, provide a link to the Creative
Commons licence, and indicate if you modified the licensed material.
You do not have permission under this licence to share adapted material
derived from this article or parts of it. The images or other third party
material in this article are included in the article’s Creative Commons
licence, unless indicated otherwise in a credit line to the material. If
material is not included in the article’s Creative Commons licence and
your intended use is not permitted by statutory regulation or exceeds
the permitted use, you will need to obtain permission directly from the
copyright holder. To view a copy of this licence, visit http:// creat iveco
mmons. org/ licen ses/ by- nc- nd/4. 0/.

References

  1.  Odeyemi, O., Mhlongo, N.Z., Nwankwo, E.E., Scholatica, U.C.,
Okoye, C.C.: Big data applications in portfolio management: a
review of techniques and strategies. Int J Sci Res Arch 11(1),
1984–1999 (2024)

  2.  Ahmadi, S.: A comprehensive study on integration of big data
and AI in financial industry and its effect on present and future
opportunities. Int J Curr Sci Res Rev 7(01), 66–74 (2024)
  3.  Selvakumar, S., Inbarani, H., Shakeel, P.M.: A hybrid person-
alized tag recommendations for social e-learning system. Int J
Control Theory Appl 9(2), 1187–1199 (2016)

  4.  Olabanji, S. O., Oladoyinbo, O. B., Asonze, C. U., Oladoyinbo,
T. O., Ajayi, S. A., & Olaniyi, O. O. (2024) Effect of adopting AI
to explore big data on personally identifiable information (PII) for
financial and economic data transformation. Available at SSRN
4739227.

  5.  Leung, M.F., Jawaid, A., Ip, S.W., Kwok, C.H., Yan, S.: A port-
folio recommendation system based on machine learning and big
data analytics. Data Sci Finance Econ 3(2), 152–165 (2023)
  6.  Adeoye, O.B., Addy, W.A., Ajayi-Nifise, A.O., Odeyemi, O.,
Okoye, C.C., Ofodile, O.C.: Leveraging AI and data analytics for
enhancing financial inclusion in developing economies. Finance
Account Res J 6(3), 288–303 (2024)

  7.  Reddy, S.R.B., Reddy, S.: Large scale data influences based on
financial landscape using big data. Tuijin Jishu/J Propuls Technol
44(4), 3862–3870 (2023)

  8.  Eni, L. N., Chaudhary, K., Raparthi, M., & Reddy, R. Evaluating
the role of artificial intelligence and big data analytics in indian
bank marketing. Tuijin Jishu/Journal of Propulsion Technology,
44(3).

  9.  Chen, Z.L.: Research and application of clustering algorithm for
text big data. Comput. Intell. Neurosci. 2022(1), 7042778 (2022)
 10.  Li, Y., Chu, X., Tian, D., Feng, J., Mu, W.: Customer segmenta-
tion using K-means clustering and the adaptive particle swarm
optimization algorithm. Appl. Soft Comput. 113, 107924 (2021)
 11.  Huang, L., Lu, H.: Design of intelligent financial data manage-
ment system based on higher-order hybrid clustering algorithm.
PeerJ Comput Sci 10, e1799 (2024)

 12.  Sharaf, M., Hemdan, E.E.D., El-Sayed, A., El-Bahnasawy, N.A.:
A survey on recommendation systems for financial services. Mul-
timed Tools Appl 81(12), 16761–16781 (2022)

 13.  Cai, X., Hu, Z., Chen, J.: A many-objective optimization recom-
mendation algorithm based on knowledge mining. Inf. Sci. 537,
148–161 (2020)

 14.  Wan, H., Yu, S.: A recommendation system based on an adap-
tive learning cognitive map model and its effects. Interact. Learn.
Environ. 31(3), 1821–1839 (2023)

 15.  Azietaku, M. (2024). Customers Classification using Recency
Frequency,  Monetary  value  (RFM),  and  K-means  clustering
algorithm (Doctoral dissertation, Masarykova univerzita, Eko-
nomicko-správní fakulta).

 16.  Zare, H., Emadi, S.: Determination of customer satisfaction using
improved K-means algorithm. Soft. Comput. 24(22), 16947–
16965 (2020)

 17.  Asemi, A., Asemi, A., Ko, A.: Investment recommender system
model based on the potential investors’ key decision factors. Big
Data (2023). https:// doi. org/ 10. 1089/ big. 2022. 0302

 18.  Luo, W.: Application of improved clustering algorithm in invest-
ment  recommendation  in  embedded  system.  Microprocess.
Microsyst. 75, 103066 (2020)

 19.  Asemi, A., Asemi, A., Ko, A.: Adaptive neuro-fuzzy inference
system for customizing investment type based on the potential
investors’  demographics  and  feedback.  J  Big  Data 10(1),  87
(2023)

 20.  Sengupta, A., Jana, P., Dutta, P.N., Mukherjee, I.: Optimal stock
allocation for an automated portfolio recommender system in the
perspective of maximum fund utilization. Expert Syst. Appl. 242,
122857 (2024)

 21.  Li, L., Wang, J., Li, X.: Efficiency analysis of machine learning
intelligent investment based on K-means algorithm. Ieee Access
8, 147463–147470 (2020)

 22.  Dandugala, L.S., Vani, K.S.: Advancing big data clustering with
fuzzy logic-based IMV-FCA and ensemble approach. Iranian J
Fuzzy Syst 21(2), 141–160 (2024)

 23.  You, J.: E-commerce recommendation algorithm based on big
data analysis and genetic fuzzy clustering. Financial Eng Risk
Manag 6(9), 28–33 (2023)

 24.  Chiou-Wei, S.Z., Lee, Y.T.: Application of KL distance-based
intelligent recommendation method to fund recommendation for
users with investment behavior in Asia region. Heliyon (2024).
https:// doi. org/ 10. 1016/j. heliy on. 2024. e32959

 25.  Datta, N.: Finance data analysis (Version 1.0). Kaggle (2022).
Available at https:// www. kaggle. com/ code/ nitin datta/ finan ce-
data- analy sis/ input. Accessed 7 July 2022

Publisher's  Note  Springer  Nature  remains  neutral  with  regard  to
jurisdictional claims in published maps and institutional affiliations.

