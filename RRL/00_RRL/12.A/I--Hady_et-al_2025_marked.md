Artificial Intelligence Review (2025) 58:354
https://doi.org/10.1007/s10462-025-11340-5

Multi-agent reinforcement learning for resources allocation
optimization: a survey

Mohamad A. Hady1 · Siyi Hu1 · Mahardhika Pratama1 · Zehong Cao1 ·
Ryszard Kowalczyk1,2

Accepted: 29 July 2025 / Published online: 27 August 2025
© The Author(s) 2025

Abstract
Multi-Agent  Reinforcement  Learning  (MARL)  has  become  a  powerful  framework  for
numerous  real-world  applications,  modeling  distributed  decision-making  and  learning
from  interactions  with  complex  environments.  Resource Allocation  Optimization  (RAO)
benefits significantly from MARL’s ability to tackle dynamic and decentralized contexts.
MARL-based approaches are increasingly applied to RAO challenges across sectors play-
ing  a  pivotal  role  in  industry  4.0  developments.  This  survey  provides  a  comprehensive
review of recent MARL algorithms for RAO, encompassing core concepts, classifications,
design  steps  and  benchmarks.  By  outlining  the  current  research  landscape  and  identify-
ing primary challenges and future directions, this survey aims to support researchers and
practitioners in leveraging MARL’s potential to advance resource allocation solutions.

Keywords  Multi-agent reinforcement learning · Resource allocation optimization

  Siyi Hu

siyi.hu@unisa.edu.au

Mohamad A. Hady
mohamad.hady@mymail.unisa.edu.au

Mahardhika Pratama
dhika.pratama@unisa.edu.au

Zehong Cao
jimmy.cao@unisa.edu.au

Ryszard Kowalczyk
ryszard.kowalczyk@unisa.edu.au

1

2

STEM, University of South Australia, Mawson Lakes Blvd, Mawson Lakes, SA
5095, Australia

Systems Research Institute, Polish Academy of Sciences, Warsaw, Poland

1 3

354  Page 2 of 49

1  Introduction

Multi-agent  reinforcement  learning  (MARL)  has  quickly  become  an  essential  area  of
research,  providing  effective  solutions  for  distributed  decision-making  in  dynamic  and
decentralized environments. As multiple agents interact and learn in shared settings, MARL
addresses the complexities of real-world applications, especially in situations with non-sta-
tionary and evolving conditions (Ning and Xie 2024; Hao et al. 2023; Nguyen et al. 2020).
In  parallel,  Resource Allocation  Optimization  (RAO)  has  gained  significant  attention,  as
optimizing resource distribution–such as time, energy, network bandwidth, and computa-
tional power–can enhance efficiency and effectiveness across a variety of fields (Sharma and
Yoon 2018; Wei et al. 2021; Sharma and Wonsik 2021; Allahham et al. 2022).

MARL  is  particularly  suited  to  tackling  RAO  challenges,  as  it  enables  decentralized,
adaptive  decision-making.  This  ability  is  critical  in  industries  like  telecommunications,
energy  management,  cloud  computing,  and  transportation,  where  efficient  resource  man-
agement plays a vital role (Hwang et al. 2025; Wong et al. 2023; Zabihi et al. 2023). For
example, in cloud computing, MARL-based algorithms can optimize resource scheduling
and load balancing, leading to improved system performance and reduced costs. Similarly,
global supply chains benefit from efficient resource allocation, boosting productivity and
reducing  expenditures  (Jiang  and  Sheng  2009;  Ren  et  al.  2022).  In  power  grids,  where
renewable  energy  sources  are  increasingly  integrated,  MARL  enables  dynamic  energy
resource allocation to balance supply and demand (Zhang et al. 2023). Transportation net-
works also leverage MARL’s adaptive capabilities, with applications such as traffic signal
control in cities to alleviate congestion and reduce emissions (Wu et al. 2020). A generic
illustration of MARL solution for RAO framework is provided in Fig. 1 that describes how
any resources are allocated to a certain task or activity with multi-agent decision makers.

Agent-1

Agent-2

Agent-N

Policy

Policy

Policy

Action

Action

Action

Allocating
Resource

Rewards

Observations

ENVIRONMENT

Current Task/ Activity

Resources

Remaining
Tasks/ Activities

Fig. 1  MARL solution for RAO. Any resources can be allocated by several agents to complete tasks or
activities. Each agent has its own policy to handle resource allocation determined by the rewards and
observations of the whole system states that may come from resources and tasks situations

M. A. Hady et al.1 3
Page 3 of 49  354

Historically,  RAO  problems  have  been  addressed  through  classical  optimization  and
heuristic methods (Halabian 2019). However, these methods often lack the flexibility and
scalability required in complex, real-time environments Sarah et al. (2023). RL has emerged
as  a  powerful  alternative  for  solving  resource  allocation  problems  (Khani  et  al.  2024;
Deng 2025; Lee et al. 2025). Recent studies have also explored meta-RL and meta-DRL
approaches (Xu and Jian 2024; Lotfi and Afghah 2025), integrating model-agnostic meta-
learning (Finn et al. 2017) to DRL in RAO problem (Rao et al. 2024) aiming to improve
single-agent  adaptability  across  varying  task  settings.  While  these  methods  address  task
generalization in single-agent environments, our focus lies in extending RL to multi-agent
systems. MARL builds on RL by enabling multiple interacting agents to learn and adapt
collaboratively  across  distributed  nodes. This  transition  from  single-agent  to  multi-agent
settings supports more scalable and decentralized solutions, which are essential for address-
ing the increasing complexity of modern RAO scenarios (Lei et al. 2020; Noor-A-Rahim
et al. 2020; Chen et al. 2021).

Despite rising interest in MARL and its RAO applications, there is a lack comprehen-
sive surveys that focus specifically on this intersection. Existing surveys cover related top-
ics–such as RL in energy systems (Yu et al. 2021), task allocation in multi-robot systems
(Orr  and  Dutta  2023),  and  resource  management  in  wireless  networks  (Feriani  and  Hos-
sain  2021)–but  do  not  offer  an  extensive  review  of  MARL-driven  RAO  across  different
industries. Unlike our study, several recent surveys as provided in the Table 1 mostly dis-
cussed RAO only in a specific application field. In fact, many common aspects can be uni-
fied as a general framework to integrate MARL across different RAO application domain as
mainly discussed in our survey. Therefore, this survey fills that gap by providing a focused
review on the use of MARL in RAO, with the following primary contributions:

 ● Mapping  the  current  landscape  of  MARL  algorithms  and  frameworks  used  in  RAO,

providing researchers with a consolidated resource.

 ● Offering a systematic review to synthesize advancements, highlight trends, and identify

challenges and opportunities unique to MARL applications in RAO.

 ● Categorizing recent literature in MARL training frameworks and their application areas.
 ● Listing real-world benchmarks and available testbeds for RL and MARL algorithm de-

Table 1  Comparison of related
survey works with some as-
pects: brief survey of Classical
Approaches (CA); providing
Resources Classifications (RC);
MARL in Diverse Applications
(DA); and Application Fields
(AF) and its total numbers

CA RC DA AF*/Number

✗
✗

Scope
RL + RAO
RL & MARL +
RAO
MARL + RAO ✗
MARL + Task
✗
allocation
MARL + Deci-
sion making

Related Survey
Yu et al. (2021)
Feriani and Hos-
sain (2021)
Li et al. (2022)
Orr and Dutta
(2023)
Ning and Xie
(2024)
Hua et al. (2025) MARL + RAO ✗
MARL + RAO ✗
Zhang et al.
(2025)
Ours

✗

MARL + Gen-
eral RAO

✓

✗
✗

✗
✗

✗

✗
✗

✓

✗
✗

✗
✗

✓

✗
✗

✓

E/1
TN/1

TN/1
R/1

T, E, TN, IP,
CB/5
T/1
TN/1

E, TN, DC,
T, M/5

*Application  Fields:  Energy  (E),  Telecommunication  and  Networks
(TN), Robotics (R), Transportation (T), Image Processing (IP), Chips
and Biochips (CB), Distributed Computing (DC), Manufacturing (M)

Multi-agent reinforcement learning for resources allocation optimization:…1 3
354  Page 4 of 49

velopment in RAO.

This survey is both timely and necessary, serving as a foundational reference for research-
ers  and  practitioners  in  the  field.  By  focusing  on  recent  developments,  selecting  high-
impact  studies,  and  examining  critical  aspects  such  as  non-stationarity,  scalability,  agent
communication,  and  coordination,  we  aim  to  provide  a  comprehensive  overview  of  cur-
rent  MARL  research  in  the  context  of  RAO.  The  remainder  of  this  survey  is  organized
as follows (see Fig. 2): Sect. 2 categorizes types of resources and reviews classical RAO
approaches, including linear programming, heuristic optimization, and game theory. It high-
lights their applications and limitations in dynamic, large-scale, and decentralized systems.
Section 3 introduces the fundamentals of reinforcement learning (RL) and extends them to
multi-agent reinforcement learning (MARL), with a focus on their applicability to decen-
tralized and dynamic RAO scenarios. Section 4 surveys MARL solutions for RAO-related
applications and challenges. It reviews the use of MARL in domains such as telecommu-
nications,  energy  systems,  distributed  computing,  transportation,  and  manufacturing,  and
discusses challenges including dynamic environments, partial observability, scalability, and
resource heterogeneity. This section also examines key frameworks such as CTCE, DTDE,
and CTDE, along with emerging approaches like graph-based MARL. Section 5 introduces
representative benchmarks used to evaluate MARL performance in RAO settings, includ-
ing satellite missions, power grids, container management, and traffic systems. Section 6
outlines future research directions, emphasizing the need for improved scalability, real-time
adaptability,  and  agent  coordination.  Potential  solutions  include  hierarchical  MARL  and
mean-field approximation techniques.

PRELIMINARY AND FUNDAMENTAL

SOLUTION AND APPLICATION

Section I - Introduction

Section IV - RAO Leveraging MARL

The importance of RAO and MARL as
emerging research fields in the
digitalization era
Survey Motivation and Contribution
Paper structure

Section II - Resources Allocation Optimization

Classification of Resources
Principles and Objectives of RAO
Classical Methods in RAO
Challenges in Modern RAO Problems (from
classical approach, solution is in Section
IV)

MARL in Different RAO Application Fields:
Telecommunication Network and IoT
Energy
Distributed Computing
Transportation
Manufacturing

Common Challenges:

Adaptability in Continuously Changing Environments
Coordinating Resources with Partial Observability
Dealing with Large-Scale Systems
Handling Heterogeneity in Resources and Objectives

Section III - Brief Foundation of MARL

Section V - Available Standarized Benchmark

Why MARL Match to Modern RAO
Reinforcement Learning
RL as Optimization
Multi-Agent Reinforcement
Learning

Satellite System
Power Grid
Traffic Management
Waste Management

Section VI - Future Directions and Challenges

Section VII - Conclusion

Fig. 2  Complete manuscript body structure used in this survey: Preliminary section mainly covers the
fundamental of RL and MARL methods. Then, we introduce the concept of RAO, its classical solution
and highlight the challenges in the recent trends which can be solved using MARL algorithm and dis-
cussed in the RAO leveraging MARL section

M. A. Hady et al.1 3
Page 5 of 49  354

2  Resource allocation optimization

Resource  Allocation  Optimization  (RAO)  is  a  significant  area  of  research  across  many
fields, focusing on the challenge of distributing resources among agents or tasks to improve
system efficiency, productivity, or fairness. Resource allocation is the structured distribution
of finite resources among tasks or activities to meet a defined objective, such as efficiency
or cost. This process is fundamental across various fields, including energy management,
cloud  computing,  manufacturing,  and  telecommunications,  etc.  The  effective  allocation
requires identification of available resources, assessment of task demands, and allocation
of resources in a way that aligns with system goals, often under constraints such as time,
budget, or capacity (Feriani and Hossain 2021). The primary objective of RAO is to allo-
cate  resources  as  effectively  as  possible,  balancing  competing  demands  to  optimize  spe-
cific goals, such as minimizing delays, maximizing throughput, reducing costs, or ensuring
fairness among users (Tang et al. 2015; Nair et al. 2018; Binyamin and Ben Slama 2022).
In industries like telecommunications, cloud computing, energy distribution, manufactur-
ing, and transportation, efficient allocation of resources such as bandwidth, computational
power, energy, and physical assets is crucial to maintaining high performance while mini-
mizing  costs  and  reducing  waste. As  systems  become  more  complex  and  interconnected
with advancements like the Internet of Things (IoT) and digitalization in large-scale dis-
tributed systems, the demand for effective resource allocation becomes even more critical.

2.1  Principles and objectives of RAO

Resource location introduces additional complexity in allocation strategies. Non-distributed
resources are concentrated in a single location or managed under a centralized authority.
While these systems minimize communication overhead and latency, they often face scal-
ability  challenges  and  are  susceptible  to  single  points  of  failure.  Conversely,  distributed
resources  are  spread  across  multiple  locations  or  nodes  and  require  coordination  across
interconnected systems. This setup offers scalability, fault tolerance, and flexibility, making
distributed systems ideal for dynamic environments such as cloud computing, multi-robot
coordination, and smart grids. However, distributed systems also pose challenges like com-
munication overhead and coordination latency, necessitating advanced algorithms for effi-
cient resource management (Zhang and Debroy 2023; Huang et al. 2023).

2.1.1  Resource allocation process

In  practice,  resource  allocation  strategies  are  guided  by  specific  characteristics  of  the
resources themselves. For instance, in distributed cloud computing, resources like process-
ing  power  are  spread  across  multiple  servers,  necessitating  allocation  methods  that  bal-
ance load across the network to enhance response times and availability (Jiang 2015). In
contrast, centralized resources in manufacturing, such as machinery, are managed within a
single facility to minimize downtime and improve throughput. For divisible resources, such
as bandwidth in telecommunications, allocations can vary to meet user demand, reducing
latency  and  enhancing  throughput.  Indivisible  resources,  such  as  individual  machines  or
personnel, require discrete allocation, where entire units are assigned based on task require-
ments. Finally, renewable resources, like energy from solar panels, are allocated cyclically

Multi-agent reinforcement learning for resources allocation optimization:…1 3354  Page 6 of 49

to maintain availability without depletion, while non-renewable resources, such as a fixed
budget, require careful allocation to support long-term goals (Wang et al. 2021).

2.1.1.1  Problem formulation  Consider a set of tasks indexed by i, where i = 1, 2, . . . , n.
Let xi denote the amount of resource allocated to the i-th task. The total amount of resource
n
N. Additionally, task-specific limits
i=1 xi ≤
available, N , constrains the allocation as:
on resource allocation, represented by lower and upper bounds li and ui, are applied as:
ui, i = 1, 2, . . . , n. These constraints can be incorporated directly into the opti-
li ≤
mization model, allowing for efficient adjustments according to operational needs.

xi ≤

∑

2.1.2  Objective of RAO

The objective function for RAO, denoted f (x1, x2, . . . , xn), is formulated to achieve opti-
mal resource distribution by minimizing costs or maximizing benefits. This can be repre-
sented as follows (Ibaraki and Katoh 1988; Ushakov 2013):

maximizing f (x1, x2, . . . , xn)

subject to

n

i=1
∑

xi ≤

N,

li ≤

xi ≤

ui, i = 1, 2, . . . , n,

(1)

where N  represents the total available amount of the resource. In cases where the objective
f , as maximizing f  is
is to maximize profit, the problem can be re-framed by minimizing
equivalent to minimizing its negative.

−

The structure of the objective function f (x1, x2, . . . , xn) is often customized to fit the

specific requirements of the application, and it may take various forms (Patriksson 2008):

 ● Separable function: A common structure where the objective is expressed as the sum of

individual cost functions for each resource, such as

 ● Convex  function:  When  each  fi  is  convex,  enabling  the  use  of  convex  optimization

n
i=1 fi(xi).

∑

techniques for efficiency.

 ● Minimax or maximin objectives: In some scenarios, the goal is to minimize the maxi-
mum cost, maxi fi(xi), or maximize the minimum cost, mini fi(xi), which can help
balance resource allocation across tasks.

 ● Fairness-oriented function: A fairness-focused allocation can be achieved by minimiz-
ing a function g(maxi fi(xi), mini fi(xi)), where g is a non-decreasing function, there-
by balancing extremes in resource distribution.

2.2  Resources properties

In  RAO,  the  properties  of  resources  play  a  pivotal  role  in  determining  effective  alloca-
tion  strategies.  Resources  can  be  broadly  classified  by  their  divisibility,  duration,  and
location, each influencing management approach and system design. These classifications
are illustrated in Fig. 3. Discrete resources–such as physical machines, servers, or person-
nel–are indivisible and allocated as whole units. These are typically modeled using Integer

M. A. Hady et al.1 3

Resources

Divisibility

Page 7 of 49  354

Person

Storage box

Machine

Computing

Disk storage

Bandwidth

Discrete:
(Indivisible)

Continuous:
(Divisible)

Availability

Non-renewable :

Oil Fuel

Soil & Mineral

Natural Gas

Solar energy

Wind energy

Water

Renewable :

Location

Non-distributed

Distributed

Fig. 3  Resource classification by divisibility, availability, and location properties

Z

R

≥

