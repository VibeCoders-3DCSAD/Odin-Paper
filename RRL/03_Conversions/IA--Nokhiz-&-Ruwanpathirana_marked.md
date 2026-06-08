JOURNAL OF SOCIAL COMPUTING Volume 6, Number 3, September 2025
ISSN 2097-5015 03/07 pp184−208 DOI: 10.23919/JSC.2025.0015
Consumer Autonomy or Illusion? Rethinking
Consumer Agency in the Age of Algorithms
Pegah Nokhiz*† and Aravinda Kanchana Ruwanpathirana†
Abstract: Consumer agency in the digital age is increasingly constrained by systemic barriers and
algorithmic manipulation, raising concerns about the authenticity of consumption choices. Nowadays,
financial decision-making is shaped by external pressures like obligatory consumption, algorithmic
persuasion, and unstable work schedules that erode financial autonomy. Obligatory consumption (like
subscriptions and hidden fees) is intensified by digital ecosystems. Algorithmic tactics like Buy Now Pay
Later (BNPL) and personalized recommendations lead to impulsive purchases. Unstable work
schedules also undermine financial planning. Therefore, it is important to study how these factors
impact consumption agency. To do so, we examine formal models grounded in discounted
consumption with constraints that bound consumer agency. Specifically, we construct analytical
scenarios in which consumers face fixed obligatory payments, algorithm-influenced impulsive
consumption, or unpredictable income due to temporal instability. Using this framework, we
demonstrate that even rational, utility-maximizing agents can experience early financial ruin when
agency is limited across structural, behavioral, or temporal dimensions and how diminished autonomy
directly impacts long-term financial well-being. Our central argument is that consumer agency must be
treated as a value (not a given) requiring active cultivation, especially in digital ecosystems. The
connection between our formal modeling and the central argument allows us to indicate that
limitations on agency (whether structural, behavioral, or temporal) can be rigorously linked to
measurable risks like financial instability. This connection thus also provides a basis for normative
claims regarding consumption as a value, by anchoring them in a formally grounded analysis of
consumer behavior. As solutions, we stress that promoting true consumer agency demands systemic
interventions, regulations, and consumer education to support value deliberation and informed
autonomous choices. We formally demonstrate how these measures strengthen agency.
Key words: consumption; agency; obligatory consumption; algorithmic persuasion
1 Introduction mental health, social equity, and sustainable economic
practices[1–3]. However, consumer behavior is shaped
The ability to make informed choices about spending
and saving (autonomy in consumption) is crucial for not only by individual preferences but also by social
promoting individual empowerment, financial and norms and peer influences. In the digital economy,
Pegah Nokhiz is with the Digital Life Initiative, Cornell Tech, New York, NY 10044, USA. E-mail: pegah.nokhiz@gmail.com.
Aravinda Kanchana Ruwanpathirana is with the School of Computing, National University of Singapore, Singapore 117417, Singapore. E-
mail: kanchana.ruwanpathirana@gmail.com.
* To whom correspondence should be addressed.
† Pegah Nokhiz and Aravinda Kanchana Ruwanpathirana contribute equally to this paper.
Manuscript received: 2025-04-13; revised: 2025-06-26; accepted: 2025-07-11
© The author(s) 2025. The articles published in this open access journal are distributed under the terms of the
Creative Commons Attribution 4.0 International License (http://creativecommons.org/licenses/by/4.0/).

Pegah Nokhiz et al.: Consumer Autonomy or Illusion? Rethinking Consumer Agency in the Age… 185
algorithms and personalized marketing further systems encourage overspending by deferring
complicate these dynamics. Algorithms frequently payments[16, 17], time-limited promotions and
generate filter bubbles, restricting access to diverse personalized recommendations create a sense of
viewpoints. Through manipulative design strategies and urgency and artificial need[18–21], dynamic pricing and
persuasive advertising, they steer consumers toward freemium models restrict free features and encourage
impulsive buying decisions, thereby diminishing their in-app purchases[22, 23], social media algorithms amplify
sense of agency[4, 5]. Systemic barriers also play a the social pressure to conform[16, 24, 25], and techniques
critical role in limiting agency. For example, attributing like fear of missing out (FOMO)-driven scarcity alerts
the purchase of unhealthy groceries to personal further prompt impulsive buying[21, 26].
laziness (overemphasizing individual choice and placing Work schedule instability: Unpredictable work
individual blame) neglects broader structural issues schedules significantly harm workers’ financial security
related to consumers’ self-determination, such as and well-being, particularly affecting vulnerable groups
limited access to affordable nutritious food and the like part-time employees, those with lower incomes or
pervasive presence and promotion of unhealthy education, and food service and retail sectors with
options[6]. These dynamics raise critical concerns more erratic schedules[27, 28]. The instability of work
about the authenticity of consumer agency in the hours leads to burnout, conflicts between work and
digital age: Are individuals today genuinely making personal life, and financial disruptions[29–33]. This
independent decisions about their saving and spending, inconsistency in earnings complicates financial planning,
or is agency in consumption becoming increasingly undermining workers’ ability to make informed
illusory? Consider the following examples. decisions about saving and spending, thus reducing
Obligatory consumption: Obligatory their consumption autonomy.
consumption encompasses essential expenditures At the same time, the increasing use of digital tools
driven by social, cultural, legal, or economic pressures, and algorithms in workforce management, particularly
such as taxes, insurance premiums, tuition fees, loan for labor scheduling, can further undermine workers’
repayments, and child support. In the digital age, this consumption agency. While these technologies
phenomenon has intensified due to subscription-based improve efficiency, they can also lead to greater
models and dependencies on digital ecosystems. A few instability in workers’ schedules[34–37]. For example,
examples among many include recurring payments that reports from The New York Times highlight that these
are often overlooked but accumulate to substantial tools have made work hours more unpredictable, as
amounts, such as subscriptions for software like they can dynamically and in real-time adjust schedules
Microsoft Office, streaming services like Netflix[7], with little to no advance notice[34, 38].
gaming memberships[8], and Internet of Things (IoT) Our work. In response to the earlier question of
devices relying on subscription-based models[9, 10]. whether individuals today are truly making independent
Additionally, hidden fees from delivery apps, in-app choices or if agency in consumption is becoming more
purchases, and transaction charges further raise illusionary, we argue that in the age of algorithms,
consumer costs[11]. Remote work expenses[12] and many consumers are subject to value capture, where
educational e-resources, such as digital textbooks and externally imposed values (such as those embedded in
e-learning subscriptions, also place additional strain on manipulative marketing) are adopted without critical
budgets[13, 14]. reflection or personal adaptation[39]. Furthermore,
Algorithmic persuasion & impulsive systemic barriers, including socio-economic inequality,
consumption: Algorithms embedded in digital algorithmic biases, and the misuse of algorithms in
platforms employ psychological tactics to influence areas like automated work scheduling, undermine
consumer behavior, often leading to impulsive consumer agency by restricting individuals’ ability to
purchases and financial strain. Consumers have make decisions aligned with their unique values and
explicitly stated that they attribute excessive needs.
consumption to such marketing strategies[15]. For In this context, consumption agency must be
example, strategies such as Buy Now Pay Later (BNPL) recognized as a value to be actively cultivated, rather

186 Journal of Social Computing, September 2025, 6(3): 184−208
than assumed. Thus, to strengthen agency, it is critical Our contribution. In summary, the key
to showcase the impacts of these challenges on contributions of this paper are as follows:
consumption autonomy more than ever before. For • We formally demonstrate the consequences of a
consumers, understanding these dynamics helps them lack of agency in consumption, which are exacerbated
make more informed decisions about their immediate by algorithms. We illustrate these effects across three
and future financial needs. They can move toward true distinct use cases: obligatory consumption, algorithm-
consumption agency, which enables individuals to make driven impulse purchases, and dynamic work scheduling.
independent decisions about what, when, and how to • We discuss the significance of true agency in
consume, based on their own values and preferences, consumption and formally prove that empowering
without being influenced by external pressures, consumers to move toward true agency can help them
manipulative strategies, or systemic limitations. avoid financial distress.
For policymakers, these insights provide valuable • We highlight the significance of viewing
guidance for anticipating economic behaviors and consumption as a value rather than a given in the
developing interventions, such as regulatory modern economy. Additionally, we demonstrate the
frameworks and social welfare programs[40]. benefits of encouraging deliberation on consumption,
Acquiring these insights therefore requires which can be facilitated through educational initiatives
examining consumption behavior (i.e., how individuals and policy-driven regulatory measures.
make decisions about spending and saving) within the We first present the related work in Section 2. We
constraints of limited agency. To carry out this study, then introduce the core modeling framework in
in this paper, we utilize discounted utility models, a Section 3.1. Subsequently, we apply this framework to
widely recognized class of frameworks in economics explore issues related to limited agency in several
for analyzing intertemporal consumption behavior[41, 42]. scenarios, including obligatory consumption,
These consumption models help deepen our algorithmic persuasion and impulsive consumption, and
understanding of how individuals make decisions about work scheduling, in Sections 3.2, 3.3, and 3.4,
consumption and saving over time. Our objectives in respectively. Afterward, we propose potential
this study are twofold. solutions in Section 4 and include a discussion of
(1) We formally analyze the impact of algorithmic limitations and future work in Section 5. Finally, we
strategies on consumption behavior and the resulting present our conclusions in Section 6.
effects on consumer financial well-being and stability.
2 Literature Review
That is, we formally assess consumption with bounded
agency where the absence of true agency in Consumption model. Consumption models, part of
consumption decisions leads to financial distress. the broader discounted utility (DU) framework,
(2) We identify solutions that can help mitigate explore how individuals make intertemporal decisions
these impacts to foster greater consumption agency. about consumption and saving[41, 42]. These models
We specifically analyze several scenarios to assume individuals maximize discounted utility, often
determine whether individuals compelled to adopt prioritizing immediate rewards over future ones[43],
predetermined consumption values or influenced by and focus on choices regarding when to consume or
external pressures are at a higher risk of experiencing save[44]. Key models include the permanent income
early financial bankruptcy. Additionally, we examine hypothesis (PIH), the life-cycle model[41, 45, 46], and the
the adverse effects on financial utility for individuals who, neoclassical model[47]. The PIH predicts consumption
due to uncertainty about their work schedules, are based on expected average income over time, while
unable to exercise consumption agency or plan their the life-cycle model adds a finite time frame for asset
finances effectively. As part of the solutions, we accumulation and use. The neoclassical model builds
demonstrate how reassessing consumption values on these principles using neoclassical economic theory.
(through value deliberation and prioritization of Additionally, the income fluctuation problem (IFP),
genuine needs) can improve financial well-being and another model within this family of models, introduces
empower consumers. income uncertainty and limits consumption to current

Pegah Nokhiz et al.: Consumer Autonomy or Illusion? Rethinking Consumer Agency in the Age… 187
assets, prohibiting consumption beyond owned requirements[12]. Education systems increasingly
resources[42, 48–54]. mandate digital resources, such as e-textbooks and
AI, consumption, and agency. The concept of online learning platforms, creating additional financial
agency in consumption and in the presence of burdens for students[13, 14]. Healthcare and wellness
algorithmic decisions has been explored in various sectors have also adopted subscription-based models.
contexts, e.g., studies on consumer agency and its Telemedicine services and wearable health devices,
adaptability during environmentally imposed such as fitness trackers, often tie essential features to
constraints such as the pandemic[1], recommendation recurring payments, further embedding obligatory
systems that could either enhance or undermine user consumption into consumers’ lives[62, 63].
agency by tailoring experiences to user preferences Algorithmic persuasion. Extensive research has
but also restricting agency through over-reliance on been conducted on persuasive consumption and
opaque algorithms[55, 56], and studies on fairness in AI impulse purchases, particularly within consumer
emphasizing the importance of agency (as a general behavior, marketing strategies, and algorithmic design.
concept) as a dimension of equity, noting that Algorithmic personalized recommendations, which use
constrained or manipulated choices disproportionately tailored products and offers, are commonly employed
affect vulnerable populations[2, 39, 57]. Furthermore, to boost consumption[18, 19]. These recommendations
prior work suggests that interpretability and often make use of user data to enhance relevance and
transparency can support user agency by fostering urgency, increasing the chances of unplanned
trust and enabling informed decision-making[3, 58, 59]. purchases[18, 19]. Time-sensitive offers and scarcity
Obligatory consumption. Researchers have tactics are highly effective in triggering impulsive
explored various dimensions of this phenomenon, behavior[20, 21]. Approaches like flash sales, countdown
highlighting how subscription-based models dominate timers, and low-stock alerts create a sense of urgency
consumer spending. For instance, Amazon Prime and and fear of missing out (FOMO), prompting users to
Netflix exemplify this trend, requiring continuous make quick purchase decisions without much
payments for access and locking users into ongoing deliberation[20, 21]. Dark patterns, which are
costs[7]. Similarly, gaming platforms leverage battle manipulative design techniques, further contribute to
passes and memberships to restrict content access, impulse buying. These include deceptive interface
effectively monetizing user engagement over time[8]. designs, preselected add-ons, and hidden costs that
Additionally, digital ecosystems where consumers are push users toward unintended purchases[64, 65].
often tied to proprietary infrastructures (such as Additionally, gamification elements like reward points,
Apple’s App Store or Google Play) restrict users’ badges, and streaks are used to enhance engagement
ability to switch providers without incurring additional and increase spending, particularly in e-commerce and
expenses[60, 61]. IoT devices, including smart gaming platforms[66, 67].
thermostats and home security systems, further Social media platforms amplify these effects through
exacerbate these dependencies by requiring influencer endorsements, viral trends, and targeted
subscriptions to unlock full functionality[9, 10]. Hidden advertisements, leading to impulsive and unnecessary
costs associated with digital platforms, e.g., delivery consumption[16, 24]. The integration of “buy now”
apps that impose service fees and mandatory tips, features directly within social media apps makes the
digital payment systems like PayPal and Venmo with transition from browsing to purchasing seamless,
transaction charges are other examples of obligatory increasing impulsive buying behavior[68, 69]. The rise of
consumption[11]. mobile commerce (m-commerce) has also been
Work-related obligations further embed identified as a significant driver of impulsive buying[26, 70].
consumption into daily life. The rise of remote work The ease and convenience of smartphones facilitate
has necessitated investments in digital tools, high- spontaneous purchases, while push notifications and
speed internet, and office equipment, while gig personalized ads on mobile devices serve as constant
economy workers face additional costs for maintaining prompts for consumption[26, 71]. Lastly, subscription-
vehicles or upgrading smartphones to meet platform based models and microtransactions in digital services

188 Journal of Social Computing, September 2025, 6(3): 184−208
and games promote repeated impulse spending work scheduling and its wide-ranging consequences.
through low-cost, recurring payments that accumulate Unstable schedules contribute to income volatility[29–33],
over time[72, 73]. which in turn leads to financial and life hardships[32, 90–93].
Remark. Although both obligatory consumption These include burnout from precarious work
and algorithmic persuasion can involve recurring schedules[94, 95] and work-family conflicts[96, 97],
payments, they differ in nature. Obligatory particularly affecting parents dealing with unpredictable
consumption has many forms, which also include or just-in-time schedules. Furthermore, parental work
structural, essential, or externally imposed expenses instability has been linked to increased anxiety and
like child support, remote work equipment, child behavioral problems[27]. In the field of human-
telemedicine, online/digital education, and taxes, which computer interaction (HCI), researchers have taken a
inherently differ from subscriptions. These are driven participatory approach to studying similar issues. This
by legal, social, or infrastructural pressures. Detailed includes emphasizing the importance of worker
examples were listed earlier for each category. participation in scheduling decisions to ensure
Algorithmic persuasion refers to tactics that exploit fairness[98] and exploring elicitation methods to model
consumers to prompt voluntary, often impulsive, worker preferences for more effective schedule
spending. While some recurring payments (like in-app management[99]. Additionally, scheduling software and
purchases) may appear in both contexts, they are not planning algorithms have been identified as
the same. An opt-in subscription under algorithmic contributors to more unpredictable schedules,
persuasion highlights how this expenditure may be particularly for low-wage workers in the service
strategically engineered for choice-influencing rather sector[34–37]. For instance, a report in The New York
than fulfilling essential needs. In contrast, an obligatory Times highlighted cases where algorithmically
subscription is one that is required for basic access to scheduled employees received their timetables less
platform lock-ins and needed functionalities (like the than three days before the start of the workweek[34].
ones mentioned earlier that are tied to proprietary Sudden schedule changes and sales-driven pay
infrastructures of App stores or IoT devices/security reductions have also been correlated with these
systems’ mandatory subscription fees in digital practices[38].
ecosystems). So, although the subscription categories
3 Fallacy of Agency: Case Study
may appear similar in name, the nature of the
expenses differs significantly. Rather than being an In this section, we explore various scenarios of
impulsive choice, these examples are strict expenses consumption behavior that reveal the illusion of agency.
and limit financial flexibility due to economic, legal, or We will formally demonstrate that even rational
infrastructural constraints. agents can experience adverse outcomes, despite
Ruin analysis and minimum subsistence. appearing to have clear autonomy. Our analysis
Financial bankruptcy, or ruin, has been extensively focuses on three key cases.
studied in various theoretical and applied frameworks. (1) Mandatory consumption of a fixed amount at
Research has focused on evaluating an insurer’s each time step.
insolvency risks[74, 75], reducing bankruptcy risks[76, 77], (2) Algorithmic persuasion and impulsive
and investment modeling[78]. These works collectively consumption, involving spending money on basic living
contribute to understanding and addressing the needs such as food and shelter (minimum subsistence)
challenges associated with financial ruin[79, 80]. Separately, alongside externally-influenced impulsive consumption
the concept of lower bounds on consumption values.
(minimum subsistence levels) has also been extensively (3) The adverse effects of unpredictable work
studied in relation to utility-maximizing consumption schedules on worker consumption agency.
strategies[81–89] which indicates that one needs to pay Why these three scenarios? Each condition
for basic needs such as food and shelter. contributes to a subtle but critical form of epistemic
Work schedule instability. Current research harm in which individuals’ ability to act as credible,
focuses heavily on sociology, particularly on irregular autonomous agents is diminished. We selected these

  Pegah Nokhiz et al.:   Consumer Autonomy or Illusion? Rethinking Consumer Agency in the Age… 189
|                   |     |         |             |     |               |     |     |     |      | (   |             | )   |     |     |
| ----------------- | --- | ------- | ----------- | --- | ------------- | --- | --- | --- | ---- | --- | ----------- | --- | --- | --- |
|                   |     |         |             |     |               |     |     |     |      |     | (cid:229)+¥ |     |     |     |
| three  conditions |     |  (i.e., |  obligatory |     |  consumption, |     |     |     |      |     | btu(c)      |     |     |     |
|                   |     |         |             |     |               |     |     |     | maxE |     |             |     |     | (1) |
algorithmic persuasion, and work schedule instability) Rt;yt t
t=0
because they reflect distinct, yet deeply interconnected,
s.t.,
ways in which consumer agency is constrained in the
|                                                  |     |     |     |     |     |     |     |     |     |      | (cid:0)c)+y |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----------- | --- | --- | --- |
|                                                  |     |     |     |     |     |     |     |     | a   | =R(a |             |     |     | (2) |
| digital economy.                                 |     |     |     |     |     |     |     |     | t+1 | t    | t t         | t   |     |     |
| • Obligatory consumption captures structural and |     |     |     |     |     |     |     |     |     |      | ⩽a          |     |     |     |
|                                                  |     |     |     |     |     |     |     |     |     | 0<c  |             |     |     | (3) |
t t
economic constraints that reduce consumers’ freedom
|     |     |     |     |     |     |     | where  | b2(0;1)  | represents |     |  the |  discount |     |  factor, |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ---------- | --- | ---- | --------- | --- | -------- |
to opt out of ongoing financial commitments.
|     |     |     |     |     |     |     | reflecting |  consumers’  |     | preference |     |  for |  immediate |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------ | --- | ---------- | --- | ---- | ---------- | --- |
•  Algorithmic   persuasion    highlights   how   digital
|            |      |         |          |            |     |           | rewards |  over |  long-term |     |  rewards |  of |  equivalent |     |
| ---------- | ---- | ------- | -------- | ---------- | --- | --------- | ------- | ----- | ---------- | --- | -------- | --- | ----------- | --- |
| interfaces |  and |  design |  tactics |  influence |     |  behavior |         |       |            |     |          |     |             |     |
magnitude. The utility function can be any standard
through manipulation.
|     |     |     |     |     |     |     | utility  function |     |  in  economics, |     |  such |  as |  the  constant |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --------------- | --- | ----- | --- | -------------- | --- |
• Work scheduling instability reflects the temporal
relative risk aversion (CRRA) utility[102, 103], which is
uncertainty that undermines individuals’ ability to plan
used to capture individuals’ tendency to prefer lower-
and make informed decisions.
|     |     |     |     |     |     |     | risk,  smaller |     |  gains  over |  higher-risk |     |  outcomes |     |  with |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------ | ------------ | --- | --------- | --- | ----- |
Together, these cases span structural, technological,
|               |     |             |     |          |     |              | potentially |  larger |  payoffs[104]. |     |  The |  last |  constraint |     |
| ------------- | --- | ----------- | --- | -------- | --- | ------------ | ----------- | ------- | -------------- | --- | ---- | ----- | ----------- | --- |
| and  temporal |     |  dimensions |  of |  agency, |     |  offering  a |             |         |                |     |      |       |             |     |
ensures that the consumer can only consume from
multidimensional view of how autonomy is eroded.
|     |     |     |     |     |     |     | available |  assets. |  This |  prohibits |     |  behaviors |  such |  as |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ----- | ---------- | --- | ---------- | ----- | --- |
This framework also aligns with recent calls in both
|           |      |         |         |         |             |      | maintaining |  positive |     |  assets |  at  every |  time |  step |  by |
| --------- | ---- | ------- | ------- | ------- | ----------- | ---- | ----------- | --------- | --- | ------- | ---------- | ----- | ----- | --- |
| economics |  and |  ethics |  in  AI |  toward |  relational |  and |             |           |     |         |            |       |       |     |
borrowing indefinitely.
systemic determinants.
Using the discounted utility model, we can analyze
Before delving into these cases, we will first establish
consumer behavior to understand how individuals act
the underlying model and system properties.
in various circumstances and evaluate their financial
3.1    Basic model and system property
stability across different scenarios. To achieve this, we
We  begin  by  outlining  the  foundational  model require  a  concept  that  encapsulates  a  consumer’s
dynamics underlying our arguments. Suppose that a financial instability. In this study, we use the concept of
“ruin” to capture this notion. Ruin refers to a situation
| consumer starts with an initial asset value of a |     |     |     |     |     | . The |     |     |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
0
where a consumer exhausts their assets within a short
consumer aims to consume these available assets while
period. Formally:
simultaneously working to grow them through saving,
Ruin. We define ruin as the state where 9T<+¥
investing, and other means. Let a be the assets’ value
t
at the time-point t and c be the consumption. Let R such that a ⩽0 for t=T. This would mean that the
t+1
|     |     |     | t   |     |     | t   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
be the return on assets and y the income where R consumer would no longer be able to sustain their
|     |     |     |     | t   |     | t   | consumption, leading to financial ruin. |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
and/or y are coming from a known distribution.
t
In Sections 3.2 and 3.3, we examine two scenarios:
| With |  these  parameters |     |  established, |     |  we |  can  now |            |              |     |      |            |     |              |     |
| ---- | ------------------ | --- | ------------- | --- | --- | --------- | ---------- | ------------ | --- | ---- | ---------- | --- | ------------ | --- |
|      |                    |     |               |     |     |           | obligatory |  consumption |     |  and |  impulsive |     |  consumption |     |
outline our model of consumption under uncertainty,
where various behavioral constraints impact consumers’
which serves as the basis for our arguments. Although
financial stability. We demonstrate how the probability
numerous models aim to capture consumption under
of financial ruin shifts under different conditions and
| uncertainty, |  they |  all  fundamentally |     |     |  depend |  on  the |     |     |     |     |     |     |     |     |
| ------------ | ----- | ------------------- | --- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
how these behaviors can lead to early ruin. In Section
discounted utility framework, which is widely used in
|           |     |          |      |                |     |         | 3.4,  we |  extend |  the |  analysis |  to |  temporal |  factors, |     |
| --------- | --- | -------- | ---- | -------------- | --- | ------- | -------- | ------- | ---- | --------- | --- | --------- | --------- | --- |
| economics |  to |  analyze |  the |  relationship  |     | between |          |         |      |           |     |           |           |     |
illustrating how greater certainty in temporal events
consumption and savings (i.e., intertemporal consumption
can enhance achieved utility.
models with discounted utility)[41, 48, 49, 100, 101]. In a
discounted  utility  model,  an  agent  consumes  an 3.2    Obligatory consumption
amount c at each time step t, deriving utility u(c) from In  this  section,  we  examine  the  first  use  case:
|     | t   |     |     |     |     | t   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a concave function u. The goal is to determine a policy obligatory consumption.
that maximizes the total discounted utility over time. How  does  this  condition  affect  consumer
Formally, we can define the basic model as agency? Obligatory consumption constrains agency by

    190 Journal of Social Computing, September 2025, 6(3): 184−208
|                                                       |          |            |                  |               |     |     | (cid:229)T(cid:0)1y |        |     |
| ----------------------------------------------------- | -------- | ---------- | ---------------- | ------------- | --- | --- | ------------------- | ------ | --- |
| turning                                               |  certain |  financial |  decisions  into |  non-choices. |     |     |                     | a      |     |
|                                                       |          |            |                  |               |     |     | c =                 | t + 0: |     |
| When individuals are locked into certain payments for |          |            |                  |               |     |     | T                   | T T    |     |
t=0
mandatory  needs,  utilities,  or  platform-related  fees . Note that E(c)!Y.
Let c=c
¥
(often without a clear understanding of long-term costs) Consider the scenario where T!+¥. We can see
| they lose the ability to re-prioritize their expenditures |     |     |     |     | that, |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
|                                                           |     |     |     |     |       | (   | )   |     |     |
in response to changing needs or circumstances. These
|                                                          |     |     |     |     |     | (cid:229)+¥ |     | (cid:229)+¥ |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | ----------- | --- | ----------- | --- |
|                                                          |     |     |     |     |     | E btu(c     | ) = | btE(u(c))⩽  |     |
| expenses become effectively fixed, and the inflexibility |     |     |     |     |     |             | t   |             |     |
|                                                          |     |     |     |     |     | t=0         |     | t=0         |     |
limits the individual’s capacity to act in accordance (cid:229)+¥
btu(E(c));
| with  their |  own |  values  or |  preferences. |  Even  when |     |     |     |     |     |
| ----------- | ---- | ----------- | ------------- | ----------- | --- | --- | --- | --- | --- |
t=0
expenses were initially chosen, their persistent and
where the inequality comes from Jensen’s Inequality.
| sometimes opaque nature (e.g., hidden mandatory fees) |     |     |     |     |     |     |     | (           | )   |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- |
|                                                       |     |     |     |     |     |     |     | (cid:229)+¥ | 1   |
|                                                       |     |     |     |     |     |     |     | btu(c       | ⩽   |
undermines ongoing deliberation and adaptive decision- Therefore,  we  get  that  E ) u(Y).
|     |     |     |     |     |     |     |     |     | t 1(cid:0) b |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ |
t=0
making,  weakening  the  authenticity  of  consumer Note that c =c for all t due to an obligatory amount c.
t
autonomy (which is an epistemic harm). N ow  con sider  the  scenario  where  a >
|                                                    |     |     |     |     | (         | )                                         |     |     | 0   |
| -------------------------------------------------- | --- | --- | --- | --- | --------- | ----------------------------------------- | --- | --- | --- |
| To model this scenario, the consumer is restricted |     |     |     |     | 1         |                                           |     |     |     |
|                                                    |     |     |     |     | u(cid:0)1 | u(Y) . However, in this case, consuming a |     |     |     |
1(cid:0)b 0
to consuming a predetermined fixed amount at each
at the first time step would leave the consumer with
time step. While the consumer has the flexibility to
|     |     |     |     |     | more  utility |  than |  not  going |  to  ruin. |  A  rational |
| --- | --- | --- | --- | --- | ------------- | ----- | ----------- | ---------- | ------------ |
select this fixed amount initially, it cannot be adjusted
|     |     |     |     |     | consumer |  with  the |  goal |  of  maximizing |  utility  can, |
| --- | --- | --- | --- | --- | -------- | ---------- | ----- | --------------- | -------------- |
later, effectively committing to a rigid consumption plan.
therefore, consume all assets in a short finite time and
We will formally investigate the effect this would have
go to ruin but still end up with better overall utility
on the financial stability of the consumer.
compared to a scenario where they would save assets
| To make things simple, let us assume that R |     |     |     | =1 for |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
t ■
and consume within an infinite horizon.
| all t and y is coming from a distribution D |     |     |     | . We can |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
|                                             | t   |     |     | Y        |     |     |     |     |     |
This shows that no matter how rational and optimal
show the following.
the consumer’s behavior is, the lack of agency and the
Theorem 1. Consider an income y coming from a
t
obligatory nature of the consumption could lead to
| distribution D |  with a known mean Y. Assume that the |     |     |     |                                                    |     |     |     |     |
| -------------- | ------------------------------------- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- |
|                | Y                                     |     |     |     | adverse outcomes. Note that we have only relied on |     |     |     |     |
consumer is only allowed to consume a fixed constant
|     |     |     |     |     | the  fact |  that  the |  utility |  is  concave. |  This  is  a |
| --- | --- | --- | --- | --- | --------- | ---------- | -------- | ------------- | ------------ |
obligatory amount c⩾0 at every step. A rational utility-
characteristic common to the class of consumption
| maximizing |  consumer |  would |  go  to |  ruin  when  the |     |     |     |     |     |
| ---------- | --------- | ------ | ------- | ---------------- | --- | --- | --- | --- | --- |
functions referred to as risk-averse. This indicates that
utility function is concave.
even risk-averse behavior is insufficient to prevent a
| Concept |  sketch.  | Before |  presenting |  the  formal |          |               |       |              |             |
| ------- | --------- | ------ | ----------- | ------------ | -------- | ------------- | ----- | ------------ | ----------- |
|         |           |        |             |              | consumer |  from  facing |  ruin |  when  their |  agency  is |
proof of Theorem 1, we provide a brief overview of
constrained.
the main argument. In the limit, fixed consumption
|     |     |     |     |     | Remark |  on  the |  concave |  utility.  | The  use  of |
| --- | --- | --- | --- | --- | ------ | -------- | -------- | ---------- | ------------ |
converges to the income level. Given the concavity of
concave utility functions in settings with fixed or non-
the utility function, Jensen’s inequality implies that the
discretionary consumption is a preexisting choice. For
resulting utility over an infinite horizon is bounded.
|                   |        |                   |               |                     | example,   |  Ref.  [105] |  studies  |  a     |  habit-formation |
| ----------------- | ------ | ----------------- | ------------- | ------------------- | ---------- | ------------ | --------- | ------ | ---------------- |
| This  observation |        |  allows           |  us  to  show |  that,  for         |            |              |           |        |                  |
|                   |        |                   |               |                     | constraint |  using  CRRA |  utility, |  where |  consumption     |
| sufficiently      |  large |  initial  assets, |  there        |  exists  a  finite- |            |              |           |        |                  |
cannot fall below a fraction of past levels. The work of
horizon consumption path that yields a strictly higher
|                      |     |          |                  |                | Ref.  [106] |  considers |  a    |  fixed  upper |  bound  on  |
| -------------------- | --- | -------- | ---------------- | -------------- | ----------- | ---------- | ----- | ------------- | ----------- |
| utility,  ultimately |     |  leading |  to  termination |  in  a  finite |             |            |       |               |             |
|                      |     |          |                  |                | consumption |  under     |  CRRA |  preferences, |  while  the |
number of steps.
work of Ref. [107] analyzes both fixed upper and fixed
Proof.  Consider  the  discounted  utility  model lower consumption bounds using the same class of
introduced in Eqs. (1) and (2), under the setting where utility  functions.  These  examples  illustrate  that
R =1 for all t. Assume that the consumer goes to ruin concave utility functions have been used in models
t
at time T. Let c  be the constant consumption for ruin where consumption is partially or fully constrained,
T
at time T. Note that, similar in spirit to our notion of obligatory consumption.

  Pegah Nokhiz et al.:   Consumer Autonomy or Illusion? Rethinking Consumer Agency in the Age… 191
However, in practice, a consumer cannot consume Assume that the return rate R is fixed at 1, and for all
t
arbitrarily small amounts near 0. To meet their basic t, jb (cid:0)Bj⩽d and jy (cid:0)Yj⩽e. Also, assume (Y(cid:0)B)<0.
|     |     |     |     |     |     |     | t   |     | t   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
needs  and  sustain  themselves  (i.e.,  the  minimum There exists a T<+¥ such that with high probability
| subsistence), the consumers must consume at least a |     |     |     |     |     |     | a ⩽0. |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
T
specific minimum amount at each time step, which Concept  sketch.  Before  presenting  the  formal
serves as a lower bound on consumption. Our results proof of Theorem 2, we begin with a brief outline of
trivially  extend  to  the  case  where  minimum the  main  idea.  Since  both  income  and  minimum
subsistence  is  considered.  We  will  state  this  as  a subsistence levels are bounded, we can derive bounds
corollary for completeness.
on the change in assets at any time step t. Because the
Corollary 1. Consider an income coming from a
final asset level is the cumulative sum of these changes
distribution D  with a known mean Y. Assume that the over time, we can apply this boundedness along with
Y
consumer is only allowed to consume a fixed constant standard  concentration  inequalities.  Under  the
amount ⩾b at every step (where b is the minimum
assumption that the means of income and minimum
subsistence).  A  rational  utility-maximizing  consumer subsistence behave as expected, it follows that, with
would go to ruin when the utility function is concave.
high probability, the agent will reach ruin within a finite
3.3    Algorithmic  persuasion  and  impulsive number of steps T. The formal proof is given below.
consumption
Proof. Consider the model introduced in Eqs. (1)
In this section, we examine the case of algorithmic and (2). Let a  be the initial assets and a  be the assets
|     |     |     |     |     |     |     |     | 0   |     | T   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
persuasion and impulsive consumption. at time point T. Then we can see that,
How  does  this  condition  affect  consumer   (cid:229)T(cid:0)1 (cid:0)(cid:229)T(cid:0)1
|     |     |     |     |     |     |     |     |     | =a + | ⩽   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
|     |     |     |     |     |     |     |     | a   | y    | c   |     |
agency?  Through  personalized  advertising,  urgency T 0 t t
|     |     |     |     |     |     |     |     |     | t=0 | t=0 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
cues, and psychologically manipulative interface design,
(cid:229)T(cid:0)1 (cid:0)(cid:229)T(cid:0)1
|                    |     |         |     |              |     |        |     |     | a + y | b;  |     |
| ------------------ | --- | ------- | --- | ------------ | --- | ------ | --- | --- | ----- | --- | --- |
| digital  platforms |     |  create |  an |  environment |     |  where |     |     | 0 t   | t   |     |
|                    |     |         |     |              |     |        |     |     | t=0   | t=0 |     |
impulsive spending feels like self-directed behavior but
where the last inequality comes from the fact that
i s  h e a v il y   e x t e r n a l ly  s h ap e d .   C o n s u m e r s   w o u l d   b e (cid:229)T(cid:0)1
|     |     |     |     |     |     |     | c ⩾b  for all t. For ease of notation, let l |     |     | =a + | y (cid:0) |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | ---- | --------- |
r es p o n d i ng   t o   e n g i n ee r ed  t r ig g e r s  d e s ig n e d   to   b y p a s s t t T 0 t
|                                                      |     |       |            |       |           |     | (cid:229)T(cid:0)1 |     |            |     | t=0 |
| ---------------------------------------------------- | --- | ----- | ---------- | ----- | --------- | --- | ------------------ | --- | ---------- | --- | --- |
| critical  deliberation.                              |     |  This |  epistemic |  harm |  produces |     |                    |     |            |     |     |
|                                                      |     |       |            |       |           |     | b. Note that l     |     | ⩾a . Also, |     |     |
| what[39] calls value capture, where external systems |     |       |            |       |           |     | t                  | T   | T          |     |     |
t=0
| impose  consumption                                    |     |  values |  that |  individuals |     |  adopt |     |     |                       |     |     |
| ------------------------------------------------------ | --- | ------- | ----- | ------------ | --- | ------ | --- | --- | --------------------- | --- | --- |
|                                                        |     |         |       |              |     |        |     |     | E(l)⩽a +(Y(cid:0)B)T: |     |     |
| without recognizing the deviation from their own long- |     |         |       |              |     |        |     |     | T 0                   |     |     |
term  goals  or  ideals.  Thus,  consumer  agency  is We can also see that under our assumptions,
substantially hollowed out.

|                                                     |     |     |     |     |     |     | Y(cid:0)B(cid:0)d(cid:0)e⩽y |     | (cid:0)b ⩽Y(cid:0)B+d+e: |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | ------------------------ | --- | --- |
| In this setting, the consumer is allowed to consume |     |     |     |     |     |     |                             |     | t t                      |     |     |
any (feasible) amount. The consumer consumes c at
Using the Hoeffding’s inequality on l and assuming
t
| each  time |  point  | t  which |  consists |  of |  the  minimum |     |     |     |     | T   |     |
| ---------- | ------- | -------- | --------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
that T is large enough, i.e., T is such that (B(cid:0)Y)T⩾a
,
| subsistence b and the impulsive consumption c |     |     |     |     |     | (cid:0)b. |             |     |     |     | 0   |
| --------------------------------------------- | --- | --- | --- | --- | --- | --------- | ----------- | --- | --- | --- | --- |
|                                               | t   |     |     |     |     | t t       | we see that |     |     |     |     |
The consumer’s goal is to maximize their utility. We
|                                                       |     |     |     |     |     |     |   Pr(a | ⩾0)⩽ |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------ | ---- | --- | --- | --- |
| can see that under certain constraints, even when the |     |     |     |     |     |     |        | T    |     |     |     |
| consumer is assumed to have freedom of choice, the    |     |     |     |     |     |     | Pr(l   | ⩾0)= |     |     |     |
T
optimal  behavior  for  the  consumer  is  to  consume Pr(l(cid:0)(a +(Y(cid:0)B)T)⩾(cid:0)a +(B(cid:0)Y)T)⩽
|     |     |     |     |     |     |     |     | T 0 |     | 0   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
available  assets  in  a  short  finite  time  to  gain  the 2((cid:0)a +(B(cid:0)Y)T)2
0
(cid:0)
maximum utility possible. (Y(cid:0)b+d+e(cid:0)(Y(cid:0)b(cid:0)d(cid:0)e))2(cid:1)T
|          |      |          |       |           |               |      | e          |                 |     | =   |     |
| -------- | ---- | -------- | ----- | --------- | ------------- | ---- | ---------- | --------------- | --- | --- | --- |
| Theorem  |  2.  | Consider |  the  |  scenario |  where        |  the |            |                 |     |     |     |
|          |      |          |       |           |               |      | 2((cid:0)a | +(B(cid:0)Y)T)2 |     |     |     |
| consumer |  has |  control |  over |  their    |  consumption, |      |            | 0               |     |     |     |
(cid:0) (2d+2e)2(cid:1)T
| subjected to the consumption c |     |     |     | ⩾b at each time point |     |     | e   |     | :   |     |     |
| ------------------------------ | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- |
t t
t (where b comes from a distribution with mean B and Furthermore, for any T such that T>2a=(B(cid:0)Y), we
|                                                    | t   |     |     |     |     |     |     |     |     | 0   |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| the income comes from a distribution with mean Y). |     |     |     |     |     |     | get |     |     |     |     |

    192 Journal of Social Computing, September 2025, 6(3): 184−208
|     |     |     | 2((B(cid:0)Y)T=2)2 |     |     |     |          |             |       |       |            |          |     |
| --- | --- | --- | ------------------ | --- | --- | --- | -------- | ----------- | ----- | ----- | ---------- | -------- | --- |
|     |     |     |                    |     |     |     | temporal |  parameter. |  This |  idea |  has  been |  studied |  in |
(cid:0)
(2d+2e)2(cid:1)T recent work[109–111], which introduce the concept of
|     | Pr(a | ⩾0)⩽e |     |     | =   |     |     |     |     |     |     |     |     |
| --- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
T
“lookahead”, representing the degree of certainty one
((B(cid:0)Y))2T
(cid:0) 8(d+e)2 has about future outcomes. This is especially relevant
|     |     |     | e   | :   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
as we would like to formally evaluate the hypothesis
((B(cid:0)Y))2
Let  c= .  We  get  that  with  probability that  having  more  awareness  of  upcoming  work
8(d+e)2
⩾1(cid:0)e(cid:0)cT, the assets at time T, a ⩽0 and the schedules  enables  workers  to  better  manage  their
, satisfy a
|     |     |     |     | T   | T   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
consumer would go to ruin at time point T. ■ finances and exercise greater autonomy. That is:
|             |     |       |      |               |     |          | How      |  does  this |  condition |       |  affect    |  consumer |         |
| ----------- | --- | ----- | ---- | ------------- | --- | -------- | -------- | ----------- | ---------- | ----- | ---------- | --------- | ------- |
| We  observe |     |  that |  the |  introduction |  of |  impulse |          |             |            |       |            |           |         |
|             |     |       |      |               |     |          | agency?  | Unstable    |            |  work |  schedules |           |  impair |
consumption and minimum subsistence constraints in
consumption agency by undermining the individual’s
both of our settings can eventually lead to ruin under
|     |     |     |     |     |     |     | ability |  to  plan, |  anticipate, |     |  and  allocate |  financial |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | ------------ | --- | -------------- | ---------- | --- |
specific conditions, as outlined in the previous claims.
resources effectively. Agency is not only about making
Theorem 2 shows that in this case, agents are likely to
|            |       |         |     |                 |     |         | choices,      |  but  about |     |  having       |  the  temporal |     |  and  |
| ---------- | ----- | ------- | --- | --------------- | --- | ------- | ------------- | ----------- | --- | ------------- | -------------- | --- | ----- |
| experience |  ruin |  within |  a  |  finite  number |  of |  steps. |               |             |     |               |                |     |       |
|            |       |         |     |                 |     |         | informational |  stability  |     |  to  evaluate |  options.      |     |  When |
Moreover, the probability of avoiding ruin decreases
income is volatile and work hours unpredictable (as
exponentially with time t.
|        |            |     |       |            |               |     | often  happens |  under     |  algorithmic |     |  labor     |  scheduling),   |     |
| ------ | ---------- | --- | ----- | ---------- | ------------- | --- | -------------- | ---------- | ------------ | --- | ---------- | --------------- | --- |
| It  is |  important |  to |  note |  that  the |  implications |  of |                |            |              |     |            |                 |     |
|        |            |     |       |            |               |     | individuals    |  lack  the |  foresight   |     |  necessary |  for  financial |     |
Theorem 2 are significant.
|     |     |     |     |     |     |     | planning. |  This  temporal |     |  uncertainty |  prevents |     |  them |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------------- | --- | ------------ | --------- | --- | ----- |
• This is because when income distributions have
from aligning spending and saving with their values,
low average income and high variance, even if income
|     |     |     |     |     |     |     | instead |  forcing  short-term, |     |  reactive |  decisions. |     |  The |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------------------- | --- | --------- | ----------- | --- | ---- |
is high at certain points in time, the likelihood of early
formal analysis in this section shows that even rational
ruin is high as well. In other words, despite having high
consumers with unstable schedules face systematically
income at certain moments, the high uncertainty in
|     |     |     |     |     |     |     | lower  utility, |  illustrating |     |  that |  agency  is |  structurally |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ------------- | --- | ----- | ----------- | ------------- | --- |
income means that if regular consumption exceeds the
constrained by temporal unpredictability.
average income, there is a strong likelihood of quickly
|     |     |     |     |     |     |     | A lookahead of  |     | k steps (weeks) implies that the |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | -------------------------------- | --- | --- | --- | --- |
depleting resources.
agent is aware of the exact income and financial shocks
| •  Even |  if  the |  average |  income |  is  lower |  than |  the |                               |     |     |     |                       |     |     |
| ------- | -------- | -------- | ------- | ---------- | ----- | ---- | ----------------------------- | --- | --- | --- | --------------------- | --- | --- |
|         |          |          |         |            |       |      | they will face over the next  |     |     |     | k steps in their work |     |     |
consumer’s  expenditures,  they  may  still  recklessly schedule. References [109, 110] formally demonstrate
deplete their savings to cover excessive consumption. the consequences of this concept, as explained below.
As discussed earlier, algorithms can push individuals to
Theorem 3[109, 110]. Consider two individuals, one
| consume, |  even |  when |  financially |  incapable, |     |  through |     |     |     |     |     |     |     |
| -------- | ----- | ----- | ------------ | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
with a lookahead of k steps and one with no lookahead.
| targeted |  ads, |  creating |  urgency |  or  scarcity |  (such |  as |     |     |     |     |     |     |     |
| -------- | ----- | --------- | -------- | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
There are instances with bounded income, where the
FOMO-driven strategies), freemiums, and time-limited individual with lookahead achieves significantly higher
offers.  These  tactics  exploit  psychological  and utility compared to the individual without lookahead.
emotional  triggers  to  influence  decision-making,  a Furthermore,  the  gap  between  the  utility  of  the
phenomenon  known  as  optimism  bias,  where individual with lookahead and the individual without
individuals tend to underestimate their expenses, often lookahead linearly increases with k. Formally, if u is
c
leading them to make poor financial decisions despite the utility of the individual with lookahead k and u  is
z
having the means to plan more effectively[108]. the utility of the individual without lookahead, then

| 3.4    Work scheduling |     |     |     |     |     |     |     |     | (cid:0)u | ⩾Ω(k): |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | --- | --- | --- |
|                        |     |     |     |     |     |     |     |     | u c      | z      |     |     |     |
In  the  previous  sections,  we  observed  that  an The  formal  version  of  the  Theorem  3,  and  the
individual’s  ability  to  maintain  long-term  financial complete (restated) proof from Refs. [109, 110], are
stability varies based on the level of agency they possess. available in the Appendix B, for completeness and ease
However, in our results so far, adjustments to the of reference. The proof itself uses a carefully defined
agency were made by modifying monetary parameters. class of income distributions and applies Yao’s min-
In this section, we explore the concept of agency as a max  theorem[111]  to  focus  the  argument  on

  Pegah Nokhiz et al.:   Consumer Autonomy or Illusion? Rethinking Consumer Agency in the Age… 193
deterministic algorithms, to demonstrate the desired while  the  intuitive  understanding  is  that  a  lack  of
control is detrimental, the precise formal long-term
utility gap.
Theorem 3 implies that even if the worker without consequences are often uncertain and rarely discussed.
lookahead  is  behaving  optimally,  the  worker  with Our results formally demonstrate the significance of
lookahead consuming optimally is always guaranteed these aftereffects: Many consumers fall prey to value
to have an advantage. That is, the gap between the capture,  where  externally  imposed  values  (such  as
utilities of the worker who knows their schedule in those  embedded  in  manipulative  marketing)  are
|     |     |     |     |     | accepted |  without |  critical |  reflection |     |  or  personal |     |
| --- | --- | --- | --- | --- | -------- | -------- | --------- | ----------- | --- | ------------- | --- |
advance with that of the worker without a lookahead,
|     |     |     |     |     | adaptation[39]. |  Additionally, |     |  they |  encounter |  systemic |     |
| --- | --- | --- | --- | --- | --------------- | -------------- | --- | ----- | ---------- | --------- | --- |
increases with k. Therefore, the more lookahead the
barriers such as mandatory consumption and suboptimal
individual has, the more utility they can acquire. This
|     |     |     |     |     | practices |  like |  faultily |  executed |  automated |     |  work |
| --- | --- | --- | --- | --- | --------- | ----- | --------- | --------- | ---------- | --- | ----- |
also suggests that a worker who is aware of their
work  schedule  will  consistently  experience  greater scheduling, which further reduce consumer agency.
utility from consumption, as they can manage their Thus, we argue that consumer agency is a value to
finances more effectively and exercise greater autonomy. be  nurtured  rather  than  an  inherent  given.  These
|     |     |     |     |     | theoretical |  insights |  (particularly |     |  those |  addressing |     |
| --- | --- | --- | --- | --- | ----------- | --------- | -------------- | --- | ------ | ----------- | --- |
To visually summarize the discussions in Sections 3.2,
situations intensified by algorithmic influences) serve as
| 3.3,  and |  3.4,  | Fig.  1  shows |  a  conceptual |  diagram/ |     |     |     |     |     |     |     |
| --------- | ------ | -------------- | -------------- | --------- | --- | --- | --- | --- | --- | --- | --- |
a tangible reminder that fostering consumption as a
| flowchart |  of  all |  scenarios, |  their  characteristics, |  and |     |     |     |     |     |     |     |
| --------- | -------- | ----------- | ------------------------ | ---- | --- | --- | --- | --- | --- | --- | --- |
value holds greater significance in today’s economy.
potential outcomes.
4.1    True consumption agency
Additionally, some experimental results with real-
 inspirations[112–116]
world  data on  the  scenarios Fostering agency can be seen as moving toward true
| discussed |  in  these |  sections |  are  presented |  in  the |     |     |     |     |     |     |     |
| --------- | ---------- | --------- | --------------- | -------- | --- | --- | --- | --- | --- | --- | --- |
agency which means making independent, informed,
Appendix D. Note that the experiments are included
and deliberate choices about consumption, free from
solely to illustrate key theoretical insights in action;
external pressures, manipulative tactics, or systemic
they are not the focus of the contribution. Their role
constraints. True agency allows individuals to make
is supportive and interpretive, not foundational. decisions based on their genuine needs and financial
|                |     |            |              |     | circumstances, |  resisting |     |  the  forces |  that |  encourage |     |
| -------------- | --- | ---------- | ------------ | --- | -------------- | ---------- | --- | ------------ | ----- | ---------- | --- |
| 4    Suggested |     |  Solution: |  Intervening |  by |                |            |     |              |       |            |     |
unnecessary or excessive consumption.
Consumer Value Deliberation
|     |     |     |     |     | In  an |  ideal  world, |  where |  individuals |     |  enjoyed |  this |
| --- | --- | --- | --- | --- | ------ | -------------- | ------ | ------------ | --- | -------- | ----- |
The  results  presented  highlight  a  nuanced  outlook: level  of  agency  and  were  trying  to  maximize  their

Autonomy in consumption
|     |     | Obligatory consumption |     | Algorithmic persuasion |     | Work schedule instability |     |     |     |     |     |
| --- | --- | ---------------------- | --- | ---------------------- | --- | ------------------------- | --- | --- | --- | --- | --- |
Structural and economic
|     |     |     | constraints, essential or | Manipulative influences, |     |     | Temporal uncertainty,      |     |     |     |     |
| --- | --- | --- | ------------------------- | ------------------------ | --- | --- | -------------------------- | --- | --- | --- | --- |
|     |     |     |                           | impulsive spending       |     |     | hinders financial planning |     |     |     |     |
imposed expenses
Limited consumer agency
Constraints on independent, informed, and
value-aligned financial decisions
Lower financial welfare
Financial instability
Higher likelihood of early financial ruin

Fig. 1    Summary  of  the  explored  real-world  scenarios  with  bounded  consumer  agency,  with  each  scenario
illustrating a distinct aspect of limited consumer agency within the digital economy, often leading to unfavorable
financial outcomes.

    194 Journal of Social Computing, September 2025, 6(3): 184−208
financial  utility,  they  would  be  capable  of  avoiding recommendation systems critically, adapting them to
financial ruin indefinitely (we formally prove this in their  personal  values  rather  than  adopting  them
| Theorem |  A1  in |  the  Appendix |     |  A).  However, |  true | wholesale[120]. |     |     |     |     |     |     |
| ------- | ------- | -------------- | --- | -------------- | ----- | --------------- | --- | --- | --- | --- | --- | --- |
consumption agency may be an overly idealistic concept, To assess this category of interventions, we formally
given the reality that certain expenses, such as food, rent, demonstrate their impact. Specifically, we assume that
and legal obligations like taxes and child support, are individuals allocate their financial resources initially to
unavoidable  and  essential  for  maintaining  a  basic non-negotiable essential expenses (such as food, shelter,
standard  of  living.  While  true  agency  may  be  an taxes, and transportation) and other fundamental and
aspirational ideal, striving toward it as a value provides obligatory  needs.  Any  remaining  funds  are  then
a framework for developing practical solutions that budgeted for discretionary (opt-in) purchases, which
enhance consumer autonomy. are frequently shaped by algorithm-driven influences.
Therefore, we propose consumption value deliberation Consequently,  let  b  be  the  sum  of  minimum
as a guiding mindset for developing interventions at subsistence, obligatory consumption, and a fixed set of
both individual and societal levels. This approach seeks opted-in  impulsive  consumptions.  As  long  as  the
to  address  unavoidable  financial  obligations  while remaining  variable  fraction  of  the  impulsive
empowering  consumers  to  exercise  greater (cid:0)b the agent can avoid ruin.
|                                                   |     |     |     |     |     | consumption is <a |     |     | +y    |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | ----------------- | --- | --- | ----- | --- | --- | --- |
|                                                   |     |     |     |     |     |                   |     |     | t t+1 |     |     |     |
| consumption autonomy. Value deliberation empowers |     |     |     |     |     | That is,          |     |     |       |     |     |     |
consumers by enabling them to make more informed Theorem  4.  For  simplicity,  assume  R =1.  Also
t
choices. This process, for both consumers and policy- assume b>1=2. Let y ⩾b (where b is the fixed non-
t
makers, involves actively evaluating competing values, negotiable  expenses)  for  all  t.  Then  the  optimal
needs, and preferences that shape spending and saving consumption of a utility-maximizing consumer would
| decisions, |  thereby |  taking |  incremental |  steps |  toward |     |     |     |     |     |     |     |
| ---------- | -------- | ------- | ------------ | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
allow them to avoid ruin.
true agency.
|     |     |     |     |     |     | Concept |     |  sketch.  | Before |  presenting |  the |  formal |
| --- | --- | --- | --- | --- | --- | ------- | --- | --------- | ------ | ----------- | ---- | ------- |
proof of Theorem 4, we briefly outline the core idea.
4.2    Individual consumer value deliberation
Under the given assumptions, we show that if there
| At  the |  individual |  level, |  value |  deliberation-based |     |     |     |     |     |     |     |     |
| ------- | ----------- | ------- | ------ | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
exists a consumption path that terminates at some
| interventions |  lead |  to  consumer |     |  empowerment |  by |     |     |     |     |     |     |     |
| ------------- | ----- | ------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
finite time t, it is possible to construct an alternative
enabling individuals to consciously prioritize their genuine
|              |      |              |       |                   |     | infinite-horizon |     |  consumption |     |  sequence |  that |  yields |
| ------------ | ---- | ------------ | ----- | ----------------- | --- | ---------------- | --- | ------------ | --- | --------- | ----- | ------- |
| needs  above |  all |  else.  This |  type |  of  intervention |  is |                  |     |              |     |           |       |         |
strictly higher utility. The formal proof is given below.
inspired by previous work emphasizing that budgeting
helps with a clearer understanding of one’s financial Proof. Assume otherwise. The agent would have to
stop consuming at some time point T for this to be the
| situation, |  leading |  to  better |     |  decision-making |  and |       |      |           |     |               |              |     |
| ---------- | -------- | ----------- | --- | ---------------- | ---- | ----- | ---- | --------- | --- | ------------- | ------------ | --- |
|            |          |             |     |                  |      | case. |  Now |  consider |     |  the  optimal |  consumption |     |
increased financial stability[117–119]. Examples include:
|                                              |     |     |     |     |     | sequence fc; |     | c; :::; | c g. |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | ------------ | --- | ------- | ---- | --- | --- | --- |
| Encourage consumer reflection and awareness: |     |     |     |     |     |              |     | 0 1     | T    |     |     |     |
Inform  consumers  on  how  algorithmic  marketing Case 1: If c ⩾2b.
T
manipulates their choices. Promote critical reflections In this case consider the new consumption sequence,
|     |     |     |     |     |     | fc; |     | (cid:0)b; | :::g where the agent consumes |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------------------------- | --- | --- | --- |
to  help  consumers  identify  and  prioritize  their c; :::; c b; b; b;
|     |     |     |     |     |     | 0 1 | T   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:0)b at time step T and keeps on consuming b after that.
| authentic needs. |     |     |     |     |     | c   |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
T
Promote  financial  literacy  and  resistance It is easy to see that this is a feasible solution. We can
strategies:  Equip  consumers  with  skills  that  help see that the change in utility, d, is
u
| them with budgeting and resistance to spending on the |     |     |     |     |     |     | (   |     |     |     |     | )   |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     | (cid:229)T(cid:0)1 |     | (cid:229)+¥ |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ----------- | --- | --- |
fly  on  algorithmic  nudges.  Develop  educational d = btu(c)+bTu(c (cid:0)b)+ btu(b) (cid:0)
|     |     |     |     |     |     |     | u   |     | i   | T   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
resources to help consumers regain control over their (t=0 ) t=T+1
(cid:229)T(cid:0)1
decision-making processes in the digital environment. btu(c)+bTu(c ) =
| Controlled |     |  use  of |  algorithmic |  suggestions: |     |     |     |      | i   | T   |     |     |
| ---------- | --- | -------- | ------------ | ------------- | --- | --- | --- | ---- | --- | --- | --- | --- |
|            |     |          |              |               |     |     |     | t=(0 |     |     | )   |     |
b
| Advocate |  for |  treating |  algorithmically-generated |     |     |     |     |                |           |                |     |     |
| -------- | ---- | --------- | -------------------------- | --- | --- | --- | --- | -------------- | --------- | -------------- | --- | --- |
|          |      |           |                            |     |     |     | bT  | u(c (cid:0)b)+ |           | u(b)(cid:0)u(c | ) ⩾ |     |
|          |      |           |                            |     |     |     |     | T              | 1(cid:0)b |                | T   |     |
recommendations as tools for exploration rather than
|            |          |            |     |         |      |     | bT(u(c | (cid:0)b)+u(b)(cid:0)u(c |     | ))⩾0: |     |     |
| ---------- | -------- | ---------- | --- | ------- | ---- | --- | ------ | ------------------------ | --- | ----- | --- | --- |
| definitive |  guides. |  Consumers |     |  should |  use |     |        | T                        |     | T     |     |     |

  Pegah Nokhiz et al.:   Consumer Autonomy or Illusion? Rethinking Consumer Agency in the Age… 195
