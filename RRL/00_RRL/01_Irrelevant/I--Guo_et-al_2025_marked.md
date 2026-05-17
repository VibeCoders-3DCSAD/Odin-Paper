Review
The Energy Management Strategies for Fuel Cell Electric
Vehicles: An Overview and Future Directions

Jinquan Guo 1,*, Hongwen He 2

, Chunchun Jia 3 and Shanshan Guo 1

1

2

School of Machinery and Automation, Weifang University, Weifang 261061, China; guoss@wfu.edu.cn
School of Mechanical Engineering, Beijing Institute of Technology, Beijing 100081, China; hwhebit@bit.edu.cn

3 Research Centre for Electric Vehicles and Department of Electrical and Electronic Engineering, The Hong

Kong Polytechnic University, Hong Kong 999077, China; chunchun.jia@polyu.edu.cn

* Correspondence: jqguo@wfu.edu.cn

Abstract

The rapid development of fuel cell electric vehicles (FCEVs) has highlighted the critical
importance of optimizing energy management strategies to improve vehicle performance,
energy efficiency, durability, and reduce hydrogen consumption and operational costs.
However, existing approaches often face limitations in real-time applicability, adaptability
to varying driving conditions, and computational efficiency. This paper aims to provide
a comprehensive review of the current state of FCEV energy management strategies, sys-
tematically classifying methods and evaluating their technical principles, advantages, and
practical limitations. Key techniques, including optimization-based methods (dynamic
programming, model predictive control) and machine learning-based approaches (rein-
forcement learning, deep neural networks), are analyzed and compared in terms of energy
distribution efficiency, computational demand, system complexity, and real-time perfor-
mance. The review also addresses emerging technologies such as artificial intelligence,
vehicle-to-everything (V2X) communication, and multi-energy collaborative control. The
outcomes highlight the main bottlenecks in current strategies, their engineering applicabil-
ity, and potential for improvement. This study provides theoretical guidance and practical
reference for the design, implementation, and advancement of intelligent and adaptive
energy management systems in FCEVs, contributing to the broader goal of efficient and
low-carbon vehicle operation.

Keywords: energy management strategy; model predictive control; reinforcement learning;
transfer learning

1. Introduction

The development of new energy vehicles (NEVs) contributes significantly to reducing
dependence on fossil fuels, enhancing energy diversity, lowering carbon emissions in the
transportation sector, improving air quality, and promoting the transition toward a green
and low-carbon society. At the same time, it facilitates the application of clean energy
sources such as electricity and hydrogen, accelerating the deep integration between the
transportation and energy systems, and thus holds substantial environmental, economic,
and social significance [1–4]. Figure 1 systematically illustrates the relationships between
various NEV technology pathways and their corresponding energy sources, reflecting
a coordinated advancement in energy diversification, CO2 emission reduction, and air
quality improvement. The transition from conventional internal combustion engine vehicles

Academic Editor: Michael Fowler

Received: 9 August 2025

Revised: 11 September 2025

Accepted: 19 September 2025

Published: 22 September 2025

Citation: Guo, J.; He, H.; Jia, C.; Guo,

S. The Energy Management Strategies

for Fuel Cell Electric Vehicles: An

Overview and Future Directions.

World Electr. Veh. J. 2025, 16, 542.

https://doi.org/10.3390/

wevj16090542

Copyright: © 2025 by the authors.

Published by MDPI on behalf of the

World Electric Vehicle Association.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under the terms and

conditions of the Creative Commons

Attribution (CC BY) license

(https://creativecommons.org/

licenses/by/4.0/).

World Electr. Veh. J. 2025, 16, 542

https://doi.org/10.3390/wevj16090542

World Electr. Veh. J. 2025, 16, 542

2 of 26

(ICEVs) to hybrid electric vehicles (HEVs), plug-in hybrid electric vehicles (PHEVs), battery
electric vehicles (BEVs), and finally to fuel cell electric vehicles (FCEVs) demonstrates a
progressive electrification of the powertrain, which aligns with the fundamental logic of
low-carbon transformation in the transport sector. Conventional ICEVs primarily rely
on gasoline and diesel derived from petroleum, which are associated with high carbon
emission intensities. In contrast, HEVs and PHEVs incorporate electric drive systems that
significantly improve energy efficiency and reduce carbon emissions. BEVs rely entirely
on electricity, and their environmental benefits are closely linked to the carbon intensity of
the power generation mix. With the global energy transition underway and the growing
emphasis on environmental sustainability, FCEVs, which make use of hydrogen as fuel
to produce electricity through the electrochemical reaction of hydrogen and oxygen to
drive the electric motor, have become one of the solutions to replace traditional internal
combustion engine vehicles. FCEVs offer distinct advantages, including zero emissions,
superior efficiency, and low noise levels, making them a promising option for reducing
carbon emissions and promoting sustainable transportation development [5–12].

Figure 1. The relationships between various NEV technology pathways and their corresponding
energy sources.

The Toyota Motor Corporation has proposed that the future of the automotive industry
will be characterized by the coexistence and coordinated development of three technological
pathways: battery electric vehicles, hybrid electric vehicles, and fuel cell electric vehicles.
This vision emphasizes that different types of new energy vehicles will play distinct roles
based on their respective advantages, as shown in Figure 2. For instance, BEVs are well-
suited for short-distance urban travel, HEVs offer transitional benefits in improving fuel
efficiency and reducing emissions, while FCEVs, with their fast-refueling capability and
long driving range, are more appropriate for long-distance transportation and commercial
vehicle applications. By establishing a diversified powertrain system, this approach not
only better meets the complex and varied demands of the market but also contributes to
the sustainable development of the automotive industry.

Fuel cell vehicles are typically equipped with energy storage units such as power
batteries and supercapacitors. These auxiliary energy systems work together with the fuel
cell power system. The key challenge for fuel cell vehicle control strategies is how to opti-

 World Electr. Veh. J. 2025, 16, 542

3 of 26

mize the energy flow among the fuel cell power system, power battery, and supercapacitor
through control strategies to achieve the hybrid power system’s high performance [13–25].

Figure 2. The future of the automotive industry from Toyota Motor Corporation’s perspective.

Control strategies for fuel cell vehicles are currently classified into three main types:
rule-based, optimization-based, and machine learning-based approaches. These control
methods have progressed from static control approaches to dynamic adjustments of power
distribution between the fuel cell and energy storage units, tailored to real-time vehicle
driving cycle and driving demands, thereby greatly strengthening the fuel cell vehicle’s
energy management for better performance and efficiency.

To provide a comprehensive understanding of current research in fuel cell electric
vehicle (FCEV) energy management, a systematic literature search was conducted using
Web of Science, Scopus, and IEEE Xplore with keywords such as “Fuel Cell Electric Vehicle”,
“Energy Management Strategy”, and “Reinforcement Learning” for the period 2015–2025.
Peer-reviewed articles directly related to FCEV energy management were included, while
non-English, unrelated, or duplicate studies were excluded. This approach ensures a
structured and comprehensive coverage of existing methods and challenges.

Building on this literature foundation, this paper aims to promote the further develop-
ment of energy management technology by reviewing existing studies and summarizing
key technologies. The specific tasks include: (1) providing an overview of the topological
structure, advantages, and disadvantages of FCEV powertrain systems; (2) classifying
existing energy management methods based on theoretical foundations, with a systematic
review of the latest research progress, including the control principles, technical advan-
tages, and limitations of each method; and (3) discussing future research directions in
energy management technology, with a focus on multi-energy coordination, data-driven
approaches, and artificial intelligence technologies [26–35].

2. The Structural Design of Fuel Cell Hybrid Powertrain System

Fuel cell electric vehicles can be classified into four distinct architectures based on
the integration of fuel cells with auxiliary energy systems: fuel cell standalone powertrain
systems, fuel cell–battery hybrid powertrain systems, fuel cell–supercapacitor hybrid pow-

 World Electr. Veh. J. 2025, 16, 542

4 of 26

ertrain systems, and fuel cell–battery–supercapacitor hybrid powertrain systems. Each of
these configurations exhibits distinct characteristics in terms of energy efficiency, power
density, and dynamic performance, and is selected according to specific application require-
ments and operating conditions [36–38].

2.1. The Fuel Cell Standalone Powertrain System

Figure 3a shows the fuel cell standalone powertrain system, where electricity is pro-
duced directly by the electrochemical reaction of hydrogen and oxygen, which in turn
powers the electric motor that drives the fuel cell hybrid vehicle.

Figure 3. Structure diagram of fuel cell powertrain system. (a) The fuel cell standalone powertrain
system; (b) The fuel cell–battery hybrid powertrain system; (c) The fuel cell–supercapacitor hybrid
powertrain system; (d) The fuel cell-battery-supercapacitor hybrid powertrain system.

This system does not rely on additional energy storage devices or is equipped with
only a small amount of energy storage to maintain short-term stability. As a result, it has
advantages such as a simple structure, low cost, and light weight. In parallel, the fuel cell,
functioning as an environmentally friendly power source, offers high energy conversion
efficiency. However, fuel cells have high requirements for instantaneous power response,
making it difficult to meet high power demands such as acceleration and climbing. When
there is frequent gear shifting or large load fluctuations, the fuel cell may have limited
responsiveness to rapid load changes, leading to efficiency reduction and affecting the
system’s lifespan. Therefore, this system is suitable for applications with relatively stable
operating conditions and lower dynamic performance requirements, and is rarely used in
actual vehicle applications.

It should be emphasized that the relatively slow dynamic response of fuel cells is not
inherently disadvantageous in all applications. For instance, in long-haul buses or logistics
vehicles, where the power demand is relatively stable, the fuel cell can operate under near
steady-state conditions with high efficiency and durability. In contrast, in urban buses or
passenger vehicles with frequent load fluctuations, the limited transient response becomes
more significant, often requiring hybridization with batteries or supercapacitors to meet

  (a)  (b)   (c)  (d)  World Electr. Veh. J. 2025, 16, 542

5 of 26

acceleration and braking demands. This distinction clarifies the suitability of standalone
fuel cell systems for stable-load applications.

2.2. The Fuel Cell-Battery Hybrid Powertrain System

The fuel cell–battery hybrid powertrain system is illustrated in Figure 3b, where
the fuel cell and power battery operate in a coordinated manner. The fuel cell serves
as the primary source of continuous power, primarily supplying energy to the vehicle’s
driving electric motor, whereas the power battery functions to mitigate power fluctuations
and support transient load demands, recover energy, and assist in power output during
acceleration. During deceleration or braking, the power battery recovers energy and
stores it.