Programming (IP), where the resource variable xj must take non-negative integer values
(xj ∈
0).  In  contrast, continuous  resources–such  as  bandwidth,  processing  power,  or
≥
memory–can be allocated in fractional amounts. These are modeled with real-valued vari-
ables (xj ∈

0), enabling more flexible and fine-grained allocation strategies.
The  duration  of  resource  availability  significantly  impacts  allocation  methods,  as
resources may be either renewable or non-renewable. Renewable resources–such as solar
energy or CPU time–replenish over time and require time-dependent constraints for effec-
tive management (xi(t)
t). In contrast, non-renewable resources–such as bud-
gets, storage, or fossil fuels–are finite and subject to cumulative upper-bound constraints
Ri). These distinctions are essential for modeling real-world systems, where
(
renewable and non-renewable resources often coexist and must be managed in a coordinated
∑
and efficient manner. Recognizing the temporal nature of resource availability is therefore
critical for designing appropriate allocation strategies.

t xi(t)

Ri(t),

≤

≤

∀

Effectively  managing  resource  allocation  requires  a  structured  approach  to  align
resources with the specific demands of a system. This process involves understanding the
type  of  resources,  whether  distributed  or  non-distributed  and  the  needs  of  the  agents  or
processes involved. Distributed resources, which are common in cloud computing, allow for
flexible and scalable allocation across users and systems, though they introduce challenges
in managing latency and coordination (Halabian 2019; Sadatdiynov et al. 2023). In con-
trast, non-distributed resources, typical in manufacturing, often rely on a centralized alloca-
tion framework that provides direct oversight but may experience bottlenecks as demands
increase.

Given these distinctions, the allocation strategy should be adapted to the resource type to
maintain system efficiency. This approach requires assessing availability, demand, and con-
straints to ensure that resources are distributed effectively to meet system objectives, such
as maximizing throughput or minimizing idle time. The following section outlines a general
process for resource allocation, demonstrating how these principles apply to real-world sce-
narios. Figure 3 illustrates the distribution of resources in different properties.

Multi-agent reinforcement learning for resources allocation optimization:…1 3
354  Page 8 of 49

2.3  Classical methods in RAO

This section describes several classical methods to understand their limitations and potential
applications in RAO (see the full list of methods in Table 2).

2.3.1  Linear programming

Linear Programming (LP) is one of the foundational techniques in optimization, particularly
effective for RAO problems with linear relationships between variables. LP optimizes a lin-
ear objective function under linear equality and inequality constraints. This makes it useful
for traditional RAO problems such as cost minimization, profit maximization, and efficient
allocation of resources like time, money, or physical assets (Saaty et al. 2003).

While LP is suitable for problems with manageable numbers of variables and constraints,
modern  systems  like  cloud  computing  or  telecommunications  often  involve  high-dimen-
sional settings with large numbers of constraints and variables, making LP computationally
expensive for large-scale RAO in real-time contexts.

LP is inherently a centralized approach, assuming a single entity with full knowledge of
resources, constraints, and objectives. However, many RAO scenarios involve decentral-
ized systems, like multi-agent systems in smart grids or IoT networks, where LP’s central-
ized nature can lead to inefficiencies due to communication overhead and the need to gather
global information.

2.3.2  Heuristic optimization

Heuristic algorithms provide a flexible alternative for RAO by focusing on finding accept-
able, near-optimal solutions within a reasonable time frame. These methods are particularly
useful for complex, large-scale, or time-sensitive RAO scenarios where exact solutions are

Table 2  Summary of classical
approaches for RAO solution

Category
Linear
programming
Heuristic
optimization

Algorithm
Mixed integer lin-
ear programming
Simulated
annealing

Genetic
algorithms

Particle swarm
optimization

Representative work
Saaty et al. (2003)

Spinellis et al. (2000);
Suman and Kumar (2006);
Attiya and Hamam (2006);
Bi et al. (2020); Kosanoglu
et al. (2024)
Alcaraz and Maroto (2001);
Cardon et al. (2000); Tseng
et al. (2017); Gao et al.
(2020); Shao et al. (2024)
Bratton and Kennedy (2007);
Gong et al. (2012); Lin and
Chiu (2018); Liu et al. (2022)

Fuzzy logic based Xu et al. (2008); Wu et al.
(2018); Khan et al. (2019);
Zhang et al. (2021)

Game theory

Cooperative game Khan and Ahmad (2006);

Non-cooperative
game

Zhang et al. (2015)
Khan and Ahmad (2006); Ye
and Chen (2013)

M. A. Hady et al.1 3
Page 9 of 49  354

impractical. While  heuristics  do  not  guarantee  an  optimal  solution,  they  offer  a  practical
trade-off  between  accuracy  and  computational  efficiency,  making  them  suitable  for  real-
time applications.

 ● Simulated Annealing (SA): Inspired by the annealing process, SA probabilistically ex-
plores the solution space, refining the search to find near-optimal solutions, especially
useful in complex RAO scenarios (Kirkpatrick et al. 1983; Spinellis et al. 2000).

 ● Genetic Algorithms (GA): GA uses principles of natural selection to evolve solutions,
making it suitable for large or complex RAO problems with vast search spaces, such as
those found in multi-agent systems (Cardon et al. 2000) and cloud resource allocation
(Tseng et al. 2017).

 ● Particle Swarm Optimization (PSO): PSO simulates social behaviors, where particles
(potential solutions) adjust based on their experiences and those of their neighbors. This
approach is particularly well-suited for distributed optimization problems in RAO (Ken-
nedy and Eberhart 1995).

 ● Fuzzy Logic-Based Algorithms: These algorithms handle uncertainty in RAO by using
linguistic variables and fuzzy rules, providing flexible allocation even when resource
demand and availability are imprecise (Xu et al. 2008).

2.3.3  Game theory

Game theory models RAO as a strategic interaction among agents, each with potentially
competing  resource  needs.  In  non-cooperative RAO  scenarios,  each  agent  aims  to  maxi-
mize its utility independently (Khan and Ahmad 2006; Ye and Chen 2013). For example, in
wireless communication, users share a common spectrum, each aiming to maximize data
rates while accounting for interference from others (Cesana et al. 2008). The resulting Nash
equilibrium represents an optimized allocation where no user can unilaterally improve their
outcome, though it may not achieve global optimization.

In cooperative RAO scenarios, agents may form coalitions to share resources in ways
that  improve  system-wide  outcomes.  Cooperative  game  theory  models  these  coalitions,
with  the  Shapley  value  providing  a  way  to  distribute  gains  fairly  based  on  each  agent’s
contribution to the coalition (Khan and Ahmad 2006; Zhang et al. 2015). This approach is
particularly relevant in decentralized RAO, such as multi-agent systems where autonomous
agents either compete or cooperate for shared resources (Zhang et al. 2012). By capturing
interactions  among  agents,  game  theory  provides  a  structured  framework  for  optimizing
resource sharing in settings where individual and group goals intersect.

2.4  Limitation and challenge in classical RAO approach

Classical  RAO  approaches,  including  Linear  Programming,  heuristic  optimization,  and
game theory, provide essential tools for resource allocation. However, modern RAO prob-
lems  present  challenges  that  these  methods  cannot  fully  address  (Sarah  et  al.  2023). As
systems  become  increasingly  complex,  interconnected,  and  dynamic,  classical  methods
struggle  with  issues  like  scalability,  adaptability,  and  decentralization.  Key  challenges
include:

Multi-agent reinforcement learning for resources allocation optimization:…1 3354  Page 10 of 49

 ● Continuous  and  Rapid  Changing  Issues:  Modern  RAO  environments,  such  as  power
grids, cloud computing, and telecommunications networks, are characterized by rapidly
changing resource demands and availability. Classical methods, which assume static or
semi-static conditions, struggle to adapt to these dynamic settings. For example, cloud
computing experiences sudden fluctuations in demand for processing power, storage,
and bandwidth due to varying user activities or service request spikes (Zhang and De-
broy 2023), while power grids must balance supply and demand in real time to miti-
gate voltage fluctuations through optimal power management (Sun and Qiu 2021; Alam
et al. 2016). Similarly, next-generation mobile communication networks face challenges
in real-time adaptability and dynamic load distribution (Wang et al. 2024). Applications
such as autonomous vehicles, financial trading, and smart grids require rapid decision-
making under strict time constraints, but classical methods, which rely on solving com-
plex equations or iterative processes, often cannot provide near-instant solutions (Singh
et al. 2017). Furthermore, many modern systems operate under significant uncertainties,
such as unpredictable network congestion in telecommunications or changing energy
supplies and demands influenced by external factors (Suzuki et al. 2022).

 ● Decentralization  and  Partial  Observability:  In  many  modern  RAO  settings,  such  as
multi-agent  networks,  smart  grids,  and  IoT  systems,  resource  allocation  decisions
are  increasingly  decentralized  and  distributed,  with  agents  making  independent  deci-
sions based on local information (Halabian 2019; Liao et al. 2020; Hu et al. 2020; Hu
et al. 2024). Classical, centralized approaches are not well-suited for these scenarios,
as they assume full system observability and a central entity managing allocation. In
decentralized systems, each agent operates with partial knowledge of the environment
and  must  balance  its  own  objectives  against  those  of  other  agents.  Handling  partial
observability requires advanced, distributed algorithms that can coordinate effectively
without relying on global information, reducing the need for extensive communication
overhead.

 ● Scalability  Issues: As  systems  grow  larger,  resource  allocation  complexity  escalates,
often exceeding the capabilities of classical optimization techniques. Techniques like
linear programming and heuristics become computationally infeasible when applied to
large-scale systems, such as cloud computing networks, fog computing, or power grids,
where  thousands  or  millions  of  components  (e.g.,  servers,  devices,  or  users)  need  to
share limited resources (Costa et al. 2022; Gao et al. 2022b; Gao et al. 2023). The com-
putational costs of classical methods scale poorly with the number of variables and con-
straints, which leads to significant delays and inefficiencies. Many classical approaches
rely on centralized control, where a single entity manages resource allocation based on
global system information. In large-scale systems, centralized decision-making is im-
practical due to bandwidth, latency, and processing limitations, causing bottlenecks and
long delays. Techniques like mean-field approximations have been developed to address
these  scalability  challenges,  though  they  remain  limited  in  handling  highly  intercon-
nected systems (Yang et al. 2018; Wang et al. 2020).

 ● Heterogeneity of Resources and Objectives: Modern RAO problems often involve di-
verse resource types and multi-objective optimization, such as minimizing cost while
maximizing  efficiency  and  ensuring  fairness.  Unlike  classical  problems  that  assume
homogeneous  resources,  modern  systems  must  consider  a  range  of  resource  types
(e.g.,  bandwidth,  energy,  memory)  with  unique  characteristics  and  constraints  (Gao

M. A. Hady et al.1 3Page 11 of 49  354

et al. 2022a; Zhao et al. 2023). Additionally, multi-objective optimization requires bal-
ancing competing goals, which classical methods often cannot handle without signifi-
cant adjustments, making them impractical for complex, multi-dimensional RAO tasks.

The classical approaches often face several limitations to solve resource allocation as sum-
marized in the Table 3. The classical methods typically model and assume static or predict-
able environments, making them less adaptable to real-time changes, whereas MARL agents
continuously learn and adjust to dynamic conditions. For instance, the heuristic approaches,
beside  simple  and  fast,  are  hand-crafted  and  lack  generalization.  They  do  not  adapt  to
changes continuously, struggle with partial observability, and fail to coordinate effectively
in decentralized settings. Moreover, both classical game theory and heuristics handle agent
heterogeneity poorly, lacking mechanisms to dynamically accommodate diverse objectives
and resource constraints. The classical Game-theoretic models typically assume static envi-
ronments  and  full  observability,  making  them  poorly  suited  for  real-time  adaptation  and
partial information settings. Computing equilibrium becomes intractable as the number of
agents increases, limiting scalability. The scalability becomes a major challenge for tradi-
tional techniques as the size and complexity of the system grow, while MARL distributes
learning across agents, enabling efficient performance even in large-scale settings.

Additionally,  classical  methods  generally  rely  on  centralized  control  and  full  system
visibility,  which  limits  their  applicability  in  decentralized  and  partially  observable  envi-
ronments. MARL, in contrast, supports decentralized decision-making and performs well
under  local  or  incomplete  information.  Finally,  conventional  models  often  struggle  to
handle heterogeneous systems with varying agent roles or capabilities, while MARL can
develop specialized policies tailored to diverse agent functions, allowing for more flexible
and robust resource allocation.

These limitations arise some challenges underscore the need to move beyond classical
approaches  toward  more  advanced, AI-driven  RAO  methods,  with  a  particular  focus  on
MARL. In the following sections, we first introduce the foundational concepts of RL and
the key principles of MARL. We then survey MARL solutions in addressing RAO prob-
lems, structured as follows: Sect. 4.3.1 explores solutions for continuous and rapidly chang-
ing  issues,  Sect.  4.3.2  examines  approaches  to  decentralization  and  partial  observability,
Sect. 4.3.3 addresses scalability challenges, and Sect. 4.3.4 reviews strategies for managing
heterogeneity in resources and objectives.

Table 3  Comparison of classical
approaches, RL and MARL in
RAO

Aspect

Adaptability

Classical
approaches
Static

Scalability
Decentralization
Partial observability
Heterogeneity

Poor
✗
✗
✗

RL

MARL

Adapt to
dynamic
Poor
✗

✓
✗

Adapt to
dynamic
Good

✓
✓
✓

Multi-agent reinforcement learning for resources allocation optimization:…1 3
354  Page 12 of 49

3  MARL foundations

To effectively address the complex and dynamic nature of resource allocation optimization
(RAO) problems, especially those involving multiple interdependent decision variables and
system nodes, Multi-Agent Reinforcement Learning (MARL) has emerged as a powerful
solution. The RAO scenarios often demand adaptability, responsiveness to environmental
changes, and the ability to model cooperative interactions among multiple agents. MARL
is well-suited for such challenges, as it enables agents to learn optimized strategies through
directly interact with the environment. To fully leverage MARL potential in RAO appli-
cations, it is essential to understand its foundational concepts, including its mathematical
formulation, agent interaction models, and learning paradigms. Therefore, in this section
we introduce the core principles of MARL, laying the groundwork before we discuss its
application in diverse resource allocation contexts.

3.1  Reinforcement learning as optimization

RL  is  fundamentally  suited  to  address  the  decision-making  needs  in  RAO  by  enabling
agents to learn optimal resource allocation policies through trial and error in dynamic and
uncertain  environments.  Through  interactions  with  the  environment,  agents  can  identify
actions that maximize long-term rewards while adapting to immediate changes in resource
demands or availability. This interactive learning process aligns well with RAO’s goal of
balancing long-term efficiency with real-time demands. The agent’s Q-function estimates
the expected cumulative reward for each action in a given state, guiding optimal actions
that balance immediate and future outcomes. In RAO, this allows the agent to dynamically
allocate resources based on the current system state and its expected impact on future per-
formance Mao et al. (2016).

One  of  RL’s  key  advantages  in  RAO  is  its  capacity  to  adapt  to  changing  conditions
(Vengerov 2007). Real-world RAO  applications often involve unpredictable fluctuations,
such as varying workloads in cloud computing or shifts in energy demand in smart grids.
RL’s  continuous  learning  framework  allows  agents  to  adjust  allocation  strategies  in  real
time, accommodating shifts in resource availability or demand. Importantly, RL also sup-
ports  decision-making  under  uncertainty,  allowing  agents  to  explore  allocation  strategies
even without full knowledge of future requirements or the actions of other agents.

Reinforcement  Learning  (RL)  is  a  machine  learning  paradigm  where  an  agent  learns
to make sequential decisions by interacting with an environment to maximize cumulative
rewards over time (Sutton and Barto 2018). In RL, the agent’s objective is to learn a policy
(a mapping from states to actions) that optimizes long-term rewards, adjusting its actions
based on feedback from the environment.

3.1.1  Markov decision process

The RL framework is formally represented as a Markov Decision Process (MDP), which
models the environment, agent actions, state transitions, and rewards (Sutton 1988). This
structure  allows  agents  to  dynamically  adapt  their  actions  based  on  observed  states  and
obtained rewards, offering potential for real-time, flexible resource allocation in static or
semi-static conditions. An MDP is defined by a tuple (S, A, p, r, γ). Here, S represents the

M. A. Hady et al.1 3Page 13 of 49  354

set of possible states, while A denotes the set of actions available to the agent. The transition
dynamics are modeled by the probability function p(s′
s, a), which describes the probability
of moving from state s to state s′ after taking action a. The immediate reward, r(s, a, s′),
captures the reward received from transitioning from s to s′ by action a. The discount factor
[0, 1] determines the relative importance of future rewards in the optimization process,
γ
weighting immediate rewards more heavily when closer to zero.

∈

|

3.1.2  Learning objective and Bellman equation

∞

In an MDP, the objective is to find an optimal policy π∗, that maximizes the expected cumu-
lative reward, or return, over time. The return at time step t, denoted Rt, is expressed as the
i=0 γirt+i+1. To guide its decisions, the agent relies on
sum of discounted rewards Rt =
value functions, specifically the state value function Vπ(s) and the state-action value func-
tion Qπ(s, a). The state value function, Vπ(s) = Eπ [Rt|
St = s], represents the expected
return when beginning in state s and following policy π. The state-action value function,
St = s, At = a], provides the expected return when starting from state
Qπ(s, a) = Eπ [Rt|
s,  taking  action  a,  and  then  following  policy  π.  These  value  functions  are  recursively
defined by the Bellman equations, which relate the current value of a state to the expected
value of future states and rewards. The Bellman equation for the state value function Vπ(s)
is given by:

∑

Vπ(s) =

π(a

s)

|

a
∑

s′
∑

p(s′

|

s, a) [r(s, a, s′) + γVπ(s′)]

(2)

The state value function Vπ(s) can alternatively be expressed in terms of the action-value
function Qπ(s, a) as:

Qπ(s, a) =

s, a)

p(s′

|

[

r(s, a, s′) +γ

π(a′

|

a′
∑

s′)Qπ(s′, a′)

]

s′
∑

(3)

The  policy  π  aims  to  maximize  this  equation,  yielding  the  optimal  state-action  value
Q∗(s, a) across all states and actions.

3.1.3  Deep RL

As environments become increasingly complex and involve more factors, traditional meth-
ods like SARSA and Q-learning struggle with scalability and stability. This has led to the
development  of  advanced  algorithms  such  as  Deep  Q  Networks  (DQN),  which  approxi-
mate  the  Q-value  function  with  a  neural  network  Q(s, a; θ),  where  θ  represents  the  net-
work  parameters.  To  stabilize  training,  DQN  introduces  Experience  Replay  and  a  target
Q-network to decouple updates. The target Q-value and the corresponding loss function are
defined together as:

L(θ) = E

[(

r + γ max

a′

Q(s′, a′; θ′)

−

2

Q(s, a; θ)

]

)

(4)

Multi-agent reinforcement learning for resources allocation optimization:…1 3

354  Page 14 of 49

Enhancements  like  Double  DQN  (Van  Hasselt  et  al.  2016)  and  Dueling  DQN  (Wang
et al. 2016) improve performance by reducing overestimation bias and separating state val-
ues from action advantages.

Policy Gradient (PG) methods optimize the policy by directly maximizing the expected
return J(θ) using Monte Carlo estimates. In the vanilla PG approach, the gradient is given
by:

∇θJ(θ) = Eπ

T

[

t=0
∑

∇θ log π(at|

st; θ)Gt

,

]

(5)

where Gt is the cumulative reward from time step t onward. Actor-Critic methods (Konda
and Tsitsiklis 1999) combine Policy Gradient (PG) methods with value function estimation,
where the actor updates the policy parameters, and the critic evaluates the value function.
Advantage Actor-Critic  (A2C)  (Mnih  et  al.  2016)  further  reduces  variance  by  using  the
advantage function, A(s, a) = Q(s, a)

V (s), instead of the value function.

To maintain stability, Trust Region Policy Optimization (TRPO) (Schulman 2015) and
Proximal Policy Optimization (PPO) (Schulman et al. 2017) constrain updates to prevent
large  deviations  from  the  current  policy. TRPO  achieves  this  by  limiting  KL  divergence
while PPO uses a clipped objective.

−

3.2  Multi-agent reinforcement learning

MARL  extends  the  reinforcement  learning  framework  to  environments  where  multiple
agents interact and learn concurrently within a shared space (Bu et al. 2008). While standard
RL methods focus on optimizing the cumulative reward of a single agent, MARL addresses
the  complexities  arising  from  multiple  autonomous  agents  learning  and  adapting  simul-
taneously. This is especially relevant for RAO in large-scale, decentralized, and dynamic
systems where agents must cooperate or compete to manage limited resources effectively.

3.2.1  Why MARL match to modern RAO

The capabilities of MARL make it highly effective for addressing the core challenges in
modern RAO. Its decentralized training and execution paradigms enable agents to learn and
act autonomously, reducing the computational bottlenecks and data flow issues inherent in
centralized systems (Ma et al. 2024). This scalability is critical for RAO applications that
span large-scale networks, such as telecommunications or smart grids, where centralized
solutions fall short.

Additionally, MARL’s continuous learning processes allow agents to update their poli-
cies based on real-time feedback, making the approach highly adaptable to rapidly changing
environments, such as fluctuating energy demands in power grids or dynamic workloads
in cloud computing. In RAO settings that involve multi-agent systems, such as multi-robot
teams or IoT networks, MARL also supports decentralized operations (Zhou et al. 2023).
This is especially useful under the CTDE paradigm, where agents rely on local observations
and make decentralized decisions, addressing the need for distributed control in large-scale
systems with limited information (Charbonnier et al. 2022).

M. A. Hady et al.1 3
Page 15 of 49  354

MARL is also well-suited to handle heterogeneous resources and diverse objectives. It
allows for multi-objective optimization, enabling agents to balance local goals with over-
arching system objectives–a crucial feature for systems requiring distinct allocation strate-
gies for varied resources like bandwidth, energy, and memory (Xiao et al. 2023). Moreover,
MARL’s support for stochastic games and Dec-POMDPs equips agents to make informed
decisions in uncertain environments (Nguyen et al. 2020), a necessity in RAO tasks with
unpredictable variables such as fluctuating network loads in telecommunications or variable
energy supplies in smart grids.

By providing a structured and adaptable framework, MARL offers a decentralized, scal-
able, and responsive approach to the demands of dynamic and complex resource allocation
environments (Ning and Xie 2024). The following sections will delve into specific MARL
algorithms and methods tailored to these challenges, examining their potential to meet the
unique requirements of modern RAO applications.

3.2.2  Stochastic games

In multi-agent systems (MAS), agents operate within cooperative, competitive, or mixed
environments. These interactions are captured through the formalism of Stochastic Games
(SGs), a generalization of Markov Decision Processes (MDPs) that accommodates multi-
agent dynamics (Hu and Wellman 2003). A stochastic game, or Multi-Agent MDP (MA-
,  where  S
MDP),  involving  N  agents  is  defined  by  the  tuple:
represents the set of states, Ai is the set of actions available to agent i, forming the joint
action set A = A1 × · · · ×
[0, 1] is the state transition function, and
S
ri : S
→

R is the reward function for each agent i.

In  stochastic  games,  the  state  transitions  depend  on  the  joint  action  a = (a1, . . . , aN )
of all agents, which is critical for addressing dynamic RAO challenges. In fully coopera-
tive settings, all agents share a single reward function, aligning with the goal of optimiz-
ing resource allocation for a common objective. In contrast, competitive settings introduce
conflicting objectives (e.g., in zero-sum games where r1 + r2 = 0 for two agents), while
mixed settings involve a combination of cooperative and competitive elements, providing
flexibility to model various RAO scenarios.

AN , T : S

N
i=1, T,

N
i=1⟩

Ai}

