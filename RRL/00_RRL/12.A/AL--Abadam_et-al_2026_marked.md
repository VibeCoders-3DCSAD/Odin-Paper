Development of A Cross-Platform Application Blue-Collar
Marketplace with Prescriptive Analytics Using Linear
Programming Algorithm

John Bernard Abadam
Information Systems Department
Technological Institute of the Philippines
Metro Manila, Philippines
qjblabadam@tip.edu.ph

Risty Acerado
Information Systems Department
Technological Institute of the Philippines
Metro Manila, Philippines
racerado.is@tip.edu.ph

Avan Cevlar Cuevas
Information Systems Department
Technological Institute of the Philippines
Metro Manila, Philippines
qakcuevas@tip.edu.ph
Roselia Morco∗
Information Systems Department
Technological Institute of the Philippines
Metro Manila, Philippines
rmorco@tip.edu.ph

Abstract
Unemployment remains a persistent issue in the Philippines, espe-
cially among low- and middle-income earners who lack access to
immediate and flexible work opportunities. To address this, a cross-
platform application was developed to facilitate job matching for
blue-collar workers. The developed system integrates prescriptive
analytics through a linear programming algorithm to provide opti-
mized and fair pricing suggestions for job posts, helping employers
make data-informed decisions while ensuring equitable compen-
sation for freelancers. Data inputs for the algorithm were sourced
from the Public Employment Service Office (PESO) and Katherine
Townhomes. Additional features such as identity verification and a
feedback system were incorporated to promote trust and service ac-
countability. Developed using the Rapid Application Development
(RAD) model, the project used an iterative approach, comprising
planning, design, construction, and deployment phases, to ensure
user-centered outcomes. The application was evaluated using the
ISO/IEC 25010 software quality model, with a focus on functional
suitability, performance efficiency, usability, and reliability. Evalua-
tion results revealed high user satisfaction and system effectiveness,
with the platform receiving a rating of 4.98 out of 6 from a diverse
group of IT professionals and regular users. The developed system
not only delivers a functional and accessible job marketplace but
also contributes to bridging employment gaps by leveraging tech-
nology to foster fair labor practices, transparency, and economic
empowerment. The project demonstrates the potential of intelli-
gent platforms to address employment challenges in developing
countries by creating inclusive, data-driven, and user-centric digital
solutions.

∗Corresponding author

This work is licensed under a Creative Commons Attribution 4.0 International License.
ICSIM 2026, Yokohama, Japan
© 2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2173-1/2026/01
https://doi.org/10.1145/3796315.3796343

CCS Concepts
• Information systems; • Information systems applications; •
Decision support systems applications; • Data analytics;

Keywords
applied computing, operations research, linear programming, soft-
ware and its engineering, rapid application, development, blue-
collar jobs, job marketplace, prescriptive analytics, cross-platform
application development, linear programming

ACM Reference Format:
John Bernard Abadam, Avan Cevlar Cuevas, Risty Acerado, and Roselia
Morco. 2026. Development of A Cross-Platform Application Blue-Collar
Marketplace with Prescriptive Analytics Using Linear Programming Al-
gorithm. In 2026 The 9th International Conference on Software Engineering
and Information Management (ICSIM 2026), January 21–23, 2026, Yokohama,
Japan. ACM, New York, NY, USA, 7 pages. https://doi.org/10.1145/3796315.
3796343

1 INTRODUCTION
Employment remains a complex and persistent challenge in the
Philippines, particularly for low-income individuals and those with-
out access to quality education or professional training. Despite
the country’s economic growth in recent years, a substantial por-
tion of the population continues to face barriers to securing stable
and fulfilling employment. These barriers include limited access to
formal job opportunities, underemployment, and a lack of inclusive
systems accommodating individuals with varying educational back-
grounds and skill levels [1]. Simultaneously, rapid urbanization and
demanding professional work have left many high-income earners
with limited time for managing day-to-day personal or household
tasks. This growing disparity between labor supply and demand
highlights an urgent need to reassess how work is distributed, ac-
cessed, and valued across various sectors of society. Understanding
employment not merely as a matter of economic necessity but
as a pathway to social equity highlights the importance of inclu-
sive, flexible, and technology-driven solutions. In the Philippine
context, where informal work and digital connectivity intersect,

