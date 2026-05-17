# Multi-agent reinforcement learning for resources allocation optimization: a survey

## Metadata

```yaml
---
paper_id: "10.1007/s10462-025-11340-5"
designation: international
title: "Multi-agent reinforcement learning for resources allocation optimization: a survey"
authors: "Hady, M. A.; Hu, S.; Pratama, M.; Cao, Z.; Kowalczyk, R."
year: 2025
venue: "Artificial Intelligence Review"
odin_topics: ["4.A", "7.B", "7.C", "12.A", "12.B"]
shorthand_tags: ["/pfms-intelligent-features", "/budget-rec-approaches", "/constraint-allocation", "/budget-rec-formulation", "/budget-rec-algo-candidates", "/budget-rec-algo-tradeoffs", "/eval-frameworks-survey", "/eval-ml-design"]
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[X]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
---
```

## TL;DR

Multi-agent reinforcement learning enables decentralized, adaptive resource allocation across telecommunications, energy, computing, transportation, and manufacturing, outperforming classical optimization in dynamic environments.

## Problem and Motivation

Classical RAO methods (linear programming, heuristics, game theory) lack scalability and adaptability for modern dynamic, decentralized systems. This limits real-time resource allocation in domains like cloud computing, smart grids, and IoT networks where conditions change rapidly. No prior survey had comprehensively mapped MARL algorithms to RAO challenges across multiple industries with a unified framework.

## Approach

- Scope: 126+ papers on MARL for RAO from telecommunications, energy, distributed computing, transportation, and manufacturing.
- Classification: Resources categorized by divisibility (discrete/continuous), availability (renewable/non-renewable), and location (distributed/non-distributed).
- RAO formulation: General optimization problem with objective function and constraints (Equation 1).
- MARL foundations: Markov Decision Process, Stochastic Games, Dec-POMDP, and three learning paradigms (CTCE, DTDE, CTDE).
- Algorithm comparison: Evaluated on adaptability, scalability, distributional training, and heterogeneity.
- Challenge mapping: Four primary RAO challenges (adaptability, partial observability, scalability, heterogeneity) and corresponding MARL solutions.
- Benchmarks: Reviewed available simulators (BSK-RL for satellites, power grid networks, CityFlow for traffic, ContainerGym).
- Future directions: Scalability, sim-to-real gap, safety, trustworthiness, and integration with federated learning, transformers, digital twins.

## Findings

- **MARL outperforms classical methods in dynamic RAO environments by enabling continuous adaptation and decentralized execution**.
- CTDE (centralized training, decentralized execution) is the most widely adopted paradigm, balancing coordination during training with scalable real-time execution.
- DTDE scales best to large agent populations but lacks coordination; CTCE is limited to small-scale controlled settings due to scalability and privacy constraints.
- Partial observability in RAO is addressed via CTDE with centralized critics or value decomposition (e.g., QMIX), enabling agents to act on local observations.
- Resource heterogeneity (e.g., CPU, memory, bandwidth) is handled by CTDE with credit assignment, allowing agents to balance multiple objectives.
- Available RAO benchmarks (BSK-RL, power grid, CityFlow, ContainerGym) are limited by realism, availability, and sim-to-real transfer gaps.

## Key Figures and Tables

- Figure 1: MARL solution for RAO framework → agents allocate resources based on rewards and observations.
- Figure 2: Survey structure → preliminary fundamentals → RAO classical methods → MARL solutions → benchmarks.
- Figure 3: Resource classification by divisibility, availability, location → discrete vs. continuous, renewable vs. non-renewable, distributed vs. non-distributed.
- Table 5: MARL algorithms across applications with primary challenges → adaptability and partial observability dominate telecommunications and energy.
- Table 6: MARL paradigm comparison (CTCE, DTDE, CTDE) on adaptability, scalability, distributional training, heterogeneity → DTDE and advanced CTDE score highest.

## Key Equations

$$\sum_{i=1}^{n} x_i \leq N, \quad l_i \leq x_i \leq u_i$$
*Resource allocation constraint: total resource N distributed across tasks with lower/upper bounds.*

$$Q(s,a) = \sum_{s'} p(s'|s,a)[r(s,a,s') + \gamma \max_{a'} Q(s',a')]$$
*Bellman optimality equation for Q-learning, balancing immediate reward and future value.*