The first inequality simply uses the fact that b>1=2
4.3    Ethical and social regulation
and the second inequality is due to the fact that u(:) is On a societal level, consumption value deliberation can
| concave and therefore u(c |     | (cid:0)b)+u(b)⩾u(c |     | ). Thus, in |     |     |     |     |     |     |     |
| ------------------------- | --- | ------------------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
happen by policy-makers implementing regulations that
|     |     | T   |     | T   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
this case, we get a consumption sequence of infinite
|     |     |     |     |     |     | recognize |  the  importance |  of  respecting |     |  consumer |     |
| --- | --- | --- | --- | --- | --- | --------- | ---------------- | --------------- | --- | --------- | --- |
length that yields better utility.
|              |                   |         |          |      |       | autonomy,                                              |  enhancing  their |  agency, |  and |  ultimately |     |
| ------------ | ----------------- | ------- | -------- | ---- | ----- | ------------------------------------------------------ | ----------------- | -------- | ---- | ----------- | --- |
| Case 2: If c | <2b.              |         |          |      |       |                                                        |                   |          |      |             |     |
|              | T                 |         |          |      |       | guiding them toward achieving true consumption agency. |                   |          |      |             |     |
| We  can      |  see  that  there |  exists |  a  d>0  | such |  that |                                                        |                   |          |      |             |     |
Examples include,
(1(cid:0)b)c +bd=b  (because  1(cid:0)b<1=2  and  c <2b). Promote  ethical  AI  development:  Encourage
| T   |     |     |     |     | T   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
From this, using the concavity of u((cid:1)), we can see that the creation and implementation of ethical AI systems
u(b)=u((1(cid:0)b)c +bd)⩾(1(cid:0)b)u(c)+bu(d)⩾(1(cid:0)b)u(c). that  prioritize  consumer  and  worker  well-being  to
|     | T   |     | T   |     | T   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Now we can consider the new consumption sequence avoid disturbing the delicate balance between creating
| fc; |     |     | :::g, |     |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
where  c; :::; c T(cid:0)1 ; b; b; b;  where  the  agent persuasive advertising and exploiting the customer[120].
0 1
keeps on consuming b after time step T(cid:0)1. It is easy
|     |     |     |     |     |     | This  can |  be  achieved |  by  setting |     |  clear |  ethical |
| --- | --- | --- | --- | --- | --- | --------- | ------------- | ------------ | --- | ------ | -------- |
to see that this is a feasible solution. The change in guidelines[120]  to  prevent  manipulative  tactics  and
utility would be providing  incentives  (such  as  enhancing  employee
|     | (                  |             | )              |     |     |                                                     |     |     |     |     |     |
| --- | ------------------ | ----------- | -------------- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- |
|     |                    |             |                |     |     | morale and gaining a competitive edge) to companies |     |     |     |     |     |
|     | (cid:229)T(cid:0)1 | (cid:229)+¥ |                |     |     |                                                     |     |     |     |     |     |
|     | d = btu(c)+        |             | btu(b) (cid:0) |     |     |                                                     |     |     |     |     |     |
u i that prioritize responsible AI practices, particularly in
|     | (t=0 | t=T | )   |     |     |     |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
areas like work scheduling.
(cid:229)T(cid:0)1
|     | btu(c)+bTu(c |                | ) = |     |     |                                                          |     |     |     |     |     |
| --- | ------------ | -------------- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- |
|     |              | i              | T   |     |     | Algorithm regulation: Regulating algorithms can          |     |     |     |     |     |
|     | t=(0         |                | )   |     |     |                                                          |     |     |     |     |     |
|     | 1            |                |     |     |     | help reduce uncertainties related to financial planning. |     |     |     |     |     |
|     | bT           | u(b)(cid:0)u(c | ⩾0: |     |     |                                                          |     |     |     |     |     |
|     |              |                | )   |     |     | For instance, the Schedules that Work Act of 2014        |     |     |     |     |     |
|     | 1(cid:0)b    |                | T   |     |     |                                                          |     |     |     |     |     |
(H.R. 5159), introduced in the U.S. Congress, requires
The inequality comes from the fact we established
employers to provide employees with at least two
earlier. Therefore, in this case, we get a consumption
|     |     |     |     |     |     | weeks’  | notice  of  schedule |  changes |     |  and  minimum |     |
| --- | --- | --- | --- | --- | --- | ------- | -------------------- | -------- | --- | ------------- | --- |
sequence of infinite length that yields better utility.
|     |     |     |     |     |     | hours[96]. |  This  Act  acknowledges |     |  that |  employees |     |
| --- | --- | --- | --- | --- | --- | ---------- | ------------------------ | --- | ----- | ---------- | --- |
We can observe that in either case, for any finite
should have the ability to make informed decisions
consumption sequence, there is a way to improve it
about their personal time and should not be forced to
with an infinite horizon. Therefore, with a sufficiently
adapt to sudden changes imposed by employers. This
high income to cover their basic needs, consumers
value is rooted in respect for individual rights and
| can  maximize |  their  utility |  while |  still |  avoiding |  early |     |     |     |     |     |     |
| ------------- | --------------- | ------ | ------ | --------- | ------ | --- | --- | --- | --- | --- | --- |
personal choice.
■
ruin.
|                |     |            |                |     |       | In  another |  example,      |  the  San    |  Francisco |  Board |  of     |
| -------------- | --- | ---------- | -------------- | --- | ----- | ----------- | -------------- | ------------ | ---------- | ------ | ------- |
| To  summarize, |  by |  deploying |  interventions |     |  that |             |                |              |            |        |         |
|                |     |            |                |     |       | Supervisors |  has  improved |  protections |            |  for   |  hourly |
increase self-discipline to allocate the funds for the
workers in retail chain stores by adopting provisions
products or services truly needed (and then evaluating
from the Retail Workers Bill of Rights. These new
| the  remaining |  amount |  for  discretionary |     |  spending), |     |             |                     |     |              |          |     |
| -------------- | ------- | ------------------- | --- | ----------- | --- | ----------- | ------------------- | --- | ------------ | -------- | --- |
|                |         |                     |     |             |     | regulations |  require  employers |     |  to  provide |  greater |     |
consumers can gain greater control over their finances
advance notice when setting/changing work schedules,
and avoid early ruin. aiming to improve predictability for employees[96].
Remark   on   return   rates   and   β.    Theorem  4 In  the  context  of  work  scheduling,  implementing
assumes R =1 and b>1=2. The assumption R =1 is regulations like the examples above has shown positive
|     | t   |     |     |     | t   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
made for simplicity, but the argument does not depend effects. References [109, 110] reveal that employees
⩾1.
on this specific value and remains valid for any R who are given advanced notice of schedule changes
t
The condition b>1=2 reflects the idea that when b is
|     |     |     |     |     |     | experience |  improved  financial |  well-being. |     |  Advanced |     |
| --- | --- | --- | --- | --- | --- | ---------- | -------------------- | ------------ | --- | --------- | --- |
too small, the incentive to delay consumption diminishes,
|     |     |     |     |     |     | planning |  allows  workers |  with  variable |     |  schedules |  to |
| --- | --- | --- | --- | --- | --- | -------- | ---------------- | --------------- | --- | ---------- | --- |
leading consumers to prefer immediate consumption gain greater autonomy over their financial planning.
in  order  to  maximize  utility.  Ensuring  that  b  is That  is,  they  can  manage  their  consumption  and
sufficiently large prevents the resulting behavior from savings more effectively, which leads to better financial
being solely driven by discounting effects. decision-making and agency.

    196 Journal of Social Computing, September 2025, 6(3): 184−208