203ICSIM 2026, January 21–23, 2026, Yokohama, Japan

John Bernard Abadam et al.

exploring alternative employment systems is crucial for addressing
unemployment and adapting to evolving labor demands.

This paper explores these challenges in depth, drawing from
existing labor trends, government initiatives, and socioeconomic
data to identify gaps in the current employment landscape. It also
lays the foundation for proposing potential innovations to make
job opportunities more accessible and responsive to the diverse
needs of the Filipino workforce.

1.1 Background of the Study
Unemployment remains a pressing socioeconomic concern, partic-
ularly in developing countries such as the Philippines. It refers to
individuals who are actively seeking employment but are unable
to secure suitable work. Globally, an estimated 192 million peo-
ple faced this challenge in 2022 due to limited access to education,
scarce job opportunities, and inadequate training [2]. The World
Bank reported that the global unemployment rate in 2023 stood
at 5.1%, representing approximately 178 million individuals strug-
gling to find decent work opportunities [3]. The consequences of
unemployment extend beyond personal economic hardship, as they
also threaten social stability and long-term national development.
One alarming outcome of persistent unemployment is its corre-
lation with increased crime rates. Socioeconomic stressors, such
as income inequality, limited opportunities, and unemployment,
are often cited as key factors that drive individuals toward unlaw-
ful activities in an attempt to meet their basic needs [4, 6]. These
actions not only affect direct victims but also severely impact the
families of offenders, especially children, by compromising their
health, emotional well-being, education, and future economic mo-
bility [14]. Addressing unemployment is thus critical not only for
economic progress but also for promoting public safety and social
equity [6].

In the Philippines, as of April 2023, approximately 2.04 million
Filipinos were unemployed, a figure that, while seemingly modest in
percentage terms, affects millions of households [1]. To address this,
several programs have been introduced. The Public Employment
Service Office (PESO) facilitates access to job vacancies, particularly
for blue-collar workers, and connects employers with potential
hires [9]. Similarly, JobStart Philippines, under the Department
of Labor and Employment (DOLE), provides life skills training
to improve youth employability [9]. The Government Internship
Program (GIP) also offers individuals aged 18–30 the opportunity
to gain work experience and develop practical competencies [13].
While these government-led initiatives show promise, their im-
plementation faces several limitations. Many programs lack long-
term support structures, provide minimal stipends, and rely heavily
on traditional employer-employee arrangements that may not align
with the realities of low-income individuals. For many, daily sub-
sistence takes precedence over participating in extended training
or internship programs. Consequently, short-term, hourly-based
employment, often associated with blue-collar or gig work, emerges
as a more practical and immediate alternative. However, access to
such jobs remains constrained due to trust issues, informal hiring
practices, and the prevalence of recruitment scams [7, 12].

Recognizing these challenges, this study proposes a technology-
driven employment platform focused primarily on blue-collar job

opportunities, aligning with the United Nations Sustainable De-
velopment Goal (SDG) 8: Decent Work and Economic Growth,
which advocates for inclusive and productive employment for all
[5]. This cross-platform system, accessible via mobile and web, aims
to empower both freelancers and employers by providing secure
job postings, optimized pricing, and identity verification mecha-
nisms, thereby enhancing trust and safety in the hiring process.
By expanding access to verified, short-term employment opportu-
nities for underserved populations, the platform aims to enhance
economic resilience, reduce informality in the labor market, and
promote inclusive economic participation [10, 11].

By adopting this approach, it contributes to broader efforts to
promote sustainable economic growth, reduce inequalities in em-
ployment access, and build a more responsive and secure labor
market, particularly for low-income and underrepresented workers
in the Philippines.

The study aims to design and evaluate a cross-platform job-
matching system that supports efficient interaction between free-
lancers and employers. Specifically, it seeks to implement an ad-
ministrative dashboard for effective monitoring and visualization
of key operational data, integrate descriptive and prescriptive ana-
lytics through a Linear Programming (LP) model to support pricing
recommendations, and assess the overall quality and performance
of the developed system using the ISO/IEC 25010 software qual-
ity model, with emphasis on functional suitability, performance
efficiency, usability, and reliability.

