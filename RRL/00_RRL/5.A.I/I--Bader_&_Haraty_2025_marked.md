International Journal of Computing and Digital Systems
2025, VOL. 18, NO. 1, 1–19

http://dx.doi.org/10.12785/ijcds/1571107231

Bridging AI and Emotion: Enhanced Models for Personal
Finance Manager Applications

Samir Bader 1 and Ramzi A. Haraty2

1 Department of Computer Science and Mathematics, Lebanese American University, Beirut, Lebanon

Received 6 June 2024, Revised 22 March 2025, Accepted 22 March 2025

Abstract: paper focuses on creating and deploying an innovative Financial Advisor Application that would revolutionize conventional
financial planning methods with the help of state-of-the-art artificial intelligence tools and effective financial services. Indeed, the
essence of this application is user-oriented and focuses on creating more ways to engage the user and help make the right decisions
by redesigning the interface and providing individualized financial guidance. The application combines different aspects of financial
management, including budgeting, transaction tracking, and goal setting, but also sees novelties as an artificial intelligence function that
detects anomalies in transactions and the merchant offers explicitly created for clients. The technical structure involves access to data,
the description of each module, and the use of AI that provides anticipatory analysis and tools for advanced financial planning. Business
testing and vulnerability assessments were performed proving the business value and reliability of the application; thus, avoiding data
leakage and modularity viruses. The work assesses the effects on the users’ satisfaction when provided with such technologies and
their ability to change their financial management behaviour; therefore, providing an exhaustive scenario of the credentials of AI for
improving the efficacy of financial advisory. The conclusions released in the paper should advance knowledge of financial technology
as it demonstrates how the intelligent systems used in a presented application can lead to noteworthy improvements for both users and
financial companies.

Keywords: AI, Anomaly Detection, Financial Planning, Fintech, and Sentiment Analysis

1. INTRODUCTION

users.

The Financial Advisor Application is a perfect example
of the synergy of highly developed IT solutions and pro-
found financial knowledge in the constantly evolving field
of fintech. This application revolutionizes personal finance
management by utilizing advanced AI along with a plethora
of financial products and services that are unique to the
clients. Unlike traditional instruments that work indepen-
dently of one another, this platform offers a global picture
of a person’s financial status and provides recommendations
and solutions.

Due to the advanced semantic AI, the Financial Advisor
Application is proficient
in identifying users’ emotions
regarding financial activities and textual information. This
advanced feature allows the application to provide more
personalized financial advice and emotional support, mak-
ing the financial management process more accessible and
sensitive. As the program determines the user’s emotional
state when making financial decisions, the application offers
recommendations that match the feelings and objectives of
the user; thus, increasing the interest and satisfaction of

E-mail address: rharaty@lau.edu.lb, samir.bader@lau.edu

Also, constant transactions are controlled by the appli-
cation through highly developed anomaly detection algo-
rithms. This security feature quickly detects any suspicious
activity associated with fraudulent activities; thus, protect-
ing users’ financial resources. The anomaly detection ability
protects the money and makes users aware of standard
spending patterns to avoid risking their money.

Apart from these features,

the application also cus-
tomizes the shopping experience by identifying the mer-
chants with whom the users have transactions. This fea-
ture provides a user-friendly experience and can save the
most money by recommending discounts and promotions
from associated sellers. As a result, the Financial Advisor
Application dictates that users get only the best deals
by considering past purchases and preferences, promoting
financial optimality and customer happiness. It questions the
conventional business models of financial consulting and
modernizes the principles of the personal finance industry.
It gives an insight
into the prevailing position of the
application of AI in the financial sector, which opens up

2

First Author, Samir Bader. Second Author, Ramzi Haraty

future financial decision-making as informative, inclusive,
and innovative. When reflecting on the possibilities and
features of the Financial Advisor Application, it is crucial to
realize that this is not merely an application but a financial
assistant that helps users in their economic endeavors with
accuracy and wisdom.

A. Problem Statement

This desire for more effective tools to extend financial
consultancy with the help of the internet and mobile appli-
cations highlights the necessity of stable methods to develop
individual, particular approaches for every user. Most con-
temporary approaches to managing financial and accounting
activity are based on fixed structures that ignore essential
data, such as general user behavior and attitude needed to
define what kind of recommendations the administrators
should give. The problem is that these applications become
mere carriers of simple data transfers and cannot analyze
user data such as frequency, mood, and preferences crucial
to providing timely financial assistance [1-3].

Today’s financial platforms can process structured data
effectively, they cannot extract as much value as from the
unstructured data that stems from inputs about the users
and descriptions of the transactions [1]. This can lead to
recommending other products or services that the user does
not need or cannot handle emotionally; thus, limiting the
possibility of positive interaction and satisfaction. Specifi-
cally, it has been found that studies on concrete applications
of the soft computing paradigms, like the applications with
semantic analysis or the applications that include adaptive
learning mechanisms, help solve the problems of financial
advising. However, the practical application of these com-
plex methods requires effort.

Regarding the above issue, an effective approach for
improvement is to combine TensorFlow and Keras with a
Python environment. This integration will help the applica-
tion learn the users’ activities and preferences by integrating
semantic AI and M-learning solutions. So, achieving these
objectives will facilitate the receipt and analysis of transac-
tional data such as the number of transactions, the frequency
of transactions, the currency, and any other quantitative
indicators. It will also process inputs that contain quality or
quantity data, such as the quantity of product, the quality
of material, and so on. The knowledge of the users’ re-
quirements will be constructed by applying artificial neural
networks in this application. This functionality can give
general information concerning financial conduct and give
particular recommendations depending on the user’s data,
significantly increasing user satisfaction.

This study seeks to fill the gap between conventional fi-
nancial advisory platforms and advanced AI-based solutions
by developing a financial advisor application that analyzes,
comprehends, and responds to each user’s economic story.
This approach solves the crucial problem of improving the
quality and effectiveness of digital services’ financial rec-
ommendations, which raises users’ confidence in financial

planning applications.

B. Scope of the Work

This work is wholly devoted to the user. Our vision is to
create a highly sophisticated Financial Advisor Application
as a service and a sidekick in the financial life. This work
involves leveraging the features of NET Core 6 to design an
extremely robust and highly scalable application. We have
integrated advanced features of AI in Python, which are
generally used for deep learning, such as anomaly detection,
consecutive transaction prediction, and semantic analysis
[2]. By using this diverse approach, we aim to enhance a
user’s experience by providing timely and accurate informa-
tion on managing money. This project has been developed
with the needs of user experiences in mind.

It

is also not simply a matter of incorporating the
different and complex aspects of modern financial advisory
services’ features into the application’s architecture. It is
about developing a framework that is open and capable of
changing according to the conditions of the field. Abstract
classes define the application structure, and this decision
makes it possible to add new features and change the prod-
uct’s behavior without affecting its essential characteristics
by third parties.

Implementing AI and machine learning into the appli-
cation is not just a technicality. It’s a strategic decision
to address three primary objectives: anomaly detection for
better transaction security, predictive analysis for better fi-
nancial decisions, and semantic analysis for better financial
planning advice.

Among them, the most important is to develop and
optimize deep learning models for detecting anomalies in
financial transactions. Python and other necessary machine
learning libraries will be used to create the application that
will assist in identifying suspicious activity and increasing
transaction security. We know how critical security and
reliability are in financial applications and strive to provide
you with a product you can rely on.

To develop predictive models for financial forecasting:
The application will analyze historical financial data and
the user’s transaction history to predict specific financial
outcomes. This will empower users to make informed and
accurate economic decisions.

To incorporate semantic analysis for understanding user
sentiment and behavior,
the application will use NLP
techniques to better understand user inputs and feedback
and provide more accurate and practical financial planning
recommendations based on the client’s emotional status.

The research questions guiding the development of this

application are:

•

In what ways can deep learning models be used to
solve the problem of identifying anomalous transac-

International Journal of Computing and Digital Systems

3

tions? NET Core 6 environment?

• What methods can be used to effectively forecast
financial patterns and users’ actions based on trans-
actional data using Python-based AI tools?

C. Research Objectives

This work aims to bridge the gap between conven-
tional financial advisory platforms and advanced AI-driven
solutions by developing a sophisticated Financial Advisor
Application. The key objectives of this research are:

• Enhancing Financial Security – Develop and optimize
deep learning models for detecting anomalies in fi-
nancial transactions, improving transaction security
through AI-driven anomaly detection techniques.

• Predictive Financial Analysis – Create predictive
models that analyze historical financial data and user
transaction histories to forecast financial trends and
empower users with informed decision-making.

• AI-Powered Financial Planning – Incorporate seman-
tic analysis and natural language processing (NLP) to
understand user sentiment and behavior, enabling the
application to provide personalized financial advice
based on users’ emotional and financial conditions.

D. Research Contributions

This work contributes to the field of AI-driven financial

advisory systems by:

• Developing a Scalable and Adaptive AI-Driven Fi-
nancial Advisory Framework – The application ar-
chitecture is designed with abstract classes, enabling
adaptability and extensibility in financial advisory
services.

•

Integrating Advanced AI Techniques for Financial
Advisory Services – By leveraging deep learning for
anomaly detection, predictive analytics, and semantic
analysis, this study enhances the accuracy and relia-
bility of financial recommendations.

• Enhancing Transaction Security in Digital Financial
Services – Implementing anomaly detection tech-
niques helps identify suspicious activities, increasing
users’ confidence in financial applications.

•

Improving User-Centric Financial Advisory Services
– The application’s NLP-based semantic analysis tai-
lors financial advice to users’ emotional and financial
states, providing a more intuitive and personalized
experience.

The rest of the paper is organized as follows: Section
2 provides the literature review. Section 3 describes the
methodology of the work. Section 4 presents the experimen-
tal results and section 5 supplies a discussion of the results.

And finally, section 6 concludes the paper and provides
future directions.

E. Selecting a Template (Heading 2)

First, confirm that you have the correct template for your
paper size. This template has been tailored for output on the
21cm X 28cm Paper Size.

F. Maintaining the Integrity of the Specifications

The template is used to format your paper and style
the text. All margins, column widths, line spaces, and text
fonts are prescribed; please do not alter them. You may note
peculiarities. For example, the head margin in this template
measures proportionately more than is customary. This mea-
surement and others are deliberate, using specifications that
anticipate your paper as one part of the entire proceedings,
and not as an independent document. Please do not revise
any of the current designations.

2. LITERATURE REVIEW

The spread and development of fintech have fostered fur-
ther development of new applications that would contribute
to the simplification of financial transactions and increase
the accuracy and personalization of the offered financial
recommendations. Among these innovations, the Financial
Advisor Application is one of the best
integrated and
sophisticated applications in the world of technology. This
paper aims to provide a literature review to establish the
essential technologies and critical applications that define
this revolutionary application. This new financial advisory
tool combines contemporary computational techniques with
traditional but customized services.

A. Comprehensive Financial Overview

The application gives users a summary of the financial
situation, combining the data from several accounts and
the asset summary, liability, expenditure, and savings plan.
Users can make sound financial decisions by offering pre-
cise and concise financial decisions since the application
provides a clear and concise financial picture. This feature
corresponds with Anderson, who states that data integration
and visualization play a crucial role in improving user
experience and their decision-making process [1].

B. Technological Base and Management Framework

As stated earlier, the basis of the described Financial
Advisor Application is the use of .NET Core — a decision
that signals the readiness to build solid and scalable apps
[3]. NET Core is a highly adaptive, fast, and secure platform
crucial for financial applications involving users’ data. It
ensures that complex capabilities are closely integrated
and the application will not slow down or have issues
with various loads. This is especially the case within the
financial services industry, where the accuracy of data and
its authenticity cannot be compromised.

It is integrated with NET Core, and the application
utilizes Python’s AI features, including TensorFlow and
Keras. These libraries are among the most advanced tools

4

First Author, Samir Bader. Second Author, Ramzi Haraty

for deep learning, which can analyze enormous amounts of
information successfully and search for valuable informa-
tion. Consequently, the use of the two has become mixed up.
NET Core for structure and Python for intelligent operations
are the best pairs that bring high efficiency and intelligence
to the Financial Advisor Application.

C. Future Directions and Research Opportunities

Thus, the application of AI in financial advisory services
offers many potential research avenues, especially regarding
the protection of users’ data,
the usage of responsible
AI, and the suitability of AI in financial decision-making.
Future research could focus on the effects of real-time data
analysis on economic forecasting, the utilization of AI to
improve financial awareness, and how best to increase the
degree of customization of financial advice using more
sophisticated machine learning algorithms.

Moreover,

the application’s architecture and features
allow for integrating quantitative and qualitative sentiment
analyses of financial statements. Thus, perpetuating the
integration of these elements can lead to further efficiency
and customization in economic consulting.

The Financial Advisor Application is a new generation
of personal finance management tools that incorporate the
best features. Based on NET Core 6 and AI technologies
developed using Python, it will be possible to provide users
with a powerful, safe, and highly customized experience [3].
The application stands out from other financial technology
applications through its capacity to predict trends, identify
deviations from standards, and analyze user sentiment.
The continued advancement of the application will give a
glimpse of the possibilities and difficulties of using AI in
delivering effective and efficient financial services to users,
propelling the development of better and more effective
user-oriented financial technologies.

D. The Relationship between Deep Learning and Machine

Learning
The programming tools most useful for machine learn-
ing in Python are TensorFlow and Keras, which can predict
financial trends, detect anomalies, and analyze semantics
[7-8]. These capabilities enable the application to detect
transaction patterns, predict
the users’ future economic
activities, and ascertain their needs. RNNs will do the data
analysis, and insights and recommendations will be given
with the help of data analysis. However, very subtle patterns
in the data may not be easily detected.

Substantial evidence suggests that machine learning
models should be incorporated into financial forecasting.
For example, models help predict market trends and identify
patterns humans may not notice. These capabilities are
crucial for creating a predictive financial advisory setting
that responds to the user’s data shift.

E. Customization and Extensibility

When it comes to extensibility and customization, the
application’s architecture, especially the usage of abstract

classes, serves as a guideline [4]. This architectural decision
enables third-party developers and financial institutions to
extend the application’s core functionalities to suit different
needs while not risking the overall integrity of the appli-
cation [5]. It is a strategic move that centralizes the needs
of a global user base and the required financial regulations,
languages, and operational customizations

This flexibility is essential to keeping the application
up to date and effective in a rapidly evolving financial
environment provided by abstract classes. This aligns with
research by Tertilt and Scholz, who postulated that financial
solutions must be flexible enough to suit users’ needs.

F. Personalized Financial Advice

Personalization is the foundation of the Financial Ad-
visor Application’s proposition. As such, the application
can provide recommendations consistent with the user’s
spending patterns and financial objectives through semantic
analysis and predictive models. Whether it is about saving
money, investing money, or even planning for the bud-
get, the application is designed to help according to the
particularity of the user. This level of personalization is
accomplished through learning and development to ensure
that the advice is helpful and efficient in the future.

G. AI-Driven Merchant Recommendations

For better user experience and more savings, the Fi-
nancial Advisor Application also uses Artificial Intelligence
to analyze users’ transaction history and suggest merchant
offers. This not only helps the consumer by making the
experience more personal and tailored to their needs but
also helps them save money with discounts and sales from
the partnered vendors. The application also employs user
data and artificial intelligence to provide users with the
most enriching offers, thus giving value to their financial
operations.

H. AI Predicting Trends

It has been proved that AI can perform very well in
predictive solutions across different domains, particularly fi-
nancial platforms. Historical data are significant because AI
computers can find hidden patterns that human analysts may
otherwise ignore. Deep learning and neural networks have
been critical in helping identify these patterns. For instance,
Rezaei et al. have described how deep learning algorithms
can perform the stock market’s future downtrends with a
high accuracy level, which can be helpful for investment
[6].

I. AI in Other Fields

Although AI is particularly incorporated in finance, it
resonates in multiple industries. In healthcare, AI algorithms
are used for outbreak prediction and deep learning is utilized
to design individual patients’ care plans [7]. In the same
way, in retail, AI is used to keep track of the stock and make
recommendations to customers [8]. These advancements
also indicate that AI has the unique ability and capacity
to tailor applications to revolutionize several industries and
sectors [14-16].

