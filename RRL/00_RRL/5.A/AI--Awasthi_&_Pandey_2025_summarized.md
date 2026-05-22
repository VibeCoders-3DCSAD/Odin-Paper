# How reinforcement learning can drive personalized financial wellness

## Metadata

```yaml
---
paper_id: "10.30574/ijsra.2025.15.1.1244"
designation: algorithm-specific
title: "How reinforcement learning can drive personalized financial wellness"
authors: "Pandey, V.; Awasthi, V."
year: 2025
venue: "International Journal of Science and Research Archive"
odin_topics: ["5.A", "5.C", "7.B", "7.C", "11.B"]
shorthand_tags: ["/profiling-role", "/profile-dimensions", "/classification-vs-clustering", "/budget-rec-approaches", "/budget-rec-formulation", "/budget-rec-algo-candidates", "/budget-rec-algo-tradeoffs", "/value-driven-retention"]
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

A DQN-based reinforcement learning agent, combined with K‑Means user personas and GPT‑powered conversation, learns personalized saving recommendations that outperform baseline strategies in a simulated personal finance environment.

## Problem and Motivation

Many individuals struggle to save, invest, and budget effectively, yet traditional tools and robo‑advisors offer generic, one‑size‑fits‑all advice. Poor financial planning leads to low emergency savings and persistent debt, undermining long‑term financial wellness. Prior AI systems lacked a mechanism to dynamically learn optimal choices from a user’s own behavior over time.

## Approach

- **Problem formulation:** Personal finance management modeled as a Markov Decision Process (MDP) with monthly timesteps. State includes savings and month index; actions are discrete saving amounts (e.g., $0–$50); reward is final net savings after 12 months.
- **RL algorithm:** Deep Q‑Network (DQN) with experience replay and target network. Uses ε‑greedy exploration and a simple multi‑layer perceptron to approximate Q‑values.
- **User personas:** K‑Means clustering on synthetic user data (income + saving rate) creates three personas (low‑income/low‑saver, mid‑income/moderate, high‑income/high‑saver). Persona label augments the agent’s state.
- **Conversational interface:** OpenAI GPT‑4 API translates RL recommendations into natural language, injects persona‑aware tone, and handles user questions.
- **Environment simulation:** 12‑month episodes with monthly income $100, mandatory expenses $50, 10% shock probability ($30 unexpected expense). Sparse reward (final savings only).
- **Baselines:** Compare learned policy against “save $0” and “always save $50” strategies.

## Findings

1. The learned DQN policy achieved an **average final savings of ~$450** across test episodes, significantly outperforming the “save $0” baseline (often negative) and closing the gap to the ideal “always save $50” benchmark (~$564 expected).
2. Training curves (Figure 2) show average episode reward rising from ~$20 to **$100–$120** over 5,000 episodes, demonstrating clear learning.
3. Persona clustering (Figure 1) produced interpretable groups, enabling persona‑conditioned policies (e.g., debt‑averse reward shaping for low‑income users).

- The conversational agent successfully wrapped numeric recommendations (e.g., “save $50”) into empathetic, persona‑appropriate explanations with follow‑up engagement questions.

## Key Figures and Tables

- Figure 1: Scatter plot of synthetic users colored by K‑Means cluster → three distinct personas (low‑income low‑saver, mid‑income moderate, high‑income high‑saver) with centroids marked.
- Figure 2: Training performance (moving average of final episode reward over 5,000 episodes) → reward increases steadily from near zero to ~$100–$120, with variability due to shocks and exploration.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| RL | Reinforcement Learning – an agent learns by trial and error to maximize long‑term reward. |
| DQN | Deep Q‑Network – a neural network that estimates the future reward of each action in a given state. |
| MDP | Markov Decision Process – a mathematical framework for sequential decision making with states, actions, rewards, and transitions. |
| NLP | Natural Language Processing – enabling computers to understand and generate human language. |
| GPT | Generative Pre‑trained Transformer – a large language model used for conversational AI. |
| K‑Means | An unsupervised clustering algorithm that groups data points into k clusters by minimizing within‑cluster distances. |
| PFWA | Personalized Financial Wellness Agent – the proposed end‑to‑end system combining RL, clustering, and NLP. |

## Critical Citations

- [Mnih et al., 2015] – Introduced DQN and demonstrated human‑level control in Atari; foundational for the RL approach used here.
- [Schlosky et al., 2024] – Showed ChatGPT generates reasonable but generic financial tips, motivating the need for personalization via RL.
- [D’Acunto & Rossi, 2021] – Survey of robo‑advising limitations, cited to justify moving beyond portfolio allocation into budgeting and debt management.

## Relevance to Odin

**Topics:**

5.A — Financial Behavioral Profiles in Personal Finance

5.C — Financial Behavioral Profile Classification Algorithm

7.B — Budget Recommendation in Personal Finance Systems

7.C — Budget Recommendation Algorithm

11.B — Retention Mechanisms and Engagement Design

**Contribution to Odin:**

This paper directly justifies Odin’s use of unsupervised clustering (K‑Means) to build user personas from behavioral data (income, saving rate), enabling the system to tailor financial recommendations from the start — even before observing a new user’s transaction history. The MDP formulation of personal finance as a sequential decision problem provides a formal blueprint for Odin’s budget recommendation module, where actions (e.g., how much to save or allocate to a category) are learned to maximize long‑term financial wellness rather than following static rules. The integration of a conversational AI (GPT) as an interface layer demonstrates how Odin can explain recommendations in natural language, adapt tone to persona, and potentially collect user feedback — a mechanism shown to boost engagement and trust, directly supporting Odin’s value‑driven retention strategy.

**Directly justifies:**

- “Unsupervised clustering (K‑Means) on behavioral features (income, saving rate) produces interpretable user personas that can condition a recommendation policy, addressing the cold‑start problem in financial profiling.”
- “Deep Q‑Network (DQN) learns saving policies that improve final savings by >$400 over a naive baseline in a stochastic monthly budgeting environment, proving RL’s applicability to personal finance decision support.”
- “A conversational AI interface powered by GPT‑4 can translate RL numeric actions into empathetic, persona‑aware advice, improving user engagement and perceived trust without requiring fine‑tuning.”
- “Reward shaping in the MDP (e.g., penalizing debt for a low‑income persona) allows a single RL agent to produce different behaviors for different user types, enabling personalization without separate models.”

**Limits of relevance:**

- The simulated environment is highly simplified (fixed income, only one discretionary spending category, binary shock). Real‑world deployment would require more complex state and action spaces (multiple spending categories, debt vs. saving trade‑offs).
- User personas derived only from income and saving rate; Odin’s profiling should incorporate additional dimensions (e.g., spending volatility, family obligations, financial goals).
- No evaluation on real user data or live deployment; performance claims are from a synthetic environment.
- The paper does not address manual transaction entry (Odin’s scope) vs. API‑based data ingestion, which may affect state update frequency and data completeness.

## Limitations

- Environment and user data are entirely synthetic; external validity to real Filipino young professionals is unproven.
- The action space only controls saving amount; no joint actions for debt repayment, investment, or category‑level budgeting. [unacknowledged]
- Reward is final net savings only — does not penalize extreme frugality or user discomfort, which could lead to unrealistic recommendations.
- DQN with a discretized state table was used for the core experiment; the paper mentions neural DQN but does not provide comparative results. [unacknowledged]
- No user study or engagement metrics; the claim that conversational AI boosts trust is argued from prior literature, not measured.

## Remember This

- 🔑 **+$430 average final savings** — RL agent learned to beat naive baseline by a large margin in a 12‑month stochastic simulation.
- 📌 K‑Means on income + saving rate produced three clean personas — cheap, interpretable cold‑start profiling for Odin.
- 💡 GPT‑4 translates RL actions into empathetic, persona‑aware chat — retention mechanism without gamification.
- ⚠️ Synthetic environment only — real‑world income volatility, multiple categories, and manual entry not tested.