1.2 Significance of the Study
Providing accessible job opportunities for low- to middle-income
earners is a shared vision among many policymakers seeking to
ensure a quality and sustainable standard of living for citizens.
The developed system may contribute to this goal by promoting
fair, transparent, and technology-driven employment practices that
foster safer and more sustainable ways to earn a living.

The primary beneficiaries of this initiative are individuals who
struggle to find short-term or flexible work opportunities that align
with their skills and daily availability. Through this platform, free-
lancers can easily browse available jobs suited to their abilities
and preferences, enabling them to earn immediate income through
short-duration tasks. This flexibility allows workers to manage
their schedules more effectively compared to traditional eight-hour
work arrangements, ultimately supporting their financial needs
and reducing work-related stress.

For employers, particularly those from higher-income house-
holds, the developed system provides a convenient means of hiring
workers on demand for occasional or unplanned tasks such as
household cleaning, delivery, or personal assistance. This arrange-
ment promotes efficiency and cost savings, as employers pay only
for completed tasks rather than maintaining long-term employment
contracts.

Additionally, the developed system enhances safety and account-
ability through features such as user identity verification, requiring
government-issued identification before registration. This verifica-
tion process fosters trust between employers and freelancers while
ensuring a secure digital environment. By providing legitimate
earning opportunities, the platform also contributes to reducing

204Development of A Cross-Platform Application Blue-Collar Marketplace with Prescriptive Analytics Using Linear
Programming Algorithm

ICSIM 2026, January 21–23, 2026, Yokohama, Japan

petty crimes motivated by financial hardship, thereby supporting
community safety and social stability.

emphasizing service quality and user satisfaction through verified
professional workers and 24/7 support [12].

At the policy level, the project aligns with United Nations Sus-
tainable Development Goal 8: Decent Work and Economic Growth,
by fostering inclusive employment and reducing unemployment
within local communities. Beyond its social impact, the project
also offers value to researchers and organizations by generating
business intelligence and actionable insights through data analytics.
These findings can inform future innovations, enhance labor mar-
ket strategies, and inform the development of data-driven policies
that promote equitable economic participation.

The developed system holds both societal and research signifi-
cance, empowering workers, aiding employers, promoting ethical
employment practices, and contributing to national and global goals
of sustainable and inclusive economic growth.

2 REVIEW OF RELATED LITERATURE
This section presents relevant studies, government initiatives, and
digital innovations that address unemployment and promote liveli-
hood development. It also includes discussions on conceptual and
architectural frameworks supporting the developed system. The
literature review highlights the intersection of technology, data
analytics, and socioeconomic policies in providing employment
opportunities and enhancing national productivity.

In response to persistent unemployment, government agencies
and policymakers have implemented programs to provide accessible
job opportunities and skills training. In the Philippines, the Public
Employment Service Office (PESO) serves as a local hub connecting
employers and job seekers. It provides listings for various positions
such as service crew, production workers, and call center agents,
bridging the gap between workforce supply and labor demand [9].
Another initiative, JobStart Philippines, implemented by the
Department of Labor and Employment (DOLE), aims to enhance
employability among the youth by offering training and life skills de-
velopment [9]. After completing the training phase, participants are
referred to partner employers for internships, giving them practical
experience and professional exposure. Similarly, the Government
Internship Program (GIP) provides short-term work opportunities
in public offices to individuals aged 18–30, enabling them to gain
valuable workplace experience while receiving financial assistance
[13]. These initiatives collectively promote workforce readiness
and contribute to economic resilience.

However, despite their benefits, such programs face challenges
in scalability, funding, and accessibility. Many participants from
low-income backgrounds prioritize immediate income over long-
term training, which limits their participation in programs. Conse-
quently, flexible, short-term employment remains an attractive and
necessary option for many workers.

The rise of digital technologies has given birth to various job-
matching platforms that address unemployment by linking workers
to short-term or task-based opportunities. One notable example is
TaskRabbit, a U.S.-based platform that connects freelancers with
clients seeking assistance with services such as plumbing, delivery,
and home repairs [12]. Similarly, Handy focuses on professional
home services like cleaning, furniture assembly, and general repairs,

Another example, Snagajob, streamlines recruitment for part-
time and full-time service jobs in the hospitality industry by allow-
ing job seekers to maintain digital profiles that serve as employment
applications. This approach streamlines hiring and minimizes pa-
perwork, making the process more efficient for both employers and
job seekers [12].