ri}

S,
⟨

→

×

×

×

A

A

{

{

3.2.3  Partially observable stochastic games (POSGs) and Dec-POMDP

In  practical,  multi-agent  systems  frequently  face  partial  observability,  where  each  agent
only has limited information about the environment’s state, introducing additional complex-
ity due to uncertainty. To address this, Partially Observable Stochastic Games (POSGs) as
the  multi-agent  formulation  of  the  POMDP  framework,  allowing  several  agents  to  make
decisions  based  on  partial  and  uncertain  observations  and  each  agent  optimizes  its  own
expected return. Additionally, the agents may have an individual reward functions per agent,
and  it  has  a  general  interaction  settings  as  cooperative,  competitive  or  mixed  interaction
behavior depends on the nature of the system.

In  multi-agent  RAO  problem,  agents  work  collaboratively,  aiming  to  maximize  total
expected cumulative rewards of all agents over time. Each agent only has access to its own
local observation history and make decisions independently, without access to the global state
or other agents observations especially in the testing time or deployment stage. Therefore,

Multi-agent reinforcement learning for resources allocation optimization:…1 3354  Page 16 of 49

{

S,
⟨

Ai}

N
i=1, T, r,

N
i=1, O, N, γ

the Dec-POMDP, a special case of POSGs, is well-suited for modeling cooperative agent
behavior in RAO problems. In this setting, all agents share a common reward function r(S, A),
which promotes cooperation over competition (Hansen et al. 2004). Dec-POMDP is defined
Oi}
as:
, where S represents the set of environment states,
{
⟩
AN
and each agent i has an action space Ai, forming the joint action space A = A1 × · · · ×
for N agents. The state transition function T : S
[0, 1] describes the probability
of transitioning from state s to s′ given the joint action a = (a1, . . . , aN ). The global reward
function r : S
R provides feedback based on the joint actions. Each agent i has an
ON . The observa-
observation space Oi, and the joint observation space is O = O1 × · · · ×
[0, 1] gives the probability of agent i receiving observation
tion function O : S
oi given state s and joint action a. The number of agents is N, and γ
[0, 1] is the discount
factor that determines the importance of future rewards.

→

→

→

×

×

×

×

×

O

A

A

A

∈

S

Dec-POMDPs  align  well  with  RAO  tasks  that  require  cooperative  agent  behavior  for
optimal  resource  distribution.  They  enable  agents  to  operate  collectively  under  partial
observability and pursue system-wide objectives, effectively addressing complex coordina-
tion challenges in a decentralized manner.

3.2.4  Learning paradigms

The  training  of  agents  in  MARL  follows  three  main  paradigms.  Each  paradigm  presents
unique benefits and trade-offs for modern RAO, depending on the scale, distribution, and
interdependence  of  resources.  Figure  4  illustrates  the  structural  differences  among  these
paradigms.

3.2.4.1  Centralized training and centralized execution (CTCE)  In CTCE paradigm, a cen-
tralized controller determines the actions for all agents based on the global state, optimizing
coordinated interactions. The controller utilizes a global policy πglobal(s) or a value func-
tion  Qglobal(s, a)  to  select  the  optimal  joint  action  a,  either  by  setting  a = πglobal(s)  or
by choosing a = arg maxa′ Qglobal(s, a′). While CTCE ensures coordinated actions, scal-
ability can be challenging as the number of agents increases, due to the exponential growth
of the joint action space and the communication demands required for real-time access to

Centralized Training &
Execution

Agent-1

Agent-2

Agent-N

Environment

Decentralized Training and Execution

Agent-1

Agent-2

Agent-N

Environment

Centralized Training
Shared information

Decentralized
Execution

Agent-1

Agent-2

Agent-N

Environment

Fig. 4  Comparison of Training and Execution Paradigms in MARL: a CTCE is a fully centralized frame-
work which combines all observations and actions of the agents into a joint observation-action space.
b DTDE is a term for fully decentralized setting that treats all agents independently with their own obser-
vation, action, and reward (Wen et al. 2021). c CTDE framework has training in a centralized manner with
information from other agent, then deploy the trained policy to each agent independently

M. A. Hady et al.1 3
the global state. CTCE is best suited to controlled environments with relatively few agents,
where centralized control remains practical, while it encounters limitations in larger or more
decentralized RAO settings, such as distributed energy networks or cloud systems, where
scalability and latency are significant considerations.

Page 17 of 49  354

3.2.4.2  Decentralized training and decentralized execution (DTDE)  In DTDE, each agent
operates independently, selecting actions based solely on its local observations. The policy
πi(oi) maps each agent’s local observation oi to an action ai as ai = πi(oi), or alternatively,
using a local value function ai = arg maxa′i
Qi(oi, a′i). This decentralized framework offers
advantages in scalability and flexibility, enabling agents to operate autonomously. As such,
DTDE is suitable for highly distributed settings, such as sensor networks or fully decen-
tralized RAO scenarios. However, DTDE does not inherently provide coordinated actions,
which  can  result  in  non-stationary  environments  where  agents  must  adapt  to  the  evolv-
ing policies of others. Independent learning (IL) methods, such as Independent Q-Learning
(IQL) and Independent Proximal Policy Optimization (IPPO), are effective for large-scale,
distributed tasks but may encounter challenges when coordination or shared objectives are
essential, as seen in cooperative RAO contexts.

3.2.4.3  Centralized training and decentralized execution (CTDE)  CTDE combines the ben-
efits of centralized training and decentralized execution. During training, agents have access
to  global  state  information,  which  allows  for  a  centralized  learning  process. A  global  Q
function Qglobal(s, a) or value function Vglobal(s) is used to optimize the joint behavior of
agents. During execution, however, each agent follows its individual Q function Qi(oi, ai)
or  learned  policy  πi(oi)  based  on  local  observations  oi,  allowing  for  decentralized  deci-
sion-making without access to the global state or knowledge of other agents’ actions. Key
approaches under CTDE include centralized critic and credit assignment methods. The cen-
tralized critic approach (e.g., MADDPG Lowe et al. (2017) and MAPPO Yu et al. (2022))
uses  a  centralized  function  during  training  to  evaluate  joint  actions,  while  credit  assign-
ment methods like Value Decomposition Networks (VDN) Sunehag et al. (2018) and QMIX
Rashid et al. (2020) decompose joint rewards to guide individual agents. CTDE’s flexibility
makes it ideal for complex RAO applications, such as managing resources in distributed
cloud  environments,  where  agents  must  independently  make  allocation  decisions  while
aligning with overall system objectives.

4  RAO leveraging MARL

MARL  offers  a  powerful  approach  to  tackling  modern  challenges  in  RAO,  particularly
where traditional methods fall short in scalability, dynamic adaptation, and decentralized
decision-making. MARL extends reinforcement learning (RL) to involve multiple agents
interacting within a shared environment, enabling a collaborative, decentralized approach
to resource allocation that adapts to complex and changing conditions Bu et al. (2008). This
section  is  divided  into  three  subsections.  The  first  subsection  provides  a  general  design

Multi-agent reinforcement learning for resources allocation optimization:…1 3354  Page 18 of 49

and construction steps to solve RAO  problem using  MARL algorithm is provided  in  the
first subsection. Moreover, in the next subsection, a summarization of the available MARL
algorithm  for  different  application  is  discussed,  then  followed  by  the  primary  challenges
addressed in that particular field and application.

4.1  Design and construction of MARL for RAO problem

To solve RAO problems using MARL, a structured approach is required–one that aligns the
dynamics of multi-agent systems with the objectives of RAO. We begin by clearly identify-
ing the RAO problem and formulating it appropriately. Based on this, we select a suitable
MARL  learning  paradigm  and  algorithm,  design  the  reward  function,  and  then  train  the
agents. The final step involves evaluating the learned policy to determine whether it meets
the  intended  objectives.  This  step-by-step  methodology  is  explained  in  three  stages  and
offers general guidance for effectively applying MARL to a wide range of RAO scenarios
across different domains.

4.1.1  Step 1: RAO problem identification and formulation

This step begins with identifying the resource allocation problem and translating it into a
form suitable for learning-based solutions. It involves clearly defining the resources (e.g.,
bandwidth, power, task slots), as discussed in Sect. 2.2, the agents involved (e.g., satellites,
machines, vehicles), and the system objectives (e.g., maximizing throughput, minimizing
latency, improving fairness), in line with the optimization goals introduced in Sect. 2.1. It is
also essential to determine whether the environment involves cooperative, competitive, or
mixed agent interactions. Most RAO problems fall within the cooperative setting, but this
distinction influences the structure of the MARL framework to be used. Once the problem is
identified, it is mathematically formulated using either a Markov Game or a Decentralized
Partially Observable Markov Decision Process (Dec-POMDP). A Markov Game general-
izes single-agent MDPs to multi-agent systems by including joint actions, rewards, and state
spaces. When agents only have partial observability, the Dec-POMDP formulation is more
appropriate. This step includes defining the state space, action space, transition function,
observation  model,  and  reward  function.  Examples  of  such  formulations  across  different
RAO domains are summarized in Table 4. The cost or objective function from the original
RAO problem should be carefully mapped to a reward function to ensure that the learning
objective aligns with the optimization goal.

4.1.2  Step 2: determine the MARL learning paradigm and algorithm

After formulating the problem, the next step is to choose an appropriate MARL learning
paradigm that fits both the training process and execution environment. Common options
include three different types: CTCE, CTDE, and DTDE. Among these, CTDE is the most
widely  adopted  due  to  its  ability  to  balance  coordination  during  training  with  scalable,
decentralized execution. The choice of paradigm should reflect practical system constraints,
such  as  communication  bandwidth,  privacy  requirements,  and  the  level  of  observability
available to each agent. Following this, the selection of a specific MARL algorithm depends
on multiple factors, including the type of agent interactions (cooperative or competitive),

M. A. Hady et al.1 3Page 19 of 49  354

Table 4  Examples of observations, actions, and reward functions across application fields
Application field Observations, actions and reward functions

Telecom-
munications
and network
management:
resource alloca-
tion in wireless
network
Energy: power
distribution
networks

Distributed com-
puting: mobile
edge computing

Transporta-
tion: traffic
management

Observations: Channel State Information (CSI); Quality of Service
(QoS) information from several neighbors; signal-to-interference-plus-
noise ratio (SINR); long-term average interference.
Actions: Transmit power level.
Reward Functions: A weighted sum-rate utility function; average
throughput across the entire network

Observations: Active and reactive powers of loads; active power from
PVs; reactive power from PV inverters; voltage values.
Actions: Ratio of maximum reactive power generated.
Reward Functions: Voltage barrier function; reactive power generation
loss
Observations: Data size of the computation task; required computing
resources; task deadline; computing device distance; inter-satellite vis-
ibility and inter-satellite distance (specific for satellite edge computing).
Actions: Offloading ratio and computing capability; selected device or
server.
Reward Functions: System energy consumption; delay; computation
rate;.
Observations: Waiting time; queue length; vehicle location; longitudinal
and lateral position and speed of observed vehicles.
Actions: Selected lanes; high-level control for autonomous vehicle: turn
left, turn right, cruise, speed up, slow down.
Reward Functions: travel time for all vehicles; Collision; stable speed;
headway time; and merging cost evaluations

Manufacturing:
flexible job shop
scheduling

Observations: Machine productivity and relationships; status of ma-
chines (performing/available); workload of jobs (finished/remaining) at
different operations.
Actions: Select a job from candidate jobs (machine-agent) or choose a
machine from fixed set (job-agent).
Reward Functions: Minimizing number of time steps to complete all
jobs

Representa-
tive works
Nasir and
Guo (2019);
Naderial-
izadeh et al.
(2021); Guo
et al. (2020)

Wang et al.
(2021); Sun
and Qiu
(2021)

Zhang et al.
(2024);
Liu et al.
(2024);
Gao et al.
(2023); Gao
et al. (2023)
Chen et al.
(2023);
Antonio and
Maria-Dolo-
res (2022);
Wang et al.
(2020)
Zhang et al.
(2023); Liu
et al. (2023)

how resources are distributed among agents, the level of observability, the action space (dis-
crete or continuous), and the need for inter-agent coordination. The chosen algorithm must
be compatible with the selected learning paradigm and capable of scaling to the number of
agents involved. Key algorithmic properties to consider include sample efficiency, adapt-
ability to dynamic environments, stability during training, and convergence behavior. These
should align with the system dynamics and the reward structure defined in Step 1.

4.1.3  Step 3: policy training, evaluation, and adaptation

In the final step, the MARL agents are trained within a simulated environment that mimics
the real-world dynamics of the RAO problem. The training process should include appro-
priate exploration strategies and may benefit from techniques like curriculum learning to
handle  complex  task  structures. After  training,  the  learned  policy  is  evaluated  based  on
whether it achieves acceptable or optimal performance within the application context. Per-
formance evaluation involves measuring metrics such as resource utilization efficiency, task
success rate, average latency, fairness, and robustness under uncertainty. These evaluations

Multi-agent reinforcement learning for resources allocation optimization:…1 3354  Page 20 of 49

should  be  benchmarked  against  classical  optimization  methods  or  heuristic  baselines  to
assess whether the MARL-based approach provides tangible improvements. Where neces-
sary,  fine-tuning  may  be  conducted  to  adapt  the  trained  policy  to  real-world  constraints.
This includes addressing the sim-to-real gap by validating the policy’s robustness under real
deployment  conditions,  accounting  for  hardware  limitations,  real-time  requirements,  and
partial observability. Deployment considerations must also include computational feasibil-
ity and long-term policy stability under dynamic conditions.

4.2  MARL for RAO in different application fields

This  section  explores  how  MARL  serves  as  a  powerful  framework  for  addressing  RAO
problems  across  various  domains. We  begin  by  discussing  how  Reinforcement  Learning
(RL)  functions  as  an  optimization  technique  capable  of  handling  dynamic  and  uncertain
environments. Building on this foundation, we highlight the advantages of MARL in solv-
ing complex RAO tasks that involve multiple decision-making agents operating in decen-
tralized or partially observable settings. We then present how MARL has been applied to
RAO challenges in diverse real-world fields such as Telecommunication Network and IoT,
Energy,  Distributed  Computing,  Transportation,  and  Manufacturing.  Finally,  we  identify
and analyze key challenges commonly encountered in applying MARL to RAO, including
adaptability, coordination, scalability, and heterogeneity in resources (see summary in Table
5).

4.2.1  Telecommunication network and IoT

4.2.1.1  Vehicular network  Resource allocation in vehicular networks is a critical challenge
due  to  the  highly  dynamic  and  decentralized  nature  of  vehicular  environments. With  the
growing demand for intelligent transportation systems, efficient allocation of communica-
tion, computing, and storage resources is essential to ensure low latency, high reliability,
and optimal system performance. The integration of Multi-Agent Reinforcement Learning
(MARL)  has  emerged  as  a  promising  solution  for  enabling  distributed  decision-making
and  adaptability  in  such  dynamic  settings.  MARL  allows  vehicles  and  network  nodes  to
learn  cooperative  strategies  in  real-time,  handle  partial  observability,  and  respond  effec-
tively to time-varying network conditions. The reviewed papers demonstrate how MARL
significantly  enhances  adaptability in  vehicular  network  environments.  Mostly,  including
Li et al. (2022); Ji et al. (2023); Parvini et al. (2023); Wang et al. (2024); Mei and Wang
(2024); Ergün (2025) incorporate adaptive MARL algorithms such as MAPPO, MAD3QN
and MADDPG to dynamically respond to changing network conditions and user demands.
Studies like Seid et al. (2021); Zhang et al. (2020); Wu et al. (2020); Mondal et al. (2025);
Jun-Han et al. (2025); Liu and Deng (2025) further apply these models to UAV-enabled IoT,
secure communications, and traffic, highlighting the algorithms’ ability to handle variabil-
ity. Hu et al. (2024) design a multi-agent deep deterministic policy gradient (MADDPG)-
based offloading optimization and resource allocation algorithm (MADDPG-O2RA2) for
6 G vehicle-to-vehicle network. Distributed and cooperative setups in Hu et al. (2020) and
Zhou et al. (2023) exemplify the importance of decentralized decision-making in real-time
resource management. Although Zhao et al. (2023) and Yin and Yu (2021) do not explicitly
state adaptability, they adopt advanced MARL frameworks capable of operating in hetero-

M. A. Hady et al.1 3Table 5  MARL  for  RAO  in  different  application  and  its  primary  challenge:  A  (Adaptability),  PO  (Partial
Observability), LS (Large Scale), H (Heterogeneity)
Application
Field

MARL algorithm

Primary challenge
A
✓

PO

✓

Page 21 of 49  354

Telecommunica-
tion Network and
IoT (Sect. 4.2.1)

Vehicular Network

Mobile Network

Energy
(Sect. 4.2.2)

Distrib-
uted Computing
(Sect. 4.2.3)

Wireless Network

Computer Network
IoT Network
Microgrid

Smart Grid
Renewable Energy

Power Distribution

Home Energy
Management
Satellite Edge
Computing
Mobile Edge
Computing

Cloud and Fog
Computing
Vehicle Edge
Computing

Vehicle Fog
Computing
Traffic Management

Transportation
(Sect. 4.2.4)

MADQRL
MADDPG
MAD3QN
Graph Based
MADDPG
MAPPO
MADQRL
MAPPO
MADQRL
MAPPO
MATRPO
MADDPG
MATD3
MAPPO
MAD3QN
MATD3
Graph Based
MADDPG
MAT
MADQRL

MAAC

MAD3QN
MADDPG
MAAC
MAPPO
MAAC

MAD3QN
MAAC
MADDPG
MAPPO
MAAC

MADDPG
MAAC
MADQRL
Graph Based

Autonomous Vehicles MADDPG

Manufacturing
(Sect. 4.2.5)

Vehicle Allocation
Flexible Job shop

Cognitive
Manufacturing

MATD3
MAAC
MADQRL
Graph Based
MADDPG
MAPPO
Graph Based
Graph Based

LS
✓

–

✓

✓
✓
–

–
–

✓

✓

✓

H
–

✓

✓

–
–

✓

✓
–

–

–

–

✓

✓

–

–

–

✓

✓

✓
–

–

–

✓

✓

–

–

–
–

–

✓

–

✓
–

✓

✓
✓

✓

✓

–

✓

✓

✓

✓

✓

✓

–
✓

✓

–

✓

–
✓
–

–
–

✓

–

–

–

–

✓

✓

✓

✓

–
–

–

Multi-agent reinforcement learning for resources allocation optimization:…1 3354  Page 22 of 49

geneous and dynamic vehicular networks. Overall, these works underscore the strength of
MARL in providing flexible, context-aware solutions for resource allocation, outperforming
static or rule-based conventional methods.

4.2.1.2  Mobile  network  The  reviewed  studies  in  mobile  network  environments,  particu-
larly  under  the  complexity  of  mobile  network  management  and  heterogeneous  architec-
tures.  Du  et  al.  (2022)  proposed  a  graph-based  MARL  (GA-Net  MARL)  framework  for
dynamic  resource  management  in  6  G  in-X  subnetworks,  emphasizing  the  capability  of
graph structures to capture inter-agent relationships and support scalability. Allahham et al.
(2022) addresses the challenges of network selection and resource allocation in multi-RAT
(Radio Access  Technology)  networks  using  MADDPG,  enabling  collaborative  decision-
making in diverse environments. Meanwhile, Kim and Lim (2021) leverages MAPPO for
end-to-end  network  slicing,  facilitating  efficient  and  adaptive  management  of  resources
across network segments. Collectively, these works underline MARL’s ability to handle the
heterogeneity, real-time demands, and large-scale coordination challenges present in next-
generation mobile networks.

4.2.1.3  Wireless network  The integration of MARL into wireless networks demonstrates
promising capabilities for optimizing dynamic and distributed operations. Naderializadeh
et  al.  (2021)  employs  MADQRL  to  manage  wireless  resources  in  a  decentralized  fash-
ion, effectively tackling the coordination challenges among multiple agents in large-scale
environments. In a complementary approach, Guo et al. (2020) proposes a MAPPO-based
framework to jointly optimize handover control and power allocation, highlighting MARL’s
strength in handling coupled decision-making problems in wireless networks. Zhang and
Guo (2025) proposes a fully scalable MARL framework using MAPPO as well, where each
agent optimizes spectrum, power, and scheduling locally to minimize packet delays under
stochastic  traffic  in  both  conflict  graph  and  cellular  network  settings. Tu  and  Ma  (2025)
introduces  the  Multi-Agent,  Multi-Parameter,  Interaction-Driven  Contention  Window
Optimization (M2I-CWO) algorithm to optimize multiple CW parameters in IEEE 802.11
Wireless LANs. Together, these studies showcase MARL’s potential to outperform classical
approaches by enabling adaptive, scalable, and cooperative solutions for complex wireless
resource allocation scenarios.

4.2.1.4  Computer network  In computer network application, You et al. (2020) leverages
a fully distributed MADQRL framework for packet routing, enabling each agent to make
routing decisions independently while adapting to network dynamics. This design reduces
reliance  on  centralized  control  and  enhances  scalability.  Similarly,  Suzuki  et  al.  (2022)
adopts  a  cooperative  MADQRL  approach  for  dynamic  virtual  network  allocation  under
fluctuating traffic demands, demonstrating how MARL can effectively respond to variability
in network load while maintaining efficient resource use. Both studies underscore MARL’s

M. A. Hady et al.1 3ability to enable decentralized, adaptive, and resilient solutions for complex computer net-
working problems.

Page 23 of 49  354

4.2.1.5  IoT  network  In  the  IoT  Network,  Xiao  et  al.  (2023)  proposes  a  MAPPO-based
multi-agent  deep  reinforcement  learning  framework  to  address  resource  allocation  chal-
lenges in large-scale IoT networks, specifically tailored for ultra-reliable low-latency com-
munication  (URLLC)  scenarios.  Their  approach  enables  decentralized  agents  to  make
real-time decisions under strict QoS requirements while coordinating effectively to handle
the scale and complexity of controllable IoT systems. Li et al. (2025) introduces Mobility-
as-a-Resilience-Service (MaaRS), a resilience model that uses mobile UAVs and a robust
MADDPG  approach to optimize task allocation and system recovery amid uncertainties,
enhancing resource allocation in smart farms. These work highlights how MARL, can meet
the stringent demands of emerging IoT applications that require both scalability and reli-
ability in dynamic environments.

4.2.2  Energy

4.2.2.1  Microgrid  Recent  research  has  increasingly  leveraged  MARL  for  efficient  and
scalable energy management in microgrid systems. Xu et al. (2024) proposes a hierarchi-
cal  trust-region  MARL  framework  (MATRPO)  to  optimize  operations  across  intercon-
nected multi-energy microgrids, focusing on collaboration and trust-aware learning. Abid
et  al.  (2024); Wang  et  al.  (2025)  develops  multi-objective  optimization  strategy  employ-
ing MADDPG and actor-critic to enhance planning decisions for microgrid resource allo-
cation, balancing multiple operational goals. Zhang et al. (2023) introduced a distributed
control  architecture  using  MATD3  for  real-time  energy  management,  enabling  flexible
coordination among microgrids with varying energy types. Complementarily, Jendoubi and
Bouffard (2023) designs a hierarchical MARL model using MADDPG to support layered
decision-making,  improving  learning  efficiency  and  coordination  in  complex  microgrid
systems. These works collectively illustrate the diverse applications of MARL techniques
in  enhancing  energy  distribution,  planning,  and  real-time  control  within  smart  microgrid
infrastructures.

4.2.2.2  Smart grid  In smart grid applications to enhance the efficiency and autonomy of
energy systems. Kumari et al. (2024) introduces a decentralized residential energy manage-
ment system leveraging Deep Q-Network-based MARL (MADQN), focusing on distributed
decision-making for home energy optimization. Their approach enables agents to learn opti-
mal consumption strategies while ensuring grid stability. Meanwhile, Roesch et al. (2020)
applies  MAPPO  in  an  industrial  smart  grid  context,  where  multiple  agents  coordinate  to
manage energy flows dynamically and adaptively, reflecting the increasing complexity of

Multi-agent reinforcement learning for resources allocation optimization:…1 3354  Page 24 of 49

industrial  power  systems.  These  contributions  underscore  the  effectiveness  of  MARL  in
addressing decentralized, real-time control challenges in smart grids.

4.2.2.3  Renewable energy  Recent advances in MARL have significantly contributed to opti-
mizing renewable energy integration across diverse systems. Jayanetti et al. (2024) proposes
a  MARL  framework  based  on  Multi-Agent Actor-Critic  (MAAC)  for  renewable  energy-
aware workflow scheduling across distributed cloud data centers, aiming to improve energy
efficiency and computational performance. Shen et al. (2022) develops a MAD3QN-based
optimization framework for building energy systems, incorporating renewable sources to
balance comfort and energy costs. Chen et al. (2022) introduces a physics-shielded MARL
method utilizing MATD3 for active voltage control in photovoltaic and battery-integrated
grids, enhancing both safety and operational stability. These studies showcase the versatility
of MARL in addressing the complexities of renewable energy systems.

4.2.2.4  Power distribution  In power distribution systems, MARL has emerged as a pow-
erful tool for decentralized voltage and reactive power control. Hu et al. (2024) proposes
a  graph-based  MARL  approach  using  a  decentralized  training  and  decentralized  execu-
tion (DTDE) framework for Volt-VAR control, demonstrating scalability and coordination
among distributed agents. Wang et al. (2021) applies both MADDPG and MATD3 algo-
rithms to enhance active voltage regulation performance in distribution networks, improv-
ing adaptability in dynamic environments. Sun and Qiu (2021) introduces a two-stage Volt/
VAR control method using MADDPG for active distribution networks, combining global
planning  and  local  reactive  power  adjustment.  Wu  et  al.  (2024)  proposes  Multi-Agent
Transformer (MAT) to solve adaptability issue of the Multi-building multi-energy virtual
power  plants  which  is  caused  by  the  dynamic  behaviors  of  agents  joining  or  leaving  the
environment. These  works  illustrate  the  effectiveness  of  MARL  in  enabling  adaptability,
robust, and cooperative strategies in the modern power grids.

4.2.2.5  Home  energy  management  In  the  application  of  Home  Energy  Management,
MARL  has  been  widely  explored  to  optimize  distributed  control  and  enhance  residen-
tial  energy  flexibility.  Charbonnier  et  al.  (2022)  proposes  a  scalable  MARL  framework
based on MAQRL to manage distributed energy resources while preserving user comfort
and ensuring scalability across numerous households. Xu et al. (2020) introduces a data-
driven home energy management method employing MADQRL, which efficiently adapts to
dynamic consumption patterns and uncertain energy generation in smart homes. Similarly,
Ahrarinouri  et  al.  (2020)  utilizes  MADQRL  to  enable  collaborative  energy  management
among residential buildings, achieving significant improvements in both cost reduction and
peak load management. These studies demonstrate the capability of MARL approaches to

M. A. Hady et al.1 3deliver intelligent, decentralized, and adaptive energy management solutions in residential
environments.

Page 25 of 49  354

4.2.3  Distributed computing

4.2.3.1  Satellite edge computing  In the domain of distributed computing, especially satel-
lite mobile edge computing (SMEC), managing large-scale task offloading across multiple
dynamic  nodes  is  a  complex  challenge.  Zhang  et  al.  (2024)  addresses  this  by  proposing
a  Multi-Agent  Actor-Critic  (MAAC)  based  collaborative  optimization  framework.  The
approach is designed to be scalable and adaptable, enabling decentralized satellite nodes to
efficiently learn offloading strategies under highly dynamic and resource-constrained con-
ditions. By coordinating multiple agents in a shared environment, the solution effectively
tackles  the  scalability  issues  typical  in  SMEC  scenarios,  making  it  promising  for  future
large-scale satellite-enabled computing systems.

4.2.3.2  Mobile  edge  computing  The  MARL  has  emerged  as  a  powerful  approach  for
addressing complex challenges in Mobile Edge Computing (MEC), particularly in large-
scale environments where resource allocation, task offloading, and adaptability to dynamic
conditions are critical. The following papers highlight the challenges of large-scale resource
allocation and adaptability in MEC. Liu et al. (2024) focuses on computation rate maximi-
zation  for  SCMA-aided  edge  computing  in  IoT  networks  with  the  MAD3QN  algorithm,
addressing scalability and adaptation in dynamic environments. Gao et al. (2023) and Gao
et al. (2022b) tackle large-scale cooperative task offloading and resource allocation in het-
erogeneous MEC systems, utilizing the MAAC algorithm to manage scalability and adapt-
ability in diverse conditions. Chen et al. (2024) addresses unpredictable environments by
applying a Robust MADDPG. Gao et al. (2023) proposes Com-DDPG for task offloading
in MEC systems for the internet of vehicles, emphasizing the ability to adapt to informa-
tion-communication-enhanced environments. Zhao et al. (2022) presents MATD3 for task
offloading in UAV-assisted MEC, focusing on scalable and adaptable solutions for mobile
edge networks. Cao et al. (2020) applies MADDPG to address multichannel access and task
offloading challenges in Industry 4.0, emphasizing large-scale adaptability. Lastly, Wu et al.
(2023) uses MAPPO for minimizing completion delay and energy consumption in MEC-
based Industrial IoT (IIoT) systems, emphasizing scalability in handling large-scale IIoT
environments.

4.2.3.3  Cloud and fog computing  Resource allocation problem can be found in the cloud
application domain as in Nagarajan et al. (2025). This work a hybrid optimum and multi-
agent  deep  reinforcement  learning  (MADRL)  technique  for  Dynamic  Task  Scheduling
(DTS)  in  a  container  cloud  environment.  In  the  application  of  Fog  Computing,  Jain  and
Kumar (2023) focuses on QoS-aware task offloading in a fog computing environment, uti-

Multi-agent reinforcement learning for resources allocation optimization:…1 3354  Page 26 of 49

lizing the MAAC algorithm to address resource allocation and task management challenges
in distributed, resource-constrained fog networks.

4.2.3.4  Vehicle  edge  computing  Kang  et  al.  (2023)  presents  a  MAPPO-based  approach
for  cooperative  UAV  resource  allocation  and  task  offloading  in  hierarchical  aerial  com-
puting systems. Ju et al. (2023) proposes a joint secure offloading and resource allocation
strategy for vehicular edge computing networks using MADDQN, addressing both security
and resource management challenges. Zhu et al. (2020) and Xue et al. (2025) utilize the
MAAC and MATD3 algorithms for vehicular computation offloading in IoT environments,
emphasizing task allocation in vehicular edge computing systems. Zhang et al. (2021) com-
bines adaptive digital twin technology with MADDPG to optimize resource management
in vehicular edge computing and networks. These studies highlight the importance of scal-
ability, adaptability, and security in resource allocation and task offloading for vehicle edge
computing systems.

4.2.3.5  Vehicle fog computing  Wei et al. (2023) explores many-to-many task offloading in
vehicular fog computing using the MAAC algorithm, addressing the challenge of efficiently
managing resource allocation and task offloading between multiple vehicles and fog nodes.
Gao et al. (2022a) proposes a fast adaptive task offloading and resource allocation approach
in  heterogeneous  vehicular  fog  computing  systems,  also  utilizing  the  MAAC  algorithm
to enhance the efficiency and adaptability of resource management in dynamic vehicular
environments. Both studies emphasize the scalability and flexibility required for efficient
resource allocation in vehicular fog computing.

4.2.4  Transportation

4.2.4.1  Traffic  management  The  following  research  works  explore  the  application  of
MARL in traffic management. Zhang et al. (2024) presents MARLens, a visual analytics
approach to understanding traffic signal control using MADDPG. Chen et al. (2023) applies
MAAC for highway on-ramp merging in mixed traffic to enhance traffic flow. Zeynivand
et  al.  (2022)  implements  MADQRL  for  traffic  flow  control,  optimizing  vehicular  move-
ment across networks. Wang et al. (2020) introduces STMARL, a spatio-temporal MARL
approach  for  cooperative  traffic  light  control  using  a  graph-based  method.  Wang  et  al.
(2020) addresses large-scale traffic signal control with MADQRL, optimizing traffic man-
agement in urban settings. Wu et al. (2020) utilizes MADDPG for urban traffic light control
in vehicular networks, focusing on multi-agent coordination to improve traffic efficiency.
These studies demonstrate the versatility and effectiveness of MARL algorithms in optimiz-
ing various aspects of traffic management.

4.2.4.2  Autonomous  vehicle  MARL  is  applied  to  autonomous  vehicles  for  optimizing
decision-making,  coordination,  and  resource  allocation  in  various  driving  environments.
MARL approaches enable autonomous vehicles to interact, cooperate, and make decisions

M. A. Hady et al.1 3Page 27 of 49  354

in  complex,  dynamic  settings,  improving  safety,  efficiency,  and  traffic  flow. Antonio  and
Maria-Dolores (2022) applies MATD3 to manage connected autonomous vehicles at inter-
sections, optimizing vehicle coordination and traffic flow. Jiandong et al. (2021) explores
UAV cooperative air combat maneuvers, using MAAC for decision-making in autonomous
vehicle  control  scenarios.  Chen  et  al.  (2021)  leverages  graph  neural  networks  combined
with reinforcement learning for multi-agent cooperative control of connected autonomous
vehicles, optimizing vehicle coordination in complex networked environments. These stud-
ies demonstrate the potential of MARL for enhancing the coordination and decision-making
capabilities of autonomous vehicles in both traffic and cooperative tasks.

4.2.4.3  Vehicle allocation and routing  MARL has shown promising results in the applica-
tion of autonomous vehicles, particularly for resource allocation and optimization in com-
plex transportation systems. By enabling vehicles to interact and cooperate with each other,
MARL approaches can improve routing, task allocation, and overall operational efficiency
in autonomous vehicle systems. Ren et al. (2022) applies MADDPG to optimize vehicle
routing  in  supply  chain  management,  focusing  on  the  allocation  and  efficient  routing  of
vehicles. Their approach integrates route recorders to enhance coordination and decision-
making,  ensuring  that  vehicles  are  efficiently  assigned  tasks  and  follow  optimal  routes,
thereby  improving  supply  chain  logistics  and  transportation  efficiency. This  study  show-
cases the potential of MARL in optimizing vehicle allocation and routing, with a focus on
practical applications in supply chain management.

4.2.5  Manufacturing

In manufacturing systems, MARL can significantly improve RAO task by enabling decen-
tralized decision-making among autonomous agents, enhancing flexibility, efficiency, and
adaptability in complex production environments.

4.2.5.1  Flexible job shop  MARL has emerged as an effective approach to solve RAO prob-
lems in complex manufacturing process, especially in flexible job shop scheduling. In such
systems, multiple agents must make real-time, adaptive decisions to allocate resources, opti-
mize production workflows, and meet dynamic constraints, which is essential for increasing
efficiency  and  reducing  costs.  Jing  et  al.  (2024)  utilizes  a  graph-based  MARL  approach
combined with Graph Convolutional Networks (GCN) to optimize flexible job shop sched-
uling, enhancing the adaptability of agents in handling complex scheduling tasks. Heik et al.
(2024) proposes MAPPO to dynamically allocate manufacturing resources, addressing the
need  for  adaptive  decision-making  under  changing  production  conditions.  Zhang  et  al.
(2023)  introduces  DeepMAG,  which  integrates  deep  reinforcement  learning  with  multi-
agent  graphs  for  flexible  job  shop  scheduling,  allowing  agents  to  adapt  to  evolving  task
requirements and machine statuses. Liu et al. (2023) combines deep reinforcement learning
and a multi-agent system to dynamically schedule re-entrant hybrid flow shops, accounting
for worker fatigue and skill levels, thus improving adaptability in labor resource allocation.
Finally, Zhang et al. (2022) focuses on dynamic job shop scheduling using MAPPO, which
enables  multi-agent  manufacturing  systems  to  adapt  to  real-time  changes  and  uncertain-

Multi-agent reinforcement learning for resources allocation optimization:…1 3354  Page 28 of 49

ties  in  the  production  process.  These  studies  highlight  the  crucial  role  of  adaptability  in
optimizing flexible job shop scheduling through MARL, especially dynamic manufacturing
environments.

4.2.5.2  Cognitive  manufacturing  Cognitive  manufacturing,  which  integrates  AI  and
machine learning, has significant potential for improving decision-making, resource optimi-
zation, and process efficiency in manufacturing systems. MARL plays a key role in cogni-
tive manufacturing by enabling multiple agents to work together in a decentralized manner
to learn and adapt to various manufacturing tasks and environmental changes. Zheng et al.
(2021) addresses this challenge by proposing an industrial knowledge graph-based MARL
approach for cognitive manufacturing. Their approach enables agents to dynamically learn
and  adapt  to  different  manufacturing  tasks  through  the  use  of  knowledge  graphs,  which
helps in representing complex relationships between various system components.

4.3  MARL as a solution for modern RAO challenges

The  complexity  of  modern  RAO  has  led  to  the  extension  of  RL  to  multi-agent  settings,
enabling each agent to make localized and distributed resource allocation decisions. MARL
offers  a  range  of  paradigms  that  effectively  address  the  specific  challenges  in  RAO.  By
extending traditional reinforcement learning to handle multiple agents within a shared envi-
ronment, MARL introduces solutions that leverage centralized, decentralized, and hybrid
learning paradigms. This flexibility enables MARL to meet scalability, adaptability, coor-
dination, and privacy needs in RAO, making it a valuable framework for modern, complex
systems. In this subsection, we discuss further four primary challenges and how it is solved.

4.3.1  Adaptability in continuously changing environments

In dynamic and uncertain environments, RAO must deal with changes in resource demands
and availability that often occur unpredictably. A straightforward way to extend RL to multi-
agent settings is to combine the observations and actions of all agents into one input–output
model. This leads to a centralized learning setup, often referred to as CTCE, where a single
controller learns a joint policy for the entire system using global information. This setup can
appear advantageous because it allows the central controller to respond quickly to changes.
With access to all agents’ data, the controller can adjust the allocation strategy based on the
full system state, which seems useful in environments where demands change frequently.
However, while this centralization simplifies coordination in theory, it brings several impor-
tant limitations in practice.

First,  CTCE  becomes  difficult  to  scale  as  discussed  in  Sect.  3.2.4.  Then,  the  behav-
ior  of  one  agent  can  influence  the  learning  process  for  others,  making  the  environment
non-stationary and harder to learn from. These challenges even reduce the reliability and
effectiveness of CTCE in larger systems. Another concern is system resilience, as a central-
ized controller creates a single point of failure. If it fails or becomes overloaded, the entire
system may break down. Additionally, in resource allocation scenarios involving sensitive
data, such as personal information in healthcare Guindo et al. (2012) or financial data in

M. A. Hady et al.1 3Page 29 of 49  354

blockchain-based management systems Yánez et al. (2020), sharing all observations with a
central controller raises significant privacy and security concerns. These constraints make
fully centralized MARL frameworks less viable for many real-world applications. There-
fore, such settings are not widely used in the RAO research field, particularly when privacy,
data protection, or mission-critical robustness is required.

However, centralized methods can still perform well under controlled settings. For exam-
ple, Jain and Kumar (2023) tested CTCE-based algorithms such as DQN, DDPG, and SAC
for managing dynamic cloud computing tasks while maintaining Quality of Service (QoS).
The system considered various requirements, including latency, energy use, deadlines, and
task priorities. The SAC algorithm showed the best results, but the training was done offline
in a centralized cloud environment with full access to all data, conditions that are not realis-
tic in most practical deployments. Similarly, in Hu et al. (2020), a centralized method called
Compounded-Action Actor-Critic (CA2C) was used to manage UAV trajectory planning.
This algorithm handled both continuous and discrete actions in a joint model and was shown
to outperform other baselines in reducing the Age of Information (AoI). However, this also
relied on full observability and a central controller, and was tested only in simulation.

In  summary,  while  CTCE  frameworks  may  offer  strong  performance  in  idealized  set-

tings, they face serious limitations in scalability, robustness, and real-world applicability.

4.3.2  Coordinating resources with partial observability

In many RAO application, each agent can only observe a limited view of the overall envi-
ronment (e.g., local resource availability or neighboring agents’ actions). For instance, in a
network setting, an agent may only know its local bandwidth but not the network congestion
affecting other agents. This fragmented view makes it challenging for agents to make well-
informed decisions about resource allocation, often leading to suboptimal use of resources.
Partial  observability  leads  to  scenarios  where  agents  might  allocate  resources  based  on
incomplete or outdated information, which can create conflicts, over-allocations, or wasted
resources. For instance, an agent might allocate a resource already claimed by another, or
under-utilized resources that could have been shared more effectively.

RAO settings often demand that agents make decisions with limited local information,
particularly  in  IoT  networks,  multi-robot  systems,  and  other  distributed  architectures. To
optimize resource allocation, agents must coordinate their actions with limited information.
However, partial observability inherently limits their ability to understand how their deci-
sions impact others, especially in large systems where agents’ actions can have ripple effects
across  the  environment.  Inadequate  coordination  can  result  in  inefficient  policies  where
agents inadvertently work against each other. Addressing partial observability in resource
allocation  requires  a  combination  of  these  techniques  to  create  a  more  cohesive  MARL
framework, enabling agents to coordinate effectively despite limited information. This way,
agents can make more informed decisions, improving both local and global resource utiliza-
tion. For example, in a grid computing system, multiple agents might allocate tasks to the
same computing node, overloading it and slowing down task processing, while other nodes
remain idle. This lack coordination wastes computational resources and increases process-
ing times. Here, DTDE is highly applicable, as discussed in Sect. 3.2.4. The independence
afforded  by  DTDE  is  crucial  in  applications  where  maintaining  privacy  and  minimizing

Multi-agent reinforcement learning for resources allocation optimization:…1 3354  Page 30 of 49

communication costs are essential, such as decentralized task allocation in manufacturing
systems Zheng et al. (2021).

In an interconnected multi-energy microgrid optimization, Zhang et al. (2023) proposed
solution  to  the  decentralization  problem  in  microgrid  system.  The  authors  implemented
MADRL  algorithm  with  an  attention  mechanism  added  to  the  centralized  critic  to  meet
local customized energy demands in a form of decentralized execution. In this work, CTDE
framework is used to maintain global optimization performance with the coordination of
each agent. By using this framework, agents are trained with access to a centralized view
of the environment, allowing them to learn optimal strategies that account for the whole
system’s needs. During execution, agents act based on their local observations, but they are
guided by policies shaped by this global perspective.

However, in cases where some level of centralized oversight is feasible, CTCE can pro-
vide fully coordinated solutions. CTCE is ideal for small-scale RAO tasks with a limited
number of agents requiring precise synchronization, such as coordinated robotic tasks in
structured environments Jain and Kumar (2023). In this setting, CTCE enables the system
to optimize resource use by leveraging a complete, centralized understanding of all agents’
actions and states.

4.3.3  Dealing with large-scale systems

In centralized or semi-centralized approaches, scaling up the number of agents increases the
computational complexity and memory requirements due to the prodigious amount of state
and  action  information  that  needs  to  be  processed.  The  complexity  grows  exponentially
as the number of agents increases, making it impractical for real-time resource allocation.
Besides, In a DTDE framework, each agent is trained and operates independently, relying
only on local observations without needing centralized information Jiandong et al. (2021);
Wu  et  al.  (2020).  In  other  words,  the  agents  are  trained  to  maximize  their  local  rewards
and optimize their policies independently. This independence feature reduces computational
overhead,  as  each  agent  handles  its  learning  and  decision-making  based  on  local  states,
which is more scalable than a central agent tracking the states and actions of all others. With
more agents, there is a risk that individual decision quality may degrade if agents lack suffi-
cient information or coordination. In large-scale systems, maintaining high decision quality
is critical to ensure efficient use of resources across all agents Gao et al. (2023). Through
local  interactions  and  learning  policies  tailored  to  specific  environments,  agents  can  still
achieve  near-optimal  decisions  at  scale,  even  without  full  knowledge  of  other  agents’
actions.  This  framework  can  maintain  decision  quality  by  focusing  on  improving  each
agent’s local policy, which contributes to a more stable system-wide resource allocation.

Scalability  is  a  core  challenge  in  large-scale  resource  allocation  systems,  where  han-
dling numerous agents and their interactions becomes increasingly complex. This problem
emerges as discussed in Sect. 2.4 and raises complexity explosion. Specifically, scalability
issues arise when the algorithms or strategies used to allocate resources cannot efficiently
handle an increase in agents or resource demands. In RAO, each agent must choose actions
that contribute to optimal resource allocation. This problem is particularly pronounced in
real-time  RAO  scenarios,  such  as  network  bandwidth  allocation  or  power  distribution,
where decisions must be made quickly. As an impact, the agents might redundantly allo-
cate resources, over-commit shared resources, or even leave some resources underutilized

M. A. Hady et al.1 3Page 31 of 49  354

due  to  lack  of  information  about  other  agents’  decisions  without  effective  coordination.
This results in inefficiencies and potential bottlenecks in resource distribution. Leveraging
MARL frameworks, either DTDE or CTDE, can help agents to learn efficient policies in
large-scale and partially observable environments without a central controller.

To solve scalability in RAO problem, DTDE scales well with a large number of agents.
This is particularly beneficial in resource allocation scenarios where there are many resources
and  agents  in  distributed  energy  systems  or  communication  networks.  Since  agents  train
and  execute  independently,  DTDE  systems  do  not  require  the  sharing  of  sensitive  infor-
mation among agents or a central controller. This feature can be crucial in situations like
network resource allocation, where privacy and security concerns are high. DTDE allows
agents to adapt to local environmental changes or constraints without waiting for a central-
ized  update  or  communication.  This  can  lead  to  more  dynamic  and  responsive  resource
allocation,  as  agents  can  adjust  in  real-time  based  on  localized  resource  availability  and
demand. In DTDE, agents are trained to act independently without a centralized controller,
reducing the computational burden and making the system scalable. In Gao et al. (2023),
a task offloading based on MARL has been implemented for Information-Communication-
Enhanced Mobile Edge Computing for the Internet of Vehicles. This work evaluates LSTM
network and a BRNN, Actor Critic MARL in a fully decentralized setup and compares all
of the algorithms performance.

Graph  based  MARL  has  been  evaluated  to  solve  problem  in  power  distribution  using
DTDE framework in Hu et al. (2024). The authors proposed algorithm divides the power
distribution system into several regions, each region treated as an agent. Then an MARL
was designed by employing Hierarchical Graph Recurrent Network (HGRN) structure that
combines  the  advantages  of  Hierarchical  Graph Attention  (HGAT)  and  Gated  Recurrent
Unit  (GRU)  enables  the  communication  between  heterogeneous  agents.  Another  graph
based MARL has been implemented in Zheng et al. (2021) by using industrial knowledge
graph (IKG)-based multi-agent reinforcement learning. It is designed to solve the robot task
allocation and completion problem in a manufacturing network.

MARL’s capacity for decentralized real-time adaptation is a key advantage here, particu-
larly in CTDE framework, where agents are trained with global insights, yet operate with
decentralized policies in real-time as mentioned in Sect. 3.2.4. For instance, in energy man-
agement systems, CTDE enables agents to adapt to fluctuating demands while maintaining
overall grid stability Guo et al. (2020). By updating policies based on local observations
and  previously  learned  global  strategies,  agents  can  quickly  react  to  dynamic  conditions
without  centralized  intervention.  Furthermore,  CTDE’s  use  of  a  centralized  critic  during
training mitigates the non-stationary issue that arises from agents learning simultaneously.
This is particularly effective in RAO applications like edge computing, where agents (serv-
ers or virtual machines) optimize resource allocation across fluctuating workloads Wu et al.
(2023). By combining centralized training with decentralized adaptability, CTDE balances
the need for coordination with the flexibility to handle rapid environmental changes.

By training with centralized information but executing with decentralized policies, the
system can scale to a large number of agents and environments. During training, agents can
learn to cooperate and avoid conflicts or inefficient resource usage. Decentralized execution
allows agents to quickly adapt to local changes in demand or resource availability without
waiting for global updates. Another benefit is that CTDE reduces communication overhead

Multi-agent reinforcement learning for resources allocation optimization:…1 3354  Page 32 of 49

during execution, which is crucial in systems where bandwidth or computational power is
constrained.

One type of Credit Assignment is developed using Value Decomposition (VD) method.
The common algorithm that has been used in RAO problem is QMix. It has been evaluated
to solve a problem for vehicular cloudlet in automotive industry Ahmed et al. (2023). A joint
Q function is used to evaluate the actions of all agents collectively. The global reward is
computed based on the combined agent’s performance, and the centralized system updates
a joint action-value function.

Currently,  value  decomposition  (VD)  methods  are  less  commonly  used  in  RAO  com-
pared to centralized critic (CC) approaches. VD represents cooperative strategies by decom-
posing  the  joint  action-value  function  Qtot  into  individual  action-value  functions  Qi  for
each agent. It assumes that the team’s total value can be factorized into components attrib-
uted to individual agents, typically through additive or structured decomposition. However,
these assumptions may break down in environments with strong inter-agent dependencies.
In contrast, CC methods–generally policy-based–integrate more naturally with actor-critic
frameworks. They tend to offer greater stability and robustness to hyperparameter tuning,
making them easier to apply across diverse tasks. Moreover, CC approaches support distrib-
uted training, where agents independently update their policies while relying on a shared
critic  during  training.  On  the  other  hand,  VD  methods  depend  on  a  joint  Q-value  struc-
ture, which often requires synchronized execution among agents. This requirement limits
scalability  and  can  hinder  practical  deployment  in  real-world  settings. Additionally,  VD
methods are typically more sensitive to hyperparameter tuning, further complicating their
use in dynamic or large-scale scenarios. These limitations contribute to the broader adop-
tion of centralized critic methods in many contemporary multi-agent reinforcement learning
applications.

For  instance,  in  cloud  environments,  Wu  et  al.  (2023),  a  task  offloading  optimization
problem  for  edge  computing  based  Industrial  IoT  (EIIoT)  infrastructure  has  been  solved
using  MARL  algorithm. An  actor-critic  (AC)  DRL  framework  is  adopted  to  construct  a
suitable lightweight offloading decision system and optimize the joint completion delay and
energy consumption in the EIIoT.

CTDE can be used to allocate spectrum resources dynamically between different users or
devices in a 5 G or IoT network. Agents (representing base stations or users) learn to allo-
cate bandwidth efficiently based on energy consumption Meng et al. (2020); Nasir and Guo
(2019), traffic demand and channel quality Kim and Lim (2021). Additionally, in energy
management  systems,  CTDE  MARL  is  used  to  allocate  power  from  renewable  sources
among  consumers  or  storage  devices.  Agents  (representing  homes,  factories,  or  storage
units) learn to request power optimally to balance supply and demand, minimize waste, and
ensure grid stability. Also, this paradigm has been evaluated in the optimization of power
allocation for home energy management using MAPPO algorithm Guo et al. (2020). In fact,
MAPPO is also built upon centralized critic network and it shows competitive performance
to solve the task in energy management.

4.3.4  Handling heterogeneity in resources and objectives

In multi-agent systems, agents must balance diverse resource types, availability, and pos-
sibly conflicting objectives. Resources often vary widely in their characteristics, utility, and

M. A. Hady et al.1 3Page 33 of 49  354

constraints, leading to heterogeneity in their availability, value, and compatibility with dif-
ferent tasks. For instance, in cloud computing, resources like CPU, memory, storage, and
GPU have different capacities, costs, and efficiencies, and not all tasks require or benefit
from each resource in the same way. In smart grids, energy sources might vary (e.g., solar,
wind, fossil fuel), each with unique costs, emissions, and reliability levels. Matching the
right resource to the right demand while maintaining system efficiency becomes complex
in such diverse resource pools. Resource heterogeneity can create allocation inefficiencies
and under-utilization. Allocating a resource poorly suited to a task can lead to degraded per-
formance, over-utilization of high-value resources, and an imbalance where some resources
are over-consumed while others are underutilized. Heterogeneity in resources and objec-
tives adds complexity to the task of matching available resources with the diverse needs of
agents. Poor matching leads to inefficiency, where high-demand or specialized resources are
wasted on low-priority or incompatible tasks. This can reduce overall performance, degrade
system stability, and prevent high-priority tasks from accessing the necessary resources as
discussed in Sect. 2.4.

Many RAO problems involve multiple types of resources, each with unique allocation
goals. CTDE is well-suited for these heterogeneous environments, as it allows centralized
training to capture complex interdependencies between diverse resource types as discussed
in Sect. 3.2.4. For example, in cloud computing, agents trained with CTDE learn to balance
between CPU, memory, and bandwidth resources Wu et al. (2023), optimizing across mul-
tiple metrics such as energy consumption, latency, and throughput.

In situations with diverse agent goals or conflicting objectives, Credit Assignment within
CTDE is particularly valuable. Credit assignment decomposes the joint action-value func-
tion into individual agent rewards, enabling each agent to receive feedback on its contribu-
tion to the overall objective. Value decomposition methods, such as QMIX, can facilitate
nuanced resource allocation in scenarios like vehicular cloudlets, where agents (vehicles)
must  manage  bandwidth  and  energy  resources  to  optimize  communication Ahmed  et  al.
(2023).

A Centralized Critic (CC) (by using actor-critic methods) or a centralized policy network
is used to optimize the overall objective, accounting for interactions between agents as in
Wei et al. (2023). During  training, CC has access to the global  state of  the  system (e.g.,
overall network load, resource availability, and actions of all agents). This allows the agents
to learn how their individual actions affect overall system performance. Agents can share
experiences and learn from each other, which speeds up training and improves coordina-
tion. CC approaches address the non-stationary problem caused by the changing behaviors
of agents. These help to stabilize learning by using a shared critic function to evaluate the
actions of multiple agents, reducing the complexity of dealing with multiple evolving poli-
cies. Once the training is complete, agents operate independently based only on their local
observations. They no longer have access to the full state of the environment or the actions
of other agents. This decentralized execution is scalable to large environments with multiple
agents, as each agent can act autonomously without relying on global information in real
time.

Multi-agent reinforcement learning for resources allocation optimization:…1 3354  Page 34 of 49

4.4  Summary of MARL learning paradigms and algorithms comparison

To summarize, we compare various MARL algorithms across four key dimensions: adapt-
ability (A), scalability to large-scale problems (LS), support for distributional training (DT),
and the ability to handle agent heterogeneity (H) as shown in Table 6. Adaptability refers to
how well the algorithm adjusts to dynamic changes, such as varying tasks, agent numbers,
or goals. Scalability to large-scale problems measures how effectively the algorithm per-
forms as the number of agents or environment complexity increases. Distributional training
indicates whether the training process can be distributed across multiple nodes or agents
to reduce computational bottlenecks. This criterion evaluates how the training workload is
architecturally split–i.e., policies can be trained in parallel across multiple nodes or agents
to speed up computation and reduce centralized load. Please note that this setup can still
assume  centralized  data  access,  where  each  agent  may  have  visibility  into  other  agents’
states  or  actions. And  the  last  is  Heterogeneity,  which  captures  the  algorithm’s  ability to
manage agents with different observation spaces, action sets, or roles. Together, these crite-
ria provide a structured view of how MARL methods perform under practical demands such
as scalability, efficiency, and adaptability to complex, diverse, and dynamic environments.
Building on these criteria, we provide a high-level comparison of the main MARL par-
adigms.  CTCE  algorithms  typically  score  low  across  all  four  dimensions. Their  reliance
on  global  observability  and  centralized  execution  makes  them  unsuitable  for  large-scale
or dynamic RAO tasks, as they lack both flexibility and the infrastructure for distributed
training. They also assume homogeneous agent roles, limiting their applicability in hetero-
geneous settings. DTDE algorithms represent the opposite end of the spectrum. They are
naturally adaptable to changing environments and agent populations, highly scalable due
to their decentralized structure, and inherently support distributional training. Their design
allows each agent to operate and learn independently, making them particularly well-suited
for real-world, large-scale RAO problems with diverse agent capabilities. CTDE methods
offer a middle ground. While they generally perform well in adaptability and heterogeneity,
their scalability and support for distributional training vary depending on implementation.
Algorithms such as MAPPO or HAPPO provide strong coordination while retaining some

Learning paradigm Algorithm
CTCE

DTDE

CTDE

Table 6  MARL learning para-
digm and algorithm comparison

A (Adaptability), LS (Large-
Scale, DT (Distributional
Training), H (Heterogeneity)

*Depending on the Graph-based
structure, since it may have a
network connection between
agents hindering the distributed
training process

LS DT H

A
Low
Centralized PPO
Centralized DQN Low
High
IQL
High
DDPG
High
IPPO
Moderate
MATD3
Moderate
MAD3QN
Moderate ✓
MADQRL
Moderate
QMIX
Moderate
VDN
High
MAAC
High
MAPPO
High
MAT
High
Graph-based

✓
✓

 ✓  ✓ ✓
 ✓ ✓  ✓
 ✓  ✓ ✓
 ✓  ✓ ✓
 ✓ ✓
✓
✓
✓
✓
✓
✓  ✓
✓
✓
✓
 ✓

✓

*

M. A. Hady et al.1 3
Page 35 of 49  354

degree of scalability. However, approaches like QMIX or VDN, which rely on joint value
decomposition, often require synchronized training and centralized coordination, limiting
their use in highly distributed systems. Overall, DTDE and advanced CTDE methods dem-
onstrate stronger alignment with the demands of modern RAO scenarios, especially where
decentralized control, heterogeneous agents, and scalability are critical.

5  Available RAO simulators for benchmarking

In MARL, a standardized simulator or environment for benchmarking is equipped with the
Open-AI gymnasium (gym) (Towers et al. 2024) library as their main framework to be inte-
grated with any common reinforcement learning algorithms. Here, we listed some publicly
available benchmarks for RAO task inspired by the real-world application which are com-
monly used, based on gym library and can be widely used for evaluating MARL algorithm
before it is implemented to the real application.

5.1  Earth observation satellite mission

In  Stephenson  and  Schaub  (2024b),  an  open-source  Python  package  for  developing  and
customizing reinforcement learning environment has been designed by the authors to solve
spacecraft  tasking  problems.  It  integrates  Basilisk,  a  high-performance  and  high-fidelity
spacecraft  simulation  framework,  with  the  abstractions  of  satellite  tasks  and  operational
goals, all within the standard Gymnasium API wrapper for RL environments (see Fig. 5).
This package is specifically designed to support the needs of researchers in reinforcement
learning and spacecraft operations. Some works has been done to solve earth observation
mission using RL algorithm Herrmann et al. (2023), Herrmann et al. (2024), Stephenson and
Schaub (2024a) and currently a MARL framework has been provided as an example. This
work has an open source codes available here: https://github.com/AVSLab/bsk_rl.

5.2  Power grid networks

A common power management benchmark has been proposed in Wang et al. (2021). This
environment introduces a power network problem that provides a compelling yet challeng-
ing real-world scenario for the application of MARL as illustrated in Fig. 6. The growing
trend  of  de-carbonization  is  putting  significant  pressure  on  power  distribution  networks.
Active voltage control has emerged as a promising solution to alleviate power congestion
and enhance voltage stability without requiring additional hardware, by leveraging control-
lable devices within the network, such as rooftop Photo-voltaic (PV) and Static Var Com-
pensator (SVC). It has been used for a robust evaluation of MARL algorithms in Guo et al.
(2022), cooperative MARL with individual global max Hong et al. (2022), dynamic MARL
algorithm configuration Xue et al. (2022), some power networks research Chen et al. (2022);
Lu et al. (2023), etc. These devices are numerous and spread across wide geographic areas,
making MARL an ideal approach. The codes of this work is publicly available here:  h t t p s :   /
/ g i t h u  b . c o  m / F  u t u  r  e - P o w   e r - N e t  w o  r  k s / M A P D N.

Multi-agent reinforcement learning for resources allocation optimization:…1 3354  Page 36 of 49

2. Imaging or Scanning

1. Downlinking

3. Charging

4. Desaturating

Fig. 5  Earth Observation Mission Environment in BSK-RL: The number of satellite can be defined either
single satellite or multi-satellite. Each satellite has its own action: 1) Downlinking: Transmit collected
data to the ground station with predefined transmission speed and delete the data after successfully down-
linked; 2) Imaging or Scanning: Satellite capturing image of a target using optical sensor or scanning any
object on the earth surface using radar sensor (with two different payloads and can be used for different
tasks); 3) Charging: The satellite is in charging mode and pointing its solar panel towards sun direction to
maximize solar energy absorption; 4) Desaturating: There is a condition of the satellite’s rotating wheel
rotates saturatedly and the speed should be reduced to control their attitude

