Results in Engineering 24 (2024) 102828

Contents lists available at ScienceDirect

Results in Engineering

journal homepage: www.sciencedirect.com/journal/results-in-engineering

Budget allocation problem for projects with considering risks, robustness,
resiliency, and sustainability requirements

Reza Lotfi a,b,*, Masoud Vaseei c, Sadia Samar Ali d,e, Sayyed Mohammad Reza Davoodi f,
Mansour Bazregar g, Soheila Sadeghi h
a Department of Industrial Engineering, Yazd University, Yazd, Iran
b Behineh Gostar Sanaye Arman, Tehran, Iran
c Department of Industrial Engineering, Lahijan Branch, Islamic Azad University, Lahijan, Iran
d Department of Industrial Engineering, Faculty of Engineering, King Abdulaziz University, Jeddah, Saudi Arabia
e Supply chain Department, New Delhi Institute of Management, New Delhi 110062, India
f Department of Management, Dehaghan Branch, Islamic Azad University, Dehaghan, Iran
g Department of Industrial Management, Islamic Azad University South Tehran Branch, Tehran, Iran
h Dreeben School of Education, University of the Incarnate Word, San Antonio, TX, USA

A R T I C L E I N F O

A B S T R A C T

Keywords:
Budget allocation
Projects
Resiliency
Risk
Robustness

Budget Allocation Problem (BAP) for projects is considered one of the critical risks that necessitate the
completion of projects in the shortest possible duration. This aspect is significant in extensive projects such as
national endeavors directly impacting people’s livelihoods. This research focuses on introducing Sustainable,
Robust, Resilient, and Risk-averse Budget Allocation for Projects (S3RBAP). A hybrid robust stochastic optimi-
zation approach was employed, incorporating Weighted VaR (WVaR) and the minimum function as risk criteria
to ensure the robustness of the objective function. This model is designed to minimize the weighted expected
value, WVaR, and the minimum progress function, thereby promoting the 3R and sustainability framework to
tackle budget fluctuations and enhance project viability. The case study revolves around the construction of
national projects in Iran. Ultimately, the project’s required budget was allocated within the budgetary con-
straints. Sensitivity analysis found that the integration of 3R and sustainability led to a 13.5 % reduction in the
progress function compared to scenarios without these principles. Furthermore, increasing the conservatism
coefficient to 20 % decreased the progress function to (cid:0) 0.58 %. Reducing the resiliency coefficient had an
adverse effect by disrupting the budget allocation process. The computational time is increased gradually with
the escalation of problem complexity, while the progress function decreases due to the increased number of
projects. The findings demonstrate that using an exponential function promotes risk aversion, whereas a sine
function encourages risk-seeking behaviour within this research context.

1. Introduction

In the realm of project management, the allocation of budget re-
sources is a critical aspect that directly impacts the success and sus-
tainability of projects. Mainly, when it comes to allocating budgets for
projects, taking into account potential risks and ensuring robustness in
financial planning are key factors that demand careful consideration [2].
Managing project budgets while acknowledging risks and ensuring
robustness requires an integrated approach that considers various facets,
such as uncertainty, unforeseen events, and the need for contingency
planning [3–7]. By proactively addressing risks in budget allocation and

incorporating robustness into financial planning, organizations can
enhance their ability to achieve project objectives, mitigate potential
setbacks, and deliver successful outcomes [9–11].

In the dynamic landscape of project management, the allocation of
budgets plays a pivotal role in determining the trajectory and success of
projects. Effectively distributing financial resources is crucial
for
meeting project milestones, delivering outcomes, and achieving orga-
nizational goals. However, the budget allocation process becomes even
more complex and challenging when risks are factored into the equa-
tion. Risks, ranging from uncertainties in market conditions to unfore-
seen events, can significantly impact a project’s financial health and

* Corresponding author. Department of Industrial Engineering, Yazd University, Yazd, Iran.

E-mail address: reza.lotfi.ieng@gmail.com (R. Lotfi).

https://doi.org/10.1016/j.rineng.2024.102828
Received 9 April 2024; Received in revised form 19 August 2024; Accepted 1 September 2024
Available online 17 September 2024
2590-1230/© 2024 The Authors.  Published by Elsevier B.V. This is an open access article under the CC BY-NC license ( http://creativecommons.org/licenses/by-
nc/4.0/ ).

R. Lotfi et al.

overall viability [12,13].

Project managers and stakeholders must adopt a proactive approach
integrating risk management practices with robust budget allocation
strategies to navigate these challenges and enhance project resilience.
By anticipating potential risks, assessing their impact on budgetary
constraints, and developing contingency plans, organizations can miti-
gate adverse effects, improve project outcomes, and ensure the suc-
cessful completion of projects within set financial parameters [14,15].
In this context, this paper delves into the critical importance of
considering risks and robustness in project budget allocation. By
exploring relevant literature, best practices, and case studies, we aim to
shed light on the strategic approaches that enable organizations to
navigate uncertainties, optimize resource utilization, and achieve proj-
ect success amidst evolving challenges in the project management
landscape (see Fig. 1).

Hence, assessing and distributing the budget effectively for timely
project completion is crucial. This issue is significant as it impacts
project progression and minimizes project delays. It is imperative for
organizations and project managers to closely monitor projects and
allocate budgets efficiently to expedite project timelines [16]. Re-
searchers and managers should incorporate mathematical models to
address this challenge [17]. The study’s results present a new method
emphasizing strength and adaptability in the BAP. We also promote
robust optimization and resilience in the BAP, employing a risk-averse
approach to manage uncertainties and address risk-averse decision--
making. Moreover, it is crucial to consider sustainability as a key aspect
of project management.

Ultimately, the research’s innovation and primary goal can be

summarized as.

• BAP for projects considering Risks, Robustness, and Resiliency (3R),
• Considering the policies for distributing budgets for projects,
• Paying attention to sustainability as a project occupation for

distributing budgets for projects.

The paper’s organization is detailed as follows: Section 2 offers a
survey of recent works in the field of BAP. Section 3 explains the
mathematical model of S3RBAP. Section 4 encompasses the research
results, sensitivity analysis, and discussions. Section 5 explores mana-
gerial perspectives and real-world applications. Section 6 defines con-
clusions and future research.

2. Recent and related works

This study conducts a literature review to explore related works
within the domain of BAP. Moreover, we categorize and present the

Fig. 1. BAP problem.

2

Results in Engineering 24 (2024) 102828

related works in Table 1, which details the methodology, uncertainty,
risk, and case study related to BAP. Subsequent sections elaborate on
recent works.

2.1. Recent works on BAP with MILP

A novel hybrid methodology is introduced by Fu, Xiao, Lee, and
Huang [18]. They have presented a new innovative method that com-
bines
the Grey Wolf Optimization Algorithm (GWOA) with a
simulation-optimization framework to address stochastic optimization
issues in manufacturing and service systems. They incorporate a budget
allocation rule to select top solutions and show through numerical ex-
amples that this approach surpasses existing allocation strategies,
delivering better solutions in fewer iterations.

