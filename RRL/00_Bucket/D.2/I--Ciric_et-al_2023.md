Article
Single and Multiple Separate LSTM Neural Networks for
Multiple Output Feature Purchase Prediction

Milica ´Ciri´c 1,*

, Bratislav Predi´c 2

, Dragan Stojanovi´c 2 and Ivan ´Ciri´c 3,*

1

2

Faculty of Civil Engineering and Architecture, University of Niš, Aleksandra Medvedeva 14, 18000 Niš, Serbia
Faculty of Electronic Engineering, University of Niš, Aleksandra Medvedeva 12, 18000 Niš, Serbia;
bratislav.predic@elfak.ni.ac.rs (B.P.); dragan.stojanovic@elfak.ni.ac.rs (D.S.)
Faculty of Mechanical Engineering, University of Niš, Aleksandra Medvedeva 14, 18000 Niš, Serbia

3
* Correspondence: milica.ciric@gaf.ni.ac.rs (M. ´C.); ivan.ciric@masfak.ni.ac.rs (I. ´C.)

Abstract: Data concerning product sales are a popular topic in time series forecasting due to their
multidimensionality and wide presence in many businesses. This paper describes the research
in predicting the timing and product category of the next purchase based on historical customer
transaction data. Given that the dataset was acquired from a vendor of medical drugs and devices,
the generic product identiﬁer (GPI) classiﬁcation system was incorporated in assigning product
categories. The models built are based on recurrent neural networks (RNN) and long short-term
memory (LSTM) neural networks with different input and output features, and training datasets.
Experiments with various datasets were conducted and optimal network structures and types for
predicting both product category and next purchase day were identiﬁed. The key contribution of this
research is the process of data transformation from its original purchase transaction format into a time
series of input features for next purchase prediction. With this approach, it is possible to implement a
dedicated personalized marketing system for a vendor.

Keywords: recurrent neural networks; purchase forecasting; time series prediction

Citation: ´Ciri´c, M.; Predi´c, B.;
Stojanovi´c, D.; ´Ciri´c, I. Single and

Multiple Separate LSTM Neural

Networks for Multiple Output

Feature Purchase Prediction.

Electronics 2023, 12, 2616. https://

doi.org/10.3390/electronics12122616

Academic Editor: Javid Taheri

Received: 6 May 2023

Revised: 4 June 2023

Accepted: 8 June 2023

Published: 10 June 2023

Copyright: © 2023 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under

the terms and

conditions of the Creative Commons

Attribution (CC BY) license (https://

creativecommons.org/licenses/by/

4.0/).

1. Introduction

The prediction of ﬁnancial data has been a challenging topic for a long time and was
addressed by many researchers. Among other things, researchers have tried to predict
the following: the future values of stock prices [1–3], foreign exchange rates [4], sale
volumes of one or multiple product categories [5–7], and the product category of the next
purchase [8,9]. The prediction of sales data is particularly interesting as a research topic due
to how widespread it is. Additionally, it has many dimensions that can be targeted when
predicting a future purchase: timing of the purchase, product category, quantity, or will
the customer even make another purchase. If the predictions have a reasonable reliability,
the businesses can use them in making decisions for inventory or production planning,
personalized marketing or determining prices. Such additional information can be used to
prevent business crisis or even increase proﬁt [10].

Sales data can be represented as a time series where past values are known and the
future values are what are being predicted. There are many methods used for this task,
and each has its beneﬁts and disadvantages while their performance varies based on
the application [11]. Recently, artiﬁcial neural networks have been used in time series
forecasting, often outperforming more “traditional” methods [12,13]. For ﬁnancial data
speciﬁcally, statistical models are not best suited due to their non-stationary nature. A type
of recurrent neural networks (RNNs), a long short-term memory neural network (LSTM),
has an advantage when working with time series that have long-term dependencies. This
is due to the vanishing gradient problem of RNNs that is solved in LSTM neural networks.
LSTMs were found to generally perform better than other methods with longer time
ranges [14].

Electronics 2023, 12, 2616. https://doi.org/10.3390/electronics12122616

https://www.mdpi.com/journal/electronics

electronicsElectronics 2023, 12, 2616

2 of 14

This research was started with the goal of predicting a customer’s next purchase based
on the information of previous purchases. The process was started by predicting the next
purchase day for each customer. Initial work was done with statistical methods [15,16],
which were then compared to neural networks [17] and ﬁnally additional features were
added to neural networks to achieve better results [18]. The next logical question was if it
is possible to predict the product category for the next purchase with adequate reliability.
Information about the predicted contents of the next purchase could be used in personalized
advertising and in creating customer-speciﬁc offers. The research presented in this paper
focuses on predicting product categories that will appear in the next purchase of a speciﬁc
customer. Additionally, the prediction of product categories and next purchase day output
features with different neural network setups are compared. The main takeaway is that
deciding what approach is best deﬁnitely depends on the output feature and it is best
to try different approaches before making a ﬁnal decision. The experiments performed
with multiple setups and datasets showed that a dedicated neural network produced
signiﬁcantly better results in predicting the product category, while for predicting the
timing of the next purchase, the single multivariate neural network was superior. The main
novelty and research contribution lies in data preprocessing and transformation applied to
the original data format in order to form the optimal input data structure for presented time
series prediction. Speciﬁcally, a hierarchical classiﬁcation system was used for deﬁning
product categories and creating a new type of input feature vector. This original input
feature vector affects both product category prediction and next purchase day prediction.
An additional advantage lies in the applicability and usability of the network output results
in various vendor commercial purposes. The rest of the paper is structured as follows.
Section 2 is an overview of the literature review in prediction in sales and other ﬁnancial
data. Section 3 provides the description of the used methodology, including the dataset.
Section 4 contains the results of conducted experiments, while the discussion of the results
is in Section 5. Finally, the conclusions are given in Section 6.

2. Literature Review

In [4], the authors use a combination of symbolic processing and recurrent neural
networks for foreign exchange rate prediction. They argue that the methods used are better
suited for high noise, highly non-stationarity time series prediction. In their experiments,
they achieved a 47.1% error rate in predicting the direction of changes and were able to
lower that rate to 40% by excluding examples for which the system had low prediction
conﬁdence.

The research presented in [5] focuses on comparing XGBoost-LSTM combination
forecasting model with classical time series prediction models for the purpose of forecasting
sales volume. Results for the combination model were much better than the original
XGBoost single model.

LSTM was the best performing model for customer product prediction in research try-
ing to predict which users will buy mobile devices or cameras based on tweets mentioning
these devices collected from the Twitter API [19]. However, for determining relevance to
customer purchasing behaviour, a feed-forward neural network achieved better results. In
this research, predicting the purchase was aided by the sequential nature of the tweets.

According to the authors of [20], if there are cross-correlations, a multivariate time
series model will probably generate more accurate forecasts when compared to univariate
models. However, if there are no correlations, it is usually the other way around. In this
research, the best results were achieved when using ARIMA (compared to univariate and
multivariate state space models) and the authors’ explanations were that the case of a
tourist ﬂow from different European countries to Seychelles shows an absence of a ‘rich’
cross-correlation structure.