This system optimizes control strategies to ensure the fuel cell always operates within
its optimal efficiency range, thereby reducing hydrogen consumption. In addition, the
power battery helps enhance the system’s dynamic response, allowing it to adapt to various
complex operating conditions. However, the system is more complex and costlier, and the
power battery adds weight and occupies more space. Therefore, this system is more suitable
for applications that require frequent start-stop operations, such as urban passenger cars
and logistics vehicles.

2.3. The Fuel Cell-Supercapacitor Hybrid Powertrain System

The fuel cell–supercapacitor hybrid powertrain system is depicted in Figure 3c, where
the fuel cell and supercapacitor collaboratively work. In this configuration, the fuel cell is
primarily responsible for supplying power, while the supercapacitor is responsible for rapid
energy storage and release, effectively supporting transient power demands and enhancing
dynamic performance. During the vehicle acceleration, the supercapacitor discharges
quickly to provide additional power; during deceleration or braking, the supercapacitor
recovers braking energy and stores it. This system optimizes energy use to improve
overall efficiency.

Supercapacitors have high power density and excellent transient performance, making
them effective in supporting short-term high-power demands. At the same time, the
fuel cell can focus on providing stable power, thereby extending its lifespan. However,
supercapacitors have a low energy density and cannot meet long-term high-load demands.
The system is also costlier and has a limited range of applications. Therefore, this system is
primarily used in vehicles that require frequent start-stop operations, such as short-distance
buses and logistics vehicles.

2.4. The Fuel Cell-Battery-Supercapacitor Hybrid Powertrain System

The fuel cell-battery-supercapacitor hybrid powertrain system is shown in Figure 3d.
In this system, the fuel cell, power battery, and supercapacitor function in harmony to
achieve a balance between long-range endurance, high power output, and energy recovery.
The fuel cell serves as the primary power source, the battery stores and delivers energy
for moderate power demands, while the supercapacitor handles instantaneous power
requirements. The subsystems are dynamically optimized through an energy manage-
ment system, which intelligently schedules power distribution to maximize the overall
system performance.

The main advantages of this system lie in its excellent dynamic response capability,
enabling it to adapt to various complex driving cycles. It also maximizes the fuel cell
efficiency, extends the system’s lifespan, and improves overall energy utilization. However,
the system has a complex structure and has stricter development and maintenance require-
ments. Therefore, this system is suitable for applications with extremely high-performance
requirements, such as long-distance buses, heavy-duty trucks, and military vehicles.

World Electr. Veh. J. 2025, 16, 542

6 of 26

2.5. Comparative Summary of Powertrain Architectures

To support system-level design decisions, Table 1 summarizes the key trade-offs
among the four fuel cell powertrain architectures discussed above, with a focus on energy
efficiency, cost, size/weight, and dynamic performance [39,40].

Table 1. The key trade-offs among the four fuel cell powertrain architectures.

Architecture Type

Energy Efficiency

Cost
(USD/kW)

Size/Weight
(kg/kW)

Dynamic
Performance

Standalone Fuel Cell

Fuel Cell–Battery
Hybrid

Fuel
Cell–Supercapacitor
Hybrid

40–55% (sensitive to
load fluctuations)

45–60% (optimized
FC operation)

45–58% (effective
transient support)

800–1200

8–12

500–800

10–15

Poor

Good

600–900

9–13

Excellent

Fuel Cell–Battery–
Supercapacitor Hybrid

50–65% (full-range
optimization)

900–1500

12–18

Excellent

Typical Applications

Low-speed,
stable-load vehicles

Urban buses, logistics
vehicles

Short-distance buses,
delivery vans

Long-haul buses,
heavy-duty trucks

The results indicate that standalone fuel cell systems exhibit relatively low efficiency
(40–55%) and poor dynamic performance, but remain attractive in low-speed, steady-load
applications due to their lowest cost (800–1200 USD/kW) and lightest weight (8–12 kg/kW).
In contrast, the fuel cell–battery hybrid raises efficiency to 45–60% by buffering energy
fluctuations, with moderate cost (500–800 USD/kW) and weight (10–15 kg/kW), making
it widely adopted in urban buses and logistics vehicles. The fuel cell–supercapacitor
hybrid achieves 45–58% efficiency and outstanding transient response, at a cost of
600–900 USD/kW and weight of 9–13 kg/kW, which is advantageous for short-distance
and stop-and-go operations. The three-source hybrid demonstrates the highest efficiency
(50–65%) and dynamic adaptability, but with significantly higher cost (900–1500 USD/kW)
and weight (12–18 kg/kW), making it more suitable for long-haul buses and heavy-duty
trucks. Overall, hybrid configurations clearly outperform standalone fuel cells in efficiency
and adaptability, although the trade-offs in cost and system complexity remain critical
considerations for practical deployment.

3. Research Progress on Energy Management Strategies

Approaches for optimizing energy consumption in fuel cell electric vehicles are com-
monly classified into three primary approaches: rule-based control, which relies on pre-
defined logic and conditions; optimization-based control, which aims to maximize perfor-
mance through mathematical modeling and solution techniques; and machine learning-
based control, which adapts and improves based on data-driven insights and real-time
vehicle performance (Figure 4).

In practical applications, there are also hybrid control strategies that combine multiple
control methods [41–57]. Among these, rule-based control is straightforward and simple
to execute, but it lacks the ability to achieve global optimization, limiting its effectiveness
in handling complex and dynamic driving environments; optimization-based control can
improve fuel economy but has high computational demands; machine learning-based
control has adaptive capabilities but is complex to train and difficult to interpret. Different
strategies are suitable for different application scenarios, and the specific choice needs to
comprehensively consider vehicle requirements, computational resources, and operating
environments to optimize the economic efficiency, dynamic performance, and operational
lifespan of the fuel cell or battery within the power system. Therefore, it is essential to

World Electr. Veh. J. 2025, 16, 542

7 of 26

develop advanced control strategies and improve energy management techniques to ensure
optimal performance under varying operational driving environments [58–64].

Figure 4. The classification of energy management strategies.

3.1. The Rule-Based Energy Management Strategy

The rule-based energy management strategy regulates the power allocation between
the fuel cell power system and auxiliary energy storage components—such as the power
battery and supercapacitor—through a predefined set of deterministic control rules, typi-
cally derived from expert knowledge or empirical observations. For example, the classic
rule-based strategy is the Charging Deplete-Charging Sustain (CD-CS) strategy, which
determines whether the powertrain operates in pure fuel cell, pure electric, or hybrid mode
based solely on the battery’s State of Charge (SOC). Another common strategy is the power-
following control strategy, which typically bases its decisions on driving conditions (such
as acceleration, constant speed, braking, etc.) and vehicle load requirements to determine
the output power of each energy source [65–69].

For instance, a power-following control strategy proposed by Zhang et al. [70], il-
lustrated in the flowchart in Figure 5, employs fixed upper and lower thresholds for the
power battery (set at 30% and 70%, respectively). When the SOC drops below the limit,
the fuel cell operates at its maximum power output; conversely, when it exceeds the upper
limit, the fuel cell reduces its output or ceases operation. While strategies such as the
Charge Depleting–Charge Sustaining (CD-CS) approach, thermostat control, and finite
state machine control offer simplicity and ease of implementation, their reliance on fixed
rules may limit adaptability under varying driving conditions. Consequently, although
these methods contribute to improved system efficiency and operational stability, their
effectiveness may be constrained in complex or highly dynamic scenarios.

Although the aforementioned methods are simple to implement and have relatively
low computational burden, they suffer from poor adaptability and flexibility, making
them unsuitable for complex driving environments and dynamic operating conditions.
To address these limitations, fuzzy logic control strategies based on non-deterministic
rules have been further developed. These strategies use fuzzy inference systems to handle
complex, nonlinear energy management issues.

In this approach, system input variables (such as accelerator pedal position, vehicle
speed, SOC, etc.) are transformed into fuzzy sets and then processed through a rule base to
derive the appropriate output power (as shown in Figure 6). Fuzzy control methods do not
require precise mathematical models and can address uncertainty and nonlinearity within
the system. As a result, they perform well under conditions of incomplete information
and exhibit good adaptability [71,72]. The main advantages of this method are its strong
flexibility and good real-time performance, making it suitable for driving environments
with high uncertainty.

 World Electr. Veh. J. 2025, 16, 542

8 of 26

Figure 5. The flowchart of the power-following control strategy algorithm.

Figure 6. The fuzzy logic-based control strategy.

3.2. The Optimization-Based Energy Management Strategy

The optimization-based control strategy uses mathematical optimization algorithms
to determine the energy allocation scheme, typically aiming to minimize fuel consump-
tion, improve dynamic response, or extend system lifespan. It is generally classified into
two main categories: global optimization methods, which aim to determine the optimal
control strategy over a complete driving cycle with prior knowledge of driving condi-

   World Electr. Veh. J. 2025, 16, 542

9 of 26

tions, and real-time optimization methods, which seek to make near-optimal decisions
dynamically based on current and predicted vehicle states.

3.2.1. The Global Optimization Control Strategy

The global optimization control strategy generally seeks to minimize energy consump-
tion, assuming that the global driving cycle are known and that the powertrain’s operating
range serves as the boundary conditions. The objective is to optimize the distribution of
multiple energy sources using various optimization algorithms. Global optimization meth-
ods commonly employed in energy management systems include: Dynamic Programming
(DP), which exhaustively evaluates all possible state-action combinations to identify the
globally optimal control strategy over a predefined driving cycle, is widely used for its accu-
racy in finding optimal solutions; Pontryagin’s Maximum Principle (PMP), considering the
alternative, converts the optimization problem into a boundary-value problem by applying
necessary optimality conditions, ensuring an efficient determination of the optimal solution;
Genetic Algorithms (GA) mimic evolutionary processes, utilizing selection, crossover, and
mutation to explore complex and nonlinear solution spaces, providing robust performance
in uncertain environments; Simulated Annealing (SA) adopts a probabilistic approach to
accept suboptimal solutions, enabling the algorithm to escape local optima and converge
toward a global solution; Particle Swarm Optimization (PSO) simulates social behavior
among particles, iteratively refining candidate solutions based on both individual and
collective experiences; with convex objective functions and constraints, the Convex Opti-
mization (CO) offers a robust mathematical framework for solving optimization problems,
ensuring the problem is tractable and has a unique global solution [73–84].

Among these approaches, dynamic programming is frequently regarded as the most
classical method. It is grounded in Bellman’s Principle of Optimality, which involves
dividing the overall problem into smaller subproblems, solving each optimally, and then
using these solutions to construct the global optimum. Therefore, DP can find the global
optimum and is less likely to become stuck in local optima. However, its state space
size grows exponentially with increasing dimensions, leading to a dramatic increase in
computational complexity, making it difficult to apply online. It is typically used for offline
optimization to generate reference trajectories or theoretical benchmarks.

