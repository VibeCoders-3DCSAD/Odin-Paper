A User Profile System for the Finance Platform of Commerce

Zhonghuang Hu
China Communications Trading &
Supply Co., Ltd.
Beijing, China
huzhonghuang@126.com

Yubo Qiu
China Communications Information
Technology Group Co.
Beijing, China
qiuyubo@ccccltd.cn

Songnan Hu
CCCC (Xiamen) E - commerce Co.,
Ltd.
Xiamen, China
husongnan@ccccltd.cn

Zijie Cheng
CCCC (Xiamen) E - commerce Co.,
Ltd.
Xiamen, China
chengzijie@ccccltd.cn

Shuai Qiu
CCCC (Xiamen) E - commerce Co.,
Ltd.
Xiamen, China
qiushuai@ccccltd.cn

Abstract
With the rapid advancement of big data technology, user profiling
has emerged as a critical tool for enterprises to refine operations and
enhance precision marketing. This paper explores the application
of user profiling within the financial platform of commerce, focus-
ing on the integration of internal and external data resources, data
mining techniques, and the construction of a user profile model and
system. The proposed system aims to achieve precise marketing,
risk control, and informed decision-making by providing compre-
hensive insights into user behavior and preferences. The system
encompasses modules for individual and group user profiles, be-
havior trend analysis, and tag management, facilitating detailed
user segmentation and targeted marketing strategies. A sample
K-means clustering algorithm is also presented to demonstrate user
grouping based on shared characteristics. The findings highlight
the potential of user profiling to improve customer satisfaction and
overall competitiveness in the financial industry, while promoting
cross-industry data integration and the continuous evolution of
user profile models.

CCS Concepts
• Information systems → Enterprise information systems.

Keywords
User Profile System, Behavior Analysis, Data Processing, Data Inte-
gration

ACM Reference Format:
Zhonghuang Hu, Yubo Qiu, Songnan Hu, Zijie Cheng, and Shuai Qiu. 2024.
A User Profile System for the Finance Platform of Commerce. In 2024 the
12th International Conference on Information Technology (ICIT) (ICIT 2024),
December 13–15, 2024, Kuala Lumpur, Malaysia. ACM, New York, NY, USA,
6 pages. https://doi.org/10.1145/3718391.3718436

Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
ICIT 2024, Kuala Lumpur, Malaysia
© 2024 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 979-8-4007-1737-6/24/12
https://doi.org/10.1145/3718391.3718436

1 INTRODUCTION
The information on the web is always too general to solve individual
user’s need. An accurate representation of a user’s interest is stored
in a user portrait. Researchers are interested in how to identify the
interest of the user and build an accurate profile.

In the year of 2015, the State Council of China proposed the “Ac-
tion Plan for Promoting the Development of Big Data” [4] pointed
that “the data has become a basic strategic resource for the coun-
try, and big data is increasingly becoming a new driving force for
economic transformation and development.” In 2016, in response
to the development and application of big data, the China Bank-
ing and Insurance Regulatory Commission emphasized the need
to proactively formulate a big data strategy, actively establish a
big data service system, strengthen data sharing, deepen big data
applications, and unleash the value of data. In view of the huge
data system and massive data, developing valuable information
through data mining has become an important challenge. As the
Internet gradually enters the era of big data, it will inevitably bring
a series of changes and reshapes to enterprises and user behaviors;
the biggest change is that all user behaviors are "visualized" in front
of enterprises. With the in-depth research and application of big
data technology, enterprises are increasingly focusing on how to
use big data to serve refined operations and precision marketing,
and then further explore potential business value. Therefore, the
concept of user profiling came into being. User protrait can make
the service objects of products more focused and more focused. To
increase client’s satisfaction and increase the competition, financial
institutions, especially banking institutions, need to rapidly inno-
vate their products. To make good use of existing data assets to
make data valuable. To achieve this goal, the use of user profile as
a tool has become a breakthrough in solving industry pain points.
User profiles can effectively present user characteristics and pro-
vide support for product innovation. Traditional financial industry
relies on communication between account managers and customers
to understand customers. The user profile system can effectively
break the resource binding relationship between account managers
and customer resources. Anyone can understand customers com-
prehensively and three-dimensionally through the system.

As industry competition continues to intensify, product and
service homogeneity and customer loyalty decrease, the stickiness
between users and products gradually decreases, and the user churn

267ICIT 2024, December 13–15, 2024, Kuala Lumpur, Malaysia

