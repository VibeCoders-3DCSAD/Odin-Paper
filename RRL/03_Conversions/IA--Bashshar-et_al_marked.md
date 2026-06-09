International Journal of Engineering Science and Advanced Technology (IJESAT) Vol 25 Issue 06, June, 2025
ARTIFICIAL INTELLIGENCE-DRIVEN PERSONAL
FINANCE SOLUTION
Syed Abdullah Bashshar 1, Mohammed Imran2 , Piske Sanjay Kumar3,
Edigi Shivani Goud4, Dr. M .Venunath5, Dr. M.L.M. Prasad6
1234UG Student, Department of Computer Science and Engineering - AI&ML,
Joginpally B R Engineering College
5Associate Professor, PhD , Department of Computer Science and Engineering - AI&ML,
Joginpally B R Engineering College
Email : tovenunath@gmail.com
6Associate Professor,PhD,Department of Computer Science and Engineering - AI&ML,
Joginpally B R Engineering College
Email : mlm.prasad@yahoo.com
Abstract : mismanagement of finance in the first place.
In the age of digital payments and e-commerce, Payment through channels like credit cards,
individuals face increasing difficulty in tracking and reputed subscription months, and mobile banking
managing personal finances efficiently. Manual makes it difficult for investors to accept a clear
methods such as spreadsheets and ledger entries often view of their spending habits. This inspires bad
fall short in offering real-time insights and predictive budgeting practices, overshooting, and little
capabilities. This paper presents an AI-powered savings. On the other hand, maintaining expense
personal finance assistant that leverages Natural records in notebooks or through career
Language Processing (NLP) and time-series forecasting spreadsheets is time-consuming, and it is liable to
to automate the categorization of financial transactions errors and can hardly help decision-makers
and predict future expenses. Implemented using Python, forecasting decisions regarding their finances.
Django, and SQLite, the system integrates NLP Artificial Intelligence (AI) is being touted as a
techniques through the Natural Language Toolkit game-changer for this nexus by way of bringing
(NLTK) and forecasting via the ARIMA model. The automation, instantaneous insights, and
tool enables users to track income and expenses, receive contextualized interventions into the financial co-
intelligent insights, and plan budgets proactively. management activity of a person. Such IPAs have
Experiments conducted on real-world financial data already made impact areas such as healthcare,
demonstrate high accuracy in categorization and education, and customer service. However, their
reliable forecasting with low mean absolute error application remains largely unexplored within
(MAE) and root mean square error (RMSE). The results personal finance, notwithstanding mounting
indicate that AI-driven automation can significantly evidence that suggests intelligent systems bolster
enhance personal finance management by promoting user engagement and help get rid of the tiresome
awareness, improving financial planning, and routine tasks. It has become possible to do
encouraging responsible spending behavior. The processing and gain knowledge from unstructured
system's modular architecture ensures scalability and transaction data, to categorize spending
extensibility, offering a practical foundation for future automatically, and even to forecast future expenses
advancements in intelligent financial tools. with the advances in NLP and machine learning.
These abilities transform finance software from
Keywords : Personal finance, NLP, expense
being a passive record keeper into planning tools,
forecasting, ARIMA, transaction categorization,
which, in turn, can help foster better budgeting and
financial planning, AI
saving behavior. This paper presents a Personal
I . INTRODUCTION Finance Assistant powered by AI to track expenses,
The digital and ever-changing world today has categorize transactions on-the-fly, and forecast
made it necessary to manage one's own income and spending for the next 30 days. The system makes
expenditures perfectly, where human insufficient use of NLP techniques for interpreting transactions
time and lack of skill can often lead to and an ARIMA model for performing statistical
ISSN No: 2250-3676 www.ijesat.com Page 413 of 418

International Journal of Engineering Science and Advanced Technology (IJESAT)  Vol 25 Issue 06, June, 2025
forecasting. Developed in Python with Django and  in favor of choosing to fine-tune our NLP models
SQLite, it comes with a responsive web interface  for transaction categorization in personal finance.
| and  backend  |     | automation  |     | that  | allows  | users  | to  |     |     |     |     |     |     |     |     |
| ------------- | --- | ----------- | --- | ----- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| receive  | financial  | insights  |     | on  | the  | fly.  Our  | key  |     |     |     |     |     |     |     |     |
| -------- | ---------- | --------- | --- | --- | ---- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
objective is to arm users with more information
Mirestean et al. (2021) explore IPA design across
about their finances and predictions to help guide
|     |     |     |     |     |     |     |     | domains  | with  | the  | vantage  | point  |     | of  increasing  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----- | ---- | -------- | ------ | --- | --------------- | --- |
smart, conscientious spending. By going beyond
|               |                  |     |     |         |           |     |      | possibilities  |     | for  | personalized  |     | context-aware  |     |     |
| ------------- | ---------------- | --- | --- | ------- | --------- | --- | ---- | -------------- | --- | ---- | ------------- | --- | -------------- | --- | --- |
| the  typical  | voice-activated  |     |     | helper  | paradigm  |     | and  |                |     |      |               |     |                |     |     |
|               |                  |     |     |         |           |     |      | actions.       | It  | saw  | financial     |     | applications   |     | as  |
general information retrieval, this project shows
|     |     |     |     |     |     |     |     | underdeveloped,  |     |     | which  | should  | be  | taken  | as  a  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | ------ | ------- | --- | ------ | ------ |
how personalized AI can have a real-world impact
|     |     |     |     |     |     |     |     | potential  | fertile  | ground  |     | for  innovation-proactive  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ------- | --- | -------------------------- | --- | --- | --- |
in everyday financial decision-making.
decision-making tools. Arrieta et al. (2019) built an