Approximate Dynamic Programming (ADP) addresses the “curse of dimensionality”
by introducing function approximation (e.g., value function fitting or neural networks). This
significantly reduces computational requirements, enabling online or real-time applications,
while still achieving near-optimal results in many practical use cases.

In contrast, Stochastic Dynamic Programming (SDP) incorporates randomness into
state transitions or control effects, making it suitable for systems operating under uncer-
tainty, such as real-world traffic and variable driver behavior. By computing the expected
value of the cost function, SDP achieves optimality in probabilistic terms but often requires
longer convergence time due to the complexity of sampling-based evaluation.

A detailed comparison is provided in Table 2, which includes both algorithmic features
and practical performance metrics based on reported values from literature and typical
experimental setups.

As shown in Table 2, dynamic programming offers the highest theoretical performance
but suffers from an extremely high computational burden, which makes it impractical for
real-time vehicle control. ADP, by simplifying the value function and policy representation,
reduces runtime by an order of magnitude while maintaining over 90% of the fuel-saving
benefit compared to DP. SDP is effective in uncertain or stochastic environments but
requires more iterations and careful design of probability models. From an engineering

World Electr. Veh. J. 2025, 16, 542

10 of 26

standpoint, ADP is currently the most promising trade-off method, balancing optimization
quality, real-time feasibility, and deployment complexity.

Table 2. Comparative analysis of DP, ADP, and SDP in energy management applications.

Feature/Metric

DP (Dynamic
Programming)

ADP (Approximate DP)

SDP (Stochastic DP)

Applicable Problem

Deterministic Optimization

State Transition

Objective Function

xk+1 = f (xk, uk)

min ∑ gk(xk, uk)

Optimality

Global Optimum

Deterministic with
Complexity
xk+1 ≈ fapprox(xk, uk)

Optimization under
Uncertainty
xk+1 = f (xk, uk, wk)

Jpolicy = E

(cid:21)

γk gk(xk, uk)

(cid:20) T
∑
k=0

Jpolicy = E

(cid:21)

γk gk(xk, uk)

(cid:20) T
∑
k=0

Near-Optimal
(Approximate)

Expected Value Optimum

Computational Complexity

Very High (offline only)

Medium (online feasible)

High (longer convergence)

Typical Runtime [85,86]

>1000 s (UDDS, MATLAB
R2021b, I7-10750H)

10–100 s (WLTC, MATLAB
R2021b, I7-10750H)

60–300 s (UDDS, MATLAB
R2021b, I7-10750H)

Fuel Economy Improvement
(vs. Rule) [87]

About 18–20% UDDS, WLTC
(SOC∈(30, 70))

About 12–15% WLTC
(SOC∈(30, 70))

About 10–13% UDDS
(SOC∈(30, 70))

Real-Time Applicability

No

Yes

Representative Use Case

Offline benchmark
generation

Embedded control in
EV/FCV

Partial (depends
on modeling)

Adaptive strategies
under traffic

3.2.2. The Real-Time Optimization Control Strategy

Recent studies on real-time optimization control strategies for energy management
predominantly explore two major methods: the Equivalent Consumption Minimization
Strategy (ECMS), which aims to reduce fuel consumption by efficiently distributing energy
between various power sources, and Model Predictive Control (MPC), which utilizes
system models to predict future behaviors and optimize control actions over a defined time
window, both being widely adopted approaches in energy management systems.

The ECMS is derived from the optimal fuel consumption control strategy originally
developed for Hybrid Electric Vehicles (HEVs), but has since been adapted and enhanced
for use in fuel cell vehicle power systems. The core of this strategy lies in establishing
an equivalent relationship between the fuel cell output power and the battery power
draw. This relationship converts the battery’s energy usage into an equivalent amount of
hydrogen consumption, which allows for the optimization of energy balancing between
the fuel cell power system and the power battery to ensure efficient energy consumption.
One of the key benefits of ECMS is its strong real-time performance, allowing for quick
adjustments to energy distribution, while also maintaining low computational complexity,
making it an attractive choice for real-time applications.

Despite these advantages, ECMS does have its limitations. One significant drawback
is its reliance on a single equivalent factor, which may not be sufficient to adapt to varying
and complex driving conditions, such as steep slopes or high-speed driving. Under these
circumstances, a fixed equivalent factor might lead to suboptimal performance, either
overusing the battery or underutilizing the fuel cell. To overcome this limitation, numerous
researchers have proposed the Adaptive ECMS (A-ECMS), an advanced version of the
traditional ECMS that dynamically adjusts the equivalent factor in response to real-time
driving cycle and system performance. This adjustment allows for more precise control
over energy distribution, ensuring that power is managed efficiently under varying driving
scenarios. As a result, A-ECMS offers a more adaptable and optimized energy manage-

World Electr. Veh. J. 2025, 16, 542

11 of 26

ment solution, improving the overall performance, fuel efficiency, and lifespan of fuel cell
electric vehicles, particularly in environments with fluctuating demands. For example,
Gao et al. [88] introduced an innovative approach by proposing a variable equivalent factor
that adapts according to the battery’s SOC. This dynamic adjustment mechanism enhances
the control strategy, enabling the fuel cell electric vehicle to maintain an optimal SOC while
effectively harnessing the surplus energy of the power battery. The reported simulation
outcomes featuring a transient deviation of no more than 1.2% and a steady-state deviation
of no more than 0.2% demonstrate the method’s high precision and robustness. Com-
pared to conventional ECMS, this strategy significantly improves the adaptability of energy
management across varying driving environments.

Additionally, the MPC operates by formulating a mathematical model of the system to
predict its future behavior over a specified time horizon. At each control cycle, it optimizes
the control inputs to meet predefined objectives, such as reducing hydrogen consumption
or prolonging battery life.

Its core feature is rolling optimization, which involves optimizing the control inputs
for a future period at each sampling moment, but implements only the first control action
of the optimized input sequence at each sampling instant before recalculating the control
sequence in the subsequent control cycle.

As a result, obtaining sufficiently accurate predictions of future driving cycles has
become a key area of research in MPC. The prediction methods employed include various
techniques such as the Markov Transition Matrix (MTM), the Exponential Forecasting (EF),
the Neural Networks (NN), the Auto-Regressive Integrated Moving Average (ARIMA), the
Support Vector Machine (SVM), the Tensor Padding (tensor padding refers to the process
of adding artificial values to tensors to ensure consistent dimensionality for neural network
operations), and the Deep Q-Network (DQN) algorithms et al. [9,10,89–92].

Among these, the MTM is a probability-based prediction method, which mainly
includes three steps: speed state discretization, Markov transition matrix construction,
and speed prediction [64,93]. Since the vehicle speed transition characteristics vary for
different driving modes (such as urban, highway, and suburban), later studies introduced a
driving mode recognition process after speed state discretization, improving the prediction
accuracy. For example, Lin et al. [94] employed the K-means clustering algorithm to
categorize segments of the driving condition based on their characteristic features and
incorporated a neural network-based driving mode recognition before constructing the
Markov matrix, and by leveraging this clustering technique, the predictive capability for
future vehicle velocity is notably enhanced.

Currently, there is considerable research on short-term vehicle speed prediction based
on neural networks, with common types including the Back Propagation Neural Networks
(BPNN), the Radial Basis Function Neural Networks (RBFNN), the Convolutional Neu-
ral Networks (CNN), and the Long Short-Term Memory (LSTM) [95,96]. For instance,
Lin et al. [97] adopted a thoughtful data preparation strategy by randomly reordering mul-
tiple typical operating conditions and merging them into a comprehensive training dataset
comprising 7031 samples. This approach enriched the diversity of training scenarios, en-
hancing the robustness of the model. Furthermore, the use of the Levenberg–Marquardt
algorithm for iterative training of the neural network demonstrates a deliberate emphasis
on convergence speed and fitting accuracy. The results showed the best performance within
a 5 s prediction range, improving by 12.5% compared to the Markov method. Li et al. [98]
effectively integrated traffic information into their modeling framework and proposed a
hybrid vehicle speed prediction model combining CNN and bidirectional long short-term
memory (Bi-LSTM) networks. This integrated architecture leverages the strengths of spatial

World Electr. Veh. J. 2025, 16, 542

12 of 26

feature extraction and temporal sequence learning, resulting in a notable improvement in
the accuracy of future speed predictions.

Driven by recent advancements in Vehicle-to-Everything (V2X) communication, the
real-time acquisition of traffic information has become a reality, and many researchers
have integrated traffic information into vehicle speed prediction [99–103]. For example,
Liu et al. [104] utilized real-time location and traffic signal information in a Vehicle-to-
Infrastructure (V2I) scenario to plan vehicle speed and proposed a model predictive control
method with variable weights for vehicle speed control. He et al. [105] introduced an
innovative dynamic driving cycle construction method that incorporates a real-time traffic
information tensor model (Figure 7), utilizing a speed segment database and a traffic tensor
model database. By enabling the real-time generation and dynamic updating of global
driving cycles in response to current traffic conditions, this technique provides a substantial
improvement in the accuracy and responsiveness when constructing global driving cycles.
The method demonstrates strong potential for improving the adaptability of vehicle control
strategies under complex and evolving traffic environments. Guo et al. [106] proposed a
speed planning method tailored to the specific driving characteristics of buses, aiming to
generate appropriate speed reference intervals. By aligning bus operation with traffic signal
timing, this approach effectively reduces idling at intersections and has a considerable
impact on reducing the total energy consumption throughout the journey. The method
demonstrates a practical and targeted strategy for enhancing the energy efficiency of public
transportation systems.

Figure 7. The driving cycle dynamic construction method based on the tensor model.

In addition, the control strategies for fuel cell electric vehicles have developed target
functions that balance dynamic response and service life, based on optimizing overall vehi-
cle energy consumption [107,108]. For example, Lin et al. [109] innovatively incorporated
the open-circuit voltage degradation of the fuel cell into the energy management evaluation
function as an equivalent hydrogen consumption term. This integration enables the energy

World Electr. Veh. J. 2025, 16, 542

13 of 26

management strategy to account for both immediate fuel efficiency and long-term system
durability. In comparison with traditional rule-based strategies, the proposed method
achieved a 2.6% reduction in hydrogen consumption and a 4.1% decrease in open-circuit
voltage degradation, highlighting its effectiveness in balancing energy efficiency with fuel
cell longevity. Wang et al. [110] introduced a new factor, the rate of change in fuel cell
power, into the energy management strategy, with constraints on power rate of change,
start-stop cycles, and maximum power. They analyzed the impact of different weight
coefficients on overall vehicle energy consumption and proposed an adaptive optimization
energy management strategy that considers performance degradation.

3.3. The Machine Learning-Based Energy Management Strategy