These existing platforms demonstrate how technology can en-
hance employment access, improve user experience, and foster trust
through identity verification and performance-based feedback sys-
tems, features that also inform the design of the proposed platform
in this study.

The integration of data analytics into employment systems has
gained traction in both private and public sectors. Research by
Galdon-Sanchez and Gil [10] found that the adoption of big data
and analytics provides actionable insights for improving produc-
tivity, innovation, and job creation, particularly among small and
medium-sized enterprises (SMEs). Data-driven decision-making
enables organizations to develop strategies that more closely align
with labor market trends, ultimately reducing unemployment and
enhancing competitiveness.

During the COVID-19 pandemic, predictive analytics played a
crucial role in tracking unemployment patterns. Simionescu and
Cifuentes-Faura [15] leveraged Google Trends data to estimate
monthly unemployment rates in Spain and Portugal, providing pol-
icymakers with insights to anticipate economic challenges and take
timely action. This example underscores how analytics tools can
support governments and organizations in managing workforce-
related issues, a concept that informs the prescriptive analytics
aspect of the research project.

The relationship between employment and economic growth
has been widely studied in development economics. Haider et al.
[11] emphasized that countries with higher employment intensity
exhibit stronger GDP growth, reinforcing the need to create jobs
that contribute meaningfully to national output. Similarly, Correa
[8] found that unemployment hurts GDP, while moderate inflation
may stimulate economic activity by encouraging consumption and
investment. These findings highlight the importance of balanced
macroeconomic policies that support job creation while maintain-
ing economic stability.

Furthermore, Sustained productivity growth, supported by tech-
nological investment and infrastructure development, can con-
tribute to the creation of high-value jobs and overall economic
advancement. Thus, leveraging digital innovation to connect work-
ers with employment opportunities not only addresses individual
livelihood concerns but also contributes to broader national devel-
opment goals.

The reviewed literature demonstrates that both government pro-
grams and digital job-matching platforms play significant roles
in addressing unemployment. However, traditional government
programs often lack flexibility, while existing commercial platforms
are primarily targeted toward developed economies. Bridging these
gaps requires a localized, inclusive, and data-driven solution tai-
lored to the Philippine context.

205ICSIM 2026, January 21–23, 2026, Yokohama, Japan

John Bernard Abadam et al.

support tools. Particular emphasis was placed on addressing incon-
sistent job pricing and the lack of data-driven recommendations
in existing platforms, which led to the inclusion of a prescriptive
analytics component using Linear Programming.

3.2 User Design Phase
In the User Design phase, interface prototypes were developed
using tools such as Figma and WordPress, later transitioning to a
PHP-based architecture for full front-end and back-end integration.
Iterative design sessions were conducted, incorporating continuous
feedback from potential users to refine navigation, usability, and
visual layout.

An administrative dashboard was designed to visualize job mar-
ket trends, service category distributions, and pricing analytics.
During this phase, the analytics framework was finalized, com-
bining descriptive analytics (for historical and trend analysis) and
prescriptive analytics (for optimized job pricing recommendations).

3.3 Construction Phase
The Construction phase involved full-scale system development.
The core system architecture was implemented using PHP, while
analytics computations were handled through Python libraries. Ma-
jor system functionalities such as user authentication, job posting,
application matching, messaging, and dashboard reporting
were developed and tested.

3.3.1 Linear Programming Model Specification. As part of the pre-
scriptive analytics component, a Linear Programming (LP) model
was developed to assist employers in determining fair, competitive,
and market-aligned job pricing.

a) Model Type: The model is a single-objective Linear Program-
ming model. No normalization or scaling was required, as
all monetary values were expressed in consistent currency
units (PHP).

b) Decision Variable: The decision variable is the recommended

job price, expressed in Philippine Pesos (xxx).

c) Objective Function: The objective of the model is to maxi-
mize employer value by setting a competitive price that bal-
ances affordability and freelancer attractiveness. Formally,
the objective is expressed as Maximize Z=x{Maximize } Z =
xMaximize Z=x, reflecting the goal of achieving the highest
feasible price within market and system constraints, thereby
improving job acceptance rates while maintaining employer
budget efficiency.