II. LITERATURE SURVEY intelligent  agent  called  Money  Empire  that
|     |     |     |     |     |     |     |     | categorized  |     | expenditure  |     | and  | generated  | financial  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------ | --- | ---- | ---------- | ---------- | --- |
The development of Intelligent Personal Assistants
|         |          |       |                |     |     |            |     | summaries.  |     | It  exhibited  |     | well  | the  | use  of AI  | in  |
| ------- | -------- | ----- | -------------- | --- | --- | ---------- | --- | ----------- | --- | -------------- | --- | ----- | ---- | ----------- | --- |
| (IPAs)  | has  so  | much  | symbiotically  |     |     | augmented  |     |             |     |                |     |       |      |             |     |
personal finance but had no expense forecasting
digital interactions in day-to-day applications of
features, thus limiting its usefulness in forward-
healthcare, education, automation, and finance. A
looking financial planning. Buchanan (2019) made
glance through the seminal works of IPAs will shed
|     |     |     |     |     |     |     |     | a  critical  |     | analysis  | about  | Microsoft  |     | Cortana,  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------- | ------ | ---------- | --- | --------- | --- |
light onto some important contributions in the field
praising it for aiding digital tasks while at the same
of personal finance with emphasis on systems that
time finding a great weakness in decision-making
integrate NLP, machine learning, and intelligent
and domain-specific reasoning.
| automation.                                       | Budiherwanto  |     |     |     | (2025)  | made  | a   |     |     |     |     |     |     |     |     |
| ------------------------------------------------- | ------------- | --- | --- | --- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| comparative evaluation of the best of commercial  |               |     |     |     |         |       |     |     |     |     |     |     |     |     |     |
III. PROPOSED WORK
IPAs: Siri, Google Assistant, and Alexa. The result
The proposed work focuses on the development of
| shows  | that  these  |     | systems  | are  | really  | good  | in  |     |     |     |     |     |     |     |     |
| ------ | ------------ | --- | -------- | ---- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
an Artificial Intelligence-driven personal finance
| recognizing  | speech  |     | and  | carrying  |     | out  | general  |           |      |              |     |      |            |     |      |
| ------------ | ------- | --- | ---- | --------- | --- | ---- | -------- | --------- | ---- | ------------ | --- | ---- | ---------- | --- | ---- |
|              |         |     |      |           |     |      |          | solution  | for  | simplifying  |     | and  | improving  |     | how  |
errands but they cannot deal with domain-specific
|     |     |     |     |     |     |     |     | income  | and  | expenses  |     | are  | managed  |     | by  an  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---- | --------- | --- | ---- | -------- | --- | ------- |
tasks such as financial forecasting or personalized
individual. While the world is increasingly digital
| expense  | tracking.  | This,  |     | therefore,  |     | points  | to  the  |     |     |     |     |     |     |     |     |
| -------- | ---------- | ------ | --- | ----------- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
with online transactions and e-commerce spells, a
necessity of building assistants with complexities
|     |     |     |     |     |     |     |     | lot  of  | users  | just  | cannot  |     | maintain  | financial  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ----- | ------- | --- | --------- | ---------- | --- |
in certain domains, such as personal finance. Weber
awareness because of the sheer volume of their
| et  al.  | (2023)  | presented  |     | a  drone-based  |     | assistant  |     |     |     |     |     |     |     |     |     |
| -------- | ------- | ---------- | --- | --------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
spending data and their complex nature. For most
| having  | AI  capabilities  |     |     | for  | object  | detection,  |     |     |     |     |     |     |     |     |     |
| ------- | ----------------- | --- | --- | ---- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
people, the use of spreadsheets or mobile banking
navigation in real-time, and autonomous decision-
|     |     |     |     |     |     |     |     | applications  |     | is  usually  |     | devoid  | of  | automation,  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------ | --- | ------- | --- | ------------ | --- |
making. This system was mostly geared towards
|             |     |           |     |                |     |      |      | understanding  |     | in  | context  |     | of  the  | financial  |     |
| ----------- | --- | --------- | --- | -------------- | --- | ---- | ---- | -------------- | --- | --- | -------- | --- | -------- | ---------- | --- |
| operations  | in  | physical  |     | environments,  |     | but  | the  |                |     |     |          |     |          |            |     |
transaction, or predictive features. These gaps are
| architectural  | approach     |            | of         | integrating  |                 | several AI  |      |              |         |           |               |              |        |           |         |
| -------------- | ------------ | ---------- | ---------- | ------------ | --------------- | ----------- | ---- | ------------ | ------- | --------- | ------------- | ------------ | ------ | --------- | ------- |
|                |              |            |            |              |                 |             |      | being        | filled  | by        | the  project  |              | using  | the       | single  |
| modules        | into         | a  single  | framework  |              |                 | informs     | the  |              |         |           |               |              |        |           |         |
|                |              |            |            |              |                 |             |      | intelligent  |         | platform  |               | of  Natural  |        | Language  |         |
| continued      | development  |            |            | of           | software-based  |             |      |              |         |           |               |              |        |           |         |
Processing (NLP) and time-series forecasting. The
assistants in finance for whom real-time decision-
|     |     |     |     |     |     |     |     | proposed  | system,  |     | through  | the  | implementation  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --- | -------- | ---- | --------------- | --- | --- |
making  and  predictive  insight  are  equally  using Python's Natural Language Toolkit (NLTK)
| important.  | Rane       | (2023)  |         | imagined  |       | sensor-laden  |         |           |            |     |               |     |     |              |     |
| ----------- | ---------- | ------- | ------- | --------- | ----- | ------------- | ------- | --------- | ---------- | --- | ------------- | --- | --- | ------------ | --- |
|             |            |         |         |           |       |               |         | library,  | processes  |     | unstructured  |     |     | transaction  |     |
| personal    | assistant  |         | robots  |           | able  | to            | decide  |           |            |     |               |     |     |              |     |
descriptions and automatically classifies them into
| autonomously  |     | with  | merging AI.  |     | Since  | the  | key  |     |     |     |     |     |     |     |     |
| ------------- | --- | ----- | ------------ | --- | ------ | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
predefined categories of expenditure. This requires
points  of  such  a  work  involve  autonomous  neither  manual  intervention  for  labeling  nor
| behavior,  | especially  |     | context-aware  |     |     | behavior,  | it  |     |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | -------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
provides ability for real-time insight into altering
lends the direct applications to be in line with ours
financial behavior. Moreover, the platform uses the
in automating financial insights and forecasting.
|          |          |         |     |          |      |        |     | ARIMA  | (AutoRegressive  |     |     | Integrated  |     |     | Moving  |
| -------- | -------- | ------- | --- | -------- | ---- | ------ | --- | ------ | ---------------- | --- | --- | ----------- | --- | --- | ------- |
| Buckley  | et  al.  | (2021)  |     | pursued  | the  | study  | of  |        |                  |     |     |             |     |     |         |
Average) model to forecast future expenses based
education using NLP through a personal learning
|     |     |     |     |     |     |     |     | on  historical  |     | financial  |     | data."  | The  | objective  | is  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ---------- | --- | ------- | ---- | ---------- | --- |
assistant. The work concluded that training an NLP
therefore to help users in tracking past expenses
system bestowed with domain-specific knowledge
and thus foresee future financial events in order to
| should  | improve  | the  | accuracy  |     | of  | information  |     |     |     |     |     |     |     |     |     |
| ------- | -------- | ---- | --------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
put together timely plans for budgeting. Python,
extraction and relevance to task execution. This is
somehow, continues to be a favorite in core logic,
| ISSN No: 2250-3676  |     |     |     |     |     |     | www.ijesat.com |     |     |     |     |     | Page 414 of 418 |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --------------- | --- | --- |

