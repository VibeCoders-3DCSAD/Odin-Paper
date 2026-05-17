Artificial Intelligence Review (2023) 56:13521–13617
https://doi.org/10.1007/s10462-023-10466-8

Deep learning modelling techniques: current progress,
applications, advantages, and challenges

Shams Forruque Ahmed1 · Md. Sakib Bin Alam2 · Maruf Hassan1 ·
Mahtabin Rodela Rozbu3 · Taoseef Ishtiak4 · Nazifa Rafa5 · M. Mofijur6,7 ·
A. B. M. Shawkat Ali8,9 · Amir H. Gandomi10,11

Published online: 17 April 2023
© The Author(s) 2023

Abstract
Deep learning (DL) is revolutionizing evidence-based decision-making techniques that can
be applied across various sectors. Specifically, it possesses the ability to utilize two or more
levels of non-linear feature transformation of the given data via representation learning in
order to overcome limitations posed by large datasets. As a multidisciplinary field that is
still in its nascent phase, articles that survey DL architectures encompassing the full scope
of the field are rather limited. Thus, this paper comprehensively reviews the state-of-art DL
modelling  techniques  and  provides  insights  into  their  advantages  and  challenges.  It  was
found  that  many  of  the  models  exhibit  a  highly  domain-specific  efficiency  and  could  be
trained by two or more methods. However, training DL models can be very time-consum-
ing, expensive, and requires huge samples for better accuracy. Since DL is also suscepti-
ble  to  deception  and  misclassification  and  tends  to  get  stuck  on  local  minima,  improved
optimization of parameters is required to create more robust models. Regardless, DL has
already been leading to groundbreaking results in the healthcare, education, security, com-
mercial,  industrial,  as  well  as  government  sectors.  Some  models,  like  the  convolutional
neural network (CNN), generative adversarial networks (GAN), recurrent neural network
(RNN), recursive neural networks, and autoencoders, are frequently used, while the poten-
tial of other models remains widely unexplored. Pertinently, hybrid conventional DL archi-
tectures have the capacity to overcome the challenges experienced by conventional models.
Considering that capsule architectures may dominate future DL models, this work aimed to
compile information for stakeholders involved in the development and use of DL models in
the contemporary world.

Keywords  Deep learning · Deep learning architecture · Neural network · Boltzmann
machine · Deep belief network · Autoencoders

 *  Shams Forruque Ahmed

shams.ahmed@auw.edu.bd; shams.f.ahmed@gmail.com

 *  Amir H. Gandomi

gandomi@uts.edu.au

Extended author information available on the last page of the article

Vol.:(0123456789)1 3

13522

1  Introduction

S. F. Ahmed et al.

Developing  machines  with  the  ability  to  ‘think’  has  been  a  long-running  aspiration  of
inventors  throughout  history.  The  popular  idea  of  replicating  intelligent  human  behavior
arranged as processes in machines (Dick 2019) has fueled researchers’ imaginations. In the
present time, artificial intelligence (AI) is a thriving and rapidly changing field with vari-
ous applications in society and economics, such as understanding speech or images, textual
analysis,  and  in  supporting  an  actively  growing  research  body  (Lu  et  al.  2018).  Machine
learning  (ML),  a  part  of  AI,  is  a  multidisciplinary  field  spanning  computer  science,  sta-
tistics,  and  data  science  that  addresses  the  need  for  computers  to  improve  automatically
through experience and by the use of data (Jordan and Mitchell 2015). ML is advancing
evidence-based  decision-making  in  the  fields  of  healthcare,  education,  national  security,
finance,  economics,  manufacturing,  and  marketing  (Jordan  and  Mitchell,  2015),  specifi-
cally by implementing various approaches to teach computers to achieve tasks. However,
conventional ML techniques cannot efficiently process raw data and require mindful engi-
neering and great expertise (Lecun et al. 2015). In the real world, every piece of data may
be  influenced  by  different  factors  of  variations,  thus  requiring  humans  to  factor  in  those
variations  and  decide  whether  to  incorporate  them  or  not.  Overcoming  such  flaws,  deep
learning (DL) has recently emerged as a promising approach in ML (Lecun et al. 2015),
currently dominating the majority of the works in the field of ML (Alpaydin 2020).

While it may appear as a seemingly new concept, the idea of DL can be traced back to
the 1940s and subsequently underwent roughly three waves of development with the most
recent  current  revival  beginning  in  2006  (Goodfellow  et  al.  2016).  During  the  first  wave
between 1940 and 1960, DL was known as cybernetics, then it gained popularity again in
the 1980s-1990s as connectionism. Fundamental methods such as radial basis function net-
works and multilayer perceptrons were employed in 2014 to solve the problem of design-
ing mobile adaptive tracking controllers (Tzafestas 2014). These two neural networks were
found  suitable  for  decision-making  and  control.  Later,  Sengupta  et  al.  (Sengupta  et  al.
2020)  pointed  out  a  few  reasons  why  DL  rose  to  prominence  in  the  twenty-first  century,
including the surge of “big data” with quality labels, improvements in regularization tech-
niques,  development  of  near-perfect  optimization  algorithms,  creation  of  niche  software
platforms  that  can  enable  the  integration  of  architectures,  and  advancements  in  paral-
lel  computing  power  and  multi-core,  multi-threaded  execution.  In  fact,  big  data  became
a  huge  issue  for  conventional  ML  algorithms  along  with  the  increasing  size  of  the  net-
work, whereby the performance of old algorithms either became overloaded or deteriorated
(Khamparia  and  Singh  2019).  The  enhanced  performance  of  DL  can  be  attributed  to  its
ability to utilize two or more levels of non-linear feature transformation of the given data
(Zeiler and Fergus 2014).

Deep  learning  allows  computational  models  with  multiple  layers  to  gradually  extract
higher-level features from the raw input (Alpaydin 2020; Deng and Yu 2014). The “deep”
in  DL,  therefore,  denotes  a  high  credit  assignment  path  (CAP)  depth,  which  has  been
assigned a value of 2 by most researchers (Sugiyama 2019; Telikani et al. 2021; Kashyap
et al. 2021; Mousavi and Gandomi 2021; Tahmassebi et al. 2018a, b, 2019, 2020; Jayara-
man  et  al.  2020;  Kumar  et  al.  2019).  Deep  learning  enables  computers  to  learn  com-
plex  concepts  by  forming  them  out  of  simple  ones.  Goodfellow  et  al.  (2016)  adequately
explained that, “Deep learning is a particular kind of machine learning that achieves great
power and flexibility by learning to represent the world as a nested hierarchy of concepts,
with each concept defined in relation to simpler concepts, and more abstract representations

1 3
13523

computed in terms of less abstract ones” (Goodfellow et al. 2016). DL is primarily based
on artificial neural networks, a type of computing system roughly mimicking the biological
neural networks of animal brains (Chen et al. 2019), and may employ supervised, unsuper-
vised, or semi-supervised representation learning (Bengio et al. 2013; Lecun et al. 2015;
Schmidhuber 2015). Representation learning, also known as feature learning, sets DL apart
from other techniques in ML. Unlike manual feature engineering, feature learning enables
computers  to  spontaneously  find  the  representations  required  for  the  classifications  from
raw data (Bengio et al. 2013). DL, therefore, relies on very little hand-tuning and has the
ability to analyze the rapidly increasing computations and data. The requirement for man-
ual engineering is only restricted to operations, such as altering the numbers and sizes of
layers, to yield different degrees of abstraction (Bengio et al. 2013; Lecun et al. 2015).

The  applications  of  DL  span  various  disciplines  and  sectors.  To  begin  with,  DL  has
exhibited  remarkable  performance  in  image  recognition  (Carrio  et  al.  2017;  Krizhevsky
and Hinton 2017; Lecun et al. 2015; Szegedy et al. 2015; Tompson et al. 2014; Wei et al.
2019), displayed potential in image restoration (Schmidt 2014), and demonstrated ground-
breaking results in speech recognition (Cireşan et al. 2012; Deoras et al. 2011; Hinton et al.
2012; Lecun et al. 2015; Sainath et al. 2013). It is currently used in the speech recognition
systems of major day-to-day products (Case et al. 2014; Deng and Yu 2014; Lemley et al.
2017) as well as in the operation of unmanned vehicles (Carrio et al. 2017). The area of
language processing has also been harnessing the benefits of DL (Deng and Yu 2014), in
which  DL  contributes  to  natural  language  understanding  and  translation  (Collobert  et  al.
2011; Mesnil et al. 2015; Sutskever et al. 2014), query response (Bordes et al. 2014), sen-
timent  analysis,  text  classification,  information  recovery  (Huang  et  al.  2013;  Shen  et  al.
2014),  and  writing  style  recognition  (Brocardo  et  al.  2017),  just  to  name  a  few.  DL  has
also been revolutionizing the health sector (Miotto et al. 2018), particularly yielding far-
reaching implications for drug discovery and design and in effectively predicting interac-
tions of potential drugs with molecules of interest (Ma et al. 2015). DL’s ability to acquire
end-to-end  learning  models  from  complex,  unstructured,  diverse,  and  poorly  annotated
data  has  also  led  to  advancements  in  biomedical  research  (Collobert  et  al.  2011;  Naylor
2018;  Ravì  et  al.  2017).  With  its  high  image  recognition  skills,  DL  has  been  applied  in
clinical imaging, such as neuroimaging (Sui et al. 2020), and has shown great promise in
the identification and detection of lesions, cancer cells, and different organs, as well as in
image  enhancement  (Cao  et  al.  2019;  Litjens  et  al.  2017;  Wieslander  et  al.  2017).  Bio-
informatics has also applied DL for predicting gene ontology annotations, understanding
the functions of different genes (Chicco et al. 2014), and most importantly for anticipating
how mutations in non-coding DNA affect gene expressions and susceptibility to diseases
(Leung et al. 2014; Xiong et al. 2016).

DL’s applications range far beyond science. For example, the military has taken advan-
tage of the highly efficient image and object recognition ability of DL for various opera-
tions  (Mendis  et  al.  2016;  Yang  et  al.  2018).  Businesses  have  applied  DL  for  improving
their customer relationship management, where it allows for the estimation of the customer
lifetime value that would result from possible direct marketing activities (Tkachenko 2015).
The recommendation systems in various commercial products utilize DL to understand and
predict user preferences (Da’u and Salim 2020; Feng et al. 2019; Oord et al. 2013). Simi-
larly, it has been also used in targeting an appropriate audience for mobile advertisements
(De  et  al.  2017).  Furthermore,  DL  utilizes  both  supervised  and  unsupervised  learning  in
financial fraud detection and anti-money laundering by identifying anomalies and abnor-
mal money transactions (Paula et al. 2016). While DL has been helping to advance several
fields of research, society, and the economy, it can also be exploited for malicious attempts.

Deep learning modelling techniques: current progress,…1 313524

S. F. Ahmed et al.

For instance, DL has been drawing criticisms for compromising cybersecurity as it is sus-
ceptible to attacks by hackers and to deceit (Li et al. 2019a, b, c, d; Norton and Qi 2017;
Papernot et al. 2016). Nevertheless, DL modelling architectures suffer from some errors;
in  several  instances,  DL  was  found  to  misclassify  or  randomly  classify  images  (Nguyen
et al. 2015; Szegedy et al. 2015). To tackle these issues, it is pertinent to design models that
internally create states that are equivalent to image-grammar (Zhu and Mumford 2006). In
addition, Mühlhoff (2020) has argued that despite its much-extolled advantage of requiring
minimal  hand-tuning,  DL,  in  fact,  relies  on  microwork  by  humans,  thereby  calling  it  “a
form  of  distributed  orchestration  of  human  cognition  through  networked  media  technol-
ogy” (Mühlhoff 2020).

The uses of DL technologies in the contemporary world and their potential for further
applications cannot be disregarded, despite some limitations. Many scholarly works have
been  undertaken  to  comprehensively  review  the  applications  of  DL  technologies  across
different  sectors.  Most  review  works  focus  on  specific  areas  and  implementations  of  DL
(Arulkumaran et al. 2017; Gheisari et al. 2017; Pouyanfar et al. 2018; Vargas et al. 2017).
Other  reviews  have  surveyed  DL  architectures  and  algorithms  in  the  context  of  specific
applications, such as speech emotion recognition (Fayek et al. 2017; Pandey et al. 2019),
text  classification  (Zulqarnain  et  al.  2020),  early  diagnosis  of  Alzheimer’s  (Ortiz  et  al.
2016),  electronic  health  records  (Roberto  et  al.  2020;  Xiao  et  al.  2018),  medical  image
analysis  (Akkus  et  al.  2017;  Cao  et  al.  2019;  Liu  et  al.  2019;  Shoeibi  et  al.  2020),  time
series  forecasting  (Lara-ben  and  Carranza-garc  2021),  aircraft  maintenance,  repair,  and
overhaul (Rengasamy et al. 2018), and land cover mapping (Pashaei and Kamangir 2020).
With  DL  having  gained  momentum  only  recently,  review  articles  on  DL  architectures
encompassing  the  full  scope  of  the  field  are  still  lacking.  Dixit  et  al.  (Dixit  et  al.  2018)
provided a brief overview of seven of the most widely used DL architectures (deep neu-
ral  networks,  deep  belief  networks,  recurrent  neural  networks,  deep  Boltzmann  machine,
restricted  Boltzmann  machine,  deep  autoencoders,  and  convolutional  neural  networks),  a
list of DL libraries, and some of the most common applications. However, as is perceiv-
able, their paper is not a comprehensive review of existing architectures. In addition to the
models  discussed  by  Dixit  et  al.  (2018),  Sengupta  et  al.  (2020)  have  covered  generative
adversarial neural networks and highlighted tests that can be undertaken before implement-
ing different neural networks in safety–critical systems. Shrestha et al. (Shrestha 2019) pro-
vided a rigorous overview of the neural networks and DNNs and found certain limitations
that  constrain  training,  such  as  overfitting,  long  training  time,  and  high  susceptibility  to
getting stuck in the local minima.

Khamparia and Singh (2019) contributed perhaps one of the most important studies
on DL architectures, even though it is limited to neural networks. Their meta-analysis
critically reviewed twelve DL modelling techniques and found that advanced DL archi-
tectures that are combinations of a few conventional architectures are far more robust
than  their  conventional  counterparts.  A  comprehensive  list  of  DL  architectures  and
their related applications was also presented. Nevertheless, as a continuously expand-
ing and developing field, there is a need to critically review and compile information
on  the  state-of-art  DL  modelling  techniques.  Therefore,  by  first  delving  into  a  brief
discussion  on  DL  as  a  subset  of  ML,  this  paper  comprehensively  reviews  all  of  the
available DL modelling techniques. While these modelling techniques have many ben-
efits across multiple disciplines, they are not without limitations. Therefore, this paper
also  highlights  the  advantages  and  drawbacks  of  these  models  and  concludes  with
future perspectives on DL models, providing directions for enhancing the architecture
designs  and  increasing  the  implementation  of  DL  technologies  across  more  sectors.

1 3
Overall, this paper aims to disseminate essential information on the constantly evolv-
ing field of deep learning and direct future research towards improving existing model-
ling techniques.

13525

2   Methodology for selecting, collecting, and analyzing pertinent data

This  review  utilized  an  integrative  literature  method  to  analyze  almost  all  available
deep  learning  modelling  approaches,  as  well  as  their  current  progress,  applications,
advantages, and challenges. Throughout this method, relevant and reliable papers were
selected, collected, filtered, carefully evaluated and analyzed. The database was found
using  credible  websites,  e.g.  Scopus  and  refereed  journals  from  reputable  publish-
ers  such  as  Nature,  Elsevier,  Taylor  &  Francis,  Springer,  Wiley,  ACS,  Inderscience,
MDPI, Frontiers, and Sage. Relevant keywords such as “Deep learning”, “Deep learn-
ing  architecture”,  “Deep  learning  modelling”,  “Advantages  of  deep  learning”,  “Chal-
lenges  of  deep  learning”,  “Future  of  deep  learning”,  and  each  deep  learning  model
such  as  “Vector  space  model”,  “Convolutional  neural  network”,  “Recurrent  neural
network”  and  so  on,  were  used  to  find  out  publications  related  to  the  present  work.
Through the Scopus database, 186,154 papers published within the last five years were
identified. The references and bibliographies of the aforementioned publications were
sifted  and  compiled  in  order  to  locate  more  relevant  papers.  The  following  criteria
were used to thoroughly scan and categorize the abstract, introduction, and conclusion
from selected papers:

(i)  Preliminary consideration was given to only peer-reviewed articles from reputable

publishers and websites

  (ii)  Researchers who are actively engaged in the relevant research field were chosen and

collected

  (iii)  The selected publications were evaluated for their balance between modern studies

and prior research

  (iv)  Referring to websites that employ the aforementioned keywords commercially

(v)  The most recent and cutting-edge algorithms relevant to the present work were

emphasised

  (vi)  Some publications of relevance that were cited in recent studies were rigorously

retrieved as the original source of the studies.

The above criteria assisted in selecting 748 papers that are more relevant. Through-
out  the  entire  review  process  of  available  relevant  papers,  several  questions  were
raised. To answer these questions, some other references were sourced and examined
for  further  clarification  and  improvement.  Papers  for  the  present  study  were  chosen
based on a set of inclusion and exclusion criteria, which are illustrated in Table 1. A
total of 419 articles were finally selected by applying the exclusion criteria. Although
the  exclusion  criteria  appeared  to  provide  a  solid  foundation  to  find  peer-reviewed
and high-quality academic articles, some of the characteristics of the exclusion crite-
ria appeared to be biased and skewed, making it difficult to discover high-quality aca-
demic journals. The authors conducted a test–retest procedure to overcome this issue.

Deep learning modelling techniques: current progress,…1 3

13526

S. F. Ahmed et al.

Table 1   Inclusion and exclusion criteria to select papers for the present review

Inclusion criteria

Exclusion criteria

The publications chosen are all academic and peer-

reviewed

Even if they are academic or peer-reviewed, publica-
tions lacking a robust discussion are not included

The publications should be pertinent to the topic of

Publications that lack information about the afore-

the present study

mentioned keywords are not selected

The papers should be capable of answering the

The results of any literature that showed a high level

research questions

of repetition were filtered out

Any additional information that appears pertinent

Any literature with insufficient references and con-

and valuable is also selected

texts was not considered

3   Deep learning

Deep learning (DL) is considered an evolution of machine learning (ML) that incorpo-
rates  algorithms  to  learn  from  data  to  accomplish  some  tasks  without  being  explicitly
programmed (Lecun et al. 2015). Both ML and DL are a subset of artificial intelligence
(AI). ML powers a wide range of automated functions in various businesses, from data
security  services  hunting  down  malware  to  finance  specialists  looking  for  trade  warn-
ings. It has also a wide variety  of applications in modern  society, such as: developing
intelligent personal assistants for finding helpful information (Dhyani and Kumar 2019),
recommender systems that can suggest relevant items to the users (Zhang et al. 2019),
machine translation to provide the most accurate translation of any text in any language
(Poliak et al. 2018), and predicting the class of object in an image (Chen et al. 2018a;
b).  The  way  machines  can  learn  new  techniques  becomes  interesting  whenever  deep
learning  techniques  are  employed.  The  effectiveness  of  traditional  machine-learning
approaches is comparatively lower than DL techniques, as illustrated in Fig. 1, consid-
ering that they require a large volume of data to provide significant results. For a long
time, designing a feature extractor for machine learning systems demanded hand-crafted
features  to  simplify  the  learning  process.  However,  such  feature  extraction  techniques
need human expertise and significant domain understanding.

Fig. 1   Performance of deep
learning against traditional learn-
ing (Ng 2015)

1 3
13527

Deep learning allows machines to learn from their mistakes and comprehend the world
as  a  hierarchy  of  concepts.  In  this  learning  process,  the  machines  learn  from  data  using
a  general-purpose  learning  algorithm,  thus  needing  less  human  expertise  to  describe  all
the  knowledge  that  the  machine  requires  expressly.  The  models  of  DL  employ  a  layered
network  architecture,  known  as  an  artificial  neural  network  (ANN)  (Schmidhuber  2015),
which  is  modelled  after  the  human  brain’s  analogous  networks.  The  embedding  of  lay-
ers  results  in  a  significantly  more  efficient  learning  experience  than  traditional  machine
learning  models.  The  ability  of  deep  learning  to  achieve  high-level  features  from  a  mas-
sive amount of input data, referred to as feature engineering, distinguishes it from machine
learning.  As  a  result,  deep  learning  is  gaining  popularity  with  innovative  applications  in
natural  language  processing  (NLP),  computer  vision,  and  predictive  modelling  (Ahmad
et al. 2019).

4   Deep learning modelling techniques

Deep  learning  modelling  techniques  enable  computational  models  to  learn  feature
representation  in  data  using  multiple  processing  layers  and  several  levels  of  abstrac-
tion (Lecun et al. 2015). Artificial neural networks (ANNs) provide the foundation of
advanced deep learning models (Schmidhuber 2015) and perform well in a variety of
domains. However, ANNs suffer from certain drawbacks, such as no guaranteed con-
vergence to an optimal solution and being prone to overfitting the training data. There-
fore, researchers have tried to find solutions using deep architecture. The term “deep”
in  “deep  learning”  was  motivated  by  the  number  of  processing  layers  through  which
the data must pass in the network. A deep learning model is made up of multiple layers
that stack up on top of each other (Fig. 2). The first layer (input) consists of units con-
taining  values  fed  to  every  neuron  in  the  first  hidden  layer,  then  the  predicted  results
come out of the model from the output (final) layer. The number of units in this layer
equals  the  number  of  output  classes  desired.  The  hidden  layers  placed  between  the
input  and  output  layers  apply  weights  to  the  inputs  and  pass  them  through  an  activa-
tion function. The activation function is used to help the network add non-linearity and
learn complex relationships in the data. The backpropagation algorithm computes the

Fig. 2   a Conventional neural
network b Deep learning neural
network (Oka et al. 2021)

Deep learning modelling techniques: current progress,…1 313528

S. F. Ahmed et al.

error between the predicted result  and the desired class in the output layer,  then  pro-
ceeds to the hidden layer to reduce the loss by adjusting the weights. This process is
repeated until the output is accurate enough to be useful.

Considering  the  concepts  of  neural  networks  discussed  above,  several  deep  learn-
ing  modelling  techniques  are  built  as  described  in  the  following  subsections.  These
techniques  have  various  applications,  such  as  the  detection,  classification  of  objects
in  images  and  video  data  (Lea  et  al. 2016),  finding  sentiment  and  emotion  from  text
data  (Jin  Wang  et  al.  2016a;  Hassan  et  al.  2018;  Majumder  et  al.  2019),  audio  pro-
cessing applications like speech recognition (Rao et al. 2018a; b), and neural machine
translation (NMT) with translation between different languages (Sutskever et al. 2014).
Developing  a  deep  learning-based  model  in  these  fields  requires  the  pre-processing
of raw data, feature selection, optimal parameter determination, and the evaluation of
classification  accuracy  and  convergence  speed.  This  section  covers  different  types  of
deep  learning  modelling  approaches  and  explains  their  underlying  mathematical  con-
cepts, advancements, latest implementations, and applications in various fields.

4.1   Vector space model

The vector space model (VSM) is an arithmetic model in which texts are represented as
vectors. It has been successfully applied in information filtering, information retrieval,
and  other  areas  (Abualigah  and  Hanandeh,  2015;  Van  Gysel  et  al.  2018;  Mitra  and
Craswell 2017). The vector elements describe the weights or importance of every word
in  a  document.  The  cosine  similarity  technique  can  be  applied  to  find  the  degree  of
similarity  between  two  documents  (Günther  et  al.  2016).  In  the  vector  space  model
shown below, documents are described as a term-document matrix (Shi et al. 2018) or
a  term-frequency  matrix,  where  the  rows  represent  the  documents  and  the  terms  are
defined by the columns. Words, sentences, or phrases are often used as terms, each of
which depends on the application and context. Each cell signifies the term’s weight in
a document, and if a term is present in the document, the cell value will be non-zero.

T1
w11
w12
⋯
w1n

D1
D2
⋯
Dn

T2 … Tt
w21 … wt1
w22 … w11
⋯ ⋯ ⋯
⋯ wtn
w2n

⎡
⎢
⎢
⎢
⎢
⎢
⎣

⎤
⎥
⎥
⎥
⎥
⎥
⎦

Suppose there is a document Dk and a query q . The cosine similarity formula can be

used to find the similarity between Dk and q using the formula:

𝑐𝑜𝑠

Dk, q

=

�

�

N
i=1wi,jwi,q

N
∑
i=1wi,j

2

N
i=1wi,q

2

(1)

�

∑

�

∑

The query and document vectors are not correlated if the cosine value gives zero in
Eq. (1). The vector space model assumes that the terms are independent of each other.
As a result, the model ignores the possibility of semantically related index terms.

1 3
13529

4.1.1   Word embedding

In recent years, research interest in the concept of using a vector representation of words
and  word  embedding  has  increasingly  progressed.  The  latter  has  been  often  utilized  in
advanced natural language processing applications, such as information retrieval, question
answering  (Zhou  et  al.  2016),  and  machine  translation  (Zhang  et  al.  2017a;  b,  c).  Word
embedding  is  a  method  of  generating  vectors  and  mapping  them  to  associated  words.
Tomas Mikolov’s word2vec (Mikolov et al. 2013) models can generate high-dimensional
vector  representations  of  words  when  training  on  a  large  text  dataset  (Demeester  et  al.
2016).  These  vectors  are  capable  of  capturing  syntactic  and  semantic  information.  In  its
simplest form, a word2vec model involves the training of a simple neural network to com-
plete  a  task  and  includes  only  one  hidden  layer  in  the  neural  network,  as  shown  in  Fig..
The goal is to simply learn the hidden layers’ weights, which are used as word vectors in
many applications (Zhang et al. 2015). The size of the input layer depends on the number
of words in the vocabulary for training, where one neuron represents one word. The hidden
layer size is defined by how many dimensions we want to keep in the resulting word vec-
tors. It is suggested that the dimensionality of the vectors be set between 100 and 1000 in
the original model (Demeester et al. 2016). Higher dimensionality provides high quality of
word embedding, while the output layer has the same size as the input layer.

To train the embedded weights, the continuous bag of words (CBOW) and skip-gram
are  two  useful  techniques.  Given  a  target  word,  the  skip-gram  model  attempts  to  predict
alternative context words. Here, input to hidden layer connections remains the same as the
word2vec  fully  connected  network.  However,  a  simple  modification  is  made  in  the  hid-
den  to  output  layer  connection  to  give  space  for  the  selected  number  of  context  words.
Contrariwise, the CBOW model aims to predict target words given a set of context words,
the number of which depends on the setting of the window size. For example, in the sen-
tence, “the quick brown fox jumped over the lazy dog.”, ‘the’ and ‘brown’ might be used
as context words and ‘quick’ as the target word. A tweak to the neural network architecture
is required in this scenario as is a simple modification to adjust the input to hidden layer
connection C times. Here, C is the number of context words. By adding these configura-
tions  to  the  network,  the  hidden  layer’s  output  can  be  found  by  taking  the  mean  of  the
context words. The steps after calculating the hidden layer remain precisely the same. A
text  classification  system  was  proposed  by  Ali  et  al.  (2019)  for  retrieving  transportation
sentiment from social networking and news sites. The authors combined a topic2vec and
word2vec  to  create  a  word  embedding  model  that  describes  the  documents  using  a  low
dimensional vector but keeps the semantic meanings. The model obtains a sentiment clas-
sification accuracy of 93% with transportation datasets, outperforming topic2vec document
representation  approaches.  The  model  treats  the  unimportant  words  as  sentiment  words
that cause decreasing classification performance. However, sophisticated data pre-process-
ing is needed to improve classification accuracy (see Figs. 2, 3).

4.1.2   Sentence embedding

The  sentence  embedding  model  aims  to  produce  a  fixed-length  continuous  vector  repre-
senting  the  entire  input.  A  rough  sense  of  the  relative  locations  of  the  sentence  vectors
in  the  original  vector  space  can  be  obtained  from  the  figure.  Similar  sentences  are  close
together in summary-vector space. Skip-thought is one of the popular sentence embedding

Deep learning modelling techniques: current progress,…1 313530

S. F. Ahmed et al.

Fig. 3   Illustration of word2vec fully connected neural network (Orkphol and Yang 2019)

models that demonstrates significant results in several tasks, including semantic similarity,
paraphrase  detection,  image  annotation  (how  well  the  sentences  describe  an  image),  and
classifications (Kiros et al. 2015).

Vector  representation,  which  is  used  for  words,  phrases,  sentences,  paragraphs,  docu-
ments, or even images, can be generalized as representing “thoughts.” On the other hand,
the skip-thought model abstracts skip-gram architecture to the sentence level (Kiros et al.
2015). The idea behind this model is that the context words embed a word’s meaning. The
model tries to map sentences with common syntactic and semantic information into simi-
lar vectors by reconstructing the neighbouring sentence. The skip-thought model has three
main parts: encoder, previous decoder, and next decoder, as shown in Fig. 4.

In Fig. 4, given a sentence si at index i , the encoder produces a fixed-length representa-
tion zi . It needs to access the word embedding layer (also called the lookup table layer) that
maps each word into a corresponding vector. Inside an encoder, a recurrent neural network
(RNN) with the gated recurrent unit (GRU) or long short-term memory (LSTM) activation
is fed every word sequentially in a sentence. This encoder captures the temporal patterns
of sequential word vectors. The previous decoder takes the embedding zi from the encoder
and “tries” to generate the proceeding sentence si−1 . This decoder uses another recurrent
network  that  generates  the  sentence  sequentially  and  shares  the  same  lookup  table  layer
from the encoder. The next decoder takes the embedding zi from the encoder and “tries” to
generate the subsequent sentence si+1 . This decoder also uses a recurrent network similar to
the previous decoder. The encoder is the end result of the skip-thought model as it contains
syntactic and semantic information.

Fig. 4   Skip-thought model overview (Hassan et al. 2018)

1 3
13531

Due to the vast amount of textual data surfacing online, the demand for text summa-
rization is continuously increasing worldwide. As a result, the necessity of natural lan-
guage processing (NLP) models arises to extract the essential and valuable information
from the long text while maintaining critical information. Mohd et al. (2020) introduced
a text summarizer that obtains the features of a long text document using different tech-
niques, such as Latent Dirichlet Allocation (LDA) and Term Frequency-Inverse Docu-
ment Frequency (TF-IDF), which represents each sentence as a numerical vector. Simi-
lar vectors are aggregated together using a genetic algorithm. Lastly, the LDA technique
was utilized to obtain the center sentence of each cluster to be included in the resulting
summary.  The  macro-average  of  precision  from  the  experimental  results  was  found  to
be 34%, which is higher than the benchmark standard. However, the technique was per-
formed on only one dataset, and thus the precision may not be feasible.

Different  types  of  difficulties,  such  as  combining  syntactic  information  or  identi-
fying  different  labels  for  the  document  classification  task,  are  acknowledged  using
DocBERT.  The  DocBERT  is  a  document  classification  model  based  on  Bidirectional
Encoder  Representations  from  Transformers  (BERT)  (Adhikari  et  al.  2019).  The  gen-
eral idea is to use a fully connected layer to filter the representation obtained from the
common language specification (CLS) token and then employ a SoftMax layer to con-
vert  768-dimensional  encoding  to  class  distribution.  Adhikari  et  al.  (2019)  reported
the  state-of-the-art  results  on  four  popular  datasets,  attempting  to  address  the  BERT
model’s high computational expense and reduce the parameters by 30-fold. The average
document length was found to be less than BERT, while the maximum length was 512.
However,  BERT  can  outperform  non-contextual  embeddings  on  various  tasks,  such  as
the clinical domain. Si et al. (2019) explored the performance of classic word embed-
ding  approaches  (word2vec,  GloVe)  and  contextualized  methods  (BERT)  on  a  clinical
concept extraction task. The output of the BERT model was fed into a bi-LSTM, which
showed  that  contextual  embeddings  play  a  significant  role  in  achieving  better  perfor-
mance (F1-measures of 93.18) on various benchmark tests in the datasets like SemEval.

4.1.3   Graph embedding

Graph  embedding  is  a  technique  for  transforming  a  whole  graph  into  a  single  vector
while preserving the graph’s relevant information. The resulting vectors contain highly
informative features that can be used for the task, such as node classification, ranking,
alignment,  link  prediction,  clustering,  and  visualization.  The  primary  goal  of  graph
embedding  techniques  is  to  reflect  high-dimensional  points  into  a  residual  continuous
vector space with low dimensions (Fig. 5). As a result, it is easy to compute the node
similarity using the dot product or cosine distance formula. Graph analytics is also con-
siderably  faster  and  more  accurate  than  computing  in  the  high-dimensional  complex
graph domain.

Although  matrix-factorization  approaches  have  been  proposed  to  represent  a  node
earlier, they are significantly affected by conventional dimension reduction techniques.
Comparatively,  recent  techniques  focus  on  learning  node  embeddings  using  random
walk characteristics. A graph structure can be translated into a sample collection of lin-
ear sequences using the DeepWalk model (Perozzi et al. 2014), which employs hierar-
chical  SoftMax  techniques  as  the  loss  function.  The  primary  concept  underlying  this
method is to learn embeddings, and therefore (Hamilton et al. 2017):

Deep learning modelling techniques: current progress,…1 313532

S. F. Ahmed et al.

Fig. 5   Graph embedding (Xu 2020)

DEC

zi, zj

≜

�

�

ezT
i zj
vk∈V ezT
i zk

≈ Pg, T(vj

vi)

(2)

�

∑

(

where  Pg, T(vj
;andDEC
zi, zj
decode the graph metrics.

vi)  denotes  the  probability  of  visiting  from  vertex  vi  to  vj  on  a  length-T
  is  a  function  that  takes  the  node  embeddings  zi  and  zj  and  uses  them  to
|
)

A hypergraph embedding method, LBSN2Vec, was developed by Yang et al. (2019) for
location-based social network (LBSN) data that enhances friendship and location predic-
tion task effectiveness. LBSN provides services to the users to publish their location and
location-related  contents  like  photos  or  notes.  Encoding  both  users  and  places  into  low-
dimensional vectors produces hyperedges by sampling friendships and checking-in using
a random walk. The model chooses two nodes from the sample graph and then feeds the
nodes  into  a  model  similar  to  skip-gram  to  generate  low-dimensional  vectors  represent-
ing  the  nodes.  The  authors  revealed  that  the  LBSN2Vec  model  outperforms  the  baseline
graph  embeddings  in  predicting  the  friendship  of  two  individuals  and  location  predic-
tion by 32.95% and 25.32%, respectively. However, the study was limited to random walk
approaches  for  the  location  prediction  task  in  the  hypergraph.  Further  research  is  thus
required  to  take  advantage  of  the  meta-graph  or  hypergraph  for  the  deep  learning-based
recommendation model.

4.2   Convolutional neural network

Convolutional  neural  networks  (CNNs)  are  particularly  useful  to  reduce  the  number  of
parameters in an ANN. This has inspired researchers and practitioners to consider adopt-
ing larger models to accomplish tasks that were previously difficult to handle with regular
ANNs. The CNN model is influenced by an animal’s visual cortex and is intended to learn
low-level to high-level features from the data received gradually. For example, the model
first detects the low-level edge in the first layer in the image classification task and then the
high-level features like shapes and faces in an image (see Fig. 5).

1 3
13533

To  understand  the  architecture  of  CNN,  we  explain  the  essential  CNN  model  compo-
nents. A CNN model is comprised of three primary layers: convolution, pooling, and fully
connected layers. The first two layers generate features from the input, while the third layer,
the  fully  connected  layer,  connects  the  extracted  features  to  the  final  output.  The  convo-
lution  layers  retrieve  the  high-level  characteristics  from  the  data  provided.  The  primary
objective is to compute different feature maps by projecting a tiny array of numbers called
a "kernel" to the input data. The input is also known as a tensor. An element-wise product
between each kernel element and the input tensor is performed at each position of the ten-
sor. Then, the summation of these values is calculated and applied to the associated index
of the output tensor (Fig. 6). Multiple kernels are used to repeat this process to produce an
arbitrary number of feature maps. Each feature map represents distinct input tensors’ char-
acteristics, and each kernel can be considered as a different feature generator. The size and
number of kernels are two primary hyperparameters that describe the convolution opera-
tion. Usually, the kernels’ size is 3 × 3, but it can also be 5 × 5 or 7 × 7. The number of ker-
nels is chosen arbitrarily depending on the depth of the output feature maps. Mathemati-
cally, convolution operation can be defined by the following equation (Khan et al. 2020):

f k
l (p, q) =

ic(x, y) ⊙ ek

l (u, v)

c
∑

x,y
∑

(3)

where  f k
l  is the output feature map of the k-th convolution operation of the l-th layer. This
can  be  computed  as  Fk
l (p, q), … f k
l (P, Q)] ,  where  ic  is  the  input  tensor
and ic(x, y) is an element of that tensor. These values will be element-wise multiplied by
ek
l (u, v) , the k-th convolutional kernel of the l-th layer.

l (1, 1), … f k

l = [f k

CNN introduces non-linearity to the network by applying a non-linear activation func-
tion.  Previously,  the  popular  choice  was  non-linear  activation  functions,  including  sig-
moid  or  tangent  functions  (LeCun  et  al.  2012).  However,  to  resolve  the  vanishing  gradi-
ent problem (Nwankpa et al. 2018) of the sigmoid and tangent function, Rectified Linear
Unit  (ReLU)  and  its  variants,  such  as  leaky  ReLU  and  Parametric  Rectified  Linear  Unit
(PReLU), are used. One of the recently proposed activation functions named Mish outper-
forms ReLU and other typical activation functions in many deep networks across bench-
mark datasets (Misra 2019). The activation function of the convolutional feature map can
be computed as:

Fig. 6   Convolution operation

Deep learning modelling techniques: current progress,…1 313534

ak
l = g(Fk
l )

S. F. Ahmed et al.

(4)

where Fk
and ak

l  is the output of a convolutional operation that goes to an activation function g();

l  is the non-linear output of the k-th input feature map in the l-th layer.

The  extracted  features  from  the  convolutional  and  pooling  layers  are  flattened  to
a  one-dimensional  array  of  numbers.  Those  features  are  then  fed  into  the  traditional
neural  network,  where  each  input  is  connected  to  its  subsequent  layer  neurons  by  a
learnable weight. The main drawback of a fully CNN is that it requires training many
parameters, which contributes to its high computational expense and possible overfit-
ting. The dropout technique is used to overcome such difficulties, in which a few nodes
and  connections  are  removed  (Goodfellow  et  al.  2013).  The  output  layer  is  the  final
layer of CNNs, where softmax function is widely used to provide probability distribu-
tion (Russakovsky et al. 2015). Another classifier, the support vector machine (SVM),
can also classify data (Tang 2013).

Parallel computing has made CNNs more efficient than humans in recognizing vis-
ual patterns, making them a desirable alternative for wide-area monitoring because of
their advantages over humans. Mukherjee et al. (2020) proposed a CNN-based genera-
tive model, namely “GenInSAR”, for combined coherence estimation and phase filter-
ing which directly learns interferometric synthetic aperture radar (InSAR) data distri-
bution.  InSAR  is  a  developing  and  extremely  successful  remote  sensing  method  for
monitoring  a  variety  of  geophysical  parameters,  including  surface  deformation.  The
unsupervised training on simulated and satellite InSAR images of the proposed model
(GenInSAR)  outperformed  the  other  comparable  methods  (CNN-InSAR(as-is),  CNN-
InSAR(retrained),  NLSAR,  NLInSAR,  Goldstein,  Boxcar)  in  reducing  the  total  resi-
due (by more than 16.5% on average), with fewer over-smoothing/artifacts surrounding
branch  cuttings.  Compared  to  the  related  methods,  the  phase  cosine  error,  coherence
and phase root-mean-square-error of GenInSAR were improved by 0.05, 0.07 and 0.54,
respectively. As a result, the InSAR machine learning can be improved by GenInSAR’s
ability to produce new interferograms.

4.2.1   CNN‑LSTM

Long short-term memory (LSTM) can learn long-term relationships in data. However,
spatial data like images are challenging to model with the standard LSTM. The convo-
lutional neural network combined with long short-term memory (CNN-LSTM) is based
on  an  LSTM  network  that  is  primarily  designed  for  sequence  prediction  tasks  where
the  input  is  spatial  data,  such  as  images,  videos,  or  temporal  structure  of  words  in  a
sentence, paragraph, or document. The model shown in Fig. 7 illustrates the combined
regional CNN and LSTM to identify the sentiment of text (Wang et al. 2016a), which
considers an individual sentence as a region and long-distance relationship of sentences
in the prediction task.

The  main  architecture  of  the  CNN-LSTM  model  consists  of  the  input  layer,  convolu-
tion layer, pooling layer, sequential layer (LSTM hidden layer), and fully connected layer.
The first three layers are the CNN layers. The CNN layer’s output data is transferred to the
LSTM layer. Following temporal modelling, the data from the LSTM layers are sent to a
fully connected layer. These layers are well-suited to produce higher-order features that are

1 3
13535

Fig. 7   Regional CNN-LSTM model for sentiment analysis (Jin Wang et al. 2016a)

easy to distinguish within distinct categories. The CNN model is used for feature extrac-
tion, while the LSTM model is employed for data interpretation over time.

4.2.2   Temporal convolutional network (TCN)

The  novel  work  on  the  temporal  convolutional  networks  (TCNs)  was  first  proposed
by  Lea  et  al.  (2016)  for  video-based  action  segmentation.  This  approach  involves  two
phases:  (i)  CNN  computes  the  low-level  features  that  encapsulate  spatial–temporal
information,  and  (ii)  RNN  feeds  the  low-level  features  into  a  classifier  to  extract  the
high-level temporal information. Although TCN demands the integration of two differ-
ent  models,  it  offers  a  unified  technique  to  capture  all  two  layers  of  information  in  a
hierarchical  manner.  The  original  TCN  model  possesses  a  convolutional  encoder  and
decoder architecture. The model captures a set of video features as the input and then
extracts a D-dimensional feature vector for each video frame. If a video has T frames,
the input X appends all the frame-wise features in a way that X ∈ ℝT×D
 . Similar to other
CNN architectures, the networks apply some filters followed by non-linear activation of
the input to extract features. The convolution consists of l layers, where the collection
of filters in each layer is defined as {W (i)}Fl
i=1 for W (i) ∈ ℝd×Fl−1 . Here, Fl is the number of
convolution filters in the l layer with a temporal window d. If Xl−1 is an output from the
previous  layer,  the  l-th  layer  output,  Xl ,  can  be  calculated  as  follows  (Kim  and  Reiter
2017):

Xl = f (W ∗ Xl−1)

(5)

where  f  denotes any non-linear activations functions, e.g., ReLu.

Convolutional  neural  networks  and  their  variants  are  used  in  various  applica-
tions, such as the detection, classification of objects in images and video data, finding

Deep learning modelling techniques: current progress,…1 313536

S. F. Ahmed et al.

sentiment and emotions in natural language data, and audio processing applications like
voice  recognition.  A  CNN-based  architecture  named  LeafNet  was  developed  by  Barré
et  al.  (2017)  to  identify  plant  species  from  the  leaf  images.  The  authors  experimented
with  their  model  on  three  publicly  available  state-of-the-art  datasets  of  leaf  images:
LeafSnap,  Foliage,  and  Flavia.  The  previous  studies  on  these  datasets  were  based  on
the  hand-crafted  feature  extraction  technique.  After  data  augmentation,  approximately
270,000  leaf  images  were  used  on  a  17-layer  CNN  to  train  the  LeafNet  model  with
image sizes of 256 × 256 pixels. Improved accuracies (by 0.8–13.3%) of 86.3%, 95.8%,
and 97.9% were found on the LeafSnap, Foliage, and Flavia datasets, respectively, com-
pared  to  previous  studies.  However,  this  method  is  comparatively  slow  (training  takes
about 32 h) and lacks context due to the small, cropped window sizes.

In  another  work,  a  region-based  convolutional  neural  network  (R-CNN)  has  been
applied in the computer vision field for the object detection task. Li et al. (2019a, b, c, d)
proposed the stereo R-CNN method that can perform three-dimensional (3D) object detec-
tion in autonomous vehicle navigation. The method identifies and integrates objects in both
the  left  and  right  images  simultaneously  and  uses  a  region-based  object  detection  align-
ment  to  retrieve  the  correct  3D  bounding  box.  The  stereo  R-CNN  captures  input  images
with a resolution of 600 × 2000 and takes advantage of ImageNet’s pre-trained ResNet-101.
The model was evaluated on the KITTI object detection benchmark. The proposed method
outperformed  a  previous  study  (Chen  et  al.  2018a,  b)  for  3D  object  proposals  by  over
25–30%.  Due  to  the  absence  of  precise  depth  information,  the  model  can  only  produce
shallow 3D detection results. Variations in appearance can also have a significant impact.

Chen et al. (2018a, b) introduced an unsupervised domain adaptation model for cross-
domain object detection based on the faster R-CNN model (Zhang et al. 2016a, b). They
employed two domain classifiers: one for high-level features at the global image scale and
another for features clipped by the region proposal network at the instance (object) scale.
The model was validated for different domain shift datasets. Via experiments, the authors
found that the domain adaptive faster R-CNN model outperforms the faster R-CNN model
by over 8.8%. This improvement was found consistent across the categories, thus indicat-
ing that the suggested method can minimize domain mismatch between object categories.
However, the model was not trained to recognize traffic in darkness and is only adaptable
to specific scenarios.

A dynamic CNN-based system was proposed by Chu et al. (2017) for tracking objects in
videos. Using shared CNN features and Region of Interest Pooling, the model takes advan-
tage  of  single  object  trackers.  The  experimental  results  showed  that  the  proposed  online
multi-object tracking algorithm outperforms Markov decision processes by 4%. Although
the model performed well in tracking objects, it is unsuitable for applications with limited
resources. Also, the model may consume a lot of memory and time as it constructs a net-
work for individual objects and performs online learning. Since CNN works well for both
image classification and natural language processing tasks, CNN-based text classification
models  are  gaining  popularity.  For  instance,  multi-layer  CNN  produces  optimal  features
during the training process to reflect the semantics of the sentence being evaluated. These
semantic constructs can be applied to a variety of applications, including text classification,
text summarization, and information retrieval.

A  CNN-based  method  was  suggested  by  Hughes  et  al.  (2017)  for  classifying  clinical
texts  into  one  of  26  categories,  such  as  “Brain”  or  “Cancer.”  The  model  classifies  texts
by  converting  each  document  into  a  sentence-level  representation.  The  authors  used
two  stacked  convolutional  layers  followed  by  a  pooling  layer.  The  experimental  analy-
sis revealed that the model improves the word embedding-based methods by accuracy of

1 3
13537

around  15%.  However,  the  model  was  trained  with  a  relatively  small  dataset  (4000  sen-
tences). To improve the model performance, domain adaptation techniques can be used to
transfer knowledge from another domain to the medical field (Sun et al. 2016).

CNN-based  models  have  also  been  successfully  applied  in  the  sentiment  analysis  of
Twitter data. To predict user behavior via sentiment analysis, Liao et al. (2017) examined
different deep learning techniques. They employed CNN and word embedding techniques
to  get  better  results  than  traditional  learning  algorithms,  such  as  SVM  and  Naive  Bayes
classifiers.  Their  approach  interpreted  the  sentence  matrix  to  be  the  same  as  an  image
matrix. A linear kernel was convoluted to that sentence matrix, and a max-pooling func-
tion  was  applied  to  each  feature  to  find  the  fixed-length  representation  of  the  sentence.
The model was assessed on several benchmark datasets, including MR and STS Gold. The
maximum development accuracy was found to be up to 74.5%. To improve the model accu-
racy, a multilayer CNN may be used instead of a simple CNN (single channel) for sentence
classification.

CNN-based  approaches  are  also  becoming  more  prominent  in  cosmology  because  of
their noticeable performance. DeepSphere is a graph-based CNN that works on cosmologi-
cal data analysis (Perraudin et al. 2019) to predict a class from a map and classify pixels.
The data often come as spherical maps represented as a graph in the network so that the
model can perform the convolution and pooling operations. In the latter work, DeepSphere
outperformed  all  the  baselines  by  10%  in  terms  of  classification  accuracy.  However,  the
model was applied to only the classification problem performed on scalar fields. To further
demonstrate the performance of DeepSphere, it would be useful to make comparisons to
various spherical CNN implementations with different sampling techniques.

4.3   Recurrent neural network (RNN)

Recurrent  neural  networks  (RNNs)  have  recently  demonstrated  promising  performance
on various natural language processing tasks and have produced superior results on mul-
tiple  tasks,  such  as  sentiment  classification  (Wang  et  al.  2016c),  image  captioning  (Yao
et al. 2017), and language translation (Li et al. 2017a; b). There are numerous situations in
which data sequences describe the case itself. For example, in a language modelling task,
a  sequence  of  words  defines  their  meaning.  If  the  sequences  are  disturbed,  the  informa-
tion makes no sense. In a traditional neural network, the assumption is that there has no
dependency between the input and output. Considering this case, a network connecting to
prior information is needed to fully comprehend the data. As a response, RNNs are useful,
which are termed from the fact that they execute the same computation for each sequence
element.  The  output  in  every  state  is  dependent  on  the  previous  calculation.  RNNs  keep
a  "memory"  that  captures  the  information  about  what  has  been  computed  so  far  (Tomaš
Mikolov et al. 2010, 2011). An RNN can be unfolded into an entire network, as illustrated
in Fig. 8.

The computation flows running in an RNN for the text processing task are as follows:

•  xt denotes the present input at time step t, where input is given as a one-hot encoded
t

vector. For example, x1 = [ 1 0 0 0 0 ]

 is the initial word in a sentence.

•  st signifies the hidden state at time step t, captures the “memory of the network, and is

computed using the previous hidden state and the present step’s input:

Deep learning modelling techniques: current progress,…1 313538

S. F. Ahmed et al.

Fig. 8   Unfolded recurrent neural network (Lecun et al. 2015)

st = f (Uxt + Wst−1)

(6)
where  f  is an element-wise non-linear function, such as tanh or ReLU . In the case of calcu-
lating the first hidden state, st−1 is typically set to all zeros. W and U are the weight matrix
of the hidden state and input, respectively.

•  ot represents the output at time step t. For instance, to predict the next word in a sen-

tence, the probability can be calculated by applying the softmax function.

ot = softmax(Vst)

(7)

An RNN can, in theory, summarize all historical information up to time step st . Unfor-
tunately, the accuracy of RNNs is significantly inhibited by the vanishing gradient problem
(Bengio  et  al.  1994).  To  address  this  problem,  gated  recurrent  units  and  long  short-term
memory have become more powerful models and gained acceptance in recent years as the
best strategy to implement recurrent neural networks.

Fig. 9   A schematic for a long short-term memory cell (Jenkins et al. 2018)

1 3
13539

4.3.1   Long short‑term memory (LSTM)

A  long  short-term  memory  (LSTM)  network  is  comprised  of  different  memory  blocks
referred  to  as  cells.  A  cell  is  constructed  by  gates  that  control  the  flow  of  information:
forget, input, and output gates (Fig. 9). A forget gate removes information from a cell con-
figuration,  and  the  input  gate  updates  the  newly  entered  data  to  the  cell.  The  input  gate
determines the rate at which new data enter the cell, whereas the output gate limits the data
in the cell and computes the output activation of the LSTM unit.

The gating mechanism in a LSTM can be defined by the following equations:

it = 𝜎(W ixt + Uiht−1 + bi)

ft = 𝜎(W f xt + Uf ht−1 + bf )

ot = 𝜎(W oxt + Uoht−1 + bo)

̃Ct = tanh(W gxt + Ught−1 + bg)

Ct = ft ⊗ Ct−1 + it ⊗ �Ct

ht = ot ⊗ tanh(ct)

where it is input gate;  ft denotes forget gate; ot is output gate at a time step t;
memory cell vector; and W and U are parameter matrices.

4.3.2   Bidirectional long‑short time memory (BiLSTM)

(8)

(9)

(10)

(11)

(12)

(13)
̃Ct is a new

Regular recurrent neural networks with LSTM cells can be extended to bidirectional recur-
rent neural networks in which the data is passed through two LSTMs (Graves et al. 2013;
Graves and Schmidhuber 2005). One forward LSTM offers the input sequence in the cor-
rect  order  (forward  layer),  and  another  backward  LSTM  provides  the  input  sequence  in
reverse order (backward layer). This technique improves the model’s accuracy by captur-
ing the long-term dependencies of the input sequence in both directions. In the BiLSTM,
the  forward  layer  computation  is  identical  to  those  in  the  regular  LSTM  that  computes
��⃗ht, ��⃗ct ) from t = 1toT . On the other hand, the backward layer computes the
the sequences (
sequences

⃖���ht,⃖��ct from t = Tto1 as described below:

⃖�it = 𝜎(W ixt + Uiht+1 + bi)

⃖�ft = 𝜎(W f xt + Uf ht+1 + bf )

⃖��ot = 𝜎(W oxt + Uoht+1 + bo)

⃖����Ct = tanh(W gxt + Ught+1 + bg)

(14)

(15)

(16)

(17)

Deep learning modelling techniques: current progress,…1 313540

S. F. Ahmed et al.

⃖���Ct = ⃖�ft ⊗ ⃖������Ct+1 + ⃖�it ⊗

⃖����Ct

⃖��ht = ⃖��ot ⊗ tanh(⃖��ct)

(18)

(19)

In  a  study  conducted  by  Siami-Namini,  Tavakoli,  and  Namin  (2019),  LSTM  and  BiL-
STM were compared in terms of time series data modelling. The prediction accuracy of the
BiLSTM-based  model  was  37.78%  higher  than  that  of  standard  LSTM-based  models  after
training with both directions of input data. However, BiLSTM-based models achieved slower
performance than the LSTM-based models. Another study (Brahma 2018) introduced a new
model suffix bidirectional LSTM (SuBiLSTM) that improved BiLSTM for sentiment classifi-
cation and question classification tasks (see Figs. 7, 8, 9).

4.3.3   Gated recurrent unit (GRU)

The  architectures  of  a  gated  recurrent  unit  (GRU)  and  long  short-term  memory  (LSTM)
are closely related, since both are crafted similarly and, in some situations, generate equally
outstanding results (Murali and Swapna 2019). The GRU cell is comprised of two gates: an
update gate z and a reset gate r. It addresses the vanishing gradient problem of a regular RNN
by using the update gate to determine how much historical memory (from earlier time steps)
should be maintained and proceed to the future and the reset gate to pair the new input with
the prior memory, as shown in Fig. 10.

The gating mechanism in GRU is expressed by the following equations:

z = 𝜎(Wzht−1 + Uzxt)

r = 𝜎(Wrht−1 + Urxt)

c = 𝑡𝑎𝑛h

Wc(ht−1 ⊗ r

+ Ucxt)

(

)

(20)

(21)

(22)

Fig. 10   Gated recurrent unit cell (Zhao et al. 2019)

1 3
13541

(23)
where xt is the input vector; ht is output vector; W and U are parameter matrices; 𝜎 is the
sigmoid function; and ⊗ denotes the Hadamard product (entry-wise product).

ht = (z ⊗ c) ⊗ ((1 − z) ⊗ ht−1)

Due  to  their  versatility  in  various  applications,  RNNs  have  been  successfully  used  in
multiple tasks, including language modelling, speech-to-text processing, caption generator,
machine translation, and other fields. RNN has also been applied in the sentiment analysis
task to produce effective outcomes. For instance, Basiri et al. (2021) proposed a model to
determine the sentiment from long reviews and short tweet text. In the model, the attention
mechanism in RNNs is used to pay more attention to certain factors by assigning different
weights  when  processing  the  data.  The  linguistic  structures  become  more  descriptive  by
applying the attention mechanism. Two bidirectional LSTM and GRU are also employed
to generate the input text’s previous and next contexts feature representation. The proposed
model improved the accuracy from 1.85% to 3.63% for five long review datasets and from
0.25% to 0.54% for three short tweet datasets. While the study emphasized sentiment clas-
sification at the document level, there is potential to investigate sentiment classification at
the sentence and aspect levels.

Another RNN model based on dialogue was built with an attention mechanism for emo-
tion detection in textual conversations with six emotion labels (Majumder et al. 2019). The
model  has  several  variants,  including  DialogueRNN + Att  and  BiDialgouRNN,  and  con-
siders  both  context  and  speaker  information.  The  network  employs  three  GRUs  to  track
individual speaker states, global context from the preceding utterances, and the emotional
state through the conversations. The data are provided and fed into the GRU for emotion
representation,  depending  on  the  context.  Although  the  DialogueRNN  model  achieved  a
better f1-score of 6.62% on several experiments, which is above the baselines (Majumder
et al. 2019), it is time-consuming for training and not parameter-efficient for global or local
contexts.

In  RNN-based  neural  machine  translation  (NMT),  sequence-to-sequence  (seq2seq)
architectures  are  used  to  deal  with  translation  between  languages.  These  seq2seq  archi-
tectures apply two RNNs, namely an encoder and decoder. A study (Camgoz et al. 2018)
utilized the standard seq2seq model to recognize sign language gestures from a video of
someone performing continuous signs. In the study, the CNN was trained on the sentence
level annotation to extract features from the video before translating it to text. These fea-
tures were fed to the seq2seq model. The model scored 18.13 on the BLEU-4 matric (Pap-
ineni et al. 2001) and 43.80 on the ROUGE matric (Lin 2004). The model assumed that
the  CNN  could  learn  good  feature  representation,  but  this  hypothesis’s  validity  was  not
evaluated.

To  model  long  texts  for  generating  semantic  relations  between  sentences,  researchers
face challenges in sentiment analysis. Rao et al. (2018a, b) handled the problem by propos-
ing the State Refinement-LSTM (SR-LSTM) and SSR-LSTM models based on deep RNN.
The models have two hidden layers: the first one uses LSTM to represent the semantic rela-
tionship of sentences, and the second one encodes those sentence relationships at the docu-
ment level. The SR-LSTM model outperformed other models by obtaining an accuracy of
44% and 63.9% on the IMDB and yelp2015 datasets, respectively, while the SSR-LSTM
model achieved an accuracy of 44.3% and 63.8% on the same datasets. However, the mod-
els considered only the sequential order of the documents. In future works, it may possible
to represent the documents using tree-structured LSTM.

RNNs have also been successfully applied in intelligent health care systems. For example,
Uddin et al. (2020) presented a multi-sensors data fusion network that relies on a recurrent

Deep learning modelling techniques: current progress,…1 313542

S. F. Ahmed et al.

neural network to recognize human activities and behavior. They extracted features from mul-
tiple  body  sensors  and  enhanced  the  features  using  Kernel  Principal  Component  Analysis
(KPCA)  techniques.  Then,  human  activities  were  recognized  by  training  a  deep  RNN.  The
proposed method was assessed on three publicly available datasets. The average performance
was found to be 99% using precision, recall, and F1-score matrices. It is possible to extend the
work by developing a real-time human behavior tracking system with considering more com-
plex human activities.

The RNN-LSTM approach for time series modelling has recently attracted much interest.
The  applicability  of  RNN-LSTM  was  analyzed  by  Sahoo  et  al.  (2019)  for  predicting  daily
flows during the low-flow periods. The model effectively used the time series data by taking
advantage of the LSTM memory cell to learn features from both the current and past values
of  an  observable  object.  The  model’s  performance  (root-mean-square  error  RMSE = 0.487)
on  hydrological  data  outperformed  the  traditional  RNN  model  (RMSE = 0.516)  and  naive
method (RMSE = 0.793). Nevertheless, multiple hidden LSTM layers can be used to enhance
the performance of the model. Experts are also attempting to use deep learning approaches
in  typhoon  prediction  as  deep  learning  techniques  become  more  sophisticated.  Alemany
et al. (2019) proposed a fully connected RNN to predict hurricane trajectories from historical
cyclone data that could learn from all types of hurricanes. The model produced better predic-
tion accuracy than the previous models. For example, the mean absolute error (0.0842) of the
RNN model was better than that of the previous sparse RNN average model (0.4612) to track
Hurricane Sandy in 2012. The model may take advantage of converting the grid locations to
latitude–longitude coordinates to reduce the conversion error.

4.3.4   Deep echo state network

The deep echo state network (DeepESN) is a recently proposed technique to enhance the effi-
ciency of a general echo state network (ESN) in several domains. ESN is a reservoir comput-
ing  model  in  which  the  reservoir  computing  shows  efficiency  to  train  RNNs  by  preserving
memory using its recurrent nature. A dynamic reservoir is incorporated in ESN, presenting a
sparsely linked recurrent network of neurons that differs from a traditional multilayered neu-
ral  network.  The  reservoir  is  the  network’s  only  hidden  layer,  and  its  input  connections  are
assigned at random and cannot be trained. On the other hand, the weights between the reser-
voir and output are the only ones that can be trained. The system learns the weights by linear
regression rather than backpropagation. DeepESN is simply the ESN model’s application of
the deep learning architecture.

The  DeepESN  output  is  produced  using  a  linear  structure  of  the  recurrent  units  across
all recurrent layers. After initialization, the DeepESN reservoir component is left untrained.
Therefore, the usual ESN technique is subject to stability limitations. Such limits are stated
in DeepESN by the criteria for the ESN of the deep reservoir computing network. In the deep
echo state network, input is processed by the first layer, and the previous layers’ outputs pro-
cess the successive layers’ inputs. Therefore, the state transition function of a DeepESN can be
presented by the following equation (Lukoševičius and Jaeger 2009):

x(l)(t) =

1 − a(l)

x(l)(t − 1) + a(l)tanh(W (l)

in i(l)(t) + 𝜃(l) + ̂W (l)x(l)(t − 1))

(24)

(

)
where  l represents the number of layers; W (l)
 denotes
̂W (l)
 expresses the recurrent weight matrix for layer l . Here, i(l)(t)
bias weight vector; and
signifies the input for the l th layer of the network at time t . The output of the model can be
expressed by the following equation:

in  refers to the input matrix for  l ; 𝜃(l)

1 3
T
y(t) = Wout[x(1)(t)x(2)(t) … x(Nl)]

+ 𝜃out

13543

(25)

where Wout is the weight matrix between the reservoir and output y(t).

Based on the DeepESN, a novel technique was developed by Gallicchio et al. (2018a)
for  diagnosing  Parkinson’s  disease.  This  is  a  significant  initial  work  in  the  DeepESN
domain that shows the superiority of DeepESN over the shallow echo state network model.
The proposed technique identified Parkinson’s disease by using the time series data gath-
ered from a tablet device while subjects performed sketching spiral tests with a pen. The
acquired data contain x and y components of the pen, pen pressure, and grip angle. These
signals were used to feed the model with no feature extraction and data pre-processing. The
proposed model was evaluated on a public spiral test dataset and showed to perform better
than the shallow ESN and other state-of-the-art methods.

Gallicchio  et  al.  (2018b)  proposed  a  DeepESN  technique  based  on  additive  decom-
position  for  predicting  the  time  series  data  where  the  additive  decomposition  technique
was used as a pre-processing step to the model. Data are split into three parts by additive
decomposition (trend, seasonality, and residual) and then fed to the DeepESN. The perfor-
mance  of  the  additive  decomposition-DeepESN  was  compared  with  LSTM,  GRU,  ESN,
and  DeepESN  algorithms  on  six  different  datasets.  The  proposed  model  demonstrated
significant performance for large, multidimensional data. Although ESN was found to be
computationally efficient, it delivered a poor performance in prediction. LSTM and GRU
required five times more computational time than DeepESN and additive decomposition-
DeepESN. The additive decomposition-DeepESN model showed a low standard deviation,
proving its stability, whereas other reservoir algorithms were unstable, i.e., with a higher
standard deviation. Thus, the additive decomposition technique has the ability to improve
the stability and performance of the DeepESN.

4.3.5   Elman recurrent neural network

The  difference  between  the  Elman  recurrent  neural  network  (ERNN)  (Elman  1990)  and
other recurrent networks is that the hidden layer’s output is used as input for the context
layer in the former. The architecture of ERNN consists of four layers: input layer, recurrent
layer, hidden, and output layer. Each layer has one or multiple neurons that use a non-linear
function of their weighted sum of inputs to transfer information from one layer to the next.
Each  hidden  neuron  is  linked  to  a  neuron  of  the  single  recurrent  layer  with  the  constant
weight of one. As a result, the recurrent layer contains a copy of the hidden layer’s state
one instant ago. The benefit of using ERNN is that it emphasizes the relationship between
future and previous values even when it is difficult to learn from them. The ERNN can be
described by the following equations (Achanta and Gangashetty 2017):

ht = f

Wixt + Wht−1 + bh

(26)

(
yt = g(Uht + bo)

)

(27)
where Wi signifies hidden weight’s input; W denotes the recurrent weight matrix of the hid-
den layer; bh represents the hidden bias; U refers to the hidden output matrix; bo is the Bias
Vector of the output layer; and  f  and g are the non-linear functions of hidden and output
layers, respectively. Input is represented by xt , the state of ht and yt refer to the outputs at
time t.

Deep learning modelling techniques: current progress,…1 313544

S. F. Ahmed et al.

An ERNN model with a stochastic time effective function (ST-ERNN) was developed
by Jie Wang et al. (2016b) to forecast stock indices. The architecture is built by combin-
ing  ERNN,  multilayer  perceptron,  and  stochastic-time-effective  function,  where  a  sto-
chastic  process  is  used  to  describe  the  level  of  historical  data  impact  in  the  market.  The
time-strength function includes a drift function and Brownian motion to model the appear-
ance  of  random  changes  while  keeping  the  primary  trend.  The  proposed  neural  network
performs  better  than  other  existing  neural  networks  in  financial  time  series  forecasting.
Considering the rapid changes in the stock market data that make the field non-linear and
nonstationary,  predicting  this  kind  of  data  is  very  challenging.  Nevertheless,  ST-ERNN
showed a significant performance that can be crucial for future experiments in this domain.
Krichene et al. (2017) applied ERNN for forecasting Mackey Glass time-series elements.
The performance of ERNN was evaluated via comparison with two other existing models
(Al-Jumeily  et  al.  2014;  Park  2010)  using  the  same  dataset,  where  ERNN  showed  better
performance. It is worth noting that optimal performance was achieved when the weights
of the context units were randomly initialized.

4.4   Recursive neural network

A recursive neural network (RvNN) is a nonlinear model that can function on structured
inputs and is applicable to parse trees in natural language processing (NLP), image anal-
ysis,  protein  topologies,  among  other  applications  in  structured  domains.  For  instance,
RvNN performs extremely well in the NLP tasks. Despite their deep structure, the archi-
tecture of RvNN lacks the capacity for hierarchical representation (Irsoy and Cardie 2014)
and contains complex informative processing models. Because they acquire high-level rep-
resentations  from  explicit  inputs,  recursive  networks  are  effective  in  many  deep  learning
tasks where the input is a structure. RvNNs are normally defined on a directed positional
acyclic graph (Micheli et al. 2007). The form of RvNN is shown in Fig. 11, referring to the
parse tree on the left side (Ma et al. 2018). If the parent node’s feature vector is  p, and c1
and c2 are its children, then

p = f (w.[c1;c2] + b)

(28)

Fig. 11   The tree and its associated RvNN architecture (Ma et al. 2018). In the figure, S represents a sen-
tence, NP is a noun phrase, VP is a verb phrase, D denotes determiner, N signifies noun, and V is a verb

1 3
13545

where  f (.) is the activation function. The computation is recursively done for all nodes, and
the hidden vectors of nodes’ can then be used for different classification tasks.

Tree-structured recursive neural networks (RvNNs) were used to perform rumor detec-
tion on Twitter by Jing Ma, Gao, and Wong (2018). This study constructed two recursive
networks on top-down and bottom-up tree-structured neural networks. Rather than a sen-
tence’s parse tree, the model’s input is a propagation tree rooted from a source post, and
each node is a sensitive post rather than individual words. Recursive feature learning can
capture the content semanticization of posts along with the tree structure and the receptive
relationship between them. The basic concept of the bottom-up model is to create a feature
vector by traversing each node recursively from the leaves to the root on the top. On the
other hand, the concept of the top-down approach is to create an enhanced feature vector
for  each  post,  considering  its  propagation  direction,  in  which  rumor  indicators  are  com-
bined along the path of propagation. However, for the non-rumor class, the proposed mod-
els did not perform well. Yet, they could add other types of data into the structured neural
models, such as user properties, to boost representation learning even further.

Biancofiore et al. (2017) analyzed atmospheric particulate matter (PM) and forecasted
daily  averaged  concentrations  of  PM10  and  PM2.5  up  to  1–3  days.  Particulate  matter  is
a significant pollutant that affects human health, thus studies on reducing PM are critical.
The latter researchers implemented a multiple linear regression model, feed-forward neu-
ral network, and neural networks with the recursive structure and found that the recursive
neural network model outperforms the other methods. The total number of input variables
and neurons in the second layer in the model determines how many neurons are in the first
layer. The network’s output, the predicted particulate matter concentration, is represented
by a single neuron in the final layer. In the latter work, the RvNN model correctly predicted
95% of the days, but this decreased to 57% when considering only the days where the lim-
its were exceeded. In addition, the false-positive rate was 30% in this study.

Lim  and  Kang  (2018)  extracted  the  relation  between  chemical  compounds  and  genes.
They  experimented  with  three  methods,  a  tree-LSTM  model  with  a  position  feature  and
a  subtree  containment  feature,  and  implemented  an  ensemble  process.  The  authors  also
implemented  a  stack  augmented  parser  interpreter  neural  network  (SPNN).  The  study
revealed  that  the  SPNN  with  ensemble  technique  outperformed  the  tree-LSTM  with
ensemble  technique,  which  means  that  the  extra  tracking  layer  is  beneficial.  However,
the  proposed  model  is  unable  to  comprehend  the  structure  of  a  sentence.  More  training
instances are needed to resolve this error. Also, coordination was not detected, whereby a
comma, parenthesis, or special term like “and” or “or” is used to express coordination rela-
tions. This form of error may be avoided with the use of a separate module that looks for
terms of equal emphasis.

4.5   Neural tensor network

In  several  natural  language  processing  tasks,  neural  tensor  networks  (NTNs)  have  been
successful.  However,  they  need  to  estimate  a  considerable  number  of  parameters,  often
resulting  in  overfitting  (Yang  et  al.  2015)  and  excessive  training  times.  An  NTN  model
constructed by Socher, Chen, et al. (2013) implements a 3D tensor for combining two input
vectors as bellow:

f (xT

1 W [1∶k]x2 + V

x1
x2

]

[

+ b)

(29)

Deep learning modelling techniques: current progress,…1 313546

S. F. Ahmed et al.

where W [1∶k] ∈ ℝnxnxk
 is the tensor ( W is a slice matrix); V ∈ ℝk×2n
 is the linear mapping to
combine input vectors x1 and x2; b refers to a bias term;  f  is the non-linear activation func-
tion; and xT

1 W [1∶k]x2 is an array of k bilinear products.

In contrast to the regular neural network model, NTN can connect two input vectors
with a tensor directly. Although the NTN model is efficient, it takes considerable time
to compute. Several studies were done to reduce the time complexity using parameter
reduction  techniques.  For  instance,  Ishihara  et  al.  (2018)  introduced  two-parameter
reduction techniques based on the matrix decomposition method, while Y. Zhao, Liu,
and  Sun  (2015)  and  P.  Liu,  Qiu,  and  Huang  (2015)  proposed  simple  matrix  decom-
position  techniques  for  reducing  parameters.  A  neural  tensor  model  named  the  con-
volutional NTN converts all word tokens into vectors with the help of a lookup layer,
encode questions and answers with coevolutionary, pooling layers to fixed-length vec-
tors, and finally modelling their interactions with a tensor layer. Therefore, in a seman-
tic vector space, this model will group related questions and answers to avoid the prob-
lem of lexical distances.

Qiu  and  Huang  (2015)  proposed  a  convolutional  NTN  for  community-based  ques-
tion answering, integrating sentence modelling and semantic matching into one model.
They  implemented  contrastive  max-margin  criterion  to  train  the  model.  This  study
evaluated two different datasets for English and Chinese languages and found that the
proposed  model  can  handle  more  complex  interactions  with  tensor  layers  than  exist-
ing models. However, texts were converted into fixed-length vectors with the proposed
convolutional layer, saving the essential information lost in bag-of-words. The experi-
ments on the Chinese dataset demonstrated worse performance than the English data-
set, which may be due to some mistakes in the segmentation of the Chinese expression.
A  deep  attention  NTN  for  visual  question  answering  was  introduced  by  Bai  et  al.
(2018).  In  this  approach,  tensor-based  representations  are  used  to  find  the  joint  rela-
tionship between images, questions, and responses. The authors used bilinear features
to model images and questions that were further encoded by third dimension, i.e. the
response as a triplet. The correlation between various triplets was broken down by dif-
ferent types of answers and questions. For the most discriminatory inference reasoning
method,  a  slice-wise  attention  module  was  developed.  The  model  was  optimized  by
learning  a  label  regression  with  Kullback–Leibler  divergence  losses.  This  designing
technique enabled fast convergence and scalable training across a wide range of answer
sets.  The  proposed  model  structure  was  integrated  into  the  known  visual  question
answering models MLB (Kim et al. 2017) and MUTAN (Ben-Younes et al. 2017). The
proposed technique showed more accuracy than independent MLB and MUTAN mod-
els.  This  study  compared  GloVe  word  embedding  with  the  word  embedding  learned
from  the  proposed  model  and  demonstrated  that  the  model  could  be  applied  to  more
visual question answering models for further verification.

Hu  et  al.  (2017)  proposed  enhanced  face  recognition  performance  by  combining
face recognition features and facial attribute features in a variety of tasks. They created
a robust tensor-based model that develops fusion as a problem of tensor optimization.
Due to the great number of parameters, the model was not effective in explicitly opti-
mizing this tensor, and therefore a rich fusion architecture was proposed on the basis
of  the  tensor.  The  results  revealed  that  this  tensor-based  fusion’s  Tucker-Low-Rank
decomposition has the same Gated Two Stream neural network, making neural network
learning  simple  but  effective.  The  authors  experimented  on  three  well-known  data-
bases  (MultiPIE,  CASIA  NIR-VIS2.0,  and  LFW)  and  found  that  the  fusion  approach

1 3
13547

significantly  increased  the  face  recognition  performance.  This  technique  can  be
expanded to large-scale data utilizing effective Mini Batch SGD-based learning since
they set the equivalence between tensor-factorization and gated neural network archi-
tecture. Another advantage is that this model can be expanded to deeper architectures.

4.6   Continuous‑bag‑of‑word with denoising autoencoder‑logistic regression

To analyze sentiments, a Multimodal Learning technique was presented by Baecchi et al.
(2016)  by  implementing  neural  network-based  models  for  microblogging  contents  that
might consist of texts and images. The proposed architecture is based on the continuous-
bag-of-word (CBOW) model (Mikolov et al. 2013) and was further extended to include
a  denoising  autoencoder  (DA)  to  include  visual  data.  Thus,  CBOW-logistic  regres-
sion  (LR)  is  the  extended  version  of  CBOW.  The  difference  between  CBOW  and  the
extended model is that the new architecture can perform classification and representa-
tion concurrently. The idea behind this approach is that the multi-tasking technique can
develop the performance of a neural network, while the proposed model can incorporate
semantic and sentiment polarity. The model was further extended to CBOW-DA-LR to
include visual data, such as images in tweets. The descriptor acquired by the denoising
autoencoder, along with the regular word presentation, provides a new descriptor for a
word window in the tweet and learns a logistic regressor at the same time. The proposed
CBOW-DA-LR  technique  was  compared  to  SentiBank,  a  commonly-used  approach  in
this domain, and showed higher accuracy (79% accuracy on text + image data vs. 72% of
SentiBank). Although this specific technique shows significant improvements, it should
be further evaluated to ensure its validity.

4.7   Deep belief network

A  deep  belief  network  (DBN)  is  used  to  stack  several  unsupervised  networks  utiliz-
ing  the  hidden  layer  of  each  network  for  the  next  layer’s  input.  A  stack  of  restricted
Boltzmann machines (RBMs) is typically used in the DBN. The benefit of the restricted
Boltzmann machine is to fit the sample features (Hinton 2009). Therefore, a hidden lay-
er’s output in an RBM can be used as another RBM’s visible layer input. This method
may be considered as the further extraction of the features from the extracted features of
the samples.

Suppose that W is the generative weights of the hidden layers learned by an RBM denote
W) . If v is the visible vector, then
h, W) and prior distribution over hidden vectors  p(h

p(v
the probability of v can be expressed by the equation:

|

p(v) =

p(h

W)p(v

|
h, W)

(30)

where p(v
of the grouped following distribution on hidden vectors.

h, W) is kept after learning W; and p(h

|

|

W) is replaced by a more reliable model

|

A  computer-aided  diagnosis  system  was  built  by  Abdel-Zaher  and  Eldeib  (2016)  for
detecting breast cancer, utilizing a weight-initialized backpropagation neural network from
a trained DBN having identical architecture. The authors implemented DBN in an unsuper-
vised state for acquiring the input features from the main Wisconsin breast cancer dataset.

|

h
∑

Deep learning modelling techniques: current progress,…1 313548

S. F. Ahmed et al.

The  obtained  network  weight  matrix  of  DBN  was  then  shifted  into  the  backpropagation
neural  network  to  enroll  the  supervised  state.  In  the  supervised  form,  the  backpropaga-
tion neural network was evaluated on Levenberg Marquardt and Conjugate Gradient algo-
rithms.  The  proposed  methodology  showed  99.68%  accuracy,  which  outperforms  prior
studies. Therefore, this work proposes an efficient system to construct an accurate breast
cancer  classification  model.  However,  a  deep  belief  network  needs  significant  computa-
tional  effort  on  hardware,  and  thus  building  a  real-life  computer-aided  diagnosis  system
based on DBN is very challenging.

Zhao et al. (2017) proposed a feature learning technique named discriminant DBN for
synthetic  aperture  radar  (SAR)  image  classification.  In  the  study,  discriminant  features
were obtained in an unsupervised way by integrating the ensemble-learning technique with
a  DBN.  Some  SAR  image  patch  subsets  were  organized  and  labelled  for  training  weak
classifiers,  then  the  particular  patch  was  defined  by  projection  vectors.  The  SAR  image
patch was projected into each weak decision space covered by weak classifiers. The mod-
el’s  performance  was  found  to  be  better  than  other  proposed  approaches  in  this  domain.
However, since fixed neighbors govern the model, the weak classifier’s training strategy’s
neighbor selection process may cause significant variance in pseudo-labelling. Some adap-
tive strategies can be utilized to choose specific samples for training the weak classifiers.

Another  deep  belief  network,  namely  convolutional  deep  belief  network  (CDBN)  is  a
hierarchical generative model for a real size image. RBM and DBN find it challenging to
scale to complete pictures since they do not take into account the 2D form of the image,
and therefore, the weights for detecting a specific feature must be acquired separately for
each position. CDBN addresses this issue by scaling to the size of real images. The key to
this  solution  is  probabilistic  max-pooling,  a  new  strategy  for  shrinking  higher  layer  rep-
resentations  in  a  probabilistically  sound  manner.  This  model  stacks  convolutional  RBMs
(CRBMs)  to  construct  a  multilayer  structure  similar  to  DBNs.  The  CRBM  is  analogous
to  RBM,  except  the  weight  among  the  hidden  and  visible  layers  is  distributed  over  each
position in the image. By integrating the energy functions of all individual layer pairs, the
system generates an energy function. After training the given layer, the weights and activa-
tions of the layer are frozen and passed on to the next layer as input.

Assume  a  CDBN  with  detection  layer  ( H ),  visible  layer  ( V ),  pooling  layer  ( P ),  and
}
 . The energy function can be described as

 has groups, shared weights Γ = {Γ1,1 … Γk,k

 ); H′
 and detection unit  Hl

 and K ′

another higher detection layer ( H′
connects pooling unit Pk
(Lee et al. 2009):

�

E

v, h, p, h�

= −

v◦

W k ∗ hk

−

bk

hk
ij −

pk◦

Γkl ∗ h�l

−

b�
l

h�l
ij

(

)

k
∑

(

k
∑

ij
∑

)

k,l
∑

(

l
∑

ij
∑

)

(31)
Based on CNN structure, Wu et al. (2018) presented a novel technique for pathological
voice detection, in which the weights of the CNN are pre-trained by a CDBN. The model
uses  statistical  approaches  to  detect  the  structure  of  the  input  data.  The  performance  of
the proposed technique was compared with the existing techniques using the Saarbrucken
voice database. Generative models are generally used to develop the deep learning models
on a small dataset and avoid overfitting. The study reported an accuracy of 68% and 71%
on the validation set, respectively. This is a slight improvement compared to other exist-
ing methods. The results demonstrated that CNN can be tuned more robustly by applying
CDBN to initiate the weights and can avoid the overfitting issue. However, the accuracy for
the testing set decreased, which proves that a more robust system might affect the accuracy.

1 3
13549

A Gaussian Bernoulli-based CDBN (GCDBN) model is made up of many coevolution-
ary layers that are built on Gaussian Bernoulli restricted Boltzmann machines (GBRBM).
Therefore, the architecture takes the benefit of GBRBM and convolution neural networks.
After  each  convolutional  layer,  the  feature  maps  are  down-sampled  using  a  stochastic
pooling  layer.  Using  a  convolutional  neural  network  and  GRBM,  the  proposed  system
can extract relevant features from a real-sized image using generative convolution filters,
reducing the amount of connecting weights, and improving the learning of spatial informa-
tion  from  nearby  picture  patches.  Li  et  al.  (2019a,  b,  c,  d)  proposed  the  GCDBN  model
for  image  feature  extraction,  which  can  reduce  the  computational  cost  significantly  by
replacing fully connected weights with the convolutional filter. However, as a limitation of
this study, only one GCDBN was built with five layers. The recognition accuracy can be
increased by adding more convolutional and pooling layers in the proposed architecture.

DBNs  are  also  widely  used  in  the  analysis  of  hyperspectral  imaging  (HSI).  However,
they fail to examine training samples’ prior knowledge, limiting the discriminant capacity
of  retrieved  features  for  classification.  MMDBN,  a  manifold-based  multi-DBN  was  thus
proposed  by  Li  et  al.  (2022)  in  order  to  acquire  deep  manifold  characteristics  of  hyper-
spectral  imaging.  The  MMDBN  created  a  hierarchical  initiation  approach  that  initializes
the network based on the data’s hidden local geometric structure. The MMDBN algorithm
efficiently  extracted  the  deep  characteristics  from  each  HSI  class.  Experimental  findings
on  the  Salinas,  Botswana  and  Indian  Pines  datasets  reach  90.48%,  97.35%,  and  78.25%,
respectively, demonstrating that MMDBN outperforms some state-of-the-art algorithms in
classification performance. MMDBN’s classification performance can be further improved
by designing the combined spectral-spatial deep manifold networks.

4.8   Hybrid neural network

The process of artificial neural network (ANN) learning entails predicting values for a set
of parameters and an architecture (Guti 2011). After choosing an architecture, supervised,
unsupervised,  or  reinforcement  learning  is  often  accomplished  by  repetitively  modifying
the connection weights using a gradient descent-based optimization method. The signifi-
cant challenges with this type of technique are the need for a prior-determined architecture
for the neural net, its sensitivity to early training conditions, and its local nature. Several
activations or transfer methods have been used for the hidden layer nodes in hybrid mod-
els.  Many  studies  have  suggested  hybridizing  various  basis  functions  via  a  single  hybrid
hidden layer or different linked pure layers. A hybrid neural network (HNN) was initially
introduced to model a fed-batch bioreactor [36]. The hybrid model is comprised of a partial
first  principal  model  that  provides  previous  information  about  the  process  with  a  neural
network, which acts as an estimate of unmeasured process arguments.

A genetic algorithm is a type of evolutionary algorithm that uses evolutionary biology
concepts like inheritance and mutation. A number of operators (selection operator, substi-
tution operator, recombination operator, and mutation operator) are used in genetic algo-
rithms  to  bring  together  the  current  generation’s  eligible  members  to  produce  new  eligi-
ble members. Arabasadi et al. (2017) developed a hybrid technique that combines genetic
algorithms with neural networks for diagnosing coronary artery disease, using Gini-index,
principal component analysis, information-gain, and weight-by-SVM for feature selection.
The  initial  weights  of  a  neural  network  were  determined  with  a  genetic  algorithm,  then
the neural network was trained using training data. The proposed technique implements a

Deep learning modelling techniques: current progress,…1 313550

S. F. Ahmed et al.

feed-forward topology with one hidden layer in the neural network. The experiment con-
tained  22  inputs  and  five  neurons  in  a  hidden  layer  to  produce  an  output  that  indicates
whether the patient has CAD or not. The suggested approach improved the performance of
a neural network by around 10% by upgrading its initial weights with a genetic algorithm
that offers better weights for the neural network. However, several limitations were found
in  this  study.  Instead  of  genetic  algorithms,  other  established  evolutionary  algorithms
like evolution strategy and Particle-Swarm-Optimization (PSO) could be implemented to
ensure the validity of the model. Some parameters, such as momentum factor and learning
rate, could also be optimized.

A novel metaheuristic method was suggested for improving the free parameters of the
PV  generation  forecasting  engine.  Using  this  metaheuristic  optimization  approach,  the
shark-smell-optimization (SSO) technique has been enhanced. The metaheuristic algorithm
incorporates efficient operators to improve its global and local search capabilities. A new
forecasting methodology was applied to a hybrid forecasting engine that combines a neu-
ral network with a metaheuristic algorithm (Abedinia, Amjady, and Ghadimi 2018). This
method includes a two-stage feature selection filter that filters out inefficient inputs using
information-theoretic  criteria,  such  as  mutual  information  and  interaction  gain.  For  PV
generation prediction, a three-stage neural network-based forecasting engine was designed
and trained via a combination of a metaheuristic algorithm and the Levenberg–Marquardt
learning method. With the help of this hybrid technique, the neural network-based forecast-
ing engine eliminated underfitting and overfitting problems.

An HNN with Wavelet Transform and Bayesian Optimization was used in a study con-
ducted  by  (Liu  et  al.  2022)  to  predict  the  copper  price  for  the  short-term  and  long-term.
Wavelet Transform was applied to the data to reduce noise and remove extraneous informa-
tion whereas the algorithm of Bayesian Optimization was utilized on the searching task’s
hyperparameter.  For  training  and  forecasting  copper  price,  GRU  and  LSTM  were  used.
The results showed that the proposed approaches, GRU or LSTM, can accurately forecast
the copper price in the short and long term with the mean squared errors of less than 3%
in both cases. With this HNN, the unnecessary data can be filtered out while the optimal
hyperparameter  set  is  searched.  It  is  simple  and  straightforward  to  use  in  predicting  the
price of other commodities such as the stock market.

4.8.1   Probabilistic neural network (PNN) and two‑layered restricted Boltzmann (RBM)

A hybrid deep learning model was presented by Ghosh, Ravi, and Ravi (2016) for senti-
ment classification that combines a two-layered restricted Boltzmann machine (RBM) and
probabilistic neural network (PNN). Sentiment classification is a sub-domain of sentiment
analysis  that  identifies  positive  and  negative  sentiments  from  a  review.  In  the  proposed
architecture,  RBM  was  used  for  dimensionality  reduction,  and  PNN  classified  the  senti-
ment. The hybrid model was assessed in five datasets and performed better than other exist-
ing  models  in  this  domain.  The  technique  achieved  a  sensitivity  of  92.7%,93.3%,  93.1%,
94.9%,  and  93.2%  for  a  book  dataset,  movie  dataset,  electronics,  and  kitchen  appliance
dataset, respectively. The study revealed that the model does not rely on external resources,
such as sentiment dictionaries, reducing the system’s complexity. It also does not perform
POS  tagging,  which,  although  is  typically  needed  in  this  domain,  reduces  the  system’s
time complexity. In future works, the model should be evaluated with more experiments to
ensure its validity.

1 3
13551

4.8.2   Dynamic artificial neural network

In  the  field  of  deep  learning,  dynamic  neural  networks  (DNNs)  are  an  emerging  technique
that can outperform traditional static models in terms of accuracy, adaptiveness, and compu-
tational  complexity  (Han  et  al.  2021).  Static  models  have  limited  parameters  and  computa-
tional  graphs  at  the  inference  stage,  whereas  DNN  architecture  and  parameters  are  flexible
to different inputs. The outputs of static models are computed based on their link with feed-
forward inputs, as there is no feedback. However, the outputs of dynamic neural networks are
determined by the present and previous values of inputs, outputs, and the network architec-
ture (Abbas Ali Abounoori Esmaeil Naderi Nadiya Gandali Alikhani Hanieh Mohammadali
2016). DNNs can be divided into three types (Tavarone et al 2018): (i) instance-wise dynamic
models that process each instance individually using data-dependent structures or parameters,
(ii) spatial-wise dynamic models that perform adaptive computing on image data at various
spatial locations, and (iii) temporal-wise dynamic models that accomplish adaptive inference
for sequential data, such as movies and texts along the temporal dimension. Instance-wise and
spatial-wise methods are used specifically in image recognition, whereas temporal-wise mod-
els show emerging improvements in text and audio data. These three types can be combined
simultaneously for video-related research domains (Li et al. 2017a, b; Niklaus et al. 2017).

Godarzi et al. (2014) improved an artificial neural network (ANN), specifically named a
nonlinear autoregressive model with eXogenous input (NARX), to predict oil prices by devel-
oping a dynamic neural network. For the validation and improvements of results, the method-
ology followed three stages: ANN static, time series, and NARX. For identifying the signifi-
cant factors that affect the oil price, a time series model was developed in the first stage. Then,
a static ANN model was built to verify the acquired data from the first stage to ensure the opti-
mal performance of the NARX model. In the last phase, the NARX model was implemented
for the prediction. The methodology was found to be a novel approach for oil price prediction
and can be used for other domains like predicting coal or natural gas price.

4.9   Generative adversarial networks

Goodfellow et al. (2014) was the pioneer of adversarial training for image generation, whereby
training is formulated as a minimax adversarial game and a discriminator is used to distin-
guish  fake  data  from  real  samples.  The  generator  works  by  generating  fake  samples  based
on a probabilistic model with the given data. Then, a classification model is applied to verify
whether the generated samples belong to the expected class. The generator aims to fool the
discriminator, whereas the discriminator works to detect the false samples generated by the
generator. Generative models have been used in a wide range of research domains and have
undergone numerous advances since their introduction (Bau et al.  2019; Odena et al.  2017;
Brock et al. 2019; Ledig et al. 2017; Miyato et al. 2018; Karras et al. 2018). In every adversar-
ial approach, there are two models working simultaneously: (i) the generative model acquires
the  data  distribution,  and  (ii)  the  discriminative  model  measures  the  probability  of  sample
point whether it is coming from the training samples. Generative adversarial networks (GAN)
learning concerns finding the optimal parameters 𝜃∗
 by a
minimax game. This relation can be represented by the following expressions (32–35), as sug-
gested by Goodfellow et al. (2014):

G for a generator function G

Z;𝜃G

(

)

𝜃∗
G = 𝜃G

argmin

maxf

𝜃D

𝜃G, 𝜃D

(

)

(32)

Deep learning modelling techniques: current progress,…1 313552

S. F. Ahmed et al.

= 𝜃G

argminf (𝜃G, 𝜃∗

D(𝜃G))

𝜃∗
D

𝜃G

= 𝜃G

argmaxf

𝜃G, 𝜃D

(

)

(

)

where f is determined by:

f

𝜃G, 𝜃D

= 𝔼

x∼pdata

log

D

x;𝜃D

+ 𝔼Z∼N(0,1)

log(1 − D(G(Z;𝜃G

;𝜃D))]

(33)

(34)

(35)

)

(

For ensuring maximum loss in the above equation, the optimal discriminator D∗(x) is
a known smooth function for the generator probability  pG(x) , as described in (Goodfel-
low et al. 2014). The smooth function can be formulated as:

[

(

(

))]

)

[

D∗(x) =

pdata(x)
pdata(x) + pG(x)

(36)

GAN  has  been  in  a  wide  range  of  applications  since  its  emergence.  Generative
approaches  are  being  applied  to  validate  machine  learning  models’  robustness  and  to
generate  new  data  for  rare  examples  and  for  image-to-image  translation  (Park  et  al.
2019; Taigman et al. 2017; Xu et al. 2018), image super-resolution (Ledig et al. 2017;
Sønderby et al. 2017), synthesis training (Brock et al. 2019; Tang et al. 2019), text-to-
image synthesis (Hong et al. 2018; Zhang et al. 2017a, b, c), and many more. However,
the training of generative models is very sensitive to the selected hyperparameters. New
network architectures have been introduced on a regular basis to this research paradigm
in order to maintain training stability.

4.9.1   Unrolled generative adversarial networks

To  solve  the  problems  of  mode  collapse,  instability  of  GANs  network  training  with
complex recurrent generators, and increasing diversity, Pfau (2017) introduced a method
for reducing complexity in GANs training. The proposed algorithm defines the genera-
tor’s  objective  in  order  to  achieve  an  unrolled  optimization  of  the  discriminator.  The
authors argued to use a local optimum of the discriminator parameters 𝜃∗
D(as presented
in Eq. 34) to be demonstrated as a fixed point, which comes from an iterative optimiza-
tion procedure. Pfau (2017) developed the complex recurrent generators increasing the
diversity and scope of the data distribution. To explain the unrolled GAN, the authors
used the discriminator parameter 𝜃∗
D to express the fixed mark of an iterative optimiza-
tion process. The expression continues in the following order (15–17):

𝜃0
D = 𝜃D

= 𝜃k

D + 𝜂k

df (𝜃G, 𝜃k
D)
d𝜃K
D

𝜃∗
D

𝜃G

= lim
k→∞

𝜃k
D

(37)

(38)

(39)

where  𝜂k
  represents  the  learning  rate  scheduler.  Equation  (37)  is  the  full  batch  steepest
gradient ascent equation, and Eqs. (36) and (38) supplement the expression to explain the

(

)

1 3
13553

iterative  optimization  process.  This  approach  is  different  from  that  presented  in  (Good-
fellow  et  al.  2014),  which  indicates  that  the  generator  requires  that  the  discriminator  be
updated  via  several  steps  to  run  every  update  step  for  the  generator.  Some  drawbacks  of
this algorithm include high computational cost and cost for each training period as well as
increased complexity with respect to the number of steps.

4.9.2   Style‑based generator architecture for generative adversarial networks

Motivated by the style-transfer model presented in (Huang and Belongie 2017), an alterna-
tive generator architecture was proposed in (Karras et al. 2019) for GANs. The presented
generator improved the state-of-the-art work with regard to traditional distribution matri-
ces, which continued towards finding better interpolation properties and latent factors vari-
ation.  The  authors  stated  that  compared  to  the  traditional  generators  (Karras  et  al.  2018)
that are used to feed the latent code within the input layer, their architecture (Karras et al.
2019)  allows  input  to  be  mapped  through  an  intermediate  space.  This  latent  space  then
allows  control  of  the  generator  through  the  adaptive  instance  normalization  or  AdaIN
(Dumoulin et al. 2018, 2017; Ghiasi et al. 2017; Huang and Belongie 2017) within every
convolutional layer. The proposed automated linear separability and perceptual path met-
rics quantified the aspects needed for the generator.

The affine transformations learned from the 8-layer MLP was specialized by a parame-
ter w to styles y, where y = (ys, yb), which led to AdaIN (Dumoulin et al. 2018, 2017; Ghiasi
et al. 2017; Huang and Belongie 2017). Followed by the synthesis network g of each con-
volution layer, AdaIN function performs the computation as follows:

AdaIN (xi, y) =y s,i

xi

xi − 𝜇
𝜎
xi
(

)

+ yb,i

(40)

where each feature map xi is normalized individually, the feature matrix is scaled, and bias
is added by applying the respective scalar components from the style y . Karras et al. (2019)
redesigned the generator architecture, which exposed new approaches for image synthesis
tasks. It is clear from the obtained results that style-based generators outperform the tradi-
tional GAN generators.

(

)

4.9.3   Multi‑Level generative models for partial label learning (MGPLL)

with non‑random label noise

The  presented  MGPLL  method  (Yan  and  Guo  2020)  learns  a  problem  through  a  feature
level and label level generator. It follows a bidirectional mapping of data points and label
vectors. A noise label generation is also used while developing the network to form non-
random noise and to execute label denoising. The model architecture has a multi-class pre-
dictor  to  locate  the  training  samples  to  denoise  label  vectors.  Afterwards,  a  conditional
feature generator is applied to perform the inverse mapping. Yan and Guo (2020) adopted
adversarial loss from Wasserstein Generative Adversarial Network (WGAN) to formulate
their learning. They  claimed their model  to  be  the  pioneering work that  exploited multi-
level generative architecture models. Moreover, the network was modelled with non-ran-
dom noise labels in order to learn the partial label (Zeng et al. 2013). The noise label gen-
erator was responsible for exploiting non-random characteristics of noise labels, whereas

Deep learning modelling techniques: current progress,…1 313554

S. F. Ahmed et al.

the  data  feature  generator  was  accountable  for  executing  the  conditioning  upon  the  data
samples based on the particular ground data. Later, the prediction model performed inverse
mapping between these labels and features. The GAN architecture was designed particu-
larly for label learning partially. The conditional label level generator pointed to the advent
of the label-dependent non-random noise, whereas the feature level generator was used to
produce data from the denoised label vectors. As a partial label learning generative archi-
tecture, the authors tested the model against both synthetic PL and real-world (FG-NET,
Lost, MSRCv2, Birdsong, Yahoo! News) datasets, where they achieved satisfactory state-
of-the-art performance.

4.9.4   Dual adversarial co‑learning for multi‑domain text classification

Multi-domain sentiment classification was performed by Wu and Guo (2020) through the
novel dual adversarial  co-learning  method.  The  authors explored a number  of  real-world
sentiment analysis tasks and demonstrated how multi-domain text classification (MDTC)
addresses  the  problem  of  a  model  constructed  for  one  domain  failing  when  tested  on
another domain. The methodology focuses on domain-invariant and domain-specific fea-
tures by shared-private networks, and two classifiers were trained to extract features. Both
the classifiers and feature extractors were designed to work in an adversarial manner, which
resulted  in  the  basis  of  prediction  discrepancy  on  unlabeled  data.  A  multinomial  multi-
domain  adversarial  discriminator  was  developed  to  enhance  the  effectiveness  of  feature
extraction  of  the  domain  invariant  features.  This  technique  separates  the  domain-specific
features from the domain invariant features. The presented methodology is novel in such a
way that the network tries to align data across domains within the extracted feature space
and  labelled  and  unlabeled  data  within  each  domain.  This  technique  also  contributes  to
avoiding overfitting the limited labelled data.

i=1  and  unlabeled  instances Um = {(xi)}um

According to Wu and Guo (2020), if each of the M domains has a limited number of
labelled  instances,  then  Lm = {(xi, yi)}lm
i=1 .  In  the
study,  the  challenge  was  to  make  use  of  all  available  resources  of  the  M  domains.  The
authors reported that this helped to improve the multi-domain classification performance.
They furthermore introduced separation regularizer (Bousmalis et al. 2016; Liu et al. 2016)
to ensure that domain-specific extractors remained distinct from the extractors, which are
domain-invariant. The introduced methodology was designed to pull features from domain
invariant  and  domain-specific  literature.  The  shared  private  network  was  used  to  pass
the extracted features from the texts, followed by two classifiers that work together in an
adversarial  fashion.  A  multinomial  multi-domain  discriminator  was  applied  to  increase
the effectiveness of domain-invariant feature extraction. The authors tested this model on
two MDTC benchmark datasets and for unsupervised domain adaptability. The generative
model positions data with respect to extracted feature space and distinguishes labelled and
unlabeled data between each domain. However, the model should be more robust to avoid
overfitting for limited data samples.

4.9.5   Capsule neural network

A capsule neural network (CapsNet) was first introduced by Sabour et al. (2017) to address
a  few  drawbacks  of  the  convolutional  neural  network  (CNN).  For  instance,  the  sub-sam-
pling  layers  involved  in  CNN  provide  less  translation  invariance.  Also,  CNN  loses  the

1 3
13555

information about location and position estimation and is more prone to overfitting train-
ing  data  for  these  reasons.  It  learns  the  features  without  understanding  the  spatial  infor-
mation. Thus, most of the CNN models are not effective to avoid misclassification. Cap-
sNet addresses these issues by avoiding the sub-sampling layers, which helps the model to
maintain the spatial and pose information. The idea of capsules was introduced by Hinton
et al. (2011). CapsNets use these “capsule” neural units to encode the relationship between
features and location with capsules as well as transformation matrices. Since this approach
acquires translation equivariance, CapsNets are more powerful than CNN for samples with
misled spatial and pose information.

The dynamic routing algorithm (Sabour et al. 2017) also helps CapsNets to overcome
the inability of features to acquire spatial information and scarcity of rotational invariance.
CapsNets  also  encode  part-whole  relationships  like  orientations,  brightness,  and  scales
among different entities that are objects’ features or feature parts. They use shallow CNN
to acquire spatial information. However, CapsNets perform poorly on classification tasks
for missing semantic information. For shallow convolutional architecture, a high number of
convolutional kernels are used to provide the network with a broad receptive field, but this
approach is also prone to overfitting. Since their inception, CapsNets has been employed
in various researches, including cancer and tumor cell detection (Mobiny and Van Nguyen
2018;  Afshar  et  al.  2018),  generative  adversarial  network  (Jaiswal  et  al.  2019),  monitor-
ing  machine  health  (Zhu  et  al.  2019),  object  height  classification  (Popperli  et  al.  2019),
rice image recognition (Li et al. 2019a, b, c, d), protein translational analysis (Wang et al.
2019), hyperspectral images (Landgrebe 2002), and many more.

Hyperspectral images are used for agriculture (Gevaert et al. 2015), land coverage clas-
sification (Yan et al. 2015), vegetation and water resource studies (Govender et al. 2007),
scene classification (Hu et al. 2015), and other environmental monitoring related activities.
Deng et al. (2018) presented two-layered CapsNet, which was trained on less training sam-
ples than Hyperspectral Image (HSI) classification. The work was motivated by the sim-
plicity and comparability of shallower deep networks. The model was trained on two real-
life HSI data: PaviaU (PU) and Salins A. Upon the observation, CapsNet gave an overall
accuracy of 94% and an average accuracy of 95.90% on the PU dataset, whereas CNN had
93.45% and 95.63% accuracy, respectively. The study also made a comparison among Ran-
dom Forests, Support Vector Machines, and CNN with CapsNet in terms of network archi-
tecture. The authors stated that traditional deep learning-based models would not be suit-
able for HSI datasets (Zhong et al. 2018) and that CNN could achieve higher performance
with more training samples, but for limited training data, CapsNet worked better. Figure 12
shows the native logic for Hyperspectral Image (HSI) classification in its conceptual form.

CapsNet was also used in another HSI study (Jiang et al. 2020), in which a new model
called Conv-Caps was designed by integrating CNN and a capsule network with Markov
Random Fields (MRF) for possessing spectral as well as spatial information. With MRF,
the study used graph cut expansion for more efficient classification performance. A CNN-
based  feature  extractor  was  also  used  in  the  network  design.  In  the  model,  the  layer  was
followed  by  a  feature  map  in  order  to  obtain  a  probability  map.  In  the  last  stage,  MRF
was  used  to  find  subdivision  labels.  This  method  takes  proper  advantage  of  the  spectral
and spatial information that hyperspectral images provide. The model was evaluated with
a Bayesian framework perspective and produced satisfactory results. To make capsule net-
works more robust, various research approaches have been introduced over time, a few of
which are presented below.

Deep learning modelling techniques: current progress,…1 313556

S. F. Ahmed et al.

Fig. 12   HSI classification overview presented in (Deng et al. 2018)

4.9.6   Multi‑lane capsule network

Multi-Lane  Capsule  Network  (MLCN)  was  introduced  by  Do  Rosario  et  al.  (2019)  to
address  the  limitation  of  traditional  Capsule  Networks.  The  algorithm  was  tested  on  the
reputed  FashionMNIST  and  CIFAR10  datasets.  When  compared  to  traditional  CapsNet
architectures, the authors achieved satisfactory outcomes with their novel lane proposals.
The experimental baseline was similar to the original configuration employed in (Sabour
et al. 2017). According to the findings of do Rosario et al. (2021), MLCN was found to be
two times more efficient, on average, than the typical capsule network. The authors intro-
duced  the  problem  of  load  balancing  that  occurs  when  distributing  heterogeneous  lanes
within both homogeneous and heterogeneous accelerators. They addressed this issue with
a greedy approach, which was argued to be 50% more efficient than the brute force naive
approach.  Furthermore,  the  load  balancing  issue  was  handled  by  the  neural  architecture
search created by their MLCN models, which matched device memory.

Chang and Liu (2020) improved the MLCN algorithm by addressing the issue of cap-
sule  networks  creating  undesirable  priorities  in  the  background,  which  usually  results  in
poor performance if the background contains too much variance. The authors proposed a
newly  configured  multi-lane  capsule  network  architecture  with  a  strict-squash  (MLSCN)
function for image classification with a complex background to solve this issue. The novel
architecture  replaced  the  traditional  squash  function  and  optimized  the  dropout  function
d. The strict-squash algorithm was proposed to prevent the vulnerability of dynamic rout-
ing while also limiting the uselessness of the capsule initialization features. For meaning-
ful feature extraction, the authors also proposed a coherent dynamic weighting assignment
strategy  in  the  multi-lane  module.  By  combining  these  two  methods,  the  authors  recom-
mended  MLSCN  on  the  basis  of  MLCN.  The  research  work  focused  on  addressing  the

1 3
13557

issue  of  misclassification  of  images  with  complex  backgrounds.  This  issue  can  be  repre-
sented with the input formalized as below (Chang and Liu 2020):

Gi×j

in = ((g11, ..., g1j), (g21, ..., g2j), ..., (gi1, ..., gij))

(41)

where  gij  is  the  input  pixel  value  in  location  ( i, j ).  After  the  convolutional  network  pro-
cesses, the feature map can be obtained using:
Fi×j
out = ((̂g11, ..., ̂g1j), (̂g21, ..., ̂g2j), ..., (̂gi1, ..., ̂gij))

(42)

where   ̂gij is the output pixel value in the location ( i, j ); and Fi×j
out is the capsule layer input,
which is responsible to finish the classification step. Following this step, the output layer
can be defined as:

P = {p1, p2, ...pj}

where  pi is the probability for each category. Most of the regions of an input image have
a  background  as  the  content  or  information;  however,  this  information  is  useless  as  it  is
the background of the image. Yet, the capsule network provides redundant attention to the
information. As a result, it was identified as the fundamental cause of poor performance in
traditional capsule networks. This problem was solved using the aforementioned network
combined  with  the  original  capsule  network  along  with  multi-lane  architectures.  Chang
and Liu (2020) improved their work by making three major contributions: the strict-squash
function, lanes filter, and drop-circuit.

If ui is activation vector of the capsule i of the previous layer, Vj

i is the inclination
of  the  capsule  i  moving  to  be  clustered  in  capsule  j .  The  relation  between  these  two
parameters can be formalized by the following equation (Chang and Liu 2020):
Vj

i = wj

i × ui

|

(43)

The  summation  of  coupling  coefficients  between  i  and  the  other  previous  capsules
|
equals 1, which was achieved by a ‘routing SoftMax’ in which the initial logits bij are
prior probabilities and the capsule i must be coupled with capsule j. Equations (44)-(47)
are used to perform the necessary computations for the model architecture (Chang and
Liu 2020).

|

cij =

exp

bij
k bik
�
�

sj =

∑
(cj

i × vj

i)

i
∑

(44)

(45)

|
The  squash  function  is  interpreted  as  a  normalization  step  upon  the  weighted  sum

|

from the previous layers and is presented as:

uj = Squash

Sj

=

2

Sj

Sj

Sj

2

(46)

(

)

|
1 +
|
|
|

|
Sj
|
|
|
|
|
|

|

|
|
|

|

|

|
|
|

|
|
|

|

Deep learning modelling techniques: current progress,…1 313558

S. F. Ahmed et al.

Finally, to compute cj
the result of the first iteration:

|

i and update ui or vj

i , the following equation is used, where uj is

bj

i = bj

|
i + vj

i × uj

(47)

|

|

|

Based on the best classification performance on four benchmark image classification
datasets, Chang and Liu (2020) found that, in comparison with a single input type, mul-
tiple input types can help the multi-lane architecture to achieve better results. One short-
coming of their research was the drop-circuit, which could not recognize the combined
adapted  lanes.  Consequently,  the  dropout  algorithm  would  need  further  research  as  it
establishes randomness in the experimental results.

4.9.7   Complex‑valued capsule network (Cv‑CapsNet)

To  adjust  complex  datasets,  He  et  al.  (2019)  focuses  on  the  extraction  of  multi-scale,
complex-valued,  and  high-level  features.  Moreover,  they  introduced  an  algorithm  with  a
restricted encoding unit of the complex-valued capsule and dense network, with a generali-
zation of the dynamic routing in the complex-valued realm. The generalized dynamic rout-
ing algorithm was used to fuse the real- and imaginary values of complex-valued primary
capsules. The parameters trained for complex-valued routing were lowered when compared
to real-valued routing of the same dimensional capsules. He et al. (2019) also introduced
Cv-CapsNet +  + as  an  extended  framework  utilizing  a  3-level  Cv-CapsNet  model.  It  was
designed for multi-scale high-level complex-value feature extraction and merging the low-
level capsules information that represents the features of instantiation. In addition, Trabelsi
et al. (2018) presented a method to simulate complex and real-valued convolution, which
was demonstrated for a complex-valued filter matrix W = (A + iB) and a complex-valued
vector h = (x + iy) using the following computation:

W ∗ h = (A + iB) ∗ (x + iy)

(48)

Real-valued matrices were also presented to introduce the real and imaginary parts in

Eq. (49)

ℜ(W ∗ h)
ℑ(W ∗ h)

[

=

]

[

A −B
B A

∗

]

[

x
y

]

(49)

Here, the real and the imaginary components of the output convolutions are two sepa-
rate parts. Moreover, the real and the imaginary part for all complex-valued convolutions
are detached from each other but concatenated with respect to the real and complex parts
for the following complex-part layer. He et al. (2019) argued that this modelling guaran-
tees the sustainability of the complex-valued convolutions and ensures the complex-valued
encoding. Thus, the architecture was employed to fetch multi-scale features, including orig-
inal,  semantic,  and  structure  features.  In  the  model,  CReLU  (complex-valued)  (Trabelsi
et  al.  2018)  was  chosen  as  the  activation  function.  The  authors  implemented  the  model
on CIFAR10 Fashion and MNIST datasets. The model performed well by achieving fewer
trainable parameters with a smaller number of iterations. The generalized dynamic routing
algorithm helped to combine the  real values  with  the  imaginary  values, greatly reducing
the  number  of  trainable  parameters  for  the  same  dimensional  complex  routing  model  as
compared to the real-valued routing models. However, they could not reduce the computa-
tional complexity for training the model.

1 3
13559

4.9.8   Multi‑scale CapsNet

A novel variation of capsule networks was introduced by Xiang et al. (2018), focusing on
computational  efficacy  and  representation  capacity.  In  the  leading  stage  of  the  presented
multi-scale  architecture,  information  was  extracted  following  the  multi-scale  information
extraction method. However, on the second stage hierarchy, the features were encoded into
multi-dimensional  capsules.  An  improved  drop-out  was  also  introduced  in  the  research
work to enhance the robustness of the capsule network. The authors considered the hier-
archical  features  of  the  dataset  and  exploited  multi-dimensional  capsules  for  encoding
those  features.  The  multi-scale  capsule  encoding  consists  of  two  stages,  where  the  first
stage  obtains  the  semantic  and  structural  information  through  multi-scale  feature  acqui-
sition.  Another  top  branch  of  the  two  layers  retrieved  the  semantic  information  from  the
data  as  well.  The  foremost  hierarchy  of  the  middle  branch  of  the  architecture  performed
the  medium-level  feature  extraction  process.  The  last  branch  took  on  the  actual  original
features that were obtained without trainable parameters. In the second stage of the archi-
tecture, feature hierarchies were encoded into multi-dimensional capsules. The final branch
layer was encoded to high-level features of 12D, medium level features of 8D and low-level
features of 4D. The following weight matrices were used to compute the predicted vectors
(Xiang et al. 2018):

̂u1
j

i = Wiju1

i

|
̂u2
j

i = Viju2

i

|
̂u3
j

i = Uiju3

i

|

̂u = concat(̂u1, ̂u2, ̂u3)

Equation  (50)  is used as  the objective function  of  the  multi-category  capsule network

(Xiang et al. 2018):

J

LM =

Tj𝑚𝑎𝑥

0, m+ −

Vj

j=1
�

�

2

�

‖

‖

+ 𝜆

1 − Tj

max(0,

Vj

− m−)2

(50)

�

�

‖

‖

The length of a capsule portrays the probability of the entity, where the length is argued
to  be  compressed  to  [0,1].  Equation  (51)  represents  that  the  length  can  be  compressed
without changing its direction and helps in translating the length as the capsule detects the
actual probability of a given data feature:

vj =

2

2

sj
sj

sj
1 +
‖

sj
‖
where vj represents the capsule output of the j-th unit; and sj is the total input. Dynamic
‖
routing  was  used  as  a  form  of  the  information  selection  method,  which  ensures  that  the
outputs  of  the  children  capsules  are  sent  to  their  respective  parent  capsules  (Xiang  et  al.
2018).  On  the  other  side,  the  routing  coefficients  are  adjusted  by  the  update()  function
shown below:

‖

‖

‖

(51)

Deep learning modelling techniques: current progress,…1 313560

S. F. Ahmed et al.

bi+1 = bi + ̂uj

⋅ uj

ci+1 = softmax(bi+1)

The authors achieved state-of-the-art performance of the model on FashionMNIST and
CIFAR10  datasets.  MS-CapsNet  was  also  used  in  the  Synthetic  Aperture  Radar  (SAR)
image  detection  task  (Xiang  et  al.  2018).  Gao  et  al.  (2021)  addressed  the  issue  of  noise
detection and deformation sensing in traditional CNN architectures with their implemented
multiscale  capsule  network  for  feature  extraction  in  SAR  image  pixels.  The  multiscale
module exploited spatial information from the image features. The authors also applied an
adaptive fusion convolution module to address the issue of noise detection and tested the
model’s architecture on three real-life SAR datasets.

4.9.9   Attention mechanism

The  attention  mechanism  is  described  as  a  mapping  mechanism  to  query  and  set  a  key-
value pair to the output. In the output, all of the elements in values, keys, query, and out-
put  are  vectors.  The  output  values  are  produced  as  a  weighted  sum  of  the  input  values,
and the weight values are assigned using a compatibility function. The query with respect
to  the  associated  key  generates  this  compatibility  function.  Self-attention,  also  known  as
intra-attention, is such an attention-based mechanism that relates various positions of a unit
sequence to compute the representation of that sequence input. The self-attention algorithm
has been used for reading comprehension (Cheng et al. 2016), textual entailment (Paulus
et  al.  2018),  summarization  (Parikh  et  al.  2016),  task-dependent  sentence  representation
(Lin et al. 2017), and in many other fields.

Vaswani  (2017)  introduced  the  transformer-based  attention  mechanism  for  sequence
transduction,  replacing  the  recurrent  units  to  employ  in  encoder-decoder  network  archi-
tectures  for  multi-headed  self-attention  units.  The  transformer  was  trained  significantly
for translation tasks and was found to be faster than the recurrent and convolutional-based
architectures. The model was applied to 2014 WMT English-to-German and 2014 WMT
English-to-French  machine  translation  work.  The  encoder  was  used  to  map  and  input
sequence  for  symbol  representations  and  to  generate  an  output  sequence  given  the  con-
tinuous  representation.  The  transformer  was  employed  to  follow  the  overall  architecture
with the help of self-attention as well as the point-wise fully connected layers within the
encoder-decoder network architecture.

Vaswani (2017) proposed a self-attention algorithm to perform two machine translation
work and achieved satisfactory and parallelizable results. The model obtained a 28.4 score
on BLEU for the 2014 WMT English-German machine translation task and a 41.8 score
on the 2014 WMT English-French machine translation work. The model was generalized
through the transformer-based attention mechanism on words, which proved to be advanta-
geous over previous researches (Gehring et al. 2017; Kaiser and Sutskever 2016). It was
successfully implemented to the English constituency parsing task with both large and lim-
ited training samples. However, the authors did not evaluate this model for image, audio,
and video data.

1 3
13561

4.9.10   Deep Boltzmann machines

Deep  Boltzmann  Machine  (DBM)  (Srivastava  and  Salakhutdinov  2014),  a  deep  neu-
ral  network  architecture,  is  trained  in  a  semi-supervised  approach.  The  architecture  of
DBM  allows  the  network  to  acquire  knowledge  about  complex  feature-based  relation-
ships.  DBMs  have  a  wide  range  of  applications  like  facial  expression  recognition  (He
et al. 2013), text recognition (Srivastava and Salakhutdinov 2014), person identification
from audio-visual data (Alam et al. 2017), 3D model recognition (Leng et al. 2015), and
many more. DBM consists of units that are respective to input data. The hidden units in
a  DBM  consist  of  symmetrical-coupled  stochastic  binary  units.  Different  layers  of  the
DBM architecture hold the binary hidden units. Coupling is enabled in consecutive two
layers in a top-down and bottom-up approach. Such structure allows DBM to understand
complicated internal representations of input data.

4.9.11   Deep‑FS: A feature selection algorithm for deep Boltzmann machines

A  deep  feature  selection  algorithm  was  presented  by  Taherkhani  et  al.  (2018),  which
was argued to have the ability to remove unwanted features from extensively large data-
sets. Considering that a feature selection algorithm can help improve the performance of
a machine learning model significantly, this algorithm was developed for DBM domain
work.  The  algorithm  was  used  by  a  Deep  Boltzmann  Machine  and  gathered  the  data
distribution in a network. Such an algorithm is capable of embedding feature selection
within a Restricted Boltzmann Machine, as presented in Fig. 13.

Considering  an  RBM  of  D  binary  units,  if V  is  a  vector  containing  states  of  the  D
units,  there  is  the  set  V ∈  {0,1}D  and  a  vector  h,  which  contains  states  of  the  hidden
units.  If  an  RBM  has  F  hidden  neurons,  the  F  dimensional  hidden  variables  are  h  ∈
{0,1}F. Taherkhani et al. (2018) expressed the joint configuration of V and h as defined
in the following Eq. (52):

D

F

D

F

E(𝐕, h) = −

Wijvihj −

bivi −

ajhj

i=1
∑

j=1
∑

i=1
∑

j=1
∑

(52)

Fig. 13   Representation  of  a  restricted  Boltzmann  machine  comprised  of  two  layers  of  hidden  and  visible
neurons. In the network, there are D visible and F hidden neural units (Taherkhani et al. 2018)

Deep learning modelling techniques: current progress,…1 313562

S. F. Ahmed et al.

where Wij is the weight connecting the ith visible component vi and the jth hidden compo-
nent hj ; and bi and aj are the biases connecting to the ith visible units and the jth hidden
units, respectively. An energy function was employed by Taherkhani et al. (2018) for the
joint distribution of the visible and hidden variables, which assignment is demonstrated in
Eq. (53):

P(𝐕, h) =

1
Z

exp(−E(𝐕, h))

(53)

where  Z  is  a  partition  function,  also  known  as  the  normalizing  term.  The  function  Z  is
defined below:

Z =

exp(−E(𝐕, h))

V
∑

h
∑

(54)

The overall sum was calculated for all pairs (V,h). If V is a D dimensional vector and h
is an F dimensional binary vector, there are  2D+F different pairs of (V,h) that are possible.
Additionally, the visible units are considered to be binary. Moreover, the conditional prob-
h) were calculated in (Taherkhani et al. 2018) by the following
abilities of P(h
equations:

V)  and P(V

|

|

F

P(h

V) =

p

hj

V

|

j=1
∏

(

D

)

|

P(V

h) =

p

vi

h

Furthermore, these conditional probabilities can be extended as:

i=1
∏

(

)

|

|

p

hj = 1

𝐕

= g(

(

)

|

D

i=1
∑

F

Wijvi + aj)

p

vi = 1

𝐡

= g(

Wijhj + bi)

(

)

j=1
∑

|

(55)

(56)

(57)

(58)

Based on the results of Taherkhani et al. (2018), the novel feature selection algorithm
was designed to handle feature selection from large datasets. The algorithm was embedded
into DBM classifiers, which helped to handle a reduced quantity of input features with less
learning errors from large datasets. The algorithm performed well because of its ability to
remove irrelevant features from large data. The results demonstrated that more than 45%
of  the  features  can  be  reduced  from  the  FashionMNIST  dataset,  which  helped  to  reduce
the network error from 0.97 to 0.90%. In addition, the time of execution was reduced by
more  than  5.5%  for  classification  tasks.  The  model  was  tested  on  GISETTE,  PANCAN,
and  MADELON  datasets  and  showed  to  be  highly  effective  for  all  datasets.  Specifi-
cally, it reduced the input features by 81% for GISETTE, 77% for PANCAN, and 57% for
MADELON datasets.

1 3
13563

4.9.12   Restricted Boltzmann machine

Restricted Boltzmann machine (RBM) is a variant of the Boltzmann Machine, contain-
ing a stochastic neural network (generally) for unsupervised learning (Guo et al. 2016).
Unlike other Boltzmann machines, RBMs have a defining trait of providing a bipartite
graph for its visible and hidden layers, enabling the implementation of a gradient-based
contrastive divergence algorithm for training. Developed RBM models use noisy recti-
fied  units  (linear)  to  store  data  on  intensities.  To  create  learning  modules,  RBMs  can
be efficiently applied to compose deep networking models, such as Deep Energy Mod-
els  (DBNs),  Deep  Boltzmann  Machines  (DBMs),  and  Deep  Belief  Networks  (DBNs).
Generally, RBMs are not a popular choice for computer vision-based applications; how-
ever, in recent times, a few RBM models have been structured to perform vision tasks.
For  example,  Shape  Boltzmann  Machine,  proposed  by  Eslami  et  al.  (2014),  can  learn
to  apply  the  probability  distribution  method  on  object  shapes  to  model  binary  shape
images.

Another prominent use of RBMs, suggested by Kae et al. (2013), is in combination
with  CRF  to  model  local  and  global  structures  for  face  segmentation  with  improved
performance in face labelling. Furthermore, another novel method based on DBN archi-
tecture and mean-covariance RBM was employed for phone recognition. Various frame-
works and models for RBMs have been intensively studied and developed, each having
its  own  sets  of  merits  and  demerits.  Although  most  RBMs  that  are  utilized  for  vision
tasks exhibit remarkable capability in performing image and object classification/iden-
tifying  tasks,  such  models  must  be  a  hybrid  of  one  or  more  networks  to  be  efficient.
As  of  yet,  standard  RBMs  alone  are  not  adopted  for  memory  associative  or  computer
vision-based tasks and are usually in compliance with more than one other deep learn-
ing framework.

4.9.13   Sequence classification restricted Boltzmann machines with gated units

The  intractability  of  learning  and  inference  in  RBM  was  investigated  by  Tran  et  al.
(2020)  considering  the  exponential  complexity  of  the  gradient  computation  while
maximizing  the  log-likelihoods.  The  algorithm  optimized  a  conditional  probability
distribution  in  place  of  a  joint  probability  distribution  for  sequence  classification.  The
authors  also  introduced  gated-Sequence  Classification  Restricted  Boltzmann  Machine
(gSCRBM), in which an information processing gate is integrated alongside long short-
term memory (LSTM) networks. The network architecture was evaluated in an optical
character  recognition  (OCR)  task  and  for  multi-resident  activity  recognition  in  smart
homes. It was argued that gSCRBM requires much fewer parameters compared to other
recurrent  architectures  with  memory  gates.  The  SCRBM  was  constructed  by  the  roll-
ing RBMs along with the class label over the time of training. The network architecture
interpreted the probability distribution with the following equation:

p

y1∶T , x1∶T , h1∶T

=

p(yt, xt, ht

ht−1)

T

(59)

where 𝐱1∶T
sequence of class labels; and 𝐡0

 , 𝐡1∶T

(

 are the hidden unit biases.

 are the time series corresponding to the visible and hidden states; y1∶T

|

 is a

t=1
∏

)

Deep learning modelling techniques: current progress,…1 313564

S. F. Ahmed et al.

The model faced difficulty with an intractable inference, as explained in (Sutskever and
Hinton  2007).  The  authors  also  suggested  that  this  problem  could  be  solved  through  the
addition of recurrent units, as done for RTRBM (Sutskever et al. 2009). For RTRBM, the
class labels were excluded, while in the case of SCRBMs, local distribution at time t was
p(yt, 𝐱t, 𝐡t

𝐡t−1) . This was replaced by the expression presented in Eq. (60):

|

p(yt, 𝐱t, 𝐡t

̂𝐡t−1

=

exp(−E𝜃(yt, 𝐱t, 𝐡t;̂𝐡t−1)
yt,𝐱t,𝐡t exp(−E𝜃(y� , 𝐱� , 𝐡� ;̂𝐡t−1)

(60)

�

∑

�
�
�

̂𝐡t−1

where

 is the expected values vector for the hidden units at time t-1 and is calculated as:

̂𝐡t−1 = 𝔼[𝐇t−1

𝐱1∶t−1, y1∶t−1]

(61)

The local energy function is given by:

E𝜃

(

y�

, 𝐱�

, 𝐡�

;̂𝐡t−1

= −

𝐱t

)

[

(

)

|
xh + 𝐮⊤

yt +

⊤𝐖

̂𝐡t−1

⊤

𝐖

hh

(

)

𝐡t − 𝐚⊤𝐱t − byt − 𝐜⊤𝐡t
]

(62)

The  algorithm  was  designed  to  achieve  better  learning  and  dynamic  interference  in
sequence  classification.  For  long-term  information  retrieval,  the  algorithm  followed  the
structure  of  rolling  RBMs,  and  gated  units  (gSCRBM)  were  introduced.  The  gSCRBM
performed  better  in  terms  of  parameters  because  it  was  trained  with  fewer  parameters
than traditional LSTMs and GRUs. The model was evaluated to prove its superior perfor-
mance over advanced LSTM structures (Yu et al. 2019), Bidirectional LSTM (BiLSTM),
and  Stacked  LSTM  (StackedLSTM)  (Graves  and  Schmidhuber  2005).  It  was  found  that
SCRBM  outperformed  the  other  models  in  terms  of  generalization.  Although  GRUs  and
LSTMs  generated  better  results  in  a  few  circumstances,  the  authors  explained  that  those
architectures demand more sophisticated structures, longer processing time, and more hid-
den units. SCRBM was found to be more compact with fewer parameters but with the same
amount of neurons as another RNN network containing the same hyperparameters. How-
ever, the SCRBM was not able to capture long-term information, which led to a vanishing
gradient  or  exploding  gradient  problem.  This  issue  was  later  resolved  by  the  gated  unit
(gSCRBM).

4.10   Stacked denoising autoencoders

4.11   Autoencoders

Autoencoder neural networks were designed for unsupervised learning by applying a back-
propagation algorithm of the target values for equalizing the inputs. The autoencoder learns
the approximation between the output and identity function when the input is compared to
the output. When the autoencoder discovers the features or data structure, the hidden units
are subjected to a sparsity constraint. Autoencoder models require knowledge of the geom-
etry of the data to properly understand the input data. Constraining the node in the hidden
layer allows autoencoders to learn the low-dimensional representation of the model.

1 3
13565

Fig. 14   Representation of Elman network (Liou et al. 2014)

4.11.1   Autoencoders for Words

Liou et al. (2014) presented the Elman network for encoding each word of a different vec-
tor  in  semantic  space,  which  is  related  to  corresponding  entropy  coding  (Elman  1990,
1998) and is operated on an encoder for training. The authors utilized the Elman network
as a super Turing machine for powerful computation work (Siegelmann 1995). Figure 14
illustrates the Elman network employed by a simple recurrent network, which was designed
for semantic word categorization. However, because it could not handle the encoding task,
the Elman network was redesigned in order to encode the words into the semantic space

Fig. 15   Schematic representation of deep energy model (Samaniego et al. 2020)

Deep learning modelling techniques: current progress,…1 313566

S. F. Ahmed et al.

domain. The achieved codes were utilized in indexing, ranking, and categorizing literary
tasks.

Liou  et  al.  (2014)  encoded  each  word  for  individual  vectors  while  training.  The  ward
was bound with corresponding entropy coding in semantic space. The training methodol-
ogy also included ranking, indexing and categorizing literacy steps from the training data.
The model was trained on the basis of acquired datasets from two Chinese novels: Romance
of the Three Kingdom and Dream of the Red Chamber. However, they still needed to inves-
tigate whether a low error rate could be achieved without the renewed coding units and the
same network architecture.

4.11.2   Deep energy models

The deep energy model (DEM) is a deep learning training technique for deep networks and
architects based on the restrictive Boltzmann machine learning methodology (I. Goodfel-
low et al. 2016; Guo et al. 2016). It includes a feed-forward neural network that transforms
data inputs deterministically rather than modelling the output via a layer of stochastic hid-
den units (perceptron/neuron), as shown in Fig. 15. The feedforward network (g𝜃) acts on
the universal approximation theorem in order to approximate a continuous function, map-
ping corresponding inputs and outputs (Nguyen-Thanh et al. 2020).

Unlike deep belief networks and deep Boltzmann machines that have multiple stochas-
tic hidden layers, DEM consists of a single stochastic hidden layer (h), which allows effi-
cient inference and simultaneous training of all the layers within the network (Ngiam et al.
2011). Hopfield energy models were one of the earlier developed DEMs that, in their sim-
plistic nature, allow closed-form modelling (Bartunov et al. 2019). However, the Hopfield
model has significant demerits and is unable to work with the quadratic dimensionality of
memory patterns. The capacity for more patterns is also limited by the number of param-
eters in the network. Since real-world data consist of higher-order dependencies, the Hop-
field  energy  model  cannot  be  used  (Bartunov  et  al.  2019).  Ngiam  et  al.  (2011)  utilized
the DEM approach to process natural images, demonstrating significant improvements in
data  outputs  when  compared  to  greedy  layer-wise  training.  In  recent  years,  the  develop-
ment  of  energy-based  models  meta-learning  (EBMM)  has  been  observed  to  show  better
performance as a memory model that is capable of recalling training, memorizing patterns,
and performing compression (Bartunov et al. 2019; Kraska et al. 2018; Parkhi et al. 2015;
Sun et al. 2015; Zhang et al. 2016a, b). Meta-based learning primarily operates on the read
(x;θ ) and write (X) functions by means of truncated gradient descent, as follows:

read (̃x; 𝜃) = x(K+1) = xk − 𝛾 (k)∇xE

x(k)

, x(0) = ̃x

L(X, 𝜃) =

1
N

N

i=1
∑

W(x, θ) = E(x;θ) + α

(

)

E[

xi − read

xi;𝜃

2

2

]

|
|
|

|
∇xE(x;θ)

(

2
2 + β

)|
|
|
|
θ − θ

2
2

write (X) 𝜃(T), 𝜃(t+1) = 𝜃(t) − 𝜂(t) 1
N

||
|

N

i=1
∑

||

|
||
∇𝜃W(xi,𝜃(t)), 𝜃(0) = 𝜃

||

(63)

(64)

(65)

(66)

1 3
13567

where x  is  the  input  (the  deterministic  dynamics);  X  represents  the  Nth  set  of  input  pat-
terns compressed into parameters,θ , by the writing rule; N is the number of stored patterns;
k = 1,  2,…K  (number  of  sequences  required  to  be  updated  to  perform  gradient  descent
for  optimization  for  reading  function);  t = 1,  2,…T  (number  of  sequences  required  to  be
updated  to  perform  gradient  descent  for  optimization  for  write  function),  respectively;
γ(k)andη(t)
 are the learned stepped sizes for reading and writing functions respectively; E(x)
represents the energy function; ∇x is the derivative operator; and W(x, θ) is the writing loss
function, consisting of meta parameters α andβ , representing the energy function at a local
minimum that must be two-fold and requires the hessian term to be positive. The later part
of the writing loss function performs optimization, limiting deviation of prior parameter, θ ,
from the initial parameter,θ . Finally, implementing gradient descent tunes the writing func-
tion as Eq. (34); where L(X, θ) denotes the score matching objective, or the reconstruction
error for the read function.

Compared  to  past  DEMs,  EBMMs  can  utilize  slow  gradient  learning,  having  effec-
tive convolutional memories, particularly due to fast writing rules (Bartunov et al. 2019).
EBMMs also adhere to and manage memory capacity efficiently, even for non-compress-
ible inputs, such as binary strings to natural images of high compression. It also has the
ability to differentiate different patterns (energy levels). The method proposed by Bartunov
et al. (2019) resolves the functioning pace of EBMMs with fast writing and limited param-
eter updates (a maximum of 5 steps), adding new inputs for the weights. Another advan-
tage  of  this  method  is  the  association  of  faster  reading  and  fewer  gradient  descent  steps.
The employability of the proposed operations, which store N patterns in memory and do
not require additional assumptions, further adds to the efficiency of the model (Bartunov
et  al.  2019).  However,  batch  writing  assumption  is  a  challenge  for  EBMM  and  could  be
improved with more elaborate architecture.

It is also difficult to find the optimum balance between writing speed and the model’s
capacity (a commonality for most deep learning energy models) (Ba et al. 2016; Bartunov
et al. 2019). In addition, the characterized properties of the learning attractor models are
not  yet  known,  and  EBMM  cannot  return  different  associations  when  under  uncertainty,
which occurs due to compression. Furthermore, with the general application of gradient-
based  meta-learning,  it  is  difficult  to  evaluate  the  expected  outcome  of  EBMMs,  mainly
because of the high dimensionality pattern space of inputs that increases the resulting dis-
tortion of the model and decreases the output reliability after adaptation. Therefore, a dif-
ferent gradient descent functionality is necessary. Also, parametric gradient-based optimi-
zation requires significant updates (for memory/recalling applications) and, hence, is slow.
Resolving these existing issues, together with the observation and exploration of more sto-
chastic variants for EBMMs would lead to significant improvements for DEM.

Statistical  learning  and  construction  of  an  inference-free  hierarchical  framework  offer
a  viable  solution  for  density  estimation,  consisting  of  higher  dimensional  challenges.  By
utilizing Bayesian (Eq. (67)) and Parzen score matching functions (Eq. (68)) (Saremi et al.
2018;  Vincent  2011)  together  with  a  multilayer  perceptron  of  scalable  energy  learning
operation (Eq. (69)), the deep energy estimator network (DEEN) can be modelled and fur-
ther optimized (Saremi et al. 2018), as follows:

̂x(ξ) = ξ + σ2ψ(ξ;θ)

(67)

where σ denotes any level of noise; ψ represents the score function; ξ is the noisy measure-
ment of underlying random variable x; and θ is the parameter vector.

Deep learning modelling techniques: current progress,…1 313568

S. F. Ahmed et al.

P(ξ) =

S(ξ

x(k))

1
n

(68)

(69)

k
∑
where P represents the Parzen density estimator; S signifies the smoothing kernel; k rep-
resents  the  nth  x  of  a  dataset,  x = {x1, x2 … xn
 };  and  n  is  the  number  of  elements  in  the
dataset, x.

|

E(x;θ) =

w(L+1)
α

h(L)
α

x;

w(1), w(2), … , w(L)

=

εα(x;θ)

α
∑

(

{

α
∑

})

In Eq. (69) (Saremi et al. 2018), E(x;θ) is linearly constructed from the preceding hid-
den layer  hL, in which w is the weight of each data x and parameter θ , εα
 denotes the expert
(corresponding products of expert, PoE) parametrized by the neural network, and α signi-
fies the number of iterations.

Deep  energy  estimator  networks  (DEENs)  have  been  demonstrated  to  be  effective
with  high  dimensionality  data  values  (Saremi  et  al.  2018).  However,  it  is  important
to  note  that  although  DEEN  can  auto-regularize  due  to  its  Parzen  function,  it  is  not
an  autoencoder.  In  fact,  DEEN  can  operate  with  a  decoder  by  not  directly  estimating
the score functions (Alain et al. 2014) and, thus, skipping stability issues of denoising
autoencoders. Being dataset-dependent, DEEN does not impose any bounds towards σ
and can be effectively regularized. Apart from working with higher dimensionality data,
deep  energy  estimators  are  employed  for  semi-supervised,  unsupervised  learning,  and
generative modelling (Saremi et al. 2018). DEENs provide consistent estimations and,
therefore, acquire increasing interest; however, more testing is required to examine the
network’s performance for dynamic data as well as the scalability potential.

Another  prominent  application  of  DEM  is  the  nonlinear  finite  deformation  hyper-
elasticity problem, operating on an energy and loss function. For instance, using Eule-
rian  motion  description  and  transport  deformation  gradient  formulation,  the  nonlinear
response of elastic materials (in 3D) with a large deformation continuum can be mod-
elled by employing DEM via DNNs. In a previous work, a neural network is structured
using  Eq.  (70),  then  optimized  to  minimize  its  potential  energy  using  a  loss  function
(Nguyen-Thanh et al. 2020):

̂zl
k = σ

nl−1

(

j=1
∑

kj ̂zl−1
wl

k + bl

k

, 0 < 1 < L (the ﬁnal layer)

)

(70)

where ̂z is the final output of the final layer l; w and b are weights and biases, respectively;
and σ is the activation function acting on the kth neuron of the lth layer.

DEM  can  also  be  utilized  for  nonlinear  deformation,  being  faster  with  fewer  cod-
ing and having the traction-free boundary conditions to be auto-filled. Training enables
faster solution retrieval, and the model can be easily coded in common machine learn-
ing operating platforms, such as TensorFlow and Pytorch (Nguyen-Thanh et al. 2020).
However, the use of DEM has certain drawbacks due to the imposition of the boundary
condition of parameters and the associated integrations used for modelling and, there-
fore, requires further study to improve the integration techniques. Moreover, the mod-
elling  tends  towards  non-convexity  of  loss  function  during  the  nonlinear  evolution  of
network  neurons,  and  so,  an  enhanced  theoretical  understanding  is  required  to  better
establish the deep neural network architecture. DNNs for finite deformation hyper-elas-
ticity  are  trained  using  backpropagation,  computing  the  gradient  loss  and  minimizing

1 3
13569

the  function,  using  a  standard  optimizer.  Considering  the  tendency  of  a  gap  to  exist
between backpropagation and energy-based models, Nguyen-Thanh et al. (2020) admin-
istered  forward  propagation  to  approximate  the  solution  with  defined  boundary  condi-
tions,  which  directs  the  prediction.  Scellier  and  Bengio  (2017)  proposed  equilibrium
propagation to bridge gaps between backpropagation and the energy-based model. The
main  objective  of  equilibrium  propagation  is  to  ensure  a  learning  framework  for  the
DEMs with a 0.00% training error. Provided the statistics of an excellent training error
score, it would be interesting to observe the performance of such a system for different
deep  learning  techniques  and  DEMs  with  complex  non-linear  data  of  high  parameters
and dimensions.

Reinforcement  learning  (RL)  is  another  intensively  studied  deep  learning  method
that  has  unique  connections  with  DEMs  in  terms  of  state  and  action  spaces.  RL  sur-
pluses the shortcomings associated with DEMs, which are mostly sampling issues and
unpopularity  with  regression  models  (Zhang  et  al.  2020).  For  example,  performing
molecular modelling using a DEM-based system would be difficult due to the absence
of  frameworks  that  do  not  involve  a  classification  route  for  the  dataset.  Consequently,
when  it  comes  to  modelling  problems  that  do  not  involve  density  estimations  or  the
necessity for energy functions, a new neural network is required. Recently, Zhang et al.
(2020) proposed a novel approach, where RL is reformulated into distribution learning
to resolve sampling issues, using a minimax generative adversarial network to develop a
targeted adversarial learning optimized sampling (TALOS) methodology. Another tech-
nique  using  entropy  policy,  called  variational  adversarial  density  estimation  (VADE),
was  also  effective  (for  molecular  modelling),  demonstrating  how  cross-fertilization
between  EBMs/DEMs  and  RL  can  overcome  the  challenges  of  EBMs.  Haarnoja  et  al.
(2017) explored maximum RL via DEM using the Markov decision process (Eq. (71))
and  modified  the  objective  to  maximize  the  entropy  (Eq.  (72)).  Using  soft  Q  learning
and  the  Bellman  equation,  the  model  operated  on  learning  maximum  entropy  policies
(Eq. (73)).

πstd=argmaxπ

t
∑

E(st+at

)∼pπ

[r(st, at)]

πMaxEnt=argmaxπ

t
∑

E(st+at

)∼pπ

[r(st, at)] + αH(π(⋅

st))]

(71)

(72)

where S and a are state and action space, respectively; r denotes reward;  p𝜋 signifies the
marginals of state and state action for the policy, π(⋅

st) ; and α acts as a hyperparameter.

|

πMaxEnt(at

st) = exp

1
α

(Q∗

sof t

St, at
|

− V∗

sof t(st)))

(73)

sof t represents a partition log function; and Q∗
|

where V∗
detailed by Ziebart and Fox (2010) and Haarnoja et al. (2017), respectively).

sof t denotes a Q-function (proven and

(

)

Reinforcement  learning  energy  modelling  policies,  which  are  suitable  for  high-
dimensional  values,  have  been  observed  to  be  robust  and  applicable  to  code  robotic
tasks  and,  hence,  have  become  quite  popular  amid  humanoid  robots.  Although  the
model requires pre-training of the general-purpose stochastic policies, when compared
with  other  deep  energy  modelling  techniques,  reinforcement  learning  via  DEM  seems
most  promising,  particularly  by  being  able  to  solve  inputs  and  sampling  issues  for
energy-based modellings.

Deep learning modelling techniques: current progress,…1 313570

S. F. Ahmed et al.

4.11.3   Deep coding network

Deep  predictive  coding  network  is  a  bio-inspired  framework  built  on  the  theoretical
understanding  of  how  the  brain  infers  sensory  stimuli.  The  mechanism  by  which  the
brain speculates decisions based on certain data (e.g. visual information) has been for-
mulated as the baseline for predictive coding, followed by the adaptation of filter objec-
tives and training of modules via gradient descent. However, due to the still very mis-
understood  functioning  of  neurons  in  the  brain,  it  is  likely  that  the  connected  neurons
in the brain consist of a more complex architecture, significantly limiting existing deep
learning models. Incorporating a feedforward and feedback (prediction making) system
along  with  each  layer  of  a  neural  network  is  a  generative  understanding  of  deep  cod-
ing networks, particularly the deep predictive coding system. Such networks are heav-
ily studied and used for computer vision, where classification for images and videos is
performed.

A base equation for a deep predictive coding network is given by (Dora et al. 2018):

N

Y1,X1

Y1,X1

E =

(

lp

yl
m,n − ̂yl

m,n

+

lp

yl
m,n

+

lp(w(l)

m,n,i,j))

(74)

)

m,n
∑

m,n
∑

l=0
∑

m,n,i,j
(
∑
where lp is the calculated error in compliance with p-norm; yl
m,n is a vector in a channel of
the lth layer, consisting of mth rows and nth columns; w(l)
m,n,i,j represents the filter through
which neurons at m, n position of l layer is projected; Y1andX1 are the height and width of
the layer arranged in a 3D box shape; and ̂y and y denote the predicted and actual activity
of neurons, respectively.

)

(

With limited research and understanding of brain processing, particularly of events asso-
ciated with memory, learning, and attention, developing mature and complex deep predict-
ing  coding  network  architectures  remains  challenging.  Therefore,  visual  image  mapping
requires further analysis. Nevertheless, many novel deep learning frameworks and applica-
tions employ the use of predictive coding across various fields for plethora machine learn-
ing applications. For instance, Dora et al. (2018) developed a generative model based on
deep predictive coding and trained using unsupervised learning for processing real-world
images and to effectively capture the statistical regularities of the data. Such ability makes
the model suitable for various image classification and computer vision tasks. The applica-
tion of a similar model in security is another prominent example.

The importance of machines to detect video anomalies is gaining popularity to enhance
security and surveillance. However, video anomalies are highly ambiguous and complex,
with high error margins and poor scores in existing reconstruction and prediction modules
(Hasan et al. 2016; Liu et al. 2017; Ye et al. 2019). A recent application of deep learning
by  Ye  et  al.  (2019)  demonstrated  an  improved  video  anomaly  detection.  Using  a  predic-
tive coding network with an error refinement module, the methodology was able to refine
coarse predictions, reconstruct errors, and create a framework that assembles reconstruc-
tion and prediction modules. The modified predictive coding model uses a multilayer net-
work that extracts prediction error features (Eqs. (75) and (76)). The new predictions are
then  generated  to  rectify  prediction  errors  using  the  convolution  of  the  ConvLSTM  unit,
enabling  sequential  dynamics  modelling  (Eq.  (77)).  Afterwards,  the  system  performs
refinement.  To  reach  a  refined  estimation,  score  gaps  between  the  frames  (normal  and
abnormal) are reconstructed. Equation (79) represents the error refinement module based
on  Eq.  (78).  The  objective  functions  were  minimized  and  optimized.  Metrics,  including

1 3
intensity (to measure pixel-wise difference),  gradient  (to  prevent blurry  predictions),  and
motion constraints, were utilized as a part of the adversarial training strategy.

13571

PEP ∶ Ej−1 = Ij−1 − ̂I(j−1)

where  Ej−1  is  the  previous  prediction  error;  Ij−1  represents  the  ground  truth;  and
denotes the previous prediction.

Rj−1 = PEP(Ej−1)

In Eq. (44), Rj−1 extracts deep features, and Ej−1 is the previous prediction error.
̂Ij = Conv(ConvLSTM

Rj−1

)

(75)
̂I(j−1)

(76)

(77)

̂Ij  is  the  updated  prediction  generated  from  the  previous  prediction  error;  and
where
ConvLSTM  is  a  special  LSTM  operation  (spatial  convolutions  placed  for  connected
transformations).

(

)

ΔS =

t∈NSt
Tn

∑

−

t∈ASt
Ta

∑

(78)

where ΔS is the regularity score gap for error refinement (between normal and abnormal
frame); St is the regularity score; t, time frame; N is the sequence number set for the nor-
mal frame; A is the sequence number set for the abnormal frame; and Tn and Ta denote the
total number of normal and abnormal frames, respectively.

(79)
(
̂Et and Et are the updated prediction error and preceding prediction error of time step

)

̂Et = ERM

Et

where
t, respectively.

Another novel method was proposed by Tandiya et al. (2018) based on deep parse coding
to detect radio frequency (RF) anomalies that are present in wireless connections. The neural
network was trained to recognize the anomaly when there is a potent deviation between the
predicted and actual outcomes. The method performs real-time RF monitorization, which is
both non-intrusive and automated. Tandiya et al. (2018) demonstrated that the use of deep pre-
dictive coding is faster and more efficient than other ML-based approaches. Sequenced images
of the network’s normal operation were obtained using Prednet, a video frame detector, which
teaches the network to make predictions and detect anomalies. Auto-tuning the hyperparam-
eters could be one significant improvement for the predictive coding networks, using:

S𝛼
xx(n, f ) =

1
N

N

r=1
∑

1
N � XN� (n, f + 𝛼∕2)X∗

N� (n, f − 𝛼∕2)

(80)

where α = cycle frequency as one axis.

The anomaly detection efficiency of this neural network was close to 100%. The seis-
mocardiography-based detector showed to act relatively faster than the first detector, which
is  responsible  for  the  detection  anomaly  in  consecutive  spectrogram  images.  The  seis-
mocardiography-based detector spots image anomalies almost instantaneously, and such a
methodology of anomaly detection can be employed for networks with variable constraints
and  devices.  However,  the  robustness  of  detection  can  be  further  improved  by  working

Deep learning modelling techniques: current progress,…1 313572

S. F. Ahmed et al.

with  complex  anomalies,  evaluating  longer  run  times,  and  employing  machine  learning
techniques to process raw data in different forms. Showing promising error rates and effi-
cient predictive capacity, each framework has its own merits and demerits. Given that pre-
dictive coding is an area that requires further understanding, the functions and frameworks
applied by machine learning engineers to solve problems in various disciplines, with vari-
ous biases, can be significantly improved and optimized further.

The main objective of sparse coding, a special case of deep predictive coding, is to deter-
mine a set of input vectors as a linear combination of basis vectors, which is then taught to
efficiently represent data, as seen in Eq. (49) (for example, image data for classification). In
a study by Zhang et al. (2017a, b, c), deep sparse coding (a deep modelling technique) pro-
duced effective results in extracting high distinct features from raw image pixels, for which
the process is based on unsupervised learning. The deep sparse coding network is constructed
upon  basic  input,  a  sparse-coding  and  pooling  layer,  and  a  normalization  and  map  reduc-
tion  layer.  Such  an  algorithm  uses  heuristics  to  minimize  non-convex  functions.  Although
the system is dependent on a CNN architecture and could have improved speed, the overall
framework is easier to code and functions better than any independent CNNs. However, deep
sparse coding suffers from not being mathematically rigorous and converging towards a local
minimum. Arora et al. (2015) demonstrated how sparse coding can also converge to a global
minimum, providing a novel-based initialization method that returns a better starting point.

Cij = arg min

1
2

xi,j − Wcij

2, s.t

cij

≤ K

L0

(81)

where  Xij is the receptive field at spatial location i, j; W represents the weight of the input;
C is the number of colored channels (of the input layer), as well as the number of feature
maps for the feature map layer (Zhang et al. 2017a, b, c); K controls the sparsity of cij ; and
L0 is a constraint under batch tree orthogonal matching pursuit.

||

||

|

|
|
|

|
|
|

|

C = arg min

1
2

I −

M

m=1

wm ∗ Cm

2
F

+ 𝛽

where wm is the kernel; and Cm is the sparse feature map.

∑

‖
‖
‖
‖
‖

‖
‖
‖
‖
‖

M

M

∑

m=1
m=1
|
|

C1

|
|

(82)

Convolutional sparse coding network (CSN), based on Eq. (50), incorporates the frame-
work of a convolutional system (Zhang et al. 2017c). Similar to a deep sparse coding net-
work that primarily performs patch-level approximation, CSN conducts image-level recon-
struction (approximation as well), but with more hindrance due to the convolution’s nature.
Therefore, deep sparse coding was observed to propagate sharp information forward. The
hierarchical  sparse  coding  (HSC)  framework  is  a  similar  working  sparse  coding  network
that  completes  the  patch  operation  using  concatenation  methodology.  For  HSCs,  map
reduction layers are essential to delve deeper. Utilizing multi-level optimization and non-
negative  sparse  coding,  Sun  et  al.  (2017)  developed  a  multilayer  sparse  coding  network.
The latter system is a deep learning framework consisting of bottleneck modules with an
expansion  and  reduction  layer  of  sparse  coding,  consisting  of  wide  and  slim  dictionaries
that are able to generate high- and low-dimensional distinct features and clustered repre-
sentations,  respectively.  A  supervised  learning  technique  was  also  employed  to  train  the
dictionaries, optimizing regulatory parameters. Although the network requires fewer layers
and  parameters,  the  deep  learning  architecture  should  be  further  studied  to  improve  pro-
cessing efficiency. The general descriptions of each deep learning modelling technique, as

1 3
13573

e
h
t

m
o
r
f

s
n
o
i
t
a
t
n
e
s
e
r
p
e
r

e
h
t

;
)
T
R
E
B

(

r
e
m
r
o
f
s
n
a
r
t

2
1
5

s
i

h
t
g
n
e
l

m
u
m
i
x
a
m

r
e
d
o
c
n
e

l
a
n
o
i
t
c
e
r
i
d
i
b

T
R
E
B
n
o

d
e
s
a
b

l
e
d
o
m

t
n
e
r
e
ff
i
d

g
n
i
y
f
i
t
n
e
d
i

r
o
f

t
n
e
m
u
c
o
d

e
h
t

r
o
f

s
l
e
b
a
l

k
s
a
t

n
o
i
t
a
c
fi
i
s
s
a
l
c

t
n
e
m
u
c
o
d

e
g
a
r
e
v
a

e
h
T

t
n
e
m
u
c
o
D

s
r
e
t
e
m
a
r
a
p

f
o
r
e
b
m
u
n

e
h
t

d
e
c
u
d
e
R

f
o

t
n
e
m
p
o
l
e
v
e
D

.
l
a

t
e

i
r
a
k
i
h
d
A

n
a
h
t

s
s
e
l

s
i

h
t
g
n
e
l

n
o
i
t
a
c
fi
i
s
s
a
l
c

s
e
m

i
t

0
3

y
b

n
o
i
t
a
c
fi
i
s
s
a
l
c

t
n
e
m
u
c
o
d

)
9
1
0
2
(

e
h
t

s
e
t
a
g
i
t
s
e
v
n
i

t
o
N

l
a
c
i
n
i
l

C

e
c
n
a
m
r
o
f
r
e
p

r
e
t
t
e
b

g
n
i
v
e
i
h
c
A

w
o
h
f
o

t
n
e
m
s
s
e
s
s
A

)
9
1
0
2
(

.
l
a

t
e

i
S

f
o

s
t
fi
e
n
e
b

e
c
n
a
m
r
o
f
r
e
p

T
R
E
B
o
i
B
g
n
i
n
u
t
-
e
n
fi

t
x
e
t

l
a
c
i
n
i
l
c

h
t
i

w

n
o
i
t
c
a
r
t
x
e

t
p
e
c
n
o
c

-
i
r
a
v

n
o

)
8
1
.
3
9

f
o

s
e
r
u
s
a
e
m
-
1
F
(

d
r
o
w
c
i
s
s
a
l
c

l
l
e
w

s
t
s
e
t

k
r
a
m
h
c
n
e
b

s
u
o

s
e
h
c
a
o
r
p
p
a

g
n
i
d
d
e
b
m
e

d
n
a

)
e
V
o
l
G

,
c
e
v
2
d
r
o
w

(

s
d
o
h
t
e
m
d
e
z
i
l
a
u
t
x
e
t
n
o
c

-
c
a
r
t
x
e

t
p
e
c
n
o
c

l
a
c
i
n
i
l
c

a

n
o
m
r
o
f
r
e
p

)
T
R
E
B

(

k
s
a
t

n
o
i
t

h
t
i

w
e
u
q
i
n
h
c
e
t

e
h
t

d
e
t
s
e
T

-
i
r
a
m
m
u
s

t
x
e
T

n
o
i
s
i
c
e
r
p

f
o

e
g
a
r
e
v
a
-
o
r
c
a
m
e
h
T

-
a
m
m
u
s

t
x
e
t

a

d
e
c
u
d
o
r
t
n
I

t
e
s
a
t
a
d

e
n
o

y
l
n
o

n
o
i
t
a
z

s
t
l
u
s
e
r

l
a
t
n
e
m

i
r
e
p
x
e

e
h
t

m
o
r
f

%
4
3

d
n
u
o
f

s
a
w

t
x
e
t

g
n
o
l

a

f
o

s
e
r
u
t
a
e
f

e
h
t

s
n
i
a
t
b
o
t
a
h
t

r
e
z
i
r

e
h
t

t
c
a
r
t
x
e

o
t

t
n
e
m
u
c
o
d

e
l
b
a
u
l
a
v

d
n
a

l
a
i
t
n
e
s
s
e

l
a
c
i
t
i
r
c

g
n
i
n
i
a
t
n
i
a
m

e
l
i
h
w
n
o
i
t
a
m
r
o
f
n
i

n
o
i
t
a
m
r
o
f
n
i

.
l
a

t
e

d
h
o
M

)
0
2
0
2
(

-
e
r
p

a
t
a
d

d
e
t
a
c
i
t
s
i
h
p
o
S

t
n
e
m

i
t
n
e
S

r
o
f

%
3
9

f
o

y
c
a
r
u
c
c
a

n
a

d
e
v
e
i
h
c
A

-
s
a
l
c

t
x
e
t

a

e
s
o
p
o
r
P

)
9
1
0
2
(

.
l
a

t
e

i
l

A

e
r
a

s
t
x
e
t

h
c
i
h
w
n
i

l
e
d
o
m
c
i
t
e
m
h
t
i
r
a

n
a

s
i

M
S
V

e
c
a
p
s

r
o
t
c
e
V

s
k
r
a
m
e
R

)
s
(
n
o
i
t
a
c
i
l
p
p
A

)
s
(
e
m
o
c
t
u
O

)
s
(
k
s
a
t

n
i
a

M

d
e
y
e
v
r
u
s

y
d
u
t
S

n
o
i
t
p
i
r
c
s
e
d

l
a
r
e
n
e
G

l
e
d
o
M

g
n
i
l
l
e
d
o
m
g
n
i
n
r
a
e
l

p
e
e
d

n
o

d
e
t
c
u
d
n
o
c

s
e
i
d
u
t
s

e
h
t

f
o
w
e
i
v
r
e
v
O

2
e
l
b
a
T

o
t

d
e
d
e
e
n

s
i

g
n
i
s
s
e
c
o
r
p

,
s
i
s
y
l
a
n
a

h
c
i
h
w

,
n
o
i
t
a
c
fi
i
s
s
a
l
c

t
n
e
m

i
t
n
e
s

n
o
i
t
a
c
fi
i
s
s
a
l
c

e
v
o
r
p
m

i

-
l
e
d
o
m
c
i
p
o
t

-
u
c
o
d

c
e
v
2
c
i
p
o
t

d
e
m
r
o
f
r
e
p
t
u
o

y
c
a
r
u
c
c
a

g
n
i
l

s
d
o
h
t
e
m
n
o
i
t
a
t
n
e
s
e
r
p
e
r

t
n
e
m

-
a
t
r
o
p
s
n
a
r
t

g
n
i
v
e
i
r
t
e
r

r
o
f

m
e
t
s
y
s

n
o
i
t
a
c
fi
i
s

m
o
r
f

t
n
e
m

i
t
n
e
s

n
o
i
t

s
t
e
s
a
t
a
d

n
o
i
t
a
t
r
o
p
s
n
a
r
t

h
t
i

w

d
n
a

g
n
i
k
r
o
w
t
e
n

l
a
i
c
o
s

s
e
t
i
s

s
w
e
n

s
t
n
e
m
e
l
e

r
o
t
c
e
v

e
h
T

.
s
r
o
t
c
e
v

s
a

d
e
t
n
e
s
e
r
p
e
r

f
o

e
c
n
a
c
fi
i
n
g
i
s

r
o
s
t
h
g
i
e
w
e
h
t

e
z
i
r
e
t
c
a
r
a
h
c

y
f
i
t
n
e
d
i

n
a
c

t
I

.
t
n
e
m
u
c
o
d
a

n
i
h
t
i

w
d
r
o
w
h
c
a
e

s
u
h
t

d
n
a

,
s
t
n
e
m
u
c
o
d

t
c
n
i
t
s
i
d

g
n
o
m
a

s
e
i
t
i
r
a
l
i

m
i
s

o
t

e
u
d

,
r
e
v
e
w
o
H

.

m
s
i
r
a
i
g
a
l
p

t
c
e
t
e
d

o
t

s
t
s
i
s
s
a

/
s
t
n
e
m
u
c
o
d

g
n
o
l

,
s
e
u
l
a
v

y
t
i
r
a
l
i

m
i
s
w
o
l

r
i
e
h
t

s
a
h
M
S
V
e
h
T

.
d
e
t
n
e
s
e
r
p
e
r

y
l
r
o
o
p

e
r
a

s
r
e
p
a
p

n
o
i
t
a
m
r
o
f
n
i

n
i

d
e
t
n
e
m
e
l
p
m

i

y
l
e
v
i
t
c
e
ff
e

n
e
e
b

s
n
o
i
t
a
c
i
l
p
p
a

r
e
h
t
o

g
n
o
m
a

,
l
a
v
e
i
r
t
e
r

d
n
a
g
n
i
r
e
t
l

fi

l
e
d
o
m

)

M
S
V

(

Deep learning modelling techniques: current progress,…1 3

13574

S. F. Ahmed et al.

y
l
n
o

n
a
c

l
e
d
o
m
e
h
t

,
n
o
i
t

-
a
m
r
o
f
n
i

h
t
p
e
d

e
s
i
c
e
r
p

D
3
w
o
l
l
a
h
s

e
c
u
d
o
r
p

s
t
l
u
s
e
r

n
o
i
t
c
e
t
e
d

e
c
n
a
r
a
e
p
p
a

n
i

s
n
o
i
t
a
i
r
a
V

-

-
fi
i
n
g
i
s

a

e
v
a
h

o
s
l
a

n
a
c

t
c
a
p
m

i

t
n
a
c

n
o
i
t

%
0
3
—
%
5
2

r
e
v
o

y
b

s
e
i
d
u
t
s

-
c
e
t
e
d

t
c
e
j
b
o
D
3
m
r
o
f

-
r
e
p

n
a
c

t
a
h
t

N
N
C
R

-

s
u
o
m
o
n
o
t
u
a

n
i

n
o
i
t

g
n
i
v
i
r
d

)
d

,
c

,
b

f
o

e
c
n
e
s
b
a

e
h
t

o
t

e
u
D

-

-
c
e
t
e
d
t
c
e
j
b
O

s
u
o
i
v
e
r
p

e
h
t

f
o

e
n
o

d
e
m
r
o
f
r
e
p
t
u
O

o
e
r
e
t
S
d
o
h
t
e
m
a

e
s
o
p
o
r
P

,
a
9
1
0
2
(

.
l
a

t
e

i

L

y
l
n
o

s
o
i
r
a
n
e
c
s

c
fi
i
c
e
p
s

n
o
i
t

%
8
.
8
+
o
t

p
u

l
e
d
o
m

y
t
e
i
r
a
v

a

n
i

n
o
i
t
c
e
t
e
d

s
n
i
a
m
o
d

e
g
a
m

i

f
o

n
o
i
t
a
t
p
a
d
a

n
i
a
m
o
d

t
c
e
j
b
o
r
o
f

d
o
h
t
e
m

o
t

e
l
b
a
t
p
a
d
a

s
i

l
e
d
o
m
e
h
T

-
c
e
t
e
d
t
c
e
j
b
O

N
N
C
R

-

r
e
t
s
a
f

e
h
t

d
e
m
r
o
f
r
e
p
t
u
O

d
e
s
i
v
r
e
p
u
s
n
u

n
a

y
l
p
p
A

)
b

,
a
8
1
0
2
(

.
l
a

t
e

n
e
h
C

m
o
d
n
a
r

e
h
t

y
l
n
o

d
e
n
i
m
a
x
E

-
n
o
i
t
a
c
o
L

h
p
a
r
g

e
n
i
l
e
s
a
b

e
h
t

s
m
r
o
f
r
e
p
t
u
O

h
p
a
r
g
r
e
p
y
h

a

p
o
l
e
v
e
D

h
p
a
r
g
r
e
p
y
h

e
h
t

n
i

k
l
a
w

l
a
i
c
o
s

d
e
s
a
b

h
t
w
o
r
g

e
g
a
r
e
v
a

n
a

s
g
n
i
d
d
e
b
m
e

n
o
i
t
c
i
d
e
r
p

n
o
i
t
a
c
o
l

r
o
f

k
r
o
w
t
e
n

-
c
e
p
s
e
r

,

%
2
3
.
5
2

d
n
a
%
5
9
.
2
3

f
o

d
o
h
t
e
m
g
n
i
d
d
e
b
m
e

r
o
f

c
e
V
2
N
S
B
L

.
l
a

t
e

g
n
a
Y

)
9
1
0
2
(

s
k
s
a
t

y
l
e
v
i
t

l
a
i
c
o
s

d
e
s
a
b
-
n
o
i
t
a
c
o
l

n
o
i
t
c
i
d
e
r
p

n
o
i
t
a
c
o
l

d
n
a

s
s
e
n
e
v
i
t
c
e
ff
e

k
s
a
t

p
i
h
s
d
n
e
i
r
f

d
e
c
n
a
h
n
e

t
a
h
t

a
t
a
d

k
r
o
w
t
e
n

w
o
l
s

y
l
e
v
i
t
a
r
a
p
m
o
C

-

-
s
a
l
c

t
n
a
l
P

,

%
3
.
6
8
f
o

y
c
a
r
u
c
c
a

n
a
d
n
u
o
F

t
a
h
t

t
e
N
f
a
e
L

t
c
u
r
t
s
n
o
C

.
l
a

t
e

é
r
r
a
B

-
y
a
l

y
r
a
m

i
r
p

e
e
r
h
t

f
o

d
e
s
i
r
p
m
o
c

s
i

l
e
d
o
m
N
N
C
A

l
a
n
o
i
t
u
l
o
v
n
o
C

s
k
r
a
m
e
R

)
s
(
n
o
i
t
a
c
i
l
p
p
A

)
s
(
e
m
o
c
t
u
O

)
s
(
k
s
a
t

n
i
a

M

d
e
y
e
v
r
u
s

y
d
u
t
S

n
o
i
t
p
i
r
c
s
e
d

l
a
r
e
n
e
G

l
e
d
o
M

)
d
e
u
n
i
t
n
o
c
(

2
e
l
b
a
T

)
h

2
3

t
u
o
b
a

k
o
o
t

g
n
i
n
i
a
r
t
(

n
o
i
t
a
c
fi
i
s

-
S
f
a
e
L
e
h
t

n
o
%
9
.
7
9

d
n
a

,

%
8
.
5
9

y
f
i
t
n
e
d
i

o
t

d
e
s
u

e
b

n
a
c

)
7
1
0
2
(

d
e
t
c
e
n
n
o
c

y
l
l
u
f

d
n
a

,
g
n
i
l
o
o
p

,
n
o
i
t
u
l
o
v
n
o
c

:
s
r
e

w
o
d
n
i
w
d
e
p
p
o
r
c

,
l
l
a
m

s

e
h
t

o
t

e
u
d
t
x
e
t
n
o
c

s
k
c
a
L
-

s
e
z
i
s

,
t
e
s
a
t
a
d

a
i
v
a
l
F
d
n
a

,
e
g
a
i
l
o
F

,
p
a
n

e
h
t

m
o
r
f

s
e
i
c
e
p
s

t
n
a
l
p

y
l
e
v
i
t
c
e
p
s
e
r

s
e
g
a
m

i

f
a
e
l

s
e
r
u
t
a
e
f

d
e
t
c
a
r
t
x
e

e
h
t

s
t
c
e
n
n
o
c

,
r
e
y
a
l

d
e
t
c
e
n
n
o
c

y
l
l
u
f

e
h
t

,
r
e
y
a
l

d
r
i
h
t

e
h
t

e
l
i
h
w

,
t
u
p
n
i

e
h
t

m
o
r
f

s
e
r
u
t
a
e
f

e
t
a
r
e
n
e
g
s
r
e
y
a
l

o
w

t

t
s
r
fi
e
h
T

.
s
r
e
y
a
l

-
c
u
d
e
r

r
o
f

l
a
i
c
fi
e
n
e
b

y
l
l
a
i
c
e
p
s
e

e
r
a

s
N
N
C

.
a
t
a
d

e
k
a
t

y
e
h
t

s
e
m

i
t
e
m
o
s

,
r
e
v
e
w
o
H

.
k
r
o
w
t
e
n

l
a
r
u
e
n

-
fi
i
s
s
a
l
c

t
x
e
t

,
n
o
i
t
c
e
t
e
d

t
c
e
j
b
o

n
i

d
e
s
u

y
l
l
a
c
i
p
y
t

e
r
a

s
l
e
d
o
m
e
s
e
h
T

.
a
t
a
d

n
i
a
r
t

o
t

e
m

i
t

r
e
g
n
o
l

a

l
a
i
c
fi

i
t
r
a

n
a

n
i

s
r
e
t
e
m
a
r
a
p

f
o

r
e
b
m
u
n
e
h
t

g
n
i

d
e
d
i
v
o
r
p

e
h
t

m
o
r
f

s
e
r
u
t
a
e
f

l
e
v
e
l
-
h
g
i
h

t
c
a
r
t
x
e

s
r
e
y
a
l

n
o
i
t
u
l
o
v
n
o
c

e
h
T

.
t
u
p
t
u
o
l
a
n
fi
e
h
t

o
t

s
i
s
y
l
a
n
a

t
n
e
m

i
t
n
e
s

d
n
a

n
o
i
t
a
c

)

N
N
C

(

k
r
o
w

-
t
e
n

l
a
r
u
e
n

1 3

13575

y
r
o
m
e
m

f
o

t
o
l

a

e
m
u
s
n
o
C

-

e
m

i
t

d
n
a

d
e
t
i

m

i
l

h
t
i

w
s
n
o
i
t

s
e
c
r
u
o
s
e
r

d
e
m
r
o
f
r
e
p
m
h
t
i
r
o
g
l
a

g
n
i
k
c
a
r
t

k
r
o
w
e
m
a
r
f
d
e
s
a
b
-
N
N
C

n
o
i
s
i
c
e
d

v
o
k
r
a

M
n
a
h
t

r
e
t
t
e
b

n
i

s
t
c
e
j
b
o

g
n
i
k
c
a
r
t

r
o
f

%
4

y
b
s
e
s
s
e
c
o
r
p

s
o
e
d
i
v

-
a
c
i
l
p
p
a

r
o
f

e
l
b
a
t
i
u
s
n
U

-

g
n
i
k
c
a
r
t

t
c
e
j
b
O

t
c
e
j
b
o
-
i
t
l
u
m
e
n
i
l
n
o

d
e
s
o
p
o
r
p

e
h
T

c
i
m
a
n
y
d

a

e
s
o
p
o
r
P

)
7
1
0
2
(

.
l
a

t
e

u
h
C

m
o
r
f

e
g
d
e
l
w
o
n
k

r
e
f
s
n
a
r
t

e
h
t

o
t

n
i
a
m
o
d

r
e
h
t
o
n
a

o
t

d
e
s
u

e
b

n
a
c

s
e
u
q
i
n

d
l
e
fi

l
a
c
i
d
e
m

t
u
o
b
a

y
b

s
d
o
h
t
e
m
d
e
s
a
b

g
n
i
d

r
o

"
n
i
a
r
B
"

s
a

h
c
u
s

%
5
1

"
r
e
c
n
a
C
"

n
o
i
t

-
d
e
b
m
e

d
r
o
w
e
h
t

o
t

d
e
r
a
p
m
o
c

,
s
e
i
r
o
g
e
t
a
c

6
2

f
o

e
n
o

)
7
1
0
2
(

-
h
c
e
T
n
o
i
t
a
t
p
a
d
A
n
i
a
m
o
D

-
a
c
fi
i
s
s
a
l
c

t
x
e
T

y
c
a
r
u
c
c
a

n
o
i
t
c
i
d
e
r
p
r
e
t
t
e
b

d
e
w
o
h
S

o
t
n
i

t
x
e
t

l
a
c
i
n
i
l
c

y
f
i
s
s
a
l
C

.
l
a

t
e

s
e
h
g
u
H

l
e
d
o
m
e
h
t

t
s
o
o
b

o
t

d
e
s
u

s
i
s
y
l
a
n
a

%
5
.
4
7

o
t

p
u
m
u
m

a
t
a
d

r
e
t
t
i

w
T
m
o
r
f

e
b

y
a
m
N
N
C

r
e
y
a
l
i
t
l
u
m
A

t
n
e
m

i
t
n
e
S

-
i
x
a
m
s
a
w
y
c
a
r
u
c
c
a

t
n
e
m
p
o
l
e
v
e
D

r
o
i
v
a
h
e
b
r
e
s
u

t
c
i
d
e
r
P

.
l
a

t
e

o
a
i
L

)
7
1
0
2
(

f
o

n
o
s
i
r
a
p
m
o
c

e
h
t

g
n
i
s
s
i

M

l
a
c
i
g
o
l
o
m
s
o
C

y
b

s
e
n
i
l
e
s
a
b
e
h
t

n
a
h
t

r
e
t
t
e
B

a

,
e
r
e
h
p
S
p
e
e
D
p
o
l
e
v
e
D

.
l
a

t
e

n
i
d
u
a
r
r
e
P

t
n
e
r
e
ff
i
d

h
t
i

w
s
n
o
i
t
a
t
n
e
m

-
e
l
p
m

i

N
N
C

l
a
c
i
r
e
h
p
s

s
e
u
q
i
n
h
c
e
t

g
n
i
l
p
m
a
s

y
c
a
r
u
c
c
a

s
u
o
i
r
a
v

o
t

e
r
e
h
p
S
p
e
e
D

s
i
s
y
l
a
n
a

a
t
a
d

n
o
i
t
a
c
fi
i
s
s
a
l
c

f
o

s
m
r
e
t

n
i

%
0
1

-
u
l
o
v
n
o
c

d
e
s
a
b
-
h
p
a
r
g

k
r
o
w
t
e
n

l
a
r
u
e
n

l
a
n
o
i
t

d
n
a

p
a
m
a
m
o
r
f

s
s
a
l
c

m
o
r
f

s
l
e
x
i
p

y
f
i
s
s
a
l
c

a
t
a
d

l
a
c
i
g
o
l
o
m
s
o
c

a

t
c
i
d
e
r
p

n
a
c

t
a
h
t

)
9
1
0
2
(

-
n
r
a
e
l

e
n
i
h
c
a
m
R
A
S
n
I

e
h
T

c
i
t
e
h
t
n
y
S

,
s
d
o
h
t
e
m
d
e
t
a
l
e
r

e
h
t

o
t

d
e
r
a
p
m
o
C

d
e
s
a
b
-
N
N
C
a

t
c
u
r
t
s
n
o
C

.
l
a

t
e

e
e
j
r
e
h
k
u
M

y
b

d
e
v
o
r
p
m

i

e
b

n
a
c

g
n
i

o
t

y
t
i
l
i
b
a

s
’
R
A
S
n
I
n
e
G

-
o
r
e
f
r
e
t
n
i

w
e
n

e
c
u
d
o
r
p

s

m
a
r
g

n
o
i
t
u
b
i
r
t
s
i
d

e
r
e
w
R
A
S
n
I
n
e
G

f
o

r
o
r
r
e
-
e
r
a
u
q
s

d
n
a

7
0
.
0

,
5
0
.
0

y
b

d
e
v
o
r
p
m

i

y
l
e
v
i
t
c
e
p
s
e
r

,
4
5
.
0

-
r
e
h
o
c

d
e
n
i
b
m
o
c

r
o
f

d
n
a

n
o
i
t
a
m

i
t
s
e

e
c
n
e

h
c
i
h
w
g
n
i
r
e
t
l

fi
e
s
a
h
p

-
r
e
t
n
i

s
n
r
a
e
l

y
l
t
c
e
r
i
d

c
i
t
e
h
t
n
y
s

c
i
r
t
e
m
o
r
e
f

)

R
A
S
n
I
(

r
a
d
a
r

e
r
u
t
r
e
p
a

n
o
i
t
u
b
i
r
t
s
i
d

a
t
a
d

a
t
a
d
r
a
d
a
r

e
r
u
t
r
e
p
a

-
n
a
e
m

-
t
o
o
r

e
s
a
h
p

d
n
a

e
c
n
e
r
e
h
o
c

,
”
R
A
S
n
I
n
e
G
“

y
l
e
m
a
n

,
r
o
r
r
e

e
n
i
s
o
c

e
s
a
h
p

e
h
t

,
l
e
d
o
m
e
v
i
t
a
r
e
n
e
g

)
0
2
0
2
(

s
k
r
a
m
e
R

)
s
(
n
o
i
t
a
c
i
l
p
p
A

)
s
(
e
m
o
c
t
u
O

)
s
(
k
s
a
t

n
i
a

M

d
e
y
e
v
r
u
s

y
d
u
t
S

n
o
i
t
p
i
r
c
s
e
d

l
a
r
e
n
e
G

l
e
d
o
M

)
d
e
u
n
i
t
n
o
c
(

2
e
l
b
a
T

Deep learning modelling techniques: current progress,…1 3

13576

S. F. Ahmed et al.

-
a
c
fi
i
s
s
a
l
c

t
n
e
m

i
t
n
e
s

e
t
a
g

d
n
a

e
c
n
e
t
n
e
s

e
h
t

t
a

n
o
i
t

-
i
t
s
e
v
n
i
o
t

l
a
i
t
n
e
t
o
p
s
i

e
r
e
h
T

s
l
e
v
e
l

t
c
e
p
s
a

s
i
s
y
l
a
n
a

t
n
e
m

i
t
n
e
S

n
i

s
t
e
s
a
t
a
d
w
e
i
v
e
r

g
n
o
l

e
v
fi
r
o
f

y
c
a
r
u
c
c
a

f
o

s
m
r
e
t

t
r
o
h
s

s
a

l
l
e
w
s
a

s
w
e
i
v
e
r

e
h
t

t
u
o

d
n
fi
n
a
c

t
a
h
t

g
n
o
l

m
o
r
f

t
n
e
m

i
t
n
e
s

t
x
e
t

t
e
e
w

t

%
3
6
.
3

o
t

%
5
8
.
1
m
o
r
f

d
e
v
o
r
p
m

I

l
e
d
o
m
N
N
R
N
N
C
d
l
i
u
B

-

.
l
a

t
e

i
r
i
s
a
B

)
1
2
0
2
(

-
n
i
a
r
t

r
o
f

g
n
i
m
u
s
n
o
c
-
e
m
T

i

-
c
e
t
e
d

n
o
i
t
o
m
E

-
h
t
e
m
e
n
i
l
e
s
a
b

e
h
t

d
e
m
r
o
f
r
e
p
t
u
O

-
a
i
D
d
e
c
u
d
o
r
t
n
I

.
l
a

t
e

r
e
d
m
u
j
a

M

-
r
e
t
e
m
a
r
a
p
t
o
n

d
n
a

g
n
i

r
o

l
a
b
o
l
g

r
o
f

t
n
e
i
c
ffi
e

s
t
x
e
t
n
o
c

l
a
c
o
l

n
o
i
t

r
e
h
g
i
h
%
2
6
.
6

a

g
n
i
v
e
i
h
c
a

y
b

s
d
o

e
g
a
r
e
v
a

n
o

e
r
o
c
s
-
1
F

n
o
i
t
o
m
e

r
o
f

m
s
i
n
a
h
c
e
m

e
n
o

h
t
i

w
s
n
o
i
t
a
s
r
e
v
n
o
c

s
l
e
b
a
l

n
o
i
t
o
m
e

x
i
s

f
o

l
a
u
t
x
e
t

n
i

n
o
i
t
c
e
t
e
d

n
o

t
l
i
u
b
N
N
R
e
u
g
o
l

n
o
i
t
n
e
t
t
a

h
t
i

w
N
N
R

)
9
1
0
2
(

y
t
i
d
i
l
a
v

s
’
s
i
s
e
h
t
o
p
y
h

s
i
h
t

t
u
b

,
n
o
i
t
a
t
n
e
s
e
r
p
e
r

e
r
u
t

d
e
t
a
u
l
a
v
e

t
o
n

s
a
w

n
o
i
t
a
l
s
n
a
r
t

c
i
r
t
a
m

g
n
i
m
r
o
f
r
e
p

e
n
o
e
m
o
s

f
o

s
n
g
i
s

s
u
o
u
n
i
t
n
o
c

e
n
i
h
c
a
m

E
G
U
O
R
e
h
t

n
o

0
8
.
3
4

d
n
a

c
i
r
t
a
m

o
e
d
i
v

a
m
o
r
f

s
e
r
u
t
s
e
g

)
8
1
0
2
(

-
a
e
f

d
o
o
g

n
r
a
e
l

d
l
u
o
c
N
N
C

l
a
r
u
e
N

4
-
U
E
L
B
e
h
t

n
o

3
1
.
8
1

d
e
r
o
c
S

e
g
a
u
g
n
a
l

n
g
i
s

e
z
i
n
g
o
c
e
R

.
l
a

t
e

z
o
g
m
a
C

-
e
e
r
t

g
n
i
s
u

s
t
n
e
m
u
c
o
d

e
h
t

t
n
e
s
e
r
p
e
r

o
t

e
l
b
i
s
s
o
p

s
i

t
I

-

M
T
S
L
d
e
r
u
t
c
u
r
t
s

s
t
n
e
m
u
c
o
d

e
h
t

f
o
r
e
d
r
o

l
a
i
t
n
e
u
q
e
s

e
h
t

y
l
n
o

d
e
r
e
d
i
s
n
o
C

-

s
i
s
y
l
a
n
a

t
n
e
m

i
t
n
e
S

n
a
h
t

e
c
n
a
m
r
o
f
r
e
p
r
e
t
t
e
b

d
e
w
o
h
S

r
o
f

s
t
x
e
t

g
n
o
l

l
e
d
o
M

n
a

g
n
i
n
i
a
t
b
o

y
b

s
l
e
d
o
m

r
e
h
t
o

%
9
.
3
6

d
n
a
%
4
4
f
o

y
c
a
r
u
c
c
a

t
n
e
m

i
t
n
e
s

r
o
f

s
e
c
n
e
t
n
e
s

c
i
t
n
a
m
e
s

g
n
i
t
a
r
e
n
e
g

n
e
e
w
t
e
b

s
n
o
i
t
a
l
e
r

s
i
s
y
l
a
n
a

)
b

,
a
8
1
0
2
(

.
l
a

t
e

o
a
R

.

G

r
e
w
o
l
s

e
v
e
i
h
c
a

o
t

r
a
e
p
p
a

g
n
i
l
l
e
d
o
m

d
e
s
a
b
-
M
T
S
L
d
r
a
d
n
a
t
s

o
t

%
8
7
.
7
3

s
e
i
r
e
s

e
m

i
t

n
i

M
T
S
L
B

i

)
9
1
0
2
(

.
l
a

t
e

-
n
e
u
q
e
s

d
e
d
r
o
c
e
r

n
o
i
t
a
m
r
o
f
n
i

l
l
a

g
n
i
r
u
t
p
a
c

f
o

k
r
o
w
t
e
n

l
a
r

s
l
e
d
o
m
d
e
s
a
b
M
T
S
L
B

i

s
e
i
r
e
s

e
m
T

i

y
b

y
c
a
r
u
c
c
a

g
n
i
t
s
a
c
e
r
o
f

d
e
c
n
a
h
n
E

d
n
a

M
T
S
L
e
r
a
p
m
o
C

i
n
i
m
a
N

-
i

m
a
i
S

e
l
b
a
p
a
c

s
e
i
r
o
m
e
m
h
t
i

w
s
k
r
o
w
t
e
n

l
a
r
u
e
n

e
r
a

s
N
N
R

-
u
e
n

t
n
e
r
r
u
c
e
R

s
k
r
a
m
e
R

)
s
(
n
o
i
t
a
c
i
l
p
p
A

)
s
(
e
m
o
c
t
u
O

)
s
(
k
s
a
t

n
i
a

M

d
e
y
e
v
r
u
s

y
d
u
t
S

n
o
i
t
p
i
r
c
s
e
d

l
a
r
e
n
e
G

l
e
d
o
M

)
d
e
u
n
i
t
n
o
c
(

2
e
l
b
a
T

e
h
t

n
a
h
t

e
c
n
a
m
r
o
f
r
e
p

s
l
e
d
o
m
d
e
s
a
b
-
M
T
S
L

s
l
e
d
o
m

g
n
i
l
l
e
d
o
m
a
t
a
d

n
i

s
u
o
e
g
a
t
n
a
v
d
a

s
i

t
I

.
t
i
n
u

g
n
i
d
e
c
e
r
p

e
h
t

n
i

y
l
l
a
i
t

)

N
N
R

(

t
n
i
o
p

t
h
g
i
l
h
g
i
h

e
h
t

e
c
n
i
s

s
e
i
r
e
s

e
m

i
t

g
n
i
t
s
a
c
e
r
o
f

s
N
N
R

.
s
t
u
p
n
i

s
u
o
i
v
e
r
p

f
o

r
e
d
n
i
m
e
r

a

s
a

s
k
r
o
w

e
h
t

e
t
u
c
e
x
e

y
e
h
t

t
a
h
t

t
c
a
f

e
h
t

o
t

e
u
d

l
u
f
e
s
u

e
r
a

.
t
n
e
m
e
l
e

e
c
n
e
u
q
e
s

h
c
a
e

r
o
f

n
o
i
t
a
t
u
p
m
o
c

e
m
a
s

g
n
i
d
o
l
p
x
e

d
n
a

t
n
e
i
d
a
r
g
m
o
r
f

r
e
ff
u
s
y
e
h
t

t
u
B

s
e
c
n
e
u
q
e
s

r
e
g
n
o
l

s
t
i

m

i
l

h
c
i
h
w

,
s
e
u
s
s
i

g
n
i
h
s
i
n
a
v

1 3

-
r
o
t
i
n
o
m

r
o
i
v
a
h
e
b

n
a
m
u
h

-
r
e
d
i
s
n
o
c

h
t
i

w
m
e
t
s
y
s

g
n
i

n
a
m
u
h

x
e
l
p
m
o
c

e
r
o
m
g
n
i

e
m

i
t
-
l
a
e
r

a

p
o
l
e
v
e
d

o
t

s
e
i
t
i
v
i
t
c
a

e
r
a
c

h
t
l
a
e
h

s
m
e
t
s
y
s

e
r
o
c
s
-
1
F
d
n
a

,
l
l
a
c
e
r

,
n
o
i
s
i
c
e
r
p

g
n
i
s
u
%
9
9

s
a

d
e
r
u
s
a
e
m

k
r
o
w
t
e
n

n
o
i
s
u
f

a
t
a
d

n
a
m
u
h

e
z
i
n
g
o
c
e
r

o
t

s
e
c
i
r
t
a
m

r
o
i
v
a
h
e
b

d
n
a

s
e
i
t
i
v
i
t
c
a

d
e
d
n
e
t
x
e

e
b

n
a
c

k
r
o
w
e
h
T

t
n
e
g
i
l
l
e
t
n
I

s
a
w
e
c
n
a
m
r
o
f
r
e
p

e
g
a
r
e
v
a

e
h
T

s
r
o
s
n
e
s
-
i
t
l
u
m
a

t
n
e
s
e
r
P

.
l
a

t
e

n
i
d
d
U

)
0
2
0
2
(

f
o

e
c
n
a
m
r
o
f
r
e
p

e
h
t

t
s
o
o
b

l
e
d
o
m
e
h
t

o
t

d
e
s
u

e
b

n
a
c

s
r
e
y
a
l

M
T
S
L
n
e
d
d
i
h

e
l
p
i
t
l
u
M

g
n
i
l
l
e
d
o
m

s
e
i
r
e
s

e
m
T

i

d
n
a
)
6
1
5
.
 0
 =
E
S
M
R

(

l
e
d
o
m
N
N
R

)
3
9
7
.
0
=
E
S
M
R

(
d
o
h
t
e
m
e
v
i
a
n

s
d
o
i
r
e
p
w
o
fl
-
w
o
l

l
a
c
i
g
o
l
o
r
d
y
h
n
o
)
7
8
4
.
0
=
E
S
M
R

(

-
e
r
o
f

o
t

-

N
N
R
M
T
S
L
f
o

l
a
n
o
i
t
i
d
a
r
t
e
h
t
d
e
m
r
o
f
r
e
p
t
u
o
a
t
a
d

g
n
i
r
u
d

s
w
o
fl
y
l
i
a
d

t
s
a
c

e
c
n
a
m
r
o
f
r
e
p
l
e
d
o
m
N
N
R
M
T
S
L

-

y
t
i
l
i
b
a
c
i
l
p
p
a

e
h
t

e
z
y
l
a
n
A

.
l
a

t
e

o
o
h
a
S

)
9
1
0
2
(

e
k
a
t

y
a
m

l
e
d
o
m
e
h
T

n
o
o
h
p
y
T

n
a
e
m
e
h
t

,

Y
D
N
A
S
e
n
a
c
i
r
r
u
h
r
o
F

-
n
o
c

y
l
l
u
f

a

e
s
o
p
o
r
P

.
l
a

t
e

y
n
a
m
e
l
A

e
h
t

e
c
u
d
e
r

o
t

s
e
t
a
n
i
d
r
o
o
c

r
o
r
r
e

n
o
i
s
r
e
v
n
o
c

-
t
r
e
v
n
o
c

f
o

e
g
a
t
n
a
v
d
a

s
n
o
i
t
a
c
o
l

d
i
r
g

e
h
t

g
n
i

e
d
u
t
i
g
n
o
l
–
e
d
u
t
i
t
a
l

o
t

e
h
t

n
a
h
t

r
e
t
t
e
b

s
i

)
2
4
8
0
.
0
(

l
e
d
o
m

s
e
i
r
o
t
c
e
j
a
r
t

e
n
a
c
i
r
r
u
h

e
g
a
r
e
v
a
N
N
R
e
s
r
a
p
s

s
u
o
i
v
e
r
p

e
n
o
l
c
y
c

l
a
c
i
r
o
t
s
i
h
m
o
r
f

l
e
d
o
m

)
2
1
6
4
.
0
(

n
r
a
e
l

d
l
u
o
c

t
a
h
t

a
t
a
d

-
r
u
h

f
o

s
e
p
y
t

l
l
a
m
o
r
f

s
e
n
a
c
i
r

n
o
i
t
c
i
d
e
r
p

N
N
R
e
h
t

m
o
r
f

r
o
r
r
e

e
t
u
l
o
s
b
a

t
c
i
d
e
r
p

o
t

N
N
R
d
e
t
c
e
n

)
9
1
0
2
(

s
k
r
a
m
e
R

)
s
(
n
o
i
t
a
c
i
l
p
p
A

)
s
(
e
m
o
c
t
u
O

)
s
(
k
s
a
t

n
i
a

M

d
e
y
e
v
r
u
s

y
d
u
t
S

n
o
i
t
p
i
r
c
s
e
d

l
a
r
e
n
e
G

l
e
d
o
M

)
d
e
u
n
i
t
n
o
c
(

2
e
l
b
a
T

13577

d
e
r
u
t
c
u
r
t
s

e
h
t

o
t
n
i

d
e
d
d
a

t
s
o
o
b

o
t

,
s
e
i
t
r
e
p
o
r
p

r
e
s
u

g
n
i
n
r
a
e
l

n
o
i
t
a
t
n
e
s
e
r
p
e
r

s
a

h
c
u
s

,
s
l
e
d
o
m

l
a
r
u
e
n

r
e
h
t
r
u
f

n
e
v
e

d
e
d
e
e
c
x
e

e
h
t

e
r
e
h
w
s
y
a
d

e
h
t

y
l
n
o

f
i

d
e
s
a
e
r
c
e
d

s
i

d
e
r
e
d
i
s
n
o
c

e
r
a

s
t
i

m

i
l

y
c
a
r
u
c
c
a

n
o
i
t
c
i
d
e
r
p

l
a
u
t
c
A

d
n
a

0
1
M
P

g
n
i
t
s
a
c
e
r
o
F

5
.
2
M
P

e
h
t

f
o
%
5
9

d
e
t
c
i
d
e
r
p

y
l
t
c
e
r
r
o
C

c
i
r
e
h
p
s
o
m
t
a

e
z
y
l
a
n
A

.
l
a

t
e

e
r
o
fi
o
c
n
a
i
B

y
d
u
t
s

s
i
h
t

n
i

d
e
z
y
l
a
n
a

s
y
a
d

d
n
a

,
r
e
t
t
a
m
e
t
a
l
u
c
i
t
r
a
p

)
7
1
0
2
(

d
e
g
a
r
e
v
a

y
l
i
a
d

t
s
a
c
e
r
o
f

0
1
M
P
f
o

n
o
i
t
a
r
t
n
e
c
n
o
c

o
t

e
n
o
m
o
r
f

5
.
2
M
P
d
n
a

d
a
e
h
a

s
y
a
d

e
e
r
h
t

n
o

n
o
i
t

r
e
t
t
i

w
T

-
u
c
c
A

.
e
g
a
t
s

y
l
r
a
e

n
a

t
a

s
r
o
m
u
r

s
t
e
s
a
t
a
d
t
n
e
r
e
ff
i
d

o
w

t

n
o

y
c
a
r

n
o

d
e
s
a
b

,
n
o
i
t
c
e
t
e
d

r
o
m
u
r

r
o
f

s
l
e
d
o
m

g
n
i
t
s
i
x
e

r
e
h
t
o

n
a
h
t

r
e
t
t
e
b

,

%
7
.
3
7

s
e
h
c
a
o
r
p
p
a

d
e
r
u
t
c
u
r
t
s
-
e
e
r
t

p
u

s
k
r
o
w
t
e
n
l
a
r
u
e
n

d
n
a
%
3
.
2
7

s
a

d
e
t
a
l
u
c
l
a
c

s
a
w

-

m
o
t
t
o
b

d
n
a

n
w
o
d
-
p
o
t

e
g
a
m

i

,
)
P
L
N

(

g
n
i
s
s
e
c
o
r
p

e
g
a
u
g
n
a
l

l
a
r
u
t
a
n

n
i

r
e
h
t
o

g
n
o
m
a

,
s
e
i
g
o
l
o
p
o
t

n
i
e
t
o
r
p

d
n
a

,
s
i
s
y
l
a
n
a

s
e
e
r
t

e
s
r
a
p

o
t

l
u
f
e
s
u
s
i

d
n
a

s
t
u
p
n
i

d
e
r
u
t
c
u
r
t
s

s
n
o
i
t
a
c
i
l
p
p
a

n
i
a
m
o
d

d
e
r
u
t
c
u
r
t
s

s
k
s
a
t

d
e
t
a
l
e
r
-
P
L
N
n
i

l
l
e
w
y
l
l
a
n
o
i
t
p
e
c
x
e

s
k
r
o
w

t
I

k
r
o
w
t
e
n

l
a
r

)

N
N
v
R

(

e
b

n
a
c

a
t
a
d
f
o

s
e
p
y
t

r
e
h
t
O

-
c
e
t
e
d

r
o
m
u
R

y
f
i
t
n
e
d
i

o
t

y
t
i
l
i
b
a

g
n
o
r
t
s

a

d
e
w
o
h
S

e
v
i
s
r
u
c
e
r

o
w

t

p
o
l
e
v
e
D

)
8
1
0
2
(

.
l
a

t
e

a

M

n
o

s
e
t
a
r
e
p
o

t
a
h
t

l
e
d
o
m

r
a
e
n
i
l
n
o
n

a

s
i

N
N
v
R

-
u
e
n

e
v
i
s
r
u
c
e
R

Deep learning modelling techniques: current progress,…1 3

13578

S. F. Ahmed et al.

e
v
i
t
c
e
ff
e

g
n
i
s
u

a
t
a
d

g
i
b

d
e
s
a
b
-
D
G
S
h
c
t
a
b
-
i
n
i
m

o
t

d
e
l
a
c
s

e
b

n
a
c

y
d
u
t
s

g
n
i
n
r
a
e
l

n
o
i
t

s
e
s
a
b
a
t
a
d

e
e
r
h
t

n
o

y
c
a
r
u
c
c
a

,

E
I
P

i
t
l
u
M

-

,
0
.
2
S
I
V
R
N
A
I
S
A
C

I

W
F
L
d
n
a

e
c
a
f

f
o

n
o
i
t
a
n
i
b
m
o
c

s
e
r
u
t
a
e
f

n
o
i
t
i
n
g
o
c
e
r

e
t
u
b
i
r
t
t
a

l
a
i
c
a
f

d
n
a

e
v
o
r
p
m

i
n
a
c

s
e
r
u
t
a
e
f

-
r
e
p

n
o
i
t
i
n
g
o
c
e
r

e
c
a
f

t
n
e
r
e
ff
i
d

n
i

s
e
c
n
a
m
r
o
f

s
e
g
n
e
l
l
a
h
c

-
d
o
m
g
n
i
r
e
w
s
n
a

n
o
i
t
s
e
u
q

n
o
i
t
a
c
fi

i
r
e
v
r
e
h
t
r
u
f

r
o
f

s
l
e

y
l
e
v
i
t

-
c
e
p
s
e
r

s
l
e
d
o
m
N
A
T
U
M
d
n
a

g
n
i
r
e
w
s
n
a

n
o
i
t

l
a
u
s
i
v

e
r
o
m
o
t

d
e
i
l
p
p
a

g
n
i
r
e
w
s
n
a

B
L
M
g
n
i
t
s
i
x
e

n
a
h
t

%
0
7
.
1

d
n
a

-
s
e
u
q
l
a
u
s
i
v
r
o
f

N
T
N

e
b

d
l
u
o
c

d
o
h
t
e
m

s
i
h
T

n
o
i
t
s
e
u
q

l
a
u
s
i
V

%
8
9
.
1

f
o

e
c
n
a
m
r
o
f
r
e
p

d
e
s
a
e
r
c
n
I

n
o
i
t
n
e
t
t
a

p
e
e
d

p
o
l
e
v
e
D

)
8
1
0
2
(

.
l
a

t
e

i
a
B

e
h
t

n
i

d
e
s
u

h
c
a
o
r
p
p
a

e
h
T

-
i
n
g
o
c
e
r

e
c
a
F

%
0
0
1
t
s
o
m
l
a

d
e
n
i
a
t
b
o
l
e
d
o
m
e
h
T

e
h
t

w
o
h

e
t
a
r
t
s
n
o
m
e
D

)
7
1
0
2
(

.
l
a

t
e

u
H

e
l
u
d
o
m
e
t
a
r
a
p
e
s

y
l
e
v
i
t
c
e
p
s
e
r

,

%
1
.
4
6

d
n
a

7
.
3
6

a

f
o

e
s
u

e
h
t

h
t
i

w
d
e
d
i
o
v
a

e
b

y
a
m
h
c
i
h
w
d
e
t
c
e
t
e
d

s
d
n
u
o
p
m
o
c

s
e
n
e
g

d
n
a

t
a

d
e
t
a
l
u
c
l
a
c

e
r
e
w

l
e
d
o
m
N
N
I
P
S

s
e
n
e
g

d
n
a

s
d
n
u
o
p
m
o
c

e
h
t

d
n
a

g
n
i
s
s
e
c
o
r
p
-
e
r
p

a
r
t
x
e

l
a
c
i
m
e
h
c

n
e
e
w
t
e
b

)
8
1
0
2
(

t
o
n

s
i

n
o
i
t
a
n
i
d
r
o
o
C

l
a
c
i
m
e
h
C

g
n
i
d
u
l
c
n
i

l
e
d
o
m
e
h
t

r
o
f

s
e
r
o
c
s

-
F

s
p
i
h
s
n
o
i
t
a
l
e
r

t
c
a
r
t
x
E

g
n
a
K
d
n
a
m
L

i

x
e
l
p
m
o
c

e
r
o
m
e
l
d
n
a
h

n
a
c

r
o
s
n
e
t

h
t
i

w
s
n
o
i
t
c
a
r
e
t
n
i

g
n
i
t
s
i
x
e

n
a
h
t

s
r
e
y
a
l

s
l
e
d
o
m

g
n
i
r
e
w
s
n
a

n
o
i
t
s
e
u
q

e
s
e
n
i
h
C
d
n
a

h
s
i
l
g
n
E

,
s
t
e
s

n
o
i
t
s
e
u
q

d
e
s
a
b

d
n
a
g
n
i
l
l
e
d
o
m
e
c
n
e
t
n
e
s

o
t
n
i

g
n
i
h
c
t
a
m
c
i
t
n
a
m
e
s

g
n
i
t
a
r
g
e
t
n
i

,
g
n
i
r
e
w
s
n
a

l
e
d
o
m
e
n
o

-
i
r
a
v

n
i

l
u
f
s
s
e
c
c
u
s

n
e
e
b

e
v
a
h
s
N
T
N

.
r
o
s
n
e
t

a

o
t

s
n
o
i
t
a
c
i
l
p
p
a

g
n
i
s
s
e
c
o
r
p

e
g
a
u
g
n
a
l

l
a
r
u
t
a
n

s
u
o

-
u
p
m
o
c

s
i

t
i

,
e
v
i
t
c
e
ff
e

s
i

l
e
d
o
m
N
T
N
e
h
t

h
g
u
o
h
t
l

A

e
v
i
s
n
e
t
n
i

y
l
l
a
n
o
i
t
a
t

d
e
s
a
b

-
a
t
a
d
s
e
g
a
u
g
n
a
l

t
n
e
r
e
ff
i
d

o
w

t

n
o

-
y
t
i
n
u
m
m
o
c

r
o
f

N
T
N

)
5
1
0
2
(

s
r
o
t
c
e
v

t
u
p
n
i

o
w

t

t
c
e
n
n
o
c

y
l
t
c
e
r
i
d

n
a
c
N
T
N

,
s
l
e

k
r
o
w
t
e
n

)

N
T
N

(

N
T
N

l
a
n
o
i
t
u
l
o
v
n
o
c

e
h
T

-
y
t
i
n
u
m
m
o
C

s
t
r
a
-
e
h
t
-
f
o
-
e
t
a
t
s

e
h
t

d
e
m
r
o
f
r
e
p
t
u
O

l
a
n
o
i
t
u
l
o
v
n
o
c

a

t
c
u
r
t
s
n
o
C

g
n
a
u
H
d
n
a

u
i
Q

-
d
o
m
k
r
o
w
t
e
n

l
a
r
u
e
n

l
a
n
o
i
t
n
e
v
n
o
c

o
t

t
s
a
r
t
n
o
c

n
I

r
o
s
n
e
t

l
a
r
u
e
N

s
k
r
a
m
e
R

)
s
(
n
o
i
t
a
c
i
l
p
p
A

)
s
(
e
m
o
c
t
u
O

)
s
(
k
s
a
t

n
i
a

M

d
e
y
e
v
r
u
s

y
d
u
t
S

n
o
i
t
p
i
r
c
s
e
d

l
a
r
e
n
e
G

l
e
d
o
M

)
d
e
u
n
i
t
n
o
c
(

2
e
l
b
a
T

t
r
o
ff
e

l
a
n
o
i
t
a
t
u
p
m
o
c

t
n
a
c

a

g
n
i
d
l
i
u
b

,
e
r
a
w
d
r
a
h

n
o

d
e
d
i
a
-
r
e
t
u
p
m
o
c

e
f
i
l
-
l
a
e
r

e
t
i
u
q

s
i

m
e
t
s
y
s

s
i
s
o
n
g
a
i
d

g
n
i
g
n
e
l
l
a
h
c

n
o
i
t
c
e
t
e
d

-
s
i

W

e
h
t

n
o
%
8
6
.
9
9

s
a

d
e
t
a
u
l
a
v
e

-
t
h
g
i
e
w
a

h
g
u
o
r
h
t

)
6
1
0
2
(

b
i
e
d
l
E

d
e
s
u
s
i

N
B
D
e
h
T

.
d
e
z
i
l
i
t
u

y
l
l
a
c
i
p
y
t

s
i

)
s

M
B
R

(

t
e
s
a
t
a
d
r
e
c
n
a
c

t
s
a
e
r
b

n
i
s
n
o
c

-
a
p
o
r
p
k
c
a
b

d
e
z
i
l
a
i
t
i
n
i

k
r
o
w
t
e
n
l
a
r
u
e
n

n
o
i
t
a
g

N
B
D
d
e
n
i
a
r
t

a
m
o
r
f

-
i
h
c
r
a

l
a
c
i
t
n
e
d
i

g
n
i
v
a
h

e
r
u
t
c
e
t

e
h
t

s
a
g
n
i
v
r
e
s

k
r
o
w
t
e
n

h
c
a
e

f
o

r
e
y
a
l

n
e
d
d
i
h

e
h
t

h
t
i

w

,
s
k
r
o
w
t
e
n

d
e
s
i
v
r
e
p
u
s
n
u

e
l
p
i
t
l
u
m
k
c
a
t
s

o
t

e
h
t

s
a
h
M
B
R
e
h
T

.
r
e
y
a
l

t
n
e
u
q
e
s
b
u
s

e
h
t

r
o
f

t
u
p
n
i

s
c
i
t
s
i
r
e
t
c
a
r
a
h
c

e
l
p
m
a
s

g
n
i
t
t

fi
f
o

e
g
a
t
n
a
v
d
a

k
r
o
w
t
e
n

)

N
B
D

(

-
fi
i
n
g
i
s

s
e
r
i
u
q
e
r

N
B
D
e
c
n
i
S

r
e
c
n
a
c

t
s
a
e
r
B

s
a
w

l
e
d
o
m
e
h
t

f
o

y
c
a
r
u
c
c
a

e
h
T

r
e
c
n
a
c

t
s
a
e
r
b

e
s
o
n
g
a
i
D

d
n
a

r
e
h
a
Z
-
l
e
d
b
A

s
e
n
i
h
c
a
m
n
n
a
m
z
t
l
o
B
d
e
t
c
i
r
t
s
e
r

f
o

k
c
a
t
s

a

,

N
B
D
n
I

f
e
i
l
e
b

p
e
e
D

1 3

-
i
s
s
a
l
c

k
a
e
w
a

f
o

y
g
e
t
a
r
t
s

t
n
a
c
fi
i
n
g
i
s

e
s
u
a
c

y
a
m

r
e
fi

-
o
d
u
e
s
p

n
i

e
c
n
a
i
r
a
v

d
e
n
r
e
v
o
g

s
i

t
i

s
a

g
n
i
l
l
e
b
a
l

e
m
o
S

.
s
r
o
b
h
g
i
e
n

d
e
x
fi
y
b

e
b

n
a
c

s
e
i
g
e
t
a
r
t
s

e
v
i
t
p
a
d
a

c
fi
i
c
e
p
s

k
c
i
p

o
t

d
e
w
o
l
l
o
f

e
h
t

g
n
i
n
i
a
r
t

r
o
f

s
e
l
p
m
a
s

s
r
e
fi
i
s
s
a
l
c

k
a
e
w

g
n
i
n
i
a
r
t

e
h
t

f
o

s
s
e
c
o
r
p

n
o
i
t
a
c
fi
i
s
s
a
l
c

t
r
a
-
e
h
t
-
f
o
-
e
t
a
t
s

d
e
m
a
n

e
u
q
i
n
h
c
e
t

g
n
i

N
B
D

t
n
a
n
i
m

i
r
c
s
i
d

e
r
u
t
r
e
p
a

c
i
t
e
h
t
n
y
s

r
o
f

e
g
a
m

i

)

R
A
S
(

r
a
d
a
r

n
o
i
t
a
c
fi
i
s
s
a
l
c

n
o
i
t
c
e
l
e
s

r
o
b
h
g
i
e
n

e
h
T

e
g
a
m

i

R
A
S

e
h
t

d
e
m
r
o
f
r
e
p
t
u
o

y
l
t
n
a
c
fi
i
n
g
i
S

-
n
r
a
e
l

e
r
u
t
a
e
f

a

e
s
o
p
o
r
P

.
l
a

t
e

o
a
h
Z

)
7
1
0
2
(

y
b

d
e
v
o
r
p
m

i

r
e
h
t
r
u
f

e
b

d
e
n
i
b
m
o
c

e
h
t

g
n
i
n
g
i
s
e
d

n
a
c

e
c
n
a
m
r
o
f
r
e
p

n
o
i
t

p
e
e
d

l
a
i
t
a
p
s
-
l
a
r
t
c
e
p
s

s
k
r
o
w
t
e
n

d
l
o
f
i
n
a
m

g
n
i
g
a
m

i

s
e
n
i
P
n
a
i
d
n
I

d
n
a

a
n
a
w
s
t
o
B

,
s
a
n

,

%
5
3
.
7
9

,

%
8
4
.
0
9

h
c
a
e
r

s
t
e
s
a
t
a
d

o
t

N
B
D

-
i
t
l
u
m
d
e
s
a
b

-
d
l
o
f
i
n
a
m
a

,
l
e
d
o
m

-
e
h
t
-
f
o
-
e
t
a
t
s

e
m
o
s

s
m
r
o
f
r
e
p
t
u
o

g
n
i
g
a
m

i

l
a
r
t
c
e
p
s
r
e
p
y
h

N
B
D
M
M

t
a
h
t

g
n
i
t
a
r
t
s
n
o
m
e
d

f
o

s
c
i
t
s
i
r
e
t
c
a
r
a
h
c

,
y
l
e
v
i
t
c
e
p
s
e
r

,

%
5
2
.
8
7

d
n
a

d
l
o
f
i
n
a
m
p
e
e
d

e
r
i
u
q
c
a

-
a
c
fi
i
s
s
a
l
c

s
’
N
B
D
M
M

l
a
r
t
c
e
p
s
r
e
p
y
H

-
i
l
a
S
e
h
t

n
o

s
g
n
i
d
n
fi

l
a
t
n
e
m

i
r
e
p
x
E

N
B
D
M
M
p
o
l
e
v
e
d

o
T

)
2
2
0
2
(

.
l
a

t
e

i

L

n
o
i
t
a
c
fi
i
s
s
a
l
c

n
i

s
m
h
t
i
r
o
g
l
a

t
r
a

e
c
n
a
m
r
o
f
r
e
p

s
k
r
a
m
e
R

)
s
(
n
o
i
t
a
c
i
l
p
p
A

)
s
(
e
m
o
c
t
u
O

)
s
(
k
s
a
t

n
i
a

M

d
e
y
e
v
r
u
s

y
d
u
t
S

n
o
i
t
p
i
r
c
s
e
d

l
a
r
e
n
e
G

l
e
d
o
M

)
d
e
u
n
i
t
n
o
c
(

2
e
l
b
a
T

13579

-
i
n
g
o
c
e
r

e
h
T

.
s
r
e
y
a
l

e
v
fi

y
l
n
o

h
t
i

w
N
B
D
C
G
e
n
o

e
b

n
a
c

y
c
a
r
u
c
c
a

n
o
i
t

e
r
o
m
g
n
i
d
d
a

y
b

d
e
s
a
e
r
c
n
i

-
l
o
o
p

d
n
a

l
a
n
o
i
t
u
l
o
v
n
o
c

s
r
e
y
a
l

g
n
i

e
h
T

.
d
e
v
o
r
p
m

i

s
a
w
e
c
n
a
m
r
o
f
r
e
p

-
a
t
u
p
m
o
c
w
o
l

d
e
w
o
h
s

l
e
d
o
m

e
h
t

h
t
i

w
d
e
r
a
p
m
o
c

t
s
o
c

l
a
n
o
i
t

n
n
a
m
z
t
l
o
B
d
e
t
c
i
r
t
s
e
r

)

M
B
R
B
G

(

s
e
n
i
h
c
a
m

f
o

t

fi
e
n
e
b

e
h
t

e
k
a
t

o
t

s
d
o
h
t
e
m
g
n
i
t
s
i
x
e

-
u
l
o
v
n
o
c

d
n
a

M
B
R
B
G

s
k
r
o
w
t
e
n
l
a
r
u
e
n

n
o
i
t

n
o
i
t
c
a
r
t
x
e

n
o
i
t
c
a
r
t
x
e

e
r
u
t
a
e
f

,
n
o
i
t
u
l
o
v
n
o
c

i
l
l
u
o
n
r
e
B
n
a
i
s
s
u
a
G
n
o

)
d

,
c

,
b

t
l
i
u
b

t
s
u
j

t
n
e
m

i
r
e
p
x
e

s
i
h
T

e
r
u
t
a
e
f

e
g
a
m

I

d
n
a

e
c
n
a
i
r
a
v

g
n
i
r
e
d
i
s
n
o
c

y
B

d
e
s
a
b

l
e
d
o
m
a

e
s
o
p
o
r
P

,
a
9
1
0
2
(

.
l
a

t
e

i

L

e
u
s
s
i

g
n
i
t
t

fi
r
e
v
o

e
h
t

y
a
w
a

p
e
e
k

n
a
c

t
i

d
n
a

,
s
t
h
g
i
e
w

g
n
i
y
l
p
p
a

y
b

y
l
t
s
u
b
o
r

e
h
t

e
t
a
i
t
i
n
i

o
t

N
B
D
C

-
c
e
t
e
d

e
c
i
o
v

%
6
6
s
a
w
N
N
C

f
o
y
c
a
r
u
c
c
a
e
h
t

e
c
i
o
v
l
a
c
i
g
o
l
o
h
t
a
p
r
o
f

-
u
l
o
v
n
o
c

s
k
c
a
t
s

l
e
d
o
m
s
i
h
T

.
e
g
a
m

i

e
z
i
s

l
a
e
r

f
e
i
l
e
b

p
e
e
d

n
o
i
t

s
a
e
r
e
h
w
y
l
e
v
i
t
c
e
p
s
e
r

%
7
7
d
n
a

%
1
7
d
n
a
%
8
6
d
e
v
e
i
h
c
a
N
B
D
C

n
o

d
e
s
a
b

n
o
i
t
c
e
t
e
d

e
r
u
t
c
u
r
t
s
N
N
C

y
l
e
v
i
t
c
e
p
s
e
r

r
e
y
a
l
i
t
l
u
m
a

t
c
u
r
t
s
n
o
c

o
t

)
s

M
B
R
C

(

s

M
B
R

l
a
n
o
i
t

d
n
a

n
e
d
d
i
h

e
h
t

f
o

t
h
g
i
e
w
e
h
t

s
e
t
u
b
i
r
t
s
i
d
M
B
R
C

e
h
t

,

M
B
R
e
k
i
l
n
U

.
s
N
B
D
o
t

r
a
l
i

m
i
s

e
r
u
t
c
u
r
t
s

e
g
a
m

i

e
h
t

s
s
o
r
c
a

s
r
e
y
a
l

e
l
b
i
s
i
v

k
r
o
w
t
e
n

)

N
B
D
C

(

e
r
o
m
d
e
n
u
t

e
b

n
a
c
N
N
C

l
a
c
i
g
o
l
o
h
t
a
P

s
t
e
s
g
n
i
t
s
e
t
d
n
a
n
o
i
t
a
d
i
l
a
v
e
h
t

r
o
F

e
u
q
i
n
h
c
e
t

l
e
v
o
n

a

t
n
e
s
e
r
P

)
8
1
0
2
(

.
l
a

t
e

u
W

a

r
o
f

l
e
d
o
m
e
v
i
t
a
r
e
n
e
g

l
a
c
i
h
c
r
a
r
e
i
h

a

s
i

N
B
D
C

l
a
n
o
i
t
u
l
o
v
n
o
C

Deep learning modelling techniques: current progress,…1 3

13580

S. F. Ahmed et al.

d
n
a

e
t
a
r

g
n
i
n
r
a
e
l

s
a

h
c
u
s

d
l
u
o
c

r
o
t
c
a
f

m
u
t
n
e
m
o
m

d
e
z
i
m

i
t
p
o

e
b

y
r
a
n
o
r
o
c

k
r
o
w
t
e
n

l
a
r
u
e
n

a

f
o

e
c
n
a
m
r
o
f
r
e
p

s
e
n
i
b
m
o
c

t
a
h
t

e
u
q
i
n

)
7
1
0
2
(

t
u
o
b
a

n
o
i
t
a
m
r
o
f
n
i

s
u
o
i
v
e
r
p

s
e
d
i
v
o
r
p

t
a
h
t

l
e
d
o
m

e
s
a
e
s
i
d

y
r
e
t
r
a

c
i
t
e
n
e
g

a

h
t
i

w
s
t
h
g
i
e
w

l
a
i
t
i
n
i

g
n
i
d
a
r
g
p
u

y
b
%
0
1

d
n
u
o
r
a

y
b

s
t
i

m
h
t
i
r
o
g
l
a

h
t
i

w
s
m
h
t
i
r
o
g
l
a

c
i
t
e
n
e
g

y
r
a
n
o
r
o
c

g
n
i
s
o
n
g
a
i
d

r
o
f

s
k
r
o
w
t
e
n
l
a
r
u
e
n

e
s
a
e
s
i
d

y
r
e
t
r
a

s
a

s
t
c
a

h
c
i
h
w

,
k
r
o
w
t
e
n

l
a
r
u
e
n

a

h
t
i

w
s
s
e
c
o
r
p

e
h
t

.
s
t
n
e
m
u
g
r
a

s
s
e
c
o
r
p

d
e
r
u
s
a
e
m
n
u

f
o

e
t
a
m

i
t
s
e

n
a

y
g
r
e
n
e

,
n
o
i
t
a
c
fi
i
s
s
a
l
c

t
n
e
m

i
t
n
e
s

r
o
f

l
u
f
e
s
u

s
i

t
I

r
e
h
t
o

y
n
a
m
d
n
a

,
s
i
s
o
n
g
a
i
d

e
s
a
e
s
i
d

,
g
n
i
t
s
a
c
e
r
o
f

s
n
o
i
t
a
c
i
l
p
p
a

k
r
o
w
t
e
n

)

N
N
H

(

s
r
e
t
e
m
a
r
a
p

r
e
h
t
o

e
m
o
S

g
n
i
s
o
n
g
a
i
D

e
h
t

s
e
v
o
r
p
m

i

h
c
a
o
r
p
p
a

d
i
r
b
y
h

e
h
T

-
h
c
e
t

d
i
r
b
y
h

a

p
o
l
e
v
e
D

.
l
a

t
e

i
d
a
s
a
b
a
r
A

l
a
p
i
c
n
i
r
p

t
s
r
fi

l
a
i
t
r
a
p

a

f
o

d
e
s
i
r
p
m
o
c

s
i

N
N
H
e
h
T

l
a
r
u
e
n

d
i
r
b
y
H

s
k
r
a
m
e
R

)
s
(
n
o
i
t
a
c
i
l
p
p
A

)
s
(
e
m
o
c
t
u
O

)
s
(
k
s
a
t

n
i
a

M

d
e
y
e
v
r
u
s

y
d
u
t
S

n
o
i
t
p
i
r
c
s
e
d

l
a
r
e
n
e
G

l
e
d
o
M

)
d
e
u
n
i
t
n
o
c
(

2
e
l
b
a
T

g
n
i
t
t

fi
r
e
d
n
u

t
n
e
v
e
r
p

o
t

s
e
u
s
s
i

g
n
i
t
t

fi
r
e
v
o

d
n
a

s
i
h
t

f
o

p
l
e
h

e
h
t

h
t
i

w

d
o
h
t
e
m
d
i
r
b
y
h

n
i
a
m
o
d

e
h
t

n
i

s
l
e
d
o
m

r
e
h
t
o

g
n
i
t
s
a
c
e
r
o
f

d
i
r
b
y
h

a

n
o

k
r
o
w
t
e
n

l
a
r
u
e
n
a

g
n
i

c
i
t
s
i
r
u
e
h
a
t
e

M

a

h
t
i

w

-
t
a
r
g
e
t
n
i

y
b

e
n
i
g
n
e

m
h
t
i
r
o
g
l
a

e
l
b
a

s
i

e
n
i
g
n
e

g
n
i
t
s
a
c
e
r
o
f

g
n
i
t
s
a
c
e
r
o
f

n
a
h
t

y
c
a
r
u
c
c
a

n
o
i
t
c
i
d
e
r
p
r
e
t
t
e
b

d
e
s
a
b

y
g
o
l
o
d
o
h
t
e
m
g
n
i

)
8
1
0
2
(

d
e
s
a
b
-
k
r
o
w
t
e
n

l
a
r
u
e
n

e
h
T

y
g
r
e
n
e

r
a
l
o
S

d
e
d
i
v
o
r
p
l
e
d
o
m
d
e
s
o
p
o
r
p

e
h
T

-
t
s
a
c
e
r
o
f

w
e
n

a

t
s
e
g
g
u
S

.
l
a

t
e

a
i
n
i
d
e
b
A

n
o

y
l
e
r

t
o
n

s
e
o
d

l
e
d
o
m

s
i
h
T

-
s
a
l
c

t
n
e
m

i
t
n
e
S

-
d
o
m

r
e
h
t
o

n
a
h
t

r
e
t
t
e
b

d
e
m
r
o
f
r
e
P

e
r
u
t
c
e
t
i
h
c
r
a

n
a

e
s
o
p
o
r
P

.
l
a

t
e

h
s
o
h
G

h
c
u
s

,
s
e
c
r
u
o
s
e
r

l
a
n
r
e
t
x
e

-
r
a
n
o
i
t
c
i
d

t
n
e
m

i
t
n
e
s

s
a

e
h
t

s
e
c
u
d
e
r

s
u
h
t

d
n
a

,
s
e
i

y
t
i
x
e
l
p
m
o
c

s
’

m
e
t
s
y
s

n
i

r
e
t
t
e
b
m
r
o
f
r
e
p
t
o
n

d
l
u
o
c

t
u
b

d
n
a

)

N
N
P
(

k
r
o
w
t
e
n
l
a
r

-
i
l
p
p
a

n
e
h
c
t
i

K
d
n
a

,
s
c
i
n
o
r
t
c
e
l
E

n
n
a
m
z
t
l
o
B
d
e
t
c
i
r
t
s
e
r

s
t
e
s
a
t
a
d

e
c
n
a

)

M
B
R

(

e
n
i
h
c
a
m

r
e
h
t
e
g
o
t

n
o
i
t
a
c
fi
i
s

s
t
e
s
a
t
a
d
D
V
D
d
n
a

s
k
o
o
B
n
i

s
l
e

-
u
e
n
c
i
t
s
i
l
i
b
a
b
o
r
p
g
n
i
s
u

)
6
1
0
2
(

e
h
t

e
l
i
h
w

t
u
o

d
e
r
e
t
l

fi
e
b

r
e
t
e
m
a
r
a
p
r
e
p
y
h

l
a
m

i
t
p
o

n
a
c

a
t
a
d

y
r
a
s
s
e
c
e
n
n
u

d
e
h
c
r
a
e
s

s
i

t
e
s

g
n
i

d
e
t
s
a
c
e
r
o
f

y
l
e
t
a
r
u
c
c
a

,

M
T
S
L
r
o

-
s
e
y
a
B
d
n
a
m
r
o
f
s
n
a
r
T

n
i

%
3

n
a
h
t

s
s
e
l

f
o

s
r
o
r
r
e

d
e
r
a
u
q
s

m
r
e
t

t
r
o
h
s

e
h
t

r
o
f

e
c
i
r
p

t
r
o
h
s

e
h
t

n
i

e
c
i
r
p
r
e
p
p
o
c

e
h
t

n
a
e
m
e
h
t

h
t
i

w
m
r
e
t

g
n
o
l

d
n
a

o
t

n
o
i
t
a
z
i
m

i
t
p
O
n
a
i

r
e
p
p
o
c

e
h
t

t
c
i
d
e
r
p

s
e
s
a
c

h
t
o
b

m
r
e
t
-
g
n
o
l

d
n
a

e
h
t

,

N
N
H
e
h
t

h
t
i

W

-
t
s
a
c
e
r
o
f

e
c
i
r
P

U
R
G

,
s
e
h
c
a
o
r
p
p
a

d
e
s
o
p
o
r
p

e
h
T

t
e
l
e
v
a
W
h
t
i

w
N
N
H
e
s
U

)
2
2
0
2

.
l
a

t
e

u
i
L
(

n
o
i
t
c
i
d
e
r
p

e
h
t

s
e
s
a
e
r
c
n
i

d
n
a

l
e
d
o
m

s
e
i
r
e
s
-
e
m

i
t

y
c
a
r
u
c
c
a

e
h
t

m
o
r
f

d
e
n
i
a
t
b
o

s
t
u
p
t
u
o

n
o
i
t
c
i
d
e
r
p

e
c
i
r
p

l
i
o

r
o
f

s
l
e
d
o
m
N
N
A
d
n
a

s
e
i
r
e
s
-
e
m

i
t

n
a
h
t

N
N
D
g
n
i
s
u

n
o
i
t
c
i
d
e
r
p

t
c
i
d
e
r
p

o
t

N
N
A
n
a

f
o

-
p
o
l
e
v
e
d

y
b
s
e
c
i
r
p
l
i
o

l
a
r
u
e
n

c
i
m
a
n
y
d
a

g
n
i

k
r
o
w
t
e
n

)
4
1
0
2
(

l
a
n
o
i
t
i
d
a
r
t

m
r
o
f
r
e
p
t
u
o

n
a
c

t
a
h
t

e
u
q
i
n
h
c
e
t

g
n
i

k
r
o
w
t
e
n

l
a
r

-
e
v
i
t
p
a
d
a

,
y
c
a
r
u
c
c
a

f
o
s
m
r
e
t

n
i

s
l
e
d
o
m
c
i
t
a
t
s

)

N
N
D

(

y
t
i
x
e
l
p
m
o
c

l
a
n
o
i
t
a
t
u
p
m
o
c

d
n
a

,
s
s
e
n

e
h
t

s
t
s
u
j
d
a

l
e
d
o
m
e
h
T

e
c
i
r
p

l
i

O

d
e
v
e
i
h
c
a

s
a
w
y
c
a
r
u
c
c
a

r
e
t
t
e
B

e
c
n
a
m
r
o
f
r
e
p

e
h
t

e
v
o
r
p
m

I

.
l
a

t
e

i
z
r
a
d
o
G

-
g
r
e
m
e

n
a

e
r
a

)
s
N
N
D

(

s
k
r
o
w
t
e
n

l
a
r
u
e
n
c
i
m
a
n
y
D

-
u
e
n

c
i
m
a
n
y
D

1 3

s
e
i
t
i
r
a
l
i

m

i
s

h
c
a
o
r
p
p
a

d
e
h
s
i
l
b
a
t
s
e

y
b

s
e
u
q
i
n
h
c
e
t

g
n
i
n
r
a
e
l

s
l
e
d
o
m
d
e
s
a
b
-
k
r
o
w
t
e
n

-
n
o
c

g
n
i
g
g
o
l
b
o
r
c
i
m

r
o
f

t
s
i
s
n
o
c

t
h
g
i
m

t
a
h
t

t
n
e
t

l
a
r
u
e
n

g
n
i
t
n
e
m
e
l
p
m

i

s
e
g
a
m

i

d
n
a

s
t
x
e
t

f
o

s
e
t
a
r
o
p
r
o
c
n
i

t
a
h
t

R
L
-
W
O
B
C

f
o

t
n
e
m
e
c
n
a
h
n
e

s
t
e
e
w

t

n
i

s
e
g
a
m

i

s
a

h
c
u
s

,
a
t
a
d

l
a
u
s
i
v

-
d
r
o
w
c
i
t
n
a
m
e
s
/
c
i
t
c
a
t
n
y
s

n
i

l
l
e
w
d
e
m
r
o
f
r
e
p

e
b

n
a
C

s
i
s
y
l
a
n
a

t
n
e
m

i
t
n
e
S

-
l
l
e
w
a

s
i

h
c
i
h
w

,
h
c
a
o
r
p
p
a

l
a
d
o
m

i
t
l
u
m

f
o

e
s
u

e
h
t

)
6
1
0
2
(

n
a

s
i

R
L
-
A
D
W
O
B
C

-

.

m
h
t
i
r
o
g
l
a

W
O
B
C
e
h
t

f
o

k
n
a
B

i
t
n
e
S
e
h
t

d
e
m
r
o
f
r
e
p
t
u
O

h
t
i

w
s
t
n
e
m

i
t
n
e
s

e
z
y
l
a
n
A

.
l
a

t
e

i
h
c
c
e
a
B

n
o
i
s
n
e
t
x
e

n
a

s
i

)

R
L
(

n
o
i
s
s
e
r
g
e
r

c
i
t
s
i
g
o
l
-

W
O
B
C

R
L
-
A
D
W
O
B
C

-

s
k
r
a
m
e
R

)
s
(
n
o
i
t
a
c
i
l
p
p
A

)
s
(
e
m
o
c
t
u
O

)
s
(
k
s
a
t

n
i
a

M

d
e
y
e
v
r
u
s

y
d
u
t
S

n
o
i
t
p
i
r
c
s
e
d

l
a
r
e
n
e
G

l
e
d
o
M

l
a
i
t
i
n
i

t
n
a
c
fi
i
n
g
i
s

a

s
i

s
i
h
T

g
n
i
s
o
n
g
a
i
D

t
n
a
c
fi
i
n
g
i
s

d
e
w
o
h
s
N
S
E
p
e
e
D

-
h
c
e
t

l
e
v
o
n

a

p
o
l
e
v
e
D

.
l
a

t
e

o
i
h
c
c
i
l
l
a
G

a

f
o

y
c
n
e
i
c
ffi
e

e
h
t

e
c
n
a
h
n
e

n
a
c
N
S
E
p
e
e
D
e
h
T

o
h
c
e

p
e
e
D

)
d
e
u
n
i
t
n
o
c
(

2
e
l
b
a
T

e
h
t

s
w
o
h
s

t
a
h
t

N
S
E
p
e
e
D

N
S
E
p
e
e
D

f
o

y
t
i
r
o
i
r
e
p
u
s

N
S
E
w
o
l
l
a
h
s

e
h
t

r
e
v
o

l
e
d
o
m

e
s
a
e
s
i
d

r
o
F

.
)

N
S
E
(

k
r
o
w
t
e
n

e
t
a
t
s

o
h
c
e

g
n
i
t
s
e
t

d
n
a

n
o
i
t
a
d
i
l
a
v

,
g
n
i
n
i
a
r
t

5
9
.
2

,
7
6
.
2

s
a
w
y
c
a
r
u
c
c
a

s
t
i

,
t
e
s

N
S
E
n
a
h
t

e
r
o
m
%
7
0
.
3

d
n
a

g
n
i
s
o
n
g
a
i
d

r
o
f

N
S
E

e
s
a
e
s
i
d

s
’
n
o
s
n
i
k
r
a
P

-
h
c
e
t

N
S
E

l
a
u
s
u

e
h
T

.
s
r
e
y
a
l

t
n
e
r
r
u
c
e
r

l
l
a

s
s
o
r
c
a

s
t
i
n
u
t
n
e
r
r
u
c
e
r

e
h
t

f
o

e
r
u
t
c
u
r
t
s

r
a
e
n
i
l

a

g
n
i
s
u

d
e
c
u
d
o
r
p

s
i

t
u
p
t
u
o
N
S
E
p
e
e
D
e
h
T

.
s
n
i
a
m
o
d

h
c
u
S

.
s
n
o
i
t
a
t
i

m

i
l

y
t
i
l
i
b
a
t
s

o
t

t
c
e
j
b
u
s

s
i

e
u
q
i
n

a
i
r
e
t
i
r
c

e
h
t

y
b
N
S
E
p
e
e
D
n
i

d
e
t
a
t
s

e
r
a

s
t
i

m

i
l

g
n
i
t
u
p
m
o
c

r
i
o
v
r
e
s
e
r

p
e
e
d

e
h
t

f
o
N
S
E
e
h
t

r
o
f

k
r
o
w
t
e
n

f
o

n
i
a
m
o
d

e
h
t

n
i

k
r
o
w

s
’
n
o
s
n
i
k
r
a
P

e
h
t

o
t

d
e
r
a
p
m
o
c

e
c
n
a
m
r
o
f
r
e
p

-
p
e
e
D
n
o

d
e
s
a
b

e
u
q
i
n

)
a
8
1
0
2
(

l
a
r
e
v
e
s

n
i

)

N
S
E
(

k
r
o
w
t
e
n

e
t
a
t
s

o
h
c
e

l
a
r
e
n
e
g

k
r
o
w
t
e
n
e
t
a
t
s

)

N
S
E
p
e
e
D

(

d
e
v
e
i
h
c
a

e
b
n
a
c

e
c
n
a
m
r
o
f

-
n
e
m
i
d
i
t
l
u
m
e
g
r
a
l

a

r
o
f

-
r
e
p

t
n
a
c
fi
i
n
g
i
S

.
l
e
d
o
m

a
t
a
d
l
a
n
o
i
s

n
o
i
t
a
i
v
e
d

d
r
a
d
n
a
t
s

e
h
t

r
o
f

N
S
E
p
e
e
D
D
A

-

-
c
i
d
e
r
p

a
t
a
d
s
e
i
r
e
s

e
m

i
t

)

D
A

(

n
o
i
t
i
s
o
p
m
o
c
e
d

e
v
i
t
i
d
d
a

e
r
e
h
w
n
o
i
t

s
a

d
e
s
u

s
a
w
e
u
q
i
n
h
c
e
t

p
e
t
s

g
n
i
s
s
e
c
o
r
p
-
e
r
p

a

l
e
d
o
m
e
h
t

o
t

e
h
t

f
o

y
t
i
l
i
b
a
t
s

e
h
t

s
e
v
o
r
p

n
o
i
t
c
i
d
e
r
p

w
o
l

a

h
t
i

w
s
t
e
s
a
t
a
d

x
i
s

n
o

l
l
e
w

y
b

d
e
t
o
n
e
d

l
e
d
o
m

)
b
8
1
0
2
(

n
o
i
t
a
i
v
e
d

d
r
a
d
n
a
t
s
w
o
l

A

s
e
i
r
e
s

e
m
T

i

d
e
m
r
o
f
r
e
p

l
e
d
o
m
N
S
E
p
e
e
D
D
A

-

N
S
E
p
e
e
D
a

t
c
u
r
t
s
n
o
C

.
l
a

t
e

o
i
h
c
c
i
l
l
a
G

13581

r
o
f

d
e
s
u

e
b

n
a
c

a
t
a
d

y
r
a

-
r
e
p

e
l
b
a
e
c
i
t
o
n

a

g
n
i
t
t
e
g

l
e
d
o
m
e
h
t

f
o

e
c
n
a
m
r
o
f

g
n
i
t
s
a
c
e
r
o
f

h
t
i

w
n
o
s
i
r
a
p
m
o
c

n
i

n
o
i
s
i
c
e
r
p

g
n
i
t
s
a
c
e
r
o
f

n
i

t
n
e
m
e
v
o
r
p
m

i

N
N
R
E
d
n
a

,

N
N
T
S

,

N
N
P
B

,

N
N
R
E
g
n
i
n
i
b
m
o
c

y
b

,
n
o
r
t
p
e
c
r
e
p

r
e
y
a
l
i
t
l
u
m

-
e
m

i
t
-
c
i
t
s
a
h
c
o
t
s

d
n
a

n
o
i
t
c
n
u
f

e
v
i
t
c
e
ff
e

)
c

,
b

,
a
6
1
0
2
(

e
h
T

.
r
e
m
r
o
f

e
h
t

n
i

r
e
y
a
l

t
x
e
t
n
o
c

e
h
t

r
o
f

t
u
p
n
i

l
a
r
u
e
n

t
n
e
r

t
u
p
n
i

:
s
r
e
y
a
l

r
u
o
f

s
e
s
i
r
p
m
o
c

e
r
u
t
c
e
t
i
h
c
r
a
N
N
R
E

e
s
u
t
a
h
t

s
n
o
r
u
e
n

e
l
p
i
t
l
u
m

r
o

e
n
o
s
a
h

r
e
y
a
l

h
c
a
E

f
o
m
u
s

d
e
t
h
g
i
e
w

r
i
e
h
t

f
o

n
o
i
t
c
n
u
f

r
a
e
n
i
l
-
n
o
n

a

o
t

r
e
y
a
l

e
n
o
m
o
r
f

n
o
i
t
a
m
r
o
f
n
i

r
e
f
s
n
a
r
t
o
t

s
t
u
p
n
i

.
r
e
y
a
l

t
u
p
t
u
o

d
n
a

n
e
d
d
i
h

,
r
e
y
a
l

t
n
e
r
r
u
c
e
r

,
r
e
y
a
l

e
n
o

t
x
e
n

e
h
t

k
r
o
w
t
e
n

)

N
N
R
E
(

-
n
o
i
t
a
t
s
n
o
n

d
n
a

r
a
e
n
i
l
n
o
N

s
e
c
i
d
n
i

k
c
o
t
S

n
a

d
e
w
o
h
s

l
e
d
o
m
d
e
s
o
p
o
r
p

e
h
T

e
r
u
t
c
e
t
i
h
c
r
a

n
a

d
l
i
u
B

.
l
a

t
e

g
n
a
W

s
a

d
e
s
u

s
i

t
u
p
t
u
o
s
’
r
e
y
a
l

n
e
d
d
i
h

e
h
t

,

N
N
R
E
n
I

-
r
u
c
e
r

n
a
m
E

l

Deep learning modelling techniques: current progress,…1 3

13582

S. F. Ahmed et al.

-
n
e
m
i
d

r
e
h
g
i
h

x
e
l
p
m
o
c

r
a
e
n
i
l

r
o
f

d
e
n
i
m
a
x
e
n
u

s
r
e
t
e
m
a
r
a
p

d
n
a

s
n
o
i
s

l
a
c
i
t
s
i
t
a
t
s

n
i

n
o
i
t
a
m

i
t
s
e

g
n
i
n
r
a
e
l

t
n
e
t
s
i
s
n
o
c

r
o
f

l
l
e
w
s
m
r
o
f
r
e
p

n
o
i
t
a
m

i
t
s
e

p
e
t
s
-
e
l
g
n
i
s
d
n
a

,
y
g
r
e
n
e

g
n
i
n
r
a
e
l

n
i

)

N
E
E
D

(

e
h
t

,
n
o
i
t
c
n
u
f

g
n
i
r
o
c
s

s
n
o
i
t
a
r
e
p
o

g
n
i
s
i
o
n
e
d

l
a
n
o
i
s
n
e
m
i
d
-
h
g
i
h
r
o
f

a
t
a
d
c
i
t
e
h
t
n
y
s

d
n
a

k
r
o
w
t
e
n
r
o
t
a
m

i
t
s
e

g
n
i
n
r
a
e
l

p
e
e
d

f
o

)
8
1
0
2
(

s
i

l
e
d
o
m
N
E
E
D
e
h
T

y
t
i
s
n
e
D

k
r
o
w
t
e
n

r
o
t
a
m

i
t
s
e

g
n
i
n
r
a
e
l

p
e
e
D

y
t
i
l
i
t
u

e
h
t

e
t
a
r
t
s
n
o
m
e
D

.
l
a

t
e

i

m
e
r
a
S

r
o
i
v
a
h
e
b

l
a
d
o
m

i
t
l
u
m
x
e
l
p

-
r
u
p
-
l
a
r
e
n
e
g

g
n
i
n
i
a
r
t
-
e
r
p

s
e
i
c
i
l
o
p

c
i
t
s
a
h
c
o
t
s

e
s
o
p

d
i
o
n
a
m
u
h

g
n
i
d
l
i
u
B

s
t
o
b
o
r

-
i
t
l
u
m
d
e
t
a
c
i
l
p
m
o
c

g
n
i
t
n
e
s
e
r
p
e
r

f
o

y
t
e
i
r
a
v
a

n
i

r
o
i
v
a
h
e
b

l
a
d
o
m

s
t
x
e
t
n
o
c

-
n
r
a
e
l

t
n
e
m
e
c
r
o
f
n
i
e
r

g
n
i
s
u

,

M
E
D
a
i
v

g
n
i

n
o
i
s
i
c
e
d
v
o
k
r
a

M

e
h
t

s
s
e
c
o
r
p

)
7
1
0
2
(

-

m
o
c

s
e
r
u
t
p
a
c

y
l
e
v
i
t
c
e
ff
E

;
s
k
s
a
t

c
i
t
o
b
o
R

y
l
e
t
a
r
u
c
c
a

f
o

e
l
b
a
p
a
c

s
i

l
e
d
o
m
e
h
T

m
u
m
i
x
a
m
e
r
o
l
p
x
E

.
l
a

t
e

a
j
o
n
r
a
a
H

e
h
t

g
n
i
z
i
l
a
i
t
i
n
i

y
l
m
o
d
n
a
R

g
n
i
t
s
a
c
e
r
o
F

d
e
z
i
l
a
m
r
o
n
s
’
l
e
d
o
m
d
e
s
o
p
o
r
p

e
h
T

r
a
e
n
i
l
-
n
o
n

a

y
l
p
p
A

.
l
a

t
e

e
n
e
h
c
i
r

K

t
x
e
t
n
o
c

e
h
t

f
o

s
t
h
g
i
e
w

e
h
t

e
c
u
d
o
r
p

n
a
c

s
t
i
n
u

s
t
l
u
s
e
r

l
a
m

i
t
p
o

s
e
i
r
e
s
-
e
m

i
t

s
t
n
e
m
e
l
e

y
e
k
c
a

M

s
s
a
l
G

s
l
e
d
o
m
N
N
R

l
a
n
o
i
t
i
d
a
r
t

r
e
h
t
o

o
t

e
c
n
i
s

t
s
e
t

k
r
a
m
h
c
n
e
b

-
l
a
h
c

e
r
a

s
t
n
e
m
e
l
e

s
t
i

n
o
i
t
c
i
d
e
r
p
r
o
f

g
n
i
g
n
e
l

d
o
o
g

a

s
w
o
h
s

t
a
h
t

d
e
r
a
p
m
o
c

)
5
6
1
0
.
0
(

l
a
m
i
n
i
m
s
a
w

N
N
R
o
t

s
s
a
l
G
–
y
e
k
c
a

M

e
u
l
a
v

r
o
r
r
e

e
r
a
u
q
s

n
a
e
m

t
o
o
r

d
e
m
a
n
m
e
t
s
y
s

c
i
t
o
a
h
c

)
7
1
0
2
(

,
s

M
E
D

t
s
a
p

o
t

d
e
r
a
p
m
o
C

g
n
i
d
l
i
u
B

-
n
o
i
t
c
n
u
f

e
h
t

d
e
v
l
o
s
e
r

d
o
h
t
e
m
e
h
T

f
o

t
n
e
m
y
o
l
p
m
E

.
l
a

t
e

v
o
n
u
t
r
a
B

r
o
f

e
u
q
i
n
h
c
e
t

g
n
i
n
i
a
r
t

g
n
i
n
r
a
e
l

p
e
e
d

a

s
i

M
E
D

y
g
r
e
n
e

p
e
e
D

s
k
r
a
m
e
R

)
s
(
n
o
i
t
a
c
i
l
p
p
A

)
s
(
e
m
o
c
t
u
O

)
s
(
k
s
a
t

n
i
a

M

d
e
y
e
v
r
u
s

y
d
u
t
S

n
o
i
t
p
i
r
c
s
e
d

l
a
r
e
n
e
G

l
e
d
o
M

)
d
e
u
n
i
t
n
o
c
(

2
e
l
b
a
T

w
o
l
s

e
z
i
l
i
t
u

n
a
c

s

M
M
B
E

g
n
i
v
a
h

,
g
n
i
n
r
a
e
l

t
n
e
i
d
a
r
g

l
a
n
o
i
t
u
l
o
v
n
o
c

e
v
i
t
c
e
ff
e

y
l
r
a
l
u
c
i
t
r
a
p

,
s
e
i
r
o
m
e
m

s
e
l
u
r

g
n
i
t
i
r

w

t
s
a
f

o
t

e
u
d

d
e
s
s
e
r
p
m
o
c

s
e
i
r
o
m
e
m

t
s
a
f

g
n
i
v
a
h

,
s

M
M
B
E
f
o

e
c
a
p

g
n
i

r
e
t
e
m
a
r
a
p

d
e
t
i

m

i
l

d
n
a

g
n
i
t
i
r

w

r
o
f

s
t
u
p
n
i

w
e
n

g
n
i
d
d
a

,
s
e
t
a
d
p
u

s
t
h
g
i
e
w
e
h
t

g
n
i
n
r
a
e
l

d
e
s
a
b
-
a
t
e
m

-
y
g
r
e
n
e

o
t

d
o
h
t
e
m

l
e
d
o
m
y
r
o
m
e
m
d
e
s
a
b

g
n
i
r
o
t
s

r
o
f

)

M
M
B
E
(

s
n
r
e
t
t
a
p

)
9
1
0
2
(

M
B
R
e
h
t

n
o

d
e
s
a
b
s
t
c
e
t
i
h
c
r
a

d
n
a

s
k
r
o
w
t
e
n

p
e
e
d

s
t
i
n
u

n
e
d
d
i
h

c
i
t
s
a
h
c
o
t
s

f
o

r
e
y
a
l

a

a
i
v

t
u
p
t
u
o

e
h
t

g
n
i
l
l
e
d
o
m
n
a
h
t

r
e
h
t
a
r
y
l
l
a
c
i
t
s
i
n
i
m
r
e
t
e
d

s
t
u
p
n
i

d
n
a

s
N
B
D
o
t

t
s
a
r
t
n
o
c

n
I

.
)
n
o
r
u
e
n
/
n
o
r
t
p
e
c
r
e
p
(

a

f
o
s
t
s
i
s
n
o
c

M
E
D

,
s
e
n
i
h
c
a
m
n
n
a
m
z
t
l
o
B
p
e
e
d

s
e
l
b
a
n
e

h
c
i
h
w

,
r
e
y
a
l

n
e
d
d
i
h
c
i
t
s
a
h
c
o
t
s

e
l
g
n
i
s

l
l
a

f
o

g
n
i
n
i
a
r
t

s
u
o
e
n
a
t
l
u
m
i
s

d
n
a

e
c
n
e
r
e
f
n
i

d
i
p
a
r

a
t
a
d
s
m
r
o
f
s
n
a
r
t

t
a
h
t

k
r
o
w
t
e
n

l
a
r
u
e
n

d
r
a
w
r
o
f

-
d
e
e
f

a

s
e
d
u
l
c
n
i

t
I

.
y
g
o
l
o
d
o
h
t
e
m
g
n
i
n
r
a
e
l

k
r
o
w
t
e
n

e
h
t

n
i
h
t
i

w
s
r
e
y
a
l

e
h
t

l
e
d
o
m

)

M
E
D

(

1 3

13583

-
e
v
o
r
p
m

i

d
e
e
n

s
e
u
q
i
n
h
c
e
t

n
o
i
t
a
r
g
e
t
n
i

,
s
n
o
i
t
i
d
n
o
c

y
r
a
d
n
u
o
b

f
o

n
o
i
t
i
s
o
p
m

I

-

n
o
i
t
a
v
i
t
c
a

r
a
e

s
t
n
e
m

-
n
i
l
n
o
n

a

y
b

d
e
t
a
u
l
a
v
e

e
r
a

s
n
o
r
u
e
n

n
e
h
w
n
o
i
t
c
n
u
f

-
r
e
p
y
h

n
o
i
t

y
t
i
c
i
t
s
a
l
e

d
e
z
i
m
i
n
i
m
s
i

y
g
r
e
n
e

l
a
i
t
n
e
t
o
p

y
g
r
e
n
e

l
a
i
t
n
e
t
o
p

)
0
2
0
2
(

.
l
a

t
e

s
s
o
l

e
h
t

f
o

y
t
i
x
e
v
n
o
c
n
o
N

-

-
a
m
r
o
f
e
d
e
t
i
n
i
F

n
e
h
w
e
t
a
t
s
m
u
i
r
b
i
l
i
u
q
e

s
l
fi
l
u
F

s
e
z
i
m
i
n
i
m
y
l
t
c
e
r
i

D

h
n
a
h
T
-
n
e
y
u
g
N

s
k
r
a
m
e
R

)
s
(
n
o
i
t
a
c
i
l
p
p
A

)
s
(
e
m
o
c
t
u
O

)
s
(
k
s
a
t

n
i
a

M

d
e
y
e
v
r
u
s

y
d
u
t
S

n
o
i
t
p
i
r
c
s
e
d

l
a
r
e
n
e
G

l
e
d
o
M

)
d
e
u
n
i
t
n
o
c
(

2
e
l
b
a
T

e
v
i
t
a
g
e
n

s
e
t
a
r
t
s
n
o
m
e
d

t
n
i
o
p

d
e
x
fi
a

s
d
r
a
w
o
t

s
t
c
a
p
m

i

)

U
P
G

(

n
o
i
t
a
x
a
l
e
r

y
h
t
g
n
e
l

e
r
a
w
d
r
a
h

-
k
c
a
b

n
e
e
w
t
e
b

s
p
a
g

e
h
t

d
n
a

n
o
i
t
a
g
a
p
o
r
p

l
e
d
o
m
d
e
s
a
b
-
y
g
r
e
n
e

;
s
e
c
n
e
u
q
e
s

g
n
i
n
i
a
r
t

e
h
t

n
i

l
a
t
i
g
i
d
;
s
t
i
u
c

e
l
b
a
v
i
e
c
n
o
c

e
r
o
m
n
o
i
t
a
g
a
p
o
r
p

e
g
d
i
r
b

o
t

n
o
i
t
a
g
a
p
o
r
p

)
7
1
0
2
(

o
i
g
n
e
B

e
t
a
t
s

s
u
o
i
v
e
r
p

y
r
e
v
e

s
e
r
o
t
S

-
r
i
c

g
o
l
a
n
A

-
k
c
a
b

c
i
t
a
t
s

s
e
k
a
m
y
d
u
t
s

e
h
T

m
u
i
r
b
i
l
i
u
q
e

e
s
o
p
o
r
P

d
n
a

r
e
i
l
l
e
c
S

-
e
s
r
a
p
s

p
e
e
d

e
h
t

h
g
u
o
h
t
l

A

-
s
a
l
c

e
g
a
m

I

k
r
o
w
t
e
n

g
n
i
d
o
c
-
e
s
r
a
p
s

p
e
e
D

g
n
i
n
r
a
e
l

e
r
u
t
a
e
f

e
g
a
m

I

.
l
a

t
e

g
n
a
h
Z

n
o

d
e
s
a
b

k
r
o
w
e
m
a
r
f

d
e
r
i
p
s
n
i
-
o
i
b
a

s
i

N
C
D

g
n
i
d
o
c

p
e
e
D

e
h
t

,
y
l
l
a
c
i
t
a
m
o
t
u
a

s
e
g
a
m

i

-
e
s
r
a
p
s

p
e
e
d

e
h
t

f
o

d
e
e
p
s

o
t

s
d
e
e
n

k
r
o
w
t
e
n

g
n
i
d
o
c

d
e
v
o
r
p
m

i

r
e
h
t
r
u
f

e
b

g
n
i
s
i
o
n
e
d

s
l
e
x
i
p

e
g
a
m

i

w
a
r

m
o
r
f

w
a
r

m
o
r
f

s
e
r
u
t
a
e
f

d
d
o

,
n
o
i
s
s
e
r
p
m
o
c

s
e
r
u
t
a
e
f

t
c
n
i
t
s
i
d

h
g
i
h

g
n
i
t
c
a
r
t
x
e

k
r
o
w
t
e
n

h
g
u
o
r
h
t

d
o
h
t
e
m
e
h
T

.
a
t
a
d

y
r
o
s
n
e
s

s
t
e
r
p
r
e
t
n
i

n
o

d
e
s
a
b

s
t
n
e
m
g
d
u
j

s
t
c
i
d
e
r
p

n
i
a
r
b
e
h
t

h
c
i
h
w

s
a
h

)
n
o
i
t
a
m
r
o
f
n
i

l
a
u
s
i
v

s
a

h
c
u
s
(

s
t
c
a
f

c
fi
i
c
e
p
s

r
e
t
l

fi
f
o

n
o
i
t
p
a
d
a

e
h
t

y
b

d
e
w
o
l
l
o
f

,
g
n
i
d
o
c

e
v
i
t

-
c
i
d
e
r
p

r
o
f

n
o
i
t
a
d
n
u
o
f

e
h
t

s
a

d
e
b
i
r
c
s
e
d

n
e
e
b

d
e
z
i
l
i
t
u

y
l
e
v
i
s
n
e
t
x
e

e
r
a

s
k
r
o
w
t
e
n
e
s
e
h
T

.
t
n
e
c
s
e
d

t
n
e
i
d
a
r
g

a
i
v
s
e
l
u
d
o
m

f
o

g
n
i
n
i
a
r
t

d
n
a

s
e
v
i
t
c
e
j
b
o

o
s
l
a

s
i

N
C
D
e
h
T

.
d
e
h
s
i
l
p
m
o
c
c
a

s
i

n
o
i
t
a
c
fi
i
s
s
a
l
c

g
n
i
d
l
i
u
b

g
n
i
d
u
l
c
n
i

s
r
o
t
c
e
s

r
e
h
t
o

y
n
a
m
n
i

d
e
s
u

e
l
c
i
h
e
v

s
u
o
m
o
n
o
t
u
a

,
e
c
n
a
l
l
i
e
v
r
u
s

d
n
a

y
t
i
r
u
c
e
s

-
c
e
t
e
d

t
c
e
j
b
o

,
s
e
c
i
v
r
e
s

n
o
i
t
a
c
i
n
u
m
m
o
c

,
l
o
r
t
n
o
c

o
e
d
i
v

d
n
a

e
g
a
m

i

e
r
e
h
w

,
n
o
i
s
i
v

r
e
t
u
p
m
o
c

n
i

n
o
i
t
a
c
fi
i
s
s
a
l
c

d
n
a

n
o
i
t

s
t
c
e
t
e
d

k
r
o
w
t
e
n

g
n
i
d
o
c

,
n
o
i
t
a
c
fi
i
s

n
i

s
t
l
u
s
e
r

e
v
i
t
c
e
ff
e

d
e
t
a
r
t
s
n
o
m
e
d

g
n
i
d
o
c
-
e
s
r
a
p
s

p
e
e
d

y
b

)
c

,
b

,
a
7
1
0
2
(

n
i
a
r
b

e
h
t

w
o
h

f
o

e
g
d
e
l
w
o
n
k

l
a
c
i
t
e
r
o
e
h
t

e
h
t

k
r
o
w
t
e
n

)

N
C
D

(

Deep learning modelling techniques: current progress,…1 3

13584

S. F. Ahmed et al.

n
o
i
t
a
z
i
l
a
m
r
o
n

h
c
t
a
b

h
t
i

w

g
n
i
n
r
a
e
l

p
e
e
d

r
e
h
t
o

d
n
a

w
e
f

h
t
i

w
s
e
i
l
p
m
o
C

;
s
l
o
o
t

s
r
e
y
a
l

d
n
a

s
r
e
t
e
m
a
r
a
p

g
n
i
d
o
c

e
s
r
a
p
s

f
o

s
t
s
o
c

e
l
b
i
t
a
p
m
o
c

;
k
r
o
w
t
e
n

n
o
i
t
a
c
fi
i
s
s
a
l
c

e
g
a
m

I

;
n
o
i
t

o
t

g
n
i
d
o
c

e
s
r
a
p
s

l
a
n
o
i
t
n
e
v
n
o
c

e
h
t

e
v
i
t
a
g
e
n
-
n
o
n

h
t
i

w
s
n
o
i
t

;
s
e
r
u
t
c
e
t
i
h
c
r
a

r
e
y
a
l
i
t
l
u
m

y
t
i
c
a
p
a
c

g
n
i
n
r
a
e
l

d
e
d
n
a
p
x
e

g
n
i
d
o
c

e
s
r
a
p
s

n
i
a
r
b

e
h
t

f
o

n
o
i
t
a
z
i
n
a
g
r
o

e
h
t

d
n
a
t
s
r
e
d
n
u

o
t

y
r
a
s

s
e
g
a
m

i

d
l
r
o
w

-
l
a
e
r

r
e
f
n
i

e
h
t

e
v
o
r
p
m

i

o
t

r
e
d
r
o

o
t

n
i

m
h
t
i
r
o
g
l
a

n
o
i
s
i
v

r
e
t
u
p

-

m
o
c

;
n
o
i
t

s
k
s
a
t

d
n
a

n
o
i
t
a
c
fi
i
s
s
a
l
c

e
g
a
m

i

s
u
o
i
r
a
v

p
e
e
d

n
o

d
e
s
a
b

,
l
e
d
o
m

s
k
s
a
t

n
o
i
s
i
v

r
e
t
u
p
m
o
c

r
o
f

,
g
n
i
n
r
a
e
l

d
e
s
i
v
r
e
p

d
l
r
o
w

-
l
a
e
r

g
n
i
s
s
e
c
o
r
p

-
u
s
n
u

g
n
i
s
u

d
e
n
i
a
r
t

,
g
n
i
d
o
c

e
v
i
t
c
i
d
e
r
p

s
e
g
a
m

i

-
s
e
c
e
n

e
r
a

s
e
i
d
u
t
s

e
r
o
M

-
a
l
s
n
a
r
t

e
g
a
m

I

r
o
f

e
l
b
a
t
i
u
s

d
n
u
o
f

s
a
w

l
e
d
o
m
e
h
T

e
v
i
t
a
r
e
n
e
g

a

p
o
l
e
v
e
D

.
l
a

t
e

a
r
o
D

)
8
1
0
2
(

l
a
n
o
i
t
a
t
u
p
m
o
c

e
h
t

s
e
c
u
d
e
R

-
c
e
t
e
d
t
c
e
j
b
O

d
e
d
n
e
t
x
e

y
l
t
n
e
i
c
ffi
E

-
a
t
n
e
s
e
r
p
e
r

e
t
a
i
d
e
m
r
e
t
n
I

)
7
1
0
2
(

.
l
a

t
e

n
u
S

h
t
i

w
s
k
r
o
w
t
e
n

o
t

e
l
b
a
l
a
c
S

s
u
o
m
o
n
o
t
u
A

g
n
i
d
o
c

e
v
i
t
c
i
d
e
r
p

p
e
e
d

f
o

e
s
u

e
h
T

d
n
a

n
o
i
t
a
z
i
r
o
t
i
n
o
M

.
l
a

t
e

a
y
i
d
n
a
T

s
s
e
n
t
s
u
b
o
r

s
e
c
i
v
e
d

y
n
a
m

-
e
v
o
r
p
m

i

e
r
i
u
q
e
r

d
l
u
o
w

-
a
m
o
n
a

x
e
l
p
m
o
c

r
o
f

t
n
e
m

g
n
i
y
o
l
p
m
e

d
n
a

s
e
m

i
t
-
n
u
r

r
e
g
n
o
l

g
n
i
t
a
u
l
a
v
e

,
s
e
i
l

w
a
r

s
s
e
c
o
r
p

o
t

s
e
u
q
i
n
h
c
e
t

s

m
r
o
f

t
n
e
r
e
ff
i
d

n
i

a
t
a
d

g
n
i
n
r
a
e
l

e
n
i
h
c
a
m

-
a
c
i
n
u
m
m
o
c

s
e
c
i
v
r
e
s

n
o
i
t

e
l
c
i
h
e
v

;
l
o
r
t
n
o
c

e
n
i
h
c
a
m

r
e
h
t
o

n
a
h
t

t
n
e
i
c
ffi
e

-
c
i
d
e
r
p

p
e
e
d

y
b

y
c
n
e
u
q

s
e
h
c
a
o
r
p
p
a

d
e
s
a
b
-
g
n
i
n
r
a
e
l

g
n
i
d
o
c

e
v
i
t

e
r
o
m
d
n
a

r
e
t
s
a
f

d
n
u
o
f

s
a
w

-
e
r
f
o
i
d
a
r

f
o
s
i
s
y
l
a
n
a

)
8
1
0
2
(

t
n
e
m
e
v
o
r
p
m

i

t
n
a
c
fi
i
n
g
i
s

g
n
i
d
o
c

e
v
i
t
c
i
d
e
r
p

e
h
t

r
o
f

a

e
b

d
l
u
o
c

s
r
e
t
e
m
a
r
a
p

s
k
r
o
w
t
e
n

d
n
a

y
t
i
r
u
c
e
s

e
c
n
a
l
l
i
e
v
r
u
s

e
s
r
a
o
c

e
n
fi
e
r

o
t

e
l
b
a

s
a
w
e
l
u
d
o
m

,
s
r
o
r
r
e

t
c
u
r
t
s
n
o
c
e
r

,
s
n
o
i
t
c
i
d
e
r
p

d
n
a

n
o
i
t
c
u
r
t
s
n
o
c
e
r

s
e
l
b
m
e
s
s
a

t
a
h
t

k
r
o
w
e
m
a
r
f

a

e
t
a
e
r
c

d
n
a

t
n
e
m
e
n
fi
e
r

r
o
r
r
e

n
a

h
t
i

w

s
e
l
u
d
o
m
n
o
i
t
c
i
d
e
r
p

n
o
i
t
c
e
t
e
d

-
r
e
p
y
h

e
h
t

g
n
i
n
u
t
-
o
t
u
A

g
n
i
d
l
i
u
B

k
r
o
w
t
e
n

g
n
i
d
o
c

e
v
i
t
c
i
d
e
r
p

e
h
T

y
l
a
m
o
n
a

o
e
d
i
v

e
v
o
r
p
m

I

)
9
1
0
2
(

.
l
a

t
e

e
Y

s
k
r
a
m
e
R

)
s
(
n
o
i
t
a
c
i
l
p
p
A

)
s
(
e
m
o
c
t
u
O

)
s
(
k
s
a
t

n
i
a

M

d
e
y
e
v
r
u
s

y
d
u
t
S

n
o
i
t
p
i
r
c
s
e
d

l
a
r
e
n
e
G

l
e
d
o
M

)
d
e
u
n
i
t
n
o
c
(

2
e
l
b
a
T

1 3

h
c
r
a
e
s
e
r

r
e
h
t
r
u
f

s
d
e
e
n

n
o
i
t

l
a
n
o
i
t
i
d
a
r
t

f
o

e
s
i
o
n

o
t

e
v
i
t
i
s
n
e
s

k
r
o
w
t
e
n

e
l
u
s
p
a
c

l
a
n
o
i
t

-
r
o
f
r
e
p

r
o
o
p

f
o
m
e
l
b
o
r
p

e
h
t

g
n
i
e
b

o
t

e
u
d

;
s
e
u
s
s
i

e
c
n
a
m

e
h
t

d
e
v
l
o
s

)

N
C
S
L
M

(

-
i
d
a
r
t

e
h
t

f
o
m
e
l
b
o
r
p

s
k
r
o
w
t
e
n

e
l
u
s
p
a
c

t
n
u
o
c
c
a

o
t

g
n
i
n
r
u
t

f
o

f
o

y
t
r
e
p
o
r
p

y
r
e
v
e

r
o
f

e
g
a
m

i

n
a

d
e
z
i
l
a
r
e
n
e
g

e
h
t

g
n
i
y
l
p
p
A

n
o
i
t
a
m
r
o
f
n
I

d
e
t
c
i
r
t
s
e
r

f
o

t
i
n
u

g
n
i
d
o
c
n
e

l
e
v
o
N

l
e
v
e
l
-
h
g
i
h

e
h
t
g
n
i
t
c
a
r
t
x
E

13585

e
r
a

t
a
h
t

s
e
l
u
s
p
a
c

y
r
a
m

i
r
p

f
o

s
e
u
l
a
v

y
r
a
n
i
g
a
m

i

d
n
a

y
l
h
g
i
h

d
e
u
l
a
v
-
x
e
l
p
m
o
c

-
o
g
l
a

g
n
i
t
u
o
r

c
i
m
a
n
y
d

-
l
a
e
r

e
h
t

e
s
u
f

o
t

m
h
t
i
r

-

m
a
r
a
p

e
h
t

d
e
s
a
e
r
c
e
d

r
o
f

d
e
n
i
a
r
t

e
b

o
t

s
r
e
t
e

s
l
e
d
o
m
d
e
u
l
a
v
-
x
e
l
p
m
o
c

d
e
u
l
a
v
-
l
a
e
r

o
t

d
e
r
a
p
m
o
c

-
n
e
m
i
d

r
a
l
i

m

i
s

f
o

s
l
e
d
o
m

,
r
e
v
e
w
o
H

.
s
e
l
u
s
p
a
c

n
o
i
s

-
a
t
u
p
m
o
c

d
a
h

s
l
e
d
o
m
e
h
t

y
t
i
x
e
l
p
m
o
c

l
a
n
o
i
t

-
x
e
l
p
m
o
c

e
h
t

n
i

n
o
i
t
a
t
n
e
m
e
l
p
m

i

n
i
a
m
o
d

d
e
u
l
a
v

n
o
i
t
c
a
r
t
x
e

k
r
o
w
t
e
n
e
s
n
e
d

e
u
l
a
v
-
x
e
l
p
m
o
c

d
e
u
l
a
v
-
x
e
l
p
m
o
c

r
e
h
t
o
n
a

h
t
i

w

e
h
t

g
n
i
z
i
l
a
r
e
n
e
g

,
e
l
u
s
p
a
c

-
i
t
l
u
m

f
o

n
o
i
t
a
m
r
o
f
n
i

d
e
u
l
a
v
-
x
e
l
p
m
o
c

e
l
a
c
s

o
t

r
e
d
r
o

n
i

s
e
r
u
t
a
e
f

r
o
f

m
h
t
i
r
o
g
l
a

g
n
i
t
u
o
r

c
i
m
a
n
y
d

s
t
e
s
a
t
a
d

x
e
l
p
m
o
c

t
p
o
d
a

.
l
a

t
e

e
H

.
J

)
9
1
0
2
(

)
0
2
0
2
(

n
o
i
t
a
c
o
l

d
n
a

s
e
r
u
t
a
e
f

n
e
e
w
t
e
b

p
i
h
s
n
o
i
t
a
l
e
r

e
h
t

-
i
r
t
a
m
n
o
i
t
a
m
r
o
f
s
n
a
r
t

s
a

l
l
e
w
s
a

s
e
l
u
s
p
a
c

h
t
i

w

n
o
i
t
a
l
s
n
a
r
t

s
e
r
i
u
q
c
a

h
c
a
o
r
p
p
a

s
i
h
t

e
c
n
i
S

.
s
e
c

l
u
f
r
e
w
o
p

e
r
o
m
e
r
a

s
t
e
N
s
p
a
C

,
e
c
n
a
i
r
a
v
i
u
q
e

d
n
a

l
a
i
t
a
p
s

d
e
l
s
i
m
h
t
i

w
s
e
l
p
m
a
s

r
o
f

N
N
C
n
a
h
t

e
l
o
h
w

-
t
r
a
p

e
d
o
c
n
e

s
t
e
N
s
p
a
C

.
n
o
i
t
a
m
r
o
f
n
i

e
s
o
p

d
n
a

,
s
s
e
n
t
h
g
i
r
b

,
s
n
o
i
t
a
t
n
e
i
r
o

e
k
i
l

s
p
i
h
s
n
o
i
t
a
l
e
r

’
s
t
c
e
j
b
o

e
r
a

t
a
h
t

s
e
i
t
i
t
n
e

t
n
e
r
e
ff
i
d

g
n
o
m
a

s
e
l
a
c
s

,
r
e
v
e
w
o
H

.
n
o
i
t
a
m
r
o
f
n
i

l
a
i
t
a
p
s

e
r
i
u
q
c
a

o
t

N
N
C

n
o
i
t
a
c
fi

i
s
s
a
l
c

n
o

y
l
r
o
o
p
m
r
o
f
r
e
p

s
t
e
N
s
p
a
C
e
h
t

w
o
l
l
a
h
s

e
s
u

y
e
h
T

.
s
t
r
a
p

e
r
u
t
a
e
f

r
o

s
e
r
u
t
a
e
f

n
o
i
t
a
m
r
o
f
n
i

c
i
t
n
a
m
e
s

g
n
i
s
s
i
m

r
o
f

s
k
s
a
t

)
t
e
N
s
p
a
C

(

k
r
o
w
t
e
n

m

s
i
n
a
h
c
e
m

t
u
o
p
o
r
d

e
h
T

-
i
n
g
o
c
e
r

e
g
a
m

I

d
e
v
l
o
s

s
n
o
i
t
c
n
u
f

h
s
a
u
q
s

l
e
v
o
n

e
h
T

h
s
a
u
q
s
-
t
c
i
r
t
s

e
h
T

u
i
L
&
g
n
a
h
C

e
d
o
c
n
e

o
t

s
t
i
n
u

l
a
r
u
e
n

”
e
l
u
s
p
a
c
“

e
s
u

s
t
e
N
s
p
a
C

l
a
r
u
e
n

e
l
u
s
p
a
C

s
k
r
a
m
e
R

)
s
(
n
o
i
t
a
c
i
l
p
p
A

)
s
(
e
m
o
c
t
u
O

)
s
(
k
s
a
t

n
i
a

M

d
e
y
e
v
r
u
s

y
d
u
t
S

n
o
i
t
p
i
r
c
s
e
d

l
a
r
e
n
e
G

l
e
d
o
M

)
d
e
u
n
i
t
n
o
c
(

2
e
l
b
a
T

Deep learning modelling techniques: current progress,…1 3

13586

S. F. Ahmed et al.

m
o
d
n
a
R
e
h
t
h
t
i

w
n
o
s
i
r
a
p

r
o
t
c
e
V

t
r
o
p
p
u
S

,
s
t
s
e
r
o
F

r
o
f

r
e
t
t
e
b

k
r
o
w
s
t
e
N
s
p
a
C

t
a
h
t

e
v
o
r
p

o
t

s
r
e
fi
i
s
s
a
l
c

n
o
i
t
a
c
fi
i
s
s
a
l
c

I
S
H

-

N
N
C
d
n
a

s
e
n
i
h
c
a

M

t
r
a
-
e
h
t
-
f
o
-
e
t
a
t
s

d
e
s
a
b

;
s
t
e
s
a
t
a
d
A
s
n
i
l
a
S
d
n
a
U
P
e
h
t

r
o
f

e
r
u
t
c
e
t
i
h
c
r
a

e
h
T

.
r
e
p
a
p

d
n
a
%
5
4
.
3
9

e
v
a
g
N
N
C
s
a
e
r
e
h
w

y
l
e
v
i
t
c
e
p
s
e
r

s
e
i
c
a
r
u
c
c
a
%
3
6
.
5
9

e
b

o
t

d
e
n
g
i
s
e
d

s
a
w

d
e
t
i

m

i
l

h
t
i

w
d
e
n
i
a
r
t

r
o
f

s
e
l
p
m
a
x
e

g
n
i
n
i
a
r
t

e
g
a
m

I

l
a
r
t
c
e
p
s
r
e
p
y
H

)
I
S
H

(

n
o
i
t
a
c
fi
i
s
s
a
l
C

-
a
c
fi
i
s
s
a
l
c

I
S
H
g
n
i
n
i
a
r
t

-
s
a
l
C
e
g
a
m

I

%
4
9
l
l
a
r
e
v
o

n
a

d
e
v
e
i
h
c
a

e
r
u
t

-

m
o
c

a

e
d
a
m
d
n
a

n
o
i
t

n
o
i
t
a
c
fi
i
s

e
g
a
r
e
v
a

n
o
%
0
9
.
5
9

d
n
a

y
c
a
r
u
c
c
a

s
a
w
e
r
u
t
c
e
t
i
h
c
r
a

s
i
h
t

n
i

d
e
t
n
e
s
e
r
p

r
o
f

t
h
g
u
o
r
b

s
a
w
s
t
e
N
s
p
a
C

l
a
r
t
c
e
p
s
r
e
p
y
H

-
c
e
t
i
h
c
r
a

t
e
N
s
p
a
C
d
e
t
n
e
s
e
r
p

e
h
T

t
e
N
s
p
a
C

r
e
y
a
l
-
o
w

t

A

.
l
a

t
e

g
n
e
D

)
8
1
0
2
(

s
s
e
n
t
s
u
b
o
r

e
h
t

d
e
c
n
a
h
n
e

e
l
u
s
p
a
c

l
a
n
o
i
t
i
d
a
r
t

e
h
t

f
o

-
p
a
C
-
S
M
d
n
a

k
r
o
w
t
e
n

.
s
t
e
N
s
p
a
C

l
a
n
o
i
t
i
d
a
r
t

d
e
m
r
o
f
r
e
p
t
u
o

s
t
e
N
s

s
a
w
s
i
s
y
l
a
n
a

d
e
l
i
a
t
e
d

o
N

k
r
o
w
t
e
n

e
h
t

f
o

d
e
m
r
o
f
r
e
p

-

m
o
c

r
e
v
o

s
e
r
u
t
c
e
t
i
h
c
r
a

s
t
e
s
a
t
a
d

x
e
l
p

n
o
i
t
c
a
r
t
x
e

r
o
f

e
l
b
i
s
n
o
p
s
e
r

s
i

e
g
a
t
s

t
s
r
fi
e
h
t

d
n
a

y
c
n
e
i
c
ffi
e

l
a
n
o
i
t
a
t

l
a
r
u
t
c
u
r
t
s
d
n
a

c
i
t
n
a
m
e
s
g
n
i
n
i
a
t
b
o

-
a
t
n
e
s
e
r
p
e
r

f
o

y
t
i
c
a
p
a
c

-
i
t
l
u
m
g
n
i
y
o
l
p
m
e
y
b
n
o
i
t
a
m
r
o
f
n
i

d
n
a

;
g
n
i
n
r
a
e
l
n
o
i
t
a
m
r
o
f
n
i

e
l
a
c
s

e
l
b
i
s
n
o
p
s
e
r

s
i

e
g
a
t
s
d
n
o
c
e
s

e
h
t

s
l
e
v
e
l
y
h
c
r
a
r
e
i
h
e
h
t
g
n
i
d
o
c
n
e

r
o
f

l
a
n
o
i
s
n
e
m
i
d
-
i
t
l
u
m

r
o
f

s
e
r
u
t
a
e
f

f
o

s
e
l
u
s
p
a
c

l
a
n
o
i
t
i
d
a
r
t

f
o

n
o
i
t

s
k
r
o
w
t
e
n

e
l
u
s
p
a
c

t
u
o
p
o
r
d

d
e
v
o
r
p
m

i

e
h
T

n
o
i
t
a
m
r
o
f
n
I

,
e
r
u
t
c
e
t
i
h
c
r
a
d
e
g
a
t
s
-
o
w

t

a
n
e
e
w
t
e
B

-
u
p
m
o
c

e
h
t

g
n
i
c
n
a
h
n
E

.
l
a

t
e

g
n
a
i
X

)
8
1
0
2
(

s
i

p
e
t
s

g
n
i
n
i
a
r
t

h
c
a
e

d
e
s
a
e
r
c
n
i

t
i

s
a

h
g
i
h

f
o

s
a

t
n
u
o
m
a

e
h
t

h
t
i

w
y
l
r
a
e
n
i
l

s
p
e
t
s

g
n
i
l
l
o
r
n
u

f
o

-
n
i
a
r
t

N
A
G

e
s
p
a
l
l
o
c

e
d
o
m

f
o

s
m
e
l
b
o
r
p

e
h
t

e
h
t

g
n
i
n
fi
e
d

h
g
u
o
r
h
t

-
u
c
c
a

e
s
a
e
r
c
n
i

o
t

e
t
e
p
m
o
c

s
k
r
o
w
t
e
n

l
a
r
u
e
n

o
w

t

l
a
i
r
a
s
r
e
v
d
a

g
n
i

g
n
i
n
i
a
r
t

’
s
N
A
G
d
e
z
i
l
i
b
a
t
s

d
n
a

o
s
l
a

t
I

.
s
r
o
t
a
r
e
n
e
g

t
n
e
r
r
u
c
e
r

h
t
i

w

d
n
a

t
n
e
m

t
r
o
s
s
a

e
h
t

d
e
s
a
e
r
c
n
i

n
o
i
t
u
b
i
r
t
s
i
d

a
t
a
d
f
o

e
p
o
c
s

e
v
i
t
c
e
j
b
o
r
o
t
a
r
e
n
e
g

d
e
l
l
o
r
n
u

g
n
i
d
r
a
g
e
r

e
h
t

f
o

n
o
i
t
a
z
i
m

i
t
p
o

r
o
t
a
n
i
m

i
r
c
s
i
d

d
e
s
i
v
r
e
p
u
s
n
u

s
e
t
a
r
e
p
o

n
e
t
f
o

t
I

.
s
n
o
i
t
c
i
d
e
r
p

e
t
a
r

f
o

e
l
b
a
p
a
c

s
i

t
I

.
n
r
a
e
l
o
t

s
e
m
a
g
m
u
s
-
o
r
e
z

e
v
i
t

.
a
t
a
d

d
e
t
a
r
e
n
e
g

f
o

g
n
i
l
p
m
a
s

e
h
t

g
n
i
z
i
l
e
l
l
a
r
a
p

-
a
r
e
p
o
o
c

n
o

d
e
s
a
b

k
r
o
w
e
m
a
r
f

a

s
e
z
i
l
i
t
u

d
n
a

r
e
d
r
o

n
i

y
l
t
n
a
t
s
n
o
c

d
e
d
i
v
o
r
p

e
b

o
t

d
e
e
n

a
t
a
d

t
o
n

r
o
l
l
e
w
s
e
t
a
r
e
p
o
N
A
G

r
e
h
t
e
h
w
e
n
i
m
r
e
t
e
d

f
o

o
t

s
m
r
o
f

s
u
o
i
r
a
v

s
a

n
i
a
r
t

o
t

r
e
d
r
a
h

s
i

t
i

,
r
e
v
e
w
o
H

k
r
o
w
t
e
n

)

N
A
G

(

t
s
o
c

l
a
n
o
i
t
a
t
u
p
m
o
c

e
h
T

g
n
i
z
i
l
i
b
a
t
S

d
e
v
l
o
s

d
o
h
t
e
m
d
e
c
u
d
o
r
t
n
i

e
h
T

s
N
A
G
g
n
i
z
i
l
i
b
a
t
S

)
7
1
0
2
(

u
a
f
P

h
c
i
h
w
n
i

m
h
t
i
r
o
g
l
a

g
n
i
n
r
a
e
l

e
n
i
h
c
a
m
a

s
i

N
A
G

e
v
i
t
a
r
e
n
e
G

s
k
r
a
m
e
R

)
s
(
n
o
i
t
a
c
i
l
p
p
A

)
s
(
e
m
o
c
t
u
O

)
s
(
k
s
a
t

n
i
a

M

d
e
y
e
v
r
u
s

y
d
u
t
S

n
o
i
t
p
i
r
c
s
e
d

l
a
r
e
n
e
G

l
e
d
o
M

)
d
e
u
n
i
t
n
o
c
(

2
e
l
b
a
T

1 3

s
l
e
b
a
l
h
t
u
r
t
d
n
u
o
r
g
y
f
i
t
n
e
d
i

.
s
e
l
p
m
a
s
g
n
i
n
i
a
r
t
e
h
t

m
o
r
f

o
t
y
l
s
u
o
e
n
a
t
l
u
m

i
s
d
e
k
r
o
w

e
h
t

m
o
r
f
d
e
v
i
e
c
r
e
p
e
r
e
w

s
e
l
p
m
a
s
g
n
i
n
i
a
r
t
e
s
e
h
T

e
t
a
d
i
d
n
a
c
e
h
t
d
n
a
s
e
r
u
t
a
e
f

d
e
z
i
s
e
h
t
n
y
s
d
n
a
d
l
r
o
w

-
l
a
e
r

e
c
n
a
m
r
o
f
r
e
p
t
l
u
s
e
r

t
r
a
-
e
h
t

-
f
o
-
e
t
a
t
s

t
o
g
d
n
a
s
t
e
s
a
t
a
d

s
s
o
r
c
a
l
e
d
o
m
e
h
t
d
e
t
s
e
t

s
r
o
h
t
u
a
e
h
T

.
s
t
n
i
o
p

e
h
t

n
i

d
e
t
n
e
s
e
r
p

o
s
l
a

s
a
w

l
e
d
o
m

e
s
r
e
v
n
i

d
e
m
r
o
f
r
e
p

h
c
i
h
w

r
e
p
a
p

d
n
a

s
l
e
b
a
l

n
e
e
w
t
e
b

s
g
n
i
p
p
a
m

s
e
r
u
t
a
e
f

s
t
c
e
p
s
a
m
o
d
n
a
r
-
n
o
n

d
e
m
r
o
f
r
e
p

-
i
d
n
o
c

e
r
a

h
c
i
h
w
s
l
e
b
a
l

e
s
i
o
n

f
o

-
o
e
r
o
M

.
l
e
b
a
l

e
u
r
t

e
h
t

n
o

d
e
n
o
i
t

s
l
e
v
e
l

o
w

t

h
g
u
o
r
h
t

d
e
s
a
b
l
e
b
a
l

a

f
o

d
e
s
a
b
-
e
r
u
t
a
e
f

a

d
n
a

r
o
t
a
r
e
n
e
g

e
r
u
t
a
e
f

a
t
a
d

e
h
t

,
r
e
v

,
r
o
t
a
r
e
n
e
g

l
a
i
r
a
s
r
e
v
d
a

g
n
i
n
o
i
t
i
d
n
o
c

d
e
m
r
o
f
r
e
p

l
e
d
o
m

a

r
e
d
n
u

d
e
n
g
i
s
e
d

-
c
e
p
s
e
r

e
h
t

n
o

s
e
l
p
m
a
s

a
t
a
d

n
o

g
n
i
p
p
a
m

l
a
n
o
i
t
c
e
r
i
d
i
b

n
o
i
t
c
i
d
e
r
p
A

.
s
l
e
b
a
l

e
u
r
t

e
v
i
t

k
r
o
w
e
m
a
r
f

k
r
o
w
t
e
n

d
o
h
t
e
m
d
e
s
o
p
o
r
p

e
h
T

-
s
a
l
c

t
n
e
m

i
t
n
e
S

t
u
o

d
e
l
l
u
p

h
c
a
o
r
p
p
a

d
e
s
o
p
o
r
p

e
h
T

d
e
s
o
p
o
r
p
s
r
o
h
t
u
a

e
h
T

13587

d
e
l
l
e
b
a
l

d
e
t
a
u
t
i
s

o
s
l
a

d
n
a

e
c
a
p
s

e
r
u
t
a
e
f

d
e
t
c
a
r
t
x
e

-
l
o
d
o
h
t
e
m
d
e
s
o
p
o
r
p

e
h
T

.
n
i
a
m
o
d

h
c
a
e

n
e
e
w
t
e
b

a
t
a
d

d
e
l
e
b
a
l
n
u

d
n
a

d
i
o
v
a

o
t

e
l
b
a

s
a
w
y
g
o

f
o

e
s
a
c

n
i

g
n
i
t
t

fi
r
e
v
o

e
h
t

h
g
u
o
r
h
t

s
n
i
a
m
o
d

s
s
o
r
c
a

a
t
a
d

d
e
n
g
i
l
a

a
t
a
d

d
e
t
i

m

i
l

n
o
i
t
a
c
fi
i
s

-
i
r
a
v
n
i
-
n
i
a
m
o
d

h
t
o
b
f
o

s
e
r
u
t
a
e
f

s
t
x
e
t

c
fi
i
c
e
p
s
-
n
i
a
m
o
d

d
n
a

t
n
a

l
a
u
d

h
t
i

w
g
n
i
n
r
a
e
l
-
o
c

s
k
r
o
w
t
e
n

l
a
i
r
a
s
r
e
v
d
a

f
o

h
c
a
o
r
p
p
a

l
e
v
o
n

a

-
i
t
n
e
s

n
i
a
m
o
d
-
i
t
l
u
m

r
o
f

n
o
i
t
a
c
fi
i
s
s
a
l
c

t
n
e
m

)
0
2
0
2
(

o
u
G
&
u
W

)
0
2
0
2
(

s
r
o
t
a
r
e
n
e
g

o
s
l
a

r
o
t
a
r
e
n
e
g

e
h
T

.
n
o
i
t
a
l
o
p
r
e
t
n
i

r
o
f

n
o
i
t
a
i
r
a
v

e
h
t

d
e
l
g
n
a
t
n
e
s
i
d

e
t
a
r
u
c
c
a

e
r
o
m
g
n
i
d
n
a
t
s
r
e
d
n
u

s
r
o
t
c
a
f

t
n
e
t
a
l

e
h
t

k
r
o
w
t
e
n

r
e
t
t
e
b
m
r
o
f
r
e
p

n
a
c

s
r
o
t

N
A
G

l
a
n
o
i
t
i
d
a
r
t

n
a
h
t

e
r
u
t
c
e
t
i
h
c
r
a

r
o
t
a
r
e
n
e
g

f
o

n
o
i
t
u
b
i
r
t
s
i
d
l
a
r
e
n
e
g

e
h
t

e
h
t

f
o

n
o
i
s
r
e
v

e
t
a
n
r
e
t
l
a

o
t

g
n
i
d
a
e
l

,
s
c
i
r
t
e
m
y
t
i
l
a
u
q

l
a
i
r
a
s
r
e
v
d
a

e
v
i
t
a
r
e
n
e
g

)
9
1
0
2
(

-
a
r
e
n
e
g

d
e
s
a
b
-
e
l
y
t
s

e
h
T

g
n
i
n
g
i
s
e
d
e
R

d
e
v
o
r
p
m

i

r
o
t
a
r
e
n
e
g

d
e
s
o
p
o
r
p

e
h
T

d
e
s
a
b
-
r
e
f
s
n
a
r
t

e
l
y
t
s
A

.
l
a

t
e

s
a
r
r
a
K

s
r
o
t
a
r
e
n
e
g
e
h
t

f
o
h
t
o
B

g
n
i
n
r
a
e
l

l
e
b
a
L

l
e
d
o
m

r
o
t
a
r
e
n
e
g
l
e
b
a
l

e
s
i
o
n

e
h
T

d
e
k
r
o
w

l
e
d
o
m
e
h
T
-

o
u
G
&
n
a
Y

.

Y

s
k
r
a
m
e
R

)
s
(
n
o
i
t
a
c
i
l
p
p
A

)
s
(
e
m
o
c
t
u
O

)
s
(
k
s
a
t

n
i
a

M

d
e
y
e
v
r
u
s

y
d
u
t
S

n
o
i
t
p
i
r
c
s
e
d

l
a
r
e
n
e
G

l
e
d
o
M

)
d
e
u
n
i
t
n
o
c
(

2
e
l
b
a
T

Deep learning modelling techniques: current progress,…1 3

13588

S. F. Ahmed et al.

o
t

t
c
e
p
s
e
r

h
t
i

w

t
c
a
p
m
o
c

s
r
e
t
e
m
a
r
a
p
f
o

r
e
b
m
u
n

a

l
a
u
q
e

n
a

h
t
i

w
n
r
a
e
l

o
t

l
a
r
u
e
n

n
e
d
d
i
h

f
o

r
e
b
m
u
n

M
B
R
C
S

,
r
e
v
e
w
o
H

.
s
t
i
n
u

e
t
a
l
u
m
u
c
c
a

t
o
n

d
l
u
o
c

n
o
i
t
a
m
r
o
f
n
i

m
r
e
t
-
g
n
o
l

l
e
d
o
m
e
h
T

.

M
B
R
C
S
d
e
c
u
d
o
r
t
n
i

g
n
i
l
l
o
r

h
g
u
o
r
h
t

d
e
n
g
i
s
e
d

s
a
w

s
e
d
o
n

s
s
a
l
c

r
i
e
h
t

h
t
i

w
s

M
B
R

e
c
n
e
u
q
e
s

n
o
p
u

e
c
n
e
r
e
f
r
e
t
n
i

s
r
o
h
t
u
a

e
h
t

,
n
o
i
t
a
c
fi
i
s
s
a
l
c

e
m

i
t

o
t

t
c
e
p
s
e
r

h
t
i

w

t
n
e
r
r
u
c
e
R
n
i

e
c
n
e
r
e
f

d
e
t
c
i
r
t
s
e
R

l
a
r
o
p
m
e
T

e
n
i
h
c
a

M
n
n
a
m
z
t
l
o
B

-
o
p
x
e

e
h
t

f
o

s
l
e
d
o
m

f
o

r
e
t
c
a
r
a
h
c

l
a
i
t
n
e
n

g
n
i
t
u
p
m
o
c

t
n
e
i
d
a
r
g

e
r
o
m

s
i

M
B
R
C
S

,
s
N
N
R

e
c
n
e
r
e
f
r
e
t
n
i

c
i
m
a
n
y
d

d
n
a

g
n
i
n
r
a
e
l

n
o
i
t
a
t
n
e
s

-
r
e
t
n
i

d
n
a

g
n
i
n
r
a
e
l

f
o

d
r
a
d
n
a
t
s

o
t

g
n
i
r
a
p
m
o
C

d
n
a

g
n
i
n
r
a
e
L

-
e
r
p
e
r

n
i

s
t
l
u
s
e
r

r
e
t
t
e
b

e
v
e
i
h
c
a

o
T

y
t
l
u
c
ffi
i
d

e
h
t

s
s
e
r
d
d
a

o
T

.
l
a

t
e

n
a
r
T

)
0
2
0
2
(

d
n
a

t
u
p
n
i

f
o

s

m
e
l
b
o
r
p

n
o

h
c
i
h
w
s
e
i
t
i
l
a
d
o
m

t
u
p
t
u
o

t
n
e
m

i
r
e
p
x
e

o
t

t
e
y

e
r
e
w

o
i
d
u
a

,
s
e
g
a
m

i

e
d
u
l
c
n
i

a
t
a
d

o
e
d
i
v

d
n
a

n
o
i
t

-
t
e
b

d
e
w
o
h
s

t
a
h
t

d
e
m
r
o
f
r
e
p

e
r
e
w

-
z
i
l
e
l
l
a
r
a
p

e
r
e
w

t
a
h
t

s
t
l
u
s
e
r

r
e
t

o
t

e
m

i
t

s
s
e
l

d
e
r
i
u
q
e
r

t
i

d
n
a

e
l
b
a

d
e
n
i
a
r
t

e
b

-
r
u
c
e
r

h
t
i

w
d
e
s
n
e
p
s
i
d

n
o
i
t
u
l
o
v
n
o
c
d
n
a

e
c
n
e
r

m
s
i
n
a
h
c
e
m
n
o
i
t
n
e
t
t
a

e
h
t

n
i

d
e
t
n
e
s
e
r
p

s
a
w

r
e
p
a
p

s
l
e
d
o
m
d
e
s
a
b
-
r
e
m
r
o
f
s
n
a
r
T

-
c
e
t
e
d
t
c
e
j
b
O

s
k
s
a
t

n
o
i
t
a
l
s
n
a
r
t

e
n
i
h
c
a
m
o
w
T

d
e
s
a
b
-
r
e
m
r
o
f
s
n
a
r
t

A

)
7
1
0
2
(

i
n
a
w
s
a
V

-
f
u
s

t
u
b

t
e
s

g
n
i
n
i
a
r
t

l
l
a
m

s

l
a
n
o
i
t
a
t
n
e
s
e
r
p
e
r

m
o
r
f

s
r
e
f

s
e
u
s
s
i

y
c
n
e
i
c
ffi
e
n
i

e
c
a
f

,
n
o
i
t

g
n
i
l
l
e
b
a
l

e
t
a
r

r
o
r
r
e

e
n
o
h
p
%
5
.
0
2

a

,
s
N
B
D

h
t
i

w
n
o
i
t
c
n
u
j
n
o
c

n
i

s
e
r
u
t
a
e
f

d
n
a

e
r
u
t
c
e
t
i
h
c
r
a

N
B
D
n
o

d
e
s
a
b

d
e
v
e
i
h
c
a

s
a
w

M
B
R
e
c
n
a
i
r
a
v
o
c
-
n
a
e
m

a

r
o
f

l
u
f
e
s
u

s
i

M
B
R
c
m
e
h
T

-
i
n
g
o
c
e
r

e
n
o
h
P

M
B
R
c
m

f
o

e
s
u

e
h
t

h
g
u
o
r
h
T

d
o
h
t
e
m

l
e
v
o
n

a

p
o
l
e
v
e
D

.
l
a

t
e

l
h
a
D

)
0
1
0
2
(

e
n
o
h
p
r
o
f

)

M
B
R
c
m

(

n
o
i
t
i
n
g
o
c
e
r

e
r
u
t
a
e
f

r
o
f

e
v
i
t
c
e
ff
e

y
r
e
v

m
o
r
f

s
e
s
o
p
r
u
p

n
o
i
t
c
u
d
e
r

g
n
o
l
A

.
s
t
e
s
a
t
a
d

e
g
r
a
l

r
e
b
m
u
n

e
h
t

g
n
i
c
u
d
e
r

h
t
i

w

m
h
t
i
r
o
g
l
a

e
h
t

,
s
e
r
u
t
a
e
f

f
o

-
a
c
fi
i
s
s
a
l
c

d
e
s
a
e
r
c
n
i

d
n
a

e
t
a
r

r
o
r
r
e

d
e
c
u
d
e
r

o
s
l
a

n
o
i
t
a
i
r
a
v

e
m

i
t

o
t

t
c
e
p
s
e
r

h
t
i

w
e
c
n
a
m
r
o
f
r
e
p

n
o
i
t

n
o
i
t

m
o
r
f

n
o
i
t
c
e
l
e
s

e
r
u
t
a
e
f

t
u
p
n
i

r
o
f

-
z
t
l
o
B
p
e
e
D
o
t
n
i

d
e
d
d
e
b
m
e

s
a
w

-
n
r
a
e
l

d
n
a

s
e
r
u
t
a
e
f

t
u
p
n
i

e
c
u
d
e
r

s
t
e
s
a
t
a
d

e
g
r
a
l

m
o
r
f

s
r
o
r
r
e

g
n
i

o
t

s
r
e
fi
i
s
s
a
l
c

s
e
n
i
h
c
a

M
n
n
a
m

m
h
t
i
r
o
g
l
a

e
h
T

.
s
t
e
s
a
t
a
d

e
g
r
a
l

d
e
b
m
e

o
t

d
o
h
t
e
m
n
o
i
t

-
z
t
l
o
B
d
e
t
c
i
r
t
s
e
R
a

n
i

-
c
e
l
e
s

e
r
u
t
a
e
f

e
u
q
i
n
u

a

d
e
c
u
d
o
r
t
n
i

k
r
o
w

e
n
i
h
c
a

M
n
n
a
m

)
8
1
0
2
(

-
i
h
c
r
a

s
t
I

.
h
c
a
o
r
p
p
a

d
e
s
i
v
r
e
p
u
s
-
i

m
e
s

a

n
i

d
e
n
i
a
r
t

e
g
d
e
l
w
o
n
k

e
r
i
u
q
c
a

o
t

k
r
o
w
t
e
n

e
h
t

s
w
o
l
l
a

e
r
u
t
c
e
t

,
n
o
i
t
i
n
g
o
c
e
r

t
x
e
t

,
n
o
i
t
i
n
g
o
c
e
r

n
o
i
s
s
e
r
p
x
e

l
a
i
c
a
f

e
k
i
l

s
n
o
i
t
a
c
i
l
p
p
a

f
o

e
g
n
a
r

e
d
i
w
a

e
v
a
h

s

M
B
D

.
s
p
i
h
s
n
o
i
t
a
l
e
r

d
e
s
a
b
-
e
r
u
t
a
e
f

x
e
l
p
m
o
c

t
u
o
b
a

D
3

,
a
t
a
d

l
a
u
s
i
v
-
o
i
d
u
a
m
o
r
f

n
o
i
t
a
c
fi

i
t
n
e
d
i

n
o
s
r
e
p

e
r
o
m
y
n
a
m
d
n
a

,
n
o
i
t
i
n
g
o
c
e
r

l
e
d
o
m

s
i

m
h
t
i
r
o
g
l
a

l
e
v
o
n

e
h
T

-
c
e
l
e
s

e
r
u
t
a
e
F

d
e
s
o
p
o
r
p

s
a
w
m
h
t
i
r
o
g
l
a

l
e
v
o
n
A

h
c
r
a
e
s
e
r

d
e
s
o
p
o
r
p

e
h
T

.
l
a

t
e

i
n
a
h
k
r
e
h
a
T

s
i

t
a
h
t

e
r
u
t
c
e
t
i
h
c
r
a

k
r
o
w
t
e
n

l
a
r
u
e
n

p
e
e
d

a

s
i

M
B
D

s
k
r
a
m
e
R

)
s
(
n
o
i
t
a
c
i
l
p
p
A

)
s
(
e
m
o
c
t
u
O

)
s
(
k
s
a
t

n
i
a

M

d
e
y
e
v
r
u
s

y
d
u
t
S

n
o
i
t
p
i
r
c
s
e
d

l
a
r
e
n
e
G

n
n
a
m
z
t
l
o
B

s
e
n
i
h
c
a

M

)

M
B
D

(

l
e
d
o
M

p
e
e
D

)
d
e
u
n
i
t
n
o
c
(

2
e
l
b
a
T

1 3

13589

-
i
t
s
e
v
n
i

o
t

y
r
a
s
s
e
c
e
n

s
i

t
I

,
g
n
i
x
e
d
n
I

f
o

d
e
t
s
i
s
n
o
c

d
o
h
t
e
m
g
n
i
n
i
a
r
t

e
h
T

k
r
o
w
t
e
n

l

n
a
m
E
g
n
i
s
U

.
l
a

t
e
u
o
i
L

.
r
e
d
o
c
n
e
o
t
u
a

d
e
k
c
a
t
s

e
h
t

f
o
n
o
i
s
n
a
p
x
e

n
a

s
i

E
A
D
S

s
k
r
a
m
e
R

)
s
(
n
o
i
t
a
c
i
l
p
p
A

)
s
(
e
m
o
c
t
u
O

)
s
(
k
s
a
t

n
i
a

M

d
e
y
e
v
r
u
s

y
d
u
t
S

n
o
i
t
p
i
r
c
s
e
d

l
a
r
e
n
e
G

l
e
d
o
M

d
e
k
c
a
t
S

d
e
c
u
d
e
r

r
e
h
t
e
h
w
e
t
a
g

e
l
b
a
n
i
a
t
t
a

e
r
e
w
s
r
o
r
r
e

e
h
t

d
n
a

s
e
d
o
c

d
e
s
i
v
e
r

e
h
t

g
n
i
z
i
l
i
t
u

t
u
o
h
t
i

w

s
d
o
h
t
e
m
e
m
a
s

s
k
s
a
t

y
r
a

d
e
n
i
a
r
t

e
h
T

.
g
n
i
d
o
c

y
p
o
r
t
n
e

g
n
i

y
p
o
r
t
n
e

d
e
c
u
d
e
r

d
a
h

s
e
d
o
c

-
u
p
m
o
c

h
g
i
h

a

s
a
h

t
i

,
r
e
v
e
w
o
H

.
h
g
u
o
r
h
t

d
e
s
s
a
p

s
i

a
t
a
d

t
u
p
n
i

s
a

r
e
y
a
l

y
b

r
e
y
a
l

s
r
u
c
c
o

h
c
i
h
w

t
s
o
c

l
a
n
o
i
t
a
t

d
n
a

,
g
n
i
k
n
a
r

-
a
z
i
r
o
g
e
t
a
c

-
r
e
t
i
l

f
o

n
o
i
t

-
a
p
e
s

o
t
n
i

d
r
o
w
h
c
a
e

g
n
i
d
o
c
n
e

d
r
o
w
h
t
i

w
k
r
o
w
o
t

)
4
1
0
2
(

d
e
t
c
e
n
n
o
c

e
r
a

s
r
e
d
o
c
n
e
o
t
u
a

g
n
i
s
i
o
n
e
d

l
a
r
e
v
e
S

g
n
i
s
i
o
n
e
d

-
d
n
o
p
s
e
r
r
o
c

o
t

d
e
t
a
l
e
r

s
a
w

t
i

d
n
a

k
r
o
w
e
r
u
t

e
c
a
p
s

c
i
t
n
a
m
e
s

n
i

s
r
o
t
c
e
v

e
t
a
r

-
a
r
e
t
i
l

m
o
r
f

s
e
c
n
e
u
q
e
s

,
g
n
i
n
i
a
r
t
-
e
r
p

d
e
s
i
v
r
e
p
u
s
n
u
s
i

E
A
D
S
f
o

e
r
u
t
a
e
f

)
E
A
D
S
(

t
n
a
t
r
o
p
m

i

n
A

.

E
A
D
S
a
m
r
o
f

o
t

n
i
a
h
c

a

n
i

s
r
e
d
o
c
n
e
o
t
u
a

)
d
e
u
n
i
t
n
o
c
(

2
e
l
b
a
T

Deep learning modelling techniques: current progress,…1 3

13590

S. F. Ahmed et al.

well as the main surveyed studies in terms of their main objectives, outcomes, and applica-
tions, have been summarized in Table 2.

5   Advantages and challenges of deep learning models

The  several  advantages  underpinning  deep  learning  models,  including  image  processing
and recognition, speech recognition, self-driving cars, and so on, have sparked such wide-
spread  attention.  The  main  benefit  of  using  deep  learning  models  over  machine  learning
(ML)  technologies  is  their  capacity  to  produce  new  features  through  a  limited  range  of
features in the trained dataset (Kotsiopoulos et al. 2021). These models can generate new
tasks for solving current ones as well as they also cover a variety of human life aspects.
A significant amount of time can be saved using deep learning models when dealing with
massive  datasets,  as  deep  learning  algorithms  can  generate  features  without  the  need  for
human intervention (Gupta et al. 2021).

Despite their numerous advantages, deep learning models have a number of noticeable
challenges. First, they are unable to provide arguments supporting the fact that a particular
conclusion is reached (Signorelli 2018). In addition, unlike typical machine learning, peo-
ple are not able to follow an algorithm to figure out why the system decides that the image
portrayed is a dog rather than a cat. To correct these types of errors in deep learning algo-
rithms,  the  entire  algorithm  must  be  revised,  which  requires  additional  time.  Also,  high-
performance computing units, high powerful GPUs and enormous quantities of storage are
needed to train the models. Therefore, deep learning models require more time compared
to traditional ML methods (Palanichamy 2019). The challenges of applying the deep learn-
ing models are summarized in Table 3 along with their advantages.

In  general,  deep  learning  (DL)  often  produces  better  results  as  opposed  to  machine
learning. For example, the largest data portion of an institute/organization is unstructured
since  it  appears  in  so  many  different  formats,  including  texts  and  images.  Most  machine
learning (ML) algorithms struggle to make sense of unstructured data, therefore this type
of data is underutilized. Herein lies the strength of deep learning. The main benefit of using
DL over other ML algorithms is its capacity to produce novel features from limited sets of
features  already  present  in  the  training  dataset.  It  follows  that  DL  algorithms  can  devise
new challenges to address existing problems. DL enables full-cycle learning by using neu-
ral networks’ capability for featurization, from inputting raw data to producing an outcome.
This  approach  allows  for  the  optimization  of  all  relevant  parameters,  which  ultimately
results in improved precision.

A  key  advantage  of  using  the  DL  approach  is  that  it  can  perform  feature  engineering
on its own. In this method, the algorithm is not given any explicit instructions, but rather
it  automatically  searches  through  the  data  for  features  that  correlate  and  then  combines
them to facilitate faster learning. Because of its ability to handle massive data, DL scales
extremely  well.  The  algorithms  of  DL  can  be  learned  on  a  wide  range  of  data  formats
while  still  producing  insights  relevant  to  the  objectives  of  the  training.  For  instance,  DL
algorithms can be utilized to identify correlations between social media activities, market
research, and other factors in order to predict the future stock value of a particular firm.

There are a number of issues with DL models as well. In order to outperform alternative
methods, deep learning needs access to a massive dataset. Therefore managing data is the
key  challenge  that  hinders  DL  in  industrial  implementations.  Deep  learning  is  currently

1 3
13591

h
c
t
a
m
a

g
n
i
s
u
a
c

,
d
e
t
a
i
c
o
s
s
a

e
b

t
o
n

l
l
i

w
y
r
a
l
u
b
a
c
o
v
m
r
e
t

t
c
n
i
t
s
i
d

a

d
n
a

t
x
e
t
n
o
c

r
a
l
i

m

i
s

a

h
t
i

w
s
r
e
p
a
p

;
s
c
i
t
n
a
m
e
s

o
t

y
t
i
v
i
t
i
s
n
e
S
-

"
e
v
i
t
a
g
e
n

e
s
l
a
f
"

f
o

y
r
e
v
t
o
n

s
i

t
i

h
g
u
o
h
t
l
a

,
e
v
i
t
i
u
t
n
i

s
i

g
n
i
t
h
g
i
e
w

f
o

s
s
e
c
o
r
p
e
h
T
-

l
a
m
r
o
f

h
c
u
m

t
n
e
d
n
e
p
e
d
n
i

y
l
l
a
c
i
t
s
i
t
a
t
s

e
b

o
t

d
e
m
u
s
s
a

e
r
a

s
m
r
e
t

,
y
l
l
a
c
i
t
e
r
o
e
h
T
-

s
u
h
t

d
n
a

,
s
t
n
e
m
u
c
o
d

t
c
n
i
t
s
i
d

g
n
o
m
a

s
e
i
t
i
r
a
l
i

m
i
s

s
e
fi

i
t
n
e
d
I

-

t
a
h
t

s

m
r
e
t

e
h
t

f
o

r
e
d
r
o

e
h
t

,
e
c
a
p
s

r
o
t
c
e
v

f
o

n
o
i
t
a
t
n
e
s
e
r
p

e
h
t

n
I

-

m
s
i
r
a
i
g
a
l
p

t
c
e
t
e
d

o
t

s
t
s
i
s
s
a

t
s
o
l

s
i

s
t
n
e
m
u
c
o
d
e
h
t

n
i

d
e
r
a
e
p
p
a

r
a
e
n
i
l

f
o
s
i
s
a
b
e
h
t

n
o

d
e
t
c
u
r
t
s
n
o
c

s
i

t
i

s
a

e
r
u
t
c
u
r
t
s

n
i

e
l
p
m
S
-

i

y
t
e
i
r
a
v
a

d
n
a

y
r
e
u
q
c
fi
i
c
e
p
s

a

r
o
f

s
t
n
e
m
u
c
o
d

t
x
e
t

t
n
a
v
e
l
e
r

"

e
v
i
t
i
s
o
p

e
s
l
a
f
"

f
o

h
c
t
a
m
a

o
t

d
a
e
l

n
a
c

s
g
n
i
r
t
s
b
u
s

d
r
o
w

;
t
n
e
m

e
r
a

s
r
e
p
a
p
/
s
t
n
e
m
u
c
o
d

g
n
o
l

,
s
e
u
l
a
v

y
t
i
r
a
l
i

m
i
s
w
o
l

r
i
e
h
t

o
t

e
u
D

-

-
u
c
o
d

e
h
t

n
i

s

m
r
e
t

e
h
t

h
c
t
a
m
y
l
t
c
a
x
e

t
s
u
m
h
c
r
a
e
s

s
d
r
o
w
y
e
K

-

g
n
i
h
c
t
a
m

l
a
i
t
r
a
p

r
o
f

s
t
i

m
r
e
P
-

y
r
a
n
i
b

t
o
n

e
r
a

s
t
h
g
i
e
w
m
r
e
T
-

a
r
b
e
g
l
a

m
y
n
o
n
y
s

d
n
a

y
m
e
s
y
l
o
p
m
o
r
f

s
r
e
ff
u
S
-

e
l
a
c
s

s
u
o
u
n
i
t
n
o
c

a

n
o
s
e
i
r
e
u
q

d
n
a

s
t
n
e
m
u
c
o
d

d
e
t
n
e
s
e
r
p
e
r

y
l
r
o
o
p

n
e
e
w
t
e
b

e
e
r
g
e
d

y
t
i
r
a
l
i

m
i
s

e
h
t

f
o

n
o
i
t
a
t
u
p
m
o
c

e
h
t

r
o
f

s
w
o
l
l

A

-

y
t
i
u
g
i
b
m
a

c
i
t
s
i
u
g
n
i
l

h
t
i

w
g
n
i
p
o
c

f
o
e
l
b
a
p
a
c
n
i

s
i

M
S
V

l
a
u
t
x
e
T
-

t
s
o
m
e
h
t

g
n
i
t
a
r

d
n
a

g
n
i
y
f
i
t
n
e
d
i

y
b
s
t
n
e
m
u
c
o
d

d
e
v
e
i
r
t
e
r

s
k
n
a
R

-

)

M
S
V

(

l
e
d
o
m
e
c
a
p
s

r
o
t
c
e
V

s
e
g
n
e
l
l
a
h
C

s
e
g
a
t
n
a
v
d
A

s
l
e
d
o
m
g
n
i
n
r
a
e
l

p
e
e
D

s
e
u
q
i
n
h
c
e
t

g
n
i
l
l
e
d
o
m
g
n
i
n
r
a
e
l

p
e
e
d

f
o

s
e
g
n
e
l
l
a
h
c

d
n
a

s
e
g
a
t
n
a
v
d
A

3
e
l
b
a
T

s
a

l
l
e
w
s
a

,
n
i
a
r
t

o
t

d
e
r
i
u
q
e
r

e
r
a

s
t
e
s

a
t
a
d

r
e
g
r
a
l

y
l
e
v
i
t
a
r
a
p
m
o
C

-

N
N
C
n
i

d
e
r
i
u
q
e
r

e
h
t

f
o

y
t
i
x
e
l
p
m
o
c

e
h
t

m
o
r
f

g
n
i
s
i
r
a

s
e
g
n
e
l
l
a
h
c

n
o
i
t
a
z
i
m

i
t
p
O

-

-
a
t
n
e
i
r
o
m
e
t
s
y
s

,
d
n
u
o
r
g
k
c
a
b

x
e
l
p
m
o
c

s
a

h
c
u
s

s
e
c
n
a
t
s
m
u
c
r
i
c

e
s
i
t
r
e
p
x
e

n
i
a
m
o
d

s
e
r
i
u
q
e
r

h
c
i
h
w

,
n
o
i
t
a
t
o
n
n
a

t
c
e
r
r
o
c

g
n
i
g
n
e
l
l
a
h
c

t
n
e
r
e
ff
i
d

r
e
d
n
u

t
s
u
b
o
r

d
e
r
e
d
i
s
n
o
c

e
r
a

s
l
e
d
o
m
e
h
T
-

y
c
a
r
u
c
c
a

d
n
a

e
c
n
a
m
r
o
f
r
e
p

t
o
n
s
i

t
a
h
t

g
n
i
s
s
e
c
o
r
p

e
g
a
m

i

n
i

y
l
l
a
n
o
i
t
i
d
a
r
t

d
e
s
u

s
s
e
c
o
r
p

a
t
a
d

n
i
a
r
t

o
t

e
m

i
t

r
e
g
n
o
l

a

e
k
a
t

s
e
m

i
t
e
m
o
S
-

y
l
l
a
i
t
n
a
t
s
b
u
s

s
i

e
m

i
t

g
n
i
t
s
e
t

f
o

y
c
n
e
i
c
ffi
e

e
h
t

,
g
n
i
n
i
a
r
t

r
e
t
f

A

-

s
n
o
i
t
a
t
i

m

i
l

e
r
a
w
d
r
a
h

d
n
a

,
s
l
e
d
o
m

n
o
i
t
a
n
i
m
u
l
l
i

d
n
a

,
s
n
o
i
t
u
l
o
s
e
r

s
u
o
i
r
a
v

,
e
z
i
s

d
n
a

n
o
i
t

U
P
G
d
a
b

a

g
n
i
s
u

n
i
a
r
t

o
t

e
m

i
t

e
r
o
m
s
e
k
a
T
-

n
o
i
t
a
c
fi
i
s
s
a
l
c

n
i

e
m

i
t

s
s
e
l

s
e
r
i
u
q
e
R

h
g
i
h
s
i

t
s
o
c

l
a
n
o
i
t
a
t
u
p
m
o
C

-

M
V
S
g
n
i
d
u
l
c
n
i

s
e
h
c
a
o
r
p
p
a

r
e
h
t
o

f
o

t
a
h
t

n
a
h
t

r
e
h
g
i
h

l
a
c
i
t
i
r
c

t
c
e
t
e
d

n
a
c

y
l
l
a
c
i
t
a
m
o
t
u
a

,
n
o
i
s
i
v
r
e
p
u
s

n
a
m
u
h

t
u
o
h
t
i

W

-

-

n
o
i
t
i
n
g
o
c
e
r

e
g
a
m

i

f
o
s
m
e
l
b
o
r
p

e
h
t

n
i

n
o
i
s
i
c
e
r
p

h
g
i
H

-

s
r
e
t
e
m
a
r
a
p

m
e
t
s
y
s

e
c
u
d
e
r

y
l
t
n
a
c
fi
i
n
g
i
s

n
a
c

h
c
i
h
w

,
g
n
i
l
l
e
b
a
l

a
t
a
d

r
o
o
P
-

d
e
t
a
c
i
l
p
m
o
c

d
n
a

g
n
i
m
u
s
n
o
c
-
e
m

i
t

a

s
i

g
n
i
r
e
e
n
i
g
n
e

e
r
u
t
a
e
F
-

)

N
N
C

(

k
r
o
w
t
e
n

l
a
r
u
e
n
l
a
n
o
i
t
u
l
o
v
n
o
C

Deep learning modelling techniques: current progress,…1 3

13592

S. F. Ahmed et al.

t
o
n
n
a
c

t
i

,
e
r
u
t
a
e
f

g
n
i
t
a
v
i
t
c
a

n
a

s
a

d
e
s
u

s
i

h
n
a
T
r
o

u
l
e
R
n
e
h
W

N
N
C
n
a
h
t

l
u
f
r
e
w
o
p
s
s
e
l

s
i

N
N
R

-

-

-
b
o
r
p

l
a
n
o
i
t
a
t
u
p
m
o
c

r
o
f

N
N
R
n
a

n
i
a
r
t

o
t

e
m

i
t

g
n
o
l

a

s
e
k
a
t

t
I

-

s
m
e
l

e
h
t

f
o

e
r
u
t
c
u
r
t
s

e
h
t

g
n
i
w
o
n
k

t
u
o
h
t
i

w
d
e
s
s
e
r
g
o
r
p

e
b

t
o
n
n
a
c

t
I

-

e
l
p
m
a
s

t
u
p
n
i

h
c
a
e

r
o
f

e
e
r
t

N
N
R
y
b

d
e
s
s
e
c
o
r
p
e
b

n
a
c

t
u
p
n
i

f
o

h
t
g
n
e
l

y
n
A

-

n
r
a
e
l

o
t

s
d
e
e
n

k
r
o
w
t
e
n

e
h
t

s
r
e
t
e
m
a
r
a
p

e
h
t

s
t
i

f
o

e
s
u
a
c
e
b
w
o
l
s

y
l
e
v
i
t
a
r
a
p
m
o
c

s
i

s
s
e
c
o
r
p

n
o
i
t
a
t
u
p
m
o
c

e
h
T
-

-
n
e
m
i
d
t
u
p
n
i

e
h
t

n
e
v
e

t
n
a
t
s
n
o
c

s
n
i
a
m
e
r

n
o
i
s
n
e
m
i
d

l
e
d
o
m
e
h
T
-

e
r
u
t
a
n

t
n
e
r
r
u
c
e
r
/
d
e
t
a
e
p
e
r

d
e
s
a
e
r
c
n
i

s
i

n
o
i
s

a

t
i

s
e
k
a
m

s
l
e
v
e
l
/
s
r
e
y
a
l

e
h
t

s
s
o
r
c
a

n
o
i
t
a
m
r
o
f
n
i

f
o
w
o
fl
e
h
T
-

s
n
o
i
t
a
l
e
r
r
o
c
m
r
e
t
-
g
n
o
l

s
a

l
l
e
w
s
a

s
e
c
n
e
u
q
e
s

g
n
o
l

y
l
g
n
i
d
e
e
c
x
e

e
l
d
n
a
h

,
s
c
i
m
a
n
y
d

r
a
e
n
i
l
n
o
n

e
l
d
n
a
h

o
t

s
N
N
R
w
o
l
l
a

s
t
u
p
n
i

s
e
i
r
e
s

e
m
T
-

i

k
s
a
t

h
s
i
r
a
m
t
h
g
i
n

g
n
i
t
i

m

i
l

,
s
r
e
y
a
l

e
h
t

l
l
a

r
e
v
o

e
m
a
s

e
h
t

s
n
i
a
m
e
r

t
h
g
i
e
w

,

N
N
R
n
I

-

w
o
l
s

d
n
a

x
e
l
p
m
o
c

e
r
a

s
e
s
s
e
c
o
r
p

g
n
i
n
i
a
r
T
-

s
t
u
p
n
i

s
u
o
i
v
e
r
p

f
o

r
e
d
n
i
m
e
r

a

s
a

s
k
r
o
w

t
n
i
o
p

s
e
c
n
e
u
q
e
s

r
e
g
n
o
l

s
t
i

m

i
l

d
o
o
h
r
o
b
h
g
i
e
n

l
e
x
i
p
e
v
i
t
c
e
ff
e

e
h
t

d
n
e
t
x
e

o
t

s
r
e
y
a
l

p
u

k
c
a
t
s

o
t

e
l
b
a
n
U

-

t
h
g
i
l
h
g
i
h

e
h
t

e
c
n
i
s

s
e
i
r
e
s

e
m

i
t

g
n
i
t
s
a
c
e
r
o
f

n
i

s
u
o
e
g
a
t
n
a
v
d
a

s
i

t
I

-

h
c
i
h
w

,
e
u
s
s
i

g
n
i
h
s
i
n
a
v

g
n
i
d
o
l
p
x
e

d
n
a

t
n
e
i
d
a
r
g
m
o
r
f

s
r
e
ff
u
S
-

l
a
n
o
i
t
u
l
o
v
n
o
c

h
t
i

w
n
o
i
t
c
n
u
j
n
o
c

n
i

d
e
s
u

y
l
t
n
e
u
q
e
r
f

e
r
a

s
N
N
R

-

)

N
N
R

(

k
r
o
w
t
e
n

l
a
r
u
e
n

t
n
e
r
r
u
c
e
R

s
e
g
n
e
l
l
a
h
C

s
e
g
a
t
n
a
v
d
A

s
l
e
d
o
m
g
n
i
n
r
a
e
l

p
e
e
D

)
d
e
u
n
i
t
n
o
c
(

3
e
l
b
a
T

-
k
a
m
e
r
o
f
e
b

e
c
n
e
u
q
e
s

e
r
i
t
n
e

e
h
t

o
t

s
s
e
c
c
a

e
v
a
h

o
t

y
r
a
s
s
e
c
e
n
s
i

t
I

-

-
t
e
n

l
a
r
u
e
n
t
n
e
r
r
u
c
e
r

l
a
n
o
i
t
c
e
r
i
d
i
b

f
o
s
n
o
i
s
n
e
t
x
e

e
h
t

h
g
u
o
r
h
t

h
c
e
e
p
s

e
m

i
t
-
l
a
e
r

f
o

s
n
o
i
t
a
c
i
l
p
p
a

e
h
t

n
i

e
l
b
a
t
i
u
s

e
b

t
o
n

y
a
M

-

y
l
e
v
i
t
a
r
a
p
m
o
c

e
r
a

y
c
a
r
u
c
c
a

d
n
a

y
c
n
e
i
c
ffi
e

s
t
i

,
s
e
s
a
c

t
s
o
m
n
I

-

N
N
R
n
a

n
a
h
t

s
r
e
t
e
m
a
r
a
p
e
r
o
m

y
h
c
r
a
r
e
i
h

r
e
fi
i
s
s
a
l
c

a

e
t
u
t
i
t
s
n
o
c

n
a
c

k
r
o
w
t
e
n

e
h
t

n
i

r
e
y
a
l

h
c
a
E
-

n
o
i
t
i
n
g
o
c
e
r

d
e
t
c
u
r
t
s
n
o
c

s
i

N
N
R
B
H
e
h
t

s
a

s
k
r
o
w
t
e
n

r
e
h
t
o

e
h
t

n
a
h
t

r
e
t
t
e
b

-
i
r
p
o
r
p
p
a

e
b
t
o
n

y
a
m

t
i

,
s
d
r
o
w
e
r
u
t
u
f

s
e
t
a
p
i
c
i
t
n
a
N
N
R
B
H
e
c
n
i
S
-

e
m

i
t

e
v
i
t
i
s
o
p

d
n
a

e
v
i
t
a
g
e
n

h
t
o
b
s
t
s
a
c
e
r
o
f

y
l
s
u
o
e
n
a
t
l
u
m
S
-

i

s
n
o
i
t
c
i
d
e
r
p

g
n
i

N
N
R
d
n
a

)

N
N
R
B

(

k
r
o
w

s
i
h
t

n
I

.
s
e
n
o

r
o
i
r
p
e
h
t

n
o

d
e
s
a
b

d
r
o
w

t
x
e
n
e
h
t

t
s
a
c
e
r
o
f

o
t

e
t
a

y
c
a
r
u
c
c
a

n
o
i
t
c
i
d
e
r
p

r
e
t
t
e
b

r
o
f

d
e
d
e
e
n
e
r
a

s
t
e
s
a
t
a
d

e
g
r
a
L
-

y
c
a
r
u
c
c
a

r
o
o
p

n
i

t
l
u
s
e
r

l
l
i

w
N
N
R
B
H
g
n
i
s
u

,
e
s
a
c

s
n
o
i
t
c
e
r
i
d

g
n
i
r
e
d
i
s
n
o
c

f
o

e
s
u
a
c
e
b

y
t
i
x
e
l
p
m
o
c

l
a
n
o
i
t
a
t
u
p
m
o
c
m
o
r
f

s
r
e
ff
u
S
-

k
r
o
w
t
e
n

e
r
i
t
n
e

e
h
t

f
o

s
s
e
n
e
v
i
t
c
e
ff
e

e
h
t

n
i

e
l
o
r

l
a
c
i
t
i
r
c

a

s
y
a
l
p

)

N
N
R
B
H

(

k
r
o
w
t
e
n

l
a
r
u
e
n

e
c
n
e
u
q
e
s

e
h
t

f
o

d
n
e

d
n
a

g
n
i
n
n
i
g
e
b

e
h
t

h
t
o
b

f
o

n
w
o
n
k
e
b

t
s
u
M

-

d
n
a

s
k
s
a
t

n
o
i
t
a
c
fi
i
s
s
a
l
c

s
e
l
d
n
a
h
N
N
R
B
H
e
h
t

n
i

r
e
y
a
l

h
c
a
E
-

t
n
e
r
r
u
c
e
r

l
a
n
o
i
t
c
e
r
i
d
i
b

l
a
c
i
h
c
r
a
r
e
i
H

1 3

13593

g
n
i
r
u
d

n
w
o
n
k

e
b

o
t

d
e
e
n

s
e
l
p
m
a
s

t
u
p
n
i

e
h
t

f
o
s
e
r
u
t
c
u
r
t
s

e
e
r
T
-

-
n
e
g
a
t
e
m
g
n
i
y
f
i
s
s
a
l
c

s
a

h
c
u
s

s
k
s
a
t

n
o
i
t
a
z
i
r
o
g
e
t
a
c

r
o
f

l
u
f
e
s
U

t
n
e
i
d
a
r
g

g
n
i
h
s
i
n
a
v

h
t
i

w
m
e
l
b
o
r
p
a

s
e
c
a
f

t
I

-

s
k
r
o
w
t
e
n

l
a
r
u
e
n

h
p
a
r
g

d
n
a

s
k
r
o
w
t
e
n

e
r
u
t
c
u
r
t
s

e
k
i
l
-
e
e
r
t

e
h
t

n
r
a
e
l

o
t

d
e
z
i
l
i
t
u

e
b

n
a
c

t
I

s
e
n
e
c
s

-

-

w
o
l
s

d
n
a

c
fi
i
c
e
p
s
-
n
i
a
m
o
d

s
i

g
n
i
s
r
a
P
-

-

m
o
c

e
r
a

h
c
i
h
w
s
e
l
p
m
a
s

e
h
t

g
n
i
y
f
i
t
n
e
d
i

f
o

e
l
b
a
p
a
c

s
i

N
N
v
R

-

d
o
i
r
e
p

g
n
i
n
i
a
r
t

e
h
t

s
e
i
g
o
l
o
h
p
r
o
m
e
l
p
m
a
s

c
i
m
o

s
k
r
o
w
t
e
n
l
a
r
u
e
n
e
v
i
s
r
u
c
e
r

e
h
t

,
y
t
i
x
e
l
p
m
o
c

c
i
s
n
i
r
t
n
i

e
h
t

o
t

e
u
D

e
c
n
a
i
l
e
r

e
c
n
a
t
s
i
d
-
g
n
o
l

f
o
m
e
l
b
o
r
p

e
h
t

y
b

d
e
t
c
i
ffl
a

s
i

N
N
v
R

-

-

g
n
i
r
o
c
s

e
h
t

f
o
s
i
s
a
b

e
h
t

n
o

r
e
h
t
o
n
a

e
n
o

o
t

r
a
l
i

m
i
s

y
l
e
v
i
t
a
r
a
p

n
o
i
t
c
n
u
f

t
o
n

s
i

t
a
h
t

s
t
e
s
r
e
p
u
s

s
t
i

d
n
a
m
a
r
g
i
b

y
r
e
v
e

r
o
f

d
e
r
i
u
q
e
r

e
r
a

s
l
e
b
a
L
-

s
e
l
p
m
a
s

e
h
t

n
e
e
w
t
e
b

-
t
a
i
c
u
r
c
x
e

s
i

s
N
N
v
R

r
o
f

a
t
a
d

d
e
l
l
e
b
a
l

g
n
i
n
i
a
t
b
o

f
o

s
s
e
c
o
r
p
e
h
T
-

s
e
r
u
t
a
e
f

l
a
n
o
i
s
n
e
m
i
d
-
h
g
i
h

f
o

n
o
i
t
a
t
n
e
s
e
r
p
e
r

a

s
e
d
i
v
o
r
P
-

e
s
a
h
p

g
n
i
n
r
a
e
l

e
h
t

g
n
i
r
u
d

e
v
i
s
n
e
p
x
e

e
t
i
u
q

y
l
l
a
n
o
i
t
a
t
u
p
m
o
C

-

k
r
o
w
t
e
n

l
a
r
u
e
n

e
v
i
s
r
u
c
e
r

g
n
i
m
u
s
n
o
c
-
e
m

i
t

d
n
a

t
l
u
c
ffi
i
d

y
l
g
n
i

p
i
h
s
n
o
i
t
a
l
e
r

l
a
c
i
h
c
r
a
r
e
i
h

e
k
i
l
-
e
e
r
t

a

g
n
i
t
a
r
e
n
e
g

f
o

e
l
b
a
p
a
C

-

d
e
t
a
c
i
l
p
m
o
c

y
l
l
a
c
i
s
n
i
r
t
n
i

e
r
a

e
h
t

g
n
i
s
u
s
p
i
h
s
n
o
i
t
a
l
e
r

s
s
a
l
c

h
t
i

w
d
e
t
a
t
o
n
n
a

e
b

n
a
c

a
t
a
d

e
r
u
t
u
F
-

d
l
r
o
w

l
a
e
r

n
i

d
n
fi
o
t

y
s
a
e

s
k
s
a
t

g
n
i
n
r
a
e
l

d
e
s
i
v
r
e
p
u
s
n
u

d
n
a

d
e
s
i
v
r
e
p
u
s

h
t
o
b

r
o
f

e
l
b
a
t
i
u
S
-

-
a
c
fi
i
s
s
a
l
c

d
n
a

n
o
i
s
s
e
r
g
e
r

h
t
o
b

g
n
i
s
s
e
r
d
d
a

f
o

e
l
b
a
p
a
c

s
i

t
i

s
a

s
m
e
l
b
o
r
p

n
o
i
t

f
e
i
l
e
b

p
e
e
d

s
a

e
t
a
r
u
c
c
a

s
a

e
b

t
o
n

y
a
m
s
k
r
o
w
t
e
n

l
a
r
u
e
n

e
v
i
s
r
u
c
e
R

-

l
a
r
u
t
a
n

d
n
a

e
g
a
u
g
n
a
l

g
n
i
z
y
l
a
n
a

r
o
f

l
a
i
c
fi
e
n
e
b

y
l
e
m
e
r
t
x
E
-

)

N
N
v
R

(

k
r
o
w
t
e
n

l
a
r
u
e
n

e
v
i
s
r
u
c
e
R

s
e
g
n
e
l
l
a
h
C

s
e
g
a
t
n
a
v
d
A

s
l
e
d
o
m
g
n
i
n
r
a
e
l

p
e
e
D

)
d
e
u
n
i
t
n
o
c
(

3
e
l
b
a
T

e
d
i
w
a

n
o

s
h
p
a
r
g

e
g
d
e
l
w
o
n
k

e
s
r
a
p
s

n
o

t
c
a
p
m

i

l
a
m
i
n
i
m
a

s
a
H

n
r
a
e
l

y
l
r
e
p
o
r
p

o
t

d
e
r
i
u
q
e
r

e
r
a

s
e
l
p
m
a
s

t
e
l
p
i
r
t

e
g
u
H

-

-

s
s
e
n
e
s
r
a
p
s

g
n
i
n
r
a
e
l

n
o
i
t
a
t
n
e
s
e
r
p
e
r

y
t
i
t
n
e

e
h
t

e
z
i
m
i
n
i
M

-

s
e
i
t
i
t
n
e

d
n
a

s
p
i
h
s
n
o
i
t
a
l
e
r

n
e
e
w
t
e
b

s
e
g
a

e
l
a
c
s

m
e
l
b
o
r
p

h
c
i
h
w

,
s
r
e
t
e
m
a
r
a
p

f
o

t
n
u
o
m
a

e
g
u
h

a

f
o

n
o
i
t
a
m

i
t
s
e

e
h
t

e
r
i
u
q
e
R

-

k
r
o
w
t
e
n

l
a
r
u
e
n
e
h
t

f
o

s
l
e
d
o
m
s
u
o
i
v
e
r
p
s
u
o
r
e
m
u
n

s
e
z
i
l
a
r
e
n
e
G

-

l
a
r
u
e
n

r
e
h
t
o

e
h
t

o
t

d
e
r
a
p
m
o
c

d
e
d
e
e
n
s
i

d
o
i
r
e
p

g
n
i
n
i
a
r
t

g
n
o
L
-

s
e
o
d

r
e
y
a
l
k
r
o
w
t
e
n

l
a
r
u
e
n

l
a
c
i
p
y
t

a

n
a
h
t

a
t
a
d

l
a
n
o
i
t

s
r
e
t
e
m
a
r
a
p

y
n
a
m
o
s

s
e
s
i
r
p
m
o
c

t
i

s
a

s
l
e
d
o
m
k
r
o
w
t
e
n

a
i
v

y
l
t
i
c
i
l
p
m

i

y
l
n
o

n
a
h
t

r
e
h
t
a
r

s
t
u
p
n
i

o
w

t

e
h
t

y
l
p
i
t
l
u
m
n
a
c

t
I

-

g
n
i
t
t

fi
r
e
v
o

o
t

s
d
a
e
l

y
l
t
n
e
u
q
e
r
f

-
a
l
e
r

g
n
i
l
l
e
d
o
m

r
o
f

y
a
w

l
u
f
r
e
w
o
p

y
l
e
v
i
t
a
r
a
p
m
o
c

a

s
e
d
i
v
o
r
P
-

h
g
i
h

y
l
e
m
e
r
t
x
e

s
i

y
t
i
x
e
l
p
m
o
c

l
a
n
o
i
t
a
t
u
p
m
o
c

f
o

l
e
v
e
l

e
h
T
-

-
k
n
i
l

c
i
t
n
a
m
e
s

d
e
t
a
c
i
l
p
m
o
c

e
h
t

n
i
a
l
p
x
e

y
l
e
v
i
t
c
e
ff
e

n
a
c
N
T
N

-

)

N
T
N

(

k
r
o
w
t
e
n
r
o
s
n
e
t

l
a
r
u
e
N

d
e
fi
i
c
e
p
s

a

n
i
h
t
i

w
g
n
i
n
o
s
a
e
r

a
i
v

s
e
i
t
i
t
n
e

n
e
e
w
t
e
b

s
n
o
i
t
c
e
n
n
o
c

e
l
b
i
s
i
v
n
i

f
o

n
o
i
t
c
i
d
e
r
p
e
h
t

n
i

n
o
i
s
i
c
e
r
p

r
e
h
g
i
h

e
d
i
v
o
r
p

o
t

e
l
b
A

-

l
a
u
t
x
e
t

r
o
i
r
e
t
x
e

o
n

n
e
h
w
n
e
v
e

n
o
i
s
n
e
t
x
e

e
s
a
b
a
t
a
d

s
w
o
l
l

A

-

e
l
b
a
l
i
a
v
a

e
r
a

s
e
c
r
u
o
s
e
r

e
s
a
b

e
g
d
e
l
w
o
n
k

y
t
i
r
a
e
n
i
l
-
n
o
n

Deep learning modelling techniques: current progress,…1 3

13594

S. F. Ahmed et al.

t
c
a
p
m

i

y
l
b
a
r
e
d
i
s
n
o
c

d
l
u
o
c

h
c
i
h
w

,
s
e
g
a
m

i

t
u
p
n
i

f
o

k
r
o
w
e
m
a
r
f

n
o
i
t
c
e
l
e
s

r
e
t
e
m
a
r
a
p

e
t
a
i
r
p
o
r
p
p
a

f
o

y
t
l
u
c
fi

s
i
s
y
l
a
n
a

a
i
d
e
m

i
t
l
u
m
n
i

n
o
i
t
a
c
i
l
p
p
a

s
a

l
l
e
w
s
a

e
c
n
a
m
r
o
f
r
e
p

r
i
e
h
t

d
e
s
i
v
r
e
p
u
s
n
u

n
a

o
s
l
a

s
i

t
i

s
a

d
e
r
i
u
q
e
r

s
i

a
t
a
d

d
e
l
l
e
b
a
l

o
N

-

r
e
h
t
r
u
f

o
t

y
r
a
s
s
e
c
e
n

s
e
s
s
e
c
o
r
p
e
h
t

g
n
i
d
r
a
g
e
r

y
t
i
r
a
l
c

f
o

k
c
a
l

e
h
T
-

,
s
i
s
o
n
g
a
i
d
e
s
a
e
s
i
d

g
n
i
d
u
l
c
n
i

s
d
l
e
fi
s
u
o
r
e
m
u
n

n
i

y
l
d
a
o
r
b

n
o
i
t
a
m
i
x
o
r
p
p
a

g
n
i
n
i
a
r
t

m
u
m
i
x
a
m
g
n
i
s
u

k
r
o
w
t
e
n

e
h
t

e
z
i
m

i
t
p
o

w
o
fl
c
ffi
a
r
t

,
g
n
i
s
s
e
c
o
r
p

e
g
a
m

i

,
n
o
i
t
i
n
g
o
c
e
r

e
c
a
f

d
n
a

h
c
e
e
p
s

g
n
i
n
i
a
r
t

N
B
D
e
h
t

,
d
e
v
l
o
v
n
i

a
t
a
d

f
o

t
n
u
o
m
a

t
s
a
v

e
h
t

o
t

e
u
D

-

f
o

n
o
i
t
a
t
e
r
p
r
e
t
n
i

d
n
a

,
n
o
i
t
a
c
fi
i
s
s
a
l
c

r
e
c
n
a
c

t
s
a
e
r
b

,
g
n
i
t
s
a
c
e
r
o
f

N
B
D
a

n
i
a
r
t

o
t

t
s
o
c

l
a
n
o
i
t
a
t
u
p
m
o
c

h
g
i
H

-

d
e
i
l
p
p
a

s
e
r
u
t
a
e
f

t
u
p
n
i

g
n
i
n
r
a
e
l

n
i

s
t
fi
e
n
e
b

t
n
a
c
fi
i
n
g
i
s

e
v
a
H

-

s
d
e
e
n

e
h
t

t
e
e
m

t
o
n

y
a
m

s
u
h
t

d
n
a

,
e
v
i
s
n
e
t
n
i
-
e
m

i
t

e
r
a

s
e
s
s
e
c
o
r
p

e
g
a
u
g
n
a
l

l
a
r
u
t
a
n

s
m
e
t
s
y
s

n
o
i
t
a
c
i
l
p
p
a

e
m

i
t
-
l
a
e
r

f
o

-
n
a
r

f
o

g
n
i
n
r
a
e
l

c
i
t
s
i
r
e
t
c
a
r
a
h
c

y
d
a
e
t
s

e
h
t

m
o
r
f

t

fi
e
n
e
b

s
N
B
D

-

n
e
h
w
d
e
p
m
a
l
c

g
n
i
e
b
a
t
a
d
t
u
p
n
i

e
h
t

o
t

e
u
d

r
o
o
p

s
i

e
c
n
a
m
r
o
f
r
e
P
-

n
i

n
o
i
t
a
c
i
l
p
p
a

t
n
e
i
c
ffi
e

y
l
h
g
i
h

g
n
i
l
b
a
n
e

,
s
e
l
p
m
a
s

t
u
p
n
i

y
l
m
o
d

n
i
a
r
t
-
e
r
p

o
t

d
e
s
u

s
i

m
h
t
i
r
o
g
l
a

g
n
i
n
r
a
e
l

e
c
n
e
g
r
e
v
i
d

e
v
i
t
s
a
r
t
n
o
c

a

n
o
i
t
i
n
g
o
c
e
r

h
c
e
e
p
s

d
n
a

e
c
a
f

,
g
n
i
t
i
r

w
d
n
a
h

f
o

s
a
e
r
a

e
h
t

s
m
e
l
b
o
r
p

n
o
i
s
i
v

r
e
t
u
p
m
o
c

d
n
a

s
s
e
c
o
r
p

N
B
D

-
r
e
i
h

p
e
e
d

a

n
r
a
e
l

y
l
e
v
i
t
c
e
ff
e

o
t

g
n
i
n
i
a
r
t

r
e
y
a
l
-
y
b
-
r
e
y
a
l

s
e
s
u

t
I

-

f
o

n
o
i
t
a
z
i
m

i
t
p
o
e
c
n
a
m
r
o
f
r
e
p

e
h
t

r
o
f

l
e
d
o
m
c
i
t
s
i
l
i
b
a
b
o
r
p

y
h
c
r
a

s
m
e
l
b
o
r
p

n
o
i
t
a
c
fi
i
s
s
a
l
c

e
l
p
m
i
s

t
o
n
s
i
S
N
A
G
n
i

g
n
i
t
r
e
v
n
I

-

-
c
a
x
e

s
i

h
c
i
h
w

,

w
o
l
s

y
l
t
n
e
r
e
h
n
i

s
i

s
s
e
c
o
r
p

g
n
i
t
a
r
e
n
e
g

a
t
a
d
e
h
T
-

a
t
a
d

d
e
t
a
r
e
n
e
g

f
o

g
n
i
l
p
m
a
s

e
h
t

g
n
i
z
i
l
e
l
l
a
r
a
p

f
o

e
l
b
a
p
a
c

s
i

t
I

l
a
n
o
i
s
n
e
m
i
d
-
h
g
i
h

f
o

n
o
i
t
a
r
e
n
e
g

e
h
t

h
t
i

w
g
n
i
l
a
e
d

n
e
h
w
d
e
t
a
b
r
e

y
b

n
o
i
t
u
b
i
r
t
s
i
d

y
t
i
l
i
b
a
b
o
r
p

a

e
t
a
m

i
t
s
e

o
t

e
r
i
u
q
e
r

t
o
n

s
e
o
d
N
A
G

-

-

n
o
i
t
i
n
g
o
c
e
r

e
c
i
o
v

s
a

h
c
u
s

,
a
t
a
d

-
n
e
o
t
u
a

l
a
n
o
i
t
a
i
r
a
v
a

e
k
i
l

d
n
u
o
b

r
e
w
o
l

a

f
o

n
o
i
t
c
u
d
o
r
t
n
i

e
h
t

l
l
e
w
s
e
t
a
r
e
p
o
N
A
G

r
e
h
t
e
h
w
e
n
i
m
r
e
t
e
d

o
t

r
e
d
r
o

n
i

y
l
t
n
a
t
s
n
o
c

d
e
d
i
v
o
r
p

e
b

o
t

d
e
e
n

a
t
a
d

f
o
s
m
r
o
f

s
u
o
i
r
a
v

s
a

n
i
a
r
t

o
t

r
e
d
r
a
H

e
g
r
e
v
n
o
c

o
t

g
n
i
g
n
e
l
l
a
h
c

d
n
a

e
l
b
a
t
s
n
u

s
i

g
n
i
n
i
a
r
t

N
A
G

e
u
s
s
i

e
s
p
a
l
l
o
c

e
d
o
m
m
o
r
f

s
r
e
ff
u
s

t
I

-

-

-

-
t
e
b

d
n
a

r
e
p
r
a
h
s

d
l
e
i
y

o
t

d
e
t
a
r
t
s
n
o
m
e
d

y
l
l
a
c
i
r
i
p
m
e

n
e
e
b

s
a
h

t
I

-

-
u
c
i
t
r
a
p

,
l
e
d
o
m
e
v
i
t
a
r
e
n
e
g

f
o

e
p
y
t

r
e
h
t
o

y
n
a

n
a
h
t

s
t
l
u
s
e
r

r
e
t

r
e
d
o
c
n
e
o
t
u
a

l
a
n
o
i
t
a
i
r
a
v

y
l
r
a
l

r
e
d
o
c

t
o
n

r
o

o
e
d
i
v

,
o
i
d
u
a

,
e
g
a
m

i

,
a
t
a
d

f
o
s
e
p
y
t

r
a
l
i

m
i
s

e
t
a
r
e
n
e
g

o
t

e
l
b
a
p
a
C

-

-

m
o
c

y
l
e
m
e
r
t
x
e

n
a

s
i

t
x
e
t

r
o

h
c
e
e
p
s
m
o
r
f

s
e
m
o
c
t
u
o

g
n
i
c
u
d
o
r
P
-

e
n
o

l
a
n
i
g
i
r
o

e
h
t

o
t

s
t
x
e
t

d
n
a

s
s
e
c
o
r
p

d
e
t
a
c
i
l
p

t
e
r
p
r
e
t
n
i

y
l
k
c
i
u
q

n
a
c

d
n
a

a
t
a
d

f
o
e
a
i
t
u
n
i
m
e
h
t

o
t
n
i

e
v
l
e
d

s
N
A
G

-

-
r
e
p
u
s
n
u

f
o

h
c
a
o
r
p
p
a

e
h
t

d
n
a

g
n
i
n
i
a
r
t

f
o

y
t
i
l
i
b
a
t
s
n
i

e
h
t

o
t

e
u
D

-

-
n
r
a
e
l

e
n
i
h
c
a
m

r
o
f

l
u
f
e
s
u
m
e
h
t

g
n
i
k
a
m

,
s
t
a
m
r
o
f

y
n
a
m
o
t
n
i

t
i

t
u
p
t
u
o

e
t
a
r
e
n
e
g

o
t

t
l
u
c
ffi
i
d
e
r
o
m
s
e
m
o
c
e
b

t
i

,
g
n
i
n
r
a
e
l

d
e
s
i
v

s
k
s
a
t

g
n
i

s
i

e
g
a
m

i

n
a

y
f
i
t
n
e
d
i

d
n
a

y
c
a
r
u
c
c
a

y
t
i
s
n
e
d

e
h
t

t
s
a
c
e
r
o
f

o
t

e
l
b
a
n
U

-

s
N
A
G
g
n
i
s
u

y
l
i
s
a
e

d
e
z
i
n
g
o
c
e
r

e
b

n
a
c

e
l
p
o
e
p

d
n
a

,
s
t
e
e
r
t
s

n
o

s
c
i
r
t
e
m
n
o
i
t
a
u
l
a
v
e

c
i
s
n
i
r
t
n
i

f
o

k
c
a
L
-

r
a
c

g
n
i
k
r
a
p

,
s
t
s
i
l
c
y
c
i
b

,
s
e
e
r
t

s
a

h
c
u
s

s
t
c
e
j
b
o

f
o

s
e
p
y
t

t
n
e
r
e
ff
D

i

-

h
t
i

w
d
e
e
c
o
r
p

o
t

h
g
u
o
n
e

e
s
n
e
d

s
t
c
e
j
b
o

t
n
e
r
e
ff
i
d

o
w

t

n
e
e
w
t
e
b

e
c
n
a
t
s
i
d

e
h
t

e
r
u
s
a
e
m
o
t

e
l
b
A

-

)

N
A
G

(

k
r
o
w
t
e
n

l
a
i
r
a
s
r
e
v
d
a

e
v
i
t
a
r
e
n
e
G

l
a
n
o
i
s
n
e
m
i
d
-
o
w

t

e
h
t

n
o
i
t
a
r
e
d
i
s
n
o
c

o
t
n
i

e
k
a
t

t
o
n

o
d
s
N
B
D

-

-
f
i
d
e
h
t

s
s
e
r
d
d
a

n
a
c

s
N
B
D
h
t
i

w
h
c
a
o
r
p
p
a

g
n
i
n
r
a
e
l

y
d
e
e
r
g

e
h
T
-

)

N
B
D

(

s
k
r
o
w
t
e
n

f
e
i
l
e
b

p
e
e
D

s
e
g
n
e
l
l
a
h
C

s
e
g
a
t
n
a
v
d
A

s
l
e
d
o
m
g
n
i
n
r
a
e
l

p
e
e
D

)
d
e
u
n
i
t
n
o
c
(

3
e
l
b
a
T

1 3

13595

e
h
t

f
i

y
l
r
a
l
u
c
i
t
r
a
p

,
e
m

i
t

g
n
i
n
i
a
r
t

n
e
h
t
g
n
e
l

t
h
g
i
m
h
c
i
h
w

,
l
e
d
o
m

n
o
i
t
a
c
fi

i
t
n
e
d
i

d
n
a

,
g
n
i
l
l
e
d
o
m

,
n
o
i
t
c
i
d
e
r
p

a
t
a
d

f
o

s
e
c
n
e
u
q
e
s

g
n
o
l

s
n
i
a
t
n
o
c

a
t
a
d

t
u
p
n
i

s
’
l
e
d
o
m

g
n
o
l

d
n
a

k
r
o
w
t
e
n

l
a
r
u
e
n

t
n
e
r
r
u
c
e
r

a

h
t
i

w
d
e
t
a
r
o
p
r
o
c
n
i

s
i

t
I

-

d
e
n
i
o
j
s
i
d

d
n
a

t
c
n
i
t
s
i
d
m
e
h
t

p
e
e
k

n
e
t
f
o

s
m
s
i
n
a
h
c
e
m
n
o
i
t
n
e
t
t

A

m
e
t
s
y
s

e
h
t

e
z
i
l
e
l
l
a
r
a
p

o
t

s
s
e
c
o
r
p
s
u
o
i
d
e
t

d
n
a

g
n
o
l

a

s
i

t
I

-

-

y
h
t
g
n
e
l

f
o

g
n
i
l
l
e
d
o
m
e
h
t

s
e
l
b
a
n
e

h
c
i
h
w
y
r
o
m
e
m
m
r
e
t
-
t
r
o
h
s

s
e
i
c
n
e
d
n
e
p
e
d

l
a
r
o
p
m
e
t

t
o
n

s
u
h
t

,
s
e
l
u
d
o
m
o
w

t

e
s
e
h
t

n
e
e
w
t
e
b

n
o
i
t
c
a
r
e
t
n
i

g
n
i
t
n
e
v
e
r
p

s
t
n
e
m
e
l
e

f
o

n
o
i
t
c
e
l
l
o
c

,
e
l
u
d
o
m
n
o
i
t
n
e
t
t
a

l
a
i
t
a
p
s

d
n
a

l
e
n
n
a
h
c

d
e
t
a
c
i
d
e
d
e
h
t

g
n
i
s
u

a

n
o

g
n
i
t
a
r
t
n
e
c
n
o
c

y
b

y
l
b
i
x
e
fl
s
s
e
c
o
r
p

e
v
i
t
i
n
g
o
c

e
h
t

s
l
o
r
t
n
o
C

-

l
a
m

i
t
p
o

l
a
r
o
p
m
e
t

,
s
n
o
i
s
n
e
m
i
d

l
a
i
t
a
p
s

n
o

g
n
i
s
u
c
o
f

f
o

e
l
b
a
p
a
c

s
i

t
I

-

-
c
a
r
e
t
n
i

l
e
n
n
a
h
c

e
z
i
t
i
r
o
i
r
p

t
o
n

o
d
s
d
o
h
t
e
m
n
o
i
t
n
e
t
t
a

s
u
o
r
e
m
u
N

-

s
r
o
t
c
e
v

t
u
p
n
i

e
h
t

f
o
s
e
r
u
t
a
e
f

s
u
o
i
r
a
v

r
o

,
s
n
o
i
s
n
e
m
i
d

-
r
o
f
n
i

g
n
i
c
u
d
e
r

e
c
n
e
h

,
s
t
h
g
i
e
w
n
o
i
t
n
e
t
t
a

g
n
i
t
u
p
m
o
c

n
e
h
w
n
o
i
t

e
t
a
r
e
n
e
g

o
t

r
o
t
c
e
v

t
u
p
n
i

h
c
a
e

k
n
i
l

n
a
c
m
s
i
n
a
h
c
e
m
n
o
i
t
n
e
t
t

A

-

n
o
i
s
s
i
m
s
n
a
r
t

n
o
i
t
a
m

y
l
l
a
c
i
r
t
e
m
m
y
s

d
n
a

y
l
t
c
e
r
i
d

e
r
o
m

r
o
t
c
e
v

t
u
p
t
u
o

e
h
t

-
i
d
d
a

t
n
a
c
fi
i
n
g
i
s

e
c
u
d
o
r
t
n
i

s
e
u
q
i
n
h
c
e
t

n
o
i
t
n
e
t
t
a

f
o

y
t
i
r
o
j
a
m
e
h
T
-

t
n
a
v
e
l
e
r

t
s
o
m
s
i

t
a
h
t

t
u
p
n
i

n
a
m
o
r
f

n
o
i
t
a
m
r
o
f
n
i

e
c
u
d
e
d

n
a
c

t
I

-

r
e
w
o
l
s

g
n
i
s
u
a
c

,

m
r
o
f

r
e
t
e
m
a
r
a
p

l
e
d
o
m
n
i

n
o
i
t
a
t
u
p
m
o
c

l
a
n
o
i
t

-
u
c
i
t
r
a
p

,
e
c
n
a
m
r
o
f
r
e
p

s
e
v
o
r
p
m

i

h
c
i
h
w

,
k
s
a
t

a

g
n
i
t
e
l
p
m
o
c

o
t

s
e
r
u
t
c
e
t
i
h
c
r
a

r
e
g
r
a
l

d
n
a

g
n
i
s
s
e
c
o
r
p

e
g
a
u
g
n
a
l

n
i

y
l
r
a
l

n
o
i
s
i
v

r
e
t
u
p
m
o
c

o
t

d
e
t
a
l
e
r

t
o
n

s
n
o
i
t
a
c
i
l
p
p
a

r
o
f

e
t
a
i
r
p
o
r
p
p
a
n
i

k
r
o
w
t
e
n

l
a
r
u
e
n

t
p
e
c
n
o
c

e
h
t

e
k
a
m
y
a
m

s
e
i
t
i
t
n
e

e
l
u
s
p
a
c

f
o

t
p
e
c
n
o
c

d
i
g
i
r

e
h
T
-

l
a
n
o
i
t
u
l
o
v
n
o
c

e
k
i
l

s
r
e
t
e
m
a
r
a
p

y
n
a
m
o
s

e
r
i
u
q
e
r

t
o
n

s
e
o
d

t
I

-

t
e
N
e
g
a
m

I

s
a

h
c
u
s

s
t
e
s
a
t
a
d

e
g
r
a
l

y
l
r
a
l
u
c
i
t
r
a
p

,
s
t
e
s
a
t
a
d

e
r
u
t
c
u
r
t
s

s
t
i

n
i

y
t
i
x
e
l
p
m
o
c

s
s
e
l

-
o
v
n
o
c

o
t

d
e
r
a
p
m
o
c

t
n
e
m
e
l
p
m

i

o
t

y
t
i
x
e
l
p
m
o
c

r
e
h
g
i
h

s
e
s
s
e
s
s
o
P
-

s
n
o
i
t
a
c
i
l
p
p
a

f
o
e
g
n
a
r

e
d
i
w
a

n
i

e
g
a
s
u

r
o
f

e
l
b
a
t
i
u
s

g
n
i
n
i
a
r
t

d
e
s
a
b
-
e
n
i
l
n
o

r
o
f

e
l
b
a
t
i
u
s

t
o
N

-

s
t
e
N
s
p
a
C
s
e
k
a
m
s
t
e
s
a
t
a
d

r
e
l
l
a
m
s

n
o

y
t
i
l
i
b
a

d
e
z
i
l
a
r
e
n
e
g

l
l
e

W

-

t
o
n
n
a
c

t
i

s
t
u
p
t
u
o

r
o
t
c
e
v

r
o

x
i
r
t
a
m
s
e
t
a
r
e
n
e
g

t
e
N
s
p
a
C
e
h
t

s
A

-

t
n
i
o
p
w
e
i
v
e
h
t

f
o

e
v
i
t
c
e
p
s
e
r
r
i

,
s
t
c
e
j
b
o

e
z
i
n
g
o
c
e
r

o
t

s
t
e
N
s

s
k
r
o
w
t
e
n

l
a
r
u
e
n

l
a
n
o
i
t
u
l

-
p
a
C
s
w
o
l
l
a

s
r
o
t
c
e
v

r
e
t
e
m
a
r
a
p

r
o

s
e
c
i
r
t
a
m
e
s
o
p

f
o

e
g
a
s
u

e
h
T
-

s
n
o
i
t
c
n
u
f

s
s
o
l

s
u
o
i
v
e
r
p

e
s
u
e
r

y
l
p
m
i
s

s
r
e
t
e
m
a
r
a
p

n
o
i
t
a
i
t
n
a
t
s
n
i

t
c
e
j
b
o
s
s
a
l
c

g
n
i
r
u
t
p
a
c

f
o

e
l
b
a
p
a
C

s
t
c
e
j
b
o

r
e
s
o
l
c

h
s
i
u
g
n
i
t
s
i
d

o
t

e
l
b
a

t
o
N

-

t
a
h
w
d
n
a
t
s
r
e
d
n
u

o
t

s
e
r
u
t
a
e
f

c
fi
i
c
e
p
s

e
r
o
m

t
n
e
s
e
r
p
e
r

s
t
e
N
s
p
a
C

-

-

l
a
n
o
i
t
a
t
u
p
m
o
c

r
i
e
h
t

g
n
i
z
i
l
i
t
u

y
l
l
u
f

m
o
r
f

s
U
P
G
g
n
i
t
i

m

i
l

,
e
z
i
l
e
l

-
l
a
r
a
p

o
t

t
l
u
c
ffi
i
d

s
a

l
l
e
w
s
a

c
i
m
a
n
y
d
s
i

s
s
e
c
o
r
p

g
n
i
t
u
o
r

e
h
T
-

y
t
i
l
i
b
a
p
a
c

g
n
i
n
r
a
e
l

s
i

k
r
o
w
t
e
n

e
h
t

w
o
h

d
n
a

s
u
o
i
r
a
v

s
s
o
r
c
a

y
l
t
n
e
t
s
i
s
n
o
c
m
r
o
f
r
e
p

o
t

e
l
b
a

t
o
n

e
r
a

s
t
e
N
s
p
a
C

-

e
h
t

o
t

e
u
d

e
c
n
a
m
r
o
f
r
e
p

t
r
a
-
e
h
t
-
f
o
-
e
t
a
t
s

e
v
e
i
h
c
a

n
a
c

t
e
N
s
p
a
C

-

)
t
e
N
s
p
a
C

(

k
r
o
w
t
e
n

l
a
r
u
e
n
e
l
u
s
p
a
C

s
e
g
n
e
l
l
a
h
C

s
e
g
a
t
n
a
v
d
A

s
l
e
d
o
m
g
n
i
n
r
a
e
l

p
e
e
D

)
d
e
u
n
i
t
n
o
c
(

3
e
l
b
a
T

e
h
t

n
i

s
r
e
t
e
m
a
r
a
p
t
h
g
i
e
w

l
a
n
o
i
t
i
d
d
a

s
d
d
a
m
s
i
n
a
h
c
e
m
n
o
i
t
n
e
t
t

A

-

g
n
i
d
u
l
c
n
i

m
e
t
s
y
s

x
e
l
p
m
o
c

a

f
o

s
k
s
a
t

y
n
a

f
o

e
c
n
a
d
i
u
g

s
w
o
l
l

A

-

m

s
i
n
a
h
c
e
m
n
o
i
t
n
e
t
t

A

Deep learning modelling techniques: current progress,…1 3

13596

S. F. Ahmed et al.

n
o
i
t
u
c
e
x
e

-
t
e
p
m
o
c

r
e
h
t
o
e
h
t

n
a
h
t

r
e
w
o
l
s

y
l
e
v
i
t
a
r
a
p
m
o
c

s
i

g
n
i
n
i
a
r
t

E
A
D
S
-

n
o
i
t
a
t
n
e
s
e
r
p
e
r

a
t
a
d

t
c
a
p
m
o
c

g
n
i
n
r
a
e
l

n
i

d
e
s
u

e
b

n
a
C

-

l
a
c
i
r
e
m
u
n

s
a

l
l
e
w
s
a

e
v
i
t
a
r
e
t
i

n
o

s
e
i
l
e
r

t
i

s
a

s
m
h
t
i
r
o
g
l
a

g
n
i

y
s
i
o
n

g
n
i
d
d
e
b
m
e

y
b

y
c
a
r
u
c
c
a

g
n
i
n
r
a
e
l

p
e
e
d

s
e
v
o
r
p
m

i

E
A
D
S
-

n
o
i
t
c
e
l
e
s

l
e
d
o
m
g
n
i
d
n
a
m
e
d
y
l
l
a
n
o
i
t
a
t
u
p
m
o
c

r
o
f

t
n
e
m
e
r
i
u
q
e
r

t
e
s

t
s
e
t

e
h
t

t
u
o
h
g
u
o
r
h
t

e
z
i
l
a
r
e
n
e
g

e
h
t

d
n
a

y
t
i
l
a
n
o
i
s
n
e
m
i
d

s
’
a
t
a
d

t
u
p
n
i

e
h
t

y
b

d
e
t
a
c
i
l
p
m
o
C

-

o
t

e
s
i
o
n
e
m
o
s

e
c
u
d
o
r
t
n
i

o
t

d
n
a

a
t
a
d

t
r
o
t
s
i
d

o
t

d
e
s
u

e
b

n
a
c

t
I

-

s
r
e
t
e
m
a
r
a
p

l
e
d
o
m
g
n
i
n
r
a
e
l

n
i

n
o
i
t
a
z
i
m

i
t
p
o

s
r
e
y
a
l

e
h
t

n
i

s
r
e
d
o
c
n
e
o
t
u
a

s
r
e
t
e
m
a
r
a
p
r
e
p
y
h

t
s
u
j
d
a

o
t

s
e
u
q
i
n
h
c
e
t

-
r
o
w
e
t
o
n
s
a

l
l
e
w
s
a

d
e
l
i
a
t
e
d

h
t
i

w
n
o
i
s
r
e
v
a
t
a
d
w
a
r

a

s
r
e
v
i
l
e
D

-

d
e
z
i
m

i
t
p
o

y
l
h
g
i
h

r
o
f

d
e
r
i
u
q
e
r

e
b

y
a
m
e
m

i
t

g
n
i
n
i
a
r
t

y
h
t
g
n
e
l

A

-

n
o
i
t
a
m
r
o
f
n
i

e
r
u
t
a
e
f

y
h
t

n
o
i
s
n
e
m
i
d
-
h
g
i
h

h
t
i

w
s
e
r
u
t
a
e
f

e
h
t

o
t

e
l
a
c
s

o
t

y
t
i
l
i
b
a
n
I

t
s
o
c

l
a
n
o
i
t
a
t
u
p
m
o
c

h
g
i
H

-

-

e
l
b
a
i
l
e
r

s
i

E
A
D
S
e
h
t

g
n
i
z
i
l
i
t
u
s
s
e
c
o
r
p

g
n
i
n
r
a
e
l

d
e
s
i
v
r
e
p
u
s
n
U

g
n
i
t
s
a
c
e
r
o
f

d
a
o
l

e
h
t

n
i

t
u
p
n
i

e
h
t

r
e
v
o

l
o
r
t
n
o
c
m
o
d
n
a
r

e
s
o
L
-

s
e
u
s
s
i

g
n
i
t
t

fi
-
r
e
v
o

d
n
a

g
n
i
h
s
i
n
a
v

t
n
e
i
d
a
r
g

d
i
o
v
a

y
l
e
v
i
t
c
e
ff
e

n
a
C

-

-

g
n
i
g
n
e
l
l
a
h
c

s
i

s
o
i
r
a
n
e
c
s

t
s
e
t

n
e
e
s
n
u

y
l
s
u
o
i
v
e
r
p

d
e
c
u
d
e
r

e
b
n
a
c

s
s
a
p
e
l
g
n
i
s

a

n
a
h
t

r
e
w
o
l
s

y
l
b
a
e
c
i
t
o
n

s
i

e
c
n
e
r
e
f
n
i

e
t
a
m
i
x
o
r
p
p
A

-

y
l
t
s
u
b
o
r

e
r
o
m
s
t
u
p
n
i

s
u
o
u
g
i
b
m
a

e
l
d
n
a
h

n
a
C

-

s
N
B
D
n
i

s
a

)
p
u
-
m
o
t
t
o
b
(

h
t
i

w
s
r
e
t
e
m
a
r
a
p

d
n
a

s
e
c
n
e
r
e
f
n
i

g
n
i
n
r
a
e
l

s
m
r
o
f
r
e
p

y
l
t
n
e
i
c
ffi
E
-

r
e
y
a
l
-
y
b
-
r
e
y
a
l

e
r
i
u
q
e
r

y
e
h
t

s
a

n
i
a
r
t

o
t

t
l
u
c
ffi
i
d

d
n
a

e
v
i
t
i
u
t
n
i

s
s
e
L
-

e
l
g
n
i
s

a

o
t
n
i

s
e
c
r
u
o
s

a
t
a
d

e
l
p
i
t
l
u
m
e
t
a
r
g
e
t
n
i

n
a
c

l
e
d
o
m
M
B
D

e
h
t

o
t

d
e
r
a
p
m
o
c

e
v
i
s
n
e
p
x
e

y
l
l
a
n
o
i
t
a
t
u
p
m
o
c

s
i

g
n
i
n
i
a
r
t

M
B
D

-

g
n
i
n
i
a
r
t

d
e
r
e
y
a
l
-
y
d
e
e
r
g

k
r
o
w
t
e
n

f
e
i
l
e
b

p
e
e
d

e
h
t

f
o

g
n
i
n
i
a
r
t

a
t
a
d

n
i

s
e
r
u
t
a
e
f

t
n
e
t
a
l

g
n
i
y
f
i
t
n
e
d
i

f
o

e
l
b
a
p
a
C

-

-

g
n
i
n
i
a
r
t
-
e
r
p

d
n
a

g
n
i
l
p
m
a
s

-
a
c
fi
i
s
s
a
l
c

d
n
a

l
a
v
e
i
r
t
e
r

l
u
f
e
s
u
s
e
t
a
r
o
p
r
o
c
n
i

t
a
h
t

n
o
i
t
a
t
n
e
s
e
r
p
e
r

n
i

g
n
i
n
r
a
e
l

f
o

y
t
l
u
c
ffi
i
d

e
h
t

e
t
a
b
r
e
c
a
x
e

s
r
e
y
a
l

n
e
d
d
i
h
e
l
p
i
t
l
u
M

-

d
e
l
e
b
a
l
n
u

f
o

s
e
m
u
l
o
v

e
g
r
a
l

e
s
u

y
l
e
v
i
t
c
e
ff
e

n
a
c

l
e
d
o
m
M
B
D

-

s
e
n
i
h
c
a
m
n
n
a
m
z
t
l
o
B
p
e
e
d

a
t
a
d

s
n
o
i
t
c
n
u
f

s
e
u
s
s
i

n
o
i
t
i
n
g
o
c
e
r

t
c
e
j
b
o

d
n
a

h
c
e
e
p
s

g
n
i
v
l
o
s

n
i

g
n
i
s
i
m
o
r
P
-

s
e
r
u
t
a
e
f

n
o
i
t

n
o
i
t
i
t
r
a
p

y
b

d
e
s
u
a
c

e
u
s
s
i

e
c
n
e
r
e
f
n
i

d
r
a
h

e
h
t

o
t

e
u
d
e
g
n
e
l
l
a
h
c

a

s
e
r
u
t
c
u
r
t
s

r
e
y
a
l
i
t
l
u
m
g
n
i
s
u

a
t
a
d

s
i

s
e
n
i
h
c
a
m
n
n
a
m
z
t
l
o
B
p
e
e
d

n
i

g
n
i
n
r
a
e
l

c
i
t
s
i
l
i
b
a
b
o
r
p
m
u
m
i
x
a
M

-

t
u
p
n
i

m
o
r
f

n
o
i
t
a
t
n
e
s
e
r
p
e
r

f
o

s
l
e
v
e
l

s
u
o
i
r
a
v

g
n
i
n
r
a
e
l

f
o

e
l
b
a
p
a
C

-

)

M
B
D

(

e
n
i
h
c
a
m
n
n
a
m
z
t
l
o
B
p
e
e
D

s
e
g
n
e
l
l
a
h
C

s
e
g
a
t
n
a
v
d
A

s
l
e
d
o
m
g
n
i
n
r
a
e
l

p
e
e
D

)
d
e
u
n
i
t
n
o
c
(

3
e
l
b
a
T

o
t

e
l
b
a
z
i
l
a
r
e
n
e
g

y
l
t
n
e
i
c
ffi
u
s

s
i

t
a
h
t

d
l
o
h
s
e
r
h
t

a

g
n
i
z
i
m

i
t
p
O

-

g
n
i
n
u
t
-
e
n
fi
f
o
s
s
e
c
o
r
p

e
h
t

f
o

s
r
o
r
r
e

t
h
g
i
e
w
e
h
t

,

E
A
D
S
g
n
i
s
U

-

)
E
A
D
S
(

s
r
e
d
o
c
n
e
o
t
u
a

g
n
i
s
i
o
n
e
d

d
e
k
c
a
t
S

1 3

13597

e
h
t

g
n
i
v
a
h

s
k
r
o
w
t
e
n

y
r
a
n
i
d
r
o

n
a
h
t

r
e
g
n
o
l

s
i

e
m

i
t

l
a
n
o
i
t
a
t
u
p
m
o
C

-

g
n
i
n
r
a
e
l

d
e
s
i
v
r
e
p
u
s
n
u

g
n
i
s
u

d
e
n
i
a
r
t

e
b

n
a
C

-

r
a
e
n
i
l
n
o
n

d
n
a

d
e
t
a
c
i
l
p
m
o
c

l
e
d
o
m
o
t

d
e
d
e
e
n
e
r
a

s
r
e
y
a
l

e
r
o
M

-

s
e
h
c
a
o
r
p
p
a

s
r
e
y
a
l

f
o

t
n
u
o
m
a

e
m
a
s

d
e
s
a
b
-
g
n
i
n
r
a
e
l

e
n
i
h
c
a
m

r
e
h
t
o

n
a
h
t

t
n
e
i
c
ffi
e

e
r
o
m
d
n
a

r
e
t
s
a
F
-

s
n
g
i
s
e
d

k
r
o
w
t
e
n

g
n
i
d
o
c

n
o
i
t
a
c
fi
i
s
s
a
l
c

-
r
o
f
n
i

s
s
e
c
o
r
p

o
t

n
i
a
r
b

e
h
t

s
e
r
i
u
q
e
r

y
l
p
m
i
s

k
s
a
t

t
l
u
c
ffi
i
d
e
r
o
m
A

-

y
l
b
a
r
e
d
i
s
n
o
c

s
N
C
P

r
o
r
r
e

d
e
t
a
m

i
t
s
e

e
h
t

w
o
h

t
u
o
b
a

y
t
n
i
a
t
r
e
c
n
u
e
h
t

m
o
r
f

s
r
e
ff
u
S
-

d
e
m
r
o
f
r
e
p
e
r
a

s
n
o
i
t
a
c
fi
i
s
s
a
l
c

o
e
d
i
v

d
n
a

e
g
a
m

i

k
r
o
w
t
e
n

e
m
a
s

e
h
t

h
g
u
o
r
h
t

y
l
w
o
l
s

e
r
o
m
n
o
i
t
a
m

l
a
r
u
t
a
n

e
r
e
h
w

,
n
o
i
s
i
v

r
e
t
u
p
m
o
c

f
o

d
l
e
fi
e
h
t

n
i

e
l
b
a
c
i
l
p
p
A

-

y
a
m
n
o
i
t
a
t
u
p
m
o
c

b
u
s

s
’
k
r
o
w
e
m
a
r
f

N
C
P
e
h
t

f
o
e
g
a
t
s

h
c
a
E
-

-
a
t
n
e
s
e
r
p

r
i
e
h
t

e
n
fi
e
r

o
t

y
l
e
v
i
s
r
u
c
e
r

s
e
s
s
e
c
o
r
p

p
u
-
m
o
t
t
o
b

d
n
a

e
g
n
e
l
l
a
h
c

g
n
i
t
u
p
m
o
c

e
l
b
a
t
c
a
r
t
n
i

n
a

l
a
e
c
n
o
c

n
o
i
t
i
n
g
o
c
e
r

t
c
e
j
b
o
e
v
i
s
u
l
c
n
o
c

d
n
a

t
c
a
x
e

e
r
o
m
g
n
i
n
r
e
c
n
o
c

n
o
i
t

s
n
o
i
t
c
n
u
f

n
o
i
t
a
z
i
m
i
n
i
m

n
w
o
d
-
p
o
t

n
u
r

o
t

s
N
C
P
n
i

d
e
s
u
e
r

e
b

n
a
c

e
r
u
t
c
e
t
i
h
c
r
a

e
l
g
n
i

S
-

a
t
a
d

n
i

s
n
o
i
t
a
l
e
r

e
v
o
r
p
m

i

d
l
u
o
c

s
r
e
t
e
m
a
r
a
p
r
e
p
y
h

f
o

t
n
e
m
t
s
u
j
d
a

d
e
t
a
m
o
t
u
A

-

k
r
o
w
y
e
h
t

h
g
u
o
h
t
l
a

e
g
r
e
v
n
o
c

o
t

d
o
i
r
e
p

r
e
g
n
o
l

a

d
l
e
i
y

n
a
c

s

M
E
D

-

y
r
e
v
e

t
a

t
n
r
a
e
l

s
n
o
i
t
a
t
n
e
s
e
r
p
e
r

e
h
t

s
r
e
t
l
a

s
a

l
l
e
w
s
a

e
c
n
a
m

t
l
u
c
ffi
i
d

e
t
i
u
q

s
i

s
l
e
d
o
m
d
e
s
a
b
-
y
g
r
e
n
e

p
e
e
d

e
h
t

n
i

e
c
n
e
r
e
f
n
I

-

e
g
a
m

i

d
n
a

g
n
i
l
l
e
b
a
l

e
c
n
e
u
q
e
s

,
n
o
i
t
i
n
g
o
c
e
r

t
c
e
j
b
o

n
i

l
u
f
e
s
U

e
l
b
a
l
i
a
v
a

t
o
n
s
i

g
n
i
n
r
a
e
l

e
r
u
t
a
e
F
-

g
n
i
l
l
e
d
o
m
n
i

e
l
b
i
x
e
fl
e
r
a

s

M
E
D

-

-

s

M
E
D
n
i

)
g
n
i
n
r
a
e
l
(

d
o
o
h
i
l
e
k
i
l

e
t
a
u
l
a
v
e

o
t

t
l
u
c
ffi
i
d
s
i

t
I

-

s
r
e
y
a
l

c
i
t
s
a
h
c
o
t
s

n
e
d
d
i
h

n
a
h
t

r
e
h
t
a
r

s
r
e
y
a
l

c
i
t
s
i
n
i
m
r
e
t
e
d

s
e
i
t
l
u
c
ffi
i
d
l
a
n
o
i
t
a
t
u
p
m
o
c

f
o

t
l
u
s
e
r

a

s
a

r
a
l
u
p
o
p

s
s
e
L
-

n
e
d
d
i
h

g
n
i
s
u

y
l
t
n
e
i
c
ffi
e

g
n
i
n
r
a
e
l

d
n
a

e
c
a
f
r
e
t
n
i

m
r
o
f
r
e
p

n
a
c

t
I

-

o
t

e
l
b
i
s
s
o
p
m

i

n
e
t
f
o

s
i

h
c
i
h
w

,
n
o
i
t
i
t
r
a
p

f
o

n
o
i
t
c
n
u
f

e
h
t

o
t

e
u
d

n
o
i
t
a
r
o
t
s
e
r

y
l
e
s
i
c
e
r
p

e
t
u
p
m
o
c

-
n
e
m
i
d
-
h
g
i
h

f
o
s
n
o
i
t
u
b
i
r
t
s
i
d

y
t
i
l
i
b
a
b
o
r
p

l
e
d
o
m
o
t

l
o
o
t

l
u
f
e
s
U

-

y
r
o
e
h
t

n
i

l
e
v
e
l

s
i

e
l
p
m
a
s

-
r
o
f
r
e
p
e
v
i
t
a
r
e
n
e
g

s
e
c
n
a
h
n
e

M
E
D

f
o
g
n
i
n
r
a
e
l

d
e
s
a
b
-
t
n
i
o
J

-

n
o
i
s

e
l
b
a
b
o
r
p

a

y
l
e
k
i
l

w
o
h

y
l
i
s
a
e

e
t
u
p
m
o
c

o
t

e
l
b
a

t
o
n
s
i

t
i

s
a

s
l
e
d
o
m

s
r
e
y
a
l

c
i
t
s
a
h
c
o
t
s

n
e
d
d
i
h

e
l
g
n
i
s

h
t
i

w

e
v
i
s
s
e
r
g
e
r
o
t
u
a

r
o
w
o
fl
e
k
i
l

M
E
D
n
i

d
o
h
t
e
m
g
n
i
l
p
m
a
s

t
c
e
r
i
d

o
N

-

s
r
e
y
a
l

c
i
t
s
i
n
i
m
r
e
t
e
d

n
e
d
d
i
h

l
a
r
e
v
e
s

e
t
a
r
o
p
r
o
c
n
i

o
t

e
l
b
a
p
a
C

-

)

M
E
D

(

l
e
d
o
m
y
g
r
e
n
e

p
e
e
D

s
e
g
n
e
l
l
a
h
C

s
e
g
a
t
n
a
v
d
A

s
l
e
d
o
m
g
n
i
n
r
a
e
l

p
e
e
D

)
d
e
u
n
i
t
n
o
c
(

3
e
l
b
a
T

e
v
i
t
c
i
d
e
r
p

p
e
e
d

d
e
t
a
c
i
l
p
m
o
c

d
n
a

e
r
u
t
a
m
p
o
l
e
v
e
d

o
t

t
l
u
c
ffi
i
d
s
i

t
I

-

e
g
a
m

i

s
a

h
c
u
s

,
s
m
e
l
b
o
r
p

n
o
i
t
a
c
fi
i
s
s
a
l
c

l
a
r
e
v
e
s

r
o
f

e
v
i
t
c
e
ff
E
-

)

N
C
P
(

k
r
o
w
t
e
n

g
n
i
d
o
c

e
v
i
t
c
i
d
e
r
P

Deep learning modelling techniques: current progress,…1 3

13598

S. F. Ahmed et al.

e
h
t

f
o

n
o
i
t
a
z
i
m

i
t
p
o

d
e
n
i
b
m
o
c

e
h
t

,
s
t
e
s
a
t
a
d

e
g
r
a
l

f
o
e
s
a
c

e
h
t

n
I

-

s

M
B
R
n
i

t
n
e

n
o
i
t
a
m
i
x
o
r
p
p
a

r
e
w
o
l
s

e
h
t

o
t

e
u
d
e
l
b
i
s
a
e
f

t
o
n
s
i

s
r
e
t
e
m
a
r
a
p

-
s
e
r
g
e
r

,
n
o
i
t
c
u
d
e
r

y
t
i
l
a
n
o
i
s
n
e
m
i
d

,
n
o
i
t
a
c
fi
i
s
s
a
l
c

r
o
f

e
l
b
a
t
i
u
S
-

e
h
t

n
a
h
t

r
e
w
o
l
s

y
l
t
n
a
c
fi
i
n
g
i
s

s
i

e
c
n
e
r
e
f
n
i

n
o
i
t
a
m
i
x
o
r
p
p
a

e
h
T
-

s
e
l
b
a
i
r
a
v

n
e
d
d
i
h

s

M
B
R
n
i

d
e
s
u
s
s
a
p

p
u
-
m
o
t
t
o
b

e
l
g
n
i
s

-
d
n
e
p
e
d

y
l
l
a
n
o
i
t
i
d
n
o
c

t
o
n

e
r
a

s
t
e
s

t
i
n
u

e
l
b
i
s
i
v

d
n
a

n
e
d
d
i
h

e
h
T
-

f
o

n
o
i
t
c
n
u
f

e
h
t

g
n
i
t
a
l
u
c
l
a
c

e
c
n
i
s

d
e
t
a
c
i
l
p
m
o
c

e
t
i
u
q
s
i

g
n
i
n
i
a
r
T
-

g
n
i
r
e
t
l

fi

s

M
B
R

f
o

e
c
a
f
r
e
t
n
i

e
v
i
t
a
r
o
b
a
l
l
o
c

d
n
a

,
g
n
i
n
r
a
e
l

e
r
u
t
a
e
f

,

g
n
i
l
l
e
d
o
m
c
i
p
o
t

,
n
o
i
s

t
n
e
m
t
s
u
j
d
A

t
h
g
i
e
w
m
o
r
f

s
r
e
ff
u
S
-

k
s
a
t

r
a
l
u
c
i
t
r
a
p
e
h
t

n
o

d
e
s
a
b

s
e
s
s
e
c
o
r
p

d
e
s
i
v

y
s
a
e

t
o
n
s
i

t
n
e
i
d
a
r
g

y
g
r
e
n
e

e
h
t

-
r
e
p
u
s
n
u

d
n
a

d
e
s
i
v
r
e
p
u
s

h
t
o
b

n
i

d
e
n
i
a
r
t

e
b

o
t

e
l
b
a

e
r
a

s

M
B
R

-

d
n
a

x
e
l
p
m
o
c

r
o
f

s
n
o
i
t
a
t
i

m

i
l

e
v
a
h

g
n
i
r
e
p
m
e
t

l
e
l
l
a
r
a
p

d
n
a

e
c
n
e
g

g
n
i
s
s
e
c
o
r
p

a
t
a
d

l
a
n
o
i
s
n
e
m
i
d
-
h
g
i
h

s
e
r
u
t
a
e
f

d
e
s
i
v
r
e
p
u
s
n
u

g
n
i
n
r
a
e
l

r
o
f

l
u
f
e
s
U

y
s
a
t
n
a
f

d
n
a

,
n
o
i
t
c
a

,
a
m
a
r
d

g
n
i
d
u
l
c
n
i

e
r
o
m
d
e
g
r
e
v
n
o
c

e
b

n
a
c

g
n
i
n
i
a
r
t

,
s
n
i
a
h
c

e
r
u
t
a
r
e
p
m
e
t

r
e
w
o
l

h
t
i

W

-

f
o

e
s
u
a
c
e
b
M
B
D

l
a
n
o
i
t
i
d
a
r
t

a

n
a
h
t

r
e
t
s
a
f

y
l
e
v
i
t
a
r
a
p
m
o
c

s
i

t
I

s
r
e
ff
u
s

y
c
a
r
u
c
c
a

e
h
t

t
u
b

,
y
l
d
i
p
a
r

s
e
d
o
n

e
h
t

g
n
o
m
a

s
n
o
i
t
c
e
n
n
o
c

f
o

r
e
b
m
u
n

e
h
t

n
i

s
n
o
i
t
a
t
i

m

i
l

e
h
t

-

-

-
r
e
v
i
d

e
v
i
t
s
a
r
t
n
o
c

s
a

h
c
u
s

s

M
B
R

f
o

s
m
h
t
i
r
o
g
l
a

g
n
i
n
i
a
r
t

e
h
T
-

s
e
l
b
a
i
r
a
v

n
e
d
d
i
h

l
a
r
e
v
e
s

e
n
i
m
r
e
t
e
d

d
n
a

e
n
i
m
a
x
e

o
t

e
l
b
a
p
a
C

-

M
B
R
n
a

n
r
a
e
l

o
t

s
s
e
c
o
r
p

e
v
i
s
n
e
t
n
i

y
l
l
a
n
o
i
t
a
t
u
p
m
o
C

-

e
r
o
m
g
n
i
t
a
r
o
p
r
o
c
n
i

y
b

d
e
c
n
a
h
n
e

e
b

n
a
c

y
t
i
c
a
p
a
c

g
n
i
l
l
e
d
o
M

-

)

M
B
R

(

e
n
i
h
c
a

M
n
n
a
m
z
t
l
o
B
d
e
t
c
i
r
t
s
e
R

s
e
g
n
e
l
l
a
h
C

s
e
g
a
t
n
a
v
d
A

s
l
e
d
o
m
g
n
i
n
r
a
e
l

p
e
e
D

)
d
e
u
n
i
t
n
o
c
(

3
e
l
b
a
T

1 3

13599

limited in its applicability because of the extensive computer resources and training data-
sets it necessitates. It is still a mystery as to how exactly DL models arrive at their conclu-
sions. Not like in traditional ML, where we can trace back the reasoning behind a system’s
identification of a given image as representing a cat rather than a dog. To rectify errors in
DL algorithms, the entire algorithm must be modified. However, no universally applicable
theory is available that can help us to choose the appropriate DL tools as it needs knowl-
edge of training methods, topology, and other features.

6   Comparative analysis of deep learning modelling techniques

Through  the  present  review,  it  has  been  determined  to  what  extent  deep  learning  (DL)
modelling  techniques  can  be  used  in  real-world  applications.  In  addition,  the  methods
employed,  the  outcomes,  and  the  challenges  of  DL  that  have  been  modelled  are  identi-
fied. The comparative study compares available DL techniques based on their strengths and
weaknesses, as well as performance metrics. The advantages and challenges outlined in the
previous section make up the basis for the comparative study on strengths and weaknesses.

6.1   Comparative study based on weakness and strength

One  of  the  common  DL  models,  namely  the  vector  space  model  (VSM)  is  found  simple
in structure and allows the computation of the similarity degree between documents and
queries  on  a  continuous  scale.  In  contrast,  the  VSM  assumes  that  words  are  statistically
independent. Additionally, documents with a similar context and distinct term vocabulary
will not be connected, resulting in a "false negative" match. Convolutional neural network
(CNN), on the other hand, uses less time for classification and has good precision in image
recognition  challenges.  However,  comparatively  larger  data  sets  are  required  to  train  for
CNN.  Poor  data  labeling  is  another  disadvantage  of  CNN,  which  can  dramatically  affect
system performance and precision. Several classification issues, including image classifica-
tion, have been successfully addressed using a predictive coding network (PCN). One of its
drawbacks is that there is a lack of certainty regarding how the estimated error minimiza-
tion functions.

It is observed that the recurrent neural network (RNN) is useful for time series forecast-
ing. In RNN, weight remains constant across all levels, minimizing the number of param-
eters the network must learn. However, gradient and explosion vanishing issues limit the
length  of  RNN  sequences.  Its  computation  process  is  comparatively  slow  because  of  its
repeated/recurrent  nature.  However,  for  highly  optimal  execution,  a  long  training  period
may be needed. In most cases, the efficiency and accuracy of the Hierarchical bidirectional
recurrent neural network (HBRNN) are comparatively better than the other networks as it
is  constructed  through  the  extensions  of  bidirectional  recurrent  neural  network  (BRNN)
and RNN. Before predictions can be made with HBRNN, the full sequence must be acces-
sible. On the basis of the scoring function, the recursive neural network (RvNN) is capable
of detecting samples that are relatively similar to one another. Obtaining labeled data for
RvNNs is an incredibly challenging and time-consuming task. Compared to a typical neu-
ral network layer, a neural tensor network (NTN) is a powerful tool for modelling relational

Deep learning modelling techniques: current progress,…1 313600

S. F. Ahmed et al.

data. Massive triplet samples are required for NTN to properly train, however, this has a
little effect on sparse knowledge graphs on a global scale.

Deep  belief  network  (DBN)  enables  highly  efficient  applications  in  the  domains  of
handwriting,  face,  and  speech  recognition  due  to  the  model’s  continual  learning  of  the
characteristics  of  randomly  input  samples.  However,  DBNs  do  not  account  for  the  two-
dimensional structure of input images, which could significantly affect their performance.
Attention  mechanism  can  deduce  information  from  an  input  that  is  most  pertinent  to
accomplishing  a  task,  hence  enhancing  performance,  especially  in  language  processing.
Ambiguous  inputs  can  be  handled  by  Deep  Boltzmann  machine  (DBM)  more  robustly.
DBM  is  capable  of  identifying  latent  features  in  data.  One  of  the  limitations  of  DBM  is
that maximum probabilistic learning in DBM is a challenge due to the hard inference issue
caused by partition functions. The restricted Boltzmann machine (RBM) is comparatively
faster  than  a  traditional  DBM  because  of  the  limitations  in  the  number  of  connections
among the nodes. But the process of learning an RBM is computationally intensive, and in
the case of large datasets, the combined optimization of the parameters is not feasible due
to the slower approximation interface of RBMs.

A well-generalized ability on smaller datasets makes capsule neural network (CapsNet)
suitable for use in a wide range of applications. CapsNets are not able to perform consist-
ently  across  various  datasets,  particularly  large  datasets  such  as  ImageNet.  Using  hidden
deterministic layers as opposed to hidden stochastic layers, the deep energy model (DEM)
can perform interface and learn quickly. It is less popular due to computational difficulties
and the difficulty of evaluating the likelihood (learning) in DEMs. A generative adversar-
ial network (GAN) does not require estimating a probability distribution by introducing a
lower bound like a variational autoencoder. But GAN has a mode collapse problem, and its
data-generation process is intrinsically slow.

6.2   Comparative study based on performance criteria

This  section  compares  the  performance  of  several  deep  learning  modelling  techniques
based on two key performance factors such as prediction accuracy and complexity level,
which are crucial for suitable model selection. The study of the computational complex-
ity of deep learning models is important because it can answer the fundamental question
of  why  deep  learning  architecture  performs  substantially  better  than  traditional  machine
learning  algorithms.  In  addition,  understanding  the  complexity  is  useful  to  analyze  and
compare  different  deep  learning  models  and  improve  their  performance.  The  complexity
analysis of deep learning models highly depends on the model structure; on the other hand,
the  models  are  structurally  different.  Therefore,  they  cannot  be  generalized  and  directly
compared to one another.

One  of  the  recent  studies  (Hu  et  al.  2021)  surveyed  the  latest  research  on  model  com-
plexity  in  deep  learning.  In  the  study,  four  factors  that  influence  the  deep  learning  model
complexity were surveyed: (i) model framework including activation functions such as tanh,
ReLu, and others, (ii) model size, including the depths of the neural network layers and the
number of trainable parameters, (iii) optimization process such as the number of iterations
(epochs)  to  optimize  the  model,  optimization  algorithms,  hyperparameters,  and  (iv)  data
complexity,  which  includes  class  imbalance  and  high  dimensional  data.  The  performance
of a DL model also relies on other parameters such as hardware platforms (high-end GPU),
compiler optimization, and implementation tools. Based on some of those factors and lit-
erature availability, we analyze the performance and computational complexity of different

1 3
Table 4   Comparison of different variants of deep learning architectures applied in different fields based on
performance criteria and complexity

Deep learning model

Applied field

Performance (prediction accu-
racy or other matrices)

Compu-
tational
complexity

13601

AE

BD-LSTM
Bi-LSTM
CNN

CNN-LSTM
GRU
LSTM
RNN

RNN-GRU
RNN-LSTM
RNN-LSTM

Time Series Prediction

Sentiment Analysis
Time Series Prediction
Sentiment Analysis
Malicious URLs Detection
Human Activity Recognition
Intrusion Detection Systems
Malicious URLs Detection
Time Series Prediction
Time Series Prediction
Sentiment Analysis
Time Series Prediction
Intrusion Detection Systems
Sentiment Analysis
Sentiment Analysis
Human Activity Recognition

High

High
Medium
Medium
High
High
Medium
High
Medium
Medium
Low
Low
High
Medium
High
Medium

High

High
High
High
Medium
High
Medium
Medium
Medium
Medium
Low
Medium
Medium
Medium
Medium
Medium

variants of deep learning models across different application fields (Seo et al. 2020; Zeroual
et al. 2020; Cui et al. 2018; Vazhayil et al. 2018; Shakya et al. 2018), and classify them into
three  categories:  Low,  Medium,  and  High,  as  illustrated  in  Table  4.  The  lack  of  relevant
comparative DL literature is identified as the key challenge behind this comparative survey.

The time complexity of an algorithm mainly depends on the input data, and it can be
described using the big-oh notation. Due to its complex nature of architecture, structural
differences, and many other factors, the time complexity of the deep learning model is usu-
ally  measured  by  how  long  it  takes  a  model  to  solve  a  problem  on  specified  hardware.
An  empirical  analysis  of  how  the  configuration  settings  affect  the  running  time  of  deep
learning models was conducted by Lee and Chen (2020). The analysis demonstrated that
model complexity increases the running time, but if the data quality is below average, it
is not worthwhile to increase model complexity. In the sentiment analysis task, increasing
the  CNN  model’s  complexity  may  not  improve  the  performance,  whereas  increasing  the
RNN model’s complexity invariably improves the model performance. Bi-LSTM is found
to be superior to other CNN and RNN models for sentiment analysis (Seo et al. 2020). In
malicious  URL  detection,  CNN-LSTM  gives  comparatively  high  accuracy  than  ordinary
CNN with a little more computational cost (Vazhayil et al. 2018). However, CNN shows a
significant improvement over RNN-LSTM in computer vision tasks such as human activity
recognition (Shakya et al. 2018). CNN is a better choice in intrusion detection systems if
it is a binary classification problem (Cui et al. 2018). For multi-class classification, regular
CNN  performs  poor  than  others  while  RNN  is  a  good  choice  because  of  the  sequential
data. It is much more computationally expensive than RNN in its architecture. Compared
to RNN, Auto Encoder (AE) shows superior performance in forecasting time-series data.
But RNN is relatively faster and needs less computational cost than LSTM, Bi-LSTM, and
AE (Zeroual et al. 2020).

Deep learning modelling techniques: current progress,…1 313602

S. F. Ahmed et al.

7   Future of deep learning

As we step foot into a new era of surplus big data and information, the future of deep learn-
ing  is  not  only  prominent  but  vital  for  the  advancement,  resilience,  and  problem-solving
endeavors of the globe. Deep learning has become a necessary tool across every discipline
from science, engineering, humanity, and health to climate studies and many more. From
developing cybersecurity and surveillance to performing quantum computing, deep learn-
ing will be an evident constant of the future. With the great success of deep networks in
the  field  of  computer  vision  and  the  development  of  artificial  intelligence,  being  able  to
extract meaningful and correct features from data to generate necessary outcomes, without
discrimination  and  being  more  tolerant  of  nuisance  variations  in  data  (Deng  2014;  Guo
et al. 2016), deep learning is the basis for future innovations. As of yet, further knowledge
and understanding are required to improve and construct deep learning networks that deal
with  complex  high  dimensionality  data  and  variations  to  characterize  inputs  and  outputs
efficiently (Kato et al. 2016).

The  growing  interest  in  investments,  particularly  of  giant  tech  companies  (Google,
Facebook, Apple), represents and signals the value and potency of deep learning in the pre-
sent and future. Although deep learning demands high computational power and constant
training to generate reliable results, more work is yet to be done to ensure that deep learn-
ing networks are efficient and cost-effective in extracting and identifying distinct features
from  real-world  data,  mimicking  the  ability  of  biological  intelligence.  Therefore,  when
constructing a deep learning methodology, it is important to ensure that the model can deal
with uncertainty, is scalable, and has transferable qualities to be implemented and applied
to multiple problem systems (Zhang et al. 2020). Alongside the development of deep learn-
ing techniques, the availability of user-friendly hardware and software systems are signifi-
cant future prospects for deep learning.

Larger  and  more  extensive  datasets  are  necessary  for  enhancing  the  performance  of
DL  models  in  a  complex  and  dynamic  construction  environment  including  many  human
resources,  several  types  of  equipment,  and  a  variety  of  human  and  equipment  activities
(Fink et al. 2020). As humanity surfs the wave of artificial intelligence and deep learning,
ethical frameworks must be developed to ensure the sound employment and enhancement
of  deep  learning  techniques  in  order  to  manage  proper  conduction  and  utilization  of  big
data  that  are  fed  into  deep  learning  architectures,  subsequently  generating  beneficial  and
sustainable solutions. Due to the small sample size of training and limited unsafe activities
considered, several workers’ actions can not be recognized (Ding et al. 2018). With a larger
dataset, the model can therefore improve and give more precise results. Nevertheless, there
is  presently  no  publicly  available  complete  and  standardized  dataset,  also  for  particular
tasks like activity recognition, pose detection and object detection, as well as for different
views, a wide range of construction sites, occlusion circumstances, and lighting.

Combining deep learning with expert knowledge can be a fruitful area of research since
models may be dynamically augmented with acquired new data, resulting in effective digi-
tal  twins  which  can  help  in  maintenance  decision  making.  Despite  the  fact  that  physics-
induced  deep  learning  is  now  pursuing  multiple  directions,  there  is  no  agreement  or  no
consolidation on various directions as well as how they can be translated to industrial appli-
cations. There is a need for additional studies to refine and consolidate these techniques,
which may help increase the generalization ability of the models developed. Another issue
that must be addressed in future studies is the effective selection and composition of sets of
training data. This is especially important in environments that are constantly changing and

1 3
have extremely variable operating conditions, where the training dataset is not representa-
tive  of  the  whole  range  of  predicted  operating  conditions.  Continuous  decisions  must  be
made as to whether new data needs to be included in training datasets and the algorithms
updated, or whether the information is repetitive and included already in the datasets used
for training the algorithms.

13603

8   Conclusion

Deep  learning  (DL)  is  a  thriving  multidisciplinary  field  that  is  still  in  its  nascent  phase.
With  the  growing  availability  of  data,  DL  architectures  can  be  successfully  applied  to
problems  across  various  sectors  in  the  modern  world.  This  paper  provides  a  comprehen-
sive systematic review of the state-of-the-art DL modelling techniques. Some models can
be trained by two or more methods, which means their efficiency relies on the domain in
which they are used. The use of hierarchical layers for proper data classification, as well
as  supervision  in  learning  to  determine  the  importance  of  the  database  of  interest,  are
both important factors to develop robust DL models. While nearly all of the models dis-
play  robustness  to  some  extent,  existing  techniques  are  still  flawed,  which  subjects  them
to criticisms. With the availability of big data across various domains, the quality of data
can become an issue when training DL models. Training DL models can also be very time-
consuming,  expensive,  and  requires  hundreds  of  correct  examples  for  better  accuracy,
which can limit their use for everyday purposes or in sensitive security systems. The result-
ing models may also be domain-specific and, therefore, may have restricted applications.
In  addition,  DL  is  susceptible  to  deception  and  misclassification,  which  can  threaten  the
social  and  financial  securities  of  individuals  and/or  corporations.  Getting  stuck  on  local
minima also makes most models unsuitable for online modes.

CNNs, RNNs, GANs, and autoencoders are the more frequently used DL architectures
across  various  sectors.  However,  the  potential  application  of  other  architectures  in  cur-
rent areas that use DL is widely unexplored. This paper found that advanced DL models,
which are essentially hybrid conventional DL architectures, have the potential to overcome
the challenges experienced by conventional models. Moreover, generative models exhibit
greater capabilities as they are less reliant on examples. Future networks should strive to
generate a set of possible outcomes, instead of providing one final prediction for the input,
which may help tackle the issue of distorted or unclear inputs. Developing new strategies
to  optimize  parameters,  particularly  hyperparameters,  is  another  possibility  that  requires
further investigation. Capsule architectures may dominate future DL models as they offer
an enhanced way of routing information between layers. If the current challenges can be
addressed, DL models can potentially contribute to further innovations in the field of AI
and for solving far more complex problems.

Acknowledgements  The  authors  highly  express  their  gratitude  to  Asian  University  for  Women,  Chatto-
gram, Bangladesh for their support in carrying out this study.

Funding  Open Access funding enabled and organized by CAUL and its Member Institutions.

Declarations

Conflict of interest  The authors declare that they have no known competing financial interests or personal
relationships that could appear to have influenced the work reported in this study.

Deep learning modelling techniques: current progress,…1 313604

S. F. Ahmed et al.

Open  Access  This  article  is  licensed  under  a  Creative  Commons  Attribution  4.0  International  License,
which  permits  use,  sharing,  adaptation,  distribution  and  reproduction  in  any  medium  or  format,  as  long
as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Com-
mons licence,  and indicate if changes were made. The images or other third party material in this article
are  included  in  the  article’s  Creative  Commons  licence,  unless  indicated  otherwise  in  a  credit  line  to  the
material. If material is not included in the article’s Creative Commons licence and your intended use is not
permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly
from the copyright holder. To view a copy of this licence, visit http:// creat iveco mmons. org/ licen ses/ by/4. 0/.

References

Abbas AA, Naderi E, Gandali A, Hanieh M (2016) Comparative study of static and dynamic artificial neural
network models in forecasting of tehran stock exchange. Int J Bus Dev Stud 8:43–59. https:// doi. org/
10. 22111/ IJBDS. 2016. 2635

Abdel-Zaher AM, Eldeib AM (2016) Breast cancer classification using deep belief networks. Expert Syst

Appl 46:139–144. https:// doi. org/ 10. 1016/j. eswa. 2015. 10. 015

Abedinia O, Amjady N, Ghadimi N (2018) Solar energy forecasting based on hybrid neural network and

improved metaheuristic algorithm. Comput Intell 34(1):241–260. https:// doi. org/ 10. 1111/ coin. 12145

Achanta S, Gangashetty SV (2017) Deep Elman recurrent neural networks for statistical parametric speech

synthesis. Speech Commun 93:31–42. https:// doi. org/ 10. 1016/j. specom. 2017. 08. 003

Adhikari A, Ram A, Tang R, Lin J (2019) DocBERT: BERT for document classification. arXiv: 1904. 08398
Afshar P, Mohammadi A, Plataniotis KN (2018) Brain tumor type classification via capsule networks. In:
Proceedings - international conference on image processing, ICIP. https:// doi. org/ 10. 1109/ ICIP. 2018.
84513 79

Ahmad J, Farman H, Jan Z (2019) Deep learning methods and applications. In: SpringerBriefs in computer

science. https:// doi. org/ 10. 1007/ 978- 981- 13- 3459-7_3

Akkus  Z,  Galimzianova  A,  Hoogi  A,  Rubin  DL,  Erickson  BJ  (2017)  Deep  learning  for  brain  MRI  seg-
mentation: state of the art and future directions. J Digit Imaging 30:449–459. https:// doi. org/ 10. 1007/
s10278- 017- 9983-4

Alain G, Bengio Y, Courville A, Fergus R, Manning C (2014) What regularized auto-encoders learn from

the data-generating distribution. J Mach Learn Res 15(1):3563–3593

Alam MR, Bennamoun M, Togneri R, Sohel F (2017) A joint deep Boltzmann machine (jDBM) model for
person identification using mobile phone data. IEEE Trans Multimed 19(2):317–326. https:// doi. org/
10. 1109/ TMM. 2016. 26155 24

Alemany S, Beltran J, Perez A, Ganzfried S (2019) Predicting hurricane trajectories using a recurrent neural
network.  In:  33rd  AAAI  conference  on  artificial  intelligence,  AAAI  2019,  31st  innovative  applica-
tions of artificial intelligence conference, IAAI 2019 and the 9th AAAI symposium on educational
advances in artificial intelligence, EAAI 2019.  https:// doi. org/ 10. 1609/ aaai. v33i01. 33014 68

Ali F, Kwak D, Khan P, El-Sappagh S, Ali A, Ullah S, Kim KH, Kwak KS (2019) Transportation sentiment
analysis using word embedding and ontology-based topic modeling. Knowledge-Based Syst. https://
doi. org/ 10. 1016/j. knosys. 2019. 02. 033

Al-Jumeily D, Ghazali R, Hussain A (2014) Predicting physical time series using dynamic ridge polynomial

neural networks. PLoS ONE 9(8):e105766. https:// doi. org/ 10. 1371/ journ al. pone. 01057 66

Alpaydin E (2020) Introduction to machine learning. MIT Press, Cambridge
Arabasadi Z, Alizadehsani R, Roshanzamir M, Moosaei H, Yarifard AA (2017) Computer aided decision
making for heart disease detection using hybrid neural network-genetic algorithm. Comput Methods
Programs Biomed. https:// doi. org/ 10. 1016/j. cmpb. 2017. 01. 004

Arora  S,  Ma  T,  Moitra  A  (2015)  Simple,  efficient,  and  neural  algorithms  for  sparse  coding.  PMLR,  pp

113–149

Arulkumaran  K,  Deisenroth  MP,  Brundage  M,  Bharath  AA  (2017)  A  brief  survey  of  deep  reinforcement
learning. In: IEEE signal processing magazine, special issue on deep learning for image understand-
ing pp 1–16

Ba J, Hinton G, Mnih V, Leibo JZ, Ionescu C (2016) Using fast weights to attend to the recent past. Adv

Neural Inf Process Syst 29:4338–4346

Baecchi C, Uricchio T, Bertini M, Del Bimbo A (2016) A multimodal feature learning approach for sen-
timent  analysis  of  social  network  multimedia.  Multimed  Tools  Appl.  https:// doi. org/ 10. 1007/
s11042- 015- 2646-x

1 3
13605

Bai Y, Fu J, Zhao T, Mei T (2018) Deep attention neural tensor network for visual question answering. In:
Lecture notes in computer science (including subseries lecture notes in artificial intelligence and lec-
ture notes in bioinformatics). https:// doi. org/ 10. 1007/ 978-3- 030- 01258-8_2

Barré P, Stöver BC, Müller KF, Steinhage V (2017) LeafNet: a computer vision system for automatic plant

species identification. Ecol Inform. https:// doi. org/ 10. 1016/j. ecoinf. 2017. 05. 005

Bartunov S, Rae JW, Osindero S, Lillicrap TP (2019) Meta-learning deep energy-based memory models.

https:// arXiv. org/ 1910. 02720

Basiri ME, Nemati S, Abdar M, Cambria E, Acharya UR (2021) ABCDM: an attention-based bidirectional
CNN-RNN  deep  model  for  sentiment  analysis.  Futur  Gener  Comput  Syst  115:279–294.  https:// doi.
org/ 10. 1016/j. future. 2020. 08. 005

Bau D, Zhu JY, Strobelt H, Zhou B, Tenenbaum JB, Freeman WT, Torralba A (2019) GaN dissection: visu-
alizing and understanding generative adversarial networks. In: 7th international conference on learn-
ing representations, ICLR 2019

Bengio Y, Simard P, Frasconi P (1994) Learning long-term dependencies with gradient descent is difficult.

IEEE Trans Neural Netw 5(2):157–166. https:// doi. org/ 10. 1109/ 72. 279181

Bengio  Y,  Courville  A,  Vincent  P  (2013)  Representation  learning :  a  review  and  new  perspectives.  IEEE

Trans Pattern Anal Mach Intell 35:1798–1828

Ben-Younes H, Cadene R, Cord M, Thome N (2017) MUTAN: multimodal tucker fusion for visual question
answering. In: Proceedings of the IEEE international conference on computer vision. https:// doi. org/
10. 1109/ ICCV. 2017. 285

Biancofiore F, Busilacchio M, Verdecchia M, Tomassetti B, Aruffo E, Bianco S, Di Tommaso S, Colangeli
C, Rosatelli G, Di Carlo P (2017) Recursive neural network model for analysis and forecast of PM10
and PM25. Atmos Pollut Res. https:// doi. org/ 10. 1016/j. apr. 2016. 12. 014

Bordes  A,  Weston  J,  Chopra  S  (2014)  Question  answering  with  subgraph  embeddings.  https:// arXiv. org/

1406. 3676

Bousmalis  K,  Trigeorgis  G,  Silberman  N,  Krishnan  D,  Erhan  D  (2016)  Domain  separation  networks.  In:

Advances in neural information processing systems

Brahma  S  (2018)  Improved  sentence  modeling  using  suffix  bidirectional  LSTM.  https:// arXiv. org/ 1805.

07340

Brocardo ML, Traore I, Woungang I, Obaidat MS (2017) Authorship verification using deep belief network

systems. Int J Commun Syst 30:e3259. https:// doi. org/ 10. 1002/ dac. 3259

Brock A, Donahue J, Simonyan K (2019) Large scale GaN training for high fidelity natural image synthesis.

In: 7th international conference on learning representations, ICLR 2019

Camgoz NC, Hadfield S, Koller O, Ney H, Bowden R (2018) Neural sign language translation. In: Proceed-
ings of the IEEE computer society conference on computer vision and pattern recognition. https:// doi.
org/ 10. 1109/ CVPR. 2018. 00812

Cao Z, Duan L, Yang G, Yue T, Chen Q (2019) An experimental study on breast lesion detection and clas-
sification from ultrasound images using deep learning architectures. BMC Med Imaging 19:1–9
Carrio  A,  Sampedro  C,  Rodriguez-ramos  A,  Campoy  P  (2017)  A  review  of  deep  learning  methods  and

applications for unmanned aerial vehicles. J Sensors 14:2017. https:// doi. org/ 10. 1155/ 2017/ 32968 74

Case C, Casper J, Catanzaro B, Diamos G, Elsen E (2014) Deep speech: scaling up end-to-end speech rec-

ognition. https:// arXiv. org/ 1412. 5567

Chang S, Liu J (2020) Multi-lane capsule network for classifying images with complex background. IEEE

Access 8:79876–79886. https:// doi. org/ 10. 1109/ ACCESS. 2020. 29907 00

Chen X, Kundu K, Zhu Y, Ma H, Fidler S, Urtasun R (2018a) 3D object proposals using stereo imagery for
accurate  object  class  detection.  IEEE  Trans  Pattern  Anal  Mach  Intell  40(5):1259–1272.  https:// doi.
org/ 10. 1109/ TPAMI. 2017. 27066 85

Chen Y, Li W, Sakaridis C, Dai D, Van Gool L (2018b) Domain adaptive faster R-CNN for object detection
in the wild. In: Proceedings of the IEEE computer society conference on computer vision and pattern
Recognition. https:// doi. org/ 10. 1109/ CVPR. 2018. 00352

Chen  YY,  Lin  YH,  Kung  CC,  Chung  MH,  Yen  I  (2019)  Design  and  implementation  of  cloud  analytics-
assisted smart power meters considering advanced artificial intelligence as edge analytics in demand-
side managment for smart homes. Sensors 19:2047

Cheng J, Dong L, Lapata M (2016) Long short-term memory-networks for machine reading. EMNLP con-
ference on empirical methods in natural language processing, proceedings. https:// doi. org/ 10. 18653/
v1/ d16- 1053

Chicco D, Sadowski P, Baldi P, Milano P, Elettronica D (2014) Deep autoencoder neural networks for gene
ontology annotation predictions. In: 5th ACM conference on bioinformatics, computational biology,
and health informatics - BCB’14. pp 533–540. https:// doi. org/ 10. 1145/ 26493 87. 26494 42

Deep learning modelling techniques: current progress,…1 313606

S. F. Ahmed et al.

Chu  Q,  Ouyang  W,  Li  H,  Wang  X,  Liu  B,  Yu  N  (2017)  Online  multi-object  tracking  using  CNN-based
single object tracker with spatial-temporal attention mechanism. In: Proceedings of the IEEE interna-
tional conference on computer vision. https:// doi. org/ 10. 1109/ ICCV. 2017. 518

Cireşan D, Meier U, Masci J, Schmidhuber J (2012) Multi-column deep neural network for traffic sign clas-

sification. Neural Netw 32:333–338. https:// doi. org/ 10. 1016/j. neunet. 2012. 02. 023

Collobert R, Weston J, Bottou L, Karlen M, Kavukcuoglu K, Kuksa P (2011) Natural language processing

(Almost) from scratch. J Mach Learn Res 12:2493–2537

Cui J, Long J, Min E, Liu Q, Li Q (2018) Comparative study of CNN and RNN for deep learning based
intrusion detection system. In: Lecture notes in computer science (including subseries lecture notes in
artificial intelligence and lecture notes in bioinformatics). https:// doi. org/ 10. 1007/ 978-3- 030- 00018-
9_ 15

Da’u A, Salim N (2020) Recommendation system based on deep learning methods: a systematic review and

new directions. Artif Intell Rev 53:2709–2748. https:// doi. org/ 10. 1007/ s10462- 019- 09744-1

Dahl  GE,  Ranzato  M,  Mohamed  AR,  Hinton  G  (2010)  Phone  recognition  with  the  mean-covariance

restricted Boltzmann machine. Adv Neural Inf Process Syst 23:469–477

De S, Maity A, Goel V, Shitole S, Bhattacharya A (2017) Predicting the popularity of instagram posts for
a  lifestyle  magazine  using  deep  learning.  In:  2017  2nd  international  conference  on  communication
systems, computing and IT applications (CSCITA) pp 174–177

Demeester  T,  Sutskever  I,  Chen  K,  Dean  J,  Corado  G  (2016)  Distributed  representations  of  words  and
phrases and their compositionality. EMNLP 2016 - Conference empirical methods natural language
process processing

Deng L (2014) A tutorial survey of architectures, algorithms, and applications for deep learning. APSIPA

Trans Signal Inf Process 3:e2. https:// doi. org/ 10. 1017/ atsip. 2013.9

Deng L, Yu D (2014) Deep learning: methods and applications. Found Trends Signal Process 7:197–387
Deng F, Pu S, Chen X, Shi Y, Yuan T, Shengyan P (2018) Hyperspectral image classification with capsule
network using limited training samples. Sensors 18(9):3153. https:// doi. org/ 10. 3390/ s1809 3153
Deoras A, Povey D, Mikolov T, Burget L, Černocký J (2011) Strategies for training large scale neural net-
work  language  models.  In:  IEEE  workshop  on  automatic  speech  recognition  and  understanding  pp
196–201

Dhyani M, Kumar R (2019) An intelligent Chatbot using deep learning with Bidirectional RNN and atten-

tion model. Mater Today Proceedings. https:// doi. org/ 10. 1016/j. matpr. 2020. 05. 450

Dick S (2019) Artificial intelligence. Harvard Data Sci Rev 1:1–8. https:// doi. org/ 10. 1162/ 99608 f92. 92fe1

50c

Ding L, Fang W, Luo H, Love PED, Zhong B, Ouyang X (2018) A deep hybrid learning model to detect
unsafe behavior: integrating convolution neural networks and long short-term memory. Autom Constr
86:118–124

Dixit M, Tiwari A, Pathak H, Astya R (2018) An overview of deep learning architectures, libraries and its
applications areas. In 2018 international conference on advances in computing, communication con-
trol and networking. pp 293–297. https:// doi. org/ 10. 1109/ ICACC CN. 2018. 87484 42

Do Rosario VM, Borin E, Breternitz M (2019) The multi-lane capsule network. IEEE Signal Process Lett

26:1006–1010. https:// doi. org/ 10. 1109/ LSP. 2019. 29156 61

do  Rosario  VM,  Breternitz  M,  Borin  E  (2021)  Efficiency  and  scalability  of  multi-lane  capsule  networks
(MLCN). J. Parallel Distrib Comput. 155:63–73. https:// doi. org/ 10. 1016/J. JPDC. 2021. 04. 010
Dora  S,  Pennartz  C,  Bohte  S  (2018)  A  deep  predictive  coding  network  for  inferring  hierarchical  causes
underlying  sensory  inputs,  Lecture  notes  in  computer  science  (including  subseries  lecture  notes  in
artificial  intelligence  and  lecture  notes  in  bioinformatics).  Springer.  https:// doi. org/ 10. 1007/ 978-3-
030- 01424-7_ 45

Dumoulin V, Perez E, Schucher N, Strub F, Vries H, Courville A, Bengio Y (2018) Feature-wise transfor-

mations. Distill. https:// doi. org/ 10. 23915/ disti ll. 00011

Dumoulin V, Shlens J, Kudlur M (2017) A learned representation for artistic style. In: 5th international con-

ference on learning representations, ICLR 2017 - conference track proceedings

Elman JL (1990) Finding structure in time. Cogn Sci 14(2):179–211. https:// doi. org/ 10. 1016/ 0364- 0213(90)

90002-E

Elman JL (1998) Generalization, simple recurrent networks, and the emergence of structure. In: Proceedings

20th annual conference cognitive science society

Eslami  SMA,  Heess  N,  Williams  CKI,  Winn  J  (2014)  The  shape  boltzmann  machine:  a  strong  model  of

object shape. Int J Comput Vis 107:155–176. https:// doi. org/ 10. 1007/ s11263- 013- 0669-1

Fayek HM, Lech M, Cavedon L (2017) Evaluating deep learning architectures for speech emotion recogni-

tion. Neural Netw 92:60–68. https:// doi. org/ 10. 1016/j. neunet. 2017. 02. 013

1 3
13607

Feng X, Zhang H, Ren Y, Shang P, Zhu Y, Liang Y (2019) The deep learning-based recommender system
“pubmender” for choosing a biomedical publication venue: development and validation study. J Med
Internet Res 21:e12957. https:// doi. org/ 10. 2196/ 12957

Fink O, Wang Q, Svensen M, Dersin P, Lee W-J, Ducoffe M (2020) Potential, challenges and future direc-
tions  for  deep  learning  in  prognostics  and  health  management  applications.  Eng  Appl  Artif  Intell
92:103678

Gallicchio C Micheli A Pedrelli L (2018a) Deep echo state networks for diagnosis of Parkinson’s disease.
In: ESANN 2018a - Proceedings, European symposium on artificial neural networks, computational
intelligence and machine learning

Gallicchio C, Micheli A, Pedrelli L (2018b) Design of deep echo state networks. Neural Netw 108:33–47.

https:// doi. org/ 10. 1016/j. neunet. 2018. 08. 002

Gao Y, Gao F, Dong J, Li HC (2021) SAR image change detection based on multiscale capsule network.
IEEE Geosci Remote Sens Lett. 18(3):484–488  https:// doi. org/ 10. 1109/ LGRS. 2020. 29778 38
Gehring J, Auli M, Grangier D, Yarats D, Dauphin YN (2017) Convolutional sequence to sequence learn-

ing. In: 34th International conference on machine learning, ICML 2017

Gevaert CM, Suomalainen J, Tang J, Kooistra L (2015) Generation of spectral-temporal response surfaces
by combining multispectral satellite and hyperspectral UAV imagery for precision agriculture appli-
cations. IEEE J Sel Top Appl Earth Obs Remote Sens. https:// doi. org/ 10. 1109/ JSTARS. 2015. 24063
39

Gheisari M, Wang G, Bhuiyan ZA (2017) A survey on deep learning in big data. In: 2017 IEEE Interna-
tional conference on computational science and engineering (CSE) and IEEE international conference
on embedded and ubiquitous computing (EUC) 2:173–180

Ghiasi G, Lee H, Kudlur M, Dumoulin V, Shlens J (2017) Exploring the structure of a real-time, arbitrary
neural artistic stylization network. In: British machine vision conference 2017, BMVC 2017. https://
doi. org/ 10. 5244/c. 31. 114

Ghosh R, Ravi K, Ravi V (2016) A novel deep learning architecture for sentiment classification. In: 2016
3rd International conference on recent advances in information technology, RAIT 2016. https:// doi.
org/ 10. 1109/ RAIT. 2016. 75079 53

Godarzi AA, Amiri RM, Talaei A, Jamasb T (2014) Predicting oil price movements: a dynamic artificial
neural network approach. Energy Policy 68: 371–382. https:// doi. org/ 10. 1016/j. enpol. 2013. 12. 049
Goodfellow IJ, Pouget-Abadie J, Mirza M, Xu B, Warde-Farley D, Ozair S, Courville A, Bengio Y (2014)
Generative  adversarial  nets.  Adv  Neural  Inform  Process  Syst.  https:// doi. org/ 10. 3156/ jsoft. 29.5_
177_2

Goodfellow I, Bengio Y, Courville A (2016) Deep learning. MIT Press, Cambridge
Goodfellow IJ, Warde-Farley D, Mirza M, Courville A, Bengio Y (2013) Maxout networks. In: 30th Inter-

national conference on machine learning, ICML 2013.

Govender M, Chetty K, Bulcock H (2007) A review of hyperspectral remote sensing and its application in
vegetation  and  water  resource  studies.  Water  SA  33(2):145–151.  https:// doi. org/ 10. 4314/ wsa. v33i2.
49049

Graves A, Schmidhuber J (2005) Framewise phoneme classification with bidirectional LSTM and other neu-
ral  network  architectures.  Neural  Netw  18(5–6):602–610.  https:// doi. org/ 10. 1016/j. neunet. 2005. 06.
042

Graves  A,  Jaitly  N,  Mohamed  AR  (2013)  Hybrid  speech  recognition  with  Deep  Bidirectional  LSTM.  In:
2013 IEEE workshop on automatic speech recognition and understanding, ASRU 2013 - proceedings
https:// doi. org/ 10. 1109/ ASRU. 2013. 67077 42

Günther F, Dudschig C, Kaup B (2016) Latent semantic analysis cosines as a cognitive similarity measure:
evidence from priming studies. Q J Exp Psychol. https:// doi. org/ 10. 1080/ 17470 218. 2015. 10382 80
Guo  Y,  Liu  Y,  Oerlemans  A,  Lao  S,  Wu  S,  Lew  MS  (2016)  Deep  learning  for  visual  understanding:  a

review. Neurocomputing 187:27–48. https:// doi. org/ 10. 1016/j. neucom. 2015. 09. 116

Gupta A, Anpalagan A, Guan L, Khwaja AS (2021) Deep learning for object detection and scene perception

in self-driving cars: survey, challenges, and open issues. Array 100057

PA Gutiérrez and C Hervás-Martínez (2011) Hybrid artificial neural networks: models, algorithms and data.

In: 11th international work-conference on artificial neural networks

Haarnoja T, Tang, H, Abbeel P, Levine S (2017) Reinforcement learning with deep energy-based policies
Hamilton  WL,  Ying  R,  Leskovec  J  (2017)  Representation  learning  on  graphs:  methods  and  applications.

https:// arXiv. org/ 1709. 05584

Han Y, Huang G, Song S, Yang L, Wang H,  Wang Y (2021) Dynamic Neural networks: a survey. IEEE

Transactions on Pattern Analysis and Machine Intelligence 44(11):7436–7456

Hasan M, Choi J, Neumann J, Roy-Chowdhury AK, Davis LS (2016) Learning temporal regularity in video

sequences

Deep learning modelling techniques: current progress,…1 313608

S. F. Ahmed et al.

Hassan  M,  Bin  Alam  MS,  Ahsan,  T  (2018)  Emotion  detection  from  text  using  skip-thought  vectors.  In:
2018 International conference on innovations in science, engineering and technology, ICISET 2018.
https:// doi. org/ 10. 1109/ ICISET. 2018. 87456 15

He J, Cheng X, He J, Xu H (2019) Cv-CapsNet: Complex-valued capsule network. IEEE Access 7:85492–

85499. https:// doi. org/ 10. 1109/ ACCESS. 2019. 29245 48

He S, Wang S, Lan W, Fu H, Ji Q (2013) Facial expression recognition using deep boltzmann machine from
thermal infrared images. In: Proceedings - 2013 humaine association conference on affective comput-
ing and intelligent interaction, ACII 2013. https:// doi. org/ 10. 1109/ ACII. 2013. 46

Hinton GE (2009) Deep belief networks. Scholarpedia. https:// doi. org/ 10. 4249/ schol arped ia. 5947
Hinton G, Deng L, Yu D, Dahl GE, Mohamed AR, Jaitly N, Senior A, Vanhoucke V, Nguyen P, Sainath TN,
Kingsbury B (2012) Deep neural networks for acoustic modeling in speech recognition: the shared
views of four research groups. IEEE Signal Process Mag 29(6):82–97

Hinton GE, Krizhevsky A, Wang SD (2011) Transforming auto-encoders. In: Lecture notes in computer sci-
ence (including subseries lecture notes in artificial intelligence and lecture notes in bioinformatics).
https:// doi. org/ 10. 1007/ 978-3- 642- 21735-7_6

Hong S, Yang D, Choi J, Lee H (2018) Inferring semantic layout for hierarchical text-to-image synthesis.
In: Proceedings of the IEEE computer society conference on computer vision and pattern recognition.
https:// doi. org/ 10. 1109/ CVPR. 2018. 00833

Hu F, Xia GS, Hu J, Zhang L (2015) Transferring deep convolutional neural networks for the scene classifi-
cation of high-resolution remote sensing imagery. Remote Sens 7(11):14680–14707. https:// doi. org/
10. 3390/ rs711 14680

Hu X, Chu L, Pei J, Liu W, Bian J (2021) Model complexity of deep learning: a survey. Knowl Inf Syst.

https:// doi. org/ 10. 1007/ s10115- 021- 01605-0

Hu  G,  Hua  Y,  Yuan  Y,  Zhang  Z,  Lu  Z,  Mukherjee  SS,  Hospedales  TM,  Robertson  NM,  Yang  Y  (2017)
Attribute-enhanced face recognition with neural tensor fusion networks. In: Proceedings of the IEEE
international conference on computer vision. https:// doi. org/ 10. 1109/ ICCV. 2017. 404

Huang X, Belongie S (2017) Arbitrary style transfer in real-time with adaptive instance normalization. In:
Proceedings of the IEEE international conference on computer vision. https:// doi. org/ 10. 1109/ ICCV.
2017. 167

Huang P, He X, Gao J, Deng L, Acero A, Heck L (2013) Learning deep structured semantic models for web
search using clickthrough data. In: Proceedings of the 22nd ACM international conference on infor-
mation and knowledge management pp 2333–2338

Hughes  M,  Li  I,  Kotoulas  S,  Suzumura  T  (2017)  Medical  text  classification  using  convolutional  neu-
ral  networks.  Studies  in  Health  Technology  and  Informatics,  pp  246–250.  https:// doi. org/ 10. 3233/
978-1- 61499- 753-5- 246

Irsoy O, Cardie C (2014) Deep recursive neural networks for compositionality in language. In: Advances in

neural information processing systems

Ishihara T, Hayashi K, Manabe H, Shimbo M, Nagata M (2018) Neural tensor networks with diagonal slice
matrices. In: NAACL HLT 2018 - 2018 conference of the North American chapter of the association
for computational linguistics: human language technologies - proceedings of the conference. https://
doi. org/ 10. 18653/ v1/ n18- 1047

Jaiswal A, AbdAlmageed W, Wu Y, Natarajan P (2019) CapsuleGAN: generative adversarial capsule net-
work. In: Lecture notes in computer science (including subseries lecture notes in artificial intelligence
and lecture notes in bioinformatics). https:// doi. org/ 10. 1007/ 978-3- 030- 11015-4_ 38

Jayaraman S, Ramachandran M, Patan R, Daneshmand M, Gandomi AH (2022) Fuzzy deep neural learn-
ing based on goodman and Kruskal’s Gamma for Search Engine Optimization. IEEE Trans Big Data
8(1), 268–277

Jenkins  IR,  Gee  LO,  Knauss  A,  Yin  H,  Schroeder  J  (2018)  Accident  scenario  generation  with  recurrent
neural networks. In: 2018 21st International conference on intelligent transportation systems (ITSC).
IEEE, pp 3340–3345

Jiang X, Zhang Y, Liu W, Gao J, Liu J, Zhang Y, Lin J (2020) Hyperspectral image classification with Cap-
snet  and  Markov  random  fields.  IEEE  Access  8:191956–191968.  https:// doi. org/ 10. 1109/ ACCESS.
2020. 30291 74

Jordan MI, Mitchell TM (2015) Machine learning: trends, perspectives, and prospects 349
Kae A, Sohn K, Lee H, Learned-Miller E (2013) Augmenting CRFs with Boltzmann machine shape priors

for image labeling 2019–2026. https:// doi. org/ 10. 1109/ CVPR. 2013. 263

Kaiser  Ł,  Sutskever  I  (2016)  Neural  GPUs  learn  algorithms.  In:  4th  International  conference  on  learning

representations, ICLR 2016 - conference track proceedings

1 3
13609

Karras T, Aila T, Laine S, Lehtinen J (2018) Progressive growing of GANs for improved quality, stability,
and variation. In: 6th international conference on learning representations, ICLR 2018 - conference
track proceedings

Karras T, Laine S, Aila T (2019) A style-based generator architecture for generative adversarial networks.
In: Proceedings of the IEEE conference on computer vision and pattern recognition 2019 pp 4396–
4405. https:// doi. org/ 10. 1109/ CVPR. 2019. 00453

Kashyap PK, Kumar S, Jaiswal A, Prasad M, Gandomi AH (2021) Towards precision agriculture: iot-ena-
bled  intelligent  irrigation  systems  using  deep  learning  neural  network.  IEEE  Sens  J  21(16):17479–
17491. https:// doi. org/ 10. 1109/ JSEN. 2021. 30692 66

Kato N, Fadlullah ZM, Mao B, Tang F, Akashi O, Inoue T, Mizutani K (2016) The deep learning vision for
heterogeneous network traffic control: proposal, challenges, and future perspective. IEEE Wirel Com-
mun 24:146–153 https:// doi. org/ 10. 1109/ MWC. 2016. 16003 17WC

Khamparia  A,  Singh  MM  (2019)  A  systematic  review  on  deep  learning  architectures  and  applications.

Expert Syst 36:e12400. https:// doi. org/ 10. 1111/ exsy. 12400

Khan A, Sohail A, Zahoora U, Qureshi AS (2020) A survey of the recent architectures of deep convolutional
neural networks. Artif Intell Rev 53:5455–5516. https:// doi. org/ 10. 1007/ s10462- 020- 09825-6
Kim JH, On KW, Lim W, Kim J, Ha JW, Zhang BT (2017) Hadamard product for low-rank bilinear pool-
ing.  In:  5th  international  conference  on  learning  representations,  ICLR  2017  -  conference  track
proceedings

Kim  TS,  Reiter  A  (2017)  Interpretable  3D  human  action  analysis  with  temporal  convolutional  networks.
IEEE  Computer  society  conference  on  computer  vision  and  pattern  recognition  workshops.  https://
doi. org/ 10. 1109/ CVPRW. 2017. 207

Kiros R, Zhu Y, Salakhutdinov R, Zemel RS, Torralba A, Urtasun R, Fidler S (2015) Skip-thought vectors.

Advances in neural information processing systems

Kotsiopoulos  T,  Sarigiannidis  P,  Ioannidis  D,  Tzovaras  D  (2021)  Machine  learning  and  deep  learning  in

smart manufacturing: the smart grid paradigm. Comput Sci Rev 40:100341

Kraska T, Beutel A, Chi EH, Dean J, Polyzotis N (2018) The case for learned index structures. In: Proceed-
ings of the ACM SIGMOD international conference on management of data. Association for comput-
ing machinery, New York, pp 489–504. https:// doi. org/ 10. 1145/ 31837 13. 31969 09

Krichene  E,  Masmoudi  Y,  Alimi  AM,  Abraham  A,  Chabchoub  H  (2017)  Forecasting  using  elman  recur-
rent neural network.  Advances in Intelligent Systems and Computing, pp 488–497. https:// doi. org/ 10.
1007/ 978-3- 319- 53480-0_ 48

Krizhevsky A, Hinton GE (2017) ImageNet classification with deep convolutional neural networks. Com-

mun ACM 60:84–90

Kumar A, Ramachandran M, Gandomi AH, Patan R, Lukasik S, Soundarapandian RK (2019) A deep neural

network based classifier for brain tumor diagnosis. Appl Soft Comput 82:105528

Landgrebe D (2002) Hyperspectral image data analysis. IEEE Signal Process Mag 19(1):17–28. https:// doi.

org/ 10. 1109/ 79. 974718

Lara-ben P, Carranza-garc M (2021) An experimental review on deep learning architectures for time series

forecasting. Int J Neural Syst 31:2130001. https:// doi. org/ 10. 1142/ S0129 06572 13000 11

Lea C, Vidal R, Reiter A, Hager GD (2016) Temporal convolutional networks: a unified approach to action
segmentation.  In:  Lecture  notes  in  computer  science  (including  subseries  lecture  notes  in  artificial
intelligence and lecture notes in bioinformatics). https:// doi. org/ 10. 1007/ 978-3- 319- 49409-8_7
LeCun YA, Bottou L, Orr GB, Müller K-R (2012) Efficient backprop BT - neural networks: tricks of the

trade. In: Neural networks: tricks of the trade

Lecun  Y,  Bengio  Y,  Hinton  G  (2015)  Deep  learning.  Nature  521:463–444.  https:// doi. org/ 10. 1038/ natur

e14539

Ledig C, Theis L, Huszár F, Caballero J, Cunningham A, Acosta A, Aitken A, Tejani A., Totz J, Wang Z,
Shi W (2017) Photo-realistic single image super-resolution using a generative adversarial network. In:
Proceedings - 30th IEEE conference on computer vision and pattern recognition, CVPR 2017. https://
doi. org/ 10. 1109/ CVPR. 2017. 19

Lee  R,  Chen  IY  (2020)  The  time  complexity  analysis  of  neural  network  model  configurations.  In:  Pro-
ceedings - 2nd international conference on mathematics and computers in science and engineering,
MACISE 2020. https:// doi. org/ 10. 1109/ MACIS E49704. 2020. 00039

Lee  H,  Grosse  R,  Ranganath  R,  Ng  AY  (2009)  Convolutional  deep  belief  networks  for  scalable  unsuper-
vised learning of hierarchical representations. In: Proceedings of the 26th international conference on
machine learning, ICML 2009 https:// doi. org/ 10. 1145/ 15533 74. 15534 53

Lemley J, Bazrafkan S, Corcoran P (2017) Deep learning for consumer devices and services. IEEE Consum

Electron Mag 6:48–56

Deep learning modelling techniques: current progress,…1 313610

S. F. Ahmed et al.

Leng B, Zhang X, Yao M, Xiong Z (2015) A 3D model recognition mechanism based on deep Boltzmann

machines. Neurocomputing 151:593–602. https:// doi. org/ 10. 1016/j. neucom. 2014. 06. 084

Leung MKK, Xiong HY, Lee LJ, Frey BJ (2014) Deep learning of the tissue-regulated splicing code. Bioin-

formatics 30:i121–i129. https:// doi. org/ 10. 1093/ bioin forma tics/ btu277

Li Z, Huang H, Zhang Z, Shi G (2022) Manifold-based multi-deep belief network for feature extraction of

hyperspectral image. Remote Sens 14:1484

Li J, Xiong D, Tu Z, Zhu M, Zhang M, Zhou G (2017a) Modeling source syntax for neural machine transla-
tion. In: ACL 2017a - 55th annual meeting of the association for computational linguistics, proceed-
ings of the conference (Long Papers). https:// doi. org/ 10. 18653/ v1/ P17- 1064

Li  Z,  Yang  Y,  Liu  X,  Zhou  F,  Wen  S,  Xu  W  (2017b)  Dynamic  computational  time  for  visual  attention.
In: Proceedings - 2017 IEEE international conference on computer vision workshops, ICCVW 2017.
https:// doi. org/ 10. 1109/ ICCVW. 2017. 145

Li JB, Schmidt FR, Kolter JZ (2019a) Adversarial camera stickers: a physical camera-based attack on deep

learning systems. In: International conference on machine learning. pp 3896–3904

Li P, Chen X, Shen S (2019b) Stereo R-CNN based 3D object detection for autonomous driving. In: Pro-
ceedings  of  the  IEEE  computer  society  conference  on  computer  vision  and  pattern  recognition.
https:// doi. org/ 10. 1109/ CVPR. 2019. 00783

Li Y, Qian M, Liu P, Cai Q, Li X, Guo J, Yan H, Yu F, Yuan K, Yu J, Qin L, Liu H, Wu W, Xiao P, Zhou Z
(2019c) The recognition of rice images by UAV based on capsule network. Cluster Comput. https://
doi. org/ 10. 1007/ s10586- 018- 2482-7

Li  Z,  Cai  X,  Liu  Y,  Zhu  B  (2019d)  A  Novel  Gaussian-Bernoulli  based  convolutional  deep  belief  net-
works  for  image  feature  extraction.  Neural  Process  Lett  49:305–319.  https:// doi. org/ 10. 1007/
s11063- 017- 9751-y

Liao S, Wang J, Yu R, Sato K, Cheng Z (2017) CNN for situations understanding based on sentiment analy-

sis of twitter data. Procedia Comput Sci. https:// doi. org/ 10. 1016/j. procs. 2017. 06. 037

Lim S, Kang J (2018) Chemical-gene relation extraction using recursive neural network. Database.https://

doi. org/ 10. 1093/ datab ase/ bay060

Lin Z, Feng M, Dos Santos CN, Yu M, Xiang B, Zhou B, Bengio Y (2017) A structured self-attentive sen-
tence embedding. In: 5th international conference on learning representations, ICLR 2017 - confer-
ence track proceedings

Lin CY (2004) Rouge: a package for automatic evaluation of summaries. Proc work text summ branches out

(WAS 2004)

Liou  CY,  Cheng  WC,  Liou  JW,  Liou  DR  (2014)  Autoencoder  for  words.  Neurocomputing  139:84–96.

https:// doi. org/ 10. 1016/j. neucom. 2013. 09. 055

Litjens G, Kooi T, Bejnordi BE, Arindra A, Setio A, Ciompi F, Ghafoorian M, Laak JAWMV, Der G, Van
B, Clara IS (2017) A survey on deep learning in medical image analysis. Med Image Anal 42:60–88.
https:// doi. org/ 10. 1016/j. media. 2017. 07. 005

Liu S, Wang Y, Yang X, Lei B, Liu L, Xiang S, Ni D, Wang T (2019) Deep learning in medical ultra-
sound analysis: a review. Engineering 5:261–275. https:// doi. org/ 10. 1016/j. eng. 2018. 11. 020
Liu  K,  Cheng  J,  Yi  J  (2022)  Copper  price  forecasted  by  hybrid  neural  network  with  Bayesian  optimi-
zation and wavelet transform. Resour Policy 75:102520. https:// doi. org/ 10. 1016/j. resou rpol. 2021.
102520

Liu P, Qiu X, Xuanjing H (2016) Recurrent neural network for text classification with multi-task learn-

ing. In: IJCAI international joint conference on artificial intelligence

Liu W, Luo W, Lian D, Gao S (2017) Future frame prediction for anomaly detection—a new baseline.
In: Proceedings of the IEEE conference on computer vision and pattern recognition 6536–6545
Lu  H,  Li  Y,  Chen  M,  Kim  H,  Serikawa  S  (2018)  Brain  intelligence:  go  beyond  artificial  intelligence.

Mobile Netw Appl 23:368–375

Lukoševičius M, Jaeger H (2009) Reservoir computing approaches to recurrent neural network training.

Comput Sci Rev 3(3):127–49. https:// doi. org/ 10. 1016/j. cosrev. 2009. 03. 005

Ma J, Sheridan RP, Liaw A, Dahl GE, Svetnik V (2015) Deep neural nets as a method for quantitative struc-
ture—activity relationships. J Chem Inf Model 55:263–274. https:// doi. org/ 10. 1021/ ci500 747n
Ma  J,  Gao  W,  Wong  KF  (2018)  Rumor  detection  on  twitter  with  tree-structured  recursive  neural  net-
works. In: ACL 2018 - 56th annual meeting of the association for computational linguistics, pro-
ceedings of the conference (Long Papers). https:// doi. org/ 10. 18653/ v1/ p18- 1184

Majumder N, Poria S, Hazarika D, Mihalcea R, Gelbukh A, Cambria, E (2019) DialogueRNN: an atten-
tive  RNN  for  emotion  detection  in  conversations.  In:  33rd  AAAI  Conference  on  artificial  intel-
ligence, AAAI 2019, 31st innovative applications of artificial intelligence conference, IAAI 2019
and the 9th AAAI symposium on educational advances in artificial intelligence, EAAI 2019https://
doi. org/ 10. 1609/ aaai. v33i01. 33016 818

1 3
13611

Mendis GJ, Randeny T, Wei, J, Madanayake A (2016) Deep learning based doppler radar for micro VAS
detection and classification Gihan J. Mendis. In: MILCOM 2016–2016 IEEE military communica-
tions conference pp 924–929

Mesnil G, Dauphin Y, Yao K, Bengio Y, Deng L, Hakkani-tur D, He X (2015) Using recurrent neural
networks for slot filling in spoken language understanding. IEEE/ACM trans audio, speech Lang
Process 23:530–539

Micheli A, Sperduti A, Starita A (2007) An introduction to recursive neural networks and kernel meth-
ods for cheminformatics. Curr Pharm Des 13(14):1469–1496. https:// doi. org/ 10. 2174/ 13816 12077
80765 981

Mikolov T, Karafiát M, Burget L, Jan C, Khudanpur, S (2010) Recurrent neural network based language
model. In: Proceedings of the 11th annual conference of the international speech communication
association, INTERSPEECH 2010

Mikolov T, Kombrink S, Burget L, Černocký J, Khudanpur S (2011) Extensions of recurrent neural net-
work language model In: ICASSP, IEEE international conference on acoustics, speech and signal
processing - proceedings. https:// doi. org/ 10. 1109/ ICASSP. 2011. 59476 11

Mikolov  T,  Chen  K,  Corrado  G  Dean  J  (2013)  Efficient  estimation  of  word  representations  in  vector
space.  In:  1st  international  conference  on  learning  representations,  ICLR  2013  -  workshop  track
proceedings

Miotto R, Wang F, Wang S, Jiang X, Dudley JT (2018) Deep learning for healthcare: review, opportuni-

ties and challenges. Brief Bioinform 19:1236–1246. https:// doi. org/ 10. 1093/ bib/ bbx044

Misra  D  (2019)  Mish:  a  self  regularized  non-monotonic  neural  activation  function.  https:// arXiv. org/

1908. 08681

Mitra  B,  Craswell  N  (2017)  Neural  text  embeddings  for  information  retrieval  (WSDM  2017  tutorial)
In: WSDM 2017 - Proceedings of the 10th ACM international conference on web search and data
mining https:// doi. org/ 10. 1145/ 30186 61. 30227 55

Miyato  T,  Kataoka  T,  Koyama  M,  Yoshida  Y  (2018)  Spectral  normalization  for  generative  adversarial
networks.  In:  6th  international  conference  on  learning  representations,  ICLR  2018  -  conference
track proceedings

Mobiny A, Van Nguyen H 2018 Fast CapsNet for lung cancer screening. In: Lecture notes in computer
science  (including  subseries  lecture  notes  in  artificial  intelligence  and  lecture  notes  in  bioinfor-
matics). https:// doi. org/ 10. 1007/ 978-3- 030- 00934-2_ 82

Mohd  M,  Jan  R,  Shah  M  (2020)  Text  document  summarization  using  word  embedding.  Expert  Syst

Appl. https:// doi. org/ 10. 1016/j. eswa. 2019. 112958

Mousavi  M,  Gandomi  AH  (2021)  Deep  learning  for  structural  health  monitoring  under  environmental
and operational variations. In: Nondestructive characterization and monitoring of advanced mate-
rials,  aerospace,  civil  infrastructure,  and  transportation  XV.  International  society  for  optics  and
photonics p 115920H

Mühlhoff R (2020) Human-aided artificial intelligence: or, how to run large computations in human brains?
Toward  a  media  sociology  of  machine  learning.  New  Media  Soc  22:1868–1884.  https:// doi. org/ 10.
1177/ 14614 44819 885334

Mukherjee S, Zimmer A, Sun X, Ghuman P, Cheng I (2020) An unsupervised generative neural approach

for InSAR phase filtering and coherence estimation. IEEE Geosci Remote Sens Lett 18:1971–1975

Murali S, Swapna TR (2019) An empirical evaluation of temporal convolutional network for offensive text

classification. Int J Innov Technol Explor Eng 8(8)

Naylor  CD  (2018)  On  the  prospects  for  a  (deep)  learning  health  care  system.  J  Am  Med  Assoc

320:1099–1100

Ng A (2015) What data scientists should know about deep learning. www. slide share. net/ Extra ctCon f44
Ngiam  J,  Chen  Z,  Wei  Koh  P,  Ng  AY  (2011)  Learning  deep  energy  models.  In:  Proceedings  of  the  28th

international conference on machine learning (ICML-11)  pp 1105–1112

Nguyen A, Yosinski J, Clune J (2015) Deep neural networks are easily fooled: high confidence predictions
for unrecognizable images. In: Proceedings of the IEEE conference on computer vision and pattern
recognition pp 427–436

Nguyen-Thanh VM, Zhuang X, Rabczuk T (2020) A deep energy method for finite deformation hyperelas-

ticity. Eur J Mech 80:103874. https:// doi. org/ 10. 1016/j. eurom echsol. 2019. 103874

Niklaus S, Mai L, Liu F (2017) Video frame interpolation via adaptive separable convolution. In: Proceed-
ings of the IEEE international conference on computer vision. https:// doi. org/ 10. 1109/ ICCV. 2017. 37

Norton AP, Qi Y (2017) Adversarial-playground: a visualization suite showing how adversarial examples

fool deep learning. In: 2017 IEEE symposium on visualization for cyber security (VizSec) pp 1–14

Nwankpa  CE,  Ijomah  W,  Gachagan  A,  Marshall  S  (2018)  Activation  functions:  comparison  of  trends  in

practice and research for deep learning.   https:// arXiv. org/ 1811. 03378

Deep learning modelling techniques: current progress,…1 313612

S. F. Ahmed et al.

Odena A, Olah C, Shlens J (2017) Conditional image synthesis with auxiliary classifier gans. In: 34th Inter-

national conference on machine learning, ICML 2017

Oka A, Ishimura N, Ishihara S (2021) A new dawn for the use of artificial intelligence in gastroenterology.

Hepatol Pancreatol Diagn 11:1719

Oord  VD,  Dieleman  S,  Schrauwen  B  (2013)  Deep  content-based  music  recommendation.  Neural  Inform

Process Syst 26:1–9

Orkphol K, Yang W (2019) Word sense disambiguation using cosine similarity collaborates with Word2vec

and WordNet. Futur Internet 11:114

Ortiz  A,  Munilla  J,  Gorriz  JM,  Ramirez  J  (2016)  Ensembles  of  deep  learning  architectures  for  the  early
diagnosis of the Alzheimer’s disease. Int J Neural Syst 26:1–23. https:// doi. org/ 10. 1142/ S0129 06571
65002 58

Palanichamy K (2019) Integrative omic analysis of neuroblastoma. Computational epigenetics and diseases.

Elsevier, Amsterdam, pp 311–326

Pandey  K,  Shekhawat  HS,  Prasanna,  SRM  (2019)  Deep  learning  techniques  for  speech  emotion  recogni-

tion : a review. 2019 29th international conference radioelektronika pp 1–6

Papernot N, Mcdaniel P, Jha S, Fredrikson M, Celik ZB, Swami A (2016) The limitations of deep learning
in adversarial settings. In: 2016 IEEE European symposium on security and privacy (EuroS and P) pp
372–387

Papineni K, Roukos S, Ward T, Zhu W-J (2001) BLEU: a method for automatic evaluation of machine trans-

lation. Assoc Comput Linguist. https:// doi. org/ 10. 3115/ 10730 83107 3135

Parikh AP, Täckström O, Das, D, Uszkoreit J (2016) A decomposable attention model for natural language
inference. In: EMNLP 2016 - conference on empirical methods in natural language processing, pro-
ceedings. https:// doi. org/ 10. 18653/ v1/ d16- 1244

Park T, Liu MY, Wang TC, Zhu JY (2019) Semantic image synthesis with spatially-adaptive normalization.
In: Proceedings of the IEEE computer society conference on computer vision and pattern recognition.
https:// doi. org/ 10. 1109/ CVPR. 2019. 00244

Park  DC  (2010)  A  time  series  data  prediction  scheme  using  bilinear  recurrent  neural  network.  In:  2010
International  conference  on  information  science  and  applications,  ICISA  2010.  https:// doi. org/ 10.
1109/ ICISA. 2010. 54803 83

Parkhi OM, Vedaldi A, Zisserman A (2015) Deep face recognition. British machine vision association
Pashaei M, Kamangir H (2020) Review and evaluation of deep learning architectures for efficient land cover
mapping with uas hyper-spatial imagery: a case study over a wetland. Remote Sens 12:959. https://
doi. org/ 10. 3390/ rs120 60959

Paula  EL,  Ladeira  M,  Carvalho  RN,  Marzag  T  (2016)  Deep  learning  anomaly  detection  as  support  fraud
investigation in Brazilian exports and anti-money laundering. In: 2016 15th IEEE International con-
ference on machine learning and applications (ICMLA) pp 954–960. https:// doi. org/ 10. 1109/ ICMLA.
2016. 73

Paulus R, Xiong C, Socher R (2018) A deep reinforced model for abstractive summarization. In: 6th inter-

national conference on learning representations, ICLR 2018 - conference track proceedings

Perozzi B, Al-Rfou R, Skiena S (2014) DeepWalk: online learning of social representations. In: Proceedings
of the ACM SIGKDD international conference on knowledge discovery and data mining. https:// doi.
org/ 10. 1145/ 26233 30. 26237 32

Perraudin  N,  Defferrard  M,  Kacprzak  T,  Sgier  R  (2019)  DeepSphere:  efficient  spherical  convolutional
neural network with HEALPix sampling for cosmological applications. Astron Comput 27:130–46.
https:// doi. org/ 10. 1016/j. ascom. 2019. 03. 004

Pfau D (2017) Unrolled GAN 1–25
Poliak A, Belinkov Y, Glass J, Van Durme B (2018) On the evaluation of semantic phenomena in neural
machine translation using natural language inference. In: NAACL HLT 2018 - 2018 conference of the
North American chapter of the association for computational linguistics: human language technolo-
gies - proceedings of the conference. https:// doi. org/ 10. 18653/ v1/ n18- 2082

Popperli M, Gulagundi R, Yogamani S, Milz S (2019) Capsule neural network based height classification
using low-cost automotive ultrasonic sensors. In: IEEE intelligent vehicles symposium, proceedings.
https:// doi. org/ 10. 1109/ IVS. 2019. 88138 79

Pouyanfar S, Saad S., Yilin Y, Haiman T, Tao Y, Reyes MP, Shyu M, Chen S-C, Iyengar SS (2018) A sur-
vey on deep learning: algorithms, techniques, and applications. ACM Comput Surv 51(5):1–36
Qasim Abualigah LM, Hanandeh ES (2015) Applying genetic algorithms to information retrieval using vec-

tor space model. Int J Comput Sci Eng Appl. https:// doi. org/ 10. 5121/ ijcsea. 2015. 5102

Qiu  X,  Huang  X  (2015)  Convolutional  neural  tensor  network  architecture  for  community-based  question

answering. In: IJCAI International joint conference on artificial intelligence

1 3
13613

Rao G, Huang W, Feng Z, Cong Q (2018a) LSTM with sentence representations for document-level senti-
ment classification. Neurocomputing 308:49–57. https:// doi. org/ 10. 1016/j. neucom. 2018. 04. 045
Rao  K,  Sak  H,  Prabhavalkar  R  (2018b)  Exploring  architectures,  data  and  units  for  streaming  end-to-end
speech  recognition  with  RNN-transducer.  In:  2017  IEEE  automatic  speech  recognition  and  under-
standing workshop, ASRU 2017 - proceedings. https:// doi. org/ 10. 1109/ ASRU. 2017. 82689 35
Ravì D, Wong C, Deligianni F, Berthelot M, Andreu-perez J, Lo B (2017) Deep learning for health infor-

matics. IEEE J Biomed Heal Inform 21:4–21

Rengasamy D, Figueredo GP, Advanced T, Analysis D (2018) Deep learning approaches to aircraft mainte-
nance, repair and overhaul: a review. In: 2018 21st International conference on intelligent transporta-
tion systems (ITSC) pp 150–153

Roberto J, Solares A, Elisa F, Raimondi D, Zhu Y, Rahimian F, Canoy D, Tran J, Catarina A, Gomes P, Pay-
berah AH, Zottoli M, Nazarzadeh M, Conrad N (2020) Deep learning for electronic health records: a
comparative review of multiple deep neural architectures. J Biomed Inform 101:103337. https:// doi.
org/ 10. 1016/j. jbi. 2019. 103337

Russakovsky O, Deng J, Su H, Krause J, Satheesh S, Ma S, Huang Z, Karpathy A, Khosla A, Bernstein M,
Berg AC, Fei-Fei L (2015) ImageNet large scale visual recognition challenge. Int J Comput Vis 115:
211–252. https:// doi. org/ 10. 1007/ s11263- 015- 0816-y

Sabour S, Frosst N, Hinton GE (2017) Dynamic routing between capsules. Adv Neural Inform Processing

Syst. https:// doi. org/ 10. 48550/ arXiv. 1710. 09829

Sahoo BB, Jha R, Singh A, Kumar D (2019) Long short-term memory (LSTM) recurrent neural network
for low-flow hydrological time series forecasting. Acta Geophys 67(5):1471–1481. https:// doi. org/ 10.
1007/ s11600- 019- 00330-1

Sainath  TN,  Mohamed  A,  Kingsbury,  B,  Ramabhadran  B,  Watson  IBMTJ,  Heights  Y  (2013)  Deep  con-
volutional neural networks for LVCSR. In: Proceedings  acoustics, speech and signal processing pp
8614–8618

Samaniego  E,  Anitescu  C,  Goswami  S,  Nguyen-Thanh  VM,  Guo  H,  Hamdia  K,  Zhuang  X,  Rabczuk  T
(2020) An energy approach to the solution of partial differential equations in computational mechan-
ics via machine learning: concepts, implementation and applications. Comput Methods Appl Mech
Eng 362:112790

Saremi  S,  Mehrjou  A,  Schölkopf  B,  Hyvärinen  A  (2018)  Deep  energy  estimator  networks.  https:// arXiv.

1805. 08306

Scellier B, Bengio Y (2017) Equilibrium propagation: bridging the gap between energy-based models and

backpropagation. Front Comput Neurosci 11:24. https:// doi. org/ 10. 3389/ fncom. 2017. 00024

Schmidhuber J (2015) Deep learning in neural networks: an overview. Neural Netw 61:85–117. https:// doi.

org/ 10. 1016/j. neunet. 2014. 09. 003

Schmidt U (2014) Shrinkage fields for effective image restoration. In: Proceedings of the IEEE conference

on computer vision and pattern recognition https:// doi. org/ 10. 1109/ CVPR. 2014. 349

Sengupta  S,  Basak  S,  Saikia  P,  Paul  S,  Tsalavoutis  V,  Atiah  FD,  Ravi  V,  Alan  R,  Ii  P  (2020)  A  review
of deep learning with special emphasis on architectures applications and recent trends. Knowledge-
Based Syst 194:105596

Seo S, Kim C, Kim H, Mo K, Kang P (2020) Comparative study of deep learning-based sentiment classifi-

cation. IEEE Access 8:6861–6875. https:// doi. org/ 10. 1109/ ACCESS. 2019. 29634 26

Shakya SR, Zhang C, Zhou Z (2018) Comparative study of machine learning and deep learning architecture
for  human  activity  recognition  using  accelerometer  data.  Int  J  Mach  Learn  Comput  8(6):577–582.
https:// doi. org/ 10. 18178/ ijmlc. 2018.8. 6. 748

Shen Y, He X, Gao J, Deng L, Mesnil G (2014) A latent semantic model with convolutional-pooling struc-
ture for information retrieval. In: Proceedings of the 23rd ACM international conference on confer-
ence on information and knowledge management. pp 101–110

Shi  T,  Kang  K,  Choo  J,  Reddy  CK  (2018)  Short-text  topic  modeling  via  non-negative  matrix  factoriza-
tion enriched with local word-context correlations. In: The web conference 2018 - proceedings of the
world wide web conference, WWW 2018. https:// doi. org/ 10. 1145/ 31788 76. 31860 09

Shoeibi  A,  Ghassemi  N,  Khodatars  M,  Jafari  M,  Hussain  S,  Alizadehsani  R  (2020)  Application  of  deep
learning techniques for automated detection of epileptic seizures: a Review.  https:// arXiv. org/ 2007.
01276

Shrestha  A  (2019)  Review  of  deep  learning  algorithms  and  architectures.  IEEE  Access  7:53040–53065.

https:// doi. org/ 10. 1109/ ACCESS. 2019. 29122 00

Si Y, Wang J, Xu H, Roberts K (2019) Enhancing clinical concept extraction with contextual embeddings. J

Am Med Informatics Assoc. https:// doi. org/ 10. 1093/ jamia/ ocz096

Deep learning modelling techniques: current progress,…1 313614

S. F. Ahmed et al.

Siami-Namini S, Tavakoli N, Namin AS (2019) The performance of LSTM and BiLSTM in forecasting time
series. In: Proceedings - 2019 IEEE International conference on big data, big data. https:// doi. org/ 10.
1109/ BigDa ta470 90. 2019. 90059 97

Siegelmann HT (1995) Computation beyond the turing limit. Science 80:268. https:// doi. org/ 10. 1126/ scien

ce. 268. 5210. 545

Signorelli CM (2018) Can computers become conscious and overcome humans? Front Robot AI 5:121
Socher R, Chen D, Manning CD, Ng AY (2013) Reasoning with neural tensor networks for knowledge base

completion. Adv Neural Inf Proc Syst 1:e2

Sønderby  CK,  Caballero  J,  Theis  L,  Shi  W,  Huszár  F  (2017)  Amortised  map  inference  for  image  super-
resolution. In: 5th international conference on learning representations, ICLR 2017 - conference track
proceedings

Srivastava N, Salakhutdinov R (2014) Multimodal learning with deep Boltzmann machines. J Mach Learn

Res 15

Sugiyama S (2019) Human behavior and another kind in consciousness: emerging research and opportuni-

ties. IGI Global, Hershey

Sui J, Liu M, Lee J, Zhang J, Calhoun V (2020) Deep learning methods and applications in neuroimaging. J

Neurosci Methods 339:108718. https:// doi. org/ 10. 1016/j. jneum eth. 2020. 108718

Sun  P,  Hui  C,  Bai  N,  Yang  S,  Wan  L,  Zhang  Q,  Zhao  Y  (2015)  Revealing  the  characteristics  of  a  novel
bioflocculant and its flocculation performance in Microcystis aeruginosa removal. Sci Rep 5:17465.
https:// doi. org/ 10. 1038/ srep1 7465

Sun X, Nasrabadi NM, Tran TD (2017) Supervised deep sparse coding networks.  https:// arXiv. org/ 1701.

08349

Sun B, Feng J, Saenko K (2016) Return of frustratingly easy domain adaptation. In: 30th AAAI conference

on artificial intelligence, AAAI 2016

Sutskever I, Hinton G, Taylor G (2009) The recurrent temporal restricted boltzmann machine. In: Advances

in neural information processing systems 21 - proceedings of the 2008 conference

Sutskever I, Vinyals O, Le QV (2014) Sequence to sequence learning with neural networks. In: Advances in

neural information processing systems

Sutskever  I,  Hinton  G  (2007)  Learning  multilevel  distributed  representations  for  high-dimensional

sequences. J Machine Learn Res. 2:548–555

Szegedy C, Liu W, Jia Y, Sermanet P, Reed S, Anguelov D, Erhan D, Vanhoucke V, Rabinovich A (2015)
Going deeper with convolutions. In: Proceedings of the IEEE conference on computer vision and pat-
tern recognition. pp 1–9

Taherkhani A, Cosma G, McGinnity TM (2018) Deep-FS: a feature selection algorithm for deep Boltz-
mann machines. Neurocomputing 322:22–37. https:// doi. org/ 10. 1016/j. neucom. 2018. 09. 040
Tahmassebi  A,  Gandomi  AH,  Fong  S,  Meyer-Baese  A,  Foo  SY  (2018a)  Multi-stage  optimization  of  a

deep model: a case study on ground motion modeling. PLoS ONE 13:e0203829

Tahmassebi  A,  Gandomi  AH,  McCann  I,  Schulte  MHJ,  Goudriaan  AE,  Meyer-Baese  A  (2018b)  Deep
learning  in  medical  imaging:  Fmri  big  data  analysis  via  convolutional  neural  networks.  In:  Pro-
ceedings of the practice and experience on advanced research computing. pp 1–4

Tahmassebi A, Ehtemami A, Mohebali B, Gandomi AH, Pinker K, Meyer-Baese A (2019) Big data ana-
lytics in medical imaging using deep learning. In: Big data: learning, analytics, and applications.
international society for optics and photonics, p 109890E

Tahmassebi  A,  Martin  J,  Meyer-Baese  A,  Gandomi  AH  (2020)  An  interpretable  deep  learning  frame-
work  for  health  monitoring  systems:  a  case  study  of  eye  state  detection  using  EEG  Signals.  In:
2020 IEEE symposium series on computational intelligence (SSCI). IEEE pp 211–218

Taigman Y, Polyak A, Wolf L (2017) Unsupervised cross-domain image generation. In: 5th international

conference on learning representations, ICLR 2017 - conference track proceedings

Tandiya N, Jauhar A, Marojevic V, Reed JH (2018) Deep predictive coding neural network for rf anom-
aly  detection  in  wireless  networks.  arXiv:2018.8403654.  https:// doi. org/ 10. 1109/ ICCW. 2018.
84036 54

Tang Y (2013) Deep learning using linear support vector machines. https:// arXiv. org/ 1306. 0239
Tang Z, Yang J, Pei Z, Song X, Ge B (2019) Multi-process training gan for identity-preserving face syn-

thesis. IEEE Access 7:97641–97652. https:// doi. org/ 10. 1109/ ACCESS. 2019. 29302 03

Tavarone  Raffaele,      Badino  L  (2018)  Conditional-computation-based  recurrent  neural  networks  for

computationally efficient acoustic modelling. Interspeech, pp 1274–1278

Telikani  A,  Gandomi  AH,  Choo  K-KR,  Shen  J  (2021)  A  cost-sensitive  deep  learning  based  approach
for network traffic classification. IEEE Trans Netw Serv Manag 19(1):661–670. https:// doi. org/ 10.
1109/ TNSM. 2021. 31122 83

1 3
13615

Tkachenko Y (2015) Autonomous CRM control via CLV approximation with deep reinforcement learn-
ing in discrete and continuous action space.  arXiv:1504.01840. https:// arXiv. org/ 1504. 01840
Tompson J, Jain A, Lecun Y, Bregler C (2014) Joint training of a convolutional network and a graphical

model for human pose estimation. 27:1–9 https:// arXiv. org/ 1406. 2984

Trabelsi  C,  Bilaniuk  O,  Zhang  Y,  Serdyuk  D,  Subramanian  S,  Santos  JF,  Mehri  S,  Rostamzadeh  N,
Bengio,  Y,  Pal  CJ  (2018)  Deep  complex  networks.  In:  6th  international  conference  on  learning
representations, ICLR 2018 - conference track proceedings

Tran  SN,  Garcez  ADA,  Weyde  T,  Yin  J,  Zhang  Q,  Karunanithi  M  (2020)  Sequence  classifica-
tion  restricted  boltzmann  machines  with  gated  units.  IEEE  Trans  Neural  Networks  Learn  Syst
31:4806–4815. https:// doi. org/ 10. 1109/ TNNLS. 2019. 29581 03

Tzafestas SG (2014) Mobile robot control IV: fuzzy and neural methods. In: Tzafestas SG (ed) Introduc-

tion to mobile robot control. Elsevier, Oxford, pp 269–317

Uddin MZ, Hassan MM, Alsanad A, Savaglio C (2020) A body sensor data fusion and deep recurrent
neural network-based behavior recognition approach for robust healthcare. Inf Fusion 55:105–115.
https:// doi. org/ 10. 1016/j. inffus. 2019. 08. 004

Van  Gysel  C,  De  Rijke  M,  Kanoulas  E  (2018)  Neural  vector  spaces  for  unsupervised  information

retrieval. ACM Trans Inf Syst 36(4):1–25. https:// doi. org/ 10. 1145/ 31968 26
Vargas R, Mosavi A, Ruiz R (2017) Deep learning: a review. Adv Intell Syst Comput
Vaswani A (2017) Attention is all you need . Adv Neural Inf Process Syst 2017 pp 5999–6009 arXiv:

1706. 03762 v5

Vazhayil A, Vinayakumar R, Soman K (2018) Comparative study of the detection of malicious URLs using
shallow and deep networks. In: 2018 9th international conference on computing, communication and
networking technologies, ICCCNT 2018. https:// doi. org/ 10. 1109/ ICCCNT. 2018. 84941 59

Vincent  P  (2011)  A  connection  between  scorematching  and  denoising  autoencoders.  Neural  Comput

23:1661–1674. https:// doi. org/ 10. 1162/ NECO_a_ 00142

Wang J Yu LC, Lai KR, Zhang X (2016a) Dimensional sentiment analysis using a regional CNN-LSTM
model. In: 54th Annual meeting of the association for computational linguistics, ACL 2016 - Short
Papers. https:// doi. org/ 10. 18653/ v1/ p16- 2037

Wang J, Wang J, Fang W, Niu H (2016b) Financial time series prediction using elman recurrent random

neural networks. Comput Intell Neurosci. https:// doi. org/ 10. 1155/ 2016/ 47425 15

Wang X, Jiang, W, Luo Z (2016c) Combination of convolutional and recurrent neural network for sentiment
analysis of short texts. In: COLING 2016 - 26th international conference on computational linguis-
tics, proceedings of COLING 2016: technical papers

Wang D, Liang Y, Xu D (2019) Capsule network for protein post-translational modification site predic-

tion. Bioinformatics 35(14):2386–2394. https:// doi. org/ 10. 1093/ bioin forma tics/ bty977

Wei Q, Kasabov N, Polycarpou M, Zeng Z (2019) Deep learning neural networks: methods, systems, and

applications. Neurocomputing 396:130–132. https:// doi. org/ 10. 1016/j. neucom. 2019. 03. 073

Wieslander H, Forslid G, Bengtsson E, Wahlby C, Hirsch J-M, Stark CR, Sadanandan SK (2017) Deep con-
volutional neural networks for detecting cellular changes due to malignancy. In: Proceedings of the
IEEE international conference on computer vision workshops pp 82–89

Wu  Y,  Guo  Y  (2020)  Dual  adversarial  co-learning  for  multi-domain  text  classification.  In:  AAAI  2020  -
34th  AAAI  Conference  artificial  intelligence,  pp  6438–6445.  https:// doi. org/ 10. 1609/ aaai. v34i04.
6115

Wu H, Soraghan J, Lowit A, Di Caterina G (2018) A deep learning method for pathological voice detection using
convolutional  deep  belief  network.  In:  Proceedings  of  the  annual  conference  of  the  international  speech
communication association, INTERSPEECH. https:// doi. org/ 10. 21437/ Inter speech. 2018- 1351

Xiang C, Zhang L, Tang Y, Zou W, Xu C (2018) MS-capsnet: a novel multi-scale capsule network. IEEE

Signal Process Lett 25:1850–1854. https:// doi. org/ 10. 1109/ LSP. 2018. 28738 92

Xiao  C,  Choi  E,  Sun  J  (2018)  Review  Opportunities  and  challenges  in  developing  deep  learning  models
using  electronic  health  records  data:  a  systematic  review.  J  Am  Med  Informatics  Assoc  25:1419–
1428. https:// doi. org/ 10. 1093/ jamia/ ocy068

Xiong HY, Alipanahi B, Lee LJ, Bretschneider H, Yuen RKC, Hua Y, Gueroussov S, Hamed S, Hughes TR,
Morris Q, Barash Y, Adrian R, Jojic N, Scherer SW, Blencowe BJ (2015) The human splicing code
reveals new insights into the genetic determinants of disease. Science 347(6218):1254806. https:// doi.
org/ 10. 1126/ scien ce. 12548 06

Xu M (2020) Understanding graph embedding methods and their applications. SIAM Rev 63(4):825–853.

https:// doi. org/ 10. 1137/ 20M13 86062

Xu T, Zhang P, Huang Q, Zhang H, Gan Z, Huang X, He X (2018) AttnGAN: fine-grained text to image genera-
tion with attentional generative adversarial networks. In: Proceedings of the IEEE computer society confer-
ence on computer vision and pattern recognition. https:// doi. org/ 10. 1109/ CVPR. 2018. 00143

Deep learning modelling techniques: current progress,…1 313616

S. F. Ahmed et al.

Yan WY, Shaker A, El-Ashmawy N (2015) Urban land cover classification using airborne LiDAR data: a

review. Remote Sens Environ. 158:295–310. https:// doi. org/ 10. 1016/j. rse. 2014. 11. 001

Yan Y, Guo Y (2020) Multi-level generative models for partial label learning with non-random label noise.

https:// doi. org/ 10. 24963/ ijcai. 2021/ 449

Yang Z, Yu W, Liang P, Guo H, Xia L, Zhang F, Ma Y, Ma J (2019) Deep transfer learning for military
object recognition under small training set condition. Neural Comput Appl 31:6469–6478. https:// doi.
org/ 10. 1007/ s00521- 018- 3468-3

Yang B, Yih W tau, He X, Gao J, Deng L (2015) Embedding entities and relations for learning and infer-
ence  in  knowledge  bases.  In:  3rd  international  conference  on  learning  representations,  ICLR  2015
- conference track proceedings

Yang  D,  Qu  B,  Yang  J,  Cudre-Mauroux  P  (2019)  Revisiting  user  mobility  and  social  relationships  in
LBSNs: a hypergraph embedding approach. In: The web conference 2019 - proceedings of the world
wide web conference, WWW 2019. https:// doi. org/ 10. 1145/ 33085 58. 33136 35

Yao T, Pan Y, Li Y, Mei T (2017) Incorporating copying mechanism in image captioning for learning novel
objects. In: Proceedings - 30th IEEE conference on computer vision and pattern recognition, CVPR
2017. https:// doi. org/ 10. 1109/ CVPR. 2017. 559

Ye M, Peng X, Gan W, Wu W, Qiao Y (2019) AnoPCN: video anomaly detection via deep predictive coding
network.  In:    MM  2019  -  Proceedings  27th  ACM  international  conference  multimedia  1805–1813.
https:// doi. org/ 10. 1145/ 33430 31. 33508 99

Yu Y, Si X, Hu C, Zhang J (2019) A review of recurrent neural networks: LSTM cells and network architec-

tures. Neural Comput 31(7):1235–1270. https:// doi. org/ 10. 1162/ neco_a_ 01199

Zeiler MD, Fergus R (2014) Visualizing and understanding convolutional networks. European conference

on computer vision. Springer, Cham, pp 818–833

Zeng Z, Xiao S, Jia K, Chan TH, Gao S, Xu D, Ma Y (2013) Learning by associating ambiguously labeled
images.  In:  Proceedings  of  the  IEEE  computer  society  conference  on  computer  vision  and  pattern
recognition. https:// doi. org/ 10. 1109/ CVPR. 2013. 97

Zeroual A, Harrou F, Dairi A, Sun Y (2020) Deep learning methods for forecasting COVID-19 time-series data: a
comparative study. Chaos, Solitons Fractals 140:110121. https:// doi. org/ 10. 1016/j. chaos. 2020. 110121
Zhang  D,  Xu  H,  Su  Z,  Xu  Y  (2015)  Chinese  comments  sentiment  classification  based  on  word2vec  and

SVMperf. Expert Syst Appl 42(4):1857–1863. https:// doi. org/ 10. 1016/j. eswa. 2014. 09. 011

Zhang C, Bengio S, Hardt M, Recht B, Vinyals O (2016a) Understanding deep learning requires rethinking

generalization. Commun ACM 64:107–115. https:// doi. org/ 10. 1145/ 34467 76

Zhang L, Lin L, Liang X, He K (2016b) Is faster R-CNN doing well for pedestrian detection?. In: Lecture
notes in computer science (including subseries lecture notes in artificial intelligence and lecture notes
in bioinformatics). https:// doi. org/ 10. 1007/ 978-3- 319- 46475-6_ 28

Zhang B, Xiong D, Su J, Duan H (2017a) A context-aware recurrent encoder for neural machine translation. IEEE/
ACM Trans Audio Speech Lang Process 25(12):2424–2432. https:// doi. org/ 10. 1109/ TASLP. 2017. 27514 20
Zhang H, Xu T, Li H, Zhang S, Wang X, Huang X, Metaxas D (2017b) StackGAN: text to photo-realistic
image synthesis with stacked generative adversarial networks. In: Proceedings of the IEEE interna-
tional conference on computer vision. https:// doi. org/ 10. 1109/ ICCV. 2017. 629

Zhang S, Wang J, Tao X, Gong Y, Zheng N (2017c) Constructing deep sparse coding network for image

classification. Pattern Recognit 64:130–140. https:// doi. org/ 10. 1016/j. patcog. 2016. 10. 032

Zhang S, Yao L, Sun A, Tay Y (2019) Deep learning based recommender system: a survey and new per-

spectives. ACM Comput Surv 52(1):1–38. https:// doi. org/ 10. 1145/ 32850 29

Zhang J, Lei YK, Zhang Z, Chang J, Li M, Han X, Yang L, Yang YI, Gao YQ (2020) A perspective on deep
learning for molecular modeling and simulations. J Phys Chem A 124(34):6745–6763. https:// doi. org/
10. 1021/ acs. jpca. 0c044 73

Zhao  Y,  Liu  Z,  Sun  M  (2015)  Phrase  type  sensitive  tensor  indexing  model  for  semantic  composition.  In:

Proceedings of the national conference on artificial intelligence

Zhao  Z,  Jiao  L,  Zhao  J,  Gu  J,  Zhao  J  (2017)  Discriminant  deep  belief  network  for  high-resolution  SAR
image classification. Pattern Recognit 61:686–701. https:// doi. org/ 10. 1016/j. patcog. 2016. 05. 028
Zhao H, Chen Z, Jiang H, Jing W, Sun L, Feng M (2019) Evaluation of three deep learning models for early
crop classification using Sentinel-1A imagery time series-a case study in Zhanjiang. China Remote
Sens 11(22):2673. https:// doi. org/ 10. 3390/ rs112 22673

Zhong Z, Li J, Luo Z, Chapman M (2018) Spectral-spatial residual network for hyperspectral image classifi-
cation: a 3-D deep learning framework. IEEE Trans Geosci Remote Sens 56(2):847–858. https:// doi.
org/ 10. 1109/ TGRS. 2017. 27555 42

Zhou G, Xie Z, He T, Zhao J, Hu XT (2016) Learning the multilingual translation representations for ques-
tion  retrieval  in  community  question  answering  via  non-negative  matrix  factorization.  IEEE/ACM
Trans Audio Speech Lang Process 5:5–6. https:// doi. org/ 10. 1109/ TASLP. 2016. 25446 61

1 3
13617

Zhu S, Mumford D (2006) A stochastic grammar of images a stochastic grammar of images. Found Trends

Comput Graph Vis 2(4):2. https:// doi. org/ 10. 1561/ 06000 00018

Zhu Z, Peng G, Chen Y, Gao H (2019) A convolutional neural network based on a capsule network with
strong  generalization  for  bearing  fault  diagnosis.  Neurocomputing  323:62–75.  https:// doi. org/ 10.
1016/j. neucom. 2018. 09. 050

Ziebart BD, Fox D (2010) Modeling purposeful adaptive behavior with the principle of maximum causal

entropy. Carnegie Mellon University

Zulqarnain M, Ghazali R, Mazwin Y, Hassim M, Rehan M (2020) A comparative review on deep learning
models for text classification. Indones J Electr Eng Comput Sci 19:325–335. https:// doi. org/ 10. 11591/
ijeecs. v19. i1. pp325- 335

Publisher’s Note  Springer Nature remains neutral with regard to jurisdictional claims in published maps and
institutional affiliations.

Authors and Affiliations

Shams Forruque Ahmed1 · Md. Sakib Bin Alam2 · Maruf Hassan1 ·
Mahtabin Rodela Rozbu3 · Taoseef Ishtiak4 · Nazifa Rafa5 · M. Mofijur6,7 ·
A. B. M. Shawkat Ali8,9 · Amir H. Gandomi10,11

1
Science and Math Program, Asian University for Women, Chattogram 4000, Bangladesh
2  Data Science and Artificial Intelligence, Asian Institute of Technology, Chang Wat 12120,

Pathum Thani, Thailand

3  Department of Computational Biology, Carnegie Mellon University, Pittsburgh, PA 15213, USA
4
5  Department of Geography, University of Cambridge, Downing Place, Cambridge CB2 3EN,

School of Computer Science, Carleton University, Ottawa, ON K1S 5B6, Canada

United Kingdom

6  Centre for Technology in Water and Wastewater, School of Civil and Environmental Engineering,

University of Technology Sydney, Ultimo, NSW 2007, Australia

7  Mechanical Engineering Department, Prince Mohammad Bin Fahd University, Al Khobar 31952,

Saudi Arabia

8

School of Engineering and Technology, Central Queensland University, Melbourne, VIC 300,
Australia

School of Science and Technology, The University of Fiji, Lautoka, Fiji

9
10  Faculty of Engineering and Information Technology, University of Technology Sydney, Sydney,

NSW 2007, Australia

11  University Research and Innovation Center (EKIK), Óbuda University, 1034 Budapest, Hungary

Deep learning modelling techniques: current progress,…1 3