$$\nabla_\theta J(\theta) = \mathbb{E}_\pi \left[ \sum_{t=0}^{T} \nabla_\theta \log \pi(a_t|s_t;\theta) G_t \right]$$
*Policy gradient updates toward actions that yield higher cumulative reward G_t.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| MARL | Multi-Agent Reinforcement Learning: multiple agents learn policies through interaction in shared environment. |
| RAO | Resource Allocation Optimization: distributing finite resources to maximize efficiency or fairness. |
| CTCE | Centralized Training and Centralized Execution: single controller uses global state to decide all agents' actions. |
| DTDE | Decentralized Training and Decentralized Execution: each agent learns and acts independently from local observations. |
| CTDE | Centralized Training and Decentralized Execution: agents train with global info but execute using local policies (most common for RAO). |
| Dec-POMDP | Decentralized Partially Observable Markov Decision Process: cooperative multi-agent framework with partial observability. |
| MDP | Markov Decision Process: single-agent decision-making with states, actions, rewards, and transitions. |

## Critical Citations

- [Bu et al., 2008] — Comprehensive survey of multiagent reinforcement learning fundamentals.
- [Lowe et al., 2017] — MADDPG algorithm, foundational CTDE with centralized critic.
- [Rashid et al., 2020] — QMIX, key value decomposition method for cooperative MARL.
- [Sutton and Barto, 2018] — Standard textbook on reinforcement learning.

## Relevance to Odin

**Topics:**

4.A — Landscape of Existing Personal Finance Systems

7.B — Budget Recommendation in Personal Finance Systems

7.C — Budget Recommendation Algorithm

12.A — Evaluation Frameworks for Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This survey directly informs Odin's budget recommendation module by framing budget allocation as a resource allocation optimization problem with constraints (income, category floors/ceilings). The comparison of MARL paradigms (CTCE, DTDE, CTDE) provides justification for algorithm selection — CTDE's balance of centralized training and decentralized execution maps to Odin's need to learn from global user data while running locally on mobile devices. Although Odin is a single-user system (not multi-agent), the paper's treatment of constraint-based allocation, objective functions, and credit assignment across heterogeneous resources offers transferable design patterns for allocating budget across spending categories. The survey's evaluation benchmarks and simulator review also guide Odin's testing methodology using ISO 25010 and SUS.

**Directly justifies:**

- "Constraint-based resource allocation formulated as maximizing an objective subject to upper and lower bounds (Equation 1) directly applies to budget recommendation where income is total resource N and category floors/ceilings are l_i and u_i."
- "Centralized Training with Decentralized Execution (CTDE) is the most widely adopted MARL paradigm for RAO because it balances coordination during training with scalable real-time execution — applicable to learning a global budget policy that runs locally on a user's device."
- "MARL algorithms (MADDPG, MAPPO, MAAC) outperform classical linear programming and heuristics in dynamic, partially observable resource allocation environments, supporting the use of learning-based methods over static budget templates."
- "Evaluating RAO algorithms requires standardized benchmarks and metrics such as resource utilization, task success rate, and fairness — directly transferable to budget recommendation evaluation using adherence rate and user retention."

**Limits of relevance:**

- The paper focuses on industrial RAO (telecom, energy, transportation) not personal finance; budget allocation differs in scale and objective complexity.
- MARL assumes multiple autonomous agents; Odin is a single-user system with multiple categories, requiring adaptation of credit assignment concepts.
- No empirical comparison of MARL against simple heuristic budgeting strategies in a personal finance context.
- The surveyed benchmarks (satellite, power grid, traffic) do not simulate human spending behavior or financial constraints.

## Limitations

- The survey does not provide quantitative meta-analysis or performance rankings of MARL algorithms across RAO tasks. [unacknowledged]
- Limited discussion of computational resource requirements for deploying MARL on mobile devices (relevant to Odin's mobile-first constraint). [unacknowledged]
- The authors acknowledge the sim-to-real gap but offer no concrete solutions for bridging it.
- Most reviewed papers use simulated environments; real-world validation is sparse.
- The survey excludes personal finance and consumer budgeting domains entirely.

## Remember This

- 🔑 MARL enables decentralized resource allocation without a central controller — scales to hundreds of agents.
- 📌 CTDE (centralized training, decentralized execution) is the dominant paradigm for dynamic RAO.
- ⚠️ No personal finance applications surveyed — direct transfer requires adapting multi-agent concepts to single-user category allocation.
- 💡 RAO formulation (Eq. 1) maps directly to budget recommendation: total income N, category bounds l_i and u_i.
- 🔍 Available benchmarks (BSK-RL, CityFlow, ContainerGym) lack personal finance scenarios — Odin will need custom evaluation.