International Journal of Engineering Science and Advanced Technology (IJESAT)  Vol 25 Issue 06, June, 2025
Django is  the web  framework of  choice, while  one or more fields, to normalization of all date and
SQLite functions as a lightweight database.
|     |     |     |     |     |     |     | numerical                                            | fields.  | With     |         | regard   | to            | descriptions,  |          |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | -------- | -------- | ------- | -------- | ------------- | -------------- | -------- |
|     |     |     |     |     |     |     | cleaning goes a step further by removing irrelevant  |          |          |         |          |               |                |          |
|     |     |     |     |     |     |     | information                                          | that     | could    | affect  |          | the  quality  |                | of  the  |
|     |     |     |     |     |     |     | input-output                                         |          | process  | in      | Natural  |               | Language       |          |
Processing (NLP). Since preprocessing removes as
much noise from the data as possible, it thereby sets
|     |     |     |     |     |     |     | the  stage  | for  | accurate  |     | categorization  |     |     | and  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | --------- | --- | --------------- | --- | --- | ---- |
forecasting.

Transaction Categorization Using NLP
In an effort to minimize human work and further
financial insight, the system does categorization
|     |     |     |     |     |     |     | using  | NLP  techniques.  |     |     | Through  |     | the  | NLTK,  |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----------------- | --- | --- | -------- | --- | ---- | ------ |
transaction descriptions are tokenized, stop words
are excluded that do not really contribute to the
meaning, and finally, the lemmatization of words is
|     |     |     |     |     |     |     | done  into  | their         | root     | forms         | that         | could  | serve       | as  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------- | -------- | ------------- | ------------ | ------ | ----------- | --- |
|     |     |     |     |     |     |     | keywords.   | Each          | keyword  |               | is  matched  |        | against     | a   |
|     |     |     |     |     |     |     | couple      | of  category  |          | dictionaries  |              | to     | categorize  |     |
transactions into groceries, transportation, utilities,

