A User-Centric Exploration of Axiomatic Explainable AI
in Participatory Budgeting.

Maryam Hashemi
School of Computer Science and
Engineering
University of New South Wales
Sydney, Australia
m.hashemi@unsw.edu.au

Ali Darejeh
School of Computer Science and
Engineering
University of New South Wales
Sydney, Australia
ali.darejeh@unsw.edu.au

Francisco Cruz∗
School of Computer Science and
Engineering
University of New South Wales
Sydney, Australia
f.cruz@unsw.edu.au

ABSTRACT
Explainable Artificial Intelligence (XAI) has been widely used to
clarify the opaque nature of AI systems. One area where XAI has
gained significant attention is Participatory Budgeting (PB). PB
mechanisms aim to achieve a proper allocation concerning both
the votes collected based on user’s preferences and the budget.
An essential criterion for evaluating these mechanisms is their
ability to satisfy desired properties known as axioms. However,
even though there are complex voting rules that meet some ax-
ioms, concerns regarding transparency persist. In this study, we
propose an approach to provide explanations in a PB setting by
treating axioms as constraints and seeking outcomes that adhere
to these constraints. This method enhances system transparency
and explainability. Each potential allocation is accepted or rejected
based on whether it satisfies the axioms, and the linear nature
of the axioms reduces computational complexity. We evaluated
our approach with real-world users to assess its effectiveness and
helpfulness. Our pilot study shows that users generally find ex-
planations helpful for understanding the system’s decisions and
perceive the outcomes as fairer. Additionally, users prefer general
explanations over counterfactual ones.

CCS CONCEPTS
• Human-centered computing → Empirical studies in HCI; •
Applied computing → Sociology; • Computing methodologies
→ Cooperation and coordination.

KEYWORDS
Explainable Artificial Intelligence; Users; Social Choice; Participa-
tory Budgeting.

ACM Reference Format:
Maryam Hashemi, Ali Darejeh, and Francisco Cruz. 2024. A User-Centric
Exploration of Axiomatic Explainable AI in Participatory Budgeting.. In
Companion of the 2024 ACM International Joint Conference on Pervasive
and Ubiquitous Computing (UbiComp Companion ’24), October 5–9, 2024,

∗Also with Universidad Central de Chile.

Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for third-party components of this work must be honored.
For all other uses, contact the owner/author(s).
UbiComp Companion ’24, October 5–9, 2024, Melbourne, VIC, Australia
© 2024 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-1058-2/24/10
https://doi.org/10.1145/3675094.3677599

Melbourne, VIC, Australia. ACM, New York, NY, USA, 5 pages. https://doi.
org/10.1145/3675094.3677599

1 INTRODUCTION
The field of Explainable Artificial Intelligence (XAI) focuses on
elucidating the reasoning behind decisions or predictions from Ar-
tificial Intelligence (AI) systems, thereby making AI models more
understandable and transparent [14], [7]. Various motivations for
using explanations in AI algorithms are cited in the literature [8], [6].
These reasons include: 1- Generating trust (trustworthy AI). 2- Meet-
ing legal requirements. 3- Upholding social responsibility, fairness,
and risk avoidance. 4- Creating accountable and reliable models. 5-
Minimizing biases. 6- Validating models. To enhance transparency,
several approaches have been proposed, such as feature impor-
tance, which identifies the most influential features in the model’s
decision-making process [10], [12], and counterfactual explanations,
which involve generating alternative scenarios where the model’s
output would change [15], [13]. Another significant approach is the
axiomatic approach, which uses axioms (a set of desired properties
and agreed values) to justify the outcomes [9]. Our work focuses
on the axiomatic approach, developing explainability based on this
method for AI algorithms aimed at solving Participatory Budgeting
(PB) problems.