G

0

Zone 3

23

L

24

L

25

L

1

2

L

3

L

4

L

5

L

Zone 2

19

L

20

L

21

L

22

L

29

L

30

L

33

L

Zone 4

26

L

6

L

Zone 1

7

L

13

L

14

L

18

L

Fig.  6  Power  Grid  Networks  environment:  This  system  simulates  the  energy  distribution  and  control
within 4 different zones and 33 Bus Networks. Bus 2-33 voltages should be controlled by the system
and Bus 0-1 represent the substation at the main grid with constant voltage and infinite active and reac-
tive power capacity. There are several PV energy sources located in different areas that is challenging to
maintain the voltage stability and control

M. A. Hady et al.1 3

Page 37 of 49  354

5.3  Traffic management

CityFlow  is  a  multi-agent  reinforcement  learning  (MARL)  environment  developed  for
large-scale  urban  traffic  management  (Zhang  et  al.  2019).  It  tackles  the  complex  task  of
traffic  signal  control,  which  requires  real-time  adaptation  to  dynamic  traffic  conditions
and coordination among thousands of agents, such as vehicles and pedestrians. CityFlow
features fundamentally optimized  data structures and efficient algorithms, enabling high-
speed, city-wide simulations. It supports flexible road network and traffic flow configura-
tions based on both synthetic and real-world data, and includes a user-friendly interface for
integrating reinforcement learning models (see Fig. 7). Most importantly, CityFlow enables
large-scale, interactive traffic simulations and opens new possibilities for advancing intel-
ligent transportation systems through machine learning. In Wei et al. (2019) the CityFlow is
used to develop the algorithm. The resources of this simulator can be found here:  h t t p s : / / g i t
h u b . c o m / c i t y fl  o w - p r o j e c t / C i t y F l o w     .