|     |     |     |     |     |     |     | etc. In this  | way, the categorization really helps  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------------------------------------- | --- | --- | --- | --- | --- | --- |
Fig 1 : Proposed Architecture
folks learn their spending behaviors without having
There is a responsive web interface that lets a user
to do it manually.
| upload  | transaction  |     | history  | to  see  | categorized  |     |     |     |     |     |     |     |     |     |
| ------- | ------------ | --- | -------- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Expense Forecasting Through ARIMA
summaries and forecasted expenses presented with
Financial foresight is given to the prediction of
| easy-to-understand  |     |     | visualizations.  |     | Automated  |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | --- | ---------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
expenses with the help of ARIMA (AutoRegressive
transaction classification, 30-day expense forecast,
usage  of  interactive  dashboards,  and  modular  Integrated  Moving  Average).  Hence,  ARIMA
|         |                   |     |          |          |          |     | analyzes  | time-series  |     | data  | of  past  | expenses  |     | and  |
| ------- | ----------------- | --- | -------- | -------- | -------- | --- | --------- | ------------ | --- | ----- | --------- | --------- | --- | ---- |
| design  | for  scalability  |     | of  the  | system.  | Through  |     |           |              |     |       |           |           |     |      |
looks for trend and seasonal patterns to generate its
intelligent categorization and predictive analytics,
own predictions for the next 30 days. This type of
| personalized  | financial  |     | insights  | are  | offered,  | thus  |     |     |     |     |     |     |     |     |
| ------------- | ---------- | --- | --------- | ---- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
helping  users  make  solid  decisions  and  spend  forecast  prepares  a  user  for  any  budgetary
|     |     |     |     |     |     |     | constraints  | that  | may  | arise  | in  | the  not-so-distant  |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----- | ---- | ------ | --- | -------------------- | --- | --- |
wisely. This work will lay the path for future AI-
future, thus providing him with an opportunity to
| related  | personal  | finance  | tools,  |     | addressing  | the  |     |     |     |     |     |     |     |     |
| -------- | --------- | -------- | ------- | --- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
adjust his expenses accordingly. And the model's
increased need for intelligent yet straightforward
financial management in the digital world.  accuracy is also maintained by using standard error
metrics such as MAE and RMSE.

|     |     |     |     |     |     |     | Evaluation and Testing |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
IV. METHODOLOGY
|     |     |     |     |     |     |     | To  validate  | the  | effectiveness  |     |     | of  | the  | system,  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ---- | -------------- | --- | --- | --- | ---- | -------- |
Data Collection
|            |        |       |          |           |          |     | comprehensive  |     | testing  | is  | conducted  |     | using  | real- |
| ---------- | ------ | ----- | -------- | --------- | -------- | --- | -------------- | --- | -------- | --- | ---------- | --- | ------ | ----- |
| The  very  | first  | step  | in  the  | system's  | working  |     |                |     |          |     |            |     |        |       |
world financial datasets. Evaluation focuses on the
methodology is to collect financial transaction data
|            |         |             |       |       |        |        | accuracy  | of  | transaction  |     | categorization,  |     |     | the  |
| ---------- | ------- | ----------- | ----- | ----- | ------ | ------ | --------- | --- | ------------ | --- | ---------------- | --- | --- | ---- |
| from  its  | users.  | Typically,  | this  | data  | comes  | in  a  |           |     |              |     |                  |     |     |      |
reliability of expense forecasting, and the overall
structured manner, such as CSV files containing
|     |     |     |     |     |     |     | user  experience.  |     | Metrics  |     | such  | as  | classification  |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | -------- | --- | ----- | --- | --------------- | --- |
essential transaction fields like date, description,
accuracy, MAE, and RMSE provide quantitative
| amount,  | and  | transaction  | type,  |     | i.e.,  income  | or  |     |     |     |     |     |     |     |     |
| -------- | ---- | ------------ | ------ | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
measures of performance. User feedback on the
| expense.  | Users  | give  | their  system  |     | the  raw  | data  |     |     |     |     |     |     |     |     |
| --------- | ------ | ----- | -------------- | --- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
interface responsiveness and clarity of financial
through uploading bank statements or credit card
|     |     |     |     |     |     |     | insights  | also  | informs  | iterative  |     | improvements,  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----- | -------- | ---------- | --- | -------------- | --- | --- |
statements. This raw data from the initial intake
ensuring the system meets practical usability and
forms the basis upon which subsequent analysis
functionality standards.
and predictions are made.
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Data Preprocessing

V.ALGORITHMS
| After  this  | collection  |     | of  | transaction  |     | data,  it  |     |     |     |     |     |     |     |     |
| ------------ | ----------- | --- | --- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |

processes  preprocessing  to  render  the  data  1. NLP for Transaction Categorization
scrupulous, standardized, and fit for analysis. It
This system uses NLP techniques to analyze the
will encode the removal of extraneous characters
transaction descriptions and apply the category to
from any of the fields, from text inconsistencies in
| ISSN No: 2250-3676  |     |     |     |     |     | www.ijesat.com |     |     |     |     |     | Page 415 of 418 |     |     |
| ------------------- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --------------- | --- | --- |

International Journal of Engineering Science and Advanced Technology (IJESAT)  Vol 25 Issue 06, June, 2025
the transaction. The main steps of the process are
as follows:
Tokenization : Words are separated into tokens.
|            |     |          |     | Words  | which  | are  | often  |     |     |     |     |     |     |     |
| ---------- | --- | -------- | --- | ------ | ------ | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
| Stop-word  |     | Removal  | :   |        |        |      |        |     |     |     |     |     |     |     |
irrelevant (e.g., ``and,`` the'').
Lemmatization :  Words are returned to their base

