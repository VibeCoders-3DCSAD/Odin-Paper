Highlights

Use of Boosting Algorithms in Household-Level Poverty Measurement: A Machine Learn-
ing Approach to Predict and Classify Household Wealth Quintiles in the Philippines
Erika Lynet V. Salvador

• CatBoost achieved the highest accuracy (90.93%) and overall performance metrics, followed by XGBoost,

GBM, and LightGBM. AdaBoost had the lowest performance.

• AUC-ROC scores indicated that CatBoost, GBM, LightGBM, and XGBoost excelled in distinguishing

between poverty classes, while AdaBoost lagged behind.

• Computational efficiency varied, with AdaBoost having the shortest training time but longest testing time.
CatBoost had the longest training time but was highly efficient during testing. GBM, LightGBM, and
XGBoost balanced well between training and testing times.

4
2
0
2

y
a
M
8
2

]

Y
C
.
s
c
[

1
v
1
6
0
3
1
.
7
0
4
2
:
v
i
X
r
a

Use of Boosting Algorithms in Household-Level Poverty
Measurement: A Machine Learning Approach to Predict and
Classify Household Wealth Quintiles in the Philippines

Ms. Erika Lynet V. Salvadora,b,∗,1 (Researcher)

aDepartment of Mathematics and Statistics, Amherst College, College St., Amherst, 01002, Massachusetts, United States of America
bScience, Technology, Engineering, and Mathematics Strand, Senior High School Department, De La Salle University Integrated School
Manila, Taft Avenue, Malate, Manila, 2401, National Capital Region, Philippines

A R T I C L E I N F O

A B S T R A C T

Keywords:
machine learning
classification
household wealth index
Philippines

This study assessed the effectiveness of machine learning models in predicting poverty
levels in the Philippines using five boosting algorithms: Adaptive Boosting (AdaBoost),
Cat Boosting (CatBoost), Gradient Boosting Machine (GBM), Light Gradient Boosting
Machine (LightGBM), and Extreme Gradient Boosting (XGBoost). CatBoost emerged as
the superior model and achieved the highest scores across accuracy, precision, recall, and
F1-score at 91%, while XGBoost and GBM followed closely with 89% and 88% respectively.
Additionally, the research examined the computational efficiency of these models to analyze
the balance between training time, testing speed, and model size—factors crucial for real-
world applications. Despite its longer training duration, CatBoost demonstrated high testing
efficiency. These results indicate that machine learning can aid in poverty prediction and in the
development of targeted policy interventions. Future studies should focus on incorporating a
wider variety of data to enhance the predictive accuracy and policy utility of these models.

1. Introduction

As of 2024, over 700 million people globally live in extreme poverty and survive on less than $2.15 (Php 125)
per day [1]. To address this, governments worldwide are intensifying efforts to achieve Sustainable Development
Goal 1 (SDG) which targets the eradication of poverty in all its forms by 2030. However, recent research
suggests that the lingering effects of the COVID-19 pandemic may endure in various countries until 2030 [2].
This presents a significant challenge to the goal of reducing global poverty—a target already at risk prior to
the crisis. Hence, the need for significant political intervention is now more pressing than ever [1]. In order for
policymakers to formulate targeted interventions and allocate resources efficiently, accurately determining poverty
levels is paramount [3]. Data empowers governments and organizations to devise strategies that genuinely uplift
individuals and communities from poverty. Without accurate data, policy initiatives risk falling short in addressing
the underlying causes of poverty or reaching those most in need [4].

Poverty, however, is defined diversely. Broadly, poverty measurement approaches fall into two categories:
monetary and non-monetary [5]. The monetary approach, as the name suggests, defines poverty based on income
or expenditure. For instance, the established poverty methodology in the Philippines employs pre-tax income as
an indicator of household well-being [6, 7]. On the other hand, several researchers contend that poverty extends
beyond financial lack and includes aspects such as opportunity, education, and healthcare deficits [8]. Simply put,
they view poverty as multidimensional, not solely defined by money.

Unfortunately, the drawback of conventional econometric methodologies in forecasting poverty is their
tendency to oversimplify the multidimensional nature of poverty. Many prevailing measurements for poverty are
structured without consideration for non-monetary indicators of welfare, such as an individual’s and household’s
health, nutritional, or educational status [9]. Econometric models often rely on pre-selected features (i.e., income)
based on economic theory or prior knowledge, which may often overlook important relationships or interactions
in the data. Therefore, it is of vital importance to conduct assessments considering diverse dimensions of poverty
to formulate effective reduction policies.

Efforts to refine poverty measurement increasingly employ diverse data and machine learning methodologies.
Machine learning models present distinct advantages over econometric counterparts because they can mitigate
multicollinearity, achieve heightened accuracy, process data expeditiously, accommodate extensive datasets,
and minimize human involvement [10]. Furthermore, machine learning algorithms excel in feature selection

∗Corresponding author

erisalvador28@amherst.edu (E.L.V. Salvador)
linkedin.com/in/salvadorerika/ (E.L.V. Salvador)

ORCID(s): 0009-0003-2045-5459 (E.L.V. Salvador)

E.L.V. Salvador: Preprint submitted to Elsevier

Page 1 of 9

Predicting poverty via boosting algorithms

by automatically identifying relevant variables and capturing data relationships, even amidst nonlinearity or
obscured patterns [11]. Each variable’s impact on poverty is scrutinized during selection and favors those with
significant effects to construct models. These capabilities allow machine learning models to effectively handle
high-dimensional data and generate more accurate predictive models.

Only a limited number of studies have employed machine learning methods to address poverty in the
Philippines, utilized nationwide data from the Demographic and Health Survey (DHS) Program and compared
various these machine learning models. For example, one study [12] utilized geospatial data, including nighttime
lights and daytime satellite imagery, to model socioeconomic well-being, which achieved an R2 (goodness of fit)
of 0.63. Similarly, another study [13] used social media data, low-resolution satellite images, and volunteered
geographic information to map poverty, which obtained an R2 of 0.66 compared to 0.63 with satellite imagery
alone. These studies primarily relied on geospatial data. Conversely, another research [14] analyzed a dataset from
the Community-Based Monitoring System (CBMS) Database of Lagangilang, Abra, utilizing various models but
with only 13 features, where the Naive Bayes model yielded the best performance. Another related study [15]
applied K-means clustering and 17 features within a small, undisclosed community in the Philippines.

Significantly, a gap exists in the utilization and comparison of various machine learning methodologies
for assessing poverty in the Philippines. None of the previously mentioned studies explored extensive datasets
comprising hundreds of household characteristic features suitable for model estimation. While [12] utilized data
from the DHS, they focused on only four main features. Therefore, this study aimed to broaden poverty analysis
using machine learning techniques across an extensive dataset, working under less restrictive assumptions to
effectively identify low-income households. Furthermore, this research aimed to tackle the underutilization of
boosting algorithms in poverty prediction [16]. In fact, XGBoost is the sole boosting algorithm with a 14% usage
rate in a recent scoping review on machine learning and poverty prediction [17]. However, recent research indicates
that the family of boosting algorithms has expanded with several compelling proposals and boasts improvements in
both speed and accuracy [18]. As a result, this study sought to utilize a subset of boosting algorithms in predicting
poverty in the Philippines.

2. Data and Methods
2.1. Data Cleaning

The data for this study was obtained from the 2022 DHS in the Philippines. The original dataset consisted
of 2,099 features collected from 30,372 households. A threshold of 3,050 was assigned (Figure X) because most
features had fewer than 3,050 missing values. Columns exceeding the missing value threshold were removed, and
rows with any remaining null values were deleted. Furthermore, some interview-related logistic features, such as
the date of the interview, were manually removed. After this step, the dataset was reduced to 396 features from
2,099 features, and 20,679 households from 30,372 households.

Figure 1: Distribution of Missing Values across Features. Blue Line = 3,050

E.L.V. Salvador: Preprint submitted to Elsevier

Page 2 of 9

Predicting poverty via boosting algorithms

2.2. Data Partitioning

After data cleaning, the dataset underwent random partitioning, with 80% allocated for training and the
remaining 20% reserved for assessing model performance. Additionally, to optimize the model’s hyperparameters,
a validation set comprising 10% of the training set was required. This division was executed using a stratified
sampling technique.

2.3. Feature Scaling

Afterwards, scaling was implemented to ensure uniform scaling across all features. Binary features were left
unscaled, while numerical and ordinal features were scaled. First, the scaler was trained on the training data using
z-score normalization. The training data was then transformed according to these normalization parameters. Finally,
the same parameters were applied to the testing data. This ensured consistency and prevented data leakage.

2.4. Feature Selection

To address potential efficiency issues associated with an excessive number of features [11], the study employed
the SelectFromModel() method to identify significant features for each model. SelectFromModel is a feature
selection technique in scikit-learn that acts as a meta-transformer compatible with any estimator that evaluates
feature importance, such as decision trees or L1-norm regularized linear models. After evaluating all models, the
study tallied the frequency of each feature’s selection and identified those most frequently chosen as the final set of
selected features. This process resulted in the selection of 66 features deemed most relevant for predicting poverty.
Pearson’s Correlation Coefficient was applied to the subset of selected features to check for multicollinearity. For
pairs of features with a correlation coefficient of 0.8 or higher, the feature with the lower selection frequency
was removed. From the original 36 features initially selected via SelectFromModel(), the final count remained the
same, as there is minimal to no multicollinearity among them. These features, ranked by their frequency in the
SelectFromModel() results, are listed in Table 1.

Table 1: Description of Features

No. Feature
1

Source of drinking water

Type of toilet facility

Has television

Has refrigerator

Has bicycle

2

3

4

5

6

7

Description
Can take on 20 different values from ‘piped water’ (10), ‘tube
well water’ (20), ‘dug well’ (30), ‘surface from spring’ (40), and
more.

Can take on 17 values from ‘flush toilet’ (10), ‘pit toilet latrine’
(20), ‘no facility’ (30), and more.

Can take on values ‘yes’ (1) or ‘no’ (0).

Can take on values ‘yes’ (1) or ‘no’ (0).

Can take on values ‘yes’ (1) or ‘no’ (0).

Has motorcycle/scooter

Can take on values ‘yes’ (1) or ‘no’ (0).

Has car/truck

Can take on values ‘yes’ (1) or ‘no’ (0).

8 Main floor material

9 Main wall material

10 Main roof material

Can take on 15 different values from ‘natural’ (10), ‘rudimentary’
(20), ‘finished’ (30), and more.

Can take on 22 different values from ‘natural’ (10), ‘rudimentary’
(20), ‘finished’ (30), and more.

Can take on 18 different values from ‘natural’ (10), ‘rudimentary’
(20), ‘finished’ (30), and more.

11 Has telephone (landline)

Can take on values ‘yes’ (1) or ‘no’ (0).

12

Type of cookstove

Can take on 11 different values from ‘electric stove’ (1), ‘solar
cooker’ (2), ‘liquefied petroleum gas (LPG)/cooking gas stove’
(3), and more.

13

14

Share toilet with other households

Can take on values ‘yes’ (1) or ‘no’ (0).

Type of cooking fuel

Can take on 13 values from ‘alcohol/ethanol’ (1), ‘gaso-
line/diesel’ (2), kerosene/paraffin (3), and more.

E.L.V. Salvador: Preprint submitted to Elsevier

Page 3 of 9

Predicting poverty via boosting algorithms

No. Feature

Description

15

Location of toilet facility

16 Has watch

17 Has a computer

18 Has bank account

19

Type of light at home

Can take on 11 different values from ‘electric stove’ (1), ‘solar
cooker’ (2), ‘liquefied petroleum gas (LPG)/cooking gas stove’
(3), and more.

Can take on values ‘yes’ (1) or ‘no’ (0).

Can take on values ‘yes’ (1) or ‘no’ (0).

Can take on values ‘yes’ (1) or ‘no’ (0).

Can take on 16 different values from ‘electricity’ (1), ‘solar
lantern’ (2), ‘rechargeable flashlight’ (3), and more.

20 Has washing machine

Can take on values ‘yes’ (1) or ‘no’ (0).

21 Has air conditioner

Can take on values ‘yes’ (1) or ‘no’ (0).

22 Has gas range/stove with oven

Can take on values ‘yes’ (1) or ‘no’ (0).

23 Has microwave/toaster oven

Can take on values ‘yes’ (1) or ‘no’ (0).

24 Has audio component/karaoke

Can take on values ‘yes’ (1) or ‘no’ (0).

25 Has cable services

Can take on values ‘yes’ (1) or ‘no’ (0).

26

Tenure status of the housing unit

Can take on 7 values from ‘own or owner-like possession of the
house and lot’ (1), ‘own the house, rent the lot’ (2), ‘own the
house, rent-free lot with consent of the owner’ (3), and more.

27

28

Type of place of residence

Can take on values ‘urban’ (1) or ‘rural’ (2).

Time to get to water source (min-
utes)

Numerical value.

29 Has electricity

Can take on values ‘yes’ (1) or ‘no’ (0).

30 Number of rooms used for sleeping Numerical value.

31 Has mobile telephone

Can take on values ‘yes’ (1) or ‘no’ (0).

32 Mobile phone used for financial

Can take on values ‘yes’ (1) or ‘no’ (0).

transactions

33 Has induction stove

Can take on values ‘yes’ (1) or ‘no’ (0).

34 Has DVD player

Can take on values ‘yes’ (1) or ‘no’ (0).

35

Beneficiary of Pantawid Pamilyang
Pilipino Program (4Ps)

36 Observed place for handwashing

Can take on values ‘yes’ (1) or ‘no’ (0).

Can take on 6 different values from ‘observed, fixed facility
(sink/tap) in dwelling’ (1), ‘observed, fixed facility (sink/tap) in
yard/plot’ (2), ‘observed, mobile object (bucket/jug/kettle)’ (3),
and more.

2.5. Machine Learning Models

This study employed five boosting algorithms: Adaptive Boosting (AdaBoost), Cat Boosting (CatBoost),
Gradient Boosting Machine (GBM), Light Gradient Boosting Machine (LightGBM), and Extreme Gradient
Boosting (XGBoost). These models were chosen for their robustness and their ability to handle high-dimensional
data, which is crucial for a study that aimed to consider the multidimensional nature of poverty. To handle
class imbalance, the Synthetic Minority Over-sampling Technique (SMOTE) was employed on the training data.
Hyperparameter tuning was conducted both using manual trial and error and grid search on the validation data.
Table 2 showcases the hyperparameters for the project.

E.L.V. Salvador: Preprint submitted to Elsevier

Page 4 of 9

Predicting poverty via boosting algorithms

Table 2: Parameters for Different Gradient Boosting Algorithms

Algorithm
Adaptive Boosting (AdaBoost)

Cat Boosting (CatBoost)

Gradient Boosting Machine (GBM)

Light Gradient Boosting Machine (LightGBM)

Extreme Gradient Boosting (XGBoost)

Parameter
learning_rate
n_estimators

depth
iterations
learning_rate

learning_rate
max_depth
n_estimators

learning_rate
n_estimators
num_leaves

learning_rate
max_depth
n_estimators

Value
0.5
200

4
300
0.3

0.3
3
300

0.1
200
31

0.3
3
300

2.6. Performance Metrics

To evaluate the performance of various machine learning algorithms in predicting and classifying household
poverty levels, a range of performance metrics was calculated and compared to thoroughly evaluate the models.
The performance of each algorithm was assessed based on the average of the metrics. These metrics include:

Accuracy Score. The accuracy score is the ratio of correctly predicted instances to the total instances in the
dataset. It is calculated as the sum of true positives and true negatives divided by the total number of predictions:

Accuracy =

𝑇 𝑃 + 𝑇 𝑁
𝑇 𝑃 + 𝑇 𝑁 + 𝐹 𝑃 + 𝐹 𝑁

(1)

where TP represents true positives (i.e., poor households correctly identified as poor), TN represents true negatives
(i.e., non-poor households correctly identified as non-poor), FP represents false positives (i.e., non-poor households
incorrectly identified as poor), and FN represents false negatives (i.e., poor households incorrectly identified as
non-poor).

Precision Score. Precision measures the proportion of correctly predicted positive instances to the total

predicted positive instances. It is calculated as:

Precision =

𝑇 𝑃
𝑇 𝑃 + 𝐹 𝑃

(2)

Recall. Recall, also known as sensitivity or the true positive rate, measures the proportion of correctly predicted

positive instances to all actual positive instances. It is calculated as:

Recall =

𝑇 𝑃
𝑇 𝑃 + 𝐹 𝑁

(3)

F1 Measure. The F1 score is the harmonic mean of precision and recall and provides a balanced measure that

takes both into account. It is calculated as:

F1 Score = 2 ×

Precision × Recall
Precision + Recall

(4)

Area Under the Receiver Operating Characteristic Curve (AUC-ROC). The ROC, or Receiver Operating
Characteristic curve, plots the recall against the FP Rate (FPR) at various threshold settings. The AUC, or Area
Under the Curve, quantifies the overall performance of the model by calculating the area under the ROC curve,
with values ranging from 0 to 1. A model with an AUC closer to 1 indicates excellent performance and effectively
distinguishes between positive and negative classes, while an AUC closer to 0.5 suggests the model performs no
better than random guessing.

Confusion Matrix. A confusion matrix is a tabular representation of actual versus predicted classifications,
composed of true positives, true negatives, false positives, and false negatives. This matrix provides an overview
of model performance through helping identify specific types of classification errors. While the confusion matrix

E.L.V. Salvador: Preprint submitted to Elsevier

Page 5 of 9

Predicting poverty via boosting algorithms

provides detailed data, it can be less informative in high-dimensional problems with many classes and requires
careful interpretation to understand the significance of each component. Metrics like accuracy, precision, and recall
counterbalance the confusion matrix by summarizing these details into more interpretable forms.

The computational efficacy of various metrics in addition to traditional performance metrics above was also
examined. The computational efficacy was obtained by measuring the training time, testing time, and model size.
To capture these metrics, the time module was utilized to record the duration of training and testing processes, and
the memory_profiler library to monitor the memory usage and model size. These additional assessments provided
a comprehensive understanding of the efficiency and practicality of the models in real-world applications.

2.7. Tools and Libraries

The study employed various Python libraries and software for data analysis and machine learning operations.
Specifically, the study utilized NumPy (version 1.25.0) and pandas (version 1.5.1) for data manipulation and pre-
processing, seaborn (version 0.13.2) and matplotlib (version 3.6.0) for data visualization, and scipy (version 1.10.0)
for statistical analysis. For machine learning modeling and evaluation, the study used scikit-learn (version 1.4.2),
lightgbm (version 4.2.0), xgboost (version 1.8.0), and catboost (version 1.1.0). Additionally, memory_profiler
(version 0.61.0) was utilized to monitor and optimize memory usage during the implementation. These packages
are accessible via the website Python Package Index or through pip.

3. Results

The research employed five machine learning models on DHS data from the Philippines: Adaptive Boosting
(AdaBoost), Cat Boosting (CatBoost), Gradient Boosting Machine (GBM), Light Gradient Boosting Machine
(LightGBM), and Extreme Gradient Boosting (XGBoost). Wealth classification was approached as a five-class
problem (Richest, Richer, Middle, Poorer, Poorest). Each model was trained on 80% of the cleaned dataset and
evaluated on the remaining 20%. Hyperparameters were optimized using a validation set, which comprised 10%
of the training data, with performance assessed through metrics such as accuracy, precision, recall, and F1-score.
As shown in Table 3, the performance metrics for the five models were as follows: CatBoost achieved the highest
accuracy at 90.93%, followed by XGBoost at 89.41%, GBM at 89.05%, and LightGBM at 88.52%. AdaBoost had
the lowest accuracy at 80.39%. In terms of precision, CatBoost again ranked highest with 90.92%, followed by
XGBoost at 89.39%, GBM at 89.04%, and LightGBM at 88.51%, with AdaBoost recording a precision of 83.55%.
For recall, CatBoost led with 90.93%, while XGBoost had 89.41%, GBM showed 89.05%, and LightGBM was
close behind with 88.52%. AdaBoost had the lowest recall at 80.39%. Regarding the F1 score, CatBoost achieved
the highest at 90.92%, followed by XGBoost with 89.40%, GBM at 89.04%, and LightGBM at 88.50%, with
AdaBoost recording the lowest F1 score at 80.15%. The rankings of the models with respect to all metrics were
consistent: CatBoost was first, followed by XGBoost, GBM, LightGBM, and AdaBoost in that order. However, the
metric values for the top four models are remarkably similar, with only AdaBoost exhibiting significantly lower
performance metrics.

Table 3: Performance Evaluation Metrics of the Boosting Models

Accuracy Precision Recall
Model
0.803917
AdaBoost
0.909333
CatBoost
GBM
0.890474
LightGBM 0.885155
0.894101
XGBoost

0.835551
0.909193
0.890362
0.885137
0.893919

0.803917
0.909333
0.890474
0.885155
0.894101

F1 Score
0.801523
0.909191
0.890353
0.884996
0.893981

Meanwhile, Table 4 provides the AUC-ROC scores to assess the performance of different models in predicting
household poverty levels. For the "Poorest" class, CatBoost, GBM, LightGBM, and XGBoost achieved scores
around 0.98 to 0.99, while AdaBoost scored significantly lower at 0.90. This is reflected in the confusion
matrix for AdaBoost (Figure 1), which shows a higher number of misclassifications, particularly with true
"Poorest" instances being predicted as "Poorer" and some as "Richer." On the other hand, for the "Poorer" class,
CatBoost, GBM, LightGBM, and XGBoost all achieved high scores of 0.99, while AdaBoost scored lower at 0.73.
AdaBoost’s confusion matrix reveals significant misclassifications for the "Poorer" class, with many instances
being misclassified as "Poorest" or "Middle." In both classes, CatBoost, GBM, LightGBM, and XGBoost show
fewer misclassifications (FigureS 2.2-2.5), consistent with their higher AUC-ROC scores. For the "Middle" class,
all models demonstrated perfect performance with scores of 1.00, which is confirmed by their confusion matrices
showing almost no misclassifications for this class.

E.L.V. Salvador: Preprint submitted to Elsevier

Page 6 of 9

Predicting poverty via boosting algorithms

In the "Richer" class, CatBoost, GBM, LightGBM, and XGBoost again achieved perfect scores of 1.00, while
AdaBoost scored lower at 0.79. AdaBoost’s confusion matrix shows misclassifications for the "Richer" class,
with some instances being misclassified as "Poorer" or "Richest." Conversely, CatBoost, GBM, LightGBM, and
XGBoost showed strong performance with minimal misclassifications. Lastly, for the "Richest" class, CatBoost,
GBM, LightGBM, and XGBoost achieved near-perfect scores of 1.00, and AdaBoost scored slightly lower at 0.99.
The confusion matrix for AdaBoost shows a small number of misclassifications for this class, with some instances
predicted as "Richer."

Table 4: AUC-ROC Scores for Each Class Across the Boosting Models

Class
Poorest
Poorer
Middle
Richer
Richest

AdaBoost CatBoost GBM LightGBM XGBoost
0.98
0.99
1.00
0.99
1.00

0.98
0.99
1.00
0.99
1.00

0.99
0.99
1.00
0.99
1.00

0.90
0.73
0.99
0.79
1.00

0.98
0.99
1.00
0.99
1.00

Additionally, the study examined the models’ computational efficacy to assess the practical applicability of the
models. Recent research often neglects these metrics and focuses instead on previous benchmarks. Table 5 provides
the comparison of various models in terms of training time, testing time, and model size. AdaBoost stands out with
the shortest training time at approximately 4.48 seconds, making it the quickest model to train. However, it takes
the longest time for testing at 0.23 seconds. In contrast, CatBoost, while having the longest training time of 69.29
seconds and the largest model size at 30.50 MB, demonstrates exceptional efficiency during testing, taking only 0.01
seconds. GBM (Gradient Boosting Machine) shows moderate performance, with a training time of 16.81 seconds,
a testing time of 0.02 seconds, and a model size of 15.80 MB. LightGBM and XGBoost exhibit a good balance,
featuring relatively quick training times of 2.17 and 2.58 seconds, respectively, along with small model sizes of
2.50 MB and 3.10 MB. LightGBM takes slightly longer during testing at 0.07 seconds, compared to XGBoost’s
0.03 seconds.

Table 5: Computational Efficacy Metrics Across the Boosting Models

Metric
Training Time (seconds)
Testing Time (seconds)
Model Size (MB)

AdaBoost CatBoost GBM LightGBM XGBoost
16.81
0.02
15.80

69.29
0.01
30.50

4.48
0.23
1.20

2.58
0.03
3.10

2.17
0.07
2.50

4. Discussion

The evaluation of five machine learning models—AdaBoost, CatBoost, GBM, LightGBM, and XGBM—on
DHS data from the Philippines revealed that CatBoost consistently achieved the highest performance metrics,
including accuracy, precision, recall, and F1-score. XGBoost followed closely, with GBM and LightGBM also
demonstrating strong performance. AdaBoost lagged behind with the lowest performance across all metrics.
Moreover, AUC-ROC curves further validated the models’ discriminative capabilities in predicting household
poverty levels. CatBoost, GBM, LightGBM, and XGBoost achieved near-perfect AUC values across most
classes, particularly in distinguishing the "Poorest," "Middle," "Richer," and "Richest" classes. AdaBoost showed
significantly lower AUC scores, especially for the "Poorest" and "Poorer" classes, which was reflected in its
higher misclassification rates. In terms of computational efficiency, AdaBoost had the shortest training time but
the longest testing time. CatBoost required the longest training time and the largest model size but demonstrated
exceptional testing efficiency. GBM, LightGBM, and XGBoost balanced well between training and testing times,
with LightGBM and XGBoost also showing smaller model sizes.

Overall, CatBoost emerged as the top performer across all metrics, followed closely by XGBoost, GBM, and
LightGBM. AdaBoost, while efficient in training time, showed lower performance in accuracy, precision, recall,
and F1-score, as well as higher misclassification rates. LightGBM and XGBoost demonstrated a good balance of
high performance and computational efficiency, thus are strong candidates for practical applications.

This study also highlighted the most impactful features in predicting poverty through the feature selection
method, as outlined in Table 1, indirectly suggesting potential areas for policy focus. Future research could model
how changes in these features affect predicted poverty classes explicitly. These findings have global implications

E.L.V. Salvador: Preprint submitted to Elsevier

Page 7 of 9

Predicting poverty via boosting algorithms

Figure 2: Figures 2.1-2.5 (From Left to Right): Confusion Matrices for AdaBoost (Fig 2.1), CatBoost (Fig 2.2), GBM
(Fig 2.3), LightGBM (Fig 2.4), and XGBoost (Fig 2.5).

for poverty alleviation efforts. Policymakers can gain more accurate insights into poverty dynamics and develop
targeted interventions addressing the multifaceted nature of poverty by utilizing machine learning techniques.
However, the limitations in this study, such as the reliance on DHS data and the need for further validation
using alternative datasets or methodologies must be acknowledged. Therefore, incorporating more complex types
of information for analysis and poverty prediction is necessary. Combining GPS data with survey data, for
instance, could significantly enhance the accuracy of poverty level classification in the Philippines. Utilizing
more sophisticated information, such as GPS data, night light data, and other advanced metrics, could improve
the precision of poverty predictions.

E.L.V. Salvador: Preprint submitted to Elsevier

Page 8 of 9

Predicting poverty via boosting algorithms

5. Conclusion

This study demonstrated the effectiveness of machine learning boosting algorithms, particularly CatBoost,
in predicting household poverty levels in the Philippines. CatBoost emerged as the top performer by offering
high accuracy and computational efficiency. However, AdaBoost lagged behind in performance metrics. Feature
selection highlighted areas for potential policy intervention. Overall, this research contributes development to
poverty alleviation efforts through the utilization of advanced technology.

6. Bibliography

References
[1] World Bank. Poverty overview: Development news, research, data, April 2024. Retrieved May 1, 2024, from https://www.worldbank.

org/en/topic/poverty/overview.

[2] Katharina Shulla, Benedikt F. Voigt, Sabin Cibian, Giovanni Scandone, Elena Martinez, Filip Nelkovski, and Pegah Salehi. Effects of

covid-19 on the sustainable development goals (sdgs). Discover Sustainability, 2:1–19, 2021.

[3] Michael Riegner. Implementing the data revolution for the post-2015 sustainable development goals: Toward a global administrative law

of information. World Bank Legal Review, 7:17, 2016.

[4] Merilee S. Grindle. Good enough governance: Poverty reduction and reform in developing countries. Governance, 17:525–548, 2004.
[5] Benoit Decerf. A preference-based theory unifying monetary and non-monetary poverty measurement. Journal of Public Economics,

222:104898, 2023.

[6] Jose Ramon G. Albert. [analysis] on poverty lines and counting the poor, May 2023. Retrieved from https://www.rappler.com/

voices/thought-leaders/228230-analysis-poverty-lines-counting-poor-filipino.

[7] Karen Joyce Briones, John Lopez, Ron Joseph Elumbre, and Timothy Miguel Angangco. Income, consumption, and poverty measurement

in the philippines, 2021. Retrieved from https://mpra.ub.uni-muenchen.de/106025/.

[8] Sabina Alkire, Jose Manuel Roche, Paola Ballon, James Foster, Maria Emma Santos, and Suman Seth. Multidimensional poverty

measurement and analysis. Oxford University Press, USA, 2015.

[9] Dorothy Watson, Christopher T. Whelan, Bertrand Maître, and James Williams. Non-monetary indicators and multiple dimensions: The

esri approach to poverty measurement. The Economic and Social Review, 48(4):369–392, 2017.

[10] G. Shobana and K. Umamaheswari. Forecasting by machine learning techniques and econometrics: A review. In 2021 6th International

Conference on Inventive Computation Technologies (ICICT), pages 1010–1016. IEEE, 2021.

[11] Jundong Li, Kewei Cheng, Suhang Wang, Fred Morstatter, Robert P. Trevino, Jiliang Tang, and Huan Liu. Feature selection: A data

perspective. ACM Computing Surveys (CSUR), 50(6):1–45, 2017.

[12] Isaiah Tingzon, Abigail Orden, Keane Teruel Go, Selena Sy, Vedran Sekara, Ingmar Weber, and Dong Kim. Mapping poverty in the
philippines using machine learning, satellite imagery, and crowd-sourced geospatial information. In The International Archives of the
Photogrammetry, Remote Sensing and Spatial Information Sciences, volume 42, pages 425–431, 2019.

[13] Carla Ledesma, Omar Laurente Garonita, Leonardo Jay Flores, Isaiah Tingzon, and Delia Dalisay. Interpretable poverty mapping using

social media data, satellite images, and geospatial information, 2020. arXiv preprint arXiv:2011.13563.

[14] John Arlo Talingdan. Performance comparison of different classification algorithms for household poverty classification. In 2019 4th

International Conference on Information Systems Engineering (ICISE), pages 11–15. IEEE, 2019.

[15] Maria Pilar Repollo, Renier Aurelius, and Carl Robielos. Applying clustering algorithm on poverty analysis in a community in the

philippines. In IEOM Society International, pages 1511–1521, 2021.

[16] Qiang Li, Sherry Yu, Damien Échevin, and Ming Fan. Is poverty predictable with machine learning? a study of dhs data from kyrgyzstan.

Socio-Economic Planning Sciences, 81:101195, 2022.

[17] Aigul Usmanova, Azeddine Aziz, Dostonbek Rakhmonov, and Walid Osamy. Utilities of artificial intelligence in poverty prediction: a

review. Sustainability, 14(21):14238, 2022.

[18] Christophe Bentéjac, András Csörgő, and Guillermo Martínez-Muñoz. A comparative analysis of gradient boosting algorithms. Artificial

Intelligence Review, 54:1937–1967, 2021.

E.L.V. Salvador: Preprint submitted to Elsevier

Page 9 of 9