With the rapid advancement of computational intelligence technologies, machine
learning based energy management strategies have garnered growing attention in recent
years. These approaches leverage data-driven models to capture complex system dynamics
and user behaviors, offering improved adaptability and optimization capabilities compared
to conventional rule-based or model-based methods. Machine learning methods analyze a
significant volume of historical data (such as driver behavior, road condition information,
traffic patterns, etc.) and use intelligent algorithms for model training. This enables driver
demand recognition, future road condition prediction, and the integration of multi-source
information, such as weather and traffic accidents, with control strategies, enhancing the
overall vehicle intelligence. Currently, machine learning-based energy management strate-
gies can be broadly categorized into four main paradigms: supervised and unsupervised
learning, reinforcement learning, transfer learning, and federated learning [111–118]. Each
of these approaches offers distinct advantages in terms of data utilization, adaptability, and
scalability, enabling more intelligent and context-aware energy management solutions in
complex and dynamic vehicular environments.

3.3.1. Supervised/Unsupervised Learning-Based Energy Management Strategy

Supervised learning is a method of training models based on existing input-output
sample data and is often used in conjunction with optimization-based energy manage-
ment strategies. In supervised learning, labeled data is essential for training, whereas
unsupervised learning is independent of labeled data [119,120].

Supervised learning is typically used in energy management strategies to learn pat-
terns from historical data, thereby predicting future power demands or optimal energy
distribution strategies. For example, Deep Neural Networks (DNN) can be used to pre-
dict power demand under different driving modes by training on historical driving data;
Support Vector Machines (SVM) can be used to identify driving modes and adjust the
energy management strategy accordingly; and decision tree models can be trained using
historical labeled data with Random Forest (RF) algorithms to identify the optimal energy
distribution strategy under different driving conditions [9,93].

Unsupervised learning is used to automatically discover patterns from data. Com-
mon methods include group formation algorithms, including K-Means and density-based
spatial clustering with noise, which are used to identify different driving modes (e.g.,
city driving, highway driving) and driving styles (e.g., aggressive driving, economical
driving, balanced driving), applying different energy management strategies for each
mode. Autoencoders and Principal Component Analysis (PCA) algorithms are commonly
utilized for dimensionality reduction and feature extraction, enabling the identification
of key variables that significantly impact energy management performance [10,94]. By
effectively filtering redundant or less informative data, these techniques enhance model

World Electr. Veh. J. 2025, 16, 542

14 of 26

interpretability and computational efficiency, thereby supporting the development of more
accurate and responsive energy management strategies.

3.3.2. The Reinforcement Learning-Based Energy Management Strategy

As a significant component of machine learning, the Reinforcement Learning (RL)
has experienced rapid development and has been extensively applied to energy manage-
ment in recent years. Its ability to learn optimal control policies through interaction with
dynamic environments makes it particularly well-suited for addressing the complexity
and uncertainty inherent in real-time energy management scenarios. It primarily involves
training an agent within a given environment to optimize cumulative rewards, thereby
deriving an optimal control strategy. The RL-based energy management encompasses
various approaches, including value function-based methods, Deep Deterministic Policy
Gradient (DDPG), Proximal Policy Optimization (PPO), and other advanced reinforcement
learning techniques [121,122]. These methods leverage deep learning architectures to han-
dle high-dimensional state spaces and improve the stability and convergence of policy
learning, leading to improved effectiveness of energy management strategies, particularly
in dynamic and complex driving scenarios.

1. Value Function-based Method

Q-learning operates by learning the optimal action-value function, which predicts the
expected cumulative reward for each state-action pair, thereby guiding the agent toward
optimal decision-making. By quantifying the expected return of an action in a specific
state, the Q-value directs the agent’s policy toward maximizing long-term rewards. As a
model-free approach, Q-learning operates without the need for a predefined model of the
environment, and it is proven to converge to the optimal Q-value within a finite state-action
space, making it highly effective for sequential decision-making problems, such as energy
management. However, it faces challenges when dealing with large state spaces, as it
becomes difficult to store all the Q-values, and it also struggles with continuous action
spaces. Therefore, Q-learning in energy management typically assumes discrete actions
and cannot be directly applied to complex environments [123].

To address the aforementioned issues, the Deep Q-Network (DQN) algorithm has
been gradually developed. It combines Q-learning with deep neural networks to achieve
optimal energy management without relying on historical data (Figure 8). DQN is suit-
able for optimizing problems with nonlinear, high-dimensional state spaces [124,125]. For
example, Zheng et al. [126] employed the Deep Q-Network (DQN) algorithm, optimiz-
ing for both economy and durability, and compared the performance improvements of
various algorithms under an identical driving environment. The equivalent hydrogen
consumption using the DQN algorithm was only 3.09% higher than the globally optimal
DP algorithm. This small deviation illustrates a favorable trade-off between performance
and computational efficiency, highlighting the practical applicability of DQN for real-time
energy management.

2. Deep Deterministic Policy Gradient-based Method

The DDPG is a reinforcement learning algorithm based on Policy Gradient (PG)
methods, designed specifically for continuous action spaces. By leveraging the discrete-
action learning capability of DQN and the continuous-action optimization of DPG, DDPG
provides a robust framework for tackling complex control tasks, such as those encountered
in autonomous systems and robotics. The algorithm directly outputs actions through a
policy network, which enhances decision-making efficiency and facilitates real-time control
in environments with continuous, high-dimensional action spaces [127].

World Electr. Veh. J. 2025, 16, 542

15 of 26

Figure 8. Energy management strategy framework based on DQN.

Twin Delayed Deep Deterministic Policy Gradient (TD3) builds upon the DDPG
algorithm, incorporating additional mechanisms to mitigate issues like overestimation bias
and instability in reinforcement learning. and designed to address some of the challenges
associated with DDPG, such as instability and overestimation of Q-values. It addresses
critical issues such as Q-value estimation bias, unstable policy updates, and inefficient
exploration, which are prevalent in DDPG. These improvements enhance its suitability
for energy management strategies in fuel cell electric vehicles, where the control tasks are
continuous, stochastic, and inherently complex [128].

Ensemble/Enhanced Twin Delayed Deep Deterministic Policy Gradient (E-TD3) is
an advanced reinforcement learning algorithm that builds upon the TD3 optimization
framework. It further improves the stability, robustness, and iterative exploration efficiency
of control strategies. For example, Huang et al. [129] proposed an enhanced version of the
TD3 algorithm, referred to as E-TD3, which incorporates several improvements aimed at
enhancing learning stability and policy performance. The computational framework of the
proposed E-TD3 algorithm is illustrated in Figure 9, detailing the modifications introduced
to the original TD3 architecture.

3.

Proximal Policy Optimization-based Method

Proximal Policy Optimization (PPO) builds upon traditional policy gradient methods
by introducing mechanisms that ensure more stable and efficient policy updates during rein-
forcement learning. By using a surrogate objective function and incorporating a trust region
approach, PPO strikes a balance between exploration and exploitation, making it particu-
larly effective for solving complex control tasks in dynamic environments, specifically de-
signed for continuous control tasks in high-dimensional, complex environments [130,131].

World Electr. Veh. J. 2025, 16, 542

16 of 26

Figure 9. Energy management strategy framework based on E-TD3.

PPO mainly improves upon traditional policy gradient methods, making them more
stable, efficient, and easier to implement. For example, Li et al. [132] proposed an energy
management strategy based on PPO and compared it with DQN and TD3 (Figure 10).
Performance metrics included algorithmic convergence behavior, energy consumption
optimization, and fuel cell lifespan. The results demonstrated that, under both training and
validation conditions, PPO, DQN, and TD3 exhibited varying hydrogen consumption levels,
highlighting their respective efficiencies in energy management, relative to the DP baseline
scheme, which were 3.79%, 8.45%, and 6.86%, respectively. These findings indicate the
relative efficiency of each algorithm in reducing hydrogen consumption, with PPO showing
the closest performance to the globally optimal DP scheme. Additionally, compared to
DQN and TD3, PPO reduced fuel cell degradation by 2.51% and 0.12%, respectively. The
convergence speed of PPO was 93.55% and 97.17% faster than DQN and TD3, respectively,
demonstrating superior learning efficiency and optimization capability.

Figure 10. Energy management strategy framework based on PPO.

 World Electr. Veh. J. 2025, 16, 542

17 of 26

4. Real-Time Deployability and Embedded Inference Analysis of DRL Methods

While Deep Reinforcement Learning (DRL) algorithms such as DQN, DDPG, PPO,
and TD3 have demonstrated notable performance improvements in fuel cell hybrid vehicle
control (e.g., up to 3.09% energy saving compared to DP), their practical deployment
requires careful evaluation of onboard computational constraints. The inference efficiency
comparison of RL algorithms for onboard FCEV applications is shown in Table 3.

Table 3. Inference efficiency comparison of RL algorithms for onboard FCEV applications.

Algorithm

Typical Model Size

DQN [133]

About 0.5–2 M

DDPG [134]

About 1–3 M

PPO [135]

About 1–2 M

TD3/E TD3 [136]

About 2–4 M

Inference Latency (on
Jetson/ARM)

10–30 ms @ Jetson Xavier
NX, FP32, batch = 1

15–40 ms Jetson TX2, FP16,
batch = 1

20–50 ms @ ARM
Cortex-A72, PyTorch 1.8,
FP32

25–60 ms Jetson Xavier,
FP32, batch = 1

Control Frequency

Low (1–10 Hz)

Deployment
Feasibility

Moderate (needs
pruning)

Medium (5–20 Hz)

Feasible

Medium (5–12 Hz)

Computationally
heavier

Medium (5–10 Hz)

Needs optimization

For instance, DQN and TD3 involve fully connected deep Q-networks with thousands
to millions of parameters, depending on input dimensionality and network depth. On
embedded automotive platforms such as NVIDIA Jetson Xavier NX, inference latency typi-
cally ranges between 5 and 30 ms per decision, which is acceptable for low-frequency
control (e.g., 10 Hz), but might be limiting for high-speed dynamics or fine-grained
energy management [137].

Moreover, algorithms like PPO and TD3 require multiple policy rollouts and gradient
updates during training, which can be computationally expensive. While these processes
are often offloaded to cloud or desktop training environments, runtime inference must
be lightweight enough for deployment on automotive-grade ECUs (e.g., ARM Cortex-A
series) [138]. Model quantization and network pruning techniques can help reduce the
model size and inference delay, albeit potentially at the cost of performance degradation.
Therefore, although DRL-based strategies offer promising improvements, their inte-
gration into real-time fuel cell vehicle control systems remains constrained by hardware
resources, memory bandwidth, and latency budgets. Balancing model complexity with
onboard feasibility is crucial for practical implementation.

3.3.3. Transfer Learning-Based Energy Management Strategy