As service organizations, municipalities play a crucial role in stra-
tegic planning and community development by implementing projects
with pre-allocated budgets. The challenge lies in fairly distributing
projects among municipalities while minimizing budget discrepancies.
Jemmali [19] introduces lower bounds and heuristics to address this
equity distribution problem, with their performance evaluated in an
experimental study.

Shi, Xiang, Xiao, and Xing [20] focus on the importance of trans-
portation infrastructure like pavements and bridges for a nation’s
economy. It highlights the challenges posed by the underperformance
and structural deficiencies in these infrastructure elements, necessi-
tating repair or reconstruction. The research develops and tests algo-
rithms to optimize maintenance decisions for deteriorating multi-facility
transportation infrastructure systems, demonstrating their efficiency
and effectiveness
in finding satisfactory maintenance strategies.
Important insights are provided to guide decision-making in real-world
scenarios.

Blockchain’s integration with Internet of Things (IoT) has been
extensively researched due to its security and privacy benefits. Edge
computing aids IoT blockchain development by allowing IoT devices to
acquire computational resources from edge servers. The interaction and
pricing dynamics between edge servers and IoT devices with budget
allocation problems are modelled as a multi-leader, multi-follower
Stackelberg game to optimize resource allocation and maximize profits,
with efficient algorithms designed to reach the Stackelberg Equilibrium
in Ding et al. [9]. Extensive simulations confirm the effectiveness of the
proposed model and algorithms.

In the United States, transportation agencies encounter challenges
such as insufficient funding and deterioration of road surfaces. Abu-
khalil and Smadi [8] utilize optimization methods like integer pro-
gramming for network-wide maintenance planning to tackle these
issues. However, the high computational demand hinders the scalability
of the algorithm. This research presents the mathematical formulation of
binary integer programming that incorporates budget limitations and
constraints related to the Percentage of Poor Assets (PPA). It introduces
a novel approach that integrates the PPA constraint and a technique to
decrease the search space through the statistical bootstrap method. The
efficacy of the proposed approach is showcased by comparing it with
other optimization methods on a small network of asphalt concrete
pavements, demonstrating a significant reduction in the time required
for budget allocation across 400 segments.

The IoT research community is increasingly interested in Blockchain
due to its decentralization and security features. However, privacy
concerns arise as all nodes have access to sensitive data on the chain. To
cover this subject, a Local Differential Privacy (LDP) mechanism is
proposed by K. Zhang et al. [21] to perturb data before uploading.
Traditional LDP methods face challenges fitting with Blockchain due to
fixed input ranges and large data volumes. A novel LDP mechanism
splits numerical data and uses digital bit perturbation, adapting privacy
budgets for enhanced data utility with minimal deviation. Mean esti-
mation is employed to evaluate the performance, showcasing the
effectiveness of the proposed LDP mechanism in preserving privacy

R. Lotfi et al.

Table 1
Classification of recent works.

Reference

[13]
[18]
[25]
[23]
[19]
[20]
[9]
[8]
[21]
[1]
[2]
[22]
[26]
[14]
[24]
This research

Type

BAP
BAP
PBAP
BAP
BAP
BAP
BAP
BAP
BAP
3RBAP
BAP
BAP
BAP
BAP
BAP
S3RBAP

Methodology

Mixed-Integer Linear Programming (MILP) + Simulation
MILP + GWOA
Machine learning
Multiobjective Simulation + VEGA
MILP + Branch-and-bound
MILP
Bilevel MIP
Binary integer programming
MILP
MILP
MILP
MILP + Tabu search
Statistic approach
Strata
Simulation
MILP

Uncertainty

Possibilistic
Stochastic
–

Stochastic
–

Stochastic
–
–
–

RO
–

Stochastic
–

Possibilistic
Possibilistic
Robust optimization

Results in Engineering 24 (2024) 102828

Risk

Case study

–
–
–
–
–
–
–
–
–
✓
–
–
–
–
–
✓

Numerical Example (NE)
NE
NE
NE
NE
NE
NE
NE
NE
Healthcare project
NE
NE
Iran
NE
NE
National projects in Iran

while maintaining data utility.

Lotfi et al. [1] introduced 3RBAP to enhance budget allocation
strategies for large-scale projects. The research showed that 3RBAP
improved project progress by 17.07 % compared to traditional methods.
Sensitivity analysis showed that increasing conservativity and reducing
resiliency could improve progress. The study also highlighted the po-
tential for further optimization in budget allocation.

Umrawal et al. [2] expanded upon the conventional discrete influ-
ence maximization problem through a novel approach. Instead of
exclusively offering complimentary products to a limited group of
influencers within a budget,
they explored a strategy involving
providing discounts to a broader array of influencers to enhance
engagement while working within the exact budget boundaries. This
alternative scenario can be interpreted as maximizing the multilinear
extension of a monotone submodular set function while abiding by an L1
constraint. To address this challenge, they introduced and assessed a
highly efficient (1-1/e)-approximation algorithm. Through conducting
experiments on an actual social network, they showcased the effec-
tiveness of this method compared to existing approaches for generalized
influence maximization dilemmas.

Tabu search is a robust technique for addressing combinatorial
optimization challenges; however, it encounters difficulties in stochastic
simulation optimization due to simulation disturbances. Yu, Lahrichi,
and Matta [22] introduced an effective strategy for allocating simulation
budgets to tackle this issue. The current approaches for budget alloca-
tion in tabu search lack efficiency. A novel budget allocation approach
grounded in the extensive deviation framework is suggested to enhance
the performance of tabu search under stochastic circumstances. This
fresh policy is proven to be nearly optimal in maximizing the likelihood
of tabu search making accurate decisions in a single iteration. Experi-
mentation on real-world issues indicates that the proposed technique
empowers tabu search to attain superior outcomes with the same
computational resources.

2.2. Recent works on BAP with simulation

Xiao et al. [13] focus on prioritizing options given input uncertainty
within a set budget. It establishes a model for the optimal allocation of
computing resources, estimates accurate ranking probabilities, and
suggests a sequential ranking approach. The effectiveness of this method
is showcased through numerical simulations, offering clarity on optimal
conditions and effective resource allocation strategies.

Kou, Xiao, Cao, and Lee [23] created guidelines for allocating
simulation budgets in the Vector Evaluation Genetic Algorithm (VEGA)
to enhance its effectiveness in addressing multiobjective simulation
optimization challenges. These allocation guidelines were evaluated and

demonstrated to boost the search effectiveness of VEGA in uncertain
conditions by decreasing the average distance to the actual Pareto front
and improving the accuracy of the estimated Pareto front.

Traditional stochastic optimization in financial operations research
involves a two-step process: calibrating parameters of stochastic pro-
cesses and optimizing decision vectors. Uysal, Li, and Mulvey [24]
combine these steps in an end-to-end feedforward network, examining
model-based and model-free variants. Computational experiments show
improved out-of-sample performance with a model-based approach,
achieving a Sharpe ratio of 1.16 compared to 0.83 for a pure-risk
budgeting model. Filtering assets further enhances The end-to-end al-
gorithm by boosting the out-of-sample Sharpe ratio to 1.24. This
approach is versatile and applicable to various financial and optimiza-
tion problems.

