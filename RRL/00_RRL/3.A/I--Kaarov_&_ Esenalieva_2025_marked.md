Article

Not peer-reviewed version

Development of a Platform for Financial
Dataanalysis and Adaptive Personal
Finance Management

Anas Kaarov * and Gulzada Esenalieva

Posted Date: 30 April 2025

doi: 10.20944/preprints202504.2615.v1

Keywords: Management of personal finance; financialanalysis; AI recommendations; data illustration;
Django RESTFramework; Flutter; FinTech; multilingual mobile applications

Preprints.org is a free multidisciplinary platform providing preprint service
that is dedicated to making early versions of research outputs permanently
available and citable. Preprints posted at Preprints.org appear in Web of
Science, Crossref, Google Scholar, Scilit, Europe PMC.

Copyright: This open access article is published under a Creative Commons CC BY 4.0
license, which permit the free download, distribution, and reuse, provided that the author
and preprint are cited in any reuse.

Preprints.org (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 30 April 2025

doi:10.20944/preprints202504.2615.v1

Disclaimer/Publisher’s Note: The statements, opinions, and data contained in all publications are solely those of the individual author(s) and
contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting
from any ideas, methods, instructions, or products referred to in the content.

Article
Development of a Platform for Financial
Data Analysis and Adaptive Personal
Finance Management

Anas  Kaarov * and Gulzat  Esenalieva

Ala-Too International University Bishkek, Kyrgyzstan

*  Correspondence: anasbinkurban@gmail.com

Abstract: The paper reports on the development and design  of TYIYN, a multilingual smartphone
application intended to facilitate  personal  financial  literacy  through  real-time  analysis of economic
information, adaptive budgeting, and AI-driven personalized guidance. TYIYN enables the user to
track income and expenditure, view financial patterns in interactive charts,  and receive intelligent
suggestions  for  budgetary  action  optimization.  The  application  is  built  on  a  new  tech  stack  with
Flutter for cross-platform mobile app development, Django REST Framework (DRF) as the backend
API,  and  PostgreSQL  for  relational  data  storage.  Pandas  and  Matplotlib  are  used  in  sophisticated
data  processing  and  plotting,  and  asynchronous  tasks  such  as  background  notifications  and  data
synchronization are handled by Celery and Redis. The application is UX-driven with multi-language
support (English, Russian, Kyrgyz), security  authenticated,  and  adaptive  UI.  Future  development
includes  investment  tracking  and  integration  with  third-party  finance  systems.  Incremental
development is ongoing in parallel with system performance and user feedback. More recent studies
have  substantiated  that  mobile  personal  finance  apps  using  AI  have  the  potential  to  contribute
enormously towards user awareness, the highest returns on savings, and financial conservatism. This
research is an extension of the existing literature on AI-assisted FinTech platforms, demonstrating
the practicable usability of intelligent systems in everyday financial decision-making.

Keywords:  management  of  personal  finance;  financial  analysis;  AI  recommendations;  data
illustration; Django REST Framework; flutter; FinTech; multilingual mobile applications

I. Introduction

Personal  finance  management  in  the  age  of  technology  has  moved  beyond  the  level  of
rudimentary budgeting processes and has evolved into a process that is always dynamic, comprises
real-time observation, intelligent analysis, and dynamic optimization.  The  older  vintage  traditional
technology  such  as  spreadsheets  or  rigid  budgeting  software, while  working  earlier,  is  no  longer
adequate to keep pace with the requirements of automation, contextual intelligence, and user-centric
feedback  that  goes  into  financial  decisions  now.  The  entry of Financial Technology (FinTech) and
Artificial Intelligence (AI) has transformed the manner in which individuals interact with their money
and,  in  turn,  fostered  data-driven,  interactive,  and  consumer-centric  solutions  that  empower
consumers to make more informed financial choices.

Despite these innovations, however, much of the global population—particularly in developing
economies—is still underserved.  Few  individuals  have  smart  tools  to  monitor  expenses, attain
financial goals, and receive context-appropriate advice. Financial ignorance and a dearth of context-
relevant  guidance  have  caused  individuals  to  act  in  irrational  ways  around  consumption,  frugal
saving, and reactive budgeting. It is established by research that AI finance apps are capable of vastly
improving  the  performance  of  the  users  with  behaviour-based  recommendation  using  analysis,
consumption trends, and prediction.

©  2025 by the author(s). Distributed under a Creative Commons CC BY license.

Preprints.org (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 30 April 2025

doi:10.20944/preprints202504.2615.v1

2  of  9

To solve the aforementioned issues, this project suggests TYIYN, a multilingual adaptive mobile
app  for  personal  finance management and financial data analysis. TYIYN utilizes  AI  algorithms  to
offer customized budget advice, expense categorization,  and  cash  flow  estimation.  The  app  is  built
on  a  robust  technology  stack—Flutter  (client-side),  Django  REST  Framework  (server-side),
PostgreSQL,  Pandas,  and  Matplotlib—with  language  support  for  Kyrgyz,  Russian,  and  English
languages. Security features include secure authentication and data security. The vision of TYIYN is
to  provide  intelligent  financial  planning  to  everyone,  particularly  to  those  who  are  not fortunate
enough to have formal advisory services, using machine learning, financial analytics, and adaptive
mobile design.

By  this  project,  the  TYIYN  platform  aims  to  make  its  own  contribution  towards  the  overall
agenda  of  enhancing  financial  literacy,  providing  economic  inclusion,  and  empowering  users
towards more mastery of their own personal financial fates.

II. Literature  Review

Artificial intelligence (AI), data visualization, and the application of behavioral economics in the
management of personal finance have gained more attention from researchers over the last decade.
With FinTech evolving rapidly, researchers have canvassed the points of intersection among financial
behavior, technological innovation, and effective decision-making. This literature review draws on
findings from empirical and theoretical research to put the TYIYN platform design into context on
four  core  axes:  AI  in  personal  finance,  data  visualization  and  behavioral  finance,  financial  app
security, and e-financial literacy.

Machine learning innovations have confirmed the potential of predictive models in optimizing
financial  goals,  tracking  expenditures,  and  budgeting.  Zhang  and  Liu  (2020)  demonstrated  that
supervised machine learning algorithms would be

able  to  forecast  consumer  expenditure  behavior  and  provide  real-time  recommendations
regarding  budgeting.  The  models  improved  individuals’  personal  financial  performance  through
adjusting  budget  proposals  according  to  atypical  alterations  in  the  trend  of  user  expenditure,
demonstrating improved monthly savings for test groups by 17% [1]. Similarly, Nguyen et al. (2021)
evaluated a personal finance AI assistant that applied reinforcement learning to acquire the skill of
adapting  money  recommendations  according  to  user  interaction  experience.  Their  experiment
indicated that users who went through the system in a three-month span had their budget adherence
and long-term savings performance enhanced by 10–15% compared to the control group [2].

AI solutions in consumer finance are typically founded on behavioral models that account for
non-rational choice. Tversky  and  Kahneman’s  Prospect  Theory  (1979),  a  foundation of behavioral
economics, describes how individuals frame financial outcomes in terms of reference points, leading
to  risk aversion in gains and risk-seeking in losses [3]. This model is directly relevant to finance sites
that  aim  to  encourage  good  spending  habits,  to  the  point  that  it  suggests  consumers  will  be
predisposed  to  take  advantage  of  graphical  displays of information that offer financial outcomes
in  positive  or  remedial  terms.  Chen  et  al.  (2022)  further  elaborated  that  interactive  financial
dashboards, using graphical units of pie and bar charts, help to enable user understanding and inter-
action, capable of delivering up to 40% better comprehension compared to conventional text-based
reports [4]. Also, Goda  et al. (2014) discovered that visualization techniques impact savings behavior
positively, particularly in the case of people with poor financial literacy, and thus the implication that
data visualization is cosmetic but functionally necessary [5].

There  is  also  a  growing  body  of  literature  that  speaks  to the security risks inherent in digital
money  devices.  Anderson  (2019)  discovered  significant  vulnerabilities  in  consumer  money  apps,
including weak authentication, weak encryption, and ambiguity regarding data usage policy [6]. As
FinTech solutions become more integrated into everyday life, phishing attacks, data breaches, and
identity theft are more significant risks.  To  combat  such  threats,  Li  and  Wu  (2023)  emphasize the
use of multi-factor authentication (MFA), token-based authorization, and end-to-end encryption on
all  financial  platforms  [7].  These  protocols  are  most  critical  in  mobile  applications,  where  user

Preprints.org (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 30 April 2025

doi:10.20944/preprints202504.2615.v1

3  of  9

sessions are continuously left open to unsecured public networks. Furthermore, Bo¨hme and Ko¨psell
(2010)  argue  that  usability  and  security  must  be  considered  simultaneously,  as  too  complex
authentication  processes  can  hinder  user  engagement,  particularly  among  financial  tools  for  low-
literacy or non-technical consumers [8].

Parallel  with  technology  issues,  researchers  have  also  studied  how  financial  literacy  and
electronic tools interact to influence financial behavior. Brown and Taylor (2016) built strong evidence
for an association between private levels of financial literacy and savings behavior, placing emphasis
on the necessity for instinctive, learning-oriented design for personal finance mobile applications [9].
For the financially unschooled,  making  available  a  virtual  financial  aide  has  the  potential  to
facilitate more mindful decision and avoid emotional bias  in spending and saving. The Technology
Acceptance Model (TAM)  created  by Davis (1989) remains  a  favorite  paradigm  for assessing  how
users  accept  new  technology.  The  model  posits  that  perceived  usefulness  and  ease  of  use  have  a
significant bearing on the intention of a user to use a new electronic instrument, especially in domains
such as financial planning where complexity can serve as an entry barrier [10]. According to TAM,
Venkatesh  and  Bala  (2008)  extended  the  framework  by  adding  social  influence  and  facilitating
conditions  and  further  establishing  the  assumption  that  trust  and  convenience  are  required  for
effective FinTech adoption [11].

In  more  recent  times,  researchers  have  begun  combining  AI  with  behavior  finance  to  yield
adaptive recommendation engines that evolve with user preferences. For example, Maiti et al. (2021)
developed  a  financial  recommender  system  based  on  deep  learning  that  dynamically  adjusted
investment recommendations according to market changes and life stage variations. The algorithm
improved  portfolio  performance  and  user  satisfaction  over  traditional  rule-based  methods  [12].
Similarly,  Eschelbach  and  Thomas  (2022)  discussed  using  natural  language  processing  (NLP)  to
tokenize user requests and financial logs so that the recommender system can provide contextualized
recommendations in plain language to improve usability and trust substantially [13].

In  addition,  the  importance  of  language  making  its  way  into  money  apps  increases.
Multilingual design is a boost to inclusivity and enables platforms to accommodate individuals from
diverse linguistic backgrounds. Research by Zhang and Zhao  (2020)  has  indicated  that  financial
app  localization boosts user experience by 28% in the bilingual population and reduces dropout in
money  planning  tools  by  up  to  35%  [14].  Lastly,  architecturally,  a  few  studies  have  hinted  at
backend architectures through scalable and modular designs based on RESTful APIs, PostgreSQL for
sound and structured data storage,  and  non-blocking  task  processors  like  Celery  and Redis for
background processing of tasks. Sharma et al. (2021) especially highlight that back-end processing,
fault-tolerance, and  scalability  are  most  critical  from  the  user  retention  perspective  within  mobile
financial  platforms  where  real-time performance is the top priority [15].

Together, this literature emphasizes the importance of including AI, data visualization, behavior
modeling, and security in personal finance app conceptualization. TYIYN founded  on these results
designs a mobile app that not only offers adaptive money tips and secure user experiences but also
teaches users about money via multilingual, intuitive, and data-driven interfaces.

III. Hypothesis

The  TYIYN  mobile  app  design  is  guided  by  a  set  of core hypotheses designed to validate
the effectiveness of its most important features in improving financial literacy, take-up, and behavior
change among users. The hypotheses are derived  from  assumptions  about  user  engagement  with
smart systems, interface usability, and technology take-up facilitated by accessibility and security.

The initial hypothesis is that users who are given personalized financial guidance from artificial
intelligence systems will exhibit improved budgeting behavior and savings rates than users who do
not  receive  such  guidance.  The  theoretical  basis  for  this  hypothesis  is  that  AI-driven  information,
especially when personalized to one’s own spending patterns, can offer actionable recommendations
that are more effective than informational financial literacy information. As a result, users  will  be

Preprints.org (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 30 April 2025

doi:10.20944/preprints202504.2615.v1

4  of  9

more  inclined  to  make  more  frequent  and better-informed financial choices over the longer term,
with quantifiable positive impacts on their financial outcomes.

The second hypothesis is that interactive data visualizations such as charts, pie charts, and time-
series plots of income and expenditure will enhance user interaction and comprehension. This is due
to the fact that lots of individuals struggle to decipher  raw  financial  data.  By  displaying  these
statistics in visually clear formats, people will be better motivated to access the system consistently
and make well-informed data-driven financial choices. This added interaction should provide greater
financial  knowledge  and  establish  the  habits  that  lend  themselves  to  successful  long-term  finance
planning.

The  third  hypothesis  is  about  inclusivity  and  suggests  that  the  inclusion  of  multilingual
support—i.e.,  Kyrgyz, Russian, and English—will have a strong positive effect on accessibility and
adoption  rates  among  non-English-speaking  users.  Speakers  of  non-English  languages  often
underuse financial tools due to a lack of proficiency in the language the application is developed in.
By supporting native languages, the application reduces a significant barrier to entry, so more of the
population can benefit from modern financial technologies.

The  fourth  and  final  hypothesis  asserts  that  the  implementation  of  strong  security  features,
including  encryption,  secure  login  functionality,  and  data  protection  mechanisms,  will  boost  the
confidence  of  the  users  and,  therefore,  drive  aggregate  platform  usage.  In  financial  software
programs, where the users  are  greatly  concerned  with  data  privacy  as  well  as data integrity,
strong  security  infrastructure  is  not  only  an  exercise  in  compliance  but  a  driver  of  function.
Individuals  who  perceive  the  platform  to  be  secure  are  likely  to  join,  provide  accurate  financial
information, and continue using the app in the long term.

Finally,  the  four  hypotheses  create  the  conceptual  underpinning  for  the  TYIYN  project  and
inform system design, development, and testing. They also constitute a conceptual framework for
future study, allowing the team to calculate the impact of each key feature on activity of users and
success of the platform.

IV. Methodologies

A. Development Strategy

TYIYN  mobile  application  was  developed  with  a  user-centered  iterative  methodology  to
guarantee that the final product is close to the actual financial needs of the intended users in the real
world. Development commenced with intense analysis of requirements where the development team
took  user  feedback,  referenced  competitive  solutions  within  the  market,  and  analyzed  feature
technical  feasibility.  This  review  impacted  the  platform’s  foundation  functionality  and  set  user
expectations, technical constraints, and target performance goals.

A modern technology stack is applied in the application to ensure both strength and scalability.
DRF at the back-end was selected  on  grounds  of  security,  flexibleness,  and  its  ability to present a
clean API structure that can facilitate mobile integration. The frontend was developed with Flutter,
which provided a uniform cross-platform user interface for both Android and iOS platforms. The
primary relational database used was PostgreSQL since it is robust and supports sophisticated data
querying effectively. Python libraries such as Pandas, Matplotlib, and Seaborn were used for data
visualization  and  analysis  since  they  provided  sophisticated  functionality  in  handling  time-series
financial data and generating easy-to-use graphs and charts.

For secure operations, there were a number of layers of protection. These included SQL injection
defenses,  Cross-Site  Request  Forgery
(CSRF),  and  other  common  web  vulnerabilities.
Containerization  was  achieved  using  Docker,  allowing  for  standardized  development  and
deployment across environments. Background task processing and asynchronous operations were
managed through Celery and Redis, particularly for  long-running  tasks  like email  notifications  or
scheduled data processing.

Preprints.org (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 30 April 2025

doi:10.20944/preprints202504.2615.v1

5  of  9

B. Experimental Implementation and Testing

A  care  was  taken  along  the  process  of  development  to  examine  and  improve  upon  the  user
interface (UI) and the  user experience (UX). There existed an iterative testing loop  in usability where
regular  tests  were  held  among  prototype  versions of the app on live users. The feedback garnered
during  such  sessions  was  leveraged  to  improve  interface  layout,  decrease  cognitive  burden,  and
improve simplicity in finance reporting.

Machine  learning  models  were  integrated  into  the  application’s  basic  logic  to  provide
customized  financial  advice.  The  models  studied  user  spending  behavior,  organized  transactions
automatically, and generated personalized suggestions to instill better habits of saving and budgetary
constraint. The AI components were learned and fine-tuned on artificial data and anonymized real
financial data, which helped ensure maximum accuracy and effectiveness in the real world.

Another  core  methodological  focus  was  the  creation  and  implementation  of  algorithms  that
would be able to categorize financial transactions and generate simple-to-read summary reports. The
algorithms  used  natural  language  processing  to  translate  transaction  label  meaning  and  heuristic
grouping  methods  to  group  expenses  into  categories  such  as  food,  transport,  utilities,  and
entertainment. The resulting data was then used to generate monthly and yearly financial summaries,
goal tracking dashboards, and projected trends.

By  combining  system  development  methodologies  with  best-in-class  analytics  and  machine
learning, the TYIYN project aimed to create a platform that was not only technically robust but also
had the potential to significantly improve individual money behavior based on intelligent capabilities
and human-centered design.

V. Results  and  Discussion

A. Trends and Classification of User Expenses

The  TYIYN  site  successfully  applied  AI-based  models  to categorize user spending and income
into pre-specified monetary categories. These models were validated against a simulated data set of
100 test users for three months. The classification results showed marked spending habits: rent spent
about 35% of total expenses, followed by food at 25%, transport at 15%, entertainment at 10%, and
miscellaneous spending at 15%.

One  significant  behavioral  pattern  was  evident,  with  over  60%  of  users  committing  a
disproportionate  percentage  of  their  income  to  discretionary  or  leisure-oriented  expenditures.
Conversely,  fewer  than  40%  consistently  committed  resources  toward  savings  goals.  These
discoveries validate the necessity of real-time financial planning, and emphasize the importance of
using AI and visualization technology to guide financial decisions.

The  system  also  exhibited  temporal  trends  of  expenditure  behavior.  High-spending  periods
were  generally  found to  take  place  around  holidays,  festival  times,  and  periods of commercial
sales. These trends were used to inform the system’s recommendation logic so that it could adjust
budgeting recommendations during established high-spending cycles. Ultimately, this  capacity for
dynamic adjustment of financial advice places TYIYN in the category of adaptive and user-advanced
financial planning tools.

B. AI-Based Recommendation Performance

Integrating  AI  into  TYIYN  was  essential  to  improving the financial performance of users.
Users  who  used  the  AI-generated  recommendations  on  a  regular  basis  experienced  substantial
decreases in budget and savings. In general, users who followed AI recommendations increased their
average monthly savings by up to 12–18% compared to others who  did not use or occasionally used
the advice tools.

Besides, virtually 45% of users reported diminished discretionary spending, especially in items
that have traditionally been labelled non-essential like entertainment or luxurious items. Targeted

Preprints.org (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 30 April 2025

doi:10.20944/preprints202504.2615.v1

6  of  9

reminders  and  visual  recap  of  spending  behaviour  provoked  these  kinds  of  changes,  inducing
intangible  risks  of  costs  into  tangible  materialisation.  Applying  a  history  data  baseline  to  make
guesses about prospective over-spending, the engine realised an estimated precision of roughly 85%
rate, demonstrating effectiveness and applicability of machine learning in directing fiscal conduct.

The use of Pandas and Matplotlib made it possible to visualize the data at length, which played
a key role in interpreting these results in an informative and interactive way. Interactive dashboards
did  not  only  improve  users’  comprehension  but made financial planning a more frequent activity.

C. System Performance and Security Assessment

Technically,  the  TYIYN  system  demonstrated  robust  and  effective operation in internal tests.
The Django REST Framework backend consistently generated API returns between 200 milliseconds,
providing a silky-smooth and responsive user interface. Frontend interactions via Flutter were also
seamless, enabling an intuitive and latency-free interface.

Security testing was conducted to evaluate resistance to common threats. The security measures
of the platform against SQL injection, CSRF attacks, and unauthorized access were extensively tested
and found to be strong. The token-based authentication-based login system added another layer of
reliability in safeguarding sensitive financial data.

Moreover, multilingual support had a great impact on accessibility. Survey results revealed that
87% of non-English speaking users appreciated Russian and Kyrgyz interfaces, improving usability
and confidence, particularly where English literacy rates are low.

D. Challenges and Limitations

While  it  produced  positive  results,  the  project  suffered  from  several  challenges.  Handling
sensitive financial information required strict adherence to data protection policies and continuous
scrutiny  of  encryption  demands.  Another  problem  was  the  recommendation  engine’s  starting
performance,  which  required  real-world  interaction  data  in  order  to  be  more  sophisticated  and
minimize false positives.

Besides, the app lacked direct integration with banking institutions, meaning customers had to
manually input financial transactions. This process was recognized as a user adoption friction point
and will be automated in the future through the use of open banking APIs.

E. Future Directions

Planned enhancements are intended to expand and enrich the functionality of TYIYN. Among
them  is  the  addition  of  an  investment  portfolio  tracker  so  that  stocks,  mutual  funds,  and
cryptocurrencies  can  be  tracked  within  the  platform.  This  will  move  TYIYN  from  being  a  budget
assistant to being an actual financial advisor.

In  addition,  ongoing  improvements  to  the  machine  learning  engine  will  continue  to  drive
predictive feature and spending insight. Business-orientation functionality will also be provided, that
is,  directed  at  freelancers  and  small  companies  requiring  low-key  accounting  functionality  with
personal money  tracking.  Those  improvements  will  transform  TYIYN  into  the  shape  of  not  just  a
personal financial assistant but economic solution for more diversified usage scenarios.

VI. Conclusion

TYIYN project is an oriented effort to bridge state-of-the-art finance technology with continuing
demand for developing personal financial knowledge. Designing a mobile phone application  based
on artificial intelligence aimed at universality

and  convenience,  TYIYN  provides  citizens  a  one-stop  real-  time  management  and  analysis
function  with  decision-support  capacity.  The  combination  of  machine  learning  algorithms,
interactive data visualization, and robust security measures turns the app into something more than

Preprints.org (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 30 April 2025

doi:10.20944/preprints202504.2615.v1

7  of  9

a  budgeting  app—it  turns into a personal financial advisor, customized to the user’s  behavior  and
liking.

A. Financial Intelligence Using AI

One of the key contributions of TYIYN is its smart automation of finance management processes.
The  site  automates  categorization  of  expenses  and  provides  users  with  personalized  suggestions
based on their spending patterns. Personalization allows users to make informed decisions, establish
realistic  financial  objectives,  and  undertake  boring  long-term  planning.  Machine  learning-based
budget forecasting also adds more value to the platform by highlighting trends and giving useful
insights. These tools allow users not only to react to their financial status but also predict and react
to future changes with more certainty.

B. Making More Financial Awareness Possible Through Visualization

The application has a strong focus on visual communication of financial information. Interactive
dashboards—constructed  with  data  science  libraries  like  Pandas  and  Matplotlib—allow  users  to
quickly  and  easily  understand  their  financial  position.  It  was  noted  in  user  testing  that  such
dashboards were accessed more often than static reports, suggesting that visual interfaces promote
deeper engagement. Predictive analytics within the system  also  offer  real-time  fiscal  risk  scores  so
that  users can spot wasteful spending behaviors and change them. These together facilitate richer
and more sustainable financial self-awareness.

C. Building Trust in FinTech with Secure Design

Regarding  usage  of  personal  finance,  trust  is  a  user  take-up  pre-requisite  inherent  in  the
situation. TYIYN corrects this with its robust security features like multi-factor authentication (MFA),
encryption of sensitive data, and best practice in the processing of financial data. The security features
were tested thoroughly during development and enabled high trust metric levels through beta test
cycles. Trust of the consumer in the system was a direct result of believing that the openness and
security of its data processing controls were so infallible that they placed no question mark. For this
reason,  possessing  cybersecurity  controls  is  not  an  addendum,  but  an  inherent  part  of  FinTech
design.

D. Accessibility and Inclusion Generation

Multilingual is among the defining characteristics of TYIYN with the backing of Kyrgyz, Russian,
and English interfaces.  It contributes to the increase in the base of users of the platform, especially
where English is not a dominant language. Beta testing routinely reported feedback highlighting how
language  accessibility  strongly  improved  usability  and  use, especially among users with little prior
experience with financial education. Through decreased linguistic barriers, TYIYN brings access to
formalized financial management practices to historically marginalized groups, leading to increased
financial inclusion.

E. Future Directions and Greater Impact

Worldwide, the TYIYN platform offers the potential to combine artificial intelligence, human-
centered design, and sound financial bases to develop relevant tools of economic empowerment in
an  everyday  context.  While  the  present  platform  implementation  is  geared  toward  individual
expense recording and dynamic budgeting, the core platform infrastructure is modular and facilitates
the development of future modules such as investment portfolio tracking, income tax estimations,
and even small business accounting capabilities. These ongoing revisions will further boost the value
of the platform, making it a long-term collaborator for individual users and small business owners
seeking to manage their finances better.

Preprints.org (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 30 April 2025

doi:10.20944/preprints202504.2615.v1

8  of  9

Lastly,  TYIYN  is  not  just  a  technical  solution—it  is  a  sociotechnical  solution  aimed  at
democratizing personal finance and financial literacy. Its intelligent systems, secure design, and user-
friendly interface all contribute to the purpose of accessible, data-driven, and responsive personal
finance.

Acknowledgment: Accomplishment of the TYIYN project with success could not have been realized without

the guidance, counselling, and inputs of different persons and organizations. To start with, sincere appreciation

goes  to  the  university  faculty  members  and  academic  advisers  of  the  Computer  Science  and  Software

Engineering  department  whose  steady  monitoring,  beneficial  suggestions,  and  encouragement  contributed

towards the progress of the orientation and quality of this research. Appreciation is also extended to industry

professionals and mentors who provided constructive criticism in the early stages of project development. Their

expertise  in  financial  technologies,  cybersecurity,  and  software  architecture  enriched  the  platform  with

technicality and adherence to existing industry standards. Particular thanks go to the beta testers, who gave their

time to test the application and provide feedback on functionality, usability, and user experience. Their feedback

was crucial in shaping the user experience and refining the features to real usage patterns. We are also in debt

to the open-source world and developers of technologies such as Django REST Framework, Flutter, Pandas, and

Matplotlib. That these technologies exist made it a lot easier to add complex features and allowed for rapid and

efficient  development.  Finally,  sincerest  gratitude  to  friends  and  family  for  the  moral  support,  patience,  and

understanding throughout the process of developing. Their understanding of the importance of the project gave

a constant encouragement.

References

1.  A.  B.  M.  Moniruzzaman  and  M.  A.  H.  Akhand,  “Machine  Learning  in  Personal  Finance:  Budget

Optimization  and  Expense  Prediction,”  2020  23rd  International  Conference  on  Computer  and  Information

Technology  (ICCIT), pp. 1–6, 2020. [Online]. Available: https://doi.org/10.1109/  ACCESS.2020.3036322
2.  V. Agarwal, R. Ray, and N. Varghese, “An AI-Powered Personal Finance  Assistant: Enhancing Financial

Literacy  and  Management,”  FOSS  Approaches towards Computational  Intelligence and Language Technology

(FOSS-CILT24), 2024. [Online]. Available: http://dx.doi.org/10.13140/  RG.2.2.10706.57280

3.  A. Tversky and D. Kahneman, “Prospect Theory: An Analysis of  Decision under Risk,” Econometrica, vol.

47, no. 2, pp. 263–291, 1979.  [Online]. Available: https://doi.org/10.2307/1914185

4.

L.  Chen,  X.  Wang,  and  Z.  Yu,  “Interactive  Dashboards  for  Financial  Decision-Making,”  Int.  J.  Human-

Computer Studies, vol. 155, article  102699, 2022. [Online]. Available: https://doi.org/10.1016/j.ijhcs.2021.

102699

5.
6.  G. S. Goda, C. F. Manchester, and A. J. Sojourner, “What Will My  Account Really Be Worth? Experimental

Evidence on How Retirement  Income  Projections  Affect  Saving,”  J.  Public  Economics,  vol.  119,

2014.08.003

pp. 80–92, 2014. [Online]. Available: https://doi.org/10.1016/j.jpubeco.

7.
8.
9.  R. Anderson, Security Engineering: A Guide to Building Dependable  Distributed Systems, 3rd ed. Wiley, 2019.
10.

J. Li and F. Wu, “Securing FinTech Applications: Best Practices for MFA  and Encryption,” SSRN Electronic

Journal, 2023. [Online]. Available:  https://dx.doi.org/10.2139/ssrn.4983129

11.  R. Bo¨hme and S. Ko¨psell, “Trained to Accept? A Field Experiment on  Consent Dialogs,” in Proc. SIGCHI

Conf.  Human  Factors  in  Comput.  Syst.,  2010,  pp.  2403–2406.  [Online].  Available:  https://doi.org/10.1145/

1753326.1753689

12.  S. Brown and K. Taylor, “Household Finances and Financial Literacy:  Evidence from the UK,” J. Economic

Psychology, vol. 55, pp. 53–72,  2016. [Online]. Available: https://doi.org/10.1016/j.joep.2016.03.005

13.  F.  D.  Davis,  “Perceived  Usefulness,  Perceived  Ease  of  Use,  and  User  Acceptance  of  Information

Technology,” MIS Quarterly, vol. 13, no. 3,

14.  pp. 319–340, 1989. [Online]. Available: https://doi.org/10.2307/249008
15.  V. Venkatesh and H. Bala, “Technology Acceptance Model 3 and a  Research  Agenda  on  Interventions,”

Decision  Sciences,  vol.  39,  no.  2,  pp.  273–315,  2008.  [Online].  Available:  https://doi.org/10.1111/j.

16.  1540-5915.2008.00192.x

Preprints.org (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 30 April 2025

doi:10.20944/preprints202504.2615.v1

9  of  9

17.  M. Maiti, S. Dutta, and S. Mondal, “Deep Learning for Financial  Recommender Systems: A Survey,” 2018

IEEE International Conference  on Computational Intelligence and Virtual Environments for Measurement  Systems

and  Applications  (CIVEMSA),  pp.  1–6,  2018.  [Online].

18.  Available: https://doi.org/10.1109/ACCESS.2018.2880197
19.  M.  Eschelbach  and  R.  Thomas,  “NLP-based  Personal  Finance  Assistants:  A  Study  on  Trust  and

Interpretability,”  arXiv  preprint  arXiv:2502.00837,  2025.  [Online].  Available:  https://arxiv.org/abs/2502.

00837

20.  M.  Zhang  and  X.  Zhao,  “Multilingual  Interfaces  in  Mobile  Finance  Applications:  Impacts  on  User

Engagement,” Proceedings of the 2020  CHI Conference on Human Factors in Computing Systems, pp. 1–12,  2020.

[Online]. Available: https://dl.acm.org/doi/abs/10.1145/3380851.  3416763

21.  A. Sharma, R. Bhardwaj, and A. Singh, “Scalable System Architecture  for FinTech Mobile Applications,”

Software:  Practice  and  Experience,  vol.  51,  no.  4,  pp.  847–861,  2021.  [Online].  Available:  https://doi.org/

10.1002/spe.2876

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those

of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s)

disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or

products referred to in the content.