International Journal of Computing and Digital Systems

5

J. AI and Sentiment Analysis

Considering the growing popularity of AI applications
in various industries, it is paramount to explore customer
sentiment analysis. It typically marks text mining techniques
that seek to identify the tone of opinion users express.
This technique finds broader usage in the financial world
for ascertaining the market mood from news articles and
tweets. A listing by Bollen et al. [9] revealed that the mood
on Twitter could affect the movements of the stock market,
making sentiment analysis crucial in market analysis.

K. Behavior Prediction

Customer behavior prediction using artificial

intelli-
gence includes identifying patterns and definitions of behav-
ior to make assumptions about the likely behavior of cus-
tomers in the foreseeable future. This is particularly helpful
in marketing with personalized segments and customer
maintenance programs. For instance, there are behavioral
prediction models to determine which customers are most
likely to churn, so businesses can take preventive measures
[8]. This capability is also essential in processing financial
expenditure since spending behaviors can provide valuable
insights into financial management advice [10].

L. Forecasting

AI has enormously changed the different sectors through
the foresighted analysis of the data collected. Some models,
such as the LSTM and N-BEATS, have been used in
finance studies, as shown in the time series forecasting.
Such models can deal with intricate data patterns and offer
robust prediction, which can help make decisions [11].

Therefore, there is enough ground for integrating ma-
chine learning models in financial forecasting. For instance,
models aid in comprehending attitudes and climates that
humans may not discern inherently. These capabilities are
essential for constructing an accurate advisory financial
environment that adapts to the alteration of data mentioned
by users [12].

M. AI in Natural Language Processing

The developments in natural language processing (NLP)
have contributed immensely to improving the capability and
capacity of various forms of AI to interpret and create nat-
ural languages. These enhancements have ensured a better
handling of user interactions and an excellent sentiment
analysis. It is essential to discuss deep learning trends in
NLP, the progress made, and the future that may lie ahead
for these technologies, which was addressed by Young et
al. in the perspective of 2018 [13].

N. AI in Financial Advisory and Planning

Recent research underscores the transformative impact
of AI in financial advisory systems. For example, Wang
et al. [14] explored the use of generative AI for dynamic
portfolio optimization, demonstrating how reinforcement
learning algorithms can provide real-time investment strate-
gies. Similarly, Patel and Kumar [15] investigated AI-driven

budget planning tools that leverage predictive analytics to
anticipate users’ future financial needs based on historical
data, showcasing improved financial decision-making out-
comes.

AI’s ability to detect anomalies in financial transactions
has also been a focal point. Lee et al. [16] developed a
machine learning framework for fraud detection in dig-
ital payments, combining deep learning techniques with
anomaly detection algorithms. Their results revealed higher
accuracy in identifying fraudulent transactions compared to
traditional methods. Additionally, a study by Ramachandran
et al. [17] highlighted the integration of AI with blockchain
to enhance transparency and security in financial systems.

O. Sentiment Analysis in Fintech

Sentiment analysis has become a pivotal tool in un-
derstanding consumer behavior and market trends. A re-
cent study by Chen et al. [18] examined the integration
of sentiment analysis into mobile banking applications.
By analyzing customer feedback and app usage patterns,
their AI model provided personalized recommendations and
improved customer satisfaction rates. Another noteworthy
contribution by Gupta et al. [19] focused on combining
sentiment analysis with transaction data to offer tailored
merchant recommendations, emphasizing the importance of
contextual understanding in fintech applications.

P. Advanced Machine Learning Models for Sentiment

Analysis
The application of advanced machine learning models
has pushed the boundaries of sentiment analysis in fintech.
Transformer models, such as BERT and GPT, have been
widely adopted for their superior language understanding
capabilities. For instance, Sun et al. [14] demonstrated
the use of fine-tuned BERT models in analyzing customer
reviews for predicting product success in financial market-
places. Similarly, the study by Iqbal et al. [20] showcased
the effectiveness of TCN and N-BEATS models in com-
bining time-series data with sentiment analysis to predict
financial trends.

In 2024, Johnson et al. introduced a hybrid model that
integrates sentiment analysis with knowledge graphs for
financial decision support systems. This approach allowed
for a more comprehensive understanding of user behavior
and preferences, enhancing the personalization of financial
recommendations [21].

Q. Challenges and Future Directions

While recent advancements are promising, challenges
remain in deploying AI and sentiment analysis in fintech.
Scalability issues, data privacy concerns, and the complexity
of unstructured data processing continue to be significant
hurdles. Several studies,
including Sharma et al. [22],
highlighted the need for more robust frameworks to address
these challenges, particularly in real-world deployments.

6

First Author, Samir Bader. Second Author, Ramzi Haraty

ments, fund transfers, and withdrawals.

2) Merchant Data – Contains information about mer-
chants associated with user transactions, including
vendor type,
transaction frequency, and discount
eligibility.

3) Account Data – Covers financial account details,
including balance history, account type (checking,
savings, credit), spending trends, and income pat-
terns.

4) These data inputs are pre-processed and normalized
before being fed into the system’s analytical models.

C. Processing and Analysis

The core of the system architecture consists of three AI-
driven analytical components, which process the input data
and extract meaningful financial insights:

Anomaly Detection (Fraud Detection and Unusual

Spending Patterns)

•

Implemented using TensorFlow and Keras deep learn-
ing frameworks, the anomaly detection model evalu-
ates transaction data to detect irregular patterns.

• Techniques such as Isolation Forests, One-Class
SVM, and Autoencoders are used to identify fraudu-
lent transactions, unauthorized spending, or financial
distress signals

• The model assigns an anomaly score to each trans-
action, flagging suspicious activity for further review
or intervention.

D. Sentiment Analysis (User Mood and Financial Behavior)
• Employs natural language processing (NLP) and deep
learning models (LSTMs, Transformers) to assess
user sentiment from transaction patterns and spending
habits.

• Uses emotional indicators derived from transaction
data to determine financial well-being (e.g., stress-
related spending, impulse purchases, or conservative
financial behavior).

• Outputs an emotional score that helps tailor financial
advice based on the user’s current financial mood.

E. Predictive Modeling (Financial Forecasting and Person-

alized Recommendations)
• Utilizes advanced predictive analytics models such
as Transformers, Temporal Convolutional Networks
(TCN), and N-BEATS to analyze transaction history
and forecast future financial behaviors.

• The model generates personalized financial forecasts,
such as expected cash flow, potential budget deficits,
and optimal saving strategies.

Figure 1. Architecture of the application

3. METHODOLOGY

This study employs a data-driven approach that inte-
grates machine learning (ML) and artificial intelligence (AI)
techniques to provide personalized financial advice based on
users’ banking transactions. The primary objectives of this
approach are:

• Understanding Customer Behavior and Sentiment –
Utilizing sentiment analysis to assess users’ financial
moods, spending tendencies, and emotional states that
may impact financial decisions.

• Detecting Anomalies in Financial Transactions –
Implementing anomaly detection models to identify
unusual transaction patterns, such as potential fraud,
unexpected spending habits, or financial distress.

• Generating Personalized Merchant Discounts and Fi-
nancial Recommendations – Leveraging predictive
analytics to recommend financial products, savings
strategies, or tailored merchant discounts based on
transaction history and user behavior.

To achieve these objectives, the methodology incorpo-
rates semantic analysis, predictive modeling, and anomaly
detection as core analytical components [4]. The system
leverages advanced deep learning models, natural language
processing (NLP), and statistical algorithms to provide
highly accurate and real-time financial insights.

A. Architecture

The system architecture, illustrated in Figure 1, is de-
signed to seamlessly integrate multiple data streams, apply
sophisticated AI-based analytics, and generate personalized
financial recommendations. The architecture consists of
several key components, each responsible for distinct stages
of data processing and decision-making.

B. Data Inputs and Sources

1) Transaction Data – Includes all financial transactions
conducted by the user, such as purchases, bill pay-

• The system also integrates sentiment-aware financial
predictions, improving forecasting accuracy by 25

International Journal of Computing and Digital Systems

7

F. Backend System and Data Integration

Acts as the integration hub for all analytical components
resulting from the backend system, developed in .NET Core
6.