2.3. Recent works on BAP with other methods

Participatory budgeting, a democratic method widely used in global
cities, involves public project funding decisions. A literature review from
the computational social choice field explores this topic by merging
computer science and microeconomic theories. A mathematical model is
presented by Aziz and Shah [25], categorizing budgeting models based
on project divisibility and funding restrictions. Various approaches focus
on preference collection, welfare goals, fairness criteria, and voter mo-
tivations. Future research opportunities in participatory budgeting are
also discussed.

Song and Kawai [14] introduced and examined a dynamic allocation
strategy for finite budgets in stratified sampling on the unit hypercube
using adaptive variance reduction through Strata. The allocation plan is
periodically adjusted based on diminishing stratum variances, and
stratum means estimates and changes to variance reduction parameters.
This scheme can incorporate various established algorithms for param-
eter exploration. The scheme establishes optimal learning rates for
stratum batches when employing stochastic approximation, adapting to
changes in batch size. Numerical outcomes are presented to validate the
theoretical conclusions and showcase the efficacy of the proposed
strategy.

A company’s problem-solving endeavours can be seen as blending
physical and cognitive actions to reach a specific outcome. The firm’s
internal structure influences how information inputs are allocated across
various task units, impacting the distribution of mental work. Bouzari,
Gyenge, Ebrahimi, and Fekete-Farkas [26] focused on Iranian Small And
Medium Enterprises (SMEs); they utilized NCA analysis, a cutting-edge
method, with the assistance of R software to assess data. The results
highlight that meeting six prerequisites is essential to attain a 50 %
efficient performance level: a minimum of 22.7 % innovation, 30.4 %

3

R. Lotfi et al.

Results in Engineering 24 (2024) 102828

CSR, 56.7 % IT investment, 38.3 % SMM, 11.7 % product differentiation,
and 38.3 % CRM.

2.4. Research gap

The prior research on BAP according to classification criteria such as
type, methodology, uncertainty, risk, solution approach, and case study
is categorized in Table 1. The analysis reveals the researchers’ lack of
examination and input on the BAP problem. A new approach for the
3RBAP problem is attempted in this study, along with the application of
a novel mathematical model. Therefore, a 3RBAP model is required to
handle uncertainty and withstand complex situations such as COVID-19.
This model is proposed for national projects. The contribution of this
research is determined as follows based on the gap analysis.

• BAP for projects considering the 3R approach,
• Paying attention to sustainability as a project occupation for
distributing budgets for projects (This model is called S3RBAP).

3. Problem description

This study explores the S3RBAP issue, recognizing the significance of
managing project budgets and meeting managerial needs to achieve a
balanced allocation considering requirements and constraints. The
optimal budget allocation achieved is illustrated in Fig. 2.

To guarantee robustness, robust stochastic optimization, and worst-
case scenarios are integrated into the objective function (progress based
on budget allocation). Additionally,
stochastic programming is
embedded to address potential fluctuations and disruptions. The study
examines and proposes robust budget allocation policies to mitigate
budget fluctuations, aiming to maximize project progress based on
allocated budgets. Finally, budget allocation is performed for projects
under uncertain scenarios.

Drawing upon these considerations, the S3RBAP model is proposed,

incorporating three key strategies.

1. Robust approach: This approach incorporates vital stochastic
optimization and accounts for worst-case scenarios in the objective
function (tracking progress based on budget allocation) to guarantee
resilience [1,27].

2. Resilience approach: This plan utilizes an adaptable budgeting
method that considers different scenarios and includes a disruption
factor [28,29].

3. Risk-averse approach: This strategy incorporates the minimax
function into the objective function (progress function) to minimize
risk [30,31].

4. Sustainability approach: This policy considers sustainability as a

project occupation and distributing project budgets [32,33].

Assumptions.

a) The budget and progress of each project are not definitively known

and uncertain,

b) The maximum budget limit integrates a resilience factor following

the resilience policy,

c) The decision-maker assigns a weighting factor to each project based
on factors like remaining duration, completion percentage, the
project owner’s influence, and the project’s complexity level,

d) To manage fluctuations and disruptions, the issue is framed as robust

stochastic programming,

e) It is presumed that the remaining progress function of each project
progresses linearly in alignment with the allocated budget. It means
that by paying one unit of budget, amount of progress project is one
percent.

f) The model uses a fixed budget that must be evenly spread across

projects [1].

Notations.

Indices (sets):
i

s

Parameters:

bacis

rccis

bacrccis

pris

pps
MBud

β
δ

εi
duris
remduris

ψi

λ1, λ2,
λ3, λ4
wi

Budget at completion for project i under
scenario s,
Remaining claims of contractors for
project i under scenario s,
Total budget at completion for project i
under scenario s,bacrccis = bacis + rccis,
Percent complete for project i under
scenario s,
Probability occurrence of scenario s,
Total budget for assignment between
project,
Conservativity coefficient,
Resiliency or disruption coefficient for
budget,
Occupation for project i,
Duration of project i under scenario s,
Remaining duration for project i under
scenario s, remduris = duris(1 (cid:0) pris),
Significant factor for project i based on
project owner,
A significant factor for components of
the weight factor
Total weight factor for project i based on
remaining duration, percent complete,
significant factor of project owner and
occupation level of project,

∑

pris

+ λ2

s
∑
∑

+

pris

i

s

∑

1
remduris

wi = λ1

s
∑
∑

i

s

+ λ4

λ3

ψ i∑
ψ i

i

1
remduris
εi∑
εi

,

i

Set (Index) of
projects, i ∈ I =
{1, 2, ..., i},
Set (Index) of
scenarios, s ∈ S =
{1, 2, ..., s},

Value for case
study

U(4000,22,000)⋅
(0.01(s-1)+0.99)
U(500,1000)⋅
(0.01(s-1)+0.99)
bacrccis = bacis +
rccis,
U(40,90)/100)⋅
(0.01(s-1)+0.99)
s/(|S| (|S| +1))/2)
100,000

10
80

[U(50,100)]
[U(200,300)]
remduris =
duris(1 (cid:0) pris),
1/ |I|

25

Based on
formulation

Unit

Dollar

Dollar

Dollar

Percent

Percent
Dollar

Percent
Percent

Person
Days
Days

Percent

Percent

Percent

∑
εi

0.6

i
10, 20, 70

Person

Percent

ocu

Minimum occupation for projects,

ω1, ω2,
ω3

Weight factor for VaR, CVaR, EVaR.

Fig. 2. S3RBAP.

4

R. Lotfi et al.

Results in Engineering 24 (2024) 102828

Decision variables:
Continues and positive variables.

xi

Budget assignment for project i,

Free variables.

wprBap
is