or root form (e.g., running → run).
|     |     |     |     |     |     |     |     |     |     | Fig 2 : List of Goals |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- |
The part of actually doing the categorization is
|     |     |     |     |     |     |     |     | The AI-powered  |     | personal  |     | finance  | assistant  | was  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------- | --- | -------- | ---------- | ---- |
done by keyword matching with the help of domain
|     |     |     |     |     |     |     |     | evaluated  | on  | certain  | key  | axes:  | transaction  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | ---- | ------ | ------------ | --- |
dictionaries: there would be a dictionary for each
|         |     |            |      |           |     |          |        | categorization  |     | accuracy,  | expense  |     | forecastability,  |     |
| ------- | --- | ---------- | ---- | --------- | --- | -------- | ------ | --------------- | --- | ---------- | -------- | --- | ----------------- | --- |
| domain  | or  | category;  | for  | example,  |     | if  any  | token  |                 |     |            |          |     |                   |     |
and user experience. The system provided the user
| identifies  | with  | any  | of  | the  words  |     | stored  | in  the  |     |     |     |     |     |     |     |
| ----------- | ----- | ---- | --- | ----------- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
with a dual benefit by simultaneously using NLP-
| ``Food``  | class  | dictionary,  |     | then  | the  | transaction  |     |     |     |     |     |     |     |     |
| --------- | ------ | ------------ | --- | ----- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
would be marked under that category.  based  and  time-series-based  technologies  to
|     |     |     |     |     |     |     |     | analyze  | and  | make  sense  | of  | financial  | activities.  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ------------ | --- | ---------- | ------------ | --- |
2. ARIMA (Auto Regressive Integrated Moving
Transaction categorization sits at the core of the
Average) for Expense Forecasting
|     |     |     |     |     |     |     |     | system,  | wherein  | the  | Random  | Forest  | classifier,  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ---- | ------- | ------- | ------------ | --- |
The ARIMA model combines three components to  using TF-IDF features, is employed. With more
|     |     |     |     |     |     |     |     | than  1,000  |     | labeled  | transaction  | descriptions  |     | for  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | ------------ | ------------- | --- | ---- |
analyze and forecast time series data:
training data, the model achieved good results with
Auto Regressive (AR) part: The value at time t
an 80:20 train-test split: with an accuracy of 86.2%,
depends on its previous values:
precision of 0.88, recall 0.85, and F1-score of 0.86.
|     |       |         |          |       |         | +ϵ    |     | These figures imply efficient classification, mainly  |     |     |     |     |     |     |
| --- | ----- | ------- | -------- | ----- | ------- | ----- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|     | Y=ϕ t | 1 Y t−1 | +ϕ 2  Y  | t−2 + | +ϕ  p Y | t−p t |     |                                                       |     |     |     |     |     |     |
dealing with common categories, such as Food,
| where ϕ are AR coefficients, p is the order of  | i   |     |     |     |     |     |     |                                                        |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
|                                                 |     |     |     | ⋯   |     |     |     | Travel, Utilities, and Entertainment. Analysis of the  |     |     |     |     |     |     |
autoregression, and ϵ is white noise error.
t
confusion matrix indicated some overlaps between
Integrated (I) part: Differencing the series ddd  categories that were similar, such as "Dining" and
times to make it stationary:  "Groceries,"  which  suggests  there  is  still  some
|     |     |     |             |     |     |     |     | room  for  | improvement. This  |     |     | improvement  |     | may  |
| --- | --- | --- | ----------- | --- | --- | --- | --- | ---------- | ------------------ | --- | --- | ------------ | --- | ---- |
|     |     | Y′= | dY=(1−B)dY  |     |     |     |     |            |                    |     |     |              |     |      |
|     |     |     | t           | t   | t   |     |     |            |                    |     |     |              |     |      |
certainly come through by enhancing the model
Here, B is the backs hift operator (BY =Y )  with  more  domain-specific  labeled  data,  thus
|     |     |     | ∇   |     |     | t t−1 |     |             |                 |     |     |            |       |         |
| --- | --- | --- | --- | --- | --- | ----- | --- | ----------- | --------------- | --- | --- | ---------- | ----- | ------- |
|     |     |     |     |     |     |       |     | increasing  | categorization  |     |     | accuracy.  | This  | aligns  |
and d is the differencing order.
with the findings of Li et al. (2008), who have
Moving Average (MA) part: Modeling error
stressed the enhancement of semantic extraction
terms as a linear combination of previous error  within intelligent assistant systems leveraging NLP
terms:
methodologies. The assistant holds great promise
Y=ϵ+θ  ϵ +θ  ϵ + +θ ϵ   for automating and simplifying everyday personal-
|     |     | t t | 1 t−1 | 2 t−2 |     | q  t−q  |     |                  |     |         |      |            |        |       |
| --- | --- | --- | ----- | ----- | --- | ------- | --- | ---------------- | --- | ------- | ---- | ---------- | ------ | ----- |
|     |     |     |       |       |     |         |     | finance-related  |     | chores  | and  | hazelling  | users  | with  |
where θ are MA coefficients and q is the order of
j
|     |     |     |     |     | ⋯   |     |     | explicit insights through strong categorization and  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- |
moving average.
forecasting capabilities.

VI.RESULTS AND DISCUSSION
| The  | proposed  |     | AI-powered  |     | personal  |     | finance  |     |     |     |     |     |     |     |
| ---- | --------- | --- | ----------- | --- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
assistant was evaluated across multiple functional
and technical dimensions, including the accuracy
of transaction categorization, reliability of expense
| forecasting,  |     | and  | overall  | user  | experience.  |     | The  |     |     |     |     |     |     |     |
| ------------- | --- | ---- | -------- | ----- | ------------ | --- | ---- | --- | --- | --- | --- | --- | --- | --- |

| experiments  |     | demonstrate  |     |     | that  | the  | system  |     |     |     |     |     |     |     |
| ------------ | --- | ------------ | --- | --- | ----- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- |