In the development of energy management strategies for vehicles, a key challenge
lies in efficiently adapting pre-trained models to varying driving conditions, vehicle con-
figurations, or geographic environments. Traditional methods typically require extensive
retraining with large-scale new datasets, which is both time-consuming and computation-
ally expensive. To address this issue, Transfer Learning (TRL) has emerged as a promising
paradigm for enhancing the adaptability and generalization of control strategies with
limited data and computational resources. This method is particularly suitable for en-
ergy management applications, where rapid deployment and robustness across diverse
scenarios are essential.

Transfer learning refers to the process of fine-tuning an already trained model for
a new task. The primary goal is to minimize reliance on large-scale training data while
enhancing the generalization capability of energy management strategies. This is especially
beneficial in scenarios where data availability is limited or computational resources are

World Electr. Veh. J. 2025, 16, 542

18 of 26

constrained, enabling effective adaptation of models to new, unseen environments with
minimal additional training.

The underlying principle of transfer learning involves transferring knowledge, includ-
ing models, features, and parameters, learned from one or more source domains to one or
more target domains, thereby improving learning performance. This is particularly advan-
tageous for knowledge transfer between different vehicle models or driving environments,
enhancing the model’s flexibility and robustness.

For example, Huang et al. [129] integrated transfer learning into deep reinforcement
learning algorithms, building upon the E-TD3 framework. They proposed a Deep Transfer
Reinforcement Learning (DTRL) method tailored for hybrid powertrain energy manage-
ment (Figure 11). This approach enables an energy management strategy trained in one city
to be effectively transferred to another, thereby improving model scalability and adaptabil-
ity. Simulation results demonstrated that, under the proposed transfer learning framework,
development time was reduced by 90.38%, and fuel efficiency improved by 6.07% in fuel
cell hybrid vehicles.

Figure 11. Energy management strategy framework based on transfer learning.

Despite its advantages, transfer learning faces several challenges in practical appli-
cations. One issue is the heterogeneity between domains, such as differences in vehicle
configurations, environmental conditions, and sensor modalities, which may lead to do-
main shifts and performance degradation. Additionally, if the knowledge from the source
domain is not sufficiently relevant to the target task, negative transfer may occur, adversely
affecting the model’s performance.

To address these limitations, researchers have explored domain adaptation techniques
such as feature alignment and model fine-tuning. Nevertheless, ensuring robust generaliza-
tion across domains and validating the effectiveness of transfer learning under real-world
conditions remain crucial directions for future research.

 World Electr. Veh. J. 2025, 16, 542

19 of 26

3.3.4. Federated Learning-Based Energy Management Strategy

While transfer learning enables knowledge reuse across domains to accelerate conver-
gence and reduce data dependence, it often relies on access to labeled data from source
and target environments. In contrast, federated learning (FL) complements TL by enabling
collaborative model training across multiple vehicle nodes without requiring centralized
data collection. This decentralized learning paradigm is particularly advantageous for
energy management applications, where data privacy, system scalability, and distributed
computation are critical considerations.

Given the distributed nature of vehicle fleets and the privacy sensitivity of onboard
data, FL offers a promising solution for intelligent energy optimization in connected
transportation systems. By facilitating model updates through encrypted gradient or
weight exchanges instead of raw data transfer, FL ensures privacy preservation while
minimizing communication costs (Figure 12) [139].

Figure 12. Energy management strategy framework based on federated learning.

However, several challenges hinder large-scale deployment. Communication over-
head, caused by frequent parameter synchronization between vehicles and central servers,
demands high-bandwidth, low-latency infrastructure. Techniques such as gradient sparsifi-
cation and asynchronous updates have been proposed to reduce this burden, though often
at the expense of model convergence and stability.

Furthermore, statistical heterogeneity among clients-resulting from varying vehicle
usage patterns, traffic conditions, and environmental contexts-can impair global model
generalization. This non-IID nature of vehicular data has motivated the development of
personalized FL and cluster-wise aggregation approaches.

Robustness is also essential for real-world deployment. Issues such as intermittent
connectivity, client dropout, and heterogeneous computing capabilities pose nontrivial
obstacles. Despite promising results in simulated environments, comprehensive field trials
are needed to validate FL’s performance, reliability, and energy-saving potential under real
driving conditions [140].

World Electr. Veh. J. 2025, 16, 542

20 of 26

4. Conclusions

The energy management strategy for FCEVs is a critical enabling technology to en-
hance system efficiency, extend component lifespan, and optimize overall vehicle per-
formance. With the continuous advancement of power electronics, control theory, and
artificial intelligence, FCEV energy management strategies are gradually evolving from sim-
ple rule-based approaches and global optimization methods toward adaptive optimization,
data-driven control, and intelligent decision-making frameworks.

This review first analyzed the topological structure of FCEV power systems, high-
lighting the advantages and disadvantages of different multi-source architectures. Based
on this, a systematic comparison of energy management strategies was provided, rang-
ing from fuzzy control, optimization-based methods such as DP and MPC, to emerging
AI-driven approaches. While fuzzy logic offers robustness to uncertainty, its optimization
effect is limited. Optimization-based methods can deliver near-optimal energy allocation
through accurate modeling, but suffer from high computational cost. AI-based strategies,
especially reinforcement learning, have shown promise in capturing system nonlinearity
and improving real-time adaptability.

Looking ahead, three development directions can be identified. (1) AI-based energy
management, leveraging machine learning and reinforcement learning to improve real-
time control and adapt to dynamic driving conditions. These methods are particularly
suitable for on-board implementation in the near term.
(2) V2X-enabled cooperative
optimization, which will integrate FCEVs with intelligent transportation infrastructure,
allowing anticipatory scheduling and coordinated energy allocation under external factors
such as traffic flow and road gradient. This represents a medium-term research focus,
dependent on infrastructure maturity. (3) Cloud-based monitoring and fleet management,
where large-scale vehicle-cloud collaboration can enable predictive maintenance, fault
diagnosis, and route-level optimization, especially for buses and logistics fleets. This long-
term approach supports system-level coordination but requires reliable communication
and data security.

In addition to control strategies, it must also be recognized that the deployment of
FCEVs is constrained by the technological bottlenecks of the fuel cell itself, including
durability, cost, and hydrogen storage limitations. More importantly, achieving true zero-
emission requires that hydrogen fuel be produced from renewable or low-carbon sources,
not fossil-based pathways. Although these issues fall beyond the immediate scope of this
review, they will fundamentally determine the sustainability and scalability of future FCEV
energy management solutions.

By prioritizing on-board AI solutions in the short term, while progressively incor-
porating V2X and cloud-based approaches, a scalable, adaptive, and intelligent energy
management ecosystem for FCEVs can be realized, ultimately supporting the transition
toward zero-emission transportation.

Author Contributions: J.G.: conceptualization, methodology, writing—original draft preparation,
funding acquisition. H.H.: methodology, supervision. C.J.: formal analysis, writing—review and edit-
ing. S.G.: methodology. All authors have read and agreed to the published version of the manuscript.

Funding: This project is supported by the Shandong Province Natural Science Foundation (Grant No.
ZR2023QF134). Weifang University Doctoral Research Start-up Fund (2023BS29).

Data Availability Statement: No new data were created or analyzed in this study. Data sharing is
not applicable to this article.

Conflicts of Interest: The authors declare no conflicts of interest.

World Electr. Veh. J. 2025, 16, 542

References

21 of 26

1.

The Right Car, in the Right Place, at the Right Time. January 2022. Available online: https://www.toyota.co.uk/discover-toyota/
sustainability/sustainable-mobility (accessed on 1 January 2022).

2. Nonobe, Y. Development of the fuel cell vehicle mirai. IEEJ Trans. Electr. Electron. Eng. 2017, 12, 5–9. [CrossRef]
3.

Kojima, K.; Fukazawa, K. Current status and future outlook of fuel cell vehicle development in Toyota. ECS Trans. 2015, 69, 213.
[CrossRef]

4. Manoharan, Y.; Hosseini, S.E.; Butler, B.; Alzhahrani, H.; Senior, B.T.F.; Ashuri, T.; Krohn, J. Hydrogen fuel cell vehicles; current

5.

6.

status and future prospect. Appl. Sci. 2019, 9, 2296. [CrossRef]
Shao, Z.; Yi, B. Developing trend and present status of hydrogen energy and fuel cell development. Bull. Chin. Acad. Sci. 2019, 34,
469–477.
Xiong, S.; Song, Q.; Guo, B.; Zhao, E.; Wu, Z. Research and development of on-board hydrogen-producing fuel cell vehicles. Int. J.
Hydrogen Energy 2020, 45, 17844–17857.

7. Muthukumar, M.; Rengarajan, N.; Velliyangiri, B.; Omprakas, M.A.; Rohit, C.B.; Raja, U.K. The development of fuel cell electric

8.

vehicles—A review. Mater. Today Proc. 2021, 45, 1181–1187. [CrossRef]
Pramuanjaroenkij, A.; Kakaç, S. The fuel cell electric vehicles: The highlight review. Int. J. Hydrogen Energy 2023, 48, 9401–9425.
[CrossRef]

9. He, H.; Meng, X. A Review on Energy Management Technology of Hybrid Electric Vehicles. Trans. Beijing Inst. Technol. 2022, 42,

773–783.

10. Wang, Y.; Fan, Y.; Ou, K.; Wei, Z.; Zhang, J. Research Progress on Traffic Information-Integrated Energy Management for Fuel Cell

Vehicles. Automot. Eng. 2024, 46, 2314–2328.

11. Trencher, G.; Taeihagh, A.; Yarime, M. Overcoming barriers to developing and diffusing fuel-cell vehicles: Governance strategies

and experiences in Japan. Energy Policy 2020, 142, 111533. [CrossRef]

12. Ehsani, M.; Gao, Y.; Longo, S.; Ebrahimi, K. Modern Electric, Hybrid Electric, and Fuel Cell Vehicles; CRC Press: Boca Raton, FL,

USA, 2018.

13. Ahmadi, S.; Bathaee, S.M.T.; Hosseinpour, A.H. Improving fuel economy and performance of a fuel-cell hybrid electric vehicle
(fuel-cell, battery, and ultra-capacitor) using optimized energy management strategy. Energy Convers. Manag. 2018, 160, 74–84.
[CrossRef]

14. Caux, S.; Gaoua, Y.; Lopez, P. A combinatorial optimisation approach to energy management strategy for a hybrid fuel cell vehicle.

Energy 2017, 133, 219–230. [CrossRef]

15. Lü, X.; Wu, Y.; Lian, J.; Zhang, Y.; Chen, C.; Wang, P.; Meng, L. Energy management of hybrid electric vehicles: A review of energy
optimization of fuel cell hybrid power system based on genetic algorithm. Energy Convers. Manag. 2020, 205, 112474. [CrossRef]
16. Zhao, X.; Wang, L.; Zhou, Y.; Pan, B.; Wang, R.; Wang, L.; Yan, X. Energy management strategies for fuel cell hybrid electric