Weighted progress of project i under scenario s based on assigning
budget,
Progress of project i under scenario s after assigning budget,

prBap
is
bb
Z
Γ
Γʹ
s
ΓΓ
WVaR(ε) Weighted VaR, CVaR and EVaR by normal distribution.

Summation of budget assignment,
Objective function (progress function),
Minimum of the physical percent complete,
The expected value of the physical percent complete under scenario s,
The expected value of the physical percent complete,

VaR, CVaR, and EVaR based on a normal distribution assumption [34,
35]. Constraints (3), (4), and (5) represent Mean Absolute Deviation
(MAD), minimum progress, and expected progress values across all
scenarios. Constraints (6) explain the average progress of project i.
Constraints (7) and (8) state a weighted and simple form of the progress
of project i under scenario s based on assigning a budget that is a linear
form. Constraints (9) determine that each budget assignment for every
project is less than budget at completion with remaining contractors’
claims under scenario s. Constraints (10) are the summation of budget
assignments based on the mathematical model. Constraints (11) guar-
antee summation of budget assignment less than total budget with
resiliency approach and disruption. Constraints (12) guarantee that the
amount of employment created is greater than the threshold as a sus-
tainability constraint. Constraints (13) are positive, and the budget
assignment for the project i..

3.1. Mathematical model

3.2. Linearization of min and sign function (Preliminary)

maximize Z = (1 (cid:0) β)ΓΓ + β

(Γʹʹ + WVaR(ε))
2

,

subject to:
Progress constraints:

(

WVaR(ε) = ΓΓ +

ω1z1(cid:0) α + ω2

σ =

∑

pps

s

⃒
⃒ΓΓ (cid:0) Γʹ

s

⃒
⃒,

√

̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅
(cid:0) 2α ln(α)

+ ω3

)

σ,

ϕ(z1(cid:0) α)
α

Γʹʹ = min

(cid:0)

)
, ∀s,

Γʹ

s

s
∑

ΓΓ =

ppsΓʹ

s

,

s
∑

wprBap
is

i

, ∀s,

Γʹ

s

=

wprBap
is

= wiprBap

is

, ∀i, s,

Budget constraints:

prBap
is

= xis

bacrccis

(1 (cid:0) pris) + pris, Type 1
Linear

∀i, s,

xi ≤ bacrccis, ∀i, s,

Resiliency constraint in the budget:

∑

xi = bb,

i

bb ≤ δMBud,

Sustainability constraint (occupation level):

∑

εisgn(xi) ≥ ocu,

i

Decision variables:

xi ≥ 0, ∀i,

(1)

(2)

(3)

(4)

(5)

(6)

(7)

(8)

(9)

(10)

(11)

(12)

(13)

As can be seen, paying attention to robustness, uncertainty, and risk
requires us to consider the occurrence probabilities of different scenarios
in the objective function. The objective function (1) aims to optimize the
expected value, WVaR, and minimize the physical percentage comple-
tion. This novel function aims to manage fluctuations in progress by
considering scenarios, risks, and robustness. In addition, the conserva-
tism coefficient (β) is applied in the objective function (1). The formu-
lation of WVaR is outlined in constraints (2), which introduce WVaR as a
novel comprehensive risk assessment criterion comprising weighted

The constraints (3), (5), and (12) are structured as Mixed Integer
Non-Linear Programming (MINLP). To efficiently and promptly enhance
the solution, these constraints need to be transformed into MILP through
operational research techniques. This optimization process aims for a
smooth improvement within a short timeframe. Linearization tech-
niques have been utilized to expedite the resolution of the model based
on these equations [36–38].

Nonlinear constraints

Change to linear constraints (form)

ε = min

(ζs),

s

= sgn(Ωi),

βi
Ωi ≥ 0,
βi

∈ {0, 1}.

ki = |Ωi|,

ε ≤ ζs

, ∀s ∈ S.

βi

≤ 1 +

Ωi
Mbig

(cid:0) eps, ∀i ∈ I,

≥

βi

Ωi
Mbig

, ∀i ∈ I.

(14)

(15)

(16)

ki = αi + βi

, ki = αi (cid:0) βi

, αi, βi

≥ 0, ∀i.

(17)

3.3. Linearization of S3RBAP

In the previous section, constraints (3), (5) and (12) were converted
from the NLP form to the LP form through equations (18)-(23) by line-
arzation approach that is defined in equations of (14) to (17). This one-
stage process, aimed at improving computational time, was discussed by
Lotfi, Kargar, Gharehbaghi, & Weber [39]. To linearize the model, co-
variate variables have been introduced for nonlinear functions such as
absolute values and the multiplication of binary and positive variables
[40,41].

Linearization of S3RBAP

maximize Z = (1 (cid:0) β)ΓΓ + β

(Γʹʹ + WVaR(ε))
2

,

subject to:
∑

pps(vas + vbs),

σ =

s

ΓΓ (cid:0) Γʹ

s

= vas (cid:0) vbs, ∀s,

Γʹʹ ≤ Γʹ

s

, ∀s,

∑

εiyi ≥ ocu,

i

yi ≤ 1 + xi
Mbig

(cid:0) eps, ∀i,

5

(18)

(19)

(20)

(21)

(22)

R. Lotfi et al.

yi ≥ xi
Mbig

, ∀i,

Constraints (2), (4), (6) to (11), (13).

3.4. Complexity of the main problem

(23)

Results in Engineering 24 (2024) 102828

The problem scale (S3RBAP) is obtained from equations (24)–(27) in
the mathematical model. All variables and constraints of different kinds
are determined. It is noticeable that positive free variables and con-
straints differ based on the scenario and timeframe. Based on formula-
tion, two sets are defined that do not increase the scale of the model on a
large scale. Therefore, commercial solvers can solve the model in a
minimum timeframe. But it is suggested to solve the model exact algo-
rithm types like Lagrange relaxation and Bender decomposition:

No. of Binary variables = |I|,

No. of Positive variables = |I| + 2|S|,

No. of Free variables = 8 + |S|(3|I| + 1),

No. of Constraints = 8 + |S|(3 + 4|I|) + 2|I|.

3.5. Functions for progress curve (S-curve)

(24)

(25)

(26)

(27)

As is known, it is assumed that the project’s progress remains linear
based on the budget assignment in our formulation. This assumption
results in the model being considered Linear Programming (LP) (see
Fig. 3). Consequently, the removal of this assumption and its replace-
ment with a nonlinear function in this section transforms the model into
NLP as described by constraints (28) to (32). Therefore, the structure of
constraint (8) can be replaced by constraints (28) or (29) or (30) or (31)
or (32) by risk type. Eventually, the model must be solved using heu-
ristic, metaheuristic, or other solutions to minimize time in equations
(33)–(37). S-curve functions for the progress curve based on risk level
are suggested as follows.

Fig. 3. S-curve functions for progress curve based on risk level.

maximize Z = (1 (cid:0) β)ΓΓ + β (Γʹʹ+WVaR(ε))
Subject to:
(

)

2

, Model name