5.4  Container management

A real-world industrial control task inspired resource allocation environment has been pro-
posed in Pendyala et al. (2024). The authors outline the real-world industrial control task that
served as the basis for RL benchmark. This task stems from the final phase of a waste sort-
ing process (see Fig. 8). The environment comprises a solid material transformation facil-
ity containing multiple containers and a much smaller number of Processing Units (PUs).
These containers are continuously filled with material, where the flow rate of the material

Fig. 7  Snapshot from the CityFlow simulation which manages traffic flows allocation at the intersection
for single agent RL and multiple intersection for MARL

Multi-agent reinforcement learning for resources allocation optimization:…1 3
354  Page 38 of 49

Waste Material Flow in

Waste Conveyor

Container-
1

Container-
2

Container-
n

PU Distributor

PU-1

PU-2

PU-j

Output
Product

Fig. 8  ContainerGym environment: This environment simulate the waste processing unit that is assumed
the waste materials flow input continuously and store them to multiple containers. It should maintain the
container level and allocate to Processing Unit (PU) that requiring waste materials to be processed

Table 7  Summary of algorithms
tested in the benchmarks or
simulators

Benchmark
BSK-RL

Power distribution networks

ContainerGym

Traffic management

Algorithm
PPO
MAPPO + Communication
IAC
IDDPG
MADDPG
SQDDPG
IPPO
MAPPO
MAAC
MATD3
COMA
FACMAC
PPO
TRPO
DQN
Graph based MARL