vehicles: Classification, comparison, and outlook. Energy Convers. Manag. 2022, 270, 116179. [CrossRef]

17. Marzougui, H.; Amari, M.; Kadri, A.; Bacha, F.; Ghouili, J. Energy management of fuel cell/battery/ultracapacitor in electrical

hybrid vehicle. Int. J. Hydrogen Energy 2017, 42, 8857–8869. [CrossRef]

18. Gu, H.; Yin, B.; Yu, Y.; Sun, Y. Energy management strategy considering fuel economy and life of fuel cell for fuel cell electric

vehicles. J. Energy Eng. 2023, 149, 04022054. [CrossRef]

19. Min, D.; Song, Z.; Chen, H.; Zhang, T. Genetic algorithm optimized neural network based fuel cell hybrid electric vehicle energy

20.

management strategy under start-stop condition. Appl. Energy 2022, 306, 118036. [CrossRef]
Showers, S.O.; Raji, A.K. State-of-the-art review of fuel cell hybrid electric vehicle energy management systems. AIMS Energy
2022, 10, 458–485. [CrossRef]

21. Munoz, P.M.; Correa, G.; Gaudiano, M.E.; Fernández, D. Energy management control design for fuel cell hybrid electric vehicles

using neural networks. Int. J. Hydrogen Energy 2017, 42, 28932–28944. [CrossRef]

22. Davis, K.; Hayes, J.G. Fuel cell vehicle energy management strategy based on the cost of ownership. IET Electr. Syst. Transp. 2019,

9, 226–236. [CrossRef]

23. Zhou, D.; Al-Durra, A.; Gao, F.; Ravey, A.; Matraji, I.; Simoes, M.G. Online energy management strategy of fuel cell hybrid electric

vehicles based on data fusion approach. J. Power Sources 2017, 366, 278–291. [CrossRef]

24. Carignano, M.G.; Costa-Castelló, R.; Roda, V.; Nigro, N.M.; Junco, S.; Feroldi, D. Energy management strategy for fuel cell-

supercapacitor hybrid vehicles based on prediction of energy demand. J. Power Sources 2017, 360, 419–433. [CrossRef]

25. Carignano, M.; Roda, V.; Costa-Castelló, R.; Valiño, L.; Lozano, A.; Barreras, F. Assessment of energy management in a fuel

26.

cell/battery hybrid vehicle. IEEE Access 2019, 7, 16110–16122. [CrossRef]
Song, K.; Ding, Y.; Hu, X.; Xu, H.; Wang, Y.; Cao, J. Degradation adaptive energy management strategy using fuel cell state-of-
health for fuel economy improvement of hybrid electric vehicle. Appl. Energy 2021, 285, 116413. [CrossRef]

27. Chen, W.; Wang, Y.; Li, B. Overview on current research status and development trends of hydrogen-powered rail transit. Electr.

Drive Locomot. 2023, 3, 1–11.

World Electr. Veh. J. 2025, 16, 542

22 of 26

28. Teng, T.; Zhang, X.; Dong, H.; Xue, Q. A comprehensive review of energy management optimization strategies for fuel cell

passenger vehicle. Int. J. Hydrogen Energy 2020, 45, 20293–20303. [CrossRef]

29. Aminudin, M.A.; Kamarudin, S.K.; Lim, B.H.; Majilan, E.H.; Masdar, M.S.; Shaari, N. An overview: Current progress on hydrogen

fuel cell vehicles. Int. J. Hydrogen Energy 2023, 48, 4371–4388. [CrossRef]

30. Han, X.; Li, F.; Zhang, T.; Song, K. Economic energy management strategy design and simulation for a dual-stack fuel cell electric

31.

vehicle. Int. J. Hydrogen Energy 2017, 42, 11584–11595. [CrossRef]
Shen, D.; Lim, C.C.; Shi, P. Fuzzy model based control for energy management and optimization in fuel cell vehicles. IEEE Trans.
Veh. Technol. 2020, 69, 14674–14688. [CrossRef]

32. Wu, J.; Peng, J.; Li, M.; Wu, Y. Enhancing fuel cell electric vehicle efficiency with TIP-EMS: A trainable integrated predictive

energy management approach. Energy Convers. Manag. 2024, 310, 118499. [CrossRef]

33. Kandidayeni, M.; Trovão, J.P.; Soleymani, M.; Boulon, L. Towards health-aware energy management strategies in fuel cell hybrid

34.

electric vehicles: A review. Int. J. Hydrogen Energy 2022, 47, 10021–10043. [CrossRef]
Fu, Z.; Li, Z.; Si, P.; Tao, F. A hierarchical energy management strategy for fuel cell/battery/supercapacitor hybrid electric vehicles.
Int. J. Hydrogen Energy 2019, 44, 22146–22159. [CrossRef]

35. Li, X.; Wang, Y.; Yang, D.; Chen, Z. Adaptive energy management strategy for fuel cell/battery hybrid vehicles using Pontryagin’s

Minimal Principle. J. Power Sources 2019, 440, 227105. [CrossRef]

36. Wang, Z.; Xie, Y.; Sun, W.; Zang, P. Modeling and Energy Management Strategy Research of Fuel Cell Bus. J. Tongji Univ. (Nat. Sci.

37.

Ed.) 2019, 47, 97–103.
Serpi, A.; Porru, M. Modelling and design of real-time energy management systems for fuel cell/battery electric vehicles. Energies
2019, 12, 4260. [CrossRef]

38. Abdeldjalil, D.; Negrou, B.; Youssef, T.; Samy, M.M. Incorporating the best sizing and a new energy management approach into

the fuel cell hybrid electric vehicle design. Energy Environ. 2025, 36, 616–637. [CrossRef]

39. Ahluwalia, R.K.; Wang, X.; Star, A.G.; Papadias, D.D. Performance and cost of fuel cells for off-road heavy-duty vehicles. Int. J.

40.

Hydrogen Energy 2022, 47, 10990–11006. [CrossRef]
Sorlei, I.S.; Bizon, N.; Thounthong, P.; Varlam, M.; Carcadea, E.; Culcer, M.; Raceanu, M. Fuel cell electric vehicles—A brief review
of current topologies and energy management strategies. Energies 2021, 14, 252. [CrossRef]

41. Rezk, H.; Nassef, A.M.; Abdelkareem, M.A.; Alami, A.H.; Fathy, A. Comparison among various energy management strategies for
reducing hydrogen consumption in a hybrid fuel cell/supercapacitor/battery system. Int. J. Hydrogen Energy 2021, 46, 6110–6126.
[CrossRef]

42. Zhang, Y.; Zhang, C.; Fan, R.; Deng, C.; Wan, S.; Chaoui, H. Energy management strategy for fuel cell vehicles via soft actor-critic-
based deep reinforcement learning considering powertrain thermal and durability characteristics. Energy Convers. Manag. 2023,
283, 116921. [CrossRef]

43. Liu, Y.; Liu, J.; Qin, D.; Li, G.; Chen, Z.; Zhang, Y. Online energy management strategy of fuel cell hybrid electric vehicles based

on rule learning. J. Clean. Prod. 2020, 260, 121017. [CrossRef]

44. Liu, J.; Ren, F.; Yan, F.; Wu, Y.; Sun, Y.; Hu, D.; Chen, N. Energy Management Strategy for Hydrogen Fuel Cell Vehicle Considering

45.
46.

Fuel Cell Stack Lifespan. Chin. J. Automot. Eng. 2023, 13, 517–527.
Shi, J.; Xie, J.; Zhao, Y. Research on durability control strategy of vehicle fuel cell. Mod. Manuf. Eng. 2021, 8, 56–63.
Jia, C.; Zhou, J.; He, H.; Li, J.; Wei, Z.; Li, K.; Shi, M. A novel energy management strategy for hybrid electric bus with fuel cell
health and battery thermal-and health-constrained awareness. Energy 2023, 271, 127105. [CrossRef]

47. Yan, M.; Xu, H.; Jin, L.; He, H.; Li, M.; Liu, H. Co-optimization for fuel cell buses integrated with power system and air
conditioning via multi-dimensional prediction of driving conditions. Energy Convers. Manag. 2022, 271, 116339. [CrossRef]
48. Wu, J.; Zhang, Y.; Ruan, J.; Liang, Z.; Liu, K. Rule and optimization combined real-time energy management strategy for

minimizing cost of fuel cell hybrid electric vehicles. Energy 2023, 285, 129442. [CrossRef]

49. Zhou, D.; Ravey, A.; Al-Durra, A.; Gao, F. A comparative study of extremum seeking methods applied to online energy

management strategy of fuel cell hybrid electric vehicles. Energy Convers. Manag. 2017, 151, 778–790. [CrossRef]

50. Chen, B.; Ma, R.; Zhou, Y.; Ma, R.; Jiang, W.; Yang, F. Co-optimization of speed planning and cost-optimal energy management

51.

for fuel cell trucks under vehicle-following scenarios. Energy Convers. Manag. 2024, 300, 117914. [CrossRef]
˙Inci, M.; Büyük, M.; Demir, M.H.; ˙Ilbey, G. A review and research on fuel cell electric vehicles: Topologies, power electronic
converters, energy management methods, technical challenges, marketing and future aspects. Renew. Sustain. Energy Rev. 2021,
137, 110648. [CrossRef]

52. Lee, H.; Cha, S.W. Energy management strategy of fuel cell electric vehicles using model-based reinforcement learning with

data-driven model update. IEEE Access 2021, 9, 59244–59254. [CrossRef]

53. Zhou, D.; Al-Durra, A.; Matraji, I.; Ravey, A.; Gao, F. Online energy management strategy of fuel cell hybrid electric vehicles:

A fractional-order extremum seeking method. IEEE Trans. Ind. Electron. 2018, 65, 6787–6799. [CrossRef]

World Electr. Veh. J. 2025, 16, 542

23 of 26

54.

Song, K.; Wang, X.; Li, F.; Sorrentino, M.; Zheng, B. Pontryagin’s minimum principle-based real-time energy management
strategy for fuel cell hybrid electric vehicle considering both fuel economy and power source durability. Energy 2020, 205, 118064.
[CrossRef]

55. Yuan, J.; Yang, L.; Chen, Q. Intelligent energy management strategy based on hierarchical approximate global optimization for

plug-in fuel cell hybrid electric vehicles. Int. J. Hydrogen Energy 2018, 43, 8063–8078. [CrossRef]

56. Zhao, Z.; Wang, T.; Li, M.; Wang, H.; Wang, Y. Optimization of fuzzy control energy management strategy for fuel cell vehicle

power system using a multi-island genetic algorithm. Energy Sci. Eng. 2021, 9, 548–564. [CrossRef]