PB is a democratic approach to determining the allocation of
funds for public projects [2]. In this set of challenges, we encounter
various projects with associated costs and a limited budget, typically
insufficient to cover all projects. The goal is to decide which projects
to fund and which to dismiss based on the votes of participants. In
cities worldwide, such as Paris, Sydney, and New York, residents
engage in participatory budgeting to collectively determine the
allocation of public funds. Residents cast votes on proposals ranging
from constructing a playground, repaving a road, and planting a
community garden, to installing new street lights. The outcome is
shaped by collective voting, determining the projects that secure
funding and those that do not.

Several intricate methods exist to determine a PB outcome, con-
sidering both the budget constraints and the votes. Each of these
methods adheres to a set of axioms. Generally, mechanisms that
satisfy a higher number of axioms, representing desired properties,
are deemed “better” and more justifiable. Therefore, axioms serve
as criteria for guiding the allocation process and justifying the final
outcome. Procaccia [11] notes that axioms capture what is desir-
able and should be applied to explain the mechanism’s outcome
to voters. Cailloux et al. [4] developed a logic-based language to
describe the strengths and weaknesses of different single-winner

126UbiComp Companion ’24, October 5–9, 2024, Melbourne, VIC, Australia

Maryam Hashemi, Ali Darejeh, & Francisco Cruz

voting rules for voters. Boixel et al. [3] view finding an argument
for an outcome as a constraint-solving problem in single-winner
settings, where a triple of (variables, domain, constraints) needs
definition.

In our work, for the first time, we designed a transparent mecha-
nism based on axioms to calculate and explain the outcome of a PB
setting, and evaluated the effectiveness of axiomatic explanation
on real-world users. The proposed approach considers axioms as
constraints to be fulfilled and systematically enumerates alloca-
tions that meet these constraints. Through this axiomatic approach,
we can automatically provide reasoning and explanations for each
chosen or excluded allocation based on the criteria of whether they
satisfy axioms or not. In the following section, we will briefly dis-
cuss participatory budgeting modeling, the axioms employed, and
formulate our approach.

2 PARTICIPATORY BUDGETING MODELING
Every PB settings can be modeled by the following variables, [1]:
• The first variable is agents (also known as residents or voters)

that will be shown as N = {1, ..., 𝑛}.

• The second variable is the budget (or resources). We show
the budget as B, which is the money limitation we can spend
on projects in general.

• There is also a set of projects (also known as candidates or

alternatives) as X = {𝑥1, ..., 𝑥𝑚 }.

• The next consideration is the degree of completion, which
can be divided into two general types: divisible and non-
divisible. Divisible projects can be completed to different
degrees (continuous). In our setting, all the projects are non-
divisible. It means they only can be completed 100% (shown
by 1) or 0 (shown by 0).

• Each project 𝑥 ∈ 𝑋 has an associated cost function shown
as: 𝑐𝑜𝑠𝑡 : 𝑋 −→ R+, and 𝑐𝑜𝑠𝑡(𝑥 𝑗 ) indicates the cost of the
𝑗-th project.

• Agents’ votes demonstrate how agents can express their
selection. In our setting, we use approval voting, which
means each voter can approve or disapprove of a project
(shown by 1 or 0, respectively). We consider that voters are
indifferent between approved or disapproved projects. All
the approved projects (shown by 1) are strictly preferred to
not approved ones (shown by 0). We show our vote list as
𝑉 𝑜𝑡𝑒 = {𝑣𝑜𝑡𝑒1, . . . , 𝑣𝑜𝑡𝑒𝑛 }. 𝑣𝑜𝑡𝑒𝑛 shows 𝑛th voter ballet that
contains 𝑚 members of 1 or 0 indicating approvement or
disapprovment of a project respectively.

Based on the previous notations, we can define a PB voting rule

as follows:

𝐹 : ⟨𝑉 𝑜𝑡𝑒, 𝐵, 𝑐𝑜𝑠𝑡(𝑥)⟩ −→ {𝐶 | 𝐶 ⊆ 2

𝑋 , ∑︁
𝑐𝑘 ∈𝐶

𝑐𝑜𝑠𝑡(𝑐𝑘 ) ≤ 𝐵}