follows a stochastic process that varies by container. Although this environment is devel-
oped for RL algorithm, it can be extended into the MARL settings by adding more agents.
This work has a publicly available codes here: https://github.com/Pendu/ContainerGym.

5.5  Tested algorithms

Based  on  the  mentioned  available  simulators,  several  algorithms  have  been  found  in  the
repository  and  reported  in  literature  as  shown  in  Table  7.  In  different  environments  the

M. A. Hady et al.1 3

Page 39 of 49  354

implemented algorithms ranges from on-policy and off-policy, single-agent to multi-agent
and different MARL learning paradigms.

5.6  The need of realistic benchmark

Despite the growing interest in developing more realistic MARL applications, the current
available benchmark environments present several key limitations. First, realism remains a
major concern, as many existing simulators simplify the complexities found in real-world
applications, such as physical constraints, noisy observations, or dynamic agent interactions.
Second, availability is limited–many benchmarks are either proprietary, domain-specific, or
lack sufficient documentation and community support, which hinders broader adoption and
comparative  evaluation.  Third,  the  sim-to-real  transfer  gap  remains  largely  unaddressed.
Benchmarks often overlooked to reflect the discrepancies between simulated environments
and deployment scenarios, leading to policies that perform poorly or unpredictably in real-
world systems.

To  address  these  limitations,  there  is  a  critical  need  for  a  unified  offline  MARL  data-
set that spans diverse RAO task configurations, agent types, and objectives. This dataset
should be standardized, compositional, and designed to bridge the gap of offline learning
algorithms to real-world deployment. It would also facilitate research on offline-to-online
transfer,  sample-efficient  fine-tuning,  and  policy  robustness  in  resource-constrained  or
safety-critical  deployments.  Furthermore,  these  datasets  could  serve  as  a  foundation  for
pretraining  transferable  policy  representations  that  generalize  across  structurally  related
multi-agent environments, enabling progress toward more practical and applicable MARL
solutions.

6  Potential challenges and future directions

6.1  Potential challenges

MARL  offers  a  powerful  solution  for  addressing  the  complexity  and  dynamic  nature  of
RAO. By allowing decentralized agents to learn optimal strategies through interaction with
their environment, MARL can handle the challenges of non-stationary condition, competi-
tion, and cooperation, providing a flexible, scalable approach for optimizing resource dis-
tribution in a variety of domains. However, several challenges remains in this domain stand
out as critical obstacles for both academic research and engineering practice.

6.1.1  Scalability

In the future, MARL research lies in scaling up to environments with hundreds or thousands
of interacting agents. The exponential growth of the joint action space and the difficulty in
learning stable policies in such dense interaction environments demand new approaches to
improve performance further. In highly decentralized RAO problems, such as traffic man-
agement across a city-wide network, distributed energy resource allocation on a national
scale smart grid, or internet over thousands of satellites, the agents must coordinate deci-
sions in near real-time while still learning effectively from limited local observations.

Multi-agent reinforcement learning for resources allocation optimization:…1 3354  Page 40 of 49

6.1.2  Simulator and real system gap

Another emergence issue is the gap between simulated training environments and real-world
deployment. Even small inaccuracies in the simulation model–such as  incorrect assump-
tions about network latency, environmental dynamics, or agent behavior–may lead to sub-
optimal or unsafe decisions in the real deployment. This problem is amplified in multi-agent
systems, as one agent’s suboptimal action can cascade through the environment, triggering
chain reactions among neighboring agents. The accumulated error may eventually result in
systemic failures, especially in tightly coupled systems like satellite constellation coordina-
tion or vehicular edge computing, where resource misallocation can propagate rapidly.

6.1.3  Safety and trustworthiness

In safety-critical RAO applications such as emergency communication networks, autono-
mous vehicles, or energy management, deploying MARL without guarantee and explain-
ability is unacceptable. The black-box nature of deep reinforcement learning exacerbates
concerns  around  explainability  and  trustworthiness. The  stakeholders  need  to  understand
the reason behind the agent made a specific decision, especially when failures occur. Fur-
thermore, recovery mechanisms must be in place. For instance, if an agent deviates from
its optimal path or encounters a new scenario, the system should switch back to a backup
policy or trigger a recovery mode to prevent failures. Research in safe MARL is needed to
enable verifiable and robust decision-making. Additionally, efforts to develop recoverable
MARL  frameworks,  which  allow  agents  to  recover  from  mistakes  without  impact  to  the
overall system, are essential for deployment in the future.

6.2  Future directions

The application of MARL in RAO holds immense promise, addressing the potential chal-
lenges to shape advanced industrial revolutions in many domains. MARL’s capabilities such
as adaptive learning, scalable coordination, and modeling intricate agent interactions, posi-
tion it as a powerful paradigm for future resource management systems across domains.

One of key research direction is enhancing scalability and efficiency in real-world sys-
tems. As applications scale to encompass hundreds or thousands of agents–such as in the
Internet  of  Things  (IoT),  edge  computing,  or  autonomous  transportation–MARL  must
effectively  manage  computational  complexity  and  communication  overhead.  Networked
and  hierarchical  MARL  frameworks  allows  for  multi-level  abstraction  and  decomposi-
tion of complex tasks into manageable sub-problems, improving scalability and decision-
making efficiency. Similarly, techniques like mean-field approximations (Yang et al. 2018)
and  decentralized  learning  architectures  (Zhang  et  al.  2019)  offer  practical  solutions  for
scaling  MARL  in  distributed  environments. As  systems  scale-up,  seamless  collaboration
between agents is needed to ensure coherent collective behavior. Advances in Graph-based
modelsZhang et al. (2023) and communication-efficient protocols are critical for improving
cooperation, particularly in reducing computational complexity and communication load.

Another critical aspect is heterogeneity of agents and environments variations, since the
real-world RAO tasks often involve diverse resources, agent types and objectives. MARL
systems must generalize well across diverse tasks and rapidly adapt to the new task. These

M. A. Hady et al.1 3Page 41 of 49  354

capabilities  are  essential  in  domains  with  heterogeneity  like  energy-efficient  scheduling
(Shen et al. 2022), 6 G resource management (Du et al. 2022; Hu et al. 2024), and hetero-
geneous V2X networks (Zhao et al. 2023; Zhong et al. 2024). Enhancing generalization,
policy transfer and fine-tuning across structurally related scenarios remains an open chal-
lenge with high impact to the community. The growing use of Transformer-based MARL
offers a universal policy handling the adaptability in dynamic number of inputs or outputs
(Hu et al. 2021) and enhanced sequence modeling and facilitates long-horizon planning and
synchronization (Wen et al. 2022).

Additionally, the integration of MARL with Federated learning (Zhang et al. 2021; Li
et  al.  2022;  Jiang  et  al.  2025),  emerging  technologies  such  as  Quantum  computing  (Yun
et al. 2023) and Safe-MARL (Melcer et al. 2022) also presents new opportunities to develop
secure, decentralized, and resilient RAO systems.

Bridging the gap between simulation and real-world deployment is an urgent need. As
discussed in the Sect. 5.6, more realistic benchmark or simulators can minimize this gap.
The use of Large-scale digital twins also offer realistic, high-fidelity simulations for vali-
dating MARL algorithms under complex, evolving scenarios, thereby reducing sim-to-real
transfer issues. Additionally, the integration of Edge AI enables low-latency, localized deci-
sion-making for time-critical RAO applications–such as smart grids, industrial automation,
and connected vehicles–while minimizing reliance on centralized infrastructure.

These  research  directions  highlight  the  urgent  need  for  scalable,  adaptive,  safe,  and
deployable MARL to address the exponential growing of RAO domains affecting higher
problem complexity and demands of real-world resource allocation optimization problems.

7  Conclusion

This survey examines the intersection of MARL and RAO, highlighting recent advances
and emerging trends in this rapidly evolving area. MARL has demonstrated considerable
potential in addressing the challenges of decentralized and dynamic resource allocation by
enabling agents to learn and adapt in complex, uncertain environments. We reviewed core
methodologies, surveyed applications across diverse domains, and analyzed the strengths
and limitations of existing approaches.

Despite  this  progress,  several  key  challenges  remain,  including  non-stationary,  lim-
ited scalability, coordination complexity, and the need for more generalizable algorithms.
Tackling these issues calls for further research into improved training paradigms, adaptive
communication  mechanisms,  and  hybrid  techniques  that  integrate  MARL  with  classical
optimization strategies.

Future work should also prioritize the deployment of MARL in emerging domains, the
establishment  of  standardized  RAO  benchmarks,  and  the  development  of  task-relevant
evaluation metrics. By addressing these gaps, the community can advance the capabilities
of MARL and broaden its impact on real-world resource allocation systems.

Acknowledgements  This work has been supported by the SmartSat CRC, whose activities are funded by the
Australian Government’s CRC Program.

Author contributions  M.A.H. (Mohamad A. Hady) led the development of the manuscript content and per-
formed the primary research and writing. S.H. (Siyi Hu) contributed to both the manuscript content and the

Multi-agent reinforcement learning for resources allocation optimization:…1 3354  Page 42 of 49

overall framework design, and served as the corresponding author. M.P. (Mahardhika Pratama), J.C. (Jimmy
Cao), and R.K. (Ryszard Kowalczyk) provided supervision, critical suggestions, and contributed to discus-
sions throughout the development of the manuscript. All authors reviewed and approved the final version of
the manuscript.

Funding  Open Access funding enabled and organized by CAUL and its Member Institutions

Data availability  No datasets were generated or analysed during the current study.

Declarations

Conflict of interest  The authors declare no Conflict of interest.

Open  Access    This  article  is  licensed  under  a  Creative  Commons Attribution  4.0  International  License,
which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as
you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons
licence,  and  indicate  if  changes  were  made.  The  images  or  other  third  party  material  in  this  article  are
included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material.
If material is not included in the article’s Creative Commons licence and your intended use is not permitted
by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the
copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

References

Abid MS, Apon HJ, Hossain S, Ahmed A, Ahshan R, Lipu MH (2024) A novel multi-objective optimization
based multi-agent deep reinforcement learning approach for microgrid resources planning. Appl Energy
353:122029

Ahmed M, Liu J, Mirza MA, Khan WU, Al-Wesabi FN (2023) Marl based resource allocation scheme lever-
aging vehicular cloudlet in automotive-industry 5.0. Journal of King Saud University 35(6):101420
Ahrarinouri M, Rastegar M, Seifi AR (2020) Multiagent reinforcement learning for energy management in

residential buildings. IEEE Trans Ind Inf 17(1):659–666

Alam MR, St-Hilaire M, Kunz T (2016) Computational methods for residential energy cost optimization in

smart grids: a survey. ACM Comput Surv 49(1):1–34

Alcaraz J, Maroto C (2001) A robust genetic algorithm for resource allocation in project scheduling. Ann

Oper Res 102:83–109

Allahham MS, Abdellatif AA, Mhaisen N, Mohamed A, Erbad A, Guizani M (2022) Multi-agent reinforce-
ment learning for network selection and resource allocation in heterogeneous multi-rat networks. IEEE
Trans Cogn Commun Netw 8(2):1287–1300

Antonio GP, Maria-Dolores C (2022) Multi-agent deep reinforcement learning to manage connected autono-

mous vehicles at tomorrow’s intersections. IEEE Trans Veh Technol 71(7):7033–7043

Attiya G, Hamam Y (2006) Task allocation for maximizing reliability of distributed systems: a simulated

annealing approach. J Parallel Distrib Comput 66(10):1259–1266

Bi J, Yuan  H,  Duanmu  S,  Zhou M, Abusorrah A  (2020)  Energy-optimized partial computation offloading
in mobile-edge computing with genetic simulated-annealing-based particle swarm optimization. IEEE
Internet Things J 8(5):3774–3785

Binyamin SS, Ben Slama S (2022) Multi-agent systems for resource allocation and scheduling in a smart

grid. Sensors 22(21):8099

Bratton D, Kennedy J (2007) Defining a standard for particle swarm optimization. In: 2007 IEEE swarm

intelligence symposium. IEEE, pp 120–127

Bu L, Babu R, De Schutter B et al (2008) A comprehensive survey of multiagent reinforcement learning.

IEEE Trans Syst Man Cybern C Appl Rev 38(2):156–172

Cao Z, Zhou P, Li R, Huang S, Wu D (2020) Multiagent deep reinforcement learning for joint multichan-
nel  access  and  task  offloading  of  mobile-edge  computing  in  industry  4.0.  IEEE  Internet  Things  J
7(7):6201–6213

Cardon A, Galinho T, Vacher JP (2000) Genetic algorithms using multi-objectives in a multi-agent system.

Robot Auton Syst 33(2–3):179–190

M. A. Hady et al.1 3Page 43 of 49  354