Esnaﬁ et al. in [6] describe the comparison of many different methods for predicting
furniture sales as an example of seasonal time series. The authors conclude that neural
networks in general performed better than classical forecasting methods with stacked

Electronics 2023, 12, 2616

3 of 14

LSTM being the best. In total, Prophet, LSTM, stacked LSTM and CNN were the closest in
prediction performance.

An interesting approach is presented in [21]. The authors developed a graph-multi-
scale pyramid networks (GMP) framework with the intent of including multi-scale temporal
dynamics and arbitrary inter-dependencies that exist between product categories. The
part of the GMP is a convolutional neural network whose task is to encode the categorical
temporal pattern at all scales (daily, weekly, bi-weekly, monthly). Their experiments show
that this method performs better than the state-of-the-art baselines.

In purchase prediction, one of the main challenges in the non-contractual setting
is how to differentiate customers that are currently in between transactions and those
that will not return [22]. A proposed solution has been developed as a machine learning
framework for forecasting future purchases based on the customer transaction database.
In this research, customer characteristics were determined on a monthly level. Some of
the customer characteristics included the following: the number of total purchases, the
mean time between purchases, the mean values of purchases, and the time frame variation.
In their experiments, they used logistic lasso regression, extreme learning machine and
gradient tree boosting on transactional data of a central European manufacturer, with
gradient tree boosting outperforming the other two.

However, according to [23], despite experimenting with different network setups and
feature combinations, there was not a single setup/combination that could achieve superior
results in all three of the posed tasks. The authors used an LSTM neural network to forecast
day of the week, time of day and product category for an online shopping store and had
the most difﬁculty in predicting the product category.

Both [24,25] suggest that there is a difference in the purchasing process, as well as
feature interaction, when a customer actually makes a purchase and when they are simply
browsing and/or give up on the purchase.

Additionally, the purpose of a purchase can be a factor in purchase decision making.
The authors of [26] argue that personal purchases are characterized as impulsive, while
business purchases follow a more rigid, formalized process where there is a “need”, not a
“want”.

The topic of [27] is to predict purchase behaviour in large product assortments by
using purchase history data and potentially customer characteristics. They consider latent
Dirichlet allocation and mixtures of Dirichlet-multinomials, and conclude that the former
performs similar to the latter while being far more scalable.

Consumer behaviour was also analysed in [28] in order to build a model for fore-
casting the next purchase date and the purchase amount. Input data was collected from
conﬁrmation emails sent to customers after purchase. In this research, the best performing
model was Bayesian network classiﬁcation.

In [29], a sales forecasting model based on LSTM was developed where one of the input
variables, “number of the active bookers per day”, was estimated. The use of a predicted
variable as an input variable to another model increases the chance of uncertainty entering
the system, while the sales predictions results depend on various uncertainties or noise
due to the estimated input variable and different noise distributions such as normalized,
uniform, and logistic distributions.

Luo et. al. proposed the extreme deep factorization machine (xDeepFM) model to
explore the correlations between the sales-inﬂuencing features as much as possible, and
then modelled the sales prediction using LSTM in [30] to improve the accuracy of the
prediction model. The hybrid forecasting model has a higher optimization rate compared
to other models and provides a scientiﬁc basis for apparel companies’ demand plans.

Seasonal long short-term memory (SLSTM) was presented in [31] as a method for
predicting the sales of agricultural products to stabilize supply and demand. The SLSTM
model is trained using the seasonality attributes of week, month, and quarter as additional
inputs to historical time-series data. The forecasting results of the proposed SLSTM model

Electronics 2023, 12, 2616

4 of 14

were compared to auto ARIMA, Prophet, and a standard LSTM and SLSTM outperforms
the other presented models regarding the metrics proposed in their research.

Based on the analysed research, it can be concluded that the main advantage of
LSTM neural networks is their ability to capture both short-term and long-term sequence
patterns. Their complexity, however, increases training times, which can be a problem if
time constraints exist.

3. Methods

The whole purchase prediction process from collecting data to evaluating results is
shown in Figure 1. The data is collected from the database containing all purchase transac-
tions, customer, and product information. Next, several data transformation processes are
applied to adapt data for the regression model. This is followed with the training of mul-
tiple LSTM neural networks with different input and output features. Finally, prediction
results are evaluated.

Figure 1. The purchase prediction process.

The novelty, compared to related work, is using the generic product identiﬁers for
deﬁning product categories. Additionally, a new type of input feature is constructed based
on generic product identiﬁer (GPI) values for products in the purchase. This feature is a
multi-hot encoded vector named the GPI drug group/category vector. One beneﬁt of the
proposed approach is the possibility of applying it to a different domain with a deﬁned
classiﬁcation system similar to GPI.

Individual parts of the purchase prediction process are described in the following

subsections.

3.1. Data Collection

This research was performed with data acquired from a medical device and drug
company. The data was collected from the database containing all purchase transactions,
customer, and product information. Collected data consist of purchasing transactions
for a great number of customers during a four-and-a-half-year period. All the personal
identiﬁable information was anonymized before any other data transformation process.

Electronics 2023, 12, x FOR PEER REVIEW 4 of 16   model is trained using the seasonality attributes of week, month, and quarter as additional inputs to historical time-series data. The forecasting results of the proposed SLSTM model were compared to auto ARIMA, Prophet, and a standard LSTM and SLSTM outperforms the other presented models regarding the metrics proposed in their research. Based on the analysed research, it can be concluded that the main advantage of LSTM neural networks is their ability to capture both short-term and long-term sequence pat-terns. Their complexity, however, increases training times, which can be a problem if time constraints exist. 3. Methods The whole purchase prediction process from collecting data to evaluating results is shown in Figure 1. The data is collected from the database containing all purchase trans-actions, customer, and product information. Next, several data transformation processes are applied to adapt data for the regression model. This is followed with the training of multiple LSTM neural networks with different input and output features. Finally, predic-tion results are evaluated.  Figure 1. The purchase prediction process. The novelty, compared to related work, is using the generic product identifiers for defining product categories. Additionally, a new type of input feature is constructed based on generic product identifier (GPI) values for products in the purchase. This feature is a multi-hot encoded vector named the GPI drug group/category vector. One benefit of the proposed approach is the possibility of applying it to a different domain with a defined classification system similar to GPI. Individual parts of the purchase prediction process are described in the following subsections. 3.1. Data Collection This research was performed with data acquired from a medical device and drug company. The data was collected from the database containing all purchase transactions, customer, and product information. Collected data consist of purchasing transactions for Electronics 2023, 12, 2616

5 of 14

The original format of the data contained around 7.5 million transactions including
data such as the identiﬁer of the customer, the identiﬁer of the product, the quantity of
the product, and the date and time of the transaction. Each transaction was for a single
product even though a customer had (usually) ordered multiple products, because each
was recorded separately. After aggregating transactions from the same order and removing
customers with less than four orders, just under one million orders remained. Those orders
were made by around 10,100 customers. Figure 2 shows the histogram of the number of
orders per customer. It is noticeable that the majority of customers made 200 or less orders.