Fig 3 : Forecasts of expenses for the next 30 days
effectively integrates natural language processing
| and       | time  series  |      | forecasting    |     | to  support  | users      | in  |             |     |        |      |                    |     |     |
| --------- | ------------- | ---- | -------------- | --- | ------------ | ---------- | --- | ----------- | --- | ------ | ---- | ------------------ | --- | --- |
| managing  |               | and  | understanding  |     | their        | financial  |     |             |     |        |      |                    |     |     |
|           |               |      |                |     |              |            |     | The  ARIMA  |     | model  | was  | thus  implemented  |     | to  |
behavior.  predict expenses by taking a look at the six months
|                     |     |     |     |     |     |     |                | of  transaction  |     | data  | considered  |     | the             | past.  |
| ------------------- | --- | --- | --- | --- | --- | --- | -------------- | ---------------- | --- | ----- | ----------- | --- | --------------- | ------ |
| ISSN No: 2250-3676  |     |     |     |     |     |     | www.ijesat.com |                  |     |       |             |     | Page 416 of 418 |        |

International Journal of Engineering Science and Advanced Technology (IJESAT)  Vol 25 Issue 06, June, 2025
Differencing  was  used  in  making  the  data  This  work  builds  the  design,  development,  and
stationary.  The  best  parameters  (p,  d,  q)  were  evaluation  of  an  AI-powered  personal  finance
selected using the Akaike Information Criterion  assistant with transaction categorization using NLP
(AIC). The forecasting performance was evaluated  and expense prediction with ARIMA-based time-
based on:  series forecasting. The system offers two important
Mean Absolute Error (MAE): 253.47  improvements  over  traditional  financial
management tools: autonomous categorization and
Root Mean Square Error (RMSE): 318.91
|     |     |     |     |     |     |     | predictive  | insights,  |     | so  | users  | can  | manage  | their  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | --- | ------ | ---- | ------- | ------ |
These forecast patterns were able to pick up the  finances efficiently and in a proactive manner.
| main seasonal patterns and spending variations. A  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
visual depiction in Figure 1 depicts the predicted
Developed with Python-based technologies such as
| expenses  | for  | the  next  | 30  | days  against  |     | actual  |          |        |      |               |     |     |                  |     |
| --------- | ---- | ---------- | --- | -------------- | --- | ------- | -------- | ------ | ---- | ------------- | --- | --- | ---------------- | --- |
|           |      |            |     |                |     |         | Django,  | NLTK,  | and  | Statsmodels,  |     |     | this  assistant  |     |
historical expenses, where a close tie is seen in
|     |     |     |     |     |     |     | achieves  | very  | high  | accuracy  |     | in  | categorization  |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----- | ----- | --------- | --- | --- | --------------- | --- |
most of the periods.
(86%) and forecasting in relative terms of error
| Such  | results  | stand  | as  good  | evidence  |     | toward  |       |      |         |     |                  |     |     |           |
| ----- | -------- | ------ | --------- | --------- | --- | ------- | ----- | ---- | ------- | --- | ---------------- | --- | --- | --------- |
|       |          |        |           |           |     |         | (MAE  | and  | RMSE);  | it  | is,  therefore,  |     | a   | reliable  |
application in real-world budgeting scenarios and
system. In addition to a responsive and easy-to-use
have been backed by similar studies in AI-assisted
|     |     |     |     |     |     |     | interface,  | ensuring  |     | accessibility  |     | to  | the  | greatest  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | --- | -------------- | --- | --- | ---- | --------- |
financial forecasting (Arrieta et al., 2019; Cao et
number of users possible, usability evaluation was
al., 2020).
|     |     |     |     |     |     |     | positive,  | and  | the  | administrators  |     | confirmed  |     | its  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ---- | --------------- | --- | ---------- | --- | ---- |
usefulness in solving real-world personal finance
problems.As also indicated in the related work,
intelligent agents are evolving user experiences by
|     |     |     |     |     |     |     | automating     |     | complex           | processes  |     | and   | presenting  |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----------------- | ---------- | --- | ----- | ----------- | --- |
|     |     |     |     |     |     |     | context-aware  |     | recommendations.  |            |     | This  | particular  |     |
project focuses on personal finance, where timely
|     |     |     |     |     |     |     | insights                              | and  | accurate  | predictions  |        |     | can  make  | a   |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | ---- | --------- | ------------ | ------ | --- | ---------- | --- |
|     |     |     |     |     |     |     | difference                            |      | in        |              | sound  |     | decision-  |     |
|     |     |     |     |     |     |     | making/complementing that evolution.  |      |           |              |        |     |            |     |
Fig 5 :  Earnings Overview
Cross-browser  testing  ensured  flawless  cross- With its robustness and functionality, the current
platform behavior of the user interface on these  implementation  leaves  room  for  future
|     |     |     |     |     |     |     | improvements. These  |     |     | may  | include  |     | integrating  | a   |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ---- | -------- | --- | ------------ | --- |
devices. Users could enter transactions, see their
wider breed of banking APIs, developing adaptive
spending summaries by category, and navigate to
forecast dashboards without experiencing delays or  learnings for personal recommendations, carrying
stutters. User sentiment was then measured through  out anomaly detection in spend patterns in real-
a  Likert  scale  questionnaire  presented  to  ten  time,  or  adding  multilingual  interface  support.
participants. The responses were mostly positive:  These advancements will surely play their role in
|     |     |     |     |     |     |     | strengthening  |     | the  | system  | and  | pursuits  |     | across  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---- | ------- | ---- | --------- | --- | ------- |
All scores show the system was able to provide an
different users and financial situations.
otherwise smooth interaction with an intuitive user