Trovato et al.

rate becomes more serious. Therefore, it is particularly important to
use multiple data sources and apply big data technology to achieve
more accurate user profiles, thereby promoting product optimiza-
tion, iterative upgrades of business, customized services and more
accurate marketing.

The rest of this paper is organized as follows: In Section 2 we
present related work. Preliminaries are given in Section 3. In Section
4, we present our user profile model and the system of user profile
is introduced in section 5. We conclude the work of this paper in
Section 6.

2 RELATED WORK
The Internet industry was the first to propose and apply user profile
technology. The concept originated from the Persona concept pro-
posed by Alan Cooper, the father of interactive design. Alan Cooper
explained that Persona is a virtual user corresponding to a real user,
and is a target customer model based on a series of real data. Based
on this technology, the user profile system was developed. Initially,
the University of California gradually learned by displaying and
collecting users’ satisfaction with the current page to establish a
user interest model. Later, the California University of Management
developed the user profile system Web Watcher [2], which changed
from individual users to group users, using data collectors to record
users’ behavior, preferences, and basic information on the Inter-
net, and using this statistical information to derive the browsing
behavior of user groups, thereby building a user interest model.

Currently, the need for software systems to automatically adapt
to their users has been recognized and the research on user pro-
file [9]. A user model is initialized either with default values or
by querying and grouping the user in “stereotypes” [1]. User pro-
file has been widely applied in the financial industry, e-commerce
industry, power industry, and telecom industry. Especially in the
financial industry, with the popularization of big data technology
and the emphasis on data in the financial industry, user profile has
gradually become an important means for financial institutions
to enhance their competitiveness. Recently, financial institutions
integrate internal and external data resources, utilize data mining
and big data analysis techniques, construct user profile models,
and achieve comprehensive understanding and accurate prediction
of customer behavior. This not only helps financial institutions
achieve precise marketing and risk control, but also improves cus-
tomer satisfaction and loyalty.

Franca et al. did research in the field of psychology highlighted
the value of identifying users’ personality traits, which helps build
adaptive and personalized systems and improve user experiences [5].
Gu et al. proposed a psychological modeling method based on
computational linguistic features to profile personality traits of
users on Sina Weibo and their correlations with user’s social be-
haviors [6]. This research investigates the potential relationship
between personality traits of users, profile information, and social-
network behaviors on Sina Weibo. This approach understanded
demographic and psychological profiles of users on social media
without customer disruption. Chen et al. used classification algo-
rithms in machine learning to predict users’ demographic attributes
based on a month of data collected with the Sogou search engine
in order to generate users’ profiles [3]. The proposed model is a

two-stage structure using a month of data with demographic labels
as the training data. The first stage of the structure is based on
traditional machine learning models and neural network models,
whereas the second one is a combination of the models from the
first stage. Paper [7] minis mobile user behavior patterns and con-
structs a group user profile by analyzing access data collected from
the WeChat Mini Program. They extract the attributes of mobile
users considering their age group, geographic information, and on-
line duration. Using Z-score standardized processing and K-means
clustering algorithm, they model the user profiles through three
dimensions including interaction intensity, daily average duration,
and access frequency. Zhang et al. constructed a power user behav-
ior assessment model based on a huge number of user profiles [11].
After text conversion, data cleaning and variable attribute analysis
the huge number of grid customer service phone data, a lot of user
profiles are established. The logistic regression model is combined
with the decision tree algorithm to complete the construction of
the electric power user behavior evaluation model.

The e-commerce industry utilizes the personal profile function
of social platforms for marketing and promotion, thereby enriching
the data dimensions of user consumption habits, consumption abil-
ity, consumption preferences, etc. accumulated by the e-commerce
industry itself, and efficiently conducting marketing and promo-
tion [10]. With the rapid development of big data analysis technol-
ogy and the rapid accumulation of data in various industries, user
profiles are gradually utilizing massive amounts of data between
industries to promote active understanding of users and provide
users with better experiences [8]. The enrichment of data dimen-
sions and the breaking of barriers to information exchange between
industries have driven the development of data analysis and the
improvement of user profile models, thus forming a virtuous cycle
mechanism. Methods and applications.