57. Vimalraj, C.; Sivaraju, S.S.; Ranganayaki, V.; Elanthirayan, R. Economic analysis and effective energy management of fuel cell and

battery integrated electric vehicle. J. Energy Storage 2024, 101, 113719. [CrossRef]

58. Liu, T.; Huo, W.; Lu, B. Time-convolution based energy management strategy for fuel cell vehicles. J. Chongqing Univ. Technol.

(Nat. Sci.) 2024, 38, 93–101.

59. Gao, F.; Gao, X.; Zhang, H.; Yang, K.; Song, Z. Management Strategy for Fuel Cell Trams with Both Global and Transient

Characteristics. Trans. China Electrotech. Soc. 2023, 38, 5923–5938.

60. Togun, H.; Aljibori, H.S.S.; Abed, A.M.; Biswas, N.; Alshamkhani, M.T.; Niyas, H.; Paul, D. A review on recent advances on
improving fuel economy and performance of a fuel cell hybrid electric vehicle. Int. J. Hydrogen Energy 2024, 89, 22–47. [CrossRef]
61. Zhang, H.; Yang, J.; Zhang, J.; Xu, X. Multiple-population Firefly Algorithm-based Energy Management Strategy for Vehicle-

mounted Fuel Cell DC Microgrid. Proc. CSEE 2021, 41, 833–846.

62. Zhang, R.; Chen, Z.; Liu, S. Adaptive Energy Management Strategy for High Power Hydrogen Fuel Cell Heavy-Duty Truck Based

on Low Pass Filter. Automot. Eng. 2021, 43, 1693–1701.

63. Li, Q.; Wang, X.; Meng, X.; Zhang, G.; Chen, W. Comprehensive Energy Management Method of PEMFC Hybrid Power System

64.

Based on Online Identification and Minimal Principle. Proc. CSEE 2020, 40, 6991–7002.
Fu, J.; Fu, Z.; Song, S. Best equivalent hydrogen consumption control for fuel cell vehicle based on Markov decision process-based.
Control Theory Appl. 2021, 38, 1219–1228.

65. Liu, N.; Yu, B.; Guo, A. Analysis of Power Tracking Management Strategy for Fuel Cell Hybrid System. J. Southwest Jiaotong Univ.

66.

2020, 55, 1147–1154.
Ji, C.; Li, X.; Liang, C. Simulation of Energy Management for Hybrid Power System of Vehicle Fuel Cell Lithium Ion Power
Battery Based on LMSAMESim. J. Beijing Univ. Technol. 2020, 46, 58–67.

67. Wang, Y.; Sun, B.; Li, W. Energy Management Strategy of Fuel Cell Electric Vehicles Based on Wavelet Rules. J. Univ. Jinan (Sci.

Technol.) 2021, 35, 322–328.

68. Lu, D.; Bao, Y. Control Parameter Optimization of Thermostatically Controlled Loads Based on a Genetic Algorithm. J. Electr.

Power 2021, 36, 355–362.

69. Zeng, F.; Yu, Y.; Bu, J. Research on energy management strategy for military intergrated starter generator hybrid vehicle based on

finite state machine. Sci. Technol. Eng. 2020, 20, 7472–7483.

70. Zhang, F.; Hu, B.; Zhang, H. An Energy Management Strategy for Fuel Cell Incremental Power System. Trans. Beijing Inst. Technol.

2024, 44, 51–59.

71. Li, J.; Zhu, Y.; Xu, Y. Research on Control Strategy Optimization in Power Transmission System of Hybrid Electric Vehicle.

Automot. Eng. 2016, 38, 10–14.

72. Liu, J.; Xiao, P.; Fu, B.; Wang, J.; Zhao, Y.; He, L.; Chen, J. Research on Mode Switching Control Strategy of Parallel Hybrid Electric

Vehicle. China J. Highw. Transp. 2020, 33, 42–50.

73. Wang, Z.; Xie, Y.; Zang, P. Energy management strategy of fuel cell bus based on Pontryagin’s minimum principle. J. Jilin Univ.

(Eng. Technol. Ed.) 2020, 50, 36–43.

74. Hong, Z.; Li, Q.; Chen, W. An Energy Management Strategy Based on PMP for the Fuel Cell Hybrid System of Locomotive. Proc.

CSEE 2019, 39, 3867–3879.

75. Meng, X.; Li, Q.; Chen, W.; Zhang, G. An Energy Management Method Based on Pontryagin Minimum Principle Satisfactory

Optimization for Fuel Cell Hybrid Systems. Proc. CSEE 2019, 39, 782–792.

76. Zhang, A.; Fang, L.; Hu, H. Energy Management Strategy of Plug-in Fuel Cell Tram Based on Speed Optimization, PSO. Urban

Mass Transit 2022, 25, 249–254.

77. Wei, X.; Liu, B.; Leng, J. Research on Eco-Driving of Fuel Cell Vehicles via Convex Optimization. Automot. Eng. 2022, 44, 851–858.
78. Zhang, Y.; Ma, R.; Zhao, D.; Huangfu, Y.; Liu, W. An online efficiency optimized energy management strategy for fuel cell hybrid

79.

electric vehicles. IEEE Trans. Transp. Electrif. 2022, 9, 3203–3217. [CrossRef]
Shen, D.; Lim, C.C.; Shi, P. Robust fuzzy model predictive control for energy management systems in fuel cell vehicles. Control
Eng. Pract. 2020, 98, 104364. [CrossRef]

80. Chatterjee, D.; Biswas, P.K.; Sain, C.; Roy, A.; Ahmad, F.; Rahul, J. Bi-LSTM predictive control-based efficient energy management

system for a fuel cell hybrid electric vehicle. Sustain. Energy Grids Netw. 2024, 38, 101348. [CrossRef]

World Electr. Veh. J. 2025, 16, 542

24 of 26

81. Wei, X.; Sun, C.; Ren, Q.; Zhou, F.; Huo, W.; Sun, F. Application of alternating direction method of multipliers algorithm in energy

management of fuel cell vehicles. Int. J. Hydrogen Energy 2021, 46, 25620–25633. [CrossRef]

82. Zhou, Y.; Li, H.; Ravey, A.; Péra, M.C. An integrated predictive energy management for light-duty range-extended plug-in fuel

cell electric vehicle. J. Power Sources 2020, 451, 227780. [CrossRef]

83. Mazouzi, A.; Hadroug, N.; Alayed, W.; Iratni, A.; Kouzou, A. Comprehensive optimization of fuzzy logic-based energy
management system for fuel-cell hybrid electric vehicle using genetic algorithm. Int. J. Hydrogen Energy 2024, 81, 889–905.
[CrossRef]

84. Hosseini, S.M.; Kelouwani, S.; Kandidayeni, M.; Amammou, A.; Soleymani, M. Fuel efficiency through co-optimization of speed
planning and energy management in intelligent fuel cell electric vehicles. Int. J. Hydrogen Energy 2025, 126, 9–21. [CrossRef]
85. Xin, W.; Zheng, W.; Qin, J.; Wei, S.; Ji, C. Energy management of fuel cell vehicles based on model prediction control using radial

basis functions. J. Sens. 2021, 2021, 9985063. [CrossRef]

86. Du, C.; Huang, S.; Jiang, Y.; Wu, D.; Li, Y. Optimization of energy management strategy for fuel cell hybrid electric vehicles based

on dynamic programming. Energies 2022, 15, 4325. [CrossRef]

87. Lee, H.; Cha, S.; Kim, H.; Kim, S. Energy Management Strategy of Hybrid Electric Vehicle Using Stochastic Dynamic Programming; SAE

Technical Paper; SAE International: Pennsylvania, PA, USA, 2015.

88. Gao, F.; Zhang, H. Adaptive Instantaneous Equivalent Energy Consumption Optimization of Hydrogen Fuel Cell Hybrid Electric

Tram. J. Mech. Eng. 2023, 59, 226–238.

89. Nagem, N.A.; Ebeed, M.; Alqahtani, D.; Jurado, F.; Khan, N.H.; Hafez, W.A. Optimal design and three-level stochastic energy
management for an interconnected microgrid with hydrogen production and storage for fuel cell electric vehicle refueling stations.
Int. J. Hydrogen Energy 2024, 87, 574–587. [CrossRef]

90. Ghaderi, R.; Kandidayeni, M.; Soleymani, M.; Boulon, L.; Trovão, J.P.F. Online health-conscious energy management strategy for

a hybrid multi-stack fuel cell vehicle based on game theory. IEEE Trans. Veh. Technol. 2022, 71, 5704–5714. [CrossRef]

91. Zhang, Y.; Ma, R.; Zhao, D.; Huangfu, Y.; Liu, W. A novel energy management strategy based on dual reward function Q-learning

for fuel cell hybrid electric vehicle. IEEE Trans. Ind. Electron. 2021, 69, 1537–1547. [CrossRef]

92. Guo, J.; He, H.; Sun, C. ARIMA-based road gradient and vehicle velocity prediction for hybrid electric vehicle energy management.

IEEE Trans. Veh. Technol. 2019, 68, 5309–5320. [CrossRef]

93. Zhou, Y.; Ravey, A.; Péra, M. Multi-mode predictive energy management for fuel cell hybrid electric vehicles using Markov

driving pattern recognizer. Appl. Energy 2020, 258, 114057. [CrossRef]

94. Lin, X.Y.; Zhang, G.J.; Wei, S.S. Velocity prediction using Markov Chain combined with driving pattern recognition and applied

to Dual-Motor Electric Vehicle energy consumption evaluation. Appl. Soft Comput. 2021, 101, 106998. [CrossRef]

95. Zhang, X.; Chen, Z.; Wang, W.; Fang, X. Prediction Method of PHEV Driving Energy Consumption Based on the Optimized CNN

Bi-LSTM Attention Network. Energies 2024, 17, 2959. [CrossRef]

96. Zhang, Z.; Wang, Y.X.; He, H.; Sun, F. A short-and long-term prognostic associating with remaining useful life estimation for

proton exchange membrane fuel cell. Appl. Energy 2021, 304, 117841. [CrossRef]

97. Lin, X.; Ye, J.; Wang, Z. Trip distance adaptive equivalent hydrogen consumption minimization strategy for fuel-cell electric

vehicles integrating driving cycle prediction. Chin. J. Eng. 2024, 46, 376–384.

98. Li, C.; Li, M.; Yu, M.; Wang, Z.; Zhao, X. Research on short-time speed prediction based on WSO-optimized CNN-BiLSTM. J.

Chongqing Univ. Technol. (Nat. Sci.) 2024, 38, 38–47.

99. Yan, M.; Xu, H.; Li, M.; He, H.; Bai, Y. Hierarchical predictive energy management strategy for fuel cell buses entering bus stops

scenario. Green Energy Intell. Transp. 2023, 2, 100095. [CrossRef]