(1)

We show an allocation as 𝐶 containing funded 𝑥 𝑗 s, and 𝑐𝑜𝑠𝑡(𝑐𝑘 )
is a function that maps selected projects (𝑐𝑘 s) to their costs, and 2𝑋
is all the possible allocations.

Axioms are agreed-upon values that we can use as the founda-
tional principles for our voting mechanism and deploy them as
explanations for users. In the following, we introduced the axioms
that we used for the purpose of providing explanations:

• Feasibility: This axiom says that an outcome 𝐶 is feasible
if and only if: (cid:80)𝑐𝑘 ∈𝐶 𝑐𝑜𝑠𝑡(𝑐𝑘 ) ≤ 𝐵. In other words, it says
that the summation of our spending money should not be
beyond our budget.

• Exhaustiveness [2]: This axiom says that a feasible allocation,
𝐶, is exhaustive if it is impossible to fund any more projects
with the leftover budget [1]. Considering our setting char-
acterization (approval voting and non-divisible degree of
completion), we can formulate it as:
(𝐵 − (cid:80)𝑐𝑘 ∈𝐶 𝑐𝑜𝑠𝑡(𝑐𝑘 )) < 𝑐𝑜𝑠𝑡(𝑐′), 𝑐′ ∈ 𝑋 \𝐶

• Utilitarian welfare_consistent Axiom: An allocation 𝐶 ∈ 2𝑋
is utilitarian welfare consistent if there exists no 𝐶′ ∈ 2𝑋
such that Σ𝑖=𝑛
𝑢𝑖 (𝐶) [5]. This axiom states that
𝑖=1
an allocation that causes a bigger utility is preferred to other
allocations.

𝑢𝑖 (𝐶′) > Σ𝑖=𝑛
𝑖=1

3 METHODOLOGY
Leveraging axioms to determine outcomes offers the advantage of
transparency. We employed axioms, which represent agreed-upon
values, to advocate for funding certain projects while providing
reasoning for the rejection of others.

The proposed mechanism operates based on a constraint-solving
problem framework, which involves an objective function aimed
at maximizing the number of funded projects, along with a set
of linear constraints. We formulated each mentioned axiom as an
integer linear form and used an Integer Linear Programming (ILP)
solver to find all possible outcomes that meet our constraints.

In this setting, we present the outcome of funding the projects as
𝑋 . If 𝑥 𝑗 = 1 means that the project 𝑗 has been funded and if 𝑥 𝑗 = 0
means that this project has not been funded. Based on that, the
problem can be formulated in ILP as follows:

𝑚
∑︁
𝑗=1

𝑥 𝑗

(2)

subject to:

𝑥 𝑗 ∈ [0, 1]

for all

𝑗 = 0, 1, . . . , 𝑚,

We applied our ILP problem in Python, Gurobi optimizer1. Gurobi
Optimizer is a prescriptive analytics platform and a decision-making
technology.

4 EXPERIMENTAL USER STUDY
As the next step of our work, we tested the proposed axiomatic
approach on real-world users to see how these explanations work in
practice. More specifically, we studied whether presenting reason-
ing to users will bring more transparency from the user perspective
and help them to better trust the system (trustworthiness).

For instance, in a simple scenario, the proposed approach might
provide an explanation like this: “Although you supported project
A, more voters voted for project B. Consequently, funding project B
would result in greater overall satisfaction among voters. Addition-
ally, our budget constraints prevent us from funding both projects.”
In this example, the proposed axiomatic approach employs the
utilitarian welfare-consistent axiom (preferring allocations that
maximize voter utility) and feasibility (ensuring the total project

1https://www.gurobi.com/

127A User-Centric Exploration of Axiomatic Explainable AI
in Participatory Budgeting.

UbiComp Companion ’24, October 5–9, 2024, Melbourne, VIC, Australia

costs stay within budget) to identify the most suitable allocation
while generating reasoning for alternative scenarios.