• The backend system, developed in .NET Core 6, acts
as the integration hub for all analytical components.

• Ensures real-time data flow between the anomaly
detection, sentiment analysis, and predictive modeling
layers.

• Manages user authentication, data security, and API
communication for seamless interaction with financial
institutions and third-party services.

G. Personalized Financial Recommendations

The insights generated by the analytical components are

processed to provide tailored financial advice and alerts:

Figure 2. MCC dataset

• Budgeting Recommendations – Users receive per-
sonalized suggestions on how to optimize spending,
avoid unnecessary expenses, and improve savings.

• Transaction Security Alerts – Users are notified of
suspicious transactions, with recommendations on
how to respond.

• Merchant Discounts & Financial Product Offers –
Based on spending habits, users receive customized
discount offers or financial product suggestions (e.g.,
credit card rewards, high-yield savings accounts).

4) User Notification & Actionable Insights – Financial
recommendations, security alerts, and budget sug-
gestions are presented to users through the UI.
5) Feedback Loop & Model Optimization – The system
continuously learns from user interactions, refining
its prediction accuracy and recommendation preci-
sion over time.

J. Dataset

The dataset was aggregated from bank transaction logs,
which were processed and analyzed to extract meaningful
insights. The data sources include:

The recommendation engine operates in real-time, en-

suring that users receive timely and actionable insights.

• Bank Transaction Records: Historical records of fi-

nancial transactions conducted by users.

H. User Interface and Integration

• Front-end application (Web/Mobile): Provides an in-
tuitive user experience, displaying financial insights,
risk alerts, and recommended actions.

• Merchant Category Code (MCC) Classification: Stan-
dardized categories assigned by Visa and Mastercard
to classify businesses based on their primary services
as depicted in figure 2.

•

Interactive Features: Users can adjust financial goals,
explore alternative budgeting strategies, and receive
AI-driven assistance.

• Merchant Data and Demographics: Additional details
about businesses where transactions were made, in-
cluding industry type and transaction frequency.

• Visual Analytics: Includes graphs and dashboards il-
lustrating spending patterns, anomaly detections, and
future financial projections.

I. System Flow and Execution Pipeline

1) Data Collection & Pre-Processing – The system
gathers and cleans transaction, merchant, and ac-
count data.

2) AI-Based Analytics Execution – Data is processed
through the anomaly detection, sentiment analysis,
and predictive modeling components.

3) Backend Processing & Decision Making – The
backend system integrates AI-generated insights and
determines appropriate recommendations.

K. Transaction Data

dbo.Customer Cards,

dbo.Extratransactions,
dbo.fina SubCategory,
dbo.fin goal
dbo.fin Budget, dbo.Budget Category.

fin MainCategory,

dbo.Extraaccounts,
dbo.fin Category,
dbo.fin MainCategory,
dbo.fin Goals,

Description: Detailed records of user transactions, in-
cluding transaction amount, date, and MCC codes. These
transactions span various categories like dining,
travel,
retail, and more, providing a comprehensive view of user
spending.

8

First Author, Samir Bader. Second Author, Ramzi Haraty

Figure 3. The dashboard

Figure 4. Suggestion’s box

L. Merchant Data

Tables:

dbo.Merchant List,

dbo.Merchant Suggestion,
dbo.Merchant Promotion,
dbo.Merchant Category, dbo.CustomerType Merchant.

dbo.Merchants,
dbo.Merchant GiftCard,
dbo.Merchant Rewards,

Description: Information about merchants categorized
by Visa and Mastercard. This includes details about the
types of merchants frequented by users and the offers
available.

Use Case: Helps provide personalized merchant recom-
mendations and discounts based on user transaction history.
Figure 4, provides suggestions for the user, and figure 5
shows the merchant’s box.

M. Account Data

Tables:

dbo.Extraaccounts,

dbo.Customer user,
dbo.Extratransactions, dbo.Finance Budget, dbo.Budget,
dbo.CardsProducts, dbo.CardsTypes, dbo.Cards Cashback.

Description: Includes data about users’ account balances
and activities, such as savings, checking, and investment ac-
counts. Monitoring these accounts helps in setting realistic
financial goals and budgeting.

Use Case: Essential for creating comprehensive user
profiles and providing accurate financial advice. Figure 6

Figure 5. Merchants box

Figure 6. Spending behavior chart

shows the spending behavior.

N. User Profiles

Tables:

do.Customers

do.Customer user,

dbo.PersonalInfo.

Description: Detailed profiles for each user, combin-
ing their transaction history and account data, including
demographic information, spending habits, income levels,
and financial goals. Use Case: Provides the foundation for
personalized financial advice and recommendations.

O. Anomaly Detection Data

Tables: dbo.ML Transactions anomalies.

Description: Data for identifying irregular transactions
that may indicate fraud or unexpected behavior. This table
stores information about detected anomalies.

Use Case: Enhances transaction security by identifying
and alerting users of potentially fraudulent activities. Figure
7 displays an anomaly transaction.

P. Budget and Goals

Tables:

dbo.Finance Goals,

dbo.fin Budget,

dbo.Budget Category,
dbo.Finance Goal MainCategory.

International Journal of Computing and Digital Systems

9

Figure 7. Anomaly transaction

Figure 9. Budget widgets

Figure 10. Budget dashboard

scaled to a manageable level to enable their use in the
analysis aiming to standardize the results by either using
the current US dollar exchange rate or inflating the amount
to the current year if necessary.

2) Training

Language Models: To determine whether each transac-
tion description is positive, negative, or neutral, we em-
ployed pre-trained language models specialized in financial
data for sentiment analysis on the cleaned transaction de-
scriptions. These models included BERT and GPT, which
were fine-tuned on a financial text corpus to enhance the
model’s performance on context-dependent terms.

Classification: Based on the nature and details of the

Figure 8. Budget creation

Description: Information about users’ budgets and financial
goals. This includes the categorization of expenses and the
tracking of progress towards financial targets.

Use Case: It helps users set and manage financial
goals and budgets, ensuring they stay on track with their
financial plans. Figure 8 shows the budget creation window
and figure 9 portrays the budget widgets. Figures 9 and
10 depicts the budget dashboard and the goal creation
respectfully. Figure 11 specifies the goal creation.

Q. Sentiment Analysis and Data Integration

This is an essential component of the Financial Advisor
Application as it categorizes customers’ emotions according
to their transactions. This process is necessary to analyze
the user’s behavior and recommend financial decisions. This
section reports a detailed plan on how the study will process
the sentiment analysis and integrate data [9].

1) Preprocessing

Data Cleaning: Transaction descriptions were prepro-
cessed to eliminate noise and ensure that all the entries
were in the same format. This step included preprocessing
the text by adjusting common formatting issues, including
punctuation, capitalization, and spelling errors.

Normalization: The transaction amounts and dates were

Figure 11. Goal creation

10

First Author, Samir Bader. Second Author, Ramzi Haraty

transaction descriptions, these transactions were then di-
vided into a set of pre-determined emotional types, namely
Outgoing, Sad, Feeling Generous, Shopping, Roadtrip, Ad-
venturous, Health-Focused, Stressed, Culturally Engaged,
and Tech Enthusiast.

3) Integration

Sentiment Scores: The sentiment of each transaction
was then determined based on the emotion associated with
it. These scores were then compiled and computed over
various intervals to give insights into the user’s emotional
patterns.

Profile Enrichment: The sentiment scores were com-
bined with other user data, such as transaction history
and account details,
the user profiles. This
integration provided a more comprehensive picture of the
user’s financial activity.

to augment

Contextual Analysis: This would have the added advan-
tage of complementing numerical data and the findings from
sentiment analysis in a way that was impossible through
conventional statistical modeling. For instance, many small
purchases interspersed with more significant amounts could
indicate that the person is spending money because of stress.

4) Personalized Insights

Behavior Prediction: By combining the data, the appli-
cation could suggest how the user will spend money in the
future and give recommendations. For example, a user in
the Health-Focused segment will be given suggestions for
membership in a fitness club or other health offers.

Anomaly Detection: The sentiment analysis also high-
lighted possible abnormalities. For instance, an abrupt
change in spending behavior from a user classified as Risk-
Averse to high-risk spending would prompt an alert.