5    Limitation and Future Work incorporate  these  normative  dimensions  into
|     |     |     |     |     |     |     | optimization |  models. |     |  This  could |  involve |  developing |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ------------ | -------- | ----------- | --- |
In this section, we present discussions and list some of
|     |     |     |     |     |     |     | frameworks |  that |  not |  only |  account |  for |  traditional |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | ---- | ----- | -------- | ---- | ------------ |
the limitations of our study.
|     |     |     |     |     |     |     | economic |  factors |  but |  also |  consider |  the |  ethical |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ---- | ----- | --------- | ---- | -------- |
Intertemporal consumption model. The model
implications of consumption decisions.
employed here is intentionally simple, relying on utility-
Behavioral economics, cognitive impacts, and
maximizing rational agents. This does not imply that
prospect theory. While our model is grounded in
we believe individuals in the real world are perfectly
the rational utility-maximizing framework (due to the
| rational  utility |  maximizers. |       |  Rather, |  our  |  focus           |  is  on |         |            |     |      |           |              |     |
| ----------------- | ------------ | ----- | -------- | ----- | ---------------- | ------- | ------- | ---------- | --- | ---- | --------- | ------------ | --- |
|                   |              |       |          |       |                  |         | reasons |  mentioned |  in |  the |  previous |  paragraph), |  we |
| demonstrating     |  that        |  even |  within  |  this |  straightforward |         |         |            |     |      |           |              |     |
acknowledge that real-world consumer behavior gets
representation of reality, where agents make the most
impacted by cognitive factors and behavioral elements.
optimal decisions possible, the adverse effects of a lack
|     |     |     |     |     |     |     | Behavioral |  economics |     |  has |  demonstrated |     |  that |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | ---- | ------------- | --- | ----- |
of agency in consumption are still evident. Furthermore,
|                   |     |          |         |      |      |         | individuals |  frequently |            |  exhibit |  present          |  bias[125], |  loss |
| ----------------- | --- | -------- | ------- | ---- | ---- | ------- | ----------- | ----------- | ---------- | -------- | ----------------- | ----------- | ----- |
| while  discounted |     |  utility |  models |  may |  not |  be  as |             |             |            |          |                   |             |       |
|                   |     |          |         |      |      |         | aversion    |  and        |  reference |          |  dependence[126], |             |  and  |
innovative or advanced as some newer alternatives,
inconsistent preferences under uncertainty[127]. These
they remain the most commonly used framework for tendencies  can  significantly  impact  consumption
analyzing intertemporal choice[121].
decisions. For instance, present-biased consumers may
However, the absence of debt and other liabilities is
be particularly vulnerable to short-term promotions
a limitation in our framework. For example, in real-
or Buy Now Pay Later schemes, choosing immediate
world scenarios, controlled debt, such as credit card
|                       |     |             |              |     |            |     | gratification |  despite |     |  long-term |  financial |     |  harm[127]. |
| --------------------- | --- | ----------- | ------------ | --- | ---------- | --- | ------------- | -------- | --- | ---------- | ---------- | --- | ----------- |
| usage,  significantly |     |  influences |  consumption |     |  patterns. |     |               |          |     |            |            |     |             |
Similarly, the framing of losses in subscription-based
Consumers often rely on credit even when they lack
|     |     |     |     |     |     |     | services |  or  scarcity |     |  cues  in |  digital |  marketing |  can |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- | --------- | -------- | ---------- | ---- |
sufficient assets to cover their expenses. However, exploit reference dependence, causing consumers to
our model does not account for these scenarios. Debt over-consume  or  stick  to  suboptimal  payment
plays a dual role in consumption: it acts as an enabler, commitments. Prospect theory[126] provides a more
| allowing  individuals |     |  to |  make  purchases |     |  they |  might |     |     |     |     |     |     |     |
| --------------------- | --- | --- | ---------------- | --- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
psychologically realistic alternative by capturing such
| otherwise |  forgo, |  while |  simultaneously |     |  introducing |     |     |     |     |     |     |     |     |
| --------- | ------- | ------ | --------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
anomalies through non-linear probability weighting and
| hidden  costs |  through |  the |  accumulation |     |  of  interest |     |     |     |     |     |     |     |     |
| ------------- | -------- | ---- | ------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
asymmetric value functions.
| and  long-term |  debt |  burdens. |     |  Additional |  details |  on |     |     |     |     |     |     |     |
| -------------- | ----- | --------- | --- | ----------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
While these extensions would undoubtedly enrich
debt  (and  discounting[40, 122])  can  be  found  in  the the  descriptive  accuracy  of  our  framework,  our
Appendix C. decision to use a classical discounted utility model was
Additionally, consumers may not only be individuals deliberate: it allows us to isolate the structural impacts
but also organizations or communities, each aiming to of agency constraints in a clean and tractable way,
maximize multiple objectives that may not necessarily
ensuring that any observed harms are not artifacts of
align with utility. For instance, they might prioritize
|     |     |     |     |     |     |     | irrational |  behavior |  but |  instead |  emerge |  even |  under |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ---- | -------- | ------- | ----- | ------ |
minimizing expenses or risk, maximizing social welfare,
|     |     |     |     |     |     |     | optimal |  decision-making. |     |  This |  offers |  a  |  tractable |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------------- | --- | ----- | ------- | --- | ---------- |
environmental sustainability, profit, and so on. Our estimate of the risks posed by limited agency, meaning
model does not account for these cases. that under behavioral models, these effects may be
Furthermore, when using consumption models to stronger or more pervasive. Future work could build
analyze  intertemporal  decision-making,  it  is  crucial on this foundation by embedding bounded rationality
for researchers, policymakers, and advisors to account and behavioral parameters into the model to evaluate
for  the  normative  commitments  that  may  be their compounding effects.
overlooked[123–124]. For example, incorporating ethical
Societal uniformity. Our paper assumes a level of
considerations, such as the impact of advertising or societal  uniformity  with  all  agents  facing  similar
the psychological effects of social comparison, could external forces and constraints, however, there exist
lead to more comprehensive models. societal inequities where certain groups are targeted
Future research in this area could explore how to more by algorithms or have more payment obligations.