Figure 2. Histogram of the number of orders per customer.

3.2. Data Preprocessing

Data pre-processing and building training datasets was performed in Python, utilizing

the Pandas library [32].

The ﬁrst step in data transformation was anonymizing all personal identiﬁable infor-
mation. Next, GPI or partial GPI was determined on an individual basis and those data
were added to product information.

Original data product information contained properties such as product identiﬁers
(internal ID, not relevant outside the system), product names and GPIs. The GPI (generic
product identiﬁer) is a 14-character therapeutic classiﬁcation system. It contains seven
2-character hierarchical groups where each tier contains different information about a drug
product: drug group, drug class, drug subclass, drug base name, drug name, dose form
and dose strength. This level of granularity enables storing very general or very speciﬁc
information about a drug product [33].

GPIs are universal and can be used for drug products from all vendors. However, the
full GPI was not available in the system for all products. About half of the products had
a full GPI stored, while the rest had no values. The GPI contains 7 tiers of information,
but not all were necessary for each of the attempted predictions. Since the 2-character
groups are hierarchical, it was possible to ﬁll in the ﬁrst 4 to 8 characters for almost all
products using available product info, leaving only 2.5% of the products without any GPI
information.

The ﬁrst 2-characters represent the drug group. There are 99 possible values, i.e.,
99 drug groups, which can be grouped in 15 categories of similar drug groups. In both
cases, an additional Unknown value was considered, representing products missing GPI
data. A bar chart representing the number of purchases containing each of the 100 GPI drug
groups is given in Figure 3. Evidently, not all drug groups are equally represented—some
are ordered much more frequently than others.

Electronics 2023, 12, x FOR PEER REVIEW 5 of 16   a great number of customers during a four-and-a-half-year period. All the personal iden-tifiable information was anonymized before any other data transformation process. The original format of the data contained around 7.5 million transactions including data such as the identifier of the customer, the identifier of the product, the quantity of the product, and the date and time of the transaction. Each transaction was for a single product even though a customer had (usually) ordered multiple products, because each was recorded separately. After aggregating transactions from the same order and remov-ing customers with less than four orders, just under one million orders remained. Those orders were made by around 10,100 customers. Figure 2 shows the histogram of the num-ber of orders per customer. It is noticeable that the majority of customers made 200 or less orders.  Figure 2. Histogram of the number of orders per customer. 3.2. Data Preprocessing Data pre-processing and building training datasets was performed in Python, utiliz-ing the Pandas library [32]. The first step in data transformation was anonymizing all personal identifiable infor-mation. Next, GPI or partial GPI was determined on an individual basis and those data were added to product information. Original data product information contained properties such as product identifiers (internal ID, not relevant outside the system), product names and GPIs. The GPI (generic product identifier) is a 14-character therapeutic classification system. It contains seven 2-character hierarchical groups where each tier contains different information about a drug product: drug group, drug class, drug subclass, drug base name, drug name, dose form and dose strength. This level of granularity enables storing very general or very specific information about a drug product [33]. GPIs are universal and can be used for drug products from all vendors. However, the full GPI was not available in the system for all products. About half of the products had a full GPI stored, while the rest had no values. The GPI contains 7 tiers of information, but not all were necessary for each of the attempted predictions. Since the 2-character groups are hierarchical, it was possible to fill in the first 4 to 8 characters for almost all products using available product info, leaving only 2.5% of the products without any GPI infor-mation. The first 2-characters represent the drug group. There are 99 possible values, i.e., 99 drug groups, which can be grouped in 15 categories of similar drug groups. In both cases, an additional Unknown value was considered, representing products missing GPI data. Electronics 2023, 12, 2616

6 of 14

Figure 3. Number of orders per drug group.

Collected transaction data contained information about the date and time of the
purchase. In the following step, input data were adapted for the regression model by
transforming the date/time information into a value that signiﬁes the number of days
that have passed between the previous relevant purchase and the current purchase. This
way, the time series describing the purchase history contained a series of numbers, each
representing the number of days that passed between two consecutive purchases. To be
able to create a time series, a minimum of two relevant purchases are needed, but a greater
number (at least ﬁve purchases) is preferable for better results.

Since the research aim was to predict drug groups that will be contained in the next
purchase of a customer, the transactions were then aggregated by date/time to include all
products from the same purchase. The result was a list of all products in the purchase and
the GPI (or a partial GPI), including the drug group of each product.

Next, the GPI group and category vectors were derived for the whole purchase. The
resulting feature, used for prediction, was a multi-hot encoded vector with each element
representing the presence of a speciﬁc drug group/category in the purchase. The ﬁnal step
was to transform all this information into time series for training and testing LSTM neural
networks.

There are three datasets used for the experiments. Each dataset contains transactions
for the same period, but only for customers that have made at least a speciﬁed number
of purchases during that period. The data set of 100+ purchases contains transactions
from customers that have made at least 100 purchases during the deﬁned period. Analo-
gously, the 20+ purchases dataset and the 5+ purchases dataset contains transactions from
customers that have at least 20 or 5 purchases, respectively, during the deﬁned period.

3.3. Training Neural Networks

The training process was done separately for several different types of neural network
structures and input/output features. Experiments were conducted with neural networks
implemented in Python using the Keras library [34] running on top of TensorFlow [35].

Several sets of experiments were performed with different setups. Each set is deﬁned

by a few characteristics:
•
•

The usage of drug groups (100 groups) or drug categories (16 categories);
Predicting the next purchase day and drug group/category together with a single
neural network or with two separate neural networks; and
The dataset used, where datasets are deﬁned by a minimal number of relevant pur-
chases by a single customer.

•

Electronics 2023, 12, x FOR PEER REVIEW 6 of 16   A bar chart representing the number of purchases containing each of the 100 GPI drug groups is given in Figure 3. Evidently, not all drug groups are equally represented—some are ordered much more frequently than others.  Figure 3. Number of orders per drug group. Collected transaction data contained information about the date and time of the pur-chase. In the following step, input data were adapted for the regression model by trans-forming the date/time information into a value that signifies the number of days that have passed between the previous relevant purchase and the current purchase. This way, the time series describing the purchase history contained a series of numbers, each represent-ing the number of days that passed between two consecutive purchases. To be able to create a time series, a minimum of two relevant purchases are needed, but a greater num-ber (at least five purchases) is preferable for better results. Since the research aim was to predict drug groups that will be contained in the next purchase of a customer, the transactions were then aggregated by date/time to include all products from the same purchase. The result was a list of all products in the purchase and the GPI (or a partial GPI), including the drug group of each product. Next, the GPI group and category vectors were derived for the whole purchase. The resulting feature, used for prediction, was a multi-hot encoded vector with each element representing the presence of a specific drug group/category in the purchase. The final step was to transform all this information into time series for training and testing LSTM neural networks. There are three datasets used for the experiments. Each dataset contains transactions for the same period, but only for customers that have made at least a specified number of purchases during that period. The data set of 100+ purchases contains transactions from customers that have made at least 100 purchases during the defined period. Analogously, the 20+ purchases dataset and the 5+ purchases dataset contains transactions from cus-tomers that have at least 20 or 5 purchases, respectively, during the defined period. 3.3. Training Neural Networks The training process was done separately for several different types of neural net-work structures and input/output features. Experiments were conducted with neural net-works implemented in Python using the Keras library [34] running on top of TensorFlow [35]. Several sets of experiments were performed with different setups. Each set is defined by a few characteristics: Electronics 2023, 12, 2616

