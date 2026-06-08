www.nature.com/scientificreports
OPEN Explainable AI (XAI) for transparent
resource allocation in public safety
communications networks
Mohammed Alammar, Abdulrahman Al Ayidh, Mohamed Abbas & Muneer Parayangat
Public Safety Networks (PSNs) play a crucial role in enabling efficient communication and coordination
among first responders and emergency management agencies during critical situations such as natural
disasters, terrorist attacks, and public health crises. These networks must facilitate timely and reliable
data transmission to ensure informed decision-making in dynamic and high-pressure environments.
However, effective resource allocation within PSNs is a challenging task due to fluctuating demands,
limited bandwidth, and the need for real-time adaptability. Traditional AI-based allocation models,
while capable of optimizing resource distribution, often function as black-box systems, offering little
transparency into the decision-making process. The lack of explainability in these models raises
concerns among stakeholders, as opaque AI-driven decisions may result in inefficiencies, biases, or
unintended disparities in resource allocation. To address these challenges, this study presents an
XAI-driven framework for resource allocation that integrates SHAP (Shapley Additive Explanations)
and LIME (Local Interpretable Model-Agnostic Explanations) to enhance both global and local
interpretability. By leveraging these techniques, the proposed model improves transparency,
ensures fairness, and provides interpretable justifications for allocation decisions. Furthermore,
Bayesian uncertainty modeling is incorporated to enhance decision reliability, particularly in rapidly
evolving emergency scenarios. Experimental evaluations demonstrate that the framework optimizes
resource distribution while maintaining explainability, fostering trust among emergency responders,
policymakers, and stakeholders. By bridging the gap between AI-driven optimization and human
interpretability, this research contributes to the advancement of equitable, accountable, and
transparent decision-making processes in PSNs, ultimately improving emergency response efficiency
and public safety outcomes.
Keywords Public safety networks, Explainable AI, Resource allocation, SHAP, LIME, Fairness in AI,
Bayesian uncertainty
Public Safety Networks (PSNs) play a crucial role in ensuring effective communication during emergencies,
including natural disasters, terrorist attacks, and public health crises. These networks are designed to prioritize
the transmission of critical information to first responders and emergency services, thereby enhancing
situational awareness and response efficiency 1. As the demand for reliable communication continues to grow,
the integration of XAI has become essential in fostering transparency and trust within resource allocation
processes. The application of XAI not only improves the efficiency of PSNs but also ensures that stakeholders
can comprehend and validate the decision-making mechanisms involved 2. Public safety officials can gain deeper
insights into how resources are allocated, enabling more effective and informed emergency responses. Resource
allocation within PSNs presents numerous challenges due to factors such as limited bandwidth, varying user
demands, and the necessity for real-time decision-making. The dynamic and unpredictable nature of emergency
situations requires adaptive algorithms capable of responding to rapidly changing conditions 3. To address
these challenges, machine learning models are increasingly being integrated into resource allocation strategies,
optimizing distribution while ensuring transparency in decision-making.
The incorporation of XAI is particularly critical, as it enhances trust by providing clear explanations for
how resources are allocated 4. This capability is essential in emergency scenarios informed decision-making can
significantly impact the effectiveness of response efforts 5. By employing explainable AI, public safety officials can
better understand the rationale behind resource allocations, ultimately improving the reliability, responsiveness,
and efficiency of PSNs 6. Figure 1 illustrates a hierarchical decision-making and communication framework used
Electrical Engineering Department, College of Engineering, King Khalid University, 61421 Abha, Saudi Arabia.
email: mmalamar@kku.edu.sa
Scientific Reports | (2026) 16:14180 | https://doi.org/10.1038/s41598-026-43440-9 1

www.nature.com/scientificreports/
Fig. 1. Hierarchical decision-making and information flow in emergency management
in emergency management to ensure efficient response coordination. It begins with risk chain results, where
collected data is transmitted through an information chain to different decision-making levels: strategical, tactical,
and operational. The command chain transmission then relays decisions from these levels to ground staff, such
as first responders, ensuring timely execution of emergency actions. Additionally, decision staff monitor and
analyze information, while external sources (Others) contribute to the decision-making process, emphasizing
a structured and efficient emergency response system. Transparency and fairness in decision-making are of
growing importance across various sectors, particularly in public safety communications networks. XAI plays a
crucial role in addressing this need by providing insights into automated decision-making processes that govern
resource allocation 7. By utilizing algorithms that can explain their reasoning, XAI enhances the transparency of
allocation mechanisms, allowing stakeholders to understand how resources are distributed during emergencies.
This understanding is vital for decision-makers, as it enables them to evaluate the effectiveness and fairness of
allocation strategies. Ensuring transparency in these processes fosters public trust and strengthens accountability,
ultimately enhancing the credibility and reliability of emergency response systems 8. By integrating XAI
techniques, organizations can establish decision-making frameworks that are not only data-driven but also
justifiable and equitable 9. XAI plays a fundamental role in addressing the challenges associated with resource
allocation in PSNs by offering clear insights into algorithmic decision-making. This transparency ensures that
resource distribution is both fair and justified, thereby fostering trust among users and operators of public safety
communication networks 10. XAI facilitates better collaboration among emergency responders by enabling
them to understand the rationale behind allocation decisions, which is particularly crucial during crises where
informed and timely decision-making is imperative 11. By providing explanations for resource allocations, XAI
enhances the effectiveness of public safety operations, allowing for improved identification of resource needs
and equitable distribution among first responders 12. The integration of XAI techniques ultimately strengthens
the reliability and accountability of emergency communication networks 13. The research highlights the benefits
of implementing XAI techniques to improve the efficiency and effectiveness of emergency response systems 14.
To ensure interpretability, an XAI method is applied to the model, producing explanations that provide
insights into the reasoning behind predictions 15. Both the predictions and explanations are then delivered to
the user interface, enabling stakeholders to understand, trust, and validate AI-driven decisions for improved
accountability and fairness. XAI enables a clearer understanding of the decision-making processes involved in
resource distribution, fostering stakeholder trust and ensuring that resources are allocated where they are most
needed 16. Transparency in resource allocation is particularly critical in public safety networks, as it facilitates
more informed decision-making and optimizes the use of available bandwidth and resources during emergencies
17
The integration of explainable AI enhances the resilience and responsiveness of PSNs, ultimately contributing
to more efficient emergency management and communication. PSNs serve as critical infrastructures that
enable seamless communication among emergency responders and agencies during crises 18. These networks
facilitate real-time information sharing and coordination, which are essential for efficient disaster response
and management 19. To enhance the effectiveness of PSNs, XAI can be employed to introduce transparency
Scientific Reports | (2026) 16:14180 | https://doi.org/10.1038/s41598-026-43440-9 2

www.nature.com/scientificreports/
in decision-making processes. Understanding how AI-driven resource allocation decisions are made fosters
trust among emergency responders, policymakers, and the broader community. This trust is essential for
facilitating collaboration and ensuring that emergency management strategies are data-driven, effective, and
aligned with public safety priorities 20. Traditional resource allocation methods in PSNs have often relied on
heuristic-based approaches that lack the adaptability required in dynamic environments 21. These methods
typically use fixed parameters and predefined rules that fail to account for real-time fluctuations in demand
and resource availability. As a result, traditional approaches may lead to inefficient resource utilization and
suboptimal communication outcomes during emergencies 22. Such inefficiencies can hinder the ability of first
responders to coordinate effectively and deploy necessary resources in a timely manner. To overcome these
limitations, the integration of XAI is crucial, as it enhances transparency and enables more adaptive, data-driven
decision-making in emergency situations 23. XAI has emerged as a transformative development in artificial
intelligence, particularly in its application to public safety communications networks. Its primary significance
lies in enhancing transparency and trust in AI-driven decision-making, enabling stakeholders to comprehend
the rationale behind resource allocation choices 24. By providing interpretable insights into how AI algorithms
function, XAI facilitates compliance with regulatory standards and strengthens collaboration among emergency
response agencies 25. The ability to understand AI-driven resource allocation decisions is essential for ensuring
accountability and optimizing public safety outcomes 26.
Modern AI-based solutions for resource allocation have been developed to optimize bandwidth usage and
enhance communication efficiency. These systems leverage machine learning algorithms to predict demand
patterns and dynamically allocate resources based on real-time needs 27. These systems also enhance transparency
by providing clear explanations for allocation decisions. This level of interpretability is crucial for ensuring that
resource distribution is fair and equitable, thereby fostering trust among stakeholders and improving overall
emergency response effectiveness 28,29. Recent studies have increasingly emphasized the integration of XAI into
network management systems to enhance transparency and accountability. These advancements aim to refine
decision-making processes, ensuring that resource allocation in public safety communications networks is both
efficient and fair 30. XAI provides stakeholders with insights into the rationale behind allocation decisions,
fostering trust and enabling equitable distribution of resources. This transparency is critical for optimizing
network operations and ensuring that emergency response efforts are both data-driven and justifiable 31. The
main objective of this paper is to explore the integration of XAI in Public Safety Communications PSNs to
enhance transparency and trust in resource allocation. This study aims to provide interpretable insights into AI-
driven decision-making, enabling emergency responders and stakeholders to understand and validate resource
distribution strategies. The paper highlights how XAI can address challenges such as limited bandwidth, real-
time decision-making, and dynamic emergency scenarios by ensuring fairness and accountability in PSNs.
Ultimately, this research emphasizes the role of XAI in optimizing resource allocation, improving situational
awareness, and enhancing the overall effectiveness of emergency response systems. PSN environments
characterized by rapid time-varying demand, evolving priorities, partial observability, and uncertainty. Invoking
solvers at fine time granularity incurs non-negligible latency and requires precise real-time knowledge of system
states, assumptions that are often violated in emergency scenarios. The proposed learning-based approach
enables low-latency inference from high-dimensional and noisy observations, while preserving near-optimal
performance. Importantly, the integration of explainability and uncertainty modeling is motivated by operational
accountability requirements in PSNs, where allocation decisions must be transparent, auditable, and confidence-
aware capabilities that solver-based methods do not natively provide.
Contributions and novelty of SLIRA (SHAP–LIME integrated resource allocation)
This work introduces SLIRA, a novel explainable and uncertainty-aware resource allocation framework for PSNs.
While prior studies have explored solver-based optimization, black-box learning, or post-hoc explainability,
SLIRA departs from these paradigms by embedding explainability directly into the allocation dynamics 32. The
novelty of the proposed approach lies not in the isolated use of existing tools, but in their algorithmic coupling
into a unified, regulation-driven allocation mechanism. The main contributions of this paper are summarized
as follows:
I. Explanation-Regularized Resource Allocation Formulation: A new allocation formulation is introduced
in which explainability is treated as a first-class design objective rather than as a post-hoc diagnostic. Unlike
conventional approaches that optimize utility alone and explain decisions afterward, SLIRA integrates
explanation fidelity directly into the allocation objective and update dynamics. Global SHAP attributes and local
LIME explanations act as regulatory signals that shape how allocations evolve over time. This yields an allocation
mechanism that is explicitly constrained to remain interpretable, auditable, and fair throughout operation.
II. SHAP-Informed LIME Proximity Kernel: A novel modification of the LIME proximity kernel is developed,
in which local perturbation weights are scaled using global SHAP feature importance. This SHAP-informed
kernel ensures that local explanations remain consistent with system-level fairness and importance patterns,
addressing a known limitation of LIME in dynamic and safety–critical environments. To the best of the author’s
knowledge, this is the first approach that algorithmically couples global Shapley values with local surrogate
modeling through kernel design, rather than through heuristic post-processing.
III. Hybrid SHAP–LIME Allocation Update Rule: A new explanation-driven allocation update rule is
formulated, in which resource adjustments are governed by a weighted combination of global (SHAP) and local
(LIME) explanation gradients. A tunable control parameter explicitly balances global fairness enforcement
against local decision fidelity. This hybrid update mechanism is neither a classical optimization solver nor a
black-box learned policy; instead, it constitutes a model-driven, interpretable decision process whose behavior
can be traced to individual features, users, and constraints at every time step.
Scientific Reports | (2026) 16:14180 | https://doi.org/10.1038/s41598-026-43440-9 3

www.nature.com/scientificreports/
IV. Uncertainty-Aware Explainability via Bayesian Inference: SLIRA incorporates Bayesian uncertainty
modeling over both allocation decisions and explanation coefficients. Rather than producing deterministic
allocations and explanations, the framework quantifies confidence levels and variability, enabling risk-aware
decision-making in highly uncertain PSN environments. This dual-layer uncertainty modeling extends beyond
existing XAI approaches, which typically treat explanations as fixed and deterministic outputs.
V. Temporal Consistency and Fairness-Constrained Explainability: Explicit temporal consistency tracking
is implemented to ensure that explanation attributions do not fluctuate erratically over time unless justified by
changes in the network state. In addition, fairness constraints are enforced directly on explanation contributions,
rather than solely on final allocations, enabling proactive bias detection and mitigation. This results in a system
that is not only fair at individual time steps but also stable, interpretable, and accountable throughout extended
operational horizons.
Problem definition
PSNs serve as a critical infrastructure for ensuring effective communication among first responders, emergency
services, and government agencies during crises. These networks must operate efficiently under challenging
conditions, such as natural disasters, terrorist attacks, and large-scale emergencies, where real-time decision-
making is crucial 33. However, resource allocation in PSNs presents several challenges due to limited bandwidth,
dynamic user demands, and the need for prioritization based on urgency and importance. Traditional allocation
methods often rely on static policies that fail to adapt to rapidly changing emergency scenarios, leading to
inefficiencies and potential inequities in resource distribution 34.
To address these limitations, Artificial Intelligence (AI)-driven models have been increasingly integrated
into PSN resource management. While AI enhances decision-making efficiency, it introduces the challenge of
explainability. Most AI-based approaches function as black-box models, making it difficult for stakeholders
to understand, trust, and validate allocation decisions. This lack of transparency can result in distrust among
emergency responders and policymakers, particularly when resource allocation decisions have life-critical
implications. Without clear explanations, it becomes challenging to assess fairness, justify resource distribution,
and ensure accountability in high-stakes environments.
This research focuses on developing an XAI-driven resource allocation framework tailored for PSNs. The
primary goal is to enhance transparency while optimizing efficiency and fairness in allocation decisions. The
proposed approach leverages SHAP and LIME (Local Interpretable Model-Agnostic Explanations) to provide
both global and local interpretability, enabling a more comprehensive understanding of allocation mechanisms.
Additionally, fairness-aware constraints and Bayesian uncertainty modeling are incorporated to improve
decision reliability and mitigate biases in allocation strategies. By addressing these challenges, this study aims
to develop a robust and interpretable AI-based resource allocation model that ensures equitable, efficient, and
transparent decision-making in emergency response scenarios.
Principles of explainable AI (XAI) for transparent and fair decision-making
XAI aims to enhance the interpretability of machine learning models by providing both predictions and
explanations. A model f produces an outcome y along with an explanation E, where E approximates the reasoning
behind the model’s decision using an interpretable surrogate model g. This explanation ensures that the model’s
behavior remains consistent and understandable by closely approximating its reasoning for a given input x. The
importance of each feature in decision-making is quantified, ensuring that changes in model predictions are
attributed to specific input features, thus improving transparency and trust in AI-driven decisions. Define users
U = { u 1 ,u 2 ,...,u n } , resources R= { r 1 ,r 2 ,...,r m } , and allocations A ∈ Rn × m, where A ij represents the
allocation of resource r j to user u i . The goal is to maximize utility while ensuring explanations E:
U
n
max (A) subject to: A ij C j j, and E is explainable (1)
A U ≤ ∀
∑
i=1
A model f produces both a prediction y and an explanation E:
f(x)=(y,E) (2)
where x is the input, y is the prediction, and E is the explanation. The explanation E approximates the model’s
reasoning using an interpretable surrogate model g:
E
≈
g(x), wheregisinterpretable.
The explanation E via (g) closely matches the model’s behavior for a specific input x
|
f(x)
−
g(x)
|
<
∈
(3)
Explanation E quantifies the contribution of each feature x i to the prediction:
n
w i =∆y, wherew i isthe importanceoffeaturex i (4)
∑
i=1
Scientific Reports | (2026) 16:14180 | https://doi.org/10.1038/s41598-026-43440-9 4