(1 (cid:0) pris) + pris, n = 1 T1 ∀i, s,

(33)

n

xis
bacrccis

prBap
is

=

or

prBap
is

=

)
n

xis

(
bacrccis (cid:0) 1
e
e (cid:0) 1

(1 (cid:0) pris) + pris, n = 1 T2 ∀i, s,

(34)

or

(

((

prBap
is

=

ln

)

xis
bacrccis

))
n

(e (cid:0) 1) + 1

(1 (cid:0) pris) + pris, n = 1 T3 ∀i, s,

(35)

Functions

f1(x) = xn, 0 ≤ x ≤ 1,

(28)

Name

T1 (Linear)

Risk type
0 ≤ n < 1
Risk-seeking

n = 1
Risk-neutral

n > 1
Risk-averse

(

)n

f2(x) =

ekx (cid:0) 1
ek (cid:0) 1
0 ≤ x ≤ 1, k ∈ R;

T2 (Exponential)

Risk-seeking

Risk-seeking

Risk-averse

,

(29)

T3 (Logarithm)

Risk-seeking

Risk-seeking

Risk-averse

f3(x) = (ln(x(e (cid:0) 1) + 1))n,
0 ≤ x ≤ 1,

(30)

(

f4(x) =

sin

0 ≤ x ≤ 1,

))n

,

(π
2

x

n

,

f5(x) =

)
(
x + sin(kπx)
kπ
ʹ + 1,
0 ≤ x ≤ 1, k = 2k
ʹ ∈ N;
k

(31)

(32)

T4 (Sine)

Risk-seeking

Risk-seeking

Risk-seeking with distortion,

T5 (Linear + Sine)

Risk-seeking with distortion

Risk-neutral with distortion

Risk-averse with distortion

6

R. Lotfi et al.

Results in Engineering 24 (2024) 102828

Table 2
Specification and results of the case study.

Problem

|I||S|

No. of Variables

Binary

Positive

P1

8⋅3

8

14

Free

83

No. of Constraints

Progress function (percent)

Occupation (person)

Time computation (second)

129

86.4 %

498

0.225

Table 3
Assigning budget for national projects by the S3RBAP.

Constraints (2), (4), (6) to (11), (13).

Budget assignment (xi)

4. Results and discussion

Project 1
Project 2
Project 3
Project 4
Project 5
Project 6
Project 7
Project 8

i = 1
i = 2
i = 3
i = 4
i = 5
i = 6
i = 7
i = 8

Problem

P1

Total

or

5730.3
14909.5
7094.9
8969.7
7261.6
7407.4
8895.4
6532.1
66800.8

(

(

prBap
is

=

sin

)))
n