d) Constraints: The pricing model is subject to a minimum
market price constraint (x≥Pminx ge P_{min}x≥Pmin) to
ensure compliance with acceptable market or freelancer
rates, a maximum employer budget constraint (x≤Pmaxx
le P_{max}x≤Pmax) to prevent exceeding the employer’s
stated budget, and a demand-based constraint (x≤Pdemandx
le P_{demand}x≤Pdemand) to maintain competitiveness un-
der prevailing market demand. A non-negativity constraint
(x≥0x ge 0x≥0) is also imposed.

e) Parameter Definitions. Solution Method: The model pa-
rameters are defined in Table 1. The LP model was solved
using the Simplex Method, producing feasible and optimal
pricing recommendations. These recommended prices were

Figure 1: Three-tier Architecture

The research project responds to this need by integrating pre-
scriptive analytics and secure identity verification into a cross-
platform employment marketplace. Through these innovations,
it aims to enhance job accessibility, improve employer-employee
trust, and contribute to sustainable economic growth aligned with
United Nations Sustainable Development Goal 8: Decent Work and
Economic Growth [5].

The system employs a three-tier architecture, comprising the
presentation, logic, and data layers, each serving a distinct role in
ensuring efficiency and scalability. Figure 1 shows the system’s ar-
chitectural framework and how these layers interact to support its
overall functionality. The presentation layer, developed using PHP
and JavaScript, provides an intuitive user interface for employers,
freelancers, and administrators. It emphasizes responsive design
and seamless accessibility across both desktop and mobile plat-
forms to enhance user experience. The Logic Layer, implemented
primarily with Python scripts, serves as the system’s core process-
ing component. It executes pricing recommendations based on
the Linear Programming model while managing the business logic
responsible for job matching and analytics generation. Finally, the
Data Layer utilizes a MySQL database to store essential records,
including user profiles, job postings, applications, and transaction
histories. This layer ensures efficient data retrieval, consistency,
and integrity across all system operations, thereby supporting the
platform’s stability and reliability.

3 RESEARCH METHODOLOGY
3.1 Requirements Planning Phase
The development process began with the Requirements Planning
phase, where the research team analyzed existing digital job plat-
forms and conducted informal interviews with potential users to
identify functional requirements, pricing challenges, and usability
concerns. Based on these findings, the system was conceptualized
as a digital job marketplace for blue-collar workers and employers
in Metro Manila, focusing on short-term services such as cleaning,
delivery, handyman work, and personal assistance.

During this phase, core system functionalities were identified, in-
cluding distinct user roles (freelancer, employer, and administrator),
job posting and matching workflows, and analytics-driven decision

206Development of A Cross-Platform Application Blue-Collar Marketplace with Prescriptive Analytics Using Linear
Programming Algorithm

ICSIM 2026, January 21–23, 2026, Yokohama, Japan

Table 1: Parameter Definitions

Parameter

Description

𝑃𝑚𝑖𝑛
𝑃𝑚𝑎𝑥
𝑃𝑑𝑒𝑚𝑎𝑛𝑑

Minimum acceptable market price
Employer’s maximum budget
Market demand-based price ceiling

Unit

PHP
PHP
PHP

integrated into the system dashboard and presented to em-
ployers during job posting.

3.4 Cutover Phase
Following system construction, the Cutover phase focused on de-
ployment, integration testing, and system refinement. Integration
testing ensured compatibility across all modules, while usability
testing validated feature completeness and navigation efficiency.
Identified issues were addressed through iterative improvements
to enhance reliability and user experience.

3.5 System Evaluation
The system was evaluated based on the ISO/IEC 25010 software
quality standards, with particular focus on functional suitability,
performance efficiency, usability, and reliability. Functional suit-
ability assessed whether the system features met the specified re-
quirements, while performance efficiency measured responsiveness,
processing speed, and stability. Usability was evaluated in terms of
ease of use, learnability, and interface intuitiveness, and reliability
was examined the system’s stability under varying usage conditions.
Evaluation was conducted through a combination of technical test-
ing and user feedback from IT professionals and general users,
providing a comprehensive measure of both system quality and
user satisfaction.