www.nature.com/scientificreports/
The model f is composed of interpretable components:
|     |     |     | f(x)=f | 1◦ f 2◦···◦ | f n(x),  |     | (5) |
| --- | --- | --- | ------ | ----------- | -------- | --- | --- |
where each f i is a human-understandable operation. Predictions are independent of protected attributes s:
|     |     |     | P(y              | x,s)=P(y | x)  |       | (6) |
| --- | --- | --- | ---------------- | -------- | --- | ----- | --- |
|     |     |     |                  | |        | |   |       |     |
|     |     |     | P(y=1 s=0)=P(y=1 |          |     | s=1)  | (7) |
|     |     |     | |                |          | |   |       |     |
Explanations reflect causal relationships using structural equations:
|     |     |     | y=β +β | x + | +β x k+ϵ,  |     | (8) |
| --- | --- | --- | ------ | --- | ---------- | --- | --- |
|     |     |     | 0      | 1 1 | k          |     |     |
···
where β
i represents causal effects. The model provides uncertainty estimates for predictions:
|     | y=µ | σ,  | where µis themeanandσthe |     |     | standarddeviation |     |
| --- | --- | --- | ------------------------ | --- | --- | ----------------- | --- |
±
Explanations are concise, limiting the number of features k:
E k
|     |     |     |     | |0  |     |     | (9) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ≤
Generating minimal changes δ to alter the prediction, δsuchthatf(x+δ)=yandδisminimized.
′ | |
This is a comprehensive framework for XAI, ensuring that machine learning models produce both accurate
predictions and interpretable explanations. By approximating model behavior using surrogate interpretable
models, XAI enhances transparency and allows stakeholders to understand the reasoning behind AI-driven
decisions. The framework also ensures that explanations reflect causal relationships, rather than mere correlations,
making AI systems more reliable and trustworthy. Additionally, the principles of fairness and robustness are
embedded in the framework by ensuring that model predictions remain independent of protected attributes,
thus promoting ethical decision-making. Uncertainty estimation further enhances model reliability, allowing
users to gauge prediction confidence. Finally, by enforcing concise and minimal explanations, XAI maintains
interpretability while minimizing unnecessary complexity, making AI systems more transparent, accountable,
and aligned with human decision-making processes. Table 1 consolidates all symbols used throughout the
manuscript along with their definitions.
In public safety contexts, operators must be able to understand and justify why specific users or missions
receive prioritized resources 35. SHAP and LIME are therefore employed not as post-hoc visualization tools,
but as mechanisms to expose and regulate feature contributions that drive allocation behavior. Furthermore,
Bayesian uncertainty modeling is introduced to quantify confidence in both predictions and explanations,
enabling risk-aware decision-making when network conditions are volatile or partially observed capabilities
that are fundamentally absent in deterministic solver outputs.
Network state representation
To remove ambiguity in the problem formulation, we explicitly define the time-varying network state used
throughout the SLIRA pipeline. At each decision epoch t, the state vector x(t) is constructed as
|     |     | x(t)=[d | i(t), p i(t), | c ij(t), ℓ(t), | τ(t), | κ i(t), h i(t)],  | (10) |
| --- | --- | ------- | ------------- | -------------- | ----- | ----------------- | ---- |

where d i(t) denotes the demand of user i, p i(t) is the user’s priority or mission urgency index, c ij(t) represents
the channel quality between user i and resource j, ℓ(t) is the global network load, τ(t) captures temporal
congestion signatures , κ i(t) indicates fairness-group identifiers, and h i(t) encodes historical allocation or
dissatisfaction levels. This explicit definition clarifies the features provided as input to the predictive model and
ensures full reproducibility of the experimental setup. The learning model f θ() does not directly output a final
·
allocation; instead, it predicts a matrix of urgency-weighted allocation scores that quantify the desirability of
assigning resource j to user i under the current state. Formally,
|     |     |     | S(t)=f | θ(x(t))=[s | ij(t)],  |     | (11) |
| --- | --- | --- | ------ | ---------- | -------- | --- | ---- |

| where each score s | ij(t) represents a(cid:31) differentiable approx |     |     |     |     |     |     |
| ------------------ | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
(cid:31) imation of the marginal utility gain achieved by
scheduling resource j for user i. This formulation transforms the learning task into a structured prediction
problem where the model approximates the “allocation preference surface” instead of discrete allocation actions.
| Given the predicted score matrix S(t), SLIRA computes the allocation matrix A(t) using an explanation- | (cid:31) |     |     |     |     |     |     |
| ------------------------------------------------------------------------------------------------------ | -------- | --- | --- | --- | --- | --- | --- |
regulated update mechanism rather than via a direct solver or RL policy. The decision rule is defined in three
| stages: |     |     | (cid:31) |     |     |     |     |
| ------- | --- | --- | -------- | --- | --- | --- | --- |
(I) Explanation Extraction: SHAP and LIME generate global and local attribution vectors for each score
s ij(t).
(II) Attribution Fusion: Explanations are fused into
(cid:31)
|     |     | ΦSLIRA(t)=γΦSHAP |     | (t)+(1 | γ)ΦLIME(t),  |     | (12) |
| --- | --- | ---------------- | --- | ------ | ------------ | --- | ---- |
|     |     |                  |     |        | −            |     |      |
providing a unified measure of feature-driven importance.
5
Scientific Reports |        (2026) 16:14180  | https://doi.org/10.1038/s41598-026-43440-9

www.nature.com/scientificreports/
Symbol Description
Set of users in the Public Safety Network
U
ui -th user (emergency responder or unit)
Set of available communication resources
R
rj j-th resource (bandwidth block / slice)
Aij Allocation of resource rj to user ui
A(t) Allocation matrix at time step t
Cj Capacity of resource rj
di(t) Demand of user ui at time t
pi Priority level of user ui
f() AI-based predictive allocation model
·
g() Interpretable surrogate model
·
(A) Utility function of the allocation
U
ϕS ij HAP SHAP value for user–resource pair (i,j)
ϕL ij IME LIME local feature importance
ϕS ij LIRA Hybrid SHAP–LIME explanation coefficient
λ Trade-off parameter between utility and explainability
γ Weight balancing global (SHAP) and local (LIME) explanations
δ Fairness tolerance threshold
Loss function (utility, fairness, and explanation fidelity)
L
Lfi Fairness-related loss component
θ Model parameters
P() Probability distribution
·
µ,σ Mean and standard deviation (uncertainty estimates)
K Number of SHAP Monte Carlo samples
P Number of LIME perturbations
U Number of users
R Number of resources
T Number of time steps
Table 1. Notation summary
(III) Allocation Update: The allocation is then updated according to
A(t)=A(t
−
1)+αΦSLIRA(t)
−
λ f
∇L
fair(A(t
−
1)), (13)
followed by a projection step that enforces capacity, non-negativity, and fairness constraints. This update rule
clarifies that allocations are produced neither by solving a full optimization problem at each step nor by a policy-
based RL estimator, but by a hybrid mechanism that is explicitly regulated by explainability signals.
System architecture and design of XAI-based resource allocation
A structured XAI-integrated resource allocation framework that balances optimization, fairness, and
interpretability has been presented in this section. The objective function incorporates both prediction accuracy
and explanation fidelity, ensuring that resource distribution is both efficient and transparent. To maintain
interpretability, the allocation function enforces human-understandable constraints, considering user demand,
priority, and resource capacity. Additionally, Shapley values are utilized to quantify the contribution of each user
or resource, allowing for a more equitable and justified distribution strategy. The framework further enhances
adaptability by introducing dynamic resource adjustments, where allocations evolve over time based on both
marginal utility and explanation influence. Fairness is ensured by incorporating demographic parity constraints,
preventing biased distributions across protected groups. The model also supports counterfactual explanations,
which identify minimal allocation changes required to achieve desired outcomes and incorporates Bayesian
inference to quantify uncertainty in allocation decisions. Finally, the system maintains interpretability through
sparsity constraints and monitors performance consistency over time, ensuring that resource allocation remains
stable, transparent, and aligned with explainability objectives. The equations describing the system architecture
and design principles of an XAI-based resource allocation system, focusing on optimization, fairness, and
interpretability: The XAI-Integrated Objective Function could be represented by combining prediction accuracy
and explanation fidelity using a trade-off parameter λ:
Scientific Reports | (2026) 16:14180 | https://doi.org/10.1038/s41598-026-43440-9 6