interface. Test users commented that the UI helped  FUTURE SCOPE
them comprehend and delve into their financial  Although strong in its current implementation, the
data quite easily, thus drawing attention to a great
AI-enabled personal finance assistant could shine
interface design with usability and transparency.
even brighter with some very promising extensions
This can be compared to observations presented by
|     |     |     |     |     |     |     | affecting  | factors  | like  | efficiency,  |     | scalability,  |     | and  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ----- | ------------ | --- | ------------- | --- | ---- |
Ribes (2023) and Galperti (2019), who emphasize  user  engagement.  Integration  with  real-time
| a  consideration  |     | for  | well  engineering  |     | the  | user  |     |     |     |     |     |     |     |     |
| ----------------- | --- | ---- | ------------------ | --- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
banking APIs and financial platforms should be
| experience  | as  | a  pre-condition  |     | for  an  | intelligent  |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ----------------- | --- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
one of the options for expansion to let the system
| digital  | assistant  | to  be  | accepted.  | This  | feedback  |     |     |     |     |     |     |     |     |     |
| -------- | ---------- | ------- | ---------- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
automatically grab transaction data for the accounts
shows that not only does the interface facilitate the  involved. This  would  mean no onerous manual
execution of basic financial tasks, but that it also
entry and provide a broader picture of the user's
| generates  | user  | engagement  |     | by  being  |     | clear,  |     |     |     |     |     |     |     |     |
| ---------- | ----- | ----------- | --- | ---------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
financial activity. Besides, putting in place support
responsive, and attractive.
for various international financial systems would
|     |     |     |     |     |     |     | make this tool useful on a global scale. The other  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
CONCLUSION
route involves strengthening the NLP processor so
the assistant may interpret more complex queries
| ISSN No: 2250-3676  |     |     |     |     |     | www.ijesat.com |     |     |     |     |     |     | Page 417 of 418 |     |
| ------------------- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --------------- | --- |

International Journal of Engineering Science and Advanced Technology (IJESAT)  Vol 25 Issue 06, June, 2025
and  respond  naturally  and  conversationally,  so  Information  Fusion,  58,  82–115.
https://doi.org/10.1016/j.inffus.2019.12.012
| interaction                                        | becomes  |     | more  | intuitive.  |     | Putting  | in  |     |     |     |     |     |     |     |     |
| -------------------------------------------------- | -------- | --- | ----- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| place integration with voice assistants or mobile  |          |     |       |             |     |          |     |     |     |     |     |     |     |     |     |
10. Buchanan, B. G. (2019). Artificial intelligence in
voice input would boost accessibility and usability,  finance. Zenodo (CERN European Organization for
particularly  if  users  want  the  financial-tracking  Nuclear  Research).
process to be hands-free.
https://doi.org/10.5281/zenodo.2626454
REFERENCES  11.   Giudici, P. (2018). Fintech Risk Management: A
|     |     |     |     |     |     |     |     | research  | challenge  |     | for  | artificial  |     | intelligence  | in  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ---- | ----------- | --- | ------------- | --- |

1. Budiherwanto, I. (2025). The influence of artificial
|     |     |     |     |     |     |     |     | finance.  | Frontiers  |     | in  | Artificial  |     | Intelligence,  | 1.  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | --- | ----------- | --- | -------------- | --- |
intelligence and the technology acceptance model
https://doi.org/10.3389/frai.2018.00001
on sustainable financial governance. Jurnal Ilmiah

12. Berman, J. Z., et al. (2015). Expense neglect in
| Manajemen  |     | Kesatuan,  |     | 13(3),  |     | 1791–1802.  |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ---------- | --- | ------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
forecasting personal finances. Journal of Marketing
https://doi.org/10.37641/jimkes.v13i3.3256
|            |      |        |     |         |        |               |     | Research,  |     |     |     | 53(4),  |     | 535–550.  |     |
| ---------- | ---- | ------ | --- | ------- | ------ | ------------- | --- | ---------- | --- | --- | --- | ------- | --- | --------- | --- |
| 2. Weber,  | P.,  | Carl,  | K.  | V.,  &  | Hinz,  | O.  (2023a).  |     |            |     |     |     |         |     |           |     |
https://doi.org/10.1509/jmr.15.0101
Applications of Explainable Artificial Intelligence
|                |     |             |     |         |           |               |          | 13.   Khashei,  |     | M.,  &  | Bijari,     | M.  | (2010).  | A         | novel  |
| -------------- | --- | ----------- | --- | ------- | --------- | ------------- | -------- | --------------- | --- | ------- | ----------- | --- | -------- | --------- | ------ |
| in  Finance—a  |     | systematic  |     | review  |           | of  Finance,  |          |                 |     |         |             |     |          |           |        |
|                |     |             |     |         |           |               |          | hybridization   |     | of      | artificial  |     | neural   | networks  | and    |
| Information    |     | Systems,    |     | and     | Computer  |               | Science  |                 |     |         |             |     |          |           |        |
ARIMA models for time series forecasting. Applied
literature. Management Review Quarterly, 74(2),
|           |     |                                     |     |     |     |     |     | Soft  | Computing,  |     |     | 11(2),  |     | 2664–2675.  |     |
| --------- | --- | ----------------------------------- | --- | --- | --- | --- | --- | ----- | ----------- | --- | --- | ------- | --- | ----------- | --- |
| 867–907.  |     | https://doi.org/10.1007/s11301-023- |     |     |     |     |     |       |             |     |     |         |     |             |     |
https://doi.org/10.1016/j.asoc.2010.10.015
00320-0

14. Ilyina, A., & Samaniego, R. M. (2008). Technology