100. Wei, X.; Sun, C.; Liu, B.; Huo, W.; Ren, Q.; Sun, F. Co-Optimization of Vehicle Speed and Energy for Fuel Cell Vehicles. J. Mech.

Eng. 2023, 59, 204–212.

101. Zhang, H.; Yang, J.; Zhang, J.; Song, P.; Xu, X. Pareto-Based Multi-Objective Optimization of Energy Management for Fuel Cell

Tramway. Acta Autom. Sin. 2019, 45, 2378–2392.

102. Yang, J.; Xu, X.; Zhang, J.; Song, P. Multi-objective Optimization of Energy Management Strategy for Fuel Cell Tram. J. Mech. Eng.

2018, 54, 153–159. [CrossRef]

103. Yu, K.; Wang, S.; Yang, D.; Fu, H.; Liao, Y. Real-time Energy Management Strategy of Fuel Cell Vehicles Based on Multi-Objective

Optimization. J. Zhengzhou Univ. (Eng. Sci.) 2024, 45, 80–88.

104. Liu, P.; Li, Z.; Jiang, P.; Shu, H.; Liu, Z. A New Method for Vehicle Speed Planning and Model Prediction Control underV2I. J.

Chongqing Univ. Technol. (Nat. Sci.) 2022, 41, 27–33.

105. He, H.; Guo, J.; Peng, J.; Tan, H.; Chao, S. Real-time Global Driving Cycle Construction Method and the Application in Global

Optimal Energy Management in Plug-in Hybrid Electric Vehicles. Energy 2018, 152, 95–107.

106. Guo, J.; He, H.; Wei, Z.; Li, J. An economic driving energy management strategy for the fuel cell bus. IEEE Trans. Transp. Electrif.

2022, 9, 5074–5084. [CrossRef]

World Electr. Veh. J. 2025, 16, 542

25 of 26

107. Jia, C.; Liu, W.; He, H.; Chau, K.T. Deep reinforcement learning-based energy management strategy for fuel cell buses integrating

future road information and cabin comfort control. Energy Convers. Manag. 2024, 321, 119032. [CrossRef]

108. Guo, J.; He, H.; Li, J.; Liu, Q. Driving information process system-based real-time energy management for the fuel cell bus to

minimize fuel cell engine aging and energy consumption. Energy 2022, 248, 123474.

109. Lin, X.; Li, X.; Lin, H. Optimization Feedback Control Strategy Based ECMS for Plug-in FCHEV Considering Fuel Cell Decay

China. J. Highw. Transp. 2019, 32, 153–161.

110. Wang, Y.; Yu, Q.; Wang, X. Adaptive Optimal Energy Management Strategy of Fuel Cell Vehicle by Considering Fuel Cell

Performance Degradation. J. Traffic Transp. Eng. 2022, 22, 190–204.

111. Lin, X.; Xia, Y.; Wei, S. Energy management control strategy for plug-in fuel cell electric vehicle based on reinforcement learning

algorithm. Chin. J. Eng. 2019, 41, 1332–1341.

112. Li, X.; He, H.; Wu, J. Knowledge-guided deep reinforcement learning for multi-objective energy management of fuel cell electric

vehicles. IEEE Trans. Transp. Electrif. 2024, 11, 2344–2355. [CrossRef]

113. Quan, S.; He, H.; Wei, Z.; Chen, J.; Zhang, Z.; Wang, Y. Customized Energy Management for Fuel Cell Electric Vehicle Based
on Deep Reinforcement Learning-Model Predictive Control Self-Regulation Framework. IEEE Trans. Ind. Inform. 2024, 20,
13776–13785. [CrossRef]

114. Huang, R.; He, H.; Su, Q. An intelligent full-knowledge transferable collaborative eco-driving framework based on improved soft

actor-critic algorithm. Appl. Energy 2024, 375, 124078. [CrossRef]

115. Gao, F.; Zhang, H.; Wang, W.; Li, M.; Gao, X. Energy Saving Operation Optimization of Hybrid Energy Storage System for

Hydrogen Fuel Cell Tram. Trans. China Electrotech. Soc. 2022, 37, 686–696.

116. Liu, P.; Li, Q.; Meng, X.; Luo, S.; Li, L.; Liu, S.; Chen, W. Collaborative Optimization of Hydrogen Fuel Cell Urban Emu Operation

Based on Multi-directional Differential Evolution Algorithm. Proc. CSEE 2024, 44, 1007–1019.

117. Huang, R.; He, H.; Su, Q.; Härtl, M.; Jaensch, M. Type-and task-crossing energy management for fuel cell vehicles with longevity

consideration: A heterogeneous deep transfer reinforcement learning framework. Appl. Energy 2025, 377, 124594. [CrossRef]

118. Li, M.; Liu, H.; Yan, M.; Wu, J.; Jin, L.; He, H. Data-driven bi-level predictive energy management strategy for fuel cell buses with

algorithmics fusion. Energy Convers. Manag. X 2023, 20, 100414. [CrossRef]

119. Jui, J.J.; Ahmad, M.A.; Molla, M.M.I.; Rashid, M.I.M. Optimal energy management strategies for hybrid electric vehicles: A recent

survey of machine learning approaches. J. Eng. Res. 2024, 12, 454–467. [CrossRef]

120. Jouda, B.; Al-Mahasneh, A.J.; Mallouh, M.A. Deep stochastic reinforcement learning-based energy management strategy for fuel

cell hybrid electric vehicles. Energy Convers. Manag. 2024, 301, 117973. [CrossRef]

121. Ghaderi, R.; Kandidayeni, M.; Boulon, L.; Trovao, J.P. Q-learning based energy management strategy for a hybrid multi-stack fuel

cell system considering degradation. Energy Convers. Manag. 2023, 293, 117524. [CrossRef]

122. Wang, D.; Mei, L.; Xiao, F.; Song, C.; Qi, C.; Song, S. Energy management strategy for fuel cell electric vehicles based on scalable

reinforcement learning in novel environment. Int. J. Hydrogen Energy 2024, 59, 668–678. [CrossRef]

123. Deng, P.; Wu, X.; Yang, J.; Yang, G.; Jiang, P.; Yang, J.; Bian, X. Optimal online energy management strategy of a fuel cell hybrid

bus via reinforcement learning. Energy Convers. Manag. 2024, 300, 117921. [CrossRef]

124. Yin, Y.; Zhang, X.; Pan, X. Equivalent factor of energy management strategy for fuel cell hybrid electric vehicles based on

Q-Learning. J. Automot. Saf. Energy 2022, 13, 785–795.

125. Tang, X.; Chen, J.; Liu, T.; Qin, Y.; Cao, D. Distributed deep reinforcement learning-based energy and emission management

strategy for hybrid electric vehicles. IEEE Trans. Veh. Technol. 2021, 70, 9922–9934. [CrossRef]

126. Zheng, C.; Zhang, D.; Xiao, Y.; Li, W. Reinforcement learning-based energy management strategies of fuel cell hybrid vehicles

with multi-objective control. J. Power Sources 2022, 543, 231841. [CrossRef]

127. Chen, W.; Peng, J.; Ren, T.; Zhang, H.; He, H.; Ma, C. Integrated velocity optimization and energy management for FCHEV: An

eco-driving approach based on deep reinforcement learning. Energy Convers. Manag. 2023, 296, 117685. [CrossRef]

128. Jia, C.; He, H.; Zhou, J.; Li, J.; Wei, Z.; Li, K.; Li, M. A novel deep reinforcement learning-based predictive energy management for

fuel cell buses integrating speed and passenger prediction. Int. J. Hydrogen Energy 2025, 100, 456–465. [CrossRef]

129. Huang, R.; He, H.; Su, Q.; Härtl, M.; Jaensch, M. Enabling cross-type full-knowledge transferable energy management for hybrid

electric vehicles via deep transfer reinforcement learning. Energy 2024, 305, 132394. [CrossRef]

130. Peng, J.; Ren, T.; Chen, Z.; Chen, W.; Wu, C.; Ma, C. Efficient training for energy management in fuel cell hybrid electric vehicles:

An imitation learning-embedded deep reinforcement learning framework. J. Clean. Prod. 2024, 447, 141360. [CrossRef]

131. Chen, H.; Guo, G.; Tang, B.; Hu, G.; Tang, X.; Liu, T. Data-driven transferred energy management strategy for hybrid electric

vehicles via deep reinforcement learning. Energy Rep. 2023, 10, 2680–2692. [CrossRef]

132. Li, B.; Cui, Y.; Xiao, Y.; Fu, S.; Choi, J.; Zheng, C. An improved energy management strategy of fuel cell hybrid vehicles based on

proximal policy optimization algorithm. Energy 2025, 317, 134585. [CrossRef]

133. Ajani, T.S.; Imoize, A.L.; Atayero, A.A. An overview of machine learning within embedded and mobile devices–optimizations

and applications. Sensors 2021, 21, 4412. [CrossRef]

World Electr. Veh. J. 2025, 16, 542

26 of 26

134. González, M.L.; Ruiz, J.; Andrés, L.; Lozada, R.; Skibinsky, E.S.; Fernández, J.; García-Vico, Á.M. Deep Learning Inference on Edge:
A Preliminary Device Comparison. In International Conference on Intelligent Data Engineering and Automated Learning; Springer
Nature: Cham, Switzerland, 2024; pp. 265–276.

135. Kumar, R.; Sharma, A. Edge AI: A Review of Machine Learning Models for Resource-Constrained Devices. Artif. Intell. Mach.

Learn. Rev. 2024, 5, 1–11.

136. Chen, B.; Wang, M.; Hu, L.; Zhang, R.; Li, H.; Wen, X.; Gao, K. A hierarchical cooperative eco-driving and energy management
strategy of hybrid electric vehicle based on improved TD3 with multi-experience. Energy Convers. Manag. 2025, 326, 119508.
[CrossRef]

137. Farooq, M.A.; Shariff, W.; Corcoran, P. Evaluation of thermal imaging on embedded GPU platforms for application in vehicular

assistance systems. IEEE Trans. Intell. Veh. 2022, 8, 1130–1144. [CrossRef]

138. Lucan Orăs, an, I.; Seiculescu, C.; Căleanu, C.D. A brief review of deep neural network implementations for ARM cortex-M

processor. Electronics 2022, 11, 2545. [CrossRef]

139. Niu, Z.; He, H. A data-driven solution for intelligent power allocation of connected hybrid electric vehicles inspired by offline

deep reinforcement learning in V2X scenario. Appl. Energy 2024, 372, 123861. [CrossRef]

140. Mesdaghi, A.; Mollajafari, M. Improve performance and energy efficiency of plug-in fuel cell vehicles using connected cars with

V2V communication. Energy Convers. Manag. 2024, 306, 118296. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

