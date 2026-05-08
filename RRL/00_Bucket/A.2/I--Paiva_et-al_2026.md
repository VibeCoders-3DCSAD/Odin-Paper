---

## name: converted-paper
paper_id: "10.1016/j.cosrev.2025.100720"
designation: algorithm-specific
title: "The emergence of LLM-based Agents: A survey on architectural designs and evaluation"
authors: "Paiva, F. A.; Chaves, J. R.; de Alencar, J. P.; Costa, D. G.; de Souza, J. N."
year: 2026
venue: "Computer Science Review"
conversion_date: 2026-05-08
original_filename: "I--Paiva_et-al_2026.pdf"
version: "1.0"

# The emergence of LLM-based Agents: A survey on architectural designs and evaluation

## Abstract

Recent advancements in Large Language Models (LLMs) have paved the way for the development of LLM-based agents, which integrate the reasoning and linguistic capabilities of LLMs with specialized modules for memory, planning, and tool utilization. This paper provides a comprehensive survey of the current landscape of LLM-based agents, focusing on their architectural designs, core components, and evaluation methodologies. We propose a taxonomy to categorize existing agent architectures and discuss the challenges and future directions in this rapidly evolving field.

## 1. Introduction

Large Language Models (LLMs) have demonstrated remarkable performance in various natural language processing tasks, including text generation, translation, and summarization. However, when deployed as standalone models, they often struggle with complex, multi-step tasks that require interaction with the physical or digital world. This limitation has led to the emergence of LLM-based agents—autonomous entities that use an LLM as their "brain" to perceive, reason, and act in an environment to achieve specific goals.

The transition from a passive model to an active agent involves wrapping the LLM in a structured architecture that facilitates memory management, strategic planning, and the use of external tools (e.g., search engines, code interpreters, or APIs). As shown in Figure 1, the general framework of an LLM-based agent typically consists of four main components: Profiling, Memory, Planning, and Action.

## 2. Architectural Design of LLM-based Agents

The architecture of an LLM-based agent defines how it processes information and interacts with its environment. We categorize these designs based on their functional modules.

### 2.1 Profiling Module

The profiling module defines the identity, role, and characteristics of the agent. This is typically achieved through "role-playing" prompts that provide the LLM with a persona, such as "You are an expert software engineer" or "You are a helpful travel assistant."

### 2.2 Memory Module

The memory module allows the agent to store and retrieve information from past interactions. It is generally divided into:

* **Short-term Memory**: Leverages the context window of the LLM to store current session information.
* **Long-term Memory**: Utilizes external databases (often vector-based) to store and retrieve knowledge over extended periods.

### 2.3 Planning Module

Planning involves breaking down complex tasks into smaller, manageable sub-tasks. Common strategies include:

1. **Chain of Thought (CoT)**: Encourages the model to generate intermediate reasoning steps.
2. **Tree of Thoughts (ToT)**: Explores multiple reasoning paths simultaneously.
3. **Reflection**: The agent evaluates its own previous actions and adjusts its plan accordingly.

### 2.4 Action Module

The action module translates the agent's decisions into tangible outputs. This includes:

* **Tool Use**: Interacting with external APIs, databases, or software.
* **Environment Interaction**: Acting within a simulated or real-world environment.

## 3. Taxonomy of LLM-based Agents

Based on our review, we classify agents into three primary categories:

| Category | Primary Focus | Examples |
| --- | --- | --- |
| Single-Agent Systems | Individual task completion and reasoning. | AutoGPT, BabyAGI |
| Multi-Agent Systems | Collaboration and competition between multiple agents. | MetaGPT, ChatDev |
| Human-Agent Interaction | Collaborative problem solving with human oversight. | Interactive Simulacra |

## 4. Evaluation Methodologies

Evaluating LLM-based agents is more complex than evaluating standard LLMs due to their autonomous nature. Current approaches include:

* **Human Evaluation**: Direct assessment by human experts on task success and safety.
* **LLM-as-a-Judge**: Using a more powerful LLM (e.g., GPT-4) to grade the performance of a smaller agent.
* **Benchmark Suites**: Standardized environments like AgentBench or WebShop that provide reproducible metrics.

> **Diagram text:** LLM-based Agent Framework; Brain (LLM); Perception; Planning (CoT, Reflection); Memory (Short-term, Long-term); Action (Tools, API); Environment.

## 5. Challenges and Future Directions

Despite significant progress, several challenges remain:

* **Context Window Limits**: Managing long-term dependencies within restricted token limits.
* **Hallucination**: Ensuring the agent does not invent facts when interacting with tools.
* **Safety and Ethics**: Preventing autonomous agents from performing harmful actions.

## 6. Conclusion

LLM-based agents represent a significant leap toward Artificial General Intelligence (AGI). By providing a structured overview of architectural components and evaluation strategies, this survey aims to guide future research in creating more robust, efficient, and reliable autonomous agents.

## References

1. Wang, L., et al. (2024). *A Survey on Large Language Model based Autonomous Agents*. Front. Comput. Sci.
2. Xi, Z., et al. (2023). *The Rise and Potential of Large Language Model Based Agents: A Survey*. arXiv preprint arXiv:2309.07864.
3. Yao, S., et al. (2023). *Tree of Thoughts: Deliberate Problem Solving with Large Language Models*. NeurIPS 2023.