Pegah Nokhiz et al.: Consumer Autonomy or Illusion? Rethinking Consumer Agency in the Age… 197
Furthermore, the likelihood of benefiting from public not considered as deciding factors in our study, e.g.,
policies aimed at addressing these disparities may also inflation erodes the purchasing power of consumers,
vary among different demographic groups. For example, making it more difficult for individuals to maintain their
if the individual is a gig worker, some of the policy standard of living and save for future consumption.
interventions such as a minimum window of advance Similarly, unexpected social emergencies, such as
notice for altering work schedules do not apply to them. pandemics, can lead to financial precarity with sudden
If there exists diversity among individuals in managing unemployment, reduced income, or increased health-
their finances based on a specific community they are related expenses[100], significantly affecting consumption
part of, the system could try to incorporate this patterns.
heterogeneity into its decision-making processes. Like other foundational economic models, ours
Additionally, lower-income individuals, gig workers, offers a foundation for the future. More complex
or those with limited digital literacy, are more likely to extensions (with more complex macro factors) are
rely on platforms with dark patterns and Buy Now Pay possible. So to expand upon and complement the
Later systems. These dynamics are further compounded aforementioned macro-level factors, one may consider:
by racial and ethnic disparities, as marginalized • Inflation: As mentioned earlier, inflation reduces
communities may be overrepresented in precarious the real value of income and savings over time,
labor sectors and underprotected by regulatory
potentially accelerating financial ruin even under
infrastructure[33]. Thus, the risks we model may in fact
otherwise sustainable consumption plans.
be amplified for these groups, making the normative
• Economic recessions: Lead to increased
question of consumption agency all the more urgent.
unemployment, reduced wages, and greater scheduling
This recognition has direct implications for the
instability, further constraining agency and raising the
design of targeted interventions: First, policy
likelihood of ruin.
frameworks could prioritize sector-specific algorithmic
• Public health or emergency crises (e.g., pandemics):
regulation, particularly in domains like retail, delivery,
Trigger sudden behavioral changes in spending (e.g.,
and food service, where unpredictable scheduling and
panic buying), disrupt work schedules, and create new
surveillance technologies are common. For instance,
obligatory expenses (e.g., healthcare and remote work
existing initiatives like the Retail Workers Bill of Rights
infrastructure).
in San Francisco can be endorsed more carefully for
• Government-based regulations like subsidies or
the most affected workers. Second, consumer
stimulus packages can also influence income levels and
protection strategies can be sensitive to digital
consumption decisions by providing temporary relief
manipulation risks among lower-income populations,
or incentives for certain types of spending[101], such as
like opt-in delays for Buy Now Pay Later usage on
renewable energy adoption or housing investments.
platforms where these features disproportionately
• Also, economic recessions or global supply chain
exploit financial vulnerability. Third, financial education
disruptions may result in income instability and
efforts must be context-aware: programs targeting low-
increased costs of goods and services[128], further
income or gig workers should not assume ample time,
constraining consumer choices.
attention, or technological access. Instead, these
programs can be delivered via workplace partnerships, These impacts and the underlying population’s
mobile-accessible content, or simplified budgeting response to them (as well as the recourse to change
tools that accommodate erratic income. Finally, circumstances[129]) differ significantly based on factors
consumer-facing transparency requirements (for such as gender[130–131], disability[132], race[133], and
example, algorithmic decision notices or cost- health status[134]. While these factors are critical in
accumulation alerts) could help mitigate manipulation shaping consumption behavior, they fall outside the
in environments where deliberation is otherwise scope of our current study and remain important
undermined. areas for the future.
Other future directions: macro On the motivation behind proposed
socioeconomical impacts. There are external interventions & more specific interventions. To
socioeconomic impacts on one’s income that we have ground our recommendations in real-world practices,

    198 Journal of Social Computing, September 2025, 6(3): 184−208
we draw on existing policy interventions as illustrative 6    Conclusion
cases. For instance, the Schedules that Work Act in
This paper’s core contribution is a formal analysis of
the U.S. Congress and San Francisco’s Retail Workers
financial instability arising from diminished consumption
Bill of Rights demonstrate the viability of regulating
agency. Our framework tackles three key questions
| algorithmic |  work |  scheduling |     |  by  mandating |     |  advance |     |     |     |     |     |     |     |
| ----------- | ----- | ----------- | --- | -------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
relevant to consumption agency in today’s economy.
notice and predictable hours.
• What are the aftereffects of a lack of agency in
These initiatives offer promising templates but also
|           |                 |     |              |     |             |      | consumption, |      |  particularly |        |  when    |  exacerbated |  by     |
| --------- | --------------- | --- | ------------ | --- | ----------- | ---- | ------------ | ---- | ------------- | ------ | -------- | ------------ | ------- |
| highlight |  implementation |     |  challenges. |     |  Businesses |  may |              |      |               |        |          |              |         |
|           |                 |     |              |     |             |      | algorithms?  |  How |  do           |  these |  effects |  manifest    |  across |
face increased compliance costs, particularly small or
different scenarios, such as obligatory consumption,
resource-constrained employers who rely on just-in-
|                   |     |             |     |        |      |              | impulsive |  algorithm-driven |     |     |  purchases, |  and |  dynamic |
| ----------------- | --- | ----------- | --- | ------ | ---- | ------------ | --------- | ----------------- | --- | --- | ----------- | ---- | -------- |
| time  scheduling. |     |  Similarly, |     |  calls |  for |  algorithmic |           |                   |     |     |             |      |          |
work scheduling?
| transparency |  may |  encounter |     |  pushback |     |  due  to |     |     |     |     |     |     |     |
| ------------ | ---- | ---------- | --- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
• Why should consumption be considered a value
| proprietary |  concerns |     |  or  technical |     |  opacity. |  On  the |     |     |     |     |     |     |     |
| ----------- | --------- | --- | -------------- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
that needs to be fostered rather than a given in the
| consumer |  side, |  education |  campaigns |     |  must |  contend |     |     |     |     |     |     |     |
| -------- | ------ | ---------- | ---------- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
modern economy?
| with  low |  engagement, |     |  information |     |  fatigue, |  and |     |     |     |     |     |     |     |
| --------- | ------------ | --- | ------------ | --- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
• What are the effects of educational and policy
resistance to behavior change. Therefore, any effective
regulatory interventions served as consumption value
| intervention |  must         |  balance       |  regulatory |              |  ambition |  with   |              |          |     |      |           |            |     |
| ------------ | ------------- | -------------- | ----------- | ------------ | --------- | ------- | ------------ | -------- | --- | ---- | --------- | ---------- | --- |
|              |               |                |             |              |           |         | deliberation |  methods |     |  (by |  enabling |  consumers |  to |
| practical    |  feasibility, |  incorporating |             |  incentives, |           |  phased |              |          |     |      |           |            |     |
achieve true agency and empowering them in their
| rollouts, |  and |  stakeholder |  input |  to |  ensure |  both |     |     |     |     |     |     |     |
| --------- | ---- | ------------ | ------ | --- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
decision-making)?
compliance and impact. Future work could formalize
We answer these questions through formal analyses
these trade-offs and assess policy outcomes through
|     |     |     |     |     |     |     | of  intertemporal |     |  consumption |     |  models |  with |  limited |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------------ | --- | ------- | ----- | -------- |
simulations or field studies.
|     |     |     |     |     |     |     | consumption |     |  agency |  and |  illustrate |  the |  resulting |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | ---- | ----------- | ---- | ---------- |
We contend that consumer agency was limited even
adverse effects (like early financial ruin and diminished
before the prevalent use of algorithms, but automation
consumer utility) that arise when consumer agency is
has made existing issues more widespread. Thus, to
eroded by systemic barriers, algorithmic manipulation,
motivate our interventions and through the proposed
and obligatory consumption patterns. We also illustrate
| interventions, |     |  we |  aim |  to  support |     |  gradual |     |     |     |     |     |     |     |
| -------------- | --- | --- | ---- | ------------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
the positive effects of recognizing consumer agency as
improvements to empower consumers, but they may
a value and adopting value deliberation as a mindset
not fully restore agency in all contexts.
for interventions at both individual and societal levels.
That is, the specificity, effectiveness, and desirability
|     |     |     |     |     |     |     | Potential |  measures |  include |     |  regulatory |  oversight |  to |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | -------- | --- | ----------- | ---------- | --- |
of certain interventions are very context-dependent.
|     |     |     |     |     |     |     | mitigate |  manipulative |     |  practices |     |  and |  consumer |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- | ---------- | --- | ---- | --------- |
Therefore, our proposals are intended as part of an
education initiatives to improve financial literacy.
| ongoing,  |  necessary       |     |  conversation |     |  about |  how  to      |          |     |     |     |     |     |     |
| --------- | ---------------- | --- | ------------- | --- | ------ | ------------- | -------- | --- | --- | --- | --- | --- | --- |
| intervene |  in  algorithmic |     |  systems      |     |  that  |  increasingly | Appendix |     |     |     |     |     |     |
shape consumption. The interventions’ aim was not to
A    True Agency in an Ideal Setting
present a specific finished solution but to reframe the
debate around actionable steps given the algorithmic
In an ideal world, where individuals enjoy true agency,
erosion  of  agency.  Interventions  create  friction  in they  would  be  capable  of  avoiding  financial  ruin
exploitative processes and empower consumers within indefinitely. We formally state this below.
those  constraints.  Relevant  contributions  also  add Theorem A1. Assuming that Y (Y ⩾0) is drawn
t t
value to current debates on responsible AI and digital from a distribution with known mean (denoted by Y),
governance. if we allow the agent to vary the consumption without
|     |     |     |     |     |     |     | any variability constraints other than 0⩽c |     |     |     |     |     | ⩽a, then |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | -------- |
Nonetheless, the intervention we formally analyze in
t t
Section 4.2 is very specific and focuses on a more under isoelastic utility with l>0 (and l̸=1), a rational
concrete  objective;  namely,  encouraging  effective agent with utility maximization goals could consume
budgeting and value-based deliberation in consumption with infinite horizon without going to ruin early.
| decisions. |     |     |     |     |     |     | The proof of the Theorem A1 is as follows: |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- |

  Pegah Nokhiz et al.:   Consumer Autonomy or Illusion? Rethinking Consumer Agency in the Age… 199