Merchant Recommendations: It could even recommend
merchants based on people’s emotional trends and spend-
ing habits. For example, users categorized as Adventurous
might be offered specific coupons and deals on products
from subscribed merchants that fall under the travel cate-
gory.

5) Feedback Loop

User Interaction: Users could engage with the applica-
tion by confirming or disputing the sentiment categoriza-
tions. This feedback process helped improve the models
and increase the precision of the predictions over time.

Continuous Learning: These sentiment analysis models
were refined using user feedback and fresh transaction data
incorporated into the system.

by data and, simultaneously may consider the emotional
context of the situation.

R. Predictive Modeling

We used sophisticated statistical tools to forecast future
spending patterns and recommend proper financial manage-
ment. These models were meant to evaluate past financial
transactions to predict future actions. Here’s a detailed
breakdown of our approach to predictive modeling: Here’s a
detailed breakdown of our approach to predictive modeling
[5].

1) Transformer Models

Architecture: Transformer architectures efficiently learn
long-term dependencies inherent in data and thus do not
require sequential computations, making them suitable for
time series prediction. They employ self-attention mecha-
nisms that determine the relevance of different points in a
sequence.

Implementation: The Transformer model was devel-
oped using TensorFlow/Keras. It comprises several stacked
blocks of multi-head self-attention and feed-forward net-
work, normalized across the layers and dropout layers to
avoid overfitting.

Training: It was trained on sequences of historical trans-
action data. We fine-tuned it with a learning rate scheduler,
the Adam optimizer, and a mean squared error loss function.

2) Temporal Convolutional Networks (TCN)

Architecture: TCNs are developed for sequence model-
ing; they employ causal convolutions to prevent the model
from producing the temporal order of the data. They can
address long-term dependencies and are effective in train-
ing.

Implementation: The TCN model was trained using the
TCN library available in Keras. The architecture comprised
several dilation convolutions, residual connections, and nor-
malization layers.

Training: The model was fine-tuned using the historical
transaction data. The hyperparameters were adjusted to
select the number of filters, kernel size, and dilation rate.
For optimization, the mean squared error loss function was
employed.

3) N-BEATS

Architecture: N-BEATS stands for Neural basis expan-
sion analysis for interpretable time series forecasting, a time
series forecasting model. It breaks down time-series data
into trends and seasonality features, giving a more human-
friendly forecast.

The Financial Advisor Application incorporated senti-
ment analysis and information about the user’s transactions
and accounts, allowing for sophisticated and feasible rec-
ommendations. This created a holistic approach that helped
provide users with recommendations and insights backed

Implementation: The N-BEATS model was implemented
using custom Keras layers, as described in the following
section. The architecture comprised several dense layers
with ReLU activations and final linear layers that output
the trend and seasonality components.

International Journal of Computing and Digital Systems

11

Training: The model was trained using historical trans-
actional data. We included learning rate scheduling and
early stopping to enhance the training process. The mean
squared error loss function was employed for optimization.

4) Data Preparation

Normalization: All input data were normalized, as the
models need to receive data in a proper format. This step
required normalizing the transaction amounts and equal-
izing the time intervals. Sequence Generation: For the
Transformer and TCN models, sequences of data points
were created to form the input to the models. Each sequence
was a predetermined number of data points, representing a
window of transactions over history.

Feature Engineering: To improve the model’s perfor-
mance, features like user age and gender, account balances,
and sentiment scores derived from the transaction descrip-
tions were added.

5) Evaluation Metrics

1) Model Selection and Training

Algorithm Choice: We divided the chosen anomaly
detection algorithms into two categories: unsupervised and
supervised machine learning algorithms, namely Isolation
Forest, LOF, and One-Class SVM. These algorithms are
beneficial in detecting anomalies in transactional data and
do not need to be trained, as they are given labeled data
sets.

Training Data: Transaction data collected over the years
were employed to train the models. This data contained
standard spending patterns, a sample of the actual fraudulent
transactions that the models could learn, and normal and
abnormal spending.

2) Data Preprocessing

Feature Extraction: To fine-tune the anomaly detection
models, features of transaction data were selected. These
include transaction amount, frequency, time, MCC code,
and user profile.

Mean Absolute Percentage Error (MAPE): This was
used to assess the models’ performance in predicting the
outcomes. MAPE is the average of relative errors and gives
an idea of the size of the mistakes, which is easier to
understand than absolute errors.

Normalization: The data was scaled to a standardized
range to ensure consistency across all data points. This pro-
cess is crucial for optimizing the performance of distance-
based anomaly detection algorithms, such as LOF and
Isolation Forest.

Accuracy: The validity of the models was measured
by how well they forecasted future transactions within a
tolerance level. This involved assessing the models on new
data to test for their applicability across different contexts.

6) Integration and Testing

Real-Time Predictions: The models were incorporated
into the application to enable a predictive model of users’
spending patterns. This entailed applying the models to the
real world and designing a data processing and prediction
output system.

User Feedback: The users were given the forecasts and
asked to verifying whether they were correct or not. This
feedback helped to enhance the models and made them
more accurate and reliable over time.

These more complex and accurate predictive models
enabled the Financial Advisor Application to offer users
exact and personalized financial advice, assisting them in
controlling their financial affairs more efficiently. The ap-
plication of modern machine learning algorithms guaranteed
the predictions’ accuracy and specificity, thus improving the
general usability of the product.

S. Anomaly Detection

Identifying abnormalities in transactions that may show
signs of fraud or any other unusual activity is essential.
This is a process in which machine learning algorithms are
used to identify instances of spending that are out of the
ordinary [23]. Here’s a detailed breakdown of our approach
to anomaly detection:

3) Model Implementation

Isolation Forest: This algorithm isolates observations by
randomly choosing one feature and then choosing a split
value between the largest and the most minor features. Thus,
fewer splits which must be made to isolate an observation
means that the observation is likely to be an outlier.

Local Outlier Factor (LOF): LOF estimates the density
of the given data point concerning its neighbors. Anomaly
means that there is a point in the data set whose density is
significantly less than the density of its neighbors.

One-Class SVM: This algorithm learns the decision
function for anomaly detection, which is the hyperplane
that best separates most data points from the rest.

4) Real-Time Anomaly Detection

Continuous Monitoring: The models checked for new
transactions in real time, comparing them to the typical
pattern of activity as learned from the data. Any variations
greater than 5% were considered significant and marked as
outliers.

Alert Generation: If an abnormality is observed, the
system triggers an alert, and the user is notified to confirm
the observation. This alert contained information such as the
amount, merchant, and transaction time to enable a user to
authenticate or deny the transaction.

5) User Feedback Loop

Verification Process: Customers were notified of the
marked transactions. If a user identified a transaction as

12

First Author, Samir Bader. Second Author, Ramzi Haraty

genuine, the model decreased its false positive rate through
parameter changes. On the other hand, if the particular
transaction was deemed fraudulent, then the model became
more sensitive toward patterns of the same kind.

Model Refinement: The users’ input was regular, allow-
ing the models to be adjusted and fine-tuned over time and
decreasing false positives and negatives.

6) Evaluation Metrics

Precision and Recall: These metrics were employed to
measure the performance of the anomaly detection models.
Specificity is the number of positive detections that are
true positives out of all the positives detected. At the same
time, sensitivity is the number of actual positives marked
as positives.

ROC-AUC Score: The Receiver Operating Character-
istic—Area Under Curve (ROC-AUC) score was used to
measure the performance of the models in discriminating
between normal and abnormal transactions.

7) Integration and Deployment

System Integration: The anomaly detection models were
deployed to the Financial Advisor Application’s backend for
use in the advisory process. This included establishing data
feeds for real-time tracking and transactions occurring in
the business environment.

Deployment: The models were tested in a production
environment where they acted as a watchdog, analyzing user
transactions and highlighting any suspicious activity to the
user for further validation.

The Financial Advisor Application successfully used
powerful and efficient algorithms to detect such anomalies,
offering users more control and security. It also enabled
users to be notified of any malicious activities and take
necessary action to safeguard their money.

T. AI-Driven Merchant Recommendations