Cesana M, Malanchini I, Capone A (2008) Modelling network selection and resource allocation in wireless
access networks with non-cooperative games. In: 2008 5th IEEE international conference on mobile ad
hoc and sensor systems. IEEE, pp 404–409

Charbonnier F, Morstyn T, McCulloch MD (2022) Scalable multi-agent reinforcement learning for distrib-

uted control of residential energy flexibility. Appl Energy 314:118825

Chen M, Gündüz D, Huang K, Saad W, Bennis M, Feljan AV, Poor HV (2021) Distributed learning in wire-
less networks: recent progress and future challenges. IEEE J Sel Areas Commun 39(12):3579–3605
Chen  S,  Dong  J,  Ha  P,  Li Y,  Labi  S  (2021)  Graph  neural  network  and  reinforcement  learning  for  multi-
agent  cooperative  control  of  connected  autonomous  vehicles.  Comput-Aided  Civil  Infrastruct  Eng
36(7):838–857

Chen  P,  Liu  S,  Wang  X,  Kamwa  I  (2022)  Physics-shielded  multi-agent  deep  reinforcement  learning  for
safe active voltage control with photovoltaic/battery energy storage systems. IEEE Trans Smart Grid
14(4):2656–2667

Chen  D,  Hajidavalloo  MR,  Li  Z,  Chen  K,  Wang  Y,  Jiang  L,  Wang  Y  (2023)  Deep  multi-agent  rein-
forcement  learning  for  highway  on-ramp  merging  in  mixed  traffic.  IEEE  Trans  Intell  Transp  Syst
24(11):11623–11638

Chen Y, Sun Y, Yu H, Taleb T (2024) Joint task and computing resource allocation in distributed edge com-
puting systems via multi-agent deep reinforcement learning. IEEE Trans Netw Sci Eng.  h t t p s : / / d o i . o r g
/ 1 0 . 1 1 0 9 / T N S E . 2 0 2 4 . 3 3 7 5 3 7 4

Costa B, Carvalho L, Rosa M, Araujo A, et al (2022) Computational resource allocation in fog computing: a

comprehensive survey. ACM computing surveys

Deng Y (2025) A reinforcement learning approach to traffic scheduling in complex data center topologies. J

Comput Technol Softw. https://doi.org/10.5281/zenodo.15164624

Du  X,  Wang  T,  Feng  Q, Ye  C,  Tao  T,  Wang  L,  Shi Y,  Chen  M  (2022)  Multi-agent  reinforcement  learn-
ing  for  dynamic  resource  management  in  6G  in-X  subnetworks.  IEEE  Trans  Wireless  Commun
22(3):1900–1914

Ergün S (2025) Resource allocation optimization for effective vehicle network communications using multi-

agent deep reinforcement learning. J Dyn Games 12(2):134–156

Feriani A,  Hossain  E  (2021)  Single  and  multi-agent  deep  reinforcement  learning  for AI-enabled  wireless

networks: a tutorial. IEEE Commun Surv Tutor 23(2):1226–1252

Finn C, Abbeel P, Levine S (2017) Model-agnostic meta-learning for fast adaptation of deep networks. In:

International conference on machine learning. PMLR, pp 1126–1135

Gao X, Liu R, Kaushik A (2020) Hierarchical multi-agent optimization for resource allocation in cloud com-

puting. IEEE Trans Parallel Distrib Syst 32(3):692–707

Gao Z, Yang L, Dai Y (2022) Fast adaptive task offloading and resource allocation via multiagent reinforce-
ment learning in heterogeneous vehicular fog computing. IEEE Internet Things J 10(8):6818–6835
Gao Z, Yang L, Dai Y (2022) Large-scale computation offloading using a multi-agent reinforcement learning

in heterogeneous multi-access edge computing. IEEE Trans Mob Comput 22(6):3425–3443

Gao Z, Yang L, Dai Y (2023) Large-scale cooperative task offloading and resource allocation in heteroge-

neous MEC systems via multi-agent reinforcement learning. IEEE Internet Things J 11:2303

Gao H, Wang X, Wei W, Al-Dulaimi A, Xu Y (2023) Com-ddpg: task offloading based on multiagent rein-
forcement learning for information-communication-enhanced mobile edge computing in the internet of
vehicles. IEEE transactions on vehicular technology

Gong YJ, Zhang J, Chung HSH, Chen WN, Zhan ZH, Li Y, Shi YH (2012) An efficient resource allocation

scheme using particle swarm optimization. IEEE Trans Evol Comput 16(6):801–816

Guindo LA, Wagner M, Baltussen R, Rindress D, van Til J, Kind P, Goetghebeur MM (2012) From efficacy
to equity: literature review of decision criteria for resource allocation and healthcare decisionmaking.
Cost Eff Resour Alloc 10(1):9. https://doi.org/10.1186/1478-7547-10-9

Guo D, Tang L, Zhang X, Liang YC (2020) Joint optimization of handover control and power allocation
based on multi-agent deep reinforcement learning. IEEE Trans Veh Technol 69(11):13124–13138
Guo J, Chen Y, Hao Y, Yin Z, Yu Y, Li S (2022) Towards comprehensive testing on the robustness of coop-
erative multi-agent reinforcement learning. In: Proceedings of the IEEE/CVF conference on computer
vision and pattern recognition. pp 115–122

Halabian H (2019) Distributed resource allocation optimization in 5G virtualized networks. IEEE J Sel Areas

Commun 37(3):627–642

Hansen EA, Bernstein DS, Zilberstein S (2004) Dynamic programming for partially observable stochastic

games. In AAAI 4:709–715

Hao  J, Yang T, Tang  H,  Bai  C,  Liu  J,  Meng  Z,  Liu  P, Wang  Z  (2023)  Exploration in  deep  reinforcement
learning: from single-agent to multiagent domain. IEEE transactions on neural networks and learning
systems

Multi-agent reinforcement learning for resources allocation optimization:…1 3354  Page 44 of 49

Heik D, Bahrpeyma F, Reichelt D (2024) Adaptive manufacturing: dynamic resource allocation using multi-

agent reinforcement learning

Herrmann A, Stephenson M, Schaub H (2023) Reinforcement learning for multi-satellite agile earth observing

scheduling under various communication assumptions. In: AAS Rocky Mountain GN &C conference

Herrmann A,  Stephenson  MA,  Schaub  H  (2024)  Single-agent  reinforcement  learning  for  scalable  earth-

observing satellite constellation operations. J Spacecr Rocket 61(1):114–132

Hong Y, Jin Y, Tang Y (2022) Rethinking individual global max in cooperative multi-agent reinforcement

learning. Adv Neural Inf Process Syst 35:32438–32449

Hu J, Wellman MP (2003) Nash q-learning for general-sum stochastic games. J Mach Learn Res 4:1039–1069
Hu J, Zhang H, Song L, Schober R, Poor HV (2020) Cooperative internet of UAVs: distributed trajectory

design by multi-agent deep reinforcement learning. IEEE Trans Commun 68(11):6807–6821

Hu S, Zhu F, Chang X, Liang X (2021) Updet: universal multi-agent reinforcement learning via policy decou-

pling with transformers. arXiv:2101.08001

Hu B, Zhang W, Gao Y, Du J, Chu X (2024) Multi-agent deep deterministic policy gradient-based computa-
tion  offloading  and  resource  allocation  for  ISAC-aided  6G  V2X  networks.  IEEE  Internet  Things  J.
https://doi.org/10.1109/JIOT.2024.3432728

Hu D, Li Z, Ye Z, Peng Y, Xi W, Cai T (2024) Multi-agent graph reinforcement learning for decentralized

volt-var control in power distribution systems. Int J Electr Power Energy Syst 155:109531

Hua M, Qi X, Chen D, Jiang K, Liu ZE, Sun H, Zhou Q, Xu H (2025) Multi-agent reinforcement learning
for connected and automated vehicles control: recent advancements and future prospects. IEEE Trans
Automat Sci Eng. https://doi.org/10.1109/TASE.2025.3574280

Huang B, Zhou M, Lu XS, Abusorrah A (2023) Scheduling of resource allocation systems with timed petri

nets: a survey. ACM Comput Surv 55(11):1–27

Hwang S, Lee H, Kim M, Lee I (2025) Multi-agent deep reinforcement learning for decentralized multi-UAV
mobile edge computing networks. IEEE Internet Things J. https://doi.org/10.1109/JIOT.2025.3527016

Ibaraki T, Katoh N (1988) Resource allocation problems: algorithmic approaches. MIT press, Cambridge
Jain V, Kumar B (2023) Qos-aware task offloading in fog environment using multi-agent deep reinforcement

learning. J Netw Syst Manage 31(1):7

Jayanetti A, Halgamuge S, Buyya R (2024) Multi-agent deep reinforcement learning framework for renew-
able energy-aware workflow scheduling on distributed cloud data centers. IEEE Trans Parallel Distrib
Syst. https://doi.org/10.1109/TPDS.2024.3360448

Jendoubi I, Bouffard F (2023) Multi-agent hierarchical reinforcement learning for energy management. Appl

Energy 332:120500

Ji  Y,  Wang  Y,  Zhao  H,  Gui  G,  Gacanin  H,  Sari  H, Adachi  F  (2023)  Multi-agent  reinforcement  learning
resources allocation method using dueling double deep q-network in vehicular networks. IEEE Trans
Veh Technol 72(10):13447–13460

Jiandong Z, Qiming Y, Guoqing S, Yi L, Yong W (2021) UAV cooperative air combat maneuver decision

based on multi-agent reinforcement learning. J Syst Eng Electron 32(6):1421–1438

Jiang Y (2015) A survey of task allocation and load balancing in distributed systems. IEEE Trans Parallel

Distrib Syst 27(2):585–599

Jiang C, Sheng Z (2009) Case-based reinforcement learning for dynamic inventory control in a multi-agent

supply-chain system. Expert Syst Appl 36(3):6520–6526

Jiang W, Zhan Y, Fang X (2025) Satellite edge computing for mobile multimedia communications: a multi-
agent  federated  reinforcement  learning  approach. ACM  Transactions  on Autonomous  and Adaptive
Systems

Jing X, Yao X, Liu M, Zhou J (2024) Multi-agent reinforcement learning based on graph convolutional net-

work for flexible job shop scheduling. J Intell Manuf 35(1):75–93

Ju Y, Chen Y, Cao Z, Liu L, Pei Q, Xiao M, Ota K, Dong M, Leung VC (2023) Joint secure offloading and
resource allocation for vehicular edge computing network: a multi-agent deep reinforcement learning
approach. IEEE Trans Intell Transp Syst 24(5):5555–5569

Jun-Han  W,  He  H,  Cha  J,  Jeong  I,  Chang-Jun A  (2025)  Multi-agent  reinforcement  learning  for  efficient

resource allocation in internet of vehicles. Electronics 14(1):192

Kang H, Chang X, Mišić J, Mišić VB, Fan J, Liu Y (2023) Cooperative UAV resource allocation and task
offloading in hierarchical aerial computing systems: a mappo-based approach. IEEE Internet Things J
10(12):10497–10509

Kennedy J, Eberhart R (1995) Particle swarm optimization. In: Proceedings of ICNN’95-international con-

ference on neural networks, vol 4. IEEE, pp 1942–1948

Khan SU, Ahmad I, (2006) Non-cooperative, semi-cooperative, and cooperative games-based grid resource
allocation. In: Proceedings 20th IEEE international parallel & distributed processing symposium. IEEE,
pp 10–pp

M. A. Hady et al.1 3Page 45 of 49  354

Khan AA, Abolhasan M, Ni W, Lipman J, Jamalipour A (2019) A hybrid-fuzzy logic guided genetic algorithm
(h-flga) approach for resource optimization in 5g vanets. IEEE Trans Veh Technol 68(7):6964–6974
Khani M, Sadr MM, Jamali S (2024) Deep reinforcement learning-based resource allocation in multi-access

edge computing. Concurr Comput Pract Exp 36(15):e7995

Kim Y, Lim H (2021) Multi-agent reinforcement learning-based resource management for end-to-end net-

work slicing. IEEE Access 9:56178–56190. https://doi.org/10.1109/ACCESS.2021.3072435

Kirkpatrick  S,  Gelatt  CD  Jr,  Vecchi  MP  (1983)  Optimization  by  simulated  annealing.  Science

220(4598):671–680

Konda V, Tsitsiklis J (1999) Actor-critic algorithms. Adv Neural Inf Process Syst 12
Kosanoglu F, Atmis M, Turan HH (2024) A deep reinforcement learning assisted simulated annealing algo-

rithm for a maintenance planning problem. Ann Oper Res 339(1):79–110

Kumari A, Kakkar R, Tanwar S, Garg D, Polkowski Z, Alqahtani F, Tolba A (2024) Multi-agent-based decen-
tralized residential energy management using deep reinforcement learning. J Build Eng 87:109031
Lee N, Woo J, Kim S (2025) A deep reinforcement learning ensemble for maintenance scheduling in offshore

wind farms. Appl Energy 377:124431

Lei L, Tan Y, Zheng K, Liu S, Zhang K, Shen X (2020) Deep reinforcement learning for autonomous internet

of things: model, applications and challenges. IEEE Commun Surv Tutor 22(3):1722–1760

Li T, Zhu K, Luong NC, Niyato D, Wu Q, Zhang Y, Chen B (2022) Applications of multi-agent reinforce-
ment learning in future internet: a comprehensive survey. IEEE Commun Surv Tutor 24(2):1240–1279
Li X, Lu L, Ni W, Jamalipour A, Zhang D, Du H (2022) Federated multi-agent deep reinforcement learning for

resource allocation of vehicle-to-vehicle communications. IEEE Trans Veh Technol 71(8):8810–8824

Li S, Jin J, Afrin M, Ge X, Fu J, Tian YC (2025) Mobility-as-a-resilience-service in internet of robotic things
through robust multi-agent deep reinforcement learning. IEEE Internet Things J.  h t t p s : / / d o i . o r g / 1 0 . 1 1
0 9 / J I O T . 2 0 2 5 . 3 5 3 5 1 4 8

Liao  X,  Hu  X,  Liu  Z,  Ma  S,  Xu  L,  Li  X,  Wang  W,  Ghannouchi  FM  (2020)  Distributed  intelligence:  a
verification  for  multi-agent  drl-based  multibeam  satellite  resource  allocation.  IEEE  Commun  Lett
24(12):2785–2789

Lin JT, Chiu CC (2018) A hybrid particle swarm optimization with local search for stochastic resource alloca-

tion problem. J Intell Manuf 29(3):481–495

Liu Z, Deng Y (2025) Resource allocation strategy for vehicular communication networks based on multi-

agent deep reinforcement learning. Vehicular Commun 53:100895

Liu XF, Zhang J, Wang J (2022) Cooperative particle swarm optimization with a bilevel resource allocation

mechanism for large-scale dynamic optimization. IEEE Trans Cybern 53(2):1000–1011

Liu Y, Fan J, Zhao L, Shen W, Zhang C (2023) Integration of deep reinforcement learning and multi-agent
system  for  dynamic  scheduling  of  re-entrant  hybrid  flow  shop  considering  worker  fatigue  and  skill
levels. Robotics and Computer-Integrated Manufacturing 84:102605

Liu P, An K, Lei J, Sun Y, Liu W, Chatzinotas S (2024) Computation rate maximization for SCMA-aided
edge computing in IoT networks: a multi-agent reinforcement learning approach. IEEE Trans Wireless
Commun. https://doi.org/10.1109/TWC.2024.3371791

Lotfi F, Afghah F (2025) Meta reinforcement learning approach for adaptive resource optimization in o-ran.

In: 2025 IEEE wireless communications and networking conference (WCNC). IEEE, pp 1–6

Lowe R, Wu Y, Tamar A, Harb J, Abbeel OP, Mordatch I (2017) Multi-agent actor-critic for mixed coopera-
tive-competitive environments. In: Advances in neural information processing systems, pp 6379–6390
Lu Y, Xiang Y, Huang Y, Yu B, Weng L, Liu J (2023) Deep reinforcement learning based optimal schedul-
ing of active distribution system considering distributed generation, energy storage and flexible load.
Energy 271:127087

Ma C, Li A, Du Y, Dong H, Yang Y (2024) Efficient and scalable reinforcement learning for large-scale net-

work control. Nat Mach Intell 6:1–15

Mao H, Alizadeh M, Menache I, Kandula S (2016) Resource management with deep reinforcement learning.

In: Proceedings of the 15th ACM workshop on hot topics in networks, pp 50–56

Mei R, Wang Z (2024) Multi-agent deep reinforcement learning-based resource allocation for cognitive radio

networks. IEEE Trans Veh Technol. https://doi.org/10.1109/TVT.2024.3486156

Melcer D, Amato C, Tripakis S (2022) Shield decentralization for safe multi-agent reinforcement learning.

Adv Neural Inf Process Syst 35:13367–13379

Meng F, Chen P, Wu L, Cheng J (2020) Power allocation in multi-user cellular networks: deep reinforcement

learning approaches. IEEE Trans Wireless Commun 19(10):6255–6267

Mnih V, Badia AP, Mirza M, GravesA, Lillicrap T, HarleyT, Silver D, Kavukcuoglu K (2016) Asynchronous
methods for deep reinforcement learning. In: International conference on machine learning. PMLR, pp
1928–1937

Multi-agent reinforcement learning for resources allocation optimization:…1 3354  Page 46 of 49

Mondal A, Mishra D, Alexandropoulos GC, Al-Nahari A, Jäntti R (2025) Multi-agent reinforcement learning
for offloading cellular communications with cooperating UAVs. IEEE Transactions on aerospace and
electronic systems

Naderializadeh N, Sydir JJ, Simsek M, Nikopour H (2021) Resource management in wireless networks via

multi-agent deep reinforcement learning. IEEE Trans Wireless Commun 20(6):3507–3523

Nagarajan S, Rani PS, Vinmathi M, Subba Reddy V, Saleth ALM, Abdus Subhahan D (2025) Multi agent
deep  reinforcement  learning  for  resource  allocation  in  container-based  clouds  environments.  Expert
Syst 42(1):e13362

Nair AS, Hossen T, Campion M, Selvaraj DF, Goveas N, Kaabouch N, Ranganathan P (2018) Multi-agent
systems  for  resource  allocation  and  scheduling  in  a  smart  grid.  Technol  Econ  Smart  Grids  Sustain
Energy 3:1–15

Nasir YS, Guo D (2019) Multi-agent deep reinforcement learning for dynamic power allocation in wireless

networks. IEEE J Sel Areas Commun 37(10):2239–2250

Nguyen TT, Nguyen ND, Nahavandi S (2020) Deep reinforcement learning for multiagent systems: a review

of challenges, solutions, and applications. IEEE Trans Cybern 50(9):3826–3839

Ning Z, Xie L (2024) A survey on multi-agent reinforcement learning and its application. J Autom Intell.

https://doi.org/10.1016/j.jai.2024.02.003

Noor-A-Rahim  M,  Liu  Z,  Lee  H, Ali  GMN,  Pesch  D,  Xiao  P  (2020) A  survey  on  resource  allocation  in

vehicular networks. IEEE Trans Intell Transp Syst 23(2):701–721

Orr J, Dutta A (2023) Multi-agent deep reinforcement learning for multi-robot applications: a survey. Sensors

(Basel) 23(7):3625

Parvini  M,  Javan  MR,  Mokari  N, Abbasi  B,  Jorswieck  EA  (2023) Aoi-aware  resource  allocation  for  pla-
toon-based c-v2x networks via multi-agent multi-task reinforcement learning. IEEE Trans Veh Technol
72(8):9880–9896

Patriksson  M  (2008) A  survey  on  the  continuous  nonlinear  resource  allocation  problem.  Eur  J  Oper  Res