3 PRELIHMINARY
3.1 Data Acquisition and Data Processing
Data acquisition is based on varying user participation methods,
the collection of raw user profile data can be categorized into two
approaches: explicit and implicit acquisition. Explicit acquisition in-
volves users manually inputting their basic information, behavioral
preferences, and related data. This straightforward method offers
high-quality data but necessitates active user engagement and typi-
cally limits the scope of accessible information. Conversely, implicit
acquisition is transparent to users and encompasses two main tech-
niques: logging user information during interactions and analyzing
user behavior patterns to deduce characteristics. The richer data
obtained through implicit methods results in more comprehen-
sive user profiles. In practice, both methods are often combined by
industry and academia to leverage the diverse data trails left by
users.

Data processing refers to the purification of raw data to eliminate
impurities, yielding standardized data suitable for constructing user
profiles. Key data processing techniques include word segmenta-
tion, data filtering, and data normalization. Word segmentation is
crucial for unstructured text data processing; data filtering ensures
the reliability of basic data by ridding it of impurities; and data
normalization maintains consistency across input model data.

268A User Profile System for the Finance Platform of Commerce

ICIT 2024, December 13–15, 2024, Kuala Lumpur, Malaysia

3.2 Tag Selection and Tag Weight
Tags symbolize specific user characteristics and serve as a highly
correlated content organization method, enabling swift identifica-
tion of suitable content and classifications. From a computational
hierarchy perspective, tags can be categorized into fact tags and
model tags. Fact tags are derived from statistical analyses of raw
data, for instance, user purchase frequency, which reflects a statis-
tical overview of a user’s actual purchase behavior over a specified
duration. Conversely, model tags are formulated based on fact tags
by establishing associations with business challenges, thereby yield-
ing tags tailored for user profile selection models.

Tags primarily address the issue of description. However, in
practical applications, resolving the problem of data correlation is
equally important. Hence, tags are often designed as a comprehen-
sive system encompassing multiple tags. Each tag holds varying
degrees of significance in portraying specific dimensions of a user
profile. Consequently, assigning weights to these tags based on
their importance in characterizing user profiles is imperative. The
prevalent weighting methodologies can be broadly classified into
subjective and objective weighting methods. Objective weighting
methods encompass the entropy weight method, correlation co-
efficient method, and standard deviation method, among others.
Subjective weighting methods include the subjective experience
method, expert survey weighting method, Delphi method, and ana-
lytic hierarchy process.

3.3 User Profile Model selection
User profiling technology is a multidisciplinary combination that
requires knowledge fusion in areas such as knowledge graphs, nat-
ural language processing, machine learning, and data mining. The
commonly used user profile models are mainly divided into three
categories: text mining techniques, classification algorithms, clus-
tering algorithms, etc. Text mining mainly focuses on the mining
and processing of unstructured data, including TF-IDF, vector space
models, topic models, etc; Classification algorithms are suitable for
supervised learning user classification, including artificial neural
networks (ANN), proximity algorithms (KNN), support vector sup-
port machines (SVM), etc; Clustering algorithms are suitable for
unsupervised learning user clustering, including k-means clustering
algorithm, k-centroid algorithm, density based clustering algorithm
DBSCAN, hierarchical agglomerative clustering algorithm HAC,
etc.

The application scope of user profiling is very broad, mainly
including three aspects: firstly, by analyzing potential users and
targeting specific user groups for advertising placement, unneces-
sary cost investment can be reduced; Secondly, by analyzing the
correlation of user data, a personalized recommendation system
for users can be constructed to achieve customized deployment of
services or products for thousands of people; Thirdly, evaluate the
operational effectiveness of the enterprise, improve product opera-
tions, enhance service quality and user experience, and promote
the healthy development of the enterprise.

merged as a super-document to train the classifier for each concept.
A super-document goes through an indexing to calculate a vector.
The weight of each vocabulary term (vector) is stored the in that
concept. Thus, each concept is treated as n-dimensional vectors in
which n represents the number of unique terms in the vocabulary.
Each term weight is calculated as 𝑡 𝑓 × 𝑖𝑑 𝑓 and normalized by their
length. In more detail, 𝑢𝑤𝑖 𝑗 represents the unnormalized weight of
term 𝑖 in concept 𝑗, is calculated as equation (1) and (2)

𝑢𝑤𝑖 𝑗 = 𝑡 𝑓𝑖 𝑗 × 𝑖𝑑 𝑓𝑖

𝑖𝑑 𝑓𝑖 = 𝑙𝑜𝑔

