---

## name: summary-paiva-2026
paper_id: "10.1016/j.cosrev.2025.100720"
designation: algorithm-specific
parent_title: "The emergence of LLM-based Agents: A survey on architectural designs and evaluation"
summary_version: "1.0"

# Executive Summary: LLM-based Agent Architectures

## 1. Core Logic & Research Intent

The paper addresses the functional gap between passive Large Language Models (LLMs) and active autonomous agents. The primary objective is to systematize the transition from text-prediction models to goal-oriented entities capable of perception, reasoning, and environmental interaction. This is achieved by wrapping the "LLM brain" in a multi-modular framework.

## 2. Technical Architecture (The Agent Blueprint)

The survey defines a standard 4-pillar architecture for autonomous agents:

* **Profiling Module**: Establishes the agent's persona and domain expertise through "role-playing" prompts.
* **Memory Module**:
* **Short-term**: Managed via the LLM's context window.
* **Long-term**: Implemented through external vector databases for persistent knowledge retrieval.


* **Planning Module**: Breaks complex goals into sub-tasks using Chain of Thought (CoT), Tree of Thoughts (ToT), and self-reflection loops.
* **Action Module**: Executes decisions through tool utilization (APIs, code interpreters) and direct environment interaction.

## 3. Taxonomy of Systems

The paper categorizes current developments into three distinct operational scales:

| Scale | Focus | Notable Frameworks |
| --- | --- | --- |
| **Single-Agent** | Individual task reasoning | AutoGPT, BabyAGI |
| **Multi-Agent** | Collaborative/Competitive logic | MetaGPT, ChatDev |
| **Human-Agent** | Interactive problem solving | Interactive Simulacra |

## 4. Evaluation & Critical Constraints

Evaluation shifts from static linguistic metrics to dynamic performance benchmarks:

* **Methodology**: Utilizes "LLM-as-a-Judge" (e.g., GPT-4 grading smaller agents) and benchmark suites like AgentBench.
* **Critical Bottlenecks**: The study identifies three primary inhibitors to agent scaling: context window saturation, the risk of "hallucinated" tool calls, and the ethical implications of autonomous action.

## 5. Conclusion

LLM-based agents represent a fundamental shift toward Artificial General Intelligence (AGI) by providing LLMs with the "body" (tools) and "memory" (history) required for complex autonomy.