185(1):1–46

Pendyala A, Dettmer J, Glasmachers T, Atamna A (2024) Containergym: a real-world reinforcement learning
benchmark for resource allocation. In: Nicosia G, Ojha V, La Malfa E, La Malfa G, Pardalos PM, Ume-
ton R (eds) Machine learning, optimization, and data science. Springer, Cham, pp 78–92

Rao N, Xu H, Qi Z, Wang D, Zhang Y (2024) Fast adaptive jamming resource allocation against frequency-
hopping spread spectrum in wireless sensor networks via meta deep reinforcement learning. IEEE Trans
Aerosp Electron Syst. https://doi.org/10.1109/TAES.2024.3418944

Rashid T, Samvelyan M, De Witt CS, Farquhar G, Foerster J, Whiteson S (2020) Monotonic value function

factorisation for deep multi-agent reinforcement learning. J Mach Learn Res 21(178):1–51

Ren  L,  Fan  X,  Cui  J,  Shen  Z,  Lv Y,  Xiong  G  (2022) A  multi-agent  reinforcement  learning  method  with
route  recorders  for  vehicle  routing  in  supply  chain  management.  IEEE  Trans  Intell  Transp  Syst
23(9):16410–16420

Roesch M, Linder C, Zimmermann R, Rudolf A, Hohmann A, Reinhart G (2020) Smart grid for industry

using multi-agent reinforcement learning. Appl Sci 10(19):6900

Saaty TL, Vargas LG, Dellmann K (2003) The allocation of intangible resources: the analytic hierarchy pro-

cess and linear programming. Socioecon Plann Sci 37(3):169–184

Sadatdiynov K, Cui L, Zhang L, Huang JZ, Salloum S, Mahmud MS (2023) A review of optimization meth-
ods for computation offloading in edge computing networks. Digit Commun Netw 9(2):450–461
Sarah A, Nencioni G, Khan MMI (2023) Resource allocation in multi-access edge computing for 5g-and-

beyond networks. Comput Netw 227:109720

Schulman J (2015) Trust region policy optimization. arXiv:1502.05477
Schulman J, Wolski F, Dhariwal P, Radford A, Klimov O (2017) Proximal policy optimization algorithms.

arXiv:1707.06347

Seid AM, Boateng GO, Mareri B, Sun G, Jiang W (2021) Multi-agent DRL for task offloading and resource

allocation in multi-UAV enabled IoT edge network. IEEE Trans Netw Serv Manag 18(4):4531–4547

Shao  X,  Kshitij  FS,  Kim  CS  (2024)  Gails:  an  effective  multi-object  job  shop  scheduler  based  on  genetic

algorithm and iterative local search. Sci Rep 14(1):2068

Sharma S, Wonsik Y (2021) Multiobjective optimization for resource allocation in full-duplex large distrib-

uted MIMO systems. Adv Electr Comput Eng 21(2):67

Sharma S, Yoon W (2018) Multi-objective energy efficient resource allocation for wpcn. Int J Eng Res Tech

11:2035–2043

Shen R, Zhong S, Wen X, An Q, Zheng R, Li Y, Zhao J (2022) Multi-agent deep reinforcement learning

optimization framework for building energy system with renewable energy. Appl Energy 312:118724

Singh AK, Dziurzanski P, Mendis HR, Indrusiak LS (2017) A survey and comparative study of hard and soft
real-time  dynamic  resource  allocation  strategies  for  multi-/many-core  systems. ACM  Comput  Surv.
https://doi.org/10.1145/3057267

M. A. Hady et al.1 3Page 47 of 49  354

Spinellis D, Papadopoulos C, Smith JM (2000) Large production line optimization using simulated anneal-

ing. Int J Prod Res 38(3):509–541

Stephenson M Schaub H (2024a) Reinforcement learning for earth-observing satellite autonomy with event-

based task intervals. In AAS Rocky Mountain GN &C conference, Breckenridge, CO

Stephenson MA, Schaub H (2024b) Bsk-rl: modular, high-fidelity reinforcement learning environments for

spacecraft tasking. In: 75th international astronautical congress, Milan, Italy, IAF

Suman B, Kumar P (2006) A survey of simulated annealing as a tool for single and multiobjective optimiza-

tion. J Oper Res Soc 57(10):1143–1160

Sun X, Qiu J (2021) Two-stage volt/var control in active distribution networks with multi-agent deep rein-

forcement learning method. IEEE Trans Smart Grid 12(4):2903–2912

Sunehag P, Lever G, Gruslys A, Czarnecki WM, Zambaldi V, Jaderberg M, Lanctot M, Sonnerat N, Leibo JZ,
Tuyls K, Graepel T (2018) Value-decomposition networks for cooperative multi-agent learning based
on team reward. In: Proceedings of the 17th international conference on autonomous agents and Mul-
tiAgent systems. International Foundation for Autonomous Agents and Multiagent Systems, AAMAS
’18, Richland, SC, pp 2085–2087

Sutton RS (1988) Learning to predict by the methods of temporal differences. Mach Learn 3:9–44
Sutton RS, Barto AG (2018) Reinforcement learning: an introduction. MIT press, Cambridge
Suzuki A, Kawahara R, Harada S (2022) Cooperative multi-agent deep reinforcement learning for dynamic
virtual network allocation with traffic fluctuations. IEEE Trans Netw Serv Manage 19(3):1982–2000

Tang J, So DK, Alsusa E, Hamdi KA, Shojaeifard A (2015) Resource allocation for energy efficiency optimi-

zation in heterogeneous networks. IEEE J Sel Areas Commun 33(10):2104–2117

Towers  M,  Kwiatkowski A,  Terry  J,  Balis  JU,  De  Cola  G,  Deleu  T,  Goulão  M,  Kallinteris A,  Krimmel
M,  KG  A  et  al  (2024)  Gymnasium:  a  standard  interface  for  reinforcement  learning  environments.
arXiv:2407.17032

Tseng FH, Wang X, Chou LD, Chao HC, Leung VC (2017) Dynamic resource prediction and allocation for

cloud data center using the multiobjective genetic algorithm. IEEE Syst J 12(2):1688–1699

Tu YH, Ma YW (2025) A comprehensive multi-agent deep reinforcement learning framework with adaptive
interaction strategies for contention window optimization in IEEE 802.11 wireless lans. ICT Express.
https://doi.org/10.1016/j.icte.2025.01.010

Ushakov  IA  (2013)  Optimal  resource  allocation:  with  practical  statistical  applications  and  theory.  Wiley,

Hoboken

Van Hasselt H, Guez A, Silver D (2016) Deep reinforcement learning with double q-learning. In: Proceedings

of the AAAI conference on artificial intelligence, vol 30

Vengerov D (2007) A reinforcement learning approach to dynamic resource allocation. Eng Appl Artif Intell

20(3):383–390

Wang Z, Schaul T, Hessel M, Hasselt H, Lanctot M, Freitas N (2016) Dueling network architectures for deep
reinforcement learning. In: International conference on machine learning. PMLR, pp 1995–2003
Wang X, Ke L, Qiao Z, Chai X (2020) Large-scale traffic signal control using a novel multiagent reinforce-

ment learning. IEEE Trans Cybern 51(1):174–187

Wang Y, Xu T, Niu X, Tan C, Chen E, Xiong H (2020) Stmarl: a spatio-temporal multi-agent reinforcement
learning approach for cooperative traffic light control. IEEE Trans Mob Comput 21(6):2228–2242
Wang J, Xu W, Gu Y, Song W, Green TC (2021) Multi-agent reinforcement learning for active voltage control
on power distribution networks. In: Ranzato M, Beygelzimer A, Dauphin Y, Liang P, Vaughan JW (eds)
Adv Neural Inf Process Syst, vol 34. Curran Associates Inc, New York, pp 3271–3284

Wang L, Liang H, Mao G, Zhao D, Liu Q, Yao Y, Zhang H (2024) Resource allocation for dynamic platoon
digital  twin  networks:  a  multi-agent  deep  reinforcement  learning  method.  IEEE Trans Veh Technol.
https://doi.org/10.1109/TVT.2024.3414447

Wang Q, Li W, Mohajer A (2024) Load-aware continuous-time optimization for multi-agent systems: toward

dynamic resource allocation and real-time adaptability. Comput Netw 250:110526

Wang C, Wang M, Wang A, Zhang X, Zhang J, Ma H, Yang N, Zhao Z, Lai CS, Lai LL (2025) Multiagent
deep reinforcement learning-based cooperative optimal operation with strong scalability for residential
microgrid clusters. Energy 314:134165

Wei H, Chen C, Zheng G, Wu K, Gayah V, Xu K, Li Z (2019) Presslight: learning max pressure control to
coordinate traffic signals in arterial network. In: Proceedings of the 25th ACM SIGKDD international
conference on knowledge discovery & data mining. Association for Computing Machinery, KDD ’19,
New York, NY, USA, pp 1290–1298

Wei W, Yang R, Gu H, Zhao W, Chen C, Wan S (2021) Multi-objective optimization for resource allocation

in vehicular cloud computing networks. IEEE Trans Intell Transp Syst 23(12):25536–25545

Wei Z, Li B, Zhang R, Cheng X, Yang L (2023) Many-to-many task offloading in vehicular fog computing: a

multi-agent deep reinforcement learning approach. IEEE Trans Mob Comput 23(3):2107–2122

Multi-agent reinforcement learning for resources allocation optimization:…1 3354  Page 48 of 49

Wen G, Fu J, Dai P, Zhou J (2021) Dtde: a new cooperative multi-agent reinforcement learning framework.

Innov 2(4):100162

Wen M, Kuba J, Lin R, Zhang W, Wen Y, Wang J, Yang Y (2022) Multi-agent reinforcement learning is a

sequence modeling problem. Adv Neural Inf Process Syst 35:16509–16521

Wong A,  Bäck T,  Kononova AV,  Plaat A  (2023)  Deep  multiagent  reinforcement  learning:  challenges  and

directions. Artif Intell Rev 56(6):5023–5056

Wu H, Pang GKH, Choy KL, Lam HY (2018) Dynamic resource allocation for parking lot electric vehicle
recharging using heuristic fuzzy particle swarm optimization algorithm. Appl Soft Comput 71:538–552
Wu T, Zhou P, Liu K, Yuan Y, Wang X, Huang H, Wu DO (2020) Multi-agent deep reinforcement learning for

urban traffic light control in vehicular networks. IEEE Trans Veh Technol 69(8):8243–8256

Wu G, Xu Z, Zhang H, Shen S, Yu S (2023) Multi-agent drl for joint completion delay and energy consump-

tion with queuing theory in mec-based iiot. J Parallel Distrib Comput 176:80–94

Wu H, Qiu D, Zhang L, Sun M (2024) Adaptive multi-agent reinforcement learning for flexible resource
management in a virtual power plant with dynamic participating multi-energy buildings. Appl Energy
374:123998

Xiao Y, Song Y, Liu J (2023) Multi-agent deep reinforcement learning based resource allocation for ultra-

reliable low-latency internet of controllable things. IEEE Trans Wireless Commun 22(8):5414–5430
Xu H, Jian C (2024) A meta reinforcement learning-based virtual machine placement algorithm in mobile

edge computing. Clust Comput 27(2):1883–1896

Xu J, Zhao M, Fortes J, Carpenter R, Yousif M (2008) Autonomic resource management in virtualized data

centers using fuzzy logic-based approaches. Clust Comput 11:213–227

Xu X, Jia Y, Xu Y, Xu Z, Chai S, Lai CS (2020) A multi-agent reinforcement learning-based data-driven

method for home energy management. IEEE Trans Smart Grid 11(4):3201–3211

Xu X, Xu K, Zeng Z, Tang J, He Y, Shi G, Zhang T (2024) Collaborative optimization of multi-energy multi-
microgrid system: a hierarchical trust-region multi-agent reinforcement learning approach. Appl Energy
375:123923

Xue K, Xu J, Yuan L, Li M, Qian C, Zhang Z, Yu Y (2022) Multi-agent dynamic algorithm configuration. Adv

Neural Inf Process Syst 35:20147–20161

Xue J, Wang L, Yu Q, Mao P (2025) Multi-agent deep reinforcement learning-based partial offloading and

resource allocation in vehicular edge computing networks. Comput Commun 234:108081

Yánez W, Mahmud R, Bahsoon R, Zhang Y, Buyya R (2020) Data allocation mechanism for internet-of-
things systems with blockchain. IEEE Internet Things J 7(4):3509–3522.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / J I O
T . 2 0 2 0 . 2 9 7 2 7 7 6

Yang Y, Luo R, Li M, Zhou M, Zhang W, Wang J (2018) Mean field multi-agent reinforcement learning. In:

International conference on machine learning. PMLR, pp 5571–5580

Ye D, Chen J (2013) Non-cooperative games on multidimensional resource allocation. Futur Gener Comput

Syst 29(6):1345–1352

Yin  S, Yu  FR  (2021)  Resource  allocation  and  trajectory  design  in  UAV-aided  cellular  networks  based  on

multiagent reinforcement learning. IEEE Internet Things J 9(4):2933–2943

You X, Li X, Xu Y, Feng H, Zhao J, Yan H (2020) Toward packet routing with fully distributed multiagent

deep reinforcement learning. IEEE Trans Syst Man Cybern Syst 52(2):855–868

Yu L, Qin S, Zhang M, Shen C, Jiang T, Guan X (2021) A review of deep reinforcement learning for smart

building energy management. IEEE Internet Things J 8(15):12046–12063

Yu C, Velu A, Vinitsky E, Gao J, Wang Y, Bayen A, Wu Y (2022) The surprising effectiveness of PPO in

cooperative multi-agent games. Adv Neural Inf Process Syst 35:24611–24624

Yun  WJ,  Kim  JP,  Jung  S,  Kim  JH,  Kim  J  (2023)  Quantum  multiagent  actor-critic  neural  networks  for
internet-connected  multirobot  coordination  in  smart  factory  management.  IEEE  Internet  Things  J
10(11):9942–9952

Zabihi Z, Eftekhari Moghadam AM, Rezvani MH (2023) Reinforcement learning methods for computation

offloading: a systematic review. ACM Comput Surv. https://doi.org/10.1145/3603703

Zeynivand A, Javadpour A, Bolouki S, Sangaiah AK, Ja’fari F, Pinto P, Zhang W (2022) Traffic flow control

using multi-agent reinforcement learning. J Netw Comput Appl 207:103497

Zhang X, Debroy S (2023) Resource management in mobile edge computing: a comprehensive survey. ACM

Comput Surv 55(13s):1–37

Zhang Y, Guo D (2025) Multi-agent reinforcement learning for multi-cell spectrum and power allocation.

IEEE Trans Commun. https://doi.org/10.1109/TCOMM.2025.3534565

Zhang G, Yang K, Chen HH (2012) Resource allocation for wireless cooperative networks: a unified coopera-

tive bargaining game theoretic framework. IEEE Wirel Commun 19(2):38–43

Zhang  H,  Jiang  C,  Beaulieu  NC,  Chu  X,  Wang  X,  Quek  TQ  (2015)  Resource  allocation  for  cognitive
small  cell  networks:  a  cooperative  bargaining  game  theoretic  approach.  IEEE Trans Wirel  Commun
14(6):3481–3493

M. A. Hady et al.1 3Page 49 of 49  354

Zhang H, Feng S, Liu C, Ding Y, Zhu Y, Zhou Z, Zhang W, Yu Y, Jin H, Li Z (2019) Cityflow: a multi-agent
reinforcement learning environment for large scale city traffic scenario. In: The world wide web confer-
ence. Association for Computing Machinery, WWW ’19, New York, NY, USA, pp 3620–3624

Zhang SQ, Zhang Q, Lin J (2019) Efficient communication in multi-agent reinforcement learning via vari-

ance based control. Adv Neural Inf Process Syst. https://doi.org/10.48550/arXiv.1909.02682

Zhang Y, Mou Z, Gao F, Jiang J, Ding R, Han Z (2020) Uav-enabled secure communications by multi-agent

deep reinforcement learning. IEEE Trans Veh Technol 69(10):11599–11611

Zhang K, Cao J, Zhang Y (2021) Adaptive digital twin and multiagent deep reinforcement learning for vehic-

ular edge computing and networks. IEEE Trans Ind Inform 18(2):1405–1413

Zhang M, Dou Y, Chong PHJ, Chan HC, Seet BC (2021) Fuzzy logic-based resource allocation algorithm for

V2X communications in 5G cellular networks. IEEE J Sel Areas Commun 39(8):2501–2513

Zhang W, Yang D, Wu W, Peng H, Zhang N, Zhang H, Shen X (2021) Optimizing federated learning in dis-

tributed industrial iot: a multi-agent approach. IEEE J Sel Areas Commun 39(12):3688–3703

Zhang Y, Zhu H, Tang D, Zhou T, Gui Y (2022) Dynamic job shop scheduling based on deep reinforcement
learning  for  multi-agent  manufacturing  systems.  Robotics  and  Computer-Integrated  Manufacturing
78:102412

Zhang B, Hu W, Ghias AM, Xu X, Chen Z (2023) Multi-agent deep reinforcement learning based distributed
control architecture for interconnected multi-energy microgrid energy management and optimization.
Energy Convers Manage 277:116647

Zhang  JD,  He  Z,  Chan  WH,  Chow  CY  (2023)  Deepmag:  deep  reinforcement  learning  with  multi-agent

graphs for flexible job shop scheduling. Knowledge-Based Systems 259:110083

Zhang H, Zhao H, Liu R, Kaushik A, Gao X, Xu S (2024) Collaborative task offloading optimization for sat-
ellite mobile edge computing using multi-agent deep reinforcement learning. IEEE Trans Veh Technol.
https://doi.org/10.1109/TVT.2024.3405642

Zhang Y, Zheng G, Liu Z, Li Q, Zeng H (2024) Marlens: understanding multi-agent reinforcement learning
for traffic signal control via visual analytics. IEEE Trans Vis Comput Graph.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / T
V C G . 2 0 2 4 . 3 3 9 2 5 8 7

Zhang J, Liu Z, Zhu Y, Shi E, Xu B, Yuen C, Niyato D, Debbah M, Jin S, Ai B et al (2025) Multi-agent rein-

forcement learning in wireless distributed networks for 6g. arXiv:2502.05812

Zhao N, Ye Z, Pei Y, Liang YC, Niyato D (2022) Multi-agent deep reinforcement learning for task offloading

in UAV-assisted mobile edge computing. IEEE Trans Wirel Commun 21(9):6949–6960

Zhao J, Hu F, Li J, Nie Y (2023) Multi-agent deep reinforcement learning based resource management in

heterogeneous v2x networks. Digit Commun Netw

Zheng P, Xia L, Li C, Li X, Liu B (2021) Towards self-x cognitive manufacturing network: an industrial

knowledge graph-based multi-agent reinforcement learning approach. J Manuf Syst 61:16–26

Zhong Y, Kuba JG, Feng X, Hu S, Ji J, Yang Y (2024) Heterogeneous-agent reinforcement learning. J Mach

Learn Res 25:1–67

Zhou H, Jiang K, He S, Min G, Wu J (2023) Distributed deep multi-agent reinforcement learning for coopera-

tive edge caching in internet-of-vehicles. IEEE Trans Wireless Commun 22(12):9595–9609

Zhu X, Luo Y, Liu A, Bhuiyan MZA, Zhang S (2020) Multiagent deep reinforcement learning for vehicular

computation offloading in IoT. IEEE Internet Things J 8(12):9763–9773

Publisher's Note  Springer Nature remains neutral with regard to jurisdictional claims in published maps and
institutional affiliations.

Multi-agent reinforcement learning for resources allocation optimization:…1 3