#𝑜 𝑓 𝑑𝑜𝑐𝑢𝑚𝑒𝑛𝑚𝑡𝑠𝑖𝑛𝑡ℎ𝑒𝑐𝑜𝑙𝑙𝑒𝑐𝑡𝑖𝑜𝑛
#𝑜 𝑓 𝑑𝑜𝑐𝑢𝑚𝑒𝑛𝑡𝑠𝑖𝑛𝑡ℎ𝑒𝑐𝑜𝑙𝑙𝑒𝑐𝑡𝑖𝑜𝑛𝑡ℎ𝑎𝑡𝑐𝑜𝑛𝑡𝑎𝑖𝑛𝑡𝑖

(1)

(2)

where 𝑡 𝑓𝑖 𝑗 is the number of occurrences of 𝑡𝑖 in 𝑠𝑑 𝑗 , 𝑖𝑑 𝑓𝑖 ‘is the
super-document used for training concept 𝑗.

(2) Collecting user data. The documents are stored in a log file
by a proxy server. The documents are extracted for each user and
filtered to remove documents that are considered as not suitable
[10].

(3) classifying the documents. Documents and concepts are listed
in the vector model and the similarity is calculated in the vector.
The similarity between concept 𝑐 𝑗 and document 𝑑𝑘 is calculated
as equation (3).

𝑠𝑖𝑚𝑖𝑙𝑎𝑟𝑖𝑡𝑦 (𝑐 𝑗 , 𝑑𝑘 ) = 𝑐 𝑗 ◦ 𝑑𝑘 =

𝑛
∑︁

𝑖=1

𝑤𝑖 𝑗 × 𝑑 𝑗𝑘

(3)

where 𝑛 represents the number of terms in the vocabulary, 𝑤𝑖 𝑗 is
the normalized weight or term 𝑖 in concept 𝑗.

After the similarity is calculated, the results are sorted, the
weights from documents which match the same concept are accu-
mulated. A user file consists all concepts with weights are created
as a result.

As shown in Figure 1, the profile model contains four layers:

Figure 1: The User Profile Model

4 THE USER PROFILE MODEL
To build a user profile model, usually it requires three steps: (1)
Training the classifier. The training data for a particular concept are

Data Collection Layer: This foundational layer serves as the
cornerstone and indispensable prerequisite for building user pro-
files. It involves the systematic gathering of a myriad of data points

269ICIT 2024, December 13–15, 2024, Kuala Lumpur, Malaysia

Trovato et al.

from a variety of sources. These sources include but are not lim-
ited to user interactions on digital platforms, user information,
transactional histories, browsing behaviors, business activities, and
more. The data collected is both structured (e.g., numerical data in
databases) and unstructured (e.g., text data from social media posts).
The quality, completeness, and timeliness of the data collected are
crucial factors that directly influence the accuracy and reliability
of the user profiles generated.

Data Storage Layer: This layer is responsible for securely stor-
ing and managing the vast amounts of data collected from the data
collection layer. It employs advanced database management systems
and storage solutions to ensure the data is organized, accessible,
and scalable. The data storage layer also supports data backup and
recovery to ensure that data can be restored quickly and efficiently
in the event of a failure. Integrity checks, such as data validation and
consistency enforcement, are performed to maintain data accuracy
and reliability. Effective management of the data stored in this layer
enables seamless access and retrieval for subsequent processing
and analysis in the Middle Layer.

The Middle Layer: Positioned between the data storage layer
and the data visualization layer, this layer is a multifaceted entity
that can be both abstract and tangible. It serves as the brain of the
profile system, interacting with both the data storage layer and
the data visualization layer to implement the intricate business
logic of user profiles. The middle layer is tasked with processing,
integrating, and analyzing the data stored in the bottom layer. This
includes data cleaning to remove inconsistencies and errors, data
normalization to ensure uniformity, and data enrichment to add
context and value. Additionally, the middle layer employs advanced
algorithms and machine learning models to extract meaningful
insights and patterns from the data. These insights are then used to
create detailed and nuanced user profiles that encapsulate various
aspects of user behavior, preferences, demographics, and more.
Through sophisticated data visualization tools and systems, the
data results and models implemented in the middle layer can be
transformed into visually compelling and easily understandable
formats. This enables business users and analysts to gain insights
into user behavior, identify trends, and make informed decisions
based on data-driven insights.