The Financial Advisor Application uses AI to ana-
lyze the user’s transaction history and select appropriate
merchant offers to improve user satisfaction and achieve
even more significant savings. This feature ensures that it
provides subscribed merchants discounts and special deals
tailored to users’ needs [4]. Here’s a detailed breakdown of
our approach to AI-driven merchant recommendations:

1) Behavior Analysis

Transaction History Analysis: The application can then
use this information to examine users’ spending habits
based on previous transactions. This means determining the
most common products bought, the most popular merchant
categories, and typical spending by a cardholder.

Feature Extraction: Some extracted attributes include
transaction frequency, average spending per category, and
transaction time. This data assists in creating a user profile

of their interests and needs, hence achieving the company’s
goals.

2) Merchant Matching

Merchant Categorization: MCC codes and other at-
tributes of merchants include location, kinds of products,
and promotions they offer. This can be useful in pairing
users with the appropriate merchants based on their prefer-
ences.

Collaborative Filtering: The application utilizes collab-
orative filtering algorithms to search for other merchants
frequented by users with similar habits. This method uses
the users’ buying patterns to recommend new merchants to
them based on their purchasing activities.

3) Personalized Offers

Dynamic Offer Generation: The application provides
personalized offers to users for their purchases and to
merchants who have subscribed to it. The offers include
coupons, vouchers, cash-back options, and loyalty programs
based on usage.

Contextual Recommendations: The application makes
recommendations based on user interaction and activity. For
instance, if the user has recently purchased food items, it
may recommend coupons from nearby grocery stores.

4) Machine Learning Models

Recommendation Algorithms: To improve recommen-
dation accuracy, several machine learning models, such as
matrix factorization and deep learning, are employed. These
models are built based on user interactions and can update
themselves with better predictions.

Real-Time Processing: It adapts the recommendations
to the users’ real-time transaction data to provide the most
suitable recommendations at the right time.

5) User Feedback Loop

Interaction and Engagement: The recommendations al-
low users to accept or reject offers. This feedback helps
fine-tune the recommendation systems.

Continuous Learning: These recommendations are ad-
justed based on users’ feedback and new transaction data
to keep the models current and valuable.

6) Evaluation Metrics

Precision and Recall: These metrics show the recom-
mendation system’s efficacy. Precision is defined as the ratio
of the relevant offers to all the recommended offers, whereas
recall is the ratio of the relevant offers recommended to the
pertinent total offers.

User Satisfaction: Self-administered questionnaires and
user feedback measure satisfaction with the recommenda-
tions. This qualitative data helps enhance the recommenda-
tion activity.

International Journal of Computing and Digital Systems

13

7) Integration and Deployment

System Integration: The recommendation engine is built
and incorporated into the Financial Advisor Application’s
backend. This involves setting up data pipelines to ingest
and process transaction data continuously.

Deployment: A production environment system actively

works in real-time to present users with merchant offers.

With the help of AI-based merchant suggestions, the
Financial Advisor Application increases user engagement
and saves more money by providing a personalized shop-
ping experience. This way, the users are presented with
relevant offers made available promptly, making managing
their financial resources more fruitful.

U. Integration and Deployment

We needed to assess the effectiveness of our predictive
and anomaly detection models incorporated into the Finan-
cial Advisor Application to guarantee that the results de-
livered were accurate and would improve the application’s
user experience. Here’s a detailed breakdown of our model
evaluation approach: Here’s a detailed breakdown of our
model evaluation approach:

1) Evaluation Metrics

Mean Absolute Percentage Error (MAPE): MAPE was
used to assess the fitness of the predictive models developed
in this study. The average absolute difference between the
predicted and actual values shows how well the model
performs. A lower value of MAPE is preferable, which
means the accuracy of the prediction is high.

Precision and Recall: Regularity analysis was performed
using precision and recall. Precision refers to the ratio of
correctly identified positive cases to the total number of
cases identified as abnormal. In contrast, recall refers to
the ratio of actual anomalous cases detected to the total
number of strange cases in the data set. The first set of
metrics, precision and recall, should be high to suggest that
anomaly detection is effective.

ROC-AUC Score: The Receiver Operating Characteris-
tic—Area Under Curve (ROC-AUC) was used to evaluate
the overall performance of the anomaly detection models.
The ROC-AUC score measures how well the model dis-
criminates between normal and abnormal transactions, and
the closer to 1 the score is, the better the model performs

2) Cross-Validation

K-Fold Cross-Validation: This technique was adopted to
assess the performance of the predictive models. The given
dataset of samples was partitioned into k sets, and the model
was trained on k-1 sets and tested on the remaining set.
This was done k times, and in each iteration, one of the
subgroups was used as a test set. The average of all the k
trials offered an excellent estimate of the model’s accuracy.

Stratified Sampling: To detect the anomalies, stratified
sampling allowed the training and test data sets to be in

the same ratio of normal and abnormal transactions, thus
providing a fair environment for testing.

3) Hyperparameter Tuning

Grid Search: It determined the best hyperparameters for
each model to train and test on the dataset. We tuned the
hyperparameters of the models by evaluating them with
predefined hyperparameters to determine which hyperpa-
rameters produced the best model performance.

Random Search: Besides the grid search, random search
was used to cover a more extensive range of hyperparame-
ters quickly and perhaps find better parameters.

4) Real-Time Testing

Deployment in Production Environment: These models
were then put into real-life production to determine how
they would fare when used under actual situations. This
included constant practice and fine-tuning based on the
exact data that was available.

User Feedback Integration: The users’ ability to confirm
or correct the predictions and anomalies the models flag is
valuable feedback for model improvement.

5) Performance Monitoring

Continuous Evaluation: The models incorporated real-
time data to facilitate optimum performance throughout the
process. Measures such as the accuracy rate, the rate of
detecting anomalies, and the user satisfaction index were
checked frequently.

Automated Alerts: To ensure that the model does not
drastically change its performance, an alert system was
developed to notify the developers of any such changes to
take appropriate measures.

6) Model Retraining

Periodic Retraining: The models were fine-tuned with
new datasets to capture more recent trends and tendencies
in the users’ activity. This ensured that the models did not
become outdated but retained their accuracy and usefulness
in the organization.

Adaptive Learning: The models were expected to be
adaptable in making predictions and detecting anomalies
from the most recent user interactions and feedback.

To achieve this, the Financial Advisor Application uti-
lized a comprehensive evaluation strategy to determine
whether the models developed within the system were accu-
rate, reliable, and capable of offering personalized financial
advice. This approach enriched the user experience and
helped to build confidence in the application’s effectiveness
in managing and protecting economic transactions.

7) Scenarios

The financial advisor application is designed to provide
personalized and intelligent financial support to its users

14

First Author, Samir Bader. Second Author, Ramzi Haraty

Figure 13. The transformers

Figure 12

by leveraging advanced technologies such as anomaly de-
tection, sentiment analysis, and predictive modeling. These
features aim to enhance user experience, promote financial
well-being, and ensure security through actionable insights
and recommendations.

Below are real-world scenarios that demonstrate the
application’s capabilities in various aspects of financial
management, including fraud prevention, budgeting, mer-
chant recommendations, predictive analysis, and sentiment-
based guidance. Each scenario highlights how the system
identifies user-specific needs and delivers tailored solutions
to address them effectively.

4. RESULTS AND ANALYSIS
A. Without Sentiment Analysis
1) Transformer Model Performance

Figure 13 shows the Transformer model’s performance
in predicting customer spending behavior without senti-
ment analysis. The overall mean absolute percentage is
the average difference between the calculated theoretical
and observed values. Accuracy indicates the degree of the
model’s efficiency in predicting the opinion poll results.
The forecasts most accurately capture the actual spending
behavior [5].

In addition, the model replicates the customer spending

Figure 14. The TCN

pattern with a time lag and fluctuations in the lines other
than what was predicted by the model. This is commonplace
in real-world forecasting scenarios where it is impossible to
get a perfect score [5].

2) Temporal Convolutional Networks (TCN)

Figure 14 displays the results of the TCN model without
employing sentiment analysis. A MAPE means that the
model is, on average, right in its predictions, given by the
5th percentile. It is also important to note that these figures
are only 5% away from the actual spending. It indicates that
the model is a good predictor as most values are close to the
actual expenditure [5]. The model can monitor expenditure
patterns and estimate future costs almost accurately.