Proof. Assume that you are given parameter b and
|     |     |     |     |     |     |     |     | as desired. |     |     |     |     |     |     | ■   |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
utility function u(c). Consider the optimal consumption
|     |     |     |     |     |     |     |     | B    Work |  Scheduling: |     |     |  Formal |  Theorem |     |  and |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | --- | --- | ------- | -------- | --- | ---- |
sequence that you get where the agent goes to ruin at
the Corresponding Proofs (Restated from
time point T (here, asset ruin is assumed to be the
Refs. [109, 110])
point where the available assets for the next iteration
|                             |     |            |     |     |         |                       |     | Let  y,                                                | x,  and  | c   | represent |     |  income, |  assets, |  and |
| --------------------------- | --- | ---------- | --- | --- | ------- | --------------------- | --- | ------------------------------------------------------ | -------- | --- | --------- | --- | -------- | -------- | ---- |
|                             |     |            |     |     |         |                       |     | t                                                      | t        |     | t         |     |          |          |      |
| reach 0). Let this be C=fc; |     |            |     |     | c; :::; | c g. This is possible |     |                                                        |          |     |           |     |          |          |      |
|                             |     |            |     | 1   | 2       | T                     |     | consumption at time t, respectively, with T indicating |          |     |           |     |          |          |      |
|                             |     |            |     | ⩽a  |         |                       |     |                                                        |          |     |           | p   |          |          |      |
| only if Y                   |     | =0 since c |     | .   |         |                       |     |                                                        |          |     |           |     |          |          |      |
T+1 T T the job duration and u(c)= c representing the utility
|                                                       | Now |  consider                  |  the         |  amended |          |  sequence |  where      |                                                      |        |               |           |     |            |         |      |
| ----------------------------------------------------- | --- | -------------------------- | ------------ | -------- | -------- | --------- | ----------- | ---------------------------------------------------- | ------ | ------------- | --------- | --- | ---------- | ------- | ---- |
|                                                       |     |                            |              |          |          |           |             | derived                                              |  from  |  consumption  |           | c.  |  Also,     |  assume |  no  |
| C(cid:3)=fc;                                          |     | c; :::;                    | (cid:0)e; e; | :::g.    |  We  can |  see      |  that  this |                                                      |        |               |           |     |            |         |      |
|                                                       |     |                            | c            |          |          |           |             | discounting (b=1) and that income y lies within the  |        |               |           |     |            |         |      |
|                                                       | 1   | 2                          | T            |          |          |           |             |                                                      |        |               |           |     |            |         |      |
| does not go to asset ruin at point T since we consume |     |                            |              |          |          |           |             |                                                      |        |               |           |     | t          |         |      |
|                                                       |     |                            |              |          |          |           |             | range                                                | [0;Y]. |  Previous     |  research |     |  in  Refs. |  [109,  | 110] |
| less than c                                           |     |  and we still have e left. |              |          |          |           |             |                                                      |        |               |           |     |            |         |      |
|                                                       |     | T                          |              |          |          |           |             | shows that in certain cases, a worker with lookahead |        |               |           |     |            |         |      |
(cid:229)T(cid:0)1
We can see that the total utility for C is  btu(c)+ privileges has a distinct advantage over one without,
t
t=1
bT(cid:1)u(c and this benefit increases linearly with the amount of
) and we can also see that the total utility for C(cid:3)
T
|     |          |        | (cid:229)T(cid:0)1 |                     |     |                            |     | lookahead.                                           |     |     |     |     |     |     |     |
| --- | -------- | ------ | ------------------ | ------------------- | --- | -------------------------- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |          |        |                    | btu(c)+bT(cid:1)u(c |     | (cid:0)e)+bT+1(cid:1)u(e). |     |                                                      |     |     |     |     |     |     |     |
| is  |  greater |  than  |                    |                     |     |                            |     |                                                      |     |     |     |     |     |     |     |
|     |          |        |                    | t                   |     | T                          |     | Before presenting the main theorem, Refs. [109, 110] |     |     |     |     |     |     |     |
t=1
Therefore, the change in utility is
introduce the following lemma:
|     |     | (                  |                     |     |                           |     | )       |               |       |      |            |     |                  |     |      |
| --- | --- | ------------------ | ------------------- | --- | ------------------------- | --- | ------- | ------------- | ----- | ---- | ---------- | --- | ---------------- | --- | ---- |
|     |     |                    |                     |     |                           |     |         |               |       |      | a2(1=2;1)  |     |                  |     |      |
|     |     | (cid:229)T(cid:0)1 |                     |     |                           |     |         | Lemma         |  A1.  | Let  |            |     | be  a  constant, |     |  and |
|     | d   | >                  | btu(c)+bT(cid:1)u(c |     | (cid:0)e)+bT+1(cid:1)u(e) |     | (cid:0) |               |       |      |            |     |                  |     |      |
|     | u   |                    | t                   |     | T                         |     |         | w2(0;1). Then |       |      |            |     |                  |     |      |
|     |     | ( t=1              |                     | )   |                           |     |         |               |       |      |            |     |                  |     |      |
(cid:229)T(cid:0)1
|     |     | btu(c        | )+bT(cid:1)u(c                               |     |     |     |     |     | p   | p   |     |                    |                 |     |     |
| --- | --- | ------------ | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --------------- | --- | --- |
|     |     |              |                                              | )   | >   |     |     |     | w⩽  |     | p 1 | (w(cid:0)a)(cid:0) | 1 (w(cid:0)a)2: |     |     |
|     |     |              | t                                            | T   |     |     |     |     |     | a+  |     |                    |                 |     |     |
|     |     | t=1          |                                              |     |     |     |     |     |     |     | 2 a |                    | 8               |     |     |
|     |     | bT(cid:1)u(c | (cid:0)e)+bT+1(cid:1)u(e)(cid:0)bT(cid:1)u(c |     |     | ):  |     |     |     |     |     |                    |                 |     |     |
|     |     | T            |                                              |     |     | T   |     |     |     |     |     |                    |                 |     |     |
Proof. We have
Now what we are left to do is to argue that there
exists an e>0 that satisfies bT(cid:1)u(c (cid:0)e)+bT+1(cid:1)u(e)⩾   p p 1
|     |     |     |     |     |     |     |     |     |     | w(cid:0) | a(cid:0) | p (w(cid:0)a)= |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | -------------- | --- | --- | --- |
T
bT(cid:1)u(c =) (cid:0)e)+b(cid:1)u(e)⩾u(c ). Let g(e)=u(c (cid:0) 2 a
|     | )   | u(c |     |     |     |     |     |     |     |     | (   |     | )   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | T   |     | T   |     | T   |     | T   |     |     |     |     |     |     |     |     |
e)+b(cid:1)u(e), then we would like to claim that there p 1 p p 1
|     |     |     |     |     |     |     |     |     |     | (w(cid:0)a) |     | (cid:0) | =   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |     |             | w+  | a       | 2 a |     |     |
exists a e>0 such that g(e)⩾g(0). Consider the e
(w(cid:0)a)(a(cid:0)w)
that maximizes g((cid:1)), then for this bu′(e)=u′(c (cid:0)e). p p p =
T
|     |                               |     |     |     | c1(cid:0)l(cid:0)1 |               |     |     |     | 2 a(      | w+            | a)2 |     |     |     |
| --- | ----------------------------- | --- | --- | --- | ------------------ | ------------- | --- | --- | --- | --------- | ------------- | --- | --- | --- | --- |
|     | Isoelastic utility: Let u(c)= |     |     |     |                    | . Assume that |     |     |     |           | (w (cid:0)a)2 |     |     |     |     |
|     |                               |     |     |     | 1(cid:0)l          |               |     |     |     | (cid:0) p | p             | p : |     |     |     |
l̸=1.  Let  e>0  be  such  that  be(cid:0)l=(c (cid:0)e)(cid:0)l =) 2 a( w+ a)2
T
| bu′(e)=u′(c |     | (cid:0)e). |  For |  notational |     |  convinience, |  let |       |      |              |     |             |     |     |      |
| ----------- | --- | ---------- | ---- | ----------- | --- | ------------- | ---- | ----- | ---- | ------------ | --- | ----------- | --- | --- | ---- |
|             |     | T          |      |             |     |               |      | Since |  the |  denominator |     |  satisfies  | ⩽8, |  we |  get |
s=be(cid:0)l=(c (cid:0)e)(cid:0)l Then, we can see that, p p 1 1
|     |       | T                             |     |                      |     |     |     | w⩽  | a+ p | (w(cid:0)a)(cid:0) |     | (w(cid:0)a)2. |     |     | ■   |
| --- | ----- | ----------------------------- | --- | -------------------- | --- | --- | --- | --- | ---- | ------------------ | --- | ------------- | --- | --- | --- |
|     |       | (c (cid:0)e)1(cid:0)l(cid:0)1 |     | (e)1(cid:0)l(cid:0)1 |     |     |     |     | 2    | a                  | 8   |               |     |     |     |
|     | g(e)= | T                             |     | +b                   |     |     |     |     |      |                    |     |               |     |     |     |
1(cid:0)l 1(cid:0)l = Theorem A2. Consider two individuals: one with a
(c (cid:0)e) (e) 1+b lookahead  of  k  steps  and  the  other  without  any
|     |     | T         | (c (cid:0)e)(cid:0)l+b(e)(cid:0)l |     |           | (cid:0) | =         |                          |     |     |     |                            |     |     |     |
| --- | --- | --------- | --------------------------------- | --- | --------- | ------- | --------- | ------------------------ | --- | --- | --- | -------------------------- | --- | --- | --- |
|     |     | 1(cid:0)l |                                   |     | 1(cid:0)l |         | 1(cid:0)l |                          |     |     |     |                            |     |     |     |
|     |     |           | T                                 |     |           |         |           | lookahead. Let c;c;:::;c |     |     |     |  denote the consumption of |     |     |     |
|     |     |           |                                   |     |           |         |           |                          |     | 1   | 2   | T                          |     |     |     |
|     |     | c         | 1+b                               |     |           |         |           |                          |     |     |     |                            |     |     |     |
T s(cid:0) = the individual with k-step lookahead, and z ;z ;:::;z
|     |     | 1(cid:0)l  | 1(cid:0)l |     |     |     |     |        |                   |     |     |          |             | 1 2      | T   |
| --- | --- | ---------- | --------- | --- | --- | --- | --- | ------ | ----------------- | --- | --- | -------- | ----------- | -------- | --- |
|     |     |            |           |     |     |     |     | denote |  the  consumption |     |     |  of  the |  individual |  without |     |
|     |     | c1(cid:0)l | cl        | 1+b |     |     |     |        |                   |     |     |          |             |          |     |
T T (cid:0) = lookahead. There exist instances where all incomes lie
|     |     | 1(cid:0)l(c | (cid:0)e)l   | 1(cid:0)l |           |     |     |                                   |     |            |                   |      |     |     |     |
| --- | --- | ----------- | ------------ | --------- | --------- | --- | --- | --------------------------------- | --- | ---------- | ----------------- | ---- | --- | --- | --- |
|     |     |             | T            |           |           |     |     | within the range [0;Y], such that |     |            |                   |      |     |     |     |
|     |     | c1(cid:0)l  | c            | l 1+b     |           |     |     |                                   |     |            |                   |      |     |     |     |
|     |     |             | T            | (cid:0)   |           |     |     |                                   |     |            |                   |      |     |     |     |
|     |     | T           |              |           | =         |     |     |                                   |     |            |                   |      |     |     |     |
|     |     | 1(cid:0)l   | (c (cid:0)e) | 1(cid:0)  | l         |     |     |                                   |     | p          |                   | p    | p   |     |     |
|     |     |             | ( T          |           | )         |     |     |                                   |     | (cid:229)T | (cid:0)(cid:229)T | ⩾Ω(k |     |     |     |
|     |     |             |              |           | l         |     |     |                                   |     |            | c                 | z    | Y): |     |     |
|     |     | c1(cid:0)l  |              | e         | 1+b       |     |     |                                   |     |            | t                 | t    |     |     |     |
|     |     | T           | 1+           |           | (cid:0)   | =   |     |                                   |     | t=1        | t=1               |      |     |     |     |
|     |     | 1(cid:0)l   |              | (cid:0)e) | 1(cid:0)l |     |     |                                   |     |            |                   |      |     |     |     |
(c
|     |     |             |        | T        |           |     |     | Proof.                   | References |     |  [109,                         | 110] |  assume |  that |  both |
| --- | --- | ----------- | ------ | -------- | --------- | --- | --- | ------------------------ | ---------- | --- | ------------------------------ | ---- | ------- | ----- | ----- |
|     |     | c1 (cid:0)l | (      | )        | 1+b       |     |     |                          |            |     |                                |      |         |       |       |
|     |     |             | 1+b1=l | l(cid:0) | ⩾         |     |     |                          |            |     |                                |      |         |       |       |
|     |     | T           |        |          |           |     |     | individuals start with a |            |     | =0. Also, since incomes can be |      |         |       |       |
|     |     | 1(cid:0)l   |        |          | 1(cid:0)l |     |     |                          |            |     | 1                              |      |         |       |       |
c1(cid:0)l(cid:0)1 scaled without loss of generality, the assumption is
|     |     | (1+b) |     | ⩾g(0); |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
T 1(cid:0)l
that Y=1. Let y be defined as
t

    200 Journal of Social Computing, September 2025, 6(3): 184−208
{

|     |     |     | 1; fort⩽k=2; |     |     |     | Using Lemma A1: |     |     |     |     |     |     |
| --- | --- | --- | ------------ | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
y =
|     |     | t   | fork=2<t⩽k; |     |     |     |             |      | p   |                      |               |     |     |
| --- | --- | --- | ----------- | --- | --- | --- | ----------- | ---- | --- | -------------------- | ------------- | --- | --- |
|     |     |     | x;          |     |     |     |   (cid:229) | p    |     | 1 (cid:229)          | 1             |     |     |
|     |     |     |             |     |     |     |             | z ⩽k | a+  | p (z(cid:0)a)(cid:0) | (z(cid:0)a)2: |     |     |
|     |     |     |             |     |     |     |             | i    |     |                      | i             | i   |     |
|     |     |     |             |     |     |     |             |      | 2   | a                    | 8             |     |     |
where x is uniformly sampled from the interval [0;1]. i⩽k i⩽k
Both individuals are aware of this input distribution. Since the total consumption cannot exceed the total
For  simplicity,  they  assume  that  the  total  time income (equal to ka), the middle term on the right
horizon T equals k. This assumption can be relaxed by is ⩽0. This simplifies to
(1+x)
| setting y | =     |          |               |                  |         |        |     |           | p   | p          |               |     |     |
| --------- | ----- | -------- | ------------- | ---------------- | ------- | ------ | --- | --------- | --- | ---------- | ------------- | --- | --- |
|           | t     |          |  for all t>k. |                  |         |        |     | (cid:229) | ⩽k  | a(cid:0) 1 | (z(cid:0)a)2: |     |     |
|           |       | 2        |               |                  |         |        |     |           | z   |            |               |     |     |
|           |       |          |               |                  |         |        |     |           | i   | 8          | i             |     |     |
| Firstly,  |  they |  examine |               |  the  individual |  using  | k-step |     | i⩽k       |     |            |               |     |     |
lookahead. Since this individual can observe the value Using the Cauchy-Schwarz inequality and Formula
1+x
| of x, they opt to consume an amount of  |     |     |     |     |     |  at each | (A2): |     |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | -------- | ----- | --- | --- | --- | --- | --- | --- |
2
|     |     |     |     |     |     |     |     |     |     | (   | )   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |     |     | 2   |     |     |
time step. This strategy is viable because the income (cid:229) (z(cid:0)a)2⩾ 1 (cid:229)jz(cid:0)aj
>c2k:
during the first k=2 steps is y =1, ensuring that their i k i
|     |     |     |     |     |     |     |     | i   |     | i   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t
assets are adequate to sustain this consumption. As a
Combining these inequalities, it follows that:
re√su lt ,  the total utility (given that T=k) amounts to
|     |       |     |     |     |     |     |     |     | p           | p           | c2k |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | --- | --- | --- |
|     |       |     |     |     |     |     |     |     | (cid:229) z | ⩽k a(cid:0) | :   |     |     |
|     | 1 + x |     |     |     |     |     |     |     |             | i           |     |     |     |
| k   | .     |     |     |     |     |     |     |     |             |             | 8   |     |     |
|     | 2     |     |     |     |     |     |     |     | i           |             |     |     |     |
This result demonstrates that if the deterministic
Next, they examine the individual without lookahead.
Intuitively, this person is unable to predict the value of algorithm chooses z values that satisfy Formula (A1),
i
1+x
the no-lookahead algorithm results in a total utility
| x, making it impossible to consistently consume  |     |     |     |     |     | .   |     |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2
that is Ω(k) worse than that of the lookahead algorithm.
References [109, 110] show that even with complex
To complete the proof, Refs. [109, 110] show that if
| strategies, |     |  the  individual |     |  without  lookahead |     |  cannot |               |            |     |             |        |        |      |
| ----------- | --- | ---------------- | --- | ------------------- | --- | ------- | ------------- | ---------- | --- | ----------- | ------ | ------ | ---- |
|             |     |                  |     |                     |     |         | x  is  chosen |  uniformly |     |  at  random |  from  | (0;1), |  the |
achieve a high total utility.
|      |        |        |          |                |     |        | condition |  Formula |  (A1) |  holds |  with |  a  constant |     |
| ---- | ------ | ------ | -------- | -------------- | --- | ------ | --------- | -------- | ----- | ------ | ----- | ------------ | --- |
| They |  apply |  Yao’s |  min-max |  theorem[111], |     |  which |           |          |       |        |       |              |     |
probability for some c>0. Since S is fixed, then
asserts that for a specific input distribution, the best (cid:12) (cid:12)
|     |     |     |     |     |     |     |     |     | (cid:12) | (cid:12) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --- | --- | --- |
algorithm for that distribution is deterministic. Thus,   (cid:12) 2S 1+x (cid:12)
|     |     |     |     |     |     |     |     |     | (cid:0) | (cid:12)>2c; |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | --- | --- |
(cid:12)
to  derive  the  required  lower  bound,  it  suffices  to k 2
| examine |  deterministic |     |  algorithms |  and |  evaluate |  the | or equivalently: |     |          |          |     |     |     |
| ------- | -------------- | --- | ----------- | ---- | --------- | ---- | ---------------- | --- | -------- | -------- | --- | --- | --- |
|         |                |     |             |      |           |      |                  |     | (cid:12) | (cid:12) |     |     |     |
expected difference in total utility across the random   (cid:12) (cid:12)
|                                                          |     |     |     |     |     |     |     |     | (cid:12) 4S (cid:0)1(cid:0)x | (cid:12)     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | ------------ | --- | --- | --- |
|                                                          |     |     |     |     |     |     |     |     | (cid:12)                     | (cid:12)>4c: |     |     |     |
| choice of x. For any deterministic algorithm, during the |     |     |     |     |     |     |     |     | k                            |              |     |     |     |
time steps 1; 2; :::; (k=2), the algorithm observes an For any fixed a, if x(cid:24) (0;1), the probability that
uar
income  of  1,  meaning  the  consumption  values ja(cid:0)xj⩽1=3 is at most 2=3. Therefore, the condition
| z; z; | :::; |  are predetermined. Let S=z |     |     | +z  | +(cid:1)(cid:1)(cid:1)+ |                                                      |     |     |     |     |     |     |
| ----- | ---- | --------------------------- | --- | --- | --- | ----------------------- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|       |      | z (k=2)                     |     |     |     |                         | holds with c=1=12 and with a probability of at least |     |     |     |     |     |     |
| 1     | 2    |                             |     |     | 1   | 2                       |                                                      |     |     |     |     |     |     |
z .
| (k=2) |     |     |     |     |     |     | 1=3. |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
Consider the scenario where the following condition
|     |     |     |     |     |     |     | In  summary, |  with |  a  |  probability |  of  | 1=3,  the |  no- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----- | --- | ------------ | ---- | --------- | ---- |
holds:
lookahead algorithm performs Ω(k) worse than the
|     |     |     | (cid:12)   | (cid:12)     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | (cid:12) k | 1+x (cid:12) |     |     |     |     |     |     |     |     |     |
(cid:12) (cid:12)S(cid:0) (cid:1) (cid:12) (cid:12)>c(cid:1)k lookahead  algorithm  and  cannot  achieve  better
(A1)
|     |     |     | 2   | 2   |     |     | performance. Therefore, the expected utility gap is also |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
for some parameter c. In this case, Refs. [109, 110] Ω(k). By applying Yao’s min-max theorem, this lower
p
d√emonstrate  that  (cid:229) z  is  significantly  less  than bound holds for any (potentially randomized) algorithm
|     |     |     | i   | i   |     |     |          |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
|     | 1+x |     |     |     |     |     | as well. |     |     |     |     |     | ■   |
k .
2
|        |     | 1+x                                     |     |     |     |     | C    Modeling Debt and Behavioral Anomaly |     |     |     |     |     |     |
| ------ | --- | --------------------------------------- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- |
| Let a= |     | . From the assumption, it is known that |     |     |     |     |                                           |     |     |     |     |     |     |
2
|     |     |     |     |     |     |     | An  important |  direction |     |  for |  future |  work |  lies  in |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ---------- | --- | ---- | ------- | ----- | --------- |
k
| jz +z | +(cid:1)(cid:1)(cid:1)+z |     | (cid:0) aj>ck, which implies |     |     |     |                                                  |     |     |     |     |     |     |
| ----- | ------------------------ | --- | ---------------------------- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
| 1     | 2                        | k=2 | 2                            |     |     |     | extending our model to incorporate consumer debt |     |     |     |     |     |     |
  (cid:229)jz(cid:0)aj>ck and  behavioral  deviations  from  standard  discounted
(A2)
i
|     |     |     | i⩽k |     |     |     | utility theory, such as hyperbolic discounting. These |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |

  Pegah Nokhiz et al.:   Consumer Autonomy or Illusion? Rethinking Consumer Agency in the Age… 201
features play a central role in real-world consumption are conceptually aligned with our goals and represent
decisions and would enrich the theoretical analysis of
promising avenues for further study.
agency under financial constraint.
D    Additional Experimental Analysis
Debt, particularly in the form of credit cards, Buy
|     |     |     |     |     |     | In  this  section, |     |  using |  our  model, |     |  we  explore |  four |
| --- | --- | --- | --- | --- | --- | ------------------ | --- | ------ | ------------ | --- | ------------ | ----- |
Now Pay Later (BNPL) schemes, and payday loans,
different sets of experiments regarding the algorithmic
serves as a mechanism for smoothing consumption
|     |     |     |     |     |     | persuasion |  and |  ruin, |  behaviors |  of |  different |  income |
| --- | --- | --- | --- | --- | --- | ---------- | ---- | ------ | ---------- | --- | ---------- | ------- |
over time when current income or assets are insufficient.
|               |                |     |          |           |            | classes, |  behaviors |  of |  different |  individuals |     |  based  on |
| ------------- | -------------- | --- | -------- | --------- | ---------- | -------- | ---------- | --- | ---------- | ------------ | --- | ---------- |
| In  classical |  intertemporal |     |  models, |  allowing |  for  debt |          |            |     |            |              |     |            |
education level (to avoid social uniformity and explore
| would  relax |  the |  constraint  |     | ⩽a  | and  introduce |     |     |     |     |     |     |     |
| ------------ | ---- | ------------ | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
c
|           |              |     |     | t                       | t   | more  diverse     |     |  subgroups |  that |  could      |  potentially |  be          |
| --------- | ------------ | --- | --- | ----------------------- | --- | ----------------- | --- | ---------- | ----- | ----------- | ------------ | ------------ |
| borrowing |  constraints |     |     |  or  interest-dependent |     |                   |     |            |       |             |              |              |
|           |              |     |     |                         |     | underprivileged), |     |  and       |  work |  scheduling |              |  effects  on |
repayment obligations. However, this also introduces
financial utility.
| new  risks: |  under |  limited |     |  agency |  (e.g.,  impulsive |     |     |     |     |     |     |     |
| ----------- | ------ | -------- | --- | ------- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
(1) Experimental setup
purchases or unpredictable income), access to debt
We begin by describing the key components of our
can amplify financial fragility, increase the likelihood of
experimental setup.
| ruin,  and |  create |  feedback |     |  loops  where |  short-term |     |     |     |     |     |     |     |
| ---------- | ------- | --------- | --- | ------------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
choices  impose  long-term  burdens.  For  example, Model  of  computation:  Our  experiments  are
manipulated urgency or misleading repayment terms based on the computational framework introduced in
Section 3.1. This model employs value iteration to
| can  cause |  consumers |     |  to  overborrow |     |  without  fully |     |     |     |     |     |     |     |
| ---------- | ---------- | --- | --------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
compute optimal consumption paths, which are then
anticipating the long-run costs.
used in the simulations to determine final consumption
| Behavioral |     |  anomalies, |     |  such |  as  hyperbolic |     |     |     |     |     |     |     |
| ---------- | --- | ----------- | --- | ----- | --------------- | --- | --- | --- | --- | --- | --- | --- |
and asset trajectories. The discounting factor b is set
| discounting[40,  |        | 122],  refer |  to |  empirically |  observed   |          |        |           |     |           |            |     |
| ---------------- | ------ | ------------ | --- | ------------ | ----------- | -------- | ------ | --------- | --- | --------- | ---------- | --- |
|                  |        |              |     |              |             | to  0.95 |  based |  on  what |  is |  commonly |  practiced |  in |
| patterns         |  where |  individuals |     |  heavily     |  overweight |          |        |           |     |           |            |     |
immediate rewards compared to future outcomes, far literature in general settings[114–115].
more than exponential discounting predicts. Formally, Assets and income: The initial asset level is set at
hyperbolic discounting modifies the temporal weight 141 140 US dollars, corresponding to the median net
worth reported by the Federal Reserve in 2019[112].
on future utility such that the discount factor becomes
|     |     |     |     |     |     | Monthly |  income |  is |  drawn |  from |  a  |  log-normal |
| --- | --- | --- | --- | --- | --- | ------- | ------- | --- | ------ | ----- | --- | ----------- |
time-inconsistent: individuals may plan to save in the
distribution with a mean of 5957.25 US dollars and a
| future  but |  fail |  to  follow |  through |     |  when  the  future |     |     |     |     |     |     |     |
| ----------- | ----- | ----------- | -------- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
standard deviation of 378.74 US dollars, derived from
becomes the present. This deviation leads to dynamic
inconsistency,  myopic  spending,  and  a  stronger annual income statistics provided by the U.S. Bureau of
susceptibility to manipulative design features like flash Labor Statistics for 2019[113].
sales, scarcity cues, or short-term promotions. In the To  explore  the  impact  of  income  level,  we  also
presence  of  algorithmic  persuasion,  hyperbolic simulate  both  low-  and  high-income  scenarios  in
|     |     |     |     |     |     | Section |  (3)  in |  the  Appendix |     |  D. |  We  consider |  the |
| --- | --- | --- | --- | --- | --- | ------- | -------- | -------------- | --- | --- | ------------- | ---- |
discounting can exacerbate consumer vulnerability by
individuals with income in the range from 1250 US
aligning system-level nudges with consumers’ inherent
|     |     |     |     |     |     | dollars |  to  2500 |  US |  dollars |  as |  the |  low-income |
| --- | --- | --- | --- | --- | --- | ------- | --------- | --- | -------- | --- | ---- | ----------- |
present bias.
While  both  debt  modeling  and  hyperbolic individuals and the individuals with income in the range
discounting  are  highly  relevant  to  the  broader from 8334 US dollars to 12 500 US dollars as the high-
discourse  on  consumption  agency,  we  deliberately income individuals[113]. The low-income group receives
chose not to include them in our current formalism income from a distribution with a mean of 1899.33 US
for  tractability  and  interpretability.  Our  primary dollars and standard deviation of 77 US dollars, while
objective  was  to  isolate  and  analyze  the  structural the high-income group’s distribution has a mean of
|     |     |     |     |     |     | 8869.92 |  US |  dollars |  and |  standard |  deviation |  of |
| --- | --- | --- | --- | --- | --- | ------- | --- | -------- | ---- | --------- | ---------- | --- |
impact of limited agency (particularly under algorithmic
and  systemic  constraints)  within  a  clean,  utility- 199.60 US dollars[113].
maximizing framework. Including debt dynamics or non- Simulation  setup  and  plots:  Each  experiment
standard temporal discounting would add additional simulates 50 000 agents, with each agent planning over
modeling  complexity;  nonetheless,  these  extensions a 100-month horizon. The point of ruin is defined as

    202 Journal of Social Computing, September 2025, 6(3): 184−208
the first month in which an agent’s asset level falls agents  manage  to  maintain  solvency.  Nonetheless,
under the standard setup, a subset of agents is able to
| below  zero. |  From |     |  these |  simulations, |     |  we  generate |     |     |     |     |     |     |     |     |
| ------------ | ----- | --- | ------ | ------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
histograms representing the distribution of ruin times delay ruin significantly, with some surviving until the
| across agents. |     |     |     |     |     |     |     | end of the planning horizon. |     |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
(2)  Algorithmic  persuasion,  impulsive (3) Diverse subgroups: Low-income vs. high-
| consumption, and ruin |     |     |     |     |     |     |     | income |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
In this experiment, we investigate how algorithmic In  this  experiment,  we  examine  how  income
persuasion  and  impulsive  consumption,  under influences  the  likelihood  of  financial  ruin.  The
motivation is to consider analyzing varied demographic
| minimum |  subsistence |     |  conditions, |     |  contribute |     |  to |     |     |     |     |     |     |     |
| ------- | ------------ | --- | ------------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
segments and striving to prevent assumptions of social
financial ruin. The model and experimental parameters
homogeneity.
follow the standard configuration detailed in Section (1)
|                   |     |     |       |               |     |               |     | We  consider      |     |  agents      |  with |  low-income  |  and |  agents       |
| ----------------- | --- | --- | ----- | ------------- | --- | ------------- | --- | ----------------- | --- | ------------ | ----- | ------------ | ---- | ------------- |
| in  the  Appendix |     |  D  |  with |  the  general |     |  income/asset |     |                   |     |              |       |              |      |               |
|                   |     |     |       |               |     |               |     | with  high-income |     |  as  defined |       |  in  Section |      |  (1)  in  the |
setting for the entire underlying population with no
Appendix D. For these income-specific scenarios, the
| income |  classes |  defined |  yet. |  The |  mean |  expenditure |     |     |     |     |     |     |     |     |
| ------ | -------- | -------- | ----- | ---- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
value  is  5253  US  dollars  per  month  based  on  the mean expenditure is 2850 US dollars for the low-
income group and 7082.83 US dollars for the high-
| statistics |  provided |  by |  the |  U.S. |  Bureau |  of |  Labor |     |     |     |     |     |     |     |
| ---------- | --------- | --- | ---- | ----- | ------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
income group, following the same 2019 statistics[113].
| Statistics   |  for |  2019[113].  |        | Figure |  A1  | presents     |  the |                 |     |               |     |              |      |          |
| ------------ | ---- | ------------ | ------ | ------ | ---- | ------------ | ---- | --------------- | --- | ------------- | --- | ------------ | ---- | -------- |
|              |      |              |        |        |      |              |      | Other  settings |     |  are  similar |     |  to  Section |  (1) |  in  the |
| distribution |  of  |  ruin        |  times |  for   |  the |  algorithmic |      |                 |     |               |     |              |      |          |
Appendix D.
persuasion and impulsive consumption scenario.
Our computational behavioral model incorporates a
Analysis: Figure A1 illustrates that agents operating
discount factor b, which represents the consumer’s
| under  minimum |     |  subsistence |     |  constraints |     |  tend |  to |           |            |        |     |          |            |       |
| -------------- | --- | ------------ | --- | ------------ | --- | ----- | --- | --------- | ---------- | ------ | --- | -------- | ---------- | ----- |
|                |     |              |     |              |     |       |     | level  of |  patience. |  While |  in |  general |  settings, |  more |
experience ruin within a short number of time steps.
commonly used values like 0.95 can be used[114–115],
A significant fraction of agents reach ruin within the
|           |         |               |     |                  |     |            |     | this  parameter |     |  has  been |  studied |     |  in  more |  depth. |
| --------- | ------- | ------------- | --- | ---------------- | --- | ---------- | --- | --------------- | --- | ---------- | -------- | --- | --------- | ------- |
| first  10 |  steps, |  highlighting |     |  the  heightened |     |  financial |     |                 |     |            |          |     |           |         |
Findings suggest that b can vary with income level. Thus,
vulnerability caused by impulsive consumption in such
|     |     |     |     |     |     |     |     | for  individuals |     |  with  a |  low  income |     |  we  set |  a  lower |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | -------- | ------------ | --- | -------- | --------- |
conditions. This rapid onset of ruin underscores the
discount factor (around b=0:5), whereas those with a
| short-term |  instability |     |  faced |  by |  these |  agents. |  The |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | ------ | --- | ------ | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
high income we set a higher discount factor (around
| frequency |  of |  ruin |  decreases |  steeply |     |  over |  time, |     |     |     |     |     |     |     |
| --------- | --- | ----- | ---------- | -------- | --- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
b=0:9) per prior research on b for these income
| indicating |  that |  as  the |  simulation |     |  progresses, |     |  fewer |     |     |     |     |     |     |     |
| ---------- | ----- | -------- | ----------- | --- | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
classes[116]. In Fig. A2, we provide the distributions of
|   20 000 |     |     |     |     |     |     |     | the ruin times for the low-income and high-income |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| 17 500   |     |     |     |     |     |     |     | individuals.                                      |     |     |     |     |     |     |
stnega fo rebmuN 15 000 Analysis: Figure A2 illustrates the distribution of
|     |     |     |     |     |     |     |     | ruin  times |  under |  impulsive |     |  consumption |     |  for  agents |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ---------- | --- | ------------ | --- | ------------ |
12 500
with low- and high-income levels. In the low-income
10 000
|     |     |     |     |     |     |     |     | scenario, |  nearly |  all  | 50  000  | agents |  go |  to  ruin |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ----- | -------- | ------ | --- | --------- |
7500
immediately within the first time step. The histogram
5000
|     |     |     |     |     |     |     |     | is  sharply |  concentrated |     |  at |  the |  origin |  with  no |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------- | --- | --- | ---- | ------- | --------- |
2500
|     |     |     |     |     |     |     |     | meaningful |  tail, |  indicating |  extreme |     |  financial |  fragility. |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ----------- | -------- | --- | ---------- | ----------- |
0 20 40 60 80 100 This  suggests  that  under  low-income  and  impulsive
|     |     |     | Time step (month) |     |     |     |     |           |         |      |            |     |             |       |
| --- | --- | --- | ----------------- | --- | --- | --- | --- | --------- | ------- | ---- | ---------- | --- | ----------- | ----- |
|     |     |     |                   |     |     |     |     | behavior, |  agents |  are |  incapable |  of |  sustaining |  even |
Fig. A1    Distribution of ruin times under algorithmic
|            |      |     |            |               |     |     |      | minimal |  subsistence, |  leading |     |  to  near-instantaneous |     |     |
| ---------- | ---- | --- | ---------- | ------------- | --- | --- | ---- | ------- | ------------- | -------- | --- | ----------------------- | --- | --- |
| persuasion |  and |     |  impulsive |  consumption. |     |     |  The |         |               |          |     |                         |     |     |
collapse.
experiment simulates 50 000 agents, and the resulting
|              |           |             |            |          |        |       |        | In  contrast, |        |  while  many |  high-income |               |  agents |  also  |
| ------------ | --------- | ----------- | ---------- | -------- | ------ | ----- | ------ | ------------- | ------ | ------------ | ------------ | ------------- | ------- | ------ |
| distribution |  reflects |             |  the  time |  at      |  which |  each |  agent |               |        |              |              |               |         |        |
|              |           |             |            |          |        |       |        | experience    |  early |  ruin,       |  the         |  distribution |         |  shows |
| experiences  |  ruin.    |  The x-axis |            |  denotes |  the   |  time |  step  |               |        |              |              |               |         |        |
(month) when ruin occurs, while the y-axis indicates noticeably more spread, with a non-trivial number of
the number of agents who go to ruin at each time step. agents surviving for longer durations. This reflects the

  Pegah Nokhiz et al.:   Consumer Autonomy or Illusion? Rethinking Consumer Agency in the Age… 203
|     |     |     |     |     |     |     |     | Once again, the discount factor b has been studied |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- |
40 000
in the prior literature, and findings suggest that b may
35 000
vary with education. In particular, individuals with a
stnega fo rebmuN
30 000
|     |     |     |     |     |     |     |     | high |  school |  education |  typically |  exhibit |  a  lower |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------- | ---------- | ---------- | -------- | --------- |
25 000
discount factor (around b=0:5), whereas those with a
20 000
college degree tend to have a higher value (around
15 000
b=0:83)[116]. As shown in prior research[110], people
10 000
with higher education tend to have higher income,
5000
more financial flexibility, and a resultant financial utility,
|     | 0   |     | 20  | 40  | 60  | 80  | 100 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
which indicates that the lower-education group is the
Time step (month)
|     |     |     | (a) High-income |     |     |     |     | underprivileged group in this setting. |             |        |              |     |               |
| --- | --- | --- | --------------- | --- | --- | --- | --- | -------------------------------------- | ----------- | ------ | ------------ | --- | ------------- |
|     |     |     |                 |     |     |     |     | The                                    |  experiment |  setup |  is  similar |  to |  the  general |
50 000
setting in Section (1) in the Appendix D. In Fig. A3, we
provide the distributions of the ruin times for college
40 000
stnega fo rebmuN
degree holders and high-school diploma holders.
| 30 000 |     |     |     |     |     |     |     | Analysis: Figure A3 illustrates the distribution of |        |            |              |     |              |
| ------ | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | ------ | ---------- | ------------ | --- | ------------ |
|        |     |     |     |     |     |     |     | ruin  times                                         |  under |  impulsive |  consumption |     |  for  agents |
20 000
  35 000
10 000
30 000
stnega fo rebmuN
25 000
|     | 0   |     | 20  | 40  | 60  | 80  | 100 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Time step (month)
20 000
(b) Low-income

15 000
| Fig. A2    Distribution                               |     |           |  of  ruin    |  times   |              |  for  low-income |        |        |      |     |     |     |        |
| ----------------------------------------------------- | --- | --------- | ------------ | -------- | ------------ | ---------------- | ------ | ------ | ---- | --- | --- | --- | ------ |
| households                                            |     |  and      |  high-income |          |  households. |                  |  The   | 10 000 |      |     |     |     |        |
| experiment simulates 50 000 agents, and the resulting |     |           |              |          |              |                  |        |        | 5000 |     |     |     |        |
| distribution                                          |     |  reflects |  the         |  time    |  at  which   |  each            |  agent |        |      |     |     |     |        |
| experiences                                           |     |  ruin.    |  The x-axis  |  denotes |              |  the  time       |  step  |        |      |     |     |     |        |
|                                                       |     |           |              |          |              |                  |        |        | 0    | 20  | 40  | 60  | 80 100 |
(month) when ruin occurs, while the y-axis indicates Time step (month)
the number of agents who go to ruin at each time step. (a) College degree

| buffering                                          |  effect |  of |  higher |  income: |  though |     |  impulsive | 35 000 |     |     |     |     |     |
| -------------------------------------------------- | ------- | --- | ------- | -------- | ------- | --- | ---------- | ------ | --- | --- | --- | --- | --- |
| consumption still leads most high-income agents to |         |     |         |          |         |     |            | 30 000 |     |     |     |     |     |
stnega fo rebmuN
| financial |  ruin |  relatively |     |  quickly, |  greater |     |  income | 25 000 |     |     |     |     |     |
| --------- | ----- | ----------- | --- | --------- | -------- | --- | ------- | ------ | --- | --- | --- | --- | --- |
provides some capacity to delay collapse. Overall, the
20 000
results highlight that income level influences time to ruin.
15 000
| Low-income |     |  agents |  exhibit |  much |     |  lower |  financial |     |     |     |     |     |     |
| ---------- | --- | ------- | -------- | ----- | --- | ------ | ---------- | --- | --- | --- | --- | --- | --- |
10 000
resilience, while high-income agents display a modest
| degree of resilience. |     |     |     |     |     |     |     |     | 5000 |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
(4) Diverse subgroups: High school vs. college
|           |                    |     |     |          |     |          |          |     | 0   | 20  | 40                      | 60  | 80 100 |
| --------- | ------------------ | --- | --- | -------- | --- | -------- | -------- | --- | --- | --- | ----------------------- | --- | ------ |
| graduates |                    |     |     |          |     |          |          |     |     |     | Time step (month)       |     |        |
|           |                    |     |     |          |     |          |          |     |     |     | (b) High-school diploma |     |        |
| In        |  this  experiment, |     |  we |  examine |     |  another |  set  of |     |     |     |                         |     |        |
Fig. A3    Distribution of ruin times for college degree
| experiments |     |  to |  explore |  the |  effects |  of |  impulsive |     |     |     |     |     |     |
| ----------- | --- | --- | -------- | ---- | -------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
consumption for different subgroups. Specifically, we holders  and  high-school  diploma  holders.  The
experiment simulates 50 000 agents, and the resulting
| analyze   |  how   |  educational |      |  attainment |     |  affects  |  financial |              |           |             |           |        |                  |
| --------- | ------ | ------------ | ---- | ----------- | --- | --------- | ---------- | ------------ | --------- | ----------- | --------- | ------ | ---------------- |
|           |        |              |      |             |     |           |            | distribution |  reflects |  the        |  time  at |  which |  each  agent     |
| stability |  based |  on          |  the |  effects    |  it |  has  on  | b  in      |              |           |             |           |        |                  |
|           |        |              |      |             |     |           |            | experiences  |  ruin.    |  The x-axis |  denotes  |        |  the  time  step |
consumption decisions (and how these differences can (month) when ruin occurs, while the y-axis indicates
lead agents to experience ruin). the number of agents who go to ruin at each time step.
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

204 Journal of Social Computing, September 2025, 6(3): 184−208
with high-school diploma and college degree. In the References
high school diploma scenario, nearly all 50 000 agents
[1] S. Gordon-Wilson and D. Godefroit-Winkel, Consumer
go to ruin very quickly within the first 20 time steps.
agency in sustainable consumption behaviour and
The histogram indicates financial fragility. This suggests
environmentally imposed constraints: A multi-level
that underprivileged groups (here with lower b in the approach, Bus. Strategy Environ., vol. 33, no. 8, pp.
impulsive case) are incapable of efficiently sustaining 7942–7959, 2024.
[2] A. Rubel, C. Castro, and A. Pham, Algorithms, agency,
themselves, leading to sudden collapse.
and respect for persons, Soc. Theory Pract., vol. 46, no. 3,
In contrast, while many college degree-holding
pp. 547–572, 2020.
agents also experience early ruin, the distribution [3] B. C. Cheong, Transparency and accountability in AI
systems: Safeguarding wellbeing in the age of algorithmic
shows significant spread, with a significant number of
decision-making, Front. Hum. Dyn., vol. 6, p. 1421273,
agents surviving for longer durations. This reflects the
2024.
differences that consumption bounds could potentially [4] E. Pariser, The Filter Bubble: How the New Personalized
Web is Changing What We Read and How We Think. New
have on diverse education level subgroups.
York, NY, USA: Penguin Books, 2011.
Overall, the results highlight that various factors
[5] A. Mathur, G. Acar, M. J. Friedman, E. Lucherini, J.
representing different subpopulations (like b here for Mayer, M. Chetty, and A. Narayanan, Dark patterns at
group differentiation to avoid social uniformity) can scale, Proc. ACM Hum. Comput. Interact., vol. 3, pp. 1–32,
2019.
impact time to ruin.
[6] M. V. Ploeg, Access to affordable, nutritious food is
(5) Work schedule instability analysis limited in “food deserts”, https://www.ers.usda.
Prior works[109, 110] show both empirically and gov/amber-waves/2010/march/access-to-affordable-
formally that underprivileged workers (particularly nutritious-food-is-limited-in-food-deserts, 2010.
[7] T. EMB, The rise of subscription-based business models,
those with limited foresight into their future schedules)
https://blog.emb.global/subscription-based-business-
experience significantly lower financial utility compared model/, 2024.
[8] C. Bercu, Monetization and engagement in freemium
to those with greater lookahead. The ability to
games, PhD dissertation, IT University of Copenhagen,
anticipate upcoming work hours allows individuals to
Copenhagen, Denmark, 2016.
better plan consumption and savings, ultimately [9] R. H. Kerschbaumer, T. Foscht, and A. B. Eisingerich,
resulting in higher utility. Additionally, the effect of Smart services and the rise of access-based subscription
models, in Smart Services, M. Bruhn and K. Hadwich, eds.
income is straightforward: higher earnings allow
Wiesbaden, Germany: Springer Fachmedien Wiesbaden,
individuals to meet consumption needs more
2022, pp. 179–205.
comfortably due to their higher utility scale across all [10] T. Inaba, Evaluation of subscription-based sales of IoT-
enabled consumer devices, in Proc. IEEE Int. Conf.
lookahead conditions. Moreover, disadvantaged groups
Industrial Engineering and Engineering Management (IEEM),
holding more rapidly depreciating assets have an even
Kuala Lumpur, Malaysia, 2022, pp. 1206–1210.
greater need for advance information about their [11] J. Johnen and R. Somogyi, Deceptive features on
work schedules, given their already vulnerable financial platforms, Econ. J., vol. 134, no. 662, pp. 2470–2493,
2024.
standing.
[12] M. Kenney and J. Zysman, The rise of the platform
These studies also reveal that employees who are economy, Issues in Science and Technology, vol. 32, no. 3,
given advanced notice of schedule changes based on p. 61, 2016.
[13] L. Subramaniam, C. S. Yap, F. W. Jalaludin, and K. W.
regulations like the Schedules that Work Act of 2014
Hen, Digital divide and university students’ online
(H.R. 5159) and Retail Workers Bill of Rights in San
learning amidst COVID-19 pandemic in Malaysia, Libri,
Francisco[96] experience improved financial well-being.
vol. 74, no. 2, pp. 197–210, 2024.
Advanced planning allows workers with variable [14] M. Sun, L. Xiong, L. Li, Y. Chen, J. Tang, W. Hua, and Y.
schedules to gain greater autonomy over their financial Mao, Digital divide in online education during the
COVID-19 pandemic: A cosmetic course from the view
planning. That is, they can manage their consumption
of the regional socioeconomic distribution, Front. Public
and savings more effectively, which leads to better
Health, vol. 9, p. 796210, 2022.
financial decision-making and agency. [15] M. T. P. Heath and A. Chatzidakis, ‘Blame it on
marketing’: Consumers’ views on unsustainable
Conflict of Interest consumption, Int. J. Consum. Stud., vol. 36, no. 6, pp.
656–667, 2012.
The authors declare no conflict of interest. [16] R. I. Rodrigues, P. Lopes, and M. Varela, Factors affecting

  Pegah Nokhiz et al.:   Consumer Autonomy or Illusion? Rethinking Consumer Agency in the Age… 205
impulse buying behavior of consumers, Front. Psychol., vol. [31] D. Farrell and F. Greig, Paychecks, paydays, and the

12, p. 697080, 2021. online platform economy, in Proc. Annual Conference on
[17] R. H. Thaler, Mental accounting matters, J. Behav. Decis. Taxation and Minutes of the Annual Meeting of the National

Making, vol. 12, no. 3, pp. 183–206, 1999.
Tax Association, Washington, DC, USA, 2016, pp. 1–40.
[18] J. Chen, Y. Zhang, and Z. Liu, Unlocking the power of J. Larrimore, A. Durante, C. Park, and A. Tranfaglia,
|             |     |                   |              |     | [32] |     |     |     |     |
| ----------- | --- | ----------------- | ------------ | --- | ---- | --- | --- | --- | --- |
| algorithmic |     |  recommendations: |  The  effect |  of |      |     |     |     |     |
Report on the economic well-being of US households in
recommendation characteristics on users’ willingness to 2015,  https://www.federalreserve.gov/publications/files/
| value |  co-creation,  | Curr.  Psychol., |  vol.  44,  no.  | 3,  pp. |     |     |     |     |     |
| ----- | -------------- | ---------------- | ---------------- | ------- | --- | --- | --- | --- | --- |
2016-report-economic-well-being-us-households-2017
1492–1510, 2025.
05.pdf, 2016.
| [19] X. |  Li,  How |  do  algorithmic |  recommendations |  lead |     |     |     |     |     |
| ------- | --------- | ---------------- | ---------------- | ----- | --- | --- | --- | --- | --- |
[33] D. Schneider and K. Harknett, Income volatility in the
|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
consumers to make online purchases? https://www.hec. service  sector:  Contours,  causes,  and  consequences,
edu/en/how-do-algorithmic-recommendations-lead- https://appam.confex.com/appam/2017/webprogram/Paper
consumers-make-online-purchases, 2022.
22205.html, 2017.
[20] N. Oberoi, How can limited-time discounts (such as flash
[34] J. Kantor, Working anything but 9 to 5, https://www.
|   sales and limited-time offers) affect the urgency and |     |     |     |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
nytimes.com/interactive/2014/08/13/us, 2014.
impulsive  buying  behavior  of  consumers?  EPH- [35] A. Lancaster, The pros and cons of scheduling software,

International Journal of Business & Management Science, https://www.restaurantbusinessonline.com/technology/
doi: 10.53555/eijbms.v10i1.172. pros-cons-scheduling-software, 2015.
[21] J. Valentine, The psychology of scarcity: Using limited- [36] K. Griesbach, A. Reich, L. Elliott-Negri, and R. Milkman,
|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
time offers and exclusive deals to drive conversions, Algorithmic  control  in  platform  food  delivery  work,
https://medium.com/@johnvalentinemedia/the- Socius, vol. 5, p. 2378023119870041, 2019.
psychology-of-scarcity-marketing-how-fomo-drives- [37] A.  Zhang,  A.  Boltz,  C.  W.  Wang,  and  M.  K.  Lee,

Algorithmic management reimagined for workers and by
conversions-c5594d129bfd, 2024.
[22] J. Runge, J. Levav, and H. S. Nair, Price promotions and workers: Centering worker well-being in gig work, in

“freemium” app monetization, Quant. Mark. Econ., vol. Proc. CHI Conf. Human Factors in Computing Systems, New
20, no. 2, pp. 101–139, 2022. Orleans, LA, USA, 2022, pp. 1–20.
[23] N. Mishra, S. Najafi, S. Najafi Asadolahi, and A. Tsay, [38] K. Loggins, Here’s what happens when an algorithm
|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
How  freemium  gets  consumers  to  pay  a  premium: determines your work schedule, https://www.vice.com/
The role of loss-aversion, https://doi.org/10.2139/ssrn. en/article/heres-what-happens-when-an-algorithm-
| 2961548, 2017. |     |     |     |     | determines-your-work-schedule/, 2020. |     |     |     |     |
| -------------- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- |
[24] M. Y. T. Gwee and K. T. T. Chang, Effects of persuasive [39] C. Nguyen, Value capture, J. Ethics Soc. Philos., vol. 27, no.

| claims on desirability and impulse purchase behavior, |     |     |     |     |   3, p. 469, 2024. |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- |
[40] S. Frederick, G. Loewenstein, and T. O’donoghue, Time
https://www.researchgate.net/publication/287362362_

Effects_of_persuasive_claims_on_desirability_and_ discounting and time preference: A critical review, J.
impulse_purchase_behavior, 2021. Econ. Lit., vol. 40, no. 2, pp. 351–401, 2002.
[25] S. Mishra and R. Ashfaq, Influencer impact: Examining the [41] A.  Deaton,  Understanding  Consumption.  Oxford,  UK:

|     |     |     |     |     | Oxford University Press, 1992. |     |     |     |     |
| --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- |
effect of influencers on consumer behavior and purchase,
[42] A. Deaton, Saving and liquidity constraints, Tech. rep.,
| Traditional Journal of Multidisciplinary Sciences, vol. 1, no. 1, |     |     |     |     |     |     |     |     |     |
| ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
National Bureau of Economic Research, New York, NY,
pp. 55–72, 2023.
| [26] X. Zheng, J. Men, F. Yang, and X. Gong, Understanding |     |     |     |     | USA, 1989. |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
  [43] C.  F.  Chabris,  D.  I.  Laibson,  and  J.  P.  Schuldt,
| impulse buying in mobile commerce: An investigation |     |     |     |     |               |          |                  |                    |     |
| --------------------------------------------------- | --- | --- | --- | --- | ------------- | -------- | ---------------- | ------------------ | --- |
|                                                     |     |     |     |     | Intertemporal |  choice, |  in  Behavioural |  and  Experimental |     |
into hedonic and utilitarian browsing, International Journal
Economics, S. N. Durlauf and L. E. Blume, eds. London,
of Information Management, vol. 48, pp. 151–160, 2019.
[27] D. Schneider and K. Harknett, It’s about time: How UK: Palgrave Macmillan UK, 2010, pp. 168–177.
  work schedule instability matters for workers, families, [44] P. A. Samuelson, A note on measurement of utility, Rev.

Econ. Stud., vol. 4, no. 2, pp. 155–161, 1937.
| and |  racial  inequality, |  https://shift.hks.harvard.edu/files/ |     |     |     |     |     |     |     |
| --- | -------------------- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
[45] M. Friedman, The permanent income hypothesis, in A
| 2019/10/Its-About-Time-How-Work-Schedule-Instability- |     |     |     |     |            |                   |            |                |      |
| ----------------------------------------------------- | --- | --- | --- | --- | ---------- | ----------------- | ---------- | -------------- | ---- |
|                                                       |     |     |     |     | Theory  of |  the  Consumption |  Function, |  M.  Friedman, |  ed. |
Matters-for-Workers-Families-and-Racial-Inequality.pdf, Princeton, NJ, USA: Princeton University Press, 1957,
2019.
pp. 20–37.
[28] E. D. McCrate, Unstable and on-call work schedules in
  [46] M.  Friedman,  A  Theory  of  the  Consumption  Function.
| the |  United  States |  and  Canada, |  https://www.ilo.org/ |     |     |     |     |     |     |
| --- | --------------- | ------------- | --------------------- | --- | --- | --- | --- | --- | --- |
Princeton, NJ, USA: Princeton University Press, 2018.
publications/unstable-and-call-work-schedules-united-
|     |     |     |     |     | [47] M.  Bütler,  | Neoclassical |  life-cycle |  consumption: |  A  |
| --- | --- | --- | --- | --- | ----------------- | ------------ | ----------- | ------------- | --- |

states-and-canada, 2018. textbook  example,  Econ.  Theory,  vol.  17,  no.  1,  pp.
[29] A. Hannagan and J. Morduch, Income gains and month-
|     |     |     |     |     | 209–221, 2001. |     |     |     |     |
| --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- |
to-month income volatility: Household evidence from Q.  Ma,  J.  Stachurski,  and  A.  A.  Toda,  The  income
[48]
| the |  US  financial |  diaries, |  https://doi.org/10.2139/ssrn. |     |     |     |     |     |     |
| --- | -------------- | --------- | ------------------------------ | --- | --- | --- | --- | --- | --- |
fluctuation problem and the evolution of wealth, J. Econ.
| 2659883, 2015. |     |     |     |     | Theory, vol. 187, p. 105003, 2020. |     |     |     |     |
| -------------- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- |
[30] J. Morduch and J. Siwicki, In and out of poverty: Episodic [49] T. Sargent and J. Stachurski, Quantitative economics,
|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
poverty and income volatility in the US financial diaries, Tech. rep., Citeseer, 2014.
Soc. Serv. Rev., vol. 91, no. 3, pp. 390–421, 2017. [50] W.  J.  Den  Haan,  Comparison  of  solutions  to  the
|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

206 Journal of Social Computing, September 2025, 6(3): 184−208
incomplete markets model with aggregate uncertainty, J. ecommerce-gamification, 2024.
Econ. Dyn. Contr., vol. 34, no. 1, pp. 4–27, 2010. [68] S. Allen, Social media’s growing impact on our lives,
[51] M. Kuhn, Recursive equilibria in an Aiyagari-style https://www.apa.org/members/content/social-media-
economy with permanent income shocks, Int. Econ. Rev., research, 2019.
vol. 54, no. 3, pp. 807–835, 2013. [69] K. Singh, How subscription-based platforms
[52] G. Rabault, When do borrowing constraints bind? Some revolutionized microtransactions, https://globalindian
new results on the income fluctuation problem, J. Econ. network.com/subscription-based-platforms-revolutionised-
Dyn. Contr., vol. 26, no. 2, pp. 217–245, 2002. microtransactions/, 2024.
[53] M. Reiter, Solving heterogeneous-agent models by [70] Y. L. Wu and Y. S. Ye, Understanding impulsive buying
projection and perturbation, J. Econ. Dyn. Contr., vol. 33, behavior in mobile commerce, https://core.ac.uk/
no. 3, pp. 649–665, 2009. download/pdf/301359586.pdf, 2013.
[54] J. Schechtman and V. L. S. Escudero, Some results on “an [71] Y. Wang, J. Pan, Y. Xu, J. Luo, and Y. Wu, The
income fluctuation problem”, J. Econ. Theory, vol. 16, no. determinants of impulsive buying behavior in electronic
2, pp. 151–166, 1977. commerce, Sustainability, vol. 14, no. 12, pp. 1–18, 2022.
[55] M. Wu, W. Liu, Y. Wang, and M. Yao, Negotiating the [72] P. Ferreira, Micropayments vs. subscriptions: Decoding
shared agency between humans & AI in the the currency of convenience, https://www.finance
recommender system, arXiv preprint arXiv: 2403.15919, magnates.com/fintech/micropayments-vs-subscriptions-
2024 decoding-the-currency-of-convenience/, 2023.
[56] K. Hosanagar and D. Lee, AI in personalized product [73] P. Chaudhary and R. O. DaSouza, Consumer readiness
recommendations, Manag. Bus. Rev., vol. 3, nos. 1&2, pp. for microtransactions in digital content business models,
24–28, 2023. Businesses, vol. 4, no. 3, pp. 473–490, 2024.
[57] J. M. Álvarez, A. Colmenarejo, A. Elobaid, S. Fabbrizzi, M. [74] H. Schmidli, On minimizing the ruin probability by
Fahimi, A. Ferrara, S. Ghodsi, C. Mougan, I. investment and reinsurance, Ann. Appl. Probab., vol. 12,
Papageorgiou, P. R. Lobo, et al., Policy advice and best no. 3, pp. 890–907, 2002.
[75] S. Asmussen and H. Albrecher, Ruin Probabilities.
practices on bias and fairness in AI, Ethics Inf Technol, vol.
Singapore: World Scientific, 2010.
26, p. 31, 2024.
[76] R. Abebe, J. Kleinberg, and S. M. Weinberg, Subsidy
[58] LogRocket, Best practices for designing ethical AI user
allocations in the presence of income shocks, Proc. AAAI
interfaces, https://blog.logrocket.com/ux-design/best-
Conf. Artif. Intell., vol. 34, no. 5, pp. 7032–7039, 2020.
practices-designing-ethical-ai-user-interfaces/, 2023.
[77] M. Papachristou and J. Kleinberg, Allocating stimulus
[59] P. Brey and B. Dainow, Ethics by design for artificial
checks in times of crisis, in Proc. ACM Web Conf. 2022,
intelligence, AI and Ethics, vol. 4, no. 4, pp. 1265–1277,
Virtual Event, 2022, pp. 16–26.
2024.
[78] I. Karatzas, J. P. Lehoczky, S. P. Sethi, and S. E. Shreve,
[60] S. Shao, Antitrust in the consumer platform economy:
Explicit solution of a general consumption/investment
How Apple has abused its mobile platform dominance,
problem, Math. Oper. Res., vol. 11, no. 2, pp. 261–294,
https://doi.org/10.2139/ssrn.3603682, 2020.
1986.
[61] D. Geradin and D. Katsifis, The antitrust case against the
[79] E. Bayraktar and V. R. Young, Maximizing utility of
apple app store, J. Compet. Law Econ., vol. 17, no. 3, pp.
consumption subject to a constraint on the probability of
503–585, 2021.
lifetime ruin, Finance Res. Lett., vol. 5, no. 4, pp. 204–212,
[62] A. Haleem, M. Javaid, R. P. Singh, and R. Suman,
2008.
Telemedicine for healthcare: Capabilities, features,
[80] P. Grandits, An optimal consumption problem in finite
barriers, and applications, Sens. Int., vol. 2, p. 100117,
time with a constraint on the ruin probability, Finance
2021.
Stoch., vol. 19, no. 4, pp. 791–847, 2015.
[63] P. A. Anawade, D. Sharma, and S. Gahane, A
[81] X. Zhang and M. Liu, Fairness in learning-based
comprehensive review on exploring the impact of
sequential decision algorithms: A survey, arXiv preprint
telemedicine on healthcare accessibility, Cureus, vol. 16,
arXiv: 2001.04861, 2020.
no. 3, p. e55996, 2024. [82] F. J. Zimmerman and M. R. Carter, Asset smoothing,
[64] L. Harris and L. Zhu, What hides in the shadows:
consumption smoothing and the reproduction of
Deceptive design of dark practices, https://www.congress.
inequality under risk and subsistence constraints, J. Dev.
gov/crs-product/IF12246, 2022.
Econ., vol. 71, no. 2, pp. 233–260, 2003.
[65] Federal Trade Commission, FTC report shows rise in
[83] M. J. Álvarez-Peláez and A. Díaz, Minimum consumption
sophisticated dark patterns designed to trick and trap
and transitional dynamics in wealth distribution, J. Monet.
consumers, https://www.ftc.gov/news-events/news/press-
Econ., vol. 52, no. 3, pp. 633–667, 2005.
releases/2022/09/ftc-report-shows-rise-sophisticated- [84] Y. H. Shin and B. H. Lim, Comparison of optimal
dark-patterns-designed-trick-trap-consumers, 2023. portfolios with and without subsistence consumption
[66] Y. K. Chou, The Octalysis framework for gamification & constraints, Nonlinear Anal. Theory Meth. Appl., vol. 74, no.
behavioral design, https://yukaichou.com/gamification- 1, pp. 50–58, 2011.
examples/octalysis-complete-gamification-framework/, [85] G. Shim and Y. H. Shin, Portfolio selection with
2024. subsistence consumption constraints and CARA utility,
[67] Scavify, What is Ecommerce Gamification? 15 Genius Math. Probl. Eng., vol. 2014, no. 1, p. 153793, 2014.
Strategies in 2024, https://www.scavify.com/gamification/ [86] J. Antony and T. Klarl, Non-renewable resources,

  Pegah Nokhiz et al.:   Consumer Autonomy or Illusion? Rethinking Consumer Agency in the Age… 207
subsistence  consumption,  and  Hartwick’s  investment Singapore, 2024, pp. 43–56.
[102] L. Ljungqvist and T. J. Sargent, Recursive Macroeconomic
rule, Resour. Energy Econ., vol. 55, pp. 124–142, 2019.

[87] C. Dwork and C. Ilvento, Fairness under composition, Theory. Cambridge, MA, USA: MIT Press, 2018.

arXiv preprint arXiv: 1806.06122, 2018. [103] P. P. Wakker, Explaining the characteristics of the power

[88] J. Miranda-Pinto, D. Murphy, K. J. Walsh, and E. R. (CRRA) utility family, Health Econ., vol. 17, no. 12, pp.

|     | Young,  | Saving |  constraints, |  inequality, |  and |  the  credit |     | 1329–1344, 2008. |     |     |     |     |     |
| --- | ------- | ------ | ------------- | ------------ | ---- | ------------ | --- | ---------------- | --- | --- | --- | --- | --- |
[104] T. O’Donoghue and J. Somerville, Modeling risk aversion
market response to fiscal stimulus, Eur. Econ. Rev., vol.
  in economics, J. Econ. Perspect., vol. 32, no. 2, pp. 91–114,
151, p. 104355, 2023.
| [89] | J. Miranda-Pinto, D. Murphy, K. J. Walsh, and E. R. |     |     |     |     |     |     | 2018. |     |     |     |     |     |
| ---- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |

Young, A model of expenditure shocks, J. Monet. Econ., [105] B. Angoshtari, E. Bayraktar, and V. R. Young, Optimal

consumption under a habit-formation constraint: The
vol. 154, p. 103807, 2025.
deterministic case, https://doi.org/10.2139/ssrn.4259364,
| [90] | N.  Bania |  and |  L.  Leete, |  Income |  volatility |  and  food |     |     |     |     |     |     |     |
| ---- | --------- | ---- | ----------- | ------- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- |

|     | insufficiency in US low-income households, 1991–2003, |     |     |     |     |     |     | 2022. |     |     |     |     |     |
| --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
Tech. rep., Citeseer, 2006. [106] Z. Q. Xu and F. Yi, An optimal consumption-investment

[91] L. Leete and N. Bania, The effect of income shocks on model  with  constraint  on  consumption,  Math.  Contr.

food insufficiency, Rev. Econ. Househ., vol. 8, no. 4, pp. Relat. Fields, vol. 6, no. 3, pp. 517–534, 2016.
[107] K. H. Roh and Y. H. Shin, Optimal consumption and
|     | 505–526, 2010. |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
portfolio selection with lower and upper bounds on
[92] B. McCarthy, A. Carter, M. Jansson, C. Benoit, and R.

Finnigan, Poverty, material hardship, and mental health consumption, Adv. Differ. Equ., vol. 2020, no. 1, p. 343,
|     | among workers in three front-line service occupations, J. |     |     |     |     |     |     | 2020. |     |     |     |     |     |
| --- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
[108] J. Peetz and R. Buehler, Is there a budget fallacy? The
|     | Poverty, vol. 22, no. 4, pp. 334–354, 2018. |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
role of budgeting in predicting time and money usage,
[93] S. J. Lambert, J. R. Henly, and J. Kim, Precarious work

schedules  as  a  source  of  economic  insecurity  and Organizational Behavior and Human Decision Processes, vol.
institutional distrust, RSF Russell Sage Found. J. Soc. Sci., 114, no. 2, pp. 168–182, 2009.
[109] P. Nokhiz, Modeling and simulation of artificial societies
|     | vol. 5, no. 4, pp. 218–257, 2019. |     |     |     |     |     |     |           |            |      |            |      |                |
| --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --------- | ---------- | ---- | ---------- | ---- | -------------- |
|     |                                   |     |     |     |     |     |     | to  study |  precarity |  and |  inequity, |  PhD |  dissertation, |
[94] D. Schneider and K. Harknett, Consequences of routine

work-schedule instability for worker health and well- Department of Computer Science, Brown University,
being, Am. Sociol. Rev., vol. 84, no. 1, pp. 82–114, 2019. Providence, RI, USA, 2024.
[95] C. B. Hawkinson, S. B. Andrea, A. Hajat, A. Minh, S. [110] P. Nokhiz, A. K. Ruwanpathirana, A. Bhaskara, and S.

|     |     |     |     |     |     |     |     | Venkatasubramanian, Counting hours, counting losses: |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- |
Owens, K. Blaikie, J. Seiler, A. R. Molino, and V. M.
The toll of unpredictable work schedules on financial
|     | Oddo, |  A  cross-sectional |     |  analysis |  of  work |  schedule |     |     |     |     |     |     |     |
| --- | ----- | ------------------- | --- | --------- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- |
notice and depressive symptoms in the United States, security, arXiv preprint arXiv: 2504.07719, 2025.
|     |                                              |     |     |     |     |     | [111] | R.  Motwani |  and |  P.  Raghavan,  |     | Randomized |  Algorithms. |
| --- | -------------------------------------------- | --- | --- | --- | --- | --- | ----- | ----------- | ---- | --------------- | --- | ---------- | ------------ |
|     | SSM Popul. Health, vol. 22, p. 101413, 2023. |     |     |     |     |     |       |             |      |                 |     |            |              |
[96] L.  Golden,  Irregular  work  scheduling  and  its Cambridge, MA, USA: Cambridge University Press, 2013.
  [112] N.  Bhutta,  J.  Bricker,  A.  C.  Chang,  L.  Dettling,  S.
|     | consequences, |     |  https://doi.org/10.2139/ssrn.2597172, |     |     |     |     |     |     |     |     |     |     |
| --- | ------------- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Goodman, A. H. Volz, J. Hsu, K. B. Moore, S. Reber, and
2015.
R. Windle, Changes in U.S. family finances from 2016 to
[97] J. R. Henly and S. J. Lambert, Unpredictable work timing

in  retail  jobs:  Implications  for  employee  work–life 2019: Evidence from the survey of consumer finances,
Federal Reserve Bulletin, vol. 106, no. 5, p. 42, 2020.
conflict, ILR Rev., vol. 67, no. 3, pp. 986–1016, 2014.
[113] U.S. Bureau of Labor Statistics, Consumer expenditure
| [98] | A. Uhde, N. Schlicker, D. P. Wallach, and M. Hassenzahl, |           |                  |             |                    |               |     |            |                                             |     |     |     |     |
| ---- | -------------------------------------------------------- | --------- | ---------------- | ----------- | ------------------ | ------------- | --- | ---------- | ------------------------------------------- | --- | --- | --- | --- |
|      |                                                          |           |                  |             |                    |               |     | surveys,   |  https://www.bls.gov/cex/2019-CEQ-infobook. |     |     |     |     |
|      | Fairness                                                 |  and      |  decision-making |             |  in  collaborative |  shift        |     |            |                                             |     |     |     |     |
|      | scheduling                                               |  systems, |  in              | Proc.  2020 |  CHI               |  Conf.  Human |     | pdf, 2019. |                                             |     |     |     |     |
[114] A. Patnaik, J. Venator, M. Wiswall, and B. Zafar, The role
|     | Factors in Computing Systems, Honolulu, HI, USA, 2020, |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
of heterogeneous risk preferences, discount rates, and
pp. 1–13.
earnings expectations in college major choice, J. Econom.,
[99] M. K. Lee, I. Nigam, A. Zhang, J. Afriyie, Z. Qin, and S.

Gao, Participatory algorithmic management: Elicitation vol. 231, no. 1, pp. 98–122, 2022.
|     |                                                     |     |     |     |     |     | [115] | R.  Cooper  |  and |  J.  Willis, |  Discounting:  |     |  Investment     |
| --- | --------------------------------------------------- | --- | --- | --- | --- | --- | ----- | ----------- | ---- | ------------ | -------------- | --- | --------------- |
|     | methods for worker well-being models, in Proc. 2021 |     |     |     |     |     |       |             |      |              |                |     |                 |
|     |                                                     |     |     |     |     |     |       | sensitivity |  and |  aggregate   |  implications, |     |  https://ideas. |
AAAI/ACM Conf. AI, Ethics, and Society, Virtual Event, 2021,
repec.org/p/red/sed015/607.html, 2014.
pp. 715–726.
[116] K. M. Ericson and D. Laibson, Intertemporal choice,
| [100] | P. Nokhiz, A. K. Ruwanpathirana, N. Patwari, and S. |     |     |     |     |     |     |     |     |     |     |     |     |
| ----- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
https://doi.org/10.1016/bs.hesbe.2018.12.001, 2019.

Venkatasubramanian, Precarity: Modeling the long term [117] K. L. Archuleta, The role of budgeting in financial well-
effects of compounded decisions on individual instability,   being: A literature review, Journal of Financial Therapy,
|     | in  Proc. |  2021 |  AAAI/ACM |  Conf. |  AI,  Ethics, |  and  Society, |     |     |     |     |     |     |     |
| --- | --------- | ----- | --------- | ------ | ------------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
vol. 4, no. 2, pp. 16–32, 2013.
Virtual Event, 2021, pp. 199–208. [118] S. A. DeVaney and W. DeVaney, The impact of financial
|     | P. Nokhiz, A. K. Ruwanpathirana, N. Patwari, and S. |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[101] education  on  personal  budgeting  practices,  Journal  of

Venkatasubramanian,  Agent-based  simulation  of Financial Counseling and Planning, vol. 31, no. 1, pp. 69–80,
|     | decision-making |     |  under |  uncertainty |  to |  study  financial |     |     |     |     |     |     |     |
| --- | --------------- | --- | ------ | ------------ | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
2020.
precarity, in Advances in Knowledge Discovery and Data [119] S.  Neubauer  and  B.  M.  Tull,  Financial  literacy  and

Mining, D. N. Yang, X. Xie, V. S. Tseng, J. Pei, J. W. financial decision-making in the context of retirement
Huang, and J. C. W. Lin, eds. Singapore: Springer Nature savings: A systematic review, Financial Planning Review,

208 Journal of Social Computing, September 2025, 6(3): 184−208
vol. 8, no. 3, pp. 1–18, 2017. [128] National Bureau of Economic Research, Supply chain
[120] Forbes Coaches Council, Ethical AI in marketing: disruptions and pandemic-era inflation, https://www.
Balancing automation with human values, https://www. nber.org/digest/202404/supply-chain-disruptions-and-
forbes.com/councils/forbescoachescouncil/2024/11/06/et pandemic-era-inflation, 2024.
hical-ai-in-marketing-balancing-automation-with-human- [129] V. Gupta, P. Nokhiz, C. D. Roy, and S.
values/, 2024. Venkatasubramanian, Equalizing recourse across groups,
[121] J. Cohen, K. M. Ericson, D. Laibson, and J. M. White, arXiv preprint arXiv: 1909.03166, 2019.
Measuring time preferences, J. Econ. Lit., vol. 58, no. 2, [130] F. D. Blau and L. M. Kahn, The gender wage gap: Extent,
pp. 299–347, 2020. trends, and explanations, J. Econ. Lit., vol. 55, no. 3, pp.
[122] G. Ainslie and N. Haslam, Hyperbolic discounting, 789–865, 2017.
https://psycnet.apa.org/record/1993-97149-003, 1992. [131] L. Reader, P. Nokhiz, C. Power, N. Patwari, S.
[123] B. Laufer, T. Gilbert, and H. Nissenbaum, Optimization’s Venkatasubramanian, and S. Friedler, Models for
neglected normative commitments, in Proc. 2023 ACM understanding and quantifying feedback in societal
Conf. Fairness, Accountability, and Transparency, Chicago, systems, in Proc. 2022 ACM Conf. Fairness Accountability
IL, USA, 2023, pp. 50–63. and Transparency, Seoul, Republic of Korea, 2022, pp.
[124] P. Nokhiz, A. K. Ruwanpathirana, and H. Nissenbaum, 1765–1775.
Rethinking optimization: A systems-based approach to [132] M. Whittaker, M. Alper, C. L. Bennett, S. Hendren, L.
social externalities, arXiv preprint arXiv: 2506.12825, Kaziunas, M. Mills, M. R. Morris, J. Rankin, E. Rogers, M.
2025. Salas, et al., Disability, bias, and AI, https://ainowinstitute.
[125] D. Laibson, Golden eggs and hyperbolic discounting, Q. J. org/publications/disabilitybiasai-2019, 2019.
Econ., vol. 112, no. 2, pp. 443–478, 1997. [133] C. Zwerling and H. Silver, Race and job dismissals in a
[126] D. Kahneman and A. Tversky, Prospect theory: An federal bureaucracy, Am. Sociol. Rev., vol. 57, no. 5, pp.
analysis of decision under risk, Econometrica, vol. 47, no. 651–660, 1992.
[134] M. T. Hicken, H. Lee, J. Morenoff, J. S. House, and D. R.
2, pp. 263–291, 1979.
[127] A. Tversky and D. Kahneman, Advances in prospect Williams, Racial/ethnic disparities in hypertension
theory: Cumulative representation of uncertainty, J. Risk prevalence: Reconsidering the role of chronic stress, Am.
Uncertain., vol. 5, no. 4, pp. 297–323, 1992. J. Public Health, vol. 104, no. 1, pp. 117–123, 2014.
Pegah Nokhiz received the PhD degree Aravinda Kanchana Ruwanpathirana
in computer science from Brown received the PhD degree in computer
University, USA in 2024. She is a science from The University of Utah, USA
postdoctoral fellow at the Digital Life in 2024, and the BS degree in computer
Initiative (DLI), Cornell Tech, USA. Her science from University of Moratuwa, Sri
research focuses on the long-term effects Lanka in 2018. He is a postdoctoral
of algorithms, optimizations, and machine researcher at the School of Computing,
learning in social contexts. She leverages National University of Singapore, Singapore.
interdisciplinary perspectives such as econometrics, normative His research focuses on machine learning theory, with interests
reasoning, and agent-based modeling to investigate such domain- in theoretical foundations, algorithms, and their applications to
spanning questions. learning systems.