Data Visualization Layer: This is the pinnacle of the profile
system, often referred to as the narrow user profile. It represents
the final output, presenting the insights and patterns derived from
the middle layer in a visually appealing and intuitive manner. The
data visualization layer employs a variety of charts, graphs, dash-
boards, and other visual elements to display user profiles, trends,
and patterns. These visualizations enable business users to quickly
and easily understand complex data sets, identify key trends and
insights, and make data-driven decisions. By providing a clear and
concise view of user behavior and preferences, the data visual-
ization layer supports strategic planning, product development,
marketing campaigns, and more.

5 A USER PROFILE SYSTEM
The user profile system is developed to provide precise marketing,
risk prevention and control, decision-making. The main functional-
ities currently contain three parts, as shown in Figure 2:

User Profile Module includes three main functionalities. List
of User Profiles contains a collection of all user profiles created
within the system, allowing for easy access and overview. Indi-
vidual User Profile details profile of individual user, including
user basic information, user financial information, user working
information, user company information, user preferences, purchase
history, and any other relevant data points. This provides a holistic
view of each user. User Behavior Trends provide analysis and vi-
sualization of user behavior over time, identifying patterns, trends,
and changes in user preferences or interactions. This can help pre-
dict future behaviors and optimize user engagement strategies.

User Group Profile Module include five major functionalities.List
of User Groups Profiles contains a collection of all user group
profiles, enabling quick navigation and comparison between differ-
ent user groups. Individual User Group Profile contains in-depth
profiles of a specific user group, detailing shared characteristics,
interests, and behaviors. This helps tailor marketing and product
development efforts to better meet the needs of these groups. User
Group Analysis details examination of user group data, including
demographics, preferences, and behaviors, to gain insights into the
unique qualities and challenges of each group. User Group Trends
provide tracking and analyzing trends within user groups, such
as changes in preferences or emerging behaviors, to stay ahead
of market shifts and user needs. User Group Company Analy-
sis evaluates how user groups interact with specific companies,
identifying areas for improvement, and opportunities for deeper
engagement or loyalty building.

Tag Information Module contains three key functionalities. List
of User Tags includes a list of all tags assigned to individual users,
helping to categorize and group users based on shared attributes and
behaviors. List of User Group Tags is similar to user tags, but for
user groups, allowing for the categorization and analysis of groups
based on common characteristics and trends. Tag Management
provides tools for creating, editing, and deleting tags, as well as
assigning them to users or user groups. This feature ensures that
the tagging system remains up-to-date and relevant, supporting
accurate and efficient user segmentation and analysis.

5.1 Sample Characteristics of User Profile
The Table 1 describe a list of sample characteristics of user’s basic
information used in profile.

5.2 A Sample K-means User Grouping

Algorithm

The K-means algorithm is an unsupervised learning algorithm used
to divide a dataset into K clusters (groups), where each cluster is
represented by its centroid (center point) [8]. The algorithm contin-
uously updates the centroid and grouping through iteration until
the convergence condition is reached. In user grouping applications,
users with similar characteristics or behaviors can be grouped to-
gether to facilitate subsequent recommendations, analysis, and
other applications.

A sample K-means algorithm for grouping users is provided as

follows.

(1) Initialize centroids: Randomly select K users from the user

dataset as the initial centroids.

270A User Profile System for the Finance Platform of Commerce

ICIT 2024, December 13–15, 2024, Kuala Lumpur, Malaysia

Figure 2: Functionalities of the User Profile System

User Info User Financial Info

Name
Age
ID
Education
Gender
Email
Cell Phone

Contribution
Level of Credit
Income
Expenditure
Row Asset
Debt

User Working Info
Company
Position and Rank
Work Experience
Year of working in the Company
Industry Background

User Transaction Info
Transaction of Parties
Transaction Items
Time and Location
Transaction Status
Price and Payment Method
Relevant Information
Transaction History

Table 1: User Characteristics

(2) Iteration process: Start iterating until the maximum num-
ber of iterations Max_iteration is reached or the change in
centroid is less than the threshold Threshold.

(a) Grouping: For each user, calculate their distance to all cen-
troids and assign them to the group with the centroid with
the smallest distance. During initialization, set a maximum
value as the minimum distance, traverse all centroids, find
the centroid with the smallest distance, and record the
index of that centroid as the user’s group ID. After as-
signing each user to the corresponding group, the current
grouping result User_Groups is obtained.

(b) Update centroid: For each group, calculate the centroid
of all users within the group (i.e., the new centroid). This
is usually achieved by calculating the average of all user
information within the group. Store all new centroids in
the new_centroids list.