3) N-BEATS

Figure 15 shows the accuracy of the N-BEATS model
applied to customer spending prediction without sentiment
analysis. The MAPE shows the average prediction error of
the model in terms of expenditure compared to the actual
figure. This study obtained a high accuracy level. As can

International Journal of Computing and Digital Systems

15

Figure 15. N-BEATS

Figure 16. The transformers

be observed from the statistics, the predicted values follow
a similar trend to the actual spending.

The predictive line shows a clear trend, which suggests
that the model captures the mean spending level but not
the variation in the data. This may indicate that the model
needs to be adjusted to address more significant variability
or that more inputs, such as sentiment information, should
be incorporated into the model to enhance the accuracy of
the forecasted spending [5].

B. With Sentiment Analysis Included
1) Transformer Model Performance

The figure below presents the result of utilizing a
Transformer model for customer spending forecasting with
the integration of sentiment analysis. This is in the range
for the MAPE, which means that the error between the
expected and the actual values is, on average, the overall
accuracy. This indicates that the forecasted value is nearly
as accurate as the recorded actual spending [9].

Adding sentiment improves the model’s ability to esti-
mate spending, which is more accurate than the model that
does not incorporate sentiment data. Figure 15 depicts the
transformers.

2) Temporal Convolutional Networks (TCN)

Figure 16 displays the results of adopting the TCN
model for predicting customer spending with the sentiment
analysis element. The MAPE means that the predictions
made by the model are off by this percentage from the actual
values on average. The accuracy indicates that the model
can somewhat capture the trend of expenditure fluctuations
[9].

These statistics show how the model uses sentiment data
to predict spending movements, which is indicated by the
difference between the expected and actual spending trends.

3) Temporal Convolutional Networks (TCN)

Figure 17 illustrates the result of an N-BEATS model
that integrates sentiment analysis for customer spending

Figure 17. The TCN

prediction. The MAPE denotes the difference in the av-
erage error between the expected and actual values. This
type of recognition is accurate and shows that the actual
expenditure predictions are correct [9].

The introduction of sentiment analysis improves the
accuracy of model prediction and provides a better fit to
the actual spending data than the results obtained without
sentiment data.

Including SA in the predictive models makes them
more accurate since it provides a closer estimate of the
actual spending pattern. This improvement is evident from
the following findings: lower MAPE and higher accuracy
models when sentiment data is included. Adding sentiment
in enhancing the
analysis to the applications is crucial
solutions offered to users in the financial domains.

The Financial Advisor Application can successfully pre-
dict the user’s expenses, monitor changes, and recommend
relevant merchants, thus improving financial literacy and
usage.

16

First Author, Samir Bader. Second Author, Ramzi Haraty

terns. Our predictive analysis models significantly enhance
financial planning accuracy by incorporating deep learning
models and sentiment analysis to interpret user emotions
and economic behaviors.

C. Impact of Sentiment Analysis on Predictive Accuracy

• Mean Absolute Percentage Error (MAPE) improved
from 10.5% to 7.8% when sentiment analysis was
incorporated.

• Root Mean Squared Error (RMSE): o Transformer
Model: 0.062 o TCN Model: 0.074 o N-BEATS
Model: 0.057 (best performer)

• Predictive accuracy within a 90% confidence interval:
Achieved 88% alignment with actual user behavior,
indicating high reliability in financial forecasting.

Our approach outperforms conventional budgeting appli-
cations, which primarily rely on static rule-based algorithms
(e.g., Mint, YNAB). Unlike these traditional systems, our
models:

• Analyze historical

transactional data in real-time,

adjusting predictions dynamically.

•

Integrate deep learning techniques
(Transformer,
TCN, N-BEATS) to capture complex temporal de-
pendencies in financial transactions.

• Leverage user sentiment analysis to factor in psy-
chological influences on financial decisions, a feature
largely absent in current fintech applications.

The reduction in prediction error by 25% compared to
rule-based systems highlights the transformative impact of
AI-driven financial forecasting in personal finance manage-
ment.

D. Comparison with Existing Fintech Solutions

To provide a comprehensive evaluation, we compared
our system’s performance, in table 1, against existing fintech
solutions across two key dimensions: anomaly detection and
predictive analysis.

Figure 18. N-BEATS

5. DISCUSSION AND COMPARATIVE ANALYSISs
A. Anomaly Detection Performance Analysis

The experimental results demonstrate the robustness of
our anomaly detection system, achieving an accuracy of
92%, with a precision of 90%, recall of 85%, and an F1-
score of 87.5%. The ROC-AUC score of 0.93 indicates a
strong ability to distinguish between normal and fraudulent
transactions. These results suggest that our approach pro-
vides a substantial improvement over conventional financial
fraud detection systems, which typically report precision
and recall values in the range of 70–80

A key contributing factor to this performance gain is our
multi-model anomaly detection approach, which leverages
advanced machine learning techniques, including Isolation
Forests and One-Class SVM. Unlike conventional fraud
detection mechanisms that rely on static rule-based systems,
our method adapts dynamically to new transaction patterns,
reducing false positives and enhancing detection accuracy.

• Our model,

in contrast, adapts to evolving finan-
cial fraud patterns, leveraging deep learning-based
anomaly detection.

• Precision at 90% vs.

traditional 70–80%: Higher
precision indicates fewer false positives, ensuring that
legitimate transactions are not incorrectly flagged.

• Recall at 85% vs. traditional 70–80%: A higher recall
ensures that the system captures more actual fraud-
ulent transactions, minimizing the risk of undetected
fraud.

Furthermore, our approach enables real-time anomaly
detection without requiring constant human intervention,
making it scalable for high-volume financial environments.

B. Predictive Financial Analysis Performance

Financial forecasting is inherently complex due to the
stochastic nature of market behaviors and user spending pat-

International Journal of Computing and Digital Systems

17

Figure 19. Anomaly detection comparison

Figure 20. Predictive analysis comparison

E. Key Contributions & Broader Implications

Our Ap-
plication

The findings of this research underscore several signifi-
cant contributions to AI-driven financial advisory systems:

Traditional
Bank-
ing/Fraud
Detection
Systems

70–80%

70–80%

Existing
Budget-
ing Apps
(Mint,
YNAB,
etc.)

ap-

Not
plicable

ap-

Not
plicable

Feature

Anomaly De-
tection Preci-
sion
Anomaly De-
tection Preci-
sion

Financial
Forecasting
Method

Statistical
Models

Rule-
Based
Systems

90%

85%

Deep
Learning
(Trans-
former,
TCN, N-
BEATS)

Incorporation
of Sentiment
Analysis
MAPE
(Prediction
Error)
Real-Time
Adaptability

No

No

Yes

ap-

Not
plicable

10–12%

7.8%

Limited

No

Yes

Extensibility
& Scalability

Limited

No

(via

6

Yes
.NET
Core
frame-
work)

This comparative analysis reinforces the superiority
of our approach in terms of accuracy, adaptability, and
predictive power. Unlike existing applications that rely
on predefined heuristics, our system continuously evolves
based on real-time data streams and user behavioral trends.

Figures 19 and 20 provide a comparison of the various
models against anomaly detection and predictive analysis.

1) Advanced AI-driven anomaly detection: Our ap-
proach significantly improves financial transaction
security, reducing false positives while enhancing
fraud detection accuracy.
Integration of sentiment analysis into financial fore-
casting: Demonstrates the tangible benefits of emo-
tional insights in financial decision-making, reducing
prediction errors by 25%.

2)

3) Use of deep learning architectures for predictive
modeling: Unlike existing budgeting applications,
our system leverages sophisticated models (Trans-
former, TCN, N-BEATS) to enhance financial plan-
ning accuracy.

4) Scalable and adaptable financial advisory frame-
work: Developed using .NET Core 6, allowing seam-
less integration of new financial tools and third-party
extensions.

By addressing the limitations of conventional financial
advisory solutions, our work paves the way for more
intelligent, adaptive, and user-centric financial applications
that can dynamically evolve with users’ financial behaviors
and market trends.

it

However,

is essential

to note that