(

xis
bacrccis

π

2

or

(1 (cid:0) pris) + pris, n = 1 T4 ∀i, s,

(36)

Managers in Iran survey and estimate the parameters of national
projects for S3RBAP. The performance of the mathematical model and
estimated parameters is demonstrated based on managers for real pro-
jects. The number of indices of the primary model (P1) is defined in
Table 2, and government managers assign the parameters in the notation
list. In this case, seven projects with three scenarios are involved. The
computer system was configured as Intel(R) Core (TM) i5-4210U CPU @
1.70 GHz 2.40 GHz, 16.0 GB RAM, 64-bit operating system, and x64-
based processor. The primary model was solved with the GAMS-
CPLEX solver. The project budget was distributed in central and other
provinces (see Fig. 4). The probability of occurrence is based on the
optimistic, pessimistic, and possible scenarios proposed by managers

⎛

(

⎜
⎜
⎝

prBap
is

=

(

(

))

⎞
n

xis
bacrccis

)

sin

kπ

+

xis
bacrccis
kπ

⎟
⎟
⎠

(1(cid:0) pris)+pris,n=1,k=3 T5 ∀i,s,

(37)

Fig. 4. National projects for the S3RBAP.

7

R. Lotfi et al.

Results in Engineering 24 (2024) 102828

Fig. 5. Assigning budget for national projects by the S3RBAP.

Table 4
Comparing P1- S3RBAP and without risk and resilience.

Problem

P1- S3RBAP
P1- S3RBAP (without

scenario, resiliency and
conservatism)

GAP

Progress
function
(Percent)

86.4 %
98.1 %

Occupation
(person)

498
599

Time
computation
(Second)

0.225
0.211

13.5 %

20.3 %

(cid:0) 6.2 %

with the same value. The pessimistic, probable, and optimistic events
are suggested to have a probability of occurrence of 33 %. After running
the model and assigning the budget to the project, it is observed that the
objective function, which is determined as the progress function
(percent), is 86.4 % in Table 2, and the final BA is depicted in Table 3
and Fig. 5. In each scenario, an exact value is present, not a randomized
value; therefore, the value of parameters does not change in every run.
A hybrid format incorporates the mean, min function, and WVaR of
progress to define conservatism and a robust approach. This format is
made robust by adding the coefficient of every section.

If each national project receives the budget based on a mathematical

Table 5
Variation of conservatism coefficient.

approach, the total progress is 86.4 %, as seen in Table 2.

4.1. Comparing the proposed model

Ultimately, S3RBAP is compared with the scenario that excludes the
consideration of scenario, resiliency, and conservatism in Table 5. When
sustainability and 3R are utilized, it is observed that the performance
function is decreased by 86.4 % and 13.5 % compared to when scenario,
resiliency, and conservatism are not considered (see Table 4 and Fig. 6).

4.2. Analysis of the conservatism coefficient

In this section, conservative decision-makers vary the conservatism
coefficient (β) as a parameter. When transitioning between 0 % and 20
%, if the conservatism coefficient is increased to 20 %, the progress
function decreases in Table 5, Figs. 7 and 8. When the conservatism
coefficient is elevated to 10 %, the progress function is reduced to 0.58
%, while the time computation experiences a slight change, and the
occupation of projects is not changed.

Problem

P1
P1
P1-main
P1
P1

Conservatism coefficient (β)

Progress function (percent)

Occupation (person)

Time computation (second)

Variation

0 %
5 %
10 %
15 %
20 %

86.9 %
86.7 %
86.4 %
86.2 %
85.9 %

498
498
498
498
498

8

0.255
0.205
0.225
0.255
0.26

0.58 %
0.35 %
0.00 %
(cid:0) 0.23 %
(cid:0) 0.58 %

R. Lotfi et al.

Results in Engineering 24 (2024) 102828

Fig. 6. Comparing the proposed model.

Fig. 9. Analysis of resiliency coefficient for the progress function.

Fig. 7. Analysis progress function based on the conservatism coefficient.

Fig. 10. Analysis of resiliency coefficient on time computation.

Table 6
Analysis of resiliency coefficient.

Problem

Resiliency
coefficient
(δ)

Progress
function
(percent)

Occupation
(person)

Time
computation
(second)

P1-

main

60 %
70 %
80 %

90 %
100 %

85.1 %
86.4 %
86.4 %

86.4 %
86.4 %

438
498
498

498
498

0.265
0.205
0.225

0.205
0.249

Variation

(cid:0) 1.50 %
0.00 %
0.00 %

0.00 %
0.00 %

Fig. 8. Analysis time computation based on the conservatism coefficient.

4.3. Analysis of resiliency coefficient

This part modifies the resiliency coefficient (δ) as a factor influencing
resilience to budget allocation distribution. A decrease in the resiliency
coefficient leads to a decrease in the progress function. Lowering the

resiliency coefficient reduces and disturbs the budget allocation process,
leading to decreased progress function and increased occupation of
projects (see Figs. 9 and 10, and Table 6).

4.4. Analysis of the scale of main model

Several large-scale problems are defined in Table 7. It can be
observed that with an increase in the scale of problems, the time

9

R. Lotfi et al.

Results in Engineering 24 (2024) 102828

Table 7
Progress and time computation for large-scale problems.

Problem

|I||S|

No. of Variables

No. of Constraints

Progress function (percent)

Occupation (person)

Time computation (second)

P1
P2
P3
P4
P5

Binary

Positive

8⋅3
20⋅5
40⋅7
60⋅7
100⋅9

8
20
40
60
100

14
30
54
74
118

Free

83
313
855
1275
2717

129
463
1229
1829
3835

86.4 %
84.70 %
80.10 %
79.20 %
77.60 %

498
1202
1866
2800
4774

0.225
0.192
0.2
0.309
0.302

Fig. 11. Progress function for large-scale problems.

Fig. 12. Time computation for large-scale problems.

computation shows a smooth growth, and the progress function de-
creases, as depicted in Figs. 11 and 12. Due to the high number of
projects, the maximization of the expected value of the progress function
is reduced. Project occupation has increased.

4.5. Analysis of the project’s remaining progress function (S-curve)

In this section, we change the project’s remaining progress function
based on BA (S-curve function). to a nonlinear function. As a result, this
model changed to NLP. S-curve functions for the progress curve based on

10

Fig. 13. Analysis of progress function types on progress.

risk level are computed as follows (see Table 8, Figs. 13 and 14). The
results show that utilizing the exponential function makes it risk-averse,
and the sine function makes it risk-seeking in this research.

4.6. Discussion

After reviewing the existing literature, a research gap in BAP was
identified. As a result, it is necessary to establish a mathematical model
to develop S3RBAP. This study area is new and has not been explored
previously, marking the first instance of such a mathematical model
being formulated for BAP.

Despite efforts made by Jemmali [19], Lotfi et al. [1], and Yu et al.
[22] to address the identified research gap, none of them incorporated
3R and sustainability. This study aims to fill this gap by integrating 3R
and sustainability. A comprehensive model is required that highlights
robustness, resilience to budget disturbances, and risk mitigation. This
model optimizes allocating a specific budget among projects, intro-
ducing a unique approach that merges BAP with 3R and sustainability. A
sensitivity analysis is employed to demonstrate the model’s performance
across different scenarios, comparing it to a scenario that does not
consider 3R and sustainability.

Additionally, an examination of S3RBAP is carried out to investigate
variations in the conservatism coefficient, resilience coefficient, and the
effects of the scale problem and different progress function estimations.
This model is proposed as a solution for BAP, delivering an optimal
outcome and integrating robust stochastic optimization to tackle un-
certainties and risks. The sensitivity analysis results reveal that incor-
porating 3R and sustainability leads to a 13.5 % decrease in the progress
function compared to not considering them. Moreover, increasing the
conservatism coefficient by 10 % results in a 0.58 % reduction in the

R. Lotfi et al.

Results in Engineering 24 (2024) 102828

Table 8
Analysis of the project’s remaining progress function (S-curve).

Model
Name

T2
T5
T1 (P1)
T3
T4

Exponential
Linear + Sine
Linear
Logarithm
Sine

Setting

n = 1, k = 1
n = 1, k = 3
n = 1
n = 1
n = 1

|I||S|

8.3
8.3
8.3
8.3
8.3

Progress function (percent)

Occupation (person)

Time computation (second)

82.9 %
83.60 %
86.4 %
89.70 %
92.40 %

498
379
498
498
498

0.285
0.283
0.225
0.277
0.275

allocation, it is crucial and impacts people’s lives, enhancing social
outcomes. The BAP issue should receive increased attention from project
and senior managers. Emphasizing 3R and sustainability in the reen-
gineering of BAP is deemed essential for better economic and political
considerations than previously, necessitating an increased focus on
occupation. This study examines BAP for the first time, integrating the
3R and sustainability approach. It is recommended that managers and
researchers incorporate mathematical models to facilitate and make
optimal decisions. With the application of this model, managers can
enhance people’s lives and expedite project completion by making
informed decisions and conducting expert work. Consequently, we
advocate adopting this innovative model across all portfolio projects to
allocate budgets for medium- and large-scale projects.

6. Conclusions and outlook

A novel insight incorporating sustainability and the 3R approach is
proposed for BAP in this research for the first time. A hybrid robust
stochastic optimization technique was utilized, incorporating WVaR and
the minimum function as risk criteria for ensuring robustness in the
objective function. The objective function was designed to minimize the
weighted expected value, WVaR, and minimum progress function,
advocating for the 3R and sustainability approach to address budget
fluctuations and attract occupation. Ultimately, budgets are allocated to
projects under uncertain scenarios as part of this proposed methodology.

The findings are as follows.

1. S3RBAP is compared with the scenario that excludes the consider-
ation of scenario, resiliency, and conservatism in Table 5. When
sustainability and 3R are utilized, it is observed that the performance
function is decreased by 86.4 % and 13.5 % compared to when
scenario, resiliency, and conservatism are not considered (see
Table 4).

2. Conservative decision-makers vary the conservatism coefficient (β)
as a parameter. When transitioning between 0 % and 20 %, if the
conservatism coefficient is increased to 20 %, the progress function
decreases in Table 5, Figs. 7 and 8. When the conservatism coeffi-
cient is elevated to 10 %, the progress function is reduced to 0.58 %,
while the time computation experiences a slight change, and the
occupation of projects is not changed.

3. The resiliency coefficient (δ) influences resilience to budget alloca-
tion distribution. A decrease in the resiliency coefficient leads to a
decline in the progress function. Lowering the resiliency coefficient
reduces and disturbs the budget allocation process,
leading to
decreased progress function and increased project occupation (see
Figs. 10 and 13, and Table 6).

4. Several large-scale problems are defined in Table 7. It can be
observed that with an increase in the scale of problems, the time
computation shows a smooth growth, and the progress function de-
creases, as depicted in Figs. 11 and 12. Due to the high number of
projects, the maximization of the expected value of the progress
function is reduced. The occupation of projects has increased.

5. The project’s progress function is changed to a nonlinear one,
resulting in this model changing to NLP. S-curve functions for the
progress curve based on risk level are computed as follows (see

Fig. 14. Analysis of progress function types on time computation.

progress function, with minimal changes in computation time. Lowering
the resilience coefficient negatively impacts progress and project
completion. As the scale of problems increases, computation time rises
steadily while the progress function decreases. Maximizing the expected
value of the progress function declines significantly as the number of
projects grows. The findings suggest that using an exponential function
promotes risk-averse behaviour, whereas a sine function underscores
risk-seeking tendencies in this research.

5. Managerial insights and practical implications

An integrated approach that considers risks, robustness, resiliency,
and sustainability requirements should be considered when allocating
project budgets. Comprehensive risk assessments should be conducted
to identify and mitigate potential threats to sustainability goals. Budgets
should be developed to withstand uncertainties and changes, ensuring
that sustainability objectives are not compromised. Resources should be
strategically allocated to enhance the project’s ability to adapt to
changing conditions while maintaining sustainable practices. Long-term
sustainability implications should be considered when making budget
decisions to prevent short-term gains from impacting long-term sus-
tainability. Stakeholders should be involved in aligning with their
values, and monitoring and evaluation mechanisms should be imple-
mented to track impacts and make necessary adjustments. Innovation,
efficiency, transparency, and accountability should be encouraged to
optimize sustainability outcomes. A culture of continuous improvement
should be fostered to enhance overall project sustainability.

BAP is considered one of the critical factors in project completion on
time. It is observed that when national projects have a significant budget

11

R. Lotfi et al.

Results in Engineering 24 (2024) 102828

Table 8, Figs. 13 and 14). The results show that utilizing the expo-
nential function makes it risk-averse, and the sine function makes it
risk-seeking in this research.

One of the research constraints involves the resolution of the
nonlinear progress remaining function as a S-curve function model. Due
to the presence of MINLP, a recommendation is made to consider the
utilization of a new exact algorithm, such as heuristic and metaheuristic
algorithms, which are deemed suitable for efficiently solving the MINLP
model, thereby achieving near-optimal solutions and establishing lower
and upper bounds [42,43].

Moreover, exploring alternative methods to address uncertainty,
such as fuzzy logic, robust convex optimization, and data-driven robust
optimization, is suggested as an innovative approach for researchers. A
notable contribution to reducing risk can be achieved through the
application of coherent risk criteria [44–46]. Finally, applying RCVaR,
CMARS, RCMARS, and RMARS are helpful for this problem [47].

Ethical approval

Not applicable.

Consent to participate

Not applicable.

Consent to publish

Not applicable.

Funding

There is no funding.

Availability of data and materials

The data and code supporting this study’s findings are available on

request from the authors.

CRediT authorship contribution statement

Reza Lotfi: Writing – review & editing, Writing – original draft,
Visualization, Validation, Supervision, Software, Resources, Project
administration, Methodology,
Investigation, Funding acquisition,
Formal analysis, Data curation, Conceptualization. Masoud Vaseei:
Writing – review & editing, Validation, Software, Methodology. Sadia
Samar Ali: Writing – review & editing, Validation, Software, Method-
ology. Sayyed Mohammad Reza Davoodi: Writing – review & editing,
Methodology. Mansour Bazregar: Writing – review & editing, Meth-
odology. Soheila Sadeghi: Methodology, Writing – review & editing.

Declaration of competing interest

The authors declare that they have no known competing financial
interests or personal relationships that could have appeared to influence
the work reported in this paper.

Data availability

Data will be made available on request.

References

[1] R. Lotfi, E. Haqiqat, M.S. Rajabi, A. Hematyar, Robust and resilience budget

allocation for projects with a risk-averse approach: a case study in healthcare
projects, Comput. Ind. Eng. 176 (2023) 108948.

12

[2] A.K. Umrawal, V. Aggarwal, C.J. Quinn, Fractional budget allocation for influence
maximization, in: Paper Presented at the 2023 62nd IEEE Conference on Decision
and Control (CDC), 2023.

[3] L. Alkhattabi, A. Alkhard, A. Gouda, Effects of change orders on the budget of the
public sector construction projects in the kingdom of Saudi Arabia, Results in
Engineering 20 (2023) 101628.

[4] R. Lotfi, P. MohajerAnsari, M.M.S. Nevisi, M. Afshar, S.M.R. Davoodi, S.S. Ali,
A viable supply chain by considering vendor-managed-inventory with a
consignment stock policy and learning approach, Results in Engineering 21 (2024)
101609.

[5] D. Meng, H. Yang, S. Yang, Y. Zhang, A.M. De Jesus, J. Correia, S.-P. Zhu, Kriging-
assisted hybrid reliability design and optimization of offshore wind turbine support
structure based on a portfolio allocation strategy, Ocean Eng. 295 (2024) 116842.
[6] D. Meng, S. Yang, A.M. De Jesus, T. Fazeres-Ferradosa, S.-P. Zhu, A novel hybrid
adaptive Kriging and water cycle algorithm for reliability-based design and
optimization strategy: application in offshore wind turbine monopile, Comput.
Methods Appl. Mech. Eng. 412 (2023) 116083.

[7] S. Yang, D. Meng, H. Wang, C. Yang, A novel learning function for adaptive

surrogate-model-based reliability evaluation, Philosophical Transactions of the
Royal Society A 382 (2264) (2024) 20220395.

[8] Y. Abukhalil, O. Smadi, A bootstrap-based integer programming algorithm for

budget allocation in pavement management systems, J. Infrastruct. Syst. 28 (1)
(2022) 04021056.

[9] X. Ding, J. Guo, D. Li, W. Wu, Pricing and budget allocation for IoT blockchain with

edge computing, IEEE Trans. Cloud Comput. 11 (2) (2022) 1608–1621.
[10] D. Meng, S. Yang, A.M. de Jesus, S.-P. Zhu, A novel Kriging-model-assisted

reliability-based multidisciplinary design optimization strategy and its application
in the offshore wind turbine tower, Renew. Energy 203 (2023) 407–420.

[11] D. Meng, S. Yang, H. Yang, A.M. De Jesus, J. Correia, S.-P. Zhu, Intelligent-inspired
framework for fatigue reliability evaluation of offshore wind turbine support
structures under hybrid uncertainty, Ocean Eng. 307 (2024) 118213.

[12] Z. Gao, R.Y. Liang, T. Xuan, VIKOR method for ranking concrete bridge repair

projects with target-based criteria, Results in Engineering 3 (2019) 100018.

[13] H. Xiao, F. Gao, L.H. Lee, Optimal computing budget allocation for complete
ranking with input uncertainty, IISE Transactions 52 (5) (2020) 489–499.
[14] C. Song, R. Kawai, Dynamic finite-budget allocation of stratified sampling with
adaptive variance reduction by strata, SIAM J. Sci. Comput. 45 (2) (2023)
A898–A932.

[15] D. Zeqiraj, Enhanced oil recovery (EOR) project scheduling with multiobjective of

maximum net present value and minimum makesapn, Results in Engineering 13
(2022) 100339.

[16] M.A. Musarat, W.S. Alaloul, S.M.B. Zainuddin, A.H. Qureshi, A. Maqsoom,

Digitalization in malaysian construction industry: awareness, challenges and
opportunities, Results in Engineering (2024) 102013.

[17] M.M.A. Oda, B.A. Tayeh, S. Alhammadi, Y.I.A. Aisheh, Key indicators for

evaluating the performance of construction companies from the perspective of
owners and consultants, Results in Engineering 15 (2022) 100596.

[18] Y. Fu, H. Xiao, L.H. Lee, M. Huang, Stochastic optimization using grey wolf

optimization with optimal computing budget allocation, Appl. Soft Comput. 103
(2021) 107154.

[19] M. Jemmali, An optimal solution for the budgets assignment problem, Oper. Res.

55 (2) (2021) 873–897.

[20] Y. Shi, Y. Xiang, H. Xiao, L. Xing, Joint optimization of budget allocation and

maintenance planning of multi-facility transportation infrastructure systems, Eur.
J. Oper. Res. 288 (2) (2021) 382–393.

[21] K. Zhang, J. Tian, H. Xiao, Y. Zhao, W. Zhao, J. Chen, A numerical splitting and
adaptive privacy budget-allocation-based LDP mechanism for privacy preservation
in blockchain-powered IoT, IEEE Internet Things J. 10 (8) (2022) 6733–6741.

[22] C. Yu, N. Lahrichi, A. Matta, Optimal budget allocation policy for tabu search in
stochastic simulation optimization, Comput. Oper. Res. 150 (2023) 106046.
[23] G. Kou, H. Xiao, M. Cao, L.H. Lee, Optimal computing budget allocation for the

vector evaluated genetic algorithm in multiobjective simulation optimization,
Automatica 129 (2021) 109599.

[24] A.S. Uysal, X. Li, J.M. Mulvey, End-to-end risk budgeting portfolio optimization

with neural networks, Ann. Oper. Res. (2023) 1–30.

[25] H. Aziz, N. Shah, Participatory budgeting: models and approaches, Pathways

Between Social Science and Computational Social Science: Theories, Methods, and
Interpretations (2021) 215–236.

[26] P. Bouzari, B. Gyenge, P. Ebrahimi, M. Fekete-Farkas, Problem solving and budget
allocation of SMEs: application of NCA approach, Computation 11 (3) (2023) 48.

[27] H. Jang, A decision support framework for robust R&D budget allocation using
machine learning and optimization, Decis. Support Syst. 121 (2019) 1–12.

[28] A. Ghazi, F.H. Lotfi, Assessment and budget allocation of Iranian natural gas

distribution company-A CSW DEA based model, Soc. Econ. Plann. Sci. 66 (2019)
112–118.

[29] R. Lotfi, R. Hazrati, S. Aghakhani, M. Afshar, M. Amra, S.S. Ali, A data-driven

robust optimization in viable supply chain network design by considering Open
Innovation and Blockchain Technology, J. Clean. Prod. 436 (2024) 140369.
[30] L. Yang, J. Lou, X. Zhao, Risk response of complex projects: risk association

network method, J. Manag. Eng. 37 (4) (2021) 05021004.

[31] Y. Zhang, X. Guan, Budget allocation decisions for project risk response,

Kybernetes 50 (12) (2021) 3201–3221.

[32] R. Lotfi, A. Khanbaba, S.S. Ali, M. Afshar, M.S. Mehrjardi, S. Omidi, Net-zero,
resilience, and agile closed-loop supply chain network design considering
robustness and renewable energy, Environ. Sci. Pollut. Control Ser. (2024) 1–19.

R. Lotfi et al.

Results in Engineering 24 (2024) 102828

[33] R. Sisto, J. García L´opez, A. Quintanilla,

´
A. de Juanes, D. Mendoza, J. Lumbreras,
C. Mataix, Quantitative analysis of the impact of public policies on the sustainable
development goals through budget allocation and indicators, Sustainability 12 (24)
(2020) 10583.

[34] R. Lotfi, A. Khanbaba, H.A. Alkhazaleh, M. Changizi, M. Kadłubek, S. Aghakhani,
S. SamarAli, A viable supplier selection with order allocation by considering
robustness, risk-averse and blockchain technology, Comput. Ind. Eng. (2024)
110319.

[35] R. Lotfi, N. Mardani, S.S. Ali, S.M. Pahlevan, S.M.R. Davoodi, A robust and risk-

averse medical waste chain network design by considering viability requirements,
Oper. Res. 58 (2) (2024) 1473–1497.

[40] M. Atsmony, G. Mosheiov, Minimizing total completion time with linear

deterioration: a new lower bound, Comput. Ind. Eng. 163 (2022) 107867.
[41] M.M. Azar, M.A.S. Monfared, S.E. Monabbati, Non-cooperative two-player games
and linear bi-objective optimization problems, Comput. Ind. Eng. 162 (2021)
107665.

[42] R. Lotfi, Z. Sheikhi, M. Amra, M. AliBakhshi, G.-W. Weber, Robust optimization of
risk-aware, resilient and sustainable closed-loop supply chain network design with
Lagrange relaxation and fix-and-optimize, Int. J. Logist. Res. Appl. (2021) 1–41.

[43] W. Peng, J. Zhang, L. Chen, A bi-objective hierarchical program scheduling
problem and its solution based on NSGA-III, Ann. Oper. Res. (2021) 1–26.
[44] E. Kropat, G.W. Weber, Fuzzy target-environment networks and fuzzy-regression

[36] F. Glover, Improved linear integer programming formulations of nonlinear integer

approaches, Numer. Algebra Control Optim. 8 (2) (2018) 135.

problems, Manag. Sci. 22 (4) (1975) 455–460.

[37] I.A. Gondal, M.H. Sahir, Model for biomass-based renewable hydrogen supply

chain, Int. J. Energy Res. 37 (10) (2013) 1151–1159.

[38] H.D. Sherali, W.P. Adams, A Reformulation-Linearization Technique for Solving
Discrete and Continuous Nonconvex Problems, vol. 31, Springer Science &
Business Media, 2013.

[39] R. Lotfi, B. Kargar, A. Gharehbaghi, G.-W. Weber, Viable medical waste chain

[47] A.

[45] R. Lotfi, B. Kargar, A. Gharehbaghi, M. Afshar, M.S. Rajabi, N. Mardani, A data-
driven robust optimization for multiobjective renewable energy location by
considering risk, Environ. Dev. Sustain. (2022) 1–22.

[46] R. Lotfi, K. Kheiri, A. Sadeghi, E. Babaee Tirkolaee, An extended robust

mathematical model to project the course of COVID-19 epidemic in Iran, Ann.
Oper. Res. (2022) 1–25.

¨
Ozmen, ˙I. Batmaz, G.-W. Weber, Precipitation modeling by polyhedral RCMARS

network design by considering risk and robustness, Environ. Sci. Pollut. Control
Ser. (2021) 1–16.

and comparison with MARS and CMARS, Environ. Model. Assess. 19 (2014)
425–435.

13