4 RESULTS AND DISCUSSIONS
This section presents the organized documentation and analysis of
the system’s development outcomes. The primary objective was
to design and implement a cross-platform job marketplace that
connects blue-collar freelancers with employers seeking short-term
labor assistance. The discussion covers the system’s functionalities,
structural design, and evaluation results based on user testing and
software quality assessment.

The platform serves as a digital employment marketplace that
bridges the gap between blue-collar workers and employers seeking
temporary or task-based services. The platform facilitates quick
job matching for various work categories, including household
cleaning, personal assistance, delivery, handyman tasks, and yard
maintenance.

The development of the platform initially began with a front-end
prototype using WordPress, before transitioning to a PHP-based
architecture to achieve full integration between the front-end and
back-end components. The final system provides a seamless user
experience through the following core functionalities:

• Job posting and application management: Employers can
create and manage job listings, while freelancers can apply
for available tasks.

• Data visualization dashboard: Administrators can view ana-
lytics on job market trends, including service category dis-
tribution and seasonal demand.

• Prescriptive pricing analytics: A Linear Programming algo-
rithm generates optimized and fair price suggestions for job
postings.

• Messaging system: Facilitates communication between free-

lancers and employers for coordination and feedback.

• Review and rating system: Employers can evaluate free-
lancers’ performance to promote accountability and reliabil-
ity.

These features collectively contribute to a functional, user-
oriented system that addresses the challenges of informal hiring
and limited job accessibility in the blue-collar sector.

Figure 2 shows the administrator dashboard, which serves as
the control center for system monitoring. The dashboard displays
key metrics such as the total number of freelancers, employers,
and job postings. Additionally, it includes data visualization charts
depicting the distribution of service categories and seasonal job
trends. The administrator is also provided with tables for pricing
optimization and management of predefined pricing parameters,
supporting informed decision-making for job valuation.

4.1 Summary of Software Evaluation Results
Table 2 presents the evaluation results based on the ISO/IEC 25010
software quality standard, showing an overall mean rating of 4.98,
interpreted as Agree. This reflects a high level of user satisfaction
across the evaluated quality characteristics. The findings indicate
that the system meets the essential standards of functional suit-
ability, usability, reliability, security, portability, and performance
efficiency.

Overall, feedback from both respondent groups demonstrates a
consistently positive perception of the platform, confirming that
the system is functional, secure, user-friendly, and efficient in ac-
cordance with the ISO/IEC 25010 evaluation framework.

5 CONCLUSION AND RECOMMENDATION
5.1 Conclusion
The developed system effectively achieves its primary objective
of creating an innovative, user-centered job marketplace tailored
for blue-collar workers and employers in the Philippines. It facili-
tates efficient and inclusive connections, addressing the growing
demand for short-term labor in Metro Manila. A key innovation is
the integration of prescriptive analytics through a Linear Program-
ming algorithm, which generates dynamic, data-driven pricing
recommendations, promoting fairness, transparency, and equitable
compensation. The platform also features a dynamic administrative
dashboard that provides visual insights into user activity, job trends,
service categories, and financial summaries, supporting informed
decision-making and operational accountability. Evaluation un-
der the ISO/IEC 25010 framework demonstrated high functional
suitability, performance efficiency, usability, and reliability, with
both IT professionals and general users confirming the system’s
effectiveness, security, and ease of use. Overall, the system delivers
a functional, data-driven, and socially responsive digital employ-
ment solution, enhancing inclusive employment opportunities and

207ICSIM 2026, January 21–23, 2026, Yokohama, Japan

John Bernard Abadam et al.

Figure 2: Admin Dashboard Page

Table 2: Summary Results on ISO/IEC-25010

Respondents

Criteria

Results

Interpretation

Average Score

Interpretation

Regular Users
(e.g., Freelancer, Employer)

IT Professionals

Functionality

5.44%

Strongly Agree

4.83%

Agree

Usability
Performance
Usability
Reliability
Security
Portability
Functionality

5.21%
5.19%
5.15%
5.19%
5.02%
5.15%
5.09%

Agree
Strongly Agree
Agree
Strongly Agree
Agree
Agree
Agree

5.13%

Agree

Average Result

4.98%

Agree

contributing to the sustainable development of the gig economy in
the Philippines.