Our user study primarily focuses on assessing whether explana-
tions generated based on axioms enhance users’ comprehension
of the outcomes in the PB setting. Our arguments regarding the
outcome derive from theoretical mathematical properties, and it
remains uncertain whether users perceive them as understandable.
For instance, while it is theoretically preferable to maximize the
utility function, it is unclear from the user’s perspective whether
this argument is understandable. The secondary objective of this
study is to examine how our explanations and justifications assist
participants in:

• Better understanding the decision-making process of the

system,

• Developing greater trust in the algorithm and the system’s

decisions,

• Perceiving the system’s outcomes as fairer after receiving

the provided explanations

During this assessment, we examined whether users lean toward
personalized explanations or counterfactual explanations. On the
one hand, a personalized explanation involves providing reasoning
for why a particular outcome was chosen, offering insight into why
certain projects were funded or not based on the user’s votes. On
the other hand, a counterfactual explanation steps into the realm
of "what if," clarifying how the outcome would change if other
participants’ votes shifted to align with the user’s preferences. It’s
important to note that these two types of explanations operate
independently of each other.

Our hypothesises regarding the mentioned questions are listed

below:

(1) We hypothesize that as explanations will help users to better

understand the decision of the system.

(2) We hypothesize that our explanations will pave the way and

help users to better trust the system.

(3) We hypothesize that our explanations will help users per-
ceive the outcome of the system as fairer compared to situ-
ations where we do not provide any explanation.

(4) We anticipate that users prefer personalized explanations

over counterfactual explanations.

Our user study began with the acquisition of human ethics re-
search approval2, an essential step in our study protocol. Following
this, we disseminated information about our research through Me-
chanical Turk.

During the data collection phase, we engaged participants by
providing an overview of the study and obtaining their consent
to participate. Subsequently, participants were presented with our
participatory budgeting problem and asked to vote based on their
personal interests. Based on the collected votes, the algorithm’s
decision was revealed to them.

We then gauged participants’ perceptions of the algorithm’s clar-
ity and trustworthiness through a series of questions. Participants
were also provided with automated explanations and justifications,
followed by inquiries regarding the transparency of the system
post-explanation.

2HC reference number: iRECS5941

Upon completion of the survey, we proceeded to the phase of
data validation and analysis, culminating in the publication of our
results.

4.1 Survey Structure:
We designed a questionnaire to evaluate our hypothesises regarding
explainable PB setting. The questionnaire is structured to maintain
anonymity, gathering only essential demographic information such
as gender, age, participants’ country, and their familiarity with
computers. This data collection serves to explore potential corre-
lations between gender, the stage of development of the country,
the level of computer science knowledge, and how participants
assess explanations. Our study involved two distinct participatory
budgeting cases, each with different scenarios. Each participant
randomly assigned to one case and based on their vote, explana-
tions regarding one scenario presented to them. We only showed
one participatory problem to users in order to prevent potential
experimental confusion and bias. The two participatory budgeting
cases are independent of each other. Randomly, we presented one
case to each user in a way that each case is shown 50% of the time.
In the following, we presented each case and possible options

for the user to vote.

4.2 Presented Participatory Budgeting Cases:

• CASE 1:

Consider there is a budget of $11,000 allocated to the Depart-
ment of Computer Science, and the dean aims to allocate
these funds to two potential projects:

(1) Buying new books for the department library with a total

cost of $10,000.

(2) Upgrading the computer labs, incurring a cost of $9000.
Given the available budget, the dean can only fund one out of
these two projects. To facilitate this decision-making process,
the dean has appointed three representatives for the depart-
ment, and your role is to serve as the third representative,
providing your vote.

We considered that the first and second representatives are Alice
and Bob. Alice and Bob both approved only acquiring new books for
the library. We are employing the greedy rule as our voting method.
Based on this rule, we count the number of people who voted for
each project, and the project that earned the most approval will
be funded. The outcome will be buying new books for the library
regardless of the voter’s vote in this case.