7 of 14

The ﬁrst experiment setup focused on neural networks, with both the GPI drug
group/category and the next purchase day as output features. Following previous re-
search [15–18], in next purchase day’s prediction, the initial experiments used multivariate
time series containing the number of days between consecutive purchases and the multi-hot
encoded vector of 100 drug groups present as input and was performed on LSTM and
SimpleRNN neural networks, i.e., their implementations in Keras [34]. Solving of the
problem of the vanishing gradient is the principal advantage of the LSTM [36,37], which
results in the ability to store long-term data dependencies [38,39]. According to this, LSTM
produced better results in every metric, and SimpleRNN was eliminated from further
experiments.

The second setup was directed at predicting only the GPI drug group/category using
an LSTM neural network, while the third setup focused on predicting only the next purchase
day with a separate LSTM neural network.

The structure of the LSTM cell used in the experiments is shown in Figure 4. Each cell
is essentially a memory block with three multiplicative gates: the input gate, the forget gate
and the output gate. The gates control what part of input, cell state or output will be used
in further calculations, respectively, and what part will be discarded.

Figure 4. Structure of the long short-term memory cell [40].

For the LSTM cell shown in Figure 4, the following equations apply [40]:

it = σ(Wxixt + Whiht−1 + Wcict−1 + bi)