(3) Check convergence: If the change between the new and old
centroids is less than the given threshold Threshold, the
algorithm is considered to have converged and the iteration
is stopped. Otherwise, assign the new centroid to the original
centroid and continue with the next iteration.

(4) Return result: When the iteration ends, return the final group-

ing result User_Groups and centroid Centroids.

6 CONCLUSION
User profiling provides comprehensive user insights for financial
institutions through in-depth analysis of user behavior and pref-
erences. This not only helps financial institutions achieve precise
marketing and risk control, but also significantly improves cus-
tomer satisfaction and loyalty. In the financial supply chain, user
profiling has become a key means for financial institutions to en-
hance their competitiveness. With the increase of data dimensions

Algorithm 1 K-means Algorithm for Grouping Users

Input: User_Dataset, K, Max_Iteration, Threshold
Output: User_Groups, Centroids

1: for iteration in range(Max Iteration) do
2:

User_Groups=[ ]
for user in User_Dataset: do

3:

4:

5:

6:

7:

8:

9:

10:

11:

12:

13:

14:

15:

16:

17:

18:

19:

20:

21:

22:

min_distance =maximum value
for centroid in Centroids: do

distance = calculating the distance between user and
centroid
if distance<min_distance: then

min_distance=distance
group_id=current centroid’s index

end if
User_Groups.append(group id)

end for

end for
new_centroids=[]
for i in range K: do

Group_Users = select all users in User_Dataset in group i
new_centroid= calculating Group_Users’s center
new_centroids.append(new_centroid)

end for
if the change of group center is less than Threshold then

Break

end if
Centroids=new_centroids

23:
24: end for
25: return User_Groups and Centroids

271ICIT 2024, December 13–15, 2024, Kuala Lumpur, Malaysia

Trovato et al.

and the breaking of information exchange barriers between indus-
tries, the construction of user profiles will pay more attention to
the integration and sharing of cross-industry data. This not only
enriches the content of user profiles, improves their accuracy and
comprehensiveness, but also promotes the development of data
analysis technology and the improvement of user profile models,
forming a virtuous cycle mechanism.

References
[1] P. A. Akiki, A. K. Bandara, and Y. Yu. 2016. Engineering adaptive model-driven
user interfaces. IEEE Transactions on Software Engineering 42, 12 (2016), 1118–
1147.

[2] R. Armstrong, D. Freitag, and T. Joachims. 1995. Webwatcher: A learning appren-
tice for the world wide web. In AAAI Spring symposium on Information gathering
from Heterogeneous, distributed environments. 93–107.

[3] Y. Chen, J. He, W. Wei, N. Zhu, and C. Yu. 2021. A Multi-Model Approach for

User Portrait. Future Internet 13, 6 (2021), 142–147.

[4] China State Council. 2015. The State Council issues a document to promote the
development of big data Notice of Action Plan. https://www.gov.cn/zhengce/

content/2015-09/05/content_10137.htm

[5] FO. Franca, DH Goya, and CL. C. Penteado. 2018. User profiling of the Twitter
Social Network during the impeachment of Brazilian President. Social Network
Analysis & Mining 8, 1 (2018), 1–5.

[6] H. Gu, J. Wang, Z. Wang, B. Zhuang, and F. Su. 2018. Modeling of User Portrait
Through Social Media. In 2018 IEEE International Conference on Multimedia and
Expo. 1–6.

[7] T. Hovorushchenko, D. Medzatyi, D. Kvanitskyi, and S. Kravchuk. 2022. Character-
istics and Method of Forming the User Information Portrait. In 12th International
Conference on Dependable Systems, Services and Technologies. 1–6.

[8] P. Keikhosrokiani and G. M. Fye. 2024. A hybrid recommender system for health
supplement e-commerce based on customer data implicit ratings. Multimedia
Tools & Applications 83, 15 (2024), 45315–45344.

[9] Alfred Kobsa. 1993. User Modelling: Recent work, prospects and hazards. Adaptive

User Interfaces: Principles and Practices 10 (1993), 1–14.

[10] X. Wang, B. Cai, and K. Salleh. 2024. Research on the application of cluster analysis
in cross-border e-commerce customer segmentation and market strategy. Applied
Mathematics and Nonlinear Sciences 9, 1 (2024), 2024–2568.

[11] M. Zhang, Z. Deng, C. Song, H. Liu, and M. Ding. 2022. Power user behavior
evaluation model based on 95598 user portrait. In International Conference on
Algorithms, Microchips and Network Applications. SPIE. 454–459.

272