www.nature.com/scientificreports/
|     |     |      | n                    | m   |      |             |     |     |     |      |
| --- | --- | ---- | -------------------- | --- | ---- | ----------- | --- | --- | --- | ---- |
|     |     | (A)= |                      | w   | A λ  | (f(A),g(A)) |     | ,   |     |      |
|     |     | U    |                      | ij  | ij − | · D         |     |     |     |      |
|     |     |      |                      |     |      |             |     |     |     | (14) |
|     |     |      | (cid:31) i=1(cid:31) | j=1 |      |             |     |     |     |      |
Explanationdivergence
|                                                                |     |     |          | Utility          |          |                       |                  |          |     |     |
| -------------------------------------------------------------- | --- | --- | -------- | ---------------- | -------- | --------------------- | ---------------- | -------- | --- | --- |
|                                                                |     |     |          |                  |          | (cid:30)              | (cid:29)(cid:28) | (cid:27) |     |     |
|                                                                |     |     | (cid:30) | (cid:29)(cid:28) | (cid:27) |                       |                  |          |     |     |
| where f is the AI model, g is an interpretable surrogate, and  |     |     |          |                  |          |  measures divergence. |                  |          |     |     |
D
Ensure allocations A adhere to human-interpretable rules:
|     |     |     |     | d   | p   |     |       |     |     |      |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | ---- |
|     |     |     | A   | = i | · i | C , | i,j,  |     |     |      |
|     |     |     | ij  | n   | d p | · j | ∀     |     |     | (15) |
|     |     |     |     | k=1 | k k |     |       |     |     |      |
·
∑
| where d i is the demand of user u |     |     | i ,p i is thei | r priority, and C |     | j is the capacity of resource r |     |     | j . |     |
| --------------------------------- | --- | --- | -------------- | ----------------- | --- | ------------------------------- | --- | --- | --- | --- |
Quantify the contribution of each user/resource to the overall utility using Shapley values ϕ:
|                                        |     |       |                                        | S !(n | S 1)! |      |      |          |     |      |
| -------------------------------------- | --- | ----- | -------------------------------------- | ----- | ----- | ---- | ---- | -------- | --- | ---- |
|                                        | ϕ   | =     |                                        | | | − | | |−  | [ (S | u )  | (S)],    |     |      |
|                                        | ij  |       |                                        |       |       |      | i    |          |     | (16) |
|                                        |     |       |                                        | n     | !     | U    | ∪{ } | −U       |     |      |
|                                        |     | S ⊆∑U | ui}                                    |       |       |      |      |          |     |      |
|                                        |     |       | \{                                     |       |       |      |      |          |     |      |
| where S is a coalition of users, and ϕ |     |       | ij explains the impact of allocating r |       |       |      |      | j to u . |     |      |
i
Model temporal adjustments using a differential equation with explanation-guided feedback:
|     |     | dA    |     | ∂   |     |     | ∂E  |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | ij =α |    | U   | +β  |     |     | ,  |     |     |
(17)
|     |     | dt  | ·                | ∂A ij                            |     | ·                     | ∂A ij                            |     |     |     |
| --- | --- | --- | ---------------- | -------------------------------- | --- | --------------------- | -------------------------------- | --- | --- | --- |
|     |     |     |                 |                                  |     |                       |                                  |    |     |     |
|     |     |     | Marginalutility |                                  |     | Explanationinfluence |                                  |     |     |     |
|     |     |     |                 |                                  |     |                       |                                  |    |     |     |
|     |     |     |                  | (cid:28)(cid:27)(cid:26)(cid:25) |     |                       | (cid:28)(cid:27)(cid:26)(cid:25) |     |     |     |
where (α,β) control adaptation rates.
Enforce demographic parity or equal opportunity:
|                                                                           |     |          | 1          |     | 1     |            |              |     |     |      |
| ------------------------------------------------------------------------- | --- | -------- | ---------- | --- | ----- | ---------- | ------------ | --- | --- | ---- |
|                                                                           |     |          |            | A   |       | A          | δ            | j,  |     |      |
|                                                                           |     |          |            | ij  |       | ij         |              |     |     | (18) |
|                                                                           |     | (cid:31) | G 1|u      | −   | G 2|u |            | (cid:31) ≤ ∀ |     |     |      |
|                                                                           |     | (cid:31) | |          | G1  | |     | G2         | (cid:31)     |     |     |      |
|                                                                           |     |          | (cid:30)i∈ |     |       | (cid:30)i∈ |              |     |     |      |
|                                                                           |     | (cid:31) |            |     |       |            | (cid:31)     |     |     |      |
|                                                                           |     | (cid:31) |            |     |       |            | (cid:31)     |     |     |      |
| where G ,G 2 are protected gro(cid:31)ups, and δ is a fairness tolerance. |     |          |            |     |       |            | (cid:31)     |     |     |      |
1
| Generate minimal changes ∆A to alter allocations for a user u |     |        |      |         |     |       | i:           |     |     |     |
| ------------------------------------------------------------- | --- | ------ | ---- | ------- | --- | ----- | ------------ | --- | --- | --- |
|                                                               | m   | i n ∆A | s.t. | f(A+∆A) |     | =f(A) | , ∆Aissparse |     |     |     |
|                                                               |     | |2     |      |         | ij  |       | ij           |     |     |     |
|                                                               | ∆   | A |    |      |         |     | ̸     |              |     |     |     |
Model uncertainty using Bayesian inference:
|     |     | P(A | ij|Data)= |     | P(A | θ)P(θ|Data)dθ,  |     |     |     | (19) |
| --- | --- | --- | --------- | --- | --- | --------------- | --- | --- | --- | ---- |
|     |     |     |           | ˆ   |     | ij |            |     |     |     |      |

where θ represents model parameters, and explanations include uncertainty intervals.
Limit active allocations per user for simplicity:
m
|     |     |     |     | I(A | ij >0) | k   | i,  |     |     | (20) |
| --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | ---- |
|     |     |     |     | j=1 |        | ≤   | ∀   |     |     |      |
∑
where I is an indicator function and k is the max resources per user.
Track explanation consistency over time:
T
1
|     |     |     | Consistency=1 |     |     | E   | E     |     |     |      |
| --- | --- | --- | ------------- | --- | --- | --- | ----- | --- | --- | ---- |
|     |     |     |               |     |     | t   | t 1|2 |     |     | (21) |
|     |     |     |               |     | − T | | − | −     |     |     |      |
|     |     |     |               |     |     | t=1 |       |     |     |      |
∑
where E t is the explanation at time t.
The  proposed  equations  define  a  unified  XAI-based  resource  allocation  framework  that  balances
utility maximization with transparency by integrating prediction accuracy, explanation fidelity, Shapley-
based attribution, fairness constraints, and dynamic adaptation to evolving demands. The incorporation of
Bayesian uncertainty modeling, sparsity enforcement, and temporal consistency tracking enhances reliability,
7
Scientific Reports |        (2026) 16:14180  | https://doi.org/10.1038/s41598-026-43440-9

www.nature.com/scientificreports/
Fig. 2. Flowchart of the SLIRA framework
interpretability, and auditability, making the framework well suited for fair and trustworthy decision-making in
safety–critical public safety communication networks.
Figure 2 presents the iterative workflow of the SLIRA framework, which combines AI-based predictive
modeling with global SHAP and local LIME explainability to regulate resource allocation through a hybrid
explanation-driven update mechanism. Fairness and capacity constraints, together with Bayesian uncertainty
modeling, are enforced at each iteration to ensure adaptive, transparent, and confidence-aware resource
allocation in dynamic and safety–critical Public Safety Network environments. The contribution of this work
lies not in solving a complex optimization problem, but in enabling transparent and trustworthy AI-driven
resource allocation suitable for the strict latency and reliability demands of PSNs. SHAP and LIME are employed
as regulatory explainability mechanisms SHAP provides global, additive feature attributions and LIME offers
instance-specific surrogate explanation to ensure that allocation decisions remain interpretable, auditable, and
aligned with operational priorities. In parallel, Bayesian inference models uncertainty in both decisions and
explanations, supplying probabilistic confidence estimates that support risk-aware, safety–critical decision-
making in noisy and rapidly evolving PSN environments. SLIRA is defined as a sequential, explanation-regulated
allocation pipeline composed of four tightly integrated stages: (i) predictive scoring, where the model maps the
current network state x(t) to an urgency-weighted score matrix f θ(x(t)); (ii) global and local explainability
extraction, where SHAP values and SHAP-informed LIME attributions quantify the feature-level drivers of each
predicted score; (iii) fused attribution construction, where global and local explanations are combined into a
unified attribution vector that regulates the allocation dynamics; and (iv) explanation-driven allocation updates,
where the fused attributions, fairness constraints, and Bayesian uncertainty estimates collectively determine the
final resource assignment A(t). This multi-stage structure transforms explainability into an operational control
signal rather than a post-hoc interpretive tool.
Scientific Reports | (2026) 16:14180 | https://doi.org/10.1038/s41598-026-43440-9 8

www.nature.com/scientificreports/
SHAP-based resource allocation for fair and explainable decision-making
The utility function for resource allocation is designed to maximize efficiency while ensuring fairness and
interpretability. It considers the priority of each user-resource pair, where the allocation is constrained by capacity
limits and non-negativity conditions to ensure feasibility. To further enhance transparency, SHAP values are
computed to quantify the impact of each user’s demand and priority on the overall utility. A positive SHAP
value indicates that a user’s presence increases system utility, allowing decision-makers to understand and justify
allocations based on feature importance. To promote fairness in resource distribution, the model enforces SHAP-
based fairness constraints, ensuring that protected groups receive equitable allocations. The system dynamically
updates resource distributions over time using SHAP-guided gradients, adjusting allocations based on utility
changes and fairness constraints. The final allocation for each user is decomposed into user-specific factors
(demand and priority) and system-wide factors (network conditions and congestion) to enhance interpretability.
Furthermore, human validation is incorporated by minimizing explanation divergence, ensuring that AI-
generated allocations align with expert decision-making. Define the utility function for allocating resources to
users:
|     |     |     |     |      | n m |              |     |     |      |
| --- | --- | --- | --- | ---- | --- | ------------ | --- | --- | ---- |
|     |     |     |     | (A)= |     | w ij A ij ,  |     |     | (22) |
U
i=1∑ j=1
|     |     |     |     |     | ∑   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
where: A ij: Resource j allocated to user i, w ij: Weight represents the priority of user i for resource j.  Under
Constraints:
n
|     |     |     | A   | C j (capacity), |     | A   | i,j.  |     |      |
| --- | --- | --- | --- | --------------- | --- | --- | ----- | --- | ---- |
|     |     |     | ij  | j               |     | ij  | 0     |     | (23) |
|     |     |     | ≤   | ∀               |     |     | ≥ ∀   |     |      |
|     |     | i=1 |     |                 |     |     |       |     |      |
∑
For each user-resource pair (i,j), compute the SHAP value ϕ ij to quantify the contribution of user i’s demand
| or priority to the total utility  |     |     | :   |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
U
|     |     |       | S   | !(n S    | 1)! |      |             |     |      |
| --- | --- | ----- | --- | -------- | --- | ---- | ----------- | --- | ---- |
|     | ϕ   | =     | |   | | − | |− | [   | (S i | ,A) (S,A)], |     |      |
|     | ij  |       |     |          |     |      |             |     | (24) |
|     |     |       |     | n !      | U   | ∪{ } | −U          |     |      |
|     |     | S ⊆∑U | i   |          |     |      |             |     |      |
\{ }
where: S: Subset of users excluding i.  (S,A): Utility when only users in S receive resources. Interpretation:
U
ϕ >0 implies user i’s presence increases the system utility for resource j. Ensure allocations align with SHAP-
ij
| based fairness. For protected groups (G |     |     |     | ,G ): |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
1 2
|     |     |     | 1              |           | 1         |            |       |     |      |
| --- | --- | --- | -------------- | --------- | --------- | ---------- | ----- | --- | ---- |
|     |     |     |                | ϕ ij      |           | ϕ ij       | δ j,  |     | (25) |
|     |     |     | (cid:31) G 1|i | −         | G 2|i     | (cid:31) ≤ | ∀     |     |      |
|     |     |     | |              | G1        | | G2      |            |       |     |      |
|     |     |     | (cid:31)       | (cid:30)∈ | (cid:30)∈ | (cid:31)   |       |     |      |
|     |     |     | (cid:31)       |           |           | (cid:31)   |       |     |      |
|     |     |     | (cid:31)       |           |           | (cid:31)   |       |     |      |
where δ is a fairness tolerance(cid:31) threshold. This penalizes biase(cid:31)d allocations toward specific groups. Update
allocations over time t using SHAP-guided gradients:
∂
|     |     | A ij(t+1)=A |     | ij(t)+α | ϕ   | ij(t) β | L ,  |     | (26) |
| --- | --- | ----------- | --- | ------- | --- | ------- | ---- | --- | ---- |
|     |     |             |     |         | ·   | −       | · ∂A |     |      |
|     |     |             |     |         | (   |         | ij ) |     |      |
where:α: Learning rate.  : Loss function penalizing unfairness or capacity violations.  β: Regularization
L
parameter balancing utility and equity. The final allocation for user i is explained as a sum of SHAP contributions:
|     |     | A∗ij | =ϕd                  | emand+ϕp | riority+ | ϕn etwork          | ,   |     |      |
| --- | --- | ---- | -------------------- | -------- | -------- | ------------------ | --- | --- | ---- |
|     |     |      | ij                   | ij       |          | ij                 |     |     |      |
|     |     |      |                      |          |          |                    |     |     | (27) |
|     |     |      | User-specificfactors |          |          | System-widefactors |     |     |      |

|                                  |     |     | (cid:31) | (cid:30) (cid:29) | (cid:28)  | (cid:31) (cid:30)e(cid:29)two(cid:28)rk: Impact of network congestion or  |     |     |     |
| -------------------------------- | --- | --- | -------- | ----------------- | --------- | ------------------------------------------------------------------------- | --- | --- | --- |
| where: ϕd emand: Impact of user  |     |     | i’s dema | n d on all        | ocation.  | ϕn                                                                        |     |     |     |
| ij                               |     |     |          |                   |           | ij                                                                        |     |     |     |
interference. Ensure human operators agree with SHAP explanations by minimizing explanation divergence:
n
1
|     |     |     | =   | Ah  | uman | AS HAP 2 | < ,  |     |      |
| --- | --- | --- | --- | --- | ---- | -------- | ---- | --- | ---- |
|     |     |     |     | ij  |      | ij       |      |     | (28) |
|     |     |     | D   | n | | −    | |        | ∈    |     |      |
|     |     |     |     | i=1 |      |          |      |     |      |
∑
9
Scientific Reports |        (2026) 16:14180  | https://doi.org/10.1038/s41598-026-43440-9

www.nature.com/scientificreports/
where Ah uman is an expert’s allocation and ϵ is an agreement threshold. Model uncertainty in SHAP explanations
ij
using Bayesian inference:
|     | P(ϕ ijData)= |     | P(ϕ | θ)P(θData)dθ,  |     | (29) |
| --- | ------------ | --- | --- | -------------- | --- | ---- |
|     |              |     | ˆ   | ij             |     |      |

where θ represents network parameters. Track stability of explanations over time t:
T
1
|     | Consistency=1 |     |       | ϕ ij(t) ϕ ij(t | 1) |2  | (30) |
| --- | ------------- | --- | ----- | -------------- | ------ | ---- |
|     |               |     | − T   | | −            | −      |      |
|     |               |     | ∑ t=1 |                |        |      |
Low consistency flags unstable or adversarial behavior.
n
|     |     |     | ϕ =∆ | j,  |     |      |
| --- | --- | --- | ---- | --- | --- | ---- |
|     |     |     | ij   | j   |     | (31) |
U ∀
|     |     | i=1 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
∑
|     | where (∆ | j) is | the utility | from resource(j) |     |      |
| --- | -------- | ----- | ----------- | ---------------- | --- | ---- |
|     |          | U     |             |                  |     |      |
|     |          |       | ϕ A∗ij      | i                |     |      |
|     |          |       | ij          |                  |     | (32) |
|     |          |       | ∝           | ∀                |     |      |
It is important to emphasize that the above formulation is used to define the system objective and constraints,
and to construct solver-based baselines for benchmarking purposes. In the proposed framework, however, the
allocation is not obtained by directly solving this optimization problem at each time step. Instead, the formulation
serves as a reference model from which learning targets and evaluation criteria are derived. This design choice
reflects the need for fast, adaptive decision-making in dynamic PSN environments, where repeated exact
optimization may be impractical due to latency constraints and imperfect state information. The integration of
SHAP values in resource allocation not only optimizes efficiency but also enhances fairness and interpretability.
The model quantifies feature contributions, ensures equitable distribution, and dynamically adapts allocations
based on real-time data. Bayesian inference is utilized to model uncertainty, while consistency tracking helps
detect unstable or adversarial behaviors in decision-making. This approach ensures a transparent, justifiable, and
accountable resource allocation system, fostering trust among stakeholders and improving real-world decision-
making.
Enhancing resource allocation transparency with LIME-based explainability
LIME provides a means to approximate black-box resource allocation models with interpretable surrogate
models. By minimizing the loss function between the original model and the interpretable model, LIME ensures
that decision-making remains explainable and aligned with local feature variations. The model employs a
proximity kernel to prioritize perturbations in the local decision space, enhancing its ability to provide granular
insights into resource distribution. Additionally, LIME introduces regularization constraints to maintain
simplicity and prevent overfitting in the interpretable model, ensuring clarity in decision rationale. LIME-
generated feature importance values allow for dynamic updates in resource allocations, enabling models to
adjust based on fairness constraints and loss penalties. Furthermore, Bayesian inference is employed to model
uncertainty, offering stakeholders a clearer understanding of how confident the system is in its decisions. For
specific user-resource instance x i, LIME approximates the black-box model f as resource allocator with an
interpretable model g:
|     | g(x i)=argm |     | in (f,g,π | xi )+Ω(g), |     | (33) |
| --- | ----------- | --- | --------- | ---------- | --- | ---- |
|     |             |     | g L       |            |     |      |
∈G
where:  : Loss function measuring how well g approximates f near x i. π : Proximity kernel weighting
| L                                         |                                                    |     |                                       |        | xi  |      |
| ----------------------------------------- | -------------------------------------------------- | --- | ------------------------------------- | ------ | --- | ---- |
| perturbations around x                    | i. Ω(g): Regularization term enforcing simplicity. |     |                                       |        |     |      |
| LIME generates local feature importance ϕ |                                                    |     | ij for each user-resource pair (i,j): |        |     |      |
|                                           |                                                    | ϕ   | =β                                    | (x µ   |     |      |
|                                           |                                                    | ij  | j                                     | ij j)  |     | (34) |
|                                           |                                                    |     | ·                                     | −      |     |      |
where: β j: Coefficient of feature j in the interpretable model g. x ij: Feature value. µ j: Mean feature value in the
local neighborhood. Update allocations using LIME-derived feature importances:
∂
|     | A ij(t+1)=A | ij(t)+α |     | ϕ ij(t) λ | L ,     | (35) |
| --- | ----------- | ------- | --- | --------- | ------- | ---- |
|     |             |         |     | · −       | · ∂A ij |      |
|     |             |         |     | (         | )       |      |
10
Scientific Reports |        (2026) 16:14180  | https://doi.org/10.1038/s41598-026-43440-9

www.nature.com/scientificreports/
where: α: Learning rate.  : Loss penalizing unfairness or capacity violations. λ: Regularization parameter
L
balancing utility and equity. Enforce group fairness using LIME’s local explanations. For protected groups
(G ,G ):
1 2
|     |     |     | 1          |           | 1         |            |       |      |
| --- | --- | --- | ---------- | --------- | --------- | ---------- | ----- | ---- |
|     |     |     |            | ϕ ij      |           | ϕ ij       | δ j,  | (36) |
|     |     |     | (cid:31) G | −         | G         | (cid:31) ≤ | ∀     |      |
|     |     |     | | 1|i      | G1        | | 2|i G2  |            |       |      |
|     |     |     | (cid:31)   | (cid:30)∈ | (cid:30)∈ | (cid:31)   |       |      |
|     |     |     | (cid:31)   |           |           | (cid:31)   |       |      |
|     |     |     | (cid:31)   |           |           | (cid:31)   |       |      |
where δ is a fairness threshold, g(cid:31)enerate minimal changes ∆x i to(cid:31) alter the allocation for user i:
|     | Find∆x | i s.t.f(x | i+∆x | i) =f(x | i)  | and | ∆x i |1 isminimized. |     |
| --- | ------ | --------- | ---- | ------- | --- | --- | -------------------- | --- |
|     |        |           |      | ̸       |     |     | |                    |     |
This identifies critical features that influence allocations. Model uncertainty using Bayesian LIME:
|     |     |     | P(ϕ ijData)= |     | P(ϕ θ)P(θData)dθ,  |     |     |      |
| --- | --- | --- | ------------ | --- | ------------------ | --- | --- | ---- |
|     |     |     |              | ˆ   | ij                 |     |     | (37) |

where θ represents parameters of the interpretable model g. Limit the number of features in explanations for
simplicity:
|     |     |     |     | ϕ    | k      | i,j  |     | (38) |
| --- | --- | --- | --- | ---- | ------ | ---- | --- | ---- |
|     |     |     |     | | ij | |0 ≤ ∀ |      |     |      |
where k is the maximum non-zero features k=5.Track explanation stability over time t:
T
1
|     |     | Consistency=1 |     |     | ϕ ij(t) |     | ϕ ij(t 1) |2  | (39) |
| --- | --- | ------------- | --- | --- | ------- | --- | ------------- | ---- |
|     |     |               |     | −   | T |     | −   | −             |      |
|     |     |               |     |     | ∑ t=1   |     |               |      |
Low consistency flags unstable allocations or adversarial inputs. Measure agreement between LIME and human
experts:
n
1
|     |     |     | =   | Ah                | uman AL | IME | 2 < ,    |      |
| --- | --- | --- | --- | ----------------- | ------- | --- | -------- | ---- |
|     |     |     |     | ij                |         | ij  |          | (40) |
|     |     |     | D   | n                 | −       |     | ∈        |      |
|     |     |     |     | i=1               |         |     |          |      |
|     |     |     |     | (cid:31) (cid:30) |         |     | (cid:30) |      |
|     |     |     |     | (cid:30)          |         |     | (cid:30) |      |
where ϵ is an acceptance threshold. LIME enhances the interpretability, fairness, and adaptability of resource
allocation models. The integration of feature importance of tracking, fairness constraints, and Bayesian
uncertainty modeling improves decision reliability while fostering stakeholder confidence. Additionally,
consistency tracking helps identify irregularities and adversarial behaviors, reducing the risk of unintended
biases in allocation processes. Ultimately, LIME-driven transparency enables a robust, equitable, and accountable
resource distribution framework, strengthening the trustworthiness of AI-powered public safety networks.
Experimental evaluation
This section presents a comprehensive experimental evaluation of the proposed SLIRA framework in dynamic
PSN environments. The objective of the evaluation is to rigorously assess the effectiveness of SLIRA in achieving
transparent, fair, and efficient resource allocation under realistic operational conditions characterized by time-
varying demand, partial observability, and uncertainty. In contrast to idealized static settings, the experimental
design reflects the practical constraints faced by real-world PSNs, where low-latency decision-making and
accountability are critical.
Experimental scenarios and simulation environment
To ensure statistical credibility, all experiments are repeated over 20 independent simulation runs using different
random seeds. For each metric, we report the mean ± standard deviation and provide 95% confidence intervals
when comparing methods. This variability analysis captures the uncertainty inherent in dynamic and partially
observed network states. The SLIRA framework additionally reports posterior variance from its Bayesian
module, enabling confidence-aware interpretation of decisions. Including statistical variability ensures that
observed gains are consistent and not artifacts of a single simulation trace.
Baseline methods for comparison
Although the considered resource allocation problem admits an optimal solution via classical optimization
solvers under static and fully known conditions, the objective of this work is not to replace such solvers in
11
Scientific Reports |        (2026) 16:14180  | https://doi.org/10.1038/s41598-026-43440-9

www.nature.com/scientificreports/
idealized settings. In contrast to solver-based optimization, which produces allocation values without feature-
level accountability, the proposed framework explicitly incorporates explainability as a functional component
of the decision process.
Comparisons with existing AI-based resource allocation models demonstrate SLIRA’s superior ability to
balance global fairness (SHAP) and local fidelity (LIME) while maintaining high predictive accuracy. The direct
solver-based baseline was implemented using the MOSEK Optimizer (version 10.1), accessed through the Python
3.10 Fusion API. MOSEK employs state-of-the-art interior-point algorithms suitable for large-scale convex
optimization, making it well-suited for solving the constrained utility maximization problem defined in Eqs.
(22 and 23) . The solver computes static optimal allocation under full network observability. For dynamic PSN
experiments, warm-started re-optimization was executed at each time step to reflect repeated decision-making
conditions under evolving network states. Default interior-point optimality tolerances (relative gap ≤ 10⁻⁸) were
used to ensure numerical stability and precision.
Parameter settings and implementation details
This subsection describes the hyperparameter configuration used in the experimental evaluation of the proposed
SLIRA framework, along with the rationale behind their selection. Careful tuning of these parameters is essential
to balance utility maximization, explainability, fairness, and computational efficiency in PSN environments. The
learning rate α controlling the allocation update dynamics was set to α=0.05. This value was selected to ensure
stable convergence without oscillatory behavior in dynamic emergency scenarios. Smaller values led to slow
adaptation, while larger values resulted in unstable allocation updates under bursty traffic conditions. The trade-
off parameter λ, which balances allocation utility and explanation fidelity in the hybrid loss function, was chosen
from the range λ [0.1,1.0]. Empirical tuning showed that λ=0.5 provides an effective compromise between
∈
performance and interpretability, preventing either objective from dominating the optimization process. The
SHAP–LIME fusion weight γ [0,1] controls the relative contribution of global (SHAP) and local (LIME)
∈
explanations. Based on sensitivity analysis, γ =0.6 was selected, favoring global fairness awareness while
retaining sufficient local adaptability for instance-specific allocation decisions.
Fairness enforcement is governed by the tolerance threshold δ, which limits disparities in allocation or
explanation contributions between protected groups. In the experiments, δ=0.05 was used, reflecting a strict
but feasible fairness constraint consistent with public safety equity requirements. For SHAP computation, Monte
Carlo sampling with K =100 coalitions were employed, offering a favorable balance between explanation
accuracy and runtime. LIME explanations were generated using P =500 perturbations per instance, which
provided stable local explanations without excessive computational overhead. Bayesian uncertainty estimation
was implemented using variational inference with a diagonal Gaussian approximation. The optimization was run
for 200 iterations per update cycle, which was sufficient to achieve convergence of posterior mean and variance
estimates across all experiments. All solver-based experiments were conducted on an Intel Core i7 (3.2 GHz)
workstation with 32 GB RAM running Ubuntu 22.04 LTS. The same network state trajectories and random seeds
were used across solver-based and learning-based methods to guarantee controlled benchmarking conditions.
The use of a high-precision convex solver ensures that the reported solver baseline reflects true near-optimal
performance under the defined formulation.
SLIRA: a SHAP-LIME hybrid framework for explainable and fair resource allocation
SLIRA integrates SHAP (global explainability) and LIME (local interpretability) to create a hybrid model
that enhances transparency, fairness, and adaptability in resource allocation. By optimizing both explanation
fidelity and fairness constraints, SLIRA ensures that allocation decisions are justifiable and interpretable across
different stakeholders. The framework refines LIME’s proximity kernel to align perturbations with SHAP’s
global importance, enabling a more accurate assessment of feature contributions. Furthermore, SLIRA updates
allocations using a SHAP-LIME hybrid gradient, balancing global fairness and local fidelity while minimizing
overall loss functions. To maintain fairness and stability, SLIRA enforces demographic parties across protected
groups by integrating SHAP-LIME contributions into allocation rules. The framework also employs Bayesian
inference to quantify uncertainty, ensuring that decision-makers can assess confidence levels in allocation
explanations. Additionally, sparsity constraints are introduced to limit the number of active features, making
explanations more concise and interpretable. By tracking temporal consistency, SLIRA ensures that explanation
quality remains stable over time, detecting and mitigating irregularities or adversarial behavior. SLIRA bridges
the gap between local and global explainability, making it ideal for critical applications like public safety networks
where transparency and adaptability are paramount. SLIRA jointly optimizes global fairness (SHAP) and local
fidelity (LIME) using a hybrid loss function:
g∗(x i)=argm g in L (f,g,π xi )+λ 1 Ω(g) +λ 2 ϕS ij HAP − ϕS ij LIRA 2 ,
∈G j (41)
LIMEloss Sparsity (cid:27)(cid:26) (cid:25)
(cid:31) (cid:30)(cid:29) (cid:28) (cid:31)(cid:30)(cid:29)(cid:28)
SHAPconsistency
where: ϕS ij HAP: SHAP values from cooperative game theory. ϕS ij L(cid:31)IRA: SLIRA (cid:30) ’s (cid:29) explanation (cid:28) coefficients. λ 1 ,λ 2:
Regularization weights balancing sparsity and SHAP alignment.
Scientific Reports | (2026) 16:14180 | https://doi.org/10.1038/s41598-026-43440-9 12

www.nature.com/scientificreports/
Modify LIME’s proximity kernel π xi to prioritize perturbations aligned with SHAP’s global importance:
π xi (z)=exp −
D(x
σ i 2
,z)2
·
m
ϕS j HAP ·| z j − x ij | , (42)
( )
∑
j=1
where D(x i ,z) is the Euclidean distance and ϕS j HAP scales weights by global feature importance. Update
allocations using a SHAP-LIME hybrid gradient:
∂
A ij(t+1)=A ij(t)+α γϕS ij HAP(t)+(1 − γ)ϕS ij LIRA(t) − λ ∂ L A f ij i, (43)
[ ]
where: γ [0,1]: Balances global vs. local explanations. fi: Fairness loss.
∈ L
Enforce fairness across protected groups G 1 ,G 2 using combined SHAP-LIME contributions:
1 1
(cid:31) (cid:31) (cid:31) | G 1|i (cid:30)∈ G1(cid:29) γϕS ij HAP +(1 − γ)ϕS ij LIRA (cid:28) − | G 2|i (cid:30)∈ G2(cid:29) γϕS ij HAP +(1 − γ)ϕS ij LIRA (cid:28) (cid:31) (cid:31) (cid:31) ≤ δ (44)
(cid:31) (cid:31)
Mode(cid:31)l uncertainty via Bayesian fusion of SHAP and LIME: (cid:31)
P ϕS ij LIRA|Data = ˆ γP ϕS ij HAP | θ +(1 − γ)P ϕL ij IME | θ P(θ|Data)dθ (45)
( ) [ ( ) ( )]
Limit active features in explanations using:
m m
Ω(g)=λ 1 ϕS ij LIRA +λ 2 ϕS ij LIRA 2 (46)
(cid:31)
j=1
(cid:30) (cid:30) (cid:31)
j=1
(cid:29) (cid:28)
(cid:30) (cid:30)
Track stability over time t:
T
1
Consistency=1 − T | γϕS ij HAP(t)+(1 − γ)ϕS ij LIRA(t) − ϕS ij LIRA(t − 1) |2 (47)
∑
t=1
Generate minimal changes ∆x i to alter allocations, guided by both SHAP and LIME:
∆x∗i =argm ∆x in i | ∆x i |1 +λ | f(x i+∆x i) − f(x i) | s.t. ϕS ij LIRA(x i+∆x i) ̸ =ϕS ij LIRA(x i) (48)
SLIRA presents a robust, interpretable, and fairness-aware resource allocation framework by integrating global
and local explainability techniques. Its ability to optimize transparency, fairness, and adaptability makes it
particularly suited for high-stakes environments like public safety networks. The framework’s key advantages
include enhanced interpretability, reduced bias in allocations, improved stability over time, and the ability
to quantify uncertainty. By combining the strengths of SHAP and LIME, SLIRA sets a new standard for fair,
explainable, and accountable AI-driven decision-making.
The predictive model is designed to approximate the mapping from the network state to urgency-weighted
allocation scores, rather than to directly output final allocations. This separation allows the system to re-
place repeated solver invocations with a single forward inference step, significantly reducing computational
latency. Unlike solver-based approaches, the learning model can operate under partial observability and noisy
measurements and can generalize from historical patterns to unseen operating conditions. Consequently, the
predictive component provides a practical mechanism for real-time allocation guidance in PSNs, while the fi-
nal allocation remains subject to explicit feasibility and fairness constraints. Algorithm 1 provides the complete
operational specification of the SLIRA pipeline, detailing how predictive modeling, explainability, fairness reg-
ulation, and uncertainty quantification interact to produce interpretable resource allocation decisions. Starting
from the observed network state x(t), the algorithm generates urgency-weighted allocation scores, computes
global SHAP values and local LIME explanations, and fuses them into a unified attribution signal that directly
regulates the allocation update rule. The updated allocation is then projected onto the feasible constraint set
and supplemented with Bayesian uncertainty estimates to ensure confidence-aware operation. Together, these
steps define a coherent, explanation-driven allocation mechanism tailored for dynamic and safety–critical PSN
environments.
Scientific Reports | (2026) 16:14180 | https://doi.org/10.1038/s41598-026-43440-9 13

www.nature.com/scientificreports/
Algorithm 1. SLIRA (SHAP–LIME Integrated Resource Allocation) Pipeline
Scientific Reports | (2026) 16:14180 | https://doi.org/10.1038/s41598-026-43440-9 14

www.nature.com/scientificreports/
The definition of x(t), f θ(x(t)), and the update rule leading to A(t) establishes the complete SLIRA
pipeline. Unlike traditional solver-based or heuristic policies, SLIRA integrates prediction, explainability, fairness
regulation, and constraint projection into a unified iterative mechanism. This explicit formulation ensures that
the experimental results directly correspond to the defined model behavior and eliminates ambiguity regarding
the origin of the final allocation decisions.
Evaluation metrics
To explicitly address whether learning-based allocation is necessary given the availability of efficient solvers, we
benchmark the proposed SLIRA framework against direct solver-based optimization under identical conditions.
While the solver achieves optimal utility in static scenarios, its performance degrades under dynamic and
uncertain conditions due to repeated re-optimization overhead and sensitivity to imperfect state information.
SLIRA maintains comparable utility with significantly lower runtime, while additionally providing fair
consistency, explainability, and uncertainty awareness. These results demonstrate that the value of the proposed
approach lies not in exceeding solver optimality, but in delivering deployable, transparent, and risk-aware
allocation decisions in real-time PSN environments.
SLIRA is benchmarked against (i) a direct solver-based optimizer (ii) a black-box AI baseline that predicts
allocation scores followed by feasibility projection, and (iii) explainability ablations such as SHAP-only and
LIME-only post-hoc explanations. Performance is evaluated using utility/QoS, fairness gaps, explanation fidelity
and stability, uncertainty calibration, and runtime. Results are reported as mean ± standard deviation with 95%
confidence intervals across multiple seeds, and relative (%) improvements are computed to quantify performance
gains. The benchmark comparison includes solver-based methods, baseline AI approaches, explainable AI
variants, and the proposed SLIRA framework, all evaluated under identical Public Safety Network scenarios.
Table 2 presents a comprehensive comparison of classical optimization-based methods, heuristic and learning-
based approaches, post-hoc explainable AI models, and the proposed SLIRA framework for resource allocation
in Public Safety Networks. The evaluated methods differ in their allocation mechanisms, ranging from direct
convex optimization solvers and priority-based heuristics to learned AI models with and without explainability
and uncertainty awareness. The results demonstrate that direct solver-based approaches achieve optimal utility
under static conditions but incur higher computational costs and provide no interpretability. Greedy heuristics
offer minimal runtime overhead at the expense of substantially reduced utility and fairness. Black-box AI models
closely match solver performance with significantly lower runtime but lack transparency and fairness guarantees.
Incorporating post-hoc explainability (SHAP or LIME) improves interpretability reporting without materially
affecting allocation behavior or fairness. In contrast, the proposed SLIRA framework achieves a strong balance
between performance, fairness, explainability, and stability. While maintaining utility within 2% of the optimal
solver, SLIRA reduces the fairness gap by more than 40% relative to solver-based methods and exhibits superior
temporal stability. The full SLIRA model further provides uncertainty awareness through Bayesian inference,
enabling confidence-calibrated decisions with modest additional computational overhead that remains suitable
for real-time deployment.
The comparison highlights a crucial distinction: while the solver baseline provides mathematically optimal
allocations in static, perfectly known environments, it cannot adapt rapidly to dynamic PSN states without
incurring repeated computational overhead. The black-box AI model provides lower-latency inference but lacks
transparency and introduces higher fairness variability. SLIRA maintains near-optimal utility while delivering
significantly improved fairness consistency and much higher temporal stability. Furthermore, SLIRA uniquely
provides interpretable, feature-attributed decisions and uncertainty quantification, which are essential for
operational accountability in PSNs. Thus, the added value of SLIRA is not in outperforming solvers in static
utility, but in enabling deployable, accountable, and robust allocation decisions in dynamic and uncertain
settings.
In addition to absolute performance values, we compute relative improvements (%) for each method with
respect to the direct solver baseline. This reporting strategy provides a clearer assessment of trade-offs introduced
by explainability and uncertainty modeling. For example, we quantify the percentage reduction in fairness
disparity, the percentage gain in temporal stability, and the relative change in utility, which is typically below 2%
Avg.
Runtime
Explainability Fidelity Temporal Stability per Step
Method Allocation Mechanism Utility (↑) Fairness Gap (↓) (↑) (↑) (ms)
Direct Solver (Static Optimal) Convex optimization 1.000 ± 0.000 0.087 ± 0.012 N/A High 48.3
Warm-Started Solver Repeated optimization 0.992 ± 0.006 0.085 ± 0.014 N/A Medium 36.7
Greedy Heuristic Priority-based heuristic 0.913 ± 0.021 0.132 ± 0.028 N/A Medium 2.1
Black-Box AI Learned scores + projection 0.987 ± 0.010 0.094 ± 0.019 Low Medium 4.8
AI + SHAP (Post-hoc) Black-box + SHAP audit 0.986 ± 0.011 0.093 ± 0.018 Medium Medium 6.9
AI + LIME (Post-hoc) Black-box + LIME audit 0.984 ± 0.012 0.096 ± 0.020 Medium Low 7.4
SLIRA (No Bayesian) Explanation-regulated update 0.983 ± 0.009 0.061 ± 0.010 High High 9.2
SLIRA (Full Model) SHAP–LIME + Fairness + Bayesian 0.981 ± 0.008 0.052 ± 0.008 Very High Very High 10.6
Table 2. Comparative benchmarking of resource allocation strategies in public safety networks
Scientific Reports | (2026) 16:14180 | https://doi.org/10.1038/s41598-026-43440-9 15

www.nature.com/scientificreports/
Metric Black-Box AI AI + SHAP AI + LIME SLIRA (Full)
Utility Change (%) − 1.3% − 1.4% − 1.6% − 1.9%
Fairness Gap Reduction (%) − 7.9% − 6.9% − 5.7% − 40.2%
Temporal Stability Gain (%) + 8.1% + 9.4% + 6.7% + 31.5%
Explainability Gain Low Medium Medium High (Regulatory)
Table 3. Relative performance gains of explainable and SLIRA-based allocation methods compared to the
solver baseline
for SLIRA. Percentage-based metrics make explicit the benefits of explanation-regulated updates and highlight
cases where SLIRA provides substantial stability and fairness gains despite small differences in raw utility.
The results in Tables 2 and 3 show that SLIRA delivers a strong balance between performance and
interpretability. While the direct solver achieves the highest utility under static conditions, SLIRA remains within
1–2% of this value while achieving substantially improved fairness (over 40% reduction in fairness gap) and
significantly enhanced temporal stability (over 30% gain). Furthermore, SLIRA demonstrates markedly higher
explainability and fidelity due to the fusion of global and local attributes. The consistency of these gains across
multiple runs, as reflected by narrow confidence intervals, confirms that SLIRA improves transparency and
stakeholder interpretability without compromising allocation performance. These findings directly substantiate
the claims made in the introduction and validate the effectiveness of explanation-regulated decision-making.
Table 3 summarizes the relative (percentage-based) performance changes of learning-based and explainable
allocation strategies with respect to the direct solver baseline, providing a clearer interpretation of trade-offs
between efficiency, fairness, stability, and explainability. Negative values in Utility Change (%) indicate minor
reductions relative to solver optimality, while positive values in Fairness Gap Reduction and Temporal Stability
Gain reflect improvements over the baseline. The results show that black-box AI and post-hoc explainable AI
methods (SHAP and LIME) achieve utility levels close to the solver, with only marginal performance degradation
(≤ 1.6%), but offer limited improvements in fairness and temporal stability. In contrast, the proposed SLIRA
framework demonstrates a substantially different behavior: although it incurs a slightly larger utility deviation
(− 1.9%), it achieves a dramatic reduction in fairness disparity (− 40.2%) and a significant improvement in
temporal stability (+ 31.5%). Moreover, SLIRA uniquely provides regulatory grade explainability, where
explanations actively govern allocation decisions rather than serving as post-hoc diagnostics.
I. Standardized Evaluation Metrics: To ensure a rigorous and reproducible experimental validation, we adopt
a set of standardized and well-defined evaluation metrics that jointly capture allocation performance, fair-
ness, stability, explainability, and computational efficiency. Allocation performance is quantified using nor-
malized system utility, defined as the aggregate weighted satisfaction of user demands relative to the maxi-
mum achievable value under capacity constraints. Fairness is evaluated through the inter-group allocation
gap, measured as the absolute difference in mean resource allocation between protected user groups, which
directly reflects distributional equity. Temporal stability is assessed by computing the consistency of allo-
cation and explanation patterns across consecutive time steps, capturing the robustness of decisions under
dynamic network conditions. Explainability quality is evaluated through explanation fidelity and sparsity
metrics, which measure how accurately surrogate explanations approximate the predictive model while
remaining interpretable. Finally, computational efficiency is reported as the average per-step runtime, ena-
bling a direct comparison between solver-based, learning-based, and explainability-regulated approaches.
All metrics are formally defined prior to result presentation to avoid ambiguity and to facilitate reproduci-
bility.
II. Relative and Percentage-Based Performance Improvements: Beyond reporting absolute metric values, we
emphasize relative and percentage-based improvements to provide a clearer interpretation of the trade-
offs introduced by explainability and uncertainty modeling. For each metric, the performance of learn-
ing-based and explainable approaches is normalized with respect to the direct solver baseline, which serves
as a reference upper bound for static optimality. Relative changes are expressed as percentage gains or
losses, allowing direct comparison across heterogeneous metrics such as utility, fairness gap, and stability.
This reporting strategy highlights that while black-box and explainable AI approaches incur only marginal
utility degradation (typically below 2%), the proposed SLIRA framework achieves substantial relative im-
provements in fairness and temporal stability, far exceeding those of post-hoc explainable baselines.
III. Uncertainty and Variability Analysis: To account for stochasticity in traffic demand, channel conditions,
and learning processes, all experiments are conducted over multiple independent simulation runs with
different random seeds. Reported results correspond to the mean and standard deviation of each metric,
and confidence intervals are provided where appropriate. This variability analysis ensures that observed
improvements are statistically meaningful rather than artifacts of a single realization. In addition, SLI-
RA uniquely incorporates Bayesian uncertainty modeling, enabling explicit quantification of confidence
in both allocation decisions and explanation coefficients. The posterior variance of allocations is analyzed
alongside performance metrics, revealing that higher uncertainty correlates with volatile network states
and congestion events. This uncertainty-aware evaluation provides an additional layer of robustness as-
sessment that is absent in solver-based and black-box AI methods, which produce deterministic outputs
without confidence estimates.
Scientific Reports | (2026) 16:14180 | https://doi.org/10.1038/s41598-026-43440-9 16

www.nature.com/scientificreports/
IV. Interpretation and Experimental Credibility: The combination of standardized metrics, relative perfor-
mance reporting, and uncertainty analysis substantially strengthens the credibility of the experimental
validation. Rather than relying on isolated performance snapshots, the evaluation demonstrates consist-
ent trends across multiple runs and diverse scenarios. Importantly, the results show that SLIRA preserves
near-optimal allocation efficiency while delivering statistically significant improvements in fairness consist-
ency and temporal stability, supported by reduced variability and calibrated uncertainty estimates. These
findings directly substantiate the claim that explainability in SLIRA is not merely descriptive but opera-
tional, enabling more robust and accountable decision-making in dynamic public safety network environ-
ments.
To provide a standardized and reproducible basis for comparison, we evaluate all approaches using a set of
well-defined metrics that capture allocation performance, fairness, interpretability, and stability. (1) Utility: the
normalized system utility, defined as the weighted sum of satisfied user demands relative to the solver-optimal
benchmark. (2) Fairness gap: the absolute difference in average allocation between protected user groups. (3)
Temporal stability: the average correlation between consecutive allocation matrices, measuring robustness
under dynamic conditions. (4) Explainability fidelity: the agreement between the predictive model and its local
surrogate explanations (LIME) and the consistency of global attributions (SHAP). (5) Runtime: the average per-
step computational latency. These metrics allow us to quantify the contribution of explainability and uncertainty
modeling beyond raw allocation quality.
Computational complexity and runtime analysis
This section provides a rigorous computational analysis of the proposed SLIRA framework in comparison with
solver-based re-optimization methods. Specifically, we present (i) a formal asymptotic complexity derivation
that characterizes the theoretical scaling behavior of both approaches, (ii) an empirical runtime decomposition
that isolates the computational contribution of each component within the SLIRA pipeline, and (iii) a log-
scale scaling visualization that illustrates divergence in growth rates as the problem dimension increases. The
primary objective of this analysis is to clarify the structural reason why SLIRA achieves lower per-step latency,
even though it incorporates Bayesian uncertainty estimation and Monte Carlo–based explainability techniques
(SHAP and LIME), which may initially appear computationally intensive. While these components introduce
additional processing steps, their computational cost scales linearly with feature dimension and remain bounded
due to fixed sampling sizes. In contrast, solver-based approaches require repeated convex re-optimization at each
decision epoch, incurring cubic complexity in the number of allocation variables.
Theoretical asymptotic complexity analysis
Let U denote the number of users, R denote the number of resources, and F denote the feature dimension.
The total number of allocation decision variables is defined as N =UR. The direct solver baseline computes
allocations by solving the constrained utility maximization problem defined in Eqs. (22)–(23). Interior-point
methods for convex optimization exhibit worst-case computational complexity O(N3)=O((UR)3), primarily
due to repeated matrix factorization and Newton-step updates required during each iteration. In dynamic
Public Safety Network (PSN) environments where re-optimization is performed at every time step T, the total
computational complexity becomes O(T(UR)3). This cubic dependence on the decision variable dimension
leads to rapidly increasing runtime as the system scale grows.
In contrast, SLIRA decomposes the allocation procedure into structured and computationally lighter stages.
The predictive forward inference step has complexity O(UR). SHAP-based Monte Carlo sampling, with fixed
K =100, incurs complexity O(KF), while LIME local surrogate fitting, with fixed P =500, contributes
O(PF). Variational Bayesian uncertainty estimation scales as O( θ ), where θ denotes the number of model
| | | |
parameters. Finally, the explanation-driven allocation update and projection step has complexity O(UR).
Because K and P are fixed constants independent of system size, the dominant scaling term becomes O(UR).
Consequently, under dynamic operation across T time steps, the total computational complexity of SLIRA is
O(TUR), which grows linearly with the number of allocation variables.
Formally, the asymptotic comparison satisfies
limN
→∞O
O
(
(
N
N
3
)
)
=0
, demonstrating that SLIRA grows
asymptotically slower than solver-based re-optimization as system dimension increases.
Importantly, Bayesian inference and Monte Carlo sampling in SLIRA operate on feature attribution and
learned score surfaces rather than on combinatorial allocation search. Therefore, their computational cost
scales linearly with feature dimension and remains independent of the cubic growth associated with convex re-
optimization over allocation variables. This structural distinction explains why SLIRA achieves lower per-step
latency despite incorporating uncertainty modeling and explainability mechanisms. Figure 3 presents a log–log
scaling comparison between solver-based convex optimization O(N3) and the SLIRA framework O(N). The
horizontal axis represents the number of decision variables N =UR, while the vertical axis shows normalized
computational cost on a logarithmic scale. On the log–log plot, the solver-based optimization curve exhibits
an approximate slope of 3, confirming its cubic scaling behavior O(N3), while the SLIRA curve exhibits an
approximate slope of 1, confirming its linear scaling O(N). As the number of decision variables N increases, the
divergence between the two curves becomes increasingly pronounced, illustrating how solver-based approaches
experience rapid runtime escalation under large-scale Public Safety Network configurations. In contrast,
SLIRA maintains controlled and predictable growth due to its linear dependence on system dimension. This
visualization clearly demonstrates that the observed runtime advantage of SLIRA arises from fundamental
structural differences in computational complexity rather than from minor constant-factor optimizations.
Scientific Reports | (2026) 16:14180 | https://doi.org/10.1038/s41598-026-43440-9 17

www.nature.com/scientificreports/
Fig. 3. Asymptotic Computational Complexity Scaling of Solver-Based Optimization versus SLIRA
Component Average runtime (ms)
Predictive Forward Pass 2.1
SHAP Computation 3.4
LIME Local Fit 2.8
Bayesian Update 1.2
Allocation Projection 0.9
Total SLIRA 10.4 ms
Direct Solver Re-Optimization 36.7 ms
Table 4. Per-step latency breakdown (U = 50, R = 20).
Per-step runtime decomposition
To complement the asymptotic analysis and provide practical insight into computational behavior, this
subsection presents a detailed per-step runtime decomposition of the SLIRA framework. Rather than reporting
only aggregate latency, the computational contribution of each operational component within the allocation
pipeline is isolated and quantified, including predictive inference, SHAP computation, LIME surrogate fitting,
Bayesian uncertainty estimation, and the explanation-driven projection step. To provide further transparency,
we report a detailed per-step latency breakdown.
Table 4 provides a detailed decomposition of SLIRA’s per-step runtime across its principal computational
stages, including predictive inference, SHAP-based global attribution, LIME-based local surrogate fitting,
Bayesian uncertainty estimation, and the explanation-driven projection step. This breakdown makes explicit
how total latency is distributed within the framework and reveals that no single component disproportionately
dominates the overall computational budget. Although SHAP and LIME introduce additional processing
through Monte Carlo sampling and local perturbation modeling, their computational costs remain bounded
because the sampling sizes (K and P) are fixed constants independent of system dimension. As a result, their
contribution scales linearly with feature dimension rather than with the number of allocation variables. In
contrast, the solver baseline performs full convex re-optimization at every decision epoch, requiring repeated
matrix factorizations and Newton-step updates whose complexity grows cubically with the number of decision
variables. This structural requirement leads to substantially higher per-step latency, particularly as system size
increases. The runtime decomposition therefore demonstrates that Bayesian inference and Monte Carlo-based
explainability mechanisms introduce only modest linear overhead within SLIRA and do not constitute the
dominant source of computational cost.
Scientific Reports | (2026) 16:14180 | https://doi.org/10.1038/s41598-026-43440-9 18

www.nature.com/scientificreports/
Empirical scaling behavior
To validate the theoretical complexity analysis, runtime growth was measured across progressively increasing
system dimensions. The results indicate that solver-based runtime exhibits super linear growth once the number
of users exceeds approximately U >40, reflecting the cubic dependence on allocation variables. In contrast,
SLIRA’s runtime increases approximately linearly with system size, consistent with the derived asymptotic
behavior. Even under large-scale configurations, SLIRA maintains stable per-step latency below 15 ms,
demonstrating predictable and controlled scaling. These empirical observations confirm that the observed
speed advantage is not incidental or implementation-specific but structurally grounded in the computational
architecture of the framework. The primary reason SLIRA achieves lower runtime lies in replacing repeated
convex re-optimization with a computational pipeline composed of a single forward inference step, fixed cost
explainability mechanisms, and linear projection operations. Solver-based approaches repeatedly perform
matrix inversion and Newton-step updates whose computational burden scales cubically with the number
of allocation variables. By contrast, SLIRA operates on a learned urgency-weighted score surface and applies
explanation-regulated updates without solving a full optimization problem at each time step. Consequently, the
runtime benefit emerges from architectural design and complexity order differences rather than from omission
of Bayesian or Monte Carlo components.
Simulation scenario and PSN modeling assumptions
To evaluate the effectiveness, interpretability, and fairness of the proposed SLIRA framework, a realistic yet
controllable PSN simulation environment was constructed. The simulation is designed to emulate operational
conditions commonly encountered in emergency response scenarios, such as natural disasters, large public
events, and multi-agency crisis coordination, where communication resources are limited and demand fluctuates
rapidly.
The simulated PSN consists of a centralized radio access network serving a set of emergency users
U = { u 1 ,u 2 ,...,u N } , where N ∈{ 20,30,50 } depending on the experiment. The available communication
resources R = { r 1 ,r 2 ,...,r M } represent shared bandwidth blocks, with M =5. Each resource r j is associated
with a finite capacity C j, reflecting spectrum and infrastructure limitations typical of PSNs during congestion.
Users are divided into heterogeneous emergency classes, including police, fire services, medical responders,
and command units. Each user u i is characterized by:
I. A time-varying demand d i(t), representing required data rate or communication load,
II. A priority level p i, reflecting mission criticality and role hierarchy,
III. A protected group attribute (used only for fairness evaluation, not decision input).
Priority levels are normalized to ensure comparability across agencies and are dynamically updated in response
to emergency escalation or de-escalation phases.
Emergency traffic is modeled using stochastic burst processes to capture sudden surges in communication
demand, such as those observed during disaster onset or major incidents. Specifically, user demands follow a
mixed distribution combining baseline Poisson arrivals with bursty spikes governed by a heavy-tailed process.
This modeling choice reflects the unpredictable and highly dynamic nature of PSN traffic.
Time is discretized into allocation intervals t=1,...,T, where SLIRA updates allocations iteratively based
on both predicted utility and explanation-guided feedback. This enables the framework to adapt to evolving
network conditions while maintaining interpretability and fairness constraints.
All experiments are conducted using synthetic data generated under the above assumptions. While real PSN
datasets are typically unavailable due to confidentiality and security restrictions, the simulation parameters are
chosen to closely align with values reported in public safety communication standards and prior literature. The
use of synthetic data allows systematic control over network scale, demand variability, and fairness stress-testing
while ensuring reproducibility.
The AI-based prediction model estimates demand urgency and allocation utility from observable network
state features, including current load, historical demand trends, and priority indicators. SHAP and LIME
explanations are then computed on top of these predictions to regulate allocation updates, enforce fairness, and
provide human-interpretable justifications.
The chosen simulation framework balances realism and analytical clarity. It is sufficiently rich to reflect real
PSN challenges such as congestion, priority conflicts, and emergency dynamics—while remaining interpretable
and computationally tractable for explainable AI analysis. This design allows a focused evaluation of SLIRA’s
core contributions: transparent decision-making, fairness-aware resource allocation, and uncertainty-informed
adaptation under high-stakes conditions.
Computational complexity analysis
Computational efficiency is a critical requirement for resource allocation in PSNs, where decisions must be
made under strict real-time constraints. This section analyzes the computational complexity of the proposed
SLIRA framework and compares it with standalone SHAP- and LIME-based explainability approaches. SHAP
computes feature attributions using cooperative game theory, which has an exponential worst-case complexity
(2n) with respect to the number of features n. Such complexity is impractical for large-scale or real-time
O
PSN deployments. To address this, the proposed framework adopts Monte Carlo SHAP sampling, reducing the
computational cost to (K n), where K is the number of sampled coalitions. This approximation preserves
O ·
explanation fidelity while significantly reducing runtime. LIME, on the other hand, constructs local surrogate
models by generating perturbed samples around each instance. Its complexity scales as (P n), where P is
O ·
the number of perturbations. While LIME is computationally efficient for local explanations, it lacks global
Scientific Reports | (2026) 16:14180 | https://doi.org/10.1038/s41598-026-43440-9 19

www.nature.com/scientificreports/
consistency and may require repeated evaluations for dynamic network states. SLIRA integrates SHAP and
LIME in a unified framework while maintaining tractable computational complexity.
SLIRA amortizes the cost of global SHAP computations across multiple allocation intervals, avoiding
redundant recalculations at every time step. As a result, the marginal per-iteration complexity of SLIRA
approaches that of LIME while retaining global explainability. The allocation update step, including SHAP–
LIME gradient computation and fairness constraint enforcement, scales linearly with the number of users U and
resources R, yielding a complexity of (U R). Bayesian uncertainty estimation is performed using variational
O ·
inference, which adds a modest overhead that scales linearly with the number of model parameters and does
not dominate the overall runtime. Compared to standalone SHAP, SLIRA significantly reduces runtime while
providing richer interpretability and fairness guarantees. Compared to LIME, SLIRA introduces a moderate
additional cost due to global explanation alignment but achieves superior stability, fairness consistency, and
uncertainty awareness. This trade-off is acceptable in PSN environments, where decision justification and
reliability are as critical as raw computational speed.
Dataset and resource description
This study evaluates SLIRA framework using a synthetic, yet realistic dataset designed to emulate operational
conditions in Public Safety Networks (PSNs). Due to security, confidentiality, and availability constraints
associated with real PSN data, synthetic data are commonly adopted in the literature to enable controlled
experimentation while preserving realism. The dataset parameters and assumptions are chosen in accordance
with typical public safety communication scenarios reported in prior studies. The simulated PSN consists of a
set of emergency users U = { u 1 ,u 2 ,...,u N } , where N ∈{ 20,30,50 } depending on the experiment. Users
represent heterogeneous public safety entities, including police units, fire services, medical responders, and
command-and-control personnel. Each user is characterized by a time-varying traffic demand, a priority level
reflecting mission criticality, and observable network state features used by the AI predictor. The available
resources R = { r 1 ,r 2 ,...,r M } correspond to shared communication resources such as bandwidth blocks,
time–frequency resource units, or logical network slices in LTE/5G public safety systems. In the simulations,
M =5, and each resource r j has a finite capacity C j, representing spectrum and infrastructure limitations
under congested emergency conditions. Traffic demand is modeled as a stochastic process combining baseline
communication activity with bursty emergency-driven surges. This captures realistic PSN behavior, where
sudden incidents lead to sharp increases in data and voice traffic. Priority levels are normalized and dynamically
adjusted to reflect changes in emergency severity, escalation, or resolution phases. These demand and priority
signals are used as inputs to the AI-based prediction model, which estimates allocation urgency and utility. The
dataset also includes protected group attributes used exclusively for fairness evaluation and monitoring. These
attributes are not provided as inputs to the allocation model, ensuring that fairness constraints are enforced
through explainability-driven regulation rather than direct discrimination. All experiments are conducted over
multiple steps to evaluate dynamic adaptation, explanation stability, and uncertainty behavior.
Cost of SLIRA versus SHAP and LIME: time complexity and runtime considerations
In PSNs, computational efficiency is a critical design requirement, as resource allocation decisions must be
generated under strict latency and reliability constraints. This subsection analyzes the computational cost of the
proposed SLIRA framework and compares it with standalone SHAP- and LIME-based explainability methods,
highlighting the trade-offs between runtime complexity and explainability performance.
Standalone SHAP computes feature attributions based on cooperative game theory, which exhibits
exponential worst-case complexity (2n) with respect to the number of features n. Such complexity is
O
prohibitive for real-time PSN deployment. To mitigate this issue, SLIRA employs Monte Carlo sampling–based
SHAP approximations, reducing the computational cost to (K n), where K denotes the number of sampled
O ·
coalitions. This approximation preserves global explanation fidelity while significantly reducing runtime.
LIME, in contrast, generates local explanations by fitting surrogate models around individual instances using
perturbed samples. Its complexity scales as (P n), where P is the number of perturbations. While LIME
O ·
is computationally efficient for local interpretability, it lacks global consistency and often requires repeated
recalculations in dynamic environments such as PSNs.
where global SHAP sampling and local LIME perturbations are executed in parallel. Importantly, SLIRA
amortizes the cost of SHAP computations across multiple allocation intervals by reusing global explanations
when network conditions evolve smoothly. As a result, the marginal per-iteration runtime of SLIRA approaches
that of LIME while retaining global fairness awareness. The allocation update step, including SHAP–LIME
gradient fusion, fairness enforcement, and capacity constraint handling, scales linearly with the number of users
U and resources R, yielding a complexity of (U R). Bayesian uncertainty estimation is implemented using
O ·
variational inference, which introduces a modest additional overhead that scales linearly with the number of
model parameters and does not dominate the overall runtime. Figure 4 illustrates the practical runtime and
scalability trade-offs among SHAP, LIME, and SLIRA. While SLIRA incurs a slightly higher computational cost
than LIME due to global explanation alignment, it remains significantly more efficient than standalone SHAP and
provides superior fairness consistency, temporal stability, and uncertainty quantification. These characteristics
make SLIRA well suited for safety–critical PSN scenarios, where explainability and reliability are as important
as computational speed. SLIRA achieves a balanced trade-off between computational cost and explainability
performance, offering a scalable and practically deployable solution for real-time explainable resource allocation
in PSN’s.
To provide a comprehensive evaluation and directly address concerns regarding the necessity of the proposed
learning-based allocation mechanism, we compare SLIRA against two key baseline categories: (i) direct solver-
based optimization, representing the mathematically optimal solution under perfect state information, and (ii)
Scientific Reports | (2026) 16:14180 | https://doi.org/10.1038/s41598-026-43440-9 20

www.nature.com/scientificreports/
Fig. 4. Comparative runtime and explainability cost analysis of SHAP, LIME, and the proposed SLIRA
framework in public safety networks
the original non-explainable AI model, representing the predictive allocation approach without explanation
regulation. The solver baseline computes an optimal allocation at every time step using convex optimization
under the full system constraints. The original AI baseline employs the predictive model f θ(x(t)) to generate
allocation scores, which are then projected onto the feasible allocation space without incorporating SHAP/LIME
explanations or uncertainty modeling. These baselines allow us to quantify, under identical scenarios, the trade-
offs between optimality, real-time feasibility, and explainability offered by SLIRA.
Results and discussion
This section presents the results and analysis of SLIRA framework, evaluating its performance in terms of
explainability, fairness, and efficiency. The findings highlight how SLIRA enhances resource distribution
transparency, ensuring that allocation decisions are both interpretable and justifiable. Furthermore, the
discussion examines the impact of SLIRA’s optimization techniques, including sparsity constraints, Bayesian
uncertainty modeling, and fairness-aware adjustments, on overall system stability. Key performance metrics
such as explanation consistency, feature attribution accuracy, and allocation fairness are analyzed to validate
SLIRA’s effectiveness. Additionally, insights from expert evaluations are incorporated to assess how SLIRA’s
explanations align with human decision-making standards. The results demonstrate that SLIRA significantly
improves accountability, adaptability, and stakeholder trust, making it a powerful tool for explainable and
equitable AI-driven resource management.
Figure 5 illustrates user utility distribution in a resource allocation system, aiming to maximize overall
utility while maintaining fairness. The blue bars represent the utility achieved by each user, showing significant
variation across the user base. The red dashed line indicates the average utility, providing a benchmark for
assessing whether individual users receive higher or lower than average resource allocation benefits. The results
demonstrate that some users exceed the average utility threshold, while others fall below, highlighting the need
for adaptive allocation mechanisms to balance efficiency and fairness in resource distribution.
Figure 6 presents the variation of the XAI-integrated objective function as a function of λ trade-off parameter,
which balances utility maximization and explanation fidelity. The fluctuating pattern suggests that small
changes in λ lead to significant variations in the objective function, indicating a complex relationship between
predictive performance and interpretability. Higher values of λ do not necessarily correspond to an optimal
trade-off, highlighting the need for fine-tuned regularization to balance utility and explanation divergence. This
analysis underscores the importance of selecting an appropriate λ value to achieve an optimal balance between
explainability and decision efficiency in resource allocation.
Figure 7 represents the probability density function of uncertainty in allocation decisions, modeled using
a Bayesian framework. The distribution follows a bell-shaped curve, indicating that most model parameter
(Θ) values are concentrated around zero, with lower probabilities for extreme values. This suggests that the
allocation model is more confident in central predictions, while uncertainty increases towards the distribution
tales. Such an analysis is crucial for decision-making in resource allocation, as it allows stakeholders to quantify
the confidence levels associated with different allocation strategies.
Figure 8 presents a histogram depicting the distribution of the number of active allocations per user,
emphasizing the impact of sparsity constraints in ensuring interpretability. The most frequent numbers of active
Scientific Reports | (2026) 16:14180 | https://doi.org/10.1038/s41598-026-43440-9 21

www.nature.com/scientificreports/
Fig. 5. Utility maximization in resource allocation across users
Fig. 6. Trade-off analysis in XAI-integrated objective function
allocations are three, suggesting that the model enforces a limit on excessive allocations, thereby enhancing
decision clarity. The presence of users with varying numbers of active allocations indicates some flexibility in
the allocation process while still maintaining a controlled level of sparsity. This approach helps in simplifying
resource distribution decisions, ensuring that allocations remain concise, interpretable, and effective for real-
world applications.
Figure 9 illustrates the evolution of explanation consistency over multiple time steps, reflecting the system’s
stability in generating interpretable decisions. The initial fluctuations indicate variability in explanations, but as
the system progresses, the explanation values increase and stabilize, suggesting improved reliability. The high
final consistency value of 0.967 demonstrates that the model maintains a strong level of interpretability over
time, ensuring that explanations remain coherent and meaningful. This analysis highlights the effectiveness
of the monitoring framework, ensuring that AI-driven resource allocation decisions remain trustworthy and
transparent.
Scientific Reports | (2026) 16:14180 | https://doi.org/10.1038/s41598-026-43440-9 22

www.nature.com/scientificreports/
Fig. 7. Bayesian uncertainty in allocation decisions
Fig. 8. Sparsity constraint for interpretability in resource allocation
Figure 10 presents a contour plot visualizing the loss function associated with the unified explanation
objective, where λ1 and λ2 control trade-offs between explanation sparsity and SHAP consistency. The color
gradient represents loss values, with darker regions indicating lower loss and lighter regions signifying higher
loss. The distribution of loss values suggests that optimal trade-offs exist in specific parameter ranges, where
the model achieves a balance between explainability constraints and predictive accuracy. This analysis helps
in identifying ideal hyperparameter settings, ensuring that the explanation framework remains interpretable,
efficient, and reliable for decision-making.
Figure 11 depicts the relationship between the SHAP-informed proximity kernel weight and the Euclidean
distance D(xi,z)D(x_i, z). The decreasing trend in kernel weight illustrates that closer perturbations (lower
distances) are assigned higher weights, reinforcing the local interpretability of the model. As the distance
increases, the kernel weight gradually declines, indicating a diminishing influence of farther instances on the
explanation process. This behavior aligns with SHAP’s emphasis on global feature importance, ensuring that
resource allocation decisions prioritize relevant local perturbations while maintaining consistency with broader
system-level explanations.
Scientific Reports | (2026) 16:14180 | https://doi.org/10.1038/s41598-026-43440-9 23

www.nature.com/scientificreports/
Fig. 9. System performance monitoring through explanation consistency
Fig. 10. Loss visualization for unified explanation objective
Figure 12 illustrates the impact of the SHAP-LIME hybrid gradient on dynamic resource allocation updates,
as governed by the parameter γ\gamma. The linear increase in allocation updates suggests that as γ\gamma
increases, the system places a greater emphasis on SHAP-based global fairness over LIME’s local fidelity. This
smooth and consistent growth pattern indicates that the integration of SHAP and LIME ensures a balanced
approach to resource distribution adjustments.
Such a framework enhances decision-making transparency, allowing for fair and interpretable resource
allocation in dynamic environments. Figure 13 presents a group fairness constraint analysis, comparing
the feature contributions of two distinct groups in a resource allocation system. The histogram illustrates
the distribution of feature contributions for Group 1 (blue) and Group 2 (red), with vertically dashed lines
representing their respective mean values. The minimal difference of 0.022 between the two group means
suggests that the allocation model achieves a high degree of fairness, ensuring no significant bias in feature
importance. This fairness constraint enforcement helps maintain equitable decision-making, reducing potential
disparities in AI-driven resource allocation.
Figure 14 illustrates the temporal consistency of explanations generated by SHAP (solid blue line) and SLIRA
(dashed red line) across different time steps. The fluctuations in both explanation methods indicate variations
Scientific Reports | (2026) 16:14180 | https://doi.org/10.1038/s41598-026-43440-9 24

www.nature.com/scientificreports/
Fig. 11. SHAP-informed proximity kernel and distance relationship
Fig. 12. Dynamic resource allocation with SHAP-LIME hybrid gradient
in feature importance over time, with SHAP exhibiting more stable patterns compared to SLIRA. The overall
consistency score of 0.592 suggests a moderate level of stability in the explanation outputs, highlighting potential
areas for improving alignment between global and local interpretability. This analysis is crucial for ensuring
reliable and explainable AI-driven resource allocation, where consistency in feature importance directly impacts
fairness and trust in decision-making. Figure 15 visualizes the impact of counterfactual changes (Δx) on the
i
model’s predictions, where the y-axis represents the absolute change in output |f(x+Δ x)−f(x )|. Initially, as Δx
i i i i
increases, the prediction changes decrease, indicating a region of stability in the model’s decision boundary.
However, beyond a certain threshold (around Δx ≈ 1.5), the change in prediction reaches a local minimum,
i
suggesting a point where the model’s decision is highly robust to minor alterations.
This analysis is essential for evaluating model sensitivity, ensuring interpretability, and identifying stable
decision regions in resource allocation tasks. Figure 16 compares the agreement between human expert
allocations (A (human)) and the SLIRA model allocations (A (sLIRA)), with an overall agreement error of 0.390.
ij ij
The data points exhibit variability, indicating differences in decision alignment between human experts and
SLIRA across multiple cases. Some points are closely clustered along the diagonal, suggesting areas where SLIRA
aligns well with human judgment, while others deviate significantly, highlighting instances of disagreement.
Scientific Reports | (2026) 16:14180 | https://doi.org/10.1038/s41598-026-43440-9 25

www.nature.com/scientificreports/
Fig. 13. Group fairness constraint in feature contribution analysis
Fig. 14. Temporal consistency analysis of SHAP and SLIRA explanations
This validation process is crucial for refining SLIRA’s decision-making transparency, ensuring that AI-driven
allocations align with expert expectations while maintaining fairness and efficiency.
Figure 17 shows that SLIRA can demonstrate high precision, matching SHAP’s accuracy while significantly
surpassing LIME’s performance. By integrating SHAP’s global Shapley values with LIME’s local approximations,
SLIRA ensures accuracy across both system-wide assessments and per-instance evaluations. Unlike SHAP,
which overlooks local variations, or LIME, which lacks global consistency, SLIRA’s hybrid approach delivers
comprehensive interpretability.
In sparsity control, SLIRA effectively balances feature selection by utilizing elastic regularization, ensuring
that non-critical features are minimized without compromising accuracy. This enhances model clarity and
interpretability beyond SHAP’s limited sparsity handling and LIME’s moderate control. SLIRA also excels in
computational efficiency, significantly reducing processing demands compared to SHAP and outperforming
LIME. By employing SHAP-informed sampling, SLIRA accelerates decision-making, making it well-suited for
real-time resource allocation in high-stakes scenarios such as emergency response. Beyond interpretability and
efficiency, SLIRA enforces group fairness and temporal stability, dynamically adjusting allocations in response
Scientific Reports | (2026) 16:14180 | https://doi.org/10.1038/s41598-026-43440-9 26

www.nature.com/scientificreports/
Fig. 15. Counterfactual explanations and prediction sensitivity
Fig. 16. Human validation of SLIRA agreement with experts
to crises while ensuring regulatory compliance. In contrast, SHAP’s static fairness framework and LIME’s
instability in dynamic environments limit their applicability for long-term, high-risk deployments. Additionally,
SLIRA’s human-validated explanations enhance audit-ready transparency, making it an essential tool for public
safety networks and critical decision-making environments. Figure 18 presents a comparative evaluation of
SHAP, LIME, and SLIRA across three key explainability parameters: Scalability, Dynamic Adaptability, and
Uncertainty Quantification. SLIRA demonstrates the highest scalability, outperforming both SHAP and LIME
by efficiently handling large datasets and complex models. While LIME achieves moderate scalability, SHAP
struggles in this area due to its computationally intensive nature, limiting its applicability in large-scale systems.
In terms of Dynamic Adaptability, SLIRA again surpasses SHAP and LIME by effectively adjusting to changing
environments and real-time conditions.
SHAP and LIME exhibit only moderate adaptability, making them less reliable in high-stakes applications
that require continuous adjustment. SLIRA’s superior adaptability ensures its suitability for dynamic domains
such as crisis management and evolving network systems. For Uncertainty Quantification, SLIRA leads by
providing robust confidence estimation in model explanations, ensuring greater reliability and transparency.
SHAP maintains moderate effectiveness in handling uncertainty, offering reasonable but less adaptable
estimations. LIME, however, ranks the lowest in this category, indicating limitations in accurately quantifying
the uncertainty associated with its explanations. Figure 19 illustrates the progressive improvement from SHAP
to LIME to SLIRA across three key parameters: Human Interpretability, Counterfactual Robustness, and Group
Fairness Enforcement. SHAP provides a strong baseline for interpretability but lacks adaptability and fairness
mechanisms. LIME enhances interpretability slightly while offering marginal improvements in robustness and
Scientific Reports | (2026) 16:14180 | https://doi.org/10.1038/s41598-026-43440-9 27

www.nature.com/scientificreports/
Fig. 17. SLIRA’s superiority in precision, sparsity control, and computational efficiency
Fig. 18. Comparative evaluation of SHAP, LIME, and SLIRA across scalability, dynamic adaptability, and
uncertainty quantification
fairness. SLIRA, by integrating the strengths of both, achieves the highest overall performance. In Counterfactual
Robustness, SLIRA demonstrates significant improvements over both SHAP and LIME, ensuring that model
explanations remain stable under minor input variations. SHAP, while effective in some scenarios, does not
explicitly account for counterfactual consistency. LIME provides moderate robustness but lacks the structural
enhancements that SLIRA incorporates to maintain reliability in complex decision-making environments. For
Group Fairness Enforcement, SLIRA outperforms both SHAP and LIME by implementing mechanisms that
dynamically adjust allocations to maintain fairness across different groups. SHAP, while ensuring a degree
of fairness at a global level, lacks adaptability for real-time adjustments. LIME introduces localized fairness
considerations but does not fully address systemic biases, making SLIRA the most effective solution for equitable
decision-making. Figure 20 visualizes the distribution of performance scores for SHAP, LIME, and SLIRA across
three critical parameters: Emergency Prioritization, Explanation Divergence, and Regulatory Compliance.
SLIRA consistently outperforms SHAP and LIME by maintaining higher median scores and lower variance,
Scientific Reports | (2026) 16:14180 | https://doi.org/10.1038/s41598-026-43440-9 28

www.nature.com/scientificreports/
Fig. 19. Waterfall-based comparative analysis of SHAP, LIME, and SLIRA across interpretability, robustness,
and fairness
Fig. 20. Analysis of SHAP, LIME, and SLIRA across emergency prioritization, explanation divergence, and
regulatory compliance
indicating robust and stable performance. In contrast, SHAP and LIME exhibit broader distributions, suggesting
less consistency in their evaluations.
In Explanation Divergence, where lower raw values indicate better performance, SLIRA demonstrates the
most concentrated and optimized distribution. This suggests that SLIRA produces more consistent and reliable
explanations, addressing a key limitation in SHAP and LIME, which show wider spreads and lower median
scores. The instability in SHAP and LIME makes them less suitable for high-stakes applications requiring
precise and trustworthy model interpretations. For Regulatory Compliance, SLIRA again leads with the highest
performance and the least variability, ensuring adherence to established fairness and governance standards.
SHAP provides a reasonable baseline but lacks the adaptability required for evolving compliance frameworks.
LIME, with the most dispersed and lower scores, struggles to meet regulatory demands consistently, making
SLIRA the most suitable approach for applications where strict compliance and interpretability are essential.
Conclusion
This study presents an XAI-based resource allocation framework designed to enhance transparency, fairness,
and efficiency in PSNs. As PSNs play a critical role in facilitating real-time communication and coordination
among emergency responders, ensuring optimal resource allocation is essential for effective crisis management.
However, traditional AI-based models often function as black-box systems, making it difficult for stakeholders to
interpret and trust their decisions. To address this limitation, the proposed framework integrates SHAP (Shapley
Additive Explanations) and LIME (Local Interpretable Model-Agnostic Explanations), providing both global
and local interpretability. This enables decision-makers to better understand and validate AI-driven allocations,
ensuring that resources are distributed in a transparent and justifiable manner. Additionally, the incorporation
of fairness-aware constraints and Bayesian uncertainty modeling ensures that allocations remain equitable while
maintaining reliability in highly dynamic emergency conditions. By systematically analyzing feature importance
and prediction confidence, the framework minimizes biases and improves trust among emergency personnel
Scientific Reports | (2026) 16:14180 | https://doi.org/10.1038/s41598-026-43440-9 29

www.nature.com/scientificreports/
and policymakers. Experimental evaluations confirm that the proposed approach significantly enhances
explainability and stakeholder confidence without compromising allocation performance. Future research may
explore the integration of real-time feedback loops, adaptive learning mechanisms, and reinforcement learning
strategies to further refine decision-making processes, ultimately improving the resilience and effectiveness of
PSNs in high-stakes emergency scenarios.
Data availability
The data of this study is available from the corresponding author upon request. Corresponding author: Dr. Mo-
hammed M. Alammar, Department of Electrical Engineering, King Khalid University, Abha, Asir 61421, Saudi
Arabia (email: mmalamar@kku.edu.sa).
Received: 16 November 2025; Accepted: 4 March 2026
References
1. Raja, S. et al. OCHSA: Designing energy‐efficient lifetime‐aware leisure degree adaptive routing protocol with optimal cluster head
selection for 5G communication network disaster management. Sci. Program. 2022(1), 5424356. h tt p s : / / d o i .o r g / 1 0 . 1 1 55 / 2 0 2 2 / 5 4
2 4 3 5 6 (2022).
2. Alsamhi, S. H. et al. Green internet of things using UAVs in B5G networks: A review of applications and strategies. Ad Hoc Netw.
117, 102505. https://doi.org/10.1016/j.adhoc.2021.102505 (2021).
3. Mahor, V., Rawat, R., Kumar, A., Garg, B., & Pachlasiya, K. (2023). IoT and artificial intelligence techniques for public safety and
security. In Smart urban computing applications (pp. 111–126). https://doi.org/10.1201/9781003373247-5
4. Khan, A., Gupta, S. & Gupta, S. K. Emerging UAV technology for disaster detection, mitigation, response, and preparedness. J.
Field Robot. https://doi.org/10.1002/rob.22075 (2022).
5. Alsamhi, S. H. et al. UAV computing-assisted search and rescue mission framework for disaster and harsh environment mitigation.
Drones 6(7), 154. https://doi.org/10.3390/drones6070154 (2022).
6. Neely, S., Eldredge, C. & Sanders, R. Health information seeking behaviors on social media during the COVID-19 pandemic
among American social networking site users: Survey study. J. Med. Internet Res. https://doi.org/10.2196/29802 (2021).
7. Marome, W. & Shaw, R. COVID-19 response in Thailand and its implications on future preparedness. Int. J. Environ. Res. Public
Health 18(3), 1089. https://doi.org/10.3390/ijerph18031089 (2021).
8. Mohiuddin, M., Hosseini, E., Faradonbeh, S. B. & Sabokro, M. Achieving human resource management sustainability in
universities. Int. J. Environ. Res. Public Health 19(2), 928. https://doi.org/10.3390/ijerph19020928 (2022).
9. Seid, A. M., Boateng, G. O., Mareri, B., Sun, G. & Jiang, W. Multi-agent DRL for task offloading and resource allocation in multi-
UAV enabled IoT edge network. IEEE Trans. Netw. Serv. Manag. 18(4), 4531–4547. https://doi.org/10.1109/TNSM.2021.3096673
(2021).
10. Wang, H. & Ran, B. Network governance and collaborative governance: A thematic analysis on their similarities, differences, and
entanglements. Public Manag. Rev. https://doi.org/10.1080/14719037.2021.2011389 (2023).
11. Fauzan, R., Harsono, K., Meisandy, R. P., Barokah, M. & Muhaimin, M. I. Optimising human resource management as an effort to
improve employee performance through digital attendance. Riwayat Educ. J. Hist. Humanit. 7(1), 16–25. h t t p s : / / do i . o r g / 1 0 .2 4 8 1 5
/ j r . v7 i 1 . 3 6 4 1 2 (2024).
12. Zhang, J. & Chen, Z. Exploring human resource management digital transformation in the digital age. J. Knowl. Econ. h t t p s : // d o i .
o r g / 10 . 1 0 0 7 / s 1 31 3 2 - 0 2 3 - 0 12 1 4 - y (2024).
13. Trischler, J. & Westman Trischler, J. Design for experience–a public service design approach in the age of digitalization. Public
Manag. Rev. https://doi.org/10.1080/14719037.2021.1899272 (2022).
14. Shet, S. V., Poddar, T., Samuel, F. W. & Dwivedi, Y. K. Examining the determinants of successful adoption of data analytics in human
resource management–A framework for implications. J. Bus. Res. 131, 311–326. https://doi.org/10.1016/j.jbusres.2021.03.054
(2021).
15. Wang, S. et al. Explainable AI for 6G use cases: Technical aspects and research challenges. IEEE Open Journal of the Communications
Society https://doi.org/10.1109/OJCOMS.2024.3386872 (2024).
16. Zhang, K., Zheng, B., Xue, J., & Zhou, Y. (2025). Explainable and Trust-Aware AI-Driven Network Slicing Framework for 6G IoT
Using Deep Learning. IEEE Internet of Things Journal, 1. https://doi.org/10.1109/JIOT.2025.3619970
17. Nwakanma, C. I., Ahakonye, L. A. C., Njoku, J. N., Odirichukwu, J. C., Okolie, S. A., Uzondu, C., ... & Kim, D. S. (2023). Explainable
artificial intelligence (XAI) for intrusion detection and mitigation in intelligent connected vehicles: A review. Applied Sciences,
13(3), 1252. https://doi.org/10.3390/app13031252
18. Sun, G., Xu, Z., Yu, H. & Chang, V. Dynamic network function provisioning to enable Network in Box for industrial applications.
IEEE Trans. Ind. Inform. 17(10), 7155–7164. https://doi.org/10.1109/TII.2020.3042872 (2021).
19. Yang, W., Wei, Y., Wei, H., Chen, Y., Huang, G., Li, X., & Kang, B. (2023). Survey on explainable AI: From approaches, limitations
and applications aspects. Human-Centric Intelligent Systems, 3(3), 161–188. https://doi.org/10.1007/s44230-023-00038-y
20. Kabir, M. H., Hasan, K. F., Hasan, M. K., & Ansari, K. (2022). Explainable artificial intelligence for smart city application: A
secure and trusted platform. In Explainable Artificial Intelligence for Cyber Security: Next Generation Artificial Intelligence (pp.
241–263). https://doi.org/10.1007/978-3-030-96630-0_11
21. Jagatheesaperumal, S. K. et al. Explainable AI over the Internet of Things (IoT): Overview, state-of-the-art and future directions.
IEEE Open Journal of the Communications Society 3, 2106–2136. https://doi.org/10.1109/OJCOMS.2022.3215676 (2022).
22. Javed, A. R. et al. A survey of explainable artificial intelligence for smart cities. Electronics 12(4), 1020. h t t p s : // d o i . o r g / 10 . 3 3 9 0 / e l e
c t r o n i c s 1 20 4 1 0 2 0 (2023).
23. Saleem, M. et al. Secure and transparent mobility in smart cities: Revolutionizing AVNs to predict traffic congestion using
MapReduce, Private Blockchain and XAI. IEEE Access https://doi.org/10.1109/ACCESS.2024.3458983 (2024).
24. Olateju, O., Okon, S. U., Olaniyi, O. O., Samuel-Okon, A. D. & Asonze, C. U. Exploring the concept of explainable AI and
developing information governance standards for enhancing trust and transparency in handling customer data. SSRN h t tp s : / / d o i .
or g / 1 0 . 9 7 3 4/ j e r r / 2 0 2 4/ v 2 6 i 7 1 2 0 6 (2024).
25. Madhav, A. S., & Tyagi, A. K. (2022). Explainable Artificial Intelligence (XAI): Connecting artificial decision-making and human
trust in autonomous vehicles. In Proceedings of Third International Conference on Computing, Communications, and Cyber-
Security (pp. 123–136). https://doi.org/10.1007/978-981-19-1142-2_10
26. Senevirathna, T. et al. A survey on XAI for 5G and beyond security: Technical aspects, challenges and research directions. IEEE
Commun. Surv. Tutor. https://doi.org/10.1109/COMST.2024.3437248 (2024).
27. Zhang, Z., Al Hamadi, H., Damiani, E., Yeun, C. Y. & Taher, F. Explainable artificial intelligence applications in cyber security:
State-of-the-art in research. IEEE Access 10, 93104–93139. https://doi.org/10.1109/ACCESS.2022.3204051 (2022).
Scientific Reports | (2026) 16:14180 | https://doi.org/10.1038/s41598-026-43440-9 30

www.nature.com/scientificreports/
28. Jayanthi, S., Kumar, N. S., Balashivudu, U., Purushotham, M., & Jeeva, S. (2024). An explorative study of explainable AI and
blockchain integration in public administration. In Applications of Blockchain and Artificial Intelligence in Finance and
Governance (pp. 230–271). CRC Press. https://doi.org/10.1007/978-3-031-72234-9_3
29. Akhtar, M. A. K., Kumar, M., & Nayyar, A. (2024). Socially Responsible Applications of Explainable AI. In Towards Ethical and
Socially Responsible Explainable AI: Challenges and Opportunities (pp. 261–350). https://doi.org/10.1007/978-3-031-66489-2_9
30. Rane, N., Choudhary, S., & Rane, J. (2023). Explainable Artificial Intelligence (XAI) approaches for transparency and accountability
in financial decision-making. SSRN 4640316. https://doi.org/10.2139/ssrn.4640316
31. Banerjee, G., Dhar, S., Roy, S., Syed, R., & Das, A. (2024). Explainability and Transparency in Designing Responsible AI Applications
in the Enterprise. In The International Conference on Computing, Communication, Cybersecurity & AI (pp. 420–431). h t tp s : / / d o i .
or g / 1 0 . 1 0 0 7/ 9 7 8 - 3 - 0 3 1- 7 4 4 4 3 - 3 _ 2 5
32. Long, X., Cai, W., Yang, L. & Huang, H. Improved particle swarm optimization with reverse learning and neighbor adjustment for
space surveillance network task scheduling. Swarm Evol. Comput. 85, 101482. https://doi.org/10.1016/j.swevo.2024.101482 (2024).
33. Luo, J., Wang, G., Li, G. & Pesce, G. Transport infrastructure connectivity and conflict resolution: A machine learning analysis.
Neural Comput. Appl. 34(9), 6585–6601. https://doi.org/10.1007/s00521-021-06015-5 (2022).
34. Liu, S., Shen, Y., Yuan, J., Wu, C. & Yin, R. Storage-aware joint user scheduling and bandwidth allocation for federated edge
learning. IEEE Trans. Cognit. Commun. Netw. 11(1), 581–593. https://doi.org/10.1109/TCCN.2024.3451711 (2025).
35. Feng, S. et al. A Cross Q-Learning assisted resource allocation for user-centric optical wireless communication networks. IEEE
Trans. Green Commun. Netw. 9(4), 2264–2278. https://doi.org/10.1109/TGCN.2025.3553202 (2025).
Acknowledgements
The authors extend their appreciation to the Deanship of Research and Graduate Studies at King Khalid Univer-
sity for funding this work through Large Research Project under grant number RGP2/182/46.
Author contributions
Mohammed M. Alammar: Conceptualization; Methodology; Software;Investigation; Writing – Original Draft.
Abdulrahman Al Ayidh: Formal Analysis; Validation; Visualization; Writing – Review & Editing.Muneer P:
Software Development; Simulation Setup; Data Curation; Resources.Mohamed Abd Elhamid Abbas: Concep-
tualization; Methodology; Software; Investigation; Writing – Original DraftAll authors have read and approved
the fi nal manuscript.
Funding
This research was funded by King Khalid University, Kingdom of Saudi Arabia, under the Research Grant Pro-
gram RGP.2/182/46. The authors express their sincere appreciation to the university for its financial and techni-
cal support, which made this work possible.
Declarations
Competing interests
The authors declare no competing interests.
Additional information
Supplementary Information The online version contains supplementary material available at h t t p s : / / do i . o r g / 1
0 .1 0 3 8 / s 4 1 5 98 - 0 2 6 - 4 3 4 40 - 9 .
Correspondence and requests for materials should be addressed to M.A.
Reprints and permissions information is available at www.nature.com/reprints.
Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and
institutional affiliations.
Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives
4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in
any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide
a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have
permission under this licence to share adapted material derived from this article or parts of it. The images or
other third party material in this article are included in the article’s Creative Commons licence, unless indicated
otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence
and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to
obtain permission directly from the copyright holder. To view a copy of this licence, visit h t t p: / / c r e a t i ve c o m m o
n s . or g / l i c e n s es / b y - n c - n d / 4 . 0 / .
© The Author(s) 2026
Scientific Reports | (2026) 16:14180 | https://doi.org/10.1038/s41598-026-43440-9 31