5.2 Recommendations
Future work should focus on enhancing the system through the
implementation of concrete, feature-driven improvements that in-
crease usability, transparency, and decision accuracy. Key priorities
include the development of an automated job classification and tag-
ging mechanism to standardize service categories, reduce manual
input, and improve job discoverability. Additionally, the introduc-
tion of structured review scoring and reputation metrics, based on
clearly defined performance criteria such as reliability, communica-
tion, and service quality, would enhance trust and accountability
within the platform. Lastly, the incorporation of rule-based deci-
sion support features, including pricing guidance and job-matching
recommendations derived from historical platform data and prede-
fined thresholds, would further support informed decision-making
for both freelancers and employers.

6 DECLARATION OF ARTIFICIAL

INTELLIGENCE RESEARCH ASSISTANCE
The authors used AI-assisted writing tools to improve the clarity
and readability of portions of the manuscript. These tools did not
contribute to the research design, data analysis, or conclusions. The
authors reviewed all content and take full responsibility for the
final manuscript.

References
[1] Philippine Statistics Authority. (2023). 2023 Annual labor and employment status.
Retrieved from https://psa.gov.ph/statistics/survey/labor-and-employment/lfs
[2] United Nations. (2023). World employment and social outlook: Trends 2023. Interna-
tional Labour Organization. Retrieved from https://www.ilo.org/global/research/
global-reports/weso/2023/lang--en/index.htm

[3] World Bank Open Data. (2023). World Bank Open Data. Retrieved October
9, 2025, from https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS?end$=
$2023&start$=$2020

[4] Jawadi, F., Mallick, S. K., Cheffou, A. I., & Augustine, A. (2019). Does higher
unemployment lead to greater criminality? Revisiting the debate over the
business cycle. Journal of Economic Behavior & Organization, 182, 448–471.
https://doi.org/10.1016/j.jebo.2019.03.025

[5] United Nations. (2025). Goal 8: Decent Work and Economic Growth. Retrieved

from https://www.un.org/sustainabledevelopment/economic-growth/

[6] United Nations Office on Drugs and Crime (UNODC). Crime Prevention. Re-
trieved from https://www.unodc.org/unodc/en/justice-and-prison-reform/cpcj-

208Development of A Cross-Platform Application Blue-Collar Marketplace with Prescriptive Analytics Using Linear
Programming Algorithm

ICSIM 2026, January 21–23, 2026, Yokohama, Japan

crimeprevention-home.html

[7] Sevillano, S. (2023). Online ad lures Filipino victims into job scams abroad. Philip-
pine News Agency. Retrieved from https://www.pna.gov.ph/articles/1202698
[8] Correa, E. (2023). Effect of unemployment, inflation and foreign direct investment
on economic growth in Sub-Saharan Africa. Journal of Developing Economies,
8(2), 297–315. https://doi.org/10.20473/jde.v8i2.47283

[9] PhilJobNet. (2023). Public Employment Service Office (PESO). Retrieved from https:

//peis.philjobnet.ph/peso.aspx

[10] Galdon-Sanchez, J. E., & Gil, R. (2021). Big Data adoption and employment in
small and medium enterprises. Working Paper, University of Pennsylvania. Re-
trieved from https://www.law.upenn.edu/live/files/11669-big-data-adoption-and-
employment-in-small-and

[11] Haider, A., Jabeen, S., Rankaduwa, W., & Shaheen, F. (2023). The nexus between
employment and economic growth: A cross-country analysis. Sustainability,

15(15), 11955. https://doi.org/10.3390/su151511955

[12] Handy for Pros (Now Angi Services). House Cleaning & Handyman Services.

Retrieved from https://www.handy.com/

[13] Department of Labor and Employment (DOLE). (2024). Government Internship
Program (GIP). Retrieved from https://www.dole.gov.ph/government-internship-
program/

[14] National Institute of Justice. Hidden consequences: The impact of incarceration on
dependent children. Retrieved from https://nij.gov/journals/278/Pages/impact-of-
incarceration-on-dependent-children.aspx

[15] Simionescu, L., & Cifuentes-Faura, J. (2022). Forecasting national and regional
youth unemployment in Spain using Google Trends. Social Indicators Research,
164(3), 1187–1216. https://doi.org/10.1007/s11205-022-02984-9

209