3. Rane, N. (2023). Role and challenges of ChaTGPT
|      |          |             |     |             |               |     |     | and  | Finance.  |     | SSRN  |     | Electronic  |     | Journal.  |
| ---- | -------- | ----------- | --- | ----------- | ------------- | --- | --- | ---- | --------- | --- | ----- | --- | ----------- | --- | --------- |
| and  | similar  | generative  |     | artificial  | intelligence  |     | in  |      |           |     |       |     |             |     |           |
https://core.ac.uk/display/79856962
finance and accounting. SSRN Electronic Journal.

15. Binner, J. M., Kendall, G., & Chen, S. (2004).
https://doi.org/10.2139/ssrn.4603206
|     |     |     |     |     |     |     |     | Applications of artificial intelligence in finance and  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
4. Ribes, E. A. (2023). Transforming personal finance
|     |     |     |     |     |     |     |     | economics.  |     | In  | Advances  |     | in  | Econometrics.  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --------- | --- | --- | -------------- | --- |
thanks to artificial intelligence: myth or reality?
https://doi.org/10.1016/s0731-9053(2004)19
| Financial  |     | Economics  |     |     | Letters,  |     | 2(1).  |     |     |     |     |     |     |     |     |
| ---------- | --- | ---------- | --- | --- | --------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
16.   Manning, C. D., & Schütze, H. (1999). Foundations
https://doi.org/10.58567/fel02010002
|     |     |     |     |     |     |     |     | of  | Statistical  |     | natural  | language  |     | processing.  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | --------- | --- | ------------ | --- |

| 5. Zaremba,  |     | A.,  &  | Demir,  | E.  | (2023).  | ChatGPT:  |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ------- | ------- | --- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
https://doi.org/10.1017/S1351324902212851
| Unlocking the Future of NLP in Finance. SSRN  |     |     |     |     |     |           |     |              |      |     |           |     |          |              |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --------- | --- | ------------ | ---- | --- | --------- | --- | -------- | ------------ | --- |
|                                               |     |     |     |     |     |           |     | 17. Zysman,  | J.,  | &   | Heertje,  | A.  | (1990).  | Innovation,  |     |
| Electronic                                    |     |     |     |     |     | Journal.  |     |              |      |     |           |     |          |              |     |
Technology, and finance. The American Journal of
https://doi.org/10.2139/ssrn.4323643
|     |     |     |     |     |     |     |     | Comparative  |     |     | Law,  |     | 38(1),  |     | 190.  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | ----- | --- | ------- | --- | ----- |
6.   Buckley, R., Zetzsche, D., Arner, D., & Tang, B.
https://doi.org/10.2307/840260
| (2021).  | Regulating  |     | Artificial  |     | intelligence  |     | in  |     |     |     |     |     |     |     |     |
| -------- | ----------- | --- | ----------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

18. Harvey, A. C. (1984). A unified view of statistical
| Finance:    | Putting  |     | the  human  |     | in  the  | loop.     | SSRN  |              |     |              |     |          |     |                   |     |
| ----------- | -------- | --- | ----------- | --- | -------- | --------- | ----- | ------------ | --- | ------------ | --- | -------- | --- | ----------------- | --- |
|             |          |     |             |     |          |           |       | forecasting  |     | procedures.  |     | Journal  |     | of  Forecasting,  |     |
| Electronic  |          |     |             |     |          | Journal.  |       |              |     |              |     |          |     |                   |     |
|             |          |     |             |     |          |           |       | 3(3),        |     |              |     |          |     | 245–275.          |     |
https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_I
https://doi.org/10.1002/for.3980030302
D3831758_code524849.pdf?abstractid=3831758&
|     |     |     |     |     |     |     |     | 19.   Forgue,  | R.  | E.,  | &  Garman,  |     | E.  (1988).  |     | Personal  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---- | ----------- | --- | ------------ | --- | --------- |
mirid=1
finance.

7. Mirestean, A., et al. (2021). Powering the Digital
https://openlibrary.org/books/OL56751M/Personal
| Economy:  |     | Opportunities  |     | and  | risks  | of  Artificial  |     |     |     |     |     |     |     |     |     |
| --------- | --- | -------------- | --- | ---- | ------ | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
_finance
| intelligence  |     | in  | finance.  | Departmental  |     |     | Paper,  |     |     |     |     |     |     |     |     |
| ------------- | --- | --- | --------- | ------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |

| 2021(024),  |     |     |     |     |     |     | 1.  |     |     |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

https://doi.org/10.5089/9781589063952.087
8.   Mhlanga, D. (2020). Industry 4.0 in Finance: The
| impact     | of Artificial  |             | intelligence  |                | (AI)   | on       | digital  |     |     |     |     |     |     |     |     |
| ---------- | -------------- | ----------- | ------------- | -------------- | ------ | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| financial  |                | inclusion.  |               | International  |        | Journal  | of       |     |     |     |     |     |     |     |     |
| Financial  |                |             | Studies,      |                | 8(3),  |          | 45.      |     |     |     |     |     |     |     |     |
https://doi.org/10.3390/ijfs8030045

9. Arrieta, A. B., et al. (2019). Explainable Artificial
| Intelligence  |     | (XAI):  |     | Concepts,  |     | taxonomies,  |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ------- | --- | ---------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
opportunities and challenges toward responsible AI.
| ISSN No: 2250-3676  |     |     |     |     |     |     | www.ijesat.com |     |     |     |     |     |     | Page 418 of 418 |     |
| ------------------- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --------------- | --- |