the conclusion
made here is somewhat dissimilar to the positive sentiments
based on the assumption of the total efficiency of sentiment
analysis in enhancing the model predictions. Notably, the
TCN model reveals that including sentiment data does not
constantly improve the predictive performance, which raises
the question of whether sentiment data that drives market
responses aligns with the inherent forecast mechanisms of
specific models [24], [25].

F. Limitations and Future Work

Despite these promising results, some challenges and

limitations remain:

18

First Author, Samir Bader. Second Author, Ramzi Haraty

• Generalization across diverse financial behaviors:
While our models perform well on experimental data,
future work should explore their adaptability across
different user demographics and financial habits.

• Computational efficiency: Deep learning models re-
quire significant computational resources. Future op-
timizations, including model pruning and edge AI
deployment, will be explored to improve efficiency.

• User trust & adoption: While AI-driven financial rec-
ommendations improve accuracy, user trust remains
a critical factor. Future studies will examine user
perception, trust-building strategies, and human-AI
interaction in financial decision-making.

deployment at scale,
integrating robust mechanisms for
handling unstructured data, and conducting extensive real-
world testing to address deployment challenges. Further
research could also explore hybrid approaches that combine
machine learning with domain-specific financial expertise
to enhance the interpretability and reliability of predictions.
By addressing these challenges, the potential of AI-driven
financial applications to deliver timely, personalized, and
secure financial recommendations can be fully realized,
advancing both user experience and the financial services
sector.

References
[1] M. J. Zaki and W. Meira Jr, Data mining and analysis: fundamental
concepts and algorithms. Cambridge University Press, 2014.

6. CONCLUSION

This research analyzed the performance of recent ma-
chine learning models, such as transformer models, TCN,
and N-BEATS, in predicting customer spending patterns
and offering tailored solutions. By integrating sentiment
analysis, we demonstrated how these models process high-
dimensional data, improve forecasting accuracy, and en-
hance financial advisory capabilities. The Transformer
model’s elasticity in handling varied inputs, particularly
sentiment data, allowed it to capture long-term dependen-
cies and subtle changes in customer sentiment, making it
highly effective for predicting spending patterns. Similarly,
the TCN model and N-BEATS model showed significant en-
hancements in performance when combined with sentiment
analysis, with the latter excelling in breaking down time-
series data into trends and seasonality for more detailed
customer behavior analysis.

Our findings highlight the transformative potential of
integrating advanced machine learning models with senti-
ment analysis for comprehending customer behavior and
providing individualized financial recommendations. These
models not only improve customer financial planning but
also enable merchants to better target prospective customers
based on transaction histories and spending habits, thus
creating a mutually beneficial ecosystem.

Despite these promising results, there are several limi-
tations and avenues for future research. One key challenge
lies in scalability—while the models performed well in
controlled environments, their efficiency and responsiveness
in handling large-scale, real-world financial data streams
require further investigation. Additionally, the models pri-
marily rely on structured and semi-structured data; extend-
ing their capabilities to process unstructured data, such
as textual descriptions or social media sentiment, remains
a critical area for development. Another concern is the
deployment of these systems in real-world settings, where
issues such as data privacy, security vulnerabilities, and
compliance with financial regulations must be addressed
rigorously.

Future work should focus on refining these models for

[2]

I. Goodfellow, Y. Bengio, and A. Courville, Deep learning. MIT
Press, 2016.

[3] F. Chollet, Deep learning with Python. Manning Publications,

2017.

[4]

J. Heaton, N. Polson, and J. Witte, “Deep learning for finance: deep
portfolios,” Applied Stochastic Models in Business and Industry,
vol. 33, no. 1, pp. 3–12, 2017.

[5] D. M. Nelson, A. C. Pereira, and R. A. de Oliveira, “Stock market’s
price movement prediction with lstm neural networks,” in IEEE
International Joint Conference on Neural Networks (IJCNN). IEEE,
2017, pp. 1419–1426.

[6] M. Rezaei, M. R. F. Sani, and S. M. Homayouni, “Deep learning-
based stock market prediction,” IEEE Access, vol. 8, pp. 124 408–
124 422, 2020.

[7] A. Esteva, B. Kuprel, R. A. Novoa, J. Ko, S. M. Swetter, H. M. Blau,
and S. Thrun, “Dermatologist-level classification of skin cancer with
deep neural networks,” Nature, vol. 542, no. 7639, pp. 115–118,
2017.

[8] A. Agrawal, J. S. Gans, and A. Goldfarb, “Prediction machines:
the simple economics of artificial intelligence,” Harvard Business
Review, 2018.

[9]

J. Bollen, H. Mao, and X. Zeng, “Twitter’s mood predicts the stock
market,” Journal of Computational Science, vol. 2, no. 1, pp. 1–8,
2011.

[10] V. Kumar and D. Shah, “Building and sustaining profitable customer
loyalty for the 21st century,” Journal of Retailing, vol. 80, no. 4,
pp. 317–329, 2004.

[11] S. Rasp, P. D. Dueben, S. Scher, J. A. Weyn, S. Mouatadid, and
N. Thuerey, “Weatherbench: a benchmark dataset for data-driven
weather forecasting,” Quarterly Journal of the Royal Meteorological
Society, vol. 146, no. 730, pp. 370–385, 2020.

[12] R. Carbonneau, K. Laframboise, and R. Vahidov, “Application of
machine learning techniques for supply chain demand forecasting,”
European Journal of Operational Research, vol. 184, no. 3, pp.
1140–1154, 2008.

[13] T. Young, D. Hazarika, S. Poria, and E. Cambria, “Recent trends in
deep learning-based natural language processing,” IEEE Computa-
tional Intelligence Magazine, vol. 13, no. 3, pp. 55–75, 2018.

International Journal of Computing and Digital Systems

19

[14] K. Sun, “Fine-tuned bert models for sentiment analysis in financial
marketplaces,” Journal of AI Applications in Economics, vol. 13,
no. 3, pp. 19–37, 2023.

[21] P. Johnson, “Knowledge graphs and sentiment analysis for decision
support in fintech,” Advanced Computational Finance, vol. 7, no. 2,
pp. 88–104, 2024.

[15] S. Patel and R. Kumar, “Predictive analytics for budget planning in
fintech,” Digital Finance Advances, vol. 11, no. 2, pp. 67–81, 2022.

[16]

J. Lee, “Ai-driven fraud detection in digital payments,” International
Journal of Financial Security, vol. 8, no. 3, pp. 23–40, 2023.

[17] V. Ramachandran, “Blockchain-enhanced ai for transparent financial
systems,” Journal of Blockchain and AI, vol. 10, no. 1, pp. 45–62,
2024.

[18] Y. Chen, “Sentiment analysis in mobile banking: enhancing user
experience through ai,” Journal of Financial Technology, vol. 12,
no. 1, pp. 34–49, 2024.

[19] R. Gupta, “Integrating sentiment analysis with transaction data for
merchant recommendations,” Fintech Innovations Quarterly, vol. 9,
no. 4, pp. 78–92, 2023.

[20] H. Iqbal, “Combining tcn and n-beats models for financial forecast-
ing,” AI and Finance Journal, vol. 15, no. 3, pp. 56–71, 2022.

[22] T. Sharma, “Challenges in deploying ai in fintech: a scalability
perspective,” Journal of AI Ethics in Finance, vol. 5, no. 2, pp.
101–115, 2023.

[23] V. Chandola, A. Banerjee, and V. Kumar, “Anomaly detection: a
survey,” ACM Computing Surveys, vol. 41, no. 3, pp. 1–58, 2009.

[24] M. El Abaji and R. A. Haraty, “Enhancing bitcoin fore-
cast accuracy by integrating ai,
sentiment analysis, and fi-
nancial models.” Journal of Computing and Digital Systems.
http://dx.doi.org/10.12785/ijcds/1571026011, vol. 17, no. 1, pp. 1–
15, 2025.

[25] R. A. Haraty and S. Sobeh, “Unveiling insights from unstruc-
tured wealth: A comparative analysis of clustering techniques on
blockchain cryptocurrency data,” Journal of Advances in Comput-
ing and Engineering, http://dx.doi.org/10.21622/ACE.2024.04.1.698,
vol. 4, no. 1, pp. 1–43, 2024.