ft = σ(Wx f xt + Wh f ht−1 + Wc f ct−1 + b f

ct = ftct−1 + ittanh(Wxcxt + Whcht−1 + bc)

ot = σ(Wxoxt + Whoht−1 + Wcoct + bo)

ht = ottanh(ct)

(1)

(2)

(3)

(4)

(5)

In the equations stated above, i, f, o, c and x represent the activation vectors for the
input gate, forget gate, output gate, and cell and cell input, where σ is the sigmoid function,
h is the hidden vector, b the biases and W represents the weight matrices. Each weight
matrix it is marked in subscript, indicating to which connection it applies.

Electronics 2023, 12, x FOR PEER REVIEW 7 of 16   • The usage of drug groups (100 groups) or drug categories (16 categories); • Predicting the next purchase day and drug group/category together with a single neural network or with two separate neural networks; and • The dataset used, where datasets are defined by a minimal number of relevant pur-chases by a single customer. The first experiment setup focused on neural networks, with both the GPI drug group/category and the next purchase day as output features. Following previous re-search [15–18], in next purchase day’s prediction, the initial experiments used multivariate time series containing the number of days between consecutive purchases and the multi-hot encoded vector of 100 drug groups present as input and was performed on LSTM and SimpleRNN neural networks, i.e., their implementations in Keras [34]. Solving of the problem of the vanishing gradient is the principal advantage of the LSTM [36,37], which results in the ability to store long-term data dependencies [38,39]. According to this, LSTM produced better results in every metric, and SimpleRNN was eliminated from further ex-periments. The second setup was directed at predicting only the GPI drug group/category using an LSTM neural network, while the third setup focused on predicting only the next pur-chase day with a separate LSTM neural network. The structure of the LSTM cell used in the experiments is shown in Figure 4. Each cell is essentially a memory block with three multiplicative gates: the input gate, the forget gate and the output gate. The gates control what part of input, cell state or output will be used in further calculations, respectively, and what part will be discarded.  Figure 4. Structure of the long short-term memory cell [40]. For the LSTM cell shown in Figure 4, the following equations apply [40]: 11()txithitcitiiWxWhWcb−−=+++, (1) 11(txfthftcftffWxWhWcb−−=+++, (2) 11tanh()ttttxcthctccfciWxWhb−−=+++, (3) Electronics 2023, 12, 2616

8 of 14

3.4. Evaluation

The neural networks from the ﬁrst setup were evaluated separately since they con-
tained all output features, while the second and the third were evaluated together because
each of them outputs a part of the required features.

In all setups, the problem was posed as a regression, i.e., based on previous values in a
time series, the neural network predicts the following values. However, for the evaluation
of these experimental results, it was not possible to adequately measure the performance
with regression metrics. The output of the neural networks contained, similarly as the input,
the number of days until the next purchase and the GPI drug group/category vector for
the next purchase. For the number of days until the next purchase, it was possible to apply
regression metrics or convert to a classiﬁcation problem—is there going to be a purchase
in the following 7 days? For the GPI drug group/category vector, each element has the
value of 0 or 1 where 0 signiﬁes that this drug group/category will not appear in the next
purchase, while 1 signiﬁes that it will. For the evaluation of these predictions, it is better
to focus on how many of the drug group/category present in the purchase were correctly
predicted. Since there are 100 drug groups (99 plus an Unknown value) and 16 categories
(15 plus an unknown value) there are usually much more drug groups/categories that
will not be present in a purchase than those that will. Therefore, simply looking at the
number of correctly predicted vector elements will not adequately represent the situation
and it is necessary to look at present and missing drug groups/categories separately. This
is equivalent to transforming this problem to a classiﬁcation one—accuracy, precision and
recall can be measured for two classes: the drug group/category that will appear in the
following purchase (the corresponding vector element is 1) and the drug group/category
that will not appear in the following purchase (the corresponding vector element is 0). This
approach is similar to the one proposed in previous research predicting the next purchase
day [17,18]. The output of the neural network was the predicted number of days until
the next relevant purchase, but predictions were divided in two classes: “A purchase will
happen in the following 7 days” and “There will be no purchase in the following 7 days”.
This allowed for the viewing of the problem in two ways and applying both types of metrics
(i.e., regression and classiﬁcation metrics).

4. Results

Results for all experiments are shown using accuracy, precision and recall [41]. Ac-
curacy presents a quotient of the sum of correctly classiﬁed instances of any class and the
total number of instances of all classes. Precision for a certain class is the quotient of the
number of correctly classiﬁed instances of that class and all instances that were classiﬁed as
that class. Recall, on the other hand, is the quotient of the number of correctly classiﬁed
instances of a class and the number of all instances that belong to that class.

As mentioned in the previous section, the initial set of experiments performed the
prediction of 100 drug group vector and the next purchase day with a multivariate LSTM
neural network and a multivariate SimpleRNN neural network using the Keras library
in Python. LSTM neural networks produced better results in all measured metrics with
the most obvious differences in precision and recall for the “Realized purchases” category
in predicting the GPI drug group. For this reason, SimpleRNN neural networks were
eliminated from the following experiments. In order to demonstrate the differences in
results with these two types of neural networks, Table 1 shows the results for the 100+ pur-
chases dataset.

Results of the following experiments are shown in Figures 5–7. Each ﬁgure shows
the results for one of the datasets and consists of two charts: one represents the metric
values for the prediction of drug groups/categories and the other shows the results for the
prediction of the next purchase day. The values for metrics are calculated separately for the
prediction of drug groups/categories and the prediction of the next purchase day. Different
neural networks are represented with different colours and denoted with abbreviated
names as follows. A single multivariate LSTM neural network for simultaneous prediction

Electronics 2023, 12, 2616

9 of 14

of the drug category vector (16 drug categories) and next purchase day is denoted as
SMLSTM 16. The combination of a multivariate LSTM neural network for the prediction
of the drug category vector (16 drug categories) and a pseudo-multivariate LSTM neural
network for prediction of the next purchase day is denoted as MLSTM + PMLSTM 16.
A single multivariate LSTM neural network for the simultaneous prediction of the drug
group vector (100 drug groups) and the next purchase day is denoted as SMLSTM 100.
Finally, the combination of a multivariate LSTM neural network for the prediction of the
drug group vector (100 drug groups) and a pseudo-multivariate LSTM neural network
for the prediction of the next purchase day is denoted as MLSTM + PMLSTM 100. In all
the charts, the class “Realized Purchases” is labelled as RP, while the class “Unrealized
purchases” is labelled as UP.

Table 1. The 100+ purchases dataset—prediction of the GPI drug groups/categories and the next pur-
chase day with multivariate LSTM and multivariate SimpleRNN neural networks. Better performance
is marked with bold lettering for each metric.

GPI Drug Groups

Realized
Purchases

Unrealized
Purchases

Accuracy

Next Day

Realized
Purchases

Unrealized
Purchases

Precision

Recall

Precision

Recall

Precision

Recall

Precision

Recall

92.34%

62.33%

97.50%

99.65%

84.47%

46.02%

96.44%

99.43%

95.16%

94.42%

99.86%

99.28%

93.02%

87.00%

99.71%

92.48%

86.00%

98.50%

Accuracy

97.27%

96.03%

Multivariate LSTM

Multivariate SimpleRNN

Figure 5. Prediction results for the 100+ purchases dataset: (a) results for the prediction of drug
groups/categories; and (b) results for the prediction of the next purchase day.

Figure 6. Prediction results for the 20+ purchases dataset: (a) results for the prediction of drug
groups/categories; and (b) results for the prediction of the next purchase day.

Electronics 2023, 12, x FOR PEER REVIEW 9 of 16   eliminated from the following experiments. In order to demonstrate the differences in re-sults with these two types of neural networks, Table 1 shows the results for the 100+ pur-chases dataset. Table 1. The 100+ purchases dataset—prediction of the GPI drug groups/categories and the next purchase day with multivariate LSTM and multivariate SimpleRNN neural networks. Better perfor-mance is marked with bold lettering for each metric.  GPI Drug Groups Next Day  Accuracy Realized Purchases Unrealized Purchases Accuracy Realized Purchases Unrealized Purchases Precision Recall Precision Recall Precision Recall Precision Recall Multivariate LSTM 97.27% 92.34% 62.33% 97.50% 99.65% 95.16% 99.86% 93.02% 87.00% 99.71% Multivariate SimpleRNN  96.03% 84.47% 46.02% 96.44% 99.43% 94.42% 99.28% 92.48% 86.00% 98.50% Results of the following experiments are shown in Figures 5–7. Each figure shows the results for one of the datasets and consists of two charts: one represents the metric values for the prediction of drug groups/categories and the other shows the results for the pre-diction of the next purchase day. The values for metrics are calculated separately for the prediction of drug groups/categories and the prediction of the next purchase day. Differ-ent neural networks are represented with different colours and denoted with abbreviated names as follows. A single multivariate LSTM neural network for simultaneous prediction of the drug category vector (16 drug categories) and next purchase day is denoted as SMLSTM 16. The combination of a multivariate LSTM neural network for the prediction of the drug category vector (16 drug categories) and a pseudo-multivariate LSTM neural network for prediction of the next purchase day is denoted as MLSTM + PMLSTM 16. A single multivariate LSTM neural network for the simultaneous prediction of the drug group vector (100 drug groups) and the next purchase day is denoted as SMLSTM 100. Finally, the combination of a multivariate LSTM neural network for the prediction of the drug group vector (100 drug groups) and a pseudo-multivariate LSTM neural network for the prediction of the next purchase day is denoted as MLSTM + PMLSTM 100. In all the charts, the class “Realized Purchases” is labelled as RP, while the class “Unrealized pur-chases” is labelled as UP.   (a) (b) Figure 5. Prediction results for the 100+ purchases dataset: (a) results for the prediction of drug groups/categories; and (b) results for the prediction of the next purchase day. Electronics 2023, 12, x FOR PEER REVIEW 10 of 16     (a) (b) Figure 6. Prediction results for the 20+ purchases dataset: (a) results for the prediction of drug groups/categories; and (b) results for the prediction of the next purchase day.   Electronics 2023, 12, 2616

10 of 14

Figure 7. Prediction results for the 5+ purchases dataset: (a) results for the prediction of drug
groups/categories; and (b) results for the prediction of the next purchase day.

It is clear at ﬁrst sight that the drug group/category vector prediction for the following
purchase produces signiﬁcantly better results when using a dedicated neural network
for all datasets and using both drug groups and drug categories. The most noticeable
improvement can be seen for the recall in the “Realized purchases” class, which increased
by 15–50%. In this case, recall is the quotient of the number of drug groups/categories
that were correctly predicted to appear in the next purchase and the number of all drug
groups/categories that appeared in the next purchase(s). Additionally, the increase for the
“Realized purchases” class’s recall is always greater when using all 100 drug groups.

For the prediction of the next purchase day, the situation is exactly the opposite. Except
some minor variations in the 100+ purchases dataset, almost all metrics show better results
when a single neural network performs simultaneous prediction of the purchase day and
the GPI drug group/category.

If only the drug groups/categories that are present in the following purchases are
taken into account, the number of correctly or incorrectly predicted purchased drug
groups/categories can be analysed. The results are relatively similar for experiments
using the drug groups and experiments using drug categories. For the sake of clearer visual
representation, the data plotted is from experiments with drug categories because there are
only 16 of them, compared to 100 drug groups.

Figure 8 shows the minimum number of correctly predicted purchased drug categories
by percentage for the 100+ purchases dataset and dedicated LSTM neural network. This
means that the experiments were conducted using an LSTM neural network trained on
the 100+ purchases dataset where the only output is the drug categories vector. After per-
forming the experiments, the number of correctly predicted drug categories was calculated
for each customer taking into account only those that actually appear in the following
purchase. It was then possible to determine the percentage of total customers for which the
following occurred: at least one purchased category was correctly predicted, at least two
categories were correctly predicted, etc. For 95.7% of customers, at least one category that
was purchased in the following purchase was correctly predicted. At least two categories
were correctly predicted for 82.91% of customers, at least three for 67.18% of customers and
for 51.19% of customers at least four categories were correctly predicted.

The other way of looking at the experimental results is by viewing the number of
incorrectly predicted categories, again only considering categories that are present in the
next purchase. By using an analogous process as described above, the percentage of total
customers was determined for which the following occurred: no more than one category
was incorrectly predicted, no more than two categories were incorrectly predicted, etc. After
examining the numbers, it was evident that there were never more than ﬁve incorrectly
predicted categories out of those that were present in the following purchases. The chart
showing the maximum number of incorrectly predicted purchased drug categories by

Electronics 2023, 12, x FOR PEER REVIEW 11 of 16      (a) (b) Figure 7. Prediction results for the 5+ purchases dataset: (a) results for the prediction of drug groups/categories; and (b) results for the prediction of the next purchase day. It is clear at first sight that the drug group/category vector prediction for the follow-ing purchase produces significantly better results when using a dedicated neural network for all datasets and using both drug groups and drug categories. The most noticeable im-provement can be seen for the recall in the “Realized purchases” class, which increased by 15–50%. In this case, recall is the quotient of the number of drug groups/categories that were correctly predicted to appear in the next purchase and the number of all drug groups/categories that appeared in the next purchase(s). Additionally, the increase for the “Realized purchases” class’s recall is always greater when using all 100 drug groups. For the prediction of the next purchase day, the situation is exactly the opposite. Ex-cept some minor variations in the 100+ purchases dataset, almost all metrics show better results when a single neural network performs simultaneous prediction of the purchase day and the GPI drug group/category. If only the drug groups/categories that are present in the following purchases are taken into account, the number of correctly or incorrectly predicted purchased drug groups/categories can be analysed. The results are relatively similar for experiments using the drug groups and experiments using drug categories. For the sake of clearer visual representation, the data plotted is from experiments with drug categories because there are only 16 of them, compared to 100 drug groups. Figure 8 shows the minimum number of correctly predicted purchased drug catego-ries by percentage for the 100+ purchases dataset and dedicated LSTM neural network. This means that the experiments were conducted using an LSTM neural network trained on the 100+ purchases dataset where the only output is the drug categories vector. After performing the experiments, the number of correctly predicted drug categories was cal-culated for each customer taking into account only those that actually appear in the fol-lowing purchase. It was then possible to determine the percentage of total customers for which the following occurred: at least one purchased category was correctly predicted, at least two categories were correctly predicted, etc. For 95.7% of customers, at least one cat-egory that was purchased in the following purchase was correctly predicted. At least two categories were correctly predicted for 82.91% of customers, at least three for 67.18% of customers and for 51.19% of customers at least four categories were correctly predicted. Electronics 2023, 12, 2616

11 of 14

percentage for the 100+ purchases dataset and dedicated LSTM neural network is shown in
Figure 9. No more than one category was incorrectly predicted for 81.17% of customers, no
more than two for 93.6% of customers, no more than three for 98.26% of customers and no
more than four for 99.63% of customers.

Figure 8. Minimum number of correctly predicted purchased drug categories by percentage for the
100+ dataset and dedicated LSTM neural network.

Figure 9. Maximum number of incorrectly predicted purchased drug categories by percentage for
the 100+ purchases dataset and dedicated LSTM neural network.

For illustration purposes, the structure of a neural network prediction is given below.
The prediction represented here is an example of an output from a single multivariate
LSTM neural network for the simultaneous prediction of the drug category vector (16 drug
categories) and next purchase day:

1 0 0 1 1 1 0 0 1 0 0 0 1 0 1 1 3.45

The ﬁrst 16 values represent a multi-hot drug category vector in which 0 denotes that
the appropriate drug category is not expected in the following purchase, while 1 denotes

Electronics 2023, 12, x FOR PEER REVIEW 12 of 16    Figure 8. Minimum number of correctly predicted purchased drug categories by percentage for the 100+ dataset and dedicated LSTM neural network. The other way of looking at the experimental results is by viewing the number of incorrectly predicted categories, again only considering categories that are present in the next purchase. By using an analogous process as described above, the percentage of total customers was determined for which the following occurred: no more than one category was incorrectly predicted, no more than two categories were incorrectly predicted, etc. After examining the numbers, it was evident that there were never more than five incor-rectly predicted categories out of those that were present in the following purchases. The chart showing the maximum number of incorrectly predicted purchased drug categories by percentage for the 100+ purchases dataset and dedicated LSTM neural network is shown in Figure 9. No more than one category was incorrectly predicted for 81.17% of customers, no more than two for 93.6% of customers, no more than three for 98.26% of customers and no more than four for 99.63%. of customers.   Electronics 2023, 12, x FOR PEER REVIEW 13 of 16     Figure 9. Maximum number of incorrectly predicted purchased drug categories by percentage for the 100+ purchases dataset and dedicated LSTM neural network. For illustration purposes, the structure of a neural network prediction is given below. The prediction represented here is an example of an output from a single multivariate LSTM neural network for the simultaneous prediction of the drug category vector (16 drug categories) and next purchase day: 1 0 0 1 1 1 0 0 1 0 0 0 1 0 1 1 3.45 The first 16 values represent a multi-hot drug category vector in which 0 denotes that the appropriate drug category is not expected in the following purchase, while 1 denotes that the drug category is expected in the next purchase. The final value represents the estimated number of days until the following purchase by the specified customer. 5. Discussion In all experiments with the prediction of the drug groups/categories that will appear in the following purchase, the metrics were higher when using drug groups instead of drug categories. This leads to the conclusion that transforming the data to generate the vector of drug categories is unnecessary since it is an additional step that does not produce better results. The reason for this is probably the fact that original data contain more de-tails (more specific groups versus more general categories) allowing for more precise pre-dictions. In the case of next purchase day prediction, the added information about the content of the purchase helped produce more accurate predictions than relying solely on the num-ber of days between consecutive purchases. As for using the drug group or drug category vector, there was a slight difference in favour of using all 100 drug groups. This difference was not very significant, but since the drug categories were derived from the drug groups, it was only logical to use the original form of the data in prediction. If the results for different experiment setups are compared across datasets, there were no significant variations in accuracy, i.e., very good results can be achieved even with a small number of purchases per customer. The biggest difference can be noticed in recall for the “Realized purchases” category in both the drug group/category and next purchase day prediction, which significantly increased in datasets with a greater number of pur-chases per customer. The conclusion that can be derived is that when there is more histor-ical information (a greater number of purchases), a greater percent of the actual future purchases will be correctly predicted.   Electronics 2023, 12, 2616

12 of 14

that the drug category is expected in the next purchase. The ﬁnal value represents the
estimated number of days until the following purchase by the speciﬁed customer.

5. Discussion

In all experiments with the prediction of the drug groups/categories that will appear
in the following purchase, the metrics were higher when using drug groups instead of drug
categories. This leads to the conclusion that transforming the data to generate the vector of
drug categories is unnecessary since it is an additional step that does not produce better
results. The reason for this is probably the fact that original data contain more details (more
speciﬁc groups versus more general categories) allowing for more precise predictions.

In the case of next purchase day prediction, the added information about the content of
the purchase helped produce more accurate predictions than relying solely on the number
of days between consecutive purchases. As for using the drug group or drug category
vector, there was a slight difference in favour of using all 100 drug groups. This difference
was not very signiﬁcant, but since the drug categories were derived from the drug groups,
it was only logical to use the original form of the data in prediction.

If the results for different experiment setups are compared across datasets, there
were no signiﬁcant variations in accuracy, i.e., very good results can be achieved even
with a small number of purchases per customer. The biggest difference can be noticed in
recall for the “Realized purchases” category in both the drug group/category and next
purchase day prediction, which signiﬁcantly increased in datasets with a greater number
of purchases per customer. The conclusion that can be derived is that when there is more
historical information (a greater number of purchases), a greater percent of the actual future
purchases will be correctly predicted.

6. Conclusions

In this paper, research in the ﬁeld of purchase prediction based on historical customer
transactions is presented. The original data from the medical supply company was pre-
processed and transformed to create a time series appropriate as input for a neural network.
Due to the medical nature of the data, part of the GPI was used to determine product
category information in its original form and a shortened version devised by grouping
similar categories. Multiple neural networks for the prediction of the next purchase day,
GPI drug groups/categories and all features together were trained. The trained networks
were evaluated with multiple datasets, differing on the minimal number of purchases
per customer. The results show that the drug groups/categories for the next purchase
can be predicted with a higher accuracy when using an LSTM neural network dedicated
solely to predicting this output feature. However, for predicting the next purchase day, it is
preferable to use a single LSTM neural network that predicts all output features. It can be
concluded that a combined approach should give the best results if the goal is to achieve
superior accuracy for all output features.

One practical limitation of the proposed approach is the usage of the GPI for deﬁning
product categories. Since this therapeutic classiﬁcation system is used for identifying drug
products, it limits the application of this approach to the ﬁeld of medical drugs. However,
this novel approach can be applied to any domain which uses a classiﬁcation system,
whether hierarchical or non-hierarchical.

In further research, it would be interesting to use a greater number of hierarchical
groups of the GPI which would enable focusing on more speciﬁc classiﬁcation of the
product in question.

Author Contributions: Conceptualization, B.P. and M. ´C.; methodology, M. ´C. and B.P.; software,
M. ´C.; validation, B.P., D.S. and I. ´C.; data curation, B.P.; writing—original draft preparation, M. ´C.;
writing—review and editing, B.P., D.S. and I. ´C. All ﬁgures and tables are the authors’ contributions,
except those explicitly cited. All authors have read and agreed to the published version of the
manuscript.

Electronics 2023, 12, 2616

13 of 14

Funding: This research received no external funding.

Data Availability Statement: Restrictions apply to the availability of these data. Data were obtained
from a medical device and drug company and, due to conﬁdentiality issues, are not publicly available.

Conﬂicts of Interest: The authors declare no conﬂict of interest.

References

1.

2.

3.
4.

Zhang, X.; Liang, X.; Zhiyuli, A.; Zhang, S.; Xu, R.; Wu, B. AT-LSTM: An Attention-based LSTM Model for Financial Time Series
Prediction. IOP Conf. Ser. Mater. Sci. Eng. 2019, 569, 052037. [CrossRef]
Althelaya, K.A.; El-Alfy, E.-S.M.; Mohammed, S. Evaluation of bidirectional LSTM for short-and long-term stock market prediction.
In Proceedings of the 2018 9th International Conference on Information and Communication Systems (ICICS), Irbid, Jordan,
3–5 April 2018; pp. 151–156. [CrossRef]
Kim, S.; Kang, M. Financial series prediction using Attention LSTM. arXiv 2019, arXiv:1902.10877.
Giles, C.L.; Lawrence, S.; Tsoi, A.C. Noisy Time Series Prediction using Recurrent Neural Networks and Grammatical Inference.
Mach. Learn. 2001, 44, 161–183. [CrossRef]

5. Wei, H.; Zeng, Q. Research on sales Forecast based on XGBoost-LSTM algorithm Model. J. Phys. Conf. Ser. 2021, 1754, 012191.

6.

[CrossRef]
Esnaﬁ, Y.; Amin, S.H.; Zhang, G.; Shah, B. Time-series forecasting of seasonal items using machine learning—A comparative
analysis. Int. J. Inf. Manag. Data Insights 2022, 2, 100058.
Pavlyshenko, B.M. Machine-Learning Models for Sales Time Series Forecasting. Data 2019, 4, 15. [CrossRef]

7.
8. Wang, P.; Zhang, Y.; Niu, S.; Guo, J. Modeling Temporal Dynamics of Users’ Purchase Behaviors for Next Basket Prediction.

9.

J. Comput. Sci. Technol. 2019, 34, 1230–1240. [CrossRef]
Stanimirovi´c, A.; ´Ciri´c, M.; Džoni´c, B.; Stoimenov, L.; Petrovi´c, N. Sistem za davanje preporuka baziran na tehnologijama
semantiˇckog web-a (Recommender system based on semantic web technologies). Proc. YUINFO 2012, 2012, 147–152.

10. Gruenen, J.; Bode, C.; Hoehle, H. Predictive Procurement Insights: B2B Business Network Contribution to Predictive Insights in the
Procurement Process Following a Design Science Research Approach. In Proceedings of the Designing the Digital Transformation:
12th International Conference, DESRIST 2017, Karlsruhe, Germany, 30 May–1 June 2017; Volume 10243, pp. 267–281. [CrossRef]

11. De Gooijer, J.G.; Hyndman, R.J. 25 years of time series forecasting. Int. J. Forecast. 2006, 22, 443–473. [CrossRef]
12.

Fu, R.; Zhang, Z.; Li, L. Using LSTM and GRU neural network methods for trafﬁc ﬂow prediction. In Proceedings of the 31st
Youth Academic Annual Conference of Chinese Association of Automation (YAC 2016), Wuhan, China, 11–13 November 2016;
Volume 7804912, pp. 324–328. [CrossRef]

13. Verma, A. Consumer Behaviour in Retail: Next Logical Purchase using Deep Neural Network. arXiv 2010, arXiv:2010.06952.
14. McNally, S.; Roche, J.; Caton, S. Predicting the Price of Bitcoin Using Machine Learning. In Proceedings of the 2018 26th Euromicro
International Conference on Parallel, Distributed and Network-Based Processing (PDP), Cambridge, UK, 21–23 March 2018;
pp. 339–343.
Stojˇci´c, A.; Radosavljevi´c, N.; Predi´c, B.; Kovaˇcevi´c, M.; Roganovi´c, M. Analiza vremenskih serija: Metode predvi ¯danja budu´ce
potražnje u veleprodaji (Time Series Analysis: Methods for Future Demand Forecasting in B2B Sales). In Proceedings of the
Zbornik Radova—63. Konferencija za Elektroniku, Telekomunikacije, Raˇcunarstvo, Automatiku i Nuklearnu Tehniku, Srebrno
jezero, Serbia, 3–6 June 2019; pp. 923–928.

15.

16. Predi´c, B.; Radosavljevi´c, N.; Stojˇci´c, A. Time series analysis: Forecasting sales periods in wholesale systems. Facta Univ. Ser.

17.

18.

Autom. Control. Robot. 2020, 18, 177–188. [CrossRef]
´Ciri´c, M.; Predi´c, B. Predicting Purchase Day in B2B: From Statistical Methods towards LSTM Neural Networks. In Proceedings
of the 10th International Conference on Information Society and Technology, Kopaonik, Serbia, 8–11 March 2020; pp. 193–197,
ISBN 978-86-85525-24-7.
´Ciri´c, M.; Predi´c, B. Pseudo-multivariate lstm neural network approach for purchase day prediction in b2b. Facta Univ. Ser. Autom.
Control. Robot. 2021, 19, 151–162. [CrossRef]

19. Korpusik, M.; Sakaki, S.; Chen, F.; Chen, Y.Y. Recurrent Neural Networks for Customer Purchase Prediction on Twitter. CBREcsys@

recsys 2016, 1673, 47–50.

20. du Preez, J.; Witt, S.F. Univariate versus multivariate time series forecasting: An application to international tourism demand. Int.

J. Forecast. 2003, 19, 435–451. [CrossRef]

21. Huang, C.; Wu, X.; Zhang, X.; Zhang, C.; Zhao, J.; Yin, D.; Chawla, N.V. Online Purchase Prediction via Multi-Scale Modeling of
Behavior Dynamics. In Proceedings of the 25th ACM SIGKDD international conference on knowledge discovery & data mining,
Anchorage, AK, USA, 4–8 August 2019. [CrossRef]

22. Martínez, A.; Schmuck, C.; Pereverzyev, S.; Pirker, C.; Haltmeier, M. A machine learning framework for customer purchase

prediction in the non-contractual setting. Eur. J. Oper. Res. 2018, 281, 588–596. [CrossRef]

23. Cirqueira, D.; Helfert, M.; Bezbradica, M. Towards Preprocessing Guidelines for Neural Network Embedding of Customer
Behavior in Digital Retail. In Proceedings of the 2019 3rd International Symposium on Computer Science and Intelligent Control,
Amsterdam, The Netherlands, 25–27 September 2019. [CrossRef]

Electronics 2023, 12, 2616

14 of 14

25.

24.

Stubseid, S.; Arandjelovic, O. Machine Learning Based Prediction of Consumer Purchasing Decisions: The Evidence and Its
Signiﬁcance. In Proceedings of the AI and Marketing Science workshop at AAAI-2018, New Orleans, LA, USA, 2 February 2018;
pp. 100–106, ISBN 978-1-57735-801-5.
Suchacka, G.; Stemplewski, S. Application of Neural Network to Predict Purchases in Online Store. In Proceedings of the 37th
International Conference on Information Systems Architecture and Technology–ISAT 2016–Part IV, Karpacz, Poland, 18–20
September 2016; Springer International Publishing: Cham, Switzerland, 2017; Volume 524, pp. 221–231, ISBN 978-3-319-46583-8.
26. Chai, Y.; Liu, G.; Chen, Z.; Li, F.; Li, Y.; Effah, E.A. A Temporal Collaborative Filtering Algorithm Based on Purchase Cycle. In
Proceedings of the Cloud Computing and Security: 4th International Conference, ICCCS 2018, Haikou, China, 8–10 June 2018;
Revised Selected Papers, Part II. Springer International Publishing: Cham, Switzerland, 2018; pp. 191–201. [CrossRef]
Jacobs, B.J.; Donkers, B.; Fok, D. Model-Based Purchase Predictions for Large Assortments. Mark. Sci. 2016, 35, 389–404.
[CrossRef]

27.

28. Kooti, F.; Lerman, K.; Aiello, L.M.; Grbovic, M.; Djuric, N.; Radosavljevic, V. Portrait of an Online Shopper: Understanding and
predicting consumer behavior. In Proceedings of the Ninth ACM International Conference on Web Search and Data Mining, San
Francisco, CA, USA, 22–25 February 2016. [CrossRef]

29. Goel, S.; Bajpai, R. Impact of Uncertainty in the Input Variables and Model Parameters on Predictions of a Long Short Term

Memory (LSTM) Based Sales Forecasting Model. Mach. Learn. Knowl. Extr. 2020, 2, 256–270. [CrossRef]

30. Luo, T.; Chang, D.; Xu, Z. Research on Apparel Retail Sales Forecasting Based on xDeepFM-LSTM Combined Forecasting Model.

Information 2022, 13, 497. [CrossRef]

31. Yoo, T.-W.; Oh, I.-S. Time Series Forecasting of Agricultural Products’ Sales Volumes Based on Seasonal Long Short-Term Memory.

Appl. Sci. 2020, 10, 8169. [CrossRef]

32. McKinney, W. Data structures for statistical computing in python. In Proceedings of the 9th Python in Science Conference, Austin,

TX, USA, 28 June–3 July 2010; Volume 445, pp. 51–56.

33. Available online: http://wolterskluwer.com/en/solutions/medi-span/about/gpi (accessed on 6 August 2022).
34. Keras. Available online: https://keras.io (accessed on 8 January 2020).
35. Abadi, M.; Barham, P.; Chen, J.; Chen, Z.; Davis, A.; Dean, J.; Devin, M.; Ghemawat, S.; Irving, G.; Isard, M.; et al. Tensorﬂow:
A system for large-scale machine learning. In Proceedings of the 12th USENIX Symposium on Operating Systems Design and
Implementation (OSDI ’16), Savannah, GA, USA, 2–4 November 2016; pp. 265–283.

36. Gers, F.A.; Schmidhuber, J.; Cummins, F. Learning to forget: Continual prediction with LSTM. In Proceedings of the 9th
International Conference on Artiﬁcial Neural Networks: ICANN ’99; Institution of Engineering and Technology (IET), Edinburgh,
UK, 7–10 September 1999; pp. 850–855.

37. Gers, F. Long Short-Term Memory in Recurrent Neural Networks. Ph.D. Thesis, Ecole Polytechnique Federale de Lausanne,

Lausanne, Switzerland, 2001.

38. Hochreiter, S. The Vanishing Gradient Problem During Learning Recurrent Neural Nets and Problem Solutions. Int. J. Uncertain.

Fuzziness Knowl. Based Syst. 1998, 6, 107–116. [CrossRef]

39. Hochreiter, S.; Schmidhuber, J. Long short-term memory. Neural Comput. 1997, 9, 1735–1780. [CrossRef] [PubMed]
40. Graves, A. Generating Sequences With Recurrent Neural Networks. arXiv 2014, arXiv:1308.0850.
41. Lever, J.; Krzywinski, M.; Altman, N. Classiﬁcation Evaluation. Nat. Methods 2016, 13, 541–542. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

