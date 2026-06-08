SHS Web of  Conferences 218, 02012 (2025)
ICDDE 2025

https://doi.org/10.1051/shsconf/202521802012

Machine  Learning  Methods
Segmentation and Recommendation Systems

in  Customer

Yiran Guo*

Math & Agricultural and Natural Resource Department, University of Maryland, College Park,
Maryland, 20742, United States of America

Abstract. As access to all kinds of data becomes more and more available,
the need for people to efficiently classify and extract useful data is urgent,
especially  for  businesses.  Machine  learning  has  enhanced  recommender
systems through collaborative filtering, content-based filtering, and hybrid
models.  Collaborative  filtering  predicts  user  preferences  based  on  past
interactions but faces cold start and scalability issues. This article shows that
content-based  filtering  uses  attributes  to  recommend  items,  but  relies  on
metadata  quality.  Case  studies  show  that  Amazon  applied  collaborative
filtering  and  DBSCAN  for  fraud  detection,  improving  recommendation
accuracy by 12%. Banks use machine learning for segmentation and fraud
detection, and PCA improves anomaly detection by 15%. Healthcare applies
clustering for patient classification, improving treatment accuracy by 18%.
This article points out that current technical challenges include data quality
issues, privacy risks, and bias. Poor data quality leads to inaccurate results,
while  privacy  issues  (as  shown  by  the  Equifax  breach)  require  stronger
protection.  Future  solutions  include  bias  detection,  diverse  datasets,  and
encryption techniques to enhance security and reliability.

1 Introduction

In  a  competitive  and  data-driven  market,  understanding  and  dividing  customers  by  their
behavior and preferences is critical for businesses to thrive. Traditional way of learning such
information  and  making  segmentation  is  simply  to  separate  customers  by  demographics,
geography, and behavior. However, such approaches often fail to deal with the complexity
and size of modern datasets, and in the process, they create inefficiencies and miss out on
potential opportunities [1].

To solve such problems, machine learning has come into play. It has revolutionized these
fields,  delivering  scalable,  automated,  and  highly  accurate  solutions  that  outperform
traditional  methods  [2].  With  its  powerful  ability  to  segment  based  on  shared  traits,
companies can generate recommendation systems to tailor customers’ needs and encourage
sales. However, this system is not perfect, its efficacy largely relies on the ability to process
high amounts of data and adapt to changing consumer preferences [3]. At this point, choosing
different methods based on the data set traits becomes more important.

* Corresponding author: emilyg9@terpmail.umd.edu

 © The   Authors,  published  by EDP  Sciences.  This  is  an  open  access  article  distributed  under  the  terms  of the Creative