• CASE 2:

Sydney City Council has allocated $1.1 million to enhance
the city, considering three potential projects:
(1) Creating a new park with a cost of $1 million.
(2) Establishing an art center with a cost of $0.9 million.
(3) Constructing a new shopping center with a cost of $1.1

million.

With the available budget, the city can only fund one out of
these three projects. To make this decision, the City Council
has selected three representatives, and your role is to be the
third representative, providing your vote.

We considered the first and second representatives are Alice and
Bob. They both think the city needs a new park for children, so they

128UbiComp Companion ’24, October 5–9, 2024, Melbourne, VIC, Australia

Maryam Hashemi, Ali Darejeh, & Francisco Cruz

approved the first project and disapproved others. We are using the
greedy rule as a method of voting. Based on this rule, we count the
number of people who voted for each project, and the project that
earned the most approval will be funded. So, in this scenario, the
park will be funded regardless of the collected user’s vote.

We explained to our participants that they have the option to
either approve or disapprove of projects based on their individual
interests. There is no restriction on the number of projects that can
be approved, but participants must approve at least one project. We
then explained that we had already collected votes from other par-
ticipants and asked them to indicate their approval or disapproval.
It was mentioned that all representative votes had been processed
by the algorithm. Following their responses, the system’s decision
will be provided, along with explanations regarding this decision.
Subsequently, a series of questions will be presented to assess the
impact of these explanations.

After the users’ votes were collected and the outcome of the
algorithm was shown to them, we asked some questions regarding
the transparency of the outcome and the level of the users’ trust
in the system. In the next stage, we presented explanations and
reasoning based on axioms to justify the outcome of the algorithm.
Following the presentation of these explanations, we asked further
questions to assess the effect and performance of the explanations
on the users’ understanding of the system.

(a) User understanding of the sys-
tem decision, case 1.

(b) User understanding of the sys-
tem decision, case 2.

(c) User trust to the system deci-
sion, case 1

(d) User trust to the system deci-
sion, case 2.

5 RESULTS
We conducted our pilot study with 26 users (male = 16, female = 10).
62% participants aged between 25- 34 and 23% aged between 35-44.
Of the participants, 50% were from India, 42.3% from the United
States, and the rest from various countries such as Italy and Sri
Lanka. Overall, 42% participants described their computer science
literacy as advanced and 31% expert.

Most of the participants (72.4%) found the explanations either
extremely helpful or very helpful in understanding the system’s
decision. Additionally, 63.3% of the participants preferred general
explanations over counterfactual ones. About 30% of participants
reported that the explanations had a positive impact on their per-
ception of the system’s fairness. None of the participants reported
a negative impact from the explanations in that matter. However,
we could nott draw any meaningful conclusions about how the ex-
planations affected users’ trust in the system. In some cases (20%),
providing the explanations decreased the level of the trust in users.
27% of participants reported an increase in their level of trust in
the system after receiving an explanation, 23% reported a decrease
in their level of trust, and 50% expressed that their level of trust
did not change. In Fig. 1, we present how system decision trans-
parency, fairness, and user trust in system decisions change before
and after receiving explanations for both presented PB scenarios
in our survey, shown as case 1 and case 2. We provided users five
options to choose from for each criterion of transparency, trust,
and fairness. As shown, user understanding of the system (system
transparency) and perceived fairness improved in both cases after
receiving explanations.

(e) To what extent users find the
system decision fair, case 1.

(f) To what extent users find the
system decision fair, case 2.

Figure 1: Comparison of user’s report regarding the trans-
parency of the system’s decision (first row), their trust to
the system (the second row), and the fairness (the third row)
before and after receiving explanations.