Commons Attribution  License  4.0  (https://creativecommons.org/licenses/by/4.0/).

SHS Web of  Conferences 218, 02012 (2025)
ICDDE 2025

https://doi.org/10.1051/shsconf/202521802012

In  the  past  decades,  machine  learning  has  significantly  progressed  in  customer
segmentation and recommendation systems. Early studies focused on clustering algorithms
like K-Means and hierarchical algorithms, which laid the groundwork for the grouping of
customers  based  on  shared  attributes  [1].  However,  challenges  such  as  making
recommendations for new users and learning user preferences with limited interaction scales
may  reduce  the  prediction  efficiency.    Subsequent  studies  introduced  more  advanced
techniques,  such  as  collaborative  filtering  and  content-based  filtering,  that  improved  the
accuracy of recommendation systems based on user behavior and product features [3].

More recently, hybrid models and reinforcement learning have combined the strengths of
different  methods  to  make  personalized  and  dynamic  recommendations  [2].  These
advancements indicate the evolution of machine learning methods and their growing impact
on marketing strategies.

This essay aims to provide a detailed comparison of machine learning methods used in
customer  segmentation  and  recommendation  systems.  It  will  evaluate  their  real-world
applications  across  industries  from  e-commerce  and  banking  to  healthcare,  taking  into
account  the  challenges  they  face.  Furthermore,  the  essay  will  explore  upcoming
improvements  and  trends,  such  as  explainable  AI,  federated  learning,  and  real-time
personalization. By doing so, it seeks to offer actionable intelligence on how businesses can
leverage machine learning to enhance customer experience and drive growth.

2  Overview  of  machine
segmentation

learning  methods

in  customer

2.1 Traditional customer segmentation methods

The  conventional  customer  segmentation  methods  employ  demographic,  geographic,  and
behavioral data in customer segmentation [4]. Although they are easy to implement and quite
straightforward, these methods are less scalable and data-sensitive dynamic. Hence, they are
not  the  most  effective  in  today's  competitive  economy  [5].  In  contrast,  machine  learning-
based segmentation has scalability, automation, and the ability to work with complex sets of
data  and  thus  is  an  improved  solution  for  modern-day  companies  [2].  This  revolution  of
machine learning has opened doors to new ways for companies to understand their customers
in more progressive and actionable forms.

2.2 Advantages of machine learning-based segmentation

Nowadays,  some  of  the  most  widely  used  machine  learning  algorithms  for  customer
segmentation are K-means clustering, Density-Based Spatial Clustering of Applications with
Noise  (DBSCAN),  and  Principal  Component  Analysis  (PCA).  All  these  methods  have
advantages and disadvantages, and therefore businesses need to make wise choices according
to their different types of data sets. K-means clustering is used for customer segmentation
based on similarity measures. It does this by dividing the data set into k groups, in which
each customer is placed in the group with exactly the nearest mean [1]. It can be used in big
data  and  is  extremely  easy  to  implement.  However,  one  of  the  main  limitations  is  that  it
requires the number of clusters to be specified before it can be implemented, which might
not  be  easy  if  the  cluster  number  is  unknown.  K-Means  also  assumes  that  clusters  are
spherical and are evenly distributed, which may not be the case in all real data.

2

SHS Web of  Conferences 218, 02012 (2025)
ICDDE 2025

https://doi.org/10.1051/shsconf/202521802012

2.3 Common machine learning algorithms for customer segmentation

DBSCAN groups points based on density and it identifies dense regions as clusters and marks
low-density points as noise, which doesn’t have such requirements as K-Means, so it is more
flexible than K-Means. That's why it performs excellently on outlier detection and handling
noise data. It also performs well with irregularly shaped data as it generates clusters based on
density rather than proximity to the center mean [3]. However, DBSCAN doesn’t perform
well with data sets that have varied densities and requires it to be very highly optimized in
its parameters.

To  overcome  some  issues  with  high-dimensional  data,  PCA  can  be  applied  as  a  pre-
processing phase before applications of clustering algorithms. Since PCA transforms high-
dimensional  data  into  a  lower-dimensional  space  while  preserving  as  much  variance  as
possible, it has fewer instances of features. PCA allows noise and redundancy removal in the
data, which results in improved performance of the clustering algorithm [6]. For example,
when  used  in  conjunction  with  K-Means,  PCA  is  used  to  remove  the  "curse  of
dimensionality"  so  that  the  high  dimensionalities  of  the  data  render  it  impossible  for  the
clustering algorithm to effectively identify patterns. But PCA also makes linear separability
assumptions and can do the same to remove important nonlinear relationships between data.

3 Machine learning in recommendation systems

3.1 The role of customer segmentation in recommendation systems

Generally speaking, customer segmentation sets the foundation for recommendation systems.
Customer segregation by attributes or behaviour helps the company learn about the interest
of the customers and suggest products or services according to customer needs. Some of the
most well-known and preferred techniques are collaborative filtering, content filtering, and
hybrid models.

3.2 Collaborative filtering

Collaborative  filtering  is  the  most  extensive  practice  of  recommendation  systems.  It  runs
under  the  premise  of  making  recommendations  with  the  assistance  of  user  feedback.  The
user-based  collaborative  filtering  suggests  items  for people  with  the  same  interests,  while
item-based  collaborative  filtering  suggests  the  same  kind  of  items  that  the  user  enjoyed
previously [2]. However, collaborative filtering experiences several crucial restrictions. For
example, the cold start problem is when the system does not suggest items for new customers
or items due to the non-existence of history. Scalability with big data is the second restriction
since the calculations become complex with the rise of items and customers [3].

3.3 Content-based filtering

On the contrary, content filtering cares more about item attributes rather than user-interaction
history.  It  applies  item  attributes  and  user  ratings  for  making  recommendations.  With  the
above scenario, if the user provides that they enjoyed action movies, the system will utilize
the data of the genre, actors, and director related to action movies to make recommendations
[1].  The  above  recommendation  tactic  is  effective  if  the  user-interaction  data  are  sparse.
However, the performance of content filtering heavily depends upon the quality and coverage
of the metadata. Poorly labeled and incorrect metadata may lead to undesired performances
of the system [4].

3

SHS Web of  Conferences 218, 02012 (2025)
ICDDE 2025

https://doi.org/10.1051/shsconf/202521802012

3.4 Hybrid models

To overcome the shortcomings of collaborative and content-based filtering, hybrid models
are suggested as a robust solution. For instance, matrix factorization models are capable of
factorizing the user-item interaction matrix into latent components and combining the latter
with  content-based  attributes  for  personalized  recommendation  intentions  [6].  The
mechanism  helps  the  system  assume  item  attributes  and  user  behavior  to  provide  more
accurate  and  richer  recommendations.  In  recent  years,  Hybrid  models  have  been  used  for
deep  learning  such  as  neural  networks  of  particular  interest.  The  models  are  capable  of
learning complex item attributes and user behavior relationships again for improvement of
recommendation precision [7].

Comparing these solutions, collaborative filtering is more appropriate for scenarios with
abundant user-interaction data since it learns implicit relationships between user behaviour.
However,  it  suffers  with  new  items/users  and  is  computationally  intensive  with  big  data.
Content-based filtering is suited wherever item metadata is abundant, thereby it is best suited
for expert markets/niche markets. However, the dependence of the quality on metadata can
be a challenge. Hybrid models integrate collaborative and content filtering by taking the best
of collaborative filtering and content filtering but with more challenges for deployment and
sustenance.

4 Real-world applications

4.1 Real-world applications

In the real world, machine learning methods are used in different fields by several successful
companies and have benefited customers around the world.

commerce platforms may handle massive amounts of data daily, which makes machine
learning  crucial  for  delivering  personalized  experiences  and  driving  sales.  For  example,
Amazon relies on collaborative filtering and deep learning to serve customers. The company
uses  Collaborative  filtering  to  analyze  user  behaviors,  such  as  their  past  purchases  and
browsing history, to suggest similar items that users may like [3]. For example, if a user buys
science fiction books with high frequency, Amazon’s system will recommend other science
fiction books purchased by other users with similar tastes. However, traditional clustering
methods like K-Means struggle with complex, non-linear user interactions.  To solve that
issue, Amazon has adopted DBSCAN to detect abnormalities such as fraudulent transactions.
Studies show that DBSCAN improves recommendation accuracy by 12% compared to K-
Means  in  handling  noisy  data  [8].  By  processing  these  vast  amounts  of data  in  real-time,
Amazon can ensure that recommendations remain relevant and timely.

4.2 Customer segmentation and fraud detection

In the banking and finance fields, while digital banking is thriving, institutions are available
to  get  more  transactional  data.  Under  such  conditions,  using  machine  learning  for
segmentation and recommendation becomes more urgent for providing better service. For
example, a bank might identify a group of high-net-worth individuals who frequently invest
in stocks and mutual funds. This segmentation allows the bank to offer products of exclusive
investment opportunities, to tailor the needs of this group [1]. Moreover, machine learning
plays  a  critical  role  in  fraud  detection.  Unusual  large  withdrawals  or  transactions  from
unfamiliar  places  can  be  seen  as  suspicious  by  analyzing  transaction  data  with  machine
learning models. Detecting high-dimension transactional data is challenging, using PCA to

4

SHS Web of  Conferences 218, 02012 (2025)
ICDDE 2025

https://doi.org/10.1051/shsconf/202521802012

reduce noise and highlight key transaction patterns improves the accuracy by 15% [9]. This
proactive approach helps banks protect their customers and reduce financial losses.

4.3 Patient segmentation and personalized treatment

In  healthcare  fields,  patient  segmentation  is  one  of  the  most  important  applications  of
machine learning. In such a situation, K-Means can be used to group patients based on their
medical history, symptoms, and genetic information. However, when it comes to complex
and overlapping medical conditions, DBSCAN identifies patients with similar symptoms and
genetic  markers  in  noisy  datasets.  By  doing  so,  patient  classification  accuracy  has  been
improved by 18% [7].

Doctors can identify the most effective treatment for patients. For example, in managing
chronic  diseases,  personalized  treatment  plans  can  significantly  improve  outcomes  [7].  A
study by Lee et al. also demonstrated how clustering algorithms could identify subgroups of
diabetes patients with distinct risk profiles, which enables healthcare providers to provide
more accurate interventions [10].

5  Challenges  in  machine  learning-based  segmentation  and
recommendations

One of the biggest challenges in machine learning-based segmentation and recommendation
systems is data quality. Since the accuracy of the method depends highly on the quality of
input data, any incomplete, noisy, or biased data might lead to poor  performance [3]. For
example,  if  a  retailer’s  company  contains  too  many  missing  values  or  outdated  data,  the
results  may  fail  to  reflect  current  behaviors.  Then  that  may  cause  irrelevant  marketing
campaigns and waste of money. Additionally, privacy concerns can make the use of machine
learning more complex. In health and finance industries, sensitive customer information is
collected,  which  makes  sensitive  data  protection  urgent.  A  notable  example  is  the  2017
Equifax  data  breach,  where  the  personal  information  of  147  million  people  was  exposed,
leading to widespread criticism and financial penalties [1].

For  suggestions  to  tackle  the  challenges,  it’s  important  to  develop  bias-detection
algorithms  and  diversify  training  datasets  to  improve  recommendations.  Also,  businesses
should  be  aware  of  privacy  issues,  especially  in  finance  and  healthcare.  Therefore,  using
advanced  encryption  techniques  to  protect  sensitive  information  is  beneficial  for  both  the
reputation and sticking to the policies.

6 Conclusion

By choosing different machine learning methods according to data traits, the segmentation
and  recommendation  accuracy  have  been  enhanced  in  different  scales.  Through  scalable,
automated, and accurate solutions, machine learning has outpaced traditional techniques that
were  overwhelmed  by  volume  and  complex  data.  At  the  same  time,  with  such  customer-
oriented  and  dynamic  recommendations,  companies  and  customers  can  both  enjoy  the
benefits of the market.

Despite  such  amazing  advancements,  there  are  problems.  Data  transparency  and  data
quality are some of the problems to be considered while using the machine learning approach.
However, the  revolutionary power of machine  learning in these sectors cannot be denied.
Organizations that can implement and integrate these technologies efficiently can still keep
a balance and grab market shares. Therefore, the solution lies in continuous research, ethical
practices, and commitment to deliver customers' values responsibly.

5

SHS Web of  Conferences 218, 02012 (2025)
ICDDE 2025

https://doi.org/10.1051/shsconf/202521802012

References

1.  Owolabi, P.C. Uche, N.T. Adeniken, O. Efijemue, S. Attakorah, O.G. Emi-Johnson,
E. Hinneh, Comparative analysis of machine learning models for customer churn
prediction in the U.S. banking and financial services: Economic impact and industry-
specific insights. J. Data Anal. Inf. Process. 12(3), 388–418 (2024)
P. Joga, B. Harshini, R. Sahay, Comparative analysis of machine learning models for
customer segmentation. In: SpringerLink (1970)

2.

3.  A. Amin, J.M. Chatterjee, Comparative analysis of machine learning models for

4.

customer segmentation. In: M.K. Shukla, A.K. Misra, A.L. Jameel, S. Gupta (eds.)
Advances in Computational Intelligence and Learning, pp. 63–75. Springer (2023)
S. Jain, S. Gupta, A review on customer segmentation methods using machine
learning. In: Proceedings of the 2021 International Conference on Data Science and
Engineering, pp. 333–344. Springer (2021)

5.  H. Smolic, How to use machine learning for customer segmentation. Medium (2024).
https://hrvoje-smolic.medium.com/how-to-use-machine-learning-for-customer-
segmentation-49612667301d

6.  A novel approach for customer segmentation and product recommendation to boost

sales using machine learning. IEEE Conf. Publ., IEEE Xplore (n.d.).

7.  G. Wang, Customer segmentation in the digital marketing using a Q-learning based

differential evolution algorithm integrated with K-means clustering. PLoS ONE 20(2)
(2025)

8.  R. Johnson, T. Smith, K. Brown, Customer segmentation in digital banking using

machine learning. Int. J. Bank. Finance 12(2), 78–95 (2021)

9.  Y. Chen, L. Zhang, H. Wang, Machine learning for fraud detection in banking: A

comprehensive review. J. Financ. Technol. 15(3), 45–60 (2022)

10.  S. Lee, J. Kim, H. Park, Personalized treatment plans for diabetes patients using

clustering algorithms. Healthc. Inform. Res. 27(4), 210–225 (2021)

6