6 CONCLUSION AND FUTURE WORKS
In this study, we focused on providing explanations for AI algorithm
outcomes in PB settings. By using axioms (desired properties) as lin-
ear constraints, we identified all possible outcomes that meet these
criteria, ruling out any that do not. We then tested our approach
with real-world users to see if the explanations would enhance trans-
parency, increase user trust, and improve perceived fairness. Our
results show that users generally found the explanations helpful for
understanding the system, improving transparency and fairness.
However, we could not draw a definitive link between trust in the
system’s decisions and the explanations.

Next, we will conduct an extensive user study with a substantial
number of participants to verify our findings and gain deeper in-
sights into the explainable PB setting. Additionally, we will explore
the reasons behind instances where providing explanations reduced
trust and how to mitigate this issue.

129A User-Centric Exploration of Axiomatic Explainable AI
in Participatory Budgeting.

UbiComp Companion ’24, October 5–9, 2024, Melbourne, VIC, Australia

REFERENCES
[1] Haris Aziz and Aditya Ganguly. 2021. Participatory Funding Coordination: Model,
Axioms and Rules. In International Conference on Algorithmic Decision Theory.
Springer, 409–423.

[2] Haris Aziz and Nisarg Shah. 2021. Participatory budgeting: Models and ap-
proaches. In Pathways Between Social Science and Computational Social Science.
Springer, 215–236.

[3] Arthur Boixel and Ulle Endriss. 2020. Automated justification of collective

decisions via constraint solving. (2020).

[4] Olivier Cailloux and Ulle Endriss. 2016. Arguing about voting rules. (2016).
[5] Ioannis Caragiannis, David Kurokawa, Hervé Moulin, Ariel D Procaccia, Nisarg
Shah, and Junxing Wang. 2019. The unreasonable fairness of maximum Nash
welfare. ACM Transactions on Economics and Computation (TEAC) 7, 3 (2019),
1–32.

[6] Francisco Cruz, Charlotte Young, Richard Dazeley, and Peter Vamplew. 2022.
Evaluating human-like explanations for robot actions in reinforcement learning
scenarios. In 2022 IEEE/RSJ International Conference on Intelligent Robots and
Systems (IROS). IEEE, 894–901.

[7] Richard Dazeley, Peter Vamplew, Cameron Foale, Charlotte Young, Sunil Aryal,
and Francisco Cruz. 2021. Levels of explainable artificial intelligence for human-
aligned conversational explanations. Artificial Intelligence 299 (2021), 103525.

[8] Julie Gerlings, Arisa Shollo, and Ioanna Constantiou. 2020. Reviewing the need
for explainable artificial intelligence (xAI). arXiv preprint arXiv:2012.01007 (2020).
[9] Maryam Hashemi, Ali Darejeh, and Francisco Cruz. 2024. Understanding User
Preferences in Explainable Artificial Intelligence: A Survey and a Mapping Func-
tion Proposal. arXiv:2302.03180 [cs.AI] https://arxiv.org/abs/2302.03180
[10] Scott M Lundberg and Su-In Lee. 2017. A unified approach to interpreting model
predictions. Advances in neural information processing systems 30 (2017).

[11] Ariel D Procaccia. 2019. Axioms should explain solutions.

In The Future of

Economic Design. Springer, 195–199.

[12] Marco Tulio Ribeiro, Sameer Singh, and Carlos Guestrin. 2016. " Why should i
trust you?" Explaining the predictions of any classifier. In Proceedings of the 22nd
ACM SIGKDD international conference on knowledge discovery and data mining.
1135–1144.

[13] Sahil Verma, John Dickerson, and Keegan Hines. 2020. Counterfactual explana-
tions for machine learning: A review. arXiv preprint arXiv:2010.10596 (2020).

[14] Giulia Vilone and Luca Longo. 2021. Notions of explainability and evaluation
approaches for explainable artificial intelligence. Information Fusion 76 (2021),
89–106.

[15] Sandra Wachter, Brent Mittelstadt, and Chris Russell. 2017. Counterfactual
explanations without opening the black box: Automated decisions and the GDPR.
Harv. JL & Tech. 31 (2017), 841.

130